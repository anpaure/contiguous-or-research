# Audit of the Catalan two-rail switch against K15 and K16

Date: 2026-07-31  
Status: exact lightweight replay; no all-dimension existence claim

## 1. Scope

This note audits

```text
MATH_THEOREM_CATALAN_TWO_RAIL_RAINBOW_SWITCH_REDUCTION_20260731.md
```

against two authenticated finite objects:

1. the resident all-depth-complete K15 two-factor with cycle lengths
   `6390,45`; and
2. the endpoint-rerooted K16 carrier used in the exact K16 word.

The K15 replay verifies the **post-switch** rail ledger for every choice of
distinguished coordinate, but a local hosted-square test has eleven isolated
cross seams and proves that this particular factor is not the literal output
of the stated local switches.  The K16 replay shows that the exact K16
carrier is not itself the cap-two upper-union-floor rail for the proposed
K16-to-K17 recursion.  Neither fact settles existence of a different
Catalan rail package.

## 2. Exact switch ledger

Put

\[
 M=\binom{2m}{m},\qquad
 N=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname{Cat}_m.
\]

The switch reduction begins with an unmarked $U$-cycle on $N$
rank-$(m+1)$ sets and a marked cap-two $C$-cycle on $M$ rank-$m$ sets.  The
$U$-cycle has $N$ distinct lower colours and misses $K$ middle facets.  The
cap-two theorem gives the $C$-cycle an upper-**union** floor profile; its
full lower-intersection profile need not be a floor profile.

In each matched host block, choose one of the two $C$-edges to retain and
cut the other.  Cut the corresponding $K$ distinct $U$-edges.  The $2K$
replacement edges are containments.  For the switch indexed by an unused
facet $X$, their lower colours are exactly

\[
                              J_X,\quad X,            \tag{2.2}
\]

where $J_X$ is the colour of the removed $U$-edge.  Thus the final
degree-two factor has forced type counts

\[
 \boxed{
 U\!U=N-K,\qquad C\!C=M-K=N,\qquad U\!C=2K.}
                                                        \tag{2.3}
\]

The $N-K$ fixed unmatched $C$-edges and the $K$ retained one-of-two
$C$-edges must jointly give all $N$ marked lower colours once.  The
unmarked internal edges and containment seams then contribute

\[
              (N-K)+2K=N+K=M                           \tag{2.4}
\]

distinct unmarked lower colours.  This is the exact lower-rainbow ledger.
For a fixed host injection its additional condition is the one-of-two
matching

\[
 X\longmapsto (R_X,J_X),\qquad X\cap R_X              \tag{2.5}
\]

whose retained colours, together with the fixed unmatched colours, form the
complete marked palette, while the cut endpoints $J_X$ are distinct.  This
is exactly 2-SAT after the host injection is fixed: forbid an option outside
the residual palette and every pair sharing a retained colour or a cut
endpoint.  A pre-switch lower floor is only a stronger duplicate-cut
specialization, not a hypothesis of the revised local theorem.

The local proof in the reduction is sound.  Distinct $J_X$'s select
distinct $U$-edges.  Since the unused facets $X$ are disjoint from the
old seam-facet set, all inserted cross edges are distinct.  Adjacent
selected $U$-edges may share a vertex, but each removed incident edge is
replaced by one cross edge, so degree two is still preserved.

## 3. K15: the post-switch ledger is exact

Use the authenticated factor

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  from3_markov_s7_merge.components.json
SHA-256 f765d52aa68810af0e4897c6881f46ecf016b86394341a97f894dc6b53058151
```

Its defining candidate has SHA-256

```text
0c11aefbfe3a0661c457b48f0a7a82afacc6d02d4362e23e5d710bb799135555
```

and its two cyclic components have lengths $6390$ and $45$.  The
independent factor audit is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  from3_markov_s7_merge.independent.audit.json
SHA-256 c5f700aef824b93e257957c313a7395eb3d2512c773e6d434f08934ba93ac6f4.
```

Here $m=7$, so

\[
 (M,N,K)=(3432,3003,429).                              \tag{3.1}
\]

Fix any one of the fifteen coordinates as $z$.  Call a middle owner
$A$ if it avoids $z$, and $B$ if it contains $z$.  Direct replay gives
the same table for every $z$:

| quantity | exact value | switch prediction |
|---|---:|---:|
| $A$-vertices | 3003 | $N$ |
| $B$-vertices | 3432 | $M$ |
| internal $AA$ edges | 2574 | $N-K$ |
| internal $BB$ edges | 3003 | $M-K=N$ |
| cross edges | 858 | $2K$ |
| maximal $A$-fragments | 429 | $K$ |
| maximal $B$-fragments | 429 | $K$ |

All $6435$ edge intersections are distinct and are precisely all rank-seven
sets.  More specifically:

* the $3003$ $BB$-edge colours are exactly all rank-seven colours
  containing $z$;
* the $2574$ $AA$-edge colours and $858$ cross-edge colours are
  disjoint and together are exactly all $3432$ rank-seven colours avoiding
  $z$; and
* every cross edge is literally
  
  \[
       U\;--\;(z+X),\qquad X\subset U,                 \tag{3.2}
  \]
  
  so its lower colour is $X$.

Thus the K15 factor realizes the conclusion of the lower-rainbow switch
theorem, with exactly the Catalan number of fragments on each rail, for
every coordinate $z$.

There is an important scope boundary.  This does **not** exhibit the input
data $(C_i,U_i,\phi,R_X,J_X)$.  In particular, the artifact does not
provide cap-two rail completions or pair the $858$ final containment seams
into the $429$ local rectangles of the theorem.  The finite missing
interface is a coloured endpoint completion, not a count.

More exactly, necessary data for a reverse certificate inside the
local-switch architecture would choose endpoint matchings $D_A,D_B$ after
the cross seams are deleted, with all of the following properties:

1. adjoining $D_A$ and $D_B$ makes the two rails Hamilton cycles;
2. the $D_A$-colours are $K$ distinct members of the final cross palette;
3. $D_A\cup D_B\cup E_{AB}$ decomposes into $K$ hosted alternating
   four-cycles, in each of which one marked endpoint is the lower colour of
   the $D_A$-edge and the other is the unused facet $X$.

Necessity follows by reading the four edges in (3.1) or (3.2) of the switch
theorem.  These three conditions are not quite sufficient by themselves:
the completed marked rail must additionally have the cap-two block
alignment and union-floor profile.  In particular, the retained other edge
at each unused $X$ must meet the other seam facet of its host $U_i$.
With that fourth condition, orienting each hosted four-cycle recovers one
local switch and all the data $J_X,X,X\cap J_X$.  The hosted-square
condition is already strictly stronger than the verified post-switch
counts.

It can be tested before solving either endpoint matching.  Write a final
cross seam as

\[
                       e=(U,z+X),\qquad X\subset U.    \tag{3.3}
\]

If two seams $e=(U,z+X)$ and $f=(V,z+Y)$ came from one switch, then the
removed unmarked edge was $UV$ and its lower colour was the marked endpoint
on one of the two seams.  Hence necessarily

\[
             |U\cap V|=m,\qquad U\cap V\in\{X,Y\}.    \tag{3.4}
\]

Conversely, (3.4) is exactly the local hosted-square compatibility test:
the other marked endpoint is a distinct facet of its host and hence is
Johnson-adjacent to $U\cap V$.

For the authenticated K15 factor, the compatibility graph on the $858$
cross seams has $2225$ edges and degree histogram

\[
\begin{array}{c|rrrrrrrrrrrrrr}
\deg&0&1&2&3&4&5&6&7&8&9&10&11&12&13\\ \hline
\#&11&72&129&107&87&78&86&64&61&66&61&29&5&2.
\end{array}                                             \tag{3.5}
\]

The same histogram occurs for every one of the fifteen coordinates.  In
particular, eleven seams are isolated, so the seams cannot be partitioned
into the $K=429$ local pairs required by the theorem.  Thus this K15 factor
is an exact count-and-palette calibration but a rigorous **non-instance** of
the literal local-switch architecture for every choice of $z$.

The statement about two components is equally scoped.  Delete the final
cross edges and contract every maximal constant-$z$ run.  The large
physical cycle contains $852$ cross edges and the small cycle contains
$6$, for every $z$.  Hence this **post-switch** contracted graph is two
alternating cycles of lengths $852=2\cdot426$ and $6=2\cdot3$; equivalently,
the product of its two endpoint pairings has cycle type $(426)(3)$ rather
than $(429)$.  This follows from the final factor alone; it does not
identify either pre-switch rail.  It verifies the palette theorem but fails
the one-cycle conclusion of Corollary 4.1 if one attempts to regard it as a
completed switch package.

