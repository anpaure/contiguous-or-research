# The protected K17 seven-factor has no C6/C8 fusion tree

**Date:** 2026-08-01  
**Lane:** D, one-copy coloured-Euler/component rounding  
**Status:** exact local fusion algebra; complete fixed-factor incidence-C6
and incidence-C8 catalogues; complete dynamic C6 regeneration sweep; exact
single-C6 residence and rank-11--13 ticket atlas.  This is a fixed-factor
no-go, not a no-go for prospectively choosing another residual factor or
for the full resident q-port packet.

## 1. Frozen factor and switch convention

The input is the independently verified protected factor

```text
scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv
SHA-256 7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df
```

It is a degree-two factor of the rank-eight/rank-nine incidence graph on
`[17]`, with 48,620 incidence edges, 52 immutable protected incidences,
complete rank-ten support, and seven components.  In literal component-ID
order their owner sizes are

\[
\begin{array}{c|rrrrrrr}
i&0&1&2&3&4&5&6\\ \hline
|C_i|&14305&8615&1362&18&4&3&3.
\end{array}                                                \tag{1.1}
\]

Its cyclic residence ledger is

\[
 (r_1,r_2,r_3)=(0,3073,2710),\qquad
 b_{\rm open}=5760,                                      \tag{1.2}
\]

and its upper holes at ranks 11, 12, 13 are respectively

\[
                         1502,295,9.                       \tag{1.3}
\]

For a rank-seven core `K` and distinct outside labels `a,b,c`, put

\[
 L_a=K+a,\quad L_b=K+b,\quad L_c=K+c,
\]

\[
 O_{ab}=K+a+b,\quad O_{bc}=K+b+c,\quad O_{ca}=K+c+a.
\]

The incidence hex has the two matchings

\[
 \{L_aO_{ab},L_bO_{bc},L_cO_{ca}\},\qquad
 \{L_aO_{ca},L_bO_{ab},L_cO_{bc}\}.                      \tag{1.4}
\]

An **admissible C6 fusion** is an orientation of (1.4) such that the old
matching is selected, the new matching is absent, no old edge is protected,
and the three old edges lie on three distinct current components.  Replacing
old by new preserves every incidence degree and all owner/lower vertices and
merges the three components into one.  Its component decrement is two and
its relative successor sign is `+1`.

At every involved lower vertex, keep its other selected owner fixed.  This
gives three old and three new rank-ten colours.  The switch is
**rank-ten-safe** iff, after aggregating repeated colours, every old colour
still has positive global multiplicity.  This is the exact last-witness
test; no heuristic colour score is used.

## 2. Complete first-generation C6 catalogue

There are exactly

\[
 2\binom{17}{7}\binom{10}{3}=4,667,520                 \tag{2.1}
\]

oriented incidence hexes.  The exact census is

```text
selected old phase                         46,960
selected and protected-preserving          46,818
three distinct current components           3,379
also rank-ten-safe                             405
```

The complete component-triple distribution is

\[
\begin{array}{c|r|r}
\text{components}&\text{all}&\text{rank-ten-safe}\\ \hline
012&3293&391\\
013&44&9\\
023&5&1\\
123&3&1\\
014&10&0\\
024&5&0\\
015&8&1\\
025&1&0\\
016&9&2\\
026&1&0.
\end{array}                                               \tag{2.2}
\]

### Theorem 2.1 (component-core cut)

No three preinstalled admissible C6 packets form a spanning loose
hypertree on the seven components.

#### Proof

Every row of (2.2) contains at least two vertices of

\[
                           \{C_0,C_1,C_2\}.               \tag{2.3}
\]

Consequently it contains at most one of the four outside components
`C_3,C_4,C_5,C_6`.  Three hyperedges therefore cover at most three of those
four outside components.  They cannot cover all seven vertices, hence
cannot realize `7->5->3->1`.  This argument precedes literal-support and
rank-ten compatibility; the exact ordered loose-hypertree pattern count is
zero. \(\square\)

This is stronger than finding no resource-disjoint triple by search.  It is
a transparent component cut in the complete first-generation catalogue.

## 3. Exact single-fusion ticket atlas

Every one of the 405 rank-ten-safe fusions was materialized independently.
Each gives five components, retains all 52 protected incidences and all
19,448 rank-ten targets, and has a complete cyclic interval replay through
rank 13.

Across the 405 rows, the residence changes satisfy

\[
 \Delta r_1=0,qquad -3\le\Delta r_2\le4,qquad
 -5\le\Delta r_3\le5.                                   \tag{3.1}
\]

Although 151 switches reduce the raw number `r_1+r_2+r_3`, every switch
worsens the best independent-opening residual:

\[
                         2\le\Delta b_{\rm open}\le13.    \tag{3.2}
\]

The final upper-hole ranges are

