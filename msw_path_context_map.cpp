#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using U32 = std::uint32_t;

static std::pair<U32, int> apply_g(U32 x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, down_zero = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++down_zero;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 && (before[i] == 0 || before[i] == 1))
            if (++ordinal == down_zero + 1) return {x | (U32{1} << i), i};
    assert(false);
    return {};
}

static std::pair<U32, int> apply_h(U32 y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, up_one = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) && height == 1) ++up_one;
        height += ((y >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) && (before[i] == 0 || before[i] == 1))
            if (++ordinal == up_one) return {y & ~(U32{1} << i), i};
    assert(false);
    return {};
}

static std::string bits(U32 x, int length) {
    std::string out;
    for (int i = 0; i < length; ++i)
        out.push_back(((x >> i) & 1U) ? '1' : '0');
    return out;
}

struct PathFactor {
    int m;
    std::vector<int> owner;
    std::vector<U32> roots;

    explicit PathFactor(int dimension)
        : m(dimension), owner(U32{1} << (2 * m), -1) {
        generate(0, 0, 0, 0);
    }

    void add(U32 root) {
        int id = static_cast<int>(roots.size());
        roots.push_back(root);
        U32 x = root;
        assert(owner[x] < 0);
        owner[x] = id;
        for (int i = 0; i < m; ++i) {
            auto [y, ignored_g] = apply_g(x, m);
            (void)ignored_g;
            assert(owner[y] < 0);
            owner[y] = id;
            auto [next, ignored_h] = apply_h(y, m);
            (void)ignored_h;
            x = next;
            assert(owner[x] < 0);
            owner[x] = id;
        }
    }

    void generate(int position, int up, int down, U32 mask) {
        if (position == 2 * m) {
            add(mask);
            return;
        }
        if (up < m)
            generate(position + 1, up + 1, down, mask | (U32{1} << position));
        if (down < up)
            generate(position + 1, up, down + 1, mask);
    }

    std::vector<U32> states(U32 root) const {
        std::vector<U32> out{root};
        U32 x = root;
        for (int i = 0; i < m; ++i) {
            auto [y, ignored_g] = apply_g(x, m);
            (void)ignored_g;
            out.push_back(y);
            auto [next, ignored_h] = apply_h(y, m);
            (void)ignored_h;
            x = next;
            out.push_back(x);
        }
        return out;
    }
};

static U32 parse(const std::string& word) {
    U32 value = 0;
    for (int i = 0; i < static_cast<int>(word.size()); ++i)
        if (word[i] == '1') value |= U32{1} << i;
    return value;
}

static U32 swap_first(U32 word) {
    if (((word >> 0) ^ (word >> 1)) & 1U)
        word ^= U32{1} | (U32{1} << 1);
    return word;
}

static U32 reverse_complement(U32 word, int length) {
    U32 out = 0;
    for (int p = 0; p < length; ++p)
        if (((word >> (length - 1 - p)) & 1U) == 0)
            out |= U32{1} << p;
    return out;
}

struct EdgeWitness {
    U32 hub_root = 0;
    U32 left_state = 0;
    U32 right_state = 0;
    int left_index = -1;
    int right_index = -1;
};

static std::map<std::pair<U32,U32>,EdgeWitness> suffix_edges(int rank) {
    PathFactor base(rank), boundary(rank + 1);
    struct Record { U32 root, state; int index; };
    std::map<int,std::map<U32,Record>> by_hub;
    for (U32 root : base.roots) {
        U32 capped_root = U32{1} | (root << 2);
        int capped_owner = boundary.owner[capped_root];
        assert(capped_owner >= 0);
        auto path = boundary.states(boundary.roots[capped_owner]);
        for (int index = 0; index < static_cast<int>(path.size()); ++index) {
            U32 state = path[index];
            int hub = boundary.owner[swap_first(state)];
            assert(hub >= 0);
            if (hub == capped_owner) continue;
            by_hub[hub].try_emplace(root, Record{root, state, index});
        }
    }
    std::map<std::pair<U32,U32>,EdgeWitness> out;
    for (const auto& [hub, records] : by_hub) {
        for (auto left = records.begin(); left != records.end(); ++left) {
            auto right = left;
            for (++right; right != records.end(); ++right) {
                auto key = std::make_pair(left->first, right->first);
                out.try_emplace(key, EdgeWitness{
                    boundary.roots[hub], left->second.state,
                    right->second.state, left->second.index,
                    right->second.index});
            }
        }
    }
    return out;
}

