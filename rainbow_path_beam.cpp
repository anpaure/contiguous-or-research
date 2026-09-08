#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;

struct Eval {
    int deficit = 0, covered = 0, lower = 0, upper = 0;
    int rank_below_possible = 0, potential = 0;
    int focus = 0;
    int singleton_matching = 0;
    int hall_matching = 0;
};
struct State { vector<uint16_t> path; Eval eval; uint64_t hash = 0; };
static int K, RANK, D, FULL;
static int MIN_COLORS;
static string MODE = "normal";
static vector<uint8_t> FOCUS;

static uint64_t hash_path(const vector<uint16_t>& path) {
    uint64_t value = 0xcbf29ce484222325ULL;
    for (int x : path) value = (value ^ x) * 0x100000001b3ULL;
    return value;
}

static bool valid(const vector<uint16_t>& path) {
    vector<uint8_t> color(1 << K);
    int distinct = 0;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2) return false;
        const int edge = path[i] & path[i + 1];
        if (!color[edge]) {
            color[edge] = 1;
            ++distinct;
        }
    }
    return distinct >= MIN_COLORS;
}

static Eval evaluate(const vector<uint16_t>& path) {
    Eval result;
    for (int bit = 0; bit < K; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                result.deficit += max(0, D + 1 - (i - first));
        }
    }
    vector<uint8_t> count(1 << K);
    auto record = [&] (int value, int wanted) {
        if (popcount(static_cast<unsigned>(value)) != wanted) return;
        if (!count[value]) {
            ++result.covered;
            if (wanted < RANK) ++result.lower;
            if (wanted > RANK) ++result.upper;
            if (wanted > RANK && FOCUS[value]) result.focus += FOCUS[value];
        }
        if (count[value] != 255) ++count[value];
    };
    for (int value : path) record(value, RANK);
    for (int length = 2; length <= D + 1; ++length)
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = FULL;
            for (int j = left; j < left + length; ++j) value &= path[j];
            record(value, RANK - length + 1);
        }
    for (int length = 2; RANK + length - 1 <= K; ++length)
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            record(value, RANK + length - 1);
        }
    for (int mask = 1; mask <= FULL; ++mask) if (count[mask]) {
        int reward = 1024;
        for (int bonus = 256, occurrence = 1;
             bonus && occurrence < count[mask]; bonus >>= 1, ++occurrence)
            reward += bonus;
        result.potential += reward;
    }
    for (int mask = 1; mask <= FULL; ++mask) {
        if (popcount(static_cast<unsigned>(mask)) != RANK - 1) continue;
        if (count[mask] || !(mask & ~path.front()) || !(mask & ~path.back()))
            ++result.rank_below_possible;
    }

    // Necessary singleton-labelability test for a factor D^D A = path.
    // A bit is forced at a position if some positive central window has that
    // position as its unique legal pin.  Position j can carry singleton {b}
    // only if b is allowed there and no other bit is forced there.  A maximum
    // bipartite matching then measures how many distinct singleton entries can
    // coexist.  This exactly exposes the first obstruction in the k=12 lift.
    const int n=path.size()+D;
    vector<int> envelope(n,FULL),forced(n);
    for(int position=0;position<n;++position)
        for(int i=max(0,position-D);i<=min((int)path.size()-1,position);++i)
            envelope[position]&=path[i];
    for(int bit=0;bit<K;++bit) for(int i=0;i<(int)path.size();++i)
        if(path[i]&(1<<bit)) {
            int only=-1,count_allowed=0;
            for(int position=i;position<=i+D;++position)
                if(envelope[position]&(1<<bit)){only=position;++count_allowed;}
            if(count_allowed==1)forced[only]|=1<<bit;
        }
    vector<vector<int>> singleton_candidate(K);
    for(int bit=0;bit<K;++bit) for(int position=0;position<n;++position)
        if((envelope[position]&(1<<bit))&&!(forced[position]&~(1<<bit)))
            singleton_candidate[bit].push_back(position);
    vector<int> owner(n,-1);
    auto augment=[&](auto&&self,int bit,vector<uint8_t>&seen)->bool {
        for(int position:singleton_candidate[bit])if(!seen[position]){
            seen[position]=1;
            if(owner[position]<0||self(self,owner[position],seen)){
                owner[position]=bit;return true;
            }
        }
        return false;
    };
    for(int bit=0;bit<K;++bit){vector<uint8_t>seen(n);
        result.singleton_matching+=augment(augment,bit,seen);}
    if(K==12&&D==2) {
        const vector<int> hall_masks{
            800,801,802,804,816,896,897,900,904,912,928,960,
            1824,1920,2848,2944
        };
        vector<int> hall_owner(n,-1);
        auto hall_augment=[&](auto&&self,int index,vector<uint8_t>&seen)->bool {
            const int target=hall_masks[index];
            for(int position=0;position<n;++position) {
                if(seen[position]||(target&~envelope[position])||
                   (forced[position]&~target))continue;
                seen[position]=1;
                if(hall_owner[position]<0||self(self,hall_owner[position],seen)){
                    hall_owner[position]=index;return true;
                }
            }
            return false;
        };
        for(int index=0;index<(int)hall_masks.size();++index){vector<uint8_t>seen(n);
            result.hall_matching+=hall_augment(hall_augment,index,seen);}
    }
    return result;
}

