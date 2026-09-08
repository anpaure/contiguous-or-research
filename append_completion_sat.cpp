#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

#include "cadical.hpp"

using namespace std;

namespace {

long long binomial(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

int containment_bound(int k, int n, int target_rank) {
    long long bound = n;
    for (int witness_rank = 1; witness_rank <= k; ++witness_rank) {
        const long long family = binomial(k, witness_rank);
        if (family > n) continue;
        long long candidate = n - family;
        if (witness_rank <= target_rank)
            candidate += binomial(target_rank, witness_rank);
        bound = min(bound, candidate);
    }
    return static_cast<int>(max<long long>(0, min<long long>(n, bound)));
}

vector<char> covered_masks(const vector<int>& word, int limit) {
    vector<char> seen(limit, false);
    vector<int> previous, current;
    for (int x : word) {
        current.clear();
        current.push_back(x);
        for (int old : previous) current.push_back(old | x);
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (int value : current) seen[value] = true;
        previous.swap(current);
    }
    return seen;
}

// By Dilworth's theorem, the width of a finite poset is the number of
// vertices minus a maximum matching in the bipartite strict-order graph.
// Here the order is set inclusion on the masks missing from the fixed
// prefix.  The append formulas are intended for small repair sets; callers
// guard this explicit O(|missing|^2) graph construction.
struct InclusionWidthCertificate {
    int width = 0;
    vector<uint8_t> maximum_antichain;
};

InclusionWidthCertificate inclusion_poset_width(const vector<int>& masks) {
    const int n = static_cast<int>(masks.size());
    vector<vector<int>> adjacency(n);
    for (int left = 0; left < n; ++left)
        for (int right = 0; right < n; ++right)
            if (left != right && !(masks[left] & ~masks[right]))
                adjacency[left].push_back(right);

    vector<int> left_match(n, -1), right_match(n, -1), distance(n);
    int matching = 0;
    while (true) {
        queue<int> pending;
        fill(distance.begin(), distance.end(), -1);
        for (int left = 0; left < n; ++left)
            if (left_match[left] < 0) {
                distance[left] = 0;
                pending.push(left);
            }
        while (!pending.empty()) {
            const int left = pending.front();
            pending.pop();
            for (int right : adjacency[left]) {
                const int next = right_match[right];
                if (next >= 0 && distance[next] < 0) {
                    distance[next] = distance[left] + 1;
                    pending.push(next);
                }
            }
        }

        auto augment = [&](auto&& self, int left) -> bool {
            for (int right : adjacency[left]) {
                const int next = right_match[right];
                if (next < 0 ||
                    (distance[next] == distance[left] + 1 &&
                     self(self, next))) {
                    left_match[left] = right;
                    right_match[right] = left;
                    return true;
                }
            }
            distance[left] = -1;
            return false;
        };

        int added = 0;
        for (int left = 0; left < n; ++left)
            if (left_match[left] < 0 && augment(augment, left)) ++added;
        if (!added) break;
        matching += added;
    }
    InclusionWidthCertificate result;
    result.width = n - matching;
    result.maximum_antichain.assign(n, 0);

    // Recover a maximum antichain from the minimum vertex cover dual to the
    // maximum matching.  Traverse unmatched L->R and matched R->L edges from
    // every unmatched left vertex.  The antichain is
    // {x : x_L is reachable and x_R is not reachable}.
    vector<uint8_t> reachable_left(n, 0), reachable_right(n, 0);
    queue<pair<bool, int>> pending;
    for (int left = 0; left < n; ++left)
        if (left_match[left] < 0) {
            reachable_left[left] = 1;
            pending.push({false, left});
        }
    while (!pending.empty()) {
        const auto [right_side, vertex] = pending.front();
        pending.pop();
        if (!right_side) {
            for (int right : adjacency[vertex]) {
                if (left_match[vertex] == right || reachable_right[right])
                    continue;
                reachable_right[right] = 1;
                pending.push({true, right});
            }
        } else {
            const int left = right_match[vertex];
            if (left >= 0 && !reachable_left[left]) {
                reachable_left[left] = 1;
                pending.push({false, left});
            }
        }
    }
    int antichain_size = 0;
    for (int index = 0; index < n; ++index)
        if (reachable_left[index] && !reachable_right[index]) {
            result.maximum_antichain[index] = 1;
            ++antichain_size;
        }
    if (antichain_size != result.width) {
        cerr << "internal inclusion-width duality failure\n";
        exit(2);
    }
    return result;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc < 5 || argc > 6) {
        cerr << "usage: append_completion_sat k append_length prefix.txt "
                "output.txt [seed]\n";
        return 2;
    }
    const int k = stoi(argv[1]);
    const int q = stoi(argv[2]);
    const int limit = 1 << k;
    const int seed = argc == 6 ? stoi(argv[5]) : 1;
    const bool containment_caps = [] {
        const char* value = getenv("APPEND_CONTAINMENT_CAPS");
        return value && *value && string(value) != "0";
    }();
    vector<int> prefix;
    {
        ifstream input(argv[3]);
        for (int x; input >> x;) {
            if (x <= 0 || x >= limit) return 2;
            prefix.push_back(x);
        }
    }
    int skipped_prefix_index = -1;
    if (const char* value = getenv("APPEND_SKIP_INDEX"); value && *value) {
        skipped_prefix_index = stoi(value);
        if (skipped_prefix_index < 0 ||
            skipped_prefix_index >= static_cast<int>(prefix.size())) {
            cerr << "APPEND_SKIP_INDEX outside prefix\n";
            return 2;
        }
        prefix.erase(prefix.begin() + skipped_prefix_index);
    }
    const vector<char> old_seen = covered_masks(prefix, limit);
    vector<int> missing;
    vector<int> missing_by_rank(k + 1, 0);
    for (int mask = 1; mask < limit; ++mask)
        if (!old_seen[mask]) {
            missing.push_back(mask);
            ++missing_by_rank[
                popcount(static_cast<unsigned>(mask))];
        }

    // A universal fixed prefix needs no completion logic.  Preserve the
    // requested output length with arbitrary nonzero padding; appending terms
    // cannot destroy any old witness.  This also avoids the phase heuristic's
    // modulo-by-zero when missing is empty.
    if (missing.empty()) {
        ofstream output(argv[4]);
        if (!output) return 2;
        for (int position = 0; position < q; ++position) output << 1 << '\n';
        cerr << "SAT completed_length=" << prefix.size() + q
             << " missing=0 trivial_padding=1\n";
        return 0;
    }

    // Every target absent from the fixed prefix needs a witness ending at a
    // new position.  At one right endpoint, the suffix OR values form an
    // inclusion chain and hence contain at most one member of any fixed-rank
    // antichain.  Therefore q appended endpoints can cover at most q missing
    // targets from each rank layer.
    for (int rank = 1; rank <= k; ++rank)
        if (missing_by_rank[rank] > q) {
            cerr << "UNSAT structurally rank=" << rank
                 << " missing_layer=" << missing_by_rank[rank]
                 << " append_endpoints=" << q << '\n';
            return 20;
        }

    // Every target absent from the fixed prefix has a selected witness whose
    // right endpoint is one of the q appended positions.  At a fixed right
    // endpoint, suffix OR values form an inclusion chain.  Hence the entire
    // missing-mask poset is the union of q chains and must have width at most
    // q.  A rank layer is only one possible antichain; this exact test can be
    // strictly stronger.  Avoid constructing a quadratic comparability graph
    // for repair instances already far outside this solver's practical size.
    constexpr int maximum_explicit_poset_size = 4096;
    int missing_poset_width = -1;
    vector<uint8_t> maximum_missing_antichain(missing.size(), 0);
    if (static_cast<int>(missing.size()) <= maximum_explicit_poset_size) {
        InclusionWidthCertificate certificate =
            inclusion_poset_width(missing);
        missing_poset_width = certificate.width;
        maximum_missing_antichain = move(certificate.maximum_antichain);
        if (missing_poset_width > q) {
            cerr << "UNSAT structurally antichain_width="
                 << missing_poset_width
                 << " append_endpoints=" << q << '\n';
            return 20;
        }
    }

    // Every cross-seam interval contains a suffix of the fixed prefix.  Only
    // its OR value matters to the appended variables, and there are at most k
    // distinct such values.
    struct FixedSuffix {
        int value;
        int shortest_length;
    };
    vector<FixedSuffix> fixed_suffixes;
    int suffix = 0;
    for (int i = static_cast<int>(prefix.size()) - 1; i >= 0; --i) {
        suffix |= prefix[i];
        if (fixed_suffixes.empty() || fixed_suffixes.back().value != suffix)
            fixed_suffixes.push_back(
                {suffix, static_cast<int>(prefix.size()) - i});
    }

    CaDiCaL::Solver solver;
    // CaDiCaL requires proof tracing to start immediately after solver
    // initialization, before options, variable declarations, or clauses.
    if (const char* proof = getenv("APPEND_COMPLETION_PROOF"); proof && *proof)
        if (!solver.trace_proof(proof)) {
            cerr << "could not open proof trace " << proof << '\n';
            return 2;
        }
    solver.set("quiet", 1);
    solver.set("seed", seed);
    const int declared_variables =
        q * k + static_cast<int>(missing.size()) *
                      (q * (q + 1) / 2 +
                       q * static_cast<int>(fixed_suffixes.size()) + q);
    solver.declare_more_variables(declared_variables);
    int next = q * k + 1;
    long long clauses = 0;
    auto X = [k](int position, int bit) { return 1 + position * k + bit; };
    auto add = [&](const vector<int>& clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
        ++clauses;
    };

    // Zero append entries are useless and would contradict minimality anyway.
    for (int position = 0; position < q; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) nonzero.push_back(X(position, bit));
        add(nonzero);
    }

