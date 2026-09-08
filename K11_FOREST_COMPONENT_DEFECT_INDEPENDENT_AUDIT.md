# Independent audit of the `k=11` component-defect refinements

## Verdict

**PASS, within the selected-witness scope stated in the source note.**

I found no mathematical gap in the new claims of
`K11_FOREST_COMPONENT_DEFECT_NEXT.md`.  They are valid consequences of the
already audited unrestricted `k=11,n=465` witness-band and two-coloured
central-forest theorems.  In particular, none of the arguments assumes a
fixed derivative row, a connected forest, or Johnson adjacency beyond what
is derived in the minimal-component branches.

The first unsupported step is therefore: **none in the claimed theorem
ledger**.  The first genuinely unresolved step remains outside this note:
turning one of the surviving central skeletons into a pin-surviving complete
OR array, or proving that no such realization exists.

This audit does **not** promote the scalar profile relations to sufficient
conditions.  The two-ended promotion relation is a complete necessary
finite projection of the endpoint-gap equations, not a proof that every
surviving profile has a physical schedule or an OR labeling.  The source
note respects that distinction.

## Audited inputs

The audited files were:

```text
781137d41c4feb11ffe8a0341e68266999af3de7568c0af160f2bb1f2ee6030e
  K11_FOREST_COMPONENT_DEFECT_NEXT.md

2a68876c19e5aac6ef684d40f6f95b8b3150b1eeaa6e02e212c21f3ea74a3017
  scratch/enumerate_k11_component_defect_profiles.cpp
```

The inherited facts were checked against `MATHEMATICAL_HANDOFF.md` and
`K11_INTEGRATED_SEARCH.md`, especially the unrestricted monotone band,
central linear-forest, adjacent-shadow, endpoint-alignment, singleton-pool,
and literal-boundary results.

## 1. Exact colour-specific cuts

Fix one endpoint colour with defect `u`.  Among the `X_t` selected rank-six
intervals of width at most `t`, at least `X_t-u` are matched.  A matched
rank-five interval sharing that endpoint is a proper subinterval, hence has
width at most `t-1`.  Injectivity of the endpoint matching gives

```text
X_t-u <= Y_(t-1),  0<=t<=2.
```

This proves (2.1).  Taking the smaller of the two colour defects gives
`x0<=u_*` and `x0+x1-y0<=u_*`.  For `t=2`, using both layer totals `462`
turns the same row into `y2-x3<=u_*`.  The equivalences and the comparison
with the older summed-colour rows are correct.

The weighted inequality (2.8) is also correct.  Deleting `u` matched pairs
leaves an upper-minus-lower width contribution of at least `462-u`.  The
least possible total width of the unmatched upper vertices is

```text
mu6(u)=sum_(s=1)^3 (u-X_(s-1))_+,
```

and the greatest possible total width of the unmatched lower vertices is

```text
mu5(u)=min(u,y1+y2)+min(u,y2).
```

Substitution gives exactly (2.8).  In the audited scalar region `y2>=87`
and `u<=3`, `mu5(u)=2u`, matching the checker implementation.

## 2. Adaptive endpoint alignment and diamonds

For one colour, the common rank-five/rank-six endpoint set has size
`462-u`.  Intersecting it with the 330 selected rank-four endpoints inside
465 physical positions gives

```text
330+(462-u)-465 = 327-u.
```

Strict nesting at an aligned endpoint forces rank-five width at least one
and rank-six width at least two.  Adding the 165 rank-three endpoints gives

```text
165+330+(462-u)-2*465 = 27-u,
```

and four strictly nested widths under the rank-six width-three cap are
exactly `0,1,2,3`.  Thus (3.3)--(3.6) and their counter forms are correct.

Let `A_L,A_R` denote the rank-five targets occurring at the two types of
rank-four/central alignment.  Distinct rank-five witnesses have distinct
endpoints, so these are target sets, not merely populations with
multiplicity.  Inclusion-exclusion gives

```text
|A_L intersect A_R| >= 192-(uL+uR)=192-c.
```

At such a target `S`, the two rank-four masks are distinct proper facets of
`S`, so their union is `S`.  The two rank-six masks are distinct proper
cofacets (the no-double-colour theorem rules out equality), so their
intersection is `S`.  This proves the full diamond identity (3.8).  The
analogous `27-c` and `327-c` refinements follow by one further intersection
with the opposite central-neighbour set.

## 3. Monotone and six-local components

For a two-edge segment

```text
P_i --L-- Q_j --R-- P_i',
```

proper containment gives both
`left(P_i)<left(P_i')` and `right(P_i)<right(P_i')`; hence `i<i'` in the
common left/right order of the rank-five witnesses.  The dual two-edge
segment gives increasing rank-six indices.  Since colours alternate in each
component, reversing a component if necessary makes both same-layer index
sequences strictly increasing.

Each central endpoint family omits only three of the 465 physical positions.
At a shared endpoint, the two order indices therefore differ by at most
three.  A two-edge same-rank step differs by at most six.  Theorem 3 and its
local-shadow corollary are consequently valid.

For a forest with `924` vertices and `c` components there are `924-c` edges.
On either 462-vertex side, degrees are at most two, which forces at least
`462-c` degree-two vertices.  Their two distinct rank-five neighbours union
to the rank-six target, and dually their rank-six neighbours intersect to
the rank-five target.  The index-distance-six qualification is justified by
the preceding paragraph.

## 4. Component bookkeeping and the minimal branches

An imbalanced alternating path lacks one incidence of each colour.  Balanced
paths lack two incidences of one colour.  Equal central layer sizes imply
equal numbers `a` of lower-heavy and upper-heavy components, yielding

