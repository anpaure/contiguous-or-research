# Exact r99 portal, same-palette, and joint-cover Benders closure

Date: 2026-07-29  
Lane: L  
Status: solver-free singleton, same-palette, and joint-cover rows; exact canonical max-closure separator; general replayed-core theorem proved

## 1. Main result

The 29 canonical high-slack radius-99 cuts do not require 29 incumbent
no-goods or a CP-SAT assumption-core run.  Every one violates the same exact
lower-q1 endpoint portal inequality:

```text
cut[4529]
  <= cut[3299]+cut[4560]+cut[4598]+cut[4936]
   + cut[5049]+cut[5463]+cut[7892]+cut[9827]
   + cut[11485]+cut[12197]+cut[12207]+cut[14126]
   + cut[17805]+cut[22581].                         (1.1)
```

This is a proof-safe generalized Benders cut.  Its fixed-seam core has only
eight rows:

- the lower-q1 row for colour `(0,1849)`; and
- the seven upper degree half-rows `deg_y(v)<=0` at

  ```text
  v in {89,99,109,263,288,355,613}.
  ```

The core is solver-free infeasible and subset-minimal.  A literal 99-seam
witness has been frozen for every one-row deletion.  Thus (1.1) is not a
solver-returned sufficient core without replay: it is an independently
checked algebraic Hall certificate.

All 1,328 existing unique-colour portal inequalities are valid coefficient-one
Boolean strengthenings of singleton endpoint-Hall cuts.  They subsume the observed presolve failures: each of the
29 high-slack cuts violates 17 through 23 of them, and all violate (1.1).
For the fixed source, adding all 1,328 source-unique-colour rows is already
their complete static singleton portal closure; repeating that same separator
adds nothing new.  This says nothing about newly lost multi-source colours or
grouped rows.

They are not a sufficiency theorem for q1 completion, even on the frozen r99
source.  Explicit motif-hitting cuts in both locked-edge branches satisfy all
1,328 rows but violate level-2 same-palette Hall: lower demand/capacity is
`5/3`, while upper is `8/4`.  Singleton portal rows do not charge shared
endpoint capacity only once.  The next exact closure is the grouped
same-palette endpoint-cover family

```text
sum_{c in C} lost_c(x) <= sum_{v in Z} b_v(x),       (1.2)
```

whenever `Z` meets every off-source provider seam of every colour in `C`.
The canonical subfamily obtained by taking the full portal union
`Z=union_(c in C)P_c` has an exact polynomial max-closure/min-cut separator,
including fractional master points.  This is not a separator for every
arbitrary endpoint cover `Z` in (1.2).  Even (1.2) remains only necessary for
the two-palette binary degree-exact seam problem.

After canonical same-palette closure converges, explicit retain/delete cuts
remain.  The new joint double-repair hypergraph couples one unique lower
colour, one unique upper colour and both endpoint capacities per candidate
seam.  Two solver-free full covers give exact projected rows with displayed
deficits 14 and 3, rejecting those cuts.  These are feasible-cover margins,
not certified minimum-cover deficits.  They supersede same-palette closure as
the current cut-only candidate filter, not as a logically dominating family.
The lifted Benders master already contains the complete double-seam matching,
so every joint-cover row is implied there; a full fixed-cut iteration must
still retain the same-palette rows and replayed feature-core fallback.

No new H100 solve was started.  The actual high-slack cut is proved
solver-free; the general extractor is frozen and compiled for the next
portal-feasible incumbent.

## 2. Exact fixed-cut seam subproblem

Let `F` be the frozen 858-edge loopless source factor, let `A` be all 26,570
loopless off-source catalogue seams, and let `D subset F` be a 99-edge source
cut.  Put

```text
b_v(D) = number of cut source edges incident with v.
```

Since `F` is degree two, `b_v(D)` lies in `{0,1,2}` and

```text
sum_v b_v(D) = 198.
```

For every lower or upper q1 colour `c`, let `P_F(c)` be its selected source
provider set and define

```text
lost_c(D) = 1  iff  P_F(c) subset D.                 (2.1)
```

This definition must include multi-source colours.  Sole-provider Pareto
counts are only lower bounds on the exact lost-row census.  For example, the
canonical retain witness labelled `(50,63)` actually loses 57 lower and 65
upper rows: seven extra lower and two extra upper rows have multiple source
providers.

### Theorem 2.1 (signature exactness)

The cut `D` has a loopless degree-two both-q1 seam completion if and only if
there are binary variables `y_a`, `a in A`, satisfying

```text
sum_{a in A} y_a = 99,                               (2.2)

sum_{a incident v} y_a = b_v(D)       for every v,  (2.3)

sum_{a in A, colour_p(a)=c} y_a >= 1
       for every palette p and every c with lost_c(D)=1.  (2.4)
```

