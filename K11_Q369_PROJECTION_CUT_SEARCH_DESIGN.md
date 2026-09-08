# Exact coordinate-projection cuts for the q369 two-path search

## 1. Purpose

The current path search minimizes pin failures for one heuristically chosen
perfect lower-cell matching.  A positive score is not an obstruction: another
matching or a genuinely non-matching factor assignment may work.

For a coordinate set `H`, the exact projected lower problem existentially
quantifies every factor bit on `H`.  If that problem is UNSAT, the row is
impossible independently of every matching choice.  This note supplies a
compact exact CNF for that projection and a lazy cutting-plane hook for
`k11_q369_hall_search.cpp`.

It also incorporates the proved q369 second-shadow cut

```text
|{C_p intersect C_(p+1) intersect C_(p+2):
      p=0..366 or p=369..459, rank=4}| >= 323.
```

The latter is checked in-process on every proposed path move.

## 2. Exact projected problem

Fix `H subseteq [11]`, `h=|H|`.  A projected factor is a word

```text
x_0,...,x_464 in 2^H
```

satisfying the projected central equations

```text
OR_(p=i..i+2) x_p = C_i intersect H       (i<369),
OR_(p=i..i+3) x_p = C_i intersect H       (i>=369).
```

The 1023 residual short cells are all 465 singletons, all 464 pairs, and
the 94 triples starting at positions 369 through 462 (zero based).  For a
projected pattern `P subseteq H`, put

```text
m_H(P)=#{S subseteq [11]: 1<=|S|<=5 and S intersect H=P}.
```

Every exact lower factor must make the multiset of projected ORs of those
1023 cells contain `P` exactly `m_H(P)` times.

### Projection theorem

The formula emitted by `k11_q369_projection_cnf.cpp` is SAT if and only if
such a projected factor exists.

**Proof.**  The first `465h` variables are the factor bits.  The central
clauses impose the displayed OR equations exactly.  Every residual cell has
one selected projected pattern, and the selector implications make its OR
equal that pattern coordinate by coordinate.  For every pattern, a unary
counter imposes an upper capacity `m_H(P)`.  There are exactly 1023 cells and

```text
sum_P m_H(P)=1023.
```

Therefore exact-one selection at every cell and all upper capacities force
every pattern count to equal its capacity.  Conversely, any projected factor
with the required histogram selects its actual pattern at every cell and
satisfies every counter.  QED.

Thus UNSAT is a sound row rejection.  SAT is only a necessary relaxation
unless `H=[11]`; omitted coordinates and their joint pin conflicts remain.

`k11_q369_projection_verify.cpp` independently reads the first `465h` model
variables and checks every central OR and the complete 1023-cell histogram.
Its `--factor` mode checks a retained 465-entry compact projected factor
directly, so large CNFs and DIMACS models need not be kept for SAT witnesses.

For the original SMT encoding, `k11_q369_multibit_projection_smt.cpp --model`
emits all factor-bit values and `k11_q369_projection_smt_verify.cpp` parses the
Z3 output and performs the same independent semantic checks. This closes the
gap between a bare `sat` line and a retained, inspectable projected factor.

## 3. Why a bank of minimal failures is the right score

Projection feasibility is monotone: if `H` is UNSAT, every superset of `H`
is UNSAT.  Start with the known eleven-coordinate UNSAT row and delete
coordinates while SAT/UNSAT is preserved.  Inclusion-minimal failing sets
form exact learned cuts.

For a finite bank `B` of such coordinate sets, define

```text
projection_failures(C)=#{H in B: projection(C,H) is UNSAT}.
```

This score is independent of a lower-cell matching.  Zero means the row has
escaped every learned exact obstruction; it does not assert global SAT.
When a zero-bank row remains globally UNSAT, minimize a new failing projection
and append it to the bank.  This is an ordinary exact cutting-plane loop.

## 4. Lazy integration into the path search

Calling SAT on every local move is too expensive.  The patched search uses
two levels:

1. Every move is filtered by the exact structural gates, including
   `D3>=323`, and evaluated by the existing Hall/matching score.
2. An external exact projection hook is called only for a cheap-score
   improvement or periodically for a candidate within eight matching-pin
   failures of the current record.

Set

```bash
export Q369_PROJECTION_HOOK='/root/q369/projection_bank_score.sh \
  /root/q369/k11_q369_projection_cnf kissat /root/q369/projection.bank'
export Q369_PROJECTION_PERIOD=250
```

The search writes the candidate row to a unique temporary file and appends
that path to the hook command.  The hook prints one nonnegative integer.  In
the record comparator, exact projection failures precede the heuristic
matching-pin score:

```text
central factorability,
D3 hard-cut deficit,
Hall deficit,
exact projection failures,
fixed-matching pin failures,
D3 coverage tie-break,
upper holes, ...
```

