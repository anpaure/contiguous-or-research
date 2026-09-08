# Exact alternating Hall/SDR audit for the 12,873-entry partial `k=16` word

## Frozen scope and status

The frozen word is
`scratch/k16_12873_repaired_partial.word`, with length `12873` and SHA-256

```text
0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

Its exact missing-mask set is

```text
H = {10365, 52833, 52835}.
```

The results below are exact but scoped.  They prove:

1. arbitrary replacement of cells `6437,6438,6439` cannot repair the word;
2. the natural two-cell portal cannot be completed by one arbitrary additional
   cell substitution anywhere in the word; and
3. `7804` of the `12871` contiguous three-cell blocks fail the ordinary
   window-form Hall condition.

They do **not** yet exclude arbitrary three noncontiguous substitutions, all
three-cell blocks, or arbitrary replacement on the full central 11-cell
support.  The `5067` blocks which pass ordinary Hall still require the shared
literal condition below.

## Exact alternating-rematching theorem

Let `w=(w_0,...,w_{n-1})` be the frozen partial word and let `P` be a proposed
set of edited positions.  A target mask is *safe outside `P`* if it has an old
exact-OR interval disjoint from `P`.  Let

```text
R_P = {all nonzero target masks} - {targets safe outside P}.
```

Thus `R_P` contains the original holes and every old target whose entire old
witness family meets `P`.  This is the exact alternating cascade: installing
an original hole while destroying a private old witness puts that displaced
target back into the same residual family.

For every physical interval `I` meeting `P`, define

```text
S_I = I intersect P,
F_I = OR of the frozen, unedited cells in I.
```

Collapse intervals having the same form `(F_I,S_I)`.  For a target `t`, its
relaxed neighborhood is

```text
N(t) = {(F,S) : F is a submask of t}.
```

The collapse is exact for capacity: under any fixed replacement literals, one
form has one exact OR label and therefore cannot represent two different
targets.  Consequently every repair satisfies the Hall inequalities

```text
|union of N(t), t in X| >= |X|        for every X subset of R_P.       (H)
```

Hall alone is not sufficient because forms share edited cell literals.  The
exact strengthening is as follows.  Choose an injective representative
`phi(t)=(F_t,S_t)` for every `t in R_P`.  For each edited position `p`, put

```text
J_p = intersection of all t for which p is in S_t,
```

with `J_p=65535` when no selected form uses `p`.  The selected SDR is realizable
if and only if

```text
J_p != 0                                                   for every p in P,
F_t OR (OR of J_p over p in S_t) = t                       for every t in R_P. (J)
```

Necessity follows because a replacement literal at `p` must be a submask of
every selected target whose interval uses `p`.  For sufficiency assign the
literal `x_p=J_p`; condition `(J)` then makes every selected interval exact.
Targets outside `R_P` retain their frozen avoiding witnesses.  Therefore
existence of an SDR satisfying `(J)` is an exact repair criterion, while `(H)`
is its solver-free relaxation.

For a contiguous block of width `m`, forms have the concrete representation
`(F,a,b)`, where `[a,b]` is the nonempty local subinterval of edited cells and
`F` is the OR of the optional frozen left suffix and right prefix.  This is the
form representation used by the audit.

## Central three-cell Hall obstruction

Take

```text
P = {6437,6438,6439},
old values = [32768, 18553, 10361].
```

The exact residual family has 14 targets:

```text
R_P = {10361,10365,18553,26745,32768,43129,43133,
       50801,51321,52833,52835,52849,52983,59513}.
```

The alternating maximum matching has size `12`.  An explicit Hall-deficient
set is

```text
X = {10361,10365,18553,26745,32768,51321,52833,52835},  |X|=8.
```

Its entire collapsed neighborhood is

```text
N(X) = {(0,0,0),(0,0,1),(0,0,2),
        (0,1,1),(0,1,2),(0,2,2)},                         |N(X)|=6.
```

These are precisely the six internal subinterval geometries of a three-cell
block, all with zero exterior mask.  Hence `|N(X)|=6<8`; arbitrary nonzero
values in these three cells are impossible even before shared-bit conflicts
are imposed.

## Natural portal and its exact one-cell no-go

The exact two-cell portal is

```text
position 6436: 18033 (0x4671) -> 18017 (0x4661)
position 6439: 10361 (0x2879) -> 10365 (0x287d).
```

It installs all of `H`, with witnesses

```text
10365 : [6439,6439]
52833 : [6433,6437], [6434,6437]
52835 : [6432,6437].
```

It simultaneously displaces exactly

```text
G = {10361,18033,20081,20215,26745,
     43129,50801,52849,52983,59513}.
```

Now allow one further substitution at any position `p`, to any nonzero value
`x`.  Since every `g in G` is absent after the portal edits, every new witness
for every `g` must contain `p`.  Therefore

```text
x is a submask of intersection(G) = 0x71,
```

leaving exactly 15 possible nonzero values.  If `L_p` is the exact set of ORs
of frozen intervals ending at `p-1`, together with zero, and `R_p` is the
analogous set beginning at `p+1`, then the exact labels installable through
the new literal are

```text
C_p(x) = {l OR x OR r : l in L_p, r in R_p}.
```

The necessary and sufficient condition for recovering all of the already
missing family `G` by that one substitution is simply `G subset of C_p(x)`.
The audit enumerates all

```text
12873 positions * 15 values = 193095 exact contexts.
```

The histogram of `|G intersect C_p(x)|` is

```text
0:190982, 1:1897, 2:156, 3:20, 4:24, 6:16.
```

Thus the maximum is `6/10` and there are zero full candidates.  All 16 maxima
use position `6434` or `6435` and a value in

```text
{16,17,48,49,80,81,112,113},
```

recovering only

```text
{18033,20081,20215,50801,52849,52983}.
```

This closes the natural portal plus one arbitrary additional substitution,
including a third substitution placed outside the seam neighborhood.  It is
not a no-go for a different jointly chosen three-edit portal.

## Reproducible artifacts

The solver-free driver is
`scratch/audit_k16_12873_partial_threewindow_hall_20260730.py`:

```text
SHA-256 ff97a39a3835035597e8d09e677d86738aef0b0bd4a03a80d92f34cbbacd3d28
```

The frozen report is
`scratch/k16_12873_partial_threewindow_hall_20260730.audit.json`:

```text
file SHA-256    db8bc3a160698808fd90d44a7c3c71f4a8a7c47d3b3ec435dafd701b606c548c
payload SHA-256 712cb3c6eb3a165c98716997f70ab1903a6b80d4c413a23e0c59ea4e0cc22ebb
```

Fresh replay reports `PASS_SCOPED_HALL_OBSTRUCTION`, central Hall deficiency
`2`, portal-plus-one maximum recovery `6`, zero portal-plus-one full repair
candidates, `7804` width-three Hall failures, and `5067` Hall-relaxation
passes.
