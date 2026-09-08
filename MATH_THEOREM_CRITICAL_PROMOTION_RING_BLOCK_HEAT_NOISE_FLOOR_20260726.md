# Critical full-top promotion rings: the exact block heat identity and its noise-floor obstruction

Date: 2026-07-26

Pure mathematics only.  No computation, search, solver, or probabilistic
rounding theorem is used.

## 0. Result

Put

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad
 \lambda_q={W\over N_q}.
 \tag{0.1}
\]

Let \(H\) be the least integer for which

\[
 \lambda_H\ge m+H,
 \qquad M=m+H,
 \qquad \mathcal U=\binom{[2m]}M.
 \tag{0.2}
\]

Thus

\[
 H=(1+o(1))\sqrt{m\log m},\qquad
 N_H=(1+o(1)){W\over m},\qquad
 MN_H=W-o(W).
 \tag{0.3}
\]

For \(0\le q\le H\), define the nested, identical per-top census

\[
 s_q=\min\left\{M,\left\lfloor{N_q\over N_H}\right\rfloor\right\}.
 \tag{0.4}
\]

Then \(s_0=M\), \(s_H=1\), and \(s_q\) is nonincreasing.  Hence one
may put exactly

\[
 a_H=1,\qquad a_d=s_d-s_{d+1}\quad(0\le d<H)
 \tag{0.5}
\]

tag-\(d\) chains in every full-top promotion ring.  This is a literal
tagged version of the ring in Theorem 3.6 of
`MATH_THEOREM_EP_MULTISCALE_ROTOR_AND_CONTEXT_HALL_OBSTRUCTION_20260726.md`.
Its cumulative rank-\(q\) census is \(s_q\) per top.

This note proves the following.

1. The scalar census defect is negligible:
   \[
    h_0+2\sum_{q=1}^Hh_q=o(W),
    \qquad h_q:=N_q-N_Hs_q\ge0.
    \tag{0.6}
   \]
   Thus the profile is an approximate SCD census at the aggregate-mask
   accuracy actually needed by the compiler.

