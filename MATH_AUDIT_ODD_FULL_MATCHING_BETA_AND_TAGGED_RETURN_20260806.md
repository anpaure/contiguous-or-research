# Independent audit: corrected full-matching beta path and the exact tagged-return interface

**Date:** 2026-08-06  
**Files audited:**

* `MATH_THEOREM_ODD_FULL_MATCHING_TERMINAL_BETA_LOCAL_PATH_20260806.md`;
* `MATH_THEOREM_ODD_TAGGED_CHECKPOINT_BETA_TRAIN_RETURN_20260806.md`.

No computation is used.

## Verdict

The local beta conversion has a valid path in the actual matching
contraction, but the `B_1:0->2` branch in the current file contains one
incorrectly modelled `p_2` toggle.  With the physical scan geometry

```
u | v | b | g,
p_1=(g,b),
p_2=(v,u),
```

the correction is especially simple: the `p_2` matching edge changes the
displayed head coordinates and performs the next advertised local move for
free.  The corrected branch has four macrosteps, not five.  No external
relay clock is needed.

The marked train return is valid under three explicit hypotheses:

1. the transported head is scan-pair aligned so that its near block is
   exactly `p_2=(v,u)=20` at the beta source;
2. the physical corridor contains only the guardable alphabet
   `{20,01,21}`; and
3. a literal collar-order/source record disjoint from `p_1` persists until
   one target collar occurrence has been written.

The current global construction has not yet proved hypotheses 1 and 3, and
its all-guardable-corridor claim excludes the bounded midpoint/record
exceptions only by assumption.  Thus the local directed gate is closed
after correction, while the global odd collar remains conditional on one
alignment/copy-before-erase scheduling lemma.

## 1. Exact physical scan geometry

Take four consecutive physical coordinates in the order

```
u,v,b,g.
```

The root-adjacent boundary-last scan orders the two relevant pairs as

```
p_1=(g,b),   p_2=(v,u).
```

Thus the physical head value `uv=02` means that the ordered scan state on
`p_2` is `20`, which is quiet.  This reversal is load-bearing.  It is also
why a later `p_2` matching edge cannot be written as though it left the
four displayed coordinates unchanged.

The selected nonquiet involution is

```
01 <-> 10,
02 <-> 11,
12 <-> 21,
```

and the quiet states are `00,20,22`.

## 2. Corrected `B_1:0->2` path

The source and target are

```
0201 -> 0021.
```

The exact majority-to-majority route is

```
0201  =>  0120  =>  1011  =>  0102  =>  0021.
```

Every macrostep is one physical edge followed by the forced first-nonquiet
matching edge:

1. `0201 -> 0111` by `v->b`.  Now `p_1=11`, so
   `11->02` gives `0120`.
2. `0120 -> 1020` by `v->u`.  Now `p_1=02`, so
   `02->11` gives `1011`.
3. `1011 -> 1002` by `b->g`.  Now `p_1=20` is quiet, while
   `p_2=(v,u)=01` is first nonquiet.  Its edge `01->10` changes
   `(u,v)=(1,0)` directly to `(0,1)`, giving `0102`.
4. `0102 -> 0012` by `v->b`.  Now `p_1=21`, so
   `21->12` gives `0021`.

The fifth macrostep in the current theorem is therefore spurious.  At the
third matching edge the local state is `0102`, not `1002`; the displayed
physical move `1002->0102` must be deleted.

No later delimiter pair is changed.  The adjacent head pair `p_2` is the
only relay and its one toggle is part of the required conversion of the head
from `02` to the target block `00`; it is not supposed to be restored to its
source value at the local endpoint.

## 3. The other two branches pass

With the same coordinate order, the route

```
0221 => 1112 => 2021 => 2120 => 2201
```

is exact:

* `0221 ->1121`, then `p_1:12->21`, gives `1112`;
* `1112 ->2012`, then `p_1:21->12`, gives `2021`;
* `2021 ->2111`, then `p_1:11->02`, gives `2120`;
* `2120 ->2210`, then `p_1:01->10`, gives `2201`.

Here `p_1` is first nonquiet at every physical endpoint, even when `p_2`
is also nonquiet.  The neutral branch is the prefix

```
0221 => 1112 => 2021.
```

All physical transfers are legal and all forced matching edges are exactly
as displayed.

