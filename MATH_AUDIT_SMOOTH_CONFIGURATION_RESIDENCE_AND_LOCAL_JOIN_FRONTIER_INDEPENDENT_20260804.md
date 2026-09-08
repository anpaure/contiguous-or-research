# Independent audit: smooth configuration, residence, and localized joins

**Date:** 2026-08-04
**Audited synthesis:**
`MATH_SYNTHESIS_SMOOTH_CONFIGURATION_RESIDENCE_AND_LOCAL_JOIN_FRONTIER_20260804.md`
**Audited synthesis SHA-256:**
`54ff7075122a53374f3879ab93bf48450711562f6dcf997aff265d5a6f3b89ab`
**Method:** independent symbolic replay of every theorem used in the
synthesis, including the smooth configuration dual, all-scale ceiling
inequality, carry-aware knapsack/Bellman reduction, exact coagulation
reduction, three-pairing residence cover, the one-step and full-port router
theorems, the two-coordinate common-cap min-max, upper blocker theorem,
run-transparent square, the syndrome-quotient resident cube construction,
the two-adic whole-cell selector obstruction, complementary-age
cross-stratum collar, localized interface join, and the macro-resident
Hall/holonomy/switch-tree theorem.  The final re-audit also includes the
all-grid first-crossing/endpoint-saturation/Apéry theorem, both current
`n=4` efficiency-branch notes, the residue-carrying puncture theorem, and
the exact dicut/one-shore contained-cell obstruction.
No finite search, solver, or random experiment is used as evidence.

Final-rebase inputs for the newly added rows were frozen at:

| role | SHA-256 |
|---|---|
| all-grid first-crossing/Apéry theorem | `72e532231483e7d107ac103097a0507aea56afe09ca865dc743df153bdc597b1` |
| independent all-grid audit | `d404632e3bd805f92333276c74d3a094991da224f22259f11ba24193c0842173` |
| maximum-density lower-bound obstruction | `2a3bc8f4c0b2d444edc15c9720cf165d75a7855b13d4dd32e7741359c2c4cc1b` |
| complete two-efficient `n=4` theorem | `47819d25abf75877b6bc723ed593354bb0e76582635996227ac9c48812b986c8` |
| independent two-efficient audit | `20dcdbb21cd71ed2bacd6c637ff59ee23ffa2dec6ed1da61cf42f05af07d2fbb` |
| three-efficient `n=4` reduction | `b620128fdefd9063099a6e1032c1685d155ba9aa95bab96b0e49612c11987faf` |
| independent three-efficient audit | `d6c4448561ea344f48a8a53b171420047695e6d312f218371d51706102d47327` |
| residue-carrying puncture theorem | `bd0f567bcd91f09e6c40216d08c0463e7abbe495756392095e5839ea8d690fbd` |
| independent puncture audit | `8d1cad8e99ddefb7a9dd73e7bf56cd30fc3e00242383b1ff2c4ce5f0598e37f1` |
| exact dicut/one-shore theorem | `87ffe4d7e5d76f91676bfb9848d3f641b0586ce87049bfc1044b79043e164df1` |
| independent dicut audit | `7bf53c4c1ff017c1a2e30bd22daa713ca433223437f7d6efc561caec0fa78d21` |

## 0. Verdict

**PASS after proof-scope corrections incorporated into the synthesis.**

The synthesis is a conditional implication and obstruction ledger.  It
does not prove

\[
                    \nu(k)\le B(k)+O(1)
\]

or `nu(k)=B(k)` in all dimensions.  Its finite statement remains equality
through `k=16`.

The audited corrections were substantive quantifier clarifications rather
than changes to the component mathematics.

1. Continuum coagulation is the leading **primal analogue** of the finite
   binomial configuration problem, not an asserted finite-to-continuum
   equivalence.  No cone-closedness or converse rounding is assumed.
2. The five-capacity separator proves that mixed-denomination prices lie
   outside the concave-plus-ceiling cone.  It does not prove that a future
   separator must vary with dimension; a fixed macroscopic mixed pattern
   is still possible.
3. The `h+2` pairing redundancy statement is recorded for every fixed `h`,
   matching the proved quantifier.
4. The literal Boolean router now explicitly retains private gain prefixes,
   injective physical sink reservations, and type legality common to every
   gain incident with a port.
5. “Existing even taps” was replaced by the actual conditional requirement:
   materialized terminal-only even-tap certificates of bounded charge.
6. The final implication now requires one compatible selected odd spine and
   literal export of its next state.  Terminal tap and repair choices are
   not exported or accumulated.
7. The three-frame result is an exact cover of the owner set with overlaps,
   not a partition or an exactly-once cover.
8. The dense macro-Hamilton corollary is stated on the loopless seam graph;
   self-connectors may not be counted toward its `n/2` degree hypothesis.
9. The all-`a` ceiling inequality is distinguished from physical covering
   scope: `0<a<=A` supplies the primitive one-denomination rays, while
   `a>A` is an additional analytic test.
10. Enlarging from `(0,A)`-generated physical prices to all monotone
    subadditive clock prices is justified by the exact closure-domination
    lemma, rather than silently identifying the two pointwise classes.
11. The one-period residue bound is replaced by the exact carry-aware
    knapsack closure and finite Bellman equivalence.  The Bellman inequality
    itself remains open.
12. The one-step Boolean face closes its own suffix Hall problem, but does
    not eliminate the full active-port cut on a general parent-derived
    router.  The protected two-factor supplies only an abstract incidence
    factor.
