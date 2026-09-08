# Adjacent necklaces: rooted gap matching reduces exactly to a 4/5 path, whose imbalance is unbounded

**Date:** 2026-08-05  
**Method:** a rooted split/merge involution and evaluation of a Gaussian
binomial at minus one; no computation  
**Status:** unconditional rooted reduction and exact warning.  It validates
the natural canonical-gap matching locally, but proves that the remaining
4/5 path cannot be closed by an ordinary near-perfect path matching.

## 1. Rooted cyclic gap compositions

A nonempty cyclic `3`-separated cut set on a `q`-cycle is equivalently a
cyclic composition

\[
                     g_1+\cdots+g_k=q,
                     \qquad g_i\ge3.                 \tag{1.1}
\]

Distinguish one cut and list the gaps from that root.  Protect the final
gap `g_k`; the other `k-1` gaps are called internal.

Deleting an internal cut merges two consecutive gaps.  Conversely,
inserting a cut splits one gap into two parts at least three.  These are
exactly the vertical exit-toggle edges of the all-one full-merge fibre.

## 2. Exact split/merge involution

Scan `g_1,...,g_(k-1)` from the root and stop at the first part outside
`{4,5}`.

* If the first active part is `g_j>=6`, replace it by

  \[
                              (3,g_j-3).              \tag{2.1}
  \]

* If it is `g_j=3`, merge it with its successor:

  \[
                              (3,g_{j+1})mapsto3+g_{j+1}. \tag{2.2}
  \]

The successor may be the protected final gap.  The distinguished root cut
is never removed.

### Theorem 2.1 (rooted vertical matching)

Rules (2.1)--(2.2) form a fixed-point-free involution on every rooted gap
composition having an active internal part.  Every pair is one literal
vertical toggle.  The unmatched rooted compositions are exactly

\[
                (\epsilon_1,\ldots,\epsilon_{k-1},h),
                \qquad \epsilon_i\in\{4,5\},\quad h\ge3. \tag{2.3}
\]

#### Proof

All parts before the first active position are 4 or 5 and are unchanged.
Splitting a part at that position creates a leading 3, which is the first
active part on rescanning and is merged back.  Merging a leading 3 with
its successor creates a part at least 6 at the same position, which is
split back.  Thus the two rules are inverse.  Their only fixed-free
residue is the absence of an active internal part, namely (2.3).
\(\square\)

This is the strongest form of the “first minimum gap” idea that does not
need a cyclic tie-break: once a root is protected, the matching is exact.

## 3. The residual is a binary token path

Fix `k` and let exactly `t` of the first `n=k-1` parts in (2.3) equal 5.
Then the final gap is forced:

\[
                         h=q-4n-t.                   \tag{3.1}
\]

Within this family, shifting a cut between neighboring internal gaps
changes

\[
                             45\longleftrightarrow54. \tag{3.2}
\]

Hence its horizontal graph is the weight-`t` binary token graph of the
path on `n` positions.

The deleted-cut hub of an edge (3.2) contains a distinguished merged
part `4+5=9`.  After fixing the hub, the split site, and every other
expanded nine, that site has only the two expansions `45` and `54`.
Thus every pointed horizontal edge determines its rooted hub uniquely.

The converse is not injective.  A hub may contain several nines, and the
other nines may be expanded independently.  For example the same rooted
hub `(9,9,h)` supports the disjoint edges

\[
  (4,5,4,5,h)-(5,4,4,5,h),\qquad
  (4,5,5,4,h)-(5,4,5,4,h).                         \tag{3.3}
\]

Consequently an arbitrary matching of the binary token path need not be
hub-rainbow.  Distinct-hub selection is a separate global constraint.

## 4. Exact shore imbalance

Let

\[
 D(n,t)=\sum_{1\le i_1<\cdots<i_t\le n}
                    (-1)^{i_1+\cdots+i_t}.           \tag{4.1}
\]

This is the difference of the two bipartition shores of the path token
graph, up to a global sign.

### Theorem 4.1 (Gaussian value at minus one)

Write `n=2m` or `2m+1`.  Then

\[
 D(2m,t)=
 \begin{cases}
 0,&t\text{ odd},\\
 (-1)^s\binom ms,&t=2s,
 \end{cases}                                        \tag{4.2}
\]

and

\[
 D(2m+1,t)=
 \begin{cases}
 (-1)^s\binom ms,&t=2s,\\
 (-1)^{s+1}\binom ms,&t=2s+1.
 \end{cases}                                        \tag{4.3}
\]

#### Proof

The coefficient generating function is

\[
 \sum_tD(n,t)z^t=\prod_{i=1}^n(1+(-1)^iz).
\]

For `n=2m` this is `(1-z^2)^m`; for `n=2m+1` it is
`(1-z)(1-z^2)^m`.  Reading coefficients gives (4.2)--(4.3). \(\square\)

In particular, the absolute shore difference can be

\[
                         \binom{\lfloor n/2\rfloor}
                                      {\lfloor t/2\rfloor},             \tag{4.4}
\]

which is unbounded.  The smallest relevant example is `n=4,t=2`, whose
six strings have shores of sizes four and two.

### Corollary 4.2 (ordinary path matching is insufficient)

The rooted split/merge involution cannot be completed merely by taking a
near-perfect matching in every residual 4/5 path family.  Some such
families have matching deficiency at least two, and in general the parity
lower bound (4.4) grows without bound.

The odd circulation blossoms are therefore essential even after rooting:
they provide the same-shore interaction that an ordinary adjacent-swap
path lacks.

## 5. Unrooted boundary

Theorem 2.1 protects a chosen root cut.  An unrooted necklace can have
several rotationally equivalent candidate roots, and forgetting the mark
does not automatically descend the rooted involution.  A complete cyclic
proof still needs either:

1. a rotation-compatible root selector;
2. an odd-cover transfer theorem for rooted matchings; or
3. a direct cyclic matching tree.

Even after that descent, Theorem 4.1 shows that a hub-rainbow blossom bank
must repair the residual path imbalance.

## 6. Scope

Proved:

1. an exact rooted vertical involution;
2. the exact residual alphabet `{4,5}` plus one terminal sidecar;
3. identification of residual horizontal edges with a path token graph;
4. a precise pointed-edge-to-rooted-hub map, with noninjective fibres; and
5. the exact, potentially unbounded residual shore imbalance.

Not proved:

1. unrooted cyclic descent;
2. enough circulation blossoms to remove (4.4) in every family;
3. composition with earlier ambient matching stages; or
4. the all-dimensional adjacent-necklace theorem.
