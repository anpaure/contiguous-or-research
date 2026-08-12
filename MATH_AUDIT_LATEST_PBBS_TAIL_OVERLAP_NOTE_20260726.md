# Audit of the repaired sprinkling theorem, the PBBS sub-Gaussian band, and the exterior quantifier

Date: 2026-07-26

## Verdict

The three points in the latest note have the following exact status.

1. The repaired sprinkling theorem is correct **with the aggregate shallow-hole hypothesis** and for an approximate row-count/covering formulation.  It does not preserve an exact middle factor.
2. The canonical PBBS support theorem is genuinely uniform for every depth (1\le q\le m), and the proved critical residence bound plus the audited compiler really does give a literal coefficient-one central band for every (h=o(\sqrt m)).
3. The existing product-SCD exterior word covers the exterior at every cutoff, but has cost (o(W)) if and only if (H/\sqrt m\to\infty).  At (H=A\sqrt m) for fixed finite (A), its normalized cost tends to a positive constant (F(A)).  It therefore does not overlap the PBBS theorem below the Gaussian scale.

Thus the suggested final quantifier check has a negative answer: the full constant-one theorem is not closed by the two existing constructions.  The unconditional central result is nevertheless much stronger than a logarithmic band.

## 1. Repaired sprinkling theorem

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad C_m=W/n,
 \qquad N_q=\binom{n}{m-q},
\]

and let (M_q(\mathcal Q)) be the number of uncovered rank-((m-q)) targets.  Put

\[
 q_0=\left\lceil\sqrt{2m\log\log m}\right\rceil .
\]

The exact sufficient shallow hypothesis is

\[
 \boxed{\sum_{0\le q\le q_0}M_q(\mathcal Q)=o(W).}
 \tag{1.1}
\]

Add (k=\lceil C_m/\log m\rceil) independent uniform cyclic orders.  The exact interval probability gives, for a fixed rank-((m-q)) target,

\[
 \Pr(\text{missed by the sprinkle})
 \le \exp\!\left(-\frac{W}{N_q\log m}+o(1)\right).
\]

Moreover

\[
 \lambda_q:=\frac W{N_q}
 =\prod_{i=1}^q\frac{m+1+i}{m+1-i},
 \qquad
 \log\lambda_q\ge\frac{q(q+1)}{m+1}\ge\frac{q^2}{m}.
\]

Hence (q>q_0) implies (\lambda_q/\log m\ge\log m), and therefore

\[
 \sum_{q>q_0}\mathbb E M_q^{\rm sprinkle}
 \le \frac1m\sum_qN_q
 \le\frac{2^{n-1}}m
 =O(W/\sqrt m)=o(W).
 \tag{1.2}
\]

Complementation duplicates the same estimate on the upper side.  Markov's inequality and (1.1) produce a deterministic realization with aggregate (o(W)) holes.  The final row count is ((1+o(1))C_m).

The qualification is essential: adjoining arbitrary rows preserves approximate size and coverage, and adds only (o(W)) middle occurrences, but it does **not** preserve an exact middle ownership factor.  Thus this theorem cannot be inserted verbatim into an exact-factor statement.

## 2. What is uniform in the PBBS theorem

For the same canonically oriented centered PBBS Johnson (2)-factor, the global-maximum fan theorem proves

\[
 1\le \mu^{\rm corr}_{P,q}(S)\le\binom{2q+1}{q}
 \quad
 \left(1\le q\le m,\ S\in\binom{[n]}{m-q}\right).
 \tag{2.1}
\]

Thus the lower correct-rank support is all-depth, not a fixed-(q) extrapolation.  It is legitimate to use it to refute an independent-depth entropy bill.  It is not yet a literal cyclic-wreath word: some PBBS windows have the wrong intersection rank, and the Johnson components need not have cyclic residence.

The audited dominance-staircase compiler gives

\[
 L_H\le W+2HC_m+2(5H-1)\nu_H(P_m),
 \tag{2.2}
\]

covering ranks (m-H+1,\ldots,m+H+1).  The fixed-window reciprocal-height estimate at

\[
 H_0=\lceil\sqrt m\rceil
\]

gives an absolute constant (C) with

\[
 \nu_{H_0}(P_m)\le C C_m\sqrt m.
 \tag{2.3}
\]

Since (\nu_H) is monotone increasing in the allowed residence length,

\[
 \nu_H(P_m)\le C C_m\sqrt m\qquad(H\le H_0).
 \tag{2.4}
\]

For an intended half-width (h=o(\sqrt m)), take (H=h+1).  This is the necessary one-rank shift: (2.2) then covers at least

\[
 [m-h,m+h+1].
\]

Substitution yields

\[
 L_{h+1}-W=O(C_mh\sqrt m)=o(W),
 \tag{2.5}
\]

because (W=(2m+1)C_m).  Thus every (h=o(\sqrt m)), including (h=\sqrt m/\log m), is an unconditional literal central-band theorem.  No monotonicity assumption on a separate constant (\kappa(A)) is needed; monotonicity of (\nu_H) and the single (A=1) bound suffice.

## 3. Exact exterior quantifier

For the exact even-dimensional product-SCD exterior length, write

\[
 \mathsf W_m=\binom{2m}{m}.
\]

The construction covers both exterior tails for every cutoff.  If

\[
 H/\sqrt m\longrightarrow c<\infty,
\]

then its normalized length has the exact limit

\[
 \frac{L_m(m-H-1)}{\mathsf W_m}\longrightarrow F(c),
\]

where

\[
 F(c)=2\sqrt2\int_0^\infty
 8\sqrt{\frac2\pi}\,y^2e^{-2y^2}
 e^{-2(c-y)_+^2}\,dy>0.
 \tag{3.1}
\]

In particular (F(0)=2\sqrt2).  The uniform upper bound

\[
 \frac{L_m(m-H-1)}{\mathsf W_m}
 \le C_0e^{-H^2/(8m)}
\]

then proves the sharp equivalence

\[
 \boxed{
 L_m(m-H-1)=o(\mathsf W_m)
 \iff H/\sqrt m\to\infty .}
 \tag{3.2}
\]

The trimmed odd lift doubles both the exterior length and, asymptotically, the middle width, so it has the same normalized limit.  The exterior construction is factor-blind, so it remains valid after arbitrary central recoupling or deletion; there is no hidden MSW-specific interface.  Its problem is purely its positive baseline cost at fixed Gaussian cutoff.

## 4. Consequence

The proved regimes are

\[
 \text{PBBS central: }h=o(\sqrt m),
 \qquad
 \text{product-SCD exterior economical: }H/\sqrt m\to\infty.
\]

They leave a genuine Gaussian annulus.  Closing it still requires, for example,

\[
 \nu_{\lceil A\sqrt m\rceil}(P_m)
 =o_A(C_m\sqrt m)
 \quad\text{for every fixed }A>0,
\]

followed by diagonalization, or a new annulus/fusion construction.  A fixed-(A) product-SCD tail does not close the gap.
