# Independent audit of `MIXED_PROFILE_CROSSLINE.md`

## 1. Verdict

**Verdict: PASS.**  I found no counterexample, reversed inequality, missing
quadratic term, or hypothesis mismatch in the finite cross-line charge, its
limiting form, the scalar relaxation, the mixed-profile saturation theorem,
or Theorem 8.1.  In particular:

* the finite error in the master inequality is genuinely only `O_b(a)`;
* a triple intersection must be credited once, exactly as in (3.3)--(3.5);
* the discrete three-set rearrangement bound used in (8.5) has the stated
  leading term and only `O(a)` rounding error;
* the optimization in (8.8) is correct on the whole domain
  `2 <= s <= 9/4`; and
* the final maximum is exactly `3271/1152 < 3`.

The proof is conditional in precisely the way stated in the source.  Theorem
8.1 needs all of the following along the same asymptotic sequence:

1. `D=o(a^2)`;
2. weak convergence of the normalized directed-plateau measures;
3. limiting support contained in `[4/3,3/2]`; and
4. `H_a(c)->0` for every sufficiently small fixed positive `c`.

It gives no conclusion for positive seam mass, for support leaking outside
that interval, or for an abstract measure which has not been lifted to the
three direction/level sets.  The source records all three limitations.

There are two minor exposition omissions, neither of which is a mathematical
gap:

* the passage `b upward to 4/3` in Section 8 tacitly uses compactness/diagonal
  subsequences (or, equivalently, takes a supremum over the compact feasible
  direction-count domain before taking the limit); and
* (8.5) invokes the discrete Riesz rearrangement inequality without spelling
  out its finite rounded version.

Both details are supplied below.

## 2. Fixed-threshold geometry

Fix `1<b<2`, and let a selected plateau have edge length `lambda>ba` on
coordinate level `t`.

### 2.1 Line capacity and allowed levels

The line has `2a-|t|+1` vertices and the plateau uses `lambda+1` of them, so

```text
lambda <= 2a-|t|,
|t| <= 2a-lambda < (2-b)a.
```

This proves (2.2).  There are at most `2(2-b)a+O(1)` integral levels in one
direction.

Two selected plateaux cannot occupy the same level in the same direction.
Their vertex sets would be disjoint subsets of that one line, but together
they would use more than `2ba+2 > 2a+1` vertices.  Hence (2.3) follows:

```text
n_i <= 2(2-b)a+O(1),
m <= 6(2-b)a+O(1)=O_b(a).
```

The count of cross-direction line pairs is exactly

```text
I_0=n_x n_y+n_y n_z+n_z n_x=(m^2-S_2)/2.
```

Two such lines intersect in the hexagon exactly when the absolute value of
the sum of their levels is at most `a`.  Thus `I=I_0-N` is exactly the number
of genuinely intersecting selected-line pairs.  A point incident with all
three selected directions contributes three pairs, so `0<=J<=I/3`.

No concentration, cyclic-order, or balance assumption enters these counts.

## 3. Finite omission charge and all endpoint errors

For a selected plateau `P`, the number of unused vertices on its selected
line is exactly

```text
r(P)=2a-|t(P)|-lambda(P).
```

Consequently

```text
R=sum_P r(P)=2am-E-T.                              (A3.1)
```

At a lattice point `p`, write `d_p` for the number of selected coordinate
lines through it and `u_p` for the number of their selected plateaux which
use it.  Summing `d_p-u_p` over points counts precisely the omissions in
(A3.1).

The plateau edge intervals are pairwise disjoint.  Within one coordinate
this follows from maximality of the constant blocks; between two coordinates
an edge constant in both would have all three coordinates constant and would
therefore have identical endpoints.  A word vertex has only two incident
word edges, so `u_p<=2`.  If `u_p=2`, both plateaux end at that vertex and
their edge intervals are consecutive.  Among `m` disjoint linear edge
intervals there are at most `m-1` such adjacencies (the source safely uses
`m`).

