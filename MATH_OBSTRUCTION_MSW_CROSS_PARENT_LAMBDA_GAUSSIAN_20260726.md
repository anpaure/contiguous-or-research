# The literal MSW cross-parent collision count: a persistent marked-gap obstruction

Date: 2026-07-26

## 0. Outcome

The cross-parent excess criterion

\[
 \Lambda_{\mathcal Q}
 =\sum_{(q,S)}w_q
   \left(d(q,S)-\max_Cd_C(q,S)\right)=o(W)              \tag{0.1}
\]

is false for the complete literal Catalan parent family on a Gaussian
window.

Put

\[
 k=m-r-1,\qquad
 H=H_{m,r+1}={1\over2}\binom{2k}{k},\qquad
 c=\operatorname {Cat}_{r-1},\qquad M=Hc.               \tag{0.2}
\]

There is a matching of

\[
 \boxed{
 K_k=(2k-3)\operatorname {Cat}_{k-2}
     ={k\over2(2k-1)}H}                                 \tag{0.3}
\]

pairs of distinct aligned parent contexts with the following property.
For every pair, one fixed suffix endpoint of all `c` switches in the first
packet is the same physical target as the corresponding endpoint of all
`c` switches in the second packet, simultaneously at every depth

\[
                         q=r+h,qquad1\le h\le k-1.      \tag{0.4}
\]

Consequently, at every such depth,

\[
 \boxed{
 \sum_S\left(d(q,S)-\max_Cd_C(q,S)\right)
 \ge cK_k={k\over2(2k-1)}M
          =\left({1\over4}+o(1)\right)M.}               \tag{0.5}
\]

Let the lower MWB quota and weight be

\[
 a_q={W\over\binom{2m+1}{m-q}},\qquad
 \kappa_q=\lfloor a_q\rfloor,qquad w_q={1\over\kappa_q}.             \tag{0.6}
\]

For fixed `A>0`, uniformly on `q<=A sqrt(m)`,

\[
                         w_q\ge e^{-A^2-o(1)}.           \tag{0.7}
\]

It follows that

\[
 \boxed{
 \Lambda_{[r+1,A\sqrt m]}^{\rm MWB}
 \ge\left({Ae^{-A^2}\over4}+o(1)\right)M\sqrt m
 =\Omega\left({W\sqrt m\over r^{3/2}}\right).}          \tag{0.8}
\]

At the fatal scale `r=Theta(log m)`, the right side is much larger than
`W`.  Even the first `Theta(r^(3/2))` depths after `r` contribute
`Omega(W)`.

Thus the packet-TU deletion theorem remains correct, but its exceptional
incidence hypothesis cannot hold for the complete parent atlas.  The
obstruction consists of same-sign suffix stars, not determinant-two
triangles.  Hence (0.8) does not by itself prove an integral gap for the
cap objective.  It proves that cross-parent incidences cannot be paid
literally and that a successful Gaussian rounding theorem must retain and
rebundle these persistent fibres.

---

## 1. Literal endpoint equality

For a parent context `C`, depth `q`, parity arm
`a in {E,O}`, and exceptional endpoint
`xi in {beta_C,gamma_C}`, write

\[
 T^{a,\mathrm{suf},\xi}_{C,q}
  =K^{a,\mathrm{suf}}_{C,q}\cup\{\xi\},
 \qquad
 T^{a,\mathrm{pre},\xi}_{C,R,q}
  =K^{a,\mathrm{pre}}_{C,R,q}\cup\{\xi\}.              \tag{1.1}
\]

The signs are prescribed by the four-arm formula and play no role in
set equality.

For any two endpoint presentations `K union {xi}` and `L union {zeta}`,
where the displayed endpoint is absent from its own core, equality holds
if and only if one of the following mutually exclusive alternatives
holds:

\[
\begin{array}{ll}
\text{direct:}&\xi=\zeta\text{ and }K=L,\\
\text{one-label exchange:}&
 \xi\ne\zeta,\quad K\setminus L=\{\zeta\},\quad
 L\setminus K=\{\xi\}.                                 \tag{1.2}
\end{array}
\]

This is the exact set-theoretic classification of every prefix--prefix,
suffix--suffix, or mixed endpoint collision.

Inside one packet the prefix cores contain the complete insertion or
deletion set of the spectator `R`.  Thus they recover `R`, and the four
prefix endpoint supports are packet-private.  The suffix cores erase the
spectator and depend only on the exterior pointed context.  Therefore the
only high-multiplicity rows inside a packet are its four fixed suffix
rows.

