# Independent audit of aggregate rotor semigroup and buffer rounding

Date: 2026-08-01  
Lane: R, integral sequel to monotone-rotor fractional circulation  
Verdict: **PASS after two theorem-scope corrections and one explicit
threshold completion**

Audited corrected theorem:

```text
MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md
SHA-256 ad4cdb5b604c3bdd1df6a074ac0929afadc6f470b7ce603ef1775c0c944cf5ad
```

The semigroup equations and two-buffer conductor are correct.  The canonical
Ferrers/binomial age-signature vector clears the conductor for every
`k>=31`.  What is integral is exactly the age-type/signature quotient; a
primitive package need not have a one-copy labelled lift.

## 1. Generator and resource audit

For `0<=a<d<b<r`, the nontrivial generator is

```text
g_(a,b)=q_(a,b)e_a+p_(a,b)e_b,
q_(a,b)=C(b-a-1,d-a),
p_(a,b)=C(b-a-1,d-a-1).
```

Putting `u_a=d-a` and `v_b=b-d`, direct cancellation gives

```text
u_a q_(a,b)=v_b p_(a,b).
```

The two unit-buffer identities are exactly

```text
g_(d-1,b)=(b-d)e_(d-1)+e_b,
g_(a,d+1)=e_a+(d-a)e_(d+1).
```

Consequently equations (1.2) of the theorem are necessary and sufficient
for membership in the formal rotor-generator semigroup.  For a vector from
`W M_(r,d)`, the resource inequality `L>=H` follows from

```text
L-H=dW-sum_ell ell A_ell>=0.
```

The corrected standalone conductor theorem states this hypothesis
explicitly.

## 2. Two-buffer conductor audit

After deleting coordinates `d-1,d+1`, balanced resource totals obey

```text
Y_0=H^circ-A_(d-1)=L^circ-A_(d+1).
```

If `Y_0>0`, route `Y_0+Q^circ` fractionally on the complete internal
bipartite graph and round every edge multiplicity down.  The total resource
lost is strictly below `Q^circ`, so the retained internal resource `Y'`
satisfies `Y'>=Y_0`.  The residual nonbuffer low and high occurrences consume
respectively

```text
L^circ-Y',       H^circ-Y'
```

units from the opposite buffers.  Both buffer remainders equal `Y'-Y_0`
and are closed by `g_(d-1,d+1)`.  For `Y_0<=0`, the same calculation holds
with `Y'=0`.

The one-buffer proof is also exact: scalar slack `E>=Q` leaves at least `Q`
low-buffer resource before rounding, and the additional loss is strictly
below `Q`.  Finally, every `0<=E<Q` is removed with low resources `1,2,3`
as displayed in (4.2), after which the balanced lemma applies.  No parity or
floor residue remains.

## 3. Exact `k>=31` threshold

The original finite artifact alone checked only a bounded interval, while
the original prose gave an unspecified asymptotic threshold.  The corrected
theorem closes that gap.

Hockey-stick summation gives

```text
Q_(r,d)=sum_(u=2)^d u C(r-d+u-1,u+1).
```

Standard central-binomial bounds give `d<=ceil(sqrt(r))`.  For `r>=64`,
they also give `d>=4` and `r>2d+2`, so the Ferrers boundary does not touch
the four required buffers.  For

```text
ell in {d-3,d-2,d-1,d+1},
```

the adjacent-central product is at least `exp(-25/11)>1/16`, whence

```text
A_ell>=W/(16r)>=2^(2r-6)/r^(3/2).
```

Meanwhile `Q<r^2 2^(r-1)`.  Since
`2^(r-5)>r^(7/2)` at `r=64` and the ratio increases, every required buffer
is at least `Q+1` for all `r>=64`.

The finite part was independently replayed on H100 with `-O3`, a 256 MiB
virtual-memory cap, and a 30-second timeout.  The hardened checker now makes
the threshold part of its exit condition rather than merely printing it.
It reports

```text
first pass: 23;
later failures: 24,26,28,30;
last failure: 30;
all_from_k31: true;
threshold_asserted: true.
```

Thus the exact scan covers `31<=k<=126`, while the symbolic tail begins at
`k=127`.  The archived replay continues through `k=1000`.  “First pass 23”
is not a monotone threshold, and a conductor-criterion failure is not a
proof of semigroup nonmembership.

```text
scratch/audit_aggregate_monotone_rotor_semigroup_20260801.cpp
  SHA-256 e7a3bc0a678de63b2b391c792dfadbbd1ffc1f2d67ab8edb4e6d893ec8fa5986
scratch/aggregate_monotone_rotor_semigroup_20260801.audit.json
  SHA-256 f565dade46e6eac737cbfad9a101d145068c32250beca3d20997d26e5e73ecf7
```

## 4. Exact integral scope and primitive obstruction

For every `k>=31`, the theorem proves:

> The canonical residual rank-count vector is an exact nonnegative integer
> sum of short, long, and mixed **age-type/signature** rotor generators,
> of total type-occurrence mass `W`, with zero residue in every rank-count
> coordinate.

It does not yet prove a labelled multicover of mass `W`.  At
`(r,d,a,b)=(4,2,1,3)`, the primitive mixed generator `e_1+e_3` has type
cycle

```text
(1,2,1) <-> (2,1,1).
```

A same-owner two-state labelled lift would force `C'_1=C_0` on the first
arc and `C_2=C'_1` on the return, contradicting disjointness of the nonempty
cells `C_0,C_2`.  Hence denominator clearing may realize `mA` without
realizing `A` itself.

## 5. Weakest remaining named theorem

The first open gate is the following **Named Rotor Flag-Colouring theorem
(NRFC)**.

Choose one aggregate type template `(U,c,J)`, `|U|=W`, supplied by the
semigroup theorem.  One must find:

1. a successor permutation `tau` of `U`, allowed to rethread different
   primitive packages;
2. a bijection `u -> T_u` from `U` to all `r`-subsets of `[k]`;
3. ordered age partitions `T_u=C_(u,0) dotunion ... dotunion C_(u,d)` of the
   prescribed types, with nonempty source letters `B_u=C_(u,0)` and literal
   recurrence

   ```text
   C_(tau(u),i+1)=C_(u,i)-B_(tau(u))       (0<=i<d);
   ```

4. for every rank `s`, a bijection from the marked nested prefixes
   `C_(u,0) union ... union C_(u,j-1)` of rank `s` to the prescribed residual
   named rank-`s` targets.

Multiple successor cycles are allowed.  Requiring one cycle is stronger.
Ore--Ryser completion, residence, upper/deep witnesses, and common-cap
compatibility are subsequent gates and are not implied by NRFC.

Therefore the invariant integer residue is closed only in the aggregate
age-signature quotient.  The exact next obstruction is simultaneous
one-copy labelled lifting plus named-owner/nested-target colouring, not
another scalar conductor.
