# Product-SCD completion around a balanced subcube reserve

Date: 2026-07-31  
Status: exact all-`m` child-compatible outer matching and one-middle-role
transversal; finite audit through `m=8`; the opposite middle role and
physical forest remain open

## 0. Verdict

The balanced subcube reserve has an exact integral compatibility property
which is stronger than its uniform fractional weighting.

Fix `2a` collar coordinates, an `a`-set `A` in the collar, and let the
remaining ground set have size `2(m-a)`.  There is an ambient symmetric
chain decomposition of `B_(2m)` which contains the entire subcube

```text
                         A + B_(2(m-a))
```

as a literal union of chains.  Its central flags consequently have the
following properties.

1. The reserve lower and upper resources are matched internally.
2. The nonreserve lower and upper resources are matched perfectly to one
   another.
3. The on-chain middle owner of every nonreserve flag is distinct and lies
   outside the reserve middle layer.

Thus the complement already has an **integral three-resource
transversal**: lower, upper and one oriented middle role are solved exactly.
For this supplied matching the only missing ordered-four-transversal rows
are injectivity/avoidance of the opposite middle corners and acyclicity of
the resulting physical graph.

This does not prove Catalan Linear Matching.  The opposite-corner map of a
canonical product SCD can have large fibres away from the collar, so the
remaining condition is still global.  What is removed is a separate outer
Hall obstruction and a separate owner-resource obstruction around the
recursive reserve.

## 1. A product-of-chains lemma

Write a finite chain of length `p` as

```text
                         c_0 < c_1 < ... < c_p
```

and one of length `q` as `d_0<...<d_q`.  Assume `p<=q`.  Their product
grid has the following symmetric-chain decomposition, indexed by
`h=0,...,p`:

```text
(c_h,d_0),...,(c_h,d_(q-h)),
(c_(h+1),d_(q-h)),...,(c_p,d_(q-h)).                 (1.1)
```

The chain in (1.1) begins in relative rank `h` and ends in relative rank
`p+q-h`.  The chains partition the grid: a cell `(c_i,d_j)` lies on the
horizontal part with `h=i` when `j<=q-i`, and otherwise on the vertical
part with `h=q-j`.  Hence the product of two symmetric chains has an SCD.
Applying (1.1) box by box proves the standard fact that the Cartesian
product of two SCDs has an SCD.

If the input lengths satisfy `p>q`, interchange the two factor chains
before applying (1.1), then restore their original coordinate blocks in
each output cell.  This is a literal symmetry of the product grid; no rank
or endpoint formula changes.  The audit implements this swap explicitly.

There is one useful rigidity in (1.1).  If the first factor is a singleton
chain, its product with `d_0<...<d_q` is that same chain with the singleton
coordinate adjoined; it is not mixed with another box.

## 2. Prescribing the balanced singleton

Let the collar ground set `C` have size `2a`, and fix
`A in binom(C,a)`.

### Lemma 2.1

`B_C` has an SCD in which `{A}` is a singleton chain.

### Proof

Every SCD of `B_(2a)` has

```text
                         Cat_a > 0
```

middle singleton chains.  The coordinate-permutation group is transitive
on `binom(C,a)`.  Apply a coordinate permutation carrying any singleton
middle member to `A`.  `square`

Choose such a collar SCD `S_C`, and choose an arbitrary SCD `S_R` of the
core cube on `R`, where `|R|=2(m-a)`.  Apply the box decomposition (1.1)
to `S_C x S_R`; call the resulting ambient decomposition `S`.

### Theorem 2.2 (literal child sub-SCD)

The chains of `S` lying in `A+B_R` are exactly

```text
                         { A+D : D in S_R }.          (2.1)
```

In particular, they form an SCD of the balanced child subcube and no other
ambient chain meets that subcube.

### Proof

