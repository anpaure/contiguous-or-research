# Exact global sparse-factor SAT for a fixed `k=11`, `q=369` row

## 1. Purpose and scope

The globally rainbow maximal-shadow branch is impossible by
`RAINBOW_PAIR_TRIPLE_OBSTRUCTION.md`.  The surviving compressed route keeps
only the fixed central row and its mixed `02|03` schedule, then searches every
factor bit globally.

This formulation does **not** assume:

* that a lower window equals a consecutive intersection of central masks;
* that any two lower windows have prescribed labels;
* that changes are confined to the eight-position boundary zone;
* the coordinatewise maximal factor.

It has exactly

\[
465\cdot11=5115
\]

semantic factor-bit variables.  All other variables merely select exact
witness intervals for the lower targets.  An optional universal mode also
adds selectors for upper targets not already guaranteed by the central row.

For a fixed row, default-mode SAT certifies exact central realization and all
1023 lower masks.  It gives a universal array when the row's consecutive
unions already cover the upper ideal.  Otherwise universal mode must also be
SAT.  A verified universal model proves `nu(11)=465`; UNSAT refutes only that
fixed row and schedule, not the unrestricted problem.

## 2. Fixed geometry and factor variables

Let `C_1,...,C_462` be a permutation of the rank-six layer.  Prescribe

\[
I_i=\begin{cases}
[i,i+2],&1\le i\le369,\\
[i,i+3],&370\le i\le462.
\end{cases}                                      \tag{2.1}
\]

Put

\[
E_j=\bigcap_{i:j\in I_i}C_i,
\qquad1\le j\le465.                              \tag{2.2}
\]

Introduce

\[
a_{j,b}\quad(1\le j\le465,\ b\in[11]),          \tag{2.3}
\]

where `a_(j,b)=1` means bit `b` occurs in factor entry `A_j`.

The first 5115 DIMACS variables are fixed by

\[
\operatorname{var}(j,b)=11(j-1)+b.               \tag{2.4}
\]

This fixed numbering makes model reconstruction independent of selector
enumeration.

## 3. Exact central clauses

For every `j` and `b notin E_j`, add

\[
\neg a_{j,b}.                                     \tag{3.1}
\]

For every position, require a nonzero entry:

\[
\bigvee_{b\in E_j}a_{j,b}.                        \tag{3.2}
\]

For every `i` and every `b in C_i`, add the positive pin

\[
\bigvee_{j\in I_i}a_{j,b}.                        \tag{3.3}
\]

Equations (3.1) and (3.3) are equivalent to

\[
\bigcup_{j\in I_i}A_j=C_i                         \tag{3.4}
\]

for all central masks.  If a clause (3.2) or (3.3) is empty, the row is
immediately impossible.  This is the exact mixed-run/factorability gate; no
separate run ansatz is used in the CNF.

## 4. Why every lower witness is short

Let `J=[l,r]` have length at least four.  Then `l<=462`, and the prescribed
central interval `I_l` lies inside `[l,l+3] subseteq J`.  Hence

\[
\bigcup_{j\in J}A_j\supseteq C_l
\]

has rank at least six.  Therefore every target of ranks one through five must
use a physical interval of length at most three.

There are 1392 such intervals.  The 369 early central triples are forced to
rank six, leaving exactly

\[
1392-369=1023
\]

potential lower slots, equal to the number of nonempty lower masks.  Thus any
satisfying factor automatically makes the lower targets and the remaining
short cells bijective, although the encoding needs only target at-least-one
clauses.

This is where the global formulation escapes the no-go theorem: the OR of a
physical overlap may be a strict subset of the corresponding central-set
intersection.

## 5. Exact witness selectors

For a target `S` and a candidate physical interval `J=[l,r]`, introduce one
selector `w_(S,J)`.  The implication

\[
w_{S,J}\Longrightarrow\bigcup_{j\in J}A_j=S       \tag{5.1}
\]

is encoded coordinatewise:

\[
\neg w_{S,J}\lor\neg a_{j,b}
\quad(j\in J,\ b\in E_j\setminus S),              \tag{5.2}
\]

and

\[
\neg w_{S,J}\lor\bigvee_{j\in J}a_{j,b}
\quad(b\in S).                                    \tag{5.3}
\]

Finally, for every required target,

\[
\bigvee_{J\in\mathcal W(S)}w_{S,J}.               \tag{5.4}
\]

No at-most-one clauses are needed.  One physical interval cannot satisfy two
different exact labels, and the 1023 lower targets already fill the 1023
available lower slots by counting.

### Safe candidate pruning

The generator keeps `J` only if all of the following hold.

1. **Envelope union:**

   \[
   S\subseteq\bigcup_{j\in J}E_j.
   \]

