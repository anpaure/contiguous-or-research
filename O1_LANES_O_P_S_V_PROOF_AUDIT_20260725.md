# Proof-body audit: lanes O, P, S, and V

Date: 2026-07-25

All latest proof bodies requested for these four lanes were read in full.
This note records the mathematical verdicts; it does not promote any
conditional gate to a proof of constant one.

## O — Gaussian prefix freezing and stopping-depth rebundling

**Verdict: sound, with a live but unproved boundary-existence gate.**

The arithmetic saturation identity

\[
|Z_q|-D_q=\rho_q-R_q
\]

is exact.  Residual feasibility is used, in the correct direction, only
when deriving (D_q\le R_q) and the upper bound (|Z_q|\le\rho_q).
The Gaussian subinterval on which (c_q=1), its positive lower density
\(\rho_q/W\ge\gamma_A+o(1)\), and the Hardy-tail implication
\(R_q=o(W/\sqrt m)\) all have the right constants and uniform quantifiers.
Thus the robust-slack architecture really costs
\(\Omega_A(W\sqrt m)\).

The orbit-invariance statement correctly minimizes over resolutions
transported together with the factor.  Its independent-alignment lower
bound fixes the resolution before choosing the random relabelling; the two
quantifiers are not interchanged.  The cyclic span identity and the
disjoint mixed-star inequality are valid, with disjointness used at both
boundary-endpoint steps.

The stopping/rebundling report gives an exact row-state ILP and an exact
decorated-row perfect-matching equivalence.  Forest support is totally
unimodular.  The stated bad-component extension theorem is valid because
it explicitly assumes internal exact coverability of the whole bad
resource union; without that clause it would be false.  The one-rank Hall,
synchronous packet, and logarithmic multistar cuts have the correct
directions and constants.

Imported packet lower bounds are used only for their audited
\(\Theta(\operatorname{Cat}_m)\) scale comparison.  They are not used to
prove the central saturation theorem.  The remaining assertion—existence
of a low-cost singular boundary solution, equivalently a cheap balanced
literal endpoint factor—is explicitly unproved.

**Cap recommendation: retain.**  This is a distinct positive boundary
formulation plus a sharp no-go for robust-flow interiors.

## P — hard quotas and adaptive bridge release

**Verdict: sound architecture no-go; positive correlation theorem open.**

The disjoint three-owner forcing lemma is exact and integral.  The native
cube theorem uses genuinely invariant targets, so arbitrary dependent
component signs do not evade it.  The Catalan generating-function
constant

\[
\delta_{\rm inv}=107897/19784704
\]

checks from the cited independently audited recursive packet matching.
The fixed-position case split correctly protects
\(\operatorname{Cat}_{m-5}\) disjoint triples for every fixed position.
The exact hard-quota-to-literal-word ledger has the correct exceptional
scale (o(\operatorname{Cat}_m/\sqrt m)\).

In the AFR report, the private C8 effect really consists of the cancelling
transfers

\[
(3,1)\to(2,2),\qquad(1,1)\to(0,2),
\]

so the displayed subcube is exactly depth-one-floor-energy flat.  The
fixed-position half-(\ell^1\) ledger, mesoscopic block capacity, Catalan
tail bound, leakage-derivative identity, and global-minimum locking all
have the correct signs and quantifier order.  Locking does not refute an
additive-residue AFR theorem, as the report correctly states.

One harmless rate typo was found and corrected in P5:

\[
\log(W/N_q)=q(q+1)/m+O_A(m^{-1/2}),
\]

not (O_A(m^{-1})\), uniformly for (q\le A\sqrt m).  This is one mesh
step and does not change the (O_A(1)) floor-threshold exception count or
the Riemann-sum conclusion.

The surviving same-bridge leakage-correlation theorem is unproved.  The
lane supplies no current positive construction beyond exact motion and
capacity diagnostics.

**Cap recommendation: merge/archive.**  Preserve the invariant-packet
no-go and leakage identity in the retained AB/K bridge-packet lane.  If a
slot later opens, P is the strongest of the no-go-only reserve lanes.

