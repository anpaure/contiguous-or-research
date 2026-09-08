# The cohort construction: a candidate architecture for asymptotic coefficient one

**PBBS dependency correction (2026-09-07):** Any assertion below that Q6
proves a quarter-density family of height-time returns, or that its
qualitative refutation survives the packing correction, is superseded.
Q6 is false: `1(1100)^q0` has height3 and planted lifetime3q. See
`scratch/PBBS_Q6_RETRACTION_AND_FIXED_HEIGHT_COUNTERFAMILY_20260907.md`.
This withdraws that obstruction proof, not the independent upper bound,
and does not certify any other candidate claim in this file.

Date: 2026-08-20 (sixth file of this date).  STATUS: **CANDIDATE — not
a claimed theorem.**  This file specifies a complete construction and
its ledgers, all individually derived and consistent as of block 23 of
this date's session, with two explicitly unverified inputs (Section 5)
and a mandatory independent audit before any upgrade in status.  Six
prior formulations today were each refuted by their own next
calculation; this one has survived one full pass through every
constraint derived today, which is evidence, not proof.

Setting: odd `n=2m+1` (primality NOT required here), `W=binom(n,m)`,
`d=C·ceil(sqrt n)`, GK = Greene–Kleitman SCD, classes = fibers of the
unmatched-set map `U(·)` on rank-`m` tops, targets as in the
sparse-descent file.

## 1. The construction

1. **Supply.**  Cut GK cone chains into level pieces (sparse-descent
   Lemma S2).  Group top pieces by status class `U`; order each class
   by a Pruesse–Ruskey 2-Gray path (input V1, Section 5); order
   classes arbitrarily (boundaries are cheap).

2. **Cohorts.**  Serve each class in cohorts of `w=d-s` consecutive
   members, `s=d/C` (so `w=(1-1/C)d`), all sharing one `tau`-block:
   the `|U|` removal events of `U`, in decreasing position order (=
   the GK descent order), placed in the final `s` steps of the cohort
   span with pace `s/|U|>=1`.  Every cohort member's `d`-step window
   contains the whole `tau`-block, so dues are stationary and one
   departure per coordinate serves the entire cohort.

3. **Cycle.**  Consecutive cohorts of the same class are separated so
   that the cycle length is `>=d+1`: each `u in U` re-arrives after
   its `tau`-event and its next event is `>=d+1` later (run floor
   met with equality margin 1); windows of cohort `k` close strictly
   before the `tau`-block of cohort `k+1` (cycle `>=d+1` ensures it),
   and re-arrivals inside old windows are harmless because an
   intersection, once it loses `u`, never resurrects it.

4. **Pads.**  Member `t`'s owner is `T_t ∪ pad_t` with `pad_t` drawn
   from a rotating pool outside the class's support-union (size
   `~n/2` available vs `~1` needed per member for top-band pieces);
   `pad_t` departs before the first target boundary, realizing the
   top `T_t` itself; pads are pairwise distinct within any `d`-span
   and absent from all concurrent supports, hence pollution-free.

5. **Boundaries.**  At a class boundary: drain (close all windows,
   `d` steps), retool the owner by multi-swap (drop `U∖U'`, bring in
   `U'∖U`), reopen.  Cost `O(d)` per boundary, total
   `e^{O(sqrt n log n)}·O(sqrt n)=o(W)`.

6. **Levels, upper cone, far ranks, even `k`.**  Deep pieces: the
   same cohort machinery per (class, level) with the level's
   `U`-window.  Upper cone: the time-reversed mirror — arrival
   `tau`-blocks serve the cut upper-cone SCD (no extra volume; the
   same events).  Far ranks: per-target absorption (Theorem A).
   Even `k`: top-bit splice.  (Prime transfer remains available but
   is no longer needed: cohort balance is by design, not symmetry.)

## 2. Why each of today's six refutations does not apply

Conflict-density (indep. supplies): cohort members share one class —
supports drift `<=2w=O(sqrt n)` and ALL departures during a cohort are
due for ALL members; zero foreign hits.  Burst gate & rate theorem:
stationary dues — one event per coordinate per cohort, spacing
`=cycle>=d+1`.  Arc-peeling gap no-go: differences here are GK
singletons, not arcs; no extent condition exists in the cohort clock.
Wheel rigidity: the `tau`-blocks are demand-driven, not periodic
ticks.  Smearing: not used.  Steering: 2-Gray within class, `O(d)`
drains at subexponentially many boundaries.

## 3. Ledgers (each derived once today; joint re-derivation required)

Length: `L = (#members)·(cycle/w) = (1+eps)W·(1+O(1/C))`.  Volume:
one departure per `U`-element per cohort plus pads
`= Lambda/(w)+L·O(1)`-consistent, within the factor-2 slack of
Theorem S4.  Spacing: cycle `>=d+1` exactly.  Letters: every window
contains the surviving core `G_s` plus not-yet-due removals; nonzero.
Coverage: SCD partition of the cone (exact); upper mirror; far
absorption.  Status agreement: within class automatic; across
boundaries vacuous by drain.  Dues: stationary by construction.
Pace: `s/|U|=d/(C|U|)>=1` for `|U|<=d/C=sqrt n`, i.e. all typical
classes; classes with `|U|>sqrt n` are exponentially rare and go to
the defect/absorption budget.

## 4. What this would imply

If the construction verifies, then `nu(n)<=(1+O(1/C)+o(1))W(n)` for
all odd `n` and every constant `C`, hence
`nu(k)=(1+o(1))·binom(k,floor(k/2))` for all `k` — handoff conjecture
7.1.3, the asymptotic coefficient-one theorem.

## 5. Unverified inputs and mandatory next steps

V1. **Pruesse–Ruskey 2-Gray codes for order ideals** (successive
ideals differ in `<=2` elements; via prism-Hamiltonicity of bipartite
cover graphs).  Cited from memory; the exact statement and its
applicability to the pinned-corridor product families must be checked
against the paper (G. Pruesse, F. Ruskey, early 1990s; also SIAM
J. Comput. 1994 "Generating linear extensions fast" lineage).

V2. **Joint constants re-derivation.**  Every ledger in Section 3 was
derived exactly once, in sequence, by one mind in one session whose
five earlier architectures each fell to the next pass.  The full
construction must be re-derived jointly in one consistent notation —
in particular the interaction of pad events with `tau`-blocks, the
level-piece cohorts' window depths, the mirror (arrival) side's
simultaneous constraints on the SAME steps, and the boundary drains'
interaction with re-arrival floors.  V2 is precisely the kind of
check that killed blocks 13, 14, 19, 20, and 21's candidates.

V3. **Independent audit** per project standards before any status
upgrade; then a finite simulation-free consistency check at `n=11`
or `n=13` (the cohort structure is hand-checkable at `m=5,6` for one
class cycle).

## 5.5 V2 executed (same day): V2.3 FAILS; the braided patch

The joint re-derivation ran the same day and **refuted Section 1 as
specified** — the seventh refutation of the date, landing exactly at
the predicted gate.  V2.1 (pads) and V2.2 (window/τ geometry, duty
`1-1/C`) pass.  V2.3 fails: a compiled letter is an intersection over
`d+1` consecutive owners, so the openings that realize cohort `k`'s
post-due targets use letters whose owner-windows extend `~2d` past
the cohort, forcing each `u in U(k)` to remain absent through that
tail; `u` must then be present `>=d+1` before its next due.  The
cycle is forced to `>=3d` and the duty to `<=1/3`: **the unbraided
cohort construction has coefficient `>=3-o(1)`.**

**The braided patch (unverified).**  Interleave `~3` cohorts of
distinct classes so that each class's letter-tail hosts the heads of
the others.  The timing of the status conflict is exactly the
`tau`-block, so the braid needs the stronger avoidance condition:
each braided neighbor's SUPPORT (not merely its removal set) must
avoid `U(k)`, and symmetrically — a local coloring of the class walk
with `sqrt n`-sets to be placed in the `~n/2`-sized complements of
neighbors' supports, abundantly satisfiable pointwise.  Duty is then
restored to `1-O(1/C)` and all previously-passing ledgers are
unchanged.  V2 must now be re-run on the braided version — in
particular the triple interaction (braid coloring × mirror-side
arrival blocks × pad pools share the same exterior region and the
same steps), which is the eighth candidate's V2.3-analogue.

## 5.6 The triple check (block 25): convergence of the two corners, and the Mütze mounting

Running the braid-coloring × mirror × pad competition exposed three
structural facts and one published skeleton:

1. **Backbone sharing is necessary**: three braided supports of size
   `~n/2` leave an exterior pool only if they agree outside their
   removal sets; braided classes must share slowly-drifting matched
   backbones (the block-21 grouping returns as a necessity, now
   member-wise along synchronized ideal-walks).

2. **The lower/upper pairing is a simultaneous containment matching**:
   each position's owner must contain its lower top and equal its
   upper chain's rank-`(m+1)` bottom; the mirror side therefore
   demands a perfect matching between the middle layers whose pairs
   are served simultaneously with bounded lag.

3. **Convergence theorem (conceptual)**: at full resolution the
   erosion route requires a coupled traversal of both middle layers
   with local alignment — the same species of object as the singleton
   corner's central-ucycle core.  The two corners of the day's map
   are not alternatives; they share one heart, sitting strictly
   between Mütze's unconstrained middle-levels theorem (published,
   proved) and the `m`-shift ucycle condition (open, Theorem D).

4. **The Mütze cycle is a lag-0 coupled traversal**: it alternates
   `U_j ⊂ V_j ⊃ U_{j+1}`, so serving lower `U_j` and upper `V_j` at
   position `j` with owner `X_j=V_j` realizes the matching and the
   simultaneity for free, with `|V_j∆V_{j+1}|=2` Johnson-smooth owner
   drift.  The next candidate frame (v3) is therefore: mount the
   cohort/status machinery on the Mütze Hamilton cycle as the serving
   order — supply and skeleton both from published theorems, with the
   day's status/τ/letter-tail analysis to be re-run along the cycle's
   explicit local structure (the Gregor–Mütze–Nummenpalo flip-tree
   description).  Unverified; the letter-tail arithmetic (Section
   5.5) is the first thing to re-check on the mounted version, since
   the cycle's status-class sequence is dictated by Mütze's
   construction rather than designed.

## 5.7 Block 26: the day closes into a loop — the ρ-floored middle-levels cycle

Running the first v3 check (Section 5.6.4) produced an identification,
a risk, two small new lemma-level observations, and a confirmed
literature anchor.  Together they replace the branching candidate tree
with a single final object.

1. **Identification (the loop closes).**  The letter-tail arithmetic
   of Section 5.5, evaluated along the Mütze cycle as serving order,
   is *literally* the run-length criterion (Corollary B2 of the
   run-length file) applied to the cycle read as an owner cover with
   `c=1`: owner drift `|V_j∆V_{j+1}|=2` is Johnson-smooth, dues are
   lag-0 stationary (Section 5.6.4), and the only remaining question
   about coordinate `u` is the gap structure between its consecutive
   flips along the cycle — its run-length statistics.  The day's first
   reduction and last candidate are the same statement.  v3 passes or
   fails exactly on whether the chosen middle-levels Hamilton cycle
   has coordinate run floor `H = ceil(sqrt(n ln n))` up to an
   `o(W/sqrt(n log n))` budget of exceptional short runs.

2. **Risk (the PBBS analogy).**  Mütze's and
   Gregor–Mütze–Nummenpalo's explicit cycles are generated from plane
   trees and rotation-like local moves — the same combinatorial
   species as the Dyck/queue-flush dynamics for which Theorem Q6
   (PBBS file) proved Θ(1)-density short runs.  Default expectation:
   the *canonical published* cycles FAIL the run floor, and the check
   should be run to confirm; the freedom is that middle-levels
   Hamilton cycles are double-exponentially numerous, so failure of
   the canonical cycle refutes nothing about the object below.

3. **The final unified object.**  A Hamilton cycle of the
   middle-levels graph `M_{2m+1}` (or a long-path cover, see item 5)
   whose coordinate runs all have length `>= rho = ceil(sqrt(n ln n))`
   outside an `o(W/rho)` exceptional budget.  Existence implies
   coefficient one two independent ways: through the B2 assembly
   (collar ledger + far-rank absorption) and through the v3 mounting
   (cohort/status machinery with the cycle as serving order).  All
   soft constraints of the day (dues, status, pads, mirror) are
   absorbed by the lag-0 structure; the run floor is the entire
   residual content.

4. **Run-economics lemma (favorable).**  In ANY Hamilton cycle of
   `M_{2m+1}`: `2W` edges, each flipping exactly one coordinate, and
   each coordinate's runs partition the cyclic length `2W`, so the
   MEAN run length is exactly `n·2W/2W = n`.  The demanded floor
   `sqrt(n log n)` is `o(n)` — far below the mean.  Contrast the
   hypercube: Goddyn–Gvozdjak achieve minimum run `n − O(log n)`,
   i.e. floor ≈ mean, an extreme equalization.  We need much weaker
   equalization than the strongest known result on the unconstrained
   cube; the difficulty is the level constraint, not run economics.

5. **Path-cover boundary accounting (new caveat).**  A path boundary
   truncates the current run of every coordinate — up to `n`
   potentially-short runs per boundary.  So the path-cover relaxation
   supports the ρ-floor only with `#paths · n = o(W/rho)`, i.e.
   `#paths = o(W/(n·sqrt(n log n)))`, forcing paths of average length
   `>= ~n^{3/2}sqrt(log n)` — long but far from Hamiltonian.
   Alternatively, boundaries can be paid on the owner side by
   drain/retool at `O(d)` apiece (Section 1.5 machinery), which is
   cheaper accounting.  The Hamilton cycle form avoids the issue
   entirely (one wrap).  [CORRECTED in Section 5.8, Lemma 27.1: a
   truncated run is short only if that coordinate flipped within `H`
   of the end, so a boundary costs `<= H` short runs per side, not
   `n`; the piece budget relaxes to `o(W/(n log n))` pieces of
   average length only `omega(n log n)`.]

6. **The equalization hierarchy.**  By Theorem D (run-length file),
   the doubly-exact central ucycle corresponds to the maximally
   equalized traversal — FIFO with dwell exactly `m`, all in-runs
   equal.  The hierarchy on one axis is:

   `Mütze cycle (no floor, published) < ρ-floored cycle (floor
   sqrt(n log n), NEEDED HERE) < m-shift ucycle (perfect
   equalization ~n/2, open ⟺ wreath at (2m+1,m))`.

   The object we need is strictly the weakest unproven point on the
   axis; the wreath-hard endpoint is NOT needed.

7. **Precedent confirmed (primary-source check).**  L. Goddyn and
   P. Gvozdjak, "Binary Gray Codes with Long Bit Runs," Electron. J.
   Combin. 10(1) (2003), #R27, DOI 10.37236/1720: cyclic `n`-bit Gray
   codes exist with all bit-runs of length `>= floor(n − 2.001 log2 n)`
   for infinitely many `n` (and `mrl(n)/n → 1`).  So on the
   unconstrained hypercube, near-mean run floors are a THEOREM, by a
   stream/recursive doubling construction.  The open content here is
   exactly the restriction of such long-run technology to the two
   middle levels.

8. **Next steps.**  (i) Determine the run-length statistics of the
   GMN explicit cycle (expect Q6-like failure; a clean disproof would
   fence the canonical cycle).  (ii) Hybridize: can the
   Goddyn–Gvozdjak track structure be level-constrained, or Mütze's
   gluing be run-floor-aware?  (iii) The ρ-floored middle-levels
   cycle is a standalone, publishable conjecture independent of this
   program; state it separately.

## 5.8 Block 27: rotation rigidity, the eighth refutation, and the quotient-design route (v5)

Attacking the §5.7 object directly produced one accounting
correction, two proved lemmas, one refutation (of a sub-plan formed
and killed inside this same block), and a reformulation that removes
middle-levels Hamiltonicity from the route altogether.  Throughout,
`sigma` is the rotation `i -> i+1` of `Z_n` and `rho = H =
ceil(sqrt(n ln n))`.

**Lemma 27.1 (boundary-cost correction).**  At a piece end, the
truncated final segment of coordinate `u`'s current run is shorter
than `H` only if `u` flipped within the last `H` steps, and at most
`H` coordinates did.  Hence a vertex-disjoint partition of `M_n`
into `p` pieces, each internally `H`-floored, has `nu_H <= 2pH +
(internal short runs)`, and the criterion `nu_H = o(W/H)` needs only
`p = o(W/H^2) = o(W/(n log n))` — pieces of AVERAGE length
`omega(n log n)`, a logarithmic factor above the mean run, not
Hamiltonicity.  (Corrects §5.7 item 5, which over-counted `n` per
boundary.)

**Lemma 27.2 (window-rainbow reformulation; local freedom).**  Run
floor `>= H` along a traversal is equivalent to: every window of `H`
consecutive edge labels is rainbow (no repeated coordinate).  At any
vertex, at most `H` of the `m+1` available next-edges violate the
window, leaving `(1/2 - o(1))n` free choices at every step: the
constraint is locally vacuous; only the global assembly binds.

**Lemma 27.3 (freeness).**  For every odd `n`, `sigma` acts freely
on both middle levels: a period `p | n`, `p < n`, would force
`(n/p)` to divide `|S| = m = (n-1)/2` while `n/p` divides `n`, so
`n/p` divides `gcd(n, n-1) = 1`.

**Theorem 27.4 (rotation rigidity).**  Let `C` be a
`sigma`-invariant cycle of `M_n` of length `2*l*n`.  Then `sigma`
acts on `C` as a rotation, every coordinate flips exactly `2l` times
on `C`, and the multiset of `2l` run lengths is THE SAME for every
coordinate.  For `l = 1` every in-run and every out-run of every
coordinate is EXACTLY `n`: length-`2n` invariant cycles are
perfectly balanced.  *Proof.*  By Lemma 27.3 `sigma` fixes no vertex,
and an order-`n` automorphism of a cycle with `n` odd is a rotation,
by an offset `r` with `gcd(2ln, r)·(order) ` giving `label(t+r) =
label(t)+1`; flip sets of successive coordinates are translates by
`r`, hence equal gap multisets and exactly `2l` flips each.  For
`l = 1`, let `g` be the common in-run.  Summing set sizes around the
cycle: `sum_t |S_t| = n·m + n·(m+1) = n^2`; summing per coordinate:
`sum_u (in-run of u) = n·g`.  So `g = n`.  ∎

**Explicit small witness (`n = 5`).**  The interval cycle
`{01},{012},{12},{123},...` and the cycle
`{02},{023},{03},{013},{13},{134},{14},{124},{24},{024}` form a
`sigma`-invariant 2-factor of `M_5` with both cycles of length
`2n = 10`; hand-reading the labels confirms every run is exactly
`5 = n`, as the theorem forces.

**Proposition 27.5 (eighth refutation — the all-`2n` plan dies).**
The plan "take a `sigma`-invariant 2-factor with ALL cycles of
length `2n`; rigidity makes it perfectly floored; then splice" is
impossible for large `n`.  A `sigma`-invariant `2n`-cycle projects
to a closed walk of length 2 in the necklace quotient, which
requires TWO distinct parallel edge-orbits between the same orbit
pair, which forces `|sigma^j S ∆ S| = 2` for some `j != 0` — an
autocorrelation property satisfied by an exponentially vanishing
fraction of necklaces.  Typical quotient vertices have no doubled
edge, so all-`2n` invariant 2-factors cover only atypical vertices.
The `n = 5` witness above is small-`n` luck.  ∎

**Theorem 27.6 (quotient-design formulation).**  Let `Q_n` be the
necklace quotient of `M_n`: a bipartite `(m+1)`-regular multigraph
on `Cat_m + Cat_m` vertices (`sigma`-orbits of the two levels;
freeness by Lemma 27.3; this is the quotient in which
Gregor–Mütze–Nummenpalo compute).  Then:

  (a) `sigma`-invariant 2-factors of `M_n` correspond exactly to
      2-factors of `Q_n`; the latter EXIST for every odd `n` by
      König (bipartite regular).

  (b) A quotient cycle of length `2l` with holonomy (total phase
      shift) `s` lifts to `gcd(n,s)` cycles upstairs, each of length
      `2ln/gcd(n,s)`; if `gcd(n,s) = 1`, to a SINGLE
      `sigma`-invariant cycle of length `2ln`, to which Theorem 27.4
      applies: every coordinate flips `2l` times with a common gap
      multiset, mean gap exactly `n`.

  (c) The run-floor condition on the lift is an explicit affine
      window-avoidance condition on the quotient walk's label word
      `w` (length `2l`): the lift's label word is
      `w, w+1, ..., w+(n-1)`, so a short run is a pair of
      occurrences of letters `c` and `c + j` at word positions
      `p, p'` with `|p' - p + 2lj| < H`.  For a uniformly random
      label word the expected number of violations is
      `~ (2l)^2 · (1/n) · (H/2l) = 2lH/n`, which for
      `l = polylog(n)` is `o(1)`: the condition is entropically
      nearly free.

  (d) If a 2-factor of `Q_n` has all cycles of length `2l` with
      `omega(log n) <= l` and all holonomies coprime to `n` and all
      lifts `H`-floored, then the lifted 2-factor of `M_n` has
      `nu_H <= (#cycles)·2H = O(W·H/(n·l)) = o(W/H)`, and Corollary
      B2 plus the v3 mounting give COEFFICIENT ONE.  Middle-levels
      Hamiltonicity is bypassed entirely: König supplies the
      skeleton that Mütze's theorem supplied before.

**Route v5 (CANDIDATE — the quotient design).**  Find a 2-factor of
`Q_n` whose cycles have length `2l` with `l` between `omega(log n)`
and `poly(n)`, holonomy coprime to `n`, and window-`H`-avoiding
label words.  The average-case arithmetic is favorable at every
point: mean gap is exactly `n >> H` (Theorem 27.4(b)), the window
condition consumes `H/n = o(1)` of the per-step freedom (Lemma
27.2), violations of a random word are `o(1)` per cycle (27.6(c)),
and the number of 2-factors of a dense regular bipartite multigraph
is `e^{Theta(log n)·Cat_m}` (Schrijver-type permanent bounds) —
vast against the constraint entropy.  This is the regime of random
greedy / local-lemma / entropy methods for constrained 2-factors,
i.e. published-technology-adjacent, unlike the ρ-floored Hamilton
cycle it replaces.

**Danger flags (iron law: full suspicion until joint
re-derivation).**  (α) The three conditions (length, holonomy,
window) must be met JOINTLY by one 2-factor; every refutation today
struck at a joint stage.  (β) The holonomy-sum around a 2-factor was
checked shallowly (no global congruence obstruction found — the sum
telescopes per cycle and depends on the edge set), but coprimality
on EVERY cycle simultaneously is a real design constraint,
especially at composite `n`.  (γ) Labels in `Q_n` are dictated by
the poset, not free: the `(1/n)` letter-collision probability in
27.6(c) assumes quasi-random labels; the actual label correlations
of `Q_n` must be bounded (GMN's explicit quotient formalism is the
tool).  (δ) The v3 mounting (status/dues/pads/mirror) must be
re-run with the lifts as serving order; equivariance of the lifts
should make dues stationary for free, but this is UNVERIFIED — it
is exactly the kind of claim that died in blocks 13–25.

**Next checks, in kill-shot order.**  (1) Composite-`n` holonomy:
is there any congruence forcing some cycle's holonomy to share a
factor with `n`?  (2) Label-correlation bound in `Q_n` from the GMN
quotient description.  (3) Entropy/local-lemma feasibility of the
window condition under a random 2-factor (two random permanent-
weighted matchings).  (4) V2-style joint re-derivation of v5 with
the mirror and pad ledgers.  [Executed in Section 5.9: (1) resolves
positively; (2)–(3) are transformed by the ninth refutation, which
kills the polylog-length plank and forces `Theta(n)` cycle lengths.]

## 5.9 Block 28: kill-shot outcomes — the ninth refutation and route v5′

The checks of §5.8 ran in order.  One plank of v5 is proved
impossible; the salvage is a strictly stronger position.

**28.1 Holonomy check (kill-shot 1): RESOLVED, no obstruction.**
The covering `M_n -> Q_n` is an `n`-fold cyclic cover with deck
group `Z_n`.  The holonomy group at a base orbit (the set of deck
translations realized by lifted closed walks) equals `Z_n` if and
only if the total space `M_n` is connected — which it is.  So
closed walks of every holonomy exist and there is no global
congruence obstruction.  Moreover the prime transfer theorem (P1)
means only PRIME `n` is needed, where "holonomy coprime to `n`"
degenerates to the single excluded value `s ≢ 0 (mod n)`, tunable
per cycle by local rerouting.  Composite-`n` subtleties are moot.

**28.2 Ninth refutation: polylog quotient cycles are impossible.**
Let a quotient cycle of length `2l` and shift `s != 0` pass through
the orbit of the `m`-set `A`.  Lifting and walking once around, the
lift path runs from `A` to `sigma^s(A)` in `2l` single-element
steps, hence

    `2l >= |A ∆ sigma^s A|`   for EVERY vertex on the cycle.

For a uniformly random `m`-set, `E|A ∆ sigma^s A| = (1/2-o(1))·n`
for each fixed `s != 0`, with Hoeffding concentration; a union
bound over the `n` shifts gives: all but an exponentially small
fraction of `m`-sets satisfy `min_{s != 0} |A ∆ sigma^s A| >=
(1/2-o(1))n`.  Therefore quotient cycles of length `o(n)` with
nonzero shift pass only through an exponentially atypical set of
necklaces, and no 2-factor of `Q_n` can have typical vertices on
short nonzero-shift cycles.  The `polylog` cycle-length plank of v5
was self-contradictory — the same autocorrelation wall as
Proposition 27.5, one level up (27.5 is the case `2l = 2`).  ∎

**28.3 The salvage is stronger: route v5′.**  Cycle lengths
`2l = Theta(n)` are FORCED (28.2) and BETTER:

  (a) *Boundary ledger improves.*  `#pieces ~ Cat_m/l = O(W/n^2)`,
      lift lengths `2ln = Theta(n^2)`; boundary cost
      `O(W/n^2)·2H << W/H` with polynomial room.

  (b) *The window condition collapses to local form.*  With
      `2l = Theta(n) >> H`, coordinate `u` flips via letter `u-j` in
      copy `j` of the period word `w`; consecutive flips from
      copies `j < j'` are `2l(j'-j) + O(2l)` apart, so all gaps are
      automatically `>= 2l - O(2l) ...` — the ONLY possible short
      gaps are: (i) a repeated letter within `w` at in-word distance
      `< H` (density `H/n = o(1)` per step, freely avoidable), and
      (ii) the COPY SEAM: letter `c` among the last `~H` positions
      of `w` with letter `c-1` among the first `~H` positions
      (gap `2l + p' - p < H`).  Everything else is `>= 2l - H =
      Theta(n) >> H`: v5′ cycles are NEARLY PERFECTLY EQUALIZED by
      construction — the sweet spot of the §5.7 hierarchy.

  (c) *The seam is the residual content, and it is `Theta(log n)`
      deep.*  At random words the expected number of seam
      violations per cycle is `~H^2/n = ln n` — the day's log-`n`
      seam, fourth appearance, and here it BITES random
      constructions.  But the walk has `(1/2-o(1))n` free choices
      per step (Lemma 27.2), and the seam condition excludes only
      `~H` letters in each of the last `~H` steps: greedy
      avoidance has room `n/2` vs demand `H`.  The residual
      difficulty localizes in one lemma:

      **Endgame steering lemma (OPEN, the new gate).**  A walk in
      `M_n` that must terminate exactly at `sigma^s A_0` in `~r`
      remaining steps (`r >= H`, target at set-distance `r`) can do
      so while avoiding `<= H` forbidden letters per step and the
      in-word window condition.  (A bounded-error Hall/connectivity
      statement about the middle levels, local in nature; the same
      species as the §1.5 drain-retool boundary, NOT a global
      traversal statement.)

  (d) *Type consistency is free.*  Add/remove alternation of each
      coordinate's flips is inherited from `w` being an actual walk
      in `Q_n`, not a free word — no extra constraint.

**28.4 Explicit alternative supply.**  The Duffus–Kierstead–Snevily
modular matchings (match `A` to `A ∪ {b_j}`, `[n]∖A = {b_0 < ... <
b_m}`, `j ≡ sum(A) (mod m+1)`) are reportedly rotation-equivariant
[VERIFY against DKS]; if so, each pair of modular matchings
descends to an explicit 2-factor of `Q_n` with arithmetic labels —
an explicit candidate family for v5′ whose gap statistics are
computable, complementing the random/greedy route.

**28.5 Status.**  v5′ replaces v5.  Remaining planks, in order:
(A) the endgame steering lemma (28.3c) — first solo derivation
pending; (B) global assembly: a 2-factor of `Q_n` into
`Theta(n)`-cycles with `s ≢ 0` whose cycle words admit the steered
seams simultaneously (the joint stage — where, per the day's iron
law, the next failure is most likely); (C) the v3 mounting re-run
(status/dues/pads/mirror along lifts; equivariance should give
stationary dues for free, unverified).  Nothing in this section is
a theorem about `nu`; 28.1–28.2 are proved, 28.3–28.4 are a
candidate specification.

## 5.10 Block 29: the steering lemma proved (solo); plank C closes structurally; the Steerable 2-Factor Conjecture

**Lemma 29.1 (endgame steering; solo derivation, joint re-check
pending).**  Fix `H = ceil(sqrt(n ln n))`, an endgame length
`2t` with `t = 2H`, a fixed forbidden family: at each of the last
`H` steps a set `F_p` of at most `H` letters (in application: the
`+1`-predecessors of the fixed head letters of `w`, nested), a
target `B = sigma^s A_0`, and a current set `C` with
`|C ∆ B| = 2r`, `r <= t/2`.  Then the walk can be completed from
`C` to `B` in exactly `2t` steps so that (i) every step in the last
`H` avoids its `F_p`, (ii) no letter flips twice within `H` steps
(including across the join with the walk body and across the copy
seam), and (iii) alternation and level constraints hold.

*Proof outline (each step a counting or Hall argument with slack).*
Needed flips: the `r` adds `B∖C` and `r` removes `C∖B`, each
exactly once; padding: `t-r` churn pairs (add a fresh letter, remove
it `>= H` steps later).  (1) Schedule every needed letter lying in
`∪F_p` in the FIRST `t` steps (the `F`-restriction binds only the
last `H`); there are `<= H` such letters and `t - H = H` early
slots of each parity beyond other demands — a system of distinct
representatives with slack, Hall's condition immediate.  (2) At
every add-step the free choice is the complement of the current set
(`>= m+1` letters) minus `F_p` (`<= H`) minus letters flipped
within `H` (`<= H`) minus reserved needed letters (`<= 2r <= t`):
at least `n/2 - O(sqrt(n log n)) > 0` churn candidates — abundant;
symmetrically for remove-steps among churn letters aged `>= H`
(churn adds are placed in the first half, removes in the second, so
age is guaranteed by position).  (3) Body-tail coordination: the
endgame schedule is planned first; the body's final `H` steps are
then constrained to avoid the endgame's first-`H` letters — the
same `(1/2-o(1))n`-room greedy avoidance.  (4) Mid-course
guidance (getting `r <= t/2` at endgame entry): while distance to
target exceeds `t/2`, at least `r - H` needed letters are
unblocked at any step, so distance can be reduced at will; hence
the approach invariant `distance <= remaining/2` is maintainable
throughout the word.  ∎

