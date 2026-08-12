# Hinge hexagons, the owner-attachment trade lattice, and its exact homology obstruction

## Status

This note proves an explicit bounded owner-attachment exchange which
preserves one-copy owners, all declared named lower targets, and exact state
balance.  The two-owner version is a hinge rectangle `C4`; the first
genuinely three-role version is a `C6`.

It also computes the exact lattice invariant of any chosen bounded trade
atlas.  The quotient is the first integral homology of the owner--head
compatibility graph after filling the physically available trade cycles.
Thus bounded cokernel does not follow from local trade existence alone.  It
does follow if every chordless compatibility cycle is an authenticated
completed `C4` or `C6`.

The theorem is purely at the mixed-rotor owner/declared-payload/state row.
It does not prove that the corrected pull-clock packages admit the required
common hinge completion, nor does it silently preserve an upper/residence
guard not included in the completed rectangle.

## 1. Completed hinge roles

Let `I` be a set of occurrence roles.  Role `i` has:

* a fixed owner resource packet `T_i` (one owner or a fixed ordered tuple
  of owner windows);
* a fixed declared named-target payload `C_i`;
* a fixed chosen tail state `a_i`; and
* a set `H_i` of admissible head states.

For every `h in H_i`, write

\[
                             K_i(a_i,h)                       \tag{1.1}
\]

for a literal trace packet.  Assume that, as `h` varies, every packet in
(1.1) has the same owner, named payload, tail, and every other guard which
has been declared part of the completed interface.  The hinge rectangle
theorems supply exactly this situation after the relevant guard rows have
been proved left/right separable.

Make the bipartite compatibility graph

\[
                  G=(I,V;E),\qquad ih\in E\iff h\in H_i,       \tag{1.2}
\]

where repeated physical head states are represented by capacity clones if
necessary.  An integral balanced selection is a matching which uses every
role once and every required head clone once.  Its literal trace is
obtained by replacing an edge `ih` by (1.1).

## 2. Every alternating compatibility cycle is a literal trade

### Theorem 2.1 (completed-hinge cycle exchange)

Suppose the compatibility graph contains the simple alternating cycle

\[
 i_0h_0i_1h_1\cdots i_{s-1}h_{s-1}i_0.                      \tag{2.1}
\]

Assume the current selection uses `i_j h_j` for every `j`, while the other
cycle edge at `i_j` is `i_j h_(j-1)` (indices modulo `s`).  Then

\[
 \{K_{i_j}(a_{i_j},h_j):j\in\mathbb Z_s\}
 \longleftrightarrow
 \{K_{i_j}(a_{i_j},h_{j-1}):j\in\mathbb Z_s\}                \tag{2.2}
\]

is an exact `s`-against-`s` literal trade.  It preserves:

1. every owner, once rolewise;
2. every declared named target, once rolewise;
3. the complete tail-state multiset;
4. the complete head-state multiset, and hence exact state boundary; and
5. every guard included in the completed hinge interface.

It changes the head--owner attachment by the cyclic permutation
`h_j -> h_(j-1)`.

#### Proof

The role set is unchanged, so the fixed owner and payload of every role are
unchanged.  The tail `a_i` of every role is unchanged.  The new heads are a
permutation of the old heads.  Hence both sides of (2.2) have identical
tail and head counters.  Every replacement edge belongs to `G`, so (1.1)
is a literal accepted packet with the same completed interface.  `square`

### Corollary 2.2 (the bounded `C4` and `C6` moves)

For `s=2`, (2.2) is the usual two-owner crossed-head rectangle switch.  For
`s=3`, it is the explicit hexagonal exchange

\[
 \begin{aligned}
 &(i_0,h_0)+(i_1,h_1)+(i_2,h_2)\\
 &\hspace{2cm}\longleftrightarrow
 (i_0,h_2)+(i_1,h_0)+(i_2,h_1).                       \tag{2.3}
 \end{aligned}
\]

Thus an authenticated three-role completed hinge gives a bounded `C6`
which changes owner attachment while preserving all named rank marginals
and exact state balance.

When the three old arcs lie in three distinct Euler components, (2.3)
also fuses those components into one.  Component fusion is additional to,
not needed for, the resource identity above.

## 3. The exact attachment lattice

Orient every edge of `G` from `I` to `V`, and let

