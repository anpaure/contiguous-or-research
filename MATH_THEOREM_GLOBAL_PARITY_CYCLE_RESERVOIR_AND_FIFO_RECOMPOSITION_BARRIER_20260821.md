# Global parity cycles: an exact central reservoir and the FIFO recomposition barrier

**Date:** 2026-08-21  
**Status:** the statements below are proved.  They identify a linear
global unordered switch reservoir after forgetting chronology, and they give exact
cycle and cut-complexity barriers to lifting that reservoir by sparse
tail-MTF switches.  They do **not** produce the missing common-path rounding:
the abstract paths constructed below need not satisfy FIFO, the tail floor,
or the other ranks in the matched parity.

## 1. Setup

Let

\[
 n=2m+1,\qquad
 \mathcal L={ [n]\choose m},\qquad
 \mathcal R={ [n]\choose {m+1}},\qquad
 |\mathcal L|=|\mathcal R|=W.
\]

The palette regime used in the fixed-endpoint statements is

\[
 H=\lceil\sqrt{n\log n}\rceil,\qquad
 K=\{m-H,\ldots,m+1+H\},\qquad
 f=m+H+2,\qquad d=n-f+1=m-H.                         \tag{1.0}
\]

Thus `|K|=2H+2=o(n)`, `d=n/2-o(n)`, and `d<=k<f` for
every `k in K`.

Suppose the central rank in the selected parity is `m`.  A selected
rank-`m` matching gives a family

\[
 \mathcal A\subseteq \mathcal L,\qquad |\mathcal A|=N=W-r, \tag{1.1}
\]

of distinct recorded targets, partitioned into the ordered decks of the
selected cores.  In the budget palette, `N=sa` and

\[
 r=W-N=o(W/n),\qquad s=o(W).                            \tag{1.2}
\]

Here `a` is the number of recorded positions in a core and `s` is the
number of cores.  Whenever bridge accounting is invoked, the exact
endpoint-restoring bridge length and the budget normalization are

\[
 R_{\rm br}=n^3+f^2=\Theta(n^3),\qquad
 s=\left\lfloor {W\over a+2R_{\rm br}}\right\rfloor,
 \qquad N=sa.                                          \tag{1.2a}
\]

For consecutive rank-`m` targets `A,A'`, their rank-`(m+1)` transition
color is

