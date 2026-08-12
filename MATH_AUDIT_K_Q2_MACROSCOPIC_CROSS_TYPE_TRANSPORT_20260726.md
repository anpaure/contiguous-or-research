# Final audit of macroscopic Q2 cross-type transport

Date: 2026-07-26

Audited file:
MATH_ATTACK_K_Q2_MACROSCOPIC_CROSS_TYPE_TRANSPORT_20260726.md.

Method: pure mathematics only.

## Verdict

**PASS.**  All numerical normalizations, Gaussian constants, local carrier
ledgers, packing constants, the \(5/4\) visibility threshold, and the stated
seam scope agree with the detailed reports and their audits.

Three notation/scope clarifications are advisable but do not alter any
conclusion:

1. distinguish the global odd-layer centre from the centre conditional on
   the infinity bit;
2. call the \(\Theta(m)\) statement the exact linear-centre relaxation time
   unless a separate spectral-gap theorem is being invoked; and
3. retain “ideal/product-transversal” in every use of the binomial
   \(5/4\)-visibility operator, because its literal overlapping realization
   remains the missing theorem.

## 1. Global and conditional deletion means

For the global uniform rank-\((m-j)\) law on \(2m+1\) coordinates,
\[
 \mathbb E f
 ={(m-j)(m-j-1)\over2(2m+1)}.
\]
Hence the exact global displacement is
\[
 \boxed{
 \Delta_j^{\rm glob}
 ={j(2m-j-1)\over2(2m+1)}.}
\]
The global pair-death mass in step \(j\) is therefore
\[
 W\,\mathbb E{2f\over m-j}
 ={m-j-1\over2m+1}W,
\]
exactly as stated in (0.2).

Conditional on a fixed infinity bit \(\varepsilon\), the paired subset has
rank \(m-j-\varepsilon\) inside \(2m\) coordinates, so
\[
 \bar f_{j,\varepsilon}
 ={(m-j-\varepsilon)(m-j-\varepsilon-1)\over2(2m-1)}
\]
and
\[
 \boxed{
 \Delta_{\varepsilon,q}
 ={q(2m-2\varepsilon-q-1)\over2(2m-1)}.}
\]
Thus (0.6), (1.4), and (5.3) are conditional-sector formulas.  This is
appropriate because every packed local gadget freezes infinity.  The
global and conditional displacements differ by \(O_A(m^{-1/2})\) for
\(q\le A\sqrt m\).

The infinity-death mass is exactly \(W/(2m+1)\) per step and
\(O_A(W/\sqrt m)\) through the Gaussian window.  The source and target
sector weights differ by the same \(o(1)\) fraction.  Therefore discarding
the crossing-infinity paths does not change any constant-order Gaussian
transport or total-variation conclusion.

In (1.8), \(\pi_q\) may be read either as the fixed-\(\varepsilon\)
conditional law or, after summing the two asymptotically identical sectors,
as the global marginal.  Writing \(\pi_q(\cdot\mid\varepsilon)\) in the
conditional proof would remove the only ambiguity.

## 2. Unbiased recoupling and OU constants

The exact transition probabilities
\[
 d(f)={f(f+j+\varepsilon)\over\binom m2},
 \qquad
 b(f)={\binom{m-j-\varepsilon-2f}{2}\over2\binom m2}
\]
are correct.  Direct expansion gives
\[
 b(f)-d(f)
 =-{2m-1\over m(m-1)}
    (f-\bar f_{j,\varepsilon}).
\]
Thus the centred linear eigenvalue is
\[
                         1-{2m-1\over m(m-1)}
\]
and its relaxation time is \(\Theta(m)\).  This exact eigenmode and the
martingale variance bound already prove that \(O(\sqrt m)\) steps move
\(f/\sqrt m\) by \(o_p(1)\).  A full-chain spectral relaxation assertion
is unnecessary; “linear-centre relaxation” is the safest wording.

On \(z=4(f-\bar f)/\sqrt m\), the central birth and death probabilities
are \(1/8+o(1)\), giving
\[
                         2\partial_z^2-2z\partial_z.
\]
The source and target limits differ by \(2A\) standard deviations, so
\[
                         2\Phi(A)-1
\]
is the correct equal-variance normal total-variation constant.

Likewise, the one-seed product means differ by \(A/6\) on the
\(f/\sqrt m\) scale, or \(2A/3\) on the unit-variance \(z\) scale, giving
\[
                         2\Phi(A/3)-1.
\]
The 80-owner product means differ by \(A/10\) on the \(f/\sqrt m\) scale,
or \(2A/5\) on the \(z\) scale, giving
\[
                         2\Phi(A/5)-1.
\]
All three constants are normalized correctly.

## 3. The 80-owner carrier and packing

The four local type-one counts are
\[
                         48,\quad32,\quad32,\quad16.
\]
Pointwise, the uniform carrier decomposes into source-zero, first-death,
second-death, and survivor-high classes of densities
\[
                         {2\over5},\quad{1\over5},
                         \quad{1\over5},\quad{1\over5}.
\]
Thus corner \(11\) erases a Bernoulli-\(2/5\) contribution.  The shifted
upper ledger, common \(\mathbb Z_4\) colouring, and twenty-cycle
all-length suspension agree with the positive-addendum audit.

For global packing, the exact eligibility probabilities are
\[
                         80/2^{10}=5/64,\qquad1/2.
\]
The half-mean Chernoff exponents \(5B/512\) and \(P/16\), conditioning
factor \(2(m+1)\), \(4^r\) resolutions, \(20^r\) copies of
\(Q_{2r+s}\), and component count \(G/(2h)\) are all correct.

## 4. The \(5/4\) threshold

Equating the exact product mean \(2L/5\) with the conditional-sector
target displacement gives
\[
 L^*_{\varepsilon,q}
 ={5q(2m-2\varepsilon-q-1)\over4(2m-1)}
 ={5q\over4}+O_A(1),
\]
with increment
\[
 L^*_{\varepsilon,q+1}-L^*_{\varepsilon,q}
 ={5(m-\varepsilon-q-1)\over2(2m-1)}
 ={5\over4}+O_A(m^{-1/2}).
\]
For the disjoint tensor \(L=q\), the residual gap is exactly
\[
 \Delta_{\varepsilon,q}-{2q\over5}
 ={q(2m-10\varepsilon-5q-1)\over10(2m-1)}
 ={q\over10}+O_A(1).
\]

For independent product-transversal gadget incidences,
\[
 D_L\sim\operatorname{Bin}(L,2/5),
 \qquad\operatorname{Var}D_L=6L/25.
\]
At \(L=O(\sqrt m)\), its centred fluctuation is \(O_p(m^{1/4})\), so
matching \(L^*\) removes the Gaussian type-centre obstruction.

This last conclusion is an operator-capacity statement.  Once
\(L>q\), a physical depth-\(q\) realization cannot be a disjoint product;
the independence/binomial description is an ideal benchmark for the
missing overlapping braid.  The synthesis states this boundary correctly
in Sections 5--6.

## 5. Seam implication

The fixed-frame row estimate
\[
                         \mathsf W_1(\nu_{q,G},V_G)
                         \le{2tq\over h}G
\]
has the correct factor two.  The standard componentwise linearization has
certified collar charge \(O(HW/h)\).  With
\(t,H=\Theta(\sqrt m)\), that particular implementation cannot keep
\(t/h\) positive while making \(H/h=o(1)\).

This is not a universal lower bound against seam-aligned windows,
frame monodromy, or a fused braid.  The synthesis explicitly preserves
that caveat, so its seam implication is correctly scoped.

No substantive correction is required.

