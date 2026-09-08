# K16 state2: complete standard O4 census and the zero-host obstruction

Date: 2026-07-30  
Lane: K  
Status: proved, independently replayed, sharply scoped

## 1. Statement

Let `T` be the authenticated length-12,873 rank-eight chronology

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464
```

It has forced flat starts `6432,12869,12871`, scalar capacity `32175`, exact
maximal-envelope reconstruction, and exactly two missing upper masks

```text
H0=0x4e79,  H1=0xc679.
```

Consider every fixed-endpoint standard four-cut rethread below the two
terminal flats.  Thus, for cuts

```text
0 <= a < b < c < d < 12869,
```

write

```text
T = A | B | C | D | E
```

and replace the three internal blocks by any signed permutation

```text
A | eps1 P_pi(1) | eps2 P_pi(2) | eps3 P_pi(3) | E,
```

where `pi in S3` and each `eps` independently chooses forward or reverse
orientation.  Patterns which restore an old cut edge are the already-audited
O2/O3 strata.

**Theorem.** No provenance-irreducible standard O4 rethread of `T` satisfies
all five conditions

1. `G=0`, with the two terminal flat pairs fixed;
2. scalar capacity at least `lambda=26332`;
3. nonempty maximal envelopes with exact reconstruction of every middle row;
4. complete coverage of every upper mask;
5. at least one fixed-chronology proper-prefix host for every nonempty lower
   mask of rank at most seven.

The full irreducible O4 atlas contains nineteen upper-complete exact-envelope
representations, but every one has a zero-host lower mask.  The minimum
zero-host count is one, attained by the already known `u0` chronology, whose
sole obstruction is `0x4c71`.  No zero-host-free chronology exists to emit.

This is an exact finite theorem about the standard fixed-endpoint O4 fibre. It
does not exclude five-cut rethreads, terminal-flat cuts, block fragmentation,
duplication/deletion, target-multiset changes, or unrelated chronologies.

The lower strata were frozen before this census.  The complete tail-fixed O2
scan has one hole-pinned descriptor and no exact carrier.  The genuine O3
scan has 299 descriptors, with filter ledger

```text
299 -> 278 G0 -> 267 capacity -> 4 exact envelopes -> 2 upper-complete.
```

Those two rows are

```text
u0 cuts [3278,6388,12826], capacity 29065, zero hosts {0x4c71};
u1 cuts [5725,6388,12826], capacity 31512, zero hosts {0x4879,0x4c39}.
```

Thus the result below completes the requested O3/O4 static-atlas audit rather
than assuming that either O3 row was a compiler candidate.

## 2. Canonical O4 patterns

Represent each exposed boundary port by

```text
(r,delta),  r in {0,1,2,3}, delta in {0,1},
```

meaning source position `c_r+delta`.  A signed permutation pairs the eight
ports into four new seams.  A seam joining `(r,0)` to `(r,1)` restores the old
cut edge at `c_r`, so that representation belongs to a lower cut stratum.

There are `3!*2^3=48` signed permutations.  Their restored-edge histogram is

```text
0 restored: 25
1 restored: 16
2 restored:  6
4 restored:  1.
```

Hence precisely 25 patterns are provenance-irreducible.  Their seam-variable
multigraph is 2-regular on the four cut variables.  It is either

- a simple four-cycle, for twenty patterns; or
- a doubled perfect matching, for five structural patterns.

This classification is purely symbolic and is unaffected by the numerical
cut positions.  Length-one blocks can make two descriptors produce the same
target order; the census keeps the provenance representations and the audit
also hashes the resulting orders.

## 3. Missing rank-nine masks pin seams

### Lemma 3.1 (rank-nine seam birth)

Let an order consist entirely of rank-eight sets, and let a rank-nine set `U`
be absent before a block rethread.  If `U` occurs afterwards as the OR of a
contiguous interval, some new seam joins two distinct rank-eight children of
`U`, and their union is exactly `U`.

### Proof

Every member of a `U`-witnessing interval is a rank-eight subset of `U`.
Moving along the interval, some adjacent pair must change value, since a
constant interval has rank-eight union.  Two distinct rank-eight subsets of a
rank-nine set have union `U`.  If that adjacency were internal to a transported
block, it existed before the rethread and would already witness `U`.  It is
therefore a new seam. `square`

The two holes `H0,H1` cannot use the same seam: their common rank-eight child
is `0x4679`, and it has only one source occurrence, whereas a seam has two
distinct source endpoints.  Thus they pin two distinct seam slots.

At occurrence level the directed child-port counts are

```text
H0: 88,   H1: 72.
```

After imposing both seam equations and requiring an increasing cut tuple,
the exact partial-descriptor census is

```text
free cuts      0       1      2
descriptors 26620    1852      6.
```

The one-free descriptors have 5,797,698 valid completions before exact
deduplication and the later filters.

## 4. Unique-rank-nine cut kernel

### Lemma 4.1 (unique adjacent witness replacement)

Suppose an old cut deletes an adjacent pair whose union is a rank-nine mask
`U`, and that pair is the unique adjacent `U`-pair in the source.  If the new
chronology is upper-complete, some realized new seam has endpoint union `U`.

### Proof

Any new interval witnessing `U` contains a change between distinct
rank-eight children of `U`, hence an adjacent pair with union `U`.  No internal
adjacency of a transported block can supply it: such an adjacency existed in
the source and would contradict uniqueness.  The supplying adjacency must be
a new seam. `square`

This lemma is an exact cut-kernel filter, not a Johnson heuristic.  Applying
it after `G=0` and capacity leaves

```text
class       domain       G0      capacity  unique-q1 kernel
free 0       26620      21425      20593          350
free 1     5797698    5351742    5145248        84005.
```

## 5. Proof-safe constant-depth interior filter

For constant deadline `h`, define on the source order

```text
E_h(p) = intersection(T[p-h],...,T[p]),
R_h(i) = OR(E_h(i),...,E_h(i+h)).
```

Inside a transported oriented block, every length-`h+1` intersection and
every radius-`h` replay equation is invariant under reversal.  Therefore, if
a source interval is placed wholly inside a constant-depth sector, then

```text
E_h(p) != empty,
R_h(i) = T_i
```

must hold at every position whose whole neighbourhood stays inside that
piece.  Prefix sums of the source violations give an O(1) exact range query.
Only equations crossing a block seam or a flat boundary are deferred to the
full maximal-envelope reconstruction.

This filter cannot reject a valid chronology.  Away from a deadline drop it
tests exact carrier equations transported bijectively from the candidate back
to the source.  Near a drop, a previous higher-depth row can contribute an
additional intersection constraint.  The actual envelope is then a subset of
the constant-`h` model envelope.  Consequently an empty constant-`h` window
remains empty, and a bit already missing from the constant-`h` replay cannot
reappear in the actual replay.  The rejection predicate is therefore
hereditary even in the boundary margin.  It leaves

```text
free 0:   128 representations,
free 1: 18910 representations,
```

or 19,038 distinct `(pattern,cuts)` descriptors after pin-assignment
deduplication.  They are not asserted to be distinct target orders.  Full
replay gives

```text
19,038  G0 + scalar-capacity confirmations
    23  exact nonempty maximal-envelope reconstructions
    19  arbitrary-upper-complete chronologies.