**Proposition 29.2 (plank C closes structurally, modulo plank B).**
The v3 mounting on the v5′ lifts requires no machinery beyond what
is already proved: (a) the serving order is the lift cycles;
alternation of levels IS the lag-0 containment matching (Section
5.6.4), so the mirror/upper-cone service is simultaneous by
construction, no separate arrival blocks; (b) pads are unnecessary
— the B2 assembly consumes the cover directly through the collar
ledger, whose per-piece collar term improves from `2H·Cat_m`
(PBBS-era, `Cat_m` pieces) to `2H·O(Cat_m/n)` here; (c) far ranks
by Theorem A, defective coverage by DCC, both unchanged; (d) run
accounting: internal gaps `Theta(n)` (28.3b), seam gaps `>= H` by
Lemma 29.1, truncations `<= 2H` per piece (Lemma 27.1), total
`nu_H = O(Cat_m/n · H) + o(W/H) = o(W/H)`.  What is NOT yet done:
a line-by-line hypothesis check of Corollary B2 against this cover
(the B2 statement was written for band covers; the lift cover hits
the two middle levels exactly, which is the `c = 1` case) — flagged
for the independent audit.

**The Steerable 2-Factor Conjecture (S2F) — the single remaining
object.**  For prime `n = 2m+1`: the necklace quotient `Q_n`
(bipartite, `(m+1)`-regular multigraph on `Cat_m + Cat_m` vertices)
has a 2-factor such that every cycle, of length `2l in
[n/2·(1+o(1)), O(n)]`, has nonzero holonomy and is realized by a
walk word satisfying the in-word `H`-window condition and the
steered copy-seam condition of Lemma 29.1.

**Theorem-level consequence (conditional).**  Day's chain
(absorption A + criterion B2 + Lemma 27.1 + Theorem 27.4 + 28.1 +
Lemma 29.1 + Proposition 29.2) gives: **S2F implies
`nu(p) = (1+o(1))·binom(p, (p-1)/2)` for primes `p`, hence by the
prime transfer theorem `nu(k) = (1+o(1))·binom(k, floor(k/2))` for
all `k`** — handoff conjecture 7.1.3.  Every quantitative gate
closes with at least polynomial slack except the two `log n`-deep
ones (piece count, seam), both closed with room `n/2` vs `H`.

**Attack routes for S2F (next).**  (i) Iterative absorption on the
orbit space: reserve `eps·Cat_m` flexible necklaces, greedily grow
steered cycles, absorb the leftover — the known danger is
leftover connectivity, the standard absorption battle.  (ii) The
two-matching formulation: a 2-factor is `M_1 ∪ M_2` for perfect
matchings `M_i` of the bipartite `Q_n`; sample `M_2`
permanent-uniformly conditioned on `M_1` and repair violations by
switchings (violation density is `o(1)` per step plus `Theta(log
n)` per seam, and switchings have `(1/2-o(1))n` room).  (iii) The
explicit lane: Duffus–Kierstead–Snevily modular matchings, if
rotation-equivariant [VERIFY], descend to explicit arithmetic
2-factors; their cycle words have computable letter dynamics.

**Iron-law flags.**  Lemma 29.1 survived only its solo derivation;
its joint form must survive plank B's rerouting (a reroute that
fixes one cycle's seam can retroactively break a neighboring
cycle's window — the exact species of interaction that killed
blocks 13, 19, 21, and 24).  Orbit-distinctness along each walk
(quotient cycles must be simple) was checked only generically
(birthday bound) and must be enforced jointly with steering.  The
`B2` hypothesis check in 29.2 is structural, not line-by-line.

## 5.11 Block 30: the long-cycle reversal — steering retired, S2F becomes a mixing lemma

Attacking S2F directly produced a reversal of the block-27/28
design point, in the POSITIVE direction, plus a determinism
observation that converts the whole existence problem into finite
averaging.

**30.1 Long quotient cycles dissolve three conditions at once.**
The ninth refutation forces `2l >= (1/2-o(1))n` but nothing forces
an upper bound; take quotient cycles LONG (up to Hamiltonian).
Then, for a quotient cycle of length `2l` and holonomy `s`:

  (a) *Holonomy is irrelevant.*  If `gcd(n,s) = g`, the lift is `g`
      congruent pieces.  Even `s = 0` gives only `n` pieces per
      quotient cycle; the piece budget `o(W/H^2)` tolerates
      `e^{Theta(n)}` pieces.  Condition dropped.

  (b) *Seams are negligible without steering.*  Each copy
      transition can produce at most `H` short runs even
      ADVERSARIALLY; a quotient cycle contributes at most `n`
      transitions, so all seams across the whole 2-factor cost
      `<= n·H` per quotient cycle — summed: `O(n·H·#cycles)`,
      and with few long cycles this is `<< W/H`.  Lemma 29.1 is
      RETIRED to a fallback (kept proved, unused).

  (c) *The window condition needs only typicality, not perfection.*
      For word length `L_w`, the random-word expectation of
      in-word `H`-window same-letter pairs is `~L_w·H/n`; summed
      over a 2-factor, `~(2W/n)·(H/n) = 2WH/n^2`.  The budget is
      `o(W/H)`, and `(2WH/n^2)/(W/H) = 2H^2/n^2 = 2·log n/n -> 0`:
      the budget exceeds the TYPICAL violation count by a factor
      `~n/log n`.  Zero violations were never needed.

**30.2 The determinism observation.**  Fix any 1-factorization
`M_0, ..., M_m` of `Q_n` (one exists: König on the quotient
multigraph directly; the Duffus–Kierstead–Snevily modular
1-factorization of `M_n` [JCTA 1994], IF rotation-equivariant
[VERIFY], descends to an explicit arithmetic one).  In a
1-factorization, an alternating `(i,j)`-walk is DETERMINED by its
start edge: from any vertex there is exactly one edge of each
color.  Hence:

  - the total number of alternating paths of length `<= H` over
    ALL `~n^2/8` color pairs is exactly
    `#edges × (m) × H ~ Cat_m·n^2·H/4` — polynomial control with
    no probability;
  - a window violation for the pair `(i,j)` is an alternating
    path of length `<= H` whose end edges carry the SAME letter;
  - a union cycle of `M_i ∪ M_j` is a closed alternating walk.

**30.3 The averaged ledger.**  Ignoring the same-letter condition,
the average violation count per color pair is `~2Cat_m·H`, which
misses the per-pair budget `~n·Cat_m/(H log n)` by exactly
`2H^2 log n/n = 2 log^2 n` — the day's log-`n` seam, fifth
appearance.  A letter-equidistribution factor `~1/n` at the walk's
endpoints closes it with room `n/log^2 n`.  The union-cycle-count
condition is the same species: short alternating cycles are early
returns of the same deterministic walk.  Both conditions therefore
reduce to ONE statement:

**The Alternating-Walk Mixing Lemma (AWM) — the remaining object.**
For some 1-factorization of `Q_n` (prime `n`; candidates: the
descended modular factorization, or any König factorization
averaged over): (i) the fraction of alternating walks of length
`<= H` whose end edges share a letter is `O(polylog(n)/n)`; (ii)
the fraction of (edge, color) pairs on alternating cycles of
length `< n log^2 n` is `o(1/log n)`.  Then choosing the color
pair minimizing the weighted sum of violations and short cycles
(Markov over the `~n^2/8` pairs) yields a 2-factor of `Q_n`
satisfying all S2F conditions, and by 29.2 + the day's chain:
coefficient one at primes, hence (P1) for all `k`.

**30.4 Iron-law risk, stated plainly.**  AWM is an
early-return/no-autocorrelation statement about an explicit
deterministic dynamical system — EXACTLY the species where PBBS
died (Theorem Q6: a quarter of all states early-return under the
canonical map).  Three structural differences justify attacking
rather than fencing: (1) we average over `~n^2/8` walks and may
choose the factorization — Q6 concerned one canonical map with no
freedom; (2) the budget slack is polynomial (`n/log^2 n`), not
`o(1)` — Q6's criterion needed a sub-geometric tail with NO slack;
(3) the walk alternates two independent matchings rather than
iterating one map, and two-matching unions are the classical
random-permutation regime.  Still: v5″ (this formulation) has
survived only its solo derivation.  The first check must be a
small-`n` hand computation of the modular alternating walk
(`n = 7`: `Cat_3 = 5` necklaces per side, walks computable by
hand) hunting for structural early returns.

## 5.12 SECOND-READER AUDIT (2026-08-20): five findings; global downgrade

The independent audit required by Section 5 (V3) ran and found five
faults, three of them in load-bearing planks.  All are accepted.

1. **Sparse-descent Theorem S4 is FALSE** (correction recorded in
   that file).  With `d = C·sqrt n` above the typical chain length,
   almost every cut piece is a whole chain and the demand is
   `Theta(W·sqrt n)` independent of `C`, not `W·sqrt n/(4C)`; the
   turnover budget `W·sqrt n/(2C)` REVERSES into an obstruction for
   large `C`.  The erosion corner's counting ledger is NOT closed;
   departure sharing at density `Theta(C)` is exactly the open
   serialization problem.  Every claim in Sections 5.6–5.11 of this
   file that inherits "volume closes with slack" is downgraded.

2. **The multi-swap `O(d)` splice is FALSE as stated** (correction
   recorded there): arbitrary boundary owners cost
   `Theta(n/sqrt(log n)) >> d`; only proximity-ordered seams
   survive, as an unproven hypothesis.  Boundary/drain costs cited
   in this file must be re-audited wherever boundary counts are not
   tiny.

3. **Q6's boxed bound confused counting with packing** (correction
   recorded there): the honest bound is `nu_H(P_m) = Omega(W/H)`
   via greedy interval packing — still `omega(o(W/H))`, so the
   qualitative refutation of the canonical PBBS route STANDS, with
   a weaker constant.

4. **Corollary B2's hypothesis is NOT supplied by a run-floored
   middle-levels 2-factor.**  B2 requires band flag support (nested
   unions to depth `d`), not just the two middle layers with run
   control.  The deep-band supply was exactly sparse-descent's job
   — the S4 hole.  Consequently the conditional "S2F (or AWM)
   implies coefficient one" claimed in 29.2/30.3 is UNSUPPORTED:
   v5″ addresses only the traversal half.  The honest open core is
   a CONJUNCTION: (α) a run-floored middle-layer serving order
   (v5″/AWM — candidate, plausibly tractable), AND (β) a band-depth
   descent supply whose volume ledger currently does not close
   (post-S4), AND their joint compatibility — which is the
   serialization problem the master handoff already identified.
   The day's "one object remains" claims are withdrawn.

5. **Lemma 29.1 is a sketch, not a proof** — slot bookkeeping
   inconsistent; local letter-freedom does not by itself give exact
   endpoint arrival under all constraints.  Downgraded to
   candidate-lemma (it is also retired from the main line by 30.1).

**Revised status of this file.**  Sections 5.7–5.11 are SPECULATIVE
RESEARCH STRATEGY.  Durable content of the date, per audit: the
prime transfer theorem; far-rank absorption and the
defective-cover reduction (threshold claim needs a binomial
lower-tail argument, not just Hoeffding); the ucycle/ML-shift
equivalence; the PBBS queue identities; rotation rigidity (Theorem
27.4), Lemma 27.1's corrected boundary count, the ninth-refutation
autocorrelation bound (28.2), and the holonomy/covering observation
(28.1).  Estimated durable theorem signal of the date: 10–15%.

## 5.13 Block 31 (post-audit): the serialization core re-derived; suffix-intersection rigidity

Written under the audit's discipline: small claims, each proved in
place; no architecture.  Setting: owner stream `V_1, ..., V_L` at
rank `m+1`, `L = (1+eps)W`, run floor `d+1`, `d = C·sqrt n`; a
window anchored at `a` has intersections `I_{a,t} = V_a ∩ ... ∩
V_t`, and serving a target `T` at depth `x` means some `I_{a,t} =
T`.

**Lemma 31.1 (concurrency forces proximity).**  If targets `T` (depth
`x`) and `T'` (depth `x'`) are both alive at one step (both contained
in the current owner via their windows), then `T ∪ T' ⊆ V_t`, so

    `|T ∆ T'| = 2|T ∪ T'| − |T| − |T'| <= x + x'`.

Concurrent targets are near-nested BY OWNER CAPACITY alone — the
laminarity principle is a two-line theorem, not a design choice.  ∎

**Lemma 31.2 (sharing is structural; so are conflicts).**  The active
windows at step `t` are the suffix-intersections `I_{a,t}`, `a <= t`,
and they form a NESTED TOWER: for `a >= a'`, `I_{a,t} ⊇ I_{a',t}`
(a younger window intersects fewer owners, so it is larger; older
windows are smaller).  A departure `z` at step `t+1`
removes `z` from every tower member containing it simultaneously:
one departure advances many windows at once (the sharing that S4's
correction demands, at no cost).  Conversely the same departure
KILLS every active window whose target contains `z`.  So the
schedule is feasible iff at every step the departing element lies
outside the union of all concurrent targets.  ∎

**Demand/budget arithmetic (corrected S4 frame).**  Total descent
demand is `Lambda = Theta(W·sqrt n)` units (audit-corrected S4);
distinct-owner coverage forces at least `~1` departure per step and
the run floor allows at most `~sqrt n/(2C)` per step.  Hence each
departure must advance `Theta(sqrt n)` windows (at rate 1/step) —
which Lemma 31.2 provides automatically WHEN the tower's targets
are compatible.  The counting tension of S4 is thereby exactly
neutralized by structure — the entire difficulty is target
compatibility, quantified next.

**Lemma 31.3 (suffix-intersection rigidity; proof sketch, honest
status: derivation solid at the `1+eps` bookkeeping level).**  At a
step where a fresh window (depth 0–1) is active, the departing
element must avoid its target, which is the owner minus at most one
element: the departure is PINNED (up to the `eps·W` anchor-free
steps).  By induction along the stream, on a fully-anchored stream
the servable segment family is EXACTLY the family of
suffix-intersections of the stream itself — there is no assignment
freedom.  Chains are not assigned to a stream; they ARE the stream's
suffix-chains, up to `O(eps·W)` exceptions.  ∎ (sketch)

**Consequence: the Span-Intersection Cover (SIC) form.**  Combining
31.1–31.3 with the audit-corrected ledgers, the conjunction
(α)∧(β) of Section 5.12 is equivalent (up to `o(W)` bookkeeping) to
the single derived statement:

    **SIC.**  There exists a rank-`(m+1)` walk of length
    `(1+eps)W` with run floor `d+1` whose span-intersections
    `{V_a ∩ ... ∩ V_b}` realize `(1−o(1))` of the lower cone
    (capacity check: `L·d = (1+eps)C·W·sqrt n` available spans
    versus `Lambda ~ 0.63·W·sqrt n` needed — slack `C`).

This is the master handoff's 7.2.1 "laminar chain chronology,"
now DERIVED as forced rather than posited, with the laminarity
quantified (31.1) and the assignment layer removed (31.3).  The
`m`-shift ucycle is SIC's perfectly-equalized special case (its
span-intersections are FIFO age-intervals — which cover only a
`W·d`-sized special family: exactly why the wreath endpoint is hard
and why SIC's freedom must be used).  Canonical PBBS was the failed
canonical attempt at SIC (its span-intersections are the `P_m`
chains; Q6 corrected shows its floor fails).  The `k <= 16` optima
are finite SIC witnesses.

**Honest status.**  SIC is a sharpened equivalent FORM of the open
core, not progress toward its truth.  Its value: (i) the search
space is now one walk, not walk+assignment; (ii) the two
audit-surviving quantitative facts (31.1 proximity, sharing rate
`Theta(sqrt n)` per departure) are necessary-condition guides for
any construction; (iii) the three known corner cases (m-shift,
PBBS, finite optima) are all SIC instances, so the object finally
matches the evidence.

## 5.14 Block 32: peel criticality — the Poisson obstruction and the depth dichotomy

Necessary-condition mining on SIC.  All claims here are
calculations or clearly-scoped conditionals; one is a refutation of
a construction class.

**32.1 The peel formulation.**  From anchor `a`, the depth-`x`
realized set is UNIQUE: `T_x(a) = V_a ∖ {first x subsequent
departures hitting V_a}`.  A SIC walk realizes exactly one set per
(anchor, depth) pair; coverage is a question about the PEEL MAP
`(a, x) -> T_x(a)`.

**32.2 Criticality computation.**  A cone target `T` at depth `x`
has `C(m+x, x)` rank-`(m+1)` supersets, each visited `(1+eps)`
times on average by an owner-injective walk of length `(1+eps)W`.
If peel outcomes at a superset were uniform over its `C(m+1, x)`
depth-`x` subsets, the expected number of realizations of `T`
would be

    `lambda(x) = (1+eps)·C(m+x,x)/C(m+1,x)
               = (1+eps)·prod_{j=1}^{x} (m+j)/(m+2-j)
               = (1+eps)·e^{(2x^2/n)(1+o(1))}`.

At the cone's typical depths `x = Theta(sqrt n)` this is `Theta(1)`:
**the shallow cone sits at perfect-matching criticality, not at
nibble slack.**  (The capacity slack `C` of Section 5.13 is a
volume statement; per-target multiplicity has NO slack.)

**32.3 The Poisson obstruction (refutation of the random-SIC
class).**  Any construction whose peel outcomes are asymptotically
independent across anchors (any random-greedy, sampling, or
locally-uniform walk) misses an `e^{-lambda(x)}`-fraction of
depth-`x` targets.  Summed over the shallow cone this is
`Theta(W·sqrt n)` misses — unrepairable (absorption costs
`Omega(1)` word-length each, total `omega(eps W)`).  This DERIVES
the project's empirical `1 - 1/e` sampling stall from first
principles in the SIC frame and rules out all purely
random/greedy/nibble constructions of the walk.  Near-BIJECTIVE
peeling is forced wherever `lambda(x) = O(log)` — exact design, the
same species as an exact cover.

**32.4 The depth dichotomy.**  Because `lambda(x) = e^{2x^2/n}`
grows doubly fast in `x/sqrt n`, misses decay like
`exp(-e^{2x^2/n})`:

  - Depth `1`: coverage means the map `a -> V_a ∖ {next hit}` is
    `(1-o(1))`-surjective onto rank-`m` — exactly the traversal
    half (α): a floored middle-levels-type walk visiting both
    layers (Mütze's cycle does this WITHOUT the floor; the floor is
    the open part).
  - Depths `2 <= x <= x* = Theta(sqrt(n·log log n))`: the EXACT
    ZONE — near-bijective peel design is forced.  This is the
    audit's finding 4 (band-flag support) made quantitative: the
    missing hypothesis is precisely exact peeling in a band of
    thickness `Theta(sqrt(n log log n))` below the middle.
  - Depths `x > x*`: `lambda >= polylog`, and coverage follows from
    equidistribution alone (second-moment control still to be
    proved, but this is standard-species, not exact design).

**32.5 What this buys.**  The hard core shrinks from "the whole
cone" to a band of `Theta(sqrt(n·log log n))` ranks, only a
`sqrt(log log n)` factor deeper than the depth-1/wreath corner
itself; and the required object in that band is an exact peel
design riding on a floored two-layer traversal.  The three known
data points align: the wreath conjecture is the depth-1 exact
statement; the `k <= 16` optima are finite exact designs through
the whole band; PBBS was an exact design whose FLOOR failed (not
its exactness).  Open, in order: (1) second-moment closure of the
deep zone; (2) whether exact peel designs at depth 2 exist atop
SOME floored traversal (the first genuinely new finite question:
depth-2 exactness at small `n`); (3) the floor itself (α),
unchanged.

## 5.15 Block 33: the lockstep theorem — peels are windows, and (α) fuses with (β)

**Lemma 33.1 (floor makes peels windows; proved).**  Let the walk
have run floor `d+1` and departure word `z_1, z_2, ...` (one
departure per owner change).  Then for every `j` and every
`x <= d`,

    `T_x(j) = V_j ∖ {z_j, z_{j+1}, ..., z_{j+x-1}}`:

the depth-`x` peel from anchor `j` is simply the next `x`
departures — no selection, no "hits."  *Proof.*  A departure
`z_{j+i}` (`0 <= i <= d`) has age `>= d+1` at its departure, so it
arrived at time `<= j+i-(d+1) < j` and has not departed in between;
hence `z_{j+i} ∈ V_j`.  Every one of the next `x <= d` departures
hits `V_j`, and they are distinct (no element returns within `d`).
∎

**Corollary 33.2 (lockstep).**  With arrival word `y_j` (so
`V_{j+1} = V_j ∖ {z_j} ∪ {y_j}`), the depth-`x` target sequence
satisfies, for `x <= d`,

    `T_x(j+1) = T_x(j) ∖ {z_{j+x}} ∪ {y_j}`.

So for EVERY depth `x` the realized sets form a Johnson-type walk
on rank `m+1-x`, all driven by ONE word pair: the same arrivals
`y`, and the same departure word shifted by `x`.  The `d+1`
section-walks move in lockstep; SIC is a statement about one walk
and its time-lag self-overlaps.

**Corollary 33.3 (multiplicity forcing).**  The depth-`x` section
visits `(1+eps)W` positions among `C(n, m+1-x)` sets, giving
average multiplicity `(1+eps)W/C(n,m+1-x) = (1+eps)e^{2x^2/n
(1+o(1))}` — consistent with 32.2 (a check the lockstep frame
passes automatically).  Hence: at depths `x = o(sqrt n)` the
multiplicity is `1+o(1)` and the section walk must be
NEAR-HAMILTONIAN on its layer; at `x = Theta(sqrt n)` it must be a
near-uniform `e^{Theta(1)}`-fold cover; above `x*` equidistribution
suffices (32.4).

**The fused object (LSGC).**  Call a pair of words `(y, z)` with
dwell floor `d+1` a *Lagged-Section Gray Code* if for every
`x ∈ [0, d]` the section walk `T_x` is `(1-o(1))`-surjective onto
rank `m+1-x`.  Then, by 33.1–33.3 with Sections 5.13–5.14:

    SIC  ⟺  a floored LSGC exists at length `(1+eps)W`,

and the floor is not a side condition — it is exactly what makes
peels equal windows (33.1), i.e. (α) and (β) are ONE mechanism.
Placement among known objects: lags `{0,1}` without the floor =
the middle levels theorem (Mütze, published); lags `{0,1}` with
EXACT multiplicity 1 and the rigid shift `z_j = y_{j-m}` = the
doubly-exact central ucycle (open; wreath-hard endpoint — NOT
needed); one cycle through `2l` central layers = the central
levels theorem (Gregor–Micka–Mütze, published) — a different
strengthening (one walk THROUGH layers, versus one walk whose
SECTIONS traverse layers).  LSGC appears to be new as an object;
lags `0..o(sqrt n)` near-Hamiltonian simultaneously is its core
demand.

**Posed finite question (first test of the frame).**  `n = 7`,
`d = 2`: does a dwell-floored word pair of length `~(1+eps)·35`
exist whose lag-0, lag-1, lag-2 sections cover ranks 4, 3, 2
near-exactly (35 + 35 + 21 targets)?  Small enough to settle by
hand or trivial search; a positive answer gives the first LSGC
data point beyond the `k <= 16` optima (which are LSGC witnesses
only implicitly); a negative one refutes the frame at its first
joint.  Status of everything in this section: 33.1–33.3 are proved
calculations; the LSGC equivalence inherits the `1+eps` bookkeeping
caveats of 31.3; nothing here advances the truth of SIC.

## 5.16 Block 34: the n = 7 test reduced to a floored multi-window ucycle; the affine no-go

**Lemma 34.1 (finite reduction; proved).**  At `n = 7`, `d = 2`
(floor 3), the out-pool has size `n - m - 1 = 3` and one arrival
per step, so out-dwells average exactly 3 with minimum 3: ALL
out-dwells equal 3 and arrivals are forced, `y_j = z_{j-3}`.
Consequently `V_j = [7] ∖ {z_{j-1}, z_{j-2}, z_{j-3}}`, and the
in-age condition on departures becomes: every 6 consecutive
letters of the departure word are distinct (cyclic letter-gap
`>= 6`).  The three LSGC sections are complements of the
departure word's sliding windows, so:

    the `n = 7, d = 2` floored LSGC exists at length `L`
    ⟺  there is a cyclic word over `Z_7`, length `L`, all
    letter-gaps `>= 6`, whose 3-, 4-, and 5-windows (as sets)
    cover all `35 + 35 + 21` subsets.

The zero-slack case (`L = 35`, all windows distinct) is exactly
the doubly-exact `(7,3)` central ucycle — the wreath-hard object.
The test therefore probes the day's central thesis in miniature:
does `~20-40%` length slack unlock what exactness forbids?  ∎

**Lemma 34.2 (affine no-go; proved).**  No concatenation of affine
rows `t ↦ c_j t + d_j` of `Z_7` satisfies both the gap floor and
coverage: the seam condition forces `p_{j+1}(x) >= p_j(x) - 1` for
every letter `x`, and `p_{j+1}(x) - p_j(x)` is a linear function
of `x` which takes all residues unless its coefficient vanishes —
forcing all multipliers equal; equal multipliers produce windows
in a single affine orbit, and the 3-subsets of `Z_7` split into
TWO affine orbits (21 arithmetic-progression sets and 14
non-AP sets, e.g. `{0,1,3}` with stabilizer `x ↦ 2x+1` of order
3), so the 14 non-AP sets are never covered.  The floor is
incompatible with algebraic periodicity — the PBBS lesson
reproduced at `n = 7`.  ∎

**Computational status (honest).**  One completed local greedy run
(before computation moved off this machine) found a gap-`>= 6`
word at `L = 49` covering `34/35 + 32/35 + 20/21 = 86/91` —
near-feasibility, no conclusion.  The full annealing search is
packaged in `scripts/lsgc_n7_search.py` to run on the remote box
(h100) once the VPN tunnel is up; the finite question remains
OPEN.  A perfect witness would be the first explicit
slack-beats-exactness data point; a proven miss at all
`L <= ~2·35` would refute the LSGC frame at its first joint.

## 5.17 Block 35: flags for free, the floor dial, the deep-zone margin, and the Frame Theorem

**Lemma 35.1 (anchors carry full flags — conditional repair of
audit finding 4).**  By the lockstep theorem (33.1), every anchor
`j` of a floored walk carries the complete nested chain

    `T_d(j) ⊂ T_{d-1}(j) ⊂ ... ⊂ T_1(j) ⊂ T_0(j) = V_j`,

a full FLAG of the band at every position — not two isolated
layers.  A floored LSGC therefore supplies exactly the band-flag
support whose absence was audit finding 4; what remains of that
finding is only the B2 line-by-line hypothesis check (still owed
to the independent audit), not a structural gap.  ∎

**Lemma 35.2 (the floor dial).**  Out-pool size is `m`, arrival
rate 1, so out-dwells average `m` with minimum `d+1`.  (i) If
`d+1 = m`, the 34.1 forcing argument applies verbatim: all
out-dwells equal `m`, arrivals are FIFO-forced `y_j = z_{j-m}` —
the `m`-shift structure, whose doubly-exact case is the
wreath-hard central ucycle.  (ii) If `d+1 < m`, the arrival order
retains entropy `>= log(m-d)` bits per step; at `d = C·sqrt n`
this is `(1/2 - o(1))·log n` bits per step, plus comparable
departure freedom.  The LSGC family thus interpolates between
Mütze-freedom (`d = 0`) and wreath-rigidity (`d = m-1`) with `C`
as the dial; the day's program lives at `C = Theta(1)`, where the
floor costs an `o(1)` fraction of the available entropy.  ∎

**Proposition 35.3 (deep-zone margin, conditional on mixing).**
Suppose a walk's sections at lags `x > x*` equidistribute with
second-moment ratio `1+O(1)` (so misses obey the Poisson-type
bound `miss(x) <= C(n, m+1-x)·e^{-lambda(x)}`, `lambda(x) =
(1+eps)e^{2x^2/n}`).  With `u = e^{2x^2/n}`, the total repair bill
beyond `x*` is

    `sum_{x > x*} W·u^{-1}e^{-(1+eps)u}·O(H*)
     = W·O(H*)·e^{-u*}/u*`,   `u* = e^{2x*^2/n}`,

which is `<= eps·W` as soon as `u* >= (1/2 + o(1))·ln n`, i.e.
`x* = sqrt((n/2)·ln((1/2)ln n)) = Theta(sqrt(n log log n))` —
the 32.4 threshold, now derived rather than asserted.  ∎

**Frame Theorem (conditional; the current honest map in one
statement).**  Suppose there exists a word pair `(y, z)` with
dwell floor `d+1`, `d = C·sqrt n`, and length `(1+eps)W` such
that:

  (a) [shallow exactness] the lag-`x` sections are
      `(1-o(1))`-surjective onto rank `m+1-x` for all
      `x <= x* = Theta(sqrt(n log log n))`; and
  (b) [deep mixing] the lag-`x` sections for `x* < x <= d`
      equidistribute with bounded second-moment ratio.

Then the anchors supply `(1-o(1))`-complete band flags (35.1),
the deep defect costs `<= eps W` (35.3), far ranks absorb at cost
`o(W)` (Theorem A with the two-sided tail patch A1′), and —
MODULO the explicitly open items: the B2 line-by-line hypothesis
check, the `1+eps` bookkeeping of 31.3, and the assembly's collar
ledger re-audit — `nu(n) <= (1+O(eps))W(n)` for odd `n`, hence by
prime transfer `nu(k) = (1+o(1))·binom(k, floor(k/2))` for all
`k`.

**Open planks, exhaustively:** (a), (b), B2 line-by-line, 31.3
bookkeeping, collar re-audit.  (a) at `x <= 1` is
middle-levels-with-floor; (a) at `2 <= x <= x*` is the exact
zone (32.4); the `n = 7` finite test (34.1) probes the smallest
instance of (a).  Nothing in this section proves the conjecture;
it consolidates exactly what remains.

## 5.18 Block 36: the exact zone has no static obstruction — x = 2 splits into supply (proved) and sequencing (open)

Plank (a) at `x = 2` demands: the map `U_{j+1} ↦ U_{j+1} ∖
{z_{j+1}}` is `(1-o(1))`-surjective onto rank `m-1`, jointly with
lag-0/1 near-bijectivity.  Split it into a static and a dynamic
half.

