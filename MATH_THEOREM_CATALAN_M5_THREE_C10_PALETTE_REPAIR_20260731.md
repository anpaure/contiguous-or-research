# A three-`C10` palette repair gives a leaf-peelable decorated `ML(9)` cycle

Date: 2026-07-31  
Status: exact explicit `m=5` positive base; preliminary nonstandard palette
repair plus one audited decoration and physical closure; no all-`m` induction

## 0. Verdict

The global palette failure of the unmodified standard `m=5` Merino--Mička--
Mütze gluing family is repairable.  Starting with its palette-transparent
`g0,g1` Hamilton cycle in `ML(9)`, toggle the following three pairwise
vertex-disjoint alternating ten-cycles, in the displayed order:

```text
C1 = 15 47 45 109 105 361 329 333 269 271
C2 = 298 314 306 310 308 436 420 428 424 426
C3 = 149 157 153 155 154 218 210 214 212 213
```

Every intermediate two-factor is one Hamilton cycle.  The missing turn
palettes evolve exactly as

```text
                 lower                         upper
base       {73,146,292}                 {219,365,438}
after C1      {146,292}                     {219,438}
after C2          {146}                         {219}
after C3              {}                            {}
```

The final cycle has a perfect `210/210` augmented matching.  The resulting
alternating turn representatives have a **forest** gap graph and a literal
`0^4` trace breaker.  Their physical diamond lift is a spanning `42`-path
forest in `J(10,5)`.  An explicit set of `42` Johnson connectors closes it
to one Hamilton cycle, with both connector-colour lists injective.

Thus the strongest standard-family obstruction at item 2172 is not an
`m=5` existence obstruction.  It is exactly a need for a preliminary
nonstandard palette repair.

This is a new finite positive base.  It does **not** prove that the three
switches arise recursively in every dimension, that the displayed trace
breaker is protected from an unspecified future collar catalogue, or that
the physical closure has a nontrivial quotient voltage.

## 1. The repair is monotone and private at the colour-bank level

For each switch, precisely three lower and three upper turn multiplicities
decrease by one, and precisely three on each shore increase by one.  No
previously present colour disappears.  The exact signed banks are:

```text
        lower -                     lower +
C1      13,104,321                  73,97,268
C2      52,266,416                  50,292,392
C3      26,133,208                  25,146,196

        upper -                     upper +
C1      125,303,489                 175,365,377
C2      318,427,500                 315,438,492
C3      159,250,469                 219,246,413
```

The six-colour banks are disjoint between the three switches, separately on
both shores.  Each switch inserts exactly one missing lower colour and one
missing upper colour.  In this literal sense the repair catalogue is private
and support-monotone; it does not rely on a cancellation between switches.

The final lower multiplicity profile is

\[
                         1^{43}2^{40}3^1,
\]

and the upper profile is

\[
                         1^{44}2^{38}3^2.
\]

## 2. Exact alternating-SDR certificate

Write the final Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{125},B_{125},A_0,
\]

and put

\[
 \ell_i=A_i\cap A_{i+1},\qquad u_i=B_{i-1}\cup B_i.
\]

Use the augmented bipartite graph whose left shore is the disjoint union of
the `126` occurrences `A_i` and the `84` lower colours, and whose right
shore is the disjoint union of the `126` occurrences `B_j` and the `84`
upper colours.  Its edges are

\[
 A_iB_{i-1},\quad A_iB_i,\quad A_i u_i,\quad \ell_jB_j.
\]

The final graph has a perfect matching of size `210`.  Reading its turn
edges gives index sets `I,J`, each of size `84`, such that

* `i -> u_i` is a bijection on `I`;
* `j -> ell_j` is a bijection on `J`; and
* selected `A`- and `B`-positions alternate around the cycle.

This is exactly the alternating-turn-SDR/gap-Hall criterion, rather than two
separate palette surjections.

Relative to the original deficient standard cycle, the old/final augmented
graphs have `459` common edges and `45` edges on each side of their symmetric
difference.  A maximum matching of the common graph has size `196`, hence
common deficiency `14`.  Its symmetric difference with the displayed final
perfect matching has fourteen augmenting paths, of lengths

```text
3 3 3 3 3 3 3 3 3 3 3 3 5 7
```

