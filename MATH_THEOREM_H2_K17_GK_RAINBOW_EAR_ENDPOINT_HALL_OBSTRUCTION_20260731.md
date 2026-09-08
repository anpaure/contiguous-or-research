# Supported-ear Hall obstruction and the cut gate for the `k=17` GK forest

Date: 2026-07-31  
Status: exact finite Hall **NO-GO** for arbitrary-length ears on the
immutable authenticated GK forest; solver-free short certificate for the
ledger `(4024,905,252,42)`; exact necessary cut-and-ear gate.  No `k=17`
word or no-go for a cut/rethreaded forest is claimed.

## 0. Outcome

Let `F` be the authenticated two-cut Greene--Kleitman path forest on
rank-seven subsets of `[17]`.  It has `5224` components and `10448`
degree-one vertices.  Form the complete local edge/wedge catalogue on the
old endpoints and the `4072` unused rank-seven vertices, then monotonically
peel every edge which lacks a surviving turn wedge at an unused endpoint.
Every valid ear family is a post-fixed point and therefore survives this
peel.

In the greatest supported catalogue, connect a missing rank-six colour to
the fresh rank-eight union of each surviving carrier edge.  A global
rank-eight-rainbow completion would induce a matching saturating all
`2224` missing colours.  Exact replay instead gives

\[
\begin{array}{c|c}
\text{provider matching rank}&1780/2224\cr
\text{deficiency}&444\cr
\text{zero provider rows}&416\cr
\text{DM Hall witness}&584\text{ rows versus }140\text{ unions}.
\end{array}                                                   \tag{0.0}
\]

Hence **no arbitrary-length locally clean ear completion exists on the
immutable forest**, even before endpoint topology and global rank-nine
collisions.  Cutting old edges changes the endpoint set and all three
palettes, so it is outside this no-go and is the live branch.

There is also a short solver-free subcertificate.  Among the `2224`
missing rank-six colours, exactly `674` have no rank-seven superset among
the original degree-one vertices.

In the fixed-forest ear class, an ear of length `j` has the form

\[
                 e_0,u_1,\ldots,u_{j-1},e_j,        \tag{0.1}
\]

where `e_0,e_j` are original forest endpoints and every `u_i` is an
unused rank-seven vertex.  A colour with no endpoint superset can occur
only on one of the `j-2` internal edges `u_i u_{i+1}`.  Consequently every
valid fixed-forest ledger must satisfy

\[
             \boxed{\sum_{j\ge3}(j-2)x_j\ge674.}    \tag{0.2}
\]

The proposed corrected ledger gives only

\[
             252+2\cdot42=336<674.                 \tag{0.3}
\]

Thus that ledger has a literal Hall deficiency `338` before endpoint pairing,
rank-eight or rank-nine freshness, component topology, or Boolean-diamond
guards are considered.  The earlier `294` all-unused-colour split was a
strictly weaker projection and did not certify the displayed ledger.

## 1. Exact fixed-forest object

Write

* `E` for the `10448` degree-one vertices of `F`;
* `U` for the `4072` rank-seven vertices unused by `F`;
* `M` for the `2224` missing rank-six edge colours; and
* 
  \[
       M_0=\{c\in M:\text{ no }e\in E\text{ contains }c\}.
                                                               \tag{1.1}
  \]

The authenticated literal census gives

\[
                         |M_0|=674.                \tag{1.2}
\]

Consecutive vertices of an ear are Johnson-adjacent rank-seven sets.
Their edge colour is their unique rank-six intersection.  A selected ear
family is required to cover every colour in `M`, although other new edges
may repeat already used rank-six colours.

The qualifier *fixed forest* is load-bearing.  An old degree-two vertex
cannot be reused as an ear vertex without first deleting an old forest
edge.  Such cut-and-expose constructions are treated separately in
Section 6.

## 2. Greatest-supported-ear Hall theorem

The next reduction is independent of every proposed length ledger.

### Local catalogue

An allowed edge is a Johnson edge `vw` with `v,w in E union U` such that

1. its rank-eight union is outside the retained GK rank-eight palette;
2. every boundary turn forced when `v` or `w` lies in `E` is a rank-nine
   colour outside the retained GK rank-nine palette; and
3. an `E-E` edge does not join the two endpoints of the same GK component.

