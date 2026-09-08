# Generalized Pascal braids reduce to one exact 0--1 system

Date: 2026-07-29

Status: theorem and exact finite model.  The theorem is proved below.  The
first `k=15` implementation is

```text
scratch/solve_k15_generalized_pascal_braid.py
```

No new word-length upper bound is claimed here.

## 1. Setup

Let `n=2m`, distinguish a new coordinate `z`, and split the middle layer of
`[n]+z` into

```text
A = {z}+C([n],m),                 B = C([n],m+1).
```

Fix a Hamilton path

```text
P = (T_0,...,T_{W-1}),            W=C(2m,m),
```

in `J(2m,m)` whose adjacent intersections cover every `(m-1)`-set.  This is
the property already possessed by the audited `k=14` carrier.

For each edge `e=T_iT_{i+1}` of `P`, introduce a Boolean `x_e`.  For each
containment `T subset U`, `|T|=m`, `|U|=m+1`, introduce a cross Boolean
`z_{T,U}`.  Finally, for every Johnson edge `U_1U_2` in `J(2m,m+1)`, put

```text
T = U_1 intersection U_2,         V = U_1 union U_2
```

and introduce a Boolean `y_{T;U_1,U_2}`.

Write

```text
d_A(T) = sum{x_e : e incident with T in P}.
```

## 2. Exact equations

The generalized braid system is

### The `AA` lower rainbow

For every `X in C([n],m-1)`,

```text
sum{x_e : intersection(e)=X} = 1.                         (2.1)
```

### Degree two on `A`

For every `T in C([n],m)`,

```text
d_A(T) + sum_{U superset T} z_{T,U} = 2.                 (2.2)
```

### The no-`z` lower rainbow

For every `T in C([n],m)`,

```text
sum_{U superset T} z_{T,U}
 + sum_{U_1 intersection U_2=T} y_{T;U_1,U_2} = 1.       (2.3)
```

### Degree two on `B`

For every `U in C([n],m+1)`,

```text
sum_{T subset U} z_{T,U}
 + sum_{U' adjacent U} y_{U intersection U';U,U'} = 2.   (2.4)
```

### The two upper covers

For every `U in C([n],m+1)`,

```text
sum{x_e : union(e)=U} + sum_{T subset U} z_{T,U} >= 1,   (2.5)
```

and for every `V in C([n],m+2)`,

```text
sum{y_{T;U_1,U_2} : U_1 union U_2=V} >= 1.              (2.6)
```

All variables are Boolean.

## 3. Two-sector braid theorem

**Theorem.**  Every solution of (2.1)--(2.6) defines a 2-factor on the full
middle layer of `[2m+1]` with

1. every colour in `z+C([2m],m-1)` occurring exactly once;
2. every colour in `C([2m],m)` occurring exactly once;
3. every colour in `z+C([2m],m+1)` covered;
4. every colour in `C([2m],m+2)` covered.

The first two families are together exactly all rank-`m` lower-q1 targets;
the last two are together exactly all rank-`m+2` upper-q1 targets of the odd
problem.

### Proof

Use selected `x` edges between the corresponding `A` vertices, selected
`y` edges between `B` vertices, and selected `z` edges between `A` and `B`.
Equation (2.2) gives degree two at every `A` vertex and (2.4) gives degree
two at every `B` vertex, so the result is a 2-factor on the full middle
deck.

An `AA` edge has lower colour `z + intersection(e)`.  Equation (2.1)
therefore gives every `z`-containing lower target exactly once.

A cross edge from `z+T` to `U` has lower colour `T`.  A `BB` edge
`U_1U_2` has lower colour `U_1 intersection U_2=T`.  Equation (2.3) says
that these two sources jointly give every lower target not containing `z`
exactly once.

An `AA` edge of union `U` and a cross edge ending at `U` both have upper
colour `z+U`; hence (2.5) is precisely the `z`-containing upper cover.
A `BB` edge has upper colour `U_1 union U_2`, so (2.6) is precisely the
upper cover not containing `z`.  QED.

## 4. Counts and path structure are automatic

Combining (2.2) and (2.3) gives

```text
sum y with lower T = d_A(T)-1.
```

Thus `d_A(T)` is automatically `1` or `2`: the selected `AA` graph has no
isolated vertices and is a path forest inside `P`.  Equation (2.1) selects

```text
C(2m,m-1)=C(2m,m+1)
```

edges, so its number of path components is

```text
C(2m,m)-C(2m,m+1)=Cat(m).
```

Consequently the selected cross count and `BB` count are forced:

```text
cross = 2 Cat(m),
BB    = C(2m,m+1)-Cat(m).
```

This recovers the exact sector census observed in the solved `k=13`
certificate without imposing any strict forward/reverse Pascal blocks.

## 5. Residence

The runs of the distinguished coordinate `z` are exactly the components of
the selected `AA` path forest.  Hence depth-`d` residence for `z` is the
local condition

