# Self-audit: double-turn two-factor normal form and `r=3` repair

**Date:** 2026-08-05  
**Audited note:**
`MATH_THEOREM_DOUBLE_TURN_TWO_FACTOR_NORMAL_FORM_AND_R3_C8_REPAIR_20260805.md`

## 1. Matching and colour counts

The rank-`(r-1)/r` incidence graph on a `(2r-1)`-set is `r`-regular on
both equal shores.  Removing one perfect matching leaves degree `r-1`.

For fixed `R in binom(Omega,r+1)`, each of its `r+1` rank-`r` facets `Y`
has one preimage `A=f_0^{-1}(Y)`.  The other intermediate rank-`r` set
between `A` and `R` gives one residual edge of colour `R`, and this is
reversible.  Hence the class size `r+1` is exact.

The total-class census agrees with the residual edge count:

\[
 |\mathcal U|(r+1)
 ={2r-1\choose r+1}(r+1)
 =W(r-1)=|E(B-M_0)|.
\]

The uniform residual weight `1/(r-1)` therefore has matching degree one
and colour load `(r+1)/(r-1)`.

## 2. PBBS complement audit

Put `m=r-1`.  The audited centered PBBS factor on rank-`m` owners has

\[
 e_X=\{f^{-1}(X),f(X)\},\qquad
 f^{-1}(X)\cup f(X)=X^c,qquad
 \chi(X)=f^{-1}(X)\cap f(X),
\]

where `X` runs over every rank-`m` set and `chi` covers every rank-`(m-1)`
set with multiplicity one, two, or three.  On complementary rank-`m+1=r`
owners, the edge intersection is `X` and the edge union is `chi(X)^c`.
These are respectively the complete rank-`r-1` palette exactly once and
the complete rank-`r+1` palette surjectively.  Complementation preserves
the PBBS component bound `Cat_m=Cat_(r-1)`.  The unconditional two-factor
claim is therefore exact.

## 3. Two-factor and forest scope

Two edge-disjoint perfect matchings give every lower and owner vertex
degree two.  The lower vertex itself labels the projected intersection, so
lower exactness is automatic.  Upper coverage is exactly the colour-class
hit condition.  Connectedness is needed only for the Hamilton version.

Retaining one edge per upper colour gives `U` edges.  It is a forest exactly
when it omits an edge from every original factor cycle.  A spanning forest
with `W` vertices and `U` edges has `W-U=Cat_r` components.  The graphic
transversal theorem is therefore exact, including isolated vertices.

For the PBBS factor, omitting `mu_R-1` occurrences of every colour and
hitting every factor cycle is a capacitated matching from cycles to
nonsingleton colours.  For a cycle set `mathscr S`, one colour `R` can
cover at most one demand on each incident cycle and at most
`q_R=mu_R-1` demands overall.  Its exact cut contribution is therefore

\[
 \min\{q_R,n_R(\mathscr S)\},
\]

not merely `q_R` whenever it occurs.  The corrected capacitated Hall
system (3.3) is exact.

Weight each **distinct** cycle--colour incidence by `q_R/mu_R`.  For every
cut,

\[
 n_R(\mathscr S){q_R\over\mu_R}
 \le\min\{q_R,n_R(\mathscr S)\}.
\]

Hence weighted repeat mass at least one on every cycle is a sufficient
condition.  Two distinct repeated colours suffice because
`(mu_R-1)/mu_R>=1/2`.  Occurrences are deliberately deduplicated within
one cycle.  The aggregate inequalities `sum q_R=Cat_r` and
`#cycles<=Cat_(r-1)` do not imply every Hall cut and are not promoted to a
proof of the graphic transversal.

## 4. PBBS `q2` bridge audit

In the natural, uncomplemented centered PBBS factor, the two factor edges
adjacent at owner `A` have lower angle colours

\[
 f^{-2}(A)\cap A,\qquad A\cap f^2(A).
\]

Their intersection is the parity-three-state window

\[
 f^{-2}(A)\cap A\cap f^2(A).
\]

The direct PBBS Dyck theorem proves this has rank `r-3` at every owner and
covers every rank-`r-3` target.  Thus the full PBBS factor is
unconditionally `q1`- and `q2`-complete in the required turn sense.

The q2 Pascal lift needs a one-occurrence section of the repeated q1 angle
word.  Such a section must both hit every factor cycle with its omissions
and retain, for every q2 target, at least one owner whose two adjacent angle
occurrences are selected.  The corrected omission Hall theorem is exactly
the first of these two rows.  Full-factor q2 completeness is not used to
infer section q2 completeness.

## 5. Literal `r=3` audit

The original lower sequence is

\[
 45,45,25,35,13,14,12,12,23,34,
\]

so its distinct colours are all ten pairs except `15,24`, with surplus
copies of `45,12`.

Deleting `145-245` and `124-125` and adding `145-125` and `245-124`
changes the lower multiset by

\[
 -45-12+15+24.
\]

Every changed edge has union `1245`, so the upper multiset is literally
fixed.  The two displayed five-cycles partition all ten rank-three owners.

The incidence symmetric difference

\[
 145-45-245-24-124-12-125-15-145
\]

has eight distinct vertices.  Its edge-status word is
`old,old,new,new,old,old,new,new`; it is a genuine bipartite `C8` surgery,
but not an alternating matching flip.  It uses four lower colours, as
required by the two repeated/two missing defect.

## 6. `C6` scope

A standard alternating `C6` perfect-matching exchange presupposes a valid
factor before the move.  The source cycle has duplicated/missing lower
vertices and is outside that fibre.  The claim that the displayed direct
repair is not one `C6` is therefore type-correct.  The note deliberately
does not exclude a broader three-port rethreading of the augmented tight
enumeration leading to a different target.

For the fixed-exterior repair there is a second exact reason: its lower
degree correction is supported on four vertices `45,12,15,24`, whereas one
bipartite `C6` has only three lower vertices.

## 7. Verdict

\[
 \boxed{\text{PASS: all normal forms, counts, the graphic criterion, and
 the `r=3` `C8` identity are proof-safe.}}
\]
