# K16 H1: arbitrary-support escape duality and sharp singleton-portal boundary

Date: 2026-07-30  
Status: **proved solver-independent theorem; the coupled one-outside-edit universal subcase remains open**

## 1. Result

The outside-projection escape condition has an exact interval-hypergraph
dual for **every** retained support `A`: if source reset fails, the outside
edit set must stab one residual target's complete final-word witness family.
For a fixed final word this gives the exact lower bound

```text
|E| >= restricted witness packing number.
```

This bound cannot be made larger than one from the authenticated source
witness hypergraph and stabbing condition alone.  The source has the unique
hole

```text
H = 0x2c6d.
```

For every position `p` outside `A`, changing just `x[p]` to `H` makes the
complete `H`-witness family a star centred at `p`.  Its transversal and
packing numbers are both exactly one.  In the frozen joint13 instance all
`12,860` outside positions are such singleton portals.

This is a sharp boundary of the projection method, not a universal word:
the one-portal words used below generally lose other targets.  Therefore a
lower bound of two or more would have to use coupled universality or
collateral constraints, not witness stabbing alone.

## 2. Arbitrary retained support

Let `x=(x[0],...,x[n-1])` be a word of nonzero bit masks.  For a target `T`
write

```text
W_T(w) = { [l,r] : OR(w[l],...,w[r]) = T }.
```

Let `A` be any retained set of positions, put `P={0,...,n-1}\A`, and define

```text
pi_A(y)[i] = y[i]  for i in A,
             x[i]  for i in P,

E = { i in P : y[i] != x[i] },

R_A(x) = { T : every x-witness for T meets A }.
```

The last definition includes every source hole, because its source witness
family is empty.

For an interval family `F`, let `tau_P(F)` be the minimum number of points of
`P` meeting every member of `F`; it is infinity if a member has empty trace
on `P`.  Let `nu_P(F)` be the maximum size of a subfamily whose traces on
`P` are pairwise disjoint.

### Theorem 2.1 (exact outside-trace dual)

For every interval family whose members have nonempty trace on `P`,

```text
tau_P(F) = nu_P(F).                                      (2.1)
```

#### Proof

List the points of `P` in their natural order.  Each nonempty trace `I ∩ P`
is an interval in this ordered list.  Repeatedly take a trace with earliest
right endpoint, select that endpoint, and delete every trace containing it.
The selected points stab all traces.  The traces that caused successive
selections are pairwise disjoint, so the number selected is simultaneously
an upper bound on `tau_P` and a lower bound on `nu_P`.  The reverse inequality
`tau_P >= nu_P` is immediate.  Hence equality holds.

### Theorem 2.2 (arbitrary-support escape and packing bound)

Let `y` be universal.  If `pi_A(y)` is not universal, then some
`T in R_A(x)` satisfies

```text
E meets every member of W_T(y),                         (2.2)
```

and consequently

```text
|E| >= tau_P(W_T(y)) = nu_P(W_T(y)) >= 1.              (2.3)
```

#### Proof

Choose a target `T` missing from `pi_A(y)`.  It must lie in `R_A(x)`:
otherwise `x` has a `T`-witness disjoint from `A`, and `pi_A(y)` agrees with
`x` on that entire interval.  If a `y`-witness for `T` avoided `E`, then `y`
and `pi_A(y)` would agree on the witness, contradicting the choice of `T`.
Thus (2.2) holds.  Since `E` is a `P`-transversal, (2.3) follows from Theorem
2.1.  Universality makes `W_T(y)` nonempty.

The useful normalization form is the contrapositive.

### Corollary 2.3 (`k`-packing normalization)

If every `T in R_A(x)` has `k` final-word witnesses whose traces on `P` are
pairwise disjoint, then every universal `y` with `|E|<k` has universal
projection `pi_A(y)`.

Thus a scalable outside-edit lower bound requires a **uniform final-word
packing theorem for every residual target**.  Source witness multiplicity by
itself does not supply that theorem.

## 3. Sharp impossibility from a source hole

### Theorem 3.1 (singleton-hole portal)

Suppose `x` misses a target `H`, let `A` be any proper retained support, and
choose `p in P`.  Define

```text
z^(p)[p] = H,
z^(p)[i] = x[i]  for i != p.
```

Let `L_p` be the number of consecutive cells immediately left of `p` whose
values are submasks of `H`, and define `R_p` analogously on the right.  Then

```text
W_H(z^(p)) = { [p-a,p+b] : 0 <= a <= L_p, 0 <= b <= R_p }.    (3.1)
```

In particular,

