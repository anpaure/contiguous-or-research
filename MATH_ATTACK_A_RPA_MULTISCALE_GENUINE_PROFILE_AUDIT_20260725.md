# Audit of the multiscale genuine protected-sector profile

Date: 2026-07-25

Method: pure mathematics only. No finite search, solver, computation, or
web search is used.

## 0. Verdict

The proposed construction is valid, with two notation clarifications:

1. the sparse indices are (J_t=10^t) for (1\le t\le K);
2. the final bound is

   \[
   Q\,H>\frac9{10}\bigl(2e^{-3/5}\bigr)^K,
   \tag{0.1}
   \]

   where (QH) means the product (Q\cdot H), and the exponential is
   (e^{-3/5}), not (e^{-3}/5).

Since (2e^{-3/5}>1), this is a genuine-return counterprofile to every
universal estimate

\[
 Q=O(H/r_0).
\]

It is not a counterexample to \(\mathrm{RP}_A\): it refutes only this
proposed pointwise profile-product strengthening.

## 1. Construction and exact pruning ranks

Fix (K\ge1) and put

\[
 H=10^{3K},
 \qquad
 \ell=10^K,
 \qquad
 J_t=10^t\quad(1\le t\le K).
\]

Use a first-deepest spine of height (H).  Put every pre-spine sector
(A_i) equal to the empty forest.  In the post-spine sector at depth
(J_t), put a forest of path branches with multiplicity

\[
 Y_t=2^{K-t}10^{3K-t}
     =\frac{2^{K-t}H}{J_t}
 \quad\text{at length }J_t,
 \tag{1.1}
\]

together with, in the post-spine sector at depth one,

\[
 y_1=H^2-2^KH
 \tag{1.2}
\]

additional length-one path branches.  All other post-spine sectors are
empty.  Thus, writing (M_a=1^a0^a),

\[
 B_{J_t}=M_{J_t}^{Y_t},
 \qquad
 B_1=M_1^{y_1},
 \tag{1.3}
\]

and the literal contour word is

\[
 D=1^H0B_{H-1}0B_{H-2}\cdots0B_1 0.
 \tag{1.4}
\]

The sparse forest edge mass is

\[
 \sum_{t=1}^KJ_tY_t
 =H\sum_{t=1}^K2^{K-t}
 =H(2^K-1).
\tag{1.5}
\]

Hence the total semilength is exactly

\[
 r_0
 =H+y_1+\sum_tJ_tY_t
 =H^2.
\tag{1.6}
\]

After (j) simultaneous peak-pruning rounds, a path branch of length
(a) contributes ((a-j)_+) edges.  Therefore

\[
 \boxed{
 r_j=H-j+\sum_{a>j}(a-j)y_a.}
\tag{1.7}
\]

The longest side branches have length (J_K=\ell), and

\[
 Y_K=10^{2K}>0.
\]

Thus side forest remains at every (j<\ell), while it is empty at
(j=\ell).  Consequently

\[
 r_j>H-j\quad(j<\ell),
 \qquad
 r_\ell=H-\ell,
\tag{1.8}
\]

so (ell) is exactly the first mountain depth.

The second rank difference in (1.7) is

\[
 r_{j-1}-2r_j+r_{j+1}=y_j,
\tag{1.9}
\]

where (y_j) denotes the number of side path branches of length (j).
Thus these branch multiplicities are exactly the Pascal inverse-fibre
free masses used in the product below.

## 2. Chronology and genuine zero winding

The root-before-spine terminal-tower placement is not used: a pre-spine
forest can become the canonical first deepest forest after transport, so
that placement does not satisfy the audited no-preemption hypothesis.

For the sectors in Section 1, however,

\[
 A_i=\varnothing\quad(0\le i<H),
 \tag{2.1}
\]

and every nonempty (B_a) is a forest of paths of relative height exactly
(a).  Hence

\[
 \operatorname{fht}(B_a)=a\le a.
 \tag{2.2}
\]

The original attachment is also legal because all supported (a) satisfy

\[
 a\le\ell< H/2,
 \qquad
 a\le H-a.
 \tag{2.3}
\]

Proposition 6.1 of
`PBBS_ZERO_WINDING_CONVERSE_COUNTERAUDIT_20260725.md` therefore applies
exactly.  It states that the displayed spine remains the canonical first
deepest spine through all (H) sector shifts.  If (C_j) is the
cumulative step-two deficit, then

\[
 \delta(D_j)-C_j=H-j>0\quad(0\le j<H),
 \qquad
 \delta(D_H)=C_H.
 \tag{2.4}
\]

