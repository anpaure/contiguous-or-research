# Section 186 — q369 Hall-zero and two-path factor search

## Scope

This section concerns the canonical single-switch schedule for a hypothetical
length-465 nonzero solution at \(k=11\):

\[
C_i=\bigvee_{p=i}^{i+2}A_p\quad(1\le i\le369),
\qquad
C_i=\bigvee_{p=i}^{i+3}A_p\quad(370\le i\le462),
\]

where \((C_i)\) is a permutation of the 462 rank-six masks.  It does not claim
that every unrestricted optimum must use this exact switch location.

The schedule is nevertheless extremal in a proved sense.  Endpoint saturation
forces at least 93 full-length/full-recency rank-six witnesses in every equality
case, while this schedule has exactly 93.  Its other 369 central witnesses have
defect exactly one, so it saturates the endpoint count.

## 1. The short-cell Hall gate

There are exactly 1023 masks of ranks one through five and exactly 1023 lower
cells left after the 369 short central witnesses are reserved:

\[
465+464+(463-369)=1023.
\]

The exact central envelopes define a bipartite graph from lower masks to
individually legal short intervals.  A legal edge passes all of the following
necessary tests:

1. the interval envelopes can supply every target bit;
2. every position can stay nonzero while its value is contained in the target;
3. the interval does not contain a prescribed central value with an outside
   bit;
4. removing the target's outside bits does not individually erase every pin of
   an intersecting central equation.

Different targets must use different physical intervals.  Hence a perfect
matching is necessary.

All 79 local rank-six rows were scanned.  All 17 rows with no individually
empty target failed Hall, with deficiencies 2 through 7.  Exact lower-factor
CNFs for all 17 were UNSAT, and all DRAT proofs were independently verified.
The full batch and hashes are in
`scratch/certificates/k11_q369_global_factor/batch_zero_empty/`.

The Hall components are not copies of one universal obstruction.  For example:

- `focus14_seed` has two deficiency-one components of sizes \(26/25\) and
  \(27/26\), with common cores 66 and 129;
- `lower956_upper546` has three deficiency-one components of sizes \(16/15\),
  \(19/18\), and \(53/52\), with common cores 276, 74, and 8;
- `lower956_upper541` has components \(17/15\) and \(3/2\).  The latter is the
  nested chain \(11\subset139\subset651\), forced onto only two cells.

Thus `empty_targets=0` checked only the singleton Hall inequalities.  Maximum
matching is the correct cheap global gate.

## 2. Hall zero was reached

A C++ path search was changed to score

\[
(\text{central pin deficit},\ \text{Hall deficiency},\
  \text{upper missing})
\]

before invoking exact SAT.  Starting from the best existing rows, it reached a
perfect \(1023/1023\) matching in seconds.  It subsequently found full-path
Hall-zero rows with 36, 17, 16, and finally 12 missing upper masks.

The upper-12 row has ten missing rank-seven masks and two missing rank-eight
masks.  It improves the previous 13-hole structural checkpoint, but its exact
lower-factor CNF is UNSAT.  The checked formula has 8569 variables and 23947
clauses; its DRAT proof verifies independently.

This settles an important question: ordinary Hall feasibility is not the final
lower-labeling obstruction.

## 3. Exact fixed-matching pin criterion

For a perfect lower-cell matching \(m\), let \(E_p\) be the central envelope at
factor position \(p\).  For each bit \(b\), put

\[
D_b(m)=\bigcup_{S:\,b\notin S}m(S),
\qquad
Z_b(m)=\{p:b\in E_p\}\setminus D_b(m).
\]

The matching is pin-surviving exactly when all three conditions hold:

1. every factor position has at least one surviving bit;
2. every central positive pair \((C_i,b)\), \(b\in C_i\), has
   \(I_i\cap Z_b(m)\ne\varnothing\);
3. every selected lower witness \((S,m(S))\) and every \(b\in S\) has
   \(m(S)\cap Z_b(m)\ne\varnothing\).

Indeed, if these hold, set

\[
A_p=\{b:p\in Z_b(m)\}.
\]

Envelope containment excludes every unwanted central bit; the definition of
\(D_b\) excludes every unwanted lower-target bit; and conditions 1–3 give all
required positive occurrences.  Therefore a matching with zero failed
conditions constructs an exact lower-complete central factor directly.

This supplies a strictly stronger, constructive search score:

\[
(\text{central pin deficit},\ \text{Hall deficiency},\
  \text{matching pin failures},\ \text{upper missing}).
\]