Consequently seam-completion feasibility depends on `D` only through the
pair

```text
( b(D), {c: lost_c(D)=1} ).                          (2.5)
```

#### Proof

After deleting `D`, vertex `v` has degree `2-b_v(D)`.  Equation (2.3) restores
degree two exactly.  Every q1 colour not lost in (2.1) retains a selected
source provider and is automatic.  Every lost colour needs precisely the
addition-provider row (2.4).  Summing (2.3) over all vertices gives twice
(2.2), so (2.2) is redundant but useful as a fixed-radius hard row.  No other
property of the source cut appears.  ∎

This theorem deliberately excludes top chronology, newly created residence
motifs, connectivity and voltage.  Infeasibility of (2.2)--(2.4) excludes
every stronger target; feasibility certifies only degree and both q1 palettes.

## 3. The critical eight-row core

The lower colour `(0,1849)` has sole selected source provider edge 4529, with
quotient endpoints `{88,316}`.  Its 35 loopless off-source providers form
exactly

```text
K_9 minus the edge {88,316}
```

on the nine vertices

```text
{88,316} union {89,99,109,263,288,355,613}.          (3.1)
```

Thus every replacement provider meets the seven-node set

```text
P={89,99,109,263,288,355,613}.                       (3.2)
```

The selected source has two distinct incident edges at each node of `P`, and
the resulting 14-edge union is

```text
H={3299,4560,4598,4936,5049,5463,7892,
   9827,11485,12197,12207,14126,17805,22581}.        (3.3)
```

No edge of `H` is incident with two nodes of `P`.

### Theorem 3.1 (portal Benders row)

Every loopless degree-balanced both-q1 completion of a source cut `D`
satisfies (1.1).

#### Proof

If edge 4529 is retained, (1.1) is automatic.  If it is cut, colour
`(0,1849)` is lost and a replacement provider must be added.  By (3.1), that
provider has positive incidence at some `v in P`.  Degree restoration gives
`b_v(D)>=1`, so at least one of the two selected source edges incident with
`v` is cut.  Those source edges are exactly the bank `H`.  Hence the right
side of (1.1) is at least one.  ∎

### Theorem 3.2 (solver-free subset-minimal core)

Take the hard seam row `sum_a y_a=99` and the following eight feature rows:

```text
q1(lower,(0,1849)),
deg_y(v)<=0  for v in P.                             (3.4)
```

The system (3.4) is infeasible.  Removing any one of its eight feature rows
makes it feasible.  Therefore it is an inclusion-minimal feature core.

#### Proof

The q1 row selects one of the 35 edges of `K_9-{88,316}`.  Every such edge
meets `P`, while the seven degree rows forbid every selected incidence in
`P`; this is the contradiction.

If the q1 row is removed, choose any 99 distinct allowed seams avoiding `P`.
If the degree row at `v in P` is removed, choose the provider seam `{88,v}`
and 98 further distinct allowed seams avoiding `P\{v}`.  These assignments
satisfy the hard cardinality row and all seven remaining feature rows.  The
permanent audit records and rechecks all eight literal seam lists.  ∎

For a master cut, the eight-feature logic no-good says

```text
lost_(0,1849)(D) + sum_{v in P} 1[b_v(D)<=0] <= 7.   (3.5)
```

Since the colour is source-unique and the seven portal incidences are the 14
distinct edges in `H`, (3.5) is equivalent on binary master cuts to the linear
row (1.1): all seven zero-demand predicates hold exactly when every edge of
`H` is uncut.  The two formulations need not define the same fractional
relaxation.

### Corollary 3.3 (all 29 high-slack cuts are subsumed)

Every canonical Pareto cut has

```text
4529 in D,    D intersect H = empty.
```

Hence all 29 violate (1.1), across both locked-edge branches and every one of
the 29 Pareto loss pairs.  Their fixed-cut seam infeasibility is therefore
proved independently of the absent per-cut model/log files and independently
of CP-SAT.  One generalized row dominates the 29 full incumbent no-goods.

## 4. The full 1,328-row portal family

There are 675 lower and 673 upper source-unique colours.  Twenty have a
parallel off-source provider on the two endpoints of their source edge and do
not yield a nontrivial portal cut.  The remaining rows are

```text
667 lower + 661 upper = 1328.                        (4.1)
```

For such a colour `c`, let `e(c)` be its sole source provider.  Let `P_c` be
the set of endpoints outside `e(c)` used by alternative provider seams, and
let `H_c` be the selected source edges incident with `P_c`.  The exact row is

```text
cut[e(c)] <= sum_{h in H_c} cut[h].                  (4.2)
```

