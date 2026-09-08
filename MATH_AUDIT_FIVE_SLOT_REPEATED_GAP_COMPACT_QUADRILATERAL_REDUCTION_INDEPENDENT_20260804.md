# Independent audit of the five-slot compact quadrilateral reduction

**Date:** 2026-08-04  
**Verdict:** **GO as a reduction.**  The two lower bounds, coordinate maps,
and unresolved interiors are exact.  The signs of the two quadrilateral
functions remain open.

## Exact binding

Audited theorem:

`MATH_THEOREM_FIVE_SLOT_REPEATED_GAP_COMPACT_QUADRILATERAL_REDUCTION_20260804.md`

SHA-256:

`b8e6c1584079bfc510770f47d8b67b1e6508abd7cfa40f64fa0400a56e7010fa`

The endpoint-descent and reflection inputs were checked against the
retracted precursor only in the portions explicitly retained as valid;
the reversed no-interior-minimum inequality is not used here.

## 1. Short-singleton coordinates

Put `y=a+beta`, `v=A-2y`, and `u=v+a=A-(2y-a)`.  Then

\[
 2a+2\beta<A\iff v>0,
\]

\[
 A<2a+3\beta=3y-a\iff2a+3v<A,
\]

and

\[
 a\le\beta=y-a\iff a\le {A-v\over4}.
\]

The second strict inequality and `a>=0` imply `v<A/3`.  Conversely these
relations recover `y=(A-v)/2` and `beta=y-a`, so no condition is lost.
Thus

\[
 0<v<A/3,\qquad0\le a\le(A-v)/4,\qquad2a+3v<A
\]

is exactly the original unresolved domain.

The period-`a+2 beta=2y-a` train has the literal clock

\[
 0,a,y,2y-a,2y,3y-a,\ldots .
\]

The first five entries are below `A`, the sixth is above `A`, and
`a<=beta` supplies the residue superadditivity.  Endpoint descent therefore
gives

\[
 R\ge C+F(a)+F(y)+F(2y-a)+F(2y).
\]

Since `2y-a=A-(v+a)` and `2y=A-v`, two applications of

\[
 F(A-w)>-F(w)-\varepsilon
\]

have the displayed direction and give exactly `R>Q_R(a,v)`.

## 2. Long-singleton coordinates

Put `t=A-p-a`, equivalently `p=A-a-t`.  Then

\[
 p<A-a\iff t>0,
 \qquad
 p>A-2a\iff t<a,
 \qquad
 p>3a\iff4a+t<A.
\]

Hence the unresolved interior is exactly

\[
 0<t<a<A/4,\qquad4a+t<A.
\]

The source now correctly distinguishes this strict domain from the
adjoined density-tie boundary `4a+t=A`.  On that boundary `p=3a` and the
original train is the already-positive ceiling `P(3a,a)=C(a)`.  Demanding
`Q_P>0` also on the weakly enlarged domain is a permissible stronger
sufficient condition, not an equivalence.

The period-`p` train has the exact clock

\[
 0,a,2a,p,p+a,p+2a,\ldots .
\]

The original domain puts its first five entries below `A` and its sixth
above `A`; `p>3a` makes the three-residue form superadditive.  Endpoint
descent yields

\[
 P\ge C+F(a)+F(2a)+F(p)+F(p+a).
\]

Finally `p=A-(a+t)` and `p+a=A-t`, so reflection gives exactly
`P>Q_P(a,t)`.  No inequality is reversed.

## 3. Boundary and strictness audit

* In the `R` face, `v=0` and `2a+3v=A` are threshold boundaries and are
  correctly excluded by the two strict inequalities inherited from the
  original gate.  The density tie `a=beta` remains allowed.
* In the `P` face, `t=0` is `p=A-a`, `t=a` is `p=A-2a`, and
  `4a+t=A` is `p=3a`.  The first two and the third are known-positive
  boundary faces; the unresolved gate is their strict interior.  The
  theorem's optional adjoining of the third face does not weaken its
  sufficient implication.
* The word "compact" refers to the bounded finite-dimensional reduction.
  The displayed unresolved domains themselves retain open faces and are
  not topologically closed compact sets unless all known-positive boundary
  faces are deliberately adjoined.

## 4. No immediate convexity or endpoint closure

The existing train facts do not give a fixed curvature sign for either
quadrilateral.  For fixed `a`,

\[
 {\partial^2Q_P\over\partial t^2}
 =-F''(t)-F''(a+t),
\]

while for fixed `v`,

\[
 {\partial^2Q_R\over\partial a^2}
 =F''(a)-F''(v+a).
\]

Neither expression has a determined sign from the proved fact that every
interior critical point of `F` is a strict maximum.  In the other `R`
coordinate,

\[
 {\partial^2Q_R\over\partial v^2}
 ={1\over4}F''((A-v)/2)-F''(v)-F''(v+a),
\]

which is likewise unsigned.  The correct no-interior-minimum inequality
controls an earlier point from below by the two enclosing endpoints; it
does not lower-bound the forward differences occurring in `Q_R` or
`Q_P`.  Therefore no convexity, concavity, or endpoint-only closure follows
immediately from the current lemmas.

## 5. Scope

The theorem validly removes all subthreshold periods and gives the two
bounded threshold-period lower bounds `Q_R` and `Q_P`.  The added scope
note correctly records that uniform positivity of `Q_P` on its full
closed domain is false at the limiting corner, so `Q_P` is only a useful
sufficient target on proper subranges.  This scope clarification changes
none of the reduction identities audited above.  The theorem does not
prove positivity for every five-slot Bellman table.
