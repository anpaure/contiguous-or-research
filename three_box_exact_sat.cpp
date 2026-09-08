#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <vector>

using namespace std;

struct CNF {
    int vars = 0;
    vector<vector<int>> clauses;

    int new_var() { return ++vars; }
    void add(vector<int> c) { clauses.push_back(std::move(c)); }

    void write(const string& path) const {
        ofstream out(path);
        if (!out) throw runtime_error("cannot open CNF output: " + path);
        out << "p cnf " << vars << ' ' << clauses.size() << '\n';
        for (const auto& c : clauses) {
            for (int lit : c) out << lit << ' ';
            out << "0\n";
        }
    }
};

static int total_bits(int p, int q, int r) { return p + q + r; }

static uint64_t prefix_mask(int offset, int length, int used) {
    uint64_t answer = 0;
    for (int i = 0; i < used; ++i) answer |= uint64_t(1) << (offset + i);
    return answer;
}

static vector<uint64_t> box_targets(int p, int q, int r, bool include_zero = false) {
    vector<uint64_t> targets;
    for (int x = 0; x <= p; ++x) {
        for (int y = 0; y <= q; ++y) {
            for (int z = 0; z <= r; ++z) {
                uint64_t mask = prefix_mask(0, p, x)
                              | prefix_mask(p, q, y)
                              | prefix_mask(p + q, r, z);
                if (mask || include_zero) targets.push_back(mask);
            }
        }
    }
    sort(targets.begin(), targets.end());
    targets.erase(unique(targets.begin(), targets.end()), targets.end());
    return targets;
}

static long long box_width(int p, int q, int r) {
    vector<long long> coeff(1, 1);
    for (int length : {p, q, r}) {
        vector<long long> next(coeff.size() + length, 0);
        for (int i = 0; i < (int)coeff.size(); ++i)
            for (int j = 0; j <= length; ++j)
                next[i + j] += coeff[i];
        coeff.swap(next);
    }
    return *max_element(coeff.begin(), coeff.end());
}

static vector<long long> rank_counts(int p, int q, int r) {
    vector<long long> coeff(1, 1);
    for (int length : {p, q, r}) {
        vector<long long> next(coeff.size() + length, 0);
        for (int i = 0; i < (int)coeff.size(); ++i)
            for (int j = 0; j <= length; ++j)
                next[i + j] += coeff[i];
        coeff.swap(next);
    }
    return coeff;
}

static int rank_slack_bound(int p, int q, int r) {
    vector<long long> count = rank_counts(p, q, r);
    int answer = 1;
    long long lower = 0;
    for (int rank = 1; rank < (int)count.size(); ++rank) {
        long long middle = count[rank];
        int delay = 0;
        while (lower > 1LL * delay * middle + 1LL * delay * (delay + 1) / 2)
            ++delay;
        answer = max<long long>(answer, middle + delay);
        lower += count[rank];
    }
    return answer;
}

static bool verify_word(int p, int q, int r, const vector<uint64_t>& a,
                        vector<uint64_t>* missing_out = nullptr) {
    const int bits = total_bits(p, q, r);
    if (bits >= 63) throw runtime_error("this checker supports at most 62 increments");
    const uint64_t limit = uint64_t(1) << bits;
    for (uint64_t x : a) if (x >= limit) return false;

    vector<uint64_t> got;
    got.reserve(a.size() * (a.size() + 1) / 2);
    for (int left = 0; left < (int)a.size(); ++left) {
        uint64_t value = 0;
        for (int right = left; right < (int)a.size(); ++right) {
            value |= a[right];
            got.push_back(value);
        }
    }
    sort(got.begin(), got.end());
    got.erase(unique(got.begin(), got.end()), got.end());

    vector<uint64_t> missing;
    for (uint64_t target : box_targets(p, q, r)) {
        if (!binary_search(got.begin(), got.end(), target)) missing.push_back(target);
    }
    if (missing_out) *missing_out = missing;
    return missing.empty();
}

struct WitnessVar {
    int left;
    int right;
    int var;
};

static vector<uint64_t> inward_hex_spiral(int side) {
    if (side < 0 || side % 2) throw runtime_error("hex spiral requires an even side");
    int a = side / 2;
    vector<uint64_t> result;
    const int direction[6][3] = {
        {0, -1, 1}, {1, -1, 0}, {1, 0, -1},
        {0, 1, -1}, {-1, 1, 0}, {-1, 0, 1}
    };
    for (int radius = a; radius >= 1; --radius) {
        int u = -radius, v = radius, w = 0;
        for (const auto& d : direction) {
            for (int step = 0; step < radius; ++step) {
                int x = a + u, y = a + v, z = a + w;
                result.push_back(prefix_mask(0, side, x)
                               | prefix_mask(side, side, y)
                               | prefix_mask(2 * side, side, z));
                u += d[0]; v += d[1]; w += d[2];
            }
        }
    }
    result.push_back(prefix_mask(0, side, a)
                   | prefix_mask(side, side, a)
                   | prefix_mask(2 * side, side, a));
    return result;
}

