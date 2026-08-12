# Modular-sum stars admit a constant-density depth-two Dirac packing

**Date:** 2026-08-06  
**Method:** exact balanced-exchange charging, sequential forbidden-edge
averaging, vertex pruning, and Dirac's Hamilton-cycle theorem  
**Status:** unconditional named-packet theorem.  It constructs a
constant-density family of long common-core star packets with pairwise
disjoint targets at depths one and two.  In the top PBBS slab its capacity
is more than ten times the theta-reset deficit.  Disjointness at all depths
up to (d=\Theta(\sqrt n)) remains open.

## 0. Result

Let (s\le n/2), put

\[
                         v=n-s+1,
\]

and identify the ground set with \(\mathbb Z_n\).  There is a modular-sum
class

\[
 \mathcal Q_c=
 \left\{Q\in\binom{\mathbb Z_n}{s-1}:
             \sum_{x\in Q}x=c\pmod n\right\}
\]

of size at least \(\binom n{s-1}/n\).

### Theorem 0.1 (constant-density depth-two star packing)

For every sufficiently large \(n\), there are at least

\[
 \left\lfloor\frac{|\mathcal Q_c|}{100}\right\rfloor
 \tag{0.1}
\]

distinct cores (Q_i\in\mathcal Q_c), private sets

\[
 R_i\subseteq\mathbb Z_n\setminus Q_i,
\]

and cyclic orders \(\pi_i\) on \(R_i\) such that

\[
 |R_i|\ge
 \left(1-\frac2{\sqrt{99}}\right)v,
 \tag{0.2}
\]

and all targets

\[
 Q_i+\{x\},
 \qquad
 Q_i+\{x,y\}\quad(xy\text{ an edge of }\pi_i)
 \tag{0.3}
\]

are pairwise distinct over all \(i\).

Thus the selected star packets serialize at least

\[
 \left(
  \frac1{100}\left(1-\frac2{\sqrt{99}}\right)+o(1)
 \right)
 \frac{s}{n}\binom ns
 \tag{0.4}
\]

full pieces with no rank-\(s\) or rank-\((s+1)\) collision.

For the top full PBBS slab

\[
 n=2m+1,qquad s=m-2d,
\]

where

\[
 \frac1W\binom ns\longrightarrow e^{-\pi},
 \qquad \frac{s}{n}\longrightarrow\frac12,
\]

the coefficient in (0.4) tends to

\[
 c_2=
 \frac1{200}\left(1-\frac2{\sqrt{99}}\right)e^{-\pi}
 >1.7\cdot10^{-4}.
 \tag{0.5}
\]

The theta-reset deficit coefficient is

\[
 \eta=2\sigma-1
 =4\sum_{q\ge1}e^{-4\pi q^2}
 <1.5\cdot10^{-5}.
 \tag{0.6}
\]

Hence the depth-two collision-free bank has more than ten times the raw
piece capacity needed by the theta ledger.

The theorem is a named construction.  It does not assert cyclic
equivariance or compatibility with PBBS owner envelopes.

## 1. Exact depth-two collision ports

For a core \(Q\), a packet of private length \(L\) is a cycle on a set

\[
 R\subseteq\mathbb Z_n\setminus Q,qquad |R|=L.
\]

Its depth-two targets are \(Q+e\), where \(e\) runs through the edges of
the cycle.

Take two distinct equal-colour cores (P,Q\in\mathcal Q_c).  Put

\[
 A=P\setminus Q,qquad B=Q\setminus P.
\]

The modular-sum identity gives

\[
                         \sum A=\sum B\pmod n.
 \tag{1.1}
\]

The bottom stars are disjoint, so \(|A|=|B|\ne1\).  At depth two a
collision is possible only when

\[
 |A|=|B|=2.
\]

It then occurs exactly when \(B\) is a cycle edge in the packet on \(P\)
and \(A\) is a cycle edge in the packet on \(Q\), because

\[
                         P+B=Q+A.
 \tag{1.2}
\]

Thus every previous packet exposes a finite set of forbidden edge ports in
every future complement.

### Lemma 1.1 (one-edge charging bound)

Fix a selected packet ((P,R,\pi)) and one cycle edge

\[
                         A\in E(\pi).
\]

There are at most \(\lfloor n/2\rfloor\) equal-colour future cores \(Q\)
for which this edge creates one forbidden reverse port.

