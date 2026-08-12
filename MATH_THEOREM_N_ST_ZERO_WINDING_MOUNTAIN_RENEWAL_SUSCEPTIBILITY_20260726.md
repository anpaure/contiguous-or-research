# Exact bounded ST susceptibility in the zero-winding mountain renewal sector

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, web
input, or probabilistic independence assumption is used.

## 0. Outcome

Put

\[
 N=2r+1,\qquad H=\lceil A\sqrt r\rceil .
\]

The global ST two-point problem asks for the genuine PBBS return-start set
\(E_H\) and

\[
 R_H=|E_H|,\qquad
 \mathcal C_H=\sum_{t=1}^{H+1}|E_H\cap\tau^{-t}E_H|.
\]

This note computes these statistics exactly on the complete inverse fibre
over a mountain core.  This is a literal PBBS invariant sector, not a
static occupancy relaxation.

Fix \(A>0\) and a constant

\[
                         \frac A2<c<A.             \tag{0.1}
\]

Let \(h\to\infty\) through values for which

\[
                         p=2h-1
\]

is prime, and choose integer ranks \(r>h\) with

\[
                         \frac h{\sqrt r}\longrightarrow c.  \tag{0.2}
\]

Such sequences exist: take any sequence of odd primes \(p\), put
\(h=(p+1)/2\), and take an integer nearest \((h/c)^2\).  Write

