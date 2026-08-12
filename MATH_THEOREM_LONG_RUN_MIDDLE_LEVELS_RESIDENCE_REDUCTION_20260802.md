# Long-run Middle Levels cycles and exact residence

**Date:** 2026-08-02  
**Status:** unconditional equivalence for the residence row of an odd
middle-layer carrier.  Immediate-lower ownership is automatic.  Immediate
upper colours, deeper upper shadows, the source factor, and the lower
compiler are not asserted here.

## 1. Setup

Let `k=2r-1`, and write an oriented Hamilton cycle of the Middle Levels
graph alternately as

\[
 T_0,X_1,T_1,X_2,\ldots,T_{W-1},X_0,T_0,
 \qquad W=\binom{k}{r},
\]

where every `T_i` has rank `r` and every `X_i` has rank `r-1`.  Put

\[
 p_i=T_i\setminus X_{i+1},\qquad
 q_i=T_{i+1}\setminus X_{i+1}.
 \tag{1.1}
\]

Thus the two bit flips between consecutive rank-`r` owners are

\[
       T_i\xrightarrow{\ p_i\ }X_{i+1}
           \xrightarrow{\ q_i\ }T_{i+1},                \tag{1.2}
\]

with `p_i` a deletion and `q_i` an insertion.  The projected owner cycle is

\[
                    T=(T_0,\ldots,T_{W-1}).              \tag{1.3}
\]

For two occurrences in the cyclic flip sequence

\[
             p_0,q_0,p_1,q_1,\ldots,p_{W-1},q_{W-1},     \tag{1.4}
\]

their forward position distance is the positive number of flip steps from
the first occurrence to the second.

## 2. Exact flip-gap formula

### Theorem 2.1 (insertion-to-deletion gap equals owner residence)

Fix a coordinate `x`.  Suppose `q_i=x`, and let `p_j=x` be the next
occurrence of `x` in the cyclic flip sequence.  Then the positive run of
`x` in the projected owner cycle is

\[
                   T_{i+1},T_{i+2},\ldots,T_j,           \tag{2.1}
\]

and has length

\[
       j-i=\frac{\operatorname{dist}(q_i,p_j)+1}{2}.      \tag{2.2}
\]

Consequently the projected owner cycle is depth-`d` resident if and only if

\[
 \boxed{\operatorname{dist}(q_i,p_j)\ge 2d+1}
 \tag{2.3}
\]

for every insertion flip `q_i` and the next deletion flip of the same
coordinate.

#### Proof

After the insertion `q_i=x`, the first rank-`r` owner containing `x` is
`T_{i+1}`.  A bit in a binary cycle alternates between insertion and
deletion, so it remains present until the next `x`-flip, namely `p_j`.
That deletion is taken from `T_j`, and hence (2.1) is the complete positive
run.  In (1.4), `q_i` is followed by

\[
 p_{i+1},q_{i+1},\ldots,p_j,
\]

so its position distance to `p_j` is `2(j-i)-1`.  Rearranging gives (2.2),
and (2.3) is precisely the requirement that every positive run have at
least `d+1` owners.  \(\square\)

### Theorem 2.2 (the dual zero-run formula)

If `p_j=x` and `q_l=x` is the next occurrence of `x`, then the zero run in
the owner cycle has length

\[
       l-j=\frac{\operatorname{dist}(p_j,q_l)-1}{2}.      \tag{2.4}
\]

Thus simultaneous positive and negative depth-`d` residence is equivalent
to (2.3) together with

\[
       \operatorname{dist}(p_j,q_l)\ge 2d+3.             \tag{2.5}
\]

The proof is identical: the absent owners are
`T_{j+1},\ldots,T_l`.

## 3. A clean sufficient classical-looking target

Call a cyclic Gray code **`g`-long-run** when any two consecutive flips of
the same coordinate have cyclic position distance at least `g`.  Theorems
2.1--2.2 immediately give:

### Corollary 3.1

An oriented `(2d+1)`-long-run Middle Levels Hamilton cycle projects to a
depth-`d` resident rank-`r` Johnson cycle.  A `(2d+3)`-long-run cycle gives
both positive and negative depth-`d` residence.

Every rank-`(r-1)` target occurs exactly once as a consecutive intersection,
because

\[
                         T_i\cap T_{i+1}=X_{i+1}.         \tag{3.1}
\]

Hence a long-run Middle Levels theorem would close the owner, immediate
lower-palette, topology, and residence rows simultaneously.

For the OR problem the required gap is only

\[
                       2d(k)+1=\Theta(\sqrt{k}),          \tag{3.2}
\]

far below the trivial alphabet ceiling `k`.  This is the precise analogue,
inside the Middle Levels graph, of long-run binary Gray codes.  The known
full-hypercube theorem of Goddyn--Gvozdjak gives bit runs of length
`k-O(log k)` in `Q_k`, but it does not by itself restrict to the two middle
levels.  The missing external-style theorem is therefore:

> **Long-run Middle Levels lemma.**  For every sufficiently large odd `k`,
> the Middle Levels graph has a Hamilton cycle whose same-coordinate flip
> distance is at least `2d(k)+1`.

This lemma is sufficient for residence, but not for the whole OR problem.
The union colour on projected edge `i` is

\[
        T_i\cup T_{i+1}=X_{i+1}\cup\{p_i,q_i\},          \tag{3.3}
\]

so rank-`(r+1)` surjectivity is an additional decoration.  Ranks above
`r+1`, literal source factorization, and lower common-cap compilation remain
separate gates.

## 4. Exact finite-search consequence

For an occurrence-labelled Middle Levels factor, residence blockers need
not be expressed as set unions.  It is enough to forbid every oriented
transition-label motif

\[
 q_i=x,\quad p_j=x,\quad 1\le j-i\le d.                 \tag{4.1}
\]

This is exactly the positive short-run family; no stronger all-pairs label
separation is required.  The condition is stable under cutting precisely
when it holds cyclically.  It therefore supplies a smaller independent
validator and a transition-label CEGAR interface for the `k=17,d=3`
carrier search.

The independent implementation
`scratch/audit_middlelevels_flip_gaps_20260802.cpp` (SHA
`e6d2c4bffb727a685acccdc116818ae128424372e67fe68d31b2f4588bd297ec`)
computes both sides separately.  It reproduces `5,372` short positive runs
on the connected `c68b.double_fusion` factor and `4,029` on
`paired_escape005`, with exact flip-gap/direct-run agreement in both cases.
