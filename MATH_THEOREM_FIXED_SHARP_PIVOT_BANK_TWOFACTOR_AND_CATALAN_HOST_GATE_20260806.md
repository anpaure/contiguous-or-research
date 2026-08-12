# A fixed sharp-pivot bank has an exact two-factor host, while connected residence remains a Catalan port gate

**Date:** 2026-08-06  
**Method:** protected Middle-Levels extension, rooted Catalan decomposition,
component-port Hall, and uniform-marginal scaling  
**Status:** unconditional fixed-bank two-factor theorem and exact
bounded-defect connector reduction.  No connected resident carrier is
claimed.

## 0. Outcome

Let

\[
 G=ML_r
\]

be the incidence graph between ranks \(r-1\) and \(r\) of a
\((2r-1)\)-element set.  Let \(\mathcal P\) be a pairwise
incidence-vertex-disjoint bank of at most \(H\) collared sharp-pivot paths,
each with \(3d\) Johnson transitions and hence \(6d\) incidence edges.
For the audited top-deadline bank one may take

\[
 H\le31,\qquad |E(\mathcal P)|\le186d,\qquad d=\Theta(\sqrt r).
\tag{0.1}
\]

The following conclusions are proof-safe.

1. For all sufficiently large \(r\), the direct incidence lift of
   \(\mathcal P\) is contained in a simple spanning two-factor of \(G\).
   Lifting the original rank-\(m\) paths through their rank-\((m+1)\)
   unions makes this factor upper-\(q1\)-exact.
2. This gives no component bound better than the trivial \(W/3\), where
   \(W\) is one shore size.  Hamilton-anchored separate matching completion
   reduces the count to a polynomial but may create common coloured edges,
   so it is not yet a simple carrier.
3. In the complementary rooted-owner formulation, a connected completion
   with \(e\) missing derived immediate-upper colours and \(s\) path
   components is equivalent to one exact protected Catalan-forest plus
   free-port certificate.  In particular the desired connected
   \(O(1)\)-defect rooted host is the case \(e=O(1),s=1\).
4. Uniform one-edge common-basis marginals avoid every fixed literal bank
   of \(O(d)\) basis elements, but do not certify avoidance of the complete
   matching-port halo.  The latter has order \(rd\), and its expected
   intersection under a \(\Theta(1/r)\)-marginal distribution has order
   \(d\), not \(o(1)\).
5. Even a clean constant protected forest need not extend after the first
   parity matching is frozen.  Thus the first matching, upper
   representatives, connector ports, and protected paths must be chosen
   jointly.

The exact remaining owner-layer theorem is therefore not another
small-protected-factor statement.  It is a protected Catalan
representative-and-port theorem, followed by a separate global residence
extension.

## 1. Unconditional two-factor hosting

### Theorem 1.1

Assume

\[
 \Delta(\mathcal P)\le2,\qquad 6Hd\le r-2.
\tag{1.1}
\]

Then \(G\) has a simple spanning two-factor \(F\) containing every
incidence of \(\mathcal P\).

For the audited bank, take \(r=m+1\).  The rank-\((r-1)=m\) shore consists
of the original owners and the rank-\(r=m+1\) shore consists of their
immediate union colours.  Every such factor therefore visits every
immediate-upper colour exactly once and has zero upper-\(q1\) defect.

### Proof

The protected paths are incidence-vertex-disjoint, so their union has
maximum degree at most two.  Its edge count is at most \(6Hd\).  The small
protected-factor theorem applies under (1.1) and gives a spanning
two-factor containing the complete bank.

Every vertex on each shore has degree two in that factor.  In the direct
owner/upper-colour lift, a rank-\(r\) vertex lies between two distinct
rank-\((r-1)\) owners and is their union.  Hence all rank-\(r\) colours
occur exactly once.  \(\square\)

For \(H=31\), condition (1.1) is

\[
 186d\le r-2,
\tag{1.2}
\]