2. Choose one tagged cyclic ring at every top.  Resample the ring at one
   uniformly chosen top from the full cyclic catalogue, keeping the tag
   profile (0.5) fixed.  If \(\Phi\) is the sum, over all central ranks,
   of the floor-correct pair-collision energies, then there is an exact
   constant \(\Phi_{\rm heat}\) such that
   \[
    \boxed{
    \mathbb E[\Phi' -\Phi_{\rm heat}\mid\Phi]
      =\left(1-{2\over N_H}\right)
       (\Phi-\Phi_{\rm heat}).}
    \tag{0.7}
   \]
   This is an exact block identity, not an asymptotic spectral estimate.

3. The fixed point in (0.7) is
   \[
    \boxed{
    \Phi_{\rm heat}
       =\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.}
    \tag{0.8}
   \]
   On the other hand, the integer floor baseline at every rank is zero,
   because \(N_Hs_q\le N_q\).  Therefore (0.8) is genuine avoidable
   collision mass, not a forced floor term which may be subtracted in a
   hole estimate.

4. For an arbitrary restricted component catalogue, its exact heat noise
   is one half of the average symmetric-difference replacement count.
   Consequently an \(o(W)\) heat floor requires two independent options
   at a typical top to differ in only \(o(m)\) chain-rank occurrences.
   Since a ring carries \((\sqrt\pi+o(1))m^{3/2}\) such occurrences,
   this means incidence-vector agreement on a
   \(1-o(m^{-1/2})\) fraction of the entire tagged carrier.  This is a
   necessary Hamming-overlap threshold for low-noise heat; by itself it
   does not imply coherent consecutive forced-tail agreement between the
   corresponding chain histories.

5. In a two-shore switch system the requirement is incompatible with
   linear repair capacity.  If \(D_U\) is the number of occurrence
   replacements between the two shores at top \(U\), then the heat noise
   contributes exactly \(\frac14\sum_UD_U\) to the stationary collision
   energy, up to the \(o(W)\) scalar census term.  If
   \(\sum_UD_U=o(W)\), every child differs from a fixed shore in only
   \(o(W)\) occurrences and hence cannot repair a linear hole mass.  If
   \(\sum_UD_U=\Omega(W)\), the heat floor is already \(\Omega(W)\).

Thus independent one-top heat, including adjacent-swap two-seed heat, does
not prove an \(o(W)\)-collision approximate SCD.  A surviving use of the
promotion-ring catalogue must be a globally correlated matching or an
aligned multi-top switch whose barycentric covariance is already
floor-negative.  It cannot be ordinary product block heat.

## 1. The canonical nested tag profile

Every cyclic order on a top \(U\in\mathcal U\) gives \(M\) chain slots.
Assign \(a_d\) of them tag \(d\), where (0.5) is used.  Since

\[
 \sum_{d=q}^Ha_d=s_q,
 \tag{1.1}
\]

exactly \(s_q\) chains in that ring reach each of the ranks \(m-q\) and
\(m+q\).  At tag \(H\) there is exactly one chain, as required for
within-ring mask disjointness at the common top.

Let

\[
 S_q=N_Hs_q,
 \qquad h_q=N_q-S_q.
 \tag{1.2}
\]

The floor and cap in (0.4) give \(h_q\ge0\).

### Lemma 1.1 (aggregate census defect)

One has (0.6).

#### Proof

If the minimum in (0.4) is not capped at \(M\), then

\[
 0\le h_q<N_H.
 \tag{1.3}
\]

There are \(H+1\) values of \(q\), and

\[
 HN_H=O(WH/m)=o(W).
 \tag{1.4}
\]

It remains to consider the capped ranks.  Write

\[
 T=MN_H,
 \qquad D_0=W-T.
 \tag{1.5}
\]

At a capped rank,

\[
 h_q=N_q-T\le D_0=O(WH/m).
 \tag{1.6}
\]

Capping also implies \(N_q\ge T\), and hence

\[
 \lambda_q\le {W\over T}={\lambda_H\over M}=1+O(H/m).
 \tag{1.7}
\]

Uniformly for \(q\le H=o(m^{2/3})\),

\[
 \log\lambda_q={q^2\over m}
   +O\left({q\over m}+{q^3\over m^2}\right).
 \tag{1.8}
\]

An elementary matching lower bound in (1.8) shows from (1.7) that every
capped \(q\) is \(O(\sqrt H)\).  Their total contribution is therefore

\[
 O(\sqrt H D_0)
  =O\left(W{H^{3/2}\over m}\right)=o(W),
 \tag{1.9}
\]

because \(H\sim\sqrt{m\log m}\).  Combining (1.3)--(1.9), and counting
the two signs for \(q>0\), proves (0.6). \(\square\)

The exact SCD radius census is

\[
 \gamma_d=N_d-N_{d+1}\quad(d<H),
 \qquad \gamma_H=N_H.
 \tag{1.10}
\]

The profile (0.5) has total tag-\(d\) count \(N_Ha_d\).  Since cumulative
census discrepancies are exactly the \(h_q\), its total variation from
(1.10) is at most

\[
 \sum_{d=0}^{H-1}|h_d-h_{d+1}|+h_H
 \le2\sum_{q=0}^Hh_q=o(W).
 \tag{1.11}
\]

Thus this is also an \(o(W)\)-accurate tag histogram, not merely a
rankwise scalar construction.

## 2. Tagged-ring incidence vectors

Use the disjoint target space

\[
 \mathcal X=\binom{[2m]}m
 \ \sqcup\!
 \bigsqcup_{q=1}^H
 \left(\binom{[2m]}{m-q}\sqcup
       \binom{[2m]}{m+q}\right).
 \tag{2.1}
\]

The two copies at depths \(q>0\) are rank-labelled.  For a tagged cyclic
ring \(\xi\) at top \(U\), let

\[
 v_U^\xi\in\{0,1\}^{\mathcal X}
 \tag{2.2}
\]

be its chain-mask incidence vector.  Theorem 3.6 cited above proves that
within one ring all active chain masks at a fixed rank are distinct.  Thus
the vector is genuinely binary.  Its squared norm is the fixed number

\[
 R=M+2\sum_{q=1}^Hs_q.
 \tag{2.3}
\]

The rank \(m+H\) coordinate is fixed by the top: its unique active chain
owns \(U\).

For \(0\le q\le H\), put

\[
 C_q^-=\binom M{m-q}=\binom M{H+q},
 \qquad
 C_q^+=\binom M{m+q}=\binom M{H-q}.
 \tag{2.4}
\]

At \(q=0\) the two expressions refer to the same middle cell and are
counted only once.

Let the catalogue at \(U\) consist of all cyclic orders, together with all
placements of the fixed tag multiset (0.5), and let \(\xi\) be uniform in
this catalogue.  Label symmetry gives the exact barycentre

\[
 \overline v_{U,q}^{\,-}(S)
 ={s_q\over C_q^-}\mathbf1_{\{S\subset U\}},
 \qquad
 \overline v_{U,q}^{\,+}(S)
 ={s_q\over C_q^+}\mathbf1_{\{S\subset U\}}.
 \tag{2.5}
\]

For the upper cell at \(q=H\), this says
\(\overline v_{U,H}^{\,+}=e_U\).

Indeed, each active phase of a uniform labelled cyclic order has a uniform
rank-\((m\pm q)\) interval in \(U\), and there are \(s_q\) active phases.
Distinctness within a ring ensures that no multiplicity correction is
hidden in (2.5).

Summing (2.5) over all tops gives a constant global barycentre in each
rank cell:

\[
 A_q^\pm(S):=\sum_{U\supset S}\overline v_{U,q}^{\,\pm}(S)
 ={N_Hs_q\over N_q}=:\mu_q.
 \tag{2.6}
\]

Here we used

\[
 {\binom{2m-(m\pm q)}{M-(m\pm q)}
   \over \binom M{m\pm q}}
 ={N_H\over N_q}.
 \tag{2.7}
\]

By construction \(0<\mu_q\le1\).

### Lemma 2.1 (exact one-ring variance)

Put \(g_U^\xi=v_U^\xi-\overline v_U\).  Then

\[
 \|g_U^\xi\|_2^2=\sigma^2
 \tag{2.8}
\]

for every catalogue choice \(\xi\), where

\[
 \begin{aligned}
 \sigma^2={}&R-{M^2\over C_0^-}\\
 &-\sum_{q=1}^H
 \left({s_q^2\over C_q^-}+{s_q^2\over C_q^+}\right).
 \end{aligned}
 \tag{2.9}
\]

In particular the final upper term is \(s_H^2/C_H^+=1\), expressing the
zero variance of the forced top coordinate.

#### Proof

In a rank cell containing \(s_q\) ones, (2.5) gives

\[
 \|v\|_2^2=s_q,\qquad
 \langle v,\overline v\rangle={s_q^2\over C_q^\pm},
 \qquad
 \|\overline v\|_2^2={s_q^2\over C_q^\pm}.
 \tag{2.10}
\]

Therefore that cell contributes
\(s_q-s_q^2/C_q^\pm\) to (2.8).  Sum the middle cell once and every
positive-depth cell twice. \(\square\)

## 3. Exact floor correction and block heat

We first record the integer baseline without assuming \(S\le N\).  If a
rank cell has \(N\) targets and total incidence \(S=aN+r\), where

\[
 a=\left\lfloor{S\over N}\right\rfloor,
 \qquad0\le r<N,
 \tag{3.1}
\]

then the minimum possible pair collision is

\[
 B(N,S)=N\binom a2+ar.
 \tag{3.2}
\]

For loads \(L_x\), define

\[
 \Phi_{N,S}(L)=\sum_x\binom{L_x}2-B(N,S).
 \tag{3.3}
\]

Writing \(S/N=a+\theta\), one has the exact identity

\[
 \boxed{
 \Phi_{N,S}(L)
 ={1\over2}\left(
   \left\|L-{S\over N}{\bf1}\right\|_2^2
       -N\theta(1-\theta)\right).}
 \tag{3.4}
\]

This follows by expanding both sides and using \(\sum_xL_x=S\).

For the canonical profile, \(S_q=N_Hs_q\le N_q\), so \(a=0\) and

\[
 \boxed{B(N_q,S_q)=0.}
 \tag{3.5}
\]

Let one ring \(\xi_U\) be selected at each top, and put

\[
 L=\sum_Uv_U^{\xi_U},\qquad
 G=\sum_Ug_U^{\xi_U}.
 \tag{3.6}
\]

Equation (2.6) says that in every rank cell

\[
 L=\mu_q\mathbf1+G,
 \qquad \langle\mathbf1,G\rangle=0.
 \tag{3.7}
\]

Let \(\Phi\) be the sum of (3.3) over the cells (2.1).  Equations
(3.4)--(3.7) give

\[
 \Phi={1\over2}\left(
       \|G\|_2^2-\sum_{\text{cells}}N_q\mu_q(1-\mu_q)
                         \right).
 \tag{3.8}
\]

Choose a top \(J\) uniformly from \(\mathcal U\), and replace
\(\xi_J\) by an independent uniform catalogue choice.  Conditional on the
current selection,

\[
 G'=G-g_J+g_J',
 \qquad \mathbb E g_J'=0,
 \qquad \mathbb E\|g_J'\|_2^2=\sigma^2.
 \tag{3.9}
\]

Since every current \(g_U\) also has norm \(\sigma\), summing over the
choice of \(J\) gives

\[
 \begin{aligned}
 \mathbb E[\|G'\|_2^2-\|G\|_2^2\mid G]
 &={1\over N_H}\sum_U
 \left(-2\langle G,g_U\rangle
       +\|g_U\|_2^2+\sigma^2\right)\\
 &=-{2\over N_H}\left(\|G\|_2^2-N_H\sigma^2\right).
 \end{aligned}
 \tag{3.10}
\]

Define

\[
 \boxed{
 \Phi_{\rm heat}={1\over2}\left(
 N_H\sigma^2-\sum_{\text{cells}}N_q\mu_q(1-\mu_q)
                              \right).}
 \tag{3.11}
\]

Substituting (3.10) into (3.8) proves the exact contraction identity
(0.7).

Notice its direction.  If \(\Phi>\Phi_{\rm heat}\), heat decreases the
energy.  If \(\Phi<\Phi_{\rm heat}\), heat increases it.  In particular,
an exact collision-free packing is repelled, in expectation, toward the
product-noise floor.

### Remark 3.1 (nonidentical prescribed profiles)

The same calculation has an exact two-harmonic form when the prescribed
counts \(s_{U,q}\) depend on \(U\).  Put

\[
 A=\sum_U\overline v_U,qquad
 G=\sum_U(v_U-\overline v_U),qquad
 \Sigma=\sum_U\sigma_U^2.
 \tag{3.12}
\]

Under one uniformly chosen block resampling,

\[
 \mathbb E\langle A,G'\rangle
   =\left(1-{1\over N_H}\right)\langle A,G\rangle,
 \tag{3.13}
\]

\[
 \mathbb E(\|G'\|_2^2-\Sigma)
   =\left(1-{2\over N_H}\right)(\|G\|_2^2-\Sigma).
 \tag{3.14}
\]

Thus the linear barycentre-cancellation mode and the quadratic noise mode
have different eigenvalues.  Ordinary heat destroys any negative linear
correlation needed to cancel its positive quadratic noise; it does not
turn that cancellation into a coercive estimate.

## 4. Evaluation of the heat floor

### Lemma 4.1 (total central census)

One has

\[
 S_0+2\sum_{q=1}^HS_q
   =(\sqrt\pi+o(1))W\sqrt m.
 \tag{4.1}
\]

#### Proof

Uniformly for \(q\le H\),

\[
 {N_q\over W}
 =\exp\left(-{q^2\over m}+o(1)\right),
 \tag{4.2}
\]

because \(H=o(m^{2/3})\).  Since \(H/\sqrt m\sim\sqrt{\log m}\to\infty\),
the Riemann sum gives

\[
 \sum_{q=0}^HN_q
  =\left({\sqrt\pi\over2}+o(1)\right)W\sqrt m.
 \tag{4.3}
\]

Lemma 1.1 permits replacing every \(N_q\) by \(S_q\) at an aggregate
cost \(o(W)\).  Equation (4.1) follows. \(\square\)

### Lemma 4.2 (the within-top mean-square correction)

Apart from the forced upper top coordinate,

\[
 N_H\left[{M^2\over C_0^-}
 +\sum_{q=1}^H
 \left({s_q^2\over C_q^-}+{s_q^2\over C_q^+}\right)-1\right]
 =o(W).
 \tag{4.4}
\]

#### Proof

For the middle and every lower cell,

\[
 C_0^-,C_q^-\ge\binom MH.
 \tag{4.5}
\]

Since \(s_q\le M\), their total contribution is at most

\[
 O\left({N_HHM^2\over\binom MH}\right)=o(W).
 \tag{4.6}
\]

For an upper cell write \(j=H-q\).  If \(2\le j\le H\), then

\[
 C_q^+=\binom Mj\ge\binom M2,
 \tag{4.7}
\]

so all these cells together contribute \(O(HN_H)=o(W)\).  For \(j=1\),

\[
 {N_{H-1}\over N_H}={m+H\over m-H+1}<2
 \tag{4.8}
\]

for large \(m\), whence \(s_{H-1}=1\), and the contribution is
\(N_H/M=o(W)\).  Finally \(j=0\) is the forced top coordinate, for which
\(s_H^2/C_H^+=1\).  Subtracting that displayed unit proves (4.4).
\(\square\)

Lemmas 4.1--4.2 and (2.9) imply

\[
 N_H\sigma^2=(\sqrt\pi+o(1))W\sqrt m.
 \tag{4.9}
\]

Moreover,

\[
 0\le N_q\mu_q(1-\mu_q)
 =S_q{h_q\over N_q}\le h_q.
 \tag{4.10}
\]

Lemma 1.1 therefore shows that the second term in (3.11) is \(o(W)\).
Equations (3.11) and (4.9) prove (0.8).

This asymptotic is the decisive baseline audit.  The true integer floor
baseline is zero by (3.5), while the product block-heat baseline is larger
than the permitted \(o(W)\) error by a factor of order \(\sqrt m\).
Already the middle cell alone has

\[
 \Phi_{{\rm heat},0}
 ={1\over2}\left[
 N_H\left(M-{M^2\over\binom MH}\right)
       -W\mu_0(1-\mu_0)\right]
 =\left({1\over2}+o(1)\right)W.
 \tag{4.11}
\]

Thus even discarding every nonmiddle rank does not leave an \(o(W)\)
product-heat baseline.

## 5. Collision energy controls aggregate holes

In a cell with \(S=N-h\le N\) occurrences, let \(H_{\rm cell}\) be its
number of uncovered targets.  Then

\[
 H_{\rm cell}=h+\sum_x(L_x-1)_+.
 \tag{5.1}
\]

Since

\[
 (L_x-1)_+\le\binom{L_x}2,
 \tag{5.2}
\]

one has

\[
 \sum_{\text{cells}}H_{\rm cell}
 \le h_0+2\sum_{q=1}^Hh_q+\Phi.
 \tag{5.3}
\]

Thus \(\Phi=o(W)\) would indeed prove an \(o(W)\)-hole approximate SCD.
But (0.7)--(0.8) show that full-catalogue product heat contracts toward
\(\Theta(W\sqrt m)\), not toward the regime required in (5.3).

## 6. Restricted catalogues and the exact incidence-agreement threshold

The obstruction is not peculiar to the uniform full catalogue.  Let
\(\mathcal C_U\) be any finite catalogue of tagged rings at top \(U\), all
with the same prescribed tag profile, and use its uniform measure.  Put

\[
 d_U(\xi,\eta)
 ={1\over2}\|v_U^\xi-v_U^\eta\|_2^2.
 \tag{6.1}
\]

Because the two binary vectors have the same number of ones in every rank
cell, \(d_U(\xi,\eta)\) is exactly the number of old chain-rank
occurrences which must be replaced to pass from \(\xi\) to \(\eta\).

### Lemma 6.1 (dispersion equals average replacement distance)

For two independent uniform choices \(\xi,\eta\in\mathcal C_U\),

\[
 \boxed{
 \sigma_U^2:=\mathbb E\|v_U^\xi-\overline v_U\|_2^2
 =\mathbb E d_U(\xi,\eta).}
 \tag{6.2}
\]

#### Proof

The standard polarization identity gives

\[
 \mathbb E\|v_U^\xi-\overline v_U\|_2^2
 ={1\over2}\mathbb E\|v_U^\xi-v_U^\eta\|_2^2.
 \tag{6.3}
\]

Now use (6.1). \(\square\)

Let \(A=\sum_U\overline v_U\).  Under the independent product measure on
the restricted catalogues, the expected raw pair collision is

\[
 \Phi_{\rm prod}
 ={1\over2}\left(\|A\|_2^2+\sum_U\sigma_U^2
                  -\sum_{\text{cells}}S_q\right),
 \tag{6.4}
\]

because the integer floor baseline is zero.  Cauchy--Schwarz in each rank
cell gives

\[
 \|A\|_2^2\ge\sum_{\text{cells}}{S_q^2\over N_q}.
 \tag{6.5}
\]

Therefore, using (0.6),

\[
 \boxed{
 \Phi_{\rm prod}
 \ge {1\over2}\sum_U\mathbb E d_U(\xi,\eta)-o(W).}
 \tag{6.6}
\]

Since \(N_H=(1+o(1))W/m\), an \(o(W)\) product heat floor necessarily
requires

\[
 {1\over N_H}\sum_U\mathbb E d_U(\xi,\eta)=o(m).
 \tag{6.7}
\]

By (2.3) and Lemma 4.1, a full tagged ring has

\[
 R=(\sqrt\pi+o(1))m^{3/2}
 \tag{6.8}
\]

chain-rank occurrences.  Thus (6.7) says that two typical available ring
options must agree on all but \(o(m)\) of them, namely on a fraction

\[
 1-o(m^{-1/2}).
 \tag{6.9}
\]

This is the exact incidence-agreement threshold.  The full cyclic catalogue has
average replacement distance \((\sqrt\pi+o(1))m^{3/2}\), so it violates
(6.7) by a factor of order \(\sqrt m\).

No chronological parsing is encoded in the distance \(d_U\).  Therefore
(6.9) must not be read as a sufficient long-tail theorem: converting
incidence agreement into one common consecutive physical tail would need
an additional matching/parsing lemma.  The separate monotone tag-path
construction supplies the required tails directly.

## 7. Two-shore switches: capacity versus noise

Suppose now that every top has exactly two options \(\xi_U^0,\xi_U^1\),
chosen with equal probability, and put

\[
 D_U=d_U(\xi_U^0,\xi_U^1).
 \tag{7.1}
\]

Then (6.2) specializes to

\[
 \boxed{\sigma_U^2={D_U\over2}.}
 \tag{7.2}
\]

Indeed, two independent shores differ with probability \(1/2\).  Hence
(6.6) becomes

\[
 \boxed{
 \Phi_{\rm prod}\ge{1\over4}\sum_UD_U-o(W).}
 \tag{7.3}
\]

On the other hand, every child obtained by choosing one shore per top
differs from the all-zero child in at most \(\sum_UD_U\) occurrence
replacements.  One replacement changes the aggregate number of holes by
at most one: deleting an occurrence can create at most one hole, and
inserting its replacement can remove at most one hole, with the two effects
having opposite signs.  Therefore

\[
 \left|H_{\rm agg}(\varepsilon)-H_{\rm agg}(0)\right|
 \le\sum_UD_U.
 \tag{7.4}
\]

Equations (7.3)--(7.4) give the promised dichotomy.

* If \(\sum_UD_U=o(W)\), the heat floor may be \(o(W)\), but the entire
  switch system has only \(o(W)\) hole-repair capacity relative to either
  shore.
* If the system has \(\Omega(W)\) occurrence capacity, its independent
  heat floor is \(\Omega(W)\), already too large.

For an adjacent transposition in a cyclic order, at most two old and two
new intervals change in each rank.  Therefore a two-shore adjacent-swap
ring component has

\[
 D_U=O(H).
 \tag{7.5}
\]

Across all tops,

\[
 \sum_UD_U=O(HN_H)=o(W).
 \tag{7.6}
\]

So adjacent-swap components have a harmless heat floor precisely because
they have negligible global correction capacity.  Serially adding enough
independent swap directions to obtain linear capacity returns, through
(7.3), a linear heat floor.

## 8. Exact implication boundary

Proved here:

1. a literal nested per-top tag profile whose aggregate rank and tag-census
   defect is \(o(W)\);
2. the exact full-catalogue one-block heat identity (0.7);
3. its floor-correct stationary value
   \((\sqrt\pi/2+o(1))W\sqrt m\);
4. the exact two-rate harmonic identity for nonidentical prescribed
   profiles;
5. the average-distance formula (6.2) for arbitrary restricted ring
   catalogues;
6. the necessary \(o(m)\)-per-top incidence-agreement threshold for an
   \(o(W)\) heat floor; and
7. the exact two-shore capacity/noise obstruction (7.3)--(7.4).

Not proved or refuted:

1. a globally correlated selection of one tagged ring per top with
   \(o(W)\) aggregate collisions;
2. an aligned multi-top component resolution whose choices have negative
   cross-block floor covariance; or
3. the promotion-ring approximate-SCD factorization itself.

The useful conclusion is nevertheless sharp for the proposed heat lane.
The integer floor baseline is negligible, while ordinary ring-resampling
noise is enormous.  Restricting to incidence-near components removes that
noise only by removing the amount of local freedom needed to repair a
linear defect.  Any positive continuation must therefore correlate many
tops before averaging; it cannot be a product of independent one-top ring
heats.
