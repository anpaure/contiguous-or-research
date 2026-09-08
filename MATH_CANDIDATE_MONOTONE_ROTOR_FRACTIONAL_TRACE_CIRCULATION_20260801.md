# Monotone rotor clockability of the fractional trace gate

> **Promoted after independent audit.**  The authoritative corrected theorem
> is `MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`.
> This candidate is retained only as the original submission; its statement
> omits the corrected range, ambient-`k` notation, and complete Ferrers
> conventions.

Date: 2026-08-01  
Status: independently audited after the scope and normalization corrections
recorded below.  The argument closes the unrooted invariant **fractional**
marked-trace gate.  It does not claim an
integral one-owner chronology, named-target exact cover, connected/rooted
Euler support, upper-shadow coverage, or common-cap feasibility.

## 1. Statement

Fix `r>=2` and `1<=d<=r-1`.  Let

```text
M_(r,d)={q in R^(r-1): 0<=q_1<=...<=q_(r-1)<=1,
                         sum_s q_s<=d}.
```

Let `C_(r,d)` be the age-composition set in Section 2.  Define `ST_(r,d)`
to consist of the vectors `q` for which there are a probability law `pi`
on `C_(r,d)`, a normalized stationary type flow `f`, and mark variables
such that

```text
sum_c pi(c)=1,
sum_c' f(c,c')=sum_c' f(c',c)=pi(c),
q_s <= sum_(c:s in R(c)) pi(c)                 (1<=s<r),
```

where `R(c)` is the set in (2.2) below.  This is normalized per owner; the
established biregular lift then gives a same-owner invariant literal
fractional circulation.

### Theorem 1 (monotone rotor theorem)

```text
M_(r,d) subseteq ST_(r,d).
```

Consequently, put

```text
r=ceil(k/2), W=C(k,r), Lambda=sum_(s=1)^(r-1) C(k,s),
d=min{q:qW+C(q+1,2)>=Lambda}, h=(Lambda-dW)_+.
```

Choose an actual `h`-cell left-justified Ferrers subset of the triangular
boundary board, let `b_s` be its column counts, and extend `b_s=0` for
`s>d`.  Then the optimal triangular residual vector

```text
q_s=(C(k,s)-b_s)/C(k,r)
```

belongs to `ST_(r,d)`.  Here `sum_s b_s=h`,
`0<=b_s<=C(k,s)`, and `b_1>=...>=b_d>=0`; nonincreasing numbers without
these inherited triangular quantifiers do not suffice.

## 2. Age transitions and the labelled lift

For an age composition

```text
c=(c_0,...,c_d), c_0>0, c_i>=0, sum_i c_i=r,
```

the available distinct proper suffix ranks form the set

```text
R(c)={c_0+...+c_(j-1):1<=j<=d,
                         c_0+...+c_(j-1)<r}.          (2.2)
```

There is a literal same-owner transition `c->c'` exactly when

```text
c'_(i+1)<=c_i, 0<=i<d.                               (2.1)
```

Repeated partial sums caused by zero age classes are counted once.  For a
fixed type edge, the compatibility graph between labelled age
partitions is biregular.  Distributing a type-edge flow uniformly over its
labelled compatibility edges gives uniform outgoing mass on the source
partitions and uniform incoming mass on the target partitions.  Thus every
type circulation lifts to a literal-state circulation.  Averaging over
owners and coordinate permutations makes every suffix target of a fixed
rank uniform.

## 3. Vertices of the monotone demand polytope

For `1<=ell<=r-1`, let `v_ell` be one on ranks
`r-ell,...,r-1` and zero below.  Every monotone `q` has the unique form

```text
q=sum_ell alpha_ell v_ell,
alpha_ell>=0,
sum_ell alpha_ell<=1,
sum_ell ell alpha_ell<=d.                              (3.1)
```

The vertices are

```text
0;
v_a                                      (1<=a<=d);
(d/b)v_b                                 (d<b<=r-1);
((b-d)/(b-a))v_a+((d-a)/(b-a))v_b        (1<=a<d<b<=r-1).
```

Indeed a vertex of (3.1) has at most two positive coordinates.  A
two-coordinate vertex makes both scalar inequalities tight, so its indices
straddle `d` and the displayed coefficients are forced.

