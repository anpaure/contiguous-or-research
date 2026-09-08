# Protected exchange robustness, the structural-zero Hamilton gate, and a linear path cover

## Status

The complete clean PBBS packet bank is known to extend to a spanning
two-factor.  This note asks whether that two-factor can always be made
Hamiltonian while retaining every packet edge.

The answer is **not proved here**.  What is proved is:

1. after one matching role is fixed, its full exchange digraph remains
   strongly connected after all protected edges of that role are frozen;
2. after the other factor matching is also forbidden, every closed exchange
   shore must cut a linear number of factor arcs;
3. this still does not force a component-transversal `C6` or a
   Hamilton-safe `C8`; and
4. independently of the cycle-merging gate, the packet bank is contained in
   a spanning linear forest with at most `8h=O(m)` components.

Thus ordinary reachability and linear-component path coverage are no longer
obstructions.  The exact remaining topological statement is a
**short-circuit lifting theorem in the structural-zero exchange digraph**.

## 1. Middle-shadow input

Let

\[
 G=ML_{m+1}=(X,Y;E),\qquad r=m+1,qquad |X|=|Y|=W.
 \tag{1.1}
\]

We use the established middle-shadow inequality

\[
 \boxed{
 |N_G(A)|-|A|\ge\min\{r-1,W-|A|\}}
 \tag{1.2}
\]

for every nonempty `A` in either shore.  This is the
`ML_m` inequality in
`MATH_THEOREM_FACTOR_RESTRICTED_RADO_WEIGHTED_AND_MIDDLE_LEVELS_ROUTER_20260804.md`
with its parameter replaced by `m+1`.

## 2. A protected matching contraction stays strongly connected

Let `M` be an arbitrary perfect matching from `Y` to `X`; thus `M(U)` is
the rank-`m` set matched to `U`.  Define the loopless directed contraction
`D_M` on vertex set `Y` by

\[
 U\longrightarrow V
 \quad\Longleftrightarrow\quad
 U\ne V,\quad M(U)\subset V.
 \tag{2.1}
\]

Every vertex has indegree and outdegree `r-1`.

### Theorem 2.1 (protected contraction robustness)

If \(Z\subseteq Y\) and

\[
 |Z|\le r-2,
 \tag{2.2}
\]

then `D_M-Z` is strongly connected.

#### Proof

If `D_M-Z` were not strongly connected, the union of one sink strong
component would give a nonempty proper set

\[
 Q\subsetneq Y\setminus Z
 \]

with no arc from \(Q\) to \((Y\setminus Z)\setminus Q\).  Every neighbour in
\(G\) of a member of \(M(Q)\) is therefore in \(Q\cup Z\): the matched
neighbour is in `Q`, and every other neighbour is an outneighbour in
`D_M`.  Hence

\[
 N_G(M(Q))\subseteq Q\cup Z,
 \qquad
 |N_G(M(Q))|-|M(Q)|\le |Z|.
 \tag{2.3}
\]

But \(|M(Q)|=|Q|\).  Moreover, properness inside \(Y\setminus Z\) gives

\[
 W-|Q|\ge |Z|+1,
 \]

while (2.2) gives \(r-1\ge |Z|+1\).  Inequality (1.2) now makes the left
side of (2.3) at least \(|Z|+1\), a contradiction. \(\square\)

### Corollary 2.2 (the clean packet role is below the threshold)

Alternately colour every clean four-edge packet path.  Each colour class
contains two protected incidences per packet.  Thus one role freezes a set
`Z` of exactly `2h` contracted vertices.  In the optimal Ferrers range,

\[
 |Z|=2h\le d(d+1)
      =\left(\frac\pi4+o(1)\right)r<r-1.
 \tag{2.4}
\]

Consequently the full one-role exchange digraph remains strongly connected
after every protected edge of that role is frozen.