#### Proof

Such a core must have the form

\[
                         Q=P-B+A,
 \tag{1.3}
\]

where (B\in\binom P2) and

\[
                         \sum B=\sum A\pmod n.
\]

For a prescribed sum, an unordered pair is determined after choosing one
of its two entries.  Hence there are at most \(\lfloor n/2\rfloor\) such
pairs \(B\).  For each one, (1.3) determines \(Q\), and its forbidden port
is precisely (B\subseteq\mathbb Z_n\setminus Q).  \(\square\)

## 2. Sequential averaging

Let

\[
                         M=|\mathcal Q_c|,
 \qquad \rho=1/100.
\]

Suppose (t<\rho M) packets have already been chosen, each of private
length at most \(v\).  For every unchosen core \(Q\), let \(F_Q\) be the
graph of complement pairs which would create a depth-two collision with an
earlier packet.

### Lemma 2.1 (average forbidden-edge bound)

At stage \(t\),

\[
 \sum_{Q\text{ unchosen}}|F_Q|
 \le \frac{tvn}{2}.
 \tag{2.1}
\]

Consequently some unchosen core satisfies

\[
 |F_Q|\le\varepsilon v^2,
 \qquad
 \varepsilon:=\frac{\rho}{1-\rho}\frac{n}{2v}
 <\frac1{99}.
 \tag{2.2}
\]

#### Proof

Every prior packet has at most \(v\) cycle edges, and Lemma 1.1 charges each
edge to at most (n/2) future forbidden ports.  This proves (2.1), even
with multiplicity.  There are at least ((1-\rho)M) unchosen cores.  Divide
(2.1) by that number and use (t<\rho M).  Since (s\le n/2), one has
(v>n/2), giving the strict final inequality in (2.2).  \(\square\)

## 3. Prune once and use Dirac

Choose a core \(Q\) satisfying (2.2), and put

\[
                         x=\sqrt\varepsilon.
\]

Delete from its \(v\)-element complement every vertex whose degree in
\(F_Q\) exceeds \(xv\).  Since

\[
 \sum_u d_{F_Q}(u)=2|F_Q|\le2\varepsilon v^2,
\]

fewer than \(2xv\) vertices are deleted.  Let \(R_Q\) be the surviving
private set and (L_Q=|R_Q|).  Then

\[
 L_Q\ge(1-2x)v,
 \tag{3.1}
\]

and the allowed graph

\[
                         G_Q=K_{R_Q}-F_Q
\]

has minimum degree

\[
 \delta(G_Q)\ge L_Q-1-xv.
 \tag{3.2}
\]

Because

\[
 x<1/\sqrt{99}<0.101,
\]

equations (3.1)--(3.2) give, for all sufficiently large \(v\),

\[
                         \delta(G_Q)\ge L_Q/2.
 \tag{3.3}
\]

Dirac's theorem supplies a Hamilton cycle \(\pi_Q\) in \(G_Q\).  Use this
cycle as the next star packet.  None of its edges lies in \(F_Q\), so it
creates no depth-two collision with an earlier packet.

Iterate until \(\lfloor\rho M\rfloor\) packets have been chosen.  This
proves pairwise depth-two disjointness.  All cores lie in one modular-sum
class, so their bottom stars are pairwise disjoint as well.  Equation (2.2)
gives

\[
 L_Q\ge
 \left(1-\frac2{\sqrt{99}}\right)v,
\]

which proves (0.1)--(0.3).

Finally,

\[
 Mv\ge\frac1n\binom n{s-1}(n-s+1)
     =\frac{s}{n}\binom ns.
\]

Multiplying by the selected fraction and the retained private fraction
proves (0.4).  The top-slab limits give (0.5), and the elementary numerical
bounds \(e^{-\pi}>1/24\) and \(\eta<1.5\cdot10^{-5}\) already give the
strict comparison needed in (0.5)--(0.6).  \(\square\)

The construction is algorithmic at the finite combinatorial level: choose
a minimum-forbidden unchosen core, prune, and find a Hamilton cycle in the
Dirac graph.

## 4. Why the same proof does not reach every depth

There is an exact extension of Lemma 1.1.

Fix a prior depth-\(j\) target

\[
                         X=P\cup I,qquad |I|=j.
\]

An equal-colour future core (Q\subset X) has complement interval