static std::map<int,std::vector<std::pair<U32,int>>> boundary_records(
        const PathFactor& base, const PathFactor& boundary, U32 root) {
    std::map<int,std::vector<std::pair<U32,int>>> out;
    U32 capped_root = U32{1} | (root << 2);
    int capped_owner = boundary.owner[capped_root];
    auto path = boundary.states(boundary.roots[capped_owner]);
    for (int index = 0; index < static_cast<int>(path.size()); ++index) {
        U32 state = path[index];
        int hub = boundary.owner[swap_first(state)];
        if (hub != capped_owner) out[hub].push_back({state, index});
    }
    (void)base;
    return out;
}

static U32 wrapped_boundary_state(U32 old_boundary_state, int rank) {
    assert((old_boundary_state & 3U) == 2U); // prefix 01
    U32 inner = old_boundary_state >> 2;
    U32 mirrored = reverse_complement(inner, 2 * rank);
    // 01 . 1 . mirror(inner) . 1
    return (U32{1} << 1) | (U32{1} << 2)
           | (mirrored << 3) | (U32{1} << (2 * rank + 3));
}

static void dump_wrap_edges(int rank) {
    auto small = suffix_edges(rank);
    auto large = suffix_edges(rank + 1);
    PathFactor base(rank), boundary(rank + 1), high_boundary(rank + 2);
    int failures = 0;
    for (const auto& [key, witness] : small) {
        U32 left_wrap = U32{1}
            | (reverse_complement(key.first, 2 * rank) << 1);
        left_wrap |= U32{0} << (2 * rank + 1);
        U32 right_wrap = U32{1}
            | (reverse_complement(key.second, 2 * rank) << 1);
        std::pair<U32,U32> lifted_key = std::minmax(left_wrap, right_wrap);
        auto found = large.find(lifted_key);
        if (found == large.end()) {
            ++failures;
            continue;
        }
        const auto& lifted = found->second;
        auto left_records = boundary_records(base, boundary, key.first);
        auto right_records = boundary_records(base, boundary, key.second);
        bool correlated = false;
        U32 correlated_left = 0, correlated_right = 0, correlated_hub = 0;
        for (const auto& [hub, left_list] : left_records) {
            auto right_found = right_records.find(hub);
            if (right_found == right_records.end()) continue;
            for (auto [left_state, left_index] : left_list) {
                (void)left_index;
                U32 left_lift = wrapped_boundary_state(left_state, rank);
                for (auto [right_state, right_index] : right_found->second) {
                    (void)right_index;
                    U32 right_lift = wrapped_boundary_state(right_state, rank);
                    int left_hub = high_boundary.owner[swap_first(left_lift)];
                    int right_hub = high_boundary.owner[swap_first(right_lift)];
                    if (left_hub == right_hub) {
                        correlated = true;
                        correlated_left = left_lift;
                        correlated_right = right_lift;
                        correlated_hub = high_boundary.roots[left_hub];
                        break;
                    }
                }
                if (correlated) break;
            }
            if (correlated) break;
        }
        std::cout << "WRAP_EDGE x=" << bits(key.first, 2 * rank)
                  << " y=" << bits(key.second, 2 * rank)
                  << " hub=" << bits(witness.hub_root, 2 * (rank + 1))
                  << " states=" << bits(witness.left_state, 2 * (rank + 1))
                  << '@' << witness.left_index << ','
                  << bits(witness.right_state, 2 * (rank + 1))
                  << '@' << witness.right_index
                  << " Wx=" << bits(left_wrap, 2 * (rank + 1))
                  << " Wy=" << bits(right_wrap, 2 * (rank + 1))
                  << " new_hub="
                  << bits(lifted.hub_root, 2 * (rank + 2))
                  << " new_states="
                  << bits(lifted.left_state, 2 * (rank + 2))
                  << '@' << lifted.left_index << ','
                  << bits(lifted.right_state, 2 * (rank + 2))
                  << '@' << lifted.right_index
                  << " correlated=" << correlated;
        if (correlated)
            std::cout << " corr_hub="
                      << bits(correlated_hub, 2 * (rank + 2))
                      << " corr_states="
                      << bits(correlated_left, 2 * (rank + 2)) << ','
                      << bits(correlated_right, 2 * (rank + 2));
        std::cout << '\n';
    }
    std::cout << "WRAP_EDGE_SUMMARY rank=" << rank
              << " edges=" << small.size()
              << " failures=" << failures << '\n';
}

