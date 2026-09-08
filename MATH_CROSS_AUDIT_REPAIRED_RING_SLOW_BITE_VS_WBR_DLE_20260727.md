# Cross-audit of the repaired-ring slow bite against weighted RPRN and WBR+

Date: 2026-07-27

Scope: coefficient-one owner packing only.

## 0. Verdict

The owner near-packing in
MATH_THEOREM_REPAIRED_RING_GROWING_UNIFORMITY_SLOW_BITE_TRAJECTORY_20260726.md
is not proved unconditionally.

The choices

\[
 L=\Theta((\log m)^2),\qquad J=\Theta(\log m)
\]

have enough numerical room. They do not close the generator hierarchy.
Even granting every static path-mesh estimate in Sections 3--4 of that
note, the generator of a monitored pure power contains mixed
repeated-next-edge moments and common-next-edge column correlations
which are not among the static observables.

The corrected WBR+ statement is in
MATH_THEOREM_FINITE_DENSITY_WASTEFUL_REPAIRED_RING_NIBBLE_20260726.md,
Sections 6--7. It does not fill this gap: it assumes cumulative
near-regularity and bridge regeneration, is quantified for each fixed
\(z>0\), and concerns a compensated wasteful trajectory. The slow-bite
note uses an uncompensated continuous random-greedy trajectory and
\(z=m^{-1/20}\).

The precise missing statement is the aggregate dynamic diagonal
link-energy system ADLE+ACLE in Section 4 below, uniformly down to
\(z=m^{-1/20}\), together with its first-moment drift and root analogue.
This is the aggregate form of DLE (4.1)/(4.3) in
MATH_THEOREM_WEIGHTED_RPRN_AND_DIAGONAL_LINK_ENERGY_GATE_20260726.md.

Conditional on ADLE+ACLE and a noncascading weighted quarantine, the
checkpoint errors and final owner ledger close. Without ADLE, the
current proof supplies no unconditional \(o(N)\)-root leave.

## 1. Hypotheses and exact owner ledger

Two hypotheses must be explicit. Let \(H\) be the least integer such
that

\[
 {\binom{2m}{m}\over\binom{2m}{m-H}}\ge m+H,
\tag{1.1}
\]

and delete a nonempty block

\[
                         1\le\kappa=o(m)
\tag{1.2}
\]

of consecutive phases. Put

\[
 M=m+H,\quad r=M-\kappa,\quad K=r+1,\quad
 N=\binom{2m}{m-H},\quad W=\binom{2m}{m}.
\tag{1.3}
\]

The minimality in (1.1), not merely
\(H=(1+o(1))\sqrt{m\log m}\), gives

\[
 W-rN=O((H+\kappa)N)=o(W).
\tag{1.4}
\]

If a rooted matching misses \(s\) roots, its exact owner leave is

\[
                         W-rN+rs.
\tag{1.5}
\]

Since \(rN=(1-o(1))W\), (1.5) is \(o(W)\) exactly when
\(s=o(N)\). This ledger in the slow-bite note is correct.

## 2. The numerical buffer arithmetic

Put

\[
\begin{aligned}
 z&=m^{-1/20},& T&={K\over20}\log m,\\
 E&=\lceil2\log m\rceil,& \tau&={K\over40},\\
 L&=\lceil100(\log m)^2\rceil,& J&=\lceil20\log m\rceil.
\end{aligned}
\tag{2.1}
\]

Then \(E\tau\ge T\), and

\[
 L-EJ\ge50(\log m)^2
\tag{2.2}
\]

for all sufficiently large \(m\).

The slow-bite note uses

\[
 \varepsilon_*={CL^4\over m^2z^2}.
\tag{2.3}
\]

Its own generator-error formula (4.5), however, contains the explicit
factor \(L^2\varepsilon_L\). A safe common parameter is therefore

\[
 \boxed{\bar\varepsilon_*={CL^6\over m^2z^2}.}
\tag{2.4}
\]

This correction is harmless numerically:

\[
 T\bar\varepsilon_*
 =O(m^{-9/10}\log^{13}m)=o(1).
\tag{2.5}
\]

