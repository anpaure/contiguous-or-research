# Port-flow switching has exact shadow Lipschitz constants, but the fixed `K15` parent cannot be made resident

Date: 2026-07-31  
Status: proved dimension-uniform switching and conditional probabilistic theorems; proved fixed-parent obstruction; no `K17` word or all-dimension existence theorem

## 1. Scope and authenticated base

The base carrier is

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
```

with SHA-256

```text
39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

It is a Hamilton cycle on all `24310` rank-nine owners of `[17]`, and its
rank-eight adjacent intersections are all distinct.  Thus middle ownership,
connectivity and lower `q1` are fixed throughout this note.  The current
defects are

\[
\begin{array}{c|rrrr}
\text{upper rank}&10&11&12&13\\ \hline
\text{holes}&1891&910&128&3
\end{array}
\]

and lower `q2/q3` holes `1623/1013`.

The purpose of the note is to identify exactly what random integral
port-flow switching can and cannot change.  In particular, none of the
results below rebuilds the owner cycle or lower `q1` palette.

## 2. Upper shadows are induced-component statistics

Let

\[
 C=(V_0,V_1,\ldots,V_{N-1})
\]

be a cyclic Johnson Hamilton cycle on \(\binom{[n]}R\).  For
\(A\subseteq[n]\), put

\[
        \mathcal V_A=\{V\in\tbinom{[n]}R:V\subseteq A\}.
\]

### Lemma 2.1 (exact upper-component criterion)

For \(R<|A|\le n\), the set \(A\) is the union of a contiguous interval of
\(C\) if and only if some connected component of the induced graph
\(C[\mathcal V_A]\) has vertex-union \(A\).

#### Proof

If an interval has union \(A\), all of its vertices lie in
\(\mathcal V_A\).  It is contained in one induced component, and adding the
remaining vertices of that component cannot enlarge the union beyond
\(A\); hence the component union is \(A\).  Conversely, every component of
the induced subgraph is a cyclic interval (or, for \(A=[n]\), the whole
cycle), so a component with union \(A\) is a literal witness. \(\square\)

For a coordinate \(x\), the positive \(x\)-runs are similarly the
components of

\[
 C[\{V:x\in V\}].                                      \tag{2.1}
\]

This removes any dependence on an arbitrarily selected witness bank.

## 3. Exact dimension-uniform seam Lipschitz theorem

