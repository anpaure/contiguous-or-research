# Independent audit of the `B+1` Catalan Hamilton-path certificate

Date: 2026-08-01  
Lane: K, owner/q1 path certificate and temporal pivot ledger  
Status: **GO**, with a fixed-`M_0` wording correction, a strengthened
directed-port decomposition, and an explicit scope condition on the unique
nonowner cell.

## 0. Verdict

The two formal equivalences in
`MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md`
are correct.

* A perfect incidence matching `M_0` plus a near-perfect matching `Q` of
  size `W-1` gives an upper-surjective alternating Hamilton path exactly
  when the contracted links `lambda(Q)` are graphic-independent.
* Selecting one edge of `Q` for each immediate-upper colour gives an exact
  split

  \[
       |Q_0|=U=W-C,
       \qquad |Q_1|=C-1.                               \tag{0.1}
  \]

  Here `Q_0` is a rooted Catalan forest with `C` components.

The constructive form is sharper than “`Q_1` is a tree.”  Because
`Q_0 union Q_1` is a matching, every `Q_0` component is a directed path
with one free incoming and one free outgoing incidence port, and `Q_1`
must form a **directed Hamilton path through those `C` components**.  An
arbitrary unlabelled component tree is insufficient.

The temporal correction also passes.  Before pivot insertion the `h`
crossing depth-`h` cells are

\[
                         U_j=M_j\cup M_{j+1},qquad |U_j|=r+1,  \tag{0.2}
\]

whereas afterwards they are replaced by `h+1` rank-`r` owner cells.  Thus
the packet cannot be inserted into the same local letters of a pre-existing
flat `B` source.  When `h=d` and `B=W+h`, the final row has `W+1` cells.
A direct simple-carrier construction uses `W` consecutive distinct owner
cells and one controlled boundary surplus.  Calling the surplus a
nonowner is a sufficient design condition—or follows from value-simplicity
of the entire row—but does not follow from the scalar count alone, which
also permits a duplicate owner.

## 1. Fixed-`M_0` path equivalence

Let the two shores of `ML_m` be

\[
 \mathcal L={[2m-1]\choose m-1},
 \qquad
 \mathcal M={[2m-1]\choose m},
 \qquad |\mathcal L|=|\mathcal M|=W.                  \tag{1.1}
\]

Fix a perfect matching `M_0`.  For `e=LV` outside `M_0`, set

\[
 \operatorname {up}(e)=M_0(L)\cup V,
 \qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).             \tag{1.2}
\]

Let `Q` be a matching outside `M_0` of size `W-1`.  The graph
`M_0 union Q` spans all `2W` incidence vertices, has `2W-1` edges, maximum
degree two, and one unmatched vertex of `Q` on each shore.  Contracting the
`M_0` edges gives exactly `lambda(Q)` on `W` vertices.  If those `W-1`
links are graphic-independent, they form a spanning tree.  Matching at the
two endpoints of each contracted `M_0` edge gives contracted degree at most
two, so the tree is a path.  Undoing the contractions gives an alternating
Hamilton path.

At an internal lower vertex `L`, its two owner neighbours are `M_0(L)` and
the `Q`-endpoint `V`; their union is `up(LV)`.  Hence
`up(Q)` is the complete rank-`m+1` palette exactly when the internal lower
turns are upper-surjective.  The converse follows by contracting the
already prescribed decomposition `M_0 union Q`.

The phrase “colour an arbitrary Hamilton path so that one colour is the
fixed `M_0`” would be false.  A Hamilton path determines its own size-`W`
parity class.  Already in `ML_2=C_6`, deleting an edge of a prescribed
perfect matching yields a Hamilton path whose perfect parity class is the
other matching.  This does not refute the formal theorem, because its second
statement already requires the path to equal `M_0 union Q`.

The endpoints are on opposite shores.  The unique lower endpoint has no
two-owner turn, and hence is precisely the one lower-`q1` colour absent from
the `W-1` owner transitions.

## 2. Catalan decomposition and the hidden port condition

Assume the path certificate.  Choose one edge of `Q` carrying each of the

\[
                         U={2m-1\choose m+1}=W-C       \tag{2.1}
\]

upper colours.  Since one edge has one colour, these choices are distinct;
call them `Q_0`.  They remain a matching and their links remain a forest.
On the full `W`-vertex contracted ground this forest has

