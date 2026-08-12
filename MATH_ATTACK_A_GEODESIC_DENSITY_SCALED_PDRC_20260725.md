# Density-scaled PDRC for geodesic strips: an additive iteration and the thin-chain obstruction

Date: 2026-07-25

Method: pure mathematics only. No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Outcome

Let

\[
 W=\binom{2m}{m},\qquad
 N_q=\binom{2m}{m-q}=\binom{2m}{m+q},\qquad
 \lambda_q=\frac W{N_q}.
\]

Take return-free geodesic certificates whose full grid side has length

\[
 g=s+2Q-1=(1-o(1))H,
\]

so that exactly \(s\) central phase columns are physical. Splitting the
calibrated carrier paths into such pieces gives

\[
 T=\left\lfloor\frac Ms\right\rfloor N_H,\qquad
 \rho_s=\frac{sT}{W}=1-o(1).                       \tag{0.1}
\]

This attack gives one positive conditional theorem and two unconditional
advances.

1. The old PDRC is stronger than necessary. Equal residual tag degrees,
   pointwise lower target loads, and multiplicative control of every link
   are not used by the bite proof. It is enough to preserve:

   - positive exact buffered priority degree at every nonexceptional tag;
   - pathwise clearance slack; and
   - density-scaled \(L^2\) owner energy and the mixed
     exposed-to-raw flag hazard energy.

   This weakest sufficient form is called \(\mathrm{DSPDRC}_2\) below.

2. If \(\mathrm{DSPDRC}_2\) regenerates after every bite, activate at
   residual density \(u\) with

   \[
   \boxed{\alpha_u=\frac{\theta}{mu},}              \tag{0.2}
   \]

   not with a fixed \(\theta/m\) fraction of the current residual. Every
   bite then selects a fixed

   \[
   \left(\theta-o(1)\right)\frac{T}{m}              \tag{0.3}
   \]

   geodesic strips when \(s=o(m)\). After \(O(m)\) bites the leave is

   \[
   e=o(T/\sqrt m),                                  \tag{0.4}
   \]

   and the remaining augmented targets cost \(eK_s=o(W)\). Thus
   density-scaled PDRC would prove coefficient one directly, without a
   later cross-shadow or braid reserve.

3. Wide product rectangles are initially rare. For a fixed strip \(P\),
   the proportion of orbit grids whose controlled strip shares two
   incomparable cells with \(P\) is

   \[
   O\!\left(
      \frac{\rho_s\lambda_Q\,s(2Q+1)}{m^2}
     \right)
   =m^{-1+o(1)}.                                    \tag{0.5}
   \]

   Hence initial rectangle pruning is degree-negligible.

4. Rectangle pruning does not regenerate deadlines. There are two
   legitimate physical grids with no common owner and with width-one
   full-grid intersection, hence with no compressed \(2\times2\)
   rectangle, such that selecting one grid blocks two depth-one phase
   columns of the other. The exact chunk deadline is

   \[
   \bar d_1^{(s)}=1,                                \tag{0.6}
   \]

   so the second grid has zero legal priorities after this single
   rectangle-free selected edge.

The route therefore does not yet prove coefficient one. The exact missing
statement is density-scaled regeneration of the owner energy, the mixed
exposed-to-raw hazard energy, and clearance-majorization support. Rectangle rarity controls
wide pair overlaps, but it does not control scattered width-one chain
hits or the common lower/upper Hall cut.

## 1. Exact strip normalization and deadlines

Let the physical phase set be

\[
 I=\{Q,Q+1,\ldots,Q+s-1\}.
\]

The full grid is

\[
 G_{i,j}
 =C\cup\{a_{i+1},\ldots,a_g\}
     \cup\{b_1,\ldots,b_j\},
 \qquad 0\le i,j\le g.                              \tag{1.1}
\]

For \(t\in I\) and \(0\le q\le Q\), its literal controlled flags are

