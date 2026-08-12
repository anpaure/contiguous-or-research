# K17 J7: corrected all-q1 run9 scope, literal two-interface collar, and fixed-cycle splice gate

Date: 2026-08-01  
Lane: H2 independent authentication / protected physical J7  
Status: **local collar GO; corrected capped run9 UNKNOWN; fixed MMM
changed-support at most nine NO-GO.  No unrestricted K17 conclusion.**

## 0. Exact verdict

The native fusion

\[
  30844\longrightarrow26750\longrightarrow27246                 \tag{0.1}
\]

is a genuine protected J7 column.  Its two lower colours are `26748,26734`
and its two upper colours are `30846,27262`.  It has a nonempty six-letter
depth-three source and no internal positive owner run below four.

There are three separate global statements.

1. The corrected run9 formula forces J6 and J7, deletes the two old
   occurrences of the new lower colours, retains complete rank-ten/q1 rows,
   and requires at least one target-28926 socket.  Its semantics pass an
   independent clause audit.  The one proof-producing Kissat run reached its
   resource cap without a SAT or UNSAT line.  Its verdict is exactly
   `UNKNOWN_RESOURCE_CAP_EXIT_137`; the retained DRAT file is only an
   incomplete, noncertifying prefix.
2. J7 does embed in the frozen 1430-type word as a literal *five-owner*
   two-interface collar of types

   \[
                    4\to3\to7\to0\to8.              \tag{0.2}
   \]

   Thus the local physical/type obstruction is closed positively.  What
   remains is one complementary rooted quotient path through the other 1425
   owner orbits, with the complementary palettes and nonzero total voltage.
3. In the one frozen MMM owner/lower-rainbow quotient cycle, no labelled
   successor exchange containing either orientation of J7 and changing at
   most nine tails preserves both owner and lower-q1 orbit bijections.  The
   first unclosed changed-support catalogue in that fixed host is ten.

Statements 2 and 3 do not conflict.  The first selects the whole
complementary path prospectively; the second modifies one already frozen
cycle while retaining its lower matching.

## 1. Literal J7 column and exact all-q1 replacement ledger

One six-cell realization of (0.1) is

```text
4096,80,10244,16424,26690,512.
```

Its three length-four OR windows are exactly (0.1), with certified age types
`3,7,0`, namely

\[
 (3,3,2,1),\quad(5,2,1,1),\quad(1,5,2,1).           \tag{1.1}
\]

The corresponding quotient owner representatives are
`7711,8077,13623`; the lower representatives are `6687,7053`, and the upper
representatives are `8079,13631`.  Each list is repetition-free.

In the SCD run9 carrier, extracting the three owners forces four cuts:

| cut | lost lower | lost upper |
|---|---:|---:|
| `2002:1` | `30780` | `30972` |
| `686:3` | `26718` | `26878` |
| `686:4` | `26686` | `27262` |
| `1965:1` | `27182` | `27502` |

The new upper `27262` repays the third row, and new upper `30846` repays the
J6 cut `634:6`.  Exact lower-q1 uniqueness additionally forces

| cut | removed old lower | exported upper |
|---|---:|---:|
| `693:3` | `26748` | `27900` |
| `1562:2` | `26734` | `26863` |

These are the unique old occurrences of the two new lower colours.  Omitting
these two guards was the defect in the deliberately superseded preliminary
run; its partial proof has no theorem status.

## 2. Corrected run9 formula and capped computation

The corrected builder is

```text
scratch/build_h2_k17_run9_j7_global_q1_master_20260801.cpp
SHA-256 438368b774d4eb5a83b1cfcfbcd14d4fc7ee29d3effb1aff52b60279b395c207
```

The base formula has `2,203,044` variables and `10,758,306` clauses.  J6
and J7 are the positive units `551076,551077`; all six J7 cuts are
conditional implications, and the two lower replacement implications are
variables `2187117,2191049`.  Target `28926` is one at-least-one clause over
512 socket rows, not an exactly-one constraint.  Of those rows, 466 survive
the direct owner/cut screen.

The independently reconstructed rank-ten semantics find:

* every expected q1 clause exactly once;
* no empty expected clause;
* both forced macros and all 51 expected conditional macro-cut clauses;
* zero macro-delivery, macro-residence, or lower-replacement mismatches; and
* direct surviving provider counts

  \[
  26863:22,\quad26878:8,\quad27502:18,\quad
  27900:32,\quad30972:12.                            \tag{2.1}
  \]

Adding the authenticated static, one-seam and multi-seam residence clauses
gives the exact eager formula

```text
p cnf 2203044 55238036
SHA-256 438c51a4e6b44af4de8ea8064435c00a2279c7b5c08bc141cab6af6331a1ae03
```

The unique proof run was capped at 1770 CPU seconds, 1800 wall seconds and
16 GiB.  It ended by signal 9 with exit 137 after 1736.81 user plus 33.14
system seconds, wall time `29:30.26`, and peak RSS 3,673,552 KiB.  There is
no SAT line, UNSAT line, model, DRAT-trim invocation, or core.  Therefore:

> **The corrected run9 face is UNKNOWN, not UNSAT.**

Terminal hashes are:

