# Component-neutral Catalan U-insertion ledger

Date: 2026-07-31  
Status: exact all-`r` counting and endpoint-type theorem; endpoint
compatibility, state-safe Hall, upper shadows, and compiler feasibility remain
separate gates

## 1. General four-sector setup

Let `r >= 2`, let `E` have size `2r-1`, and add two coordinates
`x,y`.  The rank-`r+1` layer on `E+x+y` splits into

\[
\begin{aligned}
 U&=\binom E{r+1},\\
 X&=\{T+x:T\in\tbinom Er\},\\
 Y&=\{T+y:T\in\tbinom Er\},\\
 A&=\{C+x+y:C\in\tbinom E{r-1}\}.
\end{aligned}                                                     \tag{1.1}
\]

Put

\[
 W_r=\binom{2r-1}{r},\qquad
 N_r=\binom{2r-1}{r+1},\qquad
 J_r=W_r-N_r.                                                     \tag{1.2}
\]

Then

\[
 \frac{N_r}{W_r}=\frac{r-1}{r+1},\qquad
 W_r=\frac12\binom{2r}{r},
\]

and therefore

\[
             J_r=\frac1{r+1}\binom{2r}{r}=\operatorname{Cat}_r.   \tag{1.3}
\]

The four owner decks have sizes `N_r,W_r,W_r,W_r`.  The lower-q1
target counts, grouped by their new-coordinate tags, are

\[
 00:W_r,\qquad x:W_r,\qquad y:W_r,\qquad xy:N_r.                  \tag{1.4}
\]

For K17, `r=8`, so

\[
 W_8=6435,\qquad N_8=5005,\qquad J_8=1430=\operatorname{Cat}_8.   \tag{1.5}
\]

## 2. Full component-neutral ledger

### Theorem 2.1 (Catalan component neutrality)

Assume:

1. `U` is partitioned into `c` nonempty Johnson paths;
2. each of `A,X,Y` is partitioned into `J_r` nonempty lower-rainbow
   paths, grouped into `J_r` legal `Y-A-X` macro paths; and
3. the resulting `c+J_r` path components are joined into one
   component-level path by `c+J_r-1` actual Johnson seams, and the complete
   path is lower-q1 rainbow.

Then the lower-q1 edge-slot counts are

\[
\begin{array}{c|c}
xy&W_r-J_r=N_r,\\
x&(W_r-J_r)+J_r=W_r,\\
y&(W_r-J_r)+J_r=W_r,\\
00&(N_r-c)+(c+J_r-1)=W_r-1.
\end{array}                                                       \tag{2.1}
\]

Every external component seam is then forced to have lower tag `00`.  In
particular, the component count `c` cancels exactly.  If the
colours within each tag family are pairwise distinct, the `xy,x,y`
families are complete and the unique lower-q1 hole lies in the untagged
`00` sector.  The total number of path edges is

\[
 N_r+3W_r-1=\binom{2r+1}{r+1}-1.                                 \tag{2.2}
\]

#### Proof

Each of the `J_r` path pieces in any one of `A,X,Y` has one
fewer internal edge than vertex, giving `W_r-J_r=N_r` internal
edges.  The `J_r` `Y-A` sockets add the missing `y`-tagged
edges, and the `J_r` `A-X` sockets add the missing
`x`-tagged edges.  This proves the first three rows of (2.1).

The first three rows already use every available lower colour with tag
`xy`, `x`, or `y`.  A further external seam of one of those tags would
repeat a colour, since the corresponding slot count equals the whole target
family.  Global lower rainbowness therefore forces every external seam to
have tag `00`.

The `c` U paths have `N_r-c` internal edges.  Joining the
`c+J_r` components into one path uses exactly `c+J_r-1`
external seams.  As just proved, all have tag `00`.  Their sum is
`N_r+J_r-1=W_r-1`, proving the last row.  Pascal's identity applied
to (1.1), or direct addition of the four rows, proves (2.2).  Pairwise
distinctness then turns the slot equalities into the stated palette
conclusion.  QED.

This is a two-coordinate odd-to-odd Pascal braid theorem
`2r-1 -> 2r+1`.  It is not, without another argument, a one-coordinate
odd-to-even lift theorem.

### Proposition 2.1A (Catalan macro count is forced in the native class)

Suppose instead that each of A, X, and Y is partitioned into the same `b`
nonempty paths and grouped into `b` legal Y-A-X macros, and that every
`xy`-tagged lower colour occurs exactly once, all on internal A--A edges.
Then

