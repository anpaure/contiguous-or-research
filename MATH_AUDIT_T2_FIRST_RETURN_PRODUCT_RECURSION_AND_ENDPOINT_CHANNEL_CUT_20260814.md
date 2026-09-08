# Hostile audit of the `T2` first-return product recurrence and endpoint-channel cut

**Date:** 2026-08-14

**Audited source:**
`MATH_REDUCTION_T2_FIRST_RETURN_PRODUCT_RECURSION_AND_D9_SIX_CHANNEL_PORT_OBSTRUCTION_20260814.md`

**Verdict:** **PASS in the narrowed scope stated by the source.**  The note
proves an all-`s` suffix-label product-tree recurrence, identifies the frozen
`D5` tree as its `s=5` instance, proves the growing-degree obstruction for
the fixed zigzag bridge port, and gives a canonical cross-split matching
with an exact context-independent MSW rank signature.  It does not claim an
all-`s` actuator/resource compiler.  The Proskurowski--Ruskey Hamilton path
is correctly separated as an abstract degree-two topology escape, so the
growing-port theorem is not presented as a no-go for all suffix trees.

## 1. Claims checked

### 1.1 Product-tree edge count and connectivity

In split block `(i,j)`, the left-fibre copies contribute

\[
 \operatorname {Cat}_j(\operatorname {Cat}_i-1),
\]

and the single right-child copy at `U=P_i` contributes

\[
 \operatorname {Cat}_j-1.
\]

Their sum is `Cat_i Cat_j-1`, and the construction is connected because
the right-child copy meets every left fibre at its `U=P_i` vertex.  Adding
one bridge between every consecutive pair of the `s` first-return blocks
gives

\[
 \sum_{i+j=s-1}(\operatorname {Cat}_i\operatorname {Cat}_j-1)+(s-1)
 =\operatorname {Cat}_s-1.
\]

Thus the connectivity/count proof really gives a tree; acyclicity is not
being inferred from the quotient alone.

Every child edge remains a two-coordinate transposition after context
insertion.  The bridge words

\[
 1Q_i0\,10Q_{j-1},\qquad1Q_i\,10\,0Q_{j-1}
\]

differ only in coordinates `2i+2,2i+3`.  Hence the recurrence lies in the
specified Dyck transposition graph.

### 1.2 Exact `D5` identification

With the frozen `D3/D4` trees and the unique `D2` edge, the five block
counts are

```text
13, 4, 3, 4, 13,
```

so there are `37` internal edges and four bridges.  These decompose exactly
as `26 child_D4`, `8 child_D3`, `3 child_D2`, and `4 split_bridge`, matching
the frozen 41-edge builder.  The four generated zigzag bridges agree
literally with the four frozen words.  No actuator rows are transported by
this identification; the source says this explicitly.

### 1.3 Zigzag degree and channel pigeonhole

The frozen seeds have `deg_T3(Q3)=1` and `deg_T4(Q4)=2`.  In every later
split-zero block, the right-child copy transfers all incidences of
`Q_(s-1)` to `Q_s=10Q_(s-1)`, and the first quotient bridge adds one more.
No other constructor meets `Q_s`.  Thus

\[
                         \deg_{T_s}(Q_s)=s-2.
\]

Every endpoint-anchored circuit incident with a suffix root consumes one
distinguished prefix owner over that root.  Owner-disjoint circuits on two
incident suffix edges cannot reuse the same prefix owner, even if mixed
channels at the other endpoints are allowed.  Therefore `k` endpoint
channels force degree at most `k`.  The thresholds in the source are exact:

```text
four-channel frozen-D5 phase set: first forced failure at s=7 (degree 5)
all six changed T2 prefix owners: first forced failure at s=9 (degree 7).
```

This is a terminal-owner cut for the fixed product recurrence.  It says
nothing about non-anchored circuits or a different suffix tree.

### 1.4 Cross-split matching and rank signature

For every `U in D_i` and `W in D_(j-1)`, the pair

