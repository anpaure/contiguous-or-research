# BFE, a hexagon outgoing matching, and the exact port-completion cuts

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Put

\[
 J=[2s],\qquad {\cal D}={\cal D}_s,\qquad
 B=C_s,\qquad c=C_{s-1},
\]

and write \(\overline{\cal D}=\{J\setminus P:P\in{\cal D}\}\).
There are three distinct questions in the proposed hexagon construction.

1. Can oriented incidence hexagons, together with leftover edges, form the
   outgoing perfect matching \(g\)?
2. Can one choose the downward perfect matching \(h\) so that
   \(g\cup h\) consists of equal-length port paths?
3. Can those paths end at the prescribed complements, rather than at a
   permutation of the complementary ports?

The first two questions have exact matching answers at the level of the
abstract middle-levels ledger. For a vertex-disjoint hexagon packing, the
leftover \(g\)-edges exist if and only if the leftover incidence graph
satisfies Hall. After fixing any equal-size phase partition, the
\(h\)-edges exist phase by phase if and only if the corresponding phase
graphs satisfy Hall. These matchings automatically give abstract paths of
equal length \(2s\), but generally with a port twist.

The third question is not another scalar Hall condition. It is an exact
monodromy equation. A phase-homogeneous \(C_6\) toggle changes the abstract
twist by a transported 3-cycle. Consequently:

* a bank of such toggles preserves the parity of the port twist;
* an odd base twist cannot be repaired by \(C_6\) orientations alone;
* in the abstract reusable-switch model, the remaining group obstruction
  is componentwise evenness in the strand 3-uniform hypergraph; and
* for a one-use bank, the exact gate is a Boolean ordered product of the
  transported 3-cycles.

There is a further metric correction. A nonidentity twisted ledger is not
a legal packet in an ordinary fixed-exterior \(s\)-step wreath slab. Its
local endpoint distance is \(|P\cap\tau(P)|<s\) on every moved row, so its
length-\(s\) trace is nongeodesic. Exterior motion can repair the distance
only when

\[
                  |O_L\setminus O_R|=|P\setminus\tau(P)|
\tag{0.0}
\]

on every row, followed by a complete crossing-collar ownership proof. In
particular, a sparse 3-cycle twist has fixed and moved ports and cannot be
realized with one common moving exterior: a fixed port forces the left
side of (0.0) to be zero, while a moved port forces it to be positive.
Thus the \(C_6\) bank below is an abstract matching/path-ledger bank. It
becomes a literal fixed-exterior construction only for an orientation
whose final monodromy is already the identity.

There is also a previously hidden ownership cut. Every extendable outgoing
matching has exactly \(c\) roots which insert \(2s\) first, and those roots,
together with every middle state containing \(\{1,2s\}\), exactly saturate
all upper states containing \(\{1,2s\}\). Thus, after the \(c\) endpoint
roots are fixed, \(g\) is block diagonal across the tight cut

\[
 \boxed{
 \left\{X:\{1,2s\}\subset X\right\}\ \dot\cup\ R_\infty
 \quad\longleftrightarrow\quad
 \left\{Y:\{1,2s\}\subset Y\right\}.}
 \tag{0.1}
\]

Both orientations of a \(C_6\) respect this cut only if all six of its
vertices lie on the same side. In particular, every endpoint root edge is
frozen and no mixed hexagon belongs to the endpoint-face switch bank. This
is an exact cut obstruction to using an arbitrary near-decomposition into
hexagons.

The note ends with a conditional abstract-to-literal compiler theorem. It
identifies the strictly smaller lemma still needed for coefficient one:
construct a
cut-respecting, phase-homogeneous near-decomposition whose leftover Hall
matchings meet the nonuniform Catalan entrance quotas and whose transported
3-cycles solve the port-monodromy equation. If one instead retains a
nonidentity final twist, an owner-dependent exterior-moving packet and its
full crossing collars are additional, presently unproved data.

## 1. The correct nonuniform BFE target

Let

\[
 w_{s,j}=C_{j-1}C_{s-j}\qquad(1\le j\le s).
 \tag{1.1}
\]

The scalar first-return target is not uniform on \([2s]\). Its integral
near-balanced form is

\[
\begin{aligned}
 q_1&=0,\qquad q_{2s}=c,\\
 q_{2j}+q_{2j+1}&=w_{s,j},\qquad
 |q_{2j}-q_{2j+1}|\le1 \quad(1\le j<s).
\end{aligned}
\tag{1.2}
\]