A positive heuristic score is not an impossibility proof, since another
perfect matching may fare better.  A score of zero is a certificate and yields
the factor explicitly.

The search now marks as hot every position occurring in a failed factor,
central, or target pin condition.  This fixes an important bug in the first
Hall-zero run: alternating-Hall reachability is empty at Hall zero, so its path
moves had previously been blind to the true conflicts.

## 4. A certified 60-target pin obstruction

For the Hall-zero upper-17 row, the full exact lower CNF is UNSAT.  Its retained
proof core has 283 input clauses, 77 lemmas, and 416 resolution steps.  The core
uses 72 lower targets, 98 short cells, and 165 target/cell selectors.

Rebuilding the formula with only those 72 targets and greedily deleting targets
produced a certified UNSAT subinstance on 60 targets.  Eight random deletion
orders all ended at size 60.  There are two observed variants; 59 targets are
common and the last target is either 775 or 899.  The final 60-target UNSAT
formula has its own independently verified DRAT proof.  This is a concrete
joint pin obstruction, not an interval-count or Hall failure.

Artifacts are in
`scratch/certificates/k11_q369_global_factor/hall_zero/`, including the full
selector-to-slot map and the two 60-target subinstances.

## 5. Structural correction: two paths, not one

The first Hall search retained an unnecessary invariant: all 462 central masks
formed one rainbow Johnson path.  The saturated schedule naturally splits at
the switch:

\[
P=(C_1,\ldots,C_{369}),\qquad Q=(C_{370},\ldots,C_{462}).
\]

The correct top-layer skeleton is:

- \(P\) is a 369-vertex Johnson path;
- \(Q\) is a 93-vertex Johnson path;
- their 368+92=460 internal rank-five intersection colors are distinct;
- the three maximal endpoint cells are the early pair at start 0 and the late
  triples at starts 369 and 462 (zero based); the two missing rank-five colors
  must match into two of these cells, while the third is the unique omitted
  maximal cell;
- the seam \(C_{369}\mid C_{370}\) need not be a Johnson edge.  A distance-two
  seam has rank-eight union and is a natural upper portal.

The search now preserves these two internal rainbow paths while allowing an
arbitrary seam.  Its moves include within-component reversals and relocations,
plus equal-size block exchanges between the two components.

This correction immediately found Hall-zero rows with non-Johnson seams.  A
rank-eight-seam row reduced the heuristic pin score from 88 to 56; it had 40
upper holes and remained exact-lower UNSAT.  A later endpoint-cut row reached
45 failed target pins and zero failed central pins (with a rank-nine seam and
45 upper holes); its exact lower formula is also UNSAT.  Both checked proofs
are retained as `q369_two_conflict56.*` and `q369_two_conflict45.*`.

For the conflict-45 row, a much deeper matching-only run (256 randomized
perfect-matching restarts and 100,000 alternating-path updates) did not improve
45.  In the retained best matching all failures are positive target pins; none
is a central pin or empty factor position.  Thirty-one of the 45 failed
witnesses begin in the late 93-vertex block, and bit 6 accounts for 13 failures.
This concentration motivated block-aware hot moves rather than more blind
matching randomization.

## 6. Coordinate projection evidence

The upper-17 full-path row passes every projected histogram test on at most four
coordinates but fails exact five-coordinate tests for the zero-based sets

\[
\{1,2,3,4,6\},\qquad \{1,3,4,6,7\}.
\]

The rank-eight-seam two-path conflict-56 row passes both of these exact tests.
Therefore the two-path correction escapes the first known bounded-coordinate
obstruction, even though the complete eleven-coordinate lower formula remains
UNSAT.  The remaining failure has a different or wider coordinate structure.

## 7. Current status and next exact gates

What is now proved computationally for the q369 branch:

- Hall deficiency zero is attainable;
- upper missing 12 is attainable simultaneously with Hall zero in the old
  full-path subspace;
- a rank-eight seam is attainable simultaneously with Hall zero in the correct
  two-path subspace;
- neither Hall zero nor the tested five-bit projections imply global pin
  survival;
- every exact UNSAT claim above has an independently checked DRAT certificate.

The active target is a two-path row with a zero fixed-matching pin score.  Such
a row would immediately yield a 465-entry lower-complete factor.  After that,
the remaining upper masks must be repaired without losing the factor, or the
upper masks can be included directly in the exact universal CNF.

No length-465 universal array is claimed yet, and none of these fixed-schedule
UNSAT certificates excludes an unrestricted optimum.
