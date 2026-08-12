# Thirty-lane audited mathematical synthesis

Date: 2026-07-24

This note synthesizes the thirty independent lettered attacks A--Z and
AA--AD.  Every primary report was allowed to run to its own conclusion and
was then checked by another mathematical lane.  The detailed corrected
statements are recorded in items 1370--1415 of
`MATHEMATICAL_HANDOFF.md`; the first ten lanes also have the compact note
`MATH_ATTACK_FIRST_WAVE_SYNTHESIS_20260724.md`. The complete synthesis was
itself cross-audited in
`MATH_ATTACK_30_LANE_SYNTHESIS_AUDIT_20260724.md`; the present text includes
the audit's normalization and scope corrections.

## 1. Outcome

The thirty lanes did **not** prove

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor},
\]

and they did not change any exact numerical interval for \(k<20\).

The first wave produced two especially compact candidate sufficient
reductions.  The later waves have now separated them sharply:

1. the strongly anisotropic three-box ray theorem DRAY is **false**;
2. the adaptive Johnson-forest move-to-front route survives only in its
   weaker portal--trace form \(\mathrm{PTAD}_A\), while canonical strip
   implementations have a new residual-depletion ceiling.

The later waves also prove that the corrected near-baseline
component-noise gate is quantitatively false on every fixed nontrivial
Gaussian window.  These are route eliminations, not counterexamples to the
contiguous-OR conjecture.

They also established a large body of exact algebra locating the obstruction
more precisely. Averaged fractional marginals, signed lattice indices,
abstract quota divisibility, nested ownership before cyclic packaging,
coherent harmonic contraction, and reset accounting all have exact
solutions in their respective relaxations. They are not thereby removable
from every formulation: prescribed positive quotas can still fail, cyclic
packaging is open, component noise survives harmonic smoothing, and a
sublinear reset/path toll remains unproved. The common unresolved theme is
positive correlated selection, but the audited routes impose different
structures on that selection.

## 2. Exact finite status

For nonzero masks,

\[
\nu(1),\ldots,\nu(10)=1,2,4,7,12,21,37,72,128,254,
\qquad \nu(12)=926.
\]

The unresolved values and rigorous intervals are

\[
\begin{array}{c|c}
k&\nu(k)\\ \hline
11&[465,477]\\
13&[1719,1852]\\
14&[3434,3676]\\
15&[6438,7352]\\
16&[12873,14704]\\
17&[24313,29408]\\
18&[48623,58816]\\
19&[92381,117632].
\end{array}
\]

For the all-mask convention, add one.  The exact audit and all evidence
classifications are in `EXACT_K_LT20_STATUS_AUDIT_20260724.md`.

New finite endpoint-fork theorems impose strong necessary structure on one
fixed witness selection in a general near-equality word; the double-fork
conclusion additionally uses the recorded rank cap. At \(k=11\) those
hypotheses force hundreds of double-fork junctions and sharply constrained
low-rank components, but no contradiction. The separate lift-slack theorems
constrain tagged one-bit lifts with specified high/low run patterns, not
every equality witness. Neither theorem changes the lower bound 465.

## 3. Disproved endgame: DRAY and compact three-box CB

Let \(g_3(p,q,r)\) be the minimum range-maximum word length for the product
box \([0,p]\times[0,q]\times[0,r]\).  The former DRAY target asserted that,
for every fixed \(0<a<b\) and \(c>2b\),

\[
g_3(at,bt,ct)=(at+1)(bt+1)+o(t^2).
\]

This is false.  The audited finite witness-order argument now proves

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\]

The proof orders one middle-layer witness per endpoint, derives a
rank-capped start budget, extracts a short internal coordinate-threshold
run from every block of \(p+q+2\) middle targets, and uses one literal pin
to separate the neighboring negative witnesses.  Balanced block pairing
then telescopes the endpoint slack.  No common-pin or architecture
assumption is used.

