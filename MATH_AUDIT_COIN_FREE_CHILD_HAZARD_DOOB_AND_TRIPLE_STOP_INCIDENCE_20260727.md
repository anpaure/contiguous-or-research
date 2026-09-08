# Coin-free child hazards, the exact reference, and the localized triple-stop ledger

Date: 2026-07-27

Scope: the pair-parent/triple-child boundary in the compensated
vertex-induced ordinary-promotion-frame process.  This is an audit of the
proposed child-wise Hilbert process and of the final conversion to stopped
marked incidence.  No independence hypothesis is used.

## 0. Verdict

There are two distinct conclusions.

1.  The exact child-wise nonterminal normalizer is valid, but its
    comparison with the natural reference depends on whether compensation
    clocks remain.  If \(T=S\cup\{a\}\), where \(|S|=2\), then in the
    compensated-union interpretation

    \[
      Z_T(t)=
      {d_t(T)\over d_0(T)u_t^{r-3}}
      \exp\!\left[-\int_0^t\beta_T(s)\,ds\right]
      \tag{0.1}
    \]

    is a nonnegative supermartingale after terminal death and the usual
    degree/profile stops are included.  Before PPS,

    \[
      0\le \int_0^t\beta_T(s)\,ds
      \le {C A_2\over m}\left({1\over u_t}-1\right).
      \tag{0.2}
    \]

    Hence, uniformly for \(u_t\ge z\), the child-specific reference is

    \[
      d_0(T)u_t^{r-3}
      \exp\!\left[\int_0^t\beta_T(s)\,ds\right]
      =(1+o(1))d_0(T)u_t^{r-3}                         \tag{0.3}
    \]

    uniformly under the sufficient condition \(A_2/(mz)=o(1)\).  In the
    literal edge-only process, the same statements hold with the exact
    reference \(R_T^E\) in (1.12), but comparison with \(u^{r-3}\)
    additionally requires the integrated degree-deficit condition (2.8).
    The
    displayed estimate does not assert necessity of that condition for an
    individual child.  The sign in (0.3) is positive:
    common events lower the nonterminal hazard, so the correct reference
    is larger than \(d_0(T)u^{r-3}\), not smaller.

2.  The active-mass Hilbert argument, as presently stated, is not a
    proved route.  For

    \[
      p_{S,a}={d_0(Sa)\over (r-2)d_0(S)},\qquad
      P_S(t)=\sum_{a\ {\rm active}}p_{S,a},              \tag{0.4}
    \]

    \(P_S/u_t\) is not a martingale.  It has an explicit nonnegative
    degree-deficit/common-event drift.  Moreover whole-arm PSF pays the
    exclusive-shore part of the centered bracket, but not the surviving
    same-row/common-resource kernel; simultaneous shore deletion and
    survivor decrement also leave the boundary covariance (5.16).  Thus
    Doob/Freedman applied to \(P_S\), plus PSF alone, does not prove CHD.

There is a useful but insufficient positive conclusion after the relevant
reference comparison is granted.  If the potential monitors are anchored
at time zero (or introduced by a predictable cohort with the corresponding
entry-value ledger), the one-child
supermartingales (0.1), the exact identity

\[
  \sum_{a}q_3(Sa)=(r-2)q_2(S),                           \tag{0.5}
\]

and the already proved whole-arm pair-profile census give only the
**time-zero monitor-label** estimate

\[
  \boxed{
  \mathbb E[\hbox{time-zero \(q_3\)-mass of crossing monitors}]
  \le {C L^{C_*}\over A_3}\,W=o(W)}                     \tag{0.6}
\]

whenever \(A_3/L^{C_*}\to\infty\).  This is **not** the required stopped
incidence estimate.  At its first PFS\(_3\) crossing, the child degree in
its natural current reference is \(\Theta(A_3q_3(T))\).  Thus the
conversion from (0.6) to literal stopped link incidence multiplies by
\(A_3\), exactly cancelling Doob's \(A_3^{-1}\).  The resulting bound is
only \(O(L^{C_*}W)\), not \(o(W)\).

Accordingly, (0.6) is a genuine positive theorem only under the convention
that “stopped incidence” means the static monitor label
\(\omega(T)=q_3(T)\).  The downstream literal quarantine convention used
when active link rows are actually removed is the natural-current or
literal-row quantity in (4.9), and is not closed.

Consequently neither link-local nor whole-center triple stopping is closed
by the proposed Doob argument.  A tail \(o(A_3^{-1})\), or equivalently a
quadratic energy which charges a crossing by \(A_3^2\), is genuinely
needed.  The centered Hilbert route was designed to provide this extra
factor, but its common-resource bracket is not controlled by whole-arm
PSF.  An adaptively chosen monitor creates a further, independent
selection obstruction.

