# Absorbed direction flow and a global coarea constraint

## 1. Scope and outcome

This note adds one coupling which is absent from the current combined
three-box marked-process relaxation.  It uses the notation and the proved
finite plateau geometry of `MULTISCALE_DIRECTION_COUPLING_NEXT.md` and
`MIXED_PROFILE_CROSSLINE.md`.

At a dangerous threshold, an absorbed predecessor--successor seam is not an
unlabelled unit of capacity.  Its two plateau directions are necessarily
different.  Consequently the absorbed seams form an off-diagonal flow on the
same three direction classes which enter the cross-line inequality.  Moreover,
every absorbed successor lies on a strictly positive coordinate level.  This
makes intersections between absorbed successor lines especially costly: three
absorbed lines cannot pass through one point, so the additive-triple correction
cannot erase their pair-intersection charge.

The results below are necessary conditions for every actual three-box middle
order.  They do not yet prove a subquadratic construction or a quadratic
obstruction.

## 2. Finite off-diagonal flow

Fix `c>1` and retain the directed internal plateaux whose edge lengths exceed
`ca`.  Write them in their physical word order.  A plateau `P` has:

* fixed-coordinate direction `d(P)` in `{x,y,z}`;
* fixed integer level `t(P)`;
* edge length `lambda(P)`; and
* a rising cross-coordinate `r(P)`, with `r(P) != d(P)`.

For two consecutive retained plateaux `P,Q`, let `M(P,Q)` be the maximum of
the rising coordinate `r(P)` over the physical word segment from the end of
`P` through the start of `Q`.  Call the seam **actually absorbed** exactly
when

```text
d(Q)=r(P),
t(Q)=M(P,Q).
```

The audited seam geometry then supplies the necessary bounds

```text
lambda(P)-a <= t(Q) <= 2a-lambda(Q).                         (2.0)
```

The interval test alone is not sufficient: the rising coordinate may attain
a larger value inside the gap.

Let `n_d(c)` be the number of retained plateaux of direction `d`, and let
`A_de(c)` count absorbed seams whose predecessor has direction `d` and whose
successor has direction `e`.

### Theorem 2.1 (absorbed-flow constraints)

For every fixed threshold,

```text
A_dd(c)=0,
sum_e A_de(c) <= n_d(c),
sum_d A_de(c) <= n_e(c).
```

If `m(c)=n_x(c)+n_y(c)+n_z(c)` and `A(c)=sum_(d,e) A_de(c)`, then for a linear
tail

```text
A(c) <= min(m(c)-1, 2(m(c)-max_d n_d(c))).                 (2.1)
```

For a cyclic tail, replace `m(c)-1` by `m(c)`.

#### Proof

Absorption gives `e=r(P) != d(P)`, proving the zero diagonal.  A retained
plateau has at most one outgoing tail seam and at most one incoming tail seam,
which proves the row and column bounds.

Every absorbed seam is a bichromatic edge of the direction-coloured tail
path.  Fix a largest colour class.  Every bichromatic edge has at least one
endpoint outside that class, while every such vertex is incident with at most
two path edges.  Hence there are at most twice as many bichromatic edges as
non-majority vertices.  A linear path has only `m-1` edges in total.  This
proves (2.1).  The cyclic statement is identical.  QED.

After division by `a`, every limiting process therefore satisfies, at every
threshold which is a continuity point for both the tail-length and
absorbed-edge lifetime measures,

```text
A(c) <= min(f(c), 2(f(c)-max_d alpha_d(c)))                 (2.2)
```

with the harmless one-edge linear correction absorbed by `o(1)`.

## 3. The flows at different thresholds have common lifetimes

For physical plateau indices `i<j`, let

```text
H(i,j)=max{lambda(q): i<q<j},
```

with an empty maximum equal to zero.  The threshold-contraction theorem says
that `i` is the retained predecessor of `j` exactly for

```text
H(i,j) <= ca < min(lambda(i),lambda(j)).                    (3.1)
```

The direction condition and the seam-local maximum `M(i,j)` defining actual
absorption depend only on the two physical plateaux and their intervening
word segment, not on `c`.  Thus every actually absorbed off-diagonal edge
contributes on one interval of thresholds and nowhere else.

### Corollary 3.1 (common edge-lifetime representation)

For any nonnegative integrable weight `w` and

```text
W(s)=integral_(1 to s) w(c) dc,
```

define the normalized finite flow by `A_de,a(c)=A_de(c)/a`.  Then

```text
integral w(c) A_de,a(c) dc
 = (1/a) sum over actually absorbed physical d->e edges (i,j)
     [W(min(s_i,s_j))-W(max(1,h_ij))]_+,                    (3.2)
```

Here `s_i=lambda(i)/a` and `h_ij=H(i,j)/a`.  Threshold endpoints have
Lebesgue measure zero.  Equation (3.2) is exact for a linear tail; comparison
with a cyclic convention changes the normalized flow by at most `1/a`.

Hence the matrices `A_de(c)` cannot be optimized independently at different
thresholds.

## 4. Absorbed positive lines cannot hide in the triple correction

At the fixed threshold, let `B` be the family of successor plateaux of
absorbed seams.  The lower absorption inequality and `lambda(P)>ca` give

```text
t(Q) >= lambda(P)-a > (c-1)a > 0                         (4.1)
```

for every `Q in B`.

Let `T_B=sum_(Q in B) t(Q)`.  Let `I_B` count intersecting pairs of selected
coordinate lines belonging to two members of `B` in different directions.
Recall the finite notation from the cross-line theorem: `E` is selected
plateau edge mass, `m` is selected plateau count, `T` is the sum of absolute
levels, `I` counts all intersecting cross-direction selected-line pairs, and
`J` counts selected triple-line intersection points.  The audited master
inequality is

