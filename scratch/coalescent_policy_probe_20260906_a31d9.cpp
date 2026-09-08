#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <queue>
#include <random>
#include <vector>

// Exploration only. Monte Carlo output is not an upper-bound certificate.
double density3(double a, double b, double c) {
    std::array<double, 3> x{a, b, c};
    std::sort(x.begin(), x.end());
    double v = std::max(0.0, x[0] + x[1] - x[2]);
    return 1.0 / x[2] - v * v / (4 * x[0] * x[1] * x[2]);
}

double cost4(std::vector<double> x) {
    std::sort(x.begin(), x.end());
    return 1.0 / x[3] + density3(x[0], x[1], x[2]);
}

double cost5pair(const std::vector<double>& x, int i, int j) {
    double a = x[i], b = x[j];
    std::vector<double> rest;
    for (int t = 0; t < 5; ++t) if (t != i && t != j) rest.push_back(x[t]);
    std::sort(rest.begin(), rest.end());
    double c = rest[0], d = rest[1], e = rest[2];
    auto q = [=](double s) {
        double v = std::max(0.0, s - d + c), w = std::max(0.0, s - c - d);
        return s * s / (2 * e) + s * s / (2 * d)
            - (v * v * v - w * w * w) / (12 * c * d);
    };
    double lo = std::abs(a - b), hi = a + b;
    double value = q(std::min(hi, e)) - q(std::min(lo, e));
    double l = std::max(lo, e), u = std::max(hi, e);
    value += u - l + density3(c, d, e) * (u * u - l * l) / 2;
    return value / (2 * a * b);
}

double cost5(const std::vector<double>& x) {
    double best = 1e100;
    for (int i = 0; i < 5; ++i) for (int j = i + 1; j < 5; ++j)
        best = std::min(best, cost5pair(x, i, j));
    return best;
}

int main(int argc, char** argv) {
    int m = argc > 1 ? std::atoi(argv[1]) : 32;
    int n = argc > 2 ? std::atoi(argv[2]) : 100000;
    int mode = argc > 3 ? std::atoi(argv[3]) : 0;
    double threshold = argc > 4 ? std::atof(argv[4]) : 1.0;
    std::mt19937_64 rng(20260906);
    std::normal_distribution<double> normal;
    std::uniform_real_distribution<double> uniform(-1, 1);
    long double total = 0, squared = 0;
    for (int sample = 0; sample < n; ++sample) {
        std::vector<double> x;
        for (int i = 0; i < m; ++i) {
            double a = normal(rng), b = normal(rng), c = normal(rng);
            x.push_back(std::sqrt(a * a + b * b + c * c));
        }
        if (mode == 4) {
            std::array<double, 3> active{x[0], x[1], x[2]};
            for (int t = 3; t < m; ++t) {
                int i = std::min_element(active.begin(), active.end()) - active.begin();
                double a = active[i], b = x[t];
                active[i] = std::sqrt(a * a + b * b + 2 * a * b * uniform(rng));
            }
            std::sort(active.begin(), active.end());
            double value = (1 / active[1] + 1 / active[2])
                * std::sqrt(std::acos(-1.0) * m / 8);
            total += value;
            squared += value * value;
            continue;
        }
        while (x.size() > 5) {
            std::sort(x.begin(), x.end());
            int i = 0, j = 1;
            if (mode == 1) {
                // Feed the smallest factor to the largest unfrozen factor.
                for (int t = 1; t < static_cast<int>(x.size()); ++t)
                    if (x[t] < threshold * std::sqrt(m)) j = t;
            } else if (mode == 2) {
                // Freeze the largest factor; accumulate all others sequentially.
                j = static_cast<int>(x.size()) - 2;
            } else if (mode == 3) {
                // Feed whichever of the two largest factors is currently smaller.
                j = static_cast<int>(x.size()) - 2;
                if (x.back() < threshold * std::sqrt(m)) j += 1;
            }
            double a = x[i], b = x[j];
            double r = std::sqrt(a * a + b * b + 2 * a * b * uniform(rng));
            x.erase(x.begin() + j);
            x.erase(x.begin() + i);
            x.push_back(r);
        }
        double value = x.size() == 5 ? cost5(x) : cost4(x);
        value *= std::sqrt(std::acos(-1.0) * m / 8);
        total += value;
        squared += value * value;
    }
    double mean = total / n;
    double se = std::sqrt(std::max(0.0L, squared / n - mean * mean) / n);
    std::cout << std::setprecision(12) << "EXPLORATORY_MONTE_CARLO m=" << m << " samples=" << n
              << " mode=" << mode << " threshold=" << threshold
              << " estimate=" << mean << " standard_error=" << se << '\n';
}