\[
                         I'=X\setminus Q,qquad |I'|=j,
\]

and must satisfy

\[
                         \sum I'=\sum X-c\pmod n.
 \tag{4.1}
\]

### Lemma 4.1 (higher-depth candidate bound)

One fixed depth-\(j\) target creates forbidden \(j\)-interval ports in at
most

\[
                         \frac1j\binom{s+j-1}{j-1}
 \tag{4.2}
\]

equal-colour future cores.

#### Proof

Choose a \((j-1)\)-subset \(J\subset X\).  Equation (4.1) determines the
unique possible last residue.  Hence there are at most
\(\binom{s+j-1}{j-1}\) successful pairs \((J,x)\).  Every valid
\(j\)-set \(I'\) is counted exactly \(j\) times, once for each choice of
its omitted member.  Distinct \(I'\) give distinct cores
\(Q=X\setminus I'\).  \(\square\)

At density \(\rho\), the same double count therefore gives average
forbidden fraction at depth \(j\) bounded by

\[
 \frac{\rho}{1-\rho}\,
 \frac Lj\,
 \frac{\binom{s+j-1}{j-1}}{\binom vj}.
 \tag{4.3}
\]

Using \(L\le v\), the factor after \(\rho/(1-\rho)\) is at most

\[
 \prod_{r=1}^{j-1}\frac{s+r}{v-j+r}.
 \tag{4.4}
\]

In particular, whenever \(s+j\le v\), every factor in (4.4) is at most
one.  This includes the complete top PBBS slab \(1\le j\le d\).  Therefore
the **average scalar forbidden density stays at most**

\[
                         \frac\rho{1-\rho}=\frac1{99}
 \tag{4.5}
\]

at every depth separately.  There is no growing scalar-density obstruction.

However, global density is not the correct Hamilton-order criterion.

### Proposition 4.2 (sharp link obstruction to density-only rounding)

Fix one coordinate \(x\) in a \(v\)-set and one depth \(j\).  Let the
forbidden family consist of all \(j\)-sets containing \(x\).  Its density
is

\[
 \frac{\binom{v-1}{j-1}}{\binom vj}=\frac jv,
 \tag{4.6}
\]

which is \(o(1)\) when \(j=o(v)\).  Nevertheless every cyclic order has
exactly \(j\) cyclic \(j\)-intervals containing \(x\), and hence no cyclic
order avoids this forbidden family.

Thus even an \(o(1)\) global forbidden density does not imply one legal
cyclic order.  The all-depth extension needs link-wise expansion (or a
multiscale pruning theorem), not another aggregate count.  Proposition 4.2
does not claim that the packet-generated forbidden families actually equal
this star; it identifies the sharp form which the next theorem must exclude.

## 5. The exact next lemma

The depth-two obstruction is now constructively closed with surplus.  The
remaining statement is:

> **Multidepth cyclic-order avoidance.**  Select a constant-density
> subfamily of modular-sum cores and a linear-size private cyclic order on
> each so that, simultaneously for (2\le j\le d), no balanced exchange
> \(Q\cup I=Q'\cup I'\) places both \(I\) and \(I'\) among the cyclic
> \(j\)-intervals.

Lemma 4.1 shows exactly why a first-moment core colour is insufficient for a
direct all-depth Dirac proof: one modular equation saves one power of \(n\),
while the number of possible exchanged positions grows like \(j\).

A successful extension needs one of:

1. a hierarchy of additional moments used without discarding a polynomial
   fraction of the cores;
2. a multiscale cyclic order whose long intervals are determined by its
   short collision-free skeleton; or
3. a direct switching theorem in the growing-state interval-order host.

Even after that lemma, the selected stars must be placed in the PBBS owner
envelopes and joined in one owner-compatible Euler chronology.

## 6. Scope

Proved here:

* a constant-density modular-core subfamily;
* explicit sequential construction of linear-size private cycles;
* pairwise disjoint depth-one and depth-two packet targets;
* more than tenfold theta-deficit capacity in the top PBBS slab; and
* the exact higher-depth candidate count exposing the limit of the method.

Not proved here:

* target disjointness for (3\le j\le d);
* cyclic-equivariant selection;
* PBBS owner-envelope or Euler compatibility;
* short-piece/global-compiler compatibility; or
* \(\nu(k)\le B(k)+O(1)\).
