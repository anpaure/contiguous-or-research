# Two-shore receiver safety is a linear matroid-parity problem

**Date:** 2026-08-05  
**Method:** endpoint transversals, generic linear representations, and
Lovasz's matroid-parity matrix; no computation  
**Status:** unconditional exact formulation for selecting an initially
packable receiver-square subbank.  It also records a literal fixed-fan
obstruction.  Ordinary sector matching extension and the choice of a
perfect passive pairing at every unfixed hub are separate constraints.

## 1. One endpoint shore is a bicircular matroid

Let `E` be a catalogue of literal or quotient receiver-square jobs.  For
each `e in E`, let

\[
 A_e\subseteq V_A,\qquad B_e\subseteq V_B,
 \qquad |A_e|,|B_e|\le2                              \tag{1.1}
\]

be its two diagonal endpoint lists after fixed vertex deletions and orbit
coalescence.  Occurrence labels distinguish parallel jobs.

On the ground set `E`, define `M_A` by declaring `F subseteq E`
independent when the lists `(A_e:e in F)` have an SDR.  Define `M_B`
symmetrically.

### Lemma 1.1

`M_A` and `M_B` are transversal matroids.  In the two-element-list
picture, their independent sets are exactly the edge sets whose endpoint
multigraph is a pseudoforest.

#### Proof

The first statement is the definition of a transversal matroid.  For
lists of size at most two, orient a job edge toward its selected endpoint.
Distinct representatives are exactly an orientation with pairwise
distinct heads.  A connected multigraph admits such an orientation for
all its edges exactly when it has at most as many edges as vertices,
equivalently when it contains at most one cycle.  Apply this component by
component. \(\square\)

Thus a bank is initially endpoint-packable on both shores precisely when

\[
                              F\in M_A\cap M_B.        \tag{1.2}
\]

## 2. Exact common-selection formulation by matroid intersection

The simplest formulation stays on the original job ground set.

### Theorem 2.1 (common bicircular min--max)

Let `nu` be the maximum number of candidate jobs whose two endpoint graphs
are both pseudoforests.  Then

\[
 \boxed{
 \nu=\min_{X\subseteq E}
          \bigl(r_A(X)+r_B(E\setminus X)\bigr),}       \tag{2.1}
\]

where `r_A,r_B` are the two bicircular/transversal matroid rank functions.
For `sigma in {A,B}` these ranks have the explicit component formula

\[
 r_\sigma(F)
   =\sum_{C\in\operatorname{Comp}(Q_\sigma[F])}
        \min\{|E(C)|,|V(C)|\}
   =|F|-\sum_C(|E(C)|-|V(C)|)_+.                      \tag{2.2}
\]

#### Proof

By Lemma 1.1 the feasible job sets are exactly the common independent sets
of `M_A` and `M_B`.  Edmonds' matroid-intersection min--max theorem gives
(2.1).  The maximum independent subset inside one connected endpoint
component has size `min(e,v)`, by orienting a tree away from a root or one
cycle cyclically.  Summing components gives (2.2). \(\square\)

Thus endpoint safety fails for a required cardinality `q` if and only if
some partition `X,E setminus X` satisfies

\[
                         r_A(X)+r_B(E\setminus X)<q.   \tag{2.3}
\]

This is the exact combinatorial selector certificate requested by the
receiver problem.  Equivalently, if `delta_A(F)=|F|-r_A(F)` and similarly
for `B`, then

\[
 \boxed{
 |E|-\nu=
   \max_{X\subseteq E}
      \bigl(\delta_A(X)+\delta_B(E\setminus X)\bigr).} \tag{2.3a}
\]

So every unavoidable lost job is certified by a partition of the
catalogue into an `A`-bicycle side and a `B`-bicycle side.

### 2.1 Equivalent linear matroid-parity lift

Make two copies `e_A,e_B` of every candidate job `e`.  On the doubled
ground set put the direct-sum matroid

\[
                              M=M_A\oplus M_B.         \tag{2.4}
\]

Partition its ground elements into the pairs

\[
                              P_e=\{e_A,e_B\}.         \tag{2.5}
\]

### Theorem 2.2 (two-shore bicircular parity)

The maximum number of candidate jobs whose two endpoint graphs are both
pseudoforests is exactly the maximum number of pairs `P_e` whose union is
independent in `M`.

