# Exact additive-renewal formulas for the PBBS \(ST_A\) start process

Date: 2026-07-26

Method: pure mathematics only.  No computation, experiment, random
occupancy model, or external input is used.

## 0. Result and scope

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,
 \qquad G=2H-1.
\]

Let \(\phi\) be the one-step rooted-Dyck PBBS map and
\(\tau=\phi^2\).  Let \(E_H\) be the normalized rank-\(m\) roots on
parent \(\tau\)-cycles longer than \(H+1\) whose omitted physical label
has its first return by time \(G\).  Define

\[
 R_H=|E_H|,
 \qquad
 \mathcal C_H=\sum_{u=1}^{H+1}
       |E_H\cap\tau^{-u}E_H|.
 \tag{0.1}
\]

This note derives two exact, equivalent formulas for both quantities.

* The first is an additive positive-increment renewal formula on the
  literal two-step PBBS orbit.
* The second is a coefficient-exact Pascal formula after simultaneous
  peak deletion.  It includes the actual two-time fibre transport rather
  than an independent coupling.

The formulas prove the following rigorous conclusions.

1. If

   \[
      {H R_H\over B_m}\longrightarrow\infty,
   \]

   then

   \[
      \boxed{\mathcal C_H/R_H\longrightarrow\infty.}
   \]

   This follows from the exact Fejér-window inequality.  It does not
   decide the critical regime \(R_H=\Theta(B_m/H)\).

2. There is a complete genuine zero-winding PBBS sector at the Gaussian
   scale for which

   \[
      H{R_H^{\rm mt}\over|\Omega_{m,h}|}\longrightarrow2Ac,
      \qquad
      {\mathcal C_H^{\rm mt}\over R_H^{\rm mt}}
        \longrightarrow2Ac,
      \qquad {A\over2}<c<A.
   \tag{0.2}
   \]

   Thus critical one-point density does **not** force divergent
   susceptibility in every genuine PBBS invariant fibre.  This refutes a
   fibrewise or uniform additive-renewal compiler theorem.

3. The mountain sector has only

   \[
       |\Omega_{m,h}|=exp(O(\sqrt m\log m))
       =o(B_m/H)
   \]

   roots.  Therefore (0.2) does not refute global \(ST_A\).  A global
   bounded-ratio refutation still requires the same behaviour on
   Pascal-saddle cores of total weight \(\Omega(B_m/H)\).

4. At that saddle, the parent Pascal fibre is two-time neutral.  One
   active reduced phase retains at least \(3/4-o(1)\) of its fibre and
   two active phases retain at least \(1/2-o(1)\) jointly.  Hence the
   exact unresolved quantity is the Pascal-weighted autocorrelation of
   the reduced predecessor-active phases, not a missing outer-fibre
   factor.

Accordingly, the global requested dichotomy is not decided.  The exact
renewal identities prove supercritical divergence and a sharp genuine
bounded-ratio local obstruction, but neither a global divergent ratio nor
a Catalan-critical bounded-ratio lower bound is presently justified.

## 1. The literal positive-increment renewal

For a normalized Dyck root \(D\), use the canonical first-maximum
factorization

\[
 D=P,1,R,0,S.
 \tag{1.1}
\]

The displayed one is the first up-step which reaches the global maximum,
and the displayed zero is the first subsequent return to height zero.
Put

\[
 a(D)=|P|+1=\delta(D),
 \qquad
 c(D)=|S|+1=d(D),
 \qquad
 \widehat c(D)=d(\phi D).
 \tag{1.2}
\]

Let

\[
 D_j=\tau^jD,
 \qquad
 a_j=a(D_j),
 \qquad
 c_j=c(D_j),
 \qquad
 \widehat c_j=\widehat c(D_j).
 \tag{1.3}
\]

### Lemma 1.1 (two positive telescopes)

For every \(j\),