There are two meanings of “coin-free”, and the audit must separate them.
If compensation remains in the physical dynamics but is absorbed into the
union hazard, (0.1)--(0.3) hold under PPS.  If “coin-free” literally means
that compensation clocks are deleted and only selected edges ring, the
reference has an additional integrated degree-deficit term.  Whole-arm PSF
does not bound it.  Sections 1--2 give both formulas.  The stopped-incidence
cancellation and the common-row diagonal obstruction apply even after the
stronger reference comparison is granted.

## 1. Exact nonterminal child hazards

### 1.1 Compensated-union benchmark

Let \({\cal H}_t\) be the current \(r\)-uniform catalogue, let

\[
  \nu_t={1\over r\Delta_t},\qquad
  \chi_t(y)={\Delta_t-d_t(y)\over r\Delta_t},            \tag{1.1}
\]

and put

\[
  J_t(A)=\sum_g(|g\cap A|-1)_+.
  \tag{1.2}
\]

The total physical-union deletion hazard is

\[
  \Lambda_t(A)={|A|\over r}-{J_t(A)\over r\Delta_t}.
  \tag{1.3}
\]

Fix an active triple \(T\), and write

\[
  N_T(t)=d_t(T)=\sum_{F\supseteq T}1_{\{F\ {\rm active}\}}.
  \tag{1.4}
\]

For one active row \(F\supseteq T\), the rate of a deletion which kills
\(F\) but avoids \(T\) is exactly

\[
\begin{aligned}
  \Lambda_t(F)-\Lambda_t(T)
  &={r-3\over r}
    -\nu_t\bigl(J_t(F)-J_t(T)\bigr).                    \tag{1.5}
\end{aligned}
\]

This is an identity, not an independence approximation: events meeting
\(T\) are terminal, while the difference of the two union hazards counts
precisely the events avoiding \(T\) and meeting \(F\setminus T\).

Define, while \(N_T>0\),

\[
  \beta_T(t)=\nu_t{\displaystyle
       \sum_{F\supseteq T}\bigl(J_t(F)-J_t(T)\bigr)
       \over N_T(t)},                                   \tag{1.6}
\]

and put \(\beta_T=0\) after \(N_T=0\).  Summing (1.5) over the current
\(T\)-link gives

\[
  {\cal L}^{\rm nt}_tN_T
  =-{r-3\over r}N_T+\beta_TN_T.                         \tag{1.7}
\]

Since \(u_t=e^{-t/r}\), division by \(u_t^{r-3}\) cancels the first
term.  Multiplication by the predictable finite-variation factor
\(\exp(-\int\beta_T)\) cancels the second.  A terminal event meeting
\(T\) sends \(N_T\) to zero and hence contributes only negative drift.
This proves the supermartingale assertion (0.1).

Equivalently, the exact nonterminal reference is

\[
  R_T^{\rm comp}(t)=\exp\!\left[-\int_0^t
        \left({r-3\over r}-\beta_T(s)\right)ds\right]
        =u_t^{r-3}e^{B_T(t)},                            \tag{1.8}
\]

where \(B_T=\int\beta_T\).  This proves the sign and the exponent in
(0.3); the full degree reference is \(d_0(T)R_T^{\rm comp}\).

### 1.2 Literal edge-only process

If compensation clocks are removed, let only selected edges ring at rate
\(\nu_t=(r\Delta_t)^{-1}\).  The exact nonterminal hazard of the
\(T\)-link is

\[
 h_T^E(t)={\nu_t\over N_T(t)}
 \sum_{F\supseteq T}
 |{\cal E}_t(F)\setminus{\cal E}_t(T)|.                 \tag{1.9}
\]

Using

\[
 |{\cal E}_t(F)\setminus{\cal E}_t(T)|
 =\sum_{x\in F\setminus T}d_t(x)
  -[J_t(F)-J_t(T)],                                     \tag{1.10}
\]

and \(|F\setminus T|=r-3\), one obtains

\[
\boxed{
 {r-3\over r}-h_T^E(t)
 ={1\over r\Delta_tN_T(t)}
 \sum_{F\supseteq T}
 \left[
  \sum_{x\in F\setminus T}(\Delta_t-d_t(x))
  +J_t(F)-J_t(T)
 \right].}                                              \tag{1.11}
\]

Both bracketed terms are nonnegative.  Thus, writing the right side of
(1.11) as \(\epsilon_T^E(t)\), the exact edge-only reference is

\[
 \boxed{
 R_T^E(t)=u_t^{r-3}
 \exp\!\left[\int_0^t\epsilon_T^E(s)\,ds\right].}        \tag{1.12}
\]

The normalized coordinate
\[
 Z_T^E(t)={d_t(T)\over d_0(T)R_T^E(t)}                  \tag{1.13}
\]
has zero predictable nonterminal drift and is a nonnegative
supermartingale after terminal death.  Formula (1.12), rather than
\(u^{r-3}e^{B_T}\) with only the \(J\)-term, is the literal coin-free
answer.

