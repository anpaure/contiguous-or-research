# Two exact buffered-C6 routes to an additive-constant induction

Date: 2026-07-31  
Lane: root synthesis, compound seams versus dispersed leave  
Status: exact conditional induction and exact comparison.  The selector
theorems are proved; one named construction theorem remains open on each
route.  No unconditional `nu(k)<=B(k)+O(1)` theorem is claimed.

## 0. Verdict

There are two genuinely different ways to avoid the cubic load of the full
buffered-C6 atlas.

* **Route A, sparse exposure.**  Count occurrence-labelled physical seam
  events, not damaged windows.  Charge

  \[
                         s_{\rm ev}\le a\Phi+s_0,                 \tag{0.1}
  \]

  and compress the entire `O(D)` signed collar of one event into one exact
  packet task.  On a bounded regenerative sublevel `Phi<=E`, this gives an
  absolute number of lists and an elementary greedy selector.
* **Route B, dispersed leave.**  Permit many task lists, but assign them to
  source-private anchors so that every complete resource token has weighted
  anchor code

  \[
              N_0^\times(r)=0,\qquad N_1(r)=O(1),\qquad
              N_2(r)=O(m).                                      \tag{0.2}
  \]

  Then every token has external menu load `O(m)`, every `O(D)` packet has
  external degree `O(mD)`, and Haxell selects from quadratic lists when
  `D=o(m)`.

There is no total logical ordering.  Route B is genuinely weaker on the
**exposure/task-count axis** because it permits an unbounded dispersed leave;
Route A is genuinely weaker on the **selector/correlation axis** because a
bounded bank needs only per-other-list exclusions and not a global weighted
code.  In the bare source-private C6 role model, bounded `H` automatically
gives `N_1,N_2=O(1)`, so Route A is the sparse special case of Route B's local
load accounting.  That implication need not extend to nonlocal cap/topology
tickets.  End to end, Route A asks for a strong defect-Lipschitz physical
lift, while Route B replaces it by a stronger global anchor-and-routing
correlation theorem.

## 1. Common packet and conflict model

Let `m` be the side parameter and `D=D_m` the largest declared dependency
span.  A task `t` has a list `P_t` of complete packets.  A packet names:

1. its local C6 or rerouter support;
2. every protected colour, occurrence, and replacement witness;
3. its complete cap path and sink ticket; and
4. every topology edge or ownership state needed for literal composition.

If a packet is claimed to preserve arbitrary-width upper intervals across
its slot, it also names the complete prefix-OR and suffix-OR sequences of the
off-state and replacement.  The current typed boundary state (ports,
connectivity, endpoint type) is only topological and does not contain this
information.

The lean fixed-basis face in Theorem 2.4 is an explicit exception to the
per-packet cap-path requirement: one common matching is frozen in advance,
and packets delete only distinct cells unused by that matching.

Two packets are adjacent in the cross-list conflict graph `Gamma` iff they
cannot be used together.  Pairwise nonadjacency is accepted as composition
only when topology is fixed/triangular and all capacity and witness choices
are named tickets; otherwise a separate graphic/Rado test remains.

For lists `P_i,P_j`, define

\[
 \delta_{ij}:=\max_{p\in P_i}|N_\Gamma(p)\cap P_j|,
 \qquad
 \Delta:=\max_{i,p\in P_i}\sum_{j\ne i}|N_\Gamma(p)\cap P_j|.   \tag{1.1}
\]

For any task order `pi`, greedy succeeds if

\[
 |P_{\pi(j)}|>
       \sum_{r<j}\delta_{\pi(r),\pi(j)}                         \tag{1.2}
\]

at every step.  In particular, `|P_t|>=alpha m^2` and
`delta_ij<=beta mD` suffice for `H` tasks when

\[
                      \alpha m^2>(H-1)\beta mD.                 \tag{1.3}
\]

Haxell instead applies whenever

\[
                            \min_t|P_t|\ge2\Delta.               \tag{1.4}
\]

If every list has average external degree at most `barDelta`, deleting its
packets of degree greater than `2barDelta` retains at least half the list and
leaves induced maximum degree at most `2barDelta`.  Hence an original lower
bound `L_0>=8barDelta` implies (1.4).  This averaging statement must hold in
every list, not merely after averaging over all lists.

The complete unpruned atlas cannot supply (1.4): a fixed incidence occurs in
`6m^2` packets and a fixed shore vertex in `3(m+1)m^2`, so a packet already
has cross-list degree at least `(3m+2)m^2` through one endpoint.  This is a
no-go only for feeding the full atlas directly to Haxell.  The exact
average-load extraction theorem below shows that it is not a no-go for a
Catalan-scale dispersed reservoir.