## S — recursive SCD selection and endpoint rigidity

**Verdict: sound; standard recursion closed, nonstandard recursive Hall
gate remains live.**

The four child signatures are exhaustive, including the separately handled
radius-one boundary.  Every standard outer child is indeed a rotor source.
The clipped top radius is omitted, the prefix cost uses the sharp weight
\(2d\), and the Gaussian constant

\[
2\left(\int_0^A e^{-x^2}\,dx-Ae^{-A^2}\right)
\]

is correct.  The two-Lipschitz surgery calculation forces a linear number
of changed states in every typical annulus.

The integral pseudo-orbit/BTK example correctly separates statewise
marginals from arc-correlated coloring.  The local odd-cycle atom example
is a valid two-cover with no one-cover selector.  The exact one-layer
forced-target theorem is sound: injectivity of the two endpoint perfect
matchings really makes the two remaining rotor inequalities automatic.
The decomposition into paired-rainbow defect and Boolean-extendability
loss is therefore exact.  Recursive compatibility across layers remains
an explicit unproved hypothesis.

In S5, the endpoint slack identity and its cancellation to the
endpoint-incidence form are algebraically exact.  The corner
order-statistic bound has constant
\((3/4)6^{1/3}\), and division by the band scale gives the stated
\(t^{5/3}\) separation.  The global rank-packing inequality, degree-two
alternation/diamond classification, and safe-point theorem are sound.
The aggregate parity-ladder conclusions correctly remain conditional on
the near-minimal endpoint-incidence hypothesis (4.11); no implication from
near global word length is claimed.

The rotor chronology, BTK-stack, and static global-portal inputs used here
are cited as separately audited inputs and are used within their stated
scopes.

**Cap recommendation: retain.**  This lane closes a major tempting
architecture while leaving an exact, genuinely different recursive
matching target.

## V — fixed-kernel portals and target Hall

**Verdict: sound, but the stationary portal-metric route is closed.**

The full-mask separator isolates all nonfull ranks.  Within a productive
low-core component, rank (m+H) occurs at the unique interval length
\(2H+1\).  Initialization starts form nested unions and contribute at most
one target each at a fixed rank.  Therefore the all-interval bound

\[
|\operatorname{OR}_{m+H}|\le |\mathcal S_H^+|+(2H+1)C
\]

really counts every physical interval, not only designated witnesses.
Combined with the audited fixed-kernel translation theorem and its explicit
owner hypothesis, the constructed (W+o(W)\) word has only (o(W))
rank-(m+H\) support.  The common relabelling argument has the correct
probability quantifiers and cannot change this support cardinality.

The portal Hall report gives the exact clone-Hall deficiency formula.
Componentwise target-rainbowness yields

\[
|N(X)|\ge |X|+2H x_{\max},
\]

so two components satisfy (H\)-fold Hall.  The upper-depth-one anchor,
all-subset repetition-loss criterion, explicit three-state deficit
\(H-5\), and minimal-cut private-target inequality all check.  The
three-state pattern is correctly scoped as locally realizable, not proved
to coexist in one exact factor.

The imported fixed-kernel support collapse was checked against
`LONG_COMPONENT_MTF_CONSTRUCTION_20260725.md` and its cross-audit: it
explicitly assumes the product extensions contain (W-o(W)) owners, the
same hypothesis used here.  Componentwise rainbowness and the global
depth-one anchor are the audited odd-factor inputs used by the Hall file.

The positive Hall theorem extracts arbitrary supported targets.  It does
not cover a prescribed central band, and no (W/H\)-endpoint Hall set is
constructed.  Thus it does not survive as a direct constant-one route.

**Cap recommendation: archive after merge.**  Preserve the literal
support-collapse theorem in AD/H and the exact target-Hall criterion there.

## Relative ranking under a sixteen-thread cap

Among these four lanes:

1. **O — retain**;
2. **S — retain**;
3. **P — first reserve / merge then archive**;
4. **V — archive after merge**.

No file in these four lanes proves MWB, MWC, or
\(\nu(k)\le(1+o(1))W(k)\).
