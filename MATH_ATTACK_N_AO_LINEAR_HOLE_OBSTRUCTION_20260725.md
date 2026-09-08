# Lane N continuation: exact two-sided anchor transport and a linear MSW obstruction

Date: 2026-07-25

Method: pure mathematics only. No web search, finite search, solver, or
long-running computation is used.

## 0. Result and exact scope

The existential theorem \(\mathrm{AO}_A/\mathrm{SDH}_A\) is not proved or
disproved here. A genuinely sharper exact-factor obstruction is proved.

At every depth, after an arbitrary legal earlier history, the canonical
anchor histogram is immutable. Its exact minimum \(\ell^1\)-transport to a
balanced floor/ceiling histogram is

\[
 \max\left\{
   \sum_S(c_q-\mu_q(S))_+,
   \sum_S(\mu_q(S)-c_q-1)_+
 \right\}.
\]

Every supported adjacent-deletion orientation requires at least this many
stage-\(q\) toggles. This is a two-sided statement: the first term is the
defect below the exact integer floor and the second is the excess above the
exact integer ceiling.

At depth one, \(c_1=1\). Hence every canonical lower-shadow hole forces a
distinct incoming toggle. Combining this observation with the independently
audited marked-gap theorem gives, for the canonical MSW factor,

\[
 \boxed{
 T_1(F_m^{\rm MSW})
 \ge
 \left[
 (2m-3)\operatorname{Cat}_{m-2}
 -\frac{2}{m+2}\binom{2m+1}{m}
 \right]_+
 =(1/16-o(1))W.}
\]

Thus canonical MSW, with any cyclic phase or reversal and any subsequent
adaptive history, cannot satisfy the \(o(W)\)-recourse conclusion of
\(\mathrm{AO}_A\) for any fixed \(A>0\). More strongly, every exact factor
within row distance \((1/8-\varepsilon)\operatorname{Cat}_m\) of MSW has
stage-one cost at least \((\varepsilon/2-o(1))W\).

This closes the entire sparse-repair basin of MSW, improving the previous
audited \(\Theta(W/m)\) stage-one lower bound by a factor of order \(m\).
It does **not** rule out a distant exact factor with \(o(W)\) cost, and so
does not settle the existential \(\mathrm{AO}_A/\mathrm{SDH}_A\) theorem or
the constant-one contiguous-OR theorem.

## 1. Exact adaptive notation

Let

\[
 n=2m+1,\qquad
 W=\binom{n}{m},\qquad
 B=\frac Wn=\operatorname{Cat}_m,
\]

and let \(F\) be one exact cyclic middle factor, consisting of \(B\)
wreath rows and \(W\) labelled middle owners. At depth \(q\), put

\[
 r=m-q,\qquad
 N_q=\binom nr,
\]

and divide exactly

\[
 W=c_qN_q+\rho_q,
 \qquad c_q=\left\lfloor\frac W{N_q}\right\rfloor,
 \qquad 0\le \rho_q<N_q.
\tag{1.1}
\]

For owner \(X\), let \(L_q(X)\) be its canonical depth-\(q\) cyclic
interval. Define the immutable canonical anchor histogram

\[
 \mu_q(S)=\#\{X:L_q(X)=S\},
 \qquad S\in\binom{[n]}r.
\tag{1.2}
\]

An arbitrary admissible history through depths \(1,\ldots,q-1\) changes the
second endpoint of some stage-\(q\) sibling edges, but it does not change
their canonical endpoints \(L_q(X)\). Orient the resulting labelled
multigraph at stage \(q\). Let

* \(O_q(S)\) be the number of toggled owner edges whose canonical anchor is
  \(S\);
* \(I_q(S)\) be the number of toggled owner edges whose chosen alternate
  endpoint is \(S\);
* \(T_q=\sum_SO_q(S)=\sum_SI_q(S)\).

The final load is exactly

\[
 b_q(S)=\mu_q(S)-O_q(S)+I_q(S).
\tag{1.3}
\]

A balanced orientation has

\[
 b_q(S)=c_q+\mathbf1_{H_q}(S)
\tag{1.4}
\]

for one genuine set
\(H_q\subseteq\binom{[n]}r\) of cardinality \(|H_q|=\rho_q\). The
cardinality is forced by summing (1.4) and using (1.1).

