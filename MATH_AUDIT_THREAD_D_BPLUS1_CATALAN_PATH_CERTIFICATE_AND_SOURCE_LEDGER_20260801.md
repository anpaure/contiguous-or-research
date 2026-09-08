# Referee audit: the `B+1` certificate is a protected Catalan path, not a near-factor with residual closure

Date: 2026-08-01  
Lane: Thread D / `B+1` owner interface  
Status: exact owner-layer equivalence, protected port gate, and source-cell
ledger.  No source antecedent or all-`k` construction is claimed.

## 0. Verdict

The correction in
`MATH_THEOREM_BPLUS1_CATALAN_HAMILTON_PATH_CERTIFICATE_20260801.md` is
mathematically sound:

* `M0` is a perfect incidence matching;
* `Q` is a matching outside `M0` of size `W-1`;
* `up(Q)` is the complete immediate-upper palette; and
* `lambda(Q)` is a spanning tree.

Then `M0 union Q` is already an alternating Hamilton **path**.  There is no
residual matching and no closure edge.  Selecting one representative of
each upper colour gives

\[
 |Q_0|=U=W-C,\qquad |Q_1|=(W-1)-U=C-1,                 \tag{0.1}
\]

where `Q0` is a rooted Catalan forest and `Q1` is a tree on its `C`
contracted components.

The exact missing protected theorem is consequently a joint
upper-transversal/endpoint-matching/graphic-tree certificate, equivalently
a Hamilton path in the directed component-port graph.  It cannot be
obtained circularly from an arbitrary pre-existing flat factor.

## 1. Exact path equivalence

Let `ML_m` have shores

\[
 {cal L}={{[2m-1]}\choose {m-1}},\qquad
 {cal M}={{[2m-1]}\choose m},
\]

both of size `W`, and put

\[
 U={2m-1\choose m+1},\qquad C=W-U=\operatorname {Cat}_m.
\]

Fix a perfect matching `M0`.  For `e=LV notin M0`, write

\[
 \operatorname {up}(e)=M_0(L)\cup V,qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).              \tag{1.1}
\]

### Proposition 1.1

For a matching `Q subset ML_m-M0`, the following are equivalent.

1. `|Q|=W-1`, `up(Q)` covers all `U` upper colours, and `lambda(Q)` is
   graphic-independent.
2. `M0 union Q` is a spanning alternating Hamilton path and its internal
   lower-shore turns cover all upper colours.

#### Proof

The perfect matching `M0` covers all `2W` incidence vertices.  A matching
`Q` of size `W-1` leaves exactly one vertex uncovered on each shore.  Hence
`M0 union Q` has `2W-1` edges, maximum degree two, and exactly two
degree-one vertices.

Contracting the `M0` edges gives the labelled link graph `lambda(Q)` on
`W` vertices.  A graphic-independent graph with `W-1` edges is a spanning
tree.  Every contracted vertex has degree at most two: at most one `Q` edge
uses its lower endpoint and at most one uses its middle endpoint.  Thus the
tree is a path.  Undoing the contraction gives the asserted alternating
Hamilton path.  The turn at an internal lower vertex `L` is precisely
`M0(L) union V=up(LV)`.

The converse follows by contracting the perfect-matching colour class of
the alternating Hamilton path.  \(\square\)

There is one lower-shore endpoint and one middle-shore endpoint.  The lower
endpoint has no two-owner turn; it is the unique lower-`q1` colour not
realized by an owner-owner transition.

## 2. Exact Catalan decomposition and ports

Choose from `Q` one occurrence of every upper colour and call the chosen
set `Q0`.  Then `|Q0|=U`, its links are a forest, and it has exactly

\[
                             W-U=C                       \tag{2.1}
\]

components, isolated vertices included.  Put `Q1=Q-Q0`; (0.1) follows.
Contracting the `Q0` components turns `Q1` into a spanning tree.

There is a sharper directed formulation.  Since `Q0` is a matching and its
links are a forest, every component is a directed path.  Let

* `t(K)` be its unique terminal vertex with no used outgoing/tail port; and
* `h(K)` be its unique initial vertex with no used incoming/head port.

An incidence from `t(K)` to the middle vertex `M0(h(K'))` is a physical
connector arc `K->K'`.  Endpoint matching permits at most one chosen arc
leaving and at most one entering each component.  Therefore:

> `Q1` is a `C-1`-edge contracted tree if and only if its arcs form a
> directed Hamilton path through the `C` Catalan components.

Indeed, the endpoint capacities make every contracted degree at most two;
graphic acyclicity excludes directed cycles; and a forest on `C` vertices
with `C-1` edges is connected.  Exactly one tail port and one head port
remain unused.  They are the two physical endpoints of the Hamilton path,
not a residual `1 x 1` Hall problem.

## 3. The exact protected common-matroid gate

Let a protected incidence path bank be properly two-edge-coloured

\[
                         P=P_0\mathbin{\dot\cup}P_1.      \tag{3.1}
\]

