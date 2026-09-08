# The corrected decorated-two-factor target has an exact flow and relational root

Date: 2026-07-31  
Status: exact reductions and exact relational composition; no all-dimension
decorated two-factor is claimed

## 0. Verdict and hierarchy

Put `D2F(m)` for the corrected decorated-two-factor assertion on
`ML(2m-1)`: the two turn palettes are globally bijective, selected shore
types alternate cyclically on every marked factor component, and every
component passes the corrected trace test

\[
 \mathsf{Acc}(w)=
 \begin{cases}
 1,&w=0^{2q},\\
 0,&w=1^{2q},\\
 0,&0<|w|_1<2q,\text{ every zero-run has length }2
                    \text{ and every one-run is odd},\\
 1,&\text{otherwise}.
 \end{cases}                                      \tag{0.1}
\]

The all-one rejection is load-bearing.  The original candidate statement
without it is false already at `m=3`: one fully marked factor cycle supplies
both palettes exactly but lifts to two physical rail cycles.

After this correction, `D2F(m)` implies the Catalan Linear Matching
statement.  It is the weakest **currently stated Middle-Levels-resolvable**
sufficient target, not an equivalence with arbitrary Catalan linear
matchings.

This note gives three exact ways to use the weaker target.

1. For a proposed diamond matching, support by *some* Middle Levels
   two-factor is an integral bipartite `b`-flow.  There are no subtour,
   Hamiltonicity, or voltage rows.
2. For a fixed two-factor, decoration is exactly upper-turn surjectivity,
   one upper representative per colour, one aggregate labelled gap--colour
   perfect matching, and the constant-state test (0.1).
3. On a normalized recursive decomposition, the full correlated relation
   of factor degrees, occurrence matching, and trace fragments composes by
   natural join and existential projection.  Its empty-boundary accepting
   root is equivalent to `D2F(m)`.  No component-merging state is present.

The positive `ML(7)` hexagon theorem is an accepting finite fixture for this
minimal route.  Its fixed-decoration transparent gluing rule is a stronger
diagonal subrelation and must not be promoted to a necessary D2F condition.

## 1. The exact factor-extension flow

Let

\[
 G=ML(2m-1)
\]

with bipartition

\[
 {\cal A}=\binom{[2m-1]}{m-1},\qquad
 {\cal B}=\binom{[2m-1]}m.
\]

Let `M` be a perfect matching of the Boolean diamond graph on
`[2m-1] union {infinity}`.  Define its forced Middle Levels support
`Theta(M)` as follows.

* A cross diamond contributes its literal edge `A--B` of `G`.
* A diamond whose physical Johnson edge lies on the `B` rail contributes
  the unique length-two path `B_0--A--B_1` of `G`.
* A diamond whose physical edge lies on the `infinity+A` rail contributes
  the unique length-two path `A_0--B--A_1`.

Repeated support edges are retained once.  The centre of either length-two
path is the corresponding marked occurrence.

### Theorem 1.1 (factor-extension equivalence)

For a perfect diamond matching `M`, the following are equivalent.

1. `M` is induced by a componentwise decoration of some spanning
   two-factor `F` of `G`.
2. `Theta(M)` is contained in a spanning two-factor of `G`.
3. Every vertex has `deg_Theta(v)<=2`, and, after putting

   \[
     b(v)=2-\deg_{\Theta(M)}(v),\qquad
     E_0=E(G)\setminus E(\Theta(M)),                 \tag{1.1}
   \]

   the system

   \[
      x_e\in\{0,1\},\qquad
      \sum_{e\in E_0:e\ni v}x_e=b(v)\quad(v\in V(G))             \tag{1.2}
   \]

   is feasible.

#### Proof

`1 -> 2` is literal: every selected turn uses its two incident factor edges,
and every residual cross diamond uses one factor edge.

For `2 -> 1`, let `F` contain `Theta(M)`.  Mark the centre of every
same-rail diamond and leave the cross-diamond endpoints unmarked.  Since
`M` is perfect, the cross diamonds form a perfect matching `R` between all
unmarked `A`- and `B`-occurrences.  On a factor component containing marks,
deleting the marked vertices leaves paths perfectly matched by `R`; hence
those paths have even order, so consecutive marks, including the
wraparound pair, lie on opposite shores.  On a factor component containing
no mark, `R` is one of its two alternating phases.  The diamond matching
uses every untagged upper colour and every tagged lower colour exactly once,
so the two selected turn palettes are globally bijective.  Thus `M` is the
componentwise decoration induced by `F`.

Finally, a set `X subseteq E_0` completes `Theta(M)` to degree two at every
vertex exactly when its incidence vector solves (1.2).  A finite simple
graph of degree two at every vertex is a spanning two-factor.  This proves
`2 iff 3`.  \(\square\)

### Corollary 1.2 (integral Hall/cut certificate)

