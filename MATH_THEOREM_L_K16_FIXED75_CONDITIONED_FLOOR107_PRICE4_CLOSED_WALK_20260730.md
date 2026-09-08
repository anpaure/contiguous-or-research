# K16 fixed75: a price-four closed-walk obstruction and conditioned floor 107

Date: 2026-07-30

## 0. Verdict

Let `F75` be the authenticated 75-seam block

\[
                         3C_{15}+C_{30}
\]

inside the frozen K16 211,604-seam source-relative bank.  There is no binary
balanced port-capacity-one selection of 106 seams which contains `F75` and
services all 93 frozen targets.  Since the independently authenticated
five-lock automaton already excludes counts at most 105 in the larger
balance/service relaxation, every such selection containing `F75` has

\[
                              |X|\ge 107.              \tag{0.1}
\]

This is a theorem about the named fixed face.  It is not a global floor 107,
does not exclude count 106 after changing the D4 block, and does not assert a
K16 carrier or literal word at count 107.

The decisive obstruction is much smaller than the full 1,024-profile atlas.
After `F75` is fixed, mark the three residual price-four targets

\[
                 T=\{46811,56173,60854\}.             \tag{0.2}
\]

Every admissible residual directed closed walk meeting one member of (T)
has exact-dual slack at least three, and no residual directed closed walk of
slack at most five meets two members of (T).  A count-106 residual packet
has total slack at most five but must service all three members once.  Its
cycle decomposition is therefore impossible.

## 1. Frozen ledger and the residual-31 face

For a seam (e:u\to v), write (H(e)) for its frozen service set.  The exact
scale-two certificate gives target prices

\[
 b_t\in\{1,2,4\},\qquad \sum_t b_t=207,
\]

an integral port potential (y), and nonnegative integral slack

\[
 s(e)=2+y_v-y_u-\sum_{t\in H(e)}b_t.                 \tag{1.1}
\]

The authenticated D4 audit proves the following exact facts about `F75`.

1. It is a balanced capacity-one set of 75 tight seams on 75 ports.
2. It services 60 targets once, with price histogram
   (45\cdot2+15\cdot4=150).
3. Its complementary 33 targets have price histogram
   (15\cdot1+15\cdot2+3\cdot4), of total price 57.

Suppose (X\) were a count-106 balanced capacity-one service selection
containing `F75`, and put

\[
                         P=X\setminus F75.            \tag{1.2}
\]

Then (P) has 31 seams, is balanced and capacity one, and avoids every port
occupied by `F75`.  Telescoping (1.1) around the balanced selection gives

\[
 2|X|=212=207+Q+R,\qquad Q+R=5,                      \tag{1.3}
\]

where (Q) is repeated target price and (R=\sum_{e\in P}s(e)).

The authenticated five-lock normal form says that every integral equality
profile is a word in

\[
                         \{S,0,1,2\}^5.               \tag{1.4}
\]

At each lock, `S` contributes one unit to scalar slack, while a digit chooses
one of the three residual price-one targets to repeat once.  Thus every
profile has

\[
 0\le R\le5,
\]

repeats only residual price-one targets, hits no target already serviced by
`F75`, and services every member of (T) exactly once.  The profile counts
are

```text
R          0    1    2   3   4  5
profiles 243  405  270  90  15  1
```

for a total of (4^5=1024).

The exact residual-31 reduction and atlas are proved in
`MATH_THEOREM_L_K16_FIXED75_C106_RESIDUAL31_FIVE_LOCK_PORTAL_BLOCKS_20260730.md`.
The atlas itself is

```text
scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json
SHA-256 a08a6d8f42b9e9e70b0e7278edfd5492032eb7733a3710c53e821101597a7125
payload b892695f00b0bc1120c3d9dd0c920b573cf36954e5aac0c236c4685f566b2ce0
```

## 2. The exact clean graph

Let (G_{\le5}) be obtained from the raw seam bank by deleting a seam when
any of the following holds.

1. It touches one of the 75 ports occupied by `F75`.
2. It services a target already serviced by `F75`.
3. It has slack greater than five.

### Lemma 2.1 (clean-graph necessity)

Every seam of the hypothetical residual packet (P) lies in (G_{\le5}).

#### Proof

