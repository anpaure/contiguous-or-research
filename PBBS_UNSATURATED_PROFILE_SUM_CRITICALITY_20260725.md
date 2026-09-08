# Exact unsaturated pruning-profile sum and the surviving critical obstruction

Date: 2026-07-25

Method: pure mathematics only.  No computation, finite search, solver, or
web search is used.

## 0. Result

Fix a genuine zero-winding PBBS return of height/duration (s).  Let

\[
 p=\min\{j:r_j=s-j\},\qquad q=s-p,
\]

and assume the unsaturated inequality

\[
 p<2q.
\tag{0.1}
\]

At level (p) the pruned root is the mountain (M_q).  Put

\[
 b=2q-p+1=2s-3p+1.
\tag{0.2}
\]

Thus (0.1) is exactly (b\ge2).  Let

\[
 Q_0(z)=Q_1(z)=1,\qquad
 Q_{j+1}(z)=Q_j(z)-zQ_{j-1}(z),
\]

and (C_j(z)=Q_j(z)/Q_{j+1}(z)).

For fixed (r,s,p), let \(\mathcal E_{r;s,p}\) be the complete
full-depth Pascal-fan **capacity envelope**, summed over every convex
pruning-rank profile with first mountain depth exactly (p).  This is an
upper bound for the number of genuine returns with those parameters; it
does not assert that every tower counted by the envelope is dynamically
realizable.

### Theorem 0.1 (exact profile-sum collapse)

One has

\[
 \boxed{
 \mathcal E_{r;s,p}
 =[z^{r-s}]\,\mathscr F^\star_{s,p}(z),}
\tag{0.3}
\]

where

\[
 \boxed{
 \mathscr F^\star_{s,p}(z)
 =\frac{C_p(z)^b}{Q_p(z)^3}
 \left[1-\left(1-\frac{z^p}{Q_p(z)^2}\right)^b\right].}
\tag{0.4}
\]

The bracket in (0.4) is the exact correction (y_p\ge1) saying that
(p), rather than an earlier level, is the first mountain depth.

At the critical point,

\[
 \boxed{
 4^{-s}\mathscr F^\star_{s,p}(1/4)
 =\frac{2}{(p+1)^3}
 \left(\frac{p+1}{p+2}\right)^b
 \left[1-\left(1-\frac1{(p+1)^2}\right)^b\right].}
\tag{0.5}
\]

In particular,

\[
 4^{-s}\mathscr F^\star_{s,p}(1/4)
 \le
 \frac{Cb}{(p+1)^5}e^{-cb/(p+1)}.
\tag{0.6}
\]

### Theorem 0.2 (aggregate capacity is coefficient-one critical)

For every fixed (A>0),

\[
 \boxed{
 \sum_{\substack{s\le A\sqrt r\\p<2(s-p)}}
 \mathcal E_{r;s,p}
 =O_A(4^r/r^2)
 =O_A(\operatorname{Cat}_r/\sqrt r).}
\tag{0.7}
\]

More sharply,

\[
 \boxed{
 \lim_{\varepsilon\downarrow0}\limsup_{r\to\infty}
 \frac{r^2}{4^r}
 \sum_{\substack{s\le A\sqrt r\\
                  p\le\varepsilon\sqrt r\\
                  p<2(s-p)}}
 \mathcal E_{r;s,p}=0.}
\tag{0.7a}
\]

Thus every common envelope \(p=o(\sqrt r)\) is negligible already at
start-count level, for all endpoint overlaps simultaneously.  Only
\(p\asymp\sqrt r\) can remain critical.

This is a genuine improvement over every pointwise-profile estimate: the
full profile sum itself reaches the coefficient-one quotient scale.
However, the order in (0.7) cannot be replaced by little-oh using the
capacity envelope alone.  There are a fixed (A), a constant (c>0),
and arbitrarily large (r) for which