The total is correct because \(w_{s,s}=c\) and
\(\sum_jw_{s,j}=B\). The spike \(q_{2s}=c\) is compulsory. Replacing
(1.2) by uniform coordinate marginals asks for a point outside the exact
factor polytope.

To include ownership and completion, let \(\Gamma(P)\) be the family of
clean length-\(2s\) alternating inclusion paths from \(P\) to
\(\overline P\), meaning that every internal lower state avoids
\({\cal D}\cup\overline{\cal D}\).
For \(\gamma\in\Gamma(P)\), let \(b_1(\gamma)\) be its first inserted
coordinate. Introduce variables \(z_\gamma\ge0\) and impose

\[
\begin{aligned}
 \sum_{\gamma\in\Gamma(P)}z_\gamma&=1
       &&(P\in{\cal D}),\\
 \sum_{\gamma:X\in\gamma}z_\gamma&=1
       &&\left(X\in\binom Js\setminus
                    ({\cal D}\cup\overline{\cal D})\right),\\
 \sum_{\gamma:Y\in\gamma}z_\gamma&=1
       &&\left(Y\in\binom J{s+1}\right).
\end{aligned}
\tag{1.3}
\]

The entrance projection is

\[
 x_{P,X,Y}=\sum_{\substack{\gamma\in\Gamma(P):\\
                 (X_0,Y_0,X_1)=(P,Y,X)}}z_\gamma,
 \qquad
 q_b=\sum_\gamma z_\gamma,1_{\{b_1(\gamma)=b\}}.
 \tag{1.4}
\]

Call (1.3)--(1.4), together with (1.2),
\(\mathrm{BFE}^{\rm ext}_s\). An integral point is exactly an anchored
\({\cal D}_s\)-port path factor with the desired entrance quotas. This is
the ownership-correct version of BFE. Discarding the internal path
variables gives the earlier four-partite entrance hypergraph, which is an
outer relaxation and has no automatic integrality theorem.

The uniform average of the even-pair conjugate factors is a fractional
point of (1.3) with the fractional version of (1.2). Thus the obstruction
below is not fractional feasibility. It is the structure required of an
integral point.

## 2. The forced endpoint face

For one path \(\gamma\), let

\[
 r(\gamma)=\hbox{the insertion time of }2s,\qquad
 d(\gamma)=\hbox{the deletion time of }1.
 \tag{2.1}
\]

### Theorem 2.1 (the endpoint spike holds on the full fractional polytope)

Every point satisfying (1.3) obeys

\[
 \boxed{q_{2s}=c.}
 \tag{2.2}
\]

Moreover every path with positive weight and \(r(\gamma)\le d(\gamma)\)
satisfies

\[
 r(\gamma)=1,\qquad d(\gamma)=s.
 \tag{2.3}
\]

Hence the paths in (2.3) have total weight exactly \(c\).

#### Proof

On one path, the number of upper states containing \(\{1,2s\}\) minus
the number of lower states containing that pair is
\(1_{\{r\le d\}}\). Summing with (1.3) gives

\[
 \sum_\gamma z_\gamma 1_{\{r(\gamma)\le d(\gamma)\}}
 =\binom{2s-2}{s-1}-\binom{2s-2}{s-2}=c.
 \tag{2.4}
\]

The lower pair count on one path is \((d-r)_+\). Therefore

\[
 \sum_\gamma z_\gamma(d(\gamma)-r(\gamma))_+
 =\binom{2s-2}{s-2}=(s-1)c.
 \tag{2.5}
\]

Every path counted in (2.4) contributes at most \(s-1\) to (2.5), and
all other paths contribute zero. Equality in (2.5) forces every
positive-weight path counted in (2.4) to attain the maximum, which is
exactly (2.3). A path inserts \(2s\) first if and only if \(r=1\); (2.2)
now follows from (2.4). \(\square\)

Thus the endpoint law is not merely an invariant of integral factors. It
is a forced face of the ownership LP: all variables indexed by a path with
\(r\le d\) but \((r,d)\ne(1,s)\) vanish.

## 3. The saturated endpoint-corridor cut

Set

