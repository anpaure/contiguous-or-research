# Complete equivariant `K=16` residence + both-`q1` orbit model

Date: 2026-07-29
Status: exact encoding theorem and solver-free implementation audit; no solve was run.

Implementation:

* `scratch/solve_k16_complete_equivariant_residence_q1_cegar_20260729.py`
* frozen catalogue imported from
  `scratch/k16_even_necklace_q1_factor_20260729.py`

## 0. Verdict

There is an exact model for the complete fixed-label `C_15`-equivariant
factor class with no width, component, successor, voltage, or orientation
selector.  Its initial master has

\[
  27,456\text{ Boolean edge-orbit variables},\qquad
  858+764+764=2,386\text{ rows}.                 \tag{0.1}
\]

The 858 rows are weighted quotient degree-two equations.  The two sets of
764 rows are complete lower- and upper-`q1` coverage.  Strict positive
residence at least four is added by exact physical-lift CEGAR.  Every short
literal run produces a valid clause on at most four distinct edge-orbit
variables; an all-positive physical triangle is explicitly included.

This is complete for invariant two-factors under the fixed coordinate
labels.  It is not a six-width, FRR, RTR, complement-double, connected, or
unit-voltage subclass.  It does not cover non-equivariant factors.

## 1. Frozen orbit catalogue

Let `rho` rotate coordinates `0,...,14` and fix coordinate `z=15`.  The
action on the middle rank of `J(16,8)` is free.  Let `Ebar` be the set of
undirected `rho`-orbits of physical Johnson edges.  The frozen catalogue
audits

\[
 |Vbar|=858,\quad |Ebar|=27,456,\quad
 |Ebar_{AA}|=12,012,\quad |Ebar_{AB}|=3,432,\quad
 |Ebar_{BB}|=12,012.                              \tag{1.1}
\]

There are 28 quotient loops.  A loop occurs twice in its owner's incidence
list.  Thus, for `y_e in {0,1}`,

\[
  \sum_{(e,s)\in I(v)} y_e=2\qquad(v\in Vbar)     \tag{1.2}
\]

is exactly physical degree two after lifting.  Conversely, every invariant
spanning two-factor is a union of full edge orbits and satisfies (1.2).
Therefore (1.2) neither fixes nor bounds the quotient components or their
voltages.

The audited catalogue digest is

```text
e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3
```

The imported core source hash at audit time is

```text
4e86c8621f682a2df2a3721008e6a4b95c8623a9f3e69a8f32b930241938e2c6
```

Both hashes are serialized in wrapper artifacts.

## 2. Exact physical `q1` coefficients

For a lower or upper target-color orbit `O`, let `s_O=|O|`.  Every physical
edge orbit has size 15.  If one provider edge orbit is selected, each
literal target in `O` occurs exactly

\[
                         c_O=15/s_O             \tag{2.1}
\]

times.  Therefore its exact literal load is

\[
       L_O=\sum_{e:\,\operatorname{col}(e)=O}c_Oy_e,       \tag{2.2}
\]

and literal coverage is exactly `L_O>=1`.

At `K=16`, each palette has 764 target orbits.  In each palette 762 orbits
have `s_O=15,c_O=1`, and two have `s_O=5,c_O=3`.  The exceptional rows are:

| palette | top bit | canonical old masks | orbit size | coefficient | providers/orbit |
|---|---:|---|---:|---:|---:|
| lower | 1 | `3171`, `5285` | 5 | 3 | 12 |
| upper | 0 | `7399`, `11627` | 5 | 3 | 12 |

All ordinary rows have 36 provider edge orbits.  The wrapper audits (2.1)
by expanding all 15 rotations of every provider, not merely by assuming
orbit-stabilizer arithmetic.  Boolean support rows would have the same
feasible set, but the coefficient-three form is required for correct
physical load, excess, or objective ledgers.

## 3. Labelled-walk residence projection

Fix an integral solution of (1.2), lift every selected orbit, and orient a
physical factor component only for traversal.  For coordinate `a`, suppose
the cyclic indicator word contains a positive run

\[
                         0,1^ell,0,qquad 1\le ell\le3.     \tag{3.1}
\]

Let `f_0,...,f_ell` be the two boundary edges and the `ell-1` internal
edges of this labelled physical walk.  Write `bar f_i` for their fixed
edge-orbit IDs and put

\[
                         Q=\{\bar f_0,\ldots,\bar f_ell\}. \tag{3.2}
\]

Repeated orbit IDs in (3.2) are deliberately deduplicated.  Add

