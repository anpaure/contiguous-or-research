# Hypergraph audit of cyclic-interval SCD resolutions

> **Status correction.**  The middle-only matching problem discussed in
> Sections 1--2 is already solved exactly: the Mütze--Standke--Wiechert
> minimum-change Chung--Feller construction gives a spanning
> `C_(2m+1)`-factor of the odd graph, hence an exact wreath factor.  See
> `ODD_GRAPH_EXACT_WREATH_FACTOR.md`.  The codegree calculations remain
> correct, but the claim that even the approximate middle statement is an
> open theorem is obsolete.  The unresolved content is the vertical
> extension.  Its exact form is the nested-matching criterion in
> `MSW_ATOM_FLOW.md`; the quotient-lifting and initialization audit is in
> `CYCLIC_INTERVAL_LIFT_INITIALIZATION_AUDIT.md`.

This note asks whether the approximate cyclic-interval SCD conjecture can be
obtained from a standard hypergraph matching theorem.  The answer is more
delicate than the first pair-codegree heuristic suggests.

There are two distinct facts.

1.  The middle-layer wreath hypergraph is exactly regular and its full
    pair-codegree sequence is elementary.  However, its maximum codegree is
    `Theta(D/m)`, not `Theta(D/m^2)`: almost-complementary middle sets are the
    obstruction.
2.  A one-shot hypergraph whose edges are vertically resolved cyclic orders
    has even stronger chain-internal clustering.  Existing fixed-uniformity
    Pippenger--Rödl theorems do not apply in this diagonal regime.

Thus the desired approximate theorem is not currently a black-box consequence
of a nibble.  The calculations below identify the exact diagonal matching
statement that would be sufficient.

## 1. The middle wreath hypergraph

Put

\[
 n=2m+1,
 \qquad
 \mathcal V=\binom{[n]}m,
 \qquad
 W=|\mathcal V|=\binom nm.
\]

Let `H_m` be the simple `n`-uniform hypergraph on `V` whose edges are the
wreaths

\[
 \mathcal W_\pi=
 \bigl\{
   \{x_j,x_{j+1},\ldots,x_{j+m-1}\}:j\in\mathbb Z_n
 \bigr\},                                                        \tag{1.1}
\]

where `pi=(x_0,...,x_(n-1))` is a cyclic order.  Reversal gives the same
wreath.

For `m>=2`, a wreath determines its cyclic order up to reversal.  Indeed, the
Johnson-adjacency graph induced by its `n` middle sets is an `n`-cycle; along
each edge the deleted and inserted coordinates reconstruct the underlying
coordinate cycle.  Hence

\[
                         |E(H_m)|=(n-1)!/2.                       \tag{1.2}
\]

### Theorem 1 (exact degrees and pair codegrees)

`H_m` is regular of degree

\[
                         D=\frac{m!(m+1)!}{2}.                    \tag{1.3}
\]

If `S,T` are distinct middle sets and

\[
                         q=|S\setminus T|=|T\setminus S|,
\]

then their codegree is

\[
 \lambda_q=(q!)^2(m-q)!(m+1-q)!,                                \tag{1.4}
\]

and therefore

\[
 \boxed{
 \frac{\lambda_q}{D}
   =\frac{2}{\binom mq\binom{m+1}q}.
 }                                                               \tag{1.5}
\]

In particular,

\[
 \frac{\Delta_2(H_m)}D=\frac{2}{m+1},                           \tag{1.6}
\]

attained when `S,T` are disjoint.

#### Proof

Regularity follows either by transitivity or by double counting incidences:

\[
 D=\frac{((n-1)!/2)n}{\binom nm}
   =\frac{m!(m+1)!}{2}.
\]

Suppose first that directed cyclic orders, modulo rotation but not reversal,
are counted.  Anchor `S` in positions `0,...,m-1`.  If `T` starts `q` places
clockwise, the four consecutive atoms have sizes

\[
 q,\quad m-q,\quad q,\quad m+1-q.
\]

Their internal orders are arbitrary.  The second orientation gives the same
factor, so the directed count is

\[
                 2(q!)^2(m-q)!(m+1-q)!.
\]

Quotienting by reversal proves (1.4).  Formula (1.5) follows by division by
(1.3).  Its denominator is minimized at `q=m`, where it is `m+1`, proving
(1.6).  QED.

The location of the maximum matters.  The shallow Johnson pairs `q=1` have
relative codegree

\[
                         \frac{2}{m(m+1)},                        \tag{1.7}
\]

but disjoint middle sets have relative codegree `2/(m+1)`.

### Odd-graph reformulation

Let

