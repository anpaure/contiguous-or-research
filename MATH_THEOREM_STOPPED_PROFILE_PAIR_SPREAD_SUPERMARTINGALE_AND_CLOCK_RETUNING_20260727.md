# Stopped profile pair spread: exact supermartingale, triple-fibre variance, and clock retuning

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Work in the genuine vertex-induced compensated annular process. Let

\[
 r=(1+o(1))m,\qquad
 u_t=e^{-t/r},\qquad z=m^{-1/20},
\tag{0.1}
\]

and let \(D_0\) be the initial maximum resource degree. Put

\[
 q_2(x,y)={d_0(x,y)\over D_0},\qquad
 q_3(x,y,w)={d_0(x,y,w)\over D_0}.
\tag{0.2}
\]

Run inside the degree corridor

\[
 c_DD_0u_t^{r-1}\le\Delta_t\le C_DD_0u_t^{r-1}.
\tag{Deg}
\]

The proposed profile stops are

\[
 d_t(x,y)\le A_2u_t^{-1}q_2(x,y)\Delta_t
\tag{PPS}
\]

and

\[
 d_t(x,y,w)\le A_3u_t^{-2}q_3(x,y,w)\Delta_t.
\tag{PFS}
\]

The triple-fibre use also requires the static conditional profile

\[
 \boxed{
 \sum_{w\in V(e)}q_3(x,y,w)
 \le {C\over m}q_2(x,y)}
\tag{TFP}
\]

for every relevant event edge \(e\) disjoint from \(\{x,y\}\), with the
analogous one-resource bound for compensation events. This is the exact
normalization needed below; PFS alone does not imply it.

The conclusions are:

1. Before the first degree/PPS failure, for every active pair with
   \(d_0(x,y)>0\),

   \[
    \boxed{
    M_{xy}(t):=
    {d_t(x,y)\over d_0(x,y)u_t^{r-2}}}
   \tag{0.3}
   \]

   is a nonnegative stopped supermartingale. This uses the actual
   physical-union hazard; no independent-survivor surrogate is used.

2. Under PFS and TFP, one event changes \(M_{xy}\) by at most

   \[
    b_t={CA_3\over m u_t},
   \tag{0.4}
   \]

   and, before PPS reaches level \(A_2\), its predictable quadratic
   variation satisfies

   \[
    \boxed{
    \langle\mathcal M_{xy}\rangle_T
    \le {CA_2A_3\over z}.}
   \tag{0.5}
   \]

   The factor \(z^{-1}\) is forced by the exact clock

   \[
    {1\over m}\int_0^T{dt\over u_t}
    ={r\over m}\left({1\over z}-1\right).
   \tag{0.6}
   \]

3. Freedman's inequality consequently gives

   \[
    \boxed{
    \Pr(\text{\rm PPS fails for a fixed stopped pair before }u=z)
    \le
    \exp\!\left[-c{A_2z\over A_3}\right].}
   \tag{0.7}
   \]

4. Let \(P_m=m^{O(1)}L^{O(1)}\) bound the number of pair monitors charged
   to one marked owner/root occurrence, and let
   \(C_{\rm cp}=O(m\log m)\) be the number of predictable reference
   cohorts. If

   \[
    \boxed{
    {A_2z\over A_3}\gg
       \log(C_{\rm cp}P_m),}
   \tag{0.8}
   \]

   then the expected PPS-stopped marked incidence is \(o(W)\), and hence
   so is the stopped incidence with probability \(1-o(1)\).

5. The original choice \(A_2=L^{C_2}\), \(A_3=L^{C_3}\) does not satisfy
   (0.8) at \(z=m^{-1/20}\): its exponent in (0.7) tends to zero whenever
   \(C_2,C_3\) are fixed. A valid retuning is, for sufficiently large
   fixed \(B\),

   \[
    \boxed{
    A_2={A_3\over z}(\log m)^B.}
   \tag{0.9}
   \]

   This retuning is compatible with the already closed whole-arm
   hierarchy, because

   \[
    \int_0^T{CA_2\over mr u_t}\,dt
    =O\!\left({A_2\over mz}\right)
    =O\!\left({A_3(\log m)^B\over mz^2}\right)=o(1).
   \tag{0.10}
   \]

Thus PPS itself has \(o(W)\) stopped incidence **conditional on PFS,
TFP, and the retuned threshold (0.9)**. With the previously stated
polylogarithmic threshold, the proposed supermartingale proof fails
exactly at the integrated \(z^{-1}\) clock. The remaining unconditional
gate is propagation of PFS (and certification of TFP in every required
resource orbit).

## 1. Exact physical-union drift of a pair link

Fix \(x\ne y\) with \(d_0(x,y)>0\). Before either endpoint dies,

\[
 d_t(x,y)=\sum_{F\supseteq\{x,y\}}I_{V(F)}(t),
\tag{1.1}
\]

where \(I_U(t)\) is the survival indicator of the physical resource
union \(U\). Endpoint death is terminal and favorable, so the displayed
quantity is stopped there.

For every active catalogue edge \(F\), profile pair spread and the exact
edge-local pair census give

