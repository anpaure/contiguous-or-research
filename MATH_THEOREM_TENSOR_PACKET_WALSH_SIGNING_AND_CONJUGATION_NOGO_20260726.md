# Tensor packets: the exact Walsh signing gate and the independent-conjugation no-go

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, or web input is
used.

## 0. Outcome

Use the all-\(Q_2\) tensor associator packet on \(r\) eight-coordinate
blocks.  Each shore vector \(\varepsilon\in\{0,1\}^r\) partitions its

\[
                         S=24^r
\tag{0.1}
\]

middle owners into

\[
                         M=6^r
\tag{0.2}
\]

physical \(Q_{2r}\)-cells, each having

\[
                         K=4^r
\tag{0.3}
\]

vertices.  In every cell use a coordinate conjugate of the recursive
shadow-injective factor.  Exact packet-wide face separation is preserved
under these conjugations.

There are four conclusions.

1.  For fixed cell conjugations, simultaneous shore selection is exactly
    a Walsh--Gram minimization.  If \(Z_{P,q}^{\varepsilon,\pm}\) is the
    \(0/1\) target-incidence vector of packet \(P\), then

    \[
      Z_{P,q}^{\varepsilon,\pm}
       =\sum_{I\subseteq[r]}\chi_I(\varepsilon)
          \widehat Z_{P,q,I}^{\pm},
    \tag{0.4}
    \]

    and every cross-packet collision term is an inner product of two
    coefficients in (0.4).  Ordinary conditional expectation gives a
    deterministic common shore choice no worse than the constant Walsh
    term, simultaneously at all depths and on both sides.  It gives a
    coefficient-one result only if the nonconstant Walsh--Gram polynomial
    has minimum \(-\Theta(W)\).

2.  The bounded associator has genuine literal signed drift.  At local
    depth one the two shores have sixteen common shadows and eight
    old-only versus eight new-only shadows.  In the tensor packet, switching
    one shore bit changes at least

    \[
             {2Sq\over3r}
    \tag{0.5}
    \]

    literal depth-\(q\) targets when the block-pair-preserving recursive
    order is used.  Thus its half-drift has squared norm at least

    \[
                         {Sq\over6r}.
    \tag{0.6}
    \]

    With arbitrary coordinate conjugation the corresponding universally
    valid bounds are half as large.  This proves that the local Walsh
    modes are extensive.  It does **not** give their signs against loads
    from other packets.

3.  Independent uniform cell conjugations have an exact variance which
    is fatal to a product-law/conditional-expectation proof.  At depth
    \(q\le r\), put

    \[
                         p_{r,q}={2^q\over\binom{2r}q}.
    \tag{0.7}
    \]

    Conditional on any shore vector, one cell has variance

    \[
                         K(1-p_{r,q}),
    \tag{0.8}
    \]

    and one packet has variance \(S(1-p_{r,q})\).  Therefore, even if the
    shore vectors of different packets are arbitrarily correlated, but
    the cell conjugations remain conditionally independent and uniform,

    \[
      \operatorname {Var}\!\left(\sum_PZ_{P,q}^{\pm}
                              \right)
       \ge W(1-p_{r,q})-o(W).
    \tag{0.9}
    \]

    At \(q=a\sqrt m+o(\sqrt m)\), the expected balanced collision excess
    is consequently \(\Theta_a(W)\).  Independent conjugation supplies
    positive diagonal energy, not the required negative covariance.

4.  There is a stronger typical-instance no-go.  Fix one Gaussian depth.
    Choose the coordinate conjugation of every possible selected cell
    independently and uniformly.  With probability

    \[
                   1-\exp\{-\Omega_a(W/4^r)\},
    \tag{0.10}
    \]

    **every** one of the \(2^{rW/24^r}\) global shore signings leaves
    \(\Theta_a(W)\) literal targets uncovered.  The reason is the scale
    separation

    \[
       {rW\over24^r}=o\!\left({W\over4^r}\right).
    \tag{0.11}
    \]

    Hence no theorem of the form "take independent cell conjugates and
    then repair them by the \(2^r\) shore signs" can prove coefficient
    one.  Any successful use of coordinate conjugations must choose them
    in a globally correlated, near-design fashion.

This is a no-go for the proposed random-signing mechanism, not a
statewise impossibility theorem for all deterministic conjugation atlases.
The exact surviving gate is the negative Walsh--Gram condition in
Section 4.

## 1. The collision ledger after packet-wide injectivity