## 4. Explicit clocks for every vertex

### 4.1 Short suffixes

`H=(r-d,1,...,1)` has a type self-loop and offers ranks
`r-d,...,r-1`.  Marking only the final `a` suffixes realizes `v_a`; marking
none realizes zero.  This need not be a self-loop on each labelled
partition; the biregular same-owner lift supplies the literal circulation.

### 4.2 Long rotor

Fix `b>d`.  Take a permanent current core of size `r-b-1` and a mobile set
of size `b+1`.  For every positive composition

```text
a_0+...+a_d=b+1,
```

use type

```text
c=(r-b-1+a_0,a_1,...,a_d)
```

and rotate the mobile blocks:

```text
(a_0,...,a_d)->(a_d,a_0,...,a_(d-1)).                 (4.1)
```

Give every displayed rotation edge mass `1/C(b,d)`.  This is legal by
(2.1), has normalized total mass one, and makes positive compositions
uniform.  They are equivalent to uniform `d`-subsets of the `b` cut
positions.  Therefore each rank in
`r-b,...,r-1` is offered with probability `d/b`, giving `(d/b)v_b`.

### 4.3 Mixed rotor

Fix `1<=a<d<b`.  Put

```text
D=d-a, L=b-a, R=r-a.
```

Use the preceding long rotor with owner rank `R`, depth `D`, and long
suffix length `L`, then append `a` singleton age classes to every type.
Legality at the interface follows from positivity of the last mobile block;
all later comparisons are `1<=1`.

Equivalently, every reduced rotation edge has mass `1/C(b-a,d-a)`.
The reduced rotor offers ranks `r-b,...,r-a-1` with probability
`D/L=(d-a)/(b-a)`.  The appended rail offers every rank
`r-a,...,r-1` with probability one.  Hence the marked vector is

```text
((b-d)/(b-a))v_a+((d-a)/(b-a))v_b.
```

Convex combinations prove Theorem 1.

## 5. The true triangular vector is monotone

Use the canonical `r,W,Lambda,d,h,b` from Theorem 1.  Then

```text
b_1>=b_2>=...>=b_d>=0.
```

Binomial coefficients increase through rank `r-1`, so

```text
q_(s+1)-q_s=(C(k,s+1)-C(k,s)+b_s-b_(s+1))/W>=0.
```

Also `0<=q_s<=1` and

```text
sum_s q_s=(Lambda-h)/W<=d.
```

Thus `q in M_(r,d)` and Theorem 1 supplies a balanced invariant literal
fractional clock.  A fixed rank-`s` target lies in `C(k-s,r-s)` owners, while a uniform
rank-`s` suffix of one owner has probability `1/C(r,s)`.  Its central load
is therefore

```text
C(k-s,r-s) q_s/C(r,s)
 = W q_s/C(k,s)
 = 1-b_s/C(k,s),
```

exactly complementary, after the common symmetric fractional averaging, to
the Ferrers boundary.  This is not an integral named-target cover.

## 6. Exact scope and the next gate

The long rotor on the `C(b,d)` positive mobile compositions decomposes into

```text
kappa(b,d)=1/(d+1) sum_(q | gcd(d+1,b+1))
              phi(q) C((b+1)/q-1,(d+1)/q-1).         (6.1)
```

type necklaces.  In the mixed case replace `(d+1,b+1)` by
`(d-a+1,b-a+1)`.  The same-owner literal lift has at least `W kappa`
type-projected components and may split further.

This theorem removes all invariant fractional rank and trace-balance cuts.
It does not fuse the rotor necklaces integrally.  In fact, on the
**complete core-free positive-composition type set with uniform marginals**,
any bijective successor map satisfying (2.1) is forced termwise to be the
cyclic rotation (4.1), by summing each coordinate inequality over the
finite composition set.  The same conclusion holds for a legal coupling
with those uniform marginals by Birkhoff decomposition.

This rigidity does not cover positive permanent cores, nonuniform laws,
altered multisets, labelled-state bijections, or a different support which
realizes the same `q`.  Therefore a physical integral theorem must either
use a split-rotor/owner-changing successor system or introduce explicit
off-rotor connector macros; merely rematching the fixed core-free type set
cannot fuse its necklaces.
