# K16 `j3959` flat-block hereditary upper core and crosspair closure

Date: 2026-07-30  
Lane: K  
Status: **exact scoped no-go for whole-block rethreads; internal-cut repair remains open**

## 1. Statement

Consider the eleven occurrence blocks in the authenticated structurally
perfect `j3959` carrier, with lengths

\[
(2,2,6443,2,2471,6,659,1142,1243,8,895).
\]

The exact flat-block DFS found 77 orders/orientations which simultaneously

1. have exactly the three required isolated flats;
2. meet scalar capacity `26332`;
3. replay every middle row from the maximal envelope with no empty cell;
4. retain all five upper service targets
   `4e79,6f79,ca79,ea79,eb79`.

Among them, the arbitrary-upper hole histogram is

```text
20 holes   16
21 holes   47
22 holes    2
23 holes   12
```

The following stronger component theorem holds.

> **Theorem 1 (hereditary nineteen-hole core).** Nineteen upper targets are
> absent from every concatenation obtained by permuting and independently
> reversing the eleven whole blocks, whether or not that concatenation passes
> the replay/capacity tests:
>
> ```text
> 4779 477b 4f33 56d9 5753 6a79 6b79
> 8f3c 8f3e 8f7c 8f7e cf45 cf75
> da56 db56 df45 e566 f566 f766
> ```
>
> Of the twenty holes in a minimum carrier, only `7137` belongs to the
> whole-block seam alphabet.  It has precisely the two signed realizations
>
> \[
> 6F\mid5F,qquad 5R\mid6R,
> \]
>
> with the literal adjacent witness
>
> \[
> \texttt{7117}\lor\texttt{6137}=\texttt{7137}.
> \]

> **Theorem 2 (exact replay-compatible trade).** In the complete 77-carrier
> replay/capacity catalogue, the only carriers which fill `7137` are IDs 0
> and 1.  Each loses exactly
>
> \[
> \{\texttt{4ef7},\texttt{ce71},\texttt{cef7}\}.
> \]
>
> Thus the unique positive whole-block trade has signature
>
> \[
> +\{\texttt{7137}\}
> -\{\texttt{4ef7},\texttt{ce71},\texttt{cef7}\},
> \]
>
> and increases the hole count from 20 to 22.

> **Theorem 3 (crosspair closure).** The sixteen 20-hole carriers form the
> complete path closure of their own component-port seam bank.  The bank has
> 23 undirected physical port edges, including the two path ends, and admits
> exactly sixteen spanning component paths; these are precisely the original
> sixteen carriers.  Consequently no alternating-circuit recombination using
> only their seams escapes the 20-hole face.
>
> Relative to any of the sixteen minima, every exact fixed-block carrier with
> positive upper gain changes at least nine physical component seams and
> touches at least nine blocks.  Hence neither one nor two edge-disjoint
> 2-break crosspairs can have positive gain.  Even the only global positive
> rethread has the unfavorable `1-for-3` signature above.

Therefore arbitrary-upper completion is impossible in the whole-block
algebra.  A successful next move must split at least one of the eleven blocks
or change the occurrence multiset by a source-compensated trade.  This is
exactly the scope in which the new contextual 19-row collar domain is useful.

## 2. Common and variable upper structure

All sixteen minima have the same twenty-hole set: the hereditary core in
Theorem 1 together with `7137`.  They are the full signed face

```text
8F/R,
9F,7R,5R,4R,3F,2R,1F,0F fixed,
all two orders and all four orientations of blocks 6 and 10.
```

The complete 77-carrier catalogue has exactly six upper-hole classes:

| count | holes in addition to the hereditary nineteen |
|---:|---|
| 16 | `7137` |
| 33 | `4ef7,7137` |
| 14 | `7137,ce63` |
| 2 | `4ef7,ce71,cef7` |
| 5 | `4ef7,7137,cc67,cce7` |
| 7 | `7137,cc67,cce7,ce63` |

This table accounts for all 77 states and reproduces the histogram
`16,47,2,12` exactly.

The twenty minimum holes have rank profile

```text
rank 9: 10, rank 10: 7, rank 11: 3.
```

They lie in twenty distinct free lower-`Z15` orbits.  Their nontrivial
containment chains are

```text
4779 < 477b
6a79 < 6b79
8f3c < {8f3e,8f7c} < 8f7e
cf45 < {df45,cf75}
da56 < db56
e566 < f566 < f766.
```

The other rank-nine minima are `4f33,56d9,5753,7137`.

The common support does not make the face occurrence-inert.  Exact
canonical-right-end replay finds `1139` covered targets whose witness
multiplicity changes across the sixteen rows.  Exactly `16040` targets are
canonically unique in every row; only `38` change between unique and
nonunique status.  Thus the four face bits can redistribute duplicate
witness supply, but cannot create a new target.

