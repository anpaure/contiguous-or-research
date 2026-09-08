# Pair-radius reset circulations: a long-cycle skeleton and the stable physical obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Put

\[
 n=2m,\qquad \Omega=\binom{[2m]}m,\qquad
 W=|\Omega|,
\]

and fix a perfect matching \(\Pi\) of the \(2m\) physical coordinates.
For a set \(T\), let

\[
 d_\Pi(T)=\#\{M\in\Pi:M\subseteq T\}                         \tag{0.1}
\]

be its pair radius. A Johnson transition deleting \(a\) and inserting
\(b\) is a pair flip when \(b\) is the \(\Pi\)-mate of \(a\), and is
pair-breaking otherwise.

The proposed construction was to use pair-radius target menus, add a
bounded reset/copy state at each quota-floor crossing, Eulerize the
resulting de Bruijn graph, and obtain an owner circulation with
\(o(W/H)\) cycles. The following conclusions are proved.

1. **The suffix, point-margin, and cycle ledgers are simultaneously
   feasible.** For every \(H=o(m)\), there is a pair-flip-only partial
   owner permutation on

   \[
                            G=W-o(W)                              \tag{0.2}
   \]

   owners which is cyclically \(H\)-safe, has

   \[
                            \kappa=o(W/H),                        \tag{0.3}
   \]

   and has the exact common run vector

   \[
                            R_v=G/(2m)\qquad(v\in[2m]).           \tag{0.4}
   \]

   Hence its lower and upper point margins are exactly

   \[
   G/2-qG/(2m),\qquad G/2+qG/(2m)                              \tag{0.5}
   \]

   at every \(q\le H\).

2. **The prescribed columns force dense physical resets.** Let \(P\) be
   a full \(H\)-safe owner permutation and let \(E_\Pi(P)\) be its number
   of pair-breaking transitions. At depth \(q\), let \(\nu_q^-\) be the
   exact floor/ceiling table whose bonus unit is placed on the
   \(\rho_q\) targets of smallest pair radius, where \(q\le H\) and

   \[
    W=c_qN_q+\rho_q,qquad N_q=\binom{2m}{m-q}.                  \tag{0.6}
   \]

   If \(\mu_q^-\) is the actual lower histogram, then

   \[
   \boxed{
    qE_\Pi(P)+{m-q\over4}\|\mu_q^--\nu_q^-\|_1
    \ge {Wq(2m-q-1)\over2(2m-1)}.}                             \tag{0.7}
   \]

   The same statement holds above after literal complementation. If
   \(\tau_q^-\) is any exact common-run correction of \(\nu_q^-\), the
   norm in (0.7) may be replaced by

   \[
    \|\mu_q^--\tau_q^-\|_1+\|\tau_q^--\nu_q^-\|_1.            \tag{0.8}
   \]

   Put

   \[
    S_H=\sum_{q=1}^H{q\over m-q},\qquad
    a_H={2m-H-1\over2(2m-1)},                                  \tag{0.9}
   \]

   and let \(D_{\le H}\) be the aggregate quantity in (0.8). Then

   \[
   \boxed{
                         E_\Pi(P)\ge Wa_H-{D_{\le H}\over4S_H}.} \tag{0.10}
   \]

   Consequently, if \(H=\Omega(\sqrt m)\), \(H=o(m)\), and
   \(D_{\le H}=o(W)\), then

   \[
                         E_\Pi(P)\ge(1/2-o(1))W.                 \tag{0.11}
   \]

   Under the same regime, in particular, a full pair-flip-only realization has

   \[
                         D_{\le H}\ge(1+o(1)){WH^2\over m}.     \tag{0.12}
   \]

   (Here \(H\to\infty\), so \(H(H+1)=(1+o(1))H^2\).) At Gaussian
   depth this is \(\Omega(W)\). A reset label which does not
   change the physical edge leaves \(E_\Pi\) unchanged and cannot help.

