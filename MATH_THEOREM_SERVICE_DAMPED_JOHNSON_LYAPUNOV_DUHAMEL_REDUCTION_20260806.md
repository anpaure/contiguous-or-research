# Service-damped Johnson Lyapunov and the exact Duhamel reduction

**Date:** 2026-08-06  
**Method:** exact discrete Lyapunov equation, resolvent identity, and
chronological first/second-order expansion; no computation or search  
**Status:** proof-safe analytic reduction.  Incorporating the already
present two-root future service removes the affine and degree-two slow-mode
loss from the pristine resolvent.  The remaining host-specific row is an
exact coefficient comparison between the chronological Duhamel terms and
the authenticated `ROc`/`FE3` selected-relation ledgers.  This note does
not assert that comparison.

## 1. The correct discounted pristine resolvent

Work on one mean-zero central Johnson layer.  Let

\[
 L=\sum_{s\ge1}\vartheta_s\Pi_s,
 \qquad
 B=\sum_{s\ge1}\widehat\chi_s\Pi_s,
\tag{1.1}
\]

where `L` is the normalized one-exchange Laplacian and `B` is the pristine
FIFO covariance.  Let `X` be the current total rate, put

\[
 P=I-{L\over X},
 \qquad a=\rho^2,
 \qquad \lambda=X(1-a),
\tag{1.2}
\]

and assume the stopped rate row

\[
 0<c_0\le\lambda\le C_0.
\tag{1.3}
\]

Define the **service-damped discrete Gramian** `R_a` by

\[
 \boxed{
 R_a={B\over X}+aP^*R_aP.}
\tag{1.4}
\]

Since `sqrt(a)||P||<1`, the solution is unique, positive semidefinite, and

\[
 R_a=\sum_{n\ge0}a^n(P^*)^n{B\over X}P^n.
\tag{1.5}
\]

On sector `E_s`, its exact multiplier is

\[
 \boxed{
 r_{a,s}={\widehat\chi_s/X
       \over1-a(1-\vartheta_s/X)^2}
 ={\widehat\chi_s
       \over\lambda+2a\vartheta_s-a\vartheta_s^2/X}.}
\tag{1.6}
\]

The denominator in (1.6) is comparable to `1+vartheta_s`, uniformly on
the stopped interval.  The authenticated bound

\[
 0\le\widehat\chi_s\le C\min\{d,k/s\}
\tag{JT}
\]

therefore gives

\[
 \boxed{0\le r_{a,s}\le Cd.}
\tag{1.7}
\]

This is the first key difference from the undamped Green operator
`L^dagger B`, whose low-sector multiplier is `widehat chi_s/vartheta_s`.

### Proposition 1.1 (trace and Johnson-edge resistance)

Assume the already proved pristine trace row

\[
 {1\over N}\operatorname {tr}(L^\dagger B)=O(1).
\tag{1.8}
\]

Then

\[
 {1\over N}\operatorname {tr}R_a=O(1).
\tag{1.9}
\]

Moreover, for every Johnson edge `b_xy=e_x-e_y`,

\[
 \boxed{
 \langle b_{xy},R_ab_{xy}\rangle
 ={2\over N}\operatorname {tr}(R_aL)=O(1).}
\tag{1.10}
\]

#### Proof

Since every nonconstant Johnson eigenvalue of `L` is bounded above by an
absolute constant, (1.8) implies

\[
 {1\over N}\operatorname {tr}B
 ={1\over N}\sum_sm_s\widehat\chi_s=O(1).
\]

Equation (1.6) and (1.3) give `R_a<=C B` spectrally, proving (1.9).
Transitivity on directed Johnson edges gives the equality in (1.10) by
averaging.  Finally

\[
 \operatorname {tr}(R_aL)
 =\sum_sm_s{\widehat\chi_s\vartheta_s
      \over\lambda+2a\vartheta_s-a\vartheta_s^2/X}
 \le C\operatorname {tr}B,
\]

which proves the bound.  \(\square\)

Thus a literal adjacent Johnson innovation has constant `R_a` resistance,
despite the `Theta(d)` operator norm in (1.7).

### Proposition 1.2 (arbitrary deleted-edge contraction)

