# Three-run endpoint cycles: exact normal form and finite obstruction

Date: 2026-07-29

Status: theorem plus exhaustive, search-free audit at `k=9,11`; the same
sparse signature filter is run at `k=15`.  No `k=15` word is claimed.

Artifacts:

```text
scratch/audit_strict_spiral_three_run_cycles_20260729.py
scratch/strict_spiral_three_run_cycle_audit_20260729.json
```

## 1. Exact move

Let the coordinate-zero trace of a strict spiral have `N` cyclic one-runs.
Unwrap them in order as

\[
[s_i,e_i],\qquad i\in\mathbb Z_N,
\]

and require run length at least `d+1` and a nonempty gap.  Thus the legal
interval for an end is

\[
I_i=[s_i+d,\ s_{i+1}-2].                       \tag{1.1}
\]

Choose distinct runs `i,j,l`, one of the two cyclic orientations
`sigma=(i j l)`, and new endpoints satisfying

\[
e'_a\in I_a,qquad
e'_a\equiv e_{\sigma(a)}\pmod N,qquad
e'_i+e'_j+e'_l=e_i+e_j+e_l.                   \tag{1.2}
\]

Only the three run ends move.

### Theorem 1.1 (three-run end-cycle normal form)

Every move satisfying (1.2) preserves:

1. the run-start residue permutation;
2. the run-end residue permutation;
3. the total number of ones and every residue-class sum modulo `N`;
4. minimum residence `d+1` and nonempty gaps;
5. rank `r` at every reconstructed middle position;
6. one deletion and one insertion at every Johnson seam, hence q1 rank.

It need not preserve distinctness of the middle masks or distinctness of the
q1 masks.

### Proof

Starts do not move and the three end residue classes are permuted.  The final
equation in (1.2) preserves the total number of ones.  If `h_a` is the number
of trace ones in residue class `a mod N`, then `h_(a+1)-h_a` is the number of
starts across that residue seam minus the number of ends across it.  Both
numbers remain one, so all `h_a` remain equal; their total fixes the common
value at `r`.  The interval constraints in (1.1) give residence and a
nonempty gap.  The run-transversal seam identity then gives exactly one
entering and one leaving coordinate.  Orbit injectivity is global and is not
part of this local calculation.  □

This is the first move strictly beyond a two-run transposition while keeping
the eager c-space algebra exact.

## 2. Sparse exact signature

If one trace bit at position `p` flips, equivariance changes at most the `k`
middle positions

\[
p+(xv^{-1}\bmod k)N,qquad x\in\mathbb Z_k.    \tag{2.1}
\]

For a move flipping `f` trace bits, collect these at most `kf` positions and
recompute only their middle masks.  The original carrier contains every
middle mask once.  Therefore the modified carrier contains every middle mask
once if and only if

\[
\operatorname{Counter}(\text{new masks on affected positions})
=\operatorname{Counter}(\text{old masks on affected positions}). \tag{2.2}
\]

Only edges incident with affected positions can change.  Applying the same
counter identity to their intersections is necessary and sufficient for the
q1 rainbow.  Thus (2.2) and its q1 copy are an **exact** signature filter,
not a heuristic.  Its cost is proportional to the changed support, not `W`.

The script fully replays every candidate, including all 4,037 at `k=15`, and
compares the sparse and full middle/q1 ledgers.  They agree exactly.

## 3. Sparse generator

For each ordered run pair `(i,j)`, store every legal endpoint in `I_i` with
residue `e_j mod N`, labelled by displacement `delta=e'_i-e_i`.  This gives a
directed compatibility graph.  A legal three-run move is a directed triangle

```text
i -> j -> l -> i
```

whose three displacement labels sum to zero.  Hashing the closing arc by
displacement enumerates moves in

\[
O\!\left(\sum_j d^-(j)d^+(j)\right)
\]

instead of `O(N^3)`.  This is the scalable `k=15` generator requested by the
audit.

## 4. Exact census