13. Local resident good-cell chronologies exist explicitly, but whole-cell
    exact cover is arithmetically impossible at the required dimension.
    The global selector must use residue-carrying proper path blocks before
    macro Hamiltonization; the congruence alone does not force unequal
    block lengths.
14. The `n=4` two-slot-efficient branch is completely positive, but the
    three-slot-efficient note is still a reduction theorem.  Its exact
    remaining list includes the large-residue face `z>=A,u>2A/3` in
    addition to the two subcritical boundary surfaces and the five-pulse
    `w=2u` system.
15. The nested measurable-difference/dicut characterization is exact only
    in the all-available two-frame whole-block completion model.  The
    one-shore no-go concerns connected intervals assembled from whole cells
    of one other frame that are contained in the source cell; it is not a
    no-go for arbitrary punctured blocks or for the genuinely two-shore
    nested-difference target.

These changes remove the only passages that could otherwise be read as
smuggling a constant-additive existence theorem.

## 1. Gaussian rigidity and fixed additive charge

For `k=2r` and `A=sqrt(pi)/2`, telescoping the SCD start counts and applying
the central-binomial local limit gives the residual-job density

\[
             2(A+x)e^{-(A+x)^2}\,dx\quad(x>0)
\]

and the socket density

\[
             2(A-y)e^{-(A-y)^2}\,dy\quad(0<y<A).
\]

Their first moments agree because

\[
             A=\int_0^\infty e^{-z^2}\,dz.
\]

The anonymous threshold inequalities give tail domination of every weak
chunk limit by the socket measure.  Minimality of the coefficient-one depth
leaves only `o(W sqrt(r))` unused capacity, so the first moments agree in
the limit.  Integrating the nonnegative tail difference forces equality of
all positive tails; the `q=1` cut excludes an atom at zero.  Thus the unique
feasible chunk limit is the socket measure.

The minimum-piece intensity

\[
                 \sum_{n\ge1}e^{-\pi n^2/4}<0.501
\]

is strictly below the forced socket intensity

\[
                 1-e^{-\pi/4}>0.544.
\]

Hence every minimum-piece cutting fails by `Omega(W)` independently of cut
locations.  Balanced equal pieces also fail: near maximal capacity their
chunk mass is linear in collar width, whereas the socket tail is quadratic.

For `h=d+C` with fixed `C`, the exact vacancy is

\[
 \sigma_C=\sigma_0+CW+Cd+{C(C+1)\over2}=O(W)
          =o(W\sqrt r).
\]

Therefore the same weak limit and capacity-diagonal conclusion remain
forced.  This is a necessity theorem.  It does not construct a cutting,
configuration mixture, containment matching, or source chronology.

The source notes use opposite letters for the two measures in different
files: the Gaussian-rigidity note calls the job measure `nu` and socket
measure `mu`, while the configuration/coagulation notes call them `mu` and
`nu`.  The synthesis identifies the roles in words and makes no inference
from the swapped symbols.

## 2. Exact configuration dual and price classes

For a job of length `l`, a capacity multiplicity vector `p` is physically
usable exactly when

\[
             |p|\le l\le\sum_u u p_u.
\]

One unit is placed in every selected socket and the remaining units are
added one at a time, proving sufficiency.  Separation of the upper-closed
socket-usage polyhedron gives the exact fractional criterion

\[
 \sum_l n_l\psi_\theta(l)\le\sum_um_u\theta_u
 \quad(\theta\ge0),
 \qquad
 \psi_\theta(l)=\min_{p\in\mathcal Q_l}\theta\cdot p.
\]

Replacing `theta_u` by its covering closure leaves `psi_theta` unchanged
and lowers the supply price.  The resulting price functions are precisely
the nonnegative, nondecreasing, subadditive finite covering prices.  This
excludes parity artefacts created by an equality-only coin equation, but it
does not make the configuration matrix integral.

The signed Gaussian tail kernel has zero integral and one sign change.
Weighting it by the decreasing derivative of an increasing concave price
gives the correct nonnegative socket-minus-job margin.  Thus every such
concave price passes.

For every real `a>0`, layer-cake gives

\[
 J(a)=\sum_{n\ge0}e^{-(A+na)^2},
 \qquad
 S(a)=\sum_{0\le na<A}\left(1-e^{-(A-na)^2}\right).
\]

The Fourier estimate for `a<=4A/5` and the direct Gaussian-tail estimate
for `a>=4A/5` prove `J(a)<S(a)` with no uncovered range.  Therefore every
fixed continuum one-scale ceiling function passes strictly.  In the
physical covering dual, `0<a<=A` is the primitive range, with only a
zero-measure endpoint convention at positive multiples of `A`.  If `a>A`,
the socket price is constant one and closes to the `a=A` minimum-piece ray
up to that convention, so the extra analytic functions are not extra
physical MIR rays.  The pointwise result also does not by itself supply a
uniform finite-dimensional estimate for an arbitrarily dimension-varying
denomination.

The finite price `(1,2,2,2,3)` is a valid monotone-subadditive covering
closure.  The functional

\[
             2f(1)-2f(2)+2f(4)-f(5)
\]

is nonnegative on every increasing concave price and every ceiling ray,
but equals `-1` on this table.  This proves non-generation of the physical
price cone.  It does not show that this table, or any fixed rescaling of it,
actually separates the Rayleigh measures.

