// Exact owner-targeted q4/k17 reflection-pair generator.
// Compile and run substantive searches on H100 only.

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <numeric>
#include <optional>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

#include <omp.h>

namespace {

constexpr int K = 17;
constexpr int OWNER_RANK = 9;
constexpr int CORE_SIZE = 5;
constexpr int PERIOD = 10;
constexpr int MASK_COUNT = 1 << K;
constexpr uint32_t FULL_MASK = MASK_COUNT - 1;

using RowKey = std::array<uint16_t, PERIOD>;

struct RowKeyHash {
  std::size_t operator()(const RowKey& key) const noexcept {
    uint64_t hash = 0xcbf29ce484222325ULL;
    for (uint16_t value : key) {
      hash ^= static_cast<uint64_t>(value + 1);
      hash *= 0x100000001b3ULL;
    }
    return static_cast<std::size_t>(hash);
  }
};

struct Witness {
  std::array<uint8_t, CORE_SIZE> core{};
  std::array<uint8_t, PERIOD> order{};
  std::array<uint16_t, PERIOD> owner_ids{};
};

bool witness_less(const Witness& left, const Witness& right) {
  if (left.core != right.core) return left.core < right.core;
  if (left.order != right.order) return left.order < right.order;
  return left.owner_ids < right.owner_ids;
}

struct Counters {
  uint64_t raw_anchored = 0;
  uint64_t quotient_simple = 0;
  uint64_t reflection_disjoint = 0;
  uint64_t allowed = 0;

  Counters& operator+=(const Counters& other) {
    raw_anchored += other.raw_anchored;
    quotient_simple += other.quotient_simple;
    reflection_disjoint += other.reflection_disjoint;
    allowed += other.allowed;
    return *this;
  }
};

struct Anchor {
  uint32_t core_mask = 0;
  std::array<uint8_t, CORE_SIZE> core{};
  std::array<uint8_t, 4> window{};
};

struct Arguments {
  int target_row = -1;
  int threads = 64;
  std::string instance;
  std::string allowed_rows;
  std::string catalog;
  int sample_limit = 12;
  std::string swap_context;
  std::string top_catalog;
  std::string reservoir_catalog;
  int top_k = 100000;
  int reservoir_per_hole = 256;
};

struct SelectedPair {
  int pair_index = -1;
  RowKey rows{};
  int remove_base = 0;
  int single_rows = 0;
};

struct SwapContext {
  int energy = 0;
  std::array<int, 680> loads{};
  std::vector<SelectedPair> selected;
  std::vector<int> holes;
};

struct ScoredWitness {
  Witness witness;
  int delta = 0;
  int hole_change = 0;
  int best_outgoing_pair_index = -1;
  int holes_filled = 0;
  int add_base = 0;
};

struct RankedKey {
  int delta = 0;
  int hole_change = 0;
  RowKey key{};

  bool operator<(const RankedKey& other) const {
    if (delta != other.delta) return delta < other.delta;
    if (hole_change != other.hole_change) return hole_change < other.hole_change;
    return key < other.key;
  }
};

class BoundedTop {
 public:
  explicit BoundedTop(std::size_t limit = 0) : limit_(limit) {
    records_.reserve(limit ? static_cast<std::size_t>(limit * 1.3) + 1 : 1);
  }

  void consider(const RowKey& key, const ScoredWitness& scored) {
    if (!limit_) return;
    auto found = records_.find(key);
    if (found != records_.end()) {
      if (witness_less(scored.witness, found->second.witness)) {
        found->second.witness = scored.witness;
      }
      return;
    }
    const RankedKey rank{scored.delta, scored.hole_change, key};
    if (records_.size() == limit_) {
      if (!(rank < worst_.top())) return;
      records_.erase(worst_.top().key);
      worst_.pop();
    }
    records_.emplace(key, scored);
    worst_.push(rank);
  }

  const std::unordered_map<RowKey, ScoredWitness, RowKeyHash>& records() const {
    return records_;
  }

