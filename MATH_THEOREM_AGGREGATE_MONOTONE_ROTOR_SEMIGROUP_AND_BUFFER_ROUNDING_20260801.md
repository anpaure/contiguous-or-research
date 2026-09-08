# Aggregate monotone-rotor semigroup: first hole and exact buffer rounding

Date: 2026-08-01  
Lane: integral sequel to the monotone-rotor fractional trace theorem  
Status: unconditional age-profile semigroup theorem, with an independently
replayed exact finite audit for the stated sharp threshold.  The raw
uniform-rotor semigroup is not normal, but the canonical binomial demand
belongs to it for every `k>=31`.  This closes the **aggregate invariant
integer age-signature decomposition**.  It does not give a primitive
one-copy labelled lift, select named owners or targets, or provide physical
owner fusion, residence, upper shadows, or a common cap.

## 1. Integer coordinates and the rotor generators

Fix `r>d>=1`.  Write a rational point of the monotone polytope as

```text
q=sum_(ell=1)^(r-1) alpha_ell v_ell,
alpha_ell>=0,
sum alpha_ell<=1,
sum ell alpha_ell<=d.
```

After multiplying by an owner count `W`, put

```text
A_ell=W alpha_ell                 (1<=ell<r),
A_0=W-sum_(ell>=1) A_ell.
```

Thus `A_0` is the zero-vertex multiplicity.  The integral uniform rotor
packages have the following role vectors.

* `e_0` and `e_a`, `1<=a<=d`, are the zero/short self-loop packages.
* For `b>d`, the long package is

```text
g_(0,b)=q_(0,b)e_0+p_(0,b)e_b,
q_(0,b)=C(b-1,d),
p_(0,b)=C(b-1,d-1).
```

* For `1<=a<d<b`, the mixed package is

```text
g_(a,b)=q_(a,b)e_a+p_(a,b)e_b,
q_(a,b)=C(b-a-1,d-a),
p_(a,b)=C(b-a-1,d-a-1).
```

Pascal's identity says that the type-occurrence mass of a nontrivial
package is

```text
q_(a,b)+p_(a,b)=C(b-a,d-a).
```

It is useful to regard `a=0` as an ordinary low coordinate.  Put

```text
u_a=d-a,                  0<=a<d,
v_b=b-d,                  d<b<r.
```

Then every nontrivial rotor package has the exact resource identity

```text
u_a q_(a,b)=v_b p_(a,b)=:w_(a,b).                  (1.1)
```

### Proposition 1.1 (exact semigroup equations)

The integer vector `A=(A_0,...,A_(r-1))` belongs to the semigroup generated
by the uniform short, long, and mixed rotors if and only if there are
nonnegative integers `z_(a,b)`, `0<=a<d<b<r`, such that

```text
A_b=sum_(a=0)^(d-1) p_(a,b) z_(a,b)                (b>d),
sum_(b=d+1)^(r-1) q_(a,b) z_(a,b)<=A_a             (a<d).   (1.2)
```

The unused low coordinates and all of `A_d` are filled by unit self-loop
packages.

The monotone-polytope inequalities imply the single aggregate resource cut

```text
H:=sum_(b>d) v_b A_b
 <=
L:=sum_(a<d) u_a A_a.                              (1.3)
```

Equation (1.3) is the fractional transportation condition.  Equations
(1.2) are its batched integral refinement.

## 2. The semigroup is not normal

### Proposition 2.1 (smallest-depth hole)

At `d=2`, `r=4`, and `W=2`, take

```text
A_0=1, A_3=1, and every other A_ell=0.              (2.1)
```

This vector lies in `2 M_(4,2)`: it has

```text
alpha_3=1/2,
sum alpha=1/2<=1,
sum ell alpha_ell=3/2<=2.
```

But it is not in the uniform-rotor semigroup.  The only packages containing
coordinate `3` are

```text
g_(0,3)=e_0+2e_3,
g_(1,3)=e_1+e_3.
```

The first oversupplies `A_3`; the second forces an unavailable `A_1`.
Hence the cone contains an integral point outside the semigroup.

Depth one has no such hole: (1.3) reads

```text
sum_(b>=2)(b-1)A_b<=A_0,
```

and using `A_b` copies of `g_(0,b)=(b-1)e_0+e_b` gives an integral
decomposition.  Thus (2.1) is the first hole by trace depth and aggregate
mass.

There can be no dimension-independent global conductor on every face.  For
example, on the `d=2`, `A_1=0` face, the `b`-coordinate supplied from `A_0`
is restricted to multiples of `b-1`.  The positive result below is therefore
necessarily an interior/target-specific statement.

## 3. Two exact unit buffers

The two adjacent coordinates

```text
ell_-=d-1,             ell_+=d+1
```

are special.  Directly from the binomial formulas,

```text
p_(d-1,b)=1, q_(d-1,b)=b-d,                         (3.1)
q_(a,d+1)=1, p_(a,d+1)=d-a.                         (3.2)
```

Thus `d-1` can repair an arbitrary residual high occurrence one at a time,
and `d+1` can absorb an arbitrary residual low occurrence one at a time.

