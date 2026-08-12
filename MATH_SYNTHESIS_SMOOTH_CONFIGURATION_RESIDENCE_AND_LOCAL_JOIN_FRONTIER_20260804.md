# Pure-math synthesis: smooth configuration, resident cell splicing, and localized host joins

**Date:** 2026-08-04
**Status:** audited components and a proof-safe synthesis.  No unconditional
proof of `nu(k)<=B(k)+O(1)` or of `nu(k)=B(k)` is claimed.  The exact finite
record remains equality through `k=16`.

## 0. What changed

This wave replaced three broad hypotheses by exact mathematical objects.

1. The two-SCD lower route is not governed merely by scalar or threshold
   capacity.  Its leading chain profile is unique, and its first finite gate
   is an exact whole-job configuration polyhedron.
2. The pair-cell residence route has a genuinely run-transparent local
   square, together with a corrected collar criterion for cross-stratum
   splicing and a sharp small-cell pulse obstruction.
3. The upper occurrence selector, the bounded common-cap suffix router, and
   their local seam co-instantiation now have explicit sufficient theorems
   and explicit Boolean/cyclic counterexamples.

The remaining problem is still integral correlation, but it is no longer
accurately described as one unspecified common-cap matching.

## 1. Lower chainization: the forced Rayleigh face

Put `k=2r`, `A=sqrt(pi)/2`, and let `d/sqrt(r)->A`.  In the two-SCD route,
the residual chain-length and socket-capacity measures converge to

\[
 d\nu(x)=2(A+x)e^{-(A+x)^2}\,dx\quad(x>0),          \tag{1.1}
\]

and

\[
 d\mu(y)=2(A-y)e^{-(A-y)^2}\,dy\quad(0<y<A).       \tag{1.2}
\]

Their first moments agree because

\[
 A=\int_0^\infty e^{-z^2}\,dz.                     \tag{1.3}
\]

Every chain-dependent chunk profile satisfying all anonymous socket tail
cuts converges to `mu`.  Hence:

* every minimum-number-of-chunks rule fails by `Omega(W)`, independently
  of all cut locations;
* balanced equal-part cutting fails in the top tail, where its chunk mass
  is linear in the collar width but socket mass is quadratic; and
* every literal matched limit is capacity-diagonal.

The same statements hold for `h=d+C` with every fixed `C`.  Indeed

\[
 \sigma_C=\sigma_0+CW+Cd+{C(C+1)\over2}=O(W)
            =o(W\sqrt r).                           \tag{1.4}
\]

Thus fixed additive slack does not change the leading lower geometry.  It
can act only on the second-order `W`-scale obstruction.

## 2. The exact second-order anonymous gate

The Rayleigh measures pass every Lorenz/concave fragmentation price.  After
padding the job measure at zero, the socket measure is smaller in convex
order.  There is therefore no remaining Gaussian mean, moment, or concave
separation.

Whole-chain composition is stronger.  For integer job multiplicities
`n_l`, socket multiplicities `m_u`, and

\[
 \mathcal Q_l=\left\{p\in\mathbb Z_{\ge0}^d:
 |p|\le l\le\sum_u u p_u\right\},                  \tag{2.1}
\]

the fractional configuration system is feasible exactly when

\[
 \boxed{
 \sum_l n_l\psi_\theta(l)\le\sum_u m_u\theta_u
 \quad\text{for every }\theta\ge0,}
 \qquad
 \psi_\theta(l)=\min_{p\in\mathcal Q_l}\theta\cdot p.           \tag{2.2}
\]

These prices include nonconcave residue-sensitive functions.  Explicit
abstract examples pass total capacity, majorization, and all receiving
tail cuts but violate (2.2).  Even increasing every socket capacity by one
does not generically remove the violation.  Therefore neither `B+1` scalar
slack nor the Rayleigh convex-order theorem is by itself a rounding proof.

The physical price cone can nevertheless be reduced exactly.  Replacing
`theta_u` by its covering closure `psi_theta(u)` leaves `psi_theta`
unchanged and only lowers the supply price.  Conversely, every
nonnegative, nondecreasing, subadditive sequence is its own covering
closure.  Thus there are no artificial equality-denomination parity
prices: the surviving duals are precisely monotone subadditive covering
prices.

Two large subfamilies are now closed.

* The signed Gaussian tail kernel has one sign change and zero integral,
  so every nondecreasing concave price passes.
* For every real `a>0`, the genuinely nonconcave ceiling ray

  \[
       f_a(x)=\left\lceil{x\over a}\right\rceil
  \]

  passes strictly:

  \[
  \sum_{n\ge0}e^{-(A+na)^2}
  <\sum_{0\le na<A}\left(1-e^{-(A-na)^2}\right).    \tag{2.3}
  \]

  For the physical covering dual the primitive range is `0<a<=A`; the
  endpoint `a=A` has only a zero-measure multiple-of-`A` convention.  When
  `a>A`, the socket restriction is constant one and its covering closure is
  the `a=A` minimum-piece ray up to that convention.  Thus (2.3) covers
  every physical one-denomination scale, while its `a>A` part is an
  additional analytic inequality.

Hence no fixed minimum-piece/MIR scale separates the Rayleigh limit.
Ceiling rays and concave prices still do not generate the whole physical
cone.  On capacities `1,...,5`, the monotone-subadditive covering price

\[
                  (1,2,2,2,3)                       \tag{2.4}
\]

lies outside their conic hull: the functional
`2f(1)-2f(2)+2f(4)-f(5)` is nonnegative on both generating classes and is
`-1` on (2.4).  A remaining separator, if one exists, must therefore use
a genuinely mixed-denomination covering pattern.  The present results do
not decide whether that pattern can have a fixed macroscopic shape or must
vary with the dimension.