The abstract whole-job examples correctly show that scalar capacity,
majorization, receiving threshold cuts, and even a uniform one-unit socket
increase are not generic configuration-rounding theorems.  They are not
binomial-profile no-go examples.

### Anchored-window and superadditive-clock reduction

For a monotone right-continuous price `f` with `f(0)=0`, put `rho=df` and
include the initial atom `rho({0})=f(0+)`.  Then

\[
 \rho((x,x+t])=f(x+t)-f(x),\qquad
 \rho([0,t])=f(t).
\]

Therefore the complete family

\[
                 \rho((x,x+t])\le\rho([0,t])
\]

is exactly subadditivity, not a relaxation.  Stieltjes layer cake gives the
socket-minus-job price margin `int K d rho`; Gaussian continuity removes
all endpoint ambiguity.

Although physical sockets lie only in `(0,A)`, testing all monotone
subadditive functions is still equivalent to testing all physical covering
closures.  The `(0,A)`-generated closure of any such `f` agrees with `f` on
the socket support and dominates it on the job support.  Thus positivity
for physical closures implies positivity for the enlarged test function,
and the reverse implication is immediate.

The generalized inverse

\[
 a_f(u)=\sup\{x:f(x)\le u\}
\]

is nondecreasing and superadditive.  Conversely, the inverse of every
nondecreasing superadditive clock is a monotone subadditive price, up to the
irrelevant flat/jump convention.  Ordinary layer cake then gives

\[
             \int f\,d(\text{socket}-\text{job})
             =\int_0^\infty K(a_f(u))\,du.
\]

Thus the universal continuum dual is exactly positivity on the complete
superadditive-clock cone.  Integer-valued prices give nondecreasing
superadditive jump positions; arithmetic positions reproduce ceiling rays,
and no arithmetic-cone generation is assumed.

### Carry-aware knapsack and Bellman reduction

Let `b` be the restriction of a clock to `[0,1]`, with `b(1)>=A`, and set

\[
 (\mathsf Sb)(t)=\sup\left\{\sum_i b(r_i):
               0\le r_i\le1,\ \sum_i r_i\le t\right\}.
\]

Concatenation proves superadditivity, and internal superadditivity of `b`
shows that this closure agrees with `b` on `[0,1]`.  Every global extension
dominates every feasible list, so `mathsf S b` is the least extension.  On
the tail both it and every other extension are at least `A`, where `K` is
increasing.  Therefore the exact infimum at fixed `b` is

\[
 \mathcal J(b)=\int_0^1K(b(t))\,dt+
               \int_1^\infty K((\mathsf Sb)(t))\,dt.
\]

The normalization also covers extended-valued clocks.  If finite values
before blow-up are unbounded, normalize before the blow-up.  If they are
bounded by `L`, replace only the blow-up endpoint by
`T>=max(A,2L)`.  This preserves internal superadditivity; the resulting
tail is dominated by the summable clock `floor(t)T` and tends to zero as
`T` tends to infinity.  No invalid truncation `min(a,T)` is used.

For the lower grid approximation `b_n`, a value `c_j` consumes minimum
capacity `j/n`.  Thus its closure is exactly the integer unbounded-knapsack
recurrence

\[
 V_0=0,
 \qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j}),
\]

and

\[
                    \mathcal J(b_n)={1\over n}
                    \sum_{m\ge0}K(V_m).
\]

Because `b_n<=b`, the closures satisfy `mathsf S b_n<=mathsf S b`.
Tail monotonicity and dominated convergence on the compact period give
`limsup J(b_n)<=J(b)`.  Consequently universal clock positivity is
equivalent to nonnegativity of the displayed Bellman sum for every finite
nondecreasing internally superadditive table.  This direction does not
assume convergence of the knapsack closures.

The formerly negative half-step pair is repaired by carry:
superadditivity forces endpoint value `2A`, the least clock is
`A floor(2t)`, and its all-ceiling sum is positive.  Conversely,
denomination insertion is not monotone: inserting the undominated value
`A/2` into `(0,0,A)` changes `2C(A)` to the smaller, still positive,
`C(A/2)`.  Only dominated insertions `c<=V_j` are inert.  Hence the exact
finite Bellman inequality, not the residue-pair estimate, is the open
analytic gate.

The complete `n=2` case also replays.  Internal superadditivity is exactly
`T>=2y`, yielding even values `qT` and odd values `qT+y`.  The Bellman sum
is nondecreasing in `T`.  For `y>=A/2`, its minimum is the positive
arithmetic clock of step `y`.  For `y<=A/2`, at every interior critical
point the decreasing logarithmic derivative
`lambda(z)=1/z-2z` gives

\[
 {1\over2}F_A''(y)
 \le2A\left((A^2-y^2)^{-1}-2\right)\phi(A-y)<0.
\]

Hence every interior critical point is a strict maximum and an endpoint
minimizes; the endpoints are `2C(A)` and `C(A/2)`.  Both are positive by
the all-ceiling theorem.  Any countertable therefore has grid size at least
three, not merely more than one denomination.

The `n=3` recurrence has also been replayed.  For `(0,x,y,T)`, internal
superadditivity gives `y>=2x` and
`T>=x+y`.  When `2T<=3y`, exchange of size-one/size-two/size-three
generators leaves only a two-coset period-`y` normal form with one initial
transient.  When `3y<=2T`, it leaves the exact three-coset period-`T`
normal form, again with one initial transient.  The formulas agree at
`2T=3y`.

