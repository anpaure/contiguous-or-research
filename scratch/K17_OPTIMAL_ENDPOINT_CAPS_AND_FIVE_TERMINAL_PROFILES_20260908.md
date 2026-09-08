# Optimal k17 endpoint caps and the five exact terminal profiles

2026-09-08. General endpoint-cap proof and one bounded exact h100
verification by `exact_equality_structure`. Root independently reviewed
the full checker before its single execution.

Three explicit variants of the optimal k17 word have now been checked:
one with a singleton first letter, one with a singleton last letter,
and one with both endpoints singleton. Each still has 24,313 letters
and covers all 131,071 nonempty targets by ordinary intervals. Each
recorded target witness was independently replayed by a range-OR query.

All pair-preserving right caps of the original word and its reversal
are also classified. Their combined terminal recency profiles are
exactly

    (s,7-s,1,1,1,1,1,1,1,1,1,1),  1<=s<=5.            (0.1)

The ten final entries in (0.1) are ones. These are actual profiles of
certified universal words, not merely cardinality-compatible abstract
states. This result does not yet give an optimal 18-coordinate word.

## 1. A dimension-independent endpoint-cap theorem

Let A=(A_1,...,A_m), m>=2, be a nonzero universal word on any finite
ground set. Write L=A_m and P=A_(m-1). Replace only its final letter
by a nonempty C subset L.

The last adjacent pair retains its OR if and only if

    L minus P subset C subset L.                       (1.1)

Under (1.1), every ordinary interval of length at least two has
exactly its previous OR. Indeed all unaffected intervals are
unchanged, and every changed interval contains P immediately before
the last letter; P union C=P union L. Thus only the old one-letter
target L can possibly lose its final occurrence.

Consequently, if L has any witness other than the one-letter final
interval, every cap in (1.1) preserves universality. An interior
literal copy is a particularly simple sufficient certificate. For a
proper cap, the exact condition is that L has an interval witness
inside the prefix A_1,...,A_(m-1), or that P subset L. In the latter
case the last pair itself still has union L. This also covers the
case where the required backup is a longer interval rather than a
literal copy.

The left endpoint satisfies the identical theorem under reversal.
For m>=3 both ends can be capped simultaneously whenever the two
old endpoint targets each have a witness entirely in the unchanged
interior. The first and last adjacent pairs remain unchanged, as do
all interior pairs. Every interval of length at least two is a union
of its consecutive pair ORs, hence is unchanged. The interior backups
retain the only two singleton targets that might otherwise be lost.

The length-three lower bound on this simultaneous statement avoids
the two-letter exception where both letters of the sole pair change.
No such exception is relevant for the present 24,313-letter word.

This is an actual uniform construction rule in every dimension:
once its displayed backup and subset conditions hold, it changes
the literal endpoints without a new full-cube coverage assumption.
It is not an all-dimensional existence theorem for those backups.

## 2. Exact recency-state change and profile reduction

Assume the original last pair strictly grows beyond L. In the
most-recent-first state, the first two blocks are then L and P minus L.
For a cap satisfying (1.1), every removed coordinate L minus C
occurs in P, so its last occurrence moves exactly one time step
backward. The new first two blocks are

    C, (P minus L) union (L minus C)=P minus C.          (2.1)

Every later block is unchanged. Thus the positive block-size profile
changes by

    (|L|, b_2, b_3,...)
       ->(|C|, b_2+|L|-|C|, b_3,...).                  (2.2)

If the immediate old second block were empty, one must use the
time-indexed blocks first and delete empty blocks afterward. The
strict-pair-growth condition here makes (2.2) unambiguous.

Let f=|L minus P|. Subject to the backup condition, every cap size

    max(1,f)<=|C|<=|L|

is available. If f>0 there are exactly 2^|L intersect P| cap masks;
if f=0 the nonempty cap count is 2^|L|-1.

Once arbitrary relative relabeling of the entire universal base word
is allowed, cap masks producing the same ordered block sizes are
equivalent for a terminal seam: any ordered coordinate partition
with those sizes is the image of the recency blocks under some
coordinate permutation. Therefore one actual word per size profile
suffices for that specified relabeling family. This is also proved
in [the exact one-seam theorem](EXACT_ONE_SEAM_LIFT_PRECEDENCE_AND_ENDPOINT_CAP_THEOREM_20260908.md),
Sections 3–5, which this audit independently read and checked.