 private:
  std::size_t limit_;
  std::unordered_map<RowKey, ScoredWitness, RowKeyHash> records_;
  std::priority_queue<RankedKey> worst_;
};

uint32_t rotate_mask(uint32_t mask, int shift) {
  shift %= K;
  return ((mask << shift) | (mask >> (K - shift))) & FULL_MASK;
}

uint32_t negate_mask(uint32_t mask) {
  uint32_t result = 0;
  for (int value = 0; value < K; ++value) {
    if ((mask >> value) & 1U) result |= 1U << ((-value + K) % K);
  }
  return result;
}

std::string join_values(const auto& values, const char* delimiter = ",") {
  std::ostringstream stream;
  bool first = true;
  for (auto value : values) {
    if (!first) stream << delimiter;
    first = false;
    stream << static_cast<unsigned>(value);
  }
  return stream.str();
}

Arguments parse_arguments(int argc, char** argv) {
  Arguments args;
  for (int i = 1; i < argc; ++i) {
    const std::string option = argv[i];
    auto value = [&]() -> std::string {
      if (++i >= argc) throw std::runtime_error("missing value for " + option);
      return argv[i];
    };
    if (option == "--target-row") {
      args.target_row = std::stoi(value());
    } else if (option == "--threads") {
      args.threads = std::stoi(value());
    } else if (option == "--instance") {
      args.instance = value();
    } else if (option == "--allowed-rows") {
      args.allowed_rows = value();
    } else if (option == "--catalog") {
      args.catalog = value();
    } else if (option == "--sample-limit") {
      args.sample_limit = std::stoi(value());
    } else if (option == "--swap-context") {
      args.swap_context = value();
    } else if (option == "--top-catalog") {
      args.top_catalog = value();
    } else if (option == "--reservoir-catalog") {
      args.reservoir_catalog = value();
    } else if (option == "--top-k") {
      args.top_k = std::stoi(value());
    } else if (option == "--reservoir-per-hole") {
      args.reservoir_per_hole = std::stoi(value());
    } else {
      throw std::runtime_error("unknown option: " + option);
    }
  }
  if (args.target_row < 0 || args.target_row >= 680) {
    throw std::runtime_error("--target-row must be in 0..679");
  }
  if (args.threads <= 0 || args.instance.empty()) {
    throw std::runtime_error("positive --threads and --instance are required");
  }
  if ((!args.swap_context.empty()) != (!args.top_catalog.empty())) {
    throw std::runtime_error("--swap-context and --top-catalog must be used together");
  }
  if (!args.swap_context.empty() &&
      (args.top_k <= 0 || args.reservoir_per_hole <= 0 ||
       args.reservoir_catalog.empty())) {
    throw std::runtime_error("top mode needs positive limits and --reservoir-catalog");
  }
  return args;
}

SwapContext read_swap_context(const std::string& path) {
  std::ifstream stream(path);
  if (!stream) throw std::runtime_error("cannot open swap context: " + path);
  int row_count = 0, selected_count = 0;
  SwapContext context;
  stream >> row_count >> selected_count >> context.energy;
  if (row_count != 680 || selected_count != 54) {
    throw std::runtime_error("bad swap context header");
  }
  for (int row = 0; row < 680; ++row) {
    stream >> context.loads[row];
    if (context.loads[row] < 0 || context.loads[row] > 2) {
      throw std::runtime_error("bad incumbent load");
    }
    if (context.loads[row] == 0) context.holes.push_back(row);
  }
  for (int i = 0; i < selected_count; ++i) {
    SelectedPair pair;
    stream >> pair.pair_index;
    for (uint16_t& row : pair.rows) stream >> row;
    std::sort(pair.rows.begin(), pair.rows.end());
    if (std::adjacent_find(pair.rows.begin(), pair.rows.end()) != pair.rows.end()) {
      throw std::runtime_error("repeated selected-pair row");
    }
    for (uint16_t row : pair.rows) {
      const int load = context.loads[row];
      pair.remove_base += (load == 2 ? -1 : load == 1 ? 1 : 3);
      pair.single_rows += load == 1;
    }
    context.selected.push_back(pair);
  }
  std::string extra;
  if (stream >> extra) throw std::runtime_error("trailing swap-context data");
  if (context.energy <= 0 || context.energy % 2 ||
      context.holes.size() != static_cast<std::size_t>(context.energy / 2)) {
    throw std::runtime_error("inconsistent swap context energy/holes");
  }
  return context;
}

int intersection_size(const RowKey& left, const RowKey& right,
                      const std::array<int, 680>* loads = nullptr,
                      int* single_intersection = nullptr) {
  int i = 0, j = 0, intersection = 0, singles = 0;
  while (i < PERIOD && j < PERIOD) {
    if (left[i] < right[j]) {
      ++i;
    } else if (right[j] < left[i]) {
      ++j;
    } else {
      ++intersection;
      if (loads && (*loads)[left[i]] == 1) ++singles;
      ++i;
      ++j;
    }
  }
  if (single_intersection) *single_intersection = singles;
  return intersection;
}

ScoredWitness score_swap(const RowKey& key, const Witness& witness,
                         const SwapContext& context) {
  ScoredWitness result;
  result.witness = witness;
  for (uint16_t row : key) {
    const int load = context.loads[row];
    result.add_base += (load == 0 ? -1 : load == 1 ? 1 : 3);
    result.holes_filled += load == 0;
  }
  bool first = true;
  for (const SelectedPair& outgoing : context.selected) {
    int single_intersection = 0;
    const int intersection = intersection_size(
        key, outgoing.rows, &context.loads, &single_intersection
    );
    const int delta = result.add_base + outgoing.remove_base - 2 * intersection;
    const int hole_change = (
        -result.holes_filled + outgoing.single_rows - single_intersection
    );
    const auto candidate = std::tuple(delta, hole_change, outgoing.pair_index);
    const auto incumbent = std::tuple(
        result.delta, result.hole_change, result.best_outgoing_pair_index
    );
    if (first || candidate < incumbent) {
      first = false;
      result.delta = delta;
      result.hole_change = hole_change;
      result.best_outgoing_pair_index = outgoing.pair_index;
    }
  }
  return result;
}

std::unordered_set<RowKey, RowKeyHash> read_existing_pairs(
    const std::string& path, uint64_t& pair_lines) {
  std::ifstream stream(path);
  if (!stream) throw std::runtime_error("cannot open instance: " + path);
  int rows = 0, groups = 0, self_count = 0, pair_count = 0;
  stream >> rows >> groups >> self_count >> pair_count;
  if (rows != 680 || groups != 35) throw std::runtime_error("bad instance header");
  std::string line;
  std::getline(stream, line);
  for (int i = 0; i < self_count; ++i) {
    if (!std::getline(stream, line)) throw std::runtime_error("truncated self rows");
  }
  std::unordered_set<RowKey, RowKeyHash> result;
  result.reserve(static_cast<std::size_t>(pair_count * 1.3));
  for (int i = 0; i < pair_count; ++i) {
    RowKey key{};
    for (int j = 0; j < PERIOD; ++j) {
      int row = -1;
      stream >> row;
      if (row < 0 || row >= 680) throw std::runtime_error("bad pair row");
      key[j] = static_cast<uint16_t>(row);
    }
    std::sort(key.begin(), key.end());
    if (std::adjacent_find(key.begin(), key.end()) != key.end()) {
      throw std::runtime_error("repeated row in existing pair");
    }
    result.insert(key);
  }
  pair_lines = pair_count;
  return result;
}

std::optional<std::array<bool, 680>> read_allowed_rows(const std::string& path) {
  if (path.empty()) return std::nullopt;
  std::ifstream stream(path);
  if (!stream) throw std::runtime_error("cannot open allowed-row file: " + path);
  std::array<bool, 680> allowed{};
  int row = -1;
  while (stream >> row) {
    if (row < 0 || row >= 680) throw std::runtime_error("bad allowed row");
    allowed[row] = true;
  }
  return allowed;
}

void emit_json_key(std::ostream& stream, const RowKey& key) {
  stream << '[';
  for (int i = 0; i < PERIOD; ++i) {
    if (i) stream << ',';
    stream << key[i];
  }
  stream << ']';
}

void emit_json_small_array(std::ostream& stream, const auto& values) {
  stream << '[';
  for (std::size_t i = 0; i < values.size(); ++i) {
    if (i) stream << ',';
    stream << static_cast<unsigned>(values[i]);
  }
  stream << ']';
}

void write_scored_catalogue(
    const std::string& path,
    const std::unordered_map<RowKey, ScoredWitness, RowKeyHash>& records,
    const std::array<int, 1430>& reflection,
    const SwapContext& context,
    int target_row,
    const std::string& tier) {
  std::vector<std::pair<RowKey, const ScoredWitness*>> ordered;
  ordered.reserve(records.size());
  for (const auto& [key, scored] : records) ordered.emplace_back(key, &scored);
  std::sort(ordered.begin(), ordered.end(), [](const auto& left, const auto& right) {
    const RankedKey left_rank{left.second->delta, left.second->hole_change, left.first};
    const RankedKey right_rank{right.second->delta, right.second->hole_change, right.first};
    return left_rank < right_rank;
  });
  std::ofstream output(path);
  if (!output) throw std::runtime_error("cannot write scored catalogue: " + path);
  output << "rows\tcore\torder\treflected_core\treflected_order"
            "\towner_ids\treflected_owner_ids\tbest_outgoing_pair_index"
            "\tdelta\tnew_energy\thole_change\tholes_filled\tadd_base"
            "\tcovered_incumbent_holes\ttarget_row\ttier\n";
  for (const auto& [key, scored] : ordered) {
    std::array<uint8_t, CORE_SIZE> reflected_core{};
    for (int i = 0; i < CORE_SIZE; ++i) {
      reflected_core[i] = static_cast<uint8_t>(
          (-static_cast<int>(scored->witness.core[i]) + K) % K
      );
    }
    std::sort(reflected_core.begin(), reflected_core.end());
    std::array<uint8_t, PERIOD> reflected_order{};
    std::array<uint16_t, PERIOD> reflected_owners{};
    for (int i = 0; i < PERIOD; ++i) {
      reflected_order[i] = static_cast<uint8_t>(
          (-static_cast<int>(scored->witness.order[i]) + K) % K
      );
      reflected_owners[i] = static_cast<uint16_t>(
          reflection[scored->witness.owner_ids[i]]
      );
    }
    std::vector<int> covered_holes;
    for (uint16_t row : key) {
      if (context.loads[row] == 0) covered_holes.push_back(row);
    }
    output << join_values(key) << '\t'
           << join_values(scored->witness.core) << '\t'
           << join_values(scored->witness.order) << '\t'
           << join_values(reflected_core) << '\t'
           << join_values(reflected_order) << '\t'
           << join_values(scored->witness.owner_ids) << '\t'
           << join_values(reflected_owners) << '\t'
           << scored->best_outgoing_pair_index << '\t'
           << scored->delta << '\t'
           << context.energy + scored->delta << '\t'
           << scored->hole_change << '\t'
           << scored->holes_filled << '\t'
           << scored->add_base << '\t'
           << join_values(covered_holes) << '\t'
           << target_row << '\t' << tier << '\n';
  }
}

}  // namespace