The full continuum price class now has an exact one-dimensional
description.  For a right-continuous monotone price `f` with Stieltjes
measure `rho=df`, subadditivity is equivalent to all anchored sliding-window
cuts

\[
             \rho((x,x+t])\le\rho([0,t])
             \qquad(x,t>0),                         \tag{2.5}
\]

and the socket-minus-job margin is exactly

\[
                         \int K(x)\,d\rho(x).        \tag{2.6}
\]

Testing all such `f` is equivalent to testing only physical closures
generated by capacities in `(0,A)`: closing an arbitrary `f` from that
interval leaves its socket values unchanged and can only increase its job
values.  Hence the enlarged clock cone has the same universal positivity
question even though an individual clock price need not be self-generated
from `(0,A)`.

Equivalently, the inverse level clock `a(u)` is nondecreasing and
superadditive, and the same margin is

\[
                         \int_0^\infty K(a(u))\,du. \tag{2.7}
\]

For integer prices the jump positions form one nondecreasing superadditive
sequence; arithmetic clocks are the ceiling rays, while mixed denominations
are genuinely nonarithmetic clocks.  Thus the remaining continuum dual is
not a cone-generation question but the exact positivity of (2.6), or
equivalently (2.7), on this clock cone.

The clock problem has an exact carry-aware compact reduction.  For an
internally superadditive compact profile `b:[0,1]->[0,infinity]`, define its
unbounded-knapsack closure

\[
 (\mathsf Sb)(t)=
 \sup\left\{\sum_i b(r_i):0\le r_i\le1,
                         \ \sum_i r_i\le t\right\}.             \tag{2.8}
\]

This is the pointwise least global superadditive clock extending `b`.  If
`b(1)>=A`, the exact least Gaussian functional among all extensions is

\[
 \mathcal J(b)=\int_0^1K(b(t))\,dt+
               \int_1^\infty K((\mathsf Sb)(t))\,dt.            \tag{2.9}
\]

Moreover, possible counterclocks reduce without loss to finite
denomination tables.  For every `n>=1`, let

\[
 c_0=0\le c_1\le\cdots\le c_n,
 \qquad c_{i+j}\ge c_i+c_j\quad(i+j\le n),
 \qquad c_n\ge A,
\]

and define the exact carry Bellman clock

\[
 V_0=0,
 \qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j}).        \tag{2.10}
\]

Then universal clock positivity is equivalent to the finite statement

\[
                         \sum_{m\ge0}K(V_m)\ge0     \tag{2.11}
\]

for every such table.  This inequality is open.  It is strictly stronger
than the earlier one-period residue envelope, which retained only one
partition of each quotient time and discarded carries.  In particular,
the negative endpoint pair at the critical half step is not a counterclock:
superadditivity forces the period endpoint to be `2A`, its closure is
`A floor(2t)`, and the resulting sum is strictly positive.  Even inserting
an undominated denomination can decrease the positive Bellman margin, so a
one-denomination-at-a-time monotonicity proof is unavailable.

The first mixed grid nevertheless closes exactly.  Every `n=2` table
`(0,y,T)` with `2y<=T` and `T>=A` has Bellman clock
`V_(2q)=qT`, `V_(2q+1)=qT+y` and a strictly positive Gaussian sum.  If
`y>=A/2`, monotonicity in `T` reduces to the arithmetic clock of step `y`;
if `y<=A/2`, a logarithmic-derivative argument reduces the minimum to the
two already certified endpoint clocks.  Thus any finite Bellman separator
must have grid size at least three.

At grid size three, the max-plus recurrence is classified exactly and its
positivity is now fully closed.  For a table `(0,x,y,T)`, if
`2T<=3y` the clock is a two-coset lattice of period `y` plus one transient; if
`3y<=2T` it is a three-coset lattice of period `T` plus one transient.  In
the critical subbranch of the first regime, all remaining sign information
reduces to the single scalar inequality

\[
 \mathcal H(P)=\sum_{q\ge0}
       \bigl(K(qP)+K(qP+A-P)\bigr)\ge0,
 \qquad {2A\over3}\le P\le A.                     \tag{2.11a}
\]

This scalar inequality is now proved uniformly.  Expanding the four head
Gaussians, embedding them in the full theta lattice, and bounding the two
remaining tails leaves the strict rational margin
`1/28-1/20000-1/36>0`.  Hence every regime-I table with `y<A` passes.
For `y>=A`, the same normal form is bounded below by the already proved
two-slot table `(0,x,y)`, so the rest of regime I passes as well.

Regime II is now closed too.  Period monotonicity reduces it either to an
arithmetic-clock boundary or to the compact triangle

\[
 \mathcal L_3(A;z,y)=C(A)+F_A(z)+F_A(y),
 \qquad 0\le z\le y/2,
 \quad 0\le y\le2A/3.                              \tag{2.11b}
\]

The shift has no interior minimum, so only the two boundary rows remain.
Completing each to the full Jacobi lattice and bounding the two-Gaussian
envelopes gives the uniform margins `397/20000` and `117/20000`.
Consequently every `n=3` table passes strictly.  A finite Bellman
counterexample, if one exists, has grid size at least four.

There is also now an all-grid normalization.  Delete every denomination
after the first displayed value at least `A`; this can only decrease the
functional because the two clocks agree before the crossing and lie in the
increasing Gaussian tail afterward.  At that first crossing, lower the
endpoint to `max(A,P_n)`, where `P_n` is the exact lower-denomination
Bellman value at capacity `n`.  This preserves internal superadditivity and
again can only decrease the functional.  If `P_n>=A` the endpoint is
Bellman-inert, but it cannot simply be deleted while retaining a displayed
first crossing: all remaining generator values may be below `A`.