The same spectral calculation gives

\[
 \boxed{L^{1/2}R_aL^{1/2}=L R_a\le C I.}
\tag{1.11}
\]

Consequently, for every positive semidefinite `0<=A<=L`,

\[
 \boxed{
 A R_a A\le C A\le C L.}
\tag{1.12}
\]

Furthermore,

\[
 \boxed{
 |\langle f,A R_aP f\rangle|
 \le C\langle f,Lf\rangle^{1/2}
        \langle f,R_af\rangle^{1/2}.}
\tag{1.13}
\]

#### Proof

On `E_s`, the eigenvalue in (1.11) is

\[
 \vartheta_sr_{a,s}
 ={\vartheta_s\widehat\chi_s
   \over\lambda+2a\vartheta_s-a\vartheta_s^2/X}.
\]

For central Johnson layers,
`vartheta_s<=Cs/k` for `s<=k/2`.  If `s<=k/d`, use
`widehat chi_s<=Cd`; otherwise use `widehat chi_s<=Ck/s`.
In either range `vartheta_s widehat chi_s<=C`.  This proves (1.11).

By the standard order factorization, `A<=L` gives

\[
 A=L^{1/2}C_0L^{1/2}
\]

on the support of `L`, for a positive contraction `0<=C_0<=I`.  Hence

\[
 A R_aA
 =L^{1/2}C_0(L^{1/2}R_aL^{1/2})C_0L^{1/2}
 \le C L^{1/2}C_0^2L^{1/2}\le CA,
\]

which proves (1.12).  Finally,

\[
\begin{aligned}
 |\langle f,A R_aP f\rangle|^2
 &=|\langle C_0^{1/2}L^{1/2}f,
       C_0^{1/2}L^{1/2}R_aPf\rangle|^2\\
 &\le\langle f,Lf\rangle
       \langle R_aPf,L R_aPf\rangle\\
 &\le C\langle f,Lf\rangle\langle f,R_af\rangle,
\end{aligned}
\]

because `P,L,R_a` commute and
`r_{a,s}^2(1-vartheta_s/X)^2vartheta_s<=Cr_{a,s}`.
This proves (1.13).  \(\square\)

## 2. Exact current-operator Duhamel identity

Let `\widetilde P` be any self-adjoint contraction and
`\widetilde B>=0`.  Define its current damped Gramian by

\[
 \widetilde R={\widetilde B\over X}
       +a\widetilde P^*\widetilde R\widetilde P.
\tag{2.1}
\]

Put

\[
 \mathscr S_{a,\widetilde P}(H)
   =H-a\widetilde P^*H\widetilde P,
 \qquad
 \Delta P=\widetilde P-P,
 \qquad
 \Delta B=\widetilde B-B.
\tag{2.2}
\]

The inverse is positive on positive semidefinite inputs and has the exact
future-lifetime expansion

\[
 \mathscr S_{a,\widetilde P}^{-1}(H)
 =\sum_{n\ge0}a^n(\widetilde P^*)^nH\widetilde P^n.
\tag{2.3}
\]

### Theorem 2.1 (discrete Duhamel formula)

One has exactly

\[
 \boxed{
 \begin{aligned}
 \widetilde R-R
 =\mathscr S_{a,\widetilde P}^{-1}\Bigg[{}
 &{\Delta B\over X}\\
 &+a\bigl(
      \Delta P^*RP+P^*R\Delta P
       +\Delta P^*R\Delta P\bigr)
 \Bigg].
 \end{aligned}}
\tag{2.4}
\]

#### Proof

Subtract (1.4) from (2.1), move
`a\widetilde P^*(\widetilde R-R)\widetilde P` to the left, and expand

\[
 \widetilde P^*R\widetilde P-P^*RP
 =\Delta P^*RP+P^*R\Delta P+\Delta P^*R\Delta P.
\]

Apply (2.3).  \(\square\)

The three rows in (2.4) have different meanings.

* `Delta B/X` is the signed covariance-row loss.
* The two linear `Delta P` terms are the signed first-kill switch flux.
* `Delta P^*R Delta P` is the nonnegative two-change bracket.

