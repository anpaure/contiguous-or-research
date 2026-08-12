# Joint PBBS host planting needs a promoted occurrence template: the native dense queue drops (d+1) ranks at its penultimate suffix

**Date:** 2026-08-07  
**Status:** exact local incompatibility theorem, exact orbit
degree/codegree calculus, and proof-safe occurrence-hypergraph cut.  The
adaptive SCD chainization, ideal rainbow host theorem, and dense delayed-
atom queue do not yet compose directly: a native dense endpoint cannot
carry the saturated penultimate member of a rephased upper flag.  A new
promoted template or a separate typed reset bridge is required before an
orbit-factor argument can start.

## 1. Parameters and the apparent synthesis

Use the odd PBBS parameters

\[
 n=2m+1,
 \qquad q=d+1,
 \qquad t=m-d,
 \qquad r=t-1=m-q.
\tag{1.1}
\]

The adaptive-phase theorem partitions the deep SCD band into pieces of
length at most (d), with zero scalar reset deficit.  A rephased upper
piece is saturated and ends with a flag

\[
 M\subset U,
 \qquad |M|=r-1,quad |U|=r,quad U=M\cup\{u\}.
\tag{1.2}
\]

The ideal rainbow theorem supplies many abstract central hosts

\[
 Y=M\cup B,
 \qquad T=U\cup B,
 \qquad |B|=q.
\tag{1.3}
\]

The dense delayed-atom theorem supplies a literal cyclic top row

\[
 S_e=\bigcup_{p=e-d+1}^{e}B_p,
 \qquad |S_e|=r,
\tag{1.4}
\]

with flat owners, simple local palettes, residence and regeneration.  The
following theorem shows why identifying (U) with (S_e) does not finish
the synthesis.

## 2. Exact penultimate-drop theorem

Let (S_e\in\binom{[n]}r) be any cyclic top row satisfying:

1. every positive coordinate run in ((1_{x\in S_e})_e) has length at
   least (d);
2. (d_J(S_e,S_{e+1})=q=d+1) for every (e); and
3. (B_p=\bigcap_{j=0}^{d-1}S_{p+j}) is the maximal delayed-atom word.

Define the natural penultimate suffix at endpoint (e) by

\[
 Z_e=\bigcup_{p=e-d+2}^{e}B_p.
\tag{2.1}
\]

### Theorem 2.1 (native penultimate rank loss)

For every (e),

\[
 \boxed{S_e\setminus Z_e=S_e\setminus S_{e+1}.}
\tag{2.2}
\]

Consequently

\[
 \boxed{|Z_e|=r-q=m-2d-2.}
\tag{2.3}
\]

#### Proof

Put (D_{e+1}=S_e\setminus S_{e+1}).  If (x\in D_{e+1}), its positive
run ends at (e).  Residence makes it present throughout
(e-d+1,\ldots,e), so (x\in B_{e-d+1}).  Every atom in (2.1) has an
intersection window containing (e+1), where (x) is absent.  Thus
(x\notin Z_e).

Conversely, let (x\in S_e\cap S_{e+1}), and let ([a,b]) be the
positive run containing those two positions.  It has length at least
(d).  There is a length-(d) subinterval of ([a,b]) whose start (p)
satisfies

\[
 e-d+2\le p\le e.
\]

Indeed (b\ge e+1), (a\le e), and (a\le b-d+1); hence one may choose
(p) in

\[
 [\max(a,e-d+2),\min(e,b-d+1)].
\]

Then (x\in B_p\subseteq Z_e).  This proves (2.2).  The distance
condition gives (|D_{e+1}|=q), while every atom in (2.1) is contained
in (S_e).  Equation (2.3) follows.  \(\square\)

### Corollary 2.2 (native dense flags have degree zero)

At a rephased upper endpoint, the literal depth-((d-1)) suffix must be
the saturated penultimate target (M) of rank (r-1).  In every native
dense delayed-atom realization it instead has rank (r-q).  Since
(q=d+1>1), no native dense endpoint realizes (1.2).

Equivalently, if the occurrence-host incidence hypergraph requires the
same endpoint simultaneously to carry the rephased SCD flag and the native
dense queue suffixes, every flag has degree zero.

This is stronger than the frozen-envelope estimate (D_f\le d+2): on
the direct same-endpoint identification, the required occurrence does not
exist at all.

## 3. The exact missing promotion ticket

Although (Z_e) is too small, (2.2) identifies the only possible
saturated penultimate set between (Z_e) and (S_e).  For
(u\in D_{e+1}), put

