# Triangular endpoint ordering is an exact one-sided bandwidth problem

## 1. Purpose

The ordered-orthogonal-chain normal form reduces a universal OR word to two
orthogonal chain partitions, an ordering of their endpoint slots, and the
coordinatewise pinning condition.  It is tempting to start with any known
pair of orthogonal symmetric-chain decompositions and regard the endpoint
ordering as a lower-order bookkeeping problem.

This note proves that this is false in general.  For two width-sized chain
partitions, the minimum number of extra endpoint slots needed merely to put
all occupied cells in the physical triangle `left <= right` is exactly a
one-sided bandwidth parameter of their incidence graph.  In particular, an
expanding (hence random-looking) incidence graph needs a linear number of
extra slots.  Any `W+o(W)` construction obtained from orthogonal chain
partitions must therefore build a nested sequence of almost Hall-tight
incidence cuts from the outset.

The result is independent of both the forced within-chain precedence orders
and pinning.  It is a necessary obstruction which occurs before either of
those additional gates; it is not by itself a sufficient endpoint
realization theorem.

## 2. The incidence graph

Let

\[
                 \mathcal L=\{L_1,\ldots,L_W\},\qquad
                 \mathcal R=\{R_1,\ldots,R_W\}
\]

be two chain partitions of the same finite poset.  Assume they are
orthogonal:

\[
                         |L\cap R|\leq 1
             \qquad(L\in\mathcal L,R\in\mathcal R).
\]

Their incidence graph is the bipartite graph

\[
 G=(\mathcal L,\mathcal R;E),\qquad
 LR\in E\Longleftrightarrow L\cap R\ne\varnothing .             \tag{2.1}
\]

A triangular-support labeling in `n=W+d` physical positions chooses injective
labels

\[
       \ell:\mathcal L\longrightarrow[n],\qquad
       r:\mathcal R\longrightarrow[n]
\]

such that

\[
                         \ell(L)\leq r(R)
                         \qquad(LR\in E).                       \tag{2.2}
\]

The unused labels are the empty left- and right-endpoint families.  Condition
(2.2) is necessary before one asks whether the cells can be pinned by array
entries.

For bijections

\[
        \pi:\mathcal L\to[W],\qquad \sigma:\mathcal R\to[W],
\]

put

\[
 b^+(\pi,\sigma)
   =\max_{LR\in E}\bigl(\pi(L)-\sigma(R)\bigr),
\]

and define the one-sided bipartite bandwidth

\[
              b^+(G)=\min_{\pi,\sigma} b^+(\pi,\sigma).          \tag{2.3}
\]

Negative values cause no difficulty; write `b^+_0(G)=max(0,b^+(G))`.

## 3. Exact ordering theorem

### Theorem 1

The least `d>=0` for which injections satisfying (2.2) exist in `W+d`
positions is exactly

\[
                              \boxed{b^+_0(G)}.                   \tag{3.1}
\]

### Proof

Suppose first that a triangular-support labeling in `W+d` positions is given.
Order the nonempty left families by their physical labels and let `pi(L)` be
the rank of `ell(L)` among those `W` labels.  Define `sigma(R)` analogously.
Because at most `d` physical labels are unused on either side,

\[
                         \pi(L)\leq\ell(L),\qquad
                         r(R)\leq\sigma(R)+d.                    \tag{3.2}
\]

For every edge `LR`, equations (2.2)--(3.2) give

\[
                         \pi(L)\leq\sigma(R)+d.
\]

Hence `b^+(G)<=d`.

Conversely, choose orders `pi,sigma` with `b^+(pi,sigma)<=d`.  Put all empty
left slots after the occupied ones and all empty right slots before the
occupied ones:

\[
                       \ell(L)=\pi(L),\qquad
                       r(R)=d+\sigma(R).                         \tag{3.3}
\]

Then every edge satisfies

\[
                    \ell(L)=\pi(L)\leq d+\sigma(R)=r(R),
\]

