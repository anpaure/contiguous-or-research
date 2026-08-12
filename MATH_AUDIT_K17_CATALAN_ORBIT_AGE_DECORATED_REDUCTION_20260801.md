# Audit of the `k=17` Catalan-orbit age-decorated reduction

Date: 2026-08-01

Audited source:

```text
MATH_REDUCTION_K17_CATALAN_ORBIT_AGE_DECORATED_RAINBOW_CYCLE_20260801.md
```

Verdict: the corrected implication is sound.  It is a conditional
one-copy reduction, not an existence proof.  Its upper-safe physical
opening is essential and remains unconstructed.

## 1. Rows that pass

### Free orbits and denominator

For prime 17, every nonempty proper subset has a free rotation orbit.
Therefore the rank-nine and rank-eight quotient layers both have

\[
 {1\over17}\binom{17}{9}={1\over17}\binom{17}{8}=1430
\]

vertices.  The type masses sum to 1430, and the proper-suffix capacities
at ranks two through eight equal the target-orbit counts exactly.

### Changing-owner age lemma

For

\[
 T'=T-\{\alpha\}+\{\beta\},\qquad C_3=\{\alpha\},
\]

selecting `c'_(i+1)` survivors from `C_i` and refreshing every other
retained coordinate plus `beta` into age zero gives a disjoint partition
of `T'` with the declared type.  The identity

\[
 |C'_0|=1+\sum_{i<3}(c_i-c'_{i+1})=c'_0
\]

is correct.  This is exactly the literal last-occurrence update.

### Residence and deepest suffix

Every selected transition deletes the unique age-three coordinate.  A
newly inserted or refreshed coordinate cannot be deleted before traversing
ages zero, one, two, and three.  Hence every cyclic positive owner run has
length at least four.

Moreover

\[
 C_0\cup C_1\cup C_2=T-C_3=T-\{\alpha\}=T\cap T'.
\]

Thus rank-eight suffix coverage is literally the lower-q1 Johnson rainbow.

### Voltage lift

A single quotient cycle with nonzero total voltage modulo 17 lifts to one
cycle on all `17*1430=24310` owners.  Primality makes nonzero equivalent to
coprime voltage.

### `W+3` linearization

The periodic source word has one letter per owner orbit lift and satisfies
`D^3 A=T`.  Cutting one period and retaining the three wrap letters gives
length `W+3=24313`.  All width-at-most-three source suffix cells survive,
and every nonwrapping interval of four or more source letters rewrites as a
nonwrapping consecutive-owner union.

Exact quotient coverage at ranks two through eight lifts to all physical
targets because these target actions are free.  The 436 rank-one slots
need not be distinct: any one singleton orbit representative lifts to all
17 singleton targets.

## 2. Essential upper-opening qualification

Cyclic upper target-orbit coverage is not sufficient.  A target may have
only witnesses crossing the chosen physical cut, and its rotated copies do
not all become nonwrapping witnesses in the same linearization.

The corrected item 8 requires one chosen physical opening such that, after
discarding every cyclic owner interval crossing the cut, the remaining
linear owner intervals still cover all ranks ten through seventeen.  With
that condition Theorem 5.1 is sound.  Without it the theorem would be
false as stated.

## 3. One harmless overconstraint

The exact 16 directed type-transition multiplicities from the fractional
certificate are sufficient but not necessary.  Exact node-type masses and
literal changing-owner compatibility on a selected quotient cycle already
induce a balanced type circulation.  The search model may therefore omit
the 16 arc quotas without weakening the final implication.

## 4. Fixed published MMM cycle does not work

The unit-voltage published MMM quotient cycle is owner- and lower-rainbow,
but its physical owner chronology has minimum coordinate-run length two,
including 5,695 length-two and 1,598 length-three runs.  It cannot support
a depth-three age decoration.

The independent H100 `-O3` replay is

```text
scratch/audit_k17_mmm_cycle_depth3_age_nogo_20260801.cpp
```

and reports

```text
PASS_K17_MMM_CYCLE_DEPTH3_AGE_NOGO
voltage=1 owners=24310 min_run=2 length2=5695 length3=1598
```

Thus the owner cycle and age flags must be selected jointly.

## 5. Exact lower/owner search skeleton

The factorized generator

```text
scratch/build_k17_catalan_orbit_age_lower_skeleton_20260801.cpp
```

encodes one quotient Johnson cycle cover, exact age-type masses, literal
age partitions and survivor transitions, and exact suffix-orbit rainbows
at ranks two through eight.  Its H100 materialization has

```text
5,068,292 variables
25,215,929 clauses
102,944 directed non-self quotient arcs
836,550 suffix-choice variables
```

Connectivity and voltage are intended as lazy decoded cuts.  Strict-upper
coverage and the upper-safe opening are explicitly omitted.  Consequently
SAT of this skeleton is only a lower/owner milestone, never a `k=17`
universal-word certificate.
