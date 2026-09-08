# Independent audit: Chamber-II stationary-strip elimination

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_SIX_SLOT_CHAMBER_II_STATIONARY_STRIP_ELIMINATION_AND_LONG_WRAP_CURVE_20260804.md`  
**Audited source SHA-256:**
`f5dbde2a817c6ab23ade7de5c0f0d691d80db4d4bb23865f9643959efa79c91b`  
**Method:** independent symbolic replay; no numerical search and no finite
enumeration.

## Verdict

**GO, with the source's stated reduction-only scope.**  The proof correctly
eliminates the old two-compact stationary strip as an independent
Chamber-II gate.  Once the already-proved threshold and repeated-gap faces
are imported, all of Chamber II follows from

\[
 \mathcal P_-(P,a)=C(P)+F_P(a)+F_P(2a)>0.
\]

For each fixed period, this surviving boundary has at most one interior
local-minimum point.  A global nonpositive minimum must satisfy the KKT
system recorded in the source.  The audit does **not** sign that residual
curve and therefore makes no claim of complete six-slot positivity or of
an OR-word upper bound.

## 1. Derivative normalization and reflected curvature

For `w=Ax`, direct differentiation of the compact rows `q=0,1` and the
Gaussian tail gives

\[
 {F_P'(Ax)\over2A}
 =\sum_{q\ge0}h(1+x+q\rho)-h(1-x)-h(1-\rho-x),
 \qquad \rho=P/A.
\]

The derivatives used in the source replay exactly:

\[
 h''(z)={\pi\over2}z\left({\pi z^2\over2}-3\right)
 e^{-\pi z^2/4},
\]

\[
 h'''(z)={\pi\over2}e^{-\pi z^2/4}
 \left(-4\eta^2+12\eta-3\right),
 \qquad \eta={\pi z^2\over4}.
\]

The two roots in `eta` are `(3-sqrt(6))/2` and `(3+sqrt(6))/2`.
On `[3/5,7/5]` the argument `eta` lies strictly between them, so `h''`
is strictly increasing there.  For `x in [2/5,1/2]`, the two endpoints
instead lie on opposite sides of the zero `sqrt(6/pi)` of `h''`.
Consequently

\[
 h''(1+x)\ge h''(1-x)\quad(0\le x\le1/2),
\]

strictly when `x>0`.

Twice differentiating the normalized train derivative gives

\[
 T_\rho''(x)=h''(1+x)-h''(1-x)
 +\sum_{q\ge1}h''(1+x+q\rho)-h''(1-\rho-x).
\]

Here the reflected pair is nonnegative; every tail argument is at least
`3/2>sqrt(6/pi)` and hence every tail term is positive; and
`0<=1-rho-x<=1/2<sqrt(6/pi)`, so the last subtracted term is
nonnegative.  Thus `T_rho''>0`.  The Gaussian tail supplies uniform
majorants for every termwise differentiation used here.

A strictly convex derivative cannot have two distinct zeros at which its
own derivative is nonnegative: the strict supporting-line inequality at
the first zero makes the value at the second strictly positive.  Therefore
`F_P` has at most one interior local minimum on `[0,A-P]`.

## 2. Exact polygon-boundary audit

At fixed `P`, the closed Chamber-II fibre is

\[
 a\ge0,\qquad b\ge2a,\qquad2b\le P+a,\qquad b\le A-P.
\]

These give exactly four faces.

1. **`a=0`.**  The table
   `(0,b,P,P+b,2P)` is a four-slot internally superadditive table.
   Besides the tautological sums, its only inequality is `2b<=P`.
   Its Bellman clock is
   `V_(2q)=qP`, `V_(2q+1)=qP+b`, so complete four-slot positivity gives
   `C(P)+F_P(b)>0`.  Adding arithmetic-ceiling positivity `C(P)>0`
   yields the required `2C(P)+F_P(b)>0`.

2. **`2b=P+a`.**  This is precisely the prethreshold repeated-gap value
   `L_3(P;a,(P+a)/2)`.  The other chamber inequality gives
   `3P+a<=2A`, so the frozen repeated-gap theorem applies.  The sole
   endpoint excluded by its strict `P<2A/3` statement is
   `(P,a)=(2A/3,0)`, already covered by the preceding `a=0` face.

3. **`b=A-P`.**  This is the previously proved five-slot threshold
   endpoint.

4. **`b=2a`.**  This is the only face not already signed.

If a nonpositive minimum were interior, its two independent first
derivatives would give `F_P'(a)=F_P'(b)=0`, and positive semidefiniteness
of the diagonal Hessian would give `F_P''(a),F_P''(b)>=0`.  Interior
Chamber II has `0<a<b`, contradicting the at-most-one-minimum theorem.
Compactness and strict positivity of the other three closed faces leave
only `b=2a`.  This validates the complete stationary-strip elimination.

## 3. One-dimensional residual curve

On `b=2a`, the exact remaining interval is

\[
 0\le a\le m(P):=\min\{P/3,(A-P)/2\}.
\]

For `Q_P(a)=C(P)+F_P(a)+F_P(2a)`, one has

\[
 Q_P'(a)=F_P'(a)+2F_P'(2a),
\]

and

\[
 (Q_P')''(a)=F_P'''(a)+8F_P'''(2a)>0.
\]

The domains are valid because `2a<=A-P`.  Hence `Q_P` also has at most
one interior local minimum.  All endpoint identities replay exactly:

* `Q_P(0)=3C(P)>0`;
* when `P<=3A/5`, `m(P)=P/3` and splitting the `P/3` lattice into its
  three residue classes gives `Q_P(P/3)=C(P/3)>0`;
* when `P>=3A/5`, `m(P)=(A-P)/2` and the endpoint is the signed threshold
  face;
* at `P=A/2`, the audited inequality `F_(A/2)'(w)<0` for
  `0<=w<=A/3` makes `Q_(A/2)` decreasing, with minimum
  `Q_(A/2)(A/6)=C(A/6)>0`.