In the subcritical first regime, `T>=A` forces
`2A/3<=y<A` and the shift `z=T-y` lies in `[A-y,y/2]`.  The kernel is
decreasing on `[0,A/2]`, so the transient `K(x)-K(z)` is nonnegative.  The
same logarithmic-derivative argument makes every interior shift-critical
point a strict maximum.  Hence the minimum occurs at `z=A-y` or `z=y/2`,
reducing the row to

\[
 \mathcal H(y)=\sum_{q\ge0}
   \bigl(K(qy)+K(qy+A-y)\bigr)
 \quad\hbox{or}\quad C(y/2).
\]

The latter is positive.  The scalar `H` is now positive on its complete
interval as well.  Its four head Gaussians are a subset of

\[
 \Theta(t)=\sum_{j\in\mathbb Z}e^{-A^2(t-j)^2}
 \le2+4\sum_{m\ge1}e^{-4\pi m^2}.
\]

The two omitted negative tails are maximized at `t=2/3`; their successive
ratios are at most `e^{-8pi/9}` and `e^{-pi}`.  The elementary bounds in
the source give

\[
 \mathcal H(P)>{1\over28}-{1\over20000}-{1\over36}>0.
\]

The head expansion and both tail indices have been checked independently;
there is no omitted or duplicated Gaussian.  Thus all regime-I tables with
`y<A` pass.  If `y>=A`, the regime-I normal form is bounded below by the
two-slot Bellman sum for `(0,x,y)`: replacing its shift `z>=x` by `x` can
only enlarge the negative Gaussian tail.  The two-slot theorem therefore
closes the rest of regime I.

The regime-II closure has also been independently replayed.  Monotonicity
in the period reduces the boundary `y>=2A/3` to an arithmetic clock plus a
nonnegative transient.  For `y<=2A/3`, it reduces to

\[
 C(A)+F_A(z)+F_A(y),
 \qquad0\le z\le y/2,
 \quad0\le y\le2A/3.
\]

The logarithmic-derivative calculation makes every interior critical point
of `F_A(z)` a strict maximum, leaving the two endpoint rows.  The separate
triangle theorem completes each shifted Gaussian row to the full Jacobi
lattice.  Its theta identity has the correct omitted shores, its
two-Gaussian envelope has no interior minimum, and the rational estimates
give uniform margins

\[
 J_1>{397\over20000},
 \qquad
 J_2>{117\over20000}.
\]

Thus every `n=3` Bellman table passes strictly.  A finite countertable, if
one exists, has grid size at least four.  This still does not establish the
universal all-grid Bellman inequality.

### All-grid first crossing, saturation, and Apéry tails

The all-grid normalization in the synthesis is exact.  If `N` is the first
displayed index with `c_N>=A`, deleting all later denominations leaves the
Bellman clock unchanged through `N`, lowers it afterward, and still keeps it
at least `A` there.  Since `K` is increasing on `[A,infinity)`, the
functional can only decrease.  This is prefix deletion in the monotone
tail, not insertion monotonicity.

For a first-crossing endpoint `n`, let `P_n` be the exact best capacity-`n`
configuration using only lower denominations.  Replacing `c_n` by
`max(A,P_n)` preserves every internal superadditivity inequality and again
can only lower the tail functional.  If `P_n>=A`, the endpoint is genuinely
Bellman-inert, because every use can be replaced by an attaining lower
configuration.  The synthesis correctly retains the caveat that this
endpoint cannot simply be deleted while preserving a **displayed** first
crossing: all remaining generator values may be below `A` even though their
Bellman closure eventually crosses it.

For the reduced weights

\[
 d_j=c_j-j\lambda,
 \qquad\lambda=\max_j c_j/j,
\]

critical denominations have weight zero and all noncritical edges have
strictly negative weight.  Deleting repeated-vertex segments makes every
optimal residue walk simple, so its witness uses at most `g-1` noncritical
steps, where `g` is the gcd of the critical capacities.  The normalized
critical semigroup has the elementary conductor used in the source.  Exact
padding then gives

\[
 V_m=\lambda m+\beta_{m\bmod g}
 \qquad(m\ge n(n-1)).
\]

Thus the finite-head plus at most `g` shifted Gaussian lattices in the
synthesis are exact.  This does not sign the finite head or bound `n`.
The explicit table `(0,15A/16,2A,3A)` also verifies the stated warning:
its Bellman functional is strictly **below** the arithmetic clock at its
maximum density, so no single-density-lattice lower bound may discard the
head.

### Current `n=4` status

The complete two-slot-efficient branch has been independently audited.  Its
periodized Rayleigh derivative has the claimed sign through period `4A/5`;
above that threshold every interior critical point reduces to the exact
three-Gaussian strongly convex inequality.  Every rational cell and
critical-point certificate is strict.  Hence this entire branch is proved
positive, not merely reduced.

The three-slot-efficient note has a different status.  The split
`w=max(y,2u)` gives two overlapping faces:

* on `w=y`, one has `v=y`, so only the finite transient
  `sigma([x,u))` remains outside the effective three-coset clock (it lies
  wholly in the compact monotonicity range only on the corresponding
  bounded-`u` subfaces);
* on `w=2u`, the exact formula has the three finite transient pulses plus
  the two uniform-lattice comparison pulses, with occurrence multiplicity
  retained.  This is exactly five pulses, including the adverse tail pulse.

