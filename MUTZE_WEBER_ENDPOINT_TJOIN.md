# Endpoint antipodalization of the Mütze--Weber path system

## 1. Outcome

The published Mütze--Weber induction already gives an exact spanning family
of dangling paths in

\[
                         Q_{2m+2}(m+1,m+2).                         \tag{1.1}
\]

Its endpoint multiset is very far from antipodal.  If

\[
 C=C_m=\operatorname{Cat}_m,
 \qquad
 D=D_m=C_{m+1}-2C_m,                                  \tag{1.2}
\]

then the four endpoint-sector counts are

\[
 \boxed{(n_{00},n_{10},n_{01},n_{11})
             =(2D+C,\ 2C,\ C,\ 0).}                  \tag{1.3}
\]

Hence no operation which merely permutes the existing terminal endpoints
can produce complementary paths.  At least `D+C` endpoint replacements are
necessary, so `Theta(C_m)` is the optimal scale of any refinement.

The endpoint-moving part has an exact formulation as a capacitated signed
`T`-join.  Relative to the published edge set `H_0`, blue edges are inserted
and red edges are deleted.  The difference decomposes into alternating
trails whose endpoints lie in the endpoint-symmetric-difference set, plus
alternating cycles.  At an old endpoint being internalized the terminal
trail edge is blue; at a new endpoint it is red.  A trail need not pair the
two endpoint types: `A--A` and `B--B` trails may occur in balancing pairs.

After choosing a complement-invariant target endpoint set `T`, the remaining
global condition has a compact certificate.  Add the artificial antipodal
matching on `T`.  The switched system is a complementary path factor if and
only if every cycle in the resulting 2-factor contains exactly one
antipodal matching edge.  Correct path length is then automatic from
Johnson distance and total mass.

Thus the surviving all-dimensional problem is precise:

> Find a complement-invariant `T` and a signed `T`-join of support
> `O(C_m)` for which every augmented cycle contains exactly one antipodal
> edge, while retaining the two-copy shadow provenance of the published
> recursion.

No finite-dimensional computation is used below.

## 2. The published central system

Let

\[
 \mathscr P_m=\mathscr P_{2m}(m,m+1),
 \qquad
 \mathscr U_m=\mathscr P_{2m}(m+1,m+2)               \tag{2.1}
\]

be the central and first-upper Mütze--Weber dangling-path systems.  Their
path counts are

\[
                         |\mathscr P_m|=C,
 \qquad                  |\mathscr U_m|=D.           \tag{2.2}
\]

The central induction is the disjoint union

\[
\begin{aligned}
 \mathscr H_0={}&\mathscr U_m\circ(0,0)\\
 &\mathbin{\dot\cup}\ \mathscr P_m\circ(1,0)\\
 &\mathbin{\dot\cup}\ \mathscr P'_{2m+2},           \tag{2.3}
\end{aligned}
\]

where the mixed family has `C` paths and satisfies