The noncircular protected certificate consists of the following jointly
chosen objects.

1. A perfect matching `M0` containing `P0` and avoiding every edge of
   `P1`.
2. A split `P1=A0 dotunion A1` and a matching `Q0` containing `A0`, with
   exactly one representative of every upper colour and with forest links.
3. A matching `Q1` containing `A1`, using only the unused tail/head ports of
   `Q0`, whose contracted arcs form a directed Hamilton path.
4. The two final unused ports must equal the declared physical boundary
   types required by the source/compiler interface.

Equivalently, on the physical edge ground set outside `M0`, the union
`Q=Q0 union Q1` obeys the rank equations

\[
 \begin{aligned}
 |Q|&=W-1,\\
 r_{\rm tail}(Q)=r_{\rm head}(Q)&=W-1,\\
 r_{\rm gr}(\lambda(Q))&=W-1,\\
 r_{\rm up}(Q)&=U,\\
 P_1&\subseteq Q.                                      \tag{3.2}
 \end{aligned}
\]

Here the first two ranks are the two endpoint partition matroids,
`r_gr` is the labelled graphic matroid rank, and `r_up` is the partition
rank by upper colour.  The upper row is a full-rank condition rather than
independence, because `|Q|=W-1>U` and connector edges may repeat upper
colours.

The two-stage form is often more informative: `Q0` must simultaneously be
an upper-partition base and be independent in both endpoint partition
matroids and the graphic matroid; `Q1` must extend it to a common endpoint-
feasible graphic base.  This is the exact common-matroid/port correlation.
Neither an upper transversal alone nor an unlabelled spanning tree alone
implies it.

## 4. The `W+1 = W` owners `+ 1` nonowner source-cell ledger

At total source length `B+1`, the relevant depth row has exactly `W+1`
physical cells.  An exact-owner realization of Proposition 1.1 uses

\[
                    W\text{ owner cells}+1\text{ nonowner cell}.      \tag{4.1}
\]

The owner cells must realize every middle owner once.  Their consecutive
owner-owner transitions are the `W-1` links of `Q`.  Therefore the direct
path-certificate realization places the nonowner cell at a boundary of the
owner block.  An interior nonowner would break one edge of `Q` and create
two mixed transitions; that is a different certificate and needs an
explicit bypass/repair theorem.

More precisely, orient the link path from its unique unused head port
`h_*` to its unique unused tail port `t_*`.  The owner order starts at
`M0(h_*)` and ends at `M0(t_*)`; the missing lower colour is `t_*`.
Accordingly the direct one-cell service attaches the nonowner at the
`t_*` end (or, after reversing the whole chronology, at the corresponding
left boundary).

The one boundary nonowner has three separate obligations:

1. provide or route the unique lower-`q1` colour absent from the `W-1`
   owner-owner turns;
2. obey the declared endpoint cap/erosion state at the unused tail and head
   ports; and
3. preserve residence and every deeper lower/upper witness crossing the
   boundary.

Thus (4.1) is an exact scalar ledger, not a compiler theorem.  The owner
path alone does not identify the nonowner payload or prove a common cap.

## 5. Circular arguments excluded

Three tempting derivations are invalid.

### 5.1 Arbitrary protected-factor completion

The small protected-factor theorem gives a spanning two-factor.  It gives
neither one component nor the correlated upper/graphic ranks (3.2).
Opening one edge in each of `c` cycles leaves only `W-c` variable edges,
not the required `W-1` tree unless `c=1`.

### 5.2 Delete an edge from an upper-surjective Hamilton cycle

Even if a protected upper-surjective Hamilton cycle is already known,
deleting its closure edge gives (0.3) only when that edge's upper colour has
another surviving occurrence and the edge is not protected.  The required
transparent opening is extra data, not a consequence of Hamiltonicity.

### 5.3 Insert the pivot into a pre-existing flat source

For the monotone pivot, the `h` pre-insertion crossing cells are

\[
                         U_j=M_j\cup M_{j+1},            \tag{5.1}
\]

of rank one above the `h+1` post-insertion owner cells `M_0,...,M_h`.
Consequently the source before insertion is necessarily nonflat on this
block.  Starting with a flat `B`-length factor and inserting the pivot
assumes away the required nonflat scaffold and is circular.

The valid construction target is a jointly designed `B+1` source whose
final depth row consists of the protected Hamilton owner path and the one
controlled boundary nonowner cell.  Producing that source, its global
residence, arbitrary-width upper coverage, and its literal common lower cap
remain separate hypotheses.

## 6. Referee conclusion

The owner-layer `B+1` correction is a genuine weakening of the earlier
near-factor route:

\[
 \boxed{\text{upper-exact rooted Catalan forest}
        +\text{ protected }(C-1)\text{-connector port path}.}
\]

There is no residual closure.  The exact unresolved owner theorem is the
protected common-rank system (3.2), with prescribed final port types.  The
additional `W+1`-cell source ledger contains one nonowner boundary cell and
cannot be deduced from a pre-existing flat factor.
