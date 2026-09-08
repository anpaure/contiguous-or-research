# The q4 k17 fixed-lower mixed-C4 projection has full rank only after symmetry breaking, and L3 preservation is an exact lift-kernel gate

**Date:** 2026-08-14

**Status:** exact symbolic classification plus a finite H100 theorem for the
70 fixed rank-eight bracelets.  The unrestricted fixed projection has full
binary rank, but the frozen 54-deficit vector is outside the fixed-to-fixed
unit-current span.  The note gives the exact factor-dependent integer kernel
which must be checked to preserve the rank-seven `L^(3)` ledger.  It does
not assert occurrence, disjoint packing, or feasibility of that kernel.

## 0. Outcome

A mixed Johnson `C4` on rank-nine owners has immediate-lower unit current

```text
                             e_A-e_B,                         (0.1)
```

where `A,B` are adjacent rank-eight sets.  Reduce rank-eight sets by
translation and project `(0.1)` modulo two onto the 70 reflection-fixed
bracelets.  There are only three nonzero cases:

```text
A,B fixed:          e_[A]+e_[B],
exactly A fixed:    e_[A],
neither fixed:      0.                                      (0.2)
```

The fixed-to-fixed transfer graph is unexpectedly sparse:

```text
                    two C16 components + 38 isolated vertices.          (0.3)
```

It has 32 nonloop edges and binary incidence rank 30.  In contrast, every
fixed bracelet has a fixed-to-nonfixed neighbor, so the singleton columns
in the second line of `(0.2)` give full rank 70.  Full fixed rank is
therefore exactly a **symmetry-breaking** phenomenon.

For the frozen quotient-self catalogue, sixteen fixed lower bracelets are
already made odd and 54 remain deficient.  Thirty of those 54 are isolated
in `(0.3)`.  Consequently:

> **Theorem 0.1 (sharp fixed-projection cut).**  Fixed-to-fixed mixed unit
> currents cannot span the frozen 54-deficit vector.  If arbitrary unpaired
> fixed-to-nonfixed unit currents are admitted, the vector is in the fixed
> projection span.  The minimum number of unit currents needed to realize
> that projection alone is exactly 46.

The word "projection" is essential.  The singleton moves may leave a
nonfixed lower current, and occurrence in a selected owner factor is not
automatic.

Preserving the rank-seven age ledger is a second, independent linear gate.
For a selected owner factor `F`, every occurrence-level `C4` has a literal
rank-eight current `b_j` and a literal rank-seven current `c_j`.  The exact
necessary ledger system is

```text
                    sum_j x_j b_j = required lower-q1 current,
                    sum_j x_j c_j = 0.                         (0.4)
```

Equivalently, non-literal pure-rail lift choices give finite ticket-
signature columns `(Delta_8,Delta_7)`.  The unresolved span is the fixed
projection of the **integer kernel of `Delta_7`**, not the unrestricted
rank-70 space in `(0.2)`.

## 1. Fixed rank-eight bracelets and unit-current graph

Every reflection-fixed rank-eight translation necklace has a unique
centred representative

```text
                            (+-S),       S in binom([8],4).      (1.1)
```

It omits zero, so there are `binom(8,4)=70` bracelets.  Join two bracelets
when some physical translates are adjacent in `J(17,8)`.  A loop means two
adjacent physical sets lie in the same translation orbit and has zero
current in the quotient, so loops are recorded but removed from the action
graph.

The exact census is

```text
nonloop fixed--fixed edges                              32
fixed quotient loops                                     8
nonloop component sizes                         16,16,1^38
fixed--fixed binary incidence rank                       30. (1.2)
```

Normalize a vertex further by its four selected reflection-pair IDs.  The
32 nonloop edges split evenly according to intersection size:

```text
                   |S intersect T| = 0,1,2,3:  eight each.      (1.3)
```

Thus these are not merely the distance-one or distance-two edges from the
earlier fixed-owner catalogues.

For each fixed bracelet, count distinct nonfixed quotient neighbors.  The
degree histogram is

