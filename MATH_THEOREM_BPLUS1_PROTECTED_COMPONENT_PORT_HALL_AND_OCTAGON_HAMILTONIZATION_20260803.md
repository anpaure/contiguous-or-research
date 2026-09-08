# Exact component-port Hall and protected octagon Hamiltonization for the `B+1` route

**Date:** 2026-08-03  
**Status:** unconditional component-port min--max, exact protected endpoint
criterion, and conditional palette-preserving cycle absorption.  No
computation is used.  This theorem does not construct the required Boolean
port expansion or the arbitrary-width witness bank.

## 0. Outcome

Use the rooted Catalan decomposition of
`MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`.
Thus `M_0` is fixed, `Q_0` is an upper-exact rooted Catalan forest, and

\[
                         C=\operatorname {Cat}_m
\tag{0.1}
\]

is the number of directed path components of `lambda(Q_0)`.  A fixed pivot
collar is already contained in `M_0 union Q_0`, or its forced connector
arcs are first contracted as in Section 1.

Every component has one free outgoing and one free incoming port.  Let `B`
be the bipartite graph of literal connector occurrences between those two
port shores, after deleting all pivot-forbidden, residence-forbidden, and
other structurally unavailable occurrences.  Put

\[
 \delta(B)=max_{X\subseteq\mathcal C}
             \bigl(|X|-|N_B(X)|\bigr)
           =C-\nu(B),                                  \tag{0.2}
\]

where `mathcal C` is the component set and `nu(B)` is maximum matching
size.

The exact port conclusions are:

1. A connector matching `A` leaves exactly

   \[
                             C-|A|                     \tag{0.3}
   \]

   directed path components; every other component is a directed cycle.
2. The least positive number of path components obtainable from this fixed
   port fibre is

   \[
                       \boxed{\max\{1,\delta(B)\}}.     \tag{0.4}
   \]
3. A state with exactly one path plus any number of cycles exists iff

   \[
                             \delta(B)\le1.             \tag{0.5}
   \]
4. For prescribed initial component `S` and terminal component `T`, such a
   state exists iff the graph obtained by deleting the outgoing copy of
   `T` and incoming copy of `S` has a perfect matching.  This is one
   ordinary Hall system.
5. A direct Hamilton path exists iff some total component order makes that
   endpoint Hall matching entirely forward.  Equivalently, the exact
   minimum number of components in a connector **forest** is a min over
   orders of an ordinary Hall deficiency.

Thus ordinary component Hall does more than provide a scalar estimate: it
determines the path-component count exactly.  What it does not determine is
the number of directed cycles.

Every exact four-resource switch preserves the selected tail and head
banks, so it preserves (0.3).  Hence, on a fixed rooted fibre,

\[
 \boxed{\delta(B)>1
 \Longrightarrow
 \text{no port-preserving switch sequence can produce one Hamilton path}.}
\tag{0.6}
\]

When `delta(B)<=1`, choose a `C-1` connector matching.  It gives one path
plus cycles.  If every remaining cycle is serially accessible by a
pivot-disjoint quaternary Boolean octagon using three edges in order on the
current path, the octagon theorem absorbs the cycles one by one, preserves
the complete immediate-upper palette, and ends at the required protected
Hamilton path.

This isolates the topology gate into two exact rows:

\[
 \boxed{\text{one-defect component-port Hall}
        +\text{serial protected cycle accessibility}.}          \tag{0.7}
\]

The first row is solved by max flow.  The second is a genuine Boolean
occurrence theorem and remains open in general.

## 1. Rooted components, protected contraction, and the port graph

Write the components of `lambda(Q_0)` as

\[
                  K=(v_0\longrightarrow\cdots\longrightarrow v_t).
\]

Its free incoming port is at `v_0`, and its free outgoing port is at
`v_t`.  A residual incidence occurrence joining the outgoing port of `K`
to the incoming port of `L` gives a directed component arc `K->L`.

The two copies of the component set form the port graph

\[
 B=(\mathcal C^{\rm out},\mathcal C^{\rm in};E_B).      \tag{1.1}
\]

Delete an edge of `B` whenever its literal occurrence

* meets a protected pivot resource;
* violates a declared endpoint, residence, or source guard;
* is not an available incidence relative to the fixed root `M_0`; or
* conflicts with a connector occurrence already forced by the collar.

