# Lane C/L: growing harmonics amplify the all-transposition giant-shield obstruction

Date: 2026-07-25

Method: pure mathematics only.  No search, computation, solver, or
probabilistic experiment is used.

## 0. Verdict

Put

\[
n=2m+1,\qquad W=\binom nm,\qquad
t=\operatorname{Cat}_m=\frac Wn,\qquad
H=\lceil A\sqrt m\rceil,
\]

where \(A>0\) is fixed.  At depth \(q\), put

\[
r_q=m-q,\qquad N_q=\binom n{r_q},\qquad
c_q=\left\lfloor\frac W{N_q}\right\rfloor,
\]

and write

\[
f_q=\mu_q-\frac W{N_q}\mathbf1.
\]

Fix a constant

\[
0<\gamma<\log4
\]

and define

\[
J=J_{m,\gamma}
=\left\lfloor\frac{\gamma H}{\log(108m)}\right\rfloor,
\qquad
\Lambda=(J+1)(n-J).
\tag{0.1}
\]

For every exact factor \(F\), split its centered squared mass into

\[
\mathcal L_J(F)
=\sum_{q\le H}\sum_{2\le j\le J}
  \frac{\|P_{E_j}f_q\|_2^2}{c_q},
\tag{0.2}
\]

\[
\mathcal H_J(F)
=\sum_{q\le H}\sum_{j>J}
  \frac{\|P_{E_j}f_q\|_2^2}{c_q}.
\tag{0.3}
\]

The first theorem below proves the uniform exact-factor bound

\[
\boxed{
\mathcal L_J(F)
\le U_{m,\gamma}:=
\frac{tH^3}{n}e^{\gamma H}.}
\tag{0.4}
\]

For a transposition \(\tau\), let \(s_\tau(F)\) be the largest number of
old-side rows in one freshly recomputed ownership component, and put

\[
k_s(F)=\#\{\tau:s_\tau(F)>s\}.
\tag{0.5}
\]

For a row \(C\), let \(w_{C,q}\) be the indicator of its cyclic
rank-\(r_q\) intervals, and define the full row-displacement capacity

\[
\mathscr R_{\tau,H}(F)
=\sum_{q\le H}\frac1{c_q}
 \sum_{C\in F}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{0.5a}
\]

Let \(V_\tau^{>J}\) be the high-sector component variance defined in
(2.3), and put

\[
k_s^{\rm eff}(F)
=\#\{\tau:V_\tau^{>J}>s\mathscr R_{\tau,H}(F)\}.
\tag{0.5b}
\]

This counts genuinely high-harmonic **active** shields.  Cauchy--Schwarz
inside each ownership component gives

\[
\boxed{k_s(F)\ge k_s^{\rm eff}(F),}
\tag{0.5c}
\]

because \(s_\tau(F)\le s\) implies
\(V_\tau^{>J}\le s\mathscr R_{\tau,H}(F)\).

Let

\[
D_{m,H}
=\sum_{q\le H}
\frac{(m-q)(m+q+1)-2}{c_q},
\qquad
T_n=\binom n2.
\tag{0.6}
\]

The growing-harmonic shield theorem is the exact implication

\[
\boxed{
k_s(F)\ge k_s^{\rm eff}(F)\ge
\left\lceil
\frac{\Lambda}{2}
-\frac{sWD_{m,H}}{2\mathcal H_J(F)}
-\frac{T_nU_{m,\gamma}}{\mathcal H_J(F)}
\right\rceil}
\tag{0.7}
\]

for every all-transposition component-cut local minimum with
\(\mathcal H_J(F)>0\), and every integer \(s\ge0\).

This strengthens the earlier degree-two C obstruction.  Let
\(\mathscr X_m\) be the full intrinsic \((2\ 3)\)-cell of the canonical
MSW factor.  Put

\[
M_A=\left\lceil e^{2(A+1)(A+2)}\right\rceil,
\qquad
E_m^*=\frac{t4^H}{2048M_AH^4},
\tag{0.8}
\]

and

\[
s_m^*=\left\lfloor
\frac{\Lambda E_m^*}{4WD_{m,H}}
\right\rfloor.
\tag{0.9}
\]

If a corner \(F\in\mathscr X_m\) were locally minimal for every
transposition, then

\[
\boxed{
k_{s_m^*}(F)\ge k_{s_m^*}^{\rm eff}(F)
\ge
\left\lceil
\frac{3\Lambda}{8}-\delta_m
\right\rceil,
\qquad
\delta_m:=\frac{T_nU_{m,\gamma}}{E_m^*}=o_{A,\gamma}(1).}
\tag{0.10}
\]