\[
 X_t=G_{t,t},\qquad
 L_q(t)=G_{t+q,t},\qquad
 U_q(t)=G_{t-q,t}.                                  \tag{1.2}
\]

Thus one strip has \(s\) targets in each of the \(2Q+1\) rank-tagged
rows.

Put

\[
 c_q^{(s)}
 =\min\left\{s,\left\lfloor\frac{N_q}{T}\right\rfloor\right\},
 \qquad
 d_q^{(s)}=s-c_q^{(s)},                             \tag{1.3}
\]

\[
 \Lambda_q=\sum_{r=1}^q\lambda_r,\qquad
 C_m=(\log m)^2,                                    \tag{1.4}
\]

and

\[
 h_q
 =\left\lceil C_m\frac{s}{m}\Lambda_q\right\rceil, \tag{1.5}
\]

\[
 \bar d_q
 =\min\{s,\max(d_q^{(s)},h_q)\},\qquad
 \bar c_q=s-\bar d_q.                               \tag{1.6}
\]

The audited chunk-slack estimate is

\[
 \sum_{q=1}^Q(\bar d_q-d_q^{(s)})=o(s).             \tag{1.7}
\]

Consequently the scalar loss caused by (1.6) is

\[
 2T\sum_{q=1}^Q(\bar d_q-d_q^{(s)})=o(Ts)=o(W).
                                                               \tag{1.8}
\]

The modified augmented size is

\[
 K_s=s+2\sum_{q=1}^Q\bar c_q
 =(\sqrt\pi+o(1))s\sqrt m.                          \tag{1.9}
\]

Indeed \(N_q/T=s/(\rho_s\lambda_q)\), the cap affects only
\(o(\sqrt m)\) depths, and

\[
 \sum_{q=1}^Q\lambda_q^{-1}
 =\left(\frac{\sqrt\pi}{2}+o(1)\right)\sqrt m.
\]

The baseline calibrated scalar leave is

\[
 {\cal L}_s
 =W-sT+2\sum_{q=1}^Q(N_q-c_q^{(s)}T)
 =o(W).                                             \tag{1.10}
\]

This is the usual floor/cap ledger: noncapped remainders total
\(O(QT)=o(W)\), capped depths contribute \(o(W)\), and \(W-sT=o(W)\).
The enlargement (1.8) is additional to (1.10).

The distinction between \(g\) and \(s=g-2Q+1\) is exact. Replacing one by
the other is asymptotically harmless because \(Q=o(g)\), but deadline and
rounding identities below use \(s\).

## 2. Exact buffered residual kernels

Let

\[
 Z=(Z_0;(Z_q^-,Z_q^+)_{1\le q\le Q})
\]

be the targets already claimed by a partial matching. Fix one unprioritized
base strip \(P\) above a remaining tag. A phase \(t\in I\) has first old
blocked depth

\[
 r_Z(t)
 =\min\{q:L_q(t)\in Z_q^-\ \hbox{or}\ U_q(t)\in Z_q^+\},          \tag{2.1}
\]

with \(r_Z(t)=Q+1\) if no such depth exists. Put

\[
 B_q^Z(P)=|\{t\in I:r_Z(t)\le q\}|,\qquad
 \sigma_q^Z(P)=\bar d_q-B_q^Z(P).                  \tag{2.2}
\]

The exact number of old-legal common priorities is

\[
 \Pi_Z(P)
 =(s-B_Q^Z(P))!
  \prod_{q=1}^Q
  \frac{(\bar d_q-B_{q-1}^Z(P))!}
       {(\bar d_q-B_q^Z(P))!},                     \tag{2.3}
\]

when all factorials are defined, and zero otherwise.

Call \(P\) **buffered** if all its owners avoid \(Z_0\) and

\[
 \sigma_q^Z(P)\ge h_q\qquad(1\le q\le Q).           \tag{2.4}
\]

For a remaining tag \(U\), define its exact buffered degree