For any finite table, let `lambda=max_j c_j/j`, let `g` be the gcd of the
maximum-density denominations, and form the reduced residue graph modulo
`g`.  Its maximum reduced residue weights `beta_r` have simple witnesses
of at most `g-1` subcritical steps.  Exactly, for every
`m>=n(n-1)`,

\[
                     V_m=\lambda m+\beta_{m\bmod g}.           \tag{2.11c}
\]

Thus every possible separator is a finite head plus at most `g` shifted
Gaussian lattice tails; there is no unstructured infinite Bellman
recursion.  The tempting stronger lower bound by the single
maximum-density lattice is false, so the finite head cannot be discarded.

The stabilized shifts carry more structure than arbitrary cosets.  If
`P=h lambda` is a chosen maximum-density period and `s_r` are its Apéry
shifts, concatenating residue walks gives the exact carry inequalities

\[
 s_{r+t}\ge s_r+s_t\quad(r+t<h),
 \qquad
 P+s_{r+t-h}\ge s_r+s_t\quad(r+t\ge h).             \tag{2.11d}
\]

Hence `(0,s_1,...,s_(h-1),P)` is itself internally superadditive and its
Bellman clock is exactly `qP+s_r`.  The formal Apéry tail is therefore one
honest smaller Bellman clock, not an unconstrained product of residue
choices.  This recursion does not remove the finite availability head, and
when `P<A` it does not meet the already proved first-crossing hypothesis.

At grid size four, maximal generator efficiency gives an exact two-coset
form, an effective three-coset form with only three exceptional positions,
or a four-coset Apéry tail whose nonperiodic prefix has capacity below nine.
All three branches are now proved positive.  In the two-slot-efficient
branch, below period `4A/5` a periodized Rayleigh derivative is positive,
while above it every interior critical point collapses to a three-Gaussian
strongly convex inequality with a strict rational margin.  In the
four-slot-efficient branch, the exact reduced residue weights are

\[
 \beta_1=\max\{d_1,d_2+d_3,3d_3\},\qquad
 \beta_2=\max\{d_2,2d_3\},\qquad \beta_3=d_3,
\]

with one delayed residue-one correction at capacity five.  The complete
threshold face `T=A` has margin `47/10000`.  Endpoint monotonicity then
leaves only

\[
 C(\alpha)+K(4\alpha)-K(5\alpha),
 \qquad A/4\le\alpha\le A/3,
\]

and the small-step Fourier ceiling margin dominates its adverse tail by
`1117/94500`.  Hence the size-four-efficient branch is positive.  Only
the three-slot-efficient branch then needs explanation.

That branch is handled without dropping any transient.  On the face
`w=y` it is an effective three-coset clock plus one finite transient pulse;
on `w=2u` it is one uniform three-step ceiling margin plus five
occurrence-labelled pulses, including the adverse tail pulse.  Every face
with `z>=A` is first-crossing reducible to the proved `n<=3` theorem.  In
the remaining subcritical `w=y` face, strict period monotonicity reduces
the interior to the two surfaces `P+u=A` and `P+u=2y`.  The first is
positive by an endpoint-period train comparison with margin
`1659/220000`.  On the second, writing the repeated period gap as
`b=y-u` gives a train strictly increasing in `b`; its minimum is the
uniform lattice `C(y/2)>0`.  Finally, the complete `w=2u` pulse functional
is increasing in its period.  At its lower boundary it is bounded either
by the first train margin or by the Apéry scalar margin `1117/94500`.

Consequently every internally superadditive Bellman table of grid size at
most four has strictly positive functional.  At this stage the first
possible finite counterexample had grid size five.  This is a finite dual
theorem; it does not by itself prove the all-slot inequality.

The next grid, `n=5`, has a complete availability-filtered Apéry
normal form.  First-crossing deletion forces the threshold to occur at slot
five, and a maximal-efficiency size `h in {2,3,4,5}` gives respectively:

* a two-state lattice plus exactly two finite pulses;
* a three-state lattice plus exactly five finite pulses;
* twelve linear residue forms and the exact head below capacity fifteen;
* sixteen simple paths per nonzero residue and the exact head below
  capacity sixteen.

The identity is exact at every capacity, including tied maximum-density
generators; availability is part of the residue maximization, so no early
representative is silently replaced by a later one.  The `h=2` branch has
already been signed completely.  Its first-crossing constraints leave only

\[
 {2A\over5}\le y<{A\over2},
 \qquad A-2y\le s\le {y\over2},
\]

where a concave periodized-Rayleigh derivative envelope reduces the sign to
two exact boundary inequalities and proves
`mathcal L_2(y;s)>=C(y/2)>0`; both finite pulses are nonnegative.  Hence an
`n=5` counterexample must lie in `h=3,4,5` at this stage.

There is also an all-grid endpoint normalization.  Saturate the first
threshold endpoint to `max(A,P_n)` and assign a table to its least
maximum-density size.  If that size is the endpoint `n`, then necessarily
`c_n=A`: if `c_n=P_n>A`, an attaining lower partition contains a lower
denomination of at least the endpoint density.  Thus the genuinely `h=5`
branch lies entirely on its threshold face.  On that face,
`c_i<=iA/5`.  Exact one-period train estimates give

\[
 F_A(v)>-{1\over40}\quad(v\le3A/5),
 \qquad
 F_A(v)>-{21\over400}\quad(v\le4A/5).
\]

The literal endpoint-period bound therefore gives

\[
 \Phi>{1\over25}+{1\over25}-{1\over40}-{21\over400}
      ={1\over400}>0.
\]

Thus the `h=5` branch is closed completely, and every five-slot
counterexample must lie in `h=3` or `h=4`.

