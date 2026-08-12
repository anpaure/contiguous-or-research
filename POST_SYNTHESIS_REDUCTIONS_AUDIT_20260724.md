# Audit of the post-synthesis reductions

Sources audited:

* MATHEMATICAL_HANDOFF.md, items 1398--1399;
* MATH_ATTACK_30_LANE_SYNTHESIS_20260724.md, Sections 5.5--5.6;
* HARD_QUOTA_STAR_MATCHING_REDUCTION_RAW_20260724.md;
* HARD_QUOTA_STAR_MATCHING_REDUCTION_AUDIT_20260724.md;
* GLOBAL_COMPONENT_NOISE_MINIMIZER_RAW_20260724.md;
* GLOBAL_COMPONENT_NOISE_MINIMIZER_AUDIT_20260724.md;
* GLOBAL_COMPONENT_NOISE_SPECTRAL_CROSS_AUDIT_20260724.md.

Date: 2026-07-24

## 1. Verdict

Both post-synthesis additions are valid conditional sufficient reductions.
Their constants and odd exact-factor normalization check.

Three qualifications are required.

1. The hard-quota exceptional-size estimate implies MWB only when one common
   \(F=G\sqcup B\) and its quota domination hold throughout every fixed
   Gaussian window, followed by diagonalization, or throughout one admissible
   growing window. Small \(|B|\) alone does not imply MWB.
2. In the component-noise section, \(R_H\) must be defined by its exact
   unscaled squared side-difference formula. It is four times the literal
   variance contributed by fair complete-side choices. Calling it simply
   “component variance” can introduce a factor-four ambiguity.
3. Handoff item 1399 incorrectly says that exact-factor histograms have zero
   point margins. Their point margins are fixed and nonzero. The **centered**
   histograms have zero point margins, which is exactly what removes Johnson
   degrees zero and one. The spectral constant \(4(n-1)\) remains correct.

The corrected component-noise criterion must be imposed on a global
minimizer of the same \(H\)-window objective, for every fixed Gaussian
window if MWB is the desired conclusion. Neither new criterion is necessary
or known comparable with RFEN, LM\(_A\), or SCOV\(_A\).

## 2. Common odd exact-factor normalization

Both reductions use
\[
n=2m+1,\qquad
W=\binom{n}{m},\qquad
N_q=\binom{n}{m-q},\qquad
c_q=\left\lfloor\frac{W}{N_q}\right\rfloor ,
\]
and
\[
\operatorname{Cat}_m=\frac{W}{n}.
\]

This is the odd exact-factor normalization. No even-dimensional
\(\binom{2m}{m}\) quantity enters either reduction.

The controlled ranks satisfy \(1\le q\le H\le m-1\) in the hard-quota
argument. For the component spectral argument one may take
\(H\le m-2\); the terminal singleton rank has constant histogram and can be
discarded.

## 3. Hard-quota exceptional completion

### 3.1 Reciprocal quota mass

Put
\[
\lambda_q=\frac{W}{N_q}
=\prod_{i=0}^{q-1}\frac{m+2+i}{m-i}.
\]
Since \(c_q=\lfloor\lambda_q\rfloor\ge\lambda_q/2\),
\[
\frac1{c_q}\le\frac2{\lambda_q}.
\]
The Gaussian estimate gives
\[
\sum_{q=1}^{m-1}\frac1{c_q}
\le\sqrt{2\pi m}.
\tag{3.1}
\]

The sharper asymptotic in both additions is also correct:
\[
\boxed{
\sum_{q=1}^{m-1}\frac1{c_q}
=(I+o(1))\sqrt m,\qquad
I=\int_0^\infty
\frac{dx}{\lfloor e^{x^2}\rfloor}.}
\tag{3.2}
\]
Indeed, for \(q=x\sqrt m+O(1)\),
\(\lambda_q\to e^{x^2}\); the finitely many floor discontinuities on compact
intervals are harmless and (3.1) controls the tail.

### 3.2 Exceptional-family charge