Away from those shared endpoints, `u_p<=1`.  The four possible values of
`d_p` give

| `d_p` | worst `u_p` | `d_p-u_p` | `binom(d_p,2)-1[d_p=3]` |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 |
| 2 | 1 | 1 | 1 |
| 3 | 1 | 2 | 2 |

At a shared endpoint the deficit from this inequality is at most one:
for `(d_p,u_p)=(2,2)` it is one, and for `(3,2)` it is also one.  Therefore

```text
R >= sum_p binom(d_p,2)-J-m = I-J-m.               (A3.2)
```

This verifies both the local triple correction and the complete endpoint
accounting.  Combining (A3.1) and (A3.2) gives the exact displayed form

```text
E <= 2am-T-(m^2-S_2)/2+N+J+m.
```

Since `m=O_b(a)`, the error in (1.2) is indeed `O_b(a)`, not `O(a^2)`.

Using `J<=I/3` gives (3.6) algebraically.  Finally, `n` distinct integer
levels have absolute-value sum at least `floor(n^2/4)`.  Thus
`T>=S_2/4-O(1)`, and substitution into (3.6) gives the coefficient
`S_2/12` in (3.7).  All signs in (3.5)--(3.7) are correct.

## 4. Limiting passage

At a continuity threshold `b`, the selected count and length normalize as

```text
m/a -> f(b),
E/a^2 -> ell(b).
```

Same-level uniqueness implies that each normalized level marginal is
dominated by Lebesgue measure.  The finite support inequality
`|t|/a <= 2-lambda/a` is closed under weak convergence, giving (4.4).

The other normalized terms converge as claimed:

```text
T/a^2 -> tau,
S_2/a^2 -> s_2,
N/a^2 -> eta.
```

For the last convergence, a pair of normalized levels is nonintersecting
exactly when `|u+v|>1`.  Since both marginals are dominated by Lebesgue
measure, their product assigns zero mass to the two boundary lines
`u+v=+1` and `u+v=-1`.  Hence the discontinuous indicator causes no loss.

The bound `0<=J/a^2<=I/(3a^2)=O(1)` permits a further subsequence on which
`J/a^2->theta`.  Division of (3.5) by `a^2` then gives exactly (4.8), while
`J<=I/3` gives (4.9) and hence (4.10).  The source correctly does **not**
claim that weak level marginals determine `theta`; microscopic additive
structure can remain in this limit.

## 5. Fringe and scalar envelopes

For `1<b<3/2`, put `q=2-b` and `w=3-2b`.  A positive nonintersecting pair
must have both levels in `(b-1,q]`.  Under the change of variables
`x=q-u`, `y=q-v`, the condition becomes `x+y<w` in `[0,w]^2`.
For two densities bounded by one with masses `r,s`, initial-interval
compression maximizes this area, giving

```text
Phi_w(r,s)=rs-(r+s-w)_+^2/2.
```

The same argument handles the negative fringe, proving (4.12).  For
`b>=3/2`, `q<=1/2`, so `|u+v|<=1` and `eta=0`.

For one fixed level `u`, one other direction contains at most

```text
d_b(u)=(|u|-(b-1))_+
```

nonintersecting level mass.  Summing over the two other directions and then
dividing by two because every unordered pair was seen at both endpoints
gives (5.3) with no missing factor of two.

The integrand in (5.4) is even and nondecreasing in `|u|`; the bathtub
principle therefore places the minimizing mass on the centered interval.
Direct integration gives

```text
h_b(alpha)=alpha^2/4                                   if alpha<=2(b-1),
h_b(alpha)=alpha^2/12+2(b-1)alpha/3-2(b-1)^2/3         otherwise.
```