which is automatic for all sufficiently large \(r\).

### Scope

Theorem 1.1 is a cycle-cover theorem.  Since the Middle-Levels graph has
girth at least six, a spanning two-factor may have as many as \(W/3\)
components.  The theorem also preserves only the residence certified
inside the protected collars.  It does not constrain coordinate runs in
the unprotected completion or complete the collars' clipped outer flags.

There is a second, complementary orientation.  Complementing the
rank-\(m\) owner paths gives rank-\((m+1)\) owner paths on the same ground
set and permits the usual rooted Catalan decomposition through their lower
incidence shore.  This exchanges the two immediate palettes and also
exchanges positive-run and zero-gap residence.  The direct upper-shore
factor theorem and the rooted Catalan theorem below are therefore two
projections of the same local bank, not one automatic simultaneous host.

## 2. The strongest Hamilton-anchored quantitative relaxation

Alternately colour every protected path and write

\[
 \mathcal P=F_0\mathbin{\dot\cup}F_1.
\]

Each colour class is a matching and

\[
 f_i:=|F_i|\le3Hd.
\tag{2.1}
\]

Its all-occurrence endpoint exposures are at most \(f_i\).  Since
\(H\) is fixed and \(d=\Theta(\sqrt r)\), the sub-half exposure hypothesis
of the Hamilton-anchored matching theorem holds eventually.

### Theorem 2.1

There are perfect matchings \(M_i\supseteq F_i\) such that their coloured
union contains the oriented protected bank and has at most

\[
 1+\frac12\sum_{i=0}^1
 \left(8rf_i^2+64r^2f_i+10f_i\right)
\tag{2.2}
\]

components.  The number of common coloured edges has the same bound without
the leading one.

For the audited bank, putting \(f=93d\) gives

\[
 c\le
 1+69192\,r d^2+5952\,r^2d+930d
 =O(r^{5/2}).
\tag{2.3}
\]

### Proof

Apply the subexponential protected-matching and Hamilton-anchored completion
theorem to the two colour classes.  Formula (2.2) is its component bound.
Substitution of \(f=3Hd\), with \(H=31\), gives (2.3).  \(\square\)

This is not a simple-factor theorem: a common edge of \(M_0,M_1\) is a
coloured two-cycle and repeats its owner.  Consequently (2.2) is useful
localization of the topology debt, but it cannot be called a carrier until
the common edges and residual components are removed together.

## 3. Exact protected Catalan \((e,s)\) certificate

Fix a perfect parity matching \(M_0\) containing the first colour class of
the protected bank.  Contract its edges and use the resulting roots as the
owner vertices.  Every remaining incidence \(a\) has

* one rooted tail;
* one rooted head;
* one immediate-upper turn colour \(u(a)\); and
* one directed rooted link \(\lambda(a)\).

Let

\[
 W=\binom{2r-1}{r},\qquad
 U=\binom{2r-1}{r+1},\qquad
 C=W-U=\operatorname{Cat}_r.
\tag{3.1}
\]

The indexing shift is immaterial: these are the usual rooted-Catalan
parameters for the chosen owner shore.

### Definition 3.1

A protected Catalan \((e,s)\) certificate consists of disjoint incidence
sets \(Q_0,Q_1\) satisfying:

1. \(Q_0\) is a matching, \(\lambda(Q_0)\) is a forest, and its upper
   colours are distinct;
2. \(Q_0\) represents exactly \(U-e\) upper colours and contains every
   protected second-colour edge designated as an upper representative;
3. \(Q_1\) uses only the free outgoing and incoming ports of the directed
   path components of \(\lambda(Q_0)\);
4. \(Q_0\cup Q_1\) is a matching and
   \(\lambda(Q_0\cup Q_1)\) is a forest with exactly \(s\) components;
5. every protected second-colour edge not placed in \(Q_0\) is contained in
   \(Q_1\).