```text
E = {p},
H in R_A(x),
tau_P(W_H(z^(p))) = nu_P(W_H(z^(p))) = 1,                (3.2)
```

and `{p}` is the unique minimum transversal.

#### Proof

The singleton `[p,p]` has OR `H`.  Any `H`-witness avoiding `p` would be an
unchanged source interval and hence an `x`-witness for the missing target
`H`, impossible.  An interval containing `p` has OR `H` exactly when every
other value in it is a submask of `H`; it can therefore extend precisely
through the two consecutive submask runs.  This proves (3.1).  Every member
contains `p`, while the singleton member forces every transversal to contain
`p`, proving (3.2).

### Corollary 3.2 (sharp logical boundary)

No conclusion `|E| >= 2` can follow solely from

```text
the authenticated source x,
an arbitrary proper retained support A,
T in R_A(x), and
E stabs every final-word T-witness.
```

Those premises have the explicit one-edit realization of Theorem 3.1.  A
stronger conclusion for universal words must use facts not present in the
local stabbing premise, such as simultaneous coverage of the other targets
or a collateral/debt invariant.

The word `z^(p)` is not asserted to be universal.  Hence this theorem does
not rule out a separate proof that universality forces `|E|>=2`; it identifies
exactly the missing ingredient such a proof must add.

## 4. Exact frozen-source census

For the authenticated word

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
n = 12,873,
```

and the joint13 support

```text
S = {0,1,4486,4487,4488,4489,6438,6439,6440,
     12869,12870,12871,12872},
```

the independent audit gives the following exact interval-hypergraph census.

1. All `82,863,501 = n(n+1)/2` source intervals are classified.  They cover
   `65,534` nonzero targets and miss only `H=0x2c6d`.
2. Intervals inside the three fixed-complement segments cover `65,480`
   targets and leave exactly the known `55` joint13 residual targets.
3. Among those residual targets, the source has `58` literal intervals:
   the occurrence-count histogram is

   ```text
   0 witnesses : 1 target  (H)
   1 witness   : 51 targets
   2 witnesses : 2 targets
   3 witnesses : 1 target.
   ```

   Every one of the `54` nonempty source families has a common point, so
   each separately has `tau=nu=1`.  Thus even deleting the hole from the
   census does not create a source residual packing bound of two.
4. The union of all `54` nonempty **source** families has transversal number
   eight, with one minimum transversal

   ```text
   {0,3,4486,4489,6438,6440,12869,12871}.
   ```

   This collective number is not an escape bound: Theorem 2.2 has the
   existential quantifier "some residual target" and concerns final-word
   witnesses, not the union of all source families.
5. Every one of the `12,860` positions outside `S` is a one-edit `H` portal.
   Across the separate words `z^(p)`, the exact cardinality distribution of
   the resulting `H`-witness stars is

   ```text
   |W_H(z^(p))|    number of p
          1          12,129
          2             621
          3              69
          4              36
          6               5.
   ```

   Cardinality varies, but all `12,860` families have the same exact dual
   value `tau_P=nu_P=1`.

   A particularly literal portal is `p=5`, where `x[5]=0x4421`: after the
   replacement `z^(5)[5]=H`, the complete hole-witness family is exactly
   `{[5,5]}`.

The complete 58-interval residual table, common cores, endpoint-state stream
digests, and portal-run census are recorded in the audit artifact.

## 5. Consequence for frozen joint13 and the open subcase

The companion guard-ladder theorem proves that every source-reset projection
onto `S` is nonuniversal.  Therefore any universal length-12,873 word `y`
must have a residual target `T` satisfying (2.2), and its outside-edit count
obeys the exact final-word bound (2.3).

The strongest source-only numerical corollary is nevertheless just

```text
|E| >= 1,
```

and it is sharp for the witness-stabbing premise.  The precise remaining
subcase is:

> Can arbitrary values on the 13 joint13 cells, together with exactly one
> arbitrary edit at an unrestricted outside position, cover all 65,535
> targets?

Nothing here settles that coupled universal problem.  No SAT result, local
radius search, or collar594 search is used or duplicated.

## 6. Reproducible audit

```text
scratch/audit_k16_h1_outside_escape_transversal_sharpness_20260730.py

scratch/k16_h1_outside_escape_transversal_sharpness_20260730.audit.json
```

Run:

```bash
python3 scratch/audit_k16_h1_outside_escape_transversal_sharpness_20260730.py \
  --output scratch/k16_h1_outside_escape_transversal_sharpness_20260730.audit.json
```

The audit is endpoint-DP enumeration with at most eleven live OR states per
right endpoint.  It is solver-free and takes linear time up to the 16-bit OR
state factor.
