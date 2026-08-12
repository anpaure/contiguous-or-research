# Exact audit of the `k=17` two-cut Greene--Kleitman forest

Date: 2026-07-31  
Status: **PASS, exactly for Section 4 of
`PROPOSED_K17_TWO_ZONE_GK_EAR_CONSTRUCTION_20260731.md`**

This note does not audit or imply either ear-completion gate in Sections
5--6.

## 1. The pivot convention

Coordinates are `0,...,16`.  At a chosen cut, scan cyclically, assigning
step `+1` to a coordinate in the rank-six set \(C\) and step `-1` to a
coordinate outside \(C\).  Prefix time zero participates.  If \(t_*\) is
the **last prefix boundary** at which the maximum height is attained, the
pivot is the coordinate immediately following that boundary.  Thus the two
orders are

```text
0,1,...,16
9,10,...,16,0,1,...,8.
```

This boundary convention matters.  The pivot is not the last included
coordinate at a maximum.  It is the next coordinate, indexed by the
maximizing boundary.  It is the unique convention compatible with both
\(C+p_s(C)\) and the seven asserted reflection rows.

The total walk height is \(2(6)-17=-5\).  Hence its last maximum cannot be
the terminal prefix, and the following step is a downstep.  The pivot is
therefore absent from \(C\), as required by an upward map.

## 2. Each cut gives an injective upward map

Fix either cut.  Let \(S_t\) be the prefix walk, \(M\) its maximum and
\(t_*\) its last maximum.  The pivot step goes from \(M\) to \(M-1\).
After changing that step from absent to present, the new walk is unchanged
through \(t_*\) and is two higher thereafter.  It first attains its new
maximum \(M+1\) at the pivot and never exceeds \(M+1\), because every old
prefix after the last maximum was at most \(M-1\).

Thus the inverse deletes the step at the **first** maximum of the image
walk.  This is a constructive inverse, not a cardinality argument.  It proves
both cut maps injective.  The literal audit separately obtains `12376`
different images from the \(\binom{17}{6}=12376\) inputs for each cut.

## 3. Exact distinct-pivot condition and reflection count

Split the word as \(AB\), with \(A\) on coordinates `0,...,8` and \(B\) on
`9,...,16`.  Let \(a=|C\cap A|\), let

\[
 s=2a-9,
\]

and let \(m_1,m_2\) be the maximum prefix heights of the two pieces,
including the initial zero.

In the order \(AB\), the last global maximum lies in \(A\) precisely when
\(m_1>s+m_2\); equality belongs to the later piece \(B\).  In the order
\(BA\), whose first-piece displacement is \(-5-s\), the last maximum lies
in \(B\) precisely when

\[
 m_2>(-5-s)+m_1.
\]

Both strict inequalities hold exactly when

\[
 1\le m_1-(2a-9)-m_2\le4.                 \tag{3.1}
\]

If the expression is at most zero, both cuts select the same pivot in
\(B\); if it is at least five, both select the same pivot in \(A\).
Therefore (3.1) is equivalent to distinct pivots.  In the distinct case
\(p_0(C)\in A\) and \(p_9(C)\in B\), so in fact

\[
 p_9(C)>p_0(C).                            \tag{3.2}
\]

On its natural support
\(\max(0,2p-\ell)\le m\le p\), reflection gives the number of length
\(\ell\) walks with \(p\) upsteps and maximum exactly \(m\):

\[
 g_{\ell,p}(m)
 =\binom{\ell}{p-m}-\binom{\ell}{p-m-1}.   \tag{3.3}
\]

Outside that support the count is zero; the raw binomial difference should
not be interpreted as a count there.  Summing
\(g_{9,a}(m_1)g_{8,6-a}(m_2)\) over (3.1) gives, for
\(a=0,\ldots,6\),

```text
8, 232, 1744, 4384, 3124, 624, 36,
```

and hence `10152` nondegenerate edges.  The audit independently checks the
reflection formula on every length-eight and length-nine word and checks
(3.1) on all `12376` rank-six words.  There are zero mismatches.

## 4. Product-SCD anatomy and the complete component count

The two-block view gives a human derivation of the whole forest, not merely
its edge count.  Let \(q\) and \(r\) be the bottom ranks of the segment GK
chains containing \(C\cap A\) and \(C\cap B\).  Since the maximum of a
rank-\(a\) member in a chain of bottom rank \(q\) is \(a-q\),

\[
 m_1=a-q,\qquad m_2=(6-a)-r,qquad
 m_1-(2a-9)-m_2=3-q+r.                    \tag{4.1}
\]

The numbers of length-nine chains at bottom ranks `0,...,4` are

```text
1, 8, 27, 48, 42,
```