The proof is identical to Theorem 3.1.  The frozen family has alternate-node
sizes `5^1,6^16,7^1311` and support sizes
`10^2,11^2,12^14,13^48,14^1262`.

All 29 canonical cuts violate between 17 and 23 portal rows.  Thus their
presolve `INFEASIBLE` statuses are fully subsumed by (4.2).  They supply no
evidence of a deeper binary seam obstruction.

### Proposition 4.1 (static closure stabilizes immediately)

For the fixed source and fixed seam catalogue, all data in (4.2) are static.
Adding all 1,328 rows to the cut master is therefore already closed under
re-separating singleton unique-colour portals.  A second pass can find no new
row of the same type.

This does not say that the resulting master projection equals the seam
completion projection.

## 5. Why singleton portal closure is not a Hall theorem

Fix one palette.  For a colour set `C` and an endpoint set `Z`, suppose every
allowed provider seam for every `c in C` meets `Z`.

### Theorem 5.1 (grouped endpoint-cover Hall row)

Every fixed-cut seam completion satisfies

```text
sum_{c in C} lost_c(D) <= sum_{v in Z} b_v(D).        (5.1)
```

#### Proof

For each lost colour in `C`, choose one selected provider seam.  Distinct
colours in one palette require distinct seams because one seam has only one
colour in that palette.  Every chosen seam consumes at least one incidence in
`Z`.  The total available incidence in `Z` is the right side of (5.1) by
degree restoration.  ∎

For one colour, (5.1) has right side

```text
sum_{v in Z} b_v(D)
=sum_{source h incident Z}|h intersect Z| cut[h].
```

Portal row (4.2) replaces every positive incidence multiplicity by coefficient
one.  It is a valid Boolean strengthening because its left side is binary: a
lost unique colour needs at least one positive portal incidence.  Thus portal
rows are coefficient-one strengthened rank-one endpoint-cover cuts, not
literally the rank-one formula when a source edge has two portal endpoints.
They do not generate the grouped inequality by mere summation when several
colours share the same portal capacity: summing singleton rows counts the same
source cut support once per colour, whereas (5.1) charges its finite endpoint
capacity only once.

The minimum abstract obstruction has one endpoint of capacity one and two
lost same-palette colours whose provider families all meet that endpoint.
Both singleton portal tests read `1<=1`, while the grouped row reads `2<=1`.
Thus singleton closure is not universally sufficient.

The independently verified motif-1993 local fibre supplies a physical warning
of the same kind: all pointwise blockers can be cleared while a six-row
palette/endpoint grouped Hall core remains.  That object is not a
portal-feasible radius-99 cut of the present frozen source, so it disproves a
universal singleton theorem but does not settle the finite frozen-r99
remainder.

For the original 29 Pareto seeds, an exact solver-free audit independently finds no
violating grouped endpoint cover with at most two portal nodes among the 29
current seeds.  Separately, all 29 violate many singleton rows whose portal
sets have size five through seven.  Whether
every *portal-feasible* frozen r99 cut passes all grouped rows is answered
negatively by the next theorem.

### Theorem 5.2 (strict level-2 Hall cuts in both branches)

There are explicit 99-edge motif-hitting cuts `D_R,D_D` in the retain and
delete/replace branches respectively such that both satisfy all 1,328
first-order portal rows.  Nevertheless:

1. In both branches the lower colour set has source providers

   ```text
   T_L={764,1559,9750,21323,24374}.
   ```

   Its portal union has 32 nodes.  The exact cut incidence on that union is
   three, while all five source providers are cut.  Hence the Hall row reads
   `3>=5` and has deficit two.
2. In the retain branch the upper set is

   ```text
   T_UR={652,764,1406,2169,7445,12575,16767,24697}.
   ```

   Its portal union has 51 nodes and cut incidence four, versus demand eight.
3. In the delete branch the upper set is

   ```text
   T_UD={1406,2169,7445,12575,16767,20660,22501,24697}.
   ```

   Its portal union has 52 nodes and cut incidence four, again versus demand
   eight.

The lower row is identical in the two branches.  Thus the four displayed
branch/palette certificates deduplicate to exactly three globally valid
linear Benders rows.

#### Proof

The permanent audit reconstructs all 147 motifs, all 1,328 portal rows and
all replacement-provider families.  Each cut has radius 99, lies in its named
branch, hits all 147 current source motifs and violates no singleton portal
row.  This does not construct additions or a resident completed factor.  For each
displayed same-palette colour set, every replacement provider meets the union
of its portal nodes.  Theorem 5.1 therefore applies.  Direct endpoint counting
gives the stated `5>3` and `8>4` violations.  ∎

For a selected source-edge set `T` and portal union `P`, the exact master row
is

