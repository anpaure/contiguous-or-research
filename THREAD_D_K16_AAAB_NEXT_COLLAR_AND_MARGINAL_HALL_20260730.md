# Thread D: K16 AAAB next-collar and marginal-Hall theorem

**Date:** 2026-07-30  
**Scope:** source-independent one-block K16 joint rail model; exact catalogue
and finite matching only.  No source carrier, edit radius, SAT inference, or
randomness is used.

## Theorem

Fix one of the four compressed branches

\[
  \operatorname{AAAB}_{380},\quad \operatorname{AAAB}_{384},\quad
  \operatorname{AAAB}_{395},\quad \operatorname{AAAB}_{406}.
\]

Write the forced terminal states as

\[
 X_0\longrightarrow X_1\longrightarrow X_2\longrightarrow X_3,
 \qquad \operatorname{shore}(X_0X_1X_2X_3)=AAAB,
\]

where (X_1) is the named middle at A-position (427).  Then:

1. The shifted three-state intersection
   (X_1\cap X_2\cap X_3) is independent of the chosen one of the 640
   terminal fragments.  Its canonical q2 label is

   \[
   \begin{array}{c|c}
   \text{branch middle}&\text{forced shifted q2 label}\\ \hline
   380,395&4683\\
   384,406&4685.
   \end{array}
   \]

2. Exactly 35 B-to-B options can leave (X_3) without violating the
   depth-three insertion-history condition.  For every terminal fragment,
   these 35 options split into five classes of seven according to the next
   four-state intersection (X_1\cap X_2\cap X_3\cap X_4):

   \[
   \begin{array}{c|c}
   \text{branch middle}&\text{five possible q3 labels}\\ \hline
   380,395&587,601,713,1609,2341\\
   384,406&589,617,841,1171,2633.
   \end{array}
   \]

   The five cases are therefore an exact disjoint and exhaustive refinement
   of each AAAB branch.  None repeats the installed q3 label 4681.

3. The AB seam and every one of the 35 legal first B edges have different
   lower tight-q1 colours.  Thus this collar does not consume the unique
   repeat token of the `rank(R-1)` palette.

4. Among the 640 terminal fragments, 150 consume the unique repeat token of
   the `top+rank(R)` palette.  Conditional on any such fragment, the other
   427 occurrences must be a bijection onto the other 427 colours.  Every
   one of these 150 conditional incidence systems passes both exact marginal
   Hall tests:

   \[
     \nu(\text{colour--source})=
     \nu(\text{colour--target})=427.
   \]

   The minimum colour degree is 6 or 7 on the source side and 5 or 6 on the
   target side.  After also deleting forced-degree, terminal-colour, and
   immediate-history conflicts, every uncovered q1 row retains at least 18
   option providers; every unforced node retains at least 35 outgoing and
   at least 34 incoming options.  Hence no one-level colour--source,
   colour--target, row-support, or node-support Hall cut closes any of the
   four branches.

The surviving obstruction is genuinely joint: a residual edge must realize
its source, target, colour, rail order, and three-step history
simultaneously.  Passing both marginal Hall projections does not assert that
this three-index system has an integral transversal.

## Proof of the collar partition

The terminal-position theorem gives one of the 80 q2 prefixes and places its
second state at A-position 427.  Its next state is the A endpoint at position
428, whose outgoing edge is necessarily the unique AB seam.  Direct
substitution in the exact quotient representatives gives the shifted q2
labels in the table; they are constant over all 80 prefixes and all eight
seams per prefix.

At (X_3), the three most recent inserted old coordinates are distinct.
The next B state has eight old coordinates.  Positive depth-three residence
forbids deleting precisely those three recent coordinates, leaving five
possible deletions.  After a deletion there are seven possible insertions,
so there are exactly (5\cdot7=35) legal options.  The intersection
(X_1\cap X_2\cap X_3\cap X_4) depends on the deleted coordinate but not on
the newly inserted coordinate.  Thus each deletion class has seven members.
Canonicalizing the five intersections gives the two five-label rows above.
The finite audit checks this identity separately for all (4\cdot640)
terminal fragments.

More explicitly, the selected outgoing B option has one deleted coordinate,
so it belongs to exactly one of the five deletion classes.  Its four-state
intersection has one canonical label, and the five displayed labels are
distinct.  Hence no selected option belongs to two cases (pairwise
disjointness), while the (5\cdot7=35) classes contain every
residence-compatible outgoing option (exhaustiveness).  This is a partition
of the **specific first post-seam window**, not a partition of all q3
providers elsewhere in the chronology.

## Exact q1 current and the failed local obstruction