so (3.3) is a valid triangular-support labeling.  This proves (3.1).
\(\square\)

The proof also shows that interspersing the empty slots cannot improve on
placing all left empties at the end and all right empties at the beginning.

## 4. Nested near-tight cuts

The bandwidth formulation has an equivalent cut consequence which is more
useful asymptotically.

### Corollary 2

If `b^+(G)<=d`, then there is a nested flag

\[
 \varnothing=X_0\subset X_1\subset\cdots\subset X_W=\mathcal L,
 \qquad |X_s|=s,                                      \tag{4.1}
\]

such that

\[
                              |N_G(X_s)|\leq s+d
                              \qquad(0\leq s\leq W).              \tag{4.2}
\]

### Proof

Take orders attaining bandwidth at most `d` and let `X_s` be the final `s`
left vertices in the `pi` order.  Every \(L\in X_s\) has

\[
                         \pi(L)\geq W-s+1.
\]

For every neighbor `R`, the bandwidth inequality gives

\[
                         \sigma(R)\geq W-s+1-d.
\]

There are at most `s+d` right vertices in these final positions, proving
(4.2).  The sets `X_s` are nested by construction.  \(\square\)

Thus near-width endpoint ordering requires not just one sparse cut, but a
complete nested sequence of almost nonexpanding left sets, one at every
cardinality.

There is also an exact flag characterization.  Orders of bandwidth at most
`d` exist if and only if there are complete flags
\(X_s\subseteq\mathcal L\) and \(Y_s\subseteq\mathcal R\), with
`|X_s|=|Y_s|=s`, such that

\[
                              N_G(X_s)\subseteq Y_{s+d}            \tag{4.3}
\]

with \(Y_t=\mathcal R\) for `t>=W`.  One direction is the preceding proof; in
the other direction, read the two flags as vertex orders.

In fact the right flag can be eliminated from the optimization.

### Theorem 2 (exact one-flag formula)

For a left order `pi`, let `X_s` be its suffix of size `s`.  Then the least
bandwidth achievable by a compatible right order is

\[
              d_\pi=\max_{0\leq s\leq W}
                       \bigl(|N_G(X_s)|-s\bigr)_+ .               \tag{4.4}
\]

Consequently

\[
 b^+_0(G)=\min_{\pi}\max_{0\leq s\leq W}
                       \bigl(|N_G(X_s)|-s\bigr)_+.                \tag{4.5}
\]

### Proof

Necessity is Corollary 2.  For sufficiency, let `q(R)` be the first suffix
size for which `R` enters `N_G(X_s)`.  In a right order, encode the position
of `R` from the end by

\[
                         \tau(R)=W-\sigma(R)+1.
\]

Every incident edge has displacement at most `d` exactly when

\[
                         \tau(R)\leq q(R)+d.                       \tag{4.6}
\]

This is a unit-time scheduling problem with deadlines `q(R)+d`.  The number
of jobs with deadline at most `t` is

\[
              |N_G(X_{t-d})|\leq(t-d)+d=t                         \tag{4.7}
\]

(with `X_u` empty for `u<0`).  The standard earliest-deadline schedule is
therefore feasible and supplies the required right order.  \(\square\)

This sufficiency is only for bare triangular support.  If the right order is
also constrained to be a linear extension of a within-chain precedence
digraph, the deadline schedule need not be permitted.

## 5. Expansion obstruction

### Corollary 3

Suppose that for some `1<=s<=W` every `s`-element subset
\(X\subseteq\mathcal L\) satisfies

\[
                              |N_G(X)|\geq s+a.                    \tag{5.1}
\]

Then

\[
                              b^+_0(G)\geq a.                      \tag{5.2}
\]

In particular, if for one fixed `alpha,epsilon>0`, every
\(X\subseteq\mathcal L\) of size `floor(alpha W)` obeys

\[
                         |N_G(X)|\geq(1+\epsilon)|X|,
\]

then any triangular endpoint realization needs

