# Ballot twisted cycles after geodesic correction: exact conditional supply ledger

Date: 2026-07-26

Method: pure mathematics only.

## 0. Authoritative outcome

Let \(R\) be the fatal Catalan parent scale and \(s\) the rank of a
candidate twisted packet.  Put

\[
 C_n=\operatorname {Cat}_n,\qquad
 \theta={C_R\over p},\qquad
 \delta_\theta={1\over2}-{1\over\theta}.
\tag{0.1}
\]

Then

\[
 4\le\theta<16-{24\over R+1},\qquad
 {1\over4}\le\delta_\theta<{7\over16},
\tag{0.2}
\]

and one aligned fatal parent has certified demand

\[
                         D_R(\theta)=\delta_\theta C_R.
\tag{0.3}
\]

There is a gate before any supply comparison.

Let \(J\) have size \(2s\), let \(P\in\binom Js\), and suppose a nominal
\(s\)-step slab has endpoints

\[
 A=O_L\cup P,\qquad
 B=O_R\cup(J\setminus\tau(P)).
\tag{0.4}
\]

Writing \(e=|O_L\setminus O_R|\), the Johnson distance is

\[
 \boxed{
 d_J(A,B)=e+|P\cap\tau(P)|.}
\tag{0.5}
\]

Every contiguous segment of a minimum wreath is geodesic.  Hence an
\(s\)-step physical slab requires, row by row,

\[
 \boxed{
 e=|P\setminus\tau(P)|.}
\tag{0.6}
\]

In the ordinary fixed-exterior slab, \(O_L=O_R\), so \(e=0\) and

\[
                         \boxed{\tau(P)=P\quad\text{for every row}.}
\tag{0.7}
\]

Therefore every nonidentity ballot cycle has exactly zero physical
realizations in an ordinary fixed-exterior \(s\)-step wreath slab.
Serial repetition cannot repair this: the first twisted segment is already
nongeodesic, and metric defects are nonnegative and additive.

The cycle catalogue is consequently an abstract \(b\)-factor/path-ledger
catalogue unless one constructs a genuinely exterior-moving packet which
satisfies (0.6), owns every ambient state and colour exactly once, and
includes the full crossing-collar carrier.

The rest of this note gives the exact supply/demand inequality
conditional on such a construction.  It does not assert that one exists.

Assume \(2s\le R\).  The exact maximum row-disjoint packing of literal
size-\(s\) boundary contexts in one fatal parent is

\[
 \boxed{
 N_{R,s}=2C_{R-s}-C_sC_{R-2s}.}
\tag{0.8}
\]

This already subtracts the overlap of the left and right parent banks.
Define

\[
                         \lambda_{R,s}={C_sN_{R,s}\over C_R}.
\tag{0.9}
\]

For each directed cycle length \(3\le\ell\le s+1\), let

* \(Q^{\rm ext}_{s,\ell}\) be the number of strand-admissible cycle-stage
  certificates in one local packet which have a proved exterior-moving
  realization satisfying (0.6) and the full ambient collar ledger;
* \(J_{R,s,\ell}\) be the number of complete order-\(\ell\) serial atoms
  retained in one fatal parent after every parent-context overlap and
  serial compatibility condition;
* \(M^{\rm full}_{s,\ell}\) be the carrier mass of one physical
  exterior-moving cycle stage, including both its local windows and all
  crossing collars.

Every complete atom uses \(\ell\) stages.  Define the exact utilization
factor

\[
 \boxed{
 \kappa_{R,s,\ell}
 ={\,\ell J_{R,s,\ell}\over
    N_{R,s}Q^{\rm ext}_{s,\ell}}}
\tag{0.10}
\]

when \(Q^{\rm ext}_{s,\ell}>0\), and put \(\kappa=0\) otherwise.

If all stages are charged to one parent/certificate resource, then

