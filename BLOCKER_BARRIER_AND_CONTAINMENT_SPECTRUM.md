# Complete endpoint-blocker barrier and containment spectrum

## 1. Fractional endpoint cap

Choose one witness interval `I_S` for every nonempty Boolean mask.  Let
`x_S>=0` satisfy

\[
 \sum_{S\in C}x_S\le1
\]

for every inclusion chain in the punctured Boolean lattice, and put
`Theta=sum_S x_S`.

### Theorem 1

If a physical interval `J` has OR `T`, then

\[
 |J|\le n-\Theta+\sum_{S\subseteq T}x_S
      =n-\sum_{S\not\subseteq T}x_S.                 \tag{1.1}
\]

At one left endpoint, selected witness labels form a chain, so the total
weight beginning before `J` is at most the number of positions before it.
The analogous right-endpoint statement bounds witnesses ending after `J`.
Every witness not contained in `J` is counted by at least one of these two
classes.  A witness contained in `J` has label contained in `T`, which proves
(1.1).

## 2. Optimal blocker for one target

For fixed `T`, let

\[
 P_T=\{S\ne\varnothing:S\not\subseteq T\},\qquad
 \omega(T)=\operatorname{width}(P_T).
\]

Unit weight on a maximum antichain gives

\[
 |J|\le n-\omega(T).                                 \tag{2.1}
\]

Dilworth partitions `P_T` into `omega(T)` chains, so no chain-feasible
fractional weighting has larger excluded weight.  Thus (2.1) is the exact
best cap obtainable from one endpoint-chain blocker.

If `|T|=s`, then

\[
 P_T\cong B_s\times(B_{k-s}\setminus\{\varnothing\}).
\]

Product normality makes this poset Sperner, with rank numbers
`C(k,j)-C(s,j)`.  For

\[
 r=\lceil k/2\rceil,\qquad W=\binom kr,
\]

unimodality together with the central adjacent-rank comparison gives

\[
 \boxed{\omega(k,s)=W-\binom sr}\quad(s<k),            \tag{2.2}
\]

and `omega(k,k)=0`.  Hence the optimal target cap at length `n` is

\[
 \lambda_n(k,s)=
 \begin{cases}
 n-W+\binom sr,&s<k,\\
 n,&s=k.
 \end{cases}                                          \tag{2.3}
\]

## 3. Complete nested Hall hierarchy

Distinct targets need distinct physical intervals.  Therefore every `t`
must satisfy

\[
 \sum_{\substack{1\le s\le k\\\lambda_n(k,s)\le t}}
   \binom ks
 \le tn-\binom t2.                                    \tag{3.1}
\]

Let `H(k)` be the least `n` satisfying every row (3.1).

### Theorem 2 (collapse)

\[
 \boxed{H(k)=B(k)}.                                    \tag{3.2}
\]

Moreover, the upper central rank always maximizes the rank-count bound.  If

\[
 L=\sum_{j=1}^{r-1}\binom kj,
\]

and `d` is least with

\[
 L\le dW+\binom{d+1}{2},                              \tag{3.3}
\]

then

\[
 B(k)=W+d.                                             \tag{3.4}
\]

At `n=W+d`, targets below rank `r` have cap `d`; (3.1) at `t=d` is exactly
(3.3).  At the breakpoint for rank `s>=r`, write
`u=C(s,r)` and `h=s-r+1`.  The extra interval capacity is

\[
 uW-\binom u2.
\]

For `s=r` this is exactly `W`.  For `s>r`, `u>=2h` and `u<=W` give at least
`hW`, enough for all ranks `r,...,s`; the small cases and full-set endpoint
are direct.

Conversely, for every rank `q` and target below rank `q`, the complete
rank-`q` layer is an antichain in `P_T`.  Thus the Hall row at
`t=n-C(k,q)` contains the rank-`q` rank-count inequality.  Hence `H>=B`,
completing (3.2).

## 4. Consequences

If `A` is any antichain of size `q` and `T` avoids every member of `A`, then
`A subseteq P_T`, so `omega(T)>=q` and `lambda_n(T)<=n-q`.  The optimal Hall
row therefore implies

\[
 |\operatorname{Av}(A)|\le I(n,n-q)
\]

for every dimension.  No non-level antichain improves the central layer.

More generally, every bounded-height family and every chain-feasible
fractional blocker is pointwise dominated by (2.3): Dilworth gives

\[
 \sum_{S\not\subseteq T}x_S\le\omega(T).
\]

Thus all scalar arguments of the form

```text
endpoint-chain capacity
 -> targetwise maximum witness length
 -> nested interval Hall inequalities
```

stop exactly at `B(k)`.

This does not constrain competition for named nonnested cells, simultaneous
left/right endpoint orders, precedence cycles, or coordinate pin survival.
Those are the first remaining sources of information.  See
`BLOCKER_BARRIER_AND_CONTAINMENT_SPECTRUM_AUDIT.md` and
`scratch/check_blocker_barrier.py`.
