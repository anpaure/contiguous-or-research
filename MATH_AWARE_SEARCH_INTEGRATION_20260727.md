# Math-aware search integration

Date: 2026-07-27

## Purpose

The search code now distinguishes three logically different objects:

1. a final exact wreath factor;
2. a reachable sequential packet state; and
3. a decorated recharge carrier.

The previous searches often used a statistic from one category as a proxy for
another.  The latest mathematics proves that those substitutions are invalid.
This integration records the exact objectives and supplies common executable
evaluators.

## Shared exact evaluators

`scratch/math_aware_search_metrics.py` contains:

* the balanced integer quota and the true overload (O_q);
* the weighted MWB objective (sum_q O_q/c_q);
* the CPCR identity
  
  \[
  E_q-E_q^{\min}
  =2\sum_T\binom{L_q(T)-c_q}{2};
  \]

* the phase-capacity diagnostic PCap;
* the exact Johnson residence certificate
  (a_i=d_{i+m}), which is stronger than distinct deletions;
* the remaining conditional common-child Dirichlet kernel;
* exact one-bite/whole-bite stopped-profile loss, including same-bite
  coalescence and its reachable pair-energy upper bound; and
* exact column-multiset signatures for decorated recharge.

`scratch/test_math_aware_search_metrics.py` tests all identities, including the
five-vertex distinct-deletion/non-wreath counterexample.

## Exact-wreath switch search

`scratch/check_wreath_shadow_switches.py` now supports

```text
--math-greedy mwb|cpcr|lex
```

Every accepted state is still an exact factor into length-(2m+1) odd cycles,
so wreath validity is a hard constraint.  The primary `mwb` key is the theorem's
actual weighted (L^1) quantity.  CPCR, total (L^1), and holes are only
tie-breakers.

`scratch/search_wreath_math_objective.py` adds tabu/annealed exploration of
worsening and plateau moves.  This is necessary because the archived notes
prove that both hole-greedy and CPCR-greedy order-eight searches have positive
local minima.

As a regression/integration check, the new search found at (m=4)

\[
\sum_q O_q/c_q=2,
\]

improving the archived full-cover factor's (10/3).  Its only defect is
(O_2=6), with (c_2=3); depth one and every deeper audited rank are exactly
balanced.  The emitted 48-switch path is replayable from the MSW factor.

`scratch/audit_wreath_multidepth_energy.py` now computes its legacy energy
through the common CPCR evaluator.  This exposed and corrected one stale
assertion: the archived (m=5) depth-one local minimum has seven depth-two
holes, although its stored CPCR vector was already correct.

## Reachable packet search

`scratch/search_reachable_bites.py` ranks legal bites by the exact functional

\[
L_{\mathcal M}(\mathcal B)
=\sum_d(c_d-Z_d).
\]

The input contains one common selected packet family across all depths.  It is
therefore impossible for this procedure to score the independently chosen
floor-perfect profiles ruled out by the arbitrary-state no-go.  The output
also includes old--new repeats, same-bite coalescence, and the reachable
common-interval pair bound.

The whole-bite optimizer now has three exact modes:

* `enumerate` lists small bites;
* `bnb` maximizes fresh coverage with a dependency-free branch-and-bound; and
* `kissat` binary-searches the optimum with exact cardinality, entrance
  matching, and coverage clauses.

Optional `legal_entrance` data makes entrance disjointness a hard constraint,
not a post-hoc filter.  `--emit-lp PREFIX` writes the exact fractional maximum
fresh-union primal and the audited dual

\[
 \min\left\{\sum_v a_v+\sum_h(1-p_h)+s z:\
 z+\sum_{v\in e_0}a_v\ge\sum_{h\in e}p_h\right\}.
\]

`scratch/whole_bite_optimizer.py` also verifies rational dual certificates.
Thus a static pair-energy score is used only as an upper bound; the actual
reachable integral optimum and the fractional obstruction now have separate,
explicit interfaces.

## Conditional spectral stop

`scratch/score_cooccurrence_kernel.py` evaluates

\[
{1\over r}\sum_y
 \operatorname {Var}_{p}
 \left(a\mapsto {d_t(S,a,y)\over\mu_{S,a}}\right).
\]

This is the exact stochastic term not paid by PPS, PFS3, theta, or whole-arm
PSF.  It must be recorded along the actual trajectory.  It is not a static
pruning theorem: an abstract block design satisfies all earlier marginal
bounds while making this kernel too large.

### Moving-shore boundary covariance

The later edge-only Doléans audit proves that the centered kernel by itself is
not the trajectory gate.  `scratch/math_aware_search_metrics.py` therefore
also exposes `moving_shore_generator_stats`.  For every explicit selected
event it records, exactly,

\[
-\mathcal D_S(g),\qquad 2\delta_gH_g,\qquad
\|h_g^\circ\|_2^2,\qquad
{d_gH_g^2\over P_SP_g}.
\]

The output contains both the signed generator

\[
-\mathcal D_S(g)+2\delta_gH_g+\|h_g^\circ\|_2^2
\]

and the sharp sign-free ASE--CHD upper bound.  The scorer never replaces one
by the other.  `scratch/score_cooccurrence_kernel.py` accepts an explicit
`values`/`weights`/`events` trajectory snapshot and emits this full ledger in
addition to the legacy centered diagnostic.  Its regression suite includes
the exact two-child obstruction where the centered square is zero but the
true generator is positive.

This changes the search contract: a state may be ranked as a stochastic
compensator only from the full moving-shore certificate.  Static centered
co-occurrence remains a diagnostic and may not be used as a proof-preserving
pruning rule.  Hereditary Hall/load coherence remains a separate gate.

## Fixed-slot MSW compensation layer

The slot-two layer is no longer a finite pattern used as a heuristic.  The
marked-\(\Gamma\) collar theorem proves for every \(m\)

\[
\Gamma_{m,2}=3C_{m-2},\qquad \Delta\mathrm{CPCR}_1=-C_{m-2}.
\]

`scratch/msw_slot2_symbolic_compensation.py` supplies the symbolic
certificate, and the fixed-slot searches put this proved shore first while
still replaying every resulting exact factor.  Deeper-rank scores remain
empirical: the bounded contextual packet ceiling forbids promoting this one
layer into a Gaussian-band theorem.

## Residence and the H-safe fork

`scratch/audit_johnson_residence.py` prevents a length-(n), fresh-deletion
Johnson cycle from being silently counted as a wreath.  Search may keep an
`H-safe` auxiliary state, but a final certificate must either pass the exact
residence check or include a separately verified (o(W))-cost repackaging.

## Exact prime-quotient sigma state

### Exact k=11 closure