2. **Nonzero position support:** `S intersect E_j` is nonempty for every
   `j in J`, because every factor entry is constrained nonzero.
3. **Contained central targets:** if `I_i subseteq J`, then `C_i subseteq S`.
4. **Single-witness central-pin survival:** for every `b in C_i minus S`, the
   legal central pin set

   \[
   P_{i,b}=\{j\in I_i:b\in E_j\}
   \]

   is not contained in `J`.  Otherwise selecting `J` would erase every pin
   for `(i,b)`.

All four tests are necessary, so pruning preserves completeness.  Conflicts
caused jointly by two or more selected witnesses remain in the factor clauses
and are solved globally.

## 6. Lower and upper targets

In the default lower mode, all 1023 masks of ranks one through five receive
selectors over intervals of length at most three, and no upper selectors are
introduced.

Central masks of rank six are already represented by (3.4).  For upper masks,
first enumerate all consecutive unions of the fixed row.  By the
left-anchored hull identity, every such value occurs in **every** factor
realizing the central row.  No selector is needed for it.

With the optional `--universal` flag, any missing upper target is also encoded
by (5.1)--(5.4).  The exact
containment-multiplicity length caps at `n=465` are

\[
\begin{array}{c|ccccc}
|S|&7&8&9&10&11\\ \hline
\max |J|&10&31&87&213&465.
\end{array}                                      \tag{6.1}
\]

Thus the current `k11_lower956_upper549.txt` row, which misses twelve
rank-seven masks and one rank-eight mask, would need upper selectors only
through lengths 10 and 31.  Exact candidate enumeration shows that those
thirteen masks have no compatible factor intervals for this fixed row, so its
universal-mode formula contains thirteen empty clauses.  Its lower-mode
formula remains a meaningful and very small global factor-label gate.

## 7. Soundness and completeness for a fixed row

### Theorem

The default generated formula is satisfiable if and only if there is a
nonzero 465-entry factor which:

1. realizes every prescribed central interval (2.1);
2. represents every nonempty lower mask;
In universal mode there is the additional requirement:

3. every upper mask not already guaranteed by a consecutive central-row
   union is represented.

Consequently a satisfying lower-mode model is lower-complete; it is universal
if the row is upper-complete.  Every satisfying universal-mode model is a
universal nonzero `k=11` array.

### Proof

Given a model, read the first 5115 variables as `A`.  Clauses (3.1)--(3.3)
give exact central realization and nonzero entries.  For each encoded target,
(5.4) selects a candidate; clauses (5.2)--(5.3) make its OR exactly the target.
In universal mode the hull theorem supplies all upper masks omitted from the
selector set.

Conversely, given a factor of the specified mode, choose one witnessing
interval for every encoded target.  Every lower witness has length at most
three by Section 4; in universal mode every upper target has a witness within
the proved cap (6.1).  Its interval
passes all four safe pruning tests, and setting the corresponding selector
true satisfies (5.2)--(5.4).  All remaining selectors may be false.  QED

## 8. Model reconstruction and independent verification

The generator's decode mode reads a SAT model, extracts variables `1,...,5115`,
and writes the 465 integer masks.  It then checks central realization and all
lower masks; with `--universal`, it checks full coverage before accepting.

`k11_q369_global_factor_verify.cpp` is intentionally separate.  Given only
the fixed row and decoded array, it checks:

* row permutation and array ranges/nonzeroness;
* all 462 mixed central intervals exactly;
* all 108345 physical intervals;
* all 1023 lower targets, and optionally all 2047 nonzero targets;
* an independent distinct-suffix-OR recurrence.

A SAT claim is valid only after this second binary prints PASS in the matching
lower or universal mode.

## 9. Computational scale and search order

The base has 5115 variables.  Selector count is data-dependent and printed
by rank, together with the number removed by each safe prune.  The intended
workflow is:

1. run `--count` on several fixed factorable rows;
2. choose rows minimizing selector count and upper omissions;
3. emit DIMACS without solving locally;
4. run CaDiCaL/Kissat remotely with proof output for UNSAT cases;
5. decode and independently verify every SAT model.

For `k11_lower956_upper549.txt`, the audited lower-mode inventory is

\[
\boxed{8363\text{ variables},\qquad22843\text{ clauses}},
\]

with 3248 selectors distributed by target rank as

\[
49,551,1099,1061,488.
\]

Every lower target has at least one candidate and every central pin has at
least one legal factor position.  This count is small enough for a
proof-producing remote SAT run.  Universal mode adds thirteen target clauses,
but each is empty for this row, certifying that its known upper holes cannot be
recovered by changing factor labels alone.

Unlike the refuted rainbow branch, this CNF allows global sparse changes at
all 465 positions and arbitrary collisions among maximal meet shadows.  It is
therefore the smallest presently justified exact factor-label search on a
fixed q369 central row.