\[
                         \boxed{\kappa_{R,s,\ell}\le1.}
\tag{0.11}
\]

For an internal conveyor, one complete atom consumes \(\ell\) cycle
certificates.  For external repetition, it consumes \(\ell\) parent
placements.  Thus the formal serial factor \(\ell\) is paid exactly once
and may not also be treated as free carrier amplification.

Let \(G_{\rm joint}\) be the actual cap descent of one complete integral
choice after every cycle length, physical target collision, background,
and crossing window has been combined.  Define

\[
 \Gamma_{R,s}
 ={G_{\rm joint}\over
 N_{R,s}\sum_{\ell=3}^{s+1}
 \kappa_{R,s,\ell}Q^{\rm ext}_{s,\ell}
                         M^{\rm full}_{s,\ell}},
\tag{0.12}
\]

with value zero if the denominator vanishes.  The hinge is
one-Lipschitz, so \(0\le\Gamma_{R,s}\le1\).  This is one joint quotient,
not a product of marginal correlation estimates.

The exact conditional supply/demand inequality is

\[
 \boxed{
 \Gamma_{R,s}\lambda_{R,s}
 \sum_{\ell=3}^{s+1}
 \kappa_{R,s,\ell}
 {Q^{\rm ext}_{s,\ell}\over C_s}
 M^{\rm full}_{s,\ell}
 \ge\delta_\theta.}
\tag{0.13}
\]

For the ordinary fixed-exterior slab, (0.7) gives

\[
                         Q^{\rm ext}_{s,\ell}=0
                         \qquad(\ell\ge3),
\tag{0.14}
\]

so the left side of (0.13) is zero.  This is the primary decision.

There is also a corrected dense abstract ballot bank.  The canonical
factor contains

\[
                         \boxed{C_{s-3}}
\tag{0.15}
\]

pairwise vertex-disjoint clean suffix \(C_8\) routers.  They are
strand-admissible as abstract path-factor toggles, act on four root
strands, and have order four.  But (0.7) prevents them from being ordinary
fixed-exterior wreath packets.

Optimistically suppose every one of these routers acquires a valid
exterior-moving realization.  Put

\[
                         c_s={C_{s-3}\over C_s}
                         ={1\over64}(1+O(s^{-1})).
\tag{0.16}
\]

Then their exact conditional requirement is

\[
 \boxed{
 \Gamma_{R,s}\kappa_{R,s,4}
 \lambda_{R,s}c_s M^{\rm full}_{s,4}
 \ge\delta_\theta.}
\tag{0.17}
\]

Since

\[
 \lambda_{R,s}
 ={2\over\sqrt\pi s^{3/2}}(1+o(1))
\tag{0.18}
\]

for \(s=o(R)\), the hard-endpoint carrier threshold is

\[
 \boxed{
 M^{\rm full}_{s,4}
 \ge
 \left({14\sqrt\pi\over\Gamma_{R,s}\kappa_{R,s,4}}
       +o(1)\right)s^{3/2}.}
\tag{0.19}
\]

The local fixed-coordinate part of one \(C_8\) stage affects only four
rows and at most \(2s+1\) cyclic starts per row:

\[
                         M^{\rm loc}_{s,4}\le4(2s+1).
\tag{0.20}
\]

If no additional collar mass is proved, its best possible
hard-overshoot ratio is

\[
 \boxed{
 \mathcal R^{\rm loc}_{C_8}(R,s)
 \le {16\over7}\lambda_{R,s}c_s\,4(2s+1)
 =\left({4\over7\sqrt{\pi s}}+o(1)\right).}
\tag{0.21}
\]

It tends to zero.  Thus the dense suffix bank is still short at the
growing-\(D_s\) parent scale if only its local carrier is counted.

An exterior-moving escape is not disproved by (0.21), because its collars
are part of the packet.  What is required is the sharp lower bound

