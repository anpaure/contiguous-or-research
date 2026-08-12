# K16 pass33 matching-protected halo packets

## 1. Exact verdict and scope

This note works only with the authenticated pass33 chronology

```text
scratch/defect_transport_sparse_bad2_20260730/shorebfs_out/pass_33.targets
```

of SHA-256

```text
2dbb84bc6467047d99019e58b6a33072cbca8f0bc6e62c451954603611fcf2ec.
```

Its compiler graph has 26,332 lower targets, 32,063 physical cells, and the
frozen maximum matching $M$ has

\[
 |M|=26308,\qquad \operatorname{def}=24.                 \tag{1.1}
\]

The proposed common-`0200` halo moves the unique occurrence

```text
6b29@3846 -> row 4653
```

and seeks the two new incidences

```text
6a29 -- J13964=[4654,4657),
4a29 -- J13966=[4655,4657).
```

The outcome is negative for the smallest matching-protected packet classes,
but it gives a sharp next gate.

1. Installing `6b29` at row 4653 necessarily destroys three specified
   frozen matching edges.  Moving its unique old occurrence necessarily
   destroys at least one of two specified source edges.  Thus a zero-loss
   matching-protected occurrence transport is impossible in every packet
   architecture, not merely in the tested finite classes.

2. After adding row 4652 to the destination packet, exactly ten algebraic
   endpoint values realize exact inherited-depth replay and both new halo
   cells; exactly eight retain the actual schedule.  The unique
   nonincumbent, schedule-legal value with minimum frozen loss is
   `63a9@2378`.

3. The exact matching question under exterior-edge retention contracts to a
   75-left bipartite graph and threshold 52.  This is necessary and
   sufficient; scalar loss counts are only a prefilter.

4. The direct three-cycle class (12,871 rows), every nontrivial rigid aligned
   packet through width 64 (2,080 arcs including the trivial exact width-one
   substitution), the complete width-at-most-four minimal one-token packet
   class (915 formal packet descriptions), and the separated direct/crossed
   width-at-most-four one-token atom library (2,832 formal descriptions)
   contain no middle-exact completion.

5. A separate H100-CPU census of all 92,862,704 source-collar support-two
   profiles has 416 middle-exact rows but none retaining 24 of the 25 source
   matching edges.  Its minimum frozen loss is two.

6. The derived physical envelope word is already on the optimal ghost-free
   equality face

   \[
   (G,S,J,F)=(0,0,0,3).
   \]

   Its unique literal providers of the canonical post-ghost-kill pair are
   `2c6d@[3783,3786]` and `c679@[12826,12829]`, with inclusive endpoints.
   All three saved halo cycles retain both providers and have
   `delta(G,S,J,F)=(0,0,0,0)`; their failure is purely at the protected
   matching gate.

No exact/all-upper carrier of deficiency below 24 is produced.  Within local
width at most four, the smallest remaining packet class must either import at
least two external tokens into one packet or use dependency-overlapping
packets at an anchor.  A dependency-separated one-token packet of width at
least five is also open.  Any survivor must then pass the exact 75-left
matching test, arbitrary-upper replay, full physical replay, and the named
`{2c6d,c679}` provider gate.

The old root occurrence-cycle generator was edited after its saved depth-seven
run.  Its current source hash is therefore not used to authenticate that run.
The three saved all-upper carriers used below are instead authenticated by
their explicit occurrence cycles, byte-identical target reconstruction, and
independent Hall certificates.

## 2. Dependency closure and packet signatures

All relevant rows precede the first flat and have depth three.  For a row
word $T$, put

\[
 P_j(T)=T_{j-3}\cap T_{j-2}\cap T_{j-1}\cap T_j,
 \qquad
 \widehat T_i=\bigcup_{j=i}^{i+3}P_j(T).                \tag{2.1}
\]

Middle reconstruction is exactly $\widehat T_i=T_i$.

For a compiler cell $C=[s,s+ℓ)$, where $1≤ℓ≤3$, its complete
incidence signature consists of

* the ordered envelopes $P_s,…,P_{s+ℓ-1}$;
* their union $A_C$;
* the mandatory mask $M_C$.

A lower target $R$ is incident with $C$ exactly when

\[
 M_C\subseteq R\subseteq A_C,
 \qquad R\cap P_j\ne\varnothing\quad(s\leq j<s+\ell).
                                                               \tag{2.2}
\]

### Lemma 2.1 (exact dependency interval)

