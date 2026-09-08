# Thread D: exact229 shifted-eight `0200` support-three engine gate

Date: 2026-07-30.  Exact local audit and engine contract; no large search.

## 1. Frozen inputs

The exact Hall parent is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.targets
SHA-256 cae23cfcedbc9d193ebd9191045edd0e5c14f56af5fc96a802b8cefa7cd7e974.
```

Its generalized compiler graph has matching `26307/26332`, canonical Hall
shore `212/187`, and deficiency 25.  The matching audit used below is

```text
scratch/k16_splitpair_hall_basis_20260730/exact229.hall.audit.json
SHA-256 85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0.
```

The shifted-eight near chronology is

```text
scratch/k16_exact229_shifted8_natural_near_20260730.targets
SHA-256 e8c720ef977b5f561c32d84c7c4a51e710999eab80d88bf814aa1f855b254f06.
```

It has the same three flats `6320,12869,12871`, capacity 32063, no zero
envelope and no arbitrary-upper hole.  It has exactly one middle-replay
failure:

```text
row       3845
target    6ba8
envelopes 6888,6828,6920,6120
OR        69a8
missing   0200.
```

The authenticated donor and Hall-component sources are

```text
exact_229.hall_components.k.audit.json
  SHA f3532a10f89422bbadc4fb981b490dd9d13a77cfdfa0604b66e63fd9d31ad25d

exact_229.paired_halo_seam_donor.audit.json
  SHA 87128dc4dbde011d5d20b928d020a27d596a52162da063a4f83ef0d41c23f152.
```

## 2. Exact protected physical cells

Cell IDs are zero based and enumerate `(start,length)` by increasing start,
then increasing length.  Because the flat schedule is fixed, the two physical
keys below have the same dense IDs in the exact229 and shifted-eight rows.

For a cell `c=[s,s+l)`, write

```text
profile(c) = (Mandatory(c); E_s,...,E_(s+l-1)),
Allowed(c) = OR(E_s,...,E_(s+l-1)).
```

The exact229 profiles and complete lower candidate sets are

| cell | physical key | ordered envelopes | allowed | mandatory | all candidates |
|---:|---|---|---:|---:|---|
| 13964 | `(4654,3)` | `6021,4821,0829` | `6829` | `6809` | `6809,6829` |
| 13966 | `(4655,2)` | `4821,0829` | `4829` | `4809` | `4809,4829` |

Both right vertices are unmatched in the frozen exact229 maximum matching and
neither is in the old `187`-cell Hall neighbourhood.

The shifted-eight desired halo changes precisely these profiles to

| cell | ordered envelopes | allowed | mandatory | all candidates |
|---:|---|---:|---:|---|
| 13964 | `6221,4a21,0a29` | `6a29` | `6809` | `6809,6829,6a09,6a29` |
| 13966 | `4a21,0a29` | `4a29` | `4809` | `4809,4829,4a09,4a29` |

Thus the halo is literally incidence-monotone on the two columns: each
envelope letter gains `0200`, while both mandatory masks stay fixed.  The two
new Hall-shore incidences are `6a29--13964` and `4a29--13966`.

For completeness, the matching continuation cell is

```text
cell 18077 = (start6025,length3)
envelopes  = 5828,5029,5221
allowed    = 5a29
mandatory  = 4a09
candidates = 4a09,4a29,5a09,5a29.
```

It is matched to `4a29`; `5a29` and `6a29` are unmatched left vertices.
Consequently the two explicit disjoint augmenting paths are

```text
6a29 -- cell13964,
5a29 -- cell18077 --[M] 4a29 -- cell13966.                 (2.1)
```

If every old matching edge is retained, (2.1) proves `26307 -> 26309`, hence
deficiency `25 -> 23`.

## 3. Candidate predicate to implement

For any proposed final chronology, a lower target `S` is adjacent to a cell
with ordered envelope letters `E_0,...,E_(l-1)`, allowed mask `A`, and
mandatory mask `M` if and only if

```text
M subset S subset A,
S & E_j != 0 for every j,                                  (3.1)
1 <= rank(S) <= 7.
```

The engine must use (3.1), not only `(A,M)`.  For this objective the exact
fail-closed predicates are:

1. reconstruct the final flat/depth schedule and physical cell numbering;
2. require cell 13964 to remain key `(4654,3)` and cell 13966 key `(4655,2)`;
3. recompute the ordered envelopes and mandatory masks literally;
4. require the two desired profiles in the second table exactly;
5. check (3.1) for all four old incidences and the two advertised new shore
   incidences;
6. retain the frozen matching edge `4a29--cell18077` and verify that 13964 and
   13966 remain unused by the transported old matching;
7. for a global `25->23` claim, replay all 26,307 transported matching edges,
   not merely the three cells displayed here.

Items 2--4 are stronger and simpler than a candidate-only test.  If an engine
wants the weakest sufficient local test, it may instead demand (3.1) for
`6809,6829,6a29` at 13964 and `4809,4829,4a29` at 13966, together with the
matching conditions in items 6--7.

## 4. Exact `0200` repair condition

Let `Q'` be a proposed final target chronology and `E'_p` its maximal
envelopes.  Exact replay at the sole bad row is

```text
E'_3845 | E'_3846 | E'_3847 | E'_3848 = 0x6ba8.           (4.1)
```

For the shifted-eight input the left side is `69a8`, so a repair must put
`0200` into at least one of these four envelope letters.  Under the unchanged
depth-three schedule,

```text
E'_p = intersection(Q'_(p-3),Q'_(p-2),Q'_(p-1),Q'_p).     (4.2)
```

Rows 3843 and 3844 initially omit `0200`.  In an occurrence-preserving
support-three cycle, omitting position `J=3846` leaves only one external
`0200` token for those two zero rows and cannot create a carrier.  Hence `J`
is mandatory.  Write the rooted directed cycle as

```text
Q'_J = Q_s,  Q'_s = Q_t,  Q'_t = Q_J.                    (4.3)
```

Then `Q_s` must contain `0200`.  With only the two further edits, the only
available carrier is `E'_3848`, so the engine should test (4.1) literally
after enforcing this necessary donor-bit filter.  It must still replay every
affected row: importing `0200` at J alone does not guarantee the other
coordinates.

## 5. Complete connected support-three diagnostic

Use the distance-six interaction graph on the three support positions.  The
spatially connected class containing J consists exactly of triples whose two
successive sorted gaps are at most six.  There are

```text
108 unordered supports,
216 directed orientations,
178 rooted rows after the Q_s & 0200 != 0 filter.           (5.1)
```

A direct exact replay of these 178 rows gives:

```text
flat fingerprint unchanged                      178
zero-envelope failures                           19
nonzero-envelope middle-replay failures         159
exact-middle survivors                            0.       (5.2)
```

Thus the genuinely connected support-three class is closed before upper
coverage and Hall.  This is a structural no-go for (4.3) with the declared
distance-six connected support.  It does not close the one-close-edge plus
remote-return class, support at least four, a block rethread, or a chronology
that first changes the shifted-eight macro itself.

## 6. Engine integration contract

The safe gate order is

```text
occurrence permutation
-> exactly three legal flats / valid depth schedule
-> nonzero envelopes
-> all middle rows exact, including (4.1)
-> exact ordered profiles at 13964 and 13966
-> arbitrary-width upper holes zero
-> transport all old matching edges
-> install the two augmenting paths (2.1)
-> full generalized Hall replay.
```

The current connected support-three engine should terminate at (5.2).  The
profile and matching clauses remain the correct interface for the next remote
or higher-support engine; they must not be weakened to the scalar presence of
`0200` or to allowed-mask containment.

