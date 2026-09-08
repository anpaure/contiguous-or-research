# K16 external-H38 expanded13: canonical-cell strengthening

Date: 2026-07-30  
Lane: AD  
Status: exact equisatisfiable encoding and solver-free audit; no solve verdict

## 1. Frozen instance

The source-relative instance is the unbounded-cardinality dynamic-substitution
model in the remote bundle

```text
/home/amodo/or15/work/root_k16_external_ready_h38_expanded13_20260730
```

with local frozen copies under

```text
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
```

Its exact inputs are

```text
model.cnf
SHA-256 73a426dcb8586ef70dc23902d52caad628a3b63190e411b24f53b144ded8b715

model.map
SHA-256 6afae83ab5e574a5b975cf4b9a64494dadf29afdf53f7965ab1d7f906be2a6c3

k16_Hfinal_externalblockers_v2_h38.word
SHA-256 575f9e5b3453618636918cb410cff88390e12c2dd09fc4d635820b40e1bd4880

k16_external_ready_h38_expanded13_positions_20260730.txt
SHA-256 6298916f9ed2f5415f7f4ec72db90cb996b8fe18efc473c959821a17a7e7624c
```

The editable physical positions are

```text
110,111,112,666,667,670,4299,4301,6522,6523,6524,6526,9958.
```

The map has `budget=-1`, 94 repair targets, 1,956 witness terms, 2,177
variables, 37,093 clauses, and 82,744 literals.  Thus there is no edit-count
or change-cardinality constraint.  This absence is essential below.

## 2. Generic canonical-cell theorem

For editable index (i) and coordinate (q), let (x_{i,q}) be the actual
cell bit.  Each witness variable (w=(T,[a,b],N)) certifies an exact literal
interval for target (T): when (w=1), every editable cell in ([a,b]) is a
submask of (T), and the cells jointly supply every bit in the residual need
(Nsubseteq T).  Every repair target has an at-least-one row over its
witnesses, and every editable cell is nonzero.

Define

\[
 {cal O}_{i,q}=\{w=(T,[a,b],N):a\le i\le b, q\notin T\}.
\]

Add the canonical-completion row

\[
 \boxed{x_{i,q}\ \vee\!\bigvee_{w\in{cal O}_{i,q}}w}                 \tag{2.1}
\]

for every (i,q).

### Theorem 2.1

For an unbounded-cardinality dynamic-substitution model of the displayed
form, adding all rows (2.1) preserves satisfiability.  In a strengthened
model,

\[
 x_{i,q}=1
 \quad\Longleftrightarrow\quad
 q\in\bigcap\{T:w=(T,I,N)=1, i\in I\},                              \tag{2.2}
\]

where the empty intersection is the full coordinate set.

#### Proof

The parent formula already contains

\[
                 w\Longrightarrow \neg x_{i,q}
       \qquad(w\in{cal O}_{i,q}).                                    \tag{2.3}
\]

Together, (2.1) and (2.3) give (2.2).

