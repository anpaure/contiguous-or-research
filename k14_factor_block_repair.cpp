#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <utility>
#include <vector>

using namespace std;

// Direct repair of an already valid factor word A.
//
// Split A into blocks of length at least witness_limit.  Reversing a segment
// of blocks, while reversing every block in that segment, reverses one
// contiguous subword of A.  Every interval internal to a block survives, as
// does every interval crossing an unchanged boundary.  Only the two cut
// boundaries change.  We certify every previously covered mask by either an
// internal interval or by a suffix-prefix interval at a selected boundary.
// Consequently every accepted move is monotone: it cannot lose any mask that
// the input word covered.

struct SignedBlock {
    int id = -1;
    bool reversed = false;
};

struct Candidate {
    int model_gain = 0;
    int l = 0;
    int r = 0;
    bool operator<(const Candidate& o) const {
        if (model_gain != o.model_gain) return model_gain > o.model_gain;
        if (l != o.l) return l < o.l;
        return r < o.r;
    }
};

struct RelocCandidate {
    int model_gain = 0;
    int a = 0, b = 0, c = 0;
    bool reverse_x = false;
    // Deliberately reversed ordering: priority_queue::top() is the worst kept
    // candidate, so a better candidate compares less than a worse candidate.
    bool operator<(const RelocCandidate& o) const {
        if (model_gain != o.model_gain) return model_gain > o.model_gain;
        if (a != o.a) return a < o.a;
        if (b != o.b) return b < o.b;
        if (c != o.c) return c < o.c;
        return reverse_x < o.reverse_x;
    }
};

static vector<int> read_word(const string& path) {
    ifstream in(path);
    if (!in) throw runtime_error("cannot open input: " + path);
    vector<int> a;
    int x;
    while (in >> x) a.push_back(x);
    if (a.empty()) throw runtime_error("input word is empty");
    return a;
}

static vector<char> exact_coverage(const vector<int>& a, int masks) {
    vector<char> seen(masks, 0);
    vector<int> prev, cur;
    prev.reserve(32);
    cur.reserve(32);
    for (int x : a) {
        cur.clear();
        cur.push_back(x);
        for (int y : prev) cur.push_back(x | y);
        sort(cur.begin(), cur.end());
        cur.erase(unique(cur.begin(), cur.end()), cur.end());
        for (int y : cur) seen[y] = 1;
        prev.swap(cur);
    }
    return seen;
}

static int count_seen(const vector<char>& seen) {
    return accumulate(seen.begin(), seen.end(), 0);
}

class RepairSearch {
public:
    RepairSearch(vector<int> input, int k_, int block_len_, int witness_limit_,
                 int protect_rank_)
        : original(std::move(input)), k(k_), mask_count(1 << k_),
          block_len(block_len_), witness_limit(witness_limit_),
          protect_rank(protect_rank_) {
        if (block_len < witness_limit)
            throw runtime_error("block length must be at least witness limit");
        for (int x : original) {
            if (x < 0 || x >= mask_count)
                throw runtime_error("entry outside k-bit range");
        }
        make_blocks();
        initial_seen = exact_coverage(original, mask_count);
        make_internal_colors();
        make_initial_path();
        make_arc_cache();
        make_boundary_counts();
        audit_certificate();
    }

