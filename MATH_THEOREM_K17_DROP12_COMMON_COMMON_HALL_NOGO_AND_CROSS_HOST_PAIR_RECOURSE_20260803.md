# K17 drop-12 common/common Hall no-go and corrected pair-recourse boundary

**Date:** 2026-08-03

**Status:** exact fixed-parent common/common Hall obstruction and corrected
two-mode occurrence formulation. The two older negative unary screens are
superseded: one excluded the global 23-row occurrence union, and the next
excluded the ten materialized incumbent LLR hosts. The final host-admitting
V2 replay establishes the unary no-go and forced partner-host condition for
the 468 rank-improving modes only.
All statements are bound to the canonical compressed parent
`e878bf19654d8478b4552451a3b5c9a54716e1383d2513c59d680091e10b5ffb`
and ten-mode final table
`fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c`.
Phase 1 remains transported-owner evidence; no native-phase-1 claim is made.

## 1. Bound finite data

The exact individually common helper/control pool is

```text
scratch/k17_drop12_canonical_target20_20260803/input/
  exact_state_common.coalesced.pin_disjoint.incumbent_disjoint.tsv
SHA-256 6dd057e147ce36f725eb4112bc11f8528c2596d1995d3c73a33bc4aaf5995cab
```

It contains 3,483 modes: the 3,494 pin-safe common records minus exactly 11
incumbent-endpoint conflicts.  Its current audit has SHA-256
`84790f5fef14c258e33cb29ac3dba5c6bb06cdb5fc1bcb7702638b9a16bcaf82`.
Write this mode set as \(P\).

The exact supplier score ledger has SHA-256
`84a4475d2d3d445ff8acc827cbf22ce56b539294208ab482ebe4e8e6f4308cb7`.
It contains 515 modes surviving the incumbent \(23/2\) Hall row: 468 have
matching rank \(16878/16898\), and 47 have rank \(16877/16898\).  Write the
468 unary supplier-deficiency-20 modes as \(H\).

The superseded candidate-local occurrence ledger for \(H\) has SHA-256
`21ab1c4f987c54d835306394c86a7aef0b96ead2caeaf31153b9513889a91050`,
and its audit has SHA-256
`01c6c895b823f95281461ce909546f21d20f33ef14bd66e8d0b676e0fda7645e`.
It exhausted physical tuples only after imposing the overstrong global
union-23 exclusion. Its positive witnesses remain literal positives, but its
zero census is not a no-go under the corrected phase-specific contract.

The superseded phase-specific unary replay has audit SHA-256
`79a4776ab79ec8f44b45fd4374e7bd3cd0d41ddc8daa47152dfc63af88233c0a`
and historical manifest-file SHA-256
`a7eaf78bc136a6f35d0ef583fa00f2deb298bbbf1875362a638156745b445095`.
It reserves 20 rows in each phase, permits flag-consistent use of the three
opposite-phase-only rows, and finds zero common states for all 468 modes in
\(H\). This is still not an exact negative result: it excludes the ten
materialized incumbent LLR hosts from the witness bank. Endpoint immutability
for the candidate transfer does not make those long rows unavailable as
occurrence witnesses. Its zero census is therefore calibration only.
The historical manifest later failed two overwritten source entries and is
not a valid freeze; it is retained here only to identify that superseded run.

The final host-admitting V2 replay has source SHA-256
`92d929b0aae6a6f7e908b8ad0754e3f02871051ec78daf116094132e4ffcbf1d`,
audit SHA-256
`22947f62a855bdf32613100f294dcd541b9541ac31db06b04075e8665ba17fde`,
and manifest SHA-256
`860741486619423d87d1f685234f49692fd39a2a7025c2ead72c904cb90c4891`.
It admits all ten immutable incumbent LLR hosts as witness rows and still
finds zero common states for all 468 modes in \(H\).

The exact common-mode Hall metrics have SHA-256
`3497a610f5aacc4aabc7559d78e7ca24f856ec8c05a3805c13a8972a60c69e68`.
The resource-disjoint pair summary has SHA-256
`8f9ff48c25474260fcdaf92e00bd4579e9527c86a0770bfd58d646c1cb9b35d0`.
The adaptive target-20 matching theorem is bound here through its immutable
local snapshot, SHA-256
`246fbc50e1aee2829f10088c844d4db63177ca082345a00b06c0127aeb664e16`.