\[
 \lambda(AA')=A\cup A'.                               \tag{1.3}
\]

It is defined exactly when `AA'` is an edge of the Johnson graph `J(n,m)`.
The first color in each core is a boundary color involving its unrecorded
seed state.  Thus all but one color per core are labels of temporal Johnson
edges.

## 2. Hall deficiency is cycle rank plus a sublinear forest term

The following reformulation applies to every omitted rank `q`, not only the
central one.  For a slot set `I`, let `Gamma_q(I)` be the bipartite incidence
graph whose left vertices are the slots in `I`, whose right vertices are
the colors in `union_(i in I) U_(i,q)`, and whose edges are the observation
incidences `(i,T)`, `T in U_(i,q)`.  Band-simplicity gives
`|U_(i,q)|=a`, so this graph has no repeated edge from one slot to one color.
Let

\[
 g_q(I)=\text{number of connected components of }\Gamma_q(I)
\]

and let

\[
 \beta_q(I)=e(\Gamma_q(I))-v(\Gamma_q(I))+g_q(I)       \tag{2.1}
\]

be its cyclomatic number.

### Theorem 2.1 (exact cyclomatic Hall formula)

For every nonempty slot set `I`,

\[
 Q_q(I):=a|I|-\left|\bigcup_{i\in I}U_{i,q}\right|
 =\beta_q(I)+|I|-g_q(I).                              \tag{2.2}
\]

Consequently the colored-Hall deficiency from the parity reduction is

\[
 \delta_q=
 \max_{I\subseteq[s]}
 \left(
  \beta_q(I)+|I|-g_q(I)-\sum_{i\in I}h_{i,q}
 \right)_+.                                           \tag{2.3}
\]

The empty-set term in (2.3) is understood to be zero.

At the omitted middle rank, where `h_(i,m+1)=0`, duplicate mass is monotone
and hence

\[
 \delta_{m+1}=\beta_{m+1}([s])+s-g_{m+1}([s]).         \tag{2.4}
\]

In particular,

\[
 \beta_{m+1}([s])\le\delta_{m+1}
 \le\beta_{m+1}([s])+s.                               \tag{2.5}
\]

Thus tree-like cross-block overlaps cost at most `s=o(W)`.  A linear
central defect is, up to `o(W)`, exactly a linear cycle-space dimension.

#### Proof

The incidence graph has

\[
 e=a|I|,
 \qquad
 v=|I|+\left|\bigcup_{i\in I}U_{i,q}\right|.
\]

Substitution in (2.1) gives (2.2), and substitution of (2.2) in the exact
Hall formula gives (2.3).  At the central rank the maximum duplicate mass
is attained by all slots, giving (2.4).  Finally `1<=g<=s` gives (2.5).
\(\square\)

### Lemma 2.2 (one exact cycle-breaking move)

Suppose an observation incidence `(i,B)` lies on a cycle of
`Gamma_(m+1)([s])`.  If a valid path switch replaces that occurrence by a
color `B'` absent from the entire current deck, while leaving all other
incidences unchanged, then

\[
 \beta_{m+1}\mapsto\beta_{m+1}-1,
 \qquad
 \delta_{m+1}\mapsto\delta_{m+1}-1.                   \tag{2.6}
\]

#### Proof

Deleting an edge on a cycle does not change the component count and lowers
the cycle rank by one.  Its old color vertex remains incident to the rest of
that cycle.  Adding `(i,B')` adds one edge and one new leaf vertex, changing
neither the component count nor the cycle rank.  The color union grows by
one, so duplicate mass also falls by one.  \(\square\)

Deleting all `s` boundary incidences can lower cycle rank by at most `s`.
Therefore, when the central defect is `Theta(W)`, all but `o(W)` of its
cycle rank survives among the internal transition incidences.  Boundary
switches cannot hide the bulk obstruction.

## 3. The unordered central projection has a linear switch reservoir

Let `\mathcal B_n` be the middle-level inclusion graph with shores
`\mathcal L,\mathcal R`.
It is `(m+1)`-regular and bipartite.  Hence its edges decompose into
`m+1` perfect matchings.  Fix two edge-disjoint perfect matchings `F_1,F_2`.
For `B in \mathcal R`, write `alpha_j(B)` for the `m`-face matched to `B`
by `F_j`.
Then

\[
 e_B=\{\alpha_1(B),\alpha_2(B)\}                      \tag{3.1}
\]

is a Johnson edge and `lambda(e_B)=B`.

### Theorem 3.1 (degree-two distinct-color reservoir)

Let `\mathcal M subseteq \mathcal R` be any desired family of transition
colors.
At least

\[
 |\mathcal M|-2r                                      \tag{3.2}
\]

of its colors admit edges `e_B` having both endpoints in `\mathcal A`.
The resulting edges have pairwise distinct colors and maximum degree at
most two on `\mathcal A`.

In particular, if `\mathcal M` is a `Theta(W)` family of currently missing
central colors, then the selected central deck contains `Theta(W)`
non-temporal Johnson edges of those missing colors, arranged as a disjoint
union of paths and cycles of maximum degree two.

#### Proof

For each `j`, the map `alpha_j:\mathcal R->\mathcal L` is a bijection.
Therefore at most `r`
members of `\mathcal M` have `alpha_j(B)` outside `\mathcal A`.  Discarding
the exceptions for `j=1,2` loses at most `2r` colors.  The two endpoints in
(3.1) are distinct because the matchings are edge-disjoint.  Each
`A in \mathcal L` is used once by each perfect matching, so it is incident with at
most two retained edges.  Finally, the union of the endpoints of `e_B` is
exactly `B`, making the colors distinct.  \(\square\)

There is also a count which does not choose the two matchings.  A color
`B in \mathcal R` is unavailable in `J(n,m)[\mathcal A]` only if at most one of its
`m+1` faces lies in `\mathcal A`, and hence at least `m` of its faces lie in
`\mathcal L\setminus\mathcal A`.  Since every missing `m`-set has exactly
`m+1` supersets in `\mathcal R`, double counting gives

\[
 \#\{B:\lambda^{-1}(B)\cap E(J[\mathcal A])=\varnothing\}
 \le {m+1\over m}r.                                  \tag{3.3}
\]

Moreover, with `D_J=m(m+1)` the Johnson degree,

\[
 e(J(n,m)[\mathcal A])
 \ge {W D_J\over2}-rD_J.                              \tag{3.4}
\]

Thus in the budget palette the global deck has
`(1-o(1))Wm(m+1)/2` global induced Johnson edges (possibly including
same-slot chords) and misses only `o(W)` possible union colors.  The
scarcity of typical **within-slot** chords is not a scarcity of global
unordered edges.

There is a useful conditional cross-slot version.  If every selected
rank-`m` slot deck is chordless, then every non-temporal induced Johnson edge
is cross-slot.  There are exactly `N-s` internal temporal edges, so (3.4)
leaves at least

\[
 {W D_J\over2}-rD_J-(N-s)
 =(1-o(1)){Wm(m+1)\over2}                             \tag{3.5}
\]

cross-slot edges.  Under the same hypothesis, every edge supplied by
Theorem 3.1 for a currently missing color is cross-slot.  Without
chordlessness, Theorem 3.1 and (3.4) are global statements and do not by
themselves distinguish same-slot chords from cross-slot edges.

## 4. Abstract central recomposition is already exact

The Middle Levels theorem supplies a Hamilton cycle in `\mathcal B_n`.
Write it cyclically as

\[
 A_1,B_1,A_2,B_2,\ldots,A_W,B_W,A_1,                 \tag{4.1}
\]

where `B_j=A_j union A_(j+1)` and indices are cyclic.

### Theorem 4.1 (exact unqueued central path cover)

For every `\mathcal A subseteq \mathcal L` of size `N=W-r`, there is a collection of
at most `max(1,r)` abstract Johnson paths which

1. uses every vertex of `\mathcal A` exactly once;
2. has exactly `N` pairwise distinct rank-`(m+1)` colors after assigning one
   boundary color to each path; and
3. consequently has central Hall deficiency zero.

If paths are required to have at most `a` recorded vertices, they may be
split into at most

\[
 \left\lceil{N\over a}\right\rceil+\max(1,r)          \tag{4.2}
\]

paths without losing either distinctness assertion.

#### Proof

Delete from the cyclic order (4.1) every `A_j` outside `\mathcal A`.
The surviving `A` vertices occur in at most `r` nonempty cyclic runs when
`r>0`, and in one run when `r=0`.  Use each run, in its cyclic order, as a
Johnson path.  Its internal colors are the `B_j` between consecutive
surviving members of the run.  As its boundary color use the `B_j`
immediately preceding the first member of the run.  These are distinct
edges/colors of the Hamilton cycle.  A run with `b` vertices receives
`b-1` internal colors and one boundary color, so altogether the paths use
exactly `N` distinct colors.

Splitting a run between `A_j,A_(j+1)` simply turns `B_j` from an internal
color into the boundary color of the second piece.  Hence splitting loses
nothing, and summing the ceilings gives (4.2).  \(\square\)

In the budget parameters, (4.2) is at most `s+r+1`.  **If** these abstract
paths had legal tail-MTF lifts, the known exact two-sided bridges would cost
at most `2R_br(s+r+1)=o(W)`.  Indeed, writing
`W=s(a+2R_br)+rho` with `0<=rho<a+2R_br`, (1.2a) gives

\[
 r=2R_{\rm br}s+\rho
 <a+2R_{\rm br}+{2R_{\rm br}W\over a+2R_{\rm br}},
 \qquad a=e^{n/5+o(n)}.                               \tag{4.3}
\]

Together with `R_br=O(n^3)`, this bound makes each term in
`2R_br(s+r+1)` equal to `o(W)`.  The weaker asymptotic relations (1.2)
alone would not imply that bridge estimate.

Therefore neither global color supply, abstract cycle breaking, the number
of abstract components, nor endpoint restoration is the central obstacle.
Theorem 4.1 is not yet a palette construction: an arbitrary Middle Levels
path does not obey the sliding-window FIFO law.

## 5. Extensive edge change is necessary

Let `E_0` be the union of the internal temporal Johnson edges of the current
rank-`m` core traces, and let `E_1` be the analogous union after a global
recomposition which preserves the same central resource set `\mathcal A`.
Allow the new family to have `s_1` cores.

### Theorem 5.1 (new-color accounting)

The number of central colors covered after but not before the recomposition
is at most

\[
 |E_1\setminus E_0|+s_1.                              \tag{5.1}
\]

Consequently, lowering a central defect by `Delta` while preserving
`\mathcal A` requires

\[
 |E_1\setminus E_0|\ge\Delta-s_1.                    \tag{5.2}
\]

In particular, provided the recomposed family has an affordable number
`s_1=o(W)` of cores, an initial `Theta(W)` coupon defect cannot be repaired
by `o(W)` new temporal edges.  Under this same qualifier, a successful
chord-rich construction must use linearly many of its chords, not merely
contain them.

#### Proof

Every nonboundary color after the recomposition is `lambda(e)` for an edge
`e in E_1`.  If `e in E_0`, that color was already present before the
recomposition.  Thus only `E_1\setminus E_0` can supply new internal colors,
and the `s_1` boundary observations supply at most `s_1` further colors.
This proves (5.1), and support gain equals defect reduction when the total
number of observations is fixed.  \(\square\)

A useful special case is a trace-fragment recomposition.  Partition the old
ordered rank-`m` traces into `F` contiguous pieces, reverse and permute the
pieces arbitrarily, and join them into new paths on the same vertices.
Every internal undirected edge of a piece survives; only piece joins can be
new.  Hence

\[
 |E_1\setminus E_0|\le F,                              \tag{5.3}
\]

up to the harmless choice of whether `F` counts paths or joins.  Polynomially
many cuts per palette slot give `F=O(s n^C)=o(W)` for every fixed `C`, so
they cannot remove a linear cycle rank.  Dense global recomposition, on the
scale exhibited by Theorem 4.1, is necessary.

## 6. Exact FIFO gate

The obstruction to using Theorem 4.1 is visible directly in the edge
labels.  Orient an abstract Johnson path

\[
 A_0,A_1,\ldots,A_b
\]

and write

\[
 u_t=A_t\setminus A_{t-1},\qquad
 v_t=A_{t-1}\setminus A_t\qquad(1\le t\le b).         \tag{6.1}
\]

### Proposition 6.1 (exact central FIFO criterion)

Assume `b>=m`.  The path is the rank-`m` sliding-set trace of a word if and
only if

\[
 v_1,\ldots,v_m\text{ are distinct},\qquad
 A_0=\{v_1,\ldots,v_m\},                              \tag{6.2}
\]

and

\[
 v_t=u_{t-m}\qquad(m<t\le b).                         \tag{6.3}
\]

When these conditions hold, the underlying occurrence word is forced:
its initial chronological rank-`m` window is
`v_1,v_2,...,v_m`, and its later letters are `u_1,u_2,...,u_b`.

For a tail-MTF core with eligibility floor `f`, this forced word must in
addition have no repeated letter at a positive gap below `f`, including
across its seed boundary.  Once the full ordered `(f-1)`-history is fixed,
only

\[
 d=n-f+1                                                   \tag{6.4}
\]

of the `m(n-m)=m(m+1)` Johnson neighbors are legal successors.

#### Proof

For a genuine sliding word, the letter removed at transition `t` is the
letter added exactly `m` transitions earlier, which proves (6.3); during
the first `m` transitions the initial window is removed in chronological
order, proving (6.2).  Conversely, start with the chronological window in
(6.2) and append `u_1,u_2,...`.  Induction using (6.3) shows that transition
`t` removes exactly `v_t` and produces `A_t`.  This proves the equivalence
and uniqueness.

The tail-MTF legality condition is exactly the absence of equal access
letters at a positive time gap below `f`, equivalently with fewer than
`f-1` intervening occurrences.  A fixed ordered history forces
the removed member of the current `m`-set; the new letter may be any of the
`n-(f-1)=d` labels outside the last `f-1` occurrences.  The full Johnson
degree allows any of `m` removals and any of `m+1` additions, giving the
last comparison.  \(\square\)

Thus the degree-two reservoir of Theorem 3.1 and the paths of Theorem 4.1
are genuine middle-level switches but are not automatically tail-MTF
switches.  The equation `v_t=u_(t-m)` couples choices `m` steps apart, and
the eligibility floor imposes the fixed-history legality constraint as well.

## 7. Sparse cut-and-paste cannot supply the lift

There is a second, representation-free way to see how dense a successful
recomposition must be.  A **word-fragment recomposition** partitions the old
recorded core words into `F` nonempty contiguous fragments, uses each
fragment once, possibly reverses fragments, and concatenates them into new
core words.  Assume the resulting cores are legal; this assumption only
makes the conclusion stronger.

### Theorem 7.1 (collar localization)

At rank `k`, the multiset of new observations which were not old
observations has size at most

\[
 F(k-1).                                               \tag{7.1}
\]

The multiset symmetric difference between the old and new rank-`k` decks is
at most `2F(k-1)`.  In particular a word-fragment recomposition can newly
cover at most `Fm` central rank-`(m+1)` targets.  Repairing a
`Theta(W)` central defect therefore requires

\[
 F=\Omega(W/m).                                       \tag{7.2}
\]

#### Proof

Every length-`k` occurrence interval wholly contained in a fragment appears
with the same underlying set before and after recomposition; reversal does
not change that set.  The only unmatched new windows are those crossing a
new fragment boundary, and each fragment start is crossed by at most `k-1`
windows.  The identical statement for the old fragment boundaries gives
the symmetric-difference bound.  Taking `k=m+1` gives (7.2).  \(\square\)

Thus cross-slot tail swaps, alternating cycle exchanges, or rare-core
reorderings using only polynomially many long fragments per original block
have `o(W)` central mobility.  If every seam is isolated by the currently
proved exact bridge of length `R_br`, then (7.2) would cost at least

\[
 \Omega((W/m)R_{\rm br})=\Omega(Wn^2)                  \tag{7.3}
\]

physical steps.  Bridge-separated sparse switches therefore cannot be the
bulk mechanism.  A positive proof must directly build a dense
FIFO-compatible recomposition rather than simulate it by reset gadgets.

## 8. A dense common-endpoint backbone really does exist

The preceding barriers rule out sparse recomposition, but they leave one
natural escape: put a genuine fixed-endpoint switch every `Theta(n)` steps.
This is not obstructed by endpoint entropy.

Let `\mathcal T={T_f,...,T_n}` be the `d=n-f+1` tail-MTF generators.  A
generator word `w in \mathcal T^ell` acts on the positions by a permutation
`sigma(w) in S_n`, independently of the labels in the starting state.  Say
that `w` is `K`-simple if, from one (equivalently every) seed state, its
post-move observations are distinct at every rank in `K`.  Equality patterns
are independent of the seed because changing the seed only relabels every
observed set.

### Theorem 8.1 (high-entropy common-transformation bundle)

Assume `d<=k<f` for every `k in K`, put `q=|K|`, and let

\[
 \varepsilon_\ell=q{\ell\choose2}{d!\over d^d}.        \tag{8.1}
\]

Whenever `epsilon_ell<1`, there are a position permutation
`sigma in S_n` and a family `\mathcal G_ell` of `K`-simple legal generator
words such that

\[
 |\mathcal G_\ell|
 \ge {(1-\varepsilon_\ell)d^\ell\over n!},            \tag{8.2}
\]

and every `w in \mathcal G_ell` carries every seed state `pi` to the same
endpoint `sigma(pi)`.

For the palette parameters and any fixed `C>1`, taking `ell=ceil(Cn)` gives
`epsilon_ell=o(1)` and

\[
 \log|\mathcal G_\ell|
 \ge (C-1)n\log n-Cn\log2+n-o(n\log n).               \tag{8.3}
\]

Thus a common-endpoint block of linear length has `Theta(n log n)` branch
entropy, or

\[
 {1\over\ell}\log|\mathcal G_\ell|
 \ge (1-1/C)\log n-O(1)                               \tag{8.4}
\]

entropy per physical step.

The family may additionally be required to have chordless decks at both
middle ranks, with the asymptotic lower bound in (8.2) unchanged up to its
`1-o(1)` factor.  Indeed the extra excluded fraction is at most

\[
 {\ell\choose2}\bigl(m(m+1)+(m+1)m\bigr){d!\over d^d}
 =e^{-n/2+o(n)}.                                      \tag{8.4a}
\]

Here short nonconsecutive chords are impossible because both middle ranks
are at most `f-2`, and the displayed long-gap bound is the central chord
estimate.  For a fixed seed, chordlessness implies that each unordered
middle-rank deck supports at most two chronological orientations.  Thus
this strengthened bundle realizes at least `|\mathcal G_ell|/2` distinct
unordered decks at **each** middle rank.  Its entropy is real deck entropy,
not merely multiple names for one rigid deck.

#### Proof

For a uniformly random generator word, a rank-`k` target cannot return at a
positive gap below `f`.  At a larger gap, the history-free return bound is
at most `d!/d^d`, because `k>=d`.  A union bound over ranks and time pairs
shows that at least `(1-epsilon_ell)d^ell` generator words are `K`-simple.

Partition these good words according to their induced position permutation.
There are at most `n!` cells, so the largest cell gives (8.2).  Every word in
one cell has the asserted common endpoint from every seed.  Finally,
`d=n/2-o(n)`, Stirling gives `log(n!)=n log n-n+o(n)`, and (8.1) is
`exp(-n/2+o(n))` for linear `ell`.  Substitution proves (8.3)--(8.4).
\(\square\)

This bundle also has exact relabeling-averaged occurrence marginals.  Choose
the seed uniformly from `S_n` and choose a word from `\mathcal G_ell` by any
law independent of the seed.  Relabeling invariance and simplicity give,
for every `k in K` and every `S in binom([n],k)`,

\[
 \Pr(S\text{ occurs in the microblock})={\ell\over\binom nk}. \tag{8.5}
\]

Equation (8.5) is an occurrence marginal, not yet a fractional factor for a
long concatenation: the same target may occur in different microblocks.

### Proposition 8.2 (exact adjacent and nested central codegrees)

Use the strengthened bundle having chordless decks at both middle ranks,
choose its seed uniformly, and use any seed-independent law on its branch
words.  At either `k in {m,m+1}`, if `S,S'` are Johnson-adjacent, then

\[
 \Pr(S,S'\text{ both occur})
 ={\ell-1\over e(J(n,k))}
 ={2(\ell-1)\over Wk(n-k)}.                           \tag{8.6}
\]

After division by the one-target marginal `ell/W`, this is
`(8+o(1))/n^2`.

For completeness, if `S,S'` have Johnson distance `j>=2` and
`c_(k,j)(w)` is the number of distance-`j` unordered pairs in branch deck
`w`, then the exact distance-profile formula is

\[
 \Pr(S,S'\text{ both occur})
 ={2\,\mathbb E c_{k,j}(w)
   \over W{ k\choose j}{n-k\choose j}}.               \tag{8.6a}
\]

Its normalization is at most

\[
 {2{\ell\choose2}
  \over \ell {k\choose j}{n-k\choose j}}.             \tag{8.6b}
\]

For each fixed `j>=2` this is `O(n^(1-2j))` when `ell=O(n)`, but it is not
uniformly `O(n^(-3))` over growing `j`: near-disjoint central pairs have
much smaller orbits.  No favorable all-distance same-rank codegree bound is
claimed for the common-transformation bundle.

If `S in \mathcal L`, `T in \mathcal R`, and `S subset T`, then

\[
 \Pr(S,T\text{ both occur})
 ={2\ell-1\over W(m+1)},                              \tag{8.7}
\]

whose normalization by `ell/W` is `(4+o(1))/n`.

#### Proof

In a chordless simple rank-`k` deck, the only Johnson edges induced by the
`ell` observed targets are its `ell-1` temporal edges.  Uniform relabeling
is transitive on Johnson edges, proving (8.6).  A pair at Johnson distance
`j>=2` has an orbit of size

\[
 {W\over2}{k\choose j}{n-k\choose j}.
\]

Uniform relabeling is also transitive on pairs at each fixed distance `j`.
Counting those pairs in the branch deck gives (8.6a), and the trivial bound
`c_(k,j)(w)<=binom(ell,2)` gives (8.6b).

Write the central traces as `A_t` at rank `m` and
`B_t=A_(t-1) union A_t` at rank `m+1`.  The first `B` contains the one
recorded face `A_1`, and every later `B_t` contains `A_(t-1),A_t`.  There
are no other recorded containments: another `A` would be a non-temporal
Johnson neighbor of one of those two faces, while the only possible adjacent
exception would repeat a rank-`(m+1)` target.  Hence one path has exactly
`2ell-1` recorded nested pairs.  There are `W(m+1)` nested pairs globally,
and relabeling is transitive on them, giving (8.7).  \(\square\)

### Corollary 8.3 (identity backbone with linear checkpoint spacing)

Let `h` be the order of `sigma`.  Concatenate `h` arbitrary, independently
chosen members of `\mathcal G_ell`.  Every such concatenation returns every
seed state to itself, and after each `ell` steps its complete state is fixed
independently of all branch choices.  Hence any one microblock may be
replaced by another member of `\mathcal G_ell` without a bridge and without
changing either adjacent checkpoint state.

Moreover

\[
 h=\exp(O(\sqrt n\log n))=\exp(o(n)).                 \tag{8.8}
\]

For the palette parameters with `ell=ceil(Cn)`, `C>1`, the identity backbone
therefore has subexponential length, may be tiled at coefficient-one scale,
and retains the entropy rate (8.4).

#### Proof

Every microblock acts by `sigma`, so `h` of them act by `sigma^h=I`,
regardless of the branch words.  For (8.8), split the cycle lengths of
`sigma` at `sqrt n`.  The least common multiple of the small lengths divides
`product_(j<=sqrt n)j`, while there are at most `sqrt n` large cycles and
their product is at most `n^(sqrt n)`.  Taking logarithms gives
`O(sqrt n log n)`.  \(\square\)

### Corollary 8.4 (coefficient-one length accounting)

Use the palette parameters and `ell=ceil(Cn)`, `C>1`.  Put `L=h ell` and
`t=floor(W/L)`.  Any concatenation of `t` identity
backbones from Corollary 8.3 is a closed legal trajectory of length

\[
 N=tL,\qquad 0\le W-N<L=e^{o(n)},\qquad |K|(W-N)=o(W). \tag{8.9}
\]

All microblock-checkpoint observations together have total band incidence
at most

\[
 |K|th={|K|N\over\ell}=O(|K|W/n)=o(W).                \tag{8.10}
\]

Thus every collision forced by repeated checkpoint states, including the
identity seams, can be discarded wholesale at `o(W)` total band cost.
Other collisions between the interiors of different microblocks are not
controlled by (8.10).

After this wholesale deletion, every microblock contributes `ell-1`
distinct observations at every band rank.  Under the uniform-seed law of
(8.5), relabeling symmetry remains exact and the retained marginal becomes

\[
 \Pr(S\text{ occurs away from the checkpoint})
 ={\ell-1\over\binom nk}.                             \tag{8.11}
\]

#### Proof

Every backbone starts and ends at the same full state, so arbitrary branch
choices concatenate and close legally.  Since `log L=o(n)` while
`log W=(log 2)n+o(n)`, both assertions in (8.9) follow.  There are exactly
`th=N/ell` post-move microblock checkpoints.  Charging their one observation
at every band rank gives (8.10), and `|K|/ell=o(1)`.  \(\square\)

The repeated-`sigma` backbone is useful for an exact identity loop, but a
different averaging argument gives the stronger combination of a Cartesian
microblock palette and almost-certain **global** simplicity.

### Theorem 8.5 (rich rectangular checkpoint macro)

Fix `C>1`, put `ell=ceil(Cn)`, and choose a multiple `a=t ell` satisfying

\[
 \log a=o(n),\qquad nR_{\rm br}=o(a).                 \tag{8.12}
\]

For example, one may take `a` to be the largest multiple of `ell` below
`n^5`.  There is a transformation vector

\[
 \boldsymbol\sigma=(\sigma_1,\ldots,\sigma_t)\in(S_n)^t
\]

whose full fiber is a Cartesian product

\[
 \mathcal F_{\boldsymbol\sigma}
 =\mathcal F_{\sigma_1}\times\cdots\times
  \mathcal F_{\sigma_t},                             \tag{8.13}
\]

where `\mathcal F_\sigma` is the set of `ell`-step generator words inducing
`\sigma`, with the following properties.

1. Its size obeys

   \[
   \log|\mathcal F_{\boldsymbol\sigma}|
   \ge {1\over2}\left(a\log d-t\log(n!)\right)
   =\Omega(a\log n).                                  \tag{8.14}
   \]

2. Under the uniform product law on (8.13), the probability that the whole
   `a`-step core is not band-simple or has a chord at either middle rank is
   at most

   \[
   \sqrt{\eta_a},\qquad
   \eta_a:=\left(|K|+2m(m+1)\right)
        {a\choose2}{d!\over d^d}
        =e^{-n/2+o(n)}.                               \tag{8.15}
   \]

3. From every seed, all product words have the same complete state at every
   `ell`-step checkpoint and the same final state.  Thus their microblocks
   may be chosen independently without any connector.

Conditioning (8.13) on the good event in item 2 leaves
`(1-o(1))|\mathcal F_{\boldsymbol\sigma}|` paths.  With a uniform seed, this
conditioned law is relabeling-invariant, has exact target marginal

\[
 {a\over\binom nk}\qquad(k\in K),                    \tag{8.16}
\]

and has the central codegrees of Proposition 8.2 with `ell` replaced by
`a`.

#### Proof

Let `X` be a uniformly random `a`-step generator word, split into `t`
consecutive `ell`-step words, and let `\boldsymbol\Sigma` be their induced
transformation vector.  Conditional on `\boldsymbol\Sigma`, the `t` words
are independent and uniform on their respective fibers.  Hence, writing
`Z=|\mathcal F_{\boldsymbol\Sigma}|`,

\[
 \mathbb E\log Z
 =H(X\mid\boldsymbol\Sigma)
 =a\log d-H(\boldsymbol\Sigma)
 \ge a\log d-t\log(n!)=:L_a.                         \tag{8.17}
\]

Also `0<=log Z<=U_a:=a log d`.  Therefore

\[
 \Pr\{\log Z\ge L_a/2\}
 \ge {L_a\over 2U_a-L_a}.                            \tag{8.18}
\]

For `ell=Cn`, the right side tends to `(C-1)/(C+1)>0`.

Let `p(\boldsymbol\Sigma)` be the conditional probability of the bad event
in item 2.  The history-free return bound, the short-chord exclusion, and a
union bound give

\[
 \mathbb E p(\boldsymbol\Sigma)=\Pr(X\text{ is bad})
 \le\eta_a.                                           \tag{8.19}
\]

Thus `Pr(p>sqrt(eta_a))<=sqrt(eta_a)=o(1)`.  The events in
(8.18) and `p<=sqrt(eta_a)` intersect for all sufficiently large `n`.
Choose a vector in their intersection.  This proves (8.14)--(8.15), while
the definition of the vector gives the checkpoint assertion.

The good event and the transformation vector depend only on generator
positions, not on seed labels.  Uniformizing the seed therefore makes the
conditioned law relabeling-invariant.  Every good path has exactly `a`
distinct targets at every band rank and chordless central decks, proving
(8.16) and Proposition 8.2's codegree count.  \(\square\)

### Corollary 8.6 (polynomial-core fractional palette with checkpoints)

Take `a` as in Theorem 8.5, put

\[
 s=\left\lfloor{W\over a+2R_{\rm br}}\right\rfloor,
 \qquad N=sa,                                         \tag{8.20}
\]

and surround each conditioned macro core by the two exact `R_br`-step bridges
of the fixed-endpoint palette.  The resulting palette has the same exact
outer real/dummy degrees and middle degree `N/W` as the fractional
near-factor of Section 5.9, and

\[
 |K|(W-N)=o(W).                                       \tag{8.21}
\]

Its support consists of globally band-simple, centrally chordless cores of
polynomial length, with common full-state checkpoints every `Theta(n)`
steps and support size `exp(Omega(a log n))` per seed.

#### Proof

Choose the seed uniformly and a conditioned word from Theorem 8.5.  Equation
(8.16) is exactly the symmetry input used in the fractional palette proof;
the same real/dummy decorations therefore give the asserted degrees.  The
floor estimate gives

\[
 W-N<a+2R_{\rm br}
       +{2R_{\rm br}W\over a+2R_{\rm br}}.
\]

After multiplication by `|K|/W`, the first two terms vanish exponentially
and the last is `O(|K|R_br/a)=o(1)` by (8.12), proving (8.21).  Moreover
`R_br/a=o(1/n)`, so the largest nonmiddle layer is below `N`, exactly as in the
budget fractional theorem.  \(\square\)

There are now two rigorously distinct uses of the rectangular cell.

- Conditioning on global simplicity gives the exact fractional palette in
  Corollary 8.6, but destroys literal coordinate independence.
- Leaving the product cell unconditioned preserves independent
  microblock switches.  By (8.15), over coefficient-one total length the
  expected band incidence lying in bad macro cores is at most

  \[
  |K|W\sqrt{\eta_a}=o(W).                             \tag{8.22}
  \]

  Those cores may therefore be charged wholesale at negligible scale in a
  probabilistic construction.

What remains unproved in the second use is target coverage and retained-
parity matching among the good product choices.  Theorem 8.5 removes the
endpoint, entropy, checkpoint, and global-simplicity objections to a dense
product switch scheme; it does not supply the required colored cycle
descent.

This is an actual legal tail-MTF switch architecture, not merely a Johnson
projection.  Trace reconstruction shows that its distinct branch words give
distinct ordered traces at each middle rank.  Endpoint rigidity permits up
to `Theta(n)` variable middle-rank observations in a block of length `Cn`,
and the bundle has exponentially many distinct unordered decks.  This proves
that dense switching has no raw endpoint-count, branch-entropy, or
relabeling-marginal obstruction.  It does **not** prove a linear lower bound
on target-replacement distance between branches, hence does not yet prove
`Theta(W)` useful mobility.

What is still missing is exactly the useful part: no theorem here says that
the microblock replacement can be chosen to delete a prescribed incidence
cycle while keeping the already selected `P` resources matched.  Nor does
local `K`-simplicity prevent collisions between different microblocks.
The backbone converts the old physical-switch question into a dense
multirank selection problem with common full-state checkpoints every
`Theta(n)` steps; it does not solve that selection problem.

## 9. What this settles and what remains

The proved conclusions are:

1. Central Hall defect is cycle rank, up to the `o(W)` forest term.
2. Every near-complete selected rank-`m` deck has a linear, maximum-degree-two
   reservoir of any linear family of desired missing union colors.
3. After FIFO is discarded, a Middle Levels Hamilton cycle gives an exact
   central path cover with zero Hall deficiency and affordable component
   count.
4. Any repair of a linear defect using `o(W)` resulting cores must change
   linearly many temporal edges.  Sparse slotwise, cross-slot, or
   bridge-separated recompositions cannot do so.
5. Dense legal common-endpoint switching at linear spacing has ample entropy
   and exact relabeling-averaged marginals, so it remains a live architecture.
6. A polynomial-length macro can have a genuinely Cartesian product of
   independent checkpoint-block fibers before conditioning, with
   `exp(Omega(a log n))` branches and only `exp(-Omega(n))` bad mass.  After
   conditioning it yields an exact globally simple fractional palette, but
   the coordinates are no longer independent.

Accordingly, global unordered chord supply and abstract alternating cycles
are no longer the unknowns.  The subsequent one-central reduction
`MATH_REDUCTION_ONE_CENTRAL_MATCHING_PLUS_GRAPHIC_COLORS_20260821.md`
strictly weakens the provisional parity formulation used earlier in this
note: it is enough to preserve or rematch the rank-`m` decks and to keep the
total graphic Hall deficiency at every other band rank sublinear.
Proposition 6.1 is the exact central FIFO constraint, while Theorem 8.5
supplies the strongest legal checkpoint palette here on which such a
theorem might act.  No such common-path rounding theorem is proved here.

## 10. Finite audit

All finite checks were run on `ssh h100`, not on the local machine.

- For `n=5,7,9`, two perfect matchings of the middle-level inclusion graph
  were constructed.  Across 600 random choices of `mathcal A` and
  `mathcal M`, the program verified (3.1)--(3.3), the `|M|-2r` bound, and
  maximum reservoir degree two.
- Across 2,000 random block-color incidence graphs, it verified (2.2)
  exactly.  In all 413 instances containing a cycle, replacing a cycle edge
  by a fresh leaf lowered cyclomatic number by exactly one.
- Across 9,600 cyclic fragment recompositions, including independently
  reversed fragments, it verified the bound (7.1).
- Exhaustive common-transformation grouping at `(n,f,K,ell)` equal to
  `(7,5,{3,4},9)`, `(7,5,{3,4},11)`, and `(8,5,{4},9)` found respectively
  largest simple fibers of sizes `12,29,21`.  Every fiber had its asserted
  common endpoint from every tested seed, distinct ordered central traces,
  and an identity-backbone order equal to `7,2,7`, respectively.
- On all `9!` relabelings of one chordless `(n,f,K,ell)=(9,7,{4,5},10)`
  word, the exact single-target, adjacent-pair, and nested-pair frequencies
  agreed with (8.5)--(8.7).

These checks audit the normalizations and boundary counts; the proofs do
not depend on them.
