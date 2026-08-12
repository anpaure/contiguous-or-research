# The dual GMM forest supplies the `U` deck, but socket--palette synchronization is an extra gate

Date: 2026-07-31  
Status: unconditional dual-deck theorem, exact same-forest closure criterion,
and a finite solver-free counterexample to automatic synchronization; no `K17`
word or new numerical upper bound is claimed

## 0. Result

Let \(\Omega\) have size \(2r-1\), and put

\[
 M={2r-1\choose r-1},\qquad
 N={2r-1\choose r-2},\qquad
 b=M-N=\operatorname {Cat}_r.                       \tag{0.1}
\]

The lower-rainbow GMM forest used for the balanced `A/X/Y` residual factor
has a second, exact interpretation.  Complementing its edge colours gives
all pure `U` owners, and taking the line paths of the forest gives a
lower-rainbow path cover of the complete `U` deck.  Thus the pure-deck
existence problem is automatic once the GMM forest has been chosen.

The joint untagged palette is not automatic.  It is controlled by an exact
zero-slack boundary equation.  If the forest has \(c\) nontrivial path
components and \(n_0=b-c\) isolated vertices, then its `U` paths leave
exactly \(b+c\) untagged colours.  The balanced residual factor has two
socket banks of size \(b\).  In the strict cyclic insertion normal form,
the two socket-colour sets must have union equal to the missing `U` palette
and intersection of size \(n_0\).  After that bank equation, two ordinary
endpoint-containment matchings and one quotient-connectivity test are
necessary and sufficient.

An explicit \(r=3\) tight-enumeration forest and lower-rainbow Hamilton
parent satisfy the balanced residual-factor theorem but fail the bank
equation for every orientation.  Two forced sockets at isolated forest
vertices repeat colours already used inside the `U` deck.  Therefore the
facet-staircase/partial-substitution mechanism supplies the `U` owners
uniformly, but it does **not** by itself supply the joint untagged palette.

For `K17`, the exact remaining owner-level target is consequently a
**boundary-controlled GMM forest** (or a separately chosen dual forest)
whose missing-colour bank is synchronized with the residual sockets.
Upper service, residence, and the common-cap compiler remain later gates.

## 1. The dual line-forest construction

Let

\[
 \mathcal C={\Omega\choose r-1},\qquad
 \mathcal Z={\Omega\choose r-2},\qquad
 \mathcal U={\Omega\choose r+1}.                    \tag{1.1}
\]

