# The all-block conjugate has linear edit moment

Date: 2026-07-26

Method: pure mathematics only.  No enumeration, solver, or numerical
experiment is used.

Let (F_s) be the canonical anchored (D_s)-port Chung--Feller factor,

\[
 \eta_s=\prod_{i=1}^{s-1}(2i\ \ 2i+1),
 \qquad
 G_s(P)=\eta_sF_s(\eta_sP),
 \qquad B=C_s.
\tag{0.1}
\]

The purpose of this note is to settle the sparse-edit question for this
explicit pair.  The conclusion is negative and does not depend on the
unknown sizes of the full ownership components:

\[
 \boxed{
 \Xi(F_s,G_s)\ge
 { (s-1)(s-2)\over 2s-1}
 =\left({1\over2}+o(1)\right)s.}
\tag{0.2}
\]

In particular, the hypothesis

\[
                         \Xi(F_s,G_s)=o(\sqrt s)
\tag{0.3}
\]

in the growing-port sparse-edit component theorem fails by a factor of
order (sqrt s).  This closes that theorem as a route for the literal
all-block pair.

The ownership components still have an exact phase-owner description and
an exact conjugacy pairing.  These give a separate carrier dichotomy:
the whole (F_s/G_s) displacement has zero order-two norm, while a
productive invariant direction can occur only by choosing opposite shores
in a pair of distinct components exchanged by (eta_s).  Thus component
asymmetry is the only possible carrier escape, but it does not repair
(0.2).

## 1. An alternating-order law for the MSW flip word

For a Dyck word (x=x_1\cdots x_{2s}), let
(ho(x)) be its MSW flip-coordinate permutation.  Recall the exact
recursion

\[
 \rho(1u0v)=
 \bigl(d,\ d-\rho(\mu(u)),\ 1,\ d+\rho(v)\bigr),
 \qquad d=|u|+2,
\tag{1.1}
\]

where (mu) is reverse-complement and affine operations on a word are
entrywise.  Notice that (d) is even.

### Lemma 1.1 (even coordinate first)

If two adjacent steps of a Dyck word are equal,

\[
                         x_j=x_{j+1},
\]

then the even coordinate among (j,j+1) occurs before the odd coordinate
in (ho(x)).

#### Proof

Induct on the semilength.  Write (x=1u0v) and put (d=|u|+2).

If (j=1), equality forces (u\ne\epsilon).  Coordinate (2) lies in
the inner block (d-ho(\mu(u))), which precedes coordinate (1) in
(1.1).  If (j=d-1), equality again forces (u\ne\epsilon), and the
closing coordinate (d) is the first entry in (1.1), so it precedes
(d-1).  At the remaining seam (j=d), the two steps are (0,1) when
(v\ne\epsilon), and hence are unequal.

For a pair wholly inside (v), the suffix shift is by the even number
(d), so parity and relative order are preserved and induction applies.

It remains to consider a pair wholly inside (u).  A global coordinate
(1+\ell), (1\le\ell\le d-2), corresponds in the inner block of
(1.1) to coordinate

\[
                         d-1-\ell
\]

of (mu(u)).  Adjacent coordinates are sent to adjacent coordinates in
reverse order.  Complementation preserves equality of their bits, and

\[
 (1+\ell)-(d-1-\ell)=2\ell-d+2
\]

is even, so the correspondence preserves the parity of each physical
coordinate.  Induction for (mu(u)) therefore again says that the even
physical coordinate occurs first.  These cases exhaust all adjacent
pairs.  (square)

## 2. Every equal block forces one rooted inversion

Write a Dyck port in the unique form

\[
                         P=1E0,
\tag{2.1}
\]

and split (E) into the (s-1) blocks occupying physical coordinates

\[
                 (2,3),(4,5),\ldots,(2s-2,2s-1).
\tag{2.2}
\]

Let

\[
 e(P)=\#\{,i:P_{2i}=P_{2i+1},}.
\tag{2.3}
\]

Thus (e(P)) is the number of (11)- and (00)-blocks in the associated
two-coloured Motzkin excursion.

Let (omega_F(P)) be the rooted coordinate word obtained by listing the
deletion order, then the insertion order, then the fixed anchor
(infty), and define (omega_G(P)) similarly.  Coordinate conjugacy
gives

\[
                         \rho_G(P)=\eta_s\rho_F(\eta_sP).
\tag{2.4}
\]

### Lemma 2.1 (equal-block inversion bound)