Equation (2.1) is the product of the singleton collar chain `{A}` with
each core chain, so the final observation of Section 1 applies.  Every
other product box uses a collar chain disjoint from `{A}` and therefore
contains no set whose collar trace is `A`.  `square`

## 3. Central flags and exact outer completion

Every nontrivial ambient chain meeting rank `m-1` has a unique central
segment

```text
                           L < T < U,                 (3.1)
```

of ranks `m-1,m,m+1`.  Its opposite middle corner is

```text
                           H=L union (U-T).           (3.2)
```

As usual, the flags `(L,U)` over all positive-radius chains form a perfect
matching between the complete lower and upper ranks, while the on-chain
owners `T` are pairwise distinct.

Define the reserve resource classes

```text
L_A = A + binom(R,m-a-1),
X_A = A + binom(R,m-a),
U_A = A + binom(R,m-a+1).                              (3.3)
```

### Theorem 3.1 (child-compatible three-resource transversal)

For the product SCD `S` above:

1. exactly the flags with `L in L_A` have `U in U_A`, and those flags are
   the central flags of the child SCD (2.1);
2. deleting those flags leaves a perfect matching between
   `binom([2m],m-1)-L_A` and `binom([2m],m+1)-U_A`;
3. the on-chain owners `T` of the remaining flags are pairwise distinct
   and avoid `X_A`.

### Proof

By Theorem 2.2, every child lower and upper resource lies on a child chain,
and its central flag stays entirely inside the child.  Conversely, every
chain outside (2.1) has collar trace different from `A` at every one of its
vertices.  Hence a nonchild flag has nonchild lower, middle owner and upper
resources.

An SCD uses every lower and upper resource in exactly one positive-radius
chain, so all central flags are a perfect lower--upper matching.  Removing
the internally matched child flags leaves a perfect matching of the two
complements.  Distinct chains have distinct middle members, proving the
owner assertion.  `square`

Equivalently, orient every flag from its on-chain owner `T` toward its
opposite corner `H`.  The nonreserve portion already satisfies:

```text
lower bijection, upper bijection, injective nonreserve tails.            (3.4)
```

For this fixed product state, Catalan Linear Matching reduces exactly to:

```text
the opposite heads are injective and avoid the occupied child head bank,
and the directed graph T -> H is acyclic.                               (3.5)
```

Changing the central owner of a flag reverses its arc but does not change
its two physical endpoints.  Therefore rerooting alone cannot repair a
physical degree greater than two; (3.5) generally requires changing flags,
not merely orientations.

## 4. Exact scope

The theorem proves more than outer fractional capacity but less than the
balanced-subcube collar theorem.

```text
child exact problem
  + integral complement outer matching
  + injective complement owner role                       proved here;

opposite-role injection
  + child/opposite-role separation
  + physical acyclicity                                   still open.
```

In particular, the canonical BTK choice is not a hidden solution: its
opposite-corner map has maximum fibre `m` in the audited examples.  The
point of Theorem 3.1 is that any future collar braid may freeze the child,
all outer colours and one middle role from the outset.  It need not solve
outer Hall and four-resource correlation simultaneously from scratch.

## 5. Audit

The independent script

```text
scratch/audit_catalan_balanced_subcube_product_scd_20260731.py
```

constructs Greene--Kleitman SCDs, moves a collar singleton to the prescribed
balanced set, applies the explicit grid decomposition (1.1), and checks all
central resources for every `m=3,...,8` and `1<=a<=min(3,m-1)`.

All seventeen cases pass.  The audit verifies the literal child sub-SCD,
the lower and upper bijections, injectivity and reserve-avoidance of every
nonchild on-chain owner, and explicitly records the still-colliding
opposite-corner fibres.  Its payload is

```text
scratch/catalan_balanced_subcube_product_scd_20260731.audit.json
```

with payload SHA-256

```text
8f16b8acb1f28f89c299ffbb1ca6b32788b7a333c317e0c999e6257947ed8db1.
```
