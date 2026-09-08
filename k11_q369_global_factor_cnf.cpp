#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace gf11 {

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int M = 462;
constexpr int SIGMA = 369;
constexpr int N = 465;
constexpr int FACTOR_VARIABLES = N * K;

struct Interval { int left, right; };

static int pc(Mask value) {
    return popcount(static_cast<unsigned>(value));
}

static array<Interval, M> make_central() {
    array<Interval, M> result{};
    for (int i = 0; i < M; ++i)
        result[i] = {i, i + (i < SIGMA ? 2 : 3)};
    return result;
}

static const array<Interval, M> CENTRAL = make_central();

static vector<long long> read_numbers(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<long long> values;
    for (long long value; input >> value;) values.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    return values;
}

static vector<Mask> read_vector(const string& path, int wanted) {
    vector<long long> raw = read_numbers(path);
    if (raw.size() == static_cast<size_t>(wanted + 1) && raw.front() == wanted)
        raw.erase(raw.begin());
    if (raw.size() != static_cast<size_t>(wanted))
        throw runtime_error(path + " must contain " + to_string(wanted) + " values");
    vector<Mask> result;
    result.reserve(wanted);
    for (long long value : raw) {
        if (value < 0 || value >= LIMIT) throw runtime_error("mask out of range");
        result.push_back(static_cast<Mask>(value));
    }
    return result;
}

static bool rank6_permutation(const vector<Mask>& row, string* reason = nullptr) {
    if (row.size() != M) {
        if (reason) *reason = "wrong row length";
        return false;
    }
    array<uint8_t, LIMIT> count{};
    for (Mask value : row) {
        if (pc(value) != 6 || ++count[value] != 1) {
            if (reason) *reason = "row is not a rank-six permutation";
            return false;
        }
    }
    for (int value = 1; value < LIMIT; ++value)
        if (pc(static_cast<Mask>(value)) == 6 && !count[value]) {
            if (reason) *reason = "row omits a rank-six mask";
            return false;
        }
    return true;
}

static array<Mask, N> envelopes(const vector<Mask>& row) {
    array<Mask, N> result;
    result.fill(static_cast<Mask>(FULL));
    for (int i = 0; i < M; ++i)
        for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
            result[p] &= row[i];
    return result;
}

static array<uint8_t, LIMIT> row_union_coverage(const vector<Mask>& row) {
    array<uint8_t, LIMIT> seen{};
    vector<Mask> previous, current;
    for (Mask x : row) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (Mask value : current) seen[value] = 1;
        previous.swap(current);
    }
    return seen;
}

class Cnf {
public:
    explicit Cnf(bool store) : store_(store) {}

    int new_variable() { return ++variables_; }
    int variables() const { return variables_; }
    long long clauses() const { return clauses_; }
    long long literals() const { return literals_; }
    const vector<int>& raw_data() const { return data_; }

    void set_base_variables(int count) { variables_ = count; }

    void add(const vector<int>& clause) {
        ++clauses_;
        literals_ += static_cast<long long>(clause.size());
        if (store_) {
            data_.insert(data_.end(), clause.begin(), clause.end());
            data_.push_back(0);
        }
    }

    void add(initializer_list<int> clause) { add(vector<int>(clause)); }

    // Monotone sequential counter.  State s[i][j] means that the first i
    // inputs contain at least j true literals.  Only forward implications are
    // needed for an at-most constraint; the final overflow clauses forbid a
    // (maximum + 1)-st true input.
    void at_most_k(const vector<int>& inputs, int maximum) {
        if (maximum < 0) throw runtime_error("negative cardinality bound");
        if (maximum >= static_cast<int>(inputs.size())) return;
        if (maximum == 0) {
            for (int input : inputs) add({-input});
            return;
        }
        vector<int> previous;
        for (int input : inputs) {
            vector<int> current(maximum);
            for (int& variable : current) variable = new_variable();
            add({-input, current[0]});
            for (int j = 0; j < static_cast<int>(previous.size()); ++j)
                add({-previous[j], current[j]});
            for (int j = 0; j + 1 < static_cast<int>(previous.size()) &&
                            j + 1 < maximum; ++j)
                add({-input, -previous[j], current[j + 1]});
            if (static_cast<int>(previous.size()) == maximum)
                add({-input, -previous[maximum - 1]});
            previous.swap(current);
        }
    }

    void write(const string& path) const {
        if (!store_) throw runtime_error("CNF storage disabled");
        ofstream output(path);
        if (!output) throw runtime_error("cannot write " + path);
        output << "p cnf " << variables_ << ' ' << clauses_ << '\n';
        for (int literal : data_) {
            output << literal;
            if (literal == 0) output << '\n';
            else output << ' ';
        }
    }

private:
    bool store_ = false;
    int variables_ = 0;
    long long clauses_ = 0;
    long long literals_ = 0;
    vector<int> data_;
};