3. **There is an independent literal support obstruction.** Every
   pair-cell-preserving complete or partial factor satisfies

   \[
                         M_q^-\ge\sum_d(B_{q,d}-A_d)_+,          \tag{0.13}
   \]

   where \(A_d\) counts middle owners of radius \(d\), and \(B_{q,d}\)
   counts rank-\((m-q)\) targets of radius \(d\). If
   \(q=(A+o(1))\sqrt m\), \(A>0\) fixed, then

   \[
   \boxed{
    M_q^-\ge
    \left(e^{-A^2}\Phi(A/2)-\Phi(-3A/2)-o(1)\right)W,}         \tag{0.14}
   \]

   and the coefficient is strictly positive. Thus the long-cycle
   construction in item 1 has \(\Omega_A(W)\) literal lower holes.
   More generally, if a partial factor has \(E_\Pi\) pair-breaking edges,
   then the right side of (0.13) decreases by at most \(qE_\Pi\).
   Therefore, provided \(q\le H\), \(o(W)\) holes at
   \(q=A\sqrt m\) already require

   \[
    E_\Pi\ge
    \left({e^{-A^2}\Phi(A/2)-\Phi(-3A/2)\over A}-o(1)\right)
    {W\over\sqrt m}
    =\Omega_A(W/H).                                             \tag{0.14a}
   \]

   The stronger positive-density conclusion (0.11) uses multiplicity
   closeness to the prescribed smallest-radius tables.

4. **The compressed new reset colour is not even a fractional flag
   projection.** At a reset

   \[
                         c_{q-1}=K-1,\qquad c_q=K,               \tag{0.15}
   \]

   any new high child family \(D\) must satisfy

   \[
                         (K+1)|D|\le K|\nabla D|.                \tag{0.16}
   \]

   A low pair-radius family has

   \[
                         \nabla\{d_\Pi\le r\}
                         =\{d_\Pi\le r+1\}                     \tag{0.17}
   \]

   on the parent rank and, at a polynomial Gaussian lower tail,

   \[
                         {|\nabla D|\over|D|}=1+o(1).            \tag{0.18}
   \]

   Hence it violates (0.16) for every fixed \(K\). The old low-load
   high-radius fringe obeys the dual Hall cut. When the two radial tails
   are disjoint and \(K\) is fixed, the forced correction is asymptotic
   to the entire reset
   fringe

   \[
    (1-\alpha_{q-1})N_{q-1}+\alpha_qN_q.                         \tag{0.18a}
   \]

   There are infinitely many Gaussian resets for which this is
   \(\Theta_K(W/\sqrt m)\). For growing reset levels the exact robust
   Hall bounds below remain valid, but no all-window fringe asymptotic is
   proved here: the reset level multiplies the shadow-expansion error.

5. **A quotient Euler tour does not control physical components.** Root
   transversality makes every used physical memory state one-in/one-out.
   A reset-state quotient may be connected while its physical lift has
   many holonomy orbits. Auxiliary reset colours which project to the
   identity may split a physical orbit, but cannot merge distinct ones.

This is the requested stable obstruction beyond the finite
\(m=H=2\) square-root example. It closes the natural bounded-state
pair-radius construction with sparse or purely labelled resets when
aggregate \(L^1\)-multiplicity closeness to the prescribed smallest-radius
tables is retained. It is not a coefficient-one no-go: an unrestricted
construction may use a positive density of genuinely pair-breaking
physical transitions, choose an expansion-rich reset family, and arrange
long physical holonomy. No such circulation is constructed here.

## 1. Labelled states still project to one physical permutation

An \(H\)-memory state is a safe physical path

\[
                         \sigma=(X_0,\ldots,X_{H-1}).            \tag{1.1}
\]

An edge appends one safe successor and shifts the state. Adjoin arbitrary
finite labels recording the quota floor, top-copy identity, reset epoch,
pair radius, or any other bounded controller state. Suppose a zero-one
edge selection has one selected edge at every physical root and equal
selected indegree and outdegree at every labelled memory.

