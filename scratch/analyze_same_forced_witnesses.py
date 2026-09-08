import argparse


def g(mask, m):
    before = []
    height = down_zero = 0
    for i in range(2 * m):
        before.append(height)
        if not mask >> i & 1 and height == 0:
            down_zero += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if not mask >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == down_zero + 1:
                return mask | 1 << i, i
    raise AssertionError


def hmap(mask, m):
    before = []
    height = up_one = 0
    for i in range(2 * m):
        before.append(height)
        if mask >> i & 1 and height == 1:
            up_one += 1
        height += 1 if mask >> i & 1 else -1
    seen = 0
    for i in range(2 * m):
        if mask >> i & 1 and before[i] in (0, 1):
            seen += 1
            if seen == up_one:
                return mask & ~(1 << i), i
    raise AssertionError


def flip_word(word):
    m = len(word) // 2
    mask = sum((bit == "1") << i for i, bit in enumerate(word))
    out = []
    for _ in range(m):
        mask, a = g(mask, m)
        mask, b = hmap(mask, m)
        out += [a, b]
    return out + [2 * m]


def dyck_words(m):
    out = []

    def rec(prefix, up, down):
        if len(prefix) == 2 * m:
            out.append(prefix)
            return
        if up < m:
            rec(prefix + "1", up + 1, down)
        if down < up:
            rec(prefix + "0", up, down + 1)

    rec("", 0, 0)
    return out


def tight_order(word):
    rho = flip_word(word)
    n = len(rho)
    return [rho[(2 * j) % n] for j in range(n)]


def area(word):
    height = ans = 0
    for bit in word:
        height += 1 if bit == "1" else -1
        ans += height
    return ans


def deadline(m):
    from math import comb

    k = 2 * m + 1
    r = m + 1
    w = comb(k, r)
    half = 1 << (k - 1)
    d = 0
    while d * w + d * (d + 1) // 2 < half:
        d += 1
    return d


def ordered_witness(left, right, d):
    n = len(left)
    s = (n + 1) // 2 - d
    for a in range(n):
        for b in range(n):
            direct = all(
                left[(a + j) % n] == right[(b + j) % n]
                and left[(a + s - 1 + j) % n]
                == right[(b + s - 1 + j) % n]
                for j in range(d)
            )
            if direct:
                return a, b, "direct"
            crossed = all(
                left[(a + j) % n] == right[(b + s - 1 + j) % n]
                and left[(a + s - 1 + j) % n] == right[(b + j) % n]
                for j in range(d)
            )
            if crossed:
                return a, b, "crossed"
    return None


def packet_moves(word):
    ans = []
    for v in range(len(word) - 1):
        if word[v : v + 2] != "01":
            continue
        candidates = [(v, v + 1, "01")]
        if v > 0 and word[v - 1] == "0":
            candidates.append((v - 1, v + 1, "001"))
        if v + 2 < len(word) and word[v + 2] == "1":
            candidates.append((v, v + 2, "011"))
        if (
            v > 0
            and v + 2 < len(word)
            and word[v - 1] == "0"
            and word[v + 2] == "1"
        ):
            candidates.append((v - 1, v + 2, "0011"))
        ans.extend(candidates)
    return ans


def apply_move(word, p, q):
    assert word[p] == "0" and word[q] == "1"
    return word[:p] + "1" + word[p + 1 : q] + "0" + word[q + 1 :]


