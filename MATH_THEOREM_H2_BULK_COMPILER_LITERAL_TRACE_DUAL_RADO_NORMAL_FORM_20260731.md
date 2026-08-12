# Literal-trace compiler duals and the exact block-Rado normal form

Date: 2026-07-31  
Status: exact theorem and independent replay on all retained optima
`k=1,...,16`  
Scope: retrospective literal trace banks; no prospective Pascal-list or
`B(k)+O(1)` claim

## 1. Result

For a fixed literal word and a legal monotone-deadline schedule, retain only
the following lower compiler incidences.  A physical short cell `C` is joined
to the unique strict-lower target

\[
                         S=A(C)=\bigvee_{p\in C}A_p.       \tag{1.1}
\]

Call this the **literal trace bank** `H_A`.  It is a sound, generally much
smaller subbank of the catalogue of all individually legal caps.

The bank has a closed dual-matroid normal form.  If

\[
 G_S=\{C:A(C)=S\},\qquad m_S=|G_S|,                    \tag{1.2}
\]

and `F` is the set of physical cells whose literal value is not a
strict-lower target, then

\[
 M_{H_A}^*=\left(\bigoplus_S U_{m_S-1,m_S}\right)
                 \oplus U_{|F|,|F|}.                  \tag{1.3}
\]

Consequently, for every cell set `D`,

\[
 \boxed{r_{M_{H_A}^*}(D)=|D|-|{S:G_S\subseteq D\}|.} \tag{1.4}
\]

This has three immediate consequences.

1. A target having one literal witness makes that cell a dual loop, so no
   positive uniform rank-density statement is true before forced closure.
2. Fix every one-witness target to its cell and remove those pairs.  Every
   remaining block has size at least two, and therefore

   \[
                  r_{M_{H_A}^*}(D)\ge |D|/2            \tag{1.5}
   \]

   on the normalized ground.  This is sharp whenever a two-witness target
   remains.
3. For elementary deletion-task lists `L_i`, put
   `U_J=union_(i in J)L_i`.  The exact Rado system becomes

   \[
        \boxed{|U_J|-|\{S:G_S\subseteq U_J\}|\ge |J|}
        \qquad(J\subseteq I).                         \tag{1.6}
   \]

   In particular, after forced closure the simple list-expansion condition

   \[
                         |U_J|\ge2|J|                 \tag{1.7}
   \]

   is sufficient.  It is sharp for this proof: one full two-cell block has
   dual rank one.

Equation (1.6) is a laminar/partition reduction of the compiler dual-Rado
gate.  It is solved by the integral network

```text
task (capacity 1) -> listed cell (capacity 1)
                   -> target block G_S (capacity m_S-1) -> sink,
```

with cells in `F` sent directly to the sink.  Thus no general matroid oracle
is needed on this face.

## 2. Proof

For every retained incidence `(S,C)` and every `p in C`, (1.1) gives
`A_p subseteq S`.  Selecting that incidence therefore does not change any
letter of `A`.  Hence any target-saturating matching in `H_A` leaves the
entire word, all assigned middle rows, and all selected lower equalities
literal.  This proves trace guarding directly.

Each physical cell has exactly one literal OR label.  Therefore the cell
sets `G_S` are pairwise disjoint, and a cell set is independent in the
cell-side transversal matroid precisely when it contains at most one member
of every `G_S`; cells in `F` are loops.  Thus

\[
 M_{H_A}=\left(\bigoplus_S U_{1,m_S}\right)\oplus U_{0,|F|}.
\]

Dualizing gives (1.3), and summing the direct-sum ranks gives (1.4).

When all singleton blocks are removed, each remaining summand satisfies

\[
 \min_{\varnothing\ne X\subseteq G_S}
 {r_{U_{m_S-1,m_S}}(X)\over|X|}
 ={m_S-1\over m_S}\ge {1\over2}.
\]

The free summand has density one, proving (1.5).  Rado's theorem together
with (1.4) is exactly (1.6); (1.5) plus (1.7) proves the sufficient
condition.  The displayed network is the standard flow model of the
partition capacities and is integral.  `square`

## 3. Why global average density is insufficient

It is essential not to replace a uniform inequality by the single scalar
ratio

\[
              \beta_0={r(M_{H_A}^*)\over|C|}
                      ={|C|-|L|\over|C|}.             \tag{3.1}
\]

The first literal counterexample occurs at `k=5`.  The exact physical bank
has `17` cells, `15` lower targets, and dual rank `2`.  The nine cells

```text
(0,1), (1,1), (2,1), (10,1), (1,2),
(3,1), (11,1), (7,1), (2,2)
```

are respectively the unique witnesses of targets

```text
0x01,0x02,0x04,0x05,0x06,0x08,0x09,0x0a,0x0c.
```

Their one-task list passes the cardinality inequality suggested by the
global ratio,