    long long candidate_count = 0;
    vector<vector<vector<int>>> rank_endpoint_flags(
        k + 1, vector<vector<int>>(q));
    vector<vector<int>> target_endpoint_flags(
        missing.size(), vector<int>(q, 0));
    long long endpoint_flag_count = 0;
    long long endpoint_distinctness_clauses = 0;
    for (int target_index = 0;
         target_index < static_cast<int>(missing.size()); ++target_index) {
        const int target = missing[target_index];
        const int target_rank = popcount(static_cast<unsigned>(target));
        const int maximum_length = containment_caps
            ? containment_bound(k, static_cast<int>(prefix.size()) + q,
                                target_rank)
            : static_cast<int>(prefix.size()) + q;
        vector<int> support;
        vector<vector<int>> support_by_end(q);
        for (int end = 0; end < q; ++end) {
            auto emit_candidate = [&](int start, int fixed_or,
                                      int physical_length) {
                if (fixed_or & ~target) return;
                if (physical_length > maximum_length) return;
                const int y = next++;
                support.push_back(y);
                support_by_end[end].push_back(y);
                ++candidate_count;
                for (int bit = 0; bit < k; ++bit) {
                    if (!(target & (1 << bit))) {
                        for (int position = start; position <= end; ++position)
                            add({-y, -X(position, bit)});
                    } else if (!(fixed_or & (1 << bit))) {
                        vector<int> clause{-y};
                        for (int position = start; position <= end; ++position)
                            clause.push_back(X(position, bit));
                        add(clause);
                    }
                }
            };

            // Appended-only intervals [start,end].
            for (int start = 0; start <= end; ++start)
                emit_candidate(start, 0, end - start + 1);
            // Cross-seam intervals: one representative per fixed suffix OR.
            for (const FixedSuffix& fixed : fixed_suffixes)
                emit_candidate(0, fixed.value,
                               fixed.shortest_length + end + 1);
        }
        if (support.empty()) {
            cerr << "target " << target << " has no candidate interval\n";
            return 20;
        }
        add(support);
        // Witness variables are existential selectors.  Choosing exactly one
        // is WLOG and removes a large amount of selector symmetry.
        for (int i = 0; i < static_cast<int>(support.size()); ++i)
            for (int j = i + 1; j < static_cast<int>(support.size()); ++j)
                add({-support[i], -support[j]});

        // Materialize the exact chosen new right endpoint for this target.
        // The target selects exactly one witness, so these flags are also an
        // exact-one endpoint encoding for the target.
        for (int end = 0; end < q; ++end) {
            if (support_by_end[end].empty()) continue;
            const int endpoint = next++;
            ++endpoint_flag_count;
            rank_endpoint_flags[target_rank][end].push_back(endpoint);
            target_endpoint_flags[target_index][end] = endpoint;
            vector<int> reverse{-endpoint};
            for (int selector : support_by_end[end]) {
                add({-selector, endpoint});
                reverse.push_back(selector);
            }
            add(reverse);
        }
    }
    // Equal-rank targets are incomparable, while suffix ORs ending at one
    // physical endpoint form a chain.  Hence at most one target from each
    // rank may choose a fixed endpoint.  If a rank layer has exactly q
    // missing members, all q new endpoints are also necessarily used.
    for (int rank = 1; rank <= k; ++rank)
        for (int end = 0; end < q; ++end) {
            const vector<int>& flags = rank_endpoint_flags[rank][end];
            for (int i = 0; i < static_cast<int>(flags.size()); ++i)
                for (int j = i + 1; j < static_cast<int>(flags.size()); ++j) {
                    add({-flags[i], -flags[j]});
                    ++endpoint_distinctness_clauses;
                }
            if (missing_by_rank[rank] == q) add(flags);
        }