This lane is no longer merely a search contract at (k=11).  The exact model
in `scratch/sigma_sat_solver.py` selects one of 15 extensions on each of the
42 translation orbits and simultaneously enforces cap-two q1, both q2
shadows, delay-three residence, quotient Hamiltonicity, and nonzero voltage.
The resulting voltage-two lift has complete shadows at every depth.  The
flat-D3 Hall compiler emits the independently verified 465-entry universal
word `scratch/sigma_sat_k11_465.word`.  Thus the finite gate is solved; the
section below now specifies the general prime construction and the next
(k=13) test.

For odd (k=2r-1), the immediate two-sided central gate is encoded by one
map

\[
 \sigma:\binom{[k]}{r-1}\to\binom{[k]}{r+1},\qquad X\subset\sigma(X).
\]

The search state must enforce three logically separate predicates:

1. every lower vertex chooses exactly one value of σ;
2. every rank-(r) vertex has degree exactly two in the induced
   middle-level graph; and
3. every rank-((r+1)) colour is used at least once.

Connectedness and quotient voltage are global terminal predicates, not soft
scores.  For prime (k=11), translation reduction gives exactly 42
multiple-choice variables with 15 values, 42 middle-degree equations, and 30
upper-coverage inequalities.  The relaxed degree-two/surjective instance is
already realized by complemented PBBS, so a future solver must not report
that relaxation as progress.  The first unresolved q1 certificate is one
quotient cycle of nonzero voltage; cap two is an additional CPCR-zero target,
not a consequence of coverage.

The same σ state determines the higher central shadows.  Along the selected
cycle,

\[
 U_i^{(2)}=\sigma(X_i)\cup\sigma(X_{i+1}),
\]

and delay-(d) residence is the hard local constraint that an inserted
coordinate is not deleted in the next (d) transitions.  Therefore q2
coverage and residence must be evaluated on the actual cyclic chronology;
they may not be inferred from q1 marginals or from scalar slack.

At (k=11), a nonzero-voltage quotient cycle makes this completely finite.
There are 126 residence inequalities and 15 q2 orbit-colour coverage
constraints.  Any short residence run has eleven disjoint translates, so a
single cut cannot repair it.  Once all residence tests pass, each of the 42
quotient cut types has exactly nine compatible endpoint flags.  A terminal
cut is accepted only if its q1 colour is repeated and the two removed q2
windows are nonessential at their exact physical targets.  Quotient coverage
alone does not guarantee such a common cut.  In the exact cap-two
certificate there are 242 physical safe cuts, and every one has flat-D3 Hall
deficiency zero; cut 1 with flag
(155\supset154\supset152) compiles completely.  By contrast the older q369
schedule has Hall deficiency 4--9 on the same cycle, so the schedule
distinction is mathematically real.

## Quota-aware diamond and exact portal constraints

The prescribed-load diamond search has a proof-safe five-part formulation:
besides lower, upper, and the two middle-clone parts, every selected diamond
uses a labelled slot for its exchanged coordinate pair.  For the random
prime-orbit Catalan design this hypergraph is asymptotically regular with
maximum codegree (O(R/r)), and a fixed-uniformity nibble gives a
near-perfect matching with a uniform unused quota margin.  Search may use
this as a starting catalogue, but a terminal coverdown must separately
certify

\[
 \text{incidence-Hall expansion}
 \quad\text{and}\quad
 \text{labelled quota circulation}.
\]

Negative pair defect alone is not an absorber certificate.

For PBBS cycle joining, every fixed-core marginal-preserving trade is
generated integrally by the (K_4) alpha triangles.  The alternating PBBS
component is untouched by all static alpha charts, both boundary (K_4)
transports, the canonical (K_5) pentagon, and every changing-core two-alpha
commutator.  The lower bound of three formal alphas is sharp: an explicit
fork of two supply alphas followed by one portal alpha is a simple
(7\leftrightarrow7) trade that opens both alternating ports while preserving
the complete q1 marginal vector.  This move is labelled rather than
equivariant.  Its eleven translates are a valid equivariant sigma-CSP move,
but quotient component merging, voltage, residence, and q2 must all be
checked explicitly before it is scored as global progress.

## Retired projective-atlas family

Exact local projective charts do attain zero local factorization defect, but
their global cocycle equations are inconsistent for every prime-power
(r\ge7).  Completed-row signs force either pairwise sign reversal on a
triangle or a two-clique graph with more functional arcs than are available.
The flat-coordinate, affine-curved, and projective exact-local atlas families
are therefore closed.  Search should not enumerate more gauge choices inside
that family; any atlas successor needs a different completed-row sign
profile.

## PBBS-to-wreath rebundling

`scratch/audit_pbbs_to_ordinary_bridge.py` evaluates the exact coupling

\[
\mathfrak C^{\rm ord}
=\mathfrak C^{\rm PBBS}_{\rm live}
 +\mathfrak R_{\rm mort}
 +\mathfrak B_{\rm ext}
\]

on literal PBBS and ordinary factors.  It also audits the complete 45-switch
\(KG(9,4)\) path and confirms that both component count and live shadow loss
must be allowed to worsen temporarily.

`scratch/search_pbbs_wreath_bridge.py` therefore searches the hard state
space directly: spanning Kneser 2-factors with point-regular components,
under physical alternating \(C_8\) switches.  It emits independently
replayable certificates.  This produced a new exact \(m=5\) bridge of 303
switches from canonical PBBS to 42 wreaths; see
`PBBS_WREATH_BRIDGE_11_5_CERTIFICATE_AUDIT_20260727.md` and
`scratch/pbbs_m5_wreath_bridge_certificate.json`.

The endpoint-proximity lane is now a separate exact-cover objective.  The
weight of a candidate wreath is its number of retained PBBS factor edges;
maximizing total weight over an exact middle-owner cover is exactly minimizing
the PBBS edge-edit distance.  `scratch/census_pbbs_wreath_overlap.cpp` emits
the complete finite catalogue and
`scratch/solve_pbbs_wreath_overlap_threshold.py` tests high-overlap
subcatalogues.  This separation matters empirically: the current closest
verified `m=5` factor has PBBS distance 267 but worse MWB/shadow loss than the
distance-306 endpoint used by the exact switch bridge.

### Return cuts and globally chosen sewing

The later PBBS proximity lemma is now executable in
`scratch/pbbs_wreath_search_metrics.py`.

* `minimum_distinct_label_cut_certificate` reconstructs an optimal cyclic
  deletion set, rather than returning only its cardinality.
* `consecutive_return_arcs` and
  `maximum_disjoint_return_arc_packing` emit the checkable circular-arc dual
  certificate

  \[
  \nu(\mathcal R)\le\kappa\le\nu(\mathcal R)+1.
  \]

* `fragments_from_cut_certificate` turns the cuts into literal PBBS paths and
  verifies that every retained run has distinct omitted labels.