```text
sum_{h in F} |ends(h) intersect P| cut[h]
    >= sum_{e in T} cut[e].                           (5.2)
```

Coefficients on the left are zero, one or two.  They must not be Booleanized:
a source edge with both endpoints in `P` supplies two units of endpoint
capacity.

The audit also emits candidate-specific signed no-goods

```text
sum_{e in T}(1-cut[e]) + sum_{h in zero_support}cut[h] >= 1.  (5.3)
```

They are valid, but redundant once the corresponding global row (5.2) is in
the master: under the antecedent of (5.3), the maximum possible left capacity
in (5.2) is the already deficient candidate capacity.  Deduplication therefore
keeps the three global rows and retains the three distinct signed no-goods only
as diagnostic certificates.

### Theorem 5.3 (exact separator for the canonical portal-union subfamily)

Fix one palette and a candidate cut vector `x in [0,1]^F`.  For every one of
the 667 lower or 661 upper nonparallel source-unique portal colours, give
colour `c` profit

```text
p_c=x[e(c)],
```
and give portal node `v` cost

```text
d_x(v)=sum_{h in F} incidence(v,h)x[h].               (5.4)
```

Here `c -> e(c)` is injective within either palette: a catalogue seam carries
exactly one colour in that palette.  It is nevertheless cleaner to regard
`T` below as a colour set; the right side is the indicated sum with its colour
multiplicity.

For a colour set `T`, let `P(T)=union_{c in T}P_c`.  The violation of its
grouped Hall row is

```text
Delta_x(T)=sum_{c in T}p_c-sum_{v in P(T)}d_x(v).     (5.5)
```

This row is valid even for the fractional seam-recourse relaxation.  Indeed,
its q1 rows are

```text
sum_{a provider of c} y_a >= x[e(c)]                 (5.5a)
```

for `c in T`.  Within one palette a seam has exactly one colour, so these
replacement-provider sets are disjoint as seam-ID sets, including when
distinct catalogue IDs have the same quotient endpoints.  Every replacement
provider of `c` meets `P_c`.
Summing (5.5a), charging each `y_a` to one of its endpoint incidences in
`P(T)`, and then using fractional degree restoration gives

```text
sum_{c in T}x[e(c)]
 <= sum_{v in P(T)} sum_{a incident v}y_a
  = sum_{v in P(T)}d_x(v).                           (5.5b)
```

The maximum of (5.5) is the maximum-weight closure in the directed network

```text
source -> colour c       capacity p_c,
colour c -> v in P_c     capacity INF,
portal v -> sink         capacity d_x(v),             (5.6)
```

where `INF>sum_c p_c`.  Consequently one exact minimum cut separates all
canonical same-palette rows indexed by `T` with cover exactly `P(T)`: a
positive closure value yields the most violated such row (5.2), and a
nonpositive value proves that every such canonical row is satisfied.

#### Proof of exact separation

A finite minimum cut cannot put a selected colour on the source side while
leaving one of its forced portal nodes on the sink side, because replacing
that infinite arc would cost more than cutting every profit arc.  Hence the
source side is a closure.  Its cut capacity is

```text
sum_{c not in T}p_c + sum_{v in P(T)}d_x(v).
```

Subtracting this from total profit gives (5.5).  The standard min-cut/closure
identity follows, with no integrality assumption on `x`.  ∎

The empty colour set has value zero, so the maximum is nonnegative and a
nonpositive answer means exactly zero.  Colours of zero profit may be omitted
without changing the optimum because every portal cost is nonnegative.

This theorem does **not** separate the full endpoint-cover family of Theorem
5.1.  There, a cover `Z` may be any set meeting every provider edge of every
selected colour.  For one provider edge `uv` this is the disjunction
`u in Z or v in Z`; it does not force all nodes of `P_c` into `Z`.  The arcs
`c -> v` for every `v in P_c` deliberately enforce the single canonical
choice `Z=P(T)`.  No completeness or polynomial-separation claim is made here
for arbitrary covers.

The distinction is already strict in a simple loopless degree-two source.
Take the source six-cycle `0-1-4-2-3-5-0`, put cut weight one on
`e_a=01,e_b=23` and zero on its other four edges, and give two distinct
same-palette colours the replacement providers `g_a=12,g_b=13`.  Neither
provider is a source edge.  The outside-base portal sets are `P_a={2}` and
`P_b={1}`, while `d_x(1)=d_x(2)=1`.  Both singleton canonical rows and the
two-colour canonical row are equalities.  However `Z={1}` meets both provider
edges, so the general endpoint-cover row has demand two and capacity one.
Thus canonical closure can certify zero maximum while Theorem 5.1 still has a
violated noncanonical row.  More generally, for fixed `T` the cheapest
arbitrary `Z` is a weighted vertex cover of the union of its
replacement-provider graphs; that disjunctive problem is the precise
additional gate.