static std::set<std::pair<int,int>> intersection_edges(
        const std::vector<std::set<int>>& supports) {
    std::map<int,std::vector<int>> fibres;
    for (int root = 0; root < static_cast<int>(supports.size()); ++root)
        for (int hub : supports[root]) fibres[hub].push_back(root);
    std::set<std::pair<int,int>> edges;
    for (const auto& [hub, roots] : fibres) {
        (void)hub;
        for (int i = 0; i < static_cast<int>(roots.size()); ++i)
            for (int j = i + 1; j < static_cast<int>(roots.size()); ++j)
                edges.emplace(roots[i], roots[j]);
    }
    return edges;
}

static void audit_left_right(int rank) {
    PathFactor base(rank), boundary(rank + 1);
    const int root_count = static_cast<int>(base.roots.size());
    std::vector<std::set<int>> left(root_count), right(root_count);
    std::vector<std::set<int>> left_nonself(root_count), right_nonself(root_count);
    std::map<int,std::set<int>> left_to_right;
    std::map<int,std::set<int>> right_to_left;

    for (int root_id = 0; root_id < root_count; ++root_id) {
        U32 root = base.roots[root_id];
        const int capped_owner = boundary.owner[U32{1} | (root << 2)];
        const int tailed_owner = boundary.owner[
            root | (U32{1} << (2 * rank + 1))];
        for (U32 state : base.states(root)) {
            U32 capped = U32{1} | (state << 2);          // 10 state
            U32 tailed = state | (U32{1} << (2 * rank + 1)); // state 01
            int lhub = boundary.owner[capped];
            int rhub = boundary.owner[tailed];
            assert(lhub >= 0 && rhub >= 0);
            left[root_id].insert(lhub);
            right[root_id].insert(rhub);
            if (lhub != capped_owner) left_nonself[root_id].insert(lhub);
            if (rhub != tailed_owner) right_nonself[root_id].insert(rhub);
            left_to_right[lhub].insert(rhub);
            right_to_left[rhub].insert(lhub);
        }
    }

    auto le = intersection_edges(left);
    auto re = intersection_edges(right);
    auto lne = intersection_edges(left_nonself);
    auto rne = intersection_edges(right_nonself);
    int l_only = 0, r_only = 0, ln_only = 0, rn_only = 0;
    for (auto edge : le) l_only += !re.count(edge);
    for (auto edge : re) r_only += !le.count(edge);
    for (auto edge : lne) ln_only += !rne.count(edge);
    for (auto edge : rne) rn_only += !lne.count(edge);
    int split_lr = 0, split_rl = 0, max_lr = 0, max_rl = 0;
    for (const auto& [hub, images] : left_to_right) {
        (void)hub;
        max_lr = std::max(max_lr, static_cast<int>(images.size()));
        split_lr += images.size() != 1;
    }
    for (const auto& [hub, images] : right_to_left) {
        (void)hub;
        max_rl = std::max(max_rl, static_cast<int>(images.size()));
        split_rl += images.size() != 1;
    }
    std::cout << "LR_AUDIT rank=" << rank
              << " roots=" << root_count
              << " L_edges=" << le.size()
              << " R_edges=" << re.size()
              << " L_only=" << l_only
              << " R_only=" << r_only
              << " Ln_edges=" << lne.size()
              << " Rn_edges=" << rne.size()
              << " Ln_only=" << ln_only
              << " Rn_only=" << rn_only
              << " split_L_to_R=" << split_lr
              << " max_L_to_R=" << max_lr
              << " split_R_to_L=" << split_rl
              << " max_R_to_L=" << max_rl << '\n';
}

static std::string reverse_complement_string(const std::string& word) {
    std::string out;
    out.reserve(word.size());
    for (auto it = word.rbegin(); it != word.rend(); ++it)
        out.push_back(*it == '0' ? '1' : '0');
    return out;
}

static std::string eta_string(const std::string& word) {
    if (word.empty()) return {};
    int height = 0, split = -1;
    for (int i = 0; i < static_cast<int>(word.size()); ++i) {
        height += word[i] == '1' ? 1 : -1;
        if (height == 0) { split = i; break; }
    }
    assert(split >= 1);
    const std::string a = word.substr(1, split - 1);
    const std::string b = word.substr(split + 1);
    return a + "01" + eta_string(b);
}

