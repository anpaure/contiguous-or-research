# The k=17 SCD compact-socket bank and its exact upper-casualty ledger

## Scope

This note records a finite, literal construction inside the authenticated
`m=9` SCD phase forest. It is a theorem about one protected socket bank and
the path forest obtained after installing that bank. It is **not** a
universal word, a completed upper-deck braid, a lower compiler, or a proof
that `nu(17)=B(17)`.

The starting forest contains all `W=24310` rank-nine owners. Minimum
positive-residence fragmentation uses `1419` cuts and gives `6281` pieces.
The exact all-minimum-cut atlas has `8894` component patterns, `12672`
distinct segments, `25344` oriented segment states, and `554218`
pairwise-extendable rank-ten seam arcs.

## 1. The compact socket used here

For a rank-ten set `U`, choose three distinct facets

```
U-{v0}, U-{v1}, U-{v2}.
```

Together with an oriented left and right guard segment, the literal
positive-run automaton checks the concatenation

```
left guard, U-{v0}, U-{v1}, U-{v2}, right guard.
```

The two internal facet joins both have union `U`. Consecutive facets that
already occur as one consistently oriented run in an old component are
extracted as one chunk; the construction does not insert a spurious cut
between them. Every remaining extraction boundary becomes a named
rank-ten child demand. A child equal to `U` is already supplied by the
socket and is not recursively charged.

This is the `h=3,L=3` specialization of the resident facet-socket algebra in
`MATH_THEOREM_RESIDENT_FACET_SOCKET_20260801.md`.

## 2. Exact simultaneous static bank

Start from the endpoint-degree all-minimum-cut master with 29 omitted
rank-ten colours. Individual compact sockets close those 29 colours except
for one new unsupported child, `97508`; a thirtieth compact socket closes
that child.

After replacing five initially colliding guard choices, the resulting bank
has the following exact properties.

* `30` socket macros;
* `90` pairwise distinct facet owners;
* `60` guard segments whose final half-open physical intervals are pairwise
  disjoint;
* no guard contains a facet extracted by another socket;
* every guard is exposed exactly after applying the common component option
  and the bank's extra cuts;
* all component-option requirements are mutually compatible;
* `81` genuinely extra cut boundaries, versus `112` raw extraction
  boundaries before crediting minimum-residence cuts;
* `3` parent-equal children, hence self-served;
* `77` children with an existing extendable one-seam provider;
* one nontrivial child, `97508`, which is the parent of the thirtieth socket;
  after that socket the child cascade is empty.

Here “existing extendable provider” is a statement in the prebank segment
atlas used by the static packing audit.  It is **not** a statement that the
provider remains an exposed endpoint seam after all guards and facet chunks
are consumed.  The later exact postbank endpoint audit finds seven raw
rank-ten zero rows; bank child `69555` is one of them.  Thus the static
socket-generation cascade is closed, while the physical final-piece child
selector is not.  This distinction is the correlated provider gate recorded
in
`MATH_THEOREM_THREAD_D_K17_SOCKET30_POSTBANK_GLOBAL_SELECTOR_AND_LOWER_CUT_20260801.md`.

The bank fixes compatible options on `102` components. Relative to the
particular frozen endpoint-degree model, `63` component options change.
Thus the bank must be integrated into the pattern/seam master; it cannot be
bolted onto that frozen model without re-solving its arc choices.

The primary audit and an independent replay both pass. The independent
replay checks facet identity, extraction chunks, option compatibility,
guard orientation, residence, Johnson joins, child colours, guard--guard
overlap, guard--facet overlap, and final cut exposure.

## 3. Exact physical piece ledger

Apply the bank's compatible component options and `81` extra cuts.

* the raw fragmentation has `6362=6281+81` pieces;
* the 90 selected facets occupy `80` extracted chunks;
* the 30 guard--socket--guard paths replace those chunks and consume 60
  distinct guards;