For `h=4`, monotone endpoint saturation gives exactly three faces:

\[
 T_*=\max\{A,P+x,y+z\}.
\]

The active threshold face `T_*=A` is now positive with exact margin
`199/2310000`, by reflecting the two upper trains and using the sharp
small-shift train bounds.  The two Bellman-inert composites `T_*=P+x` and
`T_*=y+z` are now closed as well.  A complementary-pair train theorem first
reduces both faces to one ceiling train and two reflected pairs.  Writing
`delta=T_*-A`, the active-pair equality removes every shifted Gaussian
train from the residual gate.  The only compact loss obeys

\[
 \Delta_K(u,\delta)
 <\min\left\{{3\delta\over10},{57\over1000}\right\},
 \qquad
 0<F_A(A/4)-C(A)<{1\over800}.
\]

Finally `C(A+delta)` is increasing and strictly concave.  Three exact
rational endpoint comparisons prove the resulting one-dimensional gate
uniformly.  Hence the complete five-slot `h=4` branch is positive; no
inert face remains.

The `h=3` endpoint split is similarly exact.  Every active threshold table
`c_5=A` is positive with uniform margin `69/10000`.  On the strict inert
face, all five original pulses collapse to the delayed four-slot form, and
the repeated-gap gate

\[
 \mathcal R(a,\beta)
 =\mathcal L_3(a+2\beta;a,a+\beta),
 \quad
 0\le a\le\beta,
 \quad 2a+2\beta<A<2a+3\beta,                       \tag{2.11e}
\]

remains.  The other apparent obstruction was an explicit three-pulse train
`mathcal H(p,a,b)` on `p>=3a` and `a<A-p<b<=2a`, with an adverse final
tail.  That function is now proved strictly concave in `b`.  Its threshold
endpoint is already positive, and at `b=2a` all three pulses vanish.
Consequently this entire face reduces to the second pulse-free lattice

\[
 \mathcal P(p,a)=\mathcal L_3(p;a,2a),
 \qquad
 0<a<{A\over4},\quad
 \max\{3a,A-2a\}<p<A-a.                            \tag{2.11f}
\]

Both pulse-free gates are now closed.  For the short-singleton train
(2.11e), differentiation in the repeated gap and retention of the complete
`q=1,2` blocks reduce the parameter domain to two strictly convex
one-variable branches.  Both have the same minimum at `(p,u)=(3/4,1/4)`;
three exact rational Gaussian certificates make that corner positive.
The uniform and threshold lower boundaries are positive, so
`mathcal R>0` on its full domain.

For the long-singleton lattice (2.11f), its complete `q=1,2` derivative
block `B(r,s)` is jointly convex on the larger rectangle

\[
 0\le r\le {2\over5},\qquad0\le s\le {1\over5}.
\]

At the rational point `(12/35,1/7)`, exact order-24 Taylor bounds give

\[
 B>{1\over20},\qquad0<B_r,B_s<{1\over100}.
\]

Its global supporting plane therefore yields

\[
                         B(r,s)>{79\over1750}>0.
\]

Hence \(\partial\mathcal P/\partial p>0\), and the already-positive density
and threshold lower-period boundaries close `mathcal P` throughout.  The
strict `b`-concavity then closes the retained-pulse face.  Thus every
five-slot Bellman table is positive; any finite counterexample has grid
size at least six.

The exact theta endpoint-descent obstruction remains informative but no
longer blocks the proof: at the common uniform corner the true period
`E=5A/4` is positive while the relaxation `F_E -> F_A` is negative, which
explains why the successful proof had to retain the period-three
derivative.  No finite Apéry head or retained pulse remains unclassified.

The next grid, `n=6`, now also has an exact availability-filtered normal
form.  First crossing, endpoint saturation, and least-maximizer assignment
give the five branches `h=2,...,6`; their exact stabilization cutoffs are

\[
                         (6,12,18,24,25).
\]

The two extreme branches are closed.  For `h=6`, the complementary pairs
`(c_1,c_5)` and `(c_2,c_4)`, together with `c_3<=A/2`, give the literal
endpoint-period margin `163/70000`.  For `h=2`, the exact clock is a
two-coset lattice with two nonnegative transients.  Retaining all three
compact derivative rows and reducing their concave envelope to rational
endpoint certificates proves the entire new `A/3<=y<A/2` scalar face
positive.  Thus only `h=3,4,5` remain at grid six.

There is a genuine obstruction to a purely structural induction.  The
affine setup-cost family has every lower generator indispensable, an inert
endpoint, and exact clock

\[
 V_m=\alpha m-\beta\left\lceil{m\over n-1}\right\rceil;
\]

deleting the endpoint and then restoring the first crossing returns the
same grid.  Nevertheless its balanced specialization is now proved
positive in every dimension.  Splitting its Beatty clock into selected and
omitted residues gives an omitted train `Omega_h`.  An exact root-of-unity
sum bounds its threshold-period part by `1/40000`, while shortening the
period contributes less than `-1/5832`; hence

\[
                  \Omega_h<-{4271\over29160000}<0.
\]

The selected clock therefore strictly dominates the positive arithmetic
clock.  This removes the balanced no-descent family as a separator, but it
does not close the general setup-cost parameter or the three surviving
six-slot branches.

The continuum primal is equally sharp.  Total job work equals total socket
capacity exactly, so any feasible limiting fragmentation has zero trimming
almost everywhere.  It is precisely a finite coagulation measure: partition
the socket measure into finite groups whose capacity sums have the job
measure.  In Rayleigh coordinate this is equivalent to decomposing the
Rayleigh measure into finite equal-weight blocks of arithmetic mean
`A=sqrt(pi)/2`, each block containing exactly one above-mean point and all
remaining points below the mean.  The forced group-count tails are