This verifies (5.5)--(5.8).  The two pieces of `k_b` have the same value and
derivative at `K=2(b-1)` and nonnegative second derivative.  A convex
separable function on the capped simplex is maximized at a vertex, i.e. by
filling directions successively to the cap `C=2(2-b)`.  Equations
(5.9)--(5.11) follow.  The scalar envelope is only necessary, as the source
states.

## 6. Mixed-profile boundary saturation

The proof of Theorem 6.1 is valid.  A concise way to make its inherited seam
step completely explicit is to apply the finite general boundary--seam
inequality with fixed `c<beta'<beta` and `eta=beta'-c`.

Because the limiting measure has no mass below `beta`, the number of
dangerous successors in `(ca,beta'a]` is `o(a)`.  All remaining successors
satisfy

```text
lambda-ca >= (beta'-c)a,
L-lambda >= 2a+2.
```

Vanishing `H_a(c)` therefore makes all but `o(a^2)` complement positions
visible to a dangerous-free one-sided window; the `o(a)` exceptional
successors cost only `o(a^2)` because each gap contribution is truncated at
`O(a)`.  The dangerous edge mass is `(sigma+o(1))a^2`.  There are only
`O_c(a)` dangerous plateaux, so converting edge mass to vertex-union mass
costs only `O(a)`, including all shared endpoints.

Thus

```text
|R_c| >= (3-sigma-o(1))a^2.
```

The audited quadratic reservoir law gives
`3-sigma<=9c^2/4` for every sufficiently small fixed `c<2/3`.  Taking the
large-`a` limit first and then `c down to 0` gives `sigma>=3`; disjointness
of the plateau edge sets gives `sigma<=3`.  This proves `sigma=3`.

The support-away-from-zero and vanishing-seam assumptions are both used and
cannot be deleted from this proof.

## 7. Preliminary scalar exclusions

### 7.1 Endpoint atom

Let `h=mu({3/2})`.  Saturation gives `h<=2`.  Letting `b upward to 3/2` in
(5.11), for `1<=h<=2` the cap-filling masses are `(1,h-1,0)`, and the
necessary inequality is

```text
3h/2 <= 2h-h^2/3+[1+(h-1)^2]/12.
```

This is equivalent to `3h^2-4h-2<=0`, hence
`h<=(2+sqrt(10))/3`.  For `h<1` that conclusion is automatic.

### 7.2 Total plateau count

With support in `[4/3,3/2]` and edge mass three, the total count satisfies
`2<=s<=9/4`.  At a threshold approaching `4/3` from below, write
`r=s-4/3`, so `2/3<=r<=11/12`.  The cap-filling direction masses are
`(4/3,r,0)`.  Subtracting the required edge mass from the scalar upper
bound gives

```text
-17/27+8r/9-r^2/12.
```

This is negative below its smaller root
`r=(16-2sqrt(47))/3`, proving (7.10).  The arithmetic and inequality
direction are correct.

## 8. Discrete Riesz bound in Theorem 8.1

Let `A_x,A_y,A_z` be the three finite selected integer-level sets and sort
their normalized cardinalities as `alpha>=beta>=gamma`.  The discrete
three-function rearrangement inequality on `Z` gives

```text
#{(r,s,t) in A_x x A_y x A_z : r+s+t=0}
 <= the same count for centered integer intervals of those sizes.
```

For centered intervals, convolving the intervals of normalized lengths
`beta` and `gamma` produces a trapezoid.  Because `alpha>=beta>=gamma`,
integrating it over the centered interval of length `alpha` gives

```text
beta*gamma-(beta+gamma-alpha)_+^2/4.
```

Replacing the real interval endpoints by integer endpoints changes the
triple count by `O(a)`: only `O(1)` boundary diagonals, each containing
`O(a)` pairs, are affected.  Dividing by `a^2` proves

```text
theta <= beta*gamma-(beta+gamma-alpha)_+^2/4.
```

This is exactly (8.5).  It is an upper bound depending only on the three
cardinalities, so it remains valid despite length/level correlations and
despite the fact that weak marginals do not determine the actual additive
triple density.

