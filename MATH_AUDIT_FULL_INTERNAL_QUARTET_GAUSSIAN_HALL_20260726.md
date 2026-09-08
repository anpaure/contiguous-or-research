# Audit of the full internal-quartet Gaussian Hall cut

Date: 2026-07-26

Source audited:
`MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md`.

## 0. Verdict

The theorem is correct as stated for even `m` and the fixed partition into
quartets.

In particular:

* the number of full quartets is an exact invariant of every lower window
  using only block-internal coordinate exchanges;
* the profile coefficient formulas are exact;
* the mean, variance, and local-CLT calculation give
  `exp(-A^2/11)` with the stated sign;
* the selected `Theta_A(sqrt(m))` window has positive conditional mass in
  the exact rank-`m-q` layer;
* the profile deficits add without source reuse; and
* the crossing-axis consequence and its `q/r` dilution are correct for a
  final owner-disjoint `Q_r` packet tiling into isometric `C_(2r)` cycles.

No option in the full block-internal `J(4,1)`, `J(4,2)`, `J(4,3)` atlas
can change a full quartet without using a physically cross-quartet axis.
Thus this theorem supplies the missing capacity result identified in
`MATH_AUDIT_QUARTET_RESOLUTION_STRUCTURED_CPM_20260726.md`.

Two scope qualifications should remain explicit.

1. Equation (0.5) is a statement about the **final owner-disjoint packet
   tiling**.  It should not be summed over an overlapping catalogue of
   candidate trades.
2. The numerical `q/r` conversion uses isometric `C_(2r)` packet cycles
   and `q<r`.  The Hall invariant itself is more general, but that
   occurrence calculation is not automatically valid for an arbitrary
   non-packet compiler.

These are scope clarifications, not errors in the source.

## 1. The invariant is exact

Let `X` be any owner in a lower depth-`q` window and let `T` be the
intersection of that window.

An exchange internal to a quartet removes one occupied coordinate and
adds one unoccupied coordinate in the same quartet.  Therefore the local
cardinality of every owner is constant along such an exchange.  More
decisively, a full quartet has no unoccupied coordinate and hence is
incident with no internal Johnson edge at all.

It follows that:

* if a quartet is full in `X`, no internal direction can act there, so it
  is full in every owner of the window and hence in `T`;
* if it is full in `T`, then `T subseteq X` forces it to be full in `X`.

Thus

\[
                         F(T)=F(X).                    \tag{1.1}
\]

This proof does not depend on which one-factor of a local Johnson graph
is used, on the active-set choice, on the direction order, or on a
compiler conjugate.  It even survives repeated internal directions.

There is no hidden internal escape.  To leave a full quartet, a middle
owner must remove one of its four coordinates and insert a coordinate
outside that quartet.  The corresponding physical exchange pair crosses
two quartets.

For upper windows the complementary invariant is the number of empty
quartets.

## 2. Exact profile coefficients

After choosing `k` full quartets, every other quartet is a proper subset,
with polynomial

\[
                         h(z)=1+4z+6z^2+4z^3.
\]

Hence

\[
\begin{aligned}
 |\mathcal T_{q,k}|
   &=\binom ck[z^{m-q-4k}]h(z)^{c-k},\\
 |\mathcal X_k|
   &=\binom ck[z^{m-4k}]h(z)^{c-k}.
\end{aligned}                                           \tag{2.1}
\]

The common binomial factor really does cancel in the ratio.  The
normalized coefficient variable has

\[
 \Pr(J=j)={\binom4j\over15},\qquad 0\le j\le3.
\]

Direct calculation gives

\[
 \mathbb EJ={28\over15},
 \qquad
 \mathbb EJ^2={64\over15},
 \qquad
 \operatorname{Var}J={176\over225}.                  \tag{2.2}
\]

The support contains consecutive integers, so the lattice span is one;
no parity correction is missing from the local CLT.

## 3. The exponent `-A^2/11`

Put

\[
 q=A\sqrt m+O(1),qquad
 k={m\over32}+y\sqrt m+O(1),qquad
 d=c-k.
\]

Then

\[
 d={15m\over32}-y\sqrt m+O(1),
 \qquad
 \sigma^2d={11m\over30}+O(\sqrt m).                  \tag{3.1}
\]

For

\[
 s_T=m-q-4k,qquad s_X=m-4k,
\]

one obtains

