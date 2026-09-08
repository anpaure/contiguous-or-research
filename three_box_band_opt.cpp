#pragma GCC optimize("O3,unroll-loops")

#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

struct Point { int x, y, z; };

static vector<Point> hex_ring(int radius) {
    const int direction[6][3] = {
        {0, 1, -1}, {-1, 1, 0}, {-1, 0, 1},
        {0, -1, 1}, {1, -1, 0}, {1, 0, -1}
    };
    vector<Point> ring;
    int x = radius, y = -radius, z = 0;
    for (const auto& d : direction) {
        for (int step = 0; step < radius; ++step) {
            ring.push_back({x, y, z});
            x += d[0]; y += d[1]; z += d[2];
        }
    }
    return ring;
}

static vector<Point> outward_spiral(int a) {
    vector<Point> result{{a, a, a}};
    for (int radius = 1; radius <= a; ++radius) {
        for (Point p : hex_ring(radius))
            result.push_back({a + p.x, a + p.y, a + p.z});
    }
    return result;
}

static vector<Point> hamilton_spiral(int a) {
    const int direction[6][3] = {
        {0,-1,1},{1,-1,0},{1,0,-1},
        {0,1,-1},{-1,1,0},{-1,0,1}
    };
    vector<Point> result;
    for (int radius = a; radius >= 1; --radius) {
        int x = -radius, y = radius, z = 0;
        for (const auto& d : direction) {
            for (int step = 0; step < radius; ++step) {
                result.push_back({a+x,a+y,a+z});
                x += d[0]; y += d[1]; z += d[2];
            }
        }
    }
    result.push_back({a,a,a});
    return result;
}

static vector<Point> row_snake(int a) {
    vector<Point> result;
    for (int x = 0; x <= 2 * a; ++x) {
        int low = max(0, a - x);
        int high = min(2 * a, 3 * a - x);
        if (x % 2 == 0) {
            for (int y = low; y <= high; ++y)
                result.push_back({x, y, 3 * a - x - y});
        } else {
            for (int y = high; y >= low; --y)
                result.push_back({x, y, 3 * a - x - y});
        }
    }
    return result;
}

static bool adjacent(const Point& p, const Point& q) {
    int dx = abs(p.x - q.x), dy = abs(p.y - q.y), dz = abs(p.z - q.z);
    return dx + dy + dz == 2 && max({dx, dy, dz}) == 1;
}

static vector<Point> sector_piece(int a, int sector, int option) {
    bool flip = option & 1;
    bool reversed = option & 2;
    vector<Point> piece;
    for (int radius = 1; radius <= a; ++radius) {
        vector<Point> ring = hex_ring(radius);
        bool ascending = ((radius & 1) != 0) ^ flip;
        if (ascending) {
            for (int step = 0; step < radius; ++step)
                piece.push_back(ring[sector * radius + step]);
        } else {
            for (int step = radius - 1; step >= 0; --step)
                piece.push_back(ring[sector * radius + step]);
        }
    }
    if (reversed) reverse(piece.begin(), piece.end());
    for (Point& p : piece) { p.x += a; p.y += a; p.z += a; }
    return piece;
}

static vector<Point> sector_weave(int a) {
    Point center{a, a, a};
    vector<vector<vector<Point>>> option(6, vector<vector<Point>>(4));
    for (int sector = 0; sector < 6; ++sector)
        for (int code = 0; code < 4; ++code)
            option[sector][code] = sector_piece(a, sector, code);

    vector<int> choice(6, 0), answer_choice;
    auto search = [&](auto&& self, int sector, const Point& last) -> bool {
        if (sector == 6) { answer_choice = choice; return true; }
        for (int code = 0; code < 4; ++code) {
            const auto& piece = option[sector][code];
            if (!adjacent(last, piece.front())) continue;
            choice[sector] = code;
            if (self(self, sector + 1, piece.back())) return true;
        }
        return false;
    };
    if (!search(search, 0, center)) return {};
    vector<Point> result{center};
    for (int sector = 0; sector < 6; ++sector)
        result.insert(result.end(), option[sector][answer_choice[sector]].begin(),
                      option[sector][answer_choice[sector]].end());
    return result;
}

struct Run { int bit, left, right; };

static vector<Run> internal_runs(const vector<Point>& row, int side) {
    vector<Run> runs;
    int m = row.size();
    for (int block = 0; block < 3; ++block) {
        for (int height = 1; height <= side; ++height) {
            int bit = block * side + height - 1;
            for (int i = 0; i < m;) {
                auto present = [&](int index) {
                    int coordinate = block == 0 ? row[index].x
                                   : block == 1 ? row[index].y : row[index].z;
                    return coordinate >= height;
                };
                if (!present(i)) { ++i; continue; }
                int j = i;
                while (j + 1 < m && present(j + 1)) ++j;
                if (i > 0 && j + 1 < m) runs.push_back({bit, i, j});
                i = j + 1;
            }
        }
    }
    return runs;
}

static long long width_even_cube(int a) { return 3LL * a * a + 3LL * a + 1; }

static long long lower_even_cube(int a) {
    long long side_points = 2LL * a + 1;
    long long total = side_points * side_points * side_points;
    return (total - width_even_cube(a)) / 2 - 1;
}

