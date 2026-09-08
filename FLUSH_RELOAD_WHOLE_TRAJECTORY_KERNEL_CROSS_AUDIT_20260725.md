# Flush/reload whole-trajectory kernel: cross-audit and exact boundary

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

Put

\[
 M=m+H,\qquad n=2Q,\qquad \ell=2n+1=4Q+1.
\]

The one-block trace, its fixed Boolean interval, and the common-core and
common-tail obstructions in
`FLUSH_RELOAD_ROUTE_BLOCK_DECOMPOSITION_AUDIT_20260725.md` are correct,
with two qualifications.

1. All statements about flags concern the truncated ranks
   \(m-Q,\ldots,m+Q\).  The quotient route does not by itself balance the
   deeper ranks \(q>Q\).
2. A concatenated cyclic block ledger must count \(\ell\), not
   \(\ell+1\), state slots per block, since the endpoint of one block is
   the source of the next.
3. Consequently the complete \(4Q+2\)-facet packet of one standalone
   block is not additive under concatenation.  Summing standalone block
   columns double-counts every shared boundary state.

There is an exact stationary result.  On every top \(U\), start from a
uniform quotient state and choose every flush/reload decoration uniformly.
Then every physical state at every fixed phase is uniform on the quotient
state space.  Taking the first **exactly \(M\)** state occurrences, using a
partial last block if necessary, gives a probability law on legal
\(M\)-state rotor trajectories with uniform one-time marginals.  Across all
tops, the expected load of every controlled rank-\(r\) flag is exactly

\[
 \mu_r={M\binom{2m}{M}\over\binom{2m}{r}}.
 \tag{0.1}
\]

Thus flush/reload blocks furnish a genuine stationary fractional
whole-trajectory kernel after symmetrization.

They do **not** furnish the integral balanced top-rooted flow.  Equation
(0.1) is the uniform expectation, whereas the required deterministic load
at each target is one of \(\lfloor\mu_r\rfloor,\lceil\mu_r\rceil\).
Nothing here produces one such integer choice, distinct middle ownership,
or one selected path from every top.  In particular, a mixture of highly
correlated route paths may have uniform one-time marginals even though
every path in its support has a macroscopic common core.

Three further exact conclusions sharpen the boundary.

* The boundary chain is regular but reducible: the boundary collar label
  set is invariant.  Every fixed-collar class is strongly connected and
  Eulerian, so the complete route catalogue has an exact integral cyclic
  multicover.  This removes denominators only at a very large replication
  scale; it does not descale to one trajectory per top.
* The determinant-\(2\) minor can be realized by three blocks in the **same
  top and the same fixed-collar class**.  Hence neither top grouping nor
  collar conditioning restores total unimodularity.
* For an \(M\)-state route trajectory, there is a set of
  \((1/2-o(1))m\) labels in every lower-\(Q\) flag and a set of
  \((1-o(1))H\) labels outside every upper-\(Q\) flag.  Under \(M\)
  independent uniform state columns, the probability of even the first
  property is \(\exp[-\Omega(mH)]\).  Therefore the abstract independent
  schedule cannot be transported to route paths by a perturbative
  coupling.  A successful integral theorem has to build the pathwise
  correlation from the start.

No coefficient-one conclusion follows.

## 1. Exact audit of one route

A boundary state on a fixed top \(U\) is

\[
 \omega=(A;z_1,\ldots,z_n;B),
 \qquad |A|=m-Q,\quad |B|=H-Q.
 \tag{1.1}
\]

Choose distinct \(x_1,\ldots,x_n,a\in A\), choose \(b\in B\), and let
\(z'_1,\ldots,z'_n\) be a permutation of the same collar label set
\(Z=\{z_1,\ldots,z_n\}\).  Define

\[
 C=A\setminus\{x_1,\ldots,x_n,a\},
 \quad D=B\setminus\{b\},
 \quad P=\{x_1,\ldots,x_n,a,b\}\cup Z.
 \tag{1.2}
\]

Then

\[
 |C|=m-3Q-1,\quad |D|=H-Q-1,\quad |P|=4Q+2,
 \tag{1.3}
\]