\[
 y=r-h,
 \qquad
 \Omega_{r,h}=\left\{(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^{p}:
                      \sum_jn_j=y\right\}.        \tag{0.3}
\]

The exact mountain-fibre transport is

\[
 \tau(n_0,n_1,\ldots,n_{p-1})
   =(n_{p-1},n_0,\ldots,n_{p-2}),                 \tag{0.4}
\]

and a current phase starts a first return of gap \(2h+1\) exactly when

\[
                         n_0=0.                   \tag{0.5}
\]

The return in (0.5) is in fact zero-winding.  Moreover, within the
residence cutoff \(H\), these are **all** first returns in the fibre.  Since
(0.1)--(0.2) imply,
for all sufficiently large ranks,

\[
 h+1\le H,
 \qquad
 H+1<p,                                           \tag{0.6}
\]

all these starts belong to the retained Gaussian long-cycle deck.

Let \(E^{\rm mt}_{r,h}=E_H\cap\Omega_{r,h}\) be the restriction of the
full genuine start process to this sector and put

\[
 R^{\rm mt}_{r,h}=|E^{\rm mt}_{r,h}|,
 \qquad
 \mathcal C^{\rm mt}_{r,h;H}
 =\sum_{t=1}^{H+1}
   |E^{\rm mt}_{r,h}\cap\tau^{-t}E^{\rm mt}_{r,h}|. \tag{0.7}
\]

Then the exact formulas are

\[
 \boxed{
 |\Omega_{r,h}|=\binom{y+p-1}{p-1},
 \qquad
 R^{\rm mt}_{r,h}=\binom{y+p-2}{p-2},}            \tag{0.8}
\]

and

\[
 \boxed{
 \mathcal C^{\rm mt}_{r,h;H}
  =(H+1)\binom{y+p-3}{p-3}.}                      \tag{0.9}
\]

Consequently this fibre has critical one-point density,

\[
 \boxed{
 H\frac{R^{\rm mt}_{r,h}}{|\Omega_{r,h}|}
 \longrightarrow2Ac,}                            \tag{0.10}
\]

but bounded two-point susceptibility,

\[
 \boxed{
 \frac{\mathcal C^{\rm mt}_{r,h;H}}
      {R^{\rm mt}_{r,h}}
 \longrightarrow2Ac.}                            \tag{0.11}
\]

There is a complete renewal limit.  If a start is chosen uniformly from
\(E^{\rm mt}_{r,h}\), and

\[
 X_{r,h}=
 \#\{1\le t\le H+1:\tau^tD\in E^{\rm mt}_{r,h}\},             \tag{0.12}
\]

then

\[
 \boxed{X_{r,h}\ \Longrightarrow\ \mathrm{Poisson}(2Ac).}     \tag{0.13}
\]

The exact conflict-graph inequality consequently gives an integral
quotient-edge-disjoint subfamily \(\mathcal P^{\rm mt}_{r,h}\) with

\[
 \boxed{
 |\mathcal P^{\rm mt}_{r,h}|
 \ge
 \frac{R^{\rm mt}_{r,h}}
 {1+2(H+1)(p-2)/(y+p-2)}.}                        \tag{0.14}
\]

In particular,

\[
 \liminf H\frac{|\mathcal P^{\rm mt}_{r,h}|}{|\Omega_{r,h}|}
 \ge \frac{2Ac}{1+4Ac}>0.                        \tag{0.15}
\]

Thus bounded \(\mathcal C_H/R_H\) is dynamically realizable by genuine
zero-winding PBBS returns at the critical \(1/H\) start density, even on
retained cycles.  It is not merely compatible with one-point marginals.

This does **not** refute \((ST_A)\).  The entire mountain inverse fibre has
size \(\exp(O(\sqrt r\log r))\), exponentially negligible beside
\(\operatorname{Cat}_r\).  Its first-pruned core has period one, so it is
also removed by the established long-core-period deletion.  The theorem
does, however, close a proof route: no uniform zero-winding theorem of the
form

\[
 H|E|/|\Omega|\asymp1
 \quad\Longrightarrow\quad
 \mathcal C_H/|E|\longrightarrow\infty             \tag{0.16}
\]

can hold on all genuine PBBS invariant fibres.  Any global divergence
proof must use the Catalan weight and long reduced-core chronology, not
the local predecessor renewal law alone.

## 1. Literal mountain rerooting and the zero-winding audit

Let

\[
 E_h=1^{h-1}0^{h-1}
\]

be the rank-\((h-1)\) mountain.  It has one peak and
\(p=2h-1\) equality-particle gaps.  The exact inverse peak-deletion
parametrization gives (0.3), and stars and bars gives the first formula in
(0.8).

For clarity, the literal dynamics is recalled.  If
\(w=0E_h\), put

\[
 \epsilon_j=\mathbf1_{\{w_{j-1}\ne w_j\}}.
\]

The physical gap between consecutive equality particles is

\[
 q_j=1+\epsilon_j+2n_j.                           \tag{1.1}
\]

Only the two mountain boundary indices have nonzero \(\epsilon_j\).  In
one two-step PBBS update the selected particles are the two mountain
boundary particles.  If \(C_j\) is their selection-count vector, direct
substitution gives

\[
 C_{j-1}-C_{j-2}=\epsilon_j-\epsilon_{j-1}.       \tag{1.2}
\]

The normalized distinguished particle advances by

\[
 2(h-1)=-1\pmod p.
\]

Therefore

\[
\begin{aligned}
 q'_j
 &=q_{j-1}+C_{j-1}-C_{j-2}\\
 &=1+\epsilon_j+2n_{j-1},
\end{aligned}
\]

which proves (0.4).  Thus the apparent weak-composition model is exactly
the dynamic PBBS rerooting, including its normalization shift.

The mountain selected-particle word is

\[
 \kappa_t=t(h-1)\pmod p.
\]

Since \(2(h-1)=p-1\), its distinguished particle is first reselected at
time \(p=2h-1\), while its immediate predecessor occurs exactly at the
positive times

\[
                         2,\ 2+p,\ 2+2p,\ldots .               \tag{1.2a}
\]

The exact terminal-spacing/return theorem says that an inverse lift with
terminal free occupancy \(z=n_0\) closes at the \((2z+2)\)-nd predecessor
occurrence.  Its prospective first-return time is therefore

\[
                         g(z)=2+(2z+1)p,                         \tag{1.2b}
\]

provided this lies below the ambient circumference.  For \(z=0\), this is
\(p+2=2h+1\), and the exact passage theorem proves firstness.  For
\(z\ge1\), (0.6) gives

\[
                         g(z)\ge3p+2>2H-1,                       \tag{1.2c}
\]

so no such phase has residence at most \(H\) (and if (1.2b) passes the
ambient circumference, it is a fortiori not a nonwrapping short return).
This proves both (0.5) and the asserted equality
\(E^{\rm mt}_{r,h}=E_H\cap\Omega_{r,h}\).

It remains to audit winding.  In a lift of the primitive mountain, the
only root components after the lifted mountain component are the free
leaf peaks in the terminal root corner.  Hence at a phase with composition
\(\mathbf n\),

\[
 d(D)=1+2n_0.                                     \tag{1.3}
\]

Combining (0.4) and (1.3),

\[
 d(\tau^jD)=1+2n_{-j}.                            \tag{1.4}
\]

For a start satisfying \(n_0=0\), the already proved return congruence at
step-two duration \(h\) has the form

\[
 \sum_{j=0}^{h-1}d(\tau^jD)
   =\delta(\tau^hD)+aN,
 \qquad a\in\mathbb Z_{\ge0}.                    \tag{1.5}
\]

But (1.4) and \(\sum_jn_j=y\) give

\[
 0<\sum_{j=0}^{h-1}d(\tau^jD)
 \le h+2y
 =2r-h
 <N.                                              \tag{1.6}
\]

Since \(1\le\delta(\tau^hD)<N\), equations (1.5)--(1.6) force
\(a=0\).  Thus every return counted in (0.5) is zero-winding.  No use is
made of the false converse \(d(D)=1\Rightarrow\) return; firstness was
proved first from the exact mountain predecessor itinerary.

Finally, when \(p\) is prime, every nonconstant composition has rotation
period exactly \(p\).  An active composition has \(n_0=0\) and total
mass \(y>0\), so it is nonconstant.  The second inequality in (0.6)
therefore puts every active phase on a retained quotient cycle.

## 2. The exact scalar renewal transfer

Write

\[
                         T(z)=1+z+z^2+\cdots={1\over1-z}.       \tag{2.1}
\]

A free composition coordinate contributes \(T(z)\), while forcing that
coordinate to be zero contributes one.  Therefore for any \(q\) distinct
coordinate indices \(i_1,\ldots,i_q\),

\[
 \boxed{
 \#\{\mathbf n\in\Omega_{r,h}:
       n_{i_1}=\cdots=n_{i_q}=0\}
 =[z^y]T(z)^{p-q}
 =\binom{y+p-q-1}{p-q-1}.}                       \tag{2.2}
\]