Thus DRAY and the uniform compact-balanced three-box hypothesis CB are
impossible on a whole fixed-ratio cone.  The earlier hook/SCD implication
remains a valid conditional implication, but its local hypothesis cannot be
supplied.  Any product route must now share witnesses across different
product boxes or change the decomposition itself.

The complementary corridor analysis proves exact vertical-owner and
turnover laws and an architecture-scoped high-sharing barrier.  These
support the same diagnosis but are not needed for the unrestricted lower
bound.  See `MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md`, its independent
audit, and item 1406 of the handoff.

The same endpoint mechanism is dimension-free.  For a product base of
size \(B\), rank span \(P\), and long side \(r\ge P\), every local word
satisfies

\[
g_d\ge B+\left\lceil\frac{B(r-P)}{2r}\right\rceil.
\]

An exact shoulder correction remains positive at \(r=P\).  In four
dimensions this yields

\[
\liminf_{t\to\infty}
\frac{g_4(t,t,t,3t)-(t+1)^3}{t^3}\ge\frac{49}{512}.
\]

Therefore a uniform compact-balanced four-box width-plus-\(o(R^3)\) theorem
is also false on a positive boundary/dominance sector.  This does not touch
equal/polygon-interior four-boxes or high-degree cross-parent sharing.

## 4. The shortest direct literal endgame: \(\mathrm{AD}_A\)

This section uses the even-dimensional notation
\(W_e=\binom{2m}{m}\) and \(N_{1,e}=\binom{2m}{m-1}\). For fixed \(A>0\),
put \(H=\lceil A\sqrt m\rceil\). The exact adaptive MTF
theorem says that a Johnson walk has a one-step \(H\)-saturated literal lift
if and only if every internal positive coordinate run has length at least
\(H+1\), in the audited range \(H\le m/2\). Cutting every shorter run
produces a literal word with a linear,
not quadratic, run toll.

The remaining statement is:

> **\(\mathrm{AD}_A\).** There is one oriented spanning Johnson linear
> forest in \(J(2m,m)\), together with compatible cut, dummy, and
> residual-order choices, such that
> \[
> N_{1,e}-e=o(W_e)
> \]
> and
> \[
> H(c+\rho_H)+
> \sum_{q=2}^{H}
> (\widetilde M_q^-+\widetilde M_q^+)=o(W_e).
> \]
> Here \(c\) is the forest component count, \(\rho_H\) is the number of
> internal positive coordinate runs of length at most \(H\), cut at their
> entry edges. The number \(e\) counts certified forest edges whose lower
> colours are mutually distinct and whose upper colours are separately
> mutually distinct. The final sum is the actual deep-support defect after
> all compatible boundary choices.

The exact literal length bound is

\[
L_{\rm band}\le
W_e+(2H+1)(c+\rho_H)+2(N_{1,e}-e)
+\sum_{q=2}^{H}(\widetilde M_q^-+\widetilde M_q^+).
\]

Thus \(\mathrm{AD}_A\) for every fixed \(A\), followed by diagonalization
and the known tails, proves coefficient one without exact wreath balancing.
Unconstrained path splicing already makes \(Hc=o(W_e)\); the unsolved part is
simultaneously controlling short coordinate runs and deep supports.

This is the most direct literal formulation left by the attack. It improves
the explicit physical reset charge from \((H^2+2H)\rho_H\) to
\((2H+1)\rho_H\). It does not prove that the total loss caused by cutting is
linear: the adaptive support-defect term can still deteriorate on an
\(H^2\rho_H\) scale.

The second wave weakens this ledger further.  Exact MTF bridges between
successive path endpoint states replace one reset per component by the
directed Hamilton-path portal excess \(\mathfrak P_H\).  Missing masks over
all depths may be repaired by a common trace-cylinder functional

\[
\Phi_Z(\mathcal H)=
\sum_{R\subseteq Z}
\min\{h_R,\nu(2m-|Z|)+\mathbf1_{R\ne\varnothing}\},
\]

which satisfies

\[
\max_q M_q\le\Phi_Z\le\sum_qM_q.
\]

Thus the portal--trace theorem

\[
\mathfrak P_H+\Phi_Z(\mathcal H_H)=o(W)
\]