### Theorem 3.2

The owner layer has a protected directed spanning path forest with exactly
\(s\) components and exactly \(e\) missing immediate-upper colours if and
only if it has a protected Catalan \((e,s)\) certificate.

For every such certificate,

\[
 |\operatorname{Comp}\lambda(Q_0)|=C+e,
\qquad
 |Q_1|=C+e-s.
\tag{3.2}
\]

In particular a connected upper-\(q1\)-exact Hamilton path is
\((e,s)=(0,1)\), while a connected \(O(1)\)-upper-defect host is
\((e,s)=(O(1),1)\).

### Proof

The forest \(Q_0\) has \(W\) rooted vertices and \(U-e\) edges, hence
\[
 W-(U-e)=C+e
\]
components.  Adding a free-port forest \(Q_1\) with \(C+e-s\) links leaves
exactly \(s\) components.  Tail and head injectivity make every component
a coherently directed path.  The selected \(U-e\) distinct turn colours
are precisely the covered immediate-upper palette.

Conversely, choose one occurrence of every covered upper colour in the
given directed path forest and call the selected set \(Q_0\).  It is a
matching and a subforest.  The remaining edges form \(Q_1\); contracting
the \(Q_0\) components gives the stated free-port forest and the two counts.
\(\square\)

### Exact fixed-\(Q_0\) obstruction

After contracting any forced connector paths, let \(B(Q_0)\) be the
bipartite graph between the free outgoing and incoming component ports.
For a total order \(\prec\), retain only forward arcs and let

\[
 \delta_\prec=
 \max_X\left(|X|-|N_{B(Q_0)^\prec}(X)|\right).
\tag{3.3}
\]

The minimum number of acyclic connector paths obtainable from this fixed
rooted fibre is

\[
 p_{\rm forest}(B(Q_0))=\min_\prec\delta_\prec.
\tag{3.4}
\]

Thus the connected conclusion requires a cochoice of \(M_0,Q_0\) for which
the ordered deficiency is one.  Ordinary protected factor extension and
ordinary two-shore Hall do not imply (3.4).

## 4. What uniform common-basis marginals do and do not buy

Suppose a common-basis distribution has constant marginal

\[
 \Pr(a\in Q)=p=\Theta(1/r).
\tag{4.1}
\]

For a fixed literal forbidden bank \(D_0\) of \(O(d)\) ground elements,
\[
 p|D_0|=O(d/r)=o(1),
\]
so the uniform-marginal avoidance lemma supplies a common basis disjoint
from \(D_0\).

Matching-port protection is not a literal \(O(d)\)-edge condition.  Let
\(F\) be a matching of size \(f=o(r)\) in an \(r\)-regular simple bipartite
graph, and let \(D_{\rm star}(F)\) contain every non-\(F\) edge incident
with an endpoint of \(F\).  If \(c\) is the number of edges between the two
protected endpoint shores, then

\[
 |D_{\rm star}(F)|=2rf-c-f.
\tag{4.2}
\]

Since \(f\le c\le f^2\) whenever all protected edges are present,

\[
 2rf-f^2-f\le |D_{\rm star}(F)|\le2f(r-1).
\tag{4.3}
\]

Consequently, for \(p=\Theta(1/r)\),

\[
 p|D_{\rm star}(F)|=\Theta(f).
\tag{4.4}
\]

For the sharp-pivot bank \(f=\Theta(d)=\Theta(\sqrt r)\).  Therefore the
one-point marginal argument yields at best an \(O(d)\) expected collision
ledger; its collision-free criterion \(p|D|<1\) is unavailable.

Equation (4.4) is a limitation of the proof method, not a no-go theorem for
the desired basis.  A structured deletion theorem, conditional marginals,
or direct protected common-base theorem could still avoid the entire star
halo.  Plain uniform one-point marginals cannot certify it.

## 5. A sharp fixed-parity obstruction