\[
\begin{aligned}
 L&=\binom Js\setminus\overline{\cal D},\\
 U&=\binom J{s+1},\\
 R&=\binom Js\setminus{\cal D}.
\end{aligned}
\tag{3.1}
\]

All three relevant shores have size

\[
 |L|=|U|=|R|=sB.
 \tag{3.2}
\]

An integral factor has an outgoing inclusion matching

\[
 g:L\longrightarrow U,\qquad X\subset g(X),
 \tag{3.3}
\]

and a downward inclusion matching

\[
 h:U\longrightarrow R,\qquad h(Y)\subset Y.
 \tag{3.4}
\]

Let

\[
\begin{aligned}
 {\cal X}_\infty&=\left\{X\in\binom Js:\{1,2s\}\subset X\right\},\\
 {\cal Y}_\infty&=\left\{Y\in\binom J{s+1}:\{1,2s\}\subset Y\right\},\\
 R_\infty(g)&=\{P\in{\cal D}:g(P)=P\cup\{2s\}\}.
\end{aligned}
\tag{3.5}
\]

Their sizes are

\[
 |{\cal X}_\infty|=(s-1)c,\qquad
 |{\cal Y}_\infty|=sc,\qquad
 |R_\infty(g)|=c.
 \tag{3.6}
\]

### Theorem 3.1 (tight endpoint corridor)

If \(g,h\) extend to an exact anchored factor, then

\[
 \boxed{
 g\bigl({\cal X}_\infty\dot\cup R_\infty(g)\bigr)
       ={\cal Y}_\infty,}
 \tag{3.7}
\]

and

\[
 \boxed{
 h({\cal Y}_\infty)
       ={\cal X}_\infty\dot\cup\overline{R_\infty(g)},}
 \qquad
 \overline{R_\infty(g)}=\{\overline P:P\in R_\infty(g)\}.
 \tag{3.8}
\]

In particular, fixing a set \(R_\infty\subset{\cal D}\) of size \(c\)
defines an endpoint-corridor face on which both matchings are block
diagonal across (3.7)--(3.8).

#### Proof

By Theorem 2.1, every endpoint row inserts \(2s\) first and deletes
\(1\) last. It therefore contains \(\{1,2s\}\) in each of its
\(s-1\) internal lower states and in all \(s\) upper states. The \(c\)
endpoint rows consequently use

\[
 (s-1)c=|{\cal X}_\infty|,
 \qquad sc=|{\cal Y}_\infty|
 \tag{3.9}
\]

pair-containing resources. Exact ownership says every such resource has
load one, so these rows exhaust both families. Their first outgoing edges
start at \(R_\infty\), their remaining outgoing edges start at
\({\cal X}_\infty\), and all end in \({\cal Y}_\infty\). This proves
(3.7). Their first \(s-1\) downward edges end in
\({\cal X}_\infty\), while their last downward edges end at the
complements of the endpoint roots. This proves (3.8). \(\square\)

This is stronger than the scalar equation \(q_{2s}=c\). A proposed
outgoing matching can have the correct number of endpoint roots and still
be nonextendable because it sends one state of \({\cal X}_\infty\) out of
the corridor. Equation (3.7) is then the explicit violated tight cut.

## 4. What the endpoint cut does to a \(C_6\) bank

An incidence hexagon has lower vertices and upper vertices

\[
\begin{array}{lll}
 x_1=K\cup\{a\},&x_2=K\cup\{b\},&x_3=K\cup\{c\},\\
 y_1=K\cup\{a,b\},&y_2=K\cup\{b,c\},&
 y_3=K\cup\{c,a\},
\end{array}
\tag{4.1}
\]

where \(|K|=s-1\) and \(a,b,c\notin K\) are distinct. Its two
alternating halves are perfect matchings between these three lower and
three upper vertices; their relative permutation is a 3-cycle.

### Lemma 4.1 (a switch cannot straddle a saturated cut)

Let \(A\) and \(B\) be equal-size shores of a tight matching cut, so every
allowed perfect matching under consideration must send \(A\) onto \(B\).
If both alternating halves of one \(C_6\) respect this cut, then either all
three lower vertices lie in \(A\) and all three upper vertices lie in
\(B\), or all six vertices lie outside the cut.

#### Proof