for every fixed \(A\) is sufficient for coefficient one.  Its strict
separation from raw defect summability is proved for abstract Gaussian-band
hole ledgers; realization of the separating pattern by an adaptive forest is
open.  This formulation still cannot hide a linear defect in any one rank.

## 5. Exact-factor endgames: several sufficient positive gates

Write \(n=2m+1\), \(W=\binom nm\),
\(N_q=\binom n{m-q}\), and
\(c_q=\lfloor W/N_q\rfloor\).  For an exact wreath factor \(F\), let
\(O_q(F)\) be its distance to the balanced integer load profile.  In every
fixed Gaussian window \(q\le A\sqrt m\), the \(c_q\) are bounded.

The following are exact:

\[
M_q(F)\le O_q(F)/c_q,
\]

and the floor-corrected collision energy \(\Phi_q\) dominates \(O_q\).
Fixed-window overload \(o(W)\) for every fixed \(A\) diagonalizes to MWB,
which gives the literal theorem with the audited tail construction.

The thirty lanes produced several sufficient formulations of the still
missing positive theorem.

### 5.1 Positive cut / RFEN

Exact component switching turns energy descent into a weighted component
Max-Cut.  The coherent Johnson-harmonic vector contracts by \(1-2/n\) per
greedily chosen transposition, and an \(O(n)\)-term frozen word gives a
constant contraction.  Exact martingale and integer-wall identities isolate
the remaining noise.

The unproved RFEN/wall inequality says that propagated component noise and
floor restitution cost only \(O_A(H_A\operatorname{Cat}_m)\) beyond the
coherent contraction.  If true, repeated integral leaf selection gives
fixed-window overload \(o(W)\).  Positive-cut LM\(_A\), stationary-class
SCOV\(_A\), SDP coherence, and RFEN are related sufficient routes, not
proved equivalent characterizations.

### 5.2 Adaptive Hall / cyclic alignment

Without cyclic packaging, one lower-bounded integral flow gives \(W\)
nested deletion flags that are perfectly floor/ceiling balanced at every
depth simultaneously.  Integrality, divisibility, nesting, and common
middle ownership are therefore not obstructions.

In the cyclic one-pass model, carried letters and sibling rewiring are
exactly understood.  Every point-star Hall cut is automatically safe, but
higher-order Hall cuts and repair distance remain open.  Abstract embedded
cube components have point defect zero and exponential orientation recourse;
a single allowed sibling rewire can amplify cost from 1 to \(2^d\).  These
are not packetized inside one exact factor and hence neither prove nor
disprove the existential alignment theorem.

### 5.3 Packet-Gain necklace rounding

This subsection uses the even-dimensional notation
\(W_{\rm even}=\binom{2m}{m}\), rather than the odd-factor \(W\) fixed at
the start of Section 5. Independent typed rounding has concentrated
collision defect

\[
(\sqrt\pi/e+o_{\Pr}(1))W_{\rm even}\sqrt m,
\]

so it cannot work.  An exact aligned two-necklace switch preserves the
entire middle and depth-one histograms and acts at deeper ranks by two signed
\(2\times2\) rectangles at every certified depth. It is a genuine
higher-depth primitive, but cannot
repair depth one and preserves all coordinate point margins.

The unproved Packet-Gain hypothesis asks for a support-feasible type-neutral
replacement whenever collision excess is linear, with a strictly favorable
unique-versus-hole count.  Integer descent under this hypothesis yields a
literal \(W_{\rm even}+o(W_{\rm even})\) word.  It is one sufficient
construction theorem, not an equivalent form of MWB.

### 5.4 Graver augmentation

The lifted Graver basis removes false local minima: relative to any better
exact factor, some applicable move improves the floor energy by at least a
\(1/\operatorname{Cat}_m\) fraction of the gap.  The same holds for exact
mobile-quota overload after auxiliary reoptimization.  Signed saturation
removes lattice obstructions.