\[
\begin{aligned}
 s_T-\mu d&=\left(-A-{32y\over15}\right)\sqrt m+O(1),\\
 s_X-\mu d&=-{32y\over15}\sqrt m+O(1).
\end{aligned}                                           \tag{3.2}
\]

The span-one local CLT therefore gives

\[
\begin{aligned}
 \log{|\mathcal X_k|\over|\mathcal T_{q,k}|}
 &=-{(s_X-\mu d)^2-(s_T-\mu d)^2\over2\sigma^2d}+o(1)\\
 &={15A^2+64Ay\over11}+o(1).                          \tag{3.3}
\end{aligned}

At `y=-A/4`, the numerator is `(15-16)A^2`, so

\[
                         {|\mathcal X_k|\over
                           |\mathcal T_{q,k}|}
                         \longrightarrow e^{-A^2/11}. \tag{3.4}
\]

On the interval `|y+A/4|<=A/128`, the exponent in (3.3) is at most
`-A^2/22+o(1)`.  Both the constant and the sign in the source are correct.

## 4. Positive exact-rank mass

Let a Bernoulli parameter be

\[
                         p={m-q\over2m}
                          ={1\over2}-{A\over2\sqrt m}+O(m^{-1}).
\]

Conditioning the product law on total rank `m-q` is exactly the uniform
target layer.  Before conditioning, the full-quartet indicator `I` and
the local rank `Y` satisfy, at `p=1/2`,

\[
 \operatorname{Var}I={15\over256},qquad
 \operatorname{Cov}(I,Y)={1\over8},qquad
 \operatorname{Var}Y=1.
\]

Consequently the conditional variance per quartet is

\[
                         {15\over256}-{1\over64}
                         ={11\over256}>0.              \tag{4.1}
\]

and the conditioned full-quartet count has variance `Theta(m)`.  Its
conditional mean is

\[
 cp^4={m\over32}-{A\over8}\sqrt m+O(1).              \tag{4.2}
\]

The chosen window is centered at

\[
                         {m\over32}-{A\over4}\sqrt m,
\]

a fixed number of conditional standard deviations from (4.2), and has
width `Theta_A(sqrt(m))`.  A conditional bivariate local CLT therefore
assigns it a positive limiting mass `c_A>0` for every fixed `A>0`.

Thus the use of a positive fraction of the exact target layer is valid;
it is not an unconditioned Bernoulli heuristic.

## 5. Hall deficit and crossing toll

For each `k`, all internally compatible sources of targets in
`T_(q,k)` lie in the disjoint source family `X_k`.  Since one owner has
only one depth-`q` start, at least

\[
                         (|\mathcal T_{q,k}|-|\mathcal X_k|)_+
                                                               \tag{5.1}
\]

targets of that profile are missed.  The source families for distinct
`k` are disjoint, so these deficits add.  Combining Sections 3--4 gives

\[
 (c_A-o(1))(1-e^{-A^2/22})N_q                         \tag{5.2}
\]

holes, and

\[
                         {N_q\over W}\longrightarrow e^{-A^2}.
                                                               \tag{5.3}
\]

This proves a positive coefficient `delta_A` exactly as claimed.

Now let a final packet tiling have `B` depth-`q` occurrences whose
windows contain at least one cross-quartet axis.  The other occurrences
still obey (1.1), so they can cover at most `|X_k|` targets in profile
`k`; the `B` exceptional occurrences cover at most `B` additional
targets in total.  Hence the lower-hole count is at least

\[
                         (\delta_A-o(1))W-B.           \tag{5.4}
\]

Therefore successful coverage needs `B=Omega_A(W)`.

In an isometric `C_(2r)`, one fixed axis occurs twice and belongs to
exactly `2q` cyclic depth-`q` windows when `q<r`.  Thus it appears in a
`q/r` fraction of starts.  If packet `P` has `s(P)` cross-quartet axes,
the union bound gives

\[
 B\le\sum_P{s(P)q\over r}|P|.                        \tag{5.5}
\]

Combining (5.4)--(5.5) yields

\[
 {1\over W}\sum_Ps(P)|P|=\Omega_A(r/q).              \tag{5.6}
\]

This is the correct owner-weighted average.  It does not assert that
every packet individually has that many crossing axes.

## 6. Scope

The theorem closes the capacity gap for the complete **block-internal**
quartet atlas.  It does not construct the required dense-cross-axis
tiling or prove `HCRT`.  It also does not by itself handle odd `m`; that
requires a harmless residual-coordinate version or the existing parity
transfer.