The kernel monotonicity interval and both normalized positive subfaces are
valid.  In the subcritical `w=y` domain, the effective three-coset sum is
strictly increasing in the period.  The exact rational `rho` certificate
and all endpoint derivative inequalities have been independently replayed,
so reduction to `P+u=A` and `P+u=2y` is sound.

Complete positivity of this branch is **not** proved.  Its remaining list
is

\[
 \boxed{
 \begin{gathered}
 P+u=A,\qquad P+u=2y,\\
 z\ge A,\ u>2A/3,\\
 \text{the residual five-pulse `w=2u` system.}
 \end{gathered}}
\]

The synthesis was corrected to include the middle large-residue face.  The
four-state Apéry branch remains a separate open `n=4` branch, so the
universal four-slot theorem is not claimed.

## 3. Exact continuum coagulation scope

The job and socket measures have equal total work.  If a fractional
fragmentation kernel assigns loads `z_i<=y_i` to sockets, then

\[
 \int\sum_i(y_i-z_i)\,d\rho
 =\int y\,d\nu-\int x\,d\mu=0.
\]

The integrand is nonnegative, so every used socket is full almost
everywhere.  A feasible continuum kernel is therefore exactly a finite
coagulation measure: socket capacities are grouped into finite multisets
whose sums have the job marginal.  Finiteness follows because the aggregate
piece intensity is finite.

The equivalent centered-Rayleigh identity is

\[
          z+\sum_{i=1}^nw_i=(n+1)A,
\]

with one point `z>A` and the remaining points `w_i<A`.  Thus every block has
arithmetic mean `A`.  The unavoidable group-count tails are intensity
statements,

\[
          \rho_0\{N\ge n\}\ge e^{-\pi n^2/4},
\]

not probabilities under a separately normalized law.  Their sum is
strictly below the available socket intensity, so raw group count does not
separate the measures.

No coagulation kernel is constructed.  Conversely, the stated dual price
inequalities are only asserted necessary; their analytic sufficiency would
need a closedness/tightness proof.  This justifies the synthesis's corrected
“primal analogue” language.

## 4. Residence: local switches and frame selectors

### Explicit chronology inside every sufficiently large good cell

The syndrome-quotient construction independently replays.  For a power of
two `h>=4L`, the partial sums of the `1,...,h,1,...,h` isometric cycle map
bijectively to the syndrome space.  Kernel translates therefore resolve
`Q_h` into disjoint `2h`-cycles.  Equal-column classes give the direct sum
of even-parity spaces, and weight-two differences from spanning trees in
those classes form a kernel basis with cyclic separation at least `h/4`.
The four-point class proves that `1/4` is sharp for this basis method.

Kernel differences yield directed square switches.  A parity translation
by one fixed active direction on the odd inactive shore converts every
inactive-coordinate adjacency into the same directed square template; a
naive product without this twist has parallel cut edges.  The two equally
oriented seam collars form a punctured interval of length `2L-2<h`, so no
unpriced repeated direction is hidden in the local switch.

The component quotient is a cube.  Along one quotient Hamilton path,
choose the antipodal occurrence bit recursively; this is a flat gauge, not
a reflected or cyclic holonomy assumption.  Every old component carrying
two switches then has ports at distance at least `h/2`, and the switch tree
merges all components while preserving `L`-residence.  Thus every pair cell
of dimension at least the least power of two `h>=4L` has an explicit
resident Hamilton chronology.

This theorem does not give equal-support critical collars and does not
choose among overlapping good cells.  It closes only the local good-cell
chronology; the global owner/cell selector remains.

For a same-dimensional pair-cell transfer, the two seam supports are

\[
                \{p^1,q^1\},\qquad\{p^0,q^0\}.
\]

They use opposite physical members.  Opening coherently relabelled copies
of a `rho`-run cube cycle and switching across this square merges two cycles
while reducing transition separation by at most one.  Because a matching
uses each cell at most once, these switches compose without an unpriced
multiport interaction.

For a cross-stratum `m` to `m+2` square, the seams reuse the same physical
members and the two new directions are active in the larger cube.  If a
common direction appears at inward transition-slot ages `i,j` on the two
sides of a seam, the two slots are exactly `i+j` apart.  Thus its necessary
and sufficient local safety inequality is

\[
                              i+j\ge L.
\]

The former disjoint-collar condition was sufficient but not sharp.  For one
seam, reverse the age order `i -> L-i`; `m>=L` supplies the `L-1` collar
labels and one fixed cut label.  For both seams, exclude the exceptional
large-cube directions `p,q` from both endpoint collars and form the
bipartite graph joining a small direction to a large direction exactly when
both endpoint age sums are at least `L`.  One common relabelling exists if
and only if this graph has a perfect matching for one endpoint pairing.

Every vertex has at most `L-2` forbidden neighbours.  Therefore arbitrary
endpoint histories are automatically matchable after choosing `p,q` in the
worst-case range `m>=2L-1`.  At the critical `m>=L` scale, equal support of
the two endpoint collars in each cube is already sufficient: old residence
forces the two ages of each supported direction to sum exactly to `L`, and
the complementary-age matching works at both seams.  What remains is to
plant or regenerate this balanced-support pattern.  The Johnson triangle
calculation still shows why the naive `Q_0` or `Q_1` ear has run one.

For one uniformly random perfect coordinate pairing, the exact law of the
singleton-pair dimension gives

\[
 \Pr\{X_P(T)<M\}=2^{-r+O(M\log r+\log r)}.
\]

