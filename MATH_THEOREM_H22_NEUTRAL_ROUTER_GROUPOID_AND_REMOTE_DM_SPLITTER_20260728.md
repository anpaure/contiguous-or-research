# Neutral legality routers and remote DM-circuit splitters at Hall 22

Date: 2026-07-28

Status: theorem-grade structural reduction plus one exact certified instance.
The frozen `H23 -> H23 -> H22` pair proves that a rank-neutral braid may act
in one DM component solely to make a splitter legal in a different component.
It also gives one genuine common-word/native-pin gain on the old critical DM
shore.  What is **not** proved is transitivity of neutral braids over the
remaining circuits.  In fact, the strong interpretation as one group
conjugating one splitter seed to every circuit is false: strict physical
conjugacy preserves component type, and the surviving Hall-22 shore has at
least seven types.

The exact surviving theorem target is a state-dependent groupoid orbit-hitting
statement for fully decorated splitter germs.  This note proves the algebra
which makes that hypothesis sufficient, identifies its precise common-`Q`
decoration, and reduces the next Hall descent to a concrete nested-cell portal
at one of five remaining `2/1` circuits (or to an analogous portal at another
unit-defect component).

## 1. Weak carrier states and pin-decorated lifts

Fix a depth `d`.  A **weak protected carrier state** is a tuple

\[
             \mathfrak X^{\rm wk}=(T,P,G,\mathcal I),            \tag{1.1}
\]

with the following data.

1. `T` is a deck-exact Johnson chronology.
2. `P=E_d(T)` is its nonzero maximal erosion controller.
3. `G=G(T)` is the physical target/cell compiler graph.
4. `I` records the protected residence and shadow assertions, together with
   existential exterior matching capacity or a residual-shore certificate.
   In the
   `k=15,d=3` application these are depth-three residence and complete upper
   support at every depth `q=1,...,7`, together with whatever lower-support
   conditions are explicitly requested.

A **pin-decorated lift** additionally records a designated target/cell
injection `Pi` and one explicit physical word realizing all of its pins.
The distinction is essential: unrelated native atlases may exist at two
weak endpoints without transporting one fixed pin family between them.

Write

\[
 h(\mathfrak X)=|L(G)|-\nu(G)                                    \tag{1.2}
\]

for its Hall deficiency.  The matching graph belongs to the weak state; a
common-word certificate belongs only to a pin-decorated lift.  The former
does not imply the latter.

For a selected pin family

\[
                    \Pi=\{(I_\alpha,S_\alpha)\}_\alpha,
\]

put

\[
 Z_x(\Pi)=\bigcup_{\alpha:x\notin S_\alpha}I_\alpha,
 \qquad
 E_x(P)=\{p:x\in P_p\},
 \qquad
 K_x(P,\Pi)=E_x(P)\setminus Z_x(\Pi).                            \tag{1.3}
\]

The exact common-`Q` theorem says that one nonzero word realizes the central
row and every selected pin if and only if

\[
 K_x\cap[i,i+d]\ne\varnothing
       \quad(i,\ x\in T_i),                                      \tag{1.4}
\]

\[
 K_x\cap I_\alpha\ne\varnothing
       \quad(\alpha,\ x\in S_\alpha),                            \tag{1.5}
\]

and

\[
                    \bigcup_xK_x=V.                              \tag{1.6}
\]

The maximal realizing word is

\[
                    A_p=\{x:p\in K_x\}.                          \tag{1.7}
\]

These Boolean conditions are the meaning of common-`Q` below.

## 2. Weak neutral braids form a groupoid; pin lifts form a category

An elementary signed three-cut braid has the form

\[
 A\mid B\mid C\mid D
       \longmapsto
 A\mid C^\epsilon\mid B^\delta\mid D,
 \qquad \epsilon,\delta\in\{+,-\},                              \tag{2.1}
\]

where a minus sign reverses a block.  Call (2.1) **weak protected neutral**
when both endpoints are weak protected states with the same deficiency and
every declared endpoint invariant in `I` holds.

### Theorem 2.1 (weak groupoid and pin-transition category)

Weak protected neutral signed braids and their finite concatenations form a
groupoid `N_h^wk` on the weak deficiency-`h` states.  The loops
`N_h^wk(X,X)` at a fixed state form a group.  Pin-decorated transitions,
however, form only a directed category in general.  Their reversibly
certified arrows form a subgroupoid.  There is no single unconditional group
acting on all carriers or on all DM circuits.