If one insists that the emitted colour family and endpoint cover be integral,
the exact source-unique endpoint-cover optimization uses binary colour
variables `t_c` and endpoint variables `z_v`:

```text
maximize  sum_c x[e(c)]t_c - sum_v d_x(v)z_v,
subject to t_c <= z_u+z_v
           for every replacement-provider seam uv of c.   (5.7)
```

(A provider loop at `v` would give `t_c<=z_v`.)  A positive optimum emits
`T={c:t_c=1}` and `Z={v:z_v=1}`; a nonpositive optimum certifies all arbitrary
endpoint-cover rows for this source-unique palette.  Replacing each OR row in
(5.7) by the AND implications `t_c<=z_v` for every `v in P_c` is exactly the
canonical closure network (5.6).

There is nevertheless an explicit-catalogue polynomial separator for a
**dominating fractional endpoint-cover family**.  Relax (5.7) to
`0<=t_c,z_v<=1`.  Every feasible
fractional pair emits the globally valid weighted row

```text
sum_v z_v d_x(v) >= sum_c t_c x[e(c)].                 (5.8)
```

Indeed, multiply the q1 repair row for colour `c` by `t_c`; every provider
seam `uv` can then be charged by `z_u+z_v>=t_c`, and exact degree restoration
converts added incidence to `d_x`.  Thus a positive LP optimum supplies a
valid violated row.  Conversely, every integral endpoint-cover row is an LP
feasible point, so a nonpositive LP optimum certifies all of them.  This does
not make the binary prize-weighted vertex-cover optimization polynomial; it
makes that binary restriction unnecessary for separation because the
fractional weighted family is stronger.  The four-colour `6c98` row is the
integral witness `t=1_T,z=1_P` in (5.8).

The Farkas converse sharpens this statement: (5.8), over all feasible
fractional `t,z`, exactly characterizes fractional one-palette provider
packing under endpoint **upper capacities**.  The simultaneous rank-two
lower/upper theorem, its containment of the joint-cover rows below, and the
larger dual needed for exact degree equality are proved in
`MATH_THEOREM_L_GLOBAL_ENDPOINT_CAPACITY_HALL_FARKAS_20260729.md`.

The permanent implementation uses exact rational capacities.  It finds the
maximally violated member of this fixed linear family at any rational
`x in [0,1]^F`; it does not characterize the entire fractional seam-completion
projection.  Source edge
orbits remain distinct even when quotient endpoints are parallel, and the
coefficient of a source edge is exactly its endpoint-incidence count in
`P(T)`.  Loops are outside the implementation scope: the frozen source has no
loops and addable loops are excluded.  A loop-enabled version must handle
provider loops consistently and count each source-loop degree incidence
twice.

The twenty source-unique colours with a base-parallel replacement are excluded
from (5.6).  Their outside-base portal set does not meet that parallel seam,
so the forcing arc premise is false.  They require a different endpoint cover
or direct treatment and cannot be silently inserted into this canonical
outside-base separator.  They are not excluded from the general family of
Theorem 5.1.  Multi-source colours are also outside Theorem 5.3 because their
loss indicator is not the single linear profit `x[e(c)]`.

On the two strictness candidates, exact min-cut reproduces the three rows of
Theorem 5.2 and proves they are maximally violated within the canonical
portal-union subfamily of their palettes: violations are two lower and four
upper in both branches.

The scope-complete full cut/add model now includes these three deduplicated
rows in both locked-edge branches.  The signed candidate no-goods are not also
added, because the global Hall rows imply them on binary cut vectors.  The
logic-based Benders driver installs the same three eager rows and, at every
integral cut-master incumbent, runs (5.6) in both palettes.  Any violated
canonical row is normalized, semantically replayed, added to the master and
checkpointed before the seam subproblem is called.  Resume rows are rebuilt
from their colour sets, portal unions and endpoint coefficients before use.
The standalone rational separator supplies the same operation for later
integral or fractional cut-master points without invoking the seam solver.

### Theorem 5.4 (joint double-repair hypergraph-cover row)

Let `C_L,C_U` be the 675 lower and 673 upper source-unique colours, and let
`e(c)` be the unique source provider of `c`.  Every loopless off-source seam
`a` whose two colours lie in these sets gives the four-resource hyperedge

```text
H_a={lower(a),upper(a),node_u(a),node_v(a)}.          (5.8)
```

The frozen catalogue has 20,787 such seam IDs.  Sixteen pairs have the same
four resource labels, leaving 20,771 distinct signatures; seam IDs remain
distinct in completion and matching semantics.

Put

