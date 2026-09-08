# Thread D: K16 AAAB terminal-position and q1 Hall audit

**Date:** 2026-07-30  
**Scope:** source-independent one-block K16 joint rail model; no source carrier,
edit radius, seam-repair assumption, or SAT inference.

## Result

For each of the four smallest subgroup cases

\[
  \mathrm{AAAB}_{380},\quad \mathrm{AAAB}_{384},\quad
  \mathrm{AAAB}_{395},\quad \mathrm{AAAB}_{406},
\]

the exact q3 provider row has a much smaller equivalent formulation.  Let
`pos_A` be the exact binary rail position and let \(M=429\).  Then

\[
 \boxed{
  \text{AAAB q3 witness with middle }m
  \iff
  \bigl(\text{one of the 80 q2 prefixes through }m\bigr)
  \land \bigl(\operatorname{pos}_A(m)=M-2=427\bigr).
 }
\]

Consequently:

1. the q3 condition already implies the singular q2 condition;
2. the 640-path q3 DNF and the redundant subgroup witness can be removed;
3. all earlier-AAAB disjointification clauses are redundant;
4. each branch uses 80 prefix variables and 250 clauses before q1
   strengthening, instead of 160 variables and 1045 clauses, plus the old
   disjointification clauses;
5. an exact tight-palette cut deletes 10 of the 640 terminal fragments;
6. the 150 fragments with repeat excess one now induce 11,220 exact
   conditional saturation clauses after filtering 9,830 direct degree/order
   consequences; and
7. the first-B/second-B collar theorem adds 22,400 exact, propagation-
   redundant successor rows.  The full targeted branch package therefore
   has 80 prefix variables and 33,880 clauses: 241 prefix-DNF clauses plus
   33,639 branch-extra clauses.

This is an encoding theorem, not a feasibility theorem.  Each branch still
has 630 terminal fragments after the local q1 cut, so the audit does **not**
prove any branch UNSAT.

## Terminal-position theorem

Write

\[
 H=\{0,3,6,9,12\},\qquad
 T_2=H\cup\{15\},\qquad T_3=H.
\]

The audited labels are `T_2=37449` and `T_3=4681`.  An AAAB q3 provider is a
selected path

\[
 A_0\longrightarrow A_1\longrightarrow A_2\longrightarrow B_0
\]

whose four-state intersection is a rotation of \(T_3\).  The first three
states intersect in the corresponding rotation of \(T_2\); hence the first
two options are one of the exact q2 provider prefixes.  This proves q3
implies q2.

The binary-order formulation makes each shore one directed Hamilton path.
Its unique A-to-B option leaves A-position \(M-1\).  Therefore every AAAB
provider has

\[
  \operatorname{pos}_A(A_2)=M-1,qquad
  \operatorname{pos}_A(A_1)=M-2.
\]

Conversely, suppose an exact q2 prefix
\(A_0\to A_1\to A_2\) is selected and
\(\operatorname{pos}_A(A_1)=M-2\).  The second internal edge puts \(A_2\) at
position \(M-1\), so its selected outgoing option is the unique A-to-B seam.
Every such seam removes the distinguished top coordinate from the running
intersection.  Thus the resulting four-state intersection is the rotation
of \(T_3\).  This proves the reverse implication.

There can be only one selected AAAB witness middle: it is the unique node at
A-position \(M-2\).  Hence a positive AAAB branch at middle \(m\) already
excludes every earlier AAAB middle.  The old 0, 640, 1280, and 1920 path
clauses in the four canonical branches were logically redundant.  The six
non-AAAB pattern families retain their original canonical exclusions and are
unchanged.

## Exact factored encoding

For each of the four middles, the catalogue contains exactly 80 q2 prefixes.
Every prefix has exactly eight A-to-B extensions, so its q3 row contains
exactly 640 paths and its set of two-option prefixes is exactly the q2 set.

Use one exact AND variable for each two-option prefix:

