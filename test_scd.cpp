#include <algorithm>
#include <bit>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

static string replace_stars(string s, bool first) {
    vector<int> at;
    for (int i = 0; i < static_cast<int>(s.size()); ++i)
        if (s[i] == '*') at.push_back(i);
    const int i = first ? at[0] : at[at.size() - 2];
    const int j = first ? at[1] : at.back();
    s[i] = '0';
    s[j] = '1';
    return s;
}

static vector<string> lambda(int n) {
    vector<string> chains{n & 1 ? "*" : ""};
    for (int d = n & 1; d < n; d += 2) {
        vector<string> next;
        for (const string& c : chains) {
            string outer = "*" + c + "*";
            vector<string> descendants;
            const int stars = count(c.begin(), c.end(), '*');
            if ((d & 1) == 0) {
                if (stars >= 2) {
                    string f = replace_stars(outer, true);
                    string ell = replace_stars(outer, false);
                    descendants = {outer, f, replace_stars(f, false), ell};
                } else {
                    descendants = {outer, "0" + c + "1"};
                }
            } else {
                string f = replace_stars(outer, true);
                string ell = replace_stars(outer, false);
                if (stars >= 3)
                    descendants = {outer, ell, replace_stars(ell, true), f};
                else
                    descendants = {outer, ell, f};
            }
            if (stars % 4 != d % 4) reverse(descendants.begin(), descendants.end());
            next.insert(next.end(), descendants.begin(), descendants.end());
        }
        chains.swap(next);
    }
    return chains;
}

static int mask_of(const string& c, bool top) {
    int mask = 0;
    for (int i = 0; i < static_cast<int>(c.size()); ++i)
        if (c[i] == '1' || (top && c[i] == '*')) mask |= 1 << i;
    return mask;
}

static int score(int k, const vector<int>& a) {
    vector<char> seen(1 << k);
    vector<int> prev;
    int result = 0;
    for (int v : a) {
        vector<int> cur{v};
        for (int x : prev) {
            x |= v;
            if (x != cur.back()) cur.push_back(x);
        }
        for (int x : cur) if (!seen[x]) seen[x] = 1, ++result;
        prev.swap(cur);
    }
    return result;
}

static vector<int> requests_for_order(int k, const vector<int>& order, int first_block) {
    vector<int> blocks{first_block, order[0] ^ first_block};
    vector<int> a{order[0] ^ first_block, first_block};
    int present = order[0];
    for (int oi = 1; oi < static_cast<int>(order.size()); ++oi) {
        const int target = order[oi];
        int request = target & ~present;
        bool barrier = false;
        for (int block : blocks) {
            if (block & ~target) barrier = true;
            if (barrier) request |= block & target;
        }
        if (!request) request = target;
        a.push_back(request);
        vector<int> next{request};
        for (int block : blocks) if ((block &= ~request)) next.push_back(block);
        blocks.swap(next);
        present |= request;
    }
    return a;
}

static vector<int> coollex(int n, int r) {
    string s(r, '1');
    s += string(n - r, '0');
    const string initial = s;
    vector<int> result;
    do {
        int mask = 0;
        for (int i = 0; i < n; ++i) if (s[i] == '1') mask |= 1 << i;
        result.push_back(mask);
        int length = n;
        for (int i = 2; i < n; ++i) {
            if (s[i - 2] == '0' && s[i - 1] == '1' &&
                (s[i] == '0' || s[i] == '1')) {
                length = i + 1;
                break;
            }
        }
        rotate(s.begin(), s.begin() + length - 1, s.begin() + length);
    } while (s != initial);
    return result;
}

static pair<int, vector<int>> best_cyclic_order(int k, vector<int> order) {
    pair<int, vector<int>> best;
    for (int direction = 0; direction < 2; ++direction) {
        for (int shift = 0; shift < static_cast<int>(order.size()); ++shift) {
            rotate(order.begin(), order.begin() + 1, order.end());
            const int first = order[0];
            for (int block = first; block; block = (block - 1) & first) {
                if (block == first) continue;
                auto a = requests_for_order(k, order, block);
                int s = score(k, a);
                if (s > best.first) best = {s, std::move(a)};
            }
        }
        reverse(order.begin(), order.end());
    }
    return best;
}

static vector<int> stepping(int n) {
    if (n <= 1) return {};
    if (n == 2) return {1};
    vector<int> small = stepping(n - 1), result;
    for (int x : small) result.push_back(x + 1);
    for (int x = 1; x < n; ++x) result.push_back(x);
    result.insert(result.end(), small.begin(), small.end());
    return result;
}