All counts above include labelled edge multiplicity. Parallel sibling edges
cause no ambiguity.

## 2. Floor-exact two-sided anchor-transport theorem

Define

\[
 D_q^-(F)=\sum_S(c_q-\mu_q(S))_+,
 \qquad
 D_q^+(F)=\sum_S(\mu_q(S)-c_q-1)_+.
\tag{2.1}
\]

The two quantities measure, respectively, total canonical mass missing
below the exact floor and total canonical mass exceeding the exact ceiling.

### Theorem 2.1 -- exact balanced-histogram distance

For every integer histogram \(\mu\ge0\) on \(N\) cells with total mass
\(W=cN+\rho\), \(0\le\rho<N\),

\[
 \boxed{
 \min_{\substack{H\subseteq[N]\\|H|=\rho}}
 \frac12\left\|\mu-(c\mathbf1+\mathbf1_H)\right\|_1
 =
 \max\left\{
 \sum_S(c-\mu(S))_+,\
 \sum_S(\mu(S)-c-1)_+
 \right\}.}
\tag{2.2}
\]

Consequently, for every exact factor, every stage, every admissible earlier
history, and every balanced supported orientation,

\[
 \boxed{T_q\ge\max\{D_q^-(F),D_q^+(F)\}.}
\tag{2.3}
\]

If no balanced supported orientation exists, set \(T_q=+\infty\), and the
statement remains valid.

#### Proof

For a proposed high family \(H\), set

\[
 d(H)=\sum_S(c+\mathbf1_H(S)-\mu(S))_+.
\]

Starting from \(H=\varnothing\), declaring \(S\) high increases its
contribution to \(d(H)\) by exactly one when \(\mu(S)\le c\), and by zero
when \(\mu(S)\ge c+1\). If

\[
 h=\#\{S:\mu(S)\ge c+1\},
 \qquad
 D^- =\sum_S(c-\mu(S))_+,
\]

then choosing \(\rho\) high cells optimally gives

\[
 \min_{|H|=\rho}d(H)=D^-+(\rho-h)_+.
\tag{2.4}
\]

On the other hand, the exact mass identity

\[
 \sum_S(\mu(S)-c)=\rho
\]

gives

\[
 \rho=h+D^+-D^-,
 \qquad
 D^+=\sum_S(\mu(S)-c-1)_+.
\tag{2.5}
\]

Substituting (2.5) into (2.4) yields

\[
 \min_{|H|=\rho}d(H)
 =D^-+(D^+-D^-)_+
 =\max(D^-,D^+).
\tag{2.6}
\]

The proposed balanced histogram and \(\mu\) have equal total mass, so its
total positive deficit equals its total positive excess. Hence this common
quantity is half their \(\ell^1\) distance, proving (2.2).

For a supported orientation, (1.3) gives

\[
 \|b_q-\mu_q\|_1
 \le \|O_q\|_1+\|I_q\|_1=2T_q.
\]

Apply (2.2) to the actual balanced histogram \(b_q\). This proves (2.3).
\(\square\)

### Sharpness and limitation

Equality in (2.2) concerns only unconstrained histogram transport. It does
not assert equality in (2.3): the owner graph may not support a minimizing
transport, a minimizing high family may fail Hall, and cycle or component
constraints may force strictly more toggles. Thus (2.3) is a universal
lower bound, not an orientation construction.

### Corollary 2.2 -- fixed-window necessary condition

For fixed \(A>0\), let \(K_A=\lceil A\sqrt m\rceil\). Every balanced
one-pass history satisfies

\[
 \sum_{q\le K_A}\frac{T_q}{c_q}
 \ge
 \sum_{q\le K_A}
 \frac{\max\{D_q^-(F),D_q^+(F)\}}{c_q}.
\tag{2.7}
\]

Therefore \(\mathrm{AO}_A/\mathrm{SDH}_A\) on a chosen factor requires the
right side of (2.7) to be \(o(W)\). No adaptive choice at an earlier depth
can reduce these factor-determined terms.

## 3. Exact containment-star consequence

Let \(T\subseteq[n]\), \(|T|=t\le r\), and let

\[
 U_T=\left\{S\in\binom{[n]}r:T\subseteq S\right\},
 \qquad
 u_{q,t}=|U_T|=\binom{n-t}{r-t}.
\]

Write

