# Exact C6 local delta calculus and the residence-cut gate for the protected `k=17` twin-bank factor

**Date:** 2026-08-01  
**Lane:** A, protected reset/twin-bank factor  
**Status:** exact local theorems and an exact necessary residence lower bound.
No resident upper-complete chronology or compiler is claimed.

## 0. Frozen input and verdict

The factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

is a degree-two factor of the rank-eight/rank-nine incidence graph.  Its
owner-cycle sizes are

\[
 14305,\ 8615,\ 1362,\ 18,\ 4,\ 3,\ 3.                 \tag{0.1}
\]

It contains the `52` protected incidences, equivalently the `26` protected
owner adjacencies, of the fourteen-owner reset packet and the six- and
nine-owner Ferrers banks.  Its immediate upper palette is complete.  Its
positive short-run census is

\[
 r_2=3073,\qquad r_3=2710,                              \tag{0.2}
\]

and its cyclic upper-deck holes at ranks eleven, twelve and thirteen are

\[
 1502,\qquad295,\qquad9.                                \tag{0.3}
\]

The exact old-adjacency hypergraph forced by (0.2) has transversal number

\[
 \boxed{\tau=3807}                                      \tag{0.4}
\]

even after the `26` protected owner adjacencies are forbidden.  Therefore
every resident rethread of this fixed factor changes at least `3807` old
owner adjacencies.  A pure cut-and-rewire Hamilton path consequently needs
at least `3806` new seams.  This is a necessary lower bound, not a
sufficient construction: the new seams may create fresh short runs.

The second result below gives an exact constant-time delta calculus for one
incidence C6.  Component change is read from a three-segment stub matching;
all run-below-four change is read from six capped junction neighbourhoods;
and all rank-eleven through rank-thirteen deck change is read from the
prefix/full/suffix tables of the same three segments.  Three disjoint C6s
give a `7 -> 1` contraction exactly when their component triples form a
loose three-uniform hypertree and every local splice is connected.

## 1. The owner graph of an incidence factor

Let

\[
 \mathcal L={ [17]\choose8},\qquad
 \mathcal O={ [17]\choose9}
\]

and let `F` be a simple degree-two factor of their containment graph.  At
each `l in L`, write its two selected owners as `a_l,b_l`.  Contracting the
length-two incidence path `a_l-l-b_l` gives the labelled Johnson edge

\[
 e_l=a_lb_l,\qquad a_l\cap b_l=l.                       \tag{1.1}
\]

Since every owner also has factor degree two, the graph

\[
 G(F)=\{e_l:l\in\mathcal L\}                            \tag{1.2}
\]

is a two-factor on all rank-nine owners.  Every lower colour occurs exactly
once in (1.2).  Its immediate upper colour is

\[
 u(l)=a_l\cup b_l\in{[17]\choose10}.                    \tag{1.3}
\]

This distinction is important: lower-q1 exactness follows from degrees in
the incidence factor, while upper-q1 completeness is the separate condition
that every rank-ten value has positive multiplicity in (1.3).

## 2. Incidence C6 as an exact three-edge owner switch

Fix a rank-seven set `S` and distinct coordinates `a,b,c` outside `S`.
With indices modulo three, put

\[
 \ell_a=S+a,\quad \ell_b=S+b,\quad \ell_c=S+c,          \tag{2.1}
\]

\[
 q_a=S+a+b,\quad q_b=S+b+c,\quad q_c=S+c+a.             \tag{2.2}
\]

Suppose `F` contains the alternating half

\[
 \ell_aq_a,\quad\ell_bq_b,\quad\ell_cq_c               \tag{2.3}
\]

of the incidence C6.  Let `p_i` denote the other selected owner at
`ell_i`.  Replacing (2.3) by the opposite half is legal precisely when the
three new incidences are absent; in the cyclic convention

\[
 \ell_iq_i\longmapsto\ell_iq_{i-1}.                    \tag{2.4}
\]

In particular `p_i != q_(i-1)`, so no lower vertex acquires the same owner
twice.

### Theorem 2.1 (three-edge switch identity)

Under (2.1)--(2.4), the induced owner two-factor changes by

\[
 e_i=p_iq_i\longmapsto f_i=p_iq_{i-1}
 \qquad(i=a,b,c),                                      \tag{2.5}
\]

and no other owner adjacency changes.

#### Proof

At `ell_i`, the two selected owners are `p_i,q_i` before the C6 and
`p_i,q_(i-1)` afterwards.  This gives (2.5).  Every other lower vertex has
the same two selected incidences, so its contracted owner edge is unchanged.
\(\square\)