```

## 6. Closing the two-free channels

The five doubled-matching patterns are the only structural source of two free
cut variables.  One of the five has no `H0/H1`-compatible partial descriptor;
the remaining four pattern types give twelve symbolic descriptors, of which
six admit an increasing cut tuple.

Every one of those six order-valid faces cuts source edge `6433`.  Its union
colour

```text
U*=0xce71
```

has exactly one adjacent source occurrence.  The other fixed cut is `12826`,
whose adjacent union has rank ten.  The already pinned doubled channel creates
`H0,H1`, neither equal to `U*`.  Lemma 4.1 therefore forces `U*` onto one of
the two free seams.

There are exactly 106 directed `U*` child-occurrence ports.  Imposing one of
them pins both nominally free cuts.  Thus no quadratic free-pair enumeration
or heuristic truncation remains.  The exact census is

```text
12 symbolic descriptors
 6 order-valid faces
 4 faces with a feasible 0xce71 seam
56 directed-port representations = 56 distinct cut descriptors
43 G0/capacity survivors
 1 exact-envelope survivor
 0 upper-complete survivors.
```

The sole exact-envelope survivor is pattern 24/code 45,
`3- 2+ 1-`, with cuts

```text
[6433,9717,12825,12826]
```

and capacity `32175`.  It still has the six upper holes

```text
0xca79, 0xcc79, 0xcef7, 0xea79, 0xeb79, 0xec79.
```

Hence every two-free face is closed before the lower-host stage.

## 7. Exact lower-host oracle

Let `d_i` be the forced deadline, `E_p` the maximal envelope, and let
`J=[s,e)` be a proper-prefix cell (`1 <= e-s <= d_s`).  Put

```text
U_J = OR_(p in J) E_p,
M_J = OR_i (T_i \ OR_(p in [i,i+d_i]\J) E_p).
```

Only rows `i in [s-3,e-1]` can contribute to `M_J`.

### Lemma 7.1 (literal occurrence criterion)

A lower target `S` has a nonempty occurrence on `J` while every middle row is
preserved if and only if

```text
M_J subseteq S subseteq U_J,
E_p intersect S != empty for every p in J.
```

### Proof

Every bit whose complete middle carrier lies in `J` is forced into the local
target, giving `M_J subseteq S`; no cell can contribute outside `U_J`; and
each physical cell must stay nonempty.  Conversely, replace `E_p` by
`E_p intersect S` on `J` and leave every other envelope cell unchanged.
The mandatory condition preserves every middle bit whose external supply is
absent, while all other middle bits retain an outside carrier.  The resulting
cell OR on `J` is exactly `S`. `square`

For each cell the oracle enumerates

```text
S = M_J union R,  R subseteq U_J\M_J,
```

so at most `2^8=256` masks are considered.  Scanning the fixed list of 26,332
nonempty lower masks gives the exact zero-host set.

The nineteen upper-complete rows have zero-host sets of size one, two, or
three and collapse to nine distinct target sequences.  The optimum is

```text
pattern 2, cuts [3277,3278,6388,12826], capacity 29065,
zero-host set {0x4c71}.
```

Its target and envelope hashes are exactly the authenticated `u0` hashes

```text
targets   9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
envelope  57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a
```

Thus O4 supplies no new static compiler candidate.

## 8. Independent replay

The independent Python audit does not invoke either C++ enumerator.  It

1. reconstructs all 25 signed irreducible patterns;
2. rebuilds and verifies all nineteen reported upper-complete free-zero/one
   chronologies;
3. recomputes every forced depth, flat, capacity, maximal envelope and upper
   spectrum;
4. independently enumerates every proper-prefix host and exactly matches all
   nineteen zero-host lists and subset-iteration counts;
5. reconstructs the six order-valid doubled faces, all 106 directed `0xce71`
   ports and all 56 indexed candidates; and
6. matches the `43 -> 43 -> 1 -> 0` free-two filter ledger.

It returns

```text
PASS_SCOPED_STANDARD_O4_NO_ZERO_HOST_FREE_CHRONOLOGY
```

## 9. Frozen artifacts

```text
scratch/search_k16_resident_state2_exact_4opt_zerohost_20260730.cpp
  b509e7741f1438fd994d99ff7c03b71acd840b95981888aab8e8a2e8f7bf9a62

