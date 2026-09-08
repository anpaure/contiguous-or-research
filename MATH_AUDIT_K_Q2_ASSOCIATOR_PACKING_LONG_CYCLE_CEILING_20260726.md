# Audit of the Q2-associator packing and long-cycle ceiling

Date: 2026-07-26

Audited file:
MATH_ATTACK_K_Q2_ASSOCIATOR_PACKING_AND_LONG_CYCLE_CEILING_20260726.md.

Method: pure mathematics only.

## 0. Verdict

The packet packing, general fixed-frame Hamming-row \(W_1\) estimate, and
odd-sector Gaussian demand are valid.  The collar conclusion is valid only
for the explicitly stated collar-deletion or serial-slab realization; it is
not a universal lower bound against a fused braid.

There is one useful sharpening.  On the fully product-transversal \(Q_2\)
tensor, the exact associator ledger improves the general \(W_1\) ceiling by
a factor of three.  In particular the unsuspended sibling-block tensor has
maximum mean type drift \(q/3\), whereas the uniform depth-\(q\) target law
requires \(q/2+O_A(1)\).  Thus that specific tensor already fails at the
type-law level before its \(\Theta(W)\) standard collar is charged.  This
sharpening does not apply automatically to an arbitrary radius-\(t\)
pair-geodesic Hamming row whose phase assignment may correlate with the
locally decreasing states.

## 1. The rowwise \(W_1\) normalization

Let \(P'\) be at matching-switch distance at most \(t\) from \(P\).  Every
recoupling removes at most two old matching edges and inserts at most two new
ones, so

\[
                         |P'\setminus P|\le 2t.
\]

If a \(C_{2h}\) row has \(b\) active directions outside \(P\), every such
direction occurs twice in its \(\pi\pi\) word and every occurrence belongs
to exactly \(q\) cyclic \(q\)-windows.  Since deleting one direction can
break at most one full \(P\)-pair,

\[
 \sum_{i=0}^{2h-1}
 \bigl(f_P(X_i)-f_P(L_i^{(q)})\bigr)
 \le 2qb\le 4qt.
\]

There are \(G/(2h)\) rows, so the owner-to-output coupling gives exactly

\[
 \boxed{\mathsf W_1(\nu_{q,G},V_G)\le {2tq\over h}G.}
\]

No factor two is missing.  Dependence among rows and overlap among a
sequential list of recouplings do not affect this conclusion provided every
completed row is still pair-geodesic in one final frame lying in the
radius-\(t\) matching ball.  A row whose frame changes along the cycle is
outside the theorem.

## 2. Sharpening for the completed product tensor

For one completed \(Q_2\) packet, the normalized old and new lower type
polynomials are

\[
                         {2+z\over3},\qquad 1.
\]

Thus a touched new-shore block erases one
\(\operatorname{Bernoulli}(1/3)\) contribution.  In a
product-transversal tensor, if \(J_q\) is the total number of touched,
new-shore blocks counted over starts, then

\[
 \sum_i\bigl(f_P(X_i)-f_P(L_i^{(q)})\bigr)={J_q\over3}.
\]

A block has two directions, each appearing twice, so its touch incidence is
at most \(4q\) per \(2h\)-row.  Consequently the symmetric/product
associator factor satisfies

\[
 \boxed{
 \mathsf W_1(\nu_{q,G},V_G)
 \le {2tq\over3h}G.}
\]

For the audited sibling order with \(s=0\), \(h=2t\), and \(q\le t\), every
window touches exactly \(q\) different associator blocks and equality in the
mean ledger is

\[
                         \mathbb E(f_P(X)-f_P(L_q))={q\over3}.
\]

By contrast, the target displacement in either odd sector is
\[
 {q(2m-2\varepsilon-q-1)\over2(2m-1)}
 ={q\over2}+O_A(1).
\]
Hence the unsuspended completed tensor is not merely at a collar-critical
order of magnitude: its exact signed constant is too small.

The factor-three sharpening requires the full local \(8:16\) ledger to be
sampled product-transversally.  The coarser bound \(2tqG/h\) remains valid
and appropriately scoped for arbitrary phase-correlated fixed-frame rows.

## 3. Odd-sector Gaussian demand

Conditional on the infinity bit \(\varepsilon\), the paired part of a middle
owner has defect \(\varepsilon\).  Its full-pair type law is

\[
 \pi_\varepsilon(f)=
 {1\over\binom{2m}{m-\varepsilon}}
 {m!\,2^{m-\varepsilon-2f}\over
 f!(f+\varepsilon)!(m-\varepsilon-2f)!}.
\]

At lower depth \(q\), the target law is \(\pi_{\varepsilon+q}\), and

\[
 \mu_\varepsilon-\mu_{\varepsilon+q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}.
\]

For \(q=A\sqrt m+o(\sqrt m)\), both sectors have variance
\(m/16+o(m)\), and the bounded change \(\varepsilon=0\leftrightarrow1\)
shifts the relevant Gaussian saddle and crossing threshold by only \(O(1)\).
Therefore one common truncated nonnegative one-Lipschitz test yields
\(\Omega_A(W\sqrt m)\) transport demand after the sectors are summed.
Section 5's odd-sector extension is valid.

The sentence allowing windows to cross infinity concerns this lower
Gaussian estimate only.  If a proposed Hamming row actually uses infinity
as an active direction, the rowwise \(W_1\) upper bound must count that
direction as an additional bad direction.  The canonical packets in the
audited report freeze infinity, so no correction is needed for the proved
construction.

## 4. Collar scope

The exact number of Hamming components is \(G/(2h)\).  If the standard word
realization cuts every component once and discards the entire depth-\(H\)
neighborhood of each cut, its charge is

\[
 \Theta\!\left(\min\left\{G,{HG\over h}\right\}\right)
\]
up to harmless endpoint constants.  Thus with
\(H,t=\Theta(\sqrt m)\), this certified realization cannot simultaneously
have \(t/h\) bounded below and collar \(o(W)\).

This is not a lower bound for every possible literal fusion.  Windows
crossing a seam need not be discarded if a fused braid balances their
actual targets.  Likewise the serial-slab expression
\(O(LHW/h)\) assumes separately charged slab interfaces.  Sections 6--7 of
the audited report state these caveats correctly.  For precision, the
phrases “exact action--fragmentation ceiling” in the outcome should be read
or revised to mean:

\[
\boxed{\text{ceiling for fixed-frame Hamming rows completed by the
standard collar-deletion/serial-slab interface.}}
\]

The genuinely statewise theorem independent of later seam treatment is the
row action bound, not the collar dichotomy.

## 5. Final audit boundary

**PASS:**

1. canonical near-spanning \(\mathcal V^t\square Q_s\) packing;
2. literal \(2^t\) completed factors and component count \(G/(2h)\);
3. failure of additive overlap and coordinate-overlap Cartesian tensoring;
4. the general \(2tqG/h\) fixed-frame row action bound;
5. the odd-sector \(\Omega_A(W\sqrt m)\) Gaussian demand.

**Correction/sharpening:**

1. the completed product tensor has the stronger \(2tqG/(3h)\) symmetric
   action ceiling, and its unsuspended form reaches only \(q/3\) rather than
   the required \(q/2\);
2. the collar no-go is architecture-specific and must not be promoted to a
   universal obstruction to non-Hamming or seam-balanced fusion.

