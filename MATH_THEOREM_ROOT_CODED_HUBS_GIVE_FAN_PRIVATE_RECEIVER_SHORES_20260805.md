# Root-coded hub gaps give fan-private receiver shores

**Date:** 2026-08-05  
**Method:** protected cyclic gap codes and the literal receiver-square
formula; no computation  
**Status:** unconditional construction inside an adjacent-necklace
capacity-two sector whenever the displayed slack condition holds.  It
removes the two endpoint bicircular constraints for the planted bank.  It
does not prove that the global PBBS parent factor contains the bank, nor
does it prove the residual next-level Hall/Tutte extension.

## 1. Setting

Let the coordinate cycle have length `ell`.  A literal hub is indexed by a
2-independent cut set `H` of cardinality `k`:

\[
 x_H={\bf1}+\sum_{j\in H}(e_j-e_{j+1}).                 \tag{1.1}
\]

Write the clockwise cyclic gap word of `H` as

\[
                         g(H)=(g_0,\ldots,g_{k-1}).     \tag{1.2}
\]

Thus every `g_i>=3` and `sum g_i=ell`.  A shifted petal supported in one
gap uses two adjacent legal cuts `{c,c+1}`.  Two passive petals with cut
pairs `{p,p+1}` and `{r,r+1}` give the four receiver vertices

\[
 x_{H\cup\{p+\alpha,r+\beta\}},\qquad
                         \alpha,\beta\in\{0,1\}.       \tag{1.3}
\]

Their two diagonal shores are

\[
 A=\{00,11\},\qquad B=\{10,01\}.                       \tag{1.4}
\]

The issue is that literal disjointness of different squares need not
survive quotienting by cyclic rotation.

## 2. A rotation root which survives every receiver insertion

Call a consecutive block of gaps a **marker block** when

1. it has length `s>=4`;
2. each of its entries belongs to `{4,5}`;
3. the gaps immediately before and after it are both `3`; and
4. every petal cut lies in one separate **workspace gap**.

Assume all gaps outside the marker and workspace are `3`.  Inserting two
receiver cuts in the workspace replaces that one workspace gap by three
gaps and leaves the marker pointwise unchanged.

### Lemma 2.1 (persistent cyclic root)

In every double-expansion receiver (1.3), the marker is the unique longest
cyclic run of gaps different from `3`.

Consequently every rotation between two such receivers maps marker start
to marker start and preserves the ordered marker word.

#### Proof

The protected marker is an `s`-term run of non-`3` gaps.  Outside it, all
old gaps except the workspace are `3`.  Two inserted cuts split the one
workspace gap into exactly three gaps, so the workspace can create a run
of at most three non-`3` gaps.  Since `s>=4`, the marker is the unique
longest run.  A cyclic rotation preserves gap words and therefore maps
this unique run, including its boundary after the preceding `3`, to
itself.  Its ordered entries are preserved. \(\square\)

The statement uses rotations only.  It makes no assertion for a dihedral
quotient containing reflections.

## 3. A fixed-sum family of marker codes

Fix integers `s>=4` and `w` with `0<=w<=s`.  Use as marker words all
length-`s` words over `{4,5}` having exactly `w` entries equal to `5`.
There are

\[
                              {s\choose w}              \tag{3.1}
\]

such words, and every one has the same total gap length `4s+w`.
Therefore they can be used in one fixed sector `(ell,k)`.

Suppose one hub must support `p` pairwise endpoint-disjoint shifted
petals.  A workspace gap of length

\[
                              W_0=6p+3                  \tag{3.2}
\]

suffices: take the petal starts

\[
                              c_j=4+6j,
                    \qquad 0\le j<p.                   \tag{3.3}
\]

Each `{c_j,c_j+1}` is at distance at least four from the two workspace
boundaries, and distinct split blocks start six positions apart.  Hence
all cross-choices from two different petals are jointly admissible.

The minimum total length of the resulting gap word is

\[
 \ell_0
   =(4s+w)+(6p+3)+3(k-s-1)
   =3k+s+w+6p.                                         \tag{3.4}
\]

Extra length may be added to the workspace gap.  Thus the construction is
available whenever

\[
 \boxed{
 k\ge s+3,
 \qquad
 \ell-3k\ge s+w+6p.}                                  \tag{3.5}
\]

For `q` distinct hub groups, one may take

\[
 s=\min\{t\ge4:{t\choose\lfloor t/2\rfloor}\ge q\},
 \qquad w=\lfloor s/2\rfloor.                          \tag{3.6}
\]

