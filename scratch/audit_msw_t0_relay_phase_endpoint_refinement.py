#!/usr/bin/env python3
"""Refined phase/endpoint all-width audit for the frozen T0 relay.

Each canonical owner occurrence is named by (root, owner-position).  Its
phase is owner-position parity.  Each linear colour interval records its
width, first phase, first and last owner occurrence, and whether its two
cuts are at a path endpoint.  The rethreaded paths inherit occurrence names
from owners, while inserted colours sit between their literal endpoint
occurrences.

Heavy use belongs on h100 only.
"""

from collections import Counter, defaultdict

import audit_msw_t0_relay_linear_allwidth as base


def canonical_named(m: int):
    selected = set()
    owner_names = defaultdict(list)
    for root in range(1 << (2 * m)):
        if root.bit_count() != m or not base.dyck(root, m):
            continue
        x = root
        owner_names[x].append((root, 0))
        for j in range(m):
            y = base.g(x, m)
            nx = base.hmap(y, m)
            selected.add((x, y))
            selected.add((nx, y))
            owner_names[nx].append((root, j + 1))
            x = nx
    assert all(len(v) == 1 for v in owner_names.values())
    return selected, {o: names[0] for o, names in owner_names.items()}


def named_paths(selected, names):
    adj = defaultdict(list)
    for owner, colour in selected:
        adj[(0, owner)].append((1, colour))
        adj[(1, colour)].append((0, owner))
    endpoints = [v for v, ns in adj.items() if len(ns) == 1]
    seen = set()
    out = []
    for start in endpoints:
        if start in seen:
            continue
        vertices = []
        prev = None
        cur = start
        while True:
            seen.add(cur)
            vertices.append(cur)
            nxt = [z for z in adj[cur] if z != prev]
            if not nxt:
                break
            prev, cur = cur, nxt[0]
        assert vertices[0][0] == vertices[-1][0] == 0
        owners = [z[1] for z in vertices if z[0] == 0]
        colours = [z[1] for z in vertices if z[0] == 1]
        assert len(owners) == len(colours) + 1
        # The MSW z-free path has a canonical orientation: forward endpoint
        # (root position 0) to reverse endpoint (root position m).  The T0
        # relay preserves all endpoints and re-pairs forward with reverse.
        left_pos = names[owners[0]][1]
        right_pos = names[owners[-1]][1]
        if {left_pos, right_pos} == {0, 6} and left_pos == 6:
            owners.reverse()
            colours.reverse()
        out.append((owners, colours))
    assert len(seen) == len(adj)
    return out


def refined_deck(paths, names, m):
    result = Counter()
    coarse_type = Counter()
    for owners, colours in paths:
        for q in range(1, len(colours) + 1):
            for i in range(len(colours) - q + 1):
                value = 0
                for z in colours[i : i + q]:
                    value |= z
                first = names[owners[i]]
                last = names[owners[i + q]]
                first_phase = first[1] & 1
                cuts = (i == 0, i + q == len(colours))
                sig = (q, first_phase, first, last, cuts)
                result[(value, sig)] += 1
                coarse_type[(value, q, first_phase, cuts)] += 1
    return result, coarse_type


def owner_edges(paths):
    out = set()
    for owners, _ in paths:
        for a, b in zip(owners, owners[1:]):
            out.add(tuple(sorted((a, b))))
    return out


def reverse_path(path):
    owners, colours = path
    return (list(reversed(owners)), list(reversed(colours)))


def common_phase(old_paths, new_paths):
    adj = defaultdict(set)
    for a, b in owner_edges(old_paths) | owner_edges(new_paths):
        adj[a].add(b)
        adj[b].add(a)
    phase = {}
    odd_cycle = None
    for start in adj:
        if start in phase:
            continue
        phase[start] = 0
        stack = [start]
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if b not in phase:
                    phase[b] = phase[a] ^ 1
                    stack.append(b)
                elif phase[b] == phase[a]:
                    odd_cycle = (a, b)
                    return None, odd_cycle
    return phase, None


