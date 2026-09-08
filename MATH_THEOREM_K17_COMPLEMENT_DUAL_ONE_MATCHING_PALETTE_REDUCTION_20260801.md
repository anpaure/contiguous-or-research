# Complement-dual one-matching reduction for the k=17 immediate palettes

Date: 2026-08-01  
Status: unconditional algebraic reduction.  Existence of a matching on this
restricted face, connectedness, voltage, residence, deeper upper opening,
and lower compilation remain open.

## 1. Middle-level incidence notation

Let

```text
A=C([17],9), B=C([17],8),
```

and let `G` be their containment graph.  Complement is a shore-swapping
involution

```text
C:A <-> B.
```

It acts on incidence edges and commutes with the `Z_17` rotation quotient.

Let `M` be a perfect matching from `A` to `B`, and define its complement
dual by

```text
M^vee=C M^(-1) C.
```

Equivalently, as an undirected incidence-edge set,

```text
M^vee=C(M).
```

Assume `M` and `M^vee` are edge-disjoint.  Then

```text
F=M union M^vee
```

is a complement-invariant spanning two-factor of `G`.

## 2. Occurrencewise palette duality

For `a in A`, let its two selected rank-8 neighbours be

```text
b=M(a),
b'=M^vee(a)=C(M^(-1)(C(a))).
```

Their intersection is the native rank-7 lower colour

```text
L(a)=b intersect b'.
```

At the complementary rank-8 vertex `C(a)`, the two selected rank-9
neighbours are

```text
M^(-1)(C(a))
and
(M^vee)^(-1)(C(a))=C(M(a)).
```

Their union is the native rank-10 upper colour `U(C(a))`.  De Morgan gives

```text
C(L(a))
 = C(M(a)) union C(M^vee(a))
 = C(M(a)) union M^(-1)(C(a))
 = U(C(a)).                                             (2.1)
```

### Theorem 2.1

On every complement-dual factor `F`, complementation pairs lower and upper
turn occurrences bijectively:

```text
L(a) <-> U(C(a)).
```

Consequently rank-7 surjectivity is equivalent to rank-10 surjectivity, and
the complete multiplicity histograms are complementary copies of one
another.  This remains exact after quotienting by `Z_17` because complement
commutes with rotation.

## 3. Exact reduced search problem

The former outer master selected two unrelated perfect incidence matchings
and imposed both 1,144 rank-7 and 1,144 rank-10 orbit-cover rows.  On the
complement-dual face it is enough to select one matching `M` satisfying:

1. `M` is perfect on both quotient shores;
2. `M intersect C(M)` is empty;
3. the 1,430 upper turns of `M union C(M)` cover all 1,144 rank-10 orbits.

The rank-7 rows follow from (2.1).  The resulting exact encoding is

```text
scratch/build_k17_complement_dual_rank10_factor_20260801.cpp
```

and deliberately exports the factor-incidence variables first, so the
existing topology/voltage/residence separator can audit any SAT model.

### Proposition 3.1 (the parity split is exact)

Put `A=C D`, a permutation of the 1,430 rank-9 owner orbits.  In one
orientation the owner successor permutation of `M union M^vee` is

```text
(M^vee)^(-1) M = C D C D = A^2.                       (3.1)
```

Since 1,430 is even, `A^2` cannot be a single 1,430-cycle.  Therefore a
strictly complement-dual quotient Hamilton cycle is impossible.

This is useful rather than fatal: if `A` is one 1,430-cycle, then `A^2`
has exactly two cycles.  The natural target is consequently a
palette-exact complement-dual **two-factor**, followed by one certified
non-dual alternating switch joining its two cycles.  This is the same
topological pattern that produced the k=13 optimum.

### Proposition 3.2 (odd-graph Hamilton normal form)

The same permutation `A=C D` gives an even smaller description.  Incidence
`D(a) subset a` is equivalent to

```text
C(A(a)) subset a,
```

and, since both `a` and `A(a)` have rank 9 in a 17-set, this is equivalent
to

```text
|a intersect A(a)|=1.                                  (3.2)
```

Conversely any permutation `A` of the rank-9 necklace orbits satisfying
(3.2) determines the perfect matching `D=C A`.  Thus `A` is a cycle cover
in the `Z_17` quotient of the odd graph `KG(17,8)` (written on complementary
rank-9 vertices).

If `A` is a simple cycle, write

```text
A^(-1)(a)=C(a) union {p(a)},
A(a)     =C(a) union {n(a)}.
```

The two labels are distinct away from a two-cycle, and the upper turn at
the complementary facet is exactly

```text
U(C(a))=A^(-1)(a) union A(a)
       =C(a) union {p(a),n(a)}.                        (3.3)
```

Its complementary lower colour is

```text
a minus {p(a),n(a)}.
```

Therefore the reduced search is a turn-surjective Hamilton cycle problem
in a 9-regular 1,430-vertex odd-graph quotient: the unordered pair of edge
labels at each vertex must cover all 1,144 rank-7/rank-10 necklace colours.
The 286 surplus turns are the complete immediate-palette splice budget.

## 4. Scope

This theorem does not assert that the complement-dual face is nonempty
after the rank-10 rows.  It is a sufficient, potentially restrictive lane.
It also cannot be connected before one breaks duality, by Proposition 3.1.
If SAT, it removes one entire palette coupling exactly and reduces topology
to a controlled splice problem.  If UNSAT with a checked proof, it excludes
only the complement-dual face and does not refute the unrestricted k=17
optimum.
