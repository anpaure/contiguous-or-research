# The two-sided Catalan lift: exact transfer formulation and symmetry obstruction

This note continues `CATALAN_COMPRESSED_LIFT.md`.  It does not prove the
missing all-dimensional two-sided theorem.  It does three things that narrow
that theorem substantially:

1. it gives an exact directed transfer-graph normal form for every
   Catalan-compressed middle cycle;
2. it gives a necessary-and-sufficient integral path-flow system for making
   the lower adjacent shadow complete; and
3. it proves that the tempting complement--reversal symmetrization is
   impossible for every nontrivial dimension.  In particular, the Catalan
   path components cannot be paired under complement--reversal, even up to a
   bounded exceptional family.

Throughout, let

\[
 \Omega=[2m],\qquad
 \mathcal M=\binom{\Omega}{m},\qquad
 \mathcal U=\binom{\Omega}{m+1},
\]

and put

\[
 M=|\mathcal M|=\binom{2m}{m},\qquad
 N=|\mathcal U|=\binom{2m}{m+1},\qquad
 K=M-N=\operatorname {Cat}_m.
\tag{0.1}
\]

For a Johnson edge `XY` in the middle layer, write

\[
 u(XY)=X\cup Y\in\mathcal U,
 \qquad
 \ell(XY)=X\cap Y\in\binom{\Omega}{m-1}.
\tag{0.2}
\]

## 1. The directed transfer graph

Define the **transfer graph** `G_m` on vertex set `mathcal U` by joining
`U,V` when

\[
                         |U\cap V|=2.                 \tag{1.1}
\]

We use both orientations of every edge.

### Lemma 1 (Johnson edges are transfer arcs)

There is a bijection

\[
 \{\hbox{middle Johnson edges}\}
 \longleftrightarrow
 \{\hbox{directed arcs }U\to V\hbox{ of }G_m\}
\tag{1.2}
\]

given by

\[
 XY\longmapsto
 \bigl(X\cup Y\bigr)\longrightarrow
 \bigl(\Omega\setminus(X\cap Y)\bigr).
\tag{1.3}
\]

If `U cap V={a,b}`, the inverse arc has the unique middle edge

\[
 \left(U\setminus\{a\}\right)
 \left(U\setminus\{b\}\right).                         \tag{1.4}
\]

Complementing both endpoints of a middle edge reverses its transfer arc.

#### Proof

For a middle edge put `S=X cap Y` and `U=X union Y`.  Then `|S|=m-1`,
`|U|=m+1`, and `S subset U`.  If `V=Omega minus S`, then

\[
 U\cap V=U\setminus S,
\]

which has size two.  Conversely, (1.1) implies `U union V=Omega`.  Hence
`S=Omega minus V` is an `(m-1)`-subset of `U`, and writing
`U minus S={a,b}` gives exactly the edge (1.4).  The two constructions are
inverse.  Complementation swaps union with the complement of intersection,
so it sends `U to V` to `V to U`.  QED.

Thus the tail of a transfer arc is its upper colour, while its head is the
complement of its lower colour.  The two-sided shadow problem is therefore a
directed vertex-coverage problem on one copy of the `(m+1)`st layer:

\[
 \begin{array}{c|c}
 \hbox{upper colours complete}&\hbox{every vertex occurs as a tail},\\
 \hbox{lower colours complete}&\hbox{every vertex occurs as a head}.
 \end{array}                                             \tag{1.5}
\]

## 2. Exact block-transfer normal form

Let

\[
 R=(U_0,U_1,\ldots,U_{N-1})                             \tag{2.1}
\]

be a cyclic Hamilton order in `J(2m,m+1)` for which the seams

\[
 C_i=U_{i-1}\cap U_i\in\mathcal M                       \tag{2.2}
\]

are all distinct.  This is exactly the upper order supplied by a saturating
cycle.  Let

\[
 \mathcal L=\mathcal M\setminus\{C_0,\ldots,C_{N-1}\},
 \qquad |\mathcal L|=K.                                  \tag{2.3}
\]

For block `U_i`, define its incoming and outgoing deletion labels

\[
 p_i=U_i\setminus C_i,
 \qquad
 q_i=U_i\setminus C_{i+1}.                               \tag{2.4}
\]

They are distinct.  Assign every `X in mathcal L` to one upper set
`f(X) superset X`.  The active deletion labels in block `i` are

