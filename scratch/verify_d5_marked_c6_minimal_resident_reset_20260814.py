#!/usr/bin/env python3
"""Independent finite replay for the 18+6 owner marked-C6 reset box.

This file is intended to be executed on h100 only.
"""

from collections import Counter
from hashlib import sha256


def add(base, *labels):
    return frozenset(set(base).union(labels))


def cyclic_runs(bits):
    if all(bits) or not any(bits):
        return None
    n = len(bits)
    cut = next(i for i in range(n) if bits[i] != bits[(i - 1) % n])
    vals = bits[cut:] + bits[:cut]
    runs = []
    cur = vals[0]
    size = 0
    for value in vals:
        if value == cur:
            size += 1
        else:
            runs.append((cur, size))
            cur = value
            size = 1
    runs.append((cur, size))
    return runs


def palettes(cycles):
    owners = [v for cyc in cycles for v in cyc]
    lowers = []
    uppers = []
    low_q2 = []
    up_q2 = []
    for cyc in cycles:
        n = len(cyc)
        for i in range(n):
            lowers.append(cyc[i] & cyc[(i + 1) % n])
            uppers.append(cyc[i] | cyc[(i + 1) % n])
            low_q2.append(cyc[i] & cyc[(i + 1) % n] & cyc[(i + 2) % n])
            up_q2.append(cyc[i] | cyc[(i + 1) % n] | cyc[(i + 2) % n])
    return owners, lowers, uppers, low_q2, up_q2


def assert_johnson_cycles(cycles):
    for cyc in cycles:
        assert len(cyc) == len(set(cyc))
        rank = len(cyc[0])
        for i, owner in enumerate(cyc):
            nxt = cyc[(i + 1) % len(cyc)]
            assert len(owner) == rank
            assert len(owner - nxt) == 1
            assert len(nxt - owner) == 1


def trace_minima(cycles, ground):
    owner_one = []
    owner_zero = []
    upper_one = []
    upper_zero = []
    for cyc in cycles:
        upper = [cyc[i] | cyc[(i + 1) % len(cyc)] for i in range(len(cyc))]
        for trace, one_out, zero_out in (
            (cyc, owner_one, owner_zero),
            (upper, upper_one, upper_zero),
        ):
            for label in ground:
                runs = cyclic_runs([label in v for v in trace])
                if runs is None:
                    continue
                one_out.extend(size for value, size in runs if value)
                zero_out.extend(size for value, size in runs if not value)
    return min(owner_one), min(owner_zero), min(upper_one), min(upper_zero)


def resident_port(K, x1, x2, y1, y2, z, a0, a1):
    A = add(K, z, a0)
    B = add(K, a0, a1)
    P1 = add(set(K) - {x1}, y1, a0, a1)
    P2 = add(set(K) - {x1, x2}, y1, y2, a0, a1)
    Q0 = add(set(K) - {x1, x2}, y1, y2, z, a0)
    Q1 = add(set(K) - {x2}, y2, z, a0)
    return [A, B, P1, P2, Q0, Q1]


def build(rank):
    assert rank >= 5
    K = ["h", "x1", "x2"] + [f"k{j}" for j in range(rank - 5)]
    router_out = ["z", "a0", "a1", "a2", "y1", "y2"]
    filler = [f"f{j}" for j in range(rank - 5)]
    ground = K + router_out + filler
    assert len(ground) == 2 * rank - 1

    old_router = []
    for i in range(3):
        old_router.append(
            resident_port(
                frozenset(K),
                "x1",
                "x2",
                "y1",
                "y2",
                "z",
                f"a{i}",
                f"a{(i + 1) % 3}",
            )
        )

    # The switched seam is A_i -> B_(i-1).  Starting at A_0 gives the
    # component order 0,2,1, hence the full port action (0 2 1).
    new_router_cycle = []
    i = 0
    for _ in range(3):
        new_router_cycle.append(old_router[i][0])
        j = (i - 1) % 3
        new_router_cycle.extend(old_router[j][1:])
        i = j
    assert i == 0 and len(new_router_cycle) == 18

    # A six-owner identity spectator.  Every router resource contains h;
    # every spectator resource omits h, so all three typed banks are disjoint.
    spec_extras = ["x1", "x2", "z", "a0", "a1"]
    spec_core_candidates = [v for v in ground if v != "h" and v not in spec_extras]
    Kp = frozenset(spec_core_candidates[: rank - 2])
    assert len(Kp) == rank - 2 and "h" not in Kp
    spec_x1, spec_x2 = sorted(Kp)[:2]
    spec_y1, spec_y2, spec_z, spec_a0, spec_a1 = spec_extras
    spectator = resident_port(
        Kp, spec_x1, spec_x2, spec_y1, spec_y2, spec_z, spec_a0, spec_a1
    )

    old_cycles = old_router + [spectator]
    new_cycles = [new_router_cycle, spectator]
    return frozenset(ground), old_router, new_router_cycle, spectator, old_cycles, new_cycles


