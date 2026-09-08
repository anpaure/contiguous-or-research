# Clean-room audit: aggregate rotor buffers and the Ferrers threshold

Date: 2026-08-01  
Lane: R, independent audit of the integral monotone-rotor sequel  
Verdict: **PASS with one proof-scope completion**

This note audits

```text
MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md
scratch/audit_aggregate_monotone_rotor_semigroup_20260801.cpp
scratch/aggregate_monotone_rotor_semigroup_20260801.audit.json
```

The two-buffer conductor and the Ferrers specialization are correct.  The
theorem file itself proves only “all sufficiently large `k`,” while the O3
artifact checks `31<=k<=1000`.  Those two statements alone leave a formal
gap unless the unspecified asymptotic threshold is bounded.  Section 5
below gives an explicit tail valid for `r>=64`; consequently only
`31<=k<=126` is computational.  Combined with the audited O3 table, this
proves the advertised exact threshold `k>=31`.

## 1. Exact two-buffer audit

Put

```text
u_a=d-a,                 v_b=b-d,
q_(a,b)=C(b-a-1,d-a),    p_(a,b)=C(b-a-1,d-a-1).
```

Then

```text
u_a q_(a,b)=v_b p_(a,b).
```

The two unit identities are exactly

```text
q_(d-1,b)=b-d,  p_(d-1,b)=1,
q_(a,d+1)=1,    p_(a,d+1)=d-a.
```

For Lemma 3.1, delete the buffer coordinates `d-1,d+1`.  If an internal
fractional resource flow `y_(a,b)` is rounded to

```text
z_(a,b)=floor(y_(a,b)/w_(a,b)),
```

the total resource lost is strictly smaller than the sum `Q^circ` of the
internal edge quanta.  The residual low occurrences use the `d+1` buffer,
and the residual high occurrences use the `d-1` buffer.  The two final
buffer remainders are both

```text
Y'-Y_0,
Y_0=H^circ-A_(d-1)=L^circ-A_(d+1),
```

so copies of `g_(d-1,d+1)` close them exactly.  All statements are at the
occurrence level, not merely at total resource level.

Lemma 3.2 is also exact.  Its subtraction `L-A_(d-1)` is dimensionally
correct because `u_(d-1)=1`.  After rounding, the resource still demanded
from the low unit buffer is strictly less than `A_(d-1)` (hence at most it,
integrally).

Theorem 4.1 inherits the standing hypothesis `L>=H` from the monotone
polytope.  Read as a standalone theorem, that hypothesis should be stated
explicitly; without it the displayed two-case proof has no `E<0` case.
Under the standing context, the proof is valid.  The representation of
`E=L-H<Q` by resources `1,2,3` in (4.2) is exact, and (4.1) leaves both unit
buffers at least `Q`.

## 2. Ferrers conventions and telescoping

For every `k>=3`, the audited conventions are

```text
r=ceil(k/2),
W=C(k,r),
Lambda=sum_(s=1)^(r-1) C(k,s),
d=min{q>=0:qW+C(q+1,2)>=Lambda},
h=(Lambda-dW)_+.
```

Thus rank zero is excluded from `Lambda`.  The boundary fills columns of
heights `d,d-1,...,1` from the left, with at most one partial column.  If

```text
n_s=C(k,s)-b_s,
A_0=W-n_(r-1),
A_ell=n_(r-ell)-n_(r-ell-1),
A_(r-1)=n_1,
```

then telescoping gives

```text
sum_ell A_ell=W,
sum_ell ell A_ell=sum_(s=1)^(r-1)n_s=Lambda-h,
E=L-H=dW-(Lambda-h)>=0.
```

There are no floor/ceiling discrepancies in the checker: integer division
is used only for exact binomial construction, while `d` is found by the
literal defining inequality.

When `r-ell-1>d`, the boundary does not touch the two binomial terms in
`A_ell`, and direct subtraction gives

```text
k=2r-1: A_ell=[2ell/(r+ell)] C(2r-1,r-ell),
k=2r:   A_ell=[(2ell+1)/(r+ell+1)] C(2r,r-ell).
```

## 3. The exact finite transition table

The O3 output says

```text
first_conductor_pass_k = 23,
last_conductor_failure_k = 30,
transitions = [23,24,25,26,27,28,29,30,31].
```

Therefore “first pass `23`” is not a monotone threshold.  The exact table is

```text
k<=22: fail,
k=23: pass,  k=24: fail,
k=25: pass,  k=26: fail,
k=27: pass,  k=28: fail,
k=29: pass,  k=30: fail,
k>=31 through the scanned range: pass.
```

The alternation is explained by the exact Ferrers depth:

```text
odd k=23,25,27,29,31: d=4,
even k=24,26,28,30:   d=3,
k=32:                 d=4.
```

For example,

```text
k=30: W=155117520, Lambda=459312151,
      2W+3<Lambda<=3W+6, so d=3;
k=31: W=300540195, Lambda=1073741823,
      3W+6<Lambda<=4W+10, so d=4.
```

Thus `k=30` is a sharp counterexample to the *buffer criterion* being valid
below 31.  It is not a counterexample to semigroup membership: the criterion
is only sufficient and is not applicable when `d=3`.

