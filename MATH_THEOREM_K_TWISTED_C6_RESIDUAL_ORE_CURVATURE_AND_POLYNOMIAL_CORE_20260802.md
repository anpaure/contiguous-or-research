# Twisted-`C6` residual Ore--Ryser: exact anchored curvature and the polynomial core

**Date:** 2026-08-02  
**Lane:** K, prospective pump/corridor planting  
**Status:** unconditional residual owner/lower-`q1` factor theorem under
explicit inequalities, including the opened seven-ear bank for every
fixed `d=O(sqrt(m))` regime at all sufficiently large `m`.  History,
ternary-partner correlation, topology, upper shadows and compiler rows are
not claimed.

## 0. Verdict

Put

\[
 n=2m-1,
 \qquad
 N={n\choose m}={n\choose {m-1}}.
\tag{0.1}
\]

Let `F` and `O` be the developed lower-facet and owner shores of the
twisted three-run `C6` pump.  Thus

\[
                         |F|=|O|=p=3n.                 \tag{0.2}
\]

The literal pump has a stronger property than the three rank-layer counts:

\[
 \max_{Y\notin O}|\{f\in F:f\subset Y\}|=1,
 \qquad
 \max_{x\notin F}|\{U\in O:x\subset U\}|=1.           \tag{0.3}
\]

After deleting `F,O`, write `G_P` for the residual containment graph.  For
`S subseteq L-F`, define its unprotected capacity-two margin

\[
 {cal M}_P(S)=
   \sum_{Y\in R-O}\min\{2,d_{G_P}(Y,S)\}-2|S|.         \tag{0.4}
\]

If `Q` is a protected two-bounded corridor bank, then the complete
Ore--Ryser system is equivalent to one exact anchored-curvature inequality,
given in Theorem 2.1.  In particular, `Q` contributes only an explicit
nonnegative cut waste; there is no hidden second Hall row.

For every nonempty `S`, the Boolean degree/codegree structure proves

\[
 {cal M}_P(S)\ge \min\{m-3,2|(L-F)\setminus S|\}       \tag{0.5}
\]

whenever either

\[
 |S|\le(m-2)(m-3)                                      \tag{0.6}
\]

or

\[
 |(L-F)\setminus S|\le{(m-1)(m-2)\over2}.              \tag{0.7}
\]

Consequently every protected bank with

\[
                 |E(Q)|\le m-3                         \tag{0.8}
\]

passes all Ore cuts in those two ranges.  For the opened seven-ear bank,
`|E(Q)|=52d+62`, so (0.8) is the explicit asymptotic condition

\[
                         m\ge52d+65.                    \tag{0.9}
\]

Every remaining possible obstruction is polynomially localized.  If
`q=|E(Q)|<=m-3`, then a violating family must satisfy (0.6)--(0.7) in the
opposite direction and

\[
 g(S):=|N_{ML_m}(S)|-|S|
 < {m-1\over m-2}(2p+q),                               \tag{0.10}
\]

hence

\[
 \min\{|S|,N-|S|\}
 < {2m^2\over n}{m-1\over m-2}(2p+q)
 =O(m^2+mq).                                            \tag{0.11}
\]

Thus the exponential Ore atlas first collapses to an exact pump-anchored
`O(m^2+mq)` shore core.  The Boolean stability assertion there is

\[
 \kappa(A)+\rho_O(A)\ge2p+\omega_Q(A)                 \tag{0.12}
\]

only on that core.  The two opposite Lovasz--Kruskal--Katona estimates in
Section 5 prove it under the following explicit arithmetic conditions.  Put

\[
 \begin{aligned}
 D&=(m-1)(m-2),\\
 G&={m-1\over m-2}(2p+q),\\
 B&={2m^2G\over 2m-1},\\
 c_m&={(m-2)(m-3)\over m(m-1)},\\
 a_m&={m^2-10m+12\over4(m-1)}.
 \end{aligned}                                           \tag{0.13}
\]

If