Projection is deliberately absent from the inner annealing energy because
most rows have not been sent to the oracle.  Several worker threads can keep
exploring while one worker blocks on an elite exact check.

The hook implementation is `scratch/q369_projection_bank_score.sh`.

## 5. Remote discovery workflow

Compile on a RunPod, not on the Mac for sustained work:

```bash
g++ -O3 -std=c++20 k11_q369_projection_cnf.cpp -o q369_projection_cnf
g++ -O3 -std=c++20 k11_q369_projection_verify.cpp -o q369_projection_verify
g++ -O3 -std=c++20 -pthread k11_q369_hall_search.cpp -o q369_hall_search
```

For all one-coordinate deletions, use
`scratch/run_q369_projection_deletions.sh`.  If an h=10 projection is UNSAT,
repeat inside it at h=9, then h=8, until every one-coordinate deletion is SAT.
Put the resulting minimal set on one line of `projection.bank`.

For an independently checked SAT result:

```bash
q369_projection_cnf ROW projection.cnf BITS...
kissat projection.cnf > projection.model
q369_projection_verify ROW projection.model BITS...
```

For UNSAT claims intended as certificates, retain the CNF, a proof-producing
solver trace, and an independently checked DRAT/LRAT proof.  A timeout is
neither SAT nor UNSAT and the hook treats it as an error, not a score.

## 6. Current evidence

* The faithful conflict-45 two-path row has `D3=328`, so it passes the new
  exact `323` cut.
* Exhaustive SMT over all `C(11,5)=462` five-coordinate subsets is SAT for
  that row.  Hence its first projected obstruction, if below dimension 11,
  is at dimension at least six.
* The older upper-17 full-path row fails two known five-coordinate sets.  The
  faithful two-path correction escapes them.
* Compact projected factors now certify **all eleven** ten-coordinate
  deletions of the conflict-45 row. They are retained under
  `scratch/certificates/k11_q369_global_factor/hall_zero/`
  `conflict45_h10_projections/` and each passes an independent semantic
  checker.
* Consequently every proper coordinate projection of this row is SAT, while
  its full eleven-coordinate formula has a verified DRAT refutation. Its
  remaining lower-factor obstruction is therefore irreducibly
  eleven-coordinate with respect to coordinate deletion.

These facts also delimit the method: bounded-coordinate projections were a
real guide from the upper-17 row to the two-path space, but for the conflict-45
row the first obstruction is all eleven coordinates. No bounded projection
bank can distinguish or repair this particular frontier row; the next exact
score must expose a genuinely global all-coordinate conflict or use a
different row move family.

## 7. Global fallback: minimum lower-mask drops

The coordinate-cut hierarchy has now been exhausted on the conflict-45 row.
The next faithful scalar diagnostic is the least number of rank-one-through-
five masks that an exact factor must omit. The drop encoding and its proof are
documented in `K11_Q369_MIN_DROP_DIAGNOSTIC.md`; unlike one chosen matching's
pin count, this quantity optimizes over all factor labels and all short
witness choices.

`scratch/q369_min_drop_score.sh` makes that diagnostic usable through the
existing lazy external hook. For example:

```bash
export Q369_PROJECTION_HOOK='/root/q369/q369_min_drop_score.sh \
  /root/q369/q369_factor kissat 4 45'
export Q369_PROJECTION_PERIOD=250
```

The final candidate-row path is appended automatically. The script tries
`q=0,1,...,4`; its first SAT value is an exact minimum when every lower query
returned UNSAT, and otherwise is only a sound upper bound because a timeout
is never treated as UNSAT. This hook should remain lazy: even these small
formulas take row-dependent time, and both search workers must not spend their
entire budget waiting on SAT.

### Observed exact plateau

The diagnostic changes the interpretation of the matching search:

* the retained conflict-38 row has exact minimum drop `2` although its old
  matching score was 38;
* the refined D3=330 row reduced the matching score to 10, but its certified
  exact minimum remained `2`;
* the subsequent conflict-9 row again has minimum drop `2` in the discovery
  run (`q=0,1` UNSAT and `q=2` SAT).

Thus the 38-to-9 matching improvement did not reduce the true lower-factor
distance. Matching pressure remains useful for producing structurally varied
rows, but is no longer a faithful primary objective.

Target-guard assumptions were also tested as a possible exact local heat
source. On the conflict-9 row, CaDiCaL's initial failed core had 646 of the
1,023 lower targets. Exact deletion minimization took 11,992 incremental
solves and stopped at an inclusion-minimal 480-target core, spread across all
five lower ranks. This obstruction is too diffuse to define a useful local
move neighborhood. The next feedback mechanism must preserve more geometry
than coordinate subsets or target groups—for example factor-position pin
provenance, or an exact row move that repairs a decoded two-drop factor.