\[
 \boxed{
 M^{\rm collar}_{s,4}
 \ge
 \left({14\sqrt\pi\over\Gamma\kappa}+o(1)\right)s^{3/2}
 -4(2s+1).}
\tag{0.22}
\]

No present theorem supplies such collar mass with a favourable joint
sign, exact ambient ownership, and serial closure.

Hence the corrected verdict is:

1. **Ordinary fixed exterior:** impossible statewise; supply is zero.
2. **Abstract ballot ledger:** dense clean \(C_8\) routers exist, but
   they are not physical minimum-wreath packets.
3. **Conditional exterior-moving model:** local carrier remains short by
   \(\Theta(\sqrt s)\); overcoming the hard Catalan overshoot requires
   full per-stage carrier mass at least \(14\sqrt\pi\,s^{3/2}\), adjusted
   by the joint factors \(\Gamma\kappa\).
4. No impossibility is inferred for a future exterior-moving construction
   whose fully audited collars meet (0.22).

## 1. Proof of the geodesic gate

Let the ambient row states have size \(m\).  The exterior sets in (0.4)
have size \(m-s\) and are disjoint from \(J\).  Since the two endpoint
states have equal size,

\[
                         |O_L\setminus O_R|
                         =|O_R\setminus O_L|=e.
\tag{1.1}
\]

Their intersection is

\[
 (O_L\cap O_R)
 \mathbin{\dot\cup}
 \bigl(P\cap(J\setminus\tau(P))\bigr).
\tag{1.2}
\]

It has size

\[
 (m-s-e)+(s-|P\cap\tau(P)|)
 =m-e-|P\cap\tau(P)|.
\tag{1.3}
\]

Therefore

\[
 d_J(A,B)=m-|A\cap B|
          =e+|P\cap\tau(P)|,
\tag{1.4}
\]

which proves (0.5).

A minimum wreath row is a Johnson geodesic from an \(m\)-set to its
complement.  Every contiguous subpath is geodesic: otherwise replacing
that subpath by a shorter path would shorten the whole complement path
below its Johnson distance \(m\).  Hence the slab in (0.4) has distance
exactly \(s\).  Equation (1.4) gives

\[
 e=s-|P\cap\tau(P)|=|P\setminus\tau(P)|,
\tag{1.5}
\]

proving (0.6).

When \(O_L=O_R\), \(e=0\), so
\(|P\cap\tau(P)|=s\) and \(\tau(P)=P\).  This proves (0.7).

More generally, a physical exterior-moving realization must exchange
exactly the following coordinates along each row:

\[
\begin{aligned}
 \text{deleted: }&
 (O_L\setminus O_R)
 \mathbin{\dot\cup}(P\cap\tau(P)),\\
 \text{inserted: }&
 (O_R\setminus O_L)
 \mathbin{\dot\cup}
 \bigl(J\setminus(P\cup\tau(P))\bigr).
\end{aligned}
\tag{1.6}
\]

Both sets have size \(s\) under (1.5).  Thus exterior motion changes the
literal exchange menu.  The local \(X/Y\) palette cannot simply be pushed
through a common fixed exterior; every ambient state, colour, and crossing
window must be rechecked occurrence by occurrence.

For disjoint fixed-exterior twisted segments, the excess over global
geodesic length is at least

\[
 \sum_i|P_i\setminus\tau_i(P_i)|.
\tag{1.7}
\]

This remains nonnegative even if the formal endpoint permutations
multiply to one.  It proves that serial inverse twists cannot repair the
ordinary slab.

## 2. The corrected cycle catalogue

The outgoing ballot functional graph has

\[
 Z_s={s(s-1)\over s+2}C_s
\tag{2.1}
\]

eligible \((s-1)\)-cores.  A directed functional cycle is not
automatically alternating in the full path factor: a proposed new
half-edge may already be the selected incoming edge.

The exact phase-labelled criterion is:

\[
 \boxed{
 \text{a directed outgoing cycle is factor-alternating}
 \iff
 \text{its selected states lie on pairwise distinct root strands}.}
\tag{2.2}
\]

Hence every valid outgoing cycle is clean.  The old greedy count

\[
 {s-1\over(s+1)(s+2)}C_s
\tag{2.3}
\]

is a count of edge-disjoint outgoing-cycle certificates, not by itself a
count of physical twisted packets.

The stronger explicit suffix construction gives the dense family (0.15).
Its four cut phases, in cyclic order, are

\[
                         (s-3,s-1,s-2,s-3),
\tag{2.4}
\]

and toggling produces new row semilengths

\[
                         s,\quad s+2,\quad s-1,\quad s-1.
\tag{2.5}
\]

Their sum is \(4s\).  Thus the router is orbit-length balanced for its
abstract four-cycle endpoint action.  Four coherent copies satisfy the
formal monodromy and length sums:

\[
                         \tau^4=1,\qquad
                         \sum_{\operatorname {Orb}(\tau)}q=4s.
\tag{2.6}
\]

Equations (2.5)--(2.6) do not overcome (0.7).  They are statements about
the abstract open path ledger.  Literal promotion requires exterior
movement satisfying (0.6) on every one of the four rows.

## 3. Serial-copy and parent-context accounting

Suppose a physical exterior-moving stage has been constructed.  A
complete order-\(\ell\) atom uses \(\ell\) such stages.

### 3.1 Internal conveyor

If all stages lie in one combined parent packet, a fixed supply of
\(Q^{\rm ext}_{s,\ell}\) stage certificates supports at most

\[
                         {Q^{\rm ext}_{s,\ell}\over\ell}
\tag{3.1}
\]

complete serial atoms per parent placement.  Thus

\[
                         \ell J_{R,s,\ell}
                         \le N_{R,s}Q^{\rm ext}_{s,\ell}.
\tag{3.2}
\]

### 3.2 External copies charged to one parent bank

If one certificate label is repeated in \(\ell\) exterior-moving slabs,
each complete placement consumes \(\ell\) members of the parent bank.
Hence at most \(N_{R,s}/\ell\) placements are available, and again (3.2)
holds.

These are the two standard proofs of \(\kappa\le1\).  A hybrid
construction satisfies the same bound after every stage is charged to
the certificate-parent incidence it consumes.

The exact parent count \(N_{R,s}\), rather than \(2C_{R-s}\), is essential.
For every middle filling in \(D_{R-2s}\), the left and right packet
families form a \(K_{C_s,C_s}\) row-conflict component, so one complete
shore is lost.

If a proposed exterior-moving atlas supplies additional physical stage
layers, its combined footprint must be counted directly.  Define
\(\kappa\) by (0.10) using that count.  Independent Catalan holes cannot
be credited as serial powers: they act as

\[
 (P_1,\ldots,P_\ell)
 \longmapsto(\tau P_1,\ldots,\tau P_\ell),
\tag{3.3}
\]

not as \(P\mapsto\tau^\ell P\).

Across the full dimension there are

\[
                         H_{m,R}={1\over2}{2(m-R)\choose m-R}
\tag{3.4}
\]

aligned fatal parents.  Both demand and supply acquire this factor, so it
cancels from (0.13).  If these ambient parents overlap, replace
\(H_{m,R}J_{R,s,\ell}\) by the actual globally retained number; this can
only lower \(\kappa\).

## 4. Full carrier mass and the master inequality

For a genuinely exterior-moving stage, decompose

\[
                         M^{\rm full}_{s,\ell}
                         =M^{\rm loc}_{s,\ell}
                          +M^{\rm collar}_{s,\ell}.
\tag{4.1}
\]

Here \(M^{\rm collar}\) includes every affected window meeting an exterior
exchange in (1.6), with its literal physical target and unaffected
background.  It is not permissible to assign those windows the old
fixed-context carrier.

