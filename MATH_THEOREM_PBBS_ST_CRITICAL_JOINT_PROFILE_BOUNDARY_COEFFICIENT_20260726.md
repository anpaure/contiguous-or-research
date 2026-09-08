# The critical PBBS joint profile--boundary coefficient and the surviving chronological gate

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, probabilistic
surrogate, or multiplication of marginal estimates is used.

## 0. Result

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .                 \tag{0.1}
\]

There are two different joint objects in the Gaussian PBBS problem.  They
must not be identified.

* The **genuine two-start census** asks whether both reduced phases satisfy
  the predecessor threshold

  \[
  B_2(F)\le 2H-1,
  \qquad B_2(\tau^uF)\le2H-1.                    \tag{0.2}
  \]

* The **profile--boundary envelope** takes one complete formal Pascal fan
  and asks whether a second translated terminal boundary block is also
  zero.  It does not assert (0.2) at the second phase.

This note computes both kernels exactly and evaluates the second one in the
critical lane.  The answer is saturation, not a coefficient saving.

For an unsaturated zero-winding profile put

\[
 b=2s-3p+1,\qquad K=p+b,                         \tag{0.3}
\]

and let \(d\) be a phase displacement modulo \(K\).  The number of
last-level boxes left simultaneously free by the two translated
\(p\)-blocks is

\[
 \boxed{
 r_{p,b}(d)=(b-\bar d)_++(\bar d-p)_+,
 \qquad0\le\bar d<K,
 }                                                \tag{0.4}
\]

where \(\bar d=d\pmod K\).  If \(Q_j,C_j,t_j\) are the continuants

\[
 Q_{j+1}=Q_j-zQ_{j-1},\quad C_j=Q_j/Q_{j+1},
 \quad t_j=z^j/Q_j^2,                             \tag{0.5}
\]

then the exact one-profile/second-boundary generating function is

\[
 \boxed{
 \mathscr F^{(2,d)}_{s,p}(z)
 =\frac{C_{p-1}(z)^{b+3}}{Q_{p-1}(z)^3}
   \left((1-t_p(z))^{-r_{p,b}(d)}-1\right).
 }                                                \tag{0.6}
\]

The one-anchor series is the same formula with \(r_{p,b}(d)=b\); it is
exactly the already audited capacity-envelope series

\[
 \mathscr F^\star_{s,p}(z)
 =\frac{C_p(z)^b}{Q_p(z)^3}
   \left[1-(1-t_p(z))^b\right].                  \tag{0.7}
\]

Now suppose

\[
 \frac p{\sqrt m}\longrightarrow\alpha>0,
 \qquad \frac bp\longrightarrow c\in(0,\infty),
 \qquad n:=m-s,\quad\frac n{p^2}\longrightarrow u=\alpha^{-2}.
                                                               \tag{0.8}
\]

There is a continuous density \(f_c\) on \((0,\infty)\), characterized by

\[
 \boxed{
 \int_0^\infty e^{-\lambda u}f_c(u)\,du
 =\exp\{c(1-x\coth x)\}
   \left(\frac{x}{\sinh x}\right)^5,
 \qquad x=\sqrt\lambda,
 }                                                \tag{0.9}
\]

Its first two moments are

\[
 \int_0^\infty u f_c(u)\,du=\frac c3+\frac56,
 \qquad
 \operatorname {Var}_{f_c}(u)=\frac{2c}{45}+\frac1{18}.       \tag{0.9a}
\]

such that

\[
 \boxed{
 [z^{m-s}]\mathscr F^\star_{s,p}(z)
 =\left(2ce^{-c}f_c(\alpha^{-2})+o(1)\right)
   \frac{4^m}{p^6}.
 }                                                \tag{0.10}
\]

If \(r_{p,b}(d)/p\to\rho\), then

\[
 \boxed{
 [z^{m-s}]\mathscr F^{(2,d)}_{s,p}(z)
 =\left(2\rho e^{-c}f_c(\alpha^{-2})+o(1)\right)
   \frac{4^m}{p^6},
 }                                                \tag{0.11}
\]

and hence, whenever \(\rho>0\),

\[
 \boxed{
 \frac{[z^{m-s}]\mathscr F^{(2,d)}_{s,p}}
      {[z^{m-s}]\mathscr F^\star_{s,p}}
 \longrightarrow \frac{\rho}{c}
 =\lim\frac{r_{p,b}(d)}b.
 }                                                \tag{0.12}
\]

Thus the exact joint coefficient is the geometric cyclic-arc overlap, not
the product of two one-boundary marginals.

Let

