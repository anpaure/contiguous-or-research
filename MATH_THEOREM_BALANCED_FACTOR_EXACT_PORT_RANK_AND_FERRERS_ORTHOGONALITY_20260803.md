# Balanced factors transfer exact port rank; Ferrers density is orthogonal to the literal router

**Date:** 2026-08-03  
**Status:** unconditional fixed-network theorem and symbolic counterexample.
No finite search is used.  The result identifies the sharp extra suffix
expansion hypothesis on the balanced-factor face.  It does not construct
that suffix network in the all-dimensional OR-word problem.

## 0. Result

Fix one materialized cap/guard/occurrence state and delete one fixed
compensation linkage.  Let

\[
                         B=(G,P;E)
\]

be a balanced bipartite factor with

\[
 |G|=|P|=n,
 \qquad
 \deg_B(g)=\deg_B(p)=h\ge1 .                        \tag{0.1}
\]

Assume that every factor incidence has an edge-private literal
claim-to-port prefix, that every legal claim route uses one port in its
factor menu, and that all prefix interiors are private from one fixed
suffix network.  Let \(\Gamma\) be the strict gammoid on the physical port
set \(P\) defined by linkability through that suffix network to its unused
typed sink bank.

Then the maximum number of claims simultaneously serviceable through the
factor is exactly

\[
 \boxed{\nu_{\rm claim}=r_\Gamma(P).}                \tag{0.2}
\]

Consequently, on a balanced spanning factor,

\[
 \boxed{
 \text{all claims route}
 \iff r_\Gamma(P)=|P|.}                              \tag{0.3}
\]

More generally, all but at most \(C\) claims route if and only if

\[
                         r_\Gamma(P)\ge |P|-C.       \tag{0.4}
\]

Thus the full-port condition in the private-router theorem is not merely a
modular sufficient condition on this face.  It is the exact remaining
condition.  A smaller router-good transversal cannot evade a suffix defect:
there are exactly as many claims as physical ports.

The dense Ferrers/full-erosion theorem does not imply (0.3), or any
nontrivial asymptotic substitute for it.  After fixing **any** resident
Ferrers chronology and **any** balanced factor-prefix lift on \(n\) ports,
the suffix layer can be chosen so that its port gammoid is the uniform
matroid \(U_{c,n}\), for any \(1\le c\le n\).  Every port then reaches every
one of \(n\) interchangeable sinks in a three-layer acyclic network, but

\[
                         r_\Gamma(P)=c.              \tag{0.5}
\]

In particular, the identical full-erosion or punctured-Ferrers data are
compatible both with a full literal router and with literal deficiency
\(n-1\).  The missing premise is therefore a suffix-capacity expansion
theorem, not additional hole density, row totals, per-port nonzeroness,
menu abundance, or weak connectivity.

## 1. Fixed literal interface

All data below live in one fixed residual child.  Physical vertices are
node-split and have unit capacity unless explicitly declared otherwise.

For every \(gp\in E\), fix a directed prefix

\[
                         Q_{gp}:x_g\leadsto p.       \tag{1.1}
\]

Assume:

1. distinct prefix interiors are disjoint and contain no claim start or
   physical port;
2. two prefixes may meet outside their interiors only at their common
   claim start (when they belong to the same claim) or at their common
   terminal port (when they end at the same port);
3. prefixes meet the suffix network only at their declared terminal port;
4. ports have unit physical capacity;
5. every legal factor-generated claim-to-sink path uses one prefix
   \(Q_{gp}\), then remains in the fixed suffix network; and
6. terminal type is either common within the block or retained by an exact
   state/identity gadget, so that after the declared port the legal suffix
   paths depend only on that occurrence-state port and not on a hidden
   claim identity.

Condition 5 is a port-completeness condition.  If the ambient child has an
additional route bypassing \(P\), equation (0.2) applies to the displayed
factor router, not to that larger network.

Let \(D_{\rm suf}\) be the residual suffix network and \(T\) its unused sink
bank.  Its strict gammoid \(\Gamma=L(D_{\rm suf},T)|P\) has rank

\[
 r_\Gamma(X)=\max\{\text{number of vertex-disjoint }X\text{-to-}T
                 \text{ paths}\}.                   \tag{1.2}
\]

## 2. Exact balanced rank transfer

### Theorem 2.1

Under Section 1 and (0.1), equation (0.2) holds.

### Proof

Put \(r=r_\Gamma(P)\), and choose an independent port set
\(I\subseteq P\) of size \(r\).