def valley_region_sizes(word, v):
    assert word[v : v + 2] == "01"
    stack = []
    mate = {}
    for i, bit in enumerate(word):
        if bit == "1":
            stack.append(i)
        else:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    left_open = mate[v]
    right_close = mate[v + 1]
    left = (v - left_open - 1) // 2
    right = (right_close - (v + 1) - 1) // 2
    outside = len(word) // 2 - left - right - 2
    return left, right, outside


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("m", type=int)
    parser.add_argument("--limit", type=int, default=40)
    args = parser.parse_args()

    m = args.m
    d = deadline(m)
    roots = dyck_words(m)
    orders = {word: tight_order(word) for word in roots}
    mountain = "1" * m + "0" * m
    shown = 0
    pattern_counts = {}
    support_by_pattern = {}
    cover_by_pattern = {}
    tight_cover_by_pattern = {}
    witness_delta = {}
    aligned_change_count = {}
    aligned_change_components = {}
    aligned_max_equal_run = {}
    pattern_region_hist = {}
    no_adjacent = 0
    condition_counts = {
        pattern: [0, 0] for pattern in ("01", "001", "011", "0011")
    }
    cover_rules = {}
    region_packet_root_good = 0
    region_packet_root_bad_examples = []
    for word in roots:
        if word == mountain:
            continue
        valid = []
        valid_keys = set()
        for p, q, pattern in packet_moves(word):
            mate = apply_move(word, p, q)
            if mate not in orders or area(mate) <= area(word):
                continue
            witness = ordered_witness(orders[word], orders[mate], d)
            if witness is not None:
                valid.append((q - p, p, q, pattern, mate, witness))
                valid_keys.add((p, q, pattern))
        region_packet_found = False
        for v in range(len(word) - 1):
            if word[v : v + 2] != "01":
                continue
            left, right, outside = valley_region_sizes(word, v)
            tests = [
                ("01", outside >= d, v, v + 1),
                ("001", left >= d and v > 0 and word[v - 1] == "0", v - 1, v + 1),
                ("011", right >= d and v + 2 < len(word) and word[v + 2] == "1", v, v + 2),
                (
                    "0011",
                    outside >= d
                    and v > 0
                    and v + 2 < len(word)
                    and word[v - 1] == "0"
                    and word[v + 2] == "1",
                    v - 1,
                    v + 2,
                ),
            ]
            for key, premise, p0, q0 in tests:
                if premise:
                    condition_counts[key][0] += 1
                    condition_counts[key][1] += (p0, q0, key) in valid_keys
                    region_packet_found |= (p0, q0, key) in valid_keys
            cover = []
            if outside >= d:
                cover.append("01")
            if left >= d and v > 0 and word[v - 1] == "0":
                cover.append("001")
            if right >= d and v + 2 < len(word) and word[v + 2] == "1":
                cover.append("011")
            if (
                outside >= d
                and v > 0
                and v + 2 < len(word)
                and word[v - 1] == "0"
                and word[v + 2] == "1"
            ):
                cover.append("0011")
            cover_rules[tuple(cover)] = cover_rules.get(tuple(cover), 0) + 1
        if region_packet_found:
            region_packet_root_good += 1
        elif len(region_packet_root_bad_examples) < 20:
            region_packet_root_bad_examples.append(word)
        if not valid:
            print("NO_PACKET", word)
            continue
        valid.sort()
        gap, p, q, pattern, mate, witness = valid[0]
        valley = p if pattern in ("01", "011") else p + 1
        regions = valley_region_sizes(word, valley)
        largest = tuple(i for i, x in enumerate(regions) if x == max(regions))
        pattern_region_hist[(pattern, largest)] = (
            pattern_region_hist.get((pattern, largest), 0) + 1
        )
        pattern_counts[pattern] = pattern_counts.get(pattern, 0) + 1
        a, b, orientation = witness
        rho_left = flip_word(word)
        rho_right = flip_word(mate)
        # For a direct witness, a tight-order shift by b-a is a flip-order
        # shift by 2(b-a).  Crossed witnesses are counted separately because
        # swapping the two rails is not generally one cyclic shift.
        if orientation == "direct":
            delta = (2 * (b - a)) % len(rho_left)
            aligned_changed = [
                i
                for i in range(len(rho_left))
                if rho_left[i] != rho_right[(i + delta) % len(rho_right)]
            ]
        else:
            aligned_changed = []
        aligned_change_count[len(aligned_changed)] = (
            aligned_change_count.get(len(aligned_changed), 0) + 1
        )
        if aligned_changed:
            aset = set(aligned_changed)
            comps = sum(
                1
                for i in aligned_changed
                if (i - 1) % len(rho_left) not in aset
            )
            aligned_change_components[comps] = (
                aligned_change_components.get(comps, 0) + 1
            )
            eq = [i not in aset for i in range(len(rho_left))]
            best = run = 0
            for flag in eq + eq:
                run = run + 1 if flag else 0
                best = min(len(eq), max(best, run))
            aligned_max_equal_run[best] = aligned_max_equal_run.get(best, 0) + 1
        changed_for_choice = [
            i for i, pair in enumerate(zip(rho_left, rho_right))
            if pair[0] != pair[1]
        ]
        support_by_pattern.setdefault(pattern, []).append(len(changed_for_choice))
        if changed_for_choice:
            ordered = sorted(changed_for_choice)
            gaps = [
                (ordered[(i + 1) % len(ordered)] - ordered[i]) % len(rho_left)
                for i in range(len(ordered))
            ]
            cover_by_pattern.setdefault(pattern, []).append(
                len(rho_left) - max(gaps) + 1
            )
        changed_tight = [
            i for i, pair in enumerate(zip(orders[word], orders[mate]))
            if pair[0] != pair[1]
        ]
        if changed_tight:
            ordered_tight = sorted(changed_tight)
            gaps_tight = [
                (
                    ordered_tight[(i + 1) % len(ordered_tight)]
                    - ordered_tight[i]
                )
                % len(orders[word])
                for i in range(len(ordered_tight))
            ]
            tight_cover_by_pattern.setdefault(pattern, []).append(
                len(orders[word]) - max(gaps_tight) + 1
            )
        witness_delta[(b - a) % (2 * m + 1)] = (
            witness_delta.get((b - a) % (2 * m + 1), 0) + 1
        )
        if gap > 1:
            no_adjacent += 1
            if shown < args.limit:
                left = orders[word]
                right = orders[mate]
                s = m + 1 - d
                lrail = [left[(a + j) % len(left)] for j in range(d)]
                rrail = [
                    left[(a + s - 1 + j) % len(left)] for j in range(d)
                ]
                changed = [
                    i for i, pair in enumerate(zip(flip_word(word), flip_word(mate)))
                    if pair[0] != pair[1]
                ]
                print(
                    "LONG",
                    word,
                    "->",
                    mate,
                    "move",
                    p,
                    q,
                    pattern,
                    "witness",
                    witness,
                    "left_rail",
                    lrail,
                    "right_rail",
                    rrail,
                    "changed_rho",
                    changed,
                )
                shown += 1
    print("m", m, "d", d, "patterns", pattern_counts)
    print(
        "support_ranges",
        {key: (min(vals), max(vals)) for key, vals in support_by_pattern.items()},
    )
    print(
        "cover_ranges",
        {key: (min(vals), max(vals)) for key, vals in cover_by_pattern.items()},
    )
    print(
        "tight_cover_ranges",
        {key: (min(vals), max(vals)) for key, vals in tight_cover_by_pattern.items()},
    )
    print("witness_shift", witness_delta)
    print("aligned_change_count", aligned_change_count)
    print("aligned_change_components", aligned_change_components)
    print("aligned_max_equal_run", aligned_max_equal_run)
    print("pattern_regions", pattern_region_hist)
    print("nonadjacent_roots", no_adjacent)
    print("region_condition_hits", condition_counts)
    print("region_packet_root_good", region_packet_root_good)
    print("region_packet_root_bad_examples", region_packet_root_bad_examples)
    print("region_rule_profiles", cover_rules)


if __name__ == "__main__":
    main()