\[
 \begin{gathered}
 m\ge10,
 \qquad q\le m-3,
 \qquad B\le {m+2\choose3},                              \tag{0.14}\\
 a_m(m-2)(m-3)\ge q,                                     \tag{0.15}\\
 c_m\left(p+{D\over2}\right)\ge2p+q.                   \tag{0.16}
 \end{gathered}
\]

then every Ore--Ryser inequality holds and the pump plus `Q` extends to a
spanning owner/lower-`q1` two-factor.

For `q=52d+62` and `d=O(sqrt(m))`, (0.14)--(0.16) all hold for sufficiently
large `m`.  Therefore the residual Ore--Ryser gate from 2648K is
unconditionally closed in the requested asymptotic regime.

## 1. The pump is externally one-incidence

Write `h=d+1`, `s=m-3h-1>=0`, and use the three quotient roots
`R_0,R_1,R_2` and lower colours

\[
 I_0=R_0\cap R_1,
 \quad I_1=R_1\cap R_2,
 \quad I_2=R_2\cap\tau R_0.                            \tag{1.1}
\]

### Lemma 1.1 (external cross-degree one)

Every rank-`m` owner outside `O` contains at most one member of `F`, and
every rank-`(m-1)` facet outside `F` is contained in at most one member of
`O`.

#### Proof

Compare the anchored cyclic run signatures of
`I_i` and `tau^t I_j`.  When `s>0`, the complete distance-one table, up to
reversing a pair and translating both entries, is

\[
 I_0\sim I_1,
 \qquad I_1\sim I_2,
 \qquad I_2\sim\tau I_0.                               \tag{1.2}
\]

Their unions are respectively `R_1,R_2,tau R_0`, hence are pump owners.
At the threshold `s=0`, the only extra distance-one rows are

\[
 I_2\sim\tau^{,2h+1}I_0,
 \qquad I_2\sim\tau^{\,\pm2h}I_2;                     \tag{1.3}
\]

direct substitution in the six constant runs shows that their unions are
again translates of pump roots.  There are no other rows: the unique long
run/gap anchors the translation, after which a mismatch outside the listed
run boundary contributes at least two exchanges.

If an external owner contained two pump facets, those facets would be at
Johnson distance one and their union would be that external owner,
contradicting (1.2)--(1.3).  Complementing the incidence calculation, or
performing the same run comparison for `R_i`, gives the second assertion.
\(\square\)

The distinction at `s=0` is important: the pump shores then have one extra
internal incidence orbit, but (0.3) still holds.

## 2. Exact anchored-curvature form of every cut

Let `L=binom([n],m-1)` and `R=binom([n],m)`.  Fix

\[
 S\subseteq L-F,
 \qquad T=(L-F)\setminus S,
 \qquad A=F\mathbin{\dot\cup}T=L\setminus S.           \tag{2.1}
\]

For `Y in R`, put

\[
 j_A(Y)=|\{x\in A:x\subset Y\}|,
 \qquad
 c_A(Y)=(j_A(Y)-m+2)_+\in\{0,1,2\}.                   \tag{2.2}
\]

Define the full Boolean curvature and the deleted-owner return by

\[
 \kappa(A)=2|A|-\sum_{Y\in R}c_A(Y),
 \qquad
 \rho_O(A)=\sum_{Y\in O}c_A(Y).                       \tag{2.3}
\]

Let `Q` be a protected residual edge bank with maximum degree two.  Write
`q_T(Y)` for the number of `Q`-edges between `T` and `Y`, and define

\[
 \omega_Q(A)=
  \sum_{Y\in R-O}(q_T(Y)-c_A(Y))_+.                    \tag{2.4}
\]

### Theorem 2.1 (exact Ore--Ryser identity)

The Ore--Ryser inequality indexed by `S` is equivalent to

\[
                 \boxed{\kappa(A)+\rho_O(A)
                        \ge2p+\omega_Q(A).}             \tag{2.5}
\]

In particular,

\[
                 {cal M}_P(S)=\kappa(A)+\rho_O(A)-2p. \tag{2.6}
\]

#### Proof

Since `d_S(Y)=m-j_A(Y)`,

\[
 \min\{2,d_S(Y)\}=2-c_A(Y).                            \tag{2.7}
\]