Let one exact factor split as
\[
F=G\sqcup B,\qquad b=|B|.
\]
At every controlled depth, suppose a balanced full-mass quota vector
\(b_q\) satisfies
\[
\mu_q^G(S)\le b_q(S)
\qquad\text{for every target }S.
\tag{3.3}
\]
The same \(F,G,B\) must be used at every depth in the window.

Each exceptional wreath supplies \(n\) distinct depth-\(q\) intervals, so
\[
\sum_S\mu_q^B(S)=nb.
\]
Since \(b_q-\mu_q^G\) is nonnegative and also has total mass \(nb\),
\[
\boxed{O_q(F)\le nb.}
\tag{3.4}
\]
There is no missing factor two: \(O_q\) is the minimum positive discrepancy,
equivalently the minimum half-\(\ell^1\) distance, from a balanced full-mass
quota.

Combining (3.1) and (3.4) gives exactly
\[
\boxed{
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le nb\sqrt{2\pi m}.}
\tag{3.5}
\]

Because \(W=n\operatorname{Cat}_m\),
\[
b=o(\operatorname{Cat}_m/\sqrt m)
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}=o(W),
\tag{3.6}
\]
and
\[
b=O(\operatorname{Cat}_m/m)
\quad\Longrightarrow\quad
\sum_{q\le H}\frac{O_q(F)}{c_q}=O(W/\sqrt m).
\tag{3.7}
\]
All constants and normalizations in item 1398 and Section 5.5 check.

### 3.3 Required MWB quantifier

The phrase “\(|B|=o(\operatorname{Cat}_m/\sqrt m)\) suffices for MWB” must
retain one of these quantifier patterns:

* for every fixed \(A\), one common \(F_m,G_m,B_m\) satisfies (3.3)
  simultaneously for all \(q\le\lceil A\sqrt m\rceil\), followed by the
  standard diagonalization; or
* one common construction works through
  \(H(m)=\sqrt m\,\omega(m)\), where \(\omega(m)\to\infty\) and \(H=o(m)\).

A construction for one fixed \(A\), a different core at each depth, or a
small exceptional set without (3.3) does not prove MWB. The quota vectors
themselves may vary with \(q\), because the conclusion is unlabelled
overload.

### 3.4 Star matching and codegrees

For a fixed coordinate \(v\), every wreath contains
\[
m\text{ middle sets through }v,\qquad
m+1\text{ middle sets avoiding }v.
\]
Thus a matching in the **full** wreath-support hypergraph that saturates
\(P_v\) has
\[
\frac{|P_v|}{m}=\operatorname{Cat}_m
\]
edges and covers all \(W\) middle sets. Hence
\[
\boxed{
\text{full wreath matching saturating }P_v
\iff\text{perfect exact factor}.}
\tag{3.8}
\]
“Full” is essential: a matching of projected \(P_v\)-traces may collide on
the complementary \(Q_v\) side.

In the unoriented-support convention,
\[
D_m=\frac{m!(m+1)!}{2}.
\]
For distinct middle sets at Johnson distance \(d\),
\[
\frac{\operatorname{codeg}(A,B)}{D_m}
=\frac{2}{\binom md\binom{m+1}d}.
\tag{3.9}
\]
For distinct \(A,B\in P_v\), \(1\le d\le m-1\), and the maximum is
\[
\boxed{\frac{2}{m(m+1)}.}
\tag{3.10}
\]
The projected \(P_v\)-trace is naturally two-fold; simplifying it halves
both degrees and codegrees and preserves (3.10).

These facts do not prove the antecedent. The full hypergraph has normalized
codegree \(2/(m+1)\), shallow nested quota resources already have correlation
\(2/m\), and a natural \(H\)-depth resource edge has \(n(H+1)\) incidences.
Uniform fractional weights also violate floor capacities whenever
\(W/N_q\notin\mathbb Z\). Thus the additions correctly leave all of the
following unproved:

* the quantitative leave;
* simultaneous hard quotas;
* full \(P_v/Q_v\) disjointness;
* exact wreath-factorability of the residual.

## 4. Global component-noise minimizer

### 4.1 Floor energy