Consequences of (2.5) are exact:

* all owner degrees and all lower-q1 colours are unchanged;
* the three old rank-ten colours are `p_i union q_i`;
* the three new rank-ten colours are `p_i union q_(i-1)`; and
* a protected incidence may not occur among the three deleted incidences.

Thus the signed immediate-upper delta is

\[
 \partial_{10}(R)=
 \sum_i\bigl({\bf1}_{p_i\cup q_{i-1}=R}
             -{\bf1}_{p_i\cup q_i=R}\bigr).            \tag{2.6}
\]

It is exactly multiset-neutral iff (2.6) vanishes for every `R`.  The weaker
palette-safe condition relative to old multiplicities `m_10(R)` is

\[
                  m_{10}(R)+\partial_{10}(R)\ge1
                  \quad\text{for every }R.              \tag{2.7}
\]

## 3. Exact component delta from the three path segments

Delete `e_a,e_b,e_c` from `G(F)`.  Among the affected old cycles this
produces exactly three path segments, with six exposed stubs.  Contract each
segment to one vertex.  The old pairing of its stubs and the new edges in
(2.5) become two degree-two multigraphs on these three contracted vertices;
loops and parallel edges are allowed at this contracted level.

### Theorem 3.1 (component formula)

Let `k_old` and `k_new` be the numbers of connected components of the old
and new contracted stub multigraphs.  Then