\[
             \partial:\mathbb Z^{E(G)}\longrightarrow
                       \mathbb Z^{I\sqcup V}                    \tag{3.1}
\]

be the signed vertex boundary.  Put

\[
                         Z_1(G):=\ker\partial.                  \tag{3.2}
\]

The difference of two selections with the same role and head demands lies
in `Z_1(G)`.

For an even cycle `C`, let `z_C` be its alternating signed edge vector.

### Lemma 3.1 (integral cycle lattice)

The group `Z_1(G)` is generated over the integers by the vectors `z_C` of
simple even cycles of `G`.

#### Proof

Reverse every edge on which a nonzero circulation has negative coefficient.
At each vertex the resulting nonnegative directed multigraph has equal
indegree and outdegree.  Follow unused directed edges until a directed
cycle closes, subtract its minimum edge multiplicity, and iterate.  Since
`G` is bipartite, every resulting cycle is even.  Splitting a repeated
vertex decomposes a closed walk into simple cycles.  Restoring the original
orientations gives the asserted signed decomposition.  `square`

Let `A` be any family of physically authenticated completed-hinge cycles,
for example the available `C4` and `C6` moves.  Define their trade lattice

\[
                         L_{\cal A}:=
             \langle z_C:C\in\mathcal A\rangle_{\mathbb Z}.  \tag{3.3}
\]

### Theorem 3.2 (attachment homology theorem)

Attach one oriented two-cell to `G` along every cycle in `A`, and call the
resulting two-complex `X_A`.  Then the exact cokernel of the authenticated
attachment trades is

\[
 \boxed{
 {Z_1(G)\over L_{\cal A}}
       \cong H_1(X_{\cal A};\mathbb Z).}                       \tag{3.4}
\]

In particular, the homology class of the difference of two balanced
attachments is invariant under every allowed bounded trade.  Vanishing of
that class is necessary and sufficient for the difference to be an
integer linear combination of the authenticated circuits.

#### Proof

The cellular chain complex of `X_A` in dimensions two through zero is

\[
 \mathbb Z^{\cal A}\xrightarrow{\partial_2}
 \mathbb Z^{E(G)}\xrightarrow{\partial}
 \mathbb Z^{I\sqcup V},                                      \tag{3.5}
\]

where `partial_2` sends the cell indexed by `C` to `z_C`.  Therefore

\[
 H_1(X_A;\mathbb Z)=\ker\partial/\operatorname{im}\partial_2
                   =Z_1(G)/L_A.                              \tag{3.6}
\]

This is (3.4).  `square`

The last assertion is a **lattice** statement.  A signed decomposition can
pass through negative coefficients.  Actual reconfiguration of matchings
requires a conformal sequence of cycle flips, equivalently a Markov-basis
property.  The next theorem gives a clean sufficient condition.

## 4. When `C4/C6` trades are complete

Call a cycle induced if the subgraph on its vertices contains no chord.

### Theorem 4.1 (short-chordless completion)

Assume every induced cycle of `G` has length four or six, and every such
cycle belongs to the authenticated completed-hinge atlas `A`.  Then

\[
                         L_A=Z_1(G),qquad
                         H_1(X_A;\mathbb Z)=0.                  \tag{4.1}
\]

Moreover any two perfect matchings of `G` are joined by a sequence of
literal completed-hinge `C4/C6` exchanges.

#### Proof

An even cycle with a chord is the signed sum of the two strictly shorter
even cycles cut off by that chord.  Induction on cycle length expresses
every cycle vector as an integer sum of induced cycle vectors.  Lemma 3.1
then proves the first equality, and Theorem 3.2 proves the second.

For the nonnegative statement, take two perfect matchings `M,N`.  Their
symmetric difference is a disjoint union of alternating even cycles.  If
one such cycle is induced, flip it.  Otherwise choose a chord.  Of the two
subcycles cut off by the chord, first flip the one whose alternating side
uses old matching edges on its path and introduces the chord; then flip the
other, which removes the chord and completes the original cycle flip.
Inducting on length replaces the original alternating cycle by authenticated
induced `C4/C6` flips without leaving the perfect-matching fibre.  Process
the symmetric-difference cycles one at a time.  `square`

The chordal-bipartite special case needs only the `C4` rectangles.  The
first new case beyond it is an induced `C6`, exactly the three-role exchange
(2.3).