and these sets partition \(U\).  The core choices in the first phase are
\(x_1,\ldots,x_n,a\), and those in the second phase are
\(z'_n,\ldots,z'_1\).  Hence no member of \(C\) ever leaves the quotient
core.  Likewise no member of \(D\) ever leaves the quotient tail.  For
every controlled prefix \(F_h\), \(0\le h\le 2Q\), at every route state,

\[
 C\subseteq F_h\subseteq C\cup P.
 \tag{1.4}
\]

The moving tail label at the \(\ell+1=4Q+2\) successive state occurrences
is

\[
 b,z_n,z_{n-1},\ldots,z_1,x_1,x_2,\ldots,x_n,a.
 \tag{1.5}
\]

Therefore the upper-\(Q\) flags are exactly

\[
 \{C\cup(P-p):p\in P\},
 \tag{1.6}
\]

once each.  This verifies the moving-facet packet claimed in the audited
note.  The lower-\(Q\) core evolves by deleting successively
\(x_1,\ldots,x_n,a,z'_n,\ldots,z'_1\) and inserting successively
\(b,z_n,\ldots,z_1,x_1,\ldots,x_n\), which gives exactly the displayed
Johnson trace there.

The endpoint is

\[
 (A-a+b;z'_1,\ldots,z'_n;B-b+a).
 \tag{1.7}
\]

Thus the fixed-collar Johnson-skeleton characterization is both necessary
and sufficient.

## 2. Boundary kernel, invariant classes, and cycle accounting

Let \(\Omega_U\) be the quotient state space on \(U\).  Its cardinality is

\[
 |\Omega_U|={M!\over(m-Q)!(H-Q)!}.
 \tag{2.1}
\]

For each source state, the number of decorated routes is

\[
 D_{\rm rt}
 =(m-Q)(H-Q)n!(m-Q-1)_n
 =(m-Q)_{n+1}(H-Q)n!.
 \tag{2.2}
\]

Indeed one chooses \(a\), then the ordered \(n\)-tuple of buffers from
\(A-a\), then \(b\), then the target collar order.

At block boundaries the collar label set \(Z\), not merely its order, is
fixed.  For fixed \(Z\), let \(\Omega_{U,Z}\) be the states whose collar
set is \(Z\).  Between a prescribed source and target in this class there
are

\[
 (m-Q-1)_n
 \tag{2.3}
\]

parallel decorated routes if their unordered cores differ by one
core--tail exchange, and none otherwise.  Consequently the boundary
multigraph on \(\Omega_{U,Z}\) has indegree and outdegree \(D_{\rm rt}\).
It is strongly connected: the unordered cores form the connected Johnson
graph

\[
 J(M-2Q,m-Q),
\]

and every step may prescribe the next collar order arbitrarily.

It follows that every fixed-\(Z\) class has an Euler circuit using every
decorated route in that class once.  There are
\(\binom M{2Q}\) closed classes.  A route-only circuit cannot pass from one
of them to another; mixing the classes is an averaging operation, not a
literal collar reset.

When routes are concatenated, the endpoint occurrence of one route is the
source occurrence of the next.  Thus a cyclic ledger assigns phases

\[
 0,1,\ldots,\ell-1
 \tag{2.4}
\]

to each route edge and does not count phase \(\ell\) a second time.  An
open concatenation of \(t\) blocks has exactly

\[
 1+t\ell
 \tag{2.5}
\]

state occurrences.  By contrast, the sum of the \(t\) standalone
\((\ell+1)\)-state ledgers has \(t(\ell+1)\) occurrences and therefore
overcounts exactly \(t-1\) shared boundaries.  In a cyclic concatenation
it overcounts exactly \(t\) boundaries.  Thus the complete upper-facet
packet (1.6) is a true one-block identity but cannot be added blockwise
without subtracting the seam flags.

At the calibrated top count \(N_H=(1+o(1))W/M\) and
\(t=(1+o(1))M/(4Q)\), the number of duplicated boundary columns over all
tops would be

\[
 tN_H=(1+o(1)){W\over4Q}=o(W).
 \tag{2.6}
\]

This is small in any one rank, but summing it over \(\Theta(Q)\) controlled
ranks gives \(\Theta(W)\).  It therefore cannot be silently absorbed in a
total-row defect ledger.  The phase convention (2.4), used below, removes
the duplication exactly.  This is the exact reset/cycle accounting.