    // The equal-rank endpoint clauses above are a special case of the full
    // suffix-chain law: two incomparable missing masks cannot choose the same
    // new right endpoint.  Add only the cross-rank cases here to avoid
    // duplicating the existing clauses.
    long long cross_rank_incomparability_clauses = 0;
    for (int first = 0; first < static_cast<int>(missing.size()); ++first)
        for (int second = first + 1;
             second < static_cast<int>(missing.size()); ++second) {
            if (popcount(static_cast<unsigned>(missing[first])) ==
                popcount(static_cast<unsigned>(missing[second])))
                continue;
            if (!(missing[first] & ~missing[second]) ||
                !(missing[second] & ~missing[first]))
                continue;
            for (int end = 0; end < q; ++end) {
                const int first_flag = target_endpoint_flags[first][end];
                const int second_flag = target_endpoint_flags[second][end];
                if (!first_flag || !second_flag) continue;
                add({-first_flag, -second_flag});
                ++cross_rank_incomparability_clauses;
            }
        }

    // If width equals the number of new endpoints, every endpoint must carry
    // exactly one member of any fixed maximum antichain.  At-most-one is
    // already supplied by the incomparable/equal-rank clauses; these are the
    // corresponding at-least-one endpoint supports.
    long long saturated_antichain_endpoint_clauses = 0;
    if (missing_poset_width == q) {
        for (int end = 0; end < q; ++end) {
            vector<int> support;
            for (int target = 0;
                 target < static_cast<int>(missing.size()); ++target)
                if (maximum_missing_antichain[target] &&
                    target_endpoint_flags[target][end])
                    support.push_back(target_endpoint_flags[target][end]);
            add(support);
            ++saturated_antichain_endpoint_clauses;
        }
    }