This is comparison, not existence.  A cyclic, point-regular balanced
prescribed quota can lie outside the positive cone, and every signed lift
then needs negative mass \(\Omega(W/n^3)\).  Since MWB jointly chooses its
quota, that example does not lower-bound the mobile optimum.  The remaining
assertion is still that the positive optimum itself is \(o(W)\).

### 5.5 Hard-quota exceptional completion

The reciprocal quota weights have exact order

\[
\sum_{q=1}^{m-1}\frac1{c_q}
=(I+o(1))\sqrt m,
\qquad
I=\int_0^\infty\frac{dx}{\lfloor e^{x^2}\rfloor}.
\]

If one exact factor splits as \(F=G\sqcup B\), the same core \(G\) is
coordinatewise below balanced full-mass quotas at every controlled depth,
and the residual really is the exceptional wreath family \(B\), then

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le n|B|\sqrt{2\pi m}.
\]

Thus \(|B|=o(\operatorname{Cat}_m/\sqrt m)\) suffices, and
\(|B|=O(\operatorname{Cat}_m/m)\) gives error \(O(W/\sqrt m)\).
This implication to MWB requires one common split \(F=G\sqcup B\) and the
same core \(G\) below balanced full-mass quotas throughout every fixed
Gaussian window (or throughout one admissible growing window); separate
depthwise choices do not suffice.

Saturating one fixed middle-set star by a matching in the **full** wreath
hypergraph is exactly equivalent to a perfect factor. Distinct pairs inside
that star have relative codegree \(2/[m(m+1)]\). This improvement is only
projected: conflicts on the complementary side retain relative codegree
\(2/(m+1)\), and shallow quota resources already have \(2/m\) nested
correlations. The unproved theorem must simultaneously give the quantitative
leave, all hard quotas, full two-sided disjointness, and exact residual
completion.

The final integer-absorber part of this statement has now been removed on
every fixed Gaussian window.  For fixed exact factor and quotas, form the
survival-packet hypergraph whose vertices are wreaths and whose edges are
all \((\beta(q,S)+1)\)-subsets of the owner set of \((q,S)\).  A deleted
family is quota-safe exactly when it is a vertex cover.  If \(\vartheta\)
and \(\tau\) are the fractional and integral cover values and \(R\) is the
packet rank, then

\[
\vartheta\le\tau\le R\vartheta.
\]

For \(q\le A\sqrt m\), \(R=O_A(1)\).  The packet LP also has an exact
compressed cut dual, and directly satisfies

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}\le3nH\,\vartheta(F,\beta).
\]

Thus the remaining hard-quota theorem is the strictly weaker fractional
survival-packet gate
\(\vartheta=o_A(\operatorname{Cat}_m/\sqrt m)\), still inside one exact
factor with one common quota system.  Common-threshold rounding also shows
that integer recourse along a fractional exact-factor trajectory costs only
an \(A\)-dependent constant.

### 5.6 Global component-noise minimizer

For a global minimizer of the weighted exact-factor floor energy, let

\[
R_H(F)=\sum_{\tau}\sum_{C\in\mathcal C_\tau(F)}\sum_{q\le H}
\frac{\|u_{q,C}-w_{q,C}\|_2^2}{c_q},
\]

where unordered coordinate transpositions are counted once and all norms are
unnormalized counting norms.  Thus \(R_H\) is four times the aggregate fair
complete-side variance. Raw exact-factor histograms have fixed nonzero point
margins; their centered histograms have zero total and zero point margins,
which removes Johnson degrees zero and one. Hence
the sharp transposition inequality is

\[
\sum_\tau\|f-\tau f\|_2^2\ge4(n-1)\|f\|_2^2.
\]

Writing

\[
B_H=\sum_{q\le H}\frac{V_q^{\min}}{c_q},
\]

the exact minimizer consequence is

\[
\sum_{q\le H}\frac{O_q(F)}{c_q}
\le\frac{R_H(F)}{8(n-1)}-\frac12B_H.
\]

The formerly proposed sufficient gate was

\[
R_H(F)\le4(n-1)B_H+o(nW).
\]