\[
 A_i=\{p_i,q_i\}\cup
 \{a\in U_i: U_i\setminus\{a\}\in\mathcal L,
                  f(U_i\setminus\{a\})=U_i\}.           \tag{2.5}
\]

Choose a simple path `H_i` in the complete graph on `A_i`, starting at
`p_i`, ending at `q_i`, and visiting every label in `A_i` once.  For an edge
`{a,b}` of this path, define its transfer head

\[
             h_i(a,b)=U_i^c\cup\{a,b\}\in\mathcal U.    \tag{2.6}
\]

### Theorem 2 (exact transfer-path equivalence)

The following data are equivalent.

1. A Hamilton cycle `P` through `mathcal M` such that every upper colour
   occurs in one nonempty contiguous run and the compressed upper-colour
   order is `R`.
2. An assignment `f` as above and terminal Hamilton paths `H_i` on the
   active label sets (2.5).

Under this equivalence, the transfer arcs of block `i` are exactly

\[
                      U_i\longrightarrow h_i(a,b)
            \qquad(\{a,b\}\in E(H_i)).                  \tag{2.7}
\]

Consequently, `P` also covers every lower colour if and only if

\[
 \boxed{
   \{h_i(a,b):0\le i<N,\ \{a,b\}\in E(H_i)\}
       =\mathcal U .}
\tag{2.8}
\]

#### Proof

Replace a deletion label `a` in block `U_i` by the middle facet
`U_i minus {a}`.  The path `H_i` becomes a middle Johnson path from `C_i` to
`C_(i+1)`, and every one of its edges has upper colour `U_i`.  Consecutive
blocks share their seam vertex.  The seams and the assigned members of
`mathcal L` partition `mathcal M`, so concatenating the blocks gives a
Hamilton middle cycle.

Conversely, cut such a middle cycle whenever its upper colour changes.
Every internal vertex in its `U_i` block is a nonseam facet of `U_i`, hence
gives its unique assignment to `U_i`; deletion labels recover `H_i`.

For consecutive labels `a,b`, the middle endpoints are those in (1.4), so
Lemma 1 gives precisely the head (2.6).  Lower colour `S` occurs exactly when
the head `Omega minus S` occurs.  This proves (2.8).  QED.

The theorem is asymmetric on purpose.  The saturating cycle solves all tail
constraints.  The remaining theorem is to make the heads surjective while
using only `K` assignable nonseam facets.

## 3. A necessary-and-sufficient integral path-flow system

Theorem 2 can be written without any hidden ordering choices.  This is useful
both as a proof target and as a source of min--max obstructions.

For every `X in mathcal L` and `i` with `X subset U_i`, introduce a binary
assignment variable `y_(X,i)`.  For every pair `a,b in U_i`, introduce a
binary path-edge variable `x_(i,ab)`.  Put

\[
 z_{i,a}=
 \begin{cases}
 1,&a\in\{p_i,q_i\},\\
 y_{(U_i\setminus\{a\},i)},
   &U_i\setminus\{a\}\in\mathcal L,\\
 0,&\text{otherwise}.
 \end{cases}                                             \tag{3.1}
\]

Consider the following finite zero--one system.

**Assignment equations**

\[
       \sum_{i:X\subset U_i}y_{X,i}=1
                   \qquad(X\in\mathcal L).              \tag{3.2}
\]

**Terminal path degrees**

\[
 \sum_{b\in U_i\setminus\{a\}}x_{i,ab}
 =\begin{cases}
   1,&a=p_i\text{ or }a=q_i,\\
   2z_{i,a},&a\notin\{p_i,q_i\}.
  \end{cases}                                            \tag{3.3}
\]

**Forest inequalities**

For every nonempty `D subset U_i` and every `c in D`, require

\[
 \sum_{\{a,b\}\in\binom D2}x_{i,ab}
 \le \sum_{a\in D}z_{i,a}-z_{i,c}.                      \tag{3.4}
\]

**Head-cover inequalities**

\[
 \sum_i\ \sum_{\substack{\{a,b\}\in\binom{U_i}2\\
                  U_i^c\cup\{a,b\}=V}}
            x_{i,ab}\ge1
                 \qquad(V\in\mathcal U).               \tag{3.5}
\]

### Theorem 3 (integral path-flow criterion)

