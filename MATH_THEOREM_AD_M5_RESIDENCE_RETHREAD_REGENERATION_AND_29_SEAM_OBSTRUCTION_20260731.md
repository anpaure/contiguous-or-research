# The item2183 interior rethread: exact regeneration state and a sharp 29-seam obstruction

Date: 2026-07-31  
Status: exact finite reduction and exact support lower bound; no accepting
joined all-depth/compiler chronology is claimed

## 0. Verdict

Let \(F\) be the frozen item2183 two-sided-rainbow forest on
\(J(10,5)\).  It has \(252\) owners, \(210\) selected edges and \(42\)
path components.  Its selected edges use every rank-four intersection and
every rank-six union exactly once.  A separately frozen set of \(42\)
connector edges closes it to a Hamilton cycle whose upper/lower flag tower
is complete at every depth.  Nevertheless \(F\) contains \(31\) strictly
internal coordinate words \(0110\), on \(18\) paths, so no chronology which
keeps all forty-two paths intact is depth-two resident.

The interior obstruction is substantially larger than the path count.

> **Sharp run-span theorem.** Every fragment rethread eliminating all
> thirty-one inherited length-two runs must delete at least \(29\) original
> forest seams.  There are exactly
> \[
>                         2\,3^{27}=15,251,194,969,974
> \]
> minimum run-span transversals.  One original seam is forced in every
> minimum transversal.

Thus every rethread changing at most \(28\) original forest seams is
impossible from run spans alone.  The support-\(29\) equality face admits a
q1 palette cycle cover, but the complete 511-variable degree relaxation is
proof-producing UNSAT: every such cover gives some middle owner degree at
least three.  Hence every two-palette Catalan path-forest rethread has
support at least \(30\).  This does not prove feasibility at support 30.

There are two meanings of “preserve the joint decoration,” and they have
different answers.

1. If it means preserve the *same* lower-to-upper colour pairing, then no
   interior change is possible: one rank-four/rank-six pair determines one
   Johnson edge.  Hence strict frozen-decoration preservation is
   incompatible with residence.
2. If it means retain the property of being a complete joint decoration,
   then the exact remaining q1 gate is a loopless directed cycle cover on
   the deleted colour pairs.  Owner degrees, forest topology, the flag
   tower, residence and compiler Hall are additional, independent rows.

Sections 4--8 give an exact local regeneration theorem separating these
rows.  It is the finite state that a constructive search or recursive
packet must satisfy.  It is not an existence proof.

## 1. Frozen physical object

Put

\[
 \Omega=[10],\qquad
 \mathcal X={\Omega\choose5},\qquad
 \mathcal L={\Omega\choose4},\qquad
 \mathcal U={\Omega\choose6}.
\]

For a Johnson edge \(e=XY\), define

\[
                         \lambda(e)=X\cap Y,
 \qquad                  \upsilon(e)=X\cup Y.       \tag{1.1}
\]

The item2183 forest \(F\) satisfies

\[
 |V(F)|=252,qquad |E(F)|=210,qquad c(F)=42,         \tag{1.2}
\]

and both maps

\[
       e\mapsto\lambda(e),\qquad e\mapsto\upsilon(e) \tag{1.3}
\]

are bijections from \(E(F)\) onto \(\mathcal L\) and \(\mathcal U\),
respectively.  The path-order histogram is

\[
1^3 2^2 3^{11}4^8 5^2 6^1 7^4 8^3 9^2
11^1 12^1 13^2 16^1 29^1.                           \tag{1.4}
\]

The frozen connector closure covers the complete upper-union and
lower-intersection tower through depth five.  Exactly \(46\) linear
openings retain the complete tower; \(39\) cut a connector and therefore
keep all edges of \(F\).

## 2. Strict decoration rigidity

### Lemma 2.1 (one colour pair, one physical edge)

For \(L\in\mathcal L\) and \(U\in\mathcal U\), a Johnson edge with lower
colour \(L\) and upper colour \(U\) exists if and only if \(L\subset U\).
When it exists it is unique.

#### Proof