static bool better(const State& a, const State& b) {
    if (a.eval.deficit != b.eval.deficit) return a.eval.deficit < b.eval.deficit;
    if (MODE == "upper" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (MODE == "lower" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "label" &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if (MODE == "label" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "bridge" &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if (MODE == "bridge" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (MODE == "bridge" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "complete" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "complete" &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if (MODE == "complete" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (MODE == "complete" && a.eval.focus != b.eval.focus)
        return a.eval.focus > b.eval.focus;
    if (MODE == "rotate" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "rotate" &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if (MODE == "rotate" && a.eval.focus != b.eval.focus)
        return a.eval.focus > b.eval.focus;
    if (MODE == "rotate" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (MODE == "labeling" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (MODE == "labeling" &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if (MODE == "labeling" &&
        a.eval.singleton_matching != b.eval.singleton_matching)
        return a.eval.singleton_matching > b.eval.singleton_matching;
    if (MODE == "labeling" && a.eval.hall_matching != b.eval.hall_matching)
        return a.eval.hall_matching > b.eval.hall_matching;
    if (MODE == "labeling" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if ((MODE == "labelrotate"||MODE=="keep3258") && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if ((MODE == "labelrotate"||MODE=="keep3258") &&
        a.eval.rank_below_possible != b.eval.rank_below_possible)
        return a.eval.rank_below_possible > b.eval.rank_below_possible;
    if ((MODE == "labelrotate"||MODE=="keep3258") &&
        a.eval.singleton_matching != b.eval.singleton_matching)
        return a.eval.singleton_matching > b.eval.singleton_matching;
    if ((MODE == "labelrotate"||MODE=="keep3258") &&
        a.eval.hall_matching != b.eval.hall_matching)
        return a.eval.hall_matching > b.eval.hall_matching;
    if ((MODE == "labelrotate"||MODE=="keep3258") && a.eval.focus != b.eval.focus)
        return a.eval.focus > b.eval.focus;
    if ((MODE == "labelrotate"||MODE=="keep3258") && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (a.eval.covered != b.eval.covered) return a.eval.covered > b.eval.covered;
    return a.eval.potential > b.eval.potential;
}

static void save(const State& state, const string& output_path) {
    ofstream output(output_path);
    for (int x : state.path) output << x << ' ';
    output << '\n';
}

int main(int argc, char** argv) {
    if (argc < 9) return 2;
    const string input_path = argv[1], output_path = argv[2];
    const int beam_size = stoi(argv[3]), maximum_depth = stoi(argv[4]);
    K = stoi(argv[5]); RANK = stoi(argv[6]); D = stoi(argv[7]);
    const int allowed_increase = stoi(argv[8]);
    MIN_COLORS = argc > 9 ? stoi(argv[9]) : 0;
    MODE = argc > 10 ? argv[10] : "normal";
    FULL = (1 << K) - 1;
    ifstream input(input_path);
    State initial;
    for (int value; input >> value;) initial.path.push_back(value);
    if (!MIN_COLORS) MIN_COLORS = initial.path.size() - 1;
    if (!valid(initial.path)) return 3;
    FOCUS.assign(1 << K, 0);
    for (int mask = 1; mask <= FULL; ++mask)
        if (popcount(static_cast<unsigned>(mask)) > RANK)
            FOCUS[mask] = 1 << min(7,
                popcount(static_cast<unsigned>(mask)) - RANK - 1);
    for (int length = 2; RANK + length - 1 <= K; ++length)
        for (int left = 0; left + length <= static_cast<int>(initial.path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= initial.path[j];
            if (popcount(static_cast<unsigned>(value)) == RANK + length - 1)
                FOCUS[value] = 0;
        }
    if(MODE=="keep3258"&&K==12)FOCUS[3258]=128;
    initial.eval = evaluate(initial.path);
    const int initial_deficit = initial.eval.deficit;
    initial.hash = hash_path(initial.path);
    State best = initial;
    vector<State> beam{initial};
    unordered_set<uint64_t> visited;
    visited.reserve(static_cast<size_t>(beam_size) * maximum_depth * 4);
    visited.insert(initial.hash);
    cerr << "initial deficit=" << best.eval.deficit << " covered=" << best.eval.covered << '\n';
    for (int depth = 1; depth <= maximum_depth; ++depth) {
        const size_t visited_limit=static_cast<size_t>(beam_size)*50000;
        if(visited.size()>visited_limit) {
            visited.clear();
            for(const State& state:beam) visited.insert(state.hash);
        }
        vector<State> next;
        next.reserve(static_cast<size_t>(beam.size()) * 120);
        for (const State& state : beam) {
            const int n = state.path.size();
            auto consider = [&] (State candidate) {
                candidate.hash = hash_path(candidate.path);
                if (!visited.insert(candidate.hash).second || !valid(candidate.path))
                    return false;
                candidate.eval = evaluate(candidate.path);
                if (candidate.eval.deficit > best.eval.deficit + allowed_increase)
                    return false;
                if (better(candidate, best)) {
                    best = candidate;
                    cerr << "depth=" << depth << " best deficit=" << best.eval.deficit
                         << " covered=" << best.eval.covered
                         << " lower=" << best.eval.lower
                         << " upper=" << best.eval.upper
                         << " possible5=" << best.eval.rank_below_possible
                         << " singleton=" << best.eval.singleton_matching
                         << " hall=" << best.eval.hall_matching
                         << " focus=" << best.eval.focus
                         << " potential=" << best.eval.potential << '\n';
                    save(best, output_path);
                }
                next.push_back(move(candidate));
                return false;
            };
            for (int left = 0; left < n; ++left) {
                for (int right = left + 2; right < n; ++right) {
                    if (left && popcount(static_cast<unsigned>(
                            state.path[left - 1] ^ state.path[right])) != 2) continue;
                    if (right + 1 < n && popcount(static_cast<unsigned>(
                            state.path[left] ^ state.path[right + 1])) != 2) continue;
                    State candidate;
                    candidate.path = state.path;
                    reverse(candidate.path.begin() + left,
                            candidate.path.begin() + right + 1);
                    if (consider(move(candidate))) return 0;
                }
            }

            // Or-opt relocations change three path edges rather than the two
            // changed by a reversal.  They connect components of the valid
            // rainbow-path state space that 2-opt alone cannot reach.  Use
            // Johnson neighbors of the oriented block's first vertex to find
            // candidate insertion gaps without an O(n^2) gap scan.
            if(K<=12) {
            vector<int> position(1 << K, -1);
            for (int i = 0; i < n; ++i) position[state.path[i]] = i;
            for (int length = 1; length <= 4; ++length)
                for (int left = 0, right = length - 1; right < n;
                     ++left, ++right) {
                    if (left && right + 1 < n && popcount(static_cast<unsigned>(
                            state.path[left - 1] ^ state.path[right + 1])) != 2)
                        continue;
                    vector<uint16_t> reduced;
                    reduced.reserve(n - length);
                    reduced.insert(reduced.end(), state.path.begin(),
                                   state.path.begin() + left);
                    reduced.insert(reduced.end(), state.path.begin() + right + 1,
                                   state.path.end());
                    for (int reversed = 0; reversed < 2; ++reversed) {
                        const int first = reversed ? state.path[right] : state.path[left];
                        const int last = reversed ? state.path[left] : state.path[right];
                        auto emit = [&] (int gap) {
                            State candidate;
                            candidate.path = reduced;
                            vector<uint16_t> block(state.path.begin() + left,
                                                   state.path.begin() + right + 1);
                            if (reversed) reverse(block.begin(), block.end());
                            candidate.path.insert(candidate.path.begin() + gap,
                                                  block.begin(), block.end());
                            return consider(move(candidate));
                        };
                        if (left && popcount(static_cast<unsigned>(last ^ reduced.front())) == 2)
                            if (emit(0)) return 0;
                        if (right + 1 < n &&
                            popcount(static_cast<unsigned>(first ^ reduced.back())) == 2)
                            if (emit(reduced.size())) return 0;
                        for (int removed = 0; removed < K; ++removed)
                            if (first & (1 << removed))
                                for (int added = 0; added < K; ++added)
                                    if (!(first & (1 << added))) {
                                        const int neighbor = first ^ (1 << removed) ^ (1 << added);
                                        const int gap_left = position[neighbor];
                                        if (gap_left < 0 || gap_left >= n - 1 ||
                                            (gap_left >= left - 1 && gap_left <= right))
                                            continue;
                                        const int gap_right = gap_left + 1;
                                        if (gap_right >= left && gap_right <= right) continue;
                                        if (popcount(static_cast<unsigned>(
                                                last ^ state.path[gap_right])) != 2)
                                            continue;
                                        const int gap = gap_left < left
                                            ? gap_left + 1 : gap_left - length + 1;
                                        if (emit(gap)) return 0;
                                    }
                    }
                }
            }
        }
        if (next.empty()) break;
        if (static_cast<int>(next.size()) > beam_size) {
            nth_element(next.begin(), next.begin() + beam_size, next.end(), better);
            next.resize(beam_size);
        }
        sort(next.begin(), next.end(), better);
        beam.swap(next);
        cerr << "layer=" << depth << " states=" << beam.size()
             << " front=" << beam.front().eval.deficit << ','
             << beam.front().eval.covered << ',' << beam.front().eval.lower
             << ',' << beam.front().eval.upper << ','
             << beam.front().eval.rank_below_possible
             << " visited=" << visited.size() << '\n';
    }
    save(best, output_path);
    cerr << "NONE deficit=" << best.eval.deficit << " covered=" << best.eval.covered << '\n';
    return 1;
}