## 3. The literal k17 endpoint data

The input is
[answers/k17_optimal24313.word](../answers/k17_optimal24313.word),
with SHA-256

    7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9.

Its final letters are P=25,249 and L=689, of ranks six and five.
Their union has rank seven, and

    L minus P=16.

The old letter 689 also occurs at zero-based interior position 87.
Thus all 16 caps containing the bit mask 16 preserve universality.
The original terminal profile is (5,2,1^10); the resulting profiles
are exactly (s,7-s,1^10) for s=1,...,5.

The first two letters are 8,834 and 10,913, of ranks four and six.
Their union has rank seven, and

    8834 minus 10913=2.

The old first letter 8,834 also occurs at zero-based interior
position 85. Thus all eight first caps containing the bit mask 2
preserve universality. Equivalently these are last caps of the
reversed universal word. Its original terminal profile is
(4,3,1^10), and its capped profiles are (s,7-s,1^10), s=1,...,4.

The checker enumerates ALL 16 and eight cap masks in these two
families, records their physical terminal block masks, and verifies
every prefix OR from the second onward against the unchanged old
suffix chain. It does not infer these profiles just from endpoint
cardinalities. The sorted first representative of each size is saved
as an actual literal word.

## 4. Three separately verified optimal variants

The following files retain all interior letters and change only the
indicated endpoint or endpoints:

| Variant | First mask | Last mask |
|---|---:|---:|
| [First singleton](../answers/k17_optimal24313_first_singleton.word) | 2 | 689 |
| [Last singleton](../answers/k17_optimal24313_last_singleton.word) | 8,834 | 16 |
| [Both singleton](../answers/k17_optimal24313_both_singletons.word) | 2 | 16 |

Each has length 24,313. For each word, the run independently verifies
all nonempty target masks by complete ending-OR enumeration and
then recomputes all 131,071 saved interval ORs through a segment tree
built from that literal variant. Both endpoint pairs are checked
directly to equal their old pair ORs, and both old endpoint letters
are checked to remain in the unchanged interior.

The SHA-256 hashes are respectively

    first: d819c2579db85c5130b0d43441cb736b23974c460ac5bd6cbac700b491862496
    last:  55791b5a8f707ea6db10e99ed052c10712e086cd21617a6a699e9ec1c2fe8406
    both:  9064e18b03e800833a8ea50d8517daee812e9bc001deb86247c4ed8ae18bafc4

The matching lower bound B(17)=24,313 is unchanged, so all three
verified variants are optimal. The nine representative words from
the two orientation/size families are certified by the endpoint
theorem and their literal duplicate checks; the additional full-cube
enumerations were performed specifically for the three displayed
singleton variants, not silently claimed for every representative.

## 5. Exact interface for the next-coordinate seam

The one-seam construction with a universal left base A and marked
right tail B is

    A || {z} || (B_1 union {z}) || ... || (B_l union {z}).

For a fixed B, the cited one-seam theorem gives an exact precedence
problem for a relative coordinate permutation of A. Its only
dependence on the terminal recency state of the left base is its
ordered block-size profile. Equation (0.1) therefore supplies five
fully justified base profiles for that gate.

This profile family is complete for pair-preserving terminal caps
of the original optimal word or its reversal. It is not asserted
to include every possible terminal profile of every optimal k17
word. A successful or failed decision for a particular marked tail
must keep that scope explicit. No marked tail was changed or tested
in this endpoint run.

## 6. Execution and complete artifacts

* [Reviewed standalone checker](verify_k17_endpoint_caps_and_profiles_20260908.py).
* [Complete cap, state, profile, and variant certificate](k17_endpoint_caps_20260908/endpoint_caps_and_terminal_profiles_certificate.json).
* [All representative and singleton words](k17_endpoint_caps_20260908/).

The program ran exactly once on h100 (`arboghast`), after root's full
code review, with hard limits of 10 CPU seconds, 15 wall seconds,
and 128 MiB address space. It returned PASS in approximately 0.434
seconds. No mathematical code ran locally.

Remote artifacts remain at

    h100:/home/amodo/exact-b-k17-endpoint-caps-20260908/output/

There was no interior-letter change, deletion, profile search,
coordinate-permutation search, or attempted 18-dimensional word in
this run. The result is the proved endpoint operation together with
its complete finite interface on the supplied optimum.