static string sum_expression(const vector<string>& terms) {
    if (terms.empty()) return "0";
    if (terms.size() == 1) return terms[0];
    string result = "(+";
    for (const string& term : terms) result += " " + term;
    return result + ")";
}

int main(int argc, char** argv) try {
    if (argc != 4 && argc != 5)
        throw runtime_error("usage: three_box_band_opt a D output.smt2 [spiral|snake]");
    int a = stoi(argv[1]);
    int D = stoi(argv[2]);
    string output = argv[3];
    if (a <= 0 || D < 0) throw runtime_error("invalid a or D");

    string order = argc == 5 ? argv[4] : "spiral";
    vector<Point> row;
    if (order == "spiral") row = hamilton_spiral(a);
    else if (order == "snake") row = row_snake(a);
    else if (order == "sector") row = sector_weave(a);
    else if (order.rfind("file:", 0) == 0) {
        ifstream input(order.substr(5));
        Point p;
        while (input >> p.x >> p.y >> p.z) row.push_back(p);
    }
    if (row.empty()) throw runtime_error("unknown order");
    for (int i = 0; i + 1 < (int)row.size(); ++i)
        if (!adjacent(row[i], row[i + 1])) throw runtime_error("order is not Hamilton-adjacent");
    int M = row.size();
    if (M != width_even_cube(a)) throw runtime_error("spiral cardinality error");
    vector<Run> runs = internal_runs(row, 2 * a);
    long long L = lower_even_cube(a);
    long long short_capacity = 1LL * D * M + 1LL * D * (D + 1) / 2;
    long long sigma = short_capacity - L;
    long long required_full = max(0LL, M - sigma);

    ofstream out(output);
    if (!out) throw runtime_error("cannot open output");
    out << "; order=" << order << " a=" << a << " M=" << M << " D=" << D
        << " internal_runs=" << runs.size() << " L=" << L
        << " sigma=" << sigma << " required_full=" << required_full << "\n";
    out << "(set-option :opt.priority lex)\n";
    out << "(set-option :produce-models true)\n";
    for (int i = 0; i < M; ++i)
        out << "(declare-fun a" << i << " () Int)\n"
            << "(declare-fun b" << i << " () Int)\n";
    for (int i = 0; i < M; ++i) {
        out << "(assert (and (<= 0 a" << i << ") (<= a" << i << " b" << i
            << ") (<= b" << i << ' ' << D << ")))\n";
        if (i + 1 < M)
            out << "(assert (and (<= a" << i << " a" << i + 1
                << ") (<= b" << i << " b" << i + 1 << ")))\n";
    }
    for (const Run& run : runs) {
        out << "(assert (<= (- b" << run.left - 1 << " a" << run.right + 1
            << ") " << run.right - run.left << "))\n";
    }

    vector<string> safe_terms, full_terms, gap_terms;
    int physical_length = M + D;
    for (int left = 0; left < physical_length; ++left) {
        for (int right = left; right < physical_length && right - left + 1 <= D; ++right) {
            vector<string> avoids;
            int first = max(0, left - D);
            int last = min(M - 1, right);
            for (int i = first; i <= last; ++i) {
                // J=[left,right] fails to contain I_i=[i+a_i,i+b_i].
                avoids.push_back("(or (> " + to_string(left) + " (+ " +
                                 to_string(i) + " a" + to_string(i) + ")) (< " +
                                 to_string(right) + " (+ " + to_string(i) + " b" +
                                 to_string(i) + ")))");
            }
            string condition = avoids.empty() ? "true" : "(and";
            if (!avoids.empty()) {
                for (const string& term : avoids) condition += " " + term;
                condition += ")";
            }
            safe_terms.push_back("(ite " + condition + " 1 0)");
        }
    }
    for (int i = 0; i < M; ++i) {
        full_terms.push_back("(ite (= (- b" + to_string(i) + " a" +
                             to_string(i) + ") " + to_string(D) + ") 1 0)");
        gap_terms.push_back("(- b" + to_string(i) + " a" + to_string(i) + ")");
    }
    string full = sum_expression(full_terms);
    string gaps = sum_expression(gap_terms);
    string safe = sum_expression(safe_terms);
    out << "(define-fun safe_count () Int " << safe << ")\n";
    out << "(define-fun full_count () Int " << full << ")\n";
    out << "(define-fun gap_sum () Int " << gaps << ")\n";
    out << "(maximize safe_count)\n";
    out << "(maximize full_count)\n";
    out << "(maximize gap_sum)\n";
    out << "(check-sat)\n";
    out << "(get-objectives)\n";
    out << "(get-value (safe_count full_count gap_sum))\n";
    out << "(get-value (";
    for (int i = 0; i < M; ++i) out << " a" << i << " b" << i;
    out << "))\n";

    cerr << "order=" << order << " a=" << a << " M=" << M << " D=" << D
         << " runs=" << runs.size() << " L=" << L
         << " short_capacity=" << short_capacity << " sigma=" << sigma
         << " required_full=" << required_full << '\n';
    return 0;
} catch (const exception& e) {
    cerr << "error: " << e.what() << '\n';
    return 2;
}