In a constant depth-three region the complete signature of
$C=[s,s+ℓ)$ depends only on, and in general on every row in,

\[
 \operatorname{Dep}(C)=[s-6,s+\ell+2]                 \tag{2.3}
\]

with integer endpoints included.

#### Proof

The ordered envelopes read carrier rows from $s-3$ through $s+ℓ-1$.
To decide whether a bit of any such carrier row is wholly
contained in $C$, the mandatory-mask calculation reads all four envelopes
belonging to that carrier.  Each of those envelopes reads three more rows to
its left.  The extreme rows are therefore
$s-6$ and $s+ℓ+2$.  Formula
(2.2) then proves that agreement on (2.3) preserves the complete incidence
truth value.  Each extreme can be active, so the interval is sharp. QED.

For an edge bank $E$, define

\[
 \operatorname{cl}(E)=\bigcup_{(R,C)\in E}\operatorname{Dep}(C). \tag{2.4}
\]

The exact pass33 closures are

| edge bank | size | closure |
|---|---:|---|
| source losses common to the three saved cycles | 6 | `[3840,3853)` |
| destination losses common to the three saved cycles | 3 | `[4647,4659)` |
| destination losses plus `J13964,J13966` | — | `[4647,4660)` |
| every frozen edge affected by row 3846 | 25 | `[3835,3858)` |
| every frozen edge affected by rows 4652 or 4653 | 26 | `[4641,4665)` |

Thus an exact packet-to-slot compatibility signature is not a row value.  It
is the tuple

\[
 \Sigma=(\text{boundary envelopes},\text{boundary replay vector},
          \text{exterior frozen-edge survival bitset},
          \text{variable incidence graph}).             \tag{2.5}
\]

For pairwise dependency-separated slots, occurrence ownership is a
permutation constraint and local compatibility is exactly a directed cycle
cover in the graph of signatures (2.5).  Upper completeness remains a final
literal interval-OR replay; it is not encoded by (2.5).

## 3. The four forced matching releases

### Theorem 3.1 (destination three-edge lock)

Within the frozen pass33 depth/cell structure, every chronology with
`T[4653]=6b29` destroys the three frozen
incidences

```text
61a0 -- J13959=[4653,4654),
6181 -- J13960=[4653,4655),
69a1 -- J13961=[4653,4656).
```

This is independent of every other row choice.

#### Proof

Every envelope in any of the three displayed cells lies at a position
$p\in[4653,4655]$.  Since the depth of row 4653 is three, row 4653 is one
of the intersectands defining every such envelope.  Hence the allowed union
of each cell is a submask of `6b29`.  The bit `0080` is absent from `6b29`
and present in each of `61a0,6181,69a1`.  The upper containment in (2.2)
therefore fails for all three targets. QED.

### Theorem 3.2 (source two-edge lock)

Within the frozen pass33 depth/cell structure, if the frozen incidences

```text
6828 -- J11538=[3846,3847),
6301 -- J11547=[3849,3850)
```

both survive, then `T[3846]=6b29`.

#### Proof

The first singleton incidence implies
`6828` $\subseteq P_{3846}\subseteq T_{3846}$.  Row 3846 also
participates in $P_{3849}$, so the second implies
`6301` $\subseteq P_{3849}\subseteq T_{3846}$.  But

\[
 \texttt{6828}\cup\texttt{6301}=\texttt{6b29},        \tag{3.1}
\]

and the right side has rank eight.  Since $T_{3846}$ also has rank eight,
equality is forced. QED.

The `6b29` occurrence is unique in pass33.  Combining the two theorems gives
a lower bound independent of the packet architecture, but conditional on
the fixed pass33 depth/cell structure:

> Any occurrence permutation installing `6b29` at row 4653 must release at
> least the three destination edges of Theorem 3.1 and at least one of the
> two source edges of Theorem 3.2.

If every row except 3846 is fixed, exact local replay among the physical
pass33 row values permits only the nine
replacement values

```text
2b39 2ba9 2bb1 2bb8 6b31 6b38 6ba1 6ba8 6bb0.
```

Their source frozen-loss counts are respectively

```text
6 6 6 6 5 2 3 5 5.
```

The unique minimum is `6b38@795`; it loses exactly
`6301@J11547` and `6b21@J11543`.

## 4. Exact destination companion catalogue

Fix the inherited depth array, put `T[4653]=6b29`, vary only
`T[4652]=X` over all physical rank-eight pass33 values, and require its
middle equations together with both halo incidences `6a29@J13964` and
`4a29@J13966`.  Actual preservation of the inherited flat schedule is
recorded as a separate condition.