At `u in U`, an allowed wedge is a pair of allowed incident edges `uv,uw`
whose two rank-eight unions are distinct, whose turn `v union u union w`
is a fresh rank-nine colour, and whose local boundary/turn colours are
distinct.  These are all necessary local conditions; no global collision
or topology condition is imposed.

Starting with all allowed edges and wedges, repeat the following monotone
deletions:

* delete a wedge if either of its edges was deleted;
* delete an edge if one of its endpoints lies in `U` and no surviving
  wedge centred at that endpoint contains it.

Denote the greatest fixed point by `(A_infty,W_infty)`.

### Lemma 2.1 (post-fixed-point survival)

Every edge and every internal wedge of any locally clean family of
arbitrary-length ears `E-U^*-E` belongs to `(A_infty,W_infty)`.

#### Proof

Every selected edge satisfies the raw edge tests, and the two selected
edges at each internal unused vertex form an allowed wedge.  Thus the
selected edge/wedge pair is a post-fixed point of the support operator:
each of its wedges has both incident selected edges, and every selected
edge has its selected wedge at each unused endpoint.  A post-fixed point is
contained in every iterate starting from the full catalogue, by induction,
and hence in their greatest fixed point. \(\square\)

Let `B_infty` be the bipartite graph whose left side is the `2224` missing
rank-six colours and whose right side consists of fresh rank-eight colours.
Put `c q` in `B_infty` when `A_infty` contains an edge with intersection
`c` and union `q`.

### Theorem 2.2 (supported-ear Hall gate)

If the immutable GK forest has a locally clean ear completion covering all
missing rank-six colours with pairwise-distinct new rank-eight unions, then
`B_infty` has a matching saturating its complete left side.

#### Proof

Choose one selected carrier edge for each missing rank-six colour.  By
Lemma 2.1 each chosen edge survives the peel.  Its rank-eight union is
therefore a neighbour of that colour in `B_infty`.  Global rank-eight
injectivity makes these `2224` chosen unions distinct, giving the claimed
matching. \(\square\)

The exact catalogue has `148153` raw edges and `4217728` raw wedges.  Three
support rounds leave `145117` edges and `4194675` wedges.  Its provider
graph uses `6530` rank-eight resources and has the exact data in (0.0).
In particular, the Dulmage--Mendelsohn alternating set `S` satisfies

\[
                         |S|=584>140=|N(S)|.         \tag{2.1}
\]

Theorem 2.2 and (2.1) prove the arbitrary-length immutable-forest no-go.
The peel is deliberately a relaxation: it may retain mutually inconsistent
wedges, long unused cycles, repeated rank-nine colours and bad component
topology.  A Hall failure after those relaxations is therefore proof-safe.

## 3. The endpoint-free slot theorem

### Theorem 3.1

For any family of fixed-forest ears of the form (0.1), the number of
distinct colours from `M_0` that their new edges can carry is at most

\[
                         Q=\sum_{j\ge3}(j-2)x_j.     \tag{3.1}
\]

In particular, covering all missing rank-six colours requires (0.2).

### Proof

Let `vw` be a new ear edge whose rank-six intersection is `c in M_0`.
If `v in E`, then `v` is an original endpoint containing `c`, contrary to
the definition of `M_0`; the same holds for `w`.  Hence both ends of the
edge lie in `U`.  A length-`j` ear has precisely the internal edges

\[
                    u_1u_2,\ldots,u_{j-2}u_{j-1},   \tag{3.2}
\]

so it offers exactly `max(j-2,0)` eligible slots.  Every Johnson edge has
one rank-six intersection and therefore serves at most one distinct row
of `M_0`.  Summing over ears proves (3.1), and `Q>=|M_0|=674` follows.
\(\square\)

### Hall/Rado interpretation

Make one demand vertex for each colour of `M_0` and one provider vertex
for every internal--internal edge position in the chosen ear ledger.
Join a demand to a position only when some literal ear can place that
colour there.  Regardless of those literal menus, the complete demand
set has at most `Q` neighbours.  Hall's inequality for this one set is

\[
                         674\le Q.                  \tag{3.3}
\]

Equivalently, in the transversal-matroid projection the union of all
`M_0` menus has rank at most `Q`.  Thus (0.3) is already an exact Rado
rank failure.  No collision or topology relaxation can repair it.