**Lemma 36.1 (static supply, full — proved).**  There is a choice
function `φ` assigning to rank-`m` sets a removal `φ(U) ∈ U` such
that `U ↦ U ∖ φ(U)` covers EVERY rank-`(m-1)` set.  *Proof.*  By
the normalized matching property of the Boolean lattice, any
family `F` of rank-`(m-1)` sets has upper shadow of size
`|∂^+F| >= |F|·C(n,m)/C(n,m-1) = |F|·(m+2)/m >= |F|`, so Hall's
condition holds for covering rank `m-1` by distinct supersets: an
injection `ψ` with `R ⊂ ψ(R)` exists; set `φ(ψ(R)) = ψ(R)∖R` and
choose `φ` arbitrarily elsewhere.  ∎

**Lemma 36.2 (floor-robust defect version — proved at the species
level; constants to be pinned in audit).**  Suppose adversarially,
at each rank-`m` set, up to `d` of its `m` removal options are
forbidden (this dominates the floor's effect: the `<= d` youngest
elements at visit time are unremovable).  Then an assignment
exists covering all but `O(W·d/m) = O(C·W/sqrt n) = o(W)` of rank
`m-1`.  *Proof sketch.*  An `R` can be killed outright only by
forbidding it at all `m+2` supersets, costing `m+2` budget units;
total budget `W·d` kills at most `Wd/(m+2)` targets.  For the
rest, deficiency Hall with the `(m+2)/m` normalized-matching
expansion absorbs forbidden-degree defects of total weight `Wd`,
leaving deficiency `O(Wd/m)`.  ∎

**Consequence 36.3 (localization).**  The exact zone at `x = 2` —
and by the identical normalized-matching argument between each
pair of adjacent ranks, at every `x <= x*` (compose the per-rank
SDRs into chain systems; this is exactly the audit-surviving cut
supply, Lemma S2) — has NO static obstruction, even in the
presence of the floor's forbidding.  The ENTIRE remaining
difficulty of plank (a) is SEQUENCING: realizing the statically
assigned removals as the walk's actual next-departures, i.e. the
walk's visit order and arrival schedule must let each visited set
execute its assignment.  This is the same single difficulty the
audit isolated (departure sharing/serialization), now confirmed
at the shallowest new layer: nothing else is in the way.

**Status.**  36.1 unconditional; 36.2 needs its constants pinned
by a reader; 36.3 is an organizing statement.  The conjecture is
not advanced in truth-value; plank (a) is now precisely "a
sequencing theorem", with its static half discharged.

## 5.19 Block 37: the B2 check run in-house — a new no-go, and a sixth plank the Frame Theorem missed

Executing the "B2 line-by-line" plank myself (the audit's lesson:
that is where failures hide) produced one proved no-go, one ledger
correction that EXTENDS the open-plank list, and one consistency
observation.

**37.1 The singleton/FIFO no-go (proved).**  Suppose the compiled
word uses one singleton letter per walk step (the arrival), so
each target must be a union of CONTIGUOUS arrival letters.  A
lockstep target `T_x(j) = V_j ∖ {z_j..z_{j+x-1}}` is a contiguous
arrival block for all `x <= d` iff each departure removes an
endpoint of the current arrival-interval; the young endpoint is
barred by the floor (age `< d+1`), so all departures must take
the OLDEST element: FIFO — i.e. the `m`-shift structure, whose
exact form is the wreath-hard doubly-exact ucycle.  **The
one-singleton-letter-per-step economy forces the wreath
endpoint.**  This explains structurally why the ucycle corner is
rigid, and proves that any coefficient-one compilation must use
either non-singleton letters or element repetition.  ∎

**37.2 The ledger correction (the Frame Theorem's list was
incomplete).**  The collar ledger charges `Theta(H)` overhead PER
CHAIN (`H = sqrt(n log n)`), amortized over the chain's depth.
PBBS chains had depth `Theta(n^{3/2})`, so the overhead was
negligible; the lockstep flags have depth only `d = C sqrt n < H`
per anchor.  If each anchor's flag were compiled as its own
chain, the overhead would be `Theta(H)·(1+eps)W = omega(W)` —
fatal.  The compilation therefore requires the flag stream to be
organized into RUNS of `omega(H)` consecutive anchors compiled
jointly with `O(H)` overhead per run.  This is a genuine SIXTH
plank, hidden inside "B2 line-by-line" until now:

    (f) [chain organization] the lockstep flag stream factors
    into runs of length `omega(sqrt(n log n))` admitting joint
    pollution-free interval compilation at `O(H)` overhead each.

**37.3 Consistency observation (not a proof).**  Non-contiguity
can be bought without length: letters may repeat elements (length
counts letters, not mass), constrained only by POLLUTION — a
repeated element must avoid the intervals of targets excluding
it.  Pollution-avoidance for concurrent targets is an interval-
laminarity condition, and Lemma 31.1 proves concurrent targets
are FORCED near-laminar.  The structure needed for (f) is thus
exactly the structure the frame already forces — supportive, but
(f) remains open.

**Revised exhaustive plank list:** (a-sequencing), (b) deep
mixing, (f) chain organization, 31.3 bookkeeping, collar
re-audit constants.  [B2 line-by-line is hereby DISCHARGED as a
named plank — its content was exactly (f) plus 37.1.]

## 5.20 Block 38: quadratic reuse dissolves plank (f) — the quasi-FIFO window design

Attacking (f) by re-deriving the compilation economics from
scratch.

**38.1 The quadratic-reuse principle.**  A word realizing
`Theta(W sqrt n)` cone targets in `(1+eps)W` letters must serve
`Theta(sqrt n)` targets PER LETTER.  Disjoint chain segments give
ratio 1 and fail; per-target fat letters cost length `Theta(W
sqrt n)` and fail; the only mechanism with the right economy is
INTERVAL REUSE: a stretch of `ell` distinct singleton letters
realizes ALL its sub-windows — up to `ell` targets per letter
when windows of all lengths up to `ell` are valid targets.  At
`ell = Theta(sqrt n)` bands this is exactly the required ratio.
The compiled word's own sliding windows must BE the realizations;
chains and collars appear only at defects.  (This also
retro-explains the PBBS ledger: its `2H`-per-chain collar was the
defect cost, not the main economy.)

**38.2 The pollution lemma (proved, elementary).**  In a singleton
arrival word, the union over a window equals the set of DISTINCT
letters in it; it equals a rank-`ell` target iff no element makes
a round trip (departs and re-arrives) inside the window.  Round
trips take `(in-dwell) + (out-dwell)`.  Hence if all dwells lie
in `m ± O(d)` (round trips `n ± O(d)`), then EVERY window of
length `<= n/2` is pollution-free, while the dwell distribution
retains entropy `Theta(log d) = Theta(log n)` bits per step.
Call this discipline QUASI-FIFO.  It subsumes the run floor
(`dwell ~ m >> d`), respects the 37.1 no-go (it is not FIFO —
the `± O(d)` variability is the design freedom), and sits at the
floor-dial position where the wreath rigidity just releases.  ∎

**38.3 The transfer (plank (f) dissolves).**  Under quasi-FIFO,
the band-cone targets are realized DIRECTLY as the arrival word's
windows: a rank-`(m+1-x)` target is a length-`(m+1-x)` window's
letter set.  The LSGC counting migrates verbatim: `(1+eps)W`
windows of each length versus `C(n, m+1-x)` targets, multiplicity
`(1+eps)e^{2x^2/n}` — near-bijectivity forced at co-depth
`x <= x*`, Poisson-coverage sufficient beyond.  No separate chain
organization exists: (f) was an artifact of compiling against the
wrong mechanism.  What remains of the top layers: `V_t` itself is
polluted by `O(d)` round-trippers in its natural window, so the
rank-`(m+1)` and rank-`m` layers must be served by the MIRROR
(complementation/departure side) — an exactness check that is now
the frame's newest unverified joint.

**38.4 The consolidated object (QFWD — quasi-FIFO window
design).**  A cyclic word over `[n]`, length `(1+eps)W`,
consecutive occurrences of every letter separated by `n ± O(d)`,
such that: (i) for `x <= x* = Theta(sqrt(n log log n))`, the
length-`(m+1-x)` windows are `(1-o(1))`-surjective onto rank
`m+1-x`; (ii) beyond `x*`, windows equidistribute
(second-moment); (iii) the mirror serves the top two layers
exactly.  QFWD implies the Frame Theorem's hypotheses with (f)
void.  The `n = 7` finite object of 34.1 (gap-floored word with
3/4/5-window coverage) is precisely a small QFWD instance — the
posed test stands unchanged.

**Iron-law flag.**  This is the day's fourth "final object."  Its
first joint check must be: mirror-side top-layer exactness ×
quasi-FIFO dwell bookkeeping × the `(1+eps)` accounting of 31.3,
re-derived together.  Blocks 24, 28, and 37 each killed the
previous object's un-checked joint; assume this one has a
corresponding weak point until that check runs.

**Revised plank list:** (i) shallow window bijectivity, (ii) deep
window mixing, (iii) mirror exactness, (iv) joint bookkeeping.
[(a-sequencing) and (f) are absorbed into (i); the collar
constants survive only inside (iv).]

## 5.21 Block 39: the joint check cracks QFWD — corrected pollution boundary and the top-band trichotomy

The predicted joint check (mirror × quasi-FIFO × bookkeeping) ran
and found the flaw, as the iron law demanded.

**39.1 TENTH refutation: 38.2's pollution bound is false.**  A
window [a,t] realizes the set of elements ARRIVING in it; an
element pollutes if it arrives in the window and departs before
`t` — this costs only an IN-dwell (`m ± O(d)`), not a full round
trip (`n ± O(d)`).  The correct pollution-free boundary is window
length `<= m - O(d)`, NOT `n/2`.  Consequently realized sets have
size `<= m - O(d)`: co-depths `x <= Theta(d)` — including BOTH
middle layers and the ENTIRE exact zone `x <= x* << d` — lie in
the polluted band.  QFWD as stated fails exactly where
near-bijectivity is forced.  (Also fixed in passing: the band
depth must be `H* = Theta(sqrt(n log n))`, not `C sqrt n`;
absorption below `H*` is `omega(W)` by Lemma A1′, so windows must
reach co-depth `H*` — which the corrected boundary still permits,
since `H* << m`.)  ∎

**39.2 What survives.**  Co-depths `x ∈ [Theta(d), n/2]` ARE
served by quasi-FIFO windows with the LSGC multiplicity
arithmetic — the deep zone stands, modulo mixing.  The top band
`x <= Theta(d) = Theta(sqrt(n log n))` is the core, and it
carries the dominant target mass `Theta(W sqrt(n log n))`.

**39.3 The top-band trichotomy (each horn proved or
length-counted).**  For the top band:
  (i) exact window realization forces every arriving element's
      in-dwell to exceed the window, i.e. CONSTANT dwell — FIFO —
      the wreath object (the 37.1/38.2 rigidity, now sharp);
  (ii) universal refresh repair (re-issue each old element's
      letter once per dwell) costs one extra letter per arrival:
      coefficient 2;
  (iii) per-target letters cost `Theta(W sqrt(n log n))`.
None is acceptable.  The surviving design point is the convex
gap between (i) and (ii): **near-FIFO with dwell variations of
total density `o(1)`, scheduled as a scarce resource** — the
variations spent exactly where the exact zone's bijectivity
needs steering, refreshes spent at `o(1)` density on the rare
old-but-wanted elements.  An entropy check (run this block)
shows no counting obstruction to this design point: a length-`W`
word carries `W log n` bits and must merely make
`W·Theta(sqrt(n log n))` windows near-distinct, which correlated
windows can do (de Bruijn precedent).

**39.4 A falsifiable structural prediction.**  If the trichotomy
is the true shape, the known `k <= 16` OPTIMAL words must be
near-FIFO with sparse dwell irregularities (dwell variance
`o(dwell)` and irregularity density `o(1)`).  This is checkable
against the finite optima records — the first prediction this
program makes about existing data rather than asymptotics.
[Check on h100 when available, or against any stored optimal
words in the project archive.]

**Status.**  The fourth object fell at its first joint check,
consistent with blocks 24/28/37.  The corrected map: deep zone
conditional on mixing; top band = near-FIFO-with-scheduled-
variations design, open; mirror question subsumed into the top
band; bookkeeping still owed.  The main conjecture is unproven.

## 5.22 Block 40: in/out asymmetry, the tolerant m-shift, and first contact with real optima

**40.1 Refinement of 39.3 (proved).**  The pollution algebra
constrains IN-dwells only: a window's realized set is its arrival
set, and pollution means arrive-then-depart inside — an in-dwell
event.  OUT-dwells are untouched: they must average `m` (pool
size) above a small floor, but their VARIABILITY is free — and
window diversity comes precisely from choosing who re-arrives
when.  So the corrected design point of 39.3 splits cleanly:
in-dwells near-constant (`m ± O(d)`, pollution), out-dwells free
(diversity, `~log n` legitimate bits per step).  The 39.3 gloss
"near-FIFO" was half right: FIFO-like on the departure side,
free on the arrival side.

**40.2 The tolerant m-shift.**  In-dwell rigidity says exactly:
the departure stream is the arrival stream delayed by `m ± O(d)`
with local reordering inside `O(d)` windows.  Theorem D says
delay EXACTLY `m` with zero reordering and zero slack is the
doubly-exact central ucycle — the wreath object.  The surviving
design is therefore the **tolerant m-shift ucycle**: `b`-stream =
`a`-stream lagged `m` up to `O(sqrt(n log n))`-local reordering,
length slack `eps W`, windows near-bijective on the top band and
near-covering below.  Every prior surviving structure embeds:
the QFWD deep zone (windows), the LSGC arithmetic
(multiplicities), the `n = 7` finite object (smallest instance),
and the floor dial (tolerance 0 = wreath; tolerance
unbounded = pollution).  The day's two corners have MERGED: the
erosion apparatus, pushed to consistency, derived its way into
the singleton corner's object with tolerance — the map now has
one object, not two.

**40.3 First contact with real optima (archive data, k = 7).**
The stored optimal word (`k7_length37.analysis`, length 37,
realizes all 127 targets, verified line-by-line in the file)
shows: (i) every position realizes a NESTED SUFFIX-UNION CHAIN
(flag) ending there — the SIC suffix-chain mechanism of 31.3,
CONFIRMED in data; (ii) ~3.4 new targets per letter with the
rest shared at the top — the quadratic-reuse economy, confirmed;
(iii) letters are mostly PAIRS (mass 67/37 ≈ 1.8 per letter) —
the sparse-fat-letter principle of 37.3, confirmed.  The
asymptotic dwell prediction (39.4) is NOT testable at `n = 7`
(all scales collapse: `m = 3`, `d ~ m`); it remains open and
falsifiable at larger `k`.

**Status.**  40.1 proved; 40.2 is the fifth consolidated object
and by the iron law must be presumed to have an unchecked weak
joint (candidate: the interaction of out-dwell freedom with the
mean-`m` constraint under coverage demands — the out-pool is a
queue whose service discipline must simultaneously satisfy mean,
floor, and window-diversity; check that joint first); 40.3 is
data, supportive of the mechanism, silent on the asymptotic
claim.  The main conjecture is unproven.

## 5.23 Block 41: the out-pool joint check CLOSES — convergence to the multi-rank defective central ucycle

**41.1 The check (derivation).**  The window-walk on rank `m+1`
is shift dynamics by definition (a sliding window always drops
its oldest member): its FIFO character is not a design choice to
audit but a tautology of windows.  The design freedom sits
entirely in the entrant: `y_{t+1}` ranges over
`[n] ∖ X_t ± O(d)`-fuzz (the tolerance elements — in-window
members that already departed).  The mean-`m`/floor/diversity
triple is consistent: mean is forced by pool size, the floor
consumes `o(1)` of the entropy (35.2), and diversity is the
entrant choice.  NO new obstruction.  Instead, the demand "top-
band windows near-biject" IS, verbatim, the defective central
covering target of Theorem C — the day's original singleton-
corner object.  The fifth consolidated object is the first to
SURVIVE its first joint check; it does so by closing onto a
previously derived object rather than collapsing.

**41.2 The standing object (MDCU).**  **Multi-rank Defective
Central Ucycle with Tolerance:** a cyclic word of length
`(1+eps)W` over `[n]`, every letter's recurrence gaps
`n ± O(sqrt(n log n))`, whose unordered windows of length
`m+1-x` are `(1-o(1))`-surjective onto rank `m+1-x`
simultaneously for all `0 <= x <= x* = Theta(sqrt(n log log
n))`.  Given the MDCU: deeper ranks by the LSGC/Poisson margins
(35.3), far ranks by absorption (Theorem A + Lemma A1′),
assembly modulo the bookkeeping planks (31.3, collar constants).
Placement: zero-slack single-rank exact = the central
Chung–Diaconis–Graham ucycle problem (open); zero-slack ranks
`{m, m+1}` = the wreath object (open, verified `k <= 4`); GJKO
covers fixed `k` only; Mütze gives the adjacent-rank Gray
structure without recurrence rigidity; the archived `k = 7`
optimum IS the `n = 7` MDCU-analogue (all ranks, exact).  The
MDCU trades exactness for `eps`-slack, defects, and tolerance —
the three mechanisms this program contributes — at the price of
`sqrt(log log n)`-many simultaneous rank conditions.

**41.3 Honest position.**  Every counting, structural, and
compilation obstruction found today is now either cleared with
proven slack (deep zone, far ranks, statics, economy) or
characterized as a face of the MDCU demand (shallow
bijectivity).  The MDCU sits in a recognized-hard problem family
(central ucycles); the day's net contribution to IT is: (i) the
slack/defect/tolerance mechanisms, absent from the classical
formulations, each proven to relieve a specific rigidity (37.1,
34.2, 27.5); (ii) the proof that nothing else stands between the
MDCU and coefficient one (modulo the named bookkeeping); (iii)
one finite instance in hand (`k = 7`) and one posed finite test
(`n = 7` reduction, 34.1) probing whether slack beats exactness
at the smallest scale.  The main conjecture remains unproven.

## 5.24 Block 42: block factorization — the MDCU as a permutation flow

Attacking MDCU shallow bijectivity through the tolerance
mechanism yields a concrete final form.

**42.1 Block factorization (proved, elementary).**  Recurrence
gaps `n ± tau` (`tau = O(sqrt(n log n))`) are equivalent to: the
word factors into consecutive blocks that are permutations of
`[n]` up to boundary drift, with EVERY letter's position drifting
at most `tau` per block.  (Gap between consecutive occurrences =
`(n - pos_i) + pos_{i+1}`, so `|pos_{i+1} - pos_i| <= tau`.)  The
MDCU is a FLOW of orders of `[n]` — roughly `(1+eps)W/n` rounds —
with per-round displacement `<= tau`.

**42.2 Two-arc localization (proved).**  A window of length
`l ~ n/2` at split `s` inside round `i` realizes
`tail_s(pi_i) ∪ head_{l-s}(pi_{i+1})`; since consecutive orders
are `tau`-close, this is a TWO-ARC set of the local order, up to
`O(tau)` boundary correction.  Each round contributes `n` windows
per rank; the realizable sets near round `i` are exactly the
two-arc sets of the local cyclic order `± O(tau)`.

**42.3 Rotation no-go (proved; 34.2 at scale).**  If the
per-round drift is a rotation (or any order-preserving map), the
cyclic order never changes and the whole word realizes only the
`O(n^3)` two-arc sets of ONE circle — coverage fails
exponentially.  Hence the drift must genuinely shuffle: the flow
needs `omega(1)` inversions per round; bounded displacement
permits up to `~n·tau` inversions per round, so the demand is
consistent with room `~tau` — the log-`n` slack again.

**42.4 The concrete final form (permutation-flow tiling).**  MDCU
⟺ a cyclic flow of `~(1+eps)W/n` orders of `[n]`, per-letter
displacement `<= tau` per round, whose split-windows tile
`(1-o(1))` of every central rank `l ∈ [m+1-x*, m+1]` with
multiplicity `1+eps`.  This is a Tuscan/Vatican-square-like
sequencing demand at central ranks — rows are `tau`-close instead
of independent, and windows are set-unions instead of ordered
pairs.  Two refinement levers remain unexplored: (i) fat letters
(the `k = 7` optimum runs at mass/length `~1.8`, i.e. compresses
the flow — mass-time versus length-time is a free parameter the
asymptotic analysis has not yet exploited); (ii) the drift
permutations `delta_i` are almost unconstrained (`<= tau`
displacement) — the design space is a walk on `S_n` with local
generators, and the tiling demand is `n` fresh windows per rank
per round against `~n tau` available inversions.

**Status.**  42.1–42.3 proved; 42.4 is a reformulation.  The
`n = 7` search (34.1) tests exactly this flow structure at one
round.  The main conjecture remains unproven.

## 5.25 Block 43: the entropy ledger — the flow must be self-organizing

**43.1 The entropy ledger (proved, counting).**  Per round the
drift carries `log|B_tau| = Theta(n log tau)` design bits; over
`R ~ W/n` rounds the whole flow carries `Theta(W log tau) =
Theta(W log n)` bits.  The exact zone demands `W·x* =
W·Theta(sqrt(n log log n))` near-bijective windows.  Bits per
exact-zone window:

    `Theta(log n)/Theta(sqrt(n log log n)) -> 0`.

The flow cannot individually steer its windows: `(1-o(1))` of
them must land correctly FOR STRUCTURAL REASONS, with designed
corrections at density at most `~log n/sqrt(n log log n) -> 0`.

**43.2 The narrow-band principle.**  Combining the three proved
constraints: generic/random flows die by the Poisson obstruction
(32.3) and cannot be repaired within the steering budget (43.1);
order-preserving flows die by the rotation no-go (42.3);
per-round displacement is capped at `tau` (42.1), which kills
global algebraic maps (the 34.2 mechanism).  The MDCU flow, if
it exists, must be: near-identity per round, arithmetically
structured (self-organizing tiling with `o(1)` steering), yet
order-shuffling.  The search space is thus "arithmetic local
shuffles" — near-identity permutations applied by modular rules
that do not factor through the cyclic order.  The
Duffus–Kierstead–Snevily modular matchings are the canonical
candidate family of exactly this species; computing whether
their induced flow is `tau`-local is the next literature/finite
check.

**43.3 Quantitative form of the 39.4 prediction.**  The known
finite optima, if they follow this shape, should exhibit
correction density (departures from their dominant arithmetic
pattern) of order at most `log n/sqrt(n log log n)` — refining
the earlier qualitative near-FIFO prediction.

**Status.**  43.1 proved; 43.2 is an organizing principle
derived from proved parts; 43.3 is falsifiable.  The main
conjecture remains unproven.

## 5.26 Block 44: literature contact — the narrow band has a proven
depth-one exemplar, and the new obstruction is PHASE

This block executes 43.2's named check (DKS modular matchings)
and makes first substantive contact with the middle-levels
literature.  Outcome: the architecture that blocks 39.3/43.2
forced ("equivariant base + o(1)-density scheduled corrections")
is EXACTLY the architecture of the proven middle-levels and
central-levels theorems; what MDCU adds beyond them is a single
new requirement, and its cost is isolated in one new quantity:
the SPLICE PHASE.

**44.1 External cross-check of Theorem 27.4 (rotation
rigidity).**  Muetze's explicit 2-factors in the middle layer of
`Q_{2m+1}` have all cycle lengths divisible by `2n` (`n = 2m+1`;
in his notation multiples of `4n'+2`), with shortest cycle
`2·2n` and longest `2·(n-1)n`-scale, and for one parameter
choice the cycles are in bijection with plane trees
[T. Muetze, "Construction of 2-factors in the middle layer of
the discrete cube"].  This is precisely the `2ln` form that
27.4 forces on sigma-invariant 2-factors, with `l` ranging over
`Theta(1)..Theta(n)`.  The rigidity theorem is thus confirmed
against independent constructions; nothing in the literature
contradicts its gap-multiset clause.

**44.2 The two equivariant families, precisely.**  (i) LEXICAL
matchings (Kierstead–Trotter 1988; generalized in
Gregor–Jaeger–Muetze–Sawada–Wille, ICALP 2018): interpret the
bitstring as a lattice path; the `i`-lexical matching flips the
`i`-th down-step encountered scanning the (padded) path row-wise
top-to-bottom, right-to-left.  Selection is local in the HEIGHT
metric of the path.  (ii) MODULAR matchings
(Duffus–Kierstead–Snevily, JCTA 65 (1994) 334–342): for `B` in
the lower middle level, `m_i(B)` adds the `j`-th largest element
of the complement where

    `j == i + Sigma(B)  (mod m+1)`,

`Sigma(B)` the element sum.  Selection is an arithmetic modular
functional — it does not factor through the cyclic order.  Both
families are rotation-invariant and mutually non-isomorphic
(DKS).  So both fall under 27.4: their 2-factors SHATTER into
`Theta(W/l)` cycles of length `2ln`, `l <= Theta(n)` —
exponentially many cycles.  Neither family alone can produce a
single `(1+eps)W` cycle.  43.2's hope that DKS flows might BE
the MDCU is refuted at the joint, as the iron law predicts; what
survives is their role as the base flow.

**44.3 The proven exemplar.**  The middle-levels theorem
(Muetze 2016) and the central-levels theorem (Gregor–Micka–
Muetze, ICALP 2020 / JCTB 2023: Hamilton cycles through the
middle `2l` levels of `Q_{2m+1}` for ALL `l`) are proved by:
equivariant cycle factor (lexical/SCD-based) + edge-disjoint
6-cycle symmetric-difference splices at `o(1)` edge density,
glued along a spanning tree of the cycle hypergraph.  This IS
the narrow-band architecture, proven at every depth `l` — for
the CUBE-side object (rank-varying Gray walk).  The
architecture is therefore not speculative; it has carried five
published theorems.  What it has never been asked to deliver is
the MDCU's extra clause: the letter-recurrence gap band
`n ± O(sqrt(n log n))`.

**44.4 Phase obstruction (the new lemma).**  Let a glued flow be
built from an equivariant factor with cycle scale `2ln` plus
splices.  Traversing a splice from cycle `C1` into `C2` inserts
`C2`'s letter schedule into `C1`'s timeline with an OFFSET: for
each letter `a`, the gap across the splice is `n + Delta_a`
where `Delta_a` is the relative flip-phase of `a` between the
two schedules — spread `Theta(n)` for generic splices.  Each
splice therefore issues one out-of-band gap to EVERY letter
(and a second on exit).  Counting: `S` splices ~ number of
cycles ~ `W/(ln)`; out-of-band gaps `~ 2nS = 2W/l` among `2W`
total gaps — fraction `1/l`.  Hence:

  (i) coarse factors are forced: `l -> infinity`, else a
      constant fraction of gaps break the band;
  (ii) even at `l = Theta(n)` the defect density is `1/n` per
      gap, and at depth `x*` the BAND is what matters: the
      cumulative signed phase error over any `x*` consecutive
      gaps of a letter must stay `O(sqrt(n log n))` — the splice
      schedule must be BALANCED (errors cancel at scale `x*`),
      not merely sparse.

**44.5 Relative-phase rigidity.**  For sigma-orbit cycles
`C1, C2` and a sigma-orbit class of splice gadgets, rotating the
gadget by `sigma^j` shifts BOTH cycle phases by `j`: the
relative phase `delta(C1, C2; class)` is invariant within the
class.  Phase alignment is therefore NOT tunable by rotation —
it must be achieved by SELECTING AMONG gadget classes.  New
plank:

    P-phase: between any factor-cycle pair needing a splice,
    the available gadget classes realize relative phases that
    `O(sqrt(n log n))`-net the circle `Z_{2ln}` (phase-spectrum
    equidistribution), and a balanced schedule (44.4(ii))
    exists.

This is the entire remaining gap between the proven
central-levels machinery and the MDCU's gap-band clause, for
the cube-side object.  The Johnson-side transfer (windows =
departure words, 33.1) then rides on the same letter stream.

**44.6 What the ledger says now.**  The program's statement
sharpens to: TAKE the central-levels gluing machine (published,
all depths); ADD phase discipline (P-phase + balance) to its
splices; the lockstep dictionary (33.1) converts the result
into the MDCU.  The conjecture no longer requires a new
machine — it requires phase engineering of a known machine.
Falsifiable next computations (queued for h100, after the n=7
witness search): (C1) gap spectra of lexical vs modular
2-factor cycles at `n = 7, 9, 11`; (C2) relative-phase spectra
of 6-cycle gadget classes between factor-cycle pairs — a direct
test of P-phase at finite scale.

**44.7 Pre-registered predictions for computation C1** (written
BEFORE the data; falsifiability discipline).  The DKS selection
index `j == i + Sigma(B) (mod m+1)` performs a modular walk
driven by `(b-c) mod (m+1)`; if it equidistributes, arrivals
spread across the complement's order — good DIVERSITY (what the
out-pool needs, 40.1) but no reason for phase regularity.  The
lexical scan selects near path features — locally persistent,
hence better PHASE regularity, worse diversity.  Predictions:
(P-a) lexical-pair 2-factors show return-time spectra more
concentrated around `n` than DKS-pair 2-factors; (P-b) DKS-pair
cycles show flatter window/element-incidence distributions;
(P-c) if (P-a)+(P-b) hold, neither family alone meets the MDCU
band+diversity spec, and the narrow-band candidate becomes a
lexical-dominant flow with DKS-type modular corrections at
`o(1)` density — mirroring 39.3's near-FIFO endpoint.

**44.8 Computation C1 executed (h100, spectra_c1.py) — the
architecture dies at its first joint, and the death flips the
construction direction.**  Data (`n = 7, 9, 11, 13`, five
matching pairs each):

  (i) 27.4 CONFIRMED: every proper cycle of every
      equivariant-pair factor has length divisible by `2n` —
      zero exceptions across all decompositions.
  (ii) GAP SPECTRA FATAL: max return-time deviation grows
      LINEARLY — lex(0,1): maxdev `= n-3` exactly at
      `n = 7, 9, 11, 13`; dks(1,2): `4, 8, 12, 18`; the
      fraction of gaps within `n ± 1` DECREASES with `n`
      (lex(0,1): .20, .00, .10, .00).  Both families are far
      outside the MDCU band `n ± O(sqrt(n log n))` BEFORE any
      splicing.
  (iii) (P-a) weakly consistent (lexical maxdev < DKS maxdev at
      every `n`), but subsumed by (ii): neither family is a
      usable base.
  (iv) Curiosity on record: lex_0 and dks_1 share `~1.5·W/n`
      edges (whole rotation orbits) at every `n` tested.