The `top+rank(R)` palette has 429 colours and exactly 430 selected
occurrences: 428 internal A edges and the two cross edges.  Coverage implies
exactly one duplicated colour.  If a terminal fragment has two distinct
upper colours among its three edges, its repeated colour consumes that
token.  The remaining 427 occurrences are consequently an exact rainbow on
the other 427 colours.

For a zero-slack fragment (F), let (C_F) be the 427 upper-q1 colours not
used by (F).  Delete all option literals ruled out by the three forced
edges, the unique-AB constraint, the two terminal colours, and the immediate
depth-three history tests.  Define two bipartite graphs:

* (G_S(F)) has left side (C_F) and right side the 426 residual A sources
  together with one abstract slot `BA`; (c\sim s) when an undeleted AA
  option of colour (c) leaves source (s), or an undeleted BA option of
  colour (c) exists when (s=\mathrm{BA});
* (G_T(F)) has left side (C_F) and right side the 427 residual A targets;
  (c\sim t) when an undeleted AA or BA option of colour (c) enters (t).

These are necessary marginal Hall systems for the residual rainbow.  Exact
Hopcroft--Karp gives

\[
  \nu(G_S(F))=\nu(G_T(F))=427
\]

for all 600 instances (150 in each branch).  Their exact support census is:

| conditional statistic | count among the 150 fragments in each branch |
|---|---:|
| blocked providers of the two terminal upper colours: 139 | 50 |
| blocked providers of the two terminal upper colours: 141 | 100 |
| minimum source-colour degree 6 / 7 | 60 / 90 |
| minimum target-colour degree 5 / 6 | 30 / 120 |
| immediate predecessor choices 34 / 36 / 39 / 41 / 42 | 10 / 10 / 10 / 30 / 90 |
| minimum residual node out-degree | 35 in all 150 |
| minimum residual node in-degree 34 / 36 / 39 / 41 / 42 | 10 / 10 / 10 / 30 / 90 |
| minimum provider support over every uncovered q1 row | 18 in all 150 |

This is a positive slack certificate for the two marginals, not a relaxation
or feasibility proof for the original three-index edge system.

## Candidate exact encoding

The five-way refinement is much smaller than a new arbitrary q3 path DNF.
Reuse the existing exact q2-prefix variable

\[
  p_{ef}\leftrightarrow(x_e\wedge x_f).
\]

For a fixed next-q3 label \(\lambda\), each of the 80 prefixes and each of
its eight AB seams (s) has an audited seven-option set
\(G_{ef,s,\lambda}\) at the first B vertex.  Add

\[
  \neg p_{ef}\ \vee\ \neg x_s\ \vee\
  \bigvee_{g\in G_{ef,s,\lambda}}x_g.
\]

This is 640 clauses of length nine and no new variables per refined case.
Exact outgoing degree and the history constraints make the implication an
iff for the selected prefix and seam.  Running the five labels separately
is a disjoint exhaustive subportfolio; an UNSAT claim for the parent branch
requires all five completed proofs.

The quantifier here matters.  For one chosen subcase \(\lambda\), install its
640 conditional clauses.  The five 640-clause systems are alternatives and
must **not** be conjoined.  Nor does the theorem justify constraining any
other q3 window to these labels.  A stronger chronology-wide q3 cut, a
source--target--colour matching cut, or an ordering cut would require a new
proof and is not claimed by this audit.

For reproducible implementation, the audit JSON records, for every
branch/label pair, a SHA-256 digest of the 640 semantic rows
`(first option, second option, seam option, seven first-B options)`.  Thus an
encoder can regenerate the clauses from the frozen catalogue and compare the
literal family before launching a solve without storing a second large path
atlas.

For q1 propagation, the global redundant option
`--tight-q1-at-most-two` is preferable to terminal-specific clauses.  It
introduces the exact duplicated-colour selector for each of the two
one-spare palettes.  A zero-slack terminal fragment then forces its duplicate
selector and makes every other upper-q1 row at-most-one.  This exposes the
outside-rainbow theorem globally.  The current four-branch portfolio command
did not enable that already-implemented exact strengthening.

## Reproducibility

- Audit source:
  `scratch/audit_threadD_k16_aaab_next_collar_hall_20260730.py`
- Audit payload:
  `scratch/threadD_k16_aaab_next_collar_hall_20260730.audit.json`
- Stable payload SHA-256:
  `53223ff5012658351730d396b4969ca8ca007d861010f843d7d591c31ce09e57`

The audit uses only the Python standard library and the frozen exact
catalogue constructors.  It finishes in under ten seconds on the local
audit machine and invokes no solver.