\[
 \boxed{
 \sum_{\substack{s\le A\sqrt r\\p<2(s-p)}}
 \mathcal E_{r;s,p}
 \ge c,4^r/r^2.}
\tag{0.8}
\]

Thus exact summation over profiles removes all polynomial loss but remains
exactly critical.

### Theorem 0.3 (the strip bound is marginally inactive at the frontier)

In the critical cells

\[
 p\asymp s\asymp\sqrt r,\qquad b\asymp p,
\tag{0.9}
\]

the coefficient bound underlying (0.7) is (O(4^r/r^3)) for each
((s,p)).  At the first overlap scale not removed by the log-free
shared-boundary theorem,

\[
 \lambda=\lceil r^{1/5}\rceil,
\tag{0.10}
\]

the pruning-strip estimate permits

\[
 C4^r\frac{(\lambda+2)^2}{s^6\sqrt{\lambda+1}}
 =\Theta(4^r/r^{27/10}),
\tag{0.11}
\]

which is larger than (4^r/r^3) by (r^{3/10}).  Moreover

\[
 \lambda<K(p+1)^2\log r.
\]

Consequently the presently known strip bound imposes no further marginal
restriction on a critical fan-profile cell.  A proof of little-oh must
couple the boundary word to the inverse-fibre profile, or use genuine
cross-phase/edge-packing chronology.  Multiplying or taking minima of the
two already proved marginal bounds cannot justify that coupling.

Even the stronger strip estimate summed over \(p\) remains exactly
critical.  For one fixed \(s\asymp\sqrt r\), there are
\(\Theta(\sqrt r)\) critical \(p\)-cells, of total fan-envelope capacity
\(O(4^r/r^{5/2})\).  The overlap window

\[
 r^{1/5}\le\lambda\le2r^{1/5}
\]

contains \(\Theta(r^{1/5})\) cells, each with global (already
\(p\)-summed) strip capacity \(O(4^r/r^{27/10})\).  Their total is again

\[
 \Theta(r^{1/5})\,\frac{4^r}{r^{27/10}}
 =\Theta(4^r/r^{5/2}).
\]

Thus the exponents match on each fixed-height slice as well.

## 1. Profiles as weighted partitions

For (1\le j\le p), put

\[
 y_j=r_{j-1}-2r_j+r_{j+1}\ge0.
\tag{1.1}
\]

Since

\[
 r_p=q,\qquad r_{p+1}=q-1,
\]

successive summation of (1.1) gives

\[
 \boxed{
 r_j=s-j+\sum_{a=j+1}^p(a-j)y_a,}
\tag{1.2}
\]

and in particular

\[
 \boxed{r=s+\sum_{a=1}^p a y_a.}
\tag{1.3}
\]

The condition that (p) be the *first* mountain level is exactly

\[
 \boxed{y_p\ge1.}
\tag{1.4}
\]

Indeed, (1.2) gives

\[
 r_j-(s-j)=\sum_{a=j+1}^p(a-j)y_a.
\]

If (y_p\ge1), this is positive for every (j<p).  Conversely,
(r_{p-1}>q+1) says (y_p=r_{p-1}-q-1\ge1).

Because (p<2q\le2r_j), the wrapped full-depth fan theorem has

\[
 t_j=j\qquad(1\le j\le p).
\tag{1.5}
\]

For a fixed profile and the unique bottom mountain (M_q), its complete
fan-capacity envelope is therefore

\[
 \prod_{j=1}^p
 \binom{y_j+2r_j-j}{y_j}.
\tag{1.6}
\]

This is the product of the exact unrestricted inverse-fibre sizes with
the full Pascal-fan capacity ratios.  Hence

\[
 \mathcal E_{r;s,p}
 =\sum_{\substack{y_1,\ldots,y_p\ge0\\
                  y_p\ge1\\
                  \sum j y_j=r-s}}
   \prod_{j=1}^p\binom{y_j+2r_j-j}{y_j}.
\tag{1.7}
\]