\[
                         \sum_{e\in Q}y_e\le |Q|-1.        \tag{3.3}
\]

Only coordinates `0` and `z=15` have to be traversed.  The old coordinates
form one rotation orbit.  Rotating a witness for old coordinate `a` to
coordinate zero sends its component to another selected component and
leaves every edge-orbit ID in `Q` unchanged.  The top coordinate is fixed
and is the second representative.  Hence these two coordinate scans produce
exactly the full projected cut set; the implementation asserts equality
against the frozen helper that scans all 16 coordinates.

### Theorem 3.1 (soundness of the projected walk cut)

Every strictly positive-resident invariant two-factor satisfies (3.3).

#### Proof

If every `y_e,e in Q`, were one, invariance would select every particular
physical edge `f_i`.  At every one-vertex in (3.1), these particular edges
already use both degree slots.  Hence the same bounded run is present in
every factor containing `Q`.  Such a factor is not resident.  Therefore a
resident factor omits at least one member of `Q`, which is (3.3).  The proof
does not require the orbit IDs in the physical walk to be distinct.  QED.

### Corollary 3.2 (constant-one triangles)

If a physical factor component is a triangle and coordinate `a` is one on
all three vertices, its cyclic trace is one run of length three.  Formula
(3.3) becomes the no-good on the distinct orbit support of its three
physical edges.  Thus the implementation uses the strict literal-cyclic
convention, not the bordered-run convention that skips monochromatic
factor cycles.

No other constant component can violate residence four: a simple
two-factor has component length at least three, and the only smaller-than-
four component is a triangle.

### Theorem 3.3 (CEGAR completeness)

Consider the loop that solves (1.2) and all `q1` rows, accepts an incumbent
only after exhaustive physical replay, and otherwise adds (3.3) for every
short run.  Then:

1. every accepted incumbent is a strict positive-resident both-`q1`
   equivariant spanning two-factor;
2. every added row is valid for every such factor;
3. an `INFEASIBLE` result is an exact nonexistence certificate inside the
   complete fixed-label equivariant catalogue;
4. `UNKNOWN` or exhaustion of a user round bound proves nothing.

#### Proof

Items 1 and 2 are the physical replay and Theorem 3.1.  Every nonresident
integral incumbent has at least one run (3.1), or a constant-one triangle,
so it violates at least one newly generated row.  Hence every round removes
the current assignment and no good assignment.  The binary master is
finite.  Therefore a solver proof of infeasibility after any number of
valid rows excludes all good assignments, while a feasible replay is a
literal witness.  A timeout or round bound supplies neither conclusion.
QED.

## 4. Executable and fail-closed behavior

The wrapper exposes:

```text
catalogue   solver-free orbit/count/coefficient audit
model       H100-only exact base-master construction
solve       H100-only exact residence CEGAR, at most 8 CPU workers
audit       solver-free exhaustive replay of a selected factor
```

There is no local-solve override.  Model construction and solving require
the frozen H100 hostname and reject worker counts above eight.  Every
incumbent checkpoint and final result is written by temporary-file rename.
The statuses are fail-closed:

* `FEASIBLE_COMPLETE_EQUIVARIANT_RESIDENT_Q1` is certifying and contains a
  replayed factor;
* `INFEASIBLE_COMPLETE_EQUIVARIANT_RESIDENCE_Q1` is certifying for precisely
  the fixed-label invariant catalogue;
* `UNKNOWN_NO_CERTIFICATE` and `ROUND_LIMIT_NO_CERTIFICATE` are explicitly
  noncertifying.

The final artifact records source hash, catalogue hash, full selected edge
IDs, decoded quotient cycles/voltages, physical components, literal `q1`
loads, short-run audit, and the CEGAR ledger.  Connectivity is never a hard
constraint.

## 5. Audited size and a regression

Before residence cuts, the script asserts the following model-proto counts:

| object | count |
|---|---:|
| Boolean variables | 27,456 |
| weighted degree equalities | 858 |
| lower-`q1` inequalities | 764 |
| upper-`q1` inequalities | 764 |
| total initial rows | 2,386 |
| all selector/auxiliary variables | 0 |

After `t` distinct projected run cuts, the model has `2,386+t` rows and
still 27,456 variables.  This dynamic statement is exact; no small a priori
claim for `t` is made.

For comparison, an eager positive-residence representation by all
connected shore sets of size at most three has 9,103,956 quotient rows:

\[
  8,534,955\quad\text{for the rotating old-coordinate family},\qquad
  569,001\quad\text{for the fixed top coordinate}.        \tag{5.1}
\]