The five named service masks each have exactly one interval witness in every
one of the 77 carriers, and all five witnesses lie wholly inside block 2.  In
reference carrier 47 their intervals are

```text
4e79  [11255,11256]
6f79  [11264,11265]
ca79  [11254,11255]
ea79  [11253,11255]
eb79  [11252,11255]
```

Thus whole-block rethreading preserves this bank literally; the upper failure
is not caused by losing any of the five service tokens.

## 3. Proof of the hereditary core

Every interval in a concatenation of whole blocks has the form

\[
\text{suffix of a left block}
\;|\;
\text{zero or more whole intermediate blocks}
\;|\;
\text{prefix of a right block}.
\]

If its OR equals a proper target `h`, every included partial OR and every
whole intermediate-block OR is a subset of `h`.

The eleven block totals are

```text
ce61 cc63 ffff 4e71 7fff 6777
7fff 7fff 7fff 77df 7fff.
```

Internal interval spectra are unchanged by reversal.  Since all twenty masks
are holes in carrier 47, none has an internal witness in a single block.
It remains only to inspect signed suffix/prefix pairs and the possible whole
intermediate blocks.

For eighteen of the nineteen hereditary masks other than `cf75`, no whole
block total can be an intermediate subset, and the exact signed
suffix/prefix table has no union equal to the target.  For `cf75`, the only
eligible whole intermediate blocks are 0 and 3.  The only relevant partial
ORs are

```text
block 0   ce61
block 2   c671   (one boundary orientation on each side)
block 3   4e71
```

and adjoining either or both eligible intermediate blocks never produces
`cf75`; every possible union is at most the wrong pattern `ce71` before an
outside bit appears.

For `7137`, the only relevant partial boundary ORs are

```text
block 6 suffix in orientation F   7117
block 5 prefix in orientation F   6137,
```

and their simultaneous reversal.  Their union is exactly `7137`.  This proves
Theorem 1.

The independent checker enumerates this decomposition directly.  At most
blocks 0 and 3 can be eligible intermediates for any of the twenty targets,
so this is a tiny exact bit-table, not a heuristic search.

## 4. Proof of the replay-compatible trade theorem

The exact DFS tries every unused block and each nontrivial orientation.  Its
capacity prune is an upper bound: if the current depth is `c`, the remaining
length is `L`, and `p` duplicate-pair blocks remain, postponing all `p` pairs
to the end gives the largest possible additional capacity

\[
cL-p^2.
\]

Expired replay rows and empty envelope cells cannot be repaired by a later
suffix.  Hence its 77 emitted replay/capacity/service states are complete for
the fixed eleven-block partition.

Independent replay reconstructs every emitted target word from its signed
block order, recomputes the forced depth schedule, checks every maximal
envelope cell and middle-row OR, compares the saved envelope word, and
recomputes all arbitrary-upper holes.

Only IDs 0 and 1 cover `7137`:

```text
ID 0  4F,3F,9F,8F,7F,6F,5F,2R,1F,0F,10F
ID 1  4F,3F,9F,8F,7F,6F,5F,2R,1F,0F,10R
```

Both have flats `2471,11974,11976` and capacity `26424`.  Their sole `7137`
witness is `[5524,5525]`, namely `7117,6137`.

In every one of the sixteen minima the three targets sacrificed by this move
have the same local witness packet:

```text
word[4867..4872] = 0ce7 4c67 4e63 4e71 4e71 c671

4ef7  [4867,4870], [4867,4871]
ce71  [4870,4872], [4871,4872]
cef7  [4867,4872]
```

No other exact fixed-block carrier fills any of the twenty minimum holes.
This proves Theorem 2.

## 5. Proof of component-bank closure

Give block `i` two physical ports `iL,iR` and include labeled path ends
`START,END`.  Form the union of the seam-edge sets of the sixteen minima.
Every connected degree-correct recombination using this bank is obtained by
starting at `START`, entering one unused block through one port, leaving
through the other port, and following another bank edge.

The exact traversal has 23 bank edges and exactly sixteen complete paths.
Their signed orders equal the sixteen minimum orders, with no extra path.
Every alternating-circuit subset from any overlay of these carriers uses only
bank edges, so a connected result is one of those sixteen paths.  This proves
the first part of Theorem 3.

Comparing each minimum against every one of the 77 exact states gives 1,232
ordered transitions.  Exactly 32 have positive gain: for each minimum, the
two endpoints are IDs 0 and 1.  They remove 9 or 10 old physical seams, add
the same number, and touch at least nine blocks.  All have gain one, loss
three.  There is therefore no positive pair of transitions with disjoint
block support, and no one- or two-crosspair positive endpoint.  This proves
the remainder of Theorem 3.

## 6. Consequence and scope

No generalized Hall audit is warranted for this catalogue: every carrier
still has at least twenty arbitrary-upper holes, and the only fixed-block
trade that fills a minimum hole worsens the total.

