# The exact DM-critical anchor index for primitive support-three circuits at `2e919...`

Date: 2026-08-01  
Status: **proved; complete indexed primitive support-three search authenticated**

## 1. Frozen object and scope

Let (F) be the rooted static flag factor

```text
2e9194935b261dc178daee3aaf47fc9acc1bf1f2af5b6eb31e5004bb4ffd9ceb.
```

Its common both-live root--owner graph (G_F) has maximum matching (1141)
and canonical maximum-deficiency shore

\[
 |X|=309,qquad |Y|=|N_{G_F}(X)|=20,qquad |X|-|Y|=289.       \tag{1.1}
\]

This note gives a complete, nonquadratic generator for every **primitive
support-three resource circuit which can increase the common matching**.
It is strictly broader than the factorable/overlapping-support-two
commutator shell.  No topology, upper-shadow, residence, voltage, opening,
or compiler statement is made.

## 2. The old-cut anchor theorem

An attachment state is a phase-labelled triple

\[
 s=(R,a,O),
\]

where (R) is a rank-eight quotient root, (a\notin R), and (O) is the
rank-nine quotient orbit of (R\cup\{a\}).  It is **live** precisely when
the literal transition table gives it at least one incoming and one outgoing
geometry.  Its projection contributes the common edge (R O).

### Theorem 2.1 (every matching gain has a dormant crossing anchor)

Let (C) be any resource-exact change supported on three distinct roots.  If

\[
 \nu(G_{F+C})>1141,
\]

then some state (s=(R,a,O)), with (R\in X) and (O\notin Y), is dormant
in (F), live in (F+C), and has a transition geometry (g) which is
inactive in (F), active in (F+C), and incident with a changed root.

#### Proof

For every bipartite graph (H) on the same two 1430-vertex shores,

\[
 \nu(H)\le 1430-|X|+|N_H(X)|.                              \tag{2.1}
\]

If (N_{G_{F+C}}(X)\subseteq Y), the right side is (1141), contrary to
the hypothesis.  Hence (G_{F+C}) contains an edge (RO) with (R\in X)
and (O\notin Y).  Choose a live phase state projecting to this edge.  It
was not live in (F), since (Y=N_{G_F}(X)).  Thus its old incoming count,
its old outgoing count, or both were zero.  On one zero side choose a final
active geometry.  That geometry was inactive initially.  A geometry whose
two endpoint rows are unchanged cannot change truth value, so it is incident
with the support of (C).  This is the required anchor. □

This theorem is only a necessary filter.  Activating an anchor can delete
other common edges, so every survivor must still be replayed by exact
matching and DM computation.

## 3. Exact direct geometry enumeration

Fix a physical transition geometry.  In source coordinates write its source
partition as

\[
 A=A_0\mathbin{\dot\cup}A_1\mathbin{\dot\cup}A_2,
\]

let β be the inserted coordinate, (x) the deleted coordinate, and let
σ be the canonical rotation of the target root.  For a target option put

\[
 D_i=\sigma(C_i),\quad i=0,1,2,qquad D_3=\{x\}.
\]

### Lemma 3.1 (source-partition parametrization)

The geometry is literal exactly when

\[
 x\in A_2,qquad D_1\subseteq A_0,qquad D_2\subseteq A_1,                 \tag{3.1}
\]

and

\[
 D_0=\{\beta\}\cup(A_0\setminus D_1)
                    \cup(A_1\setminus D_2)
                    \cup(A_2\setminus\{x\}).                            \tag{3.2}
\]

Consequently all compatible target options are generated, without scanning
the target menu, by choosing a target type, choosing (D_1,D_2) of its
prescribed sizes in (3.1), forcing (3.2), and rotating back by
σ(^{-1}).

#### Proof

The three containments in (3.1) are exactly the survivor conditions in the
literal transition predicate.  Its refresh identity is (3.2).  Conversely,
(3.1)--(3.2) make all survivor containments and the refresh identity true.
The four sets are disjoint and their union is the target root, so rotation
back gives a valid and unique target option. □

For the nine allowed type vectors

```text
(1,5,2),(1,6,1),(2,5,1),(3,3,2),(3,4,1),
(4,3,1),(5,1,2),(5,2,1),(6,1,1),
```

the number of compatible target options for source sizes
((|A_0|,|A_1|)) is respectively

```text
15, 21, 35, 33, 52, 69, 31, 78, 63.
```

After requiring (x\in A_2), summing over all source options gives exactly

\[
 13748                                                        \tag{3.3}
\]

compatible ordered source/target option pairs for every geometry.  The O3
census independently checked (3.3) on 32 deterministic physical geometries.

## 4. One-ended and genuinely joint anchors

For a critical geometry (g=(u,v)), let (I_u,I_v) be the incumbent
options.

* A changed literal (S\ne I_u) is a **one-ended source anchor** when
  (g(S,I_v)) is active.  Target anchors are defined symmetrically.
* A compatible pair ((S,T)) is **genuinely joint** when
  (S\ne I_u,T\ne I_v), while both (g(S,I_v)) and (g(I_u,T)) are
  inactive.