```text
E <= 2am - T - I + J + m.                                  (4.2)
```

### Theorem 4.1 (absorbed-line penalty)

At every fixed threshold,

```text
I-J >= I_B                                                   (4.3)
```

and consequently

```text
E <= 2am - T_B - I_B + m.                                   (4.4)
```

#### Proof

Charge (4.3) point by point.  A point incident with exactly two selected
coordinate lines contributes one to `I-J`.  A point incident with all three
directions contributes `3-1=2`.

At most two lines from `B` can pass through one point: their three coordinate
levels would otherwise all be strictly positive, contradicting
`x+y+z=0`.  Thus a two-line point contains at most one `B`-pair and a
three-line point also contains at most one `B`-pair.  Its contribution to
`I-J` is therefore at least its number of `B`-pairs.  Summing proves (4.3).
Since `T>=T_B`, (4.2) gives (4.4).  QED.

Define the finite empirical measure

```text
nu^A_(d,a)=(1/a) sum_(Q in B, d(Q)=d) delta_(t(Q)/a).
```

After passing to a subsequence, let `nu_d^A` be its positive-level limit, let
`tau_A=sum_d integral t dnu_d^A(t)`, and put

```text
iota_A = sum_(d<e) double_integral 1_{t+u<=1}
                                  dnu_d^A(t)dnu_e^A(u).
```

Same-line uniqueness gives

```text
nu_d^A <= Lebesgue measure on [c-1,2-c],
```

and (4.4) gives the new limiting necessary inequality

```text
ell(c) <= 2f(c)-tau_A(c)-iota_A(c).                         (4.5)
```

The measures `nu_d^A` are not free: their masses are the column sums of the
off-diagonal flow in Section 2, and their `(predecessor length, successor
length, level)` support satisfies

```text
p-1 <= t <= 2-s,                                             (4.6)
```

where `p,s,t` are normalized variables.

Equations (2.2), (4.5), and (4.6) are the promised direct bridge from seam
absorption to cross-line geometry.

## 5. Weighted cross-line coarea identity

The fixed-threshold cross-line inequality can itself be retained globally.
At finite scale define

```text
kappa_(d,a)=(1/a) sum_(P directed internal, d(P)=d, lambda(P)>a)
                   delta_((lambda(P)/a,t(P)/a)),
Xi_a=(1/a^2) sum_(actual three-line intersections among this broad family)
                   delta_(three marked lines).
```

Pass to subsequential limits `kappa_d` and `Xi`, and put
`kappa=kappa_x+kappa_y+kappa_z`.  Thus `Xi` is the actual
additive-triple measure on triples of physical lines in the three directions
whose levels sum to zero.  It is essential that `Xi` is the genuine common
triple measure, not a product of independently optimized marginals.  The
length marginal may have support on `[1,2]`; possible mass at `1` is harmless
because `W(1)=0`.

### Theorem 5.1 (global coarea inequality)

For every nonnegative continuous weight `w` with compact support in `(1,2)`
and `W(s)=integral_1^s w(c)dc`, every line-realizable limiting process obeys

```text
 integral W(s)(s-2+|t|) dkappa

 + sum_(d<e) double_integral_{|t+u|<=1}
       W(min(s,s')) dkappa_d(s,t) dkappa_e(s',u)

 - integral W(min(s_x,s_y,s_z)) dXi
 <= 0.                                                        (5.1)
```

#### Proof

At a continuity threshold `c`, rewrite the strongest cross-line inequality
as

```text
ell(c)-2f(c)+tau(c)+I(c)-theta(c) <= 0.
```

Multiply by `w(c)` and integrate.  A plateau of normalized length `s` is
present exactly for `1<c<s`, giving the first term of (5.1).  An intersecting
pair is simultaneously present exactly until `c=min(s,s')`, giving the
second term.  An actual triple point is present until the minimum of its three
lengths, giving the last term.  Tonelli applies to the nonnegative individual
pieces; subtracting the finite terms after integration gives (5.1).  At finite
scale the master inequality has the additional `+m(c)` error.  After division
by `a^2`, its weighted integral is `o(1)` because `m(c)=O(a)` uniformly away
from threshold one.  The pair boundary has zero limiting product mass by
Lebesgue domination, and `W(min(.))` is continuous for the triple measure.
Thus (5.1) follows first in the finite problem and then by subsequential weak
limits, without exchanging a limit with an unsigned difference.  QED.

## 6. Exact remaining analytic target

The combined process must now satisfy simultaneously:

1. threshold contraction and additive gap coalescence;
2. the off-diagonal flow constraints (2.1)--(2.2);
3. the common absorbed-edge lifetimes (3.1)--(3.2);
4. the absorbed positive-line penalty (4.5)--(4.6);
5. the global line/triple coarea inequality (5.1); and
6. the actual nonabsorbed seam-saving functional.

This closes a genuine loophole in the previous relaxation.  High absorption
can no longer be purchased using an aggregate `3 dt` capacity: it forces a
nearly balanced off-diagonal direction flow and a family of positive lines,
which pays `tau_A+iota_A`.  Low absorption leaves more physical predecessor
edges in the nonabsorbed seam-saving term.  What remains is to prove that one
of these two payments is uniformly large enough, after one common weighting
over edge lifetimes, to force `U(c)<4` at some threshold; or to construct a
single marked process satisfying all six conditions.
