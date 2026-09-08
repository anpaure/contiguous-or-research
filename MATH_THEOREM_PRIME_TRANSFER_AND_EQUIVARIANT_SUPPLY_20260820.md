# Prime transfer for coefficient one, and the equivariant chain supply at prime dimension from necklace-poset SCDs

Date: 2026-08-20 (fifth file of this date).  Status: Theorems P1, P2 and
Corollary P3 are proved (P2 modulo one explicitly stated lifting lemma
proved here and the cited literature constructions); Section 4 states
the reduced remaining gate.  Same-day adversarial self-audit: all
links of the day's chain re-derived (P1 width ratios exact; S4 demand
is an upper bound under sharing; the erosion-compiler equality
re-proved under run floors; P2.1 lifting and the `Cat_m -> W` chain
counts verified); one wording correction applied to P3 (symmetry
closes the cross-domain spacing component; the within-domain component
is localized into Open Problem 8 with its slack intact).  Independent
audit by a second reader remains required by project standards before
§5.6 claims are treated as certificate-grade.  Companions as indexed in
`RESEARCH_INDEX.md` under this date.

## 1. Theorem P1 (prime transfer)

If `nu(p) <= (1+delta_p) W(p)` for every prime `p`, with `delta_p -> 0`,
then `nu(k) = (1+o(1)) W(k)` for all `k`, where
`W(k)=binom(k, floor(k/2))`.

*Proof.*  For `k` given, let `p` be the largest prime `<= k`; by any
`o(k)` prime-gap bound (Hoheisel's classical `k^{0.97}`, or
Baker–Harman–Pintz `k^{0.525}`), `g:=k-p=o(k)`.  Iterating the top-bit
splice `nu(j+1)<=2nu(j)` (master handoff Section 5.1) `g` times:
`nu(k) <= 2^g nu(p) <= (1+delta_p) 2^g W(p)`.  For the width ratio,
`W(j+1)=2W(j)` exactly when `j` is odd, and
`W(j+1)=2W(j)·(1-1/(j+2))` when `j` is even.  Hence

\[
\frac{2^g W(p)}{W(k)}
=\prod_{\substack{p\le j<k\\ j\ \mathrm{even}}}
\Bigl(1-\frac{1}{j+2}\Bigr)^{-1}
=1+O\!\Bigl(\frac{g}{k}\Bigr)=1+o(1).
\]

Combining, `nu(k) <= (1+delta_p)(1+o(1))W(k)`, and `nu(k)>=B(k)>=W(k)`
always.  ∎

Consequently **the asymptotic coefficient-one conjecture needs only to
be proved for prime `k`** — where `k=n` is odd (so the odd-`n`
architecture applies directly with no even case) and, decisively, the
rotation `Z_n` acts freely on every layer except `\varnothing,[n]`.

## 2. Lemma P2.1 (quotient chains lift, and rotations are disjoint)

Let `n` be prime and let `O_1 < O_2 < ... < O_s` be a chain in the
necklace poset `N_n=B_n/Z_n` (proper nonempty classes).  Then
representatives `S_1 subset S_2 subset ... subset S_s` exist (choose
`S_1` arbitrarily; if `S_i` is chosen and `O_{i+1}>O_i`, some
representatives `T_0 supset S_0` exist with `S_0=S_i - j`, so
`T_0+j supset S_i`), and the `n` rotations of the lifted chain are
pairwise disjoint chains in `B_n`, since every proper nonempty orbit is
free for `n` prime.  A chain partition of `N_n` (restricted to ranks
`1..m`) therefore lifts to a `Z_n`-equivariant chain partition of the
full strict lower cone of `B_n`.  ∎

## 3. Theorem P2 (equivariant supply at primes) and Corollary P3

By Griggs–Killian–Savage (Electron. J. Combin. 11 (2004), #R2; the
construction behind rotationally symmetric Venn diagrams for prime
`n`), and in general by Jordan (JCTA 117 (2010), 625–641), the necklace
poset `N_n` has a symmetric chain decomposition; for prime `n`,
restricting to ranks `1..m` and applying Lemma P2.1 yields:

**Theorem P2.**  For every prime `n=2m+1` there is a
`Z_n`-equivariant partition of the strict lower cone of `B_n` into `W`
chains (`n` rotated copies of `(W-1)/n+...=Cat_m`-many lifted quotient
chains, the counts matching by the freeness of the action and
`n·Cat_m=W`, with the two trivial classes handled separately at `O(1)`
cost).

**Corollary P3 (the binding cut class of Open Problem 7′ closes at
primes).**  Cutting all `n` rotations of each lifted chain identically
(Lemma S2), anchoring by lifting a perfect matching of the quotient
middle bipartite multigraph (regular by freeness, hence König), and
serving in a chronology of the form `Phi, rho(Phi), ..., rho^{n-1}(Phi)`
for a fundamental segment `Phi` of length `(1+2eps)Cat_m` with
departure-quiet margins of width `d+1` at the domain boundaries, makes
the entire sparse-descent pipeline `Z_n`-equivariant.  Every
coordinate's global departure pattern is then an exact rotation of
every other's.  Precisely (audited wording): the *cross-domain*
component of the per-coordinate age-spacing cut class closes
identically, by equivariance together with the quiet margins (spacing
across any domain boundary is at least `2(d+1)`); the *within-domain*
component becomes a balanced finite design problem inside Open Problem
8, retaining its factor-4 slack, with the coordinate-concentration
worst cases — the collision obstruction that excludes random
assignment over the full chronology — eliminated by the exact balance
across coordinates.  Symmetry thus removes the unbounded part of the
binding cut class and localizes the remainder to one fundamental
domain.

## 4. The reduced remaining gate

**Open Problem 8 (fundamental-domain schedule).**  Within one domain
`Phi` (length `(1+2eps)Cat_m`, plus quiet margins), schedule the
`(1+eps)Cat_m` quotient segments — precedence within each segment's
window, per-step departures bounded by `m+1` against average demand
`sqrt n/(4C)` (slack `Theta(sqrt n)`), within-domain per-coordinate
spacing at slack 4, cross-boundary spacing handled by the quiet
margins — and verify the residual interval cuts by total unimodularity.

**Note (the coherence class also carries slack).**  A departure of `x`
at step `i` advances the staircase of every active window `a` with
`x in X_a`; mistimed advances ("pollution") are avoided not by timing
alone but by owner design: `X_a = G_1^{sigma(a)} ∪ P_a` with the
padding `P_a` drawn from coordinates *stable over the window's span*
(no scheduled departure there).  Stable-coordinate supply at any step
is `n-(departures in the next d steps)=n(1-1/(4C)+o(1))`, against
padding demand at most `m+1<=(n+1)/2` per window: pointwise slack
factor `~2(1-1/(4C))`.  The coherence constraints are therefore a
third slack-carrying flow class (padding assignment), alongside
capacity (`sqrt n`) and spacing (`4`); Open Problem 8 asks for their
joint integral realization.
A solution proves `nu(p)=(1+o(1))W(p)` for that prime by the
sparse-descent assembly, hence `nu(k)=(1+o(1))W(k)` for ALL `k` by
Theorem P1.

The reduction chain, now fully explicit and with every named external
ingredient published, is:

\[
\text{GKS/Jordan SCD}+\text{Lemma P2.1}+\text{Open Problem 8}
\ \Longrightarrow\ \text{P3}+\text{S1–S4}+\text{collar}+\text{absorption}
\ \Longrightarrow\ \nu(p)=(1+o(1))W(p)
\ \overset{\text{P1}}{\Longrightarrow}\ \nu(k)=(1+o(1))W(k)\ \forall k.
\]

## 4.5 Same-day addendum: two further structural facts about Open Problem 8

**(a) The upper band rides the arrivals at zero additional volume.**
Each step has `|A_i|=|D_i|`; unions of consecutive owners equal the
initial owner plus its arrivals.  Cutting the SCD of the *upper* cone
(ranks `m+2..n-1`) into co-segments and serving them through the
arrival stream is the exact time-reversal of the lower service: the
same turnover events carry both block structures (departures encode
lower blocks, arrivals encode upper co-blocks), the volume ledgers are
identical, and Theorem S4's factor-two slack covers both sides
simultaneously because the two demands ride disjoint aspects of the
same events.  Open Problem 8 therefore needs no extra length for the
upper band.