\[
                         O_{m+1}=KG(2m+1,m),
\]

the odd graph whose vertices are the middle sets and whose edges join disjoint
pairs.  Its odd girth is `2m+1`.  The wreaths (1.1), read in the step order
`j -> j+m+1`, are precisely its cycles of minimum odd length.

Indeed, consecutive sets in that step order are disjoint.  Conversely, the
equality case in the standard odd-girth proof for the odd graph shows that a
`(2m+1)`-cycle successively exposes every one of the `2m+1` omitted
coordinates, and hence reconstructs a cyclic coordinate order; its vertices
are exactly the length-`m` intervals of that order.

Consequently the middle-only approximate wreath statement is equivalently

> find a `C_(2m+1)`-packing in the odd graph covering all but `o(W)`
> vertices.

This graph formulation explains (1.6): the maximum codegrees belong to pairs
which are themselves edges of the odd graph.  It may be a better starting
point for absorption than the unstructured wreath hypergraph.  The odd graph
is `(m+1)`-regular and distance-transitive, while the desired tiles are exactly
its minimum-length odd cycles.

### A first higher-codegree cluster

Fix a middle set `S`, let `C=[n]\setminus S`, and choose distinct `x,y in C`.
Put

\[
                         T=C\setminus\{x\},
 \qquad                   U=C\setminus\{y\}.
\]

In any wreath containing all three, `T,U` are the two length-`m` windows
disjoint from `S`.  Counting the two possible endpoint assignments in a
directed order and then quotienting by reversal gives

\[
 \deg(S,T,U)=m!(m-1)!,
 \qquad
 \frac{\deg(S,T,U)}D=\frac{2}{m(m+1)}.                           \tag{1.8}
\]

Thus the large pair codegrees occur in tightly described clusters and collapse
by another factor `m` after a third compatible vertex is prescribed.  This is
exactly the kind of higher-codegree information a diagonal nibble would need
to exploit.

## 2. Why the standard matching black boxes do not settle it

The auxiliary hypergraph has

\[
 |V(H_m)|=W=\exp(\Theta(m)),
 \qquad
 |e|=n=\Theta(m),
 \qquad
 \Delta_2/D=\Theta(1/m).                                         \tag{2.1}
\]

The classical Pippenger--Rödl theorem is stated with edge uniformity fixed
before the error parameters are chosen.  It cannot be diagonalized merely
from `Delta_2/D -> 0` when `|e|=2m+1` also tends to infinity.

The quantitative Grable criterion

\[
 \Delta_2=o\!\left(\frac{D}{|e|\log |V|}\right)                  \tag{2.2}
\]

is much stronger than what is available here: the right normalized scale is
`Theta(1/m^2)`, whereas (1.6) is `Theta(1/m)`.

The 2025 full-codegree nibble theorem of Gould--Kelly allows a parameter no
larger than

\[
 B\le\sqrt{D/\Delta_2}=\Theta(\sqrt m).                           \tag{2.3}
\]

For fixed uniformity this would already force an `o(W)` leftover.  Its stated
hierarchy, however, is

\[
 1/D\ll1/A\ll\gamma\ll1/k,
\]

where the uniformity is `k+1`, and its leftover contains the factor
`B^{-1+gamma} log^A D`.  With `k=2m`, this statement supplies no diagonal
conclusion: `A` must grow faster than `m`, while `B` is only polynomial in
`m`.

Therefore even the following middle-only assertion remains a genuine theorem
to prove in this parameter range:

> **Diagonal approximate wreath statement.**  The hypergraph `H_m` has a
> matching covering `W-o(W)` middle sets.

This statement is weaker than the exact Baranyai--Katona wreath conjecture but
is not certified by the usual fixed-rank nibble citation.

## 3. The one-shot vertically resolved hypergraph

The middle packing alone does not resolve the lower and upper layers.  To see
the scale of a one-shot formulation, fix a central depth `h` and define

\[
 N_q=\binom n{m-q},
 \qquad
 \rho_q=N_q/W,
 \qquad 0\le q\le h.                                             \tag{3.1}
\]

A resolved cyclic order chooses a radius `d_j` at every one of its `n` starts.
At depth `q`, the number

\[
                         t_q=|\{j:d_j\ge q\}|                    \tag{3.2}
\]

of active chains should average

\[
                         n\rho_q,                                \tag{3.3}
\]

because there are `W/n` blocks and `N_q` targets in each of the two ranks
`m-q` and `m+1+q`.  Integer floor/ceiling profiles can realize (3.3) up to a
total `O(W/n)` discrepancy per rank.

One resolved block contains

