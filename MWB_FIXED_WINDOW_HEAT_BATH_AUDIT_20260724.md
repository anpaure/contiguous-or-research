# Audit: fixed-window MWB heat bath

Date: 2026-07-24

## Verdict

The fixed-window diagonalization, floor-corrected quadratic energy, exact
interaction-component heat bath, Johnson spectral contraction, iterated
recurrence, and one-cube missing-target lower bound are all valid.

They do **not** prove MWB.  The remaining hypothesis is the discounted
positive component-variance bound `(HB_A)`.  This is a genuine quantitative
condition over one relaxation time of the exact-factor Markov chain; no
bound for it follows from the continuous spectral contraction alone.

## 1. Fixed windows

For fixed `A>0`, put

\[
H_A=\lceil A\sqrt m\rceil,
\qquad
\alpha_m(A)=\frac1W\min_F\sum_{q\le H_A}\frac{O_q(F)}{c_q}.
\]

Then MWB is equivalent to

\[
\alpha_m(A)\longrightarrow0
\qquad\text{for every fixed }A.
\]

The forward implication is immediate.  For the reverse implication, choose
thresholds `M_j>=j^4` after which `alpha_m(j)<=1/j`, and use the diagonal
`omega(m)=j` on `[M_j,M_(j+1))`.  This keeps
`omega(m)=o(sqrt(m))` and gives the required one-factor, all-depth sum.

## 2. Integer floor energy

Write

\[
W=cN+\rho,
\qquad
Q(\mu)=\sum_S(\mu(S)-c)(\mu(S)-c-1).
\]

Every summand is nonnegative.  If

\[
D=\sum_S(c-\mu(S))_+,
\qquad
E=\sum_S(\mu(S)-c-1)_+,
\]

then the exact overload is `O=max(D,E)`, and pointwise integer inequalities
give

\[
Q\ge2D,\qquad Q\ge2E,
\qquad\text{hence}\qquad 2O\le Q.
\]

For `lambda=c+theta`, `f=mu-lambda 1`, and
`beta=N theta(1-theta)`, one has exactly

\[
Q=\|f\|_2^2-\beta.
\]

The subtraction of `beta` is indispensable: it is the unavoidable integer
floor, not error.

## 3. Exact integral heat bath

Overlay an exact factor `F` with `tau F`, where `tau` is a coordinate
transposition.  In every connected component of the bipartite ownership
graph, select either the complete `F` side or the complete `tau F` side.
Every side choice is again an exact integral factor.

If `Delta_(K,q)` is the depth-`q` load change of component `K`, a fair
independent side choice gives

\[
\mathbb E\|f_q(G)\|_2^2
=
\left\|\frac{f_q+\tau f_q}{2}\right\|_2^2
+\frac14\sum_K\|\Delta_{K,q}\|_2^2.
\]

Because every wreath gives the same point marginals, `f_q` has no Johnson
harmonic components of degrees zero or one.  Averaging over all coordinate
transpositions therefore gives

\[
\mathbb E_\tau
\left\|\frac{f_q+\tau f_q}{2}\right\|_2^2
\le\left(1-\frac2n\right)\|f_q\|_2^2.
\]

Put

\[
R_q(F,\tau)=\frac14\sum_K\|\Delta_{K,q}\|_2^2,
\qquad
\gamma_q(F)=\mathbb E_\tau R_q(F,\tau)-\frac2n\beta_q.
\]

Then, with `rho=1-2/n`,

\[
\mathbb E[Q_q(G)\mid F]\le \rho Q_q(F)+\gamma_q(F).
\]

There is a useful exact refinement.  Put

\[
s_q(F)=\frac14\mathbb E_\tau
\|f_q-\tau f_q\|_2^2-\frac2n\|f_q\|_2^2\ge0.
\]

Then

\[
\boxed{
\mathbb E[Q_q(G)\mid F]
=\rho Q_q(F)+\gamma_q(F)-s_q(F).
}
\]