For every fixed \(A\), this gate was imposed at a global minimizer of the
same \(H=\lceil A\sqrt m\rceil\) window objective.

The originally proposed \(2nB_H\) baseline forgot that the centered
histograms have zero point margins
and lies below the forced spectral floor. The corrected condition is a very
strong formal minimizer-only near-equality statement: it simultaneously requires
low floor energy, negligible aggregate fair-switch drift, and negligible
spectral mass above Johnson degree two.

This corrected gate is now **disproved**.  The sparse Boolean-
\(E_2\) stability theorem of item 1405 gives, at every same-window global
minimizer,

\[
R_H-4(n-1)B_H=\Omega_A(nW\sqrt m).
\]

Thus neither the generic \(2n\) target nor the spectrally corrected
\(4(n-1)\) near-equality target can close MWB.  The exact subgroup analysis
of item 1404 further shows that fixed aggregated multitransposition heat
collapses to global relabellings or preserves explicit orbit-profile floors;
even the point stabilizer restores all coherent smoothing as component
noise.  Adaptive recomputation or genuinely new perfect matchings remain
possible.  These no-go theorems do not by themselves refute RFEN,
LM\(_A\), or SCOV\(_A\), whose mechanisms include additional adaptive or
nonuniform structure.

## 6. What the thirty lanes rule out

The following conclusions are now rigorous within their stated scope.

- One isolated reset per queue atom plus all vertical slots in one ABKV edge
  cannot exceed depth \(o(\sqrt{\log m})\) at leading constant one within
  that audited certificate architecture.
- Exact-state portal sharing does not rescue the full cyclic-strip version
  of that architecture.  Residual-consuming strips save at most one letter
  from a full reset; with the same growing-uniformity matching hypothesis,
  \(W+o(W)\) again forces \(H=o(\sqrt{\log m})\).
- A profile-3 sparse local absorber cannot repair a linear shallow defect;
  that cleanup route needs a positive-density coarse rebundling or another
  nonlocal first stage.
- The canonical independent typed Bernoulli model at mean near one leaves a
  linear first-shadow defect. This is not a theorem about every randomized
  middle-matching algorithm.
- A separate \(o(W)\)-length appendage cannot repair a rank with more holes
  than its number of new endpoints; it may repair vertically aligned
  \(o(W)\) defects.
- Standard M-, M-natural-, and L-natural convexity fail on the positive exact
  factor fibre; Graver augmentation is the correct unrestricted discrete
  comparison tool.
- Fixed global coordinate matchings in the rotor/SCD lane have a positive
  Gaussian toll.  Mixed or phase-dependent frames are necessary there.
- Point margins, Hall feasibility, Johnson locality, and signed lattice
  saturation individually do not imply short positive transport in the
  audited abstract selector and signed-lattice relaxations; those examples
  are not positive packetized exact factors.
- Complete concentric rings, natural rasters, and globally ordered factors
  of the triangular shell all pay critical quadratic loss.
- More strongly, arbitrary three-box words on the full width plateau obey
  the unrestricted two-endpoint lower bound of item 1408.  Hence DRAY and
  the compact-balanced local three-box theorem are false, not merely blocked
  in the previously tested architectures.
- The obstructed three-box cone has positive SCD-height mass (exactly
  \(1/5\) after sorting for three equal blocks), so independent boxwise
  aggregation pays \(\Omega(W)\) excess.  Sparse bounded-degree cross-box
  portals cannot amortize it.
- The endpoint/shoulder dual extends to four boxes and gives cubic excess on
  every fixed closed-dominance ray, including \((t,t,t,3t)\).  Thus a
  uniform independently paid four-box coefficient-one theorem is false;
  equal/interior boxes and global cross-parent fusion remain open.
- Fixed aggregated multitransposition/subgroup heat cannot exploit coherent
  smoothing: connected support collapses the owner join, and even the point
  stabilizer restores the entire energy as component noise.  The corrected
  near-baseline gate is quantitatively impossible by Boolean-\(E_2\)
  stability.