After forgetting labels, the selected path rooted at \(X\) has the form

\[
                         (X,PX,P^2X,\ldots,P^HX)                 \tag{1.2}
\]

for one physical permutation \(P\) of the owner set. Indeed, the root row
chooses the first successor \(PX\), and memory balance forces the suffix
of the path rooted at \(X\) to equal the selected prefix rooted at \(PX\).
Iteration gives (1.2). Thus reset labels describe a physical solution;
they do not relax the suffix equations.

In particular, a physical pair flip remains a pair flip under every
quota-copy relabelling. A reset capable of changing the invariants below
must be a genuinely different Johnson transition.

## 2. A long-cycle pair-cell skeleton

For an owner \(X\), let \(D(X),E(X),S(X)\) be the sets of matched pairs
which are respectively double, empty, and singleton in \(X\). Since
\(|X|=m\),

\[
                         |D(X)|=|E(X)|=:d,
 \qquad |S(X)|=m-2d=:s.                           \tag{2.1}
\]

Fixing \((D,E,S)\) gives a cube \(Q_s\), because one chooses one endpoint
from every singleton pair. Cube edges are exactly physical pair flips.

### Lemma 2.1 (dyadic isometric cycle factor)

If \(r\) is a power of two, \(Q_r\) has a factor into cycles of length
\(2r\), and the cyclic direction word on every cycle is \(\pi\pi\) for a
permutation \(\pi\) of the \(r\) directions.

#### Proof

For \(r=1\), toggle the unique bit. If \(r=2h\), write a vertex as
\((u,v)\in Q_h\times Q_h\) and alternately apply the inductive neighbour
permutation to the first and second factor according to total parity.
After \(2a\) moves the state is \((F_h^au,F_h^av)\). By induction every
orbit of \(F_h\) has length \(2h\). Thus an even return requires
\(a\equiv0\pmod {2h}\). At an odd time the two child factors have been
moved numbers of times which differ by one, and those two numbers cannot
both be divisible by \(2h\). Hence the first return has length
\(4h=2r\). During its first \(r\) moves every direction is used once, and
the next \(r\) directions repeat. Since \(F_{2h}^{\,4h}\) is the identity,
\(F_{2h}\) is a permutation, so its functional orbits give the required
factor. \(\square\)

### Theorem 2.2 (safe long-cycle skeleton)

For every \(H=o(m)\), there is a retained set \(\mathcal G\subseteq\Omega\)
and a pair-flip permutation on \(\mathcal G\) satisfying (0.2)--(0.5).

#### Proof

Let

\[
                         T=\lceil4\sqrt{mH}\rceil.              \tag{2.2}
\]

Discard cells with \(s<T\). Also discard cells whose word in
\(\{D,E,S\}^m\) has a nontrivial stabilizer under cyclic rotation of the
\(m\) matched pairs. In every retained cell take

\[
                         r=2^{\lfloor\log_2s\rfloor}>s/2>H,     \tag{2.3}
\]

choose \(r\) active singleton directions equivariantly on each free
rotation orbit, freeze the other singleton directions in every possible
orientation, and apply Lemma 2.1 on the active cube.

Every \(H\)-window uses distinct pair directions and is therefore a
Johnson geodesic. A cell of size \(2^s\) contributes

\[
                         {2^s\over2r}<{2^s\over s}\le{2^s\over T} \tag{2.4}
\]

cycles. Thus \(\kappa\le W/T=o(W/H)\).

The number of owners in cells with \(s<T\) is at most

\[
                         2^m\sum_{s<T}\binom ms=o(W),           \tag{2.5}
\]

because \(T=o(m)\). A nonfree status word has period at most \(m/2\), so
the second discarded family has at most

\[
                         m(2\sqrt3)^m=o(W)                       \tag{2.6}
\]

owners.