## 4. Failure of the advertised four-length ledger

For

\[
                 (x_1,x_2,x_3,x_4)=(4024,905,252,42),            \tag{4.1}
\]

Theorem 3.1 gives

\[
               Q=x_3+2x_4=252+84=336.             \tag{4.2}
\]

Therefore the `M_0` row set alone has deficiency

\[
                         674-336=338.               \tag{4.3}
\]

This proves fixed-forest infeasibility of (4.1).  It does **not** say that
the `252` locally clean three-ear colours or `42` four-ear-only colours
were enumerated incorrectly.  It says that assigning one long ear only to
those `294` all-unused colours ignores the other `380` endpoint-free
colours, whose supersets may be old internal vertices but are not legal
uncut ear ports.

The label `corrected_minimal_ear_counts` in the existing audit JSON must
therefore be read only as the displayed local rebalance, not as a feasible
or proved-minimal global ledger.

## 5. The exact scalar repair cone

The final tail requires

\[
       S=\sum_{j\ge1}x_j=5223                        \tag{5.1}
\]

ears and

\[
       I=\sum_{j\ge1}(j-1)x_j=1535                  \tag{5.2}
\]

inserted rank-seven vertices.  Since every non-direct ear consumes at
least one inserted vertex,

\[
\begin{aligned}
 Q&=\sum_{j\ge3}(j-2)x_j\\
  &=I-\sum_{j\ge2}x_j\\
  &=I-(S-x_1)=x_1-3688.                             \tag{5.3}
\end{aligned}
\]

Combining (5.3) with Theorem 3.1 yields the necessary concentration law

\[
       \boxed{x_1\ge4362,\qquad \sum_{j\ge2}x_j\le861.}          \tag{5.4}
\]

For lengths at most four, equality in the endpoint-free cut is exactly

