# Independent audit of the three-ring clipped upper-cone reservoir

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited file:**
`MATH_THEOREM_THREE_RING_CLIPPED_UPPER_CONE_RESERVOIR_AND_ALLWIDTH_TRANSPARENCY_20260804.md`  
**Verdict:** **GO after one scope correction.**  The reservoir, disjointness,
greedy packing, clipped-residence, and conditional all-width transport
arguments are correct.  The original Theorem 5.1 omitted the necessary
hypothesis that the ambient carrier was upper-complete before the rethread.
That hypothesis and the intended width wording have been inserted.

## 1. Size-two seam traces

For cyclic indices,

\[
 L_i=K\cup\{a_i\},\qquad
 R_i=B\cup\{a_{i-1},a_i\},\qquad
 I_i=B\cup\{a_i\}.
\]

Hence `L_i cap R_i=I_i` and

\[
 L_i\cup R_i=K\cup\{a_{i-1},a_i\}=U_i.
\]

After the switch `R_i -> R_(i+1)`, the union at role `i` is
`U_(i+1)`.  Thus the three values are permuted, not deleted.  Distinctness
of all owners and lower colours follows from the distinct external traces;
no auxiliary occurrence is required for `|T|=2`.

## 2. Low-path resources and the ring

For a low trace `T`, every owner, lower colour, and upper colour has
intersection with `E` exactly `T`.  Different low traces are therefore
resource-disjoint at all three ranks.  Ring resources have the following
external traces:

- `L_i` and `I_i`: `{a_i}`;
- `R_i` and `U_i`: `{a_(i-1),a_i}`.

Since the low range begins at `|T|=3`, no low resource can equal a ring
resource.  The no-wrap identity

\[
 (q-1)+(h-1)=m-2
\]

is exact, and the sliding windows cover all `m-1` coordinates of `K`.

## 3. High-tail greedy packing

The symmetric geodesic has `q` distinct owners and `q-1` distinct colours
on each immediate shore.  Symmetric-group invariance on `Z` therefore gives
the exact hitting probabilities

\[
 \frac q{\binom Nm},\qquad
 \frac{q-1}{\binom N{m-1}},\qquad
 \frac{q-1}{\binom N{m+1}}.
\]

For `h<=d=O(sqrt(m))`, all three denominators are
`2^(2m-o(m))`.  The previously installed ring, low, and high paths forbid
at most `O(m(2^m+H_d))=2^(m+o(m))` resources at each rank, where
`H_d=2^o(m)`.  The union-bound failure probability is consequently
`2^(-m+o(m))<1`.  This proves the simultaneous greedy packing for all
sufficiently large `m`; no independence between forbidden events is used.

## 4. Clipped residence

For a low path, a `K`-coordinate occupies

\[
 [s-h+1,s]\cap[0,q-1].
\]

If this run meets neither endpoint, it has length exactly `h>=d+1`.
Every trace coordinate occupies the full path.  In a high geodesic, core
coordinates occupy the full path, `X`-coordinates have initial runs, and
`Y`-coordinates have terminal runs, so there is no internal positive run.
The two-owner ring hinges are clipped-resident vacuously.  These are only
path-internal statements; global cyclic residence remains outside the
theorem, as its scope section says.

## 5. All-width upper transport

The exact damage-cone theorem says that an old upper value which is not
retained by the unchanged/permuted channel lies in `mathcal D_3`.  The
three size-two members survive by the ring permutation.  Every larger
member has an unchanged private path whose full owner union is that target.
Thus every upper target that existed before the switch still exists after
it, provided the ambient carrier was upper-complete before the switch.

Planting `P_3` alone does not imply that targets outside `mathcal D_3`
were present initially.  The original wording of Theorem 5.1 therefore
overclaimed.  After adding the upper-completeness hypothesis, the proof is
valid.  “At every rank and width” was also ambiguous: the theorem preserves
the upper deck at all ranks without restricting witness width; it does not
assert that every target occurs at every possible interval width.

## 6. Exact scope retained

The corrected theorem proves a conditional zero-cost rethread with:

- exact strict-lower multiset transport;
- survival of the protected owner and immediate palettes;
- survival of every upper target in an initially upper-complete carrier;
- a pairwise resource-disjoint, `d`-clipped reservoir of size `o(W)`.

It does **not** prove protected-factor extension, global cyclic residence,
the background compiler, one typed common-cap state, or regeneration.