Therefore any nonpositive residual value forces the stationary system

\[
 F_P'(a)+2F_P'(2a)=0,
 \qquad F_P''(a)+4F_P''(2a)\ge0,
\]

at a unique possible `a` for each `P`.

For a global counterexample all four outer `(P,a)` faces are positive, so
the strict inequalities `P>A/2`, `P>3a`, and `P+2a<A` hold.  The inward
`b` derivative, the tangent derivative along `b=2a`, and the free period
derivative give respectively

\[
 F_P'(2a)\ge0,
\]

\[
 F_P'(a)+2F_P'(2a)=0,
\]

\[
 \sum_{q\ge1}q\{K'(qP)+K'(qP+a)+K'(qP+2a)\}=0.
\]

Thus `F_P'(a)<=0<=F_P'(2a)`.  No omitted endpoint is hidden in this KKT
system.

## 4. Frozen dependencies checked

The following dependency hashes match the source exactly:

| role | file | SHA-256 |
|---|---|---|
| original Chamber-II endpoint reduction | `MATH_THEOREM_SIX_SLOT_THREE_EFFICIENT_CHAMBER_II_PRETHRESHOLD_CRITICAL_STRIP_REDUCTION_20260804.md` | `8101f952bdfc4900f2fdd9d4b6396642c694c850cb420c7ef8dc03e24f19c1f3` |
| repeated-gap and half-period closure | `MATH_THEOREM_HALF_PERIOD_TWO_COMPACT_TRAIN_AND_PRETHRESHOLD_REPEATED_GAP_CLOSURE_20260804.md` | `c35a9db78b5dc317fa319dd150c3abe0521b3043b9dc22d7066b2d14ae2afd4a` |
| complete four-slot positivity | `MATH_THEOREM_FOUR_SLOT_BELLMAN_COMPLETE_POSITIVITY_20260804.md` | `1624cff37c4f6b45edd16234e054d43c99ceb722d7dac4b57d058a40465b68b9` |
| arithmetic-ceiling positivity | `MATH_THEOREM_SMOOTH_BINOMIAL_CONFIGURATION_DUAL_AND_CEILING_PRICE_CLASSES_20260804.md` | `c3a2c1858f59fa32e61d2f9a9252085ad7fb01f3521ab5cb46998705123e103d` |

The audit establishes the reduction and only the reduction.  The sign of
the remaining long-wrap stationary curve is still open.
