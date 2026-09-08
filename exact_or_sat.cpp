#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#elif defined(__clang__)
#pragma clang optimize on
#endif

#include <algorithm>
#include <bit>
#include <cstdlib>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

class Cnf {
    int variables_ = 0;

public:
    vector<vector<int>> clauses;

    int variable() { return ++variables_; }
    int variable_count() const { return variables_; }

    template<class... Ints>
    void add(Ints... literals) { clauses.push_back({static_cast<int>(literals)...}); }

    void add(vector<int> clause) { clauses.push_back(move(clause)); }

    // Sinz's sequential encoding.  This is linear rather than pairwise and is
    // important for the endpoint groups of the two central antichains.
    void at_most_one(const vector<int>& xs) {
        if (xs.size() <= 1) return;
        vector<int> prefix(xs.size() - 1);
        for (int& x : prefix) x = variable();
        add(-xs[0], prefix[0]);
        for (int i = 1; i + 1 < static_cast<int>(xs.size()); ++i) {
            add(-xs[i], prefix[i]);
            add(-prefix[i - 1], prefix[i]);
            add(-xs[i], -prefix[i - 1]);
        }
        add(-xs.back(), -prefix.back());
    }

    void exactly_one(const vector<int>& xs) {
        if (xs.empty()) throw runtime_error("empty exactly-one constraint");
        add(xs);
        at_most_one(xs);
    }

    void at_most_k(const vector<int>& xs, int k) {
        if (k < 0) throw invalid_argument("negative cardinality bound");
        if (k >= static_cast<int>(xs.size())) return;
        if (k == 0) {
            for (int x : xs) add(-x);
            return;
        }
        // A monotone unary counter. previous[j] being forced true means that
        // at least j+1 inputs in the processed prefix are true. One-way
        // implications suffice for an at-most constraint.
        vector<int> previous;
        for (int x : xs) {
            vector<int> current(k);
            for (int& variable : current) variable = this->variable();
            add(-x, current[0]);
            for (int j = 0; j < static_cast<int>(previous.size()); ++j)
                add(-previous[j], current[j]);
            for (int j = 0; j + 1 < static_cast<int>(previous.size()) && j + 1 < k; ++j)
                add(-x, -previous[j], current[j + 1]);
            if (static_cast<int>(previous.size()) == k)
                add(-x, -previous[k - 1]);
            previous.swap(current);
        }
    }

    // Return literals ge[q-1] which are true exactly when at least q of xs
    // are true.  Unlike the one-way counter used by at_most_k(), these
    // threshold literals are equivalences, so they may safely be used as
    // inputs to a second cardinality constraint.
    vector<int> exact_thresholds(const vector<int>& xs, int cap = -1) {
        if (xs.empty() || cap == 0) return {};
        if (cap < 0 || cap > static_cast<int>(xs.size())) cap = xs.size();
        vector<int> previous(1, variable());
        add(-previous[0], xs[0]);
        add(previous[0], -xs[0]);
        for (int i = 1; i < static_cast<int>(xs.size()); ++i) {
            vector<int> current(min(i + 1, cap));
            for (int& value : current) value = variable();
            for (int q = 1; q <= static_cast<int>(current.size()); ++q) {
                const int out = current[q - 1];
                const int same = q <= i ? previous[q - 1] : 0;
                const int lower = q == 1 ? 0 : previous[q - 2];

                // same -> out
                if (same) add(-same, out);
                // xs[i] & lower -> out; for q=1, lower is true.
                if (q == 1) add(-xs[i], out);
                else add(-xs[i], -lower, out);

                // out -> same OR (xs[i] AND lower).
                if (same) {
                    add(-out, same, xs[i]);
                    if (q > 1) add(-out, same, lower);
                } else {
                    add(-out, xs[i]);
                    add(-out, lower);
                }
            }
            previous.swap(current);
        }
        return previous;
    }

