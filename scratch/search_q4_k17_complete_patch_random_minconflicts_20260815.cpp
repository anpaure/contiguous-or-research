#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <mutex>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>

namespace {

struct Column {
  int pair_index = -1;
  std::array<int, 10> row{};
};

struct Graph {
  std::string path;
  int self_left = -1;
  int self_right = -1;
  std::vector<int> global_row;
  std::vector<Column> column;
  std::vector<std::vector<int>> incidence;
};

std::vector<int> csv(const std::string& text) {
  std::vector<int> result;
  std::istringstream input(text);
  std::string item;
  while (std::getline(input, item, ','))
    if (!item.empty()) result.push_back(std::stoi(item));
  return result;
}

Graph read_graph(const std::string& path) {
  std::ifstream input(path);
  if (!input) throw std::runtime_error("cannot open graph " + path);
  Graph graph;
  graph.path = path;
  std::string line;
  if (!std::getline(input, line)) throw std::runtime_error("missing self header");
  {
    std::istringstream row(line);
    std::string hash, label;
    row >> hash >> label >> graph.self_left >> graph.self_right;
    if (hash != "#" || label != "self") throw std::runtime_error("bad self header");
  }
  if (!std::getline(input, line)) throw std::runtime_error("missing row header");
  {
    std::istringstream row(line);
    std::string hash, label, values;
    row >> hash >> label >> values;
    if (hash != "#" || label != "rows") throw std::runtime_error("bad row header");
    graph.global_row = csv(values);
  }
  if (graph.global_row.size() != 200) throw std::runtime_error("expected 200 residual rows");
  std::array<int, 680> local;
  local.fill(-1);
  for (int i = 0; i < 200; ++i) local.at(graph.global_row.at(i)) = i;
  if (!std::getline(input, line) || line != "pair_index\trows")
    throw std::runtime_error("bad column header");
  while (std::getline(input, line)) {
    if (line.empty()) continue;
    const std::size_t tab = line.find('\t');
    if (tab == std::string::npos) throw std::runtime_error("bad column line");
    Column column;
    column.pair_index = std::stoi(line.substr(0, tab));
    const auto rows = csv(line.substr(tab + 1));
    if (rows.size() != 10) throw std::runtime_error("column does not have ten rows");
    for (int i = 0; i < 10; ++i) {
      const int mapped = local.at(rows.at(i));
      if (mapped < 0) throw std::runtime_error("column row outside residual set");
      column.row.at(i) = mapped;
    }
    std::sort(column.row.begin(), column.row.end());
    if (std::adjacent_find(column.row.begin(), column.row.end()) != column.row.end())
      throw std::runtime_error("duplicate row in column");
    graph.column.push_back(column);
  }
  graph.incidence.assign(200, {});
  for (int index = 0; index < static_cast<int>(graph.column.size()); ++index)
    for (int row : graph.column.at(index).row) graph.incidence.at(row).push_back(index);
  for (const auto& incidence : graph.incidence)
    if (incidence.empty()) throw std::runtime_error("graph has an uncovered row");
  return graph;
}

int swap_delta(const std::array<int, 200>& load, const Column& outgoing,
               const Column& incoming) {
  std::array<int, 20> touched{};
  std::array<int, 20> change{};
  int count = 0;
  auto add = [&](int row, int value) {
    for (int i = 0; i < count; ++i) {
      if (touched.at(i) == row) {
        change.at(i) += value;
        return;
      }
    }
    touched.at(count) = row;
    change.at(count) = value;
    ++count;
  };
  for (int row : outgoing.row) add(row, -1);
  for (int row : incoming.row) add(row, 1);
  int delta = 0;
  for (int i = 0; i < count; ++i) {
    const int old_value = load.at(touched.at(i)) - 1;
    const int new_value = load.at(touched.at(i)) + change.at(i) - 1;
    delta += new_value * new_value - old_value * old_value;
  }
  return delta;
}

struct Best {
  int energy = std::numeric_limits<int>::max();
  int graph = -1;
  std::vector<int> chosen;
  std::array<int, 200> load{};
  std::uint64_t thread = 0;
};

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc < 6)
      throw std::runtime_error("usage: seconds threads seed result.json graph.tsv ...");
    const double seconds = std::stod(argv[1]);
    const int thread_count = std::stoi(argv[2]);
    const std::uint64_t seed = std::stoull(argv[3]);
    const std::string result_path = argv[4];
    std::vector<Graph> graphs;
    for (int i = 5; i < argc; ++i) graphs.push_back(read_graph(argv[i]));
    if (graphs.empty() || thread_count <= 0) throw std::runtime_error("empty work set");

    const auto started = std::chrono::steady_clock::now();
    const auto deadline = started + std::chrono::duration<double>(seconds);
    std::atomic<bool> stop{false};
    std::atomic<int> best_energy{std::numeric_limits<int>::max()};
    std::atomic<std::uint64_t> restarts{0};
    std::atomic<std::uint64_t> iterations{0};
    Best best;
    std::mutex best_mutex;

    auto worker = [&](int thread_id) {
      std::mt19937_64 random(seed ^ (0x9e3779b97f4a7c15ULL * (thread_id + 1)));
      std::uint64_t local_restart = 0;
      while (!stop.load(std::memory_order_relaxed) &&
             std::chrono::steady_clock::now() < deadline) {
        const int graph_index = static_cast<int>((thread_id + local_restart) % graphs.size());
        const Graph& graph = graphs.at(graph_index);
        const int n = static_cast<int>(graph.column.size());
        std::uniform_int_distribution<int> random_column(0, n - 1);
        std::array<int, 200> load{};
        std::vector<unsigned char> selected(n, 0);
        std::vector<int> chosen;
        chosen.reserve(20);
        int energy = 200;
        for (int slot = 0; slot < 20; ++slot) {
          int selected_index = -1;
          int selected_delta = std::numeric_limits<int>::max();
          for (int sample = 0; sample < 768; ++sample) {
            const int candidate = random_column(random);
            if (selected.at(candidate)) continue;
            int delta = 0;
            for (int row : graph.column.at(candidate).row) delta += 2 * load.at(row) - 1;
            if (delta < selected_delta ||
                (delta == selected_delta && (random() & 1U))) {
              selected_index = candidate;
              selected_delta = delta;
            }
          }
          if (selected_index < 0) {
            for (int candidate = 0; candidate < n; ++candidate)
              if (!selected.at(candidate)) { selected_index = candidate; break; }
            selected_delta = 0;
            for (int row : graph.column.at(selected_index).row)
              selected_delta += 2 * load.at(row) - 1;
          }
          selected.at(selected_index) = 1;
          chosen.push_back(selected_index);
          for (int row : graph.column.at(selected_index).row) ++load.at(row);
          energy += selected_delta;
        }

        std::vector<int> tabu_until(n, 0);
        int stall = 0;
        for (int step = 1; step <= 12000 && !stop.load(std::memory_order_relaxed); ++step) {
          iterations.fetch_add(1, std::memory_order_relaxed);
          if (energy < best_energy.load(std::memory_order_relaxed)) {
            std::lock_guard<std::mutex> lock(best_mutex);
            if (energy < best.energy) {
              best.energy = energy;
              best.graph = graph_index;
              best.chosen = chosen;
              best.load = load;
              best.thread = thread_id;
              best_energy.store(energy, std::memory_order_relaxed);
              std::cerr << "best=" << energy << " graph=" << graph_index
                        << " restarts=" << restarts.load() << " iterations="
                        << iterations.load() << '\n';
              if (energy == 0) stop.store(true, std::memory_order_relaxed);
            }
          }
          if (energy == 0 || std::chrono::steady_clock::now() >= deadline) break;
          std::array<int, 200> holes{};
          int hole_count = 0;
          for (int row = 0; row < 200; ++row)
            if (load.at(row) == 0) holes.at(hole_count++) = row;
          if (hole_count == 0) break;
          const int hole = holes.at(random() % hole_count);
          const auto& incoming_bank = graph.incidence.at(hole);
          int best_incoming = -1;
          int best_position = -1;
          int best_delta = std::numeric_limits<int>::max();
          const int samples = std::min<int>(160, incoming_bank.size());
          for (int sample = 0; sample < samples; ++sample) {
            const int incoming = incoming_bank.at(random() % incoming_bank.size());
            if (selected.at(incoming)) continue;
            if (tabu_until.at(incoming) > step && best_delta <= 0) continue;
            for (int position = 0; position < 20; ++position) {
              const int outgoing = chosen.at(position);
              const int delta = swap_delta(load, graph.column.at(outgoing),
                                           graph.column.at(incoming));
              if (delta < best_delta || (delta == best_delta && (random() & 1U))) {
                best_delta = delta;
                best_incoming = incoming;
                best_position = position;
              }
            }
          }
          if (best_incoming < 0) { stall = 12000; break; }
          const double temperature = std::max(0.20, 3.0 * (1.0 - stall / 12000.0));
          const double probability = best_delta <= 0 ? 1.0 : std::exp(-best_delta / temperature);
          const double uniform = std::generate_canonical<double, 53>(random);
          if (uniform <= probability || stall > 2500) {
            const int outgoing = chosen.at(best_position);
            for (int row : graph.column.at(outgoing).row) --load.at(row);
            for (int row : graph.column.at(best_incoming).row) ++load.at(row);
            selected.at(outgoing) = 0;
            selected.at(best_incoming) = 1;
            tabu_until.at(outgoing) = step + 12 + static_cast<int>(random() % 37);
            chosen.at(best_position) = best_incoming;
            energy += best_delta;
            if (best_delta < 0) stall = 0; else ++stall;
          } else {
            ++stall;
          }
        }
        // Preserve an improvement made by the final permitted move before restart.
        if (energy < best_energy.load(std::memory_order_relaxed)) {
          std::lock_guard<std::mutex> lock(best_mutex);
          if (energy < best.energy) {
            best.energy = energy;
            best.graph = graph_index;
            best.chosen = chosen;
            best.load = load;
            best.thread = thread_id;
            best_energy.store(energy, std::memory_order_relaxed);
            std::cerr << "best=" << energy << " graph=" << graph_index
                      << " restarts=" << restarts.load() << " iterations="
                      << iterations.load() << '\n';
            if (energy == 0) stop.store(true, std::memory_order_relaxed);
          }
        }
        ++local_restart;
        restarts.fetch_add(1, std::memory_order_relaxed);
      }
    };

    std::vector<std::thread> workers;
    for (int thread = 0; thread < thread_count; ++thread) workers.emplace_back(worker, thread);
    for (auto& worker_thread : workers) worker_thread.join();
    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();

    std::lock_guard<std::mutex> lock(best_mutex);
    if (best.graph < 0) throw std::runtime_error("heuristic produced no state");
    const Graph& graph = graphs.at(best.graph);
    std::vector<int> pair_indices;
    for (int local : best.chosen) pair_indices.push_back(graph.column.at(local).pair_index);
    std::sort(pair_indices.begin(), pair_indices.end());
    int holes = 0, ones = 0, doubles_or_more = 0;
    for (int value : best.load) {
      holes += value == 0;
      ones += value == 1;
      doubles_or_more += value >= 2;
    }
    std::ofstream output(result_path);
    if (!output) throw std::runtime_error("cannot open result path");
    auto emit = [&](std::ostream& stream) {
      stream << "{\n  \"status\": \"" << (best.energy == 0 ? "SAT" : "NO_CERTIFICATE")
             << "\",\n  \"scope\": \"bounded random-greedy min-conflicts/tabu heuristic only\",\n"
             << "  \"elapsed_seconds\": " << elapsed << ",\n"
             << "  \"threads\": " << thread_count << ",\n"
             << "  \"seed\": " << seed << ",\n"
             << "  \"graphs\": " << graphs.size() << ",\n"
             << "  \"restarts\": " << restarts.load() << ",\n"
             << "  \"iterations\": " << iterations.load() << ",\n"
             << "  \"best_energy\": " << best.energy << ",\n"
             << "  \"best_graph_index\": " << best.graph << ",\n"
             << "  \"best_graph\": \"" << graph.path << "\",\n"
             << "  \"self_indices\": [" << graph.self_left << ',' << graph.self_right << "],\n"
             << "  \"load_histogram\": {\"0\": " << holes << ", \"1\": " << ones
             << ", \"2+\": " << doubles_or_more << "},\n"
             << "  \"pair_indices\": [";
      for (std::size_t i = 0; i < pair_indices.size(); ++i) {
        if (i) stream << ',';
        stream << pair_indices.at(i);
      }
      stream << "]\n}\n";
    };
    emit(output);
    emit(std::cout);
    return best.energy == 0 ? 0 : 3;
  } catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what() << '\n';
    return 2;
  }
}