struct BandOccurrence {
    uint64_t target;
    int radius;
};

struct CornerOccurrence {
    uint64_t target;
    int alpha;
    int beta;
};

static vector<uint64_t> hex_ring(int side, int radius) {
    int a = side / 2;
    vector<uint64_t> ring;
    const int direction[6][3] = {
        {0, 1, -1}, {-1, 1, 0}, {-1, 0, 1},
        {0, -1, 1}, {1, -1, 0}, {1, 0, -1}
    };
    int u = radius, v = -radius, w = 0;
    for (int side_index = 0; side_index < 6; ++side_index) {
        for (int step = 0; step < radius; ++step) {
            ring.push_back(prefix_mask(0, side, a + u)
                         | prefix_mask(side, side, a + v)
                         | prefix_mask(2 * side, side, a + w));
            u += direction[side_index][0];
            v += direction[side_index][1];
            w += direction[side_index][2];
        }
    }
    return ring;
}

static vector<CornerOccurrence> corner_band_row(int side, int phase,
                                                 bool reverse_rings,
                                                 int omitted_boundary_state) {
    int a = side / 2;
    vector<CornerOccurrence> result;
    uint64_t center = prefix_mask(0, side, a)
                    | prefix_mask(side, side, a)
                    | prefix_mask(2 * side, side, a);
    result.push_back({center, 0, 0});
    for (int radius = 1; radius <= a; ++radius) {
        vector<uint64_t> ring = hex_ring(side, radius);
        if (reverse_rings) reverse(ring.begin(), ring.end());
        int shift = ((phase % (int)ring.size()) + ring.size()) % ring.size();
        rotate(ring.begin(), ring.begin() + shift, ring.end());
        int base = 3 * (radius - 1);
        const int state_alpha[7] = {0, 0, 1, 1, 2, 2, 3};
        const int state_beta [7] = {0, 1, 1, 2, 2, 3, 3};
        int chosen_state[6], cursor = 0;
        for (int state = 0; state < 7; ++state)
            if (state != omitted_boundary_state) chosen_state[cursor++] = state;
        for (int index = 0; index < (int)ring.size(); ++index) {
            int side_index = index / radius;
            int state = chosen_state[side_index];
            result.push_back({ring[index], base + state_alpha[state],
                              base + state_beta[state]});
        }
    }
    return result;
}

static vector<BandOccurrence> outward_radial_shadow(int side, bool closed_rings) {
    if (side < 0 || side % 2) throw runtime_error("radial shadow requires an even side");
    int a = side / 2;
    vector<BandOccurrence> result;
    result.push_back({prefix_mask(0, side, a)
                    | prefix_mask(side, side, a)
                    | prefix_mask(2 * side, side, a), 0});
    const int direction[6][3] = {
        {0, 1, -1}, {-1, 1, 0}, {-1, 0, 1},
        {0, -1, 1}, {1, -1, 0}, {1, 0, -1}
    };
    for (int radius = 1; radius <= a; ++radius) {
        int u = radius, v = -radius, w = 0;
        result.push_back({prefix_mask(0, side, a + u)
                        | prefix_mask(side, side, a + v)
                        | prefix_mask(2 * side, side, a + w), radius});
        for (int direction_index = 0; direction_index < 6; ++direction_index) {
            const auto& d = direction[direction_index];
            for (int step = 0; step < radius; ++step) {
                u += d[0]; v += d[1]; w += d[2];
                bool final_return = direction_index == 5 && step + 1 == radius;
                if (!final_return || closed_rings)
                    result.push_back({prefix_mask(0, side, a + u)
                                    | prefix_mask(side, side, a + v)
                                    | prefix_mask(2 * side, side, a + w), radius});
            }
        }
    }
    return result;
}

