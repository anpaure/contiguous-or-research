# K16 endpoint transport, all-schedule pin obstruction, and three-cut gate

Date: 2026-07-31  
Status: exact source-relative theorem; no unrestricted K16 claim

## 1. Authenticated endpoint transport

The starting target order is the seed0-derived deficiency-four carrier

```text
scratch/k16_fourfilter_def4_reversal_targets_20260731.word
SHA-256 0a3a34c4f4c5e7e0fd474909a1010f2ca6d6df895bb869ac79cbacfbb757a08b.
```

Its only adjacent-union rank-nine hole is `0xb8ce`.  Its complete upper
deficit is `{0xa9fe,0xb8ce,0xb8cf}`.

For a path order (T=(T_0,ldots,T_{W-1})), define the suffix reroot

\[
R_p(T)=T_0,ldots,T_p,T_{W-1},T_{W-2},ldots,T_{p+1}.
\]

It changes only the boundary adjacency: the old colour
(T_p\cup T_{p+1}) is replaced by (T_p\cup T_{W-1}).  Apply two such
reroots:

1. At (p=6173), the old seam is `0x3cce` and the new seam is `0xb8ce`.
   Thus the q1 hole is transported from `0xb8ce` to `0x3cce`.
2. In the new order, at (p=11009), the old seam is `0x3cea` and the new
   seam is `0x3cce`.  The old colour `0x3cea` had multiplicity two, so one
   copy survives.  The q1 deck is now complete.

The resulting order is

```text
scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word
SHA-256 9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b.
```

It contains every rank-eight mask exactly once.  Direct adjacent-union replay
covers all 11,440 rank-nine masks.  Complete arbitrary-width interval replay
leaves exactly

\[
H_1=\mathtt{0x3ceb}\quad(|H_1|=10),
\qquad
H_2=\mathtt{0xa9fe}\quad(|H_2|=11).
\]

## 2. Maximum-area schedule and exact Hall witness

The exact maximum-area three-hole schedule displayed with this order is

\[
X=(12870,12871,12872),qquad Y=(0,1,8589).
\]

Its selected proper-prefix area is 30,023.  The optimistic omitted-start
credit gives 30,032 cells; the literal boundary-truncated credit is
(3+2+1=6), hence the exact physical cell count is 30,029.  All maximal
envelopes are nonzero and every middle row replays.

The exact individual-pin graph has 358,122 incidences and matching

\[
26327/26332,
\]

so its deficiency is five.  The canonical alternating shore has 30 lower
targets and 25 cells.  It decomposes into four isolated zero-host targets

```text
0x29cc, 0x38c6, 0x8000, 0x898d
```

and the same 26-target/25-cell component already present in the deficiency-
four parent.  The latter has common core `0x0169` and target set

```text
0169 016b 017b 01e9 01eb 0369 03e9 0569 056b 0769 0969 096b 0979
09e9 0b69 0d69 11e9 1969 8169 816b 8179 81e9 8369 8569 8969 9169.
```

Thus q1 closure costs exactly one additional marginal Hall unit in this
schedule: the old three isolated targets become four, while the 26/25 core
persists.

## 3. Provider-length lemma

Let a depth-(d) P/Q schedule have (s) omitted starts.  For an upper target
(U), let (ho_U) be the largest number of consecutive middle owners
contained in (U).

**Lemma.** Every physical interval (J) whose literal OR is exactly (U)
has

\[
|J|\le d+s+ho_U.
\]

**Proof.** Remove the last (d) positions of (J).  Every selected start in
the remaining interval has its entire middle carrier contained in (J), so
its middle owner is a subset of (U).  At most (s) physical positions are
omitted starts.  The retained selected starts index consecutive middle
owners.  Hence at least (|J|-d-s) consecutive owners lie in (U), which is
at most (ho_U).  Rearranging proves the inequality.  □

For the authenticated endpoint-transport order,

```text
U       contained owners   run histogram       rho_U   pin-length bound
3ceb    45                 1^25 2^10           2       8
a9fe    165                1^66 2^31 3^11 4^1  4       10.
```

## 4. All-schedule fixed-order obstruction

Augment the exact three-start/three-deadline maximal-envelope event DAG by a
single capped physical pin for (U), using the provider-length bound from
Section 3.  The state records the two hole counts, the active exact middle
accumulators, pin phase, pin OR, and pin length.  Therefore the computation
is exhaustive over every monotone depth-three P/Q schedule of this fixed
target order.

For `0x3ceb`, the exact optimum is

```text
maximum selected area  25740
optimistic capacity    25749
X                      12870,12871,12872
Y                      0,1,12872
pin                    [12872,12872]
literal cell count     25746.
```

For `0xa9fe`, the exact optimum is

```text
maximum selected area  25743
optimistic capacity    25752
X                      6102,12871,12872
Y                      0,1,6101
pin                    [6096,6101]
literal cell count     25749.
```

Both optimistic capacities are below the required 26,332 lower targets.
Since every upper-complete realization must contain each pin, either
individual bound already proves:

**Theorem.** No monotone depth-three P/Q compiler on the fixed target order
`9142910f...` can be simultaneously upper-complete and lower-universal.