The main production audit additionally verifies minimum run four and zero
lower/upper holes at every depth.  Its SHA-256 is

```text
scratch/k15_fixed_matching_pbbs_resident_20260729/
  from3_markov_s7_merge.audit.json
d7359bdd1baf42858839c46ab19c4ec3d69d73ccb2b39db655e6e955d3b8af39.
```

The final child's upper-q1 load histogram is

\[
                         1^{3675}2^{1230}3^{100}.       \tag{3.6}
\]

This is not a contradiction: cap two concerns the **pre-switch marked
rail's upper-union colours**, not the complete child's upper palette after
the two rails are braided.

## 4. K16 to K17: the authenticated carrier is not the required rail

For $m=8$, the proposed K16-to-K17 switch has

\[
 (M,N,K)=(12870,11440,1430),                           \tag{4.1}
\]

and therefore requires the post-switch edge counts

\[
 UU=10010,\qquad CC=11440,\qquad UC=2860.             \tag{4.2}
\]

The required cyclic marked-rail **upper-union** floor is

\[
                         1^{10010}2^{1430}.             \tag{4.3}
\]

Now replay the authenticated endpoint-rerooted K16 carrier

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.
```

It is a Johnson path through all $12870$ rank-eight sets.  Both adjacent
palettes are complete, but their exact load profiles are

\[
\begin{array}{c|c}
\text{rank-seven intersections}&1^{10066}2^{1319}3^{55},\\
\text{rank-nine unions}&1^{10111}2^{1229}3^{100}.
\end{array}                                             \tag{4.4}
\]

The integrality-floor profile for either complete adjacent palette on a
$12869$-edge path would be

\[
                         1^{10011}2^{1429}.             \tag{4.5}
\]

Thus completeness of both adjacent palettes does not imply a floor profile.
The K16 path has genuine triple-loaded colours on both sides.  The
rank-nine union triples are decisive here: adding one closing edge cannot
remove them, so no one-edge closure of this fixed edge set can produce the
cap-two union profile (4.3).  The rank-seven intersection triples are not
an obstruction to the revised retained one-of-two theorem.  Independently,
the endpoints have symmetric difference six, intersection rank five and
union rank eleven, so they are not Johnson-adjacent.

Therefore the exact K16 certificate is **not** the marked cap-two rail
required by the K16-to-K17 rainbow-switch theorem.  This is not an
obstruction to a different cap-two rail: the Catalan compression theorem
constructs another union-floor cycle, and the open condition is to choose
its retained one-of-two intersection colours and endpoint permutation
compatibly.

## 5. Exact remaining finite interface

The calibration isolates three logically separate layers.

1. **Post-switch arithmetic.**  K15 proves that the forced Catalan counts
   and the complete lower palette can occur together, uniformly in the
   distinguished coordinate.  Its eleven isolated seams simultaneously
   prove that those marginal facts do not force a decomposition into local
   hosted switches.
2. **Pre-switch rainbow completion.**  For the hosted subfamily one must
   construct the saturating $U$-cycle, cap-two union-floor $C$-cycle and the
   retained one-of-two matching (2.5).  Neither the K15 nor K16
   authenticated package supplies this data.  The broader endpoint-
   complement theorem does not require hosted squares.
3. **Protected chronology.**  The fragment permutation, all-depth witnesses,
   residence and common-cap compiler must be controlled.  K15 shows that a
   two-component all-depth-complete output is possible; it does not prove
   that the local switches themselves preserve those witnesses.

Consequently the Catalan two-rail theorem is a genuine sharpening of the
global component package, but it is not yet recursive.  Its smallest live
all-$m$ lemma is the simultaneous host/intersection rainbow matching plus
protected endpoint permutation, not a scalar seam bound.

## 6. Reproducer

The independent replay is

```text
scratch/audit_k_catalan_two_rail_k15_k16_anatomy_20260731.py
SHA-256 515940f8fd534f5f76ceec7aa511b439cd0b2199225ca573619a14c480af665f
```

and its frozen output is

```text
scratch/k_catalan_two_rail_k15_k16_anatomy_20260731.audit.json
SHA-256 602f14b8d23c7b0d06e39965a499cd496ce1145446a748d12e6a9122b5717eb4.
```

The script performs no search.  It reconstructs every physical edge,
checks the complete rank palettes, verifies containment of every cross seam,
and recomputes the two K16 load histograms and endpoint ranks.
