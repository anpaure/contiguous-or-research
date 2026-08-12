# Audit: K16 H1 four-portal structural phase and one-clause implication core

Date: 2026-07-30

## Verdict

**GO as a near-model and implication-core certificate.**  For the exact
explicit-witness CNF on the authenticated H1 joint13 fibre, a deterministic
incumbent-derived total assignment satisfies 55,851 of 55,852 clauses.  Its
only false clause is the bit-11 availability requirement for the selected
`0x2c6d` near-witness:

```text
(-467 OR 1621).
```

This identifies a small exact resolution core.  The failed bit-11 row gives
36 safe binary implied conflicts; eliminating all three availability bits
required by the singleton chart gives 62 distinct binary conflicts.  It is
not a SAT candidate, an UNSAT certificate, or a claim that the near-witness
choice is forced.

No solver was launched or duplicated for this audit.

## Exact formula

The independently generated explicit-witness formula is exact for arbitrary
nonzero reassignment of the thirteen four-portal hull cells, with all other
positions frozen and no edit-cardinality row.  Its dimensions are

```text
1790 variables
55852 clauses
121679 literals.
```

The variables are:

- 1,595 explicit chart choices: 29 local interval forms for each of 55
  residual targets; and
- 195 availability variables: 15 noncommon bits at each of 13 cells.

Every target contains common bit 6, which is implicit.  The four clause
families have counts

```text
choice ALO                 55
choice pairwise AMO     22330
need/availability       10301
omitter/availability    23166.
```

Frozen hashes are:

| artifact | SHA-256 |
|---|---|
| witness CNF | `f7c7c00592a682b994f6656ddf8f335ab272cd1517fb44a6cbd4e29061e19e47` |
| witness map | `146f81f628148b2fd904bb5e030236135b00cd502aa2d58051ebb32d6e82638a` |
| builder | `2a2db4190e794f13fd0e6dc4da9de537523cca3999271cdd28913829959f7647` |
| independent formula audit | `e2b3f02f40733096327ed90eaa7b8106bcbd2e97e2a7923e60f268209c629279` |

The independent audit reconstructs every clause from the separately audited
occupancy ledger.  The CNF's exact feasibility status remains unresolved.

## Deterministic structural phase

For every covered residual target, choose the least-index local chart that is
literally realized by the incumbent H1 values: every editable cell on the
chart is a submask of the target and their OR supplies the chart's residual
need.  For the sole hole, choose the source-compatible chart minimizing

```text
(number of missing need bits, witness index).
```

Finally set each availability variable to the corresponding incumbent cell
bit.

All 54 covered targets have a realized chart.  For the hole

```text
H = 0x2c6d,
```

the unique tie-broken nearest chart is witness index 2, choice variable 467:

```text
editable interval:  [1,1]
fixed-context residual need: 0x2808
incumbent p1 value: 0x2068
missing need:       0x0800 = bit 11.
```

The corresponding bit-11 availability at flat cell 1 / physical position 1
is variable 1621.  Direct evaluation of all 55,852 DIMACS rows gives exactly
one failure, one-based clause 32,463:

```text
C_H = (-467 OR 1621).
```

Every other choice, at-most-one, need, and omitter row is true.  This is a
fully assigned Hamming-distance-one clause near-model, not merely a partial
phase heuristic.

## The binary implication core

If a selected target omits bit 11 and its chosen chart crosses position 1,
the formula contains

```text
C_z = (-z OR -1621).
```

Resolving `C_H` with `C_z` gives the sound availability-free conflict

```text
(-467 OR -z).
```

There are exactly 36 such crossing chart choices: two charts (`[0,1]` and
`[1,1]`) for each of 18 bit-11-omitting targets.  Hence retaining choice 467
forces all 36 choices false.  These 36 binary resolvents may be appended as
redundant strengthening rows or used as the exact local quotient obtained by
eliminating variable 1621 from this singleton need clause.

