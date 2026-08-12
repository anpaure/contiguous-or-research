#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <chrono>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;

static int erase_bit(int x, int bit) {
    return (x & ((1 << bit) - 1)) | ((x >> (bit + 1)) << bit);
}
static bool edge(int x, int y) {
    return popcount(static_cast<unsigned>(x ^ y)) == 2;
}

struct Block { vector<int> value; };

static int endpoint(const Block& b, int orientation, bool last) {
    // orientation 0 emits front->back, orientation 1 emits back->front.
    return b.value[orientation != last ? b.value.size() - 1 : 0];
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: repair_k12_section_blocks K12_PATH BIT [OUT] [SECONDS] [SEED]\n";
        return 2;
    }
    ifstream in(argv[1]);
    vector<int> source;
    for (int x; in >> x;) source.push_back(x);
    const int bit = stoi(argv[2]);
    vector<int> path;
    for (int x : source) if (!(x & (1 << bit))) path.push_back(erase_bit(x, bit));
    if (path.size() != 462) return 2;

    vector<Block> blocks(1);
    blocks.back().value.push_back(path.front());
    for (int i = 1; i < static_cast<int>(path.size()); ++i) {
        if (!edge(path[i - 1], path[i])) blocks.push_back({});
        blocks.back().value.push_back(path[i]);
    }
    const int n = blocks.size();
    cerr << "blocks=" << n << " lengths";
    for (const auto& b : blocks) cerr << ' ' << b.value.size();
    cerr << '\n';

    vector<vector<vector<pair<int,int>>>> next(n, vector<vector<pair<int,int>>>(2));
    for (int a = 0; a < n; ++a) for (int oa = 0; oa < 2; ++oa)
        for (int b = 0; b < n; ++b) if (b != a) for (int ob = 0; ob < 2; ++ob)
            if (edge(endpoint(blocks[a], oa, true), endpoint(blocks[b], ob, false)))
                next[a][oa].push_back({b, ob});
    for (int a = 0; a < n; ++a)
        cerr << "block=" << a << " endpoint-degrees=" << next[a][0].size()
             << ',' << next[a][1].size() << '\n';

    mt19937_64 rng(argc > 5 ? stoull(argv[5]) : 120011ULL);
    const double seconds = argc > 4 ? stod(argv[4]) : 5.0;
    const auto deadline = chrono::steady_clock::now() + chrono::duration<double>(seconds);
    vector<pair<int,int>> answer, stack;
    vector<unsigned char> used(n);
    uint64_t nodes = 0;

    auto dfs = [&](auto&& self, int a, int oa) -> bool {
        ++nodes;
        if (stack.size() == blocks.size()) { answer = stack; return true; }
        if ((nodes & 65535) == 0 && chrono::steady_clock::now() >= deadline) return false;
        vector<pair<pair<int,uint64_t>,pair<int,int>>> choice;
        for (auto [b, ob] : next[a][oa]) if (!used[b]) {
            int onward = 0;
            for (auto [c, oc] : next[b][ob]) if (!used[c]) ++onward;
            choice.push_back({{onward, rng()}, {b, ob}});
        }
        sort(choice.begin(), choice.end());
        for (auto item : choice) {
            auto [b, ob] = item.second;
            used[b] = 1; stack.push_back({b, ob});
            if (self(self, b, ob)) return true;
            stack.pop_back(); used[b] = 0;
        }
        return false;
    };

    vector<pair<int,int>> starts;
    for (int i = 0; i < n; ++i) for (int o = 0; o < 2; ++o) starts.push_back({i,o});
    shuffle(starts.begin(), starts.end(), rng);
    for (auto [s,o] : starts) {
        fill(used.begin(), used.end(), 0); stack.clear();
        used[s] = 1; stack.push_back({s,o});
        if (dfs(dfs, s, o)) break;
        if (chrono::steady_clock::now() >= deadline) break;
    }
    cerr << "nodes=" << nodes << " found=" << !answer.empty() << '\n';
    if (answer.empty()) return 1;

    vector<int> result;
    for (auto [b,o] : answer) {
        if (!o) result.insert(result.end(), blocks[b].value.begin(), blocks[b].value.end());
        else result.insert(result.end(), blocks[b].value.rbegin(), blocks[b].value.rend());
    }
    ofstream out(argc > 3 ? argv[3] : "k11_k12_block_repair.txt");
    for (int x : result) out << x << ' ';
    out << '\n';
    cerr << "order";
    for (auto [b,o] : answer) cerr << ' ' << b << (o ? '-' : '+');
    cerr << '\n';
}
