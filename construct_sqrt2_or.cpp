#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

using Mask = uint64_t;
using Chain = vector<Mask>;

static uint64_t choose_u64(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    __int128 value = 1;
    for (int i = 1; i <= r; ++i) {
        value = value * (n - r + i) / i;
        if (value > numeric_limits<uint64_t>::max())
            throw overflow_error("binomial coefficient overflow");
    }
    return static_cast<uint64_t>(value);
}

static uint64_t width(int n) {
    return choose_u64(n, n / 2);
}

// The de Bruijn--Tengbergen--Kruyswijk recursive symmetric-chain
// decomposition.  Coordinates in bits[] may be arbitrary bit positions.
static vector<Chain> symmetric_chains(const vector<int>& bits) {
    vector<Chain> chains(1, Chain{0});
    for (int bit : bits) {
        const Mask z = Mask{1} << bit;
        vector<Chain> next;
        next.reserve(chains.size() * 2);
        for (const Chain& c : chains) {
            Chain long_child = c;
            long_child.push_back(c.back() | z);
            next.push_back(std::move(long_child));

            if (c.size() >= 2) {
                Chain short_child;
                short_child.reserve(c.size() - 1);
                for (size_t i = 0; i + 1 < c.size(); ++i)
                    short_child.push_back(c[i] | z);
                next.push_back(std::move(short_child));
            }
        }
        chains = std::move(next);
    }
    return chains;
}

// [C0, C1\C0, ..., Cs\C{s-1}, U\Cs], omitting empty blocks.
// Prefix ORs expose C; suffix ORs expose its complement-dual chain.
static vector<Mask> bridge_word(const Chain& c, Mask universe) {
    vector<Mask> out;
    if (c.front() != 0) out.push_back(c.front());
    for (size_t i = 1; i < c.size(); ++i) {
        Mask difference = c[i] & ~c[i - 1];
        if (difference != 0) out.push_back(difference);
    }
    Mask top_complement = universe & ~c.back();
    if (top_complement != 0) out.push_back(top_complement);
    if (out.empty()) throw logic_error("a bridge word became empty");
    return out;
}

static __int128 complement_bridge_length128(int p, int q) {
    const __int128 left_count = width(p - 1);
    const __int128 right_count = width(q);
    const __int128 two_p_minus_1 = __int128{1} << (p - 1);
    const __int128 two_q = __int128{1} << q;
    return right_count * (two_p_minus_1 + 2 * left_count - 2)
         + left_count * (two_q + right_count - 2)
         + (q & 1);
}

static uint64_t complement_bridge_length(int p, int q) {
    __int128 value = complement_bridge_length128(p, q);
    if (value > numeric_limits<uint64_t>::max())
        throw overflow_error("constructed length overflow");
    return static_cast<uint64_t>(value);
}

static int best_split(int k) {
    int best_p = 1;
    __int128 best = complement_bridge_length128(1, k - 1);
    for (int p = 2; p < k; ++p) {
        __int128 candidate = complement_bridge_length128(p, k - p);
        if (candidate < best) {
            best = candidate;
            best_p = p;
        }
    }
    return best_p;
}

struct Construction {
    int k = 0;
    int p = 0;
    int q = 0;
    vector<Mask> word;
};