For a fixed saturating order `R`, a two-sided Catalan-compressed middle cycle
exists if and only if the binary system (3.2)--(3.5) is feasible.

#### Proof

In a feasible solution, (3.2) activates every nonseam facet in exactly one
block.  Equation (3.3) gives degree one to the two terminals, degree two to
every active internal label, and degree zero to every inactive label.
Inequality (3.4), choosing an active `c`, says that every induced subgraph on
active labels has at most one fewer edge than vertices; hence the selected
graph is a forest.  Its degree sum from (3.3) shows that it has exactly
`|A_i|-1` edges.  It is therefore connected and is a Hamilton `p_i`--`q_i`
path on `A_i`.  Condition (3.5) is exactly (2.8), so Theorem 2 applies.

Conversely, paths from Theorem 2 give their incidence vectors `x`, and the
facet assignment gives `y`.  A path satisfies (3.3)--(3.4), while lower
completeness gives (3.5).  QED.

This criterion separates three genuinely different gates:

\[
 \text{facet assignment flow}
 \quad+\quad
 \text{terminal path forests}
 \quad+\quad
 \text{global head cover}.                              \tag{3.6}
\]

An ordinary perfect matching between upper and lower colours sees only the
last marginal.  It does not enforce (3.2), the path degrees, or the subtour
inequalities, so it is not sufficient.

## 4. If both sides compress, the Catalan hooks must interleave exactly

Suppose more strongly that the lower colours of `P` also occur in one
contiguous run each.  Let the `M` cyclic edge positions of `P` carry transfer
arcs

\[
                         U_j\longrightarrow V_j.         \tag{4.1}
\]

Let `B_+` be the set of gaps `j|j+1` at which the tail changes, and `B_-`
the set at which the head changes.

### Theorem 4 (Catalan boundary-interleaving law)

For every simultaneously run-compressed two-sided cycle,

\[
 |B_+|=|B_-|=N,\qquad B_+\cup B_-=\mathbb Z_M,           \tag{4.2}
\]

and therefore

\[
 \begin{aligned}
 |B_+\cap B_-|&=2N-M=M-2K,\\
 |B_+\setminus B_-|&=K,\\
 |B_-\setminus B_+|&=K.
 \end{aligned}                                          \tag{4.3}
\]

Equivalently, the `K` gaps internal to upper-colour runs and the `K` gaps
internal to lower-colour runs are disjoint, and every other gap terminates
both runs.

#### Proof

There are `N` nonempty runs in each colour word, so each boundary set has
size `N`.  If neither colour changed at a gap, two consecutive edge positions
would carry the same ordered pair `(U,V)`.  Lemma 1 says that `(U,V)`
determines one unique middle Johnson edge, so the Hamilton cycle would repeat
an edge.  Hence the union in (4.2) is all `M` gaps.  Inclusion--exclusion and
`K=M-N` give (4.3).  QED.

At a lower-colour boundary, the complements `V_j,V_(j+1)` are Johnson
adjacent: the two distinct lower colours are `(m-1)`-subsets of the shared
middle vertex.  Their seam is the complement of that middle vertex.  Thus
compressing the head runs gives a second saturating cycle.  Theorem 4 is the
exact compatibility law between the two saturating cycles: their two
Catalan-sized internal-boundary families must be disjoint and perfectly
interleaved.  This is substantially stronger than constructing the two
cycles independently.

## 5. Complement--reversal cannot pair the Catalan path components

The exact wreath factor on `2m+1` coordinates has the following
distinguished-coordinate form on the even core.  It partitions `mathcal M`
into `K` Johnson paths

\[
          P=(X_0,X_1,\ldots,X_m),\qquad X_m=X_0^c.       \tag{5.1}
\]

For such a path define

\[
 P^*=(X_m^c,X_{m-1}^c,\ldots,X_0^c).                    \tag{5.2}
\]

Upper colours of `P^*` are complements of lower colours of `P`, and vice
versa.  This makes closure under `P mapsto P^*` look tempting.  It is in fact
impossible.

### Theorem 5 (no complement--reversal-invariant path factor)

For every `m>=2`, no vertex-disjoint factor of `mathcal M` into paths (5.1)
is invariant under `P mapsto P^*`.

More strongly, no single path (5.1) satisfies `P=P^*`.

#### Proof