\[
 M_{e,u}=S_e\setminus\{u\}
 =Z_e\cup(D_{e+1}\setminus\{u\}).
\tag{3.1}
\]

Thus a **promotion ticket** must make the (d=q-1) coordinates

\[
 D_{e+1}\setminus\{u\}
\tag{3.2}
\]

visible in the penultimate suffix while keeping (u) invisible and
retaining the top value (S_e).

No source word whose letters remain the maximal delayed atoms can do this:
every coordinate of (D_{e+1}) is absent from every atom in (2.1), by
(2.2).  Therefore a successful joint PBBS template must do at least one of
the following.

1. Add a nonmaximal promotion collar and reprove flatness/residence.
2. Carry (M) at a separate interlaced endpoint and prove the required
   common-history bridge.
3. Use the dense queue only as a separate reset reservoir, with a typed
   occurrence transfer from the adaptive SCD endpoint.

The existing three theorems supply none of these bridges.

## 4. Orbit hypergraph for a promoted template

The right way to avoid frozen-envelope degree collapse is to choose the
coordinate labelling, flag, host and occurrence in one template embedding.
The following calculus makes that proposal exact.

Let (Pi) be a fixed abstract PBBS packet on (v) coordinate labels.
It contains finitely many resource occurrences of several types.  A type
(\tau) has an underlying (a_\tau)-set partitioned into labelled role
cells of sizes

\[
 \alpha_{\tau,1},\ldots,\alpha_{\tau,j_\tau},
 \qquad\sum_h\alpha_{\tau,h}=a_\tau.
\]

Let (m_\tau) be the number of occurrences of that type in (Pi).
Develop (Pi) under every injection of its (v) abstract coordinates
into ([n]), retaining parallel block copies.

### Theorem 4.1 (exact typed orbit degrees)

Every named vertex of type (\tau) has degree

\[
 \boxed{
 D_\tau=m_\tau
 \left(\prod_h\alpha_{\tau,h}!\right)
 (n-a_\tau)_{v-a_\tau}.}
\tag{4.1}
\]

For two named typed vertices (X,Y), fix their complete role-refined Venn
signature (\eta).  Let

* (u_\eta=|X\cup Y|);
* (g_\eta) be the product of factorials of all role-refined Venn atom
  sizes; and
* (\kappa_{\tau,\sigma,\eta}) be the number of ordered distinct template
  occurrence pairs of types (\tau,\sigma) with signature (\eta).

Then their codegree is

\[
 \boxed{
 D(X,Y)=\kappa_{\tau,\sigma,\eta},
 g_\eta,(n-u_\eta)_{v-u_\eta}.}
\tag{4.2}
\]

#### Proof

Choose the template occurrence.  Map each labelled role cell bijectively
to its named cell, giving the factorial product in (4.1), then inject every
remaining abstract coordinate outside the named resource.  This proves
(4.1).  For a pair, choose the ordered template pair, biject every atom of
the common role-refined Venn partition, and inject the remaining
(v-u_\eta) coordinates outside (X\cup Y).  This is (4.2).
\(\square\)

For untyped sets of ranks (a,b) and intersection (z), (4.2) reduces to

\[
 \kappa_{a,b,z},z!(a-z)!(b-z)!
 (n-a-b+z)_{v-a-b+z}.
\tag{4.3}
\]

### Dense-queue specialization

The explicit queue has

\[
 v=m+q,qquad L=q(q+1)
\]

and (L) top targets of rank (r=m-q) and (L) owners of rank (m).
Hence its complete orbit has degrees

\[
 \boxed{D_{\rm top}=Lr!(m+q+1)_{2q},}
\tag{4.4}
\]

and