Equation (2.2) is the transfer/renewal computation.  The total free mass
is conditioned exactly by coefficient extraction; the coordinates are
not declared independent.  Dynamic phase separation is handled by the
literal rotation (0.4): at lag \(t\), the second return test addresses the
coordinate \(n_{-t}\).

Taking \(q=1\) in (2.2) proves the second formula in (0.8).  For every
\(1\le t\le H+1<p\), the indices \(0\) and \(-t\) are distinct, so
\(q=2\) proves

\[
 |E^{\rm mt}_{r,h}\cap\tau^{-t}E^{\rm mt}_{r,h}|
 =\binom{y+p-3}{p-3}.                             \tag{2.3}
\]

Summing (2.3) proves (0.9).

Every selected return trace has \(h+2\le H+1\) edges and lies on a cycle
longer than \(H+1\).  Hence the standard interval conflict graph has at
most \(\mathcal C^{\rm mt}_{r,h;H}\) edges.  Turan--Cauchy gives

\[
 \alpha\ge
 \frac{(R^{\rm mt}_{r,h})^2}
 {R^{\rm mt}_{r,h}+2\mathcal C^{\rm mt}_{r,h;H}}, \tag{2.3a}
\]

which, with (2.5), proves (0.14)--(0.15).

Division gives the exact one- and two-point ratios

\[
 \frac{R^{\rm mt}_{r,h}}{|\Omega_{r,h}|}
 =\frac{p-1}{y+p-1}
 =\frac{2h-2}{r+h-2},                             \tag{2.4}
\]

and

\[
 \frac{\mathcal C^{\rm mt}_{r,h;H}}
      {R^{\rm mt}_{r,h}}
 =(H+1)\frac{p-2}{y+p-2}
 =(H+1)\frac{2h-3}{r+h-3}.                       \tag{2.5}
\]

Equations (0.2), (2.4), and (2.5) prove (0.10)--(0.11), including the
constant \(2Ac\).

