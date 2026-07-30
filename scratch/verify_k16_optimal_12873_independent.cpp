#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

int main(int argc, char** argv) {
  if (argc != 2) {
    std::cerr << "usage: verify_k16_optimal_12873_independent WORD\n";
    return 2;
  }

  std::ifstream in(argv[1]);
  if (!in) {
    std::cerr << "cannot open word\n";
    return 2;
  }

  std::vector<std::uint32_t> word;
  std::uint32_t value = 0;
  while (in >> value) {
    if (value == 0 || value >= (1u << 16)) {
      std::cerr << "invalid letter " << value << "\n";
      return 1;
    }
    word.push_back(value);
  }
  if (word.size() != 12873) {
    std::cerr << "wrong length " << word.size() << "\n";
    return 1;
  }

  std::vector<unsigned char> seen(1u << 16, 0);
  for (std::size_t left = 0; left < word.size(); ++left) {
    std::uint32_t joined = 0;
    for (std::size_t right = left; right < word.size(); ++right) {
      joined |= word[right];
      seen[joined] = 1;
      if (joined == 0xffffu) break;
    }
  }

  std::size_t covered = 0;
  for (std::uint32_t mask = 1; mask <= 0xffffu; ++mask) covered += seen[mask];
  if (covered != 65535) {
    std::cerr << "FAIL length=" << word.size() << " covered=" << covered
              << "/65535\n";
    return 1;
  }
  std::cout << "PASS length=12873 covered=65535/65535\n";
  return 0;
}
