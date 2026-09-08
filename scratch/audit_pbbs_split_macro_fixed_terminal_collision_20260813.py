#!/usr/bin/env python3
"""Audit C_h/J_h against all high pentagon owners/facets."""


def main():
    cases = 0
    for r in range(8, 501):
        owners = []
        facets = []
        terminals = []
        terminal_facets = []
        for h in range(4, r):
            G = set(range(h + 2, 2 * h + 1)) | set(range(2 * h + 4, 2 * r + 1, 2))
            X = [
                {0, h + 1, 2 * h + 2},
                {h + 1, 2 * h + 1, 2 * h + 2},
                {2, h + 1, 2 * h + 1},
                {0, 2, h + 1},
                {0, 1, h + 1},
            ]
            Y = [
                {0, 1, 2 * h + 2},
                {0, 2 * h + 1, 2 * h + 2},
                {2, 2 * h + 1, 2 * h + 2},
                {0, 2, 2 * h + 1},
                {0, 1, 2},
            ]
            P = [frozenset(G | x) for x in X]
            Q = [frozenset(G | y) for y in Y]
            owners += [(v, h, "P", i) for i, v in enumerate(P)]
            owners += [(v, h, "Q", i) for i, v in enumerate(Q)]
            facets += [(P[i] & Q[i], h, "old", i) for i in range(5)]
            facets += [(P[i] & Q[(i + 1) % 5], h, "new", i) for i in range(5)]
            terminals.append((frozenset(G | {0, h + 1, 2 * h + 1}), h))
            terminal_facets.append((frozenset(G | {0, 2 * h + 1}), h))

        owner_map = {v: (h, kind, i) for v, h, kind, i in owners}
        facet_map = {v: (h, kind, i) for v, h, kind, i in facets}
        for value, h in terminals:
            assert value not in owner_map, (r, h, owner_map[value])
        for value, h in terminal_facets:
            assert value not in facet_map, (r, h, facet_map[value])
        assert len({v for v, _ in terminals}) == len(terminals)
        assert len({v for v, _ in terminal_facets}) == len(terminal_facets)
        cases += len(terminals)
    print("PASS_PBBS_SPLIT_MACRO_CJ_COLLISION", "r=8..500", f"height_cases={cases}")


if __name__ == "__main__":
    main()
