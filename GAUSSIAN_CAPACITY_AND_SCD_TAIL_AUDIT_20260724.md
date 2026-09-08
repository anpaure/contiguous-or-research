# Audit: Gaussian-capacity transfer, Gaussian hole tax, and SCD tails

## Verdict

The three substantive claims audited here are valid:

1. the partial-wreath Gaussian-capacity transfer is an exact finite upper
   bound, including the corrected charge for both missing middle ranks;
2. the unavoidable rank-capacity hole tax has threshold
   `L=o(W/m^(1/3))`, with sharp leading term `(2/3) W sqrt(m) x^(3/2)`
   when `x=L/W -> 0` and `mx -> infinity`;
3. the symmetric-chain product word covers both Boolean tails, has the
   displayed exact length, and is `o(binomial(2m,m))` uniformly whenever
   its excluded half-width is `sqrt(m) omega(1)` and at most `m/2`.

The derived note `GAUSSIAN_WEIGHTED_WREATH_SWITCH_ENERGY_20260724.md` is
also correct in the points checked below.  Its displayed finite transfer
formula had one missing plus sign before the weighted energy term.  That
typographical error has been repaired in place.  No theorem or asymptotic
conclusion changes.

None of these results constructs the required balanced exact or partial
wreath packing.  The coefficient-one theorem remains conditional on the
weighted overload/energy gate.

## 1. Exact partial-packing capacity transfer

Let `T=ns`, `L=W-T`, and let `mu_q` be the depth-`q` load vector of a partial
middle wreath packing.  Write

```text
T=a_q N_q+r_q,  0<=r_q<N_q,
```

and let `b_q` be any balanced quota vector with `r_q` entries `a_q+1` and
all other entries `a_q`.  If

```text
U_q=sum_S (b_q(S)-mu_q(S))_+,
O_q=sum_S (mu_q(S)-b_q(S))_+,
```

then equality of the two total masses gives the exact identity

```text
U_q=O_q.
```

If `T>=N_q`, every missing target consumes at least `a_q=d_q` units of
underload, so `d_q M_q<=O_q`.  If `T<N_q`, precisely `N_q-T` quotas are
zero; after charging at most that many missing targets to the zero quotas,
each remaining missing target consumes one unit of underload.  Hence

```text
M_q <= (N_q-T)_+ + O_q/max(1,a_q).
```

This proof works for every balanced quota vector.  The minimizer in the
definition of `O_q` is obtained by assigning the `r_q` high quotas to the
`r_q` largest loads, by a one-step exchange argument.

At depth zero, disjointness of the selected middle intervals makes the load
vector binary.  Assigning the `T` high quotas to its support gives `O_0=0`,
while `(N_0-T)_+=W-T=L`.  Thus summing the lower-hole bounds and then using
complementation charges exactly `2L` for the missing `m`-sets and their
missing complementary `(m+1)`-sets.  This confirms the correction stated in
the submitted theorem.

For each selected cyclic order, the block of `n+2H+1` length-`m-H`
intervals exposes literally every cyclic interval of lengths
`m-H,...,m+H+1`.  Its length accounting is

```text
s(n+2H+1)=T+(2H+1)T/n.
```

The lower and upper holes are complementary in each rank pair.  The old
`2m`-coordinate tail word, followed by the new singleton and its anchored
copy, covers every odd-dimensional target outside the band.  Consequently
the finite inequality labelled `(GCT)` is valid.  A trimmed lift can improve
the stated tail charge by one entry, but the displayed bound is already
correct.

## 2. Gaussian hole tax and the `m^(-1/3)` threshold

Put `x=L/W` and `T=W(1-x)`.  The exact ratio

```text
N_q/W=product_{j=0}^{q-1}(m-j)/(m+2+j)
```

satisfies

```text
N_q/W <= exp(-q(q+1)/(m+q+1)).
```

If `N_q>T` and `0<=x<=1/2`, then

```text
q(q+1)/(m+q+1) < -log(1-x) <= 2x,
```

so `q^2<6mx`.  There are therefore at most `sqrt(6mx)` positive-depth
nonzero terms, each at most `L`, in addition to the depth-zero term `L`.
This proves

```text
sum_q (N_q-T)_+ <= L(1+sqrt(6mx)).
```

For sharpness, assume `x->0` and `mx->infinity`, and set `y=sqrt(mx)`.
Uniformly for `q=O(y)`, expansion of the exact product gives

```text
N_q/W = 1-q(q+1)/m+o(x).
```

For every fixed `epsilon>0`, all `q<=(1-epsilon)y` contribute according to
this expansion, while all `q>=(1+epsilon)y` contribute zero eventually.
The intervening boundary has total `O(epsilon Wxy)+o(Wxy)`.  Riemann
summation followed by `epsilon->0` yields

