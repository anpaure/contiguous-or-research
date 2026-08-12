# K16 H1 outside-column reset and joint13 face-halo fold theorem

Date: 2026-07-30  
Status: **proved solver-independent normalization strictly beyond joint13**

## 1. Authenticated source and residual hypergraph

Let `x` be the authenticated length-12,873 H1 word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
```

with sole hole

```text
H = 0x2c6d.
```

Let

```text
S = {0,1,4486,4487,4488,4489,6438,6439,6440,
     12869,12870,12871,12872}
```

be the frozen joint13 support.  Resetting the complement of `S` to `x`
leaves the exact 55-target residual family `R` authenticated in

```text
scratch/ad_k16_h1_four_portal_geometry_20260730.audit.json.
```

Every target outside `R` has a fixed source witness disjoint from `S`.
The full joint13 fibre is solver-independently impossible by
`MATH_THEOREM_K16_H1_JOINT13_RQC_GUARD_LADDER_UNSAT_20260730.md`.

For a nonzero value `v`, define its exact residual incidence column

```text
Gamma(v) = {T in R : v is a submask of T}.                         (1.1)
```

This is the column of residual targets in whose literal interval witnesses a
cell of value `v` is even eligible to occur.

## 2. Arbitrary-position residual-column reset

Consider an outside edit at position `p`, from source value `a=x[p]` to
`v=y[p]`.  Call it **column-reset-safe** if either

```text
Gamma(v) is empty,                                                  (2.1)
```

or

```text
v is a submask of a  and  Gamma(v)=Gamma(a).                        (2.2)
```

Condition (2.2) can equivalently be written

```text
v subseteq a  and  Gamma(v) subseteq Gamma(a),
```

because `v subseteq a` gives the reverse incidence inclusion automatically.

### Theorem 2.1 (simultaneous outside-column reset)

Let `y` be any same-length word with arbitrary values on `S` and an arbitrary
number of edits outside `S`.  If every outside edit is column-reset-safe,
then every residual target covered by `y` is covered by its source-reset
projection `pi_S(y)`.  Consequently, a universal `y` in this class would
normalize into the impossible joint13 fibre.  No such universal `y` exists.

#### Proof

Fix `T in R` and a literal `y`-witness interval `I` for `T`.  A cell value on
`I` is a submask of `T`.  Hence an edited cell satisfying (2.1) cannot occur
on `I` at all.

For every edited cell on `I` satisfying (2.2), `v subseteq T` implies
`T in Gamma(v)=Gamma(a)`, so

```text
v subseteq a subseteq T.
```

Simultaneously resetting all such cells therefore removes no bit from the
old interval OR and adds only bits already in `T`.  The same literal interval
still has OR exactly `T` after every outside reset.

Every target outside `R` has its fixed source witness disjoint from `S`.
Thus if `y` were universal, `pi_S(y)` would be universal.  The joint13
obstruction gives the contradiction.  This proof is independent of edit
positions, edit count, and the choices on `S`.  \(\square\)

### Exact size of the value class

Direct enumeration of (1.1) gives

```text
|{v != 0 : Gamma(v)=empty}| = 57,304,
|{v != 0 : Gamma(v)!=empty}| =  8,231.
```

Thus 87.4% of all nonzero 16-bit values are position-independent zero-
incidence values.  Their upward-closed family has exactly 59 inclusion-
minimal generators:

```text
weight 2 :  7
weight 3 : 22
weight 4 : 30.
```

The seven pair generators are

```text
0x0012, 0x0102, 0x0104, 0x0110, 0x0300, 0x1010, 0x8100.
```

The complete 59-row list and its payload digest are in the audit.  Beyond
these zero-incidence values, the authenticated source has 26,114 strict
same-column submask choices across 5,341 of the 12,860 outside positions,
with at most 29 at one position.  Depending on the source value, each outside
position has between 57,303 and 57,333 admissible **changed** values under
Theorem 2.1.

The exact escape alternative sharpened by this theorem is:

> Every universal same-length word must have an outside edit `p` with
> `Gamma(y[p])` nonempty for which either `y[p]` is not a submask of `x[p]`,
> or its residual incidence column differs from that of `x[p]`.

This is a necessary condition only; one such unsafe edit is not sufficient
for universality.

## 3. Six-face chart-equivalent halo folding

There are six exterior faces of the four joint13 blocks:

| anchor in `S` | outward ray inside the fixed gap |
|---:|:---|
| 1 | `2,3,...,4485` |
| 4486 | `4485,4484,...,2` |
| 4489 | `4490,4491,...,6437` |
| 6438 | `6437,6436,...,4490` |
| 6440 | `6441,6442,...,12868` |
| 12869 | `12868,12867,...,6441` |

On any face `f`, choose a possibly empty consecutive halo `D_f` beginning at
the first displayed outside cell.  Halos from opposite ends of one gap must
be disjoint.  Let `e_f` be the face anchor and put

```text
Q_f = {y[e_f]} union {y[p] : p in D_f},
W_f = OR(Q_f).                                                       (3.1)
```

Assume:

1. all values `q in Q_f` have one exact incidence column `Gamma_f`;
2. if `Gamma_f` is nonempty, then

   ```text
   OR(x[p] : p in D_f) is a submask of W_f;                         (3.2)
   ```

3. apart from `S`, the chosen face halos, and any disjoint edits covered by
   Theorem 2.1, the word agrees with `x`.

Define the fold `F(y)` by resetting every halo to its source values, replacing
each face anchor by `W_f`, retaining the other values on `S`, and resetting
the disjoint column-safe edits.  Then `F(y)` differs from `x` only on `S`.

### Theorem 3.1 (chart-equivalent face-halo fold)

Under assumptions 1--3, every residual target covered by `y` is covered by
`F(y)`.  Hence no universal word exists in this strictly wider support class.

#### Proof

First apply Theorem 2.1 to the disjoint column-safe edits.  It preserves every
literal residual witness on the same interval.

Fix a remaining `T in R` witness interval `I`.  Since

```text
Gamma(W_f) = intersection_{q in Q_f} Gamma(q) = Gamma_f,            (3.3)
```

a face with empty `Gamma_f` cannot meet `I`.  If a nonempty-column face meets
`I`, then `T in Gamma_f`, so every value in `Q_f`, their OR `W_f`, and by
(3.2) every reset source halo value are submasks of `T`.

If `I` meets `D_f` but not its anchor, extend the appropriate endpoint of
`I` through the rest of that halo to `e_f`.  This adds no other face: a halo
is contiguous and directly attached to its own anchor.  In the folded word,
the included anchor `W_f` restores every old halo contribution.  Reset halo
values and newly traversed source values add only submasks of `W_f subseteq
T`.  If `I` already met the anchor, replacing its value by `W_f` has the same
effect without extending the interval.

Perform these endpoint extensions for every met face.  The resulting object
is still one interval and has OR exactly `T`.  All nonresidual targets have
fixed source witnesses after the fold, so universality of `y` would imply a
universal joint13 word, contradicting the known obstruction.  \(\square\)

This is genuinely wider than a constant-copy fold: values on one face may be
unequal.  What matters is equality of their exact 55-row chart-incidence
columns, not equality of the masks.

### Concrete audited 38-cell support region

The longest consecutive source-dominated halos with nonempty incidence
columns on the six faces have widths

```text
5,4,4,3,4,5,
```

namely 25 outside cells:

```text
[2,6], [4482,4485], [4490,4493],
[6435,6437], [6441,6444], [12864,12868].
```

Together with `S`, this is a 38-cell allowed support region.  The audit gives
every face unequal values from one exact incidence class, changes 31 cells,
and folds them to six changed anchors in `S`.  Every residual witness present
in that stress word is replayed through the explicit endpoint map.

Theorem 3.1 allows shorter halos, arbitrary legal values within their common
columns, arbitrary choices on all thirteen joint13 cells, and arbitrary
additional disjoint edits satisfying Theorem 2.1.  The 38-cell instance is a
checkable witness to strict support enlargement, not a limit on the theorem.

## 4. Exact counterexample to unqualified adjacent OR folding

The hypothesis on incidence columns cannot be replaced by the rule “OR an
outside cell into the adjacent collar cell and reset it.”  At the right face
of the second block,

```text
e = 4489,  x[e] = 0x2261,
p = 4490,  x[p] = 0x2245.
```

Change only `p` to `H=0x2c6d`.  The interval `[4490,4490]` is then an exact
`H` witness.  The naive OR fold gives

```text
z[e] = 0x2261 OR 0x2c6d = 0x2e6d,
z[p] = 0x2245.
```

Both displayed folded cells contain the bit `0x0200`, which is absent from
`H`.  Therefore an `H` interval in `z` would have to avoid both positions.
Such an interval is literally an interval of the authenticated source, which
has no `H` witness.  Thus the OR fold destroys the singleton witness.

The three relevant incidence-column sizes are respectively

```text
|Gamma(0x2261)| = 14,
|Gamma(0x2c6d)| = 4,
|Gamma(0x2e6d)| = 1.
```

Their mismatch is exactly what Theorem 3.1 forbids.  This counterexample is
not universal; it refutes only the proposed unconditional fold rule.

## 5. Independent audit and scope

The audit independently reconstructs the authenticated one-hole coverage,
the 65,480/55 fixed-residual split, all 65,535 incidence columns, the complete
zero-incidence up-set, every positionwise same-column strict submask, and the
six face rays.  It then performs:

* one simultaneous 5,343-edit column-reset stress replay;
* one unequal-value 25-outside-cell face-halo fold replay;
* the exact adjacent OR-merge counterexample above.

```text
scratch/audit_k16_h1_joint13_outside_column_halo_fold_20260730.py
SHA-256 f0a60194003d4e61dadf54055adf8b281cc4b45a0c5be5ad5b7334eb354db365

scratch/k16_h1_joint13_outside_column_halo_fold_20260730.audit.json
SHA-256 ce4cef475854c66b0c9aff6673947e4032bf24e8c174ab74ea829d4a1db7f124
payload SHA-256 574996f8d393f87b419a84f77494b3985b474774239071848ca5e7cc03996276
```

The results are source-relative and use the already proved joint13
obstruction.  They do not normalize an arbitrary live-column outside edit,
an arbitrary nonconsecutive halo, or an arbitrary relocation.  Therefore
they do not prove unrestricted length-12,873 UNSAT.  The exact bracket
remains

```text
12873 <= nu(16) <= 12874.
```
