#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
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

int count(const RowMask& mask) {
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

RowMask subtract(RowMask left, const RowMask& right) {
  for (int i = 0; i < ROW_WORDS; ++i) left.word[i] &= ~right.word[i];
  return left;
}

using Bits = std::vector<U64>;

bool any(const Bits& bits) {
  for (U64 value : bits) if (value) return true;
  return false;
}

int count(const Bits& bits) {
  int result = 0;
  for (U64 value : bits) result += __builtin_popcountll(value);
  return result;
}

int first(const Bits& bits) {
  for (int word = 0; word < static_cast<int>(bits.size()); ++word)
    if (bits[word]) return 64 * word + __builtin_ctzll(bits[word]);
  return -1;
}

void set(Bits& bits, int bit) {
  bits[bit / 64] |= U64{1} << (bit % 64);
}

void clear(Bits& bits, int bit) {
  bits[bit / 64] &= ~(U64{1} << (bit % 64));
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
  while (std::getline(stream, item, ','))
    if (!item.empty()) result.push_back(std::stoi(item));
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
  const std::string prefix = "# rows\t";
  if (line.rfind(prefix, 0) != 0) throw std::runtime_error("bad row header");
  result.global_rows = parse_csv(line.substr(prefix.size()));
  if (result.global_rows.empty() || result.global_rows.size() > 200 ||
      result.global_rows.size() % 10 != 0)
    throw std::runtime_error("expected a positive multiple of ten rows, at most 200");
  std::array<int, 680> local{};
  local.fill(-1);
  for (int i = 0; i < static_cast<int>(result.global_rows.size()); ++i) {
    if (local.at(result.global_rows[i]) >= 0) throw std::runtime_error("duplicate row");
    local.at(result.global_rows[i]) = i;
  }
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
    if (count(mask) != 10) throw std::runtime_error("repeated column row");
    result.pair_index.push_back(index);
    result.column.push_back(mask);
  }
  if (result.column.empty()) throw std::runtime_error("empty column bank");
  return result;
}

enum class Verdict { SAT, UNSAT, UNKNOWN };

class Solver {
 public:
  Solver(const Instance& instance, double seconds, U64 seed, int row_slack)
      : instance_(instance), n_(instance.column.size()), words_((n_ + 63) / 64),
        rows_(instance.global_rows.size()), seed_(seed), row_slack_(row_slack),
        mode_(seed % 4), rng_(seed ^ 0xd1b54a32d192ed03ULL),
        deadline_(std::chrono::steady_clock::now() +
                  std::chrono::milliseconds(static_cast<long long>(1000.0 * seconds))) {
    adjacency_.assign(n_, Bits(words_));
    row_columns_.assign(rows_, Bits(words_));
    for (int i = 0; i < n_; ++i) {
      for (int row = 0; row < rows_; ++row)
        if ((instance_.column[i].word[row / 64] >> (row % 64)) & 1U)
          set(row_columns_[row], i);
      for (int j = 0; j < i; ++j) {
        if (disjoint(instance_.column[i], instance_.column[j])) {
          set(adjacency_[i], j);
          set(adjacency_[j], i);
        }
      }
    }
  }

  Verdict run() {
    RowMask remaining;
    for (int row = 0; row < rows_; ++row)
      remaining.word[row / 64] |= U64{1} << (row % 64);
    Bits candidates(words_, ~U64{0});
    if (n_ % 64) candidates.back() &= (U64{1} << (n_ % 64)) - 1;
    return visit(remaining, candidates);
  }

  const std::vector<int>& solution() const { return solution_; }
  U64 nodes() const { return nodes_; }
  U64 memo_hits() const { return memo_hits_; }
  U64 color_prunes() const { return color_prunes_; }
  U64 zero_prunes() const { return zero_prunes_; }
  std::size_t memo_size() const { return unsat_.size(); }
  int mode() const { return mode_; }
  int root_row() const { return root_row_; }
  U64 root_order_hash() const { return root_order_hash_; }
  int root_first_pair() const { return root_first_pair_; }

