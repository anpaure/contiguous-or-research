# Six-slot `h=4`: the literal rectangle gate restores the discarded physical correlation

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical correlated reduction.  It
returns to the literal endpoint-period train, uses the internal
superadditivity relations discarded by the two independent envelopes, and
reduces every residual physical `h=4` table to one compact three-parameter
rectangle gate.  The new gate is strictly positive at the formal far
endpoint and uniformly in a neighborhood of it, so the negative endpoint
of the former decoupled gates is proved spurious.  The complete interior
rectangle gate is not signed here; complete six-slot `h=4` positivity is
therefore not claimed.  No computation or search is used.

Put

\[
 A={\sqrt\pi\over2},
 \qquad
 F_\tau(w)=\sum_{q\ge0}K(q\tau+w),
 \qquad
 C(\tau)=F_\tau(0),
\tag{0.1}
\]

and abbreviate `F=F_A`.  The literal endpoint-period theorem says that an
inert canonical table

\[
 (0,x,y,z,P,P+u,\tau)
\tag{0.2}
\]

satisfies

\[
 \Phi\ge
 C(\tau)+F_\tau(x)+F_\tau(y)+F_\tau(z)
 +F_\tau(P)+F_\tau(P+u).
\tag{0.3}
\]

Here

\[
 \tau=A+\delta,
 \qquad
 0<\delta<A/2.
\tag{0.4}
\]

The previous two-gate theorem proves the physical branch positive through

\[
 \delta_*={43849\over643260}.
\tag{0.5}
\]

We work on the residual range `delta_*<delta<A/2`.

## 1. The exact physical rectangle

Set

\[
 p=A-P,
 \qquad
 a=p-u.
\tag{1.1}
\]

The canonical and endpoint constraints give

\[
 0<p\le {A-2\delta\over3},
 \qquad
 0\le u<p,
 \qquad
 u\le {P\over4}.
\tag{1.2}
\]

Equivalently,

\[
 \boxed{
 {2\tau\over3}\le P<A,
 \qquad
 0\le u<\min\{A-P,P/4\}.}
\tag{1.3}
\]

The four endpoint shifts not involving `y,z` are literally

\[
                         0,\quad u,\quad P,\quad P+u.
\tag{1.4}
\]

They form an additive rectangle.  This is the correlation lost when the
two reflected pairs were minimized independently.

Internal superadditivity also gives

\[
 x\le u,
 \qquad
 2y\le P,
 \qquad
 y+z\le P+u<A,
 \qquad
 2z\le\tau.
\tag{1.5}
\]

In particular,

\[
 0\le x\le u<A/4,
 \qquad
 0\le y\le A/2,
 \qquad
 y\le z\le\tau/2.
\tag{1.6}
\]

The endpoint-face equality—`X`, `Y`, or `Z`—is not needed below; (1.3)--
(1.6) hold on all three faces, including their ties.

## 2. The two remaining residues are almost complementary

Use the authenticated constants

\[
 \varepsilon={1\over20000},
 \qquad
 L={57\over1400}.
\tag{2.1}
\]

Reflection and the half-band theorem give

\[
 F(w)+F(A-w)>-\varepsilon,
 \qquad
 F(w)>L\quad(0\le w\le A/4),
\tag{2.2}
\]

while `F` is strictly decreasing on `[A/4,A/2]`.

Define

\[
 v_\delta={A-\delta\over2},
 \qquad
 \boxed{
 \Gamma(\delta)=\varepsilon+
       \bigl(F(v_\delta)-L\bigr)_+.}
\tag{2.3}
\]

Since `A/4<=v_delta<=A/2`, this is a one-dimensional explicit function.

### Lemma 2.1 (correlated `y,z` pair)

Every physical pair in (1.5)--(1.6) satisfies

\[
 \boxed{F_\tau(y)+F_\tau(z)>-\Gamma(\delta).}
\tag{2.4}
\]

Moreover,

\[
 \boxed{0<\Gamma(\delta)<{3147\over700000}.}
\tag{2.5}
\]

#### Proof

If `z<=A/2`, both trains are positive.  Suppose `z>A/2` and put

\[
                         v=A-z.
\]

The ceiling `z<=tau/2` gives `v>=v_delta`.  The strict physical inequality
`y+z<=P+u<A` gives `y<v`.

If `y>=A/4`, then `A/4<=y<v<A/2`; monotone decrease and reflection give

\[
 F_\tau(y)+F_\tau(z)
 \ge F(y)+F(z)>F(y)-F(v)-\varepsilon>-\varepsilon.
\]

If `y<A/4`, then `F(y)>L`.  Since `v>=v_delta` and `F` decreases on the
quarter-to-half band,

\[
 F_\tau(y)+F_\tau(z)
 >L-F(v)-\varepsilon
 \ge L-F(v_\delta)-\varepsilon.
\]

These two cases prove (2.4).

Finally `F(v_delta)<=F(A/4)`, and the exact quarter-shift bound

\[
                         F(A/4)<{1129\over25000}
\]

gives

\[
 \Gamma(\delta)
 <{1\over20000}+{1129\over25000}-{57\over1400}
 ={3147\over700000}.
\]