Orient every residual edge from `A` to `B`, give it capacity one, put an arc
of capacity `b(a)` from a source to every `a in A`, and an arc of capacity
`b(b)` from every `b in B` to a sink.  Then (1.2) is feasible if and only if
the maximum flow has value

\[
                    D=\sum_{a\in{\cal A}}b(a).
\]

Equivalently, for every `X subseteq A` and `Y subseteq B`,

\[
 b(X)\le |E_0(X,Y)|+b({\cal B}\setminus Y).          \tag{1.3}
\]

The network matrix is totally unimodular, so fractional feasibility is
integral.  Equation (1.3) is the capacity of the cut whose source side is
`{source} union X union (B\Y)`.

### Corollary 1.3 (a direct exact D2F target)

`D2F(m)` is equivalent to the existence of a perfect diamond matching `M`
such that

1. its physical Johnson lift `Psi(M)` is a forest; and
2. the flow of Corollary 1.2 has value `D`.

Indeed Theorem 1.1 supplies the supporting two-factor, and the forest
hypothesis forces every one of its component traces to pass (0.1).
Conversely a corrected decorated two-factor supplies both rows.

The flow row is a genuine restriction of the Middle Levels-resolvable
subclass.  The authenticated `m=3` linear diamond matching in the trace
equivalence theorem has four degree-three vertices in `Theta(M)` and hence
fails before the flow, although its physical lift is already a five-path
forest.

## 2. Two matchings and the exact fixed-factor cascade

Every spanning bipartite two-factor is the edge-disjoint union

\[
                         F=f\mathbin{\dot\cup}g       \tag{2.1}
\]

of two perfect inclusion matchings `f,g:A->B`.  Put

\[
                         \sigma=g^{-1}\circ f.        \tag{2.2}
\]

The cycles of `sigma` are exactly the factor components.  The two turn maps
are

\[
 \tau^+(a)=f(a)\cup g(a),\qquad
 \tau^-(b)=f^{-1}(b)\cap g^{-1}(b).                 \tag{2.3}
\]

Thus Hamiltonicity is only the optional stronger demand that `sigma` have
one cycle.

Fix `F`.  An **upper occurrence SDR** is a set `I subseteq A` containing one
occurrence of every rank-`m+1` value of `tau+`.  Such a set exists exactly
when `tau+` is surjective: each occurrence has one colour, so different
colours never compete for the same occurrence.

For every `sigma`-cycle meeting `I`, cut its cyclic occurrence order at the
chosen `A`-occurrences.  The resulting oriented open intervals are the
`I`-gaps.  A `B`-occurrence lies in the unique gap between the preceding and
following selected `A`-occurrences.  Define the occurrence-labelled
gap--colour graph

\[
                         H(F,I)                      \tag{2.4}
\]

with the `I`-gaps on the left, the rank-`m-2` lower colours on the right,
and one edge `(gap,c;b)` for every `B`-occurrence `b` in that gap satisfying
`tau-(b)=c`.

### Theorem 2.1 (fixed-factor gap theorem)

For fixed `F` and fixed upper SDR `I`, componentwise Catalan decorations
having upper marks `I` are in bijection with perfect matchings of `H(F,I)`.
Components disjoint from `I` are wholly unmarked.  The edge label `b` chosen
at a gap is its selected lower occurrence.

#### Proof

On a marked factor component, cyclic alternation says that exactly one
selected `B`-occurrence lies between each consecutive pair of selected
`A`-occurrences.  Global lower-palette bijectivity says that the selected
`B` turn colours enumerate the right shore of (2.4) exactly once.  These are
precisely the two endpoint constraints of a perfect matching of `H(F,I)`.
Conversely such a matching selects one `B` in every gap and one occurrence
of every lower colour, giving cyclic alternation and both palettes.  A
component with no selected `A` cannot contain a selected `B`, since a
nonempty cyclic alternating list has equally many marks of the two shores.
\(\square\)

### Corollary 2.2 (exact obstruction cascade)

For a fixed factor, corrected D2F feasibility is exactly:

1. `tau+` is surjective and one upper representative per colour is chosen;
2. `H(F,I)` has a perfect matching; and
3. the resulting trace on every active `sigma`-cycle passes (0.1).

The first nontrivial Hall row is Step 2, not Step 1.  Step 2 simultaneously
enforces lower surjectivity, component balance, and occurrence interlacing.

The partially marked bad language is

\[
                 \operatorname{Cyc}((1(11)^*00)^+),                 \tag{2.5}
\]

plus the separate all-one face.  It is constant-state.  A literal protected
substring `0110` is an immediate trace breaker.  Also, if every active
component has at least one `I`-gap spanning at least four `A`-steps, then
every choice of its one lower mark leaves a zero-run of length at least
four; in that sufficient subface, Step 2 alone proves linearity.

## 3. Exact relational induction with an accepting root