int main(int argc, char** argv) {
  try {
    const Arguments args = parse_arguments(argc, argv);
    omp_set_num_threads(args.threads);

    std::vector<uint32_t> canonical(MASK_COUNT);
    for (uint32_t mask = 0; mask < MASK_COUNT; ++mask) {
      uint32_t best = mask;
      for (int shift = 1; shift < K; ++shift) {
        best = std::min(best, rotate_mask(mask, shift));
      }
      canonical[mask] = best;
    }

    std::vector<uint32_t> representatives;
    std::vector<int> orbit_index(MASK_COUNT, -1);
    for (uint32_t mask = 0; mask < MASK_COUNT; ++mask) {
      if (std::popcount(mask) == OWNER_RANK && canonical[mask] == mask) {
        orbit_index[mask] = static_cast<int>(representatives.size());
        representatives.push_back(mask);
      }
    }
    if (representatives.size() != 1430) throw std::runtime_error("owner orbit count");

    std::array<int, 1430> reflection{};
    for (int id = 0; id < 1430; ++id) {
      const uint32_t mate_mask = canonical[negate_mask(representatives[id])];
      const int mate = orbit_index[mate_mask];
      if (mate < 0) throw std::runtime_error("missing reflected owner");
      reflection[id] = mate;
    }

    std::array<int, 1430> reduced_row{};
    reduced_row.fill(-1);
    std::vector<int> nonfixed_representatives;
    for (int id = 0; id < 1430; ++id) {
      if (id < reflection[id]) {
        const int row = static_cast<int>(nonfixed_representatives.size());
        nonfixed_representatives.push_back(id);
        reduced_row[id] = reduced_row[reflection[id]] = row;
      }
    }
    if (nonfixed_representatives.size() != 680) {
      throw std::runtime_error("nonfixed row count");
    }

    const int target_owner_id = nonfixed_representatives[args.target_row];
    const uint32_t target_owner = representatives[target_owner_id];
    std::vector<int> target_values;
    std::vector<int> outside_values;
    for (int value = 0; value < K; ++value) {
      ((target_owner >> value) & 1U ? target_values : outside_values).push_back(value);
    }
    if (target_values.size() != 9 || outside_values.size() != 8) {
      throw std::runtime_error("target rank");
    }

    std::vector<Anchor> anchors;
    for (int a = 0; a < 5; ++a)
      for (int b = a + 1; b < 6; ++b)
        for (int c = b + 1; c < 7; ++c)
          for (int d = c + 1; d < 8; ++d)
            for (int e = d + 1; e < 9; ++e) {
              const std::array<int, 5> chosen{a, b, c, d, e};
              std::array<bool, 9> in_core{};
              Anchor seed;
              for (int i = 0; i < 5; ++i) {
                in_core[chosen[i]] = true;
                seed.core[i] = static_cast<uint8_t>(target_values[chosen[i]]);
                seed.core_mask |= 1U << target_values[chosen[i]];
              }
              std::array<int, 4> window{};
              int position = 0;
              for (int i = 0; i < 9; ++i) {
                if (!in_core[i]) window[position++] = static_cast<uint8_t>(target_values[i]);
              }
              std::sort(window.begin(), window.end());
              do {
                for (int i = 0; i < 4; ++i) {
                  seed.window[i] = static_cast<uint8_t>(window[i]);
                }
                anchors.push_back(seed);
              } while (std::next_permutation(window.begin(), window.end()));
            }
    if (anchors.size() != 126 * 24) throw std::runtime_error("anchor count");

    std::vector<std::array<uint8_t, 6>> outside_orders;
    std::array<int, 8> outside{};
    for (int i = 0; i < 8; ++i) outside[i] = outside_values[i];
    std::sort(outside.begin(), outside.end());
    do {
      if (outside[6] < outside[7]) {
        std::array<uint8_t, 6> order{};
        for (int i = 0; i < 6; ++i) order[i] = static_cast<uint8_t>(outside[i]);
        outside_orders.push_back(order);
      }
    } while (std::next_permutation(outside.begin(), outside.end()));
    if (outside_orders.size() != 20160) throw std::runtime_error("outside order count");

    uint64_t existing_pair_lines = 0;
    const auto existing = read_existing_pairs(args.instance, existing_pair_lines);
    const auto allowed = read_allowed_rows(args.allowed_rows);
    if (allowed && !(*allowed)[args.target_row]) {
      throw std::runtime_error("allowed rows omit target row");
    }
    const std::optional<SwapContext> swap_context = (
        args.swap_context.empty()
        ? std::nullopt
        : std::optional<SwapContext>(read_swap_context(args.swap_context))
    );

    using Catalogue = std::unordered_map<RowKey, Witness, RowKeyHash>;
    const int worker_count = std::min(args.threads, omp_get_max_threads());
    std::vector<Catalogue> local_catalogues(worker_count);
    std::vector<Counters> local_counters(worker_count);
    std::vector<std::unordered_set<RowKey, RowKeyHash>> local_frozen_seen(
        worker_count
    );
    std::vector<BoundedTop> local_tops;
    std::vector<std::vector<BoundedTop>> local_reservoirs;
    local_tops.reserve(worker_count);
    local_reservoirs.reserve(worker_count);
    for (int thread = 0; thread < worker_count; ++thread) {
      local_tops.emplace_back(swap_context ? args.top_k : 0);
      local_reservoirs.emplace_back();
      if (swap_context) {
        local_reservoirs.back().reserve(swap_context->holes.size());
        for (std::size_t i = 0; i < swap_context->holes.size(); ++i) {
          local_reservoirs.back().emplace_back(args.reservoir_per_hole);
        }
      }
    }

#pragma omp parallel
    {
      const int thread = omp_get_thread_num();
      Catalogue& catalogue = local_catalogues[thread];
      Counters& counts = local_counters[thread];
      if (swap_context) local_frozen_seen[thread].reserve(512);
      else catalogue.reserve(65536);

#pragma omp for schedule(dynamic, 1)
      for (std::size_t anchor_index = 0; anchor_index < anchors.size(); ++anchor_index) {
        const Anchor& anchor = anchors[anchor_index];
        for (const auto& tail : outside_orders) {
          ++counts.raw_anchored;
          Witness witness;
          witness.core = anchor.core;
          std::copy(anchor.window.begin(), anchor.window.end(), witness.order.begin());
          std::copy(tail.begin(), tail.end(), witness.order.begin() + 4);

          std::array<uint16_t, PERIOD> ids{};
          bool missing = false;
          for (int start = 0; start < PERIOD; ++start) {
            uint32_t owner = anchor.core_mask;
            for (int offset = 0; offset < 4; ++offset) {
              owner |= 1U << witness.order[(start + offset) % PERIOD];
            }
            const int id = orbit_index[canonical[owner]];
            if (id < 0) {
              missing = true;
              break;
            }
            ids[start] = static_cast<uint16_t>(id);
          }
          if (missing || ids[0] != target_owner_id) {
            throw std::runtime_error("anchored owner mismatch");
          }
          std::array<uint16_t, PERIOD> sorted_ids = ids;
          std::sort(sorted_ids.begin(), sorted_ids.end());
          if (std::adjacent_find(sorted_ids.begin(), sorted_ids.end()) != sorted_ids.end()) {
            continue;
          }
          ++counts.quotient_simple;

          bool disjoint = true;
          for (uint16_t id : ids) {
            if (std::binary_search(sorted_ids.begin(), sorted_ids.end(),
                                   static_cast<uint16_t>(reflection[id]))) {
              disjoint = false;
              break;
            }
          }
          if (!disjoint) continue;
          ++counts.reflection_disjoint;

          RowKey key{};
          for (int i = 0; i < PERIOD; ++i) {
            const int row = reduced_row[ids[i]];
            if (row < 0) throw std::runtime_error("fixed owner after disjointness");
            key[i] = static_cast<uint16_t>(row);
          }
          std::sort(key.begin(), key.end());
          if (std::adjacent_find(key.begin(), key.end()) != key.end()) {
            throw std::runtime_error("repeated reduced row");
          }
          if (!std::binary_search(key.begin(), key.end(),
                                  static_cast<uint16_t>(args.target_row))) {
            throw std::runtime_error("target row lost");
          }
          if (allowed) {
            bool inside = true;
            for (uint16_t row : key) inside = inside && (*allowed)[row];
            if (!inside) continue;
          }
          ++counts.allowed;
          witness.owner_ids = ids;
          if (swap_context) {
            if (existing.contains(key)) {
              local_frozen_seen[thread].insert(key);
              continue;
            }
            const ScoredWitness scored = score_swap(key, witness, *swap_context);
            local_tops[thread].consider(key, scored);
            for (std::size_t hole_index = 0;
                 hole_index < swap_context->holes.size(); ++hole_index) {
              const int hole = swap_context->holes[hole_index];
              if (std::binary_search(key.begin(), key.end(),
                                     static_cast<uint16_t>(hole))) {
                local_reservoirs[thread][hole_index].consider(key, scored);
              }
            }
          } else {
            auto [iterator, inserted] = catalogue.emplace(key, witness);
            if (!inserted && witness_less(witness, iterator->second)) {
              iterator->second = witness;
            }
          }
        }
      }
    }

    Counters counts;
    std::size_t local_total = 0;
    for (const auto& current : local_counters) counts += current;
    for (const auto& catalogue : local_catalogues) local_total += catalogue.size();

    uint64_t existing_unique_target = 0;
    uint64_t existing_unique_target_allowed = 0;
    for (const RowKey& key : existing) {
      if (!std::binary_search(key.begin(), key.end(),
                              static_cast<uint16_t>(args.target_row))) continue;
      ++existing_unique_target;
      bool inside = true;
      if (allowed) for (uint16_t row : key) inside = inside && (*allowed)[row];
      if (inside) ++existing_unique_target_allowed;
    }

    const uint64_t expected_raw = 126ULL * 24ULL * 20160ULL;
    if (counts.raw_anchored != expected_raw) throw std::runtime_error("raw count");

    if (swap_context) {
      std::unordered_set<RowKey, RowKeyHash> frozen_seen;
      frozen_seen.reserve(512);
      for (const auto& local : local_frozen_seen) {
        frozen_seen.insert(local.begin(), local.end());
      }
      if (frozen_seen.size() != existing_unique_target_allowed) {
        throw std::runtime_error("top mode did not regenerate every frozen target mask");
      }

      BoundedTop top(args.top_k);
      for (const BoundedTop& local : local_tops) {
        for (const auto& [key, scored] : local.records()) top.consider(key, scored);
      }
      std::vector<BoundedTop> reservoirs;
      reservoirs.reserve(swap_context->holes.size());
      for (std::size_t hole_index = 0;
           hole_index < swap_context->holes.size(); ++hole_index) {
        reservoirs.emplace_back(args.reservoir_per_hole);
        for (int thread = 0; thread < worker_count; ++thread) {
          for (const auto& [key, scored] :
               local_reservoirs[thread][hole_index].records()) {
            reservoirs.back().consider(key, scored);
          }
        }
      }
      std::unordered_map<RowKey, ScoredWitness, RowKeyHash> reservoir_union;
      reservoir_union.reserve(
          swap_context->holes.size() * args.reservoir_per_hole
      );
      for (const BoundedTop& reservoir : reservoirs) {
        for (const auto& [key, scored] : reservoir.records()) {
          auto [iterator, inserted] = reservoir_union.emplace(key, scored);
          if (!inserted && witness_less(scored.witness, iterator->second.witness)) {
            iterator->second.witness = scored.witness;
          }
        }
      }
      write_scored_catalogue(
          args.top_catalog, top.records(), reflection, *swap_context,
          args.target_row, "top"
      );
      write_scored_catalogue(
          args.reservoir_catalog, reservoir_union, reflection, *swap_context,
          args.target_row, "reservoir"
      );

      const auto best = std::min_element(
          top.records().begin(), top.records().end(),
          [](const auto& left, const auto& right) {
            return RankedKey{left.second.delta, left.second.hole_change, left.first}
                 < RankedKey{right.second.delta, right.second.hole_change, right.first};
          }
      );
      if (best == top.records().end()) throw std::runtime_error("empty top catalogue");
      std::map<int, uint64_t> delta_histogram;
      std::map<int, uint64_t> hole_change_histogram;
      for (const auto& [key, scored] : top.records()) {
        (void)key;
        ++delta_histogram[scored.delta];
        ++hole_change_histogram[scored.hole_change];
      }
      std::map<int, uint64_t> reservoir_hole_coverage;
      for (int hole : swap_context->holes) reservoir_hole_coverage[hole] = 0;
      for (const auto& [key, scored] : reservoir_union) {
        (void)scored;
        for (uint16_t row : key) {
          if (swap_context->loads[row] == 0) ++reservoir_hole_coverage[row];
        }
      }

      auto emit_histogram = [](const auto& histogram) {
        std::cout << '{';
        bool first = true;
        for (const auto& [key, value] : histogram) {
          if (!first) std::cout << ',';
          first = false;
          std::cout << "\"" << key << "\":" << value;
        }
        std::cout << '}';
      };
      std::cout << "{\n";
      std::cout << "  \"status\": \"PASS\",\n";
      std::cout << "  \"mode\": \"streaming_topk_incumbent_swap\",\n";
      std::cout << "  \"target_row\": " << args.target_row << ",\n";
      std::cout << "  \"target_owner_id\": " << target_owner_id << ",\n";
      std::cout << "  \"threads\": " << worker_count << ",\n";
      std::cout << "  \"raw_parameter_count\": " << counts.raw_anchored << ",\n";
      std::cout << "  \"quotient_simple_raw\": " << counts.quotient_simple << ",\n";
      std::cout << "  \"reflection_disjoint_raw\": "
                << counts.reflection_disjoint << ",\n";
      std::cout << "  \"frozen_target_masks_regenerated\": "
                << frozen_seen.size() << ",\n";
      std::cout << "  \"top_k_requested\": " << args.top_k << ",\n";
      std::cout << "  \"top_k_retained\": " << top.records().size() << ",\n";
      std::cout << "  \"reservoir_per_hole\": " << args.reservoir_per_hole << ",\n";
      std::cout << "  \"reservoir_union_masks\": " << reservoir_union.size() << ",\n";
      std::cout << "  \"incumbent_energy\": " << swap_context->energy << ",\n";
      std::cout << "  \"best_delta\": " << best->second.delta << ",\n";
      std::cout << "  \"best_new_energy\": "
                << swap_context->energy + best->second.delta << ",\n";
      std::cout << "  \"best_hole_change\": " << best->second.hole_change << ",\n";
      std::cout << "  \"best_holes_filled\": " << best->second.holes_filled << ",\n";
      std::cout << "  \"best_outgoing_pair_index\": "
                << best->second.best_outgoing_pair_index << ",\n";
      std::cout << "  \"best_rows\":";
      emit_json_key(std::cout, best->first);
      std::cout << ",\n  \"top_delta_histogram\":";
      emit_histogram(delta_histogram);
      std::cout << ",\n  \"top_hole_change_histogram\":";
      emit_histogram(hole_change_histogram);
      std::cout << ",\n  \"reservoir_hole_coverage\":";
      emit_histogram(reservoir_hole_coverage);
      std::cout << ",\n";
      std::cout << "  \"top_catalog\": \"" << args.top_catalog << "\",\n";
      std::cout << "  \"reservoir_catalog\": \""
                << args.reservoir_catalog << "\",\n";
      std::cout << "  \"artifact_schema\": \"rows,core,order,reflected_core,reflected_order,owner_ids,reflected_owner_ids,best_outgoing_pair_index,delta,new_energy,hole_change,holes_filled,add_base,covered_incumbent_holes,target_row,tier\",\n";
      std::cout << "  \"scope\": \"exact scoring of every generated new mask; bounded deterministic top-K per shard is sufficient for the global top-K; per-hole reservoirs are independently bounded and union-deduplicated\"\n";
      std::cout << "}\n";
      return 0;
    }

    Catalogue catalogue;
    catalogue.reserve(static_cast<std::size_t>(local_total * 1.15) + 1);
    for (auto& local : local_catalogues) {
      for (auto& [key, witness] : local) {
        auto [iterator, inserted] = catalogue.emplace(key, witness);
        if (!inserted && witness_less(witness, iterator->second)) {
          iterator->second = witness;
        }
      }
      Catalogue().swap(local);
    }

    uint64_t overlap = 0;
    std::array<uint64_t, 680> new_coverage{};
    std::vector<std::pair<RowKey, const Witness*>> sample;
    sample.reserve(args.sample_limit + 1);
    for (const auto& [key, witness] : catalogue) {
      const bool old = existing.contains(key);
      overlap += old;
      for (uint16_t row : key) {
        if (!old) ++new_coverage[row];
      }
      if (args.sample_limit > 0) {
        if (static_cast<int>(sample.size()) < args.sample_limit) {
          sample.emplace_back(key, &witness);
        } else {
          const auto largest = std::max_element(
              sample.begin(), sample.end(),
              [](const auto& left, const auto& right) { return left.first < right.first; });
          if (key < largest->first) *largest = {key, &witness};
        }
      }
    }
    std::sort(sample.begin(), sample.end(),
              [](const auto& left, const auto& right) { return left.first < right.first; });
    if (overlap != existing_unique_target_allowed) {
      throw std::runtime_error("frozen target masks were not all regenerated");
    }

    if (!args.catalog.empty()) {
      std::vector<std::pair<RowKey, const Witness*>> ordered;
      ordered.reserve(catalogue.size());
      for (const auto& [key, witness] : catalogue) ordered.emplace_back(key, &witness);
      std::sort(ordered.begin(), ordered.end(),
                [](const auto& left, const auto& right) { return left.first < right.first; });
      std::ofstream output(args.catalog);
      if (!output) throw std::runtime_error("cannot write catalogue");
      output << "rows\tcore\torder\towner_ids\tstatus\n";
      for (const auto& [key, witness] : ordered) {
        output << join_values(key) << '\t' << join_values(witness->core) << '\t'
               << join_values(witness->order) << '\t'
               << join_values(witness->owner_ids) << '\t'
               << (existing.contains(key) ? "frozen" : "new") << '\n';
      }
    }

    std::cout << "{\n";
    std::cout << "  \"status\": \"PASS\",\n";
    std::cout << "  \"target_row\": " << args.target_row << ",\n";
    std::cout << "  \"target_owner_id\": " << target_owner_id << ",\n";
    std::cout << "  \"target_owner_mask\": " << target_owner << ",\n";
    std::cout << "  \"threads\": " << worker_count << ",\n";
    std::cout << "  \"raw_parameter_count\": " << counts.raw_anchored << ",\n";
    std::cout << "  \"quotient_simple_raw\": " << counts.quotient_simple << ",\n";
    std::cout << "  \"reflection_disjoint_raw\": " << counts.reflection_disjoint << ",\n";
    std::cout << "  \"allowed_raw\": " << counts.allowed << ",\n";
    std::cout << "  \"thread_local_unique_sum\": " << local_total << ",\n";
    std::cout << "  \"unique_pair_masks\": " << catalogue.size() << ",\n";
    std::cout << "  \"frozen_pair_lines\": " << existing_pair_lines << ",\n";
    std::cout << "  \"frozen_unique_pair_masks\": " << existing.size() << ",\n";
    std::cout << "  \"frozen_unique_target_masks\": " << existing_unique_target << ",\n";
    std::cout << "  \"frozen_unique_target_allowed_masks\": "
              << existing_unique_target_allowed << ",\n";
    std::cout << "  \"regenerated_frozen_target_masks\": " << overlap << ",\n";
    std::cout << "  \"genuinely_new_pair_masks\": " << catalogue.size() - overlap << ",\n";
    std::cout << "  \"allowed_filter\": ";
    if (args.allowed_rows.empty()) std::cout << "null,\n";
    else std::cout << "\"" << args.allowed_rows << "\",\n";
    std::cout << "  \"catalogue\": ";
    if (args.catalog.empty()) std::cout << "null,\n";
    else std::cout << "\"" << args.catalog << "\",\n";
    std::cout << "  \"new_row_coverage\": {";
    bool first = true;
    for (int row = 0; row < 680; ++row) {
      if (!new_coverage[row]) continue;
      if (!first) std::cout << ',';
      first = false;
      std::cout << "\"" << row << "\":" << new_coverage[row];
    }
    std::cout << "},\n";
    std::cout << "  \"samples\": [\n";
    for (std::size_t i = 0; i < sample.size(); ++i) {
      const auto& [key, witness] = sample[i];
      std::cout << "    {\"rows\":";
      emit_json_key(std::cout, key);
      std::cout << ",\"core\":";
      emit_json_small_array(std::cout, witness->core);
      std::cout << ",\"order\":";
      emit_json_small_array(std::cout, witness->order);
      std::cout << ",\"owner_ids\":";
      emit_json_small_array(std::cout, witness->owner_ids);
      std::cout << ",\"frozen\":" << (existing.contains(key) ? "true" : "false") << '}';
      if (i + 1 != sample.size()) std::cout << ',';
      std::cout << '\n';
    }
    std::cout << "  ],\n";
    std::cout << "  \"scope\": \"all anchored q4 period-10 rails containing the target owner necklace; optional allowed-row subset; deduplication by ten-row reflected-pair mask\"\n";
    std::cout << "}\n";
    return 0;
  } catch (const std::exception& error) {
    std::cerr << "ERROR: " << error.what() << '\n';
    return 1;
  }
}