## 3. Exact symmetrized stationary trajectory law

Choose \(\omega_0\) uniformly from \(\Omega_U\).  Conditional on each
boundary state, choose its route decoration uniformly from the
\(D_{\rm rt}\) possibilities, concatenate at the endpoint, and repeat.

### Theorem 3.1 (uniform phase marginals)

Every state occurrence at every fixed route phase is uniform on
\(\Omega_U\).  In particular, the first \(L\) occurrences have uniform
one-time marginals for every prescribed \(L\), whether or not \(L-1\) is
divisible by \(\ell\).

#### Proof

At block boundaries, (2.2)--(2.3) show that the transition kernel is
doubly stochastic on every fixed-collar class.  Since the initial uniform
law mixes the collar classes with their cardinality weights, every later
boundary state is uniform on \(\Omega_U\).

Fix an internal phase.  The joint law of the uniform boundary state and
the uniform legal decoration is invariant under every permutation of
\(U\).  Route evaluation at the fixed phase is equivariant under that
action.  The symmetric group acts transitively on \(\Omega_U\), so the
evaluated state is uniform.  The same argument applies to a partial final
block. \(\square\)

Take \(L=M\).  Equivalently, take

\[
 \left\lfloor{M-1\over\ell}\right\rfloor
 \tag{3.1}
\]

complete blocks and then the necessary initial segment of one further
block.  This is an exact \(M\)-state legal trajectory; discarding an
\(O(Q)\) remainder is unnecessary at the fractional level.

For \(m-Q\le r\le m+Q\), a uniform quotient state has a uniform rank-\(r\)
flag among the \(r\)-subsets of \(U\).  Now take one independent copy of
this \(M\)-state law at every top
\(U\in\binom{[2m]}M\).  For a fixed rank-\(r\) target \(T\), its expected
total load is

\[
 M{\binom{2m-r}{M-r}\over\binom Mr}
 =M{\binom{2m}M\over\binom{2m}r}
 =\mu_r.
 \tag{3.2}
\]

The middle equality is the standard double count of pairs \((T,U)\) with
\(T\subset U\).

If an oriented candidate-star statistic is a function only of the current
quotient state, as in the offered-target energy (OB2), the same
symmetrization gives its natural fractional baseline.  The theorem does
not say that the *chosen route edge* is uniform among all rotor successors;
flush/reload edges are a structured subfamily.

## 4. Why this is not the exact balanced top-rooted flow

Let

\[
 N_r=\binom{2m}r,\qquad N_H=\binom{2m}M,
 \qquad S=MN_H.
\]

The integral balanced top-rooted theorem selects exactly \(S\) columns and
requires every rank-\(r\) target to have integer load in

\[
 \{\lfloor S/N_r\rfloor,\lceil S/N_r\rceil\}.
 \tag{4.1}
\]

The stationary route law proves only

\[
 \mathbb E L_r(T)=S/N_r.
 \tag{4.2}
\]

As a fractional point, (4.2) lies in every interval (4.1).  It is therefore
a zero-defect point of the linear relaxation.  It is not an integral
realization of (4.1).  In particular:

* a sampled target load need not be a floor or a ceiling of its mean;
* at the middle rank, where the balanced flow has capacity at most one,
  sampled route trajectories need not have globally distinct owners;
* the uniform route kernel is defined on all quotient states, not on the
  particular \(M\) columns selected under each top by an integral balanced
  flow;
* the quotient specifies no canonical flags beyond depth \(Q\).

Therefore the sentence “zero-defect fractional solution” is correct only
with the word *fractional* retained and only for the truncated rows.  It
cannot be used as an integral path factorization.

## 5. Exact pathwise common-core and common-tail constraints

Consider exactly \(M\) consecutive route states beginning at a block
boundary.  Put

\[
 s_M=\left\lceil{M-1\over4Q+1}\right\rceil.
 \tag{5.1}
\]

This is the number of route blocks which are begun, counting a partial
last block.  In one begun block, at most \(2Q+1\) labels of its boundary
core are selected, and at most one label of its boundary tail is selected
as the exchanged tail label.  Hence every such trajectory has sets
\(G,E\subset U\) satisfying

