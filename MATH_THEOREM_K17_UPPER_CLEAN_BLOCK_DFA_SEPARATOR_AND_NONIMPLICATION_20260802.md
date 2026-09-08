# K17 upper clean-block equivalence, target-local separator, and rank nonimplication

Date: 2026-08-02  
Status: exact theorem, authenticated floor-1751 audit, and explicit Johnson-walk
countermodels.  No solver was launched.  This note does not assert a resident
K17 factor, a compiler, or `nu(17)=24313`.

## 0. Outcome

For every physical upper target `Z` of rank `s=10,...,16`, coverage by a
degree-two rank-nine factor has an exact clean-block characterization.  If an
incumbent misses `Z`, retaining its selected optional edge orbits incident to
the `Z`-clean physical owners freezes every clean block.  This gives the
sound target-local clause

\[
             \boxed{\ \bigvee_{e\in S_Z(F)}\neg x_e\ },          \tag{0.1}
\]

of width at most `min(1198,2 binom(s,9))`.  The clause contains no auxiliary
state variables.  If `S_Z(F)` is empty, the empty clause is a correct scoped
UNSAT certificate: fixed edges already freeze every clean block.

For rank thirteen the exact minimal linear target DFA has 1,094 states.  The
authenticated floor-1751 factor has one missing rank-thirteen orbit; every
translate has 715 clean owners in 377 clean blocks, and (0.1) has exact width
749, versus the global worst-case width 1,198.

There is no monotone theorem saying that rank-13 coverage alone forces rank
14, nor analogous implications `14->15` or `15->16`, even for cyclic Johnson
walks of rank-nine owners.  Explicit audited walks cover every target at the
lower rank while missing a prescribed target at the next rank.  These walks
repeat owners, so they do not rule out a stronger theorem using the exact
owner-once/facet/residence hypotheses.  Rank 17 is automatic once the whole
rank-nine carrier is placed in one linear chronology, since the union of the
whole chronology is `[17]`.

## 1. Clean-block equivalence

Let `F` be a physical degree-two factor on rank-nine owners of `[17]`, and
fix an `s`-set `Z`, `10<=s<=16`.  Call an owner `u` **clean** when `u subset Z`.
For a clean owner put

\[
                     H_Z(u)=Z\setminus u,\qquad |H_Z(u)|=s-9.    \tag{1.1}
\]

Delete all dirty owners from `F`.  The remaining components, called clean
blocks, are paths and cycles.

### Theorem 1.1 (clean-block equivalence)

The target `Z` is a union of a contiguous owner interval if and only if some
clean block `B` satisfies

\[
             \bigcup_{u\in B}u=Z,                               \tag{1.2}
\]

or equivalently

\[
             \bigcap_{u\in B}H_Z(u)=\varnothing.                \tag{1.3}
\]

If `Z` is missing, one may certify every clean block by one persistent hole

\[
             h_B\in\bigcap_{u\in B}H_Z(u).                      \tag{1.4}
\]

#### Proof

An interval with union `Z` contains no owner having a coordinate outside
`Z`, so it lies in one clean block.  Its union is contained in the union of
that block.  Conversely, a clean path block is itself a contiguous interval,
and a clean cycle block may be traversed once; if its total union is `Z`, it
is a witness.  Identity (1.3) is De Morgan's law inside `Z`.  If `Z` is
missing, every intersection in (1.3) is nonempty and supplies (1.4). `QED`

The statement is orientation-free.  It applies to a cycle cover as well as
to one physical Hamilton cycle.

## 2. The exact target DFA and the rank-thirteen specialization

Put `q=s-9`.  A left-to-right linear scan uses states

\[
 \{\bot,\checkmark\}\ \cup\
 \{J:\varnothing\ne J\subseteq Z,\ |J|\le q\}.                 \tag{2.1}
\]

Here `bottom` is the dirty/reset state, `checkmark` is accepting, and `J` is
the intersection of the holes seen in the current clean run.  On owner `u`:

* `u not subset Z` sends every nonaccepting state to `bottom`;
* from `bottom`, a clean owner sends to `Z-u`;
* from `J`, a clean owner sends to `J intersect (Z-u)`, with the empty set
  interpreted as `checkmark`;
* `checkmark` is absorbing.

The clean-block invariant proves exactness immediately.

### Theorem 2.1 (minimal state count)

The complete deterministic linear automaton above is minimal and has

\[
                    N_s=2+\sum_{i=1}^{s-9}\binom{s}{i}           \tag{2.2}
\]

states.

#### Proof

Every nonempty `J` with `|J|<=q` is reachable: it is the intersection of two
`q`-subsets of `Z` because `q<=7` and `s=9+q`.  The reset state is initial,
and two disjoint `q`-holes reach the accepting state.

For distinct nonempty `J_1,J_2`, after swapping their names if necessary,
choose `a in J_1-J_2`.  A `q`-set `K` containing `a` and disjoint from `J_2`
exists, since at least eight further coordinates are available.  Reading the
clean owner `Z-K` accepts from `J_2` but not from `J_1`.  A `q`-hole disjoint
from `J` distinguishes `J` from reset: it accepts from `J` and merely enters
that hole from reset.  Acceptance distinguishes `checkmark` from all other
states.  Myhill--Nerode minimality follows. `QED`

The exact K17 counts are:

| target rank `s` | hole size `q` | DFA states | clean owners | clause-width bound |
|---:|---:|---:|---:|---:|
| 10 | 1 | 12 | 10 | 20 |
| 11 | 2 | 68 | 55 | 110 |
| 12 | 3 | 300 | 220 | 440 |
| 13 | 4 | **1,094** | 715 | 1,198 |
| 14 | 5 | 3,474 | 2,002 | 1,198 |
| 15 | 6 | 9,950 | 5,005 | 1,198 |
| 16 | 7 | 26,334 | 11,440 | 1,198 |

For a cyclic component one either cuts after a dirty owner or checks the
clean component directly by Theorem 1.1.  A representative-only quotient
DFA is not exact without a phase coordinate; see Section 4.

## 3. The canonical target-local factor separator

Work on the authenticated marker-58 face.  It has 232 fixed quotient edge
orbits and chooses exactly 1,198 optional quotient edge orbits, with primary
variables `x_e`.  Let `F` be an incumbent physical degree-two factor missing
`Z`.  Define

\[
 S_Z(F)=\{e:\ x_e(F)=1\text{ and some developed edge of orbit }e
                     \text{ is incident with a clean owner}\}.  \tag{3.1}
\]

### Theorem 3.1 (persistent-hole separator)

Every factor on the same base which retains all edge orbits in `S_Z(F)` also
misses `Z`.  Therefore clause (0.1) is sound and incumbent-violated.

#### Proof

At every clean physical owner, both incumbent incident edges are either
fixed or belong to selected optional orbits in `S_Z(F)`.  Retaining those
orbits retains both incident edges.  Degree two then forbids every different
incident edge at that owner.  Hence all clean-clean edges, all clean-dirty
boundary edges, and therefore every maximal clean block are identical to
those of `F`.  Each block retains the persistent hole (1.4), so no block can
have union `Z`.  Theorem 1.1 finishes the proof. `QED`

There are at most 1,198 selected optional variables globally.  There are
`binom(s,9)` clean vertices and only two incumbent incidences at each, so

\[
                  |S_Z(F)|\le
                  \min\{1198,2\binom{s}{9}\}.           \tag{3.2}
\]

This is the exact rank-specific worst-case bound in the table.  If
`S_Z(F)=empty`, every edge incident with every clean vertex is fixed.  The
same proof shows that no assignment on this scoped base can cover `Z`, so
the correct learned row is the empty clause.