With `M=L+ceil(3 log_2 r)` and `L=O(sqrt(r))`, three independent pairings
and a union bound over at most `4^r` owners give an exact three-frame owner
cover.  More generally, the theorem's fixed-parameter quantifier gives
`h+2` frames with at least `h` good choices per owner for every fixed `h`.

### All-perfect-pairings Hall corollary

There is a further exact consequence, now incorporated into the residence
theorem.  Take all perfect pairings of `[2r]`, and orient one long-run cycle
in every good cell.  For an owner `T`, let

\[
                 a(T)=\#\{P:X_P(T)\ge M\}.
\]

The action of `S_(2r)` is transitive on middle owners and bijective on
perfect pairings, while preserving `X_P(T)`.  Hence `a(T)=a` is constant.
It is positive when `M<=r`, since a perfect matching from `T` to its
complement has `X_P(T)=r`.

Each good frame containing `T` contributes one outgoing and one incoming
successor occurrence.  Therefore the all-frame successor-occurrence
bipartite multigraph is `a`-regular.  It has a perfect matching and hence a
directed spanning permutation cover.

The word **multigraph** and the occurrence labels are essential: several
frames may supply the same Boolean arc.  The conclusion closes only
ordinary successor Hall.  The selected permutation can switch frames at
every vertex, reuse a transition coordinate inside `L` steps, or contain an
antiparallel two-cycle.  It is not yet a resident simple 2-factor.

The two-triangles-sharing-one-vertex example independently confirms that
owner coverage, even with two active frames per owner, does not imply a
spanning 2-factor.

### Whole-cell selector obstruction

The stronger literal obstruction is two-adic.  A dimension-`m` pair cell
has exactly `2^m` owners, while Legendre's formula gives

\[
                \nu_2\binom{2r}{r}=s_2(r).
\]

Therefore any partition of the owner layer into whole pair cells of
dimension at least `M` forces `M<=s_2(r)`.  Since
`s_2(r)<=floor(log_2 r)+1`, this is impossible at the
`M=Theta(sqrt(r))` residence scale, for any number of pairing frames.  The
all-pairings fixed-`m` hypergraph still has a uniform fractional exact cover
by symmetry, so the failure is genuinely integral.

The count is not sufficient below its obstruction range.  At `r=2`, the
three perfect pairings of four coordinates supply three dimension-two good
cells; every owner lies in exactly two, and the three exact-cover row types
force the unique real solution `(1/2,1/2,1/2)`.  No binary selector exists
even though `M=s_2(r)`.  Every available cell in that example actually has
size four, so the same failure is visible modulo four; the example shows
that the coarse minimum-threshold inequality is insufficient, not an
incidence obstruction independent of exact-size congruence.

For two fixed partition frames, the exact criterion also replays: in each
component of the block-intersection bipartite graph, all variables on one
shore equal one bit and the other shore its complement.  Selection fails
exactly when a component contains an unavailable block on both shores.
For three frames, first choose the selected blocks on the third shore and
delete their union.  A residual block on either remaining shore is
forbidden if its original block was unavailable or met the deleted union.
The two-frame component criterion then applies verbatim, and conversely
every resulting residual selection lifts to full original blocks disjoint
from the third-shore choice.  This is an exact component-separator
reduction, not an asserted efficient algorithm.

Hence whole-cell exact cover is not a viable global selector.  If proper
resident path blocks have sizes `b_j`, their sum must carry
`binom(2r,r)` modulo `2^M`; at least one has two-adic valuation at most
`s_2(r)`.  This does not bound the number of cuts or force unequal block
lengths; a common length of sufficiently low valuation is not excluded.
It proves only that at least one residue-carrying proper block is necessary.
A switch-only tree preserves every owner degree and multiplicity in its
fixed edge union and therefore cannot repair an overlapping or incomplete
whole-cell family.  It can Hamiltonize after the owner partition is fixed;
the theorem also does not obstruct a broader move which changes the
selected blocks as well as switching edges.

### Residue-carrying punctures and exact dicut scope

Let `q_M=2^M`, with `M>s_2(r)`, and

\[
 \omega=\binom{2r}{r}\bmod q_M.
\]

Then `nu_2(omega)=s_2(r)`.  If `q_M>=2D` and a source cell has dimension
`m>=M+1`, one of the two values `omega` and `omega+q_M` lies between `D`
and `2^m-D`.  **Conditional on the source cell carrying a cyclic
`D`-resident Hamilton ordering**, the corresponding interval and its
complement are internally resident paths with at least `D` vertices.  The
conditional phrase is essential: the puncture theorem supplies arithmetic
length freedom, not the local cycle by itself.

For arbitrary preselected pieces `U` in a third partition, extension by
whole available blocks from two other partitions is equivalent to the
following exact component condition.  Delete the owner edges labelled by
`U` in their block-intersection graph; a surviving residual block is
forbidden if it was unavailable or if its original block met `U`.  No
residual component may contain a forbidden vertex on both shores.  Blocks
swallowed entirely by `U` disappear, which is why the stronger multicut
statement requires the separate survival hypothesis in the puncture
theorem.  If additional third-shore whole blocks are selected, that
multicut statement concerns the **full** preselected set `U`, not the
residue interval alone.

When both completion shores are wholly available, the component condition
has the exact global form

\[
 U=B\setminus A,
 \qquad A\text{ `P`-measurable},
 \quad B\text{ `Q`-measurable},
 \quad A\subseteq B.
\]

