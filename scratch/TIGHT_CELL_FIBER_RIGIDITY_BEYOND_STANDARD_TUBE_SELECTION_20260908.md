# Tight-cell fiber rigidity survives arbitrary cylinder-chain repartitioning

2026-09-08. Pure analysis by ternary_lift; no mathematical execution,
catalogue, or optimization. Root and appendix_a independently read and
audited the full proof, including the finite stability inequality, exact
threshold, and Section7 extension: PASS.

This extends the scope of the cyclic obstruction in
`CORRELATED_FRACTIONAL_TUBE_SELECTION_CYCLIC_OBSTRUCTION_20260908.md`.
It allows arbitrary two-coordinate fine chains, rerouting, overlapping
chain covers, and replacement of the standard hooks. It still requires
each selected row's one-coordinate shore to be the FULL fine axis in
Sections2–6. Section7 also treats cuts whose total fill cost is lower order.
It therefore does not exclude arbitrary cuts of that shore, arbitrary
new macro templates, or a general fractional-to-integral compiler.

The result is a new necessary compatibility condition, not a realization
of the charge1248 quaternary fractional certificate. The literal q-ary
compiler in `QARY_TUBE_AMPLIFICATION_AND_FINITE_GATE_20260906_c52e9.md`
continues to require an actual integral cover.

## 1. A general two-owner condition on a tight Cartesian fiber

Let X,Y,Z be nonempty finite sets. Suppose binary functions f(x,y) and
g(y,z) satisfy

    f(x,y)+g(y,z)=1 for EVERY (x,y,z) in X times Y times Z.

Then f depends only on y, and g is its complement. Indeed, fixing y,z
makes f constant in x; fixing x,y makes g constant in z.

More generally, for two indicators on coordinate sets U,V whose lifted
cylinders exactly partition a product fiber, both indicators depend
only on U intersection V. This follows by varying one coordinate in
U minus V or V minus U at a time.

Thus rational marginal coverage is not enough on a macrocell with total
fractional load exactly1. An exact realization there must satisfy this
shared-coordinate condition. Reusing the same selector fiber in two
different tight macrocells can impose incompatible shared-coordinate
requirements, regardless of how its chains were partitioned.

## 2. The enlarged cyclic model

Write L={0,...,m-1}, H={m,...,2m-1}, and I=L union H. Let

    T1={(x,y): floor(x/m)>=floor(y/m)},
    T2={(y,z): floor(y/m)>=floor(z/m)},
    T3={(z,x): floor(z/m)>=floor(x/m)}.

Their three half-weight cylinders are the binary fractional cover of
charge15/2 inflated by m. The six nonconstant binary macrocells have
fractional load exactly1, while000 and111 have load3/2.

For each i choose ANY finite family of strict two-coordinate chains
inside Ti and pair each chain with the full remaining axis I. The fine
chains need not come from the standard tube partition, need not be
disjoint, and need not retain their entire old macro support.

Let Si be the union of the chosen two-coordinate chains. Its cylinder
indicator is fi. Assume the three cylinders cover I^3. The actual
principal charge M satisfies

    M >= sum_i ( |Si| + 2m width(Si) ).             (1)

Each family must use at least width(Si) chains, and its total chain
membership is at least |Si|. This lower bound permits internal overlap.

## 3. Exact tight cells force three binary middle-block choices

First assume the cylinder cover has no excess in the six nonconstant
macrocells, so its two possible owners partition each such cell.

In100, f1 on H times L and f2 on L times L partition the fiber. Hence
f1 on its middle block H times L depends only on y. In101, the SAME
f1 block is paired with f3 on H times H, forcing it to depend only on x.
It is consequently constant, say a in{0,1}. Cyclically the middle blocks
of S2 and S3 are constant b,c in{0,1}.

The other four tight-cell equations give every diagonal block:

| Support | LL block | middle HL block | HH block |
| --- | --- | --- | --- |
| S1 on(x,y) | 1-c | a | 1-b |
| S2 on(y,z) | 1-a | b | 1-c |
| S3 on(z,x) | 1-b | c | 1-a |

Each entry0 means the block is absent, and1 means the entire m by m
block is present. Coverage of000 and111 requires a+b+c<=2.

Every nonempty Si contains a complete square and has width exactly m.
The lower bound follows from the square's middle antichain. For the
upper bound, any chosen subset of the three macro cells is a strict
macro chain, so the ordinary two-dimensional tube partition has m
chains. Summing (1) now gives the exact possibilities

| a+b+c | total occupied macro squares | nonempty families | minimum charge |
| --- | --- | --- | --- |
| 0 | 6 | 3 | 12m^2 |
| 1 | 5 | 3 | 11m^2 |
| 2 | 4 | 2 | 8m^2 |

The bounds are attained for the respective block patterns by the tube
partitions. In particular, no exact half-density middle block can occur,
even after arbitrary repartitioning of the two-coordinate shore.

## 4. An exact rerouted8m^2 compiler

Take a=b=1,c=0. Then

    S1=I times L on(x,y),
    S2=H times I on(y,z),
    S3 is empty.

The two cylinders partition I^3 according to whether y belongs to L or H.
For j=0,...,m-1 the following explicit hooks partition I times L:

    Pj={(u,j):0<=u<=2m-1-j}
       union{(2m-1-j,v):j<v<=m-1}.

Each Pj has length3m-1-2j. Use Pj on(x,y) with full free z. For the
second family use Qj={(m+v,u):(u,v) in Pj} on(y,z), with full free x.
The Qj partition H times I. There are exactly2m physical chain pairs,
and the principal charge is exactly

    2*(2m^2 + m*2m)=8m^2.                         (2)

