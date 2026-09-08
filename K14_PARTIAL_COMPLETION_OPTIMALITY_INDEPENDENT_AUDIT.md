# Independent audit: optimal standalone completion for the `k=14` 260-mask family

## Verdict

**PASS.**

The endpoint-defect lemma in `K14_PARTIAL_COMPLETION_IMPROVEMENT.md` is
correct under its stated two-layer interpretation, and its application to the
certified `k=14` missing family proves that every **standalone** completion has
length at least 243.  The supplied 243-entry word attains this bound.

This is not a lower bound on the number of entries that must be appended to the
old 3434-entry prefix: a witness using both old and new entries crosses the
seam and need not be present in the standalone suffix.  The source note states
this limitation correctly.

The precise general hypothesis used below is that `A` and `B` are antichains
and no upper target `T in B` can be a subset of a lower target `S in A`.  It is
enough, as in the application, that all lower targets have one rank and all
upper targets have a strictly larger rank.  This is what the note's terms
"lower-rank" and "higher-rank" mean.

## 1. Mathematical audit of the endpoint-defect lemma

Let `A` be an antichain of `M` lower targets and select one interval `I_S` for
each `S in A`.

1. Two distinct selected lower intervals cannot be nested.  Interval
   containment implies containment of their OR values, contradicting the
   antichain property.
2. Consequently their left endpoints are all distinct: two intervals with the
   same left endpoint are nested.  Their right endpoints are all distinct for
   the same reason.
3. Thus, in a word of length `n`, precisely `n-M` physical positions are unused
   as selected-lower **left** endpoints, and precisely `n-M` positions are
   unused as selected-lower **right** endpoints.  These are side-specific
   resources.  A physical position may legitimately contribute one resource
   on each side, which is why the total is `2(n-M)` rather than the size of a
   union of position sets.

Now select one witness `J_T` for every `T in B`.

4. The selected upper left endpoints are mutually distinct, and the selected
   upper right endpoints are mutually distinct, because `B` is also an
   antichain.
5. Suppose `J_T` and a selected lower interval `I_S` have the same left
   endpoint.  They cannot also have the same right endpoint, since one physical
   interval has only one OR value.  If `J_T` ended first, then `J_T` would be
   contained in `I_S`, forcing `T subseteq S`, contrary to the layer
   hypothesis.  Therefore `I_S` ends first, `I_S subset J_T`, and `S subset T`.
   The identical conclusion follows for a shared right endpoint, with the
   interval order reversed.
6. If both side-endpoints of `J_T` are shared with lower witnesses, they cannot
   be shared with the same selected `I_S`: sharing both endpoints would make
   `J_T=I_S`.  Hence the shared endpoints identify distinct members of
   `{S in A : S subset T}`.

Writing

```text
c(T) = |{S in A : S subset T}|,
```

item 6 proves that `J_T` can share at most `min(2,c(T))` of its two
side-endpoints.  It therefore consumes at least

```text
max(0,2-c(T))
```

unused lower side-slots.  Item 4 ensures that two upper witnesses cannot reuse
the same unused lower-left slot or reuse the same unused lower-right slot.
Summing gives exactly

```text
2(n-M) >= sum_{T in B} max(0,2-c(T)).
```

This checks all potential endpoint collisions, including the case where an
upper left endpoint and another upper right endpoint are the same physical
position: those occupy different side-specific slots and are correctly counted
separately.

## 2. Independent reconstruction of the `k=14` application

The checker `scratch/audit_k14_completion_optimality.cpp` independently
regenerated the missing family from the 3434-entry prefix.  It found exactly:

```text
238 rank-9 targets
22 rank-10 targets
```

For every missing rank-10 target `T`, it then directly counted the missing
rank-9 targets contained in `T`.  The full histogram is:

| `c(T)` | number of rank-10 targets |
|---:|---:|
| 0 | 1 |
| 1 | 7 |
| 2 | 6 |
| 3 | 7 |
| 4 | 1 |

The unique `c=0` target is `15346`.  The seven `c=1` targets and their unique
contained lower targets are exactly:

| upper target | unique lower target |
|---:|---:|
| 7676 | 7420 |
| 8015 | 8014 |
| 13287 | 13283 |
| 13439 | 13423 |
| 13757 | 13725 |
| 14285 | 6093 |
| 15334 | 15302 |

Thus the defect is

```text
1*2 + 7*1 + 14*0 = 9.
```

With `M=238`, the lemma gives

```text
2(n-238) >= 9,
n >= 243.
```

This lower bound uses all 22 rank-10 targets equivalently, or just the eight
positive-defect targets.  The two uniform-rank families satisfy every
antichain and cross-rank hypothesis above.

