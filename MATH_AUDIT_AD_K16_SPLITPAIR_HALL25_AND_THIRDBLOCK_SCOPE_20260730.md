# K16 split-pair Hall-25 audit and the exact A-halo exchange target

Date: 2026-07-30  
Lane: AD  
Status: exact finite audit; one conditional matching-improvement lemma; no
physical improving chronology is claimed.

## 1. Frozen inputs

The source chronology is

```text
scratch/root_k16_a_fourtoken_q1hole_direct_moves_20260730/
    best_upper_complete_bad2.targets
SHA-256 dc336b93f981d09bbba9f44969bef46da51c6feeab595b05c2fd6b26b340638d
```

It is arbitrary-upper-complete but has the two already authenticated
depth-three middle replay defects at old rows 3844 and 3845.  The exhaustive
exact split-pair output is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/summary.tsv
SHA-256 296aaa105dea851d95e5e4e59bb586215b2053aeb777e966e3d18c8a158f26fd
```

and its exact enumerator is

```text
scratch/search_ad_k16_bad2_splitbuffer_pair_exact_20260730.cpp
SHA-256 bf7d944fc43eef80f429ad0eaccbedaef8351f2f819e5f16061cc2fc829bdf61
```

The search emitted eleven upper-complete rows, of which eight are distinct;
the three repetitions are the two orientations of a one-row packet.  Direct
middle replay, zero-envelope replay, row-multiset replay, and unrestricted
upper replay pass for all eight distinct chronologies.

## 2. The eight exact carriers

Every interval below uses half-open source coordinates.  The two oriented
packets are removed from the source and inserted consecutively, in the listed
order, immediately before old row 3846.

| id | first packet | second packet | SHA-256 prefix | incidences | Hall deficiency |
|---:|---|---|---|---:|---:|
| 151 | `[2186,2200)` forward | `{1240}` | `a509899b` | 347925 | 26 |
| 155 | `[2186,2200)` forward | `{3896}` | `059600a7` | 347980 | 26 |
| 162 | `[2186,2200)` forward | `[1241,1266)` forward | `ad58f4f4` | 347878 | 26 |
| 178 | `[5990,6011)` forward | `[1987,1993)` reverse | `e0b2d3f0` | 347905 | 28 |
| **229** | **`[2186,2217)` forward** | **`[1266,1295)` reverse** | **`cae23cfc`** | **347875** | **25** |
| 231 | `[2186,2217)` forward | `[4052,4105)` forward | `6dc7a62f` | 347807 | 27 |
| 233 | `[3165,3196)` forward | `{4046}` | `ab6e72cf` | 348022 | 26 |
| 282 | `[2994,3030)` reverse | `[5790,5804)` reverse | `e9dfecd6` | 347927 | 27 |

Thus exact229 is the unique Hall optimum among these eight.  Its frozen Hall
audit is

```text
scratch/ad_k16_bad2_splitpair_exact_20260730/exact_229.hall.k.audit.json
SHA-256 85471243dcdd8a8ab6dc7530fc49b6629202b4403ad90a750961153afd0b1fb0
```

It has maximum matching 26307, deficiency 25, and canonical alternating
shore

\[
 |S_{229}|=212,\qquad |N_{229}(S_{229})|=187.
\]

## 3. Exact explanation of the nine-unit gain

The comparison chronology is detached-cycle pass 1,

```text
scratch/root_k16_a_bad2_detached_cycles_20260730/out7/pass_1.targets
SHA-256 aea7a05a8837298205e9f35f39c7e6b99b8e7ef00fe46dcab9a8ab831e018e34
```

whose maximum matching is 26298 and whose deficiency is 34.

To compare right vertices without counting harmless shifts of long unchanged
segments, label every source-row occurrence by its source position
`0,...,12872`.  If the origin permutation of a derived chronology is `o`,
relabel its compiler cell `(s,length)` by the ordered tuple

\[
 C=(o(s),o(s+1),\ldots,o(s+\ell-1)).                 \tag{3.1}
\]

This is injective inside each chronology.  It identifies a transported
literal interval with itself and leaves a genuinely changed or reversed
interval distinct.  The numerical decomposition below depends on this stated
canonical identification, while its net cardinality difference does not.

Under (3.1), the symmetric difference of the two frozen maximum matchings has
379 components:

\[
 360\text{ balanced},\qquad
 14\text{ exact229-positive paths},\qquad
 5\text{ detached-positive paths}.                 \tag{3.2}
\]

Consequently

\[
 26307-26298=14-5=9.                                \tag{3.3}
\]

This is not an incidence-volume effect: exact229 has only 66 more incidence
edges than detached pass 1.  On the old detached canonical shore, exact229
restores fourteen neighbour columns and loses none:

\[
 |S_{\rm det}|=249,\quad |N_{\rm det}(S_{\rm det})|=215,
 \quad |N_{229}(S_{\rm det})|=229.                  \tag{3.4}
\]

The fourteen restored shore providers, written as `target@source-row tuple`,
are

```text
581c@(5989,5990)             583c@(5989,5990,5991)
5c30@(1987,1988)             5c70@(1986,1987,1988)
5439@(5385,5386,5387)
6a38@(3030,3031,3032)        6a70@(3029,3030,3031)
6b21@(3847,3848,3849)
4331@(6293,6294)             4339@(6293,6294,6295)
4268@(788)                   4370@(786,787)
4770@(785,786,787)           4378@(786,787,788)
```

These are precisely at the isolated token-cycle sites which exact229 leaves
in their source-relative order.  The five matching units paid by exact229
are boundary effects of moving its first packet `[2186,2217)`.  The old shore
is therefore relaxed to deficiency 20, but another shore becomes binding at
25.  This shore rotation is why counting restored providers alone would give
the wrong global conclusion.

## 4. Strongest donor geometry for the exact229 shore

On the fixed shore `S_229`, the eight exact carriers have the following
neighbour counts and exact restricted-matching deficiencies.

| id | neighbours of `S_229` | restricted deficiency |
|---:|---:|---:|
| 151 | 190 | 22 |
| 155 | 191 | 21 |
| 162 | 190 | 22 |
| 178 | 193 | 19 |
| 229 | 187 | 25 |
| 231 | 186 | 26 |
| **233** | **194** | **18** |
| 282 | 192 | 20 |

Exact233 is therefore the strongest exact-and-upper donor for the present
shore.  Relative to the source-tuple cells of exact229, it adds seven shore
neighbours and loses none.  Five of them form a common `A`-halo also present
in exact178 and exact282.  Their exact desired profiles are

| target | canonical cell | allowed | mandatory | envelope letters |
|---|---|---:|---:|---|
| `091d` | `(2186,2187)` | `091d` | `001d` | `040d,0419` |
| `291d` | `(2186,2187,2188)` | `291d` | `201d` | `0919,091c,290c` |
| `291c` | `(2187,2188)` | `291c` | `2014` | `091c,290c` |
| `2e28` | `(2217,2218)` | `2e28` | `0e00` | `2628,2c28` |
| `2f28` | `(2217,2218,2219)` | `2f28` | `0f08` | `2328,2628,2c28` |

In exact229 those five cells instead have allowed/mandatory masks

```text
2819/0819, 6819/6819, 6818/6010, 0d0c/0c0c, 2d0c/2c0c,
```

respectively, and do not provide the five displayed targets.

### Lemma 4.1 (conditional five-ear augmentation)

Suppose an exact229 modification retains every edge of its frozen matching,
retains the old nonmatching edges displayed in the five paths below, and adds
the five displayed provider incidences at the same source-tuple cells.  Then
its maximum matching has size at least 26312 and its deficiency is at most
20.

#### Proof

Relative to the frozen matching `M_229`, the following five augmenting paths
are pairwise vertex-disjoint.  Unmarked edges are nonmatching and `M` marks a
matching edge.

```text
095d -- (6126,6127,6128) --M-- 091d --NEW-- (2186,2187)
291d --NEW-- (2186,2187,2188)
a91c -- (8626,8627) --M-- 291c --NEW-- (2187,2188)
6e28 -- (4049,4050,4051) --M-- 2e28 --NEW-- (2217,2218)
2f28 --NEW-- (2217,2218,2219) --M-- 2c0c -- (5461)
```

Flip all five paths simultaneously.  Vertex-disjointness leaves a matching
with five additional edges.  This proves the claim.  ∎

Exact233 also creates the disjoint conditional ear

```text
1665 -- (2958,2959,2960) --M-- 0665 --NEW-- (3163,3164,3196),
```

which would give size 26313 and deficiency at most 19 if it too were added
without destroying the retained edges.  Its further new `4879` column is a
shore neighbour but is not an augmenting ear for the frozen matching.

The retention hypothesis is essential.  Exact233 itself has deficiency 26,
not 19.  Its matching symmetric difference with exact229 has 331 components:
320 balanced, five exact233-positive, and six exact229-positive.  The seven
exact229 provider incidences in the six lost paths are

```text
083b@(3196,3197)        allowed/mandatory 083b/0823
402f@(4046,4047)        allowed/mandatory 402f/4003
481b@(3197,3198)        allowed/mandatory 481b/4801
682d@(4047,4048,4049)   allowed/mandatory 682d/6805
482d@(4047,4048)        allowed/mandatory 482d/4805
682c@(4048,4049)        allowed/mandatory 682c/2804
483b@(3196,3197,3198)   allowed/mandatory 483b/4823
```

Thus the sharp physical target is not “switch to exact233.”  It is: restore
the five `A`-halo ears, optionally add `0665`, and preserve these seven
exact229 incidences.

The exact233 donor pair is `[3165,3196)` forward followed by the singleton
`{4046}`.  The tempting two-packet hybrid `[3165,3196)` forward plus
`[1266,1295)` reverse is absent from the complete split-pair catalogue.
Hence the desired retention cannot be asserted by an unproved simple packet
splice.

## 5. Audit of the proposed fixed-229 third-packet enumerator

The audited source is

```text
scratch/search_ad_k16_splitpair_exact229_thirdblock_hallcore_20260730.cpp
SHA-256 044a14191d0eb17496e004e08a0638b7e7c7718b8d500b2d15f200841f81369a
```

No census was run in this audit.

### Positive semantics

For every candidate which the program emits, the following are sound.

1. Fixed packets `A=[2186,2217)` forward and
   `B=[1266,1295)` reverse, and one disjoint packet `C`, are each deleted once
   and inserted once.  The row multiset and length are preserved.
2. All six orders of `A,B,C` are enumerated.
3. The selected source gaps and every literal destination window receive the
   exact seven-row depth-three test.
4. Every survivor then receives a full variable-depth middle replay and a
   full unrestricted upper replay.

No materialization or permutation-order bug was found.

### Exact completeness scope

The actual class is narrower than the header's informal “one extra
halo-separated packet.”  In code, `C` must satisfy all of the following.

* Length `1..64`, either orientation.
* Its complete six-row source context lies before the first flat:
  `C.hi+6 <= 6320`.
* It is source/destination separated by six rows:
  `C.hi+6 <= 3846` or `C.lo >= 3852`.
* It avoids the protected old rows 4400 and 4401:
  `C.hi <= 4400` or `C.lo > 4401`.
* Its source halo is disjoint from both fixed packet halos.  The inherited
  strict test requires at least seven untouched rows between packet
  intervals.

The 4400/4401 exclusion is not implied by pairwise packet-halo separation.
Therefore the current source is complete only for this explicitly protected
subclass; either the theorem scope must say so or that filter must be removed.
Likewise the strict seven-row separation must be named if six-row shared
contexts are meant to lie outside the class.

The program also does not SHA-lock the claimed authenticated input; it uses a
strong structural fingerprint only.  This is adequate for positive
mathematics on a separately hashed input but is not fail-closed provenance.
Despite `hallcore` in its name, it computes no Hall matching or fixed-shore
score; every output needs a separate exact Hall audit.

Finally, the strongest five-ear package is structurally outside this fixed-A
normal form: all five desired cells are the source/destination boundary cells
of `A`, while this census keeps `A` removed and forces `C` to be halo-disjoint
from it.  It may find unrelated or duplicate shore providers, but it cannot
literally restore those five canonical cells.

A direct destination-seam replay further shows that none of

```text
[3165,3196) in either orientation, {4046},
[5990,6011) in either orientation, [1987,1993) in either orientation
```

can be inserted as `C` with fixed `A,B` in any of the six orders.  Thus the
known exact233/exact178 donor blocks do not survive as naive third packets.

## 6. Proved boundary

The nine-unit improvement of exact229 is fully explained by the exact
14-positive/5-negative alternating-component ledger.  A repeatable
graph-theoretic improvement certificate of five, or conditionally six, is
also explicit.  What remains unproved is the literal chronology exchange
which realizes those new provider incidences while retaining the seven named
exact229 providers, exact middle replay, and unrestricted upper coverage.
The fixed-A third-packet census is sound inside its stated subclass but does
not contain this strongest exchange.