The incumbent-derived phase selects three of the blockers:

| target | selected chart variable | witness index | omitter clause | resolved conflict |
|---|---:|---:|---|---|
| `0x246d` | 148 | 2 | `(-148 OR -1621)` | `(-467 OR -148)` |
| `0x346d` | 612 | 2 | `(-612 OR -1621)` | `(-467 OR -612)` |
| `0x766d` | 873 | 2 | `(-873 OR -1621)` | `(-467 OR -873)` |

Any one selected blocker plus `C_H` is a two-clause explanation of the false
availability requirement under the phase units.  The presence of three says
that a phase retaining choice 467 must reroute at least these three incumbent
chart selections, but it is not a global lower bound on physical edits.

At target level, each of the 18 omitting targets must choose one of its 27
position-1-avoiding charts when choice 467 is true.  This conditional
27-choice row is already implied by its exact-one clauses together with the
two binary conflicts, so it is a propagation aid rather than new mathematics.

## Full singleton availability quotient

Choice 467's residual need is `0x2808`, so its singleton interval actually
forces three availability variables:

| required bit | availability variable | crossing omitter choices | affected targets |
|---:|---:|---:|---:|
| 3 | 1614 | 30 | 15 |
| 11 | 1621 | 36 | 18 |
| 13 | 1623 | 30 | 15 |

Resolving each singleton need row with every matching omitter row and merging
duplicates gives 62 distinct binary conflicts across 31 targets.  Twenty-eight
choice variables omit one required bit and 34 omit two; none omits all three.
The 36 bit-11 conflicts above are the subset directly exposed by the sole
false clause.  Bits 3 and 13 are already present in incumbent `p1=0x2068`, so
their need clauses are true in the structural phase, but their resolvents are
equally valid formula consequences.

Thus the exact local quotient is:

```text
x467 => every selected chart crossing position 1
        belongs to a target containing bits 3, 11, and 13.
```

Equivalently, all 62 chart choices violating that containment are false under
`x467`.  This is a safe redundant strengthening of the independently owned
witness formula; no strengthened solver was launched here.

## Exact local unit closure and portal cascade

The complete solver-free quotient under unit `x467` is consistent but much
smaller than the original local phase.

The singleton chart forces bits `{3,11,13}` present at flat cell 1.  Because
its target is `0x2c6d`, it also forces bits
`{1,4,7,8,9,12,14,15}` absent there.  Common bit 6 is implicit, and only
bits `{0,2,5,10}` remain free.  Thus the parent existential availability
encoding admits 16 logical patterns at flat cell 1 under `x467`.  These are
an upper bound, not sixteen distinct canonical physical values, because the
reverse availability implications were intentionally omitted.

The exact physical meet quotient has only six states.  A canonical flat1 cell
is the intersection of `H=0x2c6d` with all selected target labels crossing the
cell.  All 24 eligible labels contain bit 0 as well as the forced core, and
their projections to H have the meet-closed state set

```text
0x2849, 0x2869, 0x286d, 0x2c49, 0x2c69, 0x2c6d.
```

Every state has a one-label intersection certificate, so the six-state meet
condition alone has no Hall defect.  These six states classify the canonical
intersection normal form; they do not assert that every noncanonical raw
physical assignment at flat1 already belongs to this list.  Equisatisfiability
comes from the previously proved normalization.

Exhaustive unit propagation assigns 123 variables:

```text
4 true: 467, 1614, 1621, 1623
119 false, including 111 chart choices.
```

The 55 target domains split exactly as follows:

| conditional domain class | targets |
|---|---:|
| fixed hole chart `x467` | 1 |
| omit at least one required core bit, so cannot touch flat1 | 31 |
| contain the core but singleton-flat1 needs an H-external bit | 21 |
| retain singleton-flat1: `0x286d,0x2c69` | 2 |

There is a further exact first-collar cascade.  For each of the 21 surviving
span choices `z=[0,1]`, let