\[
 |G|\ge K_M:=m-Q-(2Q+1)s_M,
 \qquad G\subseteq L_Q(\omega_i)\quad(1\le i\le M),
 \tag{5.2}
\]

and

\[
 |E|\ge D_M:=H-Q-s_M,
 \qquad E\cap U_Q(\omega_i)=\varnothing\quad(1\le i\le M).
 \tag{5.3}
\]

To prove (5.2), start with the initial quotient core and delete from it the
union of all labels ever selected as a buffer or exchanged core label.
There are at most \((2Q+1)s_M\) such labels.  Every remaining initial-core
label stays in the quotient core throughout.  The proof of (5.3) is dual:
an initial-tail label which is never selected as a block's \(b\) remains
in the quotient tail throughout.

In the calibrated regime

\[
 Q=o(H),\qquad {Q^2\over M}\longrightarrow\infty,
 \qquad H=o(m),
 \tag{5.4}
\]

we have

\[
 K_M=(1/2-o(1))m,
 \qquad D_M=(1-o(1))H.
 \tag{5.5}
\]

Indeed

\[
 {2Q+1\over4Q+1}={1\over2}+{1\over2(4Q+1)},
\]

while \(M/Q=o(Q)=o(H)\) follows from (5.4).

### Theorem 5.1 (entropy separation from independent columns)

Let \(T_1,\ldots,T_M\) be independent uniform
\((m-Q)\)-subsets of a fixed \(M\)-set.  Then

\[
 \Pr\bigl(\exists G\in\tbinom{U}{K_M}:G\subseteq T_i
                 \text{ for every }i\bigr)
 \le
 \binom M{K_M}
 \left({(m-Q)_{K_M}\over(M)_{K_M}}\right)^M
 \tag{5.6}
\]

and hence, under (5.4),

\[
 \Pr(\text{route common-core condition})
 \le \exp\bigl[-(1/2-o(1))mH\bigr].
 \tag{5.7}
\]

#### Proof

For a fixed \(K_M\)-set \(G\), the probability that one \(T_i\) contains
it is

\[
 {\binom{M-K_M}{m-Q-K_M}\over\binom M{m-Q}}
 ={(m-Q)_{K_M}\over(M)_{K_M}}.
\]

Independence followed by a union bound gives (5.6).  Since

\[
 {(m-Q)_{K_M}\over(M)_{K_M}}
 \le\left({m-Q\over M}\right)^{K_M}
 \le\exp\left(-{K_M(H+Q)\over M}\right),
\]

and \(\binom M{K_M}\le2^M\), the right side of (5.6) is at most

\[
 \exp\{M\log2-K_M(H+Q)\}.
\]

Now use (5.5) and \(Q=o(H)\). \(\square\)

If \(\mathbb P_{\rm iid}\) is the independent uniform-column law and
\(\nu\) is any law supported on these route trajectories, Theorem 5.1
gives

\[
 \|\nu-\mathbb P_{\rm iid}\|_{\rm TV}
 \ge1-\exp[-(1/2-o(1))mH].
 \tag{5.8}
\]

This is an obstruction to a small-transport or perturbative coupling from
the independent abstract schedule.  It is not an obstruction to a new,
deliberately correlated balanced schedule; the stationary law of Section
3 is precisely such a correlated fractional law.

## 6. The determinant-2 minor survives one top and one collar

Put \(r=m+Q\), and assume \(H\ge Q+2\) and \(m\ge3Q+1\), as in the
calibrated regime.  Choose an \((r-1)\)-set \(R_0\), three further labels
\(u,v,w\), and a disjoint set \(E\) of size \(H-Q-2\).  Then

\[
 U=R_0\cup\{u,v,w\}\cup E
 \tag{6.1}
\]

is one top of size \(M\).  Choose

\[
 C\in\binom{R_0}{m-3Q-1},
 \qquad Z\in\binom{R_0\setminus C}{2Q}.
 \tag{6.2}
\]

Notice that \(|R_0\setminus C|=4Q\).  For
\(\{i,j,k\}=\{u,v,w\}\), define

\[
 P_{ij}=(R_0\setminus C)\cup\{i,j\},
 \qquad D_{ij}=E\cup\{k\}.
 \tag{6.3}
\]