## 5. Why bounded cokernel is not automatic

### Proposition 5.1 (unbounded free obstruction)

For every `t` there is a connected bipartite compatibility graph `G_t`
whose `C4/C6` trade atlas is empty and for which

\[
             {Z_1(G_t)\over L_{4,6}}cong\mathbb Z^t.          \tag{5.1}
\]

#### Proof

Take `t` disjoint chordless eight-cycles and join them by bridges in a
tree.  Bridges lie on no cycle, and the graph contains no four- or
six-cycle.  Its integral cycle lattice is the direct sum of the `t`
eight-cycle lattices, hence is `Z^t`, while `L_(4,6)=0`.  `square`

Thus neither the existence of many local rectangles nor the existence of
some hexagons proves a bounded trade cokernel.  The exact missing global
statement is one of:

* prove that the mixed-rotor compatibility complex has uniformly bounded
  `H_1` after its physical `C4/C6` cells are filled;
* prove the stronger short-chordless condition of Theorem 4.1; or
* add authenticated longer circuits whose two-cell boundaries kill the
  remaining homology classes.

## 6. Relation to the cubic flag and pentagon mechanisms

The all-depth cubic flag trade is a three-against-three equality of named
chain rows, but a single cube is not automatically a cell of `X_A`: at
depth at least four it has nonzero ordered rail boundary, and even at depth
three it changes the refined bottom-core boundary.  Only an opposed/aligned
packet whose complete state boundary cancels, together with the required
companion head rectangles, becomes the literal `C6` of (2.3).  Counting a
prospective cube before these rows close would incorrectly enlarge
`L_A`.

A clean turn-hypergraph `C5` is different.  It is an odd-cycle parity
obstruction in the three-resource matching support, not a circulation in
the bipartite owner--head attachment graph.  A one-row portal can absorb
it, but the portal plus its companion atoms must first be completed to a
resource-zero replacement before it contributes a relation to any trade
lattice.  Consequently the `C5` portal row and the attachment homology row
are complementary rather than interchangeable.

## 7. Consequence for the mixed rotor programme

The corrected pull clock proves the required stationary fractional rank
and trace marginals.  Its one-copy owner rounding can use the theorem above
only after the mixed-length roles have been embedded into one exact
owner/target table with completed hinge menus.  On that face:

1. (2.3) is the desired bounded owner-changing, named-target-neutral,
   state-neutral exchange;
2. (3.4) is the exact invariant of all such bounded exchanges; and
3. Theorem 4.1 is a concrete sufficient support theorem for complete
   integral reconfiguration.

The next proof target is therefore not a generic assertion that short
circuits generate.  It is the Boolean-specific statement that the completed
mixed-rotor owner--head compatibility graph has no unfilled homology beyond
`O(1)`, preferably that every induced cycle is an authenticated `C4` or
`C6`.

## 8. Exact collapse for the actual opposed-hinge subcube menus

The shielded opposed-hinge construction has a special form which permits a
sharper invariant than arbitrary graph homology.  Fix one internal head
spine `sigma`.  Every role in this spine fibre has a mandatory endpoint
label `b_i`, an optional label set `U_i` disjoint from `b_i`, and the
unfiltered head menu

\[
 \mathcal H_i=\{(\sigma,\{b_i\}\cup A):A\subseteq U_i\}.     \tag{8.1}
\]

For the literal opposed hinge, `U_i=D_{d,i}-{z_i}` and `A=emptyset` is
allowed because the actual final source letter is `{b_i} union A`, hence is
still nonempty.

For the exact collapse below assume the mandatory labels `b_i` are
pairwise distinct inside the fibre.  Equal-label roles share the same
canonical singleton head and require a separate physical-capacity
coalescing argument; they are not silently treated as distinct head
clones here.

Define the mutual endpoint compatibility graph `Gamma` on the roles by

\[
 ij\in E(\Gamma)
 \quad\Longleftrightarrow\quad
 \begin{cases}
 b_i=b_j,\quad\text{or}\\
 b_j\in U_i\ \text{and}\ b_i\in U_j.
 \end{cases}                                                 \tag{8.2}
\]

For an edge `ij`, put

\[
 h_{ij}:=(\sigma,\{b_i,b_j\}),                               \tag{8.3}
\]


