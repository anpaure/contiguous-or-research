# Exact SAT design for the Type-II reverse pin-load theorem

> Production status (2026-07-23): this audited design is now implemented
> behind `K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1`.  See
> `K11_TYPE2_REVERSE_PIN_LOAD_IMPLEMENTATION_AUDIT.md` for the frozen source,
> guard-off identity, and exact build inventories.  References below to a
> “proposed” edit describe the pre-implementation design stage.

## 1. Verdict and scope

`K11_TYPE2_REVERSE_PIN_LOAD.md` proves the following in the exact Type-II
two-component branch.  Let `C1` be the slack-one component, `C2` the
slack-two component, and

```text
o_b = #{i in C2 : b in A[i]}.
```

If coordinate `b` is absent from `C1`, then

```text
o_b>=59,
3 o_b + z + y2 >=386,                                (1.1)
```

where `z` is the number of literal rank-five entries and `y2` is the number
of selected rank-five witnesses of width two.

This note gives an exact production design behind a proposed optional guard

```text
K11_FOREST_TYPE2_REVERSE_PIN_LOAD=1.
```

No production source is edited here.  With one zero-CNF refactor exposing
the already allocated slack-two occurrence bank, the exact incremental
inventory is

```text
15,945 variables / 96,149 clauses.                    (1.2)
```

If that occurrence bank is rebuilt instead of reused, the fallback inventory
is

```text
21,060 variables / 111,494 clauses.                   (1.3)
```

The preferred design is (1.2).

## 2. Prerequisites and reusable state

The new guard should require

```text
K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION=1.
```

That prerequisite already transitively requires

```text
K11_FOREST_RANK_FILTRATION_TYPE2=1,
K11_FOREST_LOCAL_DENSITY_PB=1,
K11_FOREST_BAND_CUTS=1,
K11_FOREST_JOINT_BAND_CUTS=1.
```

No named-cell guard is logically required.  The length-two confinement used
by the theorem follows directly from the exact two-component slack theorem,
and the selected rank-five boundary schedule exists independently of the
optional named-cell propagation module.

The following current fields are reused:

```text
TypeIITwoComponentPinPlan::slack_one_membership[p],
TypeIITwoComponentPinPlan::slack_two_membership[p],
RankFiltrationTypeIIPlan::two_components_flag,
JointBandCutPlan::bits[j][bit],
JointBandCutPlan::one.
```

The current pin-localization constructor already allocates, for every
coordinate and position, the exact conjunction

```text
slack_two_membership[p] AND A[p,b]                    (2.1)
```

while forming `slack_two_has[b]`; it presently keeps those literals in a
temporary local vector.  Retain them in a field

```text
array<vector<int>,K> slack_two_occurrence;
```

instead.  This changes neither the clause stream nor the variable count of
the existing module.  The reverse plan uses these 5,115 existing literals as
the inputs of its `o_b` counters.

## 3. Exact slack-one coordinate union

The antecedent in (1.1) is `b notin OR(C1)`, so the reverse plan must
materialize the coordinate union of `C1`.  For each `b,p`, define

```text
occ1[b,p] <-> slack_one_membership[p] AND A[p,b].      (3.1)
```

Use the standard three-clause bidirectional AND.  Define

```text
has1[b] <-> OR_p occ1[b,p]                             (3.2)
```

with 465 forward binary clauses and one reverse clause.

For one coordinate this costs

```text
variables: 465 occurrence flags + 1 has flag =466,
clauses:   3*465 +465 +1 =1,861.
```

For all eleven coordinates the exact bank is

```text
5,126 variables / 20,471 clauses.                     (3.3)
```

Both directions in (3.2) are necessary.  A one-way `has1` flag could be set
true merely to escape the conditional pin-load rows.

## 4. Exact occurrence counters

For each coordinate, apply the production Wallace compressor plus retained
final ripple carry to the 465 reused literals (2.1).  The exact bucket
profile is

```text
[1,2,1,1,2,1,2,2].
```

There are 453 compressor full adders and eight final ripple full adders, so
one counter has

```text
461 full adders,
922 variables / 6,454 clauses,
9 output bits.                                         (4.1)
```

The eleven counters therefore cost

```text
10,142 variables / 70,994 clauses.                    (4.2)
```

Each output is the ordinary integer `o_b` in `[0,465]`; no modular carry is
discarded.

The conditional comparison `o_b>=59` uses the existing direct
first-difference constant comparator with escape literals

```text
{-two_components, has1[b]}.                            (4.3)
```

It is active exactly when two components exist and `C1` omits `b`.  Since

```text
59 = 000111011_2
```

has five set bits, this emits five clauses per coordinate and 55 total,
with no auxiliary variable.

## 5. A chain-independent expression for `z+y2`

Let `h1,...,h6` be the existing exact rank-five transition boundaries.  The
three allowed chains have the following profiles:

```text
A: y0=462+h1-h6,          y2=h3+h5-h2-h4,
B: y0=462+h1+h5-h4-h6,   y2=h3-h2,
C: y0=462+h1+h3-h2-h6,   y2=h5-h4.
```