## 2. Comparison with \(u^{r-3}\)

### 2.1 The compensated comparison

For \(T\subseteq F\), the per-event inequality

\[
  (|g\cap F|-1)_+-(|g\cap T|-1)_+
  \le
  \#\bigl\{\{x,y\}\subseteq g\cap F:
                    \{x,y\}\not\subseteq T\bigr\}       \tag{2.1}
\]

holds.  Indeed, if \(g\) meets \(T\) in \(a\ge1\) points and
\(F\setminus T\) in \(c\) points, the left side is \(c\), while the
cross pairs contribute \(ac\ge c\).  If \(a=0\), the left side is
\((c-1)_+\le\binom c2\).  Summing (2.1) over active \(g\) gives

\[
  J_t(F)-J_t(T)
  \le \sum_{\substack{\{x,y\}\subseteq F\\
                       \{x,y\}\not\subseteq T}}d_t(x,y).
  \tag{2.2}
\]

Before PPS,

\[
  d_t(x,y)\le A_2u_t^{-1}q_2(x,y)\Delta_t.              \tag{2.3}
\]

The exact promotion-frame pair census, already used in the whole-arm
PSF proof, is

\[
  \sum_{\{x,y\}\subseteq F}q_2(x,y)\le {C\over m}       \tag{2.4}
\]

for every catalogue row \(F\).  To recall its normalization, the fixed
owner cyclic-distance table gives
\(\sum_{y\in F\setminus\{x\}}d_0(x,y)\le CD_0/m^2\);
summing over the \(r=(1+o(1))m\) resources of \(F\) and dividing by two
proves (2.4).  Top-owner terms are smaller and distinct tops have zero
codegree.

Equations (2.2)--(2.4) imply, row by row,

\[
  J_t(F)-J_t(T)\le {C A_2\Delta_t\over m u_t}.           \tag{2.5}
\]

Average over the \(T\)-link and use
\(\nu_t=(r\Delta_t)^{-1}\):

\[
  0\le\beta_T(t)\le {C A_2\over r m u_t}.               \tag{2.6}
\]

Finally \(dt=-r\,du/u\), so

\[
\begin{aligned}
  B_T(t)
  &\le {C A_2\over rm}\int_0^t{ds\over u_s}
   ={C A_2\over m}\int_{u_t}^1{du\over u^2}\\
  &={C A_2\over m}\left({1\over u_t}-1\right).
                                                               \tag{2.7}
\end{aligned}
\]

This proves (0.2)--(0.3), uniformly even when \(d_t(T)\) is small: the
bound was proved before division by \(N_T\).  Children with \(d_0(T)=0\)
are absent, and after \(N_T=0\) the observable is identically zero, so
there is no denominator exception.

### 2.2 The edge-only degree-deficit gate

For the edge-only reference (1.12), the \(J\)-part of
\(\int\epsilon_T^E\) is still bounded by (2.7).  The remaining part is

\[
 {\rm ID}_T(t):=
 \int_0^t{1\over r\Delta_sN_T(s)}
 \sum_{F\supseteq T}\sum_{x\in F\setminus T}
       (\Delta_s-d_s(x))\,ds.                           \tag{2.8}
\]

Consequently

\[
 0\le
 \log{R_T^E(t)\over u_t^{r-3}}
 \le {\rm ID}_T(t)
   +{CA_2\over m}\left({1\over u_t}-1\right).            \tag{2.9}
\]

Thus the literal coin-free comparison
\[
                         R_T^E=(1+o(1))u^{r-3}           \tag{2.10}
\]
requires \(\sup_{T,t}{\rm ID}_T(t)=o(1)\), at least in the
incidence-weighted family being charged, in addition to
\(A_2/(mz)=o(1)\).  Whole-arm PSF controls common selected edges between
two displayed row shores.  It contains neither the one-row degree deficits
\(\Delta-d_s(x)\) in (2.8) nor their child-link average.  Therefore
(2.10) is an additional hypothesis in the edge-only process.

## 3. One-child maximal bound

Let the degree corridor contain the lower bound

\[
  \Delta_t\ge c_DD_0u_t^{r-1}.                           \tag{3.1}
\]

At a PFS\(_3\) crossing,

\[
  d_t(T)\ge A_3u_t^{-2}q_3(T)\Delta_t,                  \tag{3.2}
\]

where \(q_3(T)=d_0(T)/D_0\).  Hence

\[
  {d_t(T)\over d_0(T)u_t^{r-3}}\ge c_DA_3.              \tag{3.3}
\]

Put
\[
 \Theta_*=\sup_{T,t:u_t\ge z}
          \log {R_T(t)\over u_t^{r-3}},                 \tag{3.4}
\]
using the compensated reference (1.8) or the edge-only reference (1.12)
as appropriate.  In the compensated process,
\(\Theta_*\le CA_2/(mz)=o(1)\).  In the edge-only process the same
conclusion additionally requires the incidence-weighted form of
\({\rm ID}_T=o(1)\).