These statements do not give a general lower bound against an arbitrary
global Boolean literal word.  The three-box endpoint theorem is an
unrestricted lower bound for its local product problem; the product and heat
conclusions explain why additional global sharing or adaptivity is required.

## 7. Repair and portal accounting

Signed-subcube repair has an exact entropy dual.  It can compress defects
across ranks when holes share dense signed faces, but it cannot hide a
macroscopic defect concentrated in one antichain rank.  A hereditary
dense-face peeling condition is the exact route-specific geometric target
for \(O(W)\)-sized hole families; it is not necessary for MWB or an
arbitrary literal word.

Exact integer orbit scaling settles divisibility, colour counts, connector
pairing, and Euler routing for rotor circulations. Every physical circuit is
nevertheless initialized separately, with audited charge at most
\(2Q\Phi\). The remaining rotor--SCD issue is one full integral SCD with
optimized fixed-window ordered-Hall/path-forest toll \(o(W_e)\), with every
initialization and reset charged. The adaptive MTF theorem gives a separate
unscaled literal statement for one finite Johnson forest.

High-degree global portals themselves now exist at the exact forced scale.
A relabelled global Boolean SCD has only \(O(HW/k)\) aggregate same-product-
box collisions in a radius-\(H\) band.  At \(H=\Theta(\sqrt k)\), one may
encode \(\Theta(W/\sqrt k)\) selected global flags in a literal word of
length \(\varepsilon W\), carrying \(\Omega(\varepsilon W)\) useful
endpoint--box incidences.  Conversely, the central-band rank span forces
\(\Omega(W/\sqrt k)\) such endpoints.  The remaining product/portal cost is
stateful: isolated arms still cost \(\Omega(W)\), so the arm updates must be
fused into the middle-owning MTF trajectory.

For canonical MTF pieces this fusion has a sharp residual constraint.  A
component that consumes its initial residual needs a bridge of at least
\(2H+1\), while a full reset costs \(2H+2\).  If portal excess and deepest
upper defect are both \(o(W)\) at Gaussian depth, only \(o(W/H)\) components
may be depleted, yet those few components must contain a positive fraction
of all middle owners and have average length \(\omega(H)\).  Thus the live
PTAD route requires very long support-rich components or a noncanonical
global trajectory; short residual-preserving pieces cannot suffice.

That positive escape is now realized below the Gaussian scale.  For
(H=o(\log m/\log\log m)), projected strip matching gives
(o(W/H)) residual-consuming components of length \(\omega(H)\), covering
all but \(o(W)\) middle owners and deepest-upper targets with total portal
excess \(o(W)\).  More generally, (r) selected signed ranks are covered
in (W+o(W)) whenever (rH\log\log m=o(\log m)).  The missing step is no
longer existence of long fused components, but extending simultaneous
distinct support from sparse rows to every row of a Gaussian window.

## 8. Lane-by-lane audited ledger

The thirty primary directions and their surviving content are:

| Lane | Direction | Audited outcome |
|---|---|---|
| A | absorption | hard quotas packetize exactly; bounded-rank fractional cover is the remaining gate |
| B | trade/Markov | signed trade connectivity does not give positive balancing |
| C | component heat | exact Max-Cut identity; positive cut remains open |
| D | discrepancy | aggregate orbit balance does not select one factor |
| E | cyclic synchronization | exact rank-isolated owner orientations; evolving Hall gate |
| F | three-box | unrestricted plateau endpoint dual; compact local coefficient one is false |
| G | rotor/SCD | exact path-forest toll with initialization charged; canonical SCD fails |
| H | four-box | boundary/dominance local coefficient one is false; equal/interior fusion remains open |
| I | entropy repair | exact dual; same-rank defect cannot be hidden |
| J | algebraic | signed lattice surjectivity; positivity absent |
| K | Catalan rebundling | one tail subcube is inert; whole cube remains possible |
| L | positive cut | exact parity-floor restitution; LM\(_A\) open |
| M | multitransposition | exact frozen-word/wall calculus; RFEN open |
| N | adaptive Hall | exact carry dynamics; packet thresholding removes integer recourse on fixed windows |
| O | prefix freezing | exact split flow; permanent-prefix route has a Boolean-owner obstruction |
| P | mesoscopic capacity | exact \(2q\) seam envelope; no productive-sign theorem |
| Q | coupled cycles | exact lower/upper colour tower; first band normalized |
| R | PBBS | exact local alternating-C8 balance; no density/cleanup theorem |
| S | rotor/SCD | exact extension and path-cover formulas; fixed-frame Gaussian obstruction |
| T | shell braid | literal factor-two word; ring/raster/ordered-factor no-go theorems |
| U | four-box spill | cubic local/parent barrier; only global high-degree sharing can escape |
| V | entropy geometry | exact route-specific face-cover dual and dense-face peeling criterion |
| W | necklace rounding | direct even route: exact higher-depth diamond; Packet-Gain open |
| X | dominant ray | DRAY is false; separate three-box aggregation incurs linear global excess |
| Y | stationary heat | exact adaptive switch-class calculus; low-energy class minimum unproved |
| Z | discrete convexity | standard discrete convexity fails; Graver optimality exact |
| AA | SDP/Max-Cut | exact floor hierarchy and SDP bounds; positive coherence open |
| AB | overlay expansion | exact owner-orbit leakage/fragmentation identities |
| AC | positive Graver | descent to the positive optimum; no bound on that optimum |
| AD | adaptive MTF fusion | exact bridge metric; strip portals deplete residuals; long-component fusion remains open |

## 9. Best compact prompts for a new mathematical solver

The former DRAY prompt must not be used: DRAY is false.  Two clean surviving
standalone problems are the following.

### Fractional survival-packet theorem

Fix \(A>0\), put \(H=\lceil A\sqrt m\rceil\), and let
\(t=\operatorname{Cat}_m\).  Construct one exact middle wreath factor
\(F\), one balanced quota system \(\beta_q\) for all \(q\le H\), and
weights \(x_E\in[0,1]\) on its wreaths such that

\[
\sum_{E\in P}x_E\ge1
\]

for every \((\beta_q(S)+1)\)-subset \(P\) of the owner set of every lower
target \((q,S)\), while

\[
\sum_{E\in F}x_E=o_A(t/\sqrt m).
\]

The audited packet theorem converts this directly into fixed-window MWB and
hence coefficient one after diagonalization.

### Stateful global-portal theorem

For fixed \(A\), put \(H=\lceil A\sqrt m\rceil\) in the even cube.  Build
one legal MTF trajectory through the middle owners whose portal excess plus
fixed-trace repair cost is \(o(W_e)\).  Equivalently, extract
\(W_e-o(W_e)\) distinct useful central portal targets along one legal
state walk with only \(o(W_e)\) connectors.  Canonical implementations must
use only \(o(W_e/H)\) depleted components, yet those components must be
super-\(H\)-long and contain a positive fraction of all owners.

Either theorem, with the proved reductions in the handoff, yields a complete
coefficient-one proof.  Neither is currently established, and they are not
exhaustive of Packet-Gain, rotor/SCD, or nonlocal exact-factor trades.

## 10. Bottom line

The thirty-lane campaign has not proved the conjecture, but it has removed
several misleading endgames.  Local width-optimal three-box braids and the
corresponding independently paid four-box boundary routes are impossible;
fixed component-noise heat and isolated/full-strip reset schemes are also
quantitatively blocked.

The surviving positive frontier is genuinely correlated and global:

\[
\boxed{\text{a small fractional survival-packet cover inside one exact factor}}
\]

or

\[
\boxed{\text{a stateful MTF/rotor trajectory fusing }\Theta(W/\sqrt k)
\text{ high-degree portals}.}
\]

The first has no remaining generic integrality or recourse gap on fixed
windows.  The second has the correct portal incidence available, but still
lacks distinct-target extraction along one middle-productive state walk.
These are sufficient routes, not known necessary characterizations; the
nonlocal trade and rotor/SCD lanes remain live alternatives.
