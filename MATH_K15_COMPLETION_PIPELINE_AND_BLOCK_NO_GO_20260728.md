# k=15 completion pipeline and the fixed-block no-go

## 1. Audited near-carrier

The exact cyclic replacement

```
scratch/k15_uniform444_h8_exact.factor.json
sha256 f17ed7623a9cbf82c8572b36d6f1248a6497723ffec74365d63d94c24026f132
```

has zero lower and upper holes at every depth `q=1,...,7`.  Its replacement
vertices have zero depth-three residence defects; only old physical cycle 14
has 15 defects.

The joint seam artifact

```
scratch/k15_joint_h8_plusc14.path.json
sha256 67d0b26d6547cd6c2f7467c99b12362ac1645ff4b9d4abfffa2dd7bbe2d529c2
```

repairs cycle 14 and the replacement simultaneously.  It gives 17 resident
paths on 5340 vertices and retains all upper targets.  It is not yet a full
middle path: the other 14 clean old cycles contain 1095 vertices.

## 2. Exact fixed-block no-go

`scratch/search_k15_full_block_order.py` makes the downstream completion
problem finite and exact.  Its states are

* the two orientations of each of the 17 resident paths; and
* every cut and both orientations of each of the 14 clean cycles.

It chooses one state per block and one global ordering.  A transition may be
**any** seam between rank-eight endpoints, not just a Johnson edge, provided
the seam is locally depth-three resident.  The weakest meaningful coverage
model asks only that upper `q=1` remain hole-free.  Thus this model is much
more permissive than the final theorem.

The result is nevertheless exact UNSAT:

```
scratch/k15_full_block_order_allseams_q1.cnf
sha256 31aabd7f9d13e0ac0c2a586a7b044be716917bfe0244e09997a9e4889e5b2a7c

scratch/k15_full_block_order_allseams_q1.kissat.out
sha256 e51871cc66ece87c6cc0f88a842e019b78a9111c477831967e93c97677dfaa5d

s UNSATISFIABLE
process time 0.60 s
```

Consequently no choice of cuts, orientations, or residence-safe downstream
seams can turn these fixed block interiors into the required middle path while
even preserving only the first upper shadow.  Internal carrier edges must
change jointly.  This rules out treating path-count slack as a substitute for
linear realizability.

## 3. Final input contract

The compiler can start only from a JSON artifact containing

```
middle_paths (or middle_components)
```

which partitions all 6435 rank-eight masks.  Before compilation it must pass:

1. zero depth-three residence defects on every path;
2. zero upper holes at all depths `q=1,...,7`; and
3. an ordering/orientation into one length-6435 sequence whose maximal linear
   erosion `P` satisfies `D^3 P = T`.

`scratch/order_k15_resident_paths.py` performs item 3 using arbitrary added
seams, so upper coverage can only improve.  It independently rejects a path
family whose endpoint geometry cannot be linearized.

## 4. One-command finish

Once a valid full path family exists, run

```sh
python3 scratch/finish_k15_certificate.py FULL_PATHS.json \
  --prefix scratch/k15_exact_6438
```

The script:

1. orders and orients the paths by lazy exact SAT;
2. checks the exact all-lower Hall graph at ranks 1 through 7;
3. builds the global depth-three compiler CNF;
4. sends both heavy SAT jobs to the CPU-only `h100` host;
5. decodes a word of length 6438; and
6. exhaustively verifies all `2^15-1 = 32767` nonempty contiguous OR masks,
   including the exact rank-eight `D^3` row.

The underlying compiler now supports deterministic `--build-only`,
`--cnf-output`, and `--model-file` modes, so remote solving and local decoding
use exactly the same variable map.  Heavy SAT does not run on the workstation.

## 5. Current precise gate

The lower Hall/compiler and final exhaustive verifier are ready but cannot yet
be invoked honestly: there is no full 6435-vertex linear-resident exact-upper
path.  The remaining carrier search must enforce internal rerouting together
with endpoint compatibility.  A residence-zero path cover alone is not a
sufficient certificate.
