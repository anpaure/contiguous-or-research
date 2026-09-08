# Exact-construction 16-lane ledger

Date: 2026-07-27

This ledger is the active research allocation for the exact contiguous-OR
problem.  It is narrower than `CONSTANT_ONE_16_TASK_LEDGER_20260727.md`: every
lane now starts from the certified optima at every (k\le 12), including the
new exact length-465 word at (k=11), and the OR-Pascal analysis in
`EXACT_OPTIMA_BEAUTY_ANALYSIS_20260727.md`.

The governing discipline is:

1. a lane must preserve the exact middle permutation or explain how it is
   replaced;
2. a claimed central path must pass the two-sided shadow and residence audits;
3. a claimed word must pass the full contiguous-OR verifier;
4. finite search output is evidence only when accompanied by a reproducible
   verifier, and UNSAT is a theorem only with an independently checkable
   certificate;
5. no lane may hide a (\sqrt m)-scale loss under depth-by-depth notation.

## Active lanes

| ID | Lane | Exact target | Current evidence | Decisive next test | State |
|---|---|---|---|---|---|
| 1 | Sparse section-overlay connector | Select a Hamilton path from the (k=11) path/(k=12) section overlay with all 461 lower and all 330 upper colours | **Solved at q=1:** a verified path lies in an 827-edge augmentation; lower load (1^{461}), all upper colours, CPCR 54. It has 150 short one-runs | Add delay-three residence without losing either colour marginal | q1 complete; merged into 6 |
| 2 | Residence-compatible diamond lift | Turn the (k\mapsto k+2) four-sector diamond cover into a factorable Hamilton path | **Structural part solved:** one-hole lower rainbowness forces the exact Catalan/ballot block profile and a rainbow all-present forest in every coordinate section | Repair the twelve (k=11) upper colours while retaining the forced braid | theorem complete; merged into 6 |
| 3 | One-boundary-flag tableau | Compile a central path whose lower deficits lie in one nested flag into a length-(B(k)) word | **Solved exactly:** terminal residence gives a necessary-and-sufficient flag criterion; arbitrary prescribed cells reduce to coordinatewise interval hitting | Supply a compatible global set of nonboundary pins | theorem complete; feeds 4 |
| 4 | Bulk first-derivative compiler | Realize a terminal low block while preserving the complete derivative tower | **Finite/special-regime theorem:** a canonical run-alternating core satisfies `DC=DP`, so every `C⊆A⊆P` preserves all higher derivatives. At k=11, literal low masks reduce to 63 quotient surplus-Hall inequalities, minimum margin 2, and produce a cleaner second optimum. A k=7 example proves the boundary is genuine. **Scope correction:** the literal base row already exceeds capacity at k=9 and has `Theta(sqrt(k)W)` targets asymptotically, so this cannot be the uniform compiler | Use it as a terminal recursion block; replace the general lane by multirow interval-label realization | k=11 complete; asymptotic use restricted |

## Near-term supporting lanes

