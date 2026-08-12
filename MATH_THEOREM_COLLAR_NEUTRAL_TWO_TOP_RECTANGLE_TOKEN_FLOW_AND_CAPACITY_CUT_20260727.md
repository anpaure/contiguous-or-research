# Collar-neutral two-top rectangles: exact token flow and the endpoint-capacity cut

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Use the standard maximal-height calibration

\[
 W=\binom{2m}{m},\qquad
 H=\max\left\{h:
 {W\over\binom{2m}{m-h}}\le m+h\right\}.
\tag{0.1}
\]

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
\qquad
 N=\binom{2m}{M},\qquad
 \lambda={W\over N},\qquad T=dN.
\tag{0.2}
\]

Maximality gives

\[
 m-H<\lambda\le m+H.
\tag{0.3}
\]

Indeed the upper bound is the defining inequality, while failure at
\(H+1\), together with

\[
 \binom{2m}{m-H-1}
 =N{m-H\over m+H+1},
\]

gives the lower bound. Also

\[
 {W\over\binom{2m}{m-h}}
 =\prod_{j=1}^{h}{m+j\over m-j+1}.
\]

This tends to one for fixed \(h\), but is exponential in \(m\) when
\(h\) is a fixed positive fraction of \(m\). Hence \(H\to\infty\)
and \(H=o(m)\).

Thus, for all sufficiently large \(m\), \(H\ge3\),
\(m\ge6H+4\), and

\[
 N=(1+o(1)){W\over m},\qquad
 T=W-o(W).
\tag{0.4}
\]

This note studies the natural all-core closure of the certified
collar-neutral two-top rectangle from
MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md
and arbitrary chronological compositions of its coordinate relabellings
and inverses: both local legs swap their first two letters, their
protected derivatives cancel at every \(h\ne H\), and their middle
derivative is nonzero. Every top carries exactly one physical all-core
path at every time. If a subcatalogue additionally prescribes a common
fixed terminal core, some partner edges below may disappear; every
capacity obstruction remains valid, while the exact complete-bipartite
reachability statement is for the unrestricted all-core closure.
Path states are literal full words. No gauge identification or free
re-encoding of invisible suffix positions is allowed; the separately
proved cyclic re-rooting is an additional move and is not part of the
rectangle-only graph analyzed in Sections 1--7.

The global matching problem has an exact answer.

1. At one top, every certified rectangle projects to the same involution

   \[
   \beta(p_1,p_2,p_3,\ldots,p_M)
   =(p_2,p_1,p_3,\ldots,p_M).
   \tag{0.5}
   \]

   Thus the unordered first pair and the complete ordered tail are
   invariant. Every projected top component has two states.

2. The full compatibility graph splits into explicit classes
   \(\Lambda\). Inside one class it is a complete bipartite graph, and
   chronology is exactly exclusion-process token swapping. If
   \(n_{\eta\epsilon}^{\Lambda}\) are the four state counts and

   \[
   \alpha_\Lambda=\min(n_{01}^\Lambda,n_{10}^\Lambda),
   \qquad
   \beta_\Lambda=\min(n_{00}^\Lambda,n_{11}^\Lambda),
   \tag{0.6}
   \]

   then the exact attainable middle correction in that class is

   \[
   t_\Lambda r_\Lambda,\qquad
   -\alpha_\Lambda\le t_\Lambda\le\beta_\Lambda,
   \qquad t_\Lambda\in\mathbb Z,
   \tag{0.7}
   \]

   where \(r_\Lambda\) is one elementary hypersimplex rectangle. Every
   admissible \(t_\Lambda\) is already realized by one matching.
   Repeated circulation gives no additional net capacity.

3. Globally, the exact reachable protected-row corrections are

   \[
   \boxed{
   \Delta_H=\sum_\Lambda t_\Lambda r_\Lambda,\qquad
   \Delta_h=0\quad(0\le h\le2H,\ h\ne H),}
   \tag{0.8}
   \]

   with the independent box constraints (0.7). In particular,

   \[
   \boxed{
   \frac12\|\Delta_H\|_1\le N
   =(1+o(1))\frac Wm.}
   \tag{0.9}
   \]

4. Singleton marginals are far from sufficient. There are two legal
   one-path-per-top tables whose middle-load difference is one elementary
   rectangle \(r\), so

   \[
   Ar=0,\qquad \|r\|_1=4,
   \tag{0.10}
   \]

   but which lie in different rectangle-transition components. Thus a
   universal same-marginal Hall theorem fails already at \(L^1=4\).

5. There is also a baseline-independent diffuse Hall cut. One can choose
   \(N\) pairwise support-disjoint rectangles and obtain

   \[
   Az=0,\qquad \|z\|_1=4N=o(W),
   \tag{0.11}
   \]

   while the exact independent-top Hall relaxation has capacity only
   \(N\). The deficiency is at least \(N\). Under the standard maximal
   \(H\)-calibration, the two shores may even be completed to
   collision-free \(0/1\) loads of total \(T\) with identical singleton
   marginals.

