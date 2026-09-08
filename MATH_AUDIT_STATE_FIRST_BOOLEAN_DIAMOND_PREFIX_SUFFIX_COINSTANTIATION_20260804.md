# Audit: state-first Boolean diamond prefix/suffix coinstantiation

**Date:** 2026-08-04  
**Method:** independent symbolic audit; pure mathematics, no finite search  
**Audited theorem:**
`MATH_THEOREM_STATE_FIRST_BOOLEAN_DIAMOND_PREFIX_SUFFIX_COINSTANTIATION_20260804.md`  
**Verdict:** **GO**, with the factor-completion scope correction incorporated
in the audited theorem.

## 1. Port Hall row

For distinct rank-`s` sources `X_g,X_h`, their rank-`(s+1)` upper shadows
intersect in at most one value.  Consequently, for `x` gain menus of size at
least `L_0`, second-order Bonferroni gives

\[
 \left|\bigcup_g\mathcal U_g\right|
 \ge xL_0-\binom{x}{2}.
\]

Deleting a global forbidden bank of size `f_0` leaves at least

\[
 xL_0-\binom{x}{2}-f_0
\]

values.  Hall therefore follows from

\[
 Q_0(x)=x(L_0-1)-\binom{x}{2}-f_0\ge0.
\]

`Q_0` is concave, so its minimum on the integer interval `1<=x<=p` is at an
endpoint.  The two displayed conditions `(P)` are exactly `Q_0(1)>=0` and
`Q_0(p)>=0`.  This part is exact.

The simplified row is also valid.  If `p>=2`, `p<=L_0`, and
`f_0<=L_0-1`, then

\[
 Q_0(p)
 \ge (p-1)\left(L_0-1-\frac p2\right)\ge0.
\]

The case `p=1` is immediate.

## 2. Sink Hall row

After the first matching, the selected ports are distinct rank-`(s+1)`
values.  Two such values have at most one common rank-`(s+2)` upper
extension.  The identical argument with `L_1,f_1` proves `(S)` and its
simplified form.  Since all source, port, and sink arcs are fixed before the
two Hall selections and both arcs have empty interiors, distinct endpoints
give genuinely vertex-disjoint paths; there is no hidden internal-capacity
collision.

The value-injective occurrence hypothesis is essential.  If equal Boolean
values are represented at several addresses, the same proof applies only
after refining the overlap bound in the occurrence-labelled menus.  The
audited theorem states this restriction explicitly.

## 3. Two-coordinate row

Coordinate zero is matched first.  Coordinate one deletes the complete bank
of `p` selected coordinate-zero ports, so its effective forbidden bank has
size at most `f_0+p`.  Applying the same endpoint test gives exactly (4.1).
The resulting `2p` port values are globally distinct, so the sink menus again
have pairwise overlap at most one.  Applying the one-coordinate Hall row to
`2p` claims gives exactly (4.2).

The sufficient conditions (4.3) are stronger than necessary but correct:

* `p<=L_0^0` and `f_0<=L_0^0-1` imply the first port row;
* `f_0<=L_0^1-p-1` makes the total second-coordinate forbidden size at most
  `L_0^1-1`, while `2p<=L_0^1` implies `p<=L_0^1`;
* `2p<=L_1` and `f_1<=L_1-1` imply the `2p`-claim sink row.

The two source occurrences per logical gain are not optional.  One unit
source shared by two requested paths is a cut of capacity one for demand two.

## 4. Protected-factor scope

The selected one-coordinate prefix bank is a matching in `ML_m`.  Therefore
the repository's small protected-factor theorem applies whenever

\[
 \Delta(P_*\cup M)\le2,
 \qquad |E(P_*\cup M)|\le m-2.
\]

This proves only that a spanning abstract two-factor contains the selected
prefix incidences.  It does not prove that every additional incidence of an
arbitrary completion is active in the fixed cap state or avoids the private
router capacities.  The theorem was corrected to state precisely this
scope.  The already selected paths remain mutually private in their original
fixed residual network; a simultaneous physical lift of the rest of the
factor remains a separate premise.

## 5. Marginal obstruction

The obstruction in Section 6 is realizable whenever

\[
 2L\le k-s,
 \qquad L\le k-s-1.
\]

The first inequality supplies disjoint `L`-element banks of rank-`(s+1)`
extensions of one source, and the second supplies `L` upper extensions of
each suffix-rich port.  Activating prefixes only on the first bank and
suffixes only on the second gives both marginal abundance claims but no
length-two path.  Hence an incidencewise good-diamond relation, or an
equivalent common-state joint relation, is genuinely necessary.

## 6. Exact gain and exact remaining premise

The theorem does not derive the candidate prefix arcs from an abstract
Middle Levels factor.  Its unconditional gain is narrower:

> once one fixed cap/guard/phase/occurrence state exposes sufficiently many
> candidate-wise active Boolean diamonds, two elementary Hall selections
> coinstantiate private gain-to-port prefixes and typed one-step suffixes.

Thus the formerly separate prefix and suffix routing problems reduce to the
single **static good-diamond abundance lemma**.  The current Pascal/common-cap
theory still has to prove that statewise abundance (and, for two coordinates,
the source multiplicity).  No conclusion about full upper-deck, residence,
component control, or regeneration follows from this theorem alone.