\[
\begin{array}{c|ccc}
\text{rank}&11&12&13\\ \hline
\min\text{ holes}&1498&293&7\\
\max\text{ holes}&1505&297&10,
\end{array}                                               \tag{3.3}
\]

and one switch loses at most `(3,3,1)` old last-witness tickets while
gaining at most `(4,3,2)` formerly missing targets at those ranks.  Exactly
113 switches improve the total rank-11--13 hole count.  The atlas records
the literal lost and gained masks, not only these extrema.

Thus component fusion and residence/deep-shadow repair are not aligned in
this factor: local C6 topology has useful deep gains, but none improves the
best linear residence obstruction.

## 4. Dynamic C6 regeneration is also closed

The first-generation cut does not by itself exclude newly generated C6
packets.  Therefore every one of the 405 safe first fusions was applied,
and its complete current-factor C6 catalogue was rebuilt.

The dynamic enumeration was implemented incrementally but exactly.  After
a switch, only six incidence statuses change.  Any phase whose applicability
changes contains one of those incidences.  Conversely, an unchanged phase
which is three-component after a merge was already three-component before:
component contraction can identify old labels but cannot split them.  Hence
the complete next catalogue is the union of

1. all old three-component phase keys, retested against the current factor;
2. all phases containing one of the changed incidences.

An incidence belongs to an explicitly enumerated 64-key local C6 index.
Current components and rank-ten currents are recomputed for every retained
key.  A full 4,667,520-key brute replay on the named first merger agrees
exactly with this incremental construction.

The exhaustive dynamic counts are

```text
safe first states swept                              405
first states with structural generation-2 C6         14
first states with rank-ten-safe generation-2 C6        5
structural generation-2 candidates                   166
rank-ten-safe generation-2 candidates                 12
generation-3 structural candidates after all 12        0
generation-3 rank-ten-safe candidates                  0
complete 7->5->3->1 sequences                          0
```

The five live first rows are compact candidate IDs

```text
1449  (2 safe seconds)
1461  (2 safe seconds)
1980  (3 safe seconds)
2075  (3 safe seconds)
3039  (2 safe seconds).
```

The separately named merger `(K;a,b,c;phase)=(36449;1,12,13;0)` is compact
row 1213.  It has no structural generation-2 C6 at all.

### Theorem 4.1 (two-generation C6 no-go)

Within this fixed factor, no sequence of protected, prefix-rank-ten-safe
incidence-C6 fusions has trajectory `7->5->3->1`.

#### Proof

Every possible first move is one of the 405 rows.  The exact dynamic
construction above exhausts every possible second move.  Only 12 are safe.
Rebuilding the catalogue after each of those 12 gives no three-component
C6 phase even before the rank-ten test.  Hence a third fusion does not
exist. \(\square\)

This theorem is occurrence-dynamic; unlike Theorem 2.1, it does not assume
all three packets were present in the initial factor.

## 5. Complete generic q4/C8 audit

For a rank-seven core and four outside labels in a cyclic order
`p_0,p_1,p_2,p_3`, put

\[
 L_i=K+p_i,\qquad O_i=K+p_i+p_{i+1}.                    \tag{5.1}
\]

The two incidence-C8 phases are `L_i O_i` and `L_i O_(i-1)`.  A toggle on
four distinct components merges them into one, changes component count by
three, and has relative sign `-1`.  There are three unoriented cyclic orders
on a four-label set and two phases, hence the complete oriented key count is

\[
 6\binom{17}{7}\binom{10}{4}=24,504,480.                \tag{5.2}
\]

The exact protected fixed-factor census has only 17 four-component C8
candidates.  None is rank-ten-safe.  Their first-step hole counts are

\[
                     1^4,\quad2^5,\quad3^7,\quad4^1.     \tag{5.3}
\]

Allowing those temporary holes does not help.  After materializing each of
the 17 first toggles, the dynamically rebuilt second-C8 catalogue has zero
four-component candidates.  Thus there is no structural `7->4->1` C8
sequence, even under a terminal-only rank-ten requirement.

### Corollary 5.1 (q3-then-q4 arithmetic)

After one C6 fusion the component count is five.  One C8 fusion would give
`5->2`; neither a C6 nor a C8 can then act on distinct components.  Hence a
q3-then-q4 route needs a separate support-two or open boundary connector.
Two C8 fusions would have the correct arithmetic `7->4->1` and total sign
`(-1)^2=+1`, but the exact second packet is absent by the preceding census.

The C8 audit is the generic incidence matching-switch class.  It is not the
full resident q-port rail construction, whose additional atoms can alter
the available occurrence bank.

The separately reported family of 110 colours with no one-cut support was
not accompanied here by an authenticated target-to-cut ticket map.  No
claim is made about serving those colours.  In particular, the observed
two-cut closures cannot be realized inside this generic C8 class because
there is no second structural C8, but this does not rule out a larger
q-port/collar packet carrying the external ticket map.