\[
 M_q^F(T)=\sum_{S\in U_T}\mu_q(S),
 \qquad
 h_q(T)=|H_q\cap U_T|.
\]

Summing (1.3) on \(U_T\) gives the exact two-sided discrepancy bound

\[
 \boxed{
 \left|M_q^F(T)-c_qu_{q,t}-h_q(T)\right|\le T_q.}
\tag{3.1}
\]

Indeed, the difference is \(O_q(U_T)-I_q(U_T)\), whose absolute value is
at most \(T_q\). The complementary star has the same absolute histogram
discrepancy, because both histograms have total mass \(W\).

At an exact quota wall \(\rho_q=0\), the high family is forced to be empty,
and (3.1) reduces to

\[
 \left|M_q^F(T)-c_qu_{q,t}\right|\le T_q.
\tag{3.2}
\]

This makes precise which part of two-sided containment-star control can be
altered by orientation: toggles transport load, but neither earlier carries
nor current orientations change the canonical count \(M_q^F(T)\).

Equation (3.1) is necessary, not sufficient for supported simultaneous
Hall feasibility. In particular, it does not replace the internal-edge and
incident-edge Hall inequalities.

### Theorem 3.1 -- the first three bounded-order stars do not cause the depth-one failure

At \(q=1\), let \(\iota_1(T)\) be the number of owner edges internal to
\(U_T\), and let \(\eta_1(T)\) be the number of owner edges incident with
\(U_T\). With the high cells free to be chosen, the exact largest and
smallest quota masses on \(U_T\) are

\[
 \mathcal C^+(U_T)=u_{1,t}+\min\{u_{1,t},\rho_1\},
 \qquad
 \mathcal C^-(U_T)=u_{1,t}.
\tag{3.3}
\]

For every exact cyclic factor and every \(T\), both Hall rows

\[
 \iota_1(T)\le\mathcal C^+(U_T),
 \qquad
 \eta_1(T)\ge\mathcal C^-(U_T)
\tag{3.4}
\]

hold

* for \(t=1,2\) and every \(m\ge3\);
* for \(t=3\) and every \(m\ge21\).

The internal row alone is safe for \(t=1,2,3\) for every applicable
\(m\ge3\).

#### Proof

Put \(N=N_1\), \(u=u_{1,t}\), and

\[
 \alpha_t=\frac uN=\frac{(m-1)_t}{(2m+1)_t}.
\]

By (4.1) below, \(\rho_1/N=2/m\). Since

\[
 \alpha_t\le\alpha_1=\frac{m-1}{2m+1}
 \le1-\frac2m
 \qquad(m\ge3),
\]

the exact minimum-quota formula gives \(\mathcal C^-=u\). The maximum
formula is \(u+\min(u,\rho_1)\); it is important not to replace it
uniformly by \(u+\rho_1\).

The exact cyclic-residence chord bound at \(q=1\) is

\[
 \iota_1(T)
 \le
 \binom{n-t}{m-t}\frac{m-t-1}{m-t+1},
\tag{3.5}
\]

with the zero boundary cases read directly. Dividing by \(u\), the excess
above \(u\) is controlled by

\[
 \frac{\iota_1(T)}u-1
 \le
 \frac{t(m-t-1)-2}{(m-t)(m-t+1)}.
\tag{3.6}
\]

For \(t=1,2,3\), (3.6) is at most one; equivalently the three gaps in the
inequality \(\iota_1(T)\le2u\) reduce to positive polynomials

\[
 m^2-2m+4,\quad m^2-5m+10,\quad (m-4)^2+4.
\]

The other required comparison is \(\iota_1(T)\le u+\rho_1\). Writing
\(B=W/n\), exact simplification of (3.5) gives

\[
 \iota_1(T)-u
 \le
 \begin{cases}
 B(m-4)/(m+2),&t=1,2,\\[2mm]
 B(m-1)(3m-14)/(2(2m-1)(m+2)),&t=3,
 \end{cases}
\tag{3.7}
\]

whereas

\[
 \rho_1=\frac{2(2m+1)}{m+2}B.
\]

The right sides of (3.7) are at most \(\rho_1\) in all applicable cases.
Thus \(\iota_1(T)\le\min(2u,u+\rho_1)=\mathcal C^+\).

For the incident row, at \(q=1\) the owner-edge union is its middle owner
\(X\). Hence

