# Exterior-context Latin gauges and an exact diagonal collar braid

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact result and boundary

This note separates two superficially similar uses of a nonlocal
Dyck-word hash.

First, a filling-dependent permutation of a **complete stationary exterior
context fibre** is gauge-trivial. Suppose a recursive Chung--Feller segment
lives on a fixed coordinate block \(J\), every phase step is already a
Johnson step inside \(J\), and every local row is replicated in every
exterior context. Literal adjacency forces the exterior context to be
constant along the row. Permuting all exterior copies by an arbitrary
function of the filling merely renames those copies. It changes neither
the physical row multiset nor any lower-intersection or upper-union load.

Second, the exact geodesic displacement law

\[
 |O_L\setminus O_R|=d_J(P,P')                         \tag{0.1}
\]

is attainable by a literal integral braid. On a physical orientation
block \(Q_{r+d}\), a mask \(a\in\mathbb F_2^d\) replaces precisely the
inner exchanges indexed by \(\operatorname{supp}a\) with exterior
exchanges. The block splits into \(2^d\) disjoint active \(Q_r\)-facets;
an arbitrary exact isometric \(C_{2r}\)-factor can be installed separately
in every facet. Every middle owner and every selected adjacent-union token
is owned once. A half-cycle has boundary monodromy

\[
 (x,z,y)\longmapsto
 (x+a,z+\mathbf1+a,y+\mathbf1),                       \tag{0.2}
\]

and is a geodesic from

\[
 O_x\cup P_{z,y}\quad\hbox{to}\quad
 O_{x+a}\cup\bigl(J\setminus P_{z+a,y}\bigr).         \tag{0.3}
\]

The target of a window swallowing that half-cycle is

\[
 K\cup\{e_i^{x_i}:a_i=0\}
   \cup\{h_i^{z_i}:a_i=1\}.                           \tag{0.4}
\]

Thus there are exactly \(2^d\) physical swallowed targets, each of
multiplicity \(2^r\). The raw cap-\(b\) excess is exactly

\[
                    2^d(2^r-b)_+.                    \tag{0.5}
\]

There is also a genuinely filling-dependent version. Any partition of
\(\mathbb F_2^d\) into coordinate subcubes defines a stable mask
\(a(z)\); the corresponding active \(Q_r\)-cells are equal or disjoint
and cover \(Q_{r+d}\). This is the exact Latin/cocycle condition for this
diagonal-frame class.

For \(r=2d\), the local roots can be the explicit Dyck words obtained by
independently choosing \(1100\) or \(1010\) in each four-letter block.
Taking \(a=\mathbf1\) makes (0.4) recover every filling bit, and the exact
cycle factor in the \(z\)-facet may depend on an arbitrary nonlocal hash
of \(z\).

This is a genuine exterior-moving, hash-dependent, integral collar
packet. It is not yet a global MSW/Chung--Feller factor. It lacks a global
Dyck phase-zero transversal, all Chung--Feller phase bijections, and the
complete global adjacent-union palette. Promoting it requires a
parent-crossing packing whose full \(X/Y\) owner overlay closes. Section 7
gives the exact binary reciprocal-overlay condition. Thus this note gives
a literal positive local compiler and a sharp obstruction to the
stationary-context proposal, but does not claim coefficient one.

## 1. Stationary product cylinders

Let \(E,J\) be disjoint coordinate sets. Let \(\mathcal C\) be a finite
set of exterior contexts and let

\[
 O:\mathcal C\longrightarrow {E\choose k}
\]

be injective. Let \(U\) be a finite row set. For
\(0\le t\le s\), let

\[
 L_t:U\longrightarrow {J\choose r}
\]

be a local phase chart. Assume consecutive phase families are disjoint:

\[
 L_t(U)\cap L_{t+1}(U)=\varnothing.                   \tag{1.1}
\]

This holds for distinct Chung--Feller flaw layers. Choose maps
\(p_t:U\to U\) and filling-dependent exterior maps

\[
 \gamma_{t,u}:\mathcal C\longrightarrow\mathcal C.
\]

The proposed product-cylinder twist is

\[
 Z_t(c,u)=O_{\gamma_{t,u}(c)}\mathbin{\dot\cup}
                       L_t(p_tu).                     \tag{1.2}
\]

### Lemma 1.1 (phasewise context Latin condition)

Suppose \(p_t\in\operatorname{Sym}(U)\). If every
\(\gamma_{t,u}\in\operatorname{Sym}(\mathcal C)\), then

\[
 (c,u)\longmapsto(\gamma_{t,u}(c),p_tu)               \tag{1.3}
\]

is a bijection of \(\mathcal C\times U\). Hence (1.2) owns every state
of the phase-\(t\) product layer exactly once.

Conversely, if (1.3) is bijective and \(p_t\) depends only on \(u\), then
\(p_t\) and every \(\gamma_{t,u}\) are permutations.

#### Proof

Under the stated hypotheses, the inverse sends \((c',u')\) to

\[
 \left(\gamma_{t,p_t^{-1}u'}^{-1}(c'),p_t^{-1}u'\right).
\]

Conversely, the second coordinate of the bijection has every fibre of
size \(|\mathcal C|\), so \(p_t\) is bijective. On the unique source
fibre indexed by \(u=p_t^{-1}u'\), the first coordinate must map
\(\mathcal C\) bijectively to itself. \(\square\)

For a transitive group action one may put

\[
                  \gamma_{t,u}(c)=g_t(u)c.            \tag{1.4}
\]

Thus the lower Latin equations alone allow arbitrary filling-dependent
group elements. Literal chronology removes precisely this freedom.

## 2. Full-fibre gauge triviality

For equal-size sets on disjoint blocks, Johnson distance is additive:

\[
 d_J(A_E\cup A_J,B_E\cup B_J)
   =d_J(A_E,B_E)+d_J(A_J,B_J).                        \tag{2.1}
\]

### Theorem 2.1 (stationary-context chronology obstruction)

Assume (1.1), and suppose every consecutive pair in (1.2) is a Johnson
edge:

\[
                  d_J(Z_t(c,u),Z_{t+1}(c,u))=1.       \tag{2.2}
\]

Then, for every \(c,u,t\),

\[
 O_{\gamma_{t,u}(c)}=O_{\gamma_{t+1,u}(c)},           \tag{2.3}
\]

and

\[
 d_J(L_t(p_tu),L_{t+1}(p_{t+1}u))=1.                 \tag{2.4}
\]

Since \(O\) is injective,

\[
                  \gamma_{t,u}(c)=\gamma_{t+1,u}(c). \tag{2.5}
\]

Thus \(\gamma_{t,u}\) is independent of phase along every row.

#### Proof

By (1.1), the local sets are unequal, so their Johnson distance is at
least one. Additivity (2.1) and total distance one force local distance
one and exterior distance zero. This proves (2.3)--(2.5). \(\square\)

### Corollary 2.2 (complete stationary fibres are pure gauge)

Assume every local twisted row

\[
 R_u=(L_0(p_0u),\ldots,L_s(p_su))
\]

is replicated over the complete context set \(\mathcal C\), and let
\(\gamma_u\in\operatorname{Sym}(\mathcal C)\) be phase-independent. Then

\[
 \{(O_{\gamma_u(c)},R_u):c\in\mathcal C\}
 =\{(O_c,R_u):c\in\mathcal C\}                       \tag{2.6}
\]

as physical row multisets. Every lower-intersection and upper-union
target multiset is unchanged.

#### Proof

Equation (2.6) is invariance of a complete finite set under a
permutation. A stationary exterior set occurs in every state, so every
target has the form

\[
                   O_c\mathbin{\dot\cup}T(R_u).       \tag{2.7}
\]

Permuting \(c\) leaves that physical multiset unchanged. \(\square\)

For a faithful transitive action, (2.5) says
\(g_t(u)=g_{t+1}(u)\). A complete mapping, orthomorphism, or Latin square
used only to choose \(g(u)\) is therefore merely a row reindexing.

## 3. The exact displacement cocycle

Let \(|J|=2r\), let \(P,P'\in{J\choose r}\), and let
\(O_L,O_R\subseteq E\) have the same size. Consider a length-\(r\)
Johnson path from

\[
                  S=O_L\mathbin{\dot\cup}P
\]

to

\[
                  T=O_R\mathbin{\dot\cup}(J\setminus P').
\]

### Theorem 3.1 (endpoint distance law)

Such a path is geodesic only if

\[
 \boxed{|O_L\setminus O_R|=d_J(P,P').}               \tag{3.1}
\]

Conversely, if (3.1) holds, a length-\(r\) geodesic exists. For every
such geodesic, the target of a window swallowing the whole excursion is

\[
 \boxed{S\cap T=(O_L\cap O_R)\mathbin{\dot\cup}(P\setminus P').}
                                                               \tag{3.2}
\]

#### Proof

Disjointness of \(E,J\) gives

\[
\begin{aligned}
 d_J(S,T)
 &=|S\setminus T|\\
 &=|O_L\setminus O_R|+|P\cap P'|\\
 &=|O_L\setminus O_R|+r-d_J(P,P').                  \tag{3.3}
\end{aligned}
\]

A length-\(r\) path is geodesic exactly when (3.3) equals \(r\), proving
(3.1). Conversely, under (3.1), matching the \(r\) coordinates of
\(S\setminus T\) with those of \(T\setminus S\) gives a geodesic.

A shortest set path never removes a coordinate of \(S\cap T\) or inserts
one outside \(S\cup T\). Hence its full intersection is \(S\cap T\), and
direct intersection of the endpoints gives (3.2). \(\square\)

Equation (3.1) is the collar cocycle: a fixed exterior forces \(P=P'\),
while nontrivial local monodromy is possible if paid for by equal exterior
displacement.

## 4. An exact diagonal exterior-moving braid

Fix \(0\le d\le r\). Take pairwise disjoint coordinate pairs

\[
 E_i=\{e_i^0,e_i^1\},\quad
 H_i=\{h_i^0,h_i^1\}\quad(1\le i\le d),              \tag{4.1}
\]

and

\[
 A_j=\{a_j^0,a_j^1\}\quad(1\le j\le r-d).            \tag{4.2}
\]

Let \(K\) be fixed and disjoint from these coordinates. The owner block is

\[
 V(x,z,y)=K
  \cup\{e_i^{x_i}:1\le i\le d\}
  \cup\{h_i^{z_i}:1\le i\le d\}
  \cup\{a_j^{y_j}:1\le j\le r-d\},                   \tag{4.3}
\]

where

\[
 (x,z,y)\in\mathbb F_2^d\times\mathbb F_2^d
                     \times\mathbb F_2^{r-d}.
\]

Thus (4.3) is a literal \(Q_{r+d}\) orientation cell. Fix a mask
\(a\in\mathbb F_2^d\). Declare active the \(r\) pair axes

\[
 \mathcal A_a=
   \{E_i:a_i=1\}
   \cup\{H_i:a_i=0\}
   \cup\{A_j:1\le j\le r-d\}.                        \tag{4.4}
\]

The inactive axes are

\[
 \mathcal I_a=
   \{E_i:a_i=0\}\cup\{H_i:a_i=1\},                   \tag{4.5}
\]

and \(|\mathcal I_a|=d\). Fixing their orientations partitions the block
into \(2^d\) disjoint \(Q_r\)-facets.

Assume an exact factor \(\mathcal F_r\) of \(Q_r\) into isometric
\(C_{2r}\)-cycles is available. Install any coordinate/order conjugate of
\(\mathcal F_r\) in each facet, independently between facets.

### Theorem 4.1 (exact braid packet)

The union of these facet factors has the following properties.

1. Every owner (4.3) lies on exactly one cycle.
2. Every selected adjacent-union token lies on exactly one alternating
   cycle edge.
3. Every block of at most \(r\) consecutive transitions is a literal
   Johnson geodesic with distinct physical pair directions.
4. After \(r\) consecutive transitions,

   \[
   (x,z,y)\longmapsto
       (x+a,z+\mathbf1+a,y+\mathbf1).                \tag{4.6}
   \]

5. Every depth-\(r\) lower target in the facet labelled by its inactive
   orientations is

   \[
   \Phi_a(x,z)=K
     \cup\{e_i^{x_i}:a_i=0\}
     \cup\{h_i^{z_i}:a_i=1\}.                       \tag{4.7}
   \]

   There are \(2^d\) distinct targets, each of multiplicity \(2^r\).

#### Proof

The facets are disjoint and exhaustive, proving lower ownership.

An adjacent-union token of an orientation-cube edge contains both
endpoints of its changed pair and one endpoint of every other pair. It
therefore identifies its changed pair and then the underlying undirected
cube edge. Distinct cycle edges give distinct upper tokens. A cycle
factor uses a selected edge only once, and different facets have different
inactive orientations. This proves assertion 2.

On an isometric \(C_{2r}\), every \(r\) consecutive directions are the
\(r\) active directions once each. Hence every such segment is geodesic,
and its antipode toggles exactly (4.4), giving (4.6).

Across a half-cycle every active pair takes both orientations, so neither
endpoint survives the full intersection. Every inactive pair is constant
and contributes its selected endpoint. This is (4.7). There are \(2^d\)
inactive labels, and each facet has \(2^r\) based vertices. \(\square\)

### Corollary 4.2 (exact cap and trace ledgers)

At depth \(r\), the raw cap-\(b\) excess is

\[
 \boxed{\sum_T(\mu_r(T)-b)_+=2^d(2^r-b)_+.}           \tag{4.8}
\]

If \(\mathcal F_r\) has injective signed traces through depth \(H<r\),
then the entire \(Q_{r+d}\) braid block has injective signed traces
through \(H\).

#### Proof

The first assertion is Theorem 4.1(5). Traces in one facet are distinct
by hypothesis; traces in different facets contain different inactive
physical endpoints, for both intersections and unions. \(\square\)

In particular, \(r\le\lfloor\log_2b\rfloor\) eliminates this packet's
depth-\(r\) raw excess exactly.

## 5. Filling-dependent masks

Call

\[
 \mathscr P=\{(S_\lambda,b_\lambda):\lambda\in\Lambda\},
 \quad S_\lambda\subseteq[d],\quad
 b_\lambda\in\mathbb F_2^{S_\lambda}                 \tag{5.1}
\]

a subcube partition if the cylinders

\[
 Q_\lambda=\{z\in\mathbb F_2^d:z|_{S_\lambda}=b_\lambda\}       \tag{5.2}
\]

are pairwise disjoint and cover \(\mathbb F_2^d\). Define

\[
                    a(z)=\mathbf1_{S_\lambda}
                 \quad(z\in Q_\lambda).              \tag{5.3}
\]

### Theorem 5.1 (subcube-addressed diagonal braid)

For \(z\in Q_\lambda\), assign the active axes

\[
 \{E_i:i\in S_\lambda\}
 \cup\{H_i:i\notin S_\lambda\}
 \cup\{A_j:1\le j\le r-d\}.                          \tag{5.4}
\]

The selected active cells are equal or disjoint and partition the owner
block. There are exactly \(2^d\) of them, each is a physical \(Q_r\), and
arbitrary exact isometric \(C_{2r}\)-factors may be chosen independently.
The half-cycle endpoint and swallowed target are

\[
 (x,z,y)\longmapsto
  (x+a(z),z+\mathbf1+a(z),y+\mathbf1),                \tag{5.5}
\]

and

\[
 \Phi(x,z)=K
 \cup\{e_i^{x_i}:i\notin S_\lambda\}
 \cup\{h_i^{z_i}:i\in S_\lambda\}.                   \tag{5.6}
\]

Again there are exactly \(2^d\) distinct targets, each of multiplicity
\(2^r\), and (4.8) holds. Moreover,

\[
                  \tau(z)=z+a(z)                    \tag{5.7}
\]

is a permutation of \(\mathbb F_2^d\). Consequently the boundary map

\[
                  (x,z)\longmapsto(x+a(z),\tau(z))   \tag{5.8}
\]

is a bijection. Thus both left and right port labels are owned once
before any global Chung--Feller phase claim is invoked.

#### Proof

Fix \(\lambda\) and \(x|_{S_\lambda^c}\). Freeze

\[
 z|_{S_\lambda}=b_\lambda,\qquad x|_{S_\lambda^c},  \tag{5.9}
\]

and free \(x|_{S_\lambda}\), \(z|_{S_\lambda^c}\), and all \(y\).
These are respectively \(|S_\lambda|\),
\(d-|S_\lambda|\), and \(r-d\) bits, hence form a \(Q_r\).
Throughout this cell, \(z\) remains in \(Q_\lambda\), so its selected
mask is stable.

Every owner determines a unique \(\lambda\) and frozen exterior label,
so the cells are disjoint and exhaustive. Their number is

\[
 \sum_{\lambda}2^{d-|S_\lambda|}
 =\sum_\lambda|Q_\lambda|=2^d.                       \tag{5.10}
\]

Theorem 4.1 applies cellwise and gives (5.5)--(5.6). Targets from
different cells are distinct: each target records whether its \(i\)-th
endpoint comes from physical pair \(E_i\) or \(H_i\), recovering
\(S_\lambda\), and then records all bits in (5.9).

The same separation proves the cross-cell upper ledger. If two cells have
the same leaf \(\lambda\) but different frozen exterior labels, some
\(E_i\), \(i\notin S_\lambda\), is inactive in both cells with opposite
orientations. If they have distinct leaves \(\lambda,\mu\), disjointness
of the coordinate cylinders means that some
\(i\in S_\lambda\cap S_\mu\) has
\((b_\lambda)_i\ne(b_\mu)_i\). Then \(H_i\) is inactive in both cells
with opposite orientations. In either case, that inactive physical
endpoint persists in every lower state and every adjacent union, so no
lower or upper token from the two cells can coincide.

It remains to verify the asserted port bijection. On \(Q_\lambda\),
\(\tau\) maps

\[
 \{z:z|_{S_\lambda}=b_\lambda\}
 \quad\hbox{onto}\quad
 \{w:w|_{S_\lambda}=b_\lambda+\mathbf1\}.            \tag{5.11}
\]

Two original cylinders are disjoint exactly because some coordinate
fixed by both receives opposite prescribed bits. Complementing both
prescribed bits at every common fixed coordinate preserves that
opposition. Hence the image cylinders in (5.11) are pairwise disjoint.
Their cardinalities sum to \(2^d\), so they also cover the cube and
\(\tau\) is bijective. Given the output of (5.8), first invert
\(\tau\) to recover \(z\), and then translate by \(a(z)\) to recover
\(x\). This proves the final assertions. \(\square\)

The stability equation behind this theorem is exact. If an arbitrary
mask \(a(z)\) is to remain fixed throughout its selected active cell,
then necessarily

\[
 a(z')=a(z)\quad\text{whenever}\quad
 z'|_{\operatorname{supp}a(z)}
       =z|_{\operatorname{supp}a(z)}.                \tag{5.12}
\]

Indeed, precisely the coordinates outside \(\operatorname{supp}a(z)\)
are free inner axes. Condition (5.12) is also sufficient: its distinct
level cylinders are equal or disjoint and give the subcube partition.
Thus (5.12) is the exact cocycle/Latin condition in this diagonal-frame
class.

### Corollary 5.2 (explicit carry and dense-motion systems)

Two nonconstant all-\(d\) families are available.

1. Order the bits from least to most significant. For
   \(1\le j<d\), take the cylinder

   \[
   z_1=\cdots=z_{j-1}=1,\qquad z_j=0,
   \]

   with \(S=[j]\), and take the two final singleton cylinders
   \(1^{d-1}0\) and \(1^d\), both with \(S=[d]\). Then
   \(a(z)\) toggles precisely the carry prefix and

   \[
                         \tau(z)=z+a(z)              \tag{5.13}
   \]

   is addition of one modulo \(2^d\). In particular, \(\tau\) is one
   \(2^d\)-cycle, not a product of local involutions.

2. For \(d\ge3\), partition the half \(z_d=0\) into edges parallel to
   coordinate \(1\), and the half \(z_d=1\) into edges parallel to
   coordinate \(2\). On the first half put
   \(S=[d]\setminus\{1\}\), and on the second put
   \(S=[d]\setminus\{2\}\). This is a subcube partition and

   \[
                         |a(z)|=d-1                 \tag{5.14}
   \]

   for every filling, while the selected exterior/inner frame genuinely
   depends on \(z_d\).

#### Proof

The first family partitions words by their first zero, with the all-one
word as the wraparound case. Toggling the displayed fixed prefix is the
usual binary carry rule.

In the second family, fixing all coordinates except \(1\) partitions
the first half into \(e_1\)-edges; fixing all coordinates except \(2\)
partitions the second half into \(e_2\)-edges. The halves are disjoint
because coordinate \(d\) is fixed in both descriptions. The masks have
the asserted supports, so Theorem 5.1 applies. \(\square\)

## 6. Boundary interpretation and the Dyck hash

Put

\[
 O_x=\{e_i^{x_i}:1\le i\le d\},\qquad
 P_{z,y}=\{h_i^{z_i}:1\le i\le d\}
          \cup\{a_j^{y_j}:1\le j\le r-d\}.           \tag{6.1}
\]

For a constant mask define

\[
                  \tau_a(z,y)=(z+a,y).               \tag{6.2}
\]

Then (4.6) is exactly

\[
 O_x\cup P_{z,y}\longmapsto
 O_{x+a}\cup\bigl(J\setminus P_{\tau_a(z,y)}\bigr).  \tag{6.3}
\]

Moreover,

\[
 d_J(O_x,O_{x+a})=|a|
  =d_J(P_{z,y},P_{z+a,y}),                           \tag{6.4}
\]

so the endpoint cocycle holds statewise, and (3.2) becomes (4.7).
The same formulas hold leafwise for (5.3).

There is an explicit Dyck realization. Put \(r=2d\), and order the inner
coordinates in \(d\) consecutive blocks

\[
                 (\alpha_i,\beta_i,\gamma_i,\delta_i).
\]

Take

\[
 A_i=\{\alpha_i,\delta_i\},\qquad
 H_i=\{\beta_i,\gamma_i\}.                           \tag{6.5}
\]

At the left port fix \(y_i=0\), selecting \(\alpha_i\), and let
\(z_i=0,1\) select \(\beta_i,\gamma_i\), respectively. The two block
words are

\[
                         1100,\qquad1010.             \tag{6.6}
\]

Both are Dyck, and concatenations of Dyck words are Dyck. Hence

\[
                  z\longmapsto P_{z,0}               \tag{6.7}
\]

is a \(2^d\)-element cube of Dyck roots, with

\[
                  d_J(P_{z,0},P_{z+a,0})=|a|.        \tag{6.8}
\]

Taking \(a=\mathbf1\), the half-cycle exchanges every exterior pair and
every \(A_i\)-pair while freezing every \(H_i\)-pair. Its swallowed
target contains exactly the choices \(\beta_i/\gamma_i\), hence recovers
the whole filling \(z\). Because the \(z\)-facets are physically disjoint,
one may install in facet \(z\) any certified exact factor
\(\mathcal F_{r,h(z)}\) chosen by an arbitrary nonlocal hash \(h(z)\).
All packet ledgers remain exact.

With

\[
 d=\left\lfloor\tfrac12\log_2 b\right\rfloor,\qquad r=2d,       \tag{6.9}
\]

one has \(2^r\le b\). Thus every full-excursion fibre in this packet is
below cap, while the packet has \(2^d=b^{1/2+o(1)}\) distinct
filling-resolved targets.

The displayed concatenated family is sparse inside all Dyck roots, but
the same \(1100/1010\) move has an asymptotically full stable cube
packing.

### Theorem 6.1 (near-spanning Dyck fringe-cube packing)

Let \(\mathcal D_r\) be the Dyck words of semilength \(r\), equivalently
plane binary trees with \(r\) internal nodes. There is an absolute
\[
                    \delta_0=\frac12\log_2\frac{17}{16}>0        \tag{6.10}
\]

such that, whenever \(d\le\delta_0r\), apart from

\[
                         e^{-\Omega(r)}C_r            \tag{6.11}
\]

roots, \(\mathcal D_r\) partitions into disjoint \(2^d\)-element cubes.
Every cube is generated by \(d\) disjoint physical replacements

\[
                         1100\longleftrightarrow1010. \tag{6.11a}
\]

and the selected replacement sites are stable under every combination
of the \(d\) toggles.

#### Proof

In the binary-tree model, (6.11) toggles the two possible plane binary
trees with exactly two internal nodes. Call a root of such a subtree a
size-two fringe root.

Let \(F(z,u)\) count binary trees by internal nodes and size-two fringe
roots. The Catalan recursion, with the two size-two trees marked at their
root, is

\[
                  F(z,u)=1+zF(z,u)^2+2(u-1)z^2.      \tag{6.12}
\]

Fix \(u_0=1/2\). Solving the quadratic gives discriminant

\[
                  D_{u_0}(z)=1-4z+8(1-u_0)z^3.       \tag{6.13}
\]

At \(z=1/4\),

\[
                  D_{u_0}(1/4)=\frac1{16}>0.         \tag{6.14}
\]

The coefficients of \(F(z,u_0)\) are nonnegative, so by Pringsheim's
theorem its radius \(R(u_0)\) is a positive real singularity. Equations
(6.13)--(6.14), and monotonicity of \(D_{u_0}\) on \([0,1/4]\), give

\[
                         R(u_0)>1/4.                 \tag{6.15}
\]

In fact one may take

\[
                         \rho=\frac{17}{64}.           \tag{6.16}
\]

Indeed,

\[
 D_{1/2}(17/64)=\frac{817}{65536}>0,                 \tag{6.17}
\]

and \(D_{1/2}'(z)=-4+12z^2<0\) on \([0,17/64]\).
Therefore \(R(1/2)>17/64\). The value of \(\delta_0\) in (6.10) is
exactly \(\log(4\rho)/(2\log2)\).

If \(f_{r,k}\) counts trees with exactly \(k\) marked fringe roots, then

\[
\begin{aligned}
 \sum_{k<d}f_{r,k}
 &\le u_0^{-(d-1)}[z^r]F(z,u_0)\\
 &\le F(\rho,u_0)\,2^{d-1}\rho^{-r}.                 \tag{6.18}
\end{aligned}
\]

Since \(C_r=\Theta(4^rr^{-3/2})\) and \(d\le\delta_0r\), division by
\(C_r\) turns (6.18) into

\[
 O\!\left(r^{3/2}
 \exp\!\left[-\tfrac12r\log(4\rho)\right]\right)
 =e^{-\Omega(r)}.                                    \tag{6.19}
\]

For every remaining tree, list its size-two fringe roots in preorder and
select the first \(d\). Distinct size-two fringe subtrees are disjoint:
two equal-size fringe subtrees cannot properly contain one another.
Toggling one selected root changes only which of the two size-two shapes
occurs there. It neither creates nor destroys a size-two fringe root
elsewhere; its own root remains size two, and it contains no proper
size-two fringe subtree. Since both shapes have the same size, preorder
positions outside the subtree also remain unchanged.

Therefore the first \(d\) selected roots are stable under all toggles.
Their \(\mathbb F_2^d\)-orbits have size \(2^d\), are disjoint, and
partition the good roots. \(\square\)

Theorem 6.1 closes the root-supply issue even for a fixed positive linear
dimension \(d\le\delta_0r\), and hence in particular for every logarithmic
\(d=o(r)\): an exponentially small root remainder may be quarantined.
Within each root cube, Theorem 5.1 supplies a nonconstant port permutation
and an exterior-moving orientation packet. What remains is to align those
packets with all intermediate Chung--Feller layers and the global upper
palette.

### Corollary 6.2 (global Dyck-row boundary Latin cocycle)

For every \(d=o(r)\), there is a permutation

\[
                         \tau:\mathcal D_r\to\mathcal D_r       \tag{6.20}
\]

with the following properties.

1. Outside \(e^{-\Omega(r)}C_r\) exceptional roots, every \(\tau\)-orbit
   has length \(2^d\).
2. On every nonexceptional root \(P_z\), there is a carry mask \(a(z)\)
   such that

   \[
                  \tau(P_z)=P_{z+a(z)},\qquad
                  d_J(P_z,\tau(P_z))=|a(z)|.          \tag{6.21}
   \]

3. If \(x\in\mathbb F_2^d\) indexes \(d\) exterior orientation pairs,
   then

   \[
       (x,P_z)\longmapsto(x+a(z),\tau(P_z))           \tag{6.22}
   \]

   is a bijection, and its exterior displacement equals its Dyck-root
   displacement statewise.

#### Proof

Use Theorem 6.1 to partition the good roots into stable \(d\)-cubes.
Identify each cube with \(\mathbb F_2^d\) by its selected fringe shapes
and use the carry system of Corollary 5.2(1). This is a \(2^d\)-cycle on
each cube and satisfies (6.21). Fix every exceptional root.

On every good cube, (6.22) is the boundary bijection (5.8); on the
exceptional roots use \(a=0\). These disjoint bijections combine into a
global bijection. Equality of the two distances is (6.4), applied to the
physical fringe pairs. \(\square\)

Corollary 6.2 is a complete integral solution of the **two-port**
Dyck-row Latin and geodesic-displacement equations. It is not a solution
of the intermediate-phase and global \(Y\)-ownership equations.

### Proposition 6.3 (exact Dyck-boundary cap splitting)

Restrict one root cube and its exterior context cube to the left-port
occurrences \(y=0\). Under any subcube-addressed system of Theorem 5.1,
there are exactly \(2^d\) swallowed targets and every one has
multiplicity exactly \(2^d\). Hence the boundary cap-\(b\) excess is

\[
                         2^d(2^d-b)_+.               \tag{6.23}
\]

In particular, \(d\le\lfloor\log_2b\rfloor\) removes the hereditary
full-excursion overload inside every root-cube/exterior-cube bundle.

#### Proof

For a leaf \((S_\lambda,b_\lambda)\), target (5.6) records
\(\lambda\) and \(x|_{S_\lambda^c}\). Fixing that target leaves
\(z|_{S_\lambda^c}\) arbitrary in its root cylinder and
\(x|_{S_\lambda}\) arbitrary in its exterior cylinder. The number of
preimages is therefore

\[
             2^{d-|S_\lambda|}2^{|S_\lambda|}=2^d.  \tag{6.24}
\]

The target count follows from the total \(2^{2d}\) boundary occurrences,
and the cap formula follows. \(\square\)

This is the cap ledger relevant to Catalan excursion blindness. Formula
(4.8) is larger because it also counts all non-root based vertices of
the complete orientation packet.

### Proposition 6.4 (direct phase-zero anchoring is exponentially short)

The full orientation-packet factor in Theorem 4.1 cannot be promoted to
a Chung--Feller factor merely by declaring the fringe-cube states
\(P_{z,0}\) to be its phase-zero roots.

Indeed, a \(Q_{r+d}\) braid block contains

\[
                         \frac{2^{r+d}}{2r}           \tag{6.25}
\]

isometric \(C_{2r}\)-cycles. The displayed Dyck ports, including all
exterior orientations \(x\), number only \(2^{2d}\). Their ratio to the
cycle count is

\[
                         2r\,2^{d-r}.                 \tag{6.26}
\]

For disjoint size-two fringe moves, necessarily \(2d\le r\), and hence

\[
                         2r\,2^{d-r}
 \le 2r\,2^{-r/2}=o(1).                              \tag{6.27}
\]

#### Proof

Each active \(Q_r\)-facet has \(2^r/(2r)\) cycles and there are \(2^d\)
facets, proving (6.25). A displayed left port is specified by
\((x,z)\in\mathbb F_2^d\times\mathbb F_2^d\), with \(y=0\), proving the
port count. Distinct size-two fringe subtrees contain two disjoint
internal nodes each, so \(2d\le r\). The remaining formulas follow.
\(\square\)

This rules out the most direct standalone phase interpretation. It does
not rule out using the braid as a segment of longer global rows, where
phase-zero roots lie outside the local orientation block.

### Theorem 6.5 (fixed-frame, fixed-background aggregate fringe-braid alphabet obstruction)

Fix one aligned child coordinate block of semilength \(r\), one common
physical pair frame on its \(2r\) child coordinates, one common set of
\(d\) exterior pairs, and one fixed background \(K\) shared by all counted
occurrences. Consider any family of diagonal braids obtained from \(d\)
disjoint \(1100/1010\) fringe moves. Let \(\mathscr A_{r,d}\)
be the set of all possible physical swallowed targets (3.2), over every
root cube, exterior orientation, and subcube-addressed mask. Then

\[
 |\mathscr A_{r,d}|
 \le {\,2(r+d)\choose d}.                            \tag{6.28}
\]

Since disjoint size-two fringes give \(d\le r/2\),

\[
 |\mathscr A_{r,d}|
 \le {3r\choose \lfloor r/2\rfloor}
 \le 2^{3rH_2(1/6)}
 =2^{(2-\eta)r},                                     \tag{6.29}
\]

where

\[
 \eta:=2-3H_2(1/6)>0.                                \tag{6.30}
\]

Consequently, if one such boundary occurrence is realized for every
root in the good set of Theorem 6.1, then at cap \(b\) its raw overload
is at least

\[
 \boxed{
 \left((1-e^{-\Omega(r)})C_r
       -b\,2^{(2-\eta)r}\right)_+.}                  \tag{6.31}
\]

In particular, for

\[
 r\ge \frac{2}{\eta}\log_2b+O(1),                   \tag{6.32}
\]

the lower bound in (6.31) is \((1-o(1))C_r\).

#### Proof

If \(s=|a(z)|\), formula (3.2) contains \(d-s\) persistent exterior
coordinates and \(s\) coordinates of \(P_z\setminus P_{\tau z}\).
Thus its variable part has exactly \(d\) coordinates, all drawn from
the \(2d\) exterior and \(2r\) child coordinates. The remaining
background is the same physical set \(K\) in every counted occurrence,
so it does not enlarge the support. This proves (6.28).

The binomial coefficient in (6.28) increases with \(d\) on
\(0\le d\le r/2\), so it is at most
\(\binom{3r}{\lfloor r/2\rfloor}\). Since
\(\lfloor r/2\rfloor/(3r)\le1/6\), the standard entropy bound gives
(6.29).
Positivity of \(\eta\) is exact:

\[
 3H_2(1/6)<2
 \quad\Longleftrightarrow\quad
 6^6<16\cdot5^5,
\]

and \(46656<50000\).

Choose one exterior orientation for every good Dyck root. These
\((1-e^{-\Omega(r)})C_r\) occurrences use at most
\(|\mathscr A_{r,d}|\) targets. For nonnegative integral loads,

\[
 \sum_T(\mu(T)-b)_+
 \ge \sum_T\mu(T)-b|\operatorname{supp}\mu|,
\]

which proves the displayed overload bound. Finally
\(C_r=\Theta(2^{2r}r^{-3/2})\), and (6.32) makes its second term
\(o(C_r)\). \(\square\)

Theorem 6.5 rules out the **fixed-frame, fixed-background
disjoint-fringe diagonal class** as a coefficient-one solution. More
generally, if at most \(L\) backgrounds occur, multiply the support bound
(6.29) by \(L\) and replace the second term in (6.31) by
\(bL2^{(2-\eta)r}\). Without a bound on the number of backgrounds, a
root-dependent background can itself encode the root, and this argument
gives no obstruction. Changing the physical pair frame with the root also
evades the common alphabet count.

The theorem's value is therefore narrower and exact: it proves a literal
nontrivial boundary cocycle and identifies why its fixed-carrier version
still has too little statewise target entropy after all Catalan cubes are
aggregated. An escape needs monodromy whose swallowed target uses more
than \(r/2\) independently varying child/exterior coordinates, or a
cross-context braid in which the common exterior part itself carries
root-scale information.

## 7. Reciprocal component cycles

Let \(\Omega\) be a finite owner set and let \(\Pi_0,\Pi_1\) be
partitions of \(\Omega\) into complete cycles of two exact factors. Form
the bipartite multigraph \(B\) whose left vertices are cycles of
\(\Pi_0\), whose right vertices are cycles of \(\Pi_1\), and whose edge
labelled \(x\in\Omega\) joins the two cycles containing \(x\).

### Theorem 7.1 (reciprocal-overlay classification)

A binary whole-cycle hybrid covers every owner exactly once if and only
if, on each connected component of \(B\), it chooses all cycles from one
shore and no cycles from the other. There are exactly two choices per
connected component.

If both inputs are literal odd-graph factors, every such hybrid is again
a literal exact factor and owns the complementary upper shore once.

#### Proof

Let \(s(C)\in\{0,1\}\) record whether cycle \(C\) is selected. The owner
\(x\), represented by an edge \(C_0C_1\), is covered once exactly when

\[
                         s(C_0)+s(C_1)=1.             \tag{7.1}
\]

On a connected bipartite component, (7.1) determines all bits from one
initial bit: either every left cycle or every right cycle is selected.

For an odd-graph factor, the successor is a bijection on its selected
middle owners, and complementing the successor gives the upper token. A
hybrid partitioning the middle owners therefore also partitions their
complements. \(\square\)

Thus a crossing coordinate conjugate \(hF\) can be mixed with \(F\)
integrally, but a filling hash must be constant on the connected
components of their cycle overlay. A global positive theorem must prove
that a crossing conjugate has sufficiently many balanced components and
that their target effects separate the hereditary fibres. A connected
overlay leaves only the two global factors.

## 8. Exact global boundary

Theorem 4.1 is an exact alternating factor on its physical orientation
packet. It does not provide:

1. one physical Dyck root on every global cycle, with every Dyck root used
   once;
2. a bijection onto every Chung--Feller phase layer;
3. the complete global adjacent-union palette rather than one packet's
   injective selected palette; or
4. a positive-density parent-crossing packing.

There is also a separate global limitation. If every braid packet is
subordinate to one fixed physical perfect-matching frame, the full-pair
profile of that frame remains invariant under lower windows. The known
fixed-frame Gaussian Hall obstruction survives. A coefficient-one use of
the braid must vary physical frames across parent contexts, not merely
vary the cyclic order inside the \(z\)-facets.

The following are proved:

* stationary filling-dependent exterior permutations are gauge-trivial;
* nontrivial boundary monodromy is characterized by (3.1);
* the constant and subcube-addressed diagonal braids attain (3.1)
  literally, with exact \(2^d\)-way target splitting;
* the first \(d\le\delta_0r\) size-two fringes partition all but
  \(e^{-\Omega(r)}C_r\) roots into stable \(2^d\)-cubes and give an
  exact global two-port Dyck Latin permutation;
* nevertheless the full disjoint-fringe target alphabet is at most
  \(2^{(2-\eta)r}\), forcing Catalan-scale overload at logarithmic
  \(r\) as in (6.31); and
* binary global promotion is exactly componentwise in the reciprocal
  cycle overlay.

The following remain unproved:

* a positive-density embedding in one global MSW/Chung--Feller factor;
* its phase-zero, all-phase Latin, and global upper ownership equations;
* a crossing-frame component theorem removing the fixed-frame Hall cut;
* any \(o(W)\) all-depth missing-shadow or floor-covariance bound.

Accordingly the stationary-context route is closed, while a literal
exterior-moving seed with exponential target resolution is available.
The next algebraic object is a crossing-frame reciprocal-overlay/Latin
packing, not another hash on a fixed carrier.
