# Run-boundary cores eliminate unary compiler conflicts

Date: 2026-07-30  
Lane: R, pure mathematics  
Status: unconditional structural theorem for one strict resident Johnson
chronology; quantitative compiler corollary.  No all-`k` carrier satisfying
the resulting codegree bound is claimed.

## 0. Result

Let `1<=d<r`, let `T` be a strict depth-`d`-resident Johnson chronology,
let `P` be its
maximal erosion, and form the exact negative-window candidate atlas using
the mandatory run-boundary cores.  Then:

1. every retained target/witness candidate is individually compatible;
2. source nonemptiness can never fail, for any simultaneous selector from
   the retained atlas; and
3. every minimal compiler conflict has at least two target parts.

Thus the physical conflict hypergraph has girth at least two.  Combining
this with the interval-profile transversal theorem gives a concrete
quadratic Hall criterion.  If every retained lower target has at least `M`
candidates, `M>=4`, and every target part meets at most `D_j` size-`j`
minimal conflicts, then

\[
       \max_{j\ge2}D_j\le {M^2\over16}                \tag{0.1}
\]

suffices for an exact compiler.  For an upper-complete middle permutation,
(0.1) therefore proves `nu(k)=B(k)`.

This improves the generic profile theorem by removing all singleton bad
events from the physical Johnson atlas.  It does not bound the pair or
higher codegrees.  The audited two-pin common-coordinate obstruction shows
that girth two is sharp.

## 1. Maximal erosion and mandatory cores

Fix `1<=d<r`.  Let

\[
 T=(T_0,\ldots,T_{W-1}),\qquad |T_i|=r,              \tag{1.1}
\]

be a strict Johnson path, and assume every internal positive coordinate
run has length at least `d+1`.  Put `n=W+d` and

\[
 P_p=\bigcap_{i=\max(0,p-d)}^{\min(p,W-1)}T_i
 \qquad(0\le p<n).                                    \tag{1.2}
\]

Assume `P_p` is nonempty; for a strongly resident Johnson path this follows
from `r>d`.  Residence gives

\[
                         D^dP=T.                      \tag{1.3}
\]

Use the one-sided convention at the source endpoints and define

\[
 F_p=(P_p\setminus P_{p-1})\cup(P_p\setminus P_{p+1}),\tag{1.4}
\]

where a term involving a nonexistent neighbor is omitted.

### Lemma 1.1 (run-boundary mandatory core)

For every nonzero antecedent `A` satisfying `D^dA=T`,

\[
                         F_p\subseteq A_p.            \tag{1.5}
\]

Moreover `F_p` is nonempty at every source position.

#### Proof

Work in one coordinate.  A positive run `[a,b]` in `T` erodes to the
source run

\[
 [a',b'],\qquad
 a'=\begin{cases}0,&a=0,\\a+d,&a>0,\end{cases}
 \quad
 b'=\begin{cases}W+d-1,&b=W-1,\\b,&b<W-1.
 \end{cases}                                          \tag{1.6}
\]

If `a'>0`, the central window starting at `a` contains exactly one allowed
source occurrence at the left end of this eroded run, namely `a'`; hence
that coordinate is forced into `A_(a')`.  The reversed argument forces the
coordinate at every finite right endpoint `b'`.  These are precisely the
two differences in (1.4), proving (1.5).

For a strict resident Johnson path, the erosion rank has the usual ramps
and constant interior rank `r-d`.  Consecutive interior erosion states are
distinct Johnson neighbors: equality would mean that one coordinate is
inserted and deleted again within `d` transitions, producing an internal
positive run of at most `d` states.  On either ramp consecutive ranks
differ by one.  Thus every source position is an endpoint of at least one
eroded coordinate run, so (1.4) is nonempty.  This is the coordinate form
of the proved run-boundary pair lemma.  QED.

## 2. The pruned interval atlas

Let `I_d` be the nonempty source intervals of length at most `d`.  For an
interval `I`, put

\[
 P(I)=\bigcup_{p\in I}P_p,
 \qquad
 F(I)=\bigcup_{p\in I}F_p.                           \tag{2.1}
\]

Retain a candidate `(S,I)` only when

\[
                         F(I)\subseteq S\subseteq P(I),\tag{2.2}
\]

where `S` is a strict lower target.  Condition (2.2) is necessary for every
actual witness by Lemma 1.1.

