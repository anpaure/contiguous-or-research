"""Necessary integral census relaxation, not an integral grid cover."""

import argparse
import json
from pathlib import Path

from ortools.sat.python import cp_model

from q4int_verify_20260906_f7a91 import DUAL12


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('--seconds', type=float, default=60)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = [list(map(int, line.split())) for line in Path(args.input).read_text().splitlines()]
    n, k = data[0]
    populations = data[1:1+n]
    columns = data[1+n:]
    assert len(columns) == k
    model = cp_model.CpModel()
    x = [model.new_int_var(0, 1248//c[0], f'x{i}') for i, c in enumerate(columns)]
    for j, population in enumerate(populations):
        lhs = sum(c[2+j]*v for c, v in zip(columns, x))
        if DUAL12.get(tuple(population[:4]), 0):
            model.add(lhs == population[4])
        else:
            model.add(lhs >= population[4])
    model.add(sum(c[0]*v for c, v in zip(columns, x)) == 1248)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = 4
    status = solver.solve(model)
    result = {'scope': 'necessary census relaxation only; not an integral chain-pair cover',
              'status': solver.status_name(status), 'columns': k, 'orbits': n, 'walltime': solver.wall_time}
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        result['counts'] = [{'shape_line': c[1], 'multiplicity': solver.value(v), 'cost': c[0]}
                            for c, v in zip(columns, x) if solver.value(v)]
        assert sum(row['multiplicity']*row['cost'] for row in result['counts']) == 1248
        for j, population in enumerate(populations):
            actual = sum(c[2+j]*solver.value(v) for c, v in zip(columns, x))
            assert actual >= population[4]
            if DUAL12.get(tuple(population[:4]), 0):
                assert actual == population[4]
    Path(args.output).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result), flush=True)