## 3. Audit of the secondary standalone claims

The literal-lower theorem is correct.  After marking one literal occurrence
of each lower target, a hard upper witness can meet at most one marked entry,
because each hard target contains at most one missing lower target.  Trimming
assigns it to one adjacent extra run.  A run of length `s` supplies at most
`s+1` mutually nonnested hard witnesses.  Four singleton extra runs are the
only possible equality case at length 242, but the run whose entry is `15346`
cannot support a second distinct rank-10 target.

The one-nonliteral theorem is also correct.  The nonliteral lower witness
occupies a run of length at least two, so at most four extra runs exist.  If a
run of length `s` attained the `s+1` hard-witness capacity, distinct endpoint
sets and nonnesting force the `s+1` adjacent pairs.  An internal adjacent pair
inside the nonliteral lower witness has rank at most nine, so that run cannot
attain the bound.  The sole numerical equality case has one two-position run
and three singleton runs; `15346` must occupy a singleton run by itself, again
destroying equality.

The target-sensitive search truncation in section 4 is valid as well.  At
length `M+4`, the selected lower witness `I_i` lies in `[i,i+4]`.  A physical
interval of length `ell>=5` contains the `ell-4` distinct selected lower
witnesses indexed from its left endpoint through `right-4`.  If its OR is `T`,
all of those lower masks lie in `T`, so `ell<=4+c(T)`.  The boundary indices
remain inside `[1,M]`.

None of these secondary observations is needed for the 243 lower bound once
the endpoint-defect lemma is available.

## 4. Independent certificate verification

The new checker does not trust the recorded witness file or the precomputed
missing list.  It performs all of the following independently:

1. checks the target records, ranks, uniqueness, and the `238+22` split;
2. computes every `c(T)` and the exact hard family;
3. recomputes the prefix's missing masks by the distinct-suffix-OR recurrence
   and compares the resulting set with `k14_missing_260.txt`;
4. enumerates all intervals of the 243-entry standalone completion and checks
   every target;
5. checks all 260 witness-certificate records for uniqueness, bounds, rank,
   and exact recomputed OR;
6. recomputes the globally shortest witness length for every target;
7. checks that the completion consists of all 238 lower masks literally plus
   exactly the five claimed extra entries `48, 288, 8196, 8015, 15346`;
8. checks that `k14_completed_best.txt` is bytewise the prefix followed by the
   completion; and
9. independently verifies all 16,383 nonzero masks in the completed 3677-entry
   word with the suffix-OR recurrence.

The checker was compiled remotely with optimized C++ and returned:

```text
PASS
targets=260 lower=238 upper=22 c0=1 c1=7 c_ge_2=14 endpoint_defect=9 standalone_lower_bound=243
prefix=3434 completion=243 completed=3677 full_nonzero_coverage=16383/16383
shortest_witnesses rank9_len1=238 rank10_len1=2 rank10_len2=20
```

This agrees with the claimed shortest-witness distribution and independently
validates every record of `k14_completion_243_witnesses.txt`.

## 5. Audited hashes

```text
e0ce5ffc3bde570399c8ef24fad5a0e4571a0e76f697048ca10daee0b057972e  K14_PARTIAL_COMPLETION_IMPROVEMENT.md
4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad  k14_pinnable_factor_missing260.txt
152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab  k14_missing_260.txt
06f4b5a06f411a896df9d471b4e2f60d97eea537b4c81710f5e1c62117d68b19  k14_completion_best.txt
63a5f7a51e7e873db394e92cfd606c027405971598377fa96a838a9c0ac58590  k14_completion_243_witnesses.txt
d5fc5c13685ca0e2eb182de0d245e93368453d0aaeaf6e2f5cfdff219a59c83c  k14_completed_best.txt
70e6410108d82e2a062134c9b442e116b94cac5874c9bccc0c7a0850bdfadffb  scratch/certify_k14_completion.cpp
2f8422c1198766f176a4b28a800863ccee24b51a90d452ed43652bcd670782ee  scratch/audit_k14_completion_optimality.cpp
```

The remote audit binary had SHA-256
`35c9abbc702f99be14d79a64cf3760ec6f79d3194989dc569aac732b6b825235`.

## Final certified statement

For the exact 260-mask family omitted by
`k14_pinnable_factor_missing260.txt`, the minimum length of a word that covers
that family **by itself** is exactly

```text
243.
```

Therefore the concatenated nonzero universal word has certified length
`3434+243=3677`.  This proves an upper bound for the full `k=14` problem; it
does not prove that 3677 is globally shortest and does not rule out a shorter
cross-seam append to the fixed 3434-entry prefix.
