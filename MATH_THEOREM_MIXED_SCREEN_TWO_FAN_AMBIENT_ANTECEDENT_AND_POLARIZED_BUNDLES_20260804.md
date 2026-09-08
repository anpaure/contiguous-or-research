# Two mixed-screen coatom fans admit one ambient antecedent with polarized bundles

> **SUPERSEDED -- DO NOT CITE.**  The `Cd/Ic` calculation below is only an
> auxiliary generic split-core construction and does not instantiate the
> actual aligned birail action.  Its original port proof also required an
> extra stable-core pin in the `d=2` middle case.  The corrected, authoritative
> theorem is
> `MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`,
> using the phase-swapped `Ibc/Ica` blocks and the exact
> `(J+b+P,J+a+S) <-> (J+a+P,J+b+S)` mapping.

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** `DO NOT CITE` exploratory lineage.  The split-core pinning algebra
is useful, but `Cd,Ic` do not carry the packet's actual `a/b` birail targets,
and the first draft also omitted a native-overlap core pin at `d=2`.  The
authoritative construction must use the phase-dependent adjacent blocks
`Ibc/Ica`, prove a nonempty ambient baseline, and is being frozen separately.

## 0. Setting

Put `n=d+2`, where `d>=2`, and take the fixed packet core `K` to be
nonempty.  (In the intended central-layer application
`|K|=r-d-4` tends to infinity.)  Let

\[
 F=\{f_0,f_1,\ldots,f_{d+1}\}.
\]

Use the two active words

```text
P = Iab Ib bc Cd Ic Ibc Ica Ia ca Ad Bd ab,
Q = Iab Ia ca Cd Ic Ica Ibc Ib bc Bd Ad ab,
```

with upper screens at transitions `1,3,5,7` and lower screens at all
other transitions.  Expand every active triple `V` into the coatom block

\[
 O_i(V)=K\cup V\cup(F\setminus\{f_i\}),
 \qquad 0\le i\le d+1.
\tag{0.1}
\]

The blocks `Cd` and `Ic` occur consecutively and pointwise identically in
both phases.  Their three active coordinates are

\[
 Cd=\{e,c,d\},\qquad Ic=\{\infty,e,c\}.
\tag{0.2}
\]

The screen immediately left of `Cd` is lower and has active part
`{e,c}` in both phases.  The common screen between `Cd` and `Ic` is upper
and has active part `{e,c,d,infinity}`.  The screen immediately right of
`Ic` is lower and has active part `{infinity,c}` in both phases.

Let `T` denote either complete expanded owner chronology.  The mixed-screen
theorem says that every internal positive coordinate run of `T` has length
at least `d+1`; the displayed three-screen neighbourhood is the same in
both phases.

## 1. Pinned binary dilation

For a binary source trace `a`, write

\[
 (D^d a)_t=\bigvee_{p=t}^{t+d}a_p.
\]

### Lemma 1.1 (arbitrary coordinate pins in an eroded positive run)

Let `[alpha,beta]` be a finite positive run of a binary owner trace, with
`beta-alpha+1>=d+1`, and zeros immediately outside it.  The permissible
source positions for that run are exactly

\[
 [\alpha+d,\beta].
\tag{1.1}
\]

Any prescribed finite set of pins in this interval extends to an exact
binary source trace for the run: add the two endpoint positions `alpha+d,beta`
and then add positions until every consecutive gap is at most `d+1`.

#### Proof

A source occurrence at `p` affects precisely the owner positions
`[p-d,p]`.  It lies wholly in the positive run exactly when (1.1) holds.
The first owner `alpha` can only be covered by `alpha+d`, and the last
owner `beta` can only be covered by `beta`.  Once those positions are
present, the whole run is covered exactly when consecutive selected source
positions have gap at most `d+1`.  Inserting additional permissible
positions achieves this without entering either neighbouring zero window.
\(\square\)

Coordinate traces are independent, so compatible pin sets for different
coordinates may be imposed simultaneously; a source letter is simply the
set of coordinates pinned at its position.  This coordinate statement does
not by itself guarantee that every source letter is nonempty.  In the
present packet, however, every owner and screen contains the fixed nonempty
core `K`.  Its maximal erosion therefore lies in every internal source
letter of the packet.  The displayed blocks are more than `d` owner
positions from the packet endpoints, so all source addresses used below
are internal and nonempty.  Endpoint source letters remain part of the
already exported clipped boundary state.

## 2. Forced filler rotor inside any ambient antecedent

Fix one coatom block beginning at owner position `s`.  For every internal
filler `f_i`, `1<=i<=d`, the immediate owner trace around the block is

