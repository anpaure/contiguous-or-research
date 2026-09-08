# Odd APH: a unique moving pilot removes the commuting-train collision

**Date:** 2026-08-06  
**Method:** occurrence-labelled block positions and a three-block train  
**Status:** **RETRACTED as stated.**  The pilot position separates different
macro crossing counts, but it does not by itself distinguish the second and
third embedded block swaps.  Section 7 records the exact collision found by
the independent audit
`MATH_AUDIT_ODD_APH_UNIQUE_PILOT_POSITION_DECODER_20260806.md`.

## 1. Why the old two-block decoder failed

Let a two-block word `W` move monotonically through a tape factor `V`.  The
macro words before and after the crossing are `WV` and `VW`.  They may be
equal: by the elementary commuting-word theorem, this happens precisely
when `W` and `V` are powers of one primitive word.  The audited collision

```
HA | BHA  =  B | HA | HA  =  BHA | HA
```

is of exactly this form.  Therefore the number of crossed motif blocks is
not recoverable from the unmarked tape.

The following construction adds no growing history.  It carries one
literal pilot block whose *physical position* is the history.

## 2. Pilot hypotheses

Fix two block values `P` and `D`, and optionally a mate `Pbar`, with the
following properties throughout one crossing.

1. `D` occurs at one declared stationary origin address.
2. Exactly one block belongs to the pilot alphabet `{P,Pbar}`.
3. No tape block belongs to `{P,Pbar}`.
4. A protected finite record `Q` determines the source branch and the
   direction of travel.
5. At every macro checkpoint the pilot is `P` and is the trailing block of
   a three-block train

   ```
   X1 | X2 | P.
   ```

The intended odd application uses

```
P = 01,       Pbar = 10,       D = 21.
```

The raw work alphabet `{00,20,22}`, and the origin-code alphabet
`{02,11,20}`, are disjoint from `{01,10,21}` except at the declared
delimiter itself.

## 3. One macro crossing

Move a right-going train through one block `Y` in the order

```
X1 | X2 | P | Y
 -> X1 | X2 | Y | P
 -> X1 | Y  | X2 | P
 -> Y  | X1 | X2 | P.                         (3.1)
```

Each displayed arrow denotes a fixed simple path in the corresponding
four-coordinate mass layer.  During the first arrow the pilot may
temporarily be changed to `Pbar`, provided that:

* every strict state still contains exactly one member of `{P,Pbar}`; and
* the fixed branch record distinguishes any two first-arrow routes whose
  four-coordinate paths meet.

During the second and third arrows the literal pilot is fixed outside the
active pair.  The reflected permutation is used for a left-going train.

## 4. Exact pilot-position decoder

### Failed Theorem 4.1

Suppose the hypotheses of Section 2 hold and every block crossing uses
(3.1).  Suppose also that the first-arrow paths satisfy the two bullet
conditions above.  Then every macro and strict state recovers

1. the source branch;
2. the direction of travel;
3. the number of completed tape blocks;
4. which of the three arrows in (3.1) is active; and
5. the local microstep.

In particular, two paths with different crossing counts cannot meet, even
if the unpiloted train commutes with the intervening tape word.

#### Invalid proof

The unique stationary `D` fixes the origin coordinate, while `Q` fixes the
source branch and direction.  At a macro checkpoint, the physical address
of the unique pilot is an affine function of the completed crossing count,
with slope `+1` in the right-going direction and `-1` in the left-going
direction.  It is therefore injective once the direction and origin are
known.

Inside the first arrow, the unique member of `{P,Pbar}` lies in the active
pair.  Its physical address and the fixed branch record identify the
ordered endpoint type; simplicity of that branch path identifies the
microstep.  Inside the second and third arrows the pilot is fixed immediately
beside the active pair.  The old draft then asserted that its side
distinguishes the two arrows.  That assertion is false: two differently
embedded active-pair paths can produce the same full word with the pilot at
the same address.

The valid conclusion is only that equality forces the same crossing count.
Arrow number and microstep do not follow.  Hence the theorem is unproved.
\(\square\)

### Retracted Corollary 4.2 (out-and-back restoration)

If the outward pass uses increasing pilot positions and the return pass
uses the reflected schedule with the direction bit in `Q` reversed, then
the two passes are mutually disjoint away from their common turn endpoint.
The return restores every crossed block and returns `P` to its origin
address beside `D`.

#### Proof

Endpoint restoration remains algebraically correct, but path simplicity and
bank disjointness depended on Failed Theorem 4.1 and are not proved.

## 5. Setup and retirement interface

The theorem is composable only in copy-before-erase order:

1. while the old origin code is literal, copy the collar/source branch into
   `Q`;
2. route the now-spare mass-four origin pair to `P|D = 01|21`;
3. keep `D` fixed and attach `P` to every cart or return train;
4. after all tasks, return `P` beside `D`;
5. while `Q` is still literal, reverse the route `P|D` back to the old
   origin code; and
6. erase `Q` only after the raw source motif or the permanent collar record
   is literal.

This schedule prevents the pilot from being postulated as a private blank
resource.  It is a reversible reuse of the old origin record after that
record has been copied.

## 6. Exact remaining finite row

The unique pilot removes the fatal `BHAHA` collision **between different
macro counts**, but not every strict-state collision.  To obtain a complete
APH theorem one must still
bind, in the actual fixed-row graph,

* the source and lifetime of `Q`;
* the literal mass-four route from each old origin code to `01|21` and back;
* the finite first-arrow route table, particularly the equal-mass `B/M`
  branches, with `P=01` versus `Pbar=10` visible before any meeting state;
  and
* setup and teardown to the already proved fixed-row directed lift.

These are bounded route checks.  No growing progress tape, completed-prefix
decoder, or anticommutation assumption remains.

## 7. Exact counterexample and corrected sufficient hypothesis

Take

```
X1 = X2 = H = 02,       Y = B = 20,       P = 01.
```

Use for both the second and third arrows the valid simple path

```
0220 -> 0211 -> 0202 -> 0112 -> 1012 -> 1102 -> 2002.
```

In arrow 2, local state `1102` embedded at blocks 2--3 gives

```
02 | 11 | 02 | 01 = H | M | H | P.
```

In arrow 3, local state `0211` embedded at blocks 1--2 gives the identical
full word.  Source, `Q`, direction, crossing count, and pilot address all
agree; only arrow number and microstep differ.

A corrected pilot theorem follows if the full state carries a literal
three-valued phase tag throughout the interiors of arrows 1, 2, and 3 (or
if one supplies one jointly audited route bank whose three embedded interior
state sets are disjoint).  With that extra premise, pilot address gives the
crossing count, the phase tag gives the arrow, and simplicity gives the
microstep.  Constructing that phase tag in the fixed-row odd graph is the
remaining bounded row.