\[
 \eta_1(T)=A_t-\Sigma_t,
 \qquad
 A_t=\binom{n-t}{m-t},
\tag{3.8}
\]

where \(\Sigma_t\) counts owners whose two difference labels lie in
\(T\) and whose residual \(T\)-labels lie in the core. Exact cyclic
geometry gives

\[
 \Sigma_1=0,\quad
 \Sigma_2\le B/2,\quad
 \Sigma_3\le B.
\tag{3.9}
\]

For \(t=2\), every counted row makes the fixed pair adjacent and contributes
\(m-1\) to its residence; the exact pair-residence total is
\((m-1)B/2\). For \(t=3\), two candidate adjacent difference pairs would
force a cyclic consecutive triple, and only one has the third point in the
consistently oriented core, so there is at most one counted owner per row.

Finally,

\[
 A_t-u
 =\begin{cases}
 3mB/(m+2),&t=1,\\[1mm]
 2(m-1)B/(m+2),&t=2,\\[1mm]
 5(m-1)(m-2)B/(2(m+2)(2m-1)),&t=3.
 \end{cases}
\tag{3.10}
\]

The first two quantities dominate the corresponding bounds in (3.9) for
\(m\ge3\). The third dominates \(B\) exactly when

\[
 m^2-21m+14\ge0,
\]

which holds for every integer \(m\ge21\). Equations (3.8)--(3.10) prove
the incident row and the theorem. \(\square\)

This theorem was independently rederived with the exact maximum/minimum
quota capacities. Its scope is only the displayed star and complementary-
star cuts; it does not prove all Hall cuts or produce a balanced
orientation. In particular, the linear MSW obstruction below is a
high-order singleton-star/floor obstruction, not a hidden failure of the
bounded-order rows in Theorem 3.1.

### Theorem 3.2 -- exact adaptive high-family corridor

Fix a stage \(q\), a \(t\)-set \(T\), and abbreviate

\[
 M=\binom{n-t}{m-q-t},
 \qquad
 M'=\binom{n-t}{m-q+1-t}.
\tag{3.11}
\]

For owner edge \(X\), let \(C_X\) be its rank-\((m-q-1)\) core and let
\(p_X\) be its two difference labels. Put

\[
 \Sigma_q(T)=
 \#\{X:p_X\subseteq T,\ T\setminus p_X\subseteq C_X\}.
\tag{3.12}
\]

Along every balanced adaptive history, the high-family containment counts
must satisfy the exact coordinatewise corridor