## 2. Proof of the generating-function collapse

First omit the restriction (y_p\ge1).  By (1.2),

\[
 2r_j-j
 =2s-3j+2\sum_{a>j}(a-j)y_a.
\tag{2.1}
\]

Put

\[
 b_j=2s-3j+1
\tag{2.2}
\]

and define recursively

\[
 t_j=z^j\prod_{i<j}(1-t_i)^{-2(j-i)}.
\tag{2.3}
\]

Summing (y_1,y_2,\ldots,y_p) in this order and using

\[
 \sum_{y\ge0}\binom{y+A}{y}t^y=(1-t)^{-A-1}
\]

gives the exact formal-power-series identity

\[
 \mathscr F_{s,p}(z)
 :=\sum_{\mathbf y\ge0}
 \prod_j\binom{y_j+2r_j-j}{y_j}z^{\sum j y_j}
 =\prod_{j=1}^p(1-t_j)^{-b_j}.
\tag{2.4}
\]

The continuants satisfy the Cassini identity

\[
 Q_j(z)^2-z^j=Q_{j-1}(z)Q_{j+1}(z).
\tag{2.5}
\]

Induction in (2.3), with telescoping of the second differences, now gives

\[
 \boxed{t_j=\frac{z^j}{Q_j(z)^2},}
\tag{2.6}
\]

and therefore

\[
 1-t_j=\frac{Q_{j-1}Q_{j+1}}{Q_j^2}.
\tag{2.7}
\]

Since (b_{j-1}-b_j=3), all interior powers of the (Q_j)'s cancel in
(2.4), leaving

\[
 \boxed{
 \mathscr F_{s,p}(z)
 =\frac{Q_p(z)^{b-3}}{Q_{p+1}(z)^b}
 =\frac{C_p(z)^b}{Q_p(z)^3}.}
\tag{2.8}
\]

In (2.4), the final (y_p)-sum is ((1-t_p)^{-b}).  Restricting it to
(y_p\ge1) replaces this by ((1-t_p)^{-b}-1).  Thus

\[
 \mathscr F^\star_{s,p}
 =\mathscr F_{s,p}[1-(1-t_p)^b],
\]

which proves (0.3)--(0.4).

At (z=1/4),

\[
 Q_j(1/4)=\frac{j+1}{2^j},\qquad
 C_j(1/4)=\frac{2(j+1)}{j+2},\qquad
 t_j(1/4)=\frac1{(j+1)^2}.
\tag{2.9}
\]

Substitution proves (0.5), and

\[
 1-(1-x)^b\le\min\{1,bx\},\qquad
 \left(1-\frac1{p+2}\right)^b\le e^{-b/(p+2)}
\]

prove (0.6).

## 3. A tilted first-passage coefficient lemma

We use the following uniform form of the audited (1/Q_J)
anti-concentration estimate.

### Lemma 3.1

There are absolute (c,C>0) such that, for (p\ge2), (b\ge2),
(s=(b+3p-1)/2\le A\sqrt r), and (n=r-s\ge r/2),

\[
 \boxed{
 [z^n]\mathscr F^\star_{s,p}(z)
 \le
 C_A,4^n\mathscr F^\star_{s,p}(1/4),p^{-2}
 \exp\!\left(-\frac{cr}{p^2}+\frac{Cb}{p}\right).}
\tag{3.1}
\]

#### Proof

Before the final (y_p)-sum, (2.8) at depth (p-1) gives

\[
 \mathscr F_{<p}(z)
 =\frac{C_{p-1}(z)^{b+3}}{Q_{p-1}(z)^3}.
\tag{3.2}
\]

Moreover

\[
 \mathscr F^\star_{s,p}
 =\mathscr F_{<p}\big((1-t_p)^{-b}-1\big).
\tag{3.3}
\]