In every case the sum collapses to

```text
y0+y2 = 462+h1+h3+h5-h2-h4-h6.                       (5.1)
```

In the two-component Type-II branch, duplicate excess is zero, so every
literal rank-five entry is selected as a singleton and

```text
z=y0.                                                  (5.2)
```

Consequently the second row of (1.1) is equivalent, on its active branch,
to the unsigned comparison

```text
h2+h4+h6 <= 3 o_b + h1+h3+h5+76.                     (5.3)
```

This is the main implementation simplification.  There is no need to
materialize `y2`, subtract boundaries, select one of three arithmetic
circuits, or create per-chain guard variables.

## 6. Exact arithmetic circuit

All additions use the production 14-clause full adder and retain the final
carry.  Build the two coordinate-independent sides

```text
left       = (h2+h4)+h6,
right_core = (h1+h3)+(h5+76).                         (6.1)
```

Each `h` vector has nine bits and constant 76 has seven bits.  The exact
global arithmetic is

| sum | full adders | variables | clauses | output width |
|---|---:|---:|---:|---:|
| `h2+h4` | 9 | 18 | 126 | 10 |
| `(h2+h4)+h6` | 10 | 20 | 140 | 11 |
| `h1+h3` | 9 | 18 | 126 | 10 |
| `h5+76` | 9 | 18 | 126 | 10 |
| `(h1+h3)+(h5+76)` | 10 | 20 | 140 | 11 |
| **global total** | **47** | **94** | **658** | |

For each coordinate, shift the nine-bit `o_b` vector left once and add it
back to obtain `3o_b`, then add `right_core`:

| sum | full adders | variables | clauses | output width |
|---|---:|---:|---:|---:|
| `o_b+(o_b<<1)` | 10 | 20 | 140 | 11 |
| `3o_b+right_core` | 11 | 22 | 154 | 12 |

The guarded exact unsigned comparison of the eleven-bit `left` with this
twelve-bit right side uses eleven prefix-equality variables and

```text
12 + 5*(12-1) =67 clauses.                            (6.2)
```

Every comparison clause and every prefix-equality definition is prefixed by
the same escape literals (4.3).  Thus inactive arithmetic auxiliaries cannot
constrain the formula, while on the active branch the equality chain is
bidirectional and the first unequal bit decides the comparison exactly.

The per-coordinate coupled row therefore costs

```text
53 variables / 361 clauses.                           (6.3)
```

Across eleven coordinates, adding the shared global arithmetic gives

```text
677 variables / 4,629 clauses.                        (6.4)
```

## 7. Frozen incremental inventory

With the existing slack-two occurrences retained at zero cost:

| component | variables | clauses |
|---|---:|---:|
| exact slack-one coordinate union | 5,126 | 20,471 |
| eleven 465-input `o_b` counters | 10,142 | 70,994 |
| shared and per-coordinate coupled arithmetic | 677 | 4,629 |
| eleven conditional `o_b>=59` comparisons | 0 | 55 |
| **total** | **15,945** | **96,149** |

If the 5,115 slack-two occurrence conjunctions are rebuilt, add

```text
5,115 variables / 15,345 clauses,
```

which gives the fallback inventory (1.3).

## 8. Proposed source integration

The production edit, after a separate audit, should have the following
shape.

1. Parse `K11_FOREST_TYPE2_REVERSE_PIN_LOAD` and reject it unless
   `K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION` is enabled.
2. Retain the existing slack-two occurrence literals in
   `TypeIITwoComponentPinPlan`; this refactor must reproduce the old clause
   stream byte for byte when the new guard is off.
3. Construct `TypeIIReversePinLoadPlan` after
   `TypeIITwoComponentPinPlan`, passing the local-density plan, joint-boundary
   plan, Type-II plan, and pin-localization plan.
4. Emit its clauses before solving and report the four inventory categories
   in Section 7.
5. Add negative guard tests and compare the complete guard-off clause-stream
   hash with the current source.

Suggested constructor signature:

```text
TypeIIReversePinLoadPlan(
    int& next,
    const LocalDensityPBPlan& local,
    const JointBandCutPlan& joint,
    const RankFiltrationTypeIIPlan& type_two,
    const TypeIITwoComponentPinPlan& pin);
```

The module allocates and emits nothing when absent.  It applies only under
`two_components_flag`; the one-component Type-II subcases remain unchanged.

## 9. Independent checks

The companion script

```text
python3 scratch/check_k11_type2_reverse_pin_load_implementation.py
```

checks:

* the three chain formulas and the invariant identity (5.1);
* all AND/OR gate truth tables;
* the direct conditional `>=59` comparator;
* the guarded prefix comparator, including existential auxiliary states when
  inactive;
* the Wallace bucket profile and retained carry;
* every arithmetic width, variable count, and clause count;
* the preferred and fallback inventories.

This is an implementation design, not a source audit, SAT result, or proof of
`nu(11)>465`.
