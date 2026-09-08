# K17 joint 1930/1926/1923 strict-batch ancestry and topology bypass

**Date:** 2026-08-02  
**Status:** exact finite audit of the frozen K17 suffix.  This note does not
claim uniform renewal, upper completion, source realization, a lower
compiler, residency, or a word.

## 1. Frozen checkpoints

The authoritative chain is

```text
(R,H)=(1938,1733), manifest 284f2db5...
  -> (1935,1729), manifest 8f12c0dd...
  -> (1930,1721), manifest bf840621...
  -> (1926,1712), manifest 44171fe4...
  -> (1923,1702), manifest 097ec68b...
```

The last model is

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_joint_res1923_deep1702/model
SHA-256 7a80fe02517039df87bcf7f88860b1bbf201482952c1317bfbcd6aeb9d435a2c
```

Its two literal openings both have missing-upper vector
`[0,1463,237,2,0,0,0,0]`, hence `H=1702`.  The independent frozen replay
reports exact incidence degree, normalized boundary, all `16261` frozen
guards, ordinary non-`D` q1 `19412`, opened q1 `19448` in each orientation,
and one component.  The manifest file SHA-256 is
`097ec68ba65380d442dcfe4018b673db3854729213847e12f4482707d99fc2ba`.

## 2. Strict links through 1930 and 1926

Put `Phi=2R+H` per opening.  Fresh O3 C++ replay gives the following exact
actual-tail prefixes; all rows are identical in both openings.

| link | primitive | family | core | `(R,H,Phi)` | primitive delta `(dR,dH,dPhi)` |
|---|---:|---:|---:|---:|---:|
| 1935/1729 -> 1930/1721 | 1 | O | 66472 | `(1933,1727,5593)` | `(-2,-2,-6)` |
| | 2 | C6 | 90396 | `(1933,1724,5590)` | `(0,-3,-3)` |
| | 3 | O | 43904 | `(1932,1722,5586)` | `(-1,-2,-4)` |
| | 4 | O | 33894 | `(1930,1721,5581)` | `(-2,-1,-5)` |
| 1930/1721 -> 1926/1712 | 1 | O | 9441 | `(1929,1720,5578)` | `(-1,-1,-3)` |
| | 2 | O | 2259 | `(1928,1717,5573)` | `(-1,-3,-5)` |
| | 3 | C6 | 1756 | `(1928,1714,5570)` | `(0,-3,-3)` |
| | 4 | O | 2665 | `(1927,1713,5567)` | `(-1,-1,-3)` |
| | 5 | O | 45130 | `(1926,1712,5564)` | `(-1,-1,-3)` |

At every displayed prefix the auditor independently verifies exact circuit
geometry, current-tail alternation/applicability, `48620` selected incidence
edges, exact lower/owner degrees, protected edges, all frozen guards, one
component, ordinary/opened q1, and zero literal upper-deck loss relative to
both the preceding state and the link root.  Every saved cumulative batch
model is assignment-identical to the reconstructed prefix.

Thus the first link is exactly `3 O + 1 C6`, with payload `(-5,-8)` and
`dPhi=-18`; the second is exactly `4 O + 1 C6`, with payload `(-4,-9)` and
`dPhi=-17`.  Neither is an authenticated `4Q+U` decomposition for the
calibrated payload classes `Q<=(-1,+1)` and `U<=(+3,-7)`: the first contains
three `Q`-bounded primitives and one `(0,-3)` C6, while the second contains
four `Q`-bounded primitives and one `(0,-3)` C6.  In particular, the fifth
primitive of the latter is not a `U` packet merely because the packet count
is five.

## 3. The 1926 -> 1923 order obstruction

The endpoint batch contains four pairwise commuting incidence supports:

```text
id 1: O  core 49734
id 2: O  core 1205
id 3: C6 core 68485
id 5: C6 core 55436
```

The saved producer order `1,2,3,5` is not a strict path: after id 3 the
factor has two components.  Exhaustive replay of all `4!=24` orders against
the frozen guard bank gives exactly `12 PASS` and `12 FAIL`.  The exact rule
is

```text
an order is strict  <=>  id 1 or id 3 is last.
```

Equivalently, no proper prefix may contain both `{1,3}`.  This is stronger
and more precise than a simple precedence `5<3`: for example order `2,3,5,1`
passes although id 3 precedes id 5.

A canonical strict order is `1,2,5,3`.  Its exact prefixes are

| step | primitive | `(R,H,Phi)` | delta `(dR,dH,dPhi)` | two-opening new upper targets |
|---:|---|---:|---:|---:|
| 0 | `O(49734)` | `(1925,1709,5559)` | `(-1,-3,-5)` | `3,3` |
| 1 | `O(1205)` | `(1925,1704,5554)` | `(0,-5,-5)` | `5,5` |
| 2 | `C6(55436)` | `(1924,1703,5551)` | `(-1,-1,-3)` | `1,1` |
| 3 | `C6(68485)` | `(1923,1702,5548)` | `(-1,-1,-3)` | `1,1` |

Every prefix passes the same literal hard gates as Section 2, and the
reconstructed terminal assignment is byte-identical to the frozen model.
The link payload is `(-3,-10)` with `dPhi=-16` and geometry `2 O + 2 C6`.

## 4. Exact topology ticket

Let `W` be the smaller shore created by id 3 in the failed producer order,
after ids 1 and 2.  The exact split has

```text
|W| = 12738 vertices = 6369 lower + 6369 owner vertices,
complement size = 35882 vertices.
```

Immediately before id 3, the selected cut has two edges,
`120397,120565`.  Circuit id 3 removes both and adds no edge crossing this
shore, so the declared ledger is `2 -> 0`.  Circuit id 5 removes no crossing
edge and adds `101681,102774`, restoring `0 -> 2` at the endpoint.

Therefore the strict reordered ledger is

```text
id 5 first: 2 -> 4;  id 3 second: 4 -> 2.
```

This is an exact topology-ticket bypass: id 5 plants two crossing edges
before id 3 spends the existing pair.  The factor-level condition is not
"every primitive is connected"; it is the prefix cut inequality

```text
selected crossing capacity of every proper shore >= 1;
for a shore containing zero or two of the odd-degree vertices M,D,
parity strengthens this to >= 2.
```

The audited split shore has even cut parity, so its sharp threshold is `2`.
For this four-support Boolean cube, the only bad proper subsets are exactly
those containing `{1,3}`.  The two other supports together repair that cut,
which is why one of ids 1 or 3 must be the final commit.

## 5. Certified ancestry payload

The already frozen strict branch `1938/1733 -> 1935/1729` consists of
`O(3341), C6(6686), O(25361)`.  Combining it with Sections 2--3 gives a
strict, hard-legal suffix with `16` primitives (`11 O + 5 C6`):

```text
(1938,1733,Phi=5609) -> (1923,1702,Phi=5548),
delta (R,H,Phi)=(-15,-31,-61).
```

The last four supports are committed in strict order `1,2,5,3`, not their
non-strict producer order.  Because the supports commute and the independent
auditor checks terminal byte identity, this reordering preserves the exact
frozen child and all parent manifests.

## 6. Scope and renewal consequence

This example proves a finite topology-bypass fan: a packet can be a strict
path even when one natural ordering incurs topology debt, provided a
state-relative repair circuit is scheduled before the cut-consuming circuit.
It supplies a concrete sufficient ordering condition and an exact cut
ticket for this state.  It does not prove that every positive-residence state
has such a fan, nor any source/compiler/word conclusion.

Audit artifacts are frozen under:

```text
scratch/k17_joint_res1930_strict_lineage_20260802/
scratch/k17_joint_res1926_strict_lineage_20260802/
scratch/k17_joint_res1923_strict_reorder_20260802/
```