If the pivot itself forces connector arcs outside `Q_0`, first check that
they are a directed matching and form no directed cycle.  Their union with
the affected `Q_0` components is then a path forest.  Contract every such
forced path to one supercomponent and build (1.1) on the surviving free
endports.  Every theorem below applies verbatim to this contracted graph.
If the forced bank has a resource collision or a cycle, no protected
Hamilton path can contain it.

This is exact: contraction neither deletes nor invents a free port, and a
completion of the contracted path forest expands uniquely to a completion
containing the forced pivot bank.

## 2. Exact component-port min--max

Let `A` be any matching of `B`.  Regard its edges as directed arcs on
`mathcal C`.

### Lemma 2.1 (path-count identity)

If `p(A)` is the number of directed path components, counting isolated
vertices as paths, and `z(A)` is the number of directed cycle components,
then

\[
                          p(A)=C-|A|.                  \tag{2.1}
\]

### Proof

The matching condition gives indegree and outdegree at most one, so every
weak component is a directed path or directed cycle.  A path on `v`
vertices has `v-1` arcs and a cycle has `v` arcs.  Summing over all
components gives

\[
 |A|=\sum_{\rm paths}(|V|-1)+\sum_{\rm cycles}|V|=C-p(A).
\]

`square`

### Theorem 2.2 (component-port Hall min--max)

The minimum path count among connector matchings is `delta(B)`.  If at
least one path component is required, the minimum is (0.4).  In particular,
a matching whose component graph is one path plus cycles exists iff
`delta(B)<=1`.

### Proof

By Hall's deficiency theorem,

\[
                           \nu(B)=C-\delta(B).          \tag{2.2}
\]

Lemma 2.1 says that a maximum matching has exactly `delta(B)` path
components.  If `delta(B)>=1`, this is already the positive minimum.  If
`delta(B)=0`, a perfect matching gives only cycles; deleting any one of its
edges gives a matching of size `C-1` and exactly one path.  This proves
(0.4).

A one-path state must have `C-1` arcs by Lemma 2.1, so it exists exactly
when `nu(B)>=C-1`, equivalently `delta(B)<=1`.  `square`

This theorem counts cycles separately on purpose.  One-defect Hall is not
itself a Hamilton-path theorem in a reservoir which may contain directed
cycles.

## 3. Prescribed endpoints and the direct acyclic criterion

Fix distinct components `S,T`.  Let

\[
 B_{S,T}=B-\{T^{\rm out},S^{\rm in}\}.                 \tag{3.1}
\]

Both shores of `B_(S,T)` have size `C-1`.

### Theorem 3.1 (exact prescribed-endpoint Hall)

There is a connector state consisting of one directed path from `S` to `T`
and some directed cycles iff

\[
 |N_{B_{S,T}}(X)|\ge|X|
       \qquad(X\subseteq\mathcal C^{\rm out}-\{T\}).   \tag{3.2}
\]

### Proof

Hall says that (3.2) is equivalent to a perfect matching of `B_(S,T)`.
After expansion, every component other than `T` has one outgoing connector
and every component other than `S` has one incoming connector.  Therefore
the unique path starts at `S` and ends at `T`; all other weak components
are cycles.  Conversely such a state gives that perfect matching.  `square`

Now fix a total order `prec` with `S` first and `T` last, and retain only
forward arcs:

\[
 B_{S,T}^{\prec}=\{K^{\rm out}L^{\rm in}\in B_{S,T}:K\prec L\}.
\tag{3.3}
\]

### Theorem 3.2 (ordered Hall is exactly Hamiltonicity)

There is a protected connector Hamilton path from `S` to `T` whose
component order is `prec` iff `B_(S,T)^prec` satisfies Hall.

Consequently, if

\[
 \delta_{\prec}:=
 \max_{X\subseteq\mathcal C}
       (|X|-|N_{B^\prec}(X)|),                         \tag{3.4}
\]

then the minimum number of paths in any acyclic connector matching is

\[
 \boxed{
 p_{\rm forest}(B)=\min_{\prec}\delta_{\prec}.}        \tag{3.5}
\]

In particular `p_forest(B)=1` iff some ordered endpoint Hall system
succeeds.

### Proof

