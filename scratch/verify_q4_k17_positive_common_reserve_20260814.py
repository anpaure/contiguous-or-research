#!/usr/bin/env python3
"""Independent literal replay of the q4 k17 positive common reserve."""

from collections import Counter
import sys

sys.path.insert(0, "scratch")
from verify_q4_v13_seven_by_seven_atom_20260814 import BASE, EXTRA, deck


C0 = frozenset((13, 14, 15, 16))
C = C0 | {0}
P = frozenset((1, 2, 3, 4))
H = C | P
S = frozenset((1, 2, 3, 4, 5, 6))
E = frozenset((0, 8, 9, 10, 11, 12, 13, 14, 15, 16))

INSERT_OLD = (2, 3, 4, 6, 7, 8, 10, 12, 9, 11)
INSERT_NEW = (1,) + INSERT_OLD

REPEATED = (
    ((10, 8, 13, 14, 16, 11, 9, 0, 15, 12),
     (10, 8, 13, 14, 16, 11, 9, 0, 7, 15, 12)),
    ((12, 8, 16, 0, 11, 13, 14, 10, 15, 9),
     (12, 8, 16, 0, 7, 11, 13, 14, 10, 15, 9)),
    ((14, 12, 11, 13, 0, 10, 15, 8, 9, 16),
     (14, 7, 12, 11, 13, 0, 10, 15, 8, 9, 16)),
)

LEAVES = {
    2: ((11, 9, 14, 10, 12, 13, 0, 16, 15, 8),
        (11, 9, 14, 10, 7, 12, 13, 0, 16, 15, 8)),
    3: ((8, 9, 13, 10, 16, 15, 14, 0, 11, 12),
        (8, 7, 9, 13, 10, 16, 15, 14, 0, 11, 12)),
    4: ((9, 16, 15, 12, 11, 14, 10, 13, 0, 8),
        (9, 16, 7, 15, 12, 11, 14, 10, 13, 0, 8)),
}


def rail_deck(core, order):
    assert len(core) == 5
    assert len(order) in (10, 11)
    assert len(order) == len(set(order))
    assert not (set(core) & set(order))
    assert set(core) | set(order) <= set(range(17))
    n = len(order)
    owners = [
        core | frozenset(order[(i+j) % n] for j in range(4))
        for i in range(n)
    ]
    assert len(owners) == len(set(owners)) == n
    assert all(
        len(owners[i] ^ owners[(i + 1) % n]) == 2 for i in range(n)
    )
    return owners


def four_windows(order):
    n = len(order)
    return {
        frozenset(order[(i + j) % n] for j in range(4))
        for i in range(n)
    }


def assert_insertion_pair(old, new):
    assert set(old) == E
    assert set(new) == E | {7}
    reduced = list(new)
    reduced.remove(7)
    assert tuple(reduced) == tuple(old)
    assert C0 not in four_windows(old)
    assert C0 not in four_windows(new)


def atom_shore(sign):
    rails = []
    for name, rail_sign, center, order in BASE + EXTRA:
        if rail_sign == sign:
            rails.append((name, [C0 | owner for owner in deck(center, order)]))
    return rails


def macro_shores():
    plus = [("Delta+", rail_deck(C, INSERT_NEW))]
    minus = [("Delta-", rail_deck(C, INSERT_OLD))]
    for i, (old, new) in enumerate(REPEATED, 2):
        minus.append((f"Phi1^{i}-", rail_deck(S - {1}, old)))
        plus.append((f"Phi1^{i}+", rail_deck(S - {1}, new)))
    for u, (old, new) in LEAVES.items():
        plus.append((f"Phi{u}-", rail_deck(S - {u}, old)))
        minus.append((f"Phi{u}+", rail_deck(S - {u}, new)))
    return plus, minus


def vector(rails):
    out = Counter()
    for _, owners in rails:
        out.update(owners)
    return out


def assert_simple(rails):
    total = sum(len(owners) for _, owners in rails)
    values = vector(rails)
    assert len(values) == total
    assert max(values.values(), default=0) <= 1
    return values


def point_difference(positive, negative):
    out = Counter()
    for owner, count in positive.items():
        for x in owner:
            out[x] += count
    for owner, count in negative.items():
        for x in owner:
            out[x] -= count
    return out


def main():
    assert INSERT_NEW[1:] == INSERT_OLD
    assert set(INSERT_OLD) == set(range(2, 13)) - {5}
    assert set(INSERT_NEW) == set(INSERT_OLD) | {1}
    for old, new in REPEATED:
        assert_insertion_pair(old, new)
    for old, new in LEAVES.values():
        assert_insertion_pair(old, new)

    atom_plus_rails = atom_shore(1)
    atom_minus_rails = atom_shore(-1)
    macro_plus_rails, macro_minus_rails = macro_shores()

    atom_plus = assert_simple(atom_plus_rails)
    atom_minus = assert_simple(atom_minus_rails)
    macro_plus = assert_simple(macro_plus_rails)
    macro_minus = assert_simple(macro_minus_rails)
    assert (sum(atom_plus.values()), sum(atom_minus.values())) == (73, 72)
    assert (sum(macro_plus.values()), sum(macro_minus.values())) == (74, 73)

    atom_delta = atom_plus.copy(); atom_delta.subtract(atom_minus)
    assert {x: v for x, v in atom_delta.items() if v} == {H: 1}
    assert point_difference(macro_plus, macro_minus) == Counter({x: 1 for x in H})
    assert macro_plus[H] == 1 and macro_minus[H] == 0

    # Exact cross-shore collision conditions for the two rail
    # decompositions after recoupling.
    assert not set(atom_plus) & set(macro_minus)
    assert not set(atom_minus) & set(macro_plus)
    state_one = assert_simple(macro_minus_rails + atom_plus_rails)
    state_two = assert_simple(macro_plus_rails + atom_minus_rails)
    assert sum(state_one.values()) == sum(state_two.values()) == 146
    assert point_difference(state_one, state_two) == Counter()

    # R_H=A+ is a genuine nonnegative reserve.  B+=Y- and B-=Y+-H are
    # simple 73-owner matchings with the same point degrees.
    b_plus = macro_minus
    b_minus = macro_plus.copy()
    b_minus[H] -= 1
    if not b_minus[H]:
        del b_minus[H]
    assert sum(b_plus.values()) == sum(b_minus.values()) == 73
    assert max(b_minus.values()) == 1
    assert point_difference(b_plus, b_minus) == Counter()
    reserve = atom_plus
    lhs = b_plus + reserve
    rhs = b_minus + reserve
    assert lhs == state_one
    assert rhs == state_two

    print(
        "PASS q=4 k=17 atom=7x7 macro=7x7 reserve_owners=73 "
        "state_owners=146 rails_per_state=14 owner_simple=yes point_equal=yes"
    )


if __name__ == "__main__":
    main()