The crossing (3.3) implies
\[
                         Z_T(\tau_T)\ge c_DA_3e^{-\Theta_*}.
                                                               \tag{3.5}
\]
Hence Doob's inequality gives, for every time-zero anchored child monitor,

\[
  \boxed{
  \Pr(\tau_T^{\rm PFS_3}<\tau_{\rm other},\ u\ge z)
  \le {e^{\Theta_*}\over c_DA_3}
  ={1+o(1)\over c_DA_3}.}                               \tag{3.6}
\]

Here \(\tau_{\rm other}\) includes terminal death, degree failure, PPS
failure, and any already charged whole-arm stop.  Stopping preserves the
supermartingale.  No Freedman estimate and no covariance between
different children enters (3.6).

## 4. Exact child mass and the whole-arm pair ledger

Put \(b=r-2\).  Double-counting incidences in the time-zero \(S\)-link
gives

\[
  \sum_{a\notin S}d_0(Sa)=b\,d_0(S).                    \tag{4.1}
\]

After division by \(D_0\), this is (0.5).  Equivalently the fixed
weights in (0.4) sum to one and

\[
  q_3(Sa)=bq_2(S)p_{S,a}.                                \tag{4.2}
\]

Now consider one equality-resolved marked occurrence with at most
\(p=O(L)\) displayed catalogue rows.  Its pair-parent list is made from
within-row pairs and from the two exclusive shores of ordered row pairs.
The second exact census used in the whole-arm theorem is