Positivity is immediate from the definition. \(\square\)

## 3. Exact elimination of the first residue

For every `tau>=A`, every interior critical point of `F_tau` on
`[0,A/2]` is a strict local maximum.  Since `0<=x<=u<A/4`,

\[
 \boxed{
 F_\tau(x)\ge\min\{C(\tau),F_\tau(u)\}.}
\tag{3.1}
\]

No monotonicity assumption is used: (3.1) is the exact endpoint-minimum
consequence of the period-uniform critical-point theorem.

Define the correlated literal rectangle gate

\[
\boxed{
\begin{aligned}
 \mathfrak R(\delta,P,u)={}&C(\tau)+F_\tau(P)+F_\tau(P+u)\\
 &+\min\{C(\tau),F_\tau(u)\}-\Gamma(\delta),
 \qquad \tau=A+\delta.
\end{aligned}}
\tag{3.2}
\]

Its compact closed parameter domain is

\[
\boxed{
\begin{aligned}
 \mathcal D={(\delta,P,u):;&\delta_*\le\delta\le A/2,\\
 &2(A+\delta)/3\le P\le A,\\
 &0\le u\le\min(A-P,P/4)\}.
\end{aligned}}
\tag{3.3}
\]

### Theorem 3.1 (single correlated-gate reduction)

Every residual physical inert `h=4` table satisfies

\[
                         \boxed{\Phi>\mathfrak R(\delta,P,u).}
\tag{3.4}
\]

Consequently complete physical `h=4` positivity follows from the single
compact assertion

\[
                         \mathfrak R>0\quad\hbox{on }\mathcal D.
\tag{3.5}
\]

Conversely, any nonpositive physical table forces

\[
 \delta_*<\delta<A/2,
 \qquad
 (\delta,P,u)\in\mathcal D,
 \qquad
 \mathfrak R(\delta,P,u)<0.
\tag{3.6}
\]

#### Proof

Start from the literal train (0.3).  Apply Lemma 2.1 to `y,z` and (3.1)
to `x`.  The four unaltered trains are exactly the rectangle (1.4), giving
(3.4).  The first assertion of (3.6) uses the already-proved local gate
interval (0.5); strict negativity of `mathfrak R` follows from
`Phi>mathfrak R` and `Phi<=0`. \(\square\)

The reduction is strictly stronger than the former pair-plus-singleton
relaxation in the only sense needed here: `P` and `P+u` remain coupled to
the same low displacement `u`, and the two other residues retain the
physical inequality `y+z<P+u<A`.

## 4. The former far-end obstruction disappears

At the formal endpoint `delta=A/2`, the domain (3.3) collapses to the
single point

\[
                         (P,u)=(A,0).
\tag{4.1}
\]

The ceiling train is increasing, so

\[
                         C(3A/2)>C(6A/5)>{63\over1000}.
\tag{4.2}
\]

Also

\[
 F_{3A/2}(A)
 =-\sum_{q\ge0}e^{-(2A+3qA/2)^2}>-{11\over250}.
\tag{4.3}
\]

For completeness, `e^{-pi}<2161/50000`.  Successive terms in (4.3) have
ratio below `1/480`: the first exponent gap is `33pi/16>99/16`, and the
positive Taylor polynomial proves `e^{99/16}>480`; later gaps are larger.
Thus

\[
 \sum_{q\ge0}e^{-(2A+3qA/2)^2}
 <{2161\over50000}{1\over1-1/480}<{11\over250}.
\]

### Theorem 4.1 (uniform far-end positivity)

One has

\[
\boxed{
 \mathfrak R(A/2,A,0)>{23453\over700000}>0.}
\tag{4.4}
\]

Consequently there exists `eta_0>0` such that

\[
 \boxed{
 \mathfrak R(\delta,P,u)>0}
\tag{4.5}
\]

for every point of `mathcal D` with

\[
                         A/2-\eta_0<\delta\le A/2.
\]

#### Proof

At (4.1), the low minimum in (3.2) is `C(3A/2)`.  Equations
(2.5), (4.2), and (4.3) give

\[
\begin{aligned}
 \mathfrak R(A/2,A,0)
 &>2{63\over1000}-2{11\over250}-{3147\over700000}\\
 &={23453\over700000}>0.
\end{aligned}
\]

The gate is continuous on the compact domain.  If (4.5) failed in every
far-end neighborhood, there would be a sequence with `delta->A/2` and
`mathfrak R<=0`.  The domain constraints force `P->A` and `u->0`,
contradicting (4.4). \(\square\)

Thus the negative values of the former decoupled gates near `A/2` cannot
come from physical endpoint trains.  They require incompatible choices of
the independent reflected-pair bases.

## 5. Exact finite KKT locus of the remaining gate

Write

\[
 T_\tau(w)=F_\tau'(w),
 \qquad
 R_\tau(w)=\partial_\tau F_\tau(w).
\tag{5.1}
\]

There are only two smooth low branches:

\[
 \mathrm C:\quad F_\tau(u)\ge C(\tau),
 \qquad
 \mathrm U:\quad F_\tau(u)\le C(\tau).
\tag{5.2}
\]

