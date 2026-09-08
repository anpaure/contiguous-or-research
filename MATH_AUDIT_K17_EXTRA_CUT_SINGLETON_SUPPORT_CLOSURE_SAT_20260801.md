# `k=17`: a prospective extra-cut support bank covers every singleton row

Date: 2026-08-01  
Status: exact SAT witness plus independent semantic replay for a deliberately
relaxed **prospective** support projection.  Unary supports are evaluated
against the fixed base bank and are not automatically persistent when their
counterpart base block is also split.  This is not yet a literal simultaneous
refinement, a colored endpoint matching, a resident chronology, or a
universal word.

## 1. Frozen base face

The base is the authenticated protected seven-component rank-nine factor
and its lexicographically first protected-avoiding minimum residence
transversal.  It has 3,807 cuts and 3,807 owner blocks.  After the relaxed
necessary two-block residence filter, the atomic endpoint atlas has

\[
  1,289\text{ zero deleted rank-eight colours},\qquad
  368\text{ zero outgoing blocks},\qquad
  368\text{ zero incoming blocks}.
\]

Thus the frozen base has 2,025 singleton support demands.

Every nonselected, nonprotected old factor gap lying inside a base block was
then considered as one additional cut.  There are 20,477 such cuts.  The
audit permits at most one additional cut in any one base block and rebuilds
the two resulting subblocks in both orientations.

The exact support census is

```text
BASE pieces=3807 atoms=13174 zero_colours=1289 zero_tail=368 zero_head=368
EXTRA candidates=20477 viable=20477 self_noninc_closed=17629
      closure_dead=2472 empty_primary_demands=110 max_primary_cover=22
JOINT pair_supports=3194008 pair_colour_incidences=3435988
      formerly_empty_pair_repaired=110 empty_joint_demands=0
      empty_joint_colours=0 closure_joint_dead=0
```

Here a unary support uses one extra cut.  A pair support uses the new endpoint
states exposed by two extra cuts in distinct base blocks.  The last line is
only a complete singleton census: different demands may still require
incompatible seams.

## 2. Exact positive support formula

Introduce one variable `x_g` for each extra cut and one auxiliary variable
`p_e` for each two-cut support.  The formula contains:

1. `p_e -> x_g and x_h` for the two cuts of that support;
2. one positive coverage clause for each of the 2,025 original singleton
   demands, using its unary and pair supports;
3. for every selected cut, a positive closure clause requiring a selected
   unary or pair provider for that cut's newly deleted rank-eight colour;
4. at most one selected extra cut in each old base block.

No effective cardinality bound was imposed.  The resulting DIMACS instance
has

\[
       3,214,485\text{ variables},\qquad
       6,477,933\text{ clauses}.
\]

Kissat returned SAT in about four process seconds.  Its model selects 3,805
extra cuts in 3,805 distinct base pieces and marks 110,763 pair-support
auxiliaries.

## 3. Independent semantic replay

The replay does not merely rescan the DIMACS clauses.  It independently
reads the candidate, unary-cover, two-cut-support, pair-colour, and closure
ledgers and checks:

* every selected cut is viable;
* no base piece receives two extra cuts;
* every selected pair support has both endpoint cuts selected and uses two
  different base pieces;
* all 2,025 original singleton demands are covered;
* every selected cut's newly deleted colour has a selected nonincumbent
  unary or two-cut provider.

This is a semantic replay of the **prospective ledger**.  A unary support can
join a new subblock to an intact state of another base block.  If the latter
block is also selected for splitting, that intact state disappears.  The
formula presently has no implication invalidating such a unary support.
Pair supports do require both of their cuts, but that does not repair this
unary-persistence gap.

It reports

```text
selected_cuts=3805 selected_pairs=110763 covered_demands=2025
selected_pieces=3805 pair_closed_only=463
PASS_K17_JOINT_EXTRA_CUT_SUPPORT_SAT_SEMANTIC_REPLAY
```

The 463 `pair_closed_only` cuts are a useful warning: pair supports are not
cosmetic; unary closure alone does not explain this witness.