\[
 \boxed{a_{j+1}-a_j=c_j-\widehat c_j.}
 \tag{1.4}
\]

Consequently, for every \(s\ge1\),

\[
 \boxed{
  \sum_{j=0}^{s-1}c_j-a_s
  =\sum_{j=0}^{s-1}\widehat c_j-a_0.}
 \tag{1.5}
\]

#### Proof

Put \(b_j=\delta(\phi D_j)\).  The exact first-maximum block identities
give

\[
 a_j+b_j+c_j=N,
 \qquad
 b_j+a_{j+1}+\widehat c_j=N.
\]

Subtract the two equations to obtain (1.4), and sum (1.4) from
\(j=0\) to \(s-1\) to obtain (1.5). \(\square\)

Both \(c_j\) and \(\widehat c_j\) are positive odd integers.  Thus the
right side of (1.5) is a genuine positive-increment renewal process
started at level \(-a_0\).

### Theorem 1.2 (exact return-start time)

Define

\[
 \sigma(D)=\min\left\{s\ge1:
   \sum_{j=0}^{s-1}\widehat c(\tau^jD)
       \in a(D)+N\mathbb Z_{\ge0}\right\}.
 \tag{1.6}
\]

Then the first positive return gap of the omitted physical label at
\(D\) is

\[
 \boxed{g(D)=2\sigma(D)+1.}
 \tag{1.7}
\]

Equivalently, if the return has two-step winding \(w\ge0\), then

\[
 \boxed{
 \sum_{j=0}^{\sigma(D)-1}c_j
     =a_{\sigma(D)}+wN,
 \qquad
 \sum_{j=0}^{\sigma(D)-1}\widehat c_j
     =a_0+wN.}
 \tag{1.8}
\]

No smaller positive prefix satisfies either congruence.

#### Proof

The exact even-time skew product moves the physical root by
\(-c_j\pmod N\) during the \(j\)-th two-step update.  The final odd
update at phase \(s\) moves it by \(a_s\).  Thus the initial omitted
coordinate returns after \(2s+1\) steps exactly when

\[
 \sum_{j=0}^{s-1}c_j-a_s\in N\mathbb Z.
\]

The integer multiple is nonnegative because all quantities in the first
equation of (1.8) are positive.  Equation (1.5) gives the second form.
Taking the least positive \(s\) proves firstness and (1.6)--(1.8).
\(\square\)

Define the exact horizon indicator

\[
 \chi_H(D)=\mathbf1\{\sigma(D)\le H-1\}.
 \tag{1.9}
\]

Before deleting short parent cycles, the one- and two-time statistics are
therefore

\[
 \boxed{
 \widetilde R_H=\sum_{D\in\mathcal D_m}\chi_H(D),}
 \tag{1.10}
\]

\[
 \boxed{
 \widetilde{\mathcal C}_H
 =\sum_{u=1}^{H+1}\sum_{D\in\mathcal D_m}
     \chi_H(D)\chi_H(\tau^uD).}
 \tag{1.11}
\]

For complete explicitness, the second indicator in (1.11) is the shifted
renewal test

\[
 \chi_H(\tau^uD)
 =\mathbf1\left\{
 \min\left{s\ge1:
  \sum_{j=u}^{u+s-1}\widehat c_j
       \in a_u+N\mathbb Z_{\ge0}\right\}
 \le H-1\right\}.
 \tag{1.12}
\]

Thus \(\mathcal C_H\) uses two windows of the same deterministic renewal
sequence.  Replacing the two windows by independent copies changes the
problem.

If \(Z_H\) is the number of parent roots on \(\tau\)-cycles of length at
most \(H+1\), the voltage-itinerary bound gives

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(O_A(\sqrt m\log m)).
 \tag{1.13}
\]

Since the short-cycle set is \(\tau\)-invariant,

\[
 |R_H-\widetilde R_H|\le Z_H,
 \qquad
 |\mathcal C_H-\widetilde{\mathcal C}_H|
     \le(H+1)Z_H.
 \tag{1.14}
\]

