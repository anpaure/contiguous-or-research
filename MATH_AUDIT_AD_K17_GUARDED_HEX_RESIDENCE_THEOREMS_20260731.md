# Adversarial audit of the guarded `K17` q2 hex and residence-transfer theorems

Date: 2026-07-31  
Lane: AD independent audit  
Verdict: **PASS; two decisive scope corrections were identified and their
post-audit application was verified**

## 1. Audited snapshots

This audit applies to the following byte snapshots:

```text
e5e7c4ca0fc83c815214ebcb22615f4d4bb3aecd92f8544bf0164ba4b0e41cfd
  MATH_THEOREM_AD_K17_GUARDED_Q2_FLAG_PACKET_AND_RESIDENCE_HITTING_20260731.md
e0055b600538a37d3855909b7963504d3cde820317d2df2fabd64e8f96c15ae1
  MATH_THEOREM_K17_CATALAN_RESIDENCE_TRANSFER_AND_PHASE_PORT_COMPOSITION_20260731.md
```

The common frozen carrier has SHA-256

```text
39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

and contains every rank-nine owner and rank-eight intersection colour once.

I independently executed both new audit scripts.  They completed locally in
less than one second each and reproduced their frozen outputs byte for byte:

```text
52e1346fa4ed1d2ccbac1afcae28f8e1bfafd6797064049ab08c6cf8acb6f2a5
  scratch/audit_ad_k17_q2_flag_packet_geometry_20260731.py
ba6d9f9e818124c3156827ad28f59311d7dfdcffbb5cdbe68378e582469e7217
  scratch/ad_k17_q2_flag_packet_geometry_20260731.audit.json

ca8b113c0270ac4ff1489ecbb41ec3781a3efab4427e3abddd0f8fa6bef98504
  scratch/audit_ad_k17_hex_q2_residence_packet_independent_20260731.py
30fc6d7c9bdd38c443f63996b298d963fd6851aa111f4182b9018de0a8872acb
  scratch/ad_k17_hex_q2_residence_packet_independent_20260731.audit.json
