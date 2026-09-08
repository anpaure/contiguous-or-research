# Small critical values make every finite Rayleigh shoulder favorable

**Date:** 2026-08-05  
**Method:** pure mathematics; signed derivative trains and bounded-variation
quadrature; no computation, enumeration, search, or solver  
**Status:** unconditional partial closure of the finite availability
shoulder.  There is an absolute Rayleigh constant \(L_*>0\) such that every
saturated first-minimum Bellman clock whose least critical denomination has
value at most \(L_*\) has nonnegative finite shoulder.  Since the complete
formal Apéry phase is already strictly positive, every such physical clock
is strictly positive.  The compact regime \(L_*<L<\zeta\), and the
endpoint-critical face \(L=\zeta\), remain open.

## 0. Setup

Let \(K\) be the Rayleigh signed-tail kernel.  Write

\[
 M=K(0)>0
\]

and let \(\zeta\) be its unique minimum.  Thus

\[
 K'(x)<0\quad(0<x<\zeta),
 \qquad
 K'(x)>0\quad(x>\zeta).                            \tag{0.1}
\]

The derivative is integrable and of bounded variation.  Put

\[
 R=\lVert K'\rVert_\infty,
 \qquad \mathcal V=\operatorname {Var}_{[0,\infty)}(K'),           \tag{0.2}
\]

and define the positive absolute constant

\[
 \boxed{
 L_*=min\left\{{\zeta\over2},
                 {M\over2R},
                 {M\over2\mathcal V}\right\}.}     \tag{0.3}
\]

If a denominator in (0.3) were zero, its corresponding quotient is
understood as \(+\infty\).  For the Rayleigh kernel both are in fact
strictly positive and finite.

Let \(c_0=0,c_1,\ldots,c_N\) be a nonnegative saturated first-\(\zeta\)
Bellman table, let \(V\) be its physical clock, and put

\[
 \lambda=\max_{1\le j\le N}{c_j\over j}.
\]

Let \(H\) be the least critical denomination:

\[
 c_H=H\lambda,
 \qquad c_j<j\lambda\quad(1\le j<H),               \tag{0.4}
\]

and write

\[
                         L=H\lambda.                \tag{0.5}
\]

Assume \(H<N\).  First-minimum normalization then gives

\[
                         0<L=c_H<\zeta.             \tag{0.6}
\]

Let \(U\) be the formal maximum-density Apéry clock and

\[
                         \Delta_m=U_m-V_m\ge0.       \tag{0.7}
\]

## 1. Every critical-chain start lies before its period value

For \(0\le r<H\), put

\[
 x_r=U_r,
 \qquad \delta_{r,q}=\Delta_{r+qH}.                \tag{1.1}
\]

Criticality gives

\[
 U_{r+qH}=x_r+qL,
 \qquad
 \delta_{r,0}\ge\delta_{r,1}\ge\cdots\ge0.        \tag{1.2}
\]

### Lemma 1.1

For every active layer

\[
 0\le t<\delta_{r,0},
\]

its derivative-train start

\[
                         y=x_r-t                   \tag{1.3}
\]

satisfies

\[
                         0\le y<L.                 \tag{1.4}
\]

#### Proof

The formal Apéry shift has the form

\[
 U_r=\lambda r+\beta_{r\bmod g},
 \qquad \beta\le0,
\]

so, because \(r<H\),

\[
                         x_r\le\lambda r<L.
\]

The physical clock is nonnegative, hence

\[
 \delta_{r,0}=U_r-V_r\le U_r=x_r.
\]

Therefore \(0\le x_r-t<L\). \(\square\)

The inequality uses literal physical nonnegativity.  It would be false for
an arbitrary abstract nonincreasing deficit chain.

## 2. A signed quadrature lemma

For \(L>0\), \(y\ge0\), and \(n\ge1\), define

\[
 J_{L,n}(y)=\sum_{q=0}^{n-1}K'(y+qL),
 \qquad
 J_{L,\infty}(y)=\sum_{q=0}^{\infty}K'(y+qL).       \tag{2.1}
\]

The infinite series converges absolutely by the Gaussian tail.

### Lemma 2.1 (BV left-quadrature bound)

For every \(L>0\) and \(y\ge0\),

\[
 \boxed{
 L J_{L,\infty}(y)
 \le -K(y)+L\mathcal V.}                           \tag{2.2}
\]

#### Proof

On the interval

\[
 I_q=[y+qL,y+(q+1)L],
\]

one has

\[
 \left|LK'(y+qL)-\int_{I_q}K'(x)\,dx\right|
 \le L\operatorname {Var}_{I_q}(K').               \tag{2.3}
\]

Sum over \(q\ge0\).  The interval interiors are disjoint, their variation
sum is at most \(\mathcal V\), and

\[
 \int_y^\infty K'(x)\,dx=-K(y).
\]

Taking the upper error in (2.3) proves (2.2). \(\square\)

### Lemma 2.2 (all prefix slopes are nonpositive at small period)

If

\[
                         0<L\le L_*               \tag{2.4}
\]

and \(0\le y<L\), then

\[
 \boxed{J_{L,n}(y)\le0\quad\hbox{for every }n\ge1.} \tag{2.5}
\]

#### Proof

The Lipschitz bound and (0.3) give

\[
 K(y)\ge K(0)-Ry
       \ge M-RL
       \ge {M\over2}.                              \tag{2.6}
\]

Also

\[
                         L\mathcal V\le {M\over2}. \tag{2.7}
\]

Lemma 2.1 therefore gives \(J_{L,\infty}(y)\le0\).

Because \(y<L\le\zeta/2\), the terms in (2.1) are initially nonpositive
(with equality only at the possible starting point \(y=0\)).  They remain
negative until the arithmetic train crosses \(\zeta\), and
are positive thereafter.  Hence its finite partial sums first decrease and
then increase monotonically to \(J_{L,\infty}(y)\).  Their maximum is no
larger than the larger of the first negative partial sum and their
nonpositive limit.  This proves (2.5). \(\square\)

This argument is genuinely signed.  It uses both the one-well sign pattern
of \(K'\) and the exact integral \(\int_y^\infty K'=-K(y)\); an unsigned
variance or shoulder-area estimate cannot replace it.

## 3. The finite shoulder is nonnegative

For \(0\le t<\delta_{r,0}\), let

\[
 N_r(t)=\#\{q\ge0:\delta_{r,q}>t\}.                \tag{3.1}
\]

The exact critical-chain layer-cake theorem says

\[
 \Phi(V)-\Phi(U)
 =-\sum_{r=0}^{H-1}\int_0^{\delta_{r,0}}
 J_{L,N_r(t)}(x_r-t)\,dt.                          \tag{3.2}
\]

### Theorem 3.1 (small-critical-value shoulder positivity)

If \(H<N\) and

\[
                         H\lambda=L\le L_*,        \tag{3.3}
\]

then

\[
 \boxed{
 \Phi(V)-\Phi(U)\ge0.}                            \tag{3.4}
\]

Consequently

\[
 \boxed{\Phi(V)>0.}                                \tag{3.5}
\]

#### Proof

Lemma 1.1 puts every argument \(x_r-t\) in \([0,L)\).  Lemma 2.2 then
gives

\[
 J_{L,N_r(t)}(x_r-t)\le0
\]

at every active layer.  Every integrand on the right side of (3.2) is
therefore nonnegative after the leading minus sign, proving (3.4).

The inverse-circle variance theorem together with the strict all-period
Fourier coefficient theorem gives \(\Phi(U)>0\) for every complete formal
Apéry clock.  Equation (3.4) proves (3.5). \(\square\)

## 4. What is closed and what remains

The finite availability shoulder is now closed whenever the value of the
least critical denomination tends to zero or merely lies below the fixed
absolute threshold \(L_*\).  This conclusion is uniform in:

* the number of displayed denominations;
* the formal residue period and its arithmetic structure;
* the conductor length;
* the number and depths of shoulder chains; and
* every noncritical denomination.

No termwise comparison of physical and formal clock points is used.  The
complete Bellman coupling enters through the critical-chain prefix
property, while the sign is supplied by the Rayleigh derivative train.

The remaining finite-shoulder regime is the compact band

\[
                         L_*<L<\zeta,              \tag{4.1}
\]

together with the endpoint-critical face \(H=N,L=\zeta\).  In that band
the train still begins at \(0\le y<L<\zeta\), but the infinite sampled
derivative sum can no longer be signed by the coarse BV error (2.2).
Closing it requires a sharper quadrature inequality or a Bellman/Pareto
injection from the positive tail of a train to its negative prefix.

This theorem proves no occurrence-faithful Boolean reserve and no OR-word
upper bound.

## 5. Dependencies

1. `MATH_THEOREM_CYCLIC_APERY_INVERSE_CIRCLE_VARIANCE_CLOSURE_20260805.md`;
2. `MATH_THEOREM_APERY_FINITE_SHOULDER_CRITICAL_CHAIN_LAYER_CAKE_REDUCTION_20260804.md`;
3. `MATH_THEOREM_RAYLEIGH_FIRST_MINIMUM_CROSSING_AND_COMPACT_PERIOD_APERTURE_20260805.md`;
4. the bounded variation and one-well properties of the Rayleigh kernel,
   already audited in the cited Rayleigh analytic notes.
