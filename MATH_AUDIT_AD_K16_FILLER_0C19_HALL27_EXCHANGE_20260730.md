# AD audit: the 0c19 source-slot ears cost two Hall units

Date: 2026-07-30  
Status: **proved for the two frozen compiler graphs; the proposed second
return remains conditional on literal realization**

## 1. Frozen inputs and scope

This note compares the exact229 carrier with the unique nontrivial
upper-complete source-slot filler returned by the exhaustive filler census.
The authenticated inputs are

```text
dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d
  scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/best_upper_complete_bad2.targets
cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974
  scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
0c19e3c73616a4d771f29f8031aebd946131f4eeb20a571f59852458ec0f0760
  scratch/ad_k16_exact229_source_slot_filler_20260730/pass_1.targets
```

The exact229 operation deletes

\[
 A=[2186,2217),\qquad B=[1266,1295)
\]

from the source chronology and inserts (A+\operatorname{rev}(B)) before
old row 3846.  The 0c19 word additionally deletes

\[
 F=[6253,6263)
\]

and inserts \(\operatorname{rev}(F)\) in the source slot vacated by (A).
The audit reconstructs both words literally from the source before doing any
compiler calculation.

The claims below concern the exact generalized-COMP3 incidence graphs of
these two fixed words.  They do not assert that an abstract added incidence
can be realized by a legal word.

## 2. Canonical cell labels

Every compiler cell is labelled by the ordered tuple of original source-row
occurrences occupying its interval.  These labels are injective within each
of the two words.  This removes the chronology-dependent numeric cell-id
shift and makes, for example,

\[
 (6254,6255),\quad (6255,6254,6253),\quad (2217,2218,2219)
\]

literal right vertices common to the comparison whenever they occur.

Let (L) be all nonempty masks of rank below 8.  Thus

\[
 |L|=\sum_{j=1}^7\binom{16}{j}=26332.
\]

The independently rebuilt graphs have the following exact statistics.

| word | incidences | maximum matching | deficiency |
|---|---:|---:|---:|
| exact229 | 347875 | 26307 | 25 |
| 0c19 filler | 347799 | 26305 | 27 |

Their canonical alternating-reachability Hall shores have sizes (212/187)
and (212/185), respectively.  The shores overlap in 204 targets.  The
eight targets only in the exact229 shore are

```text
2e28 2e2a 2e68 2ea8 2f28 6cb0 6e28 ae28
```

and the eight only in the filler shore are

```text
22a9 2329 23a9 2aa8 2b29 a2a9 a329 aaa8.
```

This is a shore rotation, not merely the loss of two right vertices.  On the
old exact229 shore the filler has 189 rather than 187 neighbours (four new,
two lost), whereas on the new filler shore it has 185 rather than the 190
available in exact229.

## 3. Exact matching-exchange decomposition

Fix the deterministic chronology-cell-order Hopcroft--Karp maximum matching
in each graph, and canonically relabel its right vertices as above.  Their
matching symmetric difference has 76 components.  The balanced-component
histogram by number of edges is

```text
2:25, 4:12, 6:10, 8:11, 10:6, 12:3, 16:1.
```

There are five exact229-positive paths and three filler-positive paths.
Their imbalance is (5-3=2), exactly the observed matching loss.

The three positive filler components are:

1. the new edge `6cb0@(6255,6254,6253)`;
2. the new ear `2e28@(2217,2218)`, followed through the retained
   `(4049,4050,4051)` cell;
3. the new ear `2f28@(2217,2218,2219)`, replacing
   `2c0c@(2217,2218,2219)` and continuing through retained cells 2428 and
   2811.

For the five negative paths, the following table gives precisely the
exact229-only matching incidences missing from the filler graph.  Adding the
whole bundle in one row completes the displayed alternating augmenting path
and gains one matching unit.

| path | missing incidence bundle | bundle size |
|---:|---|---:|
| 1 | `2aa8@(6254,6255)` | 1 |
| 2 | `23a9@(6263,6264,6265)`, `2ba8@(6253,6254,6255)` | 2 |
| 3 | `6c30@(6256,6257,6258)` | 1 |
| 4 | `22a9@(6263,6264)`, `0ba8@(6253,6254)` | 2 |
| 5 | `2329@(6264,6265)` | 1 |

The retained part of path 1 is

```text
aaa8 -- (10306,10307) -- 2aa8.
```

The retained part of path 3 is

```text
ec30 -- (6720,6721) -- 6c30.
```

Path 5 is the longer retained chain

```text
2b29 -- (6264,6265,6266) -- 2329
     -- (6264,6265)      -- 2b28
     -- (1017,1018)      -- 0328
     -- (824,825)        -- 1b28
     -- (458,459)        -- 1b20
     -- (825)            -- 1320
     -- (219)            -- 2320
     -- (2138,2139)      -- 6320
     -- (3653).
```

Here every unlabeled alternating edge in the displayed chains is present in
the filler graph.  The replay JSON records every edge of all eight unbalanced
paths and whether it belongs to one or both incidence graphs.