This is an actual cover and a permitted rerouting in the enlarged model.
The standard whole-hook selection model had unrestricted selection optimum
10m^2. Rerouting permits the zero-tight-excess cover here at8m^2; this does
not assert that the old10m^2 optimum had zero tight-cell excess. Formula(2) merely
matches the already known integral8m^2 benchmark. It does not attain
the fractional7.5m^2 charge or give a new covering coefficient.

## 5. A finite stability bound for small tight-cell excess

Let E be the total cylinder excess volume in the six nonconstant
macrocells:

    E=sum_over_those_cells sum_points (number of owner cylinders -1),
    delta=E/m^3.

The summands are0 or1 since the cover is complete and exactly two macro
owners are possible. Physical excess, including repeated chains within
a family, is at least this E.

We prove, for delta<1/9,

    M/m^2 >= 8 - 24 delta - 6 sqrt(3 delta).        (3)

Here and below normalized errors inside a square or cube use uniform
counting measure. On a covered two-owner fiber, f(x,y)+g(y,z)>=1.
For each y, either f is1 for every x or g is1 for every z. Define
h(y)=1 precisely when f is1 for every x. If the normalized fiber excess
is epsilon, then

    ||f-h||_1 <= epsilon,
    ||g-(1-h)||_1 <= epsilon.                     (4)

For example, at a y where h=0, g is identically1, and the fraction of
ones of f is exactly the excess at that y. At h=1 the analogous statement
holds for g.

Apply(4) to the two cells using the same middle block of f1. This makes
that block close to a binary function of y and close to one of x, with
sum of the two errors at most delta. For independent uniform x,y, if
these binary functions have means p,q, their disagreement is
p+q-2pq>=min(p,1-p). Choosing the nearer constant gives a in{0,1} with

    ||f1_middle-a||_1 <= 2 delta.

Obtain b,c cyclically. Pairing a diagonal block with the appropriate
middle block in its tight cell, using
|f-(1-g)|=f+g-1, gives error at most3 delta in every diagonal block.
Thus the three supports differ in total area by at most24 delta m^2
from the binary block table of Section3: three middle errors2 delta and
six diagonal errors3 delta.

If a=b=c=1, all three lower diagonal blocks have area at most3 delta m^2.
Their cylinders cannot cover000, because coverage requires their total
area at least m^2. This would give9 delta>=1. Hence delta<1/9 implies
a+b+c<=2.

Every nonempty ideal support has a block with at least(1-3 delta)m^2
actual selected points. If a subset Q of an m by m square has width w,
each rank contains at most w selected points. Summing the rank bounds
gives

    |Q| <= sum_r min(w,rank_size_r)
         =m^2-(m-w)^2,

so width(Q)>=m-sqrt(m^2-|Q|). Therefore every such support has width at
least(1-sqrt(3 delta))m. Combine these width bounds, the area error,
and the three exact block cases in Section3. The smallest exact charge
is8m^2, and at most three width terms are lost, giving(3).

In particular, E=o(m^3) forces M>=(8-o(1))m^2. Conversely, any cover
in this enlarged cylinder model with M<=7.5m^2 must satisfy the explicit
necessary condition

    E/m^3 >= (sqrt(13)-3)^2/192.                   (5)

For delta<1/9 this follows by solving
24 delta+6 sqrt(3 delta)>=1/2 from(3); for delta>=1/9 it is automatic.
No numerical approximation is needed.

## 6. Consequence for a genuine fractional realization claim

A realization preserving the half-weight incidence volumes on every
macro support cell would give total volume6m^3 in the six tight cells.
If it actually covers them, their excess is zero. Preserving those
incidences up to o(m^3) gives tight-cell excess o(m^3). Both are excluded
at principal charge(7.5+o(1))m^2 by Sections3 and5, even with arbitrary
repartitioning and rerouting on the two-coordinate shores.

A proposed compiler can escape this theorem by cutting the full free
chains, using other macro supports, or making a nonvanishing change in
the tight-cell incidence volumes. Each escape needs its own literal
coverage and chain-charge calculation. The condition does not decide
whether the denominator15 quaternary certificate admits such a compiler,
and supplies no general fractional-to-word conversion.

## 7. Lower-order cutting of the free chains does not escape

There is a useful consequence even when the one-coordinate shores may
be arbitrary nonempty subchains J of I. Keep the same three macro
staircase supports: every row is C times J, where C is a strict chain
inside the appropriate Ti. Suppose these rows actually cover I^3.
Let their principal charge be M and put

    A=sum_rows (2m-|J|).

Let E_original be PHYSICAL excess volume in the six tight macrocells,
counting all rows and all internal overlaps. Extend every J to I. This
produces an actual cover in the model of Section2, of charge exactly
M+A. The total volume it adds, even over the entire cube, is at most

    sum_rows |C|(2m-|J|) <= (4m-1)A,

because a strict chain in I^2 has at most4m-1 members. Hence the tight
cylinder excess of the enlarged family is at most

    E_original+(4m-1)A.                           (6)

It follows from Section5 that

    E_original=o(m^3) and A=o(m^2)
        imply M>=(8-o(1))m^2.                    (7)

Thus a fractional-incidence-preserving construction of charge
(7.5+o(1))m^2 in these three macro supports must make a leading-order
change in the free-chain memberships: A cannot be o(m^2).
Such cuts are not lower order merely because each cut is at an endpoint.
This is not a lower bound on all constructions with arbitrary J; a
compiler may deliberately make A of order m^2 and calculate its actual
benefit. The result specifies which geometric change remains necessary.
