# Cross-layer width theory for every odd Boolean dimension

## 1. Outcome

Let

```text
k=2r+1,
M=C(k,r)=C(k,r+1),
n=M+d.
```

Assume `d>=1` and suppose a universal nonzero OR array of length `n` exists.
(`d=0` is already incompatible with the lower layer in every nontrivial
case.)  Independently
select one witness for every rank-`r` mask and every rank-`r+1` mask, and sort
each family by left endpoint.  Write

```text
y_j = number of selected rank-r witnesses of width j,
x_j = number of selected rank-(r+1) witnesses of width j,
```

where width is physical length minus one.

This note proves the following exact all-odd constraints.

1. Upper widths lie in `0,...,d`, while every lower width lies in
   `0,...,d-1`.
2. With

   ```text
   X_t=x0+...+xt,
   Y_t=y0+...+yt,
   Y_(-1)=0,
   ```

   one has

   ```text
   X_t <= d+Y_(t-1)                 (0<=t<=d).
   ```

3. If `W_x=sum j*x_j` and `W_y=sum j*y_j`, then

   ```text
   W_x-W_y >= M-d*(d-1)-x0.
   ```

4. Let `O_L,O_R` be the `d` endpoints omitted by the selected lower row.  Then

   ```text
   W_y=sum(O_L)-sum(O_R).
   ```

   Every selected upper singleton position belongs to `O_L intersection O_R`.
5. For every lower target family `F` of containment-chain height at most `h`,

   ```text
   |F| <= sum_j min(j,h)*y_j + h*(d-x0).
   ```

6. Put

   ```text
   L=sum_(s=1)^(r-1) C(k,s).
   ```

   When `M>=d`, define

   ```text
   q_* = min{q in {0,...,d}:
             L <= q*(M+d+r-1-q)}.
   ```

   Use `q_*=+infinity` if this set is empty.  Under the standing hypothesis
   that a candidate array exists, the actual value `q=d-x0` belongs to the
   set, so the empty case cannot occur.

   Every candidate satisfies

   ```text
   x0 <= d-q_*.
   ```

   A slightly weaker closed form is

   ```text
   x0 <= d-ceil(L/(M+d+r-1)).
   ```

The last statement is a genuine new all-odd obstruction, not merely a change
of notation.  For every conjectural rank-count length `B(k)` with odd
`7<=k<20`, it gives

```text
x0<=1.
```

Thus an equality candidate in any of those dimensions may use at most one
distinct upper-middle-layer mask as a literal array entry.  Indeed, if two
distinct rank-`r+1` masks appeared as entries, choose those singleton
occurrences as their two selected witnesses and choose the remaining upper
witnesses arbitrarily, contradicting `x0<=1`.

## 2. Equal-rank witness bands

Choose one interval for every target in one fixed rank of size `M`.  Two
selected intervals cannot contain one another: physical containment implies
containment of their OR masks, while two distinct masks of the same rank are
incomparable.  Therefore, after sorting by left endpoint,

```text
l_1<...<l_M,
u_1<...<u_M.
```

Both endpoint sequences are increasing `M`-subsets of an `M+d`-position
universe.  In zero-based notation their `i`th entries satisfy

```text
i<=l_i<=u_i<=i+d.
```

Hence every selected interval has width at most `d`.

Apply this to the upper rank `r+1`.  Any physical interval of length at least
`d+1` contains a selected upper witness.  Indeed, an interval beginning at
`a` has `a<=M-1` and contains

```text
[a,a+d],
```

which contains the selected upper interval indexed by `a`.

An exact rank-`r` interval cannot contain a rank-`r+1` witness.  Consequently
every selected lower interval has physical length at most `d`, or width at
most `d-1`.  Thus

```text
sum_(j=0)^d x_j=M,
sum_(j=0)^(d-1) y_j=M.
```

This is entirely unrestricted; no derivative row or adjacency assumption is
present.

## 3. Cumulative cross-layer nesting

Fix `t` with `0<=t<=d`.  There are `X_t` selected upper intervals of width at
most `t`, and their left endpoints are distinct.  The selected lower left
endpoint set has size `M` in `M+d` positions and therefore omits exactly `d`
positions.  At least

```text
X_t-d
```

of the upper endpoints are shared with selected lower witnesses.

At a shared left endpoint, the lower interval is a proper prefix of the upper
interval.  If it ended at or after the upper interval, it would contain the
rank-`r+1` witness while having a rank-`r` OR; equality is impossible for the
same reason.  An upper interval of width at most `t` is therefore paired with
a lower interval of width at most `t-1`.

The pairing is injective because lower left endpoints are distinct.  Hence

```text
X_t-d <= Y_(t-1),
```

which is the claimed cumulative inequality.  Right endpoints give the same
profile inequality independently.

### Summed width separation