This is stronger than the deficiency-five failure of the displayed
maximum-area schedule.  A schedule-only pin search on this order is closed;
another target-order rethread is necessary.

## 5. Single-two-opt obstruction and the next topology

The two missing targets are incomparable and

\[
H_1\cap H_2=\mathtt{0x28ea},qquad |H_1\cap H_2|=7.
\]

No rank-eight middle owner is therefore contained in both.  If a two-opt
creates a new witness for a previously absent upper target, that witness
crosses a new seam, and both seam endpoints must be contained in the target.
Thus a two-opt repairing both holes must assign its two new seams separately
to (H_1) and (H_2).

Let (P(U)=\{i:T_i\subseteq U\}).  The exact cut-index intersections are

\[
P(H_1)\cap(P(H_2)-1)=\varnothing,
\qquad
P(H_2)\cap(P(H_1)-1)=\varnothing.
\]

Hence no single internal two-opt can create both missing upper witnesses.
A prefix or suffix reroot has only one new seam and also cannot do so.

There is also no genuine fixed-endpoint three-cut repair.  Colour the two
endpoints of a new seam serving (H_1) red and those of a seam serving
(H_2) blue.  Each seam uses two distinct old cuts; pairing the two endpoints
of one old cut merely reinserts the removed edge.  Two two-element subsets of
three cuts intersect.  At an intersecting cut, one old endpoint is red and
the other blue, so that old adjacent pair gives an index in one of the two
offset intersections displayed above.  Both intersections are empty, a
contradiction.

The first live target-order topology is therefore four fixed cuts or an
endpoint-changing composition such as suffix-reroot plus two-opt.

Because the current q1 deck is complete, any such braid must also preserve
all removed unique rank-nine colours.  For the displayed schedule, a
Hall-protected braid must additionally repair five independent marginal
defects: one host for each of the four isolated targets and one extra
neighbour/augmenting route for the 26/25 `0x0169` component.  If a move
preserves all old incidences, matching can rise from 26,327 to 26,332 only
through five augmentations; scalar capacity or upper coverage alone is not
sufficient.

The upper targets and Hall packet interact sharply.  `0x3ceb` omits core bit
`0x0100`, and no target in any of the five deficient components is contained
in it.  Thus an internal `0x3ceb` provider cannot itself supply any of the
five Hall exits; all five must occur at its boundary or at external ports.
The target `0xa9fe` omits core bit `0x0001`; among the five components only
the isolated targets `0x29cc` and `0x8000` are contained in it.  Hence the
26/25 packet and isolated `0x38c6,0x898d` still require at least three
boundary/external ports.  These are necessary port counts, not a sufficiency
claim for a rethreaded schedule.

More exactly, in component order

```text
0169-packet, 29cc, 38c6, 8000, 898d
```

the masks forced outside the two provider targets are

```text
provider 3ceb: 0100,0104,0004,8000,8104
provider a9fe: 0001,0000,1000,0000,0001.
```

This is the literal boundary-port signature a candidate three/four-cut
absorber must discharge.

## 6. Scope and authenticated artifacts

The result is exact for the displayed target order and the monotone
depth-three P/Q compiler architecture.  It does not exclude a three-cut or
larger rethread, a different target order, or a non-P/Q equality word.

```text
scratch/ad_k16_fourfilter_endpoint_transport_maxpq_hall_20260731.audit.json
  SHA 807fa0c274aed16ae99cb3269da1c16a19749f9e55f6887df9cb60344ddd5bd1
  payload b134dd2efa74f9939694156fc7ef62d486c950febc1967cf27ffcd8d1dee945b

scratch/audit_k16_endpoint_transport_upper_pin_capacity_20260731.py
  SHA 6dafa3b14a4e47a983330023143cfe83f1866ff5172f00b2cfacd0b808a9a5af

scratch/k16_endpoint_transport_upper_pin_capacity_20260731.audit.json
  SHA 5bd0ce5372b70219cce2aeff1bdf0f5ee8d7e4e0dde7b3ee7962f15c8322b1dc
  payload 0d0e8a50ae51818f76c7366ae613f5c89276edac895da7d8a76714ee5295c0b0

scratch/audit_k16_endpoint_transport_fixed5_dm_protected_pins_20260731.py
  SHA 29ea14fcbb5cfce5e4231030633470a73dd9b8ca7d6c6caacc61281f742bcb70

scratch/k16_endpoint_transport_fixed5_dm_protected_pins_20260731.audit.json
  SHA e4be9c659627a934fa2d7911206140ac59205866ed427a25c8a038c9db672a38
  payload 5f8186fbe22d0f7485756a764b2cdf0c68269960fa080606588edf276def39fd

scratch/audit_k16_endpoint_transport_upperpin_independent_20260731.py
  SHA 4940f768ea95a86d8e7d071ad3dc7700c832c267f1cc97b4e861f7bcd1dff7d1

scratch/k16_endpoint_transport_upperpin_independent_20260731.audit.json
  SHA 34cc7ed60b6aed00a68f0e91aee444f02bd527ad340f239cadfa99cfc091c613
  payload 074551e6243c55595362eb55c6d39ff2faad95e828563cf050fe9111b67bccb8
```

The last implementation is independent: it does not import the primary
event-DAG code and reproduces both optima and literal replays.