The first deletion follows from port capacity one while `F75` is retained.
The second follows from the integral count-106 normal form, which permits
repeats only among the fifteen residual price-one targets.  The third follows
from nonnegative integral seam slack and (R\le5).  QED.

Raw replay gives the exact partition

```text
raw seams                          211604
removed for a fixed port             2550
removed for an F75 target hit         3273
removed for slack > 5                   87
retained clean seams                205694
```

and clean slack histogram

```text
slack       0      1      2      3      4     5
arcs    38935  32280  73713  29468  29817  1481
```

There are exactly 180 clean seams meeting (T), at 150 distinct heads.
Every one meets exactly one member of (T).  Their target/slack histogram is

```text
target   slack 0  slack 1
46811          51        9
56173          54        6
60854          53        7
```

## 3. State-expanded closed-walk pricing

For a clean seam (e), let

\[
 m(e)\subseteq T
\]

be its marked-target set.  Form the state digraph

\[
                         V(G_{\le5})\times2^T.         \tag{3.1}
\]

A seam (e:a\to b) induces

\[
 (a,M)\longrightarrow(b,M\cup m(e))
\]

with cost (s(e)).  All costs are nonnegative integers.

For each marked provider occurrence (e:u\to v), run Dijkstra from
((v,\varnothing)).  A return state ((u,M)) gives the closed walk consisting
of (e) followed by the return path, with union mask

\[
                         m(e)\cup M.                  \tag{3.2}
\]

Distances are truncated at six, where the stored value six means only “no
walk of total slack at most five”; it is not claimed as the exact unrestricted
minimum.

### Lemma 3.1 (completeness of marked-provider pricing)

The procedure above finds every marked-target union realized by a clean
directed closed walk of total slack at most five.

#### Proof

Take any such closed walk with a marked occurrence and choose one marked seam
occurrence (e:u\to v) on it.  Deleting that occurrence leaves a directed
return walk from (v) to (u).  State (3.1) records exactly the union of the
marked targets on the return walk, and Dijkstra finds a return of no greater
cost.  Conversely every returned state concatenated with (e) is a clean
closed walk with the recorded union and cost.  QED.

The exact output table is

```text
marked union mask   000  001  010  011  100  101  110  111
minimum/truncation    6    3    3    6    3    6    6    6
```

Thus each specified singleton costs at least three, and no walk of slack at
most five covers a pair or the triple.  The singleton lower bounds are sharp:

```text
target 46811 : 117908,192438,66749,207530,209317
target 56173 : 147007,173135,95845,207729,208837
target 60854 : 88808,177906,146769,207327,208895
```

Each displayed five-seam closed walk has total slack three.  Their ordered
seam-list hashes are respectively

```text
06b428ea73a36ea4e73b5f3007a398d0fa8550f71b17bbbc77bf15acc726e804
d056ed4b924f057e7ba62f07e3f7f3f856866d0d41425782f0ec1b5af517eecd
eb6d4cf0e91b4ff23df212ca7cffc86a2518f37094bb4a9eac4d38ae07108399
```

The audit checks all 180 marked provider occurrences and all eight return
coverage states for each.  Separate pair and triple rows explicitly record
zero survivors at slack at most five.

## 4. The conditioned floor theorem

### Theorem 4.1 (no fixed75 completion at count 106)

There is no binary balanced port-capacity-one count-106 selection in the
frozen source-relative seam bank which contains `F75` and services all 93
frozen targets.

#### Proof

Assume (X) exists and form (P) as in (1.2).  Balance and capacity one
decompose (P) into vertex-disjoint directed simple cycles.  Lemma 2.1 puts
every cycle inside (G_{\le5}).  Every member of (T) has residual demand
one.

If one selected cycle services two members of (T), Lemma 3.1 says that its
slack already exceeds five, contradicting (R\le5).  Otherwise the three
members of (T) lie on at least three marked cycles.  Each such cycle has
slack at least three, so

\[
                         R\ge3+3+3=9,                 \tag{4.1}
\]

again contradicting (R\le5).  QED.

The same argument works after relaxing packet count, residual capacity, and
all other target rows, provided the residual circulation remains integral and
the exact clean-graph deletions remain valid.

### Corollary 4.2 (fixed75-conditioned source-relative floor 107)

