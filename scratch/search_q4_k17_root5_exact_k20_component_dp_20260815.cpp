#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

using U64 = std::uint64_t;
constexpr int ROW_WORDS = 4;

struct RowMask {
  std::array<U64, ROW_WORDS> word{};
  bool operator==(const RowMask& other) const { return word == other.word; }
};

struct RowMaskHash {
  std::size_t operator()(const RowMask& mask) const noexcept {
    U64 hash = 0x9e3779b97f4a7c15ULL;
    for (U64 value : mask.word) {
      value ^= value >> 30;
      value *= 0xbf58476d1ce4e5b9ULL;
      value ^= value >> 27;
      value *= 0x94d049bb133111ebULL;
      value ^= value >> 31;
      hash ^= value + 0x9e3779b97f4a7c15ULL + (hash << 6) + (hash >> 2);
    }
    return static_cast<std::size_t>(hash);
  }
};

int row_count(const RowMask& mask) {
  int result = 0;
  for (U64 value : mask.word) result += __builtin_popcountll(value);
  return result;
}

bool empty(const RowMask& mask) {
  for (U64 value : mask.word) if (value) return false;
  return true;
}

bool disjoint(const RowMask& left, const RowMask& right) {
  for (int i = 0; i < ROW_WORDS; ++i)
    if (left.word[i] & right.word[i]) return false;
  return true;
}

RowMask difference(RowMask left, const RowMask& right) {
  for (int i = 0; i < ROW_WORDS; ++i) left.word[i] &= ~right.word[i];
  return left;
}

using Bits = std::vector<U64>;

bool any(const Bits& bits) {
  for (U64 value : bits) if (value) return true;
  return false;
}

int bit_count(const Bits& bits) {
  int result = 0;
  for (U64 value : bits) result += __builtin_popcountll(value);
  return result;
}

int first_bit(const Bits& bits) {
  for (int word = 0; word < static_cast<int>(bits.size()); ++word) {
    if (bits[word]) return 64 * word + __builtin_ctzll(bits[word]);
  }
  return -1;
}

void clear_bit(Bits& bits, int bit) {
  bits[bit / 64] &= ~(U64{1} << (bit % 64));
}

void set_bit(Bits& bits, int bit) {
  bits[bit / 64] |= U64{1} << (bit % 64);
}

bool has_bit(const Bits& bits, int bit) {
  return (bits[bit / 64] >> (bit % 64)) & 1U;
}

Bits intersect(const Bits& left, const Bits& right) {
  Bits result(left.size());
  for (std::size_t i = 0; i < left.size(); ++i) result[i] = left[i] & right[i];
  return result;
}

struct Instance {
  int self_left = -1;
  int self_right = -1;
  std::vector<int> global_rows;
  std::vector<int> pair_index;
  std::vector<RowMask> column;
};

std::vector<int> parse_csv(const std::string& text) {
  std::vector<int> result;
  std::istringstream stream(text);
  std::string item;
  while (std::getline(stream, item, ',')) {
    if (!item.empty()) result.push_back(std::stoi(item));
  }
  return result;
}

