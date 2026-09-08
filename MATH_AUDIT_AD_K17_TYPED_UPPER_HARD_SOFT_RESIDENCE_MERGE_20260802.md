# Exact typed merge audit for the `k=17` round-two residence/upper CEGAR master

Date: 2026-08-02  
Scope: the fixed marker58 quotient catalogue, the accumulated 385-row
residence bank, and the 249 accumulated cyclic-upper component-colour rows.
No SAT run was made.  This note proves an encoding contract, not existence,
residence, a valid opening, or an OR word.

## 1. Frozen inputs

The relevant authenticated files are:

| file | SHA-256 |
|---|---|
| `scratch/k17_marker58_residence_round2_20260802/marker58_residence_round2.cnf` | `272d0f23bedd0b22c830c4bc08883ad9bf7883de61ce1f448e648df9752f2e93` |
| `scratch/k17_marker58_residence_round2_20260802/cumulative.blocks.cnf` | `39c2378903467f06ea10ba69c5f2ea89d2fb2b545dc78bd4d484d9be9d7e68f2` |
| `scratch/ad_k17_upper_component_cegar_20260802/upper_seed.blocks.raw.cnf` | `ba91f8dba678c3cf0c3c4aba57fd2fd4bdea5adb5058ceac152541306427c77f` |
| `scratch/ad_k17_upper_component_cegar_20260802/upper4029.blocks.raw.cnf` | `e1c94d1d7d851a40354ba4e19d64407af1e8f4c2225f0a3b3ff7ffc1fe1819b9` |
| `scratch/ad_k17_upper_component_cegar_20260802/upper_cumulative.blocks.raw.cnf` | `cc907ff1febb987f3e02d6b63426cd00376d660e830fde7ac00ef6604c4e2c8f` |

The executable audit source is

`scratch/ad_k17_upper_component_cegar_20260802/audit_ad_k17_round2_typed_soft_upper_merge_20260802.cpp`

with SHA-256

`507510d246322976e66986da4170fff4e41a1d12da113b1b548fbf5dcead115e`.

Its frozen output is

`scratch/ad_k17_upper_component_cegar_20260802/round2_typed_soft_upper_merge.audit.json`

with SHA-256

`da0284b9a49bc11ce3642ad39d5422ab42c8a3c4a7d2952a6d834dcdd0624326`.

## 2. Exact set and polarity audit

Let `x_1,...,x_35713` be the catalogue primary variables.  The round-two
DIMACS has 204,167 variables and 439,532 clauses.  Canonicalizing each
clause by sorting its literals proves the following exact decomposition:

\[
  439532=439145+2+385.                                    \tag{2.1}
\]

The first 439,145 rows are the owner/facet/cap skeleton, the next retained
hard prefix includes two previously learned component cuts, and the final
385 clauses are, as a set, exactly `cumulative.blocks.cnf`.  Literal order
differs between the two files, so bytewise line comparison is not the right
test; canonical clause-set comparison gives equality.  The 385 rows are
distinct, contain 1,206 literals in total, and every literal is a negative
primary literal.

The upper banks have 149 and 141 distinct rows with exact intersection 41.
Their union therefore has

\[
       149+141-41=249                                    \tag{2.2}
\]

distinct clauses and 153,188 literals.  Every literal is a positive primary
literal, and every row is nonempty.  The frozen cumulative file is exactly
this set union.  None of its 249 rows is already a clause of the round-two
CNF.

Thus the signs themselves enforce the intended type distinction:

* a residence blocker is a negative clause
  \(C_c=\bigvee_{e\in S_c}\neg x_e\);
* an upper component-colour cut is a positive ALO
  \(A_u=\bigvee_{e\in P_u}x_e\).

The positive rows must remain hard.  They express necessary alternatives
for witnessing an already exposed missing upper target; relaxing them would
optimize away the upper requirement.

## 3. Soft-residence projection theorem

**Theorem 3.1 (exact fixed-bank projection).**  For each of the 385
residence rows introduce a fresh Boolean `y_c` and replace the hard row
`C_c` by

\[
                    C_c\vee y_c.                         \tag{3.1}
\]

For an integer \(0\le B\le385\), the projection of (3.1) together with

\[
                    \sum_c y_c\le B                       \tag{3.2}
\]

onto the old variables is exactly the set of old assignments which violate
at most `B` clauses in the accumulated residence bank.

**Proof.**  If `C_c` is false, (3.1) forces `y_c=1`; hence at most `B` rows
can be false.  Conversely, given an old assignment with at most `B` false
rows, set `y_c=1` precisely for those false rows and zero otherwise.  Then
(3.1)--(3.2) hold.  This proves equality after projection. \(\square\)

If decoded `y_c` values themselves are to be trusted as exact indicators,
also add

\[
                 \neg y_c\vee x_e\qquad(e\in S_c).       \tag{3.3}
\]

