# Exact k=13 certificate (length 1719)

## Result

`scratch/k13_res0_onehole_repair_history16x5.path_best.linear.word` is a
1719-entry word of nonzero 13-bit masks.  Its contiguous ORs contain every one
of the 8191 nonempty 13-bit masks.

SHA-256:

```text
8d202e793d3317d2c3db76fef51f9d20d0e4e09fa2899a9686285cc01f4577d0
```

For k=13, W=C(13,7)=1716 and the rank-count lower bound has d=3, so
B(13)=1719.  Therefore this word proves

```text
nu(13) = B(13) = 1719.
```

## Reproduction

The exact all-shadow, residence-safe seed consists of two physical cycles of
lengths 1547 and 169:

```sh
python3 scratch/audit_k13_disconnected_selection.py \
  scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json \
  scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.full_audit.json
```

Enumerate all cross-cycle Johnson edges and the four cut orientations.  There
are 6240 cross edges and 4277 depth-3-valid Hamilton-path splices; the best
path has just one natural lower-q1 hole and no other shadow hole:

```sh
python3 scratch/search_k13_two_cycle_path_splices.py \
  --seed scratch/k13_res0_onehole_repair_history16x5.round0.disconnected.json \
  --output scratch/k13_res0_onehole_repair_history16x5.path_splices.json \
  --keep 100
```

Compile the best middle path through the depth-3 linear OR--Pascal system:

```sh
python3 scratch/sigma_multirow_linear_compiler.py \
  scratch/k13_res0_onehole_repair_history16x5.path_splices.json \
  --k 13 --depth 3 --target-ranks 1 2 3 4 5 6 \
  --output-word scratch/k13_exact_1719.reproduced.word --timeout 300
```

Exhaustively verify all contiguous ORs and the optimal-length lower bound:

```sh
python3 scratch/sigma_sat_verify_word.py --k 13 \
  scratch/k13_res0_onehole_repair_history16x5.path_best.linear.word
```

Expected headline:

```text
PASS k=13 length=1719 covered=8191/8191
central rank=7 exact=True; counting lower bound: d=3, B(13)=1716+3=1719
```

The compact machine-readable summary is
`scratch/k13_exact_1719.certificate.json`.
