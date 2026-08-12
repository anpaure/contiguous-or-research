# Compensated \(+2\) profile propagation with a \((\log m)^2\) terminal cutoff

Date: 2026-07-27

> **AUDIT WARNING.**  The literal \(+2\)-only hypothesis
> (CG\(_J\)) below is false in physical profile order.  A quadratic Taylor
> term may repeat the same new resource (for example one compensation coin),
> producing a repeated-child \(+1\) diagonal.  The correct generator is
> (CG'\(_J\)) in
> `MATH_AUDIT_COMPENSATED_PLUS_TWO_CUTOFF_REPEATED_CHILD_DIAGONAL_20260727.md`.
> The cutoff arithmetic remains viable if that diagonal satisfies
> \(\delta_t\le m^{-1+o(1)}\) uniformly for \(t\le J\), but this bound is not
> proved here.  Accordingly this file is a conditional reduction, not a
> closure theorem.

## 0. Outcome

The uncompensated positive profile hierarchy has a genuine \(+1\) spine and
cannot be closed by scalar all-order weights.  In the compensated generator,
the exact first-order drift is subtracted.  Its positive Taylor remainder
starts at \(+2\).  This distinction permits a finite terminal cutoff.

Put

\[
 {cal T}=\Theta(m\log m),\qquad
 J=\lceil(\log m)^2\rceil,
 \qquad
 \theta=2A\sqrt{\cal T}=\Theta(\sqrt{m\log m}).
\tag{0.1}
\]

Assume the already isolated equality-resolved compensated generator bound
through total profile order \(J\):

\[
 (\mathcal G\mathscr E)_s^+
 \le
 \sum_{\substack{\ell\ge2\\s+\ell\le J}}
 A^\ell\kappa_{s+\ell}^{\ell-1}\mathscr E_{s+\ell}
 +\mathscr B_s^{(J)},
\tag{CG\(_J\)}
\]

where

\[
 \kappa_t\le\frac{Ct^4}{m^2}qquad(t\le J)
\tag{0.2}
\]

and \(\mathscr B_s^{(J)}\) contains only equality-resolved physical profiles
of total order at least \(J\).

Then all internal shifts in (CG\(_J\)) are absorbed by the geometric score

\[
 \Phi_J=\sum_{s=0}^{J}\theta^s\mathscr E_s.
\tag{0.3}
\]

Moreover, the proved time-zero higher-codegree estimate makes the complete
terminal contribution, including the factor \(\theta^J\), equal to

\[
 \boxed{\exp[-(1/2-o(1))(\log m)^3].}
\tag{0.4}
\]

A trajectory-specific Doob quarantine therefore pays \(\mathscr B^{(J)}\)
at \(o(W)\) cost.  No all-order initialization and no post-collar scalar
energy is required.

The remaining theorem is precisely (CG\(_J\)) for the actual compensated
column--row and coin-fibre generator.

## 1. Absorbing the internal \(+\ell\) shifts

Let \(t=s+\ell\).  Over the time horizon \({\cal T}\), the coefficient of
\(\theta^t\mathscr E_t\) entering from the \(\ell\)-shift is at most

\[
 {cal T}A^\ell\kappa_t^{\ell-1}	heta^{-\ell}.
\tag{1.1}
\]

Since \(\kappa_t\le1\), the choice in (0.1) gives

\[
 {cal T}A^\ell\kappa_t^{\ell-1}\theta^{-\ell}
 \le2^{-\ell}{\cal T}^{1-\ell/2}.
\tag{1.2}
\]

Summing over \(\ell\ge2\),

\[
 \sum_{\ell\ge2}2^{-\ell}{\cal T}^{1-\ell/2}
 \le\frac12.
\tag{1.3}
\]

Thus the integrated internal upward operator has norm at most \(1/2\) on
\(\Phi_J\).  The proof uses essentially that \(\ell=1\) is absent: a
\(+1\) term would require \(\theta\gtrsim{cal T}\) and would reproduce the
consecutive-spine divergence.

## 2. Terminal initialization after the geometric weight

The higher-codegree theorem through \(J=o(H)\) and the ordered child count
give, from one marked physical incidence,

\[
 \mathfrak q_J
 \le\left(\frac{CJ^2}{m}\right)^{J-1}.
\tag{2.1}
\]

The weighted terminal mass is therefore at most

\[
 \theta^J\mathfrak q_J
 \le
 \left(
   \frac{C\theta J^2}{m}
 \right)^J\frac{m}{CJ^2}.
\tag{2.2}
\]

Now

\[
 \frac{\theta J^2}{m}
 =m^{-1/2}(\log m)^{9/2+o(1)},
\tag{2.3}
\]

so

\[
 \log(\theta^J\mathfrak q_J)
 \le-left(\frac12-o(1)\right)J\log m,
\tag{2.4}
\]

which proves (0.4).

For a fixed terminal physical profile, its natural normalized link is a
nonnegative stopped supermartingale until the preceding stops.  Doob's
inequality pays a threshold crossing from its time-zero mass.  If the whole
active terminal star is quarantined at first crossing, the threshold factor
cancels exactly as in the unweighted terminal reduction.  Summing (2.4) over
all polynomial marked types remains \(o(1)\) per base incidence.

## 3. Consequence for the physical loss

Assume that (CG\(_J\)) is verified and that the degree/whole-arm stops have
the already proved \(o(W)\) incidence.  Stop a marked occurrence at its first
internal profile violation or terminal order-\(J\) violation.  Equations
(1.3) and (2.4), followed by the exact selected-incidence clock

\[
 \int r\nu_tE_t\,dt=(1+o(1))W(1-z),
\tag{3.1}
\]

give

\[
 \boxed{\text{total compensated profile quarantine}=o(W).}
\tag{3.2}
\]

This supplies the missing hereditary profile input for the ordinary-frame
near-factor process without a finite arbitrary-residual boundary.

## 4. Exact audit boundary

The algebra in Sections 1--3 is finite.  It uses only profile orders at most
\((\log m)^2\), where the static catalogue estimates are already available.
The unresolved assertion is catalogue-dynamic:

\[
\boxed{
 \text{after equality resolution and physical compensation, the positive
 generator through order }J\text{ obeys (CG\(_J\)) and has no residual
 coherent }+1\text{ term}.}
\tag{4.1}
\]

Any failure is now an explicit compensated column--row or coin-fibre orbit at
polylogarithmic total order.  The post-\(H\) consecutive spine is outside the
argument and cannot refute it.
