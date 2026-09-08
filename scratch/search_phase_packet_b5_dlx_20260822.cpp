#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <limits>
#include <sstream>
#include <string>
#include <vector>

// Algorithm X / dancing-links search for a 6-uniform exact cover on the
// residual b=5 instance emitted during the phase-packet audit.
struct DLX {
  struct Node { int l, r, u, d, col, row; };
  int cols;
  std::vector<Node> a;
  std::vector<int> sz, solution;
  long long nodes = 0;
  std::chrono::steady_clock::time_point deadline;

  explicit DLX(int c) : cols(c), a(c + 1), sz(c + 1, 0) {
    for (int i = 0; i <= c; ++i) {
      a[i] = {i - 1, i + 1, i, i, i, -1};
    }
    a[0].l = c;
    a[c].r = 0;
  }

  void add_row(int row, const std::array<int, 6>& cs) {
    int first = -1, prev = -1;
    for (int raw : cs) {
      int c = raw + 1;
      int x = static_cast<int>(a.size());
      a.push_back({x, x, a[c].u, c, c, row});
      a[a[c].u].d = x;
      a[c].u = x;
      ++sz[c];
      if (first < 0) first = x;
      if (prev >= 0) {
        a[x].l = prev;
        a[x].r = first;
        a[prev].r = x;
        a[first].l = x;
      }
      prev = x;
    }
  }

  void cover(int c) {
    a[a[c].r].l = a[c].l;
    a[a[c].l].r = a[c].r;
    for (int i = a[c].d; i != c; i = a[i].d) {
      for (int j = a[i].r; j != i; j = a[j].r) {
        a[a[j].d].u = a[j].u;
        a[a[j].u].d = a[j].d;
        --sz[a[j].col];
      }
    }
  }

  void uncover(int c) {
    for (int i = a[c].u; i != c; i = a[i].u) {
      for (int j = a[i].l; j != i; j = a[j].l) {
        ++sz[a[j].col];
        a[a[j].d].u = j;
        a[a[j].u].d = j;
      }
    }
    a[a[c].r].l = c;
    a[a[c].l].r = c;
  }

  bool search() {
    ++nodes;
    if (a[0].r == 0) return true;
    if ((nodes & 0x3ffff) == 0 &&
        std::chrono::steady_clock::now() > deadline) return false;
    int c = a[0].r;
    for (int j = a[c].r; j != 0; j = a[j].r) {
      if (sz[j] < sz[c]) c = j;
    }
    if (sz[c] == 0) return false;
    cover(c);
    for (int r = a[c].d; r != c; r = a[r].d) {
      solution.push_back(a[r].row);
      for (int j = a[r].r; j != r; j = a[j].r) cover(a[j].col);
      if (search()) return true;
      for (int j = a[r].l; j != r; j = a[j].l) uncover(a[j].col);
      solution.pop_back();
    }
    uncover(c);
    return false;
  }
};

int main(int argc, char** argv) {
  if (argc < 2) {
    std::cerr << "usage: search_phase_packet_b5_dlx EDGE_FILE [seconds]\n";
    return 2;
  }
  int seconds = argc >= 3 ? std::stoi(argv[2]) : 120;
  std::ifstream in(argv[1]);
  if (!in) return 2;
  DLX dlx(144);
  std::string line;
  int row = 0;
  while (std::getline(in, line)) {
    std::istringstream ss(line);
    std::array<int, 6> e{};
    bool ok = true;
    for (int& x : e) if (!(ss >> x)) ok = false;
    if (ok) dlx.add_row(row++, e);
  }
  dlx.deadline = std::chrono::steady_clock::now() + std::chrono::seconds(seconds);
  bool found = dlx.search();
  std::cout << (found ? "SAT" : "UNKNOWN") << " rows=" << row
            << " nodes=" << dlx.nodes << " selected=" << dlx.solution.size() << "\n";
  if (found) {
    for (int x : dlx.solution) std::cout << x << ' ';
    std::cout << '\n';
  }
  return found ? 0 : 1;
}