```text
sum_q (N_q-T)_+
  =(1+o(1)) W x y integral_0^1 (1-t^2)dt
  =(2/3+o(1)) W sqrt(m) x^(3/2).
```

The depth-zero term is lower order because `y->infinity`.  Combining this
with the easy `mx=O(1)` regime proves, under `x->0`,

```text
sum_q (N_q-T)_+=o(W) iff x=o(m^(-1/3)).
```

Thus the exponent `1/3` is intrinsic to literal repair of the unavoidable
rank deficiencies of a partial packing, rather than an artifact of the
overload proof.

## 3. Exact symmetric-chain product tail

In an SCD of an `m`-cube, the number of chains with minimum rank `a` is

```text
N_m(a)=binomial(m,a)-binomial(m,a-1),
```

and the increment word has length `w_m(0)=m` or
`w_m(a)=m-2a+1` for `a>0`.  For one chain in each of two disjoint halves,
the reverse increment word of the first followed by the forward increment
word of the second represents every union of one member from each chain.
Scheduling exactly the pairs whose minimum ranks satisfy `a+b<=r` covers
both `|S|<=r` and `|S|>=2m-r`: the latter follows from the symmetric upper
endpoints, not from an invalid complementation of OR witnesses.

Telescoping the number of second-half chains gives the exact constructed
length

```text
L_m(r)=2 sum_a N_m(a) w_m(a) C_m(r-a).
```

For `r=m-h`, split at `t=m-h-floor(m/2)`.  In the saturated part,
summation by parts gives

```text
sum_{a<=t} N_m(a)w_m(a)
 <= binomial(m,t)(2h+1+m/h),
```

and `t` is at least `h-1` ranks below the centre.  The central-binomial
ratio and `binomial(m,floor(m/2))^2/binomial(2m,m)=O(m^(-1/2))` give the
first term of the submitted uniform estimate.

In the unsaturated part, the exact identity

```text
N_m(a)w_m(a)
 =binomial(m,a)(m-2a+1)^2/(m-a+1)
```

reduces the sum to a hypergeometric second moment.  Its variance is
`r(2m-r)/(4(2m-1))`, giving the second submitted term after the elementary
binomial-ratio bound.  Both terms tend to zero uniformly when
`h/sqrt(m)->infinity` and `h<=m/2`.  The exact tail theorem and its splice
into the odd wreath word are therefore valid.

## 4. Audit of the Gaussian-weighted switch note

For an exact factor write `W=cN+r`, put `delta_S=mu(S)-c`, and let
`p=#{S:delta_S>=1}` and `B=sum_S(-delta_S)_+`.  Since `sum delta_S=r`, the
minimum balanced overload is

```text
O=B                         if p>=r,
O=r+B-p=sum_{delta>0}(delta-1)  if p<r.
```

On the other hand,

```text
Q=(1/2)sum_S delta_S(delta_S-1).
```

If `p>=r`, the negative coordinates alone contribute at least `B` to `Q`.
If `p<r`, the positive coordinates alone contribute at least
`sum(delta-1)=O`.  Hence the lossless inequality

```text
O_q<=Q_q
```

is correct.  Combining it with the capacity lemma gives
`M_q<=O_q/d_q<=Q_q/d_q`, and therefore the exact-factor finite transfer is
valid after inserting the missing plus sign in its display.

Finally, with

```text
u_q=W/N_q,
d_q=floor(u_q),
```

one has

```text
u_q >= exp(q(q+1)/(m+q+1)).
```

For `q>=ceil(2sqrt(m))`, this is at least two for all sufficiently large
`m`, so `d_q>=u_q/2`.  For `q<=m/2`, direct cross multiplication gives

```text
q(q+1)/(m+q+1) >= 2q^2/(3m).
```

Thus

```text
sum_{q<=H} q/d_q
 <= sum_{q<2sqrt(m)}q
    +2 sum_{q>=2sqrt(m)}q exp(-2q^2/(3m))
 =O(m)
```

uniformly for every `H<=m/2`.  The weighted quadratic toll of a balanced
alternating-eight switch is consequently `O(m)`, as claimed.  This estimate
does not supply the missing negative linear drift.

## Scope

The validated reductions replace pointwise capacity perfection by a
Gaussian-weighted overload/energy condition and reduce tail depth to
`sqrt(m) omega(1)`.  They do not prove that any exact wreath factor attains
weighted overload `o(W)`, nor that balanced switches descend to such a
factor.  The full asymptotic coefficient-one conjecture remains open.