Thus the initial omitted coordinate has its first return after (H)
step-two moves and the final odd move.  This is a genuine zero-winding
return of exact gap

\[
 \boxed{2H+1}.                                    \tag{2.5}
\]

There is no modular ambiguity: the total forest size is (H^2-H), so

\[
 C_H=H+2(H^2-H)=2H^2-H<2H^2+1,
 \tag{2.6}
\]

the outer circumference.

## 3. Exact product estimate

For

\[
 P_j=\prod_{i=0}^{j-1}
 \frac{2r_j-i}{2r_j+y_j-i},
 \qquad
 Q=\prod_{j=1}^{\ell}P_j,
 \tag{3.1}
\]

all factors with (j\notin\{1,J_1,\ldots,J_K\}) equal one.

For (1\le t\le K), put

\[
 G_t=H+\sum_{u>t}J_uY_u=2^{K-t}H.
 \tag{3.2}
\]

Formula (1.7) gives

\[
 r_{J_t}=G_t-J_t\left(1+\sum_{u>t}Y_u\right).
 \tag{3.3}
\]

Moreover,

\[
 \begin{aligned}
 \frac{J_t(1+\sum_{u>t}Y_u)}{G_t}
 &\le10^{-2K}+\sum_{v\ge1}20^{-v}\\
 &\le\frac1{100}+\frac1{19}
 =\frac{119}{1900}.
 \end{aligned}
 \tag{3.4}
\]

Here (J_t/G_t\le10^{-2K}\), and the (u=t+v) summand is exactly
(20^{-v}).  Therefore

\[
 2r_{J_t}-J_t+1
 >\frac{3543}{1900}G_t
 >\frac53G_t.
 \tag{3.5}
\]

Since (J_tY_t=G_t), the inequality
(log(1+x)\le x) gives

\[
 \begin{aligned}
 -\log P_{J_t}
 &=\sum_{i=0}^{J_t-1}
   \log\left(1+\frac{Y_t}{2r_{J_t}-i}\right)\\
 &\le
 \frac{J_tY_t}{2r_{J_t}-J_t+1}
 <\frac35.
 \end{aligned}
 \tag{3.6}
\]

Thus

\[
 \prod_{t=1}^KP_{J_t}>e^{-3K/5}.
 \tag{3.7}
\]

For the length-one factor, let

\[
 \widetilde R=H+\sum_tJ_tY_t=2^KH.
\]

Then

\[
 r_1=\widetilde R-\left(1+\sum_tY_t\right),
 \tag{3.8}
\]

and

\[
 \frac{1+\sum_tY_t}{\widetilde R}
 \le\frac1{\widetilde R}+\sum_{t\ge1}20^{-t}
 <\frac1{10}.
 \tag{3.9}
\]

Hence (r_1>(9/10)\widetilde R).  Since

\[
 y_1=H^2-\widetilde R,
 \qquad
 \widetilde R\le H^2,
\]

we have

\[
 2r_1+y_1\le H^2+\widetilde R\le2H^2,
\]

and therefore

\[
 P_1=\frac{2r_1}{2r_1+y_1}
 >\frac9{10}\frac{2^K}{H}.
 \tag{3.10}
\]

Combining (3.7), (3.10), and (r_0/H=H) proves

\[
 \boxed{
 Q\frac{r_0}{H}
 =QH
 >\frac9{10}\bigl(2e^{-3/5}\bigr)^K.}
 \tag{3.11}
\]

Finally,

\[
 2e^{-3/5}>1
\]

because (log2>3/5) (for example,
(log2=\int_1^2x^{-1}\,dx>3/5) by the elementary lower Riemann sum on
five equal subintervals).  Hence the right side of (3.11) is unbounded.

## 4. Adversarial boundary

* The construction proves a genuine dynamic profile, not merely a convex
  rank string: the audited protected-sector criterion supplies the literal
  first return.
* The condition (1\le t\le K) is essential; (t=0) would duplicate the
  separately prescribed length-one mass.
* The factor (Q) is the exact zero-value Pascal-fan envelope for this
  profile.  Since (j\le\ell\ll H-j\le r_j), no cyclic slot saturation or
  wrap changes the displayed (j)-fold factors.
* This invalidates (Q=O(H/r_0)), but does not invalidate the proved
  universal square-root bound (Q\le\sqrt{H/r_0}), nor does it count enough
  distinct roots to decide \(\mathrm{RP}_A\).