Size, separate resource injectivity, and protected acyclicity do not suffice
after \(M_0\) is frozen.  On the five-coordinate rooted owner instance,
there is a fixed \(M_0\) and a protected set of three arcs

\[
 P=\{A\longrightarrow D,\ C\longrightarrow H,\
       J\longrightarrow F\}
\tag{5.1}
\]

with distinct tails, heads, and upper colours, whose underlying graph is
three disjoint edges, but which lies in no rooted Hamilton path.

The obstruction is forced propagation.  The occupied heads forbid the
other incoming arcs at \(D,H,F\), making one vertex the terminal.  The
remaining single choices force the chain

\[
 A\longrightarrow D\longrightarrow J\longrightarrow
 F\longrightarrow B\longrightarrow I.
\tag{5.2}
\]

Avoiding a second forced cycle fixes the outgoing edge of \(H\), but both
of its possible heads are already occupied.  This is impossible.

There is also a four-edge resource-injective protected bank in the
unrooted \(J(5,3)\) factor fibre for which exactly two spanning two-factors
exist and both have two components.  Hence the small protected-factor
theorem cannot be upgraded to protected Hamiltonicity by adding only
distinct tails, heads, immediate colours, and acyclicity.

These finite obstructions do not disprove an asymptotic theorem for the
special prospective sharp-pivot bank.  They prove that the needed theorem
must cochoose the parity matching and connector state; it cannot complete
an arbitrary protected factor post hoc.

## 6. Residence is an independent global row

The sharp collars certify length-\((d+1)\) runs for their active labels.
Their far boundary flags are clipped.  Neither Theorem 1.1 nor the Catalan
certificate constrains coordinate ages in the unprotected owner
chronology.  A Hamilton or bounded-component solution of Section 3 can
therefore fail global residence even when every protected path is locally
resident.

A proof of the requested host needs, in addition to a protected
\((e,s)\)-certificate:

1. extension or protection of all clipped packet flags;
2. a residence condition on every unprotected coordinate run and gap; and
3. compatibility with the source antecedent and deeper interval-OR deck.

These conditions are not functions only of the Catalan component graph.

## 7. Exact frontier

The fixed \(31\)-packet bank is no longer blocked at the owner-degree or
direct upper-\(q1\) factor level.  It is blocked at the correlated
selection

\[
\boxed{
\begin{array}{c}
\text{parity matching containing the first packet phase}\\
+\ \text{upper representative forest containing the second phase}\\
+\ \text{ordered free-port deficiency }O(1)\\
+\ \text{global residence and source-envelope completion}.
\end{array}}
\tag{7.1}
\]

The sharpest sufficient theorem is:

> For the prospective sharp-pivot bank, construct a protected Catalan
> \((e,1)\) certificate with absolute \(e\), and realize its owner order by
> one resident source antecedent with protected clipped flags.

That theorem would give the desired connected upper-\(q1\)-surjective
carrier with only \(O(1)\) upper defects.  None of the current small-factor,
uniform-marginal, or connector-Hall theorems proves this joint statement.

## 8. Dependencies

The proof uses the following results at their stated scopes:

1. MATH_THEOREM_D3_TOP_DEADLINE_RAY_REPAIR_BY_SHARP_PIVOTS_20260806.md;
2. MATH_THEOREM_FIXED_H_COLLAR_Q1_TWO_FACTOR_AND_ROOTED_HOST_GATE_20260801.md;
3. MATH_THEOREM_SUBEXPONENTIAL_PROTECTED_MATCHING_AND_HAMILTON_COMPLETION_20260806.md;
4. MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md;
5. MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md;
6. MATH_LEMMA_UNIFORM_MARGINAL_FIXED_BANK_AVOIDANCE_20260801.md; and
7. MATH_THEOREM_OWNER_LAYER_RAINBOW_PATH_CUT_COUNTEREXAMPLE_AND_ACYCLIC_HALL_20260801.md.
