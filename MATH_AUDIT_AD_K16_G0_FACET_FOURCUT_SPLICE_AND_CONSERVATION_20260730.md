# AD audit: K16 G0 facet four-cut splice and the true conservation gate

Date: 2026-07-30

Status: the requested tail-fixed four-cut chronology has been constructed and
audited exactly.  It preserves the rank-eight multiset, G0 and adequate scalar
capacity, and it has raw envelope supply for all three distinguished lower
facets.  It is **not** a feasible chronology: five middle rows fail exact
maximal-envelope recovery and four upper masks are lost.  Consequently a full
static lower atlas is not semantically defined for this row.  The failure
gives a sharp carrier-run and upper-halo obstruction, not a three-mask parity
invariant.

## 1. Authenticated input and notation

Let `S=(S_0,...,S_12872)` be

```text
scratch/k16_resident_state2_upper2_targets.txt
SHA-256 77dd098d7e066cd81ed68846d554c5e5a7247e90ec764033394287f312c28464.
```

It is the authenticated rank-eight state2 chronology.  The two already
audited upper-complete standard pattern-4 rethreads are `u0` and `u1`:

```text
u0 target SHA 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
u1 target SHA 6d1f85644ed71212d29405d2595cb538e386cb8055632f0797fa5350b4b339e0.
```

For a G0 chronology `T`, let `d_i` be the forced delivery depth, initially
three and decreasing by one after each adjacent repeated middle target.  Its
maximal source envelope is

```text
E_p = intersection {T_i : i <= p <= i+d_i}.                 (1.1)
```

The chronology is envelope-valid exactly when every `E_p` is nonempty and

```text
T_i = OR(E_i,...,E_(i+d_i))                                 (1.2)
```

for every row `i`.

## 2. The Boolean facet triangle

Put

```text
Q = 0x4c79,
K = 0x4831,
a = 0x0008,  b = 0x0040,  c = 0x0400.
```

Then the three residual lower masks are precisely

```text
A = 0x4c71 = K union {b,c} = Q\a,
B = 0x4879 = K union {a,b} = Q\c,
C = 0x4c39 = K union {a,c} = Q\b.                           (2.1)
```

Thus every pair among `A,B,C` has union `Q` and their common intersection is
`K`.

The complete audited tail-fixed standard 2/3-opt census has exactly two rows
passing G0, capacity, exact envelope recovery and every upper target.  In the
coordinate order `(A,B,C)` their exact host vectors are

```text
u0 : (0,1,1),
u1 : (1,0,0).                                               (2.2)
```

The unique hosts are

```text
u0 B : [9717,9719), E=(0x4871,0x4079), Mandatory=0x0818;
u0 C : [12164,12166), E=(0x4c31,0x4c29), Mandatory=0x0c18;
u1 A : [3279,3282), E=(0x0c61,0x0471,0x4461), Mandatory=0x4830.
```

This proves an exchange obstruction inside the complete standard 2/3-opt
class.  It does not prove a global invariant.  Indeed the separately audited
capacity-32174 commutator has host vector `(1,0,1)` in the order `(A,B,C)`.
The real conflict is the canonical use of the unique owner `Q`: `u0` puts it
after the first flat beside `0x4a79` to make `B`, whereas `u1` leaves it before
the first flat beside `0x4c75` to make `A`.

## 3. The requested four-cut splice

The exact target sequence `F` is

```text
F = S[:3280]
    | S[12826:12827]
    | S[6389:12826]
    | S[3280:5726]
    | S[5726:6389]
    | S[12827:].                                            (3.1)
```

Equivalently, cut after source positions

```text
3279, 6388, 12825, 12826
```

and use block order

```text
A | v | C0 | X' | Y | D.
```

This preserves every rank-eight multiplicity and fixes the suffix beginning
at position 12827 literally.  It places the following three Johnson edges in
the chronology:

```text
0x4c75 -- 0x4c79, intersection 0x4c71;
0x4c79 -- 0x4a79, intersection 0x4879;
0x4d39 -- 0x4e39, intersection 0x4c39.                      (3.2)
```