 private:
  bool timed_out() {
    if ((nodes_ & 1023U) == 0 && std::chrono::steady_clock::now() >= deadline_)
      timeout_ = true;
    return timeout_;
  }

  int limited_color_bound(Bits candidates, int limit) const {
    int colors = 0;
    while (any(candidates) && colors < limit) {
      ++colors;
      Bits independent = candidates;
      while (any(independent)) {
        const int vertex = first(independent);
        clear(candidates, vertex);
        clear(independent, vertex);
        for (int word = 0; word < words_; ++word)
          independent[word] &= ~adjacency_[vertex][word];
      }
    }
    return colors;
  }

  Verdict visit(const RowMask& remaining, const Bits& candidates) {
    ++nodes_;
    if (timed_out()) return Verdict::UNKNOWN;
    if (empty(remaining)) {
      solution_ = current_;
      return Verdict::SAT;
    }
    if (count(remaining) % 10) return Verdict::UNSAT;
    if (unsat_.contains(remaining)) {
      ++memo_hits_;
      return Verdict::UNSAT;
    }
    const int needed = count(remaining) / 10;
    if (count(candidates) < needed) {
      unsat_.insert(remaining);
      return Verdict::UNSAT;
    }
    if (limited_color_bound(candidates, needed) < needed) {
      ++color_prunes_;
      unsat_.insert(remaining);
      return Verdict::UNSAT;
    }

    int minimum = n_ + 1;
    std::vector<std::pair<int, int>> row_degree;
    row_degree.reserve(rows_);
    for (int row = 0; row < rows_; ++row) {
      if (((remaining.word[row / 64] >> (row % 64)) & 1U) == 0) continue;
      const int degree = count(intersect(candidates, row_columns_[row]));
      minimum = std::min(minimum, degree);
      row_degree.emplace_back(row, degree);
    }
    if (minimum == 0) {
      ++zero_prunes_;
      unsat_.insert(remaining);
      return Verdict::UNSAT;
    }
    std::vector<int> row_menu;
    for (const auto& [row, degree] : row_degree)
      if (degree <= minimum + row_slack_) row_menu.push_back(row);
    std::uniform_int_distribution<std::size_t> choose_row(0, row_menu.size() - 1);
    const int branch_row = row_menu[choose_row(rng_)];
    Bits options = intersect(candidates, row_columns_[branch_row]);

    struct Choice { int vertex; int score; U64 tie; };
    std::vector<Choice> order;
    while (any(options)) {
      const int vertex = first(options);
      clear(options, vertex);
      int score = count(intersect(candidates, adjacency_[vertex]));
      if (mode_ == 0) score = 0;
      else if (mode_ == 2) score = -score;
      else if (mode_ == 3) {
        std::uniform_int_distribution<int> noise(-std::max(1, n_ / 12),
                                                  std::max(1, n_ / 12));
        score += noise(rng_);
      }
      order.push_back({vertex, score, rng_()});
    }
    std::sort(order.begin(), order.end(), [](const Choice& left, const Choice& right) {
      if (left.score != right.score) return left.score > right.score;
      return left.tie < right.tie;
    });
    if (current_.empty()) {
      root_row_ = branch_row;
      root_order_hash_ = 0xcbf29ce484222325ULL;
      for (const Choice& choice : order) {
        root_order_hash_ ^= static_cast<U64>(instance_.pair_index[choice.vertex]);
        root_order_hash_ *= 0x100000001b3ULL;
      }
      root_first_pair_ = instance_.pair_index[order.front().vertex];
    }

    for (const Choice& choice : order) {
      current_.push_back(choice.vertex);
      const Verdict verdict = visit(
          subtract(remaining, instance_.column[choice.vertex]),
          intersect(candidates, adjacency_[choice.vertex]));
      current_.pop_back();
      if (verdict != Verdict::UNSAT) return verdict;
    }
    unsat_.insert(remaining);
    return Verdict::UNSAT;
  }

