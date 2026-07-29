// Exact k=15 depth-three compiler Hall + Dulmage--Mendelsohn auditor.
//
// Build:
//   c++ -O3 -march=native -std=c++20 -o scratch/fast_k15_hall_dm \
//       scratch/fast_k15_hall_dm.cpp
//
// The program deliberately has no JSON dependency.  It extracts integer
// arrays from the proof artifacts and emits one compact JSON object per input.

#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <deque>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

int g_k = 15;
int g_depth = 3;
int g_middle_rank = 8;

struct Cell {
  int depth = 0;
  int start = 0;
  uint16_t envelope = 0;
  uint16_t mandatory = 0;
  std::array<uint16_t, 8> masks{};
  int mask_count = 0;
};

struct Graph {
  bool factorable = true;
  int structural_start = -1;
  int structural_coordinate = -1;
  std::vector<uint16_t> allowed;
  std::vector<int> targets;
  std::vector<Cell> cells;
  std::vector<std::vector<int>> adjacency;
};

struct Matching {
  std::vector<int> left;
  std::vector<int> right;
};

struct Audit {
  Graph graph;
  Matching matching;
  std::vector<int> unmatched_indices;
  std::vector<int> zero_indices;
  std::vector<char> dm_left;
  std::vector<char> dm_right;
};

struct DMComponent {
  int core = 0;
  int left = 0;
  int right = 0;
  std::array<int, 16> target_ranks{};
  std::array<int, 9> cell_depths{};
};

std::string read_file(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open " + path);
  std::ostringstream stream;
  stream << input.rdbuf();
  return stream.str();
}

size_t skip_space(const std::string& text, size_t p) {
  while (p < text.size() && std::isspace(static_cast<unsigned char>(text[p]))) ++p;
  return p;
}

std::vector<int> parse_array_at(const std::string& text, size_t p) {
  p = text.find('[', p);
  if (p == std::string::npos) return {};
  ++p;
  std::vector<int> result;
  int nesting = 1;
  while (p < text.size() && nesting) {
    p = skip_space(text, p);
    if (p >= text.size()) break;
    if (text[p] == '[') {
      ++nesting;
      ++p;
      continue;
    }
    if (text[p] == ']') {
      --nesting;
      ++p;
      if (!nesting) break;
      continue;
    }
    if (text[p] == '-' || std::isdigit(static_cast<unsigned char>(text[p]))) {
      bool negative = text[p] == '-';
      if (negative) ++p;
      int value = 0;
      while (p < text.size() && std::isdigit(static_cast<unsigned char>(text[p]))) {
        value = 10 * value + (text[p++] - '0');
      }
      if (nesting == 1) result.push_back(negative ? -value : value);
      continue;
    }
    ++p;
  }
  return result;
}

std::vector<int> extract_named_array(const std::string& text,
                                     const std::vector<std::string>& keys) {
  for (const auto& key : keys) {
    const std::string needle = "\"" + key + "\"";
    size_t p = text.find(needle);
    if (p != std::string::npos) {
      auto result = parse_array_at(text, p + needle.size());
      if (!result.empty()) return result;
    }
  }
  return {};
}

std::vector<int> extract_middle(const std::string& path) {
  const std::string text = read_file(path);
  auto result = extract_named_array(text, {"middle_path", "middle_cycle"});
  if (!result.empty()) return result;

  // middle_components is nested.  Parse the first inner array only.
  size_t p = text.find("\"middle_components\"");
  if (p != std::string::npos) {
    p = text.find('[', p);
    if (p != std::string::npos) {
      p = text.find('[', p + 1);
      if (p != std::string::npos) return parse_array_at(text, p);
    }
  }
  throw std::runtime_error(path + ": no middle path");
}

uint64_t carrier_key(const std::vector<int>& positions) {
  uint64_t key = positions.size();
  for (int p : positions) key = (key << 13) | static_cast<uint64_t>(p + 1);
  return key;
}