## 6. Distinction from prospective fixed-M0 planting

The fixed-factor no-go is not an abstract q4 obstruction.  A separate
prospective construction plants one canonical `q=4,d=3` resident packet
while jointly choosing a new residual `ML_9` degree-two factor.  Its exact
b-flow is `48556/48556`; one common alternating `M0` and one common residual
`Q` give

\[
                         3164\longrightarrow3161          \tag{6.1}
\]

components and relative sign `-1`.  The packet has 32 owners, 32 lowers and
32 distinct upper colours in both phases.  However, the resulting full
factor covers only 12,830 of 19,448 rank-ten targets; 24 packet colours
collide with the residual factor and only eight are private.  Thus it proves
fixed-`M0` component planting, not an upper-exact host.

For a general prospective packet with lower bank `L_P`, owner bank `O_P`
and fixed packet matching `M_P`, delete `L_P,O_P` from the incidence graph.
A jointly chosen residual two-factor exists exactly when

\[
 2|X|\le\sum_{y\in O\setminus O_P}
               \min\{2,|N(y)\cap X|\}
 \quad\text{for every }X\subseteq L\setminus L_P.       \tag{6.2}
\]

This is the max-flow/min-cut condition for left demand two and right
capacity two; equality of shore sizes then forces right degree two.  Every
residual even cycle splits into two matchings, one extending `M_P`.

If a global `M0` is prescribed in advance, it must restrict to `M_P` and
map residual lowers onto residual owners.  The remaining exact condition is
ordinary Hall for a perfect residual `Q` in the incidence graph with `M0`
deleted.  This separates the fixed-`M0` matching gate from the component and
upper-ticket gates.

## 7. Reproducibility and scope

Primary C6 source and artifacts:

```text
scratch/threadD_k17_q3_fusion_hypertree_20260801.cpp
SHA-256 99262f8eb4c7c0885c68e136be375a586b2ddddfceb6dd2c60db2b6446898c51

scratch/threadD_k17_q3_fusion_hypertree_20260801/audit.json
SHA-256 a28613688ac0309cc49376d9a1d418c1845130ed979289a33889b432fdb96fae

scratch/threadD_k17_q3_fusion_hypertree_20260801/candidates.tsv
SHA-256 9e78cd030d7d99b350c256978d49faf94b6c439b998ba0c1b1293a1956db2597

scratch/threadD_k17_q3_fusion_hypertree_20260801/single_fusion_tickets.tsv
SHA-256 997a2070caa32e8182948cfc36caadba83d13099a48bc8c2cde45f7063ccc632
```

The independent implementation returned `PASS` with audit

```text
scratch/threadD_k17_q3_fusion_independent_replay_20260801/audit.json
SHA-256 1cc0ad6aaa69315c294551c3de33476581534c5d59d441167b0ce0abc0a59997
```

and independently reproduced every catalogue count, component triple, and
single-fusion ticket extremum above.

Dynamic C6 sweep:

```text
scratch/threadD_k17_q3_all405_regeneration_sweep_20260801.cpp
SHA-256 1f589e732407d16e66ffc3918b84fbaaeb7f470ef73498932c015a1086cf0249

scratch/threadD_k17_q3_all405_regeneration_20260801/audit.json
SHA-256 daa0c1618d35634546b0a56f25fe58cfc0cfce27d9d9026ff9dae8599864c2c6

scratch/threadD_k17_q3_all405_regeneration_20260801/sweep.tsv
SHA-256 ca61b59c789ce71788e3ca056a91a96a7005f14c21c65912c0b96ce32d3e049f
```

Generic C8 source and final-net artifacts:

```text
scratch/threadD_k17_q4_after_c6_sweep_20260801.cpp
SHA-256 8f76fff0d7cf9bbb37896326c2a52f8a1fd51344e60e12b25221fc647e4c2911

scratch/threadD_k17_q4_dynamic_7to1_20260801/finalnet.audit.json
SHA-256 4af1d1220338af35846ca5723c5f6dcac0e5258585259df00d434343a7b8c181

scratch/threadD_k17_q4_dynamic_7to1_20260801/finalnet.sweep.tsv
SHA-256 7914a5668ce6508555f229aea4b2840f7f018378e17236b64e4616b45b1397e7
```

All heavy runs used one H100 CPU core, `-O3`, an address-space cap of 2 GiB
and a CPU-time cap of 1,200 seconds.  Exact commands, PIDs, elapsed times and
hash manifests are in the corresponding `run_manifest.json` files.

No result in this note asserts exterior linear residence, arbitrary-width
upper preservation, a fixed directed `M0`, compiler/cap feasibility,
voltage, or regenerative all-parameter induction.  The exact surviving
gate is a support-changing/open connector or a larger resident q-port
packet which changes the occurrence catalogue and carries the authenticated
external ticket map.