They must not be bounded separately before the chronological coefficient
is inserted.  The regular `K_3` counterexample shows that the first line
does not dominate the second line pointwise.

### Corollary 2.2 (monotone generator deletion)

If

\[
 \widetilde L=L-A,
 \qquad A=\sum_e w_eb_eb_e^*\ge0,
 \qquad
 \widetilde P=I-{\widetilde L\over X}=P+{A\over X},
\tag{2.5}
\]

then the Duhamel source is

\[
 \boxed{
 {\Delta B\over X}
 +{a\over X}(ARP+P^*RA)
 +{a\over X^2}ARA.}
\tag{2.6}
\]

The inverse (2.3) has total scalar lifetime at most

\[
 \sum_{n\ge0}a^n={1\over1-a}={X\over\lambda}.
\tag{2.7}
\]

Consequently the chronological inverse cancels the explicit `1/X` in the
linear first-kill row, while the quadratic row retains one `1/X`.  This is
the exact first-entry/first-two-entry scale required by `ROc` and `FE3`.
No occupation-time logarithm occurs.

For one frozen deleted-edge operator, (1.12)--(1.13) also give the exact
dimension-free source bound

\[
 \boxed{
 \begin{aligned}
 \Bigl[ {a\over X}\langle f,(A R_aP+P^*R_aA)f\rangle
       +{a\over X^2}\langle f,A R_aA f\rangle\Bigr]_+
 \le{}&{C\over X}
   \sqrt{\langle f,Lf\rangle\langle f,R_af\rangle}\\
 &+{C\over X^2}\langle f,Lf\rangle.
 \end{aligned}}
\tag{2.8}
\]

This removes every spectral factor `d`.  It does not by itself match the
available root-Lyapunov coefficient: after multiplication by `beta`,
Young absorption against `beta<R_a>` and an `eta_d||f||^2` root energy
would require `beta=O(eta_d)`, whereas the present caps give only
`beta=O(d eta_d)`.  The missing factor is exactly the expected `1/d`
boundary aperture.  Thus `(D1)` has now been reduced to a coefficient
gain, not an operator or sector estimate.

## 3. Exact predictable compensator and bracket identity

For a frozen current pair `(\widetilde P,\widetilde B)`, let an adapted
vector make one linear step

\[
 z^+=\sqrt a\,\widetilde Pz+\xi,
 \qquad \mathbb E_i\xi=0.
\tag{3.1}
\]

Then (2.1) gives the exact identity

\[
 \boxed{
 \mathbb E_i\langle z^+,\widetilde Rz^+\rangle
 -\langle z,\widetilde Rz\rangle
 =-{1\over X}\langle z,\widetilde Bz\rangle
   +\mathbb E_i\langle\xi,\widetilde R\xi\rangle.}
\tag{3.2}
\]

If the mean innovation is `m_i` rather than zero, add exactly