static int xvar(int position, int bit) {
    return position * K + bit + 1;
}

struct Stats {
    long long attempted = 0;
    long long kept = 0;
    long long prune_envelope = 0;
    long long prune_nonzero = 0;
    long long prune_central = 0;
    long long prune_pin = 0;
    array<long long, K + 1> selectors_by_rank{};
    array<int, K + 1> targets_by_rank{};
    int empty_targets = 0;
    int central_empty_pins = 0;
    int missing_upper_targets = 0;
    int encoded_upper_targets = 0;
    vector<Mask> empty_target_masks;
};

struct SelectorInfo {
    int variable;
    Mask target;
    Interval interval;
};

struct DropInfo {
    int variable;
    Mask target;
};

struct GuardInfo {
    int variable;
    Mask target;
};

class Generator {
public:
    Generator(vector<Mask> row, bool store, bool encode_missing_upper,
              int max_lower_drops = -1, bool guard_lower_targets = false)
        : row_(std::move(row)), envelope_(envelopes(row_)), cnf_(store),
          encode_missing_upper_(encode_missing_upper),
          max_lower_drops_(max_lower_drops),
          guard_lower_targets_(guard_lower_targets) {
        if (max_lower_drops_ > 1023)
            throw runtime_error("lower-drop bound exceeds 1023 targets");
        if (max_lower_drops_ >= 0 && guard_lower_targets_)
            throw runtime_error("drop relaxation and target guards are mutually exclusive");
        cnf_.set_base_variables(FACTOR_VARIABLES);
        upper_seen_ = row_union_coverage(row_);
    }

    void generate() {
        add_central_constraints();
        for (int target = 1; target < LIMIT; ++target) {
            const Mask mask = static_cast<Mask>(target);
            const int rank = pc(mask);
            if (rank <= 5) {
                add_target(mask, 3, max_lower_drops_ >= 0,
                           guard_lower_targets_);
            } else if (rank >= 7 && !upper_seen_[mask]) {
                ++stats_.missing_upper_targets;
                if (encode_missing_upper_) {
                    ++stats_.encoded_upper_targets;
                    add_target(mask, length_cap(rank));
                }
            }
        }
        if (max_lower_drops_ >= 0) {
            vector<int> variables;
            variables.reserve(drop_info_.size());
            for (const DropInfo& info : drop_info_) variables.push_back(info.variable);
            cnf_.at_most_k(variables, max_lower_drops_);
        }
    }

    void generate_only(const vector<Mask>& targets) {
        add_central_constraints();
        array<uint8_t, LIMIT> used{};
        for (Mask target : targets) {
            if (!target || pc(target) > 5)
                throw runtime_error("filtered target must have rank 1 through 5");
            if (used[target]++) throw runtime_error("duplicate filtered target");
            add_target(target, 3);
        }
    }

    const Stats& stats() const { return stats_; }
    const Cnf& cnf() const { return cnf_; }
    const vector<SelectorInfo>& selectors() const { return selector_info_; }
    const vector<DropInfo>& drops() const { return drop_info_; }
    const vector<GuardInfo>& guards() const { return guard_info_; }
    int max_lower_drops() const { return max_lower_drops_; }

private:
    vector<Mask> row_;
    array<Mask, N> envelope_{};
    array<uint8_t, LIMIT> upper_seen_{};
    Cnf cnf_;
    Stats stats_;
    vector<SelectorInfo> selector_info_;
    vector<DropInfo> drop_info_;
    vector<GuardInfo> guard_info_;
    bool encode_missing_upper_ = false;
    int max_lower_drops_ = -1;
    bool guard_lower_targets_ = false;

    static int length_cap(int rank) {
        static constexpr array<int, K + 1> cap{
            0, 3, 3, 3, 3, 3, 4, 10, 31, 87, 213, 465,
        };
        return cap[rank];
    }

    void add_central_constraints() {
        for (int p = 0; p < N; ++p) {
            vector<int> nonzero;
            for (int bit = 0; bit < K; ++bit) {
                if (envelope_[p] & (1u << bit)) nonzero.push_back(xvar(p, bit));
                else cnf_.add({-xvar(p, bit)});
            }
            if (nonzero.empty()) ++stats_.central_empty_pins;
            cnf_.add(nonzero);
        }
        for (int i = 0; i < M; ++i) {
            for (int bit = 0; bit < K; ++bit) {
                if (!(row_[i] & (1u << bit))) continue;
                vector<int> hit;
                for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
                    if (envelope_[p] & (1u << bit)) hit.push_back(xvar(p, bit));
                if (hit.empty()) ++stats_.central_empty_pins;
                cnf_.add(hit);
            }
        }
    }