\[
\begin{aligned}
 F(\mathscr P'_{2m+2})&=S(\mathscr P_m)\circ(0,0),\\
 S(\mathscr P'_{2m+2})&=S(\mathscr P_m)\circ(0,1),\\
 L(\mathscr P'_{2m+2})&=F(\mathscr P_m)\circ(0,1).   \tag{2.4}
\end{aligned}
\]

Every path starts and ends in rank `m+1`.  The paths in (2.3) visit every
rank-`m+1` and rank-`m+2` vertex exactly once.

## 3. Exact endpoint-sector ledger

### Proposition 3.1

The endpoint counts of `mathscr H_0` are (1.3).

### Proof

Each of the `D` paths in `mathscr U_m circ (0,0)` has two endpoints in
sector `00`, contributing `2D` there.

Each of the `C` paths in `mathscr P_m circ (1,0)` has two endpoints in
sector `10`, contributing `2C` there.

By (2.4), every one of the `C` mixed paths has its first endpoint in sector
`00` and its last endpoint in sector `01`.  It contributes `C` to each of
those sectors.  No term of (2.3) has an endpoint in sector `11`.  Adding the
three contributions gives

\[
             (2D+C,2C,C,0).                           \tag{3.1}
\]

\(\square\)

Complementation exchanges sectors

\[
                             00\longleftrightarrow11,
 \qquad                      10\longleftrightarrow01.              \tag{3.2}
\]

Therefore the endpoint set of any complementary path factor must have

\[
                             n_{00}=n_{11},
 \qquad                      n_{10}=n_{01}.           \tag{3.3}
\]

### Corollary 3.2 (fixed-endpoint tail-swap no-go)

No sequence of internal cuts and tail reconnections which preserves the
endpoint set of `mathscr H_0` can turn it into complementary paths.

### Proof

Such operations only permute which initial endpoint is joined to which
terminal endpoint.  They do not change the endpoint set or its sector
counts.  The counts (3.1) violate both necessary equalities in (3.3).
\(\square\)

There is also a sharp order-of-magnitude lower bound.  An **endpoint
replacement** removes one old endpoint from the endpoint set and inserts
one formerly internal lower vertex.  Initially the two signed sector
imbalances are

\[
                             \delta_0=n_{00}-n_{11}=2D+C,
 \qquad                      \delta_1=n_{10}-n_{01}=C.              \tag{3.4}
\]

One endpoint replacement decreases
`|delta_0|+|delta_1|` by at most two.  A complement-invariant endpoint set
has both imbalances zero.  Hence:

### Corollary 3.3 (optimal scale)

Every antipodal refinement changes at least

\[
                         {\delta_0+\delta_1\over2}=D+C             \tag{3.5}
\]

endpoint positions.  In particular, `Omega(C_m)` endpoint-moving work is
unavoidable, while the desired `O(C_m)` bound is scale-optimal.

## 4. Antipodality automatically gives the correct length

Put

\[
                         C'=C_{m+1}=D+2C.             \tag{4.1}
\]

### Lemma 4.1

Suppose `C'` vertex-disjoint paths partition both ranks in (1.1), and every
path has complementary lower endpoints.  Then every path contains exactly
`m+2` lower vertices and `m+1` upper vertices.

### Proof

In the Johnson graph `J(2m+2,m+1)`, an `(m+1)`-set and its complement are
at distance `m+1`.  Hence a path between them has at least `m+1` Johnson
edges and at least `m+2` lower vertices.

The total number of lower vertices is

\[
                         {2m+2\choose m+1}=(m+2)C'.   \tag{4.2}
\]

The average over the `C'` paths is therefore exactly `m+2`.  Every path is
at least this long, so equality holds for every path.  Alternation gives
exactly one fewer upper vertex.  \(\square\)

Thus there is no independent path-length balancing problem.

## 5. The signed `T`-join formulation

Let `G` be the bipartite graph in (1.1), with lower class `V` and upper
class `W`.  Let `H_0` be the edge set of the published path system and let
`T_0 subseteq V` be its endpoint set.  Thus

\[
 \deg_{H_0}(u)=2\quad(u\in W),
 \qquad
 \deg_{H_0}(v)=
 \begin{cases}
 1,&v\in T_0,\\
 2,&v\notin T_0.
 \end{cases}                                           \tag{5.1}
\]

Choose a proposed new endpoint set `T subseteq V` with

\[
                         |T|=|T_0|=2C',
 \qquad                  \bar T=T.                   \tag{5.2}
\]

Put

\[
 A=T_0\setminus T,
 \qquad
 B=T\setminus T_0.                                    \tag{5.3}
\]

Then `|A|=|B|`.  Vertices in `A` are old endpoints that must be
internalized; vertices in `B` are old internal vertices that must become
endpoints.

For every edge `e in E(G)`, introduce a signed variable

\[
 x_e\in
 \begin{cases}
 \{-1,0\},&e\in H_0,\\
 \{0,1\},&e\notin H_0.
 \end{cases}                                           \tag{5.4}
\]

The value `-1` deletes a red old edge and `+1` inserts a blue new edge.
Define the boundary demand

\[
 b_T(v)=
 \begin{cases}
 +1,&v\in A,\\
 -1,&v\in B,\\
 0,&\text{otherwise},
 \end{cases}
 \quad(v\in V),
 \qquad b_T(u)=0\quad(u\in W).                       \tag{5.5}
\]

### Theorem 5.1 (exact endpoint `T`-join)

The switched edge set

\[
                         H=H_0+x                              \tag{5.6}
\]

has degree two at every upper vertex, degree one precisely at the lower
vertices in `T`, and degree two at every other lower vertex if and only if

\[
                         \sum_{e\ni v}x_e=b_T(v)
                         \qquad(v\in V\cup W).          \tag{5.7}
\]

### Proof

For every vertex,

\[
                         \deg_H(v)=\deg_{H_0}(v)
                                      +\sum_{e\ni v}x_e.           \tag{5.8}
\]

At an upper vertex (5.7) preserves degree two.  At `A`, it changes degree
one to degree two; at `B`, it changes degree two to degree one; elsewhere
it preserves the old degree.  This proves sufficiency.  Subtracting the
two degree equations proves necessity.  \(\square\)

The bounded signed system (5.4),(5.7) is a capacitated integral
transshipment, or signed `T`-join.  Its incidence matrix is totally
unimodular; the difficulty is not integrality of the endpoint boundary.

### Proposition 5.2 (alternating-trail decomposition)

Every solution of (5.4),(5.7) decomposes into edge-disjoint alternating
trails whose endpoints belong to `A union B`, together with alternating
cycles.  The trail edge incident with an endpoint in `A` is blue, and the
trail edge incident with an endpoint in `B` is red.  A trail may join
`A` to `A`, `A` to `B`, or `B` to `B`.

Conversely, toggling any such family of trails and cycles gives a solution
of (5.7), provided no edge is used twice.

### Proof

Colour `H\setminus H_0` blue and `H_0\setminus H` red.  At every vertex
outside `A union B`, (5.7) gives equal red and blue degree.  At a vertex of
`A` there is one extra blue edge; at a vertex of `B` there is one extra red
edge.  Pair red and blue half-edges arbitrarily, leaving the unique excess
half-edge at each vertex of `A union B` unpaired.  Following these pairings
decomposes the symmetric difference into the stated alternating trails and
cycles.  The colour of each terminal edge is forced by its endpoint type.
The converse follows by checking the same local balances.  \(\square\)

Thus endpoint movement is exactly an alternating-trail problem.  The seam
complexity of the refinement is

\[
                         |\operatorname{supp}x|.       \tag{5.9}
\]

The desired scale is `O(C_m)`, and Corollary 3.3 shows that this is best
possible up to constants.

## 6. The exact antipodal component condition

The `T`-join conditions fix degrees and endpoints, but they do not prohibit
cycles and do not ensure that the two endpoints of one path are complements.
Both requirements have one exact formulation.

For a complement-invariant `T`, let

\[
                         M_T=\{\{v,\bar v\}:v\in T\}                \tag{6.1}
\]

be the artificial antipodal perfect matching on `T`, with every unordered
pair included once.

### Theorem 6.1 (one-antipodal-edge criterion)

Assume (5.4),(5.7), and put `H=H_0+x`.  Then `H` is a family of
complementary paths if and only if every connected component of

\[
                              H\cup M_T                            \tag{6.2}
\]

is a cycle containing exactly one edge of `M_T`.

### Proof

Every upper vertex and every nonendpoint lower vertex has degree two in
`H`.  Every vertex of `T` has degree one in `H` and receives one matching
edge in `M_T`.  Hence (6.2) is 2-regular and is a disjoint union of cycles.

If a component of `H` is already a cycle, it becomes a cycle of (6.2)
containing no antipodal edge.  If several path components of `H` are joined
cyclically by `M_T`, the resulting cycle contains several antipodal edges.
It contains exactly one antipodal edge precisely when it consists of one
path whose two endpoints are that complementary pair.  This proves both
directions.  \(\square\)

Combining Theorem 6.1 with Lemma 4.1 yields an exact equivalence.

### Corollary 6.2 (exact refinement gate)

The published Mütze--Weber system can be converted into an exact wreath
factor by `O(C_m)` edge changes if and only if there are a set `T` satisfying
(5.2) and a signed vector `x` satisfying (5.4),(5.7) such that

1. `|supp(x)|=O(C_m)`; and
2. every cycle of `(H_0+x) union M_T` contains exactly one edge of `M_T`.

The OR-shadow lift additionally requires that these edge changes have
two-copy bulk provenance and only `O(C_m)` recorded cuts, so their depth-`H`
exceptional windows fit in `O(HC_m)` seam halos.

## 7. The remaining theorem

The endpoint-sector obstruction rules out fixed-endpoint switches, but it
does not rule out the signed `T`-join: the required number of endpoint moves
is itself only `Theta(C_m)`.  Total unimodularity removes fractional
integrality as an issue.  The genuinely global obstruction is the
one-antipodal-edge condition of Theorem 6.1.

A proof should therefore proceed in two separated stages:

1. construct an `O(C_m)` alternating-trail `T`-join which makes the endpoint
   set complement-invariant;
2. choose or modify its alternating cycles so that the augmented 2-factor
   has exactly one antipodal edge per cycle.

The second stage is a cycle-splitting/merging problem, structurally similar
to the flippable-cycle method in middle-level Hamiltonicity, but with the
opposite target: every augmented cycle must contain exactly one prescribed
matching edge rather than all cycles being merged into one.

Until this signed `T`-join with cycle control is constructed, no
all-dimensional contractive OR lift is proved.
