# Arbitrary extreme actuator stocking and the tight mark-one identity

Date: 2026-08-01  
Lane: residual age stationarity / extension of handoff 2507RS  
Status: unconditional asymptotic marked-profile stocking theorem.  This
extends the canonical `A_(q,m)` bank of 2507RS to every full extreme profile
using the arbitrary-hole parity actuator.  It is still an age-level theorem;
stationarity of the complementary residual law and one-copy physical
Catalan planting remain separate.

## 1. Arbitrary full extreme rows

Let `A` be any `d`-mark profile containing `r-1`.  By the exact normalization
theorem, write

```text
A=([B]\H) union {r-1},
B=d+h-1,
H subseteq [B-1], |H|=h.                              (1.1)
```

Put

```text
L=H intersect [d],
U=[d+1,B]\H.
```

Then `|L|=|U|+1`.  Choose the retained low hole `m` by

```text
m=d,              if d in L;
m=1,              if d notin L and 1 in L;
m=min L,           otherwise.                         (1.2)
```

Pair `L\{m}` bijectively with `U`, and perform the mark exchanges of the
arbitrary-hole parity-sweep theorem.  Its post-exchange terminal and donor
profiles are

```text
A*=([d]\{m}) union {r-1},
Y_(a,u)=([d]\{a}) union {u}.                         (1.3)
```

The reservoir profiles are

```text
D=[d],
R_p=[d+1]\{d-p+1}.                                  (1.4)
```

## 2. Truncated parity sweeps

The published parity theorem uses the complete path

```text
D -> S_1 -> ... -> S_d -> D.
```

Only a prefix is needed.  For one used parity `epsilon`, let

```text
p_epsilon=max{d-a+1:a in L\{m}, d-a+1=epsilon mod2}.
```

Then

```text
D -> S_1^epsilon -> ... -> S_(p_epsilon)^epsilon -> D  (2.1)
```

is a legal cycle.  The internal edges are exactly those already proved in
the parity-sweep lemma.  The final edge is legal because

```text
Q(D)=(1,...,1)<=P(S_(p_epsilon)^epsilon),             (2.2)
```

all entries on the right being positive.

Together with the base terminal cycle, (2.1) uses at most

```text
3d+3                                                   (2.3)
```

full occurrence roles per input extreme row.  Removing unused suffixes of
the parity paths preserves every mark-neutrality identity because those
removed `R_p` occurrences were unchanged reservoirs on both sides.

## 3. Exact tight-column identity

### Lemma 3.1

In the complete post-regrouping stationary packet, the number of full
profiles omitting deficit `1` is exactly

```text
1[1 in H].                                             (3.1)
```

#### Proof

The base cycle omits `1` exactly when `m=1`: only its `X_m` role can do so,
because its `R_p` segment stops at `p=d-m`, and hence every omitted mark
`d-p+1` is at least `m+1>=2`.

In a parity cycle, the only role that can omit `1` has index `p=d`.  Such a
role occurs exactly when `a=1` is exchanged; it is then the donor type
`Y_(1,u)`, rather than a reservoir.  Rule (1.2) gives three cases.

1. If `1 notin H`, neither event occurs.
2. If `1 in H` and `d notin H`, choose `m=1`; the base contributes one and
   no parity cycle reaches `d`.
3. If `1,d in H`, rule (1.2) forces `m=d`; the base contributes zero and
   the exchange `a=1` makes exactly one parity cycle end at `d`.

This proves (3.1).  QED.

This identity is the essential strengthening over a coarse `O(d)` packet
bound: deficit `1` is the only potentially tight missing-slot column.

## 4. Uniform arbitrary-extreme stocking

Let `a_A` be the number of selected occurrences of every full extreme
profile `A`, and put

```text
E=sum_A a_A.
```

Every such row contains deficit `r-1`, so

```text
E<=n_(r-1)<=k.                                         (4.1)
```

Prescribe the truncated stationary packet of Sections 1--2 for every
selected occurrence.  If `M` is the number of prescribed rows, then

```text
M<=(3d+3)E<=3k(d+1)=O(k^(3/2)).                       (4.2)
```

### Theorem 4.1 (arbitrary extreme bank stocks)

For all sufficiently large `k`, all these packets can be prescribed
simultaneously inside the original `W` named marked rows, with no extra row,
while preserving every global deficit multiplicity exactly.

#### Proof

Apply the exact complete-bipartite stocking criterion of 2507RS.  Every
prescribed profile is full, so the total residual capacity cut is automatic.
Also `M=o(W)`.

The top mark `r-1` occurs once per packet, on its terminal role, hence its
requested supply is `E<=n_(r-1)`.  Every other requested mark is at most
`r-2`, and therefore has supply at least

```text
n_(r-2)>=C(k,2)-C(d+1,2)=Theta(k^2)>>M.               (4.3)
```

For the missing-slot cuts, Lemma 3.1 gives

```text
M-g_1=#{selected original extreme rows omitting 1}
     <=W-n_1,                                          (4.4)
```

because those are distinct rows of the original marked assignment.

For every `t>=2`, monotonicity gives `n_t<=n_2`, and hence

```text
W-n_t>=W-C(k,r-2)>>M.                                  (4.5)
```

Thus every individual supply and missing-slot inequality holds.  The sharp
stocking theorem has no higher-order cuts, so it supplies an integral
extension on the same `W` rows.  QED.

### Corollary 4.2

The noncanonical `k=140` profile

```text
{1,2,4,5,7,9,69}
```

is not an obstruction to age-level actuator stock.  It lies in the arbitrary
three-hole family and is covered by Theorem 4.1, even though it lies outside
the canonical `A_(q,m)` bank of 2503MH/2507RS.

## 5. Exact scope

Theorem 4.1 closes:

* arbitrary, not merely canonical, full extreme marked profiles;
* all donor and truncated-reservoir occurrence roles;
* the sole asymptotically tight missing-slot column `t=1`; and
* count-neutral marked regrouping inside the existing `W` rows.

It does not prove:

* stationary completion of the unreserved residual type law;
* integral owner-changing fusion of the stationary packets;
* upper-shadow/common-cap transparency; or
* a contiguous-OR word.

The later monotone-rotor fractional theorem closes the first item only in
the invariant fractional projection.  Integral occurrence-labelled rotor
fusion remains a separate gate.

## 6. Audit

The symbolic identities, every truncated age arc, full mark neutrality,
the `t=1` identity, and the role bound were independently replayed for
12,364 arbitrary-hole instances (`2<=d<=12`, `1<=h<=5`) on one H100-host
CPU core:

```text
scratch/audit_arbitrary_extreme_actuator_stocking_20260801.cpp
SHA256 a808f0c3fe97e84c0e43c553521790870128ac061b6a9dbcf07c0cd91f98a239

scratch/arbitrary_extreme_actuator_stocking_20260801.audit.txt
SHA256 9c614e235c83267e6b190b7d33eb15479ce9eaa0ac159170150a5d64d0cf6015
PASS_ARBITRARY_EXTREME_STOCKING cases=12364 arcs=243346
```