Define the total non-unit rounding quantum

```text
Q_(r,d)=sum_(a=0)^(d-2) sum_(b=d+1)^(r-1) w_(a,b)
       =sum_(a=0)^(d-2) sum_(b=d+1)^(r-1)
          (d-a) C(b-a-1,d-a).                       (3.3)
```

The part excluding the high buffer is

```text
Q^circ_(r,d)=sum_(a=0)^(d-2) sum_(b=d+2)^(r-1) w_(a,b);
```

clearly `Q^circ<=Q`.

### Lemma 3.1 (balanced two-buffer rounding)

Assume `L=H` and

```text
A_(d-1)>=Q^circ_(r,d),
A_(d+1)>=Q^circ_(r,d).                              (3.4)
```

Then `A` belongs to the uniform-rotor semigroup.

### Proof

Delete the two buffer coordinates.  Put

```text
L^circ=sum_(a=0)^(d-2) u_a A_a,
H^circ=sum_(b=d+2)^(r-1) v_b A_b,
Y_0=H^circ-A_(d-1)=L^circ-A_(d+1).                 (3.5)
```

If `Y_0<=0`, take no internal transport and put `Y'=0`.  If `Y_0>0`, the complete
bipartite resource graph admits a fractional transport of total

```text
Y=Y_0+Q^circ.                                       (3.6)
```

Indeed (3.4)--(3.5) give

```text
Y<=min(L^circ,H^circ).
```

For each internal edge write its resource flow as `y_(a,b)` and round its
rotor multiplicity down:

```text
z_(a,b)=floor(y_(a,b)/w_(a,b)).                     (3.7)
```

The total lost resource is strictly less than the sum of all internal edge
quanta, hence less than `Q^circ`.  Therefore the retained internal resource
`Y'` satisfies `Y'>=Y_0`.

For every nonbuffer low coordinate, send each residual occurrence to the
high buffer using (3.2).  This consumes `L^circ-Y'<=A_(d+1)` high-buffer
occurrences.  For every nonbuffer high coordinate, use (3.1) once for each
residual occurrence.  This consumes `H^circ-Y'<=A_(d-1)` low-buffer
occurrences.  The two buffer remainders are both exactly

```text
Y'-Y_0,
```

and are paired by `g_(d-1,d+1)=e_(d-1)+e_(d+1)`.
All coordinates are now exact.  QED.

### Lemma 3.2 (one-buffer rounding with scalar slack)

Put `E=L-H`.  If

```text
E>=Q_(r,d),
A_(d-1)>=Q_(r,d),                                  (3.8)
```

then `A` belongs to the uniform-rotor semigroup.

### Proof

Use only the low coordinates `a<=d-2` in a fractional transport.  Transport

```text
Y=min(H,L-A_(d-1))
```

units of high demand.  Its untransported high resource is

```text
R=max(0,H-(L-A_(d-1)))=max(0,A_(d-1)-E)
 <=A_(d-1)-Q.                                       (3.9)
```

Round every used edge down as in (3.7).  The additional loss is less than
`Q`, so all remaining high occurrences can be supplied one at a time from
coordinate `d-1` by (3.1).  Every unused low occurrence is a short
self-loop.  QED.

## 4. A target-specific conductor theorem

### Theorem 4.1 (exact buffered semigroup criterion)

Let `A in Z_>=0^r` satisfy the standing resource inequality `L>=H`.
Assume `d>=4`, `d+1<r`, and

```text
min(A_(d-3),A_(d-2),A_(d-1),A_(d+1))
   >= Q_(r,d)+1.                                    (4.1)
```

Then `A` belongs to the uniform short/long/mixed rotor semigroup.

### Proof

If `E=L-H>=Q`, apply Lemma 3.2.

Suppose `0<=E<Q`.  Remove a low-coordinate vector of resource exactly `E`
and realize it with short self-loops:

```text
E=0:       remove nothing;
E=1:       remove one copy at d-1;
E>=2 even: remove E/2 copies at d-2;
E>=3 odd:  remove one copy at d-3 and (E-3)/2 copies at d-2.  (4.2)
```

Condition (4.1) makes (4.2) available and leaves at least `Q` copies at the
low buffer.  The residual low and high resource totals are equal.  The high
buffer is unchanged and also has at least `Q` copies.  Lemma 3.1 applies.
Finally restore the removed coordinates as unit short packages.  QED.

The theorem is an explicit conductor statement, but its conductor grows
with `(r,d)`.  This is unavoidable globally by Proposition 2.1 and its face
extensions.  Its value is that `Q_(r,d)` is exponentially smaller than the
four canonical binomial buffers.

## 5. The canonical Ferrers demand clears the conductor

For the optimal Ferrers boundary, let

```text
n_s=C(k,s)-b_s                       (1<=s<r),
A_0=W-n_(r-1),
A_ell=n_(r-ell)-n_(r-ell-1)          (1<=ell<=r-2),
A_(r-1)=n_1.                                         (5.1)
```

These are exactly `W` times the alpha coordinates of the monotone demand.

### Theorem 5.1 (exact aggregate age-signature decomposition)