static void dump_support_certificate(const std::string& name,
                                     const std::vector<std::string>& words) {
    assert(!words.empty());
    const int rank = static_cast<int>(words.front().size()) / 2;
    PathFactor base(rank), boundary(rank + 1);
    std::vector<std::map<int,U32>> records;
    for (const std::string& word : words) {
        U32 root = parse(word);
        std::map<int,U32> row;
        for (U32 state : base.states(root))
            row.try_emplace(boundary.owner[U32{1} | (state << 2)], state);
        records.push_back(std::move(row));
    }
    std::vector<int> common;
    for (const auto& [hub, state] : records.front()) {
        (void)state;
        bool all = true;
        for (int i = 1; i < static_cast<int>(records.size()); ++i)
            all &= records[i].count(hub) != 0;
        if (all) common.push_back(hub);
    }
    std::cout << "BASE_CERT name=" << name << " rank=" << rank
              << " support=";
    for (const auto& word : words) std::cout << word << ',';
    std::cout << " common=" << common.size();
    if (!common.empty()) {
        int hub = common.front();
        std::cout << " hub=" << bits(boundary.roots[hub], 2 * (rank + 1))
                  << " states=";
        for (const auto& row : records)
            std::cout << bits(row.at(hub), 2 * rank) << ',';
    }
    std::cout << '\n';

    for (int i = 0; i < static_cast<int>(words.size()); ++i)
        for (int j = i + 1; j < static_cast<int>(words.size()); ++j) {
            U32 ri = parse(words[i]), rj = parse(words[j]);
            bool found_prefix = false;
            int found_hub = -1;
            U32 found_i = 0, found_j = 0;
            for (U32 si : base.states(ri)) {
                if ((si & 1U) == 0) continue;
                int hub = boundary.owner[U32{1} | (si << 2)];
                for (U32 sj : base.states(rj)) {
                    if ((sj & 1U) == 0) continue;
                    if (boundary.owner[U32{1} | (sj << 2)] == hub) {
                        found_prefix = true;
                        found_hub = hub;
                        found_i = si;
                        found_j = sj;
                        break;
                    }
                }
                if (found_prefix) break;
            }
            if (found_prefix)
                std::cout << " PREFIX1_EDGE pair=" << i << ',' << j
                          << " hub="
                          << bits(boundary.roots[found_hub], 2 * (rank + 1))
                          << " states=" << bits(found_i, 2 * rank) << ','
                          << bits(found_j, 2 * rank) << '\n';
        }

    if (common.empty()) {
        std::vector<std::set<int>> all_left(base.roots.size());
        for (int id = 0; id < static_cast<int>(base.roots.size()); ++id)
            for (U32 state : base.states(base.roots[id]))
                all_left[id].insert(
                    boundary.owner[U32{1} | (state << 2)]);
        auto edge_set = intersection_edges(all_left);
        std::vector<std::vector<int>> graph(base.roots.size());
        for (auto [a,b] : edge_set) {
            graph[a].push_back(b);
            graph[b].push_back(a);
        }
        const int source = base.owner[parse(words.front())];
        std::vector<int> parent(base.roots.size(), -2);
        std::vector<int> queue{source};
        parent[source] = -1;
        for (std::size_t head = 0; head < queue.size(); ++head)
            for (int next : graph[queue[head]]) if (parent[next] == -2) {
                parent[next] = queue[head];
                queue.push_back(next);
            }
        for (int wi = 1; wi < static_cast<int>(words.size()); ++wi) {
            int target = base.owner[parse(words[wi])];
            std::vector<int> path;
            for (int at = target; at >= 0; at = parent[at]) path.push_back(at);
            std::reverse(path.begin(), path.end());
            std::cout << " BASE_PATH name=" << name << " target=" << wi
                      << " path=";
            for (int id : path)
                std::cout << bits(base.roots[id], 2 * rank) << ',';
            std::cout << '\n';
            for (int pi = 0; pi + 1 < static_cast<int>(path.size()); ++pi) {
                int a = path[pi], b = path[pi + 1], chosen_hub = -1;
                for (int hub : all_left[a]) if (all_left[b].count(hub)) {
                    chosen_hub = hub;
                    break;
                }
                assert(chosen_hub >= 0);
                U32 sa = 0, sb = 0;
                for (U32 state : base.states(base.roots[a]))
                    if (boundary.owner[U32{1} | (state << 2)] == chosen_hub) {
                        sa = state;
                        break;
                    }
                for (U32 state : base.states(base.roots[b]))
                    if (boundary.owner[U32{1} | (state << 2)] == chosen_hub) {
                        sb = state;
                        break;
                    }
                std::cout << "  BASE_EDGE hub="
                          << bits(boundary.roots[chosen_hub], 2 * (rank + 1))
                          << " states=" << bits(sa, 2 * rank) << ','
                          << bits(sb, 2 * rank) << '\n';
            }
        }
    }
}