    bool compatible(Mask target, Interval interval) {
        ++stats_.attempted;
        Mask union_envelope = 0;
        for (int p = interval.left; p <= interval.right; ++p)
            union_envelope |= envelope_[p];
        if (target & static_cast<Mask>(~union_envelope)) {
            ++stats_.prune_envelope;
            return false;
        }
        for (int p = interval.left; p <= interval.right; ++p) {
            if (!(target & envelope_[p])) {
                ++stats_.prune_nonzero;
                return false;
            }
        }

        const int first_central = max(0, interval.left - 3);
        const int last_central = min(M - 1, interval.right);
        for (int i = first_central; i <= last_central; ++i) {
            if (interval.left <= CENTRAL[i].left &&
                CENTRAL[i].right <= interval.right &&
                (row_[i] & static_cast<Mask>(~target))) {
                ++stats_.prune_central;
                return false;
            }
        }

        for (int i = first_central; i <= last_central; ++i) {
            Mask omitted = row_[i] & static_cast<Mask>(~target);
            while (omitted) {
                const int bit = countr_zero(static_cast<unsigned>(omitted));
                bool has_pin = false, has_pin_outside = false;
                for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p) {
                    if (!(envelope_[p] & (1u << bit))) continue;
                    has_pin = true;
                    if (p < interval.left || p > interval.right)
                        has_pin_outside = true;
                }
                if (has_pin && !has_pin_outside) {
                    ++stats_.prune_pin;
                    return false;
                }
                omitted &= static_cast<Mask>(omitted - 1);
            }
        }
        ++stats_.kept;
        return true;
    }

    void add_witness(Mask target, Interval interval, int selector, int guard = 0) {
        for (int p = interval.left; p <= interval.right; ++p) {
            Mask forbidden = envelope_[p] & static_cast<Mask>(~target);
            while (forbidden) {
                const int bit = countr_zero(static_cast<unsigned>(forbidden));
                vector<int> clause;
                if (guard) clause.push_back(-guard);
                clause.push_back(-selector);
                clause.push_back(-xvar(p, bit));
                cnf_.add(clause);
                forbidden &= static_cast<Mask>(forbidden - 1);
            }
        }
        Mask required = target;
        while (required) {
            const int bit = countr_zero(static_cast<unsigned>(required));
            vector<int> hit;
            if (guard) hit.push_back(-guard);
            hit.push_back(-selector);
            for (int p = interval.left; p <= interval.right; ++p)
                if (envelope_[p] & (1u << bit)) hit.push_back(xvar(p, bit));
            cnf_.add(hit);
            required &= static_cast<Mask>(required - 1);
        }
    }

    void add_target(Mask target, int cap, bool droppable = false,
                    bool guarded = false) {
        const int rank = pc(target);
        ++stats_.targets_by_rank[rank];
        int guard = 0;
        if (guarded) {
            guard = cnf_.new_variable();
            guard_info_.push_back({guard, target});
        }
        vector<int> witnesses;
        for (int length = 1; length <= min(cap, N); ++length) {
            for (int left = 0; left + length <= N; ++left) {
                const Interval interval{left, left + length - 1};
                if (!compatible(target, interval)) continue;
                const int selector = cnf_.new_variable();
                witnesses.push_back(selector);
                selector_info_.push_back({selector, target, interval});
                ++stats_.selectors_by_rank[rank];
                add_witness(target, interval, selector, guard);
            }
        }
        if (witnesses.empty()) {
            ++stats_.empty_targets;
            stats_.empty_target_masks.push_back(target);
        }
        if (droppable) {
            const int drop = cnf_.new_variable();
            drop_info_.push_back({drop, target});
            witnesses.push_back(drop);
        }
        if (guard) witnesses.insert(witnesses.begin(), -guard);
        cnf_.add(witnesses);
    }
};

static void write_selector_map(const string& path, const Generator& generator) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    output << "variable\ttarget\trank\tleft\tright\tlength\n";
    for (const SelectorInfo& info : generator.selectors()) {
        output << info.variable << '\t' << static_cast<int>(info.target) << '\t'
               << pc(info.target) << '\t' << info.interval.left + 1 << '\t'
               << info.interval.right + 1 << '\t'
               << info.interval.right - info.interval.left + 1 << '\n';
    }
}

static void write_drop_map(const string& path, const Generator& generator) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    output << "variable\ttarget\trank\n";
    for (const DropInfo& info : generator.drops())
        output << info.variable << '\t' << static_cast<int>(info.target) << '\t'
               << pc(info.target) << '\n';
}

