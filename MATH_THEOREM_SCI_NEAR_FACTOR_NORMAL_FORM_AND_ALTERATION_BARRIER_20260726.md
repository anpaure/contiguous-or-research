# SCI near-factor normal form and the sparse-alteration barrier

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Verdict

Write

\[
 W=\binom{2m}{m},\qquad N_q=\binom{2m}{m-q},\qquad 1\le H<h<m,
\]

and let \(\mathscr C_{m,h}\) be the catalogue of whole physical
\(C_{2h}\)-strips.  For a family \(\mathcal F\subseteq\mathscr C_{m,h}\),
let \(r_q^\pm(S)\) be its load on a signed depth-\(q\) target, and let
\(r_0(X)\) be its middle load.  Put

\[
 \mathsf A_0(\mathcal F)
 :=\sum_{X\in\binom{[2m]}m}|r_0(X)-1|,
 \tag{0.1}
\]

\[
 \mathsf H_{[1,H]}(\mathcal F)
 :=\sum_{q=1}^H\sum_{\epsilon\in\{-,+\}}
 \#\{S:r_q^\epsilon(S)=0\}.
 \tag{0.2}
\]

Then the owner-recycling SCI gate has the following two-term normal form:

\[
 \boxed{
 \tau_{m,H,h}-\tau^*_{m,H,h}=o(W)
 \iff
 \exists\mathcal F:\quad
 \mathsf A_0(\mathcal F)=o(W),\quad
 \mathsf H_{[1,H]}(\mathcal F)=o(W).}
 \tag{0.3}
\]

Thus owner recycling does not remove the asymptotic middle-factor
requirement.  Every near-optimal SCI family is an approximate exact middle
factor in \(\ell^1\), and the same whole strips cover all but \(o(W)\)
targets in the entire nonmiddle band.  Conversely, these two properties
alone imply SCI; no separate first-shadow repetition estimate or cycle-count
condition is needed.

The exact fractional normalization is independently certified by the dual
vector

\[
 y_m=1,\qquad y_{m-1}=y_{m+1}=\frac{H}{2h},\qquad
 y_{m\pm q}=0\quad(2\le q\le H),
 \tag{0.4}
\]

for which every physical strip column is tight.  It gives

\[
 \tau^*_{m,H,h}=W+\frac HhN_1.
 \tag{0.5}
\]

Finally, independent rounding cannot be repaired sparsely.  At the optimal
fractional density \(1/D_1\), the number of signed depth-one holes is
concentrated at

\[
 \left(\frac2e+o(1)\right)N_1.
 \tag{0.6}
\]

Changing \(d\) whole strips changes this hole count by at most \(4hd\).
Consequently, with probability \(1-o(1)\), every alteration producing
\(o(W)\) depth-one holes must change \(\Omega(W/h)\) strip decisions.  A
successful correlated rounding is therefore a global reorganization, not a
sparse cleanup of an independent or fixed-cardinality sample.

The remaining theorem is exactly the right side of (0.3).  No proof of that
existence statement is supplied here.

## 1. Independent verification of the LP normalization

The SCI primal is

\[
 \min (2h+2H)\sum_Cx_C+\sum_Sz_S
 \tag{1.1}
\]

subject to

\[
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1,
 \qquad x_C,z_S\ge0.
 \tag{1.2}
\]

Its dual has variables \(0\le y_S\le1\) and constraints

\[
 \sum_{S\in\mathcal T_H(C)}y_S\le2h+2H
 \qquad(C\in\mathscr C_{m,h}).
 \tag{1.3}
\]

Every strip contains \(2h\) middle targets and \(2h\) targets in each of
the two signed depth-one layers.  Hence (0.4) gives, for every strip,

\[
 2h+4h\frac{H}{2h}=2h+2H.
 \tag{1.4}
\]

Its dual objective is \(W+(H/h)N_1\).  This is a whole-column certificate,
not merely an aggregate relaxation.

For the matching primal certificate, let \(D_q\) be the catalogue degree of
a signed depth-\(q\) target.  Double counting gives