    void search_2opt(int requested_target, int keep, const string& output) {
        priority_queue<Candidate> best;
        const int b = static_cast<int>(path.size());
        long long tested = 0, feasible = 0, improving = 0;

        for (int l = 0; l < b; ++l) {
            for (int r = l; r < b; ++r) {
                if (l == 0 && r == b - 1) continue; // whole-word reversal
                ++tested;
                vector<pair<int,int>> removed, added;
                if (l > 0) {
                    removed.push_back({code(path[l - 1]), code(path[l])});
                    added.push_back({code(path[l - 1]), code(flip(path[r]))});
                }
                if (r + 1 < b) {
                    removed.push_back({code(path[r]), code(path[r + 1])});
                    added.push_back({code(flip(path[l])), code(path[r + 1])});
                }

                vector<pair<int,int>> delta;
                build_delta(removed, added, delta);
                if (!preserves_initial(delta)) continue;
                ++feasible;

                if (requested_target >= 0 &&
                    !covered_after_delta(requested_target, delta)) continue;

                int gain = model_net(delta);
                // Positive model net is a certificate of a real improvement:
                // the internal+one-boundary model covered the entire input.
                if (requested_target < 0 && gain <= 0) continue;
                ++improving;
                Candidate c{gain, l, r};
                if ((int)best.size() < keep) best.push(c);
                // operator< deliberately orders a better candidate below a
                // worse one, so priority_queue::top() is the current worst.
                else if (c < best.top()) {
                    best.pop();
                    best.push(c);
                }
            }
        }

        vector<Candidate> finalists;
        while (!best.empty()) {
            finalists.push_back(best.top());
            best.pop();
        }
        sort(finalists.begin(), finalists.end(), [](const Candidate& a, const Candidate& b) {
            if (a.model_gain != b.model_gain) return a.model_gain > b.model_gain;
            if (a.l != b.l) return a.l < b.l;
            return a.r < b.r;
        });

        const int initial_count = count_seen(initial_seen);
        int best_exact = initial_count;
        Candidate winner;
        vector<int> winner_word;
        for (const Candidate& c : finalists) {
            vector<SignedBlock> p = path;
            reverse_signed_segment(p, c.l, c.r);
            vector<int> word = materialize(p);
            vector<char> cov = exact_coverage(word, mask_count);
            bool preserved = true;
            for (int s = 0; s < mask_count; ++s) {
                if (is_protected(s) && !cov[s]) { preserved = false; break; }
            }
            if (!preserved) {
                throw runtime_error("internal error: boundary certificate was unsound");
            }
            int score = count_seen(cov);
            if (requested_target >= 0 && !cov[requested_target]) continue;
            if (score > best_exact) {
                best_exact = score;
                winner = c;
                winner_word.swap(word);
                cerr << "exact improvement coverage=" << score << "/" << mask_count
                     << " model_gain=" << c.model_gain
                     << " reverse_blocks=[" << c.l << ',' << c.r << "]\n";
            }
        }

        cerr << "blocks=" << b << " tested=" << tested << " feasible=" << feasible
             << " model_improving=" << improving << " exact_checked=" << finalists.size()
             << " initial=" << initial_count << " best=" << best_exact << '\n';
        if (winner_word.empty()) {
            cerr << "NO_IMPROVING_2OPT\n";
            return;
        }
        ofstream out(output);
        if (!out) throw runtime_error("cannot open output: " + output);
        for (size_t i = 0; i < winner_word.size(); ++i)
            out << winner_word[i] << (i + 1 == winner_word.size() ? '\n' : ' ');
        cerr << "WROTE " << output << '\n';
    }

