# Independent audit: `k=17` transition gaps and the soft residence objective

Date: 2026-08-02  
Scope: the fixed marker58 quotient catalogue, its authenticated connected
`c68b.double_fusion` and `paired_escape005` factors, and the accumulated
round-two residence-blocker bank.  This note makes no SAT, existence,
all-width-upper, source, or compiler claim.

## 1. Frozen inputs and provenance

The transition-gap checker is

`scratch/audit_middlelevels_flip_gaps_20260802.cpp`

with SHA-256

`e6d2c4bffb727a685acccdc116818ae128424372e67fe68d31b2f4588bd297ec`.

The two independently replayed factor inputs were:

| factor | SHA-256 |
|---|---|
| `scratch/r2_k17_marker58_upper_q1_double_fusion_replay_20260802/c68b.double_fusion.factor.tsv` | `7d39e3aee641521df2d441d0342a2bd060dafb05cc7f5703ef206f53b6d21e3c` |
| `scratch/k17_marker58_residence_round2_20260802/paired_escape005.factor.tsv` | `19bb99264cd592db409c9b3dcb5cd6d59309e54bc64067780b2e426471381aa8` |

The round-two CNF has SHA-256
`272d0f23bedd0b22c830c4bc08883ad9bf7883de61ce1f448e648df9752f2e93`
and header `p cnf 204167 439532`.

The exact current and cumulative blocker files have hashes

* current 237 rows:
  `a0230ca760bbaba34dfb687cb991251b440f407164d71470e0fc62d949210821`;
* cumulative 385 rows:
  `39c2378903467f06ea10ba69c5f2ea89d2fb2b545dc78bd4d484d9be9d7e68f2`.

The independent current extraction audit has SHA-256
`4aa4e2e65cd439f2bdac693a6b9ef40602d837322823b8f58fa628784ad71a51`;
the exact cumulative-union audit has SHA-256
`c61fc031dadecba244b182a693b7a837f529c9f2db5a3652aef5e500ec1e0925`.

## 2. Exact transition-gap identity

Orient a cyclic Johnson owner transition as

\[
        T_i\longrightarrow T_{i+1}
          =T_i-\{p_i\}+\{q_i\}.
\]

Put the deletion event at time `2i` and the insertion event at time
`2i+1`.  If the next deletion of the newly inserted coordinate is
`p_j=q_i`, then its positive owner-run length is

\[
       \ell=j-i={((2j)-(2i+1))+1\over2}.
\]

Consequently a positive run is too short for depth `d` exactly when the
insertion-to-next-deletion gap is at most `2d-1`, equivalently
`1 <= j-i <= d`.  For `d=3`, this is precisely the length-1/2/3 positive
run family.  The authenticated rank-eight-rainbow factors have no length-1
positive runs, leaving lengths two and three.

The checker implements this event calculation and, independently, scans
the cyclic binary owner trace of every coordinate after rooting at a zero.
The two calculations agree in total on both frozen factors:

| factor | length 2 | length 3 | total short positive runs |
|---|---:|---:|---:|
| `c68b.double_fusion` | 2,873 | 2,499 | 5,372 |
| `paired_escape005` | 2,176 | 1,853 | 4,029 |

The replayed cycles each have 24,310 owners and 24,310 edges.  Thus the
published agreement claims are correct.  The checker audits **positive**
residence only; it does not audit zero-run residence.  It compares the two
methods' total short-run count, while the displayed per-length histogram
comes from the event method.  The same per-length numbers are independently
recorded in the frozen residence audits, but the checker itself does not
compare direct per-length histograms.

## 3. Why 237 clauses and 4,029 runs are consistent

The marker58 master and both incumbents are `Z_17`-equivariant.  In the
current occurrence file, grouping the 4,029 physical short runs by their
sorted nonfixed primary-variable segment gives exactly 237 groups, every
one of size exactly 17.  Hence

\[
             4029=17\cdot237.
\]

The quotient blocker for one group is

\[
        C_c=\bigvee_{x_e\in S_c}\neg x_e,
\]

where `S_c` consists of the selected nonfixed edges in the entering,
internal, and leaving segment of the short run; fixed protected edges are
omitted.  The current arity histogram is

\[
       1^{35},\quad 2^{10},\quad 3^{105},\quad 4^{87}.
\]

The old bank has 316 clauses, the current bank 237, their intersection 168,
and their exact set union 385.  Direct evaluation of all 385 clauses on the
authenticated `paired_escape005.model` gives exactly 237 violations, with
the same arity histogram above.  In particular, the incumbent satisfies
all 148 old-only clauses and violates the 168 common plus 69 new clauses.

Therefore `B=237` means 237 violated **quotient short-run-orbit clauses**.
It does not mean 237 physical runs: on this incumbent it corresponds to
4,029 physical runs.

## 4. Exact soft-blocker encoding

For each accumulated row `C_c`, introduce a fresh variable `y_c` and replace
the hard row by

\[
             C_c\vee y_c.                              \tag{4.1}
\]

Together with `sum_c y_c <= B`, projection to the primary variables is
exactly the condition that at most `B` accumulated rows are violated.  The
reverse clauses

\[
             \neg y_c\vee x_e\qquad(e\in S_c)           \tag{4.2}
\]

are optional for projected satisfiability, but make `y_c` the literal
violation indicator and are recommended for a fail-closed decoded
objective.  Without (4.2), an independent validator must recompute the
violation count from the primary assignment rather than trust arbitrary
true relaxation variables.

An incremental totalizer can expose outputs `o_j` and impose a trial bound
by the assumption `not o_(B+1)`.  A sequential counter is also exact, but a
separately rebuilt fixed-`B` counter is not by itself an incremental binary
search interface.