For a selected candidate family `theta`, define as usual

\[
 E_x=\{p:x\in P_p\},
 \qquad
 Q_x=E_x\setminus
       \bigcup_{(S,I)\in\theta:\,x\notin S}I.        \tag{2.3}
\]

The exact compiler conditions are:

* `Q_x` hits every central window `[i,i+d]` for `x in T_i`;
* `Q_x` hits every selected interval `I` for `x in S`; and
* every source position retains at least one coordinate.

## 3. No unary conflict theorem

### Theorem 3.1 (physical conflict girth is at least two)

In the atlas (2.2), every selected family automatically leaves every source
position nonempty, and no one-vertex selector can violate a central or
selected-target positive requirement.  Consequently every edge of the
negative-window conflict hypergraph has size at least two.

#### Proof

Fix a source position `p`.  Every selected candidate whose interval
contains `p` has label containing `F_p`, by (2.2).  Therefore intersecting
all its negative demands with `P_p` still leaves `F_p`; Lemma 1.1 gives

\[
 P_p\cap\bigcap_{(S,I)\in\theta:\,p\in I}S
 \supseteq F_p\ne\varnothing.                        \tag{3.1}
\]

Thus source nonemptiness never creates a conflict edge of any size.

A single candidate `(S,I)` cannot kill one of its own positive coordinates:
if `x in S`, that candidate makes no negative deletion of `x`, while
`S subseteq P(I)` ensures `E_x cap I` is initially nonempty.

It remains to exclude a one-candidate central failure.  Fix `x in T_i` and
let `[a,b]` be its positive run in `T` containing `i`.  Formula (1.6) says
that the allowed source positions in the central window are

\[
 R=E_x\cap[i,i+d].                                   \tag{3.2}
\]

No other eroded `x`-run meets this window: a preceding source run ends
before `i`, while a later positive run of `T` starts after `i` and its
eroded source run starts another `d` positions later, beyond `i+d`.

If `R` meets a finite endpoint of the eroded run, a candidate interval
covering `R` contains that endpoint.  Its mandatory core contains `x`, so
(2.2) forces `x in S`; such a candidate is not negative in `x`.

If `R` meets no finite eroded-run endpoint, neither side of (3.2) is
truncated by that run.  Hence

\[
                         R=[i,i+d],                   \tag{3.3}
\]

which has `d+1` positions.  One candidate interval has length at most `d`
and cannot cover it.  The same conclusion holds when the coordinate run
touches a global endpoint: either the opposite finite endpoint truncates
`R`, or (3.3) holds.  Thus no single negative candidate kills a central
positive coordinate.

All three exact failure types require at least two selected target parts,
which proves the theorem.  QED.

The theorem does not say pairwise compatibility is sufficient.  Two
negative pins can cover complementary portions of (3.2), and a positive
target requirement can likewise be killed by another target's interval.

### Theorem 3.2 (exact pair-conflict normal form)

Let `v=(S,I)` and `w=(R,J)` belong to distinct target parts of the pruned
atlas.  Then `{v,w}` is a size-two conflict edge if and only if at least one
of the following holds.

1. **Central cover.**  There are `i` and `x in T_i` such that
   
   \[
      x\notin S\cup R,
      \qquad E_x\cap[i,i+d]\subseteq I\cup J.       \tag{3.4}
   \]

2. **The target of `v` is killed by `w`.**  There is `x in S\setminus R`
   such that
   
   \[
                         E_x\cap I\subseteq J.       \tag{3.5}
   \]

3. **The target of `w` is killed by `v`.**  There is `x in R\setminus S`
   such that
   
   \[
                         E_x\cap J\subseteq I.       \tag{3.6}
   \]

In case (3.4), the allowed set is necessarily the full untruncated window

\[
                         E_x\cap[i,i+d]=[i,i+d].     \tag{3.7}
\]

In case (3.5), `E_x cap I` contains no finite endpoint of an eroded
`x`-run; the symmetric assertion holds in case (3.6).

#### Proof

Every incompatibility of the two chosen vertices must violate a central
positive row, one of their two selected-target positive rows, or source
nonemptiness.  Theorem 3.1 excludes the last possibility.  In a central
row, only candidates whose labels omit `x` delete `x`, so failure is
exactly (3.4).  If only one of the two labels omitted `x`, that one vertex
would already be a unary central conflict, contrary to Theorem 3.1.  This
also proves the displayed requirement `x notin S union R`.