#### Proof

A signed block exchange is a bijection of the ordered deck.  On its output
partition, swap the same two middle blocks and undo their signs; this is
again one of the four signed forms in (2.1), and it recovers the input
word.  Protectedness and equality of Hall deficiency are properties of the
two endpoint states, so they hold in both directions.  Concatenation is
associative, the empty path is an identity, and reversing a path gives its
inverse.

The available weak arrows depend on the source chronology: Johnson seam
legality, residence, shadow support, and Hall neutrality are state-dependent.
Thus their natural object is a groupoid, and only the isotropy at one state is
an honest group.

For a pin-decorated arrow, the reverse block permutation need not transport
the selected target/cell injection or preserve its Boolean conditions
(1.4)--(1.6).  Composition still makes sense, so these arrows form a directed
category; inversion exists only when reverse pin transport is separately
certified.  \(\square\)

This distinction is substantive twice over.  A Hall-neutral braid need not
induce any map between the old and new DM components.  It can instead change
the global chronology so that a physically unrelated splitter becomes legal.
And a weak orbit hit plus two endpoint native certificates is not yet a path
in the global pin-decorated category.

## 3. Splitter germs and the exact transport condition

Let `C` be an excess-one target component in a compiler graph:

\[
 |C|=|N(C)|+1,
 \qquad
 \nu(G[C,N(C)])=|C|-1.                                           \tag{3.1}
\]

Its exposed-root set is

\[
 \rho(C)=\{x\in C:C\setminus\{x\}
                    \text{ is matchable into }N(C)\}.            \tag{3.2}
\]

A **pointed splitter germ** at a protected state `X` consists of

\[
 \gamma=(s:\mathfrak X\to\mathfrak X^+,C,M_{\rm ext}),          \tag{3.3}
\]

where `s` is a protected physical exchange, `C` is the component to be
discharged, and `M_ext` is a specified exterior matching which is retained
or explicitly rerouted by `s`.

A neutral morphism `r:X->Y` transports this germ only when there are arrows
`r^+:X^+->Y^+` and `s^r:Y->Y^+` making the square

\[
\begin{array}{ccc}
 \mathfrak X&\xrightarrow{s}&\mathfrak X^+\\
 \big\downarrow r&&\big\downarrow r^+\\
 \mathfrak Y&\xrightarrow{s^r}&\mathfrak Y^+
\end{array}                                                       \tag{3.4}
\]

commute as signed deck permutations, and whose compiler and Boolean pin maps
identify the pointed local germ and the retained exterior.  The commuting
square is not automatic from Hall neutrality.

For an exchange `s:G->G^+`, define its shore current by

\[
 J_s(A)=|N_{G^+}(A)|-|N_G(A)|.                                  \tag{3.5}
\]

### Theorem 3.1 (protected conjugation preserves every cut current)

Suppose (3.4) has target bijection `alpha` and old/new physical-cell
bijections which are compiler-graph isomorphisms on the pointed component
and retained exterior.  Then

\[
                         J_{s^r}(\alpha A)=J_s(A)                 \tag{3.6}
\]

for every shore on which those isomorphisms are defined.  Component rank
gain, exposed-root reachability, exterior matching survival, and Hall descent
are therefore transported exactly.  If the Boolean pin data also transport
as in Theorem 7.1 below, deck, shadows, residence, and common-`Q` are all
preserved.

#### Proof

The two graph isomorphisms separately preserve the old and new neighbourhood
cardinalities.  Subtraction gives (3.6).  Transport the local and exterior
matchings through the cell bijections.  The remaining assertions are exactly
the protected endpoint and Boolean hypotheses in the commuting square.
\(\square\)

### Corollary 3.2 (exact orbit--stabilizer routing test)

Assume compatible **reversible pin-decorated** commuting-square lifts make
pointed splitter germs into a groupoid action.  Fix a state `X`, its isotropy
group

\[
                         H_X=\mathcal N_h^{\rm pin}(X,X),
\]

a seed germ `gamma_0` at circuit `C_0`, and the stabilizer
`H_{C_0}`.  If `C=g_C C_0`, then the possible circuit transporters are the
coset