A matching of the forward graph has no directed cycle.  With `C-1` edges,
Lemma 2.1 therefore makes it one Hamilton path.  This proves the first
claim.

For a fixed order, Hall deficiency gives maximum matching size
`C-delta_prec`; every selected arc is forward, so Lemma 2.1 gives exactly
`delta_prec` path components.  Conversely every acyclic connector matching
has a topological order, and lies in the forward graph of that order.
Minimizing over the orders proves (3.5).  `square`

The distinguished-source acyclic Hall theorem from August 1 is the special
case in which one acyclic reservoir and one endpoint are fixed in advance.
Theorems 2.2--3.2 separate what acyclicity buys: it removes precisely the
remaining cycle-accessibility row.

## 4. Palette-preserving switches and the exact invariant

Consider a replacement supported inside the fixed connector bank, so every
used tail and head is one of the current free component ports, and suppose
its old and new phases have identical lower, immediate-upper, tail, and head
resource multisets.  The Boolean hexagon, pentagon, and quaternary octagon
have this resource identity on their authenticated faces, although a
particular use belongs to this proposition only when its support really is
inside the fixed connector bank.

### Proposition 4.1 (port-defect invariance)

On a fixed rooted fibre, every such replacement preserves

* the selected outgoing component-port multiset;
* the selected incoming component-port multiset;
* the number of selected connector arcs; and therefore
* the number `p(A)` of directed path components.

It may change only the cycle count and the way the same ports are joined.

### Proof

Equality of the tail and head resource multisets preserves the selected
outgoing and incoming ports literally.  Equal old/new support size preserves
`|A|`.  Apply Lemma 2.1.  `square`

Consequently, once `Q_0` and its allowed port fibre are fixed,
`delta(B)>1` cannot be repaired by any sequence of exact palette-preserving
connector switches which stays in that fibre.  A switch involving internal
`Q_0` edges is a correlated reselection of the rooted forest and lies
outside this obstruction; it may change `Q_0`, its free ports, and `B`.

### Theorem 4.2 (serial protected octagon Hamiltonization)

Assume `delta(B)<=1`.  Choose a connector matching `A` of size `C-1`, so
`Q_0 union A` consists of one directed path `P` and `z` directed cycles.
Assume that whenever `z>0`, the current state contains a quaternary Boolean
octagon such that

1. one old octagon edge lies on a cycle;
2. the other three old edges occur in the required directed order on `P`;
3. the old and new phases are legal relative to the same root `M_0`;
4. the support avoids the protected pivot collar and its declared witness
   bank; and
5. every non-immediate guard declared in Sections 6--7 is retained or
   reverified.

Then exactly `z` serial switches produce an upper-surjective rooted
Hamilton path containing the protected pivot collar.

### Proof

The quaternary-octagon theorem replaces one directed cycle and the current
path by one directed path with the same endpoints.  It preserves the lower,
immediate-upper, tail, and head resource multisets exactly, and avoids the
pivot.  Therefore it reduces `z` by one, preserves upper surjectivity and
keeps the unique path count equal to one.  Iterate.  After `z` switches no
cycle remains, so the state is one spanning directed path.  `square`

The support-four octagon is sharp for importing only the one existing path:
no exact support-at-most-three exchange contained in one path and one cycle
can eliminate that cycle.  Thus one-defect Hall plus raw `C6` supply is not
enough for this serial route.

## 5. Starting instead from a cap-two cycle cover

Fix `M_0`, and let `F` be an upper-surjective cap-two second perfect
matching.  Its rooted links are a directed cycle cover on all `W` owners.
Since there are `U` upper colours and `W=U+C` selected edges, exactly `C`
upper colours occur twice.  Hence exactly `2C` selected occurrences carry
a duplicated colour.

### Theorem 5.1 (protected safe opening)

Let `P` be a protected edge bank with `|P|<2C`.  Then some edge
`e in F-P` carries a duplicated upper colour.  Deleting `e`

* preserves every immediate-upper colour;
* preserves `M_0` and every protected edge;
* leaves exactly one directed path and the other factor components as
  directed cycles.

If the resulting state satisfies the serial octagon accessibility of
Theorem 4.2, it therefore yields the protected upper-surjective Hamilton
path.

### Proof