The mass-three branch is disjoint from the mass-five branches.  The neutral
and `B_1:2->0` branches share their initial local prefix, so the persistent
exterior source record is genuinely necessary: at `2021`, one source stops
and the other continues.  Conditional on such a fixed record, all majority
and minority states are source- and microstep-decodable.

## 4. A fixed second head is a valid local occurrence marker

If a scan-aligned double head is stopped immediately outside `p_1`, its
near head block is `p_2` and its far head block is the following scan block.
The beta path changes only the near head and `p_1`; the far `H=02` remains
literal throughout.  Since the beta support is at the fixed physical `p_1`
neighbourhood anyway, no unbounded address decoder is needed.  The fixed
second head further separates the beta phase from every ordinary tape phase.

This conclusion is conditional on **alignment**.  The double-head transport
theorem moves a train on whichever two-coordinate block lattice was chosen
for its collar and corridor.  It does not by itself prove that a head created
on the zipper connector-block lattice can be stopped as the scan pair
`p_2=(v,u)`.  A proof must either choose the fixed collar and its entire
transport on the scan-pair lattice from the outset or give a bounded
one-site rethreading lemma.  Merely saying that the head is “next to `B_1`”
does not establish (oriented) state `p_2=20`.

## 5. Changed train mass is not an obstruction

The outward train `H|H` has mass four.  After beta conversion the returning
train has one target block `E in {00,20,22}` and one unchanged head, hence
mass two, four, or six.

For a stationary mark of mass one, two, or three, the six-coordinate
train-plus-mark total lies between three and nine.  It is therefore strictly
between zero and the capacity twelve.  The capacity-two token graph on that
interval is connected, so a simple train/mark interchange exists.

The stationary-corridor proof already allows the return active word `X'` to
differ from the outward word `X`; it uses only fixed length, nonextreme local
mass, and a stationary occurrence guard.  Hence the changed train mass is
fully legitimate.  Its compensation occurred inside the beta path through
the opposite change of `B_1`, so global mass is constant throughout.

## 6. Endpoint parity without an external relay or guard

A train/block swap moves a four-coordinate train past a two-coordinate
block.  Its weighted token-position parity changes by

```
2*mass(train) - 4*mass(block),
```

which is even.  Changing one guardable block `Y` to its stationary mark
`mu(Y)` is one physical edge and is odd.  Therefore the selected `p_1`
endpoint toggles exactly once per block that is marked, not once per block
that is crossed.

This eliminates the proposed external `Y_0` register.  Choose an even number
of marked corridor blocks:

* if the corridor length `s` is even, mark all `s` blocks;
* if `s` is odd, leave the berth-adjacent block unmarked and mark the other
  `s-1` blocks.

The outward double head is itself a visible cart, so it can cross the one
unmarked endpoint block safely.  For odd `s>=3`, the remaining marked
corridor has length at least two and supplies the ordinary stationary return.
For `s=1`, use the fixed-berth one-interior path directly.  The cases `s=0`
and even `s` are immediate.

On return, every train/mark swap is even.  Erasing the even number of marks
is also even.  The last unmarked swap, when present, is at the named fixed
berth and is even.  Thus the local beta path is entered at its literal source
endpoint and the completed return preserves its literal target endpoint.

No external `p_2`, auxiliary parity mark, or selected-row endpoint choice is
used.  During the local `B_1:0->2` path the only relay is the actual adjacent
head pair `p_2=(v,u)`, as proved in Section 2.

## 7. The persistent exterior record is not currently derived

At the fully tagged checkpoint the two collar blocks are `H|H`.  Their
ordered source type has therefore been erased.  In the existing
copy-before-erase proposal, the remaining order class is stored in the
unordered selected row of `p_1`.

The beta path changes that row.  The residual signed count and `a_1`
determine only

```
epsilon(a)+epsilon(b),
```

not the ordered pair `(a,b)`.  For sums one, two, and three there are two,
three, and two possible ordered pairs respectively.  Consequently `H|H`
plus the residual count is not the persistent exterior collar record assumed
by the tagged-return theorem.

The theorem needs one genuine copy-before-erase operation before beta, for
example:

1. write one named complemented collar position first, so its value and
   physical side, together with the sum, recover the other digit; or
2. copy the three-valued order class into a disjoint literal row which is
   held fixed through beta.

The fixed second `H` is an occurrence marker, not an order-class record.
Without one of the two operations above, the neutral branch ending at
`2021` can meet the continuing mass-five branch after the old row record has
been erased.

## 8. The all-guardable corridor is also a real hypothesis