Let \(\alpha_i=1_{\{x_i\in A\}}\) and
\(\beta_j=1_{\{y_j\in B\}}\). For one orientation there is a permutation
\(\pi_0\) with \(\alpha_i=\beta_{\pi_0(i)}\); for the other there is
\(\pi_1\) with \(\alpha_i=\beta_{\pi_1(i)}\). Since
\(\pi_1\pi_0^{-1}\) is a 3-cycle, the three \(\beta_j\)'s are equal.
The three \(\alpha_i\)'s have the same common value. \(\square\)

Apply the lemma to

\[
 A={\cal X}_\infty\dot\cup R_\infty,
 \qquad B={\cal Y}_\infty.
 \tag{4.2}
\]

No switchable inside hexagon can contain a root of \(R_\infty\): that root
omits \(2s\), and two distinct upper neighbours on the hexagon cannot both
be obtained by adding \(2s\). Hence every inside hexagon has all three
lower vertices in \({\cal X}_\infty\); equivalently,

\[
                         \{1,2s\}\subset K.
 \tag{4.3}
\]

The \(c\) edges

\[
                         P\longmapsto P\cup\{2s\}
       \qquad(P\in R_\infty)
 \tag{4.4}
\]

are therefore frozen singleton packets. A claimed massive \(C_6\) bank
must first delete them and must decompose the two residual sides of the
tight cut separately. Mixed hexagons may be used in one fixed orientation,
but they do not supply a legal switch direction in the fixed endpoint
face.

## 5. Completing the outgoing matching after a hexagon packing

Let \({\cal C}\) be a family of vertex-disjoint incidence hexagons in the
bipartite graph \(L-U\). Choosing either alternating half of every member
gives a matching from the covered lower vertices onto the covered upper
vertices. Let \(L_*\) and \(U_*\) be the uncovered vertices.

### Theorem 5.1 (exact leftover criterion for \(g\))

The oriented hexagons extend to an outgoing perfect matching \(g:L\to U\)
if and only if

\[
 |N(S)\cap U_*|\ge |S|\qquad(S\subseteq L_*).
 \tag{5.1}
\]

If a fixed endpoint-root set \(R_\infty\) is prescribed, the extension
lies in the endpoint-corridor face if and only if the forced edges (4.4)
are present, every switchable hexagon satisfies Lemma 4.1, and (5.1) holds
separately on the two leftover blocks of (4.2).

#### Proof

Every hexagon orientation already matches its three lower vertices
bijectively to its three upper vertices. Nothing about its orientation
changes the set of consumed vertices. The remaining task is exactly a
perfect matching in the induced incidence graph \(L_*-U_*\), so (5.1) is
Hall's necessary-and-sufficient condition.

On the endpoint face, the tight-cut equalities forbid crossing edges.
After removing (4.4) and the cut-respecting hexagon blocks, the matching
problem is the disjoint union of its inside and outside induced graphs.
Hall on both blocks is therefore necessary and sufficient. \(\square\)

This theorem is the exact place to choose the leftover \(g\)-edges. No
probabilistic completion statement is needed: either the two Hall systems
hold or a displayed subset \(S\) is a literal obstruction.

## 6. Layered completion by the downward matching

Choose a partition

\[
 \binom Js=L_0\dot\cup L_1\dot\cup\cdots\dot\cup L_s,
 \qquad |L_t|=B,
 \tag{6.1}
\]

with

\[
                         L_0={\cal D},\qquad
                         L_s=\overline{\cal D}.
 \tag{6.2}
\]

The Chung--Feller layers are the natural example, but the theorem needs
only (6.1)--(6.2). Given an outgoing perfect matching \(g\), put

\[
                         U_t=g(L_t)\qquad(0\le t<s).
 \tag{6.3}
\]

The \(U_t\)'s partition \(U\) and each has size \(B\). Let \(G_t(g)\)
be the bipartite containment graph between \(U_t\) and \(L_{t+1}\).

### Theorem 6.1 (abstract layer-Hall completion)

Suppose

\[
 |N(A)\cap L_{t+1}|\ge |A|
 \qquad(A\subseteq U_t, 0\le t<s).
 \tag{6.4}
\]

Then there is a downward perfect matching \(h:U\to R\) for which
\(g\cup h\) is an abstract vertex partition into \(B\) paths, each having
exactly \(2s\) incidence edges, from \({\cal D}\) to
\(\overline{\cal D}\). The terminal port is in general a permutation of
the required one. No fixed-exterior geodesicity is asserted when that
permutation is nonidentity.