### Lemma 8.1 (canonical pair-head property)

Two roles `i,j` have a common head if and only if `ij` is an edge of
`Gamma`.  Whenever `h` is any common head, the canonical pair head `h_ij`
is also common to both roles.  Hence

\[
                    i-h-j-h_{ij}-i                             \tag{8.4}
\]

is a literal completed-hinge `C4`.

#### Proof

If `h=(sigma,L)` belongs to both menus, then `b_i,b_j in L`,
`L-{b_i} subseteq U_i`, and `L-{b_j} subseteq U_j`.  For unequal mandatory
labels this gives `b_j in U_i` and `b_i in U_j`; equality is automatic.
Conversely those inclusions make `{b_i,b_j}` an allowed last letter in both
menus.  The same calculation proves the last assertion, and Theorem 2.1
turns the four compatibility edges into the literal trade (8.4).  `square`

Let `Cl(Gamma)` be the clique complex of `Gamma`.  Only its two-skeleton is
relevant to first homology.

### Theorem 8.2 (subcube attachment homology collapse)

In one unfiltered fixed-spine opposed-hinge fibre, authenticate:

1. every square (8.4); and
2. for every triangle `ijk` of `Gamma`, the canonical hinge hexagon

\[
       i-h_{ij}-j-h_{jk}-k-h_{ki}-i.                          \tag{8.5}
\]

Let `L^(can)_(4,6)` be the lattice generated by precisely the canonical
squares (8.4) and canonical triangle hexagons (8.5).  Then

\[
 \boxed{
 {Z_1(G)\over L^{\rm can}_{4,6}}
       \cong H_1(\operatorname{Cl}(\Gamma);\mathbb Z).}        \tag{8.6}
\]

#### Proof

Consider a closed walk in the bipartite compatibility graph.  Every
length-two segment `i-h-j` has `i,j in N(h)`.  By Lemma 8.1, the square
(8.4) replaces this segment, modulo an authenticated `C4` boundary, by

\[
                              i-h_{ij}-j.                       \tag{8.7}
\]

Doing this around the walk makes it a subdivided closed walk in `Gamma`.
Thus the squares eliminate every extra head vertex and identify the
remaining one-dimensional cycle presentation with the subdivision of
`Gamma`.

Under that identification, the boundary of (8.5) is precisely the
subdivision of the triangle `ijk`.  Hence quotienting further by all
authenticated canonical hexagons imposes exactly the triangle-boundary
relations in the clique complex.  The cycle group of a graph modulo its
triangle boundaries is `H_1` of its clique complex.  This proves (8.6).
`square`

This is an exact computation, not only a surjection: the square relations
give inverse representatives by (8.7), and the only additional declared
relations are the canonical triangle hexagons.

### Corollary 8.3 (chordal and one-portal closure)

The attachment trade lattice is complete in any fixed-spine fibre if
either:

1. `Gamma` is chordal; or
2. `Gamma` has a universal vertex.

In both cases

\[
                  H_1(\operatorname{Cl}(\Gamma);\mathbb Z)=0. \tag{8.8}
\]

The universal vertex is a literal **endpoint portal**: every long owner
attachment cycle is a sum of canonical `C6`s through that one role.

#### Proof

In a chordal graph, repeatedly splitting a cycle along a chord expresses
it as a sum of triangles.  Those triangles bound two-cells in the clique
complex.  A universal vertex gives the same decomposition directly by
coning every edge of a cycle to that vertex.  Apply Theorem 8.2.  `square`

### Scope of the collapse

Arbitrary completed guard filtering can remove `h_ij` even while retaining
some larger common head `h`.  Then Lemma 8.1 is no longer true in the
filtered menu, and (8.6) cannot be invoked.  A protected use therefore
needs the following explicit **minimal-head retention** row:

\[
 h\in\mathcal H_i\cap\mathcal H_j
 \quad\Longrightarrow\quad
 h_{ij}\in\mathcal H_i\cap\mathcal H_j.                    \tag{8.9}
\]

The unfiltered literal opposed-hinge rectangles satisfy (8.9)
automatically.  For guarded mixed-rotor roles, proving (8.9), chordality of
`Gamma`, or one endpoint-portal role per spine fibre is now a concrete
Boolean sufficient theorem for zero attachment homology.

## 9. An explicit physical clique bank