Then \((C,P_{ij},D_{ij})\) has exactly the route sizes (1.3), and every
\(P_{ij}\) contains the same collar set \(Z\).  Split
\(P_{ij}\setminus Z\) into ordered buffers \(X\), one exchanged core label
\(a\), and one exchanged tail label \(b\), choosing \(i,j\in X\).  This is
possible because \(|(R_0\setminus C)\setminus Z|=2Q\): use \(i,j\) and
\(2Q-2\) of those labels as buffers, and use the two remaining labels for
\(a,b\).  This produces an actual route block \(E_{ij}\) inside the same
top \(U\) and the same boundary-collar class \(Z\).

Let

\[
 S_u=R_0+u,\qquad S_v=R_0+v,\qquad S_w=R_0+w.
\]

By (1.6), the incidence matrix of the three upper-\(Q\) targets against
the three blocks \(E_{uv},E_{uw},E_{vw}\) is

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},
 \qquad \det=-2.
\tag{6.4}
\]

Thus route-block incidence is not totally unimodular even after fixing a
top and the collar invariant.  Because \(i,j\) were chosen as buffers, the
two displayed target occurrences of \(E_{ij}\) are internal route phases,
not its terminal endpoint.  Hence the same minor survives the physical
\(\ell\)-phase convention of Section 2 and is not an artefact of seam
double-counting.  The half-vector on the three blocks gives unit load on
the displayed targets, while no integral vector supported on these three
blocks does.  Other catalogue columns may repair this local defect, so
(6.4) is not a global infeasibility theorem.

## 7. What can be factorized integrally

Let \({\cal R}_U\) be the complete decorated route catalogue on one top.
Every source state has exactly \(D_{\rm rt}\) outgoing routes, so

\[
 |{\cal R}_U|=|\Omega_U|D_{\rm rt}.
 \tag{7.1}
\]

First split the boundary vertices into a source copy and a target copy and
put one bipartite edge for every decorated route.  This bipartite
multigraph is \(D_{\rm rt}\)-regular.  Hall's theorem gives a perfect
matching; deleting it and iterating gives a decomposition into exactly
\(D_{\rm rt}\) perfect matchings.  Consequently the uniform boundary
kernel is the average of deterministic bijections of the boundary state
space, each bijection preserving the collar label set.  This is an exact
integral factorization of the **boundary** transport kernel.  It does not
imply that any one matching has balanced internal route phases.

For a fixed physical phase \(0\le j<\ell\), evaluate every route at phase
\(j\).  The evaluation map is equivariant under the full symmetric group
of \(U\), and that group is transitive on \(\Omega_U\).  Hence all its
fibres have the same size.  By (7.1), every state occurs exactly

\[
 D_{\rm rt}
 \tag{7.2}
\]

times at phase \(j\).

Now take one Euler circuit in every fixed-collar boundary class, as in
Section 2, and replace every route edge by its literal \(\ell\)-update
word.  The resulting disjoint cyclic trajectories use every decorated
route once.  By (7.2), their aggregate state and controlled-flag loads are
exactly uniform at every phase.  More precisely, a fixed rank-\(r\) flag
inside \(U\) occurs

\[
 {D_{\rm rt}|\Omega_U|\over\binom Mr}
 \tag{7.3}
\]

times at each phase and \(\ell\) times that number in the complete cyclic
ledger.  Summing the same construction over all tops gives every global
rank-\(r\) target the common integer multiplicity

\[
 {\ell D_{\rm rt}|\Omega_U|\binom{2m-r}{M-r}
       \over\binom Mr}.
 \tag{7.4}
\]

This is an exact integral cyclic multicover and proves that there is no
denominator or fractional stationarity obstruction.

Its scale is \(D_{\rm rt}\) copies of every boundary state, rather than one
\(M\)-state path per top.  The determinant minor and the common-core
constraint explain why the Eulerian multicover has no presently justified
descaling.  The exact surviving theorem is therefore:

> Choose one correlated route trajectory of exactly \(M\) states at every
> top so that the aggregate truncated flag loads are floor/ceiling
> balanced, middle owners are globally distinct, and the oriented
> collision energy is admissible.

The stationary kernel proves the barycentre of this demand.  The integral
selection remains open.