## 2. Route A: compound seam tasks and reachable-chain induction

### 2.1 Exact seam ledger

For two cyclic chronologies on the same labelled occurrences, let the old-
only and new-only seam sets have size `s`.  At owner-window span `ell`, the
AD fragment identity gives

\[
     |\mathcal B^-_\ell|=|\mathcal B^+_\ell|
       =\sum_P\min\{\ell,|V(P)|\}\le\ell s.                    \tag{2.1}
\]

Least-seam ownership partitions these changed windows.  An arbitrary pairing
of one old and one new seam gives at most `s` **signed ledger groups**, each
with changed owner-window support in two radius-`D` collars.  This is only
bookkeeping.  It becomes one selectable **compound task** only if a certified
edit-event pairing supplies a nonempty packet menu whose members close the
entire signed collar and every complete ticket.  Without such a pairing,
there are at most `2s` one-sided groups.  A changed linear cut, reroot,
prefix/suffix, or endpoint cap is a separate exceptional task.

For a serial construction, `s_ev` in (0.1) counts phase-resolved,
occurrence-labelled seam events with multiplicity.  The symmetric difference
of only the initial and final endpoint sets can hide intermediate seam churn
and is not a valid substitute.

### 2.2 Conditional task bound

Let every carried parent defect have at most `lambda` named child descendants,
let at most `r_0` fresh nonseam/endpoint tasks be born, and require these,
the inherited tasks, and the seam-owned tasks to exhaust the complete child
ledger.  With certified paired collars,

\[
 H(\Phi)\le\lambda\Phi+r_0+s_{\rm ev}
          \le(\lambda+a)\Phi+(r_0+s_0).                          \tag{2.2}
\]

With only one-sided collars, replace `a,s_0` by `2a,2s_0`.  Crucially, (2.2)
counts compound packet lists, not the `Theta(D)` individual windows in each
collar.  Any unclassified fresh residence, upper, compiler, cap, or topology
row invalidates the count.

Fix an invariant sublevel `Phi<=E` and put

\[
                    H_E=(\lambda+a)E+r_0+s_0.                    \tag{2.3}
\]

If every guarded compound list has at least `alpha m^2` packets, every fixed
packet excludes at most `beta mD` members of any other current list, and
`D=o(m)`, then (1.3) holds eventually.  If the simultaneous repair is exact
and returns `Phi'<=E`, induction produces one infinite regenerative spine.
An exact reset means zero collar deficiency and zero leakage; every casualty
is charged to `Phi'`.  A separately authenticated terminal theorem of length
`B(k)+O(Phi+1)` then gives `nu(k)<=B(k)+O(1)` along the spine and its certified
parity children.

Bounded `H` alone is not a selector theorem.  If two quadratic lists force
every complete ticket through one cap-one vertex `z`, their conflict graph is
`K_(L,L)` and no pair exists.  Route A still needs the literal pairwise
exclusion/composition row in (1.3).

### 2.3 Exact protected-upper compression interface

For a slot `X=(x_1,...,x_h)`, put

\[
 \Sigma_\vee(X)=
 \left(h;\left(\bigvee_{i=1}^{j}x_i\right)_{j=0}^{h};
          \left(\bigvee_{i=h-j+1}^{h}x_i\right)_{j=0}^{h}\right). \tag{2.4}
\]

Equivalently, let `f_X(z),l_X(z)` be the first and last positions at which
coordinate `z` occurs.  Since

\[
 z\in P_j(X)\iff f_X(z)\le j,\qquad
 z\in S_j(X)\iff l_X(z)\ge h-j+1,                              \tag{2.5}
\]

equal-length slots have identical full signatures iff all their coordinate
first/last occurrence times agree.  This endpoint-time table is the compact
proof-safe signature.

If a replacement `X'` has `Sigma_vee(X')=Sigma_vee(X)`, every interval
meeting the exterior of the slot preserves its OR: it is an unchanged
exterior suffix joined to a preserved slot prefix, a preserved slot suffix
joined to an unchanged exterior prefix, or both.  This holds simultaneously
at every width and for any number of disjoint fixed slots.  In a cyclic word
the opening and physical address map must be fixed; a reroot is a separate
endpoint task.  Therefore an `O(D)`-long OR-boundary-equivalent packet leaves
only intervals wholly internal to its `O(D)` physical support for the upper
audit.  There can still be `Theta(D^2)` internal interval rows, and cap or
topology tickets may be nonlocal.