The reverse incidence graph has a matching which saturates \(I\).  Indeed,
for every \(Y\subseteq I\), all \(h|Y|\) factor incidences leaving \(Y\)
enter \(N_B(Y)\), and every gain in \(N_B(Y)\) has degree \(h\).  Hence

\[
                         h|Y|\le h|N_B(Y)|,
\]

so \(|N_B(Y)|\ge |Y|\).  Hall gives an injection

\[
                         \mu:I\longrightarrow G,
 \qquad \mu(p)p\in E.                               \tag{2.1}
\]

Take a suffix linkage witnessing independence of \(I\).  Concatenate its
path from \(p\) with \(Q_{\mu(p),p}\).  Prefix privacy and
prefix--suffix separation make these \(r\) paths mutually disjoint.  Thus
at least \(r\) gains are serviceable.

Conversely, any family of \(s\) serviceable gains uses \(s\) distinct
unit-capacity ports.  Port completeness and prefix--suffix separation show
that those ports have a simultaneous suffix linkage, hence form a
\(\Gamma\)-independent set.  Therefore \(s\le r_\Gamma(P)=r\).
This proves (0.2). \(\square\)

### Corollary 2.2 (left regular plus equal shores)

It is enough to assume

\[
 |G|=|P|=n,
 \qquad \deg_B(g)=h\ge1,
 \qquad \deg_B(p)\le h.                             \tag{2.2}
\]

Indeed, counting incidences gives

\[
 hn=|E|=\sum_{p\in P}\deg_B(p)\le hn,
\]

so every right degree is exactly \(h\), reducing to Theorem 2.1.  In
particular this applies to a spanning two-factor on the equal Middle-Levels
shores.

## 3. Exact cut form

Add a supersource with a unit arc to every port and a supersink after every
unit sink terminal.  For the suffix-vertex part \(W\) of a finite cut, with
the supersource in and the supersink out, let

\[
 P(W)=P\cap W,
 \qquad
 c(W)=\text{total finite capacity leaving }W.       \tag{3.1}
\]

Here \(W\) may contain terminal vertices (in which case their unit arcs to
the supersink contribute to \(c(W)\)); it never contains the supersink.
Infinite transport arcs are normalized in the usual way: a set crossed by
one is not finite-cut-admissible.  In a node-split representation,
\(P(W)\) refers to the head of the corresponding supersource-to-port arc.

### Theorem 3.1 (exact balanced router deficiency)

On the balanced factor face,

\[
 \boxed{
 n-\nu_{\rm claim}
 =n-r_\Gamma(P)
 =\max_W\bigl(|P(W)|-c(W)\bigr).}                   \tag{3.2}
\]

Consequently (0.4) is equivalent to the sharp all-cut inequality

\[
 \boxed{c(W)\ge |P(W)|-C\qquad\text{for every }W.}  \tag{3.3}
\]

### Proof

A cut whose suffix portion is \(W\) pays the \(n-|P(W)|\) source arcs of
ports left on the sink side and the suffix capacity \(c(W)\).  Max
flow/min cut gives

\[
 r_\Gamma(P)
 =\min_W\bigl(n-|P(W)|+c(W)\bigr).
\]

Rearrange and use Theorem 2.1. \(\square\)

Thus for an additive-constant construction the exact extra hypothesis is
uniform bounded deficit in (3.3).  Merely proving that every port has one
route checks only singleton cuts.  The obstruction may live on the full
bank or on any intermediate subset.

## 4. Arbitrary-rank suffix extension

### Theorem 4.1 (Ferrers orthogonality)

Fix any upstream object consisting of:

* a resident cyclic Johnson carrier;
* any full-erosion or punctured-Ferrers factor on it;
* any named lower-target allocation supported by that factor; and
* any balanced factor and private literal prefix lift satisfying Section 1
  on a port set \(P=\{p_1,\ldots,p_n\}\).

For every \(1\le c\le n\), there is an acyclic, three-layer, common-type
suffix network on the same port set and on \(n\) unused sinks whose strict
gammoid is exactly \(U_{c,n}\).  Hence the displayed claim router has exact
rank \(c\) and deficiency \(n-c\), while all upstream Ferrers data remain
unchanged.

### Proof

Introduce \(c\) unit bottleneck vertices

\[
                         b_1,\ldots,b_c
\]

and \(n\) unit terminal vertices

\[
                         t_1,\ldots,t_n.
\]

Add every arc

\[
                         p_i\to b_j,
 \qquad                  b_j\to t_\ell              \tag{4.1}
\]