Graph build_graph(const std::vector<int>& middle) {
  Graph graph;
  const int n = static_cast<int>(middle.size());
  if (middle.empty()) throw std::runtime_error("empty middle path");
  g_middle_rank = std::popcount(static_cast<unsigned>(middle.front()));
  const uint16_t full = static_cast<uint16_t>((1u << g_k) - 1);
  graph.allowed.reserve(n + g_depth);
  for (int i = 0; i < n + g_depth; ++i) {
    uint16_t value = full;
    for (int j = std::max(0, i - g_depth); j <= std::min(i, n - 1); ++j) {
      value &= static_cast<uint16_t>(middle[j]);
    }
    graph.allowed.push_back(value);
  }

  std::unordered_map<uint64_t, uint16_t> carrier_required;
  carrier_required.reserve(static_cast<size_t>(n) * 4);
  for (int start = 0; start < n; ++start) {
    const uint16_t target = static_cast<uint16_t>(middle[start]);
    for (int x = 0; x < g_k; ++x) {
      const uint16_t bit = static_cast<uint16_t>(1u << x);
      if (!(target & bit)) continue;
      std::vector<int> carriers;
      for (int p = start; p <= start + g_depth; ++p) {
        if (graph.allowed[p] & bit) carriers.push_back(p);
      }
      if (carriers.empty()) {
        graph.factorable = false;
        graph.structural_start = start;
        graph.structural_coordinate = x;
        return graph;
      }
      carrier_required[carrier_key(carriers)] |= bit;
    }
  }

  std::vector<int> target_index(1 << g_k, -1);
  for (int value = 1; value < (1 << g_k); ++value) {
    if (std::popcount(static_cast<unsigned>(value)) < g_middle_rank) {
      target_index[value] = static_cast<int>(graph.targets.size());
      graph.targets.push_back(value);
    }
  }
  graph.adjacency.resize(graph.targets.size());
  graph.cells.reserve(g_depth * n + g_depth * g_depth);

  for (int row_depth = 0; row_depth < g_depth; ++row_depth) {
    for (int start = 0; start < static_cast<int>(graph.allowed.size()) - row_depth;
         ++start) {
      Cell cell;
      cell.depth = row_depth;
      cell.start = start;
      cell.mask_count = row_depth + 1;
      std::vector<int> positions;
      for (int p = start; p <= start + row_depth; ++p) {
        positions.push_back(p);
        cell.masks[p - start] = graph.allowed[p];
        cell.envelope |= graph.allowed[p];
      }
      for (int bits = 1; bits < (1 << positions.size()); ++bits) {
        std::vector<int> subset;
        for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
          if ((bits >> i) & 1) subset.push_back(positions[i]);
        }
        auto it = carrier_required.find(carrier_key(subset));
        if (it != carrier_required.end()) cell.mandatory |= it->second;
      }
      const int cell_index = static_cast<int>(graph.cells.size());
      graph.cells.push_back(cell);
      for (int target = cell.envelope; target; target = (target - 1) & cell.envelope) {
        const int ti = target_index[target];
        if (ti < 0 || (cell.mandatory & ~target)) continue;
        bool intersects = true;
        for (int i = 0; i < cell.mask_count; ++i) {
          if (!(cell.masks[i] & target)) {
            intersects = false;
            break;
          }
        }
        if (intersects) graph.adjacency[ti].push_back(cell_index);
      }
    }
  }
  return graph;
}

Matching maximum_matching(const std::vector<std::vector<int>>& adjacency,
                          int right_size) {
  Matching answer;
  answer.left.assign(adjacency.size(), -1);
  answer.right.assign(right_size, -1);
  std::vector<int> distance(adjacency.size(), -1);

  auto bfs = [&]() {
    std::deque<int> queue;
    bool found = false;
    for (int left = 0; left < static_cast<int>(answer.left.size()); ++left) {
      if (answer.left[left] < 0) {
        distance[left] = 0;
        queue.push_back(left);
      } else {
        distance[left] = -1;
      }
    }
    while (!queue.empty()) {
      const int left = queue.front();
      queue.pop_front();
      for (int right : adjacency[left]) {
        const int next = answer.right[right];
        if (next < 0) {
          found = true;
        } else if (distance[next] < 0) {
          distance[next] = distance[left] + 1;
          queue.push_back(next);
        }
      }
    }
    return found;
  };

  std::function<bool(int)> dfs = [&](int left) {
    for (int right : adjacency[left]) {
      const int next = answer.right[right];
      if (next < 0 ||
          (distance[next] == distance[left] + 1 && dfs(next))) {
        answer.left[left] = right;
        answer.right[right] = left;
        return true;
      }
    }
    distance[left] = -1;
    return false;
  };

  while (bfs()) {
    for (int left = 0; left < static_cast<int>(answer.left.size()); ++left) {
      if (answer.left[left] < 0) dfs(left);
    }
  }
  return answer;
}

