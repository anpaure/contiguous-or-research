# Audit: CPCR versus exact missing targets and cross-depth coupling

Date: 2026-07-26

This note is conditional on the asserted diverse-order packet factor.  It
audits only the final load ledger and does not repair the separately recorded
literal-trace decoder issue.

## 1. Exact missing-target ledger

Fix one signed depth (c=(\epsilon,q)).  Write

\[
L(T)=\#\{P:T\in I_{P,c}\},\qquad
G=\sum_TL(T),\qquad N=N_q,
\]

and put

\[
M=\#\{T:L(T)=0\},\qquad
\mathcal R=\sum_T(L(T)-1)_+.
\]

Since the positive coordinates contribute one unit of support and then
\(\mathcal R\) repeat units,

\[
G=(N-M)+\mathcal R.
\]

Hence the advertised identity is exact:

\[
\boxed{M=N-G+\mathcal R.}
\tag{1.1}
\]

Equivalently,

\[
\boxed{
M=(N-G)_+ + \bigl(\mathcal R-(G-N)_+\bigr),
}
\tag{1.2}
\]

and the second term is nonnegative.  In the retained construction the owner
leave is exponentially small, so (G>N_q) for every protected (q\ge1) and
all sufficiently large (m).  Therefore

\[
M=\mathcal R-(G-N_q).
\tag{1.3}
\]

After summing over the (2H) signed depths, the exact missing-target theorem
is thus equivalent to cross-packet repeats being within (o(W)) of their
forced support minimum.  No covariance or balancing hypothesis is needed for
this equivalence.

## 2. CPCR is algebraically strictly stronger

Write (G=cN+r), (0\le r<N), and

\[
\Phi_c(L)=\sum_T(L(T)-c)(L(T)-c-1).
\]

Then

\[
\Phi_c(L)=2\left[
  \sum_T\binom{L(T)}2
  -N\binom c2-rc
\right].
\tag{2.1}
\]

Thus CPCR asks that every signed-depth load be close to a floor/ceiling
quota vector.  Missing-target control asks only that its support be almost
maximal.  The former implies the latter, but the converse does not follow.

The distinction is already exact when (c=1):

\[
\boxed{
\Phi_c(L)
=2M+2\sum_{T:L(T)\ge3}\binom{L(T)-1}{2}.
}
\tag{2.2}
\]

The second term is a triple-and-higher multiplicity penalty invisible to
missing-target control.

For a concrete asymptotic separation, choose
(q=\lfloor a\sqrt m\rfloor) with (0<a<\sqrt{\log2}).  Then
(G/N_q\to e^{a^2}\in(1,2)), so (c=1), and
(D:=G-N_q=\Theta(W)).  Up to one parity adjustment, take load (3) on
(D/2) targets and load (1) on every other target.  Then

\[
M=0,qquad \mathcal R=D,qquad \Phi_c(L)=D=\Theta(W).
\tag{2.3}
\]

This example is compatible with the abstract packet-injectivity data: a
simple bipartite incidence matrix with packet-row sum (2^R) and these
column degrees exists by the Gale--Ryser inequalities.  It need not be a
literal compiler-atlas state, but it proves that packet injectivity and the
mass identity do not make CPCR equivalent to missing targets.  Equivalence
on the reachable compiler orbit would require a new theorem suppressing
high multiplicities; none of the cited packet results proves one.

Therefore the correct status is:

\[
\boxed{
\text{CPCR is a sufficient strengthening, not the exact remaining
missing-target theorem.}
}
\tag{2.4}
\]

## 3. Exactly how much one compiler choice couples

One legal compiler option (\omega_P) fixes the single vector

\[
v_{P,\omega_P}
=\bigl(\mathbf1_{I_{P,q}^{-}},
       \mathbf1_{I_{P,q}^{+}}\bigr)_{q=1}^{H}.
\tag{3.1}
\]

It therefore couples all (H) depths and both signs: exactly (2H) image
coordinates in the formal CPCR model.  A slab trade likewise changes one
all-depth (2H)-coordinate derivative.  Options may not be chosen
separately for different (q)'s.

This coupling currently gives one proved benefit only: conditional
expectation rounds one common packet distribution to one common integral
choice without an additional integrality or union-bound loss.  For the
additive target cost (J=\sum_cJ_c), however,

\[
\mathbb E J=\sum_c\mathbb E J_c.
\tag{3.2}
\]

Thus the rounding theorem preserves an already-small aggregate expectation;
it does not create a cross-depth saving.  Separate depthwise distributions
(x^{(c)}) cannot be substituted for the one common distribution (x).
Indeed,

\[
\min_{\omega}\sum_cJ_c(\omega)
\ge \sum_c\min_{\omega}J_c(\omega),
\tag{3.3}
\]

so common-choice coupling is a restriction, not automatically a source of
lower cost.

The slab-circulation identity cancels the direction-support projections at
all depths because their (q)-dependence is scalar.  The cited audit also
shows that the remaining literal residues lie in the direct-sum hard kernel;
it proves no cancellation of holes, repeats, or CPCR energy there.  Likewise,
the conjugate-Latin Fourier formula is a sum of nonnegative per-depth
energies and contains no cross-depth cancellation term.

Consequently there is presently **no proved quantitative saving** from
cross-depth correlation over an additive treatment of the (2H) signed
depths.  A uniform per-colour error (\eta_mW) still requires

\[
H\eta_m\longrightarrow0
\]

to yield (o(W)) aggregate error.  The common choice is genuinely
simultaneous, but the hoped-for correlation gain remains an unproved part of
the final construction.