\[
 \mathcal J^{\rm pb}_{m;s,p}(L)
 =\sum_{d=1}^{L}[z^{m-s}]\mathscr F^{(2,d)}_{s,p}(z).           \tag{0.13}
\]

If \(L/p\to\lambda\), define the \((1+c)\)-periodic function

\[
 R_c(x)=(c-x)_++(x-1)_+\quad(0\le x<1+c)          \tag{0.14}
\]

and

\[
 \Phi_c(\lambda)=\frac1c\int_0^\lambda
 R_c(x\bmod(1+c))\,dx.                           \tag{0.15}
\]

Then

\[
 \boxed{
 \frac{\mathcal J^{\rm pb}_{m;s,p}(L)}
 {[z^{m-s}]\mathscr F^\star_{s,p}}
 =p\Phi_c(\lambda)+o(p).
 }                                                \tag{0.16}
\]

In the critical sector \(p\le b\le2p\), the minimum permitted horizon is
\(L=s+O(1)\), so \(\lambda=(3+c)/2\).  Formula (0.15) becomes

\[
 \boxed{
 \Phi_c\left(\frac{3+c}{2}\right)
 =\frac{5c^2+2c+1}{8c}.
 }                                                \tag{0.17}
\]

It lies between \(1\) and \(25/16\) for \(1\le c\le2\).  Therefore the
formal critical profile mass has mean short-lag profile--boundary degree
\(\Theta(p)=\Theta(\sqrt m)\).  Along the subsequences on which the
critical one-point envelope is \(\Theta(4^m/m^2)\),

\[
 \boxed{
 \sum_{s,p}\mathcal J^{\rm pb}_{m;s,p}(H+1)
 =\Theta_A(4^m/m^{3/2})=\Theta_A(B_m).
 }                                                \tag{0.18}
\]

This is a matching saturation theorem for the **formal joint
profile--boundary envelope**.  It is not a matching lower bound for the
genuine PBBS two-start count and therefore not a lower or upper bound for
\(\nu_{A\sqrt m}\).

The exact predecessor-threshold kernel shows why.  Conditional on two
genuine reduced active phases, the outer Pascal lift retains a fixed
positive fraction: at the saddle it is \(9/16\) for two distinct
terminal-zero coordinates and \(3/4\) for the same coordinate.  But the
kernel contains the literal factor

\[
 \mathbf1_{\{B_2(F)\le2H-1\}}
 \mathbf1_{\{B_2(\tau^uF)\le2H-1\}},             \tag{0.19}
\]

which (0.6) does not supply.  The implication

\[
 \text{one full profile fan plus a second terminal boundary}
 \Longrightarrow B_2(\tau^uF)\le2H-1             \tag{0.20}
\]

is false already at the first nontrivial PBBS lift.  Consequently neither

\[
 \nu_{A\sqrt m}=o(B_m\sqrt m)                    \tag{0.21}
\]

nor a matching \(\Omega(B_m\sqrt m)\) lower bound follows.  The remaining
quantity is exactly the Pascal-weighted short-lag autocorrelation of the
actual reduced predecessor-active set.  Marginal or envelope coefficients
cannot replace it.

## 1. The genuine predecessor-threshold two-point kernel

Let \(F\in\mathcal D_d\) have \(k\) peaks and put

\[
 y=m-d-k,\qquad K=2d+1,
 \qquad P_{y,K}=\binom{y+K-1}{K-1}.              \tag{1.1}
\]

Let

\[
 Z=\max\{a:B_{2a+2}(F)\le2H-1\},
 \quad
 Z'=\max\{a:B_{2a+2}(\tau^uF)\le2H-1\},         \tag{1.2}
\]

with value \(-1\) when the set is empty.  Pull the phase-\(u\) terminal
coordinate back to the phase-zero weak-composition simplex.  If the two
tested coordinates are distinct, the exact joint count is