Conversely, failure of (6.4) at any phase is an exact cut obstruction to
every downward matching which respects the chosen layers.

#### Proof

By Hall, choose a perfect matching

\[
                         h_t:U_t\longrightarrow L_{t+1}
 \tag{6.5}
\]

in every phase graph. The shores in (6.5) are disjoint as \(t\) varies,
so their union is a downward perfect matching \(h:U\to R\). The
two-step map

\[
                         \sigma_t=h_t\circ g|_{L_t}
                         :L_t\longrightarrow L_{t+1}
 \tag{6.6}
\]

is a bijection. Hence every component begins in \(L_0={\cal D}\), visits
one state in each successive layer, and ends in
\(L_s=\overline{\cal D}\). It has \(s\) two-step transitions, hence
\(2s\) incidence edges. The Hall obstruction is immediate. \(\square\)

This proves equal path lengths in the middle-levels ledger. Exact
complements are the condition which turns the ledger back into local
complement geodesics. Define

\[
 \Sigma=\sigma_{s-1}\cdots\sigma_0:
             {\cal D}\longrightarrow\overline{\cal D},
 \qquad
 \tau(P)=\overline{\Sigma(P)}.
 \tag{6.7}
\]

Here \(\overline{\Sigma(P)}\in{\cal D}\) identifies a terminal port with
its complementary root label. The paths form an untwisted anchored factor
if and only if

\[
                              \boxed{\tau=1.}
 \tag{6.8}
\]

Without (6.8), Theorem 6.1 gives only an equal-length
\(\tau\)-twisted **abstract path ledger**. It is not a literal
fixed-exterior wreath packet.

There is a useful sufficient criterion. Form the layered reachability
graph from \({\cal D}\) to \(\overline{\cal D}\), using all arcs

\[
 X\longrightarrow Z
 \quad\Longleftrightarrow\quad
 X\in L_t,\ Z\in L_{t+1},\ Z\subset g(X).
 \tag{6.9}
\]

If the complement matching \(P\mapsto\overline P\) is the unique perfect
matching in this root-to-terminal reachability graph, then every choice of
the phase matchings (6.5) has \(\tau=1\). This is sufficient, not
necessary.

## 7. A phase-homogeneous hexagon is an abstract order-three switch

Assume now that the three lower vertices of every hexagon \(C\in{\cal C}\)
lie in one layer \(L_{t(C)}\). Since both orientations use the same three
upper vertices, changing the orientation does not change the sets
\(U_t=g(L_t)\). Therefore the Hall systems (6.4) are independent of all
hexagon orientations. Fix one collection of downward matchings \(h_t\).

For one hexagon in phase \(t\), write its three upper vertices as
\(y_1,y_2,y_3\) and put \(z_i=h_t(y_i)\in L_{t+1}\). Toggling the
hexagon cyclically reassigns the three lower states to
\(z_1,z_2,z_3\). Thus

\[
                         \sigma_t'=\rho_C\sigma_t,
 \tag{7.1}
\]

where \(\rho_C\) is a 3-cycle on \(L_{t+1}\). The three lower states lie
on distinct abstract paths because they occupy the same layer.
Consequently the toggle cyclically permutes three right tails and creates
no detached cycle or unequal path in the ledger. It is a genuine
order-three **ledger switch**, not merely an unstructured degree-factor
cycle. It is not, by this fact alone, a geodesic fixed-exterior slab
substitution.

Let \(\rho_t(\epsilon)\) be the product of the disjoint 3-cycles selected
in phase \(t\), and let \(\sigma_t^0\) denote a base orientation. Then the
exact terminal map is

\[
 \Sigma_\epsilon=
 (\rho_{s-1}(\epsilon)\sigma_{s-1}^0)
 \cdots
 (\rho_0(\epsilon)\sigma_0^0).
 \tag{7.2}
\]

Moving the base maps to the right rewrites this as

\[
                         \tau_\epsilon
       =\Delta_{s-1}(\epsilon)\cdots\Delta_0(\epsilon)\tau_0,
 \tag{7.3}
\]

where every \(\Delta_t(\epsilon)\) is a product of fixed transported
3-cycles on the port-label set. Thus the exact one-bank endpoint gate is

\[
 \boxed{
       \Delta_{s-1}(\epsilon)\cdots\Delta_0(\epsilon)=\tau_0^{-1},
       \qquad \epsilon_C\in\{0,1\}.}
 \tag{7.4}
\]