The frozen chronology is

```text
scratch/ad_k16_g0_facet_fourcut_splice_20260730.targets.word
SHA-256 673dffa6aa44f180299ccd2332f6568bb1bd164eac4dcbccf3c50f704d8031e2.
```

### Theorem 3.1 (exact G0 and capacity ledger)

The splice `F` has flat starts

```text
3324, 12869, 12871,
```

depth histogram

```text
{3:3325, 2:9545, 1:2, 0:1},
```

and scalar proper-prefix capacity

```text
29067 > 26332.
```

#### Proof

The first repeated pair `S_6432=S_6433` lies in `C0` and moves to start
3324.  The two terminal pairs lie in the fixed suffix.  The displayed depth
histogram follows immediately, and its weighted sum is

```text
3*3325 + 2*9545 + 1*2 = 29067.
```

No deadline exits the word.

## 4. Exact carrier failure

### Lemma 4.1 (bit-run carrier criterion)

For a coordinate bit `z`, write `t_i(z)=1` when `z in T_i`.  Under (1.1),
`z in E_p` exactly when

```text
t_i(z)=1 for every i with i<=p<=i+d_i.                      (4.1)
```

Hence row `i` delivers its required bit `z` exactly when at least one
`p in [i,i+d_i]` satisfies (4.1).  In a region of constant depth `h`, away
from a depth boundary, this is equivalent to every positive incidence run
having length at least `h+1`.

#### Proof

The first assertion is the bitwise form of the intersection in (1.1).
Equation (1.2) contains bit `z` precisely when one of its `h+1` envelope
cells contains `z`.  In a constant-depth region, `E_p` contains `z` exactly
when the `h+1` rows ending at `p` all contain it.  Such a window contains a
given positive row if and only if its positive run has length at least
`h+1`.

### Theorem 4.2 (complete middle failure ledger)

All maximal envelopes of `F` are nonempty, but exactly five middle rows fail
(1.2):

```text
row   target   recovered   lost
3281  0x6639   0x6239      0x0400
3282  0x6719   0x6319      0x0400
3283  0x6798   0x6398      0x0400
9717  0xca71   0xca61      0x0010
9718  0x6479   0x6469      0x0010.                         (4.2)
```

The first three failures are exactly the length-three positive run of bit 10
on `[3281,3284)` in the depth-three region.  The last two are exactly the
length-two positive run of bit 4 on `[9717,9719)` in the depth-two region.
Each run is one row shorter than Lemma 4.1 permits.

Thus `F` is not an envelope-valid chronology.  In particular, the exact
`Mandatory` mask of a lower cell is not semantically defined by a valid
middle carrier, so a complete static lower atlas must stop fail-closed here.

## 5. Exact upper loss and raw facet supply

### Theorem 5.1 (upper loss)

The unrestricted accumulated-union replay of `F` misses exactly

```text
{0x6c79,0xca79,0xea79,0xeb79}.                              (5.1)
```

Each had a unique target-level witness in `u0`, and the splice destroys all
four:

```text
0x6c79 : [9717,9719),
0xca79 : [9715,9717),
0xea79 : [9714,9717),
0xeb79 : [9713,9717).                                      (5.2)
```

This is a literal all-width replay; it is not a q1-only screen.

Despite the failures, the maximal-envelope arrays have exactly one raw
supply/nonempty interval for each facet:

```text
A : [3279,3282), E=(0x0c61,0x0871,0x4031), OR=A;
B : [3280,3283), E=(0x0871,0x4031,0x4019), OR=B;
C : [12164,12166), E=(0x4c31,0x4c29), OR=C.                (5.3)
```

These rows prove that there is no mask-count or parity law forbidding all
three facet supplies.  They are not physical lower hosts, because Theorem
4.2 invalidates the middle carrier and therefore the `Mandatory` ledger.

## 6. The actual local conservation law