Equivalently, the labelled owner edges `U` are exactly a one-way dicut.
This characterization is not asserted for unavailable-block instances
without modifying the statement.

The one-shore obstruction has an equally precise boundary.  If a connected
cyclic interval inside one `R`-cell is a union of whole `Q`-cells **each
contained in that source cell**, then it is one `Q`-cell and has power-of-two
size.  Residue congruence forces the unique possible size
`2^{s_2(r)}`.  Under `D>=3` and `s_2(r)<D`, that cell is either smaller than
the `D`-vertex macro threshold or cannot carry a `D`-resident Hamilton
path.  This rules out the contained-cell one-shore Gray-prefix route; it
does not rule out punctured cells, cells not contained in the source cell,
or the genuine two-shore nested-difference construction.

Accordingly, the synthesis was narrowed from an unqualified “one-shore
no-go” to the exact all-available/contained-cell scope.  No existence of a
resident nested difference, macro Hall matching, or collar holonomy follows
from these cut theorems.

### Macro Hall, holonomy, and switch trees

The macro-block theorem supplies the correct memory scale.  Let the owner
layer be partitioned into internally `L`-resident directed paths with at
least `L-1` internal edges.  A perfect matching in the bipartite graph of
literal seam-safe block connectors selects one successor and one predecessor
for every block.  Between two transitions at distance below `L` there can
then be at most one new connector: they are either internal to one old block
or lie in one certified seam collar.  Thus macro Hall is necessary and
sufficient for a spanning resident cycle factor on the declared block
family.  Regularity at this **block** level is sufficient.

The dense Hamilton corollary is valid after self-connectors are discarded.
This loopless qualifier was inserted during this audit.  Without it, two
vertices carrying only self-loops would satisfy the `n/2` degree row at
`n=2` but would not have a Hamilton two-cycle.  In the loopless graph,
minimum in- and out-degree at least `n/2` forces strong connectivity and
Ghouila-Houri's degree theorem gives a directed Hamilton cycle of blocks.

Balanced endpoint collars carry a complete age phase.  If seam `i->j`
transports phase by a bijection `tau_ij`, a chosen block cycle is globally
consistent exactly when the cyclic product of its transports has a fixed
point.  Under a flat gauge

\[
                         \tau_{ij}=g_jg_i^{-1},
\]

the product telescopes to the identity, so every base cycle lifts.  This is
an exact global row missing from ordinary Hall.

The alternative switch-tree theorem is also exact.  Starting from a literal
resident cycle factor, a spanning tree of two-cycle switches merges all
components.  Residence survives when deleted ports are distinct, every old
path between consecutive new seams has at least `L-1` transitions, and each
new seam collar is resident.  Individual switch safety without this global
separation is not sufficient.

Finally, owner-level regularity cannot replace either package.  For every
multiplicity `a`, parallel occurrences of the two orientations of one
physical Johnson edge make a regular successor multigraph whose only
perfect matching projects to the nonresident antiparallel two-cycle.

## 5. Upper occurrence selection

A fixed directed edge lies in exactly `q` cyclic `q`-edge intervals.  Thus
a q1 colour of multiplicity `mu_R` enters at most

\[
                 \mu_R\left({m(m-1)\over2}-1\right)
\]

higher-target event scopes.  Under the declared bounded multiplicity,
pairwise random-scope-disjoint witness menus, and bounded repeated-colour
load, the target failure probabilities are inverse-polynomial after
`Theta(log m)` witnesses, while the variable dependency degree is only
`O(m^2 log m)`.  The symmetric local-lemma condition is therefore correct
inside this host class.

The fixed-width budget

\[
                 N_q+(t-1)V_q\le W
\]

is exact.  At q2 it yields

\[
 {V_2\over N_2}\le
 {6m\over(m-1)(m-2)(t-1)}.
\]

Thus logarithmic redundancy is possible only on an
`O(1/(m log m))` q2 leave; almost every low-width target must instead be
deterministic-safe.

The Boolean six-cycle has one repeated q1 colour and two unique admissible
q2 witnesses which force its two different occurrences.  It proves that
separate target feasibility and automatic cycle breaking do not imply one
common occurrence section.  It is a component-level obstruction, not a
spanning-factor no-go.

## 6. Small Boolean router, full-port scope, and local co-instantiation

Distinct rank-`s` ports have upper-shadow intersection at most one.  Hence
for a port subset `X`,

\[
 |N(X)\setminus F|
 \ge |X|L-{|X|\choose2}-|F|.
\]

The right side is at least `|X|` whenever `|P|<=L` and `|F|<=L-1`; checking
the two endpoints of the concave quadratic proves every Hall cut.  This is
an exact one-step Boolean suffix router.

The occurrence lift still requires all of the following in one fixed cap
state:

* distinct physical ports carrying distinct Boolean values;
* one injectively reserved physical occurrence for every eligible sink
  value;
* terminal type legality common to every gain incident with a port;
* private gain-to-port prefix interiors; and
* deletion of every unavailable or occupied sink value into `F` before the
  cardinality bound is checked.

Under these hypotheses, the regular incidence weighting gives a feasible
fractional flow and max-flow integrality gives the literal routes.  The
router theorem does not produce its ports, prefixes, sink reservations, or
common cap state.

The general factor-router statement has been independently replayed.  For
a left-`h`-regular/right-at-most-`h` incidence factor, send `1/h` along
every private claim-prefix/port-suffix concatenation.  Every claim emits one
unit and every port and suffix carries at most one.  Integral max flow then
links all claims, provided the suffixes form one simultaneous typed linkage
to distinct unused sinks in the same materialized state.  The Middle Levels
protected-factor theorem at `h=2` supplies only the abstract factor.

