# Audit: Bennett--Bohman exponent, the \(\tau\)-squeeze, and self-correcting compensators

Date: 2026-07-25

Method: pure mathematics only.

## Verdict

The calculation

\[
 \exp\left[-\frac{\log(D/\log N)}{2(k_T-1)}\right]
 \sim m^{-1/[2(1+\tau)]},
 \qquad k_T=n(1+\tau),
\]

is an algebraically correct substitution if one assumes that exact
leftover formula and \(\log D\sim2m\log m\).  It is not a valid theorem
for the augmented cyclic-interval orbit:

1. \(k_T=\Theta(m)\) grows, whereas the cited random-greedy matching
   estimates are fixed-uniformity statements unless a separate uniform
   quantitative theorem is supplied;
2. the orbit is not linear: adjacent nested protected targets have
   relative codegree \(\Theta(1/m)\), so the maximum pair codegree is
   \(L=\Theta(D/m)\), not \(O(\log N)\);
3. failure of a generic sufficient bound is not a lower bound on the
   actual random greedy process, and certainly not an impossibility
   theorem for a single-template orbit packing.

The proposed self-correcting compensator inequality is a legitimate
possible method, but currently a target rather than a proved drift law.
It must not assume that decorated-edge degree density equals unused
resource density.

## 1. Algebraic substitution and its scope

If

\[
 k_T=n(1+\tau)=(2m+1)(1+\tau)
\]

and \(\log(D/\log N)=(2+o(1))m\log m\), then

\[
 \frac{\log(D/\log N)}{2(k_T-1)}
 =\left(\frac1{2(1+\tau)}+o(1)\right)\log m.
\]

So the displayed power \(m^{-1/[2(1+\tau)]}\) follows formally.  In
particular it is \(m^{-1/2}\) at \(\tau=0\) and \(m^{-1/6}\) at
\(\tau=2\).

This only audits the arithmetic.  It does not verify that the theorem
being substituted into holds uniformly for \(k_T=\Theta(m)\).

## 2. The actual codegree parameter

The augmented orbit contains same-phase nested adjacent target pairs with

\[
 \frac{\Delta_2}{D}=\Theta(1/m).
\]

Thus \(L=\Theta(D/m)\).  Any general leftover estimate whose true
parameter is \(L/D\) must use

\[
 \left(\frac LD\right)^{1/[2(k_T-1)]}
 =m^{-1/[2(k_T-1)]}
 =\exp[-\Theta(\log m/m)]
 =1-o(1),
\]

not \(m^{-1/[2(1+\tau)]}\).  Likewise, hypotheses requiring
\(L\ll D/\operatorname{polylog}N\) fail because
\(\log N=\Theta(m)\), while \(L/D=\Theta(1/m)\).

Therefore the Bennett--Bohman black box cannot currently be invoked for
this orbit.

## 3. What the \(\tau\)-calculation can and cannot imply

Even granting the heuristic power, \(m^{-1/2}\) is not a proved
\(o(m^{-1/2})\) leftover, while \(m^{-1/6}\) is much larger.  Hence that
specific estimate would not establish the desired near-factor.

It does not prove that a single-template nibble or packing is impossible.
The middle-only wreath orbit is a direct counterexample to such an
inference: its generic random-greedy guarantee is weak, yet the MSW
theorem gives an exact matching.

For a direct augmented matching followed by literal repair, the exact
gap target is

\[
 T-\nu=o(T/\sqrt m),
\]

because \(K=\Theta(g\sqrt m)\) and \(W\sim Tg\).  The stronger
\(o(T/Q)\) target belongs to a \(1+o(1/Q)\) all-weight cut argument, not
to the necessary direct repair ledger.

## 4. Self-correcting compensator audit

A drift inequality of the form

\[
 \mathbb E[\Delta\mathcal E\mid\mathcal F_t]
 \le-c_t\mathcal E\,\Delta t
   +O(\mathcal E(\Delta\mathcal E)^2),
 \qquad c_t\ge c_0z_t^a,
\]

would be valuable.  Together with a quadratic-variation bound, it can
replace accumulation of roundwise errors by a stationary corridor.

But four assertions still have to be proved:

1. there is a sampling distribution in every residual tag fibre which
   produces the stated negative drift simultaneously for all protected
   strata;
2. the restoring coefficient has the claimed lower bound;
3. the quadratic and Taylor errors are smaller than the restoring drift
   outside the intended corridor;
4. weighted maximal inequalities control the exponentially many fibres
   at total repair cost \(o(W)\).

The stationary scale is controlled by noise divided by \(c_t\); it is
not literally independent of the run length without these estimates.

Finally, \(z_t\) is unused-resource/tag density.  The fraction of fixed
priority decorations still alive is a different quantity \(\rho_t\).
Absent a highly aligned residual it is on the scale \(z_t^{K}\), and the
assertion \(d_t(v)\ge z_td_0(v)\) is precisely an additional design
theorem, not a consequence of monotone deletion.  A self-correcting
argument may aim to prove such alignment, but it cannot use it as its
starting hypothesis.

There is an exact linear-program formulation of the first item.  If
\(p_e\) is the proposed conditional law on residual decorated edges, its
resource load is

\[
 \ell_t(v)=\sum_{e\ni v}p_e.
\]

Making all compensators equal inside a stratum requires the vector
\((\ell_t(v))_v\) to be approximately constant there, simultaneously
with the prescribed tag marginals.  This is a residual fractional
multirank matching/transport problem.  The raw orbit has the uniform
solution by symmetry, but an exposed residual does not inherit that
symmetry.  Thus a ``choose the probabilities to restore the drift'' rule
is feasible only after proving the relevant residual Hall/weighted-cut
inequalities; it is not an automatic choice of transition kernel.
