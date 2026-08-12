# OFHT as an exact cycle-hypergraph cover: functional Hall, a pointed-star obstruction, and two sufficient faces

Date: 2026-08-01  
Status: exact reformulation and scoped positive/negative theorems.  This note
does not prove the canonical Ferrers OFHT instance, connectedness, residence,
upper coverage, or a compiler theorem.

## 0. Outcome

After the integer age-type multiplicities and their marked positions have
been fixed, the one-copy owner--flag problem has three different forms.

1. Before a literal flag is chosen at each role, it is an exact cover in a
   resource hypergraph, coupled to a cycle-cover condition in the literal
   compatibility digraph.  Equivalently, it is a perfect exact cover by
   compatible directed cycle atoms.
2. After a flag table is fixed, choosing the owners and predecessors is a
   three-partite matching problem.  For integral head--owner variables its
   exact Benders projection consists of the ordinary head and owner
   degree-one rows plus one family of predecessor Hall inequalities.
3. After a functional head--owner bijection is fixed, the remaining aligned
   phase/predecessor choice is exactly a Rado transversal.  Without that
   functionalization, or without literal tail-invariance of a joint flag
   menu, there is no general Rado reduction.

Boolean symmetry gives a useful exact positive face at depth three:
balanced pointed-shadow blocks which are full-fibre closed and
pointed-simple are regular and hence satisfy every Hall cut.  Full-fibre
closure, or complete individual lists, is not sufficient by itself.  At
`(k,m,d)=(7,3,3)` there is a balanced
two-by-two literal block in which both heads retain their complete individual
fibre but share their sole predecessor.

There are also two exact absorbers with different scopes.

* At the static owner/target layer, any target-chain section whose nonempty
  chain maxima form an antichain has an automatic one-copy owner lift by a
  symmetric-chain decomposition of the Boolean lattice.
* At the chronological layer, the primitive adjacent-buffer pair needs
  exactly `d` further occurrences and has the explicit length-`d+2` facet
  absorber.  The owner blocks of these absorbers form a regular hypergraph
  with explicit codegrees, but an exact global tiling is still an additional matching
  theorem.

## 1. Literal states and candidate resources

Fix

\[
                     k\ge r>d\ge1,
 \qquad {\cal O}=\binom{[k]}r,
 \qquad W=|{\cal O}|.
\]

Let `U` be an integer role template of size `W`.  A role `u` has an age
type

\[
 c(u)=(c_0,\ldots,c_d),\qquad c_0>0,\quad c_i\ge0,
 \quad \sum_i c_i=r,                                      \tag{1.1}
\]

and a set `J(u)` of marked prefix positions.  If zero age cells make two
positions offer the same rank, retain at most one of them in `J(u)`.

A literal state for `u` is an ordered disjoint tuple

\[
 X=(X_0,\ldots,X_d),\qquad |X_i|=c_i(u),
 \qquad T(X)=\dot\bigcup_iX_i\in{\cal O}.                  \tag{1.2}
\]

For `j in J(u)` put

\[
                     P_j(X)=X_0\dot\cup\cdots\dot\cup X_{j-1}.
                                                                  \tag{1.3}
\]

For ranks `s` with `1 <= s < r`, let `Q_s` be the prescribed residual named targets of rank
`s`, and put
`Q=disjoint union_s Q_s`, retaining the rank as a resource species.  The
template is numerically compatible when

\[
 \#\{(u,j):j\in J(u),\ |P_j|=s\}=|Q_s|                 \tag{1.4}
\]

for every `s`.

A candidate `xi=(u,X)` consumes the resource set

\[
R(\xi)=\{u,T(X)\}\ \dot\cup\
             \{(|P_j(X)|,P_j(X)):j\in J(u)\}.                \tag{1.5}
\]

Discard a candidate if one of its marked targets is outside the prescribed
residual family `Q` (equivalently, retain the complementary target rows
with right side zero).

Thus the static owner--flag section is exactly a family of `W` candidates
whose resource sets partition

\[
                         U\ \dot\cup\ {\cal O}\ \dot\cup\ Q. \tag{1.6}
\]

This is a hypergraph exact cover, not a bipartite matching: one candidate
simultaneously consumes its role, one owner, and a nested target payload.
If boundary chains are not frozen in advance, add one part for the boundary
addresses and one hyperedge for every legal boundary chain; then replace
`Q` in (1.6) by the complete named lower deck.  Fixing the boundary section
and deleting its targets gives the residual form above.