**(b) The coherence constraint is a Helly interval-alignment.**
Overlapping windows cannot be given disjoint segment tops (two
`~m`-sets in `[2m+1]` generically intersect), so shared coordinates
are unavoidable; by the spacing constraint each coordinate departs at
most once inside any single window's span, so a shared coordinate `x`
has, in each active window containing it, one *due interval* (the
steps at which its block is scheduled to depart there), and the single
departure of `x` must lie in the intersection of its due intervals.
Intervals on a line satisfy Helly's theorem: pairwise intersection of
due intervals suffices.  Block boundaries within each window are
freely placeable (at most `C sqrt n` blocks in a `C sqrt n`-step
window), so Open Problem 8 is precisely the satisfiability of a
pairwise due-interval alignment CSP with per-window timing freedom,
per-step slack `sqrt n`, spacing slack `4`, padding slack `~2`, and
volume slack `2` — every numerical parameter favorable, the remaining
content purely the combinatorial consistency of the alignment.

## 4.6 Same-day addendum II: two rigidity lemmas and the sweep reformulation

**(c) Periodic clocks are infeasible.**  Assigning each coordinate
departure slots of fixed period `~4(d+1)` (the natural spacing period)
fails: a given coordinate then has a slot inside a given `d`-step
window with frequency `~1/4`, and a served segment needs all of its
`up to m` departing coordinates slotted inside its window in block
order — an event of exponentially small frequency.  Per-coordinate
timing must be designed jointly with the assignment, not fixed in
advance.

**(d) The affine alignment law.**  Suppose the stream is generated by a
global departure-time function `t(·)` (per coordinate-occurrence) and
windows are served wherever their blocks come due.  For a window at
position `a` serving segment `sigma`, coordinate `x`'s due interval is
`[a+w·idx_sigma(x), a+w(idx_sigma(x)+1))`; a single global time `t(x)`
lies in all containing windows' due intervals iff `t(x)-a` is (up to
`w`) an affine function of the block index in every served segment
containing `x`.  Hence **under any global-schedule ansatz, each
segment's block partition must be exactly the level-set partition of
`t` restricted to its support**: the chain family must be
*sweep-generated* — successive differences of every chain must follow
one global (for equivariance: cyclic) order of departure classes.  The
GKS/Jordan SCD chains are not a priori sweep-generated, which
identifies the precise mismatch between the supply of Theorem P2 and
the schedule of Open Problem 8.

**Open Problem 8′ (sweep-generated cover; implies Open Problem 8 via
the global schedule).**  Construct a `Z_n`-equivariant cover of the
strict lower cone of `B_n` (`n` prime) by at most `(1+eps)W` nested
families, each of at most `C·sqrt n` sets, whose successive differences
sweep the cyclic order of `[n]` (each difference a union of
consecutive-in-sweep departure classes), with `o(W)` covering defect
allowed.  Such a cover, fed into the global cyclic sweep schedule,
satisfies the alignment law identically, and the remaining cut classes
(capacity `sqrt n`, spacing 4 via the sweep period, padding `~2`,
volume 2) close as ledgered; by the day's chain this implies
`nu(k)=(1+o(1))binom(k,floor(k/2))` for all `k`.  Note the arc-peeling
heuristic: peeling the cyclic blocks (arches) of a representative in
cyclic order generates sweep chains naturally, but canonical selection
among the multiple peelings producing the same set is exactly the
remaining exact-cover content.

**Decisive check identified.**  The classical Greene–Kleitman chains
are sweep-generated for the LINEAR order: along a GK symmetric chain,
elements are added at the unmatched positions from left to right, so
successive differences follow one global order — the affine alignment
law holds for GK with a linear sweep.  The Griggs–Killian–Savage prime
construction and Jordan's general proof are cyclic modifications of GK
bracketing.  **If the GKS/Jordan necklace chains are cyclically
sweep-generated from each chain's root phase** — a property of their
explicit constructions that must be verified line-by-line against GKS
Section 3 — **then the object of Open Problem 8′ already exists in the
literature**, and the remaining distance to coefficient one is the
slack-verified bookkeeping of this file (cutting, anchoring, padding,
margins) assembled through the day's chain.  This verification is the
single highest-value next action in the program.

