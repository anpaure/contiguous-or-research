# Companion-graph generation and q1 square transitivity

## Status

The separated-double-swap positional generators

\[
                       g_i=s_i s_{i+m}
\tag{0.1}
\]

generate the alternating group on one shortest-wreath coordinate order.
This note audits that theorem, computes how a swap changes an opened
endpoint matching, and proves a stronger multirow consequence.

In a natural **state-closed** unrestricted host where every positional
generator can be applied diagonally to the two rows on each edge of one
connected companion graph after every preceding word, the joint action is
the full direct product of alternating groups as soon as the graph has at
least three rows.  Moreover one parity sector is already transitive on
every role set occurring in a q1 square.  If each resulting generator
occurrence carries its standard current on the current labels, the dynamic
q1 span is the full coordinate-balanced lattice.

The four-row Tamari associator adds no abstract row-order generator: its
row actions are even permutations of coordinate positions and already lie
in the alternating group.  Its possible value is physical—it may create
the moving companions needed to realize the group words.

The current canonical MSW factor is not proved to satisfy that companion
closure.  Thus this is a sharp conditional positive theorem, not an
all-dimensional q1 coverdown.

No computation or search is used.

## 1. Opened coordinate words and exchange matchings

Put

\[
                         N=2m+1.
\]

Rotate a shortest-wreath omitted-coordinate word so that the distinguished
opening label `infinity` is last:

\[
 w=(i_1,d_1,i_2,d_2,\ldots,i_m,d_m,\infty).
\tag{1.1}
\]

The associated complement geodesic starts at

\[
                         S=\{d_1,\ldots,d_m\}
\tag{1.2}
\]

and exchanges `d_t -> i_t` in that order.  Hence its exchange matching is

\[
                         \eta(d_t)=i_t.
\tag{1.3}
\]

This follows directly from the odd-cycle lift: the two edge labels around
the `t`-th inserted odd vertex are `i_t,d_t`, and the closing edge omits
`infinity`.

### Lemma 1.1 (one adjacent positional swap)

Away from the two opening edges incident with `infinity`, an adjacent
positional transposition acts on `(S,eta)` as follows.

1. Swapping positions `2t,2t+1` reverses the directed token
   `d_(t+1) -> i_(t+1)` and exchanges its two labels between `S` and
   `S^c`.
2. Swapping positions `2t+1,2t+2` transforms the consecutive tokens

   \[
       d_{t+1}\to i_{t+1},\qquad d_{t+2}\to i_{t+2}
   \]

   into

   \[
       i_{t+2}\to i_{t+1},\qquad d_{t+2}\to d_{t+1}.
   \]

   In particular it replaces `d_(t+1)` in the start endpoint by
   `i_(t+2)` and performs a two-edge rewiring of the exchange matching.

The opening-edge cases are the same identities after cyclically recutting
at `infinity`.

#### Proof

Read the even positions in (1.1) as inserted labels and the odd positions
as deleted labels.  A within-token swap interchanges those roles.  A
between-token swap interchanges `d_(t+1)` and `i_(t+2)`; regrouping the
same positions into consecutive even/odd pairs gives the two displayed
tokens.  \(\square\)

Thus inverse-pair moves do not preserve the endpoint/exchange-matching
sector which was invariant under associators alone.

## 2. Audit of the one-row alternating-group theorem

Index cyclic positions by `Z/NZ`, and let

\[
                         s_i=(i\ i+1).
\tag{2.1}
\]

A separated double swap acts by

\[
                         g_i=s_i s_{i+m}.
\tag{2.2}
\]

The two transpositions are disjoint.

### Theorem 2.1 (one-row order group)

For every odd `N=2m+1>=5`,

\[
                         \langle g_i:i\in\mathbb Z_N\rangle=A_N.
\tag{2.3}
\]

#### Proof

Every `g_i` is even.  Since `i+2m=i-1` modulo `N`,

\[
\begin{aligned}
 g_i g_{i+m}
  &=(s_i s_{i+m})(s_{i+m}s_{i+2m})\\
  &=s_i s_{i-1}.
\end{aligned}
\tag{2.4}
\]

The right side is a three-cycle on three consecutive positions.  The
consecutive three-cycles generate `A_N`, proving equality.  \(\square\)

Equation (2.4) also confirms that the cancellation in the original proof
does not require a hidden commutation: the two middle transpositions are
literally identical and adjacent in the product.

The unavoidable one-row invariant is the parity of the full cyclic
coordinate order.  Lemma 1.1 shows that endpoint matching and token-order
parity are not invariants once the `g_i` are admitted.

## 3. Diagonal actions on a companion graph

Let `Gamma` be a graph whose vertices are shortest-wreath rows.  For an
edge `uv` and `g in A_N`, write

\[
 D_{uv}(g)=(1,\ldots,g_u,\ldots,g_v,\ldots,1)
            \in A_N^{V(\Gamma)}.
\tag{3.1}
\]

This is the abstract action of applying the same row-order word to one
compatible inverse-pair companion pair.

### Theorem 3.1 (connected companion graph generation)