The purely local occurrence bound is

\[
                         M^{\rm loc}_{s,\ell}
                         \le\ell(2s+1).
\tag{4.2}
\]

There is no certified analogous bound or favourable sign for
\(M^{\rm collar}\) in the present library.  It must remain explicit in
the ledger.

There are \(J_{R,s,\ell}\) complete serial atoms, each with \(\ell\)
stages.  Their total nominal carrier mass is

\[
\begin{aligned}
 \mathcal M_{R,s}
 &=\sum_{\ell=3}^{s+1}
 J_{R,s,\ell}\ell M^{\rm full}_{s,\ell}\\
 &=N_{R,s}\sum_{\ell=3}^{s+1}
 \kappa_{R,s,\ell}Q^{\rm ext}_{s,\ell}
                         M^{\rm full}_{s,\ell}.
\end{aligned}
\tag{4.3}
\]

The second equality is the definition of \(\kappa\).  It shows exactly
where the serial factor is spent.

By definition of the joint physical coefficient,

\[
                         G_{\rm joint}
                         =\Gamma_{R,s}\mathcal M_{R,s}.
\tag{4.4}
\]

Repairing one fatal parent requires

\[
                         G_{\rm joint}
                         \ge\delta_\theta C_R.
\tag{4.5}
\]

Divide by \(C_R\) and use
\(N_{R,s}/C_R=\lambda_{R,s}/C_s\).  This proves (0.13).

The Catalan normalization is

\[
 \lambda_{R,s}
 =a_s(2-a_s)
 \left(1+O\left({s\over R}+{1\over R-2s}\right)\right),
 \qquad
 a_s={C_s\over4^s}
 ={1\over\sqrt\pi s^{3/2}}
 \left(1-{9\over8s}+O(s^{-2})\right).
\tag{4.6}
\]

## 5. Dense \(C_8\) quantitative audit

The abstract suffix bank has \(C_{s-3}\) routers.  If all receive one
physical exterior-moving realization and are packed with a common
\(\kappa\), then (0.13) specializes to (0.17).

The exact finite carrier requirement is

\[
 \boxed{
 M^{\rm full}_{s,4}
 \ge
 {\delta_\theta\over
  \Gamma_{R,s}\kappa_{R,s,4}
  \lambda_{R,s}(C_{s-3}/C_s)}.}
\tag{5.1}
\]

Since

\[
 {C_{s-3}\over C_s}
 ={s(s-1)(s+1)\over
  8(2s-1)(2s-3)(2s-5)}
 ={1\over64}(1+O(s^{-1})),
\tag{5.2}
\]

equation (5.1) becomes (0.19) at
\(\theta\uparrow16\).

If only the local mass (0.20) is credited, the exact hard-endpoint ratio,
for fixed \(s\) and \(R\to\infty\), is

\[
 \boxed{
 \mathcal R^{\rm loc}_{C_8}(s)
 \le {2s+1\over7}\,a_{s-3}(2-a_s),}
\tag{5.3}
\]

because \(a_s(C_{s-3}/C_s)=a_{s-3}/64\).  In particular

\[
 \mathcal R^{\rm loc}_{C_8}(s)
 ={4\over7\sqrt{\pi s}}(1+o(1)).
\tag{5.4}
\]

Thus the positive Catalan fraction of abstract routers does not overcome
the \(s^{-3/2}\) density of literal parent packets.  Its local per-router
mass is only \(O(s)\), while (5.1) requires
\(\Theta(s^{3/2})\).

The collar requirement (0.22) is not a formal bonus.  It must be proved
from the exterior exchange menu (1.6), with all of the following:

1. one literal ambient owner for every intermediate state and colour;
2. exact accounting for windows crossing the moving boundary;
3. one coherent order-four label conveyor;
4. the orbitwise row-length balance (2.6); and
5. a joint cap-reducing sign after unaffected backgrounds.