\[
 2\sqrt a\,\langle\widetilde Pz,\widetilde Rm_i\rangle
 +\langle m_i,\widetilde Rm_i\rangle
\tag{3.3}

and use the centered innovation in the last term of (3.2).  If the
coefficient, `P`, `B`, or `R` changes after the transition, add its literal
predictable increment; (2.4) is the exact increment for the operator
part.

Equation (3.2) is the desired coefficient-faithful architecture:

* the covariance payment has exactly coefficient `1/X`;
* the mean is a signed one-root hazard row;
* the carré-du-champ is evaluated in the same future-lifetime Gramian;
* current-versus-pristine perturbation is the signed Duhamel source
  (2.4), not an absolute operator norm.

For a time-inhomogeneous process, iteration of (3.2) uses chronological
products of the actual predictable kernels.  Equivalently, the backward
Gramian satisfies the state-space Bellman equation

\[
 \mathcal R_i(s)={\mathcal B_i(s)\over X_i}
 +\mathbb E_s\!left[
      T_i(S_{i+1})^*\mathcal R_{i+1}(S_{i+1})
      T_i(S_{i+1})ight],
\tag{3.4}

with `T_i` including the square root of the exact two-root survival
factor.  Formula (3.4), not a frozen power series, is the fully adapted
version; it is exactly the selected-relation Bellman value.

## 4. The coefficient-faithful ledger still required

The Duhamel identity reduces the host-specific proof to the following two
rows.

### `(D1)` Signed first-entry source

After the covariance loss and the two linear switch terms in (2.6) are
grouped at their unique earliest blocker, their chronological future
coefficient is dominated by the rooted-overlap selected-relation
coefficient, and their positive total is `O(A)`.  In the equivalent energy
form supplied by (2.8), the chronological boundary measure must recover
one factor `1/d` relative to the pristine `L` energy.  Since
`beta=O(d eta_d)`, that single factor is exactly sufficient for joint
Young absorption with the root energy.

### `(D2)` Two-entry bracket

After expanding `ARA` and the innovation square in (3.2), first coalesce
private-switch occurrences by the physical blocker resource which certifies
their boundary membership.  Terms with two distinct blocker resources,
with the exact future coefficient from (2.3)/(3.4), must inject with
constant multiplicity into `FE3`.  Diagonal terms and off-diagonal terms
inside one common blocker-resource star belong to the rooted one-entry
square (`ROc`/root carré).  They are **not** automatically `FE3` terms:
two different switch edges can have the same physical first hit.

These are coefficient statements, not new operator inequalities.  The
earliest-blocker partition proves uniqueness of the first blocker, and
(1.10) proves constant resistance of one literal Johnson switch.  What is
not yet proved is that the actual cylinder/future-fugacity coefficient in
the FIFO host is pointwise dominated by the chronological coefficient in
(3.4), simultaneously for the covariance and generator pieces.

Under `PCAP`, the external coefficient satisfies

\[
 \beta_T\le {C\varepsilon_P\over d^2}.
\tag{4.1}
\]

Therefore the worst pristine low-sector multiplier obeys

\[
 \boxed{
 \beta_T\|R_a\|_{2\to2}\le {C\varepsilon_P\over d}.}
\tag{4.2}
\]

This makes every already coefficient-faithful root-carré error small.  It
does not prove `(D1)`: a signed first-kill flux can be positive while its
killed covariance row is zero.  Nor does it identify a marked/cylinder
future coefficient.  Those are the only reasons the note stops short of a
`GDIR` theorem.

## 5. Audit against the known slow modes

For central layers, `vartheta_1=Theta(d^{-2})` and
`widehat chi_1=Theta(d)`.  The undamped resolvent has multiplier

\[
 {\widehat\chi_1\over\vartheta_1}=\Theta(d^3),
\]

which is the affine coordinate-star obstruction.  The damped multiplier is

\[
 r_{a,1}={\widehat\chi_1
    \over\lambda+2a\vartheta_1+o(1)}=\Theta(d).
\tag{5.1}
\]

The same calculation holds on `E_2`: complementation may cancel `E_1`,
but `widehat chi_2=Theta(d)` and `vartheta_2=Theta(d^{-2})`, so the
undamped multiplier is again `Theta(d^3)` while (5.1) remains `Theta(d)`.
Multiplication by (4.1) makes both at most `O(\varepsilon_P/d)`.  Thus neither
known slow mode refutes the service-damped candidate.

The finite regular stopped-kernel counterexample is also respected.
Damping makes a zero mode finite, with cost divided by `lambda`, but an
adapted covariance projector of eigenvalue `Theta(N)` still has damped
cost `Theta(N)`.  Hence service damping does not let equivariance or trace
replace `(D1)--(D2)`.

## 6. Proof boundary

The new unconditional facts are:

1. the exact discrete service-damped spectrum (1.6);
2. constant trace and literal Johnson-edge resistance;
3. the signed Duhamel decomposition (2.4)/(2.6);
4. the exact predictable payment/bracket identity (3.2); and
5. removal of both the affine `E_1` and even `E_2` slow-sector losses under
   `PCAP`.

The remaining analytic statement is narrower than old `JRES--JSW`:

\[
 \boxed{
 \text{prove the actual earliest-blocker future coefficient realizes
 `(D1)` and `(D2)` in every required marked cylinder.}}
\]

Until that coefficient audit is complete, the note does not prove
`GDIR`, the bottom cleanup theorem, or `nu(k)=B(k)+O(1)`.
