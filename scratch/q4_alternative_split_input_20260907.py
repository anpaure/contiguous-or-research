"""Emit the existing witness for the exact alternative-split C++ test."""
from importlib.util import spec_from_file_location, module_from_spec
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
root = Path(__file__).resolve().parent
spec = spec_from_file_location("checker", root/"q4int_verify_20260906_f7a91.py")
checker = module_from_spec(spec)
spec.loader.exec_module(checker)
raw = (root/"q4int_final1280_witness_20260906_f7a91.json").read_bytes()
assert sha256(raw).hexdigest() == "bbe7dfcd84b4dffebbae82142ed90f90ddda20d8ee4b137a0b62170a14945f36"
data = json.loads(raw)
rows = data["rectangles"]
print(len(rows))
print(*(checker.weight12(tuple((p>>(2*i))&3 for i in range(6))) for p in range(4096)))
for row in rows:
    points = set()
    for c, d in product(row["C"],row["D"]):
        p = sum(value<<(2*axis) for axis,value in zip(row["left"]+row["right"],c+d))
        points.add(p)
    split = sum(1<<i for i in row["left"])
    if not(split&1):split ^=63
    print(len(row["C"])+len(row["D"]),split,len(points),*sorted(points))
