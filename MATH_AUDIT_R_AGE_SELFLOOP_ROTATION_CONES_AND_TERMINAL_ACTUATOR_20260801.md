# Independent audit: age self-loop/rotation cones and the terminal-gap actuator

Date: 2026-08-01

Status: exact theorem and independent audit.  The self-loop and positive
rotation-orbit cones are both too small for the triangular age target from
`k=6` onward.  A parametric terminal single-hole actuator is valid, but the
actual systematic residue assignment has a completion-independent Strassen
obstruction at `k=76`.  Thus completion-only actuator libraries cannot prove
the proposed all-dimensional Unit-descent lemma.  None of these statements
rounds one trace per owner or proves a physical Catalan/compiler theorem.

## 1. Audited objects and the exact option-flow formulation

Let

```text
C_(r,d)={c=(c_0,...,c_d): c_0>0, c_i>=0, sum c_i=r}
```

and write

```text
P(c)=(c_0,...,c_(d-1)),   Q(c)=(c_1,...,c_d).
```

The age arc `c -> c'` is legal exactly when

```text
Q(c')<=P(c)                                             (1.1)
```

coordinatewise.  For a type `c`, let `D(c)` be its set of positive suffix
deficits, namely the distinct positive values among

```text
c_d, c_d+c_(d-1), ..., c_d+...+c_1.                  (1.2)
```

Consider any finite marked-profile family with masses `w_A`, where every
profile `A` is a set of at most `d` deficits.  Put

```text
Omega_A={c in C_(r,d): A subset D(c)}.
```

### Theorem 1.1 (profile-respecting age circulation)

The profiles admit an age circulation if and only if there are nonnegative
variables `x_(A,c)` and `f_(c,c')` satisfying

```text
sum_(c in Omega_A) x_(A,c)=w_A,                       (1.3)
pi(c)=sum_A x_(A,c),                                  (1.4)
sum_(c':c->c') f_(c,c')=pi(c),                        (1.5)
sum_(c':c'->c) f_(c',c)=pi(c).                        (1.6)
```

For fixed `pi`, equations (1.5)--(1.6) are equivalently the exact Strassen
cuts

```text
Q_*pi <=_st P_*pi.                                    (1.7)
```

#### Proof

Assign every profile occurrence to its completed type and count consecutive
type transitions.  This gives (1.3)--(1.6).  Conversely, split each profile
mass according to `x`; a finite conserved flow `f` decomposes into weighted
directed cycles, and every used type contains all marks assigned to it.  The
labelled age-partition lift from the audited quotient realizes the resulting
weighted same-owner trace circulation.  For rational data, denominator
scaling gives a finite periodic literal circulation.  Arbitrary real data
remain a measure, and one-copy/simple-word realization is outside this
theorem.  Eliminating `f` is precisely finite-poset Strassen, because (1.1)
is the product-order transport relation.  QED.

This is the honest Unit-descent object.  The rowwise inequality
`g_(i+1)>=g_i-1` is not a substitute for (1.5)--(1.7).

## 2. The scalar unit-drop law is insufficient

Take

```text
d=2, W=3, r=6, n=(2,1,1,1,1).
```

The exact systematic residue construction gives

```text
A_0={1,3}, A_1={1,4}, A_2={2,5}.                     (2.1)
```

Their gap vectors `(1,2),(1,3),(2,3)` all satisfy the unit-drop law.  Since
each row already has two distinct marks, its type is forced:

```text
X=(3,2,1), Y=(2,3,1), Z=(1,3,2).                    (2.2)
```

But `Z` has no successor among these three types: a successor must have
`c'_1<=c_0(Z)=1`, whereas their first positive-age coordinates are `2,3,3`.
Equivalently, the product-order down-set

```text
Delta={x:x_1<=1}
```

has positive `P`-mass and zero `Q`-mass.  This is an exact Strassen cut.
It refutes any proof using only nonincreasing `n_t` and unit drop.  It is not
itself a binomial triangular instance.

## 3. Exact self-loop cone

A type has a self-loop exactly when

```text
c_0>=c_1>=...>=c_d.                                  (3.1)
```

List its distinct positive deficits increasingly as

```text
t_i=g_1+...+g_i, 1<=i<=m.
```

Then, and only then,

```text
1<=m<=d,
1<=g_1<=...<=g_m<=g_(m+1):=r-t_m.                   (3.2)
```

The converse type is

```text
(g_(m+1),g_m,...,g_1,0,...,0).
```

Consequently the downward marked self-loop polytope is

```text
K_(r,d)=conv{1_A: A subset D, D satisfies (3.2)}.    (3.3)
```