\[
       c(G(F'))-c(G(F))=k_{\rm new}-k_{\rm old}.         \tag{3.1}
\]

In particular, one C6 merges three current owner cycles into one iff its
three removed edges lie in three distinct current cycles and the new stub
multigraph is connected.

#### Proof

All unaffected owner cycles are identical in `G(F)` and `G(F')`.  Every
affected component is obtained by gluing the same three path segments, once
with the old stub pairing and once with the new pairing.  Contracting a path
does not change the number of connected components, which proves (3.1).
\(\square\)

The connected new case is a triangle on the three contracted segments.
The other possibilities are a loop plus a doubled edge, or three loops.
This completely classifies the local topological effect, including the
cases where two or three removed edges belonged to the same old cycle.

## 4. Exact run-below-four delta from six junction records

Removing the three edges in (2.5) leaves six oriented path ends.  For a
coordinate `x` and an oriented end `v`, record the first four inward owner
bits

\[
 \sigma_x(v)=(x(v_0),x(v_1),x(v_2),x(v_3)),             \tag{4.1}
\]

truncated only if the underlying segment has fewer than four vertices.
The fourth bit is a sentinel: it decides whether a run of length at most
three is internally bounded.  If two of these neighbourhoods overlap on a
short segment, retain the physical vertices once rather than treating the
two records independently.

### Theorem 4.1 (six-neighbourhood locality)

For each `ell in {1,2,3}`, the change in the number of maximal positive
`x`-runs of length `ell` is obtained exactly by replaying the old and new
stub pairings on the union of the six records (4.1), with the sentinel bits
as boundary conditions.  Every positive run outside this union cancels.

#### Proof

The interiors of the three path segments and their orders are unchanged.
Hence a run whose incidence with all six new/old junctions is empty is the
same occurrence before and after the switch.  Conversely, a changed run of
length at most three can penetrate at most three owners inward from a
junction; the next inward bit is enough to decide maximality.  Therefore it
is wholly decided by (4.1).  Taking the physical union handles overlapping
records and constant-coordinate short segments without double counting.
\(\square\)

This theorem is an exact local scoring rule.  Merely adding six pairwise
endpoint scores is not exact when a segment has length below eight or when
a coordinate is constant on a segment; those are the two important edge
cases.

## 5. Exact rank-eleven--thirteen deck delta

For each of the three oriented segments `P`, retain its occurrence-labelled
prefix and suffix tables

\[
 \operatorname{Pref}_P(j)=\bigcup_{t=0}^{j}P_t,
 \qquad
 \operatorname{Suf}_P(i)=\bigcup_{t=i}^{|P|-1}P_t,      \tag{5.1}
\]

and its full union `U(P)`.  Let `Cross_rho(R)` be the number of cyclic owner
interval occurrences of union `R` which cross at least one stub edge when
the segments are glued by pairing `rho`.  Label an occurrence by its
component, start and positive width.  This distinguishes a full-cycle
occurrence from the zero-width interval with the same start/end address.
Along a quotient traversal every
such union has the form

\[
 \operatorname{Suf}_{P_i}(s)
 \cup\bigcup_{i<t<j}U(P_t)
 \cup\operatorname{Pref}_{P_j}(e).                     \tag{5.2}
\]

For a fixed start and increasing endpoint, the enumeration of that branch
may stop as soon as the union rank exceeds thirteen, since later ORs only
grow.  A different start is a different branch and may not be pruned by
this event.

### Theorem 5.1 (crossing-interval delta)

For every target `R` of rank eleven, twelve or thirteen,

\[
 m_{F'}(R)=m_F(R)-\operatorname{Cross}_{\rm old}(R)
                    +\operatorname{Cross}_{\rm new}(R).\tag{5.3}
\]

Thus rank-eleven--thirteen completeness after the C6 is exactly the family
of inequalities `m_(F')(R)>=1` computed from (5.1)--(5.3).

#### Proof

Every cyclic interval is either contained in one open segment or crosses a
stub edge.  The contained occurrences and their values are identical before
and after the switch.  The two crossing occurrence sets are exactly those
enumerated by (5.2), giving (5.3).  Monotonicity of OR proves the stopping
rule.  \(\square\)

Occurrence labels are essential.  Equal union values can have several old
or new witnesses, and on a tiny segment prefix and suffix descriptions may
overlap.  Enumerating each `(component,start,width)` once (or assigning it
to the first changed join after its start) prevents multiple counting when
it crosses two joins.  A set-of-values subtraction is therefore unsound;
(5.3) is a multiset identity followed by the positivity test.

## 6. Three C6s and the loose-hypertree `7 -> 1` criterion

Consider three legal C6 switches whose full six-edge symmetric-difference
supports are pairwise edge-disjoint and which remain alternating in the
chosen application order.  No added incidence may coincide with an edge
toggled by another switch.  Associate to each switch the three
**original** owner components containing its removed adjacencies.  This
gives a three-uniform hypergraph `H` on the seven original components.

### Theorem 6.1 (loose-hypertree contraction)

Assume that each switch has connected new local stub multigraph.  Then the
three switches merge the seven owner cycles into one iff

1. every local switch meets three distinct current components when it is
   applied; equivalently under the compatibility hypothesis above,
2. the component-triple hypergraph `H` is connected and Berge-acyclic.

For three triples on seven vertices this is equivalently that the incidence
bipartite graph of `H` is a tree.  In particular

\[
 |V(H)|=2|E(H)|+1=7.                                   \tag{6.1}
\]

#### Proof

One connected local switch contracts three current components to one and
therefore lowers the component count by two.  The stated edge-disjoint
alternating-support condition leaves every not-yet-used C6 valid.  In a
Berge-acyclic connected
triple system, contracting any hyperedge cannot identify two vertices of a
remaining hyperedge: such an identification would create a Berge cycle.
Hence the three contractions give `7 -> 5 -> 3 -> 1` in a suitable
leaf-removal order.  Conversely, three two-unit component reductions that
connect all seven components have a connected incidence graph with ten
vertices and nine incidence edges.  It is therefore a tree.  \(\square\)

The exact q1 compatibility row for the packet is

\[
 \sum_{\mu=1}^{3}\sum_{i=1}^{3}
 \left({\bf1}_{R=p_{\mu i}\cup q_{\mu,i-1}}
       -{\bf1}_{R=p_{\mu i}\cup q_{\mu i}}\right)=0
 \quad(R\in{[17]\choose10})                            \tag{6.2}
\]

for exact upper-multiset neutrality, or baseline multiplicity plus the
left side at least one for palette safety.  Lower-q1 neutrality is automatic.

Run deltas add only when the six-neighbourhood unions of the three switches
are disjoint.  Rank-eleven--thirteen deltas generally do **not** add after
component fusion: new intervals may cross two or three switches.  They must
be replayed on the final nine-segment quotient using (5.2).  The same final
replay is required for residence when junction neighbourhoods overlap.

## 7. The exact residence cut hypergraph of the frozen factor

On a cyclic owner component, let a positive coordinate run of length
`ell in {2,3}` occupy owner positions `i,...,i+ell-1`.  Its defect arc is
the `ell+1` old cycle adjacencies

\[
 \mathcal H(i,\ell)=
 \{e_{i-1},e_i,\ldots,e_{i+\ell-1}\}.                  \tag{7.1}
\]

### Lemma 7.1 (necessary hit)

Every resident rethread changes at least one adjacency of each set (7.1).

#### Proof

If all adjacencies in (7.1) survive, the same `0 1^ell 0` occurrence is a
contiguous internal subword of the final chronology.  It is therefore still
a forbidden positive run.  \(\square\)

The family (7.1) is a circular-arc hypergraph with edge sizes three and
four.  Protected owner adjacencies are forbidden transversal points.

### Lemma 7.2 (exact circular-arc optimizer)

Fix one arc `A`.  Every transversal chooses some allowed point `p in A`.
Condition on that `p`, remove all arcs containing it, and cut the circle at
`p`.  The remaining arcs are ordinary intervals.  Scanning by increasing
right endpoint and choosing the rightmost allowed point of the first
unhit interval gives an exact conditional optimum.  Taking the minimum over
allowed `p in A` gives the exact circular optimum.

#### Proof

Only the linear assertion needs proof.  Let `I` be the first unhit interval
and let `z` be its rightmost allowed point.  Any feasible solution contains
an allowed `y in I`.  Replacing `y` by `z` cannot uncover a later interval:
such an interval has right endpoint at least that of `I`, and if it contains
`y <= z`, its left endpoint is at most `y`, hence it also contains `z`.
Induction proves greedy optimality.  Conditioning on the selected member of
`A` exhausts all circular transversals.  \(\square\)

Applying Lemma 7.2 gives

\[
\begin{array}{c|r|r|r|r}
\text{component size}&r_2&r_3&|\mathcal H|&\tau\\ \hline
14305&1797&1607&3404&2244\\
8615 &1093& 956&2049&1349\\
1362 & 171& 146& 317& 208\\
18   &   2&   1&   3&   2\\
4    &   4&   0&   4&   2\\
3    &   3&   0&   3&   1\\
3    &   3&   0&   3&   1
\end{array}                                             \tag{7.2}
\]

whose last column sums to (0.4).  All `26` protected owner adjacencies lie
in the largest component; forbidding them does not raise its optimum.

For a final owner path obtained only by deleting old factor adjacencies and
adding new Johnson seams, if `k` old edges are deleted then exactly `k-1`
new seams are added.  Moreover the seam lower colours must inject into the
deleted lower-colour set, leaving exactly one deleted lower colour unused.
Hence (0.4) forces at least `3806` seam edges in that restricted model.
Seven-component fusion alone would require only six; residence, not
topology, is the dominant fixed-factor rethread cost.

## 8. Exact coupled completion rows after a switch packet

For any proposed C6 packet or general rethread, correctness requires one
literal final owner order `T_0,...,T_24309` satisfying all of the following
on that same order.

1. The incidence selection has owner degree two except the two path ends,
   lower degree two except one omitted lower colour, contains all `52`
   protected incidences, and is connected.
2. Every rank-ten upper colour has positive multiplicity.
3. The capped six-neighbourhood/final-junction replay has no positive run
   below four (and the corresponding zero-run row must be added if the
   downstream state requires signed residence).
4. The occurrence-labelled prefix/full/suffix replay covers every rank-
   eleven, rank-twelve and rank-thirteen target.  Hitting only the old hole
   sets (0.3) is insufficient because switches can delete unique old
   witnesses.
5. The one-pivot compiler uses one nonempty word
   `Q_0,...,Q_24312` with

   \[
   Q_i\cup Q_{i+1}\cup Q_{i+2}=T_i\quad(i<7401),        \tag{8.1}
   \]

   \[
   Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}=T_i
          \quad(i\ge7401),                             \tag{8.2}
   \]

   and with the singleton, adjacent-pair and late triple cells forming
   exactly once the complete nonempty lower ideal through rank eight.

Rows 1--5 are coupled.  Separate q1, residence, upper-hole and compiler
optima do not imply a common chronology.

## 9. Audit artifacts and scope

The exact residence calculation is independently reproducible from

```text
scratch/audit_a_k17_twinbank_residence_cut_hypergraph_20260801.py
scratch/audit_a_k17_twinbank_residence_cut_hypergraph_20260801.audit.json
```

It reads and hashes the frozen factor, reconstructs all seven cycles,
verifies the `52` protected incidences, builds every defect arc, branches on
the reference circular arc and verifies the returned transversal.  The
certificate hash recorded in the JSON is

```text
cde33b3f5c12226c6c44b87dfb683583f8be1bcdf4bd8a95c6c43a8f5f386395
```

This note proves neither that a three-C6 hypertree satisfying (6.2) exists
in the frozen factor nor that three C6s can repair the thousands of existing
residence defects.  The three-C6 theorem is a topology and local-delta
criterion.  Equation (0.4) shows that a resident completion of this *fixed*
factor requires a genuinely global rethread unless the factor itself is
first changed on a large support.
