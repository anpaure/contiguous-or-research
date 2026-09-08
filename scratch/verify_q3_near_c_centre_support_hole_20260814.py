#!/usr/bin/env python3
"""Exact finite replay for the q=3 centre/point-degree obstruction.

This verifier works only with the necessary centre variables.  It checks
that no three-rail ledger satisfies the exact point-degree bound; for a
four-rail physical shore it separately excludes net mass three and checks
that every relaxed net-mass-four state has the normal form of Proposition
4.1.  It does not claim that independently chosen t_z values arise from a
common collection of toggle words.
"""

from itertools import product


def local_states(h: int, shore: int):
    out = []
    # The global l1 mass is at most 2*shore, so larger coordinates cannot
    # occur.  The congruence and exact point equation determine t.
    for a in range(-2 * shore, 2 * shore + 1):
        if (2 * a - h) % 3:
            continue
        for b in range(-2 * shore, 2 * shore + 1):
            num = h - 8 * a - 9 * b
            if num % 3:
                continue
            t = num // 3
            if abs(t) <= shore:
                out.append((a, b, t, abs(a) + abs(b)))
    return out


def exterior_aggregate(states, slots, target_l1):
    # Eight exterior slots suffice because every nonzero slot costs at least
    # one and target_l1 <= 8.  The final flag remembers every violation of
    # the asserted normal form (nonzero exterior a or negative exterior b).
    partial = {(0, 0, 0, False)}
    for _ in range(slots):
        nxt = set()
        for sa, sb, sl, bad in partial:
            for a, b, _t, cost in states:
                if sl + cost <= target_l1:
                    nxt.add((sa + a, sb + b, sl + cost,
                             bad or a != 0 or b < 0))
        partial = nxt
    return partial


def main():
    for shore, net_mass in ((3, 3), (4, 3), (4, 4)):
        h_states = local_states(1, shore)
        e_states = local_states(0, shore)
        target_l1 = 2 * net_mass
        ext = exterior_aggregate(e_states, 8, target_l1)
        witnesses = []
        for h in product(h_states, repeat=4):
            ha = sum(x[0] for x in h)
            hb = sum(x[1] for x in h)
            hl = sum(x[3] for x in h)
            for ea, eb, el, bad in ext:
                if (ha + ea, hb + eb, hl + el) == (-1, 1, target_l1):
                    witnesses.append((h, (ea, eb, el, bad)))
        if net_mass == 3:
            assert not witnesses, witnesses[:1]
            print(f"PASS shore={shore} net_mass={net_mass} "
                  "feasible_relaxed_states=0")
            continue

        assert witnesses
        normalized = set()
        for h, (ea, eb, _el, bad) in witnesses:
            avec = tuple(x[0] for x in h)
            bvec = tuple(x[1] for x in h)
            assert sorted(avec) == [-1, -1, -1, 2]
            z0 = avec.index(2)
            assert bvec[z0] == -1
            assert ea == 0
            assert not bad
            assert all(x >= 0 for i, x in enumerate(bvec) if i != z0)
            assert eb >= 0
            assert sum(bvec[i] for i in range(4) if i != z0) + eb == 2
            normalized.add((tuple(sorted(x for i, x in enumerate(bvec) if i != z0)),
                            eb))
        print(f"PASS shore=4 net_mass=4 relaxed_states={len(witnesses)} "
              f"centre_distribution_types={len(normalized)}")


if __name__ == "__main__":
    main()
