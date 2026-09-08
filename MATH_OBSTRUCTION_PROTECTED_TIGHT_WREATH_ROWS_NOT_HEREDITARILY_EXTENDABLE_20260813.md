# Two disjoint protected tight wreath rows need not extend

**Date:** 2026-08-13  
**Status:** exact finite obstruction with a human-checkable Farkas
certificate; exhaustive small-parameter context was computed on `h100`
only

## 1. Statement

For a cyclic order `c` on `[2m+1]`, write `R(c)` for its `2m+1`
consecutive rank-`m` windows.  An exact wreath factor is a family of
`Cat_m` cyclic orders whose rows partition all rank-`m` sets.

### Theorem 1.1

At `m=3`, the two cyclic orders

\[
 \pi=(0,1,2,3,4,5,6),\qquad
 \tau=(0,2,5,1,3,6,4)
\tag{1.1}
\]

have disjoint rows, but they do not extend to an exact wreath factor.
Indeed, after prescribing them, the residual exact-cover system is
infeasible even over the nonnegative rationals.

Consequently arbitrary pairwise owner-disjoint prescribed tight rows do
**not** have a hereditary exact-wreath extension theorem.

## 2. The fourteen forced windows

The canonical row is

\[
\begin{split}
R(\pi)=\{&012,016,056,123,234,345,456\}.
\end{split}
\tag{2.1}
\]

The second row is

\[
\begin{split}
R(\tau)=\{&024,025,046,125,135,136,346\}.
\end{split}
\tag{2.2}
\]

Here, for example, `013` abbreviates the set `{0,1,3}`.  The two displayed
sets of windows are disjoint.

The twenty-one uncovered triples are

\[
\begin{split}
\mathcal U=\{&013,014,015,023,026,034,035,036,045,124,126,134,145,146,156,\\
             &235,236,245,246,256,356\}.
\end{split}
\tag{2.3}
\]

An extension would require exactly three additional wreath rows,
partitioning `mathcal U`.

## 3. A `{−1,0,1}` Farkas certificate

Give the uncovered triples the weights

\[
 y(013)=y(026)=y(124)=y(235)=-1,
\tag{3.1}
\]

\[
 y(035)=y(036)=y(256)=+1,
\tag{3.2}
\]

and give every other uncovered triple weight zero.  Thus

\[
                         \sum_{U\in\mathcal U}y(U)=-1.
\tag{3.3}
\]

There are exactly twenty unoriented wreath rows disjoint from the fourteen
forced windows.  Rooting each representative at `0`, their cyclic orders
and total `y`-weights are

\[
\begin{array}{c|rrrrrrrrrr}
c&0142563&0142635&0142653&0145263&0146235&0146253&0154263&0265143&0314526&0325614\\
\hline
y(R(c))&0&0&0&1&0&0&0&0&0&0
\end{array}
\tag{3.4}
\]

and

\[
\begin{array}{c|rrrrrrrrrr}
c&0326145&0326154&0326415&0326514&0352614&0356214&0362145&0362415&0412635&0416235\\
\hline
y(R(c))&1&0&1&1&1&1&1&1&0&0.
\end{array}
\tag{3.5}
\]

Hence every eligible residual column has nonnegative `y`-weight.  Any
nonnegative rational combination of eligible columns has nonnegative
total weight.  But exact residual coverage would give every member of
`mathcal U` load one and therefore total weight `-1` by `(3.3)`.  This is
impossible and proves Theorem 1.1.  Notice that this is stronger than a
failure of integral rounding: the protected residual face is already
rationally empty.

The enumeration in `(3.4)--(3.5)` is finite and directly checkable.  The
standard-library verifier listed in Section 5 generates all
`(7-1)!/2=360` unoriented cyclic orders and checks every assertion.

## 4. Exact small-parameter context

The H100 symmetry-reduced census fixes the canonical row and quotients
additional prescribed rows by its dihedral stabilizer.

* `m=2`: the unique disjoint-pair orbit extends.  This is the familiar
  decomposition of `K_5` into complementary five-cycles.
* `m=3`: among `121` rows disjoint from the canonical row there are `15`
  dihedral pair orbits; exactly `4` do not extend.  There are `134`
  pairwise-disjoint prescribed-triple orbits; `100` do not extend.  In
  `48` of those one can verify that each of the three prescribed pairs
  separately extends, while the triple does not.  There are `84` exact
  factors containing the canonical row.
* `m=4`: among `12,740` rows disjoint from the canonical row there are
  `777` dihedral pair orbits.  Every one of the `777` orbits extended in
  the exact CP-SAT audit, with no unknown statuses.  This is finite
  evidence, not an asymptotic theorem.

The `m=3` theorem needs none of the solver output: its certificate is
Sections 2--3.

## 5. Frozen artifacts

The human-certificate verifier is

`scratch/verify_m3_protected_wreath_pair_nogo_20260813.py`.

It uses only the Python standard library.  Its H100 transcript is

`scratch/h100_results/protected_wreath_m3_pair_nogo_certificate_20260813.txt`.

The general symmetry-reduced exact-cover audit is

`scratch/audit_protected_wreath_extension_20260813.py`,

with complete `m=2,3` JSON outputs and the sharded `m=4` output under
`scratch/h100_results/`.

## 6. Scope

This obstruction rules out the implication

\[
 \text{pairwise disjoint prescribed tight rows}
 \Longrightarrow
 \text{extendable exact wreath factor}.
\tag{6.1}
\]

It does **not** show that a tailored covariant family of clean-package
rows is nonextendable.  It also does not rule out an alternating trade,
absorber, or row rethread which changes some prescribed rows while
preserving the genuinely protected local arcs.  Those are precisely the
remaining viable mechanisms.

