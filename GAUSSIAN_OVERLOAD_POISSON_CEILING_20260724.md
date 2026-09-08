# Poisson shadow loads: the exact remaining `sqrt(m)` factor

## 1. Conclusion

The improved partial-packing threshold

```text
L=o(W/m^(1/3))
```

does remove the old *middle-leftover* obstruction.  An idealized nibble
leftover of order `W/sqrt(m)` would now be more than small enough.

It does not make an unstructured random middle matching sufficient.  In the
independent occupancy null model for its nonmiddle shadows, the exact
Gaussian-weighted balanced overload is

```text
Theta(W sqrt(m)),
```

and the Gaussian quadratic energy has the same order.  The transfer needs
`o(W)`.  Thus independence misses the remaining target by the exact factor
`sqrt(m)`.  Gaussian weights suppress all depths beyond order `sqrt(m)`, but
they cannot suppress the `Theta(sqrt(m))` shallow ranks whose mean load is
still constant.

This is a rigorous ceiling for every argument which replaces the lower
shadows of a middle packing by independent multinomial/Poisson occupancies.
It is not a nonexistence theorem for correlated wreath factors.  A successful
construction must make the shallow shadows strongly sub-Poisson, or use
switching/absorption that directly reduces their balanced overload.

## 2. Exact balanced overload of one occupancy vector

Place `T` labelled balls independently and uniformly into `N` targets and
condition on the resulting load vector

```text
X=(X_1,...,X_N),  sum_i X_i=T.
```

Write

```text
T=cN+r,  0<=r<N,
theta=r/N.
```

A balanced quota vector has `r` entries `c+1` and `N-r` entries `c`.
Let `O(X)` be its minimum overload.  Define

```text
A_N=sum_i (X_i-c-1)_+,
B_N=sum_i (c-X_i)_+,
Z_N=#{i:X_i>=c+1}.
```

### Lemma 2.1 (exact order-statistic identity)

```text
O(X)=max(A_N,B_N).
```

#### Proof

Put `delta_i=X_i-c`.  The positive deviations have total `Z_N+A_N`, the
negative deviations have total `B_N`, and `sum delta_i=r`.  Hence

```text
A_N-B_N=r-Z_N.                                      (2.1)
```

If `Z_N>=r`, assign all `r` high quotas to positive deviations.  The
remaining overload is `Z_N+A_N-r=B_N`.  If `Z_N<r`, assign high quotas to
all positive deviations; the overload is `A_N`.  These assignments are
optimal by exchanging a high quota from a smaller load to a larger one.
Equation (2.1) says that the applicable expression is always the larger of
`A_N,B_N`.  QED.

Let `P_lambda` be Poisson with mean `lambda`, put

```text
c=floor(lambda),  theta=lambda-c,
A(lambda)=E(P_lambda-c-1)_+,
B(lambda)=E(c-P_lambda)_+,
g(lambda)=max(A(lambda),B(lambda)).                 (2.2)
```

Equivalently, if `p(lambda)=Pr(P_lambda>=c+1)`, then

```text
A(lambda)-B(lambda)=theta-p(lambda).
```

The two definitions from the left and right agree at integer `lambda`,
because a mean-`c` Poisson variable has equal expected positive and negative
deviation from `c`.  Thus `g` is continuous and strictly positive on every
compact subinterval of `(0,infinity)`.

### Proposition 2.2 (Poisson occupancy limit)

If `N->infinity` and `T/N->lambda in (0,infinity)`, then

```text
O(X)/N -> g(lambda)
```

in probability and in `L^1`.

#### Proof

For each fixed `j`, the fraction of boxes of load `j` converges in `L^2` to
`exp(-lambda)lambda^j/j!`; this follows directly from the one- and two-box
multinomial probabilities.  Truncating the sums in `A_N,B_N`, applying this
finite-dimensional convergence, and then removing the truncation using the
uniform second-moment bound proves convergence of `A_N/N` and `B_N/N`.
Lemma 2.1 and uniform integrability finish the proof.  QED.

For later comparison, the quadratic capacity energy has an exact expectation.
Let

```text
Q(X)=(1/2)sum_i(X_i-c)(X_i-c-1).
```

Since an unordered pair of balls collides with probability `1/N`, while the
balanced pair-collision floor is

```text
N binom(c,2)+rc,
```

one obtains

```text
E Q(X)
 = binom(T,2)/N-N binom(c,2)-rc
 = (N/2)(c+theta^2)-lambda/2.                      (2.3)
```

## 3. Wreath-depth scaling

Return to

```text
n=2m+1,
W=binom(n,m),
N_q=binom(n,m-q),
u_{m,q}=W/N_q.
```

The exact ratio satisfies, uniformly for fixed `t` and
`q=floor(t sqrt(m))`,

```text
log u_{m,q}=q(q+1)/m+O(q^3/m^2)=t^2+o(1).          (3.1)
```

Consider the rankwise null model in which the `W` depth-`q` occurrences are
placed multinomially among the `N_q` targets.  The middle row itself may be
kept exact; omitting its single term does not affect the asymptotics.  Put

```text
d_{m,q}=floor(u_{m,q}).
```

For `lambda>=1`, define (values at the countably many integer discontinuities
of the denominator are immaterial)

```text
F_O(lambda)=g(lambda)/(lambda floor(lambda)),
F_Q(lambda)=[floor(lambda)+{lambda}^2]
            /(2 lambda floor(lambda)).             (3.2)
```

### Theorem 3.1 (exact null-model scale)

If `H/sqrt(m)->infinity` and `H=o(m)`, then

