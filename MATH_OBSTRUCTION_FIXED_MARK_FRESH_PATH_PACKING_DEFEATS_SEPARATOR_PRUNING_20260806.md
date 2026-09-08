# A near-complete fresh-path packing can have a macroscopic two-mark orientation trap

**Date:** 2026-08-06  
**Method:** a codimension-eight Johnson slice and the spectral fresh-path
packing theorem; no computation or search  
**Status:** unconditional sharp obstruction to post-hoc hotspot pruning.
The existing spectral theorem permits a near-complete packing in which,
under either orientation of every block, a constant fraction of all blocks
have their second insertion label in one fixed two-coordinate set.  Any
distribution supported on owner lifts of those retained blocks has a
one-mark atom of order `1/d`, whereas the companion cylinder requires order
`1/d^3`.  Deletion-only repair to the correct scale costs `Theta(M)` lower
vertices, not the available `O(M/d)` separator leave.  This does not
obstruct a jointly constructed mark-balanced packing.

## 1. Parameters and orientation

Put

\[
 r=\lceil k/2\rceil,\qquad t=r-d,\qquad
 \mathcal L={ [k]\choose t},\qquad M=|\mathcal L|,          \tag{1.1}
\]

where `d` tends to infinity and `d^2<=k`.  A fresh `d`-path is an oriented
sequence

\[
                         S_0,S_1,\ldots,S_{d-1}              \tag{1.2}
\]

with

\[
                         S_j=S_{j-1}-a_j+b_j                \tag{1.3}
\]

and all `2(d-1)` event labels distinct.  Its forward second insertion is
`b_2`.  Under the reverse orientation, the second insertion is the old
deletion label

\[
                         a_{d-2}.                            \tag{1.4}
\]

Fix eight distinct coordinates

\[
                         z,c,w,x,e,u,v,y\in[k].             \tag{1.5}
\]

## 2. A packed middle slice

Consider

\[
 \mathcal U={S\in\mathcal L:
       \{z,c,w,x\}\subseteq S,
       \{e,u,v,y\}\cap S=\varnothing\}.                  \tag{2.1}
\]

Deleting these eight fixed coordinates identifies `U` with

\[
                         { [k-8]\choose t-4}.               \tag{2.2}
\]

Apply the fresh-path packing theorem on this smaller ground set with path
length `d-4`.  Its central-range hypotheses hold for all sufficiently large
parameters.  We obtain pairwise vertex-disjoint fresh middle paths

\[
                         S_2,S_3,\ldots,S_{d-3}              \tag{2.3}
\]

covering all but fewer than `30|U|/(d-4)` vertices of `U`.  Let `Q` be the
number of middle paths.  Since

\[
 { |\mathcal U|\over M}
 ={(t)_4(k-t)_4\over(k)_8}=\Theta(1),                      \tag{2.4}
\]

we have

\[
                         Q=\Theta(M/d).                     \tag{2.5}
\]

All event labels internal to a middle path lie outside the eight fixed
coordinates and are mutually distinct.

## 3. Deterministic fresh collars

For every middle path, prepend

\[
 \begin{aligned}
 S_1&=S_2-z+u,\\
 S_0&=S_1-c+e,
 \end{aligned}                                             \tag{3.1}
\]

and append

\[
 \begin{aligned}
 S_{d-2}&=S_{d-3}-w+v,\\
 S_{d-1}&=S_{d-2}-x+y.
 \end{aligned}                                             \tag{3.2}
\]

The four collar transitions are

\[
 \begin{aligned}
 S_0&\xrightarrow{-e,+c}S_1
      \xrightarrow{-u,+z}S_2,\\
 S_{d-3}&\xrightarrow{-w,+v}S_{d-2}
      \xrightarrow{-x,+y}S_{d-1}.
 \end{aligned}                                             \tag{3.3}
\]

The resulting completed paths are pairwise vertex-disjoint.  Their five
role regions have the following distinct signatures on the fixed
coordinates:

\[
\begin{array}{c|c|c}
\text{region}&\text{present}&\text{absent}\\ \hline
S_0&e,u,w,x&z,c,v,y\\
S_1&c,u,w,x&z,e,v,y\\
S_2,\ldots,S_{d-3}&z,c,w,x&e,u,v,y\\
S_{d-2}&z,c,v,x&e,u,w,y\\
S_{d-1}&z,c,v,y&e,u,w,x.
\end{array}                                                \tag{3.4}
\]

Thus vertices from different regions cannot coincide.  Within the middle
regions they were already disjoint; on each outer region the maps in
(3.1)--(3.2) are injective.

Every completed path is fresh.  Its collar event labels are the eight
distinct labels in (1.5), while the middle event labels avoid all eight.
In particular,