The first arc count below includes the one identity reassignment at each run;
identity arcs are never used inside a three-cycle on distinct runs.

| case | arcs incl. identity | nonidentity arcs | legal 3-cycles | strict middle+q1 survivors |
|---|---:|---:|---:|---:|
| solved `k=9` | 83 | 69 | **27** | **0** |
| solved `k=11` | 294 | 252 | **131** | **0** |
| resident `k=15` seed | **4,719** | 4,290 | **4,037** | **0** |

Every candidate retains the correct middle and q1 ranks.  Failure is purely
orbit collision.

The closest signatures are:

| case | middle duplicates | q1 duplicates | moved runs | endpoint displacements |
|---|---:|---:|---|---|
| `k=9` | 9 | 9 | `(0,7,12)` | `(2,-1,-1)` |
| `k=11` | 11 | 22 | `(14,21,29)` | `(-1,2,-1)` |
| `k=15` | 15 | 30 | `(89,149,207)` | `(1,1,-2)` |

Thus even the closest move replaces at least one entire middle rotation
orbit.  The exact signed middle/q1 orbit signature is different for every
candidate (`27`, `131`, and `4,037` distinct joint signatures), and no
signature has its inverse in the same move catalogue.  Consequently two
3-cycles with disjoint reconstructed q1 halos and commuting boundary effects
cannot cancel by a simple inverse-signature pair.  Disjoint trace-run labels
alone do not imply this additivity after equivariant lifting.  Overlapping
moves remain nonlinear and are not ruled out by this statement.

## 5. Downstream comparison

There are no strict-carrier survivors, so there is no legitimate q2/upper/
compiler improvement in this neighborhood.  For diagnostic completeness,
the unique closest candidate in each case was evaluated after retaining its
known middle/q1 defect:

| case | q1 holes | q2 holes | terminal erosion holes | new upper holes | new compiler zero-degree targets |
|---|---:|---:|---:|---:|---:|
| `k=9` | +9 | +18 | +18 at `q=d=2` | +18 | +18 |
| `k=11` | +22 | +11 | +0 at `q=d=3` | +0 | +0 |
| `k=15` | +30 | +15 | +0 at `q=d=3` | +20 | +0 |

These rows are deliberately not called candidate carriers.  They show that
the nearest orbit substitution does not expose a hidden local repair: at
best it preserves the terminal compiler ledger while damaging the mandatory
middle/q1 ledger.

## 6. Consequence for the next neighborhood

The exact sequence of negative results is now:

```text
one balanced two-run transposition: no strict survivor;
one balanced three-run end cycle:  no strict survivor;
inverse pair of 3-cycle signatures: none.
```

This end-only slice must not be enlarged blindly.  The complete coupled
start/end support-at-most-three atlas is analyzed separately in
`MATH_THEOREM_COUPLED_RUN_SUPPORT_THREE_TWO_DECK_GIRTH_20260729.md`; it closes
all rectangles and coupled three-run overlays at the resident `k=15` seed.
Any next bounded search must therefore begin at boundary support four, or use
a genuinely extensive move such as the audited MMM shear, and impose middle
and q1 conservation before q2/q3 scoring.

For `k=15`, the generator already reduces the raw `N^3` space to 4,037 exact
moves.  Store for each its sparse signed vector

\[
(\Delta M,\Delta L_1,\Delta L_2,\Delta L_3,\Delta U),
\]

bucket first by `(Delta M,Delta L_1)`, and only score q2/q3/upper/compiler
inside a zero bucket.  The present audit proves that no singleton bucket is
zero and no two buckets are simple inverses.  That is the correct starting
point for a bounded multi-move C++ implementation.

## 7. Reproduction

```bash
python3 scratch/audit_strict_spiral_three_run_cycles_20260729.py
```

Current hashes:

```text
3a490101dc0d79d6ed504d954e4604150d2df1af7ea5f4f6f1c44a5ee2400165  script
bbeadffb2669c95f09924a941959c80ad51e3a5c76c30a541252da325aad4e31  audit JSON
```