static void generate_dyck_strings(int rank, int position, int up, int down,
                                  std::string& word,
                                  std::vector<std::string>& out) {
    if (position == 2 * rank) {
        out.push_back(word);
        return;
    }
    if (up < rank) {
        word.push_back('1');
        generate_dyck_strings(rank, position + 1, up + 1, down, word, out);
        word.pop_back();
    }
    if (down < up) {
        word.push_back('0');
        generate_dyck_strings(rank, position + 1, up, down + 1, word, out);
        word.pop_back();
    }
}

static bool check_hub_certificate(const std::vector<std::string>& roots,
                                  const std::vector<std::string>& states,
                                  const std::string& hub) {
    assert(roots.size() == states.size() && !roots.empty());
    const int rank = static_cast<int>(roots.front().size()) / 2;
    PathFactor base(rank), boundary(rank + 1);
    const int hub_id = boundary.owner[parse(hub)];
    if (hub_id < 0 || boundary.roots[hub_id] != parse(hub)) return false;
    for (int i = 0; i < static_cast<int>(roots.size()); ++i) {
        const int root_id = base.owner[parse(roots[i])];
        if (root_id < 0 || base.roots[root_id] != parse(roots[i])) return false;
        if (base.owner[parse(states[i])] != root_id) return false;
        if (boundary.owner[U32{1} | (parse(states[i]) << 2)] != hub_id)
            return false;
    }
    return true;
}

static void dump_base_certificates(int max_alpha_rank) {
    for (int t = 0; t <= max_alpha_rank; ++t) {
        std::vector<std::string> dyck;
        std::string scratch;
        generate_dyck_strings(t, 0, 0, 0, scratch, dyck);
        for (const std::string& w : dyck) {
            std::vector<std::string> alpha{
                "1" + w + "11000", "1" + w + "10100",
                "1" + w + "10010"};
            dump_support_certificate("alpha(" + w + ")", alpha);
            const std::vector<std::string> alpha_states{
                "1" + w + "01101", "1" + w + "10101",
                "0" + std::string(w.size(), '0') + "01111"};
            std::string corrected_third = "0";
            for (char bit : w) corrected_third.push_back(bit == '0' ? '1' : '0');
            corrected_third += "01111";
            auto corrected_alpha_states = alpha_states;
            corrected_alpha_states[2] = corrected_third;
            const std::string alpha_hub = "111" + w + "10000";
            const bool alpha_ok = check_hub_certificate(
                alpha, corrected_alpha_states, alpha_hub);
            const std::string eta = eta_string(w);
            const std::string r = "111" + reverse_complement_string(eta)
                                  + "000";
            const std::string q1 = "1001" + reverse_complement_string(w)
                                   + "01";
            const std::string q2 = "1010" + reverse_complement_string(w)
                                   + "01";
            PathFactor internal(static_cast<int>(r.size()) / 2);
            auto states = internal.states(parse(r));
            int i1 = -1, i2 = -1;
            for (int i = 0; i < static_cast<int>(states.size()); ++i) {
                if (states[i] == parse(q1)) i1 = i;
                if (states[i] == parse(q2)) i2 = i;
            }
            std::cout << " ALPHA_INTERNAL w=" << w << " eta=" << eta
                      << " R=" << r << " q1_index=" << i1
                      << " q2_index=" << i2
                      << " direct_cert=" << alpha_ok << '\n';
            for (std::string& x : alpha) x = reverse_complement_string(x);
            dump_support_certificate("mirror_alpha(" + w + ")", alpha);

            const std::string tword = reverse_complement_string(w);
            const std::string bart = [&] {
                std::string value;
                for (char bit : tword) value.push_back(bit == '0' ? '1' : '0');
                return value;
            }();
            const std::string A = "10110" + tword + "0";
            const std::string B = "11010" + tword + "0";
            const std::string C = "11100" + tword + "0";
            const bool mirror_ab = check_hub_certificate(
                {A,B}, {"01101" + bart + "1", "11001" + bart + "1"},
                "1110010" + tword + "0");
            const bool mirror_ac = check_hub_certificate(
                {A,C}, {"01110" + bart + "1", "11100" + bart + "1"},
                "1110100" + tword + "0");
            const bool mirror_bc = check_hub_certificate(
                {B,C}, {"11010" + bart + "1", "10110" + bart + "1"},
                "1111000" + tword + "0");
            std::cout << " MIRROR_ALPHA_DIRECT w=" << w
                      << " AB=" << mirror_ab << " AC=" << mirror_ac
                      << " BC=" << mirror_bc << '\n';
        }
    }
    const std::vector<std::pair<std::string,std::vector<std::string>>> fixed{
        {"beta", {"111000", "101100", "101010"}},
        {"gamma", {"11001100", "11011000", "11101000"}},
        {"delta", {"111000", "110100", "101100", "101010"}}};
    for (const auto& [name, support] : fixed) {
        dump_support_certificate(name, support);
        auto mirrored = support;
        for (std::string& x : mirrored) x = reverse_complement_string(x);
        dump_support_certificate("mirror_" + name, mirrored);
    }
    const std::vector<std::pair<std::string,std::vector<std::string>>> edges{
        {"delta_tail", {"101100", "110100"}},
        {"mirror_beta_left", {"101010", "110010"}},
        {"mirror_beta_right", {"110010", "111000"}},
        {"mirror_gamma_left", {"11001100", "11100100"}},
        {"mirror_gamma_right", {"11001100", "11101000"}},
        {"mirror_delta_tail", {"110010", "110100", "111000"}}};
    for (const auto& [name, support] : edges)
        dump_support_certificate(name, support);
}