For every nonnegative deficit weight vector `w`, put

```text
H_(r,d)(w)=max_D sum_(t in D) w_t,                   (3.4)
```

where `D` ranges over (3.2).  The exact anti-blocker description is

```text
x in K_(r,d) iff x>=0 and
                  w.x<=H_(r,d)(w) for every w>=0.     (3.5)
```

The support function is an integral longest-path problem.  Start at
`(0,0,0)` (with the first positive gap unrestricted by that sentinel).  Its
nonempty states are `(j,t,g)`; an edge to `(j+1,t+g',g')` is allowed when

```text
g'>=g,  g'<=r-(t+g'),  j+1<=d,                      (3.6)
```

and earns `w_(t+g')`.  One may terminate after any `1<=j<=d`; the separate
empty path represents the empty profile.  Thus there is an exact network
extended formulation, but not a polymatroid shortcut.

Indeed, for `r=8,d=2` the admissible two-point deficit sets are exactly

```text
{1,2},{1,3},{1,4},{2,4},{2,5}.                      (3.7)
```

The independent sets `I={3}` and `J={2,5}` violate augmentation.  Equivalently,
for `X={2,3}`, `Y={3,5}`, the rank values are

```text
rho(X)=rho(Y)=rho(X intersect Y)=1,
rho(X union Y)=2,
```

which violates submodularity.

### Theorem 3.1 (sharp self-loop support cutoff)

Every deficit supported by a self-loop satisfies

```text
t<=floor(d r/(d+1)).                                  (3.8)
```

Every positive integer satisfying (3.8) is supported by some self-loop.

#### Proof

For the largest deficit in (3.2),

```text
t_m=sum_(i<=m)g_i<=m(r-t_m)<=d(r-t_m).
```

Every earlier deficit then obeys the same bound.  Conversely, take
`m=min(d,t)` and split `t` into `m` positive, nondecreasing parts differing
by at most one.  If `m=d`, (3.8) gives `ceil(t/d)<=r-t`; if `m=t<d`, all
parts are one and `r-t>=1`.  Append the final gap `r-t` and use (3.2).  QED.

## 4. The triangular target is outside the self-loop cone

Put

```text
r=ceil(k/2), W=C(k,r),
Lambda=sum_(1<=s<r) C(k,s),
d=min{q:qW+C(q+1,2)>=Lambda}.
```

For every `k>=6`,

```text
d<=r-2.                                               (4.1)
```

For `k=6` this is the direct equality `21=1*20+1`.  If `k=2r` and
`r>=4`, monotonicity of the lower binomial coefficients gives

```text
Lambda/W
 <= r/(r+1)+(r-2)r(r-1)/((r+1)(r+2))
 <= r-2,
```

where the final numerator difference is `3r^2-8r-4>=0`.  If `k=2r-1`,
the case `r=4` is direct, while for `r>=5`,

```text
Lambda/W<=1+(r-2)(r-1)/(r+1)<=r-2.
```

This proves (4.1).

The boundary board has `b_1<=d`, so its triangular residual rank-one mass is

```text
q_1=(k-b_1)/W>0.                                     (4.2)
```

In deficit coordinates this is deficit `r-1`.  By (4.1),
`r-1>floor(dr/(d+1))`; hence every self-loop column has zero capacity there.
The exact Farkas separator is the single weight

```text
w_(r-1)=1, w_t=0 otherwise.                          (4.3)
```

Thus the self-loop cone fails for every `k>=6`.  For `k<=5`, the actual
depth has `d>=r-1` (or the lower ideal is empty), and the type consisting of
`r` ones followed by zeros contains every strict-lower rank.  Hence the
classification is exact: the actual triangular target lies in the self-loop
cone exactly for `k<=5`.

## 5. Positive rotation-orbit mixtures also fail

This section returns temporarily to **lower-rank coordinates** `s`; Sections
2--4 used deficit coordinates `t=r-s`.

Let `c` be a positive composition of `r` into `n=d+1` parts, and average
the rank-capacity vector over its cyclic rotation orbit.  Every proper cyclic
interval of part-sum `s` is paired with its complementary interval of sum
`r-s`.  Therefore

```text
a_s(c)=a_(r-s)(c).                                   (5.1)
```

Moreover, `a_1` is the fraction of parts equal to one.  In the actual
regime `r>d+1`, at least one part exceeds one, so

```text
a_(r-1)=a_1<=d/(d+1).                                (5.2)
```

Because `b_(r-1)=0`, the triangular demand is

```text
q_(r-1)=1                    if k=2r-1,
q_(r-1)=r/(r+1)              if k=2r.                (5.3)
```