```text
L(x)=sum_(c in C_L)x[e(c)],
U(x)=sum_(c in C_U)x[e(c)],
d_x(v)=sum_(h in F)incidence(v,h)x[h].               (5.9)
```

Let nonnegative weights `alpha_c,beta_c,gamma_v` cover every hyperedge:

```text
alpha_lower(a)+beta_upper(a)+gamma_node_u(a)+gamma_node_v(a) >= 1
                                                        for every a. (5.10)
```

Then every fractional degree/q1 completion with
`r=sum_(h in F)x[h]` additions satisfies

```text
sum_c alpha_c x[e(c)] + sum_c beta_c x[e(c)]
 + sum_v gamma_v d_x(v) >= L(x)+U(x)-r.              (5.11)
```

On the exact radius-99 face this is a fixed linear Benders row with constant
99.

#### Proof

For an integral completion, choose one added witness for every lost unique
lower colour and one for every lost unique upper colour.  The two witness
sets have sizes `L(x),U(x)` inside the same `r` additions, so their
intersection has size at least `L(x)+U(x)-r`.  Its seams have distinct lower
labels, distinct upper labels, and endpoint usage at most `d_x(v)`.  Summing
(5.10) over that intersection proves (5.11).

For a fractional completion, allocate lower witness mass `p_a` and upper
witness mass `q_a` inside the selected addition mass `y_a`, with totals
`L(x),U(x)` and `0<=p_a,q_a<=y_a`.  Set
`z_a=max(0,p_a+q_a-y_a)`.  Then

```text
sum_a z_a >= L(x)+U(x)-sum_a y_a=L(x)+U(x)-r,
```

while every lower, upper and endpoint `z`-load is bounded by the corresponding
capacity in (5.11).  Another sum of (5.10) proves the fractional claim.  ∎

For an integral cover `(A,B,N)`, the coefficient of source edge `h` in the
radius-99 row is exactly

```text
1[e_L(h) in A] + 1[e_U(h) in B]
 + sum_(v in N)incidence(v,h)
 - 1[h is lower-unique] - 1[h is upper-unique].      (5.12)
```

Endpoint incidence, not endpoint support, is required.  Thus coefficients
may be `-2,-1,0,1,2`, and parallel catalogue seam IDs must not be collapsed
in completion or packing constraints.

The permanent solver-free replay gives two full covers:

- retain: `L=69,U=74`, demand 44, cover cost `4+15+11=30`, hence the displayed
  row has deficit 14;
- delete: `L=69,U=72`, demand 42, cover cost `3+27+9=39`, hence deficit 3.

They cover all 20,787 seam IDs and reject the two cuts surviving canonical
same-palette closure.  The retain and delete rows have respectively 835 and
834 nonzero source coefficients, with canonical row hashes
`bb80fed7f3f405796014273cb41b606ccc16b56fd68aef799ec51f1e7c819645`
and
`21961e6fbc43310f53a6cddab26450f08ab1c8bae447c3afeabddaa70b0d5b1f`.

The replay proves feasible covers, not minimum-cover optimality.  Therefore
14 and 3 are exact margins of these two rows and only lower bounds on the
maximum possible integral-cover deficits.  Minimum integral cover is a
four-partite hypergraph vertex-cover ILP, not a min-cut theorem and not the
exact integral-matching dual.  Allowing fractional cover weights in (5.10)
instead gives a polynomial LP whose optimum is the exact dual of the
fractional double-matching relaxation and can only strengthen separation.

In the production Benders master, all 20,787 binary double-seam variables,
both colour-capacity families, all endpoint-capacity rows and
`sum y>=L+U-99` are already present.  Summing those rows over any cover proves
(5.11), even in the master's LP relaxation.  Hence the two eager rows are
valid projected/presolve certificates but do not strengthen that lifted
master, and a per-incumbent joint-cover solve there would be redundant.  The
cut-only CEGAR master now starts with the branch's audited row and performs a
fail-closed weighted-cover threshold separation before accepting a new cut.
Same-palette Hall remains installed: rejection of these two candidates proves
no logical domination in the reverse direction, and joint domination of the
same-palette family is also unproved.

Even the complete same-palette family (5.1) is not automatically sufficient
for (2.2)--(2.4).  Lower and upper rows share seam variables, binary
edge-selection can have odd-set obstructions, and exact degree equality also
contains lower-demand constraints.  A complete theorem would need the full
integer coloured-b-factor projection, not only endpoint-cover Hall rows.

## 6. General proof-safe feature-core Benders theorem

The following theorem is the exact fallback once a master cut satisfies all
static portal rows.

For every node `v` and threshold `t in {0,1,2}`, define master predicates

```text
G_ge(v,t;D) = 1[b_v(D)>=t],
G_le(v,t;D) = 1[b_v(D)<=t].
```

