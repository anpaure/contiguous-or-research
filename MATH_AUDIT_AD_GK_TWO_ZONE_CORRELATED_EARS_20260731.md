# Independent audit of the GK correlated-ear/common-bank theorem

Date: 2026-07-31  
Lane: AD independent arithmetic and proof audit  
Verdict: **PASS** for the exact obstruction and conditional theorems; no
`k=17` completion is certified.

## 1. Authenticated base

The current broad producer reconstructs the two-cut Greene--Kleitman forest
without using the proposed completion.  The replay verifies

\[
 (c,v,e,t)=(5224,15376,10152,4928),                    \tag{1.1}
\]

where `c` is the number of path components, `v` the rank-seven owners, `e`
the rank-six edges/distinct rank-eight unions, and `t` the distinct internal
rank-nine turns.  The identities `v-e=c` and `v-2c=t` pass.

From the path-size histogram, independent summation of `max(s-w+1,0)` gives
the all-width protected bank

\[
\begin{array}{c|rrrrrrr}
w&2&3&4&5&6&7&8\\\hline
N_w&10152&4928&1888&564&116&17&1.
\end{array}                                             \tag{1.2}
\]

The product-chain formula in the theorem independently proves both the
ranks and injectivity, so (1.2) is not used as an unexplained measurement.

## 2. Short-ear obstruction

There are exactly `2224` missing rank-six colours.  Of these, `674` have no
original endpoint superset.  Every occurrence of one of those `674` colours
must lie on an internal--internal ear edge.  Therefore

\[
                  \sum_{j\ge3}(j-2)x_j\ge674.          \tag{2.1}
\]

For `(x_1,x_2,x_3,x_4)=(4024,905,252,42)`, the left side is

\[
                         252+2(42)=336,                 \tag{2.2}
\]

so the proposed mix is impossible, independently of any solver.  The full
local split is `266` clean length-three, another `128` clean length-four,
and `280` unresolved through length four.  The old `252+42` split applies
only to the `294` all-unused subfamily.

The owner budget gives `I=1535`.  Since the number `b` of non-direct ears
satisfies `I-b>=674`, every intact completion has `b<=861` and hence at
least `4362` direct ears.  The scalar point `(4362,187,674)` meets these
equations but fails the local palette census; it is not a construction.

If `s` old edges are cut, at most `2s` newly exposed endpoint slots can
service formerly endpoint-free colours.  Thus

\[
             \sum_{j\ge3}(j-2)x_j+2s\ge674.            \tag{2.3}
\]

Keeping only the `336` displayed internal-core positions forces `s>=169`.
No `380`-row cut matching is authenticated, so the audit records only this
necessary scalar bound.

## 3. Mix-independent complement ledger

The two equations

\[
 \sum_jx_j=5223,\qquad\sum_j(j-1)x_j=1535             \tag{3.1}
\]

force `6758` new edges and `11981` new turns for every ear-length
distribution.  Hence the exact owner/rank-eight/rank-nine complements are

\[
                         2537,7400,7401.                \tag{3.2}
\]

The rank-nine row is mixed-width: `7399` prefix triples, two crossing
triples, and `16909` tail quadruples.  The obsolete `7398+3` uniform
four-window account is not used.

Only `2224` new intersections introduce missing geometric rank-six colours.
The other

\[
                         16910-12376=4534               \tag{3.3}
\]

are repeats and must carry distinct rank-five payloads.  Two boundary
letters give `4536`.  Under pairwise vertex-disjoint internal cuts, both the
missing geometric-colour count and new-edge count rise by `s`, so (3.3)
remains invariant.

## 4. Hall, chronology, and C6 scope

The capacitated Hall inequalities

\[
 \sum_{D\in X}(m_D-1)\le
 \left|\bigcup_{D\in X}\partial_5D\right|              \tag{4.1}
\]

are necessary and sufficient for an **independent** rank-five payload
assignment.  For a fixed match `S=D-g` and oriented owners `D+x,D+y`, the
twenty ordered choices of distinct `a,b in S` give the displayed local
diamond.  Adjacent diamonds share literal source letters, so (4.1) is not a
chronology theorem.

A standard fixed-four suspended C6 equality preserves geometric rank-six,
rank-eight, and named owner-slot resources.  It does not preserve the
rank-five payload coordinate unless that coordinate is explicitly included.
Likewise it changes local rank-nine turns and may change endpoint/root state.
The theorem's private-bank and serial-telescope conclusions correctly carry
all of those rows as hypotheses.

The guard census distinguishes `54` literal guard letters from only `9`
rank-nine owner colours.  No degree or Hall estimate uses `54` as a palette
degree.

## 5. Exact remaining gate

The proved constructive mechanism is conditional:

* variable-length ears amortize two old ports across many endpoint-free
  service colours;
* intact GK components preserve the full bank (1.2);
* compatible C6 fragments can telescope their internal slot debts into one
  two-port serial ear; and
* zero-flux tail/prefix packet pairs preserve the common-bank interface.

The source contains no full long-ear columns, planted C6 off phases, or
boundary signatures.  Simultaneous ear packing, the prefix path, seam
windows, higher upper intervals, residence, and compiler remain open.

## 6. Reproducibility

The independent replay is

```text
scratch/audit_ad_gk_two_zone_correlated_ears_20260731.py
scratch/ad_gk_two_zone_correlated_ears_20260731.audit.json
```

The latter has canonical payload

```text
3cfe1c7a0be68d1983670694270585e964b8f885bba80dcde52136c5f4babf61
```

Final file SHA-256 values are frozen in the theorem footer and handoff item.