static void generate(int p, int q, int r, int n, const string& cnf_path,
                     bool force_inward_spiral = false,
                     bool coordinate_faces_only = false,
                     uint64_t excluded_target = UINT64_MAX,
                     const string& target_list_path = "",
                     int radial_band_kind = 0,
                     int radial_band_shift = 0,
                     int corner_phase = 0,
                     bool corner_reverse = false,
                     int corner_omit = 6) {
    const int bits = total_bits(p, q, r);
    if (bits <= 0 || bits >= 31) throw runtime_error("generator requires 1..30 increments");
    if (n <= 0) throw runtime_error("length must be positive");

    CNF cnf;
    vector<vector<int>> x(n, vector<int>(bits));
    for (int i = 0; i < n; ++i)
        for (int b = 0; b < bits; ++b)
            x[i][b] = cnf.new_var();

    // WLOG every emitted entry is itself a nonzero box point.  For an
    // arbitrary entry X, replace X in each coordinate chain by the shortest
    // prefix containing X.  Whenever an interval formerly ORed to a box
    // target T, every X in it was contained in T, hence its prefix closure is
    // still contained in T; the interval OR remains exactly T.  Zero entries
    // can be deleted in a shortest nonzero word.
    for (int pos = 0; pos < n; ++pos) {
        cnf.add(x[pos]);
        int offset = 0;
        for (int length : {p, q, r}) {
            for (int level = 1; level < length; ++level)
                cnf.add({-x[pos][offset + level], x[pos][offset + level - 1]});
            offset += length;
        }
    }

    vector<uint64_t> targets = box_targets(p, q, r);
    if (!target_list_path.empty()) {
        targets.clear();
        ifstream target_in(target_list_path);
        if (!target_in) throw runtime_error("cannot open target list: " + target_list_path);
        uint64_t target;
        while (target_in >> target) targets.push_back(target);
        sort(targets.begin(), targets.end());
        targets.erase(unique(targets.begin(), targets.end()), targets.end());
    }
    if (excluded_target != UINT64_MAX)
        targets.erase(remove(targets.begin(), targets.end(), excluded_target), targets.end());
    if (coordinate_faces_only) {
        const uint64_t mx = (uint64_t(1) << p) - 1;
        const uint64_t my = ((uint64_t(1) << q) - 1) << p;
        const uint64_t mz = ((uint64_t(1) << r) - 1) << (p + q);
        targets.erase(remove_if(targets.begin(), targets.end(), [&](uint64_t x) {
            return (x & mx) && (x & my) && (x & mz);
        }), targets.end());
    }
    vector<long long> layer;
    if (coordinate_faces_only || excluded_target != UINT64_MAX || !target_list_path.empty()) {
        layer.assign(bits + 1, 0);
        layer[0] = 1;
        for (uint64_t target : targets) ++layer[__builtin_popcountll(target)];
    } else {
        layer = rank_counts(p, q, r);
    }
    unordered_map<uint64_t, vector<WitnessVar>> witness_vars;

    for (uint64_t target : targets) {
        const int target_rank = __builtin_popcountll(target);
        int max_length = n;
        if (!radial_band_kind) {
            for (int higher = target_rank + 1; higher < (int)layer.size(); ++higher) {
                if (layer[higher] > n) {
                    max_length = 0;
                    break;
                }
                max_length = min<long long>(max_length, n - layer[higher]);
            }
        }
        vector<int> witnesses;
        vector<int> singleton_witnesses;
        witnesses.reserve(n * min(n, max_length));
        for (int left = 0; left < n; ++left) {
            for (int right = left; right < n && right - left + 1 <= max_length; ++right) {
                int y = cnf.new_var();
                witnesses.push_back(y);
                if (left == right) singleton_witnesses.push_back(y);
                if (force_inward_spiral && target_rank == bits / 2)
                    witness_vars[target].push_back({left, right, y});

                for (int b = 0; b < bits; ++b) {
                    if ((target >> b) & 1U) {
                        vector<int> clause;
                        clause.reserve(right - left + 2);
                        clause.push_back(-y);
                        for (int pos = left; pos <= right; ++pos)
                            clause.push_back(x[pos][b]);
                        cnf.add(std::move(clause));
                    } else {
                        for (int pos = left; pos <= right; ++pos)
                            cnf.add({-y, -x[pos][b]});
                    }
                }
            }
        }
        cnf.add(std::move(witnesses));

        // Every nonzero point on a pure coordinate axis is join-irreducible
        // relative to its highest increment: some entry in any witness must
        // equal that point.  Exposing the logically implied singleton witness
        // is a strong but sound propagation clause.
        int nonzero_blocks = 0;
        int offset = 0;
        for (int length : {p, q, r}) {
            uint64_t block = ((uint64_t(1) << length) - 1) << offset;
            nonzero_blocks += (target & block) != 0;
            offset += length;
        }
        if (nonzero_blocks == 1) cnf.add(std::move(singleton_witnesses));
    }

    if (force_inward_spiral) {
        if (!(p == q && q == r && p % 2 == 0))
            throw runtime_error("spiral constraint requires p=q=r even");
        vector<uint64_t> spiral = inward_hex_spiral(p);
        if ((long long)spiral.size() != layer[bits / 2])
            throw runtime_error("internal spiral cardinality error");
        for (int i = 0; i + 1 < (int)spiral.size(); ++i) {
            const auto& first = witness_vars.at(spiral[i]);
            const auto& second = witness_vars.at(spiral[i + 1]);
            for (const WitnessVar& a : first) {
                for (const WitnessVar& b : second) {
                    if (a.left >= b.left || a.right >= b.right)
                        cnf.add({-a.var, -b.var});
                }
            }
        }
    }

    if (radial_band_kind) {
        if (!(p == q && q == r && p % 2 == 0))
            throw runtime_error("radial band requires p=q=r even");
        bool closed = radial_band_kind == 2;
        if (radial_band_kind == 3) {
            vector<CornerOccurrence> row = corner_band_row(p, corner_phase,
                                                            corner_reverse,
                                                            corner_omit);
            int a = p / 2;
            int expected = 3 * a * a + 3 * a + 1;
            if ((int)row.size() != expected)
                throw runtime_error("internal corner row cardinality error");
            for (int index = 0; index < (int)row.size(); ++index) {
                int left = radial_band_shift + index + row[index].alpha;
                int right = radial_band_shift + index + row[index].beta;
                if (left < 0 || right >= n)
                    throw runtime_error("corner band does not fit physical word");
                for (int bit = 0; bit < bits; ++bit) {
                    if ((row[index].target >> bit) & 1U) {
                        vector<int> clause;
                        for (int pos = left; pos <= right; ++pos)
                            clause.push_back(x[pos][bit]);
                        cnf.add(std::move(clause));
                    } else {
                        for (int pos = left; pos <= right; ++pos)
                            cnf.add({-x[pos][bit]});
                    }
                }
            }
        } else {
        vector<BandOccurrence> row = outward_radial_shadow(p, closed);
        int a = p / 2;
        int expected = 3 * a * a + 3 * a + 1 + (closed ? a : 0);
        if ((int)row.size() != expected)
            throw runtime_error("internal radial row cardinality error");
        for (int index = 0; index < (int)row.size(); ++index) {
            int left = radial_band_shift + index;
            int right = left + row[index].radius;
            if (left < 0 || right >= n)
                throw runtime_error("radial band does not fit physical word");
            for (int bit = 0; bit < bits; ++bit) {
                if ((row[index].target >> bit) & 1U) {
                    vector<int> clause;
                    for (int pos = left; pos <= right; ++pos)
                        clause.push_back(x[pos][bit]);
                    cnf.add(std::move(clause));
                } else {
                    for (int pos = left; pos <= right; ++pos)
                        cnf.add({-x[pos][bit]});
                }
            }
        }
        }
    }

    cnf.write(cnf_path);
    cerr << "p=" << p << " q=" << q << " r=" << r
         << " bits=" << bits << " targets=" << targets.size()
         << " width=" << box_width(p, q, r)
         << " B=" << rank_slack_bound(p, q, r) << " n=" << n
         << " spiral=" << (force_inward_spiral ? 1 : 0)
         << " faces=" << (coordinate_faces_only ? 1 : 0)
         << " excluded=" << (excluded_target == UINT64_MAX ? -1LL
                                                               : (long long)excluded_target)
         << " target_list=" << (!target_list_path.empty() ? 1 : 0)
         << " radial=" << radial_band_kind << " shift=" << radial_band_shift
         << " corner_phase=" << corner_phase
         << " corner_reverse=" << corner_reverse
         << " corner_omit=" << corner_omit
         << " vars=" << cnf.vars << " clauses=" << cnf.clauses.size() << '\n';
}