The construction is invariant under cyclic permutation of the matched
pairs. Here the cyclic run count of a coordinate is the number of
membership boundaries \(1\to0\) around a cycle; a coordinate constant on
that cycle contributes zero. On one active cycle each used pair direction
gives one such run to each of its two physical coordinates, while unused
directions give zero. Hence all \(2m\) coordinate run counts are equal. Their sum is
the number \(G\) of retained transitions, giving (0.4). The retained owner
set is coordinate-transitive under pair rotation and within-pair swaps,
so every coordinate belongs to exactly \(G/2\) retained owners. The usual
run-window count now gives (0.5). \(\square\)

This theorem proves no targetwise balance. Its purpose is to show that the
cycle and point ledgers are not the failure of the pair-cell grammar.

## 3. Exact radius drift under physical pair breaking

Let \(P\) be a full \(H\)-safe owner permutation. Write

\[
 L_q(X)=X\setminus\{a_1(X),\ldots,a_q(X)\}.                    \tag{3.1}
\]

### Lemma 3.1 (first-hit charging)

For every root \(X\),

\[
 d_\Pi(L_q(X))=d_\Pi(X)-F_q(X),                                \tag{3.2}
\]

where \(F_q(X)\) is the number of pairs full in \(X\) hit by the first
\(q\) deletions. Moreover, each such pair has a distinct first-hit
transition, and that transition is pair-breaking.

#### Proof

A pair full in \(X\) remains full in the lower trace precisely when no
endpoint is deleted. At the first deletion from a hit pair, its mate is
still present in the current owner. The inserted coordinate must be
outside the current owner and therefore cannot be that mate. Thus the
edge is pair-breaking. Distinct first-hit pairs give distinct edges.
\(\square\)

Every selected physical edge belongs to exactly \(q\) rooted forward
\(q\)-windows. Summing Lemma 3.1 yields

\[
 \sum_Xd_\Pi(L_q(X))
 \ge\sum_Xd_\Pi(X)-qE_\Pi(P).                                  \tag{3.3}
\]

The complementary upper statement follows by applying the same argument
to \([2m]\setminus U_q(X)\): a first insertion into a pair empty at the
root is necessarily pair-breaking.

## 4. The pair-radius moment inequality

For a uniform rank-\(k\) set,

\[
                         \bar d_k={k(k-1)\over2(2m-1)}.          \tag{4.1}
\]

With \(k=m-q\),

\[
                         \bar d_m-\bar d_k
 = {q(2m-q-1)\over2(2m-1)}=:qa_q.                              \tag{4.2}
\]

The table \(\nu_q^-\) places its bonus mass on the smallest values of
\(d_\Pi\), so

\[
                         \sum_T\nu_q^-(T)d_\Pi(T)
 \le W\bar d_k.                                                \tag{4.3}
\]

If two rank-\(k\) tables \(\mu,\nu\) have equal mass, then

\[
 \sum_T(\mu(T)-\nu(T))d_\Pi(T)
 \le{k\over4}\|\mu-\nu\|_1,                                  \tag{4.4}
\]

because their positive difference has mass \(\|\mu-\nu\|_1/2\) and
\(0\le d_\Pi\le k/2\).

Apply (4.3)--(4.4) to the actual histogram and combine with (3.3). This
proves (0.7). Summing its rearranged form

\[
 D_q\ge {4q\over m-q}(Wa_q-E_\Pi(P))_+                         \tag{4.5}
\]

over \(q\le H\) proves (0.10)--(0.12), where

\[
 D_q=\|\mu_q^--\tau_q^-\|_1+\|\tau_q^--\nu_q^-\|_1.           \tag{4.5a}
\]

The obstruction is independent of point margins. For completeness, one
can correct every \(\nu_q^-\) to a table \(\tau_q^-\) satisfying one
balanced common integer run vector with

\[
                         \|\tau_q^--\nu_q^-\|_1=O(m^2).         \tag{4.6}
\]