and three harmless alternating cycles.  This is the exact common-core
augmenting-linkage certificate for the compound repair.

## 3. The decoration is already leaf-peelable

For the fixed upper transversal `I`, form the occurrence-labelled gap graph:
one left vertex for each cyclic gap between successive selected `A`-
positions, one right vertex for each lower colour, and an edge when that
colour occurs in the gap.  It has `168` vertices and `107` edges.  Its
component profile is

```text
42 copies of (2 vertices, 1 edge)
16 copies of (4 vertices, 3 edges)
 2 copies of (6 vertices, 5 edges)
 1 copy  of (8 vertices, 7 edges).
```

Every component is a tree.  The selected `B`-occurrences give its unique
perfect matching.  Therefore the decoration is leaf-peelable, not merely
Hall-feasible.

The binary mark trace has forty-one zero-runs: forty of length two and one
of length four.  The length-four run occurs at physical trace positions
`140..143`.  Hence the diamond lift is a linear forest and the final cycle
carries a literal protected-face breaker.  The word *protected* here is only
literal: no future collar family has yet been declared disjoint from those
four positions.

## 4. Exact physical closure

The decorated diamond lift has all `252` rank-five subsets of `[10]` as
vertices, `210` edges, and exactly `42=Cat_5` path components.  Its path
length multiset is

```text
26,19,17,16,12,11,10,9,8,7,7,6,6,6,
5,5,5,5,5,5,5,4,4,4,4,
3,3,3,3,3,3,3,3,3,
2,2,2,2,2,2,1,1.
```

The audit records a literal set of forty-two connector edges.  They use
every formal path endpoint exactly once, avoid the forest, and close the
forest to one Hamilton cycle.  Their forty-two intersection colours are
distinct and their forty-two union colours are distinct.  Consequently the
closed physical cycle has outer-colour profiles

\[
                         1^{168}2^{42}
\]

on both shores.

Cutting this component cycle once and taking the right-comb binary
refinement gives a tree-contiguous socket schedule.  Every internal connector
is literal and node-private because the connector edges and both connector
colour lists are injective.  This is an `h=1` occurrence closure; it carries
no assertion about a nontrivial group voltage.

## 5. Search census and reproducibility

The primary exact catalogue enumerated:

* all `181` simple alternating `C8` switches, of which `41` are Hamilton-
  safe;
* all `1,592` simple alternating `C10` switches, of which `654` are
  Hamilton-safe;
* no palette-perfect single switch;
* a scoped `281`-switch common-exterior pool, producing `22,832` Hamilton-
  safe two-switch outputs and `182` states with exactly one missing colour
  on each shore; and
* every `C6/C8/C10` third switch from those `182` states.

Only third `C10` switches close both palettes.  There are `585` palette-
perfect Hamilton outputs in that census; `452` have augmented deficiency
zero.  The first one is the explicit certificate above.

Run

```text
python3 scratch/search_catalan_m5_long_switch_repair_20260731.py
python3 scratch/audit_catalan_m5_long_switch_census_independent_20260731.py
python3 scratch/audit_catalan_m5_three_c10_palette_repair_20260731.py
```

The first script produces the switch census.  The second independently
reimplements and reproduces all `585/452` census counts without importing the
primary search.  The third is a dependency-free literal replay of the
displayed witness, its matching/linkage, gap forest, trace, physical forest
and connector closure.

## 6. Certificate-separation warning

The three `C10` switches displayed here differ from those in
`MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`.
This note proves leaf-peelability and explicit colour-injective physical
closure for one repaired witness; the companion note proves preservation
over the full two-standard-hexagon cube and its private attachment paths for
another.  No present audit proves that one m=5 witness simultaneously has
both packages.  The two existential results must not be silently conjoined
in the recursive state.

## 7. Exact scope

This theorem supplies:

1. a palette-repaired `m=5` middle-levels Hamilton cycle;
2. one exact leaf-peelable Catalan decoration;
3. one exact tree-contiguous, colour-injective physical closure.

It does not supply the missing all-`m` recursion.  In particular, the three
`C10` bank repairs are an explicit finite catalogue, not yet a uniform
period-three repair lemma, and the physical right-comb is not yet coupled to
future shadow, residence, compiler or voltage states.  It closes the finite
base which item 2172 left open; it does not close Regenerative Shadow--Braid
Existence.