\[
                        9\cdot2=18\ge17,              \tag{3.2}
\]

but its dual rank is zero.  This is not a counterexample to the valid
uniform-density implication; it proves that (3.1) is not uniform density.

For the first nontrivial flat recursion fixture, `k=7`, the corresponding
literal list has eight unique-witness cells

```text
(23,1),(35,1),(15,1),(21,1),(2,1),(1,2),(32,1),(13,1),
```

and

\[
                     8\cdot10=80\ge73,
 \qquad r^*(L)=0.                                     \tag{3.3}
\]

The exact optimum `k=16` has the same phenomenon: global rank is `5898` on
`32230` cells, while six explicitly audited singleton-witness cells satisfy
`6*5898=35388>=32230` and have dual rank zero.

Ordinary list Hall is also too weak after forced closure.  At `k=7`, target
`0x05` has exactly the two witness cells `(1,1)` and `(27,1)`.  Two deletion
tasks with this same two-cell list have an ordinary cell SDR, but selecting
both exhausts `G_0x05`; (1.4) gives dual rank `1<2`.  The two-fold expansion
condition detects this obstruction at equality.

## 4. Complete retained-certificate replay

The audit reconstructs the legal assigned middle rows and physical cell
catalogues from every retained optimum.  Dimensions `4` and `5` use their
exhaustively first exceptional monotone schedules; dimension `16` uses the
authenticated endpoint-rerooted `X3/Y3` schedule.  All other nontrivial rows
are the natural flat schedules.

| k | cells | lower targets | dual rank | singleton blocks | two-cell blocks | normalized minimum density | start-order convex blocks |
|---:|---:|---:|---:|---:|---:|:---:|---:|
|1|0|0|0|0|0|--|0/0|
|2|0|0|0|0|0|--|0/0|
|3|4|3|1|2|1|1/2|2/3|
|4|5|4|1|4|0|1|4/4|
|5|17|15|2|13|2|1/2|14/15|
|6|21|21|0|21|0|--|21/21|
|7|73|63|10|53|10|1/2|53/63|
|8|143|92|51|59|20|1/2|59/92|
|9|255|255|0|255|0|--|255/255|
|10|507|385|122|292|69|1/2|294/385|
|11|1392|1023|369|768|168|1/2|768/1023|
|12|1851|1585|266|1360|194|1/2|1360/1585|
|13|5154|4095|1059|3387|501|1/2|3388/4095|
|14|6867|6475|392|6130|307|1/2|6130/6475|
|15|19311|16383|2928|13900|2100|1/2|13901/16383|
|16|32230|26332|5898|21684|3609|1/2|21685/26332|

At `k=6` and `k=9` scalar slack is literally zero, so there is no
prospective deletion capacity in this bank.  At every positive-slack
dimension from `k=5` onward the raw bank has many dual loops, but forced
closure leaves the sharp half-density normal form.

## 5. Interval and laminar scope

The witness blocks `G_S` are disjoint and hence form a laminar family, which
is why the block-capacity flow above is exact.  They are not generally
intervals in the physical monotone orders.  The first flat failure is again
`k=7`: the two witnesses `(1,1)` and `(27,1)` of `0x05` have start-order
positions `2` and `54`.  The audit separately tests start/length,
deadline/start, and length/start orders and records the complete failure
counts shown in its JSON.

One may of course reorder cells by target label so that all `G_S` are
intervals.  That does not prove the prospective compiler theorem: the
future Pascal deletion lists must be convex in the **same** order, and no
retained `k<=16` optimum exports such lists.

## 6. Exact scope boundary

This theorem is useful in two ways: it gives a literal family of dual-Rado
cuts and it identifies the precise normalization needed before a uniform
density argument can begin.  It does not solve the all-dimensional gate.

* `H_A` is chosen after the literal word is already known.  It is a
  retrospective certificate, not a construction of a future compiler.
* The stored optima do not contain elementary Pascal deletion-list
  catalogues, so (1.6) has not been checked on the bulk recursive lists.
* At `k=16`, this bank is not the `347677`-edge individually-sound graph of
  the direct CNF.  Its `21684` singleton blocks must not be confused with
  the `14060` marginally essential assignments in the separate forced-
  closure audit.
* Coupled block deletions, residence, upper witnesses, and topology remain
  separate.

No `B(k)+O(1)`, unrestricted Pascal, or `nu=B` claim is made.

## 7. Audit

Run

```text
python3 scratch/audit_h2_bulk_compiler_dual_rado_smallk_20260731.py
```

It writes

```text
scratch/h2_bulk_compiler_dual_rado_smallk_20260731.audit.json
```

and checks all middle rows, lower palettes, multiplicity histograms, the
closed dual-rank formula, the scalar-density counterexamples only when the
displayed expansion inequality actually holds, sharp positive and negative
Rado calibrations, and all three physical cell orders.  It is dependency-
free and uses no solver.