Sum only the cases `t=1,...,d-1`.  The left side is

```text
sum_(t=1)^(d-1) X_t = d*M-W_x-x0,
```

and the lower cumulative sum is

```text
sum_(t=1)^(d-1) Y_(t-1) = (d-1)*M-W_y.
```

Therefore

```text
d*M-W_x-x0 <= d*(d-1)+(d-1)*M-W_y,
```

or

```text
W_x-W_y >= M-d*(d-1)-x0.             (3.1)
```

Using only `x0<=d` recovers the weaker direct endpoint bound `M-d^2`.
Any independent improvement `x0<=b` immediately strengthens (3.1) to

```text
W_x-W_y >= M-d*(d-1)-b.
```

## 4. Omitted endpoints and upper singleton witnesses

Let `O_L` and `O_R` be the positions omitted respectively by the selected
lower left and right endpoint sets.  Both have cardinality `d`.  If `T` is
the sum of all physical position indices, then

```text
sum selected left endpoints  = T-sum(O_L),
sum selected right endpoints = T-sum(O_R).
```

Subtracting gives the exact identity

```text
W_y=sum(O_L)-sum(O_R).                 (4.1)
```

Now suppose `[p,p]` is a selected upper witness.  The array entry at `p` has
rank `r+1`.  No selected lower interval can begin at `p` or end at `p`, since
it would contain that entry and its OR would have rank at least `r+1`.
Therefore

```text
p in O_L intersection O_R.
```

Different selected upper singleton targets occupy different physical
positions, so, with `c=|O_L intersection O_R|`,

```text
c>=x0.                                      (4.2)
```

Delete the common points from `O_L,O_R` and put `q=d-c`.  The remaining sets
are disjoint `q`-subsets.  Their largest possible sum difference is obtained
by putting the `q` largest physical positions on the left and the `q` smallest
on the right:

```text
W_y <= q*(n-q)=(d-c)*(M+c).                (4.3)
```

This bound is exact for fixed `c`.  In the near-width regime `M>=d`, its right
side decreases with `c`, so (4.2) gives

```text
W_y <= (d-x0)*(M+x0).                      (4.4)
```

## 5. Fan-capped lower-width mass, sharpened by upper singletons

Use the selected lower rank-`r` row as the forbidden central antichain.  Any
witness for a target of rank at most `r-1` avoids containing a complete
selected lower interval.

The fan-capped avoidance theorem normally gives, for a chosen target family
`F` of containment-chain height at most `h`,

```text
|F| <= sum_j min(j,h)*y_j+h*d.
```

Every selected upper singleton position is one of the free lower right
endpoints, but no target of rank at most `r-1` can have a witness ending
there: such an interval contains the rank-`r+1` array entry.  Those `x0`
endpoint fans contribute zero rather than the generic cap `h`.  Hence the
exact sharpening is

```text
|F| <= sum_j min(j,h)*y_j+h*(d-x0).        (5.1)
```

The left-endpoint version gives the same scalar inequality.

### Adjacent lower antichain

Take every rank-`r-1` mask.  Its size is

```text
A=C(k,r-1)=M*r/(r+2).
```

With `h=1`, (5.1) becomes

```text
A <= (M-y0)+(d-x0),
```

so

```text
y0+x0 <= M+d-A = 2*M/(r+2)+d.             (5.2)
```

This is an all-odd `O(M/r)` bound on selected lower singleton witnesses.

### Complete lower ideal

Let

```text
L=sum_(s=1)^(r-1) C(k,s)=2^(2r)-1-M.
```

The nonempty ideal through rank `r-1` has chain height `r-1`.  Equation (5.1)
gives

```text
sum_j min(j,r-1)*y_j
    >= L-(r-1)*(d-x0).                     (5.3)
```

Since `W_y=sum j*y_j` dominates the capped sum, one always has

```text
W_y >= L-(r-1)*(d-x0).                     (5.4)
```

When `d<=r`, as in every `k<20` evaluation below, all lower widths are already
at most `r-1`, and (5.3) is exactly the total-width inequality (5.4).

More generally, (5.1) supplies a full hierarchy of valid cuts by taking any
lower Boolean slab and its exact chain height; (5.2)--(5.4) are merely the two
closed forms needed here.

## 6. A general upper-singleton theorem

Put

```text
q=d-x0.
```

Combine the fan lower bound (5.4) with the omitted-endpoint upper bound (4.4):

```text
L-(r-1)*q <= W_y <= q*(M+d-q).
```

Therefore every candidate in the regime `M>=d` satisfies

```text
L <= q*(M+d+r-1-q).                         (6.1)
```

Define

```text
q_* = min{q in {0,...,d}:
          L <= q*(M+d+r-1-q)}.
```

The actual `q=d-x0` is feasible in this one-dimensional inequality, hence

```text
x0<=d-q_*.                                    (6.2)
```