Every final activation is in exactly one of these two classes: if either
one-ended test succeeds it is generated from that literal; otherwise both
endpoints changed and the compatible pair is genuinely joint.

Let δ((S)) denote the signed resource change of a literal.  A primitive
support-three circuit consists of three nonzero deltas on distinct roots
whose sum is zero.  Thus:

* for a one-ended anchor δ, the remaining two delta classes satisfy
  α+γ(=-\delta);
* for a genuinely joint pair ((\delta_1,\delta_2)), the third class is
  forced to be (-\delta_1-\delta_2).

No additional primitivity test is needed: three nonzero deltas summing to
zero cannot contain a zero-sum proper pair, because that would force the
third delta to be zero.

## 5. Signed-coordinate inverted join

Each literal delta has at most six nonzero coordinates, all in
\(\{-1,+1\}\). Store the 2,033,054 nonzero delta classes in a hash table
and, for each signed resource coordinate \((j,\varepsilon)\), store the
inverted list

\[
 \mathcal I_{j,\varepsilon}=\{D:D_j=\varepsilon\}.         \tag{5.1}
\]

### Lemma 5.1 (complete one-anchor join)

Fix a nonzero target \(\tau\). Choose
\(j\in\operatorname{supp}\tau\) minimizing
\(\lvert\mathcal I_{j,\operatorname{sgn}\tau_j}\rvert\). Enumerate
\(D\in\mathcal I_{j,\operatorname{sgn}\tau_j}\), form
\(E=\tau-D\), reject if \(E\) is not a nonzero
\(\{-1,0,+1\}\)-vector of support at most six, and look up \(E\) in the
class table. This returns every unordered pair \(D+E=\tau\).

#### Proof

At coordinate \(j\), the equality \(D_j+E_j=\tau_j\ne0\), with
\(D_j,E_j\in\{-1,0,+1\}\), forces at least one of \(D_j,E_j\) to have
sign \(\operatorname{sgn}\tau_j\). Therefore at least one member of every
valid pair lies in the chosen inverted list. Sparse subtraction and the
exact hash lookup are both necessary and sufficient. When only one member
lies in the list it emits the pair once; when both do, order their class IDs
to remove the duplicate. □

For one-ended anchors use \(\tau=-\delta\). For genuinely joint anchors no
inverted scan is needed: merge the two sparse deltas and make one exact class
lookup. Literal records in the returned classes are expanded only after the
class-level join; equal-root records and repeated roots are rejected.

Together, Theorem 2.1, Lemma 3.1, the exhaustive one/joint split, and Lemma
5.1 prove that this generator contains **every** primitive support-three
circuit which improves the common matching.  It does not assume that the
circuit factors through an opposite-delta intermediate table.

## 6. Authenticated census and finite size

The exact census on the frozen table gives

```text
crossing dormant states                 2718
  in0/out+                              2198
  in+/out0                                90
  both0                                  430
missing-in state/geometry relations    21024
missing-out state/geometry relations   33280
deduplicated critical geometries       30885
  via incoming                         21024
  via outgoing                         12560
  via both                              2699
one-ended source marks                362779
one-ended target marks                176628
distinct one-ended literal anchors    393630
distinct one-ended delta texts        348056
  nonzero primitive classes           348055
raw joint compatible option pairs  424606980
```

The raw joint number is exactly (30885\cdot13748); one-ended and incumbent
tests remove many of these before the forced-third lookup.  A compact index
needs at most six 32-bit postings per nonzero class, hence at most

\[
 6\cdot 2033054=12198324
\]

postings (under 49 MB before vector headers).  The realized index has
11,065,570 postings.  Literal records, class ranges,
menus, geometries, and hash overhead fit safely below an 8 GB capped H100
process.

## 7. Canonical deduplication and the complete search

The complete generator uses two disjoint canonical rules.

1. If a triple contains a one-ended anchor literal, it is assigned to the
   least global option ID among its one-ended literals.  Lemma 5.1 emits its
   remaining unordered delta-class pair once.  The literal record pair is
   ordered only when both records lie in the same class.
2. If a triple has no one-ended anchor literal, it is assigned to the least
   critical geometry which is active under its three final options.  It is
   generated by the genuinely joint source/target parametrization and the
   forced-third class lookup.

Thus a triple occurs in exactly one branch and one of the sixteen shards.
The two rules are complete by Theorem 2.1 and the one-ended/genuinely-joint
dichotomy in Section 4.

For every canonical triple the search recomputes all geometries incident
with its three roots, exact incoming/outgoing counts of every affected phase
state, and exact common-edge multiplicities.  It first applies the necessary
old-cut test--the new neighbourhood of the fixed 309-root shore must have
size at least 21--and then runs a fresh Hopcroft--Karp matching and derives
the final alternating Hall shore.  Additive score deltas are never used.

### Theorem 7.1 (exact primitive support-three ceiling at `2e919...`)

Among all resource-exact primitive support-three changes of the frozen table
(F),

\[
 \max_C \nu(G_{F+C})=1142.                                  \tag{7.1}
\]

Exactly 409 canonical triples improve the common matching, and every one has
matching 1142.  All 409 lie in the one-ended branch.  The genuinely joint
branch contains no matching gain.

