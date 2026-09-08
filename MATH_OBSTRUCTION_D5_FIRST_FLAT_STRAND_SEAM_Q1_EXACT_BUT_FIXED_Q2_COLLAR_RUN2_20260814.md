# The first flat D5 strand seams are q1-exact but force a fixed q2 collar defect

**Date:** 2026-08-14
**Status:** exact typed `(1,1,2)` first-factor obstruction with standalone
H100 replay.  All owner/q1-simple embeddings in the declared canonical
seam/common-router-role search are enumerated.  Every one fails at the same
phase-independent three-support window before the auxiliary component is
entered.

## 0. Outcome

The first flat atlas factor has token exposures `(1,1,2)`.  Coupling q1
refill by logical strand succeeds: there are exactly 21 owner-simple
embeddings in which

* each of the three context cuts belongs to a three-versus-three canonical
  C6 seam;
* one companion cut from each seam is a canonical cut of one common
  18-owner router;
* the remaining companions are two dummy sockets and the next-router socket
  of the exposure-two strand; and
* the complete local owner/lower-q1/upper-q1 bank is simple and the removed
  and added q1 occurrence Counters agree exactly.

Nevertheless, no one of the 21 embeddings is q2-resident.  On the same
exposure-one token, a three-edge window wholly on the already fixed
seam/router side has exchange supports

```text
{0,2}, {3,5}, {1,2}.
```

Coordinate `2` occurs in the first and third supports.  It therefore toggles
twice with only two owner occurrences between toggles, creating an exact
owner run of length two.  The lower-q2 values of the two adjacent triple
windows are also equal.  The defect is identical in the old and new router
phases and does not touch the unbuilt dummy side.  No dummy completion,
dummy cut phase, dummy clocks or longer component beyond that cut can repair
it.

Thus the canonical strand-seam compiler solves q1 but fails the required q2
simplicity/residence collar on the first actual typed factor.

## 1. The exact strand seam

Let `C` have rank `r-2`, and choose distinct labels

```text
x0,x1,x2,y not in C.
```

With indices modulo three put

```text
A_i = C + x_i + x_(i-1),
B_i = C + x_i + y.
```

The removed and added matchings are

```text
E_i = A_i--B_i,
F_i = A_i--B_(i-1).
```

All six owners are distinct and all six pairs are Johnson edges.  Their q1
resources are

```text
lower(E_i) = C+x_i,
upper(E_i) = C+x_i+x_(i-1)+y,

lower(F_i) = C+x_(i-1),
upper(F_i) = C+x_i+x_(i-1)+y.
```

Hence the upper resources agree pointwise and the lower resources agree by
cyclic reindexing.  This is precisely the marked-C6 seam family, now used as
a fixed strand collar rather than as the router's phase switch.

Every prescribed Johnson context edge extends to 220 such oriented seam
collars at rank 11 on ground 23: choose `x0` in its rank-10 lower resource,
orient its two exchanged labels as `x2,y`, and choose `x1` from the remaining
coordinates.

## 2. The first literal q1 compiler

For the first frozen factor the three context edges are

```text
00100100110110111110000 -- 10000100110110111110000
00100100110111101110000 -- 00100100110111011110000
00100110110110101110000 -- 00100110110101101110000.
```

The exhaustive search finds

```text
220 seam collars per token,
8800 oriented router roles per token,
22416 triples sharing a candidate (H,z),
69 canonical router-cut triples,
21 owner-simple and q1-simple complete embeddings.
```

One representative has

```text
token permutation (0,2,1)
H = 00100100110110100110000
z = 0
active labels = (15,6,13)
router clocks = (x1,x2,y1,y2) = (1,3,2,5).
```

Its three removed-versus-added seam tables are:

```text
strand 0 removed
00100100110110111110000 -- 10000100110110111110000
00000110110110111110000 -- 10000110110110110110000
00100110110110110110000 -- 10100100110110110110000
strand 0 added
00100100110110111110000 -- 10100100110110110110000
00000110110110111110000 -- 10000100110110111110000
00100110110110110110000 -- 10000110110110110110000

strand 1 removed
00100110110101101110000 -- 00100110110110101110000
10100110110100101110000 -- 10100110110101100110000
00100110110111100110000 -- 10100110110110100110000
strand 1 added
00100110110110101110000 -- 00100110110111100110000
00100110110101101110000 -- 10100110110100101110000
10100110110101100110000 -- 10100110110110100110000

strand 2 removed
00100100110111011110000 -- 00100100110111101110000
10100100110111001110000 -- 10100100110111010110000
00100100110111110110000 -- 10100100110111100110000
strand 2 added
00100100110111101110000 -- 00100100110111110110000
00100100110111011110000 -- 10100100110111001110000
10100100110111010110000 -- 10100100110111100110000.
```

The frozen certificate lists the complete router owners and all 21
embeddings.  Direct recomputation verifies 24 before and 24 after q1 edges,
distinct lower and upper values, and exact occurrence-Counter equality.

## 3. Crossing q2 ledger and exact collar failure

For the representative, the obstructed fixed path is

```text
u = 10000110110110110110000
v = 00100110110110110110000
w = 00110010110110110110000
t = 01010010110110110110000.
```

Here `u--v` is the added seam join; `v--w--t` is already inside the current
router.  The exchange supports are

```text
supp(u,v) = {0,2},
supp(v,w) = {3,5},
supp(w,t) = {1,2}.
```

The two consecutive q2 windows have decks

```text
window (u,v,w):
  lower = 00000010110110110110000
  upper = 10110110110110110110000

window (v,w,t):
  lower = 00000010110110110110000
  upper = 01110110110110110110000.
```

Thus the lower-q2 resource is repeated and coordinate `2` has a length-two
owner run.  These owners and edges are identical in the old and new router
phases, so this piece has zero signed old/new current but fails q2 simplicity
and residence in both states.

The standalone replay reconstructs the actual two-deep frozen D5 context
and all 21 q1 embeddings.  In every embedding the same logical token `0`
has one fixed-side endpoint with support-union size five and the other with
size six.  Coordinate `2` is the repeated label in all 21, in both phases.
Since the bad window ends before the auxiliary component begins, changing or
lengthening that component cannot affect the defect.

## 4. Scope and next architecture

The result rules out the following local architecture for the first typed
factor:

```text
one canonical 18-owner router
+ one canonical strand C6 seam per token
+ arbitrary components attached beyond the three remaining seam cuts.
```

It does not rule out:

* changing the seam matching rather than using the canonical cyclic one;
* inserting a transition cable between the seam and current router;
* jointly recutting two adjacent routers so that the bad fixed-side window
  itself changes;
* using a longer q1-zero collar whose first join is not `u--v`; or
* abandoning factor `0` in favor of a conjugate flat factorization.

The obstruction identifies the exact item the next compiler must move: the
first seam-to-router join on logical token `0`, not the dummy rail.

## 5. H100 provenance

```text
q1 seam search
6160d338d9bb4b4b3d3a6578137b6d362bb36db25efa320d7ca8ae68609131c8
  scratch/search_d5_first_flat_strand_seam_router_q1_compiler_20260814.py

21-witness q1 certificate
18f59d809934a4283b6a71a6ee1311586c42f54955d09820332959b6e9f17b35
  scratch/search_d5_first_flat_strand_seam_router_q1_compiler_all_20260814.h100.out

standalone fixed-side hostile replay
5d9b6bd7a596bf6d8f4427674ecd6de3a3f8aa78e3f87e98f246d8aa5a4743d7
  scratch/audit_d5_first_flat_strand_seam_forced_collar_obstruction_20260814.py

hostile output
07b5a06f1254f33d3167715ab20b7d8ca7c6486d278fd095021aed39ef13b1c8
  scratch/audit_d5_first_flat_strand_seam_forced_collar_obstruction_20260814.h100.out
```

All enumeration, context reconstruction, replay and hashing ran on H100.