scratch/k16_resident_state2_exact_o4_20260730/free01.result.json
  bf12ea4a1537d9f647dd2c0227907f965789e794799eb3df48fd07ae1a7a0c4c

scratch/search_k16_resident_state2_exact_4opt_free2_ce71_20260730.cpp
  4cecbd4514fe973ae62078eaff4bee05eca1204a30745128a998354fc2adacac

scratch/k16_resident_state2_o4_free2_ce71_20260730/result.r2.json
  44b3ba752574c00ee2214e08a0704025de315e58be8a6d3e5f57d738f26a747e

scratch/audit_k16_resident_state2_exact_o4_20260730.py
  ec0b5a70115efaada11720ac1d349af33bb2b9cffb24c1c16a30327b595f9fb8

scratch/k16_resident_state2_exact_o4_20260730/independent.audit.json
  c0a96e7d369d15f0978e400621d945f0099801c26958296ce6a7ef730d970014
  payload 9b7124ee67307c73020f8264ebc256d3272d9acab6574816a58041f57a4ac6b2
```

## 10. Exact remaining move class

The standard O2/O3/O4 fixed-endpoint segment-permutation basin around state2
is closed.  A successful continuation must leave at least one of its defining
constraints.  The smallest literal possibilities are

- a five-cut rethread with no restored-edge reduction to O4;
- a cut through a terminal flat, with a new exact three-flat staircase;
- a fragmented/nonstandard braid which changes more than four seams;
- or a target-multiset-changing local exchange followed by a rethread.

This theorem neither orders those possibilities nor changes the authenticated
bracket

```text
12873 <= nu(16) <= 12874.
```
