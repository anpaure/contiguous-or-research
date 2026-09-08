# Proposed `k=17` two-zone Greene--Kleitman ear construction

Date: 2026-07-31  
Status: proposal under audit; no length-24313 word or proof is claimed.

**Audit correction.**  Sections 1--4 and the Greene--Kleitman seed census
have been independently verified, but the direct/two-edge schedule in
Section 5 is impossible.  Moreover, the first repair
`(4024,905,252,42)` is still insufficient: 674 missing rank-six colours have
no original endpoint superset, whereas that mix has only 336
internal--internal ear edges.  Exact local enumeration finds 266 of the 674
with clean three-edge ears, another 128 with clean four-edge ears, and 280
requiring longer ears, shared multi-colour ears, or cuts/reroutes.  No
corrected global ear schedule is yet certified.  A stronger Hall audit now
rules out *all* arbitrary-length ears on the immutable GK forest, so the
live version must cut/rethread that forest or replace it.  A 312-cut
exposure certificate exists, but its palette-safe ear completion is open;
see
`MATH_AUDIT_K17_TWO_ZONE_GK_FOREST_20260731.md`.

**Positive prefix update.**  A literal certificate now realizes all 2328
two-letter low blocks with distinct low targets and distinct rank-eight
unions.  After correcting the owner widths, the full rank-eight/rank-nine
gate is exactly two alternating paths in the middle-levels graph `M_17`
(prefix and tail) plus the two exceptional seam owners.  The remaining
prefix problem is the global occurrence-labelled rainbow path and endpoint
incidence, not the low-block inventory.

## 0. Target

For `k=17`,

\[
 B(17)=\binom{17}{8}+3=24313.
\]

The proposal writes a candidate word as `A=P T`, with

\[
 |P|=7401,\qquad |T|=16912.
\]

The selected-cell schedule has exactly `65535` cells for the `65535`
nonempty targets of ranks at most eight, so the proposed lower atlas is
necessarily bijective.

## 1. Exact lower-layer allocation

The layer sizes are

\[
 17,136,680,2380,6188,12376,19448,24310
\]

for ranks `1,...,8`.  Choose `4536` rank-five targets for the tail.

| physical cells | count | assigned targets |
|---|---:|---|
| `T` letters | 16912 | all 12376 rank-6 plus 4536 rank-5 |
| `DT` cells | 16911 | 16911 rank-7 |
| `D^2T` cells | 16910 | 16910 rank-8 |
| `P` letters | 7401 | all 3213 ranks 1--4 plus remaining 1652 rank-5 plus 2536 rank-7 |
| internal `DP` | 7400 | remaining 7400 rank-8 |
| seam `P|T` | 1 | final rank-7 |

The rank-7 and rank-8 counts close:

\[
 16911+2536+1=19448,\qquad 16910+7400=24310.
\]

## 2. Prefix normal form

The `4865=3213+1652` low targets are partitioned into `2328` two-letter
blocks and `209` singletons:

| two-letter block | count |
|---|---:|
| ranks `(3,5)`, disjoint | 680 |
| ranks `(4,5)`, intersection one | 972 |
| ranks `(4,4)`, disjoint | 676 |

Each two-letter block has rank-eight union.  The unused low targets are the
153 sets of ranks 1--2 and 56 rank-four sets.  Thus there are `2537` low
blocks and `2536` rank-seven separators, and

\[
 P=L_0,B_1,L_1,\ldots,B_{2536},L_{2536}.             \tag{2.1}
\]

The internal adjacent-pair cells comprise `2328` pairs internal to the
two-letter blocks and `5072` pairs adjoining separators, totalling `7400`.

### Lemma 2.1 (the un-ordered low block inventory exists)

The asserted `680+972+676` two-letter blocks and `209` singletons can be
chosen with no repeated low target.

#### Proof

First match every rank-three set to a disjoint rank-five set.  The relevant
bipartite graph has degrees

\[
 \binom{14}{5}=2002\quad\hbox{and}\quad\binom{12}{3}=220.
\]

Double-counting edges out of any left family gives Hall with factor
`2002/220>1`, so all 680 rank-three sets are matched, using 680 rank-five
sets.

Next take a matching of 676 edges in the disjointness graph on rank-four
sets.  Such a matching exists without a delicate factor theorem: in a
maximal matching the uncovered rank-four sets form an intersecting family,
of size at most `binom(16,3)=560` by Erdős--Ko--Rado.  Hence a maximal
matching has at least `(2380-560)/2=910` edges.  Keep any 676.  It consumes
1352 rank-four sets and leaves a family `U` of order 1028.

Join a rank-four set to a rank-five set when their intersection has size
one.  Before the first matching is deleted, its two degrees are

\[
 4\binom{13}{4}=2860\quad\hbox{and}\quad
 5\binom{12}{3}=1100.
\]

After deleting the 680 already used rank-five sets, every member of `U`
still has degree at least 2180.  Thus, for every `A subseteq U`,

\[
 2180|A|\le e(A,N(A))\le1100|N(A)|,
\]

so Hall saturates all 1028 members of `U`.  Retain any 972 matched pairs;
the other 56 rank-four sets are the required rank-four singletons.  Together
with all rank-one and rank-two targets they give `56+17+136=209`
singletons.  The used rank-five count is `680+972=1652`.  `square`