Let \(\mathscr P\) be an owner-disjoint family of packets.  Ignore an
\(o(W)\) owner leave; restoring it changes every estimate below by
\(o(W)\).  Thus

\[
                         |\mathscr P|S=W.
\tag{1.1}
\]

For a target rank and sign, write

\[
 \mathcal T_q^-={\binom{[2m]}{m-q}},\qquad
 \mathcal T_q^+={\binom{[2m]}{m+q}},\qquad
 N_q=|\mathcal T_q^-|=|\mathcal T_q^+|.
\tag{1.2}
\]

Complementation identifies the two target spaces, so it is enough to
write the lower formulas.  Packet-wide shadow injectivity gives

\[
 Z_{P,q}^{\omega}\in\{0,1\}^{\mathcal T_q},\qquad
 \|Z_{P,q}^{\omega}\|_1=S
\tag{1.3}
\]

for every legal state \(\omega\).  Put

\[
 \mu_q=\sum_PZ_{P,q},\qquad
 W=c_qN_q+\rho_q,\qquad
 \theta_q={\rho_q\over N_q}.
\tag{1.4}
\]

The balanced pair floor is

\[
 B_q=(N_q-\rho_q)\binom{c_q}2
             +\rho_q\binom{c_q+1}2.
\tag{1.5}
\]

Since a packet never collides with itself,

\[
 \sum_T\binom{\mu_q(T)}2
 =\sum_{P<P'}\langle Z_{P,q},Z_{P',q}\rangle.
\tag{1.6}
\]

Consequently the exact balanced collision excess is

\[
 \boxed{
 \Delta_q
 =\sum_{P<P'}\langle Z_{P,q},Z_{P',q}\rangle-B_q
 ={1\over2}\left(
    \left\|\mu_q-{W\over N_q}{\bf1}\right\|_2^2
       -N_q\theta_q(1-\theta_q)\right).}
\tag{1.7}
\]

It is nonnegative because the loads are integral.  A hole contributes at
least \(\binom{c_q+1}2\) to \(\Delta_q\).

## 2. Exact coordinate-orbit census in one cell

Fix one product cell \(C\cong Q_{2r}\).  A physical lower \(q\)-face is
specified by a \(q\)-set of active directions and one endpoint on every
inactive direction.  Hence the admissible face set has size

\[
                         F_{r,q}=\binom{2r}q2^{2r-q}.
\tag{2.1}
\]

The recursive factor has one directed start at every cube vertex.  Its
depth-\(q\) shadow map is injective, so its target image has size

\[
                         K=2^{2r}.
\tag{2.2}
\]

The signed coordinate group

\[
                         \Gamma_r=C_2^{2r}\rtimes S_{2r}
\tag{2.3}
\]

acts transitively on the \(q\)-faces.  Therefore, if \(g\) is uniform in
\(\Gamma_r\) and \(Z_{C,q}^g\) is the incidence vector of the conjugated
factor, then for every admissible face \(T\),

\[
 \Pr(T\in Z_{C,q}^g)
 ={K\over F_{r,q}}
 ={2^q\over\binom{2r}q}
 =p_{r,q}.
\tag{2.4}
\]

Thus

\[
 \mathbb EZ_{C,q}^g=p_{r,q}{\bf1}_{\mathcal F(C,q)}
\tag{2.5}
\]

and, using \(\|Z_{C,q}^g\|_2^2=K\),

\[
\begin{aligned}
 \mathbb E\|Z_{C,q}^g-\mathbb EZ_{C,q}^g\|_2^2
 &=K-F_{r,q}p_{r,q}^2\\
 &=K(1-p_{r,q}).
\end{aligned}
\tag{2.6}
\]

The same calculation holds for upper faces.  Conjugating the factor does
not affect injectivity inside the cell.  The local face-separation theorem
says that the full admissible face families of distinct product cells in
one packet are disjoint.  Hence independent conjugations in its \(M\)
cells give the exact conditional packet variance

\[
 \boxed{
 \mathbb E_g\|Z_{P,q}^g-\mathbb E_gZ_{P,q}^g\|_2^2
 =MK(1-p_{r,q})=S(1-p_{r,q}).}
\tag{2.7}
\]

For \(1\le q\le r\) and \(r\longrightarrow\infty\),

\[
                         \max_qp_{r,q}=o(1).
\tag{2.8}
\]