\[
       \rho_0\{N\ge n\}\ge e^{-\pi n^2/4},                     \tag{2.12}
\]

and their total minimum is strictly smaller than the available socket
intensity.  Thus raw group count is not the obstruction; exact additive
coagulation is.

The open anonymous lower theorem is now:

> **Smooth binomial configuration.**  Prove (2.2) for the actual counts
> `n_l=H_{t-l}` and `m_u=H_{t+u}+1`, then select integral configurations
> with only bounded terminal defect.

Its leading-order primal analogue is the Rayleigh coagulation existence
theorem just stated.  A coagulation kernel would close that continuum
primal; a negative finite Bellman table would be an exact mixed-price
separator.  No finite-to-continuum converse or dual closedness is being
assumed here.

Even this does not prove the two-SCD construction.  The selected chunks
must still be matched by literal containment into a jointly chosen collar
SCD, and then serialized with the countdown/source-word rows.

The existing coloured-rotor route is an alternative rather than a shortcut:
its stationary fractional clock is known, and a fixed exact owner--payload
table has an integral Hoffman selector, but choosing one such table and
fusing it into one coloured Euler component remain integral gates.

## 3. Residence: exact local splice and exact exceptional gate

Pair stratification partitions `J(2r,r)` into cube cells.  Within every
good cell the required chronology is now explicit.  If `h` is a power of
two with `h>=4L` and the cell dimension is at least `h`, a syndrome map
resolves the active `h`-cube into isometric `2h`-cycles.  Equal-column
weight-two kernel generators give literal square switches separated by at
least `h/4`; a parity twist handles the inactive coordinates.  Choosing
ports along a Hamilton path of the quotient cube supplies a flat
occurrence-bit gauge and a globally separated switch tree, producing an
`L`-resident Hamilton cycle of the whole cell.  The factor `1/4` is sharp
for this equal-column weight-two basis method.

This closes local good-cell chronology when the singleton dimension is at
least the least power of two `h>=4L` (hence `h<8L`).  It does not select
one compatible cell per owner and does not provide the balanced endpoint
collars needed by a critical cross-stratum splice.

For two cells of the same singleton dimension, transfer double status from
an active pair `q` to a full pair `p`.  Cutting the `q`-edge in the first
cube and the `p`-edge in the second gives a twisted Johnson square whose
two seams use opposite physical members.  Coherently relabelled
`rho`-run cube cycles merge into one cycle with run at least `rho-1`.
Thus a matching of cells splices with no further residence debt.

For an `m` to `m+2` splice, the two seams reuse the same physical `p/q`
members and those directions are active inside the larger cube.  Long arcs
alone are insufficient, but collar disjointness is stronger than necessary.
If a common direction occurs at inward transition-slot ages `i,j` across a
new seam, its exact safety condition is

\[
                              i+j\ge L.              \tag{3.1}
\]

Consequently, once the exceptional directions `p,q` are absent from the
large-side collar, one seam is always relabellable already at `m>=L`, by
reversing the two age orders.  For both seams simultaneously, require `p,q`
to be absent from both large endpoint collars, fix the common cut, and join
a small-cube direction to a large-cube direction exactly when both endpoint
age sums satisfy (3.1).  A common relabelling exists if and only if this
ordinary bipartite graph has a perfect matching.

This gives two strong corollaries.  Arbitrary endpoint histories are
automatically solvable by `m>=2L-1`, improving the former `4L` range.  At
the critical `m>=L` scale, both seams are solved when, in each cube, the two
endpoint collars use the same support: old residence forces the two ages of
each supported direction to add to `L`, so complementary matching works at
both ends.  Thus the critical open row is now planting or regenerating
balanced-support cuts, not collar cardinality.  Naive `Q_0` or `Q_1`
triangle ears still force a length-one run, so genuinely smallest cells
retain a separate buffer problem.

The exact local residence target is therefore a **balanced-cut / exceptional
multiport buffer theorem**, rather than a disjoint-collar theorem.

There is now a second, global way to remove the owner-supply part of that
exception.  For a fixed middle owner and a uniformly random perfect pairing
of the `2r` coordinates, the probability that its singleton-pair dimension
is below

\[
             M=L+\lceil3\log_2r\rceil
\]

is `2^{-r+O(sqrt(r) log r)}`.  Three independent pairings and a union bound
over the middle layer therefore yield three deterministic frames in which
every owner is good in at least one frame.  More generally, for every fixed
`h`, `h+2` frames give at least `h` good choices per owner.

This closes exact resident-capable **owner coverage**, not the factor.  The
weakest selector is a perfect matching in the symmetric successor-occurrence
graph whose induced permutation also keeps transition supports disjoint for
the next `L-1` edges.  Seam-free inheritance would be a whole-good-cell
exact cover, but that route is now ruled out arithmetically.  A dimension-`m`
pair cell has `2^m` owners, whereas

\[
             \nu_2\binom{2r}{r}=s_2(r)\le\lfloor\log_2r\rfloor+1.
                                                               \tag{3.2}
\]

Thus a partition into whole cells of dimension at least `M` forces
`M<=s_2(r)`, impossible for the required `M=Theta(sqrt(r))`, regardless of
how many pairing frames are supplied.  The all-pairings fixed-dimension
hypergraph nevertheless has a symmetric fractional exact cover, so this is
a genuine integral selector obstruction.  Even at the valuation boundary,
the three literal pairings of four coordinates give three good squares with
only the all-half fractional selector; here the failure is already visible
from the actual cell size four modulo the owner count six, so it is not a
separate incidence obstruction beyond exact-size congruence.