For every q1 colour define `L_c(D)=lost_c(D)` from (2.1).  Associate the seam
feature rows

```text
G_ge(v,t):  deg_y(v)>=t,
G_le(v,t):  deg_y(v)<=t,
L_c:        y(provider seams of c)>=1.               (6.1)
```

### Theorem 6.1 (replayed feature-core cut)

Let `K` be any set of features from (6.1).  If the hard row (2.2) together
with exactly the rows in `K` is infeasible, then every radius-99 source cut
obeys

```text
sum_{(v,t) in K_ge} G_ge(v,t;D)
+ sum_{(v,t) in K_le} G_le(v,t;D)
+ sum_{c in K_q1} L_c(D)
   <= |K|-1.                                          (6.2)
```

#### Proof

Suppose a cut violates (6.2), so every listed predicate equals one.  Any exact
seam completion for that cut satisfies each corresponding fixed feature row
in (6.1), as well as (2.2).  It would therefore be a feasible point of the
infeasible core subsystem, a contradiction.  ∎

Splitting endpoint equalities into upper and lower half-rows is essential for
the strongest generalization.  A lower core row with RHS `t` remains implied
when a future cut has `b_v>=t`; an upper core row remains implied when it has
`b_v<=t`.  An equality core would apply only at the exact same endpoint RHS.

### Exact master channeling

Because the source is degree two, introduce one-hot variables
`d_(v,0),d_(v,1),d_(v,2)` with

```text
d_(v,0)+d_(v,1)+d_(v,2)=1,
sum_{source e incident v} cut[e]=d_(v,1)+2d_(v,2).
```

Then

```text
G_ge(v,t)=sum_{s=t}^2 d_(v,s),
G_le(v,t)=sum_{s=0}^t d_(v,s).
```

For a colour with source-provider set `S_c`, channel `L_c` by

```text
L_c <= cut[e]                          for e in S_c,
L_c >= sum_{e in S_c}cut[e]-|S_c|+1.                 (6.3)
```

Equations (6.2)--(6.3) give an ordinary exact master inequality.  No q1
provider halo is assumed.

### Raw cut-literal fallback

If a fixed cut `D` is replayed infeasible but no feature core is accepted,
the radius-99 master may always add

```text
sum_{e in D} cut[e] <= 98.                            (6.4)
```

More generally, a replayed signed cut-literal core `C^+,C^-` gives

```text
sum_{e in C^+}cut[e]-sum_{e in C^-}cut[e] <= |C^+|-1. (6.5)
```

Literal polarity must be decoded through an explicit registry; applying
`abs()` to CP-SAT literal references is unsound.

## 7. Proof-safe extraction protocol

The permanent generic driver
`scratch/extract_k16_r99_fixed_cut_seam_core_20260729.py` implements the
following contract.

1. Recompute all 858 endpoint RHS values and all exact lost q1 rows, including
   multi-source colours.
2. Keep the full global 26,570-seam bank.  Pruning to positive-demand nodes is
   valid for the fixed solve but invalid for generalized core minimization,
   because dropping a zero-degree feature must re-enable those seams.
3. Keep `sum y=99` hard.  Give every nontrivial degree lower half-row, every
   degree upper half-row, and every exact lost-colour row a distinct positive
   assumption guard.
4. For a non-build solve, require and hash an exported model proto; store the
   complete positive assumption registry, raw returned literal references,
   OR-Tools version and response summaries.
5. Accept a solver-returned sufficient core only after rebuilding a fresh
   model with exactly those positive assumptions and replaying it
   `INFEASIBLE`.
6. During deletion minimization:

   - `INFEASIBLE` removes the feature;
   - `FEASIBLE/OPTIMAL` retains it and stores a solver-free-checked 99-seam
     witness;
   - `UNKNOWN` retains it provisionally and proves nothing;
   - `MODEL_INVALID` is fatal.

7. Call the final core subset-minimal only when the final core replays
   infeasible and every final core-minus-one model has a checked feasible seam
   witness whose complete 99-edge seam list is stored.
8. Emit (6.2) only after the final infeasible replay.  Always retain the exact
   incumbent fallback (6.4) after that same replay; emit neither cut on
   `FEASIBLE`, `UNKNOWN`, or `MODEL_INVALID`.

The honest CP statuses are

```text
FIXED_CUT_DEGREE_Q1_FEASIBLE,
TRUSTED_CP_INFEASIBLE_SUFFICIENT_CORE,
TRUSTED_CP_INFEASIBLE_SUBSET_MINIMAL_CORE,
UNKNOWN,
MODEL_INVALID.
```

A replayed CP core is trusted-solver evidence, not an independently checked
proof log.  The critical core in Section 3 is stronger: its infeasibility and
minimality are both solver-free.