This is stronger than ordinary matching extension: every unprotected
allowed incidence lies on an alternating matching cycle avoiding `Z`, and
can therefore be inserted while retaining the protected matching edges.
It is not yet a simple-factor Hamiltonization theorem, because that cycle
may use edges of the other factor matching.

## 3. The exact structural-zero cut

Let

\[
 F=M_0\mathbin{\dot\cup}M_1
 \tag{3.1}
\]

be a simple spanning two-factor.  Contract \(M_1\) as above.  The other
matching induces a permutation \(\sigma\) of \(Y\), defined by

\[
 M_1(U)=M_0(\sigma(U)).
\]

Equivalently, the directed \(\sigma\)-cycles are the components of \(F\)
after contraction.  (Only the fact that \(\sigma\) is a permutation and
that its arcs are precisely the contracted \(M_0\) edges is used below.)

Let \(R(F,Z)\) be the **free exchange digraph** on \(Y\setminus Z\).  It
contains the arc \(U\to V\) exactly when

\[
 M_1(U)\subset V,qquad
 V\notin\{U,\sigma(U)\},qquad U,V\notin Z.
 \tag{3.2}
\]

Thus its arcs are precisely the possible new `M_1` incidences which are
neither old `M_1` edges, old `M_0` edges, nor protected-role vertices.

### Theorem 3.1 (factor-boundary price of a closed free shore)

If \(Q\subseteq Y\setminus Z\) has no outgoing arc in \(R(F,Z)\), then

\[
 \boxed{
 |\sigma(Q)\setminus Q|+|Z|
 \ge \min\{r-1,W-|Q|\}.}
 \tag{3.3}
\]

#### Proof

Take `U in Q`.  A neighbour of `M_1(U)` in `Y` is one of four types:

1. `U`, through the old `M_1` edge;
2. `sigma(U)`, through the old `M_0` edge;
3. a protected vertex in `Z`; or
4. the head of a free-exchange arc.

By out-closedness, every neighbour of the fourth type is again in `Q`.
Therefore

\[
 N_G(M_1(Q))\subseteq Q\cup\sigma(Q)\cup Z.
 \]

Subtract \(|M_1(Q)|=|Q|\) and apply (1.2).  This gives (3.3). \(\square\)

When `W-|Q|>=r-1`, (3.3) becomes

\[
 |\sigma(Q)\setminus Q|\ge r-1-|Z|.
 \tag{3.4}
\]

For the clean packet bank, the right side is

\[
 r-1-2h
 \ge\left(1-\frac\pi4-o(1)\right)r.
 \tag{3.5}
\]

Hence a free-exchange obstruction cannot be localized to one interval, or
to any `o(r)` collection of intervals, of the current factor chronology.
It must be globally interlaced across a linear number of factor cuts.

There is also a useful exact special case.  If `Q` is a union of complete
`sigma`-cycles, then `sigma(Q)=Q`.  Provided `Q` is nonempty and leaves a
vertex outside \(Q\cup Z\), (3.3) is impossible under \(|Z|\le r-2\).
Thus no proper union of wholly unprotected factor cycles is closed under
all free exchanges.

## 4. Why this does not yet merge the cycles

A directed triangle in `R(F,Z)` is an alternating Boolean `C6` switch.
If its three vertices lie in three distinct `sigma`-cycles, it merges
those cycles into one while preserving every protected edge and retaining
a simple factor.  A suitable directed four-cycle is the corresponding
parity-changing `C8` bridge for two components.

Theorems 2.1 and 3.1 do **not** imply that either short circuit exists.

* Strong connectivity in Theorem 2.1 is proved before the `M_0` arcs are
  deleted.  Switching through one of those arcs makes the two perfect
  matchings share an edge, producing a coloured two-cycle rather than a
  simple factor.
* Theorem 3.1 proves that a structural-zero obstruction has many
  `sigma`-boundary cuts.  It does not turn those cuts into a directed
  triangle, a directed four-cycle, or any circuit whose support meets each
  old component in the Hamilton-safe order.
