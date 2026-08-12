# Audit of the long-period PBBS fibre-amplification obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

Audited source:
`MATH_THEOREM_N_ST_LONG_PERIOD_FIBRE_AMPLIFICATION_OBSTRUCTION_20260726.md`.

## 0. Verdict

The integral fibre-amplification theorem, its Pascal ratios, the strict
period threshold, the spectator-conveyor calibration, and the cyclic greedy
factor all survive adversarial audit.  I found no false collision step.

Three corrections or qualifications should be made explicit.

1. The binomial defining the passage hyperplane is zero unless
   \(0\le z\le r-d-k\).
2. The assertion \(h_E=2s-1\) is correct, but the proof should cite the
   tight-return two-child/Pascal-fan theorem, or explicitly say why \(h_E\)
   is an odd consecutive reduced child return.  The phrase “forced by the
   height-gap lower bound” suppresses this necessary identification.
3. Dense reframing and the short stable-block property are proved for the
   constructed seed starts.  They are not shown for every additional
   inverse lift introduced when a whole \(K_r(E,0)\) hyperplane is amplified.
   Thus the quantitative packing lower bound is a long-period saddle
   packing, but should not be called an all-lifts dense-reframing packing.

None of these corrections changes the quantitative conclusion or its stated
non-implication to \((ST_A)\).

## 1. Cross-offset collisions

Fix one reduced passage \((E,g)\), and enumerate its projected directed
edges by

\[
 e_t=(\tau^tE,\tau^{t+1}E).
\]

