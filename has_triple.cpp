#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int target = std::stoi(argv[1]);
    std::vector<int> path;
    for (int value; std::cin >> value;) path.push_back(value);
    for (std::size_t i = 0; i + 2 < path.size(); ++i) {
        if ((path[i] & path[i + 1] & path[i + 2]) == target) {
            std::cout << i << '\n';
            return 0;
        }
    }
    return 1;
}