## 2. Exact Hall geometry

Let \(Q\) be the canonical maximum-deficiency head shore.  Its supplier
subgraph is the disjoint union of 19 isolated heads and the two alternating
paths

\[
13148\;--\;12973\;--\;12948,
\qquad
15103\;--\;14851\;--\;1490,
\tag{2.1}
\]

where the middle vertices are physical supplier rows.  Hence

\[
|Q|=23,\qquad N_0(Q)=\{12973,14851\},\qquad
\kappa_0(Q)=23-2=21.                                      \tag{2.2}
\]

Every mode \(p\in P\) avoids all 23 head rows of \(Q\), so every head of
\(Q\) remains active.  No such mode creates a supplier identity outside
\(N_0(Q)\).  For 3,482 modes the neighborhood is unchanged.  The sole
exception is edge 52847: its host is supplier row 14851, and its post-state
destroys both shore edges incident with that source.  This removes one
neighbor identity, not two, and therefore has Hall credit \(-1\).

## 3. Common-only no-go at every cardinality

### Theorem 3.1

For every row-disjoint set \(S\subseteq P\), irrespective of which
alternative occurrence witnesses are later chosen,

\[
N_{T_S}(Q)\subseteq\{12973,14851\},
\qquad g_{T_S}(Q)\le2,
\qquad \delta(T_S)\ge21.                                 \tag{3.1}
\]

If \(52847\notin S\), then the neighborhood is exactly the parent
neighborhood and the Hall credit is zero.  If \(52847\in S\), then row
14851 is lost and the credit is \(-1\).

#### Proof

No selected endpoint is a shore head, so no inactivity term is created.
For a row-disjoint selection, each changed source row has exactly its
audited singleton post-state; all other source rows and all shore heads are
unchanged.  The metric ledger proves that none of these post-states supplies
a new identity to \(Q\).  Taking the union of their source neighborhoods
therefore gives (3.1).  Occurrence witnesses certify sockets but do not alter
the materialized supplier graph, so alternative witnesses cannot evade the
cut.  Edge 52847 is the unique audited loss.  Finally Hall's theorem gives
\(\delta(T_S)\ge |Q|-g_{T_S}(Q)\ge21\).  \(\square\)

### Corollary 3.2

Among the 5,221,318 unique unordered resource-disjoint common/common pairs,
exactly 5,219,031 have credit zero and 2,287 have credit \(-1\); none has
positive credit.
Thus the common/common face is closed before supplier matching, even though
its individual common-state witnesses are valid.

Theorem 3.1 is stronger than this pair census: no larger packing drawn only
from \(P\) can reach target 20 either.

## 4. Correct one-mode status

The supplier facts remain exact: 515 modes pass the incumbent \(23/2\) cut,
468 have rank \(16878\), and 47 remain at rank \(16877\). Exact occurrence
uses two distinct fixed sets

\[
F_0,\ F_1,\qquad |F_0|=|F_1|=20,                         \tag{4.1}
\]

not their 23-row union. A row may be reused across phases exactly when its
required flag agrees. The final V2 replay also admits the ten current
incumbent LLR hosts. It proves an empty unary common-state menu for every
mode in \(H\). The corrected unary status of the other 47 modes remains
unknown.

### Conditional cross-host lemma

Let \(h\) be any mode whose complete corrected one-mode menu is proved to
have no common declared state. Let \(p\) be a legal canonical transfer on the
same fixed parent, row-disjoint from \(h\), with \(F_0,F_1\) and the protected
bank unchanged. If \(h\) is rescued in \(T_{h,p}\), one of its selected phase
witnesses uses the new LLR host of \(p\).

The proof is unchanged: relative to \(T_h\), transfer \(p\) only deletes its
old donor long state and adds its new host long state; deletion cannot create
a witness. The final V2 replay instantiates this lemma for every one of the
468 modes in \(H\). It remains conditional outside \(H\).

## 6. Exact two-color option graph