static vector<int> stepping_rank_order(int n, int r) {
    vector<int> permutation(n);
    for (int i = 0; i < n; ++i) permutation[i] = i;
    auto current = [&] {
        int mask = 0;
        for (int i = 0; i < r; ++i) mask |= 1 << permutation[i];
        return mask;
    };
    vector<int> order{current()};
    for (int move : stepping(n)) {
        swap(permutation[move - 1], permutation[move]);
        if (move == r) order.push_back(current());
    }
    return order;
}

static int sampled_nested_coverage(int n, int r) {
    vector<int> p(n);
    iota(p.begin(), p.end(), 0);
    vector<char> seen(1 << n);
    auto sample = [&] {
        int mask = 0;
        for (int x : p) mask |= 1 << x, seen[mask] = 1;
    };
    sample();
    for (int move : stepping(n)) {
        swap(p[move - 1], p[move]);
        if (move == r) sample();
    }
    return count(seen.begin(), seen.end(), char(1));
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 6;
    const auto chains = lambda(k);
    cerr << "chains=" << chains.size() << '\n';
    cerr << "central:";
    vector<int> central;
    for (const string& c : chains) {
        int need = k / 2;
        int mask = 0;
        for (int i = 0; i < k; ++i) {
            if (c[i] == '1') mask |= 1 << i, --need;
        }
        for (int i = 0; i < k && need; ++i) if (c[i] == '*')
            mask |= 1 << i, --need;
        central.push_back(mask);
        cerr << ' ' << mask;
    }
    cerr << '\n';
    int middle_best = 0;
    vector<int> middle_array;
    for (int block = central[0]; block; block = (block - 1) & central[0]) {
        if (block == central[0]) continue;
        auto a = requests_for_order(k, central, block);
        int s = score(k, a);
        if (s > middle_best) middle_best = s, middle_array = std::move(a);
    }
    cerr << "central-order requests score=" << middle_best << " length="
         << middle_array.size() << ':';
    for (int x : middle_array) cerr << ' ' << x;
    cerr << '\n';
    const auto cool = coollex(k, k / 2);
    int cool_best = 0;
    for (int block = cool[0]; block; block = (block - 1) & cool[0]) {
        if (block == cool[0]) continue;
        cool_best = max(cool_best, score(k, requests_for_order(k, cool, block)));
    }
    cerr << "coollex size=" << cool.size() << " score=" << cool_best << " order:";
    for (int x : cool) cerr << ' ' << x;
    cerr << '\n';
    auto lambda_cycle = best_cyclic_order(k, central);
    auto cool_cycle = best_cyclic_order(k, cool);
    cerr << "best lambda rotation=" << lambda_cycle.first << " cool rotation="
         << cool_cycle.first << '\n';
    const auto nested = stepping_rank_order(k, k / 2);
    auto nested_cycle = best_cyclic_order(k, nested);
    cerr << "nested rank order size=" << nested.size() << " score="
         << nested_cycle.first << " order:";
    for (int x : nested) cerr << ' ' << x;
    cerr << '\n';
    cerr << "sampled nested chains cover=" << sampled_nested_coverage(k, k / 2)
         << '/' << ((1 << k) - 1) << '\n';
    if (k == 6) {
        vector<int> adjacent = {7,11,19,35,37,21,13,14,22,38,
                                42,50,49,41,25,26,28,44,52,56};
        auto adjacent_cycle = best_cyclic_order(k, adjacent);
        cerr << "best adjacent-interchange rotation=" << adjacent_cycle.first << ':';
        for (int x : adjacent_cycle.second) cerr << ' ' << x;
        cerr << '\n';
    }
    for (int mode = 0; mode < 12; ++mode) {
        vector<int> a;
        if (mode < 6) {
            for (int b = 0; b < k; ++b) a.push_back(1 << b);
        } else {
            for (int b = k - 1; b >= 0; --b) a.push_back(1 << b);
        }
        int previous_bottom = 0, previous_top = 0;
        for (const string& c : chains) {
            int bottom = mask_of(c, false), top = mask_of(c, true), request = 0;
            const int rule = mode % 6;
            if (rule == 0) request = bottom;
            if (rule == 1) request = top;
            if (rule == 2) request = bottom & ~previous_bottom;
            if (rule == 3) request = top & ~previous_top;
            if (rule == 4) request = bottom ^ previous_bottom;
            if (rule == 5) request = top ^ previous_top;
            if (request) a.push_back(request);
            previous_bottom = bottom;
            previous_top = top;
        }
        cout << mode << " length=" << a.size() << " score=" << score(k, a) << '\n';
    }
    if (k <= 6) for (const auto& c : chains) cout << c << '\n';
}