```text
E sum_{q=1}^H O_q/d_{m,q}
  =(C_O+o(1))W sqrt(m),

E sum_{q=1}^H Q_q/d_{m,q}
  =(C_Q+o(1))W sqrt(m),                            (3.3)
```

where

```text
C_O=integral_0^infinity F_O(exp(t^2))dt,
C_Q=integral_0^infinity F_Q(exp(t^2))dt.           (3.4)
```

Both constants are finite and strictly positive.

#### Proof

On every fixed interval `0<=q<=A sqrt(m)`, Proposition 2.2 and (3.1) turn
the normalized sums into Riemann sums.  The floor functions have only
finitely many discontinuities on a fixed interval, so they cause no problem.

For domination of the overload tail, choose any balanced quota vector `b`.
Because load and quota have equal total,

```text
O(X)<=(1/2)sum_i|X_i-b_i|.
```

A single load has variance at most `u`, while `|b_i-u|<=1`; hence

```text
E O_q <= (N_q/2)(sqrt(u_{m,q})+1).                 (3.5)
```

For `u>=2`, `floor(u)>=u/2`.  The elementary ratio bound

```text
u_{m,q}>=exp(q(q+1)/(m+q+1))
```

therefore makes the normalized tail of (3.5) at most a constant times the
Gaussian sum `sum_q exp(-q^2/m)`.  Equation (2.3) similarly bounds the
quadratic tail by a constant times `sum_q exp(-2q^2/(3m))`.  After division
by `W sqrt(m)`, both tails tend uniformly to zero as `A->infinity`.

The integrands are positive near `t=0`.  The same Gaussian domination makes
them integrable, proving (3.3)--(3.4).  QED.

The same limits hold for `T=W(1-x_m)` with `x_m->0`, with
`max(1,floor(T/N_q))` in the denominator.  Indeed, on every fixed positive
`t`-interval the mean changes by a factor `1-o(1)`, while the initial range
where it crosses the quota value zero has `o(sqrt(m))` indices.  In
particular, imposing the now-allowed `x_m=o(m^(-1/3))` does not change the
leading null-model overload.

This scale is also typical, not an expectation inflated by rare outcomes.
If the multinomial rows are sampled independently, relocating one ball in
one row changes its minimum overload by at most two and hence changes the
weighted sum by at most two.  McDiarmid's inequality over the `HW` ball
choices gives

```text
Pr(|E_H-E E_H|>z)
 <=2 exp(-z^2/(2HW)).                              (3.6)
```

Taking `z` to be any fixed fraction of `W sqrt(m)` shows

```text
E_H=(C_O+o(1))W sqrt(m)
```

with probability tending to one.  Independence between the rows is not
needed for the expectation calculation, but is part of this concentration
statement and of the null model being ruled out.

## 4. A finite lower bound showing where the factor comes from

The full limit is not needed to see the obstruction.  Choose any fixed
`a<sqrt(log 2)`.  For all `q<=a sqrt(m)` and large `m`, one has
`1<=u_{m,q}<2`, so `d_{m,q}=1`.  Lemma 2.1 gives

```text
O_q>=B_N=#{empty targets}.
```

In the multinomial model,

```text
E #{empty targets}
 =N_q(1-1/N_q)^W
 =(e^{-u_{m,q}}+o(1))N_q
 >=(e^{-2}/3)W                                      (4.1)
```

uniformly after decreasing the harmless absolute constant.  There are
`Theta(sqrt(m))` such ranks.  Thus the lower bound

```text
E E_H >= c W sqrt(m)                               (4.2)
```

already comes entirely from constant-mean shallow shadows.  Deep Gaussian
discounting cannot repair it.

## 5. Consequence for existing matching black boxes

The new leftover threshold reverses one earlier numerical comparison:

```text
W/sqrt(m)=o(W/m^(1/3)).                            (5.1)
```

Thus the *idealized* `W/sqrt(m)` leftover scale obtained by suppressing the
fixed-uniformity restrictions in the Gould--Kelly full-codegree nibble would
now satisfy the Gaussian-capacity transfer's middle-leftover condition.

No presently audited theorem actually supplies that wreath matching:

* Gould--Kelly's stated hierarchy fixes the uniformity, whereas a middle
  wreath has size `2m+1`;
* ABKV's condition fails already for the middle wreath hypergraph because
  its normalized disjoint-pair codegree is at least `2/(m+1)` while its
  uniformity is `2m+1`;
* the audited conflict-free matching theorems also have fixed-rank/vertex
  hypotheses and, in any case, their stated conclusions do not control the
  Gaussian weighted shadow overload.

More importantly, even granting the idealized leftover, any accompanying
analysis which models the lower shadows as independent occupancies gives
`E_H=Theta(W sqrt(m))` by Theorem 3.1, rather than the required `o(W)`.
Hence it misses the weighted-overload condition by a factor `sqrt(m)`.

This is a black-box/method ceiling, not a statement that every random-greedy
middle matching has Poisson shadows.  Proving sub-Poisson shadow discrepancy
for a specially coupled greedy process would itself be the missing new
theorem.  Likewise, the exact MSW factor has `L=0` but no audited asymptotic
bound on its weighted overload.  At present no existing construction meets
both conditions.

## 6. Remaining target

The leftover part of the Gaussian-capacity gate is no longer the principal
quantitative obstruction.  The exact target is now to save the full
`sqrt(m)` Poisson factor in the shallow shadows:

```text
sum_{q<=sqrt(m) omega(1)} O_q/d_q=o(W).
```

Equivalently, a successful factor must correlate `Theta(sqrt(m))`
constant-mean depth rows so that their *total* balanced overload is little-o
of one typical row's ambient width.  Middle matching alone, without a
multidepth discrepancy mechanism, does not provide this.