With

\[
I_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor},
\tag{0.11}
\]

the exact floor-sensitive asymptotics are

\[
\boxed{
s_m^*\sim
\frac{\gamma4^H}
{8192M_AI_AH^3m^{5/2}\log(108m)}
=\exp\bigl((A\log4+o_{A,\gamma}(1))\sqrt m\bigr),}
\tag{0.12}
\]

and

\[
\boxed{
k_{s_m^*}(F)
\ge
\left(\frac{3\gamma A}{4}+o_{A,\gamma}(1)\right)
\frac{m^{3/2}}{\log(108m)}.}
\tag{0.13}
\]

The complete native MSW matching has only \(m-1\) colours.  Hence all but
an \(o(1)\)-fraction of the active colours forced by (0.13) are nonnative.

Thus the merely linear giant-shield configuration left open by the first C
report is rigorously insufficient.  A genuine all-transposition AB7 lock
would require superlinearly many distinct nonnative overlays whose
high-harmonic component variance exceeds \(s_m^*\) times their entire
row-displacement capacity.  Each therefore contains a superpolynomial
component.  This still does not rule out that configuration: connected
overlays can be reused across colours, and no exact chronology theorem presently
bounds that reuse.  No all-transposition counterexample and no constant-one
conclusion is claimed.

## 1. Uniform growing-degree truncation

The exact run-cap envelope gives, for every exact factor, every \(q\le H\),
and every \(2\le j\le J\),

\[
\|P_{E_j}f_q\|_2^2
\le
\frac{\binom njq^2t^2}{4\alpha_{q,j}},
\qquad
\alpha_{q,j}=\binom{n-2j}{m-q-j}.
\tag{1.1}
\]

Since \(W/N_q>1\),

\[
c_q\ge\frac{W}{2N_q}.
\tag{1.2}
\]

Moreover,

\[
\frac{N_q}{\alpha_{q,j}}
=\frac{(n)_{2j}}{(m-q)_j(m+q+1)_j}.
\tag{1.3}
\]

For fixed \(A,\gamma\), eventually \(q,j\le m/4\).  Every numerator
factor in (1.3) is at most \(3m\), every denominator factor is at least
\(m/2\), and \(\binom nj\le(3m)^j\).  Therefore

\[
\frac{N_q}{\alpha_{q,j}}\le36^j
\]

and, using \(W=nt\),

\[
\frac1{c_q}\|P_{E_j}f_q\|_2^2
\le\frac{q^2t}{2n}(108m)^j.
\tag{1.4}
\]

Now

\[
\sum_{q\le H}q^2\le H^3,
\qquad
\sum_{j=2}^J(108m)^j\le2(108m)^J,
\]

and the definition of \(J\) gives

\[
(108m)^J\le e^{\gamma H}.
\]

Summing (1.4) proves (0.4).  This is uniform over every exact factor and
therefore over every corner of every genuine transposition cell.

## 2. High-harmonic cell quantities

Fix a transposition \(\tau\).  Let \(K\) range over the genuine ownership
components of \(F\) versus \(\tau F\), and let

\[
d_{K,q}=\mu_q(K)-\mu_q(\tau K).
\tag{2.1}
\]

Johnson projections commute with every coordinate permutation.  Define

\[
A_{\tau}^{>J}
=\sum_{q\le H}\sum_{j>J}
\frac{\left\|\sum_KP_{E_j}d_{K,q}\right\|_2^2}{c_q},
\tag{2.2}
\]

\[
V_{\tau}^{>J}
=\sum_K\sum_{q\le H}\sum_{j>J}
\frac{\|P_{E_j}d_{K,q}\|_2^2}{c_q}.
\tag{2.3}
\]

Define \(A_\tau^{\le J},V_\tau^{\le J}\) analogously.  Independent fair
component signs give the exact cell-trace identities