static vector<uint64_t> decode_model(int p, int q, int r, int n,
                                     const string& model_path) {
    const int bits = total_bits(p, q, r);
    vector<char> truth(n * bits + 1, 0);
    ifstream in(model_path);
    if (!in) throw runtime_error("cannot open model: " + model_path);
    string line;
    bool sat = false;
    while (getline(in, line)) {
        if (line == "s SATISFIABLE" || line == "SAT" || line == "SATISFIABLE") sat = true;
        if (line == "s UNSATISFIABLE" || line == "UNSAT" || line == "UNSATISFIABLE")
            throw runtime_error("model file says UNSAT");
        if (line.size() < 2 || line[0] != 'v' || line[1] != ' ') continue;
        istringstream row(line.substr(2));
        int lit;
        while (row >> lit) {
            if (lit > 0 && lit <= n * bits) truth[lit] = 1;
        }
    }
    if (!sat) throw runtime_error("no SAT status found in model");

    vector<uint64_t> a(n, 0);
    for (int i = 0; i < n; ++i)
        for (int b = 0; b < bits; ++b)
            if (truth[i * bits + b + 1]) a[i] |= uint64_t(1) << b;
    return a;
}

static vector<uint64_t> read_word(const string& path) {
    ifstream in(path);
    if (!in) throw runtime_error("cannot open word: " + path);
    vector<uint64_t> a;
    uint64_t x;
    while (in >> x) a.push_back(x);
    return a;
}