6. From the audited master-order table, every load of collision energy
   \(o(W)\) is at total-variation distance \((1-o(1))W\). Equation
   (0.9) therefore rules out a full low-collision correction by any
   rectangle-only chronology.

7. A small positive theorem survives. A prescribed signed list of fewer
   than

   \[
   \frac14\binom{m-2}{H-2}
   \tag{0.12}
   \]

   rectangles has a from-scratch installation on pairwise disjoint top
   pairs, with exactly zero protected-row collateral away from \(h=H\).
   This does not start from a prescribed table and is
   \(W^{o(1)}\), far below coefficient scale.

The exact deficient cut for the rectangle-only graph is therefore
local-component capacity, not lack of degree in the partner graph.
Quantitatively, the route which starts from the audited master baseline
needs average projected middle-deck radius \(\Omega(m)\) per top;
executing \(\Theta(m)\) moves inside the present two-state fibre does
nothing. An exact four-top
cyclic re-rooting with \(\Theta(m)\) sequential focal directions is
already proved in
MATH_THEOREM_L_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_LOCAL_REUSE_20260727.md.
Thus the next gate is global amortized packing of those recharges, with
their helper tops themselves reused, not construction of the local
recharge primitive.

No coefficient-one theorem is claimed.

## 1. Physical states and the certified involution

For a top \(U\in\binom{[2m]}M\), let

\[
 p=(p_1,\ldots,p_M)
\tag{1.1}
\]

be an injective word on \(U\). Retain the phase starts
\(1,\ldots,d\). At complementary length \(h\), its protected deck is

\[
 {\cal K}_h(U,p)
 =
 \sum_{i=1}^{d}
 e_{\,U\setminus\{p_i,p_{i+1},\ldots,p_{i+h-1}\}},
 \qquad 0\le h\le2H.
\tag{1.2}
\]

The middle row is \(h=H\). Define the boundary involution

\[
 \beta p=(p_2,p_1,p_3,\ldots,p_M).
\tag{1.3}
\]

Only the phase-\(2\) interval changes. Hence

\[
 {\cal K}_H(U,\beta p)-{\cal K}_H(U,p)
 =e_Y-e_X
\tag{1.4}
\]

for two Johnson-adjacent \(m\)-sets \(X,Y\). At other lengths the local
leg may have collateral, but the certified two-top macro pairs two such
legs so that their complete collateral cancels for every
\(h\ne H\).

### Lemma 1.1 (binary top orbit)

In every chronological sequence of certified two-top rectangles, the
state at a fixed top \(U\) alternates between \(p_U\) and
\(\beta p_U\). In particular,

\[
 \Sigma(U,p)
 =
 \bigl(U,\{p_1,p_2\},p_3,\ldots,p_M\bigr)
\tag{1.5}
\]

is invariant.

#### Proof

In the displayed two-top construction, both incident path replacements
interchange their first two letters and leave every later position
fixed. Coordinate relabelling changes the letters, not their physical
positions, and taking the inverse applies the same involution again.
Thus every incident move projects at \(U\) to the edge
\(\{p_U,\beta p_U\}\). Since \(\beta^2=1\), the claim follows.
\(\square\)

Let \(m_U^+\) count local traversals
\(p_U\to\beta p_U\), and let \(m_U^-\) count local traversals
\(\beta p_U\to p_U\); these are local orientations, not necessarily
the global names of the two rectangle shores. Their middle contribution
telescopes to

\[
 (m_U^+-m_U^-)
 \bigl({\cal K}_H(U,\beta p_U)-{\cal K}_H(U,p_U)\bigr),
\tag{1.6}
\]

where

\[
 m_U^+-m_U^-\in\{-1,0,1\}.
\tag{1.7}
\]

This is the first indication that chronological reuse cannot create
additional endpoint capacity.

## 2. Exact macro-class normal form

Fix once and for all a total order on the ground coordinates. For a
boundary orbit \(\{p,\beta p\}\), parse the physical positions as

