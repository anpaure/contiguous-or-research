# K16 c7be compiler: DM-supported maximal common-Q closure normal form

Date: 2026-07-31  
Status: exact equisatisfiable CNF reduction and independent literal-model replay; the reduced CNF was not launched

## 1. Fixed authenticated fibre

The middle chronology is

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

and the fixed monotone P/Q schedule is

\[
 X=\{12870,12871,12872\},\qquad Y=\{0,1,6388\}.
\]

Its selected proper-prefix area is 32,224.  Including the exact omitted-start
credit gives 32,230 physical lower cells.  Cell 12,781 is the singleton cell
at physical position 6,389 and is reserved for `0x8000`.  After reserving it,
the exact marginal graph has

```text
lower targets          26,331
available cells        32,229
incidences            347,677
```

The cap at position 6,389 is `0x8000`; all other position caps are the maximal
middle envelopes.  There are 70,759 envelope coordinate incidences.  The
middle, arbitrary-upper, scalar-capacity, singleton and marginal Hall gates
were independently audited before this reduction.

The literal word

```text
scratch/k16_optimal_12873_20260731.word
SHA-256 890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

is already an independently authenticated universal word.  The construction
below is therefore retained as an exact propagation/control normal form, not
as a second existence search.

## 2. Common-Q equations

Write \(E_p\) for the fixed capped envelope.  For a physical lower cell
\(C\) and a lower target \(S\), let \((S,C)\) be an incidence exactly when
the complete individual-pin criterion holds.  A selected incidence caps
every covered position by \(S\).

For a set \(F\) of selected incidences define its maximal common cap

\[
 Q_p(F)=E_p\cap\bigcap_{(S,C)\in F:\ p\in C}S. \tag{2.1}
\]

The common-Q theorem says that \(F\) is physically realizable exactly when

1. every \(Q_p(F)\) is nonempty;
2. every scheduled middle row has its exact OR under \(Q(F)\); and
3. every selected cell \((S,C)\) has OR exactly \(S\).

Necessity follows by enlarging any simultaneous physical word to (2.1).
Sufficiency is literal: \(Q(F)\) itself is the word.  No `DA=DP`, flat
sandwich, or legacy 4/7/3 collar assumption occurs here.

## 3. Matching-support reduction

### Lemma 3.1 (allowed-edge test)

Fix one matching \(M\) saturating all lower targets.  On right-cell vertices,
put an arc

\[
 C\longrightarrow M(S)
\]

for every nonmatching incidence \((S,C)\).  Let \(R_0\) be the unmatched
right cells.  Then \((S,C)\) belongs to some left-perfect matching if and
only if one of the following holds:

1. \(C=M(S)\);
2. \(C\) is reachable from \(R_0\); or
3. \(C\) and \(M(S)\) lie in the same strongly connected component.

Indeed an alternating path from a free right cell shifts the free cell along
the path, while an alternating directed cycle rotates a matching.  Conversely
the symmetric difference of two left-perfect matchings is a disjoint union
of exactly such paths and cycles.

Every literal compiler chooses one witness cell for every lower target.  A
single physical cell has one literal OR and therefore cannot witness two
different targets.  The chosen incidences form a left-perfect matching.
Consequently every edge outside Lemma 3.1's support may be deleted without
changing satisfiability.

For c7be, two different initial perfect matchings give the identical support:

```text
raw incidences                   347,677
supported incidences             252,531
deleted unsupported incidences    95,146
supported-edge SHA-256
  c625f6880d1ce6e32f20610a2af6b123000167b7f12fe2a727d46cbf122fd2d4