\[
                         g_C H_{C_0}.                             \tag{3.7}
\]

Let `A_C` be the set of collar-, matching-, shadow-, residence-, and
common-`Q`-legal splitter attachments at `C`.  A transported seed exists at
`C` if and only if

\[
            (g_CH_{C_0}\cdot\gamma_0)\cap\mathcal A_C
                         \ne\varnothing.                          \tag{3.8}
\]

Thus transitivity on unpointed circuits is insufficient: the stabilizer must
also place the complete physical germ into a legal attachment.

## 4. The universal one-seed conjugation claim is false

### Proposition 4.1 (strict physical orbit invariants)

A transport satisfying the compiler isomorphism hypotheses of Theorem 3.1
preserves at least

\[
 (|C|,|N(C)|),                                                    \tag{4.1}
\]

the target-rank histogram, target and cell degree/codegree data, native pin
depths, and, under coordinate relabelling, the cardinality of the component
root.  Consequently two pointed components with different values of any of
these data cannot be strict conjugates.

#### Proof

All listed incidence data except coordinate rank are invariants of a
bipartite graph isomorphism with its pointed cells.  A permutation of the
ground coordinates preserves target cardinality and intersections, hence the
rank histogram and root cardinality as well.  \(\square\)

The root-`20516` diamond germ has type `161/160` and target-rank profile

\[
                         (1,9,43,108),                            \tag{4.2}
\]

whereas the discharged `{4877,4909}` germ has type `2/1` and target ranks
six and seven.  They are not conjugate.  More generally the Hall-22 DM shore
contains components of the seven size types

\[
 169/168,\ 161/160,\ 160/159,\ 5/4,\ 3/2,\ 2/1,\ 1/0.            \tag{4.3}
\]

So strict physical conjugacy has at least seven orbits, before finer
chronology and common-`Q` invariants are imposed.  Even the seven isolated
`1/0` components split into at least two coordinate-conjugacy types: five
roots have rank six and two have rank seven.

Therefore the statement “one neutral braid group conjugates one legal
splitter to every remaining circuit” is false in its strong literal sense.
The H23-to-H22 route is a stateful legality preconditioner followed by a
remote splitter, not a conjugation of the root-`20516` diamond.

## 5. Remote splitters do not require component conjugation

The following matching lemma captures the weaker and useful architecture.

### Theorem 5.1 (remote router plus component saturation)

Let

\[
 \mathfrak X\xrightarrow{r}\mathfrak Y
              \xrightarrow{s}\mathfrak Z                         \tag{5.1}
\]

be protected carrier arrows and put

\[
                 n=\nu(G_\mathfrak X)=\nu(G_\mathfrak Y).
\]

Assume:

1. `r` is Hall-neutral;
2. `C` is an excess-one component at `Y` with an internal matching of size
   `|C|-1`;
3. there is an exterior matching `M_ext` of size

   \[
                   n-(|C|-1)                                    \tag{5.2}
   \]

   whose target endpoints avoid `C`;
4. after `s`, `M_ext` survives or is rerouted with the same size, and `C`
   has a matching of size `|C|` on right cells disjoint from `M_ext`.

Then

\[
                         \nu(G_\mathfrak Z)\ge n+1,
 \qquad
                         h(\mathfrak Z)\le h(\mathfrak X)-1.      \tag{5.3}
\]

If `G_Z` has a shore of gap `h(X)-1`, equality holds in (5.3).  The router
and splitter may act on completely different DM components.

#### Proof

The union of the rerouted exterior matching and the size-`|C|` matching on
`C` has size

\[
                 n-(|C|-1)+|C|=n+1.
\]

This proves the lower bound on matching rank.  A surviving shore of gap
`h(X)-1` gives the reverse Hall bound.  Nothing in this argument identifies
the component changed by `r` with `C`.  \(\square\)

### Lemma 5.2 (exposed-root ear)

Retain all old cells of an excess-one component `C` and add one new cell
`c`.  The component becomes saturated if and only if

\[
                         N(c)\cap\rho(C)\ne\varnothing.           \tag{5.4}
\]

#### Proof

If `x` lies in (5.4), match `c` to `x` and use a matching of
`C-{x}` into the old cells.  Conversely, in a perfect matching the new cell
is matched to some `x`, and deleting that edge leaves a matching of
`C-{x}` into the old cells.  \(\square\)