Both values are strictly larger than `d/(d+1)` when `r>d`.  Thus the exact
one-coordinate normalized separator is

```text
y_(r-1)=(d+1)/d.                                     (5.4)
```

Positive rotation orbits alone also fail for every `k>=6`.

For reference, even their union with self-loop columns has the valid
inequality

```text
a_(r-1)+(1/d)a_1<=1.                                 (5.5)
```

For a loop column, `a_1=0` in the regime `d<r-1`; for a rotation column,
(5.5) is (5.2).  Hence every odd `k>=7` violates the combined cone because
`q_(r-1)=1` and `q_1>0`.  Exact rational LP duals on the H100 CPU for every
actual triangular instance `1<=k<=40` agree: the combined cone is feasible
for `k<=6` and for every tested even `k`, and fails for every tested odd
`k>=7`.  The even pattern is finite evidence only; no all-even mixture
theorem is claimed.

At `k=6`, the combined equality is transparent: half the mass on the loop
type `(2,1)` and half on the positive rotation orbit of `(1,2)` gives
capacities `(1/4,3/4)`, exactly the triangular vector.

## 6. The uniform single-hole terminal actuator

Theorem 4.1 of
`MATH_THEOREM_TERMINAL_GAP_ACTUATOR_AND_K76_SYSTEMATIC_OBSTRUCTION_20260801.md`
is correct.  For

```text
d>=3, r>=d+2, 2<=j<=d, L=r-d-1,
```

let `C_j` have coordinates

```text
(C_j)_0=1, (C_j)_1=L, (C_j)_j=2,
(C_j)_i=1 otherwise (i>=2).
```

The donor type `B_j`, all-one type `D`, and moving-token types `R_p` form
the legal cycle

```text
C_j -> D -> R_1 -> ... -> R_(j-2) -> B_j -> C_j.    (6.1)
```

The only source-text correction is semantic: `B_j` has a zero in its full
cumulative suffix-deficit **list**, but its positive available deficit set
is exactly `H_j`; zero is not a marked deficit.  That wording has been fixed
in the theorem.

If a stationary residual law is stocked as

```text
sigma+a e_(C_j)+2a e_(B_j)+a sum_p e_(R_p),          (6.2)
```

changing `a` donor completions from `B_j` to `D` replaces the nonstationary
stock by uniform mass on (6.1).  The marks are unchanged because `B_j` and
`D` both contain `H_j`.  This is an unconditional parametric actuator, with
cycle length `j+1<=d+1`; the stock decomposition (6.2) is a real hypothesis.

At `k=54`, the published five-cycle repair is valid but not minimal in the
age quotient.  The forced type

```text
C=(1,21,2,1,1,1)
```

has the exact three-cycle

```text
C -> (22,1,1,1,1,1) -> (22,2,1,1,1,0) -> C.        (6.3)
```

Moving 54 occurrences of donor profile `{1,2,3,5}` from the last type to
the middle type preserves every mark.  An independent exact H100 `-O3`
replay verifies both the repair and stationarity of the residual after the
three-cycle stock is removed.

## 7. The first certificate-backed completion-independent obstruction is `k=76`

At

```text
k=76, r=38, d=5, h=0,
W=6,892,620,648,693,261,354,600,
```

the systematic profile

```text
A_*={2,3,4,6,37}                                     (7.1)
```

occurs exactly 76 times and, being full, forces

```text
C_*=(1,31,2,1,1,2).                                  (7.2)
```

Every successor `Y` must have

```text
Q(Y)<=(1,31,2,1,1).                                  (7.3)
```

If `u_1<=...<=u_5` is its suffix-deficit list with zeros and multiplicities
retained, then

```text
u_1<=1, u_2-u_1<=1, u_3-u_2<=2, u_5-u_4<=1.         (7.4)
```

The exact breakpoint classification has 38 profiles.  Every five-mark
profile beginning with one has final gap at least two; every five-mark
profile beginning with two violates `u_1<=1`; and the only four-mark profile
is `{2,3,4,6}`.  In the latter case the fifth slot must occur before two,
leaving final gap `6-4=2`.  Thus no systematic profile can be completed to
a successor satisfying (7.3).

For the principal down-set

```text
Delta={x:x<=(1,31,2,1,1)},                           (7.5)
```

every completion law has `P`-mass at least `76/W` and `Q`-mass zero.  This
violates Strassen.  An independent H100 `-O3` replay enumerates all 768
bounded successor types and finds zero compatible profile pairs.