Let \(D,D'\in\partial^{-1}(E)\) be two permitted parent starts.  If their
lifted intervals share a directed parent edge at relative offsets \(t,t'\),
then semiconjugacy gives

\[
 e_t=e_{t'}.
\]

When the reduced support is simple, \(t=t'\).  Equality of the parent edges
then gives equality of their tails,

\[
 \tau^tD=\tau^tD',
\]

and bijectivity of \(\tau^t\) gives \(D=D'\).  Thus two distinct lifts of
one simple passage cannot collide, even when they lie on the same higher
covering cycle.

For two different passages, a shared parent edge would project to a shared
reduced directed edge.  The assumed pairwise disjointness of the reduced
supports excludes this.  If the reduced ranks differ, equality of a parent
edge would in particular force equality of its uniquely first-pruned image,
so it would force the ranks to agree; hence treating the different-rank
edge sets as disjoint causes no loophole.

This proves Theorem 2.1 exactly.  It also agrees with the cyclic-cover
description: a proper simple base arc has one disjoint lift for every point
of the fibre over its initial vertex.

## 2. Exact passage and fibre formulas

Put

\[
 n=r+d-k,\qquad y=r-d-k.
\]

The complete inverse fibre and the terminal-slot-\(z\) hyperplane are

\[
 P_r(E)=\binom n{2d},
 \qquad
 K_r(E;z)=\binom{n-z-1}{2d-1},
\]

with

\[
 K_r(E;z)=0\quad\hbox{unless}\quad 0\le z\le y.
\]

Consequently

\[
 \frac{K_r(E;0)}{P_r(E)}=\frac{2d}{n},
\]

and

\[
 \frac{K_r(E;z)}{P_r(E)}
 =\frac{2d}{n}
   \prod_{j=0}^{z-1}\frac{n-2d-j}{n-1-j}
 =\frac{2d}{r+d-k}
   \prod_{j=0}^{z-1}
   \frac{r-d-k-j}{r+d-k-1-j}.
\]

Thus formulas (2.2)--(2.3) are exact.  The notation \(K_r(E,0)\) in the
source means terminal slot zero; it should not be confused with a passage
time equal to zero.

In the audited saddle tube

\[
 d=\frac r2+O(\sqrt{r\log r}),\qquad
 k=\frac r6+O(\sqrt{r\log r}),
\]

the prefactor is \(3/4+o(1)\), while each product factor is

\[
 \frac14\left(1+O\!\left(\sqrt{\frac{\log r}{r}}+\frac zr\right)\right).
\]

Uniformly for \(0\le z\le3\log r\), the logarithm of the accumulated
relative error is

\[
 O\!\left(\log r\sqrt{\frac{\log r}{r}}
          +\frac{(\log r)^2}{r}\right)=o(1).
\]

Since \(y=(1/3+o(1))r\), all these values of \(z\) are admissible for
large \(r\).  Hence

\[
 \frac{K_r(E;z)}{P_r(E)}
 =\left(\frac34+o(1)\right)4^{-z}
\]

uniformly in the stated range.

## 3. The Pascal period threshold

At

\[
 d/r\to\frac12,\qquad k/r\to\frac16,
\]

Stirling's formula gives

\[
 \frac1r\log P_r(E)
 =p_0+o(1),
 \qquad
 p_0=\frac43\log4-\log3.
\]

The established voltage-itinerary bound

\[
 \#\{E\in\mathcal D_d:\operatorname{per}_\tau(E)\le L\}
 \le2L(2d+1)^{2L}
\]

contributes

\[
 (2\gamma+o(1))r
\]

when \(L\le(\gamma+o(1))r/\log r\).  Comparing with
\(\log B_r=r\log4-O(\log r)\), the strict deletion condition is

\[
 p_0+2\gamma<\log4.
\]

Therefore

\[
 \gamma<\gamma_P,
 \qquad
 \gamma_P=\frac12\left(\log4-p_0\right)
 =\frac12\log\frac3{4^{1/3}}.
\]

The factor \(1/2\) is correct.  At every finite stage one must keep the
strict inequality \(\gamma<\gamma_P\).  Passing to

\[
 \operatorname{per}_\tau(E)
 \ge(\gamma_P-o(1))\frac r{\log r}
\]

is only a diagonal conclusion.  The source states this caveat correctly.

The diagonal argument also correctly applies to the conveyor family: its
size is \(B_r e^{-O(\sqrt r)}=B_re^{-o(r)}\), whereas each fixed-tube or
fixed-\(\gamma\) discarded class is \(B_re^{-c r}\).

## 4. Conveyor chronology

For the spectator-conveyor root, \(B_0=\varnothing\) and the canonical
spine child is a surviving root child.  Hence no pruned leaf lies in the
final root slot, so

\[
 z=0.
\]

The exact predecessor-passage theorem then gives

\[
 \kappa_{2s+1}=-1,
 \qquad n_{-1}(2s+1)=1,
 \qquad h_E<2s+1.
\]

To justify the sharper value of \(h_E\), use the tight-return Pascal fan.
The parent return is zero-winding and attains the height-gap equality

\[
 g=2s+1=2\operatorname{ht}(D)+1.
\]

After one pruning, its leader child is a genuine consecutive return based
at the same initial phase and has exact gap

\[
 g-2=2s-1.
\]

This child is precisely the first reselection of equality particle zero,
so

\[
 h_E=2s-1.
\]

Equivalently, once the child-return identification is stated, \(E\) has
height \(s-1\), the height-gap theorem gives \(h_E\ge2s-1\), same-label
gaps are odd, and \(h_E<2s+1\), forcing equality.  The conclusion in the
source is therefore right, but the missing identification should be
inserted.

## 5. Weighted cyclic selection

The full positive-residence trace of a duration-\(s\) return has

\[
 K=s+2
\]

directed quotient edges.  Two such intervals on a directed cycle can
intersect only when their start positions differ by one of

\[
 -(K-1),\ldots,-1,0,1,\ldots,K-1.
\]

Thus one chosen interval removes at most

\[
 2K-1=2s+3
\]

candidate start positions, including itself.  The reduced period retained
in Section 3 is \(\gg s\), so there is no wrap ambiguity.  Even without
that stronger inequality, the number of distinct conflicting positions
could only decrease on a shorter cycle.

On each reduced orbit, \(d\) and \(k\) are invariant and all selected
passages have \(z=0\); hence the weight \(K_r(E;0)\) is constant around
that orbit.  Ordinary cyclic greedy selection therefore retains at least

\[
 \frac1{2s+3}
 \sum_EK_r(E;0).
\]

The denominator in (4.6) is valid.  It is a safe greedy factor, not a
claim that the interval graph's independence ratio is always exactly its
reciprocal.

## 6. Final implication boundary

The audited theorem proves an integral lower-capacity obstruction:
simple disjoint reduced passage arcs amplify their complete admissible
terminal-slot hyperplanes without cross-offset collisions.  At the saddle,
a zero-slot packet has asymptotic density \(3/4\) in its inverse fibre.

It does not prove a critical packing.  Its explicit lower bound remains

\[
 \frac{B_r}{2s+3}
 \exp\!\left[-(\log(3+\eta)+o(1))s\right],
\]

which is stretched-exponentially below \(B_r/s\).  The packet-amplified
family itself has \(\Lambda=0\).  Section 7 below audits a separate
positive-boundary singleton-phase calibration, but not positive-boundary
preservation for the whole amplified hyperplane.  The surviving gate is
therefore genuinely aggregate: clustering/correlation of the
Pascal-weighted passage phases on long reduced cycles, possibly together
with a fixed-coefficient positive-boundary restriction.

## 7. Addendum: positive-boundary terminal family

The subsequently added Section 4.1 also survives audit after using the
correct full support length \(s+2\).

Write

\[
 D(F)=C_1C_2,
 \quad C_1=1^p0^p,
 \quad C_2=1^{2p-1}0^{p+1}F0^{p-2}.
\]

These are the two primitive root components.  The second is the last root
child and has height \(2p-1\).  Once its initial descent reaches height
\(p-2\), the filler can rise only to height \(2p-4\), so the displayed
initial peak remains its unique deepest level.  This root child survives
the first pruning and no root-level leaf follows it.  Therefore the first
inverse-pruning terminal slot is exactly \(z=0\).

The parent return has

\[
 g=2s+1=2\operatorname{ht}(D)+1.
\]

Its equality-particle leader child is a genuine consecutive return in
\(E=\partial D\), of gap at most \(g-2\).  Since
\(\operatorname{ht}(E)=s-1\), the height-gap theorem gives the reverse
bound \(2s-1\), and hence

\[
 h_E=2s-1.
\]

The exact passage criterion and \(z=0\) then give
\(n_{-1}(2s+1)=1\) and \(\kappa_{2s+1}=-1\).

For the size conversion, \(r=M+3p-1\) and

\[
 \frac{B_r}{\sqrt r}
 =(1+o(1))\frac{4^r}{\sqrt\pi r^2}.
\]

Consequently

\[
 \begin{aligned}
 \log\frac{4^M/M^2}{B_r/\sqrt r}
 &=-(3p-1)\log4+2\log(r/M)+O(1)\\
 &=-3p\log4+o(p),
 \end{aligned}
\]

which is exactly equation (4.12).

The full residence support has \(s+2\), not \(s\), quotient edges.  Since
constructed starts on a common top cycle lie on an \(s\)-spaced lattice,
only the two adjacent lattice starts can conflict.  After deleting short
parent cycles, the conflict graph has maximum degree at most two, so a
one-third independent set is valid.  One should first perform the
saddle/period filtering and then take this independent set.

Finally, the terminal family has size

\[
 \frac{B_r}{\sqrt r}e^{-O(p)}=B_re^{-o(r)},
 \qquad p=\Theta(\sqrt r).
\]

Every fixed saddle-complement or fixed
\(\gamma<\gamma_P\) short-period class has size \(B_re^{-cr}\), hence is
relative \(o(1)\) in this family.  A staged diagonal with the saddle tube
shrinking and \(\gamma\uparrow\gamma_P\) proves (4.13), after which the
degree-two selection retains at least one third of the remaining starts.
