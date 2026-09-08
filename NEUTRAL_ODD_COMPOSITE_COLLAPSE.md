# Collapse of the four-boundary/atomic neutral-odd composite

## 1. Outcome

The formal parity-breaking composite isolated in
`ATOMIC_ALPHA_PARITY_LOCK.md` has an exact local normal form.

Take one endpoint-safe four-boundary transfer and then cancel its canonical
right-hand rank rhombus by the inverse atomic square.  The two steps collapse
to one ledger-neutral two-strand switch on the *left* pair of one-tag
boundaries.  At the edge-set level, the entire segment exchange and right
rhombus disappear.

This gives a sharp obstruction.  A nontrivial one-tag Johnson square
preserves its two individual upper colours if and only if all four lower
vertices lie in one common upper-colour fibre.  Equivalently, the two removed
one-tag edges already have the same upper colour.  Hence no such neutral odd
composite is available in a one-tag colour-simple factor.

The composite is therefore a real parity-breaking move only when a duplicate
one-tag colour is present.  It cannot be the state-closed transposition
generator on an exact one-tag bijection without a separate duplicate
reservoir or a larger colour-cancelling switch word.

## 2. The common-support conditions

Use the notation of the four-boundary exchange:

\[
\begin{aligned}
 P&:\quad \cdots-u-a\,S\,b-v-\cdots,\\
 Q&:\quad \cdots-w-c\,T\,d-z-\cdots.
\end{aligned}
\]

Assume:

1. `P,Q` are vertex-disjoint rooted paths, and `S,T` are interior-disjoint;
2. the removed boundary sectors are `(1,0)` on `P` and `(1,2)` on `Q`;
3. all four exchange joins

   \[
       u-c,\quad d-v,\quad w-a,\quad b-z
   \]

   are one-tag Johnson edges absent from the old factor;
4. the right pair is a canonical rank rhombus: for

   \[
                         K=b\cap v,
   \]

   the two-tag edge is, after possibly exchanging its orientation,

   \[
                         d-z=Kp-Kq,
   \]

   and the inserted right joins are `d-v,b-z`;
5. after the segment exchange, `d-v` and `b-z` belong to distinct rooted
   paths, so the root-preserving inverse atomic orientation is admissible.

Conditions 1--3 are exactly the hypotheses of the four-boundary exchange.
Conditions 4--5 are the additional common-support and dynamic-flippability
requirements for the inverse atomic square.

## 3. Exact cancellation

### Theorem 3.1 (composite collapse)

Under the conditions above, perform the four-boundary exchange and then the
inverse atomic square on `d-v,b-z`.  The final edge set differs from the
initial edge set only by

\[
             \boxed{\{u-a,w-c\}\longrightarrow\{u-c,w-a\}.}
\]

All four displayed edges are one-tag edges.  The net tag ledger is zero, the
lower vertices and roots are preserved, and the terminal owners of `P,Q` are
transposed.

### Proof

The four-boundary exchange removes

\[
                   u-a,\quad b-v,\quad w-c,\quad d-z
\]

and inserts

\[
                   u-c,\quad d-v,\quad w-a,\quad b-z.
\]

By Condition 4, the inverse atomic square removes `d-v,b-z` and restores
`b-v,d-z`.  These four right-boundary changes cancel exactly.  Only the two
left-boundary replacements remain.

Cutting `u-a,w-c` separates the two root-containing prefixes from their
root-free tails.  The cross joins `u-c,w-a` attach each root prefix to the
other tail, so the two terminal owners are transposed.  Every edge removed
or inserted in the surviving switch has tag sector one, proving ledger
neutrality.  \(\square\)

Thus the two-step construction is dynamically legal precisely under the
right-rhombus hypotheses, but its **final** action needs only the left
monochromatic square.  If that left square is directly alternating, applying
it alone produces the same final factor.

## 4. Colour classification of a Johnson square

Let `J(N,k)` be the Johnson graph.  The upper colour of an edge `XY` is its
`(k+1)`-set

\[
                             \gamma(XY)=X\cup Y.
\]

Consider four distinct vertices `u,w,a,c` for which

\[
                 u-a,\quad w-c,\quad u-c,\quad w-a
\]

are Johnson edges.

### Theorem 4.1 (neutral-square classification)

The switch

\[
                 \{u-a,w-c\}\longrightarrow\{u-c,w-a\}
\]

preserves the multiset of upper colours if and only if there is one
`(k+1)`-set `Y` containing all four vertices.  In that case all four edge
colours equal `Y`.

### Proof

Suppose first that the colour multisets agree.  Match the old colour
`u union a` to an equal new colour.

If

\[
                         u\cup a=u\cup c,
\]

then `u,a,c` are all `k`-subsets of the same `(k+1)`-set `Y`.  Equality of
the remaining colours puts `w,a,c` inside another `(k+1)`-set `Y'`.  The
distinct sets `a,c` are both contained in `Y intersect Y'`; their union has
size `k+1`.  Hence `Y=Y'`, and all four vertices lie in `Y`.

In the crossed matching of colours,

\[
                         u\cup a=w\cup a,
\]

so `u,w,a` lie in one `(k+1)`-set `Y`, while the remaining equality puts
`u,w,c` in a `(k+1)`-set `Y'`.  Now the two distinct sets `u,w` force
`Y=Y'` by the same union argument.

Conversely, if all four vertices are `k`-subsets of one `(k+1)`-set `Y`,
the union of every two distinct vertices is `Y`.  All four edge colours are
therefore equal, and the switch is colour-neutral.  \(\square\)

### Corollary 4.2 (duplicate-colour necessity)

A nontrivial colour-neutral one-tag square removes two occurrences of the
same one-tag upper colour and inserts two occurrences of that same colour.
Therefore no such square occurs as an alternating switch in a factor whose
one-tag edge-colour multiplicities are all at most one.

### Corollary 4.3 (exact-bijection no-go)

On a one-tag colour-perfect factor, the four-boundary/inverse-atomic
composite cannot provide any nontrivial pure endpoint transposition while
preserving the one-tag colour bijection.

If the left square is not contained in one colour fibre, its four colours do
not cancel.  Since every old colour in a perfect factor occurs exactly once,
the switch deletes two required colours and duplicates the two newly inserted
colours already owned elsewhere.

## 5. The smallest prism charts

In the one-tag sector all four vertices of a neutral square must share the
same tag and lie among the `k`-subsets of one `(k+1)`-set.  Four distinct
such vertices exist exactly when `k+1>=4`, so the first abstract neutral
square occurs at `k=3`.  It is simply four vertices of the clique

\[
                            K_{k+1}
\]

which is the edge-colour fibre over `Y`.

This finite existence does not help a colour-simple factor: using two old
edges in that clique already requires two occurrences of colour `Y`.

An exhaustive checker can enumerate all complete bipartite Johnson squares
and verify that the colour-neutral ones are exactly these single-fibre
squares.  No dimension-specific exception is needed in the proof.

## 6. Consequence for a state-closed neutral generator

The formal composite does break the parity lock, but only by exposing a
monochromatic one-tag square.  Therefore a viable connected switch system
must do at least one of the following:

1. maintain a controlled duplicate one-tag colour reservoir throughout the
   endpoint-neutralization phase;
2. use a larger word of non-neutral one-tag squares whose colour changes
   cancel globally before returning to a colour-perfect state; or
3. supply a different ledger-neutral odd generator not reducible to one
   Johnson square.

The two-step composite alone does not satisfy the missing dynamic lemma.
Its exact obstruction is targetwise colour multiplicity, not tag-sector
accounting or endpoint parity.