## 2. Literal compatibility and the exact cycle-hypergraph

Let `E_U` be the allowed role-successor relation.  For candidates
`xi=(u,X)` and `eta=(v,Y)`, put

\[
 \xi\longrightarrow\eta
 \quad\Longleftrightarrow\quad
 (u,v)\in E_U\quad\hbox{and}\quad
 Y_{i+1}=X_i\setminus Y_0\quad(0\le i<d).                  \tag{2.1}
\]

The equalities in (2.1), rather than type inequalities or owner
containment alone, are the literal statewise condition.

### Theorem 2.1 (exact OFHT formulation)

There is a one-copy owner--flag cycle cover if and only if there are binary
variables `x_xi` and `z_(xi,eta)` satisfying

\[
\begin{aligned}
 &\sum_{X\text{ of type }c(u)}x_{u,X}=1 &&(u\in U),\\
 &\sum_{u,X:T(X)=T}x_{u,X}=1 &&(T\in{\cal O}),\\
 &\sum_{u,X,j:P_j(X)=P}x_{u,X}=1 &&(P\in Q),\\
 &\sum_\eta z_{\xi,\eta}=x_\xi,
 \qquad \sum_\eta z_{\eta,\xi}=x_\xi &&(\xi),\\
 &z_{\xi,\eta}=0 &&\text{unless }\xi\to\eta.
                                                               \tag{2.2}
\end{aligned}
\]

Equivalently, let `C` range over directed cycles of the compatibility
digraph whose candidates have pairwise disjoint role, owner, and named
target resources.  Give `C` the hyperedge

\[
                         R(C)=\dot\bigcup_{\xi\in C}R(\xi).    \tag{2.3}
\]

OFHT is equivalent to an exact cover of (1.6) by the cycle hyperedges
`R(C)`.

#### Proof

The first three rows of (2.2) say exactly that the selected candidates
partition (1.6).  The last two rows give each selected candidate one
selected successor and one selected predecessor, so the selected arcs are
a permutation and decompose into directed cycles.  Conversely, a resource-
exact family of compatible cycles supplies the variables in (2.2).
Decomposing a solution of (2.2) into its directed cycles proves the cycle-
hypergraph statement.  \(\square\)

Connectedness is not present in Theorem 2.1.  It is a later topology row.

For a fixed static section `X`, the `z` subsystem is ordinary bipartite
matching and is feasible exactly when

\[
 |N^+(A)\cap X|\ge |A|\qquad(A\subseteq X).                  \tag{2.4}
\]

The difficulty is choosing the same section in the role, owner, target, and
Hall rows.

## 3. Fixed flags: the exact three-partite and Benders forms

Fix a literal flag table `F` after contracting any protected turn bank.
Let `P,Q,O` be the residual tail, head, and owner shores, of equal size.
An aligned column `a` records a head `q(a)`, an owner `o(a)`, a physical
alignment, and its literal predecessor list

\[
                              L_F(a)\subseteq P.               \tag{3.1}
\]

Parallel aligned columns are retained.  A literal turn is a triple
`(p,q(a),o(a))` with `p in L_F(a)`.  Thus the fixed-table problem is a
perfect matching in a three-partite hypergraph, with parallel physical
columns when appropriate.

Choose head--owner columns by binary variables `u_a in {0,1}` satisfying

\[
 \sum_{a:q(a)=q}u_a=1\quad(q\in Q),
 \qquad
 \sum_{a:o(a)=o}u_a=1\quad(o\in O).                         \tag{3.2}
\]

For `X subseteq P`, put

\[
                  A_X=\{a:L_F(a)\cap X\ne\varnothing\}.      \tag{3.3}
\]

### Theorem 3.1 (exact functional-owner Hall projection)

An integral vector `u` satisfying (3.2) extends to distinct literal
predecessors if and only if

\[
                 \boxed{\sum_{a\in A_X}u_a\ge |X|
                         \quad(X\subseteq P).}                \tag{3.4}
\]

Consequently (3.2)--(3.4), with integral `u`, are necessary and sufficient
for a fixed-table one-copy owner-rainbow cycle cover.

#### Proof

After `u` is fixed, make a bipartite graph from `P` to the selected columns,
joining `p` to `a` when `p in L_F(a)`.  The selected column shore has size
`|P|` by (3.2).  Its neighbourhood of `X subseteq P` has cardinality exactly
the left side of (3.4).  Hall's theorem is therefore precisely (3.4), and a
perfect predecessor matching supplies all literal triples.  \(\square\)

