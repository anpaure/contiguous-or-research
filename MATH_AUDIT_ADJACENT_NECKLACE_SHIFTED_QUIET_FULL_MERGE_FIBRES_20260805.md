# Audit: shifted-quiet full-merge fibres

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_ADJACENT_NECKLACE_SHIFTED_QUIET_FULL_MERGE_FIBRES_20260805.md`
  
**Method:** local word replay, orbit dictionary, and exact Burnside count;
no search  
**Verdict:** PASS.  The theorem is a reduction and a scoped no-go for
fibrewise exits, not a no-go for the full graph.

## 1. Local merge audit

Every exceptional long run ends in `(odd,2,0)`.  Distinct long blocks have
disjoint terminal and following-zero coordinates, so replacing every
`2,0` by `1,1` is simultaneous and mass-preserving.  The former terminal
indices recover all reverse replacements.  Rotation carries terminal
indices to terminal indices, validating the quotient statement.

The theorem defines `Adm(B)` by the exact shifted-quiet block grammar.  It
does not replace that grammar by the false assertion that arbitrary
locally disjoint cuts always compose.

## 2. All-one fibre audit

For `B=1^q`, cuts at cyclic distance one have overlapping replacements.
Cuts at distance two create a singleton terminal `2` between consecutive
zeroes, outside the exceptional long-run grammar.  Distance at least three
creates a run of length at least two of the form

\[
                         (1,\ldots,1,2),
\]

which satisfies the backwards `(odd,1)` pairing, with a free leading one
when the length is odd.  Thus “nonempty cyclic gaps at least three” is both
necessary and sufficient.

The empty set is correctly excluded: it gives `1^q`, which has no zero and
is not a boundary composition.

## 3. Gap-composition dictionary

For `k` cuts, subtracting three from each cyclic gap gives a weak
composition of `q-3k` into `k` parts.  Choosing a different first cut
rotates those parts.  Conversely every such composition reconstructs one
cut necklace.  Therefore the layer is exactly `N_(k,q-3k)`, with no
reflection quotient and no stabilizer weight.

## 4. q=15 count audit

The five layer counts are:

\[
\begin{array}{c|c|c}
k&\text{weak-composition data}&\text{orbit count}\\ \hline
1&(12)&1\\
2&a+b=9\text{ modulo swap}&5\\
3&a+b+c=6\text{ modulo }C_3&(\binom82+2)/3=10\\
4&a+b+c+d=3\text{ modulo }C_4&\binom63/4=5\\
5&\text{all zero}&1.
\end{array}
\]

For `k=4`, a half-turn-fixed tuple has even total and a quarter-turn-fixed
tuple has total divisible by four, so no nonidentity element fixes total
three.  This validates the division by four.

The toggle bipartition is therefore `12` versus `10`, proving matching
deficiency at least two in that subgraph.

## 5. Scope audit

An ambient adjacent transfer can change the merged base, and an
alternating path through eliminated allocation vertices can induce a
Schur-complement entry absent from the first-order toggle graph.  The
parity obstruction applies only when these cross-base resources are
discarded.  The theorem states this limitation explicitly.

The result therefore proves exactly:

\[
 \boxed{\text{full merging partitions, but independent fibre matching is
 insufficient.}}
\]