    // Three cuts a<b<c split the current signed-block path as P|X|Y|S.
    // The relocation replaces it by P|Y|X|S.  When reverse_x is true, X is
    // also reversed as a word (block order reversed and every orientation
    // flipped).  All internal intervals survive; precisely three joins can
    // change.  The sparse <=witness_limit color delta is therefore exact.
    void search_relocate(int requested_target, int keep, const string& output) {
        priority_queue<RelocCandidate> best;
        const int n = static_cast<int>(path.size());
        long long tested = 0, gain_prefilter = 0, feasible = 0, improving = 0;

        for (int a = 0; a < n - 1; ++a) {
            if ((a & 15) == 0)
                cerr << "relocate progress a=" << a << '/' << n
                     << " tested=" << tested << " feasible=" << feasible
                     << " improving=" << improving << '\n';
            for (int b = a + 1; b < n; ++b) {
                for (int c = b + 1; c <= n; ++c) {
                    for (int rx = 0; rx <= 1; ++rx) {
                        ++tested;
                        vector<pair<int,int>> removed, added;
                        if (a > 0)
                            removed.push_back({code(path[a - 1]), code(path[a])});
                        removed.push_back({code(path[b - 1]), code(path[b])});
                        if (c < n)
                            removed.push_back({code(path[c - 1]), code(path[c])});

                        // Y remains forward.  X either remains forward or is
                        // reversed as one word.
                        SignedBlock first_x = rx ? flip(path[b - 1]) : path[a];
                        SignedBlock last_x  = rx ? flip(path[a])     : path[b - 1];
                        if (a > 0)
                            added.push_back({code(path[a - 1]), code(path[b])});
                        added.push_back({code(path[c - 1]), code(first_x)});
                        if (c < n)
                            added.push_back({code(last_x), code(path[c])});

                        if (!new_arcs_can_gain(added, requested_target)) continue;
                        ++gain_prefilter;
                        vector<pair<int,int>> delta;
                        build_delta_fast(removed, added, delta);
                        if (!preserves_initial(delta)) continue;
                        ++feasible;
                        if (requested_target >= 0 &&
                            !covered_after_delta(requested_target, delta)) continue;
                        int gain = model_net(delta);
                        if (requested_target < 0 && gain <= 0) continue;
                        ++improving;
                        RelocCandidate cand{gain, a, b, c, bool(rx)};
                        if ((int)best.size() < keep) best.push(cand);
                        else if (cand < best.top()) {
                            best.pop();
                            best.push(cand);
                        }
                    }
                }
            }
        }

        vector<RelocCandidate> finalists;
        while (!best.empty()) {
            finalists.push_back(best.top());
            best.pop();
        }
        sort(finalists.begin(), finalists.end(), [](const RelocCandidate& x,
                                                    const RelocCandidate& y) {
            if (x.model_gain != y.model_gain) return x.model_gain > y.model_gain;
            if (x.a != y.a) return x.a < y.a;
            if (x.b != y.b) return x.b < y.b;
            if (x.c != y.c) return x.c < y.c;
            return x.reverse_x < y.reverse_x;
        });

        const int initial_count = count_seen(initial_seen);
        int best_exact = initial_count;
        RelocCandidate winner;
        vector<int> winner_word;
        for (const RelocCandidate& cand : finalists) {
            vector<SignedBlock> p = path;
            relocate_signed_segment(p, cand.a, cand.b, cand.c, cand.reverse_x);
            vector<int> word = materialize(p);
            vector<char> cov = exact_coverage(word, mask_count);
            bool preserved = true;
            for (int s = 0; s < mask_count; ++s) {
                if (is_protected(s) && !cov[s]) { preserved = false; break; }
            }
            if (!preserved)
                throw runtime_error("internal error: relocation certificate was unsound");
            int score = count_seen(cov);
            if (requested_target >= 0 && !cov[requested_target]) continue;
            if (score > best_exact) {
                best_exact = score;
                winner = cand;
                winner_word.swap(word);
                cerr << "exact relocation improvement coverage=" << score << '/'
                     << mask_count << " model_gain=" << cand.model_gain
                     << " cuts=" << cand.a << ',' << cand.b << ',' << cand.c
                     << " reverse_x=" << cand.reverse_x << '\n';
            }
        }

        cerr << "blocks=" << n << " tested=" << tested
             << " gain_prefilter=" << gain_prefilter << " feasible=" << feasible
             << " model_improving=" << improving << " exact_checked="
             << finalists.size() << " initial=" << initial_count
             << " best=" << best_exact << '\n';
        if (winner_word.empty()) {
            cerr << "NO_IMPROVING_RELOCATION\n";
            return;
        }
        ofstream out(output);
        if (!out) throw runtime_error("cannot open output: " + output);
        for (size_t i = 0; i < winner_word.size(); ++i)
            out << winner_word[i] << (i + 1 == winner_word.size() ? '\n' : ' ');
        cerr << "WROTE " << output << '\n';
    }

    int initial_coverage_count() const { return count_seen(initial_seen); }

private:
    vector<int> original;
    int k, mask_count, block_len, witness_limit, protect_rank;
    vector<vector<int>> blocks;
    vector<SignedBlock> path;
    vector<char> initial_seen, internal_seen;
    vector<int> boundary_count;
    vector<vector<uint16_t>> arc_cache;
    vector<int> delta_work;
    vector<int> delta_touched;

    void make_blocks() {
        // Use equal block_len chunks, but merge a short tail into the previous
        // block so every block has length >= witness_limit.
        for (int i = 0; i < (int)original.size(); i += block_len) {
            int e = min<int>(original.size(), i + block_len);
            blocks.emplace_back(original.begin() + i, original.begin() + e);
        }
        if (blocks.size() >= 2 && (int)blocks.back().size() < witness_limit) {
            blocks[blocks.size() - 2].insert(blocks[blocks.size() - 2].end(),
                                              blocks.back().begin(), blocks.back().end());
            blocks.pop_back();
        }
        for (const auto& b : blocks)
            if ((int)b.size() < witness_limit)
                throw runtime_error("cannot form blocks of the requested minimum size");
    }

    int value_at(const SignedBlock& s, int pos) const {
        const auto& b = blocks[s.id];
        return s.reversed ? b[b.size() - 1 - pos] : b[pos];
    }