## 8. Artifacts and exact boundary

The pre-existing full portal audit is

```text
scratch/audit_ad_k16_r99_unique_colour_portal_rows_20260729.py
  SHA 3caeddddd667926cbec1380cfe1915194825a942441bfbaebfb28024dc149164

scratch/ad_k16_r99_unique_colour_portal_rows_20260729.audit.json
  SHA 37ff50044cd1b844060d95c3d4c1e3c41a0dc53285affbe2ea02660e7487b7cc
```

The new solver-free minimal-core replay is

```text
scratch/audit_k16_r99_critical_portal_benders_core_20260729.py
  SHA efd337ea9d26a84a179e115c25029723f0e34e2bd53300df338eabee790fe56b

scratch/k16_r99_critical_portal_benders_core_20260729.audit.json
  SHA 9bf97cdbbecabddf042dc506ae87543f3a4ba5de50dfe782948549416c9082e7
  embedded payload SHA 8189dd5c978709ebb098112542a50f5b2f95493fbac23d17b9120a1452f573e4
```

The exhaustive size-at-most-two grouped endpoint screen is

```text
scratch/audit_k16_r99_fixed_cut_small_endpoint_hall_20260729.py
  SHA 1d4786a82765c17726af203c6dcd7a141797a3440236398dc02e6252d045a97a

scratch/k16_r99_fixed_cut_small_endpoint_hall_20260729.audit.json
  SHA 333501eca2fca68ea4f9d1f3ff77b37eee2f5f11287997abfd29352414c3601b
```

The exact level-2 strictness certificate is

```text
scratch/audit_k16_r99_portal_hall_strictness_20260729.py
  SHA 4a766217bf8f2d20e8204f0d4e14e7f0cf592f1dfb966871dfc623dea50f7fab

scratch/k16_r99_portal_hall_strictness_20260729.audit.json
  SHA 685a6e080a27822a5142382062dd1b6470bf77de4631b2a55dbb00f2d95b6e0e
  embedded payload SHA 83b3f6bd4aa59aee693ec9c9d605e4fb9d94205df33e212e8385dabbaba13267
```

The exact max-closure separator and its replay are

```text
scratch/separate_k16_r99_same_palette_portal_hall_20260729.py
  SHA b57f38cb39b2bf6bd1923653a91c0c430a44e15f8c9f7bfe199cdb6181c1cb48

scratch/k16_r99_same_palette_portal_hall_maxclosure_20260729.audit.json
  SHA e779f2e37aa1bfcfe85e5feb3b1efd22986981184917e3a3f3138c5c2bd17b85
  embedded payload SHA 4bf5e46f21a346af8b3533550fe6b053f54fe2796425f99975248eaaeee3bffa
```

The strengthened full master is

```text
scratch/search_ad_k16_recenter_r99_scope_complete_20260729.py
  SHA e2208a1666b3dc20bfd4fd17edd4979d3774347a314cab8dab80e3b45d07f00d
```

The logic-based cut-master integration is

```text
scratch/solve_k16_r99_cut_add_benders_cegar_20260729.py
  SHA 5f700eeca6b36385378c5a6595ab7838b67606e1cdf2215dcc46c0c1b02c4e84
```

It was statically compiled and its closure routine was replayed locally on
the two strictness cuts, reproducing the three row hashes and margins `2,4`.
No CP-SAT solve was launched.

The generic H100-CPU-only extractor is

```text
scratch/extract_k16_r99_fixed_cut_seam_core_20260729.py
  SHA 6b0127acfd676bda858a36954a4f2f2cdb486c4d4d2e6050e579b04d623b3418
```

It has been statically compiled but not solved in this turn because no H100
headroom was available; the machine remains under the explicit memory freeze.
The exact achieved boundary is therefore:

- all 29 present high-slack fixed cuts: solver-free excluded by one minimal
  portal core;
- all 1,328 fixed-source, source-unique-colour singleton portal rows: proved
  and ready for the r99 master;
- two explicit first-order-portal-feasible cuts, one in each branch: excluded
  by three deduplicated level-2 Hall rows;
- all canonical source-unique, nonparallel portal-union rows: polynomially
  and exactly separable by rational min-cut, including fractional master
  points;
- arbitrary endpoint-cover rows, base-parallel colours and multi-source loss
  indicators: not covered by that min-cut theorem;
- sufficiency of all same-palette rows for the two-palette binary degree-exact
  seam problem: not proved and not implied by the closure theorem;
- next canonical-portal-union-feasible incumbent: either run the full
  source-unique endpoint-cover model (5.7), or pass directly to the exact
  fixed-cut feature core (6.2) before trusted CP fallback.
