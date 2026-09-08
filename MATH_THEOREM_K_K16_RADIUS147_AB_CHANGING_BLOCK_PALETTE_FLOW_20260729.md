# The radius-147 AB-changing face at `k=16`

## Exact block calculus, palette flow, and the surviving boundary-migration gate

Date: 2026-07-29  
Lane: K  
Status: **proved structural reduction and new finite obstructions; radius 147 remains open**

## 0. Verdict

Let `F_0` be the certified `k=16` equivariant quotient Hamilton factor

```
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
```

of SHA-256

```
f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5.
```

It has 858 selected quotient edges, sector counts

\[
 (AA,AB,BB)=(389,80,389),
\]

both q1 decks complete, one quotient cycle of voltage 11, one physical
Hamilton cycle, and top-one/top-zero run length at least four.  Its 3,390
old-coordinate residence defects are represented by 226 certified cyclic
edge-interval motifs.  Their transversal and packing numbers are both 147.

This note proves the following facts about every loopless quotient repair at
that minimum deletion radius.

1. The radius-147 deletion face is the Cartesian product of 112 tiny local
   transversal sets.  Its exact sector support is

   \[
   0\le d_{AB}\le27,
   \qquad
   60\le d_{BB}\le\min(70,87-d_{AB}),
   \qquad
   d_{AA}=147-d_{AB}-d_{BB}.
   \tag{0.1}
   \]

   Only 389 source edges can occur in any minimum transversal:

   \[
   209\ AA,qquad27\ AB,qquad153\ BB.
   \tag{0.2}
   \]

   The other 469 source edges are forced retained.

