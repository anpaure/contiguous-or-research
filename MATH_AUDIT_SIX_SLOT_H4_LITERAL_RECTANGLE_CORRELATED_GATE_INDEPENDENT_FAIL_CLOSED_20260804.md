# Independent fail-closed audit: six-slot `h=4` literal rectangle gate

**Date:** 2026-08-04  
**Audited theorem:**  
`MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md`  
**Audited theorem SHA-256:**  
`a8498766b53880fc4490626627c187a329e2ed4f448853e347e2160f2d573924`  
**Audited freeze manifest:**  
`MATH_FREEZE_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.sha256`  
**Manifest SHA-256:**  
`13cda4120f4eb8687e1b76b595327f6f33a65bf053c1b9f6de957185bec05a19`

**Verdict:** **FAIL CLOSED PENDING THREE PACKAGE CORRECTIONS.**  The
literal additive rectangle, correlated `y+z` estimate, first-residue
endpoint elimination, far-end Gaussian bound, continuity argument, smooth
KKT equations, and boundary/nonsmooth stratification all replay.  The
frozen package nevertheless contains one malformed theorem display, one
false arithmetic line in its frozen self-audit, and one missing dependency
needed for the asserted truncation at `delta_*`.  None of these defects
refutes the correlated reduction or its far-end positivity.

## 1. Byte authentication

Rehashing gives exactly the two requested digests above.  Running the
freeze manifest verifies both entries:

\[
\begin{array}{c|c}
\text{theorem}&\mathrm{OK}\\
\text{frozen self-audit}&\mathrm{OK}.
\end{array}
\]

Thus this audit is bound to the requested bytes.

## 2. Exact package corrections

### 2.1 Malformed rectangle display

The frozen theorem's equation (1.4) reads literally

\[
                         0,quad u,quad P,quad P+u.
\]

The intended display is

\[
 \boxed{0,\qquad u,\qquad P,\qquad P+u.}
\]

The surrounding definitions make the intended mathematics unambiguous,
but the frozen displayed formula itself requires this formatting repair.

### 2.2 False arithmetic in the frozen self-audit

The theorem's cap is correct:

\[
 {1\over20000}+{1129\over25000}-{57\over1400}
 ={35+31612-28500\over700000}
 ={3147\over700000}.
\tag{2.1}
\]

The frozen self-audit instead prints

\[
 {35+15806-14250\over700000}={3147\over700000},
\]

whose numerator on the left is `1591`, not `3147`.  It mixed
denominator-`700000` for the first term with denominator-`350000` for the
other two.  Equation (2.1) is the exact correction.  The theorem itself
uses the correct final constant.

### 2.3 Missing and presently fail-closed local-interval dependency

The frozen theorem restricts the new rectangle analysis to

\[
 \delta_*<\delta<A/2
\]

and asserts that every nonpositive physical table lies there.  This uses
the local sign theorem

`MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md`

with SHA-256

`34057076744b82574ca5d93c87d29dea301c9b9a0edf9ee4232bc72e5b091315`.

That dependency is absent from Section 7 and from the freeze manifest.
Moreover, its independent audit is fail-closed pending two weak-endpoint
repairs.  Those repairs preserve the local positivity conclusion, but a
corrected successor has not yet been frozen.  Therefore the present
package may be read unconditionally as a correlated reduction on its
displayed residual domain, but its all-residual implication through
`delta_*` is not stand-alone frozen lineage until the corrected local
theorem is included.

## 3. Literal rectangle and physical domain

Set

\[
 p=A-P,\qquad a=p-u,\qquad\tau=A+\delta.
\]

The canonical constraints give

\[
v=p+\delta\le P/2={A-p\over2},
\]

and hence

\[
3p\le A-2\delta,
\qquad
P=A-p\ge {2(A+\delta)\over3}={2\tau\over3}.
\]

Also `P+u<A` gives `u<A-P`, while maximum efficiency gives
`u<=P/4`.  Passing to the compact closure yields exactly

\[
2\tau/3\le P\le A,
\qquad
0\le u\le\min(A-P,P/4).
\]

The four literal retained shifts are

\[
0,\quad u,\quad P=A-p,\quad P+u=A-a,
\]

and satisfy the additive identity

\[
0+(P+u)=u+P.
\]

Internal superadditivity gives

\[
x\le u,\qquad2y\le P,\qquad y+z\le P+u<A,\qquad2z\le\tau.
\]

Together with monotonicity of the original table, this yields every bound
used in (1.6).  The physical rectangle and domain are exact.

## 4. Correlated `y+z` charge

If `z<=A/2`, both period trains are positive.  Otherwise set `v=A-z`.
The ceiling `z<=tau/2` gives