```

Their internal canonical payload hashes are respectively
`47342a958b625ab32c66fff88d94f1f0387c782342e431fd9297bceefe9c7cb4`
and
`5c571155594a2113177ad1791934bc7bd0d7babfc005df4c2a113a12ea42db67`.

## 2. The local q2 theorems are sound

### 2.1 Three-owner shortening

Let a shortest consecutive interval of rank-`r` Johnson owners have union
`H` of rank `r+2`.  Deleting its left endpoint removes some element `a`, so
`a` occurs only at the left endpoint.  Deleting its right endpoint removes
some distinct element `b`, so `b` occurs only at the right endpoint.  Every
interior owner is therefore the rank-`r` set `H-{a,b}`.  Two interior owners
would be consecutive equal vertices and hence cannot form a Johnson edge.
An interval of two owners has union rank `r+1`, so there is exactly one
interior owner.  This proves the width-three shortening theorem.

The same argument validates the arbitrary-interval upper-q2 ledger on every
simple Johnson cycle.  The finite replay independently checked that the
frozen carrier's arbitrary rank-eleven interval deck equals its centered
triple deck: `22695` rank-eleven occurrences, `11466` distinct targets, and
`910` missing targets.

The upper-q1 analogue used in the hex-only floor is also valid for a simple
Hamilton owner order: if an interval has rank-`r+1` union `H`, its first two
distinct adjacent owners already have rank-`r+1` union contained in `H`, and
therefore have union exactly `H`.

### 2.2 Four-coordinate packet

For `L subset H`, with ranks `r-2,r+2`, an ordering `(a,b,c,d)` of `H-L`
gives

```text
A=L+ab, V=L+bc, B=L+cd,
C=L+b,  D=L+c.
```

The identities in both notes follow literally.  Conversely, the directed
path determines

```text
a=A-V, c=V-A, b=V-B, d=B-V,
```

so the `24` directed phases are genuinely distinct; reversal pairs them into
`12` unoriented phases.  The residence words `100,110,011,001`, together
with `111` on `L` and `000` outside `H`, give exactly the displayed guard.
The additional separated-boundary hypothesis is necessary and is stated.

### 2.3 Hex delta indexing

Under the convention

```text
C_j S_j selected, C_j S_(j+1) unselected,
```

the toggle changes the selected colour pair at `S_j` from
`(F_j,C_j)` to `(F_j,C_(j-1))`.  Hence the lower delta is exactly

```text
sum_j e_(F_j intersect C_(j-1)) - sum_j e_(F_j intersect C_j).
```

At `P_j`, the owner neighbour through `C_j` changes from `S_j` to
`S_(j+1)`; at `S_j`, it changes from `P_j` to `P_(j-1)`.  These are exactly
the two signed lines in the upper-q2 formula.  Thus a hex changes three
lower-q2 centers and at most six upper-q2 centers.  The inclusion graph has
no four-cycle, so a six-cycle is indeed the smallest simple closed actuator.

## 3. The literal positive packet replays exactly

For the displayed cuts `5607,8324,11990`, the three retained fragments have
lengths `2717,3666,17927`, and the order `C || B || A` has canonical decimal
SHA-256

```text
ee236c63fcb3b2e391918eae926c47ac0ee8360ec2fa35da7fff367bd3173f94
```

The independent replay verifies all `24310` owners and all `24310` lower-q1
colours exactly once.  It also verifies, with complete multiplicity ledgers,

```text
lower q2: 17825 -> 17827, gains 0x70a3,0x782a, no loss;
upper q1: 17557 -> 17559, gains 0x7cab,0x79ba, no loss;
upper q2: 11466 -> 11468, gains 0x7bb3,0x7eab, no loss.
```

The full cyclic run replay gives `(h_2,h_3)=(1063,1829)` before and
`(1061,1828)` after.  It confirms the ten displayed coordinatewise multiset
changes, `1430` runs and positive mass `12870` for every coordinate, and no
new short run.  This is a valid local integral theorem, not a packing or
compiler theorem.

## 4. Run rigidity, donor bound, and packet floors

For a coordinate `x`, the selected incidence degree on positive owners is
`2 binom(2r-2,r-1)`.  Colours containing `x` account for
`2 binom(2r-2,r-2)` of these incidences.  Every remaining incidence is one
mixed owner adjacency.  In a connected Hamilton cycle, two mixed boundaries
bound each positive run.  This proves exactly `Cat_(r-1)` runs, hence `1430`
runs and mass `12870` in `K17`.  Both histogram moment identities and
`G_x-D_x=7150` follow.

The two-run donor inequality is sound under its intended precise hypothesis:
all unaffected run lengths are fixed and the affected multiset is
`{t,L}->{u,v}` with `u,v>=4`.  Then mass conservation gives
`t+L=u+v>=8`, or `L>=8-t`.  Without the two-input/two-output hypothesis this
is not a general packet lower bound, as the companion note correctly warns.

The old-run support floor is also sound.  Every one of the `2892` old short
runs must lose at least one of its entering, internal, or leaving seams.
The independent census gives maximum support load three, hence at least
`ceil(2892/3)=964` original seams are absent in any final intact-fragment
repair.  A sequence of `h` three-cut hexes can make at most `3h` original
seams absent, so `h>=ceil(964/3)=322`.

The new adaptive service floors are valid.  Assign each originally missing
target to the first hex which creates an occurrence.  One hex creates at
most three new upper-q1 occurrences, three lower-q2 occurrences, and six
upper-q2 occurrences.  Therefore the respective floors are

```text
ceil(1891/3)=631, ceil(1623/3)=541, ceil(910/6)=152.
```

The argument survives adaptive packet choice and temporary later loss.  The
largest displayed floor is `631`.  These are lower bounds only.

## 5. Fixed-parent scope and the exact optimum `180`

The `605` trapped length-three runs apply to the first retained-occurrence
macro family.  The stronger occurrence-transversal statement is different:
the fixed K15 parent has `1425` old length-four patterns, and `165` of them
have four unique rank-six physical colours, eleven per old coordinate.
They survive every one-occurrence-per-colour transversal, every macro
permutation/reversal, and every port completion.

I reran the independent source-level reconstruction of those `165` forced
patterns.  It reproduces the rank-six multiplicity profile
`1^3630 2^1320 3^55`, `1425` patterns, `165` forced rows, and the base CNF
dimensions `2805` variables and `4285` clauses, including `165` explicit
empty clauses.

The upgraded exact optimum `180` is also correctly scoped and encoded.
The independently replayed witness chooses one occurrence of each of the
`5005` colours, reconstructs `1430` literal macro paths, and has exactly
`180=12*15` internal short runs.  The bound-179 CNF introduces a violation
variable `y_P` for each of the `1260` non-forced patterns and encodes

```text
y_P iff every selectable physical edge of P is retained.
```

Unique edges are correctly omitted from the conjunction because they are
forced.  The forward counter soundly imposes at most `14` true `y_P` values,
so UNSAT proves at least `165+15=180`.  The CNF is syntactically consistent:
`22965` variables, `44382` clauses, maximum literal variable `22965`, and no
empty input clause.  The retained `drat-trim` transcript says `s VERIFIED`,
with a `5531`-clause core and `99145` resolution steps.  I independently
audited the encoder semantics and replayed the upper-bound witness; a local
`drat-trim` binary was not available for a fresh proof replay.

Relevant frozen hashes are:

```text
4cbf25a3f4d322c54ce91b068dc08e49223e86019d3dfccc51f065a3860cf19c  bound179.cnf
8d55ea0215b62b43aaba7a94eda194555227ffdb0a73eb174d227afa0695c018  bound179.drat
78bd2f06aa9938999374176d676dec9337fcb61a231a3f7287bfb6468f25d465  bound179.dratcheck.txt
f5b4095a131ad77ebb0a6d95d62a4a94a66852dc2979180759001ac08ec05466  bound179.map.json
8ecf43e13bfb7e0c204847f3c480dadc76af39dec979d245dc73bd5a5b5717b4  optimal.json
71ffd874fe520daf8609902cf2f12df181a55b1b38d3299633bb95c7e5e89a10  optimal.verify.json
```

This closes only the fixed-parent flat macro-transversal route.  A different
parent chronology or a genuinely nonflat compiler is not obstructed.

## 6. Corrections identified during the audit

### Correction A: connectedness is required for the run-count conclusion

In the companion theorem's facet-phase flux statement, the identity
`# removals_x = # insertions_x` is correct without a connectedness
assumption.  The sentence “it may change run lengths, but not the number of
runs” must, however, be conditioned on the toggled factor remaining
Hamilton.  In a disconnected spanning two-factor, a component may be wholly
`x`-positive; such a component contributes a cyclic positive run but no mixed
boundary.  Zero mixed-boundary flux alone does not exclude this case.