A braid may delete cells while adding others, so Lemma 5.2 alone is not a
physical exchange theorem.  The retained/rerouted exterior and local bases
in Theorem 5.1 are essential.

### Lemma 5.3 (cut-perfect `2/1` splitter)

Let `C={x,y}` have one old restricted cell shore `{x,y}`.  Replace it by two
distinct restricted shores `{x}` and `{y}`.  For every (A\subseteq C),

\[
 |N_{\rm new}(A)|-|N_{\rm old}(A)|
             =\mathbf 1[C\subseteq A].                           \tag{5.5}
\]

Hence every proper cut is unchanged and the full circuit gains exactly one
neighbour.  With the exterior hypothesis of Theorem 5.1, global matching
rank rises by one.

#### Proof

The old neighbour count is zero for (A=\varnothing) and one for every nonempty
`A`.  The new neighbour count is `|A|`.  Their difference is (5.5).  The two
new singleton cells match `x` and `y`.  \(\square\)

The zero-component analogue replaces no cell by one singleton cell and has
current `1[z in A]`.

### Proposition 5.4 (portal test without a component action)

Let `M` be a maximum matching of `G_Y`, let `M_0` be the subset of its edges
which survive in `G_Z`, and put

\[
                  r=|M|-|M_0|.                                  \tag{5.6}
\]

Let `alpha` be the maximum number of pairwise vertex-disjoint
`M_0`-augmenting paths in `G_Z`.  Then

\[
 \nu(G_Z)=|M_0|+\alpha,
 \qquad
 h(Z)=h(Y)+r-\alpha.                                             \tag{5.7}
\]

In particular, the exchange descends precisely when `alpha>=r+1`.

#### Proof

Augmenting along `alpha` disjoint paths gives a matching of the first size in
(5.7).  Conversely, the symmetric difference of `M_0` with any larger
matching contains exactly the matching-size difference many vertex-disjoint
`M_0`-augmenting paths.  Maximality of `alpha` gives the reverse inequality.
The deficiency identity follows from (5.6).  \(\square\)

This formulation is often sharper than trying to make a neutral braid act on
the DM components: it directly tests whether the reached state exposes a
legal splitter portal.

## 6. Exact H23 -> H23 -> H22 remote instance

Use the frozen carriers

\[
\begin{array}{c|c}
\text{state}&\text{SHA-256}\\ \hline
H23&8feab1da65f3924d29609246798fc543dc50d076ca9db363e8796dda2c22598d\\
H23^{\rm portal}&9f6c2631ca0ffdd24aa0f9b4cf979b223995251e4c241cef4ad61a67026646b6\\
H22&c4d36b5972a07e8c7694a741bbc5cc4a5d657ef13c434bd42433b0fc51b01798.
\end{array}                                                       \tag{6.1}
\]

The moves are

\[
 H23\xrightarrow{\operatorname{RF}(3799,4497,6039)}H23^{\rm portal}
 \xrightarrow{\operatorname{FR}(740,4051,6137)}H22.              \tag{6.2}
\]

The matching ranks and deficiencies are

\[
             16360/23\longrightarrow16360/23
                         \longrightarrow16361/22.                 \tag{6.3}
\]

The canonical DM shore sizes are

\[
             1007/984\longrightarrow1007/984
                         \longrightarrow1005/983,                 \tag{6.4}
\]

and the first two shores have the identical target digest

```text
88895c0ced520217a65802ba03060bf7ff2ed3aec192c90c6e666585f76b5c89.
```

The cross-gap matrix, with graph state indexing rows and the three canonical
shores indexing columns, is

\[
 \begin{pmatrix}
 23&23&22\\
 23&23&22\\
 22&22&22
 \end{pmatrix}.                                                   \tag{6.5}
\]

Thus the first move is exactly neutral and the second gains exactly one
matching rank.  Their full common-core contractions are

\[
 16350+10\longrightarrow16350+10,
 \qquad
 16343+17\longrightarrow16343+18.                                \tag{6.6}
\]

### 6.1 Exact seven-block chronology

Split the original H23 path `Q` at

\[
                 740,3799,4497,5788,6040,6138                   \tag{6.7}
\]

into blocks `A,...,G` of lengths

