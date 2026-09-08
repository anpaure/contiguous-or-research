# Independent audit of the `k=11` minimal-component SAT portfolios

## Verdict

**PASS for both named branches.**

The guarded modes

```text
K11_FOREST_MIN_COMPONENT=e0c1
K11_FOREST_MIN_COMPONENT=e1c2
```

are sound and complete, respectively, for the already proved selected-witness
branches `e=0,c=1` and anchored `e=1,c=2`.  This is completeness only inside
the named minimal-component branch; the two modes do not exhaust the
unrestricted `k=11,n=465` formula.

I found no indexing error, missing endpoint condition, wrong Boolean
equivalence, or unjustified low-rank compression.  The modes add no SAT
variables.  With the guard absent, the pre-existing clause stream is exactly
unchanged.

## Audited inputs

```text
c16750771e78912f427d472d845cf952e30e4909eea97b474b6fccc0d9676017
  k11_forest_sat.cpp

781137d41c4feb11ffe8a0341e68266999af3de7568c0af160f2bb1f2ee6030e
  K11_FOREST_COMPONENT_DEFECT_NEXT.md

1fa59129926724be59cc5ea3b94bb0b5b6d6670eb3c1137fbcf8c2cd358a18c9
  K11_MINCOMP_SOLVER_ENCODING.md

12aff7110503d4f28bc12427aec56c36fa6fa1652d907b4671778a3707246796
  scratch/check_k11_mincomp_schedule.cpp
```

For the absent-mode regression I compared against the immediately preceding,
independently audited branch source:

```text
c1eff19c73fa6610bd603194a43c89ffb5a54092cb35947fda64c6ed61876f0b
  k11_forest_sat_branch.cpp
```

The independent clause-stream hash shim used in that comparison is:

```text
a350169f2169a06e51999c92612a670f360add5301dc9e500ff539cb701a959e
  scratch/mincomp_hash_stub/cadical.hpp
```

## 1. Guards and prerequisites

The parser accepts exactly `e0c1` and `e1c2`.  It rejects `e0c1` unless
`K11_FOREST_RANK6_BRANCH=0`, and rejects `e1c2` unless the branch is `1`.
The existing rank-six branch gate in turn requires all four prerequisites:

```text
K11_FOREST_CANONICAL_RANK6_ENTRY=1
K11_FOREST_RANK6_BOUNDARY_ENTRY=1
K11_FOREST_BAND_CUTS=1
K11_FOREST_JOINT_BAND_CUTS=1.
```

I exercised the invalid name, absent branch, wrong branch, and missing
prerequisite cases; each exits with status 2 before formula construction.

The central component theorem itself needs no adjacent-shadow option.  The
extra four-exception clauses are naturally inert when their optional shadow
module is absent, while the direct low-rank witnesses still receive the
proved length cap.  A minimal-prerequisite `e1c2` build with no adjacent or
rank-three shadow modules completed successfully.

## 2. Common state and mask encoding

At central row index `i`, state `(a,b)` denotes the physical interval

```text
[i+a,i+b],  0<=a<=b<=3.
```

The inherited formula enforces exactly one of the ten states in every row,
monotonicity of both offsets, the exact interval OR in eleven coordinate
variables, exact rank, and a permutation of all masks in each central layer.
Consequently, a projection implication from the unique lower state to a set
of upper states is exact: both endpoint projections must be satisfied by the
same unique upper state.  Empty support correctly becomes a unit prohibition.

The added coordinate clauses are the exact truth tables

```text
z <-> x OR y:   (-x z), (-y z), (-z x y)
z <-> x AND y:  (-z x), (-z y), (z -x -y).
```

Thus the new mask equations are equivalences, not one-way containments.

## 3. Mode `e1c2`

The rank-six literal branch has a unique selected singleton rank-six witness.
The inherited boundary and coordinate symmetries put it at

```text
Q_0=[0,0],  mask(Q_0)=63.
```

The source asserts both the state and all eleven value bits.  Because state
`00` already links the central value to the array interval, this also fixes
the actual entry `A[0]=63`.

The other component has the proved order

```text
P_0,Q_1,P_1,Q_2,...,Q_461,P_461.
```

For `0<=i<=460`, write the states of `P_i,P_(i+1),Q_(i+1)` as
`(a,b),(a',b'),(c,d)`.  Physical endpoint equality is exactly

```text
i+1+c = i+a       <=> c=a-1,
i+1+d = i+1+b'    <=> d=b'.
```

These are precisely the two source projections.  The bit clauses impose

```text
Q_(i+1)=P_i OR P_(i+1),       0<=i<=460,
P_i=Q_i AND Q_(i+1),          1<=i<=460.
```

Two distinct five-subsets of the same six-set have that six-set as their
union, and two distinct six-supersets of the same five-set intersect in that
five-set, so these are exactly the component identities.  The boundary
vertices correctly have only the identity supplied by their actual two-sided
degree.

The fixed schedule contributes

```text
1 + 11                         Q_0 state and mask
+ 2*10*461                     endpoint projections
+ 3*11*461                     union identities
+ 3*11*460                     internal intersection identities
= 39,625 clauses.
```

## 4. Mode `e0c1`