static void write_word(const string& path, const vector<uint64_t>& a) {
    ofstream out(path);
    if (!out) throw runtime_error("cannot write word: " + path);
    for (int i = 0; i < (int)a.size(); ++i)
        out << a[i] << (i + 1 == (int)a.size() ? '\n' : ' ');
}

static vector<int> mask_coordinates(uint64_t mask, int p, int q, int r) {
    vector<int> result;
    int offset = 0;
    for (int length : {p, q, r}) {
        int used = 0;
        while (used < length && ((mask >> (offset + used)) & 1U)) ++used;
        result.push_back(used);
        offset += length;
    }
    return result;
}

static void print_witnesses(int p, int q, int r, const vector<uint64_t>& a) {
    for (uint64_t target : box_targets(p, q, r)) {
        int best_left = -1, best_right = -1;
        for (int left = 0; left < (int)a.size(); ++left) {
            uint64_t value = 0;
            for (int right = left; right < (int)a.size(); ++right) {
                value |= a[right];
                if (value == target &&
                    (best_left < 0 || right - left < best_right - best_left)) {
                    best_left = left;
                    best_right = right;
                }
            }
        }
        vector<int> c = mask_coordinates(target, p, q, r);
        cout << '(' << c[0] << ',' << c[1] << ',' << c[2] << ')'
             << " mask=" << target << " interval=[" << best_left + 1 << ','
             << best_right + 1 << "] length=" << best_right - best_left + 1 << '\n';
    }
}

static vector<uint64_t> missing_targets(int p, int q, int r,
                                        const vector<uint64_t>& a) {
    vector<uint64_t> missing;
    verify_word(p, q, r, a, &missing);
    return missing;
}

static string coordinate_string(uint64_t mask, int p, int q, int r) {
    vector<int> c = mask_coordinates(mask, p, q, r);
    return "(" + to_string(c[0]) + "," + to_string(c[1]) + ","
         + to_string(c[2]) + ")";
}

static void analyze_word(int p, int q, int r, const vector<uint64_t>& a) {
    const int middle_rank = (p + q + r) / 2;
    struct Record { int left, right; uint64_t target; };
    vector<Record> central;
    for (uint64_t target : box_targets(p, q, r)) {
        if (__builtin_popcountll(target) != middle_rank) continue;
        int best_left = -1, best_right = -1;
        for (int left = 0; left < (int)a.size(); ++left) {
            uint64_t value = 0;
            for (int right = left; right < (int)a.size(); ++right) {
                value |= a[right];
                if (value == target &&
                    (best_left < 0 || right - left < best_right - best_left)) {
                    best_left = left; best_right = right;
                }
            }
        }
        central.push_back({best_left, best_right, target});
    }
    sort(central.begin(), central.end(), [](const Record& x, const Record& y) {
        return tie(x.left, x.right) < tie(y.left, y.right);
    });
    cout << "central shortest witnesses ordered by left endpoint:\n";
    for (const Record& x : central)
        cout << coordinate_string(x.target, p, q, r) << " [" << x.left + 1
             << ',' << x.right + 1 << "] len=" << x.right - x.left + 1 << '\n';

    cout << "deletion deficits:\n";
    for (int pos = 0; pos < (int)a.size(); ++pos) {
        vector<uint64_t> b = a;
        b.erase(b.begin() + pos);
        vector<uint64_t> missing = missing_targets(p, q, r, b);
        cout << "delete " << pos + 1 << ' ' << coordinate_string(a[pos], p, q, r)
             << " missing=" << missing.size();
        if (missing.size() <= 8)
            for (uint64_t x : missing) cout << ' ' << coordinate_string(x, p, q, r);
        cout << '\n';
    }

    cout << "adjacent-contraction deficits:\n";
    for (int pos = 0; pos + 1 < (int)a.size(); ++pos) {
        vector<uint64_t> b = a;
        b[pos] |= b[pos + 1];
        b.erase(b.begin() + pos + 1);
        vector<uint64_t> missing = missing_targets(p, q, r, b);
        cout << "contract " << pos + 1 << '-' << pos + 2
             << " missing=" << missing.size();
        if (missing.size() <= 8)
            for (uint64_t x : missing) cout << ' ' << coordinate_string(x, p, q, r);
        cout << '\n';
    }
}