Here `s_q` is precisely the spectral surplus from Johnson harmonics above
degree two.  The sharp noise quantity is therefore `gamma_q-s_q`, not
`gamma_q` alone.

After weighting by `1/c_q` and iterating,

\[
\mathbb E\mathcal Q_A(F_T)
\le
\rho^T\mathcal Q_A(F_0)
+\sum_{t<T}\rho^{T-1-t}\mathbb E\Gamma_A(F_t).
\]

The elementary occurrence cap `mu_q(S)<=W/n` gives
`mathcal Q_A(F_0)<=H_A W^2/n`.  At `T=n^2` the first term is `o(W)`.
Therefore the stated criterion

\[
\sum_{t<n^2}\rho^{n^2-1-t}
\mathbb E[\Gamma_A(F_t)_+]=o(W)
\tag{HB_A}
\]

is sufficient for the fixed-window MWB conclusion.

The criterion may be weakened by replacing `Gamma_A` by

\[
\Gamma_A-S_A,
\qquad
S_A=\sum_{q\le H_A}\frac{s_q}{c_q},
\]

and taking the positive part.

With

\[
\widehat\Gamma_A=\Gamma_A-S_A,
\]

the discounted relation is actually an identity:

\[
\sum_{t<T}\rho^{T-1-t}
\mathbb E\widehat\Gamma_A(F_t)
=
\mathbb E\mathcal Q_A(F_T)-\rho^T\mathcal Q_A(F_0).
\]

Consequently, a small discounted `widehatGamma` hypothesis is essentially
equivalent to the desired terminal-energy conclusion; it is not an
independent simplification.  The version using `Gamma_+` is valid but may be
much stronger, because it discards the potentially large harmless harmonic
surplus `S_A`.

A sharp one-step replacement for the overly strong constant-gap `(HG_L)`
is the scale-correct estimate

\[
\boxed{
\Gamma_A(F)-S_A(F)
\le
\frac{2-\eta_A}{n}\,\mathcal Q_A(F)
+\frac{C_A}{n}H_A\operatorname{Cat}_m.
}
\tag{MHG_A}
\]

Indeed the exact drift then contracts by `eta_A/n`; iteration for
`O_A(n log(...))` steps reaches
`O_A(H_A Cat_m)=o(W)` on every fixed window.  This is the natural
transposition-scale heat-gap lemma.  It remains unproved.

## 4. Scope of the criterion

`(HB_A)` is not supplied by the spectral estimate.  The spectral term
controls the coherent displacement of the whole load vector; `Gamma_A`
measures the componentwise variance that survives the legal integral
rounding.  The latter is exactly the old obstruction in multistep form.

At the opposite extreme, if an ownership overlay is connected, it has only
one component choice.  The child is then either `F` or `tau F`, so its energy
is unchanged: covariance cancels the entire mean smoothing exactly.  This
shows directly why a spectral bound alone cannot control the heat bath,
even after iteration.

Likewise, at a global minimizer of `mathcal Q_A` over exact factors, every
legal component cube has nonnegative average drift.  Hence any universal
heat-gap inequality at that minimizer already forces
`mathcal Q_A=O_A(H_A Cat_m)`.  Such an inequality is a precise restatement
of the missing integral theorem, not a softer consequence of continuous
smoothing.

The fair heat bath is a symmetric averaging operation on each legal
switching cube.  It is not intrinsically energy-biased.  Thus one should not
expect iteration alone to force a low-energy factor: a proof must establish
a structural/coboundary estimate for `Gamma_A`, or replace the fair bath by
a legal energy-decreasing multistep circuit.

The strongest unconditional crude bound is only

\[
R_q(F,\tau)
\le \sum_S\mu_q(S)^2
=Q_q+\beta_q+\lambda_q W,
\]

which is `Q_q+O_A(W)` on a fixed window and is far too large after summing
over `Theta(sqrt(m))` depths.  Thus bounded quotas alone do not establish
`(MHG_A)`.