\[
 1,\quad O_0,\ldots,O_{i-1},\underbrace{O_i}_{0},
 O_{i+1},\ldots,O_{d+1},\quad1,
\]

because both lower and upper mixed screens contain every internal filler.

### Lemma 2.1 (forced two-sided occurrences)

Every exact depth-`d` antecedent of this trace contains `f_i` at the two
source positions

\[
 s+i-1,\qquad s+i+d+1,
\tag{2.1}
\]

and contains no `f_i` at any source position in

\[
 [s+i,s+i+d].
\tag{2.2}
\]

#### Proof

The zero owner `O_i` forbids (2.2).  The preceding owner window ends at
`s+i+d-1`, so its only position outside (2.2) is `s+i-1`; this position is
forced.  The following owner window begins at `s+i+1`, so its only position
outside (2.2) is `s+i+d+1`; that position is also forced. \(\square\)

The two guard fillers are automatically excluded from the ray intervals
below.  At `Cd`, the local trace of `f_0` is `1,0,1^(d+1),0`, so its
bounded positive run has the unique source occurrence `s+d+1`.  The trace
of `f_(d+1)` ends its left positive run at owner `s+d`, forcing the
block-side occurrence `s+d`; its next run starts after the upper-screen
zero.  At `Ic`, `f_0` again has its first block-side occurrence at relative
position `d+1`, while `f_(d+1)` has its last one at relative position `d`;
the next possible occurrence is at relative position `2d+2`.  We choose
the sparse endpoint completion from Lemma 1.1, so neither guard occurs in
`[j,d-1]` or `[d+2,d+j+1]` for `1<=j<d`.

## 3. Split-core pinning at `Cd`

Put

\[
 C_d=K\cup\{e,c\}.
\tag{3.1}
\]

Every coordinate of `C_d` is positive on the left lower screen, throughout
the `Cd` block, and on the right upper screen.  By Lemma 1.1 we may pin it
at the three relative source positions

\[
 d-1,\qquad d+1,\qquad d+2.
\tag{3.2}
\]

The pivot `d` is absent on the left lower screen and positive throughout
the block and on the right upper screen.  Its positive run starts at the
first block owner.  Pin it at