The typed/topological condition in the current buffered-hex theorem is
strictly weaker; this is not a claim about every repository use of “boundary
signature.”  It fixes typed ports, endpoint types, and connectivity, but not
the sequences in (2.4).  The literal rank-two Johnson paths
`12-13-34` and `12-24-34` have the same length, endpoints, path relation, and
total union `1234`.  After the common exterior owner `15`, however, the
crossing interval through the first two slot owners has union `1235` versus
`1245`.  Thus this buffered protected-upper interface must be upgraded to
**OR-boundary-equivalence** on the actual physical chronology in every
relevant phase.  Conversely, identical signatures do not fix internal
intervals: `(1,2,1)` and `(1,3,1)` have the same full signature but different
middle singleton ORs.  The internal packet audit remains literal.

This proves the compression implication, not its supply.  Positive-density
OR-boundary-equivalent menus are part of the missing construction.

### 2.4 Lean fixed-basis packet interface

The complete witness/path-ticket interface can be replaced by a smaller exact
face.  For a slot `X`, write

\[
 \operatorname{Int}_\vee(X)=
   \left\{\bigvee_{i=a}^{b}x_i:1\le a\le b\le |X|\right\}.       \tag{2.6}
\]

Fix one trace-guarded compiler graph with a matching `M_0` covering every
required target, and let `B` be its unused-cell dual basis.  A packet option
is **lean exact** when:

1. its actual physical slot is OR-boundary-equivalent to the off-state by
   the endpoint-time test (2.5), and
   \(\operatorname{Int}_\vee(X_{\rm off})
     \subseteq\operatorname{Int}_\vee(X_{\rm on})\);
2. it has the common typed boundary relation and uses one fixed connector/
   topology skeleton shared by every option;
3. its only change to the fixed compiler incidence face is deletion of one
   named cell `b(p) in B`; in particular it does not delete or alter any edge
   of `M_0`; and
4. simultaneously selected packets have disjoint physical slots and distinct
   deletion cells `b(p)`.

### Theorem 2.4 (lean packet composition)

Every selection of lean-exact packets preserves all old upper coverage,
the common topology, and the common trace-guarded compiler matching `M_0`.

#### Proof

An interval spanning a packet boundary is preserved by endpoint-time
equality.  An interval wholly inside an old slot has an equal-OR replacement
inside the new slot by internal-union dominance; intervals outside all slots
are unchanged.  Hence every old upper witness survives.  The common boundary
relation and fixed connector make the disjoint slot replacements commute on
one topology skeleton.  Finally, every deleted compiler cell lies in the
unused dual basis and no matched edge changes, so `M_0` itself remains a
matching covering all required targets.  Distinct deletion cells enforce the
cell capacity.  No replacement-witness choice or alternating-path ticket is
needed.  QED.

The quantifiers are load-bearing.  `M_0` must be one fixed trace-guarded
matching common to every option, the signature is taken on the actual
physical phase rows, and compiler changes must be exactly the named unused-
cell deletions.  If a packet changes a matched incidence, adds a target not
covered by `M_0`, changes the connector, or lacks internal dominance, the
general witness/graphic/gammoid interface is again necessary.

The authenticated nonflat K16 optimum is a positive cell-disjointness
calibration of this fixed-basis gate.  Its residence frontier and first-used
cell indices are

\[
             \rho=(0,0,6384),\qquad u=(0,2,6390),                 \tag{2.7}
\]

so the Ferrers prefix criterion `rho<=u` passes with raw depth-three margin
`6390-6384=6`.  The construction actually uses
`tau=(0,0,6386)`, leaving four further unused prefix units.  This validates
the fixed-basis criterion on the optimum at the level of cell identities.
It does not prove that the same matching is trace guarded after retiming;
the final-threshold point/row guards remain an open inheritance condition.

### 2.5 The one missing Route-A theorem

The single missing construction can be stated as the following package.

> **Guard-complete bounded-seam lift.**  From every state in one bounded
> reachable sublevel, construct one protected Pascal child with a
> phase-resolved seam-event charging certificate
> `s_ev<=a Phi+s_0`; classify every child obligation as inherited,
> seam-owned, or one of at most `r_0` exceptions; provide one quadratic exact
> whole-collar menu per owned event (or per one-sided event), including an
> `O(D)` lean-exact slot relative to one common connector and one fixed
> trace-guarded compiler matching, with distinct available deletion cells in
> its unused dual basis and dependency span `D=o(m)`; and regenerate the same
> bounded state.  Outside this fixed-basis face, restore the complete
> witness/graphic/gammoid tickets.