\[
                 (740,3059,698,1291,252,98,297).                 \tag{6.8}
\]

Then the three chronologies are exactly

\[
\begin{aligned}
 H23&=A B C D E F G,\\
 H23^{\rm portal}&=A B E^-D^-C F G,\\
 H22&=A D^-C F E B^-G.
\end{aligned}                                                     \tag{6.9}
\]

The final six seams lie at cumulative positions

\[
                         740,2031,2729,2827,3079,6138.           \tag{6.10}
\]

This direct form is useful for any future collar proof: the two elementary
collars overlap and cannot be added as independent ledgers.

### 6.2 The neutral move is a remote packet rotation

Inside the `161/160` component rooted at `24610`, put

\[
\begin{aligned}
 X&=\{24610,24611,24674,24675\},\\
 Y&=\{24614,24615,24678,24679\},\\
 Z&=\{28707,28770,28771\}.
\end{aligned}                                                     \tag{6.11}
\]

After cancelling every unchanged restricted cell shore, the neutral braid
is exactly

\[
                 \{Y,X\cup Z\}\longmapsto\{X\cup Y,Z\}.         \tag{6.12}
\]

It replaces two cells by two cells, preserves total restricted incidence
`11`, and keeps the component rank `160`.  The second braid makes **zero**
restricted-signature change in this component.  Thus root `24610` is only a
chronology router; it is not the discharged component.

### 6.3 The remote `2/1` circuit is split perfectly

Before and after the neutral braid, the complete restricted profile on

\[
                         C=\{4877,4909\}                          \tag{6.13}
\]

is one cell shore `{4877,4909}`.  The improving braid replaces it by exactly

\[
                         \{4877\},\qquad\{4909\}.                 \tag{6.14}
\]

The final physical cells are

\[
\begin{array}{c|c|c|c|c}
\text{cell}&(e,s)&E(c)&F(c)&(P_s,\ldots,P_{s+e})\\ \hline
7178&(1,740)&4877&4612&(781,4365)\\
13614&(2,739)&4909&4652&(809,781,4365).
\end{array}                                                       \tag{6.15}
\]

Here `E(c)` is the controller envelope and `F(c)` the mandatory mask.  Their
native traces are respectively `4877` and `4909`.  Moreover

\[
 4877\subset4909,
 \qquad
 F(13614)\not\subseteq4877                                    \tag{6.16}
\]

because the added bit `32` is mandatory in the second cell.  Thus the first
cell excludes `4909` by its envelope, while the second excludes `4877` by
its mandatory mask.  This proves the two singleton signatures directly.

The final canonical DM target shore is exactly the old shore minus
`{4877,4909}`; no target is added.  Equations (6.12)--(6.16) are therefore an
exact instance of Theorem 5.1 and Lemma 5.3.

### 6.4 Protected ledger

Every state in (6.2) is a permutation of all `6435` rank-eight masks, a
Johnson path, depth-three resident, and complete in every upper support layer
`q=1,...,7`.  The seven zero-candidate targets are unchanged.  The lower
support-hole vectors are

\[
 (4,19,6,1,0,0,0),\quad
 (4,19,6,1,0,0,0),\quad
 (4,18,6,1,0,0,0).                                               \tag{6.17}
\]

The second move gains the depth-two target `4877`; no lower support is lost.
Neither upper nor lower occurrence multiplicities are asserted invariant.
In particular, “preserves all upper shadows” here means complete support,
not equality of multiplicity vectors.

## 7. Exact common-`Q` transport

Hall neutrality or target-multiset preservation says nothing by itself about
(1.4)--(1.6).  The needed decoration is Boolean and position-sensitive.

Define the support-restricted omission bit

\[
 \beta_x(p)=\mathbf 1[p\in E_x(P)\cap Z_x(\Pi)].                 \tag{7.1}
\]

### Theorem 7.1 (decorated common-`Q` transport)

Let a protected braid carry `(P,Pi)` to `(P',Pi')`, let `alpha` be a
coordinate permutation, and let `theta` be the signed position isometry away
from the changed collars.  Suppose outside those collars

