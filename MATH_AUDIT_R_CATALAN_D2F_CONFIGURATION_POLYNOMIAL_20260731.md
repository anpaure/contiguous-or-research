# Audit of the D2F configuration polynomial and accepting-root relation

Date: 2026-07-31  
Verdict: **PASS after one occurrence-fibre scope correction**; exact for a
fixed factor and component partition; no bounded-state, dimension-recursive,
or all-dimension existence theorem

## 1. Claims which pass

For each factor component `C`, the local polynomial `P_C` enumerates exactly
its forest-safe marked configurations and its two unmarked residual phases.
All coefficients are nonnegative.  Therefore

\[
 [\mathfrak m_*]\prod_C P_C>0
\]

if and only if one local configuration per component consumes every upper
and lower turn colour exactly once.  Squarefreeness prevents repeats; the
local trace filter excludes fully marked and exceptional partial components.
The corrected cycle-budget theorem then gives exactly `Cat_m` paths.

The consumed-colour relation composes by disjoint-union join.  This is
associative and is exactly squarefree monomial-support multiplication, so the
full-palette root is equivalent to a terminal accepting decoration on the
fixed factor.

The occurrence-labelled global gap graph is also exact.  A perfect matching
chooses one lower occurrence in every cyclic upper-transversal gap and every
lower colour once.  Components receiving no upper mark remain unmarked and
retain an independent two-phase choice.  The final `f=g=0` test remains
separate.

The component-balance network is exact for its stated projection: value `P`
is equivalent to assigning both palettes to occurring components with equal
shore counts.  It is only necessary because it forgets cyclic order and
trace topology.

## 2. Required scope correction

The colour-set relation cannot express transparent transfer between two
different factors.  Every factor relation contains `(empty,empty)`, and
every accepting root uses the same full-palette pair.  Thus the frozen
`ML(7)` number six is **not** an intersection size of these colour-set
relations.

The exact census meaning is:

* `31` alternating incidence hexagons;
* `16` Hamilton outputs;
* `10` of those Hamilton outputs have a nonempty terminal decoration fibre;
* `6` source/output pairs share at least one literal occurrence-labelled
  forest decoration.

The theorem has been corrected accordingly.  Its relation is exact for
terminal existence on one fixed component partition.  Common-decoration
transfer through a hex requires occurrence identities, phases, boundary
marks and, when relevant, ports; it is governed by the separate transparent
hex criterion.

The cited census does not classify the split outputs for the weaker D2F
target, so no Hamilton restriction is inferred from `31/16/10/6`.

## 3. Final scope

The direct D2F gate is the positivity of one all-colour coefficient for one
explicit factor family.  Summing the component polynomials over a finite
terminal factor family is exact for existential terminal choice, and
unrestricted alternating circuits remove dependence on the starting
2-factor.  None of this proves connectivity by ECO/bounded/protected moves.

The theorem settles no residence, deeper-shadow, RSB, seam, voltage or
compiler row.  It is a central Catalan Linear Matching reduction only.