### Lemma 6.1 (clean depth-two seam duality)

In a uniform depth-two region with consecutive middle rows

```text
L, X, Y, R,
```

put `J=X intersect Y`.  The two envelope cells straddling the edge `X-Y` are

```text
L intersect X intersect Y,
X intersect Y intersect R.
```

Their union equals `J` if and only if

```text
J subseteq L union R.                                      (6.1)
```

#### Proof

Both cells are subsets of `J`.  A bit of `J` occurs in their union exactly
when it occurs in `L` or `R`.

For two consecutive ears `P-Q-Z` with exterior rows `L,R`, simultaneous
exposure of `P intersect Q` and `Q intersect Z` requires

```text
P intersect Q subseteq L union Z,
Q intersect Z subseteq P union R.                          (6.2)
```

Take

```text
L=0xca71, P=0x4a79, Q=0x4c79,
P intersect Q=B,
Q intersect Z=A.
```

Because bit `0x0008` belongs to `B` but not to `L`, while
`Q intersect Z=A` forces `0x0008` to be absent from `Z`, the first condition
in (6.2) fails.  Therefore the naive hinged portal can create canonical `A`
only by destroying canonical `B`.  This is the precise local facet
conservation law.  It is not a global no-go: a successful chronology may
create one facet at a different owner or cell.

The upper ledger (5.2) is coupled to the same portal.  The dependency window
of the unique `u0` host for `B` is target rows `[9713,9721)`, exactly the
window containing all four unique upper witnesses in (5.2).  A rethread that
moves the canonical `B` portal must therefore transport both its lower
carrier halo and its upper residence halo.

## 7. A positive local ladder and its exact depth obstruction

Consider the seven-row Johnson ladder

```text
0x0e75, 0x4c75, 0x4c79, 0x4a79,
0x4e39, 0x4d39, 0x5d31.                                   (7.1)
```

At uniform depth one its consecutive edge intersections are

```text
0x0c75, A, B, 0x4a39, C, 0x4d31.
```

The union of the two incident intersections recovers each of the five
internal middle rows.  Hence (7.1) is an exact local depth-one middle compiler
and exposes `A,B,C` as singleton cells.

At depth two, however, the triple-intersection envelopes are

```text
0x0c71, 0x4871, 0x4839, 0x4839, 0x4c31.
```

The row `0x4a79` recovers only `0x4879`, losing bit `0x0200`.  Thus the same
ladder is rigorously impossible at depth at least two in this form.  In the
tail-fixed G0 schedule, depth one occurs only at starts 12870 and 12871, so a
five-row depth-one core cannot be inserted without moving or reshaping a
terminal flat.

### Theorem 7.1 (exact longer depth-two ladder)

The depth-one limitation is local to the short five-core.  In a uniform
depth-two band, take the consecutive rank-eight rows

```text
0x1ec5,0x0ee5,0x0e75,0x4c75,
0x4c79,0x4a79,0x4e39,0x4f29,
0x0f39,0x4d39,0x4c3b,0x443f,
0x047f,0x446f,0x644f,0x744d.                              (7.2)
```

Every adjacent pair is Johnson-adjacent.  Beginning at the third displayed
row, the depth-two triple-intersection envelopes are

```text
0x0e45,0x0c65,0x0c71,0x4871,0x4839,0x4a29,0x0e29,
0x0d29,0x0c39,0x4439,0x043b,0x042f,0x044f,0x444d.          (7.3)
```

For every internal row from `0x4c75` through `0x446f`, the OR of its next
three envelopes is exactly that row.  Moreover the two-cell envelope ORs

```text
0x0c71 OR 0x4871 = A,
0x4871 OR 0x4839 = B,
0x0c39 OR 0x4439 = C                              (7.4)
```

supply all three facets without a middle-carrier defect.  Thus a genuine
depth-two cross-basin portal exists locally.  What remains unproved is a
whole-deck segment routing which embeds (7.2), retains G0 flat placement,
preserves all upper residence intervals, and passes the global mandatory and
all-lower atlas.