Let \(G\) be a spanning linear forest on \(\mathcal C\) with exactly one
edge of colour \(Z\) for every \(Z\in\mathcal Z\).  An edge of colour
\(Z\) joins two distinct members \(C,C'\) containing \(Z\); necessarily

\[
                         C\cap C'=Z.                 \tag{1.2}
\]

Such a forest is exactly what is obtained by suppressing the lower vertices
of a two-level tight enumeration and deleting its direct same-level edges.
It has \(N\) edges and hence \(b=M-N\) components.

For every edge \(e\) of colour \(Z_e\), define

\[
                         U_e=\Omega\setminus Z_e.    \tag{1.3}
\]

On every nontrivial component of \(G\), list its edges in path order and
list the corresponding \(U_e\)'s in the same order.  Isolated vertices of
\(G\) contribute no `U` owner.  Call the resulting path cover
\(\mathscr U(G)\).

### Theorem 1.1 (dual GMM `U`-deck theorem)

The paths \(\mathscr U(G)\) enumerate \(\mathcal U\) exactly once and are
Johnson paths.  Their internal lower colours are exactly

\[
 \mathcal I(G)=
 \{\Omega\setminus C:C\in\mathcal C,\ \deg_G(C)=2\}.             \tag{1.4}
\]

If \(n_0\) is the number of isolated vertices of \(G\) and
\(c=b-n_0\) is its number of nontrivial components, then

\[
 \begin{aligned}
 |V(\mathscr U(G))|&=N,\\
 |E(\mathscr U(G))|&=N-c,\\
 \mathcal D(G)&={\Omega\choose r}\setminus\mathcal I(G)
  =\{\Omega\setminus C:\deg_G(C)<2\},\\
 |\mathcal D(G)|&=b+c=2b-n_0.                       \tag{1.5}
 \end{aligned}
\]

#### Proof

The edge colours of \(G\) enumerate \(\mathcal Z\), and complementation is
a bijection from \(\mathcal Z\) to \(\mathcal U\), proving owner
exactness.  Suppose consecutive forest edges have colours \(Z,Z'\) and
meet at \(C\).  They are distinct rank-\((r-2)\) facets of the same
rank-\((r-1)\) set, so \(Z\cup Z'=C\).  Therefore

\[
 U_Z\cap U_{Z'}
 =\Omega\setminus(Z\cup Z')=\Omega\setminus C,       \tag{1.6}
\]

a rank-\(r\) set.  The two `U` owners are Johnson adjacent, and (1.4)
follows because precisely the degree-two vertices lie between two forest
edges.  A nontrivial forest component with \(q\) edges contributes \(q\)
`U` vertices and \(q-1\) internal edges.  Summing gives \(N\) and
\(N-c\).  Complementation identifies the unused rank-\(r\) colours with
the degree-zero and degree-one vertices of \(G\), proving (1.5). \(\square\)

This is the complement-dual form of the facet-window identity.  A forest
edge colour is one rank below a forest vertex; after complementation it is
one rank above the untagged palette.  Consecutive lower facets become
consecutive pure `U` owners, slot for slot.

In
`MATH_THEOREM_K16_SHIFTED_CHUNK_FACET_SUBSTITUTION_ANATOMY_20260731.md`,
the substituted domain is one rooted four-edge path plus one 45-edge cycle.
Here the same edge-facet operation is applied to all \(N\) edges of a GMM
forest and then complemented.  This explains exactly what the `K16`
partial-substitution mechanism contributes to the odd-to-odd step: the
internal `U` deck and palette, but not its external socket labels.

## 2. The residual socket banks

Let \(F\) be a directed lower-rainbow Johnson 2-factor on
\({\Omega\choose r}\).  Index it by \(i\), with owners \(T_i\), successor
map \(s\), and edge colours

\[
                         C_i=T_i\cap T_{s(i)}.        \tag{2.1}
\]

The \(C_i\)'s enumerate \(\mathcal C\), so we identify the vertices of
\(G\) with these indices.  Choose \(\alpha_i,\beta_i\in\{0,1\}\) satisfying

\[
                  \deg_G(C_i)+\alpha_i+\beta_i=2.    \tag{2.2}
\]

Assume the resulting `A/X/Y` graph is a balanced residual path factor.
Then \(|\alpha|=|\beta|=b\).  Its free socket colours are

\[
 \mathcal S_X=\{T_{s(i)}:\alpha_i=1\},\qquad
 \mathcal S_Y=\{T_i:\beta_i=1\}.                   \tag{2.3}
\]

Each is a set, not merely a multiset, because the parent owner deck is
simple.  The endpoint semantics are literal:

* a free `X` socket created by \(\alpha_i=1\) is the owner
  \(X_{s(i)}=T_{s(i)}+x\), and every untagged seam incident with it has
  colour \(T_{s(i)}\);
* a free `Y` socket created by \(\beta_i=1\) is \(Y_i=T_i+y\), and every
  untagged seam incident with it has colour \(T_i\).

For a `U` endpoint \(U_Z=\Omega\setminus Z\), a socket of colour \(T\)
is a legal Johnson port exactly when

\[
             T\subset U_Z
 \quad\Longleftrightarrow\quad T\cap Z=\varnothing
 \quad\Longleftrightarrow\quad Z\subset\Omega\setminus T.       \tag{2.4}
\]

A direct `Y`--`X` seam is legal exactly when its two socket colours agree;
that common rank-\(r\) set is the seam colour.

## 3. Exact same-forest palette criterion

Use the strict cyclic insertion normal form: each of the \(c\) paths of
\(\mathscr U(G)\) is placed between one free `Y` socket and one free `X`
socket, and the remaining \(b-c=n_0\) socket pairs are joined directly.
All joins are required to have untagged signature.

### Theorem 3.1 (bank overlap, endpoint Hall, and closure)

The external seams can be chosen with pairwise distinct colours completing
the internal `U` palette to all of \({\Omega\choose r}\) if and only if:

1. the **bank equation** holds,

   \[
                 \boxed{\mathcal S_X\cup\mathcal S_Y=\mathcal D(G)};
                                                               \tag{3.1}
   \]

2. after orienting every `U` path, the bipartite incidence graph from its
   left endpoints to \(\mathcal S_Y\setminus\mathcal S_X\), using (2.4),
   has a perfect matching, and independently the graph from its right
   endpoints to \(\mathcal S_X\setminus\mathcal S_Y\) has a perfect
   matching.

Under (3.1), cardinality alone forces

\[
 |\mathcal S_X\cap\mathcal S_Y|
 =2b-|\mathcal D(G)|=b-c=n_0.                       \tag{3.2}
\]

Equivalently, complement the two banks back to the forest-vertex layer:

\[
 \mathcal P_X=\{\Omega\setminus T_{s(i)}:\alpha_i=1\},\qquad
 \mathcal P_Y=\{\Omega\setminus T_i:\beta_i=1\}.                \tag{3.3}
\]

Then (3.1) is the literal defect-support equation

\[
 \boxed{
  \mathcal P_X\cup\mathcal P_Y
   =\{C\in\mathcal C:\deg_G(C)<2\},\qquad
  |\mathcal P_X\cap\mathcal P_Y|=n_0.}             \tag{3.4}
\]

Thus the boundary problem is a two-choice exact cover on the deficient
forest vertices.  It is not implied by the unsigned endpoint count used in
the residual orientation theorem.

The common bank is exactly the set of direct-seam colours; the two bank
differences, each of size \(c\), are exactly the `Y`-port and `X`-port
colours.  The resulting degree-two owner graph is one cycle if and only if
the quotient graph on the \(b\) residual macro paths and \(c\) `U` paths is
connected.  Thus (3.1), the two endpoint matchings, and this last
connectivity test are necessary and sufficient for a spanning cyclic owner
closure with the complete untagged palette.

#### Proof

The `U` interiors use \(N-c\) colours, leaving the set \(\mathcal D(G)\)
of size \(b+c\).  The \(2c\) ports and \(n_0=b-c\) direct seams use
exactly \(b+c\) external colours.  Every port colour is the label of its
one residual socket.  Every direct seam consumes one socket from each bank
with the same label and uses that label once.

If a label lies in both banks and its two sockets were used on separate
ports, that colour would repeat.  Hence every common label is used on a
direct seam.  Conversely every direct seam label lies in both banks.  The
set of distinct external colours is therefore exactly
\(\mathcal S_X\cup\mathcal S_Y\), and exact completion is equivalent to
(3.1).  Equations (1.5) and \(|\mathcal S_X|=|\mathcal S_Y|=b\) give
(3.2).  Once the common labels are paired directly, (2.4) says precisely
that the remaining legal ports are the edges of the two stated incidence
graphs.  For a fixed orientation vector, their perfect matchings are
independent because their colour shores are disjoint.  Finally every owner
and every component endpoint has degree two after the joins, so the result
is a cycle cover; it is one cycle exactly when its component quotient is
connected. \(\square\)

### 3.1 What isolated vertices do, and do not, force

Put

\[
 \mathcal D_0(G)=\{\Omega\setminus C:\deg_G(C)=0\}.              \tag{3.5}
\]

The palette theorem forces only

\[
 |\mathcal S_X\cap\mathcal S_Y|=|\mathcal D_0(G)|=n_0;          \tag{3.6}
\]

it does **not** force equality of these two sets.  Isolated forest vertices
explain why there are \(n_0\) direct seams, but residual rail propagation
may transport their socket labels to different missing colours.  If one
adds the stronger normalization “the direct seam for an isolated forest
slot must carry that slot's own complementary colour,” then and only then
one imposes

\[
               \mathcal S_X\cap\mathcal S_Y=\mathcal D_0(G).    \tag{3.7}
\]

The audit includes a connected \(r=3\) positive closure in which (3.1)
holds but (3.7) fails, so (3.7) is genuinely stronger than palette
exactness.

There is also a useful immediate obstruction.  At an isolated vertex
\(C_i\), equation (2.2) forces \(\alpha_i=\beta_i=1\).  Hence both
\(T_i\) and \(T_{s(i)}\) occur in the socket-bank union.  If either lies
in the already used internal palette \(\mathcal I(G)\), then (3.1) is
impossible, independently of every orientation and endpoint matching.

## 4. A solver-free `r=3` counterexample

Use hexadecimal masks on \(\Omega=[5]\), and take the directed parent
Hamilton cycle

```text
07, 0b, 0d, 15, 1c, 0e, 1a, 19, 13, 16.
```

Its consecutive intersections are

```text
03, 09, 05, 14, 0c, 0a, 18, 11, 12, 06,
```

the ten rank-two sets exactly once.  On these ten colours take the five
forest edges

```text
03--05 colour 01       03--06 colour 02
05--0c colour 04       09--0a colour 08
11--12 colour 10.
```

This is a spanning lower-rainbow linear forest with components

```text
06--03--05--0c,   09--0a,   11--12,   {14},   {18}.
```

It is a genuine tight-enumeration forest: the component order

```text
0c,05,03,06,0a,09,11,12,14,18
```

is a Johnson cycle, and the five displayed forest edges are exactly the
five edges mediated by the five singleton lower vertices.

The dual construction gives all five rank-four `U` owners.  Its only two
internal colours are

\[
             \mathcal I(G)=\{\mathtt{1a},\mathtt{1c}\},          \tag{4.1}
\]

and hence

\[
 \mathcal D(G)=
 \{\mathtt{07},\mathtt{0b},\mathtt{0d},\mathtt{0e},
   \mathtt{13},\mathtt{15},\mathtt{16},\mathtt{19}\}.           \tag{4.2}
\]

The isolated colour `14` occurs at parent index 3.  Its forced `X` socket
has colour

\[
                         T_4=\mathtt{1c}\in\mathcal I(G).        \tag{4.3}
\]

The isolated colour `18` occurs at parent index 6.  Its forced `Y` socket
has colour

\[
                         T_6=\mathtt{1a}\in\mathcal I(G).        \tag{4.4}
\]

Both sockets are forced by (2.2), so every orientation has
\(\{\mathtt{1a},\mathtt{1c}\}\subseteq
\mathcal S_X\cup\mathcal S_Y\).  Equations (4.1)--(4.2) therefore violate
(3.1).  Nevertheless the parent is Hamiltonian, so orienting every
nontrivial forest component and putting both sockets at each isolate gives
a balanced residual `A/X/Y` path factor by the endpoint-orientation
criterion.  Thus residual-factor existence and dual-`U` existence do not
imply their joint palette synchronization.

This is a structural counterexample, not a computational UNSAT claim.

## 5. The exact `K17` specialization

For \(r=8\),

\[
 M=6435,qquad N=5005,qquad b=1430.                \tag{5.1}
\]

If an authenticated GMM forest has \(n_0\) isolates, its dual `U` cover has

\[
 c=1430-n_0\quad\hbox{paths},                       \tag{5.2}
\]

\[
 5005-c=3575+n_0\quad\hbox{internal untagged colours},          \tag{5.3}
\]

and leaves

\[
 |\mathcal D(G)|=1430+c=2860-n_0                  \tag{5.4}
\]

colours.  A cyclic insertion has exactly

\[
 2c+n_0=2860-n_0                                  \tag{5.5}
\]

external seams.  The two residual socket banks each have 1430 labels, so
exactness is precisely

\[
 \mathcal S_X\cup\mathcal S_Y=\mathcal D(G),
 \qquad |\mathcal S_X\cap\mathcal S_Y|=n_0.         \tag{5.6}
\]

There is no scalar slack.  A failed bank label cannot be repaired by adding
another `U` component: subdivision frees one internal colour and creates
one extra seam demand.

`MATH_THEOREM_K17_GMM_ENDPOINT_ORIENTED_RESIDUAL_FACTOR_20260731.md` proves
the existence of \(G,\alpha,\beta\) satisfying the balanced `A/X/Y`
condition.  It does not constrain (5.6), the two endpoint Hall systems, or
quotient connectivity.  The facet-staircase machinery proves the internal
facet-window transfer, but likewise does not constrain those boundary data.
A uniform odd-to-odd recurrence therefore needs one of the following
genuinely stronger inputs:

1. a boundary-controlled GMM theorem choosing \(G,\alpha,\beta\) so that
   (5.6), endpoint Hall, and connected closure hold simultaneously; or
2. an independently chosen dual `U` forest whose missing palette and
   endpoint incidences synchronize with the already chosen residual
   sockets.

Only after this owner-level theorem is proved do all-width upper service,
residence, and the common-cap compiler become the next gates.  Nothing here
proves `K17`, an all-\(k\) recurrence, or a new numerical upper bound.

## 6. Audit

Run

```text
python3 scratch/audit_k17_dual_gmm_u_deck_socket_palette_20260731.py
```

The audit verifies the rank/count identities, the complete `r=3` parent
palette, the tight-enumeration realization of the forest, the dual `U`
deck and its palettes, an explicit balanced residual factor, and all eight
forest orientations.  It also verifies a separate connected positive
fixture for which the direct-colour intersection differs from the isolated
colour set, auditing the distinction between (3.6) and (3.7).  The canonical
result is written to

```text
scratch/k17_dual_gmm_u_deck_socket_palette_20260731.audit.json
```