In other words, initial two-shore receiver selection is an ordinary
matroid-parity problem in the direct sum of two transversal matroids.

#### Proof

For `F subseteq E`, the union of its pairs is

\[
 \{e_A:e\in F\}\mathbin{\dot\cup}\{e_B:e\in F\}.
\]

It is independent in the direct sum (2.4) if and only if its first part
is independent in `M_A` and its second part is independent in `M_B`.
By Lemma 1.1 this is exactly simultaneous endpoint packability. \(\square\)

This is an exact, not asymptotic, criterion.  It is also linear over a
sufficiently large rational-function field.

For `sigma in {A,B}`, form a matrix `R_sigma` whose rows are the endpoint
vertices in `V_sigma` and whose column `e_sigma` has an independent
indeterminate in every row belonging to the list `sigma_e`, and zero
elsewhere.  Algebraic independence prevents cancellation, so a set of
columns is independent exactly when its lists have an SDR.  Therefore

\[
                         R=R_A\oplus R_B              \tag{2.6}
\]

represents `M`.

Let `Z(y)` be the skew-symmetric matrix on the doubled columns with the
only nonzero entries

\[
 Z_{e_A,e_B}=y_e,\qquad Z_{e_B,e_A}=-y_e.             \tag{2.7}
\]

The linear matroid-parity rank theorem gives

\[
 \boxed{
 2\nu=\operatorname{rank}_{\mathbb F(x,y)}
                   \bigl(RZ(y)R^{\mathsf T}\bigr),}  \tag{2.8}
\]

where `nu` is the maximum cardinality in Theorem 2.1.  Hence failure to
obtain `q` endpoint-safe jobs has an exact algebraic rank certificate
`rank(RZR^T)<2q`.

Equation (2.8) is useful because all quotient loops, parallel jobs, and
structural zeros are represented literally.  It does not replace them by
an anonymous degree count.

## 3. What this theorem does and does not select

If a prospective construction merely needs any `q` jobs from a catalogue,
Theorem 2.1 is the complete initial endpoint-packing theorem.

The physical hub problem is stronger.  At one hub, candidate jobs are
unordered pairs of passive petals, and all passive petals must be used
once.  Thus the selected catalogue edges must simultaneously form a
perfect matching in each hub's petal clique.  Matchings in a graph are not
the independent sets of a matroid.  Consequently the complete choice is

\[
 \boxed{
 \text{hubwise perfect matching}
 \quad+\quad
 \text{linear two-shore matroid parity}.}             \tag{3.1}
\]

Ordinary two-matroid intersection does not express (3.1).  One may make
it a finite exact parity/matching problem, but no Hall-only min--max follows
from Theorem 2.1.

There is a useful stronger but simpler sufficient target.

### Corollary 3.1 (endpoint load two)

If, on both shores, every endpoint vertex has multigraph degree at most
two (a loop counts twice), then the entire selected job bank is initially
endpoint-packable.

#### Proof

Every connected multigraph of maximum degree at most two is a path or a
cycle, with a loop allowed as a one-vertex cycle.  Hence every component
has at most one cycle, so both endpoint graphs are pseudoforests. \(\square\)

Thus one concrete prospective construction is a hubwise perfect petal
pairing with receiver endpoint capacity two on each diagonal shore.  This
condition is stronger than the exact min--max (2.1), but it replaces all
bicycle cuts by one local load ledger.  In a quotient, loops must be priced
with degree two; merely bounding the number of job labels at a vertex by
two is not sufficient when loops occur.

There is a second independent constraint.  Endpoint SDRs choose one
endpoint on each shore, but the resulting pairwise-disjoint receiver
edges must extend through the remaining ordinary capacity-two sector.
Relative to a fixed ordinary matching this is the vertex-disjoint
alternating-path condition; without a fixed matching it is exactly the
perfect-matching condition in the augmented receiver graph.  Feasible
terminal-deletion sets form an even delta-matroid in general, not the
transversal matroid `M_A` or `M_B`.  Thus (2.1), equivalently (2.8),
certifies the empty-shore
rows only.  The proper Hall/Tutte rows still have to be imposed on the
same selection.

## 4. A fixed-fan obstruction is already literal

The construction in