\[
                         b_2=z,qquad a_{d-2}=w.             \tag{3.5}
\]

By (1.4), reversing the completed path changes its second insertion label
from `z` to `w`.

### Theorem 3.1 (orientation-robust two-mark trap)

There is a family of

\[
                         \Theta(M/d)                        \tag{3.6}
\]

pairwise vertex-disjoint fresh `d`-paths such that, under either orientation
chosen separately for each path, every second insertion label belongs to

\[
                         \{z,w\}.                           \tag{3.7}
\]

## 4. Extend it to a near-complete spectral packing

Starting from the family in Theorem 3.1, greedily add fresh `d`-paths on
the uncovered lower vertices.  Whenever at least `30M/d` vertices remain,
the spectral fresh-path lemma supplies another path.  Hence the process
ends with a fresh-path packing leaving fewer than

\[
                         30M/d                              \tag{4.1}
\]

lower vertices, while retaining all `Q=Theta(M/d)` trapped paths.

Thus the conclusion of the present near-complete packing theorem is
compatible with a constant fraction of all its blocks carrying their
second insertion mark in one fixed two-coordinate bank, even if orientation
is deferred until after the packing.

## 5. Separator-scale deletion cannot repair the mark cylinder

Now orient the retained paths arbitrarily and assign every path an `h=2`
or `h=3` punctured duplicate macro.  Every trapped path creates at least two
selected level-two occurrences whose second mark lies in `{z,w}`.

If only deletion is allowed after the lower packing has been frozen,
removing one block releases all `d` of its lower vertices.  An `O(M/d)`
lower separator can therefore delete only

\[
                         O(M/d^2)                            \tag{5.1}
\]

whole blocks.  It leaves `Theta(M/d)` trapped blocks.

Let `Y_(T,s)` indicate that the marked level-two occurrence `(T,s)` is
selected.  In every owner-disjoint lift of the retained packing,

\[
 \sum_{T\in{[k]\choose r}}
       \bigl(Y_{(T,z)}+Y_{(T,w)}\bigr)=\Theta(M/d).          \tag{5.2}
\]

Take expectations under an arbitrary distribution supported on such lifts.
Since `W=binom(k,r)=Theta(M)`, averaging (5.2) over the `2W` marked owners
shows that some pair `(T,s)`, `s in {z,w}`, satisfies

\[
                         \Pr(Y_{(T,s)}=1)=\Omega(1/d).       \tag{5.3}
\]

The required one-mark root intensity, even with any fixed allowed factor,
is

\[
 C\eta_*={C\over r(d+1)}=O(d^{-3}),                        \tag{5.4}
\]

because `r=Theta(d^2)`.  Equation (5.3) is larger by
`Omega(d^2)`.

Conversely, if every marked owner with second label in `{z,w}` is to have
probability at most (5.4), summing over the `2W` possibilities permits only

\[
                         O(W/d^3)=O(M/d^3)                  \tag{5.5}
\]

such retained marked occurrences in expectation.  Starting from
`Theta(M/d)` trapped blocks, deletion-only repair must therefore remove
`Theta(M/d)` blocks and release

\[
                         \Theta(M)                          \tag{5.6}
\]

lower vertices.

### Corollary 5.1 (no post-hoc separator pruning)

The marked-ratio regenerative extension cannot be obtained by:

1. taking an arbitrary near-complete packing supplied by the current
   spectral fresh-path theorem;
2. orienting its paths afterward;
3. deleting only `O(M/d)` lower vertices; and
4. choosing the owner tails afterward, however dependently.

The imbalance can be macroscopic before the owner choice begins.

## 6. Exact scope and next target

This is not an obstruction to a mark-balanced or kernel-balanced packing.
It shows that balance must be built into the lower path selection, or that
one must permit a global rethreading which replaces a positive fraction of
the frozen paths.  A deterministic hotspot-pruning lemma for **arbitrary**
spectral packings is false at separator scale.

The next viable lower theorem must select and orient the fresh paths while
enforcing

\[
 \#\{P:b_2(P)=s\}=O(M/(kd))=O(M/d^3)                       \tag{6.1}
\]

for every coordinate `s`, together with the finer owner-kernel marked
ratios.  The complete oriented fresh-path orbit has exactly this marginal;
the current maximal-packing proof does not preserve it.

## 7. Dependency

The only nontrivial input is the spectral fresh-path packing theorem in
`MATH_THEOREM_FRESH_JOHNSON_PATH_PACKING_AND_ALL_ORDER_RESIDUAL_20260805.md`,
applied once to the codimension-eight slice and once to extend the resulting
family.

