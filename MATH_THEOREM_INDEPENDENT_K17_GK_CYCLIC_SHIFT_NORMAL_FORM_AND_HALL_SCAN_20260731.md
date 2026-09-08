# Independent K17 cyclic-cut GK normal form and supported-ear audit

Date: 2026-07-31  
Verdict: **GO** for the complete `p_0/p_s` structural family, its scalar
telescope, its all-width rainbow property, and the first supported-ear Hall
projection.  The old half-rotation seed (`s=8`) is genuinely blocked in that
projection, whereas `s=1` and `s=16` pass it exactly.  **This is not yet an ear
packing or a length-24313 word.**

## 1. The two-cut family

For a rank-six word `C` on the cyclically ordered set `[17]`, let `p_t(C)` be
the last position at which the prefix walk, scanned from `t`, is at its
maximum.  This position is a zero.  When `p_0(C) != p_s(C)`, put an edge

\[
 C+p_0(C)\quad--\quad C+p_s(C)                         \tag{1.1}
\]

between rank-seven sets.  Write `F_s` for the resulting graph.

An independent exact enumeration confirms the following table.  The last
four columns refer to the greatest locally supported endpoint/unused-edge
relaxation, followed by the missing-rank-six versus fresh-rank-eight Hall
projection.

| `s` | base edges | vertices | components | turns | unused rank 7 | missing rank 6 | provider rank | deficiency |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 3,640 | 7,280 | 3,640 | 0 | 12,168 | 8,736 | **8,736** | **0** |
| 2 | 5,278 | 8,918 | 3,640 | 1,638 | 10,530 | 7,098 | 6,459 | 639 |
| 3 | 6,916 | 11,557 | 4,641 | 2,275 | 7,891 | 5,460 | 5,208 | 252 |
| 4 | 7,982 | 12,623 | 4,641 | 3,341 | 6,825 | 4,394 | 3,794 | 600 |
| 5 | 8,916 | 13,975 | 5,059 | 3,857 | 5,473 | 3,460 | 3,199 | 261 |
| 6 | 9,520 | 14,579 | 5,059 | 4,461 | 4,869 | 2,856 | 2,365 | 491 |
| 7 | 9,956 | 15,180 | 5,224 | 4,732 | 4,268 | 2,420 | 2,046 | 374 |
| 8 | 10,152 | 15,376 | 5,224 | 4,928 | 4,072 | 2,224 | 1,780 | 444 |

Thus the best seed for *base size* is the old `s=8` half-rotation forest, but
the unique best seed for the first immutable-ear feasibility gate is the
opposite extreme `s=1` (and its rotation mate `s=16`).  This is a genuine
changed-seed route, not a repair of the old seed.

## 2. A uniform path and all-width theorem

The structural assertions above admit a clean proof; they are not merely a
finite `k=17` observation.

### Lemma 2.1 (local `01` normal form)

For a linear binary word, greedily match every zero with a later one, using
the usual stack.  Equivalently, repeatedly cancel adjacent `01` pairs.  The
unmatched positions have the form

\[
 1^a0^b.                                                   \tag{2.1}
\]

The first unmatched zero is exactly the last-maximum pivot.  Flipping that
zero to one preserves every matched pair and changes (2.1) to
`1^(a+1)0^(b-1)`.

### Lemma 2.2 (two-arc component normal form)

Split the coordinates into the two linear arcs

\[
 A=[0,s-1],\qquad B=[s,16].                              \tag{2.2}
\]

After cancelling `01` pairs separately on the two arcs, write the unmatched
words of a rank-six set as

\[
 A:1^a0^b,\qquad B:1^c0^d.                              \tag{2.3}
\]

In the scan `AB`, the leading unmatched ones of `B` cancel the trailing
unmatched zeros of `A`.  Hence `p_0` lies in `A` exactly when `b>c`.  Likewise
`p_s` lies in `B` exactly when `d>a`.  The alternative unequal case would
require both `b<=c` and `d<=a`, contradicting

\[
 (a+c)-(b+d)=2|C|-17=-5.                                \tag{2.4}
\]

Consequently, whenever the two pivots differ,

\[
 p_0(C)\in A,\qquad p_s(C)\in B.                        \tag{2.5}
\]

Both endpoints of (1.1) have the same two local matching signatures.  If
`alpha` and `gamma` are their numbers of unmatched ones on `A` and `B`, an
oriented edge changes

\[
 (\alpha,\gamma)\longmapsto(\alpha-1,\gamma+1).          \tag{2.6}
\]

To see that no states are skipped, let `h_A=a+b`, `h_B=c+d`, and
`h=alpha+gamma`.  For the edge leaving `(alpha,gamma)`, the two inequalities
above become

\[
 h_A+1>h,\qquad h_B+1>h,                                  \tag{2.7}
\]

which are independent of the state along the signature class.  Thus each
nontrivial signature class is one full interval of consecutive states, hence
a path, and these paths are exactly the components of `F_s`.  In particular,
no cycle is possible.

### Theorem 2.3 (all-width rainbow)

Every union of `w` consecutive vertices inside the paths of `F_s` has rank
`6+w`, and these unions are globally distinct, for every `s`.

**Proof.**  On one component the two local matching signatures are fixed,
and the vertices have coordinates