Both errors are \(o(B_m/H)\).

## 2. Exact peak-deletion census for \(R_H\)

Let \(F=\partial D\in\mathcal D_d\) be the simultaneous peak deletion
of a nonexceptional parent root and put

\[
 k=\operatorname {pk}(F),
 \qquad
 p=2d+1,
 \qquad
 y=m-d-k.
 \tag{2.1}
\]

After one compulsory new leaf is assigned at each old leaf, the inverse
fibre is the weak-composition simplex

\[
 \Omega_m(F)=\left\{x=(x_0,\ldots,x_{p-1})in
     \mathbb Z_{\ge0}^{p}:\sum_ix_i=y\right\}.
 \tag{2.2}
\]

Hence

\[
 \boxed{
 P_m(F)=|\Omega_m(F)|
 =\binom{y+p-1}{p-1}
 =\binom{m+d-k}{2d}.}
 \tag{2.3}
\]

In the reduced equality-particle PBBS at \(F\), let

\[
 0<B_1(F)<B_2(F)<\cdots
\]

be the positive selection times of the immediate predecessor of the
time-zero selected particle.  If \(x_0\) is the terminal free occupancy,
the exact no-overtaking theorem gives

\[
 \boxed{g(D)=B_{2x_0+2}(F)}
 \tag{2.4}
\]

whenever this time is below \(N\), as it is in the present horizon.

Put

\[
 A_H(F)=\max\{a\ge0:B_{2a+2}(F)\le G\},
 \tag{2.5}
\]

with value \(-1\) when the set is empty.  Define, for \(a\ge0\),

\[
 U_{y,p}(a)
 =\binom{y+p-1}{p-1}
  -\binom{y-a+p-2}{p-1},
 \tag{2.6}
\]

using the binomial-zero convention, and put \(U_{y,p}(-1)=0\).
Then

\[
 U_{y,p}(a)
 =\#\{x\in\Omega_m(F):x_0\le a\}.
\]

### Theorem 2.1 (exact one-time Pascal renewal formula)

\[
 \boxed{
 \widetilde R_H
 =\epsilon_m(H)+
   \sum_{d=1}^{m-1}
   \sum_{\substack{F\in\mathcal D_d\\
                    d+\operatorname {pk}(F)\le m}}
       U_{m-d-\operatorname {pk}(F),\,2d+1}
        \bigl(A_H(F)\bigr),}
 \tag{2.7}
\]

where \(\epsilon_m(H)\in\{0,1\}\) is the completely pruned exception.

Equivalently, expanding (2.6),

\[
 \boxed{
 \widetilde R_H=\epsilon_m(H)+
 \sum_{\substack{d,F\\d+\operatorname {pk}(F)\le m}}
 \sum_{a\ge0}
 \mathbf1_{\{B_{2a+2}(F)\le G\}}
 \binom{m+d-\operatorname {pk}(F)-a-1}{2d-1}.}
 \tag{2.8}
\]

#### Proof

Equation (2.4) says that precisely the occupancies
\(0\le x_0\le A_H(F)\) are eligible.  Counting the remaining free
coordinates proves (2.7).  Splitting according to the exact value
\(x_0=a\) gives (2.8). \(\square\)

The reduced support of the census is the literal predecessor-active set

\[
 \mathscr A_H(d,k)
 =\{F\in\mathcal D_d:\operatorname {pk}(F)=k,
                         B_2(F)\le G\}.
 \tag{2.9}
\]

Every active core contributes at least its terminal-zero hyperplane

\[
 K_0(d,k)=\binom{m+d-k-1}{2d-1},
 \qquad
 {K_0(d,k)\over P_m(d,k)}={2d\over m+d-k}.
 \tag{2.10}
\]

## 3. Actual fibre transport is a Pascal-coordinate permutation

The next lemma makes the two-time formula coefficient-exact.