```

The primary implementation uses the contracted right-cell graph.  The
independent audit uses the full uncontracted bipartite alternating digraph.

## 4. Forced neutral witnesses

After matching-support pruning, exactly 14,059 targets have degree one:

```text
rank 5       195
rank 6     3,811
rank 7    10,053
```

Their `(target,cell)` catalogue has SHA-256

```text
5a1984a11b6b76eb35ed8acdbeb3653c804975a04a3ab3fe7a56cff41f6ec686.
```

Every one is cap-neutral:

\[
 E_p\subseteq S\qquad(p\in C). \tag{4.1}
\]

Thus selecting it changes no letter of the maximal envelope.  Its selector
and unit clause may be removed; only the positive clauses requiring every
bit of \(S\) somewhere in \(C\) remain.  The residual selector domain is

```text
targets                         12,272
incidence selectors            238,472
target ranks 1..7       15,120,560,1820,4173,4197,1387
edge ranks   1..7     2796,22431,60045,77556,53546,19246,2852
```

## 5. Why both AMO families are unnecessary

Introduce only an at-least-one selector row for each of the 12,272 residual
targets.

### Lemma 5.1 (cell AMO is entailed)

Suppose selectors \((S,C)\) and \((T,C)\) are both true.  Equation (2.1)
gives

\[
 \bigvee_{p\in C}Q_p\subseteq S\cap T.
\]

The positive witness clauses for the first selector require the same OR to
contain every bit of \(S\), hence to equal \(S\).  The second requires it to
equal \(T\).  Therefore \(S=T\).  Two distinct target rows can never share a
cell, so explicit cell-at-most-one clauses add no semantics.

### Lemma 5.2 (target AMO is unnecessary)

Selecting several cells for the same target is sound: the resulting word
literally realizes that target in every selected cell.  It is also harmless
for completeness.  From any satisfying selection, retain one witness for
each target and delete the extras.  Removing caps can only enlarge \(Q_p\).
The enlarged letters remain inside every middle envelope and, on every
retained lower cell, inside its retained target.  Exact middle and retained
lower ORs already contain all required bits, so enlargement cannot destroy
them or introduce a forbidden bit.  Thus every solution has a one-witness
normalization, but the CNF need not encode it.

Together Lemmas 5.1 and 5.2 remove all target/cell AMOs and all 636,794
cardinality auxiliaries present in the direct matching CNF.

## 6. Maximal-closure bit encoding

For every envelope atom \((p,b)\), let \(B_{p,b}\) be the residual selectors
whose cell covers \(p\) and whose target omits \(b\).  If this blocker set is
empty, maximal closure fixes \(q_{p,b}=1\).  Otherwise introduce one Boolean
\(q_{p,b}\) and encode

\[
 q_{p,b}\iff\bigwedge_{y\in B_{p,b}}\neg y             \tag{6.1}
\]

by the binary clauses

\[
 (\neg q_{p,b}\vee\neg y)\quad(y\in B_{p,b})
\]

and the one reverse clause

\[
 q_{p,b}\vee\bigvee_{y\in B_{p,b}}y.
\]

The exact c7be ledger is

```text
envelope atoms                   70,759
fixed-true atoms                 23,999
live common-Q atoms              46,760
blocker implications            561,707
```

Every physical position has at least one fixed-true atom.  Hence every one
of the 12,873 nonempty-letter clauses becomes a tautology.  Fixed-true atoms
also delete 74,020 of 102,960 middle-bit rows, 60,267 of 94,212 forced-lower
rows, and 475,576 of 941,187 conditional residual-lower rows.

The fixed schedule, maximal envelopes and scalar capacity are constants, not
decision variables.  No schedule or capacity PB row belongs in this CNF.

## 7. Final exact CNF ledger

The remaining clauses are:

| family | clauses | literal occurrences |
|---|---:|---:|
| residual-target at least one | 12,272 | 238,472 |
| blocker binary | 561,707 | 1,123,414 |
| maximal-closure reverse | 46,760 | 608,467 |
| middle-bit coverage | 28,940 | 97,057 |
| forced-lower-bit coverage | 33,945 | 80,407 |
| selected-lower-bit coverage | 465,611 | 1,027,268 |
| **total** | **1,149,235** | **3,175,085** |

There are exactly

```text
238,472 selector variables
 46,760 live common-Q bit variables
285,232 total variables
```

and zero cardinality auxiliaries.  This is equisatisfiable with the fixed
c7be common-Q compiler problem.

## 8. Independent positive replay

The independent audit does not import the CNF builder.  It reconstructs the
geometry through the frozen endpoint-12825 independent audit, computes the
same 252,531-edge support in the uncontracted bipartite graph, and derives
the same 285,232-variable / 1,149,235-clause ledger.

It then scans the authenticated optimal word.  For every residual lower
target it chooses the first supported cell whose literal OR is that target.
The 26,331 chosen cells are distinct.  All 14,059 forced choices agree with
the forced catalogue.  Intersecting their caps with the envelope reproduces
the authenticated word byte-for-byte, and literal replay gives:

```text
empty letters                 0
middle failures               0
selected-lower failures       0
covered nonempty masks   65,535
word SHA-256
  890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe
```

Thus the normal form is not merely equisatisfiable abstractly; it has an
independently replayed satisfying assignment inherited from the final word.
No solver was launched on the reduced CNF.

## 9. Frozen artifacts and scope

```text
production builder/audit-only source
  scratch/build_k16_c7be_dm_commonq_closure_cnf_20260731.py

production audit ledger
  scratch/k16_c7be_dm_commonq_closure_builder_20260731.audit.json

independent source
  scratch/audit_k16_c7be_dm_commonq_closure_independent_20260731.py

independent audit ledger
  scratch/k16_c7be_dm_commonq_closure_independent_20260731.audit.json
```

This theorem is exact only for the authenticated c7be chronology, its fixed
P/Q schedule, and the reserved singleton.  It is not an unrestricted
chronology theorem.  The separate literal certificate settles the K16
optimum; this note records the compiler normalization which led to it.

Frozen hashes:

```text
builder source
  87004db4c618e0f8721507bf00af8f110d3d93fd6840434ad61536f5ce4338dc
builder audit JSON
  f80f905bd04a72c455436acdbc755ed28ea59251c2b1c0a0c21da159aabbbee3
  payload 8733fb536202298a1d4c67a06373f5c13ee781d8d46b97971935feadad0587a4
independent source
  65c3572cd0c93f3a98971868f4e1222067a0f433b2838aa8851591435ef85b9b
independent audit JSON
  5532dbf850499d5cc18a8b13d861ec43335e08e6d468868ffc597e3c97086dd5
  payload 0be6af97faf78c5000a2b882281f474fba5c17c9655d05e5bd64170f4f635e8f
```