\[
v\ge A-\tau/2={A-\delta\over2}=v_\delta,
\]

and `y+z<A` gives `y<v`.

If `y>=A/4`, then `A/4<=y<v<A/2`; quarter-band decrease gives
`F(y)>F(v)`.  Period monotonicity and reflection therefore give a value
larger than `-epsilon`.

If `y<A/4`, use `F(y)>L`, `F(v)<=F(v_delta)`, period monotonicity, and
reflection.  The result is exactly

\[
F_\tau(y)+F_\tau(z)>
-\left[\varepsilon+(F(v_\delta)-L)_+\right].
\]

The cap arithmetic is the corrected equation (2.1).  No independent pair
minimum or false complementary equality appears.

**Correlated-pair verdict:** **PASS.**

## 5. Exact first-residue elimination

The physical interval is `0<=x<=u<A/4`.  The period-uniform theorem says
that every interior critical point of `F_tau` on the half band is a strict
local maximum.  Hence a minimum of `F_tau` on `[0,u]` is attained at an
endpoint:

\[
F_\tau(x)\ge\min\{F_\tau(0),F_\tau(u)\}
=\min\{C(\tau),F_\tau(u)\}.
\]

Substitution in the literal six-residue train preserves `P` and `P+u`
and proves `Phi>mathfrak R`.  Consequently `Phi<=0` indeed implies
`mathfrak R<Phi<=0`.

**Endpoint-elimination verdict:** **PASS.**

## 6. Far-end tail and continuity

At `delta=A/2`, the domain constraints force `(P,u)=(A,0)`.  The gate is

\[
2C(3A/2)+2F_{3A/2}(A)-\Gamma(A/2).
\]

Ceiling monotonicity gives

\[
C(3A/2)>C(6A/5)>{63\over1000}.
\]

The high train is exactly

\[
F_{3A/2}(A)=-\sum_{q\ge0}
e^{-(2A+3qA/2)^2}.
\]

Its first term is below `2161/50000`.  The first successive exponent gap
is `33pi/16>99/16`, and all later gaps are larger, so the tail ratio is
below `1/480`.  Therefore

\[
-F_{3A/2}(A)
<{2161\over50000}{480\over479}<{11\over250}.
\]

Using the correct Gamma cap gives

\[
2{63\over1000}-2{11\over250}-{3147\over700000}
={23453\over700000}>0.
\]

All trains and `Gamma`, including its positive-part switch, are continuous.
If nonpositive points approached the far endpoint, compactness and the
domain inequalities would force `(P,u)->(A,0)`, contradicting this strict
margin.  The one-sided positive neighborhood follows.

**Far-end verdict:** **PASS.**

## 7. KKT and subgradient completeness

On low branch `C`, the smooth gate is

\[
2C(\tau)+F_\tau(P)+F_\tau(P+u)-\Gamma.
\]

Its `u`, `P`, and `delta` equations give exactly (5.5).  On branch `U`,
the shifts are `0,u,P,P+u`, and differentiation gives exactly (5.6).
On the active Gamma branch,

\[
\Gamma'(\delta)=-{1\over2}T_A((A-\delta)/2),
\]

with derivative zero on the inactive branch.

The domain is cut out by:

\[
\delta_*\le\delta\le A/2,\quad
2\tau/3\le P\le A,\quad
0\le u\le A-P,\quad
0\le u\le P/4.
\]

Thus its complete finite stratum list consists of the two delta endpoints,
the two P endpoints, the three u boundaries, and the switch `P=4A/5`.
Adding the low-minimum and Gamma switches and the two smooth systems gives
exactly Proposition 5.2.  At `P=2tau/3`, differentiation along the moving
boundary adds

\[
{2\over3}\left(T_\tau(P)+T_\tau(P+u)\right),
\]

as stated.  Intersections require the corresponding simultaneous
one-sided inequalities; no extra smooth branch exists.

The proposition is a complete finite **stratum/KKT-type list**.  It is not
a finite list of isolated numerical candidates, and the theorem does not
claim otherwise.

**KKT/subgradient verdict:** **PASS.**

## 8. Final verdict

Subject to the corrected local-interval dependency, the substantive
mathematical conclusions pass:

1. every physical residual maps to one correlated rectangle gate;
2. the `y,z` loss is bounded by the stated one-dimensional Gamma charge;
3. the old far-end negative gates were artifacts of decoupling;
4. the new gate is uniformly positive near the far endpoint;
5. every unresolved minimum belongs to the stated finite KKT stratum list.

The frozen package itself is not correction-free.  The byte-bound verdict
is therefore

\[
\boxed{\textbf{FAIL CLOSED PENDING THE THREE PACKAGE CORRECTIONS}.}
\]