Hence the marker cost is only `O(log q)` beyond the `6p` workspace cost.

## 4. Both receiver diagonals are fan-private

Choose `q` different marker words from (3.1), and let `H_f` be the
corresponding rooted hubs.  In every hub fix a disjoint pairing of its
passive petals.  Each passive pair is one fan task; its candidates may use
any of the four orientations in (1.3).

### Theorem 4.1 (root-coded fan privacy)

Under (3.5), receiver vertex orbits belonging to different fan tasks are
pairwise disjoint.  This holds on both diagonal shores `A` and `B`.

Equivalently, if `P` is the one-candidate-per-fan partition matroid and
`M_A,M_B` are the two endpoint bicircular matroids, then every
`P`-independent set is independent in both `M_A` and `M_B`.

#### Proof

First take receivers based at two different hubs.  If their necklace
orbits were equal, some rotation would identify their cut sets.  By Lemma
2.1 it would align marker start with marker start and identify the ordered
marker words.  The chosen marker words are different, a contradiction.

Now take two different passive-pair tasks over the same hub.  Lemma 2.1
again forces every orbit equality to align marker start with itself, hence
the rotation is the identity on the labelled coordinate cycle.  Literal
receiver squares from distinct passive pairs are vertex-disjoint: equality
of two double expansions would identify the unordered pair of added cuts
and therefore the unordered pair of parent petals.  The fixed passive
pairs are distinct.  Thus no equality occurs.

Inside one fan, at most one candidate is selected by `P`, and each
nondegenerate diagonal is one ordinary edge.  Across fans the endpoint
sets are disjoint.  Each shore of a `P`-independent set is therefore a
matching, hence a pseudoforest and an independent set of its bicircular
matroid. \(\square\)

### Corollary 4.2 (zero endpoint-selector loss)

For this planted bank, every choice of one nondegenerate receiver square
per fan is simultaneously endpoint-safe.  The endpoint selector loses
zero fan tasks.

This is stronger than the one-private-shore reduction.  It does not say
that the selected endpoints extend through the background next-level
matching.

## 5. Exact loss formula when only one shore is private

The preceding construction makes both shores private.  For later parent
constructions which make only `A` private, the remaining loss is still
exactly computable.

Let `E=dotunion_f E_f` be the candidate catalogue, let `q` be the number of
fans, let `P` be the partition matroid, and let `M_B` be the remaining
bicircular endpoint matroid.  Then

\[
 \nu=\min_{X\subseteq E}
       \bigl(r_P(X)+r_B(E\setminus X)\bigr),            \tag{5.1}
\]

so the exact unavoidable endpoint loss is

\[
 \boxed{
 q-\nu
 =\max_{X\subseteq E}
    \bigl(q-r_P(X)-r_B(E\setminus X)\bigr).}           \tag{5.2}
\]

Here

\[
 r_P(X)=|\{f:X\cap E_f\ne\varnothing\}|,              \tag{5.3}
\]

and, if `G_B(Y)` is the endpoint multigraph of `Y` and `tau_B(Y)` is the
number of its tree components containing an edge,

\[
 r_B(Y)=|V(G_B(Y))|-\tau_B(Y).                         \tag{5.4}
\]

Thus (5.2) is one explicit partition--bicircular cut.  In the root-coded
construction, `r_B(I)=|I|` for every `P`-independent `I`, and (5.2) is
zero.

## 6. Residual global gate

Root coding settles quotient coalescence and endpoint bicircular capacity
for the planted receiver bank.  It does not settle the background
extension.  After the endpoints are chosen, the exact remaining object is
the augmented graph `widehat G(J,I,O)` of the paired-receiver extension
theorem:

* at even cut length, extension is equivalent to all Hall inequalities in
  that bipartite augmented graph and its polytope is totally unimodular;
* at odd cut length, extension is equivalent to the corresponding Tutte
  blossom inequalities.

Nor does (3.5) prove that a prescribed PBBS parent factor contains these
root-coded hubs.  The precise remaining parent-side statement is:

> plant the rooted gap words and their workspace petals in the same PBBS
> parent factor while preserving the all-width upper, residence, and
> common-cap interfaces.

The construction proves that **once such a parent is chosen**, no receiver
endpoint loss remains.  The former three-matroid selector obstruction is
not intrinsic to the receiver squares; it is a consequence of allowing an
unrooted arbitrary parent/anchor bank.

