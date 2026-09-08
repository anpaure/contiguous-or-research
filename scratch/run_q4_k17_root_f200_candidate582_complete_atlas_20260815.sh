#!/usr/bin/env bash
set -euo pipefail

cd /home/amodo/problem

artifact=/dev/shm/q4z17_fullatlas_fallback_rank1000_candidate.json
instance=/dev/shm/q4z17_reflect_sample0_root5_f208_fullatlas.dat
allowed=/dev/shm/q4z17_root_f200_candidate582_allowed_rows.txt
work=/dev/shm/q4z17_root_f200_candidate582_atlas_rows
all_catalog=/dev/shm/q4z17_root_f200_candidate582_atlas_all.tsv
new_catalog=/dev/shm/q4z17_root_f200_candidate582_atlas_new.tsv
manifest=scratch/search_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.json
audit=scratch/audit_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.json

python3 -m py_compile \
  scratch/build_q4_k17_fixed_free_complete_target_union_atlas_20260815.py \
  scratch/audit_q4_k17_fixed_free_complete_target_union_atlas_20260815.py

python3 - <<'PY'
import hashlib
import json
import sys

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    defect_graph,
    selected_vertices,
)

artifact = "/dev/shm/q4z17_fullatlas_fallback_rank1000_candidate.json"
instance = "/dev/shm/q4z17_reflect_sample0_root5_f208_fullatlas.dat"
allowed = "/dev/shm/q4z17_root_f200_candidate582_allowed_rows.txt"
with open(artifact, "rb") as stream:
    raw = stream.read()
assert hashlib.sha256(raw).hexdigest() == "c179c995c732f6854ee3478c1a5eb50f928d9bd4c86be97f12dc76f9707fc7b8"
d = json.loads(raw)
assert d["status"] == "FALLBACK_ROOT_CANDIDATE"
assert d["root_mask_hex"] == "0x1507067590d100800000000"
assert d["free_rows"] == len(d["free_rows_list"]) == 200
assert len(set(d["free_rows_list"])) == 200
assert d["cover_size"] == 20 and d["removed_pairs"] == 20
assert d["removed_self_groups"] == [] and d["eligible_self"] == 0
assert d["zero_groups"] == [] and d["zero_rows"] == []
assert d["instance"] == instance
with open(instance, "rb") as stream:
    instance_raw = stream.read()
assert hashlib.sha256(instance_raw).hexdigest() == "cc97b4fb16040c965f923e6ce9c847e254a0307693d5c2eaec0b616c601c2f3a"
assert instance_raw.splitlines()[0] == b"680 35 3749 280047"
with open(d["incumbent"], encoding="ascii") as stream:
    incumbent = json.load(stream)
_, _, self_options, pair_options = read_instance(instance)
vertices = selected_vertices(self_options, pair_options, incumbent)
_, _ = defect_graph(vertices)
root = int(d["root_mask_hex"], 16)
removed = [vertex for position, vertex in enumerate(vertices)
           if root >> position & 1]
assert len(removed) == 20
assert sum(vertex[0] == "self" for vertex in removed) == 0
assert sum(vertex[0] == "pair" for vertex in removed) == 20
outside = [0] * 680
for position, vertex in enumerate(vertices):
    if root >> position & 1:
        continue
    for row in vertex[3]:
        outside[row] += 1
assert max(outside) <= 1
replayed_free = [row for row, load in enumerate(outside) if load == 0]
assert replayed_free == d["free_rows_list"]
with open(allowed, "w", encoding="ascii") as stream:
    stream.write(" ".join(map(str, d["free_rows_list"])) + "\n")
PY

/usr/bin/time -f 'elapsed=%e maxrss_kb=%M exit=%x' \
  -o scratch/search_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.time \
  python3 scratch/build_q4_k17_fixed_free_complete_target_union_atlas_20260815.py \
  --binary /dev/shm/search_q4_k17_owner_targeted_reflection_pairs \
  --instance "$instance" \
  --allowed-rows "$allowed" \
  --expected-allowed-count 200 \
  --work-dir "$work" \
  --all-catalog "$all_catalog" \
  --new-catalog "$new_catalog" \
  --manifest "$manifest" \
  --jobs 2 --threads-per-job 40 \
  > scratch/search_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.out

python3 scratch/audit_q4_k17_fixed_free_complete_target_union_atlas_20260815.py \
  --manifest "$manifest" \
  --output "$audit" \
  > scratch/audit_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.out

sha256sum \
  "$artifact" "$instance" "$allowed" \
  scratch/build_q4_k17_fixed_free_complete_target_union_atlas_20260815.py \
  scratch/audit_q4_k17_fixed_free_complete_target_union_atlas_20260815.py \
  scratch/run_q4_k17_root_f200_candidate582_complete_atlas_20260815.sh \
  "$manifest" "$all_catalog" "$new_catalog" "$audit"

cat scratch/search_q4_k17_root_f200_candidate582_complete_atlas_20260815.h100.time
cat "$audit"
