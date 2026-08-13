#!/usr/bin/env python3
import argparse
from collections import defaultdict
from ortools.sat.python import cp_model


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("output")
    parser.add_argument("--seconds", type=float, default=600.0)
    args = parser.parse_args()

    options = []
    with open(args.input) as source:
        head = source.readline().split()
        assert head[0] == "H"
        m, d, n, vertices, root, expected = map(int, head[1:])
        for line in source:
            tag, child, parent, oc, a, op, b = line.split()
            assert tag == "O"
            options.append(tuple(map(int, (child, parent, oc, a, op, b))))
    assert len(options) == expected

    by_child = defaultdict(list)
    by_vertex_port = defaultdict(list)
    for index, (child, parent, oc, a, op, b) in enumerate(options):
        by_child[child].append(index)
        by_vertex_port[child, a].append(index)
        by_vertex_port[parent, b].append(index)
    assert len(by_child) == vertices - 1 and root not in by_child

    model = cp_model.CpModel()
    take = [model.new_bool_var(f"x_{i}") for i in range(len(options))]
    orientation = [model.new_bool_var(f"o_{v}") for v in range(vertices)]
    for index, (child, parent, oc, a, op, b) in enumerate(options):
        model.add(orientation[child] == oc).only_enforce_if(take[index])
        model.add(orientation[parent] == op).only_enforce_if(take[index])
    for child, indices in by_child.items():
        model.add_exactly_one(take[index] for index in indices)

    used = {}
    for key, indices in by_vertex_port.items():
        variable = model.new_bool_var(f"y_{key[0]}_{key[1]}")
        model.add_max_equality(variable, [take[index] for index in indices])
        used[key] = variable

    constraint_count = 0
    for vertex in range(vertices):
        for start in range(n):
            variables = []
            for offset in range(d + 1):
                variable = used.get((vertex, (start + offset) % n))
                if variable is not None:
                    variables.append(variable)
            if len(variables) >= 2:
                model.add_at_most_one(variables)
                constraint_count += 1

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_workers = 64
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    has_solution = status in (cp_model.OPTIMAL, cp_model.FEASIBLE)
    selected = (
        [index for index, variable in enumerate(take) if solver.boolean_value(variable)]
        if has_solution
        else []
    )
    with open(args.output, "w") as out:
        out.write(
            f"status={solver.status_name(status)} m={m} d={d} n={n} "
            f"vertices={vertices} options={len(options)} constraints={constraint_count} "
            f"selected={len(selected)} objective={solver.objective_value}\n"
        )
        for index in selected:
            out.write("S %d %d %d %d %d %d %d\n" % ((index,) + options[index]))
    print(open(args.output).readline().strip())


if __name__ == "__main__":
    main()