Indeed, take all complete radius layers and choose the required portion
of the boundary layer by complete orbits of the \(2m\)-cycle which
cyclically permutes the matched pairs and their two shores. Only one
partial orbit is nonregular. If \(d_v\) is the resulting bonus degree,
then

\[
 \left|d_v-{(m-q)\rho_q\over2m}\right|\le2m.                  \tag{4.6a}
\]

Fix once and for all an integer vector \(R\), common to all depths, with
\(R_v\in\{\lfloor W/(2m)\rfloor,\lceil W/(2m)\rceil\}\) and
\(\sum_vR_v=W\). Above the constant floor, the desired residual degree is

\[
 a_v={W\over2}-qR_v-c_q\binom{2m-1}{m-q-1}
 ={(m-q)\rho_q\over2m}-q\left(R_v-{W\over2m}\right).          \tag{4.6b}
\]

It is integral, has sum \((m-q)\rho_q\), and
\(|d_v-a_v|\le2m+q\). Pairing surplus and deficit coordinate units
therefore needs at most

\[
 {1\over2}\sum_v|d_v-a_v|\le m(2m+q)                          \tag{4.6c}
\]

Johnson transfers. For a transfer from coordinate \(u\) to coordinate
\(v\), choose an \((m-q)\)-set containing \(u\) and not \(v\), and
replace \(u\) by \(v\). Sources and recipients may be chosen distinct
from the pool of \(\binom{2m-2}{m-q-1}\) candidates. After \(t-1\)
transfers, each of the \(2(t-1)\) used endpoint sets forbids at most one
candidate source, by being either that source or its image under
\(u\mapsto v\). This pool is exponential for \(q=o(m)\), whereas
(4.6c) is polynomial. Every source
has floor load at least one, so nonnegativity is preserved. Each transfer
costs two in \(L^1\), proving (4.6). The same \(R\) is used at every
depth, and complementation supplies the upper tables. Thus the aggregate
two-sign correction through \(H=o(m)\) is \(O(m^2H)=o(W)\).

For a partial owner circulation with leave \(L\), the same proof loses at
most \(mL/2\) in its initial radius moment. Summing only
\(q\in[H/2,H]\) shows that (0.11) still holds if

\[
                         L=o(WH/m),\qquad D_{\le H}=o(W),        \tag{4.7}
\]

with \(H=\Omega(\sqrt m)\), \(H=o(m)\). This is the sharp scale supplied
by the radius moment; it does not cover an arbitrary \(o(W)\) leave.

Most importantly, (0.10) assumes \(L^1\)-multiplicity closeness to the
specified smallest-radius tables. It must not be inferred from merely
\(o(W)\) literal support holes when \(c_q\ge2\).

## 5. Literal radial support at Gaussian depth

The number of middle owners of radius \(d\) and lower rank-\((m-q)\)
targets of radius \(d\) are

\[
 A_d={m!\,2^{m-2d}\over d!^2(m-2d)!},\qquad
 B_{q,d}={m!\,2^{m-q-2d}\over d!(d+q)!(m-q-2d)!}.              \tag{5.1}
\]

Pair-cell moves preserve the sets of double and empty pairs. Every rooted
\(q\)-window from a radius-\(d\) owner therefore has lower radius \(d\).
There are exactly \(A_d\) available occurrences in that class, which
proves (0.13). An owner leave can only reduce the available occurrences.

If \(E_\Pi\) selected transitions are pair-breaking, at most \(qE_\Pi\)
rooted \(q\)-windows contain such a transition. Relabeling one occurrence
between radius classes can reduce the sum of class deficits by at most
one. Hence every partial factor satisfies the stable form

\[
                         M_q^-
 \ge\sum_d(B_{q,d}-A_d)_+-qE_\Pi.                              \tag{5.1a}
\]

The complementary statement holds above.

The likelihood ratio is

\[
 \Lambda_{q,m}(d)={A_d\over B_{q,d}}
 =2^q{(d+1)\cdots(d+q)
       \over(m-2d-q+1)\cdots(m-2d)}.                            \tag{5.2}
\]