The support (3.1) is the canonical smallest **saturation certificate**: it
contains exactly the incumbent optional orbit variables needed to state that
all clean-owner incidences are retained.  It need not be a globally
minimum-cardinality logical separator; computing such a separator would be a
different cut-minimization problem.

### Proof-carrying clause contract

A lazy row exports:

1. factor/catalogue hashes and the physical target `Z`;
2. the sorted primary variables `S_Z(F)`;
3. every clean component and one persistent hole `h_B`;
4. for every clean owner, its two incumbent incident edges, each identified
   as fixed or as an orbit in `S_Z(F)`; and
5. the negative CNF row (0.1), or an explicit empty-row verdict.

The checker independently develops all 17 translations.  No orientation,
rank-12 state, or target-DFA variable is part of the clause.

## 4. Quotient/voltage caveat and the shared 8-bit oracle

Ranks 10 through 16 have free `Z_17` target orbits.  Fixing one target
representative does **not** make cleanliness representative-local.  If a
quotient owner representative is `u`, its occurrence at phase `g` is clean
exactly when

\[
                         \rho^g u\subseteq Z.                     \tag{4.1}
\]

For a directed quotient arc of voltage `delta`, phase changes by
`g -> g+delta`.  The hole is `Z-rho^g u`.  Thus a quotient DFA must carry
the 17-valued phase, or an equivalent rotated-target state.  Testing only
the stored representative endpoints is unsound.  Clause (0.1) avoids this
mistake by developing every selected orbit before collecting its support.

For decoding, all target DFAs can be replaced by one shared first-arrival
oracle.  Fix a physical rank-nine start owner `U` and traverse its oriented
factor component.  Maintain only

\[
                         A=(\text{union seen})\setminus U,         \tag{4.2}
\]

an 8-bit subset of `[17]-U`.  A Johnson step adds at most one previously
unseen outside coordinate.  When `|A|=h` is first reached, `U union A` is the
unique rank-`9+h` interval union first delivered from this start.  Continuing
for `h=1,...,8` simultaneously enumerates ranks 10 through 17.

On the quotient factor it suffices to start once at phase zero from each of
the 1,430 owner representatives and follow `(owner,phase)` until it repeats.
The exact worst-case work is

\[
                       1430\cdot(17\cdot1430)
                       =34,763,300                           \tag{4.3}
\]

constant-time 8-bit transitions.  Rotating the start gives rotated targets,
so this covers target orbits.  The decoder uses 256 possible coupon states
and one 190-bit result bank for ranks 13--17 (140, 40, 8, 1, 1 orbits).  It
does not create per-target SAT states and is therefore the smallest practical
shared lazy layer over the v3+rank11 master.

When the oracle reports a miss, Theorem 3.1 emits the factor-primary clause.
The current v3+rank11 frozen prefix contains union562; the canonical sound
residence bank has since moved to union604 (SHA
`b75afbc422877b46668811a67ec3e09e14cf688388580a15b245499732e9d6be`).
The upper separator is an
incremental semantic row and does not repair that moving-prefix gap by
itself.  No duplicate solver was launched here.

## 5. Authenticated floor-1751 result

The read-only H100 audit used:

```text
7b88292585cee9bb8e72a0017734f466f12aa7cb12c4507bec69b40484eb81f3
  marker58_residence_round1.map.tsv
a386d9dec73a0525cb949e77304fc34f2ef7748a824865c2510c28068cbbdb6a
  floor1751/factor.tsv
eb3190b675d1a366f9c7bc920aa3ac6ab3acec0bfe37dbe986d18f3d405b0552
  floor1751/deep.holes.tsv
```

It returned

```text
PASS_K17_UPPER_CLEAN_BLOCK_SEPARATOR_AUDIT
rank13_missing_physical=17 target_orbits=1
clean_owners_per_target=715 clean_components=377:377
canonical_clause_width=749
```

The source is