The complete algebraic list is

```text
X       6339 6399 63a9 63b1 6b19 6b29 6b31 6b89 6b91 6ba1
losses     5    6    3    5    6    5    5    6    6    3
```

Here `63b1` and `6b29` create an adjacent equality in the otherwise fixed
word and are schedule-illegal unless their adjacent cluster is also
rethreaded.  Among schedule-legal nonincumbent choices, the unique minimum is

```text
63a9@2378,
```

and its three losses are exactly those in Theorem 3.1.  Thus the preferred
two-row destination packet is

```text
(6ba1,69a9) -> (63a9,6b29) at rows 4652,4653.           (4.1)
```

This endpoint table is exhaustive for a one-row companion.  It is not a
claim that (4.1) has an occurrence-conserving return.

## 5. Exact matching contraction

Let $H$ be the subset of $M$ consisting of frozen edges whose dependency
meets at least one
of rows `3846,4652,4653`.  The source and destination banks are disjoint and

\[
 |H|=25+26=51.                                          \tag{5.1}
\]

Let $L_H,R_H$ be their matched endpoints, let $U$ be the 24 left
vertices unmatched by $M$, and let $F_M$ be the 5,755 $M$-free cells.

### Theorem 5.1 (matching-protected packet criterion)

Suppose a final packet chronology $Q$ retains every edge of $M$ outside
$H$.  Then $Q$ has a matching of size at least 26,309 **containing every
such exterior edge** if and only if

\[
 \nu\bigl(G_Q[L_H\cup U,\ R_H\cup F_M]\bigr)\ge52.     \tag{5.2}
\]

#### Proof

The fixed exterior matching has size $26308-51=26257$.  Every left or
right endpoint outside the displayed residual pools is already occupied by
that matching.  Consequently any extension containing it is precisely the
disjoint union of the exterior part of $M$ and a matching in the induced residual
graph.  Total size at least 26,309 is therefore equivalent to residual size
at least $26309-26257=52$.  Bipartite matching integrality proves both
directions. QED.

The variable graph has only $51+24=75$ left vertices.  This is the exact
packet-level Hall oracle.  A scalar count of lost frozen edges is neither
necessary nor sufficient for (5.2).

### Theorem 5.2 (equality and named-pair packet gate)

Let $P_j$ be the maximal physical envelope derived from the pass33 middle
chronology.  Its exact first-middle inventory and canonical post-ghost-kill
provider data are

\[
 (G,S,J,F)=(0,0,0,3),
\]

```text
2c6d -- [3783,3786],
c679 -- [12826,12829],
```

and each displayed inclusive interval is the unique literal provider of its
target.  The three saved halo cycles in Section 6.1 have

\[
 \Delta(G,S,J,F)=(0,0,0,0)
\]

and preserve both intervals.  Hence they pass the equality and simultaneous
`{2c6d,c679}` provider gate, while failing the protected matching gate.

#### Proof

Reconstruct each $P_j$ independently as the intersection of all middle rows
whose inherited depth interval contains $j$.  Scanning from every left
endpoint to the first OR of rank at least eight gives no missing middle
target, no stall, no jump, three same-deadline extras, and no different-
deadline extra.  A separate unrestricted interval scan finds exactly the two
displayed provider intervals.  Repeating both scans on each saved cycle gives
the same ledger and intervals. QED.

The generic architecture-free equality theorem says that a length-12,873
universal word must have $G=0$ and $S+J+F=3$.  In the canonical `p12826`
ghost-kill normalization this sharpens to simultaneous service of the two
named residual targets.  Thus any later packet score must record both
`delta(G,S,J,F)` and the two literal provider booleans in addition to Hall.

## 6. Complete small-packet no-go classes

### 6.1 Root all-upper cycles

The three saved exact/all-upper occurrence cycles have target hashes

```text
candidate34  0b43cc742ef28d822f86690ea2b13d8596dc7144a84c1d9ebbe7adcde2567027
candidate45  67e606307fd951f37a52878befd5917a18eb03d4c5f5a6c4d61206353ec09fbc
candidate46  8e94ae0ad9b86b91e9122dcbd37b350ef7558c116f12bc50ec37efe7df672e5b.
```

Their Hall matchings are respectively 26,302, 26,298, and 26,301.  Exact
replay of the frozen matching gives 44, 43, and 44 destroyed edges.  In each
word the loss set is the disjoint union of the one-row loss sets at its
edited sites; no packet compensation occurs.  Thus these cycles authenticate
the halo chronology but not a matching-protected transport.

