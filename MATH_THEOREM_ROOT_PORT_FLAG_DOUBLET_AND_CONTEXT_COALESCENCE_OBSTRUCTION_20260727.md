# Root-port flag matchings do not coalesce for free: a near-perfect doublet factor and a missing context resource

Date: 2026-07-27

Method: pure mathematics.  No computation, search, solver, or external
input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad
 \mathfrak F=\{(U,x):U\in\tbinom{[n]}M,\ x\in U\}.
\]

The fixed six-uniform root-port flag hypergraph from
`MATH_AUDIT_TRIPLE_PRODUCT_CELL_ABSTRACT_RECYCLING_AND_ROOT_PORT_OBSTRUCTION_20260727.md`
does have near-perfect matchings.  This fact alone, however, cannot be
upgraded by a sparse component-merging argument to one long trail on each
top.  There is an exact near-perfect counterexample.

1. There is a flag matching covering \((1-o(1))|\mathfrak F|\) outgoing
   and incoming flags for which the local directed graph on almost every
   top is a disjoint union of directed 2-cycles and has
   \((1-o(1))M/2\) components.
2. Turning this particular matching into local simple paths by bounded
   packet replacements requires changing \(\Omega(MN)\) packet
   occurrences, where \(N=\binom nM\).  Thus no `take a Pippenger--Spencer
   matching and merge its components with o(W) switchings' theorem is
   possible.
3. Even a specially selected flag matching whose local arcs already form
   long paths and whose packet precedence relation is acyclic still does
   not contain enough information for the physical lift.  Every literal
   three-top packet has a common **oriented core-order signature** on its
   three source words.  Root-port flags do not record this signature, and
   two words with identical required flags may have incompatible
   signatures.

Consequently the requested coalescence theorem is false if its hypotheses
are only the fixed-six flag matching, local path components, and a global
acyclic precedence order.  A positive theorem must select the matching and
the word contexts simultaneously (or use the twelve-top position transport
as a genuinely context-aware macro).  This does not refute the existence
of such a specially designed selection; it refutes the proposed lossless
upgrade from the abstract flag matching.

## 1. Oriented packets and their inverses

For an \((M-2)\)-set \(C\) and distinct \(x,y,a\notin C\), write

\[
 e(C;x,y,a)
\]

for the oriented packet with local flag arcs

\[
\begin{array}{rcl}
 (C+xy,x)&\longrightarrow&(C+xy,y),\\
 (C+ya,y)&\longrightarrow&(C+ya,a),\\
 (C+ax,a)&\longrightarrow&(C+ax,x).
\end{array}
\tag{1.1}
\]

Its inverse orientation is

\[
 \bar e=e(C;x,a,y),
\tag{1.2}
\]

and has the reverse arc on each of the same three tops.  Hence \(e\) and
\(\bar e\) use disjoint signed flag resources: on a top carrying the
special pair \(\{u,v\}\), one uses \((U,u)^+,(U,v)^-\), and the other
uses \((U,v)^+,(U,u)^-\).

Call \(\{e,\bar e\}\) an **inverse doublet**.

## 2. A near-perfect matching made entirely of inverse doublets

Let the unsigned special-label resources be

\[
                         \mathcal R=\{(U,x):x\in U\}.
\]

An unoriented label triangle on

\[
 C+xy,\qquad C+ya,\qquad C+ax
\]

uses the six resources consisting of its two special labels on each of
the three tops.  The resulting six-uniform hypergraph on \(\mathcal R\)
is regular of degree

\[
                         (M-1)(n-M)
\]

and has relative maximum pair codegree \(O(m^{-1})\).  This is Lemma 6.3
of
`MATH_AUDIT_REROOT_CONVEYOR_FUSION_COLUMN_INVARIANT_AND_DENSE_SUPPORT_20260727.md`.
The fixed-uniformity Pippenger--Spencer theorem therefore supplies an
unsigned triangle matching \(\mathcal T\) covering

\[
                         (1-o(1))MN
\tag{2.1}
\]

resources.

For every \(T\in\mathcal T\), insert both orientations \(e_T,\bar e_T\).
Different members of \(\mathcal T\) use disjoint unsigned resources, and
the two orientations of one member use complementary signs.  Therefore

\[
             \mathcal P=\bigcup_{T\in\mathcal T}\{e_T,\bar e_T\}
\tag{2.2}
\]

is a matching in the signed root-port flag hypergraph.

### Theorem 2.1 (near-perfect doublet factor)

The matching \(\mathcal P\) covers \((1-o(1))MN\) outgoing flags and the
same number of incoming flags.  On every top \(U\), its local directed
graph is a vertex-disjoint union of directed 2-cycles.  On all but
\(o(N)\) tops it contains \((1-o(1))M/2\) such components.

#### Proof

If an unsigned triangle uses \((U,x),(U,y)\), its two orientations give
exactly the arcs \(x\to y\) and \(y\to x\).  Since \(\mathcal T\) is a
resource matching, no top-label vertex belongs to a second such pair.
Thus the asserted local graph is a disjoint union of 2-cycles.

Equation (2.1) says the sum, over all tops, of the number of covered
labels is \((1-o(1))MN\).  As every top has at most \(M\) covered labels,
all but \(o(N)\) tops have \((1-o(1))M\) covered labels after passing to
the usual near-perfect subfamily (or, equivalently, after discarding the
exceptional tops charged by the total deficit).  Two labels form each
component. \(\square\)

This construction has the same asymptotically optimal flag coverage as
Corollary 8.2 of the product-cell audit, but the worst possible local
component count.

## 3. A linear edit lower bound

Consider a packet edit which deletes or replaces a bounded number of
oriented packet occurrences.  An untouched inverse doublet still contains
both opposite arcs on each of its three local label pairs, and therefore
still contributes a directed 2-cycle component on those labels.

### Theorem 3.1 (sparse merging is impossible)

Let \(\mathcal P'\) be another signed-flag matching obtained from the
matching \(\mathcal P\) of Theorem 2.1 by changing \(s\) oriented packet
occurrences.  Then at least

\[
                         |\mathcal T|-s
\tag{3.1}
\]

inverse doublets remain intact.  In particular, if \(s=o(MN)\), the local
graphs still contain \(\Theta(MN)\) vertex-disjoint directed 2-cycles in
aggregate.  They cannot be one \(O(1)\)-component simple trail on almost
every top.

#### Proof

Each changed occurrence belongs to exactly one doublet.  A doublet not
containing a changed occurrence is untouched and retains all three of its
local 2-cycles.  Moreover no newly inserted packet can use either label of
one of these cycles on that top: the untouched doublet already occupies
both signs of both flag resources, and \(\mathcal P'\) is a matching.
Thus the cycle stays an isolated local component.  Since
\(|\mathcal T|=(1-o(1))MN/6\), (3.1) is linear in
\(MN\) whenever \(s=o(MN)\).  A simple directed trail cannot contain both
arcs of a directed 2-cycle without revisiting its first label.  Thus every
intact doublet has to be broken or absorbed by a nonlocal replacement.
\(\square\)

The conclusion applies in particular to any bounded-support 2-factor
merger: a bounded switching touches only boundedly many doublets, so
\(o(MN)\) such packet edits cannot coalesce this matching.  A positive
construction has to avoid the doublets at selection time or perform a
linear-size global redesign.  Pippenger--Spencer gives neither.

## 4. The missing physical resource: oriented core order

Let \(w\) be a rooted cyclic word on \(C\cup\{u,v\}\).  Define its
oriented core signature by deleting the two outside labels while retaining
the cyclic orientation:

\[
                         \rho_C(w)=w\mathbin{|}_C.
\tag{4.1}
\]

Rotation of the displayed word is immaterial; reversal is not.

### Lemma 4.1 (common-core signature of every three-top source)

For every literal matched-cut packet of
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`,
the three source words, and likewise the three target words, have the same
oriented core signature:

\[
 \rho_C(w_{xy})=\rho_C(w_{xa})=\rho_C(w_{ya}).
\tag{4.2}
\]

#### Proof

Deleting the placeholders \(A,B\) from the \(\omega\)-word gives the
cyclic concatenation

\[
 A^+,F_1,\overleftarrow{B^-},B^+,F_2,\overleftarrow{A^-}.
\]

Deleting them from the \(\eta\)-word gives

\[
 B^+,F_2,\overleftarrow{A^-},A^+,F_1,\overleftarrow{B^-},
\]

which is a rotation of the same oriented cyclic order.  Substituting
\((x,y),(x,a),(a,y)\) changes only the deleted placeholders.  The minus
shore only interchanges those placeholders, so its deletion signature is
the same as well. \(\square\)

### Corollary 4.2 (flags and precedence are insufficient)

Suppose two current words on \(C+xy\) and \(C+xa\) have the required
root flags for a common packet but unequal oriented core signatures.  No
choice of the third word, no ordering of packet events, and no acyclic
precedence certificate can make them two source rows of this packet.

Such pairs exist with identical flag data: keep the two active labels in
the required rooted positions and interchange two core labels in only one
word.  Therefore a root-port flag path factor plus a global acyclic
precedence order does not imply a physical \(\omega/\eta\)-context lift.

This is a statewise obstruction, not a counting estimate.  The flag
hypergraph has forgotten the resource \(\rho_C\) which the literal packet
uses exactly.

## 5. What remains possible

The results above do **not** prove that a good flag matching is nonexistent.
They prove the following exact implication boundary.

Proved impossible:

1. choosing an arbitrary near-perfect fixed-six flag matching and repairing
   its component count with \(o(MN)\) bounded packet switchings;
2. deducing the physical lift from local long trails and an acyclic packet
   precedence relation without a common-core context condition.

