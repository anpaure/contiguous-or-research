# Flat middle rows force private source letters: a direct-compilation barrier for diagonal fans

**Date:** 2026-08-13  
**Method:** consecutive-window inclusion and the exact middle-layer count  
**Status:** unconditional.  The theorem applies to every universal word of
length `B(k)+C`, without Johnson adjacency.  It rules out inserting a large
bank of the present nested diagonal-fan words *unchanged* into a bounded-
excess flat middle carrier.  It does not rule out a redesigned fan whose
letters are enlarged inside a common cap so that the comparable pairs are
broken.

## 1. Set-up

Put

\[
 R=\left\lceil{k\over2}\right\rceil,
 \qquad W={k\choose R},
 \qquad q=d+1\geq2.
\]

Let

\[
 A=(A_0,A_1,\ldots,A_{N+q-2})
\]

be a nonempty set word and write its length-`q` window row as

\[
 T_i=\bigcup_{j=i}^{i+q-1}A_j
 \qquad(0\leq i<N).                                      \tag{1.1}
\]

In the bounded-excess application

\[
 |A|=B(k)+C=W+d+C,
 \qquad N=|A|-q+1=W+C.                                   \tag{1.2}
\]

If `A` is universal, all `W` rank-`R` subsets occur among the `N`
windows in (1.1).  Choose one occurrence of every such subset and call its
index **selected**.  Thus the selected index set `G` has size `W`, its
window values are pairwise distinct rank-`R` sets, and the exceptional set

\[
                         B=[0,N-1]\setminus G             \tag{1.3}
\]

has size `C`.

## 2. The private-letter law

### Theorem 2.1 (two-sided private coordinates)

If both `i` and `i+1` are selected, then there are coordinates

\[
 x_i\in A_i\setminus\bigcup_{j=i+1}^{i+q}A_j,
 \qquad
 y_i\in A_{i+q}\setminus\bigcup_{j=i}^{i+q-1}A_j.       \tag{2.1}
\]

In particular neither endpoint letter is redundant against the other `q`
letters involved in the transition.

#### Proof

Put

\[
 M_i=\bigcup_{j=i+1}^{i+q-1}A_j.
\]

Then

\[
 T_i=M_i\cup A_i,
 \qquad T_{i+1}=M_i\cup A_{i+q}.                         \tag{2.2}
\]

The two selected values have the same rank `R` and are distinct.  Hence
`T_i` is not contained in `T_(i+1)` and conversely.  A point of
`T_i-T_(i+1)` must lie in `A_i` and in none of
`A_(i+1),...,A_(i+q)`, giving `x_i`.  The reverse difference gives `y_i`.
\(\square\)

This conclusion uses only exact middle-layer counting.  It does not assume
that consecutive owners are Johnson adjacent.

### Corollary 2.2 (adjacent-comparability budget)

Let

\[
 \mathcal U=\{p:0\leq p\leq N-2,\ A_p\subseteq A_{p+1}\},             \tag{2.3}
\]

\[
 \mathcal D=\{p:q-1\leq p\leq N+q-3,\ A_{p+1}\subseteq A_p\}.       \tag{2.4}
\]

Then

\[
                         |\mathcal U|\leq2C,
 \qquad                  |\mathcal D|\leq2C.             \tag{2.5}
\]

Consequently the bulk interval of source adjacencies

\[
                         q-1\leq p\leq N-2               \tag{2.6}
\]

contains at most `4C` comparable pairs.  Over the whole source word there
are at most

\[
                         4C+2(q-1)                         \tag{2.7}
\]

comparable adjacent pairs.

#### Proof

If `A_p\subseteq A_{p+1}` and `0\leq p\leq N-2`, then

\[
 T_p=\bigcup_{j=p+1}^{p+q-1}A_j
 \subseteq
 T_{p+1}.                                                \tag{2.8}
\]

Two selected windows cannot satisfy (2.8): they would be distinct
equal-rank sets in an inclusion relation.  Hence the edge `{p,p+1}` of the
window-index path meets the exceptional set `B`.

There are at most `2|B|=2C` path edges incident with `B`, proving the first
bound in (2.5).

If `A_{p+1}\subseteq A_p` and `p\geq q-1`, put `i=p-q+1`.  Then

\[
 T_{i+1}=\bigcup_{j=i+1}^{i+q-1}A_j
 \subseteq T_i.                                         \tag{2.9}
\]

Again `{i,i+1}` meets `B`; the map `p mapsto i` is injective, proving the
second bound.  Both arguments apply in the bulk (2.6), giving `4C`.
Only the first `q-1` descending pairs and the last `q-1` ascending pairs
escape the respective arguments, yielding (2.7). \(\square\)

For exact equality `C=0`, no two adjacent source letters in the bulk can be
comparable.  For `C=O(1)`, only `O(1)` bulk exceptions are possible.

## 3. Consequence for the current diagonal-fan atom

Recall the literal fan word

\[
 K,X_{A-1},X_{A-2},\ldots,X_1,Y_1,Y_2,\ldots,Y_{B-1},   \tag{3.1}
\]

where

\[
 K\subset X_1\subset\cdots\subset X_{A-1},
 \qquad
 K\subset Y_1\subset\cdots\subset Y_{B-1}.             \tag{3.2}
\]

Every internal adjacency of (3.1), except possibly `X_1,Y_1`, is a
comparable pair.  If `A,B>=2`, the word has length `A+B-1` and exactly

\[
                         A+B-3=|\text{word}|-2           \tag{3.3}
\]

such pairs.  The one-arm degeneracies have at least `|word|-2` as well.

### Corollary 3.1 (unchanged fan-bank no-go)

Suppose a source word of length `B(k)+C` contains `M` pairwise
position-disjoint nontrivial fan words (3.1) as literal consecutive blocks,
where **nontrivial** means that the displayed fan contains at least one
comparable internal adjacency, and their letters are kept unchanged.  Then

\[
                         M\leq4C+2(q-1).                  \tag{3.4}
\]

More sharply, the sum over the fans of `(|fan|-2)` is at most the right
side of (2.7).

#### Proof

Choose one comparable internal adjacency from each fan.  These source
adjacencies are distinct.  Apply (2.7); applying it to all comparable
internal adjacencies gives the sharper statement. \(\square\)

Thus the standalone product-SCD slab atlas, which concatenates a growing
bank of nested fans, cannot simply be declared the antecedent of a
`B(k)+O(1)` flat middle row.  Its physical efficiency and its exact lower
coverage remain valid, but a successful compiler must alter the fan letters
inside their occurrence caps, replace the nested arms by private-coordinate
arms, or use a different non-flat architecture with enough extra middle
windows.  Merely ordering the unchanged fan atoms or assigning rank-`R`
caps to their existing `q`-windows cannot evade (2.7).

## 4. Scope

The result does **not** say that every use of the diagonal-fan identity is
impossible.  In the standalone atlas, many axis cells are harmless extra
values rather than mandatory protected targets.  If those source letters
can be enlarged within the intersection of all genuinely designated target
rows, their comparabilities may be broken.  What (2.7) proves is that this
private-coordinate modification is load-bearing: a bounded-excess proof
cannot retain a linear number of the present comparable adjacencies.