\[
 p_{ef}\leftrightarrow (x_e\land x_f).
\]

This costs 240 equivalence clauses.  Add one clause
\(\bigvee p_{ef}\) and the nine unit clauses specifying binary position 427,
whose low-to-high bit pattern is `110101011`.  Total: 80 auxiliary variables
and 250 clauses.  The production solver now exposes the contiguous rail
position-variable range and installs this formulation only for disjoint
AAAB branches.

The exact local incidence is the same in all four cases:

- the middle has 62 possible incoming and 62 possible outgoing catalogue
  options before the branch;
- only 14 incoming and 14 outgoing options occur in a valid prefix, so 48
  options are eliminated on each side;
- the 80 prefixes use six predecessor nodes and six endpoint nodes;
- there are 30 predecessor/endpoint pairs, 20 occurring with multiplicity
  two and 10 with multiplicity four.

## Tight q1 Hall/current equation

Consider the `top+rank(R)` upper q1 palette.  It has exactly \(M=429\)
colours.  A one-block carrier has \(M-1=428\) internal A options and two
cross options, so it contributes exactly \(M+1=430\) occurrences to this
palette.  If every colour is covered and \(L_c\) is its occurrence count,
then

\[
 L_c\ge 1,qquad \sum_c L_c=430,qquad
 \sum_c(L_c-1)=1.
\]

Thus the complete palette has exactly one repeat token.  All three options
of an AAAB terminal fragment lie in this palette.  Its local repeat excess
is

\[
 \epsilon=3-\bigl|\{\ell(e_1),\ell(e_2),\ell(e_3)\}\bigr|,
\]

and necessarily \(\epsilon\le 1\).  Exact enumeration in every one of the
four branches gives

| local excess | terminal fragments | interpretation |
|---:|---:|---|
| 0 | 480 | one global repeat token remains |
| 1 | 150 | the terminal fragment consumes the only token |
| 2 | 10 | deficit one; exact no-good |

The 10 excess-two triples are installed as three-option no-goods.  This is a
consequence of q1 completeness and occurrence conservation, not a heuristic
collision score.  The 150 zero-slack fragments have also been resolved into
the exact conditional family: conditional on one of them, every other
selected `top+rank(R)` provider of either already-used colour is false.  The
deduplicated family has 11,220 clauses; 9,830 further instances are already
forced false by source degree, target degree, or the selected seam type.

The next structural layer is audited in
`THREAD_D_K16_AAAB_COLLAR_COLOUR_ORDER_FLOW_20260730.md`.  Its 22,400
successor clauses per branch couple the terminal prefix, seam, first B edge,
one-step history and order.  They are valid and installed, but are implied by
the base degree/history/order system.  More importantly, all 89,600 fixed
collars pass both marginal Hall projections and the full-uncovered
endpoint-coupled flow with one unit of slack.  This rules out a claimed local
Hall obstruction; proper colour subsets and genuinely multi-collar history
remain open.

## Reproducibility

- Solver-free audit source:
  `scratch/audit_threadD_k16_aaab_branch_hall_structure_20260730.py`
- Exact audit payload:
  `scratch/threadD_k16_aaab_branch_hall_structure_20260730.audit.json`
- Patched global solver:
  `scratch/solve_even_two_rail_joint_history_kissat_20260730.py`
- Lightweight regression:
  `scratch/test_threadD_k16_q23_disjoint_portfolio_20260730.py`

At the time of this note, the audit source SHA-256 is
`917c85daa860ccdef3394e874047ef7d2e7e4c3e270df75cf1dad45205c3e9d1`,
and the payload SHA-256 recorded inside it is
`d00f6c1675b0c993f1133b26ff877fe97326a4ced00450fa96902b2ec0cef1fe`.
The raw JSON also records a volatile wall-clock field, so its file hash is not
used as a stable identity.  The ten portfolio regressions pass locally in
under five seconds and invoke no solver.
