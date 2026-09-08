#!/usr/bin/env python3
"""Audit whether the three singleton-T2 backup rails are inverse portals.

For each height h, the ambient local ground has
  13 prefix + 2 tags + 2h clock = 2(h+8)-1
coordinates and the rail owners have rank R=h+8.  Thus the paths can be
tested literally as consecutive R-windows of positive rows in the full
canonical MSW inverse-triple atlas at m=R-1=h+7.

Heavy runs belong on h100 only.
"""

from collections import Counter
import argparse
from itertools import permutations

import audit_msw_inverse_trade_portal_shadow_20260813 as inv
import audit_msw_t2_singleton_a_clock as s
import search_msw_t2_singleton_backup_rails as backup


def gowner(base, tag, clock, h):
    return base | (tag << 13) | (clock << 15)


def dset(h, j):
    return sum(1 << ((j + k) % (2 * h)) for k in range(h))


def paths(h):
    Bx = s.base.bits("1011110011000")
    By = s.base.bits("1011110010010")
    Cx = s.base.bits("1010111011000")
    Cy = s.base.bits("1010111010010")
    Hx = s.base.bits("1000111010110")
    Hy = s.base.bits("1000111001110")
    Hz = s.base.bits("0000111001111")

    p1 = set(range(h + 1))
    K = [p1 - {0}, p1 - {1}]
    for j in range(2, h):
        nxt = set(K[-1])
        nxt.remove(j)
        nxt.add(h + j - 1)
        K.append(nxt)
    km = [sum(1 << x for x in z) for z in K]
    rho = lambda x: (h - 1 - x) % (2 * h)
    rkm = [sum(1 << rho(x) for x in z) for z in K]

    B = [gowner(Bx, 1, km[0], h), gowner(Bx, 1, km[1], h)]
    B += [gowner(By, 1, km[1], h)]
    B += [gowner(By, 1, km[j], h) for j in range(2, h)]

    C = [gowner(Cx, 1, rkm[0], h), gowner(Cx, 1, rkm[1], h)]
    C += [gowner(Cy, 1, rkm[1], h)]
    C += [gowner(Cy, 1, rkm[j], h) for j in range(2, h)]

    H = [gowner(Hx, 1, dset(h, 0), h),
         gowner(Hx, 1, dset(h, 1), h),
         gowner(Hy, 1, dset(h, 1), h),
         gowner(Hz, 1, dset(h, 1), h),
         gowner(Hz, 2, dset(h, 1), h)]
    H += [gowner(Hz, 2, dset(h, j), h) for j in range(2, h + 2)]
    out = {"B": B, "C": C, "H": H}
    R = h + 8
    n = 2 * R - 1
    for path in out.values():
        assert all(x.bit_count() == R for x in path)
        assert all((x ^ y).bit_count() == 2 for x, y in zip(path, path[1:]))
        assert max(x.bit_length() for x in path) <= n
    return out


def globalize(path, h):
    return [gowner(x[0], x[1], x[2], h) for x in path]


def candidate_paths(h):
    """All base choices for B,C, plus the monotone shortened H rail."""
    B = [globalize(row[0], h) for row in backup.bc_candidates(
        s.base.bits("1011110011010"), h, +1
    )]
    C = [globalize(row[0], h) for row in backup.bc_candidates(
        s.base.bits("1010111011010"), h, -1
    )]
    fs = backup.facets(backup.HBASE, 7)
    H = []
    from itertools import permutations
    for x0, x1, x2 in permutations(fs, 3):
        if (x0 ^ x1).bit_count() != 2 or (x1 ^ x2).bit_count() != 2:
            continue
        if x0 | x1 | x2 != backup.HBASE:
            continue
        path = [
            (x0, 1, dset(h, 0)),
            (x0, 1, dset(h, 1)),
            (x1, 1, dset(h, 1)),
            (x2, 1, dset(h, 1)),
            (x2, 2, dset(h, 1)),
        ]
        path += [(x2, 2, dset(h, j)) for j in range(2, h + 1)]
        assert backup.path_union(path) == (
            backup.HBASE, 3, (1 << (2 * h)) - 1
        )
        ro = backup.resources(path)
        if ro is not None:
            H.append(globalize(path, h))
    return {"B": B, "C": C, "Hshort": H}