## 4. Closed form for the rounding quantum

Writing `u=d-a` and `t=b-d`, the quantum is

```text
Q_(r,d)
 =sum_(u=2)^d sum_(t=1)^(r-d-1) u C(u+t-1,u)
 =sum_(u=2)^d u C(r-d+u-1,u+1).                    (4.1)
```

The second equality is the hockey-stick identity.  It is useful both for
an independent implementation and for bounding the conductor.

## 5. Explicit analytic tail

The standard central-binomial bound

```text
C(2r,r)>=4^r/(2 sqrt(r))
```

implies in both parities

```text
d<=ceil(sqrt(r)).                                   (5.1)
```

The complementary bound `C(2r,r)<=4^r/sqrt(3r+1)` gives `Lambda>3W+6`
for `r>=64`, hence `d>=4`: in the odd case it is enough that
`1/4>3/(2sqrt(3r+1))+7/4^r`, and in the even case it is enough that
`1>7/sqrt(3r+1)+14/4^r`.  Both inequalities hold at `r=64` and strengthen
thereafter.

Fix `r>=64` and

```text
ell in {d-3,d-2,d-1,d+1}.
```

Then `1<=ell<=sqrt(r)+2<=5sqrt(r)/4`, and
`r-ell-1>d` because `r>2d+2`.  Thus the Ferrers boundary is absent from
both binomial terms defining `A_ell`.  In the even case,

```text
C(2r,r-ell)/C(2r,r)
 =prod_(i=0)^(ell-1) (r-i)/(r+i+1)
 =prod_i(1-x_i),
x_i=(2i+1)/(r+i+1).
```

Here

```text
sum_i x_i<=ell^2/r<=25/16,
max_i x_i<=5/16.
```

Using `log(1-x)>=-x/(1-x)` gives

```text
C(2r,r-ell)/C(2r,r)>=exp(-25/11)>1/16.             (5.2)
```

For odd `k=2r-1`, the factors are `(r-i)/(r+i)` and the same bound holds.
The prefactors in the two exact formulas of Section 2 are at least `1/r`.
Uniformly in both parities,

```text
A_ell>=W/(16r)>=2^(2r-6)/r^(3/2).                  (5.3)
```

On the other hand, there are fewer than `dr` terms in `Q`, and every term
is at most `d 2^(r-2)`.  From (5.1), for `r>=64`, `d^2<2r`; hence

```text
Q<r^2 2^(r-1).                                     (5.4)
```

At `r=64`,

```text
2^(r-5)>r^(7/2),
```

and the ratio on the left to the right is increasing thereafter.  Equations
(5.3)--(5.4) therefore give `A_ell>Q`, hence the integer inequality
`A_ell>=Q+1`, for every `r>=64`.  Finally (5.1) gives
`d+1<=sqrt(r)+2<r`.

Consequently the finite audit is needed only for `31<=k<=126`; the analytic
tail begins at `k=127`.  This closes every `k>=31`, not merely every
sufficiently large `k`.

## 6. Exact scope of the O3 artifact

The source faithfully computes `r,W,Lambda,d,h,b,n,A,E,Q` with arbitrary-
precision nonnegative integers.  A negative `A` or negative slack would
throw during subtraction, so those signs are checked implicitly.  The
reported transition list follows from testing (4.1) at each integer `k`.

The checker does **not** independently test the displayed closed forms for
`A_ell`, the physical target-load identity, or the proof of the rounding
lemmas.  Those are symbolic claims and were audited above.  Thus the phrase
“every identity in Sections 1 and 5” should not be read as the literal scope
of the executable.

Audited hashes at the time of this note:

```text
MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md
  ad4cdb5b604c3bdd1df6a074ac0929afadc6f470b7ce603ef1775c0c944cf5ad
scratch/audit_aggregate_monotone_rotor_semigroup_20260801.cpp
  e7a3bc0a678de63b2b391c792dfadbbd1ffc1f2d67ab8edb4e6d893ec8fa5986
scratch/aggregate_monotone_rotor_semigroup_20260801.audit.json
  f565dade46e6eac737cbfad9a101d145068c32250beca3d20997d26e5e73ecf7
```

## 7. Precisely closed and precisely open gates

For the canonical Ferrers/binomial demand and every `k>=31`, the **aggregate
age-profile integer decomposition** is exact: its integer vector `A` is a
sum of formal uniform short, long, and mixed age-type rotor packages with no
aggregate residue.  This does not assert that a primitive package has a
one-copy labelled lift; the independent scope audit gives an explicit
two-state mixed-rotor counterexample.

The weakest next theorem is a **named owner--target rotor cycle-cover**:

> Given aggregate packages whose type-occurrence slots total `W`, choose a
> successor permutation that may rethread different primitive packages;
> biject the slots with the `W` named middle owners; choose literal age
> partitions satisfying the owner-changing shift recurrence; and, at every
> rank, biject the marked nested flags with the prescribed residual named
> targets.

Multiple cycles are allowed.  Hamiltonicity, residence, deeper upper
shadows, and common-cap compatibility remain subsequent gates.