### 6.2 Direct and rigid packet cycles

The literal three-cycle

```text
3846 -> 4653, z -> 3846, 4653 -> z
```

was checked for every other row $z$: 12,871 formal cycles and
zero middle-exact cycles.

More generally, for every width $1≤w≤64$ and every offset
$0≤o<w$, the rigid aligned source packet

\[
 [3846-o,3846-o+w)\longrightarrow[4653-o,4653-o+w)     \tag{6.1}
\]

was replayed with the destination exterior fixed.  Of
2,080 arcs in total, the only middle-exact one is the original
width-one substitution.  Hence every nontrivial separated packet cycle with
forced arc (6.1) is impossible before upper or Hall testing.  This is a
directed packet-arc result, not a rephrasing of the closed two-block
equal-swap census.

### 6.3 One-token packet returns

For a centre occurrence $p$, incoming token $z$, width
$w∈\{2,3,4\}$, and each of the $w$ width-$w$ intervals containing
$p$, replace the centre token by $z$ and arbitrarily permute the resulting
packet multiset.  The exact number is

\[
 \sum_{w=2}^4 w\,w!=4+18+96=118.                       \tag{6.2}
\]

For the preferred branch (4.1), put `6ba1` at row 3846 and try all 118
returns replacing `63a9@2378` by `69a9`.  None is middle-exact.  The bad-row
histogram is

```text
2:9, 3:9, 4:12, 5:3, 6:6, 7:14, 8:47, 10:18.
```

The nine closest cases preserve natural packet order and fail exactly

```text
row 2377: 43ad -> 41ad, missing 0200;
row 2378: 69a9 -> 61a9, missing 0800.
```

The complete minimal three-cluster class consists of

* six remote companion branches, $6×118$ descriptions;
* the incumbent companion return, 118 descriptions;
* the adjacent-source `6b31@3847` merger, 86 descriptions;
* three representations of the adjacent-destination `63b1@4651` merger.

Thus its exact formal size is

\[
 6\cdot118+118+86+3=915,                               \tag{6.3}
\]

and its middle-exact count is zero.  These are formal packet descriptions,
not asserted-distinct resulting words; independent canonicalization gives
607 distinct words, still with exact count zero.

Finally take the six remote destination companions

```text
6339@6293, 6399@4165, 63a9@2378,
6b19@3362, 6b89@5042, 6b91@5183
```

and the six remote source seams

```text
2b39@437, 2ba9@6263, 2bb1@468,
2bb8@2206, 6b38@795, 6bb0@681.
```

For each of these 12 centres, each incoming export in
`{6ba1,69a9}`, and all 118 packets (6.2), the local atom is middle-inexact:

\[
 12\cdot2\cdot118=2832\quad\hbox{formal atom descriptions},
 \qquad 0\quad\hbox{exact atoms}.                       \tag{6.4}
\]

These canonicalize to 1,872 distinct local words, again with exact count
zero.

Therefore the separated direct/crossed four-packet architecture using one
external token per return packet is empty.  These are multi-cluster internal
permutations, not a single transposition of two equal contiguous blocks, so
(6.3)--(6.4) are outside the earlier equal-block-length-64 quantifier.

### 6.4 Complete support-two source packet

The full source collar is `[3835,3858)`.  The support-two census chooses

* the second changed row in its 22 nonanchor positions;
* one of the 328 physical row values containing `6828` or `6301`, other than
  `6b29`, at row 3846;
* one of the 12,869 nonincumbent physical row values at the second position.

Hence the exact formal count is

\[
 22\cdot328\cdot12869=92,862,704.                       \tag{6.5}
\]

The H100-CPU census completed all rows using 7,680 KiB maximum resident
memory.  Exactly 416 profiles are middle-exact.  Their source frozen-loss
histogram is

```text
2:87, 3:92, 4:26, 5:36, 6:38, 7:46, 8:27, 9:64.
```

There is no loss-one profile.  An independent implementation replays all 416
emitted rows and reproduces every loss set and the full histogram.

This is an overinclusive two-row allele-profile census: it does not impose
occurrence conservation and can admit a repeated or unavailable donor
allele.  Its no-loss-one conclusion is therefore a valid necessary endpoint
no-go, not a packet existence theorem.  It does not say that a packet losing two
old edges cannot satisfy the residual matching criterion (5.2) after a
larger occurrence-conserving return.