Let

\[
 \eta=m^{-1/10},\qquad \eta_0={\eta\over10E}.
\tag{2.6}
\]

Then

\[
 {\eta_0^2\over T\bar\varepsilon_*}
 =\Omega\left({m^{7/10}\over\log^{15}m}\right),
\tag{2.7}
\]

and, for every fixed \(c>0\),

\[
 \left({CT\bar\varepsilon_*\over\eta_0}\right)^{cJ}
 =\exp[-\Omega((\log m)^2)].
\tag{2.8}
\]

Thus neither accumulated variance nor buffer size is the obstruction.
The checkpoint implication also needs margin: allow error \(i\eta_0\)
at checkpoint \(i\) and \((i+1)\eta_0\) at the next. The final error is
\(O(E\eta_0)=O(\eta)=o(1)\), and (2.7)--(2.8) are unchanged.

## 3. Why the static hierarchy does not regenerate

Fix a live protected cluster \(C\). Write \(A_C(t)\) for its current
number of path options and, for a next active edge \(g\) disjoint from
the protected resources, let

\[
 B_C(g)=
 |\{f\text{ counted by }A_C:f\cap g\ne\varnothing\}|.
\tag{3.1}
\]

Binomial inversion resolves multiple owner intersections inside
\(B_C(g)\), but it does not make powers linear.

For a cluster class \(\mathcal C\) with natural nonnegative weights
\(w_C\), put

\[
                         F_h=\sum_{C\in\mathcal C}w_CA_C^h.
\tag{3.2}
\]

Freeze every cluster observable at the first event deleting its center
or a protected resource. Thus a protected-resource death creates no
jump in the stopped observable. The uncompensated continuous process
then gives the exact stopped generator

\[
 \mathcal L F_h
 ={1\over K\mathcal D_R}
 \sum_{C,g}w_C
 \sum_{\ell=1}^h(-1)^\ell\binom h\ell
 A_C^{h-\ell}B_C(g)^\ell,
\tag{3.3}
\]

Thus the nonlinear terms are

\[
 \sum_Cw_CA_C^{h-\ell}\sum_g^*B_C(g)^\ell.
\tag{3.4}
\]

They are not the pure row powers recorded in (3.11)--(3.13) of the
slow-bite note: the new edge \(g\) is attached to only \(\ell\) of the
\(h\) replicas.

The carré du champ of \(F_h\) also contains

\[
 {1\over K\mathcal D_R}
 \sum_g\left(\sum_Cw_CA_C^{h-1}B_C(g)\right)^2.
\tag{3.5}
\]

