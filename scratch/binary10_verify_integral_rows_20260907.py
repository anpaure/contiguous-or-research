"""Independent exact verifier of a proposed 42-row binary10 literal cover."""
from collections import Counter
from itertools import product
import json
from pathlib import Path
import sys

data = json.loads(Path(sys.argv[1]).read_text())
rows = data["rows"]
assert len(rows) == 42
loads = Counter()
for left,right in rows:
    assert len(left) == len(right) == 5
    assert sorted(left+right) == list(range(10))
    chains = []
    for order in (left,right):
        chain = [0]
        for label in order:
            chain.append(chain[-1] | (1 << label))
        chains.append(chain)
    rectangle = {x | y for x,y in product(*chains)}
    assert len(rectangle) == 36
    loads.update(rectangle)
assert set(loads) == set(range(1024))
assert all(loads[x] == 1 for x in range(1024) if 4 <= x.bit_count() <= 6)
if "target_loads" in data:
    assert data["target_loads"] == [loads[x] for x in range(1024)]
print("PASS literal 42-row cover: all 1024 targets, tight ranks exactly once")