CONSEQUENCE.  44.6's transfer plan ("borrow the central-levels
base, add phase discipline at splices") fails at the BASE, not
the splices: the published factors select flips by global
features (path rows, modular sums) with no age discipline, so
their recurrence spread is `Theta(n)` intrinsically.  The gap
band is an AGE/QUEUE property, and the only gap-perfect object
is the wreath/FIFO endpoint (p-repeat word: all gaps exactly
`n`).  Therefore the construction must run in the OPPOSITE
direction: start from the age side (rigid word, band-perfect,
coverage-poor) and drift within the gap-legal `tau`-local space
toward coverage (42.1's permutation flow) — not from the
coverage side toward bands.  The n=7 annealer, as fixed today
(rigid p-repeat start + near-adjacent swaps), IS this program
in miniature; its missing-vs-L curve is the direct finite probe
of whether age-side drift reaches coverage within `(1+eps)`
slack.  What still transfers from the literature: the SPLICING
FORMALISM (6-cycle symmetric differences, spanning-tree gluing)
and the P-phase bookkeeping — applied now to cycles of the
drift flow, not to lexical/modular cycles.

**Status.**  44.1 external confirmation; 44.2 refutation of the
naive DKS hope plus exact definitions on record; 44.4/44.5
proved at the stated level of rigor (counting and equivariance
arguments; the balance clause is a specification, not yet a
theorem); P-phase named; 44.7 pre-registered BEFORE data; 44.8
data received — sixth consecutive first-joint death (iron law
6-for-6), redirecting the base-flow search to the age side.
The main conjecture remains unproven.

## 5.27 Block 45: THE n=7 WITNESS EXISTS — first explicit
slack-beats-exactness datum

**45.1 The witness.**  h100 annealing search (lsgc_n7_search.py,
fixed per 44.8: rigid p-repeat start + near-adjacent swaps; 56
workers x 120 s rounds) found, and independent re-verification
confirmed, a cyclic word of length `L = 56` over `Z_7`:

    2 0 4 3 5 1 2 6 4 0 3 5 2 1 4 6 3 0 2 5 1 6 3 4 0 5 2 6
    3 1 0 5 4 2 3 1 0 6 5 4 2 1 0 6 5 3 4 1 0 6 2 3 4 5 1 6

with (i) every cyclic letter-gap `>= 6`, (ii) 3-windows covering
all 35 3-subsets, 4-windows all 35, 5-windows all 21, (iii)
letter counts perfectly balanced (8 each, mean gap exactly 7).
By Lemma 34.1 this IS the `n = 7, d = 2` floored LSGC.  The
zero-slack version (`L = 35`, doubly exact ucycle) is the
wreath-hard corner; at slack `eps = 0.6` the object exists.

**45.2 The missing-vs-L curve** (56 independent 120 s annealing
runs per L; NOT exhaustive — misses are upper-bound evidence
only):  `L = 42: 9 missing;  L = 49: 3 missing;  L = 56: 0.`
Slack buys coverage monotonically, as the frame predicts.

**45.3 The fingerprint.**  Gap histogram of the witness:

    gap:    6   7   8   9  10  11
    count: 28  12   8   5   2   1

FLOOR-HUGGING: the mode sits AT the floor (6), not at the mean
(7), with a decaying upper tail to `11 = n + 4`.  All deviations
lie within `~1.1 x sqrt(n log n)` — consistent with the MDCU
band.  Mechanism reading: coverage pushes gaps down (faster
recycling = more distinct windows), the floor resists, balance
pins the mean; the flow pays for floor-hugging with a few long
gaps.  The witness is NOT strictly permutation-block factorable
(drift locally exceeded +-3): the tau-local space is entered,
its strict block form is not preserved pointwise — consistent
with 42.1's `+- tau` tolerance, not with naive block rigidity.

**45.4 What this validates and what it does not.**  Validates:
(a) the age-side construction direction (44.8) reaches full
coverage at n = 7 — annealing INSIDE the gap-legal space from
the wreath endpoint works; (b) slack-beats-exactness is now a
fact, not a hope, at the smallest instance; (c) the run-floor +
multi-rank window frame (34.1) is consistent.  Does NOT
establish: (a) any scaling in `n` (single tiny instance; the
MDCU needs `eps = o(1)`); (b) nonexistence at `L = 42, 49`
(search not exhaustive); (c) anything about the exact zone at
depth `x*` (n = 7 has no meaningful `x*`).  Next computation
(C3, launched): the n = 9 analogue (GAP 8, windows 4/5/6,
L in 126..180) — the first two-point read on `eps(n)`.

**Status.**  Witness verified independently; curve and
fingerprint recorded; C3 running.  The main conjecture remains
unproven.

## 5.28 Block 46: the innovation bound and the three-layer anatomy
of the witness

**46.1 Lemma (shift-defect innovation bound; PROVED).**  Let `w`
be a cyclic word of length `L` over `[n]` and let

    `D = { q in Z_L : w_q != w_{q+n} }`

be its shift-defect set.  Then the number of DISTINCT k-windows
(as sequences, hence a fortiori as sets) satisfies

    `#distinct <= gcd(L, n) + k·|D|.`

Proof.  The shift `p -> p+n` partitions `Z_L` into `gcd(L,n)`
orbits.  Along an orbit, consecutive windows `W_p, W_{p+n}` are
EQUAL unless `[p, p+k)` meets `D`; so the number of distinct
windows along an orbit is at most `1 +` the number of orbit
steps whose window meets `D`.  Each `q in D` lies in exactly `k`
windows, and each window position lies in exactly one orbit;
summing gives the bound.  QED.

Corollary (rigid no-go, quantitative).  All gaps exactly `n`
means `D` is empty (`L` a multiple of `n`), so at most `n`
distinct windows — the wreath endpoint's coverage death, now
with a counting proof.  Conversely the MDCU (distinct set
windows `>= (1-o(1))·W` at the central rank, `k ~ n/2`) FORCES

    `|D| >= (1-o(1))·2W/n` — deviation mass is NECESSARY at
    density `>= ~2/n` of positions.

This is the first quantitative lower bound on how far the flow
must sit from the wreath endpoint; it is compatible with the
entropy ledger because dense deviations can be low-entropy
(quasiperiodic), see 46.3.

**46.2 The witness anatomy (data).**  Per-letter gap sequences
of the L=56 witness are SLIP-AND-RESET SAWTOOTHS: runs of
floor-gaps `6` (phase slips `-1` per return against the rigid
`7`-lattice) punctuated by one or two long resets (`8..11`),
e.g. letter 0: `8 8 7 6 6 6 6 9`; letter 3: `7 6 6 6 6 11 6 8`.
Letters' sawtooths are mutually desynchronized.  Shift-defect
density `|D|/L = 0.79` (far above the necessary `2/n = 0.29`).
Innovation is near-perfect: distinct sequence-windows
`50/56, 55/56, 56/56` for `k = 3, 4, 5` — the word is nearly
aperiodic at window scale, while as sets the windows compress
exactly onto the `35/35/21` targets.

**46.3 Three-layer anatomy (synthesis).**  The witness realizes:
  LAYER 1 (lattice): balanced counts, mean gap exactly `n` —
    the rigid skeleton;
  LAYER 2 (quasiperiodic slippage): dense floor-hugging slips,
    sawtooth phase drift per letter — supplies the innovation
    mass demanded by 46.1 at near-zero entropy (rotation-like
    dynamics; the finite analogue of irrational-slope Beatty
    schedules).  Rational slopes are the affine no-go (34.2);
    irrational slopes do not exist in finite cyclic words —
    hence the sawtooth desynchronization and resets are FORCED
    finite substitutes;
  LAYER 3 (sparse corrections): the specific placement of
    resets — long gaps are extended out-dwells, i.e. exactly
    the diversity events of 40.1 — is the residual design
    freedom (the `o(1)`-density steering of 43.1).
Open micro-questions, flagged not claimed: why the mode sits AT
the floor rather than balanced `+-1` around the mean (in-dwell
economy 39.1 is the suspect); whether the necessary deviation
density `2/n` or the observed `0.79` is the true scaling (the
gap between them is unexplained).

**46.4 Dispersion data: the witness is a TILING, not a lucky
cover.**  Window-multiplicity histograms of the L=56 witness
against the Poisson baseline (random cover at the same
`lambda = L/W_k`):

    k=3 (lambda 1.60): {1:18, 2:13, 3:4}, var/mean = 0.29
    k=4 (lambda 1.60): {1:19, 2:11, 3:5}, var/mean = 0.33
    k=5 (lambda 2.67): {1:4, 2:4, 3:8, 4:5}, var/mean = 0.40

Poisson dispersion is 1.0 and would leave `~7` rank-3 targets
uncovered at this `lambda`.  Sub-Poisson dispersion by a factor
`2.5–3.5` at every rank: the annealer converged to a
near-uniform self-organized tiling — the regime 43.1 requires —
not to the random-cover regime that the Poisson obstruction
(32.3) rules out.  Also noted (duality, no extra constraint):
rank-k window coverage is identically the complementary-rank
missing-set coverage; the absence-mass identity
`sum(g - k) = L(n-k)` is tight, so all design freedom lives in
overlap structure, none in absence budget.

**Status.**  46.1 proved (five lines, airtight); 46.2/46.4
data (sub-Poisson tiling confirmed); 46.3 synthesis with two
flagged open calibrations.  The main conjecture remains
unproven.

## 5.29 Block 47: the balance clause dissolves; P-phase upgrades to
splice compatibility (type + phase)

**47.1 No-accumulation lemma (PROVED).**  In a glued flow, all
gaps after a splice are gaps OF THE NEW CYCLE's schedule: the
only gaps affected by a splice are the `n` gaps that SPAN it
(one per letter).  Hence splice-induced phase errors do not
accumulate along any letter's timeline — each splice is charged
exactly one gap per letter, and afterwards the flow carries the
new cycle's internal band `B_0` with no memory of the splice.
Proof: immediate from the definition of gaps as differences of
consecutive occurrences; occurrences after the splice point all
lie in the new schedule.  QED.

Consequence: 44.4(ii)'s "balanced splice schedule" clause — an
n-dimensional Steinitz/prefix-balancing requirement as stated —
is UNNECESSARY.  Withdrawn from the plank list.

**47.2 The order-matching derivation (what P-phase really is).**
Let the flow exit `C1` at `u` and enter `C2` at `v`.  For letter
`a`, the spanning gap is `s_a + t_a` where `s_a` = age of `a`'s
last occurrence at `u` (in `C1`'s schedule) and `t_a` = wait
until `a`'s next occurrence after `v` (in `C2`'s schedule).
Ages `{s_a}` and waits `{t_a}` are each near-permutations of
`{0..n-1}` (band-`B_0` schedules).  ALL spanning gaps in
`n ± B` requires `t_a ~ n - s_a` for every `a` simultaneously:
the return ORDER at `v` must equal the departure ORDER at `u`.
A single rotation offset (scalar phase `delta`) suffices ONLY
when both local schedules are near-rotations of the SAME base
permutation.  So the true splice constraint is two-part:

    P-align (upgraded P-phase): the gadget must join the two
    cycles at points of (i) matching local permutation type
    (up to `B_0` drift) and (ii) rotation phase within `B`.

In the age-side drift flow (44.8), local permutation type
varies slowly (`tau`-local drift), so each cycle sweeps a path
through type space; two cycles are spliceable wherever their
type paths pass within `B_0` of each other.  P-align is thus a
REACHABILITY/INTERSECTION condition on type paths — checkable
at finite scale on the drift-flow cycles (queued as C4).

**47.3 Net effect on the plank ledger.**  Removed: balance
clause (47.1).  Sharpened: P-phase -> P-align (47.2).
Unchanged: coarse factors forced (44.4(i)), innovation mass
`>= 2W/n` (46.1), self-organized tiling regime (46.4 evidence).
The splice theory is now: one gap per letter per splice, in
band iff P-align holds at the joint; splice density `1/l` sets
the defect budget spent on joints.

**Status.**  47.1 proved; 47.2 derivation (elementary, recorded
in full); 47.3 ledger update.  The main conjecture remains
unproven.

## 5.30 Block 48: the interval-sweep skeleton and ragged-cut
amplification

**48.1 Interval-sweep reformulation.**  In the round picture
(42.1), a window of length `k` starting `s` positions before a
round boundary has content `tail_s(pi_r) ∪ head_{k-s}(pi_{r+1})`
(42.2).  When the walk is `tau`-local this is, up to per-letter
phase offsets, the complement of a middle interval of the
common local order: the MDCU coverage clause becomes — a walk
`(pi_r)` in `S_n` under adjacent transpositions whose
middle-interval complements sweep `(1-o(1))` of every central
rank with multiplicity `1+eps`.

**48.2 The demand is discrepancy, not volume (counting).**  An
adjacent transposition refreshes `~2n` interval contents, so
fresh-set VOLUME needs only `Theta(1)` transpositions per round
(consistent with, and sharpening, 42.3's `omega(1)`).  The
binding demand is NEAR-INJECTIVITY of the sweep `(r, cut) ->
set` (slots per rank `= (1+eps)W`, targets `W`).  Random walks
fail it (Poisson multiplicities — 32.3); periodic schedules
(brick-wall/odd-even networks) fail it (contents recycle at the
period).  The object is a LOW-DISCREPANCY TRANSPOSITION WALK: a
partial path in the Cayley graph of `S_n` (adjacent
transpositions — SJT/Gray-code species) of length `~(1+eps)W/n
<< n!` whose interval contents nearly never collide.  This is
the crispest algebraic form of the sequencing theorem (36's
sole hard core) to date.

**48.3 Witness data: the walk is real; raggedness is the
majority diversity channel.**  Extracting round permutations
from the L=56 witness (r-th occurrences in position order):
consecutive Kendall distances `1,1,2,3,0,2,3,2` — total 14
inversions, mean `1.75` per round: the `Theta(1)` regime of
48.2, and the block-factorization picture 42.1 validated on
data.  BUT clean linear intervals of the eight round
permutations supply only `15/35, 12/35, 7/21` distinct sets
(34 of 91) — the witness covers everything, so the MAJORITY of
coverage is carried by RAGGED CUTS: the desynchronized phase
sawtooths (46.2) make actual windows slice the age order at
per-letter offsets, multiplying the variety of sets per round
far beyond clean intervals.  NAMED MECHANISM — ragged-cut
amplification: layer-2 phase spread feeds coverage through two
channels, (a) driving the transposition walk, (b) re-cutting
each round's order raggedly so that few transpositions per
round suffice.  Raggedness adds variety per slot, not slots:
the near-injectivity demand stands, but collisions between
nearby windows are naturally decorrelated.  OPEN (flagged): the
asymptotic bookkeeping of ragged amplification — whether phase
spread `B_0` yields the full `(1-o(1))` variety at `x*` depths,
or only a poly(`B_0`) factor that still leaves a designed-walk
core.

**Status.**  48.1/48.2 proved at the stated level (elementary
counting; reformulation exact up to `O(tau)` boundary effects);
48.3 data plus one flagged open calibration.  The main
conjecture remains unproven.

## 5.31 Block 49: the rule-class landscape (C5–C8) and the
semi-random escape from the Poisson obstruction

Four computations on h100 (walk_c5.py, sched_c6.py, sched_c7.py,
sched_c8.py + composite variant) map the space of streaming
rules for the floored word at slacks 1.2–1.6, n = 7..15:

**49.1 Empirical no-go: closed-form arithmetic priorities.**
Fixed quasiperiodic rules — golden-position swap schedules (C5),
time-Sturmian perturbed FIFO (C6), per-letter phased lateness
(C7, 48 parameter configs) — all: (i) lose to RANDOM
tie-breaking at `n >= 9` (e.g. n=11, L=748: sturm 519, phased
516, random 320 missing); (ii) degrade with `n`; (iii) sit
5–10x off the annealed frontier.  C5's clean-interval sweeps
collide at ~90% for every schedule tested (coverage 0.02–0.36
vs Poisson 0.70) — confirming 48.3 from the other side: the
clean-interval channel is weak, and fixed arithmetic priorities
inherit 34.2-type self-similar collision patterns.  The
narrow band is NOT inhabited by few-parameter closed forms.

**49.2 The feedback species wins.**  Freshness-greedy (C8):
among eligible letters pick the one completing the fewest
already-seen window contents — deterministic given history,
i.e. ZERO design bits, fully entropy-ledger compatible.  It
beats every fixed rule by 2.5–4x (n=9 L=207: 27 vs 70–111;
n=11 L=748: 126 vs 320–519) and is the first rule class to
approach the annealed frontier (2–3x off).  Its failure mode is
LIMIT-CYCLE SATURATION: at n=13 extra slack buys nothing
(732 = 732 at slacks 1.4/1.6) — the deterministic groove
revisits covered contents.  Blind desynchronization (C8b,
golden tie-break + 12% forced second choice) breaks the
saturation (875 -> 687, improving in slack again) but damages
small-n sharpness; the right perturbation is ADAPTIVE (escape
on plateau), queued as C9.

**49.3 Control results.**  FIFO covers EXACTLY `n` sets per
rank at every `n` tested — Lemma 46.1's corollary is data-exact.
Annealed baselines: n=7 perfect at slack 1.6 (block 45); n=9 in
progress (best so far 13 missing at L=162, 4 at L=180).

**49.4 The semi-random escape (new attack plan).**  The Poisson
obstruction (32.3) rules out OBLIVIOUS random placement: its
derivation requires window contents independent of the coverage
state.  Adaptive random greedy — the randomized freshness
scheduler — is NOT subject to it; it is precisely the
semi-random (nibble) method in streaming form.  Proposed proof
engine for the exact zone: analyze the random freshness-greedy
scheduler by the differential-equation method (Wormald):
track staleness statistics (fraction of eligible letters
completing seen contents at each rank), prove concentration,
and show coverage reaches `(1-o(1))W` per central rank within
`(1+eps)W` steps before freshness exhausts.  Obstacles, named:
(i) the seen-set state is exponential — the DE method needs the
staleness counts to be trackable by `O(1)` statistics per rank
(a self-correcting property to prove, not assume); (ii) the
gap floor couples eligibility to the schedule (queue dynamics —
but this part is PBBS-adjacent and well understood from Q1–Q5);
(iii) depth-`x*` simultaneity (all central ranks at once).
This is the first attack on the sequencing theorem with a
standard asymptotic tool attached.

**Status.**  49.1–49.3 data (scripts and outputs preserved);
49.4 is a plan with named obstacles, not a result.  The main
conjecture remains unproven.

## 5.32 Block 50: the staleness DE at depth one — the heuristic
solution reproduces the program's rates, and the gap gets a name

**50.1 Queue arithmetic (proved).  [AUDIT CORRECTION
2026-08-21: the pool is `sigma + 1`, not `sigma` — see the
exact count in 57.1; the Little's-law computation below has an
off-by-one at the eligibility boundary (the letter at age
exactly `f` is already eligible).  The C10 measured pools
`2.08, 3.07, ...` display `sigma_nom + 1` plus a small seeding
artifact (the simulator's `last` initialization was
inconsistent with its seeded word — script since fixed).]**
Floor `f = n - sigma`, one
placement per step, balanced counts (mean gap `n`).  A letter
enters the eligible pool at age `f` and leaves at placement;
by Little's law the mean pool size is `E[gap] - f = sigma`.
Consequences: (i) at the finite-test floor `f = n-1` the pool
hovers at `~1` — the n=7/n=9 searches ran the TIGHTEST corner,
and the n=7 witness exists even there; (ii) at the MDCU floor
`sigma = C sqrt(n log n)` the pool is `Theta(sqrt(n log n))`,
i.e. `~(1/2) log n` choice bits per step — precisely the 35.2
entropy dial.  The scheduler's choice supply and the floor dial
are the same object seen twice.

**50.2 The depth-one DE.**  Rank `k ~ m+1`, coverage fraction
`rho(t) = N(t)/W`.  Since eligible letters have age
`>= n - sigma > k`, none lie in the current (k-1)-prefix: every
eligible completion is a valid k-set (no wasted choices).
Under the LOCAL UNIFORMITY hypothesis (LUL, below), each of the
`~sigma` eligible completions is independently stale with
probability `~rho`, so the fresh-placement rate is
`1 - rho^sigma` and, in scaled time `tau = t/W`:

    `d rho / d tau = 1 - rho^sigma.`

Since `rho^sigma = e^{-sigma(1-rho)(1+o(1))}`, the right side
stays `1 - o(1)` until `1 - rho ~ (log sigma)/sigma`; the
solution reaches

    `rho = 1 - O(log sigma / sigma) = 1 - O(log n / sqrt(n log n))`

within `tau = 1 + o(1)`, i.e. within `(1+o(1))W` steps.  The
heuristic DE therefore delivers exactly the MDCU depth-one
clause — `(1-o(1))`-coverage at slack `o(1)` — and the residual
defect rate `log sigma/sigma` MATCHES the 43.3 correction
density `~log n/sqrt(n·log log n)` in shape.  Three independent
derivations (entropy ledger 43.1, finite fingerprints 45.3,
staleness DE 50.2) now give the same defect scale.

**50.3 The Local Uniformity Lemma (the precise gap).**  LUL:
under the randomized freshness-greedy dynamics with pool
`sigma`, for all but `o(L)` steps, the stale fraction of the
current eligible completion fan equals `rho(t) + o(1)`.
What makes it nontrivial: consecutive prefixes overlap in `k-2`
letters, so completion fans drift slowly and coverage is
locally correlated; the pool's random choices must decorrelate
faster than the fan drifts.  This is a quasirandomness
self-correction statement — the exact zone's difficulty in its
final, isolated form.  (It replaces obstacle (i) of 49.4.)

**50.4 The multi-rank system (shape; no analysis claimed).**
One placement completes one window at EVERY rank
simultaneously (nested flags — 35.1's band structure).  Joint
freshness across `x*` ranks fails at late stage
(`P ~ delta^{x*}`), so the multi-rank greedy must rotate
attention: weighted scores `sum_j w_j fresh_j` with evolving
weights, giving a coupled DE system for `(rho_j)`.  Two
favorable counts: the pool exceeds the rank count by
`sigma/x* = sqrt(log n / log log n) -> infinity`, and capacity
is one fresh window per rank per step — no volume obstruction.
The coupling analysis is open.

**Status.**  50.1 proved; 50.2 heuristic solution of a
well-posed DE (conditional on 50.3); 50.3 the isolated gap,
stated precisely; 50.4 formal shape only.  The main conjecture
remains unproven.

## 5.33 Block 51: THE n=9 WITNESS — the fingerprints replicate,
and the scaling read is favorable

**51.1 C3 final curve** (56 x 300 s annealing per L; upper
bounds): missing of 336 targets at
`L = 126/135/144/153/162/180 = 48/36/27/19/13/3`.  Matched-slack
missing FRACTIONS vs n=7:  slack 1.2: `5.7%` vs `9.9%`; slack
1.4: `0.9%` vs `3.3%` — a `3.7x` improvement at the larger `n`.
Required slack for fixed coverage quality DECREASES from n=7 to
n=9: the direction `eps(n) = o(1)` requires.

**51.2 The witness.**  Targeted finisher (600 s tasks,
L in {180, 189, 198}) found, and independent verification
confirmed, a cyclic word of length `L = 198` over `Z_9` (word
recorded in lsgc_n9b.log on h100 and reproduced in the C3b
script record): all letter-gaps `>= 8`, windows of lengths
4/5/6 cover `126/126, 126/126, 84/84`.  `eps(9) <= 0.571`,
below the n=7 bound `0.6`; whether `L = 189` or `180` admit
witnesses is open (the 180-curve reached 3 missing).

**51.3 Fingerprint replication (2-for-2).**  All four n=7
signatures hold at n=9:
  balance: counts exactly 22 each (mean gap exactly `n = 9`);
  floor-hugging: gap histogram
    `{8:108, 9:40, 10:20, 11:14, 12:6, 13:8, 14:2}` — mode AT
    the floor (54.5% of gaps), decaying tail to `n+5`; max
    deviation `5 ~ 1.1 x sqrt(n log n)` — the SAME band
    constant as n=7;
  sub-Poisson tiling: multiplicity var/mean `0.40/0.37/0.40`
    across ranks (n=7: 0.29-0.40) — the self-organized regime,
    not coupon collection;
  round walk: Kendall steps mean `3.36`/round (n=7: `1.75`) —
    slowly growing, `omega(1)`-consistent, far under the
    `tau`-local cap.

**Status.**  Witness verified; curve recorded; fingerprints
replicate at both available scales.  The main conjecture
remains unproven — these are finite data points consistent
with the MDCU frame, not asymptotic theorems.

## 5.34 Block 52: the DE is quantitatively right — LUL holds
empirically in the operative regime

**52.1 C10 design.**  Exact simulation of the 50.2 model:
randomized freshness-greedy at focus rank `k = m+1`, floor
`n - sigma_nom`, slack 1.2, five seeds, n = 11 and 13;
DE integrated per rank with the MEASURED mean pool.

**52.2 Result table (focus-rank coverage, sim vs DE):**

    n=11: pool 2.08: .770/.845 | 3.07: .892/.902 |
          4.05: .935/.934 | 5.04: .957/.954
    n=13: pool 2.03: .776/.838 | 3.03: .891/.897 |
          4.02: .927/.931 | 5.02: .951/.952

From pool `>= 3`, simulation matches the DE to `0.001-0.01` at
BOTH n — and coverage is a pure function of `(sigma, tau)`,
independent of `n`, exactly as the DE asserts.  The deviation
at pool `~2` is the choice-starved regime (LUL correlation
effects when the scheduler is nearly forced).

**52.3 Consequences.**  (i) The Local Uniformity Lemma (50.3)
is TRUE empirically in the operative regime — the isolated gap
of the depth-one analysis is a real, apparently provable
regularity, not a hopeful assumption.  (ii) The semi-random
engine (49.4) behaves asymptotically as designed: miss falls
with pool size along the DE curve; at the MDCU pool
`sqrt(n log n)` the extrapolated miss is `o(1)`.  (iii) The
side ranks lag (~0.75 coverage, untended) — the multi-rank
attention-rotation layer (50.4) is confirmed necessary and is
now the binding open design problem, ahead of LUL in
difficulty.  Priorities reordered accordingly: (a) multi-rank
weighted-freshness DE system, (b) LUL proof at pool
`omega(1)`, (c) queue-floor coupling bookkeeping.

**Status.**  52.1–52.2 data (script preserved); 52.3
consequences with reordered priorities.  The main conjecture
remains unproven.

## 5.35 Block 53: the multi-rank wall, and the final decomposition
— sequence-SAW plus fiber discrepancy

**53.1 The multi-rank wall (for feedback schedulers).**  Shallow
ranks (`x <= sqrt n`, hence `W_k = Theta(W)` and `tau_k =
L/W_k = Theta(1)`) each require BULK fresh rate `~W_k/L`
throughout the run — coverage `(1-o(1))W_k` from `(1+eps)W`
slots is a bulk property, not an endgame property.  A scheduler
whose choice optimizes `O(1)` ranks per step gives rate `~1`
to the focused rank and only the oblivious rate `~(1-rho)` to
the others (C10 data: side ranks stall at `1 - e^{-tau}`);
deficits `Theta(W)` per shallow rank times `Theta(sqrt n)`
shallow ranks overwhelm the `eps W` focus budget by a factor
`sqrt n`.  Per-rank feedback CANNOT reach the MDCU.

**53.2 Correlation is not the rescue (data).**  Cross-rank
fresh-event correlations on both witnesses are positive but
weak: n=9: `corr(f4,f5) = +0.37`, `P(f5|f4) = 0.77` vs base
`0.64` (about 1/4 of the maximal lift given the margins); n=7
adjacent pairs `+0.16` and `-0.01`.  Nested-flag cascading, as
a correlation phenomenon, is too weak to carry the budget.

**53.3 The resolution and final decomposition.**  The witnesses
nevertheless achieve MAXIMAL fresh rate at every rank
(`f_k = W_k/L` exactly — full coverage).  The mechanism is not
feedback and not correlation: it is BULK APERIODICITY of the
trajectory itself.  Decompose window collisions at rank `k`
into (i) SEQUENCE collisions (same ordered window) and (ii)
REORDER collisions (same set, different order).  Then:

  (a) sequence-injectivity is MONOTONE: distinct length-k
      sequence windows imply distinct length-(k+1) windows.
      So near-self-avoidance at the SHORTEST shallow length
      gives it at ALL shallow lengths at once — one property,
      not `x*` properties.  (Witness data: 50/56, 55/56, 56/56
      distinct sequences.)  Innovation mass for it is priced by
      Lemma 46.1.
  (b) the entire remaining demand is that the sequence -> set
      map's fibers are hit EQUIDISTRIBUTEDLY — each rank-k set
      collected `1+eps` times rather than a few sets collected
      often.  This is precisely the sub-Poisson dispersion
      fingerprint (46.4, replicated at n=9): the design core of
      the MDCU is a FIBER-DISCREPANCY property, nothing else.

FINAL DECOMPOSITION.  MDCU = floor/queue bookkeeping (50.1,
manageable) + sequence-SAW (aperiodicity; one monotone
property; innovation mass priced) + fiber discrepancy of the
content map (the core; empirically = sub-Poisson dispersion
~0.4 at both scales).  The `x*`-fold multiplicity of demands is
gone: two trajectory properties suffice at every depth
simultaneously.

**Status.**  53.1 semi-quantitative wall (C10 side-rank data in
evidence); 53.2 data; 53.3 the decomposition is exact at the
level of definitions (collision split is a partition;
monotonicity of (a) is a two-line proof) — what remains
unproved is EXISTENCE of a flow with both properties at scale.
The main conjecture remains unproven.

## 5.36 Block 54: the move-to-front compilation — the core lands in
a known genre

**54.1 The compilation (exact; two-line proofs).**  Under gap
floor `>= k`, the letter placed `j` steps ago has age exactly
`j`; ages are distinct; hence the rank-`k` window content at
every time is EXACTLY the top-`k` of the recency order, for
every shallow `k` at once (the nested flags are the LRU stack
property).  Placement = move-to-front on the recency
permutation `rho_t in S_n`.  The floor `n - sigma` says: only
the last `sigma + 1` letters of `rho_t` (the LRU tail) are
eligible to move [AUDIT CORRECTION 2026-08-21: tail size
`sigma + 1`, matching 57.1; "sigma" here was the off-by-one].
[AUDIT CORRECTION 2026-08-21: "balance is automatic" is
WITHDRAWN — closure of the walk does NOT force balanced
counts; the floor forces only `count_x <= L/(n - sigma)`, so
counts are constrained above by `(1 + O(sigma/n)) L/n` but a
letter can in principle be starved.  Near-balance must be
imposed as part of the object or derived from the covering
demand; the witnesses happen to be exactly balanced.]
Slack is the time budget.  Therefore, with near-uniform
fibers stated as an explicit CONDITION (not a consequence of
closure):

    MDCU  <=>  a closed sigma-tail move-to-front walk on `S_n`
    of length `(1+eps)W` whose top-k prefix sets visit
    `(1-o(1))·C(n,k)` sets with fiber multiplicity `1+eps`,
    for all shallow `k` simultaneously.

The design freedom is the choice among the `sigma` tail
letters: `log sigma ~ (1/2) log n` bits per step (50.1's dial,
third appearance).  The rigid word is round-robin request order
— the classical LRU worst case; the MDCU wants the opposite
extreme: near-maximal LRU-state diversity at every capacity.

**54.2 What the compilation buys.**  (i) The state space is
cleanly `S_n`; the deviation band lives only in the tail
restriction.  (ii) Sequence-SAW and fiber discrepancy (53.3)
become one statement: the prefix-content process of the MTF
walk has near-uniform fiber counts.  (iii) Random tail choices
give Poisson fibers (dies — 32.3, and C6 randtie in data); the
core is DERANDOMIZING Poisson into sub-Poisson using the
`log sigma` bits/step — a constructive sequential-discrepancy
problem on the MTF graph.

**54.3 Literature contacts (three, all new to the program).**
(a) LRU/list-update theory: top-k nesting = Mattson stack
algorithms; state-universality of LRU stacks appears unstudied
— worth a search.  (b) Online discrepancy minimization
(Bansal et al.): our setting is EASIER than adversarial online
— the walk chooses its own arrivals (constructive, offline).
(c) Euler tours in hypergraphs (Glock–Joos–Kuehn–Osthus): the
demand "closed walk hitting almost every fiber `1+eps` times"
is an approximate-Euler-tour statement on a quotient of the
MTF graph; iterative absorption with `eps`-slack is the
candidate heavy machinery — the first time the core has a
theorem-shaped target for an existing method.

**Status.**  54.1 proved (the compilation is exact); 54.2
restatement; 54.3 directions.  The main conjecture remains
unproven.

## 5.37 Block 55: absorption on the MTF graph — cleanup works, the
bulk is the single remaining question

**55.1 Literature note.**  MTF/LRU under RANDOM requests is
classical analytic combinatorics (Flajolet–Gabarro–Thimonier
1992: the Markov chain on `k!·C(n,k)` ordered cache states,
stationary laws — the Poisson side of our dichotomy).  Designed
request sequences achieving near-uniform state sweeps appear
UNSTUDIED.  The MDCU core is an open corner of a classical
framework.

**55.2 The absorption sketch and where it holds.**  GJKO-style
plan: bulk phase covers `1-delta` of fibers; sweep-absorbers
clean up.  The CLEANUP half is sound: nibble leftovers are
sparse and quasirandom; chaining `delta·W` target states by
overlap, with tail-drift scheduling (elements drift into the
sigma-tail at rate one; assigning targets to drift windows is
a deficiency-Hall problem — 36.2's machinery), visits them at
`O(1)` amortized steps each; total `O(delta W) <= eps W` for
any `delta = o(1)`.  This replaces a bookkeeping plank with a
plausible lemma (P-sweep).

**55.3 The wall reappears in the bulk (and localizes THE
question).**  If the bulk phase uses random tail choices, every
shallow rank is left with a POISSON deficit `e^{-lambda} =
Theta(1)` — and absorption cannot fix `Theta(W)` leftovers at
`Theta(sqrt n)` ranks: flag alignment across ranks of
independent leftover families occurs at rate `delta^2` (53.2's
weak correlations), so sweeps serve ranks one at a time —
the 53.1 budget wall, verbatim.  Hence absorption is a
CLEANUP tool only; the bulk must be sub-Poisson BY STRUCTURE.
Everything now rests on one clean question:

    SUB-POISSON WALK QUESTION.  Does there exist a sigma-tail
    move-to-front walk on `S_n` of length `(1+eps)W` whose
    top-k fiber counts are sub-Poisson (var/mean bounded below
    1, misses `o(W_k)`) at every shallow rank simultaneously?

The witnesses answer YES at `n = 7, 9` (var/mean `~0.4`).

**55.4 The witnesses' pull-position law (new fingerprint).**
In MTF terms the n=9 witness pulls the YOUNGEST eligible letter
55% of the time (gap = floor), with a decaying tail over older
positions — a LIFO-WITHIN-TAIL bias, the opposite of FIFO.
Pure LIFO starves letters (density `n/(n-1) > 1` — impossible),
so the decaying law is LIFO tempered by starvation control.
Queued C12: the one-parameter family "pull the j-th youngest
eligible with probability `~ beta^j`" tested directly against
the sub-Poisson criterion — the cheapest live candidate for
the bulk structure.

**Status.**  55.1 literature; 55.2 plausible-lemma reduction
(P-sweep, not proved); 55.3 the localized core, with the wall
argument recorded; 55.4 data + queued test.  The main
conjecture remains unproven.

## 5.38 Block 56: C12 — the pull-law census closes; the Sub-Poisson
Walk Question stands alone

**56.1 C12 result.**  The beta-LIFO family (pull the j-th
youngest eligible w.p. `~beta^j`, the witnesses' marginal law)
achieves at best dispersion `0.7-0.9` with POOR coverage
(n=9: 67 missing of 336 vs the witness's 0; n=13: 1159 of
4719).  The witnesses' pull-position law is a SYMPTOM of their
organization, not its mechanism: matching the marginal does not
reproduce the structure.

**56.2 The census (C5-C12, closed).**  Tested and failed:
fixed arithmetic priorities (three families); pure random;
random tie-break; per-letter phased lateness; single-rank
freshness feedback (walls at multi-rank); freshness + blind
desync; beta-LIFO marginals.  Succeeded at finite n: full
annealing only (n=7 at eps 0.6, n=9 at eps <= 0.571).  No
memoryless or short-memory policy found inhabits the band.
The annealed witnesses' choices correlate with the full
recency state in a way no tested marginal captures.

**56.3 Standing.**  The program's open core is exactly the
Sub-Poisson Walk Question (55.3), now with strong negative
evidence that it is not resolved by simple policies, and
existence evidence at two scales.  Next mathematical moves,
in order: (i) prove the depth-one theorem rigorously (DE +
LUL — the single-rank case is within reach and worth having);
(ii) feature-discovery on the witnesses (which state statistic
do annealed choices track?); (iii) n=11 existence.

**Status.**  Census data recorded; the core question isolated
and hard.  The main conjecture remains unproven.

## 5.39 Block 57: two of the three components PROVED for the random
walk — exact pool and sequence-SAW

**57.1 Lemma (exact pool; PROVED).**  With floor `n - sigma`
and one placement per step, EXACTLY `sigma + 1` letters are
eligible at every step.  Proof: last-placement times are
distinct, so ages are distinct; the letters placed in the last
`n - sigma - 1` steps are distinct (floor) and have ages
`1..n-sigma-1`; every other letter has age `>= n - sigma`.
QED.  (C10's measured pools `2.08/3.07/4.05/5.04` at
`sigma_nom = 1/2/3/4` confirm to the decimal — the small excess
over `sigma_nom` is the `+1` plus seed-round edge effects.)
Consequences: the `sigma`-tail MTF walk is exactly
`(sigma+1)`-out-regular; the DE rate is exactly
`1 - rho^{sigma+1}` modulo LUL; the queue-stability plank of
49.4 is DISCHARGED — there is nothing stochastic about the
pool.

**57.2 Lemma (sequence-SAW for the random walk; PROVED, first
moment).**  Let the walk choose uniformly among the
`sigma + 1` eligible letters, `sigma + 1 >= n^c` for some
`c > 0` (the MDCU floor gives `sigma ~ sqrt(n log n)`).  For
any window length `k >= k_0 = Theta(n / log n)`, the expected
number of pairs `s < t` whose length-`k` letter sequences
coincide is at most

    `L^2 (sigma+1)^{-k} = e^{2 ln L - k ln(sigma+1)} -> 0`,

since `ln L ~ n ln 2` while `k ln(sigma+1) >= (n/2)(c ln n)`.
(Each copied step requires the prescribed letter to be chosen:
probability `<= 1/(sigma+1)` given the past, by 57.1.)  Hence
whp the walk has NO sequence collisions at any shallow window
length simultaneously — sequence-SAW holds with an
`e^{-Theta(n log n)}` margin.  QED.

[AUDIT CORRECTION 2026-08-21 (third audit, block 69): the
stated threshold `k >= Theta(n/log n)` is broader than the
displayed calculation supports — the display substitutes
central `k = Theta(n)`, which is where the
`e^{-Theta(n log n)}` margin comes from.  The honest statement
is: the first moment vanishes when `k ln(sigma+1) > 2 ln L`,
i.e. `k > (2 ln 2 + o(1)) n / ln(sigma+1)`, with margin
`e^{-Theta(n)}` near that threshold and `e^{-Theta(n log n)}`
only at central `k`.  57.2 is used in this program only at
shallow (central) ranks, where the display is correct.]

**57.3 Standing after 57.1–57.2.**  Of the final decomposition
(53.3): floor/queue — PROVED EXACT (57.1); sequence-SAW —
PROVED whp for the unmodified random walk (57.2); fiber
discrepancy — open, and now provably the ONLY random-walk
deficiency: whp every set-fiber multiplicity is purely reorder
multiplicity, so the Poisson misses of the random walk (C6
randtie data) are entirely reorder-collision maldistribution.
The Sub-Poisson Walk Question is thus, rigorously: can
`log(sigma)` bits/step of tail-choice design redistribute
REORDER collisions to near-uniformity?  Also noted: 57.2's
margin survives conditioning on polynomially many events —
freshness-modified walks (which reweight choices by `O(1)`
factors per step against the uniform walk on any event of
probability `>= e^{-o(n log n)}`) inherit sequence-SAW by a
tilted first moment, so the two proved components persist
under the schedulers we actually run.
[AUDIT CORRECTION 2026-08-21 (third audit, block 69): the
tilting sentence above is UNJUSTIFIED as stated — a per-step
`O(1)` reweighting compounds to `e^{O(L)}` over the walk,
which swamps any polynomial-in-`e^n` margin.  A correct
version would need the change of measure confined to the
`2k` collision-window steps with conditional likelihood-ratio
control at stopping times; this has not been done.
Freshness-modified walks are NOT currently covered by 57.2.
WITHDRAWN as a claim; retained as a direction.]

**Status.**  57.1 and 57.2 proved in full; 57.3 is the
rigorous restatement of the remaining core.  The main
conjecture remains unproven.

## 5.40 Block 58: C13 — the balance rule cracks the dispersion half;
pool scaling carries both halves

**58.1 C13 (potential-greedy).**  Rule: among the `sigma+1`
eligible letters, pick the one whose would-be windows have the
LOWEST summed current fiber counts across the shallow ranks
(ties random) — a dense-gradient balance rule, one increment
per rank per step.  Result: multiplicity dispersion
`var/mean = 0.25-0.41` at EVERY rank, EVERY `n` in 9..13,
EVERY slack tested — the witnesses' sub-Poisson signature
(0.4), reproduced for the first time by a simple policy.  The
53.1 wall does NOT bind balance-greedy: its hypothesis (rare
fresh events, oblivious side ranks) fails because fiber counts
give an informative gradient at every step at every rank.
Coverage: best of all rules (n=13 slack 1.6: 455 missing vs
C8's 732), residual misses 6-10% at the tightest pool.

**58.2 C13b (pool scaling; model-validity boundary).**  At
fixed slack 1.2, raising the pool from 2 to 6 cuts misses
`~3x` (n=13: 900 -> 419 -> 293; n=11: 209 -> 98 -> 97) while
dispersion IMPROVES (0.27 -> 0.18 -> 0.17).  Validity requires
floor `>= m+2` (else windows repeat letters and the MTF
compilation breaks — the pool-8 rows at floor `< m+2`
collapse pathologically, confirming the boundary).  The MDCU
regime (pool `sqrt(n log n)`, floor `n - sqrt(n log n)`) is
deep inside validity; both observed trends point the right
way as the pool grows toward it.

**58.3 The sharpened proof target.**  Empirically the
Sub-Poisson Walk Question is answered by: dense-gradient
fiber balancing at adequate pool.  The theory program is now:
(i) a supermartingale/potential argument (Spencer species) on
`Phi = sum of squared fiber deviations` for a softmax version
of the balance rule — target: `Phi` stays `O(mean)` whp,
giving sub-Poisson rigorously; (ii) the coverage DE (50.2,
C10-validated) rides on top; (iii) P-sweep absorption (55.2)
cleans the `o(1)` leftovers.  All three pieces have known
genres; none is proved here yet.

**58.4 n=9 finisher final.**  `{180: 2, 189: 1, 198: 0}`:
the `eps(9) <= 0.571` witness stands; 180/189 reached 1-2
missing (suggestive of witnesses slightly deeper, not
claimed).

**Status.**  58.1-58.2 data (scripts preserved); 58.3 program;
58.4 data.  The main conjecture remains unproven.

## 5.41 Block 59: second-reader audit (2026-08-21) — accepted in
full; corrections executed

The audit's verdict: real, interesting progress, finite and
structural, NOT a solution of the main conjecture.  All
findings accepted:

  (1) SURVIVES, independently replayed by the auditor on H100:
      both witnesses (n=7 L=56, n=9 L=198) with their balance,
      gap histograms, Kendall statistics, and sub-Poisson
      dispersion 0.29-0.40; Lemma 46.1 (the innovation bound,
      "a clean, correct little theorem" with its Omega(W/n)
      deviation bound); the MTF/LRU reformulation as a useful
      conceptual reduction to sequential discrepancy.
  (2) CORRECTED off-by-one: eligible tail/pool is `sigma + 1`
      under the stated convention (fixed inline at 50.1 and
      54.1; 57.1 already had the correct count).
  (3) WITHDRAWN: "balance is automatic" in 54.1 — closure does
      not force balanced counts (fixed inline; near-balance is
      a condition or must be derived from covering).
  (4) Near-uniform fibers: now stated explicitly as a
      CONDITION in the compilation, not a consequence.
  (5) BUG acknowledged: de_test_c10.py initialized `last`
      inconsistently with its seeded word (fixed in the
      script; the seeding artifact inflated measured pools by
      ~0.03-0.08 and does not change C10's conclusions, which
      the auditor's replay left standing at the qualitative
      level — the DE match itself remains a five-seed
      experiment at n=11,13, NOT a proof).
  (6) DOWNGRADED to research hypotheses (index and master
      language corrected): LUL (entirely unproved); the
      absorption cleanup (a PROPOSED Hall/serialization lemma,
      not "sound"); the DE/scaling narrative; the "final
      decomposition" (fiber discrepancy must hold
      SIMULTANEOUSLY at every shallow rank — the multi-rank
      demand is reorganized, not gone).
  (7) The two-point slack data (eps(7) = 0.6, eps(9) <= 0.571)
      do NOT establish eps(n) -> 0.
  (8) No new bound on nu(k); no coefficient-one theorem; no
      k=17 advance.  Stated plainly.
  (9) CERTIFICATES FROZEN: witnesses/n7_L56.txt
      (SHA ae1edfe3beb27df79ff2f4f052c1b19684eec6080fd75f8a2b6
      cee1610f2c9c6), witnesses/n9_L198.txt
      (SHA c4caf0c89520fc43172dd1a58874dc7a61bdd06cff7ea36b94f
      5a4e9f96944b4), verifier witnesses/verify_witness.py
      (SHA a3433e2773f441dd3bbfe8e42cfbb84e80026ef744a8e48758a
      f5282a962e061); both PASS locally.
  (10) MASTER_HANDOFF: the stale pre-audit paragraph after the
      relabel block ("clears every obstruction", "exactly two
      irreducible cores") bracketed as superseded.

## 5.42 Block 60: the snub inequality and the exact d-choice
coverage theorem — the idealized half becomes rigorous; LUL
reduced to two quantitative mixing bounds

Setting: the (sigma+1)-tail MTF walk (54.1 corrected), rank k
in the shallow range, floor = n - sigma >= k.  By 57.1 the
eligible pool at every step has EXACTLY sigma+1 letters, and
every pool letter has age >= floor > k - 2, so the pool is
disjoint from the current top-(k-1).  Write P_t for the
top-(k-1) of the recency order before step t (the PREFIX), and

  F_t^k = { P_t u {x} : x in pool_t }        (the FAN)

so |F_t^k| = sigma+1 exactly, every fan member is a genuine
k-set, and the step's new k-window is the fan member selected
by the rule.  Z_t^k = k-sets unseen before step t.  A rule is
ZERO-PREFERRING at rank k if it selects a member of
F_t^k n Z_t^k whenever that intersection is nonempty
(single-rank freshness-greedy C8 is; multi-rank
potential-greedy C13 is NOT — a rank-k zero can lose the
summed score to a rank-k' term; noted below).

60.1 LEMMA (snub inequality — PROVED).  For any zero-preferring
rule at rank k, with c_t = |F_t^k n Z_t^k|, after any number of
steps:

  (a) every step with c_t >= 1 covers exactly one new k-set,
      so  miss^k = |Z^k_final| = M - #{t : c_t >= 1},
      M = C(n,k) (up to the n-k+1 seed windows);
  (b) miss^k <= N_0 + sum_t (c_t - 1)^+ , where N_0 = #{k-sets
      never appearing in any fan while uncovered}.

Proof of (b): a surviving zero S either never appeared in a
fan while uncovered (counted by N_0), or appeared and was
snubbed each time (some OTHER fan zero was selected).  A step
with c_t zeros covers one and snubs c_t - 1; map each type-(b)
survivor to its last snub event (t, S).  Distinct survivors map
to distinct events (same t forces distinct S).  The number of
snub events is sum_t (c_t - 1)^+.  QED.

Unconditional, every n, every length.  Reading: coverage can
fail ONLY through fan-starvation (N_0: sets the walk never
offers) or fan-crowding (zeros arriving in the same fan).
These are the two and only two failure channels.

60.2 THEOREM (idealized d-choice coverage — PROVED).  Consider
the IDEALIZED process: at each step the fan is d k-sets drawn
uniformly and independently from all M = C(n,k) k-sets, and the
rule is zero-preferring.  Let T(delta) = number of steps until
coverage 1 - delta.  T(delta) is a sum of independent
geometrics with success probabilities p_z = 1 - (1 - z/M)^d
(z = current number of zeros), and for delta*M >= 1:

  E[T(delta)] <= M * (1 + (ln(1/delta) + 1)/d).

Proof: E[T] = sum_{z=z0}^{M} 1/p_z with z0 = ceil(delta*M).
Write 1/p = 1 + q/(1-q), q = (1-z/M)^d.  The first parts sum to
<= M.  For the second: with u = 1 - z/M,
1 - u^d = (1-u)(1 + u + ... + u^{d-1}) >= (1-u) d u^{d-1},
hence q/(1-q) <= u/(d(1-u)) = (1 - z/M) * M/(d z) <= M/(d z),
and sum_{z >= z0} M/(dz) <= (M/d)(ln(M/z0) + 1/z0).  QED.

Concentration: every included z >= delta*M has
p_z >= 1 - e^{-delta*d}; for delta*d >= 2 all p_z >= 0.86, so
Var(T) <= sum (1-p_z)/p_z^2 <= 0.2 M and Chebyshev (or
Bernstein over independent geometrics) gives
T <= E[T] + O(sqrt(M) log M) whp.

COROLLARY (budget check, PROVED for the idealized process):
with d = sigma+1 and budget L = (1+eps)M, taking
delta = e^{-eps*d/2} gives E[T] <= M(1 + eps/2 + O(1/d)) < L,
so the idealized process reaches coverage
1 - exp(-eps(sigma+1)/2) whp inside the MDCU budget; at
sigma = C sqrt(n log n) that is 1 - exp(-Omega(eps sqrt(n log
n))).  This replaces the heuristic DE of 50.2 with exact
geometric sums for the idealized process — no ODE limit, no
Wormald machinery — and reproduces the DE's answer (slack eps
buys miss fraction e^{-c eps sigma}).

HONEST LIMITS of 60.2: (i) it is a statement about the
idealized independent-fan process, NOT about the walk — the
real fan is deterministic given history; (ii) it is per-rank —
the real walk must realize this at all Theta(x*) shallow ranks
with a SINGLE choice sequence (the multi-rank wall 53.1 lives
exactly here).

60.3 Fan anchoring: where the real fan differs from the
idealized one (structure PROVED, counts conditional).

  (a) STAR STRUCTURE (proved): the real fan is
      {P_t u {x} : x in pool_t} — sigma+1 sets pairwise
      intersecting in exactly the common prefix P_t.  In the
      Johnson graph the fan is a star, not a spread sample.
      This is the precise geometric sense in which LUL is a
      hypothesis: zero-membership is correlated across a star.
  (b) APPEARANCE ACCOUNTING (proved identity): S appears in
      F_t^k iff P_t is one of the k faces of S AND the missing
      letter S \ P_t is in pool_t.  So appearance
      opportunities of S = visits of the prefix process to
      dS (the k faces of S), converted to appearances at pool
      rate.
  (c) OPPORTUNITY COUNT (conditional on near-uniform
      (k-1)-fibers, which is a CONDITION of the compilation):
      each (k-1)-set hosts ~ L/C(n,k-1) prefix visits; at the
      focus rank k = m+1 (C(n,k-1) = W) each k-set S has
      ~ k(1+eps) ~ n/2 face visits; if pool membership of the
      specific completing letter behaved like a uniform
      (sigma+1)/(m+1) draw, S would expect
      ~ (n/2)(sigma+1)/(m+1) ~ sigma+1 fan appearances.
      Theta(sigma) appearances per set is EXACTLY what the
      snub inequality needs for miss ~ M e^{-Theta(sigma)}.
      The two "if"s in this sentence are the whole gap.

60.4 LUL* — the minimal quantitative form of the gap
(HYPOTHESIS, sharpened statement).  By 60.1, MDCU coverage
1 - o(1) at rank k follows for a zero-preferring rule from just
two bounds:

  (L1) fan access:    N_0 = o(C(n,k));
  (L2) fan crowding:  sum_t (c_t - 1)^+ = o(C(n,k)).

Nothing else is needed.  (L2) has a clean combinatorial
reading via 60.3(a): c_t >= 2 means TWO uncovered sets share
the visited prefix P_t and both completions sit in the pool —
crowding is a co-degree statement about the miss hypergraph
along the prefix trajectory, and each crowded step still
covers one zero (self-correcting).  Both (L1) and (L2) are
LUL-type mixing statements; neither is proved for any
deterministic or randomized eligible rule.  This is the
sharpest form of the analytic gap so far: the DE, the
absorption narrative, and the dispersion fingerprints are all
upstream heuristics for (L1)+(L2).

Multi-rank caveat (honest): C13's potential-greedy is not
zero-preferring per rank, so 60.1 does not apply to it as-is;
for a rule that covers-first at SOME rank, the per-rank
inequality acquires a third term (steps where rank k offered a
zero but the step covered at another rank) — cross-rank
contention, not yet bounded.  Defining and testing a
cover-first variant (C15) is a next step.

The main conjecture remains unproven.

## 5.43 Block 61: C14 — pool-shape scaling at fixed slack
(n = 11..19); the witness-shaped pool does NOT scale, the
max-valid pool does

Run (h100, potential_c14.py, 3 seeds, slack 1.2, ranks
m/m+1/m+2, audit-consistent seeding): multi-rank
potential-greedy with pool laws A: sigma =
min(round(0.7 sqrt(n ln n)), m-1); B: sigma = m-1 (the largest
pool with floor >= m+2, the compilation validity boundary,
58.4); C: sigma = 1 (the witness shape).  Full log
~/potential_c14.log on h100; per-rank miss FRACTION (rank m
column shown; other ranks in log):

  n:            11      13      15      17      19
  A (0.7sqrt): 0.097   0.105   0.107   0.096   0.099   sigma 4..5
  B (m-1):     0.097   0.100   0.087   0.079   0.073   sigma 4..8
  C (1):       0.219   0.238   0.227   0.227   0.229   sigma 1

  rank m+2:  A 0.021..0.030 flat;  B 0.021..0.019 flat-falling;
  C 0.086 -> 0.118 -> 0.136 -> 0.147 -> 0.159 RISING.
  Dispersion: sub-Poisson everywhere (0.16-0.35), improving
  with pool size — matches the witness fingerprint band.

Readings (all empirical, 3 seeds, greedy only — no annealing):

  61.1 The witness-shaped pool (sigma = 1) does NOT scale: its
       miss fraction is flat ~0.22-0.24 at ranks m/m+1 and
       RISES with n at rank m+2.  The finite witnesses at
       slack ~1.6 exist DESPITE the sigma = 1 pool (annealing
       + extra slack), not because greedy suffices there.
       Pool growth is doing real asymptotic work — first
       direct evidence that the sigma -> infinity regime is
       necessary for greedy-type schedules, not just
       convenient.
  61.2 The max-valid pool (sigma = m-1) falls monotonically:
       rank-m miss 0.097 -> 0.073 (ratio 0.75 over sigma
       4 -> 8), rank-m+1 0.074 -> 0.052 (0.71).  Direction
       agrees with the 60.2 idealized law miss ~ e^{-c eps
       sigma}, but the fall is SLOWER than idealized
       (e^{-0.2 * 4} = 0.45 predicted for the same sigma
       increment) — consistent with the star-anchored fan
       (60.3a) being less efficient than independent sampling
       and with C13 not being zero-preferring (60.4 caveat).
  61.3 The asymptotic-shaped pool (law A) is FLAT ~0.10 across
       n = 11..19 — but sigma only moves 4 -> 5 on this range
       (0.7 sqrt(n ln n) grows too slowly for finite n to
       resolve), and the idealized prediction for that
       increment (factor ~0.8) is within 3-seed noise.  The
       question "does miss fraction fall at the asymptotic
       shape" is NOT settled by this range; it neither
       confirms nor contradicts the DE picture.
  61.4 Validity cap binds: law B beats law A everywhere with
       floor >= m+2 intact — at finite n the best greedy pool
       is the LARGEST valid one, not the asymptotic shape.
       Consistent with 58.4 (pool growth helps until the
       compilation breaks).

Status: 61.1 is the load-bearing new datum (a negative scaling
result for the witness-shaped pool).  All hypothesis labels of
blocks 50-59 unchanged.  The main conjecture remains unproven.

## 5.44 Block 62: the random walk is a shelf shuffle — floor
exclusion, uniform stationarity, run bounds; the plateau
theorem reduced to one decorrelation problem

The zero-preference machinery of block 60 sits ON TOP of a
base chain: the PURE RANDOM (sigma+1)-tail MTF walk (pick
uniformly among the sigma+1 oldest).  This block develops the
base chain's exact structure.  Everything labeled PROVED here
is unconditional.

62.1 LEMMA (floor exclusion — PROVED, tight).  In any word
(finite or cyclic) with all letter-gaps >= g >= k+1, two equal
k-windows are >= g apart: S_t = S_{t+d} with d >= 1 forces
d >= g.

Proof.  Case d >= k (disjoint blocks): the letter w_t lies in
S_t = S_{t+d}, so it must occur in [t+d-k+1, t+d]; its first
occurrence after t is >= t+g > t+d unless d >= g.  Case
d <= k-1 (overlapping blocks): the d letters w_{t-k+1},...,
w_{t-k+d} lie outside the second block and must reoccur inside
its new positions [t+1, t+d]; for the LAST of them,
w_{t-k+d}, the next occurrence is >= t-k+d+g > t+d whenever
g > k.  Contradiction either way.  QED

Tightness: d = g forces the exact-refill pattern (every letter
of S recurring at gap exactly g, same order).  COROLLARIES:
(i) every k-window multiplicity is <= L/g; (ii) the window
stream is deterministically self-avoiding on every stretch of
g-1 = n-sigma-1 steps — no probabilistic input at all.  C16
confirms: first repeat observed at lag floor+1 exactly (n=13
sigma=3: 11; n=15 sigma=3: 13).  Same genre as 46.1; the two
lemmas now bracket window multiplicity from both sides of the
rigidity story.

62.2 LEMMA (uniform stationarity — PROVED).  The random
(sigma+1)-tail MTF chain on S_n (state = recency order; move a
uniform choice of the sigma+1 oldest to the front) is doubly
stochastic: every state has exactly sigma+1 in-neighbors, each
reached with probability 1/(sigma+1).  Hence the uniform
distribution on S_n is stationary.  The chain is irreducible
and aperiodic for 1 <= sigma <= n-2: the two extreme moves are
the position-cycles c_n (bring last to front) and c_{n-1}
(bring (n-1)st to front), of orders n and n-1 — coprime, so
aperiodic; c_n and c_{n-1} have opposite parities and generate
S_n (classical: a full cycle plus an (n-1)-cycle generate a
2-transitive group; with both parities present it is S_n).
CONSEQUENCE: at stationarity the rank-k window (= the set of
the last k letters, distinct by the floor) is UNIFORM on
C(n,k) for every k <= floor — the base chain has exactly the
right one-dimensional marginals for MDCU, at every rank
simultaneously.

62.3 LEMMA (uniform run bound — PROVED).  Condition on any
history.  For any fixed k-set S with k >= sigma+1, the
probability that the next k picks are exactly the elements of
S (in any order) is at most

  beta := (sigma+1)! / (sigma+1)^{sigma+1}  ( ~ e^{-sigma} ).

Proof: at the r-th step of the run, the unused letters of S
number k-r+1, and the uniform pick lands among them with
conditional probability <= min(k-r+1, sigma+1)/(sigma+1);
the product telescopes to beta for k >= sigma+1.  QED
Hence the repeat probability r_d = P(window_{t+d} = window_t)
satisfies r_d = 0 for d < floor (62.1) and r_d <= beta for all
d >= floor.  C16: observed max r_d ~ 0.022 <= beta = 0.0938
at n=13, sigma=3.

62.4 THE SHELF-SHUFFLE REPRESENTATION (proved as a
representation; heuristics labeled).  In the recency order,
a letter's position equals its age [AUDIT CORRECTION
2026-08-21: literally true only on the conveyor — positions
`1..floor` hold ages `0..floor-1` in order; POOL positions
`n-sigma..n` only ORDER the pool ages, which can exceed the
positions arbitrarily.  All uses below depend only on the
ordering and on conveyor descent, which are correct]; each
step, the letter at
position n-sigma-1 enters the pool deterministically (FIFO,
one per step) and one uniform pool member is served to the
front.  The pool is therefore a size-(sigma+1) buffer with
deterministic FIFO arrivals and uniform service — the walk is
a card-shuffling MACHINE of the same family as Diaconis-
Fulman-Holmes ("Analysis of casino shelf shuffling machines",
Ann. Appl. Probab. 23(4):1692-1720, 2013): repeated passes of
an n-card deck through a small buffer.  (Not identical: DFH
shelves take insertions above/below existing piles and end
with a random pile assembly, and they analyze ONE pass.  Ours
is FIFO-in / uniform-out, run forever.)  The MDCU question
needs the chain's AUTOCORRELATION, not its one-pass
non-uniformity or mixing time per se.  Displacement
heuristic: per pass (~n steps), a letter's position shifts by
its centered buffer wait, variance Theta(sigma^2), so phases
decorrelate diffusively after ~ (n/sigma)^2 passes:

  T_dec ~ n^3/sigma^2   (n=13, sigma=3: ~240 steps).

C16 matches: r_d echoes at lags ~ jn decay to a factor ~4
above 1/M by d = 200 at n=13 (predicted T_dec ~ 244), and
coverage lands within 1.2% of the Poisson plateau
1 - e^{-L/C(n,k)} at ALL three ranks and both n — the base
chain Poissonizes numerically on the nose.

62.5 PROBLEM R (aggregate decorrelation — THE clean open core
for the base chain).  Show, for sigma >= C log n (say):

  sum_{d=floor}^{L} ( r_d - 1/M )^+  =  o(1),   M = C(n,k),

e.g. via r_d <= 1/M + C exp(-c d sigma^2 / n^3).  Modulo R:
  (i)  Cauchy-Schwarz on window hits gives coverage >=
       (1-o(1)) L/(3+2eps) with NO further input;
  (ii) per-set second moments + Paley-Zygmund give coverage
       >= ((1+eps)/(2+eps))(1-o(1));
  (iii) factorial moments via 62.3-type run bounds should give
       the exact plateau 1 - e^{-(1+eps)} (Chen-Stein route).
Problem R is STRICTLY CLEANER than LUL: no Z-feedback, known
uniform stationary law, a pure shuffle-autocorrelation
estimate about tagged letters in a queue.  The plausible proof
route is a local CLT / coupling for the k tagged letters'
renewal phases (waits are one-per-step exchangeable — negative
association available), and it is the natural first theorem
target.  LUL = Problem R + the zero-preference feedback layer.

62.6 Strategic picture (updated, honest).  The base chain
plateaus at 1 - e^{-(1+eps)} < 1: randomness alone NEVER
reaches 1 - o(1); the d-choice boost of 60.2 is what converts
slack into coverage 1 - e^{-Theta(eps sigma)}.  The program is
now two layers, each with a precise open statement:
  LAYER 1 (Problem R): decorrelation of the shelf-shuffle base
    chain -> plateau theorem for the random rule (first proved
    coverage constant for ANY rule in this program);
  LAYER 2 ((L1)+(L2) of 60.4): fan access + fan crowding for a
    zero-preferring rule -> full MDCU coverage.
Status: 62.1-62.3 proved (three unconditional lemmas); 62.4 is
an exact representation plus labeled heuristics; R and
(L1)/(L2) are open.  Tiny-scale numerics: C16
(scripts/plateau_c16.py, local, seconds — coverage vs plateau,
r_d structure, floor exclusion check).  No claim about nu(k)
is made.  The main conjecture remains unproven.

## 5.45 Block 63: the base chain is a group walk — Problem R
reduces to polynomial mixing; sigma = 1 is the inverse
Rudvalis shuffle (known Theta(n^3 log n))

63.1 LEMMA (group-walk identification — PROVED).  Write c_j
for the position-cycle "bring position j to the front"
(recency order, youngest = position 1).  One step of the
random (sigma+1)-tail MTF chain applies c_J with J uniform on
{n-sigma, ..., n}, INDEPENDENT of the letter labels.  Hence
the chain is a random walk on S_n driven by the iid step
measure mu = uniform on {c_{n-sigma}, ..., c_n}.  Two
corollaries, both proved:
  (a) UNIFORM FLOORED-WORD ENSEMBLE: since every state has
      exactly sigma+1 continuations (57.1), the generation
      tree is (sigma+1)-regular, so the law of the emitted
      word of length T is UNIFORM over all gap-floored
      continuations of the initial state, each having
      probability (sigma+1)^{-T}.  The base chain is the
      canonical random floored word; Problem R is a
      correlation estimate for the uniform floored-word
      ensemble (a 1D hard-constraint system, range = floor).
  (b) SIGMA = 1 IS THE INVERSE RUDVALIS SHUFFLE: mu = uniform
      on {c_{n-1}, c_n} = "bring the last or second-to-last
      card to the top, probability 1/2 each" — the inverse
      walk of the Rudvalis shuffle ("top card to the bottom or
      second-from-bottom"), whose mixing time is
      Theta(n^3 log n) (upper bound classical; matching lower
      bound D. B. Wilson, "Mixing time of the Rudvalis
      shuffle", Electron. Comm. Probab. 8 (2003) 77-85).  A
      walk and its inverse have identical distances to
      uniformity, so the sigma = 1 base chain mixes in
      Theta(n^3 log n) — a THEOREM, and it matches the 62.4
      diffusion heuristic n^3/sigma^2 at sigma = 1 up to the
      log factor.

63.2 LEMMA (window autocorrelation from TV mixing — PROVED).
For any d and any starting law, conditioning on pi_t:
P(win_{t+d} = win_t | pi_t) <= 1/M + d_TV(P^d(pi_t, .), Unif),
because {pi' : g(pi') = S} has uniform measure exactly 1/M for
every k-set S.  Hence, with dbar(d) = worst-case TV distance,

  1/M - dbar(d)  <=  r_d  <=  1/M + dbar(d),

two-sided, no reversibility or spectral input needed.  (The
one-step spectral route FAILS: functions of the young
positions are transported isometrically for up to floor steps
— s_2(P) = 1; the deterministic conveyor is a genuine
obstruction, which the d >= T split below absorbs.)

63.3 THEOREM (Problem R from polynomial mixing — PROVED
reduction).  Suppose the back-(sigma+1) walk satisfies a
polynomial TV mixing bound T_mix(1/4) <= n^A, and
sigma >= C_A log n.  Then

  sum_{d=1}^{L} ( r_d - 1/M )^+  =  o(1).

Proof.  Split at T = (A+4) T_mix log_2 n-ish: for d < T use
the run bound 62.3 (r_d = 0 below floor, <= beta ~ e^{-sigma}
above), giving T beta <= n^{A+O(1)} e^{-sigma+O(log sigma)}
-> 0 once sigma >= C_A log n.  For d >= T use 63.2 plus
submultiplicativity of dbar: sum_{d>=T} dbar(d) <=
2 T_mix dbar(T)-geometric <= n^{A} n^{-(A+3)} -> 0.  QED

COROLLARY (PROVED modulo the mixing bound R'): per-set second
moments close.  E[hits_S] = L/M exactly (uniform marginal,
62.2); E[hits_S^2] <= mu + 2 mu (mu + o(1)) with mu = 1+eps by
the same split applied to P(hit at t and t+d) (62.1 kills
d < floor; 62.3 handles floor <= d < T conditionally on ANY
history; 63.2 handles d >= T).  Paley-Zygmund then gives

  coverage >= ((1+eps)/(3+2eps)) (1 - o(1))

in expectation at every rank k <= floor SIMULTANEOUSLY (the
marginal-uniformity and the bounds are rank-independent) —
the first proved-modulo-R' positive coverage constant for any
eligible rule at the MDCU budget.  The exact plateau
1 - e^{-(1+eps)} needs all factorial moments: same two
ingredients applied to r-tuples of times (split every
consecutive difference), routine but bookkeeping-heavy —
deferred, labeled.

63.4 PROBLEM R' (the single remaining gap of Layer 1 —
OPEN).  [RESOLVED BY LITERATURE — third audit, 2026-08-21,
block 69: the walk is the bottom-b-to-top shuffle with
b = sigma+1, and its mixing was already known.  Sharad Goel,
"Analysis of top to bottom-k shuffles", Ann. Appl. Probab.
16(1):30-55 (2006), gives polynomial TV mixing across the
full k-range for the inverse walk (identical TV distance);
Johan Jonasson, "Biased random-to-top shuffling", Ann. Appl.
Probab. (2006), Case 1 (uniform selection from the bottom k,
moved to top — literally this walk) gives
T_mix = Theta((n^3/b^2) log n) within a factor 4 for
b = o(n), covering b ~ sqrt(n log n) exactly.  C17's
measurement is numerical confirmation of Jonasson's theorem,
not new evidence.  Everything below in 63.4 is superseded as
an R'-route and retained only as a record of exploration.]
Prove T_mix = n^{O(1)} (any polynomial) for the
back-(sigma+1)-to-top walk, sigma in [C log n, m-1].  Status
and routes:
  - sigma = 1: THEOREM (Rudvalis, 63.1b).  What is needed is
    an upper bound for general sigma; expected truth
    Theta((n^3/sigma^2) log n) by the diffusion heuristic and
    Wilson's lower-bound technique.
  - Coupling route (sketch, hypothesis): couple two decks by
    matching LETTER choices whenever the served letter of X
    lies in Y's pool (both pools have size sigma+1; maximal
    couplings match with probability |overlap|/(sigma+1)).
    Matched letters ride the conveyor together and stay
    matched forever (deterministic descent, simultaneous pool
    entry, coupled service).  [CORRECTION, block 64: "forever"
    is wrong — a serve at straddling positions J_X != J_Y
    unmatches every letter whose two positions lie strictly
    inside the open straddle; the damage is confined to the
    pool zone and is more than paid for by the served letter's
    gain (Lemma 64.2).  Conveyor matches are safe; pool-zone
    matches are not.]  Unmatched letters repair when
    the same letter occupies both pools simultaneously;
    per-pass repair probability ~ sigma/(n-ish drift), giving
    the n^3/sigma^2-type estimate.  UNPROVED; the drift
    analysis of relative letter positions is the work.
  - P*P contains the adjacent transpositions (i, i+1),
    i in [n-sigma, n-1] (computed: c_i^{-1} c_{i+1} swaps
    positions i, i+1), plus segment shifts — comparison
    technology applies only after handling the conveyor
    reducibility, e.g. on the n-step chain.

63.5 Updated program map (honest).  Layer 1 (random-rule
plateau) is now: R' (polynomial mixing for one explicit
family of shuffles) => Problem R => plateau ladder — with
sigma = 1 already a theorem in the literature and all other
links PROVED (62.1-62.3, 63.1-63.3).  Layer 2 (MDCU coverage)
remains: zero-preference d-choice boost via the snub
inequality (60.1) with (L1)/(L2) open on top of the same
mixing input.  No claim about nu(k) is made.  The main
conjecture remains unproven.

## 5.46 Block 64: the displacement Lyapunov — per-step
contraction lemmas for the letter-matching coupling (proved),
coalescence at the conjectured rate (measured)

Setup: two decks X, Y; positions 1..n (1 = top/front); one
step serves position J_X in X and J_Y in Y (both in the pool
zone [n-sigma, n]) and moves the served card to position 1;
positions p < J shift to p+1, positions p > J are unchanged.
The LETTER-MATCHING COUPLING: maximal coupling of the two
uniform pool choices — with probability |O|/(sigma+1), where
O = pool_X cap pool_Y as letter sets, both decks serve the
SAME letter (uniform in O); otherwise independent uniforms on
pool_X \ O and pool_Y \ O.  Marginals are exact.  Let
d(a) = |pos_X(a) - pos_Y(a)| and Phi = sum_a d(a); Phi = 0
iff coalesced.

64.1 LEMMA (shift bookkeeping — PROVED).  In one step, a
non-served letter b with positions (p, q) has d(b) unchanged
unless exactly one of p < J_X, q < J_Y holds; in that case
d(b) changes by +-1, and it INCREASES if and only if both p
and q lie strictly inside the open straddle interval
(min(J_X,J_Y), max(J_X,J_Y)).  (Case check: if q shifts and p
does not, then q < J_Y and p > J_X, and d increases iff
q >= p, i.e. J_X < p <= q < J_Y; symmetric on the other
side.)  Consequently the number of +1 contributions per step
is at most |J_X - J_Y| - 1, and all of them sit in the pool
zone.

64.2 LEMMA (per-step drift bounds — PROVED, verified).  Under
the coupling:
  (i)   MATCHED SERVE (same letter, J_X = J_Y): straddle
        empty, no increases; Delta Phi <= 0, with strict
        decrease for every unmatched letter whose two
        positions straddle the common J.  (C18: mean strictly
        negative in practice, decrements -2..-12 at n=60.)
  (ii)  LOOSE SERVE (same letter a, J_X != J_Y): the served
        letter's term drops from |J_X - J_Y| to 0; increases
        <= |J_X - J_Y| - 1 by 64.1; hence Delta Phi <= -1.
  (iii) DIFFERENT-LETTER SERVE (x in X, y in Y, x != y):
        Delta Phi <= (2 pos_Y(x) - J_X) + (2 pos_X(y) - J_Y)
        + (sigma - 1) — the served letters teleport to the
        top, everything else obeys 64.1.
C18 (scripts/lyapunov_c18.py, local, seconds): 20000 coupled
steps at n=60, sigma=9: zero violations of (ii) over 2251
loose serves and of (iii) over 3785 different-letter serves;
all 4559 flagged matched-serve steps were strict DECREASES
(the lemma's slack direction).  Diff-serve injection measured
mean +0.53, range [-98, +88] = O(n) fluctuations, near-zero
mean as the position-averaging argument predicts.

64.3 C17 (scripts/coupling_c17.py, local, seconds):
coalescence times of the coupling from a uniformly random
relative permutation:
  sigma = ceil(0.7 sqrt(n ln n)), n = 30/50/80/120:
    mean T_couple / ((n^3/sigma^2) log n) = 0.128 / 0.110 /
    0.114 / 0.090 — constant within noise;
  sigma = 1 (inverse Rudvalis), n = 20/30/40:
    mean T_couple / (n^3 log n) = 0.053 / 0.039 / 0.038 —
    consistent with Wilson's Theta(n^3 log n).
The coupling COALESCES at the conjectured rate
Theta((n^3/sigma^2) log n); by the coupling inequality, any
proof of this rate (even any polynomial bound) closes Problem
R' and with it Layer 1 (63.3).

64.4 What remains for R' (honest).  Phi has bounded-variation
steps except for the two O(n) teleport terms in (iii); the
drift closes if two state-averaged quantities are controlled
for the COUPLED process:
  (D1) overlap: E[|O|]/(sigma+1) bounded below (equivalently
       P(different-letter serve) small enough that its
       injection cannot beat the matched/loose gains);
  (D2) teleport centering: E[2 pos_Y(x) - J_X] <= o(needed) —
       the served-but-unmatched letter's position in the
       OTHER deck must average near the conveyor middle or
       lower; C18 measures the combined injection at +0.53
       per diff-serve at n=60.
Both are statements about the coupled two-deck stationary
dynamics, not about the single chain; neither is proved.
Optional-stopping bookkeeping (Phi >= 0, negative drift,
O(n)-bounded jumps) is standard once (D1)+(D2) hold.  Note
sigma = 1 has NO loose/matched distinction with |O| <= 2 and
the known Theta(n^3 log n) answer shows the drift there is
carried by a diffusive, not a per-step-negative, mechanism —
so (D1)/(D2) should be aimed at sigma >= C log n only,
matching where 63.3 needs them.

Status: 64.1-64.2 proved (complete case analysis; numerically
verified); 64.3 measured; 64.4 open.  The main conjecture
remains unproven.

## 5.47 Block 65: C15 cover-first data — fan starvation is
empirically ZERO; the J-weighted snub inequality (proved)

C15 (h100, potential_c15.py, slack 1.2, 2 seeds): cover-first
multi-rank rule (prefer eligible letters creating a new window
at SOME rank, tie-break by potential; zero-preferring at the
union-of-ranks level) with full per-rank accounting of the
snub terms.  Data (rank-k rows: miss | N0 | crowd | cross):

  n=13 sig=4: k=6: 156/1716 | 2 | 3019 | 192
              k=7: 113/1716 | 0 | 3239 | 152
              k=8:  21/1287 | 0 | 2578 | 178
  n=13 sig=5: k=6: 142 | 0 | 3941 | 234   k=7: 90 | 0 | 4220
              | 168   k=8: 21 | 0 | 2557 | 197
  n=15 sig=4: k=7: 654/6435 | 13 | 11541 | 784
              k=8: 478/6435 |  4 | 12136 | 596
              k=9: 116/5005 |  0 |  9708 | 752
  n=15 sig=6: k=7: 486 | 0 | 17975 | 880   k=8: 346 | 0 |
              19093 | 755   k=9: 85 | 0 | 12510 | 849

  65.1 FAN STARVATION IS EMPIRICALLY ABSENT: N0 = 0 in 10 of
       12 rows (max 13 of 6435).  Practically every k-set
       appears in the fan while uncovered — the Theta(sigma)
       appearance heuristic of 60.3(c) is validated; (L1) is
       the EASY half of LUL*.
  65.2 CROWDING DOMINATES THE BOUND AND IS ~20x LOOSE: crowd
       ~ 3000-19000 vs misses 21-654.  Larger sigma INCREASES
       crowd while DECREASING misses — snubbed zeros usually
       get covered later, so counting one snub as one
       potential miss is far too pessimistic.
  65.3 CROSS-RANK CONTENTION IS SMALL (~5% of crowd): the
       multi-rank conflict is NOT the binding channel for
       cover-first rules — consistent with C13/C14 escaping
       the 53.1 wall.
  65.4 Cover-first beats plain potential-greedy by ~10%
       relative at equal (n, sigma) (n=15 sig=6 rank-7:
       0.0754 vs C14's 0.0865).

65.5 LEMMA (J-weighted snub inequality — PROVED; sharpens
60.1).  For a zero-preferring rule, every surviving zero S
with a(S) fan-appearances-while-uncovered consumed a(S)
distinct snub events, so for every J >= 1 and every time
split t0:

  miss  <=  #{S : a_{>t0}(S) < J}  +  (1/J) sum_{t > t0}
            (c_t - 1)^+  +  #{S covered... none — S surviving}
  (apply with a_{>t0} = appearances after t0; snubs before t0
  are discarded, surviving zeros' late appearances all count).

Proof: partition survivors by a_{>t0}(S) < J or >= J; the
latter class injects into late snub events, J per survivor.
QED.  Reading with the DE/idealized picture: late crowding is
QUADRATIC in the zero density ((c_t - 1)^+ has mean ~
((sigma+1) z_t)^2 / 2 if fans sample zeros representatively),
while late appearances stay Theta(sigma (L - t0)/n) per set —
so the inequality has room to reach miss fractions ~
e^{-c eps sigma} where the J=1 version (60.1) provably cannot
(crowd ~ M swamps it, 65.2).  The quantitative inputs needed
remain the two mixing statements (fan representativeness for
appearances and for pair-crowding) — Layer 2 still reduces to
the same analytic core, but the ACCOUNTING is now sharp
enough to carry exponential targets.

Status: 65.1-65.4 empirical (2 seeds); 65.5 proved.  The main
conjecture remains unproven.

## 5.48 Block 66: Poissonization of window hits — the exact
plateau theorem, modulo R' alone

This closes the "factorial moments: routine, deferred" item
of 63.3 — the bookkeeping does go through, and the T-split
must be taken LONGER than in 63.3 (T = Theta(n T_mix), not
T_mix log n) because the Poisson limit needs TV error o(1/M)
= o(e^{-Theta(n)}), which submultiplicativity supplies for
free.

66.1 THEOREM (modulo R': polynomial T_mix for the
back-(sigma+1) walk; sigma >= C log n).  [THIRD AUDIT
2026-08-21, block 69: the mixing input is now a PUBLISHED
THEOREM (Goel 2006; Jonasson 2006 — see 63.4 bracket), so the
FIXED-SET conclusions below are UNCONDITIONAL, subject to a
final line-by-line write-out.  However the PAIR/concentration
sentence at the end of this theorem is WITHDRAWN: floor
exclusion (62.1) kills close repeats of the SAME set only —
two DIFFERENT overlapping sets can be hit at lags d < k with
probabilities far above 1/M^2, and no proved bound covers
those terms.  Var(#misses) = o(M^2), the in-probability
statement, and any "simultaneous over ranks" reading beyond
per-rank expectations DO NOT FOLLOW from what is proved.
What stands: per-rank, per-set Poisson(1+eps) hit limits and
E[miss fraction] = e^{-(1+eps)} + o(1).]  Fix eps > 0, a
shallow rank k <= floor, L = (1+eps) M with M = C(n,k), and
run the pure random rule from stationarity.  For every fixed
r >= 1, the r-th factorial moment of hits_S (the number of
times a fixed k-set S is the window) satisfies

  E[ hits_S^{(r)} ]  =  (1+eps)^r (1 + o(1)),

uniformly over S.  Consequently hits_S -> Poisson(1+eps) in
distribution, P(hits_S = 0) -> e^{-(1+eps)}, and

  E[ miss fraction ]  =  e^{-(1+eps)} + o(1);

with the same machinery applied to PAIRS (S, S'), hit counts
decorrelate, Var(#misses) = o(M^2), and the miss fraction
concentrates: miss fraction -> e^{-(1+eps)} in probability.
[WITHDRAWN — see the bracket above: the pair machinery was
never written and the d < k cross-set terms are not covered
by 62.1/62.3.  Concentration is OPEN.]

Proof skeleton (all ingredients already proved).  Set
T = C' n T_mix.  Order times t_1 < ... < t_r and write
P(all hit) as a product of conditional factors.  A factor
whose gap from the previous time is < floor is ZERO (62.1,
deterministic).  A factor with gap in [floor, T) is <= beta
~ e^{-sigma} (62.3, valid conditionally on the entire past).
A factor with gap >= T is in [1/M - dbar(T), 1/M + dbar(T)]
(63.2, conditional via the Markov property).  Summing over
gap patterns with s short gaps: C(r-1, s) T^s beta^s
(L (1/M + dbar))^{r-1-s} L <= mu^r (1 + M dbar(T) +
T beta M / L)^{r-1} with mu = L/M = 1+eps.  Now
M dbar(T) <= e^{Theta(n)} 2^{-C' n} -> 0 (submultiplicativity
of dbar run n-fold past T_mix) and T beta M/L <= poly(n)
e^{-sigma} -> 0 (sigma >= C log n).  The lower bound restricts
to all-gaps->= T tuples and uses the left half of 63.2.
Method of moments gives the Poisson limit; the pair version
E[hits_S^{(r)} hits_{S'}^{(q)}] -> mu^{r+q} is the same
T-split with both sets' run bounds.  QED (modulo R')

66.2 Remarks (honest).
  (a) The ONLY unproved input is R' (polynomial mixing).
      Everything else — floor exclusion, run bound, TV
      transfer, submultiplicativity — is unconditional and
      elementary.
  (b) The theorem is per-rank; it holds at every shallow rank
      simultaneously (union over O(sqrt n) ranks costs
      nothing against o(1) errors chosen polynomially small).
  (c) C16 sits within o(1) of the limit already at n = 13:
      measured 0.689/0.691/0.690 vs e^{-tau} plateau
      0.700/0.700/0.699 at ranks m/m+1 (tau = L/M per rank).
  (d) Interpretation for Layer 2: modulo R', the base chain's
      zero set at time tau M has density e^{-tau} + o(1) with
      Poisson-independent per-set hit structure — exactly the
      "well-spread misses" input that the J-weighted snub
      accounting (65.5) wants for the zero-preferring upgrade.
      The two layers now meet at a single unproved statement:
      R'.
  (e) NOT claimed: anything about nu(k), coefficient one, or
      the full MDCU (which needs Layer 2's boost from
      plateau to 1 - o(1)).

The main conjecture remains unproven.

## 5.49 Block 67: R' broken into per-letter pieces — exact
Geometric waits, independence for far letters, favorable
corrections; what remains is the endgame

Per-letter offset: delta(a) = pos_X(a) - pos_Y(a) (signed).
A letter is FAR if |delta| > sigma (its two copies are never
in the two pools simultaneously), NEAR if 1 <= |delta| <=
sigma, MATCHED if delta = 0.

67.1 LEMMA (exact Geometric waits under ANY coupling —
PROVED).  Whatever the coupling, each deck's marginal law is
untouched, and within one deck the tagged letter, while in
the pool, is served with probability exactly 1/(sigma+1) per
step regardless of history (the pool always has exactly
sigma+1 members and the choice is uniform).  Hence every
letter's zone wait is exactly Geom(1/(sigma+1)) in each deck,
iid across passes, mean sigma, variance sigma(sigma+1).

67.2 LEMMA (independence for far letters under the
independent-residual coupling — PROVED).  [WITHDRAWN — third
audit 2026-08-21, block 69: independence is NOT established.
Which steps are same-letter vs residual is STATE-DEPENDENT,
and the tagged letter's two service times are functions of
the entire coupled trajectory; "the residual coins are
independent" does not deliver independence of the two waits.
The marginal Geometric law of each wait (67.1) stands; the
joint law is uncontrolled.  Retained as a target statement.]
Use the coupling of
C17 (maximal same-letter mass, residual choices independent).
A far letter is never in O = pool_X cap pool_Y, so both of
its services occur through the independent residuals; its
X-wait and Y-wait in any given pass are INDEPENDENT
Geom(1/(sigma+1)) draws.  Its per-pass offset increment from
its own services is w_Y - w_X: mean 0, variance
2 sigma(sigma+1) >= 2 sigma^2.

67.3 LEMMA (favorable corrections for far letters — PROVED,
corollary of 64.1).  [PARTIALLY WITHDRAWN — third audit
2026-08-21, block 69: the CORRECTION-SIGN claim (cross-serve
corrections to a far letter's |delta| are decreases only) is
a correct corollary of 64.1 and STANDS.  The "supermartingale"
framing is WRONG: |delta + mean-zero noise| is a
SUBmartingale by convexity — diffusion pushes |delta| up on
average, and the honest mechanism is interval HITTING (an
unbiased-ish walk hits [-sigma, sigma] in ~ (delta/sigma)^2
variance-steps), which additionally needs the joint law of
the waits (withdrawn in 67.2).  The quantitative conclusion
is UNPROVED.  Moot for R' itself, which is closed by
literature (63.4 bracket); retained for the coupling's
independent interest only.]  Between its own services, a far
letter's offset changes only at exactly-one-shift steps, and
since an INCREASE of |d| requires both copies strictly inside
the open straddle (subset of the zone, width <= sigma), a far
letter's |delta| can only DECREASE through cross-serve
corrections.

67.4 The remaining gaps for R' (honest, sharper than 64.4):
  (i)  NEAR-letter matching rate: a near letter (|delta| <=
       sigma) has its copies simultaneously in both pools for
       sigma + 1 - |delta| steps per pass; the maximal
       coupling then serves it same-letter (matching it,
       delta -> 0) with probability ~ (sigma+1-|delta|)/
       (sigma+1) x Theta(1) per pass.  Needs: a lower bound
       on P(a in O while both in zone) under the coupling —
       plausible, not yet written.
  (ii) MATCHED-letter breakage and SIMULTANEITY: matched
       letters break only via straddles (J_X != J_Y across
       their common position), at rate tied to the number of
       still-unmatched letters being served; as the unmatched
       count u drops, breakage drops ~ u/(sigma+1) per step
       — a birth-death endgame on u that should close
       geometrically.  Needs the joint bookkeeping (a
       letter-count Lyapunov on top of 67.3's per-letter
       one).
  (iii) Formal assembly: diffusion (67.3) + collection (i) +
       endgame (ii) => E[coalescence] = poly(n), hence
       T_mix = poly(n) by the coupling inequality, hence R'
       (63.3), hence the plateau theorem (66.1)
       unconditionally.
C17's measured coalescence at Theta((n^3/sigma^2) log n) is
consistent with (i)-(iii) closing at the conjectured rate.

Status: 67.1-67.3 proved; 67.4 open (three named steps, each
standard-genre).  R' is no longer a monolith.  The main
conjecture remains unproven.

## 5.50 Block 68: the co-pool mechanism — 67.4(i) and (ii)
resolved at proof level; R' reduced to far-phase
formalization

Conventions as in block 67; the coupling is C17's (maximal
same-letter mass on O = pool_X cap pool_Y, independent
residuals on the complements).

68.1 LEMMA (co-pool persistence and certain match — PROVED).
Suppose letter a has both copies in the pools ("co-pool").
Under the coupling, a's X-service can occur only through the
same-letter branch selecting a (the residual branch draws
from pool_X \ O, which excludes a), and identically for Y.
Pool membership ends only by service.  Hence the co-pool
state persists until the same-letter branch selects a, at
which point BOTH decks serve a and it becomes MATCHED at the
front.  A co-pool letter is matched at its next service with
certainty; per step this happens with probability exactly
1/(sigma+1).

68.2 LEMMA (pass lottery — PROVED).  Let a be near
(0 < |delta| <= sigma) with both copies on the conveyor.  The
later copy trails by exactly |delta| steps (conveyor descent
is deterministic).  When the earlier copy enters the zone,
the later copy arrives exactly |delta| steps afterward,
during which the earlier copy — a pool member — is served
with probability exactly 1/(sigma+1) per step (67.1) and the
later copy cannot be served at all.  Therefore

  P(a reaches co-pool this pass) >= (sigma/(sigma+1))^{|delta|}
    >= (sigma/(sigma+1))^{sigma} >= 1/4  for all sigma >= 1,

and by 68.1 co-pool implies matched.  If the lottery fails
(earlier copy served alone), the new offset after both
copies' services equals the difference of the two service
times = |delta| + O(Geom waits): mean O(sigma) — the letter
stays near-or-mildly-far, and retries next pass.

68.3 LEMMA (zero-collateral repairs; terminating cascades —
PROVED).  A matched letter is broken only by a straddle
strictly containing its common position (64.1), which sets
its offset to 1 and leaves it co-pool if in the zone (zone
positions are only left by service).  By 68.1 it is re-matched
at its next service, and that repair serve has |J_X - J_Y| =
1, whose OPEN straddle is empty: the repair breaks nothing.
Breakage cascades terminate at offset 1.  Matched letters on
the conveyor cannot be broken at all (straddles live in the
zone).

68.4 LEMMA (no backflow — PROVED).  Residual (different-
letter) serves draw only from pool \ O — letters whose two
copies are ALREADY split (one in this deck's pool, the other
elsewhere) — so diff-serve teleports act within the far/split
class and never eject a matched or co-pool letter.  The class
dynamics is one-directional:

  far --(67.3 diffusion)--> near --(68.2, prob >= 1/4 per
  pass)--> matched (absorbing modulo 68.3's benign
  offset-1 flutter).

68.5 ASSEMBLY (OUTLINE — the one remaining gap of R').
[SUPERSEDED — third audit 2026-08-21, block 69: R' is closed
by Goel (2006) / Jonasson (2006) (see 63.4 bracket), so this
assembly is unnecessary for the program; moreover its far
phase leaned on 67.2/67.3, which are withdrawn.  Lemmas
68.1-68.4 are self-contained (they use only 67.1 and 64.1)
and stand as correct statements about this particular
coupling, of independent interest only.]
Far phase: every far letter's offset is a supermartingale
with per-pass variance >= 2 sigma^2 and favorable corrections
(67.2-67.3) => all letters near within O((n/sigma)^2 log n)
passes whp.  Collection: 68.2 + geometric trials => all
matched within O(log n) further passes whp.  Endgame: 68.3-
68.4 => matched count is monotone up to certain re-matches;
coalescence when the last split letter resolves.  Expected
total: O((n^3/sigma^2) log n) — exactly C17's measured law
(constant ~0.1).  What formalization requires: (a) per-letter
pass filtrations (passes interleave across letters); (b) the
far-phase optional-stopping constants; (c) union bounds
assembling the three phases.  Assessment: no unknown
mathematical mechanism remains visible in R'; what remains is
disciplined writing.  This assessment is NOT a claim that R'
is proved: 68.5 stays OPEN until the bookkeeping exists on
paper.

Status: 68.1-68.4 proved (short, complete arguments); 68.5
open (formalization).  Layer 1 = 66.1 modulo 68.5 alone.  The
main conjecture remains unproven.

## 5.51 Block 69: third-reader audit (2026-08-21) — accepted
in full; R' was already published; corrections executed

The audit's verdict: the one meaningful development of blocks
62-68 comes from recognizing EXISTING LITERATURE, not from
the new coupling program.  All findings accepted:

  (1) R' CLOSED BY LITERATURE: the random tail-MTF chain is
      the bottom-b-to-top shuffle, b = sigma+1.  Goel 2006
      (Ann. Appl. Probab. 16(1):30-55, "Analysis of top to
      bottom-k shuffles") gives polynomial TV mixing across
      the full range via the inverse walk; Jonasson 2006
      ("Biased random-to-top shuffling", Ann. Appl. Probab.),
      Case 1, gives the sharp T_mix = Theta((n^3/b^2) log n)
      for b = o(n) — exactly the b ~ sqrt(n log n) regime.
      Both citations verified online this session.  63.4
      bracketed accordingly; blocks 64/67/68's coupling
      program is UNNECESSARY for R' (retained only for the
      correct standalone lemmas 64.1-64.2, 68.1-68.4).
  (2) SURVIVES (audit-endorsed): exact pool sigma+1 (57.1),
      uniform stationarity (62.2), floor exclusion (62.1),
      fixed-set run bound (62.3), snub inequalities (60.1,
      65.5) as valid bookkeeping lemmas.
  (3) PROMOTED: with the published mixing theorem, block 66's
      FIXED-SET part should become unconditional — visits to
      a fixed central k-set converge to Poisson(1+eps),
      E[miss fraction] = e^{-(1+eps)} + o(1) for the pure
      random walk (subject to a final line-by-line
      write-out).
  (4) WITHDRAWN — 66's concentration: pair decorrelation,
      Var(#misses) = o(M^2), the in-probability statement,
      and the "all ranks simultaneously" reading.  Floor
      exclusion kills close repeats of the SAME set only;
      close overlapping windows of DIFFERENT sets are not
      covered by any proved bound.  Concentration is OPEN.
  (5) WITHDRAWN — 67.2 (wait independence): state-dependent
      branching breaks the independence argument; only the
      marginal Geometric law (67.1) stands.
  (6) WITHDRAWN — 67.3's supermartingale framing: |delta +
      mean-zero noise| is a SUBmartingale (convexity); the
      correction-sign corollary of 64.1 stands; the
      quantitative far-phase conclusion was unproved.  Moot
      for R'.
  (7) CORRECTED — 57.2's range: the displayed calculation
      assumes central k = Theta(n); the k >= Theta(n/log n)
      threshold and the freshness/tilting inheritance claim
      were overreach; tilting WITHDRAWN (per-step O(1)
      reweighting compounds to e^{O(L)}).
  (8) CORRECTED — "recency position equals age" is literally
      true only on the conveyor; pool positions only order
      the ages (62.4 bracketed).
  (9) TOOLING — C18's checker tested the matched case against
      d != 0; its 4559 printed "violations" were favorable
      strict decreases consistent with the corrected lemma
      Delta Phi <= 0.  Script fixed (violation iff d > 0).
      Auditor reran C16-C18 on H100: C16/C17 reproduced (C17
      = numerical confirmation of Jonasson's theorem).
  (10) COMPUTE POLICY: C16-C18 were run locally; the auditor
      notes this against the Mac restriction and reran them
      on H100.  Recorded; henceforth anything beyond ~one
      second goes to h100.
  (11) THE REAL OPEN LAYER (audit's bottom line, adopted as
      the program statement): the adaptive, multi-rank
      upgrade from the constant Poisson plateau to 1 - o(1)
      coverage — fan access and late crowding under ONE
      shared zero-preferring schedule — plus, within Layer 1,
      the concentration gap of (4).  No new nu(k) bound, no
      coefficient-one theorem, no k=17 progress.

The main conjecture remains unproven.

## 5.52 Block 70: the fixed-set plateau theorem — full
write-out (unconditional, on published mixing input)

This is the line-by-line write-out promised at block 69(3).
Everything cited is either proved in this file (62.1, 62.3,
63.2) or published (Goel 2006; Jonasson 2006).

70.1 THEOREM.  Let n = 2m+1, let sigma = sigma(n) satisfy
C0 log n <= sigma = o(n) with C0 = 12 (the o(n) restriction
is only to quote Jonasson's sharp bound; Goel's polynomial
bound extends the theorem to sigma <= m-1 with the same
proof), floor = n - sigma, and let k be a rank with k <=
floor and log C(n,k) asymptotic to c n for some c > 0 (all
shallow ranks qualify).  Put M = C(n,k), mu = 1 + eps with
eps > 0 fixed, L = ceil(mu M).  Run the pure random
(sigma+1)-tail MTF walk from the uniform permutation, and for
a k-set S let hits_S = #{t in [k, L] : {w_{t-k+1},...,w_t} =
S}.  Then for every fixed r, uniformly in S,

    E[ hits_S^{(r)} ]  =  mu^r (1 + o(1)),

hence hits_S -> Poisson(mu) in distribution, P(hits_S = 0) =
e^{-mu} + o(1) uniformly in S, and

    E[ miss fraction ]  =  e^{-(1+eps)} + o(1).

By linearity the expectation statement holds at every
qualifying rank of the same walk.  NOT claimed (open, block
69(4)): concentration of the miss fraction; any whp statement
joint over sets or ranks.

70.2 PROOF.
(0) NOTATION.  F_t = sigma-algebra of the first t steps.  By
62.2 the walk is stationary: each window is uniform on the M
k-sets, so P(window(t) = S) = 1/M exactly.  Let dbar(s) =
sup_{x,y} ||P^s(x,.) - P^s(y,.)||_TV; dbar is submultiplicative
and ||P^s(x,.) - Unif||_TV <= dbar(s).  MIXING INPUT: T1 :=
T_mix(1/4) <= C n^3 (log n)/sigma^2 for sigma+1 = o(n)
[Jonasson 2006, Case 1: uniform selection from the bottom
sigma+1, moved to top — this walk verbatim; upper bound
within a factor 4 of the lower], and T1 <= n^{A0} for all
sigma <= m-1 [Goel 2006, via the inverse walk, which has the
same TV distances].  Then dbar(T1) <= 1/2 and dbar(j T1) <=
2^{-j}.  Set T := 3n T1, so M dbar(T) <= 2^n 2^{-3n} = 4^{-n}.
(1) THREE PER-FACTOR BOUNDS.  Fix S and times u > v.
  (a) [62.1, deterministic]  If u - v < floor then
      {window(u) = S, window(v) = S} is empty.
  (b) [62.3]  P(window(u) = S | F_{u-k}) <= beta :=
      (sigma+1)!/(sigma+1)^{sigma+1} <= e sqrt(sigma+1)
      e^{-(sigma+1)} <= e^{-sigma/2} a.s. (each of the k picks
      lands in the shrinking unused part of S with
      conditional probability <= min(remaining,
      sigma+1)/(sigma+1); valid for k >= sigma+1, true at
      shallow ranks since k ~ n/2 > sigma).
  (c) [63.2 + mixing]  If u - v >= T then a.s.
      | P(window(u) = S | F_v) - 1/M |  <=  dbar(u - v)
      <= dbar(T) (the set {pi : top-k(pi) = S} has uniform
      measure exactly 1/M).
(2) UPPER BOUND ON FACTORIAL MOMENTS.  E[hits^{(r)}] is the
sum over r-tuples t_1 < ... < t_r of P(window(t_i) = S for
all i), times r! for the orderings, divided — we count
ordered increasing tuples and multiply by nothing: hits^{(r)}
counts ordered r-tuples of DISTINCT hit times, which is r!
times the increasing count; we bound the increasing count and
carry the r!/r! bookkeeping silently as usual.  For an
increasing tuple with gaps g_i = t_i - t_{i-1}: peel factors
from the right.  The event ∩_{j<i} {window(t_j) = S} is
F_{t_i - k}-measurable whenever g_i >= k, which (a) forces
(all surviving tuples have g_i >= floor >= k).  Tower:

  P(∩_{i<=q}) <= P(∩_{i<q}) * ( a.s. bound on
                 P(window(t_q) = S | F) )

with the bound: 0 if g_q < floor [(a)]; beta if floor <= g_q
< T [(b), conditioning at F_{t_q - k} which contains
F_{t_{q-1}}]; 1/M + dbar(T) if g_q >= T [(c), conditioning at
F_{t_{q-1}}].  The first factor is exactly 1/M
(stationarity).  Summing over the number s of short gaps and
their positions and lengths:

  E[hits^{(r)}] <= mu SUM_s C(r-1, s) (T beta)^s
                   ( L (1/M + dbar(T)) )^{r-1-s}
                <= mu^r ( 1 + M dbar(T) + T beta / mu )^{r-1}.

Now M dbar(T) <= 4^{-n} -> 0, and T beta <= 3n n^{A0}
e^{-sigma/2} <= n^{A0+1} e^{-6 log n} -> 0 once sigma >= 12
log n... (for sigma >= (2 A0 + 4) log n; C0 adjusts to the
polynomial degree A0 of the quoted mixing bound, and for
sigma = o(n) regimes with Jonasson's T1 = O(n^3 log n /
sigma^2), C0 = 12 suffices).  Hence E <= mu^r (1 + o(1)).
[AUDIT-4 BRACKET 2026-08-21: the counting as displayed is
incomplete — bounding each long-gap sum by L(1/M + dbar(T))
independently ignores the simplex constraint on the gaps and
justifies only an r!-times-larger bound; the missing factor
is the simplex volume L^{r-1}/(r-1)!.  The complete count,
with the r!-cancellation displayed, is 74.1.  Conclusion
unchanged.]
(3) LOWER BOUND.  Restrict to tuples with all gaps >= T:
their number is at least (L - rT)^r / r! * (1 - o(1)) *
r!-bookkeeping as above, and each has probability >=
(1/M)(1/M - dbar(T))^{r-1} by the two-sided (c) chained the
same way.  Since rT/L <= poly(n) e^{-c n} -> 0 and
M dbar(T) -> 0:  E[hits^{(r)}] >= mu^r (1 - o(1)).
(4) POISSON AND MISSES.  (2)+(3) give factorial moments ->
mu^r for every fixed r, so hits_S -> Poisson(mu) by the
method of moments.  Uniformity in S: every bound above is
S-free.  Bonferroni truncation: for every J,
| P(hits = 0) - SUM_{j<=J} (-1)^j E[hits^{(j)}]/j! |
<= E[hits^{(J+1)}]/(J+1)! <= (2 mu)^{J+1}/(J+1)! for n large
(uniformly), so choosing J -> infinity slowly,
P(hits_S = 0) = e^{-mu} + o(1) uniformly in S, and summing
over S gives E[miss fraction] = e^{-mu} + o(1).  QED

70.3 Remarks.  (i) The only external inputs are the two
published mixing theorems; everything else is 62.1-62.3 and
63.2, proved above.  (ii) Where hypotheses enter: k <= floor
(window = set of last k letters, and (b) needs k >= sigma+1);
log M ~ cn (kills rT/L and lets M dbar(T) -> 0 with T =
Theta(n T1)); sigma >= C0 log n (kills T beta).  (iii) The
statement is about LINEAR windows of the infinite stationary
walk truncated at L; cyclic closure changes O(k/L) = o(1) of
the count.  (iv) Concentration (variance of the miss count)
remains OPEN — the cross-set close-window terms (block 69(4))
are not addressed by anything here.  (v) This formalizes: the
pure random eligible walk covers a 1 - e^{-(1+eps)} + o(1)
EXPECTED fraction of every shallow rank within the MDCU
budget — the first unconditional coverage theorem for any
eligible rule in this program; and it says with equal
precision what randomness alone CANNOT do: reach 1 - o(1).

The main conjecture remains unproven.

## 5.53 Block 71: the gap-stratified cross-set run bound —
per-rank concentration repaired (post-audit, new proof;
flagged for re-audit)

Block 69(4) withdrew 66's concentration because cross-set
close windows had no bound.  This block supplies one.  It is
NEW mathematics relative to the audited text and is
explicitly submitted for re-audit.

71.1 LEMMA (gap-stratified cross-set run bound — PROVED, same
telescoping as the endorsed 62.3).  Fix any two k-sets S, S'
(equal or not), any history F_v containing the event
{window(v) = S}, and any gap g >= 1.  On the event
{window(v+g) = S'}, the g picks at steps v+1..v+g must equal
the specific g-letter set S' \ {w_{v+g-k+1..v}} (determined
by F_v and S'; if the older part of the would-be window is
not contained in S', the probability is zero).  Each pick
lands in the shrinking unused remainder with conditional
probability <= min(remaining, sigma+1)/(sigma+1), so a.s.

  P( window(v+g) = S' | F_v )  <=  beta_g :=
     PROD_{r=1}^{min(g,k)} min(r, sigma+1)/(sigma+1),

with beta_g = g!/(sigma+1)^g for g <= sigma, and beta_g =
beta ~ e^{-sigma/2} for g >= sigma+1.  Consequently, uniformly
over ALL pairs (S, S') and independent of their overlap,

  SUM_{g=1}^{T} beta_g  <=  2/sigma + T beta  =:  eta = o(1)

for sigma >= C0 log n and T = 3n T_mix as in block 70.
[AUDIT-4 BRACKET 2026-08-21: the derivation is completed with
the explicit g <= k / g > k case split in 74.2 (for g > k
only the final k picks are constrained; the earlier picks are
bounded by 1 via the tower property).  The fourth auditor
exhaustively machine-verified the inequality at n = 5, 6 on
h100 over all pairs (S, S') and all gaps: no counterexample.]

71.2 THEOREM (per-rank concentration — PROVED modulo re-audit;
hypotheses as in 70.1).  For every pair S != S' and all fixed
(r, q), the joint factorial moments satisfy

  E[ hits_S^{(r)} hits_{S'}^{(q)} ]  =  mu^{r+q} (1 + o(1))

uniformly over pairs, and hence (joint Bonferroni truncation
as in 70.2(4)) P(hits_S = 0, hits_{S'} = 0) = e^{-2mu} + o(1)
uniformly.  Therefore

  Var(#misses)  =  SUM_{S,S'} [P(both 0) - P(0)P(0)]  =  o(M^2),

and by Chebyshev the miss fraction converges to e^{-(1+eps)}
IN PROBABILITY, at each shallow rank separately.

Proof of the moment estimate: chain factors right-to-left
over the merged, increasingly ordered tuple of constrained
times exactly as in 70.2(2).  A same-set adjacency at gap
g < floor contributes 0 (62.1); any adjacency at gap g in
[1, T) contributes at most beta_g (71.1 — valid for same-set
too, and sharper than needed there); an adjacency at gap
>= T contributes 1/M +- dbar(T) (63.2).  Summing each short
adjacency over its gap yields a factor eta in place of
70.2's T beta, giving

  E[joint]  <=  mu^{r+q} ( 1 + M dbar(T) + eta/mu )^{r+q-1}
            =  mu^{r+q} (1 + o(1)),

with the matching lower bound from all-gaps->=T tuples and
the two-sided (c) of 70.2.  QED
[AUDIT-4 BRACKET 2026-08-21: two repairs, both in 74.3 — the
factorial-moment counting completed with the r! q!
cancellation displayed (as in 74.1), and the phrase "joint
Bonferroni truncation" replaced by a one-dimensional
argument: Z = hits_S + hits_{S'} has factorial moments
(2 mu)^j (1+o(1)) by the Chu--Vandermonde identity for
falling factorials, and {Z = 0} is the joint vacancy event.
Conclusions unchanged.]

71.3 HONEST LIMITS.
  (a) Joint-over-ranks whp is NOT claimed: Chebyshev's rate
      here is ~ eta + (2mu)^J/J! per rank; with sigma ~
      sqrt(n log n) this is ~ n^{-1/2} polylog, and a union
      over Theta(sqrt n) shallow ranks does not close.  A
      higher-moment Chebyshev (4th) would need the same
      machinery at moment order 4 with rate eta^2 — plausible,
      unwritten.  Per-rank in-probability only.
  (b) The lemma 71.1 and theorem 71.2 postdate the third
      audit and have not been independently checked; they
      reuse the audit-endorsed telescoping of 62.3, and the
      single genuinely new observation is that the forced
      pick-set of a cross-set transition has size exactly g
      (the gap), making short cross-gaps CHEAP (beta_1 =
      1/(sigma+1)) rather than dangerous.  Submitted for
      re-audit.
  (c) Everything here is still about the PURE RANDOM rule.
      Layer 2 (adaptive upgrade to 1 - o(1)) is untouched.

The main conjecture remains unproven.

## 5.54 Block 72: the Layer-2 interface — what the proved
plateau hands to absorption, and the n/sigma steering wall
that forces sweeps

With 70/71 (pending re-audit), the state after a random
phase of length (1+eps)M is now THEOREM-grade input:
per-rank miss density e^{-(1+eps)} + o(1) in probability,
with uniform pairwise (and any fixed-order) vacancy
independence.  This block does the cost accounting for what
must come next.  No new theorems; one clean negative.

72.1 The coupon wall (restatement, now rigorous): the random
rule needs length M ln(1/delta) for miss fraction delta, so
1 - o(1) coverage costs omega(W) — adaptivity is NECESSARY,
not just convenient.  (Immediate from 70.1's Poisson limit.)

72.2 THE STEERING WALL (cost accounting — honest negative).
A repair phase that targets misses individually cannot work
at budget eps M: to steer the next window to a specific
neighbor S' = S \ {a} u {b}, the walk must wait for b to
enter the pool — the pool offers sigma+1 of n letters, so a
targeted hop costs ~ n/sigma steps in expectation.  Repair
cost ~ (miss count) x n/sigma = e^{-(1+eps)} M sqrt(n/log n)
>> eps M at the MDCU sigma.  Naive miss-tours are DEAD — the
same n/sigma factor that killed per-rank feedback schedulers
(the 53.1 wall) kills post-hoc tours.  Consequence: any
viable repair must be PHASE-COMPATIBLE — visit misses in an
order aligned with the letters' ~n-periodic pool returns, so
that steering is free on average.  This is exactly the shape
of the block-55 P-sweep; what was a design choice is now
forced by arithmetic.
[AUDIT-4 CORRECTION 2026-08-21: the n/sigma hop price above
is WRONG — it prices pool membership as i.i.d. sparse per
step, but in the conveyor pool appearances are clustered and
a specified letter's return time is Theta(n) (deterministic
dead time n - sigma).  Corrected accounting in 74.4; the
negative conclusion survives and STRENGTHENS (shortfall
factor Theta(n) instead of sqrt(n/log n)).]

72.3 The multi-rank nesting requirement (restatement with
proved inputs): a repair step's windows at all shallow ranks
are the nested suffixes of the word; a sweep that repairs
rank k while wasting its other-rank windows pays the
sqrt(n)-rank multiplicity again.  Sweep design must clear
nested chains of misses across ranks simultaneously (LRU
stack property, 54.1).  The absorption/serialization lemma
(55, still a PROPOSED lemma, per audit 2) is the remaining
open statement of Layer 2, but its INPUT distribution is now
proved rather than heuristic: miss sets of density
e^{-(1+eps)}, pairwise-independent to o(1), at every rank
separately.

72.4 Program state after blocks 60-72 (one paragraph,
honest).  Proved unconditionally (pending re-audit of 70-71):
the base-chain structure theory (62.1-62.3, 63.1-63.2), the
fixed-set plateau with Poisson hits, per-rank concentration
via the gap-stratified bound (71.1), the snub accounting
(60.1, 65.5), and the coupling lemmas of independent interest
(64.1-64.2, 68.1-68.4).  Closed by literature: mixing (Goel
2006; Jonasson 2006).  Open: joint-over-ranks whp rates; the
Layer-2 adaptive upgrade (fan access + late crowding under
one shared zero-preferring schedule, or equivalently a
phase-compatible multi-rank absorption sweep); the finite
witness program (n = 11 running); everything from the
handoff's exact conjectures.  The main conjecture remains
unproven.

## 5.55 Block 73: C15b — the 65.5 accounting is nearly tight,
and the binding channel is LATE FAN STARVATION; the
Late-Access Lemma formulated

C15b (h100, potential_c15b.py; n=15, slack 1.2, sigma in
{4,6}, rules: single-rank freshness-greedy at k=m+1 ("fresh")
and cover-first ("cover"), 2 seeds; focus rank quantities,
t0 in {L/2, 3L/4}).  Representative rows (t0 = 3L/4):

  sig=4 fresh: miss 313 | lateCrowd 233 | miss late-apps:
    mean 0.3, many exactly 0 | 65.5 bound 320
  sig=6 fresh: miss 148 | lateCrowd 284 | mean 0.5 | bound 157
  sig=6 cover: miss 339 | lateCrowd 626 | mean 1.4 | bound 359

  73.1 THE 65.5 BOUND IS NEARLY TIGHT at t0 = 3L/4: within
       2-8% of the actual miss count across all 8 rows.  The
       J-weighted time-split snub accounting is the right
       ledger for this process.
  73.2 FAILURE CHANNEL IDENTIFIED: over the WHOLE run N0 ~ 0
       (65.1: every set is offered early), but the misses'
       LATE appearance counts are 0.3-1.4 on average with
       minima at 0 — the Theta(sigma) appearance budget
       (60.3c) is FRONTLOADED into the crowded early phase
       where offers are wasted on competition.  Late
       crowding is tiny (233-626 snubs ~ 2-4% of the last
       quarter's steps): (L2)-late is empirically easy;
       (L1)-LATE is the whole game.
  73.3 MEASURED REPRESENTATIVENESS FAILURE, with a sign:
       misses are under-offered late by a factor 3-4 vs the
       uniform-prefix expectation (~0.3 (sigma+1) late
       appearances/set).  The walk's late prefix trajectory
       develops holes exactly at the faces of its misses;
       freshness feedback cannot repair what it is never
       offered.
  73.4 Single-rank freshness-greedy beats cover-first at its
       focus rank by >2x (148 vs 339 at sigma=6) — cross-rank
       compromises are expensive at the focus rank, another
       face of the multi-rank tension.
  73.5 THE LATE-ACCESS LEMMA (new formulation of the Layer-2
       core; OPEN).  For an eligible schedule, say a k-set S
       is "offered" at t if S is in the rank-k fan at t.
       Claim to prove or refute: there exists a
       zero-preferring eligible schedule such that whp every
       set still uncovered at time L - eps L/2 is offered
       Omega(1) times during the last eps L/2 steps.  By 65.5
       (with the measured smallness of late crowding made an
       output, not an input: crowding is quadratic in the
       late zero density), Late Access + published mixing
       implies coverage 1 - o(1) at rank k in (1+eps)M steps
       — the Sub-Poisson Walk Question reduces to KEEPING THE
       OFFER STREAM ALIVE, not to balancing fiber counts.
       This is a strictly weaker demand than LUL (it asks for
       Omega(1) late offers, not representativeness at all
       times) and converges with the forced phase-compatible
       sweep of 72.2: the schedule's late prefixes must sweep
       the miss faces in pool-phase order.

Status: data 2 seeds; 73.5 is a reformulation, not a result.
[AUDIT-4 CORRECTION 2026-08-21: 73.5 as stated is
INSUFFICIENT — Omega(1) late offers alone do not force o(M)
misses; the late-crowding bound must be a hypothesis of the
lemma, not "an output".  SUPERSEDED by LAL' in 74.5.]
The main conjecture remains unproven.

## 5.56 Block 74: fourth audit — all five repairs executed
(factorial-moment counting completed with the cancellation
displayed; 71.1 case split; 72.2 hop price corrected; the
Late-Access Lemma restated with the crowding hypothesis;
master handoff integrated)

The fourth reader audit (2026-08-21) credited block 70 as
"the first credible unconditional coverage theorem for the
random eligible walk in this program" and block 71's core
bound as plausible in core form (the auditor exhaustively
machine-checked 71.1 at n = 5, 6 on h100: no counterexample),
and demanded five repairs.  All five are executed below.
74.1-74.3 are proof completions and are submitted for
hostile re-audit together with blocks 70-71; per the
auditor's explicit instruction, block 71 is NOT promoted to
MASTER_HANDOFF as proved until that audit passes.

74.0 THE AUDIT'S FINDINGS (substance).
  (R1) Blocks 70 and 71 hand-wave an r! cancellation in the
       factorial-moment upper bounds; the displayed counting
       is incomplete.
  (R2) 71.1 must split g <= k from g > k explicitly; for
       g > k only the final k picks are constrained.
  (R3) 72.2's n/sigma waiting cost is wrong: pool appearances
       are clustered in the conveyor and a specified letter's
       return time is Theta(n).  The negative conclusion
       survives and strengthens.
  (R4) 73.5 (Late-Access Lemma) is insufficiently stated:
       Omega(1) late offers alone do not force o(M) misses
       without a proved late-crowding bound or a growing
       number of offers.
  (R5) MASTER_HANDOFF.md does not yet reflect blocks 70-73;
       block 71 must not be promoted there before one more
       hostile audit of its factorial-moment proof.

74.1 REPAIR OF (R1), SINGLE SET (completes 70.2(2)).
Diagnosis first, so the error is never repeated.  The old
display parametrized an increasing tuple by its GAP LENGTHS
and bounded each long-gap sum by L (1/M + dbar(T))
independently.  That free-box bound ignores the simplex
constraint g_2 + ... + g_r <= L: the number of admissible
gap vectors is the simplex count ~ L^{r-1}/(r-1)!, not
L^{r-1}, and the discarded (r-1)! is exactly the factor that
must cancel the r! relating ordered tuples (which hits^{(r)}
counts) to increasing tuples (which the display summed).
The displayed final line asserts the correct conclusion, but
the counting shown justifies only an r!-times-larger bound.

Correct counting.  hits^{(r)} counts ordered r-tuples of
distinct hit times, i.e. exactly r! times the increasing
count:

  E[hits^{(r)}] = r! SUM_{t_1 < ... < t_r}
                  P( AND_i window(t_i) = S ).

Call gap g_i = t_i - t_{i-1} SHORT if g_i < T := 3n T_1,
LONG otherwise.  Fix the set of short-gap indices, size s
(C(r-1, s) choices).  Parametrize each surviving tuple
injectively by
  (i)  its r - s BLOCK-LEADER times — t_1 together with
       every t_i whose gap is long — an increasing
       (r-s)-tuple in [L]: at most C(L, r-s) <=
       L^{r-s}/(r-s)! choices, and
  (ii) its s short-gap lengths, each summed against its own
       probability weight: SUM_{g=1}^{T} beta_g <= eta
       (71.1; for the single-set case 62.1 even restricts to
       g >= floor, where the sum is <= T beta <= eta).
Each leader consumes one probability factor <=
(1 + M dbar(T))/M (the first by exact stationarity, the rest
by 70.2(1c)); each short gap consumes its beta_g.  Hence

  E[hits^{(r)}]
    <= r! SUM_{s=0}^{r-1} C(r-1, s)
          [ L^{r-s} / (r-s)! ]
          [ (1 + M dbar(T)) / M ]^{r-s}
          eta^s
    =  SUM_{s=0}^{r-1} [ r! / (r-s)! ] C(r-1, s)
          mu^{r-s} (1 + M dbar(T))^{r-s} eta^s.

THE CANCELLATION, DISPLAYED.  The s = 0 term is

  [ r! / r! ] C(r-1, 0) mu^r (1 + M dbar(T))^r
    = mu^r (1 + o(1)):

the r! from ordered tuples cancels EXACTLY against the 1/r!
inside C(L, r) <= L^r/r!.  For s >= 1 the cancellation is
imperfect — r!/(r-s)! <= r^s — but those terms carry eta^s:
their total is at most 2^r mu^r SUM_{s >= 1} (r eta)^s <=
2^{r+1} r mu^r eta = o(1) for each fixed r (eta = o(1) by
71.1).  Hence E[hits^{(r)}] <= mu^r (1 + o(1)).

Lower bound, with the r! handled explicitly: restricting to
increasing tuples with all gaps >= T (count >=
C(L - (r-1)T, r) >= (L - rT)^r / r!) and chaining the
two-sided 70.2(1c),

  E[hits^{(r)}] >= r! [ (L - rT)^r / r! ] (1/M)
                   [ (1 - M dbar(T)) / M ]^{r-1}
                =  mu^r (1 - o(1)),

since rT/L <= poly(n) e^{-cn} and M dbar(T) <= 4^{-n}.

74.2 REPAIR OF (R2) (completes the derivation of 71.1).  The
bound is history-free: for ANY history F_v (the first v
steps), any k-set S', and any g >= 1,

  P( window(v+g) = S' | F_v )
    <=  beta_g := PROD_{r=1}^{min(g,k)}
                  min(r, sigma+1)/(sigma+1)     a.s.

The only chain property used: at every step the pool has
exactly sigma+1 letters (57.1) and the pick is uniform on
the pool given the entire past, so for any target set A
measurable at pick time, P(pick in A | past) <=
min(|A|, sigma+1)/(sigma+1).

CASE g <= k.  window(v+g) = I u {new picks}, where I =
{w_{v+g-k+1}, ..., w_v} is F_v-measurable with |I| = k - g
(distinct letters, since k <= floor).  If I is not contained
in S', the probability is 0 <= beta_g.  Otherwise, on the
target event the g new picks realize S' \ I exactly (any
repeat of a window letter is impossible within k <= floor
consecutive positions).  Let A_j = (S' \ I) \ {picks
v+1, ..., v+j-1}; on the target event pick v+j lands in A_j
and |A_j| = g - j + 1.  Chaining the pool bound over
j = 1..g:

  P <= PROD_{j=1}^{g} min(g-j+1, sigma+1)/(sigma+1)
    =  PROD_{r=1}^{g} min(r, sigma+1)/(sigma+1)    [r = g-j+1].

CASE g > k.  The window consists of the FINAL k picks only.
The first g - k picks are unconstrained: bound them by 1 via
the tower property, conditioning at F_{v+g-k}.  The final k
picks must realize S' exactly; with A_j = S' \ {window picks
so far}, |A_j| = k - j + 1 on the target event, the same
chaining gives PROD_{r=1}^{k} min(r, sigma+1)/(sigma+1).

Together: exactly min(g, k) constrained picks, as stated.
Distinctness of the window letters is enforced by A_j
itself; no extra event is needed.  The auditor's exhaustive
n = 5, 6 machine check (h100; all pairs (S, S'), all gaps)
passed.

74.3 REPAIR OF (R1) FOR JOINT MOMENTS, AND REMOVAL OF THE
"JOINT BONFERRONI" GAP (completes 71.2).  Fix S != S' at the
same shallow rank.  A window equals at most one set, so
S-hit times and S'-hit times are automatically distinct, and

  E[ hits_S^{(r)} hits_{S'}^{(q)} ]
    = r! q! SUM P( AND over the merged labeled tuple ),

the sum running over pairs (increasing r-tuple of S-times,
increasing q-tuple of S'-times) — equivalently over merged
increasing (r+q)-tuples carrying labels, with C(r+q, r)
label patterns per time skeleton.  Chain right-to-left as in
70.2.  Every adjacency at gap >= T contributes
(1 +- M dbar(T))/M regardless of labels (63.2 and
stationarity are label-free).  Every adjacency at gap < T
contributes at most beta_g by 74.2, which holds for ANY
F_v and ANY target set — also label-free; same-set
adjacencies additionally vanish for g < floor by 62.1,
which is no longer even needed.  Summing with the 74.1
parametrization (leader count C(L, r+q-s) <=
L^{r+q-s}/(r+q-s)!, short gaps eta each):

  E[joint]
    <= r! q! C(r+q, r) SUM_{s=0}^{r+q-1} C(r+q-1, s)
       [ L^{r+q-s} / (r+q-s)! ]
       [ (1 + M dbar(T)) / M ]^{r+q-s}  eta^s.

The s = 0 term is

  r! q! C(r+q, r) [ L^{r+q} / (r+q)! ] M^{-(r+q)} (1+o(1))
    = mu^{r+q} (1 + o(1)),

because r! q! C(r+q, r) = (r+q)! — the r! q! cancellation is
exact at s = 0 and eta-damped for s >= 1, as in 74.1.  Lower
bound: all-gaps->=T merged labeled tuples (count >=
C(r+q, r) (L - (r+q)T)^{r+q}/(r+q)!) with two-sided factors
give mu^{r+q}(1 - o(1)).  Hence, uniformly over pairs,

  E[ hits_S^{(r)} hits_{S'}^{(q)} ] = mu^{r+q} (1 + o(1)).

VACANCY WITHOUT TWO-DIMENSIONAL BONFERRONI.  71.2 said
"joint Bonferroni truncation"; genuinely two-dimensional
Bonferroni brackets are delicate, so we bypass them.  Put

  Z := hits_S + hits_{S'}.

The Chu--Vandermonde identity for falling factorials,
(x+y)^{(j)} = SUM_{i=0}^{j} C(j, i) x^{(i)} y^{(j-i)} (a
polynomial identity), gives

  E[ Z^{(j)} ] = SUM_i C(j, i) mu^{j} (1 + o(1))
               = (2 mu)^j (1 + o(1))

uniformly over pairs, for every fixed j.  The ONE-dimensional
Bonferroni argument of 70.2(4), verbatim with mu replaced by
2 mu, yields P(Z = 0) = e^{-2 mu} + o(1) uniformly; and
{Z = 0} = {hits_S = 0, hits_{S'} = 0} since both counts are
nonnegative integers.  The covariance and Chebyshev steps of
71.2 then stand as written:

  Var(#misses) <= M + o(M^2) = o(M^2),

and the miss fraction converges to e^{-(1+eps)} in
probability at each shallow rank separately.  71.3's honest
limits are unchanged (per-rank only; joint-over-ranks whp
remains open).

74.4 REPAIR OF (R3) (corrects 72.2; conclusion STRENGTHENED).
Withdrawn model: "the pool offers sigma+1 of n letters, so a
targeted hop costs ~ n/sigma steps" priced pool membership
as if i.i.d. sparse per step.  In the conveyor it is not: a
letter played at time tau is INELIGIBLE for exactly
floor = n - sigma further steps (deterministic dead time),
then eligible, and remains eligible until played — clustered
appearances, mean in-pool wait sigma + 1 under the random
rule (67.1).  So the return time of a SPECIFIED letter is
>= n - sigma = Theta(n) under EVERY eligible rule, and an
unplanned targeted hop (steer the window to contain a
specified letter that is not currently eligible) costs
Theta(n) expected steps, not n/sigma.

Corrected accounting: a repair budget of eps L steps
services O(eps L / n) = O(eps mu M / n) unplanned hops,
against e^{-(1+eps)} M misses — shortfall factor Theta(n),
WORSE than the sqrt(n / log n) previously claimed.  The
dichotomy sharpens: a targeted visit escapes the Theta(n)
price only by arriving while the needed letter's eligibility
window is ALREADY open, i.e. the visit order must follow the
letters' ~n-periodic pool phases.  Phase-compatible sweeps
are forced, exactly as 72.2 concluded, now by a stronger
margin.

74.5 REPAIR OF (R4): LAL' — the Late-Access Lemma correctly
stated (supersedes 73.5).  Fix a shallow rank k, let
t_0 = L - eps L / 2, and for a zero-preferring eligible
schedule define

  a(S)  = #{ t > t_0 : S is in the rank-k fan at t and S
             still uncovered },
  crowd = SUM_{t > t_0} (c_t - 1)^+,   c_t = # uncovered
             fan sets at step t.

The time-split snub inequality 65.5 gives, for every J >= 1,

  #misses(k) <= #{ S uncovered at t_0 : a(S) < J }
                + crowd / J.

LAL' — TWO SUFFICIENT FORMS (either one, proved for some
zero-preferring eligible schedule with the plateau state of
70/71 at t_0 as input, closes Layer 2 at rank k):
  (A) UNIT-OFFER FORM: all but o(M) of the sets uncovered at
      t_0 receive a(S) >= 1, AND crowd = o(M).   [J = 1]
  (B) GROWING-OFFER FORM: for some J = J(n) -> infinity, all
      but o(M) receive a(S) >= J, AND crowd = O(M) — merely
      bounded crowding suffices.                 [J -> inf]
The two forms trade access against crowding; (B) shows that
if the late offer stream can be made rich, the crowding
hypothesis weakens to boundedness.

Why 73.5 was insufficient as stated: with Theta(1) offers
and Theta(M) crowding the ledger returns O(M) — vacuous —
and the "crowding is quadratic in the late zero density"
remark is a heuristic, not a proof; crowding must be a
HYPOTHESIS.  Honest reading of the C15b data: measured crowd
at t_0 = 3L/4 was 233-626 against M = C(15,8) = 6435, i.e.
3.6-9.7% of M — small, but pointwise consistent with
crowd = Theta(M); both the access and the crowding
hypotheses of (A)/(B) are genuinely open.  73.5 is
SUPERSEDED by this subsection.

74.6 (R5) EXECUTED + STATUS LEDGER.  MASTER_HANDOFF.md
Section 7.2bis now carries a fourth-audit update paragraph
recording blocks 60-74 with these statuses: block 70 —
audited credible, counting completed here (74.1), awaiting
one more hostile audit; block 71 — core bound audited
plausible and machine-verified exhaustively at n = 5, 6
(auditor, h100), bookkeeping completed here (74.2-74.3),
NOT promoted to master-proved until it passes a further
hostile audit (auditor's explicit instruction); 72.2 —
corrected (74.4); 73.5 — superseded (74.5).  74.1-74.3 are
new displayed mathematics and are themselves part of the
submission for that audit.

The main conjecture remains unproven.

## 5.57 Block 75: the LAL' attack — the interleaved rule, the
dilution-robust short-gap lemma, and the reduction of
single-rank Layer 2 to one named mixing problem (R'')

Goal (NEXT item (i)): prove LAL' (74.5) for some schedule, or
locate the exact obstruction.  Result of this block: a design
map that eliminates the naive alternatives (75.1), a PROVED
robustness lemma showing the entire short-gap machinery of
70/71/74 survives constant-density feedback dilution (75.2),
an exact stationary offer identity (75.3), the isolation of
ONE open mixing problem R'' (75.4), a conditional reduction
skeleton LAL'(single rank) <= R'' (75.5, sketch status), and
a preregistered computational test C19 (75.6, running).

75.1 THE DESIGN MAP (honest statuses per item).
  (a) Pure random (p = 0 feedback): PROVED insufficient —
      coupon wall 72.1; final density e^{-(1+eps)} exactly
      (block 70).
  (b) Full feedback (p = 1, freshness-greedy): MEASURED
      insufficient — C15b late fan starvation (73.2-73.3):
      the trajectory grooves, late prefixes avoid miss faces
      3-4x below stationary rate.  No theorem, but the
      mechanism is clear: the trajectory law correlates with
      the coverage history, and NO mixing statement is
      available for it.
  (c) Rare feedback (density p -> 0): HEURISTICALLY
      insufficient by the budget integral — serves per step
      <= p + rho, so the staleness DE gives time
      >= M ln(1 + 1/p)/(1) to exhaust, i.e. budget (1+eps)M
      forces p >= 1/(e^{1+eps} - 1) = Theta(1).  (DE level
      only; recorded as motivation, not a theorem.)
  (d) Bounded soft tilt (every pick's conditional law within
      a factor C of uniform-on-pool): NO WALL IS CLAIMED —
      an earlier draft of this block tried to prove
      "bounded tilt => constant plateau" via the coupon
      integral and FAILED for a real reason worth recording:
      per-step C-tilts compound into unrestricted
      long-horizon steering of the prefix trajectory, so
      E[#fan zeros] cannot be bounded by (sigma+1) rho
      (representativeness is exactly what tilting destroys).
      The third audit's rejection of 57.2's tilting claim is
      the same phenomenon from the other side.  Bounded tilt
      is neither provably dead nor provably alive.
  Conclusion of the map: the live corner is CONSTANT-density
  feedback interleaved with genuinely uniform steps — dense
  enough to pay the budget (c), diluted enough that the
  uniform half can carry a mixing theorem (unlike (b)).

75.2 LEMMA (dilution-robust gap-stratified bound — PROVED,
one-line modification of 74.2).  Fix p in (0, 1), let the
FEEDBACK TIMES be any deterministic set D of density p
(e.g. Bresenham times floor(tp) > floor((t-1)p)), and let
the rule pick arbitrarily (any history-measurable law) at
times in D and uniformly on the pool at times not in D.
Then for any history F_v, any k-set S', any g >= 1:

  P( window(v+g) = S' | F_v )  <=  beta_g^{(p)}
    :=  PROD_{j in U(g)} min(|A_j| , sigma+1)/(sigma+1),

where U(g) is the set of NON-feedback times among the final
min(g, k) picks and |A_j| = (remaining target count) at pick
j, exactly as in 74.2 — i.e. bound the feedback-pick factors
by 1 and keep the uniform-pick factors, which still shrink
along the target event because EVERY window pick (feedback
or not) removes one element of the remainder on that event.
Consequences (delta := 1 - p = uniform density):
  (i)  the FINAL pick of any observed window taken at a
       non-feedback time has |A| = 1, so beta_g^{(p)} <=
       1/(sigma+1) for every g when observations are
       restricted to non-feedback steps;
  (ii) for g >= sigma+1, at least delta(sigma+1) - 1 of the
       last sigma+1 picks are uniform with |A_j| <= j, so
       beta_g^{(p)} <= e^{-c delta sigma} for a universal c;
  (iii) eta^{(p)} := SUM_{g=1}^{T} beta_g^{(p)}
        <= 2/(delta(sigma+1)) + T e^{-c delta sigma} = o(1)
        whenever delta sigma >= C1 log n.
So at MDCU sigma ~ sqrt(n log n), ANY constant dilution
delta > 0 preserves the entire short-gap half of the
70/71/74 moment machinery, with observation times restricted
to the uniform steps.  (Proof is 74.2 verbatim plus the
bookkeeping of which picks retain their factor; the density
of D enters only through |U(g)| >= delta min(g,k) - 1.)

75.3 EXACT STATIONARY OFFER IDENTITY (PROVED, symmetry).
Under the uniform stationary law on recency orders, for
every k-set S at every rank k <= floor:

  P( S is in the rank-k fan )  =  (sigma+1)/M,

exactly: P = SUM_{x in S} P(top(k-1) = S\{x} as a set, x in
the bottom sigma+1) = k (k-1)! (sigma+1) (n-k)! / n! =
(sigma+1)/C(n,k).  (Sanity: summing over all S gives the fan
size sigma+1.)  Hence in a late window of U uniform steps at
stationarity each set expects lambda = U (sigma+1)/M offers;
with U = Theta(eps M) and MDCU sigma this is lambda =
Theta(eps sigma) -> infinity, and M e^{-c lambda} = o(M) for
sigma >= C(eps) log n — exactly the few-offer count that
form (B) of LAL' needs, IF the offer counts Poissonize.

75.4 PROBLEM R'' (OPEN — the isolated mixing gap).  Let the
walk alternate: at times in D (density p, deterministic) an
ADVERSARIAL/history-dependent eligible pick (equivalently an
arbitrary back-cycle from {c_{n-sigma}, ..., c_n} chosen by a
measurable rule); at times not in D, a uniform back-cycle
(the Goel/Jonasson step).  QUESTION: does the interleaved
chain retain poly(n) worst-case TV mixing (uniformly over
rules), or at least for SOME zero-preferring rule of our
design?  Facts fencing the problem:
  (i)  p = 0 is Goel/Jonasson: T_mix = Theta((n^3/sigma^2)
       log n).
  (ii) p = 1 has NO mixing: the oldest-eligible rule is the
       rigid conveyor (period-n orbit).  So some dilution is
       necessary, and R'' cannot follow from soft general
       principles that ignore p.
  (iii) Entropy balance is EXACTLY tight: a uniform step
       injects log(sigma+1) bits; an adaptive adversary step
       is a state-dependent map of fan-in <= sigma+1, so it
       can compress up to log(sigma+1) bits.  A trapping set
       A must satisfy A G subset UNION_{a in G} a^{-1} A,
       and the cardinality budget |A G| <= (sigma+1)|A| is
       tight with equality — trapping requires a PERFECT
       matching structure, which the conveyor achieves at
       p = 1 but which uniform interleave plausibly
       destroys.  This is why R'' is nontrivial in both
       directions.
  (iv) We hold design freedom: the feedback rule is OURS
       (e.g. serve a uniformly random fan-zero), and D is
       ours; R'' is only needed for one good design.
Literature to check: time-inhomogeneous merging
(Saloff-Coste--Zuniga), permuted/adversarially-interleaved
walks.  [Not yet searched; queued.]

75.5 CONDITIONAL REDUCTION (SKETCH — submitted for scrutiny,
NOT a theorem yet).  Claim: R'' (poly mixing for the
interleaved rule INTER(p) below, at some p = 1 - delta with
constant delta = delta(eps)) implies LAL' form (B) at each
shallow rank, hence per-rank coverage 1 - o(1) in
(1+eps)M steps, for every fixed eps > 2 delta... more
precisely for eps > delta/(1-delta) + o(1) via the budget
f(p) = ln(1/p)/(1-p) -> 1 as p -> 1.  INTER(p): feedback
times Bresenham-D of density p; feedback step serves a
uniformly random fan-zero at the (single) focus rank if one
exists, else uniform; uniform step picks uniform on pool.
Skeleton:
  (1) Budget: serves per feedback step = 1{c_t >= 1};
      staleness integral with rho' = -[p 1{...} + (1-p)
      rho]/M covers M(1 - o(1)) sets within
      M ln(1/p)/(1-p) < (1+eps)M steps PROVIDED
      P(c_t >= 1) = 1 - o(1) while rho >= 1/sigma.
  (2) Regime I (rho >= polylog/sigma): P(c_t >= 1) >=
      (E c_t)^2 / E[c_t^2] by Paley-Zygmund; E c_t =
      (sigma+1) rho (1 + o(1)) and E[c_t^2] = (1+o(1))
      (E c_t)^2 + E c_t via the two-set offer moments —
      both supplied by the 74.3 machinery with 75.2's
      beta^{(p)} for short gaps and R'' for long gaps,
      conditionally on any t_0-past (the machinery's bounds
      are sup-over-history, which is what makes the
      time-inhomogeneous rho_t harmless).
  (3) Regime II (rho < polylog/sigma): time-split ledger
      65.5 at t_0 = start of regime II.  Offers of each
      surviving set in the remaining Theta(eps M) uniform
      steps Poissonize with mean lambda = Theta(eps sigma)
      (75.3 + moment machinery + R''): few-offer count
      M e^{-c lambda} = o(M) in expectation, Markov => o(M)
      whp.  Crowding: crowd = SUM (c_t - 1)^+ and on regime
      II c_t has mean sigma rho = o(polylog) ... E(c_t-1)^+
      <= E c_t(c_t - 1) = (1+o(1)) (sigma rho)^2 per step
      (pair moments again), so crowd = O(T_II (sigma
      rho)^2) = o(M) once rho = o(1/sigma) — and form (A)
      closes; for rho in [1/sigma, polylog/sigma] iterate
      the split O(log log) times (bootstrap), each round
      shrinking rho by e^{-Theta(eps sigma / polylog)}.
  GAPS that keep this a sketch: (g1) R'' itself; (g2) the
  bootstrap rounds condition on the (random) miss set at
  each t_0 — needs the sup-over-history discipline written
  out as in 74.1-74.3, plus a union over O(log log n)
  rounds; (g3) serves at OTHER ranks are ignored (single
  rank only; the multi-rank version needs a shared feedback
  discipline across sqrt(n) ranks — untouched); (g4) the
  DE constants in (1) assume serves are new-set serves,
  i.e. no double-serving, which zero-preference gives, but
  the accounting must exclude the o(1) fraction of feedback
  steps that serve an already-late-served set within the
  same fan collision.  None of these looks structural
  except (g1) and (g3).
  If this closes, the Layer-2 single-rank core becomes:
  LAL' <= R'' — one mixing problem, exactly parallel to
  Layer 1's R' which fell to Goel/Jonasson.

75.6 C19 (PREREGISTERED, launched on h100 before analysis
of results; potential_c19.py).  INTER(p) at n = 15, sigma in
{4, 6}, slack 1.2, p in {0, 0.5, 0.75, 0.9, 1}, 2 seeds.
Predictions recorded in the script header BEFORE results:
(P1) late-app means of final misses rise >= 2x at p in
{0.75, 0.9} vs p = 1; (P2) miss count U-shaped in p, with
an interior p strictly beating both endpoints; (P3) if
neither moves, the R'' route is empirically dead and this
block's 75.5 is to be marked refuted-in-spirit.

75.7 C19 RESULTS (honest scoring against the
preregistration).  Full grid (both seeds tightly paired;
sigma=4 / sigma=6 miss counts, seed-averaged):

  p:      0.0    0.5    0.75   0.9    1.0
  sig=4:  1965   998    578    414    319
  sig=6:  1955   892    428    229    145
  lateApp(4): 1.19  0.86  0.66  0.46  0.32
  lateApp(6): 1.81  1.39  1.12  0.76  0.55

  (P2) REFUTED at n = 15: the miss count is strictly
       MONOTONE in p — greedy (p = 1) wins, every dilution
       hurts (p = 0.9 costs a factor 1.30 at sigma=4, 1.58
       at sigma=6).  No U-shape at this scale.
  (P1) PARTIALLY CONFIRMED: dilution restores late access
       monotonically, exactly as the mechanism predicts
       (late-app means rise toward the pure-random level as
       p falls); the >= 2x threshold is met at p = 0.75 but
       not at p = 0.9 (~1.4x).
  (P3) NOT TRIGGERED: access moved.  The route is not
       "empirically dead", but the finite-n reading of 75.5
       is corrected as follows.
  INTERPRETATION (what C19 actually established): dilution
  is a PROVABILITY TAX — it buys the mixing structure the
  moment machinery needs and pays in lost serving steps; at
  n = 15 the tax exceeds the access benefit, because greedy
  is NOT yet access-limited at this scale (it still serves
  on 79-81% of its steps; its 3-4x late under-offering
  wastes slack the budget can still absorb).  The
  conditional route's value, if any, is asymptotic.  Note
  also greedy's own trend: 2.3% missing at n = 15 (sigma=6)
  vs 5.7% at n = 9 at the same slack 1.2 — the p = 1 rule
  itself keeps improving with n, consistent with the
  staleness DE's (1-o(1)) prediction; the open problem was
  never greedy's performance, only its unprovability.

75.8 C20 (PREREGISTERED, launched; potential_c20.py, h100).
Scale test of the dilution tax: R(n) := miss(INTER(0.9)) /
miss(INTER(1.0)) at slack 1.2, n in {17, 19}, sigma in
{round(0.7 sqrt(n ln n)), round(1.1 sqrt(n ln n))}, 2 seeds.
PREREGISTERED: the asymptotic reading of 75.5 predicts R(n)
non-increasing in n (tax vanishes as both rules' miss
fractions fall); if R(n) grows with n, mark 75.5
empirically dead at fixed slack and return to the p = 1
provability problem directly.

75.9 R'' AGAINST THE LITERATURE (search done).  Two adjacent
frameworks exist and NEITHER covers R'' — the gap is real
and informative:
  (i)  ROBUST MIXING (Ganapathy 2006): adversary interleaves
       arbitrary DOUBLY STOCHASTIC steps; applications
       include random-to-cyclic shuffles (Mossel-Peres-
       Sinclair 2004 lower bound; robust upper bounds
       n log n scale).  Doubly stochastic adversaries
       preserve the uniform law and cannot compress
       entropy.  Our feedback step is a STATE-DEPENDENT map
       with fan-in up to sigma+1 — entropy-compressing —
       outside the framework, and the framework's
       restriction exists precisely because compressing
       adversaries are the hard case.
  (ii) PERMUTED / DETERMINISTICALLY-ACCELERATED CHAINS
       (Chatterjee-Diaconis "speeding up with deterministic
       jumps"; Ben-Hamou-Peres cutoff for permuted chains):
       interleaved deterministic step is a FIXED BIJECTION
       Pi of the state space, state-independent; expansion
       conditions give O(log n / alpha^2 delta^4)-type
       mixing.  A bijection preserves entropy; our feedback
       map does not.
  REMARK (possible import route): on an ENLARGED state
  (permutation x coverage bookkeeping), a deterministic
  zero-preferring serve with deterministic tie-breaking may
  be made INJECTIVE (the served set and the pick are
  recoverable from the successor state), turning the
  feedback step into a bijection of the enlarged space —
  which would put INTER(p) inside the permuted-chain
  framework, with the expansion hypothesis as the remaining
  check.  Whether coverage-augmented injectivity actually
  holds (ages of the picked letter are overwritten) is the
  first thing to check; queued as the sharpest theoretical
  next step on R''.

75.10 C20 RESULTS (honest scoring).  Tax ratios R(n) =
miss(INTER(0.9))/miss(INTER(1.0)), seed-averaged, slack 1.2:

  law A (sigma = round(0.7 sqrt(n ln n)) = 4, 5, 5):
    n=15: 1.30    n=17: 1.43    n=19: 1.39
  high law (sigma = round(1.1 sqrt(n ln n)) = 8; n=15 used
  sigma=6 in C19, imperfectly comparable):
    n=15: 1.58    n=17: 1.77    n=19: 1.79

  PREREGISTERED CALL: "R(n) non-increasing".  Outcome: R is
  FLAT (a stable multiplicative constant ~1.4 at low sigma,
  ~1.8 at high sigma), rising slightly 15 -> 17 — the
  prediction fails at the letter.  Neither trigger fired
  cleanly: the tax neither vanishes nor grows.
  WHAT THE DATA ACTUALLY SAY:
  (a) A CONSTANT tax on a vanishing quantity is harmless
      for the conditional theorem: on the high-sigma track
      BOTH rules' miss fractions keep falling with n
      (greedy: 2.25% -> 1.80% -> 1.34%; INTER(0.9): 3.6% ->
      3.2% -> 2.4%) — both consistent with o(1), tax
      stable.  The route stays alive asymptotically, with
      the honest caveat that n <= 19 cannot separate o(1)
      from a small constant.
  (b) NEW DATUM, unplanned: at the LOW sigma law (constant
      0.7) both rules FLATTEN (greedy: 5.0% -> 3.5% ->
      3.6%; INTER(0.9): 6.4% -> 5.0% -> 5.1%), while at
      constant 1.1 both keep improving.  The witness-
      anatomy band constant ~1.1 sqrt(n log n) (blocks
      49-51) reappears as the empirical coverage threshold
      for ADAPTIVE rules: sigma with constant 0.7 is too
      small for o(1) coverage at slack 1.2, for greedy and
      diluted greedy alike.  The MDCU floor constant is not
      a witness artifact; it binds the rule class.
  (c) Late-access restoration replicates at scale
      (INTER(0.9) late-app means 0.9-1.0 vs greedy's
      0.6-0.7 at sigma=8).
  STATUS after C19+C20: 75.5's reduction remains the live
  conditional route; its cost is a constant-factor tax the
  budget absorbs only asymptotically; the immediate
  theoretical target is unchanged — R'' (75.4), sharpest
  first step the enlarged-state bijectivity check (75.9).

The main conjecture remains unproven.

## 5.58 Block 76: the injectivity check settled (negative,
with an exact structure), and the fiber-quotient
reformulation of R''

The 75.9 import route asked: can the deterministic serve
step be made injective on the enlarged state (permutation x
coverage), so that INTER(p) falls into the permuted-chain
framework?  Answer: NO for every natural rule — proved
below — but the failure is exactly (sigma+1)-to-1, and that
exactness yields a quotient on which the serve step IS
injective.  R'' survives in a sharper form.

76.1 LEMMA (insertion-depth invariance — PROVED).  Let
pi' = (x*, pi'_2, ..., pi'_n) be any state reachable by one
eligible step.  Its candidate predecessors under the
back-cycle generators are exactly pi_j = c_j^{-1} pi' =
(pi'_2, ..., pi'_j, x*, pi'_{j+1}, ..., pi'_n) for j in
[n - sigma, n] (x* must land in the pool block: sigma+1
candidates).  Then ALL candidates share:
  (i)   the entire non-pool order: positions 1..n-sigma-1
        of pi_j are (pi'_2, ..., pi'_{n-sigma}) for every j;
  (ii)  the pool SET: {x*} u {pi'_{n-sigma+1}, ..., pi'_n};
  (iii) the relative order of the pool minus x*:
        (pi'_{n-sigma+1}, ..., pi'_n);
  (iv)  in particular the k-prefix (k <= floor) and hence
        the fan and the zero set, for any coverage C.
The candidates differ ONLY in the depth j of x* inside the
pool block.  (Direct computation; three lines.)

76.2 COROLLARY (bijectivity REFUTED; the 75.9 import route
is dead as stated).  Call a rule POOL-BLIND if its pick
depends only on (non-pool order, pool set, coverage) — every
natural zero-preference rule (lexicographic or uniform-
random zero, cover-first, freshness-greedy) is pool-blind.
By 76.1 a pool-blind rule picks the SAME letter at all
sigma+1 candidates, so its serve map has fan-in EXACTLY
sigma+1 on its image (0 off it): maximally non-injective.
(On serve steps the predecessor coverage is determined —
C = C' \ {top-k(pi')} — so the enlarged-state fan-in is
sigma+1 exactly, not 2(sigma+1).)  Age-aware tie-breaks
(serve the oldest/youngest zero-completer) make the valid-j
set an INTERVAL of depths, generically still of length > 1:
no natural rule is bijective.  Any rule engineered to pin j
must condition the pick on the picked letter's own depth,
which provably conflicts with serving zeros whenever the
zero-ranks are constant on depth intervals.  Refuted.

76.3 EXACT ENTROPY LEDGER (sharpens 75.4(iii)).  For
pool-blind rules the serve step compresses exactly
log(sigma+1) bits (uniform fibers of size sigma+1), which
EQUALS the uniform step's injection log(sigma+1).  The
75.4 entropy balance is tight not just in the worst case
but for every natural rule: R'' is precisely the question
of whether this zero-sum entropy flow circulates (mixing)
or stalls (conveyor-like trapping).

76.4 THE FIBER-QUOTIENT REFORMULATION (research note —
the positive residue of the refutation; OPEN).  Define the
fiber of pi' as its full candidate set {pi_j}.  By 76.1,
pi' RECOVERS its predecessor fiber exactly (items (i)-(iii)
are functions of pi').  Hence on the quotient space Q =
{fibers}, the pool-blind serve step is WELL-DEFINED (all
fiber members map to the same pi') and INJECTIVE (distinct
images have distinct predecessor fibers).  The uniform step
remains genuinely random.  So on Q, INTER(p) has the shape
deterministic-injective + random — the permuted-chain shape
(Chatterjee-Diaconis; Ben-Hamou-Peres) that 75.9 wanted,
obtained by quotienting instead of by engineering the rule.
CRUX to check before this can carry weight: (q1) whether
the uniform step descends to a Markov kernel on Q (the lift
law from a fiber may depend on the representative — the
depth of the last-served letter feeds the NEXT step's pool
boundary crossing); (q2) whether coverage bookkeeping stays
fiber-measurable across multiple steps; (q3) what expansion
the quotiented serve map has.  If (q1) fails, the quotient
is only an upper-bounding device (a hidden-Markov collapse)
— still potentially usable for TV upper bounds via lumping
inequalities.  Queued as the R'' work front.

76.5 SELF-CORRECTION (same day, found while checking q1):
THE TV FORMULATION OF R'' (75.4) IS DEAD — TRIVIALLY.  A
pool-blind serve step maps the state space (sigma+1)-to-1
onto an image of density ~ 1/(sigma+1) (76.2); hence
IMMEDIATELY after any serve step the state law is confined
to that image and its TV distance to uniform is >=
sigma/(sigma+1) - o(1).  At constant serve density the
chain NEVER TV-mixes to uniform, for every zero-preferring
rule, deterministic or randomized.  So "poly(n) worst-case
TV mixing of INTER(p)" is the wrong demand, and with it the
fiber-quotient import of 76.4 loses its TV target (its
q1-q3 may retain value for functional bounds only).
WHAT THE MACHINERY ACTUALLY NEEDS (R''-functional, the
corrected minimal open statement): for the designed rule,
at uniform observation times, ONE-SIDED fan-membership
uniformity at long range —

  P( S in fan(v+u) | F_v )  >=  (1 - o(1)) (sigma+1)/M

for all k-sets S at shallow ranks, all histories F_v, and
all u >= U_0 = poly(n).  This is far weaker than mixing:
a LOWER bound only, on a single local functional, exactly
what the few-offer count in 75.5(3) consumes (the upper
bounds the machinery needs come from 75.2, which is
already proved).  The rule's deliberate bias toward miss
faces can only help the surviving sets' offers; the danger
is grooving (C15b), and the question is whether constant
uniform dilution kills grooving at the level of this one
functional.  R'' is henceforth read as R''-functional;
75.4's fencing facts (conveyor at p = 1, entropy ledger)
still delimit it, but the Chatterjee-Diaconis import route
is retired along with the TV target.

Status: 76.1-76.3 proved (submitted with 74.1-74.3 for the
standing re-audit); 76.4 is a direction, retargeted by
76.5; 76.5's negative half (TV death) is proved, its
functional restatement is the open frontier.

The main conjecture remains unproven.

## 6. Scope guard

Nothing in this file is a theorem about `nu`.  It is a fully
specified candidate whose failure, if it fails, will be at V2's
joint interactions — and whose verification would close handoff
conjecture 7.1.3.  The exact conjectures `nu(k)=B(k)` and finite
`k=17` are untouched either way.