Equation (7.4), not Hall, is the residual port condition.

### Corollary 7.1 (parity obstruction)

For fixed downward matchings \(h_t\), all choices of the \(C_6\)
orientations have the same twist parity. If \(\tau_0\) is odd, no
orientation produces an untwisted factor.

#### Proof

Every factor in the left side of (7.4) is a 3-cycle and is therefore even.
\(\square\)

The smallest matching switch capable of changing this parity is an
alternating \(C_8\): toggling an alternating incidence cycle of length
\(2k\) changes the strand permutation by a \(k\)-cycle, whose sign is
\((-1)^{k-1}\). A \(C_6\) has \(k=3\) and is even; a \(C_8\) has
\(k=4\) and is odd.

For abstract reusable switches, make a 3-uniform hypergraph
\({\cal H}_{\rm str}\)
on the port labels, with one hyperedge for the support of each transported
3-cycle in (7.3).

### Proposition 7.2 (the abstract reusable-switch group)

The group generated by the transported \(C_6\) switches is

\[
             \prod_{K\in\operatorname{comp}({\cal H}_{\rm str})}
                  \operatorname{Alt}(K),
 \tag{7.5}
\]

with the evident convention on components of size below three. Hence, in
the abstract ledger algebra, a reusable \(C_6\) bank can cancel
\(\tau_0\) if and only if \(\tau_0\) preserves every strand component
and has even restriction to every component. This is not a physical
fixed-exterior repetition theorem.

#### Proof

Every generator is a 3-cycle supported in one component, so the generated
group is contained in the right side. Conversely, order the hyperedges of
one connected component so that each new edge meets the union of the
preceding ones. Starting with one 3-cycle, conjugating a newly available
3-cycle by the alternating group already generated on the old vertices
produces all 3-cycles needed to add its one or two new vertices. Induction
gives the full alternating group on the component. Different components
have disjoint supports and their groups commute. \(\square\)

For a one-use bank, (7.5) gives necessary but not sufficient conditions:
the Boolean ordered-product equation (7.4) is strictly stronger than
membership in the generated group.

### Theorem 7.3 (fixed-exterior metric obstruction)

Let \(O_L,O_R\) be exterior sets, disjoint from \(J\), such that the two
ambient boundary states have the same size. Put

\[
                              e=|O_L\setminus O_R|.
\tag{7.6}
\]

For a local port \(P\in\binom Js\) and terminal label
\(Q\in\binom Js\),

\[
 d_J\bigl(O_L\cup P,,O_R\cup(J\setminus Q)\bigr)
                              =e+|P\cap Q|.
\tag{7.7}
\]

Consequently an \(s\)-step geodesic realization of an abstract twist
\(Q=\tau(P)\) requires, row by row,

\[
                              \boxed{e=|P\setminus\tau(P)|.}
\tag{7.8}
\]

In particular:

1. fixed exterior \(O_L=O_R\) forces \(\tau(P)=P\) on every row;
2. one common moving exterior can realize only twists for which
   \(|P\setminus\tau(P)|\) is constant over all ports; and
3. a sparse 3-cycle twist, which has both fixed and moved ports, has no
   common-exterior \(s\)-step geodesic realization.

#### Proof

The elements removed between the two boundary states are the disjoint
union

\[
                         (O_L\setminus O_R)
                         \mathbin{\dot\cup}(P\cap Q),
\]

which proves (7.7). Setting this distance equal to \(s\), and using
\(|P\cap Q|=s-|P\setminus Q|\), gives (7.8). A fixed port gives zero on
the right of (7.8), while a moved port gives a positive value, proving the
last assertion. \(\square\)

Even (7.8) is only the metric gate. A physical exterior-moving packet must
also exhibit every intermediate crossing state and prove exact ownership
of the exterior/local mixed \(X\)-states and \(Y\)-colours. The abstract
group calculation (7.3)--(7.5) supplies none of this collar ledger.

## 8. Relation to the ballot-forced cycle bank

For every exact port factor, the ballot argument supplies at least

\[
 \frac{s-1}{(s+1)(s+2)}C_s
       =\left(\frac1s+O(s^{-2})\right)B
 \tag{8.1}
\]