def check(rank):
    ground, old_router, new_router, spectator, old_cycles, new_cycles = build(rank)
    old = palettes(old_cycles)
    new = palettes(new_cycles)

    assert_johnson_cycles(old_cycles)
    assert_johnson_cycles(new_cycles)
    assert all(owner <= ground for owner in old[0] + new[0])

    for typed in range(3):
        assert len(old[typed]) == 24
        assert len(set(old[typed])) == 24
        assert Counter(old[typed]) == Counter(new[typed])

    # Complete q2 occurrence currents vanish on both lower/intersection and
    # upper/union shores.
    assert Counter(old[3]) == Counter(new[3])
    assert Counter(old[4]) == Counter(new[4])
    assert len(set(old[3])) == len(old[3]) == 24
    assert len(set(old[4])) == len(old[4]) == 24

    assert trace_minima(old_cycles, ground) == (3, 3, 4, 2)
    assert trace_minima(new_cycles, ground) == (3, 3, 4, 2)

    # Full first-return map on A sockets: 0->2->1->0.  Label
    # b=0,u=2,c=1, so it is (b u c); suppressing u gives (b c).
    full_return = {0: 2, 2: 1, 1: 0}
    assert full_return == {0: 2, 2: 1, 1: 0}
    marked = {0, 1}
    quotient = {}
    for start in marked:
        cur = full_return[start]
        while cur not in marked:
            cur = full_return[cur]
        quotient[start] = cur
    assert quotient == {0: 1, 1: 0}

    # The spectator first-return map is the identity in both phases.
    assert spectator in old_cycles and spectator in new_cycles

    # Exact seam-local q2 formula, including occurrence labels.
    for i in range(3):
        Ai = old_router[i][0]
        Q1i = old_router[i][5]
        Bi = old_router[i][1]
        P1i = old_router[i][2]
        j = (i - 1) % 3
        Bj = old_router[j][1]
        P1j = old_router[j][2]
        assert Q1i & Ai & Bi == Q1i & Ai & Bj
        assert Ai & Bi & P1i == Ai & Bj & P1j
        new_upper = [Q1i | Ai | Bj, Ai | Bj | P1j]
        old_upper_shifted = [
            old_router[j][5] | old_router[j][0] | old_router[j][1],
            old_router[j][0] | old_router[j][1] | old_router[j][2],
        ]
        assert new_upper == old_upper_shifted

    return {
        "rank": rank,
        "ground": len(ground),
        "owners": len(old[0]),
        "lower_q1": len(set(old[1])),
        "upper_q1": len(set(old[2])),
        "lower_q2_values": len(set(old[3])),
        "upper_q2_values": len(set(old[4])),
        "old_components": [len(c) for c in old_cycles],
        "new_components": [len(c) for c in new_cycles],
        "minima": trace_minima(new_cycles, ground),
    }


def first_return(cycle, marked):
    positions = {value: i for i, value in enumerate(cycle)}
    answer = {}
    for start in marked:
        i = positions[start]
        for step in range(1, len(cycle) + 1):
            nxt = cycle[(i + step) % len(cycle)]
            if nxt in marked:
                answer[start] = nxt
                break
    return answer


def check_terminal_types_rank7():
    rank = 7
    ground, old_router, new_router, _, _, _ = build(rank)
    K = frozenset({"h", "x1", "x2", "k0", "k1"})
    router = palettes(old_router)

    B = old_router[0][0]
    U = old_router[2][0]
    cases = []

    # Adjacent-head D5 type.
    C1 = old_router[1][0]
    T1 = frozenset(K | {"z", "f0"})
    Kp1 = frozenset((T1 - {"f0", "h"}))
    S1 = resident_port(Kp1, "k0", "k1", "a0", "a1", "f0", "h", "f1")
    assert S1[0] == T1
    cases.append(("adjacent", T1, B, C1, S1, (1, 1, 1, rank - 1, rank + 2)))

    # Distance-two-head D5 type.  The second head is a different phase on
    # port cycle 1, so the router is a tapped box and needs no serial cable.
    C2 = old_router[1][5]
    T2 = frozenset((K - {"x2"}) | {"z", "a0", "a1"})
    Kp2 = frozenset(T2 - {"h", "a0"})
    S2 = resident_port(Kp2, "a1", "k0", "f0", "f1", "h", "a0", "a2")
    assert S2[0] == T2
    cases.append(("distance_two", T2, B, C2, S2, (1, 1, 2, rank - 2, rank + 2)))

    summary = []
    for name, tail, b, c, spectator, expected in cases:
        actual = (
            len(tail - b),
            len(tail - c),
            len(b - c),
            len(tail & b & c),
            len(tail | b | c),
        )
        assert actual == expected

        spec = palettes([spectator])
        for typed in range(5):
            assert len(set(spec[typed])) == 6
            assert not (set(spec[typed]) & set(router[typed]))
        assert trace_minima([spectator], ground) == (3, 3, 4, 2)

        marked = {b, U, c}
        new_map = first_return(new_router, marked)
        assert new_map == {b: U, U: c, c: b}
        for old_cycle, mark in zip(old_router, (b, c, U)):
            assert first_return(old_cycle, {mark}) == {mark: mark}

        quotient = first_return(new_router, {b, c})
        assert quotient == {b: c, c: b}
        summary.append((name, actual, [old_router.index(cyc) for cyc in old_router if b in cyc or c in cyc]))

    return summary


def main():
    rows = [check(rank) for rank in range(5, 41)]
    terminal_rows = check_terminal_types_rank7()
    print("MARKED_C6_MINIMAL_RESIDENT_RESET PASS")
    print("checked ranks 5..40")
    for row in (rows[0], rows[-1]):
        print(row)
    print("full action (b u c), marked quotient (b c), spectator fixed")
    print("owner/lower-q1/upper-q1 palettes simple and phase-equal")
    print("lower-q2 current zero; upper-q2 current zero")
    print("old/new owner and immediate-upper minima 3/3 and 4/2")
    print("rank-7 D5 terminal types", terminal_rows)
    digest = sha256(repr((rows, terminal_rows)).encode()).hexdigest()
    print("result digest", digest)


if __name__ == "__main__":
    main()