```text
036d9f248c83fee3d7236049d262a3ed0fde9cf2a4c4e7c3a309f54782ef360f
  scratch/audit_k17_upper_clean_block_separator_20260802.cpp
40806208434edb0f79e2462076d2d4c38074f603a091bcfe8b697da1a12e007a
  scratch/k17_upper_clean_block_separator_floor1751_20260802.audit.json
```

The floor-1751 factor exposed the union595 residence row and has one missing
rank-thirteen orbit.  The new 749-literal target clause is independent of
that residence row: it excludes every factor retaining the same clean-block
incidences, not merely the exact incumbent.

## 6. Rank `s` does not monotonically force rank `s+1`

### Theorem 6.1 (explicit Johnson-walk countermodel)

For each `s in {13,14,15}` there is a cyclic Johnson walk of rank-nine owners
which covers every rank-`s` target but misses a prescribed rank-`s+1` target.

#### Construction

Fix an `(s+1)`-set `Y` and a coordinate `z outside Y`.  For every `s`-set
`Z`, make a short block of rank-nine subsets of `Z` whose union is `Z`:
start with any nine-set `U_0 subset Z`, and successively swap out distinct
old elements while inserting the `s-9` elements of `Z-U_0`.  This is a
Johnson geodesic of `s-8` owners and has union `Z`.

If `Z` is not contained in `Y`, choose one coordinate of `Z-Y` and retain it
in every owner of the block.  Such a block is entirely dirty relative to
`Y`.  The only clean blocks are the `s+1` blocks for `Z subset Y`, and each
has union the proper subset `Z`.

Join consecutive blocks as follows.  Swap `z` into the endpoint, walk inside
the connected star of rank-nine owners containing `z` (isomorphic to
`J(16,8)`), and swap `z` out at the next clean endpoint when necessary.  All
connector interiors are dirty relative to `Y`.  Close the walk in the same
way.  Every `s`-target is the union of its explicit block, while any interval
of union `Y` would have to avoid every dirty owner and hence lie inside one
clean block, whose union is a proper subset.  Thus `Y` is missing. `QED`

The executable audit obtained:

```text
rank13_targets=2380 walk_owners=20897 clean_runs=14 missing_rank14_target=16383
rank14_targets=680  walk_owners=7221  clean_runs=15 missing_rank15_target=32767
rank15_targets=136  walk_owners=1693  clean_runs=16 missing_rank16_target=65535
PASS_UPPER_RANK_NONIMPLICATION_JOHNSON_WALK
```

with source

```text
74f4005a7ea02386c50026964c9dcdaa57a740aea804a161c3f82c81b9f14fe1
  scratch/audit_upper_rank_nonimplication_johnson_walk_20260802.cpp
```

The countermodels deliberately permit repeated owners.  They prove that
Johnson adjacency plus complete lower-rank coverage is not enough for a
monotone extension theorem.  A stronger implication exploiting owner-once
exactness, q1 exactness, residence, or the rank-11 summary remains logically
possible, but no such theorem is presently established.  Therefore ranks
14, 15, and 16 must still be decoded and separated explicitly.  Rank 17 is
automatic for a complete linear owner chronology and needs no independent
target clause.

## 7. Recommended integration

1. Keep v3 residence and the exact rank-11 summary unchanged.
2. Let P2 own rank 12; this note neither duplicates nor weakens that row.
3. Decode ranks 13--17 with the shared 8-bit first-arrival oracle.
4. For each missing orbit at ranks 13--16, emit (0.1) with the phase-developed
   certificate in Section 3.
5. If a support is empty, stop with scoped UNSAT.  Otherwise append only the
   negative primary row and re-solve the existing master.
6. Final acceptance still requires one-component/nonzero-voltage replay,
   literal residence, all upper ranks, source realization, and the compiler.

This integration adds no eager target-state variables and no duplicate
rank-12 machinery.  Its first authenticated rank-thirteen row has width 749.