For every (P\in D_s),

\[
 \boxed{d_\infty(\omega_F(P),\omega_G(P))\ge e(P).}
\tag{2.5}
\]

#### Proof

Fix a block ((2i,2i+1)) counted by (e(P)).  The two bits are equal,
so (eta_sP) has the same two equal bits in that block.  Lemma 1.1 says
that (2i) precedes (2i+1) in both
(ho_F(P)) and (ho_F(\eta_sP)).  Applying (eta_s) to the latter
flip word reverses those two labels.  Hence (2i+1) precedes (2i) in
(ho_G(P)).

The two coordinates either both belong to (P) or both lie outside
(P).  They therefore occur in the same half of the rooted word: both in
the deletion list or both in the insertion list.  Extracting that half
from the alternating flip word preserves their relative order.  Thus the
pair contributes one distinct Kendall inversion between (omega_F(P))
and (omega_G(P)).  Summing over the disjoint blocks gives (2.5), since
rooted adjacent-transposition distance is Kendall distance.  (square)

## 3. Exact mean number of equal blocks

The middle word (E) in (2.1), read in two-letter blocks, is a
two-coloured Motzkin excursion of length

\[
                         r=s-1.
\]

The blocks (11,00,10,01) are respectively (U,D,H_+,H_-).  Mark each
vertical step by (u).  The generating function (M(z,u)) satisfies

\[
                         M=1+2zM+u^2z^2M^2.
\tag{3.1}
\]

At (u=1),

\[
                         M(z,1)=C(z)^2,
 \qquad [z^r]M(z,1)=C_{r+1}=C_s.
\tag{3.2}
\]

Differentiating (3.1), and writing
(t=\sqrt{1-4z}), gives the exact simplification

\[
 \left.\partial_uM(z,u)\right|_{u=1}
 =\frac{2z^2M(z,1)^2}{1-2z-2z^2M(z,1)}
 =\frac2t-2M(z,1).
\tag{3.3}
\]

Consequently the total number of equal blocks over all (C_s) ports is

\[
 \sum_{P\in D_s}e(P)
 =2\binom{2r}{r}-2C_{r+1}.
\tag{3.4}
\]

Using

\[
 \binom{2r}{r}=(r+1)C_r,
 \qquad
 \frac{C_{r+1}}{C_r}=\frac{2(2r+1)}{r+2},
\]

we obtain the exact mean

\[
 \boxed{
 {1\over C_s}\sum_{P\in D_s}e(P)
   ={r(r-1)\over2r+1}
   ={(s-1)(s-2)\over2s-1}.}
\tag{3.5}
\]

This also gives a simple support statement: (e(P)=0) only for the
(2^r) all-horizontal two-coloured Motzkin words.  Hence at least

\[
                         C_s-2^{s-1}=(1-o(1))C_s
\tag{3.6}
\]

rows have a certified rooted edit.

## 4. Linear lower bound for the exact component moment

Let ({\cal K}) be the full state-and-colour ownership components of
(F_s,G_s), with root blocks (R_K), sizes (b_K), and

\[
 D_K=\sum_{P\in R_K}
 d_\infty(\omega_F(P),\omega_G(P)).
\]

By definition,

\[
                         \Xi(F_s,G_s)
 ={1\over C_s}\sum_Kb_KD_K.
\tag{4.1}
\]

Since (b_K\ge1), Lemma 2.1 and (3.5) imply

\[
\begin{aligned}
 \Xi(F_s,G_s)
 &\ge {1\over C_s}\sum_KD_K\\
 &= {1\over C_s}\sum_{P\in D_s}
       d_\infty(\omega_F(P),\omega_G(P))\\
 &\ge {1\over C_s}\sum_{P\in D_s}e(P)\\
 &=\frac{(s-1)(s-2)}{2s-1}.
\end{aligned}
\tag{4.2}
\]

This proves (0.2).  In particular, no fragmentation theorem for this
overlay, even a decomposition into singleton-sized components, can make
the all-block endpoint pair satisfy the sparse-edit condition (0.3).

The conclusion concerns the sufficient sparse-edit moment.  It does not
assert that the true component variance must equal its sparse-edit upper
bound; a different cancellation theorem could in principle use more than
word distance.

## 5. Exact ownership-component normal form

Although their sizes are unnecessary for (4.2), the components admit an
exact description.  Write the canonical alternating tokens as