    void at_least_k(const vector<int>& xs, int k) {
        if (k <= 0) return;
        if (k > static_cast<int>(xs.size())) {
            add(vector<int>{});
            return;
        }
        const vector<int> thresholds = exact_thresholds(xs, k);
        add(thresholds[k - 1]);
    }

    void write(const string& path) const {
        ofstream out(path);
        if (!out) throw runtime_error("cannot open output CNF");
        out << "p cnf " << variables_ << ' ' << clauses.size() << '\n';
        for (const auto& clause : clauses) {
            for (int literal : clause) out << literal << ' ';
            out << "0\n";
        }
    }
};

struct Interval {
    int left;
    int right;
};

static int binomial(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    int64_t result = 1;
    for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
    return static_cast<int>(result);
}

// The rank-count lower bound needs only the targets of ranks at most r.
// Therefore, after deleting all entries of rank greater than r, the remaining
// word must still have at least C(k,r)+tau(k,r) positions, where tau is the
// least t satisfying
//
//   sum_{j<r} C(k,j) <= t C(k,r) + C(t+1,2).
//
// This is the entry-rank truncation bound used below.
static int rank_truncation_bound(int k, int r) {
    int64_t lower = 0;
    for (int j = 1; j < r; ++j) lower += binomial(k, j);
    const int64_t layer = binomial(k, r);
    int t = 0;
    while (lower > static_cast<int64_t>(t) * layer +
                       static_cast<int64_t>(t) * (t + 1) / 2)
        ++t;
    return static_cast<int>(layer) + t;
}

// If an array has length n=C(k,r)+d, order one selected witness for every
// r-set.  The i-th selected interval lies in [i,i+d].  Consequently an
// interval of OR-rank s and length ell contains at least ell-d distinct
// selected r-witnesses, all r-subsets of its OR.  Thus
//
//   ell <= d                       for r>s,
//   ell <= d+C(s,r)                for r<=s.
//
// Taking the minimum over all ranks gives the exact simultaneous
// containment-multiplicity cap used below.
static int maximum_witness_length(int k, int n, int target_rank) {
    int bound = n;
    for (int witness_rank = 1; witness_rank <= k; ++witness_rank) {
        const int family = binomial(k, witness_rank);
        if (family > n) continue;
        int candidate = n - family;
        if (witness_rank <= target_rank)
            candidate += binomial(target_rank, witness_rank);
        bound = min(bound, candidate);
    }
    return bound;
}

static bool overlap(Interval a, Interval b) {
    return max(a.left, b.left) <= min(a.right, b.right);
}

struct Encoding {
    int k;
    int n;
    int middle;
    int width;
    int slack;
    int exact_central_length;
    Cnf cnf;
    vector<vector<int>> entry;
    vector<Interval> intervals;
    vector<vector<int>> interval_or;
    vector<vector<int>> selectors;
    vector<vector<int>> selector_interval;

    static int theory_profile() {
        const char* value = getenv("OR_BENCH_PROFILE");
        if (!value || !*value) return 2;  // preserve the production default
        const int profile = stoi(value);
        if (profile < 0 || profile > 3)
            throw invalid_argument("OR_BENCH_PROFILE must be in 0..3");
        return profile;
    }

    Encoding(int bits, int length, int central_length = 0)
        : k(bits), n(length), middle(bits / 2),
          width(binomial(bits, bits / 2)),
          slack(length - width), exact_central_length(central_length),
          entry(length, vector<int>(bits)),
          selectors(1 << bits), selector_interval(1 << bits) {
        if (k <= 0 || k >= 20 || n <= 0)
            throw invalid_argument("require 1 <= k < 20 and n > 0");
        if (slack < 0)
            throw invalid_argument("length is below the Sperner bound");
    }