## 5. Transposition-pair integer floor

For a fixed coordinate transposition `tau=(a b)`, every ownership component
is individually `tau`-stable.  Indeed, in one wreath the total incidence of
`a,b` among its `n=2m+1` middle intervals is `2m=n-1`; hence some interval
contains either both or neither and is fixed by `tau`.  This fixed middle
set joins the wreath on the left to its own `tau`-image on the right.
Moreover every ownership edge `C_L--(tau D)_R` is paired by `tau` with
`D_L--(tau C)_R`.  Thus a connected component has the same wreath subset
`K` on both sides, namely `K` and `tau K`.

Consequently, for every moved target pair `p={S,tau S}`, every independent
component switch preserves

\[
\ell_p=\mu_q(S)+\mu_q(\tau S).
\]

Define the pairwise integer floor

\[
b_q(F,\tau)=\frac12\#\{p:\ell_p\text{ is odd}\}.
\]

Let

\[
D_q(F,\tau)=\frac14\|f_q-\tau f_q\|_2^2,
\qquad
R_q(F,\tau)=\frac14\sum_K\|\Delta_{K,q}\|_2^2.
\]

Integer pair loads of fixed sum give

\[
D_q\ge b_q,
\qquad
R_q\ge b_q.
\]

Put

\[
G_q=D_q-b_q\ge0,
\qquad
C_q=R_q-b_q\ge0.
\]

Then the exact fixed-transposition drift becomes

\[
\boxed{
\mathbb E[Q_q(F')\mid F,\tau]
=Q_q(F)-G_q(F,\tau)+C_q(F,\tau).
}
\]

`G_q` is the ideal integer pair-balancing gain.  `C_q` is precisely the
extra variance forced by bundling target corrections into whole ownership
components.  Pairwise, `C_q=0` exactly when every component pair imbalance
is zero, except that one imbalance `+/-1` is permitted when `ell_p` is odd.
A connected overlay has `C_q=G_q`, giving zero drift.

The clean missing transposition theorem is therefore

\[
\boxed{
\mathbb E_\tau\sum_{q\le H_A}\frac{G_q-C_q}{c_q}
\ge
\frac{\eta_A}{n}\mathcal Q_A(F)
-\frac{C_A}{n}H_A\operatorname{Cat}_m.
}
\tag{PAIR_A}
\]

This is equivalent in scale to `(MHG_A)`, but removes the exact local parity
floor before comparing coherent gain with component noise.

## 6. One-cube obstruction

At a fixed rank, call a target robust if one interaction component contains
an occurrence on both selectable sides.  A robust target survives every
side choice.  If `R` targets are robust, `U=N-R`, and `d_S` is the number of
one-sided components containing a nonrobust target, then

\[
2R+\sum_{S\text{ nonrobust}}d_S\le2W,
\qquad
\Pr(S\text{ is missed})=2^{-d_S}.
\]

Convexity yields

\[
\mathbb E M_q
\ge U\,2^{-2(W-R)/U}.
\]

At the first shadow, if `R<=(1-delta)N_1`, this is

\[
\mathbb E M_1\ge(\delta/4-o(1))N_1.
\]

Hence a single fair interaction cube cannot yield a small first-shadow
defect unless almost every target is already robust within an individual
component.

## Exact remaining theorem in this lane

For every fixed `A`, prove `(HB_A)`, or prove an equivalent multistep legal
factor-fibre estimate that dissipates

\[
\mathcal Q_A(F)=\sum_{q\le A\sqrt m}\frac{Q_q(F)}{c_q}
\]

to `o(W)`.  Every intermediate state must remain one exact wreath factor.
The cleanest local candidate is `(MHG_A)` above: it asks for a positive
fraction of the transposition-scale coherent dissipation after subtracting
both the exact integer floor and the higher-harmonic surplus.
Equivalently, use the more local pair-floor formulation `(PAIR_A)`.