\[
 D_U^{\mathrm{buf}}(Z)
 =\sum_{P\text{ buffered above }U}\Pi_Z(P).         \tag{2.5}
\]

Whenever (2.5) is positive, let

\[
 \mu_U^Z(P)=\frac{\Pi_Z(P)}{D_U^{\mathrm{buf}}(Z)}
                                                               \tag{2.6}
\]

on buffered paths.

Only targets which can create a new first blocker need enter the dynamic
energy. Internal row rainbowness makes the following indicators \(0/1\):

\[
 \chi_{r,S}^{\pm}(P)
 =
 \mathbf 1\{\exists t\in I:
      F_r^\pm(t)=S,\ r<r_Z(t)\}.                    \tag{2.7}
\]

Here \(F_r^-=L_r\) and \(F_r^+=U_r\). Define the residual loads

\[
 L_0(X)
 =\sum_{U}\Pr_{P\sim\mu_U^Z}(X\in P),              \tag{2.8}
\]

\[
 L_{r,S}^{\pm}
 =\sum_U\mathbb E_{P\sim\mu_U^Z}\chi_{r,S}^{\pm}(P).
                                                               \tag{2.9}
\]

Also define the raw central-strip load

\[
 \widetilde L_{r,S}^{\pm}
 =\sum_U
   \Pr_{P\sim\mu_U^Z}
   (\exists t\in I:F_r^\pm(t)=S).                  \tag{2.10}
\]

An exposed occurrence can acquire a new first blocker by meeting any raw
occurrence on another active path, including one whose own phase was
already blocked more shallowly. Thus the exact next-bite energy is the
mixed product \(L_{r,S}^{\pm}\widetilde L_{r,S}^{\pm}\), not merely the
square of the exposed load.

The sums are over the nonexceptional remaining tags.

## 3. The weakest sufficient hereditary PDRC

Let the initial tag number be \(T\), and suppose \(uT\) nonexceptional
tags remain. Let \(A_m\ge1\) satisfy

\[
 A_m\frac{s}{m}=O(1),\qquad
 A_m\frac{\log m}{C_m}=o(1).                       \tag{3.1}
\]

A fixed constant \(A_m\) is allowed. For geodesic chunks \(s\sim H=o(m)\),
the first quantity is in fact \(o(1)\); the weaker bounded condition also
covers the full-prefix specialization \(s=M\).

### Definition 3.1 (density-scaled exposed-hazard PDRC,
\(\mathrm{DSPDRC}_2\))

A reachable residual has \(\mathrm{DSPDRC}_2(A_m)\) if:

1. \(D_U^{\mathrm{buf}}(Z)>0\) for every nonexceptional remaining tag;
2. the owner energy obeys
   \[
   \sum_XL_0(X)^2
   \le A_m u^2\rho_s\,sT;                           \tag{3.2}
   \]
3. for every \(q\le Q\), the cumulative exposed-to-raw hazard energy obeys
   \[
   \sum_{\pm}\sum_{r=1}^q\sum_{S\in N_r}
      L_{r,S}^{\pm}\widetilde L_{r,S}^{\pm}
   \le2A_m u^2\rho_s\,sT\,\Lambda_q.                \tag{3.3}
   \]

Here \(S\in N_r\) means \(S\) ranges over the rank-\((m\pm r)\) layer
appropriate to the sign. The exceptional tag set is fixed in advance or
has total size \(o(T/\sqrt m)\); it is charged only once at the end.

The property is hereditary if it holds, with the same \(A_m\), after every
chosen bite while the nonexceptional residual density is above the
stopping threshold.

This is weaker than the earlier PDRC in four ways.

* No equality or comparability of the numbers \(D_U^{\mathrm{buf}}\) is
  required.
* No lower target-load estimate is required.
* Only aggregate quadratic/mixed energy is controlled, not every
  pointwise load.