Equations (3.1) and (3.3) give
`y_c <=> AND_{e in S_c} x_e`.  These reverse implications are unnecessary
for projected satisfiability or optimization, but they prevent gratuitous
true relaxation bits in a nonoptimal SAT model.  There are exactly 1,206
such optional clauses.

## 4. Exact dimensions before the cardinality encoding

Retaining the two sound historical component cuts, the hard/soft typed body
is:

| family | clauses |
|---|---:|
| owner/facet/cap skeleton | 439,145 |
| retained component cuts | 2 |
| hard accumulated upper ALOs | 249 |
| relaxed residence rows `(C_c OR y_c)` | 385 |
| **total before counter** | **439,781** |

Use fresh variables

\[
             y_1,\ldots,y_{385}=x_{204168},\ldots,x_{204552}. \tag{4.1}
\]

Hence the pre-counter formula has 204,552 variables.  With the optional
exact-indicator implications (3.3), it has 440,987 clauses before the
counter.  Any totalizer auxiliary variables must begin after 204,552.

If the two historical component cuts are deliberately dropped and topology
is learned from scratch, replace 439,147 by 439,145 and reduce each clause
total above by two.  The choice must be recorded; retaining already valid
lazy cuts is logically harmless.

An incremental totalizer may expose outputs `o_j` meaning
`sum y_c >= j`, so a trial bound is the assumption `-o_(B+1)`.  This makes
SAT monotone in `B` and permits binary search followed by descent.  A fixed
`B` sequential counter is also exact, but changing `B` then requires a
rebuild unless the chosen implementation explicitly supports assumptions.

## 5. Incumbent truth ledger and the `B=237` qualification

Direct primary-assignment evaluation gives:

| incumbent | false residence rows among 385 | false hard upper rows among 249 |
|---|---:|---:|
| original `c68b.double_fusion` | 316 | 155 |
| `paired_escape005` / 4,029-run incumbent | 237 | 152 |

For the current incumbent, the 237 false residence rows are the 168 rows
shared with round one plus 69 newly exposed rows; it satisfies the 148
old-only residence clauses.  On the upper side it falsifies all 141 rows
extracted from itself and another 11 seed-only rows, for 152 false union
rows.

Therefore the current factor certifies feasibility at `B=237` only for the
base/residence relaxation (with its already valid topology data).  It is
**not** a witness at `B=237` after the 249 upper rows become hard.  In the
integrated master, 237 is merely a trial bound until a satisfying decoded
factor is found.

## 6. Why simple appending is the wrong optimization build

Appending the 249 upper rows to the frozen round-two CNF is logically sound
as a different, all-hard necessary model.  It would have 204,167 variables
and 439,781 clauses.  It does not implement the proposed objective because
the old 385 residence rows remain hard.  Appending `(C_c OR y_c)` copies and
a counter while retaining those hard rows also leaves every `y_c` useless.

The correct soft build must:

1. byte-preserve the chosen 439,147-row hard prefix (or the declared
   439,145-row pristine prefix);
2. append the 249 positive upper ALOs as hard clauses;
3. replace the residence tail by the 385 clauses `(C_c OR y_c)`;
4. append one exact cardinality encoding over all 385 relaxation variables;
5. reconstruct every SAT assignment physically before accepting it.

## 7. Lazy-loop contract and exact scope of bounds

For a fixed discovered bank, proof-producing UNSAT under bound `B` proves
that every assignment satisfying the current hard relaxation violates at
least `B+1` known residence rows.  Because future valid hard cuts only
shrink the feasible set, such a lower bound remains valid after adding
topology or upper cuts.

A SAT result is provisional.  Decode the physical factor, then:

1. test degree/palettes and one physical cycle (and scoped voltage only when
   an authenticated quotient action exists);
2. run the independent insertion-to-next-deletion/direct-run residence
   oracle;
3. add every newly exposed negative residence blocker with a new relaxation
   input;
4. run cyclic all-width upper separation and add new positive ALOs;
5. separately handle linear opening, rank-10 cut restitution, source, and
   compiler gates.

When a new residence row is added, the objective itself has gained an input.
The totalizer must be extended soundly or rebuilt; silently leaving the new
row outside the counter is unsound.  Old UNSAT lower bounds persist, while a
previous SAT upper bound must be revalidated.  `B=0` for the present 385
rows is not residence until the transition-gap oracle exposes no further
motif.

The upper ALO bank is likewise a finite lazy prefix, not sufficient
all-width completion.  Its present scope is cyclic ranks 11--17 in the
fixed `Z_17` catalogue.  It makes no nonwrapping opening, nonflat source,
common-cap, compiler, or literal OR-word claim.

## 8. Exact proved boundary

Proved: exact clause-set decomposition, exact upper union and overlap,
polarity/range checks, zero pre-existing upper-row duplication, exact
incumbent violation counts, and the projected equivalence of the soft
residence encoding.

Not proved: SAT at any integrated bound, an integrated `B=237` witness,
topology or voltage of a future model, residence after CEGAR saturation,
linear opening, source realization, or a universal word.
