# Audit of the K16 upper-12874 adjacent-fusion censuses

Date: 2026-07-30  
Lane: R  
Status: both scoped no-go results valid; one uniqueness statement corrected

## 1. Frozen scope and verdict

The source is the authenticated universal word

```text
answers/k16_upper12874.word
length 12874
SHA256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

The following two claims are valid for this fixed word.

1. Replacing an adjacent pair by its bitwise OR never gives a universal
   length-12873 word.  The minimum is two holes, attained exactly at the two
   rows recorded by the census.
2. Replacing an adjacent pair by one arbitrary nonzero 16-bit mask never
   gives a universal length-12873 word.

Neither statement allows any other cell to move.

The correction is that the arbitrary-fusion minimum is **not unique as a
fusion assignment**.  Its minimum hole count is one, attained by nine
`(position,replacement)` rows and eight distinct words; every one has the
same sole hole

```text
11373 = 0x2c6d.
```

The unique object in the JSON is only the canonical maximal-intersection
record: position `1`, replacement `8297`.  Thus any theorem text saying
“the unique arbitrary-fusion minimum” must be changed to “the unique
canonical maximal-intersection minimum,” or replaced by the exact
nine-row/eight-word statement above.

## 2. Exact affected-interval ledger

Fix adjacent positions `p,p+1` in a word `w`.  Let `E_p(t)` count old
intervals ending at `p` with OR `t`, and let `S_{p+1}(t)` count old intervals
starting at `p+1` with OR `t`.

For the special replacement

```text
z = w[p] OR w[p+1],
```

every old interval containing both positions corresponds bijectively to the
new interval obtained by contracting the pair, with the same OR.  Intervals
avoiding both positions are unchanged.  The only lost intervals are the
disjoint families ending at `p` and starting at `p+1`; hence the exact lost
multiplicity is

```text
E_p(t) + S_{p+1}(t).
```

This proves the first driver's `Counter` ledger, including repeated labels.

For an arbitrary replacement `z`, the old affected intervals split
disjointly into:

- intervals ending at `p`;
- intervals starting at `p+1`;
- intervals containing both positions.

Write `a` for an optional suffix OR ending at `p-1` and `b` for an optional
prefix OR starting at `p+2`, with the empty choice having OR zero and
multiplicity one.  The third family has label

```text
a OR w[p] OR w[p+1] OR b
```

and multiplicity equal to the product of the multiplicities of `a` and `b`.
Thus the second driver subtracts every affected old interval exactly once.
Its repair set `R_p` consists precisely of targets whose total old
multiplicity equals this removed multiplicity.  Targets outside `R_p`
retain an untouched witness.

After contraction, every new affected interval has label

```text
a OR z OR b.
```

Multiplicities are irrelevant at this last step because only existence of a
witness is required; consequently replacing the context multiset by its set
of OR values is sound.

## 3. Maximal-intersection lemma

For a repair target `t`, a replacement `z` supplies `t` exactly when some
context `c=a OR b` satisfies

```text
c OR z = t.
```

In particular `z` is a submask of `t`.  Suppose `z` supplies every target in
a set `Q`, and put

```text
U = intersection(Q).
```

Then `z` is a submask of `U`.  If `c OR z=t`, the inclusions

```text
z subseteq U subseteq t
```

give `c OR U=t`.  Hence `U` supplies every target supplied by `z`.

Taking `Q=R_p` proves that a universal replacement exists if and only if the
maximal intersection works.  If a replacement leaves at most one hole `h`,
take `Q=R_p\{h}`.  The leave-one-out maximal intersection must also leave at
most that one hole.  Enumerating every nonzero submask of every successful
maximal intersection is therefore a complete enumeration of all zero- and
one-hole replacement values.  This validates the second driver's
maximal-replacement and leave-one-out reductions.

## 4. Independent extremal replay and multiplicities

An independent checker uses a literal ending-OR replay, not either census
bank recurrence.  It confirms the two adjacent-OR minima:

```text
p=0: holes {11373,18553}
p=2: holes {5229,21613}
```

It also replays all nine arbitrary-fusion one-hole rows.  They are

```text
p=0: z in {18553}
p=1: z in {8200,8201,8232,8233,8264,8265,8296,8297}
```

and each has sole hole `11373`.  The rows `(p,z)=(0,18553)` and
`(1,8297)` produce the same literal word, so there are eight distinct words.

As a separate multiplicity check, the checker directly enumerates source
intervals only for the extremal targets.  Their exact source multiplicities
are

```text
5229:1, 9325:1, 11373:1, 13421:1,
18553:1, 21613:1, 26745:2, 30317:1.
```

Every such occurrence lies in the affected family asserted by the relevant
record.  In particular target `26745`, the only repeated extremal target,
has both occurrences removed, confirming that the product/count ledger does
not accidentally collapse multiplicity.

Independent artifacts:

```text
scratch/audit_r_k16_upper12874_fusion_minima_independent_20260730.py
SHA256 9d7a67fa3d560818df935ff5a27dcaaea2b3c557babf5c8ebc20fb0c6b130dd0

scratch/r_k16_upper12874_fusion_minima_independent_20260730.audit.json
SHA256 6d69151c5d5c4ccdf271f4d31c2707442cea63504bc61fddaf3d0b374f848418
payload SHA256 48c003344c067122277e282ba0f7f2cea785c29a3ac96f84a43739fd0ebaa23e
```

## 5. Current census artifacts and documentation caveats

The audited current files are

```text
scratch/audit_k16_upper12874_adjacent_fusion_census_20260730.py
SHA256 6a4089b4599fc174d4ebc1a126a6210db19ed36577f0562bbe3a14d45cbc20e6

scratch/k16_upper12874_adjacent_fusion_census_20260730.audit.json
SHA256 8f8441844dff8470723566f38818d0e17da2af81fe66dbbd007e9040cdb6195e
payload SHA256 2b35f6e62cdf264f39425b07d55e47b522e16d0094951326d863a553a100516e

scratch/audit_k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.py
SHA256 deade2971c563312153b47ff6d6b2b6202daa8c38331507d621fc33bdf9ad279

scratch/k16_upper12874_arbitrary_two_to_one_fusion_census_20260730.audit.json
SHA256 9c9451aa69f80778ec0843dbb4471757ce779d9678a43ed6f97161a99bf7597a
payload SHA256 02ecfdcdd561fd7bd727154ade27eb3bb561f60404da9ae94409e92390ba9861
```

Earlier theorem prose cites stale hashes for both JSON files and must be
updated before freezing the package.

Two smaller documentation issues do not affect the pinned result:

1. `minimum_normalized_candidate_hole_count_histogram` is a histogram only
   for the canonical all-target intersection at each position, not over all
   arbitrary replacement masks.  The JSON scope says this correctly.
2. The arbitrary-fusion driver always writes the status string
   `PASS_NO_UNIVERSAL_ARBITRARY_ADJACENT_FUSION`; it does not assert that its
   `universal` list is empty before doing so.  On the pinned source the list
   is empty and the no-go is valid, but a fail-closed revision should either
   require emptiness or choose the status from the result.

No conclusion here excludes a nonadjacent fusion, a fusion accompanied by
other edits, or a wider coherent rethreading.