\[
                        W_r-b=N_r,
\]

and hence `b=J_r=Cat_r`.  With this value, the `X-X` interiors plus the
`A-X` sockets and the `Y-Y` interiors plus the `Y-A` sockets automatically
have `W_r` slots each.

This forcing is native-class-specific.  Off-native `xy` seams or a
repeated/missing `xy` palette can evade it.

### Corollary 2.2 (strict internal-insertion normal form)

Suppose every U path is inserted into a different one of the `J_r-1`
internal gaps of a linear Catalan macro order.  Necessarily

\[
             1\le c\le \min\{N_r,J_r-1\}.                        \tag{2.3}
\]

There are `2c` `Y-U-X` port seams and `J_r-1-c` remaining
direct `Y-X` seams, and hence

\[
 (N_r-c)+2c+(J_r-1-c)=W_r-1.                                    \tag{2.4}
\]

At K17 this is

\[
 (5005-c)+2c+(1429-c)=6434.                                     \tag{2.5}
\]

For `c=737`, the three terms are `4268,1474,692`.  The frozen
partial bridge audit presently lists 693 direct `Y-X` pairs because
it constructs a complete 6435-colour local cover before the global path is
opened.  Exactly one of those direct pairs must be omitted in the one-hole
linear carrier governed by (2.5).

The phrase "replace one direct seam" in this corollary is topological, not
label-preserving.  A direct seam `Y(T)-X(T)` has colour `T`.  If
one keeps both endpoint labels and inserts a U path between them, the two
new seams both have colour `T` and violate rainbowness.  The endpoint
labels must be globally re-paired or rerooted.

## 3. Exact endpoint types and the residual palette

Write `T,T'` for rank-`r` old projections and `V,V'` for
rank-`r+1` old projections.  The untagged external Johnson seams are
exactly