    int code(const SignedBlock& s) const { return 2 * s.id + int(s.reversed); }
    SignedBlock decode(int c) const { return SignedBlock{c / 2, bool(c & 1)}; }
    SignedBlock flip(SignedBlock s) const { s.reversed = !s.reversed; return s; }

    void make_initial_path() {
        path.resize(blocks.size());
        for (int i = 0; i < (int)blocks.size(); ++i) path[i] = {i, false};
    }

    void make_internal_colors() {
        internal_seen.assign(mask_count, 0);
        for (const auto& b : blocks) {
            for (int l = 0; l < (int)b.size(); ++l) {
                int v = 0;
                for (int r = l; r < (int)b.size() && r - l + 1 <= witness_limit; ++r) {
                    v |= b[r];
                    internal_seen[v] = 1;
                }
            }
        }
    }

    vector<uint16_t> compute_arc(int ca, int cb) const {
        SignedBlock a = decode(ca), b = decode(cb);
        vector<int> suf(1, 0), pre(1, 0);
        int v = 0;
        int na = blocks[a.id].size(), nb = blocks[b.id].size();
        for (int len = 1; len < witness_limit && len <= na; ++len) {
            v |= value_at(a, na - len);
            suf.push_back(v);
        }
        v = 0;
        for (int len = 1; len < witness_limit && len <= nb; ++len) {
            v |= value_at(b, len - 1);
            pre.push_back(v);
        }
        vector<uint16_t> colors;
        for (int ls = 1; ls < (int)suf.size(); ++ls)
            for (int lp = 1; lp < (int)pre.size() && ls + lp <= witness_limit; ++lp)
                colors.push_back(uint16_t(suf[ls] | pre[lp]));
        sort(colors.begin(), colors.end());
        colors.erase(unique(colors.begin(), colors.end()), colors.end());
        return colors;
    }

    void make_arc_cache() {
        int states = 2 * blocks.size();
        arc_cache.resize(size_t(states) * states);
        for (int a = 0; a < states; ++a)
            for (int b = 0; b < states; ++b)
                if (a / 2 != b / 2)
                    arc_cache[size_t(a) * states + b] = compute_arc(a, b);
    }

    const vector<uint16_t>& arc(int a, int b) const {
        int states = 2 * blocks.size();
        return arc_cache[size_t(a) * states + b];
    }

    void make_boundary_counts() {
        boundary_count.assign(mask_count, 0);
        for (int i = 0; i + 1 < (int)path.size(); ++i)
            for (uint16_t s : arc(code(path[i]), code(path[i + 1])))
                ++boundary_count[s];
    }

    void build_delta_fast(const vector<pair<int,int>>& removed,
                          const vector<pair<int,int>>& added,
                          vector<pair<int,int>>& out) {
        if (delta_work.empty()) delta_work.assign(mask_count, 0);
        delta_touched.clear();
        auto change = [&](int s, int d) {
            if (delta_work[s] == 0) delta_touched.push_back(s);
            delta_work[s] += d;
        };
        for (auto [a,b] : removed) for (uint16_t s : arc(a,b)) change(s, -1);
        for (auto [a,b] : added) for (uint16_t s : arc(a,b)) change(s, +1);
        out.clear();
        out.reserve(delta_touched.size());
        for (int s : delta_touched) {
            if (delta_work[s]) out.push_back({s, delta_work[s]});
            delta_work[s] = 0;
        }
    }

    bool new_arcs_can_gain(const vector<pair<int,int>>& added,
                           int requested_target) const {
        for (auto [a,b] : added) {
            const auto& colors = arc(a,b);
            if (requested_target >= 0) {
                if (binary_search(colors.begin(), colors.end(),
                                  uint16_t(requested_target))) return true;
            } else {
                for (uint16_t s : colors) if (!initial_seen[s]) return true;
            }
        }
        return false;
    }

    void audit_certificate() const {
        for (int s = 0; s < mask_count; ++s) {
            if (is_protected(s) && !internal_seen[s] && boundary_count[s] == 0) {
                throw runtime_error("block certificate misses protected mask " +
                                    to_string(s) +
                                    "; increase --witness-limit/--block");
            }
        }
    }

    void build_delta(const vector<pair<int,int>>& removed,
                     const vector<pair<int,int>>& added,
                     vector<pair<int,int>>& out) const {
        unordered_map<int,int> d;
        d.reserve(512);
        for (auto [a,b] : removed) for (uint16_t s : arc(a,b)) --d[s];
        for (auto [a,b] : added) for (uint16_t s : arc(a,b)) ++d[s];
        out.clear();
        out.reserve(d.size());
        for (auto [s,x] : d) if (x) out.push_back({s,x});
    }