Fix an endpoint-disjoint pair \(e,f\), materialize both transfers together,
and recompute their complete phase menus on that literal child.  For
\(i\in\{e,f\}\), let \(\mathcal O_i\) contain every tuple

\[
(k,w_i^0,w_i^1)                                           \tag{6.1}
\]

such that both witnesses use the same declared state \(k=(q,\alpha,\beta)\),
are valid in their respective owner phases, avoid the protected rows and the
phase-specific incumbent set \(F_\phi\), respect the ten incumbent tickets
in that phase, and impose consistent flags on a physical row reused across
phases. All ten current incumbent LLR hosts remain witness-eligible; both
candidates' new hosts remain eligible for own- or cross-support. Endpoint
immutability is not occurrence unavailability.

Make a bipartite graph \(B_{e,f}\) with shores
\(\mathcal O_e,\mathcal O_f\).  Join two options exactly when their union has
unit physical-row capacity separately in each phase and consistent flags on
all cross-phase row reuse.

### Theorem 6.1

The pair has one joint common occurrence packing if and only if

\[
                         E(B_{e,f})\ne\varnothing.       \tag{6.2}
\]

#### Proof

A feasible joint packing restricts to one option on each shore and their
combined resource constraints create an edge.  Conversely, an edge supplies
the two common declared states and all four literal phase witnesses with
exactly the required capacity and flag consistency.  \(\square\)

For a source with a corrected one-mode no-go, the conditional cross-host
lemma permits deleting every source option that does not use the partner
host. Otherwise no such deletion is proof-safe. For any fixed pair, exact
occurrence lifting still reduces to constructing the two option shores and
testing whether one compatibility edge exists. This reduction is specific
to two selected modes and makes no matroid or multi-action composition claim.

## 7. Proof-safe search boundary

Let \(U\) be the 112,621-mode fixed-bank-safe universe. For \(H\times U\),
there are 52,664,349 endpoint-disjoint directed source--partner incidences.
Removing 96,146
reverse orientations of endpoint-disjoint \(H\times H\) pairs leaves exactly
52,568,203 unique unordered child tables.

The companion theorem
`MATH_THEOREM_K17_DROP12_TWO_MODE_Q23_SURVIVOR_COVER_AND_RANK47_REPLAY_20260803.md`
proves the complete fixed-shore reduction. Every target-20 pair contains one
of 515 positive-\(Q\) modes among endpoint-disjoint pairs in this fixed-parent
universe: the 468 modes in \(H\), or one of 47 rank-16877 survivors. Its exact
fixed-\(Q\)-passing envelope has 57,832,905 unique unordered children. There
is no remaining target-20/fixed-\(Q\)-passing face with neither of the 515
anchors; unanchored pairs exist but are exact cut no-gos.

The 3,483-mode set \(P\subset U\) remains only a frozen common/common control
bank. Theorem 3.1 closes \(P\times P\), but neither \(H\times P\) nor
468-by-3,483 is a complete partner face. For every \(h\in H\), the V2 unary
no-go forces any successful partner to supply its new LLR host to at least
one of \(h\)'s phase-specific occurrence roles. The 47 survivor anchors need
their own corrected unary and child-DM ledgers.

Every surviving pair must still:

1. materialize both modes simultaneously from the e878 parent with the ten
   incumbents;
2. replay the 7,213 protected rows and all incumbent occurrences;
3. pass the exact option graph (6.2), including self- and cross-support;
4. rebuild the complete child supplier graph; and
5. authenticate matching rank at least \(16878/16898\).

The incumbent \(23/2\) row remains pruning only.  Passing it is not a full
matching certificate, and adding a partner to an \(h\in H\) can erase rank.
Abstract matching geometry permits a rank-16877 survivor and an individually
rank-stagnant partner to combine into one augmentation; no such K17 pair is
yet witnessed. Hence reduction to the 468 modes alone is not proof-safe, even
though the reduction to all 515 positive-shore anchors is exact.

## 8. Scope

This theorem closes the literal common/common face at every cardinality,
proves the corrected unary no-go for \(H\), and gives an exact pair occurrence
oracle. It does not close the 47-survivor face or prove that any pair exists,
nor chronology, residence, upper coverage, common-cap compilation, a final
word, or K17 optimality.