## 4. What is proved

For this fixed base transversal there exists a partition-compatible set of
prospective extra cuts such that, in the union of the fixed-base unary atlas
and the two-cut atlas,

\[
 \boxed{\text{every original singleton row and every selected-cut closure
 row has a prospective support of size at most two}.}
\]

This removes a candidate-universe zero-row obstruction: none of the original
singleton demands or selected-cut colours is absent from all unary/two-cut
repair faces.  It does **not** yet remove the simultaneous-refinement
obstruction, because selected cuts can destroy unary provider states.

It also proves that the 1,289 zero-colour obstruction is not stable under
interior refinement, complementing the separate result that alternative
minimum transversals can reduce it without adding cuts.

## 5. What is not proved

The witness is intentionally dense and lives only in the prospective support
projection.  It does **not** certify that its unary supports survive the
simultaneous splits, nor choose one resource-disjoint seam for every block
and colour.
In particular it does not establish:

* the orientation-coupled functional Hall inequalities;
* a three-resource tail/head/colour perfect matching;
* one connected cycle or linear path;
* the exact product residence automaton after all seams are chosen;
* restoration of the rank-ten and deeper upper palettes;
* the terminal lower compiler;
* `nu(17)=24313`.

The immediate next exact finite gate is to rebuild the selected 7,612-block
refinement literally and recompute all supports.  A sound selection model
must either use only persistent pair supports or condition every unary
support on its counterpart block remaining intact (or on a replacement
subblock state).  Only after this persistence row closes should the refined
bank be fed into the head-colour master with min-cut separation, followed by
connectivity and the full residence/upper rows.

## 6. Artifacts and hashes

Remote retained root:

```text
/home/amodo/or15/work/root_k17_joint_extra_cut_support_sat_20260801
```

Key retained hashes:

```text
support.b20477.cnf
  bcbd29215eccdc14d6527ec5d7c483178dcbe3cbf32f69ac71d09a44e757c69b
kissat.out
  93d2c9e4c1ed96863c9dec7d076046c8faf8f8d51bcd345b9a9c59aa93b7f7be
scratch/verify_k17_joint_extra_cut_support_sat_20260801.cpp
  9db6c260c08e7b6784dcc61b167ad49f7ded9d5af32560f016d36f3c87fb173d
scratch/k17_joint_extra_cut_support_sat_20260801.verify.out
  fb9cd826300e90c325674177b8a39b8eb4b8a63bf8c5acc074bb866155314fbb
scratch/k17_joint_extra_cut_support_sat_20260801.selected_cuts.tsv
  805784da83833a537340e130e17d9cce32f61aa5e14efcd44e4c34d3829d10a5
```

## 7. Persistent pair-only support is still not the integrated gate

A stricter follow-up removed the unary-persistence caveat entirely.  It
restricted to individually self-closing cuts and required every one of the
2,025 primary demands, plus every new child endpoint row, to be supported by
a seam between two selected cuts.  A verified witness exists with 1,703 cuts.

However, literal rebuilding shows why this is not the construction target:

```text
refined_pieces=5510 cut_colours=5510
RELAXED zero_colours=0 zero_tail_pieces=0 zero_head_pieces=0
    match_piece_TH=5509 match_piece_TC=5504 match_piece_CH=5504
COMMON_ORIENTATION_ZERO relaxed=653
RANK10_ZERO relaxed=459
```

The pair-only witness is therefore a correct persistence-safe support theorem
but is globally inferior to the dense cut-choice incumbent.  Minimizing the
number of support cuts is not aligned with minimizing the actual integrated
carrier defect.

```text
scratch/k17_paironly1703_support_bank_20260801.tsv
  SHA-256 eb0c385a9b75e6e2713be3899e1104cd20339c46d14bcb4cee07f20a493e6dbb
scratch/k17_paironly1703_literal_refinement_20260801.audit.out
  SHA-256 e3e6d46113728feb45a715b0f5b81b671571911ffe26361a5fa07187486cdadc
```