\[
 Z_{2a}(P)=X_a^F(P),\qquad
 Z_{2a+1}(P)=Y_a^F(P),
\]

and let (o_F(T)) be the canonical owner of token (T) in its ledger.
Define

\[
 \kappa_\ell(P)=o_F(\eta_sZ_\ell(P)),
 \qquad
 f_\ell=\kappa_\ell\eta_s.
\tag{5.1}
\]

Here (kappa_0=\eta_s), so (f_0=1).  After the common root-port edges
are contracted, the full ownership components are exactly the classes of
the least equivalence relation containing

\[
                         P\sim f_\ell(P)
 \qquad(0\le\ell\le2s).
\tag{5.2}
\]

This is an equivalence closure, not in general a group-orbit formula:
the odd (Y)-owner maps need not be injective.  Formula (5.2) is the
complete component description available without an additional theorem
about the phase-owner maps.

There is also an involution on the component set.  Applying (eta_s)
to every token and exchanging the two shores is an overlay automorphism;
after port contraction it sends a root block (K) to

\[
                         K^*=\eta_sK.
\tag{5.3}
\]

Thus every component is either self-conjugate or belongs to a two-element
pair.

## 6. The exact carrier dichotomy

Let (u_K) be any coordinate-equivariant occurrence profile contributed
by the (F_s)-rows rooted in (K).  The (G_s)-profile on the same root
block is (eta_su_{K^*}), so the component increment is

\[
                         \Delta_K=\eta_su_{K^*}-u_K.
\tag{6.1}
\]

Therefore

\[
                         \Delta_{K^*}=-\eta_s\Delta_K.
\tag{6.2}
\]

If (K=K^*), then

\[
 \Delta_K=(\eta_s-1)u_K,
 \qquad
 (1+\eta_s)\Delta_K=0.
\tag{6.3}
\]

So a self-conjugate component has zero order-two carrier norm in every
equivariant profile.

For a paired component (K\ne K^*), let (s_K) be its formal exact
switch (G_K-F_K).  Then

\[
                         \eta_ss_K=-s_{K^*},
\tag{6.4}
\]

and hence

\[
                         s_K-s_{K^*}
\tag{6.5}
\]

is an invariant exact tangent.  It is the difference of the two literal
exact children which choose opposite shores on (K,K^*).  Its carrier is

\[
 \Delta_K-\Delta_{K^*}
   =(1+\eta_s)\Delta_K.
\tag{6.6}
\]

Consequently the cyclic carrier theorem gives the exact criterion

\[
 \boxed{
 \text{productive order-two carrier}
 \iff
 \exists K\ne K^*:\ (1+\eta_s)\Delta_K\ne0.}
\tag{6.7}
\]

The whole-factor displacement is

\[
 \mu_q^{G_s}-\mu_q^{F_s}
  =(\eta_s-1)\mu_q^{F_s},
\]

and therefore always has zero norm:

\[
 (1+\eta_s)(\mu_q^{G_s}-\mu_q^{F_s})=0.
\tag{6.8}
\]

Thus the two complete shores by themselves are a carrier no-go.  A
productive full-profile hinge, if this pair has one at all, must come from
an asymmetric choice in a non-self-conjugate component pair and must pass
(6.7).  Conjugacy alone neither supplies such a pair nor proves its
carrier nonvanishing.

At (s=3), the displayed old/new pentagon paths give a useful exact
calibration.  The first phase already induces a five-cycle on the roots,
so the full overlay is connected and self-conjugate.  The five rooted
distances are

\[
                         2,6,4,6,4,
\]

with total (22).  Hence the sole component has

\[
                         \Xi(F_3,G_3)=22,
\]

and (6.7) is unavailable.  This finite calibration is not used in the
general proof.

## 7. Final status for the all-block pair

The following are now proved.

1. The ownership components are the exact phase-owner equivalence classes
   (5.2), paired by (K\mapsto\eta_sK).
2. Their unknown size distribution is irrelevant to the sparse-edit gate:
   the row words alone force the linear lower bound (0.2).
3. The global all-block displacement is norm-zero in every equivariant
   carrier, so serial repetition of the two whole shores is unproductive.
4. The only carrier escape is the precisely stated paired-component
   condition (6.7).

What remains open is a closed enumeration of the classes (5.2), and
whether any paired class satisfies (6.7) for the required physical
full-profile carrier.  Neither question can rescue this explicit pair for
the sparse-edit theorem, because (0.2) already violates its quantitative
hypothesis.