Instance read_instance(const std::string& path) {
  std::ifstream input(path);
  if (!input) throw std::runtime_error("cannot open graph input");
  Instance result;
  std::string line;
  if (!std::getline(input, line)) throw std::runtime_error("missing self header");
  {
    std::istringstream row(line);
    std::string hash, label;
    row >> hash >> label >> result.self_left >> result.self_right;
    if (hash != "#" || label != "self") throw std::runtime_error("bad self header");
  }
  if (!std::getline(input, line)) throw std::runtime_error("missing row header");
  {
    const std::string prefix = "# rows\t";
    if (line.rfind(prefix, 0) != 0) throw std::runtime_error("bad row header");
    result.global_rows = parse_csv(line.substr(prefix.size()));
  }
  if (result.global_rows.empty() || result.global_rows.size() > 200 ||
      result.global_rows.size() % 10 != 0)
    throw std::runtime_error("expected a positive multiple of ten rows, at most 200");
  std::array<int, 680> local{};
  local.fill(-1);
  for (int i = 0; i < static_cast<int>(result.global_rows.size()); ++i)
    local.at(result.global_rows[i]) = i;
  if (!std::getline(input, line) || line != "pair_index\trows")
    throw std::runtime_error("bad data header");
  while (std::getline(input, line)) {
    if (line.empty()) continue;
    const auto tab = line.find('\t');
    if (tab == std::string::npos) throw std::runtime_error("bad data row");
    const int index = std::stoi(line.substr(0, tab));
    const auto rows = parse_csv(line.substr(tab + 1));
    if (rows.size() != 10) throw std::runtime_error("column is not a ten-set");
    RowMask mask;
    for (int row : rows) {
      const int position = local.at(row);
      if (position < 0) throw std::runtime_error("column row outside residual");
      mask.word[position / 64] |= U64{1} << (position % 64);
    }
    if (row_count(mask) != 10) throw std::runtime_error("repeated column row");
    result.pair_index.push_back(index);
    result.column.push_back(mask);
  }
  if (result.column.empty()) throw std::runtime_error("empty column bank");
  return result;
}

enum class Verdict { SAT, UNSAT, UNKNOWN };

class Solver {
 public:
  Solver(const Instance& instance, double seconds)
      : instance_(instance), n_(instance.column.size()), words_((n_ + 63) / 64),
        row_total_(instance.global_rows.size()),
        deadline_(std::chrono::steady_clock::now() +
                  std::chrono::milliseconds(static_cast<long long>(1000.0 * seconds))) {
    adjacency_.assign(n_, Bits(words_));
    row_columns_.assign(row_total_, Bits(words_));
    for (int i = 0; i < n_; ++i) {
      for (int row = 0; row < row_total_; ++row)
        if ((instance_.column[i].word[row / 64] >> (row % 64)) & 1U)
          set_bit(row_columns_[row], i);
      for (int j = 0; j < i; ++j) {
        if (disjoint(instance_.column[i], instance_.column[j])) {
          set_bit(adjacency_[i], j);
          set_bit(adjacency_[j], i);
        }
      }
    }
  }

  Verdict run() {
    RowMask rows;
    for (int row = 0; row < row_total_; ++row)
      rows.word[row / 64] |= U64{1} << (row % 64);
    Bits candidates(words_, ~U64{0});
    if (n_ % 64) candidates.back() &= (U64{1} << (n_ % 64)) - 1;
    current_.clear();
    const Verdict verdict = solve(rows, candidates);
    return verdict;
  }

  const std::vector<int>& solution() const { return solution_; }
  std::uint64_t nodes() const { return nodes_; }
  std::uint64_t memo_hits() const { return memo_hits_; }
  std::uint64_t color_prunes() const { return color_prunes_; }
  std::uint64_t zero_prunes() const { return zero_prunes_; }
  std::uint64_t component_splits() const { return component_splits_; }
  std::size_t memo_size() const { return unsat_.size(); }

 private:
  bool timed_out() {
    if ((nodes_ & 4095U) == 0 && std::chrono::steady_clock::now() >= deadline_)
      timeout_ = true;
    return timeout_;
  }

  int limited_color_bound(Bits candidates, int limit) const {
    int colors = 0;
    while (any(candidates) && colors < limit) {
      ++colors;
      Bits independent = candidates;
      while (any(independent)) {
        const int vertex = first_bit(independent);
        clear_bit(candidates, vertex);
        clear_bit(independent, vertex);
        for (int word = 0; word < words_; ++word)
          independent[word] &= ~adjacency_[vertex][word];
      }
    }
    return colors;
  }