def monotone_clock_staircases(h, sign):
    """All tight clock geodesics whose cumulative unions are P_1,... ."""
    p1 = set(range(h + 1))
    out = []
    for u in p1:
        a0 = p1 - {u}
        for v in p1 - {u}:
            a1 = p1 - {v}
            # a0 -> a1 deletes v and inserts u.  Later deletions must be
            # distinct elements of the initial set a0, never the inserted u.
            remaining = sorted(a0 - {v})
            for order in permutations(remaining, max(0, h - 2)):
                seq = [set(a0), set(a1)]
                current = set(a1)
                for j, deleted in enumerate(order, 2):
                    current = set(current)
                    current.remove(deleted)
                    current.add(h + j - 1)
                    seq.append(current)
                assert len(seq) == h
                for j in range(1, h):
                    assert set().union(*seq[:j + 1]) == set(range(h + j))
                if sign < 0:
                    rho = lambda x: (h - 1 - x) % (2 * h)
                    seq = [{rho(x) for x in z} for z in seq]
                out.append([sum(1 << x for x in z) for z in seq])
    assert len(out) == __import__("math").factorial(h + 1)
    return out


def all_bc_geodesic_paths(h):
    out = {}
    for label, target, sign in (
        ("B", s.base.bits("1011110011010"), +1),
        ("C", s.base.bits("1010111011010"), -1),
    ):
        rows = []
        for clocks in monotone_clock_staircases(h, sign):
            for x, y in permutations(backup.facets(target, 7), 2):
                path = [(x, 1, clocks[0]), (x, 1, clocks[1]),
                        (y, 1, clocks[1])]
                path += [(y, 1, clocks[j]) for j in range(2, h)]
                ro = backup.resources(path)
                assert ro is not None
                rows.append(globalize(path, h))
        out[label] = rows
    return out


def owner_windows(row, R):
    n = len(row)
    cur = sum(1 << row[j] for j in range(R))
    out = [cur]
    for i in range(1, n):
        cur ^= 1 << row[i - 1]
        cur ^= 1 << row[(i + R - 1) % n]
        out.append(cur)
    assert out[-1] != out[0]
    return out


def contains_path(row, path, R):
    ws = owner_windows(row, R)
    n = len(ws)
    hits = []
    for start, x in enumerate(ws):
        if x != path[0]:
            continue
        if all(ws[(start + j) % n] == y for j, y in enumerate(path)):
            hits.append(start)
    return hits


def path_key(path):
    return tuple(path)


def orbit_key(path, h):
    """Exact orbit under S_(h+1) x S_(h+1) auxiliary relabeling.

    Prefix coordinates 0..12 are fixed.  The first auxiliary class is
    {p0}+D0 and the second is {p1} plus (clock minus D0).  A coordinate
    permutation
    is determined on a path by permuting equal-length binary columns, so
    the two sorted column multisets are a complete invariant.
    """
    inside = [13] + list(range(15, 15 + h))
    outside = [14] + list(range(15 + h, 15 + 2 * h))
    prefix = tuple(x & ((1 << 13) - 1) for x in path)

    def columns(indices):
        return tuple(sorted(
            sum(((x >> bit) & 1) << j for j, x in enumerate(path))
            for bit in indices
        ))

    return prefix, columns(inside), columns(outside)


def unoriented_orbit_key(path, h):
    return min(orbit_key(path, h), orbit_key(list(reversed(path)), h))


def canonical_completion(path, n, R):
    deleted = [next(iter_bits(x & ~y)) for x, y in zip(path, path[1:])]
    inserted = [next(iter_bits(y & ~x)) for x, y in zip(path, path[1:])]
    assert len(set(deleted)) == len(deleted)
    assert len(set(inserted)) == len(inserted)
    first = path[0]
    if not all(first >> x & 1 for x in deleted):
        return None
    if not all(not (first >> x & 1) for x in inserted):
        return None
    remaining_in = sorted(set(iter_bits(first)) - set(deleted))
    remaining_out = sorted(set(range(n)) - set(iter_bits(first)) - set(inserted))
    row = tuple(deleted + remaining_in + inserted + remaining_out)
    assert len(row) == n and len(set(row)) == n
    assert contains_path(row, path, R) == [0]
    return inv.canonical_cycle(row)


def iter_bits(x):
    while x:
        b = (x & -x).bit_length() - 1
        yield b
        x &= x - 1


def disjoint_choice(candidates):
    labels = sorted(candidates, key=lambda x: len(candidates[x]))
    answer = {}
    used = set()

    def rec(i):
        if i == len(labels):
            return True
        label = labels[i]
        for tid in candidates[label]:
            pair = {2 * tid, 2 * tid + 1}
            if pair & used:
                continue
            used.update(pair)
            answer[label] = tid
            if rec(i + 1):
                return True
            used.difference_update(pair)
        return False

    return answer if rec(0) else None