### Essential construction warning

The frozen round-two CNF already contains the 385 rows as hard clauses:

* 439,145 base owner/facet/cap clauses;
* two incumbent component cuts;
* 316 round-one residence rows;
* 69 new residence rows.

Appending relaxed copies to that CNF leaves the original hard rows in
force and does **not** create the proposed optimization problem.  A correct
builder must byte-preserve the desired hard prefix and replace, rather than
duplicate, the 385 hard residence rows.  Whether the two historical
component cuts are retained or topology is handled entirely lazily must be
declared explicitly.

## 5. What bounds are rigorous

Let `b_A(F)` be the number of violated clauses in the current accumulated
bank `A`, and let `s(F)` be the number of physical positive short runs.  On
the authenticated current factor,

\[
             b_A(F)=237,\qquad s(F)=17b_A(F)=4029.
\]

For a future master assignment, `b_A` counts only already discovered
motifs.  A new factor may expose new short-run clauses not in `A`.
Therefore:

1. proof-producing UNSAT for `b_A <= B` is a rigorous lower bound
   `b_A > B`, and hence a lower bound against residence on this catalogue;
2. SAT for `b_A <= B` is not a residence upper bound until the physical
   factor is reconstructed, topology is validated, and all new short runs
   are separated;
3. a connected physical scan with `s(F)` short runs is a genuine upper
   bound on the physical residence objective;
4. `b_A=0` is not residence unless the separation oracle finds no new
   motif.

The factor extractor supports multiple components and can generate new
blockers componentwise.  The transition-gap checker deliberately rejects a
multicomponent factor, so it is appropriate only after the lazy topology
validator has certified one physical cycle.

The positive all-width-upper CEGAR rows are logically compatible with this
soft residence bank: they are simply additional hard clauses on the same
primary variables.  There is, however, an important bound qualification.
The `paired_escape005` incumbent falsifies the 141 upper rows extracted from
it.  Thus `B=237` is a certified feasible bound for the residence/base
factor face, but not for a model in which those current or the cumulative
249 higher-upper rows are already hard.  In that strengthened face, 237 is
only a search bound until a satisfying physical factor is produced.

## 6. Fail-closed audit of the standalone checker

For the two authenticated inputs, the checker is sound: it validates file
opening and numeric parsing, degree two on every encountered owner, one
component, Johnson transitions, and the recorded intersection facet before
performing the two independent scans.

It is not yet a fully fail-closed generic `k=17` factor validator.  In
particular it does not explicitly enforce:

* every mask lies in the low `k` bits (an out-of-range flip index can index
  the event array out of bounds);
* owner rank nine and facet rank eight;
* exactly `binom(17,9)=24310` owners and edges, or every rank-nine owner;
* absence of duplicate/parallel factor rows (the endpoint-to-facet map
  overwrites duplicates).

Those omissions do not affect either frozen replay because their separate
factor audits certify the missing census and palette conditions.  They do
mean that the source should be wrapped by those authenticated checks, or a
new hardened derivative should add them, before calling it a standalone
fail-closed round-two oracle.  The frozen source and hash should not be
silently modified.

### 6.1 Hardened derivative

The frozen source above remains unchanged.  The new derivative

`scratch/audit_middlelevels_flip_gaps_failclosed_20260802.cpp`

has SHA-256

`5a344c4d926507157a595d88b720c95fb3313a1f86941449e70d646da869c398`.

Before either residence scan it now requires all of the following:

* odd `K` in `[1,31]` and every mask strictly below `2^K`;
* owner rank `(K+1)/2` and facet rank `(K-1)/2`;
* exactly `binom(K,(K+1)/2)` factor rows, distinct owners, distinct facets,
  and distinct unordered owner pairs;
* literal Johnson geometry, simple degree two, and one spanning cycle;
* exactly one semantic facet column (`color_mask` xor `facet`), no duplicate
  header name, exact TSV row width, and no terminal empty field.

It then compares the complete per-length insertion--deletion histogram with
the complete per-length direct cyclic-run histogram, not merely their totals.
The authenticated outputs are

| factor | output SHA-256 | short positive runs |
|---|---|---:|
| `c68b.double_fusion` | `f8331c807161247e3845a5c3b4d10225388f2beb6bd35643cb24a335744300fe` | 5,372 |
| `paired_escape005` | `03a50a92cd94b29045f18d46d77290219b485625d607c4323113b29627d344b6` | 4,029 |
| `c16_escape001` | `e502e7b96dc573debb124db8c3443c0419acfa2e84b9dba486fd11279430e0c9` | 3,672 |

The independent mutation/proof audit is

`scratch/ad_k17_flip_gaps_failclosed_independent_audit_20260802.md`

with SHA-256

`7cc8961197adcc2085871b1d0b4bc6a51bc66070153f3f3c6117dcbc0a573b5b`.
It rejects out-of-range, wrong-rank, wrong-count, duplicate/parallel,
duplicate-facet, ambiguous-alias, extra-field, and terminal-empty-field
fixtures.  The derivative is therefore fail-closed for a literal cyclic
middle-levels Hamilton factor.  Its scope is still positive residence only;
it does not certify zero runs, upper decks, an opening, or a compiler.

## 7. Exact boundary

Proved here: the transition-gap identity, the two exact totals, the
`4029=17*237` quotient/physical accounting, exact current violation count
237 in the 385-row bank, and the projected correctness of the soft encoding.

Open: satisfiability at any improved bound, connectivity of a future SAT
assignment, closure under newly exposed residence motifs, simultaneous
higher-upper completion, and every source/compiler gate.