For equisatisfiability, start with an arbitrary parent model and leave every
witness truth value fixed.  Define (x'_{i,q}) by the right side of (2.2).
If (x_{i,q}=1) in the old model, (2.3) shows that no true witness through
(i) omits (q); hence (x'_{i,q}=1).  Thus (x') is a coordinatewise
expansion of (x).

Consider a true witness (w=(T,[a,b],N)).  For every (iin[a,b]) and
(q\notin T), that witness itself belongs to ({\cal O}_{i,q}), so
(x'_{i,q}=0).  Therefore every transformed cell in its interval remains a
submask of (T).  Every bit of (N) supplied before the transformation is
still supplied because (x'\supseteq x).  Thus every old true witness
remains true, and each target at-least-one row remains satisfied.  Cell
nonzeroness is also preserved by expansion.

Targets omitted from the repair family have a fixed-only interval witness by
construction, so changing editable cells does not remove their certified
witness.  Finally reset each change indicator to the truth value of
"transformed cell differs from its incumbent."  The change-equivalence rows
then hold.  Because `budget=-1`, change indicators occur in no cardinality
constraint.  The transformed assignment therefore satisfies the parent and
all rows (2.1).

The reverse implication is immediate because the strengthened formula
contains every parent clause.  This proves equisatisfiability. \(\square\)

The theorem is not asserted for an exact edit budget: canonical expansion can
change the number of cells differing from the incumbent.

## 3. Why the old 216-family list does not transfer verbatim

The 216-family catalogue was the complete minimal empty-intersection
hypergraph for a different 57-target family in the three-profile
occupancy/blocker model.  It consisted of 18 two-target conflicts, 46
three-target conflicts, and 152 four-target conflicts at each collar cell.

The expanded13 model has a different 94-target repair family and uses
witness-term variables plus explicit cell bits rather than one occupancy bit
per target and cell.  Its target family already has

\[
 15\text{ disjoint pairs},\qquad
 5741\text{ inclusion-minimal zero-intersection triples}.              \tag{3.1}
\]

Thus neither the masks nor the number 216 are generic.  No completeness
claim for the higher-order expanded13 conflict hypergraph is made here.

The generic principle is nevertheless already compact in this formulation.
For any family of simultaneously true witness terms meeting one cell and
having empty target intersection, the parent implications (2.3), together
with that cell's nonzero clause, imply the corresponding witness-conflict
clause.  Hence all orders of intersection conflict are present through the
16 explicit (x)-bits.  Importing the old 216 rows would be both
target-incorrect and redundant.  The genuinely transferable strengthening
is the reverse, canonical direction (2.1).

## 4. Exact expanded13 output

There are (13\cdot16=208) rows (2.1), with no new variables.  Their witness
right sides contain 22,736 incidences in total; the minimum row has 22
omitting witnesses and the maximum has 302.  The strengthened instance has

```text
variables  2177
clauses   37301
literals 105688
```

and is frozen as

```text
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
  model.canonical.cnf
SHA-256 7ef805b9b6665e2c87bed3e18bb573ece33dc07f64e40716f2dd8c09fa85e294
```

The deterministic postprocessor is

```text
scratch/strengthen_ad_k16_external_h38_expanded13_canonical_cells_20260730.py
SHA-256 b7ac8c8f315c54f1294c56a67d68df0156b5cacc52d83f4abb0f63d53a181927
```

and its audit is

```text
scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
  model.canonical.audit.json
SHA-256 33d18cd67612eff8f3c2ad409fa9c31b0baf43833c600d59717479574aa278d3
payload SHA-256 982ddb7e9ea5d4186c6818c13c73f31abb8f090208abf80c73dd564fc43b9516
```

Before adding any row, the postprocessor reconstructs all 37,093 parent
clauses in their exact original order from the pinned map, including
nonzero-cell rows, change equivalences, witness forbidden-bit implications,
residual-need rows, and target at-least-one rows.  It also checks all mapped
variables, source incumbents, target and witness counts, input hashes, and
the census (3.1).  No SAT solver was launched.  Consequently this artifact
is an exact strengthened search instance, not a SAT candidate, an UNSAT
certificate, or a new bound on \(\nu(16)\).

An independent implementation additionally rebuilt the 65,441 fixed-only
targets, all 94 repair targets, 481 changed-interval bases, all 1,956 ordered
terms, the complete parent clause sequence, and the 208-row suffix directly
from the word and positions.  It returned `PASS`:

```text
MATH_AUDIT_AD_K16_EXTERNAL_H38_EXPANDED13_CANONICAL_CELL_INDEPENDENT_20260730.md
SHA-256 bd20b8c4eaedbe1094cd82a24b1d62c76c51675fa37ccd0dfdec964a8eda7e99

scratch/audit_ad_k16_external_h38_expanded13_canonical_cells_independent_20260730.py
SHA-256 acd8630d6f04f3a225bf94d79fc729b015dce930681e62dff6754cf711497dfd

scratch/ad_k16_external_h38_expanded13_blocker_strengthening_20260730/
  model.canonical.independent_audit.json
SHA-256 1f75b0ebb1a7a73220cdc05bae05ff7c2059fca22112789cf91d105002d97e8f
payload SHA-256 d71a9c086f1bb867fbf02072a7a9d794b35fa0b4ba0442755b788d4fdbc45807
```