For two frames, whole-block selection has an exact component criterion:
no component of the bipartite block-intersection graph may contain an
unavailable block on both shores.  For three frames, choose a subfamily of
available blocks on the third shore, delete their union, and forbid every
residual first- or second-shore block whose original block met that union.
An exact selector exists if and only if some such choice leaves no residual
intersection component forbidden on both shores.  The valuation theorem
shows that no third-shore separator can succeed in the high-`M` whole-cell
regime.

Consequently the global selector must cut good-cell chronologies into
proper resident path blocks and splice those blocks.  Their size library
must carry the residue of `binom(2r,r)` modulo `2^M`; in particular, a
library whose every block size is divisible by `2^{s_2(r)+1}` cannot
suffice.  This arithmetic row does not itself force different block
lengths.  A switch-only tree on a fixed union of whole-cell cycles cannot
repair owner overlaps or holes because switches preserve every owner
degree and multiplicity in that edge union.  Switch trees remain useful
after a punctured/spliced macro selector has already produced a spanning
factor, or inside a broader operation that also changes the selected
blocks.

The arithmetic defect can be localized sharply.  Put
`omega=binom(2r,r) mod 2^M`.  In any good cell of dimension at least
`M+1`, one can choose a cyclic resident interval of length `omega` or
`omega+2^M` so that both it and its complement have at least `L` vertices.
This is the exact one-puncture scalar freedom.  Extending a preselected
owner set `U` by whole cells from two other pairing frames has an exact
criterion: after deleting the owner edges `U` in their block-intersection
graph, no residual component may contain a touched or unavailable block on
both shores.

When all blocks are available, this criterion has the sharper closed form

\[
                         U=B\setminus A,                       \tag{3.3}
\]

for a `P`-measurable set `A`, a `Q`-measurable set `B`, and `A subseteq B`;
equivalently `U` is exactly a one-way dicut.  This rules out the direct
one-shore Gray-prefix idea.  A connected interval inside an `R`-cell which
is a union of whole contained cells from one other frame must be one cell,
so its size is a power of two; at `L>=3` and `L>s_2(r)` even the unique
residue-compatible power is either too small or cannot support an
`L`-resident Hamilton path.  Within this all-available whole-block
completion class, any surviving selector candidate must therefore be a
genuinely two-shore nested measurable difference, followed by macro Hall
and collar holonomy.

The first genuinely two-shore arity is now sharp as well.  For any source
cell `C` and one compensation cell `K`, the trace `K cap C` is a disjoint
union of equal-dimensional cube faces which are pairwise edge-isolated.
Hence a connected one-cell trace is one face.  If only one compensation
cell meets `C`, exact nested-difference completion forces the complement of
the puncture to be precisely that trace; the two-adic congruence then fixes
its dimension to `s_2(r)<L`, contradicting the resident-path requirement.
Thus every viable selector needs at least two compensation cells meeting
the source cell.  A global `3*2^a` nonresident calibration shows that
nested measurability itself is not the obstruction; the live target is a
compound two-touch resident trace.

For two touching traces, the remaining connectivity row now has an exact
linear-algebraic form.  Identify the source cube with `F_2^m`.  Each trace
is an affine subspace `t_i+L_i`; quotienting its standard-basis directions
`A_i` turns its connected face components into cosets.  After quotienting
by `A_1+A_2`, the two face families form a bipartite graph `G` with a free
translation action by

\[
 H=\pi(L_1)\cap\pi(L_2).
\]

The original face-glue graph is a complete fibre blow-up of `G`, and `G`
is a regular `H`-voltage cover of a finite base multigraph `B`.  Exact
connectedness is therefore

\[
 \boxed{B\text{ connected and its closed-walk voltages span }H.} \tag{3.4}
\]

In particular,

\[
 |E(B)|-|V(B)|+1\ge\dim H,                              \tag{3.5}
\]

so a tree base cannot glue a nontrivial common quotient direction.  This
closes face connectivity, not interval order: a valid selector still needs
a Hamilton face traversal, multi-seam residence collars, and globally
disjoint compensation cells satisfying the nested-difference dicut.

There is one exact topological corollary if all perfect pairings are used as
frames.  Orient one long-run cycle in every good cell.  By transitivity of
`S_(2r)` on middle owners, every owner is good in the same positive number
`a` of frames.  Each such frame contributes one incoming and one outgoing
successor occurrence, so the successor-occurrence bipartite **multigraph**
is `a`-regular and has a perfect matching.  This closes ordinary successor
Hall and gives a directed spanning permutation cover.  It does not close
residence or simplicity: the matching may change frames from one edge to
the next, violate the `L-1` transition-support collar, or create an
antiparallel two-cycle.

The correct selector scale is therefore macroscopic.  Partition the owner
layer into vertex-disjoint internally resident paths of at least `L-1`
edges, and join two blocks only by a literal seam whose complete two-sided
collar is resident.  These blocks close into a spanning resident cycle
factor exactly when the seam-safe block graph satisfies ordinary Hall.  A
regular **block** occurrence graph is sufficient; regularity of the owner
successor graph is not.  Indeed, arbitrarily many parallel occurrences of
the two directions of one Johnson edge give a regular owner graph whose
only permutation is a forbidden antiparallel two-cycle.

Balanced collars add one global phase row.  A safe seam transports the
endpoint age phase by a bijection, so a selected block cycle lifts exactly
when the resulting collar holonomy has a fixed point.  A flat gauge
`tau_ij=g_j g_i^{-1}` is a strong sufficient certificate, since every
cycle product telescopes to the identity.  Alternatively, starting from a
literal resident cycle factor, a globally separated spanning tree of
two-cycle switches merges all components into one resident cycle.  The
separation requirement prices reusable switch ports: between consecutive
new seams every retained old path has at least `L-1` transitions, and every
new seam collar is resident.

## 4. Upper occurrence selection