\[
 \boxed{
 \begin{aligned}
 \max\{&0,\ \rho_q-(N_q-M),\ M_{q+1}^F(T)-c_qM\}
 \le h_q(T)\\
 \le\min\{&M,\ \rho_q,\
 c_{q-1}M'+h_{q-1}(T)-\Sigma_q(T)-c_qM\}.
 \end{aligned}}
\tag{3.13}
\]

Here at \(q=1\) the preceding middle layer has \(c_0=1\), \(\rho_0=0\),
and \(h_0(T)=0\).

#### Proof

The first two lower bounds and first two upper bounds in (3.13) are the
cardinality bounds for a \(\rho_q\)-set inside a universe of size \(N_q\)
and a star of size \(M\). The internal Hall row is

\[
 M_{q+1}^F(T)\le c_qM+h_q(T),
\]

which gives the third lower bound.

The union histogram of the evolving stage-\(q\) sibling graph is exactly
the preceding balanced load. An edge is incident with \(U_T\) unless its
union contains \(T\) but its two difference labels split \(T\) between the
two endpoints. Therefore

\[
 \eta_q(T)
 =c_{q-1}M'+h_{q-1}(T)-\Sigma_q(T).
\tag{3.14}
\]

The complementary Hall row \(\eta_q(T)\ge c_qM+h_q(T)\) is precisely the
third upper bound. \(\square\)

The corridor is coordinatewise necessary, not simultaneously sufficient:
one set \(H_q\) must realize all the integers \(h_q(T)\), and then the
owner graph must support the resulting quota.

A particularly clean sufficient star certificate would be

\[
 h_q(T)=M_q^F(T)-c_qM
 \qquad(1\le|T|\le t_*).
\tag{3.15}
\]

It makes the quota mass of every selected star equal to its canonical
anchor mass. Since every internal edge has its canonical anchor in the
star and every canonical anchor in the star supplies an incident edge,

\[
 \iota_q(T)\le M_q^F(T)=b_q(U_T)\le\eta_q(T)
\]

for every earlier history. A simple high family satisfying (3.15) always
exists for \(t_*=1\): exact point homomesy makes the required high degree

\[
 \frac{(m-q)\rho_q}{n}
\]

an integer: with \(r=m-q\),

\[
 \frac{r\rho_q}{n}
 =rB-c_q\binom{n-1}{r-1}.
\]

To see existence without importing a design theorem, choose a
\(\rho_q\)-subfamily \(H\) of the complete \(r\)-layer minimizing
\(\sum_x d_H(x)^2\). If \(d_H(x)\ge d_H(y)+2\), some edge containing
\(x\) and not \(y\) can be switched from \(x\) to \(y\) without creating
a duplicate: otherwise the switch map would inject the larger difference
family \(H_x\setminus H_y\) into the smaller family
\(H_y\setminus H_x\). This switch strictly decreases the squared-degree
sum. Hence all degrees differ by at most one; their integral average forces
equality. This point-level quota need not be orientable.

For \(t_*\ge2\), existence of one simple high family with the prescribed
moments is an unresolved integral moment-fibre problem. Exact design
rounding cannot be imposed universally. For example, at \(q=1\), if \(m\)
is an odd prime, a pair-regular high family would have the forced pair
degree

\[
 \frac{B(m-1)(m-2)}{m(m+2)},
\tag{3.16}
\]

which is nonintegral. Indeed, modulo the prime \(m\),

\[
 \binom{2m}{m}
 =2\prod_{j=1}^{m-1}\frac{m+j}{j}
 \equiv2,
 \qquad
 B=\frac1{m+1}\binom{2m}{m}\equiv2.
\]

Thus the numerator in (3.16) is
\(2(-1)(-2)=4\not\equiv0\pmod m\). Small discrepancy, rather than exact design
moments, is therefore indispensable in any positive higher-order
construction.

## 4. Depth one: every lower-shadow hole costs one toggle

Assume \(m\ge3\). At \(q=1\),

\[
 N_1=\binom{2m+1}{m-1}=\frac{m}{m+2}W,
\]

so the exact division is

\[
 \lambda_1=\frac W{N_1}=\frac{m+2}{m},
 \qquad
 c_1=1,
 \qquad
 \rho_1=W-N_1=\frac{2W}{m+2}.
\tag{4.1}
\]

Define the canonical first-shadow hole count

\[
 M_1(F)=\#\left\{
 S\in\binom{[n]}{m-1}:\mu_1(S)=0
 \right\}.
\tag{4.2}
\]

### Corollary 4.1 -- exact hole-recourse inequality

Every balanced stage-one orientation of every exact factor satisfies

\[
 \boxed{T_1(F)\ge M_1(F).}
\tag{4.3}
\]

#### Proof

Since \(c_1=1\), the lower-defect term in (2.1) is exactly

\[
 D_1^-(F)=\sum_S(1-\mu_1(S))_+=M_1(F).
\]

Now apply (2.3). Equivalently, if \(S\) is a hole, no toggled edge can
leave its canonical anchor, while balancedness requires final load at least
one. Thus at least one toggled edge must enter \(S\). A labelled toggle has
only one alternate endpoint, so one toggle cannot fill two different holes.
\(\square\)

For every fixed \(A>0\), depth one belongs to the window
\(1\le q\le K_A\). Because \(c_1=1\), both the weighted and unweighted
fixed-window costs obey

\[
 \sum_{q\le K_A}T_q\ge T_1\ge M_1(F),
 \qquad
 \sum_{q\le K_A}\frac{T_q}{c_q}\ge T_1\ge M_1(F).
\tag{4.4}
\]

Stage one has no preceding carry state. Later choices cannot refund a
stage-one toggle in either cost.

## 5. Audited MSW marked-gap input

The independently audited contextual insertion--erasure theorem for the
canonical MSW factor supplies

\[
 \Gamma_m=(2m-3)\operatorname{Cat}_{m-2}
\tag{5.1}
\]

distinct marked-gap certificate pairs with disjoint pointed slots. The full
proof, including the contextual induction and distinctness recovery, is in
`MATH_ATTACK_I_MARKED_GAP_COLLISION_INDEPENDENT_AUDIT_20260725.md`.