pairwise edge-disjoint alternating-cycle certificates in the outgoing
matching. This proves a genuine uncoloured cycle supply. The present
analysis identifies the extra conditions needed before those certificates
can be used by BFE:

1. **Endpoint cut:** a switch must not straddle (3.7).
2. **Phase:** its lower vertices must lie in one \(L_t\) if it is to be an
   automatic equal-length tail switch.
3. **Entrance movement:** only switches meeting \(L_0={\cal D}\) change
   the first-edge quota vector.
4. **Monodromy:** the transported 3-cycles must solve (7.4).
5. **Physical metric:** unless the final twist is identity, a literal
   wreath realization requires (7.8) and the complete moving-exterior
   crossing collars.

Thus (8.1) alone does not prove near-balanced entrance ownership. It can
be concentrated in internal phases, and mixed certificates are frozen by
the endpoint cut. On the other hand, a cut-respecting phase-homogeneous
subbank immediately becomes an **abstract** order-three ledger bank after
the layer-Hall completion of Theorem 6.1. Its precise positive use in the
fixed-exterior problem is to search among orientations for one satisfying
\(\tau=1\); nonidentity orientations are not physical intermediate
packets.

## 9. Conditional hexagon compiler

The preceding results combine into the following exact statement.

### Theorem 9.1 (identity-orientation hexagon-to-BFE compiler)

Assume there are:

1. a set \(R_\infty\subset{\cal D}\) of size \(c\);
2. a vertex-disjoint, endpoint-cut-respecting family of incidence
   hexagons, each homogeneous in one layer \(L_t\);
3. leftover outgoing matchings satisfying the two block Hall systems of
   Theorem 5.1;
4. an orientation and leftover choice whose root edges satisfy the
   nonuniform quotas (1.2);
5. the layer Hall systems (6.4); and
6. a choice of phase matchings and hexagon orientations satisfying the
   monodromy equation (7.4).

Then the resulting \(g\cup h\) is an integral point of
\(\mathrm{BFE}^{\rm ext}_s\). It is an exact anchored
\({\cal D}_s\)-port factor and has the required first-edge quotas. Its
hexagon blocks form a bank of abstract order-three alternative ledger
orientations. Only those joint orientations which again satisfy (7.4)
are literal fixed-exterior factors; a single nonidentity toggle is not.

#### Proof

Theorem 5.1 gives the outgoing perfect matching in the fixed endpoint
face. Theorem 6.1 gives a downward perfect matching and equal-length
paths. Condition 4 gives the BFE quotas. Equation (7.4) makes the terminal
map the complement matching. Exact ownership is built into the two perfect
matchings. With identity terminal map, every \(s\)-step row joins a set to
its complement and is geodesic. Section 7 proves only the abstract
order-three ledger assertion for the alternative orientations, consistently
with Theorem 7.3.
\(\square\)

## 10. Exact remaining lemma and obstruction ledger

The near-hexagon proposal is therefore neither refuted nor completed by a
raw \(C_6\) count. Its exact remaining lemma is:

> **Cut-respecting phase-hexagon completion.** Construct a fixed
> endpoint-root set \(R_\infty\), reserve its \(c\) forced edges, and pack
> all but \(o(sB)\) of the remaining outgoing shores by hexagons which are
> simultaneously endpoint-cut-respecting and phase-homogeneous. Complete
> the leftovers through the block Hall systems, meet (1.2) using the
> phase-zero blocks, satisfy all layer Hall systems, and solve the Boolean
> monodromy equation (7.4).

There are now four audited failure certificates.

1. A subset violating (5.1) obstructs the leftover outgoing matching.
2. A subset violating (6.4) obstructs the layered downward matching.
3. Even when every Hall inequality holds, an odd base twist obstructs all
   \(C_6\)-only endpoint corrections; more generally, failure of the
   component conditions in Proposition 7.2 obstructs every reusable
   switch correction.
4. A retained nonidentity twist is prohibited in a fixed-exterior slab by
   Theorem 7.3. Exterior motion must satisfy (7.8) on every owner, and the
   metric equality still leaves the full crossing-collar ownership ledger
   to be constructed.

Most importantly, (3.7) is a coefficient-scale ownership cut forced by
the \(C_{s-1}\) endpoint spike. It shows why the scalar/fractional BFE
transport cannot simply be rounded by orienting an arbitrary massive
hexagon decomposition. The decomposition must be built around the forced
endpoint corridor from the beginning.