def audit(h, all_candidates=False):
    R = h + 8
    m = R - 1
    n = 2 * m + 1
    rail = paths(h)
    banks = ({k: [v] for k, v in rail.items()}
             if not all_candidates else candidate_paths(h))
    completions = {k: canonical_completion(v, n, R) for k, v in rail.items()}
    roots, factor = inv.build_factor(m)
    pos_row_to_records = {}
    candidates = {k: set() for k in banks}
    candidate_path_hits = {k: set() for k in banks}
    exact_completion = {k: [] for k in rail}
    path_lookup = {
        label: {path_key(path): pid for pid, path in enumerate(path_bank)}
        for label, path_bank in banks.items()
    }
    trade_count = 0
    for z in inv.dyck_words(m - 2):
        for gap in range(len(z) + 1):
            a = z[:gap] + "1100" + z[gap:]
            b = z[:gap] + "1010" + z[gap:]
            neg = (factor[a], factor[b])
            pos = inv.recover_inverse_trade(*neg, m)
            tid = trade_count
            trade_count += 1
            for side, row in enumerate(pos):
                ws = owner_windows(row, R)
                nn = len(ws)
                for label, lookup in path_lookup.items():
                    lengths = {len(path) for path in banks[label]}
                    for length in lengths:
                        for start in range(nn):
                            key = tuple(ws[(start + j) % nn]
                                        for j in range(length))
                            pid = lookup.get(key)
                            if pid is None:
                                continue
                            candidates[label].add(tid)
                            candidate_path_hits[label].add(pid)
                            pos_row_to_records.setdefault(row, []).append(
                                (label, tid, side, pid, (start,), a, b)
                            )
                for label in rail:
                    if completions[label] is not None and row == completions[label]:
                        exact_completion[label].append((tid, side, a, b))
    choice = disjoint_choice(candidates)
    print("INVERSE_PORTAL h", h, "m", m, "n", n,
          "factor_rows", len(roots), "trades", trade_count)
    for label in banks:
        sample = []
        for row, recs in pos_row_to_records.items():
            for rec in recs:
                if rec[0] == label:
                    sample.append(rec[1:])
                    if len(sample) == 3:
                        break
            if len(sample) == 3:
                break
        print(" RAIL", label,
              "path_count", len(banks[label]),
              "length_hist", dict(Counter(map(len, banks[label]))),
              "portal_trades", len(candidates[label]),
              "portal_paths", len(candidate_path_hits[label]),
              "exact_completion", len(exact_completion.get(label, ())),
              "sample", sample)
    print(" DISJOINT_NEGATIVE_CHOICE", choice)
    return all(candidates.values()) and choice is not None


def audit_relabel_orbits(h):
    """All-candidate portal census modulo admissible payload relabeling."""
    R = h + 8
    m = R - 1
    n = 2 * m + 1
    banks = candidate_paths(h)
    wanted = {
        label: {unoriented_orbit_key(path, h): pid
                for pid, path in enumerate(path_bank)}
        for label, path_bank in banks.items()
    }
    candidates = {label: set() for label in banks}
    hit_keys = {label: set() for label in banks}
    examples = {label: [] for label in banks}

    roots, factor = inv.build_factor(m)
    tid = 0
    for z in inv.dyck_words(m - 2):
        for gap in range(len(z) + 1):
            a = z[:gap] + "1100" + z[gap:]
            b = z[:gap] + "1010" + z[gap:]
            pos = inv.recover_inverse_trade(factor[a], factor[b], m)
            for side, row in enumerate(pos):
                ws = owner_windows(row, R)
                for label, lookup in wanted.items():
                    length = len(banks[label][0])
                    for start in range(n):
                        arc = [ws[(start + j) % n] for j in range(length)]
                        key = unoriented_orbit_key(arc, h)
                        pid = lookup.get(key)
                        if pid is None:
                            continue
                        candidates[label].add(tid)
                        hit_keys[label].add(key)
                        if len(examples[label]) < 3:
                            examples[label].append(
                                (tid, side, start, pid, a, b)
                            )
            tid += 1

    choice = disjoint_choice(candidates)
    print("RELABEL_ORBIT_PORTAL h", h, "m", m, "n", n,
          "factor_rows", len(roots), "trades", tid)
    for label in banks:
        print(" RELABEL_RAIL", label,
              "path_count", len(banks[label]),
              "orbit_count", len(wanted[label]),
              "portal_trades", len(candidates[label]),
              "hit_orbits", len(hit_keys[label]),
              "examples", examples[label])
    print(" RELABEL_DISJOINT_NEGATIVE_CHOICE", choice)
    return all(candidates.values()) and choice is not None