All factors in (3.3) have nonnegative coefficients, and (3.2) contains
one independent (1/Q_{p-1}) factor.  Take

\[
 z_p=\frac14\left(1+\frac{\kappa}{p^2}\right)
\]

with fixed sufficiently small absolute (kappa>0).  It lies a fixed
scaled distance below the first zero of (Q_p).  The exact path-kernel
Fourier estimate used for the critical (1/Q_J) law is uniform in this
compact scaled window and gives

\[
 \sup_k
 \frac{[z^k]Q_{p-1}(z)^{-1}\,z_p^k}{Q_{p-1}(z_p)^{-1}}
 \le Cp^{-2}.
\tag{3.4}
\]

Here is a direct proof of the required uniformity.  The zeros of
\(Q_{p-1}\) are

\[
 \rho_k=\frac1{4\cos^2(k\pi/p)}
 \qquad(1\le k<p/2),
\]

with the usual harmless terminal linear factor when the parity requires
it.  Choose \(\kappa<\pi^2/4\), and put
\(a_k=z_p/\rho_k\).  For \(k=1,2\) and all sufficiently large \(p\),

\[
 c_kp^{-2}\le1-a_k\le C_kp^{-2},
 \qquad a_k\ge\frac12.
\]

The root product for \(Q_{p-1}\) gives

\[
 \left|\frac{Q_{p-1}(z_p)}
 {Q_{p-1}(z_pe^{it})}\right|
 =
 \prod_k\frac{1-a_k}{|1-a_ke^{it}|}.
\]

Every factor is at most one.  For \(|t|\le\pi\),

\[
 |1-a_ke^{it}|^2
 =(1-a_k)^2+4a_k\sin^2(t/2)
 \ge c\big((1-a_k)^2+t^2\big).
\]

Keeping only \(k=1,2\) therefore yields

\[
 \left|\frac{Q_{p-1}(z_p)}
 {Q_{p-1}(z_pe^{it})}\right|
 \le
 \frac{Cp^{-4}}{(p^{-2}+|t|)^2}.
\]

Its integral is \(O(p^{-2})\), and Fourier inversion proves (3.4).
The finitely many \(p<5\), for which two nontrivial poles need not be
present, are absorbed into the constant.

Convolution with the other positive factors cannot increase the largest
atom.

For completeness, the needed partition-ratio bound follows directly
from the same continuant formula.  Uniformly for
(z\in[1/4,z_p]),

\[
 D\log Q_j(z)^{-1}=O(p^2),\qquad
 D\log C_p(z)=O(p),
\]

for (j\in\{p-1,p\}), where (D=z\,d/dz).  The last positive factor in
(3.3), conditioned to be nonempty, has logarithmic mean \(O(p^2+b)\):
at (1/4), (t_p=(p+1)^{-2}), its negative-binomial count has conditional
mean (O(1+b/p^2)), and (D\log t_p=O(p^2)); these estimates remain
uniform in the chosen scaled window.  Across the relative tilt
\(z_p/(1/4)-1=O(p^{-2})\), this contributes only
\(O(1+b/p^2)\), which is dominated by the displayed
\(O(1+b/p)\) bound below.  Hence

\[
 \log\frac{\mathscr F^\star_{s,p}(z_p)}
               {\mathscr F^\star_{s,p}(1/4)}
 \le C\left(1+\frac bp\right).
\tag{3.5}
\]

Coefficient tilting at (z_p), followed by (3.4)--(3.5), gives

\[
 \frac{[z^n]\mathscr F^\star_{s,p}(z)4^{-n}}
      {\mathscr F^\star_{s,p}(1/4)}
 \le Cp^{-2}
 \left(1+\frac\kappa{p^2}\right)^{-n}
 e^{C(1+b/p)},
\]

which is (3.1).  The finitely many small (p) are absorbed by changing
the constants. \(\square\)

## 4. Proof of the aggregate upper bound