| artifact | SHA-256 |
|---|---|
| `kissat.out` | `c6b3ed0a1e07e97a917ee5409c10ac538247e8c6279868465ff49f70a661dfb5` |
| `kissat.err` | `6e93e3b4cadfca8c841c7980880455991f50e890903051afb15ebf6a8205449c` |
| incomplete `proof.drat` | `c4b27839e938cc27a25b5ce56f22df30c787bd6db16237960ce93c31ce35be2e` |
| `solve.exit` | `e3b9c2844b5a5c2677b3a2279db2ec8487491dd9a23d6b22fac153391b3bb63c` |

The `NOT_SAT` postprocessor sentinel means only “solver exit was not 10”; it
is not an UNSAT verdict.

## 3. Positive five-owner two-interface collar

The first six-cell realization above does not itself extend left to the
required type 4.  That is not a structural obstruction: the exact local
model finds the eight-cell realization

```text
200,4096,8316,24608,2116,26634,512,92226,
```

whose five consecutive owner windows are

```text
28924 -> 30844 -> 26750 -> 27246 -> 92750.
```

They occupy frozen type positions `19..23` with IDs `4,3,7,0,8`.  Their
owner-orbit representatives are

```text
7231,7711,8077,13623,20149,
```

their four lower-q1 representatives are

```text
3975,6687,7053,13607,
```

and their four upper-q1 representatives are

```text
7743,8079,13631,28341.
```

All three lists are repetition-free, every source letter is nonempty, all
four transitions are Johnson, and there is no internally bounded positive
owner run below four.  Independent literal replay gives endpoint partitions

\[
 P_L=(24608,92,4096,128),\qquad
 P_R=(92226,512,8,4),                                \tag{3.1}
\]

arc voltages `0,9,7,8`, and net collar voltage 7 modulo 17.

Deleting the four collar type arcs from the frozen Euler ledger leaves
exactly 1426 arcs, with imbalance one from type 8 to type 4.  Hence the
remaining physical condition is exact:

* a 1427-vertex quotient path starting at endpoint orbit `20149` in state
  `P_R`, using all 1425 outside owner orbits, and ending at the appropriate
  voltage-twisted copy of orbit `7231` in state `P_L`;
* lower palette equal to the complement of
  `{3975,6687,7053,13607}` and the corresponding rank-2 through rank-7
  suffix complements;
* complement voltage `v != 10 mod 17`, so `v+7` is nonzero; and
* retained upper witnesses, shared resources, upper-safe opening and
  compiler rows.

This is the precise two-interface/component-splice target.  It bypasses the
two refuted direct J6 attachments: full direct append repeats upper colour
`30846`, whereas endpoint fusion creates an internal bit-12 run of length
three.

## 4. Frozen MMM component-splice obstruction

For a fixed quotient successor `sigma`, let `S` be the changed tails.  New
heads must be a bijection onto `sigma(S)`, and new lower labels must equal
the old labels on `S`.  Every chosen arc `u->v` with lower label `l` forces

\[
                    \sigma^{-1}(v),\ \lambda^{-1}(l)\in S.        \tag{4.1}
\]

Same-successor rephasings are included.  Exhaustive closure in the frozen
MMM owner/lower-rainbow cycle finds:

| support | forward states | reverse states | solutions |
|---|---:|---:|---:|
| at most 7 | 179 | 3001 | 0 |
| exactly 8 | 2355 | 39895 | 0 |
| exactly 9 | 29569 | 516549 | 0 |

The support-eight family is empty before topology, voltage, residence or
upper-q1 filters; those downstream counts are vacuous, not individual
obstructions.  The smallest open fixed-cycle exchange support is ten.
Changing the owner cycle, reselecting the lower matching, or constructing
the complementary path in Section 3 lies outside this no-go.

## 5. Exact scope and artifacts

Primary fail-closed synthesis:

```text
scratch/audit_h2_k17_run9_j7_local_global_scope_20260801.py
scratch/h2_k17_run9_j7_local_global_scope_20260801.audit.json
```

Local collar replay:

```text
scratch/audit_h2_k17_j7_two_cut_collar_independent_20260801.py
scratch/h2_k17_j7_two_cut_collar_independent_20260801.audit.json
```

Fixed-cycle bounded splice:

```text
MATH_THEOREM_H2_K17_J7_UNIT_VOLTAGE_COMPONENT_SPLICE_SUPPORT8_GATE_20260801.md
MATH_THEOREM_H2_K17_J7_COMPONENT_SPLICE_SUPPORT8_NOGO_20260801.md
MATH_THEOREM_H2_K17_J7_COMPONENT_SPLICE_SUPPORT9_NOGO_20260801.md
scratch/audit_h2_k17_j7_unit_voltage_component_splice_20260801.py
scratch/h2_k17_j7_unit_voltage_component_splice_20260801.audit.json
scratch/audit_h2_k17_j7_component_splice_support8_20260801.py
scratch/h2_k17_j7_component_splice_support8_20260801.audit.json
scratch/audit_h2_k17_j7_component_splice_support9_20260801.py
scratch/h2_k17_j7_component_splice_support9_20260801.audit.json
```

The run9 model is capped (`cap512` sockets, `cap64` providers) and does not
include ranks at least eleven, a global component chronology, lower-shadow
compilation or common cap.  The collar theorem does not construct its
complementary quotient path.  The fixed-cycle no-go concerns one frozen MMM
owner/lower matching through support nine.  None of these statements proves
or refutes global K17 equality.