## 9. Independent optimization of (8.7)

At `b upward to 4/3`, saturation supplies `ell=3`; the count is
`2<=s<=9/4`, each direction mass lies in `[0,4/3]`, and all levels lie in
`[-2/3,2/3]`.

The degree estimate gives

```text
tau-eta >= sum_i integral min(|u|,1/3) dnu_i.
```

The centered-interval minimum of the integral is

```text
h(alpha)=alpha^2/4              for 0<=alpha<=2/3,
h(alpha)=alpha/3-1/9            for 2/3<=alpha<=4/3.
```

Therefore (4.8) and the Riesz upper bound imply (8.7) with

```text
A(alpha)=alpha^2/2-h(alpha).
```

To verify (8.8), sort the masses as `a>=y>=z` and put `r=y+z=s-a`.

* If `a>=r`, then `Theta=yz`.  At fixed `a`, the function
  `A(y)+A(z)+yz` is symmetric and concave in `y` (its piecewise second
  derivative is at most zero), so it is maximized at `y=z=r/2`.  The
  expression is then `A(a)+3r^2/8`.  It is convex in `a` on
  `[s/2,4/3]`.  The value at `a=4/3` exceeds the value at `a=s/2` by

  ```text
  5(3s-8)^2/288>0.
  ```

* If `a<r`, then `Theta=yz-(r-a)^2/4`.  At fixed `r`,

  ```text
  max_{y+z=r} [A(y)+A(z)+yz]
   =3r^2/8                         for r<=4/3,
   =r^2/2-r/3+2/9                  for r>=4/3.
  ```

  Along `a+r=s`, the derivative with respect to `a` is respectively
  `r/4-1/3<=0` and zero.  Hence this branch is represented at `r=4/3`.
  Its deficit from the `a=4/3` value, with `q=s-4/3`, is

  ```text
  q^2/8-q/3+2/9=(3q-4)^2/72>0,
  ```

  because `q<=11/12<4/3`.

Thus the unique extremal shape up to permutation is

```text
(4/3,(s-4/3)/2,(s-4/3)/2),
```

and the maximum is

```text
5/9+3(s-4/3)^2/8.
```

This independently verifies (8.8).

## 10. Final constant and contradiction

Write `q=s-4/3`, so `2/3<=q<=11/12`.  Substitution in (8.7) gives the
upper bound

```text
7/3+2q/3-q^2/8.
```

Its derivative is `2/3-q/4>0` throughout the permitted interval, so its
maximum is at `q=11/12` and equals

```text
7/3+11/18-121/1152 = 3271/1152.
```

Since `3271/1152=2.8394...<3`, this contradicts the necessary lower side
of (8.7).  The numerical constant and the strict inequality are correct.

## 11. Counterexample search and scope audit

I separately checked every potential failure mode suggested by the proof:

* concentrating all directions on one coordinate only increases the convex
  count term but loses the necessary triple term and does not exceed (8.8);
* balancing all three directions is dominated by the cap-filled shape in
  Section 9;
* placing levels at the end fringes can raise `N`, but the exact master
  inequality charges the same move through `T`; no independent maximization
  of those terms is made in Theorem 8.1;
* triple points are neither omitted nor charged three times incorrectly:
  `I` sees three pairs, while (3.3) subtracts one and leaves the correct
  local omission requirement of two;
* shared word endpoints cost at most one each and only `O(a)` in total;
* atoms at either endpoint of `[4/3,3/2]` are included in Theorem 8.1; the
  threshold approaches `4/3` from below, so no atom-continuity assumption at
  `4/3` is needed; and
* the abstract two-direction lift in (8.15) passes only the deliberately
  weakened `2/3` charge.  It fails the exact charge because `J=0`, exactly as
  the source says.

I therefore find Theorem 8.1 and all lemmas on which it depends sound under
their stated hypotheses.