    // A literal ordering of the missing masks is a useful default phase.
    // For repair searches, an optional APPEND_PHASE_FILE may provide exactly
    // q valid nonzero masks from a near-solution.  This changes only the SAT
    // polarity heuristic; it adds no clause and cannot affect correctness.
    vector<int> phase_word;
    if (const char* phase_path = getenv("APPEND_PHASE_FILE");
        phase_path && *phase_path) {
        ifstream phase_input(phase_path);
        for (int value; phase_input >> value;) phase_word.push_back(value);
        if (static_cast<int>(phase_word.size()) != q ||
            any_of(phase_word.begin(), phase_word.end(),
                   [&](int value) { return value <= 0 || value >= limit; })) {
            cerr << "APPEND_PHASE_FILE must contain exactly " << q
                 << " valid nonzero masks\n";
            return 2;
        }
    }
    for (int position = 0; position < q; ++position) {
        const int phase_mask = phase_word.empty()
            ? missing[position % missing.size()]
            : phase_word[position];
        for (int bit = 0; bit < k; ++bit)
            solver.phase(phase_mask & (1 << bit) ? X(position, bit)
                                                  : -X(position, bit));
    }
    if (const char* dimacs = getenv("APPEND_COMPLETION_DIMACS"); dimacs && *dimacs) {
        if (const char* error = solver.write_dimacs(dimacs, next - 1)) {
            cerr << "DIMACS error: " << error << '\n';
            return 2;
        }
    }
    cerr << "prefix=" << prefix.size() << " skipped=" << skipped_prefix_index
         << " append=" << q
         << " missing=" << missing.size()
         << " suffix_values=" << fixed_suffixes.size()
         << " containment_caps=" << containment_caps
         << " custom_phase=" << !phase_word.empty()
         << " variables=" << next - 1 << " clauses=" << clauses
         << " candidates=" << candidate_count << '\n';
    cerr << "endpoint_flags=" << endpoint_flag_count
         << " endpoint_distinctness_clauses="
         << endpoint_distinctness_clauses
         << " missing_poset_width=" << missing_poset_width
         << " cross_rank_incomparability_clauses="
         << cross_rank_incomparability_clauses
         << " saturated_antichain_endpoint_clauses="
         << saturated_antichain_endpoint_clauses << '\n';

    const int result = solver.solve();
    if (result != 10) {
        cerr << (result == 20 ? "UNSAT\n" : "UNKNOWN\n");
        return result == 20 ? 20 : 1;
    }
    vector<int> append(q, 0);
    for (int position = 0; position < q; ++position)
        for (int bit = 0; bit < k; ++bit)
            if (solver.val(X(position, bit)) > 0) append[position] |= 1 << bit;
    vector<int> completed = prefix;
    completed.insert(completed.end(), append.begin(), append.end());
    const vector<char> final_seen = covered_masks(completed, limit);
    for (int mask = 1; mask < limit; ++mask)
        if (!final_seen[mask]) {
            cerr << "internal model verification missed " << mask << '\n';
            return 3;
        }
    ofstream output(argv[4]);
    for (int value : append) output << value << '\n';
    cerr << "SAT completed_length=" << completed.size() << '\n';
    return 0;
}