for \(1\le i,\ell\le n\) and \(1\le j\le c\).  Node-split every \(b_j\)
with capacity one and put a unit terminal arc after every \(t_\ell\).  All
sinks have one common legal type.

Any port set \(X\) of size at most \(c\) links by assigning its ports
distinct bottlenecks and distinct sinks.  No set of more than \(c\) ports
links because the \(c\) split bottleneck arcs form a separator.  Therefore

\[
                         r_\Gamma(X)=\min\{|X|,c\},  \tag{4.2}
\]

which is the rank function of \(U_{c,n}\).

The construction is strictly downstream of the fixed ports.  It changes
no carrier owner, source occurrence, hole block, Ferrers deletion, target
cell, or prefix incidence.  Theorem 2.1 gives exact claim rank \(c\).
\(\square\)

This counterexample is stronger than an isolated common bottleneck:

* every port is nonloop;
* every port reaches every sink;
* the value-level port--sink reachability graph is complete;
* the suffix network is acyclic and weakly connected; and
* each port has \(cn\) displayed length-two route choices if parallel
  bottleneck/sink choices are counted.

Yet its rank is only \(c\).  Thus local route abundance and complete
value-level reachability do not estimate literal simultaneous capacity.

## 5. Consequence for dense punctured Ferrers schedules

The full-erosion theorem and its Ferrers-hole normal form determine:

1. which source occurrences are retained;
2. which coordinate--cell incidences are deleted;
3. the row-rank deficit sequence and its discrete convexity;
4. the integral one-coordinate path-flow face; and
5. after all paths are fixed, the literal target values of the cells.

None of those five items constrains the downstream separator \(c(W)\) in
(3.2).  Theorem 4.1 keeps all five items fixed while changing the router
corank to any prescribed value in \(\{0,1,\ldots,n-1\}\).

Therefore no implication of the form

\[
 \text{dense/punctured Ferrers chronology}
 \Longrightarrow r_\Gamma(P)\ge |P|-O(1)           \tag{5.1}
\]

can follow from the presently stated Ferrers hypotheses alone.  A theorem
proving (5.1) for the OR construction must add a literal relation between
the selected occurrence schedule and the residual supplier network.

The sharp added statement on a balanced factor is exactly either of the
equivalent forms

\[
 r_\Gamma(P)\ge |P|-C
 \quad\Longleftrightarrow\quad
 c(W)\ge|P(W)|-C\quad(W).                            \tag{5.2}
\]

A stronger but easier certificate is a complete path catalogue whose
fractional load is one per port and at most one on every residual physical
capacity.  Integral max flow then proves (5.2) with \(C=0\).  Establishing
such a catalogue is an additional physical router theorem; it is not a
consequence of Ferrers density.

## 6. Relation to the frozen router theorems

The regular-factor router theorem proves that full active-port rank is a
clean sufficient certificate, while correctly declining to call it
necessary for an arbitrary left-regular/right-degree-bounded factor.  That
caveat is essential when the active port shore is larger than the claim
shore: a router-good proper port subset may suffice.

Theorem 2.1 identifies the exact boundary of that caveat.  Equal shore
sizes force right regularity, and reverse Hall lets every maximum
gammoid-independent port set be used by equally many distinct gains.
Therefore no port rank is wasted and equality (0.2) holds.

The earlier common-unit-bottleneck example proves that an abstract factor
and a parent matching do not imply a suffix router.  Theorem 4.1 strengthens
that separation in two ways: it realizes every intermediate rank, and it
does so while preserving complete individual port--sink reachability.
Thus the obstruction is precisely simultaneous cut capacity, not missing
individual routes.

## 7. Scope

Theorem 4.1 is a logical nonimplication at the fixed compiler-network
interface.  It does **not** assert that every artificial suffix network in
Section 4 is realized by an actual universal OR word, nor that the current
parent-derived suffix network has low rank.  It proves that the dense
Ferrers theorem, the abstract balanced factor, and private prefixes do not
by themselves decide that rank.

Conversely, Theorem 2.1 is an exact literal theorem only under one fixed
materialized state, port completeness, capacity-faithful occurrence
identities, prefix privacy, and a typed suffix gammoid.  Transported phase 1
or any other unproved occurrence lift remains an input rather than a
consequence.

The remaining all-dimensional task is therefore precise: construct the
dense punctured Ferrers child and, in the same occurrence state after the
fixed compensation linkage, prove the cut expansion (5.2).  No additional
aggregate hole calculation can replace that cut row.