The audited companion snapshot already contains this qualification at
Theorem 3.2; this paragraph records why it is mathematically necessary.

### Correction B: overlapping packet deltas must be current-state deltas

The main note's final composition criterion is exact only if the “sum of
exact centered deltas” means either:

1. deltas recomputed sequentially in the carrier produced by all preceding
   packets; or
2. the single direct final-minus-initial occurrence vector.

Precomputed deltas of overlapping packets in the original carrier need not
add, because an earlier packet may change the center/neighbour data used by a
later one.  The companion composition theorem already states the correct
global/sequential rule; the main summary should use the same qualification.

### Clarifications C--E

1. Replace “equivalently ... `322` packets” by “consequently ... at least
   `322` packets.”  The second bound follows from the first plus the
   three-cut restriction; it is not a biconditional characterization.
2. State the q1 shortening argument for a simple/Hamilton owner order.  This
   is exactly the setting used in the adaptive floor.
3. State Corollary 5.2 as the explicit multiset replacement
   `{t,L}->{u,v}` with all other run lengths fixed.  This removes any possible
   reading that arbitrary merging/splitting packets obey the two-run donor
   bound.

## 7. Sharp surviving boundary

After these corrections, the decisive content survives unchanged:

* upper q2 is an exact width-three ledger;
* the displayed alternating hex is a literal Pareto-positive q1-exact
  residence-transfer zipper;
* any hex-only repair of this frozen carrier needs at least `631` packets;
* the fixed K15 parent leaves at least `180` internal short runs under every
  occurrence transversal, so occurrence/flow-only repair is closed;
* changing the parent chronology or using a nonflat compiler remains live;
* global packet compatibility, higher shadows, endpoints, and one integral
  common compiler remain unproved.

## 8. Post-correction snapshot check

After the audit findings were communicated, the main theorem was revised and
then frozen for this audit at the following SHA-256:

```text
1112e7743381a193de8f1aaac3631f0304ae16ad2e89b70eaab67afae4d155e1
  MATH_THEOREM_AD_K17_GUARDED_Q2_FLAG_PACKET_AND_RESIDENCE_HITTING_20260731.md
```

The companion remained at audited SHA
`e0055b600538a37d3855909b7963504d3cde820317d2df2fabd64e8f96c15ae1`.
I checked the corrected main snapshot directly.  It now:

1. says “consequently” for the `322`-packet inference;
2. scopes the adaptive hex floors to simple Hamilton intermediate orders; and
3. requires either direct final-minus-initial q2 loads or sequential
   current-state deltas, explicitly forbidding sums of precomputed overlapping
   packet deltas;
4. states the donor claim as the exact multiset replacement
   `{t,L}->{u,v}` with all other runs fixed; and