  const Instance& instance_;
  int n_;
  int words_;
  int rows_;
  U64 seed_;
  int row_slack_;
  int mode_;
  std::mt19937_64 rng_;
  std::chrono::steady_clock::time_point deadline_;
  bool timeout_ = false;
  std::vector<Bits> adjacency_;
  std::vector<Bits> row_columns_;
  std::vector<int> current_;
  std::vector<int> solution_;
  std::unordered_set<RowMask, RowMaskHash> unsat_;
  U64 nodes_ = 0;
  U64 memo_hits_ = 0;
  U64 color_prunes_ = 0;
  U64 zero_prunes_ = 0;
  int root_row_ = -1;
  U64 root_order_hash_ = 0;
  int root_first_pair_ = -1;
};

std::string name(Verdict verdict) {
  if (verdict == Verdict::SAT) return "SAT";
  if (verdict == Verdict::UNSAT) return "UNSAT";
  return "UNKNOWN";
}

}  // namespace

int main(int argc, char** argv) {
  try {
    if (argc < 4 || argc > 6)
      throw std::runtime_error("usage: graph.tsv seconds result.json [seed] [row_slack]");
    const Instance instance = read_instance(argv[1]);
    const double seconds = std::stod(argv[2]);
    const U64 seed = argc >= 5 ? std::stoull(argv[4]) : 0;
    const int row_slack = argc >= 6 ? std::stoi(argv[5]) : 0;
    if (seconds <= 0 || row_slack < 0) throw std::runtime_error("bad run parameter");
    const auto started = std::chrono::steady_clock::now();
    Solver solver(instance, seconds, seed, row_slack);
    const Verdict verdict = solver.run();
    const double elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::vector<int> chosen;
    if (verdict == Verdict::SAT) {
      for (int local : solver.solution()) chosen.push_back(instance.pair_index.at(local));
      std::sort(chosen.begin(), chosen.end());
      if (chosen.size() != instance.global_rows.size() / 10)
        throw std::runtime_error("SAT solution has wrong size");
    }
    std::ofstream output(argv[3]);
    if (!output) throw std::runtime_error("cannot open result output");
    auto emit = [&](std::ostream& stream) {
      stream << "{\n"
             << "  \"status\": \"" << name(verdict) << "\",\n"
             << "  \"scope\": \"seeded SAT-first exact-cover traversal on one frozen graph\",\n"
             << "  \"graph\": \"" << argv[1] << "\",\n"
             << "  \"self_indices\": [" << instance.self_left << ',' << instance.self_right << "],\n"
             << "  \"residual_rows\": " << instance.global_rows.size() << ",\n"
             << "  \"pair_columns\": " << instance.column.size() << ",\n"
             << "  \"target_clique\": " << instance.global_rows.size() / 10 << ",\n"
             << "  \"seed\": " << seed << ",\n"
             << "  \"ordering_mode\": " << solver.mode() << ",\n"
             << "  \"row_slack\": " << row_slack << ",\n"
             << "  \"root_branch_row\": " << solver.root_row() << ",\n"
             << "  \"root_first_pair\": " << solver.root_first_pair() << ",\n"
             << "  \"root_order_hash\": " << solver.root_order_hash() << ",\n"
             << "  \"elapsed_seconds\": " << elapsed << ",\n"
             << "  \"nodes\": " << solver.nodes() << ",\n"
             << "  \"memo_states\": " << solver.memo_size() << ",\n"
             << "  \"memo_hits\": " << solver.memo_hits() << ",\n"
             << "  \"color_prunes\": " << solver.color_prunes() << ",\n"
             << "  \"zero_row_prunes\": " << solver.zero_prunes() << ",\n"
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