\[
 D_q=\frac{(m+q)!(m-q)!}{2(m-h)!^2},\qquad
 \frac{D_q}{D_1}=\frac{N_1}{N_q}.
 \tag{1.5}
\]

Put \(x_C=1/D_1\).  Every signed depth-one target has load one, every
deeper signed target has load at least one, and every middle target has
load \(N_1/W\).  Adding middle singleton weight \(1-N_1/W\) gives objective

\[
 (2h+2H)\frac{N_1}{2h}+W-N_1
 =W+\frac HhN_1.
 \tag{1.6}
\]

Thus (0.5) follows by strong duality.

## 2. Exact dual-slack ledger

For a fixed integral family, use a singleton precisely at every uncovered
target.  Define

\[
\begin{aligned}
 L_0&=\#\{X:r_0(X)=0\},
 &R_0&=\sum_X(r_0(X)-1)_+,\\
 L_1^\epsilon&=\#\{S:r_1^\epsilon(S)=0\},
 &R_1^\epsilon&=\sum_S(r_1^\epsilon(S)-1)_+,\\
 L_{\ge2}&=\sum_{q=2}^H\sum_\epsilon
 \#\{S:r_q^\epsilon(S)=0\}.
\end{aligned}
\tag{2.1}
\]

Let

\[
 L_1=L_1^-+L_1^+,
 \qquad R_1=R_1^-+R_1^+,
 \qquad a=\frac{H}{2h}.
 \tag{2.2}
\]

Because every selected strip is tight in (1.4), complementary slackness is
an identity, not an inequality:

\[
 \boxed{
 \tau(\mathcal F)-\tau^*
 =R_0+aR_1+(1-a)L_1+L_{\ge2}.}
 \tag{2.3}
\]

Indeed, an uncovered target contributes \(1-y_S\), while a covered target
of load \(r\) contributes \(y_S(r-1)\).  Substitution of (0.4) gives
(2.3).

## 3. Elimination of the first-shadow repetition term

Let \(k=|\mathcal F|\).  Counting incidences in the middle and in either
signed first-shadow layer gives

\[
 2hk=W-L_0+R_0,
 \tag{3.1}
\]

\[
 2hk=N_1-L_1^\epsilon+R_1^\epsilon.
 \tag{3.2}
\]

These two identities yield both directions needed below.

First, from (3.1) and the nonnegativity of \(L_0\),

\[
 R_1^\epsilon
 =2hk-N_1+L_1^\epsilon
 \le W-N_1+R_0+L_1^\epsilon.
 \tag{3.3}
\]

Since

\[
 W-N_1=\frac{W}{m+1}=o(W),
 \tag{3.4}
\]

we obtain

\[
 R_0=o(W),\quad L_1=o(W)
 \quad\Longrightarrow\quad R_1=o(W).
 \tag{3.5}
\]

Thus the weighted repetition condition \((H/h)R_1=o(W)\) is automatic;
in fact the unweighted repetition mass is already \(o(W)\).

Second, (3.2) and \(R_1^\epsilon\ge0\) imply

\[
 2hk\ge N_1-L_1^\epsilon.
 \tag{3.6}
\]

Substitution in (3.1) gives

\[
 L_0
 \le W-N_1+R_0+L_1^\epsilon.
 \tag{3.7}
\]

Consequently

\[
 R_0=o(W),\quad L_1=o(W)
 \quad\Longrightarrow\quad L_0=o(W).
 \tag{3.8}
\]

In particular,

\[
 \mathsf A_0=L_0+R_0=o(W).
 \tag{3.9}
\]

The same identities also force the cycle count

\[
 2hk=W+o(W),
 \qquad
 k=\frac{W}{2h}+o(W/h).
 \tag{3.10}
\]

This corrects a potentially misleading weaker estimate
\(k=N_1/(2h)+o(W/H)\): multiplying an \(o(W/H)\) error by the strip cost
\(\Theta(h)\) need not be \(o(W)\) when \(h/H\to\infty\).  The middle
incidence identity supplies the coefficient-safe estimate (3.10).