Consequently the original systematic Unit-descent lemma is false, not merely
unproved.  A library which changes only unmarked completions cannot repair
it, regardless of actuator radius.  Minimality at `k=76` uses the separately
authenticated exact scan: zero-fill or a one-profile repair works through
`k=75` (with the small boundary cases audited independently).  It is not a
consequence of the displayed `k=76` inequalities alone.  The broader
age/Strassen target remains open because it may regroup the marked deficits
before completion.

## 8. Exact protected-Catalan interface after the obstruction

The `k=76` cut forces a pre-completion marked-profile exchange.  At minimum,
each dead full row must relinquish a marked deficit and another row must take
it, preserving every global deficit count.  Abstractly the primitive is a
row/deficit alternating circuit, for example a count-neutral exchange

```text
(A-x, B-y) -> (A-x+y, B-y+x).                        (8.1)
```

Only after such an exchange may the resulting profiles be completed into
the actuator cycles (6.1).

In a protected Catalan host this is strictly stronger than rank-symmetric
mark neutrality.  A physical actuator must simultaneously provide:

1. distinct one-copy owner occurrences for every exchanged row and age arc;
2. a target-occurrence alternating circuit realizing (8.1), not only equal
   rank counts;
3. preserved upper-witness and common-cap payloads on the same occurrences;
4. a payload-transparent splice of the labelled actuator cycles into the
   rooted Catalan chronology with residence intact.

The existing fixed-bank avoidance theorem can protect a *chosen* `O(d)`
actuator bank.  It does not create the mark-exchange circuit or choose its
owners.  This four-row product condition is the precise remaining protected
host theorem; no `B(k)+O(1)` implication is asserted here.

## 9. Computational audit ledger

All range work below ran on one capped H100 CPU core; no sustained local
Python or C++ enumeration was used.

```text
scratch/audit_r_age_selfloop_rotation_cones_20260801.py
e6de3eda6a022e3192b47abcc240dd2dc83fb0430809e8073cb42181f29f1c25

scratch/r_age_cones_k1_20.audit.json
d89fb230363d6e53ee6230c95e39e484b424bf569b0bb3170c1f9f97f4972203

scratch/r_age_cones_k21_40.audit.json
47d8ae7bf108c45e725db905f716f1c541b54dc0af38b8c2e53788897fe4deb9

scratch/audit_r_unit_descent_option_circulation_20260801.py
989eff78bc256a4f6d85f7dc93eb387b7fee7fe6ae8a8cab07a6d859803bd793

scratch/r_unit_descent_k1_16.audit.json
5629bd30891f36f6b163aa3832ba846de7d9f4e64fd6d37cc5dbcde0d874be3a

scratch/r_unit_descent_k17_24.audit.json
f366804983beb3167acc425838ca582497d6714ce5cc10aadb75740bd3f892d5

scratch/r_unit_descent_k25_30.audit.json
b58d48ae25aa281f3ff28d3098d2cfd7a0b40038b3f7828e6006ded3f81c7328

scratch/r_unit_descent_k31_34.audit.json
2d42f69faf0bbf51cbc54c705ead30d6330158dee778d90f1de511198f44c37d

scratch/r_age_k54_threecycle_probe_h100.out
44bebb89fb1fe83ce3a75261aff1fadd58d3df581a7227eecae9ce1aed61455d

scratch/r_age_k54_threecycle_probe_h100.tsv
10061e819fe4e953aeb9d6380f443b4aea3c6f60799f59eccd3035536aca6f1c

scratch/r_age_single_hole_actuator_independent_h100.out
7805bd3679c02e2eecee25675efc3fe3c88e3165a06804289198a9696093b385

scratch/r_age_k76_independent_h100.out
37ee832cdc02bd7106b81e83fa6e4e1b86fbd68a295695b7fac9415b644f6695
```

The grouped option-circulation model gives exact integral witnesses for every
actual systematic instance through `k=34`.  The stronger authoritative scan
then proves zero-fill or one-profile repaired feasibility through `k=75` and
the no-successor theorem at `k=76`.  These finite ledgers support the symbolic
theorems but are not used to extrapolate beyond their stated ranges.

## 10. Final implication boundary

The audited conclusions are

```text
age quotient + Strassen cuts: exact fractional reduction;
self-loop cone: exactly closed negative from k=6;
positive rotation cone: exactly closed negative from k=6;
single-hole terminal completion: uniformly repairable with stock;
fixed systematic profiles: exactly refuted at k=76;
arbitrary marked-profile age circulation: still open;
one-copy protected Catalan/compiler realization: still open.
```

The shortest viable next theorem is therefore not another completion rule.
It is a bounded, occurrence-labelled marked-profile exchange packet which is
simultaneously age-circulable and transparent to a prospective protected
Catalan/common-cap host.