Suppose that, on every edge `uv` of `Gamma`, all diagonal actions
`D_uv(g)`, `g in A_N`, are available.  On a connected component `K`:

* if `|K|=1`, the generated group is trivial;
* if `|K|=2`, it is the diagonal copy of `A_N`;
* if `|K|>=3`, it is the full direct product

  \[
                           A_N^K.
  \tag{3.2}
  \]

#### Proof

Only the third case needs proof.  A connected graph with at least three
vertices has a length-two path `u-v-w`.  For `g,h in A_N`, the commutator

\[
             [D_{uv}(g),D_{vw}(h)]
\tag{3.3}
\]

is the identity on every row except `v`, where it acts by `[g,h]` (up to
the harmless inverse convention).  For `N>=5`, `A_N` is perfect, so its
commutators generate all of `A_N`.  Hence arbitrary isolated actions are
available at `v`.

If `x` is adjacent to a vertex at which isolated actions are available,
multiply `D_xv(g)` by the inverse isolated action at `v`; this isolates
`g` at `x`.  Induction along a spanning tree isolates arbitrary actions at
every vertex.  These isolated copies generate (3.2).  \(\square\)

It is enough physically to supply the generators `g_i` on every companion
edge, because Theorem 2.1 then supplies every `g in A_N`.  The theorem
assumes closure while the word is performed; time-zero availability of the
edges alone is not enough.

## 4. One parity sector contains every q1 square type

A lower-form q1 square is

\[
 \square(Z;r,s\mid a,d)
 =[Z+r+a]+[Z+s+d]-[Z+r+d]-[Z+s+a],
\tag{4.1}
\]

where `|Z|=m-3` and the four displayed labels are distinct outside `Z`.
It therefore names

\[
                         (m-3)+4=m+1
\tag{4.2}
\]

coordinate roles.

### Lemma 4.1 (alternating-group role transitivity)

`A_N` is transitive on injective assignments of any `t<=N-2` named roles
to distinct positions.

#### Proof

Choose any permutation giving the desired assignment.  If it is odd,
compose it with a transposition of two unnamed positions.  There are at
least two such positions, and this parity correction fixes every named
role.  \(\square\)

Since `m+1<=2m-1=N-2` for `m>=2`, Lemma 4.1 applies to (4.2).

### Theorem 4.2 (state-closed unrestricted-host q1 span)

Assume the companion host of Theorem 3.1 is state-closed in the following
literal sense: after every generated word, every edge `uv` and every slot
`i` again supports the native inverse-pair move `g_i`, and that occurrence
has the standard four-term current on the labels presently occupying its
roles.  Then one component of at least three rows exposes inverse-pair
currents of every square type (4.1).  Consequently its dynamic signed q1
span is the full coordinate-balanced lattice.

#### Proof

Use Theorem 3.1 to arrange, immediately before one final generator, the
labels in its `m+1` current roles.  Lemma 4.1 sends those roles to the roles
of any prescribed square, and the remaining unnamed positions absorb the
parity correction.  State closure guarantees that the final generator is
still a literal inverse-pair occurrence and therefore emits that prescribed
square.  Hence every square occurs somewhere in the dynamic orbit.  The
integer square-generation theorem says that these squares generate the
entire coordinate-balanced lattice.  \(\square\)

This proves that the one-row parity sector is not a q1-current obstruction:
q1 squares leave enough unnamed coordinates to correct parity.

## 5. The four-row associator in the combined group

The port-restored associator permutes four exchange tokens on each named
row and fixes the tensor tail.  A permutation of equal two-coordinate
blocks has coordinate-position sign

\[
                         (\operatorname{sgn}\sigma)^2=+1.
\tag{5.1}
\]

Hence every row action of the associator belongs to `A_N`.  Abstractly it
adds nothing to the group in Theorem 2.1, just as its q1 current adds
nothing to the static current span.

Its role is instead to alter the physical decomposition and possibly the
companion graph `Gamma`.  A useful theorem must show that these zero-current
reconfigurations create the edges required by Theorem 3.1 without losing
the protected rails.

## 6. Exact physical remainder

The combined algebra is now complete on the following conditional face:

\[
 \boxed{
 \begin{array}{c}
 \text{connected companion graph with at least three rows}\\
 +\text{ every }g_i\text{ remains plantable along its edges}
 \end{array}
 \Longrightarrow
 \text{full q1 balanced-lattice reachability}.}
\tag{6.1}
\]

The canonical MSW inverse pairs currently give a large matching-like
collection of `2`-cycles, not a proved connected, generator-complete
companion graph.  After one swap, the companion required for the next
`g_i` need not exist.  The four-row associator has the correct zero-q1
character but no theorem says it reconnects these companions.

Thus the exact remaining statement is:

> **Moving-companion closure.**  Zero-current associators and native
> inverse-pair moves generate, on a protected set of at least three rows, a
> connected companion graph closed under the positional generators
> `g_i`, while retaining the all-width rails and last providers.

This is strictly smaller than arbitrary coordinate-conjugate plantability.
It is also the point at which occurrence geometry, rather than permutation
group or q1 lattice algebra, enters.