def refined_with_phase(paths, names, m, phase):
    result = Counter()
    cuts_only = Counter()
    phase_only = Counter()
    for owners, colours in paths:
        for q in range(1, len(colours) + 1):
            for i in range(len(colours) - q + 1):
                value = 0
                for z in colours[i : i + q]:
                    value |= z
                first, last = owners[i], owners[i + q]
                cuts = (i == 0, i + q == len(colours))
                sig = (q, phase[first], names[first], names[last], cuts)
                result[(value, sig)] += 1
                cuts_only[(value, q, cuts)] += 1
                phase_only[(value, q, phase[first])] += 1
    return result, cuts_only, phase_only


def lifted_clock_support(paths, phase, h):
    """Support of (base OR, lifted width, literal clock union).

    Expand every base owner occurrence v to the ordered clock block
    D_0,...,D_h in phase 0 and D_h,...,D_(2h)=D_0 in phase 1, exactly as in
    (2.5) of the phase-clock theorem.  Then enumerate every nonempty linear
    interval of lifted owners.  Base coordinates and clock coordinates are
    retained separately.
    """
    full_clock = (1 << (2 * h)) - 1

    def dset(t):
        t %= 2 * h
        return sum(1 << ((t + j) % (2 * h)) for j in range(h))

    support = set()
    witnesses = {}
    for pid, (owners, _) in enumerate(paths):
        lifted = []
        for owner in owners:
            if phase[owner] == 0:
                ts = range(0, h + 1)
            else:
                ts = range(h, 2 * h + 1)
            for t in ts:
                lifted.append((owner, dset(t), t))
        for i in range(len(lifted)):
            base_or = clock_or = 0
            for j in range(i, len(lifted)):
                base_or |= lifted[j][0]
                clock_or |= lifted[j][1]
                key = (base_or, j - i + 1, clock_or)
                support.add(key)
                first_block = i // (h + 1)
                last_block = j // (h + 1)
                witnesses.setdefault(
                    key,
                    (
                        pid,
                        i,
                        j,
                        tuple(x[2] for x in lifted[i : j + 1]),
                        first_block,
                        last_block,
                        i % (h + 1),
                        j % (h + 1),
                        len(owners),
                    ),
                )
                if clock_or == full_clock and base_or == (1 << 12) - 1:
                    # Longer extensions can still change width, so do not stop.
                    pass
    return support, witnesses


def lifted_clock_support_all_witnesses(paths, phase, h):
    def dset(t):
        t %= 2 * h
        return sum(1 << ((t + j) % (2 * h)) for j in range(h))

    support = defaultdict(list)
    for pid, (owners, _) in enumerate(paths):
        lifted = []
        for block, owner in enumerate(owners):
            ts = range(0, h + 1) if phase[owner] == 0 else range(h, 2 * h + 1)
            for offset, t in enumerate(ts):
                lifted.append((owner, dset(t), t, block, offset))
        for i in range(len(lifted)):
            base_or = clock_or = 0
            for j in range(i, len(lifted)):
                base_or |= lifted[j][0]
                clock_or |= lifted[j][1]
                key = (base_or, j - i + 1, clock_or)
                support[key].append(
                    (
                        pid,
                        lifted[i][3],
                        lifted[j][3],
                        lifted[i][4],
                        lifted[j][4],
                        phase[lifted[i][0]],
                        tuple(x[2] for x in lifted[i : j + 1]),
                    )
                )
    return support


def lifted_one_path_support(path, phase, h):
    support, _ = lifted_clock_support([path], phase, h)
    return support


def owner_interval_signatures(paths, phase):
    support = set()
    witness = {}
    for pid, (owners, _) in enumerate(paths):
        for i in range(len(owners)):
            value = 0
            for j in range(i, len(owners)):
                value |= owners[j]
                key = (value, j - i + 1, phase[owners[i]])
                support.add(key)
                witness.setdefault(key, (pid, i, j))
    return support, witness