| ID | Lane | Exact target | Why it remains live | Stop condition | State |
|---|---|---|---|---|---|
| 5 | Balanced Hamiltonian transversal | A middle Hamilton path with near-floor load in both edge-colour projections | **Solved end-to-end at k=11.** The translation quotient has 42 variables with 15 choices. A 27,103-variable CNF enforces degree two, cap-two q1 coverage, both q2 shadows, residence through delay three, Hamiltonicity, and nonzero voltage. Kissat finds voltage two; the lift is one 462-cycle with complete shadows at every depth and zero residence defects. **Scaled at k=13:** an affine low-component seed can be broken to a connected voltage-six q1 cycle in 0.62s. A staged q2+h2 solve leaves exactly 27 h3 orbits, five lower-q3 holes, and no upper-q3 holes. Exact recent-insertion/deletion automata encode the joint residual; oriented-lazy connectivity reduces it to 194,463 variables and 1,181,772 clauses. Bounded portfolios are live and no timeout is interpreted as UNSAT | Remove the k=13 27+5 residual and test the depth-d compiler; in parallel prove a prime-uniform rotor/absorption theorem | k=11 complete; k=13 central gate sharply finite; general prime construction open |
| 6 | Coupled (q=1/q=2) repair at (k=11) | Starting from the q1-perfect connector, enforce delay-three residence without losing either colour marginal | Superseded by the exact quotient construction: the final cycle has both q2 shadows complete, cap-two q1, and zero residence defects, and it compiles to the optimal word | Mine the old repair traces only for local moves that generalize the exact quotient solution | **finite lane closed** |
| 7 | Coordinate-section recursion | Convert a two-sided path in (J(2m,m)) to one in odd dimension using (O(W/m)) joins | Lemma 9.1 gives one-sided-perfect forests; coordinate 12 has only 25/26 components | Coloured connector theorem with (O(W/m)) edits | parked |
| 8 | Catalan/ballot section recursion | Exploit the complete all-subset block profile forced by a one-hole lower-rainbow path | **Static structure solved:** upper loads are one weighted excess design; CPCR is its factorial energy; every nonexceptional t-section has exact mean block length r/t; all deeper incidences are Boolean transforms of truncated local times | Construct a low-discrepancy hazard schedule with rate t/r and a near-simple excess design | theorem complete; construction open |
| 9 | Boundary-factor cell order | Characterize which nested flags can be fed through the (d) extra entries | Known exact tableaux use the boundary cells as the only nonuniformity | A flag that passes capacity but cannot be realized locally | parked |
| 10 | Antipodal explicit constructor | Turn the known ((\sqrt2+o(1))W) complement-bridge construction into a simple deterministic program and identify reusable motifs | Gives the best fully explicit asymptotic baseline | No motif survives the OR-Pascal projection | parked |

## Global theorem lanes

| ID | Lane | Exact target | Interface to finite beauty | State |
|---|---|---|---|---|
| 11 | PBBS/coherent-transition carrier | Turn an exactly balanced finite-memory carrier into a globally glued rotor | Local q1/q2 packing is asymptotically solved, but chronology requires `Gamma=0`. **Finite coherent absorption succeeds at k=11:** a 17-orbit circuit produces one voltage-two Hamilton lift with all shadows and zero residence-3 defects. **The next calibrated carrier is k=15:** all depths are hole-free, with 73 physical components, five q1 load-three orbits, 90 forward-residence defects, and 945 co-residence defects. Two size-five load-three orbits are forced by Z15 symmetry, so cap two is not a valid requirement. Three static matchings independently solve its entire lower anchor gate with exact slack 2928. Cycle-space/LNS searches are active | Produce a chronology-aware circuit sequence merging k=15 while preserving the tower and forward residence; treat co-residence as the stronger optional 15-to-16 target | k=11 coherent bridge solved; k=15 exact finite carrier search active; general absorber open |
| 12 | CPCR all-depth compiler | Produce floor-corrected load error (o(W)) after bundling | Finite optima nearly attain the integrality floor at each audited depth | parked |
| 13 | Exact formula lower-bound strengthening | Prove (\nu(k)\ge B(k)) is the whole obstruction, or discover a new invariant | A short monotone-deadline proof now gives \(\nu(k)\ge B(k)\) directly. Its exact slack identity splits the deficit into unused deadline depth and repeated lower cells; only zero slack forces a flat central row. Full witness retiming has an exact coordinatewise test, while the optimal k=4 counterexample rules out unconditional flatness | lower theorem complete; exchange axioms open |
| 14 | Compensation/Dirichlet hierarchy | Close the final centered-variance term in the stochastic compiler | The hierarchy has collapsed to one quantitative inequality | parked |
| 15 | Decorated carrier cycles | Produce abundant carriers with a globally compatible wreath decoration | Separates “objects exist” from “decoration is compatible,” the recurrent global gate | parked |
| 16 | Known Gray/SCD and odd-even interface | Import tight enumerations, middle-level cycles, SCDs, and dimension lifts without losing residence | Provides exact one-sided or unbundled analogues. The shared-tail lift is now exact: equal depths are necessary, but sufficiency additionally requires a dual erosion (both runs and gaps at least d+1), a matching d-cell boundary, and complete marked seam coverage. This rules out automatic 11-to-12 and 13-to-14 lifts and shows 15-to-16 is conditional on a new bi-resident rotor | conditional theorem complete; bi-resident construction open |