    void build() {
        const int profile = theory_profile();
        for (auto& row : entry)
            for (int& variable : row) variable = cnf.variable();

        // A shortest nonzero solution never needs a zero entry: deleting one
        // preserves all nonzero interval unions.
        for (int position = 0; position < n; ++position)
            cnf.add(entry[position]);

        // Entry-rank truncation cuts.  Let p_s be the number of entries of
        // rank at most s.  Deleting every higher-rank entry preserves every
        // witness for a target of rank at most s, so the rank-count theorem
        // gives p_s >= b_s(k).  The exact per-row threshold literals make the
        // resulting tail constraints explicit.  At k=11,n=465 this proves,
        // without an ansatz, that every entry has rank at most six and that at
        // most one entry has rank six.
        vector<vector<int>> rank_at_least;
        if (profile >= 1) {
            rank_at_least.resize(n);
            for (int position = 0; position < n; ++position)
                rank_at_least[position] = cnf.exact_thresholds(entry[position]);
            for (int s = 1; s <= k; ++s) {
                const int required_low = rank_truncation_bound(k, s);
                if (required_low > n) {
                    cnf.add(vector<int>{});
                    continue;
                }
                if (s == k) continue;
                vector<int> high;
                high.reserve(n);
                for (int position = 0; position < n; ++position)
                    high.push_back(rank_at_least[position][s]); // rank >= s+1
                const int high_limit = n - required_low;
                if (required_low <= high_limit) {
                    vector<int> low;
                    low.reserve(n);
                    for (int value : high) low.push_back(-value);
                    cnf.at_least_k(low, required_low);
                } else {
                    cnf.at_most_k(high, high_limit);
                }
            }

            // At the exact k=9 rank-count length, the zero-residual short
            // band and rank-filtration rigidity force every literal entry to
            // have rank at most three.  Profile 3 measures this additional
            // theorem without changing the default production formula.
            if (profile >= 3 && k == 9 && n == 128)
                for (int position = 0; position < n; ++position)
                    cnf.add(-rank_at_least[position][3]); // forbid rank >= 4

            if (profile >= 3 && k == 8 && n == 72) {
                // Exact rank-four filtration at beta_4(8)=72: rank-below-four
                // entries form one physical interval, while literal four-sets
                // are distinct boundary values.  The cumulative rank-three
                // cut already limits their total mass to 72-beta_3(8)=15.
                for (int position = 0; position < n; ++position)
                    cnf.add(-rank_at_least[position][4]); // forbid rank >= 5

                // If low positions i and l surround j, then j is also low.
                // Here rank_at_least[p][3] is exactly the rank-four flag after
                // the preceding cap.
                for (int i = 0; i < n; ++i)
                    for (int j = i + 1; j < n; ++j)
                        for (int l = j + 1; l < n; ++l)
                            cnf.add(rank_at_least[i][3],
                                    -rank_at_least[j][3],
                                    rank_at_least[l][3]);

                // No rank-four mask may occur literally twice.  A clause for
                // each mask and position pair is falsified exactly when both
                // entries equal that mask.
                for (int mask = 1; mask < (1 << k); ++mask) {
                    if (popcount(static_cast<unsigned>(mask)) != 4) continue;
                    for (int i = 0; i < n; ++i) {
                        for (int j = i + 1; j < n; ++j) {
                            vector<int> differs;
                            differs.reserve(2 * k);
                            for (int bit = 0; bit < k; ++bit) {
                                const bool present = mask & (1 << bit);
                                differs.push_back(present ? -entry[i][bit]
                                                          : entry[i][bit]);
                                differs.push_back(present ? -entry[j][bit]
                                                          : entry[j][bit]);
                            }
                            cnf.add(move(differs));
                        }
                    }
                }
            }
        }

        // Shared exact OR variables for every interval.  Recurrence along the
        // right endpoint uses three clauses per OR gate.
        for (int left = 0; left < n; ++left) {
            for (int right = left; right < n; ++right) {
                const int id = intervals.size();
                intervals.push_back({left, right});
                interval_or.emplace_back(k);
                for (int bit = 0; bit < k; ++bit) {
                    const int out = cnf.variable();
                    interval_or[id][bit] = out;
                    if (left == right) {
                        const int in = entry[right][bit];
                        cnf.add(-out, in);
                        cnf.add(out, -in);
                    } else {
                        const int previous_id = id - 1;
                        const int previous = interval_or[previous_id][bit];
                        const int current = entry[right][bit];
                        cnf.add(-previous, out);
                        cnf.add(-current, out);
                        cnf.add(-out, previous, current);
                    }
                }
            }
        }

        const bool odd = k & 1;
        for (int target = 1; target < (1 << k); ++target) {
            const int rank = popcount(static_cast<unsigned>(target));
            const bool central = rank == middle || (odd && rank == middle + 1);
            const int maximum_length = profile >= 1
                ? maximum_witness_length(k, n, rank) : n;
            if (maximum_length <= 0)
                throw runtime_error("length contradicts a rank lower bound");
            for (int id = 0; id < static_cast<int>(intervals.size()); ++id) {
                const Interval interval = intervals[id];
                if (interval.right - interval.left + 1 > maximum_length)
                    continue;
                if (central && exact_central_length > 0 &&
                    interval.right - interval.left + 1 != exact_central_length)
                    continue;
                if (exact_central_length == -1) {
                    const int length = interval.right - interval.left + 1;
                    if (rank <= 2 && length != 1) continue;
                    if (rank == middle && length != middle - 1) continue;
                    if (rank > middle && length > rank - 1) continue;
                }
                const int select = cnf.variable();
                selectors[target].push_back(select);
                selector_interval[target].push_back(id);
                for (int bit = 0; bit < k; ++bit) {
                    const int value = interval_or[id][bit];
                    cnf.add(-select, target & (1 << bit) ? value : -value);
                }
            }
            // Pick one canonical witness interval for each target.  Every actual
            // solution admits such a choice, so this loses no solutions.
            cnf.exactly_one(selectors[target]);
        }

        // In one antichain, two distinct chosen intervals cannot share a left
        // endpoint or a right endpoint.  State this explicitly for propagation.
        if (profile >= 2) {
            vector<int> central_ranks{middle};
            if (odd) central_ranks.push_back(middle + 1);
            for (int rank : central_ranks) {
                for (int endpoint = 0; endpoint < n; ++endpoint) {
                    vector<int> same_left, same_right;
                    for (int target = 1; target < (1 << k); ++target) {
                        if (popcount(static_cast<unsigned>(target)) != rank) continue;
                        for (int j = 0; j < static_cast<int>(selectors[target].size()); ++j) {
                            const Interval in = intervals[selector_interval[target][j]];
                            if (in.left == endpoint) same_left.push_back(selectors[target][j]);
                            if (in.right == endpoint) same_right.push_back(selectors[target][j]);
                        }
                    }
                    cnf.at_most_one(same_left);
                    cnf.at_most_one(same_right);
                }
            }

        // Aggregate witness choices by interval.  A physical interval has one
        // fixed OR, so it can witness at most one distinct target in each of
        // these groups.  Explicit usage variables expose the key containment
        // conflict between low-rank and central witnesses.
        auto interval_usage = [&] (auto accepts_rank) {
            vector<int> used(intervals.size());
            for (int id = 0; id < static_cast<int>(intervals.size()); ++id) {
                vector<int> group;
                for (int target = 1; target < (1 << k); ++target) {
                    const int rank = popcount(static_cast<unsigned>(target));
                    if (!accepts_rank(rank)) continue;
                    for (int j = 0; j < static_cast<int>(selectors[target].size()); ++j)
                        if (selector_interval[target][j] == id)
                            group.push_back(selectors[target][j]);
                }
                if (group.empty()) continue;
                cnf.at_most_one(group);
                used[id] = cnf.variable();
                for (int select : group) cnf.add(-select, used[id]);
                vector<int> reverse{-used[id]};
                reverse.insert(reverse.end(), group.begin(), group.end());
                cnf.add(move(reverse));
            }
            return used;
        };
            const vector<int> low_used = interval_usage(
                [&] (int rank) { return rank < middle; });
            const vector<int> central_used = interval_usage(
                [&] (int rank) { return rank == middle; });
            if (exact_central_length == -1) {
                int eligible = 0;
                for (int id = 0; id < static_cast<int>(intervals.size()); ++id)
                    if (central_used[id]) ++eligible;
                if (eligible == width)
                    for (int used : central_used) if (used) cnf.add(used);
            }
            for (int low = 0; low < static_cast<int>(intervals.size()); ++low) {
                if (!low_used[low]) continue;
                for (int central = 0; central < static_cast<int>(intervals.size()); ++central) {
                    if (!central_used[central]) continue;
                    if (intervals[low].left <= intervals[central].left &&
                        intervals[central].right <= intervals[low].right)
                        cnf.add(-low_used[low], -central_used[central]);
                }
            }

            // For odd k, an m-set and its complementary (m+1)-set are disjoint.
            // Their witness intervals cannot overlap because entries are nonempty.
            if (odd) {
                const int universe = (1 << k) - 1;
                for (int lower = 1; lower < (1 << k); ++lower) {
                    if (popcount(static_cast<unsigned>(lower)) != middle) continue;
                    const int upper = universe ^ lower;
                    for (int i = 0; i < static_cast<int>(selectors[lower].size()); ++i) {
                        const Interval a = intervals[selector_interval[lower][i]];
                        for (int j = 0; j < static_cast<int>(selectors[upper].size()); ++j) {
                            const Interval b = intervals[selector_interval[upper][j]];
                            if (overlap(a, b))
                                cnf.add(-selectors[lower][i], -selectors[upper][j]);
                        }
                    }
                }
            }
        }

        // Every singleton target requires a literal singleton entry.  Introduce
        // exact flags and order their first occurrences to break all k! bit-label
        // symmetries.
        vector<vector<int>> is_singleton(k, vector<int>(n));
        for (int bit = 0; bit < k; ++bit) {
            for (int position = 0; position < n; ++position) {
                const int flag = cnf.variable();
                is_singleton[bit][position] = flag;
                for (int other = 0; other < k; ++other)
                    cnf.add(-flag, other == bit ? entry[position][other]
                                                : -entry[position][other]);
                vector<int> reverse_clause{flag};
                for (int other = 0; other < k; ++other)
                    reverse_clause.push_back(other == bit ? -entry[position][other]
                                                           : entry[position][other]);
                cnf.add(move(reverse_clause));
            }
            cnf.add(is_singleton[bit]);
        }
        cerr << "theory_profile=" << profile << '\n';
        for (int bit = 1; bit < k; ++bit) {
            vector<int> earlier;
            for (int position = 0; position < n; ++position) {
                vector<int> clause{-is_singleton[bit][position]};
                clause.insert(clause.end(), earlier.begin(), earlier.end());
                cnf.add(move(clause));
                earlier.push_back(is_singleton[bit - 1][position]);
            }
        }
    }