static void analyze_spiral(int side) {
    vector<uint64_t> t = inward_hex_spiral(side);
    int bits = 3 * side;
    vector<vector<char>> union_seen(bits + 1), intersection_seen(bits + 1);
    const uint64_t full = (uint64_t(1) << bits) - 1;
    const uint64_t universe = uint64_t(1) << bits;
    for (auto* table : {&union_seen, &intersection_seen})
        for (auto& row : *table) row.assign(universe, 0);
    for (int left = 0; left < (int)t.size(); ++left) {
        uint64_t u = 0, meet = full;
        for (int right = left; right < (int)t.size(); ++right) {
            u |= t[right];
            meet &= t[right];
            union_seen[__builtin_popcountll(u)][u] = 1;
            intersection_seen[__builtin_popcountll(meet)][meet] = 1;
        }
    }
    vector<long long> layers = rank_counts(side, side, side);
    cout << "side=" << side << " spiral_vertices=" << t.size() << '\n';
    cout << "rank total union intersection\n";
    for (int rank = 0; rank <= bits; ++rank) {
        long long unions = accumulate(union_seen[rank].begin(), union_seen[rank].end(), 0LL);
        long long intersections = accumulate(intersection_seen[rank].begin(),
                                             intersection_seen[rank].end(), 0LL);
        cout << rank << ' ' << layers[rank] << ' ' << unions << ' ' << intersections << '\n';
    }
    cout << "missing lower intersection targets:\n";
    for (uint64_t target : box_targets(side, side, side)) {
        int rank = __builtin_popcountll(target);
        if (rank < bits / 2 && !intersection_seen[rank][target])
            cout << coordinate_string(target, side, side, side) << ' ';
    }
    cout << '\n';

    cout << "coordinate runs (bit: lengths; boundary runs marked L/R):\n";
    for (int bit = 0; bit < bits; ++bit) {
        vector<pair<int,int>> runs;
        for (int i = 0; i < (int)t.size();) {
            if (!((t[i] >> bit) & 1U)) { ++i; continue; }
            int j = i;
            while (j + 1 < (int)t.size() && ((t[j + 1] >> bit) & 1U)) ++j;
            runs.push_back({i, j});
            i = j + 1;
        }
        cout << bit << ':';
        for (auto [l, r] : runs)
            cout << ' ' << r - l + 1 << (l == 0 ? "L" : "")
                 << (r + 1 == (int)t.size() ? "R" : "");
        cout << '\n';
    }
}

static void analyze_radial_band(int side, bool closed, int pre = 0, int post = 0) {
    vector<BandOccurrence> row = outward_radial_shadow(side, closed);
    int a = side / 2;
    int n = pre + (int)row.size() + a + post;
    int bits = 3 * side;
    uint64_t full = (uint64_t(1) << bits) - 1;
    vector<uint64_t> envelope(n, full);
    vector<char> touched(n, 0);
    for (int i = 0; i < (int)row.size(); ++i) {
        for (int pos = pre + i; pos <= pre + i + row[i].radius; ++pos) {
            envelope[pos] &= row[i].target;
            touched[pos] = 1;
        }
    }
    vector<uint64_t> axes;
    for (int block = 0; block < 3; ++block)
        for (int h = 1; h <= side; ++h)
            axes.push_back(prefix_mask(block * side, side, h));
    vector<vector<int>> edge(axes.size());
    int central_pin_failures = 0;
    for (int i = 0; i < (int)row.size(); ++i) {
        for (int bit = 0; bit < bits; ++bit) if ((row[i].target >> bit) & 1U) {
            bool found = false;
            for (int pos = pre + i; pos <= pre + i + row[i].radius; ++pos)
                found |= (envelope[pos] >> bit) & 1U;
            central_pin_failures += !found;
        }
    }
    cout << "position envelope\n";
    for (int pos = 0; pos < n; ++pos) {
        if (!touched[pos]) envelope[pos] = full;
        cout << pos << ' ' << coordinate_string(envelope[pos], side, side, side) << '\n';
        for (int target = 0; target < (int)axes.size(); ++target)
            if ((axes[target] & ~envelope[pos]) == 0) edge[target].push_back(pos);
    }
    vector<int> owner(n, -1);
    auto augment = [&](auto&& self, int target, vector<char>& seen) -> bool {
        for (int pos : edge[target]) if (!seen[pos]) {
            seen[pos] = 1;
            if (owner[pos] < 0 || self(self, owner[pos], seen)) {
                owner[pos] = target;
                return true;
            }
        }
        return false;
    };
    int matching = 0;
    for (int target = 0; target < (int)axes.size(); ++target) {
        vector<char> seen(n, 0);
        matching += augment(augment, target, seen);
    }
    cout << "axis_matching=" << matching << '/' << axes.size()
         << " boundary_slots_needed_at_least=" << axes.size() - matching
         << " central_pin_failures=" << central_pin_failures << '\n';
    vector<uint64_t> missing = missing_targets(side, side, side, envelope);
    cout << "maximal_factor_missing=" << missing.size();
    if (missing.size() <= 40)
        for (uint64_t target : missing)
            cout << ' ' << coordinate_string(target, side, side, side);
    cout << '\n';

    struct Slot { int left, right; uint64_t envelope; };
    vector<Slot> slots;
    for (int left = 0; left < n; ++left) {
        uint64_t value = 0;
        for (int right = left; right < n; ++right) {
            value |= envelope[right];
            slots.push_back({left, right, value});
        }
    }
    vector<uint64_t> lower;
    for (uint64_t target : box_targets(side, side, side))
        if (__builtin_popcountll(target) < bits / 2) lower.push_back(target);
    vector<long long> layer = rank_counts(side, side, side);
    auto matching_size = [&](bool safe_deadlines) {
        vector<vector<int>> candidate(lower.size());
        for (int target_index = 0; target_index < (int)lower.size(); ++target_index) {
            uint64_t target = lower[target_index];
            int max_length = n;
            if (safe_deadlines) {
                int rank = __builtin_popcountll(target);
                for (int higher = rank + 1; higher < (int)layer.size(); ++higher)
                    max_length = min<long long>(max_length, n - layer[higher]);
            }
            for (int slot = 0; slot < (int)slots.size(); ++slot) {
                int length = slots[slot].right - slots[slot].left + 1;
                if (length <= max_length && (target & ~slots[slot].envelope) == 0)
                    candidate[target_index].push_back(slot);
            }
        }
        vector<int> slot_owner(slots.size(), -1);
        auto dfs = [&](auto&& self, int target, vector<char>& seen) -> bool {
            for (int slot : candidate[target]) if (!seen[slot]) {
                seen[slot] = 1;
                if (slot_owner[slot] < 0 || self(self, slot_owner[slot], seen)) {
                    slot_owner[slot] = target;
                    return true;
                }
            }
            return false;
        };
        int result = 0;
        for (int target = 0; target < (int)lower.size(); ++target) {
            vector<char> seen(slots.size(), 0);
            result += dfs(dfs, target, seen);
        }
        return result;
    };
    cout << "lower_containment_matching_all=" << matching_size(false) << '/'
         << lower.size() << " safe_deadline=" << matching_size(true) << '/'
         << lower.size() << '\n';
}