For a Boolean Johnson cycle cover, one physical edge belongs to only `q`
directed `q`-edge intervals.  Hence a q1 colour of multiplicity `mu_R`
appears in at most

\[
 \mu_R\left({m(m-1)\over2}-1\right)                 \tag{4.1}
\]

higher-target event scopes.  This polynomial load makes a blocker LLL
available on the following hybrid face:

1. almost every target has one deterministic-safe old witness;
2. the vulnerable leave has logarithmically many random-colour-disjoint
   witnesses, each using boundedly many repeated colours; and
3. components have logarithmic breaker banks or an immutable private
   reserve map.

Uniform logarithmic menus are impossible at q2.  If `V_2` targets receive
`t` witnesses, then

\[
 {V_2\over N_2}\le
 {6m\over(m-1)(m-2)(t-1)}.                          \tag{4.2}
\]

Thus logarithmic redundancy can cover only an `O(1/(m log m))` vulnerable
fraction.  The factor must be clean on almost every low-width target.

This condition is substantive.  A literal Boolean six-cycle has two
distinct targets with unique admissible witnesses forcing different
occurrences of one repeated q1 colour.  Separate target feasibility and
automatic cycle breaking do not imply one occurrence section.

## 5. One-step Boolean routing and factor-restricted suffix cuts

Let `P` be distinct rank-`s` Boolean port values, each with at least `L`
common type-legal one-coordinate extensions.  Any two port neighbourhoods
intersect in at most one upper value.  Therefore, after forbidding a value
bank `F`,

\[
 |N(X)-F|\ge |X|L-{|X|\choose2}-|F|.                \tag{5.1}
\]

If `|P|<=L` and `|F|<=L-1`, Hall gives a simultaneous one-step suffix
router.  With private gain-to-port prefixes, an injective reservation of
physical sink occurrences, and terminal type legality common to every gain
incident with each factor port, the regular-factor flow becomes literal.
Precisely, if the abstract incidence factor has left degree `h` and right
degree at most `h`, weighting every incidence-prefix/port-suffix
concatenation by `1/h` gives a unit flow from every gain; integral max flow
then selects disjoint legal paths.

More generally, let `B=(G,P;E)` be the literal claim-to-port factor and let
`Gamma` be the typed strict gammoid of the residual suffix network.  The
exact factor-router deficiency is

\[
 \delta_B=\max_{X\subseteq G}
       \bigl(|X|-r_\Gamma(N_B(X))\bigr).                       \tag{5.1a}
\]

Equivalently, if

\[
 H_B(U)=\{g\in G:N_B(g)\subseteq U\},
\]

then exact routing is characterized by

\[
                 |H_B(U)|\le r_\Gamma(U)\qquad(U\subseteq P). \tag{5.1b}
\]

Thus a suffix cut is charged only for gains whose complete port menu is
trapped behind it; independence of the entire active-port set is stronger
than necessary.  For a left-`h`-regular/right-at-most-`h` factor, the single
degree-weighted flow condition

\[
 {1\over h}\sum_{p\in U}\deg_B(p)\le r_\Gamma(U)
 \qquad(U\subseteq P)                                      \tag{5.1c}
\]

is sufficient and is one ordinary scaled max-flow.

In the middle-level specialization, an `O(sqrt(m))` active port bank is
therefore harmless **on this one-step Boolean face** when every port retains
`m+1-O(1)` typed extensions and only `O(sqrt(m))` sink values are
unavailable.  Outside that face, the exact premise remains a physical
factor-restricted port-router certificate.  After deleting one fixed
compensation linkage and all prefix interiors, the stronger clean form

\[
             r_{\Gamma_{\rm suf}^{\rm type}}(P)=|P|,            \tag{5.2}
\]

remains sufficient but is no longer the sharp target.  The Middle Levels
graph `ML_m` is exactly `m`-vertex-connected.  Hence a capacity-faithful,
type-safe bidirected copy of `ML_m-F` in the suffix network routes every
claim bank with `|G|+|F|<=m`, provided the ports and a disjoint bank of
legal sinks lie in that same copy and every corridor path is typed-legal.
This makes the scalar `O(sqrt(m))` bank harmless.  The protected Middle
Levels two-factor still supplies only the abstract degree factor: the
current parent/reference matching does not embed this literal corridor,
the private prefixes, or the capacity-faithful physical port map.  A common
unit suffix bottleneck shows that a factor plus an unrelated matching
cannot imply them.

For two required physical occurrence coordinates in one fixed complete cap
state, Rado followed by Edmonds gives the exact common deficiency

\[
 \delta=
 \max_{J_0\cap J_1=\varnothing}
 \left(|J_0|-r_{N_0}(A_0(J_0))
      +|J_1|-r_{N_1}(A_1(J_1))\right).              \tag{5.3}
\]

This formula requires global product closure and prior allocation of every
cross-coordinate shared capacity.  It does not follow from two marginal
matchings or authenticate transported phase 1.

## 6. Exact local co-instantiation

Eligible aperture seams form a product Johnson slice.  Fix a bounded total
coordinate footprint and partition the slice into local profiles `lambda`.
If profile `lambda` has exact extension count `n_lambda`, and lower, upper,
and router modules share a tree of complete interface separators with one
uniform separator certificate outside an occurrence exception bank
`E_lambda`, then at least

\[
 \boxed{\sum_\lambda(n_\lambda-|E_\lambda|)_+}       \tag{6.1}
\]

seams carry one common literal tuple.  Pinned upper semijoin plus reserve
Hall and either the degree-weighted router cascade or the one-step Boolean
router may be used as modules, provided all physical interiors are private
outside complete priced interfaces.

