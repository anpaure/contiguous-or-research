# A global stopped-martingale replacement for roundwise fibre deletion

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The earlier priority-nibble audit declared exceptional fibres after every
bite and imposed tolerances `eta_t` satisfying both

\[
 \sum_t\mathscr E_t/\eta_t^2=o(W)
 \quad\hbox{and}\quad
 \sum_t\eta_t=o(1).
\]

That is unnecessarily expensive.  Degree errors accumulate as a
martingale plus predictable drift.  One may stop each fibre only when its
**cumulative** normalized error exits one fixed corridor.  A single
weighted Doob inequality then charges the entire history.

With the sharpened raw common-link estimate

\[
 \mathfrak T(x)=m^{-1+o(1)},
\]

the prospective all-rank quadratic-variation ledger is
`B_m W`, where `B_m=m^{-1/2+o(1)}`.  The theorem below would then permit
the corridor `eta=B_m^{1/4}=o(1)` while charging only `o(W)` exceptional
fibre weight.  This removes the incompatible sum of per-round tolerances.

The stochastic lemma is complete.  Its application still requires the
unproved hereditary estimate that the stopped pair-square/four-walk ledger
is at most `B_m W`.

## 1. Weighted stopped-martingale lemma

Let `F` range over a finite family of fibres with deterministic weights
`a_F>=0`.  For every `F`, let

\[
 X_{t,F}=M_{t,F}+A_{t,F}\qquad(0\le t\le R)
 \tag{1.1}
\]

be adapted, where `M_{0,F}=A_{0,F}=0`, `M_{t,F}` is a square-integrable
martingale, and `A_{t,F}` is an arbitrary predictable-drift process.  Put

\[
 \tau_F=\min\{t:|X_{t,F}|\ge\eta\}\wedge(R+1).
 \tag{1.2}
\]

Stop both processes at `tau_F wedge R`.

### Theorem 1.1 (one global corridor)

Suppose

\[
 \sum_Fa_F\,\mathbb E\langle M_F\rangle_{\tau_F\wedge R}
 \le B_2,
 \tag{1.3}
\]

and

\[
 \sum_Fa_F\,
 \mathbb E\sup_{t\le\tau_F\wedge R}|A_{t,F}|
 \le B_1.
 \tag{1.4}
\]

Then the total expected weight of fibres which ever leave the corridor is
at most

\[
 \boxed{
 \sum_Fa_F\Pr(\tau_F\le R)
 \le \frac{4B_1}{\eta}+\frac{16B_2}{\eta^2}.}
 \tag{1.5}
\]

#### Proof

If `tau_F<=R`, then either

\[
 \sup_{t\le\tau_F}|A_{t,F}|\ge\eta/2
\]

or

\[
 \sup_{t\le\tau_F}|M_{t,F}|\ge\eta/2.
\]

Markov bounds the first probability by
`2 E sup|A|/eta`.  For the second, Doob's `L^2` maximal inequality and the
martingale isometry give

\[
 \Pr\!\left(\sup_{t\le\tau_F\wedge R}|M_{t,F}|
             \ge\eta/2\right)
 \le\frac{4}{\eta^2}\,
      \mathbb E\sup_t|M_{t,F}|^2
 \le\frac{16}{\eta^2}
      \mathbb E\langle M_F\rangle_{\tau_F\wedge R}.
\]

Multiply by `a_F` and sum.  The slightly looser coefficient `4` in the
first term of (1.5) leaves room for replacing a terminal predictable drift
by its total variation.  \(\square\)

### Corollary 1.2 (coefficient-safe choice)

If

\[
 B_1+B_2\le B_mW,
 \qquad B_m=o(1),
 \tag{1.6}
\]

then taking `eta=B_m^{1/4}` gives

\[
 \sum_Fa_F\Pr(\tau_F\le R)
 \le O(B_m^{1/2}W)=o(W),
 \tag{1.7}
\]

while every unstopped normalized fibre error remains `o(1)` throughout
the entire process.

## 2. Normalization for multiplicative degree evolution

Let `D_t(F)>0` be the exact current priority-weighted degree of a live
fibre and let `rho_{t,s(F)}` be the predictable reference contraction in
its stratum.  As long as the one-bite relative change is at most `1/2`,
put

\[
 X_{t,F}
 =\log\frac{D_t(F)}{D_0(F)\prod_{u<t}\rho_{u,s(F)}}.
 \tag{2.1}
\]

The logarithmic increment has the exact decomposition

\[
 \Delta X_{t,F}
 =\bigl(\Delta X_{t,F}
       -\mathbb E[\Delta X_{t,F}\mid\mathcal F_t]\bigr)
  +\mathbb E[\Delta X_{t,F}\mid\mathcal F_t].
 \tag{2.2}
\]

The first term defines `M`; the second defines `A`.  On the stopped
corridor, logarithm and relative degree error differ by only a
`1+O(eta)` factor.  Thus (1.7) gives simultaneously:

1. an `o(W)` weighted exceptional tag/target ledger;
2. `(1+o(1))` degree comparability on every remaining fibre at every
   bite; and
3. the denominator bounds needed to normalize the next bite.

The one-bite large-change event is already covered by the exact Bernstein
and deadline ledgers in the priority audit, so it may be added to the
`o(W)` exceptional term.

## 3. The sharpened numerical target

The refined pair-shell calculation gives, before residual tilting,

\[
 \mathfrak T(x)
 =O\!\left(\frac1m+\frac g{m^{3/2}}\right)
 =m^{-1+o(1)}.
 \tag{3.1}
\]

Under ideal residual pair-square inflation at density
`z>=1/log m`, it gives

\[
 \mathfrak T_z(x)
 \le C\left(
 \frac{z^{-2}}m+
 \frac{gz^{-2}}{m^{3/2}}+
 \frac{z^{-3}}{m^{3/2}}
 \right)
 =m^{-1+o(1)}.
 \tag{3.2}
\]

There are `2Q+1=m^{1/2+o(1)}` protected strata.  After summing the
effective nibble time, the intended aggregate budget is therefore

\[
 \boxed{
 B_m
 =Q\,m^{-1+o(1)}\log\log m
 =m^{-1/2+o(1)}.}
 \tag{3.3}

This is far below one.  Corollary 1.2 would take

\[
 \eta=m^{-1/8+o(1)},
\]

which is still much smaller than the terminal resource density
`1/log m`.  Hence Johnson expansion retains the required positive fraction
of free local toggles throughout the stopped process.

## 4. Exact remaining theorem

It is enough to prove, **only up to the stopping times (1.2)**, that the
priority mean-spread and common-link kernels satisfy

\[
 \sum_Fa_F\,
 \mathbb E\sup_{t\le\tau_F\wedge R}|A_{t,F}|
 +
 \sum_Fa_F\,
 \mathbb E\langle M_F\rangle_{\tau_F\wedge R}
 \le m^{-1/2+o(1)}W.
 \tag{4.1}
\]

The raw pair-square theorem, dynamic-quarantine denominator preservation,
and the exact one-bite common-link identity establish every unweighted
ingredient of (4.1).  The unsummed term is the residual cross-slice
physical label-collision/four-walk functional.  A stopped witness-tree
bound for that functional would complete hereditary propagation.

No coefficient-one conclusion is claimed here.