This includes \(C\ne C'\) clusters coupled by the same next edge. The
spanning-forest paragraph asserts a bound for (3.5), but gives neither
a reverse map nor a multiplicity estimate relative to the depleted
current values \(A_C,A_{C'}\).

The time-zero inequalities (3.11)--(3.12) are absolute catalogue
bounds. Replacing \(D,D_X\) by current reference values and inserting
powers of \(u^{-1}\) is the dynamic assertion to be proved, not a
consequence of fresh exponential clocks. Over one checkpoint
\(\tau=\Theta(m)\), current link scales can change by
\(\exp[-\Theta(m)]\).

The stopping rule watches only orders at most \(L_i-J\). The input strip

\[
 L_i-J<\operatorname{ord}\le L_i
\tag{3.6}
\]

is not stopped. A time-simplex factor controls influence crossing a
buffer only after an operator bound at every intermediate level and a
terminal envelope at the moving top are proved. Entrance-time static
moments provide neither. Hence the displayed tail
\((CT\varepsilon_*/\eta)^J\) is asserted, not derived.

## 4. The exact missing inequality

Put

\[
                         \alpha_t={CL^4\over m^2u_t^2}.
\tag{4.1}
\]

Uniformly for every monitored moving-core cluster class, every
\(2\le\ell\le h\le J\), and every time with \(u_t\ge z\), the needed
aggregate diagonal link-energy inequality is

\[
\boxed{
 \sum_Cw_CA_C^{h-\ell}\sum_g^*B_C(g)^\ell
 \le
 (1+o(1))K\mathcal D_R(t)\alpha_t^{\ell-1}
 \sum_Cw_CA_C^h.
}
\tag{ADLE}
\]

For the same class put

\[
 Z_h(g)=\sum_Cw_CA_C^{h-1}B_C(g),\qquad
 F_h=\sum_Cw_CA_C^h,\qquad
 \Lambda_t=K\mathcal D_R(t).
\tag{4.2a}
\]

The large-jump truncation additionally requires the common-next-edge
column moment

\[
\boxed{
 \sum_g^* Z_h(g)^J
 \le(1+o(1))\Lambda_t\alpha_t^{J-1}F_h^J
 \qquad(1\le h\le J).
}
\tag{ACLE}
\]

At the checkpoints, the exceptional centered owners must satisfy the
cumulative weighted condition

\[
 \sum_{i=0}^{E}
 {\,\sum_{X\in\mathcal B_{t_i}}d_{t_i}(X)\over E_{t_i}}
 =o(1),
\tag{4.2}
\]

and the root analogue is required. The \(\ell=1\) term is replaced by
the corresponding two-sided first-moment drift identity.

For the compensated WBR+ trajectory one must add to the left side of
(ADLE) the compensation diagonal

\[
 \sum_Cw_CA_C^{h-\ell}
 \sum_y\chi_t(y)P_C(y)^\ell
\tag{4.3}
\]

with that process's rate normalization. This term is absent from the
original uncompensated slow bite. Consequently WBR+ and the slow bite
are not the same theorem.

The pointwise high-diagonal DLE

\[
 \sum_g^*B_C(g)^J
 \le(1+o(1))\Lambda_tA_C^J\alpha_t^{J-1}
\tag{4.4}
\]

outside weighted exceptional incidence, together with the first-moment
bound, is stronger than ADLE+ACLE but sufficient. Indeed, power-sum
interpolation gives

\[
 \sum_g^*B_C(g)^\ell
 \le(1+o(1))\Lambda_tA_C^\ell\alpha_t^{\ell-1}
 \qquad(1\le\ell\le J).
\tag{4.4a}
\]

Moreover, with \(p_C=w_CA_C^h/F_h\), Jensen gives

\[
\begin{aligned}
 {1\over F_h^J}\sum_gZ_h(g)^J
 &=
 \sum_g\left(
   \sum_Cp_C{B_C(g)\over A_C}
 \right)^J\\
 &\le
 \sum_Cp_C{1\over A_C^J}\sum_gB_C(g)^J
 \le(1+o(1))\Lambda_t\alpha_t^{J-1},
\end{aligned}
\tag{4.4b}
\]

where terms with \(A_C=0\) are defined as zero. This proves ACLE from
the pointwise high diagonal.

### Lemma 4.1 (endpoint interpolation)

Fix \(h\ge2\), and put

\[
 S_p(C)=\sum_g^*B_C(g)^p,\qquad
 \Lambda=K\mathcal D_R(t).
\]

Suppose

\[
 S_1(C)\le(1+\delta)\Lambda A_C
\tag{4.5}
\]

for every \(C\), and

\[
 \sum_Cw_CS_h(C)
 \le(1+\delta)\Lambda\alpha^{h-1}\sum_Cw_CA_C^h.
\tag{4.6}
\]

Then, for every \(1\le\ell\le h\),

\[
 \sum_Cw_CA_C^{h-\ell}S_\ell(C)
 \le(1+O(\delta))\Lambda\alpha^{\ell-1}
       \sum_Cw_CA_C^h.
\tag{4.7}
\]

#### Proof

Let \(\theta=(\ell-1)/(h-1)\). Log-convexity gives

\[
 S_\ell(C)\le S_1(C)^{1-\theta}S_h(C)^\theta.
\tag{4.8}
\]

Using (4.5), the exponent of \(A_C\) in
\(A_C^{h-\ell}S_1(C)^{1-\theta}\) is

\[
 h-\ell+1-\theta=h(1-\theta).
\]

Hölder's inequality over \(C\), followed by (4.6), gives

\[
\begin{aligned}
 \sum_Cw_CA_C^{h-\ell}S_\ell(C)
 &\le(1+\delta)^{1-\theta}\Lambda^{1-\theta}
 \left(\sum_Cw_CA_C^h\right)^{1-\theta}
 \left(\sum_Cw_CS_h(C)\right)^\theta\\
 &\le(1+O(\delta))\Lambda\alpha^{\theta(h-1)}
 \sum_Cw_CA_C^h.
\end{aligned}
\]

Since \(\theta(h-1)=\ell-1\), this is (4.7). \(\square\)

Lemma 4.1 repairs the mixed-power algebra once the dynamic high-diagonal
endpoint (4.6) is known. It does not prove (4.6) in an endogenous
residual.

The \(\ell=2\) case of (ADLE) controls the leading carré-du-champ term.
Indeed, the absolute jump of \(F_h\) is at most

\[
 hZ_h(g),
\tag{4.8a}
\]

because \(A^h-(A-B)^h\le hA^{h-1}B\). For each \(g\), weighted
Cauchy--Schwarz gives

\[
 \left(\sum_Cw_CA_C^{h-1}B_C(g)\right)^2
 \le
 \left(\sum_Cw_CA_C^h\right)
 \left(\sum_Cw_CA_C^{h-2}B_C(g)^2\right).
\tag{4.9}
\]

Summing over \(g\) and applying (ADLE) proves normalized
quadratic-variation rate at most \(h^2\alpha_t\). The factor \(h^2\) is
absorbed by the safe \(L^6\) parameter (2.4). ACLE supplies the
\(J\)-th column moment needed for large-jump truncation. Thus
ADLE+ACLE is the missing generator system, not a cosmetic strengthening.

## 5. Conditional cumulative drift and leave

Assume ADLE+ACLE, their first-moment and root analogues, and a weighted online
quarantine which does not create an uncontrolled suppression cascade.
Use the widening checkpoint barriers from (2.6).

Equations (2.5)--(2.8) then give total normalized martingale variation
\(o(1)\), failure mass

\[
                         \exp[-\Omega((\log m)^2)],
\tag{5.1}
\]

and final relative degree error \(O(\eta)=o(1)\). The integrated
trajectory error is

\[
 {T\eta\over K}=O(m^{-1/10}\log m)=o(1).
\tag{5.2}
\]

Consequently

\[
 x(T)=\exp(-T/K+o(1))+o(1)
     =m^{-1/20}+o(1)=o(1).
\tag{5.3}
\]

The selected edges are sequential and hence form an integral matching.
Writing \(s=(z+o(1))N\) for the missed roots, (1.5) gives

\[
\begin{aligned}
 W-r(N-s)
 &=W-rN+rs\\
 &=O\left(
 \left({H+\kappa\over m}+m^{-1/20}\right)W
 \right)
 =o(W).
\end{aligned}
\tag{5.4}
\]

This proves that all scalar parameters and cumulative-drift estimates
are compatible with coefficient one once ADLE+ACLE is supplied. It does
not prove that system.

## 6. Precise boundary

Unconditionally verified in this audit:

1. the exact owner leave identity (1.5);
2. the logarithmic buffer and variance arithmetic (2.2)--(2.8);
3. the endpoint interpolation Lemma 4.1;
4. the weighted Cauchy reduction (4.9); and
5. the conditional integration and owner ledger (5.2)--(5.4).

Not proved:

1. aggregate dynamic DLE and column energy (ADLE+ACLE) down to
   \(z=m^{-1/20}\);
2. a terminal envelope for the moving top strip (3.6);
3. a noncascading weighted quarantine for the continuous trajectory; or
4. the unconditional owner near-packing.

The smallest exact missing generator statement is ADLE+ACLE, with
(4.2), its first-moment drift, and the root analogue understood. A
stronger single endpoint inequality is the pointwise high-diagonal
bound (4.4), since (4.4a)--(4.4b) then recover both parts. The
\(L=\Theta((\log m)^2)\), \(J=\Theta(\log m)\) choice is quantitatively
adequate conditional on that inequality; it does not generate it.
