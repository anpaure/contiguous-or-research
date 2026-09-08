# Residual age profiles: exact extreme normalization and the first nonfull self-loop obstruction

Date: 2026-08-01  
Lane: residual age stationarity after items 2503MH/2507RS  
Status: unconditional structural theorems plus an exact canonical-boundary
census.  This note disproves two tempting residual classifications.  It does
not refute the arbitrary-hole parity-sweep actuator and does not settle the
joint stationary residual law (2507RS, equations (5.2)--(5.3)).

## 1. Setup

Fix owner rank `r` and depth `d`.  A marked profile is a set

```text
A={t_1<...<t_s} subseteq {1,...,r-1},  s<=d.
```

If `s=d`, its age composition is forced:

```text
c(A)=(r-t_d, t_d-t_(d-1), ..., t_2-t_1, t_1).       (1.1)
```

A self-loop age type is exactly a composition

```text
c_0>=c_1>=...>=c_d.                                  (1.2)
```

Equivalently, its positive deficit set has consecutive gaps

```text
g_1<=g_2<=...<=g_s<=r-sum_i g_i.                    (1.3)
```

The canonical multi-hole family from item 2503MH is

```text
A_(q,m)=([d-1]\{m}) union {d+q-1,r-1},
d>=3, q>=2, 1<=m<=d-1.                              (1.4)
```

## 2. Every full extreme profile is an arbitrary-hole row

### Theorem 2.1 (exact extreme normalization)

Let `A` have `d` marks and contain `r-1`.  Put

```text
B=max(A\{r-1}),
h=B-d+1,
H=[B]\(A\{r-1}).                                    (2.1)
```

Then `h>=0`, `|H|=h`, `H subseteq [B-1]`, and

```text
A=([B]\H) union {r-1}.                              (2.2)
```

If `h>=1`, this is exactly the normalized arbitrary-hole row of
`MATH_THEOREM_R_ARBITRARY_HOLE_PARITY_SWEEP_MARK_ACTUATOR_20260801.md`.
Its rank hypothesis is automatic: since `B<r-1`, one has `r>=B+2`.
The case `h=0` is the no-hole terminal row `[d-1] union {r-1}`.

#### Proof

There are `d-1` small marks, all lying in `[B]` and including `B`.  Hence

```text
|H|=B-(d-1)=B-d+1=h,
```

and `B notin H`.  Equation (2.2) is the definition of `H`.  The strict
inequality `B<r-1` gives the last assertion.  QED.

Thus the later arbitrary-hole parity theorem really does close the **local
age algebra** of every full extreme profile.  The narrower canonical family
(1.4), however, does not contain all such profiles.

## 3. The canonical `A_(q,m)` classification is false

### Theorem 3.1 (first canonical-boundary noncanonical multi-hole row)

For the canonical triangular boundary at

```text
k=140, r=70, d=7,
W=C(140,70)=93820969697840041204785894580506297666600,
```

the systematic residue construction contains the full extreme profile

```text
A={1,2,4,5,7,9,69}                                  (3.1)
```

with multiplicity `140`, on the exact residue interval

```text
[87061984418121705341882881246970362228847,
 87061984418121705341882881246970362228987).         (3.2)
```

It is a normalized three-hole row but is not `A_(q,m)` for any `q,m`.

#### Proof

The exact breakpoint calculation in the frozen audit gives (3.1)--(3.2).
For this row `B=9`, and its holes in `[8]` are

```text
H={3,6,8}.                                           (3.3)
```

If it were canonical, `B=d+q-1` would force `q=3`; the canonical holes
would then be

```text
{m,d,d+1}={m,7,8},                                   (3.4)
```

which cannot equal (3.3).  QED.

The exact O3 census checks every canonical-boundary breakpoint segment for
`3<=k<=183`; among genuine multi-hole rows (`h>=2`) (3.1) is the first
noncanonical example.  This finite minimality is audit-backed rather than
needed for the mathematical counterexample.

### Consequence

Item 2503MH plus its canonical stocking theorem 2507RS cannot by itself be
applied to every fully marked extreme systematic row.  The arbitrary-hole
parity-sweep theorem is essential, and its broader donor/reservoir profiles
must be included in any stocking theorem used downstream.

## 4. Nonfull systematic rows are not always self-loop-completable

