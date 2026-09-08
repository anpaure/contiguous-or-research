# Audit: multistep component heat flow

Date: 2026-07-24

## Verdict

The proposed floor-subtracted recurrence is correct.  It has a useful exact
interpretation: under later random coordinate transpositions, the amount
`(2/n) beta_q` is precisely the per-step noise needed to replenish the
unavoidable integer floor.  The residual `gamma_q` is the excess component
noise.

A discounted positive-`gamma` criterion along a heat-flow trajectory is a
valid sufficient condition for MWB.  Taking `T=n^2` steps kills even the
largest possible initial collision energy.

There is, however, no spectral argument that bounds `gamma` automatically.
If an interaction overlay is connected, the heat step merely chooses `F` or
`tau F`; the energy is unchanged and its covariance exactly cancels the
spectral smoothing of its mean.  The same cancellation can persist through
arbitrarily many coordinate steps.  Thus multistep telescoping reorganizes
the missing component-variance theorem but does not remove it.

## 1. Floor-subtracted energy

Put

\[
 n=2m+1,\qquad N_q=\binom n{m-q},\qquad
 \lambda_q=\frac W{N_q}=c_q+\alpha_q,
\]

and

\[
 \beta_q=N_q\alpha_q(1-\alpha_q).
\]

For an exact factor `F`, let

\[
 f_q(F)=\mu_q(F)-\lambda_q\mathbf 1,
 \qquad Q_q(F)=\|f_q(F)\|_2^2-\beta_q.
\]

The floor-corrected collision identity gives

\[
 Q_q(F)=2\Phi_q(F)\ge0.
\]

For a fixed window `q<=H`, use the weighted Hilbert norm

\[
 \|f\|_H^2=\sum_{q\le H}\frac{\|f_q\|_2^2}{c_q},
 \qquad
 \mathcal Q_H(F)=\sum_{q\le H}\frac{Q_q(F)}{c_q}=2\Psi_H(F),
\]

and write

\[
 \beta_H=\sum_{q\le H}\frac{\beta_q}{c_q}.
\]

## 2. One uniform-transposition step

Choose a coordinate transposition `tau` uniformly and then choose every side
of the interaction components between `F` and `tau F` by independent fair
coins.  For a component `K`, let `Delta_(K,q)` be its depth-`q` effect, and
put

\[
 R_q(F,\tau)=\frac14\sum_K\|\Delta_{K,q}\|_2^2,
 \qquad
 \overline R_q(F)=\mathbb E_\tau R_q(F,\tau).
\]

Every exact-factor discrepancy has zero total and zero point marginals.  It
therefore has no `U_0` or `U_1` Johnson-harmonic component.  If

\[
 D_q(F)=\frac14\mathbb E_\tau
       \|f_q(F)-\tau f_q(F)\|_2^2,
\]

then the transposition character ratios give

\[
 D_q(F)=\frac2n\|f_q(F)\|_2^2+s_q(F),
 \qquad s_q(F)\ge0.
\]

The exact heat identity is