\[
 \begin{aligned}
 V_{y,K}(Z,Z')={}&P_{y,K}
 -\binom{y-Z+K-2}{K-1}
 -\binom{y-Z'+K-2}{K-1}\\
 &+\binom{y-Z-Z'+K-3}{K-1}.
 \end{aligned}                                   \tag{1.3}
\]

If they agree, the count is

\[
 U_{y,K}(\min\{Z,Z'\})
 =P_{y,K}-\binom{y-\min\{Z,Z'\}+K-2}{K-1}.       \tag{1.4}
\]

Both expressions are zero if either threshold is negative.  Equations
(1.3)--(1.4) are joint counts; no independence is used.

In the unique Pascal saddle,

\[
 d=\frac m2+O(\sqrt{m\log m}),\quad
 k=\frac m6+O(\sqrt{m\log m}),\quad
 y=(1/3+o(1))m,\quad K=(1+o(1))m.                \tag{1.5}
\]

Writing \(\varrho=y/(y+K-1)=1/4+o(1)\), direct binomial division gives,
uniformly for \(Z,Z'\le6\log m+2\),

\[
 \frac{V_{y,K}(Z,Z')}{P_{y,K}}
 =(1-\varrho^{Z+1})(1-\varrho^{Z'+1})+o(1),      \tag{1.6}
\]

and

\[
 \frac{U_{y,K}(\min\{Z,Z'\})}{P_{y,K}}
 =1-\varrho^{\min\{Z,Z'\}+1}+o(1).              \tag{1.7}
\]

For \(Z=Z'=0\), these are respectively

\[
 \boxed{9/16+o(1),\qquad3/4+o(1).}               \tag{1.8}
\]

Thus the outer threshold cylinder has no vanishing two-time factor.  If

\[
 a_H(F)=\mathbf1_{\{B_2(F)\le2H-1\}},            \tag{1.9}
\]

the reduced weighted one- and two-time counts are

\[
 \mathscr R_H=\sum_FP_m(F)a_H(F),                \tag{1.10}
\]

\[
 \mathscr C_H=\sum_{u=1}^{H+1}\sum_F
 P_m(F)a_H(F)a_H(\tau^uF).                       \tag{1.11}
\]

After the negligible saddle and short-cycle deletions, the genuine parent
statistics obey

\[
 \left(\frac12-o(1)\right)
 \frac{\mathscr C_H}{\mathscr R_H}
 \le\frac{\mathcal C_H}{R_H}
 \le\left(\frac43+o(1)\right)
 \frac{\mathscr C_H}{\mathscr R_H}.              \tag{1.12}
\]

For coordinate-stable terminal-zero pairs, the lower constant in the
numerator can be replaced by \(9/16\).  Hence the actual short-lag
clustering is, up to fixed constants, exactly the reduced clustering in
(1.11).

## 2. Two translated last-level boundary blocks

At the first mountain depth \(p\), the reduced mountain has \(K=p+b\)
cyclic child slots.  One complete fan anchor forces a cyclic block of
\(p\) slots to vanish, leaving a complementary arc of \(b\) boxes in
which the positive last curvature \(y_p\) may be placed.

Take the first zero block to be

\[
 P_0=\{0,1,\ldots,p-1\}\subset\mathbb Z_K
\]

and the second to be \(P_d=P_0+d\).  Their allowed arcs are the
complements \(A_0,A_d\), both of size \(b\).  On a circle, two arcs of
length \(b\), whose initial points differ by \(\bar d\), intersect in two
possibly empty end pieces.  Therefore

\[
 |A_0\cap A_d|
 =(b-\bar d)_++(b-(K-\bar d))_+
 =(b-\bar d)_++(\bar d-p)_+.
\]

This proves (0.4).  Conditional on \(y_p=y\ge1\), the exact one- and
two-boundary counts are

\[
 \binom{y+b-1}{y},\qquad
 \binom{y+r_{p,b}(d)-1}{y},                      \tag{2.1}
\]

with the second count zero when \(r_{p,b}(d)=0\).

Before the last curvature is summed, the exact collapsed upper-profile
series is

\[
 \mathscr F_{<p}(z)
 =\frac{C_{p-1}(z)^{b+3}}{Q_{p-1}(z)^3}.         \tag{2.2}
\]

Since the last curvature has marker \(t_p=z^p/Q_p^2\), summing (2.1)
over \(y\ge1\) gives

\[
 \sum_{y\ge1}\binom{y+r-1}{y}t_p^y
 =(1-t_p)^{-r}-1.                                \tag{2.3}
\]

Equations (2.2)--(2.3) prove (0.6).  With \(r=b\), the continuant Cassini
identity gives (0.7).

At \(z=1/4\), \(t_p=(p+1)^{-2}\).  Thus there is also the exact finite
ratio

\[
 \boxed{
 \frac{\mathscr F^{(2,d)}_{s,p}(1/4)}
      {\mathscr F^\star_{s,p}(1/4)}
 =\frac{(1-(p+1)^{-2})^{-r_{p,b}(d)}-1}
        {(1-(p+1)^{-2})^{-b}-1}.
 }                                                \tag{2.4}
\]

For \(b\asymp p\), uniformly in \(1\le r\le b\),

\[
 \frac{(1-(p+1)^{-2})^{-r}-1}
      {(1-(p+1)^{-2})^{-b}-1}
 =\frac rb\left(1+O(p^{-1})\right).             \tag{2.5}
\]

This is already an exact tilted-mass version of (0.12).

## 3. Critical local limit

We prove the coefficient form because evaluation only at \(1/4\) does not
by itself give a coefficient asymptotic.

For \(z<1/4\), define \(\eta\) by

\[
 2\sqrt z\cosh\eta=1.
\]

The continuant has the exact form

\[
 Q_j(z)=z^{j/2}\frac{\sinh((j+1)\eta)}{\sinh\eta}.             \tag{3.1}
\]

Take

\[
 z=\frac14e^{-\lambda/p^2},\qquad x=\sqrt\lambda.
\]

Then \(\eta=x/p+O(p^{-3})\), and uniformly for \(\lambda\) in compact
subsets of the right half-plane,

\[
 \frac{Q_p(z)}{Q_p(1/4)}\longrightarrow\frac{\sinh x}{x},     \tag{3.2}
\]

\[
 \left(\frac{C_p(z)}{C_p(1/4)}\right)^b
 \longrightarrow\exp\{c(1-x\coth x)\},                       \tag{3.3}
\]

and

\[
 \frac{t_p(z)}{t_p(1/4)}
 \longrightarrow\left(\frac{x}{\sinh x}\right)^2.           \tag{3.4}
\]

Because \(bt_p(1/4)=O(p^{-1})\), the nonempty last-curvature bracket is
asymptotic to \(bt_p\).  Combining (3.2)--(3.4) with (0.7) gives the
normalized Laplace transform (0.9): three powers of \(x/\sinh x\) come
from \(Q_p^{-3}\), and two from the last-curvature marker.

Expanding at \(x=0\),

\[
 x\coth x=1+\frac{x^2}{3}-\frac{x^4}{45}+O(x^6),
 \qquad
 \log\frac{x}{\sinh x}=-\frac{x^2}{6}+\frac{x^4}{180}+O(x^6),
\]

proves (0.9a).  Positivity follows directly from the Euler products

\[
 \frac{x}{\sinh x}
 =\prod_{j\ge1}\left(1+\frac{\lambda}{\pi^2j^2}\right)^{-1},
 \qquad
 x\coth x-1
 =2\sum_{j\ge1}\frac{\lambda}{\lambda+\pi^2j^2}.
\]

The first expression is a Laplace transform of a sum of independent
exponentials.  The second is a Bernstein function, so its negative
exponential is also a Laplace transform.  Their convolution has a
continuous density which is positive on \((0,\infty)\).

The convergence upgrades to a lattice local limit.  Indeed the normalized
series contains an independent \(Q_{p-1}^{-1}\) factor.  On the circle
\(z=(1/4)e^{it}\), retaining the two nearest zeros

\[
 \rho_j=\frac1{4\cos^2(j\pi/p)},\qquad j=1,2,
\]

gives, after the scaling \(t=\xi/p^2\), the integrable bound

\[
 \left|\varphi_p(\xi)\right|
 \le\frac{C}{(1+|\xi|)^2}.                       \tag{3.5}
\]

All remaining positive-series factors have characteristic modulus at most
one.  Pointwise convergence follows from (3.2)--(3.4), and dominated
Fourier inversion therefore gives

\[
 p^2\Pr\{X_p=n\}\longrightarrow f_c(u)
 \quad\text{whenever }n/p^2\to u.                \tag{3.6}
\]

The same proof applies to (0.6) whenever \(r/p\to\rho>0\); the normalized
limit remains \(f_c\).  Finally, the exact critical-point evaluation

\[
 4^{-s}\mathscr F^\star_{s,p}(1/4)
 =\frac{2}{(p+1)^3}
 \left(\frac{p+1}{p+2}\right)^b
 \left[1-\left(1-\frac1{(p+1)^2}\right)^b\right]
 =\left(2ce^{-c}+o(1)\right)p^{-4}               \tag{3.7}
\]

combined with (3.6) proves (0.10).  Replacing \(b\) by \(r\) only in the
last nonempty factor changes the leading constant from \(c\) to \(\rho\),
which proves (0.11)--(0.12).

## 4. Exact short-lag profile--boundary clustering

Let \(L/p\to\lambda\).  Equation (0.4) gives the Riemann-sum limit

\[
 \frac1{p^2}\sum_{d=1}^Lr_{p,b}(d)
 \longrightarrow
 \int_0^\lambda R_c(x\bmod(1+c))\,dx.            \tag{4.1}
\]

The local limit in Section 3 is uniform when \(c\) and \(n/p^2\) stay in
compact subsets of \((0,\infty)\).  Terms for which \(r_{p,b}(d)=o(p)\)
are controlled by (2.5) and contribute the corresponding vanishing part
of the Riemann sum.  Summing (0.12) proves (0.16).

For the minimum critical horizon, \(L=s+O(1)\), one has

\[
 \lambda=\frac{s}{p}+o(1)=\frac{3+c}{2}+o(1).
\]

When \(1\le c\le2\), this lies in the first period of \(R_c\).  Splitting
the integral at \(1\) and \(c\) gives

\[
 \begin{aligned}
 \int_0^{(3+c)/2}R_c(x)\,dx
 &=\int_0^1(c-x)\,dx
   +\int_1^c(c-1)\,dx
   +\int_c^{(3+c)/2}(x-1)\,dx\\
 &=\frac{5c^2+2c+1}{8}.
 \end{aligned}                                   \tag{4.2}
\]

Division by \(c\) proves (0.17).  If \(H\ge s\), enlarging the lag window
can only increase (0.15), so (0.17) is a uniform positive lower bound for
every such critical cell.

The audited critical-envelope theorem supplies, along an infinite
subsequence, \(\Theta(m)\) cells with \(p,b\asymp\sqrt m\), compact
\(n/p^2\), and total one-anchor coefficient

\[
 \Theta(4^m/m^2).
\]

Multiplying cellwise by the proved joint ratio (0.16), not by a marginal
estimate, gives (0.18).  The reverse bound follows from
\(r_{p,b}(d)\le b\) and \(H=O(\sqrt m)\).

## 5. Why this does not decide \(ST_A\)

The series (0.6) has one complete formal fan and a second translated
last-level boundary.  A genuine second start requires the whole reduced
condition (0.2), including the marked predecessor chronology through all
upper levels.  These are different events.

The distinction is literal, not merely a concern about terminology.  On
the rank-three PBBS cycle

\[
 110100\longmapsto110010\longmapsto101100\longmapsto110100,
\]

two reduced phases satisfy the same tight one-phase equation, but only one
ordered phase lifts through the terminal-zero boundary to the next tight
return.  The unique lift over the other phase fails the return equations.
Thus terminal capacity plus one-phase activity does not determine the
successor incidence in (0.19).

There is a second, independent issue.  The tuples counted by (0.7) are the
exact full-fan capacity envelope.  No bounded-fibre map from all those
tuples to canonical PBBS return towers has been proved.  Therefore the
one-point lower envelope subsequence, and hence its joint refinement
(0.18), cannot be used as a lower bound for \(R_H\) or \(\mathcal C_H\).

Finally, even a genuine estimate \(\mathcal C_H/R_H=\Theta(H)\) would not
alone upper-bound the maximum independent set of the residence conflict
graph: a large second moment can be concentrated in rare dense clusters.
For the quotient packing number \(\overline\nu_H\), the unconditional
direction is only

\[
 \overline\nu_H\ge\frac{R_H^2}{R_H+2\mathcal C_H}.             \tag{5.1}
\]

To prove the desired little-oh one needs a degree-profile or Hall upper
theorem for the actual conflict graph, in addition to divergent clustering
in probability.  To refute it, it is enough to prove critical actual mass
with bounded reduced degree.

Since every quotient start has \(N\) spatial lifts,

\[
 \frac{NB_m}{H}
 =\left(\frac2A+o(1)\right)B_m\sqrt m.            \tag{5.2}
\]

Hence the exact remaining alternatives are

\[
 \sum_FP_m(F)a_H(F)=\Omega(B_m/H),\qquad
 \sum_{u,F}P_m(F)a_H(F)a_H(\tau^uF)=O(B_m/H),     \tag{5.3}
\]

which would give a physical \(\Omega(B_m\sqrt m)\) obstruction after a
bounded-degree extraction, or the stronger degree-in-probability
divergence needed by a positive proof.  The joint profile--boundary
coefficient settles neither side of (5.3).

## 6. Final boundary

The exact asymptotic calculation proves:

1. the genuine outer predecessor-threshold pair kernel, including the
   constants \(9/16\) and \(3/4\);
2. the exact one-profile/second-boundary generating function (0.6);
3. the critical local limit (0.9)--(0.12);
4. the exact cyclic short-lag coefficient (0.15)--(0.17); and
5. formal joint saturation at order \(4^m/m^{3/2}\).

It also proves a useful no-go: the critical profile--boundary coefficient
contains no \(o(1)\) saving.  Any proof of
\(\nu_{A\sqrt m}=o(B_m\sqrt m)\) must use the marked canonical
predecessor incidence omitted by (0.6), and any matching lower bound must
realize critical mass with bounded actual phase degree.  The exact reduced
autocorrelation (1.11), not another coefficient marginal, remains the
decisive unresolved object.