For a uniform rank-\((m-q)\) target and
\(q=(A+o(1))\sqrt m\), uniform Stirling expansion gives

\[
 {D-(m/4-q/2)\over\sqrt m}\Longrightarrow N(0,1/16),          \tag{5.3}
\]

and, uniformly on tight sets of the normalized variable,

\[
                         \log\Lambda_{q,m}(D)
                         \Longrightarrow N(-A^2,4A^2).         \tag{5.4}
\]

The tails outside those tight sets contribute nonnegatively to the hole
bound. Therefore

\[
 \begin{aligned}
 \liminf{M_q^-\over W}
 &\ge e^{-A^2}\,
       \mathbb E(1-e^Z)_+,
       \qquad Z\sim N(-A^2,4A^2)\\
 &=e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0,
 \end{aligned}                                                   \tag{5.5}
\]

which is (0.14). This theorem concerns a fixed pair frame and physical
pair-cell preservation. It does not obstruct dense pair-breaking seams.
Combining (5.1a) with (0.14), \(M_q^-=o(W)\) at
\(q=(A+o(1))\sqrt m\) forces

\[
 E_\Pi\ge
 \left({e^{-A^2}\Phi(A/2)-\Phi(-3A/2)\over A}-o(1)\right)
 {W\over\sqrt m}.                                               \tag{5.6}
\]

This is the sharp conclusion available from literal support alone; it is
only \(\Omega_A(W/H)\), not a positive density of all transitions.

## 6. The adjacent reset Hall cut

Let \(\mu_{q-1}\) and \(\mu_q\) be consecutive proposed lower tables.
They can be marginals of a fractional nested deletion-flag system only if

\[
 \sum_{S\in\mathcal A}\mu_q(S)
 \le\sum_{T\in\nabla\mathcal A}\mu_{q-1}(T)                    \tag{6.1}
\]

for every child family \(\mathcal A\). This is exactly the max-flow/min-cut
criterion on the consecutive-rank inclusion graph, and integral tables
admit an integral adjacent flow whenever all these cuts pass.

At the reset (0.15), apply (6.1) to the new high family \(D\). Its child
demand is \((K+1)|D|\), while every parent has capacity at most \(K\).
This proves (0.16). More robustly, every realized pair of tables satisfies

\[
 \begin{aligned}
 &\sum_{S\in D}(K+1-\mu_q(S))_+
 +\sum_{T\in\nabla D}(\mu_{q-1}(T)-K)_+\\
 &\hspace{30mm}\ge (K+1)|D|-K|\nabla D|.                       \tag{6.2}
 \end{aligned}
\]

For the pair-radius family \(D=\{d_\Pi\le r\}\), adding one coordinate
changes radius by zero or one, which gives the exact shadow identity
(0.17). The exact pair-radius mass formula and adjacent ratio imply,
uniformly for \(q=O(\sqrt m)\) and lower-tail density between
\(m^{-C}\) and \(1/4\),

\[
                         {|\nabla D|\over|D|}
 =1+O_C\!\left(\sqrt{\log m\over m}\right).                    \tag{6.3}
\]

Equations (6.2)--(6.3) prove the reset obstruction.

There is a dual cut for the old fringe. Immediately before the reset,
write the old high family as \(A=\{d_\Pi\le r_-\}\), so its complement

\[
                         E=\{T\in V_{q-1}:d_\Pi(T)\ge r_-+1\}   \tag{6.3a}
\]

has parent load \(K-1\). Put

\[
                         C=\{S\in V_q:d_\Pi(S)\ge r_-+1\}.      \tag{6.3b}
\]

If