5. includes separate final upper-q1 and all-higher-upper service/restoration
   rows, with the subsequent prose correctly referring to the other four rows.

The companion explicitly conditions run-count preservation on connected
`K'`.  Thus every decisive correction and wording clarification identified in
this audit is closed.  The final verdict on the two frozen theorem snapshots
is **PASS**.

## 9. Occurrence-coherence addendum audit

An authoritative occurrence-coherence addendum was incorporated after the
preceding PASS.  The final addendum snapshots audited here are

```text
8be1321a55317b72f2b7c758a3404b4595feaa41c884a84f8c7cbb4046c3f048
  MATH_THEOREM_AD_K17_GUARDED_Q2_FLAG_PACKET_AND_RESIDENCE_HITTING_20260731.md
bf7c6e994532ca5c5cfa28ef6ab3646a67e5e9bad147162d5c8ca7c10e982dab
  MATH_THEOREM_K17_CATALAN_RESIDENCE_TRANSFER_AND_PHASE_PORT_COMPOSITION_20260731.md
```

### 9.1 Direct reconstruction of the upper-provider profiles

I independently reconstructed this ledger from the literal oriented parent
components.  For every physical parent edge `i` I formed

```text
C_i=T_i intersect T_(i+1),
Z_i=C_i intersect C_(i+1),
U_i=T_i union T_(i+1).
```

An edge is upper-unique precisely when its `U_i` has global multiplicity one.
For the `6390+45` parent, the upper-colour multiplicity profile is

```text
1^3675 2^1230 3^100,
```

and the `5005` rank-six fibres have upper-unique occurrence profile

```text
u_Z: 0^1835 1^2685 2^465 3^20.
```

Both consistency checks close:

```text
1835+2685+465+20 = 5005,
2685+2*465+3*20 = 3675.
```

For the saved octahedral parent

```text
scratch/k15_octahedral_translation_descent_r2.factor.json
SHA-256 13c5ecaddc94bd4a240c9b2ce348f5db4508cb340658b2b0f4797b8c80472dfb
```

the independent reconstruction gives

```text
u_Z: 0^1735 1^2865 2^405,
```

again summing to `5005` fibres and `3675` unique physical providers.

### 9.2 Exact marginal theorem

In a fibre with `u_Z` upper-unique occurrences, a one-occurrence transversal
can retain at most one and therefore deletes at least `(u_Z-1)^+`.  Choosing
an upper-unique occurrence whenever one exists attains the bound independently
in every fibre.  Thus

```text
min D_up = sum_Z (u_Z-1)^+.
```

The reconstructed profiles give exactly

```text
current parent: 465+2*20 = 505;
octahedral parent: 405.
```

These count deleted internal unique witnesses, not final child holes: a port
may recreate the same upper target.

### 9.3 Correlation scope

The upper-provider rewards and all residence hyperclauses use the same
occurrence variables.  Separate marginal minimizers therefore cannot be
composed.  The final text states the precise arithmetic boundary correctly:
every transversal has `U>=505` and `R>=180`, so the formal sum inequality
`U+R>=685` is valid; what remains unknown is equality, a simultaneous
minimizer, or any interpretation of `685` as a physical child-hole count.

The octahedral exact residence value `150` is imported, with explicit scope,
from

```text
MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md
  SHA-256 c2b0920221070de61ced078a30099e6dba8d421fd2de76070e16483456ace24e
MATH_AUDIT_R_ODD_DIAMOND_OCCURRENCE_COHERENCE_AND_PORT_STATE_20260731.md
  SHA-256 4345919acc43b6c244798621cb816db27ad3dd36d8f8403e1bfde9c21f4634ce
```

and is not independently recertified by this AD addendum audit.  The main
theorem now says exactly that: AD directly reconstructs the octahedral `405`
profile, while `150` is an authoritative imported marginal optimum belonging
to a different parent chronology.  Neither source claims a common
octahedral transversal attaining `(405,150)`.

The companion conclusion carries the same joint-state caveat and does not
turn either marginal debt into a packet-composition theorem.  Accordingly the
addendum verdict, at the two final hashes above, is **PASS-ADDENDUM**.

The main addendum's stronger exported state
`(R(x),A(x),sigma(x))` is also correctly scoped: the first two entries retain
the literal identities of surviving residence packets and upper-unique
providers, while `sigma(x)` retains the induced macro paths, endpoint colours,
and port-degree demands.  Replacing these sets by their cardinalities would
lose exactly the downstream target identity which Proposition 7.4 warns is
correlated.  Choosing the residual b-flow only after this tuple is fixed is
therefore the correct dependency order.