## 4. Proof of the two-term normal form

Suppose first that \(\tau-\tau^*=o(W)\), and take an optimal integral
family.  Every term in (2.3) is nonnegative, while
\(1-a>1/2\).  Hence

\[
 R_0=o(W),\qquad L_1=o(W),\qquad L_{\ge2}=o(W).
 \tag{4.1}
\]

Equation (3.8) gives \(L_0=o(W)\), proving
\(\mathsf A_0=o(W)\).  The last two conditions in (4.1) give
\(\mathsf H_{[1,H]}=o(W)\).

Conversely, suppose the right side of (0.3) holds.  Then
\(R_0=o(W)\), \(L_1=o(W)\), and \(L_{\ge2}=o(W)\).  Equation (3.5) gives
\(R_1=o(W)\).  Substitution in (2.3), using \(0<a<1/2\), gives

\[
 \tau(\mathcal F)-\tau^*=o(W).
 \tag{4.2}
\]

This proves (0.3).

## 5. Concentration of the independent-rounding obstruction

Select each catalogue strip independently with probability

\[
 p=\frac1{D_1}.
 \tag{5.1}
\]

For a fixed signed depth-one target the probability of being uncovered is

\[
 (1-p)^{D_1}=e^{-1}+o(1).
 \tag{5.2}
\]

Therefore

\[
 \mathbb E L_1=(2e^{-1}+o(1))N_1.
 \tag{5.3}
\]

Changing one strip indicator can change \(L_1\) by at most \(4h\).  In the
Efron--Stein resampling inequality the function changes only when the old
and new Bernoulli indicators differ, an event of probability at most
\(2p\).  With \(M=|\mathscr C_{m,h}|\) and
\(Mp=N_1/(2h)\),

\[
 \operatorname {Var}(L_1)
 \le \frac12 M\,2p\,(4h)^2
 =8hN_1.
 \tag{5.4}
\]

Since \(h=o(W)\), Chebyshev's inequality gives

\[
 L_1=\left(\frac2e+o(1)\right)N_1
 \qquad\text{with probability }1-o(1).
 \tag{5.5}
\]

For arbitrary two strip families,

\[
 |L_1(\mathcal F)-L_1(\mathcal F')|
 \le4h\,|\mathcal F\triangle\mathcal F'|,
 \tag{5.6}
\]

because one changed strip affects only its \(4h\) signed depth-one
targets.  Combining (5.5)--(5.6), every alteration with
\(L_1(\mathcal F')=o(W)\) must, with probability \(1-o(1)\), satisfy

\[
 |\mathcal F\triangle\mathcal F'|
 \ge\left(\frac1{2e}+o(1)\right)\frac{W}{h}.
 \tag{5.7}
\]

The same conclusion holds for a uniform sample of the correct cardinality:
sampling without replacement has the same \(e^{-1}+o(1)\) one-target hole
probability, and the random-permutation bounded-difference inequality gives
variance \(O(hW)\).

Thus independent rounding followed by a sparse alteration, local repair, or
an \(o(W/h)\)-support partial-coloring correction cannot prove SCI.  This is
not a no-go for a globally correlated selection changing
\(\Theta(W/h)\) decisions.

## 6. Exact remaining theorem

For

\[
 H=\lceil\sqrt{m\log m}\rceil,
 \qquad h=m^{3/4+o(1)}
\]

with dyadic \(h\), it remains to prove the following single statement:

> There is a family of whole physical \(C_{2h}\)-strips whose middle load
> vector is \(o(W)\) in \(\ell^1\) from the all-ones vector and whose
> aggregate number of uncovered signed targets over all depths
> \(1\le q\le H\) is \(o(W)\).

By (0.3), this statement is equivalent to SCI and therefore implies the
constant-one theorem through the fine strip compiler.  It is not proved by
independent rounding, sparse alteration, separate depthwise choices, the
dependent owner--frame Hall theorem, or the abstract nested-flag flow.