### Theorem 4.1 (explicit residual self-loop obstruction)

For the canonical triangular boundary at

```text
k=183, r=92, d=9,
W=C(183,92)=720162138745872857431467203815692960288647797444355400,
```

the systematic residue construction contains the nonfull profile

```text
A={1,2,4,5,6,8,9,13}                                (4.1)
```

with multiplicity

```text
285916660092460398796273644655925707923024842785460. (4.2)
```

It has no self-loop completion using at most `d=9` deficit marks.

#### Proof

The exact breakpoint interval is

```text
[685904606140346905956251726870448868972373748582013750,
 686190522800439366355048000515104794680296773424799210),
```

whose length is (4.2).

Suppose a self-loop deficit set `D` of size at most nine contained (4.1).
Its consecutive gaps must be nondecreasing by (1.3).

The required consecutive marks `2<4<5` give gaps `2,1` unless another mark
is inserted strictly between `2` and `4`.  The only possible repair is to
insert `3`.  Independently, `6<8<9` gives another forced `2,1` descent, and
the only possible repair is to insert `7`.  Thus every self-loop completion
must add both `3` and `7`.  Profile (4.1) already has eight marks, while
`d=9` permits only one additional mark.  Contradiction.  QED.

The exact dynamic-program audit exhausts self-loop completions of every
canonical-boundary profile through `k=183`; (4.1) is the first **nonfull**
failure.  Again, only the explicit failure—not finite minimality—is used in
the theorem.

## 5. Rotation completion is local and therefore not the residual theorem

There is an important qualification.  Every profile `A` with `|A|<=d` can
be embedded in a positive rotation cycle whenever it extends to a `d`-set
`F subseteq [r-1]`: take the forced positive composition `c(F)` and all
cyclic rotations of its `d+1` positive coordinates.  Uniform mass on that
orbit is stationary.

For (4.1), for example, take

```text
F=A union {3},
c(F)=(79,4,1,2,1,1,1,1,1,1).                         (5.1)
```

Then `A subseteq Def(c(F))`, and the ten rotations of (5.1) form a legal
stationary cycle.

This does **not** solve the residual law.  One occurrence of `A` consumes
only one vertex of the rotation orbit; the other nine occurrence roles must
be stocked by rows whose own required marks fit the rotated deficit sets.
Doing this independently for every residual row can require more than `W`
roles.  Thus the statement

```text
every profile is locally rotation-completable
```

is true but too weak, while

```text
every non-extreme profile is self-loop-completable
```

is false by Theorem 4.1.

## 6. Correct residual frontier

After 2503MH/2507RS and the arbitrary-hole parity theorem, the remaining
age-level assertion is still the global integral circulation

```text
sum_c' f_(c,c')=sum_c' f_(c',c)=sigma_c,
sum_c sigma_c=U,
n'_t <= sum_(c:t in R(c)) sigma_c.                    (6.1)
```

Theorems 3.1 and 4.1 show that it cannot be proved by either of the two
following classifications:

1. all full extreme rows are canonical `A_(q,m)`;
2. after removing extreme actuator rows, every residual nonfull row closes
   on a self-loop.

A proof must instead do at least one genuinely global thing:

* stock the full arbitrary-hole parity bank and prove the remaining
  Strassen cuts directly; or
* pack the companion roles of positive rotation orbits jointly, sharing
  reservoirs across many marked rows.

No new obstruction to (6.1) itself is claimed here.  In particular,
Theorem 4.1 has the local rotation repair (5.1).

## 7. Frozen audit

```text
scratch/audit_residual_stationarity_profile_obstructions_20260801.cpp
SHA256 0192c7cfc03ea131a192bd0565006f32cc3bceb45dd48f9e585e1436c7683487

scratch/residual_stationarity_profile_obstructions_20260801.audit.json
SHA256 941735dcb5db5ee500f66ebd81f41657b12ffb4260fbfa770b4d4dac6bfb46b5
status PASS_RESIDUAL_STATIONARITY_PROFILE_OBSTRUCTIONS
```

The scan was compiled with `g++ -O3 -DNDEBUG` and run on one H100-host CPU
core.  It uses exact arbitrary-precision integer arithmetic, enumerates
breakpoint segments rather than the exponentially many residue rows, and
independently tests self-loop completion by the nondecreasing-gap dynamic
program.