\[
\begin{aligned}
 B&=\{p_1,p_2\}=\{a,b\},\qquad a<b,\\
 x&=p_3,\\
 F&=(p_4,\ldots,p_H),\\
 Z&=\{p_{H+1},p_{H+2}\}=\{z,z'\},\qquad z<z',\\
 \rho&=(p_{H+3},\ldots,p_M),\\
 R&=\{p_{H+3},\ldots,p_M\},\\
 G&=(p_{H+3},\ldots,p_{2H+1}).
\end{aligned}
\tag{2.1}
\]

When \(H=3\), \(F\) is empty. The underlying set \(R\) has size
\(m-2\), while the protected near-collar word \(G\) has length
\(H-1\). Define

\[
 \Lambda=(B,F,Z,R,G).
\tag{2.2}
\]

The coordinate \(x\) is the petal. The base underlying a class has
size \(M-1\), so its petal set has size

\[
 m-H+1.
\tag{2.3}
\]

Let \(\eta\in\{0,1\}\) record whether the landmark pair occurs as
\((z,z')\) or \((z',z)\), and let
\(\epsilon\in\{0,1\}\) record whether the first pair occurs as
\((a,b)\) or \((b,a)\). The residual order

\[
 \omega=(p_{2H+2},\ldots,p_M)
\tag{2.4}
\]

is a free vertex decoration. Write the corresponding state as

\[
 P_{\Lambda,x,\omega}^{\eta,\epsilon}.
\tag{2.5}
\]

The top itself is

\[
 U_{\Lambda,x}=B\cup\{x\}\cup F\cup Z\cup R.
\tag{2.6}
\]

Distinct petals give distinct tops.

### Lemma 2.1 (complete compatibility classification)

Two selected boundary orbits support one nonzero collar-neutral
first-two rectangle through the protected band if and only if they
have the same class \(\Lambda\), distinct petals, and opposite
\(\eta\)-values. Their residual decorations may differ. At a specified
table state, the move is installable if and only if their
\(\epsilon\)-values are opposite. In the orientation
\(00+11\to01+10\), it is exactly

\[
 P_{\Lambda,x,\omega}^{0,0}
 +P_{\Lambda,y,\omega'}^{1,1}
 \longrightarrow
 P_{\Lambda,x,\omega}^{0,1}
 +P_{\Lambda,y,\omega'}^{1,0}.
\tag{2.7}
\]

Consequently the partner graph induced by the selected top orbits in
one nontrivial class is complete bipartite between its two
\(\eta\)-shores.

#### Proof

For a word written

\[
 p=(u,v,c_1,c_2,\ldots,c_{M-2}),
\]

the derivative of the first-two swap at length \(h\ge2\) is

\[
 g_h(p)
 =e_{K_h\cup\{v\}}-e_{K_h\cup\{u\}},
 \qquad
 K_h=U\setminus\{u,v,c_1,\ldots,c_{h-1}\}.
\tag{2.8}
\]

Suppose two such derivatives cancel for every protected
\(h\ne H\). At \(h=2\), equality of the two opposite unit transfers
forces the same unordered boundary pair \(B\) and the same base
\(U\setminus\{c_1\}\); the two boundary orientations are opposite.
Equality successively at \(h=3,\ldots,H-1\) forces the ordered word

\[
 (c_2,\ldots,c_{H-2})=F
\]

to agree. Comparing the equal cores at \(h=H-1\) and \(h=H+1\)
forces the same unordered pair

\[
 Z=\{c_{H-1},c_H\}.
\]

If its order were also the same, the derivative at \(h=H\) would
cancel; nonzero middle action therefore forces the two orders of \(Z\)
to be opposite. Finally, equality successively for
\(h=H+2,\ldots,2H\) forces the ordered near-collar word

\[
 (c_{H+1},\ldots,c_{2H-1})=G
\]

to agree. The common base already fixes the underlying set \(R\) of
the remaining suffix. Its order after position \(2H+1\) is invisible
to every protected derivative and may differ. This proves necessity.

Conversely, common data \(\Lambda\), opposite \(\eta\), and opposite
\(\epsilon\) make the two vectors in (2.8) exact negatives for every
\(h\ne H\), independently of \(\omega,\omega'\). At \(h=H\),
reversing the landmark pair gives the nonzero rectangle computed in
(3.4). Thus the two physical first-two flips form an installable
collar-neutral rectangle. Distinct selected tops give distinct petals.
\(\square\)

In one one-path-per-top table, the selected vertices on the two
\(\eta\)-shores have disjoint petal sets: \((\Lambda,x)\) determines
the physical top \(U_{\Lambda,x}\), and only one orbit is selected
there. Hence the selected partner graph is genuinely complete
bipartite, not a complete bipartite graph with a forbidden diagonal.

If a prescribed terminal-core condition deletes some of these partner
edges, the partner graph becomes a subgraph. Token count remains an
invariant and all later capacity cuts remain true, but the exact
interval in Theorem 3.1 may shrink. The lemma does not include a
separately added reflected right-boundary swap or a generator that
changes a position \(p_j\) with \(j\ge3\).

## 3. The token-flow theorem

At a fixed class \(\Lambda\), let

\[
 n_{\eta\epsilon}=n_{\eta\epsilon}^{\Lambda}
\tag{3.1}
\]

be the current numbers of selected top orbits with state
\((\eta,\epsilon)\). A move swaps a \(0\)-coin and a \(1\)-coin across
one edge of the complete bipartite \(\eta\)-graph. Thus the total number
of \(\epsilon=1\) coins,

\[
 k_\Lambda=n_{01}+n_{11},
\tag{3.2}
\]

is invariant.

Put

\[
\begin{aligned}
 d_0&=
 e_{R\cup\{b,z'\}}-e_{R\cup\{a,z'\}},\\
 d_1&=
 e_{R\cup\{b,z\}}-e_{R\cup\{a,z\}},
\end{aligned}
\tag{3.3}
\]

the middle derivatives of the \(0\to1\) boundary flip on the two
\(\eta\)-shores. Their difference is

\[
\begin{aligned}
 r_\Lambda=d_0-d_1
 &=
 e_{R\cup\{a,z\}}+e_{R\cup\{b,z'\}}\\
 &\quad-e_{R\cup\{a,z'\}}-e_{R\cup\{b,z\}}.
\end{aligned}
\tag{3.4}
\]

It is an elementary rank-\(m\) rectangle and satisfies

\[
 Ar_\Lambda=0,\qquad \|r_\Lambda\|_1=4,
\tag{3.5}
\]

where \(A\) is the singleton-versus-middle-set incidence matrix.

### Theorem 3.1 (exact class reachability)

Define

\[
 \alpha_\Lambda=\min(n_{01},n_{10}),\qquad
 \beta_\Lambda=\min(n_{00},n_{11}).
\tag{3.6}
\]

The exact set of attainable middle corrections in class \(\Lambda\)
is

\[
 \boxed{
 \{t r_\Lambda:
 t\in\mathbb Z,\ -\alpha_\Lambda\le t\le\beta_\Lambda\}.}
\tag{3.7}
\]

Every correction in (3.7) is attained by one matching of disjoint top
pairs.

#### Proof

A forward move changes the count vector
\((n_{00},n_{01},n_{10},n_{11})\) by

\[
 (-1,+1,+1,-1)
\tag{3.8}
\]

and has middle action \(r_\Lambda\). Hence a net value \(t\) forces

\[
\begin{aligned}
 n'_{00}&=n_{00}-t,&
 n'_{01}&=n_{01}+t,\\
 n'_{10}&=n_{10}+t,&
 n'_{11}&=n_{11}-t.
\end{aligned}
\tag{3.9}
\]

Nonnegativity of these four counts gives exactly the interval in
(3.7).

Conversely, if \(t\ge0\), choose \(t\) current states from cell \(00\)
and \(t\) current states from cell \(11\), and pair them arbitrarily.
The partner graph is complete bipartite, so these \(t\) disjoint pairs
form one legal matching. If \(t<0\), pair \(-t\) states from cells
\(01\) and \(10\) and apply the reverse moves. The bounds (3.6) are
exactly what is needed. \(\square\)

### Corollary 3.2 (complete component invariants)

Fix the per-top boundary-orbit data
\((\Lambda,x,\omega,\eta)\). Within every nontrivial resulting
compatibility component, \(k_\Lambda\) is a complete invariant of the
remaining \(\epsilon\)-token configuration. If one \(\eta\)-shore is
empty, the individual \(\epsilon\)-coins on its isolated vertices are
invariants.

#### Proof

Legal moves are token slides on a connected complete bipartite graph.
We recall a proof that the \(k\)-token graph of every connected graph is
connected. Pass to a spanning tree and argue by induction on its number
of vertices. Let \(\ell\) be a leaf. If the initial and target
occupancies at \(\ell\) differ, locate the nearest hole when a token
must be moved away from \(\ell\), or the nearest token when one must be
moved toward \(\ell\). By nearestness, the internal vertices on the
unique path have the complementary occupancy, so successive legal
slides along that path give \(\ell\) its target occupancy. Freeze
\(\ell\), delete it, and apply induction to the remaining tree. Hence
two configurations with the same token count are connected. The
assertion for isolated vertices is immediate. \(\square\)

If one also adjoins protected-null pairs with the same \(\eta\) and
opposite \(\epsilon\), they merely slide tokens within one shore. They
leave the class counts in (3.9), and hence the attainable middle-action
interval, unchanged. They can merge zero-action physical states but
supply no additional rectangle capacity.

### Theorem 3.3 (exact global projected flow)

For a fixed initial one-path-per-top table, the exact corrections
reachable by certified collar-neutral rectangles are

\[
 \boxed{
 \Delta_H=\sum_\Lambda t_\Lambda r_\Lambda,\qquad
 -\alpha_\Lambda\le t_\Lambda\le\beta_\Lambda,\quad
 t_\Lambda\in\mathbb Z,}
\tag{3.10}
\]

and

\[
 \boxed{\Delta_h=0\qquad(0\le h\le2H,\ h\ne H).}
\tag{3.11}
\]

All choices of the \(t_\Lambda\)'s in (3.10) are simultaneously
installable in one round.

#### Proof

Lemma 1.1 freezes the class of every selected top orbit. Different
classes therefore use disjoint top sets. Apply Theorem 3.1 inside every
class and take the union of the resulting disjoint matchings. Every
individual macro is collar-neutral away from \(h=H\), proving
(3.11). \(\square\)

The exact fractional support function of (3.10) is

\[
 \boxed{
 \langle\phi,\Delta_H\rangle
 \le
 \sum_\Lambda
 \left[
 \beta_\Lambda\langle\phi,r_\Lambda\rangle_+
 +\alpha_\Lambda\langle-\phi,r_\Lambda\rangle_+
 \right]}
\tag{3.12}
\]

for every real target weight \(\phi\). Conversely, the family (3.12)
characterizes the real box image obtained by allowing real
\(t_\Lambda\)'s in their intervals. The bounded integer
representation (3.10), rather than (3.12) alone, is the exact integral
condition.

Each unit of \(|t_\Lambda|\) consumes two distinct tops. Consequently

\[
 2\sum_\Lambda|t_\Lambda|\le N,
\tag{3.13}
\]

and therefore

\[
 \boxed{
 \|\Delta_H\|_1
 \le4\sum_\Lambda|t_\Lambda|
 \le2N.}
\tag{3.14}
\]

This proves (0.9). It also proves that an arbitrarily long chronology
has exactly the net capacity of one matching round.

## 4. The exact independent-top Hall relaxation

There is a useful cut which does not require parsing the macro classes.
Fix the initial table \(P\). At every top \(U\), orient its binary
boundary fibre from \(P_U\) to \(\beta P_U\), and write

\[
 \delta_U
 =
 {\cal K}_H(U,\beta P_U)-{\cal K}_H(U,P_U)
 =e_{Y_U}-e_{X_U}.
\tag{4.1}
\]

Form a directed unit-capacity multigraph \(D_P\) on the middle target
layer with one arc

\[
 X_U\longrightarrow Y_U
\tag{4.2}
\]

for each top. Forget, temporarily, the requirement that selected top
toggles be paired into actual collar-neutral rectangles.

### Theorem 4.1 (Hoffman cut for independent top toggles)

An integral correction \(z\) is obtainable by independently toggling
some subset of the \(N\) top fibres if and only if

\[
 \sum_X z_X=0
\tag{4.3}
\]

and, for every target family \({\cal S}\),

\[
 \boxed{
 z({\cal S})
 \le
 c_P(\overline{\cal S},{\cal S}),}
\tag{4.4}
\]

where the right side is the number of arcs of \(D_P\) entering
\({\cal S}\).

Every actual rectangle correction satisfies (4.4).

#### Proof

Selecting top \(U\) is selecting its arc with a variable
\(f_U\in\{0,1\}\). With divergence defined as inflow minus outflow, the
required equation is

\[
 Bf=z,\qquad 0\le f\le1,
\tag{4.5}
\]

where \(B\) is the directed incidence matrix. Summing (4.5) on a
target family \({\cal S}\) gives

\[
 z({\cal S})
 =f(\overline{\cal S},{\cal S})
  -f({\cal S},\overline{\cal S})
 \le c_P(\overline{\cal S},{\cal S}),
\]

proving necessity. Conversely, (4.3)--(4.4), together with the same
inequality for complements, are the capacitated circulation cuts for
(4.5). Hoffman's circulation theorem gives a real solution. Directed
incidence matrices are totally unimodular, so integral \(z\) and
integral capacities give an integral solution \(f\).

An actual rectangle sequence toggles only a subset of these same top
fibres, so its correction belongs to this relaxation. \(\square\)

Equivalently, the relaxed polytope is the zonotope

\[
 {\cal Z}(P)=\sum_U[0,\delta_U],
\tag{4.6}
\]

with exact dual description

\[
 \boxed{
 \langle\phi,z\rangle
 \le
 \sum_U
 \max\{0,\phi(Y_U)-\phi(X_U)\}}
\tag{4.7}
\]

for every real \(\phi\). Macro compatibility and the class coin
invariants shrink (4.6); they never enlarge it.

## 5. Two exact deficient cuts

### 5.1 A physical \(L^1=4\) component obstruction

The component invariant can fail even when both endpoints are literal
one-path-per-top tables.

Choose two distinct macro classes with the same unordered first pair

\[
 B=\{a,b\},
\]

the same filler \(F\), the same landmark set \(Z=\{z,z'\}\), and the
same underlying suffix set \(R\), but two distinct protected
near-collar orders \(G\ne G'\) of the same \((H-1)\)-subset of \(R\).
Such orders exist because \(H-1\ge2\). These classes have the same
middle rectangle \(r\) in (3.4), but no compatibility edge joins them.

Choose distinct petals \(x\ne y\). Take one \(\eta=0\) top orbit with
petal \(x\) in the first class and orient its first pair with
\(\epsilon=0\). Take one \(\eta=1\) top orbit with petal \(y\) in the
second class and orient its first pair with \(\epsilon=1\). Extend
\(\epsilon=0\) constantly throughout the first selected class and
\(\epsilon=1\) constantly throughout the second. Choose one constant
\(\epsilon\)-value in every other selected class. The resulting table
\(P\) has no installable rectangle: every compatible class has only one
coin value.

Now flip the first selected word from \(\epsilon=0\) to \(1\), and the
second from \(\epsilon=1\) to \(0\), leaving every other top unchanged.
This gives another literal one-path-per-top table \(Q\). Its middle
difference is

\[
 {\cal K}_H(Q)-{\cal K}_H(P)
 =d_0-d_1=r,
\tag{5.1}
\]

so

\[
 Ar=0,\qquad \|r\|_1=4.
\tag{5.2}
\]

Nevertheless \(P\) is isolated in the certified rectangle graph, and
the two flips change the conserved coin count in their two separate
classes. Thus \(Q\) is unreachable. The other protected rows of \(P\)
and \(Q\) need not agree; the point is that a same-marginal middle
correction does not determine rectangle-component membership.

### 5.2 A diffuse Hall deficiency of order \(N\)

Fix four distinct coordinates \(a,b,z,z'\). For

\[
 R\in
 \binom{[2m]\setminus\{a,b,z,z'\}}{m-2},
\]

put

\[
 \rho_R=
 e_{R\cup\{a,z\}}+e_{R\cup\{b,z'\}}
 -e_{R\cup\{a,z'\}}-e_{R\cup\{b,z\}}.
\tag{5.3}
\]

Different \(R\)'s give disjoint four-point supports, and

\[
 A\rho_R=0.
\tag{5.4}
\]

Moreover,

\[
 \frac{\binom{2m-4}{m-2}}{W}
 =
 \frac{m^2(m-1)^2}
 {(2m)(2m-1)(2m-2)(2m-3)}
 \longrightarrow\frac1{16},
\tag{5.5}
\]

whereas \(N=(1+o(1))W/m\). Hence, for all sufficiently large \(m\),
choose \(N\) distinct cores \(R\) and put

\[
 z=\sum_R\rho_R.
\tag{5.6}
\]

Then

\[
 Az=0,\qquad
 \|z\|_1=4N=o(W),
\tag{5.7}
\]

and both \(z^+\) and \(z^-\) are \(0/1\) loads of mass \(2N\).

Let

\[
 {\cal S}=\operatorname{supp}(z^+).
\]

For every initial table,

\[
 z({\cal S})=2N,
\tag{5.8}
\]

but \(D_P\) has only \(N\) arcs in total, so

\[
 c_P(\overline{\cal S},{\cal S})\le N.
\tag{5.9}
\]

Thus (4.4) has deficiency at least \(N\). The correction fails even in
the independent-top relaxation and therefore cannot be installed by
collar-neutral rectangles.

This refutes an arbitrary same-singleton-marginal correction theorem at
the requested \(o(W)\) scale, with completely diffuse positive and
negative shores.

Under the standard maximal-\(H\) calibration, let
\(\lambda=W/N\). Failure of the defining height inequality at \(H+1\)
gives

\[
 \lambda>m-H.
\tag{5.10}
\]

Since \(T=dN\),

\[
 W-T=(\lambda-d)N>(2H-1)N>2N.
\tag{5.11}
\]

Consequently there are at least \(T-2N\) middle targets outside the
\(4N\) points in (5.6). Choose a common \(0/1\) background \(C\) of
that size and set

\[
 K={\bf1}_C+z^-,
 \qquad
 L={\bf1}_C+z^+.
\tag{5.12}
\]

Then \(K,L\) are collision-free \(0/1\) loads of total \(T\), have
identical singleton marginals, and satisfy \(L-K=z\). They need not
themselves be physical one-path-per-top coefficients; (5.12) rules out
the proposed arbitrary-load correction theorem, while Section 5.1
already gives physical endpoint tables in different components.

## 6. The full low-collision target is outside the component

Let \(K_{\rm mast}\) be the middle load of the audited master-order
table. It has total mass

\[
 T=(1-o(1))W
\tag{6.1}
\]

and is supported on a family \({\cal A}_{\rm mast}\) satisfying

\[
 |{\cal A}_{\rm mast}|
 \le2m\,2^{-H}W=o(W).
\tag{6.2}
\]

For any nonnegative integer load \(L\) of mass \(T\), define

\[
 \Psi(L)=\sum_D\binom{L_D}{2}.
\tag{6.3}
\]

Since

\[
 (L_D-1)_+\le\binom{L_D}{2},
\]

every \(L\) with \(\Psi(L)=o(W)\) has

\[
 \sum_{D\in{\cal A}_{\rm mast}}L_D
 \le|{\cal A}_{\rm mast}|+\Psi(L)=o(W).
\tag{6.4}
\]

Therefore

\[
 \frac12\|K_{\rm mast}-L\|_1
 \ge
 \sum_{D\notin{\cal A}_{\rm mast}}L_D
 =T-o(W)
 =(1-o(1))W.
\tag{6.5}
\]

Indeed the outside contribution to the \(L^1\)-distance is the
displayed mass of \(L\), while equality of the two total masses forces
the inside contribution to be at least the same amount.

But Theorem 3.3 bounds the total-variation radius of the complete
rectangle component by \(N=(1+o(1))W/m=o(W)\). Hence:

### Theorem 6.1 (rectangle-only full-target obstruction)

No chronological sequence of certified collar-neutral two-top
rectangles takes the master-order table to a table with
\(\Psi=o(W)\).

The obstruction is endpoint-state capacity. It is unaffected by
partner-graph expansion, by using \(\Theta(m)\) different partners at
each top, or by arbitrarily long rectangle circulation.

## 7. A positive sparse matching theorem

The preceding results concern a prescribed initial table. From scratch,
a short signed rectangle list can be installed on fresh tops.

Fix one requested rectangle \(\rho_R\) as in (5.3), and put

\[
 S=R\cup\{a,b,z,z'\},
 \qquad |S|=m+2.
\tag{7.1}
\]

A candidate top has the form

\[
 U=S\cup K,\qquad
 K\in\binom{[2m]\setminus S}{H-2}.
\tag{7.2}
\]

Two candidate tops form the required literal macro exactly when their
\((H-2)\)-sets \(K,K'\) are Johnson adjacent. Hence the candidate
top-pair graph is

\[
 J(m-2,H-2).
\tag{7.3}
\]

It has

\[
 B_m=\binom{m-2}{H-2}
\tag{7.4}
\]

vertices, degree

\[
 \Delta_m=(H-2)(m-H),
\tag{7.5}
\]

and \(B_m\Delta_m/2\) edges.

### Theorem 7.1 (fresh-top rectangle packing)

Let

\[
 \rho_1,\ldots,\rho_k
\tag{7.6}
\]

be any signed list of elementary rank-\(m\) rectangles. If

\[
 k-1<\frac{B_m}{4},
\tag{7.7}
\]

there are two literal one-path-per-top tables \(P,Q\) such that

\[
 {\cal K}_H(Q)-{\cal K}_H(P)
 =\sum_{j=1}^k\rho_j
\tag{7.8}
\]

and

\[
 {\cal K}_h(Q)={\cal K}_h(P)
 \qquad(0\le h\le2H,\ h\ne H).
\tag{7.9}
\]

The \(k\) macros use pairwise disjoint top pairs.

#### Proof

Proceed greedily through the requested list. Before request \(j\), at
most \(2(j-1)\) physical tops have been used. In the candidate graph
for \(\rho_j\), each blocked top destroys at most
\(\Delta_m\) candidate edges. Thus fewer than

\[
 2(j-1)\Delta_m
 <
 \frac{B_m\Delta_m}{2}
\]

edges are blocked. At least one candidate top pair remains.

Choose it, write the common \((H-3)\)-set as
\(F=K\cap K'\), and use the two exchanged coordinates as the petals
\(x,y\). The explicit two-top construction installs the requested
orientation of \(\rho_j\). Since all chosen tops are distinct, the
macros coexist. Put identical arbitrary path states on every unused top.
Summing their exact deck identities proves (7.8)--(7.9).
\(\square\)

In the Gaussian regime,

\[
 \log B_m=o(m),\qquad B_m=W^{o(1)}\ll N.
\tag{7.10}
\]

Thus Theorem 7.1 is a genuine integral matching theorem but is much too
small for coefficient one. It also constructs both endpoint tables
from scratch; it does not repair a prescribed baseline.

## 8. The necessary scale of an escape

The endpoint-capacity argument extends to every move library which acts
on the same fixed set of physical tops and retains exactly one path state
at every top throughout.

For each top \(U\), project all allowed global moves to a graph
\({\cal G}_U\) on its physical path states. Fix an initial state
\(p_U\), and let \({\cal C}_U(p_U)\) be its projected component. Define
its middle-deck radius

\[
 b_U=
 \max_{q\in{\cal C}_U(p_U)}
 \frac12
 \|{\cal K}_H(U,q)-{\cal K}_H(U,p_U)\|_1.
\tag{8.1}
\]

### Theorem 8.1 (projected-component cut)

Every chronological endpoint correction \(z\) generated by such a move
library satisfies

\[
 \boxed{
 \frac12\|z\|_1\le\sum_U b_U.}
\tag{8.2}
\]

#### Proof

The final state at top \(U\) lies in
\({\cal C}_U(p_U)\). The global middle load is the sum of the top decks.
Therefore the triangle inequality gives

\[
\begin{aligned}
 \frac12\|z\|_1
 &\le
 \sum_U
 \frac12
 \|{\cal K}_H(U,p_U^{\rm fin})
       -{\cal K}_H(U,p_U)\|_1\\
 &\le\sum_Ub_U.
\end{aligned}
\]

\(\square\)

For the certified left-boundary rectangle library, \(b_U\le1\). If
only its reflected right-boundary copy is added, the two disjoint
boundary involutions give \(b_U\le2\). Neither reaches coefficient
scale.

Combining (6.5) and (8.2), any library which repairs the master state to
\(\Psi=o(W)\) must satisfy

\[
 \sum_Ub_U\ge(1-o(1))W.
\tag{8.3}
\]

Since \(N=(1+o(1))W/m\), its average projected top-component radius must
be

\[
 \boxed{
 \frac1N\sum_Ub_U\ge(1-o(1))m.}
\tag{8.4}
\]

This is the precise global capacity requirement. The known four-top
recharge meets it at the projected local level, as follows.

### Theorem 8.2 (re-rooting saturates the local radius)

Enlarge the projected move library by the exact four-top cyclic
re-rooting from
MATH_THEOREM_L_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_LOCAL_REUSE_20260727.md.
Then, at every top \(U\) and every initial word \(p\),

\[
 \boxed{b_U=d=m-3H+1=(1-o(1))m.}
\tag{8.5}
\]

#### Proof

The rectangle supplies the projected edge

\[
 p\longleftrightarrow sp,
 \qquad s=(1\ 2),
\]

for every word \(p\). The arbitrary-word recharge supplies

\[
 p\longleftrightarrow rp,
\]

where \(r\) is the one-step cyclic position rotation. The \(M\)-cycle
\(r\) and the adjacent transposition \(s\) generate \(S_M\), since the
conjugates \(r^jsr^{-j}\) give all cyclically adjacent
transpositions. Thus the projected component contains every ordering
of the alphabet \(U\).

Let

\[
 {\cal J}(p)
 =
 \bigl\{\{p_i,\ldots,p_{i+H-1}\}:1\le i\le d\bigr\}
\]

be the \(d\) distinct deleted \(H\)-windows. For a uniformly random
coordinate permutation \(\sigma\in S_U\),

\[
 {\mathbb E}
 |{\cal J}(p)\cap\sigma{\cal J}(p)|
 ={d^2\over\binom MH}<1
\tag{8.6}
\]

for all sufficiently large \(m\). Hence some \(\sigma\) makes the two
window decks disjoint. Complementation inside \(U\) makes the
corresponding middle decks disjoint as well, so their \(L^1\)-distance
is \(2d\). Therefore \(b_U\ge d\). The reverse inequality is trivial
because every deck is a simple load of mass \(d\). \(\square\)

Thus the local radius obstruction for the master-baseline recharge route
is already overcome. The present
literal installation of one focal direction, however, uses three fresh
recharge helpers and one fresh rectangle companion. Applied
independently, it gives only constant average reuse over all consumed
tops, not the simultaneous global endpoint promised by the projected
group. High degree between the binary fibres alone cannot help; the live
gate is global packing which recycles those helper tops as later focal
tops while preserving the collar and tag interfaces.

## 9. Audited implication boundary

Proved:

1. the exact macro-class compatibility graph;
2. complete token-count component invariants;
3. the exact integral reachable box (3.10);
4. the exact independent-top Hoffman cut (4.4);
5. a physical \(L^1=4\) same-marginal component obstruction;
6. a diffuse \(o(W)\) Hall deficiency of order \(N\);
7. impossibility of the full low-collision repair from the master state;
8. a fresh-top integral packing theorem through
   \(k<B_m/4\);
9. the universal projected-component capacity inequality (8.2); and
10. saturation \(b_U=d\) of the local projected radius after the known
    four-top re-rooting is included.

Not proved:

1. a global packing/flow of the known four-top recharges in which helper
   tops are themselves reused and one globally liftable chronology
   realizes \(\Theta(m)\) net middle-deck displacement per top on
   average;
2. a matching theorem for rectangles interleaved with that recharge
   flow;
3. a prescribed-baseline lift even at the fresh-top scale;
4. owner simplicity or common nested stopping tags for the from-scratch
   endpoint tables in Theorem 7.1; or
5. coefficient one.

Thus the rectangle-only global flow is completely characterized and is
insufficient. The formal zero-marginal rectangle lattice is not the
physical transition component. For the audited master-baseline
rectangle/recharge route, the shortest viable continuation is not
stronger expansion of the two-top partner graph, nor construction of a
new local recharge already supplied by the four-top theorem. It is an
amortized global reuse theorem for the known recharge helpers, together
with the resulting charged rectangle matching and common tag interface.
This does not impose the same radius requirement on an unrelated
from-scratch construction or on a different baseline already at
sublinear total-variation distance from low collision.