\[
 d,\qquad d+2.
\tag{3.3}

The first position in (3.3) is the forced left endpoint of this positive
run, and the second is permissible; the gap is two.

For `1<=j<d`, define the literal source intervals

\[
 y_j^d=[s+j,s+d-1],\qquad
 x_j^d=[s+d+2,s+d+j+1].
\tag{3.4}

### Theorem 3.1 (right-polarized `Cd` rays)

There is an exact ambient antecedent for which

\[
 \operatorname{OR}(y_j^d)
 =C_d\cup\{f_{j+1},\ldots,f_d\},
\tag{3.5}
\]

and

\[
 \operatorname{OR}(x_j^d)
 =C_d\cup\{d\}\cup\{f_1,\ldots,f_j\}.
\tag{3.6}

No other active or guard filler coordinate occurs in these intervals.

#### Proof

The pin `s+d-1` lies in every `y_j^d`, while `s+d+2` lies in every
`x_j^d`, so both contain `C_d`.  The pivot pins (3.3) avoid every left
interval and put `d` in every right interval.

By Lemma 2.1, the left forced occurrence `s+i-1` belongs to `y_j^d`
exactly when `i>j`; the right forced occurrence `s+i+d+1` belongs to
`x_j^d` exactly when `i<=j`.  The forbidden window (2.2) rules out every
other internal-filler contribution.  The two guard occurrences sit in the
two omitted central positions.  Any active coordinate outside `Cd` is zero
on every block owner, so its source trace is zero throughout the union of
the block owner windows, which contains (3.4).  This proves (3.5)--(3.6).
\(\square\)

## 4. Split-core pinning at `Ic`

Let `s'` be the start of the next block; thus `s'=s+d+3`.  Put

\[
 C_c=K\cup\{\infty,c\}.
\tag{4.1}

Every coordinate of `C_c` is positive on both adjacent screens and the
whole `Ic` block.  Pin it at relative positions

\[
 d-1,\qquad d+1,\qquad d+2.
\tag{4.2}

The pivot `e` is positive on the left upper screen and throughout `Ic`,
but absent on the right lower screen.  Its positive run ends at the last
block owner.  Pin it at

\[
 d-1,\qquad d+1.
\tag{4.3}

For `1<=j<d`, put

\[
 y_j^c=[s'+j,s'+d-1],\qquad
 x_j^c=[s'+d+2,s'+d+j+1].
\tag{4.4}

### Theorem 4.1 (left-polarized `Ic` rays)

There is a simultaneous exact ambient antecedent for which

\[
 \operatorname{OR}(y_j^c)
 =C_c\cup\{e\}\cup\{f_{j+1},\ldots,f_d\},
\tag{4.5}
\]

and

\[
 \operatorname{OR}(x_j^c)
 =C_c\cup\{f_1,\ldots,f_j\}.
\tag{4.6}

#### Proof

The proof is the mirror of Theorem 3.1.  The common-core pins put `C_c` on
both rays; the pivot pins put `e` on every left ray and no right ray; and
Lemma 2.1 gives exactly the displayed filler prefix and suffix.

There is no conflict with the `Cd` pins.  On their shared coordinates
`K union {e,c}`, the consecutive prescribed positions are separated by at
most `d`, so Lemma 1.1 completes the common positive run.  For each internal
filler, the right forced occurrence after its `Cd` zero and the left forced
occurrence before its `Ic` zero are consecutive source positions.  The
coordinates `d` and `infinity` are absent on the opposite block, so their
pin sets lie just outside that block's forbidden source interval. \(\square\)

## 5. Native diamonds survive the split core

For either block start `t in {s,s'}` and `0<=i<=d`, define

\[
 p_i=[t+i+1,t+i+d],\quad
 o_i=[t+i,t+i+d],\quad
 o_{i+1}=[t+i+1,t+i+d+1],\quad
 q_i=[t+i,t+i+d+1].
\tag{5.1}

### Theorem 5.1 (exact native occurrence bank)

For the pinned antecedent above,

\[
 \operatorname{OR}(o_i)=O_i(V),\qquad
 \operatorname{OR}(o_{i+1})=O_{i+1}(V),
\tag{5.2}

\[
 \operatorname{OR}(p_i)=O_i(V)\cap O_{i+1}(V),
 \qquad
 \operatorname{OR}(q_i)=O_i(V)\cup O_{i+1}(V).
\tag{5.3}

#### Proof

Equation (5.2) is the defining depth-`d` reconstruction.  The interval
`q_i` is the union of the two owner intervals, proving the union identity.

For the intersection identity, Lemma 2.1 puts every internal filler other
than `f_i,f_(i+1)` in the overlap interval `p_i` and excludes precisely
those two.  The guard endpoint cases follow from their forced central
positions.  The three stable-core pins meet every `p_i`; the central
`d+1` pin also covers the unique short middle case when `d=2`.  For `Cd`, the pivot
pins `d,d+2` meet every `p_i`; for `Ic`, the pivot pins `d-1,d+1` do so.
Every coordinate outside the block is forbidden there.  Hence the overlap
union is exactly the adjacent-owner intersection. \(\square\)

For each ticket `j`, pair the two exact ray occurrences with the all-left
native route at `i=j-1`.  Within one block the `d-1` complete records are
pairwise distinct in ray, port, owner, and q1 occurrence addresses.  The
two blocks occupy different owner addresses, so their union gives

\[
 \boxed{2(d-1)}
\tag{5.4}

pairwise capacity-disjoint complete polarized socket records.  All their
local values and addresses are common to the two tensor phases.

## 6. Exact consequence and remaining rows

The isolated-rotor halo premise is no longer needed for the two useful
interior fans: their required source occurrences extend inside the actual
mixed-screen owner chronology, and the opposite lower/upper screen
orientations create the two required ray polarities.

What is **not** proved here is:

1. that the terminal cap accepts the two displayed polarized product types;
2. that the `2(d-1)` complete records coexist with one transported
   background compiler matching;
3. that the protected packet support embeds in the selected global
   Hamilton carrier; or
4. that the same prepared whole-packet state regenerates after the
   same-parity lift.

Those are state/product/topology assertions.  No local source, halo,
ray-occurrence, owner-occurrence, q1-occurrence, or multiplicity premise
remains for the displayed two-fan bank.

## 7. Dependencies

- `MATH_THEOREM_COATOM_SCREEN_TENSOR_RESIDENT_ECO_PACKET_20260801.md`
- `MATH_THEOREM_COATOM_FAN_CANONICAL_DIAMOND_BUNDLE_AND_HALO_GATE_20260804.md`
- `MATH_THEOREM_COATOM_FOUR_FAN_OCCURRENCE_SOCKET_REPLICATION_20260804.md`
- `MATH_THEOREM_FOLDED_C8_NESTED_TERMINAL_INVARIANT_AND_POLARIZED_SOCKET_20260804.md`