Together with (0.1), that eager model would have 9,106,342 rows and the
same 27,456 variables.

The latter is `429+12,012+556,560`, for singleton, edge, and connected-
triple orbits.  CEGAR avoids materializing (5.1).

Here is the count audit.  One physical shore is `J(15,7)` and has

\[
  6,435+180,180+8,348,340=8,534,955             \tag{5.2}
\]

connected sets of sizes one, two, and three.  Pairing such a set with an
old coordinate makes the rotation action free, giving the first number in
(5.1).  For the top shore, singleton and edge orbit counts are respectively
`6,435/15=429` and `180,180/15=12,012`.  A connected triple can have a
nontrivial stabilizer only under the order-three rotations by five or ten.
Each fixes 30 Johnson triangles: choose the one nonconstant coordinate
3-cycle, its occupied point, and two of the other four full 3-cycles, then
divide by three,

\[
             5\cdot3\binom42/3=30.                         \tag{5.3}
\]

Burnside therefore gives

\[
             (8,348,340+30+30)/15=556,560,                 \tag{5.4}
\]

proving the second number in (5.1).

Lightweight checks performed locally:

1. `python3 -m py_compile` passed.
2. `catalogue` completed in 1.6 seconds and returned all counts and the four
   exceptional rows above.
3. Solver-free replay of
   `scratch/k16_qfactor_q1_topresident_hamilton_20260729.json` found exactly
   zero lower/upper `q1` holes, 3,390 physical short positive runs, and 226
   distinct projected orbit cuts.  The independently reconstructed cut set
   exactly equalled the frozen core helper's cut set.  That artifact is
   correctly rejected as nonresident; it was not used as positive evidence.

No CP-SAT solve or heavy local process was launched.

## 6. Relation to the 429-orbit RTR model and the blocked FRR route

The `429`-orbit RTR turn-selector uses the odd catalogue identified with the
`BB` block: 429 upper blocks, 28 choices per block, hence 12,012 pair bits
before any one-hot compression.  Its base has 429 exact-one, 429 degree,
and 335 lower-cover rows, totaling 1,193.

The exact complement-diagonal embedding is useful for comparing scope.  If
`e={X,Y}` is an odd rank-seven edge on `S=Z_15`, set

\[
 B(e)=\{z\cup X,z\cup Y\},\qquad
 A(e)=\{S\setminus X,S\setminus Y\},                       \tag{6.1}
\]

put the same selector on `A(e)` and `B(e)`, and put every `AB` selector to
zero.  Odd upper exactness and lower completeness supply all four even
`q1` classes.  Positive runs on the `BB` rail are the odd one-runs, while
positive runs on the complemented `AA` rail are the odd zero-runs.  Thus
positive residence of the even diagonal is exactly the RTR cooldown gate,
apart from the explicit component-length check for the constant top trace.
Complementation commutes with rotation, so quotient component voltages are
preserved up to the harmless fixed-section coboundary.

This diagonal is smaller because it identifies the 12,012 `AA` bits with
the 12,012 `BB` bits and deletes all 3,432 `AB` bits.  It is a sufficient
affine slice, not a WLOG normalization.  Thus:

* RTR is the smaller sufficient subclass;
* the 27,456-bit model is the stronger, complete support model for every
  fixed-label equivariant `K=16` factor;
* an RTR no-go would not refute the complete model.

The source-relative FRR joint `x/y` model has 11,928 primary variables
after its frozen blocks are removed.  Direct canonical `BB` variables are
affinely isomorphic at that scope; eliminating the redundant cut channel
gives 11,502 delta variables.  Therefore the full catalogue is not smaller
for the already restricted FRR problem.  Given the separately supplied
exact `41<60` collar obstruction, its value is scope: it restores every
`AA`, `AB`, and `BB` choice, arbitrary cross pattern, and arbitrary
component voltage without a selector blowup.  This note does not re-audit
the `41<60` certificate.

## 7. Exact boundary of the result

Proved here:

* complete fixed-label equivariant factor scope;
* exact degree and both-`q1` rows, including coefficient-three short color
  orbits;
* exact strict positive-residence CEGAR, including constant-one triangles;
* arbitrary decoded components and voltages;
* fail-closed executable semantics and audited initial counts.

Not proved:

* existence of a resident both-`q1` factor;
* non-equivariant completeness;
* zero-residence/bi-residence (the wrapper presently enforces positive runs
  only);
* connectivity, Hamiltonicity, unit voltage, or compiler feasibility;
* a small universal upper bound on the number of CEGAR rounds.