Combine (0.5) and Lemma 3.1.  Since (n\ge r/2),

\[
 \mathcal E_{r;s,p}
 \le
 C_A4^r\frac{b}{(p+1)^7}
 \exp\!\left(-\frac{cr}{p^2}+\frac{Cb}{p}\right).
\tag{4.1}
\]

Here we discarded the additional favorable factor (e^{-cb/p}).  Since
(b\le2s\le2A\sqrt r), completing the square in
(x=\sqrt r/p) yields

\[
 -cx^2+C_Ax\le-c'x^2+C'_A.
\tag{4.2}
\]

For each (p), summing (b) over its allowed parity class and enlarging
to (1\le b\le2A\sqrt r) gives

\[
 \sum_b\mathcal E_{r;s,p}
 \le C_A4^r\,r\,(p+1)^{-7}e^{-c'r/p^2}.
\tag{4.3}
\]

The integral substitution (u=r/x^2) gives

\[
 \sum_{p\ge1}(p+1)^{-7}e^{-c'r/p^2}=O(r^{-3}).
\tag{4.4}
\]

Equations (4.3)--(4.4) prove (0.7).

If the sum in (4.4) is restricted to \(p\le\varepsilon\sqrt r\), the
same substitution gives

\[
 \sum_{p\le\varepsilon\sqrt r}
 (p+1)^{-7}e^{-c'r/p^2}
 \le
 Cr^{-3}\int_{\varepsilon^{-2}}^\infty u^2e^{-c'u}\,du.
\]

The integral tends to zero with \(\varepsilon\downarrow0\), proving
(0.7a).  As usual, the two-limit statement yields a deterministic
envelope \(\varepsilon(r)\downarrow0\) by diagonalization.

## 5. The envelope really is critical

We give an averaged lower bound which avoids claiming that the capacity
envelope is dynamically attained.

### Lemma 5.1

Normalize a positive series at (z=1/4).  If (X_h) has probability
generating function (C_h(z)/C_h(1/4)), then

\[
 \mathbb EX_h=\frac h3,qquad
 \operatorname{Var}(X_h)=O(h^3).
\tag{5.1}
\]

Consequently the normalized (1/Q_{p-1}=\prod_{h=1}^{p-2}C_h) law has
mean (Theta(p^2)), variance (O(p^4)), and there are absolute
(c_0,C_0,\eta>0) such that

\[
 \Pr(c_0p^2\le X\le C_0p^2)\ge\eta.
\tag{5.2}
\]

#### Proof

The capped Catalan recursion is

\[
 C_h=(1-zC_{h-1})^{-1}.
\]

At (z=1/4), the number of primitive arches is geometric.  Its mean is
(h/(h+2)) and its variance is (2h(h+1)/(h+2)^2).  Therefore, with
(\mu_h=\mathbb EX_h) and (v_h=\operatorname{Var}(X_h)),

\[
 \mu_h=\frac h{h+2}(1+\mu_{h-1}),
\]

which gives (mu_h=h/3), and

\[
 v_h=\frac h{h+2}v_{h-1}
     +\frac{2h(h+1)}{(h+2)^2}(1+\mu_{h-1})^2
 =\frac h{h+2}v_{h-1}+\frac{2h(h+1)}9.
\]

Thus (v_h=O(h^3)).  Independence in the product gives the asserted
mean and variance for (1/Q_{p-1}).  Paley--Zygmund supplies the lower
cutoff in (5.2), and Markov's inequality supplies the upper cutoff.
\(\square\)

Now restrict to

\[
 p\le b\le2p
\tag{5.3}
\]

with the required parity.  Then (s=(b+3p-1)/2=\Theta(p)), and (0.5)
gives uniformly

\[
 \boxed{4^{-s}\mathscr F^\star_{s,p}(1/4)=\Theta(p^{-4}).}
\tag{5.4}
\]

The normalized law of (mathscr F^\star_{s,p}) contains the
(1/Q_{p-1}) factor from Lemma 5.1.  Its remaining factors have total
mean (O(p^2)): the (b+3=O(p)) copies of (C_{p-1}) contribute
(O(p^2)), the other two (1/Q_{p-1}) factors contribute (O(p^2)),
and the nonempty final negative-binomial factor has conditional mean
(O(p^2)).  Hence, after increasing (C_0),

\[
 \Pr(c_0p^2\le X\le C_0p^2)\ge\eta'
\tag{5.5}
\]

uniformly in (5.3).

Fix a large (R), take (p\in[\sqrt R,2\sqrt R]), and take all (b)
in (5.3).  There are (Theta(R)) pairs.  Equations (5.4)--(5.5) show
that their total normalized coefficient mass, for

\[
 r=(r-s)+s\in[cR,CR],
\]

is at least (c/R).  The displayed interval contains (O(R)) integers,
so for at least one such (r),

\[
 4^{-r}\sum_{s,p}\mathcal E_{r;s,p}\ge c/R^2\asymp c/r^2.
\]

Also (s=\Theta(p)\le A\sqrt r) for one fixed (A), and (5.3) implies
(p<2q) with room to spare.  This proves (0.8).

## 6. Why the known strip collision does not make the sum strict

In the cells used in Section 5,

\[
 p\asymp s\asymp\sqrt r,\qquad b\asymp p.
\]

Equation (4.1), without its bounded exponential factors, gives

\[
 \mathcal E_{r;s,p}=O(4^r/r^3).
\tag{6.1}
\]

Take (lambda=\lceil r^{1/5}\rceil).  Since
(lambda/p^2=O(r^{-4/5})), the minimum in the pruning-strip theorem is
the central-binomial term.  Its right side is

\[
 C4^r\frac{\lambda^{3/2}}{s^6}
 =\Theta(4^r/r^{27/10}).
\tag{6.2}
\]

The ratio of (6.2) to (6.1) is (r^{3/10}).  Therefore an abstract load
table can place the complete critical fan-envelope mass of each
((s,p))-cell into the surviving overlap window without violating the
\(p\)-refined strip upper bound.  If one also imposes the stronger strip
estimate before splitting by \(p\), group \(O(r^{3/10})\) profile cells
at each overlap value.  There are \(r^{1/5}\) overlap values and hence
total capacity for \(r^{1/2}\) profile cells, exactly the number present
at fixed \(s\).  The overlap obeys

\[
 \lambda<K(p+1)^2\log r
\]

and lies just beyond every deterministic envelope (o(r^{1/5})) removed
by the log-free shared-boundary theorem.

This does not construct genuine PBBS returns attaining the envelope.  It
proves the exact implication boundary: the full profile capacity sum and
the pruning-strip collision estimate, viewed only through their present
marginals, are mutually compatible with a (Theta(\operatorname{Cat}_r/
\sqrt r)) residual.

## 7. Exact remaining theorem in this lane

The residual can now be stated more sharply than a generic profile sum.
One needs one of the following genuinely joint statements in the critical
window (p,s,b\asymp\sqrt r):

1. **Profile--boundary coupling:** after fixing the pruning profile, the
   common boundary collision has an additional (o(1)) factor beyond
   the marginal strip estimate;
2. **capacity slack:** the prescribed transported fan values have positive
   total or further compatibility often enough that the actual inverse
   fibre is (o(1)) of the zero-value envelope (1.6), on aggregate;
3. **descendant packing:** quotient-edge-disjoint parent returns have
   (o(1)) occupancy after charging their complete triangular descendant
   fans across pruning levels.

The exact profile summation has therefore succeeded up to the last
strictness: it proves an (O(1)) coefficient-one bound for this envelope.
The missing theorem is now precisely an (o(1)) chronology gain, not a
further polynomial estimate in (p,s), or (lambda).