Audit audit(const std::vector<int>& middle) {
  Audit result;
  result.graph = build_graph(middle);
  if (!result.graph.factorable) return result;
  result.matching = maximum_matching(result.graph.adjacency,
                                     result.graph.cells.size());
  for (int i = 0; i < static_cast<int>(result.graph.targets.size()); ++i) {
    if (result.matching.left[i] < 0) result.unmatched_indices.push_back(i);
    if (result.graph.adjacency[i].empty()) result.zero_indices.push_back(i);
  }

  result.dm_left.assign(result.graph.targets.size(), 0);
  result.dm_right.assign(result.graph.cells.size(), 0);
  std::deque<std::pair<int, int>> queue;
  for (int i : result.unmatched_indices) {
    result.dm_left[i] = 1;
    queue.emplace_back(0, i);
  }
  while (!queue.empty()) {
    auto [side, index] = queue.front();
    queue.pop_front();
    if (side == 0) {
      for (int cell : result.graph.adjacency[index]) {
        if (result.matching.left[index] == cell) continue;
        if (!result.dm_right[cell]) {
          result.dm_right[cell] = 1;
          queue.emplace_back(1, cell);
        }
      }
    } else {
      const int target = result.matching.right[index];
      if (target >= 0 && !result.dm_left[target]) {
        result.dm_left[target] = 1;
        queue.emplace_back(0, target);
      }
    }
  }
  return result;
}

std::vector<DMComponent> dm_components(const Audit& audit) {
  const Graph& graph = audit.graph;
  std::vector<std::vector<int>> inverse(graph.cells.size());
  for (int left = 0; left < static_cast<int>(graph.adjacency.size()); ++left) {
    if (!audit.dm_left[left]) continue;
    for (int right : graph.adjacency[left]) {
      if (audit.dm_right[right]) inverse[right].push_back(left);
    }
  }

  std::vector<char> seen_left(audit.dm_left.size(), 0);
  std::vector<char> seen_right(audit.dm_right.size(), 0);
  std::vector<DMComponent> result;
  for (int seed = 0; seed < static_cast<int>(audit.dm_left.size()); ++seed) {
    if (!audit.dm_left[seed] || seen_left[seed]) continue;
    DMComponent component;
    component.core = (1 << g_k) - 1;
    std::deque<std::pair<int, int>> queue;
    seen_left[seed] = 1;
    queue.emplace_back(0, seed);
    while (!queue.empty()) {
      const auto [side, index] = queue.front();
      queue.pop_front();
      if (side == 0) {
        ++component.left;
        const int target = graph.targets[index];
        component.core &= target;
        ++component.target_ranks[std::popcount(static_cast<unsigned>(target))];
        for (int right : graph.adjacency[index]) {
          if (audit.dm_right[right] && !seen_right[right]) {
            seen_right[right] = 1;
            queue.emplace_back(1, right);
          }
        }
      } else {
        ++component.right;
        ++component.cell_depths[graph.cells[index].depth];
        for (int left : inverse[index]) {
          if (!seen_left[left]) {
            seen_left[left] = 1;
            queue.emplace_back(0, left);
          }
        }
      }
    }
    result.push_back(component);
  }
  std::sort(result.begin(), result.end(), [](const DMComponent& a,
                                             const DMComponent& b) {
    if (a.left != b.left) return a.left > b.left;
    if (a.right != b.right) return a.right > b.right;
    return a.core < b.core;
  });
  return result;
}

template <typename T>
void json_array(std::ostream& out, const std::vector<T>& values) {
  out << '[';
  for (size_t i = 0; i < values.size(); ++i) {
    if (i) out << ',';
    out << values[i];
  }
  out << ']';
}

std::string json_escape(const std::string& value) {
  std::string result;
  for (char c : value) {
    if (c == '\\' || c == '"') result.push_back('\\');
    result.push_back(c);
  }
  return result;
}

void json_histogram(std::ostream& out, const std::vector<int>& values) {
  std::unordered_map<int, int> count;
  for (int value : values) ++count[value];
  std::vector<std::pair<int, int>> rows(count.begin(), count.end());
  std::sort(rows.begin(), rows.end());
  out << '{';
  for (size_t i = 0; i < rows.size(); ++i) {
    if (i) out << ',';
    out << '"' << rows[i].first << "\":" << rows[i].second;
  }
  out << '}';
}