static Construction construct_complement_bridge(int k, int requested_p = 0) {
    if (k < 1 || k > 25)
        throw invalid_argument("this output-explicit implementation supports 1 <= k <= 25");
    if (k == 1) return Construction{1, 1, 0, vector<Mask>{1}};

    const int p = requested_p == 0 ? best_split(k) : requested_p;
    const int q = k - p;
    if (p < 1 || q < 1)
        throw invalid_argument("the split must satisfy 1 <= p < k");

    vector<int> p_base_bits, q_bits;
    for (int bit = 0; bit + 1 < p; ++bit) p_base_bits.push_back(bit);
    for (int bit = p; bit < k; ++bit) q_bits.push_back(bit);
    const Mask z = Mask{1} << (p - 1);
    const Mask p_universe = (Mask{1} << p) - 1;
    const Mask q_universe = ((Mask{1} << k) - 1) ^ p_universe;

    // One long lifted child for every chain of Q_{p-1}.
    vector<Chain> left;
    for (Chain c : symmetric_chains(p_base_bits)) {
        c.push_back(c.back() | z);
        left.push_back(std::move(c));
    }
    vector<Chain> right = symmetric_chains(q_bits);
    if (left.size() != width(p - 1) || right.size() != width(q))
        throw logic_error("SCD chain count identity failed");

    vector<vector<Mask>> left_bridge, right_bridge;
    left_bridge.reserve(left.size());
    right_bridge.reserve(right.size());
    for (const Chain& c : left) left_bridge.push_back(bridge_word(c, p_universe));
    for (const Chain& c : right) right_bridge.push_back(bridge_word(c, q_universe));

    // A shortest right chain is the bridge that can be split across the two
    // ends without losing an assigned proper prefix/suffix.
    size_t dstar = 0;
    for (size_t j = 1; j < right.size(); ++j)
        if (right[j].size() < right[dstar].size()) dstar = j;

    const int L = static_cast<int>(left.size());
    const int R = static_cast<int>(right.size());
    const int start = L + static_cast<int>(dstar);

    // Implicit Hierholzer tour of the bidirected complete bipartite graph.
    // Each left vertex has one outgoing arc to every right vertex and vice
    // versa.  Counters avoid storing the Theta(LR) arc catalogue.
    vector<int> next_left(L, 0), next_right(R, 0);
    vector<int> stack{start}, circuit;
    circuit.reserve(static_cast<size_t>(2) * L * R + 1);
    while (!stack.empty()) {
        int v = stack.back();
        if (v < L && next_left[v] < R) {
            stack.push_back(L + next_left[v]++);
        } else if (v >= L && next_right[v - L] < L) {
            stack.push_back(next_right[v - L]++);
        } else {
            circuit.push_back(v);
            stack.pop_back();
        }
    }
    reverse(circuit.begin(), circuit.end());
    if (circuit.size() != static_cast<size_t>(2) * L * R + 1 ||
        circuit.front() != start || circuit.back() != start)
        throw logic_error("implicit Euler tour failed");

    auto bridge = [&](int vertex) -> const vector<Mask>& {
        return vertex < L ? left_bridge[vertex] : right_bridge[vertex - L];
    };
    vector<Mask> answer;
    const uint64_t expected = complement_bridge_length(p, q);
    if (expected > answer.max_size()) throw length_error("answer is too large");
    answer.reserve(static_cast<size_t>(expected));
    auto append_all = [&](const vector<Mask>& blocks) {
        answer.insert(answer.end(), blocks.begin(), blocks.end());
    };

    const vector<Mask>& cut = right_bridge[dstar];
    if (q == 1) {
        append_all(cut);
    } else {
        answer.insert(answer.end(), cut.begin() + 1, cut.end());
    }
    for (size_t i = 1; i + 1 < circuit.size(); ++i)
        append_all(bridge(circuit[i]));
    if (q == 1) {
        append_all(cut);
    } else {
        answer.insert(answer.end(), cut.begin(), cut.end() - 1);
    }

    if (answer.size() != expected)
        throw logic_error("exact complement-bridge length identity failed");
    for (Mask x : answer)
        if (x == 0 || (x >> k) != 0)
            throw logic_error("constructor emitted an invalid mask");
    return Construction{k, p, q, std::move(answer)};
}

// Independent suffix-OR verifier.  The live suffix values form a strict
// inclusion chain after adjacent duplicates are removed, hence at most k
// values survive per output position.
static bool verify_universal(const vector<Mask>& word, int k) {
    if (k > 25) throw invalid_argument("dense verifier supports k <= 25");
    vector<uint8_t> seen(size_t{1} << k, 0);
    vector<Mask> suffixes, next;
    for (Mask a : word) {
        next.clear();
        next.push_back(a);
        seen[a] = 1;
        for (Mask old : suffixes) {
            Mask value = old | a;
            if (value != next.back()) next.push_back(value);
            seen[value] = 1;
        }
        suffixes.swap(next);
        if (suffixes.size() > static_cast<size_t>(k))
            throw logic_error("suffix ORs failed to form a strict chain");
    }
    for (size_t mask = 1; mask < seen.size(); ++mask)
        if (!seen[mask]) return false;
    return true;
}

static void self_test(int maximum_k) {
    for (int k = 1; k <= maximum_k; ++k) {
        Construction c = construct_complement_bridge(k);
        if (!verify_universal(c.word, k))
            throw runtime_error("universality failed at k=" + to_string(k));
        cerr << "k=" << k << " split=" << c.p << '+' << c.q
             << " length=" << c.word.size() << " PASS\n";
    }
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    bool verify = false;
    bool length_only = false;
    if (argc >= 2 && string(argv[1]) == "--self-test") {
        int maximum_k = argc >= 3 ? atoi(argv[2]) : 14;
        self_test(maximum_k);
        return 0;
    }
    for (int i = 1; i < argc; ++i) {
        string arg = argv[i];
        if (arg == "--verify") verify = true;
        else if (arg == "--length-only") length_only = true;
        else throw invalid_argument("unknown option: " + arg);
    }

    int k, p = 0;
    if (!(cin >> k)) return 0;
    if (cin >> p) {}
    Construction c = construct_complement_bridge(k, p);
    if (verify && !verify_universal(c.word, k))
        throw runtime_error("the constructed word failed verification");

    cout << c.word.size() << '\n';
    if (!length_only) {
        for (size_t i = 0; i < c.word.size(); ++i) {
            if (i) cout << ' ';
            cout << c.word[i];
        }
        cout << '\n';
    }
    cerr << "split=" << c.p << '+' << c.q
         << " length=" << c.word.size();
    if (verify) cerr << " verified=PASS";
    cerr << '\n';
}

