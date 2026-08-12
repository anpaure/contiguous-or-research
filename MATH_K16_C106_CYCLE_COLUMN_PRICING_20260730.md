# K16 frozen-source C106 cycle-column pricing

## Scope

This note concerns only the frozen length-eight K16 source and the exact
SSSSS branch at cut count (C=106).  It is a constructive branch-and-price
lane, not a statement about arbitrary K16 sources and not a global lower
bound.

The frozen inputs are the seam ledger
`k16_len8_source_seam_ledger_20260730.bin` (SHA-256
`832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657`)
and direct certificate
`k16_direct_cycle_dual_exact_20260730.audit.json` (SHA-256
`29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d`).

## Exact cycle master

Every endpoint-balanced capacity-one seam selection is a vertex-disjoint
union of directed cycles.  In the SSSSS equality branch each selected target
has multiplicity exactly one and total direct slack is five.  A cycle column
therefore records

* its seam length;
* its set of serviced defects (with no repetition);
* its direct slack; and
* its used port vertices.

The master chooses vertex-disjoint columns, services all 93 targets exactly
once, has total length 106, and has total slack five.  The telescoping direct
identity on every cycle is

\[
2|C|=\sum_t w_t\mu_C(t)+s(C).
\]

The original exact rational point decomposes into 94 cycle generators on 662
seams.  Only eight of those generators are target-simple.  Exhaustive
two-cycle cross-splicing at common vertices tested 255,102 hybrids and added
no target-simple column.  Moreover, the 662-seam support, its complete
1,317-seam induced closure on the same 571 ports, and its 16,481-seam
incident closure are all infeasible.  Hence an integer SSSSS pack must contain
an excursion with an outside-to-outside seam.

The first exact excursion pool contains 4,808 independently replayed
target-simple columns.  Its exact master is infeasible (pool-relative only).
The optimum relaxed vertex-disjoint pack is nevertheless informative:

\[
|E|=99,\qquad s=5,\qquad
|\operatorname{supp}\mu|=79,\qquad
\sum_t w_t\mu(t)=193.
\]

It consists of 23 cycles.  The fourteen missing targets are

\[
\{33337,35044,36417,36935,37320,40066,41102,41872,
47364,49436,50976,51235,58385,61960\},
\]

and every one has weight one.

## Solver-free no-ruin barrier

Freeze those 23 cycles.  Any exact complement would have seven seams and
zero slack.  It must service all fourteen missing unit targets once.  A full
ledger census, after forbidding the 99 retained port vertices and forbidding
hits on already covered targets, leaves 37,945 admissible slack-zero seams.
Every such seam services at most one of the fourteen residual targets.
Consequently seven residual seams can supply at most seven required
occurrences, while exact completion requires fourteen.  Thus:

> **Conditional no-ruin theorem.** The frozen 23-cycle near-pack cannot be
> completed by adding seven seams without changing at least one retained
> cycle.

This is solver-free and is frozen in
`scratch/k16_c106_cycle_columns_e4_residual_barrier_20260730.audit.json`
(SHA-256
`c9836c0781b0ab3bdce6e3180b9d14145f96f3db8ec4b18c08f530f52c7fee44`).
It is conditional on this near-pack and is not a C106 impossibility theorem.

## Ruin/recreate frontier

Removing each retained cycle in turn and pricing the exact complementary
circulation over the full 211,604-seam ledger closes **all 23 one-cycle ruin
faces as infeasible**.  Twenty-two close in the initial census.  The only
initially unresolved face removes pool column 2371, a length-19 slack-three
cycle; its unrestricted residual circulation closes infeasible in 27 seconds,
and its independent single-replacement-cycle formulation closes infeasible in
75 seconds.

The next exact step is paired ruin.
It should be treated as a bidirectional resource-constrained path join: retain
the other 21 cycles, join partial paths using the residual target mask,
length, slack, and forbidden-port resources, and add every resulting cycle as
a master column.  Random raw-word or random seam perturbations do not respect
this exact residue and are not the pricing method used here.

## Exact radius-two closure

The authenticated CRT-914 census leaves exactly 208 structurally admissible
pairs of columns outside the 662-seam fractional support: four directed
quotient 2-cycles and 204 loop-loop pairs.  The independent signed-lattice
audit

`scratch/provider56_k16_c106_sssss_crt914_radius2_lattice_20260730.audit.json`

excludes all 208 before nonnegativity, binary bounds, support-port capacity or
any physical row is imposed.  The first-failing prime-power histogram is

\[
32:198,\qquad 5:8,\qquad 63079:2.
\]

Consequently every binary SSSSS solution uses at least three columns outside
the frozen 662-seam support.  This is a global frozen-face theorem, not a
statement about one incumbent.

## Guided 6--10-cycle neighborhoods

For each of the fourteen unit targets missed by the 23-cycle near-pack, exact
single-cycle pricing at slack one produced a target-simple repair cycle.  None
of these cycles intersects a retained cycle in a port.  Their obstruction is
instead service overlap: inserting one repair cycle forces the removal of
between six and ten retained cycles.  Thus the pricing portfolio derives the
first nontrivial large neighborhoods rather than choosing their radii
heuristically.

`scratch/solve_k16_c106_cycle_column_lns_20260730.py` freezes all other cycles
and solves the full residual seam circulation while preserving endpoint
balance, capacity one, count 106, slack five, and target multiplicity at most
one.  It can either hint or force the priced cycle.  The first forced case,
repairing target 36935 on its seven-cycle conflict support, is exact
infeasible.  The remaining derived supports are a finite constructive search;
timed negative cases are not promoted to no-go theorems.

The most natural radius-three incumbent face is also closed.  Removing the
three large columns 615, 2371 and 2501 leaves residual count 61, slack five
and 63 targets.  Exact full-ledger reconstruction over 208,842 admissible
seams is infeasible after 33,676 branches.  This conditional finite result is
frozen in
`scratch/k16_c106_cycle_columns_lns_single_big3_exact.audit.json` (file
SHA-256
`95d22a6da23c65ade879d1da1acdcecd861b197759c9c90e17fc3f656beed186`).

The exhaustive slack-core triple census is stronger: for every third retained
cycle (i\notin\{4,5\}), the full residual face obtained by ruining
\(\{4,5,i\}\) is infeasible.  All 21 cases are authenticated by
`scratch/k16_c106_cycle_columns_lns_triples_complete_20260730.audit.json`
(file SHA-256
`423fbfd55f2aa6613b5caeb85c8d2e2284b5a5008a0f6454add4ee0f8656dfe5`).

Likewise, forcing each of the fourteen currently priced slack-one repair
cycles and ruining precisely its six-to-ten service-conflicting incumbent
cycles gives fourteen infeasible exact residual faces.  Their consolidated
manifest is
`scratch/k16_c106_cycle_columns_lns_priced_forced_complete_20260730.audit.json`
(file SHA-256
`b2cc2de74ff4d92ab7dfa6d20341ce63a7c6da3d5d6e6ccc74ee09eed3a5da30`).
These are neighborhood no-gos, not a global SSSSS theorem: augmenting a priced
support, using a different price cycle, or moving four or more cycles without
the present service-conflict pattern remains open.

## Verification boundary

Any reduced candidate must first pass
`scratch/replay_k16_floor106_candidate_20260730.py`.  This is a distinct,
fail-closed C106 checker; the C105 checker is not applicable.  A reduced pass
is still not a K16 construction until the same checker passes its physical
separation, two-cycle, signed-row, residence, survivor, and all-depth literal
replays.
