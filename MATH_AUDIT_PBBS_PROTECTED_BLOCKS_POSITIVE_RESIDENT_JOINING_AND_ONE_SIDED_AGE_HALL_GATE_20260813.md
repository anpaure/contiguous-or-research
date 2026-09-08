# Audit of protected-block positive joining and the one-sided age-Hall gate

**Date:** 2026-08-13  
**Audited source:**
`MATH_REDUCTION_PBBS_PROTECTED_BLOCKS_POSITIVE_RESIDENT_JOINING_AND_ONE_SIDED_AGE_HALL_GATE_20260813.md`  
**Source SHA-256:**
`a7aac640b32e505fb2578c0e22f0a0ef79d5ed1facc4ef865d3049426e0bc6ae`  
**Method:** independent coordinate-run, release/deadline, matching-phase,
and quantifier audit; no computation or search  
**Verdict:** **PASS after scope corrections.**  The source is an exact
one-sided chronology reduction.  It does not yet co-select
schedule-compatible resource-disjoint paths for the full protected bank,
prove the one-sided Hall system, or retain the untouched/deep compiler
deck.

## 1. The maximal-antecedent indexing is exact

For

\[
 P_p=\bigcap_{a=0}^{d}T_{p-a},\qquad q=d+1,
\]

a nonconstant positive coordinate run `[a,b]` in the owner trace has
source support `[a+d,b]`.  This is nonempty exactly when the run has at
least `q` owners.  The union of the `q` source positions based at an owner
index `i` meets this support exactly when `i` lies in the original positive
run.  Constant-one and constant-zero coordinates are handled separately.
Thus Lemma 1.1 is correct.

The statement that every individual `P_p` is nonempty needs only `d<R`:
among `d` successive Johnson exchanges at most `d` members of the first
rank-`R` owner disappear.  This nonemptiness is weaker than the exact
inversion identity; the source now distinguishes the two claims.

## 2. Connector counts and the aperture proof pass

On a shortest connector

\[
 V_0=A,V_1,\ldots,V_\ell=B,
\]

a label deleted on edge `p` occupies `p-1` new internal owners after the
left endpoint.  A label inserted on edge `s` occupies `ell-s` internal
owners before the right endpoint.  A common endpoint label occupies all
`ell-1` internal owners.  Hence the three exact run lengths are

\[
 \lambda+p-1,\qquad \ell-s+\rho,\qquad
 \lambda+\ell-1+\rho,
\]

which verifies `(2.2)--(2.4)` without an off-by-one error.

For deletion releases `r=q+1-lambda`, sorted feasibility is
`r_(i)<=i`.  If this failed at an `i<=q`, then at least
`ell-i+1` deletion labels would have age at most `q-i`, contradicting the
unit clipped-age bound when `ell>=q`.  The insertion deadlines
`u=ell+rho-q` satisfy the dual cut: the number with `u<=s` is at most
`max(0,s+q-ell)<=s`.  Common labels are automatic because
`lambda,rho>=1`.  Corollary 2.2 is therefore exact with the one-sided
aperture `ell>=q`; no `2d+1` zero-gap aperture is being smuggled in.

## 3. The staged block join is chronology-only

The release stage on an exit arm constrains only labels which are deleted
there.  Labels inserted on a shortest arm are never deleted again inside
that arm, so their runs remain open at the far port.  Dually the entrance
stage constrains only insertion deadlines imported by the fixed block;
arbitrary deletion order merely determines the far port's right-age
profile.  Once these two profiles are fixed, Corollary 2.2 schedules the
connector.  Its length at least `q` automatically protects every label
common to its endpoints.  The remaining labels are exactly its release
and deadline jobs.  This validates the staged residence proof.

There was one genuine quantifier issue in the earlier draft.  A literal
geodesic already fixes its deletion and insertion order.  Reordering its
events can change every intermediate owner and lower facet, and hence can
destroy previously checked resource avoidance.  The corrected Theorem 3.1
therefore fixes endpoint exchange banks and proves existence of
positive-safe orders.  It concludes a **protected** path only when those
scheduled orders are also resource-disjoint.  Thus:

\[
 \text{schedule feasibility}+\text{some clean path with the same endpoints}
 \not\Longrightarrow
 \text{one clean schedule-feasible path}.
\]

Private one-tag/pair-tag signatures make much cross-segment separation
automatic, but a schedule/avoidance co-selection statement is still
needed at same-signature resources.

## 4. The size quantifier is now proof-safe

The existing long one-tag theorem handles only `O(sqrt R)` protected
components.  It cannot be applied verbatim to the `O(d^3)` complete
top-`d` casualty bank.  The source states this limitation explicitly.
Theorem 3.1 is valid for any finite list as a chronology statement, but
the physical resource-disjoint co-selection conclusion has not been
proved at that larger quantifier.

## 5. The fixed-age Hall iff is exact

Fixing `M_0` fixes, at each owner `T`, the deleted label `x_T` and the
`R-1` nontrivial possible successors

\[
 T-x_T+y,\qquad y\notin T.
\]

Positive residence imposes exactly these age rules:

* `x_T` may leave only at capped age `q`;
* the inserted `y` is born at age one;
* every persistent present label increments its capped age; and
* absent labels have no state and no waiting-time constraint.

After a forced successor matching `Q` is deleted from the split tail and
head shores, extending it is literally a perfect matching of the residual
`D^+_(M_0,a)`.  Hall is `(4.8)`.  Lifting the chosen successor of `T`
through the facet `M_0(T)` gives a second perfect incidence matching;
excluding `T` itself makes it edge-disjoint from `M_0`.  Cyclic
deterministic age consistency then gives every nonconstant positive run
length at least `q`.

The iff must—and now does—fix all of `M_0`, the full owner-age state `a`,
and the first protected phase.  Maturity `a_T(x_T)=q` is necessary for a
residual tail to have any successor, but is not sufficient: all candidate
head age vectors can still be incompatible.  Conversely, young absent
labels are not an obstruction.

## 6. Chronology and relative-wreath scope

Hall yields a cycle cover.  The subtour cuts `(5.1)` are exactly what is
needed for one successor cycle; ordinary degree restoration does not
provide them.  A later fusion must itself pass the one-sided seam test.

The clean-package tight-row identity makes relative MSW grafting a valid
alternative gate, but not a completed construction.  The frozen `m=3`
Farkas example proves that pairwise row disjointness alone does not imply
simultaneous protected-row extension.  The source correctly asks instead
for conformal exact trades with negative rows present in one factor and a
positive-safe fusion.

## 7. Frozen conclusion

The source establishes exactly

\[
\boxed{
\begin{gathered}
\text{positive residence is the flat-inversion condition},\\
\text{fixed endpoint banks have an exact one-sided scheduling test},\\
\text{fixed }(M_0,a,Q)\text{ completes iff one residual Hall system holds}.
\end{gathered}}
\]

It leaves three independent physical gates: schedule/avoidance
co-selection for the named bank, construction of a global age-Hall state
(plus subtour control), and replacement of every unprotected/deep
occurrence and typed-cap claim in that same chronology.