Summing (2.7) over `R-O` and using
`|S|=N-p-|T|` gives (2.6).

For the protected problem, put `b(v)=2-d_Q(v)` and delete the `Q` edges.
The complementary form of Ore--Ryser says that the unsupplied right demand
must not exceed `b(T)`.  At `Y`, after cancelling the `Q` edges from `S`,
that unsupplied demand is

\[
                         (c_A(Y)-q_T(Y))_+.
\]

Adding `q_T(Y)` to both sides uses

\[
 q_T(Y)+(c_A(Y)-q_T(Y))_+
 =\max\{q_T(Y),c_A(Y)\}
 =c_A(Y)+(q_T(Y)-c_A(Y))_+.
\]

The resulting inequality is

\[
 \sum_{Y\in R-O}c_A(Y)+\omega_Q(A)\le2|T|,
\]

which is exactly (2.5).  \(\square\)

This identity also explains why a marginal count is insufficient: a
protected edge is harmless on a cut exactly when its `T`-incidence is
already absorbed by the `0/1/2` critical charge at its right endpoint.

## 3. Protected-bank reduction to an unprotected margin

### Lemma 3.1 (minimal protected obstruction)

If `Q` is not extendable around the pump, then some subgraph `H subseteq Q`
and some `S subseteq L-F` satisfy

\[
 {cal M}_P(S)<|E(H)|le
 \min\{|E(Q)|,2|T|\}.                                  \tag{3.1}
\]

#### Proof

Choose `H` edge-minimal among the nonextendable subgraphs of `Q`, and take
a strict Ore cut `S`.  No edge of `H` is incident with `S`: deleting such
an edge raises the left demand by one, while restoring it and raising the
right demand can raise the right side by at most one, so the strict integer
violation would survive.

Hence every lower endpoint of `H` lies in `T`, giving
`|E(H)|<=2|T|`.  On the right,

\[
 \min\{2-d_H(Y),d_{G_P-H}(Y,S)\}
 \ge \min\{2,d_{G_P}(Y,S)\}-d_H(Y).
\]

Summing and using the strict Ore violation gives
`|E(H)|>{cal M}_P(S)`.  \(\square\)

Therefore a bound

\[
 {\cal M}_P(S)\ge\min\{\mu,2|T|\}\quad\hbox{for all }S \tag{3.2}
\]

extends every two-bounded protected bank of size at most `mu`.

## 4. All small shores close from degree and codegree

The middle-level incidence graph has same-shore codegree at most one.  By
Lemma 1.1 every residual vertex has degree at least `m-1`.

### Lemma 4.1 (small `S`)

For `s=|S|`,

\[
 {\cal M}_P(S)
 \ge {s((m-2)^2-s)\over m+s-2}.                         \tag{4.1}
\]

Consequently

\[
 1\le s\le(m-2)(m-3)
 \quad\Longrightarrow\quad
 {\cal M}_P(S)\ge m-3.                                 \tag{4.2}
\]

#### Proof

Let `E` be the number of residual incidences from `S`, let `u` be the
number of reached right vertices, and write their degrees as `d_Y`.  Then

\[
 E\ge(m-1)s,
 \qquad
 \sum_Y {d_Y\choose2}\le{s\choose2}.
\]

Cauchy--Schwarz gives

\[
 u\ge{E^2\over E+s(s-1)}
 \ge{(m-1)^2s\over m+s-2}.                              \tag{4.3}
\]

For `1<=j<=m`,

\[
 \min\{2,j\}\ge1+{j-1\over m-1}.
\]

Summing this inequality and using (4.3) proves (4.1).  Subtracting `m-3`
from its right side factors, after clearing the positive denominator, as

\[
 (s-1)((m-2)(m-3)-s),
\]

which proves (4.2).  \(\square\)

### Lemma 4.2 (small complement)

Put `t=|T|` and `D=(m-1)(m-2)`.  If `m>=5`, then

\[
 {\cal M}_P(S)
 \ge2t-{2t(t-1)\over D}.                               \tag{4.4}
\]