Call \(C'\) a **\(c\)-seam rethread** of \(C\) if it is obtained by deleting
a set \(S\) of \(c\) Johnson adjacencies of \(C\), reordering and possibly
reversing the resulting common fragments, and adding \(c\) Johnson
adjacencies to make another Hamilton cycle on the same owners.

Let \(H^+_a(C)\) be the number of missing rank-\(a\) upper interval unions.
Let \(H^-_q(C)\) be the number of missing rank-\((R-q)\) targets among
intersections of \(q+1\) consecutive owners.  Let \(S_d(C)\) be the total,
over all coordinates, of positive runs of length below \(d\).

### Theorem 3.1 (dimension-uniform shadow coefficients)

For every \(c\)-seam rethread,

\[
 \left|H^+_{R+j}(C')-H^+_{R+j}(C)\right|
 \le c\binom{n-R-1}{j-1},
 \qquad 1\le j<n-R,                                   \tag{3.1}
\]

and the two missing sets have symmetric difference at most twice the
right-hand side.  The unique rank-\(n\) target \([n]\) is always witnessed
by the whole cycle, so \(H_n^+(C)=H_n^+(C')=0\).  Consequently

\[
 \sum_{j=1}^{n-R}
 \left|H^+_{R+j}(C')-H^+_{R+j}(C)\right|
 \le \bigl(2^{\,n-R-1}-1\bigr)c.                     \tag{3.2}
\]

For every fixed lower depth,

\[
             |H^-_q(C')-H^-_q(C)|\le qc,              \tag{3.3}
\]

the symmetric difference of the two covered target sets is at most
\(2qc\), and the occurrence-histogram \(L^1\) distance is at most \(2qc\).
Finally,

\[
             |S_d(C')-S_d(C)|\le (R+1)c.              \tag{3.4}
\]

#### Proof

Suppose an upper target \(A\), \(|A|=R+j\), is covered by \(C\) but not by
\(C'\).  By Lemma 2.1, a witnessing component of
\(C[\mathcal V_A]\) must contain a deleted edge; otherwise that entire
component remains a common fragment, possibly reversed.  If the deleted
edge is \(VV'\), then

\[
                    V\cup V'\subseteq A,
 \qquad |V\cup V'|=R+1.
\]

A fixed deleted Johnson edge is therefore chargeable to at most

\[
             \binom{n-R-1}{(R+j)-(R+1)}
             =\binom{n-R-1}{j-1}
\]

targets.  Summing over the deleted edges proves the one-sided loss bound.
Interchanging \(C,C'\) gives gains and (3.1).  The full-set target
contributes zero; summing the remaining binomial coefficients gives (3.2).

A width-\((q+1)\) lower window uses exactly \(q\) cycle seams.  Each deleted
seam lies in exactly \(q\) old windows, so at most \(qc\) old occurrences
are lost; the same bound holds for new occurrences.  This proves (3.3) and
the two stated refinements.

A positive coordinate run is unchanged unless one of its entering,
internal, or leaving edges is deleted.  A Johnson edge \(VV'\) touches one
positive run for each coordinate in \(V\cup V'\), hence exactly \(R+1\)
positive runs.  Thus at most \((R+1)c\) old runs and at most the same number
of new runs fail to belong to the common unchanged family.  The absolute
difference of the short-run counts is at most the larger of these two
numbers, proving (3.4). \(\square\)

For the authenticated `K17` carrier, \((n,R)=(17,9)\).  The upper
coefficients for ranks `10` through `17` are

\[
                    1,7,21,35,35,21,7,0.              \tag{3.5}
\]

Thus ranks `10`--`13` have aggregate coefficient `64`, the complete upper
tower coefficient `127`, lower `q2/q3` coefficients `2/3`, and short runs
coefficient `10`.

## 4. Specialization to the integral macro port flow

Let \(P\) be the fixed linear forest on the rank-eight port set
\(\mathcal T\).  Its degrees determine

\[
                    d_T=2-\deg_P(T).                  \tag{4.1}
\]

An integral port flow is a `0/1` incidence vector \(F\) between pure
rank-nine owners \(U\) and facets \(T\subset U\), satisfying

\[
 \sum_{T\subset U}F_{UT}=2,\qquad
 \sum_{U\supset T}F_{UT}=d_T.                        \tag{4.2}
\]

The two selected facets of each \(U\) are the endpoints of its port edge.

### Lemma 4.1 (flow circuits are seam rethreads)

Let \(F,F'\) satisfy (4.2), and suppose both completed port graphs are
Hamiltonian.  Let

\[
 S(F,F')=\{T:\{U:F_{UT}=1\}\ne\{U:F'_{UT}=1\}\}.
                                                               \tag{4.3}
\]

Then the two expanded owner cycles are a
\(c=|S(F,F')|\)-seam rethread of the same atomic objects.  In particular, a
simple alternating incidence circuit of length \(2s\) changes exactly
\(s\) port seams.

#### Proof

At a port \(T\notin S(F,F')\), the same two atomic edge-objects meet and
their owner adjacency is unchanged.  Cutting precisely the ports in
\(S(F,F')\) leaves the same atomic fragments in both completions.  Each
completion only orders and orients those fragments.  On an alternating
incidence circuit, one selected incidence is replaced at each of its
\(s\) port vertices and nowhere else. \(\square\)

The rank-eight/rank-nine incidence graph has no four-cycle: two distinct
rank-nine sets have at most one common rank-eight facet.  Thus the smallest
primitive flow circuits are Boolean hexagons, and every such toggle has
\(s=c=3\).  This is only a switching basis statement; a hexagon toggle need
not preserve the one-cycle contraction.

The current rank-ten hole count therefore gives an unconditional dense
support requirement inside this fixed macro face:

> Any other Hamiltonian port flow having complete upper `q1` must differ
> from the authenticated flow at at least `1891` port seams.

Similarly, zero lower `q2` would require at least
\(\lceil1623/2\rceil=812\) changed seams, and zero lower `q3` at least
\(\lceil1013/3\rceil=338\).  These are necessary conditions, not existence
claims.

There is also a global topology row.  Every component \(K\) of the linear
forest \(P\) has

\[
 \sum_{T\in K}d_T=2|V(K)|-2|E(K)|=2.                 \tag{4.4}
\]

After contracting the `5005` components of \(P\), every feasible flow is
a degree-two multigraph.  The expanded port factor is Hamiltonian if and
only if this contraction is one cycle.  Integrality of (4.2) alone does not
give this global condition.

## 5. The exact upper-`q1` state system

The fixed macros separate the upper `q1` problem into three tags.  At a
port with \(d_T=1\), the unique macro endpoint has tag `X` or `Y`; write the
corresponding port classes as \(\mathcal P_X,\mathcal P_Y\).  At a port
with \(d_T=2\), two pure \(U\)-objects meet and their union is an untagged
rank-ten target.  In the authenticated macro family every \(d_T=0\) port
joins opposite tags and hence has tag `XY`; that palette is already complete
internally.  Thus no fixed \(d_T=0\) seam supplies an additional one-tag
exception to the formulation below.

Let \(\mathcal M_X\) and \(\mathcal M_Y\) be the pure rank-nine masks whose
`X`- and `Y`-tagged rank-ten targets have no fixed internal macro witness.
The authenticated counts are

\[
 |\mathcal M_X|=900,\qquad |\mathcal M_Y|=882,
 \qquad |\mathcal P_X|=|\mathcal P_Y|=984.            \tag{5.1}
\]

### Theorem 5.1 (tagged palettes are an integral lower-bounded flow)

There is a port flow satisfying both tagged palettes if and only if the
following capacitated network has flow value \(2|\mathcal U|\).

For every \(U\), create one required `X` slot when
\(U\in\mathcal M_X\), one required `Y` slot when
\(U\in\mathcal M_Y\), and

\[
             2-1_{U\in\mathcal M_X}-1_{U\in\mathcal M_Y}
\]

free slots.  Every slot has source capacity one.  A required `X` slot may
use only incidences \((U,T)\) with \(T\in\mathcal P_X\); similarly for
`Y`; a free slot may use every available incidence.  Route all slot arcs
through a capacity-one incidence node \((U,T)\), then through a port node
of sink capacity \(d_T\).

#### Proof

A saturating integral network flow selects two distinct incidences for
each \(U\), saturates every port demand, and sends each required slot to a
port producing its tagged colour.  Hence it gives (4.2) and both tagged
palettes.  Conversely, from any port flow satisfying the palettes, assign
one suitable selected incidence to each required slot and the remaining
incidences to the free slots.  The capacity-one incidence nodes enforce
the `0/1` constraint.  Network-flow integrality completes the equivalence.
\(\square\)

The untagged palette is the first non-network correlation.  An exact state
formulation is as follows.  A \(d_T=1\) port chooses one incident \(U\).  A
\(d_T=2\) port chooses an unordered pair of distinct incident owners
\(\{U,V\}\).  Choose exactly one state per port, give every \(U\) total load
two, impose the tagged rows above, and, for every pure rank-ten target
\(A\), impose

\[
 \sum_{\substack{T\subset A,\ |T|=8,\ d_T=2}}
 y_{T,\{A\setminus\{a\},A\setminus\{b\}\}}\ge1,
 \quad \{a,b\}=A\setminus T.                         \tag{5.2}
\]

There are `4021` pair ports for `3003` targets.  Formula (5.2), the tagged
rows, the owner loads, and the one-cycle contraction row are necessary and
sufficient for a connected lower-`q1`-exact, upper-`q1`-complete carrier on
the fixed macros.  The scalar opportunity counts alone do not imply this
integer state system.

## 6. Conditional probability theorem

The following is the exact local-lemma target; it is not asserted to exist
for the authenticated parent.

Equip \(\Omega=\{0,1\}^s\) with independent fair product measure, and let
its coordinates be legal switching packets such that every state is a
connected, degree-two, lower-`q1`-exact physical carrier.
Suppose flipping coordinate \(i\) is a \(c_i\)-seam rethread.  For any of
the statistics in Theorem 3.1, McDiarmid's inequality gives

\[
 \Pr(|Z-\mathbb EZ|\ge t)
 \le 2\exp\!\left(-\frac{2t^2}{\sum_i L_i^2}\right), \tag{6.1}
\]

with

\[
 L_i=\binom{n-R-1}{j-1}c_i,\quad qc_i,\quad
 \bigl(2^{n-R-1}-1\bigr)c_i,\quad\text{or}\quad(R+1)c_i
                                                               \tag{6.2}
\]

for one upper rank, lower depth \(q\), the whole upper tower, or short
runs, respectively.  This controls fluctuation, not the mean, and therefore
does not by itself prove zero defects.

For an exact-zero theorem, index every required palette, deeper witness, and
possible short-run condition by \(a\), and let \(B_a\) be its failure event.
(If connectivity is supplied only after the random choice, the topology
absorber must instead be included as another correlated failure family.)
Suppose

* \(B_a\) is contained in a cylinder event \(C_a\) depending on coordinates
  \(J_a\);
* \(\Pr(C_a)\le p_a\); and
* numbers \(x_a\in(0,1)\) satisfy

\[
 p_a\le x_a
 \prod_{\substack{b\ne a\\J_a\cap J_b\ne\varnothing}}(1-x_b). \tag{6.3}
\]

Then the asymmetric Lovász local lemma supplies one state avoiding every
failure.

A useful checkable sufficient condition is a private-polarity bank.  If
requirement \(a\) has \(h_a\) distinct switch coordinates such that the
good polarity of any one of them guarantees the requirement independently
of all other switches, then

\[
                         p_a\le2^{-h_a}.              \tag{6.4}
\]

If \(|J_a|\le s_0\), every coordinate belongs to at most \(\Delta\)
cylinders, \(h_a\ge h\), and each \(C_a\) is a union of at most \(r_0\)
such private subcylinders, the symmetric sufficient inequality is

\[
 e\,r_0\,2^{-h}\bigl(s_0(\Delta-1)+1\bigr)\le1.     \tag{6.5}
\]

Without exact zero, averaging gives the weaker statement

\[
 \mathbb E\sum_a w_a\mathbf 1_{B_a}\le\sum_a w_ap_a. \tag{6.6}
\]

Thus an `o(1)` normalized right-hand side proves an `o(1)` normalized
defect state; for the unweighted integer defect count, a total right-hand
side below one proves a zero-defect state.

Every qualifier in this theorem is needed.  Uniform integral flows are not
a product measure; an alternating circuit may split the port cycle; and a
concentration inequality around a positive mean does not imply a zero.

## 7. The fixed-parent residence branch is impossible

The dimension-uniform reason is the odd-diamond residence tax.  If a parent
rank-\(r\) chronology is \(T_i\), a coordinate is nonconstant on its cyclic
component, and its diamond trace is

\[
                         C_i=T_i\cap T_{i+1},          \tag{7.1}
\]

then every old-coordinate parent run of length \(\ell\ge2\) induces a trace
run of length exactly \(\ell-1\); a singleton run disappears rather than
becoming a positive run of length zero.  A coordinate present on an entire
component has no boundary and is a separate constant case.  Hence, in the
regenerative regime where the parent minimum is at least \(d+1\ge2\), a
flat child compiler requiring
internal runs of length at least \(d+1\) needs one of two upstream states:

1. **margin:** every parent run has length at least \(d+2\); or
2. **compensation:** an exported cut, facet, or nonflat actuator hits every
   parent run of length \(d+1\).

Ordinary parent residence \(d+1\) is not regenerative on the nonconstant
coordinates.  This is the form of the dimension-uniform theorem used from
`MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md`.

The authenticated fixed-macro audit proves that `605` length-three runs
are wholly internal to the current `1430` macros.  More strongly, after
allowing an arbitrary occurrence transversal for every repeated rank-six
trace colour, the fixed parent still has `165` forced internal patterns

\[
                         0\,111\,0.                   \tag{7.2}
\]

For each such pattern, all four supporting rank-six colours have unique
physical occurrences, so all four edges are forced in every transversal.
There are exactly eleven forced patterns for each old coordinate.  The
exact residence CNF consequently contains `165` empty clauses.

The complete coupled optimum is stronger:

\[
 \min_{\text{rank-six occurrence transversals}}
 \{\text{internal `A`-shore short runs}\}=180.        \tag{7.3}
\]

An attaining transversal has exactly twelve debts on each of the fifteen
old coordinates, and its induced graph independently reconstructs all
`1430` macros.  The lower bound is the bound-`179` CNF: it asks whether at
most fourteen non-forced patterns can survive in addition to the `165`
empty-clause patterns.  Its retained DRAT proof is independently verified,
with a `5531`-clause core and `99145` resolution steps.  Each coordinate
separately has minimum eleven, but those fifteen coordinatewise minima
cannot be realized by one common occurrence transversal.  Thus the extra
fifteen units in (7.3) are a genuine cross-coordinate integral-correlation
debt, not fifteen additional individually fixed bad events.

The frozen bound-`179` CNF and DRAT hashes are respectively
`4cbf25a3f4d322c54ce91b068dc08e49223e86019d3dfccc51f065a3860cf19c`
and
`8d55ea0215b62b43aaba7a94eda194555227ffdb0a73eb174d227afa0695c018`;
the independent `s VERIFIED` transcript has SHA
`78bd2f06aa9938999374176d676dec9337fcb61a231a3f7287bfb6468f25d465`.

### The occurrence choice also carries inherited upper debt

For a physical parent edge \(i\), write

\[
 Z_i=(T_i\cap T_{i+1})\cap(T_{i+1}\cap T_{i+2}),
 \qquad U_i=T_i\cup T_{i+1}.                          \tag{7.4}
\]

Call \(i\) upper-unique when no other parent edge has union \(U_i\), and
let \(u_Z\) count upper-unique occurrences in the fibre with colour \(Z\).
Every one-occurrence-per-\(Z\) transversal deletes at least

\[
                         \sum_Z(u_Z-1)^+              \tag{7.5}
\]

upper-unique providers, and this bound is exact: in each fibre with
\(u_Z>0\), retain one upper-unique occurrence; otherwise retain any
occurrence.  This is an exact inherited-*internal*-witness debt.  A later
port seam may recreate the target, so (7.5) is not itself a final upper-hole
lower bound.

For the authenticated parent,

\[
 u_Z:\quad0^{1835}1^{2685}2^{465}3^{20},
 \qquad\sum_Z(u_Z-1)^+=505.                           \tag{7.6}
\]

The octahedral `r2` parent has profile
\(0^{1735}1^{2865}2^{405}\), hence marginal unique-provider debt `405`,
and marginal exact residence debt `150` rather than `180`.  These two
improvements do not assert that their separate marginal optima occur at one
common transversal.

Residence avoidance clauses and upper-provider rewards use the same
occurrence variables.  Therefore the regenerative random state must select
one joint occurrence transversal carrying minimum-run compensation,
upper-unique preservation, and the induced macro port demands *before* the
central \(b\)-flow is chosen.  Separate residence and upper-service LLL
rounds discard precisely this correlation.

Therefore no probability distribution on port flows, macro orientations,
macro permutations, or rank-six occurrence transversals of this fixed
parent can satisfy flat depth-three residence.  The `165` unique-colour bad
events have probability one, and every distribution on occurrence
transversals has internal short-run count at least `180` almost surely.
In particular, applying (6.3) only to flow or occurrence variables is
vacuous.

If a genuinely different macro forest \(P'\) is supplied by a changed
parent chronology, its flow correction from \((P,F)\) must satisfy the exact
transshipment equations

\[
 \sum_{T\subset U}z_{UT}=0\quad(\forall U),\qquad
 \sum_{U\supset T}z_{UT}
 =-\bigl(\deg_{P'}(T)-\deg_P(T)\bigr)\quad(\forall T), \tag{7.7}
\]

with \(F+z\in\{0,1\}\).  These equations are necessary and sufficient for
the degree-two rows.  When \(P'=P\), \(z\) is a circulation and decomposes
into alternating circuits.  When the forest degrees change, alternating
paths carrying the prescribed divergence are unavoidable.

## 8. Exact remaining theorem boundary

The flow-only simultaneous theorem requested at the start is **false for
the authenticated fixed parent**, because of Section 7.  The strongest
surviving construction target is one of the following.

1. Change the parent chronology and construct a Hamilton-stable packet cube
   that exports either residence margin or an explicit compensation set,
   satisfies (7.7), the exact state rows (5.2), and the private-cylinder
   inequality (6.3) for every deeper upper/lower witness and every possible
   short run.
2. Keep the fixed parent but replace the flat depth-three compiler by a
   genuinely nonflat compiler that accepts the forced patterns (7.2), while
   independently solving (5.2), deeper shadows, and the common compiler.

In the first route the missing probabilistic lemma is not merely
"quasirandom b-flow": it is a **parent-chronology packet theorem** giving
simultaneously

* exact owner degree and lower `q1`;
* one common occurrence transversal coupling residence hyperclauses,
  upper-provider rewards, and macro port demands;
* one-cycle contraction;
* robust private upper/lower witnesses with (6.3); and
* parent residence margin \(d+2\), or a compensation cylinder hitting every
  minimum parent run.

The compensation object must be common across coordinates.  The exact
`180>15\cdot11` optimum proves that fifteen separately optimal coordinate
hitting choices need not synchronize to one occurrence transversal.

Theorem 3.1 supplies the needed dimension-uniform influence constants, but
no current construction supplies this correlated packet bank.  Hence this
note proves neither a `K17` word nor an all-\(k\) equality theorem.

## 9. Lineage

The base owner theorem and the fixed-parent obstruction are:

```text
MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md
MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md
MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md
MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md
scratch/k17_parent_induced_macro_port_cycle_20260731.audit.json
scratch/k17_fixed_macro_residence_obstruction_20260731.audit.json
scratch/k17_macro_residence_20260731.cnf
scratch/k17_macro_residence_optimal_20260731.json
scratch/k17_macro_residence_optimal_20260731.verify.json
scratch/k17_macro_residence_bound179_20260731.cnf
scratch/k17_macro_residence_bound179_20260731.drat
scratch/k17_macro_residence_bound179_20260731.dratcheck.txt
```

The Lipschitz, network-flow, private-cylinder, and transshipment theorems in
this note are mathematical deductions from those authenticated interfaces;
they do not rely on a new finite search.  The exact value `180` is imported
from the independently replayed witness and checked bound-`179` proof listed
above.