For example, the endpoint \(q=1\) gives \(1/r\), while at \(q=r\)
Stirling gives \(p_{r,r}=O(\sqrt r\,2^{-r})\).  The ratio
\(p_{r,q+1}/p_{r,q}=2(q+1)/(2r-q)\) shows that the maximum is at an
endpoint, proving (2.8).

## 3. The simultaneous conditional-expectation theorem

The following abstract form includes shores, cell conjugations, lower and
upper targets, and every required depth.

Let \(\Omega_P\) be any finite legal state set for packet \(P\), and let
\(\nu_P\) be any probability law on it.  Give the packet states the product
law \(\nu=\bigotimes_P\nu_P\).  For nonnegative weights \(w_q\), put

\[
 \Phi(\omega)=\sum_{q\le Q}\sum_{\pm}w_q\Delta_q^\pm(\omega).
\tag{3.1}
\]

### Theorem 3.1 (exact product-law derandomization)

There is a deterministic legal state \(\omega^*\) such that

\[
                         \Phi(\omega^*)\le\mathbb E_\nu\Phi.
\tag{3.2}
\]

Moreover, writing

\[
 \overline Z_{P,q}=\mathbb EZ_{P,q},\qquad
 \overline\mu_q=\sum_P\overline Z_{P,q},
\tag{3.3}
\]

one has the exact identity

\[
\boxed{
 2\mathbb E\Delta_q
 =\left\|\overline\mu_q-{W\over N_q}{\bf1}\right\|_2^2
  +\sum_P\mathbb E\|Z_{P,q}-\overline Z_{P,q}\|_2^2
  -N_q\theta_q(1-\theta_q).}
\tag{3.4}
\]

#### Proof

Expose the packet states successively.  At every node, the present
conditional expectation is a convex combination of its children, so one
child has no larger value.  Iteration proves (3.2).

For (3.4), expand the squared norm in (1.7).  Packet independence makes
all cross-packet centered inner products have mean zero. \(\square\)

Thus ordinary conditional expectation only derandomizes the supplied
product certificate.  It does not manufacture the missing negative
cross-packet term.

### Proposition 3.2 (product-bias optimization is tautological)

Let the legal choices be exposed through any finite collection of shore
or conjugation variables, and allow an arbitrary independent probability
distribution on the state set of each variable.  Then

\[
 \boxed{
 \min_{\text{product laws}}\mathbb E\Phi
 =\min_{\text{deterministic legal states}}\Phi.}
\tag{3.5}
\]

#### Proof

For fixed laws of all other variables, \(\mathbb E\Phi\) is affine in the
probability vector of the remaining variable.  Push that vector to an
extreme point without increasing the expectation, and repeat.  The final
product law is a point mass.  The reverse inequality is immediate because
point masses are product laws. \(\square\)

Thus optimizing independent biases and then invoking conditional
expectation is the original integral selection problem in fractional
notation.  A useful theorem must prove a geometric inequality such as
(4.6); freedom to choose the biases is not such an inequality.

## 4. Walsh--Gram normal form for the shore choices

Now fix every cell factor and conjugation, and retain only the shore vector
\(\sigma_P\in\{-1,+1\}^r\) of each packet.  Its exact Fourier expansion is

\[
 Z_{P,q}^{\sigma_P,\pm}
 =\sum_{I\subseteq[r]}\chi_I(\sigma_P)
                   \widehat Z_{P,q,I}^{\pm},
 \qquad
 \chi_I(\sigma)=\prod_{i\in I}\sigma_i.
\tag{4.1}
\]

Substitution in (1.6) gives