```text
uL=a+dL,  uR=a+dR,  c=2a+dL+dR.
```

A selected rank-six singleton interval cannot contain a proper nonempty
rank-five subinterval, so it is isolated.  Therefore `e=1` implies `a>=1`
and `c>=2`.

### `c=1`

The forest is one balanced alternating Hamilton path.  One colour is a
perfect order-preserving matching.  After contracting it, the other colour
is an order-preserving matching with one omission on each side.  Avoiding a
double-colour edge and remaining connected force the omissions to opposite
ends and force the unit shift.  After a possible reversal this is exactly

```text
Q_i=[left(P_i),right(P_(i+1))], 0<=i<=460,
```

with `Q_461` a proper same-left extension of `P_461`.  Hence consecutive
rank-five unions and consecutive rank-six intersections are rainbow and
miss exactly one target on the opposite layer.

The 462 rank-five right endpoints occupy 462 of 465 positions, so the total
gap excess over their 461 consecutive gaps is at most three.  Removing the
boundary width, shifting all remaining bins by one, and distributing at most
three further units gives precisely (5.3b)--(5.3d).  The width-difference
bound `462<=W6-W5<=467` follows from a span between 461 and 464 plus a final
proper extension between one and three.

### `e=1,c=2`

The isolated upper singleton is one upper-heavy component.  Equality of the
layer sizes forces the other component to contain all 462 rank-five targets
and the remaining 461 rank-six targets, with rank-five endpoints.  Anchoring
the singleton at the left boundary makes it `Q_0`; monotonicity forces

```text
P_0,Q_1,P_1,...,Q_461,P_461.
```

Containment and endpoint order force each `Q_(i+1)` to share the left
endpoint of `P_i` and the right endpoint of `P_(i+1)`.  The mask union,
intersection, hull, and dual gap equations (5.5)--(5.8) follow.

After deleting the singleton, either rank-five endpoint sequence has only
two omitted positions in a 464-position word.  Thus each direction has at
most two total units of gap promotion.  Removing `P_461` for the right-gap
description, or `P_0` for the left-gap description, gives exactly
(5.10)--(5.11).  If the two boundary widths agree, two different endpoint
intervals require the stated multiplicity check.  The projected bounds

```text
x1<=y0<=x1+3,
x3-2<=y2<=x3+1,
459<=W6-W5<=463
```

are all valid.

## 5. Branch-one lower-shadow compression

Deleting the boundary rank-six entry preserves every witness of rank at
most five: no interval with OR rank at most five can include a literal
rank-six entry.  The remaining word has length `464=462+2` and covers every
rank-five mask, so rank slack forces every rank-one-through-rank-four target
to have a witness of length at most two.

For rank `s=3` or `4`, the selected rank-`s` and rank-five endpoint sets now
live in 464 positions and meet in at least `R-2` positions in each colour.
At least `R-4` rank-`s` targets are therefore crossed in both colours.  This
gives the claimed `161/165` and `326/330` counts and safely reduces each
generic exception budget from six to four in the anchored `e=1` branch.

## 6. Explicit surviving schedule

The interval schedule in (8.1)--(8.2) is internally consistent.  Direct
calculation gives

```text
x=(1,0,365,96), y=(0,366,96),
uL=uR=1, c=2,
ZL324=ZR324=461,
ZL24=95, ZR24=96.
```

The isolated `Q_0` and the remaining alternating path have exactly the
claimed forest.  A Hamilton cycle in the middle-levels graph on ranks five
and six of `[11]` supplies a central mask labeling: delete the chosen
rank-six vertex `C=63`, label the remaining path in cycle order, and place
`C` on `Q_0`.  Every physical forest edge is then a genuine inclusion edge,
and the adjacent union/intersection identities hold.

This is correctly advertised only as an adversarial central certificate.
It does not give array entries, pin survival, or coverage outside the two
central layers.  It proves that current endpoint/profile constraints, even
combined with central incidence, cannot by themselves exclude `e=1,c=2`.

## 7. Independent arithmetic reproduction

I copied the exact audited source to the remote Linux worker, compiled it
with optimized C++, and ran it on a dedicated allowed core.  The source hash
was unchanged.  The output hash was

```text
6ea464140b08901496e5eeae4122265b6378d73941bca6487e508c3150d35c7a
```

The program terminated with `PASS` and reproduced all displayed counts,
including:

```text
baseline e=0: 33,454 / 290,393,090
baseline e=1: 31,918 / 272,277,079
e=0,c=1 promotion law: 32,755 / 609,086
e=1,c=2 promotion law: 31,455 / 372,855
```

It also reproduced every exact-defect row, the equality of the weighted and
cumulative counts, the width-difference ranges, and the explicit endpoint
survivor.  This machine check confirms the finite arithmetic projection; the
mathematical arguments above, rather than the assertions in the program,
establish the theorem scope.

## Exact scope for integration

The following may be promoted as proved necessary structure for a
hypothetical `k=11,n=465` solution:

- (2.1)--(2.4) and the redundant weighted row (2.8);
- adaptive counts (3.3)--(3.6) and at least `192-c` full diamonds;
- monotone, six-local alternating components and at least `462-c`
  degree-two targets per central rank;
- the exact `c=1` and anchored `e=1,c=2` central reductions;
- their one-ended and two-ended necessary promotion laws;
- the branch-one four-exception refinement;
- existence of the explicit endpoint/profile/central-incidence survivor.

The following must **not** be inferred:

- that the explicit survivor factors to an OR array;
- that either minimal branch is satisfiable;
- that the finite promotion relations are sufficient for endpoint schedules;
- that `e=1` is impossible, or that `c>=3`;
- that any of these results settle `nu(11)=465`.