This lemma proves only the inventory.  It does not order the blocks or
control any adjacent union.

**Prefix completion gate.**  Order the low blocks and separators so that
all `7400` adjacent unions are the complementary rank-eight palette and the
`7401` prefix three-letter windows provide the complementary rank-nine
owners.

## 3. Literal Boolean diamond

Let `S` have rank five and `V` rank eight with `S subset V`; write
`V-S={g,x,y}`.  Choose ordered distinct `a,b in S`, and put

\[
 C=(S-\{a,b\})+g,\qquad R=C+\{a,x\},\qquad T=C+\{b,y\}. \tag{3.1}
\]

Then `R,S,T` have ranks `(6,5,6)`,

\[
 R\cap T=C,\quad R\cup S=V-y,\quad S\cup T=V-x,
 \quad R\cup S\cup T=V. \tag{3.2}
\]

The common intersection `R cap T=C` has rank four.  There are
`3*2*5*4=120` oriented realizations.  Replacing a boundary
rank-six anchor `R` by `R-r+z`, with `z notin V`, gives `6*9=54` possible
rank-nine guards on that side.

These are `54` distinct guard *letters*, but only `9` distinct rank-nine
owner colours: the resulting owner is `V+z`, independent of which of the
six elements of `R` was removed.  Thus the guard-letter multiplicity must
not be counted as `54` independent palette choices.

## 4. Two-cut Greene--Kleitman forest

For a rank-six binary word on 17 coordinates, let `p_0(C)` be the last
position attaining the maximum prefix sum in the ordinary cut, and let
`p_9(C)` be the corresponding pivot after cutting between coordinates 8
and 9.  When the pivots differ, put

\[
 B^-(C)=C+p_0(C),\qquad B^+(C)=C+p_9(C).             \tag{4.1}
\]

The proposal asserts:

1. both pivot maps are injective SCD upward maps;
2. `p_9(C)>=p_0(C)` whenever distinct, so the projected graph is a path
   forest under the sum-of-elements potential;
3. distinct edges have distinct rank-eight unions;
4. internal turns have distinct rank-nine unions.

Splitting into pieces of lengths 9 and 8, with `a` upsteps in the first,
the distinct-pivot condition is asserted to be

\[
 1\le m_1-(2a-9)-m_2\le4.                            \tag{4.2}
\]

With

\[
 g_{\ell,p}(m)=\binom{\ell}{p-m}-\binom{\ell}{p-m-1}, \tag{4.3}
\]

the contributions for `a=0,...,6` are asserted to be

\[
 8,232,1744,4384,3124,624,36,
\]

totalling `10152` nondegenerate edges.  The complete census is asserted to
be

| statistic | count |
|---|---:|
| edges | 10152 |
| used rank-7 vertices | 15376 |
| path components | 5224 |
| internal rank-9 turns | 4928 |

## 5. Original ear ledger (refuted by the audit)

Join the `5224` components using

\[
 3688\text{ direct one-edge joins},\qquad
 1535\text{ two-edge joins through unused rank-7 vertices}.      \tag{5.1}
\]

There are `5223` joins.  The final rank-seven path then has

\[
 15376+1535=16911\text{ vertices},
\]

and

\[
 10152+3688+2(1535)=16910\text{ edges}.              \tag{5.2}
\]

Among the `6758` new edges, use `2224` to introduce the missing rank-six
intersection colours.  The other `4534` repeated intersections carry
distinct rank-five source letters, while the two outer source cells carry
the remaining two, giving `4536` rank-five tail targets.

A direct join creates two new internal rank-nine turns and a two-edge join
creates three.  Hence

\[
 4928+2(3688)+3(1535)=16909.                          \tag{5.3}
\]

These scalar identities are correct, but the schedule is combinatorially
impossible: 674 missing rank-six colours have no original endpoint superset,
while a direct/two-edge ear has no internal--internal edge on which such a
colour can occur.  See the correction at the top and the audit.

## 6. Exact finite gates

### Tail rainbow ear-completion lemma

Choose either a variable-length no-cut ear schedule satisfying

\[
 \sum_jx_j=5223,qquad
 \sum_j(j-1)x_j=1535,qquad
 \sum_{j\ge3}(j-2)x_j\ge674,
\]

or a consistently rebalanced cut-and-reroute schedule, so that
simultaneously:

1. all `2224` missing rank-six colours occur on new edges;
2. the remaining `4534` repeated intersections support distinct designated
   rank-five targets via the Boolean diamond;
3. every new rank-eight edge union is fresh;
4. every new rank-nine internal-turn union is fresh;
5. no rank-seven vertex is repeated.

### Prefix alternating-block completion lemma

Choose/order the `2537` low blocks and `2536` rank-seven separators so the
`7400` adjacent unions are precisely the remaining rank-eight targets and
the `7401` prefix three-letter windows provide the remaining rank-nine
chronology.

### Upper continuation gate

After joining prefix, seam and tail, prove that longer contiguous unions
cover every rank `10,...,17`, or preserve and identify an independent upper
witness bank.

These three statements are open.  In particular, the exact scalar ledger
does not establish any of them.