Ordinary fully tagged blocks lie in `{20,01,21}`.  The bounded unfinished
packet can additionally contain midpoint blocks `11`, and zipper interface
records need not belong to the guardable alphabet.  A mark `mu(20)=11` also
has the same literal value as a midpoint block, so one cannot silently treat
the exceptions as ordinary stationary marks.

The return theorem is correct when those exceptional occurrences are absent
from the physical corridor or have first been moved into a bounded protected
train.  The present global schedule has not yet proved that placement.  This
is exactly the “compensating occurrence assignment” which the candidate
correctly leaves open in its final section.

## 9. Correct conditional theorem

Assume:

1. a scan-aligned `H|H` train reaches the `p_1` neighbourhood with its near
   block equal to ordered scan state `p_2=20`;
2. the corridor, apart from a possible berth-adjacent unmarked block, is a
   word over `{20,01,21}`;
3. one named exterior record recovers `a_1` and the ordered collar after the
   `p_1` row changes; and
4. the compensating target block assigned to the beta head is the one needed
   by the global teardown ledger.

Then the even-mark outward transport, the corrected local path, and the
reverse marked return give a directed occurrence-labelled path

```
H|H at berth -> H|H at p_1 -> E|H at p_1 -> E|H at berth
```

which restores the literal target endpoint of `p_1`.  This theorem is
proof-safe and uses no endpoint register or external relay clock.

The remaining odd gate is now the bounded global preparation of hypotheses
1, 3, and 4, together with placement of the finitely many non-guardable
midpoint/interface blocks.  It is not a long-distance parity obstruction.

## 10. Addendum: a direct connector-lattice junction removes hypothesis 1

The alignment hypothesis above can be eliminated by working on two adjacent
connector blocks rather than first rethreading one head onto `p_2`.

Use five consecutive physical coordinates in the order

```
g,b,v,u,w,
```

with

```
p_1=(g,b),
C_1=(b,v),
C_2=(u,w).
```

After the setup half, the mixed first connector is

```
C_1=02  when a_1=0,
C_1=20  when a_1=1 or 2.
```

Put one collar head on `C_2` and keep a second collar head `C_3=02`
immediately beyond it.  The following three routes are exact paths in the
full matching contraction.

### The `a_1=0` route

```
10202 => 01211 => 11111 => 02201
      => 11210 => 21110 => 12200.
```

The physical moves are, in order,

```
w->u, v->b, u->v, w->u, v->b, u->v,
```

and the forced `p_1` rows are

```
10->01, 02->11, 11->02,
02->11, 12->21, 21->12.
```

The endpoint has

```
C_1:02->22,
C_2:02->00,
p_1:10->12.
```

### The `a_1=2` route

```
12002 => 02102 => 11012 => 01112 => 10022.
```

Its physical moves are

```
b->v, v->u, b->v, v->u,
```

and its forced rows are

```
11->02, 02->11, 10->01, 01->10.
```

The endpoint has

```
C_1:20->00,
C_2:02->22,
p_1:12->10.
```

### The neutral route

```
12002 => 21011 => 12020.
```

Both physical moves are `w->u`; the forced rows are `12->21` and
`21->12`.  The endpoint has

```
C_1:20->20,
C_2:02->20,
p_1:12->12.
```

At every physical endpoint in all three routes, `p_1` is selected
nonquiet.  Hence no claim about `p_2`, no relay preparation, and no
scan/connector rethreading is used.  Direct substitution verifies every
displayed state and forced row.

Uniformly, the endpoint is

```
C_1=C*(a_1),
C_2=C(a_1),
C_3=H.
```

Thus `C_1` is restored to the exact complemented zipper connector, while
`C_2|C_3=C(a_1)|H` is a connector-aligned return train.  The fixed
`C_3=H` supplies the local phase marker.

The two nonzero routes have disjoint literal interiors.  The neutral and
`a_1=2` routes share only their initial five-coordinate state `12002`;
they therefore still require one exterior bit which distinguishes
`a_1=1` from `a_1=2`.  The signed residual/collar record or the protected
branch register can provide that bit if it is held fixed.

This addendum closes the former hypothesis 1.  The remaining hypotheses are
now exactly:

1. retain the collar-order/branch record while `p_1` changes;
2. supply an all-guardable corridor, or a bounded treatment of its
   midpoint/interface exceptions; and
3. route the compensating block `C(a_1)` from the returned train to the
   globally assigned target occurrence.