static void write_guard_files(const string& assumptions_path,
                              const string& map_path,
                              const Generator& generator) {
    ofstream assumptions(assumptions_path);
    if (!assumptions) throw runtime_error("cannot write " + assumptions_path);
    assumptions << "c " << generator.guards().size()
                << " lower-target guard assumptions\n";
    assumptions << 'a';
    for (const GuardInfo& info : generator.guards())
        assumptions << ' ' << info.variable;
    assumptions << " 0\n";

    ofstream map(map_path);
    if (!map) throw runtime_error("cannot write " + map_path);
    map << "variable\ttarget\trank\n";
    for (const GuardInfo& info : generator.guards())
        map << info.variable << '\t' << static_cast<int>(info.target) << '\t'
            << pc(info.target) << '\n';
}

struct HallResult {
    struct Component {
        vector<Mask> targets;
        vector<Interval> intervals;
    };
    int matching = 0;
    vector<Mask> unmatched;
    vector<Mask> deficient_targets;
    vector<Interval> deficient_intervals;
    vector<Component> components;
};

static int short_interval_id(Interval interval) {
    const int length = interval.right - interval.left + 1;
    int offset = 0;
    for (int old_length = 1; old_length < length; ++old_length)
        offset += N - old_length + 1;
    return offset + interval.left;
}

static Interval short_interval_from_id(int id) {
    for (int length = 1; length <= 3; ++length) {
        const int count = N - length + 1;
        if (id < count) return {id, id + length - 1};
        id -= count;
    }
    throw runtime_error("invalid short interval id");
}

static HallResult short_interval_hall(const Generator& generator) {
    constexpr int TARGETS = 1023;
    constexpr int INTERVALS = 3 * N - 3;
    vector<Mask> targets;
    array<int, LIMIT> target_index;
    target_index.fill(-1);
    for (int value = 1; value < LIMIT; ++value) {
        const Mask mask = static_cast<Mask>(value);
        if (pc(mask) <= 5) {
            target_index[mask] = static_cast<int>(targets.size());
            targets.push_back(mask);
        }
    }
    if (targets.size() != TARGETS) throw runtime_error("lower target count");

    vector<vector<int>> edges(TARGETS);
    for (const SelectorInfo& selector : generator.selectors()) {
        if (pc(selector.target) > 5) continue;
        const int left = target_index[selector.target];
        const int right = short_interval_id(selector.interval);
        edges[left].push_back(right);
    }

    vector<int> left_match(TARGETS, -1), right_match(INTERVALS, -1), distance(TARGETS);
    auto bfs = [&]() {
        queue<int> todo;
        bool augmenting = false;
        for (int left = 0; left < TARGETS; ++left) {
            if (left_match[left] < 0) {
                distance[left] = 0;
                todo.push(left);
            } else {
                distance[left] = -1;
            }
        }
        while (!todo.empty()) {
            const int left = todo.front();
            todo.pop();
            for (int right : edges[left]) {
                const int next = right_match[right];
                if (next < 0) augmenting = true;
                else if (distance[next] < 0) {
                    distance[next] = distance[left] + 1;
                    todo.push(next);
                }
            }
        }
        return augmenting;
    };
    auto dfs = [&](auto&& self, int left) -> bool {
        for (int right : edges[left]) {
            const int next = right_match[right];
            if (next < 0 || (distance[next] == distance[left] + 1 && self(self, next))) {
                left_match[left] = right;
                right_match[right] = left;
                return true;
            }
        }
        distance[left] = -1;
        return false;
    };

    HallResult result;
    while (bfs())
        for (int left = 0; left < TARGETS; ++left)
            if (left_match[left] < 0 && dfs(dfs, left)) ++result.matching;

    vector<uint8_t> seen_left(TARGETS), seen_right(INTERVALS);
    queue<int> todo;
    for (int left = 0; left < TARGETS; ++left) {
        if (left_match[left] < 0) {
            result.unmatched.push_back(targets[left]);
            seen_left[left] = 1;
            todo.push(left);
        }
    }
    while (!todo.empty()) {
        const int left = todo.front();
        todo.pop();
        for (int right : edges[left]) {
            if (left_match[left] == right || seen_right[right]) continue;
            seen_right[right] = 1;
            const int next = right_match[right];
            if (next >= 0 && !seen_left[next]) {
                seen_left[next] = 1;
                todo.push(next);
            }
        }
    }
    for (int left = 0; left < TARGETS; ++left)
        if (seen_left[left]) result.deficient_targets.push_back(targets[left]);
    for (int right = 0; right < INTERVALS; ++right)
        if (seen_right[right]) result.deficient_intervals.push_back(short_interval_from_id(right));

    vector<vector<int>> reverse(INTERVALS);
    for (int left = 0; left < TARGETS; ++left)
        if (seen_left[left])
            for (int right : edges[left])
                if (seen_right[right]) reverse[right].push_back(left);
    vector<uint8_t> component_left(TARGETS), component_right(INTERVALS);
    for (int root = 0; root < TARGETS; ++root) {
        if (!seen_left[root] || component_left[root]) continue;
        HallResult::Component component;
        queue<pair<int, int>> pending;
        component_left[root] = 1;
        pending.push({0, root});
        while (!pending.empty()) {
            const auto [side, id] = pending.front();
            pending.pop();
            if (!side) {
                component.targets.push_back(targets[id]);
                for (int right : edges[id])
                    if (seen_right[right] && !component_right[right]) {
                        component_right[right] = 1;
                        pending.push({1, right});
                    }
            } else {
                component.intervals.push_back(short_interval_from_id(id));
                for (int left : reverse[id])
                    if (!component_left[left]) {
                        component_left[left] = 1;
                        pending.push({0, left});
                    }
            }
        }
        sort(component.targets.begin(), component.targets.end());
        sort(component.intervals.begin(), component.intervals.end(),
             [](Interval a, Interval b) { return pair{a.left, a.right} < pair{b.left, b.right}; });
        result.components.push_back(std::move(component));
    }
    sort(result.components.begin(), result.components.end(), [](const auto& a, const auto& b) {
        const int da = static_cast<int>(a.targets.size() - a.intervals.size());
        const int db = static_cast<int>(b.targets.size() - b.intervals.size());
        if (da != db) return da > db;
        return a.targets.size() < b.targets.size();
    });
    return result;
}