    int delta_for(int mask, const vector<pair<int,int>>& d) const {
        for (auto [s,x] : d) if (s == mask) return x;
        return 0;
    }

    bool preserves_initial(const vector<pair<int,int>>& d) const {
        for (auto [s,x] : d) {
            if (x < 0 && is_protected(s) && !internal_seen[s] &&
                boundary_count[s] + x <= 0) return false;
        }
        return true;
    }

    bool is_protected(int s) const {
        return initial_seen[s] && __builtin_popcount((unsigned)s) <= protect_rank;
    }

    bool covered_after_delta(int s, const vector<pair<int,int>>& d) const {
        if (internal_seen[s]) return true;
        return boundary_count[s] + delta_for(s, d) > 0;
    }

    int model_net(const vector<pair<int,int>>& d) const {
        int net = 0;
        for (auto [s,x] : d) {
            if (internal_seen[s]) continue;
            bool before = boundary_count[s] > 0;
            bool after = boundary_count[s] + x > 0;
            net += int(after) - int(before);
        }
        return net;
    }

    static void reverse_signed_segment(vector<SignedBlock>& p, int l, int r) {
        reverse(p.begin() + l, p.begin() + r + 1);
        for (int i = l; i <= r; ++i) p[i].reversed = !p[i].reversed;
    }

    static void relocate_signed_segment(vector<SignedBlock>& p, int a, int b,
                                        int c, bool reverse_x) {
        vector<SignedBlock> q;
        q.reserve(p.size());
        q.insert(q.end(), p.begin(), p.begin() + a);       // P
        q.insert(q.end(), p.begin() + b, p.begin() + c);   // Y
        if (!reverse_x) {
            q.insert(q.end(), p.begin() + a, p.begin() + b);
        } else {
            for (int i = b - 1; i >= a; --i) {
                SignedBlock s = p[i];
                s.reversed = !s.reversed;
                q.push_back(s);
            }
        }
        q.insert(q.end(), p.begin() + c, p.end());          // S
        p.swap(q);
    }

    vector<int> materialize(const vector<SignedBlock>& p) const {
        vector<int> a;
        a.reserve(original.size());
        for (const SignedBlock& s : p) {
            int n = blocks[s.id].size();
            for (int i = 0; i < n; ++i) a.push_back(value_at(s, i));
        }
        return a;
    }
};

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (argc < 2) {
        cerr << "usage: " << argv[0]
             << " FACTOR.txt [--mode 2opt|relocate] [--target MASK] [--block 10]"
                " [--witness-limit 10] [--protect-rank 14] [--keep 200] [--output repaired.txt]"
                " [--k 14]\n";
        return 2;
    }
    string input = argv[1], output = "k14_factor_block_repaired.txt";
    int k = 14, block = 10, witness = 10, target = -1, keep = 200;
    int protect_rank = 14;
    string mode = "2opt";
    for (int i = 2; i < argc; ++i) {
        string s = argv[i];
        auto need = [&]() -> string {
            if (++i >= argc) throw runtime_error("missing value after " + s);
            return argv[i];
        };
        if (s == "--target") target = stoi(need());
        else if (s == "--mode") mode = need();
        else if (s == "--block") block = stoi(need());
        else if (s == "--witness-limit") witness = stoi(need());
        else if (s == "--protect-rank") protect_rank = stoi(need());
        else if (s == "--keep") keep = stoi(need());
        else if (s == "--output") output = need();
        else if (s == "--k") k = stoi(need());
        else throw runtime_error("unknown option: " + s);
    }
    try {
        if (protect_rank < 0 || protect_rank > k)
            throw runtime_error("--protect-rank must lie in [0,k]");
        RepairSearch search(read_word(input), k, block, witness, protect_rank);
        cerr << "input coverage=" << search.initial_coverage_count() << '/' << (1 << k) << '\n';
        if (mode == "2opt") search.search_2opt(target, keep, output);
        else if (mode == "relocate") search.search_relocate(target, keep, output);
        else throw runtime_error("--mode must be 2opt or relocate");
    } catch (const exception& e) {
        cerr << "error: " << e.what() << '\n';
        return 1;
    }
    return 0;
}
