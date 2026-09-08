# Rank obstruction to absorbing a unit axis beside a short staircase axis

This note proves a deterministic obstruction for the proposed modification of the Appendix A.7 terminal compiler. It does not modify the master handoff or assert any new upper bound.

Let `s,t` be positive integers with `t <= s`, and let `p` belong to `{1,2,3,4}`. Put `h_p=t` and `h_i=s` for `i != p`. Define the coordinatewise ordered staircase

\[
 P_p(t,s)=\{(x_1,\ldots,x_4):0\le x_i<2h_i,
 \quad\mathbf1_{x_1\ge h_1}\ge\cdots\ge\mathbf1_{x_4\ge h_4}\}.
\]

Let `Q_p(t,s)=P_p(t,s) x {0,...,2s-1}`, again ordered coordinatewise. Rank is the sum of its five coordinates. Every rank is an antichain, so its cardinality lower-bounds the width and the number of chains in any chain partition.

For an integer `m >= 1`, write `[m]_q=1+q+...+q^(m-1)`, and set `[0]_q=0`.

## Exact rank polynomial

The staircase is the disjoint union of its five threshold boxes, indexed by the number of initial high coordinates. The box with the first `j` coordinates high has rank offset `h_1+...+h_j`, and all five boxes have rank polynomial `[t]_q[s]_q^3` after removing that offset. Therefore

\[
\begin{aligned}
 F_p(q)
 &= [t]_q[s]_q^3[2s]_q
 \left(\sum_{j=0}^{p-1}q^{js}
 +q^{(p-1)s+t}\sum_{j=0}^{4-p}q^{js}\right)\\
 &= [t]_q[s]_q^2[2s]_q
 \left([ps]_q+q^{(p-1)s+t}[(5-p)s]_q\right)\\
 &= \boxed{[t]_q[s]_q^2[2s]_q
 \left([4s+t]_q+q^{(p-1)s+t}[s-t]_q\right)}.
\end{aligned}
\]

For the final equality, the first interval of exponents is `[0,ps-1]`; the second is `[(p-1)s+t,4s+t-1]`. They cover the entire interval `[0,4s+t-1]` and overlap on `[(p-1)s+t,ps-1]`, whose length is `s-t`. This proves the polynomial identity without computation.

## The antichain obstruction

Put `L=4s+t` and `C(q)=[t]_q[s]_q^2[2s]_q`. Then `deg C=L-4` and `C(1)=2ts^3`. Consequently every coefficient of `C(q)[L]_q` at ranks `L-4,L-3,L-2,L-1` equals `2ts^3`: the convolution includes every coefficient of `C` at each of those ranks.

When `t<s`, the correction `q^a C(q)[s-t]_q`, where `a=(p-1)s+t`, has positive coefficients at every integer in its support `[a,a+5s-5]`. This support intersects `[L-4,L-1]`: indeed `a<=L-1`, and `a+5s-5>=L-4` for `s>=2`. (There are no positive integers `t<s` when `s=1`.) Hence

\[
 \boxed{\operatorname{width}Q_p(t,s)>2ts^3\qquad(1\le t<s).}
\]

This lower bound uses only rank antichains. It applies to arbitrary chain partitions, whether saturated, symmetric, or otherwise.

## A quantitative excess

Define

\[
 E(s,t)=\binom{s+3}{4}-\binom{s-t+3}{4}-\binom{t+3}{4}.
\]

It equals the coefficient of `q^(s-1)` in

\[
 D(q)=[t]_q[s-t]_q[s]_q^2[2s]_q.
\]

To see this, the three factors `[s]_q,[s]_q,[2s]_q` impose no upper-bound restriction at total rank `s-1`. Thus the coefficient is that of `q^(s-1)` in `(1-q^t)(1-q^(s-t))/(1-q)^5`, giving exactly the displayed binomial formula. The coefficient is strictly positive when `1<=t<s`, since both first factors permit zero and the final three factors permit a coordinate sum of `s-1`.

Choose plateau rank `L-4` for `p=1,2`, and `L-1` for `p=3,4`. The corresponding correction coefficient is `E(s,t)` for the outer positions `p=1,4`, by symmetry of `D` around degree `(5s-5)/2`. For the inner positions it is the coefficient of `q^(2s-1)` in `D`, which is at least `E(s,t)`: increasing the final `[2s]` coordinate by `s` injects rank `s-1` into rank `2s-1`, since that coordinate is initially at most `s-1`.

Therefore, uniformly in the short-axis position,

\[
 \boxed{\operatorname{width}Q_p(t,s)\ge 2ts^3+E(s,t).}
\]

Writing `z_s=t/s`, elementary expansion of the binomials gives the uniform finite-size expansion

\[
 E(s,t)=\frac{1-(1-z_s)^4-z_s^4}{24}s^4+O(s^3).
\]

If `z_s -> z` in `(0,1)`, it follows that `E(s,t)=[1-(1-z)^4-z^4]s^4/24+o(s^4)`. The leading coefficient is positive. Thus the obstruction persists at principal order, not just as an additive finite-size defect. The remainder relative to the limiting `z` is `O(s^3)` if the stronger assumption `t=zs+O(1)` is made.

## Consequence for the paired compiler charge

The proposed swap pairs the short-axis staircase (membership `5ts^3`) with a standard four-axis staircase (membership `5s^4`, chain count `s^3`) and absorbs a unit-length axis `[2s]` into the short staircase. Its proposed principal charge per macro row is

\[
 (2s)(5ts^3)s^3+(5s^4)\operatorname{width}Q_p(t,s).
\]

The width bound makes this at least

\[
 \boxed{20ts^7+5s^4E(s,t)>20ts^7\quad(t<s).}
\]

The original compiler, which absorbs the short axis `[2t]` into a standard staircase, has charge `20ts^7`. Hence this swap cannot reduce its coefficient. At `t=s` the correction vanishes, and Appendix A.7's existing chain partition attains width `2s^4`, giving equality.

## Verification record

After deriving the identity, an independent exact-integer polynomial check was run through `ssh h100`, covering every `2<=s<=16`, `1<=t<s`, and all four positions. It verified the complete polynomial factorization and the quantitative rank-antichain bound. All numerical calculations were performed on h100; the proof above does not depend on that check.
