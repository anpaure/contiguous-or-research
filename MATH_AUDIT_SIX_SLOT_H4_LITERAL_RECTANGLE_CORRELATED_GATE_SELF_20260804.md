# Self-audit: six-slot `h=4` literal rectangle correlated gate

**Date:** 2026-08-04  
**Verdict:** **GO for the stated correlated reduction.**  The theorem does
not claim full interior positivity of the new rectangle gate.

## 1. Audited artifact

| file | SHA-256 |
|---|---|
| `MATH_THEOREM_SIX_SLOT_H4_LITERAL_RECTANGLE_CORRELATED_GATE_20260804.md` | `533f194ed727b2c15d26ca2007131a3bfc22f08f401097f74d021d40cf5dd5cd` |

## 2. Physical-coordinate audit

With `p=A-P`, `a=p-u`, and `tau=A+delta`, the canonical inequalities give

\[
 p\le {A-2\delta\over3}
 \iff
 P\ge {2(A+\delta)\over3}={2\tau\over3}.
\]

The strict inequality `P+u<A` gives `u<A-P`; maximum efficiency gives
`u<=P/4`.  Hence the compact closure (3.3) is exact.

The four retained shifts are

\[
 0,\quad u,\quad P=A-p,\quad P+u=A-a.
\]

Thus they really are one additive rectangle; no independent reflected
base remains.

Internal superadditivity checks every inequality used later:

\[
 c_5\ge c_1+c_4\Rightarrow x\le u,
\]

\[
 c_4\ge2c_2\Rightarrow2y\le P,
\]

\[
 c_5\ge c_2+c_3\Rightarrow y+z\le P+u<A,
\]

and endpoint saturation gives `2z<=tau`.  Therefore
`x,u<A/4`, `y<=A/2`, and `z<=tau/2< A` on the physical interior.

## 3. Correlated `y,z` audit

If `z>A/2`, put `v=A-z`.  The ceiling gives

\[
 v\ge A-\tau/2=(A-\delta)/2=v_\delta.
\]

The strict inequality `y+z<A` gives `y<v`.  If `y>=A/4`, both lie in the
strictly decreasing quarter-to-half band, so `F(y)>F(v)`.  If `y<A/4`,
the exact lower bound `F(y)>L` and monotonicity give

\[
 F(v)\le F(v_\delta).
\]

Period monotonicity and Jacobi reflection therefore give precisely

\[
 F_\tau(y)+F_\tau(z)>-
 \left[\varepsilon+(F(v_\delta)-L)_+\right].
\]

The constant cap is arithmetically correct:

\[
 {1\over20000}+{1129\over25000}-{57\over1400}
 ={35+31612-28500\over700000}
 ={3147\over700000}.
\]

No false complementary equality or independent minimization is used.

## 4. First-residue elimination audit

The physical interval is `0<=x<=u<A/4`.  The period-uniform theorem says
every interior critical point of `F_tau` on the entire half band is a
strict local maximum.  A global minimum on `[0,u]` is therefore at an
endpoint, proving exactly

\[
 F_\tau(x)\ge\min\{F_\tau(0),F_\tau(u)\}
 =\min\{C(\tau),F_\tau(u)\}.
\]

Substitution into the literal train leaves the two high shifts `P,P+u`
unchanged and proves `Phi>mathfrak R`.  Therefore `Phi<=0` indeed implies
`mathfrak R<Phi<=0`; the strict sign in (3.6) is correct.

## 5. Far-end certificate audit

At `delta=A/2`, the lower domain boundary is `P>=A`, so `(P,u)=(A,0)` is
the unique point.  The train at the high shift is

\[
 F_{3A/2}(A)=-\sum_{q\ge0}e^{-(2A+3qA/2)^2}.
\]

The first ratio is `e^{-33pi/16}` and all later ratios are smaller.
Using `pi>3` and the positive exponential series gives
`e^{33pi/16}>e^{99/16}>480`.  Hence

\[
 -F_{3A/2}(A)
 <{2161\over50000}{480\over479}<{11\over250}.
\]

The exact final margin is

\[
 2{63\over1000}-2{11\over250}-{3147\over700000}
 ={88200-61600-3147\over700000}
 ={23453\over700000}>0.
\]

The compact-domain sequence argument correctly upgrades point positivity
to uniform positivity in some one-sided far-end neighborhood: the domain
constraints force `P->A` and `u->0` whenever `delta->A/2`.

## 6. KKT audit

On branch `C`, the smooth gate is

\[
 2C(\tau)+F_\tau(P)+F_\tau(P+u)-\Gamma.
\]

Its `u` derivative is `T_tau(P+u)` and its `P` derivative is
`T_tau(P)+T_tau(P+u)`, giving the first two rows of (5.5).  Its period
derivative gives the third row.

On branch `U`, the four smooth trains are at `0,u,P,P+u`; differentiating
them gives (5.6) exactly.  The active derivative

\[
 \Gamma'(\delta)=-\tfrac12T_A((A-\delta)/2)
\]

has the correct sign and factor.

The domain boundary list contains both outer endpoints, both `P`
endpoints, all three possible `u` boundaries, the switch `P=4A/5`, the
low-minimum switch, the `Gamma` switch, and the two smooth systems.  On
`P=2tau/3`, the additional chain-rule contribution is exactly

\[
 {2\over3}(T_\tau(P)+T_\tau(P+u)).
\]

The theorem explicitly delegates intersections to oriented one-sided
conditions, so it does not mistake a Clarke stationary maximum for a
minimum.

## 7. Scope audit

The old decoupled gates being negative at the far endpoint does not
contradict the new theorem: their independently minimizing bases cannot
satisfy the rectangle relation simultaneously.  The new theorem proves
only:

* a single correlated necessary gate for a physical counterexample;
* positivity of that gate near the far endpoint;
* a finite exact interior KKT locus.

It does not assert that the rectangle gate is positive everywhere.
Within that scope, the verdict is **GO**.