For completeness, the exact counting implication is short. Put

\[
 C_1(F)=\sum_S(\mu_1(S)-1)_+.
\tag{5.2}
\]

If a target has multiplicity \(j\), disjoint pointed slots support at most
\(\lfloor j/2\rfloor\) certificate pairs there. Hence

\[
 \Gamma_m
 \le\sum_S\left\lfloor\frac{\mu_1(S)}2\right\rfloor
 \le C_1(F_m^{\rm MSW}).
\tag{5.3}
\]

Since \(\sum_S\mu_1(S)=W\) and exactly \(N_1-M_1\) cells are nonempty,

\[
 C_1(F)=W-(N_1-M_1(F))
 =\rho_1+M_1(F).
\tag{5.4}
\]

Equations (5.3), (5.4), and (4.1) give the exact audited bound

\[
 \boxed{
 M_1(F_m^{\rm MSW})
 \ge
 \left[
 \Gamma_m-\frac{2W}{m+2}
 \right]_+.}
\tag{5.5}
\]

No probabilistic estimate or finite-data assertion enters (5.5).

## 6. Linear MSW recourse theorem

### Theorem 6.1 -- canonical MSW is linearly far from every balanced first step

For \(m\ge3\), every balanced stage-one adjacent-deletion orientation of
the canonical MSW exact factor satisfies

\[
 \boxed{
 T_1(F_m^{\rm MSW})
 \ge
 \left[
 (2m-3)\operatorname{Cat}_{m-2}
 -\frac{2W}{m+2}
 \right]_+.}
\tag{6.1}
\]

Furthermore,

\[
 \frac{(2m-3)\operatorname{Cat}_{m-2}}W
 =\frac{m(m+1)}{4(2m-1)(2m+1)},
\tag{6.2}
\]

and therefore

\[
 \boxed{T_1(F_m^{\rm MSW})\ge(1/16-o(1))W.}
\tag{6.3}
\]

For every fixed \(A>0\), every balanced one-pass MSW history consequently
satisfies

\[
 \liminf_{m\to\infty}
 \frac1W\sum_{q\le K_A}\frac{T_q}{c_q}
 \ge\frac1{16}.
\tag{6.4}
\]

#### Proof

Combine (4.3) and (5.5). To verify the constant, use

\[
 \operatorname{Cat}_{m-2}
 =\frac1{m-1}\binom{2m-4}{m-2}
\]

and cancel factorials against \(W=\binom{2m+1}{m}\); this gives (6.2).
Its limit is \(1/16\), while \(2/(m+2)\to0\). Equation (4.4) then gives
(6.4). \(\square\)

This is strictly stronger than the earlier seed-triple estimate
\(T_1\ge(275/38642+o(1))W/m\). The earlier estimate remains correct, but
is asymptotically superseded for MSW by (6.3).

## 7. Stability under exact-factor row replacement