The same formulas give an exact, nonasymptotic susceptibility phase
diagram.  For any window length \(1\le L<p\), replace \(H+1\) by \(L\).
Then

\[
 \boxed{
 \frac{1}{R^{\rm mt}_{r,h}}
 \sum_{t=1}^{L}
 |E^{\rm mt}_{r,h}\cap\tau^{-t}E^{\rm mt}_{r,h}|
 =L\frac{p-2}{y+p-2}.}                            \tag{2.6}
\]

Thus this genuine PBBS renewal sector has bounded susceptibility exactly
when \(Lp=O(y+p)\), and it diverges exactly when
\(Lp/(y+p)\to\infty\).  The dense one-defect rotor and the Gaussian
finite-susceptibility regime are the two sides of the same identity, not
different dynamical mechanisms.

## 3. Poisson renewal limit

Condition on \(n_0=0\), so the remaining \(p-1\) coordinates are uniform
weak compositions of \(y\).  Put \(L=H+1\).  For every fixed integer
\(q\ge1\), equation (2.2) and ordered choice of \(q\) future phases give

\[
 \boxed{
 \mathbb E (X_{r,h})_q
  =(L)_q\frac{(p-2)_q}{(y+p-2)_q},}               \tag{3.1}
\]

where \((x)_q=x(x-1)\cdots(x-q+1)\).  Under (0.2),

\[
 \frac{L(p-2)}{y+p-2}\longrightarrow2Ac,         \tag{3.2}
\]

and hence

\[
 \mathbb E(X_{r,h})_q\longrightarrow(2Ac)^q      \tag{3.3}
\]

for every fixed \(q\).

There is no hidden moment-indeterminacy.  For \(u\ge0\), the exact
factorial expansion is

\[
 \mathbb E(1+u)^{X_{r,h}}
 =\sum_{q=0}^{L}{u^q\over q!}
   (L)_q{(p-2)_q\over(y+p-2)_q}.                 \tag{3.4}
\]

Since \((L)_q\le L^q\) and

\[
 {p-2-i\over y+p-2-i}\le {p-2\over y+p-2},
\]

the summand in (3.4) is at most

\[
 {1\over q!}
 \left(uL{p-2\over y+p-2}\right)^q.             \tag{3.5}
\]

The base in parentheses stays bounded.  Dominated convergence in (3.4),
using (3.3), gives

\[
 \mathbb E(1+u)^{X_{r,h}}
 \longrightarrow e^{2Acu}.                      \tag{3.6}
\]

This is the factorial generating function of \({\rm Poisson}(2Ac)\),
which proves (0.13).  In particular (0.11) is not caused by cancellation
of rare highly clustered phases: a typical active phase has a tight,
finite limiting number of other active phases in the whole ST window.

## 4. Exact implication boundary

The theorem proves, on a complete literal PBBS sector:

1. exact dynamic rerooting, not an independently rotated Pascal fibre;
2. genuine first returns of Gaussian residence;
3. zero winding, with the integer winding audited in (1.3)--(1.6);
4. retained quotient cycles longer than the ST window;
5. critical one-point density \(\Theta(1/H)\);
6. the exact bounded ratio (2.5); and
7. the full Poisson short-lag law.

It does not prove a global lower bound of order
\(\operatorname{Cat}_r/H\).  Indeed

\[
 |\Omega_{r,h}|
 =\binom{r+h-2}{2h-2}
 \le (r+h)^{2h}
 =\exp(O(\sqrt r\log r)),                         \tag{4.1}
\]

whereas \(\operatorname{Cat}_r=\exp((\log4+o(1))r)\).  Hence this sector
has zero global Catalan weight.  It proves a sharp obstruction to uniform
renewal clustering, not a counterexample to \((ST_A)\).

After the established long-period reduction, the remaining global
question is consequently stricter: prove that long-period Pascal-saddle
cores cannot exhibit the same finite-susceptibility renewal law at total
weight \(\Omega(\operatorname{Cat}_r/H)\), or prove that they do and thereby
refute \((ST_A)\).  The mountain calculation shows exactly which feature
must fail globally; neither zero winding nor the predecessor-passage rule
itself forces divergence.