The prepared all-six ECO face proves the numerical seam implication
`s_ev<=24Phi+s_0` once its four-phase task exposure, common connector, halo
separation, and protected packet cube already exist.  It does not construct
that face uniformly.  Hence the missing theorem is the guard-complete lift,
not the scalar coefficient `24` or the AD window count.

## 3. Route B: a large but `1/m`-dispersed leave

At one fixed directed C6 source incidence, a resource token occurs in
exactly `m^2`, `m`, or `1` packets according as its role is source-fixed,
one-free, or zero-free.  After assigning one task to each chosen anchor, let
`N_j(r)` count anchors at which token `r` has the corresponding role.  The
exact aggregate menu load is

\[
                     \Lambda(r)=m^2N_0(r)+mN_1(r)+N_2(r).        \tag{3.1}
\]

Suppose the assignment has, for every physical, colour, witness, cap, and
topology token `r`,

\[
 N_0^\times(r)=0,\qquad N_1(r)\le A,qquad N_2(r)\le Bm,         \tag{3.2}
\]

where `N_0^times=0` means that a source-fixed token is absent from every
other selected list.  Then the external load through one token is at most
`(A+B)m`.  If each complete packet uses at most `c_0D+c_1` tokens,

\[
                         \Delta\le K(c_0D+c_1)m=O(mD),           \tag{3.3}
\]

independently of the number of task lists.  Quadratic lists and `D=o(m)`
therefore satisfy Haxell's row (1.4) eventually.  This is the precise sense
in which the leave is `1/m`-dispersed: its potentially large task count does
not accumulate more than `O(m)` menu occurrences on any typed resource.

Source-anchor injectivity alone proves only the fixed-role part.  There are
`m` pairwise endpoint-disjoint anchors for which one owner token is one-free
at every anchor, giving `N_1=m` and load `m(m-1)`.  Complete cap tickets are
also independent of local C6 geometry: two locally disjoint tasks can still
have gammoid rank one through a shared cap cut-vertex.  These examples show
that (3.2) must be proved for complete routed packets, not inferred from
local support or endpoint privacy.

### 3.1 Unconditional Catalan-scale raw reservoir

Let

\[
       W={2m+1\choose m},\qquad I=(m+1)W                         \tag{3.4}
\]

be the numbers of middle-level vertices on one shore and oriented source
incidences.  Every anchor has `m^2` raw C6 choices.  The exact typed-token row
energy of one anchor against the complete atlas is

\[
 R_m=18m^3+51m^2-4m-5<44m^3,                                   \tag{3.5}
\]

while the simpler union bound is `(18m+54)m^2`.  The finite replay for
`m=2,3,4,5` independently checks (3.5).  Retain each anchor with probability
`m^{-2}` and delete anchors whose conditional average exceeds four times its
mean.  There is a deterministic survivor family `S` with

\[
 |S|\ge {3I\over4m^2}=\Theta(W/m),\qquad
 \overline\Delta(P_e;S)\le72m+216\quad(e\in S).                 \tag{3.6}
\]

Per-list Markov pruning retains at least `m^2/2` choices of maximum external
degree at most `144m+432`; Haxell therefore chooses one pairwise-disjoint raw
C6 at every retained anchor for `m>=579`.  Thus the raw local atlas already
contains at least a constant times `W/m` mutually compatible actuators; the
family may be truncated to `Theta(W/m)`, the correct Catalan scale.  The
cubic full-atlas maximum-load theorem cannot be cited against a dispersed
reservoir.

More generally, if equal lists of size `L` have row energy at most `R`,
Bernoulli density `p` followed by weighted-degree deletion retains at least
`3pI/4` lists of average conflict at most `4pR`; per-list Markov pruning and
Haxell work whenever

\[
                              L\ge32pR.                            \tag{3.6a}
\]

For the raw row (3.5), `p=1/(1408m)` gives at least
`3W/5632=Theta(W)` compatible raw actuators.  Thus the proved raw reservoir
is stronger than the `Theta(W/m)` bank needed by the Catalan leave, but
remains unprescribed and unguarded.

This extraction is deliberately task-blind and local.  It does not say that
the retained anchors are eligible for a prescribed defect leave, nor does it
include protected arbitrary-width upper witnesses, complete cap paths, or a
topology skeleton.  For a buffered atlas the needed extension is the row-
energy inequality

\[
 {1\over|P_e|}\sum_{p\in P_e}\deg_{\rm ext}(p)
                         \le K D_m m^3                             \tag{3.7}
\]

in the full eligible anchor family, including every protected upper, cap,
sink, and topology conflict.  Fixed `m^{-2}` thinning gives per-list average
`O(D_m m)` and Haxell works for `D_m=o(m)`.  The tunable theorem is stronger:
for guarded list size `alpha m^2`, taking