\[
 \mathbb E[Q_q(F')\mid F]
   =Q_q(F)-D_q(F)+\overline R_q(F).
\]

Define

\[
 \rho=1-\frac2n,
 \qquad
 \gamma_q(F)=\overline R_q(F)-\frac2n\beta_q.
\]

Then, exactly,

\[
 \boxed{
 \mathbb E[Q_q(F')\mid F]
   =\rho Q_q(F)+\gamma_q(F)-s_q(F).
 }
\tag{2.1}
\]

In particular, the proposed inequality

\[
 \mathbb E[Q_q(F')\mid F]
 \le \rho Q_q(F)+\gamma_q(F)
\]

is correct.

With

\[
 \Gamma_H(F)=\sum_{q\le H}\frac{\gamma_q(F)}{c_q},
 \qquad
 \mathsf S_H(F)=\sum_{q\le H}\frac{s_q(F)}{c_q},
\]

equation (2.1) sums to

\[
 \mathbb E[\mathcal Q_H(F')\mid F]
 =\rho\mathcal Q_H(F)+\Gamma_H(F)-\mathsf S_H(F).
\tag{2.2}
\]

## 3. Iteration and the discounted criterion

For the Markov chain obtained by repeating this step,

\[
 \mathbb E\mathcal Q_H(F_T)
 \le
 \rho^T\mathcal Q_H(F_0)
 +\sum_{t=0}^{T-1}\rho^{T-1-t}
       \mathbb E\Gamma_H(F_t).
\tag{3.1}
\]

It is safe to replace `Gamma_H` on the right by its positive part.

There is an important distinction between the proposed `Gamma_H` and the
exact excess term.  Put

\[
 \widehat\Gamma_H(F)=\Gamma_H(F)-\mathsf S_H(F).
\]

Then (2.2) is an equality with `widehat Gamma_H`, and iteration gives

\[
 \sum_{t=0}^{T-1}\rho^{T-1-t}
   \mathbb E\widehat\Gamma_H(F_t)
 =\mathbb E\mathcal Q_H(F_T)-\rho^T\mathcal Q_H(F_0).
\tag{3.0}
\]

Thus a small discounted `widehat Gamma_H` condition is algebraically
equivalent to the desired terminal-energy statement.  It is not, by itself,
a new way to prove that statement.  The proposed `Gamma_H` is a genuine
upper surrogate because `S_H>=0`, but it can be much larger than the actual
excess noise when high Johnson harmonics are present.

There is a uniform initial bound.  A depth-`q` target occurs at most once in
one wreath and there are `W/n` wreaths, so

\[
 \mu_q(S)\le\frac Wn,
 \qquad
 \sum_S\mu_q(S)^2\le\frac{W^2}{n}.
\]

Consequently

\[
 \mathcal Q_H(F_0)\le \frac{H W^2}{n}.
\tag{3.2}
\]

For `T=n^2`,

\[
 \rho^T\mathcal Q_H(F_0)
 \le e^{-2n}\frac{H W^2}{n}=o(W).
\]

It follows that the following is a rigorous sufficient theorem:

\[
 \boxed{
 \sum_{t=0}^{n^2-1}\rho^{n^2-1-t}
   \mathbb E\bigl(\Gamma_H(F_t)\bigr)_+
   =o(W).
 }
\tag{DG}
\]

The stronger bound `O(H Cat_m)` also suffices and gives the natural
Catalan-scale residue.  Indeed, (3.1) then gives one exact terminal factor
with `mathcal Q_H=o(W)`, and hence weighted balanced overload `o(W)`.

## 4. Why the beta subtraction is exact

Write the centered heat step as

\[
 f'=P_\tau f+\zeta,
 \qquad P_\tau=\frac{I+\tau}{2},
 \qquad \mathbb E[\zeta\mid F,\tau]=0.
\]

Its conditional noise energy is

\[
 \mathbb E[\|\zeta_q\|_2^2\mid F,\tau]=R_q(F,\tau).
\]

Each component effect has zero total and zero point marginals: the two sides
of a component contain the same number of wreaths; every wreath has `n`
depth-`q` intervals and each coordinate belongs to exactly `m-q` of them.
Thus future uniform transpositions contract every component effect by at
least the same factor `rho`.

The decomposition

\[
 \overline R_q(F)=\frac2n\beta_q+\gamma_q(F)
\]

has a precise meaning.  Geometric propagation of the first term gives

\[
 \sum_{t=0}^{T-1}\rho^{T-1-t}\frac2n\beta_q
 =(1-\rho^T)\beta_q.
\]

Together with the surviving `rho^T beta_q` from the initial centered norm,
this is exactly the unavoidable final floor `beta_q`.  Only `gamma_q` is
excess propagated component noise.

For a deterministic transposition schedule this is also visible in the
exact martingale expansion

\[
 \mathbb E\|f_T\|_H^2
 =\|P_T\cdots P_1f_0\|_H^2
 +\sum_{t=1}^T
   \mathbb E\|P_T\cdots P_{t+1}\zeta_t\|_H^2.
\tag{4.1}
\]

Thus later smoothing discounts early component noise, but it does not make
that noise disappear.

## 5. A rigorous obstruction: connected overlays

If the interaction graph between `F` and `tau F` is connected, it has one
component.  The only two heat outcomes are `F` and `tau F`, so every
coordinate-relabeling-invariant energy is unchanged.  Algebraically,

\[
 R_q(F,\tau)
 =\frac14\|f_q(F)-\tau f_q(F)\|_2^2.
\tag{5.1}
\]

If every overlay encountered along a coordinate walk is connected, every
terminal factor is merely a coordinate relabeling of the initial factor and

\[
 \mathcal Q_H(F_T)=\mathcal Q_H(F_0)
\]

on every branch.  Nevertheless, the mean centered vector may be strongly
contracted.  Formula (4.1) then says that the covariance is exactly

\[
 \|f_0\|_H^2-\|\mathbb E f_T\|_H^2,
\]

so it exactly restores all spectral smoothing.

In particular, if an exact factor has connected overlays with every
coordinate transposition, then every adaptive transposition heat chain
started from it is trapped in its coordinate orbit.  A universal multistep
proof must either rule out such transposition-rigid factors above the target
energy, or establish enough fragmented overlays along the chosen trajectory.

This is an exact obstruction, not a weakness of the one-step accounting.

## 6. What can be bounded without new structure

For a moved target pair `{S,tau S}`, identify a component with a subset of
the original wreaths and put

\[
 d_K=a_K(S)-a_K(\tau S).
\]

Its contribution to `R_q` is `(1/2) sum_K d_K^2`.  Since the component
occurrence families partition the occurrences of `S` and `tau S`,

\[
 \frac12\sum_Kd_K^2
 \le\frac12(\mu_q(S)+\mu_q(\tau S))^2
 \le\mu_q(S)^2+\mu_q(\tau S)^2.
\]

Summing over moved pairs gives the universal bound

\[
 R_q(F,\tau)\le\sum_S\mu_q(S)^2
 =Q_q(F)+\beta_q+\lambda_qW.
\tag{6.1}
\]

On a fixed window `q<=A sqrt(m)`, `lambda_q=O_A(1)`, so this yields only

\[
 \gamma_q(F)\le Q_q(F)+O_A(W).
\]

That is much too large: after the geometric memory of order `n`, the desired
aggregate residue is only `O(H Cat_m)=O(HW/n)`.

There is also no automatic gain at the floor.  If `Q_q(F)=0`, every child is
integral and has nonnegative `Q_q`, so (2.1) implies

\[
 \gamma_q(F)\ge s_q(F)\ge0.
\tag{6.2}
\]

Accordingly, a pointwise Catalan-scale bound on `gamma_q` can fail as a proof
target even when the exact drift `gamma_q-s_q` is zero.  Any sharp structural
estimate must retain this harmonic cancellation.

At fixed Gaussian depths the integer floor `beta_q` can be `Theta(W)`, even
though the quota `c_q` is bounded.  Bounded quota capacity therefore does
not imply Catalan-scale component noise.

## 7. The genuine local replacement for one-shot HG

There is a sharper integer decomposition of the local gap.  For a fixed
`tau`, partition the moved depth-`q` targets into pairs
`p={S,tau S}` and put

\[
 \ell_p=\mu_q(S)+\mu_q(\tau S),
 \qquad
 b_q(F,\tau)=\frac12\#\{p:\ell_p\text{ is odd}\}.
\tag{7.0}
\]

The pair sum is preserved **componentwise**.  Here is the needed
justification.  If `tau=(a b)` and `C` is one cyclic wreath, each of `a,b`
belongs to exactly `m` of its `n=2m+1` middle intervals.  The total
`{a,b}`-incidence is therefore `2m=n-1`, so at least one middle interval of
`C` contains either both exchanged coordinates or neither.  That interval
is fixed by `tau` and gives an interaction edge joining the left copy of
`C` to the right copy of `tau C`.  After identifying that right copy with
`C`, every wreath vertex has a left-right loop.  The remaining ownership
edges are symmetric under `tau`, so every connected interaction component
has the same underlying wreath subset `K` on its two sides, namely `K` and
`tau K`.

Consequently, if `a_K(S)` is the number of `S` occurrences in `K`, the
opposite-side count is `a_K(tau S)`.  Thus

\[
 \Delta_K(S)+\Delta_K(\tau S)=0
\]

for every component separately, and every independent component choice
preserves `ell_p`.

Every component-cube outcome has integral entries on the pair with fixed
sum `ell_p`.  Its squared distance from the pair midpoint is therefore at
least zero when `ell_p` is even and at least `1/2` when it is odd.  Hence

\[
 R_q(F,\tau)\ge b_q(F,\tau).
\]

On the other hand, the contribution of the pair to
`(1/4)||f_q-tau f_q||^2` is

\[
 \frac12(\mu_q(S)-\mu_q(\tau S))^2,
\]

which is at least the same parity floor.  Define

\[
 G_q(F,\tau)=\frac14\|f_q-\tau f_q\|_2^2-b_q(F,\tau)\ge0,
\]

\[
 C_q(F,\tau)=R_q(F,\tau)-b_q(F,\tau)\ge0.
\]

Then the exact one-step drift has the transparent form

\[
 \boxed{
 \mathbb E[Q_q(F')\mid F,\tau]
   =Q_q(F)-G_q(F,\tau)+C_q(F,\tau).
 }
\tag{7.1}
\]

Here `G_q` is the gain of ideal integral balancing inside every
`tau`-orbit, while `C_q` is exactly the extra price imposed by bundling the
occurrences into interaction components.

More explicitly, on one moved pair put

\[
 d_K=a_K(S)-a_K(\tau S).
\]

Its contribution to `R_q` is `(1/2) sum_K d_K^2`.  Equality with the parity
floor holds exactly when all `d_K` vanish if `ell_p` is even, and exactly one
`d_K` equals `+1` or `-1` if `ell_p` is odd.  Thus `C_q` is an exact
component-alignment defect.  In a connected overlay, `C_q=G_q`, giving zero
drift.

A sharp local theorem can equivalently be stated as

\[
 \mathbb E_\tau\sum_{q\le H}\frac{G_q-C_q}{c_q}
 \ge \frac{\eta_A}{n}\mathcal Q_H(F)
   -\frac{C_A}{n}H\operatorname{Cat}_m.
\tag{7.2}
\]

This formulation separates the discrete plateau problem from the cyclic
component-alignment problem.  Ordinary spectral smoothing controls the
uncorrected squared-gradient term in `G_q+b_q`, but does not by itself
control either the parity floor `b_q` or the component excess `C_q`.

A pointwise theorem strong enough to make the multistep chain work is

\[
 \boxed{
 \Gamma_H(F)-\mathsf S_H(F)
 \le \frac{2-\eta_A}{n}\mathcal Q_H(F)
    +\frac{C_A}{n}H\operatorname{Cat}_m
 }
\tag{LH_A}
\]

for `H=ceil(A sqrt(m))`, at least whenever `mathcal Q_H(F)` is above the
target scale.  By (2.2), this gives

\[
 \mathbb E\mathcal Q_H(F')
 \le\left(1-\frac{\eta_A}{n}\right)\mathcal Q_H(F)
   +\frac{C_A}{n}H\operatorname{Cat}_m.
\]

Iteration, stopped on first reaching the target, produces an exact factor
with

\[
 \mathcal Q_H=O_A(H\operatorname{Cat}_m)=o(W).
\]

Equivalently, `(LH_A)` is the averaged local component-gap estimate

\[
 \mathbb E_\tau\left[
   \frac14\sum_{q\le H}\frac{
    \|f_q-\tau f_q\|_2^2-
    \sum_K\|\Delta_{K,q}\|_2^2}{c_q}
 \right]
 \ge \frac{\eta_A}{n}\mathcal Q_H(F)
   -\frac{C_A}{n}H\operatorname{Cat}_m.
\]

This is a legitimate multistep weakening of a constant-gap one-shot
permutation theorem.  It is still a new fragmentation theorem; neither
global spectral smoothing nor the floor subtraction proves it.

## 8. Adjacent versus unrestricted transpositions

The factor `rho=1-2/n` uses a uniformly random transposition among all
coordinate pairs.  If one instead chooses uniformly from the adjacent edges
of a fixed coordinate path, the underlying averaging operator has path
spectral gap of order `n^{-3}` per selected edge (the path Laplacian gap is
`Theta(n^{-2})` and one edge among `Theta(n)` is selected).  Thus `O(n)`
such adjacent steps do not provide constant continuous smoothing.

A length-`O(n)` round can have constant continuous smoothing only if its
coordinate-pair graph is itself expanding (for example, a bounded-degree
expander schedule), or if unrestricted random transpositions are used.
This distinction is separate from, and easier than, the component-noise
problem above.

## Conclusion

The discounted positive-`gamma` proposal is mathematically sound and is a
clean exact-factor sufficient criterion.  It does not yet yield MWB because
no available theorem bounds the excess noise `gamma` along a suitable
trajectory.  Connected overlays show that no amount of global spectral
telescoping can supply such a bound by itself.  The remaining theorem is
precisely a Catalan-residue fragmentation bound such as `(LH_A)`, or a
nonlocal correlated sign rule that proves `(DG)` directly.