* the final authenticated path forest has exactly `6252` pieces;
* it contains all `24310` rank-nine owners exactly once;
* every final piece has no internal positive coordinate run shorter than
  four.

This is a literal owner chronology ledger, not only a count.

## 4. All-rank upper-deck comparison

The following table compares the internal interval-OR deck of the frozen
endpoint-degree `6281`-piece forest with the internal deck after installing
the 30 authenticated guard--socket--guard paths. `newly lost` and `newly
gained` are literal mask counts.

| rank | base missing | bank missing | newly lost | newly gained |
|---:|---:|---:|---:|---:|
| 10 | 1419 | 1458 | 127 | 88 |
| 11 | 2398 | 2429 | 97 | 66 |
| 12 | 1576 | 1583 | 49 | 42 |
| 13 | 549 | 549 | 21 | 21 |
| 14 | 102 | 101 | 7 | 8 |
| 15 | 11 | 10 | 0 | 1 |
| 16 | 0 | 0 | 0 | 0 |
| 17 | 0 | 0 | 0 | 0 |

The full mask-level ledger is retained. The socket bank therefore repairs
its rank-ten support frontier at modest physical cost, but it does not make
the arbitrary-width upper deck automatic. In particular, the remaining
`10` rank-fifteen and `101` rank-fourteen misses, as well as the lower-rank
upper misses, must be supplied by the still-unselected inter-piece seams or
by longer hyperarcs.

## 5. Consequence and exact remaining gate

The bank uses only `81` of the `1120` lower-slack units left after minimum
residence fragmentation, and the number of path pieces actually decreases
from `6281` to `6252`. Hence the former 29-colour endpoint-degree residual
is not a scalar or local-residence obstruction.

The final pieces are not lower-injective: their internal rank-eight palette
has 53 repeat units.  This was outside the static-bank theorem and is now an
exact fixed-piece obstruction in the postbank selector note cited above.

What remains is correlated:

1. select a global directed path/forest on the `6252` pieces, respecting the
   bank's component options and guard orientations;
2. cover every remaining rank-ten through rank-fifteen target by a selected
   seam or constant-length hyperarc;
3. retain the exact positive-run state through all selected seams;
4. compile the strict lower ideal with the resulting physical chronology.

No statement in this note asserts any of those four rows.

## Artifacts

* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_v5_20260801.tsv`
  SHA `14e444919ef4daf6aeee1639cbe1632299193cbd8a40838c0cb652d123018697`.
* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_v5_20260801.audit.json`
  SHA `19ab65a1a0e946486a81ca0ccc8dd46e1a06187b1b977e414461090e30195c07`.
* `scratch/k17_combined30_socket_bank_v5_independent_20260801.audit.json`
  SHA `d77531b5ad73e3631b2df739febc725635ccd96656710c4de8df587d8cba6aa7`.
* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_v5_20260801.tsv.options.tsv`
  SHA `803b940be38c182ff43c5c2c022994367a5eb21d1cce8f9e0c7c597674aac43f`.
* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_upper_casualties_20260801.audit.json`
  SHA `2cdfc7aa7c275f70332d0ed3b7a77077d241ffefbf29c73f20b74c1b859cfc30`.
* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_upper_targets_20260801.tsv`
  SHA `ca387b7095fc7b7c2d57badd70048b690648093f2a5f86b2d085337d018dbd2e`.
* `scratch/k17_m9_endpoint_degree_combined30_socket_bank_final_pieces_20260801.tsv`
  SHA `2265998c234db97208c957c84ded3fe73b57192bef657ab0c26670c832175504`.
* `scratch/audit_k17_m9_compact_socket_bank_20260801.cpp`
  SHA `92319cac9e89130ee6e1242c2ef0816c57deadd5c261925673ffcbe71135d49c`.
* `scratch/audit_k17_m9_socket_bank_upper_casualties_20260801.cpp`
  SHA `dad6bf0ac9e9b500eade365968f0653a261fcf6e2e55555dc64af226ad59c19f`.