static void print_hall(const Generator& generator) {
    const HallResult hall = short_interval_hall(generator);
    cerr << "hall_targets=1023 hall_intervals=1392 hall_matching=" << hall.matching
         << " hall_deficiency=" << 1023 - hall.matching << '\n';
    cerr << "hall_unmatched_masks";
    for (Mask mask : hall.unmatched) cerr << ' ' << mask;
    cerr << '\n';
    cerr << "hall_witness_left=" << hall.deficient_targets.size()
         << " hall_witness_right=" << hall.deficient_intervals.size() << '\n';
    if (hall.deficient_targets.size() <= 256) {
        cerr << "hall_witness_masks";
        for (Mask mask : hall.deficient_targets) cerr << ' ' << mask;
        cerr << '\n';
    }
    if (hall.deficient_intervals.size() <= 256) {
        cerr << "hall_witness_intervals";
        for (Interval interval : hall.deficient_intervals)
            cerr << " [" << interval.left + 1 << ',' << interval.right + 1 << ']';
        cerr << '\n';
    }
    cerr << "hall_components=" << hall.components.size() << '\n';
    for (int index = 0; index < static_cast<int>(hall.components.size()); ++index) {
        const auto& component = hall.components[index];
        Mask common = static_cast<Mask>(FULL), united = 0;
        for (Mask mask : component.targets) common &= mask, united |= mask;
        cerr << "hall_component=" << index
             << " targets=" << component.targets.size()
             << " intervals=" << component.intervals.size()
             << " deficiency=" << component.targets.size() - component.intervals.size()
             << " common=" << static_cast<int>(common)
             << " union=" << static_cast<int>(united);
        if (component.targets.size() <= 64) {
            cerr << " masks";
            for (Mask mask : component.targets) cerr << ' ' << mask;
        }
        cerr << '\n';
    }
}

static void print_stats(const Generator& generator) {
    const Stats& s = generator.stats();
    const Cnf& cnf = generator.cnf();
    cerr << "factor_variables=" << FACTOR_VARIABLES
         << " selectors=" << s.kept
         << " drop_variables=" << generator.drops().size()
         << " guard_variables=" << generator.guards().size()
         << " max_lower_drops=" << generator.max_lower_drops()
         << " variables=" << cnf.variables()
         << " clauses=" << cnf.clauses()
         << " literals=" << cnf.literals() << '\n';
    cerr << "attempted=" << s.attempted
         << " pruned_envelope=" << s.prune_envelope
         << " pruned_nonzero=" << s.prune_nonzero
         << " pruned_central=" << s.prune_central
         << " pruned_pin=" << s.prune_pin << '\n';
    cerr << "central_empty_pins=" << s.central_empty_pins
         << " empty_targets=" << s.empty_targets
         << " missing_upper_targets=" << s.missing_upper_targets
         << " encoded_upper_targets=" << s.encoded_upper_targets << '\n';
    if (!s.empty_target_masks.empty()) {
        cerr << "empty_target_masks";
        for (Mask target : s.empty_target_masks) cerr << ' ' << target;
        cerr << '\n';
    }
    for (int rank = 1; rank <= K; ++rank)
        if (s.targets_by_rank[rank])
            cerr << "rank=" << rank << " targets=" << s.targets_by_rank[rank]
                 << " selectors=" << s.selectors_by_rank[rank] << '\n';
}