* `C6` switches preserve the parity of the component count.  Therefore an
  even-component factor cannot be Hamiltonized by `C6`s alone, regardless
  of their abundance; at least one parity-changing circuit is necessary.

The exact missing statement is therefore:

> **Protected short-circuit lifting lemma.**  Unless `F` is connected,
> `R(F,Z)` contains either a component-transversal directed triangle, or a
> Hamilton-safe directed four-cycle, or a bounded sequence of such circuits
> whose intermediate factors remain simple and avoid `Z`.

Neither the middle-levels Hamilton theorem nor ordinary strong exchange
connectivity proves this lemma.

## 5. An unconditional `O(m)`-component spanning path cover

Although a protected Hamilton cycle is still open, a linear-component
spanning path cover follows directly and with no exposure hypothesis.

### Theorem 5.1 (eight-per-packet protected path cover)

Let \(P\) be a union of \(h\) vertex-disjoint four-edge paths in \(G\).  Then
there is a spanning linear forest \(L\subseteq G\) such that

\[
 P\subseteq L,
 \qquad
 c(L)\le 8h
 \tag{5.1}
\]

for `h>0`.  For `h=0`, one may take a Hamilton path obtained by opening a
Hamilton cycle.

#### Proof

Fix any Hamilton cycle `H` of `G`.  Every component of `P` has three
internal vertices and two endpoints.

First delete from `H` every edge incident with an internal vertex of `P`.
This deletes at most `6h` edges.  At each of the `2h` endpoints of `P`, if
two `H`-edges remain, delete one of them.  Let `D` be the set of all
deleted `H`-edges.  Then

\[
 |D|\le 8h.
 \tag{5.2}
\]

Now put

\[
 L_0=(H-D)\cup P.
\]

Every internal packet vertex has degree two from `P` and no retained
`H`-edge.  Every packet endpoint has one edge from `P` and at most one
retained `H`-edge.  Every other vertex retains degree at most two.
Consequently \(\Delta(L_0)\le2\).

Deleting `|D|` edges from one cycle leaves at most `|D|` connected
components, and adding the edges of `P` cannot increase the number of
components.  Thus `c(L_0)<=8h`.

If `L_0` has a cycle component, that component contains an edge outside
`P`, because `P` itself is a forest.  Delete one such edge from every
cycle component.  This turns each cycle into a path without changing its
connected-component count and without deleting a protected edge.  The
result is the required spanning linear forest \(L\). \(\square\)

For the Ferrers bank,

\[
 c(L)\le8h\le4d(d+1)=O(m).
 \tag{5.3}
\]

This is a genuine topology bound, but it is not an additive-constant word:
serially concatenating all these paths could cost `Theta(m)` seams.

## 6. Exact endpoint-completion obstruction

Theorem 5.1 also isolates what is required to close the linear forest.
For every vertex put

\[
 b_L(v)=2-d_L(v).
\]

Since `L` is a spanning forest with `c(L)` components,

\[
 \sum_v b_L(v)=2c(L).
 \tag{6.1}
\]

A spanning two-factor extending this particular `L` exists exactly when
the residual graph `G-E(L)` has a `b_L`-factor on the deficit vertices.
A Hamilton cycle requires, in addition, that the selected deficit edges
join the path components in one cycle.  Aggregate endpoint balance or
Hamilton-laceability of the undeleted middle-levels graph does not imply
either condition after the internal packet vertices have been saturated.

Thus the proof-safe topology frontier is:

\[
 \boxed{
 \begin{array}{c}
 \text{protected spanning two-factor: proved},\\
 \text{protected spanning }O(m)\text{-path forest: proved},\\
 \text{protected Hamilton cycle/path: open},\\
 \text{missing row: structural-zero short-circuit or endpoint linkage.}
 \end{array}}
 \tag{6.2}
\]