```text
                    8 at degree52,
                   24 at degree66,
                   38 at degree72.                              (1.4)
```

In particular every basis vector `e_[A]` occurs as the fixed projection of
some abstract mixed unit current.  Conversely, `(0.2)` lists every possible
projection of a unit current, proving the rank assertions.

Every quotient adjacency used here has an ambient mixed-C4 normal form.
If `A=K+a` and `B=K+b`, with `|K|=7`, choose distinct
`p,c` outside `K+a+b`.  The four owners

```text
                 K+p+a, K+p+c, K+p+b, K+a+b                 (1.5)
```

give lower current `e_A-e_B`.  There are ample choices on the 17-point
ground.  This is an abstract occurrence statement in the complete Johnson
graph, not a claim that the needed old edges lie in a selected factor.

## 2. The frozen 54-vector and the exact number 46

Take the sixteen fixed-lower vertices in the eight-edge quotient-self
catalogue as covered and let `d` be one on each of the other 54 vertices.
The component profile of `(0.3)` is

```text
38 isolates: 30 deficient, 8 covered;
first C16:    12 deficient, 4 covered;
second C16:   12 deficient, 4 covered.                         (2.1)
```

An isolate carrying `d=1` forces one singleton fixed-to-nonfixed action,
already costing 30 moves.  On a 16-cycle, selecting a fixed-to-fixed edge
costs one and toggles its two endpoints; any remaining target bit costs one
singleton action.  Exhausting the `2^16` edge subsets gives minimum cost
eight on each cycle.  Literal minimizing edge/singleton words are frozen in
the H100 output.  Hence

```text
                               30+8+8=46.                       (2.2)
```

This proves Theorem 0.1.  It strengthens the coarse `54/2=27` bound for
this specific unit-current projection.  It is neither a construction of a
full lower ledger nor a packing of 46 physical switches.

There is also an immediate reflection boundary.  Pair a unit current with
its literal reflection.  Every fixed endpoint then occurs twice, so its
fixed projection is zero modulo two.  Therefore the rank-70 singleton
columns cannot arise from literal reflected switch pairs.  At least one
genuinely unpaired/non-literal lift choice is necessary, consistently with
the frozen global-reflection lower-parity obstruction.

## 3. Exact L3 current of an owner-zero C4

Let the two cut edges be `a--b` and `c--d`.  Denote the retained neighbor
of `a,b,c,d` on its old path by `a0,b0,c0,d0`, respectively, and reconnect
as `a--d` and `c--b`.  The immediate-lower current is

```text
 (a intersect d) + (c intersect b)
 -(a intersect b) - (c intersect d).                         (3.1)
```

The exact rank-seven three-owner-intersection current is

```text
 +(a0 intersect a intersect d)
 +(a intersect d intersect d0)
 +(c0 intersect c intersect b)
 +(c intersect b intersect b0)
 -(a0 intersect a intersect b)
 -(a intersect b intersect b0)
 -(c0 intersect c intersect d)
 -(c intersect d intersect d0).                              (3.2)
```

Repeated terms cancel as occurrence counters.  Formula `(3.2)` shows why
`L^(3)` compatibility is not a property of the four active owners alone:
it depends on the four flanking owners in the selected factor.

For a fixed factor `F`, let `J(F)` be the finite catalogue of legal mixed
`C4` occurrences, including the chosen reconnecting orientation.  Let

```text
B_8 = matrix whose column j is (3.1) on rank-eight orbits,
C_7 = matrix whose column j is (3.2) on rank-seven orbits.     (3.3)
```

Then the exact lattice of fixed-bracelet actions available without changing
the aggregate `L^(3)` ledger is

```text
 Lambda_F = { pi_fixed(B_8 x) mod 2 :
              x integer, C_7 x=0 }.                           (3.4)
```

The first factor-dependent proof obligation is precisely

```text
                               d in Lambda_F.                  (3.5)
```

Binary selection, edge disjointness, chronology, simplicity, and conformal
ordering make the eventual switch problem stronger than `(3.5)`.  Failure
of `(3.5)` is nevertheless an exact linear obstruction; success removes
the fixed-parity/L3 lattice gate but is not yet a switch packing theorem.