\[
 x=1U0\,10W,
 \qquad
 y=1U\,10\,0W
\]

is a cross-split Johnson edge.  Either endpoint recovers `U,W`, so these
edges form a matching of size `Cat_i Cat_(j-1)`.  The source correctly does
**not** call it the complete interface; extra cross-split transpositions
already occur in `D3`.

The four-rank calculation is also correct.  In `x`, the closing coordinate
`p=2i+2` is the first insertion of the primitive factor, and the first upstep
`q=2i+3` of the following `10` is deletion number `i+2`.  In `y`, use

\[
 \mu(U10)=10\mu(U),
 \qquad
 \rho(10\mu(U))=(2,1,2+\rho(\mu U)).
\]

The images of `2,1` are respectively the first deletion `p` and second
insertion `q`.  Hence

\[
 (d_x(q),i_x(p),d_y(p),i_y(q))=(i+2,1,1,2),
\]

independent of `U,W`.  The separate stem-core sign diagnostic follows from
the previously proved intrinsic rank criterion and is not mislabelled as a
post-`T2` q2-current theorem.

## 2. Hostile scope checks

The following stronger readings are false or unproved and are excluded by
the final source text.

1. **Not an all-tree obstruction.**  The Proskurowski--Ruskey theorem gives
   a transposition Hamilton path on `D_s`, hence maximum degree two.  The
   source uses this only as a suffix-label topology escape.  It does not
   claim that the PR edges admit compatible actuator circuits.
2. **No rotating-port SDR yet.**  The matching aperture supplies many local
   bridge choices, but the source does not prove a joint bounded-load choice
   together with the right-fibre anchors across the full recursion.
3. **No coordinate transport.**  The frozen context-conjugation no-go still
   applies.  The product formula on suffix labels is not a Boolean injection
   of the frozen `D3/D4` circuit resources.
4. **No closed-package shortcut.**  A local closed reset cycle is not a
   rowwise substitution theorem.  The source now requires exposed boundary
   darts, exact suppression to the prescribed factor wiring, globally
   disjoint owner/q1 palettes, and composable boundary monodromy.
5. **No automatic component action.**  A suffix-label tree and proper
   endpoint colouring do not force the simultaneous lifted toggle to have
   one output.  The component permutation remains part of the circuit
   signature and must be verified, as it was at `D5`.

These restrictions leave the exact all-semilength gate at a fresh
non-conjugate reset compiler on some bounded-degree suffix tree, with global
owner/q1 disjointness, aggregate q2 support, and one-orbit component action.

## 3. Independent H100 replay

The independent verifier rebuilds the recurrence from the frozen `D3/D4`
edge lists and checks through `D9`:

* tree connectivity and the exact `Cat_s-1` count;
* the literal `D5` role census and four bridges;
* the degree sequence `deg(Q_s)=s-2` through the six/seven threshold;
* canonical matching inclusion, size, and endpoint injectivity through
  `D8`; and
* the four-rank signature for every enumerated matching member through
  `D8`.

It reports

```text
STATUS PASS
D5_ROLE_TOTALS child_D4=26 child_D3=8 child_D2=3 split_bridge=4
SIX_CHANNEL_CUT first_failure_semilength=9 zigzag_degree=7
```

All execution and hashes were performed through `ssh h100`.  The bound
through `D8/D9` is supporting finite replay; the all-`s` claims rest on the
symbolic proofs audited above.

| artifact | H100 SHA-256 |
|---|---|
| source theorem | `48edf0ef101c11a504bd9aee425f90ddb843e11b9dd161f7f7b458224e8be0a0` |
| independent verifier | `72b556a9cda826d0ab38eb64bb866b2a49bac14338fb409df0e56398bb11cdf5` |
| H100 output | `bb0dc5b8d0266c815253c82832679db2cd5a7c943fa0655dc41c65fa95fe9e99` |

The source theorem and verifier/output are safe to freeze together in this
scope.