  std::vector<std::pair<RowMask, Bits>> components(const RowMask& rows,
                                                    const Bits& candidates) const {
    std::array<int, 200> parent{};
    std::iota(parent.begin(), parent.end(), 0);
    auto root = [&](int value) {
      int current = value;
      while (parent[current] != current) current = parent[current];
      while (parent[value] != value) {
        const int next = parent[value];
        parent[value] = current;
        value = next;
      }
      return current;
    };
    auto unite = [&](int left, int right) {
      left = root(left); right = root(right);
      if (left != right) parent[right] = left;
    };
    for (int vertex = 0; vertex < n_; ++vertex) {
      if (!has_bit(candidates, vertex)) continue;
      int first = -1;
      for (int row = 0; row < row_total_; ++row) {
        if (((instance_.column[vertex].word[row / 64] >> (row % 64)) & 1U) == 0)
          continue;
        if (first < 0) first = row;
        else unite(first, row);
      }
    }
    std::array<int, 200> component_index{};
    component_index.fill(-1);
    std::vector<std::pair<RowMask, Bits>> result;
    for (int row = 0; row < row_total_; ++row) {
      if (((rows.word[row / 64] >> (row % 64)) & 1U) == 0) continue;
      const int representative = root(row);
      if (component_index[representative] < 0) {
        component_index[representative] = result.size();
        result.emplace_back(RowMask{}, Bits(words_));
      }
      result[component_index[representative]].first.word[row / 64] |=
          U64{1} << (row % 64);
    }
    if (result.size() <= 1) return result;
    for (int vertex = 0; vertex < n_; ++vertex) {
      if (!has_bit(candidates, vertex)) continue;
      int first = -1;
      for (int row = 0; row < row_total_; ++row) {
        if ((instance_.column[vertex].word[row / 64] >> (row % 64)) & 1U) {
          first = row; break;
        }
      }
      const int index = component_index[root(first)];
      set_bit(result[index].second, vertex);
    }
    std::sort(result.begin(), result.end(), [](const auto& left, const auto& right) {
      return row_count(left.first) < row_count(right.first);
    });
    return result;
  }

  Verdict solve(const RowMask& rows, const Bits& candidates) {
    ++nodes_;
    if (timed_out()) return Verdict::UNKNOWN;
    if (empty(rows)) {
      solution_ = current_;
      return Verdict::SAT;
    }
    if (row_count(rows) % 10) return Verdict::UNSAT;
    if (unsat_.contains(rows)) {
      ++memo_hits_;
      return Verdict::UNSAT;
    }
    const int needed = row_count(rows) / 10;
    if (bit_count(candidates) < needed) {
      unsat_.insert(rows);
      return Verdict::UNSAT;
    }
    if (limited_color_bound(candidates, needed) < needed) {
      ++color_prunes_;
      unsat_.insert(rows);
      return Verdict::UNSAT;
    }

    int branch_degree = n_ + 1;
    Bits branch_options;
    for (int row = 0; row < row_total_; ++row) {
      if (((rows.word[row / 64] >> (row % 64)) & 1U) == 0) continue;
      Bits options = intersect(candidates, row_columns_[row]);
      const int degree = bit_count(options);
      if (degree < branch_degree) {
        branch_degree = degree;
        branch_options = std::move(options);
      }
    }
    if (branch_degree == 0) {
      ++zero_prunes_;
      unsat_.insert(rows);
      return Verdict::UNSAT;
    }

    if ((nodes_ & 255U) == 1) {
      auto split = components(rows, candidates);
      if (split.size() > 1) {
        ++component_splits_;
        const std::vector<int> saved = current_;
        std::vector<int> combined = saved;
        for (const auto& [component_rows, component_candidates] : split) {
          if (row_count(component_rows) % 10) {
            current_ = saved;
            unsat_.insert(rows);
            return Verdict::UNSAT;
          }
          current_ = combined;
          const Verdict verdict = solve(component_rows, component_candidates);
          if (verdict != Verdict::SAT) {
            current_ = saved;
            if (verdict == Verdict::UNSAT) unsat_.insert(rows);
            return verdict;
          }
          combined = solution_;
        }
        solution_ = combined;
        current_ = saved;
        return Verdict::SAT;
      }
    }

    std::vector<std::pair<int, int>> order;
    for (int vertex = first_bit(branch_options); vertex >= 0; ) {
      Bits next = intersect(candidates, adjacency_[vertex]);
      order.emplace_back(-bit_count(next), vertex);
      clear_bit(branch_options, vertex);
      vertex = first_bit(branch_options);
    }
    std::sort(order.begin(), order.end(), [&](const auto& left, const auto& right) {
      if (left.first != right.first) return left.first < right.first;
      return instance_.pair_index[left.second] < instance_.pair_index[right.second];
    });
    for (const auto& [score, vertex] : order) {
      (void)score;
      current_.push_back(vertex);
      const RowMask next_rows = difference(rows, instance_.column[vertex]);
      const Bits next_candidates = intersect(candidates, adjacency_[vertex]);
      const Verdict verdict = solve(next_rows, next_candidates);
      current_.pop_back();
      if (verdict == Verdict::SAT) return verdict;
      if (verdict == Verdict::UNKNOWN) return verdict;
    }
    unsat_.insert(rows);
    return Verdict::UNSAT;
  }