def stratified_base_signatures(paths, phase):
    """Finite all-h sufficient signatures.

    A span of >=3 owner blocks has one complete middle clock block, whose
    D_0..D_h (or reverse) union is all U.  Only spans of one or two blocks
    retain phase-sensitive endpoint clock geometry.
    """
    support = set()
    witness = {}
    for pid, (owners, _) in enumerate(paths):
        for i in range(len(owners)):
            value = 0
            for j in range(i, len(owners)):
                value |= owners[j]
                s = j - i + 1
                if s >= 3:
                    key = ("long", value, s)
                else:
                    # Actual endpoint offsets are chosen only after clock
                    # dilation.  At base level retain the phase word; the
                    # same offsets then give the same K_h.
                    key = (
                        "short",
                        value,
                        s,
                        tuple(phase[o] for o in owners[i : j + 1]),
                    )
                support.add(key)
                witness.setdefault(key, (pid, i, j))
    return support, witness


def main():
    m = 6
    selected, names = canonical_named(m)
    old_paths = named_paths(selected, names)
    old, old_coarse = refined_deck(old_paths, names, m)

    h1 = [
        ("101010001101", "101011001101", "101010001111"),
        ("100011001101", "100011001111", "101011001101"),
        ("100010001111", "101010001111", "100011001111"),
    ]
    h2 = [
        ("101011000101", "101011010101", "101011001101"),
        ("101001010101", "101001011101", "101011010101"),
        ("101001001101", "101011001101", "101001011101"),
    ]
    for owner, minus, plus in h1 + h2:
        em = (base.bits(owner), base.bits(minus))
        ep = (base.bits(owner), base.bits(plus))
        assert em in selected and ep not in selected
        selected.remove(em)
        selected.add(ep)

    new_paths = named_paths(selected, names)
    print(
        "endpoint_type_hist old=",
        dict(sorted(Counter(tuple(sorted((names[o[0]][1], names[o[-1]][1])))
                            for o, _ in old_paths).items())),
        "new=",
        dict(sorted(Counter(tuple(sorted((names[o[0]][1], names[o[-1]][1])))
                            for o, _ in new_paths).items())),
    )
    new, new_coarse = refined_deck(new_paths, names, m)

    phase, odd = common_phase(old_paths, new_paths)
    print("common_phase_exists=", phase is not None, "conflict_edge=", odd)
    if phase is not None:
        old_edge_bank = owner_edges(old_paths)
        new_edge_bank = owner_edges(new_paths)
        affected_old = []
        for pid, path in enumerate(old_paths):
            if any(e not in new_edge_bank for e in owner_edges([path])):
                affected_old.append(pid)
        affected_new = []
        for pid, path in enumerate(new_paths):
            if any(e not in old_edge_bank for e in owner_edges([path])):
                affected_new.append(pid)
        print(
            "affected_old_paths=", affected_old,
            "endpoint_types=",
            [
                (names[old_paths[p][0][0]][1], names[old_paths[p][0][-1]][1])
                for p in affected_old
            ],
        )
        print(
            "affected_new_paths=", affected_new,
            "endpoint_types=",
            [
                (names[new_paths[p][0][0]][1], names[new_paths[p][0][-1]][1])
                for p in affected_new
            ],
        )
        print("affected_old_detail")
        for p in affected_old:
            print(
                " ", p,
                "owners", [format(o, f"0{2*m}b")[::-1] for o in old_paths[p][0]],
                "names", [names[o] for o in old_paths[p][0]],
                "length", len(old_paths[p][1]),
            )
        print("affected_new_detail")
        for p in affected_new:
            print(
                " ", p,
                "owners", [format(o, f"0{2*m}b")[::-1] for o in new_paths[p][0]],
                "names", [names[o] for o in new_paths[p][0]],
                "length", len(new_paths[p][1]),
            )
        assert len(affected_new) <= 10
        for h in (2, 3):
            so, _ = lifted_clock_support(old_paths, phase, h)
            trials = []
            for mask in range(1 << len(affected_new)):
                trial = list(new_paths)
                for j, pid in enumerate(affected_new):
                    if mask >> j & 1:
                        trial[pid] = reverse_path(trial[pid])
                sn, _ = lifted_clock_support(trial, phase, h)
                trials.append((len(so - sn), mask, len(sn)))
            trials.sort()
            print(
                "orientation_search h=", h,
                "best=", trials[: min(16, len(trials))],
            )
            old_fixed = set()
            for pid, path in enumerate(old_paths):
                if pid not in affected_old:
                    old_fixed |= lifted_one_path_support(path, phase, h)
            new_fixed = set()
            for pid, path in enumerate(new_paths):
                if pid not in affected_new:
                    new_fixed |= lifted_one_path_support(path, phase, h)
            old_opts = [
                (
                    lifted_one_path_support(old_paths[p], phase, h),
                    lifted_one_path_support(reverse_path(old_paths[p]), phase, h),
                )
                for p in affected_old
            ]
            new_opts = [
                (
                    lifted_one_path_support(new_paths[p], phase, h),
                    lifted_one_path_support(reverse_path(new_paths[p]), phase, h),
                )
                for p in affected_new
            ]
            joint = []
            for omask in range(1 << len(affected_old)):
                os = set(old_fixed)
                for j, opts in enumerate(old_opts):
                    os |= opts[(omask >> j) & 1]
                for nmask in range(1 << len(affected_new)):
                    ns = set(new_fixed)
                    for j, opts in enumerate(new_opts):
                        ns |= opts[(nmask >> j) & 1]
                    joint.append((len(os - ns), omask, nmask, len(os), len(ns)))
            joint.sort()
            print(
                "joint_orientation_search h=", h,
                "best=", joint[: min(20, len(joint))],
            )
        # The best non-complementary orientation reverses affected paths
        # 0 and 2 in both closures.  Test its fiberwise support for a longer
        # clock range without repeating the exhaustive mask search.
        for h in range(2, 13):
            opaths = list(old_paths)
            npaths = list(new_paths)
            for j in (0, 2):
                opaths[affected_old[j]] = reverse_path(opaths[affected_old[j]])
                npaths[affected_new[j]] = reverse_path(npaths[affected_new[j]])
            so, _ = lifted_clock_support(opaths, phase, h)
            sn, _ = lifted_clock_support(npaths, phase, h)
            print(
                "chosen_orientation_support h=", h,
                "old=", len(so),
                "new=", len(sn),
                "loss=", len(so - sn),
                "birth=", len(sn - so),
            )
        opaths = list(old_paths)
        npaths = list(new_paths)
        for j in (0, 2):
            opaths[affected_old[j]] = reverse_path(opaths[affected_old[j]])
            npaths[affected_new[j]] = reverse_path(npaths[affected_new[j]])
        bs_old, bw_old = owner_interval_signatures(opaths, phase)
        bs_new, bw_new = owner_interval_signatures(npaths, phase)
        bs_loss = sorted(bs_old - bs_new, key=lambda z: (z[1], z[0], z[2]))
        bs_birth = sorted(bs_new - bs_old, key=lambda z: (z[1], z[0], z[2]))
        print(
            "base_owner_interval_signature",
            "old=", len(bs_old),
            "new=", len(bs_new),
            "loss=", len(bs_loss),
            "birth=", len(bs_birth),
        )
        for key in bs_loss[:20]:
            print("  LOSS", key, "old_witness", bw_old[key])
            value, blocks, start_phase = key
            alternatives = sorted(
                (
                    k[1],
                    k[2],
                    bw_new[k],
                )
                for k in bs_new
                if k[0] == value
            )
            print("    NEW_SAME_VALUE_ALTERNATIVES", alternatives)
        # For the five coarse signature mismatches, inspect exactly how
        # endpoint offsets compensate the opposite starting phase in the
        # lifted clock.  h=6 is large enough to expose the affine pattern.
        h_probe = 6
        ow_all = lifted_clock_support_all_witnesses(opaths, phase, h_probe)
        nw_all = lifted_clock_support_all_witnesses(npaths, phase, h_probe)
        for coarse in bs_loss:
            value, blocks, start_phase = coarse
            print("  OFFSET_COMPENSATION coarse=", coarse)
            records = []
            for key, oldws in ow_all.items():
                if key[0] != value:
                    continue
                for ow in oldws:
                    if ow[2] - ow[1] + 1 != blocks or ow[5] != start_phase:
                        continue
                    newws = nw_all.get(key, [])
                    if not newws:
                        continue
                    records.append((key[1], key[2], ow, newws[:8]))
            records.sort(key=lambda z: (z[0], z[1], z[2]))
            for rec in records[:50]:
                width, clock, ow, nws = rec
                print(
                    "   width", width,
                    "K", format(clock, f"0{2*h_probe}b")[::-1],
                    "old", ow,
                    "new", nws,
                )
        changed_old_keys = [
            k for k, w in bw_old.items() if w[0] in affected_old
        ]
        mate_location_hist = Counter(
            (
                bw_old[k][0],
                bw_new[k][0] in affected_new,
                bw_new[k][0],
            )
            for k in changed_old_keys
            if k in bw_new
        )
        print("  changed_signature_mate_hist", dict(sorted(mate_location_hist.items())))
        st_old, sw_old = stratified_base_signatures(opaths, phase)
        st_new, sw_new = stratified_base_signatures(npaths, phase)
        st_loss = sorted(st_old - st_new, key=str)
        st_birth = sorted(st_new - st_old, key=str)
        print(
            "stratified_base_signature",
            "old=", len(st_old),
            "new=", len(st_new),
            "loss=", len(st_loss),
            "birth=", len(st_birth),
        )
        for key in st_loss[:40]:
            print("  LOSS", key, "old_witness", sw_old[key])
        # Freeze the short-span certificate as literal OR maps.  Singleton
        # owners are common by construction.  For two blocks, the finite
        # condition is support inclusion of (A|B, phase(A)); the phase word
        # is automatically (p,1-p).
        short_old = {
            (owners[i] | owners[i + 1], phase[owners[i]])
            for owners, _ in opaths
            for i in range(len(owners) - 1)
        }
        short_new = {
            (owners[i] | owners[i + 1], phase[owners[i]])
            for owners, _ in npaths
            for i in range(len(owners) - 1)
        }
        print(
            "oriented_two_block_certificate",
            "old=", len(short_old),
            "new=", len(short_new),
            "loss=", len(short_old - short_new),
            "birth=", len(short_new - short_old),
        )
        for value, p in sorted(short_old - short_new):
            print(
                "  LOSS",
                format(value, f"0{2*m}b")[::-1],
                "phase", p,
            )
        # Print the complete changed old/new two-block OR maps.  Unchanged
        # edges are literal and need no certificate row.
        common_edges = owner_edges(opaths) & owner_edges(npaths)
        print("changed_old_oriented_edges")
        for pid, (owners, _) in enumerate(opaths):
            for i, (a, b) in enumerate(zip(owners, owners[1:])):
                if tuple(sorted((a, b))) in common_edges:
                    continue
                print(
                    " ", pid, i,
                    format(a, f"0{2*m}b")[::-1],
                    "->", format(b, f"0{2*m}b")[::-1],
                    "phase", phase[a],
                    "OR", format(a | b, f"0{2*m}b")[::-1],
                )
        print("changed_new_oriented_edges")
        for pid, (owners, _) in enumerate(npaths):
            for i, (a, b) in enumerate(zip(owners, owners[1:])):
                if tuple(sorted((a, b))) in common_edges:
                    continue
                print(
                    " ", pid, i,
                    format(a, f"0{2*m}b")[::-1],
                    "->", format(b, f"0{2*m}b")[::-1],
                    "phase", phase[a],
                    "OR", format(a | b, f"0{2*m}b")[::-1],
                )
        ro, co, po = refined_with_phase(old_paths, names, m, phase)
        rn, cn, pn = refined_with_phase(new_paths, names, m, phase)
        for label, aa, bb in (
            ("derived_exact", ro, rn),
            ("derived_cuts_only", co, cn),
            ("derived_phase_only", po, pn),
        ):
            loss = [(k, z, bb[k]) for k, z in aa.items() if bb[k] < z]
            print(label, "old_types=", len(aa), "new_types=", len(bb),
                  "loss_types=", len(loss),
                  "loss_units=", sum(z - zz for _, z, zz in loss))
            for k, z, zz in loss[:12]:
                value = k[0]
                print("  LOSS", format(value, f"0{2*m}b")[::-1],
                      "old/new", z, zz, "signature", k[1:])
        for h in (2, 3):
            so, wo = lifted_clock_support(old_paths, phase, h)
            sn, wn = lifted_clock_support(new_paths, phase, h)
            loss = sorted(so - sn, key=lambda z: (z[1], z[0], z[2]))
            print(
                "fiberwise_clock_support",
                "h=", h,
                "old=", len(so),
                "new=", len(sn),
                "loss=", len(loss),
            )
            hist_width = Counter(k[1] for k in loss)
            hist_clock = Counter(k[2] for k in loss)
            hist_span = Counter(
                (
                    wo[k][5] - wo[k][4],
                    wo[k][6],
                    wo[k][7],
                    wo[k][4] == 0,
                    wo[k][5] == wo[k][8] - 1,
                )
                for k in loss
            )
            hist_pid = Counter(wo[k][0] for k in loss)
            print("  width_hist", dict(sorted(hist_width.items())))
            print(
                "  clock_hist",
                {
                    format(k, f"0{2*h}b")[::-1]: v
                    for k, v in sorted(hist_clock.items())
                },
            )
            print("  span_cut_hist", dict(sorted(hist_span.items())))
            print("  old_path_hist", dict(sorted(hist_pid.items())))
            for key in loss[:20]:
                value, width, clock = key
                print(
                    "  LOSS",
                    format(value, f"0{2*m}b")[::-1],
                    "lifted_width", width,
                    "clock", format(clock, f"0{2*h}b")[::-1],
                    "old_witness", wo[key],
                )
            print("  affected_old_paths")
            for pid in sorted(hist_pid):
                owners = old_paths[pid][0]
                print(
                    "   ", pid,
                    "owners=", [format(o, f"0{2*m}b")[::-1] for o in owners],
                    "names=", [names[o] for o in owners],
                    "phases=", [phase[o] for o in owners],
                )

    exact_loss = [(k, z, new[k]) for k, z in old.items() if new[k] < z]
    coarse_loss = [
        (k, z, new_coarse[k]) for k, z in old_coarse.items() if new_coarse[k] < z
    ]
    print(
        "exact_occurrence_signature",
        "old_types=", len(old),
        "new_types=", len(new),
        "loss_types=", len(exact_loss),
        "loss_units=", sum(z - zz for _, z, zz in exact_loss),
    )
    for (value, sig), z, zz in exact_loss[:50]:
        print(
            "  LOSS",
            format(value, f"0{2*m}b")[::-1],
            "old/new", z, zz,
            "sig", sig,
        )
    print(
        "coarse_phase_cut_signature",
        "old_types=", len(old_coarse),
        "new_types=", len(new_coarse),
        "loss_types=", len(coarse_loss),
        "loss_units=", sum(z - zz for _, z, zz in coarse_loss),
    )
    for (value, q, phase, cuts), z, zz in coarse_loss[:50]:
        print(
            "  LOSS",
            format(value, f"0{2*m}b")[::-1],
            "old/new", z, zz,
            "q", q,
            "phase", phase,
            "cuts", cuts,
        )


if __name__ == "__main__":
    main()