Let \(F'\) be any exact cyclic factor, and let

\[
 b=\frac12\left|F'\triangle F_m^{\rm MSW}\right|
\tag{7.1}
\]

be its unpointed wreath-row distance from MSW. Thus exactly \(b\) canonical
MSW rows are absent from \(F'\).

The audited marked-gap stability theorem states that one removed canonical
row destroys at most \(m-1\) of the disjoint-slot certificates. Therefore

\[
 C_1(F')\ge\left[\Gamma_m-(m-1)b\right]_+.
\tag{7.2}
\]

Using the universal identity (5.4) and then (4.3) gives the exact robust
bound

\[
 \boxed{
 T_1(F')\ge
 \left[
 (2m-3)\operatorname{Cat}_{m-2}
 -(m-1)b
 -\frac{2W}{m+2}
 \right]_+.}
\tag{7.3}
\]

### Corollary 7.1 -- sharp asymptotic exclusion radius supplied by the certificate

If a sequence \(F'_m\) admits balanced stage-one orientations with
\(T_1(F'_m)=o(W)\), then necessarily

\[
 \boxed{
 b_m\ge(1/8-o(1))\operatorname{Cat}_m.}
\tag{7.4}
\]

More quantitatively, for every fixed \(\varepsilon>0\),

\[
 b_m\le(1/8-\varepsilon)\operatorname{Cat}_m
 \quad\Longrightarrow\quad
 \boxed{T_1(F'_m)\ge(\varepsilon/2-o(1))W.}
\tag{7.5}
\]

#### Proof

Divide (7.3) by \(W=(2m+1)\operatorname{Cat}_m\). If
\(b\le(1/8-\varepsilon)\operatorname{Cat}_m\), its right side divided by
\(W\) is at least

\[
 \frac{m(m+1)}{4(2m-1)(2m+1)}
 -\frac{2}{m+2}
 -\frac{m-1}{2m+1}(1/8-\varepsilon),
\]

which tends to \(\varepsilon/2\). This proves (7.5). Rearranging (7.3)
under \(T_1=o(W)\) gives (7.4). \(\square\)

The constant \(1/8\) is the exact asymptotic radius delivered by the
audited marked-gap certificate degree bound \(m-1\). No optimality among
all possible stability certificates is asserted.

## 8. Phase, reversal, and adaptive-history audit

The decisive step has three possible escape routes; none applies.

1. **Cyclic phase.** Rotating a wreath changes only its chosen written
   starting point. Its multiset of cyclic \((m-1)\)-interval anchors is
   unchanged.
2. **Reversal.** Reversing a wreath permutes the same multiset of cyclic
   \((m-1)\)-interval anchors. Hence \(\mu_1\), its holes, and (4.3) are
   reversal-invariant.
3. **Earlier history.** There is no earlier state at \(q=1\). At later
   stages, earlier carries rewire only alternate endpoints; Theorem 2.1
   already allows arbitrary such rewiring and uses only the invariant
   canonical anchors.

Thus the linear lower bound concerns one exact cyclic factor together with
every legal one-pass history on it. It is not an artifact of a pointed
representative.

The decisive inference \(T_1\ge M_1\), its constants, and the row-edit
asymptotics were independently rederived after this report was drafted.
The independent audit found only the necessary standing restriction
\(m\ge3\), already imposed above; at \(m=2\), \(c_1=2\).

## 9. Precise proved/conditional boundary

### Proved

1. The exact floor/ceiling transport identity (2.2) for every integer
   histogram and every exact remainder \(\rho_q\).
2. The history-robust supported-orientation lower bound (2.3) at every
   depth of every exact cyclic factor.
3. The exact two-sided containment-star discrepancy inequality (3.1).
4. The exact adaptive high-family corridor (3.13), including every earlier
   balanced state through \(h_{q-1}\) and the split-pair loss \(\Sigma_q\).
5. Existence of a point-regular high-quota family at every depth, together
   with the exact pair-design divisibility obstruction (3.16).
6. The exact depth-one star and complementary-star Hall safety theorem for
   orders \(t=1,2\), and for order \(t=3\) once \(m\ge21\).
7. The universal stage-one hole inequality \(T_1(F)\ge M_1(F)\).
8. The linear MSW lower bound (6.1)--(6.4).
9. The row-edit stability bound (7.3), the \(1/8\) necessary escape radius,
   and the quantitative \(\varepsilon/2\) cost inside that radius.

### Not proved

1. Existence of a distant exact factor for which all depths admit
   simultaneous balanced orientations with total cost \(o(W)\).
2. A counterexample applying to every exact factor. A factor-specific bad
   example, even one with linear cost, does not refute existential
   \(\mathrm{AO}_A/\mathrm{SDH}_A\).
3. Sufficiency of the histogram conditions (2.3) or the star conditions
   (3.1) for Hall feasibility or short supported transport.
4. Simultaneous simple-family realization of the higher-order moment
   corridors (3.13), even before owner-edge support is imposed.
5. A bounded-order containment-star obstruction: the MSW application sums
   singleton stars \(U_S=\{S\}\), equivalently order \(t=r=m-1\), rather
   than one fixed-order star. Theorem 3.1 in fact proves that the first
   three bounded orders are safe at depth one in its stated ranges.
6. Any obstruction to upper-capacity-only unlabelled MWB. The linear bound
   uses the lower pointwise floor \(b_1(S)\ge1\), and is decisive precisely
   for the two-sided balanced AO/SDH gate.
7. The sharp constant-one contiguous-OR theorem.

No unproved lemma is used in the proved statements. The marked-gap input is
the completed and independently audited theorem cited in Section 5.