\[
                         R=2\sum_{q=0}^{h}t_q                    \tag{3.4}
\]

Boolean-lattice vertices.  When `h/sqrt(n)->infinity`,

\[
                         R=\Theta(n^{3/2}).                       \tag{3.5}
\]

By permutation symmetry, a mixture of the floor and ceiling profiles has an
exact fractional perfect matching: within every rank all vertex degrees are
equal, and (3.3) makes the normalized degrees equal between ranks.

This fractional solution does **not** round by an immediate Pippenger
argument.  If `S` has rank `s` and `T=S union {x}`, then, conditioned on `S`
being one of the selected intervals of a random resolved order, `T` can be the
same-chain extension when `x` is placed at either adjacent endpoint.  This has
probability `Theta(1/m)`.  Thus the resolved-block hypergraph has

\[
                         \Delta_2/D'=\Omega(1/m),                 \tag{3.6}
\]

while its edge size is `Theta(m^(3/2))`.  The clustering is intrinsic: entire
symmetric-chain segments are deliberately selected together.

The correct matching object should therefore quotient or expose these chain
segments rather than treat every Boolean set in a resolved block as an
independent hypergraph vertex.  A plausible proof has two stages:

1. select an almost-SCD of compatible interval chains;
2. bundle their middle flags into almost-disjoint wreath cycles.

The one-shot block hypergraph hides precisely the structure needed to control
its large codegrees.

## 4. Dyck-height profiles exactly satisfy the radius ledger

There is nevertheless a canonical solution to the **numerical** threshold
problem.  Let `D_m` be the set of Dyck paths of semilength `m`.  For a path
`P` and a vertex time `j in {0,...,2m}`, let `h_P(j)` be its height.

### Theorem 2 (pointed-Dyck radius identity)

For every `0<=d<=m`,

\[
 \boxed{
 \#\{(P,j):P\in\mathcal D_m,\ h_P(j)=d\}
   =\binom{2m+1}{m-d}-\binom{2m+1}{m-d-1}.
 }                                                               \tag{4.1}
\]

#### Proof

Cut a pointed Dyck path at its marked height-`d` vertex as `P=P_1P_2`.
Reverse `P_2` in time and interchange up/down steps; this gives a nonnegative
path `Q` from height `0` to height `d`.  Concatenate

\[
                         P_1,\quad U,\quad Q+d+1.                 \tag{4.2}
\]

The result is a nonnegative ballot path of length `2m+1` ending at height
`2d+1`.

Conversely, in such a ballot path take the last up-step from height `d` to
height `d+1`.  The prefix before it is a nonnegative path from `0` to `d`, and
the suffix, shifted down by `d+1`, is a nonnegative path from `0` to `d`.
Reverse and interchange the steps of the latter path to recover `P_2`.  These
maps are inverse.

The ballot theorem counts the paths in (4.2) by the right side of (4.1).
QED.

The right side of (4.1) is exactly the forced number of radius-`d` chains in
an SCD of `B_(2m+1)`.  Thus the `2m+1` cuts of all `Catalan_m` Dyck paths give
the required threshold multiset with no rounding at all:

\[
                         d_{P,j}=h_P(j).                           \tag{4.3}
\]

This connects the cyclic-interval SCD target directly to the strengthened
wreath conjectures of Petr--Turek, which attach one cyclic permutation to each
Dyck path.  Their conjecture would solve the middle wreath partition and (4.3)
would solve the radius ledger.  What remains nonautomatic is the vertical
statement that the fixed-start intervals selected by those heights partition
each noncentral rank.  The small-codegree calculation above shows why that
additional statement should not be silently delegated to a generic matching
theorem.

## 5. Exact next theorem

The most useful purely mathematical target is now one of the following.

### Two-stage form

Construct `W-o(W)` pairwise disjoint symmetric chains, each consisting of
fixed-start intervals in some cyclic order, such that their middle members can
be bundled into cyclic orders with only `o(W)` discarded chains.

### Diagonal matching form

Prove a growing-uniformity nibble/absorption theorem tailored to `H_m` which
uses the exact pair-codegree sequence and the observed collapse in the
largest explicit cluster,

\[
 \Delta_2/D=\Theta(1/m),
 \qquad
 \deg(S,C\setminus\{x\},C\setminus\{y\})/D=\Theta(1/m^2),
\]

and first prove the corresponding global higher-codegree bounds for all
configurations.  The resulting theorem should return a matching leaving
`o(W)` vertices.

Even this second statement only settles the middle layer.  A full
`W+o(W)` OR construction still requires the vertical interval-chain packing,
for which the Dyck-height profile (4.3) is the natural exact ledger.