def audit_factor_orbits(h):
    """Search unchanged canonical MSW factor rows modulo payload relabeling."""
    R = h + 8
    m = R - 1
    n = 2 * m + 1
    banks = candidate_paths(h)
    wanted = {
        label: {unoriented_orbit_key(path, h): pid
                for pid, path in enumerate(path_bank)}
        for label, path_bank in banks.items()
    }
    root_hits = {label: set() for label in banks}
    path_hits = {label: set() for label in banks}
    examples = {label: [] for label in banks}
    roots, factor = inv.build_factor(m)
    for rid, root in enumerate(roots):
        row = factor[root]
        ws = owner_windows(row, R)
        for label, lookup in wanted.items():
            length = len(banks[label][0])
            for start in range(n):
                arc = [ws[(start + j) % n] for j in range(length)]
                key = unoriented_orbit_key(arc, h)
                pid = lookup.get(key)
                if pid is None:
                    continue
                root_hits[label].add(rid)
                path_hits[label].add(pid)
                if len(examples[label]) < 3:
                    examples[label].append((rid, root, start, pid))
    print("FACTOR_ORBIT_CARRIER h", h, "m", m, "n", n,
          "factor_rows", len(roots))
    for label in banks:
        print(" FACTOR_RAIL", label,
              "path_count", len(banks[label]),
              "orbit_count", len(wanted[label]),
              "root_hits", len(root_hits[label]),
              "path_hits", len(path_hits[label]),
              "examples", examples[label])
    return all(root_hits.values())


def audit_all_bc_orbits(h, positive):
    """Search all monotone B/C staircases in factor or inverse-positive rows."""
    R = h + 8
    m = R - 1
    n = 2 * m + 1
    banks = all_bc_geodesic_paths(h)
    wanted = {
        label: {unoriented_orbit_key(path, h): pid
                for pid, path in enumerate(path_bank)}
        for label, path_bank in banks.items()
    }
    hits = {label: set() for label in banks}
    examples = {label: [] for label in banks}
    roots, factor = inv.build_factor(m)

    def inspect(row, source):
        ws = owner_windows(row, R)
        for label, lookup in wanted.items():
            length = len(banks[label][0])
            for start in range(n):
                arc = [ws[(start + j) % n] for j in range(length)]
                pid = lookup.get(unoriented_orbit_key(arc, h))
                if pid is None:
                    continue
                hits[label].add(source)
                if len(examples[label]) < 3:
                    examples[label].append((source, start, pid))

    if positive:
        tid = 0
        for z in inv.dyck_words(m - 2):
            for gap in range(len(z) + 1):
                a = z[:gap] + "1100" + z[gap:]
                b = z[:gap] + "1010" + z[gap:]
                for side, row in enumerate(inv.recover_inverse_trade(
                        factor[a], factor[b], m)):
                    inspect(row, (tid, side, a, b))
                tid += 1
        total = tid
        mode = "inverse-positive"
    else:
        for rid, root in enumerate(roots):
            inspect(factor[root], (rid, root))
        total = len(roots)
        mode = "canonical-factor"
    print("ALL_BC_ORBIT_CARRIER", "mode", mode, "h", h,
          "m", m, "n", n, "sources", total)
    for label in banks:
        print(" ALL_BC_RAIL", label,
              "path_count", len(banks[label]),
              "orbit_count", len(wanted[label]),
              "source_hits", len(hits[label]),
              "examples", examples[label])
    return all(hits.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("h", nargs="+", type=int)
    ap.add_argument("--all-candidates", action="store_true")
    ap.add_argument("--relabel-orbits", action="store_true")
    ap.add_argument("--factor-orbits", action="store_true")
    ap.add_argument("--all-bc-factor", action="store_true")
    ap.add_argument("--all-bc-positive", action="store_true")
    args = ap.parse_args()
    status = []
    for h in args.h:
        if args.all_bc_factor:
            status.append(audit_all_bc_orbits(h, False))
        elif args.all_bc_positive:
            status.append(audit_all_bc_orbits(h, True))
        elif args.factor_orbits:
            status.append(audit_factor_orbits(h))
        elif args.relabel_orbits:
            status.append(audit_relabel_orbits(h))
        else:
            status.append(audit(h, args.all_candidates))
    print("OVERALL", int(all(status)))


if __name__ == "__main__":
    main()