\[
\mathbb E_{\rm cell}
[\mathcal H_J(F')-\mathcal H_J(F)]
=\frac14(V_\tau^{>J}-A_\tau^{>J}),
\tag{2.4}
\]

\[
\mathbb E_{\rm cell}
[\mathcal L_J(F')-\mathcal L_J(F)]
=\frac14(V_\tau^{\le J}-A_\tau^{\le J}).
\tag{2.5}
\]

Suppose now that \(F\) minimizes the full floor energy on this entire
\(\tau\)-cell.  The floor is factor-independent, so the fair mean of the
sum in (2.4)--(2.5) is nonnegative.  By (0.4), every exact child has
low-degree mass at most \(U_{m,\gamma}\).  Hence

\[
\frac14(V_\tau^{\le J}-A_\tau^{\le J})
=\mathbb E_{\rm cell}\mathcal L_J(F')-\mathcal L_J(F)
\le U_{m,\gamma}.
\]

It follows that

\[
\boxed{
A_\tau^{>J}\le V_\tau^{>J}+4U_{m,\gamma}.}
\tag{2.6}
\]

This is the only place where all-cut locality is used.  It is robust against
arbitrary cancellation between low and high Johnson degrees.

There is also the unconditional bound

\[
\boxed{A_\tau^{>J}\le4\mathcal H_J(F),}
\tag{2.7}
\]

because the high-degree projection is permutation-invariant and \(\tau\) is
orthogonal.

## 3. Component capacity and the high-degree spectral sum

For a row \(C\), let \(w_{C,q}\) be the indicator of its \(n\) cyclic
rank-\(r_q\) intervals, and put

\[
\mathscr R_{\tau,H}(F)
=\sum_{q\le H}\frac1{c_q}
\sum_{C\in F}\|w_{C,q}-\tau w_{C,q}\|_2^2.
\tag{3.1}
\]

The exact cyclic-row boundary count is

\[
\sum_\tau\mathscr R_{\tau,H}(F)=2WD_{m,H}.
\tag{3.2}
\]

If every \(\tau\)-component has at most \(s\) old-side rows, then
Cauchy--Schwarz, followed by orthogonal projection, gives

\[
V_\tau^{>J}
\le s\mathscr R_{\tau,H}(F).
\tag{3.3}
\]

Consequently, over any family of such transpositions,

\[
\sum_\tau V_\tau^{>J}\le2sWD_{m,H}.
\tag{3.4}
\]

On Johnson degree \(j\), the unnormalized Laplacian eigenvalue is

\[
\lambda_j=j(n-j+1).
\]

Every occurring degree satisfies \(j\le r_q\le m-1\), on which
\(\lambda_j\) is strictly increasing.  Therefore

\[
\begin{aligned}
\sum_\tau A_\tau^{>J}
&=2\sum_{q\le H}\sum_{j>J}
  \frac{j(n-j+1)\|P_{E_j}f_q\|_2^2}{c_q}\\
&\ge2(J+1)(n-J)\mathcal H_J(F)\\
&=2\Lambda\mathcal H_J(F).
\end{aligned}
\tag{3.5}
\]

## 4. Proof of the growing-harmonic shield theorem

Let

\[
\mathcal B_s^{\rm eff}
=\{\tau:V_\tau^{>J}>s\mathscr R_{\tau,H}(F)\},
\qquad |\mathcal B_s^{\rm eff}|=k_s^{\rm eff}(F).
\]

For \(\tau\in\mathcal B_s^{\rm eff}\), use (2.7).  For every remaining
colour, (2.6) and the defining inequality of the complement give

\[
A_\tau^{>J}
\le s\mathscr R_{\tau,H}(F)+4U_{m,\gamma}.
\]

Sum this estimate and use (3.2) and (3.5).  We obtain

\[
\begin{aligned}
2\Lambda\mathcal H_J(F)
&\le\sum_\tau A_\tau^{>J}\\
&\le4k_s^{\rm eff}(F)\mathcal H_J(F)
  +2sWD_{m,H}+4T_nU_{m,\gamma}.
\end{aligned}
\tag{4.1}
\]

Divide by \(4\mathcal H_J(F)>0\), rearrange, and use the integrality of
\(k_s^{\rm eff}(F)\).  This proves the effective bound in (0.7).
Finally, (3.3) shows that a colour with \(s_\tau(F)\le s\) cannot belong
to \(\mathcal B_s^{\rm eff}\), proving (0.5c) and the component-size
bound in (0.7).

## 5. Inserting the genuine AB7 cell floor

Let \(\mathscr X_m\) be the full canonical MSW \((2\ 3)\)-cell.  The
private target-pair theorem, applied to the full floor polynomial at depth
\(H\), gives for every corner \(F\in\mathscr X_m\)

\[
\mathcal Q_A(F)
\ge L_m:=\frac{t4^H}{1024M_AH^4}.
\tag{5.1}
\]

Indeed, there are \(\operatorname{Cat}_{m-H-2}\) distinct target pairs
with total at least \(\operatorname{Cat}_H\); convexity of the integral
floor polynomial gives a contribution at least
\(\operatorname{Cat}_H^2/4\) per pair, and the standard Catalan bounds give
(5.1).  Every object here is a literal exact factor.

The full centered squared mass is

\[
\mathcal L_J(F)+\mathcal H_J(F)
=\mathcal Q_A(F)+\sum_{q\le H}\frac{\beta_q}{c_q}
\ge\mathcal Q_A(F).
\]

By (0.4),

\[
\mathcal H_J(F)\ge L_m-U_{m,\gamma}.
\tag{5.2}
\]

Since \(\gamma<\log4\),

\[
\frac{U_{m,\gamma}}{L_m}
=\frac{1024M_AH^7}{n}
  e^{-(\log4-\gamma)H}
\longrightarrow0.
\tag{5.3}
\]

Thus, for all sufficiently large \(m\),

\[
\boxed{\mathcal H_J(F)\ge E_m^*=L_m/2.}
\tag{5.4}
\]

Apply (0.7) with \(s=s_m^*\).  From (0.9) and (5.4),

\[
\frac{s_m^*WD_{m,H}}{2\mathcal H_J(F)}
\le\frac{\Lambda}{8}.
\tag{5.5}
\]

Also

\[
\delta_m
=\frac{T_nU_{m,\gamma}}{E_m^*}
=\frac{2048M_AT_nH^7}{n}
  e^{-(\log4-\gamma)H}
=o_{A,\gamma}(1).
\tag{5.6}
\]

Substitution into (0.7) proves (0.10).

## 6. Exact asymptotic accounting

For the fixed Gaussian window,

\[
D_{m,H}\sim I_Am^{5/2},
\qquad
I_A=\int_0^A\frac{dx}{\lfloor e^{x^2}\rfloor}.
\tag{6.1}
\]

Moreover,

\[
J\sim\frac{\gamma H}{\log(108m)},
\qquad
\frac{\Lambda}{n}\sim J.
\tag{6.2}
\]

The quantity inside the floor in (0.9) tends to infinity.  Using
\(t/W=1/n\), (0.8), and (6.1)--(6.2),

\[
\begin{aligned}
s_m^*
&\sim
\frac{\Lambda}{4WD_{m,H}}
\frac{t4^H}{2048M_AH^4}\\
&\sim
\frac{\gamma4^H}
{8192M_AI_AH^3m^{5/2}\log(108m)},
\end{aligned}
\]

which is (0.12).  In logarithmic form,

\[
\log s_m^*
=A(\log4)\sqrt m-4\log m-\log\log m+O_{A,\gamma}(1).
\tag{6.3}
\]

Finally,

\[
\Lambda
\sim\frac{\gamma nH}{\log(108m)}
\sim\frac{2\gamma A m^{3/2}}{\log(108m)}.
\tag{6.4}
\]

Equations (0.10), (5.6), and (6.4) give (0.13).  Subtracting the
\(m-1=o(\Lambda)\) native colours proves the nonnative assertion.

## 7. Precise boundary

The theorem rules out every attempted simultaneous AB7 lock in which only
\(O(n)\), or more generally \(o_{A,\gamma}(m^{3/2}/\log m)\),
transposition colours have

\[
V_\tau^{>J}>s_m^*\mathscr R_{\tau,H}(F).
\]

In particular, the same conclusion holds if only that many colours carry
components of size greater than \(s_m^*\).  This is a genuine
same-quantifier obstruction: the hypothesis is local minimality for every
freshly recomputed transposition cell, and all rows and all component cuts
are literal exact wreath-factor objects.

It does not bound the number of colours in which the same owner rows may be
reused.  A connected overlay has one component and is automatically flat,
so the estimate is compatible with a factor having the required
superlinear family of connected nonnative overlays.  No theorem presently
constructs such a high-energy factor, and no exact cyclic-chronology theorem
excludes it.

The next exact statement is therefore an active-row no-recycling theorem:
for a high AB7-cell corner, prove that fewer than
\(\Omega_{A,\gamma}(m^{3/2}/\log m)\) nonnative transpositions can satisfy

\[
V_\tau^{>J}>s_m^*\mathscr R_{\tau,H}(F),
\qquad
s_m^*=\exp((A\log4+o_{A,\gamma}(1))\sqrt m).
\]

A component-size bound \(s_\tau(F)\le s_m^*\) on all but fewer than that
many colours would be a sufficient, stronger exclusion.  Either statement
would contradict (0.10) and close the giant-shield branch.  Conversely,
constructing an all-transposition local corner must explicitly realize this
superlinear active component family.  Neither branch is asserted here.