\[
\begin{aligned}
 x_1&=4362,\\
 x_3+2x_4&=674,\\
 x_2+x_3+x_4&=861.                                  \tag{5.5}
\end{aligned}

Writing `x_4=s`, the nonnegative integer solutions are

\[
       (x_1,x_2,x_3,x_4)
          =(4362,187+s,674-2s,s),\qquad0\le s\le337.             \tag{5.6}
\]

For example, retaining `42` four-edge ears gives the arithmetic ledger

\[
                         (4362,229,590,42).          \tag{5.7}
\]

Alternatively, retaining `252` three-edge ears gives

\[
                         (4362,398,252,211).         \tag{5.8}
\]

Neither (5.7) nor (5.8) is asserted locally fresh or simultaneously
selectable.  They are proof-safe next catalogues.  The local statement
that `42` colours have no clean three-edge provider also implies only
`x_4>=21` in a four-length global ledger: one four-edge ear has two
internal provider slots and might serve two such colours.

More generally put `d=x_3+2x_4`, the number of internal--internal slots,
and `q=x_4`.  Every nonnegative four-length ledger with the fixed values
`S=5223`, `I=1535` has the unique parametrization

\[
 (x_1,x_2,x_3,x_4)
   =(3688+d,\ 1535-2d+q,\ d-2q,\ q),               \tag{5.8a}
\]

where

\[
  674\le d\le1023,qquad
  \max(0,2d-1535)\le q\le\lfloor d/2\rfloor.       \tag{5.8b}
\]

The lower bound on `d` is Theorem 3.1; all other bounds in (5.8b) are
exactly nonnegativity of the four coordinates.  This is the complete
scalar four-length cone, not an existence theorem.

Importantly, every ledger satisfying (5.1)--(5.2) retains the scalar
totals

\[
       \sum_j jx_j=S+I=6758,\qquad
       \sum_j(j+1)x_j=2S+I=11981.                  \tag{5.9}
\]

Thus concentrating the same inserted vertices into fewer longer ears
repairs the endpoint-free capacity without changing the proposed word
length or the rank-eight/rank-nine counts.

## 6. The joint cut-and-ear ledger

Suppose `c` pairwise vertex-disjoint old edges are deleted before adding
ears.  Require both ends of every cut edge to have degree two in the seed,
and do not change any old rank-seven value.  Then the exact scalar ledger
is

\[
\begin{array}{c|c}
\text{quantity}&\text{after the cuts}\cr\hline
\text{seed components}&5224+c\cr
\text{seed edges}&10152-c\cr
\text{seed turns}&4928-2c\cr
\text{required new ears}&5223+c\cr
\text{new edges}&6758+c\cr
\text{new turns}&11981+2c.
\end{array}                                                   \tag{6.1}
\]

Indeed, each forest-edge deletion raises the component count by one.
Vertex-disjoint internal cuts have `2c` distinct degree-two ends, so they
delete exactly two old turns per cut.  With `I=1535` inserted vertices,
`A=5223+c` new ears contain `A+I=6758+c` edges.  An ear with `j` edges
creates `j+1` turns including its two boundary turns, so the new-turn count
is `2A+I=11981+2c`.  The total edge and turn counts remain `16910` and
`16909`, respectively.

Each cut releases at most two incidences at old vertices outside the
original endpoint set `E`.  Every new provider of a colour in `M_0` which
is not an inserted--inserted edge must consume at least one such released
incidence.  If

\[
                         D=\sum_{j\ge3}(j-2)x_j,     \tag{6.2}
\]

then the exact endpoint-free capacity cut is

\[
                         \boxed{D+2c\ge674.}        \tag{6.3}
\]

This bound is solver-independent but only necessary: it deliberately
credits every released incidence with a distinct useful colour.  For the
displayed ledger's `D=336`, it gives

\[
                         c\ge\left\lceil{338\over2}\right\rceil=169.
                                                               \tag{6.4}
\]

There is also an exact cut-cone identity.  Since

\[
 D=I-(A-x_1)=x_1-(3688+c),                          \tag{6.5}
\]

every four-length cut ledger has, with `q=x_4`,

\[
 (x_1,x_2,x_3,x_4)
  =(3688+c+D,\ 1535-2D+q,\ D-2q,\ q),              \tag{6.6}
\]

subject to (6.3) and nonnegativity.  Thus cuts and longer inserted chains
are quantitatively interchangeable only in this endpoint-free projection:
one extra internal--internal slot pays one demand, whereas one cut can pay
at most two.  Endpoint, fresh-palette and topology rows still have to be
replayed.  The bound does not apply to value-changing or genuinely nonflat
operations.

### Theorem 6.1 (joint cut/ear Hall gate)

For a fixed vertex-disjoint internal cut set `C`, `|C|=c`, let `F_C` be the
remaining forest.  Its endpoint set is the original `E` plus the `2c` cut
ends; its unused rank-seven set is still `U`.  Relative to `F_C`, there are

\[
       2224+c\text{ missing rank-six colours},\qquad
       10152-c\text{ retained rank-eight colours},\qquad
       4928-2c\text{ retained rank-nine colours}.               \tag{6.7}
\]

Build the allowed edge/wedge catalogue and greatest support fixed point
exactly as in Section 2, but with these cut-relative endpoints and palettes.
Let `B_C` be its missing-rank-six versus fresh-rank-eight provider graph.
Every cut-and-ear completion on this fixed cut set necessarily satisfies

\[
            \boxed{D+2c\ge674,\qquad \nu(B_C)=2224+c.}         \tag{6.8}
\]

where `nu` is bipartite matching rank.

#### Proof

The first inequality is (6.3).  The `c` deleted seed edges have distinct
rank-six intersections, so they add `c` rows to the original missing
palette.  Their distinct rank-eight unions leave the retained palette, and
the `2c` distinct endpoint turns leave the retained rank-nine palette,
giving (6.7).  Every valid new ear again forms a post-fixed edge/wedge
system.  Choosing one carrier edge for each of the `2224+c` missing colours
and using global rank-eight injectivity gives a matching of that order in
`B_C`, by the proof of Theorem 2.2. \(\square\)

Thus (6.8) is the exact first-stage joint cut/ear theorem: enumerate or
construct a cut set, rebuild only its supported provider graph, and reject
it before any full ear packing whenever either row fails.  Matching rank is
necessary, not sufficient; endpoint disjointness, global rank-nine
injectivity and the quotient spanning path remain downstream.

### Mixed endpoint/internal cuts

The frozen `312`-cut certificate is not in Theorem 6.1's pure internal-cut
face.  Write `a` for endpoint--internal cuts and `b` for
internal--internal cuts, all vertex-disjoint.  Then

\[
\begin{array}{c|c}
\text{quantity}&\text{value}\cr\hline
\text{cuts}&c=a+b\cr
\text{new isolated old vertices}&a\cr
\text{destroyed seed turns}&a+2b\cr
\text{seed components}&5224+a+b\cr
\text{seed edges}&10152-a-b\cr
\text{seed turns}&4928-a-2b\cr
\text{new edges}&6758+a+b\cr
\text{new turns}&11981+a+2b.
\end{array}                                                   \tag{6.9}
\]

Only the internal end of an endpoint--internal cut can newly carry a
colour of `M_0`; the isolated old endpoint still contains no such colour.
Thus the sharper exposure row is

\[
                         \boxed{D+a+2b\ge674.}       \tag{6.10}
\]

For this mixed residual forest, let `T_C` be its degree-one vertices and
`Z_C` its isolated old vertices.  Build local edges on
`T_C union Z_C union U`; require retained-neighbour boundary turns at
vertices of `T_C`, and turn wedges at every used vertex of `Z_C union U`.
The same support peel and carrier argument prove:

### Theorem 6.2 (mixed-cut supported Hall gate)

If a fixed mixed cut set `C` admits a rank-eight-rainbow path completion,
then its supported provider graph `B_C`, built with the mixed roles above,
has matching rank equal to the number of rank-six colours missing after
the cuts.

The frozen certificate has

\[
 (a,b)=(90,222),\quad a+b=312,\quad a+2b=534.       \tag{6.11}
\]

Hence it has `5536` seed components, `9840` retained edges, `4394`
retained turns, `2536` missing rank-six colours, `7070` new edges and
`12515` new turns.  Its `D=336` legacy ledger passes only the scalar row,
since `336+534=870`; the decisive test is the full matching rank in
Theorem 6.2.

## 7. Why the remaining gate is not ordinary matroid intersection

### Quantitative limits of black-box absorption

On the uncut scalar face the resource loads are sharply different:

\[
 {10446\over10448}\text{ endpoint ports},\qquad
 {1535\over4072}\text{ unused vertices},\qquad
 {6758\over14158}\text{ fresh rank-eight colours},\qquad
 {11981\over19382}\text{ fresh rank-nine colours}.             \tag{7.1}
\]

Thus a nibble could only be a bulk stage; the endpoint shore needs an
essentially exact absorber.

The raw `M_0` core has `9926` fresh unused--unused candidates, but they
touch only `1918` unused vertices.  Candidate degrees are `1..55`, unused
vertex load is at most `70`, and rank-eight load is at most `26`.  The
standard three-uniform rainbow-matching sufficient condition would demand
matching number greater than

\[
                         3(674-1)=2019,              \tag{7.2}
\]

whereas two unused vertices per core give the unconditional upper bound
`floor(1918/2)=959`.  Hence that black-box hypothesis cannot prove the
needed core.  This does not refute the real object: a longer ear may pair
two service edges through one degree-two unused centre.  Indeed the strict
cap-one core propagation forces `126` rows and then empties target `0x715`,
while, in the isolated rank-six/rank-eight core, degree-two selection
repairs the six-row obstruction with one shared centre.  Endpoint,
rank-nine and topology rows are not part of that repair.  Path-paired
service is load-bearing.

The slot inequality also sharpens topology.  Since `x_1>=4362`, at most
`861` joins are non-direct.  Deleting them from a putative quotient
Hamilton path leaves a spanning direct-ear linear forest with at most
`862` components.  Therefore the direct-ear component graph `G_1` must
satisfy

\[
                         \operatorname{pc}(G_1)\le862.           \tag{7.3}
\]

Here `pc` is the minimum number of vertex-disjoint paths in a spanning
path cover, with isolated vertices allowed as one-vertex paths.

Each GK component has two ports and each port has at most `70` Johnson
neighbours, so \(\Delta(G_1)\le140\); dense Dirac/Ore criteria are unavailable.
For the full compatibility graph `G`, every Hamilton-path witness also
forces, for nonempty proper component sets `S` and all vertex sets `X`,

\[
  1\le |\delta_H(S)|\le2\min(|S|,|S^c|),\qquad
  \operatorname{comp}(G-X)\le|X|+1.                \tag{7.4}
\]

These component cuts are separate from the supported-ear palette Hall cut.

On the uncut scalar relaxation, select `5223` quotient joins on the `5224`
GK components.  Original-port uniqueness gives quotient degree
at most two.  Graphic independence plus `5223` selected joins then forces
one spanning path.  This topology row is not a matroid: on five vertices,

\[
 A=\{12,23\},\qquad B=\{13,24,25\}                 \tag{7.5}
\]

are both linear forests with `|A|<|B|`, but `13` closes a triangle when
added to `A`, while `24` and `25` give vertex `2` degree three.  No element
of `B-A` augments `A`.

Moreover an ear packet simultaneously occupies endpoint ports, inserted
vertices, rank-eight colours and rank-nine colours.  These are several
overlapping partition systems, not one additional matroid.  Therefore a
generic two-matroid/Rado invocation cannot prove the complete tail.  A
positive theorem must exploit extra literal structure, for example a
private packet bank plus a separately certified component order, or a
robust absorber with explicit component-cut expansion.

## 8. Exact scope and next theorem target

Proved here:

1. the supported-edge/wedge survival theorem and the exact immutable-forest
   Hall no-go `1780/2224`, including the `584>140` DM witness;
2. the solver-free one-set inequality (0.2) and infeasibility of the exact
   fixed-forest ledger (4.1), with deficiency `338`;
3. the necessary replacement cone (5.4)--(5.8b);
4. the cut dimension ledger and optimistic lower bound (6.4); and
5. the reusable cut-relative Hall gate (6.8).

Still open:

* a cut set `C` for which both rows of (6.8) pass;
* literal clean-ear packing on such a cut/rethreaded forest;
* simultaneous endpoint/unused-vertex/rank-eight/rank-nine disjointness;
* a spanning component path;
* repeated rank-six Boolean-diamond guards;
* prefix completion, upper continuation, residence, and the compiler.

The immutable fixed-GK ear branch is closed for arbitrary lengths.  No
cut/rethreaded-fibre no-go, unrestricted `k=17` no-go, or length-`24313`
word is claimed.

## 9. Authenticated artifacts

The fail-closed compact catalogue generator is

```text
scratch/h2_audit_k17_gk_ear_compact_incidence_20260731.cpp
SHA-256 31ad0118b6da29f16c86800427f7c22ff4a24a9cf00cded4b9184e4d83b25cf1
```

Its H100 output contains the complete `2224`-row provider relation, zero
rows and DM lists:

```text
scratch/h2_k17_gk_ear_compact_incidence_20260731.audit.json
SHA-256 ff4eae65903fa0745d459354a38707b70140e28afcf2a2318533052f8e0dc63f
```

The independent relation/matching verifier is

```text
scratch/verify_h2_k17_gk_ear_compact_incidence_20260731.py
SHA-256 6eb6d56370bdc8978ddfe2b9f315840861a3b60745aafac37223622216db51f4

scratch/h2_k17_gk_ear_compact_incidence_20260731.verify.json
SHA-256 6e8154d6e24df7312506f182af5135c5c5583e9352d6e4f5ef2490525c03c924
canonical payload da1e6ba216f93859b4d93df756122f3d0ca1488843847930647bb3a1c56a5acf
```

It reconstructs the old rank-six/rank-eight palettes, checks every emitted
incidence literally, recomputes both codegree tables and a separate
Hopcroft--Karp matching, and verifies that the displayed `140` masks are
exactly the neighbourhood of the displayed `584` masks.  It verifies the
emitted peeled relation; soundness of the support peel is the mathematical
content of Lemma 2.1.

The separate cone/core quantitative audit is

```text
scratch/audit_h2_k17_gk_ear_hall_cone_20260731.py
SHA-256 586e10f2c4e12c67f15ac279c9636bb0bef9225aa7ad4a193803e1b6f39c1db8

scratch/h2_k17_gk_ear_hall_cone_20260731.audit.json
SHA-256 9bbde01129ed4302c6cc03ec5770f78014ec8da3c4cc6a851155660404f8a5dd
canonical payload cce49c3a957f6ec47c90be7068497f183976be11b4fd6868fee6a23937db115e
```