### Lemma 3.1 (free-gap transport)

Fix a reduced root \(F\) and a phase \(u\).  There is a permutation

\[
 \pi_{F,u}:\{0,1,\ldots,2d\}\longrightarrow
              \{0,1,\ldots,2d\}
 \tag{3.1}
\]

such that, under the actual parent PBBS fibre bijection

\[
 \Sigma_F^{(u)}:\Omega_m(F)\longrightarrow
                  \Omega_m(\tau_d^uF),
\]

the free-slot vector satisfies

\[
 \boxed{x'_j=x_{\pi_{F,u}(j)}.}
 \tag{3.2}
\]

In particular, if \(i_u(F)=\pi_{F,u}(0)\), then the terminal free
occupancy at phase \(u\), pulled back to the initial fibre, is exactly

\[
 \boxed{x_{i_u(F)}.}
 \tag{3.3}
\]

#### Proof

Equality particles preserve their cyclic identity order.  Their selected
identity word is the PBBS word of the reduced core and is independent of
the free inserted-leaf multiplicities.  In one ordered gap, adding
\(x_i\) free peaks increases the physical separation of the corresponding
adjacent persistent equality particles by exactly \(2x_i\).  During PBBS
evolution both adjacent particles receive selection counts determined
only by the core itinerary.  Hence, after the compulsory contribution at
the new core phase is subtracted, every output free coordinate has the
form

\[
 x'_j=x_{\rho(j)}+\beta_j,
\]

where \(\rho(j)\) is an adjacent persistent-particle gap and \(\beta_j\)
is independent of \(x\).

Assume first \(y>0\).  Every input coordinate can be zero in some weak
composition of \(y\).  Since every output coordinate is nonnegative,
\(\beta_j\ge0\).  Also

\[
 \sum_jx'_j=y=\sum_ix_i
\]

for every weak composition \(x\).  Varying the coordinate which carries
the free mass shows that every input coordinate occurs exactly once among
the \(\rho(j)\), while the constant terms obey \(\sum_j\beta_j=0\).
Thus all \(\beta_j=0\) and \(\rho\) is a permutation.  When \(y=0\),
both fibres consist of the single zero vector and the assertion is
immediate.  This proves (3.2)--(3.3). \(\square\)

Thus no independence hypothesis and no affine correction are required:
the holonomy can be a nontrivial permutation, but it preserves the exact
weak-composition coordinates.

## 4. Exact two-time Pascal formula for \(\mathcal C_H\)

For \(a,b\ge0\), define

\[
 V_{y,p}(a,b)
 =\binom{y+p-1}{p-1}
  -\binom{y-a+p-2}{p-1}
  -\binom{y-b+p-2}{p-1}
  +\binom{y-a-b+p-3}{p-1}.
 \tag{4.1}
\]

This is the exact number of weak compositions of \(y\) into \(p\)
parts satisfying \(x_i\le a\) and \(x_j\le b\) for two distinct
indices \(i\ne j\).  For the same index, the count is

\[
 U_{y,p}(\min\{a,b\}).
 \tag{4.2}
\]

Put both counts equal to zero if either cap is negative, and define

\[
 W_{y,p}(a,b;\varepsilon)
 =\begin{cases}
 U_{y,p}(\min\{a,b\}),&\varepsilon=1,\\
 V_{y,p}(a,b),&\varepsilon=0.
 \end{cases}
 \tag{4.3}
\]

### Theorem 4.1 (exact two-time census)

Before deleting short parent cycles,

\[
 \boxed{
 \widetilde{\mathcal C}_H
 =\sum_{u=1}^{H+1}\sum_{d=1}^{m-1}
   \sum_{\substack{F\in\mathcal D_d\\
                    d+\operatorname {pk}(F)\le m}}
   W_{y,p}\left(
       A_H(F),A_H(\tau_d^uF);
       \mathbf1_{\{i_u(F)=0\}}
       \right),}
 \tag{4.4}
\]

where \(y=m-d-\operatorname {pk}(F)\) and \(p=2d+1\).

#### Proof

At phase zero, (2.4)--(2.5) make eligibility the inequality
\(x_0\le A_H(F)\).  At phase \(u\), Lemma 3.1 pulls the terminal test
back to

\[
 x_{i_u(F)}\le A_H(\tau_d^uF).
\]

If the two indices agree, stars and bars gives (4.2); if they differ,
inclusion-exclusion gives (4.1).  Sum over every core and lag. \(\square\)

Equations (1.14), (2.7), and (4.4) are exact finite-rank formulas for the
requested retained statistics.

## 5. Saddle evaluation of the Pascal factors

The total inverse-fibre mass in the \((d,k)\) cell is

\[
 {1\over d}\binom dk\binom d{k-1}
       \binom{m+d-k}{2d}.
 \tag{5.1}
\]

Its unique entropy saddle is

\[
 d={m\over2}+O(\sqrt{m\log m}),
 \qquad
 k={m\over6}+O(\sqrt{m\log m}),
 \tag{5.2}
\]

and the total mass outside this tube is \(o(B_m/m)\).  In the tube,

\[
 p=(1+o(1))m,
 \qquad
 y=(1/3+o(1))m.
\]

For every fixed \(a\ge0\), direct division of binomial coefficients gives

\[
 {U_{y,p}(a)\over P_m(F)}
 =1-\prod_{j=0}^{a}{y-j\over y+p-1-j}
 =1-4^{-(a+1)}+o(1).
 \tag{5.3}
\]

For fixed \(a,b\ge0\) and distinct tested coordinates,

\[
 {V_{y,p}(a,b)\over P_m(F)}
 =\bigl(1-4^{-(a+1)}\bigr)
  \bigl(1-4^{-(b+1)}\bigr)+o(1).
 \tag{5.4}
\]

For the same coordinate the limit is

\[
 1-4^{-(\min(a,b)+1)}.
 \tag{5.5}
\]

In particular, two terminal-zero tests retain asymptotic fractions

\[
 \frac9{16}\quad\hbox{for distinct coordinates},
 \qquad
 \frac34\quad\hbox{for the same coordinate}.
 \tag{5.6}
\]

Without fixing the caps or coordinate relation, the deterministic
inclusion-exclusion bounds are

\[
 \left({3\over4}-o(1)\right)P_m(F)
 \le U_{y,p}(A_H(F))\le P_m(F)
 \tag{5.7}
\]

for every active phase, and

\[
 \left({1\over2}-o(1)\right)P_m(F)
 \le W_{y,p}(A_H(F),A_H(\tau^uF);\varepsilon)
 \le P_m(F)
 \tag{5.8}
\]

for every active phase pair.

Define

\[
 \mathscr R_H
 =\sum_{d,k}P_m(d,k)|\mathscr A_H(d,k)|,
 \tag{5.9}
\]

\[
 \mathscr C_H
 =\sum_{d,k}P_m(d,k)
   \sum_{u=1}^{H+1}
    |\mathscr A_H(d,k)\cap
       \tau_d^{-u}\mathscr A_H(d,k)|.
 \tag{5.10}
\]

Equations (5.7)--(5.8), the saddle-tail estimate, and the short-cycle
error give, at the critical scale,

\[
 \boxed{
 \left({1\over2}-o(1)\right)
 {\mathscr C_H\over\mathscr R_H}
 \le {\mathcal C_H\over R_H}
 \le
 \left({4\over3}+o(1)\right)
 {\mathscr C_H\over\mathscr R_H}.}
 \tag{5.11}
\]

Thus the outer additive renewal does not decide the ratio: boundedness or
divergence is inherited, within fixed constants, from the actual reduced
predecessor-active phase process.

## 6. The only unconditional divergent regime

Let \(T\) be any permutation of a set of size \(B\), let \(E\) have size
\(R\), and put

\[
 C_h(E)=\sum_{u=1}^h|E\cap T^{-u}E|.
\]

Set

\[
 Y(v)=\sum_{j=0}^h\mathbf1_E(T^jv).
\]

Then

\[
 \sum_vY(v)=(h+1)R
\]

and

\[
 \sum_vY(v)^2
 =(h+1)R+2\sum_{u=1}^h(h+1-u)|E\cap T^{-u}E|.
\]

Cauchy--Schwarz and \(h+1-u\le h+1\) give

\[
 \boxed{
 C_h(E)\ge {1\over2}
   \left({(h+1)R^2\over B}-R\right).}
 \tag{6.1}
\]

Apply this with \(T=\tau\), \(E=E_H\), and \(h=H+1\):

\[
 \boxed{
 {\mathcal C_H\over R_H}
 \ge {1\over2}
 \left({(H+2)R_H\over B_m}-1\right).}
 \tag{6.2}
\]

Therefore \(HR_H/B_m\to\infty\) forces divergence.  If
\(R_H=cB_m/H\), (6.2) gives only \((c-1)/2+o(1)\).  This limitation is
at the exact scale required by \(ST_A\), not an artifact of the proof.

## 7. A genuine bounded-ratio Gaussian renewal sector

The direct renewal formulas can be solved completely on a mountain
inverse fibre.

Choose a constant

\[
 {A\over2}<c<A.
 \tag{7.1}
\]

Let \(h\to\infty\) through values for which

\[
 p=2h-1
\]

is prime, and choose ranks \(m\) with

\[
 {h\over\sqrt m}\longrightarrow c.
 \tag{7.2}
\]

Let the reduced core be the rank-\((h-1)\) mountain and put

\[
 y=m-h,
 \qquad
 \Omega_{m,h}=\left\{(n_0,\ldots,n_{p-1})\in
    \mathbb Z_{ge0}^{p}:\sum_jn_j=y\right\}.
 \tag{7.3}
\]

The literal parent PBBS transport is

\[
 \tau(n_0,n_1,\ldots,n_{p-1})
   =(n_{p-1},n_0,\ldots,n_{p-2}).
 \tag{7.4}
\]

The mountain predecessor is selected at times

\[
 2,\ 2+p,\ 2+2p,\ldots.
\]

Hence a phase starts a return within the cutoff exactly when

\[
 n_0=0.
 \tag{7.5}
\]

For \(n_0=0\), the return gap is \(p+2=2h+1\), it is first, and its
winding is zero.  Conditions (7.1)--(7.2) give eventually

\[
 h+1\le H,
 \qquad
 H+1<p.
 \tag{7.6}
\]

Because \(p\) is prime, every active nonconstant composition has parent
period exactly \(p\), so every active phase survives the long-cycle
deletion.

Stars and bars now gives

\[
 \boxed{
 |\Omega_{m,h}|=\binom{y+p-1}{p-1},
 \qquad
 R_H^{\rm mt}=\binom{y+p-2}{p-2}.}
 \tag{7.7}
\]

For every \(1\le u\le H+1<p\), the two active tests are the distinct
coordinate equations \(n_0=n_{-u}=0\).  Therefore

\[
 \boxed{
 \mathcal C_H^{\rm mt}
 =(H+1)\binom{y+p-3}{p-3}.}
 \tag{7.8}
\]

Division yields the exact finite-rank ratios

\[
 \boxed{
 {R_H^{\rm mt}\over|\Omega_{m,h}|}
 ={p-1\over y+p-1}
 ={2h-2\over m+h-2},}
 \tag{7.9}
\]

\[
 \boxed{
 {\mathcal C_H^{\rm mt}\over R_H^{\rm mt}}
 =(H+1){p-2\over y+p-2}
 =(H+1){2h-3\over m+h-3}.}
 \tag{7.10}
\]

Equations (7.1)--(7.2) prove

\[
 \boxed{
 H{R_H^{\rm mt}\over|\Omega_{m,h}|}\to2Ac,
 \qquad
 {\mathcal C_H^{\rm mt}\over R_H^{\rm mt}}\to2Ac.}
 \tag{7.11}
\]

This is a literal PBBS bounded-ratio renewal law at the critical
\(1/H\) density.  It is not an abstract weak-composition surrogate: the
coordinate rotation (7.4), first return, zero winding, and long parent
period have all been used.

Let \(\nu_H^{\rm mt}\) be the maximum quotient-edge-disjoint subfamily
of these mountain starts.  The circular-interval conflict graph has at
most \(\mathcal C_H^{\rm mt}\) edges, so Caro--Wei and
Cauchy--Schwarz give

\[
 \nu_H^{\rm mt}
 \ge{(R_H^{\rm mt})^2
       \over R_H^{\rm mt}+2\mathcal C_H^{\rm mt}}.
 \tag{7.12}
\]

Consequently

\[
 \boxed{
 \liminf H{\nu_H^{\rm mt}\over|\Omega_{m,h}|}
 \ge {2Ac\over1+4Ac}>0.}
 \tag{7.13}
\]

Thus the bounded susceptibility produces an actual critical packing
inside this complete invariant sector.

However,

\[
 |\Omega_{m,h}|
 \le(m+h)^{2h}
 =\exp(O(\sqrt m\log m))
 =o(B_m/H).
 \tag{7.14}
\]

Thus (7.11) refutes any claim that local PBBS renewal automatically
forces divergence, but it supplies no global Catalan-critical packing.

## 8. What would decide the global additive compiler

The exact formulas isolate two sufficient global conclusions.

### Bounded-ratio refutation

If, for some fixed \(A\),

\[
 \mathscr R_H\ge\kappa {B_m\over H},
 \qquad
 \mathscr C_H\le M\mathscr R_H
 \tag{8.1}
\]

with \(\kappa>0\) and \(M<\infty\), then (5.7)--(5.11) give

\[
 R_H=\Omega(B_m/H),
 \qquad
 \mathcal C_H=O(R_H).
\]

The conflict-graph bound

\[
 \overline\nu_H
 \ge {R_H^2\over R_H+2\mathcal C_H}
 \tag{8.2}
\]

then produces \(\Omega(B_m/H)\) quotient-edge-disjoint returns and
refutes \(ST_A\) and the global additive compiler.

### Necessary positive branch

If \(R_H\ge\kappa B_m/H\) and \(ST_A\) is true, then necessarily

\[
 \mathcal C_H/R_H\longrightarrow\infty.
 \tag{8.3}
\]

But (8.3) alone is not sufficient for a little-oh packing: a positive
mass of isolated starts can coexist with rare dense clusters whose
contribution makes the scalar ratio diverge.  A positive proof must
control the full conflict-degree distribution or the higher renewal-gap
process.

The unresolved global statistic is now completely explicit:

\[
 \boxed{
 {\mathscr C_H\over\mathscr R_H}
 =
 {\displaystyle
  \sum_{d,k}P_m(d,k)
   \sum_{F\in\mathscr A_H(d,k)}
   \sum_{u=1}^{H+1}
     \mathbf1_{\mathscr A_H}(\tau_d^uF)
  \over\displaystyle
  \sum_{d,k}P_m(d,k)|\mathscr A_H(d,k)|}.}
 \tag{8.4}
\]

Here

\[
 \mathscr A_H(d,k)
 =\{F:B_2(F)\le2H-1\}
\]

uses the actual selected-particle itinerary, and the exact weights are the
Pascal coefficients (2.3).  No generic renewal heuristic evaluates
(8.4).  Proving it bounded on a critical mass would refute the compiler;
proving divergence in probability, followed by a higher-order packing
theorem, is the remaining positive route.