static vector<int8_t> read_model(const string& path, int maximum_variable) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    if (maximum_variable < FACTOR_VARIABLES)
        throw runtime_error("model variable limit is below factor variables");
    vector<int8_t> assignment(maximum_variable + 1, -1);
    string line;
    while (getline(input, line)) {
        size_t first = line.find_first_not_of(" \t\r");
        if (first == string::npos) continue;
        const char lead = line[first];
        if (lead == 'c' || lead == 's' || lead == 'S') continue;
        if (lead == 'v' || lead == 'V') ++first;
        else if (!(lead == '-' || isdigit(static_cast<unsigned char>(lead)))) continue;
        istringstream values(line.substr(first));
        for (long long literal; values >> literal;) {
            if (!literal) continue;
            const long long variable = literal < 0 ? -literal : literal;
            if (variable <= maximum_variable)
                assignment[variable] = literal > 0 ? 1 : 0;
        }
    }
    for (int variable = 1; variable <= FACTOR_VARIABLES; ++variable)
        if (assignment[variable] < 0)
            throw runtime_error("model omits factor variable " + to_string(variable));
    return assignment;
}

static vector<Mask> decode_factor(
    const vector<int8_t>& assignment) {
    vector<Mask> factor(N);
    for (int p = 0; p < N; ++p)
        for (int bit = 0; bit < K; ++bit)
            if (assignment[xvar(p, bit)] > 0)
                factor[p] |= static_cast<Mask>(1u << bit);
    return factor;
}

static Mask interval_or(const vector<Mask>& factor, Interval interval) {
    Mask result = 0;
    for (int p = interval.left; p <= interval.right; ++p) result |= factor[p];
    return result;
}

static bool verify_factor(const vector<Mask>& row, const vector<Mask>& factor,
                          bool require_universal, string* reason = nullptr,
                          const array<uint8_t, LIMIT>* allowed_lower_missing = nullptr,
                          vector<Mask>* actual_lower_missing = nullptr) {
    if (factor.size() != N) {
        if (reason) *reason = "wrong factor length";
        return false;
    }
    for (Mask value : factor) {
        if (!value || value >= LIMIT) {
            if (reason) *reason = "zero or out-of-range factor entry";
            return false;
        }
    }
    for (int i = 0; i < M; ++i) {
        if (interval_or(factor, CENTRAL[i]) != row[i]) {
            if (reason) *reason = "central mismatch at " + to_string(i + 1);
            return false;
        }
    }
    array<uint8_t, LIMIT> exhaustive{}, suffix{};
    for (int left = 0; left < N; ++left) {
        Mask value = 0;
        for (int right = left; right < N; ++right) {
            value |= factor[right];
            exhaustive[value] = 1;
        }
    }
    vector<Mask> previous, current;
    for (Mask x : factor) {
        current.clear();
        current.push_back(x);
        for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (Mask value : current) suffix[value] = 1;
        previous.swap(current);
    }
    for (int value = 1; value < LIMIT; ++value) {
        const int rank = pc(static_cast<Mask>(value));
        const bool covered = exhaustive[value] && suffix[value] &&
                             exhaustive[value] == suffix[value];
        if (rank <= 5 && !covered) {
            if (actual_lower_missing)
                actual_lower_missing->push_back(static_cast<Mask>(value));
            if (!allowed_lower_missing || !(*allowed_lower_missing)[value]) {
                if (reason) *reason = "unrelaxed coverage failure at " + to_string(value);
                return false;
            }
        }
        if (require_universal && !covered) {
            if (reason) *reason = "universal coverage failure at " + to_string(value);
            return false;
        }
    }
    return true;
}

static void write_factor(const string& path, const vector<Mask>& factor) {
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    for (int i = 0; i < N; ++i)
        output << static_cast<int>(factor[i]) << (i + 1 == N ? '\n' : ' ');
}

static void write_drop_report(const string& path, const vector<Mask>& relaxed,
                              const vector<Mask>& actual_missing) {
    array<uint8_t, LIMIT> missing{};
    for (Mask mask : actual_missing) missing[mask] = 1;
    ofstream output(path);
    if (!output) throw runtime_error("cannot write " + path);
    output << "target\trank\tactually_missing\n";
    for (Mask mask : relaxed)
        output << static_cast<int>(mask) << '\t' << pc(mask) << '\t'
               << static_cast<int>(missing[mask]) << '\n';
}

static int parse_drop_bound(const string& text) {
    size_t used = 0;
    const long long value = stoll(text, &used);
    if (used != text.size() || value < 0 || value > 1023)
        throw runtime_error("drop bound must be an integer in [0,1023]");
    return static_cast<int>(value);
}