After deleting the fixed compensation linkage and prefix interiors, the
clean sufficient general certificate is

\[
                   r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|.
\]

Menger identifies this with every active-port all-cut inequality.  The
current parent/reference matching does not derive this rank, a physical
capacity-faithful port map, or the private prefixes.  A common unit suffix
bottleneck leaves the abstract factor and reference matching exact while
creating deficiency `|P|-1`, so those marginal objects cannot imply the
router.

For two physical occurrence coordinates, after one complete cap state is
fixed and every shared cross-coordinate capacity is allocated, Rado and
Edmonds give

\[
 \delta=\max_{J_0\cap J_1=\varnothing}
 \bigl(|J_0|-r_{N_0}(A_0(J_0))
      +|J_1|-r_{N_1}(A_1(J_1))\bigr).
\]

This exact formula depends on global product closure: marginal complete
routes must combine into one legal physical bank.  It treats the two
physical occurrence coordinates of the union of the cross matchings, not
the two matchings themselves, and transported phase 1 remains theorem
input only.

For localized seam co-instantiation, fixing intersections with a bounded
coordinate footprint gives the exact product-binomial profile count.  A
tree of module join trees glued along complete shared-variable separators
is again a join tree.  A simultaneous separator certificate therefore
gives one common tuple, and injectivity of the physical seam occurrence map
removes at most `|E_lambda|` seams in profile `lambda`.  This proves

\[
          \sum_\lambda(n_\lambda-|E_\lambda|)_+
\]

accepted seams under the stated uniform profile hypotheses.

If the reduced module graph is one chordless cycle, a global tuple exists
exactly when the composed separator relation has a fixed point.  The
equality/equality/disequality triangle has full unary and pairwise support
but no fixed point.  Thus pairwise compatibility cannot replace the join
tree or an explicit cyclic fixed-point check.

## 7. Final implication audit

The final implication is now quantified correctly.  It assumes one
compatible selected odd spine.  At every level one materialized odd host
must simultaneously carry:

1. fractional and integral whole-job configurations, literal containment,
   and countdown serialization;
2. a punctured/spliced resident factor made from proper paths cut from the
   explicit good-cell chronologies, carrying the two-adic owner
   residue and satisfying critical-cell absorption, macro Hall, and collar
   holonomy or an equivalent separated switch-tree completion;
3. the hybrid all-width upper selector and component reserve;
4. a localized common seam certificate;
5. the literal one-step router interface, or the full typed active-port
   rank in both occurrence coordinates with product closure; and
6. final replay and bounded terminal charge.

It additionally assumes literal export of the next odd state and a
materialized terminal-only even tap of charge at most the same constant.
The even tap and terminal repairs are not exported.  The audited terminal
charge theorem then gives

\[
                    \nu(k)\le B(k)+C.
\]

Every item in this paragraph is an assumption of the final implication,
not an existence conclusion of the component theorems.  In particular,
the three-frame cover does not supply the required punctured selector, the
upper LLL does not construct its witness menus, the Boolean router does not
materialize its occurrence interface, and the local join theorem does not
construct a uniform separator certificate.

## 8. Exact remaining frontier

The proof-safe advances are:

* fixed additive slack leaves the forced Rayleigh lower geometry unchanged;
* scalar and Lorenz constraints reduce to the exact configuration/coagulation
  gate rather than solving it;
* concave and every fixed continuum single-scale ceiling price pass, while
  the full physical price cone reduces exactly to anchored-window measures,
  superadditive clocks, and a finite carry-aware Bellman inequality which
  remains unresolved; every grid of size at most three is now proved
  positive, the complete two-slot-efficient `n=4` branch is positive, and
  every finite table has an exact quadratic-head plus shifted-Apéry-tail
  representation; the remaining three-efficient and four-state `n=4`
  branches are not yet closed;
* sufficiently large good cells have an explicit syndrome-quotient
  resident Hamilton chronology, but the two-adic owner count rules out a
  whole-cell exact cover at the required scale; every global selector must
  use at least one residue-carrying proper path block, without an arithmetic
  requirement that all block lengths differ; one puncture has exact scalar
  residue freedom, but its extension is still the bilateral component
  separator problem;
* same-cell residence switches are run-transparent and cross-stratum
  switches have an exact complementary-age matching criterion, including a
  critical-scale balanced-support certificate; the remaining path blocks
  still require macro Hall plus holonomy or a separated switch tree; in the
  all-available completion model the puncture is exactly a two-shore nested
  measurable difference, while only the contained-cell one-shore route is
  ruled out at residence scale;
* the upper selector has a quantitative hybrid host theorem and a literal
  Boolean obstruction;
* a small distinct Boolean port bank has an exact one-step suffix router,
  while a general parent-derived port bank still requires the explicit
  full-rank all-cut certificate; and
* local co-instantiation is exact on a complete-separator join tree.

The two largest constructive gaps remain the smooth binomial
configuration-plus-literal-containment/countdown theorem and the
residue-carrying punctured-cell selector with phase-coherent balanced cuts,
an exceptional-cell buffer, and macro Hall/holonomy.  All modules must then
be co-instantiated on one compatible regenerative spine.  No component
result proves that intersection, so the all-dimensional constant-additive
conjecture remains open.