  const Instance& instance_;
  int n_;
  int words_;
  int row_total_;
  std::vector<Bits> adjacency_;
  std::vector<Bits> row_columns_;
  std::chrono::steady_clock::time_point deadline_;
  bool timeout_ = false;
  std::vector<int> current_;
  std::vector<int> solution_;
  std::unordered_set<RowMask, RowMaskHash> unsat_;
  std::uint64_t nodes_ = 0;
  std::uint64_t memo_hits_ = 0;
  std::uint64_t color_prunes_ = 0;
  std::uint64_t zero_prunes_ = 0;
  std::uint64_t component_splits_ = 0;
};

std::string verdict_name(Verdict verdict) {
  if (verdict == Verdict::SAT) return "SAT";
  if (verdict == Verdict::UNSAT) return "UNSAT";
  return "UNKNOWN";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc != 4)
      throw std::runtime_error("usage: graph.tsv seconds result.json");
    const Instance instance = read_instance(argv[1]);
    const double seconds = std::stod(argv[2]);
    const auto started = std::chrono::steady_clock::now();
    Solver solver(instance, seconds);
    const Verdict verdict = solver.run();
    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::vector<int> chosen;
    if (verdict == Verdict::SAT) {
      for (int local : solver.solution()) chosen.push_back(instance.pair_index.at(local));
      std::sort(chosen.begin(), chosen.end());
      if (chosen.size() != instance.global_rows.size() / 10)
        throw std::runtime_error("SAT solution has the wrong clique size");
    }
    std::ofstream output(argv[3]);
    if (!output) throw std::runtime_error("cannot open result output");
    auto emit = [&](std::ostream& stream) {
      stream << "{\n"
             << "  \"status\": \"" << verdict_name(verdict) << "\",\n"
             << "  \"scope\": \"exact disjoint-column decision on one frozen self-conditioned graph\",\n"
             << "  \"graph\": \"" << argv[1] << "\",\n"
             << "  \"self_indices\": [" << instance.self_left << ','
             << instance.self_right << "],\n"
             << "  \"residual_rows\": " << instance.global_rows.size() << ",\n"
             << "  \"pair_columns\": " << instance.column.size() << ",\n"
             << "  \"target_clique\": " << instance.global_rows.size() / 10 << ",\n"
             << "  \"elapsed_seconds\": " << elapsed << ",\n"
             << "  \"nodes\": " << solver.nodes() << ",\n"
             << "  \"memo_states\": " << solver.memo_size() << ",\n"
             << "  \"memo_hits\": " << solver.memo_hits() << ",\n"
             << "  \"color_prunes\": " << solver.color_prunes() << ",\n"
             << "  \"zero_row_prunes\": " << solver.zero_prunes() << ",\n"
             << "  \"component_splits\": " << solver.component_splits() << ",\n"
             << "  \"pair_indices\": [";
      for (std::size_t i = 0; i < chosen.size(); ++i) {
        if (i) stream << ',';
        stream << chosen[i];
      }
      stream << "]\n}\n";
    };
    emit(output);
    emit(std::cout);
    return verdict == Verdict::UNKNOWN ? 3 : 0;
  } catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what() << '\n';
    return 2;
  }
}