The exact ledger is

| branch | canonical resource triples | old-cut escapes | matching gains | maximum |
|---|---:|---:|---:|---:|
| one-ended | 6,032,478 | 1,811,376 | 409 | 1142 |
| genuinely joint | 8,953 | 2,373 | 0 | 1141 |

#### Proof

Theorem 2.1 assigns every improving primitive triple an inactive critical
geometry.  Sections 3--5 generate every final option assignment and every
resource completion at such a geometry.  The canonical rules above neither
delete a triple nor assign it twice.  The 32 shard audits cover residues
0 through 15 in each branch.  Every one of their resource exits is zero;
their exact counts sum to the displayed ledger.  The independent aggregate
auditor verifies all shard identities, checks all 409 emitted three-row
resource ledgers coordinatewise, proves the 409 option triples pairwise
distinct, and checks |X'|-|Y'|=1430-ν on every hit.  The displayed
maximum is therefore exhaustive over the stated primitive support-three
class. □

## 8. A literal winner and comparison with the commutator shell

One authenticated winner changes roots 216, 558, and 1348:

```text
root  216  option  413152  delta -959,960
root  558  option 1062575  delta 1,-9,959,-1191,-2014
root 1348  option 2568479  delta -1,9,-960,1191,2014
```

Its final table has SHA

```text
e6ff887bd9ebc151669045b05760d6126b7248732ed39b9cdf688581ed6a0888.
```

Independent literal replay gives

```text
common matching          1141 -> 1142
canonical Hall shore      309 -> 20  to  308 -> 20
old-shore neighbourhood    20 -> 23
gained outside old head          3
lost inside old head             0
live attachment states    1928 -> 1934
```

This physical table is different from the factorable shell's lexicographic
winner `4f5fb7f2...`, whose roots are 81, 437, and 1380.  The direct winner
is itself factorable through an overlapping-support-two intermediate and is
present in the factorable commutator catalogue (shard 3):
the complete direct search strictly broadens the quantified shell but does
not produce a larger matching gain than the factorable search.

## 9. Artifacts and exact boundary

```text
scratch/threadA_k17_2e919_anchor_index_census_20260801.cpp
  a58f3590964510310014951a67967f9d40c615189091db2994920e233e128d20

scratch/threadA_k17_2e919_anchor_index_census_20260801.audit.json
  8c9c68a324844a72eaf58db7d66e03aed420b0ccc5cccac44cdcdb45bfc87924

scratch/threadA_k17_2e919_anchor_index_projection_20260801.cpp
  97a5525f64491b9c195a3784b99a1716b0509ae2e7df00875114b254ca3d45b6

scratch/threadA_k17_2e919_anchor_index_search_20260801.cpp
  733a109cd75132f8bafa2a03b3b8863e1dc014a785549eeaa25b40f33d0e6644

scratch/audit_threadA_k17_2e919_anchor_index_shards_20260801.py
  2b1c66d8315d5ac191ebd7d9b11d87cb7231d0fe3534ea806866ee89572eb5ae

scratch/threadA_k17_2e919_anchor_index_search_20260801.independent.audit.json
  90500b62f73c07e8f7085817108e5aec4421d188920f5a88abc1aa0cc27c3018

scratch/threadA_k17_2e919_anchor_index_search_20260801/
  search_one_aggregate.audit.json
    f8075a5060a752894a1b1a1be0f46849129627483d5e1c9420cc8a59627f20fc
  search_joint_aggregate.audit.json
    7101faed699832f964f6ecadba2de59c4a8f17f967129e14d2a31a31588111bf
  search_one_00.best.steps.tsv
    13dcbe196c60c624944e1dfe0528cbf103804ff6f0fa45427a70310dad948bd7
  search_one_00.best.final_rows.tsv
    e6ff887bd9ebc151669045b05760d6126b7248732ed39b9cdf688581ed6a0888
  search_one_00.best.independent.audit.json
    d11710ea8d6ff7626faa7ed4d00433e20c61669581c59d8cfa7978560a58e61e
```

The census source is read-only, verifies the factor SHA, reconstructs every
state, geometry, liveness count, DM crossing, and literal option, and checks
the direct-pair identity (3.3).  Its peak resident memory was 96,256 KB and
its wall time was 0.87 s on one H100 CPU core.

The projection and search processes used at most 631,212 KB RSS each, under
a 1 GiB address-space cap.  The two manually timed shard-zero runs and all
30 parallel resource ledgers exited zero; all 32 shard JSONs independently
pass their mode, shard, source, and status checks.

What is proved is the complete primitive support-three matching ceiling at
this one source table.  The winner still has deficiency 288, so there is no
full common transversal and hence no quotient component profile.  No
chronology, topology, upper-shadow, residence, voltage, opening, or compiler
conclusion follows from this note.  Zero-delta sidecars, support at least
four, and serial moves from a new source table are outside Theorem 7.1.  In
particular, a decomposable unary-zero-delta plus binary circuit supported on
three roots can have nonlinear matching synergy, but it is not primitive in
the nonzero-delta sense used here and is not covered by the ceiling (7.1).