The uniform compiler target replacing the over-strong reading of lane 4 is
the exact multirow system in
`MATH_BULK_COMPILER_SCOPE_AND_MULTIROW_FRONTIER_20260727.md`: distribute all
lower masks across rows `0,...,d-1` using the rank-quantile capacities, then
satisfy the coordinatewise full interval-label criterion.  This is the
actual general form of lanes 3, 4, 9, and 13.

A depth-`d` sandwich theorem now protects the central rotor without freezing
those lower rows: choose a sparse `C subseteq P` with `D^dC=D^dP`; then every
`C subseteq A subseteq P` has the same middle and upper tower.  At `k=11`
its 3,784-variable multirow compiler solves in 0.004 seconds and produces a
third verified optimum whose `D^1` contains eight rank-three masks.  This is
the active uniform form of the compiler lane.

## Current synthesis

The exact answers, now including the formerly missing (k=11) case, point to
one construction class:

\[
\boxed{\text{Pascal-compatible bundles of inclusion chains whose middle row is a
two-sided, residence-constrained Johnson Hamilton path.}}
\]

At (k=11) all three clauses have now been realized simultaneously:

- the quotient cycle has exact two-sided colour balance through every depth;
- residence holds cyclically through the full deadline (d=3);
- every safe cut passes flat-D3 Hall, and a boundary flag plus a 231/231
  residual matching produces the universal 465-word.

At general (k), the short rows have an exact rank-quantile polytope and the
odd central path has an exact Catalan/excess-design dual.  The new finite
certificate shows that their compatibility is real, not merely separately
feasible.  What remains is to turn the 42-orbit phenomenon into a uniform
central construction **and** realize the lower quantile schedule across all
short derivative rows.  A one-row Hall compiler cannot absorb that second
task asymptotically.  This corrected pair is now the common core of the
conjectural identity (\nu(k)=B(k)).

## Verified finite baselines

- (\nu(k)=B(k)) for every (k\le 12).  The new k=11 certificate has length
  465, covers all 2047 nonempty masks, and has SHA-256
  `746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850`.
- From (k=6) onward every informative stored answer has a complete central
  derivative row.
- Two independent optimal `k=11` words verify the result.  The cleaner bulk
  tableau has `D0=(1^11,2^57,3^397)`, `D1=4^464`, `D2=5^463`, and
  `D3=6^462`; its SHA-256 is
  `bda651d3e40d0920d3e6ed12e6a2091e477695d8ad7f6bd186b831f087cf136a`.
- The (k=12\to11) coordinate section gives a 436-edge upper-perfect forest
  with 26 components.
- The raw 532-edge (k=11/k=12) overlay is impossible under the exact
  one-lower-colour/degree-two constraints because of six forced degree-three
  vertices.  This is a local obstruction, not evidence against a small
  reservoir.
- An 827-edge augmentation contains a certified q1-perfect Hamilton path.
  Staged q1-preserving descent leaves only ten q2 residence witnesses; they
  are pairwise disjoint, forcing any one-shot q2 repair to use at least ten
  cuts.
- The first explicit ten-cut instance has only the inert deleted matching;
  a successful instance must expose a nontrivial rainbow alternating circuit.

## Required artifacts from an active lane

Each active lane must return at least one of:

1. a theorem with a complete proof;
2. a verified exact construction plus a short certificate/checker;
3. a statewise obstruction stated independently of the attempted algorithm;
4. a strictly smaller, quantitatively exact gate with all loss terms exposed.
