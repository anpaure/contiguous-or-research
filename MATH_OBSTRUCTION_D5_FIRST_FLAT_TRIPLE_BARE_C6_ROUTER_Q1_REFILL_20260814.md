# The first flat D5 triple has no bare three-splice C6-router q1 refill

**Date:** 2026-08-14  
**Status:** exact context-specific obstruction with standalone H100 replay.
It rules out one bare 18-owner router attached by three independent ordinary
splices at its canonical `P2--Q0` cuts.  It does not rule out strandwise C6/C8
refill collars, serial telescoping between routers, cables, other router cuts,
or the full 226-router atlas.

## 0. Result

The first factor in the flat minimum atlas is

```text
(1010010011011011111000,
 0010010011011111111000,
 0010011011011110111000).
```

Its three literal old-factor owner edges at rank 11 on ground 23 are

```text
00100100110110111110000 -- 10000100110110111110000
00100100110111101110000 -- 00100100110111011110000
00100110110110101110000 -- 00100110110101101110000.
```

Cut these three edges and the three canonical `P_(i,2)--Q_(i,0)` edges of
one 18-owner C6 router.  At each port choose either cross orientation and
require all four endpoints to be distinct.  There is no choice for which
the six added cross edges have, in aggregate, the same lower-q1 and upper-q1
occurrence multisets as the six removed edges.

Therefore this prescribed first factor cannot be compiled by a bare router
with three independent ordinary splices.  The obstruction occurs before
clock selection, q2 crossing windows or residence collars.

## 1. Exhaustive finite census

For each prescribed context edge the search enumerates every pair `(P,Q)`
such that

```text
P--Q is a Johnson edge,
X--P and Y--Q are Johnson edges,
```

including both cross orientations.  The exact counts per edge are

```text
2026 raw oriented pairs,
1500 oriented pairs with X,Y,P,Q all distinct,
 750 unoriented physical four-owner collars.
```

Joining the three port menus by the central-router signature

```text
P_i = H + a_i + a_(i+1),
Q_i = H + a_i + z
```

leaves exactly 255 canonical three-port patterns.  For each pattern the
search compares the occurrence Counters

```text
removed lower: {X_i intersection Y_i, P_i intersection Q_i}_i
added lower:   {X_i intersection P_i, Y_i intersection Q_i}_i

removed upper: {X_i union Y_i, P_i union Q_i}_i
added upper:   {X_i union P_i, Y_i union Q_i}_i.
```

Exactly zero of the 255 patterns has both Counter equalities.  Hence the
result is an exhaustive finite UNSAT in the stated architecture, not a
random-menu failure.

## 2. Why refill cannot be imposed port by port

There is also a general four-owner warning.  Suppose two removed Johnson
edges on four distinct owners are replaced by their cross matching and the
lower and upper q1 resource pairs agree separately.  If either two lower or
two upper resources coincide, q1 simplicity already fails.  Otherwise rank
forces

```text
L1 union L2 = U1 intersection U2 = M
```

with `M` a rank-r owner common to both old intervals.  Thus one owner is
reused.  An owner-simple q1-exact C4 splice is impossible.

The search therefore imposes refill only after summing all three splice
currents.  Even that aggregate relaxation has no solution for the first
literal flat triple.

## 3. Scope and surviving compiler route

This theorem does not localize q1 conservation to individual routers in a
global atlas.  Along a logical strand, currents from consecutive router
ports may telescope.  The natural exact unit is instead a strand collar:

* exposure one: the original context cut, one router cut and one dummy
  identity cut form a three-versus-three C6 seam;
* exposure two: the original cut and two router cuts form the C6 seam;
* exposure three: the original cut and three router cuts form a four-edge
  C8 collar.

The flat histogram consequently asks for 461 C6 collars and 16 C8 collars,
not 226 independently q1-closed routers.  This obstruction is the reason
that coupling is necessary; it is not an obstruction to the coupled design.

## 4. H100 provenance

```text
subject search
d940e9f7e01c547693c8c2df6b68d7fd3a4de1a1af56654bb4de5636e85983e0
  scratch/search_d5_first_flat_router_cut_open_compiler_20260814.py

subject output
07928a004fbf5024ddad85131159e2571734c057f6003ea68bac3a21b1eb825d
  scratch/search_d5_first_flat_router_cut_open_compiler_20260814.h100.out

standalone hostile replay
aeb70fda7172de1ec077345dca530da29b59094ea0d4235a9dafaca48ba110fe
  scratch/audit_d5_first_flat_router_cut_open_q1_nogo_independent_20260814.py

hostile output
d0af0e8152e4273eed55a117cfbad32e2681c4438cb404836614f8e0faf8b8b5
  scratch/audit_d5_first_flat_router_cut_open_q1_nogo_independent_20260814.h100.out
```

Both programs independently reconstruct the context edges from the frozen
selection and flat-atlas certificate.  All enumeration and replay ran on
H100.