## 4. Non-literal pure-rail lift menu

There is a cleaner way to build the same kernel before choosing switches.
For a quotient-simple rail witness `w`, write

```text
E(w)       its oriented ten-owner quotient deck,
l_8(w)     its ten immediate-lower orbit occurrences,
l_7(w)     its ten L^(3) orbit occurrences.                   (4.1)
```

Suppose `u,v` have exactly the same oriented owner deck `E`.  Then the two
developed rails

```text
                                  u + reflection(v)             (4.2)
```

cover both orientations of every reduced owner row in `E` exactly once.
Thus `(4.2)` is an owner-exact replacement for the literal pair
`u+reflection(u)`.  Its ticket difference is

```text
Delta_8(u,v) = reflection(l_8(v)-l_8(u)),
Delta_7(u,v) = reflection(l_7(v)-l_7(u)).             (4.3)
```

On fixed rank-eight bracelets, reflection acts trivially, so the parity
action of `(4.3)` is simply the fixed projection of
`l_8(v)-l_8(u)`.  Off-diagonal pairs `u!=v` are exactly the non-literal
symmetry-breaking menu missing from a literal reflected-pair master.

Equality of the reduced ten-row mask alone is not sufficient for `(4.2)`:
the two witnesses must choose the same orientation in every nonfixed owner
pair, equivalently `E(u)=E(v)`.  This is the exact orientation condition
that the targeted owner generator must retain when forming lift fibres.

For a selected owner-cover scaffold, enumerate each oriented fibre

```text
                    W(E)={w:E(w)=E}                             (4.4)
```

and deduplicate its ordered-pair options by `(Delta_8,Delta_7)`.  Choosing
one option per selected reflected owner pair gives a finite multiple-choice
integer system.  In difference form its sharp linear gate is

```text
       sum Delta_8 = required lower-q1 current,
       sum Delta_7 = 0,                                       (4.5)
```

with the fixed parity condition `(3.5)` as its mod-two projection.  To
couple the canonical rank-seven schedule simultaneously, decorate an option
by its rail phase and replace the second row of `(4.5)` by the already
frozen equations

```text
             L3_load(A)-unmarked_phase(A)=1,
             L3_load(A)<=2                  for every A.       (4.6)
```

This is the exact reduced master interface after an owner-only cover.  It
separates the finite data still missing from the proved algebra: the current
targeted generator retains only one witness per reduced mask, whereas
`(4.4)` requires all distinct `(orientation,Delta_8,Delta_7)` signatures.

## 5. H100 verification and scope

The verifier reconstructs all 1,430 rank-eight translation orbits, all 70
fixed bracelets, every quotient Johnson neighbor, the complete graph
`(0.3)`, and the frozen sixteen/54 split from the independent quotient-self
catalogue.  It computes both binary ranks by the graphic/singleton
classification and exhausts the two `2^16` projected minimizations.

```text
scratch/verify_q4_k17_fixed_lower_mixed_c4_projection_and_lift_kernel_20260814.py
sha256 d94555683993c0bae82210a6494ca63162c5445d7afd5f21389226ff4fa56d2a

scratch/verify_q4_k17_fixed_lower_mixed_c4_projection_and_lift_kernel_20260814.h100.out
sha256 ec428eb3e86c084711dfa4a3638a171899e6e83e9dc0a34746fd8478333a0d07

frozen quotient-self catalogue output used for the 16/54 split
scratch/audit_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out
sha256 324bf271234eefede36081908c38e73e72272925e2a6b4df656cae1189fc5426
```

The exact output reports `PASS`, fixed-to-fixed rank `30`, unrestricted
fixed-projection rank `70`, thirty deficient isolates, and projection
minimum `46`.

This theorem is an abstract ledger reduction.  It does not prove that the
required old edges occur in a future owner factor; that off-diagonal lift
fibres are nonempty for its selected columns; that `d in Lambda_F`; or that
any lattice solution admits a resource-simple, chronological, edge-disjoint
sequence of physical switches.