\[
\begin{aligned}
 J_t(V(F))
 &\le\sum_{\{v,w\}\subseteq V(F)}d_t(v,w)\\
 &\le A_2u_t^{-1}\Delta_t
       \sum_{\{v,w\}\subseteq V(F)}q_2(v,w)\\
 &\le {CA_2\Delta_t\over m u_t}.
\end{aligned}
\tag{1.2}
\]

The exact compensated physical-union hazard is

\[
 \Lambda_t(V(F))
 ={ |V(F)|\over r}-{J_t(V(F))\over r\Delta_t}.
\tag{1.3}
\]

Hence, before PPS fails,

\[
 \Lambda_t(V(F))
 \ge1-\epsilon_t,\qquad
 \epsilon_t={CA_2\over mr u_t}.
\tag{1.4}
\]

For either the original polylogarithmic \(A_2\) or the retuning (0.9),

\[
 \epsilon_t\le {1\over r}
\tag{1.5}
\]

uniformly for \(u_t\ge z\), for all sufficiently large \(m\).
Linearity of the stopped generator in (1.1) therefore gives

\[
 \mathcal G_td_t(x,y)
 \le-\left(1-\frac1r\right)d_t(x,y).
\tag{1.6}
\]

Since

\[
 -{d\over dt}\log u_t^{r-2}={r-2\over r},
\tag{1.7}
\]

the deterministic transport in (0.3) leaves drift at most

\[
 -\left(1-\frac1r\right)+{r-2\over r}
 =-\frac1r.
\tag{1.8}
\]

Thus \(M_{xy}\), stopped at endpoint, degree, PPS, and PFS failures, is
a nonnegative supermartingale. Notice that PFS is not needed for this
drift; it is needed only for the maximal tail.

## 2. Comparing the PPS threshold with the natural base

The PPS boundary is

\[
 d_t(x,y)=A_2u_t^{-1}q_2(x,y)\Delta_t.
\tag{2.1}
\]

Using \(d_0(x,y)=q_2(x,y)D_0\) and (Deg), boundary crossing implies

\[
 c_DA_2
 \le M_{xy}(t)
 \le C_DA_2.
\tag{2.2}
\]

The ratio has no upward event jumps: selection or compensation only
removes future rows, while the deterministic base decreases
continuously. Thus there is no positive overshoot at the first PPS
crossing. For a maximal inequality it is enough to stop at

\[
                         M_{xy}=c_DA_2.
\tag{2.3}
\]

Doob's inequality alone would give only \(O(A_2^{-1})\). That estimate
does not beat the polynomial number of physical pair monitors when
\(A_2\) is polylogarithmic. The triple-fibre input is what gives the
exponential tail.

## 3. Triple fibres bound one-event jumps

Let \(e\) be a possible selected event edge disjoint from \(\{x,y\}\).
The number of pair-link rows killed by selecting \(e\) is

\[
 B_{xy}(e)
 =|\{F\supseteq\{x,y\}:V(F)\cap V(e)\ne\varnothing\}|.
\tag{3.1}
\]

Pair domination, PFS, and TFP give

\[
\begin{aligned}
 B_{xy}(e)
 &\le\sum_{w\in V(e)}d_t(x,y,w)\\
 &\le A_3u_t^{-2}\Delta_t
       \sum_{w\in V(e)}q_3(x,y,w)\\
 &\le {CA_3u_t^{-2}\Delta_tq_2(x,y)\over m}.
\end{aligned}
\tag{3.2}
\]

Divide by the natural pair base

\[
 B_{xy}^{\rm ref}(t)
 =d_0(x,y)u_t^{r-2}
 =q_2(x,y)D_0u_t^{r-2}.
\tag{3.3}
\]

The upper half of (Deg) gives

\[
 \boxed{
 {B_{xy}(e)\over B_{xy}^{\rm ref}(t)}
 \le {CA_3\over m u_t}.}
\tag{3.4}
\]

For a compensation event at \(w\), the jump is \(d_t(x,y,w)\).
The one-resource part of TFP and the compensation rate
\(\chi_t(w)\le1/r\) give the same normalized jump envelope after changing
the constant.

## 4. Predictable quadratic variation and the clock

Let \(\mathcal M_{xy}\) be the martingale part of \(M_{xy}\).
At time \(t\), the edge-event contribution to its quadratic-variation
rate is

\[
 {1\over (B_{xy}^{\rm ref}(t))^2}
 \sum_e\nu_t B_{xy}(e)^2,
\qquad
 \nu_t={1\over r\Delta_t}.
\tag{4.1}
\]

By (3.4),

\[
 \sum_e\nu_t B_{xy}(e)^2
 \le {CA_3\over m u_t}B_{xy}^{\rm ref}(t)
       \sum_e\nu_tB_{xy}(e).
\tag{4.2}
\]

For each current pair-link row, the total rate of edge events killing
it is at most one. Therefore

\[
                         \sum_e\nu_tB_{xy}(e)\le d_t(x,y).
\tag{4.3}
\]

