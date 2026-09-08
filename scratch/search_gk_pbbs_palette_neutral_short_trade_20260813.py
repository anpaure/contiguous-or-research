#!/usr/bin/env python3
"""Search short palette- and owner-degree-neutral switches in odd GK/PBBS.

This is an exploratory enumerator.  Old occurrences are all pairs (L,Q(L))
from the odd GK/complement factor.  A directed cycle i_0,...,i_(t-1)
means replacing (L_i,Q_i) by (L_i,Q_(i+1)).  Thus lower occurrences and
the full upper-colour multiset are preserved.  We retain only switches for
which the multiset of rank-(m+1) physical endpoints is also unchanged.

The search is rooted at one occurrence on the canonical single-soliton
cycle, so any returned switch moves one of its singleton upper colours to
an ambient lower occurrence.
"""

import argparse
import itertools
from collections import Counter, defaultdict


def masks(n, rank):
    for cc in itertools.combinations(range(n), rank):
        yield sum(1 << i for i in cc)


def unmatched(word, n):
    stack = []
    free_ones = []
    for i in range(n):
        if (word >> i) & 1:
            if stack:
                stack.pop()
            else:
                free_ones.append(i)
        else:
            stack.append(i)
    return free_ones, stack


def gk_up(word, n):
    return word | (1 << unmatched(word, n)[1][0])


def gk_down(word, n):
    return word ^ (1 << unmatched(word, n)[0][-1])


def complement_up(word, n):
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def endpoints(lower, upper):
    diff = upper ^ lower
    assert lower & ~upper == 0 and diff.bit_count() == 2
    bits = [1 << i for i in range(upper.bit_length() + 1) if diff & (1 << i)]
    return tuple(sorted((lower | bits[0], lower | bits[1])))


def rotations(word, n):
    full = (1 << n) - 1
    return [((word << s) | (word >> (n - s))) & full for s in range(n)]


def word(mask, n):
    return ''.join('1' if mask & (1 << i) else '0' for i in range(n))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('m', type=int)
    ap.add_argument('--max-half', type=int, default=4)
    ap.add_argument('--limit', type=int, default=20)
    args = ap.parse_args()
    m = args.m
    n = 2 * m + 1

    lowers = list(masks(n, m))
    uppers = []
    old_ends = []
    fibre = Counter()
    for lower in lowers:
        a = gk_up(lower, n)
        b = complement_up(lower, n)
        upper = a | b
        uppers.append(upper)
        old_ends.append(tuple(sorted((a, b))))
        fibre[upper] += 1

    # Canonical forced upper: one (m-1)-zero run and one (m+2)-one run.
    forced_upper = ((1 << (m + 2)) - 1) << (m - 1)
    roots = [i for i, upper in enumerate(uppers) if upper == forced_upper]
    assert len(roots) == 1 and fibre[forced_upper] == 1
    root = roots[0]

    # Undirected old factor components, and their change under a found switch.
    def components(edge_list):
        graph = defaultdict(list)
        for a, b in edge_list:
            graph[a].append(b)
            graph[b].append(a)
        parts = []
        part_of = {}
        for start in graph:
            if start in part_of:
                continue
            todo = [start]
            part = []
            part_id = len(parts)
            part_of[start] = part_id
            while todo:
                x = todo.pop()
                part.append(x)
                for y in graph[x]:
                    if y not in part_of:
                        part_of[y] = part_id
                        todo.append(y)
            parts.append(part)
        return parts, part_of

    old_parts, old_part_of = components(old_ends)

    by_upper = defaultdict(list)
    for j, upper in enumerate(uppers):
        by_upper[upper].append(j)

    out = []
    for lower in lowers:
        js = []
        outside = [i for i in range(n) if not lower & (1 << i)]
        for a, b in itertools.combinations(outside, 2):
            upper = lower | (1 << a) | (1 << b)
            js.extend(by_upper.get(upper, ()))
        out.append(js)
    out_sets = [set(x) for x in out]

    def neutral(cyc):
        old = Counter()
        new = Counter()
        for i in cyc:
            old.update(old_ends[i])
        for pos, i in enumerate(cyc):
            new.update(endpoints(lowers[i], uppers[cyc[(pos + 1) % len(cyc)]]))
        return old == new

    def emit(cyc):
        print('TRADE', len(cyc), 'm', m)
        for pos, i in enumerate(cyc):
            j = cyc[(pos + 1) % len(cyc)]
            print(' ', pos,
                  'L', word(lowers[i], n),
                  'oldU', word(uppers[i], n), 'old_mu', fibre[uppers[i]],
                  'newU', word(uppers[j], n),
                  'oldE', '/'.join(word(x, n) for x in old_ends[i]),
                  'newE', '/'.join(word(x, n) for x in endpoints(lowers[i], uppers[j])))
        replaced = set(cyc)
        new_edge_list = [edge for i, edge in enumerate(old_ends) if i not in replaced]
        new_edge_list += [endpoints(lowers[i], uppers[cyc[(pos + 1) % len(cyc)]])
                          for pos, i in enumerate(cyc)]
        new_parts, new_part_of = components(new_edge_list)
        touched_old = sorted({old_part_of[x] for i in cyc for x in old_ends[i]})
        touched_new = sorted({new_part_of[x] for i in cyc for x in old_ends[i]})
        print(' ', 'old_component_lengths', [len(old_parts[i]) for i in touched_old],
              'new_component_lengths', [len(new_parts[i]) for i in touched_new],
              'component_delta', len(new_parts) - len(old_parts))

    found = 0
    # Simple directed cycles rooted at root.  Canonicalize by insisting that
    # root occurs only at the beginning; reversed cycles are genuinely
    # different because the reassignment is directed.
    def dfs(path, used):
        nonlocal found
        if found >= args.limit:
            return
        last = path[-1]
        if len(path) >= 2 and root in out_sets[last]:
            if neutral(path):
                emit(path)
                found += 1
                if found >= args.limit:
                    return
        if len(path) >= args.max_half:
            return
        for nxt in out[last]:
            if nxt == root or nxt in used:
                continue
            # Avoid vacuous reassignment between duplicate occurrences of
            # the same upper colour.
            if uppers[nxt] == uppers[last]:
                continue
            used.add(nxt)
            path.append(nxt)
            dfs(path, used)
            path.pop()
            used.remove(nxt)

    dfs([root], {root})
    print('SUMMARY', 'm', m, 'occurrences', len(lowers),
          'root_out', len(out[root]), 'found', found)


if __name__ == '__main__':
    main()