The difference \(U\setminus L\) has two points, say \(a,b\).  The two
rank-five sets strictly between \(L\) and \(U\) are \(L+a\) and \(L+b\),
so the only possible edge is

\[
                            (L+a)(L+b).              \tag{2.1}
\]

Conversely (2.1) has intersection \(L\) and union \(U\). \(\square\)

### Corollary 2.2 (strict-decoration no-go)

Any two-sided-rainbow forest using the same bijection
\(\lambda(e)\mapsto\upsilon(e)\) as \(F\) is exactly \(F\).  Consequently
no interior rethread can both retain the frozen joint decoration literally
and remove even one of the inherited run defects.

This does not rule out a representative-changing alternating exchange
which produces a *different* complete joint decoration.

## 3. Closed run spans and the exact transversal

Let

\[
                         P=(v_0,\ldots,v_{a-1})
\]

be a source path and fix a coordinate \(z\).  If four consecutive vertices
have \(z\)-word

\[
                             0,1,1,0,                \tag{3.1}
\]

call their three intervening source edges the **closed span** of the run.

### Lemma 3.1 (closed-span invariance)

Suppose source edges are deleted, every surviving source fragment is
retained intact up to reversal, and the fragments are reconnected.  If no
edge in a closed span is deleted, then the new chronology still contains
the same internal length-two positive run.

#### Proof

All four vertices remain consecutive in one retained fragment.  Reversal
fixes the word \(0110\), and reconnection outside the fragment cannot alter
either bounding zero. \(\square\)

The \(31\) closed spans lie on \(18\) paths.  Their pathwise interval
stabbing numbers are

\[
 2,6,2,1,1,1,2,2,2,1,1,2,1,1,1,1,1,1,             \tag{3.2}
\]

whose sum is \(29\).

### Theorem 3.2 (sharp 29-seam support obstruction)

Every fragment rethread removing all inherited internal length-two runs
deletes at least \(29\) original forest edges.  A family of \(29\)
pairwise edge-disjoint closed spans and a \(29\)-edge hitting set certify
equality.

#### Proof

On each source path the spans are intervals in the line of path edges.
The minimum number of integer edge positions meeting them equals the
maximum number of pairwise disjoint intervals: greedily choose the right
endpoint of the first unhit interval.  The greedy intervals are disjoint
and the chosen endpoints hit every interval.  Apply this independently on
each path and sum (3.2). \(\square\)

Only two overlaps save a deletion relative to the raw count \(31\).

* On path \(15\), spans \([9,11]\) and \([11,13]\) force edge \(11\).
* On path \(26\), spans \([1,3]\) and \([2,4]\) may be hit by edge \(2\)
  or edge \(3\).

Every other defect group is one three-edge choice disjoint from the other
groups.  Hence every equality deletion set consists of the forced
\((15,11)\), one of \((26,2),(26,3)\), and one of three edges in each of
the other \(27\) spans.  This proves the exact count \(2\,3^{27}\).
The audit JSON records all runs, the primal and dual certificates, the
forced edge, and one canonical minimum set.

## 4. Exact q1 redecorating criterion

Let \(R\subseteq E(F)\) be the set of actually deleted decoration edges.
Form a directed graph \(D_R\) on vertex set \(R\), putting

\[
 e\longrightarrow f
 \quad\Longleftrightarrow\quad
 e\ne f\ \hbox{ and }\ \lambda(e)\subset\upsilon(f). \tag{4.1}
\]

### Theorem 4.1 (palette cycle-cover theorem)

There is a set \(A\) of \(|R|\) new Johnson edges such that

\[
                     F'=(F-R)\cup A                 \tag{4.2}
\]

uses every lower and every upper q1 colour exactly once if and only if
\(D_R\) has a directed cycle cover.  If \(\sigma\) is the corresponding
loopless permutation of \(R\), then the new edge indexed by \(e\) is the
unique edge

\[
           a_e=\bigl(\lambda(e)+x\bigr)
               \bigl(\lambda(e)+y\bigr),
 \qquad \{x,y\}=\upsilon(\sigma(e))\setminus\lambda(e). \tag{4.3}
\]

#### Proof