Moreover `M_P(S)=2t` for `t<m-2`.  Hence

\[
 t\le {D\over2}
 \quad\Longrightarrow\quad
 {\cal M}_P(S)\ge\min\{m-3,2t\}.                      \tag{4.5}
\]

#### Proof

Let `a` and `b` count residual right vertices with respectively zero and
one neighbour in `S`.  A type-`a` vertex has at least `m-1` neighbours in
`T`, and a type-`b` vertex at least `m-2`.  Their `T`-neighbourhoods have
pairwise intersections at most one, so

\[
 a{m-1\choose2}+b{m-2\choose2}\le{t\choose2}.
\]

For `m>=5`, the second coefficient is at least half the first.  Therefore

\[
 2a+b\le {2t(t-1)\over(m-1)(m-2)}.
\]

Since `{cal M}_P(S)=2t-(2a+b)`, this proves (4.4).  If `t<m-2`, neither
type can occur.  For `m-2<=t<=D/2`, (4.4) is at least `t>=m-2`; combining
the two ranges gives (4.5).  \(\square\)

## 5. Every other obstruction has polynomial support

Let

\[
                         g(S)=|N_{ML_m}(S)|-|S|.        \tag{5.1}
\]

The full Boolean capacity-two argument gives, whenever `g(S)>=m-1`,

\[
 \sum_{Y\in R}\min\{2,d(Y,S)\}-2|S|
 \ge {m-2\over m-1}g(S).                               \tag{5.2}
\]

Deleting `O` removes at most `2p` from the left side.  Thus an obstruction
for a bank of size `q` requires (0.10).

For the cuts under consideration, `N-|S|=p+|T|>m-1`; the exact central
shadow inequality therefore gives `g(S)>=m-1`, so (5.2) applies to every
possible obstruction.

For completeness, the rank-`(m-1)`/rank-`m` incidence matrix has largest
two singular values `m,m-1`.  Tanner's bound therefore gives

\[
 g(S)\ge
 {n|S|(N-|S|)\over n|S|+(m-1)^2N}
 \ge {n\over2m^2}\min\{|S|,N-|S|\}.                   \tag{5.3}
\]

Equations (0.10) and (5.3) prove (0.11).  Lemmas 4.1--4.2 prove that a
minimal obstruction must additionally lie outside (0.6)--(0.7).  This is
the promised exact polynomial core.

### Theorem 5.1 (the polynomial core is empty under (0.14)--(0.16))

Assume (0.14)--(0.16).  Then every two-bounded protected bank `Q` with
`|E(Q)|=q` extends around the closed pump to a spanning two-factor of
`ML_m`.

#### Proof

Suppose otherwise.  Lemma 3.1 gives an edge-minimal obstruction and a cut
`S` with

\[
                         {\cal M}_P(S)<q.               \tag{5.4}
\]

If `s<=(m-2)(m-3)`, Lemma 4.1 gives
`M_P(S)>=m-3>=q>=|E(H)|`, contrary to Lemma 3.1.  If `t<=D/2`, Lemma 4.2
and the same lemma's bound `|E(H)|<=min(q,2t)` give the same contradiction.
Therefore

\[
 s:=|S|>(m-2)(m-3),
 \qquad
 t:=|(L-F)\setminus S|>{D\over2}.                       \tag{5.5}
\]

Equations (0.10)--(0.11) give

\[
             u:=\min\{s,N-s\}<B\le{m+2\choose3}.       \tag{5.6}
\]

We treat the two possible small shores separately.

**Case 1: `u=s`.**  Complementing a family of rank-`(m-1)` sets turns its
upper shadow into the lower shadow of a rank-`m` family.  Write
`s=binom(x,m)` in the Lovasz real-binomial notation.  Since

\[
 s\le {m+2\choose3}<{m+3\choose3}={m+3\choose m},
\]

we have `x<m+3`, and Lovasz--Kruskal--Katona gives

\[
             |N_{ML_m}(S)|\ge {x\choose {m-1}}
                   \ge {m\over4}s.                     \tag{5.7}
\]

In the full incidence graph, summing