The compensation contribution satisfies the same inequality, with a
constant factor. Before the PPS boundary, (2.2) gives

\[
 {d_t(x,y)\over B_{xy}^{\rm ref}(t)}
 \le C_DA_2.
\tag{4.4}
\]

Combining (4.1)--(4.4),

\[
 {d\langle\mathcal M_{xy}\rangle_t\over dt}
 \le {CA_2A_3\over m u_t}.
\tag{4.5}
\]

Now use the actual process clock. Since \(u_t=e^{-t/r}\),

\[
 dt=-r\,{du\over u},
\tag{4.6}
\]

and therefore

\[
\begin{aligned}
 \langle\mathcal M_{xy}\rangle_T
 &\le {CA_2A_3\over m}
       \int_0^T{dt\over u_t}\\
 &= {CA_2A_3r\over m}
       \int_z^1{du\over u^2}\\
 &\le {CA_2A_3\over z}.
\end{aligned}
\tag{4.7}
\]

This proves (0.5). Replacing \(dt\) by \(du/u\), or forgetting the
outer factor \(u_t^{-1}\), would miss exactly the fatal \(z^{-1}\).

The global jump envelope before \(u=z\) is

\[
                         b={CA_3\over mz}.
\tag{4.8}
\]

## 5. Freedman tail

If PPS fails before \(u=z\), the martingale part of the stopped
supermartingale must rise by at least \(cA_2\), after absorbing its
initial value \(M_{xy}(0)=1\) and its nonpositive drift. Freedman's
inequality, (4.7), and (4.8) give

\[
\begin{aligned}
 \Pr(\tau_{xy}^{\rm PPS}<T)
 &\le
 \exp\left[
 -{cA_2^2\over A_2A_3/z+bA_2}
 \right]\\
 &\le
 \exp\left[-c{A_2z\over A_3}\right],
\end{aligned}
\tag{5.1}
\]

because \(bA_2\le CA_2A_3/(mz)\) is smaller than the variance term.
This proves (0.7).

## 6. Incidence normalization

Use predictable marked cohorts exactly as in the stopped top-strip
argument. A marked owner/root occurrence is killed terminally when its
mark dies, so all preceding drift and variance inequalities remain
valid. Resolve physical equalities before listing its pair monitors.

The pair martingales themselves are anchored at time zero. The later
reference cohorts only partition the incidence ledger; they do not reset
\(M_{xy}\). This is essential. If a genuinely new monitor is introduced
at a later stopping time, (5.1) is valid only when its entry value is at
most, say, \(c_DA_2/2\). Entering arbitrarily close to the PPS boundary
would leave no Freedman deviation to estimate.

Let

\[
 P_m=m^{O(1)}L^{O(1)}
\tag{6.1}
\]

be a uniform upper bound on the number of distinct physical pair
monitors charged to one marked occurrence. This deliberately permits the
coarse \(O(r^2)\) count. Let

\[
 C_{\rm cp}=O(m\log m)
\tag{6.2}
\]

be the number of deterministic degree/reference cohorts. Then (5.1),
linearity over marked incidences, and no union over the ambient resource
set give

\[
 \boxed{
 \mathbb E[\text{\rm PPS-stopped marked incidence}]
 \le
 C_{\rm cp}P_m
 \exp\left[-c{A_2z\over A_3}\right]W.}
\tag{6.3}
\]

Condition (0.8) makes the right side \(o(W)\). Markov's inequality at
any threshold tending to zero sufficiently slowly gives \(o(W)\)
stopped incidence with probability \(1-o(1)\).

This is the correct normalization: an ambient union bound over all
physical pairs is neither needed nor valid, while omitting \(P_m\) would
undercharge the pairs exposed by one marked occurrence.

## 7. Threshold compatibility and exact remaining gate

Take \(A_3=L^{C_3}\) and

\[
                         A_2={A_3\over z}(\log m)^B
\tag{7.1}
\]

with \(B\) large relative to the polynomial monitor and cohort exponents.
Then (0.8) holds.

The only place PPS enters the already proved whole-arm argument before
its own analytical quarantine is through the edge-hazard error

\[
                         \epsilon_t={CA_2\over mr u_t}.
\tag{7.2}
\]

Its integrated value is

\[
\begin{aligned}
 \int_0^T\epsilon_t\,dt
 &\le {CA_2\over mr}
       r\left({1\over z}-1\right)\\
 &\le {CA_3(\log m)^B\over mz^2}
 =m^{-9/10+o(1)}.
\end{aligned}
\tag{7.3}
\]

Thus the retuning does not reopen the whole-arm factorial hierarchy.
The downstream common-event clock estimates have still more margin.

What remains unproved is:

1. PFS itself has \(o(W)\) stopped incidence;
2. TFP holds uniformly in every owner/top/compensation resource orbit
   required by the process; and
3. the predictable-cohort implementation has the stated polynomial
   monitor multiplicity after all top-strip equality resolutions.

Items 2--3 are finite normalization audits. Item 1 is the next genuine
stochastic gate. With the original polylogarithmic \(A_2\), even the
pair-level Freedman exponent is insufficient because of (0.6).
