"""Literal A.7.1 position census. Run only on the authorized h100 host."""
import json
import pathlib
import socket
import sys
from fractions import Fraction

assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 execution required'

# MASTER_HANDOFF.md, A.7.1: unchanged literal fourteen-row template.
rows = [
    ("0461", "5723"), ("0473", "2651"), ("0674", "3152"),
    ("0726", "1435"), ("1507", "4263"), ("1605", "7432"),
    ("2104", "6375"), ("2150", "7463"), ("3206", "7154"),
    ("3210", "4567"), ("3617", "5204"), ("4302", "6157"),
    ("5034", "6721"), ("5426", "7301"),
]
for left, right in rows:
    assert len(left) == len(right) == 4
    assert sorted(left + right) == list('01234567')

census = []
for coordinate in '01234567':
    counts = [0, 0, 0, 0]
    positions = []
    for left, right in rows:
        shore = left if coordinate in left else right
        position = shore.index(coordinate) + 1
        positions.append(position)
        counts[position - 1] += 1
    count_sum = sum(counts)
    weighted_sum = sum(p * n for p, n in enumerate(counts, 1))
    assert count_sum == 14
    assert weighted_sum == 35
    imbalance = counts[3] - counts[0]
    assert abs(imbalance) <= 3
    census.append({
        'coordinate': int(coordinate), 'positions_by_row': positions,
        'position_counts': counts, 'sum_counts': count_sum,
        'sum_position_times_count': weighted_sum,
        'n4_minus_n1': imbalance,
        'aggregate_central_gradient': str(-Fraction(2, 3) * imbalance),
    })

maximum = max(abs(item['n4_minus_n1']) for item in census)
report = {
    'host': socket.gethostname(),
    'source': 'MASTER_HANDOFF.md A.7.1 literal fourteen rows',
    'rows': rows,
    'census': census,
    'maximum_absolute_imbalance': maximum,
    'maximizing_coordinates': [item['coordinate'] for item in census
                               if abs(item['n4_minus_n1']) == maximum],
    'all_constraints_pass': True,
}
encoded = json.dumps(report, indent=2) + '\n'
pathlib.Path(sys.argv[1]).write_text(encoded)
print(encoded, end='')