For the positive row belonging to `v`, the anchor `v` does not delete a
coordinate `x in S`; the only possible deletion is by `w`.  The row fails
exactly when `x notin R` and (3.5) holds.  This is item 2, and item 3 is
symmetric.  Conversely, each of (3.4)--(3.6) violates the indicated exact
compiler row.  Since neither singleton is incompatible by Theorem 3.1,
the violating pair is inclusion-minimal and hence is a conflict edge.

For the geometric refinements, a finite endpoint `p` of an eroded `x`-run
has `x in F_p`.  Any candidate interval containing `p` must therefore have
`x` in its label and cannot delete `x`.  A central allowed set meeting such
an endpoint cannot be covered by two negative candidates.  The dichotomy
in the proof of Theorem 3.1 then forces the full-window alternative (3.7).
The same endpoint argument applied to the single negative interval `J` in
(3.5), and symmetrically to `I` in (3.6), proves the final assertion.  QED.

Thus the complete arity-two obstruction is an explicit interval-cover
graph.  What remains beyond it is not an unspecified Hall phenomenon:
`D_2` is exactly the maximum target-part degree in the graph defined by
(3.4)--(3.6), while `D_j`, `j>=3`, measure genuinely higher covers.

## 4. Quantitative compiler corollary

Restrict every target part to a nonempty candidate sublist, let

\[
 M=\min_S|L_S|,                                       \tag{4.1}
\]

and let `D_j` be the maximum, over target parts, of the number of size-`j`
minimal conflict edges incident with that part.  Theorem 3.1 gives

\[
                         D_1=0.                       \tag{4.2}
\]

The part-profile local lemma in
`MATH_THEOREM_R_ALLK_INTERVAL_CONFLICT_PROFILE_TRANSVERSAL_20260730.md`
states that, when conflict girth is at least `g`, `M>=4`, and

\[
                D_j\le {1\over4}(M/2)^g
                \qquad(j\ge g),                      \tag{4.3}
\]

an independent full transversal exists.  Taking `g=2` gives (0.1).

### Corollary 4.1 (quadratic run-boundary Hall criterion)

Let `T` be an upper-complete, strict depth-`d`-resident permutation of the
middle layer.  If the pruned atlas has at least `M>=4` candidates per lower
target and

\[
                         D_j\le M^2/16
                         \qquad(2\le j\le r),         \tag{4.4}
\]

then one nonzero antecedent covers every lower target and

\[
                         \nu(k)=B(k).                 \tag{4.5}
\]

#### Proof

Theorem 3.1 and (4.4) satisfy the profile local lemma, so the candidate
hypergraph has a full independent transversal.  The exact negative-window
criterion constructs one common nonzero antecedent `A` with `D^dA=T` and
all lower witnesses.  Upper completeness lifts every upper owner interval
to `A`.  The deadline lower bound supplies equality.  QED.

The sharper sufficient constant before the simplification `M>=4` is

\[
                  D_j\le {M(M-2)\over8}.             \tag{4.6}
\]

## 5. Sharp scope and certificate audit

1. The theorem is fixed-chronology and integral.  Random selection appears
   only in the proof of existence of one deterministic interval selector.
2. It proves no lower bound on `M` and no upper bound on `D_j` for PBBS or
   Pascal candidates.  Those are now the exact quantitative tasks.
3. Girth two is sharp.  The resident `k=6` two-pin example has two
   individually feasible candidates whose negative intervals jointly erase
   the last two occurrences of one central coordinate.
4. The authenticated `k=11,13,15` flat words provide actual independent
   transversals and hence are consistent with the theorem.  The sufficient
   quadratic inequality need not hold for arbitrary sublists extracted from
   those words.
5. The length-`B(16)+1` certificate does not determine a named flat
   chronology or candidate atlas and therefore gives no implication in
   either direction.

The exact remaining positive theorem suggested by (4.4) is concrete:
construct a resident upper-complete chronology whose mandatory-core-pruned
target lists have quadratic expansion, in the sense that every conflict
part-degree is `O(M^2)` with constant below `1/16`.  Conversely, a scoped
negative result against this sufficient route must exhibit either empty
parts or a family of pair/higher conflict banks violating this expansion;
unary obstruction is now excluded by the run-boundary geometry itself.