Before `u` is fixed this is a three-partite matching gate.  Separate
head--owner and predecessor perfect matchings need not share the same
columns.

### Corollary 3.2 (the exact Rado face)

Fix a bijection `theta:Q->O`.  For each head `q`, let `A_theta(q)` be its
aligned columns with owner `theta(q)`.  Let `M_P` be the transversal matroid
on these columns represented by the predecessor lists (3.1).  There is a
choice of one column at every head with distinct literal predecessors if
and only if

\[
 r_{M_P}\!\left(\bigcup_{q\in Y}A_\theta(q)\right)\ge |Y|
                                      \qquad(Y\subseteq Q).   \tag{3.5}
\]

This is Rado's theorem.  The cited direct joint-menu Rado extension assumes
target-payload neutrality and that changing a tail option does not change
the predecessor status of any head option.  In the complete Boolean atlas
with `2 <= d <= m`, two
different tail flags have different successor sets, so an unpruned
tail-invariant menu is necessarily a singleton.  Thus (3.5) cannot be
promoted to an unrestricted Rado theorem over all flags.

## 4. A smallest full-fibre Hall obstruction

For Sections 4--5 specialize to the normalized depth-three setting
`k=2m+1`, `r=m+1`, `d=3`, with distinguished coordinate `0`.  A head
`(H,gamma)`, where `H subseteq [k]-{0,z}`, aligned by `z` has owner
`H union {0,z}`; after any protected
contraction, `R_z` contains the residual heads assigned this alignment and
`L_z` contains the residual tails carrying it.

Now put `m=3`.  A tail at alignment
`z` is `(S,z)`, `|S|=m-2=1`, and a pointed head is `(H,gamma)`,
`|H|=m-1=2`, with literal predecessor rule

\[
 (S,z)\to(H,\gamma)
 \quad\Longleftrightarrow\quad
 S\subset H,\quad\gamma\in S,\quad z\notin H.                \tag{4.1}
\]

Choose distinct coordinates

\[
                         0,z,\gamma,\beta_1,\beta_2,\delta
\]

all distinct in the seven-point ground set; the seventh point is unused.

Put

\[
\begin{aligned}
 L_z&=\{(\{\gamma\},z),(\{\delta\},z)\},\\
 R_z&=\{(\{\gamma,\beta_1\},\gamma),
         (\{\gamma,\beta_2\},\gamma)\}.
                                                               \tag{4.2}
\end{aligned}
\]

Every head has its complete fibre of `m-2=1` predecessors, but both fibres
are the singleton `({gamma},z)`.  Hence

\[
                         |N(R_z)|=1<2=|R_z|.                   \tag{4.3}
\]

This is the smallest obstruction on the full-fibre pointed face: one head
cannot fail when its complete fibre is retained; `m=3` is the first allowed
dimension; and two heads sharing their unique predecessor are the first
possible deficient family.  It is a local literal Hall obstruction, not a
claim that the block extends to the full canonical target table.

## 5. A Boolean regular face which proves every Hall cut

Continue in the depth-three pointed normal form, now with arbitrary
`m>=3`.  For a fixed alignment `z`, let `L_z,R_z` be balanced:

\[
                              |L_z|=|R_z|.                     \tag{5.1}
\]

Call the block full-fibre closed when

\[
 (H,\gamma)\in R_z,\ \beta\in H-\{\gamma\}
 \quad\Longrightarrow\quad
             (H-\{\beta\},z)\in L_z,                         \tag{5.2}
\]

and pointed-simple when, for every selected tail `S` and `gamma in S`,

\[
\left|\{\beta:(S+\{\beta\},\gamma)\in R_z\}\right|\le1.  \tag{5.3}
\]

Only legal external `beta` satisfying (4.1) are counted in (5.3).  In
(5.2), every `beta in H-{gamma}` is required; if its punctured predecessor
was deleted by the protected contraction, full-fibre closure fails.

### Theorem 5.1 (pointed regular Hall face)

Every nonempty balanced block satisfying (5.2)--(5.3) is
`(m-2)`-regular and has a perfect matching.

#### Proof

Every head has exactly its `m-2` punctured facets by (5.2).  For a fixed
tail, every adjacent head has one pointer `gamma in S`; (5.3) permits at
most one extension for each of the `m-2` possible pointers.  Thus