\[
\boxed{
 \sum_{P<P'}\langle Z_{P,q}^{\sigma_P},Z_{P',q}^{\sigma_{P'}}\rangle
 =\sum_{P<P'}\sum_{I,J\subseteq[r]}
   \chi_I(\sigma_P)\chi_J(\sigma_{P'})
   \langle\widehat Z_{P,q,I},\widehat Z_{P',q,J}\rangle.}
\tag{4.2}
\]

The same shore signs must be used at every depth and on both sides.
Define the weighted Gram coefficients

\[
 G_{P,I;P',J}
 =\sum_{q\le Q}\sum_{\pm}w_q
   \langle\widehat Z_{P,q,I}^{\pm},
          \widehat Z_{P',q,J}^{\pm}\rangle.
\tag{4.3}
\]

Then the nonconstant part of the simultaneous collision potential is the
single polynomial

\[
 \mathcal G(\sigma)
 =\sum_{P<P'}\ \sum_{(I,J)\ne(\varnothing,\varnothing)}
    G_{P,I;P',J}\chi_I(\sigma_P)\chi_J(\sigma_{P'}).
\tag{4.4}
\]

Uniform independent shore signs make its expectation zero.  Conditional
expectation proves only

\[
                         \min_\sigma\mathcal G(\sigma)\le0.
\tag{4.5}
\]

The desired covariance cancellation is exactly

\[
                         \boxed{\min_\sigma\mathcal G(\sigma)
                                  \le-cW+o(W)}
\tag{4.6}
\]

with the coefficient \(c\) dictated by Section 6.  Norms of the individual
Walsh coefficients do not imply (4.6): different packets, targets, signs,
and depths enter only through the signed Gram sums (4.3).

There is also an exact branch-gain form.  Suppose a conditional-expectation
procedure is about to expose one packet bit, and let

\[
 d={1\over2}\left(
       \mathbb E[Z_P\mid\sigma_i=+1,\mathcal F]
      -\mathbb E[Z_P\mid\sigma_i=-1,\mathcal F]\right),
\tag{4.7}
\]

where all depths and signs are placed in their weighted direct-sum Hilbert
space.  Let \(L\) be the conditional mean load of all other packets.  The
two child collision expectations differ by

\[
                         2\langle d,L\rangle.
\tag{4.8}
\]

The greedy decrease at this exposure is therefore

\[
                         |\langle d,L\rangle|.
\tag{4.9}
\]

Since \(d\) has total coordinate sum zero, the constant part of \(L\) is
invisible.  A \(W\)-scale theorem requires a common exposure history with

\[
                         \sum_{\text{exposures}}
                         |\langle d,L-\overline L{\bf1}\rangle|
                         =\Theta(W).
\tag{4.10}
\]

Equation (4.10), not the size of \(\|d\|_2\), is the exact missing drift
alignment condition.

## 5. The exact local drift and why it is not covariance

### Proposition 5.1 (literal shore influence)

#### Proof

In one associator block, the lower one-step image on the old shore is

\[
 C^-\ \dot\cup\ O_0^-,
\tag{5.1}
\]

where

\[
\begin{aligned}
 C^-&=\{\{x\}\cup Y:x\in\{a,b,c,d\},\ Y\in\mathcal Y\},\\
 O_0^-&=\{ab\cup\{z\},cd\cup\{z\}:z\in\{u,v,w,x\}\}.
\end{aligned}
\tag{5.2}
\]

The new shore image is

\[
 C^-\ \dot\cup\ O_1^-,\qquad
 O_1^-=\{ac\cup\{z\},bd\cup\{z\}:z\in\{u,v,w,x\}\}.
\tag{5.3}
\]

Thus \(|C^-|=16\), \(|O_0^-|=|O_1^-|=8\), and the three sets are
pairwise disjoint.  The upper lists have the same \(16+8\) decomposition:
the common part uses a special triple and a reservoir orientation, while
the old-only and new-only parts use respectively \(ab,cd\) and \(ac,bd\)
together with a reservoir triple.

Projecting to full-pair type in the original frame, and adjoining a
spectator background with \(F\) full pairs, the literal half-drifts are

\[
 D^{\mathrm{type},-}=4(e_F-e_{F+1}),\qquad
 D^{\mathrm{type},+}=4(e_{F+1}-e_{F+2}).
\tag{5.3a}
\]

Thus the familiar signed type drift is the quotient of the disjoint
eight-against-eight literal move, rather than merely an enumerator
identity.

Fix the other \(r-1\) shores and switch block \(i\).  In every product
cell, a depth-\(q\) window of the block-pair-preserving recursive order
touches block \(i\) at exactly a \(q/r\) fraction of its starts.  Exactly
two of the six old local cells are reservoir-active.  Hence at least

\[
                         {S q\over3r}
\tag{5.4}
\]

old targets have local restriction in \(O_0^-\), and none can occur on
the new shore.  The new shore has the same number in \(O_1^-\), absent on
the old shore.  Local rank distinguishes a touched target from an
untouched one.  Therefore

\[
 |\operatorname {Im}Z^{\sigma_i=+1}_{P,q}
       \mathbin\triangle
   \operatorname {Im}Z^{\sigma_i=-1}_{P,q}|
 \ge {2Sq\over3r}.
\tag{5.5}
\]

For the half-difference \(D_iZ=(Z^+-Z^-)/2\),

\[
                         \|D_iZ\|_2^2\ge {Sq\over6r}.
\tag{5.6}
\]

Equivalently, under the uniform shore measure,

\[
 \mathbb E_\sigma\|D_iZ\|_2^2
 =\sum_{I\ni i}\|\widehat Z_I\|_2^2.
\tag{5.7}
\]

In the synchronized block-pair-preserving construction, a target occurrence
depends only on the shore bits of its at most \(q\) touched blocks.  Hence
the Walsh degree is at most \(q\), and summing (5.6)--(5.7) over \(i\)
gives the literal shore-variance bound

\[
 \sum_{I\ne\varnothing}\|\widehat Z_I\|_2^2
 \ge {1\over q}\sum_i\mathbb E\|D_iZ\|_2^2
 \ge {S\over6}.
\tag{5.8}
\]

An arbitrary coordinate conjugation can put both directions from one
physical local block in a window.  Counting direction incidences still
shows that block \(i\) is touched at at least a \(q/(2r)\) fraction of
starts.  When both directions are touched, the old reservoir cells leave
\(ab\) or \(cd\), whereas the new reservoir cells leave \(ac\) or \(bd\);
these lists are again disjoint.  Thus (5.5)--(5.6) remain valid with right
sides divided by two.

This is the promised exact use of the local signed drift.  It proves that
the shore cube is not a collection of negligible moves.  But (4.8) shows
the obstruction: a large drift orthogonal to the other-packet residual
has zero conditional-expectation gain.  Coordinate conjugation preserves
the drift norm while changing precisely these unproved inner products.
\(\square\)

## 6. Independent conjugations cannot supply the cancellation

Allow an arbitrary joint law for all shore vectors.  Conditional on the
shores, choose every selected cell conjugation independently and uniformly.
Write \(\mathcal S\) for the shore sigma-field.  By (2.7) and conditional
independence across packets,

\[
 \mathbb E\left[
  \left\|\mu_q-\mathbb E(\mu_q\mid\mathcal S)\right\|_2^2
  \ \middle|\ \mathcal S\right]
 =W(1-p_{r,q})+o(W).
\tag{6.1}
\]

The Hilbert-space variance decomposition gives

\[
\begin{aligned}
 \mathbb E\|\mu_q-\mathbb E\mu_q\|_2^2
 ={}&\mathbb E\|\mu_q-\mathbb E(\mu_q\mid\mathcal S)\|_2^2\\
 &+\mathbb E\|\mathbb E(\mu_q\mid\mathcal S)
                         -\mathbb E\mu_q\|_2^2\\
 \ge{}&W(1-p_{r,q})-o(W).
\end{aligned}
\tag{6.2}
\]

Substitution into the general dependent identity yields

\[
\boxed{
 2\mathbb E\Delta_q
 \ge W(1-p_{r,q})-N_q\theta_q(1-\theta_q)-o(W).}
\tag{6.3}
\]

Since \(N_q\le W\) and \(\theta_q(1-\theta_q)\le1/4\),

\[
                         \mathbb E\Delta_q
 \ge\left({3\over8}-{p_{r,q}\over2}-o(1)\right)W.
\tag{6.4}
\]

At Gaussian depth \(q=a\sqrt m+o(\sqrt m)\), a sharper display uses
\(W/N_q\to e^{a^2}\):

\[
 2\mathbb E\Delta_q
 \ge\left(1-p_{r,q}
       -e^{-a^2}\theta_q(1-\theta_q)-o(1)\right)W.
\tag{6.5}
\]

More generally, for an arbitrary dependent packet law, success requires

\[
\boxed{
 2\sum_{P<P'}C_{P,P',q}
 =-\left\|\mathbb E\mu_q-{W\over N_q}{\bf1}\right\|_2^2
   -\sum_PV_{P,q}+N_q\theta_q(1-\theta_q)+o(W).}
\tag{6.6}
\]

For the conjugation marginals of Section 2, \(\sum_PV_{P,q}\ge
W(1-p_{r,q})-o(W)\).  Thus (6.6) is at most

\[
 -W(1-p_{r,q})+N_q\theta_q(1-\theta_q)+o(W),
\tag{6.7}
\]

and becomes \(-W+N_q\theta_q(1-\theta_q)+o(W)\) when the mean is balanced
and the total packet variance is \(W-o(W)\).  Independent cell noise
contributes no term to the left side of (6.6).  It therefore cannot be the
source of the required negative covariance.

## 7. Typical independent atlases defeat every shore signing

The preceding expectation identity already rules out a direct product-law
proof.  The following strengthens it to a simultaneous statement over all
shore signings.

Fix

\[
                         q=a\sqrt m+o(\sqrt m)\le r,
\tag{7.1}
\]

where \(a>0\) is fixed, and suppose \(r=o(m)\).  Preassign independently a
uniform coordinate conjugation to every product cell on every shore corner
of every packet.  A global shore signing selects \(M\) of these cells in
each packet.

### Theorem 7.1 (typical-atlas shore-signing no-go)

There is a constant \(c_a>0\) such that, with probability
\(1-\exp\{-\Omega_a(W/4^r)\}\), every global shore signing has at least
\(c_aW\) uncovered depth-\(q\) targets.

#### Proof

Fix one shore signing.  If \(I_{C,T}\) is the indicator that selected cell
\(C\) hits target \(T\), then the \(I_{C,T}\)'s are independent in \(C\),
and each nonzero marginal equals \(p_{r,q}\).  Put

\[
                         \lambda_T=\sum_C\mathbb EI_{C,T}.
\tag{7.2}
\]

Since every cell emits \(K\) targets,

\[
                         \sum_T\lambda_T=W+o(W).
\tag{7.3}
\]

For \(0\le x\le p<1\),

\[
                         1-x\ge\exp\{-x/(1-p)\}.
\tag{7.4}
\]

Therefore the expected number \(H_q\) of holes obeys

\[
\begin{aligned}
 \mathbb EH_q
 &=\sum_T\prod_C(1-\mathbb EI_{C,T})\\
 &\ge\sum_T\exp\{-\lambda_T/(1-p_{r,q})\}\\
 &\ge N_q\exp\left\{-{W/N_q+o(1)\over1-p_{r,q}}\right\}.
\end{aligned}
\tag{7.5}
\]

The last step is Jensen's inequality.  Since \(W/N_q\to e^{a^2}\) and
\(p_{r,q}=o(1)\),

\[
 \mathbb EH_q
 \ge\left(e^{-a^2-e^{a^2}}+o(1)\right)W.
\tag{7.6}
\]

Changing the conjugation of one selected cell can change the hole count on
at most the symmetric difference of two \(K\)-sets, hence by at most
\(2K\).  There are \(W/K+o(W/K)\) selected cells.  McDiarmid's inequality
therefore gives, for a constant \(c_a>0\),

\[
 \Pr\{H_q\le c_aW\}
 \le\exp\{-c_a^2W/(8K)+o(W/K)\}.
\tag{7.7}
\]

There are

\[
                         2^{r|\mathscr P|}
 =\exp\left\{{rW\log2\over24^r}+o(W/24^r)\right\}
\tag{7.8}
\]

global shore signings.  Since

\[
 {rW/24^r\over W/4^r}={r\over6^r}\longrightarrow0,
\tag{7.9}
\]

the union bound applied to (7.7) proves

\[
 \Pr\{\text{some shore signing has }H_q\le c_aW\}
 \le\exp\{-\Omega_a(W/4^r)\}.
\tag{7.10}
\]

This proves (0.10).  A simultaneous coefficient-one construction must
succeed at the fixed depth (7.1), so failure there already rules it out.
The same union bound may include any \(\exp(o(W/4^r))\) collection of
depths. \(\square\)

## 8. Exact boundary

Proved here:

* the exact simultaneous Walsh--Gram normal form for all shore choices;
* the exact product-law conditional-expectation theorem;
* an explicit literal lower bound for every local shore drift;
* the exact cell-conjugation marginal and variance;
* the order-\(W\) residual variance under independent cell conjugation,
  even with arbitrarily correlated shore vectors; and
* a typical-atlas theorem showing that every shore signing has
  \(\Theta(W)\) holes at a fixed Gaussian depth.

Not proved, and not ruled out:

* a specially designed deterministic conjugation atlas whose Walsh--Gram
  polynomial satisfies (4.6);
* a joint, globally correlated choice of shore vectors and cell
  conjugations forming a near-design; or
* a different outer owner-packet atlas which changes the cross-packet
  incidence geometry.

The exact remaining coefficient-one statement is therefore not a marginal
or local-drift estimate.  It is the integral alignment assertion (4.6), or
equivalently the branch-correlation assertion (4.10).  Independent
per-cell coordinate conjugation makes those correlations typically too
diffuse; it cannot be repaired by the available shore signs.