\[
                         d\geq(\epsilon\alpha+o(1))W.             \tag{5.3}
\]

### Proof

Apply (5.1) to the particular suffix `X_s` supplied by Corollary 2.  Its
neighborhood has size at most `s+d` and at least `s+a`, hence `d>=a`.
Equation (5.3) is the special case `s=floor(alpha W)` and
`a=epsilon s`.  \(\square\)

Consequently an expander-like incidence graph cannot underlie a
`W+o(W)` OR construction, even if its two chain partitions are perfectly
orthogonal and even before within-chain precedence and pin survival are
considered.

## 6. Consequences for the global programme

There is a complementary positive criterion.

### Corollary 4 (small incidence components suffice)

If every connected component of `G` has at most `s` left vertices, then

\[
                              b^+_0(G)\leq s-1.                    \tag{6.1}
\]

### Proof

For a component `K`, put

\[
                 \delta(K)=|K\cap\mathcal L|-|K\cap\mathcal R|.
\]

The component imbalances sum to zero.  Put the components in any circular
order and cut the circle immediately after a maximum of the cumulative
imbalance.  In the resulting linear order every pre-component cumulative
imbalance is nonpositive.

List the left and right vertices component by component in this common order,
using arbitrary internal orders.  Immediately before component `K`, the
difference between the numbers of listed left and right vertices is therefore
at most zero.  An edge stays inside `K`, and its additional left-minus-right
displacement is at most \(|K\cap\mathcal L|-1\leq s-1\).  This proves (6.1).
\(\square\)

For two symmetric-chain decompositions of a Boolean cube, component balance
is automatic, although Corollary 4 no longer needs it.  Fix either middle
rank.  Every symmetric chain contains exactly one member of that rank.  In
one connected component of the incidence graph, its middle-rank masks are
simultaneously in bijection with the left chains and with the right chains of
that component.

### Corollary 5 (component criterion for orthogonal SCDs)

If two orthogonal SCDs have incidence components containing at most `s`
left chains, their triangular-support bandwidth is at most `s-1`.

This converts a possible construction strategy into a concrete target:
build an orthogonal SCD pair with `s=poly(k)` incidence components, then
solve the still-separate precedence and pinning gates inside and between
those blocks.

Thus a construction whose incidence graph splits into
`poly(k)`-sized components automatically solves the triangular-support gate
with `poly(k)=o(W)` padding.  The forced precedence orders and pinning still
have to be satisfied.  The obstruction isolated here is expansion across all
scales, not local density within a small block.

For the Boolean cube, take `W=binom(k,floor(k/2))`.  Known theorems giving
two orthogonal minimum chain decompositions solve only the cell-collision
condition.  To turn such a pair into a word of length `W+d`, its incidence
graph must additionally satisfy

\[
                              b^+_0(G)\leq d.                      \tag{6.2}
\]

Therefore:

1. choosing two orthogonal decompositions independently, or seeking a
   pseudorandom/expanding incidence graph, points in exactly the wrong
   direction for constant one;
2. even triangular support cannot be deferred until after an abstract
   orthogonal pair has been constructed;
3. an asymptotically sharp construction must produce a recursively nested,
   almost Hall-tight incidence graph together with the chains themselves;
4. after (6.2), the two within-chain precedence digraphs and coordinatewise
   pin survival remain separate conditions.

For the conjectural exact value `nu(k)=B(k)`, the permitted bandwidth is only

\[
          d=B(k)-W=Theta(sqrt(k)).                                \tag{6.3}
\]

Thus an orthogonal-chain proof of the exact conjecture needs a remarkably
strong global layout: a complete flag whose neighborhood excess never
exceeds `Theta(sqrt(k))`.  This is a concrete invariant which can be audited
symbolically on any proposed all-dimensional pair.

The theorem does not obstruct the move-to-front path-cover or Catalan-braid
routes, because those construct endpoint order and chain flags
simultaneously.  It does close the shortcut “first obtain any orthogonal
SCD pair, then order it with sublinear padding.”