int fixed_neighbourhood(const Graph& graph,
                        const std::unordered_set<int>& fixed_targets) {
  std::vector<char> hit(graph.cells.size(), 0);
  for (int ti = 0; ti < static_cast<int>(graph.targets.size()); ++ti) {
    if (!fixed_targets.contains(graph.targets[ti])) continue;
    for (int cell : graph.adjacency[ti]) hit[cell] = 1;
  }
  return std::count(hit.begin(), hit.end(), 1);
}

std::array<int, 4> fixed_distance_histogram(
    const Graph& graph, const std::unordered_set<int>& fixed_targets) {
  std::array<int, 4> histogram{};
  for (const Cell& cell : graph.cells) {
    int distance = 3;
    for (int target : fixed_targets) {
      int cost = std::popcount(static_cast<unsigned>(target & ~cell.envelope));
      if (cost >= distance) continue;
      cost += std::popcount(static_cast<unsigned>(cell.mandatory & ~target));
      if (cost >= distance) continue;
      for (int i = 0; i < cell.mask_count; ++i) {
        cost += !(cell.masks[i] & target);
      }
      distance = std::min(distance, cost);
      if (!distance) break;
    }
    ++histogram[std::min(distance, 3)];
  }
  return histogram;
}

void emit(const std::string& source, const Audit& result,
          const std::unordered_set<int>& fixed_targets, bool distances,
          bool certificate) {
  std::cout << "{\"source\":\"" << json_escape(source) << "\"";
  if (!result.graph.factorable) {
    std::cout << ",\"status\":\"NOT_FACTORABLE\",\"structural_failure\":["
              << result.graph.structural_start << ','
              << result.graph.structural_coordinate << "]}\n";
    return;
  }
  std::vector<int> unmatched, zeros, dm_targets, dm_cell_indices;
  for (int i : result.unmatched_indices) unmatched.push_back(result.graph.targets[i]);
  for (int i : result.zero_indices) zeros.push_back(result.graph.targets[i]);
  for (int i = 0; i < static_cast<int>(result.dm_left.size()); ++i) {
    if (result.dm_left[i]) dm_targets.push_back(result.graph.targets[i]);
  }
  for (int i = 0; i < static_cast<int>(result.dm_right.size()); ++i) {
    if (result.dm_right[i]) dm_cell_indices.push_back(i);
  }
  std::vector<int> dm_target_ranks, dm_cell_depths, dm_cell_envelope_ranks;
  for (int value : dm_targets) dm_target_ranks.push_back(std::popcount(static_cast<unsigned>(value)));
  for (int index : dm_cell_indices) {
    dm_cell_depths.push_back(result.graph.cells[index].depth);
    dm_cell_envelope_ranks.push_back(std::popcount(static_cast<unsigned>(result.graph.cells[index].envelope)));
  }
  const auto components = dm_components(result);
  std::cout << ",\"status\":\""
            << (unmatched.empty() ? "PASS" : "HALL_DEFICIENT") << "\""
            << ",\"targets\":" << result.graph.targets.size()
            << ",\"cells\":" << result.graph.cells.size()
            << ",\"matching\":" << result.graph.targets.size() - unmatched.size()
            << ",\"deficiency\":" << unmatched.size()
            << ",\"zero_candidates\":" << zeros.size()
            << ",\"unmatched_targets\":";
  json_array(std::cout, unmatched);
  std::cout << ",\"zero_targets\":";
  json_array(std::cout, zeros);
  std::cout << ",\"dm_left\":" << dm_targets.size()
            << ",\"dm_right\":" << dm_cell_indices.size()
            << ",\"dm_targets\":";
  json_array(std::cout, dm_targets);
  std::cout << ",\"dm_cell_indices\":";
  json_array(std::cout, dm_cell_indices);
  std::cout << ",\"dm_target_rank_histogram\":";
  json_histogram(std::cout, dm_target_ranks);
  std::cout << ",\"dm_cell_depth_histogram\":";
  json_histogram(std::cout, dm_cell_depths);
  std::cout << ",\"dm_cell_envelope_rank_histogram\":";
  json_histogram(std::cout, dm_cell_envelope_ranks);
  std::cout << ",\"dm_component_count\":" << components.size()
            << ",\"dm_components\":[";
  for (size_t ci = 0; ci < components.size(); ++ci) {
    if (ci) std::cout << ',';
    const auto& component = components[ci];
    std::cout << "{\"core\":" << component.core
              << ",\"core_rank\":"
              << std::popcount(static_cast<unsigned>(component.core))
              << ",\"left\":" << component.left
              << ",\"right\":" << component.right
              << ",\"gap\":" << component.left - component.right
              << ",\"target_rank_histogram\":{";
    bool first = true;
    for (int rank = 0; rank < static_cast<int>(component.target_ranks.size());
         ++rank) {
      if (!component.target_ranks[rank]) continue;
      if (!first) std::cout << ',';
      first = false;
      std::cout << '\"' << rank << "\":" << component.target_ranks[rank];
    }
    std::cout << "},\"cell_depth_histogram\":{";
    first = true;
    for (int depth = 0; depth < static_cast<int>(component.cell_depths.size());
         ++depth) {
      if (!component.cell_depths[depth]) continue;
      if (!first) std::cout << ',';
      first = false;
      std::cout << '\"' << depth << "\":" << component.cell_depths[depth];
    }
    std::cout << "}}";
  }
  std::cout << ']';
  if (certificate) {
    std::cout << ",\"matching_edges\":[";
    bool first_edge = true;
    for (int target = 0;
         target < static_cast<int>(result.matching.left.size()); ++target) {
      const int cell = result.matching.left[target];
      if (cell < 0) continue;
      if (!first_edge) std::cout << ',';
      first_edge = false;
      std::cout << '[' << result.graph.targets[target] << ',' << cell << ']';
    }
    std::cout << "]";
    std::vector<int> cover_targets;
    cover_targets.reserve(result.graph.targets.size() - dm_targets.size());
    for (int target = 0; target < static_cast<int>(result.dm_left.size()); ++target) {
      if (!result.dm_left[target]) cover_targets.push_back(result.graph.targets[target]);
    }
    std::cout << ",\"min_vertex_cover_targets\":";
    json_array(std::cout, cover_targets);
    std::cout << ",\"min_vertex_cover_cells\":";
    json_array(std::cout, dm_cell_indices);
    std::cout << ",\"min_vertex_cover_size\":"
              << cover_targets.size() + dm_cell_indices.size();
  }
  if (!fixed_targets.empty()) {
    std::cout << ",\"fixed_target_count\":" << fixed_targets.size()
              << ",\"fixed_neighbourhood\":"
              << fixed_neighbourhood(result.graph, fixed_targets);
    if (distances) {
      auto histogram = fixed_distance_histogram(result.graph, fixed_targets);
      std::cout << ",\"fixed_distance_histogram\":[" << histogram[0] << ','
                << histogram[1] << ',' << histogram[2] << ',' << histogram[3]
                << ']';
    }
  }
  std::cout << "}\n";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    std::string fixed_file;
    bool distances = false;
    bool certificate = false;
    std::vector<std::string> sources;
    for (int i = 1; i < argc; ++i) {
      std::string argument = argv[i];
      if (argument == "--fixed-targets-file" && i + 1 < argc) {
        fixed_file = argv[++i];
      } else if (argument == "--k" && i + 1 < argc) {
        g_k = std::stoi(argv[++i]);
      } else if (argument == "--depth" && i + 1 < argc) {
        g_depth = std::stoi(argv[++i]);
      } else if (argument == "--distance") {
        distances = true;
      } else if (argument == "--certificate") {
        certificate = true;
      } else if (argument == "--help") {
        std::cout << "usage: fast_k15_hall_dm [--k K] [--depth D] "
                     "[--fixed-targets-file FILE] [--distance] "
                     "[--certificate] CERTIFICATE...\n";
        return 0;
      } else {
        sources.push_back(argument);
      }
    }
    if (sources.empty()) throw std::runtime_error("no certificates supplied");
    if (g_k <= 0 || g_k > 15 || g_depth <= 0 || g_depth > 8) {
      throw std::runtime_error("supported range is k<=15, depth<=8");
    }
    std::unordered_set<int> fixed_targets;
    if (!fixed_file.empty()) {
      const std::string text = read_file(fixed_file);
      auto values = extract_named_array(
          text, {"dm_targets", "witness_targets", "targets", "zero_targets"});
      if (values.empty()) values = parse_array_at(text, 0);
      fixed_targets.insert(values.begin(), values.end());
    }
    for (const std::string& source : sources) {
      emit(source, audit(extract_middle(source)), fixed_targets, distances,
           certificate);
    }
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "error: " << error.what() << '\n';
    return 2;
  }
}