* Only currently exposed occurrences are charged as possible new
  blockers, but they are paired against all raw occurrences. A cell
  already blocked at a shallower old depth cannot itself acquire a new
  first blocker, although it can block an exposed occurrence elsewhere.

Equations (3.2)--(3.3) are exactly the second moments used by the bite
proof below. Thus \(\mathrm{DSPDRC}_2\) is the weakest non-tautological
residual closure isolated by this argument.

## 4. Density-compensated bite

### Theorem 4.1 (one bite under \(\mathrm{DSPDRC}_2\))

Assume a residual with \(uT\) nonexceptional tags has
\(\mathrm{DSPDRC}_2(A_m)\), and let

\[
 \alpha_u=\frac{\theta}{mu}\le1                    \tag{4.1}
\]

for fixed \(0<\theta<1\). Independently activate each remaining tag with
probability \(\alpha_u\), and at an active tag sample \(P\) from (2.6).
There is an outcome containing at least

\[
 \boxed{
 \left[
  \theta-A_m\rho_s\theta^2\frac{s}{m}
  -O\!\left(A_m\theta^2\frac{\log m}{C_m}\right)
  -o(1)
 \right]\frac{T}{m}}                                \tag{4.2}
\]

chunks whose owners and all modified common-priority claims are mutually
distinct and avoid the old matching.

If \(s=(1-o(1))H=o(m)\) and additionally \(A_ms/m=o(1)\)—in particular
if \(A_m=O(1)\)—this is

\[
 (\theta-o(1))\frac{T}{m}.                          \tag{4.3}
\]

#### Proof

Let \(A\) be the number of active tags. Then

\[
 \mathbb EA=\alpha_u uT=\frac{\theta T}{m}.         \tag{4.4}
\]

For an owner \(X\), its active load has mean \(\alpha_uL_0(X)\).
The expected number \(C_0\) of owner-collision pairs is at most

\[
 \mathbb EC_0
 \le\frac{\alpha_u^2}{2}\sum_XL_0(X)^2
 \le\frac{A_m\alpha_u^2u^2\rho_s\,sT}{2}.           \tag{4.5}
\]

Delete both endpoints of every owner-collision pair. This costs at most

\[
 2\mathbb EC_0
 \le A_m\rho_s\theta^2\frac{sT}{m^2}.               \tag{4.6}
\]

Now expose new flag collisions before performing this deletion. For a
rank-tagged target \(S\), let \(Y_S^{\rm exp}\) and \(Y_S^{\rm raw}\)
be its active exposed and raw occurrence counts. Every newly blocked
exposed occurrence has an ordered witness consisting of that occurrence
and another raw occurrence on a different active tag. Independence between
tags gives

