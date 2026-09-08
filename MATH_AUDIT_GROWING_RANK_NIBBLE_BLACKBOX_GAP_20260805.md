# Growing-rank macro packing is not supplied by the current nibble black boxes

**Date:** 2026-08-05  
**Method:** parameter substitution into the stated matching theorems; no
computation or finite search  
**Status:** proof-safety audit.  This note rules out two tempting citations;
it does not rule out a macro-specific nibble proof.

## 1. The macro scale

For the fresh FIFO `h=2,3` macro hypergraph, let `R` be the number of
resources in one macro.  Then

\[
                         R=\Theta(d),\qquad d=\Theta(\sqrt{k}).
\]

The exact fractional factor is regular on both resource shores.  The
proved same-shore pair-codegree estimate has the scale

\[
       \delta_2:=\frac{D_2}{D}=O\!\left(\frac d{k^2}\right)
                    =O(d^{-3}).                              \tag{1.1}
\]

Thus the natural stopping scale of a tailored nibble is

\[
                         R^2\delta_2=O(d^{-1}),               \tag{1.2}
\]

which is exactly the `O(W/d)` leave required by the separator ledger.  The
parameter coincidence (1.2) is useful evidence, but it is not itself a
matching theorem.

## 2. The fixed-uniformity quantifier does not diagonalize

Pippenger--Spencer, Alon--Kim--Spencer, and the usual pseudorandom matching
theorems are stated with the uniformity fixed before the degree threshold is
chosen.  Their assertions have the quantifier form

\[
 \forall R,\varepsilon\ \exists D_0(R,\varepsilon),
\]

not one uniform estimate on `D_0` along `R=Theta(d)`.  Knowing that the
labelled macro degree tends to infinity does not imply

\[
                         D(k)\ge D_0(R(k),1/d(k)).             \tag{2.1}
\]

The unknown right side may grow faster than the explicit macro degree.
Consequently a fixed-rank theorem cannot be invoked by saying that every
individual dimension is finite and then taking a diagonal sequence.

## 3. Why the new full-codegree theorem still gives no usable leave

Gould--Kelly, *Advancing the Rödl Nibble* (arXiv:2511.11375), Theorem 1.4,
assumes

\[
          1/D\ll1/A\ll\gamma\ll1/R
\]

and gives a leave bounded by

\[
                         n B^{-1+\gamma}\log^A D,             \tag{3.1}
\]

where, suppressing the regularity bottleneck,

\[
 B\le \min\left\{
       \sqrt{D/D_2},
       \min_{4\le j\le R}(D/D_j)^{1/(j-1)}
       \right\}.                                             \tag{3.2}
\]

Even granting the still-unproved optimal all-order macro estimates

\[
                         D_j/D\le d^{-\Omega(j-1)},           \tag{3.3}

\]

equation (3.2) would give only `B=Theta(d)` at the target scale.  But the
FIFO orbit has

\[
                         \log D=\Theta(d\log k)
\]

up to constants depending on the macro presentation.  Hence for every
admissible `A>1`, and a fortiori under the displayed hierarchy,

\[
                    B^{-1+\gamma}\log^A D
                    \not=O(1/d).                             \tag{3.4}

Indeed the polylogarithmic factor alone grows faster than the available
linear bottleneck `B`.  The theorem is therefore quantitatively too lossy
even before addressing its fixed-uniformity hierarchy.

## 4. Vu's higher-codegree theorem is still too weak at the proved hierarchy

Vu, *New bounds on nearly perfect matchings in hypergraphs: Higher
codegrees do help* (Random Structures & Algorithms 17 (2000), Theorem
1.2.2), gives the following relevant parameter test.  For an
`(K+1)`-uniform `D`-regular hypergraph, choose majorants

\[
 D=D_1\ge D_2\ge\cdots\ge D_s.
\]

If, among other conditions,

\[
 x^3\le {D_j\over D_{j+1}}\quad(j<s),
 \qquad
 x^{K-s+2}\le {D_{s-1}\over D_s},                         \tag{4.1}
\]

then the uncovered set is `tilde O(n/x)`, with the suppressed
polylogarithmic exponent depending on the fixed theorem parameters.

Suppose the requested all-order macro estimate is proved only at the
currently targeted scale

\[
                         D_j/D\le(C/d)^{j-1}.                \tag{4.2}
\]

The consecutive ratio supplied by (4.2) is only `Theta(d)`.  The first
condition in (4.1) therefore permits at best

\[
                         x=O(d^{1/3}),                       \tag{4.3}

\]

which yields `tilde O(n d^(-1/3))`, not the required `O(n/d)` leave.
The omitted polylogarithmic factor only worsens the comparison.  To take
`x=Theta(d)`, Vu's condition would require a uniform consecutive
codegree drop of order `d^3` through the selected hierarchy.  Pair
codegrees do have that first-step scale, but it is not an all-order fact:
near-saturated geodesic clusters can have much smaller consecutive drops.

Thus higher codegrees are relevant to the bespoke proof, but Vu's stated
black box does not convert the presently targeted hierarchy into the
separator-scale leave.  Its degree threshold also retains the fixed-rank
quantifier from Section 2.

## 5. Linearization also loses the required scale

Randomly thinning until every pair-codegree is `O(1)` leaves effective
degree at most

\[
                         D/D_2=\Theta(d^3)                    \tag{4.1}

\]

at the scale of (1.1).  The Alon--Kim--Spencer simple-hypergraph bound has
the characteristic factor

\[
                         (d^3)^{-1/(R-1)}
                         =\exp\!\left(-O(\log d/d)\right),    \tag{4.2}

\]

which tends to one, not to `O(1/d)`.  Thus ``thin to linear, then apply
AKS'' cannot close the macro factor either.

## 6. Exact surviving target

The black-box failure leaves a sharp constructive theorem rather than an
undefined appeal to pseudorandomness:

> **Macro-specific quantitative nibble.**  Prove the full conditional
> codegree/concentration estimates for the labelled `h=2,3` orbit and run
> the random greedy process down to residual density `C/d`, while retaining
> the prescribed two-shore ratio, the separator reserve, and a connected
> macro-component graph.

The scale (1.2) shows why this target is plausible.  A proof must exploit
the synchronized-chain orbit beyond pair codegrees; none of the theorems
audited above supplies it automatically.

## 7. Dependency

The macro construction and the proved pair-codegrees are in

`MATH_THEOREM_FRESH_FIFO_BLOCK_CHAIN_KERNEL_AND_PAYLOAD_ATLAS_GATE_20260805.md`.