and the corresponding length-eight counts are

```text
1, 7, 20, 28, 14.
```

For a qualifying pair \((q,r)\), an edge exists at every integer

\[
 \max(q,r-1)\le a\le\min(8-q,6-r).         \tag{4.2}
\]

These edges form one path.  The complete nonempty chain-pair table is:

| \((q,r)\) | chain-pair multiplicity | edges per path |
|---:|---:|---:|
| `(0,0)` | 1 | 7 |
| `(0,1)` | 7 | 6 |
| `(1,0)` | 8 | 6 |
| `(1,1)` | 56 | 5 |
| `(1,2)` | 160 | 4 |
| `(2,0)` | 27 | 5 |
| `(2,1)` | 189 | 4 |
| `(2,2)` | 540 | 3 |
| `(2,3)` | 756 | 2 |
| `(3,1)` | 336 | 3 |
| `(3,2)` | 960 | 2 |
| `(3,3)` | 1344 | 1 |
| `(4,2)` | 840 | 1 |

The multiplicities sum to `5224`; multiplicity times path length sums to
`10152`.  Consequently this product decomposition has

\[
 V=E+K=10152+5224=15376                 \tag{4.3}
\]

used rank-seven vertices and

\[
 \sum_P(|E(P)|-1)=E-K=4928              \tag{4.4}
\]

internal turns.

More explicitly, if \(A_j,B_j\) denote the rank-\(j\) members of the two
fixed segment chains, the edge indexed by \(a\) has endpoints

\[
 L_a=(A_{a+1},B_{6-a}),\qquad
 R_a=(A_a,B_{7-a}).                       \tag{4.5}
\]

The only cross-side identities are the intended path adjacencies
\(R_a=L_{a-1}\).  Thus the `20304` endpoint incidences are **not** all
distinct: exactly `4928` identities create the internal vertices.  What is
true, and what Section 4 asserts, is injectivity on each pivot side and no
accidental collision beyond these path adjacencies.

## 5. Rank-eight and rank-nine labels are genuinely injective

The rank-eight union of edge \(a\) is

\[
 U_a=(A_{a+1},B_{7-a}).                   \tag{5.1}
\]

Its rank on the first shore determines \(a\), and each projection belongs
to one unique segment GK chain.  Thus \(U_a\) determines the chain pair and
the occurrence edge.  Equivalently, applying the first-maximum inverse of
Section 2 separately to \(U_a\cap A\) and \(U_a\cap B\) recovers both
pivots and then \(C\).  Hence all `10152` rank-eight edge unions are
distinct.

Consecutive edges \(a,a-1\) have rank-nine turn union

\[
 H_a=(A_{a+1},B_{8-a}).                   \tag{5.2}
\]

The same shore-rank and unique-chain argument recovers \(a\), both segment
chains, the internal vertex and the two occurrence edges.  Hence all
`4928` internal rank-nine unions are distinct.  The enumerator confirms both
statements with literal collision maps storing the full records, rather than
inferring injectivity from scalar counts.

## 6. Independent graph census

The freshly reconstructed labelled graph has:

| statistic | audited value |
|---|---:|
| distinct-pivot occurrence edges | 10152 |
| used rank-seven vertices | 15376 |
| degree-one vertices | 10448 |
| degree-two vertices / internal turns | 4928 |
| path components | 5224 |
| distinct rank-eight edge unions | 10152 |
| distinct rank-nine turn unions | 4928 |

Its component-size histogram, by vertices, is

```text
2:2184, 3:1716, 4:876, 5:349, 6:83, 7:15, 8:1.
```

Every degree-two vertex is checked to have exactly one ordinary-cut and one
cut-nine incidence.  A second proof of acyclicity uses the potential
\(\sum_{x\in V}x\), which increases by \(p_9-p_0>0\) on every oriented
edge.

## 7. Verdict and scope

There is **no false claim in the audited two-cut Greene--Kleitman section**
under the boundary convention in Section 1.  The machine audit therefore
records `first_false_claim: null`.

Two precision warnings remain:

1. Formula (3.3) is a counting formula only on the feasible maximum support.
2. “Rank-seven injectivity” must mean separate-side pivot injectivity; total
   endpoint-incidence injectivity is false because the `4928` internal path
   joins are intentional.

This PASS says nothing about the proposed ear joins, prefix completion,
upper continuation, residence or compiler.

Reproducer:

```text
scratch/audit_k17_two_cut_gk_forest_20260731.py
scratch/k17_two_cut_gk_forest_20260731.audit.json
```

The independent script rebuilds the graph from bitmasks, checks the
reflection formula on all short words, retains literal collision witnesses
for every injectivity gate, traverses every component and verifies the two
constructive first-maximum inverses.