\[
  (\alpha,\gamma),
  (\alpha-1,\gamma+1),\ldots .                           \tag{2.8}
\]

The union of a `w`-vertex window retains the first vertex's `A` part and the
last vertex's `B` part.  It therefore has `7+(w-1)=6+w` elements.

More importantly, applying local `01` cancellation to the union recovers
both fixed matching signatures, the first value `alpha`, and the last value
`gamma+w-1`.  Its rank determines `w`, so it recovers the first `gamma` and
therefore every pair in (2.8).  The entire window is uniquely reconstructed
from its union.  Hence two windows cannot share a colour.  QED.

This supplies the previously missing symbolic proof of rank-eight,
rank-nine, and arbitrary internal-width injectivity for the entire cyclic
second-cut family.

## 3. Rotation symmetry

Let `R_delta` rotate coordinates by `delta`.  Pivot equivariance gives

\[
 p_t(R_\delta C)=R_\delta p_{t-\delta}(C).               \tag{3.1}
\]

Taking `delta=-s`, the cuts `(0,s)` become `(17-s,0)`.  The two undirected
rails in (1.1) swap, so `F_s` and `F_(17-s)` are literally isomorphic.  The
isomorphism preserves intersections, unions, endpoint turns, supported
wedges, the support peel, and the provider graph.  It explains the exact
pairing

```text
1<->16, 2<->15, ..., 8<->9.
```

## 4. The scalar telescope is independent of the shift

Let a seed forest have `e` edges, `v` vertices, `c` components, and
`t=v-2c` internal turns.  A final tail path on 16,911 rank-seven vertices
requires

\[
 I=16911-v                                                     \tag{4.1}
\]

inserted vertices and `c-1` joining ears.  Therefore it has exactly

\[
 I+c-1=16910-e                                                \tag{4.2}
\]

new edges.  The number needed for missing rank-six colours is `12376-e`,
so the repeated-rank-six/rank-five payload is always

\[
 (16910-e)-(12376-e)=4534.                                   \tag{4.3}
\]

Similarly the new-turn count is

\[
 I+2(c-1)=16909-t.                                           \tag{4.4}
\]

After a rainbow completion, the unused global palettes are consequently

\[
 \binom{17}{8}-16910=7400,\qquad
 \binom{17}{9}-16909=7401,                                  \tag{4.5}
\]

exactly the prefix allocations.  None of these identities favours `s=8`;
changing the cut redistributes the work between the seed and its ears while
leaving the complete ledger invariant.

For `s=1`, the seed is simply 3,640 disjoint edges.  It requires 9,631
inserted rank-seven vertices and 3,639 ears, hence 13,270 new edges.  Of
those, 8,736 carry the missing rank-six colours and 4,534 carry the repeated
rank-six/rank-five payload.

## 5. What the `s=1` Hall pass does and does not prove

Two independent implementations reconstruct the greatest locally supported
edge/wedge fixed point for `s=1`:

```text
raw candidate edges                 458,934
active supported edges              454,930
active compatible wedges         20,772,564
missing rank-six rows                 8,736
fresh rank-eight provider colours    13,817
provider incidences                  272,992
zero rows                                  0
matching rank                       8,736 / 8,736
```

The materialized matching contains 8,736 distinct missing rank-six colours
and 8,736 distinct fresh rank-eight colours.  It proves that the immutable
`s=1` seed escapes the exact Hall obstruction that kills every `s=2,...,15`.

It does **not** yet select a physical ear family.  In fact, the arbitrary
Hopcroft--Karp matching is not physically usable as chosen:

```text
old-endpoint overload units          814
unused-vertex overload units         542
degree-two incompatible wedges       233
```

These are defects of that matching, not an impossibility theorem.  The next
exact gate is a **joint capacitated provider transversal**:

* one provider edge for every missing rank-six colour;
* each fresh rank-eight colour used at most once;
* each old endpoint used at most once;
* each unused rank-seven vertex used at most twice;
* when used twice, its two edges form a compatible fresh rank-nine wedge.

Only after that gate passes should one impose path packing, component-tree
topology, the remaining 4,534 repeated-colour edges, and global rank-nine
freshness.  Thus `s=1` is the first viable changed seed, not yet a completed
tail.

## 6. Reproducibility

The independent local-signature audit is

```text
scratch/audit_independent_k17_gk_cyclic_shift_family_20260731.py
  SHA-256 3822f05979bb85da4c1837e67f371688b7b4cb10a684a2dc082795eeff37b8be
scratch/independent_k17_gk_cyclic_shift_family_20260731.audit.json
  SHA-256 fd8f804c06ac44fa23cdeb8e71a1e0ea1fed3c2b7f60b81fc525394226d9ef84
  canonical payload ab812572d5c4712b530b31ea8506713db3c9ffb5d481001e6afb86bd11bd058a
```

The audited H2 aggregate on which the supported-ear table is replayed is

```text
scratch/h2_k17_cyclic_supported_hall_20260731.audit.json
  canonical payload 044596de5e7f854b999e4eedef85aa5ceb06e645ca5f3a8ad4b21b6644eeaaec
```

Scope exclusion: no prefix, upper continuation, completed tail, universal
word, or assertion `nu(17)=24313` follows from this note.