### Theorem 3.1 (minimum abstract recovery)

Let (G_F) be the fixed filler incidence graph and (M_F) the fixed matching
above.

1. Adding any two of
   `2aa8@(6254,6255)`, `6c30@(6256,6257,6258)`, and
   `2329@(6264,6265)` raises the matching from 26305 to 26307.  Two added
   incidences are necessary for that matching size.
2. Adding all three raises the matching to 26308, hence reduces deficiency to
   24.  Three added incidences are necessary to reach deficiency at most 24.
3. Adding all seven incidences in the five bundles raises the matching to at
   least 26310, hence reduces deficiency to at most 22.

Moreover, if additions are restricted to those seven exact229-only matching
incidences, the three singleton incidences are the **unique** subset of size
at most three that reaches deficiency at most 24.

#### Proof

The five paths are vertex-disjoint alternating paths relative to (M_F).
Completing a bundle therefore augments (M_F) by one, independently across
paths.  A single added incidence can increase a maximum matching by at most
one, proving the cardinality lower bounds.  The audit also directly reruns
Hopcroft--Karp after every subset of at most three of the seven candidate
edges (64 subsets total); only the stated singleton triple gains three.  It
then reruns the two-edge, three-edge, and seven-edge augmentations and obtains
26307, 26308, and 26310.  ∎

The uniqueness clause is deliberately scoped to the seven old matching
incidences.  A novel free cell adjacent directly to an unmatched left root
can repair a component with one edge.  The five unmatched roots of the loss
paths are

```text
aaa8 23a9 ec30 a2a9 2b29.
```

Connecting any three of these roots to three distinct new (M_F)-free right
cells gives three immediate vertex-disjoint augmentations.

## 4. Literal cell conflicts and the correct second-return target

The advertised source-slot ears are

```text
2e28@(2217,2218)
2f28@(2217,2218,2219).
```

They use distinct right cells from all three singleton repairs, so there is
no matching-capacity conflict.  The filler matching also contains the useful
reverse-F incidence

```text
6cb0@(6255,6254,6253).
```

That incidence creates a literal ordered-token obstruction.  The old
`2aa8@(6254,6255)` cell asks for the directed adjacency
(6254\mathbin\to6255), opposite to the adjacency
(6255\mathbin\to6254) inside the reverse-F cell.  Because every original
row occurrence appears once, both ordered intervals cannot occur in one
chronology.  The same obstruction affects the paired old cells

```text
2ba8@(6253,6254,6255)
0ba8@(6253,6254),
```

which oppose (6254\mathbin\to6253) in the reverse-F cell.

This proves the following exact boundary.

### Corollary 4.1 (minimum compatible blueprint)

Suppose a second-return macro retains the complete filler incidence graph
used by the three augmenting paths and, in particular, retains the two
advertised ears and `6cb0@(6255,6254,6253)`.  A cardinality-three Hall repair
cannot consist solely of the old canonical cell restorations.  A sufficient
cardinality-three blueprint is:

1. restore `6c30@(6256,6257,6258)`;
2. restore `2329@(6264,6265)`;
3. create a genuinely new (M_F)-free cell hosting `aaa8` directly, or a
   genuinely new (M_F)-free cell hosting `2aa8` while retaining the common
   chain through `(10306,10307)`.

The three new/free endpoints are matching-disjoint.  If they are realized
without losing the retained path incidences, the resulting graph has
deficiency at most 24.

The word “new” in item 3 is essential: under retention of the reverse-F cell,
it cannot be the old canonical `(6254,6255)` cell.  One may instead target a
new free provider for any one of the other unmatched roots `23a9`, `a2a9`,
or `2b29`, provided the other two augmentations remain disjoint.

This is a necessary-and-sufficient **graph target within the stated retained
matching/path scope**, not a literal second-filler construction.  A legal
macro must still pass exact middle replay, unrestricted upper coverage,
maximal-envelope nonzeroness, and all compiler-cell tests.  In particular,
the profile at `(6264,6265)` is changed by the deleted-F source gap even
though those two rows remain adjacent, so item 2 is a source-gap collar
repair rather than mere adjacency restoration.

## 5. Reproducibility

The solver-free replay is

```text
scratch/audit_ad_k16_filler_0c19_hall_exchange_20260730.py
```

and writes

```text
scratch/ad_k16_exact229_source_slot_filler_20260730/
  pass_1_vs_exact229.exchange.audit.json
```

The JSON status is

```text
PASS_EXACT_FIXED_GRAPH_EXCHANGE_AUDIT
```

with payload hash

```text
b40d3e4fb28b46c07926e21430bdfbe99e1e22aaba393413ada3f49829fc3e24
```

No SAT, exhaustive chronology search, or heavy local process is used by this
replay.  It reconstructs the two fixed graphs, computes two maximum
matchings, checks their canonical shores, checks every unbalanced exchange
component, and verifies the conditional correction matchings.
