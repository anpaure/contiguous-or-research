#!/usr/bin/env python3
"""Exact graph audit of the sixteen leading zero-avoidance atoms."""

from itertools import combinations


def cycle_edges(r: int) -> set[tuple[int, int]]:
    b = 2 * r + 1
    return {
        tuple(sorted((x, (x + step) % b)))
        for x in range(b)
        for step in (1, 3)
    }


def full_vertex_edge_covers(
    vertices: set[int], graph_edges: set[tuple[int, int]]
) -> list[tuple[tuple[int, int], ...]]:
    induced = [edge for edge in graph_edges if set(edge) <= vertices]
    answer = []
    for size in range(2, len(induced) + 1):
        for chosen in combinations(induced, size):
            if {x for edge in chosen for x in edge} == vertices:
                answer.append(chosen)
    return answer


def main() -> None:
    for r in range(6, 81):
        b = 2 * r + 1
        assert (-2 * r) % b in (1, b - 1)
        assert (-2 * (r - 1)) % b in (3, b - 3)
        assert (-2 * (r - 2)) % b == 5

        graph_edges = cycle_edges(r)
        root_vertices = {0, 5}
        vertex_sets = []
        blocker_terms = []
        path_sets = []
        for extra in combinations([x for x in range(b) if x not in root_vertices], 2):
            vertices = root_vertices | set(extra)
            covers = full_vertex_edge_covers(vertices, graph_edges)
            if covers:
                vertex_sets.append(vertices)
                blocker_terms.extend(covers)
                sizes = sorted(len(chosen) for chosen in covers)
                assert sizes in ([2], [2, 3])
                if sizes == [2, 3]:
                    path_sets.append(vertices)
        assert len(vertex_sets) == 16
        assert len(blocker_terms) == 22
        assert len(path_sets) == 6

        omitted = {tuple(sorted((0, 1))), tuple(sorted((0, 3)))}

        def local_terms(event_start: int):
            first = (-2 * event_start) % b
            second = (first + 5) % b
            roots = {first, second}
            terms = []
            for extra in combinations([x for x in range(b) if x not in roots], 2):
                vertices = roots | set(extra)
                terms.extend(full_vertex_edge_covers(vertices, graph_edges))
            return terms

        assert not any(omitted & set(term) for term in local_terms(3))
        for event_start in (0, r + 3):
            for term in local_terms(event_start):
                assert len(omitted & set(term)) <= 1

    expected_paths = {
        frozenset(values)
        for values in (
            (-1, 0, 2, 5),
            (0, 1, 2, 5),
            (0, 1, 4, 5),
            (0, 2, 3, 5),
            (0, 3, 4, 5),
            (0, 3, 5, 6),
        )
    }
    line_edges = {
        tuple(sorted((x, x + step)))
        for x in range(-8, 10)
        for step in (1, 3)
    }
    actual_paths = set()
    actual_sets = set()
    for extra in combinations([x for x in range(-8, 11) if x not in (0, 5)], 2):
        vertices = {0, 5, *extra}
        covers = full_vertex_edge_covers(vertices, line_edges)
        if covers:
            actual_sets.add(frozenset(vertices))
            if sorted(len(chosen) for chosen in covers) == [2, 3]:
                actual_paths.add(frozenset(vertices))
    assert len(actual_sets) == 16
    assert actual_paths == expected_paths

    print(
        "GATE_B_ZERO_AVOIDANCE_SIXTEEN_LOCAL_ATOMS_PASS "
        "coordinate_map=PASS cycle_r=6..80 atoms=16 terms=22 paths=6 "
        "puncture_states=PASS"
    )


if __name__ == "__main__":
    main()
