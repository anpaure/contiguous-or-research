# Overlapping cores admit an exact positive role flow; cyclic ordering is the remaining owner gate

**Date:** 2026-08-13  
**Method:** modular core allocation, probabilistic spread, and an exact
capacitated bipartite flow  
**Status:** unconditional positive role-allocation theorem for all parameter
tuples satisfying the explicit inequalities below, hence for the central
pure-rail parameters for all sufficiently large dimensions.  It constructs
a nonnegative collection of legal rail shells with the exact scalar and
ground-point owner degrees.  It does **not** assert that their cyclic
orders cover every named owner once.  That last condition is isolated as
one exact ordering system in Section 6.

## 1. Pure rails and the exact core-allocation formulation

Put

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c,
 \tag{1.1}
\]

and assume

\[
 1\le c<R<k,\qquad 2c<k,\qquad 2q+3\le M.
 \tag{1.2}
\]

A legal pure rail is a triple \(\rho=(C,T,\sigma)\), where

\[
 |C|=c,\qquad C\cap T=\varnothing,\qquad
 2q+2\le |T|\le M,
 \tag{1.3}
\]

and \(\sigma\) is a cyclic order on the set \(T\).  Its owner deck is

\[
 \mathcal D(\rho)
 =\{C\cup I_i^q(\sigma):i\in\mathbb Z_{|T|}\}.
 \tag{1.4}
\]

Every deck in (1.4) is simple.

Suppose first that the rank-\(R\) owner layer is partitioned by legal
rails.  Assign an owner \(A\) to the unique core of its rail and write

\[
 y_{A,C}=1
 \quad\Longleftrightarrow\quad
 A\in\mathcal D(\rho)\text{ for a selected rail with core }C.
 \tag{1.5}
\]

Then

\[
 \sum_{C\in\binom Ac}y_{A,C}=1
 \qquad\left(A\in\binom{[k]}R\right).
 \tag{1.6}
\]

For a core \(C\), put

\[
 \mathcal F_C
 =\{A\setminus C:y_{A,C}=1\}
 \subseteq\binom{[k]\setminus C}q.
 \tag{1.7}
\]

The family \(\mathcal F_C\) is a disjoint union of all-start cyclic
\(q\)-window decks of legal periods.  Conversely, (1.6), together with
such a deck decomposition of every family (1.7), gives a pure-rail owner
factor.  Thus (1.6)--(1.7) are an exact formulation, not a relaxation.

This formulation explains why independent complete core fibres are the
wrong objects.  The owner \(A\) has \(\binom Rc\) possible cores, and the
positive construction must choose among them before it asks for cyclic
decks.

## 2. The first global congruence and why it is not an obstruction

Write

\[
 W=\binom kR,\qquad D=\binom{k-1}{R-1}=\frac RkW.
 \tag{2.1}
\]

Index a prospective collection of rail shells by \(j\in[t]\).  Shell
\(j\) has a legal period \(N_j\), a core \(C_j\), and a toggle support
\(T_j\).  Put

\[
 K_x=\sum_{j:x\in C_j}N_j,
 \qquad
 T_x^\#=|\{j:x\in T_j\}|.
 \tag{2.2}
\]

Every cyclic order of shell \(j\) uses a core point in all \(N_j\)
owners and a toggle point in exactly \(q\) owners.  Hence an owner factor
must satisfy