For every `k>=31`, the integer vector (5.1) is an exact sum of formal uniform
short, long, and mixed stationary age-type rotor packages.  Their total
type-occurrence mass is exactly `W=C(k,r)`.

### Proof

First, the central-binomial estimate

```text
C(2r,r)>=4^r/(2 sqrt(r))
```

gives, in both parities,

```text
d<=ceil(sqrt(r)).                                    (5.2)
```

For `r>=64`, the complementary estimate
`C(2r,r)<=4^r/sqrt(3r+1)` gives `Lambda>3W+6`, hence
`d>=4`.  Also `r>2d+2`.  Therefore for each

```text
ell in {d-3,d-2,d-1,d+1},                           (5.3)
```

we have `r-ell-1>d`, so the small Ferrers boundary does not
alter either binomial coefficient in (5.1).  If `k=2r-1`,

```text
A_ell=[2ell/(r+ell)] C(2r-1,r-ell),                 (5.4)
```

and if `k=2r`,

```text
A_ell=[(2ell+1)/(r+ell+1)] C(2r,r-ell).             (5.5)
```

Moreover `ell<=sqrt(r)+2<=5sqrt(r)/4`.  In the even case the ratio to the
central binomial coefficient is

```text
prod_(i=0)^(ell-1) (r-i)/(r+i+1).
```

Writing the factors as `1-x_i`, we have

```text
sum_i x_i<=25/16,       max_i x_i<=5/16.
```

The inequality `log(1-x)>=-x/(1-x)` therefore bounds this product below by
`exp(-25/11)>1/16`.  The odd ratio has one fewer, no smaller, factor.  The
prefactors in (5.4)--(5.5) are at least `1/r`, so uniformly

```text
A_ell>=W/(16r)>=2^(2r-6)/r^(3/2).                  (5.6)
```

On the other hand, hockey-stick summation gives the exact formula

```text
Q_(r,d)=sum_(u=2)^d u C(r-d+u-1,u+1).              (5.7)
```

There are fewer than `dr` original summands, each below `d 2^(r-2)`, and
`d^2<2r` for `r>=64`; hence

```text
Q_(r,d)<r^2 2^(r-1).                                (5.8)
```

Since `2^(r-5)>r^(7/2)` at `r=64` and the ratio increases thereafter,
(5.6)--(5.8) imply `A_ell>Q`, hence integrally `A_ell>=Q+1`, for every
`r>=64`.  Theorem 4.1 applies.

For the remaining finite range, the exact arbitrary-precision O3 checker
named in Section 6 evaluates the defining binomial sums and criterion (4.1)
directly.  It proves the criterion for every `31<=k<=126`; the analytic
tail begins at `k=127`.  (The archived replay actually continues through
`k=1000`.)  Thus every `k>=31` is covered.  QED.

This theorem closes the aggregate **age-type/signature** integrality gap.
It is stronger than an `O(1)` residue statement at this quotient: the
residue is exactly zero for the actual binomial demand.

It does **not** close the labelled problem.  A primitive uniform age-type
package need not have a one-copy labelled lift; the fractional biregular
lift may require denominator multiplication.  The remaining theorem must
first realize and colour the occurrence-labelled flags by distinct named
owners and targets.  Physical cycle fusion, q1 palettes, residence,
arbitrary-width upper witnesses, and the common compiler cap remain later
requirements.

### Proposition 5.2 (primitive labelled-lift obstruction)

At `r=4,d=2,a=1,b=3`, the mixed generator is

```text
g_(1,3)=e_1+e_3
```

and its type cycle is

```text
c=(1,2,1)  <->  c'=(2,1,1).                        (5.9)
```

It has no two-state literal same-owner labelled lift.

### Proof

Write the labelled cells as `C_i,C'_i`.  On `c->c'`, compatibility and
cardinality force `C'_1=C_0`.  On `c'->c`, they force `C_2=C'_1`.
Therefore `C_2=C_0`, contradicting disjointness of the two nonempty cells
of the state `C`.  QED.

Thus clearing the fractional labelled-lift denominators realizes some
multiple of an aggregate package, not necessarily the primitive package or
the original mass `W`.

## 6. Exact audit

The independently replayed O3 checker verifies:

1. by exhaustive small Hilbert-semigroup enumeration through
   `d<=3,r<=6,W<=8`, that the first hole is the
   `d=2,r=4,W=2` vector in Proposition 2.1;
2. the binomial/resource identities used in its construction;
3. nonnegativity of the canonical resource slack; and
4. criterion (4.1) for every `31<=k<=1000`.

The sufficient criterion first passes at `k=23`, then alternates: it passes
at odd `23,25,27,29` but fails at even `24,26,28,30`, where `d=3`.
Its last failure is `k=30`; it passes for all `k>=31`, by the finite replay
through `126` and the analytic tail in Section 5.  A criterion failure is
not a proof of semigroup nonmembership.

```text
scratch/audit_aggregate_monotone_rotor_semigroup_20260801.cpp
scratch/aggregate_monotone_rotor_semigroup_20260801.audit.json
```