```text
E = need(z) & ~0x2c6d.
```

Every bit of `E` must be supplied at flat cell 0.  If a flat0-crossing choice
`w` belongs to a target omitting any bit of `E`, clause resolution gives

```text
(-467 OR -z OR -w).
```

The exhaustive census has 11 distinct nonzero `E` signatures, 1,878 safe
ternary resolvents, and 1,293 nontrivial rows after the unit closure.  Combining
these with the exact-one target rows gives 876 target-level implications of
the form

```text
x467 AND z  =>  target U leaves the first collar.
```

Each span choice ejects between 29 and 51 other target domains from collar 0.
Optimizing jointly over the exact six physical flat1 meet states gives the
following sharp first-collar minima:

| flat1 state | minimum flat0 need | minimum targets forced out of collar0 |
|---|---|---:|
| `0x2849` | `0x0080` | 33 |
| `0x2869` | `0x0400` | 19 |
| `0x286d` | `0x0000` | 0 |
| `0x2c49` | `0x0080` | 33 |
| `0x2c69` | `0x0000` | 0 |
| `0x2c6d` | `0x0000` | 0 |

The meet/need DP has only 4--26 states per branch and retains a canonical
minimizer and the exact ejected-target set for every physical state.  The
three zero-ejection states prove that no contradiction follows inside the
first collar alone.  Any no-go must couple the other three state branches—or
the nonzero ejection sets—to capacity or availability in the remaining
collars.  “Sharp” here means sharp for this forced-ejection cascade predicate;
additional chart compatibility can only force more ejections and physical
joint attainability is not asserted.

The exact quotient audit is

| artifact | SHA-256 |
|---|---|
| quotient driver | `2fe8dc60e89d31dccc2798e38f5044ee2370dc8406d411b477400c2c549b81f5` |
| quotient JSON | `fbe983abbad1e8996f6aee2bc4f4146913bf2a1fa2fbea1ec66cd0b71d85958f` |
| six-state meet driver | `e1ee0ee3450af05c855d71ddde74627e6210eaf79b836bc93c8b3f754ac24406` |
| six-state meet JSON | `e8a4e58cea9fafb93a4fd97e28a5e665b4f698cc486ab52d2687cbba2a934be3` |
| six-state cascade driver | `08b104496767097316d9ea6583782571704aadd68f46779f64c920a9d0943ffb` |
| six-state cascade JSON | `4d505ab2cbf83d590614edfb3fe43847699e0f5c45364fbf3505055c0dd450d8` |

## Exact scope boundary

The audit proves only:

1. the stated total assignment falsifies exactly one formula clause; and
2. the 36 bit-11 and 62 full-singleton binary conflicts are logical resolvents
   of authenticated CNF rows; and
3. the displayed unit closure and conditional collar-ejection clauses follow
   by exhaustive unit propagation and resolution.

It does not prove that variable 467 must be true, that any blocker choice is
forced, that the 36 rows alone decide the formula, or that the frozen
thirteen-cell support is globally exhaustive.  A phase-flipped solver run is
owned by the independent four-block lane and is deliberately not duplicated
here.

The retained audit artifacts are:

| artifact | SHA-256 |
|---|---|
| bit-11 audit driver | `90b666bfcff6e2edbab22c2bf4b991fa127d1fea0e1cd89ba6af61e64a36d087` |
| bit-11 audit JSON | `88e15e7f564e278ea37ac6a50033453c6cb06eade3644bdf9e5676c78b26ae3a` |
| full-singleton audit driver | `353d4fc544b7950ee4325d5ed647cc489e18c8de210c6b7d801dc3b56886aa4e` |
| full-singleton audit JSON | `94a5af9e76cf5e4a588297686f540a245660a9214b2002c0e9e7013453700100` |

The global K16 bracket is unchanged:

```text
12873 <= nu(16) <= 12874.
```
