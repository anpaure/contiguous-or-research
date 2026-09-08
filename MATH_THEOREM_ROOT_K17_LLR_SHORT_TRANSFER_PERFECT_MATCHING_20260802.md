# K17 low-rank socket defects admit a disjoint `L-L-R` short transfer

**Date:** 2026-08-02  
**Status:** exact static theorem and H100 O3 census on the authenticated
warm47 table.  No socket, source-cell, supplier, chronology, residence,
upper, compiler, or word claim is made.

## 1. The two-row exchange

Write

\[
 L=\bigcup_{s=1}^6{[17]\choose s},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Consider two chains in the compressed-normal table,

\[
       \ell\subset m\subset r,
       \qquad u\subset q,                             \tag{1.1}
\]

where `ell,u in L`, `m in M`, and `r,q in R`.  If

\[
                         \ell\subset u,               \tag{1.2}
\]

replace (1.1) by

\[
       m\subset r,
       \qquad \ell\subset u\subset q.                 \tag{1.3}
\]

### Lemma 1 (exact short-transfer exchange)

The replacement (1.1)--(1.3):

1. uses exactly the same five named targets;
2. retains the two rank-eight roots on the same physical rows;
3. retains the row-length multiset `{3,2}`;
4. retains every root--rank-nine-owner incidence; and
5. moves the short role from the `L-R` row to the `M-R` row.

Conversely, if the two roots stay on their rows and one transforms an
`L-M-R` plus `L-R` pair into an `M-R` plus `L-L-R` pair without changing
any named target, then (up to naming the two low targets) condition (1.2)
is exactly the required new containment.

#### Proof

The only new inclusion is `ell subset u`; all other inclusions already
occur in (1.1).  Both roots are unchanged, so their containing rank-nine
owners remain legal.  The target and length assertions are immediate.
Conversely, the new length-three chain must use the two old low targets and
the old `L-R` root; strictness is precisely their comparability.  QED.

This exchange lies outside the compressed-normal common-basis face because
it creates one `L-L-R` chain.  It is nevertheless an exact inclusion-chain
partition move.

## 2. The warm47 transfer graph

The authenticated warm47 table has

\[
 16,915\quad L-M-R\text{ rows},\qquad
 4,862\quad L-R\text{ rows}.                         \tag{2.1}
\]

Among its 3,899 original P2 short roles, the phase-union-zero rank census is

\[
\begin{array}{c|rrrr}
\text{bottom rank}&4&5&6&7\\ \hline
\text{union-zero roles}&17&277&724&623.
\end{array}                                           \tag{2.2}
\]

Thus exactly

\[
                    17+277+724=1,018                 \tag{2.3}
\]

of the frozen P2 zero roles are `L-R` rows.  The remaining 623 are `M-R`
rows and are not vertices on the left shore below.

Form a bipartite graph `G_transfer`:

* its left vertices are the 1,018 union-zero P2 `L-R` rows `(u,q)`;
* its right vertices are the 16,915 `L-M-R` rows `(ell,m,r)`;
* join the two rows exactly when `ell subset u`.

Every edge is one exchange from Lemma 1.

### Theorem 2 (perfect disjoint transfer)

On the authenticated warm47 table, `G_transfer` has

\[
                         34,757                       \tag{2.4}
\]

edges.  Its left degrees have minimum 4, maximum 56, and average
34.1424.  Its maximum matching has cardinality

\[
                         1,018.                       \tag{2.5}
\]

Consequently all 1,018 low-rank P2 union-zero roles can simultaneously be
turned into long `L-L-R` rows while 1,018 distinct old `L-M-R` rows become
new `M-R` short rows.

#### Proof

The O3 auditor reconstructs both shores from the literal table, constructs
exactly the containment edges (1.2), and runs Hopcroft--Karp.  The returned
matching saturates the entire left shore.  Matching edges use distinct rows
on both sides, so their two-row exchanges are pairwise disjoint.  Lemma 1
then applies simultaneously.  QED.

After all 1,018 exchanges, the four static chain-type counts are

\[
\begin{array}{c|rrrr}
\text{type}&L-L-R&L-M-R&L-R&M-R\\ \hline
\text{count}&1,018&15,897&3,844&3,551.
\end{array}                                           \tag{2.6}
\]

The length histogram remains `(0,7395,16915)`, and every target and root is
still used exactly once.

## 3. Consequence and exact remaining gate

The 1,641 frozen original-P2 union-zero roles split exactly into two
different structural problems:

\[
 1,018\text{ low-rank }L-R\text{ zeros}
 \quad+\quad
 623\text{ rank-seven }M-R\text{ zeros}.             \tag{3.1}
\]

Theorem 2 eliminates static scarcity for the first cohort without changing
the rank-seven receiver-root bank.  In particular, the fixed-root SCC
obstruction for the second cohort does not apply to these 1,018 roles.

The theorem does **not** assert that the 1,018 newly short `M-R` rows have
literal sockets.  The next exact question is a weighted/typed version of
`G_transfer`: for every edge, reprice the new `M-R` short row and the new
`L-L-R` long state in both phases, then impose supplier, private-ticket,
endpoint-state, and residual long-state Hall simultaneously.  A perfect
matching in the untyped graph is only the structural outer layer of that
problem.

Likewise, Theorem 2 does not touch the 623 already-rank-seven P2 zeros;
those still require a receiver-changing packet, a status-changing compound
column, or regenerated endpoint modes.

## 4. Frozen evidence

Local source and copied H100 artifacts:

```text
scratch/audit_root_k17_llr_short_transfer_matching_20260802.cpp
  76ce409a564538c690b75ac7bcd13d6a1be734bd456a520452202fa90f3b021d
scratch/root_k17_llr_short_transfer_matching_20260802/
  llr_short_transfer.audit.json
    75596d0b1d4e45ce1efaaf4978c0f2d45f32e3dbade7ed721c0e63660d7df946
  llr_short_transfer.matching.tsv
    f6fa956c3ad00f7d5accf87a771d1784907ba5a34b71dd98093a1d87b4ed6a94
```

Independent H100 root:

```text
/home/amodo/or15/work/root_k17_llr_short_transfer_matching_20260802/
```

Input bindings:

```text
warm47 table
  95dee6e9718f9067d4bd5c860f7763a45ee03785bdbb13b20b8d95540a7a2735
P2 structural-role ledger
  8fb841ec529a42daa70ee76408cebc091cfed954a3b4885f28a35d9a6b1498dd
```

The second input hash is the remote manifest binding; a separately authored
full-table replay has been requested and is not silently assumed here.