\[
                         W-U=C                         \tag{2.2}
\]

components, including isolates.  The remainder `Q_1=Q-Q_0` has size
`C-1`.

Because `Q_0` is a matching, every contracted vertex has indegree and
outdegree at most one.  Graphic acyclicity therefore makes each component a
coherently directed path.  It has exactly one vertex with a free incoming
port and one with a free outgoing port.  A `Q_1` edge can connect two
components only from a free outgoing port to a free incoming port; otherwise
`Q_0 union Q_1` would cease to be a matching.

The full link graph is a spanning tree.  After contracting `Q_0`, the
`C-1` links of `Q_1` consequently form a connected acyclic directed graph
with indegree and outdegree at most one.  It is therefore a single directed
Hamilton path on the `C` components.  Conversely, such a free-port path
joins the `Q_0` forest into a spanning link path.  This proves the exact
strengthening

\[
 \boxed{\text{rooted upper-exact Catalan path forest}
       +\text{ directed free-port component path}.}    \tag{2.3}
\]

Ordinary graphic connectivity after forgetting the ports does not imply
(2.3).

## 3. Protected edge-colouring scope

Let a protected incidence path bank have a proper alternating colouring

\[
                         P=P_0\mathbin{\dot\cup}P_1.    \tag{3.1}
\]

For it to lie in the Hamilton path certificate one needs, jointly,

1. a perfect matching `M_0` extending `P_0`;
2. a near-perfect matching `Q` containing `P_1`;
3. one upper representative per colour, with the forced `P_1` edges
   distributed between `Q_0` and `Q_1`;
4. graphic independence and the directed free-port condition of Section 2;
   and
5. the two unused ports must have the boundary types required by the source
   and compiler.

Proper two-edge colouring alone proves none of these extension statements.
The small protected-factor theorem may first embed `P` in an undirected
two-factor and thereby induce a compatible alternating colouring, but it
does not supply upper surjectivity, one component, or the prescribed free
ports.  Thus “the protected collar only adds forced edges” is exact only as
a formulation of the remaining constrained certificate, not as an
existence theorem.

The exact quantifier is worth making explicit.  If the directions of the
protected components matter, first choose a phase on every component so
that

\[
 T_j-I_j\in P_0,\qquad I_j-T_{j+1}\in P_1              \tag{3.2}
\]

along its declared direction (or reverse both classes on the whole
component).  One must then find `M_0,Q_0,Q_1` jointly with

\[
 M_0\cap E(P)=P_0,
 \qquad P_1\subseteq Q_0\mathbin{\dot\cup}Q_1.          \tag{3.3}
\]

The equality in (3.3) follows from the two displayed inclusions and
`Q_0 union Q_1 subseteq ML_m-M_0`, but it records the intended phase without
ambiguity.  A generic two-bounded subgraph may contain a cycle, so the word
“path bank” must mean an edge-simple linear forest.  Otherwise no Hamilton
path can contain it.

### 3.1 Literal-edge versus physical-occurrence protection

Condition (3.3) protects literal **set-valued incidence edges** `(L,V)`.
For a protected Johnson transition whose two incidences are both present,
the internal lower vertex has degree two already; hence its two owner
neighbours and its upper turn are fixed, and the whole protected component
is a contiguous subpath.  A lower endpoint with only one protected
incidence has no fixed turn.  Without the directed phase (3.2), a component
is protected only up to reversal.

The ordinary graph does not distinguish two physical source occurrences
which induce the same incidence edge.  Thus occurrence-level protection
requires an injective map from the named occurrences to distinct graph
edges (as supplied by owner/lower-resource disjoint pivot copies), or an
explicit occurrence-labelled blow-up.  Even with injectivity, (3.3) does
not preserve absolute source positions, exterior context, clipped
residence flags, common caps, or arbitrary-width windows.

Likewise `up(Q)` is set-surjectivity, not a choice of designated occurrence
for each colour.  A protected `P_1` edge is forced to remain in the path,
but it is a designated upper representative only if it is put in `Q_0`.
All protected `P_1` edges may be required in `Q_0` only when their upper
colours are globally distinct.  Resource-disjoint collars in the sense of
disjoint owner and lower-colour vertices need not have distinct upper
colours across different copies.