There is no literal rank-six entry.  Reversal is therefore a symmetry of this
branch and of every prerequisite module: it swaps left/right endpoint colors,
reindexes each monotone band, preserves widths and mask targets, and does not
move an anchored literal.  Hence choosing the left color as the perfect
matching loses no solution.

The proved one-component schedule is

```text
Q_i=[left(P_i),right(P_(i+1))],  0<=i<=460,
Q_461 is a proper same-left extension of P_461.
```

For states `(a,b),(a',b'),(c,d)` of `P_i,P_(i+1),Q_i`, the physical equations
are exactly

```text
c=a,
d=b'+1.
```

For the last row they are `c=a,d>b`.  The source implements precisely these
relations and the exact mask identities

```text
Q_i=P_i OR P_(i+1),             0<=i<=460,
P_i=Q_(i-1) AND Q_i,            1<=i<=461.
```

The final `P_461` intersection is present; no nonexistent `P_0` intersection
is added.  The clause total is

```text
2*10*461 + 3*11*461 + 10 + 3*11*461 = 39,656.
```

The independent finite checker enumerated all 1,000 state triples and all
100 final state pairs.  It returned

```text
PASS e1_triples=55 e0_triples=55 e0_boundary_pairs=10
e1_schedule_clauses=39625 e0_schedule_clauses=39656
```

## 5. Branch-one low-rank reductions

No interval of OR-rank at most five can contain the literal rank-six entry
`A[0]=63`.  Deleting that entry leaves a word of length

```text
464 = binom(11,5)+2
```

that still represents every rank-five mask.  Rank slack therefore gives a
witness of physical length at most two for every target of ranks one through
four.  The clauses

```text
not Inside(p) OR not Inside(p+2)
```

are exactly that cap for the threshold interval encoding.  They are added to
every applicable direct or generic exception witness; crossed shadow
candidates already have length at most two by construction.

In the full production option set, 66 direct rank-one/two targets and twelve
rank-three/four generic slots receive 463 clauses each:

```text
(66+12)*463 = 36,114.
```

After deletion, the selected rank-three or rank-four endpoint set and the
462 selected rank-five endpoints lie in 464 positions.  The proved
inclusion-exclusion bound leaves at most four uncrossed target names per
layer.  Forcing generic slots 4 and 5 to copy the target flags of slots 0 and
1 therefore preserves completeness.  Their interval and pin variables stay
independent, so duplicate filler witnesses remain available when fewer than
four exceptions occur.  The production clause count is

```text
2 duplicate slots * (165+330) names * 2 clauses = 1,980.
```

This restriction is applied only to an allocated six-slot layer.  With a
shadow module absent, the corresponding targets remain direct and are merely
length-capped.

## 6. Independent remote build and formula inventories

All substantial builds ran on `213.173.111.107:48809`, not on the local Mac.
The current source was independently copied and compiled with

```text
g++ -O3 -std=c++2a -Wall -Wextra -Wpedantic
```

against the existing CaDiCaL static library.  The independent binary hashes
are

```text
8fa2a3427ef17c2724ad408028bede418b6ffae62a83456f74f5052162f3a9da
  k11_forest_sat_audit

c7ff2215ccd61e980524fb8c7e3d86764ac55f0d001d27539eeb4a341f0fa3ae
  check_schedule
```

With all production optional modules enabled, the reproduced inventories are:

| formula | variables | clauses | added by min-component mode |
|---|---:|---:|---:|
| branch 0, guard absent | 2,924,697 | 14,732,380 | 0 |
| branch 0, `e0c1` | 2,924,697 | 14,772,036 | 39,656 |
| branch 1, guard absent | 2,924,938 | 14,734,039 | 0 |
| branch 1, `e1c2` | 2,924,938 | 14,811,758 | 77,719 |

For `e1c2`, the exact delta is

```text
39,625 + 36,114 + 1,980 = 77,719.
```

No mode allocates a variable.

## 7. Absent-mode byte regression

A source diff against the pre-mode source shows only:

1. parsing and validation of the new string;
2. three diagnostic counters;
3. the block guarded by `!min_component_mode.empty()`;
4. guarded diagnostic output.

No pre-existing variable allocation or clause call moved or changed.  I also
compiled the old and new sources against an independent streaming `Solver`
shim and hashed every signed literal and every clause terminator in the
production branch-zero build.  The two streams were identical:

```text
variables       2,924,697
clauses         14,732,380
literal calls   65,118,464
hash1           508f5b599ffa2587
hash2           ce4ebfb80b9d4243
```

The complete two hash-summary files were byte-identical and both had SHA-256

```text
70c5ad71c35e21e2bffdb393115d9c1392e0f8179e5f475272b8052e388f3ef4.
```

Together with the guarded source diff, this establishes the claimed
absent-mode formula regression.

## Exact scope

It is safe to deploy either mode as an exhaustive search of its named branch:

```text
e0c1: e=0 and one central component;
e1c2: the anchored literal branch and exactly two central components.
```

SAT in either mode still requires independent verification of the emitted OR
array.  UNSAT eliminates only that named branch unless accompanied by the
other component branches and a checked case split.  Nothing in this audit
claims `nu(11)=465`, nor does it claim that the two minimal-component branches
cover every possible optimum.