static vector<Mask> read_target_list(const string& path) {
    const vector<long long> raw = read_numbers(path);
    vector<Mask> targets;
    targets.reserve(raw.size());
    for (long long value : raw) {
        if (value <= 0 || value >= LIMIT)
            throw runtime_error("filtered target out of range");
        targets.push_back(static_cast<Mask>(value));
    }
    return targets;
}

static void self_test() {
    if (FACTOR_VARIABLES != 5115) throw runtime_error("factor variable count");
    int early = 0, late = 0;
    for (int i = 0; i < M; ++i) {
        const int length = CENTRAL[i].right - CENTRAL[i].left + 1;
        early += length == 3;
        late += length == 4;
    }
    if (early != 369 || late != 93) throw runtime_error("central schedule");
    long long short_intervals = 0;
    for (int length = 1; length <= 3; ++length) short_intervals += N - length + 1;
    if (short_intervals != 1392 || short_intervals - early != 1023)
        throw runtime_error("short interval arithmetic");
    const array<int, 5> caps{10, 31, 87, 213, 465};
    if (caps[0] != 3 + 7 || caps[1] != 3 + 28 || caps[2] != 3 + 84 ||
        caps[3] != 3 + 210 || caps[4] != 465)
        throw runtime_error("upper length caps");
    {
        Cnf counter(true);
        vector<int> inputs;
        for (int i = 0; i < 5; ++i) inputs.push_back(counter.new_variable());
        counter.at_most_k(inputs, 2);
        if (counter.variables() >= 31)
            throw runtime_error("counter self-test unexpectedly large");
        array<uint8_t, 32> extendible{};
        const uint32_t assignments = 1u << counter.variables();
        for (uint32_t assignment = 0; assignment < assignments; ++assignment) {
            bool clause_ok = true, current_ok = false;
            for (int literal : counter.raw_data()) {
                if (!literal) {
                    clause_ok &= current_ok;
                    current_ok = false;
                } else {
                    const int variable = literal < 0 ? -literal : literal;
                    const bool value = assignment & (1u << (variable - 1));
                    current_ok |= literal > 0 ? value : !value;
                }
            }
            if (clause_ok) extendible[assignment & 31u] = 1;
        }
        for (int input_assignment = 0; input_assignment < 32; ++input_assignment)
            if (static_cast<bool>(extendible[input_assignment]) !=
                (popcount(static_cast<unsigned>(input_assignment)) <= 2))
                throw runtime_error("sequential counter self-test");
    }
    cout << "PASS factor_vars=5115 central=369x3+93x4"
            " short=1392-369=1023 caps=10,31,87,213,465 counter=PASS\n";
}

}  // namespace gf11

