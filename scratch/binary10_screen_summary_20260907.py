"""Read a durable all-60 screen and classify genuinely different feasible cores."""
from collections import Counter, defaultdict
import importlib.util
import json
from pathlib import Path
import sys

run = Path(sys.argv[1])
records = json.loads((run/"summary.json").read_text())
spec = importlib.util.spec_from_file_location("saved_core",run/"binary10_involution_matching_core_20260907.py")
core = importlib.util.module_from_spec(spec)
spec.loader.exec_module(core)
lower, matchings = core.all_fixed_matchings()
statuses, feasible = Counter(), defaultdict(list)
for record in records:
    lines = record["summary"]
    lp = next((line for line in lines if line.startswith("LP_STATUS")),None)
    status = f"LP_{lp.split()[1]}" if lp else "NO_LP"
    statuses[status] += 1
    if status != "LP_0":
        continue
    f = dict(zip(lower,(31^b for b in matchings[record["index"]])))
    lengths, todo = [], set(lower)
    while todo:
        start = min(todo)
        current, length = start, 0
        while current in todo:
            todo.remove(current)
            length += 1
            current = f[current]
        assert current == start
        lengths.append(length)
    feasible["+".join(map(str,sorted(lengths)))].append(record["index"])
print("STATUS_COUNTS",dict(statuses))
print("FEASIBLE_BY_CYCLE_TYPE",dict(feasible))
def rotate(mask):
    return ((mask << 1) & 31) | (mask >> 4)
for index in feasible.get("2+2+2+2+2", []):
    f = dict(zip(lower,(31^b for b in matchings[index])))
    if all(f[rotate(a)] == rotate(f[a]) for a in lower):
        print("C5_INVARIANT_MATCHING_INDEX",index)
for name, representative in core.MATCHINGS.items():
    print("NAMED_REPRESENTATIVE_INDEX",name,matchings.index(representative))