**Verification executed same day (against the paper's full text).**
GKS Section 4.3: their necklace chains are exactly the Greene–Kleitman
`tau`-orbits restricted to block-code-minimal representatives,
`J_z=z,tau(z),…,tau^{k-1}(z)` with `tau` adding `min(U_0)`; their
Lemmas 15–16 show `tau` preserves both the block code and the
representative property, so every chain lives in one fixed phase frame
and adds elements at its unmatched positions in increasing order.
**The GKS necklace chains are sweep-generated — confirmed.**

**The departure-wheel schedule and the extent obstruction.**  Feeding
sweep-generated chains to the global schedule whose departures follow
the cyclic coordinate order (the "wheel", one revolution `=4C sqrt n
(1+2eps)` steps) gives: per-coordinate spacing = one revolution
`>= d+1` by construction; per-step density `sqrt n/(4C)` exactly
matching the volume ledger; serving positions determined by chain
phase; and alignment automatic.  Two hard boundaries emerged with
proofs: windows may not exceed one revolution (a coordinate departing
twice inside a window annihilates the erosion letters), and therefore
a served segment's difference support must have cyclic extent at most
a constant fraction of `n`.  GK/GKS differences (unmatched zeros) are
cyclically spread, so cutting their chains by extent would multiply
the chain count by `Theta(1)>1` factors that break the length budget.
The wheel therefore pairs not with the GKS supply but with an
*extent-localized* sweep supply — precisely the arc-peeling chains of
Open Problem 8′, whose differences are consecutive cyclic blocks by
construction.

**Open Problem 8″ — REFUTED same day (gap-length no-go).**  The
multiplicity calculation for arc-peeling ran and disproved the
formulation: a set covered by consecutive-block erasure has a single
empty cyclic arc of length at least its erasure depth, but a typical
rank-`(m-y)` target has all cyclic gaps of length `O(log n)` (its
complement is a near-half-density word), so consecutive-block
differences cannot cover typical targets at any depth `omega(log n)`.
Arc-peeling covers only exponentially atypical sets; no canonical
choice can fix this.  (Method note: this is the third same-day
refutation-by-calculation, after Conjecture C and canonical-PBBS Open
Problem 1; the program's calculational hygiene is functioning.)

**The extent constraint was an artifact; the corrected schedule.**
Re-derivation: the wheel need not tick every coordinate every
revolution.  Let the global clock be *demand-driven*: departures occur
in the fixed cyclic class order but classes with no pending demand are
skipped, per-step departure sets may be large (per-step capacity has
`sqrt n` slack), and per-coordinate spacing is enforced by the
full-cycle length (`~4d` steps) rather than by revolution ticks.  Then
a `d`-step window never sees a coordinate depart twice (spacing), the
letters survive, and a served segment needs only its difference
sequence to be *order-consistent* with the clock from its phase — no
extent condition.  **The GKS supply re-qualifies**: its chains'
differences are increasing in position order within a fixed phase
frame (verified above), exactly clock-consistent.

**Open Problem 8‴ — REFUTED for independent supplies same day (the
conflict-density calculation; fourth refutation).**  A served window
must protect its surviving core (`~n/2` coordinates) from all foreign
departures during its `d`-step span, while foreign demand during any
span touches `~n/4` coordinates (density `sqrt n/(4C)` times `d`,
independent of cohort partitioning).  For two independent segments the
probability that one's differences avoid the other's core is
`exp(-Theta(sqrt n))`; hence uncorrelated segments cannot be
span-concurrent, spans must be pairwise disjoint, and the chronology
length is at least `(1+eps)W·d` — coefficient `sqrt n`, not one.  The
cut GKS supply is uncorrelated across chains, so no clock or
assignment can serve it densely: sweep-generation was necessary but
laminarity is the binding requirement.

**The laminarity principle (the day's terminal identification).**  The
exact `k<=16` optima evade the conflict bound precisely because their
overlapping windows serve near-nested target families: one departure
advances every concurrent staircase consistently.  Densely serialized
erosion service *requires* the chain cover to come equipped with a
serving order in which span-concurrent segments share
`(1-o(1))`-fraction of support with aligned differences — a laminar
chronology.  This is handoff conjecture 7.2.1 / gate 7.3.8 in its
irreducible form: today's reductions strip away every soft obstruction
(counting, volume, spacing, capacity, padding, alignment, supply
exactness — all closed with slack or by published theorems) and
localize the entire remaining difficulty of the erosion corner in the
laminar correlation structure itself.  Dually, the singleton corner's
irreducible core is central-ucycle-type coverage (calibrated earlier
to the open wreath conjecture and CDG problem).  Both corners' cores
are now exactly matched to named open problems with all peripheral
matter cleared; any future attack should aim directly at laminar
chain chronologies or at defective central ucycles, and nothing else.

**Actionable form of the laminarity core.**  The conflict bound kills
*pre-assigned* supplies; but the owners along a stream are themselves
evolving stream states (`X_{a'} = X_a` minus departures plus
arrivals), so span-concurrent windows automatically have correlated
owners.  Laminar service therefore means the segment served at each
position must be chosen *adaptively* inside the current state — the
supply and the stream form a self-consistent pair, a fixed-point
existence problem.  The finite optimal words for `k<=16` are exactly
such self-consistent pairs, found by search; the asymptotic question
is whether an iterative-absorption argument (build most of the stream
greedily with a reserved absorber correcting the terminal defects) can
manufacture them for all prime `n`.  The specific first calculations
for the next assault: (1) the greedy phase's defect rate — what
fraction of lower targets remain unserved when segments are chosen
greedily inside evolving states (the Q6-style calculation for the
adaptive greedy); (2) the absorber primitive — a bounded-length stream
gadget that can serve any one prescribed leftover target while
preserving all ledgers (the analogue of the handoff's octagon/exchange
actuators, now with multi-swap freedom); (3) whether the prime
transfer's restriction to prime `n` unlocks transitive-group averaging
for the greedy analysis (all coordinates equivalent under `Z_n`).

**Same-day execution of calculation (1): the Gray-ordering resolution
and the conflict statistic `kappa`.**  Two further proved facts and
the resulting compression:

*Steering bound.*  Serving segments in an order with typical top
distance `Theta(m)` costs `~(Hamming distance)/(turnover per step) =
Theta(sqrt n)` steps of owner steering per segment — coefficient
`sqrt n`.  Dense service requires consecutive tops within
`O(turnover)` Hamming distance.

*Gray resolution.*  Order the top segments by a revolving-door Gray
code of the rank-`m` layer (consecutive tops differ by one swap; such
combination Gray codes are classical).  Then: (a) span-concurrent
segments share `(1-o(1))` of their supports — the laminarity
requirement holds by construction, dissolving the conflict-density
obstruction for this ordered supply; (b) steering costs `O(1)` per
segment; (c) every GK descent removes its elements in decreasing
position order, so any two concurrent descents remove shared
coordinates in the same relative order — due-interval alignment is
automatic up to window-internal boundary placement, which has slack.

*The residual statistic.*  What remains is the keep/remove conflict:
for Gray-adjacent (more generally span-concurrent) tops, a coordinate
removed by one descent may lie in the surviving core (chain bottom) of
the other.  Define `kappa` = the average, over Gray-adjacent pairs, of
`|D_a ∩ core(a')|` — removals of one demanded as survivors by the
other.  If `kappa` is small (conflicts `o(1)` per pair, or removable
by local reordering/absorber), the erosion core closes and, through
the day's chain, coefficient one follows; if `kappa=Theta(1)`
robustly, the Gray order must be co-designed with the bracketing —
e.g., ordering chains by their GKS block codes so that adjacent
chains have compatible matched structures — or this too is a
refutation.  **`kappa` is a purely combinatorial statistic of
Greene–Kleitman bracketing under revolving-door adjacency: finite,
well-posed, and computable by hand on small cases; it is the single
number the next session must compute first.**

**Same-day structure of `kappa` (the status criterion and the
path-cover reformulation).**  For Gray-adjacent tops `T={a,b,x}`-type
and `T'={a,b,y}`-type (shared support `T∩T'`), a conflict is exactly a
shared element that is unmatched (scheduled for removal) in one
segment's GK bracketing but matched (surviving core) in the other's:
**conflict-freeness = agreement of bracket status on shared
elements.**  Consequently a conflict-free dense serialization exists
iff the *status-preserving swap graph* on the middle layer — vertices
the rank-`m` sets, edges the single swaps that preserve the bracket
status of all shared elements — can be covered by `o(W/sqrt n)`
vertex-disjoint paths (each path boundary costs only `O(d)` stream
steps, so path COVER, not Hamiltonicity, is the right demand; the
allowance `o(W/sqrt n)` is enormous).  The graph refines the
`|M|`-strata (ballot-number sizes, only `m+1` strata, far below the
path allowance), so the question is intra-stratum connectivity and
near-linear traversability under local unmatched-one moves and local
rematchings — finite-checkable at `n=7` (strata sizes `14,14,6,1`)
and `n=9`.  Positive answer ⟹ `kappa`-route closes ⟹ (day's chain)
coefficient one; negative ⟹ sixth refutation and the singleton corner
stands alone.  At `n=7` the cone segments have at most two removals
each and the strata are tiny; the check is a finite exercise now
fully specified.

**The `n=7` check — executed same day, PASSES.**  Bracketing all 35
rank-3 subsets of `[7]` by the prefix-excess rule (a `1` at `p` is
unmatched iff its excess is a strict new positive maximum) gives the
unmatched-set census `|U|=3,2,1,0` with counts `1,6,14,14` — exactly
the SCD chain profile `1/6/14/14`, validating the table.  The status
classes (fibers of `U`) are eight: `∅` (14 sets, the staircase family
`p_1>=2, p_2>=4, p_3>=6`), `{1}` (9), `{3}` (3), `{5}` (2), `{1,2}`
(4), `{1,4}` (1), `{3,4}` (1), `{1,2,3}` (1).  Within a class all
shared statuses agree automatically, so intra-class Johnson edges are
all conflict-free; the `∅`- and `{1}`-classes are richly connected
staircase/star families and the rest are tiny.  A path cover by 8
paths exists — versus 35 vertices.

**Asymptotic class count.**  A feasible unmatched set `U={u_1<...<u_j}`
satisfies the staircase condition `u_i<=2i-1`, and typical excess is
`Theta(sqrt n)`, so the number of status classes is
`exp(O(sqrt n·log n))` — *sub-exponentially small* against the path
budget `o(W/sqrt n)=exp(Theta(n))`.  Covering class-by-class therefore
meets the budget with astronomical room, and the erosion core
compresses to its final residual lemma:

**Residual Lemma L (intra-class path covers).**  For every status
class (fixed unmatched set `U`, matched parts varying over the
bracket-compatible region), the induced status-preserving Johnson
graph admits a path cover by a number of paths sub-exponential in `n`
— an allowance of `o(W/(sqrt n·e^{O(sqrt n log n)}))` paths per class
on average.  The `n=7` classes satisfy this trivially; the general
statement concerns connectivity-type properties of shifted Johnson
families and is the last open link of the erosion chain.  (Failure
mode to test first: classes whose induced graphs are near-independent
sets; the flexibility of matched-element moves makes this implausible
but it must be proved or refuted — the sixth-refutation candidate.)

**Same-day resolution of Lemma L's graph half, and the burst gate
beneath it.**  Two proofs and one corrective discovery:

*Connectivity of every class — PROVED.*  A class member's excess
profile is pinned at `e(u_i)=i` (new maxima rise by unit steps), so
the profile decomposes into independent corridor segments between
pins; each segment family is the ideal lattice of a staircase poset,
whose flip graph (single-cell moves = single Johnson swaps) is
connected via the dominance order.  Classes are products of connected
flip graphs, hence connected.  Moreover each class family is the
ideal family of a poset, so the classical Pruesse–Ruskey Gray code
for order ideals (successive ideals differing in at most two
elements; via prism-Hamiltonicity of bipartite cover graphs) yields a
single serving path per class with `<=2`-swap steps — Lemma L holds
in the form needed, pending a line-check of the Pruesse–Ruskey
statement.  Within a class, status agreement holds for ALL pairs, not
just neighbors, so intra-class service is conflict-free at any
offset... at the level of roles.  However:

*The burst gate — a NEW obstruction below Lemma L (corrects the
previous block's "one link" assessment).*  Same-class concurrent
windows share their entire removal set `U`, and a shared removal must
lie in every active window's due interval; with `|U|` blocks pacing a
`d`-step window, due intervals have width `~d/|U|`, so same-class
concurrency is possible only at offsets `<=d/|U|`.  Serving a class
in bursts of that width with dead gaps of `d` costs a factor `|U| ~
sqrt n` — unless bursts of different classes interleave, which
requires cross-class phase alignment of shared removal rhythms; and
globally periodic rhythms are exactly what rigidity fact (c) above
refutes for coverage.  The alignment/coverage tension therefore
recurses from segments to classes: the erosion chain's remaining
content is a two-level phase/socket scheduling problem — precisely
the "residence, phase/socket" rows of handoff Sections 5.5 and 7.3,
now derived from first principles at their exact scale
(`pace=d/|U|`, class sizes, interleaving degrees).  The `n=7` PASS
stands but is blind to this gate (`|U|<=3` there makes bursts free).
Next candidate resolutions: (1) tower scheduling — order classes so
concurrent classes have nested `U`-prefixes with aligned shared
rhythms and staggered private ones; (2) fractional smearing — serve
each class's members across `|U|` interleaved passes, one removal
block per pass (this multiplies window count but each pass's window
shrinks to `~d/|U|`, keeping `L·(window)` invariant — the
first-glance ledger is neutral and deserves the next calculation);
(3) accept the sixth-refutation possibility for dense erosion service
and re-weight effort toward the singleton corner.

**Same-day execution: smearing refuted; burst chaining via a class
Gray walk; the two-level architecture.**  (a) Smearing fails in both
semantics: pipeline re-visits cost `Theta(W sqrt n)` owner repeats,
and pass-split windows cannot realize mid-depth targets, whose
erosion spans all earlier passes — the `|U|`-for-`|U|` cancellation
was illusory (the run floor is set by the deepest window a
coordinate participates in, not by the pass width).  (b) The burst
gate itself resolves structurally: a class's dead zone (its windows'
`d`-step tails) can host other classes' bursts provided the guest's
removal set avoids the host's core-union; within a burst, 2-Gray
adjacency makes cores drift by at most 2 per step, so the core-union
stays `~m+O(burst width)`, and a guest class fits iff its `U'` lies
in the complement — abundantly satisfiable.  Chaining `~|U|` active
bursts simultaneously requires the SEQUENCE of classes to have
slowly-drifting core-regions: **a Gray walk on `U`-space** (staircase
sets, again an ideal-type family, again Pruesse–Ruskey-amenable).
The erosion architecture is thus two-level Gray: a slow class walk
carrying nested within-class ideal Gray codes.  (c) The single
remaining calculation: shared-`u` due-window alignment across
consecutive bursts — due width `~pace=d/|U|`, burst offset `~d/|U|`,
index shifts `<=1` at each class step, paces within `1±1/|U|`: all
first-order quantities MATCH at the margin, and the verdict rests on
exact constants via the TU/flow check on the two-level structure.
No blow-up factor survives at any level examined; no proof exists
either.  (d) Note the recursion is converging: level sizes contract
`W -> e^{O(sqrt n log n)} -> (U-space classes) -> ...`
super-exponentially, so the phase/socket hierarchy bottoms out in
`O(1)`-to-`O(log)` levels; the two-level design may already be the
whole tower at the scales in play.

**Correction (same day, block 21): the shared-removal rate theorem
kills the class-Gray-walk as stated.**  A coordinate `u in U` is
removed by EVERY member of its class, so dense single-class service
demands `u`-departures at rate `|U|/d`, while the run floor caps
every coordinate at rate `1/(d+1)` — a hard factor-`|U|`
contradiction (this, not due-window width, is the true content of the
burst gate).  Gray-adjacent classes share all but one element of `U`
and therefore compound the same rates: the block-(b) resolution is
dead as stated — its core-avoidance condition was necessary but not
sufficient.  The corrected design: **removal-disjoint backbone
interleaving** — group classes by similar matched backbones and
interleave `r >= |U|` classes with pairwise-disjoint `U`-sets; each
coordinate's demand dilutes by `r`, the spacing constraint closes
with equality at `r=|U|+1`, and class throughput is fully restored
(`r` classes at rate `1/r` each).  Disjoint feasible `U`-families
exist in abundance (`u_1` may be any odd position — witnessed at
`n=7` by the disjoint feasible values `{1,2}` and `{3,4}`; the
earlier staircase bound `u_i<=2i-1` was erroneous and is hereby
withdrawn — the correct constraint is `#1s before u_i=(u_i+i)/2-i`
feasibility, which is loose).  The remaining object, one level
refined: a packing of `U`-space into epochs of `~sqrt n`
removal-disjoint classes, each epoch sharing a slowly-drifting
matched backbone, chained by the core-avoidance condition of (b).
Every individual constraint (rate, spacing, cores, drift,
disjointness, class counts) is now satisfiable in isolation with
computed slack; the joint packing is the live question.

**Scope correction (block 22): the rate theorem binds member-local
schedules only; stationary dues reconcile everything.**  If removal
indices drift so that each coordinate's due-time is stationary in
global time (`d(idx)/dt=1/pace` — exactly the affine alignment law of
Section 4.6(d), which the verified GKS sweep supply satisfies), then
ONE departure of `u` serves every concurrent member needing `u`,
regardless of concurrency; the run-floor cap binds only the number of
distinct departure events per support-residence, and remove-and-drop
(a removed coordinate exits subsequent supports, legal at the
multi-swap owner drift rate `sqrt n/(4C)` per step, which the
steering bound permits for owners even though served tops move by
2-Gray) supplies exactly one event per residence.  Consequently the
burst gate (block 19) and the rate obstruction (block 21) both bind
only designs whose dues track member-local block schedules; the
globally-clocked design threads both.  Integrated statement of the
erosion core after all corrections — three simultaneous conditions on
one walk serving `(1-o(1))` of the layer:

1. **status agreement** on shared support among span-neighbors (the
   conflict criterion, necessary — block 17);
2. **stationary dues** (the affine/global-clock law, necessary for
   shared departures — blocks 11–12 and 22);
3. **one departure per support-residence** (the run-floor rate cap,
   necessary — block 21), realized by remove-and-drop at the
   permitted owner drift rate.

Each pairwise combination is known to be satisfiable; each condition
alone has computed slack; the triple-joint walk over `(1-o(1))W` tops
is the final object.  All six prior refutations are consistent with
this statement: each killed a design violating exactly one of the
three conditions.  The `n=7` structures satisfy all three vacuously
or checkably; the first nontrivial triple-joint test is `n=11`
(`m=5`, `W=462`), beyond hand computation for the full walk, but its
LOCAL obstructions (does a status-class boundary admit a
stationary-due crossing with remove-and-drop?) are finite checks the
next session should run before any further architecture.

## 5. Scope guard

Theorem P1 is unconditional (given classical prime-gap bounds).  Lemma
P2.1 and Theorem P2 are complete given the cited published SCDs of the
necklace poset; the restriction/truncation of those SCDs to the cone
and the exact quotient chain counts should be re-verified line-by-line
against GKS Section 3 before any downstream exactness claim, since only
their existence and symmetry — not their length profile — is used by
the cut in Lemma S2 (any chain partition works; symmetric chains are a
convenience).  Open Problem 8 is open; nothing here claims it.  The
exact conjectures `nu(k)=B(k)` and finite `k=17` are untouched.
