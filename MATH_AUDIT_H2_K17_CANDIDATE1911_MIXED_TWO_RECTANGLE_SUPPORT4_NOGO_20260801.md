# Candidate1911 exact two-rectangle support-four no-go

Date: 2026-08-01  
Lane: H2 independent terminal-packet audit  
Status: **exact scoped no-go; no residence or global K17 claim**

## 1. Result

Fix the connected candidate1911 factor

```text
scratch/h2_k17_dev5_candidate1911.factor.tsv
SHA-256 c082621d6444dc2283675882557d0240babb989f2d31847eb198fbe8b4612587
```

It has one 1,430-owner quotient cycle, voltage `9 mod 17`, complete rank-10
turn palette, and lower-turn holes

\[
                         E=0x00e0f,\qquad F=0x01547.               \tag{1.1}
\]

Apply exactly two two-owner rectangles—DD, HH, or one on each side—with
union changed-owner support at most four.  There is no terminal packet that
repairs both lower holes.  Therefore none can also retain the upper palette,
connectivity, and voltage nine.

These faces are disjoint from the exhaustive one-simple-one-side circuit
run: DD/HH packets are two disjoint assignment circuits, while a DH packet
changes both matchings simultaneously.  All palettes are evaluated on the
terminal packet rather than by adding two independently safe deltas.

## 2. Exact rectangle and terminal formulas

For `M` equal to `D` or `H`, let its current incidences at distinct owners
`u,v` end at facets `f_u,f_v`.  A rectangle is a pair of cross incidences

\[
                         u f_v,\qquad v f_u.                        \tag{2.1}
\]

Replacing `u f_u,v f_v` by (2.1) preserves every owner and facet degree of
`M`.  Conversely every two-owner change of one perfect matching has this
form, with literal incidence IDs retaining parallel shift information.

For a D rectangle `R_D` and H rectangle `R_H`, construct terminal matchings
`D',H'` first.  Require their selected incidence sets to be disjoint.  At an
affected owner and facet compute directly

\[
\begin{aligned}
 L'_o&=\operatorname{can}\bigl(
       \operatorname{rot}(F(D'_o),s(D'_o))\cap
       \operatorname{rot}(F(H'_o),s(H'_o))\bigr),\\
 U'_f&=\operatorname{can}\bigl(
       \operatorname{rot}(O(D'_f),-s(D'_f))\cup
       \operatorname{rot}(O(H'_f),-s(H'_f))\bigr).                \tag{2.2}
\end{aligned}
\]

This direct formula is necessary when the rectangles overlap at an owner;
separate D-only and H-only turn deltas need not compose.

The terminal voltage is

\[
 V'=9+\sum_{e\in R_D}(s(e_{new})-s(e_{old}))
       -\sum_{e\in R_H}(s(e_{new})-s(e_{old}))\pmod {17}.          \tag{2.3}
\]

Finally traverse `H'^{-1}D'` literally.  The requested topology/voltage rows
are one quotient component of length 1,430 and `V'=9`.

## 3. Complete finite census

The exact incidence atlas contains

```text
D rectangles: 19
H rectangles: 20
raw mixed pairs: 19*20 = 380
```

On one side, distinct compatible rectangles have disjoint owner pairs.  The
same-side censuses are

```text
                         raw compatible     terminal edge-disjoint
DD                              164                    147
HH                              183                    165
```

No DD packet gains either old hole.  Eighteen HH packets gain only `E`; no
same-side packet gains `F` or both holes.

For mixed DH packets, the changed-owner union has size three for 17 pairs
and size four for 363.  After terminal D/H edge-disjointness, 336 pairs
remain.  Their direct checks give

```text
connected terminal factors:        156
voltage exactly 9:                  14
upper palette complete:             15
gain exactly one old lower hole:    18
gain both old lower holes:            0
lower palette complete:               0
full survivors:                       0
```

The local reason is already sharp.  Among all legal individual rectangles,

```text
                       E-provider rectangles    F-provider rectangles
D side                         0                         0
H side                         1 (rectangle 5)          0
```

A size-four packet changes each owner on at most one side, so this table
immediately forbids creation of `F`.  The only possible exception is a
size-three packet, where the D and H rectangles share one owner and the two
new incidences can jointly create a label absent from either one-side row.
All 17 such overlaps are included in the direct terminal census, and none
creates `F`.  Thus the missing `F` provider is an exact owner-local closure
obstruction, not a voltage or topology inference.

## 4. Smallest surviving partial seed

The unique H rectangle that can gain `E` is rectangle 5.  Its best mixed
partner under the terminal debt ordering is D rectangle 13:

```text
D owners: 15701,43691   old edges 9735,12864 -> new 9736,12863
H owners:  7455, 7711   old edges 3515, 3826 -> new 3514, 3830
```

This packet remains connected and repairs `E`, but

```text
voltage:          16
lower holes:      0x00b87,0x01547
upper holes:      0x01d9f,0x01f1f.
```

It is therefore not a candidate factor.  It is the smallest literal seed
for a third actuator whose four signed obligations are: restore `F`, restore
`0x00b87`, restore both upper colours, and correct voltage by `-7 mod 17`
while retaining connectivity.

## 5. Compact catalogue design

A C++ implementation needs only the following bounded pipeline.

1. Bind the factor TSV and reconstruct `by_owner_facet`, retaining every
   parallel incidence and shift.
2. For each matching, enumerate unordered owner pairs and both reciprocal
   cross-incidence lists; emit the 19 and 20 rectangles.
3. Pair disjoint-owner rectangles on each same-side shore, and pair every
   D/H rectangle.  Do not reject a mixed new incidence merely because it is
   selected by the old opposite matching; accept it when the opposite
   rectangle removes that edge, and test only terminal disjointness.
4. Recompute (2.2) on the union owners/facets, update exact multiplicity
   counters, then apply (2.3).
5. Traverse all 1,430 terminal successors.  Emit a factor only after every
   palette, voltage, and topology row passes.

This has only 380 raw terminal packets, so no SAT model or heavy solver is
needed.

## 6. Scope

The theorem covers every exactly-two-rectangle DD, HH, or DH packet with
union matching-owner support at most four.  It does not cover three or more
rectangles, a longer mixed alternating packet, reselection of candidate1911's
first circuit, residence, ranks at least 11, source/common-cap constraints,
or unrestricted K17.

## 7. Artifacts

```text
scratch/audit_h2_k17_candidate1911_mixed_two_rectangle_packets_20260801.py
scratch/h2_k17_candidate1911_mixed_two_rectangle_packets_20260801.audit.json
scratch/h2_k17_candidate1911_mixed_two_rectangle_packets_20260801.survivors.tsv
```

The survivor TSV contains only its header.