### 3.2 The pure pivot phase does extend to a perfect class

There is one useful positive specialization.  Any matching `F` of size
`t<=m-1` in `ML_m` extends to a perfect matching.  Indeed, delete its `t`
lower and `t` middle endpoints.  For a family `A` of remaining lower
vertices put `c=W-|A|`.  Since `A` avoids the `t` deleted lower endpoints,
`c>=t`; the middle-shadow bound gives

\[
 |N(A)|-|A|\ge\min\{m-1,c\}\ge t.                     \tag{3.4}
\]

Deleting the `t` prescribed middle endpoints therefore leaves at least
`|A|` neighbours.  Hall completes `F`.

For `H` resource-disjoint collared pivot paths, fix their directions and
take the predecessor incidences as `P_0`.  Then

\[
                         |P_0|=3Hh.                    \tag{3.5}
\]

Under `6Hh<=m-2`, (3.5) is at most `m-1`, so (3.4) supplies a perfect
matching `M_0` containing `P_0`.  Every successor incidence in `P_1` shares
its lower endpoint with its `P_0` partner and is therefore automatically
outside `M_0`.  This discharges the perfect-class/phase subgate for the pure
collar.  It does not construct `Q_0,Q_1`, and extra protected boundary
incidences require their own count and endpoint audit.

## 4. Temporal pivot calculation

Index the old source cut as

\[
 A_{-h},\ldots,A_{-1}mid A_1,\ldots,A_h              \tag{4.1}
\]

and insert `X` at index zero.  For `0<=j<h`, let `C_j` be the old
length-`h+1` crossing interval containing `h-j` left letters and `j+1`
right letters.  Let `M_j` be the new through-`X` interval containing
`h-j` left and `j` right letters.  Then

\[
                         C_j=M_j\cup M_{j+1}.           \tag{4.2}
\]

Both new intervals together contain exactly the old crossing letters plus
`X`; the monotone-pivot hypothesis makes `X` redundant in the old crossing
union.  Since consecutive `M_j` are distinct rank-`r` Johnson neighbours,

\[
                         |C_j|=r+1.                     \tag{4.3}
\]

These are all `h` old crossing cells of `D^h`.  Inserting `X` replaces them
by the `h+1` cells `M_0,...,M_h`; every other `D^h` cell is unchanged.
This proves the temporal correction without using a fitted finite pattern.

Now put `h=d` and `B=W+h`.  A word of length `B+1` has

\[
                         |D^h|=(B+1)-h=W+1             \tag{4.4}
\]

cells.  In the direct boundary-surplus architecture, the pre-insertion
depth row is

\[
 \underbrace{W-h-1}_{\text{unchanged owners}}
 +\underbrace{1}_{\text{controlled boundary nonowner}}
 +\underbrace{h}_{\text{rank-}(r+1)\ C_j},             \tag{4.5}
\]

and the post-insertion row is

\[
 \underbrace{W-h-1}_{\text{unchanged owners}}
 +\underbrace{1}_{\text{same boundary nonowner}}
 +\underbrace{h+1}_{\text{new owners }M_j}.             \tag{4.6}
\]

Thus all `W` owners appear after insertion.  The nonowner is placed at a
boundary so the `W` owner cells remain one consecutive Hamilton chronology;
an internal surplus would require a separate bypass theorem.

Equations (4.4)--(4.6) are a sufficient exact ledger.  Cardinality alone
does not force the surplus to be a nonowner: absent whole-row value-
simplicity it could be a duplicate rank-`r` owner.  The theorem therefore
correctly treats the controlled boundary nonowner and its payload as part
of the still-missing source antecedent.

## 5. Correct remaining theorem

The owner projection is now reduced exactly to a joint choice of

* the perfect class `M_0`;
* an upper-exact rooted Catalan path forest `Q_0`;
* a protected `C-1`-edge directed free-port connector path `Q_1`; and
* the two prescribed terminal port types.

There is no residual perfect matching and no closure edge.  What is not
proved is the jointly designed nonflat source in (4.5), the boundary
nonowner service, global residence, arbitrary-width upper coverage, or the
common lower compiler cap.  In particular, the result cannot be obtained
by inserting the pivot into an already-flat length-`B` source.

This audit is proof-theoretic and uses no finite search.
