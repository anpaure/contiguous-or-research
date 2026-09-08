#!/usr/bin/env python3
"""Research-only stress test for monotonic adjacent rho minima."""

from __future__ import annotations

import argparse
import math

import numpy as np


def logchoose(n: int, k: int) -> float:
    if not 0 <= k <= n:
        return float("-inf")
    return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)


def run(b: int) -> None:
    h = int(math.sqrt(b * math.log(b)))
    mult = (b - 1) // 2
    g = b // 4
    logw = logchoose(2 * b, b)
    phases = np.arange(b, dtype=np.int64)
    totals = np.zeros((h + 1, 2 * b + 1), dtype=np.float64)
    weights = {}
    for r in range(g, b - g + 1):
        weight = math.exp(2 * logchoose(b, r) - math.log(b) - logw)
        weights[r] = weight
        bits = (((mult * phases) % b) < r).astype(np.int8)
        z = np.zeros(b, dtype=np.int16)
        for q in range(1, h + 1):
            z += bits[(phases + q) % b]
            totals[q] += np.bincount(r + z, minlength=2 * b + 1) * weight

    rho = np.zeros_like(totals)
    for q in range(1, h + 1):
        for s in np.flatnonzero(totals[q] > 0):
            p = math.exp(logchoose(b, int(s)) + logchoose(b, int(s) - q) - logw)
            rho[q, s] = min(1.0, p / totals[q, s])

    max_violation = 0.0
    witness = None
    positive_mass = 0.0
    prefix_loss = 0.0
    a1 = 0.0
    max_four = 0.0
    four_witness = None
    consecutive_two_step = 0.0
    consecutive_witness = None
    failed_return_mass = 0.0
    failed_return_witness = None
    for r, weight in weights.items():
        bits = (((mult * phases) % b) < r).astype(np.int8)
        z = np.zeros(b, dtype=np.int16)
        prof = np.empty((b, h), dtype=np.int16)
        for q in range(1, h + 1):
            z += bits[(phases + q) % b]
            prof[:, q - 1] = r + z
        qidx = np.arange(1, h + 1)
        vals = rho[qidx[None, :], prof]
        adjacent = np.minimum(vals[:, 1:], vals[:, :-1])
        diffs = adjacent[:, 1:] - adjacent[:, :-1]
        where = np.argwhere(diffs > 5e-13)
        positive_mass += weight * float(np.maximum(diffs, 0).sum())
        if where.size:
            p, j = where[np.argmax(diffs[where[:, 0], where[:, 1]])]
            value = float(diffs[p, j])
            if value > max_violation:
                max_violation = value
                witness = (r, int(p), int(j + 2), int(j + 3), value)
        running = np.minimum.accumulate(vals, axis=1)
        prefix_loss += weight * float((vals - running).sum())
        a1 += weight * float(np.maximum(vals[:, 1:] - vals[:, :-1], 0).sum())
        if h >= 5:
            d4 = vals[:, 4:] - vals[:, :-4]
            loc = np.unravel_index(np.argmax(d4), d4.shape)
            if d4[loc] > max_four:
                max_four = float(d4[loc])
                four_witness = (r, int(loc[0]), int(loc[1] + 1), int(loc[1] + 5))
        if h >= 5:
            d2 = vals[:, 2:] - vals[:, :-2]
            both = (d2[:, :-2] > 5e-13) & (d2[:, 2:] > 5e-13)
            consecutive_two_step += weight * float(both.sum())
            if consecutive_witness is None and np.any(both):
                loc = np.argwhere(both)[0]
                consecutive_witness = (r, int(loc[0]), int(loc[1] + 1))
            failed = (d2[:, :-2] > 5e-13) & (vals[:, 4:] - vals[:, :-4] > 5e-13)
            failed_return_mass += weight * float(failed.sum())
            if failed_return_witness is None and np.any(failed):
                loc = np.argwhere(failed)[0]
                failed_return_witness = (r, int(loc[0]), int(loc[1] + 1))

    print(
        "ADJACENT_MIN",
        b,
        h,
        "max_violation",
        max_violation,
        "witness",
        witness,
        "positive_mass",
        positive_mass,
        "prefix_loss",
        prefix_loss,
        "A1",
        a1,
        "difference",
        prefix_loss - a1,
        "max_four",
        max_four,
        "four_witness",
        four_witness,
        "consecutive_two_step_mass",
        consecutive_two_step,
        "consecutive_witness",
        consecutive_witness,
        "failed_return_mass",
        failed_return_mass,
        "failed_return_witness",
        failed_return_witness,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("b", type=int)
    run(parser.parse_args().b)