* `enumerate_sewing_candidates` accepts a packet only after its endpoints
  form a literal length-\(2m+1\) odd-graph cycle with all omitted labels
  distinct.  Thus an H-safe Johnson path is never silently promoted to a
  wreath.

Choosing one optimal cut set before sewing is too restrictive.  At \(m=5\),
the canonical optimal cuts leave 54 of 59 fragments in no legal sewn packet.
The stronger interface `label_simple_path_pool` therefore enumerates all
physical label-simple PBBS runs first.  Exact cover then chooses the cuts and
the sewing simultaneously.

This generator has an exact finite calibration.  At \(m=5\):

\[
\begin{array}{c|rrrr}
\text{PBBS overlap}&8&9&10&11\\ \hline
\text{path-sewn wreaths}&2706&374&22&3.
\end{array}
\]

These are exactly the counts from the independent exhaustive enumeration of
all \(10!/2\) geometric wreaths.  Two runs reproduce the complete
overlap-at-least-9 catalogue (399 wreaths); three runs reproduce the complete
overlap-at-least-8 catalogue (3105 wreaths).  In general, a wreath retaining
at least \(h\) PBBS edges has at most \(n-h\) common-edge paths, so the path
generator is exact at a requested overlap threshold without enumerating all
wreaths.

`scratch/solve_pbbs_wreath_overlap_threshold.py` now uses this path generator
by default.  It also reports

* the exact return-cut lower bound on PBBS distance;
* the remaining distance gap of any feasible factor;
* terminal MWB, CPCR, and PCap statistics; and
* optional maximum-retention primal/dual LP files via `--emit-lp`.

The threshold-8 catalogue remains exact-cover UNSAT.  This is not a failure of
the generator: it is the same verified finite integrality obstruction as the
factorial census, now reached from the structural normal form.

### Target-free bridge objective

`scratch/search_pbbs_wreath_bridge.py` now supports
`--objective structural`.  Every state is scored by the exact tuple

