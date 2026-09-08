# Audit of Claude's two-rail quotient-skeleton results

Date: 2026-07-30

## Verified content

1. The K8 and K10 two-rail carriers are literal witnesses.  K10 compiles to
   the independently verified optimal 254-letter word.
2. `railanat.py` correctly recognizes those witnesses as two
   orbit-transversal Johnson paths joined by containment seams, with the
   stated q1 counts.
3. At `n=15`, a 429-vertex B-rail quotient path with 428 pairwise distinct
   edge-label orbits exists.  Independent replay of the printed path gives a
   428-edge/428-label matching.  An independently materialized A-rail path
   visits all 429 vertex orbits and covers all 335 required label orbits.
4. All thirty K10 skeletons sampled by `skelrate.sh` were subsequently passed
   to the exact rails-prescribed CNF and returned SAT-solver
   `UNSATISFIABLE`; there were no timeouts in that sample.
5. The odd-k undecorated spiral input is genuinely uniform.  Theorem 1 of
   Merino--Micka--Mutze gives, for every `n` and every shift coprime to
   `2n+1`, a block-rotational star-transposition ordering.  Deleting the star
   coordinate gives the corresponding middle-levels Hamilton cycle; projecting
   to one middle level gives an orbit-transversal Johnson carrier whose
   consecutive intersections enumerate the other middle level.  Thus the
   open odd-k obligation is the extra residence/shadow/compiler decoration,
   not existence of the strict voltage spiral itself.

## Important scope correction

`railpair2.py` does **not** generate a coherent "full exact width-2 ledger."
For a selected quotient arc it creates one Boolean for every possible
intersection/union label pair.  It enforces

```text
option -> selected_arc
selected_arc -> OR(options)
```

but never enforces at most one option for that arc.  Mutually incompatible
phase labels may therefore be asserted simultaneously to satisfy different
coverage rows.  The output is a phase-relaxed support-cover skeleton; only
the later rails-prescribed CNF decides whether one coherent phase choice per
class realizes it.

This does not invalidate the thirty exact CNF rejections.  It invalidates the
interpretation that those thirty skeletons were sampled from the exact
width-2 solution space.  In particular, `0/30` is evidence that this relaxed,
biased generator is ineffective; it is not a measure-zero theorem and does
not estimate the density of genuine two-rail carriers.

The separate `rbexact.py` rainbow-path existence result is not affected by
this particular issue: every selected path edge is forced to choose at least
one label, and every label is globally at-most-one.  Choosing one asserted
label from each of the 428 selected edges therefore gives distinct labels.
The path still supplies only one marginal rail, not the coupled K16 carrier.

## Current consequence

The two-rail normal form remains a useful exact restricted architecture, but
the hard object is joint chronology/phase/history selection.  Fixed marginal
rails followed by gauge search and relaxed skeleton generation followed by
gauge search have both failed empirically.  The sound successor is the joint
phase-free option/history model in
`MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md`.
No K16 SAT or UNSAT result follows from Claude's skeleton computations.

As of the 2026-07-30 audit, the full Waksman, two-rail Waksman, and
multicomponent K16 solver outputs were still empty while their solver
processes were live.  They are ongoing searches, not positive or negative
certificates.

## Audit of the later `railpair3.py` voltage model

The voltage-aware successor has the same coherence defect in a more serious
form.  For every selected quotient arc it introduces several Boolean variants
indexed by the relative phase `delta` and enforces only

```text
variant -> selected_arc
selected_arc -> OR(variants).
```

There is no at-most-one row on those variants.  The same omission occurs for
the admissible seam-delta variables.  Consequently one selected arc may
simultaneously assert several incompatible phases, contribute several labels
to q1/upper coverage, and contribute the sum of several deltas to the voltage
equation.  Therefore the reported `q1-only SAT` instances from `railpair3.py`
are solutions of a phase-relaxed model, not coherent voltage skeletons.  They
do not establish the claimed diagnosis that adding the voltage telescope
alone repairs `railpair2.py`.

This has no effect on the K8/K10 literal carriers or on exact downstream CNF
rejections.  It does mean that any future use of `railpair3.py` must replace
both `BoolOr` implications by exactly-one channeling before its positive
outputs carry mathematical meaning.

## Audit of the kernel and duplicate-witness ideas

The underlying idea is useful: if every vulnerable upper target has two
physically edge-disjoint witnesses, an opening cut cannot destroy its final
witness.  That is a plausible concrete interface to the protected-reservoir
and PPR theorems.

The current evidence does not yet prove that interface:

1. `kernelcount.py` explicitly calls itself an approximation.  It closes a
   linear carrier with an artificial wrap edge, represents a cyclic interval
   by the unreduced Python set `range(i,j)`, and uses greedy linear interval
   scheduling for a circular edge-disjointness problem.  Its kernel sums,
   safe-cut densities, and disjoint-witness histograms are therefore
   diagnostics, not theorem-grade counts.
2. `codd.py --dup2` asks for one quotient witness in each of two class-index
   halves.  This is a strong sufficient search condition in the widths it
   actually emits, but the width list is the fixed finite tuple
   `(2,3,4,6,9,13)`.  The implementation does not itself prove arbitrary-
   width upper coverage, physical edge-disjointness after the full lift, or
   the lower compiler/PPR conditions.
3. No `--dup2` SAT witness or UNSAT certificate is currently present.  The
   live `co13` instance was emitted with `dup2=False`.

Thus duplicate witnesses are a worthwhile construction target, but the
current scripts supply neither a K16 carrier nor an all-k theorem.  The next
sound step is a physical two-witness lemma followed by an exact circular
kernel audit, not promotion of the present census numbers.