## 7. Exact remaining gate

The following is the smallest-width class not closed here.

1. Keep one of the schedule-legal endpoint companions in Section 4.
2. At some local source or return packet of width three or four, import at
   least **two** external occurrence tokens, or allow two packet dependency
   collars to overlap.
3. Require exact middle replay and retain every edge of $M$ outside $H$.
4. Evaluate the exact residual graph (5.2), then arbitrary-upper coverage.
5. Retain literal providers for both `2c6d` and `c679`, with
   `delta(G,S,J,F)=(0,0,0,0)`.

Equivalently, a proof-safe atom is labelled by

\[
 (\text{signed occurrence multiset},\text{boundary signature},
  \text{exterior-loss bitset},\text{75-left residual adjacency}). \tag{7.1}
\]

Atoms may be joined only when the signed occurrence multisets sum to zero.
The width-at-most-four one-token atoms in (6.4) are all absent, so within that
width a genuine next search begins with two-token local atoms.  The separate
one-token width-at-least-five class remains open.  Neither class should return
to marginal halo counts or to the already closed equal-block family.

## 8. Frozen evidence and audit boundary

Primary light audit:

```text
scratch/audit_threadA_k16_pass33_matching_packet_closure_20260731.py
  SHA e136c1b273a9c97f6380818868cb9e8b865c64a71bf1df3436b429001bab97c1
scratch/threadA_k16_pass33_matching_packet_closure_20260731.audit.json
  SHA fe3c57b64491ce281a76d6a4d4ce6e2ccff49ae2211ad6c03b5a57ced6c73c24
  payload 41c6a22cbcdd73ce9869c93b2641b855d8cd13ebe7e0c71c97c9bf1167dd2eac
```

Independent equality/named-pair replay:

```text
scratch/audit_threadA_k16_pass33_equality_pair_gate_20260731.py
  SHA a821bd53bc33f74f665cfe8ed263e0bc34ddeba988c992a17e4fa59b60f1a981
scratch/threadA_k16_pass33_equality_pair_gate_20260731.audit.json
  SHA 1d0891700fe35cef0d664465d422007c09a168d8f6a3dde646edddba0939fe5b
  payload 8f2d6e6f3bb653d19db45c56011b0d511a3ddc698d34d3ea2a146e095c263e1c
```

Support-two production and frozen bundle:

```text
scratch/threadA_search_k16_pass33_source_packet_support2_20260731.cpp
  SHA 3122c70abc165d75bb9ef8c61768572108c3137d59ea8117209602fd151a958e
scratch/threadA_k16_pass33_source_packet_support2_20260731/SHA256SUMS
  SHA 547f5d9aa875b77341e2d9acf43e9d53cdcbe0b51b27af7640555d014d39fbce
scratch/threadA_k16_pass33_source_packet_support2_20260731/support2.tsv
  SHA 750183736e423124a1676f31ebd52b0704b6b21c0a38b43301ec0217a3e7b217
```

Independent emitted-row replay:

```text
scratch/audit_threadA_k16_pass33_source_packet_support2_20260731.py
  SHA b5c4e5f2a75fc0137890e58d86ac46d297e2f43e4505968096c92f218cc104a7
scratch/threadA_k16_pass33_source_packet_support2_20260731.audit.json
  SHA 77a98f32b2d4662ccaaa7779b1f0d41c44b160ee0740ec402628fd7ff2f2d20d
  payload 6095595144417f8e63704547ba8984911b727d02af8818d11124f0da0e446e5a
```

Saved all-upper/Hall authentication:

```text
scratch/k16_pass33_compatibility_cycles_20260731.audit.json
  SHA 17df5cd0ee054fa19a3769f20180df9f167d3539bd803e8ab3d5231d3e327756
candidate_34.hall.audit.json
  SHA f9b5a2eb603212233cc88f3abe8922bef7ebad87ee5d7476e4e3bf22264df87c
candidate_45.hall.audit.json
  SHA a2a79dff30daceddb6b9d947d3df4b9a1efc05fb8abdbcf011ddb23f9777ae98
candidate_46.hall.audit.json
  SHA ab2b5316722343ea0847656309431877e15865112557ceeb2fdf2e77bb52223b
```

The independent replay proves that every emitted source profile and loss set
is correct.  Completeness of the 92,862,704-row support-two census also uses
the frozen C++ loop bounds and the completed resource log.  No SAT solver,
local heavy process, or generic equal-block rescan was used.
