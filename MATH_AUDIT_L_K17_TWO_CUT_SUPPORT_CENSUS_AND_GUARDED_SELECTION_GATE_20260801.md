# Audit: the k=17 two-cut census is a complete local superatlas, not yet a selected support bank

Date: 2026-08-01  
Scope: the fixed seven-component factor
`scratch/k17_reset_twin_ferrers_bank_ml9_factor_20260801.tsv`, the
rightmost-greedy protected-avoiding 3,807-cut decomposition, and at most one
additional cut in each of its old blocks.  Residence means the deliberately
relaxed necessary two-block predicate from the contracted-endpoint audit.
Nothing here asserts a final matching, topology, upper deck, or compiler.

## 1. What the new census proves

The independently inspected source
`scratch/audit_k17_h2_extra_cut_zero_colour_closure_20260801.cpp` reproduces
the old ledger

```
base blocks                         3807
base relaxed atoms                13174
zero base lower colours            1289
zero outgoing old blocks            368
zero incoming old blocks            368
```

and exhausts all 20,477 legal nonprotected interior gaps.  With exactly one
such gap cut and every other old block left intact, all 20,477 cuts have
locally supported left/right fragments.  There are 17,629 cuts whose newly
deleted colour has a nonincumbent provider in that one-cut universe.  Unary
supports leave 110 of the 2,025 old zero demands empty.  Exhausting seams
between fragments exposed by two cuts gives 3,194,008 cut-pair rows and
3,435,988 pair--colour incidences; all 110 unary-empty demands then have a
pair witness.  Likewise every new cut colour has some unary or pair provider.

These are exact **local-superatlas** statements.  In particular, they prove
that the old 1,289/368 atomic obstruction is not stable under arbitrary
two-cut fragment exposure.  They do not prove that one set of extra cuts
simultaneously retains the advertised witnesses.

## 2. First lost guard: a unary witness assumes its other block is intact

For a candidate cut `g`, source lines 252--268 join each new fragment state
to `base_states[hs]` or `base_states[ts]`.  A recorded unary witness therefore
has the literal dependency

```
g is selected AND the old neighbour block q is not split.
```

The exported `cover.tsv` forgets `q` and the selection CNFs replace this
conjunction by the single positive literal `x_g`.  If a selected cut in `q`
shortens the relevant prefix/suffix, or destroys the old all-one state, the
advertised unary seam need not exist.  The same problem affects the
`self_closed` column and `closure.tsv`: a one-cut nonincumbent provider is not
monotone under further splitting of its old neighbour.

The pair rows do not have this particular defect.  Under the imposed
at-most-one-cut-per-old-block rule, both exposed fragment states survive when
their two cuts are selected.  However, a row aggregates all directions,
orientations and colours for the cut pair.  It is therefore sound only as a
union of independent support statements.  It is not one seam and cannot be
used as simultaneous matching capacity.

All 20,477 candidates happen to be `viable` in this instance, so reading
column 12 (`self_closed`) rather than column 8 (`viable`) does not change this
particular population.  It is nevertheless not the stated predicate and is
not a valid generic parser convention.

## 3. Second lost guard: a legal seam colour must itself have been cut

Let `D_0` be the 3,807 lower colours deleted by the base decomposition.  If
an endpoint seam has lower colour `l` not in `D_0`, the old factor edge of
colour `l` remains internal unless the unique extra gap of colour `l` is also
selected.  Using that seam without this extra cut duplicates a lower-q1
colour.  Thus every seam witness also has the guard

```
l in D_0 OR x_(the unique extra gap of colour l).
```

The census applies this implicitly when asking for a named old zero colour or
the closure of a selected cut, but not when it credits an incoming/outgoing
block demand.  Consequently the reported block support degrees are
projections, even before matching or orientation consistency is imposed.

## 4. Third lost guard: selecting cuts changes the demand set

The 2,025 rows comprise only deficits of the unsplit base decomposition.
After selecting a bank, a formerly live unsplit block can lose all of its old
neighbours, while every selected cut replaces one old block by two new
fragments.  A sound selected-bank statement must cover:

1. every surviving unsplit block's incoming and outgoing support;
2. both new fragments' incoming and outgoing support for every selected cut;
3. all 3,807 base deleted colours, except the one linear-opening colour;
4. every selected extra-cut colour, again subject to the same single global
   opening waiver.

Covering only the old zero rows and declaring the split old block repaired by
one-cut `viability` omits these conditional obligations.

## 5. The smallest sound support-selection master

Let `C(p)` be the candidate cuts in old block `p`.  Use cut variables `x_c`
with

```
sum_(c in C(p)) x_c <= 1,
u_p = 1 - sum_(c in C(p)) x_c.
```

The active blocks are the unsplit block `p` with activity `u_p`, and the two
fragments `c^-`,`c^+` with activity `x_c`.  The active lower colours have
activities

```
q_l = 1       for l in D_0,
q_(l_c) = x_c for an extra-cut colour l_c.
```

Enumerate occurrence-labelled directed seam atoms

```
a = (tail block, tail orientation, head block, head orientation, lower colour)
```

which are Johnson, nonincumbent when used to close their own deleted edge,
and pass the necessary relaxed residence predicate.  Give each atom a
support-certificate variable `y_a`.  Its exact activation rows are

```
y_a <= activity(tail block),
y_a <= activity(head block),
y_a <= q_(colour(a)).
```

If one physical orientation is required already at the support stage, add
`r_(b,0)+r_(b,1)=activity(b)` and the corresponding two inequalities
`y_a<=r_(tail,orientation(a))`, `y_a<=r_(head,orientation(a))`.  Omitting
these `r` variables gives only an orientation-free necessary projection.

With at most one global missing join colour, introduce waiver variables
`w_l` and endpoint waivers `e_b^in,e_b^out`.  The exact support rows are

```
sum_(a: tail(a)=b) y_a + e_b^out >= activity(b),
sum_(a: head(a)=b) y_a + e_b^in  >= activity(b),
sum_(a: colour(a)=l) y_a + w_l  >= q_l,
sum_l w_l <= 1,
sum_b e_b^in <= 1,
sum_b e_b^out <= 1,
w_l <= q_l,  e_b^in,e_b^out <= activity(b).
```

This is an exact 0--1 support model for the stated one-extra-cut-per-old-block
face.  It is naturally sparse in dependency arity: an atom touches two block
activities and one colour activity.  It is not ordinary set cover because
unsplit-block activities are antitone in the cut choices.  Equivalently it
is a mixed-sign, occurrence-labelled three-guard cover.

The next, strictly stronger, matching/topology master must select actual seam
atoms with one outgoing and one incoming seam per nonendpoint block, one use
per active lower colour, shared block orientations, and subtour/connectedness
rows.  Pair-aggregated auxiliaries are insufficient for that level.

## 6. Consequence for current finite outputs

Any 700-cut (or other) solution obtained from the present `cover.tsv` and
`pair_cover.tsv` proves only coverage in the projected one-/two-cut
superatlas.  Before it can be cited as a simultaneous support bank it must be
replayed by rebuilding the final partition and the full occurrence-labelled
atom set, then checking the guarded rows above.  Only after that support pass
is it meaningful to run Hall/matching, upper-ticket, topology, or fresh
compiler gates.

The current auxiliary programs do not perform that replay.
`solve_k17_h2_extra_cut_joint_bank_20260801.cpp` treats column 12
(`self_closed`) as its entire admissibility predicate, assumes those closure
witnesses persist, and scores the union of precomputed unary/pair rows.
`build_k17_h2_selfclosed_joint_bank_cnf_20260801.cpp` likewise has no
selection-dependent unary guards or new-fragment rows.  The file named
`verify_k17_joint_extra_cut_support_sat_20260801.cpp` checks the exported TSV
relations, not the reconstructed selected partition.  Moreover its assumed
pair-variable address `max_cut_var+1+pair_id` matches the original all-viable
inline CNF layout, but not the compact pair numbering and initial constant
variable used by the separate self-closed builder.  It therefore cannot
serve as an independent verifier for that builder without an explicit pair
variable map.

Thus the exact current conclusion is positive but scoped: two-cut exposure
removes every *individual* old zero row and every individual new-colour
closure row.  Simultaneous selection remains open, and its smallest sound
model is the guarded occurrence-labelled support master above.