\[
\begin{array}{c|c|c}
\text{seam}&\text{Johnson criterion}&\text{lower colour}\\\hline
Y(T)-X(T')&T=T'&T,\\
Y(T)-U(V)&T\subset V&T,\\
X(T)-U(V)&T\subset V&T,\\
U(V)-U(V')&|V\cap V'|=r&V\cap V'.
\end{array}                                                       \tag{3.1}
\]

No `A-U` seam is Johnson, while `X-X` and `Y-Y` seams
have tag `x` and `y` rather than `00`.  Thus (3.1) is
complete.

In particular, a U component may terminate at either an X or a Y port at
either end.  It can therefore mediate a change of macro orientation while
retaining tag `00`; the old common-orientation conclusion for a contiguous
`U|YAX...` braid does not extend to this distributed architecture.

Consequently an oriented insertion

\[
       Y(T_L)-P(V^-,\ldots,V^+)-X(T_R)                           \tag{3.2}
\]

is Johnson exactly when \(T_L\subset V^-\) and
\(T_R\subset V^+\), or when these conditions hold after reversing
`P`.  It is lower-rainbow only when `T_L` and `T_R` are
different and both avoid every retained internal and previously selected
colour.

### Proposition 3.1 (one unit of palette slack)

Under the lower-rainbow/internal-colour-injective hypotheses of Theorem 2.1,
the internal U palette has size `N_r-c`.  Its complement in the
untagged colour layer has size

\[
                  W_r-(N_r-c)=J_r+c.                             \tag{3.3}
\]

A component-level path requires `J_r+c-1` external seams.  Therefore
every lower-rainbow completion uses all but exactly one residual colour,
independently of `c`.

This is the precise Hall target.  Component subdivision creates no palette
surplus.

### Proposition 3.2 (basis exchange under subdivision)

Suppose a lower-rainbow component path has residual hole `h`.  Cut one
retained internal U edge of colour `a`, increasing `c` by one,
and retain every old external seam.  Any lower-rainbow repair adds one seam
whose colour is either `a` or `h`.  In the first case the hole
stays `h`; in the second it moves to `a`.

More generally, if `s` cuts free the colour set
`A={a_1,...,a_s}` and every old external seam is retained, the
`s` new seam colours are an `s`-subset of `A union {h}`;
the unique unused member is the new hole.

#### Proof

Before the cuts, all residual colours except `h` are used.  The cuts
free exactly the colours in `A` and the seam quota rises by exactly
`s`.  With every old seam retained, the only collision-free available
colours are `A union {h}`.  Exactly `s` of its `s+1` members
must be used.  QED.

## 4. Endpoint run-state matching

For one coordinate, avoidance of `010` and `0110` has live DFA
states

\[
                    \{\epsilon,0,01,011\}.                       \tag{4.1}
\]

An oriented component is typed by the partial transformation it induces on
these four states in every one of the `2r+1` child coordinates, together
with its two endpoint masks and its internal lower palette.  If residence
of the new tags `x,y` has already been proved separately by the macro
grammar, their two maps may be omitted explicitly.  A candidate external seam or
`Y-U-X` insertion is admitted only when:

1. the appropriate row of (3.1) holds;
2. its colour is available;
3. its literal endpoint collars do not create `010` or `0110`;
   and
4. when a full-state conclusion is claimed, the composed DFA map is defined
   on the actual incoming state.

After two global terminal ports on distinct components are chosen, the
`q=J_r+c` components
have `2q-2` ports to pair and require `q-1` seams.  Pure port
degree-cover feasibility is therefore a Tutte perfect-matching problem; after orienting
the components it is an exit-entry Hall problem.  Deleting state-incompatible
edges gives the guarded Tutte/Hall problem.  Adding colour uniqueness gives
a coupled port-colour matching with exactly the one unit of slack in
Proposition 3.1.

### Theorem 4.1 (typed complete-block degree-cover Hall criterion)

Fix orientations and global terminals, and partition exits and entries by
their exact DFA endpoint types.  Suppose every allowed type block is
complete bipartite after the Johnson, colour-source, and run-state guards
are intersected.  Then a degree-correct guarded endpoint matching exists if

\[
  \sum_{alpha\in I}|L_alpha|
       \le \sum_{beta\in N(I)}|R_beta|
       \qquad\text{for every set of exit types }I.                \tag{4.2}
\]

#### Proof

The guarded graph is a complete blow-up of its type quotient.  Any partial
subset of one exit type has the same type-neighbourhood as the whole type,
so the worst Hall sets are unions of complete exit types.  Equation (4.2)
is therefore ordinary Hall for the blow-up.  QED.

Completeness of the type blocks is a substantive hypothesis.  Johnson
containment and the one-unit colour pressure usually make PBBS type blocks
sparse.

### Theorem 4.2 (reroot bridge repair)

Let `B_0=(L,R;E_0)` be the actually retained guarded exit-entry graph,
and let `E_+` be guarded edges created by rerooting.  Put

\[
                   \delta(S)=(|S|-|N_{B_0}(S)|)_+.
\]

If, for every \(S\subseteq L\), the graph

\[
             E_+[S,R\setminus N_{B_0}(S)]
\]

has a matching of size at least \(\delta(S)\), then
`B_0+E_+` has a perfect exit-entry matching.

#### Proof

The matching gives \(\delta(S)\) distinct new neighbours outside the old
neighbourhood, so the augmented neighbourhood has size at least `|S|`.
Hall applies.  QED.

If a reroot deletes old edges, `B_0` must be the graph actually
retained after that reroot.  Increasing `c` by subdivision alone does
not help: Propositions 3.1--3.2 show that it leaves palette slack one.  A
useful reroot must create guarded adjacency, or deliberately transport the
unique hole through a basis exchange.

## 5. Frozen K17 scope and remaining gate

The current partial local bridge certificate is

```text
scratch/k17_pbbs_u_yux_bridge_matching_20260731.audit.json
SHA-256 ce666738203f9c5c45a180314507c0c85dcf504d1194caf90cb481412611dc74
```

with matching table SHA-256
`e602f2f3abc91909bec42bdde02422001d9c78f354207c7fd69b0288d99c4148`.
It constructs 737 locally `010/0110`-safe `Y-U-X` bridges and a
complete 6435-colour local cover.  Its own scope correctly says that it
uses no A vertices and does not solve the global A/X/Y chronology or
boundary residence.  In the strict internal-insertion normal form with the
unique hole required in the untagged sector, the final open carrier omits
one direct `Y-X` pair as in (2.5).  A more general completion can retain all
6435 frozen untagged edges and place the unique global hole in a tagged
sector.

Likewise, the frozen `0bcd...` U forest has a replayed pair-local
736-seam degree cover.  Therefore no static pair-clean UNSAT claim is valid
for that atlas.  The verified standalone failures involve additional colour
or full-DFA/global-path constraints; they must not be relabelled as ordinary
Hall failure.

Within the native component path of Theorem 2.1, the exact remaining
existence statement is:

> Choose the `J_r+c-1` occurrence-labelled external seams, their
> component orientations, and the unique omitted untagged colour so that
> the guarded endpoint graph has a saturating matching, all seam colours
> are distinct, the selected degree cover is connected (or has a certified
> component-fusing sequence), the one physical chronology passes the full
> DFA product, and the protected upper/compiler ledgers survive.

The Catalan identity removes component count from this statement.  It does
not remove endpoint type, colour correlation, or chronology.

## 6. Balanced A attachment and the exact residual degree ledger

The A-count caveat in Section 5 has now been repaired literally.  Attach one
distinct state `A_C=C+x+y` to an outer endpoint of each of the 1430 local
`YUX/YX` components.  A deterministic SDR finds 715 left attachments and
715 right attachments, each Johnson and locally `010/0110`-safe.  The frozen
atlas is

```text
scratch/k17_pbbs_u_yaux_balanced_bridge_20260731.fragments
SHA-256 23d889267915e45401cf72ca62aa5a789eb84213f6f132ea8352a05efc2e8d47
```

and its audit is

```text
scratch/k17_pbbs_u_yaux_balanced_bridge_20260731.audit.json
SHA-256 1a54589de7cd1964abef7ae1d62f5b5724d5a117e1933c27ca16f3e93ead2047
payload 0a4aaf0d1da45b561edd0c5ab27e52b4d90595a4983aa672c5f9c5b7366f9662
```

Exact replay gives 1430 path components, 9295 distinct rank-nine vertices,
7865 distinct internal lower-q1 colours, signature histogram

\[
 00:6435,\qquad x:715,\qquad y:715,\qquad xy:0,
\]

and no internal `010` or `0110`.  It uses all 5005 U states and exactly 1430
states from each of A, X, and Y.  Hence the unused vertex sets have the
balanced sizes

\[
 |A_{rem}|=|X_{rem}|=|Y_{rem}|=5005.
\]

The remaining exposed-port and colour totals force the following exact
decomposition for a **closed degree-two, all-lower-rainbow factor**:

* 5005 A--A seams carry the 5005 missing `xy` colours;
* 5005 X--X seams and 715 A--X seams carry the 5720 missing `x` colours;
* 5005 Y--Y seams and 715 A--Y seams carry the 5720 missing `y` colours.

These five rows total 16445 added edges.  They complete the 7865-edge
forest to a 24310-edge 2-factor.  A spanning open path which retains this
fixed forest instead adds only 16444 edges and omits exactly one of these
residual tagged colours.  Thus the degree equations below are the closed
factor ledger; opening or rethreading is a further step.

Indeed the A-side external degree demand is

\[
 1430+2\cdot5005=11440
   =2\cdot5005+715+715,
\]

while the X- and Y-side demands are each

\[
 715+2\cdot5005=10725
   =2\cdot5005+715.
\]

Thus the next finite theorem is a three-type port matching: an A--A
cap-two factor carrying every `xy` colour, coupled to lower-rainbow
X--X/A--X and Y--Y/A--Y factors.  This degree ledger is exact, but it does
not by itself prove the joint matching, connectivity, global DFA condition,
upper shadows, staircase, or compiler.

### Updated exact residual factor

The first `23d8...` attachment remains only a scoped partial braid; no
uncited flow value is promoted here.  A later changed attachment does pass
the complete coupled residual flow and is frozen at

```text
scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.audit.json
SHA-256 f9daf5e8ac7cb47d4b148789fcddcbd0d1a53030f6a9e0d173a892ed78063350
payload 520c709b458a772e9bb1e7727b558b72a3d1b1c8fafb0b95672dfc5d5dec9323
```

It is an exact 24310-edge all-lower-rainbow 2-factor on all 24310 owners,
with 989 components.  Its residual flows are

\[
 AA=5005,\quad XX=5005,\quad YY=5005,\quad AX=715,\quad AY=715.
\]

The AA flow is recorded as 10010 A-side incidences, equivalently 5005
undirected AA edges.

This closes the lower degree/palette factor only.  Its audit has 9103 upper
holes and many cyclic runs of lengths two and three; connectivity, opening
to a 24309-edge path, upper completion, residence, and the compiler remain
separate.