\[
(\text{unresolved owners},\ \text{lattice upper bound},\ \kappa,\
  |\#\mathrm{components}-C_m|,\ \text{component-length }L^1),
\]

with stopped-profile trace loss retained as a soft diagnostic.  The existing
target and hybrid modes remain available.  Certificate verification now
recomputes the return-cut/packing bounds and, at a terminal wreath factor,
the full MWB/CPCR/PCap vector.  Merge, component-neutral reorder, split, and
temporary trace-worsening moves are all still legal; none of these metrics is
used as a monotone pruning theorem.

The lattice upper bound is generated by
`n_spaced_lattice_cut_certificate`: one cut every (n) PBBS edges, followed
by the exact greedy line-interval repair inside each block.  The proved
reduction

\[
\kappa(F_{\rm PBBS})
\le C_m+\sum_{D\in\mathcal D_m}e_m(D)
\]

is documented in
`MATH_LEMMA_PBBS_N_SPACED_LATTICE_CUT_REDUCTION_20260727.md` and audited by
`scratch/audit_pbbs_unit_window_lattice.py`.  The missing assertion is the
uniform Catalan mean bound \(\sum_De_m(D)=O(C_m)\); the finite data do not
prove it.

## Decorated carriers

`scratch/search_decorated_signature_pairs.py` groups six-row carrier tables by
their exact column-multiset signatures and emits only top-disjoint pairs in the
same fibre.  It deliberately does not reward uncoloured cycle rank.  Random
word tables have (Theta(mN)) uncoloured carrier rank but, with high
probability, no decorated repaired packet at all.

The next deterministic generator should therefore search directly inside a
compressed signature fibre, or construct two tables simultaneously with one
shared column assignment.  Generating random cycles and testing decoration
afterward is retired.

## Retired search rules

The following are no longer valid pruning or success criteria:

* independent rankwise floor balance;
* raw holes alone;
* uncentered (L^2) energy across the plateau;
* PPS/PFS3/theta as a substitute for the conditional child kernel;
* uncoloured carrier cycle rank as a proxy for decorated circulation;
* fresh deletions as a proxy for wreath residence;
* random phases or random words as a likely source of compatibility; and
* local greedy descent without plateau/worsening moves.

## Verification commands

```bash
python3 scratch/test_math_aware_search_metrics.py
python3 scratch/check_wreath_shadow_switches.py --regression
python3 scratch/audit_wreath_multidepth_energy.py
python3 scratch/audit_johnson_residence.py \
  scratch/fixtures/johnson_residence_example.json
python3 scratch/score_cooccurrence_kernel.py \
  scratch/fixtures/cooccurrence_two_blocks.json
python3 scratch/search_reachable_bites.py \
  scratch/fixtures/reachable_bite_example.json --bite-size 2
python3 scratch/search_reachable_bites.py \
  scratch/fixtures/reachable_bite_conflicts.json --bite-size 2 --backend kissat
python3 scratch/search_decorated_signature_pairs.py \
  scratch/fixtures/decorated_signature_example.jsonl
PYTHONDONTWRITEBYTECODE=1 python3 scratch/search_pbbs_wreath_bridge.py \
  --verify scratch/pbbs_m5_wreath_bridge_certificate.json
PYTHONDONTWRITEBYTECODE=1 python3 scratch/audit_pbbs_distinct_label_cuts.py \
  --m-min 2 --m-max 8
PYTHONDONTWRITEBYTECODE=1 python3 scratch/solve_pbbs_wreath_overlap_threshold.py \
  --m 5 --threshold 9 --generator paths
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/verify_pbbs_path_catalogue_against_exhaustive.py \
  --m 5 --threshold 9
PYTHONDONTWRITEBYTECODE=1 python3 \
  scratch/search_pbbs_factor_trades.py \
  --verify scratch/m5_known_factor_best_trade_round7wide_certificate.json
PYTHONDONTWRITEBYTECODE=1 python3 scratch/audit_msw_adjacent_carriers.py \
  --m-min 3 --m-max 8
PYTHONDONTWRITEBYTECODE=1 python3 scratch/search_wreath_carrier_closure.py \
  --verify scratch/m5_carrier_beam_best_certificate.json
```

## Exact support-matched trade search

The exact-cover layer now has a structural decomposition mode.  For a base
factor \(F\), `scratch/search_pbbs_factor_trades.py` enumerates closed pairs
\((R,A)\) satisfying

\[
\bigsqcup_{C\in R}\mathcal M(C)
=\bigsqcup_{C\in A}\mathcal M(C).
\]

It chooses the removed base blocks and alternative wreaths simultaneously,
and it verifies support equality before scoring the terminal factor.  This
is strictly stronger than testing one supplied factor at a time and far more
focused than a global SAT call.

The first application produces a new exact \(m=5\) factor with weighted MWB
\(547/8\), CPCR 486, balanced \(L^1=167\), and PCap zero at every audited
depth.  Exhaustive trade enumeration proves it is optimal for weighted MWB
inside the 114-wreath union of the six previously known factors.  Conversely,
the complete overlap-at-least-eight path catalogue contributes no closed
trade of size at most six around the nearest-PBBS factor.  Thus future search
should generate candidates by support closure and shadow gain, not by a
uniform PBBS-overlap threshold.

The support-closure generator has since been made catalogue-free at bounded
trade size.  `scratch/census_wreath_base_block_signature.cpp` enumerates all
geometric wreaths touching at most \(K\) current base blocks, which is the
complete candidate set for trades removing at most \(K\) wreaths.  Exact
descent through \(K=4\) gives

```
scratch/m5_entire_universe_four_block_mwb_round1.txt
```

with weighted MWB \(391/8\), CPCR 271, balanced \(L^1=116\), 16 zero cells,
and PCap zero at every depth.  The complete no-improvement report
`scratch/m5_entire_universe_four_block_mwb_round2_report.json` proves local
optimality against every geometric trade of size at most four.  Its remaining
weighted overload is \(14+59/2+43/8\), so depth two, not depth one, is now the
dominant finite obstruction.

The complete five-block generator subsequently lowers weighted MWB to
\(371/8\) in
`scratch/m5_entire_universe_five_block_round3.txt`.  This later factor is
verified but is not claimed five-block-locally optimal.  Its last trade has
weighted coherent gain 14 and weighted noise \(99/8\), illustrating the
strict compensation inequality required by the proof.

Every new trade certificate now also records the exact quadratic identity

\[
\Delta\mathrm{CPCR}_q
=\langle\mu_q,\Delta_q\rangle+\tfrac12\|\Delta_q\|_2^2.
\]

This separates coherent compensation gain from Dirichlet noise and puts the
finite search in the same currency as the remaining stochastic theorem.  The
identity and its sufficient averaged form are proved in
`MATH_LEMMA_SUPPORT_MATCHED_TRADE_DIRICHLET_IDENTITY_20260727.md`.

There is also a new linear structural catalogue.  A pair of adjacent swaps
whose starts differ by \(m\) changes exactly three middle windows.  Pairing
opposite signed triples yields an exact 2-trade.  The resulting \(W\)-arc
generator reproduces every exhaustive 2-trade at \(m=3,4,5\) and is exposed
as `--near-move-catalogue`.  The proved construction, finite converse audit,
and directed-triple formulation are in
`MATH_LEMMA_SEPARATED_DOUBLE_SWAP_INVERSE_TRIPLE_TRADES_20260727.md`.

A still simpler linear catalogue supplies the first successful higher trade.
One adjacent swap changes two middle windows; a directed cycle of the signed
pairs across distinct factor rows is automatically an exact wreath trade.
At \(m=5\), three decorated length-five cycles are found, and the favorable
one is identical to the best trade from the complete five-block census.  A
second carrier step gives the then-current verified value \(185/4\).  See
`MATH_LEMMA_ADJACENT_CARRIER_CYCLE_TRADES_20260727.md` and the search option
`--adjacent-move-catalogue`.

## Frontier integration: chronology, annulus, and carrier closure

The later PBBS/annulus audit is now represented by executable quantities,
not prose-only warnings.

### Literal H-safety

`johnson_chronology_certificate` checks, for every $q\le H$ and every
cyclic start, that the $2q$ deleted/inserted labels are distinct. It also
computes the literal intersection and union images of the $q+1$ states.
Consequently a Johnson proxy is scored by safe windows, correct-rank lower
and upper windows, distinct targets, and repeat excess. The exact residence
certificate remains separate and mandatory for a final wreath.
`scratch/audit_johnson_residence.py --max-depth H` emits both certificates.

### One common annulus state

`shared_packet_annulus_stats` reports holes and repeats for one common packet
family over all depths. `scratch/search_reachable_bites.py` emits this profile
before and after every optimized bite. Independent rankwise leaves therefore
cannot masquerade as one correlated annulus leave. Exact-wreath searches also
expose `holes` as an optional aggregate objective; MWB remains the default.

### Executable compiler ledger

`compiler_length_ledger` evaluates the proved deterministic bound

\[
 L_H\le W+2HB_m+2(5H-1)\nu_H
\]

exactly. It accepts a supplied physical residence-packing certificate.
`bounded_return_arc_packing` computes a chronology-level packing with an
explicit duration cutoff, but is not silently promoted to a physical PBBS
theorem.

### Carrier path-closure deficiency

The adjacent carrier map now records

\[
 \operatorname{def}_{\rm perm}
 =W-\#\{\text{distinct internal targets}\}
 =\#\{\text{external arcs}\}
  +\sum_v(d^-(v)-1)^+ .
\]

This is the exact number of arcs arbitrary retargeting would have to change
to make the partial map a permutation. Legal wreath retargeting remains the
hard condition. Reports separately count raw cycle vertices, distinct-row
legal cycle vertices, repeated-row cycles, and noncycle vertices.

`scratch/search_wreath_carrier_closure.py` performs bounded tabu/beam search
on actual support-matched carrier cycles. Starting from
`scratch/m5_adjacent_carrier_next.txt`, the complete reachable component
under this atlas has only eight factors. The best closure state lowers the
deficiency from $211$ to $197$ and has two favorable cycles, but its
weighted MWB is $373/8>185/4$. The original factor remains the MWB optimum
of the component. Thus the current atlas has a finite reversible
closure/compensation trap; a proof needs path-closing moves outside pure
adjacent cycles. The replayable certificate is
`scratch/m5_carrier_beam_best_certificate.json`.

### Actual compensation coins

`compensation_family_stats` accepts literal legal trades and literal coin
weights and returns

\[
 \mathbb E G,\quad\mathbb E D,\quad\mathbb E(G-D),
 \quad\Pr(G>D),\quad\mathbb E(G-D)^+.
\]

Support-trade and carrier reports now include these fields. Catalogue size,
marginal regularity, and uniform averaging are never substituted for the
missing positive-margin inequality.

### Mixed arity closes carrier paths

The adjacent-only trap is broken by coupling the arity-two adjacent atoms
with arity-three separated-double-swap atoms. The exact owner-level theorem
is implemented by `local_move_circulation_certificate`: selected local moves
form a trade if and only if their added and removed owners form a balanced
directed multigraph.

The first primitive has two triple atoms and four adjacent atoms. One triple
passes wholesale to the other; one owner returns directly, and the remaining
pair traverses a four-edge adjacent-carrier path. The linear generator
`enumerate_triple_assisted_carrier_trades` reproduces exactly all three
size-six mixed trades around the $185/4$ factor.

The mixed mode of `scratch/search_wreath_carrier_closure.py` combines
adjacent cycles, all pure triple carrier cycles (not only inverse
2-cycles), triple-assisted paths, and
multi-junction colored carrier cycles while keeping every intermediate
object exact.  A multi-junction cycle closes several residual pair defects
by matching the terminal carrier prefix of each handoff to the target pair
of the next.  `scratch/multi_junction_carrier_cycles.py` verifies both the
atomic owner circulation and the complete support equality.  Two certified
eight-step beams from the earlier three-part atlas give

\[
 185/4\longrightarrow319/8\longrightarrow\boxed{289/8}.
\]

The final factor has $(O_1,O_2,O_3)=(12,40,33)$, CPCR 193, balanced
$L^1=85$, 15 holes, and zero PCap. The certificate is
`scratch/m5_mixed_beam_best_round2_certificate.json`. A single composed
23-step replay from the $185/4$ factor is
`scratch/m5_mixed_macro_full_path_certificate.json`; the complete theorem
and finite audit are in
`MATH_LEMMA_COUPLED_LOCAL_MOVE_CIRCULATIONS_20260727.md`.

The enlarged atlas finds a new exact size-eight trade at $m=4$ and
reconstructs a size-seven trade that previously appeared only in the
complete $m=5$ support census.  The census's size-nine trade is a pure
adjacent carrier cycle.  On three audited $m=5$ factors, the structural atlas
equals the complete exact-trade set in the full $924$-candidate
adjacent-plus-triple catalogue, with counts $21,22,14$ and no discrepancy.
The report is
`scratch/m5_structural_mixed_atlas_completeness_report.json`.  This finite
completeness is not yet a general classification theorem, but it removes the
local catalogue-search gap at those states.

### Linear triple-cycle supply and cached compensation

The separated-double-swap catalogue is itself a partial functional graph:
its removed triple is the length-two factor path centred at a unique middle
owner.  `enumerate_all_near_carrier_cycles` therefore replaces bounded DFS by
a complete $O(W)$ cycle decomposition.  The MSW flip-permutation recursion
proves an explicit all-$m$ family of

\[
 (2m-1)C_{m-2}
\]

inverse 2-cycles.  The finite audit through $m=10$ finds no additional pure
triple cycles.  Most of the proved family has favorable weighted CPCR
orientation in the audited range.  A greedy
row-disjoint simultaneous pack covers 96.2% of MSW rows at $m=10$ and retains
a 9.58% weighted-CPCR decrease after all cross-trade noise is recomputed.

`scratch/local_trade_shadow_evaluator.py` evaluates the exact quadratic
identity from changed rows only.  It powers
`scratch/audit_msw_triple_compensation.py`,
`scratch/greedy_triple_cycle_descent.py`, and
`scratch/greedy_structural_compensation_descent.py`.  The last driver escapes
the pure-triple local minimum at $m=8$ using the newly integrated adjacent,
one-junction, and multi-junction moves.  Its row-disjoint packing mode applies
many favorable structural trades simultaneously only after recomputing the
literal aggregate cross-noise.  The theorem, finite data, and exact
remaining persistence gate are recorded in
`MATH_THEOREM_MSW_TRIPLE_CARRIER_COMPENSATION_20260727.md`.

### Deterministic near-perfect MSW packet

The explicit Dyck involution in `scratch/msw_dyck_trade_matching.py` toggles
the first aligned four-bit block equal to `1100` or `1010`.  Every matched
pair is a literal inverse-triple trade, different pairs are row-disjoint, and
the unmatched fraction is bounded by

\[
 O\!\left(m^{3/2}(7/8)^{\lfloor m/2\rfloor}\right)=o(1).
\]

Thus search no longer has to discover a compatible large packet at the MSW
seed: an explicit packet covers $1-o(1)$ of its rows.  The audit
`scratch/audit_msw_dyck_trade_matching.py --all-offsets` evaluates the
*simultaneous* quadratic change, not the sum of singleton scores.  The best
translated packet is negative for every audited $4\le m\le10$ and neutral at
$m=3$, even though the odd-$m$ packets can contain individually worsening
trades and have positive cross-interaction.  The exact report is
`scratch/msw_dyck_trade_matching_offsets_m3_m10_report.json`.

`scratch/greedy_triple_cycle_descent.py --initial-aligned-block-packet`
promotes this theorem to a deterministic round-zero move on a generated MSW
seed.  It evaluates all four translated aligned-block partitions (or a
prescribed `--aligned-block-offset`), recomputes each literal aggregate CPCR
identity, and applies the best packet only when its exact change is negative;
the move and terminal factor remain replayable.  This separates two questions
cleanly:

1. row compatibility and asymptotic packet size are now proved;
2. eventual favorable aggregate orientation, and persistence after leaving
   the MSW seed, remain open compensation inequalities.

Immediate phase score is not treated as a proof-safe proxy for downstream
reachability.  `scratch/generate_msw_dyck_packet_portfolio.py` emits the base
MSW factor and all four translated packet factors with independent replay
certificates.  A beam or mixed-atlas descent can therefore retain all four
states.  The $m=5$ calibration is
`scratch/m5_msw_dyck_packet_portfolio_manifest.json`; all four certificates
replay exactly.  It also shows why the portfolio matters: offset $3$ has the
best immediate CPCR change, but after one subsequent greedy triple round
offset $0$ has the best CPCR ($1327/8$), while offset $2$ has the best MWB
score ($315/4$).  All four one-round descendant certificates replay exactly.

### Commuting fixed-slot Boolean cubes

The first-active-row matching uses at most one trade per MSW row, but the
fixed-slot theorem is stronger: trades in disjoint four-bit slots commute in
their trace slabs even when they share rows.  The executable reconstruction
`scratch/msw_fixed_slot_trade_cube.py` therefore exposes every subset of one
slot phase as an exact Boolean cube.  Its active-row count is checked against
the exact inclusion--exclusion formula

\[
 \sum_{h\ge1}(-1)^{h+1}\binom uh2^hC_{m-2h}.
\]

`scratch/search_msw_fixed_slot_cube.py` exhausts these small global cubes
with MWB, CPCR, or hole objectives and emits a one-step replay certificate.
Through $m=9$, the exhaustive MWB optimum has the parity-core form

\[
 \{2,6,\ldots,2m-6\}\quad(m\text{ even}),\qquad
 \{4,8,\ldots,2m-6\}\quad(m\text{ odd}),
\]

with the reflected odd-$m$ choice tied.  The predicted even pattern is also
internally optimal in the audited $m=10$ phase.  Every nonconstant depth's
CPCR pair count decreases at this explicit vertex for $4\le m\le10$.

The depth-one local calculation reduces the sign to one scalar correlation.
At slot $t=2$, the exact finite histogram matches four Catalan expressions
and gives coherent gain $3C_{m-2}$ against noise $2C_{m-2}$, hence change
$-C_{m-2}$, through $m=10$.  The verifier is
`scratch/audit_msw_slot2_catalan_histogram.py`.  Proving its four-class
insertion--erasure bijection is now the smallest all-$m$ compensation target.
More precisely, the observed local gain is

\[
 2\mathbf1\{\text{first MSW }h\text{-flip is at }1\}
 +\mathbf1\{z_2=z_3=1\}.
\]

Both event counts and their intersection have elementary Catalan proofs.
After cancelling common covering roots, the remaining negative witnesses
inject into positive witnesses by the three fixed prefix swaps
`101101 -> 101110`, `111101 -> 111110`,
`11010 -> 10110`, and `11101 -> 11110` (the first two share one swap).
The only missing part is the corresponding fixed-prefix MSW common-interval
identity and completeness proof; 
the theorem/evidence boundary is recorded in
`MATH_THEOREM_MSW_FIXED_SLOT_COMPENSATION_CUBE_20260727.md`.

The common-interval identity is now label-free.  In the MSW flip word, a
depth-one row interval is an arithmetic progression of q-indices with step
(-2).  Each of the three prefix injections induces an explicit finite-block
permutation of q, and modular arithmetic transports the relevant progression
to the lost target.  `scratch/msw_slot2_symbolic_compensation.py` verifies
these identities for every parity-compatible block/start through an
arbitrary requested (m), rather than sampling Dyck roots.  The exact MSW
first-return recursion now proves the q-block permutations: a leaf Tamari
rotation gives one of two block rotations according to the parity of left
edges in its binary-tree address, and the exceptional `110100` class is a
direct six-coordinate calculation.  What remains is only the inverse-fibre
completeness and target-occurrence alignment of the four six-bit prefix
classes.

A subsequent reduction bypasses even that prefix-completeness problem.  The
four affected upper targets are obtained by inserting `1011` or `1101` into
two consecutive endpoint-two paths (y_0,y_1) aligned at coordinate (1)
in the smaller MSW column.  Hence their loads are exact (Gamma)-fibre
sizes.  The depth-one scalar gate is now the marked insertion identity

\[
 c(A(y_0))-c(B(y_0))=-1-B,qquad
 c(A(y_1))-c(B(y_1))=1+B+E.
\]

The marked-Γ collar theorem now proves the required aggregate identity for
all semilengths.  Its key observation is that the aligned endpoint-two paths
are exactly

\[
 \mathcal Y_r=\{y:y\text{ begins }11, U_1(y)\in\{1,2\}\},
\]

with the two Catalan normal forms `11c` and
`11a0 complement(b) 1c`.  The exact inverse criterion then leaves only six
possible first-pivot positions.  The two event counts are $C_{r-1}$ and
$C_r-2C_{r-1}$, so the coherent margin is exactly $C_r$, proving
$\Delta\mathrm{CPCR}_1=-C_r$.  The independent
`verify_marked_gamma_collar_theorem` regression checks both the family
identification and the fibre identities through reduced semilength ten.

The same mathematics is now consumed by the searches in two ways.

1. `search_msw_fixed_slot_cube.py --selection-policy theory` replaces an
   exponential cube scan by a polynomial frontier around the parity core,
   while retaining full exact-factor reconstruction and certificate replay.
2. `greedy_triple_cycle_descent.py --initial-fixed-slot-core
   --descent-objective mwb` seeds the general carrier atlas with that exact
   shore and chooses later trades by cached *exact MWB change*.  The local
   evaluator also reports holes and PCap change; CPCR is no longer silently
   substituted for the theorem's objective.

The marked-Γ theorem is now attached to the executable search contract,
not merely to the note.  `search_msw_fixed_slot_cube.py` runs both the scalar
insertion audit and the pivot-resolved collar audit, refuses a failed finite
regression, and records the proved all-$m$ status in its report.  A
bounded `--state-limit` consumes candidates in parity-core/Hamming-distance
order, but every retained state is still reconstructed and scored as a
literal exact factor; theorem-guided ordering is never substituted for the
exact terminal verifier.

Both exact descent drivers now accept the four audited objectives

\[
  \text{MWB},\qquad \text{CPCR},\qquad \text{one-sided holes},\qquad
  \text{PCap excess}.
\]

The common dispatcher in `local_trade_shadow_evaluator.py` reads these from
the same literal load delta and verifies the selected change against the
terminal factor.  This makes the one-sided covering and phase-capacity
mathematics directly searchable without changing the default: MWB remains
the primary constant-one objective.

The first end-to-end (m=5) integration run reduced weighted MWB from
(401/4) to (643/8) in two post-core rounds, and its three-step literal
certificate replayed.  Starting from the current best (m=5) factor
((289/8)), the new MWB descent finds no improving adjacent/triple carrier
cycle, which is a useful exact local-optimality result rather than a global
claim.

As a pruning regression, radius-one theory mode was compared with the full
Boolean-cube enumeration for every (4\le m\le8).  It recovered the same
selected parity core and exactly the same weighted MWB value in all five
cases; all five emitted certificates replay.  This does not prove the
parity-core conjecture, but it verifies that the accelerated mode loses none
of the known finite optima.

## Exact OR--Pascal constructor integration

The finite exact-answer audit now supplies a separate, smaller search
contract for the exact-value conjecture.  Its authoritative synthesis is
`EXACT_OPTIMA_BEAUTY_ANALYSIS_20260727.md`; the active allocation is
`EXACT_CONSTRUCTION_16_LANE_LEDGER_20260727.md`.

### Finite rank clock; general capacity quantiles

The new representatives at (k=7,10,11,12), together with the clean stored
objects at (k=6,8,9), are rank-monotone and capacity-exact.  The verifier
`scratch/verify_rank_exact_representatives.py` checks every shortest witness.
For the audited small delays, central/factor searches should report rank-clock errors

\[
\#\{S:\tau(S)\ne\max(1,|S|-(r-d)+1)\},
\]

with the forced (k=9) capacity carry recorded separately.  This is a finite
regression metric, **not** the general construction target: asymptotically,
row zero is far too short to contain all ranks through (r-d).

The general target is the exact quantile polytope proved in
`MATH_CAPACITY_ORDERED_OR_PASCAL_QUANTILES_20260727.md`.  If

\[
c_j=W+d-j,\qquad u_j=\#\{\text{lower masks first witnessed in row }j\},
\]

then a rank-ordered candidate must satisfy

\[
0\le u_j\le c_j,\qquad \sum_{j<d}u_j=L,
\]

or, cumulatively,

\[
Q_j-e\le U_j\le\min(Q_j,L).
\]

Search should score inversions of first-witness rank and distance from this
polytope, allowing one rank to split at every row boundary.  Whole-rank rows
must not be hard-coded: they are arithmetically impossible already at
(k=9) and (k=14).  Premature upper masks are a boundary-staircase condition;
the (dW) aligned cells below a central rank-(r) row are automatically of rank
at most (r).

Do not assume that every optimum is already in this normal form.
`MATH_OPTIMAL_NORMALIZATION_EXCHANGE_20260727.md` proves only the forced
banded double-chain skeleton and gives a k=4 optimal counterexample to local
central flattening.  A proposed full witness retiming is accepted exactly by

\[
Z_b=[n]\setminus\bigcup_{S:b\notin S}I_S,
\]

requiring \(I_S\cap Z_b\ne\varnothing\) for every \(b\in S\) and
\(\bigcup_b Z_b=[n]\).  A normalization search should therefore move witness
intervals, evaluate this exact coordinatewise test, and use the lexicographic
pair

\[
(\text{central offset }\Gamma,\ \text{first-witness rank-cut inversions})
\]

rather than editing raw word entries.  Single-entry sorting is formally
insufficient; central straightening and rank compression must be coupled.

### Endpoint-rooted middle levels and boundary pins

In odd dimension, a one-hole lower-rainbow central path with its missing
lower colour below the terminal vertex is exactly the central projection of
an endpoint-rooted middle-levels Hamilton path.  Boundary feasibility is
tested from terminal residence lengths by Theorem 4.1 of
`MATH_BOUNDARY_FLAG_FACTOR_THEOREM_20260727.md`.  After arbitrary
central/lower cells are prescribed, Theorem 3.1 reduces completion to
coordinatewise interval hitting and emits the maximal legal factor.

The search order is therefore mandatory:

1. choose or repair the central path;
2. choose lower pins;
3. run the exact interval-hitting test;
4. construct the maximal legal factor; and
5. run the full contiguous-OR verifier.

There is no reason to put factor bits into a generic SAT model before step 3.

The strengthened theorem in
`MATH_PRESERVABLE_SHRINK_HALL_THEOREM_20260727.md` makes step 3 explicit.
For a witness core (H) and pruned envelopes (F), row-zero masks use the graph

\[
L\sim p\iff H_p\subseteq L\subseteq F_p.
\]

The matching condition is necessary and sufficient.  On a Johnson path each
singleton site's mandatory core has size at most two, and any site set with
no (d+1) consecutive positions is a simultaneously safe reservoir, of density
(d/(d+1)+o(1)).  Search should vary witness phases as well as minimize their
mass: the canonical k12 minimum core has a 5-versus-4 Hall obstruction, while
splitting one witness adds one bit and repairs the full matching.

### Catalan/ballot section invariant

For a one-hole lower-rainbow rank-(r) path on (2r-1) points, every fixed
(t)-set (Q) has exactly

\[
{t\over r}\binom{2r-1-t}{r-t}+\mathbf1_{Q\subseteq C_*}
\]

containing blocks, and their internal edges form a rainbow section forest.
This is a theorem, not a score.  A proposed recursive move must preserve the
resulting incidences; the executable census is
`scratch/analyze_catalan_braid.py`.

The dual absence-block identity

\[
z_Q=\binom{2r-1-t}{r}
-\sum_{U\cap Q=\varnothing}\mu^+(U)
\]

shows that upper CPCR and zero-run balance are coupled.  Search should use
both the exact upper load and the weighted zero-excursion spectrum, rather
than holes alone.

`BALLOT_UPPER_DUALITY_THEOREM_20260727.md` sharpens this into an executable
state representation.  Complement upper colours and store

\[
w(A)=\mu^+([2r-1]\setminus A)-1,
\qquad |A|=r-2.
\]

Its mass is forced to (Cat_r-1), its factorial energy is exactly CPCR, and
all zero-section counts are inclusion degrees of (w).  In particular,

\[
\mu^+(U)=r+1-z_{U^c}.
\]

So a move evaluator can update one excess-design vector and obtain both
upper loads and the complete q1 section profile; it should not maintain
these as unrelated objectives.  CPCR (Phi) also certifies an actual simple
excess design within (ell_1)-distance at most (Phi).

For construction, use transition variables rather than raw path edges.  A
variable

\[
x_{C,\{a,b\}}=1
\]

selects the Johnson chord between \(C\cup\{a\}\) and \(C\cup\{b\}\), with
lower colour \(C\) and upper colour \(C\cup\{a,b\}\).  Impose one chord for
each \(C\ne C_*\), degree two at central vertices (degree one at the two
endpoints), and the desired upper multiplicities from the excess design.
This first produces a path/cycle factor; connectivity cuts join it into the
Hamilton path.  It exposes the exact static-vs-chronological separation and
is a better global model than selecting arbitrary Johnson edges.

The target upper multiplicities need not themselves be searched.
`STATIC_EXCESS_DESIGN_CYCLIC_ORBIT_THEOREM_20260727.md` constructs a simple
CPCR-zero excess design of size (Cat_r-1) with the exact endpoint degree
vector and exponentially small relative discrepancy in every critical
higher inclusion degree.  Generate several translated/orbit-rounded such
designs, then solve only the inverse transition constraints above.  Failure
of one inverse instance is evidence about chronology, not about static
capacity or divisibility.

At higher depth, store truncated local time

\[
F_q(Q)=\sum_{B\in Z_Q}(|B|-q)_+.
\]

Boolean inversion recovers every q-step upper incidence count.  The correct
long-range target is a low-discrepancy hazard schedule: a (t)-section has
forced mean block length (r/t), while ideal q-window survival is
approximately (exp(-qt/r)).  Equal-length block penalties are therefore the
wrong surrogate; score discrepancy from hazard (t/r) across a logarithmic
grid of (t,q) pairs.

`MATH_ROTOR_HAZARD_SCHEDULE_20260727.md` supplies the exact reference law and
a deterministic high-multiplicity generator.  The finite-memory
fresh-exchange state graph is regular of degree

\[
(r-H)(r-1-H),
\]

and higher-block Euler tours give perfectly uniform aggregate lower and upper
shadows through depth (H).  Use periods from this cover as carriers, then
formulate the real task as a transversal: one lift per middle set, one lower
colour apart from (C_*), connectivity, and aggregate CPCR.  The rotor cover
is not itself the construction.  A full-queue transversal already contains
the hard subset-Ucycle problem; the finite-memory (H)-fresh transversal is
the intentionally weaker PBBS/middle-levels target.

### Staged residence

Put (L_i^{(q)}=\bigcap_{h=0}^qT_{i+h}).  Once shorter runs have been
excluded,

\[
L_i^{(q)}=L_{i+1}^{(q)}\iff b_i=a_{i+q}.
\]

Delay-(d) residence can therefore be imposed incrementally by forbidding
adjacent repetitions in (L^{(1)},\ldots,L^{(d)}).  At (k=11), q1
lower-rainbowness handles the first stage; only local no-repeat constraints
at depths two and three remain.  This is smaller than encoding all
multidepth lower colours.

### Verified q1 connector and local move radius

`K11_K12_OVERLAY_CERTIFICATE_20260727.md` supplies a static 827-edge graph
containing a Hamilton path with lower load (1^{461}) and all 330 upper
colours.  Its 150 short runs prove that q1 compatibility alone is not enough.
It is a positive seed for staged residence, not a candidate OR word.

On the q1-perfect connector, q1-preserving 3-opt descent reduces the
length-(2,3) run counts from ((83,67)) to ((10,77)).  The ten remaining q2
witness intervals are pairwise disjoint, so any one-shot q2 repair needs at
least ten cuts.  A cut set is no longer represented by a segment
permutation: cut (s) edges, build the graph on its (2s) exposed ends, and
solve a coloured perfect matching.  Connectivity of the contracted component
graph is exactly Hamiltonicity, while lower labels, upper deficits, and
residence are edge filters.

The first explicit ten-cut choice is rigorously inert: its admissible seam
graph is just the deleted matching.  Across every one-cut-per-witness choice,
the old lower hole is absent from all forty possible exposed vertices, so a
viable matching must contain a nontrivial rainbow alternating circuit and
must permute the ten removed colours exactly.  This incidence test is the
first filter; only survivors should be tested for upper coverage and seam
residence.  A direct delay-three repair needs at least twenty cuts, so the
search must remain staged.

Conversely, the factorable rank-exact k11 seed still has twelve upper holes.
The bounded circuit census exhausts all two-opt and three-cut reconnections:
no residence-safe move in that neighborhood reduces twelve.  Future search
must use the staged ten-/twenty-end matching formulation, a genuine
four-cut-or-larger braid on the factorable seed, a section-forest connector,
or a global reconstruction.  Re-running radius-three local search is retired.

## Surjective-sigma quotient and exact move alphabet

The immediate two-sided gate now has one canonical variable.  For every
lower colour \(X\in\binom{[2r-1]}{r-1}\), choose

\[
\sigma(X)\in\binom{[2r-1]}{r+1},\qquad X\subset\sigma(X).
\]

The two middle sets strictly between \(X\) and \(\sigma(X)\) are the selected
Johnson edge.  An exact model must impose

\[
\sum_{A\supset X}z_{X,A}=1,qquad
\sum_{X\subset Y\subset A}z_{X,A}=2,qquad
\sum_{X\subset A}z_{X,A}\ge1.
\tag{15.1}
\]

The first two equations alone are a bipartite 2-factor.  The third is the
orthogonal upper-clique coverage condition; the combined diamond matrix is
not TU (its smallest obstruction is a determinant-two triangle).  Do not
replace (15.1) by separate Hall checks.

For prime \(k=11\), quotient before any search: 42 lower variables, 15
choices each, 42 middle degree equations, and 30 upper coverage constraints.
The complemented centered PBBS factor already supplies a feasible relaxed
integral state with loads in \(\{1,2,3\}\) and a nonzero-voltage component.
The search target is therefore not feasibility but:

1. one quotient cycle with nonzero voltage;
2. optionally the stronger upper profile \(1^{18}2^{12}\);
3. after a safe cut, delay-three residence; and
4. rank-eight/q2 coverage.

The exact local marginal-preserving move alphabet is also known.  In a
four-coordinate Boolean octahedron it is the circulation lattice of \(K_4\).
The primitive moves are alpha triangles and four-cycles.  Four-cycles are
component-inert.  An alpha triangle can merge three components, or merge two
when its two cuts on one component have the favourable interlacement.  This
three-row move is the smallest possible parity-changing join.  Score alpha
charts first by the exact strand-pairing test, then by residence/q2 seam
damage; do not spend time on nonexistent two-row trades.

For the complemented PBBS seed at (k=11), the static alpha-support graph is
now known exactly enough to reject a direct spanning-tree search.  It has 38
translation-orbits of pure charts (418 labelled charts), but the alternating
component is incident with no alpha chart at all, including mixed charts.
Therefore one must first use a marginal-preserving commutator or a larger
trade to create a portal to this component; only after that state change
should favourable alpha interlacements be enumerated.  See
`K11_PBBS_ALPHA_CHART_SYMBOLIC_AUDIT_20260727.md`.

For prescribed upper multiplicities, the whole q1 factor is equivalently a
perfect matching in the four-partite 4-graph of
`DIAMOND_PERFECT_MATCHING_ABSORPTION_ROUTE_20260727.md`.  This is the correct
absorption model—every hyperedge is a real Boolean diamond and no wildcard
completion object is present.

## Locally orthogonal 1-factorizations

There is a second exact q1 search space which avoids arbitrary pair rounding.
Edge-colour the lower--middle inclusion graph by a complete 1-factorization
\(M_1,\ldots,M_r\), and inspect all \(\binom r2\) pair factors
\(F_{ij}=M_i\cup M_j\).  For each upper set \(A\), the diamond colour pairs
form an \((r+1)\)-regular multigraph \(G_A\) on the \(r\) factor colours.
Its exact local defect is

\[
\Delta_A=h_A+
\sum_{p:m_A(p)\ge3}\binom{m_A(p)-1}{2},
\tag{15.2}
\]

where \(h_A\) is the number of missing colour pairs.  The global identity is

\[
\frac1{\binom r2}\sum_{i<j}\Phi_1^+(F_{ij})
=\frac2{\binom r2}\sum_A\Delta_A.
\tag{15.3}
\]

Thus the exact deterministic objective is to make most \(G_A\)'s close to
\(K_r\) plus a spanning 2-factor.  Average \(\Delta_A=o(r^2)\) already gives
one pair with q1 CPCR \(o(W)\); average \(O(r)\) gives \(O(W/r)\).  This
criterion should replace generic edge-marginal or negative-correlation scores,
which provably do not control pair collisions.

The pointwise objective is locally feasible: for every prime-power (r\ge3)
there is an explicit projective finite-field chart with
(G_A=K_r+) a spanning 2-factor and hence (Delta_A=0).  Global edge
colours are exactly a coherent atlas of these row-Latin skew charts, with one
overlap equation on shared incidences.  Optimize that overlap defect rather
than regenerating local charts.  Do not use the standard lexical
factorization as a presumed solution: after the exact shift (s=r-1), its
first pair has

\[
H_{01}=W\frac{(r-3)(r-4)}{2(r+1)(2r-3)}
\]

upper holes, asymptotically (W/4).  The zero-defect (r=4) charts are an
exceptional boundary case.  See
`LOCALLY_ORTHOGONAL_FACTORIZATION_PROJECTIVE_ATLAS_20260727.md`.
