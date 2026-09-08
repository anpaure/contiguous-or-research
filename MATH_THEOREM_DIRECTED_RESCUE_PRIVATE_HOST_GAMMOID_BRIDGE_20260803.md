# Directed rescue menus as a private-host Rado system

**Date:** 2026-08-03  
**Status:** unconditional abstract lifting and expansion theorem, with a sharp
fixed-child counterexample. The private-host/Pascal hypotheses are not proved
for the K17 source/partner catalogue or uniformly in $k$. Consequently this
note does not prove JRRX, an additive upper bound, or a K17 word.

## 1. Why the pair oracle is not yet JRRX

The exact K17 source/partner oracle associates to one directed pair
$(x,y)$ two complete two-phase option sets and asks whether their
compatibility graph has an edge. This is the correct pair-local occurrence
test. It still has the quantifier order

\[
  \forall(x,y)\quad\exists\text{ a child and compatible option pair}. \tag{1.1}
\]

JRRX needs one child, one protected matching core, and one capacity network
fixed before selecting many repairs:

\[
  \exists(\theta',K,M,{\cal D})\quad
  \forall X\quad\exists\text{ disjoint routes for most tasks in }X. \tag{1.2}
\]

Interchanging (1.1) and (1.2) is invalid. The following theorem gives a
concrete sufficient condition under which the interchange is legitimate.

## 2. Coherent private-host atlas

Fix one fully materialized protected child \(\theta'\), one common protected
supplier core \(K\), and a maximum matching \(M\) of \(K\). Let \(S\) be the
unmatched-head sink bank for \(M\). Let \(\overline U\) be a finite master
set of **occurrence-labelled repair tasks**.

A coherent private-host atlas consists of:

1. a finite set \(P\) of occurrence-labelled packet ports;
2. for every \(p\in P\), one fixed physical packet state, including both
   phase options, flags, endpoints, histories, and all local resources;
3. a directed vertex-split unit-capacity network \({\cal D}\) from the ports
   to \(S\), containing every nonlocal supplier resource used by a packet;
4. for every task \(u\in\overline U\), a menu \(P_u\subseteq P\);

with the following **capacity-faithful lifting property**.

> If distinct tasks choose distinct ports and the chosen ports are linkable
> to \(S\) in \({\cal D}\), then the fixed packet states and the linkage
> coexist in the same child and decode to the same number of pairwise
> vertex-disjoint \(M\)-augmenting paths. Conversely, every simultaneous
> repair bank admitted by this atlas uses one port at most once, selects one
> of its menu ports for each repaired task, and its selected ports are
> linkable to \(S\) in \({\cal D}\).

A directly checkable sufficient condition for the lifting property is:

* each packet's local footprint is private to its port;
* each task's source-side footprint is private to that occurrence;
* a port has one source-independent physical state (otherwise split its
  source-dependent states into separate ports);
* all remaining shared capacity, including every local-versus-route
  interaction, is represented by vertices of \({\cal D}\);
* the decoder is lossless: it neither reuses one port for two tasks nor
  admits an unrepresented physical repair.

In particular, a packet port may internally be a K17-style directed
source/partner pair. The complete compatible two-phase option pair is frozen
as the state of that port. What is forbidden is using one option state for
one source and an incompatible state of the same physical host for another
source while pretending they are the same port.

Let \(\Gamma=\Gamma({\cal D},S)|P\) be the gammoid on ground set \(P\): a
port set is independent exactly when it can be linked vertex-disjointly to
\(S\). Equivalently, \(\Gamma\) is the restriction to the port vertices of
the strict gammoid on the full vertex set of \({\cal D}\). Thus any theorem
stated with a strict-gammoid ambient network applies after this harmless
restriction.

## 3. Exact private-host lifting theorem

### Theorem 3.1

For every exposed set \(U\subseteq\overline U\), the maximum number
\(m(U)\) of tasks simultaneously repaired by the coherent private-host atlas
is

\[
 m(U)=\min_{X\subseteq U}
 \left(|U\setminus X|+r_\Gamma\!\left(\bigcup_{u\in X}P_u\right)\right).
                                                               \tag{3.1}
\]

Equivalently, the exact unrepaired count is

\[
 \boxed{
 q(U)=\max_{X\subseteq U}
 \left(|X|-r_\Gamma\!\left(\bigcup_{u\in X}P_u\right)\right).} \tag{3.2}
\]

Moreover, the jointly repairable subsets of \(\overline U\) form the Rado
matroid induced by the menus \((P_u)\) and \(\Gamma\).

#### Proof

Rado's matroid transversal theorem gives (3.1) for choosing one distinct port
per selected task with the selected port set independent in \(\Gamma\).
The lifting property converts precisely those independent transversals into
simultaneous physical augmenting paths in the fixed child. Conversely, every
physical repair bank restricts to such an independent transversal because
ports are occurrence-labelled and every shared capacity lies in
\({\cal D}\). Subtracting (3.1) from \(|U|\) gives (3.2). The independent
partial transversals of a family of sets in a matroid form the Rado matroid.
\(\square\)

The theorem is a bridge rather than a restatement of JRRX: it gives physical
conditions under which a directed source/partner option catalogue becomes
one fixed-child gammoid atlas inside a strict-gammoid ambient network.
Pair-local option edges alone do not give the capacity-faithful lifting
property.

The previously proved right-private replacement-host Hall theorem is the
special case that stops before the supplier network: it produces a ticket
transversal, but not necessarily an independent port set in \(\Gamma\).
The extra content here is precisely the capacity-faithful decode of those
tickets to augmenting paths relative to one common protected matching.

## 4. A degree/load criterion giving hereditary expansion

The private case has a particularly simple certificate. Suppose there is an
injection from ports to the actual unmatched-head sink bank and every port
has a private route to its assigned sink, with these assigned routes pairwise
vertex-disjoint. In particular, \(|P|\le|S|\).
Then \(\Gamma\) is the free matroid on \(P\), so

\[
 r_\Gamma(Y)=|Y|.                                      \tag{4.1}
\]

Assume all but at most \(b_e\) tasks have menu size at least \(L\), and each
port lies in at most \(\Delta\) task menus. Put

\[
 \sigma=\min\left\{1,{L\over\Delta}\right\}.          \tag{4.2}
\]

### Theorem 4.1 (private-host expansion)

For every \(X\subseteq\overline U\),

\[
 \boxed{
 r_\Gamma\!\left(\bigcup_{u\in X}P_u\right)
 \ge \sigma |X|-\sigma b_e.}                          \tag{4.3}
\]

Thus the atlas satisfies the JRRX hereditary rank row with

\[
 1-\theta=\sigma,\qquad \gamma=\sigma b_e.             \tag{4.4}
\]

#### Proof

Let \(X_g\) be the nonexceptional tasks in \(X\). Count incidences between
\(X_g\) and its port neighborhood. There are at least \(L|X_g|\) incidences,
while every port receives at most \(\Delta\). Hence

\[
 \left|\bigcup_{u\in X}P_u\right|
 \ge {L\over\Delta}|X_g|
 \ge \sigma(|X|-b_e).
\]

Use (4.1). \(\square\)

The point is that the same degree and load bounds hold after restricting to
every labelled subfamily \(X\); hereditary expansion is automatic. No
union bound over shores is needed.

## 5. Bounded-interference extension

Full privacy can be relaxed without changing the proof architecture. Give
each port a fixed route to the sink bank. Form a conflict graph on ports by
joining two ports whose fixed routes share any unit-capacity resource. If
this graph has maximum degree at most \(c\), every port subset \(Y\) contains
an independent fixed-route family of size at least \(|Y|/(c+1)\). Therefore

\[
 r_\Gamma(Y)\ge {|Y|\over c+1}.                        \tag{5.1}
\]

Combining (5.1) with the incidence count proves

\[
 \boxed{
 r_\Gamma\!\left(\bigcup_{u\in X}P_u\right)
 \ge \tau |X|-\tau b_e,
 \qquad
 \tau={\min\{1,L/\Delta\}\over c+1}.}                \tag{5.2}
\]

This is JRRX with \(1-\theta=\tau\) and \(\gamma=\tau b_e\). The fixed-route
conflict bound is only a sufficient certificate; using the full gammoid rank
can be much stronger.

## 6. Concrete Pascal-packet corollary

Suppose a same-parity Pascal transition satisfies, in one child:

1. protected core loss at most \(L_0\);
2. an exposure \(U\) with \(|U|\ge\alpha\delta-b_0\);
3. a coherent packet atlas as above;
4. all but \(b_e\) exposed tasks have at least \(L_k\) packet ports;
5. every port belongs to at most \(\Delta_k\) task menus;
6. the fixed-route conflict degree is at most \(c_k\).

Put

\[
 \tau_k={\min\{1,L_k/\Delta_k\}\over c_k+1}.           \tag{6.1}
\]

If \(\tau_k\ge\tau>0\) uniformly and \(0<\alpha\tau\le1\), inequality
(5.2) and the protected-core gain identity give

\[
 \boxed{
 \delta'\le(1-\alpha\tau)\delta
       +L_0+\tau b_0+\tau b_e.}                        \tag{6.2}
\]

The raw packet scaling suggested by buffered Pascal/coatom constructions,

\[
 L_k=\Omega(k^2),\qquad
 \Delta_k=O(kd(k))=O(k^{3/2}),                         \tag{6.3}
\]

makes the menu/load factor in (6.1) equal to one only if these are counts of
**distinct selector channels after supplier routing**, not merely raw local
packet realizations. If the resulting routes are genuinely private,
\(c_k=0\), then \(\tau=1\). If their conflict degree is bounded by an
absolute constant, a uniform fixed fraction still follows. If
\(c_k\to\infty\), the fixed-route argument alone does not prove uniform
contraction even when raw menus are quadratic.

There is a useful consistency check: private routes require \(|P|\le|S|\),
and bounded-conflict fixed routes imply \(|P|\le(c_k+1)|S|\), because routes
ending at the same sink conflict. Thus a quadratic raw menu cannot be counted
as quadratic gammoid rank when its choices collapse onto only a bounded set
of supplier channels. Proving that the Pascal choices remain distinct after
this quotient is part of the missing geometric lemma.

Equation (6.2) is a concrete all-$k$ bridge to JRRX. What remains is the
geometric construction of the one common child and the private/bounded-
interference packet bank; the counting argument after that construction is
complete.

## 7. Sharp counterexample: complete rescue graph, rank one

The private-host/coherent-network hypotheses cannot be dropped.

For any \(m\ge2\), take tasks
\(U=\{u_1,\ldots,u_m\}\) and named partners
\(P=\{p_1,\ldots,p_m\}\). Let every directed pair \(u_i\to p_j\) have an
exact pair-local option. Thus the abstract rescue graph is \(K_{m,m}\), has
perfect matchings, menu size \(m\), and partner load \(m\).

Now require every physical option to use the same capacity-one occurrence
row \(z\). Each individual pair is valid, but no two repairs coexist. In a
fixed vertex-split network the ports are parallel and

\[
 r_\Gamma(P)=1.                                        \tag{7.1}
\]

For \(X=U\), the hereditary defect is \(m-1\). Hence no constants
\(\theta<1\), \(\gamma=O(1)\) can satisfy JRRX as \(m\to\infty\), despite
the complete pair-local rescue graph.

This counterexample is sharp in two ways:

* it uses one fixed child, so representation recourse is not the issue;
* the only missing row is literal capacity faithfulness.

An even stronger failure occurs when different pair edges live in different
representation completions: then there need not be any common child in which
the displayed menus exist at all.

## 8. Exact implication for the K17 oracle

All finite statements in this section are scoped to the canonical drop-12
consumer parent with final SHA-256
`fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`
and compressed SHA-256
`e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb`.
The older `dd608.../all27` prospective IDs are not admissible inputs.

The K17 source/partner theorem supplies the correct pair-local option oracle,
including alternative tuples, phase-specific reservations, flag coalescing,
and the directed-rescue rule after an exact unary common-zero certificate.
It does **not** yet supply a coherent private-host atlas.

To instantiate Theorem 3.1 from that oracle, a finite audit must additionally:

1. choose a bank of compound source/partner packet occurrences;
2. materialize the whole bank in one common table and one representation;
3. freeze one source-independent option state for each port, splitting
   alternatives into separate occurrence-labelled ports when necessary;
4. put every shared endpoint, witness row, flag, supplier, and matching vertex
   into one vertex-split capacity network;
5. verify that every independent port linkage replays as simultaneous
   augmenting paths in that child;
6. report menu lower degrees, port loads, core loss, and either full gammoid
   cuts or the sufficient conflict bound above.

The count 52,664,349 is the exact directed candidate-incidence domain
(52,568,203 unique child tables after reverse source/source deduplication).
The full child-local option/compatibility computation over that domain is not
reported. Consequently this domain is only a source for possible ports, not a
materialized port catalogue and not itself the ground of a proved gammoid.
The new theorem identifies the weakest clean upgrade: **one common
materialized host plus hereditary menu/load expansion after every literal
capacity is represented**.

That upgrade would turn the finite directed-rescue mechanism into the exact
packet-level rank row required by JRRX. Its existence remains open.