\[
 \boxed{K_x+qT_x^\#=D\qquad(x\in[k]).}
 \tag{2.3}
\]

In particular,

\[
 K_x\equiv D\pmod q.
 \tag{2.4}
\]

For a fixed core, (2.4) reduces to the known obstruction
\(q\mid\binom{M-1}{q-1}\).  The point of the next theorem is that, after
cores may overlap, the complete nonnegative system (2.3) is feasible.

## 3. A modular allocation lemma for weighted cores

We first record the elementary residue mechanism.

### Lemma 3.1 (consecutive weights generate every core residue)

Let \(n,n+1\) be two weights.  Suppose there are at least

\[
 Q_0=(q-1)(k-1)
 \tag{3.1}
\]

tokens of each weight.  Give every token one \(c\)-subset of \([k]\).
For every target vector \(r\in(\mathbb Z/q\mathbb Z)^k\) satisfying

\[
 \sum_xr_x\equiv c\sum_jN_j\pmod q,
 \tag{3.2}
\]

the cores can be chosen so that

\[
 \sum_{j:x\in C_j}N_j\equiv r_x\pmod q
 \qquad(x\in[k]).
 \tag{3.3}
\]

Moreover, starting from arbitrary cores on all unreserved tokens, only
\(2Q_0\) reserved token cores need be specified or changed.

#### Proof

Fix a pivot \(p\).  For each \(x\ne p\), choose a
\((c-1)\)-set \(B_x\) avoiding \(p,x\).  Reserve \(q-1\) pairs of
tokens, one of weight \(n+1\) and one of weight \(n\), for this \(x\).
In the baseline state give them respectively the cores

\[
 B_x+p,\qquad B_x+x.
\]

Switching both cores gives

\[
 (n+1)(e_x-e_p)+n(e_p-e_x)=e_x-e_p
 \pmod q.
 \tag{3.4}
\]

Complete the baseline arbitrarily and let \(b\) be its weighted core
degree vector.  Equation (3.2) says that \(r-b\) has coordinate sum zero.
It therefore has the form

\[
 r-b=\sum_{x\ne p}\delta_x(e_x-e_p),
 \qquad0\le\delta_x<q.
 \]

Switch \(\delta_x\) of the reserved pairs for \(x\).  Equation (3.4)
then gives (3.3).  \(\square\)

The lemma is positive: it assigns one actual core to every token.  It is
not a signed use of rail columns.

## 4. Exact positive core-and-toggle role flow

Take the two shortest consecutive legal periods

\[
 n=2q+2,\qquad n+1=2q+3,
 \tag{4.1}
\]

and put

\[
 h=\min\{n,M-n-1\},\qquad H=2(q-1)(k-1).
 \tag{4.2}
\]

Choose nonnegative integers \(a,b\) with

\[
 na+(n+1)b=W,qquad a,b\ge Q_0,
 \tag{4.3}
\]

and put \(t=a+b\), \(s=t-H\).  Such \(a,b\) exist whenever, for example,

\[
 W\ge nQ_0+(n+1)(Q_0+2n).
 \tag{4.4}
\]

Indeed, start with \(b\equiv W\pmod n\), and add multiples of \(n\) to
\(b\), subtracting the corresponding multiples of \(n+1\) from \(a\).
More explicitly, subtract the baseline
\(nQ_0+(n+1)Q_0\), choose
\(0\le b'<n\) with
\((n+1)b'\equiv W-nQ_0-(n+1)Q_0\pmod n\), and put

\[
 b=Q_0+b',\qquad
 a=Q_0+\frac{W-nQ_0-(n+1)Q_0-(n+1)b'}n.
\]

The last numerator is nonnegative under (4.4).

Define

\[
 E=(n+1)\sqrt{\frac{s(k+3)\log2}{2}}+H(n+1).
 \tag{4.5}
\]

### Theorem 4.1 (overlapping-core positive role ledger)

Assume (1.2), (4.3), and

\[
 \frac{Ms}{8k}>(k+2)\log2,
 \tag{4.6}
\]

\[
 E<\frac{qW}{k},
 \qquad
 \frac{hs}{2k}\ge\frac{kE}{q}.
 \tag{4.7}
\]

Then there are \(t\) legal rail shells

\[
 (C_j,T_j,N_j),qquad
 N_j\in\{n,n+1\},\quad |C_j|=c,\quad |T_j|=N_j,\quad C_j\cap T_j=\varnothing,
 \tag{4.8}
\]

such that

\[
 \sum_jN_j=W
 \tag{4.9}
\]

and the exact point equations (2.3) hold:

\[
 \boxed{
 \sum_{j:x\in C_j}N_j
 +q|\{j:x\in T_j\}|=D
 \qquad(x\in[k]).}
 \tag{4.10}
\]

Consequently, after putting an arbitrary cyclic order on every \(T_j\),
the resulting nonnegative collection of genuine simple pure rails has
exactly \(W\) owner occurrences and every ground point belongs to exactly
\(D\) of them.

#### Proof

Reserve the \(H\) tokens used by Lemma 3.1.  On each of the other \(s\)
tokens choose a core independently and uniformly from \(\binom{[k]}c\).

For a fixed point, weighted Hoeffding gives

\[
 \Pr\left(\left|K_x^{\rm rnd}
 -\frac ckW_{\rm rnd}\right|>
 (n+1)\sqrt{\frac{s(k+3)\log2}{2}}\right)
 <2^{-k-2}.
 \tag{4.11}
\]

For a fixed nonempty proper set \(X\subset[k]\), call a core
**nonextreme for \(X\)** when

\[
 0<|X\setminus C|<M.
 \tag{4.12}
\]

Because \(2c<k\), at most one of the events \(X\subseteq C\) and
\(X^c\subseteq C\) is possible.  Its probability is at most \(c/k\).
Therefore

\[
 \Pr(C\text{ is nonextreme for }X)\ge\frac Mk.
 \tag{4.13}
\]

Chernoff's inequality and (4.6), followed by a union bound over the fewer
than \(2^k\) choices of \(X\), show that with positive probability every
nonempty proper \(X\) has at least

\[
 \frac{Ms}{2k}
 \tag{4.14}
\]

nonextreme random cores.  The point events (4.11) also hold simultaneously.
Fix such a choice.

Assign the reserved cores and apply Lemma 3.1 with target
\(r_x=D\pmod q\).  Its compatibility condition holds because

\[
 kD-cW=(R-c)W=qW.
 \tag{4.15}
\]

Changing or assigning the reserved cores contributes at most \(H(n+1)\)
to the discrepancy at a coordinate.  Hence the final core loads satisfy

\[
 |K_x-cW/k|\le E,qquad K_x\equiv D\pmod q.
 \tag{4.16}
\]

Put

\[
 t_x=\frac{D-K_x}{q}.
 \tag{4.17}
\]

These are integers, and the first inequality in (4.7) makes them
nonnegative.  Also

\[
 \sum_xt_x
 =\frac{kD-\sum_xK_x}{q}
 =\frac{RW-cW}{q}=W.
 \tag{4.18}
\]

It remains to assign toggle supports.  Form the bipartite graph between
the tokens \(j\) and the points \(x\), joining \(j\) to \(x\) exactly
when \(x\notin C_j\).  Demand degree \(N_j\) at token \(j\) and degree
\(t_x\) at point \(x\), with unit edge capacities.

The exact capacitated Hall condition is

\[
 \sum_{x\in X}t_x
 \le
 \sum_j\min\{N_j,|X\setminus C_j|\}
 \qquad(X\subseteq[k]).
 \tag{4.19}
\]

For completeness, it is the ordinary max-flow min-cut condition after a
source is joined to token \(j\) with capacity \(N_j\), every allowed
token--point edge has capacity one, and point \(x\) is joined to the sink
with capacity \(t_x\).

We verify (4.19).  It is immediate for \(X=\varnothing\), and equality
holds for \(X=[k]\).  For a proper nonempty \(X\), put

\[
 z_j=|X\setminus C_j|,
 \quad
 g_N(z)=\min\{N,z\}-\frac{Nz}{M}.
 \tag{4.20}
\]

For \(1\le z\le M-1\) and \(N\in\{n,n+1\}\),

\[
 g_N(z)\ge\frac hM.
 \tag{4.21}
\]

Indeed, for \(z\le N\) use
\(g_N(z)=z(1-N/M)\), and for \(z\ge N\) use
\(g_N(z)=N(1-z/M)\).  Equations (4.14) and (4.21) give the uniform slack

\[
 S(X):=\sum_jg_{N_j}(z_j)\ge\frac{hs}{2k}.
 \tag{4.22}
\]

On the other hand,

\[
\begin{aligned}
 \sum_j\frac{N_jz_j}{M}
 &=\frac1M\sum_{x\in X}(W-K_x)\\
 &=\frac{|X|(W-D)+q\sum_{x\in X}t_x}{M}.
\end{aligned}
\tag{4.23}
\]

Since \(M-q=k-R\) and \(W-D=(k-R)W/k\), subtraction of
\(\sum_{x\in X}t_x\) from (4.23), followed by (4.22), gives

\[
\begin{aligned}
 &\sum_j\min\{N_j,z_j\}-\sum_{x\in X}t_x\\
 &=S(X)+\frac{k-R}{M}
 \left(\frac{|X|W}{k}-\sum_{x\in X}t_x\right)\\
 &\ge \frac{hs}{2k}-\frac{kE}{q}\ge0.
\end{aligned}
\tag{4.24}
\]

Here (4.16)--(4.17) bound the absolute deviation of each \(t_x\) from
\(W/k\) by \(E/q\).  Thus (4.19) holds.

Integral max flow now selects, for every token \(j\), an \(N_j\)-set
\(T_j\subseteq[k]\setminus C_j\), and selects point \(x\) in exactly
\(t_x\) supports.  Equation (4.10) follows from (4.17).  Finally, every
toggle point of a cyclic \(q\)-window deck occurs in exactly \(q\) owner
windows, independently of its cyclic order.  This proves the last
assertion.  \(\square\)

### Corollary 4.2 (central parameters)

For the central finite-OR parameters

\[
 R=\left\lceil\frac k2\right\rceil,
 \qquad q=d(k)+1=\Theta(\sqrt k),
 \tag{4.25}
\]

Theorem 4.1 applies for all sufficiently large \(k\).

#### Proof

Here \(M=k-R+q=\Theta(k)\), while \(n=2q+2=\Theta(\sqrt k)\).
Also \(W=\binom kR=2^{k-o(k)}\), whereas every quantity other than
\(W,s,t,D\) in (4.4)--(4.7) is polynomial in \(k\).  Since
\(t=\Theta(W/q)\), conditions (4.4), (4.6), and (4.7) follow for large
\(k\).  \(\square\)

This corollary is the promised positive escape from fixed-core
divisibility.  The construction uses actual cores and actual core-disjoint
toggle supports, not signed role vectors.  Supports belonging to different
shells may overlap; only the required disjointness \(C_j\cap T_j=\varnothing\)
is asserted.

## 5. What the role ledger does and does not give

Choose arbitrary cyclic orders \(\sigma_j\) on the supports from Theorem
4.1, and let

\[
 m_A=|\{j:A\in\mathcal D(C_j,T_j,\sigma_j)\}|.
 \tag{5.1}
\]

Then

\[
 \sum_Am_A=W,
 \qquad
 \sum_{A\ni x}m_A=D\quad(x\in[k]).
 \tag{5.2}
\]

Thus \(m-\mathbf1\) lies in the complete point kernel.  The signed
pure-rail theorem proves that this discrepancy is an integer sum of rail
currents.  Theorem 4.1 is stronger in a different direction: the vector
\(m\) itself is produced by a nonnegative collection of legal rails.

Neither statement implies

\[
                         m_A=1\quad\text{for every }A.
 \tag{5.3}
\]

The missing information is higher-order: which \(q\)-petal subsets become
consecutive in the chosen support orders.

## 6. The exact residual cyclic-order system

For token \(j\), let \(\Omega_j\) be the cyclic orders of \(T_j\), modulo
rotation.  Introduce binary variables

\[
 z_{j,\sigma}\in\{0,1\}
 \qquad(j\in[t],\ \sigma\in\Omega_j).
 \tag{6.1}
\]

The role ledger upgrades to an exact owner factor if and only if

\[
 \boxed{
 \sum_{\sigma\in\Omega_j}z_{j,\sigma}=1
 \qquad(j\in[t]),}
 \tag{6.2}
\]

and

\[
 \boxed{
 \sum_{j:C_j\subset A}
 \ \sum_{\substack{\sigma\in\Omega_j:\
 A\setminus C_j\in\mathcal D_q(\sigma)}}
 z_{j,\sigma}=1
 \qquad\left(A\in\binom{[k]}R\right).}
 \tag{6.3}
\]

This is now an exact multiple-choice cyclic-order matching problem.  It has
no remaining scalar or point-degree discrepancy.

There is also a precise fractional checkpoint.  In a uniform random cyclic
order on an \(N\)-set, a prescribed \(q\)-subset is one of the cyclic
windows with probability

\[
                         \frac{N}{\binom Nq}.
 \tag{6.4}
\]

Consequently uniform distributions on the order sets \(\Omega_j\) solve
the fractional form of (6.2)--(6.3) exactly if and only if

\[
 \boxed{
 \sum_{\substack{j:C_j\subset A\\A\setminus C_j\subseteq T_j}}
 \frac{N_j}{\binom{N_j}q}=1
 \qquad\left(A\in\binom{[k]}R\right).}
 \tag{6.5}

Thus the remaining positive owner program has two sharply separated rows:

1. refine the support flow so that (6.5), or another robust fractional
   ordering distribution, holds on every named owner; and
2. round that one ordering system integrally, using a protected absorber
   for only the residual named-owner leave.

Theorem 4.1 proves that fixed-core point divisibility cannot obstruct this
program globally.  Any actual positive obstruction beyond it must use the
named \(q\)-window correlations in (6.3), not merely component sizes,
ground-point degrees, or independent core fibres.

## 7. Scope

The theorem proves a genuine nonnegative overlapping-core allocation:

\[
 \boxed{
 \text{legal periods}
 +\text{actual varying cores}
 +\text{actual core-disjoint toggle supports}
 +\text{exact global point ledger}.}
\]

It does not prove owner-disjoint cyclic orders, literal lower-flag
alignment, upper-ticket preservation, socket fusion, or the common-cap
compiler.  Those rows must be imposed after, or jointly with, the exact
ordering equations (6.2)--(6.3).  In particular, this note does not infer
nonnegative semigroup normality from the already-proved signed owner
lattice.