`MATH_COUNTEREXAMPLE_INVISIBLE_BICYCLE_ESCAPE_AND_PSEUDOFOREST_TREE_DISCOUNT_20260805.md`

uses eight free hubs.  Give each hub one fixed active anchor petal and two
passive petals.  The latter form the unique passive pair at that fixed
fan state.  Their eight receiver squares have:

* pairwise distinct parent-petal endpoints;
* trivial rotational stabilizer;
* an `A`-diagonal graph which is a matching; and
* a `B`-diagonal graph consisting of two four-cycles meeting at one
  vertex.

The `B` graph has eight edges and seven vertices, so it is dependent in
`M_B`.  Each fixed fan offers only its displayed passive pair, and changing
the two exposed-petal orientations does not change the two diagonal lists
of the square.  Therefore its candidate catalogue has

\[
                  \nu\le7<8.                          \tag{4.1}
\]

### Corollary 4.1 (no post-hoc universal pairing theorem)

After the parent matching and active anchors are fixed, it is false that
the remaining passive petals can always be oriented or paired into
two-shore pseudoforests.  The obstruction occurs with no quotient folding
and with all parent endpoints distinct.

This does not rule out choosing a different parent matching or a different
active anchor before the fan state is frozen.  It proves that such a choice
must be correlated with the receiver endpoint matroids; endpoint safety
cannot be postponed until after an arbitrary ordinary factor is selected.

## 5. A proof-safe constructive target

A positive all-level theorem may use Theorem 2.1 in either of two ways.

1. **Catalogue surplus.**  Construct a prospective catalogue for which
   (2.8) has rank at least twice the number of required passive pairs, and
   then prove that a maximum parity set contains a hubwise perfect petal
   pairing.
2. **Joint parent selection.**  Include the parent matching and active
   anchors in the selector from the start, and require every chosen parent
   state to export job pairs whose doubled columns are independent in
   (2.6).

After either step, apply the pseudoforest tree-discount reduction to the
proper Hall cuts and then the augmented ordinary matching theorem.  The
labelled one-unit strict Hall result is useful only at that later stage;
it cannot establish the rank condition (2.1) at the empty shore.

## 6. Quotient and odd-level boundaries

The matrices `R_A,R_B` are built after orbit coalescence, so Theorem 2.1
is valid verbatim in a quotient sector.  There is also a positive descent
statement for a genuinely invariant occurrence bank.

### Theorem 6.1 (odd orbit quotients preserve pseudoforests)

Let an odd rotational group `H` act on an occurrence-labelled endpoint
multigraph `Q`, and suppose the selected job set is `H`-invariant.  If `Q`
is a pseudoforest, then the orbit multigraph `Q/H`, with loops and parallel
job orbits retained, is a pseudoforest.  Semiregularity is not required.

#### Proof

The group permutes connected components.  A component of the orbit graph
is therefore the quotient `C/K` of one connected component `C` by its
setwise stabilizer `K`.

If `C` is a tree, the finite group `K` fixes a vertex or an edge.  An odd
group cannot invert an edge, so after subdividing a pointwise fixed edge
if necessary there is a fixed root.  Root `C` there.  Every nonroot vertex
has a unique parent, and the parent operation is equivariant.  Hence every
nonroot vertex orbit in `C/K` has a unique parent orbit.  The quotient is
a tree.

If `C` is unicyclic, its unique cycle is `K`-invariant.  An odd group acts
on that cycle by rotations, so its quotient is again a cycle (a loop is
allowed).  Every component off the cycle is a rooted tree, and the preceding
argument shows that its quotient is a rooted tree attached to the quotient
cycle.  Thus `C/K` is unicyclic.  This proves the claim componentwise.
\(\square\)

Consequently periodic folding cannot create the first bicycle from an
already invariant, endpoint-packable occurrence bank.  What does not
automatically descend is a non-invariant labelled selection: selecting one
representative rather than full job orbits is not a quotient construction.
Nor does this theorem descend the quantitative **ordinary strict-Hall
slack**, because periodic vertex orbits may have unequal sizes.  That is a
separate proper-cut issue.

At an odd cut level, two-shore endpoint packing is still described by
Theorem 2.1, but extension through the ordinary sector is a blossom/Tutte
problem rather than a bipartite Hall problem.  No even-level network or
strict-Hall conclusion is asserted there.