```text
every selected AA component has at least d+1 vertices.    (5.1)
```

On a fixed path this is encoded by forbidding two cuts at distance at most
`d`, including the two virtual cuts immediately before the first and after
the last path vertex.  Residence of the old coordinates depends on the `BB`
and cross braiding and remains an additional, auditable condition.

## 6. The k=15 instance

For `m=7`, the exact sizes are

```text
A vertices       3432
B vertices       3003
AA edges          3003
cross edges        858
BB edges          2574
```

The implementation has about 100,000 Boolean variables:

```text
x:   3431 path-edge choices,
z:  24024 containment choices,
y:  72072 BB-edge choices.
```

The selected-edge census is `AA=3003`, `cross=858`, and `BB=2574`; the
available Boolean-variable counts are the `x,z,y` counts displayed above.

The first diagnostic run on the current best `k=14` path established:

```text
lower-rainbow degree-two system: SAT in 12.2 seconds,
z-upper channel added:           SAT in 11.3 seconds,
hard z-residence >=4:            UNSAT in presolve.
```

The last line is scoped to this fixed `k=14` path.  It proves that its
forced lower-colour occurrences create at least one short `AA` component;
it is not an obstruction to the generalized braid theorem.  It tells the
search exactly what must change in the even carrier: lower-rainbow edge
selection and residence must be optimized jointly, while the 858 cross
edges retain the shadow-repair freedom visible at `k=13`.

An exact optimization of the same fixed-path lower/degree system sharpens
this completely:

```text
minimum short AA components = 17,
length-2 components         = 13,
length-3 components         = 4,
solver status               = OPTIMAL, best bound 17,
wall time                   = 62.6 seconds.
```

Thus one exact optimum has 17 explicit local motifs, and every solution of
the fixed-path lower/degree model has at least 17 short components.  Their
locations are not proved individually forced.  The former common-colour
deficiency 85 was measuring an unnecessary condition.

Independently, maximizing the hard no-`z` upper channel under all lower and
degree equations reaches the full target:

```text
distinct BB upper colours = 2002 / 2002,
status                    = OPTIMAL,
wall time                  = 82.0 seconds.
```

The `BB` upper cover is therefore feasible on this fixed path.  A subsequent
seeded optimization closes the simultaneous interaction completely:

```text
exact lower decks              yes,
z-containing upper deck        3003 / 3003,
no-z upper deck                2002 / 2002,
middle ownership / degree two  exact,
factor components              9,
wall time                      61.6 seconds.
```

The retained factor is

```text
scratch/k15_generalized_pascal_braid/full_q1_s15105.json
```

with SHA-256 `e8092469c88b0a224bf0b11ed2661e06b5de260cc349717ea704732f47e00f29`.
It has 1,527 depth-three residence defects, 97 involving the distinguished
coordinate, and generic-strength deeper holes.  Thus all q1 compatibility
inside the generalized braid is solved; chronology/residence and the
protected deeper/compiler windows are the remaining fixed-path gates.

### Projection of the verified H19 carrier

The existing compiler-best `k=15` path is already an almost exact
generalized braid when distinguished at coordinate 14.  A solver-free audit
gives

```text
AA=3004, cross=856, BB=2574,
AA lower: 3003/3003, one duplicated label,
BB upper: 2002/2002,
BB lower: 2573 distinct, one duplicated label,
cross lower: 856 distinct, one label overlapping BB,
non-AA lower holes: 5801, 7267, 8877, 13620.
```

The AA duplicate is old-coordinate label `756`, on path edges `2582` and
`5917`.  The BB duplicate is label `12685`, on edges `840` and `5046`; the
cross/BB overlap is `3868`.  The four holes are also prominent masks in the
exact compiler residual: three of them, `5801,7267,13620`, occur in its
21-mask optimum residual, while `8877` is compiled elsewhere.  Thus the braid
defect and the compiler defect are partly the same physical support, not
independent losses.

The reproducer is

```text
scratch/audit_k15_h19_generalized_braid_projection.py
```

and its machine-readable output is

```text
scratch/k15_h19_generalized_braid_projection.audit.json.
```

All 23 undirected standard Johnson 2-opt reconnections touching one of the
four duplicate-sector edges (25 directed target hits) were checked.  None
reduces the four lower holes;
the only residence- and upper-preserving move merely swaps the two duplicate
BB occurrences.  Any repair of this exact support therefore needs at least
a three-edge/three-seam move in the standard path neighbourhood.

## 7. Significance

The earlier strict common-colour target required all selected `AA` unions
to be distinct.  The solved `k=13` factor violates that target by 147 yet is
optimal.  Equations (2.5)--(2.6) retain precisely the missing freedom: cross
edges repair the `AA` union holes.  Therefore the previous `2918/3003`
common-colour score at `k=14` is not an 85-unit barrier.  The correct finite
target is the exact linear system above, followed by residence, deeper
shadow, and compiler audits.
