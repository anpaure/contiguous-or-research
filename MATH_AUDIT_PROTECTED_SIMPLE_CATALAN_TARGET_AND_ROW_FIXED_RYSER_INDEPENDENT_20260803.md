# Independent audit: protected simple Catalan target and row-fixed Ryser transport

**Date:** 2026-08-03  
**Source audited:**
`MATH_THEOREM_PROTECTED_SIMPLE_CATALAN_TARGET_AND_ROW_FIXED_RYSER_20260803.md`  
**Source SHA-256:**
`5c18d190078df8b38e0aa70ee6bf0854617e258662caa4e2c731ca2b38bcae36`

## Verdict

**PASS.**  The simple regular Catalan target, protected-bank
avoidance threshold, row-fixed reduction to the binary-matrix interchange
theorem, and the narrowly stated immediate-upper opening consequence are
correct.  The audit found no mathematical counterexample or missing
hypothesis in those claims.

The source itself was not changed by this audit.

## 1. Degree-balancing switch

For vertices `x,y` with `d(x)>=d(y)+2`, the families

\[
 A=\{E:x\in E,\ y\notin E\},\qquad
 B=\{E:y\in E,\ x\notin E\}
\]

satisfy `|A|-|B|=d(x)-d(y)>0`.  The replacement map
`E -> E-x+y` is injective.  If every image were already an edge, it would
inject `A` into `B`, a contradiction.  Choosing a missing image therefore
preserves the number and uniformity of the edges and preserves simplicity.
The displayed quadratic-potential change is

\[
 2(d(y)-d(x)+1)<0.
\]

Thus the minimizer has degrees differing by at most one, and an integral
average forces regularity.  This proof also covers the empty and complete
families used at the endpoints.

## 2. Catalan arithmetic and current

With `v=2m-1`, `k=m+1`, and `W=binom(2m-1,m)`, direct cancellation gives

\[
 {U\over W}={m-1\over m+1},\qquad
 C=W-U={2W\over m+1}=\operatorname{Cat}_m,
 \qquad {C\over U}={2\over m-1}.
\]

Moreover

\[
 {Ck\over v}={2W\over2m-1}
 ={2\over m}{2m-2\choose m-1}
 =2\operatorname{Cat}_{m-1}.
\]

Hence the divisibility and regular degree used in Theorem 2.1 are exact;
`C<=U` is equivalent to `m>=3`.  The identities were also checked exactly
for `3<=m<=30`.

The source's derivation after (2.6) that this is the coordinate current of
two edge-disjoint perfect middle-levels matchings is correct and needs no
prior lemma.  Namely, let
`t,s : binom([v],m-1) -> binom([v],m)` be the two incidence bijections.  For
a fixed coordinate `x`, each matching uses exactly

\[
 A={2m-2\choose m-1}
\]

middle owners containing `x`.  Since the matchings are edge-disjoint,
`t(q) != s(q)` and `t(q) cap s(q)=q`; the double counts occur exactly for
the `binom(2m-2,m-2)` lower sets `q` containing `x`.  Therefore the union
rows have current

\[
 2A-{2m-2\choose m-2},
\]

which is (2.6).  This is now stated self-containedly in the audited source.

## 3. Protected-bank avoidance

For a uniform random coordinate permutation, every fixed block of the
simple regular design is uniform on the `U` upper colours.  Linearity of
expectation gives

\[
 \mathbb E|\pi(D_0)\cap F|={C|F|\over U}
 ={2|F|\over m-1}.
\]

Under the strict bound `|F|<(m-1)/2`, this is below one.  Since the
intersection size is a nonnegative integer, some permutation makes it zero.
No independence assumption is used.  Coordinate permutation preserves both
simplicity and regularity.  The `O(sqrt(m))` corollary follows for every
fixed implicit constant once `m` is sufficiently large.

The informal phrase that a colour has `m+1` rooted occurrences should define
"rooted" as the choice of its rank-`m` tail.  There are `m+1` such tail
roots and `m` possible heads for each root.  This wording does not affect
the avoidance theorem.

## 4. Row-fixed Ryser reduction

The target matrix has exactly `W=U+C` rows, every row has sum `m+1`, and
Section 2 gives the same column margins as the initial two-matching palette.
Because `D cap F` is empty, every protected colour has exactly one target
copy, so that copy can be placed on its original protected row.  Deleting
the protected rows from both matrices subtracts identical row vectors and
therefore leaves two binary matrices with equal residual row and column
margins.  The standard binary-matrix interchange theorem then gives a
sequence of `2x2` switches on residual rows only.  Restoring the deleted rows
proves Theorem 4.1 exactly.

The source now cites Theorem 1.1 of
`MATH_THEOREM_CATALAN_DUPLICATE_CURRENT_RYSER_AND_PREPARED_C6_RADO_20260803.md`.
That theorem contains the required self-contained alternating-cycle proof;
its two chord cases each reduce Hamming distance by at least two, and
reversing the switches made on the target matrix yields the required path.
No additional OR-specific lemma is needed at this abstract matrix stage.

## 5. Opening corollary and exact scope

In a literal connected realization, the projected owner graph is one cycle
whose labelled edges are the turn rows.  Every colour in `D` has two target
rows, and `D cap F` ensures that neither is protected.  Removing either such
row-edge opens the owner cycle to a spanning path while its other occurrence
still supplies the same immediate-upper colour.  Thus Corollary 4.2 is valid
as a **projected q1 opening statement**.

It does not certify survival of the removed immediate-lower row, higher-width
witnesses, residence/source guards, endpoint legality, or the physical
common-cap interface.  Those exclusions are already stated in the source;
the word "safe" should continue to be qualified by "abstract" or
"immediate-upper" whenever the corollary is cited.

## 6. Final scope check

Nothing in the audited argument constructs the colour--tail--head occurrence
selector, a literal Boolean `C6` realization of the matrix switches, a typed
capacity-faithful suffix router, or a neutral `C8` connector tree.  The exact
remaining object in (5.4) is therefore not discharged by this theorem.