    void constrain_seed(const vector<int>& seed, int max_changes) {
        if (static_cast<int>(seed.size()) != n || max_changes < 0)
            throw invalid_argument("bad seed or change radius");
        vector<int> changed(n);
        for (int position = 0; position < n; ++position) {
            changed[position] = cnf.variable();
            vector<int> some_difference{-changed[position]};
            for (int bit = 0; bit < k; ++bit) {
                const int difference = seed[position] & (1 << bit)
                    ? -entry[position][bit] : entry[position][bit];
                cnf.add(-difference, changed[position]);
                some_difference.push_back(difference);
            }
            cnf.add(move(some_difference));
        }
        cnf.at_most_k(changed, max_changes);
    }

    void constrain_windows(int length, const vector<int>& values) {
        if (length <= 0 || static_cast<int>(values.size()) != n - length + 1)
            throw invalid_argument("bad fixed-window data");
        for (int start = 0; start + length <= n; ++start) {
            int id = -1;
            for (int candidate = 0; candidate < static_cast<int>(intervals.size()); ++candidate)
                if (intervals[candidate].left == start &&
                    intervals[candidate].right == start + length - 1) {
                    id = candidate;
                    break;
                }
            if (id < 0) throw runtime_error("fixed interval not found");
            for (int bit = 0; bit < k; ++bit)
                cnf.add(values[start] & (1 << bit)
                    ? interval_or[id][bit] : -interval_or[id][bit]);
        }
    }
};