The independent endpoint-containment quotient gives a complementary floor.
The twenty minimum holes have 21 possible abstract new-seam signatures with
size histogram `11,6,3,1` at sizes `1,2,3,4`; exact set-union DP first covers
all twenty with ten seams.  There is a unique abstract ten-signature cover.
Its ten position domains are pairwise disjoint, but their ninety physical
positions contain only eleven old path edges.  Nine are mutually disjoint and
the remaining two form one length-two chain.  Every size-ten old-edge matching
therefore violates the forced two-endpoint quota of signature group zero.
Hence no physical ten-seam realization exists and the occurrence-level floor
is **eleven** new joins.

An edge-disjoint two-break contributes at most two new joins, so at least six
such crosspairs are necessary.  The whole-block theorem above shows that at
least one of those cuts must split a frozen block or change the occurrence
multiset.

This is a proof-safe no-go for

1. all permutations and orientations of these eleven indivisible occurrence
   blocks at the hereditary nineteen-hole level;
2. all 77 replay/capacity/service-feasible fixed-block carriers at the exact
   twenty-hole floor;
3. every alternating-circuit recombination using only the seam bank of the
   sixteen minima;
4. one or two edge-disjoint physical 2-break crosspairs within this algebra.

It does **not** exclude splitting a block, changing internal component edges,
using a different service block, or making a source-compensated occurrence
trade.  In particular it does not close the contextual 19-row collar/global
embedding lane.

## 7. Frozen artifacts

```text
scratch/search_k16_structural_flatblock_signature_dfs_20260730.cpp
SHA-256 c95192ced846ce8806c9c7310f4331ce636497e10884e3db21aa5b63fdd82fa8

scratch/search_k16_resident_state2_exact_2opt3opt_20260730.cpp
SHA-256 fe74d2abe71bd3a0f3a5c2278be7ff3f1ba9de19696ab73913f17d54296a928e

scratch/k16_j3959_stage2_component_crosspair_20260730/struct_0_2_1_0_1.targets
SHA-256 c745c7d3cec2416de5ea91789a4df128826c176ae65557ac6ac4b54c6a98ad22

scratch/k16_j3959_flatblock_rethread_20260730/audit_pruned.tsv
SHA-256 b0c0b34ef164633b9b3599718a14818b84e7c6ec01da35203185e5cc9a9dbf05

scratch/k16_j3959_flatblock_rethread_20260730/exact77_catalogue_remote.tgz
SHA-256 71ee4138dd6737807bb030c434a88cd1d67dfacf0f8b4c458c59d859bf12a71d

scratch/audit_k16_j3959_flatblock_component_signatures_20260730.py
SHA-256 949a39e27d5814accac52e9d40cd0773390e86d840ade37697c59b17d36cb7b2

scratch/k16_j3959_flatblock_rethread_20260730/component_upper_signatures.audit.json
SHA-256 d3773eb959531a72fc9d6ef970e7d505b74194a03b44752da357464e363ee616
payload 2ce06cfe946a409f5d1a20b6cc12811c0ebbad4a3bbcf6fcd4c07aba5fd54003

scratch/audit_k16_j3959_flatblock_hole_atlas_20260730.py
SHA-256 e01f53a1c4e16126c5f0c86d578273405566b3f27ce9e39716c6103084ca604a

scratch/k16_j3959_flatblock_rethread_20260730/independent_hole_atlas.audit.json
SHA-256 116a97fb75b6a015854fdf94ad40ccd34b950a2bb78728305ea38fb8fc7bce60
payload 323f4e40ec4d80e7c3e361e74d7eff8cd7c4a410bfa3b12f87bbbed2ab1810b4

scratch/audit_k16_j3959_flatblock_component_crosspair_core_20260730.py
SHA-256 97b5648b1fe0e4a9aa9af83c9f0b5b968a349b20b7765de49ac76dac842b65f3

scratch/k16_j3959_flatblock_rethread_20260730/component_crosspair_core.audit.json
SHA-256 7396294bda18f68ab24c1de3496678d425d43243d98ac3e700538ca2f77ef03e
payload 1cbb1df3c169f05d4a01b7e54e267fabbaff40b2cb8d813e3cecef5f72da7810

scratch/audit_k16_j3959_exact77_upper_signature_cover_20260730.py
SHA-256 a52bf9187e1d1282fdf2142f3308f51d796dc5ed354b25032dcb2e1a08cfbde5

scratch/k16_j3959_flatblock_rethread_20260730/upper_signature_cover.audit.json
SHA-256 f39c19a3541f1516d67461f6fe43a050b71f3bdf5aae360aedc8aa9d13e8c43d
payload 22ea892542f375fdb31e2ca864e26178b7123f549e74733b4a14f69aa333e295
```

The similarly named `exact77_catalogue.tgz` is not authoritative: it contains
only IDs 62--76.  The `exact77_catalogue_remote.tgz` archive above contains all
77 target/envelope pairs.