\[
             \min_{h\in R_z}d(h)=m-2
             \ge\max_{t\in L_z}d(t)>0.                        \tag{5.4}
\]

For `Y subseteq R_z`, edge counting gives

\[
 (m-2)|Y|\le e(Y,N(Y))\le(m-2)|N(Y)|,
\]

so Hall holds.  Equality of shore sizes and degree sums then forces every
tail degree to equal `m-2`.  \(\square\)

For a contracted protected bank, (5.2) also requires that none of the
punctured predecessors has been deleted.  Theorem 5.1 proves the complete
predecessor Hall row only; the target table and functional owner alignment
still have to be chosen on this face.

## 6. A static antichain-top owner absorber

The next lemma separates static target nesting from chronology.

### Theorem 6.1 (antichain-top one-copy lift)

Let `r=ceil(k/2)`.  For every role `u`, prescribe a possibly empty chain

\[
                   {\cal C}_u=\{P_{u,j}:j\in J(u)\}           \tag{6.1}
\]

such that

* `|P_(u,j)|=sum_(i<j)c_i(u)` and the sets are nested in the order of `j`;
* all named sets in all chains are pairwise distinct; and
* the maxima of the nonempty chains form an antichain in `B_k`.

Then the chains admit pairwise distinct rank-`r` owners and literal states
of their prescribed types realizing every chain exactly.

#### Proof

Fix a symmetric-chain decomposition of `B_k`.  Every set of rank below `r`
lies on a symmetric chain which contains a rank-`r` member.  Since the
nonempty maxima in (6.1) form an antichain, no two lie on the same symmetric
chain.  Map each maximum to the rank-`r` member above it on its chain.  This
is an injective containing-owner assignment.  Assign the remaining owners
arbitrarily to the empty chains.

For one role, insert `emptyset` before its prescribed chain and its assigned
owner after it.  Between consecutive prescribed prefix positions, the set
difference has cardinality equal to the sum of the intervening age-cell
sizes.  Partition that difference arbitrarily into ordered blocks of those
sizes.  Doing this in every gap produces disjoint cells
`X_0,...,X_d` of sizes `c_0,...,c_d`, and their prescribed prefix unions are
exactly the sets in (6.1).  \(\square\)

The theorem is useful when all nonempty roles carry a distinct top-rank
anchor.  It does not make transitions between the resulting states literal;
that remains (2.1).

## 7. The primitive chronology obstruction and facet absorber

Assume the source hypotheses

`k >= r+1`, `r > d >= 2`, and `s=r-d >= 2`,

and put

\[
                       s=r-d\ge2
\]

and consider the adjacent-buffer primitive types

\[
 P=(s-1,2,1,\ldots,1),
 \qquad H=(s,1,\ldots,1).                                  \tag{7.1}
\]

The formal primitive is one reciprocal pair `P<->H`.  It has no literal
two-state cycle, even when the owners may change.  More generally, any
owner-simple literal component containing a source of size below `r` has
length at least `d+2`.  For period `2 <= L <= d+1`, every cyclic
`d+1`-window contains every period letter and hence has the same owner,
contradicting owner injectivity.  For `L=1`, the sole window union is the
single source letter and has size below `r`.

Consequently the primitive pair needs at least `d` further occurrences in
any owner-simple one-copy cycle cover.
This lower bound is attained by `d` further short `H` roles.  Choose

\[
 |G|=s-2,
 \qquad b,w,v_1,\ldots,v_{d+1}
\]

pairwise disjoint and use the cyclic source letters

\[
 S_0=G\cup\{w\},
 \qquad S_i=G\cup\{b,v_i\}\quad(1\le i\le d+1).             \tag{7.2}
\]

The `d+1`-window owners are the `d+2` distinct facets

\[
T_t=Z-\{\text{the tag omitted at }t\},
\qquad Z=G\cup\{b,w,v_1,\ldots,v_{d+1}\}.                  \tag{7.3}
\]

With indices modulo `d+2`, define

\[
 C_{t,0}=S_t,\qquad
 C_{t,j}=S_{t-j}\setminus\bigcup_{h=0}^{j-1}S_{t-h}
                         \quad(1\le j\le d).                 \tag{7.3a}
\]