\[
                         p={\alpha\over64K D_m m}                 \tag{3.8}
\]

extracts `Omega(W/D_m)` compatible complete packets.  Thus even
`D_m=Theta(m)` would leave Catalan order `Omega(W/m)`, provided the full
protected energy (3.7) and prescribed-task eligibility are proved.

On the lean fixed-basis face of Theorem 2.4, the full-ticket energy simplifies:
endpoint-time equality removes every crossing-upper row, internal-union
dominance removes upper witness replacement, the common connector removes
topology choice, and the fixed matching `M_0` removes cap paths.  The only
compiler conflict is equality of the named deletion cells in `B`.  Thus the
remaining energy theorem concerns physical/internal-slot conflicts and the
task-to-distinct-`B` assignment, rather than global witness or alternating-
path tickets.

### 3.2 The one missing Route-B theorem

> **Prescribed-task protected-energy extraction theorem.**  For the actual
> extensive reachable leave, embed every prescribed task in an eligible
> positive-density source bank and extract a `Theta(W/m)`-scale reservoir of
> lean-exact packets relative to one common connector and one fixed
> trace-guarded compiler matching `M_0`, such that the remaining protected
> physical/internal row-energy bound (3.7) holds and packet deletion cells
> admit a distinct assignment inside the unused dual basis `B`; every list
> retains `Omega(m^2)` members; the density `p` leaves at least as many
> eligible anchors as prescribed tasks and satisfies
> `alpha m^2>=32pR`; and every Haxell transversal is compatible with the
> distinct-`B` assignment.  The pointwise weighted code (3.2) is a stronger
> sufficient certificate for the same degree conclusion, not an equivalent
> condition.

The raw `Theta(W/m)` extraction, weighted identity (3.1), Haxell implication,
and sharp quadratic counterexamples are proved.  What is missing is precisely
the passage from an existential raw reservoir to **prescribed-task
eligibility plus the lean endpoint-time/internal-dominance/common-connector/
fixed-basis interface and its residual row energy**.  On this face upper,
topology, and common cap are automatic; constructing the common face and the
distinct-`B` assignment is the remaining correlated theorem, not another
local C6 count.

## 4. Exact comparison

| feature | Route A: compound seams | Route B: dispersed leave |
|---|---|---|
| number of tasks | `H=O(Phi)+O(1)`, hence absolute on `Phi<=E` | may grow with `m` |
| selector input | per-other-list exclusion `O(mD)` | global external degree `O(mD)` |
| selector | greedy; Haxell optional | Haxell (or per-list-average pruning) |
| structural burden | bounded physical seam-event lift and exact collar compression | global weighted anchor/cap/topology dispersion |
| single missing theorem | guard-complete bounded-seam lift | prescribed-task protected-energy extraction |

For the same source-private C6 host, Route A is the bounded-bank special case
of Route B's local load calculation: only `O(1)` other anchors exist, so all
one-free and zero-free anchor counts are automatically `O(1)`.  Route B is
therefore genuinely weaker as an exposure/leave hypothesis.  Conversely,
Route A is weaker as a selector hypothesis: arbitrary verified per-list
exclusions suffice, without constructing a global weighted code or protected
average-energy reservoir.  Proving Route B for an extensive physical leave
is a global Hall/Rado/gammoid correlation problem which Route A avoids by
constructing only boundedly many tasks.  The routes are therefore
incomparable overall.

Neither route currently closes the contiguous-OR upper bound.  A proof of
either named missing theorem, together with the already stated terminal
physicalization, would turn the corresponding exact selector implication
into `nu(k)<=B(k)+O(1)`; without it the result remains conditional.

## 5. Dependencies

* `MATH_THEOREM_R_REACHABLE_COMPOUND_SEAM_COLLAR_GREEDY_INDUCTION_20260731.md`;
* `MATH_THEOREM_INDEPENDENT_REACHABLE_SPARSE_EXPOSURE_AND_ECO_SEAM_CHARGE_20260731.md`;
* `MATH_THEOREM_R_BUFFERED_C6_WEIGHTED_ANCHOR_AND_TOKEN_LOAD_20260731.md`;
* `MATH_THEOREM_SPARSE_C6_AVERAGE_LOAD_EXTRACTION_20260731.md`;
* `MATH_THEOREM_FULL_PREFIX_SUFFIX_UNION_BOUNDARY_SIGNATURE_20260731.md`;
* `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md`;
* `MATH_THEOREM_A_BUFFERED_HEX_UPPER_RAY_STAR_COVER_AND_S1_CALIBRATION_20260731.md`;
* `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`.
