# The authenticated `m=9` SCD forest fails the componentwise depth-three source gate

Date: 2026-08-01  
Lane: A / finite `k=17` multi-component SCD carrier  
Status: exact lightweight replay and scoped no-go for the fixed contiguous-component face

## 1. Frozen input and provenance

The authenticated flexible-detachment witness lives on `h100` at

`/home/amodo/or15/work/root_scd_detachment_20260801`.

Its CEGAR terminal files say

```text
phase_m9.winner.iteration = 0
phase_m9.cegar.terminal   = PASS_FOREST
```

and the frozen native audit prints

```text
cnf=230962/19040356 m=9 PASS selected=8008 edges=19448
palettes=19448/19448 max=1/1/2 components=4862 cycles=0
```

The remote lineage hashes are

```text
b39c549fab8b68a8166ac77218afc30fbfde9bf0f271a732c73640bb447ba5dc  phase_m9.cnf
75946e58bea2147d3899eae3f0f99aca9ba4ea413682c938ca59534b980a687c  phase_m9.winner.out
381dc1068aa39403d442c3d3b2d45a1c334dbc1e2b206449d5f678a6c1b6d473  phase_m9.map.tsv
49d3854140ed2ef3a1e2119013dc9b21e51176e4b69e5aa1a36a9a177d21d8de  phase_m9.selected.tsv
af3da9868158df3e187f859e1c1056e5a5e7c91767f1f1c7db7c8848b5dbb082  phase_m9.winner.audit.stdout
```

The selected TSV and audit metadata were copied byte-for-byte to

`scratch/a_scd_m9_depth3_audit_20260801/`.

The independent lightweight replay is

`scratch/a_scd_m9_depth3_audit_20260801/audit_scd_m9_component_depth3.py`.

It rebuilds the Greene--Kleitman `M_0` map and untouched seed providers
from first principles through the already-independent H2 replayer.  It does
not solve a SAT instance or enumerate candidate forests.

## 2. Exact maximal-source criterion

Let one directed forest component have consecutive middle owners

\[
                     O_0,O_1,\ldots,O_t.
\]

At depth `h=3`, a component source has cells

\[
                     Q_0,Q_1,\ldots,Q_{t+3}
\]

and must satisfy

\[
                     O_i=Q_i\cup Q_{i+1}\cup Q_{i+2}\cup Q_{i+3}
                     \qquad(0\le i\le t).             \tag{2.1}
\]

For each source position put

\[
 K_p=\bigcap_{\max(0,p-3)\le i\le\min(t,p)}O_i.      \tag{2.2}
\]

### Lemma 2.1 (componentwise depth-three source criterion)

A nonempty-letter source satisfying (2.1) exists if and only if

\[
 K_p\ne\varnothing\quad(0\le p\le t+3),             \tag{2.3}
\]

and

\[
 O_i=K_i\cup K_{i+1}\cup K_{i+2}\cup K_{i+3}
                     \qquad(0\le i\le t).            \tag{2.4}
\]

When it exists, `Q_p=K_p` is the componentwise maximal source.

#### Proof

Every `Q_p` lies in every owner window containing position `p`; hence
\(Q_p\subseteq K_p\).  This proves necessity of (2.3)--(2.4).  Conversely,
choosing `Q_p=K_p` proves sufficiency.  \(\square\)

Coordinatewise, failure of (2.4) is exactly an internal positive owner-trace
run of length at most three.  Reversing the path does not alter this test.
No ordering of other component blocks can repair such a run: it already has
a zero owner on each side *inside the same retained component*.

## 3. Exact census

The replay reconstructs all `24,310` roots and all `19,448` selected
forest edges, then extracts exactly `4,862` directed paths.  At depth three:

\[
\begin{array}{c|r}
\text{property}&\text{components}\ \hline
\text{maximal-source factorable}&3649\\
\text{factorability failure}&1213\\
\text{clipped signed-resident}&3328\\
\text{factorable and clipped signed-resident}&3328.
\end{array}                                          \tag{3.1}
\]

All maximal cells `K_p` are nonempty.  Every one of the `1,213` source
failures is an owner-reconstruction failure, and the failing components
are exactly those with a short internal positive run.

For clipped signed residence, the first and last trace runs of a component
are left to the later seam chronology, while every internal zero and one run
must have length at least four.  The component classification is

\[
\begin{array}{c|r}
\text{bad-sign class}&\text{components}\ \hline
\text{positive only}&408\\
\text{zero only}&321\\
\text{both signs}&805\\
\text{neither}&3328.
\end{array}                                          \tag{3.2}
\]

The individual bad-run occurrence histogram is

\[
 0\text{-run length }2:1145,
 \quad0\text{-run length }3:645,
 \quad1\text{-run length }2:1076,
 \quad1\text{-run length }3:660.                    \tag{3.3}
\]

All counts and failure predicates were replayed after reversing every path;
they are orientation-invariant.

## 4. Smallest explicit source obstruction

One three-edge component has rooted sequence

\[
                    831\to383\to65855\to98591
\]

and owner sequence, in hexadecimal,

\[
                (73f,37f,1017f,1813f)_{16}.          \tag{4.1}
\]

Coordinate `6` has owner trace

\[
                              0,1,1,0,               \tag{4.2}
\]

an internal positive run of length two.  Formula (2.2) gives

\[
 (K_0,\ldots,K_6)
 =(73f,33f,13f,13f,13f,1013f,1813f)_{16}.            \tag{4.3}
\]

Consequently

\[
 K_1\cup K_2\cup K_3\cup K_4=33f\ne37f=O_1,
\]

and

\[
 K_2\cup K_3\cup K_4\cup K_5=1013f\ne1017f=O_2.   \tag{4.4}
\]

Both reconstructions miss precisely bit `0x40`.  Lemma 2.1 therefore
proves that no depth-three source exists for this retained component, in
either orientation.

The smallest independent signed-residence obstruction after source
factorability is the component

\[
 11494\to76902\to76899\to93281,
\]

with owners

\[
 (27878,77030,76903,93283).
\]

It passes (2.3)--(2.4), but coordinate `14` has internal zero trace
`1,0,0,1`, of length two.

## 5. Consequence and exact scope

### Theorem 5.1 (fixed SCD multi-block face is infeasible)

Keep every authenticated forest component as one contiguous owner block,
allow arbitrary component permutation and reversal, and omit all `4,861`
inter-component owner windows.  Then the resulting `k=17` block face has no
flat depth-three source, regardless of the scalar slack `7401` and regardless
of the later generalized lower matching.

#### Proof

The component in Section 4 remains contiguous under every allowed operation.
Its internal trace (4.2) is unchanged up to reversal, so Lemma 2.1 rules out
its source before any seam or matching choice is made.  \(\square\)

This is the first exact failing gate requested for the authenticated
`4,862`-path carrier.  Therefore arbitrary-width upper-deck and generalized
lower-compiler solves are unnecessary on this fixed block face.

The theorem does **not** rule out an interior rethread of the SCD forest, a
nonflat compiler, splitting/interleaving a bad component, or choosing a
different exact-palette forest.  It is not a global `k=17` impossibility.

## 6. Frozen audit hashes

```text
9372c1ffe7f2f0c19d6071fd0d20f0f7b8f0c81274efffbfa0b8356e39518751  audit script
26ea47d8bf956543be7b1b1f12eaa2428270a241309f79640cd943c27529352b  audit JSON
390c2f18ca52ced690ef17f80075da432bff9d7bd7ef3098bae3af011fa288c8  canonical payload
```