\[
                         2(r_-+1)<m-q+1,                       \tag{6.3b'}
\]

then every boundary parent has a singleton pair whose deletion stays in
\(C\), and consequently \(\nabla C=E\). Polynomial Gaussian upper-tail
thresholds satisfy (6.3b'). Moreover \(|E|/|C|=1+o(1)\). The child baseline
demands \(K|C|\), while its entire parent shadow supplies at most
\((K-1)|E|\). Thus arbitrary realized tables satisfy the robust dual cut

\[
 \begin{aligned}
 &\sum_{S\in C}(K-\mu_q(S))_+
 +\sum_{T\in E}(\mu_{q-1}(T)-(K-1))_+\\
 &\hspace{27mm}\ge K|C|-(K-1)|E|.                             \tag{6.3c}
 \end{aligned}
\]

Write \(r_+\) for the threshold \(r\) defining the new family \(D\).
For compressed pair-radius threshold quantiles at a fixed-\(K\) Gaussian
reset, once both tail densities tend to zero, their thresholds satisfy
\(r_++1\le r_-\). Thus the new low-radius cut and the old
high-radius cut are disjoint. More precisely, if
\(\varepsilon_+=|\nabla D|/|D|-1\) and
\(\varepsilon_-=|E|/|C|-1\), the new and old robust deficit fractions
are respectively

\[
                         1-K\varepsilon_+,
                 \qquad 1-(K-1)\varepsilon_-.                 \tag{6.3c'}
\]

They are \(1-o(1)\) for fixed \(K\), so adding the two disjoint cuts
forces, up to lower-order threshold rounding, the whole fringe (0.18a).
If

\[
 \delta_q={\lambda_q-\lambda_{q-1}\over\lambda_{q-1}},         \tag{6.3d}
\]

that fringe lies between \(W\delta_q/(1+\delta_q)\) and
\(W\delta_q\). For growing \(K\), however, (6.3c') need not be close to
one: the reset level multiplies the shadow-expansion error. Thus no
growing-window sum, and in particular no critical-linearity claim at
\(H\lambda_H\asymp m\), is asserted without an additional uniform bound
on both products in (6.3c').

For an explicit infinite family, fix \(K\ge2\), let \(t\to\infty\), and
let \(M_t\) be the real solution of

\[
 \prod_{i=1}^t{M_t+i\over M_t-t+i}=K.                           \tag{6.4}
\]

Choose fixed \(0<\eta<2/\log K\) and
\(m_t=\lfloor M_t-\eta t\rfloor\). Then

\[
 m_t={t^2\over\log K}+O_K(t),\qquad
 c_{t-1}=K-1,\quad c_t=K,                                     \tag{6.5}
\]

and

\[
 \alpha_t={K\eta(\log K)^2+o_K(1)\over t}.                    \tag{6.6}
\]

The new bonus mass is \(\Theta_K(W/t)=\Theta_K(W/\sqrt m)\), and
(6.2) forces \((1-o(1))\) of it to be removed or paid above the parent
cap. Thus exact, or relative-\(o(|D|)\), realization of that compressed
new colour is impossible. Charging its entire new fringe as exceptional
still costs only \(o(W)\), and an expansion-rich reset family is not
obstructed.

## 7. Physical holonomy, not quotient Eulericity, controls cycles

In a root-transversal memory circulation, all edges leaving one physical
memory have the same first owner. The root row therefore gives physical
outdegree at most one, and memory balance gives equal indegree. Every used
physical memory is one-in/one-out. Consequently two owner cycles cannot be
fused by choosing a different Euler transition at a shared quotient state:
they do not share a physical state.

More formally, let a closed walk in a bounded quotient graph lift through
bijective physical fibres. Its physical component count is the number of
orbits of the closed-walk fibre permutation, or holonomy. A reset label
which projects to the identity on the physical fibre can refine or split
an orbit, but cannot merge two physical holonomy orbits.

Theorem 2.2 shows that \(o(W/H)\) physical cycles are achievable inside
the pair-cell grammar. Thus cycle count is not the obstruction there; the
target columns are. Once dense pair-breaking seams are introduced, their
physical holonomy and their all-depth target changes must be controlled in
one construction. Quotient connectedness alone supplies neither fact.

## 8. Proved and unproved boundary

The following are proved.

1. Pair cells support a cyclically \(H\)-safe \((W-o(W))\)-owner factor
   with exact common point margins and \(o(W/H)\) cycles for every
   \(H=o(m)\).
2. A pair-flip realization of the rounded smallest-radius columns has
   aggregate multiplicity discrepancy at least
   \((1+o(1))WH^2/m\).
3. If the aggregate all-depth multiplicity correction through
   \(q\le H\) is \(o(W)\), then at Gaussian window size
   \(H=\Omega(\sqrt m)\), \(H=o(m)\), at least \((1/2-o(1))W\)
   pair-breaking physical transitions are required. At one Gaussian
   depth the same conclusion needs the sharper error rate
   \(D_q=o(Wq/m)=o(W/\sqrt m)\).
4. With no pair-breaking transitions, there are \(\Omega_A(W)\) literal
   lower support holes at \(q=A\sqrt m\); with arbitrary transitions,
   \(o(W)\) holes force \(\Omega_A(W/H)\) pair-breaking edges.
5. At a floor reset, the compressed pair-radius threshold new colour
   violates an adjacent-rank fractional Hall cut, while its complementary
   threshold old fringe violates the dual cut. At fixed reset level they
   charge the whole reset fringe and need \(\Theta_K(W/\sqrt m)\)
   correction on an infinite Gaussian sequence. No growing-level
   aggregation is proved.
6. Reset labels and quotient Euler tours cannot change these physical
   conclusions.

The following remain unproved.

1. No obstruction is proved for an expansion-rich reset family combined
   with a positive density of pair-breaking physical transitions.
2. No integral circulation with those dense seams, exact common-run
   margins, all-depth \(o(W)\) target error, and \(o(W/H)\) physical
   cycles is constructed.
3. The dense-reset moment theorem assumes aggregate \(L^1\) multiplicity
   closeness to the prescribed smallest-radius tables; it is not implied
   by support holes alone once \(c_q\ge2\).
4. The partial-factor extension of the moment theorem requires
   \(L=o(WH/m)\), not merely an arbitrary \(o(W)\) owner leave.

Hence, while aggregate \(L^1\)-multiplicity closeness to the prescribed
smallest-radius tables is retained, the bounded-state
pair-radius/reset-colour route is genuinely closed unless its reset
operation is promoted from an auxiliary label to a positive-density
physical pair-breaking mechanism. Literal \(o(W)\) holes alone force only
the \(\Omega_A(W/\sqrt m)\) bound (5.6). At the positive-density escape
point the problem is again the unrestricted integral Johnson memory
circulation, with the requirement of \(o(W/H)\) physical cycles. In a
bijective-fibre quotient construction this is the corresponding
long-holonomy-orbit requirement.

## 9. Independent audit

The decisive steps were audited independently in two directions.

1. The dyadic first-return recursion, run convention, leave and cycle
   bounds, first-hit charging, factor \(1/4\) in the radius moment,
   Gaussian likelihood ratio, support coefficient, and the
   \(O(m^2)\) exact common-run correction were rederived. Equations
   (0.7)--(0.14a) and the partial-leave scale \(L=o(WH/m)\) passed.
2. The new- and old-fringe Hall signs, the exact factors
   \(1-K\varepsilon_+\) and \(1-(K-1)\varepsilon_-\), threshold
   disjointness, reset-fringe bounds, fixed-\(K\) infinite sequence,
   physical one-in/one-out projection, and bijective-fibre holonomy scope
   were checked separately. The audit rejected an earlier attempted
   growing-\(K\) whole-window sum; no such claim remains in this theorem.

Thus every displayed asymptotic is scoped either to the stated fixed
Gaussian parameter, to \(H=o(m)\), or to fixed reset level \(K\), as
indicated. The only positive-density conclusion is the aggregate
multiplicity theorem (0.10)--(0.11), not the literal-support theorem.