\[
 \mathbb E[\#\{\text{newly blocked exposed occurrences at }S\}]
 \le\alpha_u^2L_S\widetilde L_S.                    \tag{4.7}
\]

For an active path \(P\), let \(C_q(P)\) be the number of its phase
columns which acquire a new first blocker at depth at most \(q\). Summing
(4.7) and using (3.3) gives

\[
 \mathbb E\sum_{P\ {\rm active}}C_q(P)
 \le2A_m\alpha_u^2u^2\rho_s\,sT\,\Lambda_q.         \tag{4.8}
\]

Partition the increasing sequence \(\Lambda_q\) into dyadic blocks. If
some path has \(C_q(P)>h_q\) at a depth in one block, then at the last
depth \(q_j\) of that block it has

\[
 C_{q_j}(P)>
 \frac{C_m}{2}\frac{s}{m}\Lambda_{q_j},             \tag{4.9}
\]

apart from the harmless first integer block. Markov's inequality applied
to (4.8) shows that the expected fraction of active paths caught in one
block is \(O(A_m\theta/C_m)\). There are \(O(\log m)\) blocks, so the
expected number of deadline-bad active paths is

\[
 O\!\left(A_m\theta\frac{\log m}{C_m}\right)
 \frac{\theta T}{m}.                                \tag{4.10}
\]

Delete those paths from the proposed bite. Owner deletion and deadline
deletion can only remove new collisions from the survivors.

For every surviving \(P\),

\[
 C_q(P)\le h_q\le\sigma_q^Z(P)\qquad(q\le Q).       \tag{4.11}
\]

Therefore its updated first-block counts satisfy the exact deadline Hall
inequalities. Choose a new legal priority for the combined old and new
blocked sets. If a target was newly duplicated at depth \(r\), each
remaining occurrence lies in a phase whose first new blocker is at most
\(r\), so its chosen height is below \(r\). No duplicated occurrence is
claimed. Old used targets are hidden by the same combined deadline
system. Hence all new claims are mutually distinct and avoid the old
matching.

Taking an outcome at least as good as the expectation in
(4.4)--(4.10) proves (4.2). \(\square\)

### Remark 4.2 (why the factor \(u^{-1}\) is necessary)

If every bite activates a fixed \(\theta/m\) fraction of the **current**
residual, then after \(J\) ideal bites its density is

\[
 u_J=(1-\theta/m)^J.                                \tag{4.12}
\]

For \(J=O(m)\), this is bounded away from zero. Reaching
\(o(m^{-1/2})\) requires \(\Theta(m\log m)\) such multiplicative bites.
The \(O(m)\)-round claim is valid only for the density-compensated
activation (4.1), which attempts a fixed \(\theta T/m\) tags per round.

## 5. Conditional additive iteration

### Theorem 5.1 (\(\mathrm{DSPDRC}_2\) implies the required leave)

Assume the strong hereditary form of \(\mathrm{DSPDRC}_2(A_m)\): every
legal residual produced by the bites of Theorem 4.1 again satisfies
Definition 3.1 with the same \(A_m\). More minimally, it is enough to prove
that every current residual has one outcome which simultaneously meets
(4.2) and preserves Definition 3.1. The alteration calculation itself
does not prove either closure statement.

Choose \(\omega_m\to\infty\) so slowly that

\[
 \omega_m=o(\sqrt m),
\qquad
 u_*=\frac1{\sqrt m\,\omega_m}                      \tag{5.1}
\]

lies above the hereditary stopping threshold. Then \(O(m)\) applications
of Theorem 4.1 give a target-disjoint matching leaving

\[
 \boxed{e=o(T/\sqrt m)}                             \tag{5.2}
\]

chunk tags.

The complete literal ledger is

\[
 eK_s=o(W),\qquad
 O(QT)=o(W),\qquad
 O(sN_H)=o(W),\qquad
 {\cal L}_s=o(W),                                   \tag{5.3}
\]

and the one-time deadline enlargement is (1.8). Therefore the chunk
compiler gives a word of length \(W+o(W)\).

#### Proof

Choose \(\theta>0\) sufficiently small relative to a fixed upper bound in
the first condition of (3.1). Then the bracket in (4.2) is bounded below
by a positive constant \(\beta=\beta(\theta)>0\) for all sufficiently
large \(m\). Every bite
therefore selects at least

\[
 \beta\frac{T}{m}                                   \tag{5.4}
\]

new tags. Rejected active tags return to the residual; they are not
charged as physical exceptions. Thus at most \(m/\beta+1=O(m)\) bites
reduce the nonexceptional residual to at most

\[
 u_*T+O(T/m).
\]

The activation probability remains at most

\[
 \frac{\theta}{mu_*}
 =\frac{\theta\omega_m}{\sqrt m}=o(1).              \tag{5.5}
\]

Adding the fixed \(o(T/\sqrt m)\) exceptional set proves (5.2).

Equation (1.9) gives

\[
 eK_s
 =o(T/\sqrt m)\,O(s\sqrt m)
 =o(Ts)=o(W).                                       \tag{5.6}
\]

The reset ledger is \(O(QT)=O(QW/s)=o(W)\), and discarding at most \(s\)
states from each original carrier costs \(O(sN_H)=O(sW/m)=o(W)\).
Together with (1.8), these are exactly the remaining physical costs.
\(\square\)

### Relation to the requested \(N_H\)-tag prefix matching

Theorem 5.1 is stated for the \(T\) labelled chunk tags created by the
return-free decomposition. It directly suffices for coefficient one
because resets cost \(o(W)\). It is not literally a matching on the
original \(N_H\) carrier tags: independently selected chunks need not
bundle into one unreset trajectory.

For an \(N_H\)-tag prefix catalogue, the same density-compensated proof
applies verbatim with \(T=N_H\) and \(s=M\), provided the corresponding
\(\mathrm{DSPDRC}_2\) holds. The owner term in (4.2) then has constant
size, giving

\[
 \left(\theta-A_m\rho\theta^2-o(1)\right)\frac{N_H}{m}            \tag{5.7}
\]

per bite; choose a sufficiently small fixed \(\theta\). This conditional
full-prefix theorem gives exactly

\[
 N_H-o(N_H/\sqrt m)                                 \tag{5.8}
\]

matched tags in \(O(m)\) additive bites. The present geodesic-grid results
do not prove the needed bundle-level \(\mathrm{DSPDRC}_2\), so (5.8)
remains conditional.

## 6. Static rectangle pruning is initially cheap

Let \(D\) be the number of simple orbit strips above one labelled chunk
tag. For a fixed controlled strip \(P\), let \(\Box(P)\) be the set of
orbit strips on other tags whose controlled intersection with \(P\)
contains two incomparable Boolean sets.

### Theorem 6.1 (static wide-overlap degree)

\[
 \boxed{
 \frac{|\Box(P)|}{D}
 =
 O\!\left(
  \frac{\rho_s\lambda_Q\,s(2Q+1)}{m^2}
 \right)
 =m^{-1+o(1)}.}                                    \tag{6.1}
\]

Thus pruning every fresh proposal whose controlled intersection with
another proposal contains an incomparable pair is initially
degree-negligible.

#### Proof

Fix \(X\in P\) of rank \(r\in[m-Q,m+Q]\). For a set \(Y\) incomparable
with \(X\), put

\[
 a=|X\setminus Y|\ge1,\qquad
 b=|Y\setminus X|\ge1.                              \tag{6.2}
\]

The stabilizer of \(X\) is transitive on the

\[
 \binom ra\binom{2m-r}b
\]

sets of type \((a,b)\). In one product grid containing \(X\), there are at
most two cells of any fixed type \((a,b)\), one in each diagonal
direction. Double counting therefore gives

\[
 d(X,Y)
 \le
 \frac{2d(X)}
      {\binom ra\binom{2m-r}b}.                     \tag{6.3}
\]

The raw rank-\(r\) load identity gives

\[
 \frac{d(X)}D
 =\frac{sT}{\binom{2m}r}
 =\rho_s\lambda_{|r-m|}
 \le\rho_s\lambda_Q.                                \tag{6.4}
\]

For a second controlled strip \(P\), the number of its cells of any fixed
type \((a,b)\) relative to \(X\) is also at most two. Since \(g=o(m)\),

\[
 \sum_{a=1}^{g+Q}\binom{m-Q}{a}^{-1}
 =(1+o(1))\frac1m,                                  \tag{6.5}
\]

and the analogous estimate holds for \(b\). Summing (6.3) first over
incomparable \(Y\in P\), then over the \(s(2Q+1)\) choices of \(X\in P\),
gives (6.1).

If two controlled common cells are incomparable, the intersection of the
two full grids is a sublattice; their meet and join supply the corresponding
compressed \(2\times2\) rectangle, possibly with meet or join outside the
controlled strips. Thus \(\Box(P)\) is exactly the controlled-strip
wide-overlap family relevant here. It does not count a full-grid rectangle
whose incomparable witnesses both lie outside the controlled strips.
\(\square\)

Theorem 6.1 is static. Conditioning on survival may concentrate the
initially rare family \(\Box(P)\), just as the four-midpoint endpoint link
can concentrate under independent thinning. No hereditary version of
(6.1) is proved.

## 7. Exact width-one chain obstruction

The rectangle lemma cannot by itself preserve the first deadline.

### Lemma 7.1 (the exact shallow chunk deadline)

For all sufficiently large \(m\),

\[
 \boxed{\bar d_1=1.}                                \tag{7.1}
\]

#### Proof

Since \(T=\lfloor M/s\rfloor N_H\) and
\(\lambda_1=(m+1)/m\),

\[
 \frac{N_1}{T}
 =
 \frac{\lambda_H/\lambda_1}{\lfloor M/s\rfloor}
 \ge\frac{s}{\lambda_1}>s-1.                       \tag{7.2}
\]

Thus \(c_1^{(s)}\ge s-1\) and \(d_1^{(s)}\le1\). On the other hand,

\[
 C_m\frac{s}{m}\Lambda_1
 =(1+o(1))(\log m)^2\frac{s}{m}=o(1),
\]

so \(h_1=1\). Equation (1.6) gives (7.1). \(\square\)

### Theorem 7.2 (one rectangle-free edge kills a base strip)

There are two legitimate buffered geodesic grids \({\cal G}^0,{\cal G}^1\)
on distinct tags with the following properties:

1. they have no common owner;
2. their full-grid intersection is a chain and hence contains no
   compressed \(2\times2\) rectangle;
3. one priority on \({\cal G}^0\) claims a common lower depth-one cell and
   a common upper depth-one cell in two different physical phase columns;
4. after selecting that decorated strip, the base grid \({\cal G}^1\)
   has \(B_1=2>\bar d_1\), and hence exact priority degree zero.

#### Proof

Write a grid as

\[
 G_{p,j}=D_p\cup B_j,
\]

where \(D_0\supset D_1\supset\cdots\supset D_g\),
\(|D_p|=m-p\), and
\(B_0\subset B_1\subset\cdots\subset B_g\),
\(|B_j|=j\), on disjoint coordinate grounds.

Choose an index \(i\) for which \(i-1,i+1\in I\). Choose two decreasing
chains \(D_p^0,D_p^1\) which meet only in one common set

\[
 D_i^0=D_i^1=:D.                                    \tag{7.3}
\]

Such chains exist because \(g=o(m)\): use disjoint ordered \(i\)-tuples of
private additions outside \(D\) for the portions \(p<i\), and disjoint
ordered \((g-i)\)-tuples of private removals inside \(D\) for the portions
\(p>i\).

Use one ordered \(g\)-set \(b_1,\ldots,b_g\), disjoint from both decreasing
chain grounds. Let \(B_j^0\) be its ordinary prefixes. For the second grid,
transpose \(b_i,b_{i+1}\) and let \(B_j^1\) be the resulting prefixes.
Then

\[
 B_j^0=B_j^1\quad(j\ne i),\qquad B_i^0\ne B_i^1.   \tag{7.4}
\]

Since the decreasing and increasing coordinate grounds are disjoint,
(7.3)--(7.4) imply

\[
 {\cal G}^0\cap{\cal G}^1
 =\{D\cup B_j:j\ne i\}.                             \tag{7.5}
\]

This is a chain. Its only possible rank-\(m\) cell would have \(j=i\), so
the two grids share no owner. It nevertheless contains

\[
 D\cup B_{i-1}=G_{i,i-1}=L_1(i-1),                 \tag{7.6}
\]

\[
 D\cup B_{i+1}=G_{i,i+1}=U_1(i+1),                 \tag{7.7}
\]

which belong to distinct physical phase columns.

By Lemma 7.1, \(\bar c_1=s-1\). Choose the one height-zero priority column
of \({\cal G}^0\) away from \(i-1,i+1\). Then both cells (7.6)--(7.7) are
claimed. Selecting this one decorated strip is a valid one-edge matching:
there is no old target and no self-repetition. In \({\cal G}^1\), the two
different phase columns now have first blocked depth one, so

\[
 B_1^Z({\cal G}^1)=2>\bar d_1=1.
\]

The exact deadline Hall criterion makes its priority count zero.
\(\square\)

The obstruction is an actual reachable residual, and every individual
row has lost only \(O(s)\) out of exponentially many targets. It refutes
the implication

\[
 \text{near-unit row marginals + no wide rectangle}
 \Longrightarrow
 \text{pointwise deadline regeneration}.           \tag{7.8}
\]

It does not refute \(\mathrm{DSPDRC}_2\): one killed base grid may carry a
negligible fraction of its tag's enormous buffered degree. Proving
\(\mathrm{DSPDRC}_2\) requires a weighted census of these thin-chain
deadline hits.

## 8. A separate common-column Hall obstruction

Rectangle geometry also does not follow from row cardinalities.

### Proposition 8.1 (two-sided depth-one cut)

Fix a coordinate \(x\). Put

\[
 {\cal L}_x
 =\{L\in\binom{[2m]}{m-1}:x\in L\},
\]

\[
 {\cal U}_{\bar x}
 =\{U\in\binom{[2m]}{m+1}:x\notin U\}.
\]

Then

\[
 \frac{|{\cal L}_x|}{N_1}
 =\frac{|{\cal U}_{\bar x}|}{N_1}
 =\frac{m-1}{2m},                                   \tag{8.1}
\]

but no \(L\in{\cal L}_x\) is contained in any
\(U\in{\cal U}_{\bar x}\). Consequently there is no positive-height
physical depth-one column using these two available rows.

#### Proof

A uniform \((m-1)\)-set contains \(x\) with probability
\((m-1)/(2m)\). A uniform \((m+1)\)-set avoids \(x\) with the same
probability. If \(L\subset U\), every element of \(L\), including \(x\),
belongs to \(U\), contradicting the definition of \({\cal U}_{\bar x}\).
\(\square\)

This cut is not claimed to be an actual residual of the intended greedy
process. It proves that proportional row marginals and rectangle pruning
alone cannot establish common-column regeneration; an integral
cross-row condition is essential.

## 9. Exact proved/conditional boundary

### Proved unconditionally

1. The exact strip normalization \(s=g-2Q+1\).
2. The static wide-rectangle degree bound (6.1).
3. Initial wide-rectangle pruning is degree-negligible.
4. The exact first deadline \(\bar d_1=1\).
5. The reachable width-one chain obstruction, Theorem 7.2.
6. The two-sided depth-one Hall cut, Proposition 8.1.
7. The one-bite implication from the explicitly stated
   \(\mathrm{DSPDRC}_2\) assumptions.

### Conditional

If \(\mathrm{DSPDRC}_2\) regenerates down to
\(u_*=1/(\sqrt m\,\omega_m)\), then the additive \(O(m)\)-round iteration
gives a target-disjoint chunk matching with \(o(T/\sqrt m)\) leave and
hence coefficient one. The analogous full-prefix \(\mathrm{DSPDRC}_2\)
would give the requested matching on
\(N_H-o(N_H/\sqrt m)\) tags.

### Unproved minimal lemma

For every reachable residual above \(u_*\), prove positivity of the exact
buffered degrees (2.5) and the density-scaled exposed-energy inequalities
(3.2)--(3.3). Equivalently, prove a weighted
clearance-majorization/proportional-load regeneration theorem which
survives the thin-chain hits of Theorem 7.2.

No existing chunk-grid identity, static overlap census, or rectangle
pruning theorem proves this lemma. Therefore coefficient one is not
claimed.