No profile search or SAT assumption is hidden in `q_*`; it is a closed
integer calculation from `k` and `d`.

Dropping the negative quadratic term on the right of (6.1) gives the simpler
but sometimes weaker consequence

```text
q >= ceil(L/(M+d+r-1)),

x0 <= d-ceil(L/(M+d+r-1)).                    (6.3)
```

For every `r>=2`, `L>0`, so (6.3) already improves the trivial endpoint count
to the genuine all-odd statement

```text
x0<=d-1.                                      (6.4)
```

When `d>=2` and `M+r>=d`, the quadratic in (6.1) increases throughout
`0<=q<=d`.
Therefore the exact sufficient-and-necessary arithmetic condition for (6.1)
to force `x0<=1` is

```text
L > (d-2)*(M+r+1).                            (6.5)
```

Indeed, the right side is (6.1) evaluated at `q=d-2`.  If (6.5) holds, every
feasible `q` is at least `d-1`; if it fails, `q=d-2` passes this particular
combined obstruction.  This does not claim that a corresponding array exists.

## 7. Exact evaluation at the conjectural rank-count lengths below 20

Recall

```text
tau(k,s)=min{t>=0:
    sum_(j=1)^(s-1) C(k,j)
       <= t*C(k,s)+C(t+1,2)},

B(k)=max_s (C(k,s)+tau(k,s)).
```

For each requested odd dimension, set `d=B(k)-M`.  Rank `r+1` is a maximizing
rank in every row; for `k=9`, rank `r` ties it.  The resulting exact table is:

| `k` | `r` | `M` | `B(k)` | `d` | `L` | `q_*` | bound on `x0` |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 7  | 3 | 35    | 37    | 2 | 28     | 1 | `x0<=1` |
| 9  | 4 | 126   | 128   | 2 | 129    | 1 | `x0<=1` |
| 11 | 5 | 462   | 465   | 3 | 561    | 2 | `x0<=1` |
| 13 | 6 | 1,716 | 1,719 | 3 | 2,379  | 2 | `x0<=1` |
| 15 | 7 | 6,435 | 6,438 | 3 | 9,948  | 2 | `x0<=1` |
| 17 | 8 | 24,310 | 24,313 | 3 | 41,225 | 2 | `x0<=1` |
| 19 | 9 | 92,378 | 92,381 | 3 | 169,765 | 2 | `x0<=1` |

The remaining profile consequences are:

| `k` | `y0+x0` upper bound | lower bound on `W_y` | worst-case lower bound on `W_x-W_y` |
|---:|---:|---:|---:|
| 7  | 16    | `24+2*x0`      | 32 |
| 9  | 44    | `123+3*x0`     | 123 |
| 11 | 135   | `549+4*x0`     | 455 |
| 13 | 432   | `2,364+5*x0`   | 1,709 |
| 15 | 1,433 | `9,930+6*x0`   | 6,428 |
| 17 | 4,865 | `41,204+7*x0`  | 24,303 |
| 19 | 16,799 | `169,741+8*x0` | 92,371 |

The last column substitutes the proved worst case `x0=1` into (3.1).  For
`k=7` and `k=9` the length `B(k)` is already known attainable; for the larger
rows these are necessary conditions on a hypothetical equality construction,
not existence claims.

The table is independently reproduced by

```text
scratch/verify_odd_cross_layer_widths.cpp
SHA-256 5c4f7a2117b91dae15bc87e4c957e056b91f55687fbcef8a61e6f247994a1478
```

which recomputes `B(k)` from the rank-slack definition rather than embedding
the displayed `d` values.

## 8. What is genuinely general, and what remains open

The conclusions (3.1), (5.1), and (6.2) hold in every odd dimension and for
every hypothetical excess `d` with `M>=d`.  They are useful even when the
rank-count conjecture fails: one simply inserts the actual proposed length's
`d=n-M`.

In particular:

* upper singleton witnesses consume common omissions in both lower endpoint
  sets, rather than merely using generic band slack;
* each such singleton deletes an entire height-`h` free fan from every lower
  slab;
* the resulting exact scalar obstruction is the one-dimensional inequality
  (6.1); and
* all odd equality searches with `7<=k<20` may impose `x0<=1` globally WLOG.

Equivalently, in each of those searches all array entries of rank `r+1` must
have the same mask (if any occur at all).  This is a direct restriction on the
array variables, not only on an auxiliary witness schedule.

What is not proved is that `q_*=d-1`, or `x0<=1`, for every odd `k` at
`B(k)`.  Equation (6.5) isolates that question as a concrete binomial
arithmetic inequality.  Nor do these profile cuts prove existence or
impossibility at any unresolved dimension.  Their role is to constrain every
unrestricted monotone-band/central-forest search and to expose a new exact
cross-layer invariant.