The chordal condition is not merely formal.  A linear-size bank of literal
opposed hinges can be planted so that its endpoint graph is complete.

### Theorem 9.1 (opposed-hinge attachment clique)

Let the Boolean ground set have size `2r-1`.  Let `d>=2`, and let

\[
             h\le \min\{r-d,\lfloor r/2\rfloor\}.              \tag{9.1}
\]

There are `h` literal two-owner opposed-hinge macros with the following
properties.

1. Their `2h` rank-`r` owner windows are all distinct.
2. Their `h` transition roots are all distinct.
3. They share one internal head spine and have pairwise distinct mandatory
   head labels `b_0,...,b_(h-1)`.
4. Their mutual endpoint graph `Gamma` is the complete graph `K_h`.
5. If only the right-hand fixed chains are declared as named payload, those
   `h` chains are pairwise disjoint as occurrence labels and distinct at
   every rank.

Consequently the canonical `C4/C6` attachment complex of this bank has
zero first homology.  Every balanced owner-attachment difference on the
bank is an integer sum of literal named-payload- and state-neutral
hexagons (with squares for nonminimal common heads).

#### Proof

Put `ell=r-d`.  Choose pairwise disjoint label banks

\[
 \begin{aligned}
  &M, &&|M|=d-1,\\
  &P, &&|P|=\ell-h,\\
  &B=\{b_0,\ldots,b_{h-1}\},\\
  &Z=\{z_0,\ldots,z_{h-1}\},\\
  &A=\{a_0,\ldots,a_{h-1}\}.
 \end{aligned}                                               \tag{9.2}
\]

Their total size is

\[
          (d-1)+(r-d-h)+3h=r-1+2h\le2r-1,                    \tag{9.3}
\]

so the choice is possible.  Order `M` as singleton layers

\[
                       D_1,\ldots,D_{d-1}.                     \tag{9.4}
\]

For every `i`, define

\[
 \begin{aligned}
 D_{d,i}&=P\cup(B-\{b_i\})\cup\{z_i\},\\
 R_i&=M\cup D_{d,i},\\
 T_i^-&=R_i\cup\{a_i\},\\
 T_i^+&=R_i\cup\{b_i\}.                                     \tag{9.5}
 \end{aligned}
\]

Now `|D_(d,i)|=ell`, so `|R_i|=r-1` and both owners have rank `r`.
The label `b_i` is absent from `R_i`, whereas `z_i` is present.  Hence the
roots `R_i` are distinct.  The plus owners are distinguished by `z_i`, and
every minus owner contains its private `a_i`; no plus owner contains an
`A`-label and no other minus owner contains `a_i`.  Thus all `2h` owners
are distinct.

Use the opposed-hinge word