Then `C_(t+1,j+1)=C_(t,j)-C_(t+1,0)` literally.  The state at `t=0`
has type `P`; the other `d+1` states have type `H`.  Designate one of those
as the primitive `H`, mark the primitive `P,H` fully, and mark exactly ranks
`s+1,...,r-1` on the other `d` copies of `H`.  The lowest two marked ranks
occur once each.  At every higher rank the private-tag parts are distinct
proper cyclic intervals (with the common core adjoined), so the full target
sets are distinct.  This is the exact local owner/target-simple absorber.
It does not pack several absorbers globally.

The owner blocks of all such absorbers have a useful exact symmetry.  Put
`q=d+2` and define a `q`-uniform hypergraph on the owner set `{\cal O}` by

\[
 B(Z,V)=\{Z-\{v\}:v\in V\},
 \quad Z\in\binom{[k]}{r+1},\quad
 V\in\binom Zq.                                             \tag{7.4}
\]

Every edge (7.4) is the owner block of a facet absorber: choose
`b in Z-V`, distinguish one member of `V` as `w`, and order the rest as the
`v_i`; then put `G=Z-(V union {b})`, which has size `s-2`.

### Lemma 7.1 (facet-block degrees)

The hypergraph (7.4) is regular of degree

\[
                         D=(k-r)\binom r{q-1}.                 \tag{7.5}
\]

Two distinct owners have codegree zero unless they are Johnson adjacent;
an adjacent pair has codegree

\[
                         \lambda=\binom{r-1}{q-2}.             \tag{7.6}
\]

In particular

\[
                    {\lambda\over D}={q-1\over r(k-r)}
                              ={d+1\over r(k-r)}.              \tag{7.7}
\]

#### Proof

For a fixed owner `T`, choose the unique new point of `Z-T` in `k-r` ways;
that point must lie in `V`, whose other `q-1` points are chosen from `T`.
This gives (7.5).  Two owners are facets of a common `(r+1)`-set exactly
when they are Johnson adjacent, and then that set is unique.  Both omitted
points must lie in `V`, leaving `q-2` choices from their common `(r-1)`-set,
which proves (7.6).  The binomial ratio gives (7.7).  \(\square\)

Uniform edge weight `1/D` is therefore an exact fractional owner cover.
The small codegree is favourable for an approximate nibble, but it is not
an exact factor theorem.  A partition (exact cover) of all owners using
only these blocks would at least require `d+2` to divide `W`; the canonical
template may and generally must mix other modules.  Named-target disjointness is an
additional correlated resource row not measured by (7.5)--(7.7).

## 8. Pin qualification and exact remaining statement

If a comparator pin prescribes the immediate passage `G,v,G`, its incoming
and outgoing trace arcs have the same owner.  Hence it violates the owner
degree-one row before any Hall or Rado test.  A valid one-copy master must
move one side to an uncoloured boundary layer, puncture owner exactness, or
change the comparator address.

The exact positive target left by this note is therefore:

> choose one target-exact literal flag table and one functional head--owner
> attachment whose aligned predecessor blocks satisfy (3.4), preferably by
> arranging the pointed regular face (5.1)--(5.3), while treating every
> protected pin as a fixed consumed resource.

The primitive facet absorber proves that the first reciprocal rotor can be
physicalized at its sharp local cost.  Lemma 7.1 proves only the owner-block
symmetry of packing many copies.  Neither statement gives a global exact
owner/target packing, one component, residence, upper shadows, or an
`O(1)` additive bound.

## 9. Dependencies

The literal recurrence, terminal-star geometry, and original OFHT
formulation are in
`MATH_THEOREM_R_NRFC_LABELLED_COMPATIBILITY_HALL_AND_OWNER_SYMMETRY_LIMIT_20260801.md`.
The fixed functional Hall rows are in
`MATH_THEOREM_K17_H2_PROTECTED_FACTOR_ONECOPY_HALL_AND_RESIDENCE_CUT_20260801.md`.
The Rado face and its tail-invariance boundary are in
`MATH_THEOREM_K_PROTECTED_FUNCTIONAL_RADO_FACE_AND_LITERAL_TRIANGLE_EXCHANGE_OBSTRUCTION_20260801.md`.
The pointed regular face and the two-by-two obstruction are in
`MATH_THEOREM_K_RESET_CONTRACTED_POINTED_SHADOW_REGULARITY_AND_MINIMAL_STAR_OBSTRUCTION_20260801.md`.
The sharp primitive absorber is in
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`.
The immediate comparator-owner obstruction is Proposition 3.2 of
`MATH_THEOREM_THREAD_D_TPC_ONE_COPY_COLOURED_EULER_ROUNDING_20260801.md`.