Every binary balanced capacity-one service selection in the frozen seam bank
which contains `F75` has at least 107 seams.

#### Proof

The authenticated five-lock automaton excludes counts at most 105 even in a
larger source-relative balance/service relaxation.  Theorem 4.1 excludes the
only remaining count, 106, on the `F75` face.  QED.

## 5. Structural subfaces retained as explanation

The earlier portal/cycle-block analyses remain useful explanations, although
Theorem 4.1 supersedes them logically.

* At (R=0), the clean cyclic core is exactly
  (5C_3+C_{45}), with cycle lengths (3,3,3,3,3,45).  It has no provider
  for any member of (T), so all 243 all-repeat profiles are fractionally
  infeasible.  This is frozen in
  `scratch/l_k16_fixed75_c106_r0_cycle_columns_20260730.audit.json`, SHA-256
  `1161f4ddb730ca371d2bc224ed97f315420b580f3bdb875e6021176a97fd4dc0`,
  payload
  `a35efec6613f9b45ad255913c63ce6ac616ea15a2d3f39d649e8304657e7dd11`.

* At (R=1), exactly fifteen slack-one portals have a tight return.  Every
  one is a chord of the (C_{45}), and its unique simple return produces a
  length-29 macro.  With the five disjoint (C_3) fillers, attainable packet
  sizes are (29,32,35,38,41,44), never 31.  More directly, all 75 arcs in
  the one-slack cyclic core have zero incidence on (T).  Hence all 405
  one-slack profiles fail.  The standalone solver-free v2 audit is
  `scratch/l_k16_fixed75_c106_s1_portal_cycle_columns_v2_20260730.audit.json`,
  SHA-256
  `559f18c9b4d091b43e8c059b0cbaa1cb46d46f3d66fad04fc0fea7441746e590`,
  payload
  `62d23edaeef9e138466c85c7ec10bec41d79b8b5303d135abede1e36ab2f4bc7`.

Neither special-case proof is needed to exclude (R=2,3,4,5); the marked
closed-walk theorem handles all six slack strata simultaneously.

## 6. Proof artifacts and replay

The authoritative solver-free driver is

```text
scratch/audit_l_k16_fixed75_c106_price4_closed_walk_floor107_20260730.py
SHA-256 8e2da3e326666255f21fbe2312b3c9e6ce97f22d96893147fc29175f20e3f1b5
```

Its authoritative v2 output is

```text
scratch/l_k16_fixed75_c106_price4_closed_walk_floor107_v2_20260730.audit.json
SHA-256 58915e7da037ebba28e230dcd71e3084d1c4aacbfec80c5fc024128943550d7f
payload 6451cab631029429efb2548cd63ccbd3ec3417f6bf5aa0d383946aed413399b9
```

The driver pins:

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
SHA-256 a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2

scratch/l_k16_d4_cycle_blocks_20260730.audit.json
SHA-256 b9dca4325deac03fa8575ad755db2cf54b777f1dd8811009d2e35f25e5eaa7a8

scratch/l_k16_fixed75_residual31_c106_atlas_20260730.audit.json
SHA-256 a08a6d8f42b9e9e70b0e7278edfd5492032eb7733a3710c53e821101597a7125
```

A fresh root replay was byte-identical to the authoritative v2 JSON and
reproduced all 205,694 clean arcs, 180 marked providers, the complete
eight-entry cost table, and all 1,024 rejected signatures.

## 7. Exact boundary

What is proved:

1. all 1,024 integral count-106 profiles on the exact `F75` face are
   impossible;
2. the obstruction survives deletion of packet-count, residual-capacity,
   and thirty other target-service rows;
3. any global count-106 construction must leave this exact D4 face.

What is not proved:

1. a global source-relative floor 107;
2. infeasibility after changing or partially replacing `F75`;
3. a fractional-flow no-go—the clean-graph slack truncation and the (4^5)
   normal form are integral;
4. a count-107 reduced witness, physical carrier, residence-preserving
   factor, compiler certificate, or literal word.

A separate all-slack fractional experiment based only on support masks is
not used here: support masks do not record multiple occurrences of the same
marked target on one cycle.  The theorem above relies only on the exhaustive
integral closed-walk state calculation and cycle decomposition.