\[
 \boxed{D_{\rm owner}=Lm!(m+1)_q.}
\tag{4.5}

All top--top, top--owner and owner--owner codegrees are given exactly by
(4.2), with the corresponding finite intersection inventory of one queue
ring.

If a future promoted template has (h) flag ports of type
((M,u)), (|M|=r-1), its flag degree is

\[
 \boxed{D_{\rm flag}=h(r-1)!(m+q+1)_{2q}.}
\tag{4.6}

For a compatible flag--host pair with

\[
 T=M\mathbin{\dot\cup}\{u\}\mathbin{\dot\cup}B,
 \qquad |B|=q,
\]

the role-bijection factor in (4.2) is

\[
 (r-1)!q!.
\tag{4.7}

The native dense template has (h=0) by Corollary 2.2.  Formula (4.6)
becomes relevant only after a promotion/transfer template is actually
constructed.

## 5. The joint occurrence hypergraph

Assume such a promoted or transferred template has been specified.  Let

* (mathcal F) be the rephased upper flags;
* (mathcal R) be successor occurrence resources;
* (mathcal P) be lag occurrence resources;
* (mathcal Y) and (mathcal T) be coatom and owner resources.

For each flag (f), form the (4)-uniform hypergraph
(\mathcal H_f) whose edges

\[
 \{q,p,Y,T\}
\tag{5.1}
\]

are precisely the quadruples realized together with (f) by one common
template embedding and satisfying the complete phase, envelope, residence
and state conditions.  Defining candidates by common embeddings, rather
than intersecting separately frozen projections, is the quantifier change
which avoids the artificial degree collapse.

### Theorem 5.1 (proof-safe joint planting cut)

If, for every nonempty (X\subseteq\mathcal F),

\[
 \boxed{
 \nu\!\left(\bigcup_{f\in X}\mathcal H_f\right)
 >4(|X|-1),}
\tag{5.2}
\]

then one can choose one common host/occurrence quadruple for every flag,
with all successor positions, lag positions, coatoms and owners pairwise
disjoint.

#### Proof

This is the Aharoni--Haxell rainbow-matching criterion for a family of
(4)-uniform hypergraphs.  \(\square\)

If lag and successor are one atomic packet, replace (5.1) by a
(3)-uniform resource edge and (4) by (3) in (5.2).  If a preselected
bank of complete typed packets is already internally resource-disjoint,
ordinary bipartite Hall between flags and packet vertices is exact:

\[
 |N(X)|\ge|X|qquad(X\subseteq\mathcal F).
\tag{5.3}
\]

These are the weakest proof-safe all-cut formulations at the corresponding
levels of resource coalescing.  Separate Hall on successor and lag
projections is insufficient.

### Corollary 5.2 (degree-only sufficient condition)

Suppose every (\mathcal H_f) has at least (D_0) candidate edges and
every resource vertex belongs to at most (\Delta) candidate edges in any
coloured union.  If

\[
 \boxed{D_0>16\Delta,}
\tag{5.4}
\]

then (5.2) holds.

#### Proof

For (X\ne\varnothing), the coloured union has at least (|X|D_0)
edge copies.  A greedy matching in a (4)-uniform hypergraph with maximum
vertex degree (\Delta) has size at least

\[
 \frac{|X|D_0}{4\Delta}>4|X|>4(|X|-1).
\]

Apply Theorem 5.1.  \(\square\)

The constant (16) is only a robust sufficient bound.  The matching-number
cut (5.2) is strictly weaker and should be the primary target.

## 6. Protected-factor interpretation

The ideal rainbow theorem works because every flag sees the complete
Boolean host universe and the graph ratio tends to (e^{\pi/4}>2).  A
frozen literal occurrence first selects its safe envelope and only then
asks for a host; this reverses the quantifiers and reduces its candidate
degree to at most (d+2), or to zero on the direct dense endpoint.

A successful protected-factor proof must instead select a matching of
whole promoted template embeddings.  The orbit formulas (4.1)--(4.2)
provide exact marginal degrees and codegrees before conditioning.  What
must then be proved is robust extendability after deleting the already
used pieces:

\[
 \nu\!\left(\bigcup_{f\in X}\mathcal H_f^{\rm residual}\right)
 >4(|X|-1)
 \quad\text{for every }X\subseteq\mathcal F.
\tag{6.1}
\]

Pairwise small codegree of the symmetric orbit is useful for an
approximate nibble, but it does not imply (6.1) after occurrence/state
conditioning.  The complete local promotion ticket (3.2), not another
owner-count estimate, is the first missing ingredient.

## 7. Verdict

The three PBBS ingredients currently close different projections:

1. adaptive rephasing closes endpoint/reset **counts**;
2. the dense queue closes one-component literal common history and local
   owner/(q1)/residence rows;
3. the ideal rainbow theorem closes abstract flag--central-host
   **incidence**.

They do not yet share one occurrence-labelled object.  Directly combining
them is impossible because the dense queue's penultimate suffix loses
(q=d+1) coordinates, whereas the rephased SCD flag loses one.

The exact next lemma is therefore:

> **Promoted dense-reset template lemma.**  Construct one regenerative
> local template carrying the promotion set
> (D_{e+1}\setminus\{u\}), or an equivalent separate-endpoint transfer,
> while preserving flat owners, both immediate palettes, residence and
> the lag envelope; then prove the residual all-cut (5.2) for its symmetric
> orbit.

Until that template exists, the joint occurrence hypergraph has no direct
dense flag edges, and no protected-factor theorem can bridge the frozen-
envelope collapse.