int main(int argc, char** argv) {
    using namespace gf11;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc == 2 && string(argv[1]) == "--self-test") {
            self_test();
            return 0;
        }
        if ((argc == 3 || argc == 4) && string(argv[1]) == "--count") {
            const bool universal = argc == 4 && string(argv[3]) == "--universal";
            if (argc == 4 && !universal) throw runtime_error("unknown count option");
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            Generator generator(std::move(row), false, universal);
            generator.generate();
            print_stats(generator);
            return generator.stats().central_empty_pins || generator.stats().empty_targets ? 1 : 0;
        }
        if ((argc == 4 || argc == 5) && string(argv[1]) == "--map") {
            const bool universal = argc == 5 && string(argv[4]) == "--universal";
            if (argc == 5 && !universal) throw runtime_error("unknown map option");
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            Generator generator(std::move(row), false, universal);
            generator.generate();
            write_selector_map(argv[3], generator);
            print_stats(generator);
            return generator.stats().central_empty_pins || generator.stats().empty_targets ? 1 : 0;
        }
        if (argc == 3 && string(argv[1]) == "--hall") {
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            Generator generator(std::move(row), false, false);
            generator.generate();
            print_stats(generator);
            print_hall(generator);
            return 0;
        }
        if ((argc == 4 || argc == 5) && string(argv[1]) == "--build") {
            const bool universal = argc == 5 && string(argv[4]) == "--universal";
            if (argc == 5 && !universal) throw runtime_error("unknown build option");
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            Generator generator(std::move(row), true, universal);
            generator.generate();
            generator.cnf().write(argv[3]);
            print_stats(generator);
            cerr << "DIMACS=" << argv[3] << '\n';
            return 0;
        }
        if (argc == 5 && string(argv[1]) == "--build-targets") {
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            vector<Mask> targets = read_target_list(argv[3]);
            Generator generator(std::move(row), true, false);
            generator.generate_only(targets);
            generator.cnf().write(argv[4]);
            print_stats(generator);
            cerr << "filtered_targets=" << targets.size() << " DIMACS=" << argv[4] << '\n';
            return 0;
        }
        if (argc == 6 && string(argv[1]) == "--build-drops") {
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            const int maximum = parse_drop_bound(argv[3]);
            Generator generator(std::move(row), true, false, maximum);
            generator.generate();
            generator.cnf().write(argv[4]);
            write_drop_map(argv[5], generator);
            print_stats(generator);
            cerr << "drop_bound=" << maximum << " DIMACS=" << argv[4]
                 << " drop_map=" << argv[5] << '\n';
            return generator.stats().central_empty_pins ? 1 : 0;
        }
        if (argc == 6 && string(argv[1]) == "--build-target-core") {
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            Generator generator(std::move(row), true, false, -1, true);
            generator.generate();
            generator.cnf().write(argv[3]);
            write_guard_files(argv[4], argv[5], generator);
            print_stats(generator);
            cerr << "target_guards=" << generator.guards().size()
                 << " DIMACS=" << argv[3] << " assumptions=" << argv[4]
                 << " guard_map=" << argv[5] << '\n';
            return generator.stats().central_empty_pins ? 1 : 0;
        }
        if ((argc == 5 || argc == 6) && string(argv[1]) == "--decode") {
            const bool universal = argc == 6 && string(argv[5]) == "--universal";
            if (argc == 6 && !universal) throw runtime_error("unknown decode option");
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            const auto assignment = read_model(argv[3], FACTOR_VARIABLES);
            vector<Mask> factor = decode_factor(assignment);
            if (!verify_factor(row, factor, universal, &reason))
                throw runtime_error("decoded model failed: " + reason);
            write_factor(argv[4], factor);
            cout << "PASS decoded " << (universal ? "universal" : "lower-complete")
                 << " factor length=465 output=" << argv[4] << '\n';
            return 0;
        }
        if (argc == 7 && string(argv[1]) == "--decode-drops") {
            vector<Mask> row = read_vector(argv[2], M);
            string reason;
            if (!rank6_permutation(row, &reason)) throw runtime_error(reason);
            const int maximum = parse_drop_bound(argv[3]);
            Generator generator(row, false, false, maximum);
            generator.generate();
            const auto assignment = read_model(argv[4], generator.cnf().variables());
            vector<Mask> factor = decode_factor(assignment);
            vector<Mask> relaxed;
            array<uint8_t, LIMIT> allowed{};
            for (const DropInfo& info : generator.drops()) {
                if (assignment[info.variable] < 0)
                    throw runtime_error("model omits drop variable " +
                                        to_string(info.variable));
                if (assignment[info.variable] > 0) {
                    relaxed.push_back(info.target);
                    allowed[info.target] = 1;
                }
            }
            if (static_cast<int>(relaxed.size()) > maximum)
                throw runtime_error("model exceeds requested drop bound");
            vector<Mask> actual_missing;
            if (!verify_factor(row, factor, false, &reason, &allowed, &actual_missing))
                throw runtime_error("decoded relaxed model failed: " + reason);
            write_factor(argv[5], factor);
            write_drop_report(argv[6], relaxed, actual_missing);
            cout << "PASS decoded relaxed factor length=465 bound=" << maximum
                 << " relaxed=" << relaxed.size()
                 << " actually_missing=" << actual_missing.size()
                 << " factor=" << argv[5] << " report=" << argv[6] << '\n';
            cout << "relaxed_masks";
            for (Mask mask : relaxed) cout << ' ' << static_cast<int>(mask);
            cout << "\nactual_missing_masks";
            for (Mask mask : actual_missing) cout << ' ' << static_cast<int>(mask);
            cout << '\n';
            return 0;
        }
        cerr << "usage:\n"
             << "  k11_q369_global_factor_cnf --self-test\n"
             << "  k11_q369_global_factor_cnf --count ROW [--universal]\n"
             << "  k11_q369_global_factor_cnf --map ROW OUTPUT.tsv [--universal]\n"
             << "  k11_q369_global_factor_cnf --hall ROW\n"
             << "  k11_q369_global_factor_cnf --build ROW OUTPUT.cnf [--universal]\n"
             << "  k11_q369_global_factor_cnf --build-targets ROW TARGETS OUTPUT.cnf\n"
             << "  k11_q369_global_factor_cnf --build-drops ROW Q OUTPUT.cnf OUTPUT.dropmap.tsv\n"
             << "  k11_q369_global_factor_cnf --build-target-core ROW OUTPUT.cnf"
                " OUTPUT.assumptions OUTPUT.guardmap.tsv\n"
             << "  k11_q369_global_factor_cnf --decode ROW MODEL OUTPUT.factor"
                " [--universal]\n"
             << "  k11_q369_global_factor_cnf --decode-drops ROW Q MODEL"
                " OUTPUT.factor OUTPUT.dropped.tsv\n";
        return 2;
    } catch (const exception& e) {
        cerr << "error: " << e.what() << '\n';
        return 2;
    }
}
