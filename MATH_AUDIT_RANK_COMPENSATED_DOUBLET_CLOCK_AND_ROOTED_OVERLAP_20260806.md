# Audit of the rank-compensated doublet clock and rooted-overlap reduction

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_RANK_COMPENSATED_DOUBLET_CLOCK_AND_ROOTED_OVERLAP_REDUCTION_20260806.md`  
**Method:** independent replay of every weight, product-survival exponent,
collision-energy identity, and stated scope boundary; no computation or
search  
**Verdict:** **PASS AS A REDUCTION, NOT AS AN INTEGRAL PACKING THEOREM.**
The compensation, mixture drift, pair/cluster inflation, variance identity,
first collision-energy row, slot suppression, macroscopic same-base
suppression, and synchronized-chain lemma are valid under the displayed
central assumptions.  The private-split calculation closes the same-half
mixed-track entry average `(PC)` and its finite first-two-hit extension
`(FE3)`.  The exact future-overlap drift and killed-hazard reduction are
valid; the signed incidence-spread and residual hazard-error transfers are
still open.  The later joint-Lyapunov audit refutes the scalar spectral
shortcut and replaces it by the stopped Johnson-sector target `(JSEC)`.
Global queue-component connectivity is also not supplied.

## 1. Weight and rank replay

An `h`-doublet edge has

\[
 2d\quad\hbox{lowers},\qquad
 2h(d+1)\quad\hbox{owners},\qquad
 2\quad\hbox{slots}.
 \tag{1.1}
\]

Its non-slot rank is

\[
                         N_h=2d+2h(d+1).
 \tag{1.2}
\]

The fractional weight in the source gives lower load `lambda_h` from orbit
`h`.  Summing those loads over all `M` lowers and dividing by the `2d`
lower incidences per edge gives

\[
                         \Omega_h={\lambda_hM\over2d}.
 \tag{1.3}
\]

The coefficients sum to one and obey

\[
 2\lambda_2+3\lambda_3={\rho d\over d+1}.
 \tag{1.4}
\]

Thus all base mass and mean-multiplicity identities are exact.

## 2. Product compensation replay

Condition on a retained lower or owner root.  An incident edge needs
`N_h-1` other non-slots and two slots.  Multiplication by

\[
                         p^{-(N_h-1)}p_s^{-2}
 \tag{2.1}
\]

cancels their survival probability exactly.  Condition on a slot instead:
the remaining edge has `N_h` non-slots and one slot, leaving the factor
`p/p_s`.  For a conditioned tuple with `q` non-slots and `s` slots, the
remaining factor is

\[
                         p^{1-q}p_s^{-s}.
 \tag{2.2}
\]

Without conditioning, an entire edge leaves one factor `p`.  Hence the
residual total orbit masses are `p Omega_h`, so the `h` law is still
`lambda_h`.  Its expected owner consumption is

\[
 2(d+1)(2\lambda_2+3\lambda_3)=2\rho d.
 \tag{2.3}
\]

Division by `W=rho M` gives the same `2d/M` density decrement as the lower
shore.  The slot density after `n` steps is exactly

\[
 p_s=1-{2n\over kL}=1-\sigma(1-p),
 \tag{2.4}
\]

so the ceiling surplus is correctly isolated on the slot shore.

This confirms the principal new algebra.  In particular, using the
uncompensated restriction would multiply the `h=3`/`h=2` rate ratio by
`p^(2d+2)` and destroy the owner mixture.

## 3. Local-ratio replay

A conditioned non-slot pair obtains one residual factor `p^-1`; therefore

\[
                         \delta(p)=\delta_0/p.
 \tag{3.1}
\]

At `p>=c/d` and `delta_0=O(d^-3)`, this is `O(d^-2)`, safely below the
`gamma/d` stopped-clock threshold.

A marked cluster on `m` distinct owner carriers obtains `p^(1-m)`.  Thus a
base row `theta kappa^(m-1)` becomes

\[
                         \theta(\kappa/p)^{m-1}.
 \tag{3.2}
\]

The root factor `theta` is unchanged and the per-companion factor is at
most `O(d)kappa`.  Since `log(1/kappa)=Theta(d log d)`, this remains at the
required exponential companion scale.

The source now proves the base marked row for the complete orbit.  A root
unordered occurrence projects to a pointed occurrence of exact marginal
`1/[r(d+1)]`.  Each further same-half companion fixes one of at least `N_*`
remaining tail choices and has only constantly many copy roles; an
other-half companion pays the still smaller macroscopic-header atom.
Sequential exposure through size three gives `theta(C/N_*)^(m-1)`.

## 4. Variance and collision-energy replay

For two edges through a retained non-slot root, every common additional
non-slot is counted twice in the two separate survival probabilities but
once in their union, producing `p^-1`.  A common slot similarly produces
`p_s^-1`.  Hence

\[
 {\operatorname{Var}Y_v\over\ell(v)^2}
 ={1\over\ell(v)^2}\sum_{E,F\ni v}\omega_E\omega_F
 \bigl(p^{-m_N}p_s^{-m_S}-1\bigr).
 \tag{4.1}
\]

Expanding the two binomials and selecting the common resource tuple `Q`
turns the ordered edge-pair sum into

\[
                         d_\omega(\{v\}\cup Q)^2.
 \tag{4.2}
\]

This verifies the exact collision-energy identity.  It also verifies that
a worst-case `Delta_j` is stronger than necessary: the required quantity is
a sum of squared tuple codegrees weighted by the separator fugacity.

For one additional non-slot,

\[
 \sum_wd_\omega(v,w)^2
 \le\max_wd_\omega(v,w)
       \sum_wd_\omega(v,w)
 \le\delta_0(R_{\max}-1)\ell(v)^2.
 \tag{4.3}
\]

Multiplication by `p^-1-1=O(d)` gives `O(1/d)`.  If a tuple contains a
slot, one factor is at most `O(1/(kL))`; summing every remaining role gives
at worst

\[
 {1\over kL}\exp[O(d\log d)]
                         =\exp[-\Theta(d^2)].
 \tag{4.4}
\]

Thus the only unproved static row is the collision energy of tuples with at
least two additional non-slot resources and no shared slot.

## 5. The two largest apparent overlap traps

### 5.1 Same base doublet, different slots

Two augmented edges over one physical base doublet can have different slot
indices and still share every non-slot.  The `L^2` replication does not
suppress this after its weights are aggregated.  The source correctly
removes the trap by choosing the two headers at fixed linear Johnson
distance.

After one header and the port pair are fixed, the far header has
`exp[Theta(k)]` choices.  Therefore the aggregate squared atom of one base
doublet is `exp[-Theta(k)]`, whereas its separator fugacity costs only

\[
                         p^{-O(d)}=\exp[O(d\log d)].
 \tag{5.1}
\]

Because `k=Theta(d^2)`, the same-base contribution is exponentially small.
This argument relies on the explicit macroscopic-distance refinement; the
weaker condition `distance>2d` alone does not give the displayed entropy
without a constant audit.

The same separation also removes every cross-half intersection term.  A
resource in the partner macro is at Johnson distance `Theta(k)` from a
root-half resource, up to `O(d)` atomic changes.  Its stabilizer orbit has
`exp[Theta(k)]` elements.  Choosing one such resource in an intersection
tuple gives an `exp[-Theta(k)]` codegree factor, while summing all remaining
roles and fugacities costs only `exp[O(d log d)]`.  Thus the unresolved
collision energy is entirely contained in one constituent macro.

### 5.2 The last-two-owner fan

The `2h<=6` penultimate and terminal owners of one macro have the form

\[
 C_*+z_1,\ldots,C_*+z_{2h}.
 \tag{5.2}
\]

The third owner costs only one new coordinate after the core is known.  For
`s` further fixed fan owners after a root, the joint orbit has order

\[
                         r{k-r\choose s}.
 \tag{5.3}
\]

There are only constantly many fan-role subsets.  Squared-codegree energy
followed by fugacity `d^s` is therefore at most

\[
                         O(d^sk^{-(s+1)})=O(d^{-s-2}).
 \tag{5.4}
\]

Summing `1<=s<=2h-1` gives `O(d^-3)`.  For four or more fan owners a
maximum power hierarchy can fail by a power of `d`; the rooted squared
energy remains more than sufficient.  The fan refutes a naive sequential
two-new-coordinate proof but is not part of the residual overlap gap.

## 6. Synchronized-chain lemma replay

If two paths in the synchronized Boolean product share prescribed internal
levels with positive gaps `g_1,...,g_m`, one coordinate ordering pays

\[
                         \prod g_a!/n!,
 \tag{6.1}
\]

and the independent second ordering squares this probability.  The
composition sum satisfies

\[
 \sum_{g_1+\cdots+g_m=n}
 \left({\prod g_a!\over n!}\right)^2
 \le {4^{m-1}\over(n)_{m-1}^2}.
 \tag{6.2}
\]

The induction reduces to

\[
 \sum_{a=1}^Na!^2(N-a+1)!^2\le4N!^2,
 \tag{6.3}
\]

whose two endpoint terms contribute `2N!^2` and whose normalized interior
inverse-binomial tail is below two.  Consequently, for `z=O(n)`,

\[
 \mathbb E(1+z)^Z
 \le\sum_{q=0}^{n-1}{(4z)^q\over(n)_q^2}
 =1+O(1/n).
 \tag{6.4}
\]

Thus internal overlap of a fixed synchronized FIFO track is closed.  The
complete macro orbit projects with constant fibre onto the complete fresh
Johnson-path orbit on any specified lower or owner track.  Hence the
existing all-order fresh-path overlap polynomial closes every edge-pair
intersection confined to one track pair, including variable endpoint
fibres.

For a second track, one common state splits its private deletion/tail bank
into blocks on the two sides.  Unless that split is already forced, two
independent completions must choose the same `n`-set from a pool of
`Theta(d^2)` labels before further common states on that side are possible.
The one-coordinate chain moment obeys

\[
 G_n(z)\le\sum_{q=0}^{n-1}{(4z)^q\over(n)_q},
 \tag{6.5}
\]

so, for `z=O(d)`,

\[
                         {G_n(z)\over{Theta(d^2)\choose n}}
                         \le(C/d)^n.
 \tag{6.6}
\]

The backward and forward sides multiply, and there are at most three
additional private tracks.  If a lower/owner pair already forces the split,
its pair atom is `exp[-Theta(d log d)]` while all one-coordinate moments
cost only `exp[O(d)]`.  If two owner tracks force a visible `q`-split, the
distance-orbit atom is `O(d(q!)^2/[(r)_q(k-r)_q])`; after its
`(Cd/q)^q` chain moment and role sum it is `O(d^-4)` for `q>=2`.
The `q=1` case is exactly the closed last-two fan.  These checks validate
the mixed-track theorem and hence `(PC)`.

The separator-constant refinement `(ROc)` is also valid.  The dominant
single-track expression is
`(1+C d k^-2(p^-1-1))^(d+O(1))-1=O(1/(pd^2))` when
`k=Theta(d^2)`.  The sharp first energy and mixed-entry contribution are
only `O(1/(pd^4))`, as is the leading fan term, and all rigid/cross-half/slot
terms are negligible.  Thus at `p=c/d` the variance constant gains the
useful factor `1/c`.

## 7. Dynamic and cylinder scope

The main-term drift calculation is valid: rate rescaling contributes
`(N_h-1)(2d)/(Mp)` per non-slot summand, while collision with the other
non-slot resources contributes the same amount when their compensated loads
are one and total rate is `pM/(2d)`.  The two slot terms cancel against the
derivative of `p_s^-2` using slot load `sigma p/p_s`.

More generally, a `q`-non-slot-root load is compensated as
`H_Q=p^(q-1)Y_Q`.  A summand then has exponent `N_h-q`, exactly the number
of its other non-slot collision resources.  This verifies that the pair
process relevant below is `pY_(v,w)`, not the raw pair load.

The global reconstruction proposition is exact.  For each orbit `h`, every
available edge contributes its rate to exactly `2d` live lower-root loads,
so

\[
                         2dX_h=\sum_{v\ {\rm live}}Y_v^{(h)}.
 \tag{7.0}
\]

There are exactly `pM` live lowers after the prescribed number of accepted
doublets.  Cauchy--Schwarz therefore converts an orbit-resolved maximal
root budget `O(M/d)` into relative global-rate error
`O((pd)^(-1/2))`, hence `O(c^(-1/2))` at `p=c/d`.  Choosing the fixed
constant `c` large enough and stopping provisionally at the first global
failure gives a valid positive-probability bootstrap.  This removes the
need for a separate uniform-degree or global-rate theorem, conditional on
the still-open orbit-resolved `(DROOT)` estimate.  For this implication the
root process must be stopped only at its hit or at the provisional global
bootstrap stop, not at its individual bad time; the source now makes this
distinction.  Pair processes may still stop at individual bad times because
their denominator is then charged to `B_0`.

This cancellation does not prove concentration.  A proof must still show
that the global rate survives to `p=Theta(1/d)`, that the aggregate number
of owner roots which become individually bad before their first hit is
`O(M/d)` in expectation, and that the unselected stopped pair square energy
has order `M/d^2`.

The analytical-bad-root formulation is proof-safe.  It does not alter the
clock process and hence causes no deletion cascade.  The first-hit cylinder
is applied directly to the event that every prescribed root is served
before its own bad time; a bad branch has payoff zero, so no additive bad
probability contaminates an order-`Theta(d)` cylinder.  Post-run pruning is
monotone.

The selected-relation refinement is also sound when proved as a
killed-event induction.  At a raw state where a required row has failed,
the desired retained-cylinder event has payoff zero because future
quarantine will remove an endpoint.  At every state with nonzero payoff,
the ordinary raw-clock cause ratios apply.  One must test all compatible
marked blocks of the sizes used by the cylinder.  The scale
`E(B_0+B_1)=O(M/d^2)` is sufficient because one deleted doublet releases
`2d` lower resources; little-oh merely supplies extra separator slack.

The revised stopped square-energy reduction has the correct scale and
removes a selection-bias ambiguity.  Stop a pair before the first hit or
before either endpoint becomes individually bad, and set

\[
 Z^g_{v,w}=\sup
 \left({Y_{v,w}\over\min(Y_v,Y_w)}\right)^2.
 \tag{7.1}
\]

A bad relation between two non-quarantined selected blocks requires both
`Z^g_(v,w)>(gamma/d)^2` and two distinct marked first-hit causes.  The first
useful marked cause has conditional probability at most `2 eta_m`: its
rate is at most `eta_m(Y_v+Y_w)`, whereas the union hit-rate is at least
`max(Y_v,Y_w)`.  An edge hitting both endpoints creates one block and is
discarded.  The second endpoint contributes another factor `eta_m`.
Therefore

\[
 \mathbb E B_1\le
 {2\eta_m^2\over(\gamma/d)^2}
                  \mathbb E\sum_{\{v,w\}}Z^g_{v,w}.
 \tag{7.2}
\]

At `eta_m=O(1/d)`, the prefactor is constant.  Thus aggregate energy
`O(M/d^2)` gives `E B_1=O(M/d^2)`.  Likewise, if `O(M/d)` owner roots
become individually bad before their hit, the one marked-hazard factor
gives `E B_0=O(M/d^2)`.  This validates the revised Proposition 7.1.

The static pair budget is exact.  With `D_(v,w)=d_omega(v,w)`, `(PC)` and
the sharp first energy give

\[
 \mathcal S_2(p)=\sum_{v,w}D_{v,w}^2\Gamma_{v,w}(p)
                         =O(M/d^4).
 \tag{7.3}
\]

In a product residual, `H_(v,w)=pY_(v,w)` has conditional second moment
`D_(v,w)^2 Gamma_(v,w)(p)`.  If the raw stopped dynamics transfers this to
the maximal estimate

\[
 \mathbb E\sum_{v,w}\sup H_{v,w}^2=O(M/d^4),
 \tag{7.4}
\]

then the good-load lower bound and `p>=c/d` multiply (7.4) by only `O(d^2)`
and prove (7.1) summed over all pairs.  The generic Doob lemma in the source
correctly reduces (7.4) to aggregate predictable quadratic variation and
squared drift of order `S_2`.  Killing `pY_(v,w)` at its first endpoint hit
leaves its pre-hit maximum unchanged and makes the edge-pair survival
algebra exact; no future-avoidance conditioning is hidden.  The remaining
unproved pair statement is exactly `(DPAIR)`, not the cleanup implication.

The displayed one-step functional `(QPAIR)` is also correct.  Multiplying
an incident pair summand by `p` changes its deterministic scaling exponent
from `N_h-1` to `N_h-2`.  If the next selected edge is `G`, the surviving
summands are exactly those disjoint from `G`; on a root hit the sum is empty
and the process jumps to zero.  Averaging this exact increment with weights
`a_G/X` gives its predictable drift, and the uncentered second moment
bounds its conditional variance.  Hence the two rows in `(QPAIR)` imply
`(DPAIR)` by the generic Doob lemma.

The future-overlap potential correctly avoids a spurious stepwise
`log d`.  For a cross-term `E,F` through a pair root, its two compensated
rates scale with exponent `u_N+m_N` on non-slots and `u_S+m_S` on slots.
Multiplying by the change in the future weight
`(p/p_*)^m_N(p_s/p_(s,*))^m_S` cancels the shared counts and leaves only
the union exponent `u`.  The cross-term survives precisely when the next
edge misses `E union F`.  This verifies the exact drift `(FP5)`.  Under
ideal independent resource survival the remaining multiplier is
`(p'/p)^2`, the survival factor of the two killed roots; all intersection
fugacity has already been paid in `P_0<=S_2(p_*)` (with equality after
restricting `S_2` to the tested pair class and including slots).

The Bonferroni defect `(FP9)` is also exact.  Its multi-hit part is a
three-edge energy.  Expanding the first two hits gives `O(d^2)` anchor-role
pairs, each of base mass `O(d^-3)`.  Conditional on those anchors, further
intersection with the constant number of tracks in `E union F` is bounded
by the same synchronized-chain and private-split exposure used in
Theorem 5.10.  Since
`K_(p_*)(j)<=C(1+p_*^-1)^(j-2)`, this proves `(FE3)=O(S_2/d)`; rigid,
cross-half, fan, and forced-split classes use exactly their previously
audited exceptional estimates.  No arbitrary three-codegree hierarchy is
being assumed.

What remains dynamic is now sharper than the raw `(QPAIR)` statement:
transfer the cumulative positive hazard defect as `(FDEF)` and control the
two predictable drift rows `(FDRIFT1)`--`(FDRIFT2)`.  Telescoping `(FP5)`
bounds the terminal aggregate square, and the identity `(FP11)` then pays
the quadratic variation.  The initial product-residual identities do not
alone prove these transfer/self-correction rows; the evolving root loads
and denominator `X` still require a greedy-history argument.

The signed refinement `(FP13)` is important and correct.  For a typed
potential-incidence vector `g`, subtracting the type means gives the exact
parallel/orthogonal decomposition.  The parallel component is zero on
lowers because `sum_L Y=2dX` and `|L_i|=pM`; it is zero on slots because
`sum_S Y=2X`, `|S_i|=p_s kL`, and
`sigma 2d/M=2/(kL)`.  On owners it is exactly the discrepancy between the
current `2/3` rate mixture/owner ledger and their ideal values.  Hence the
first-order hazard defect is not an unsigned sum of root errors.

The root-energy contraction `(FP20)` also replays exactly: selecting an
edge removes each lower root `v` at rate `Y_v/X`, so the removed square
has conditional mean
`-X^-1 sum_v Y_v(Y_v^h-lambda_h)^2`.  On a pre-bad interval this supplies
`-c_0 R_h/X`.  Young's inequality can therefore absorb the root-energy
half of the orthogonal covariance in a joint Lyapunov.  More sharply,
writing `g_x=b_xY_x` extracts the favorable term
`-bar b_T sum_x(Y_x-bar Y_T)^2`; only the normalized derivative variance
`J_T=sum_x(b_x-bar b_T)^2` remains.  The unresolved dynamic incidence row
is `(GDIR)`: although `J_T` is initially zero by transitivity and its
creation has the same first-entry geometry as `(FE3)`, the source does not
yet prove the required cumulative bound.
This is a genuine further narrowing, not a completed dynamic theorem.

The killed-hazard Hardy lemma closes the pure service part of the pair
drift without a logarithm.  On the good interval, the conditional chance
to hit one of `v,w` is
`(Y_v+Y_w-Y_(v,w))/X>=c_0/X`.  Under the provisional global upper bound
this dominates a fixed multiple of `h_i=1-(p_(i+1)/p_i)^2`.  Exponential
survival in cumulative `h` makes the stopped Hardy operator bounded on
`L^2`, including its maximal version.  Meanwhile the exact identity

\[
                         \mu_Q=-h_iH_Q+\varepsilon_Q-\zeta_Q,
 \qquad                  \zeta_Q\ge0
 \tag{7.5}
\]

follows from `r_E(1-q_E)=rho_i^2`; `zeta_Q` is the additional analytical
bad-kill compensator and is zero in the raw hit-killed process.  It is paid
by the simultaneous loss of nonnegative potential and the same predictable
kill-hazard Hardy argument.  Telescoping the negative term in
`(FP5)` gives `E sum h_i P_i=O(S_2)`.  Therefore the service contribution
to squared accumulated drift is paid, and Cauchy--Schwarz also pays its
cross-term in `(FDRIFT1)`, provided the residual error energy `(FERR)`
holds.  The remaining pair rows can thus be stated as `(FDEF)`, `(GDIR)`,
and `(FERR)`; no independent `Theta(log d)` loss remains.

Finally, `(KH8)` correctly identifies `(FERR)` as a hazard Dirichlet form:
it is just the square of
`varepsilon_Q=sum_E xi_E r_E H_i(E)` expanded over `E,F`.  The
future-potential coefficient `c_iR_i` dominates `xi_Exi_Fr_Er_F` up to
`1+o(1)`, because only a one-step factor
`rho^-m rho_s^-m_S=1+o(1)` is missing while the future fugacity is at least
one.  Thus `(HDIR)` implies `(FERR)`.  Bonferroni decomposes its edge-hazard
error into the same signed root gradient and first-two-hit energy appearing
in `(GDIR)` and `(FE3)`.  Proving their joint stopped transfer remains the
central local analytic gap.

For a marked cluster on `m<=3` owner carriers, the compensated process is
`p^(m-1)Y_A`, and the same union count leaves the root-survival factor
`rho^m` in its future-potential drift.  This correctly reduces its dynamic
tracking to the same killed-hazard/Dirichlet mechanism.  The separate joint
Lyapunov note now supplies the required finite anchored FIFO replay,
proving `Gamma_A=O(1)` and its marked first-two-hit row through size three;
the single-root `(ROc)` alone would not have implied them.

Conditioning on a globally small cleanup event needs care.  A constant
unconditional success probability costs only a fixed factor in an
unconditional cylinder, but does not imply a fixed conditional factor after
every stopped prefix.  Full heredity requires a uniformly prefix-positive
cleanup probability or an argument that expected cleanup is sufficient.
The theorem source correctly leaves this quantifier inside the dynamic
lemma.

Balanced orientations remain independent after every doublet-closed
history, and every selected macro retains its terminal `Sym(h)` switch.
Neither fact proves that the global macro component graph is connected.

## 8. Exact remaining statements

The source leaves precisely:

1. joint local stopped transfer: the Johnson-sector stopped row
   `(JSEC)` of the joint-Lyapunov note for pair-, root-, and marked-cluster
   families, whose exact remaining adaptive form is `(JRES)`--`(JSW)`;
   this is the corrected forward/adjoint form of `(GDIR)` and
   first-order `(HDIR)`, implies `(DPAIR)` and orbit-resolved `(DROOT)`, and
   lets Proposition 6.3 supply global continuation through
   `p=Theta(1/d)`;
2. the stopped-prefix conditioning quantifier needed for a fully hereditary
   deterministic cleanup; and
3. connectivity of the macro component graph, or a separator-scale
   connector bank.

The global algebraic bootstrap and pair tracking remain distinct even
though both use local estimates: positive global rate does not prove a pair
maximal inequality, and `(DPAIR)` alone does not prevent a stall.  Vu's
theorem and the fixed-rank/full-codegree nibble theorems audited in the
dependency files do not supply item 1 with growing rank and reciprocal
error.  The rank-compensated identities substantially narrow the bespoke
proof, but the balanced-doublet integral packing is not yet closed.