Still open:

1. selecting from the start an anti-doublet packet family whose local arcs
   are one long path on almost every top;
2. selecting those paths together with a global acyclic precedence order;
3. enforcing (4.2), the fuller \(\omega/\eta\) palette agreement, and exact
   middle-owner disjointness at the same time.

The corrected positive target is consequently a **context-decorated path
matching theorem**, not a 2-factor-merging theorem in
\(\mathcal H_{\rm flag}\).  At minimum its state must include

\[
 (U,\text{tail label},\text{remote head label},\rho_C),
\]

and its packets must be selected chronologically rather than matched first
and ordered afterwards.  The twelve-top histogram-neutral recharge closes
the local position graph, but it does not remove this global context
resource.

## 6. Exact context decoration keeps fixed uniformity, but creates a transversal gate

There is a clean way to put the missing context into the incidence object.
It is useful because it shows both what fixed-uniformity matching can still
prove and why that proof is not yet the desired chronology.

For every top \(U\), let \(\mathscr W_U\) be the set of literal rooted
cyclic words on \(U\) with the retained phase start fixed.  Put

\[
                 \mathscr W=\bigsqcup_U\mathscr W_U
\]

and take signed copies \(\mathscr W^+,\mathscr W^-\).  If \(w\in
\mathscr W_U\), its position-three label is \(x\), a remote position has
label \(y\), and \(a\notin U\), Section 8 of the three-top theorem constructs
two companion source words and three target words.  Make these six signed
word states one edge.  Include all three choices of which top carries the
\(\omega\)-role.  Call the resulting six-uniform multihypergraph
\(\mathcal H_{\rm word}\).

Let \(R=M-O(H)\) be the number of remote positions and \(s=n-M\).  Counting
with role multiplicity gives

\[
                         D_{\rm word}=3Rs=\Theta(m^2).
\tag{6.1}
\]

The harmless factor three can instead be removed by making the role part
of the state.

### Lemma 6.1 (word-state codegrees)

The context-decorated hypergraph has

\[
              \Delta_2(\mathcal H_{\rm word})=O(m),
              \qquad
              {\Delta_2\over D_{\rm word}}=O(m^{-1}).
\tag{6.2}
\]

#### Proof

A source word and its target word on the same top determine the exchanged
remote label, because the two words differ exactly by its transposition
with position three.  The only free packet label is then the catalyst
outside the top, with \(s=O(m)\) choices, and there are at most three role
choices.  Two signed states on distinct tops determine their common
\((M-2)\)-core and their three outside labels whenever they can coexist;
their literal core signatures then either disagree (codegree zero) or
determine the remaining companion word and orientation (bounded
codegree).  Two source states on the same top, or two target states on the
same top, cannot belong to one packet.  These cases exhaust signed pairs.
\(\square\)

Thus fixed-uniformity Pippenger--Spencer applies **after exact context
decoration**.  It gives a matching covering all but \(o(|\mathscr W|)\)
source word states and the same number of target word states.

The inverse-doublet defect can also be removed at this level.  Pair every
literal packet with its inverse and retain one member of each pair by an
independent fair choice.  For a fixed signed word state the incident
choices are independent across inverse pairs, so its retained degree is

\[
                         (1/2+o(1))D_{\rm word}
\]

simultaneously for every state by Chernoff and a union bound: indeed
\(\log|\mathscr W|=O(m\log m)\), whereas \(D_{\rm word}=\Theta(m^2)\).
The retained codegrees do not increase.  A second application of
Pippenger--Spencer therefore gives an inverse-free near-perfect matching
of literal word-state transitions.

### Theorem 6.2 (what context-decorated matching proves)

There is an inverse-free near-perfect matching in a fixed six-uniform,
small-codegree hypergraph in which every selected edge is a genuine
\(\omega/\eta\)-compatible literal exchange.  Hence neither context
decoration nor exclusion of exact reverse doublets destroys the nibble
regime.

It does **not** give the required coefficient-one chronology.  The reason
is an exact scale mismatch.  The matching covers almost every one of the
\(|\mathscr W_U|=(M-1)!\) word states on a top, whereas a physical table
contains exactly one current word on that top.  One still has to choose a
transversal

\[
                         \{w_U\in\mathscr W_U:U\in\tbinom{[n]}M\}
\tag{6.3}
\]

which is closed under the coupled packet transitions.  Neither
Pippenger--Spencer nor an \(o(|\mathscr W|)\)-cycle count in the state
space supplies (6.3).  Even a random-permutation-scale
\(O(\log((M-1)!))\) number of state cycles per top leaves a factorial
number of possible, mutually incompatible orbits.

So the signed context-decorated formulation answers the uniformity
question positively but exposes the true coalescence gate as a
**one-state-per-top invariant transversal**, not a reverse-pair conflict.
This is why forbidding doublets is useful hygiene but cannot by itself
produce the physical word.