Write
\[
a_q=\frac{W}{N_q}=c_q+\theta_q,\qquad
f_q=\mu_q-a_q\mathbf1,
\]
\[
V_q(F)=\|f_q\|_2^2,\qquad
V_q^{\min}=N_q\theta_q(1-\theta_q).
\]
Then
\[
\boxed{
V_q(F)-V_q^{\min}
=\sum_S(\mu_q(S)-c_q)(\mu_q(S)-c_q-1)
\ge2O_q(F).}
\tag{4.1}
\]
The factor two is correct.

Define
\[
\Phi_H(F)=
\sum_{q\le H}\frac{V_q(F)-V_q^{\min}}{c_q},
\qquad
B_H=\sum_{q\le H}\frac{V_q^{\min}}{c_q}.
\tag{4.2}
\]
The selected factor \(F=F_{m,H}\) must globally minimize this same
\(H\)-window objective over the finite exact-factor space.

### 4.2 Exact definition of \(R_H\)

For an unordered coordinate transposition \(\tau\), let
\(\mathcal C_\tau(F)\) be the ownership components and let \(u_{q,C}\) and
\(w_{q,C}\) be the two complete-side histograms. With unnormalized counting
\(\ell_2\)-norms, define
\[
\boxed{
R_H(F)=
\sum_{\tau\in\binom{[n]}2}
\sum_{C\in\mathcal C_\tau(F)}
\sum_{q\le H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.}
\tag{4.3}
\]

This normalization is the one used by all subsequent constants. In the fair
Rademacher side choice, the literal variance contribution is
\(\frac14\|u_{q,C}-w_{q,C}\|_2^2\). Thus \(R_H\) is an unscaled noise sum,
not the variance itself.

Every complete-side choice is an integral exact factor. Global minimality
therefore implies, for every \(\tau\),
\[
\sum_{q\le H}\frac{\|\mu_q-\tau\mu_q\|_2^2}{c_q}
\le
\sum_C\sum_{q\le H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q}.
\tag{4.4}
\]

For later use, put
\[
D_H(F)=
\sum_{\tau\in\binom{[n]}2}
\sum_{q\le H}
\frac{\|\mu_q(F)-\tau\mu_q(F)\|_2^2}{c_q}.
\tag{4.4a}
\]

### 4.3 Point margins and the spectral constant

An exact-factor histogram does **not** have zero point margins. It has the
fixed margins
\[
\sum_{S\ni x}\mu_q(S)=\frac{(m-q)W}{n}.
\tag{4.5}
\]
The constant profile \(a_q\mathbf1\) has the same margins. Consequently the
centered vector \(f_q\) has zero total and zero point margins and lies in
Johnson degrees \(j\ge2\).

When the sum is over the \(\binom n2\) unordered transpositions once and the
norm is the unnormalized counting norm,
\[
\boxed{
\sum_\tau\|f_q-\tau f_q\|_2^2
\ge4(n-1)\|f_q\|_2^2.}
\tag{4.6}
\]
The coefficient follows from twice the Johnson Laplacian eigenvalue
\(\lambda_2=2(n-1)\). Ordered transpositions would double it.

Thus the constant \(4(n-1)\) in both additions is correct after replacing
the erroneous “histograms have zero point margins” sentence in item 1399 by
“centered histograms have zero point margins.”

### 4.4 Correct minimizer inequality

Summing (4.4) over all transpositions and using (4.6) gives
\[
R_H(F)\ge
4(n-1)\bigl(B_H+\Phi_H(F)\bigr).
\tag{4.7}
\]
By (4.1),
\[
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le\frac12\Phi_H(F).
\]
Therefore
\[
\boxed{
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le
\frac{R_H(F)}{8(n-1)}-\frac12B_H.}
\tag{4.8}
\]
Every factor and sign in Section 5.6 and item 1399 checks under definition
(4.3).

The repaired unproved criterion is
\[
\boxed{
R_H(F)\le4(n-1)B_H+o(nW).}
\tag{4.9}
\]
It gives fixed-window overload \(o(W)\) because (4.8) divides the error by
\(8(n-1)\).

To imply MWB, (4.9) must hold for a global minimizer \(F_{m,A}\) of the same
\(H_A=\lceil A\sqrt m\rceil\) objective for every fixed \(A\), followed by
diagonalization. A bound at an arbitrary factor, at a minimizer of a
different window, or for only one fixed \(A\) is insufficient.

### 4.5 Baseline and implication scope

The former \(2nB_H\) baseline is below the forced floor:
\[
R_H(F)\ge4(n-1)B_H.
\]
The gap is
\[
\bigl(4(n-1)-2n\bigr)B_H=2(n-2)B_H.
\]
On every nontrivial fixed Gaussian window,
\[
B_H=\Theta_A(W\sqrt m),
\]
so an \(o(nW)\) error cannot absorb the gap. The raw \(2nB_H+o(nW)\)
criterion is therefore asymptotically infeasible there.

At the selected global minimizer,
\[
\begin{aligned}
R_H-4(n-1)B_H
={}&(R_H-D_H)\\
&+\bigl(D_H-4(n-1)(B_H+\Phi_H)\bigr)\\
&+4(n-1)\Phi_H,
\end{aligned}
\tag{4.10}
\]
and all three terms are nonnegative. Hence (4.9) is equivalent there to
\[
\Phi_H=o(W),
\]
\[
R_H-D_H=o(nW),
\]
and
\[
D_H-4(n-1)(B_H+\Phi_H)=o(nW).
\]
These are respectively low floor energy, negligible aggregate fair-switch
drift, and negligible spectral excess above Johnson degree two.

This makes (4.9) formally stronger than merely asserting a low global
minimum, but no strict separation has been constructed inside the exact
factor fibre. It is a minimizer-only sufficient gate, not an equivalent
form of RFEN, LM\(_A\), SCOV\(_A\), or MWB. No implication in either
direction with those earlier gates is proved.

The marker-degree statement in item 1399 is also correctly repaired:
one-marker/middle double counting permits equal average degrees. The real
obstruction is that marker-only completion edges are not physical wreaths.

## 5. Required textual corrections

The additions should be retained with these edits:

1. After the exceptional-size conclusions in item 1398 and Section 5.5, add:
   “This implies MWB only with one common split and quota domination on every
   fixed Gaussian window (or one admissible growing window).”
2. In item 1399, replace “Exact factor histograms have zero point margins”
   by “The centered exact-factor histograms have zero point margins.”
3. In Section 5.6, replace “sum the complete-side component variance ... and
   call it \(R_H\)” by the exact formula (4.3), or say “sum four times the
   fair complete-side variance.”
4. State that all transpositions in the \(4(n-1)\) inequality are unordered
   and counted once, and all norms are unnormalized counting norms.
5. State the fixed-window quantifier for (4.9): for every fixed \(A\), use a
   global minimizer of that same \(H_A\)-window objective.
6. If “strictly stronger than a low minimizer” is retained, qualify it as a
   formal three-term near-equality requirement; no strict exact-factor
   separation is known.

## 6. Final classification

* Reciprocal quota constant \(I\): **accepted**.
* Bound \(n|B|\sqrt{2\pi m}\): **accepted**.
* Thresholds \(o(\operatorname{Cat}_m/\sqrt m)\) and
  \(O(\operatorname{Cat}_m/m)\): **accepted with common-window quotas**.
* Star-saturation/perfect-factor equivalence: **accepted only in the full
  hypergraph**.
* Star codegree \(2/[m(m+1)]\): **accepted as a projected fact only**.
* Floor identity and \(2O_q\) bound: **accepted**.
* Spectral coefficient \(4(n-1)\): **accepted for centered histograms,
  unordered transpositions, and counting norms**.
* Correct minimizer overload bound: **accepted**.
* Baseline \(4(n-1)B_H\): **accepted**.
* Criterion \(R_H\le4(n-1)B_H+o(nW)\): **accepted as an unproved
  fixed-window sufficient gate**.
* Comparisons with RFEN, LM\(_A\), and SCOV\(_A\): **no implication either
  way is proved**.

No coefficient-one or MWB theorem is added unconditionally.