Every deleted lower colour \(\lambda(e)\) must be paired with exactly one
deleted upper colour, and every deleted upper colour must be used exactly
once.  Thus any replacement gives a permutation \(\sigma\).  Containment
is precisely the existence condition in Lemma 2.1, while a fixed point
would reinsert the deleted old edge and contradict that \(R\) is the actual
difference support.  This gives a directed cycle cover.  Conversely a
cycle cover and Lemma 2.1 give (4.3), with every deleted colour restored
once. \(\square\)

The palette condition alone is not physical topology.  For a proposed
cycle cover, define

\[
 d_{F'}(v)=d_F(v)-|\{e\in R:v\in e\}|
                  +|\{e\in R:v\in a_e\}|.          \tag{4.4}
\]

Then \(F'\) is again a Catalan path forest exactly when

\[
 d_{F'}(v)\le2\quad(v\in\mathcal X)                 \tag{4.5}
\]

and \(F'\) is acyclic.  Since it has \(252\) vertices and \(210\) edges,
these conditions force exactly \(42\) path components.  Thus owner-degree
circulation and the graphic row remain separate from the cycle-cover row.

At equality in Theorem 3.2 there are \(29\) choice groups and \(84\)
candidate deleted edges.  The complete candidate incidence graph contains
exactly four mutual two-cycles, at path-edge pairs

\[
 \{(1,3),(1,4)\},\quad
 \{(3,21),(3,22)\},\quad
 \{(3,24),(3,25)\},\quad
 \{(12,3),(12,4)\}.                                \tag{4.6}
\]

The canonical right-endpoint minimum transversal has an acyclic
off-diagonal incidence digraph, hence has no palette replacement at all.
This is a no-go for that one minimum transversal, not for every equality
transversal.

In fact the q1 row is feasible at equality.  The companion audit gives one
minimum transversal whose selected edge indices in the twenty-nine choice
groups are

```text
1,5,6,10,15,19,22,25,3,7,0,1,0,2,6,2,8,1,6,1,4,1,11,4,4,1,0,1,2
```

and whose successor permutation is the single directed \(29\)-cycle

```text
0,5,6,24,26,19,21,3,12,10,11,18,1,28,4,17,13,23,22,27,
16,8,20,15,9,14,25,2,7.
```

Literal replay gives twenty-nine distinct inserted Johnson edges, disjoint
from the deleted edges, and exactly restores both deleted q1 colour
multisets.  Therefore palette closure does **not** raise the support floor
above \(29\).  This particular cycle cover is not owner-balanced: its
degree delta is supported on \(70\) owners, with \(35\) losing one and
\(35\) gaining one.  More decisively, direct replay gives degree histogram

\[
                         0^4 1^{94}2^{136}3^{18}
\]

and one 71-vertex/71-edge cyclic component.  It therefore fails both
physical rows.  Exact owner balance would be sufficient but is not
necessary; the exact requirements remain (4.5) and acyclicity.

### Proposition 4.2 (compact exact equality master before topology)

Index the \(84\) candidate deleted edges by \(i\), with choice group
\(g(i)\in[29]\).  There are exactly \(427\) compatible directed arcs
\(i\to j\) with \(g(i)\ne g(j)\).  Binary variables \(x_i\) and
\(y_{ij}\) describe a support-\(29\) palette exchange with owner capacity
exactly when

\[
 \sum_{g(i)=g}x_i=1                                           \tag{4.7}
\]

for every group \(g\),

\[
 \sum_jy_{ij}=x_i=\sum_jy_{ji}                                \tag{4.8}
\]

for every candidate \(i\), and

\[
 d_F(v)-\sum_{i:v\in e_i}x_i
       +\sum_{ij:v\in a_{ij}}y_{ij}\le2                      \tag{4.9}
\]

for every middle owner \(v\).  Here \(a_{ij}\) is the unique cross edge
using the lower colour of \(i\) and upper colour of \(j\).

#### Proof

Equation (4.7) is exactly the equality hitting-set normal form.  Equations
(4.8) select a loopless permutation on the chosen candidates, hence are
Theorem 4.1.  Equation (4.9) is precisely (4.4)--(4.5).  Conversely every
support-\(29\) palette exchange with owner capacity defines these variables.
\(\square\)

Acyclicity is not implied by (4.7)--(4.9).  It is imposed exactly by

\[
 |(F-R)[S]|+\sum_{ij:a_{ij}\subseteq S}y_{ij}\le |S|-1
 \quad(\varnothing\ne S\subseteq\mathcal X),                  \tag{4.10}
\]

or separated by a cycle oracle.  This gives a \(511\)-variable exact master
(\(84+427\)) before the graphic row; it is not a width or locality
relaxation.

For this frozen equality domain, (4.7)--(4.9) are in fact infeasible.  The
independently reconstructed CNF has 511 variables and 15,154 clauses; a
DRAT proof and an extracted 1,076-clause core both verify.  The encoded
owner row is exactly (4.9), not restoration of every old degree.  Therefore
acyclicity need not be invoked to exclude support 29.

## 5. Exact depth-two local regeneration

An internal positive run of a binary coordinate word has forbidden length
one or two exactly when the word contains a factor

\[
                         010\quad\hbox{or}\quad0110. \tag{5.1}
\]

The item2183 source paths have no strictly internal length-one positive
run.  Delete a set \(R\) meeting every one of the \(31\) closed spans and
let \(\mathcal Q(R)\) be the resulting source fragments.

### Theorem 5.1 (radius-three residence regeneration)

Let \(T'\) be any linear chronology obtained by orienting the fragments in
\(\mathcal Q(R)\) and joining them by Johnson-legal new seams.  Then
\(T'\) is depth-two resident if and only if no new-seam-crossing coordinate
word is \(010\) or \(0110\).  Equivalently it is enough, and necessary, to
inspect the at most four vertices in every new-seam collar, with the two
linear ends treated as open rather than cyclic.

#### Proof

Deleting edges cannot create a forbidden run strictly inside a retained
fragment.  The source has no internal \(010\), and Lemma 3.1 together with
the hitting hypothesis removes every internal \(0110\).  Therefore any
forbidden run in \(T'\) crosses a new seam and has one of the two forms
(5.1).  Conversely either displayed word bounded away from a linear end is
an internal positive run of length one or two. \(\square\)

Thus the residence row is genuinely local *after* the global 29-seam
hitting debt has been paid.  Hitting the old spans is not sufficient: a new
seam may create a fresh factor in (5.1).

## 6. Exact all-depth flag transfer

For a chronology \(T=(T_0,\ldots,T_{N-1})\), a depth-\(q\) occurrence is
a block of \(q+1\) consecutive owners, evaluated by union on the upper
shore and intersection on the lower shore.  Suppose old and new cyclic
closures share a family of maximal retained fragments \(\mathcal P\), and
let \(s\) be the number of old-only physical seams.  Put

\[
                         b_q=\sum_{P\in\mathcal P}\min(q,|P|)
                         \le qs.                    \tag{6.1}
\]

Exactly \(b_q\) old and \(b_q\) new depth-\(q\) occurrences cross the
respective seam sets; every other occurrence transports under fragment
reversal with the same union and intersection.

### Theorem 6.1 (last-provider criterion)

For each target \(S\) at rank \(5+q\) or \(5-q\), let
\(\mathcal C_q(S)\) be its occurrences wholly inside common fragments and
let \(\mathcal N_q(S)\) be its new seam-crossing occurrences.  The new
cyclic closure covers the complete depth-\(q\) layer if and only if

\[
                  \mathcal C_q(S)\cup\mathcal N_q(S)\ne\varnothing
                  \quad\hbox{for every }S.          \tag{6.2}
\]

For a linear opening, occurrences crossing the deleted opening are removed
and its prefix/suffix halo must be tested literally.  Hence a complete
cyclic tower does not by itself certify every opening.

At q1, Theorem 4.1 supplies every lower and upper colour inside \(F'\), so
opening a connector preserves q1 automatically.  At depths two through
five, (6.2) is the exact condition.  In particular no rankwise marginal or
component-count argument substitutes for the occurrence test.

## 7. Endpoint closure and the complete finite rethread theorem

Assume Theorem 4.1 gives \(F'\), and assume (4.5) plus acyclicity, so
\(F'\) is a forty-two-path forest.  Give an isolated vertex two endpoint
occurrences and every nontrivial path its two ordinary endpoints.  A set
\(C'\) of forty-two Johnson edges closes \(F'\) to one Hamilton cycle
exactly when it uses every endpoint occurrence once and its graph after
contracting the forty-two paths is connected.  Choose one edge of \(C'\)
as the linear opening.

### Theorem 7.1 (exact interior-regeneration criterion)

An accepting residence-safe, joint-q1-decorated, all-depth rethread of the
item2183 forest exists with internal deletion set \(R\) if and only if all
of the following finite conditions hold.

1. **Old-run hitting:** \(R\) meets all thirty-one closed spans.
2. **Joint decoration:** \(D_R\) has a directed cycle cover whose physical
   edges satisfy (4.5) and the graphic acyclicity row.
3. **Closure:** the resulting forty-two paths have a Johnson-legal endpoint
   matching whose contracted graph is connected, together with a declared
   opening.
4. **Residence:** every new-seam collar away from the opening avoids both
   words in (5.1), in every coordinate.
5. **Flag tower:** condition (6.2), with the declared linear endpoint
   correction, holds for every \(q=2,3,4,5\).

If “compiler-ready” is also required, append the exact envelope/Hall row of
Section 8.

#### Proof

Necessity is Lemma 3.1, Theorem 4.1, the endpoint degree/connectivity
criterion, Theorem 5.1 and Theorem 6.1.  Conversely conditions 2 and 3 give
a literal Hamilton chronology using every middle owner once and every q1
colour.  Condition 4 gives depth-two residence.  Condition 5 gives every
deeper upper union and lower intersection.  Every assertion concerns
literal consecutive blocks of the one declared chronology. \(\square\)

This theorem is a local regeneration theorem in the precise sense that,
after the global run-span and palette debts have selected the fragments,
residence and all shadow changes are confined to occurrence-labelled seam
collars.  It does not assert that those collars can be chosen.

## 8. Compiler envelopes and exact delta

Let a linear middle chronology be

\[
                         T=(T_0,\ldots,T_{251}).
\]

For a prospective length-\(254\) depth-two source define its maximal
coordinatewise envelopes

\[
 E_j(T)=
 \bigcap_{\max(0,j-2)\le i\le\min(j,251)}T_i,
 \qquad 0\le j\le253.                              \tag{8.1}
\]

### Lemma 8.1 (exact depth-two residence equivalence)

The maximal envelope word satisfies \(D^2E(T)=T\) coordinatewise if and
only if every internal positive coordinate run of \(T\) has length at
least three.

#### Proof

If an internal run has length one or two, any source occurrence of that
coordinate contributing to the run also contributes to a neighbouring
zero, impossible.  Conversely, in a run of length at least three, every
middle position lies in some three-owner subinterval wholly inside the run;
at a linear end the shortened envelope in (8.1) supplies the one-sided
positions.  Zero positions exclude the coordinate from every source cell
which can reach them. \(\square\)

Now compare the cyclic closures of two chronologies on the same owners.
Delete the old-only seams and let \(\mathcal P\) be the maximal common
cyclic fragments.  On either cyclic chronology the exact boundary family
which contains the changed-envelope support is

\[
                  b_2=\sum_{P\in\mathcal P}\min(2,|P|)\le2s             \tag{8.2}
\]

old and the same number of new occurrences.  For a fixed linear opening,
the changed internal start set is a subset of that cyclic family; a changed
opening is handled by the endpoint terms below.  The transported OR value
of an occurrence-aligned compiler cell using \(h\) consecutive envelope
letters depends on \(h+2\) owners and \(h+1\) owner seams, so its changed
start set has size at most

\[
                  b_{h+1}=\sum_{P\in\mathcal P}\min(h+1,|P|)
                  \le(h+1)s.                        \tag{8.3}
\]

If the opening changes, the four depth-two endpoint envelope cells **per
chronology** (at most eight old/new occurrences in total) and the
corresponding wider prefix/suffix halos must be added explicitly.
Absolute-position pins, controller footprints and nonaligned representative
choices require separate phase/support terms and are not covered by (8.3).

For a chronology whose *actual full seam support* is \(s=29\), (6.1),
(8.2) and (8.3) give

\[
 b_q\le29q,\qquad b_2\le58,qquad b_{h+1}\le29(h+1). \tag{8.4}
\]

Usually only the internal forest support \(|R|\) is known; connector
changes can make \(s>|R|\).  Therefore (8.4) must not be quoted with
\(29\) unless the complete chronology has been audited to change exactly
twenty-nine seams.

Finally, the item2183 chronology is not resident and has no inherited valid
depth-two compiler matching.  The locality of (8.2)--(8.3) transports
formal envelope cells, but does **not** supply Hall.  After condition 4 of
Theorem 7.1 passes, form the literal lower-target versus physical-cell
incidence graph from (8.1).  Compiler feasibility is exactly

\[
                         |N(X)|\ge|X|                \tag{8.5}
\]

for every lower-target set \(X\), equivalently a target-saturating
matching.  If a separately certified matching exists on the transported
common cells, only then may the common-core augmenting-linkage delta theorem
be used.  No such certificate is imported here.

## 9. Exact proved and open boundary

Proved:

1. strict preservation of the frozen lower-to-upper decoration pairing
   makes every physical forest edge rigid, hence cannot repair residence;
2. every fragment rethread needs at least \(29\) deleted old forest seams;
3. the complete equality hitting-set normal form and exact count
   \(2\,3^{27}\);
4. the exact q1 palette cycle-cover criterion and the separate owner-degree
   and graphic rows;
5. the exact new-seam local residence criterion;
6. the exact all-depth last-provider criterion;
7. the exact envelope support and conditional Hall/linkage boundary; and
8. proof-producing infeasibility of every support-29 q1-palette exchange
   satisfying middle-owner degree at most two.

Open:

1. whether support \(30\), or another support below the known 119-partner
   construction, admits an internally residence-clean two-palette forest;
2. a residence-compatible and all-depth connector chronology after a
   further rethread (the 119-partner forest itself has fourteen
   endpoint-locked components and is not intact-path joinable);
3. the lower compiler Hall matching for such a chronology; and
4. a dimension-uniform controlled-debt interior regeneration theorem.

The sharpest unconditional physical impossibility is therefore support at
most \(29\), together with the stronger all-support no-go under literal
frozen decoration.  The independently replayed 119-partner matching proves
that internal residence is attainable, giving the scoped bracket
\(30\le s_{\rm int}\le119\); it does not supply endpoint joining, deeper
flags or the compiler.

## 10. Frozen evidence and scope

The exact span audit is:

```text
MATH_AUDIT_AD_M5_INTERNAL_RUNSPAN_TRANSVERSAL_20260731.md
scratch/audit_ad_m5_internal_runspan_transversal_20260731.py
scratch/ad_m5_internal_runspan_transversal_20260731.audit.json
scratch/audit_ad_m5_tau29_degree2_unsat_20260731.py
scratch/ad_m5_tau29_degree2_unsat_20260731.audit.json
```

It reconstructs the frozen item2183 forest, all \(31\) runs, the exact
interval transversal, the \(84\)-candidate equality palette interface, the
four two-cycles in (4.6), and the replayed single-\(29\)-cycle palette
certificate.  Its tiny quotient feasibility step is followed by a
solver-free literal replay.  The separate degree audit reconstructs every
CNF clause and independently verifies the full DRAT proof and extracted
core; neither audit performs a carrier search.

Authoritative upstream files are:

```text
THREAD_A_M5_THREE_C10_DOWNSTREAM_COMPATIBILITY_AUDIT_20260731.md
MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md
MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md
MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md
MATH_THEOREM_AD_RESIDENCE_REDISTRIBUTION_AUTOMATON_AND_M5_ENDPOINT_LOCK_20260731.md
scratch/ad_m5_residence_clean_triple_endpoint_obstruction_20260731.audit.json
```

All claims are scoped to fragment rethreads of the frozen item2183
\(J(10,5)\) forest unless explicitly stated as a general lemma.  No web
result, heavy search or unverified finite claim is used.