The `2C` duplicated-colour occurrences cannot all lie in `P`, so choose
`e` outside it.  Its other same-colour occurrence remains after deletion.
Deleting one edge of a directed cycle opens precisely that component into a
path and changes no other component.  The final assertion is Theorem 4.2.
`square`

For the tight pivot bank, `|P|=O(d)=O(sqrt(m))`, whereas `C` is
exponential, so the immediate-upper safe opening is eventually automatic
once the cap-two protected factor exists.

This connects the fixed-factor selector reduction to the `B+1` path gate:
zero selector energy supplies `F`; topology then consists exactly of a safe
opening and protected cycle absorption.

## 6. Arbitrary-width upper witnesses are a separate guard

Immediate-upper palette preservation does **not** preserve the full
interval-OR tower.  For a cyclic owner chronology `F` and an upper target
`X`, let `mathcal W_X` be the family of cyclic owner intervals whose union
is `X`, and put

\[
                         K_X=\bigcap_{I\in\mathcal W_X}E(I).  \tag{6.1}
\]

Here `E(I)` is the set of cut edges crossed by interval `I`.

### Proposition 6.1 (exact all-width opening test)

Cutting cycle edge `e` preserves target `X` in the resulting linear word
iff

\[
                              e\notin K_X.              \tag{6.2}
\]

Thus an opening is safe for every already covered upper target iff

\[
                     e\notin\bigcup_X K_X.             \tag{6.3}
\]

### Proof

A cyclic witness survives as a nonwrapping linear interval exactly when it
does not cross the cut.  Such a witness exists exactly when not every member
of `mathcal W_X` crosses `e`, which is (6.2).  Intersect over the targets to
obtain (6.3).  `square`

Therefore Theorem 5.1 gives an automatic **q1-safe** opening, not an
automatic all-width-safe opening.  A proof of the `B+1` source must find a
duplicated provider outside both the pivot bank and the forced-cut set in
(6.3), or recreate every lost target after opening.

For a path or path forest with edge labels

\[
                              \lambda(uv)=u\cup v,
\]

the exact width-`q` criterion is: target `X` has a witness iff some
`q`-edge path has all edge labels contained in `X` and their union equal to
`X`.  Consequently a connector or octagon switch is all-width safe whenever
every target has either

1. a retained witness path disjoint from all deleted edges, or
2. an explicitly reverified witness path in the new chronology.

This guard is necessary target by target.  Equality of the immediate-upper
multiset alone supplies only the width-one row.

## 7. Cap two, connector colours, and the exact residual obstruction

Because `Q_0` already contains one occurrence of every upper colour, adding
arbitrary connectors never loses upper surjectivity.  If the stronger
cap-two property is required throughout the rooted-forest construction,
the `C-1` connector edges must additionally have pairwise distinct upper
colours.

This is not part of ordinary component Hall.  It is a three-way occurrence
matching on

\[
       (\text{outgoing component},\text{incoming component},
        \text{upper colour}).                          \tag{7.1}
\]

Even a perfect ordered port matching can be forced to repeat a colour.  For
example, on ordered components `1<2<3`, the unique endpoint matching
`1->2, 2->3` may give both arcs the same colour.  The two-shore Hall system
passes while the rainbow connector does not exist.

Thus the strongest proof-safe conclusion is:

\[
\boxed{
\begin{array}{c}
\text{fixed upper-exact protected }Q_0\\
+\ \delta(B)\le1\\
+\ \text{serial pivot-disjoint octagon accessibility}\\
+\ \text{all-width witness protection}
\end{array}
\Longrightarrow
\text{protected upper-surjective Hamilton path}.}
\tag{7.2}
\]

For the direct acyclic route, replace the middle two rows by one ordered
endpoint Hall system.  If cap two is demanded, add the rainbow occurrence
row (7.1).

The exact residual obstruction is therefore not an unidentified topology
condition.  It is the disjunction:

1. `delta(B)>1`, a certified Hall obstruction which no fixed-fibre
   palette-preserving switch can repair;
2. `delta(B)<=1` but every one-path state has a cycle outside the supported
   protected switch graph; or
3. the topology can be joined but every admissible opening/rethread destroys
   an unreplicated arbitrary-width witness.

Only a correlated reselection of `M_0,Q_0`, the pivot phase, and the guarded
port bank can escape these rows.
