# Cut-and-reroute GK completion needs at least 175 cuts in the fixed non-direct face

Date: 2026-07-31  
Status: **exact scoped lower bound and exact relaxed matching formulation**.
No 175-cut completion, prefix, upper continuation, or `K17` word is claimed.

## 1. Exact cut ledger

Let `F` be the authenticated two-cut Greene--Kleitman path forest, and cut a
set `C` of `c` old edges.  Write

\[
 \tau(C)=|\{v:\deg_F(v)=2,\ \delta_C(v)\ne\varnothing\}|.
\]

Deleting `C` leaves

\[
\begin{array}{c|c}
\text{old edges and rank-eight unions}&10152-c\\
\text{components}&5224+c\\
\text{retained old rank-nine turns}&4928-\tau(C).
\end{array}
\]

The final tail still has `16911` rank-seven vertices, `16910` edges, and
`16909` internal turns.  Therefore a reroute uses

\[
 5223+c\text{ ears},\qquad1535\text{ new internal vertices},
\]

\[
 6758+c\text{ new edges},\qquad11981+\tau(C)\text{ new turns}.       \tag{1.1}
\]

Every deleted old edge had a private rank-six intersection and a private
rank-eight union.  Thus the exact rank-six demand becomes

\[
 M_C=M_0\sqcup\{r(e):e\in C\},\qquad |M_C|=2224+c,                 \tag{1.2}
\]

while the number of repeated rank-six edge positions remains

\[
 (6758+c)-(2224+c)=4534.                                           \tag{1.3}
\]

Likewise, the new rank-eight and rank-nine columns may recover the `c`
deleted edge colours and the `tau(C)` deleted turn colours, but must avoid
all retained old colours and remain pairwise distinct.  Hence cut debt is
not free even at the scalar level.

## 2. Exact relaxed port-colour matching

For an old rank-seven vertex `v`, let

\[
 p_C(v)=2-\deg_{F-C}(v).
\]

This is its number of free port incidences after cutting.  Each cut activates
one new incidence at each of its two endpoints.  An isolated old vertex has
two copies, exactly as required by this formula.

Fix an ear-length ledger and let

\[
 Q=\sum_j(j-2)_+x_j                                                   \tag{2.1}
\]

be its number of internal--internal new edges.  Build a bipartite graph with
left shore `M_C` and right shore consisting of

* `Q` universal dummy slots, an optimistic relaxation of the actual
  internal--internal edge catalogue; and
* `p_C(v)` copies of every old vertex `v`, where colour `z` is adjacent to
  a copy of `v` exactly when `z subset v`.

Every physical completion injects each demanded colour into either its
internal--internal edge slot or one old port used by its edge.  Consequently
the relaxed graph must have a matching saturating `M_C`.  For fixed `C`,
this is one ordinary max flow, equivalently

\[
 |A|\le Q+\sum_v p_C(v)
       {\bf1}\{\exists z\in A:z\subset v\}
 \quad(A\subseteq M_C).                                               \tag{2.2}
\]

Equation (2.2) includes the `c` deleted rank-six colours.  It remains only a
necessary condition because the dummy slots are universal and partner,
rank-eight, turn, and component-topology constraints were relaxed.

With variable cuts, use a Boolean `q_e` for each old edge and matching
variables on its two incidence copies `(e,u),(e,v)`, each bounded by `q_e`.
The deleted-colour row is

\[
 \sum_p m_{r(e),p}=q_e.                                               \tag{2.3}
\]

Original missing colours have right-hand side one, every port has capacity
one, and `sum_e q_e=c`.  This is an exact compact MILP projection.  The two
incidences share one activation variable, so optimizing `C` is paired
fixed-charge matching, not ordinary min-cost flow.  Once `C` is fixed it
reduces to max flow.

## 3. The zero-endpoint bank forces `c >= 175`

Retain the old non-direct mix and add one direct reroute for each cut.  Then
the internal--internal capacity remains

\[
 Q=252+2(42)=336.                                                      \tag{3.1}
\]

Let `Y` be the 674 original missing rank-six colours with no old GK endpoint
superset.  At least

\[
                         674-336=338                                  \tag{3.2}
\]

members of `Y` must therefore use cut-created incidences at old internal
vertices.

The independent labelled census is:

```text
Y-degree of old internal vertex    0^3245 1^888 2^588 3^92 4^67 5^48
old edges by internal endpoints    0^2184 1^6080 2^1888
```

Call an old edge *good* when both endpoints are internal and both have
positive `Y`-degree.  There are `501` good edges, with `895` distinct
endpoints, but all those endpoints together see only `294` distinct members
of `Y`.

This already rules out `c=169`: equality in `2c>=338` would force every cut
to be good and every cut incidence to carry a different colour, whereas the
complete good bank reaches only 294 colours.

For the sharper bound, a non-good cut has at most one useful incidence.
Relative to the 294-colour good union, the exact positive new-contribution
histogram of all outside internal vertices is

```text
new colours contributed            1^255 2^118 3^12 4^10.
```

Thus eleven outside incidences contribute at most

\[
                         10\cdot4+1\cdot3=43                           \tag{3.3}
\]

new colours even before overlaps are charged.  Reaching 338 from the good
union needs 44 new colours, so at least twelve cuts have exactly one useful
incidence.

If `g,h,z` selected cuts have respectively two, one, and zero useful
incidences, then

\[
 2g+h\ge338,qquad g+h+z=c,qquad h+2z\le2c-338.                       \tag{3.4}
\]

Since `h>=12`, (3.4) gives

\[
                         \boxed{c\ge175}.                              \tag{3.5}
\]

This is stronger than the scalar `c>=169`.  It is still optimistic: the
deleted-colour equations (2.3), literal edge partners, palettes, turns, and
topology can only increase the required cut count.

## 4. Reproducer

```text
scratch/audit_k17_gk_cut_port_matching_lower_bound_20260731.py
  SHA-256 f66b0c11d014badaec03b455881d577fcd35ea7b8fca4b47400c2e1bb835c766

scratch/k17_gk_cut_port_matching_lower_bound_20260731.audit.json
  SHA-256 e1b96b0f8b96fb13f5e8055d3186b3bf6c5de7cc1f5b8a5290ad7cb983e62148
  payload 6c30934204b2281b7a22b44d76e05a8aa9444081c8ec0433ccf939a57d2a9678
```

The script reconstructs the labelled GK forest independently.  It does not
read or modify the earlier Section 4 audit and performs no broad search.