For two parent contexts with the same affine hole embedding, (1.2)
reduces cross-parent suffix equality to equality of their truncated
exterior parity flags; their exceptional labels are literally the same.
The construction below lies in this direct case.  It also shows why
nestedness does not prevent collisions: the two contexts have the same
hole and differ only in an exterior two-node block immediately before its
pointed cut.  That whole block is invisible to every retained suffix in
(0.4).

A complete enumeration of the additional one-label-exchange and mixed
collisions is unnecessary for (0.8), since the direct suffix family alone
already violates (0.1).

---

## 2. The pointed marked-gap pair of parent contexts

Let `R` be a Dyck word of semilength `k-2`, and choose one of its
`2k-3` gaps.  At that pointed gap insert either

\[
                         d_0=1100,qquad d_1=1010.       \tag{2.1}
\]

Keep the same aligned size-`r+1` hole at the pointed cut immediately
after the inserted block.  This gives two distinct exterior one-hole
contexts, denoted

\[
                         C_{R,g}^{(0)},qquad C_{R,g}^{(1)}.              \tag{2.2}
\]

The insertion--erasure identity for the MSW flip permutation says that,
after rotating at this cut, their omitted-label words have the form

\[
 q(C_{R,g}^{(i)})=(\pi_i,t_0,t_1,\ldots,t_{2k-4},\star),
 \qquad |\pi_i|=4,                                      \tag{2.3}
\]

where

* `pi_0` and `pi_1` are the two four-label orders generated by (2.1);
* the outside word `(t_0,...,t_(2k-4))` is identical on the two sides;
* `star` is the common inner parent hole, with the same affine local
  labels `beta,gamma` on both sides.

The proof is the usual first-return induction

\[
 \rho(1u0v)=
 (a,\ a-\rho(\mu u),\ 1,\ a+\rho(v)),
 \qquad a=|u|+2,                                       \tag{2.4}
\]

together with concatenation.  If the gap lies in `v`, use the induction
hypothesis in the final block; if it lies in `u`, reverse-complement the
gap and use the affine reflection in the second block.  Erasing the four
inserted labels recovers `rho(R)` and the pointed cut in every case.

The same inverse proves injectivity of the pointed construction.  From a
pointed context one recovers the four labels immediately preceding the
hole cut, their order distinguishes `d_0` from `d_1`, and deletion of
those labels recovers `(R,g)`.  Hence no parent context occurs in two of
the pairs (2.2).

There are therefore exactly

\[
                         K_k=(2k-3)\operatorname {Cat}_{k-2}             \tag{2.5}
\]

pairwise context-disjoint marked-gap pairs.

---

## 3. Persistence through every deeper suffix

At global depth `q=r+h`, the suffix length in the four-arm formula is

\[
                         \ell=m-q-1=k-h.                \tag{3.1}
\]

The inserted four-label word in (2.3) lies immediately before the pointed
cut.  A suffix core after the cut reads one parity class of the common
outside word.  For example, one of the two parity suffixes is

\[
 \{t_0,t_2,\ldots,t_{2(k-h)-2}\},                       \tag{3.2}
\]

up to reversal caused by the fixed ambient orientation.  Formula (3.2)
is identical for `C_(R,g)^(0)` and `C_(R,g)^(1)` for every
`1<=h<=k-1`.

Choose one prescribed sign and exceptional endpoint, say the negative
`beta` endpoint of this suffix arm.  The two contexts have the same
physical `beta` label by construction.  Thus

\[
 \boxed{
 T_{C_{R,g}^{(0)},r+h}
 =T_{C_{R,g}^{(1)},r+h}
 \quad(1\le h\le k-1).}                                \tag{3.3}
\]

This is not a one-depth coincidence.  It is a complete common nested
suffix flag.  The two parent nodes have the same size and same hole, so no
ancestor can distinguish them inside the retained flag; their first
exterior divergence is the erased block `d_0/d_1` before the cut.

Every one of the `c=Cat_(r-1)` spectator switches in a parent packet uses
this same fixed suffix endpoint.  Hence, at the common target in (3.3),

\[
                    d_{C_{R,g}^{(0)}}=d_{C_{R,g}^{(1)}}=c.               \tag{3.4}
\]

---

## 4. Exact nonhome-incidence count at one depth

Several marked-gap pairs may share the same physical target.  This can
only strengthen the nonhome incidence.  More explicitly, fix one depth
and one target `S`, and suppose `t_S` contexts from the matching (2.2)
produce `S`.  Since the context pairs are disjoint, at most
`floor(t_S/2)` matched pairs use `S`.  The total incidence at `S` from
these contexts is `ct_S`, whereas the largest one-packet contribution is
`c`.  Therefore