The displayed rows occur in the authenticated base at indices

```text
3275,3276,3277,3278,3279,12826,5726,5727,
5410,5725,6301,3826,5566,5567,5568,5569.
```

An independent source-index, Johnson-edge, envelope, middle-recovery and
facet-supply audit is

```text
scratch/ad_k16_g0_depth2_facet_ladder_20260730.audit.json
  SHA 2ec5d59585eebe7779599abbbbeab2c549d61586bba253edef4023bad94c7aa4
  payload aebba41580016f745086dab582c21752581052c958c6c4b7bb38d556988df859.
```

## 8. Exact next gate

The mask triangle itself is not the obstruction.  A successful tail-fixed
continuation must do one of the following:

1. Preserve the exact ordered `u0` dependency windows
   `[9713,9721)` and `[12160,12168)`, thereby retaining the unique `B` and `C`
   hosts and the four upper witnesses, and create a noncanonical `A` host.
   There are exactly 42 `u0` proper-prefix cells with no mandatory-outside or
   disjoint-envelope defect and exactly one missing `A` bit.  Their missing
   bit histogram is

   ```text
   0x0001:7, 0x0010:4, 0x0020:6, 0x0040:7,
   0x0400:6, 0x0800:7, 0x4000:5.
   ```

2. Embed the exact depth-two ladder (7.2) by a whole-deck guarded segment
   routing, while retaining every upper residence interval and checking the
   complete global mandatory/all-lower atlas.

3. Leave the present tail-fixed family and create a depth-one band of at
   least five internal rows by moving or reshaping the second/third flat.

The complete fixed-three-plus-one standard four-cut census has already ruled
out its 617,568 representations.  Thus item 1 is now a genuinely guarded
collar problem, not another unrestricted replay of that closed class.

## 9. Correction of the apparent 14-row halo

The proposed 14-row move is exactly the identity:

```text
source block       [3278,3292) = inclusive [3278,3291]
length             14
destination before 3278.
```

The block already starts at 3278 and contains both the alleged anchor
`0x4c75` at its first position and donor `0x4c73` at its last.  Removing and
reinserting it at 3278 leaves `u0` byte-for-byte unchanged.  Frozen copies and
the explicit audit are

```text
scratch/ad_k16_g0_halo14_identity_20260730.targets.word
  SHA 9a96c2c5a1ea6f14eb208a1a800f36853c4765b08c3a56b16c6889f0cca3f14b
scratch/ad_k16_g0_halo14_identity_20260730.max_envelope.word
  SHA 57669ee5934872f766cdd1666f5a418d6710040f1edafe2c59f2d8ddf146b54a
scratch/ad_k16_g0_halo14_identity_20260730.audit.json
  SHA 21fa4184716fbbbc27318dea3b72013abd72ca42e0db979bb61e08c6ab7ed30a.
```

It inherits `u0`'s sole zero host `A=0x4c71` and is not a new candidate.

## 10. Reproducible audit and scope

```text
scratch/audit_ad_k16_g0_facet_fourcut_splice_20260730.py
  SHA 57e5bb0bb33b3d039dd7410eef5a71560372aa906d277a2e61209da10a855940
scratch/ad_k16_g0_facet_fourcut_splice_20260730.audit.json
  SHA ea6ec27855aa57f1b683b03dc9203bf4f9b547273e2c0c9c7adbbdf017e89dcc
  payload 08a1256959128f59c38ec4d94a3804ac2d457ee637d74921aa20bdf6ba523119.
scratch/audit_ad_k16_g0_depth2_facet_ladder_20260730.py
  SHA 25328f09671cfe22e9e3a3d0857409163e323a6e0954b1007137c5dbded8d677
```

No solver was invoked.  This closes the displayed four-cut splice only.  It
does not exclude guarded collars around the 42 near-host cells, movable
original cuts, terminal-flat moves, longer depth-two ladders, or arbitrary G0
chronologies.  No K16 bound changes.