static vector<int> read_model(const string& path, int variables_needed) {
    ifstream in(path);
    if (!in) throw runtime_error("cannot open model");
    vector<char> value(variables_needed + 1, false);
    string line;
    bool sat = false;
    while (getline(in, line)) {
        if (line.rfind("s SATISFIABLE", 0) == 0) sat = true;
        if (line.empty() || line[0] != 'v') continue;
        istringstream stream(line.substr(1));
        int literal;
        while (stream >> literal) {
            if (literal > 0 && literal <= variables_needed) value[literal] = true;
        }
    }
    if (!sat) throw runtime_error("model is not SATISFIABLE");
    vector<int> result(value.begin(), value.end());
    return result;
}

static bool verify(int k, const vector<int>& a) {
    vector<char> seen(1 << k);
    vector<int> previous;
    for (int value : a) {
        vector<int> current{value};
        for (int old : previous) {
            const int next = old | value;
            if (next != current.back()) current.push_back(next);
        }
        for (int value_seen : current) seen[value_seen] = true;
        previous.swap(current);
    }
    for (int target = 1; target < (1 << k); ++target)
        if (!seen[target]) return false;
    return true;
}

int main(int argc, char** argv) {
    try {
        if (argc < 4) {
            cerr << "usage: exact_or_sat generate K N output.cnf\n"
                 << "   or: exact_or_sat decode K N solver.model\n";
            return 2;
        }
        const string mode = argv[1];
        const int k = stoi(argv[2]);
        const int n = stoi(argv[3]);
        const int central_length = argc > 5
            ? (string(argv[5]) == "graded" ? -1 : stoi(argv[5]))
            : 0;
        Encoding encoding(k, n, central_length);
        encoding.build();
        if (argc > 7) {
            ifstream data_stream(argv[6]);
            if (!data_stream) throw runtime_error("cannot open constraint data file");
            vector<int> data;
            int value;
            while (data_stream >> value) data.push_back(value);
            const string constraint = argv[7];
            if (constraint.rfind("windows", 0) == 0)
                encoding.constrain_windows(stoi(constraint.substr(7)), data);
            else
                encoding.constrain_seed(data, stoi(constraint));
        }
        if (mode == "generate") {
            if (argc != 5 && argc != 6 && argc != 8) return 2;
            encoding.cnf.write(argv[4]);
            cerr << "variables=" << encoding.cnf.variable_count()
                 << " clauses=" << encoding.cnf.clauses.size() << '\n';
            return 0;
        }
        if (mode == "decode") {
            if (argc != 5 && argc != 6 && argc != 8) return 2;
            const vector<int> model = read_model(argv[4], encoding.cnf.variable_count());
            vector<int> a(n);
            for (int position = 0; position < n; ++position)
                for (int bit = 0; bit < k; ++bit)
                    if (model[encoding.entry[position][bit]]) a[position] |= 1 << bit;
            if (!verify(k, a)) throw runtime_error("decoded array fails independent verifier");
            cout << n << '\n';
            for (int value : a) cout << value << ' ';
            cout << '\n';
            return 0;
        }
        return 2;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