\[
 ct_S-c\ge c\left\lfloor{t_S\over2}\right\rfloor.       \tag{4.1}
\]

Sum (4.1) over targets.  All `K_k` matched pairs are counted, giving

\[
 \sum_S\left(d(r+h,S)-\max_Cd_C(r+h,S)\right)
 \ge cK_k.                                              \tag{4.2}
\]

The ratio in (0.3) is exact.  Indeed,

\[
\begin{aligned}
 {K_k\over H}
 &= {2(2k-3)\over k-1}
    {\binom{2k-4}{k-2}\over\binom{2k}{k}}\\
 &=\boxed{{k\over2(2k-1)}}.                            \tag{4.3}
\end{aligned}
\]

Since `M=Hc`, equations (4.2)--(4.3) prove (0.5).

Only one of the four fixed suffix endpoints was used.  Prefix collisions,
the other suffix arm, complements, and one-label exchanges can only add
to `Lambda`.

---

## 5. MWB weighting through the Gaussian window

For the lower rank `m-q`, the exact quota ratio is

\[
 a_q={W\over N_q}
 =\prod_{j=0}^{q-1}{m+2+j\over m-j}.                    \tag{5.1}
\]

Uniformly for `q=O(sqrt(m))`,

\[
                         \log a_q={q(q+1)\over m}
                         +O(q^3/m^2).                   \tag{5.2}
\]

Hence, for fixed `A` and `q<=A sqrt(m)`,

\[
 a_q\le e^{A^2+o(1)},qquad
 {1\over\lfloor a_q\rfloor}\ge{1\over a_q}
       \ge e^{-A^2-o(1)}.                               \tag{5.3}
\]

Let `Q_A=floor(A sqrt(m))`.  Since `r=Theta(log m)=o(sqrt(m))`, (0.5)
and (5.3) give

\[
\begin{aligned}
 \Lambda_{[r+1,Q_A]}^{\rm MWB}
 &\ge e^{-A^2-o(1)}(Q_A-r)cK_k\\
 &=\left({Ae^{-A^2}\over4}+o(1)\right)M\sqrt m.         \tag{5.4}
\end{aligned}
\]

At the fatal Catalan scale,

\[
 M=H_{m,r+1}\operatorname {Cat}_{r-1}
  =\left({1\over64\sqrt\pi}+o(1)\right)
       {W\over r^{3/2}}.                                \tag{5.5}
\]

Substitution proves (0.8).

There is a cutoff-free positive-density version.  Put

\[
                         L=\lfloor r^{3/2}\rfloor.      \tag{5.6}
\]

Then `r+L=o(sqrt(m))`, so all corresponding MWB weights are `1-o(1)`.
Equations (0.5) and (5.5) give

\[
 \boxed{
 \Lambda_{[r+1,r+L]}^{\rm MWB}
 \ge\left({1\over256\sqrt\pi}+o(1)\right)W.}           \tag{5.7}
\]

Thus an `Omega(W)` collision ledger is already forced long before the
edge of the Gaussian band.

---

## 6. What this obstruction does and does not prove

The following conclusions are literal.

1. The complete fixed-scale Catalan parent atlas contains a positive
   density of paired exterior contexts whose one fixed suffix arm agrees
   through a nested run of depths.
2. The nonhome-incidence metric of the packet-TU deletion theorem is
   `Omega(W)` on `Theta(r^(3/2))` shallow depths and
   `Omega(W sqrt(m)/r^(3/2))` on a fixed Gaussian window.
3. Therefore deleting or paying every cross-parent incidence cannot give
   coefficient-one Gaussian rounding.

The collision rows have the same sign in the paired columns and each
packet contributes a star of `c` identical incidences.  No odd-cycle sign
is produced by this argument.  Accordingly it does **not** prove

\[
             K^{\mathbb Z}-K^{\rm LP}=\Omega(W).         \tag{6.1}
\]

Nor does it refute saturation rounding, packet-sum dependent rounding, or
a quotient which treats each persistent marked-gap fibre as one atom.  It
does show exactly what such a theorem must exploit: the common suffix
fibre must be retained and rounded coherently rather than declared an
exception.

The revised Gaussian rounding gate is therefore:

> Contract every persistent marked-gap suffix fibre, prove that the
> resulting quotient has `o(W)` nonhome incidence or an integral packet
> polytope, and simultaneously control the variable prefix arms and the
> state-dependent opposite-boundary interactions.

This is strictly stronger than packetwise TU and strictly more specific
than generic laminar discrepancy.