2. If `t` is half the net change in the number of AB edges, then the final
   sector counts, the A/B block counts, and the four q1 occurrence totals are
   forced.  A solver-free unique-hard-row census sharpens the scalar window
   to

   \[
   \boxed{-13\le t\le38},
   \qquad
   \boxed{54\le |F'_{AB}|\le156},
   \qquad
   \boxed{27\le b_A=b_B\le78}.
   \tag{0.3}
   \]

3. For a fixed cut, the exact q1/degree repair decomposes in three stages:

   * select new AB boundary incidences and a labelled AB matching by an
     ordinary capacitated Hall flow;
   * solve an independent coloured residual `f`-factor on shore A;
   * solve an independent coloured residual `f`-factor on shore B.

   Palette-bank selection followed by Tutte is necessary and sufficient for
   each shore.  On a genuinely bipartite shore scaffold, the forced-bank
   Hall inequalities give the corresponding exact integral flow theorem.

4. AB pairing is q1-endpoint-local.  It can change chronology, connectivity,
   and voltage, but its lower-no-top and upper-with-top q1 colours depend
   only on the two boundary endpoint sets.

5. The 36 old AB edges contained in the fixed packing union induce, in the
   full voltage-labelled AB catalogue, only 19 off-source alternatives.
   After contracting the old matching, those alternatives form a DAG.
   Therefore a radius-147 AB change cannot merely re-pair the same deleted
   boundary endpoints.  It must migrate, create, or remove at least one
   boundary endpoint.

6. The canonical `87 AA + 60 BB` transversal cannot be repaired even by a
   variable AB bank.  It has three hard lower-with-top rows with no
   endpoint-accessible BB provider, and AB additions can neither supply
   those rows nor increase same-shore residual degree.

These facts do **not** refute radius 147.  In particular, fixed-cross UNSAT
excludes only the point with no old AB deletion and no new AB insertion.  It
does not exclude the pure-insertion branch

\[
 d_{AB}=0,qquad a_{AB}=2,qquad t=1.
\tag{0.4}
\]

The exact remaining gate is a jointly chosen noncanonical local transversal,
boundary-migrating AB matching, and pair of coloured shore factors, followed
by new-motif, connectivity/voltage, deeper-shadow, and compiler audits.

## 1. Setup and four q1 sectors

Write the 16th coordinate as `z`; the other 15 coordinates carry the free
cyclic action.  The quotient middle vertices split into equal shores

\[
 V_A=\{P\subset[15]:|P|=8\}/C_{15},
\]

\[
 V_B=\{\{z\}\cup Q:Q\subset[15],\ |Q|=7\}/C_{15},
\]

with 429 vertices on each shore.  A selected edge is of type `AA`, `AB`, or
`BB` according to its endpoint shores.

Separate the q1 colours into

\[
 L_0=\text{lower, no }z,
 \quad L_1=\text{lower, with }z,
 \quad U_0=\text{upper, no }z,
 \quad U_1=\text{upper, with }z.
\]

Their target-orbit counts are

\[
 (|L_0|,|L_1|,|U_0|,|U_1|)=(429,335,335,429).
\tag{1.1}
\]

One Johnson edge supplies the following sectors:

\[
\begin{array}{c|cc}
\text{edge type}&\text{lower sector}&\text{upper sector}\\ \hline
AA&L_0&U_0\\
AB&L_0&U_1\\
BB&L_1&U_1.
\end{array}
\tag{1.2}
\]

Thus `U_0` and `L_1` are the two **hard** sectors: AB edges cannot supply
them.  The sectors `L_0,U_1` are **easy** only in the limited sense that
either a same-shore edge or an AB edge can supply them.

Throughout this note, `D=F_0\setminus F'` and `J=F'\setminus F_0`; hence a
radius-147 repair has

\[
 |D|=|J|=147.
\]

The finite catalogue statements below use the loopless quotient-seam model.
Quotient loops require their usual degree-two convention and are outside the
certified face considered here.

## 2. The exact minimum-transversal product

Let `M_1,...,M_226` be the certified old residence motifs.  The fixed
certificate contains 147 pairwise edge-disjoint motifs whose union `U` has
476 edges.  If a deletion set `D` hits every motif and `|D|=147`, then it
must choose exactly one edge from each packed motif and no edge outside `U`.
This is immediate from disjointness and equality in the packing bound.

Form the intersection graph of all 226 motifs, joining motifs that share an
edge.  It has 112 components.  Every remaining motif constraint lies wholly
inside one component, so the minimum transversals are exactly the Cartesian
product of the local minimum transversals.  The largest component contains
14 source edges, seven motifs, and four packed motifs.  Directly enumerating
these local tables, and only these tables, gives the following theorem.

### Theorem 2.1 (exact radius-147 sector atlas)

Every radius-147 old-motif transversal has a sector triple satisfying
(0.1), every integer triple in (0.1) occurs, and the union of all edges that
occur in at least one such transversal is exactly the 389-edge atlas (0.2).

#### Proof

For each of the 112 intersection components, choose one edge from each
packed motif in the component, reject the choice unless it hits every motif
in that component, and record its `(AA,AB,BB)` count.  Convolution of the 112
finite supports gives exactly 253 global triples.  Their closed form is
(0.1).  Taking the union of locally valid choices gives (0.2).  The audit
asserts both identities rather than inferring them from a sample.  Its
largest raw local choice table has only four packed rows and 14 edges.  QED.

The fixed packing union itself has sector histogram

\[
 (233,36,207),
\tag{2.1}
\]

whereas imposing all 226 motifs reduces the AB-eligible bank from 36 to 27.
The 389 eligible edges touch 506 quotient vertices,

\[
 277\text{ on A},\qquad229\text{ on B}.
\tag{2.2}
\]

There are exactly 9,207 off-source loopless catalogue edges whose endpoints
both lie in this maximal deficit-vertex atlas:

\[
 4819\ AA,qquad1159\ AB,qquad3229\ BB.
\tag{2.3}
\]

These are candidate incidences, not a feasible repair.

## 3. Exact AB cut/add and block-run calculus

Write

\[
 d_A=|D_{AA}|,
 \quad d=|D_{AB}|,
 \quad d_B=|D_{BB}|,
\]

and

\[
 a_A=|J_{AA}|,
 \quad c=|J_{AB}|,
 \quad a_B=|J_{BB}|.
\]

### Lemma 3.1 (shore half-edge conservation)

There is an integer

\[
 t={c-d\over2}
\tag{3.1}
\]

such that

\[
 a_A=d_A-t,
 \qquad a_B=d_B-t,
 \qquad c=d+2t.
\tag{3.2}
\]

Consequently the final sector counts are

\[
 (|F'_{AA}|,|F'_{AB}|,|F'_{BB}|)
 =(389-t,80+2t,389-t).
\tag{3.3}
\]

#### Proof

Deleted and added half-edges balance separately on each shore:

\[
 2d_A+d=2a_A+c,
 \qquad
 2d_B+d=2a_B+c.
\tag{3.4}
\]

Equations (3.1)--(3.3) follow.  In particular `c-d` is even.  QED.

Strict top residence forces the final AB bank to be a matching: no middle
vertex can be incident with two AB edges, since that would create a top run
of length one.  Delete the AB bank from a mixed connected factor.  On each
shore one obtains boundary-to-boundary paths, with degree one at boundary
vertices and degree two internally.  Therefore

\[
 b_A=b_B={|F'_{AB}|\over2}=40+t.
\tag{3.5}
\]

For the desired connected carrier, these are exactly the A- and B-block
counts.  If disconnected factors are admitted, the same statement applies
to all mixed components; monochromatic components require a separate
physical-length residence check.

### Lemma 3.2 (local top-residence criterion)

Assume the cross bank is a matching.  Top-one/top-zero run length is at
least four on every mixed component if and only if every same-shore
boundary-to-boundary path has at least four vertices.  Equivalently:

1. no same-shore edge joins two boundary vertices; and
2. no nonboundary vertex has two boundary neighbours on its shore.

#### Proof

The matching hypothesis excludes a block of one vertex.  A two-vertex block
is exactly a same-shore edge with two boundary endpoints.  A three-vertex
block is exactly a nonboundary middle vertex adjacent to two boundary
vertices.  Excluding these three cases is equivalent to block length at
least four.  QED.

Thus an AB insertion splits one A block and one B block; an AB deletion
merges one block on each shore.  Formula (3.5) is the global signed version
of this split/merge calculus.

## 4. Exact q1 palette ledger

For a target colour `q`, let `[E]_q` denote the number of edges of `E`
having colour `q` in the indicated palette.  The targetwise signed changes
are

\[
 \Delta L_0(q)
 =[J_{AA}]_q+[J_{AB}]_q-[D_{AA}]_q-[D_{AB}]_q,
\tag{4.1}
\]

\[
 \Delta L_1(q)=[J_{BB}]_q-[D_{BB}]_q,
\tag{4.2}
\]

\[
 \Delta U_0(q)=[J_{AA}]_q-[D_{AA}]_q,
\tag{4.3}
\]

\[
 \Delta U_1(q)
 =[J_{BB}]_q+[J_{AB}]_q-[D_{BB}]_q-[D_{AB}]_q.
\tag{4.4}
\]

These are exact multiset identities, not merely total counts.  Completeness
means that the source multiplicity plus the corresponding change is at
least one for every target.

Summing (4.1)--(4.4) and using (3.2), the four final occurrence totals are

\[
 (L_0,L_1,U_0,U_1)
 =(469+t,389-t,389-t,469+t).
\tag{4.5}
\]

Relative to (1.1), their scalar excesses are

\[
 (40+t,54-t,54-t,40+t).
\tag{4.6}
\]

Thus scalar q1 capacity alone gives

\[
 -40\le t\le54.
\tag{4.7}
\]

### 4.1 A cut-specific scalar obstruction

For a fixed cut `D`, let

* `e_A` be the number of `L_0` rows absent after retaining `F_0\setminus D`;
* `h_A` be the number of absent hard `U_0` rows;
* `h_B` be the number of absent hard `L_1` rows;
* `e_B` be the number of absent `U_1` rows.

Every repair satisfies

\[
\max\left\{
 -\left\lfloor{d\over2}\right\rfloor,
 e_A-d_A-d,
 e_B-d_B-d
\right\}
\le t
\tag{4.8}
\]

and

\[
 t\le
 \min\{54,d_A,d_B,d_A-h_A,d_B-h_B\}.
\tag{4.9}
\]

Indeed, `c=d+2t` must be nonnegative.  The `L_0` additions number
`a_A+c=d_A+d+t`, and the `U_1` additions number `a_B+c=d_B+d+t`, proving
(4.8).  Only AA edges supply `U_0`, and only BB edges supply `L_1`, proving
(4.9).  These conditions remain only scalar necessities.

### 4.2 Solver-free unique-provider strengthening

Because a globally unique current q1 row identifies its sole source edge,
the number of such rows lost by a cut is additive over the local transversal
components.  The same 112-component convolution proves:

\[
 \text{every radius-147 cut loses at least 171 unique q1 rows},
\tag{4.10}
\]

and at least

\[
 H(d)=\max(60,71-d)
\tag{4.11}
\]

unique hard rows when it deletes `d` old AB edges.  Thus at least 86 of the
147 added edges must jointly act as providers for the unique-row damage.
More importantly, the number of same-shore additions is

\[
 a_A+a_B=147-d-2t.
\]

Each such edge supplies at most one hard row, so

\[
 t\le
 \left\lfloor{147-d-H(d)\over2}\right\rfloor.
\tag{4.12}
\]

The exact transversal atlas also gives `0<=d<=27`, whence

\[
 t\ge-\lfloor d/2\rfloor\ge-13.
\tag{4.13}
\]

Maximizing (4.12) over `0<=d<=27` gives 38.  Combining (3.3), (3.5),
(4.12), and (4.13) proves the sharp audited necessary window (0.3).
It is a count window, not an existence theorem.

## 5. AB colours are boundary-endpoint data

Take an A vertex `P` and a B vertex `z+Q`.  Since `|P|=8` and `|Q|=7`, a
Johnson AB edge exists exactly when

\[
 Q\subset P.
\tag{5.1}
\]

Its q1 colours are

\[
 \lambda(P,z+Q)=Q\in L_0,
 \qquad
 \upsilon(P,z+Q)=z+P\in U_1.
\tag{5.2}
\]

Consequently the AB contribution to `L_0` depends only on its B endpoint,
and its contribution to `U_1` depends only on its A endpoint.  Pairing the
same boundary sets in a different way changes neither q1 palette.  It can,
however, change quotient components, voltage, and chronological seams.

Let `P_A,P_B` be the endpoint sets of a final cross matching `M`, and let
`H_A,H_B` be the final same-shore graphs.  Then the four support identities
are

\[
 L_0(F')=L_0(H_A)\cup\{Q:z+Q\in P_B\},
\tag{5.3}
\]

\[
 U_0(F')=U_0(H_A),
\tag{5.4}
\]

\[
 L_1(F')=L_1(H_B),
\tag{5.5}
\]

\[
 U_1(F')=U_1(H_B)\cup\{z+P:P\in P_A\}.
\tag{5.6}
\]

Thus `H_A` must cover every hard `U_0` row and every `L_0` row not already
present as a B-boundary label.  Likewise `H_B` must cover every hard `L_1`
row and every `U_1` row not already present as an A-boundary label.

## 6. Exact cut--cross--shore flow theorem

Fix a radius-147 cut `D`.  Put `R=F_0\setminus D`, and let `C` be its
retained AB bank.  Choose a set `X` of off-source labelled AB edges such that
`C union X` is a matching.  At every vertex,

\[
 d_X(v)\le d_D(v),
\tag{6.1}
\]

and no endpoint of a retained edge of `C` may be used by `X`.

Let `J_A,J_B` be the new same-shore edges.  Exact degree restoration is

\[
 d_{J_s}(v)=b_s(v):=d_D(v)-d_X(v),
 \qquad s\in\{A,B\}.
\tag{6.2}
\]

### Theorem 6.1 (variable-cross decomposition)

Conditional on `D` and `X`, degree two and complete lower/upper q1 support
are feasible if and only if, independently for each shore `s`, the
same-shore off-source catalogue contains a coloured `b_s`-factor covering
every q1 row not already supplied by `R union X`.

#### Proof

Deleting `D` creates exactly `d_D(v)` degree units at `v`.  The new cross
bank consumes `d_X(v)` of them, giving (6.2).  All remaining candidate edges
are same-shore, and their endpoint sets are disjoint between A and B.
Identities (5.3)--(5.6) assign every residual q1 row to exactly one shore.
Thus the two degree systems and the two coloured provider systems separate.
Conversely, adjoining the cross bank and two coloured factors restores
degree two and every q1 row.  QED.

### Theorem 6.2 (exact cross Hall condition)

Prescribe zero-one new-cross incidence vectors `p_A,p_B` on the two shores,
supported on vertices exposed by `D` and avoiding endpoints of `C`.  Let
`G_D` be the admissible off-source labelled AB multigraph on these vertices.
A new cross matching with these incidences exists if and only if

\[
 p_A(V_A)=p_B(V_B)
\tag{6.3}
\]

and, for every `S subseteq V_A`, `T subseteq V_B`,

\[
 p_A(S)-p_B(T)
 \le e_{G_D}(S,V_B\setminus T).
\tag{6.4}
\]

#### Proof

Send `p_A(a)` units from a source to each A vertex, one unit through each
labelled AB edge, and `p_B(b)` units from each B vertex to a sink.  A cut
with A-side `S` and B-side `T` has capacity

\[
 p_A(V_A\setminus S)+e_{G_D}(S,V_B\setminus T)+p_B(T).
\]

Requiring this to be at least the common total in (6.3) is exactly (6.4).
Integral max flow gives the matching.  QED.

When the two free endpoint sets are already prescribed, (6.4) is ordinary
Hall.  Parallel labelled edges do not change endpoint feasibility, but their
labels remain relevant to voltage and physical chronology.

### 6.1 Exact shore completion

For one shore, let `K` be the candidate same-shore graph, `b` the demand in
(6.2), and `Q` the residual q1 rows.  A coloured `b`-factor exists if and
only if there is a provider bank `P subseteq K` such that

1. `P` covers every row of `Q`;
2. `d_P(v)<=b(v)` at every vertex; and
3. `K\setminus P` has an `f`-factor with `f=b-d_P`.

The third condition is characterized exactly by Tutte's `f`-factor
inequalities.  In the notation of disjoint vertex sets `S,T`, it is

\[
 f(S)+\sum_{v\in T}\bigl(d_{K-P-S}(v)-f(v)\bigr)
 \ge q(S,T),
\tag{6.5}
\]

where `q(S,T)` counts components `W` of
`(K\setminus P)-(S union T)` for which

\[
 f(W)+e(W,T)
\]

is odd.

If the shore scaffold is genuinely bipartite, with sides `L,R`, define

\[
 \sigma(S,T)=e_K(S,R\setminus T)-b(S)+b(T).
\tag{6.6}
\]

Then a forced provider bank `P` extends to a `b`-factor exactly when it is
endpoint-feasible and

\[
 e_P(L\setminus S,T)\le\sigma(S,T)
\tag{6.7}
\]

for all `S subseteq L,T subseteq R`.  A paired-colour laminar Rado--Hall
selection is therefore a sufficient integral provider flow, and it is exact
within its fixed laminar atlas.  Artificially cloning a nonbipartite shore
does not remove the odd-component terms in (6.5).

Theorems 6.1--6.2 solve the degree/q1 decomposition only.  Path length four,
new old-coordinate motifs, connectivity, voltage, deeper shadows, and the
literal compiler remain separate constraints.

## 7. A hereditary hard-row obstruction

For a fixed cut `D`, the maximal same-shore demand is `d_D`; every cross
choice lowers it to `b=d_D-d_X`.  Consequently the endpoint-accessible
same-shore provider atlas is monotone:

\[
 K[b]\subseteq K[d_D].
\tag{7.1}
\]

AB edges supply neither `U_0` nor `L_1`.  This gives the following
cut-master filter.

### Proposition 7.1 (hard-access no-go)

If a hard row lost by `D` has no retained provider and no off-source
same-shore provider whose endpoint incidences fit `d_D`, then no
variable-cross completion of `D` exists.

More generally, for a family `Q` of hard rows on one shore, let `E_D(Q)` be
their endpoint-accessible provider bank under `d_D`, and let
`rho_{d_D}` be the maximum size of an endpoint-capacity-feasible subset.
Every completion requires

\[
 \rho_{d_D}\left(\bigcup_{q\in Q}E_D(q)\right)\ge |Q|.
\tag{7.2}
\]

#### Proof

Equation (7.1) says no cross selection can reveal a new same-shore provider.
Each same-shore edge has exactly one hard colour on its shore, so distinct
hard rows require distinct endpoint-feasible provider edges.  This proves
the singleton and family statements.  QED.

The rank in (7.2) is a necessary capacity rank, not generally a matroid rank;
without bipartite or laminar structure, these inequalities are not claimed
to replace Tutte.

### Corollary 7.2 (the canonical cut is dead even with variable cross)

The certified `87 AA + 60 BB` cut has three hard `L_1` rows

\[
 1{:}845,qquad1{:}1433,qquad1{:}2347
\tag{7.3}
\]

with no endpoint-accessible BB provider under maximal demand `d_D`.
Therefore this cut admits no variable-cross repair, including a pure AB
insertion.

This is a theorem for that exact cut.  It does not exclude a different
radius-147 transversal chosen jointly with its new boundary bank.

## 8. The cuttable-endpoint DAG obstruction

Although only 27 old AB edges can occur in a globally valid minimum
transversal, the 476-edge packing union contains 36 old AB edges.  Use this
larger set `C_cut`; a no-go on it applies a fortiori to every minimum cut.
The source AB bank is a matching, so write these old edges as

\[
 a_i b_i\qquad(1\le i\le36).
\]

Inspect the **full labelled quotient catalogue**, including every relative
phase.  On the 36 A endpoints and 36 B endpoints, it has exactly 55 AB
edges and 55 endpoint pairs:

\[
 36\text{ old diagonal edges}+19\text{ off-source edges}.
\tag{8.1}
\]

In particular, no old endpoint pair has a parallel labelled alternative.
Contract each old pair `a_i b_i`, and orient an off-source edge `a_i b_j` as
`i -> j`.  The resulting 19-arc digraph is acyclic.  One certified
topological order, written by old edge ID, is

```
118,1887,4598,5133,8173,8436,9141,9483,10035,10236,10307,
10880,11003,12055,12264,12675,12815,13977,14400,14501,
14844,15411,4691,5395,10740,12743,10537,15237,8081,15160,
10269,13639,15288,9812,6449,9935.
```

The exact 19 arcs and their new labelled edge IDs are frozen in the audit
JSON.

### Theorem 8.1 (no boundary-neutral AB rerouting at radius 147)

Assume a radius-147 resident repair has `t=0` and preserves both old AB
boundary endpoint sets.  Then its AB bank equals the old AB bank.  Hence any
nontrivial radius-147 AB change must alter at least one boundary endpoint.

#### Proof

An endpoint of a retained old AB edge is already cross-saturated, so every
changed old AB edge belongs to `D_AB subseteq C_cut`.  If the new and old
boundary endpoint sets agree, the symmetric difference between the deleted
old submatching and the new matching is a nonempty disjoint union of
labelled alternating cycles.

A two-edge alternating cycle would be a parallel labelled alternative on
one old pair, excluded by (8.1).  Every longer alternating cycle projects,
after contracting the old matching, to a directed cycle in the 19-arc
digraph, excluded by the displayed topological order.  Therefore no
nontrivial alternative matching exists.  QED.

The full graph on all 80 old boundary pairs does contain alternating cycles.
The theorem is deliberately scoped to the 36 cuttable pairs forced by the
radius-147 packing normal form.

Since `t!=0` already changes the boundary-set cardinality, Theorem 8.1 means
that **every** radius-147 AB-pattern change is a genuine boundary migration,
split, or merge.  It cannot be a palette-neutral re-pairing of the same
cuttable boundary flags.

## 9. Sparse AB pairing of unique easy rows

Among the 27 globally eligible old AB cuts, the source lower/upper
multiplicity types are exactly

\[
 20(1,1),\qquad4(1,2),\qquad3(2,1).
\tag{9.1}
\]

Thus every eligible AB deletion kills at least one globally unique easy q1
row.  For `d` such deletions,

\[
 |L_{\rm unique}|\ge\max(0,d-3),
 \qquad
 |U_{\rm unique}|\ge\max(0,d-4),
\tag{9.2}
\]

and

\[
 |L_{\rm unique}|+|U_{\rm unique}|
 \ge
 \begin{cases}
 d,&d\le7,\\
 2d-7,&d\ge7.
 \end{cases}
\tag{9.3}
\]

Across all 24 eligible unique lower colours and 23 eligible unique upper
colours, the off-source AB catalogue contains only six joint providers, and
their bipartite matching number is five.  For a fixed cut `D`, let `G_D` be
the induced graph between the actually lost unique lower and upper rows.
Then even before degree and residence are imposed, the number of new edges
needed to restore these rows is at least

\[
 |L_D|+|U_D|-\nu(G_D).
\tag{9.4}
\]

At `d=27`, (9.4) is at least

\[
 24+23-5=42.
\tag{9.5}
\]

This is a useful sparse-palette filter, not a contradiction to the
147-addition budget.

## 10. The three primitive AB directions

The smallest countwise AB changes are:

1. **Pure insertion**:

   \[
   d=0,\quad c=2,\quad t=1,
   \]

   giving final counts `(388,82,388)`, 41 blocks per shore, easy q1 excess
   41, and hard q1 excess 53.

2. **Boundary relocation**:

   \[
   d=c=1,\quad t=0.
   \]

   By Theorem 8.1 this must migrate at least one boundary endpoint.

3. **Pure merge**:

   \[
   d=2,\quad c=0,\quad t=-1,
   \]

   giving 39 blocks per shore.

The trusted fixed-cross radius-147 infeasibility result excludes only
`(d,c)=(0,0)` when the entire old AB bank is retained.  It does not imply
`d>=1`.  In particular,

```
scratch/search_k16_dynamic_cross_radius147_cut_seam_20260729.py
```

contains an explicit constraint requiring at least one old AB deletion and
therefore omits primitive 1.  By contrast,

```
scratch/search_k16_residence_radius147_variable_cross_ffactor_20260729.py
```

does not impose that row and includes the pure-insertion branch at its stated
degree/q1/original-motif scope.

## 11. Exact remaining theorem

Radius 147 is neither proved feasible nor proved impossible.  A complete
positive certificate must jointly choose:

1. one local minimum transversal in each of the 112 motif-intersection
   components;
2. new A/B boundary incidence vectors satisfying (6.1), the migration
   theorem, and the cross Hall inequalities (6.3)--(6.4);
3. a labelled AB matching on those endpoints;
4. two coloured shore factors satisfying the hard-access filters and the
   exact Tutte or genuine-bipartite Hall conditions;
5. boundary-to-boundary shore paths of at least four vertices;
6. no newly created old-coordinate residence motif;
7. the required component/voltage chronology;
8. all deeper lower and upper shadow ledgers; and
9. the literal compiler.

Conversely, a radius-147 no-go may now be proved by a setwise Hall/Tutte
violation or by the path-length/new-motif rows on this exact local-product
face.  Scalar sector capacity alone cannot close it.

## 12. Frozen artifacts and scope

New solver-free audit:

```
scratch/audit_k16_radius147_ab_structure_20260729.py
SHA-256 b76e439952f2f98bd614834037767f21786105429ece67e0e054407f04df27ca

scratch/k16_radius147_ab_structure_20260729.audit.json
SHA-256 d2d239430e82c4a5e5b560ca8a1fd5b6dcb074c2c5ebdcadc4c7b1b5f98f470c
```

Authoritative inputs:

```
scratch/k16_qfactor_q1_topresident_hamilton_20260729.json
SHA-256 f76ab4e5c30c3269da87788c275777a3b40deea96f4fbf892cd5c6027280a7a5

scratch/k16_qfactor_q1_topresident_hamilton_residence_motifs_20260729.audit.json
SHA-256 bf762af0339ec581d01e9c48991610425e51a864e065be23b8d23d21efbbf1f6

scratch/k16_residence_fixed_cross_same_shore_transversal_barrier_20260729.json
SHA-256 93936bcc90b3a627f8fea38d1038136c17278f63fdbb623f69ea8bd28703dcb2
```

The new audit performs no SAT or factor search.  It enumerates only the tiny
local transversal tables, convolves exact integer supports, builds two small
AB graphs, and verifies the stated identities in about one second locally.

The motif equality controls destruction of the **old** short-run motifs.
Added edges may create new motifs.  The fixed-cross infeasibility statement
is a trusted CP-SAT transcript without a retained standalone proof log and
is used only at that scope.  At radius 147, 147 quotient edge orbits are
removed and 147 added: 2,205 physical edges are removed and 2,205 added, so
the physical edge symmetric difference has size 4,410.