\[
  \sum_{x\in F\setminus F'}
  \sum_{y\in F'\setminus F}q_2(x,y)\le {C\over m}.       \tag{4.3}
\]

It follows from the same fixed-owner table: for fixed \(x\), summing
over the resources of \(F'\) is at most \(CD_0/m^2\), and summing over
the \(O(m)\) choices of \(x\) gives (4.3).  Resolving common physical
resources can only remove terms.

Allowing an additional \(L^{C_0}\) compressed-type multiplicity, (2.4)
and (4.3) give the deterministic ledger

\[
  \sum_{S\in{\cal S}(\iota)}q_2(S)
  \le {L^{C_*}\over m}                                  \tag{4.4}
\]

for every retained marked occurrence \(\iota\), where \(C_*\) is fixed.

Define the time-zero monitor-label charge by

\[
 {\mathsf I}_3
 =\sum_{\iota}w_\iota
   \sum_{S\in{\cal S}(\iota)}
   \sum_a q_3(Sa)
   {\bf1}_{\{Sa\ {\rm crosses\ PFS_3}\}},                \tag{4.5}
\]

where \(w_\iota\) is the owner/root incidence multiplicity and
\(\sum_\iota w_\iota\le CW\).  This counts the initial \(q_3\)-mass of
the monitors which cross.  It is not yet the current link incidence
removed at the crossing.

Using (3.6), then (0.5), then (4.4),

\[
\begin{aligned}
 \mathbb E{\mathsf I}_3
 &\le {e^{\Theta_*}\over c_DA_3}
   \sum_\iota w_\iota
   \sum_{S\in{\cal S}(\iota)}\sum_aq_3(Sa)\\
 &= {e^{\Theta_*}b\over c_DA_3}
   \sum_\iota w_\iota
   \sum_{S\in{\cal S}(\iota)}q_2(S)\\
 &\le {C e^{\Theta_*}bL^{C_*}\over mA_3}W
  \le {CL^{C_*}\over A_3}W.                            \tag{4.6}
\end{aligned}
\]

This proves (0.6).  Multiple parent representations of one triple only
overcount the left side and are already included in (4.4).  Arbitrary
correlation among child processes is harmless because (4.6) uses only
linearity of expectation.

If the whole-arm theorem has already removed a set of marked occurrences
of total incidence \(o(W)\), discard those occurrences before applying
(4.4).  Their cost is their literal marked incidence, not \(bq_2\), so
no factor \(b\) amplifies the exceptional ledger.

### 4.1 The missing current-incidence factor

There are four different quantities which earlier reports sometimes call
“incidence”.  The natural current normalized size of a triple link is

\[
  {\cal C}_T(t):=
  {d_t(T)\over D_0u_t^{r-3}}
  =q_3(T)X_T(t).                                        \tag{4.7}
\]

At the first PFS\(_3\) crossing, (3.1)--(3.3) give

\[
  c_DA_3q_3(T)\le {\cal C}_T(\tau_T)
  \le C_DA_3q_3(T),                                     \tag{4.8}
\]

up to fixed corridor constants.  There is no positive event overshoot:
\(d_t(T)\) has only downward jumps while the moving reference decreases
continuously.

More explicitly, the defining PFS\(_3\) boundary and the degree corridor
give

\[
\begin{aligned}
\text{static monitor label:}\quad&
       q_3(T),\\
\text{natural current fibre mass:}\quad&
       {d_{\tau_T}(T)\over D_0u_{\tau_T}^{r-3}}
       =\Theta(A_3q_3(T)),\\
\text{literal current rows:}\quad&
       d_{\tau_T}(T)
       =\Theta\!\left(
          A_3q_3(T)D_0u_{\tau_T}^{r-3}\right),\\
\text{current-degree-normalized rows:}\quad&
       {d_{\tau_T}(T)\over\Delta_{\tau_T}}
       =\Theta\!\left(A_3u_{\tau_T}^{-2}q_3(T)\right).
                                                               \tag{4.9}
\end{aligned}
\]

The \(u^{-2}\) in the last line is not an error: it is exactly the ratio
between the triple-link base \(D_0u^{r-3}\) and the degree base
\(D_0u^{r-1}\).  It disappears only if the downstream marked-incidence
normalization already contains the natural triple-fibre reference.  A
selected-edge clock contributes
\[
 \nu_{\tau_T}d_{\tau_T}(T)
 =\Theta\!\left({A_3q_3(T)\over r u_{\tau_T}^{2}}\right),
                                                               \tag{4.10}
\]
so the clock by itself does not remove this factor.

Therefore literal link-local stopped incidence has the scale

\[
 {\mathsf C}_3
 \asymp A_3
 \sum_{\iota}w_\iota
 \sum_{S\in{\cal S}(\iota)}\sum_a
 q_3(Sa){\bf1}_{\{Sa\ {\rm crosses}\}},                 \tag{4.11}
\]

when incidence is normalized by the natural triple-fibre base.  Combining
(4.6) with (4.11) yields only

\[
                        \mathbb E{\mathsf C}_3
 \le C L^{C_*}W,                                        \tag{4.12}
\]

with no vanishing factor.  This cancellation is sharp for a first-moment
argument: a nonnegative martingale which equals \(A_3\) with probability
\(A_3^{-1}\) and \(0\) otherwise starts at one and attains equality in
Doob's bound, while its expected value at the crossing is one.

Thus the whole-arm saving \(m^{-1}\) cancels the child multiplicity
\(b\sim m\), but it does not also pay the height \(A_3\) of a failed
monitor.  Writing

\[
 \varepsilon_S=\sum_a p_{S,a}\Pr(Sa\hbox{ crosses}),    \tag{4.13}
\]

the exact aggregate requirement is

\[
 \sum_\iota w_\iota\sum_{S\in{\cal S}(\iota)}
 q_2(S)\varepsilon_S=o\!\left({W\over bA_3}\right).
                                                               \tag{4.14}
\]

In view of (4.4), the pointwise bound
\(\varepsilon_S=o(1/(L^{C_*}A_3))\) is sufficient.  The stronger
centered-energy estimate \(O(L^C/(bA_3^2))\) proposed in the Hilbert note
would also suffice after choosing the threshold exponents with room.
Doob gives only \(O(A_3^{-1})\), with no vanishing factor beyond the
height itself.

## 5. The active mass is not a martingale

For completeness, fix the parent pair \(S\) and let \(I_a(t)\) be the
indicator that the extension resource \(a\) is still active, stopped when
\(S\) dies.  Its conditional deletion hazard is

\[
\begin{aligned}
 \gamma_{S,a}(t)
 &=\Lambda_t(Sa)-\Lambda_t(S)\\
 &={1\over r}-\delta_{S,a}(t),\qquad
 \delta_{S,a}(t)=\nu_t\bigl(J_t(Sa)-J_t(S)\bigr)\ge0.
                                                               \tag{5.1}
\end{aligned}
\]

In fact

\[
 J_t(Sa)-J_t(S)
 =|\{g:a\in g,\ g\cap S\ne\varnothing\}|,               \tag{5.1a}
\]

because adjoining \(a\) increases \((|g\cap S|-1)_+\) by one exactly
for those \(g\).  Hence the drift is strictly positive whenever the
active \(Sa\)-link is nonempty.

Therefore, with \(P_S=\sum_ap_{S,a}I_a\), the preterminal generator is

\[
  (\partial_t+{\cal L}^{\rm nt}_t){P_S\over u_t}
  ={1\over u_t}\sum_a p_{S,a}I_a\delta_{S,a}\ge0.       \tag{5.2}
\]

Thus \(P_S/u_t\), frozen at the parent terminal time, is a submartingale,
not the martingale asserted in the first active-shore calculation.  If
parent death instead sends the score to zero, it adds a favorable negative
terminal jump but still does not restore the claimed zero preterminal
drift.  One may correct each coordinate by its own factor

\[
  I_a(t)u_t^{-1}
  \exp\!\left[-\int_0^t\delta_{S,a}(s)ds\right],         \tag{5.3}
\]

but the sum then has child-dependent weights.

In the literal edge-only process the failure is already present without
the common-event correction.  A live resource \(a\) has selected-edge
hazard \(d_t(a)/(r\Delta_t)\), so the unprotected active-mass score obeys

\[
 (\partial_t+{\cal L}_t^E){P_S\over u_t}
 ={1\over r\Delta_tu_t}
  \sum_a p_{S,a}I_a(t)(\Delta_t-d_t(a))\ge0.            \tag{5.3a}
\]

Protecting \(S\) removes shared terminal events from the nonterminal
hazard and adds the nonnegative common-event term from (5.2).  Thus neither
the edge-only nor the compensated interpretation gives the asserted
zero-drift common reference without a child-specific correction.

There is also a quantitative error in the advertised shore-jump bound.
For a distance-two owner pair \(S=\{X,Z\}\), its four internal midpoint
children satisfy

\[
  q_3(SY_{ij})={1\over4}q_2(S).
  \tag{5.4}
\]

One parent-disjoint event row contains three of the four midpoints.  By
(4.2), selecting that row deletes active shore weight at least

\[
  3\,{q_3(SY_{ij})\over bq_2(S)}={3\over4b}.             \tag{5.5}
\]

Hence the previously used \(L^C/(bm)\) selected-event jump envelope is
false by a factor of order \(m\), even after complete equality
resolution.  A hypothetical uniform \(O(1/b)\) envelope would still give
a useful Freedman exponent at \(z\gg1/b\), but such an envelope is not a
consequence of whole-arm PSF: PSF counts events meeting two exclusive
full-row shores, whereas (5.5) is a conditional one-parent child-overlap
quantity.  The common-resource fourth kernel in the centered bracket is
the same unresolved distinction.

Indeed, if

\[
 w_g(t)=\sum_{\substack{a\in g\setminus S\\a\ {\rm active}}}p_{S,a},
                                                               \tag{5.6}
\]

then the selected-edge part of the predictable bracket of the corrected
active-mass process contains exactly

\[
 {1\over u_t^2}\nu_t
 \sum_{g:g\cap S=\varnothing}w_g(t)^2.                  \tag{5.7}
\]

The linear marginal identity controls
\(\nu_t\sum_gw_g\), but not the square in (5.7).  If one had the
additional pointwise estimate

\[
                         \max_gw_g\le {L^C\over b},      \tag{5.8}
\]

then, while \(P_S\le2u\), the integrated bracket would be at most

\[
 {CL^C\over b}\int_z^1{du\over u^2}
 \le {CL^C\over bz}=o(1)                               \tag{5.9}
\]

at the square-root stopping density.  Equation (5.5) is consistent with
(5.8) but disproves the stronger \(L^C/(bm)\) estimate.  Neither (5.8)
nor a direct aggregate substitute follows from exclusive-shore PSF.

The weighted mean part of the proposal is algebraically correct.  If
\(X_{S,a}=d_t(Sa)/(d_0(Sa)u^{b-1})\), then

\[
  \sum_{a\ {\rm active}}p_{S,a}X_{S,a}=uX_S.            \tag{5.10}
\]

For the appropriate child factor
\(c_a=u^{r-3}/R_{Sa}\) and \(Z_a=c_aX_{S,a}\), the reference comparison
gives

\[
 e^{-\Theta_*}uX_S\le\sum_ap_{S,a}Z_a\le uX_S.         \tag{5.11}
\]

Thus, on \(P_S\ge c_0u\) and PPS, the active weighted mean is
\(O(A_2/c_0)\).  Coordinate deletion also decreases the weighted centered
sum of squares.  These facts do not supply either the active-mass lower
tail or the common-resource carré-du-champ bound, so they do not complete
the Hilbert proof.

### 5.1 Moving-shore boundary covariance

There is an additional exact term when one selected edge both deletes
extension coordinates and decrements surviving child links.  Let \(D_g\)
be the deleted shore, of weight \(d_g\), let \(B_g\) be the surviving shore,
of weight \(P_g=P_S-d_g\), and let
\[
 \delta_g=\bar Z_{B_g}-\bar Z_S.                         \tag{5.12}
\]
Write \({\cal D}_S(g)=V_S-V_{S;B_g}\ge0\) for the variance removed by
the shore deletion.  If \(h_{g,a}\) is the Doléans-normalized decrement on
\(a\in B_g\), put
\[
 H_g=\sum_{a\in B_g}p_ah_{g,a},\qquad
 h_g^\circ=h_g-H_g/P_g.                                 \tag{5.13}
\]

Polarization after the deletion gives the jump term
\[
 -{\cal D}_S(g)-2\langle Z-\bar Z_{B_g},h_g^\circ\rangle_p
 +\|h_g^\circ\|_p^2.                                    \tag{5.14}
\]
The coordinatewise Doléans drift cancels the linear decrement centered at
the **old** mean \(\bar Z_S\), not the new mean \(\bar Z_{B_g}\).
The difference of those two linear terms is \(2\delta_gH_g\).
Consequently the exact moving-shore generator contains
\[
\boxed{
 \sum_g\lambda_g\left[
 -{\cal D}_S(g)+2\delta_gH_g+\|h_g^\circ\|_p^2
 \right].}                                              \tag{5.15}
\]

Thus coordinatewise zero drift does not reduce the generator to the
centered square alone.  Weighted ANOVA gives
\[
 {\cal D}_S(g)
 =V_{D_g}+{P_SP_g\over d_g}\delta_g^2,
\]
and completing the square yields the sign-free bound
\[
 -{\cal D}_S(g)+2\delta_gH_g
 \le {d_gH_g^2\over P_SP_g}.                            \tag{5.16}
\]
The right side is a boundary-covariance diagonal not supplied by
whole-arm PSF.

### 5.2 Literal same-row diagonal counterexample

The failure is already visible without compensation clocks.  Fix
\(b=r-|S|\ge2\) and \(D\ge2\).  Choose disjoint \(b\)-sets
\(B_1,\ldots,B_D\) and central rows
\[
                         F_i=S\cup B_i.                  \tag{5.17}
\]
For every \(x\in\bigcup_iB_i\), add \(D-1\) private \(r\)-edges through
\(x\), avoiding \(S\) and every other \(B\)-resource, with fresh remaining
vertices.  Add a disjoint degree-\(D\) reservoir so that
\(\Delta=D\).  Then
\[
 d_0(S)=D,\qquad d_0(Sx)=1,\qquad p_x={1\over bD},       \tag{5.18}
\]
and every monitored child resource has degree \(\Delta\).  Distinct
central rows have no nonterminal selected edge meeting both outside
shores, so their distinct-row whole-arm PSF term is exactly zero.

Initially all child coordinates equal one and \(V_S=0\).  Selecting a
private edge through \(x\in B_i\) deletes the coordinate \(Sx\) and kills
the unique row in each of the other \(b-1\) child links \(Sy\),
\(y\in B_i\setminus\{x\}\).  With
\[
 p={1\over bD},\qquad P'=1-p,\qquad w=(b-1)p,
\]
the exact variance created by this event is
\[
 \Delta V={w(P'-w)\over P'}
 ={(b-1)/(bD)\over1-1/(bD)}
   \left(1-{1\over D}\right).                           \tag{5.19}
\]
There are \(bD(D-1)\) private edges, each of rate \(1/(rD)\).  Hence
\[
\boxed{
 ({\cal L}V)(0)
 ={(b-1)(D-1)^2\over rD^2(1-1/(bD))}
 \ge {b-1\over4r}.}                                     \tag{5.20}
\]

For \(b\asymp r\), (5.20) is \(\Theta(1)\), while the required CHD scale
is \(L^C/(rb)=m^{-2+o(1)}\).  The degree-deficit part of the active-mass
edge-only drift (5.3a) vanishes at this state because every supported
child has degree \(\Delta\); the protected common-event correction and
the child-reference logarithmic defect are only \(O(1/(rD))\) and
\((b-1)/(rD)\), respectively, and tend to zero as \(D\to\infty\).  Thus active-mass
balance, near-natural child references, and even zero distinct-row PSF do
not imply the Hilbert diagonal.  This is an abstract simple
\(r\)-uniform catalogue, not a claimed reachable ordinary-promotion
residual; it is a literal counterexample to the proposed implication from
the listed ingredients.

## 6. Correlation, cohorts, and the exact boundary of the theorem

The estimate (3.6) is for a monitor anchored before the randomness being
bounded.  It remains valid after multiplication by a fixed marked-union
survival indicator, because death of that union is terminal and favorable.
It also remains valid for a predictable cohort introduced at time
\(\sigma\) provided its conditional entry contribution

\[
  \mathbb E\!\left[w_{\sigma,T}Z_T(\sigma)\right]
  \tag{6.1}
\]

is charged in the cohort ledger.  One may not choose \(T\) after seeing
which child has crossed and then apply the time-zero bound: the choice
\(T=T(\omega)\) equal to a crossing child makes the conditional crossing
probability one.  This elementary selection example shows that
predictability is a theorem hypothesis, not bookkeeping.

Likewise (4.6) controls only the time-zero \(q_3\)-mass of the monitors.
It controls neither the current \(Sa\)-link incidence in (4.9) nor

\[
  \sum_\iota w_\iota
   {\bf1}_{\{\text{some child monitor of }\iota\text{ crosses}\}}.
  \tag{6.2}
\]

For (6.2), the \(q_3\)-weights disappear and a polynomial monitor union
can reappear.  The exact proved theorem is therefore only:

> **Time-zero crossing-mass theorem.**  Assume \(A_2/(mz)=o(1)\), the
> degree and PPS stops, the pair-list ledger (4.4), and a time-zero
> anchored or entry-charged predictable monitor family.  Then the initial
> \(q_3\)-mass of the PFS\(_3\)-crossing monitors is at most
> \(CL^{C_*}W/A_3=o(W)\) in expectation.

This theorem does not imply \(o(W)\) current stopped incidence, even for
link-local quarantine, because of (4.8)--(4.10).  The surviving sufficient
statement is:

> **Conditional current-incidence theorem.**  Under the same hypotheses,
> if either the aggregate tail (4.14) holds or the pair-parent centered
> moving-shore generator—including the same-row diagonal and the boundary
> covariance (5.16)—has integrated budget
> \(O(L^C/(bA_3^2))\), with the active-mean separation used at a crossing,
> then literal PFS\(_3\)-stopped incidence is \(o(W)\).

Whole-arm PSF proves the exclusive-shore contribution to that
carré-du-champ, but not the common-resource kernel
\[
 {1\over r}\sum_y
 \operatorname {Var}_{p}\!\left(
 a\longmapsto {d_t(S\cup\{a,y\})\over
 d_0(Sa)u_t^{b-1}}\right).                              \tag{6.3}
\]

Here is a self-contained calibration showing that PSF cannot algebraically
bound (6.3).  Put \(v=b^2\), take \(N=b^3\) active child labels, partition
them into \(b\) groups of size \(v\), and let the current \(S\)-link rows
be

\[
                         S\cup B,\qquad
 B\in\binom{G}{b}                                         \tag{6.4}
\]

for one group \(G\), with no rows crossing two groups.  Every active child
has degree

\[
 A=\binom{v-1}{b-1},                                     \tag{6.5}
\]

and two distinct children in the same group have common degree

\[
 D=\binom{v-2}{b-2}=A{b-1\over v-1};                    \tag{6.6}
\]

children in different groups have common degree zero.  Add time-zero rows
carrying deleted private markers so that, at the state being audited,

\[
 p_a={u\over N},\qquad
 d_0(Sa)u^{b-1}=A                                        \tag{6.7}
\]

on the active labels; put the remaining \(p\)-mass \(1-u\) on inactive
labels.  A common-resource clock \(y\) then has decrement profile

\[
 {d_t(Say)\over d_0(Sa)u^{b-1}}
 =
 \begin{cases}
 (b-1)/(v-1),&a\ne y\text{ in the group of }y,\\
 0,&\text{otherwise}.
 \end{cases}                                             \tag{6.8}
\]

For each active common resource \(y\), add \(\Delta-A\) private
\(r\)-edges through \(y\), avoiding \(S\) and every other active child
resource, and use fresh vertices elsewhere.  Take \(\Delta\gg A\).
Then \(d_t(y)=\Delta\), and the total clock of the private selected edges
through \(y\) is
\[
              \nu_t(\Delta-A)=(1-o(1))/r.               \tag{6.8a}
\]
Every such private selected edge kills precisely the common-resource
sublink \(d_t(Say)\) in the other child coordinates.  The
\(p\)-weighted centered variance of that decrement is

\[
 (1+o(1)){u\over N}.                                     \tag{6.9}
\]

Indeed the support has weight
\((v-1)u/N=(1+o(1))u/b\), the nonzero value is
\((1+o(1))/b\), and its global active-shore mean is
\((1+o(1))/b^2\); subtracting the squared mean changes the leading
\(u/N\) by \(O(u/b^4)\).  Summing (6.9) over the \(N\) possible common
resources and their private selected-edge clocks gives

\[
                         Q_S^{\rm common}
 =(1+o(1)){u\over r}.                                    \tag{6.10}
\]

All child normalized degrees in (6.7) equal one, so every polylogarithmic
PFS\(_3\) boundary is respected; padding the time-zero pair degrees gives
the corresponding PPS and marginal profile scales.  Every joint decrement
in (6.8) is certified by the common resource \(y\), not by an event meeting
two exclusive central-row shores, so the distinct-row exclusive-shore PSF
score is zero for this contribution.  The desired CHD scale is
\(L^C/(rb)\), whereas
(6.10) is larger by \(ub/L^C\).  At \(u=b^{-1/2}\) this is a
\(b^{1/2}/L^C\) gap.

This is an induced \(r\)-uniform stopped state after the private markers
are deleted.  It is not asserted to be a reachable ordinary-promotion
state.  It proves the exact logical no-go: marginal stops and whole-arm
PSF do not imply the missing common-kernel estimate; a
catalogue-trajectory theorem is additional information.

If the installation uses whole-center quarantine, or if monitors are
created adaptively without the entry ledger, there is an additional
conversion obstruction beyond (6.3).  This is the precise
proved/conditional boundary.