int main(int argc, char** argv) try {
    if (argc < 2) throw runtime_error("missing mode: gen/decode/verify/witness/info");
    string mode = argv[1];
    if (mode == "gen") {
        if (argc != 7) throw runtime_error("usage: gen p q r n output.cnf");
        generate(stoi(argv[2]), stoi(argv[3]), stoi(argv[4]), stoi(argv[5]), argv[6]);
    } else if (mode == "gen-spiral") {
        if (argc != 5) throw runtime_error("usage: gen-spiral even_side n output.cnf");
        int side = stoi(argv[2]), n = stoi(argv[3]);
        generate(side, side, side, n, argv[4], true);
    } else if (mode == "gen-faces") {
        if (argc != 5) throw runtime_error("usage: gen-faces side n output.cnf");
        int side = stoi(argv[2]), n = stoi(argv[3]);
        generate(side, side, side, n, argv[4], false, true);
    } else if (mode == "gen-drop") {
        if (argc != 8) throw runtime_error("usage: gen-drop p q r n excluded_mask output.cnf");
        generate(stoi(argv[2]), stoi(argv[3]), stoi(argv[4]), stoi(argv[5]),
                 argv[7], false, false, stoull(argv[6]));
    } else if (mode == "gen-keep") {
        if (argc != 8) throw runtime_error("usage: gen-keep p q r n targets.txt output.cnf");
        generate(stoi(argv[2]), stoi(argv[3]), stoi(argv[4]), stoi(argv[5]),
                 argv[7], false, false, UINT64_MAX, argv[6]);
    } else if (mode == "gen-band") {
        if (argc != 7)
            throw runtime_error("usage: gen-band even_side distinct|closed pre_slots post_slots output.cnf");
        int side = stoi(argv[2]);
        string kind_name = argv[3];
        int kind = kind_name == "distinct" ? 1 : kind_name == "closed" ? 2 : 0;
        if (!kind) throw runtime_error("band kind must be distinct or closed");
        int pre = stoi(argv[4]), post = stoi(argv[5]);
        int a = side / 2;
        int middle = 3 * a * a + 3 * a + 1;
        int row_length = middle + (kind == 2 ? a : 0);
        int factor_length = row_length + a;
        generate(side, side, side, pre + factor_length + post, argv[6],
                 false, false, UINT64_MAX, "", kind, pre);
    } else if (mode == "gen-band-keep") {
        if (argc != 8)
            throw runtime_error("usage: gen-band-keep even_side distinct|closed pre post targets.txt output.cnf");
        int side = stoi(argv[2]);
        string kind_name = argv[3];
        int kind = kind_name == "distinct" ? 1 : kind_name == "closed" ? 2 : 0;
        if (!kind) throw runtime_error("band kind must be distinct or closed");
        int pre = stoi(argv[4]), post = stoi(argv[5]);
        int a = side / 2;
        int middle = 3 * a * a + 3 * a + 1;
        int row_length = middle + (kind == 2 ? a : 0);
        int factor_length = row_length + a;
        generate(side, side, side, pre + factor_length + post, argv[7],
                 false, false, UINT64_MAX, argv[6], kind, pre);
    } else if (mode == "gen-corner") {
        if (argc != 7)
            throw runtime_error("usage: gen-corner even_side phase reverse01 omitted_state_0to6 output.cnf");
        int side = stoi(argv[2]), phase = stoi(argv[3]);
        bool reverse_rings = stoi(argv[4]) != 0;
        int omitted = stoi(argv[5]);
        if (omitted < 0 || omitted > 6) throw runtime_error("omitted state must be 0..6");
        int a = side / 2;
        int middle = 3 * a * a + 3 * a + 1;
        generate(side, side, side, middle + 3 * a, argv[6],
                 false, false, UINT64_MAX, "", 3, 0, phase, reverse_rings,
                 omitted);
    } else if (mode == "decode") {
        if (argc != 8) throw runtime_error("usage: decode p q r n model.out word.txt");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]), n = stoi(argv[5]);
        vector<uint64_t> a = decode_model(p, q, r, n, argv[6]);
        vector<uint64_t> missing;
        if (!verify_word(p, q, r, a, &missing))
            throw runtime_error("decoded SAT model fails independent interval-OR verification");
        write_word(argv[7], a);
        cerr << "verified word of length " << a.size() << '\n';
    } else if (mode == "verify") {
        if (argc != 6) throw runtime_error("usage: verify p q r word.txt");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]);
        vector<uint64_t> a = read_word(argv[5]);
        vector<uint64_t> missing;
        bool ok = verify_word(p, q, r, a, &missing);
        cout << (ok ? "OK" : "FAIL") << " length=" << a.size()
             << " targets=" << box_targets(p, q, r).size()
             << " width=" << box_width(p, q, r)
             << " missing=" << missing.size() << '\n';
        if (!ok) {
            for (uint64_t x : missing) cout << x << ' ';
            cout << '\n';
            return 1;
        }
    } else if (mode == "witness") {
        if (argc != 6) throw runtime_error("usage: witness p q r word.txt");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]);
        vector<uint64_t> a = read_word(argv[5]);
        vector<uint64_t> missing;
        if (!verify_word(p, q, r, a, &missing))
            throw runtime_error("word is not universal for this box");
        print_witnesses(p, q, r, a);
    } else if (mode == "analyze") {
        if (argc != 6) throw runtime_error("usage: analyze p q r word.txt");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]);
        vector<uint64_t> a = read_word(argv[5]);
        if (!verify_word(p, q, r, a))
            throw runtime_error("word is not universal for this box");
        analyze_word(p, q, r, a);
    } else if (mode == "info") {
        if (argc != 5) throw runtime_error("usage: info p q r");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]);
        cout << "bits=" << total_bits(p, q, r)
             << " targets=" << box_targets(p, q, r).size()
             << " width=" << box_width(p, q, r)
             << " B=" << rank_slack_bound(p, q, r)
             << " axes=" << p + q + r << '\n';
    } else if (mode == "ranks") {
        if (argc != 5) throw runtime_error("usage: ranks p q r");
        int p = stoi(argv[2]), q = stoi(argv[3]), r = stoi(argv[4]);
        vector<long long> count = rank_counts(p, q, r);
        long long lower = 0;
        cout << "rank count lower delay bound\n";
        for (int rank = 1; rank < (int)count.size(); ++rank) {
            int delay = 0;
            while (lower > 1LL * delay * count[rank]
                         + 1LL * delay * (delay + 1) / 2) ++delay;
            cout << rank << ' ' << count[rank] << ' ' << lower << ' '
                 << delay << ' ' << count[rank] + delay << '\n';
            lower += count[rank];
        }
    } else if (mode == "spiral-info") {
        if (argc != 3) throw runtime_error("usage: spiral-info even_side");
        analyze_spiral(stoi(argv[2]));
    } else if (mode == "band-info") {
        if (argc != 4 && argc != 6)
            throw runtime_error("usage: band-info even_side distinct|closed [pre post]");
        string kind = argv[3];
        if (kind != "distinct" && kind != "closed")
            throw runtime_error("band kind must be distinct or closed");
        int pre = argc == 6 ? stoi(argv[4]) : 0;
        int post = argc == 6 ? stoi(argv[5]) : 0;
        analyze_radial_band(stoi(argv[2]), kind == "closed", pre, post);
    } else {
        throw runtime_error("unknown mode: " + mode);
    }
    return 0;
} catch (const exception& e) {
    cerr << "error: " << e.what() << '\n';
    return 2;
}