\[
 \min\{2,j\}\ge1+{j-1\over m-1}
\]

over the upper shadow and using the exact incidence total `ms` yields

\[
 \sum_{Y\in R}\min\{2,d(Y,S)\}
 \ge {m(m+2)\over4(m-1)}s.                              \tag{5.8}
\]

By Lemma 1.1, the incidences from `S` into the deleted owner bank `O` are
pairwise distinct on the `S` side, so deleting `O` removes at most `s` from
(5.8).  Therefore

\[
 {\cal M}_P(S)
 \ge {m^2-10m+12\over4(m-1)}s
 =a_ms.                                                  \tag{5.9}
\]

Equations (5.5) and (0.15) contradict (5.4).

**Case 2: `u=N-s`.**  Now

\[
 a:=|A|=N-s=p+t<B\le{m+2\choose3}={m+2\choose {m-1}}.  \tag{5.10}
\]

Let `U` be the family of rank-`m` owners all of whose `m` facets lie in
`A`, and put `u_0=|U|`.  Write `a=binom(x,m-1)`, so `x<=m+2`.  If `u_0=0`,
the next bound is immediate.  Otherwise write `u_0=binom(z,m)` with
`z>=m`; then `partial U subseteq A`, and Lovasz--Kruskal--Katona gives
`binom(z,m-1)<=a`, hence `z<=x`.  Consequently in both cases

\[
                     u_0\le{x\choose m}
                         \le {3a\over m}.               \tag{5.11}
\]

Let `v_0` count owners having exactly `m-1` facets in `A`.  Counting
incidences from `A` gives

\[
                     m u_0+(m-1)v_0\le ma.              \tag{5.12}
\]

Since `2u_0+v_0` is the full critical charge of `A`, (5.11)--(5.12) imply

\[
 \begin{aligned}
 \kappa(A)
 &=2a-(2u_0+v_0)\\
 &\ge { (m-2)(m-3)\over m(m-1)}a
 =c_ma.                                                  \tag{5.13}
 \end{aligned}
\]

Using `rho_O(A)>=0`, (5.5), and (0.16),

\[
 {\cal M}_P(S)=\kappa(A)+\rho_O(A)-2p
 \ge c_m\left(p+{D\over2}\right)-2p
 \ge q,                                                  \tag{5.14}
\]

again contradicting (5.4).  Both cases are impossible.  \(\square\)

### Corollary 5.2 (opened seven-ear residual factor)

Take `q=52d+62`.  If the local pump/corridor separation hypotheses of
2648K hold and (0.14)--(0.16) hold, the closed twisted pump together with
the opened seven-ear incidence path extends to a spanning owner/lower-`q1`
two-factor.

For every fixed constant `C`, if `d<=C sqrt(m)`, then all of these
inequalities hold for sufficiently large `m`: here `q=O(sqrt(m))`,
`B=O(m^2)`, while `binom(m+2,3)=Theta(m^3)`, the left side of (0.15) is
`Theta(m^3)`, and the left side of (0.16) is `Theta(m^2)` against an
`O(m)` right side.  This proves the asserted asymptotic residual factor
theorem.

## 6. Scope and next lemma

Proved:

* the literal pump's external cross-degree-one property;
* the exact protected Ore identity (2.5), including the corridor-waste
  term;
* every small-shore and small-complement inequality;
* extension of those cuts for `|E(Q)|<=m-3`;
* polynomial localization of every remaining cut; and
* emptiness of that core under the explicit inequalities (0.14)--(0.16),
  hence unconditional residual owner/lower-`q1` completion for
  `d=O(sqrt(m))` at all sufficiently large `m`.

Not proved:

* the functional mutual-two-cycle supply for the ternary fusion;
* common endpoint histories, component escape, or zero background charge;
* deeper upper shadows, source chronology, or the compiler.

The owner/q1 residual factor row is therefore closed.  This does not close
ambient planting as a whole: the next literal rows are functional
ternary-hex partner correlation, endpoint-history acceptance, component
escape and zero nonpump background charge.  They are not consequences of
Ore--Ryser completion.