int main(int argc, char** argv) {
    const int s = argc > 1 ? std::stoi(argv[1]) : 3;
    const std::string context = argc > 2 ? argv[2] : "10";
    if (context == "lr_audit") {
        audit_left_right(s);
        return 0;
    }
    if (context == "base_certs") {
        dump_base_certificates(s);
        return 0;
    }
    if (context == "edgewrap") {
        dump_wrap_edges(s);
        return 0;
    }
    const bool wrap = context == "wrap";
    const bool tail01 = context == "tail01";
    const int t = wrap ? 1 : (tail01 ? 0 : static_cast<int>(context.size()) / 2);
    assert(wrap || tail01 || context.size() % 2 == 0);
    assert(s + t + 1 <= 14);

    PathFactor low(s + 1), high(s + t + 1);
    const U32 u = (wrap || tail01) ? 0 : parse(context);
    const U32 context_mask = (U32{1} << (2 * t)) - 1;
    const U32 complement_u = context_mask ^ u;

    std::map<int, std::set<int>> image;
    for (U32 z = 0; z < (U32{1} << (2 * s)); ++z) {
        const int weight = __builtin_popcount(z);
        if (weight != s && weight != s + 1) continue;
        const U32 capped = U32{1} | (z << 2);
        U32 contextual = 0;
        if (tail01) {
            contextual = z | (U32{1} << (2 * s + 1));
        } else if (wrap) {
            U32 reverse_complement = 0;
            for (int p = 0; p < 2 * s; ++p)
                if (((z >> (2 * s - 1 - p)) & 1U) == 0)
                    reverse_complement |= U32{1} << p;
            // The word is 10 . 1 . rev(z) . 1 in left-to-right bit order.
            contextual = U32{1} | (U32{1} << 2)
                         | (reverse_complement << 3)
                         | (U32{1} << (2 * s + 3));
        } else {
            contextual = U32{1} | (complement_u << 2)
                         | (z << (2 + 2 * t));
        }
        int before = low.owner[capped];
        int after = high.owner[contextual];
        assert(before >= 0 && after >= 0);
        image[before].insert(after);
    }

    int bad = 0;
    std::cout << "CONTEXT_MAP s=" << s << " U=" << context
              << " low_roots=" << low.roots.size() << '\n';
    for (const auto& [before, afters] : image) {
        if (afters.size() != 1) ++bad;
        std::cout << " root=" << bits(low.roots[before], 2 * (s + 1))
                  << " images=";
        for (int after : afters)
            std::cout << bits(high.roots[after], 2 * (s + t + 1)) << ',';
        std::cout << '\n';
    }
    std::cout << "SUMMARY bad=" << bad << '/' << image.size() << '\n';
    return bad == 0 ? 0 : 1;
}