There is one `Gamma` switch,

\[
                         F((A-\delta)/2)=L.
\tag{5.3}
\]

On its active side,

\[
 \Gamma'(\delta)=-{1\over2}T_A((A-\delta)/2),
\tag{5.4}
\]

while on its inactive side `Gamma'=0`.

### Proposition 5.1 (interior stationary systems)

At an interior smooth stationary point on branch `C`,

\[
\boxed{
\begin{aligned}
 T_\tau(P)&=0,\\
 T_\tau(P+u)&=0,\\
 2R_\tau(0)+R_\tau(P)+R_\tau(P+u)-\Gamma'(\delta)&=0.
\end{aligned}}
\tag{5.5}
\]

At an interior smooth stationary point on branch `U`,

\[
\boxed{
\begin{aligned}
 T_\tau(P)+T_\tau(P+u)&=0,\\
 T_\tau(u)+T_\tau(P+u)&=0,\\
 R_\tau(0)+R_\tau(u)+R_\tau(P)+R_\tau(P+u)
 -\Gamma'(\delta)&=0.
\end{aligned}}
\tag{5.6}
\]

#### Proof

Differentiate (3.2) in the free variables.  On branch `C`, the low
minimum contributes a second copy of `C(tau)`.  The `u` equation first
gives `T_tau(P+u)=0`, and the `P` equation then gives `T_tau(P)=0`.
On branch `U`, all four rectangle shifts differentiate literally. \(\square\)

### Proposition 5.2 (complete boundary and nonsmooth list)

Every remaining minimum of `mathfrak R` on `mathcal D` lies at one of:

1. `delta=delta_*` or the far-end boundary covered by Theorem 4.1;
2. `P=2tau/3` or `P=A`;
3. `u=0`, `u=A-P`, or `u=P/4`;
4. the upper-bound switch `P=4A/5`;
5. the low-branch switch `F_tau(u)=C(tau)`;
6. the `Gamma` switch (5.3);
7. one of the smooth systems (5.5)--(5.6).

At a tie or intersection of these strata, the correctly oriented
one-sided local-minimum inequalities replace the corresponding equality
derivatives.  On the moving boundary `P=2tau/3`, the outer derivative is
obtained from (5.5) or (5.6) by adding

\[
 {2\over3}\bigl(T_\tau(P)+T_\tau(P+u)\bigr).
\tag{5.7}
\]

The other moving boundaries are handled by the same chain rule.  This is
a finite exact KKT list; no independent pair minima or hidden availability
case remains.

## 6. What has and has not been proved

The theorem proves:

1. the physical residual has one additive rectangle `0,u,P,P+u`;
2. the other residue pair costs at most the explicit one-dimensional
   charge `Gamma(delta)<3147/700000`;
3. every nonpositive physical table forces one compact correlated gate
   `mathfrak R<0`;
4. that gate is uniformly positive near the far endpoint, so the previous
   negative gate endpoint is a sharp no-go for the **decoupling**, not for
   physical `h=4`;
5. every unresolved minimum obeys the finite KKT list in Section 5.

It does not sign `mathfrak R` on the full interior of `mathcal D` and
therefore does not close six-slot `h=4`, complete six-slot Bellman
positivity, or any OR-word construction.

## 7. Frozen dependencies

| role | file | SHA-256 |
|---|---|---|
| literal endpoint-period/two-gate reduction | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| canonical `h=4` physical constraints | `MATH_THEOREM_SIX_SLOT_FOUR_EFFICIENT_SEVEN_CORRECTION_REDUCTION_20260804.md` | `fa362d05e586749467f9d5acb5f20883825d82505da71fba97fec678b4c213f9` |
| period-uniform no-interior-minimum theorem | `MATH_THEOREM_SIX_SLOT_H4_REDUNDANT_ENDPOINT_THREE_BLOCK_SCALAR_KKT_REDUCTION_20260804.md` | `f410d86f5d544755c08f269ece1d47910f2d3c055be91c7a391bb548090f53d3` |
| corrected local gate interval | `MATH_THEOREM_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_20260804.md` | `badc46480b85ef794e784ca2f62273aa6258cdf3dcfecbd915553102c6acd6af` |
| final independent GO audit of local interval | `MATH_AUDIT_SIX_SLOT_H4_OUTER_GATE_LOCAL_SIGN_AND_RESIDUAL_KKT_FINAL_GO_CROSS_20260804.md` | `5781c83357c77dd8216ecbb24ab4739e779d0c65751c7f8aecce1ef43b6ae46c` |
| Jacobi reflection and half-band estimates | `MATH_THEOREM_APERY_LONG_WRAP_EUCLIDEAN_SHIFT_AND_THETA_RESIDUAL_20260804.md` | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |
| sharp quarter-shift bounds | `MATH_THEOREM_H4_INERT_COMPACT_GAUSSIAN_GATE_CLOSURE_20260804.md` | `f88e8ac246d0533f018b7d713cfc6f09e14872d2f2026e7e29b3bc40f3a6062b` |
