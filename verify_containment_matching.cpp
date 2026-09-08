#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <bit>
#include <fstream>
#include <iostream>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

struct Record { int target, type, index, recorded; };

int main(int argc, char** argv) {
    if (argc != 5) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    const int limit = 1 << k, full = limit - 1;
    ifstream path_input(argv[3]), matching_input(argv[4]);
    vector<int> central;
    for (int value; path_input >> value;) central.push_back(value);
    vector<Record> records;
    for (Record record; matching_input >> record.target >> record.type >> record.index >> record.recorded;)
        records.push_back(record);
    if (central.empty()) return 3;
    const int rank = popcount(static_cast<unsigned>(central.front()));
    const int n = central.size() + d;
    vector<int> envelope(n, full);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d); i <= min<int>(central.size() - 1, position); ++i)
            envelope[position] &= central[i];

    vector<char> target_seen(limit);
    set<pair<int, int>> slots;
    vector<int> forbidden(n);
    int bad_target = 0, duplicate_target = 0, duplicate_slot = 0,
        bad_recorded = 0, bad_containment = 0, bad_position_nonzero = 0;
    for (const Record& record : records) {
        bad_target += record.target <= 0 || record.target >= limit ||
                      popcount(static_cast<unsigned>(record.target)) >= rank;
        if (record.target > 0 && record.target < limit) {
            duplicate_target += target_seen[record.target];
            target_seen[record.target] = true;
        }
        duplicate_slot += !slots.insert({record.type, record.index}).second;
        const int length = record.type + 1;
        if (record.type < 0 || record.type > 1 || record.index < 0 ||
            record.index + length > n) {
            ++bad_recorded; continue;
        }
        int allowed = 0;
        bool each_position = true;
        for (int p = record.index; p < record.index + length; ++p) {
            allowed |= envelope[p];
            each_position &= (record.target & envelope[p]) != 0;
            forbidden[p] |= full & ~record.target;
        }
        bad_recorded += allowed != record.recorded;
        bad_containment += (record.target & ~allowed) != 0;
        bad_position_nonzero += !each_position;
    }
    int missing_targets = 0;
    for (int target = 1; target < limit; ++target)
        if (popcount(static_cast<unsigned>(target)) < rank && !target_seen[target])
            ++missing_targets;
    vector<int> legal(n);
    int empty_positions = 0;
    for (int p = 0; p < n; ++p) {
        legal[p] = envelope[p] & ~forbidden[p];
        empty_positions += legal[p] == 0;
    }
    long long target_bit_failures = 0, central_bit_failures = 0;
    for (const Record& record : records) {
        if (record.type < 0 || record.type > 1) continue;
        int united = 0;
        for (int p = record.index; p <= record.index + record.type; ++p) united |= legal[p];
        target_bit_failures += popcount(static_cast<unsigned>(record.target & ~united));
    }
    for (int i = 0; i < static_cast<int>(central.size()); ++i) {
        int united = 0;
        for (int p = i; p <= i + d; ++p) united |= legal[p];
        central_bit_failures += popcount(static_cast<unsigned>(central[i] & ~united));
    }
    cout << "records=" << records.size() << " slots=" << slots.size()
         << " missing_targets=" << missing_targets
         << " bad_target=" << bad_target
         << " duplicate_target=" << duplicate_target
         << " duplicate_slot=" << duplicate_slot
         << " bad_recorded=" << bad_recorded
         << " bad_containment=" << bad_containment
         << " bad_position_nonzero=" << bad_position_nonzero << '\n';
    cout << "empty_positions=" << empty_positions
         << " target_bit_failures=" << target_bit_failures
         << " central_bit_failures=" << central_bit_failures << '\n';
}