\[
 X_i(A')=
 (\{a_i\},D_{d,i},D_{d-1},\ldots,D_1,
                       \{b_i\}\cup A'),
 \qquad A'\subseteq D_{d,i}-\{z_i\}.                          \tag{9.6}
\]

This is Theorem 2.1 of the shielded opposed-hinge construction with the
left optional set fixed empty.  Its two owners are exactly (9.5), its
internal head spine is the common ordered word
`(D_(d-1),...,D_1)`, and its optional head set is

\[
 U_i=D_{d,i}-\{z_i\}=P\cup(B-\{b_i\}).                        \tag{9.7}
\]

For `i != j`, (9.7) contains `b_j`; symmetrically `U_j` contains `b_i`.
Therefore every pair `ij` is an edge of `Gamma`, and its canonical common
head is the literal state with last letter `{b_i,b_j}`.  This proves
`Gamma=K_h`.

The fixed right-hand chain of role `i` has rows

\[
 D_{d,i},\quad D_{d,i}\cup D_{d-1},\quad\ldots,\quad
 D_{d,i}\cup D_{d-1}\cup\cdots\cup D_1.                     \tag{9.8}
\]

Every row retains the role-private set `D_(d,i)`, and the `D_(d,i)` are
distinct, so equal-rank rows belonging to different roles are distinct.
Declare these chains as the named payload; the common left-hand chain may
remain unmarked.  Endpoint variation does not change (9.8).

Finally `K_h` is chordal (indeed its clique complex is a simplex), so
Theorem 8.2 and Corollary 8.3 give zero attachment homology and the stated
`C4/C6` generation.  `square`

### Corollary 9.2 (fixed-size protected portal bank)

For every fixed `h`, the clique bank exists for all sufficiently large
central ranks because `d=Theta(sqrt(r))` and hence (9.1) eventually holds.
It uses exactly `2h` owner windows and carries `h` pairwise distinct marked
chains.  Thus a bounded family of mixed-rotor owner-attachment tasks can be
placed in one literal zero-homology endpoint portal bank before global
rounding.

This corollary does not embed the bank into a complete one-copy owner table
or prove that the exterior chronology routes through it.  Its gain is the
previously missing local actuator: within the planted bank, every
attachment lattice class is killed by explicit bounded literal trades,
with no named-target or state-boundary debt.

### Corollary 9.3 (unconditional owner/q1 planting)

If, in addition,

\[
                              2h\le r-2,                       \tag{9.9}
\]

then the complete clique bank is contained in a spanning two-factor of the
middle-levels incidence graph between ranks `r-1` and `r` on `[2r-1]`.
Its `h` immediate-upper colours

\[
                         R_i\cup\{a_i,b_i\}                    \tag{9.10}
\]

are pairwise distinct.

#### Proof

The protected incidence bank is the disjoint union of the paths

\[
                         T_i^- - R_i - T_i^+,qquad 0\le i<h. \tag{9.11}
\]

All roots and owners in these paths are distinct by Theorem 9.1.  Hence the
bank has maximum degree two and exactly `2h` edges.  The small protected
middle-levels factor theorem says that every maximum-degree-two protected
subgraph with at most `r-2` edges extends to a spanning two-factor.  Apply
it using (9.9).

Finally (9.10) contains the private label `a_i`, which belongs to no other
root or owner packet in the bank.  Thus the displayed upper colours are
distinct.  `square`

For every fixed `h`, (9.9) also holds eventually.  Therefore the bounded
zero-homology attachment portal is not merely an isolated word gadget: it
is unconditionally plantable in an exact owner/immediate-lower spanning
factor.  This still does not make the completing two-factor upper-exact or
connected, and it does not extend the marked chains to the full residual
target bank.

## 10. An exponential one-spine clique

Private coordinate labels are not needed role by role.  Reusing one
mandatory endpoint and varying a large set core gives exponentially many
one-copy roles in one zero-homology clique.

### Theorem 10.1 (exponential common-endpoint hinge bank)

Let `d>=2`, put

\[
                         \ell=r-d,qquad
                         n_0=2r-d-2,                           \tag{10.1}
\]

and work on `[2r-1]`.  Choose disjoint:

* an ordered internal spine `M` of `d-1` singleton layers;
* two labels `a,b` outside `M`; and
* the remaining pool `S`, of size `n_0`.

For every `D in binom(S,ell)`, define

\[
 R_D=M\cup D,qquad
 T_D^-=R_D\cup\{a\},qquad
 T_D^+=R_D\cup\{b\}.                                      \tag{10.2}
\]

Then the `N=binom(n_0,ell)` opposed-hinge roles indexed by `D` have:

1. `2N` pairwise distinct rank-`r` owners and `N` distinct transition
   roots;
2. pairwise distinct fixed right-hand named chains;
3. one common literal head state

   \[
                         h_*=(\sigma,\{b\}),                    \tag{10.3}
   \]

   where `sigma` is the common internal spine;
4. complete mutual endpoint graph `K_N`; and
5. zero attachment homology using only literal `C4` fan trades through
   `h_*`.

Moreover, if

\[
                              r\ge4d,                           \tag{10.4}
\]

the roles admit pairwise distinct literal head choices from their own
menus.

#### Proof

For each `D`, temporarily allow the shield label `z_D` to be chosen later
inside `D`, and use the word

\[
 (\{a\},D,D_{d-1},\ldots,D_1,\{b\}\cup A_D),
 \qquad A_D\subseteq D-\{z_D\}.                              \tag{10.5}
\]

The two owner windows and transition root are exactly (10.2).  Different
`D` give different roots and different plus and minus owners.  A minus
owner contains `a` and not `b`, while a plus owner contains `b` and not
`a`, so no cross-polarity collision is possible.

The fixed right-hand chain is

\[
 D,\quad D\cup D_{d-1},\quad\ldots,\quad
 D\cup D_{d-1}\cup\cdots\cup D_1.                           \tag{10.6}
\]

At every fixed rank equality of two such rows would imply equality of
their parts outside `M`, hence equality of the indexing sets `D`.  Thus the
declared chains are pairwise distinct.

Taking `A_D=emptyset` in (10.5) shows that every role admits the common
head (10.3).  Therefore every two roles are mutually compatible.  More
strongly, if a compatibility cycle contains a segment `i-h-j`, then

\[
                              i-h-j-h_*-i                       \tag{10.7}
\]

is a literal completed-hinge square.  Replacing every segment of a cycle
by its route through `h_*` expresses the cycle as a sum of these squares.
Hence the entire attachment cycle lattice is generated by the `C4` fans
and its quotient is zero.

It remains to prove the distinct-head assertion.  Before choosing `z_D`,
role `D` can realize **every proper subset** `A subsetneq D`: after choosing
such an `A`, take any `z_D in D-A`.  Thus it is enough to match all
`ell`-sets `D` injectively into the lower ideal

\[
                  \{A\subset S:|A|<\ell\},qquad A\subset D.   \tag{10.8}
\]

For a family `F subseteq binom(S,ell)`, let `partial_j F` be its rank-`j`
lower shadow.  Double-counting containments gives

\[
 |\partial_jF|
 \ge |F|{\binom\ell j\over\binom{n_0-j}{\ell-j}}
 =|F|{\binom{n_0}j\over\binom{n_0}\ell}.                    \tag{10.9}
\]

The shadows at different ranks are disjoint.  Under (10.4), already the
two top lower ranks satisfy

\[
 {\binom{n_0}{\ell-1}+\binom{n_0}{\ell-2}
       \over\binom{n_0}\ell}
 ={r-d\over r-1}
  +{(r-d)(r-d-1)\over r(r-1)}
 \ge1.                                                       \tag{10.10}
\]

Indeed the difference after multiplication by `r(r-1)` is
`r^2-3rd+d^2+d`, which is positive for `r>=4d`.  Summing (10.9) over
`j<ell` therefore proves Hall's inequality for (10.8).  Choose an SDR
`D -> A_D`, then choose `z_D in D-A_D`.  The resulting last letters
`{b} union A_D` and hence the complete head states are pairwise distinct.
`square`

### Corollary 10.2 (scale and reuse ledger)

For triangular depth `d=Theta(sqrt(r))`,

\[
 N=\binom{2r-d-2}{r-d}
   =2^{\,2r-\Theta(\sqrt r)}
   =W\,2^{-d+O(1)},                                         \tag{10.11}
\]

where `W=binom(2r-1,r)`.  The entire exponential bank reuses:

* one `(d-1)`-letter spine;
* one incoming endpoint `a`;
* one outgoing endpoint `b`; and
* one universal head portal `h_*`.

Role identity, owner uniqueness, and named-chain uniqueness are carried by
the varying `ell`-set `D`, not by private coordinate labels.  Thus the
finite ground set does **not** limit a chordal attachment bank to `O(r)`
roles.

The result is stronger than an overlapping bounded-clique tree: its mutual
endpoint graph is one complete graph on exponentially many one-copy roles,
so every ordering is a perfect elimination ordering.  What remains global
is to place enough such banks so that their tail-state multisets match the
head-state multisets and together use the full prescribed mixed-length
target inventory.  Theorem 10.1 closes attachment homology and head
distinctness inside one bank; it does not prove that final de Bruijn
balance or a partition of all owners into these banks.

## 11. Owner-wide cover by subexponentially many portal banks

The exponential bank need not be guessed in advance.  Any Middle Levels
owner cycle canonically partitions almost the entire owner shore into such
banks.

### Theorem 11.1 (near-complete owner portal-bank cover)

Let `d>=2`.  On the rank-`r` owner shore of `[2r-1]`, there is a family of
opposed-hinge roles which:

1. uses every owner exactly once, except possibly one owner when the shore
   size is odd;
2. uses pairwise distinct rank-`r-1` transition roots;
3. partitions into at most

   \[
             (2r-1)\binom{2r-1}{d-1}                         \tag{11.1}
   \]

   fixed-spine, common-endpoint portal banks;
4. has zero owner-attachment homology inside every bank; and
5. has pairwise distinct fixed right-hand named chains inside every bank.

If `r>=4d+1`, every bank separately admits pairwise distinct literal head
states.

For triangular `d=Theta(sqrt(r))`, the number of banks in (11.1) is
`2^{o(r)}`.

#### Proof

Take a Middle Levels Hamilton cycle and project it to its cyclic order of
the `W=binom(2r-1,r)` rank-`r` owners.  Consecutive projected owners are
Johnson adjacent, and their intervening rank-`r-1` roots are all distinct.
Take alternating edges of this owner cycle.  This is a perfect matching
when `W` is even and leaves one owner when `W` is odd.

Orient every selected owner pair and write it uniquely as

\[
                         R\cup\{a\}\longrightarrow
                         R\cup\{b\},                           \tag{11.2}
\]

where `|R|=r-1`.  Choose a canonical `(d-1)`-subset `M(R) subset R`, with
one canonical order, and put

\[
                              D=R-M(R).                         \tag{11.3}
\]

Use the opposed-hinge macro

\[
 (\{a\},D,D_{d-1},\ldots,D_1,\{b\}\cup A),
 \qquad A\subseteq D-\{z\},                                  \tag{11.4}
\]

where the singleton layers `D_1,...,D_(d-1)` are the ordered elements of
`M(R)` and `z in D` is selected later.

Group roles by the pair `(M(R),b)`.  There are at most (11.1) such pairs.
Within one group the internal head spine and mandatory endpoint `b` are
fixed, while `a` may vary.  Every role admits the common head with last
letter `{b}`.  The universal-head fan argument of Theorem 10.1 therefore
kills the complete attachment cycle lattice of the group using literal
`C4`s.

The matched owner pairs are disjoint by construction, and their
intervening roots are distinct.  In one fixed group, equality of two sets
`D` would imply equality of `R=M union D`; hence the `D` are distinct.
The right-hand chains

\[
 D,\quad D\cup D_{d-1},\quad\ldots,\quad D\cup M              \tag{11.5}
\]

are consequently distinct at every rank within that group.

For the head SDR, fix one group and let `S=[2r-1]-(M union {b})`, so

\[
                         |S|=2r-d-1,qquad |D|=r-d.            \tag{11.6}
\]

The group is only a subfamily of `binom(S,r-d)`.  As in Theorem 10.1, it
can use every proper subset `A subsetneq D` by choosing `z in D-A` after
`A`.  For any subfamily `F`, normalized-shadow double counting gives

\[
 |N(F)|\ge {|F|\over\binom{|S|}{r-d}}
          \sum_{j<r-d}\binom{|S|}j.                           \tag{11.7}
\]

Under `r>=4d+1`, the two terms of ranks `r-d-1,r-d-2` already make the
factor in (11.7) at least one: their ratio to the rank-`r-d` layer is

\[
 {r-d\over r}
 +{(r-d)(r-d-1)\over r(r+1)}\ge1.                            \tag{11.8}
\]

After clearing `r(r+1)`, the excess is
`r^2-3rd+d^2-r`, nonnegative under the displayed range.  Hall gives
distinct proper subsets `A`, hence distinct literal heads in that bank.

Finally,

\[
 \log_2\left((2r-1)\binom{2r-1}{d-1}\right)
       =O(d\log(r/d))=o(r)                                   \tag{11.9}
\]

for `d=Theta(sqrt(r))`.  `square`

### Exact scope

Theorem 11.1 closes the one-copy owner/root cover and the attachment-lattice
row with only one possible owner casualty and `2^{o(r)}` portal banks.  It
does **not** yet give a literal chronology.  In (11.4), with the left
optional set fixed empty, the boundary states are

\[
 \begin{aligned}
 p&=(\{a\},D,D_{d-1},\ldots,D_2),\\
 q&=(D_{d-1},\ldots,D_1,\{b\}\cup A).                        \tag{11.10}
 \end{aligned}
\]

Oppositely orienting another owner pair does not exchange these two state
forms: its tail still begins with its endpoint and contains its own `D`,
whereas its head ends with the opposite endpoint and contains `D_1`.
Thus even two roles with the same spine do not automatically cancel their
state boundaries.  The remaining global row is exact head--tail balance
across the portal banks.  Also, (11.5) is proved collision-free only within
each bank; correlating all marked chains across different spines is still
the named-target chain-selector problem.