\[
 E_{\alpha x}(P')=\theta E_x(P),
 \qquad
 \beta'_{\alpha x}(\theta p)=\beta_x(p).                          \tag{7.2}
\]

Suppose also that:

1. every transported central or positive-pin demand retains its transported
   `K_x` anchor;
2. every new or collar-crossing positive pin has a `K'_x` anchor;
3. every central demand meeting a collar satisfies (1.4); equivalently, on
   each internal controller run its two forced endpoints survive and every
   gap between surviving pins is at most `d+1`;
4. every collar point core

   \[
   C'_p=P'_p\cap
        \bigcap_{\alpha:p\in I_\alpha}S_\alpha                  \tag{7.3}
   \]

   is nonempty.

Then the final state has one common literal compiler.  Equality of the full
forbidden unions `Z'_{alpha x}=theta Z_x` is a stronger sufficient condition,
but (7.2) is the exact off-collar invariant.

#### Proof

Equation (7.2) gives

\[
                         K'_{\alpha x}=\theta K_x                \tag{7.4}
\]

off the collars.  Hypotheses 1--3 check (1.4)--(1.5) on all transported and
changed intervals.  Hypothesis 4 is exactly (1.6) inside a collar, while
(7.4) transports it outside.  Apply the maximal common-`Q` criterion
(1.4)--(1.7).  \(\square\)

### Lemma 7.2 (native pins and native ears)

For an interval `I`, define its native controller trace

\[
                         \tau_P(I)=\bigcup_{p\in I}P_p.           \tag{7.5}
\]

A native pin `(I,tau_P(I))` is negative-inert: adjoining it changes none of
the sets `K_x`.  Relative to a pre-existing exceptional pin family, it is
compiler-safe if and only if

\[
                  I\cap K_x\ne\varnothing
                  \qquad(x\in\tau_P(I)).                         \tag{7.6}
\]

In particular, an injective all-native atlas is simultaneously realized by
the unmodified word `A=P`.

#### Proof

If `x` is absent from `tau_P(I)`, then `x` is absent from every `P_p` on
`I`.  The new forbidden interval therefore removes no eligible occurrence
from `E_x(P)`, proving negative inertness.  Its positive requirements are
exactly (7.6).  In the all-native case, no native negative constraint removes
any eligible controller occurrence, so `K_x=E_x(P)` and every native trace
is realized by `P`.  \(\square\)

### Corollary 7.3 (statewise native-basis router)

At every endpoint `X_j`, suppose an injective family of physical cells has
distinct native traces forming a protected target set `B_j`.  Then the one
maximal controller `P_j` realizes all of `B_j`.  Thus a neutral braid
preserves existence of a common compiler for this partial atlas whenever

\[
                         B_{j+1}=B_j,                             \tag{7.7}
\]

even if the physical cells are rebaselined rather than transported
pin-by-pin.  If a splitter changes the basis to `B_j union {u}`, it pays one
literal native-pin unit.

This corollary is weaker than preserving an arbitrary exceptional/global
matching, but stronger than a projected Hall assertion.

### 7.4 Exact H22 native-basis gain

The H23 and portal states each possess `984` distinct native DM-right pins
with the same target basis `B_0`.  The H22 canonical DM shore has `983`
distinct native pins.  Adjoining the two cells in (6.15) gives `985`
distinct cells and targets, all simultaneously realized by the **one** final
maximal controller, and

\[
                         B_2=B_0\cup\{4877\}.                    \tag{7.8}
\]

On the old `1007`-target H23 shore, the literal native/common-`Q` gap is

\[
                         1007-985=22.                             \tag{7.9}
\]

Thus (6.2) pays one genuine literal compiler unit on the critical old shore,
not merely one Hall-rank unit.

The exact scope is important: this is a `985`-pin partial compiler.  It does
not produce a common word for a full matching of size `16361`, nor for all
`16383` nonempty targets.

### Proposition 7.4 (unlabelled pin transport is insufficient)

Even the cell family and label multiset do not determine common-`Q`.  At
`d=3`, take a local constant controller

\[
                         P_p=\{x,a,b,c\}
\]

and disjoint intervals

\[
 I_1=[1,2],\qquad I_2=[3,4],\qquad I_3=[7,8].                    \tag{7.10}
\]

Let

\[
 A=\{a,b,c\},\qquad B=\{a,b\},\qquad C=\{x,a,b,c\}.             \tag{7.11}
\]

The assignment `(A,C,B)` leaves an `x` occurrence in every four-position
central window.  The relabelled assignment `(A,B,C)`, with the same intervals
and label multiset, deletes `x` throughout `[1,4]` and violates the central
window `[1,4]`.  Positive pin demands and point nonemptiness can all remain
valid.  Therefore a router theorem must transport the Boolean profile
`beta`, not merely cell shores or target multiplicities.

This is a local controller obstruction to an unlabelled transport argument;
it is not claimed to be a frozen `k=15` carrier counterexample.

## 8. The exact conditional routing theorem

For a weak protected state `X` and a specified excess-one circuit `C`, let

\[
                         \mathcal P_C(\mathfrak X)                \tag{8.1}
\]

be the **weak portal locus** of pointed states in the neutral weak-groupoid
orbit of `(X,C)`.  A point consists of a neutral path ending at `Y`, a
specified copy `C_Y` of the target circuit which is still an excess-one
component, and a splitter satisfying simultaneously:

1. the local saturation or augmenting-path inequality of Section 5;
2. an exterior matching of the required size;
3. a final shore of gap `h-1` when exact one-unit descent, rather than merely
   descent by at least one, is asserted;
4. deck and Johnson seam legality;
5. every declared residence and shadow condition;
6. the decorated common-`Q` conditions of Theorem 7.1, or an all-native
   replacement basis as in Corollary 7.3.

### Theorem 8.1 (decorated orbit-hitting descent)

Let `C` be any remaining unit-defect DM circuit of a protected state `X`.
If

\[
 \operatorname{Orb}_{\mathcal N_h^{\rm wk}}(\mathfrak X,C)
                   \cap\mathcal P_C(\mathfrak X)\ne\varnothing, \tag{8.2}
\]

then a neutral legal router followed by a protected splitter discharges
`C_Y`
and lowers Hall deficiency by at least one while preserving all declared
shadows, residence, and common-`Q` data.  If portal condition 3 is included,
the decrease is exactly one.  If (8.2) holds after every resulting descent,
the construction iterates.

#### Proof

Choose a neutral weak morphism to a portal state supplied by (8.2).  It preserves
deficiency and every protected invariant by definition.  Apply Theorem 5.1,
or equivalently Proposition 5.4, at the portal.  The splitter gains one
matching rank.  Portal condition 3 supplies the reverse Hall bound when an
exact one-unit decrease is claimed.  Theorem 7.1 or Corollary 7.3 gives the
common word for the protected pins.  The output is again a protected state,
so the argument may be repeated.  \(\square\)

### Corollary 8.2 (the minimal induction hypothesis)

For Hall descent it is unnecessary to route a splitter to **every** circuit.
It is enough that for every reachable weak protected state of positive deficiency,

\[
 \exists C\quad
 \operatorname{Orb}_{\mathcal N_h^{\rm wk}}(\mathfrak X,C)
                   \cap\mathcal P_C(\mathfrak X)\ne\varnothing, \tag{8.3}
\]

and that the splitter output stays in the inductive class.  The universal
quantifier over circuits is needed only for prescribed-circuit control or for
simultaneously avoiding additional quota obstructions.

### Corollary 8.3 (bounded router gives a bounded richer catalogue)

A signed interval permutation with `a` blocks composed with one with `b`
blocks has at most `a+b-1` blocks.  Hence a neutral word of `t` three-cut
braids has at most

\[
                         3t+1                                    \tag{8.4}
\]

signed blocks.  A strict conjugate of one three-cut splitter therefore has
at most

\[
                         6t+4                                    \tag{8.5}
\]

blocks, or `6t+3` seams.

At depth `d`, one seam can affect at most

\[
 h_d=\sum_{e=0}^{d-1}(e+3d)=\frac{7d^2-d}{2}                    \tag{8.6}
\]

compiler profiles on either side, using the exact dependency interval
`[s-2d,s+e+d]`.  Thus at `d=3` the boundary bank has at most

\[
                         30(6t+3)                                \tag{8.7}
\]

old and the same number of new profiles.  A bounded neutral route is
therefore an exact bounded richer catalogue.  Its Hall and common-`Q`
correctness still require Sections 5 and 7; collar size alone proves neither.

## 9. The sharp Hall-22 portal target

After discharging root `4877`, the unmatched native complement is exactly

\[
\begin{split}
 \{&449,960,1103,1920,2420,2575,2676,4213,5801,7504,8217,8218,\\
   &9524,13616,13620,17683,17738,18970,19568,21641,24610,29776\}.
                                                                    \tag{9.1}
\end{split}
\]

The five remaining `2/1` roots are

\[
                         2420,2676,9524,17683,19568.              \tag{9.2}
\]

They are the cleanest candidates for another copy of the remote splitter.
For a nested component (C=\{R,R^+\}) with (R\subset R^+), the following is a
checkable sufficient portal condition.  Produce two distinct unused cells
`c_-`,`c_+` satisfying

\[
\begin{array}{lll}
 E(c_-)=R,       &F(c_-)\subseteq R,&
       P_p\cap R\ne\varnothing\quad(p\in I_{c_-}),\\
 E(c_+)=R^+,     &F(c_+)\subseteq R^+,&
       P_p\cap R^+\ne\varnothing\quad(p\in I_{c_+}),
\end{array}                                                       \tag{9.3}
\]

and

\[
                         F(c_+)\not\subseteq R.                  \tag{9.4}
\]

Then `c_-` has restricted shore `{R}`, while `c_+` has restricted shore
`{R^+}`.  To obtain the cut-perfect current (5.5), require after common
cancellation that the old restricted bank is the one shared shore
`{R,R^+}` and the new bank is exactly these two singleton shores.  (For mere
saturation, retaining the old shared shore causes no difficulty.)  Since
`E(c_-)=R` and `E(c_+)=R^+`, both cells are native.  If the native exterior
basis survives or reroutes disjointly, Lemmas 5.3 and 7.2 give one more
literal unit of descent.

The exact next theorem is therefore:

> Starting at the frozen Hall-22 state (or its six-zero Pareto mate), prove
> that its protected neutral groupoid orbit meets one portal (9.3)--(9.4) for
> a root in (9.2), or a cut-perfect portal at another component, while
> preserving an exterior matching and the decorated Boolean common-`Q`
> current.

Routing to every component would be stronger.  No such transitivity theorem
is presently proved.

## 10. Precise proved/conditional boundary

The following statements are proved.

1. Safe Hall-neutral braids form a state-dependent groupoid.
2. Strict commuting-square transport preserves every DM cut current and all
   decorated physical invariants.
3. A single strict splitter orbit cannot cover the H22 components, because
   their incidence/rank types differ.
4. A neutral router and a remote cut-perfect splitter compose to an exact
   one-unit Hall descent under the exterior matching hypothesis.
5. The H23 neutral braid acts by the packet rotation (6.12) at root `24610`,
   while the second braid leaves that component unchanged and remotely splits
   `{4877,4909}`.
6. The pair preserves deck, Johnson legality, residence, all upper support,
   and the stated lower-support ledger.
7. Its native basis grows from `984` to `985` targets on the old DM shore, so
   it pays one exact partial common-`Q` unit.
8. Theorem 8.1 makes fully decorated orbit-hitting sufficient, and (8.3) is
   the minimal Hall-descent quantifier.

The following statements remain unproved.

1. Every remaining H22 circuit lies in a legal splitter orbit.
2. Even one further Hall-22 portal satisfying simultaneously the matching,
   residence, shadow, and common-`Q` conditions.
3. Preservation of an arbitrary exceptional/global pin assignment by the
   frozen H23-to-H22 pair.
4. A common compiler for a full `16361`-edge H22 matching.
5. Hall zero, the exact `k=15` word of length `6438`, or the general
   coefficient-one theorem.

## 11. Frozen exact artifacts

The claims in Section 6 and the native/common-`Q` claim in Section 7 are
independently reconstructible from

```text
scratch/k15_segment_braid_hall23.json
scratch/k15_segment_braid_hall23_portal.json
scratch/k15_segment_braid_hall22.json
scratch/audit_k15_h22_router_splitter_structure.py
scratch/k15_segment_braid_h22_router_splitter_audit_20260728.json
scratch/k15_hall23_native_dm_pins_certificate.json
scratch/k15_hall23_portal_native_dm_pins_certificate.json
scratch/k15_hall22_native_dm_pins_certificate.json
scratch/audit_k15_h22_router_splitter_common_q.py
scratch/k15_h22_router_splitter_common_q_certificate.json
```

No search result beyond these frozen certificates is used in the mathematical
implications above.