If the module graph has one chordless cycle after attached trees are
eliminated, feasibility is equivalent to a fixed point of the composed
separator transfer.  The equality/equality/disequality triangle shows why
all modules and every pair can be feasible while the full host is empty.
Pairwise compatibility is therefore not an acceptable replacement for a
join tree or a verified cyclic fixed point.

## 7. Shortest honest implication

For a fixed charge `C`, a complete proof along the present regenerative
route would follow from one compatible selected odd spine.  At every level,
its materialized odd terminal host and its terminal-only even tap must
satisfy, as applicable, all of the following.

1. The actual mixed-denomination configuration prices (2.2), including the
   exact finite Bellman inequality (2.11), an integral
   pattern selection with bounded defect, literal cross-SCD containment
   Hall, and countdown serialization.  On the continuum face, the exact
   remaining price statement is positivity for every anchored-window
   measure / superadditive clock; concave and every fixed macroscopic
   one-denomination ceiling/MIR ray are already certified.
2. A punctured/spliced resident owner factor built from proper paths cut
   out of the explicit syndrome/switch-tree good-cell
   chronologies.  Same-stratum squares, globally regenerating
   balanced-support cuts, and a genuinely small-cell multiport buffer must
   absorb every exceptional cell, while the block system carries the
   two-adic owner residue and satisfies macro Hall plus collar holonomy (or
   an equivalent globally separated switch-tree completion).  Whole-cell
   exact cover is impossible asymptotically, and owner-level regularity is
   insufficient.
3. A deterministic-safe upper witness for almost every target, a tiny
   redundant vulnerable leave satisfying the blocker LLL, and immutable
   reserve Hall.
4. A localized product-slice seam profile with either a complete interface
   join tree or a verified unicyclic fixed point.
5. Distinct Boolean router ports with a common linear typed extension bank,
   injective sink occurrences, and private gain prefixes in that same state;
   or, on a more general face, the factor-restricted condition (5.1a),
   trapped-menu cuts (5.1b), degree-weighted flow (5.1c), or the stronger
   full typed active-port certificate (5.2), in both occurrence coordinates
   together with the product-closure hypotheses of (5.3).
6. Materialized terminal-only even-tap certificates and final literal
   replay with charge at most `C`, as required by the existing tap
   implication.
7. Literal export of the next selected odd state; terminal-only tap and
   repair choices are not exported or accumulated.

The previously proved terminal-charge implication then gives

\[
                         \nu(k)\le B(k)+C.           \tag{7.1}
\]

This is an implication, not an existence theorem.  The two most exposed
constructive gaps are now:

\[
 \boxed{
 \begin{gathered}
 \text{smooth binomial configuration + literal containment/countdown},\\
 \text{residue-carrying punctured cell selector + balanced-cut regeneration}\\
 \text{+ small-cell buffer + macro Hall/holonomy.}
 \end{gathered}}                                    \tag{7.2}
\]

The upper selector and small router have exact host-class theorems, but
their hypotheses must still be produced by the same owner chronology.

## 8. Verdict

No `B+O(1)` theorem has been proved.  What has been proved is that:

* fixed additive slack cannot bypass the leading lower fragmentation;
* Gaussian/Lorenz feasibility is not the final anonymous lower gate;
* every fixed continuum ceiling/MIR obstruction is absent, while the full
  mixed-denomination dual is exactly an anchored-window / superadditive-clock
  positivity problem with an exact carry-aware finite Bellman reduction;
  every grid of size at most five is positive, so every finite counterexample
  has grid size at least six.  At grid five the `h=2`, `h=4`, and genuine
  endpoint-efficient `h=5` branches close by their exact train bounds; the
  `h=3` threshold and short-singleton faces close by endpoint and repeated-gap
  derivative theorems, while one global convex tangent closes the remaining
  long-singleton lattice and its retained-pulse parent.  Every finite head,
  threshold chamber, and adverse pulse at this grid has been eliminated.
  Every finite table has an exact finite-head plus Apéry-tail representation;
  grid six and larger remain open;
* at grid six the complete `h=2` and `h=6` branches are positive, while the
  exact `h=3,4,5` six-slot forms remain the first finite analytic frontier;
  separately, the balanced affine no-descent family is uniformly positive
  in every dimension, but its general `beta` parameter interval remains
  open;
* an explicit syndrome-quotient switch tree supplies a resident Hamilton
  chronology inside every sufficiently large good cube cell;
  a sharp two-adic obstruction rules out selecting those whole cells as an
  exact cover at the required dimension, so residue-carrying proper path
  blocks are mandatory, though arithmetic alone does not force unequal
  lengths;
  complementary ages solve cross-stratum collar capacity at the critical
  scale; balanced cut regeneration and genuinely small-cell buffers remain,
  while multiframe owner coverage and even owner-level successor regularity
  still require a global cell selector, macro Hall plus holonomy, or
  preservation of separated switch trees; in the all-available two-frame
  completion model an extendible puncture is characterized exactly as a
  two-shore nested measurable difference, while the connected one-shore
  construction by whole cells contained in the source cell is ruled out at
  the residence scale; every two-touch trace must pass the exact affine
  voltage test (3.4), so base cycle rank must cover every common quotient
  direction before interval and residence constraints are even considered;
* the upper occurrence conflict has a literal Boolean obstruction and a
  quantitative hybrid remedy;
* the bounded suffix router is automatic on a concrete one-step Boolean
  face; in general its exact obstruction is the factor-restricted
  trapped-menu deficiency, and a bidirected Middle Levels corridor would
  close it at `O(sqrt(m))` scale, but the current parent still has to expose
  that literal typed corridor in the same occurrence state; and
* local module co-instantiation is exact on an interface tree, with the
  first cyclic obstruction explicitly identified.

The general conjecture remains open at the integral construction step.