Without these five statements, \(M^{\rm collar}\) must be set to zero and
the route is short by (5.4).

## 6. Sparse ballot-bank comparison

For completeness, the older edge-disjoint extraction has size

\[
                         b_sC_s
 ={s-1\over(s+1)(s+2)}C_s.
\tag{6.1}
\]

If every raw certificate were physically realizable, all were assigned
the most favourable length, and the full carrier had only its local
part, then its hard-endpoint ratio would satisfy

\[
 \mathcal R_{\rm sparse}^{\rm loc}(R,s)
 \le {16\over7}\lambda_{R,s}
       {(s-1)(2s+1)\over s+2}
 =\left({64\over7\sqrt{\pi s}}+o(1)\right).
\tag{6.2}
\]

This also tends to zero.  The dense \(C_8\) theorem is structurally
stronger because it proves clean strand admissibility at positive Catalan
density, but neither abstract bank crosses the geodesic gate.

## 7. Hereditary PCap form

Let \(I\) be a set of hereditary serviced depths and \(d_q\) the
certified defect per fatal parent at depth \(q\).  Put

\[
 \bar\delta_I={1\over|I|C_R}\sum_{q\in I}d_q.
\tag{7.1}
\]

Let \(M^{\rm full}_{s,\ell,I}\) be the average full carrier mass of one
physical exterior-moving stage over the same depths.  Define one joint
\(\Gamma_{R,s,I}\) only after a common serial choice has been made at
every depth.  Then

\[
 \boxed{
 \Gamma_{R,s,I}\lambda_{R,s}
 \sum_{\ell=3}^{s+1}
 \kappa_{R,s,\ell}
 {Q^{\rm ext}_{s,\ell}\over C_s}
 M^{\rm full}_{s,\ell,I}
 \ge\bar\delta_I.}
\tag{7.2}
\]

Demand and available stage occurrences acquire the same factor \(|I|\).
Thus hereditary repetition does not repair a deficient constant.
Separately optimal collar signs at different depths cannot replace the
single joint coefficient in (7.2).

For the ordinary fixed-exterior source, \(Q^{\rm ext}=0\), so (7.2) has
zero left side at every depth.

## 8. Exact remaining theorem

A positive twisted-cycle route now requires a construction, not another
abstract cycle count.  It must provide:

1. exterior-moving endpoints satisfying
   \[
   |O_L(P)\setminus O_R(P)|
       =|P\setminus\tau(P)|
   \]
   on every active row;
2. a complete ambient \(X/Y\), seam, and crossing-collar ownership ledger;
3. a serial packing count \(J_{R,s,\ell}\), hence a proved
   \(\kappa_{R,s,\ell}\);
4. full carrier mass \(M^{\rm full}_{s,\ell}\), including the collars;
5. one joint physical retention coefficient \(\Gamma\); and
6. inequality (0.13).

For the dense suffix \(C_8\) bank, the quantitative target is exactly
(5.1), asymptotically (0.19).  The known local carrier misses it by
\(\Theta(\sqrt s)\).  A full collar theorem meeting (0.22) would evade
that scalar obstruction only if it escapes the bounded-width
row-congestion invariant in
MATH_THEOREM_C8_CROSSING_COLLAR_AMPLIFIER_OBSTRUCTION_20260726.md.
That theorem rules out disjoint and \(o(\sqrt s)\)-congestion collar
amplifiers. The remaining high-congestion bounded-span case is closed by
MATH_THEOREM_C8_HIGH_CONGESTION_OVERLAY_DICHOTOMY_20260726.md: coupled
reuse forces \(\Xi=\Omega(\sqrt s)\), and decoupled reuse is counted only
once. Only a macroscopic-footprint construction with a recomputed parent
density remains outside this obstruction.

Accordingly, all previous positive language about literal fixed-exterior
serial twisted packets is retracted.  What survives is only the conditional
exterior-moving supply ledger above.