By (5.1), the transformed path has the same **ordered** endpoints:

\[
 P_0^*=X_m^c=X_0,qquad P_m^*=X_0^c=X_m.                 \tag{5.3}
\]

If a vertex-disjoint path factor were invariant, `P^*` would have to be the
unique component containing `X_0`.  Hence `P^*=P` pointwise, so

\[
                         X_i=X_{m-i}^c                   \tag{5.4}
\]

for every `i`.

If `m` is even, (5.4) at `i=m/2` makes an `m`-set equal to its complement,
which is impossible.  If `m` is odd, put `i=(m-1)/2`.  Then (5.4) makes the
two consecutive middle vertices `X_i` and `X_(i+1)` complementary.  For
`m>=2` they are disjoint, not Johnson-adjacent.  This is again impossible.
QED.

### Corollary 6 (Catalan-scale rewiring is unavoidable)

An invariant factor cannot retain even one of the original complementary-
endpoint path components unchanged.  Any complement-based repair must cut or
reassign all `K=Cat_m` components; an all-but-`O(1)` pairing is impossible.

This does not rule out a Catalan-scale global splice--`K=W/(m+1)=o(W)`--but
it proves that complement symmetry is not a free property of the MSW/GMM
factor.  The required splice is exactly as large as the Catalan defect.

The same central-edge obstruction shows that a Hamilton path through all
middle sets cannot be fixed by reverse-complement either: `M` is even, so
the two central consecutive vertices would have to be complements.

## 6. Even complement-invariant cycles are too restrictive at `m=2`

The path obstruction might suggest replacing reverse-complement symmetry by
a half-turn complement symmetry of a Hamilton **cycle**.  This also fails as
a general route, already in the first nontrivial case.

### Proposition 7

There is no complement-invariant Hamilton cycle in `J(4,2)` whose upper
union colours cover all four triples.

#### Proof

The six middle vertices form three complement pairs

\[
 A=\{12,34\},\qquad B=\{13,24\},\qquad C=\{14,23\}.
\]

Complementation has no fixed vertex and fixes no Johnson edge, so on an
invariant Hamilton `6`-cycle it acts as a half-turn.  The quotient is the
triangle `ABC`, and one complement orbit of Johnson edges is selected over
each quotient edge.

Label a middle edge by the unordered pair `{s,t}`, where `{s}` is its lower
intersection and its upper union is `Omega minus {t}`.  The two edges in its
complement orbit jointly supply the two upper colours missing `s` and `t`.
The orbit over `AB` has label one of the two pairs in `C`; cyclically, the
three selected labels choose one edge from each of the three perfect
matchings `A,B,C` of `K_4`.

Such a transversal is either a triangle on three coordinates or a star on
all four.  (The natural `S_4` action has these two orbits; one representative
of each is checked immediately.)  The lifted quotient is one `6`-cycle
exactly in the triangle case; in the star case it is two disjoint triangles.
But all four upper colours occur exactly in the star case, because the label
edges must touch all four coordinates.  Hamiltonicity and upper completeness
are therefore incompatible.  QED.

The obstruction is genuinely about symmetry, not about two-sided existence.
For example

\[
 12,13,23,24,34,14                                      \tag{6.1}
\]

is a Hamilton cycle in `J(4,2)`.  Its upper colour word is

\[
 123,123,234,234,134,124,
\]

one run for every triple, and its lower colour word is

\[
 1,3,2,4,4,1,
\]

which covers every singleton.  The successful object is necessarily
asymmetric.

## 7. Exact remaining theorem

The saturating-cycle Catalan compression is already solved.  The missing
two-sided theorem can now be stated without reference to a raw middle array:

> **Two-sided transfer-path theorem.**  For every `m`, choose a saturating
> upper order `R`, allocate the `K` nonseam middle facets, and choose the
> terminal label paths `H_i` so that their transfer heads cover `mathcal U`.
> Equivalently, prove feasibility of (3.2)--(3.5).

The stronger simultaneous-compression form must additionally realize a
second saturating cycle and obey the exact boundary interleaving law (4.3).

Theorem 5 eliminates the most obvious proposed shortcut: neither the MSW
paths nor all but a bounded number of them can simply be paired with their
reverse complements.  A successful proof must use asymmetric, Catalan-scale
cross-component rewiring, or solve the integral transfer system directly.