Let a rooted decomposition expose factor edges, turn choices, residual
occurrence edges, and the corresponding chronology fragments.  Normalize
it so that every occurrence whose eventual two factor neighbours are not
both known remains on the boundary.

At a node `x`, retain the relation `Sigma_x` of **all** internally realizable
tuples carrying:

1. used factor degree `0,1,2` at every boundary occurrence;
2. augmented matching degree `0,1` and mark state `turn/residual/open` at
   every boundary matching vertex;
3. for every oriented open trace fragment, its first and last bit, capped
   boundary zero-run lengths, boundary one-run parity, the homogeneous
   type `all-zero/all-one/mixed`, a breaker bit, and its ordered boundary
   endpoint identities/pairing; and
4. no already sealed factor component failing (0.1).

Every tuple also enforces the literal local support coupling

\[
                         \Theta(M)\subseteq F:        \tag{3.1}
\]

each selected turn forces both incident factor edges, while each selected
residual/cross diamond forces its literal factor edge.  Separate factor and
augmented-matching degree equations without (3.1) are only marginal
projections and are not sufficient.

For a mixed fragment, zero lengths need only distinguish `0,1,2,3+`, and
one lengths only their parity.  Concatenation closes the two seam runs and
updates the breaker.  The homogeneous type is essential: it distinguishes
the safe unmarked cycle from the forbidden wholly marked cycle.

### Theorem 3.1 (D2F relational composition)

The parent relation is obtained exactly by:

1. natural-joining one tuple from each child with one choice of the local
   factor and augmented edges, subject to the support coupling (3.1);
2. rejecting factor degree above two or augmented matching degree above
   one;
3. requiring every forgotten factor vertex to have degree two and every
   forgotten augmented vertex to be matched exactly once;
4. concatenating the literal oriented trace fragments; and
5. whenever a factor component is sealed, applying (0.1), rejecting on
   failure, deleting its trace summary, and existentially projecting all
   forgotten boundary data.

At the empty boundary, `Sigma_root` contains an accepting tuple if and only
if the assembled object is a corrected componentwise decorated spanning
two-factor.

#### Proof

Restrict any global corrected D2F witness to the edge sets of the child
subproblems.  Factor and matching degrees agree on shared boundary vertices,
the literal factor order cuts its component traces into exactly the stored
fragments, and every component closed below the boundary passes (0.1).
Thus restriction produces tuples accepted by Steps 1--5.

Conversely, compatible child witnesses and local choices have disjoint
interiors.  The degree checks glue them to a spanning two-factor and a
perfect augmented occurrence matching.  Trace concatenation is literal and
associative; only runs incident with a seam can change.  Every component is
tested exactly once when its final port closes.  The empty-root state
therefore has both palette bijections, componentwise alternation, and the
corrected forest trace on every component.  This is exactly D2F.  \(\square\)

This theorem is an exact relational induction, not an all-dimension
existence proof.  Its state is finite for every finite boundary, but the
number of live palette vertices and trace fragments has not been proved
uniformly bounded in the standard recursion.  The missing theorem is
nonemptiness of this correlated root relation, or a structural subclass
which guarantees it.

## 4. The role of the positive `ML(7)` hexagon

The frozen `ML(7)` theorem supplies an explicit accepting D2F root: its one
factor component is Hamilton, its two palettes are exact, its selected
occurrences alternate, and a zero-run of length six passes (0.1).  Its
physical lift is a spanning `Cat_4=14`-path forest.

Around that fixture there are `31` alternating incidence hexagons, `16`
Hamilton outputs, `10` decorable outputs, and `6` transparent outputs
admitting a common forest decoration.  For a fixed decoration, transparency
is exactly:

1. equality of the selected local turn-colour multisets separately on the
   two shores; and
2. alternation of the retained-fragment boundary mark types after
   reconnection.

This is a useful local transition inside `Sigma`, but it is the diagonal
condition that the *same* decoration survives.  A D2F proof may instead
move to a different tuple of the relation, split components, or never merge
them.  Separate lower and upper rainbows do not imply the aggregate
gap--colour matching and therefore are insufficient.

## 5. Exact scope

The proved statements are:

* the corrected factor-to-diamond implication;
* the exact factor-extension max-flow/Hall certificate;
* the fixed-factor upper-SDR plus labelled gap-matching equivalence; and
* exact relational composition with the corrected per-component accepting
  rule.

They do **not** prove an accepting root for every `m`, a bounded-width
recursion, or an all-dimension D2F construction.  Alternating-circuit
connectivity between two-factors is existential and may use global circuits;
it gives no bounded/local/ECO-only packet and need not preserve a decoration
at intermediate states.

Finally, even D2F for all `m` settles only the central Catalan Linear
Matching object.  Strict residence, deeper shadows, sockets/chronology, and
the integral common-cap compiler remain separate downstream gates for
`nu(k)=B(k)`.
