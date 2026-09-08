# Global filling-dependent MSW hashes: an exact collar cocycle, a split-braid compiler, and the present router obstructions

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Exact outcome

Write

\[
 C_r={1\over r+1}{2r\choose r},
 \qquad \mathcal D_r=\{\hbox{Dyck roots of semilength }r\}.
\]

There are four exact conclusions.

1. **A synchronized fixed-rank MSW hash cannot move its exterior
   collar.**  At consecutive Chung--Feller phases the local states are
   already distinct.  Johnson-distance additivity therefore spends the
   unique available exchange inside the child block and forces the
   exterior state to remain fixed, pointwise on every row.  This remains
   true for a hash depending on the entire Dyck word and for arbitrary
   phasewise permutations of the complete context--filling product.

2. **The two-port obstruction is not algebraic.**  For every
   \(d=o(r)\), all but \(e^{-\Omega(r)}C_r\) Dyck roots can be partitioned
   into stable \(2^d\)-cubes of disjoint
   \(1100\leftrightarrow1010\) fringe rotations.  Binary carry on every
   cube gives a permutation \(\tau\) of the Dyck roots with \(2^d\)-cycles
   and a filling-dependent mask \(a(P)\) such that

   \[
    d_J(P,\tau P)=|a(P)|.
   \]

   On \(d\) exterior orientation pairs the map

   \[
          (x,P)\longmapsto (x+a(P),\tau P)                 \tag{0.1}
   \]

   is a bijection, and its exterior displacement is exactly the local
   port displacement.  Thus (0.1) is a literal integral solution of the
   boundary Latin and geodesic-cocycle equations on asymptotically all
   Dyck roots.  This is an endpoint theorem, not an all-phase
   Chung--Feller factor.

3. **There is an exact conditional global hash compiler.**  If an
   exterior factor supplies a palette-uniform prefix router and a
   palette-uniform suffix inverse router, meeting at a central palette
   \(\{Q_c\}\), then for an arbitrary nonlocal hash \(h(P)\) the
   triangular shear

   \[
                  (c,P)\longmapsto(\rho_{h(P)}c,P)       \tag{0.2}
   \]

   gives one literal integral exact product-packet replacement, including
   the complete lower and adjacent-union ledgers.  If a group \(G\) acts
   regularly on the central contexts, one hash simultaneously bounds
   every one-context swallowed-target fibre by

   \[
                         \left\lceil {C_r\over |G|}\right\rceil.
                                                                  \tag{0.3}
   \]

   Hence the exact isolated-context, fixed-phase cap-\(p\) coding
   threshold for this regular-action compiler is

   \[
                         |G|\ge \left\lceil {C_r\over p}\right\rceil.
                                                                  \tag{0.4}
   \]

4. **Neither the explicit fringe braid nor the currently certified
   MSW \(C_6/C_8\) routers supply that compiler.**

   * The explicit diagonal construction is an exact orientation-cube
     packet, not a near-spanning MSW factor.  Its displayed Dyck ports hit
     only an \(o(1)\) fraction of its factor cycles.
   * The fixed-frame, fixed-background disjoint-fringe diagonal class has at most
     \(2^{(2-\eta)r}\) swallowed targets, where

     \[
       \eta=2-3H_2(1/6)>0.
     \]

     Once \(r\ge(2/\eta)\log_2p+O(1)\), its cap-\(p\) overload is
     \((1-o(1))C_r\).  It breaks individual excursion blindness but not
     the aggregate Catalan collision floor.  This alphabet obstruction
     does not apply when a root-dependent exterior background itself
     carries Catalan-scale information, or when the physical pair frame
     changes with the root.
   * A directed cycle of the smallest moving-exterior \(C_6\) routers
     duplicates exactly three triangle owners per context.  Identifying
     them gives degree three; retaining only the exterior conveyor inserts
     and then deletes the intermediate exterior coordinate and is not
     geodesic.
   * The paired star-to-star \(C_6\) is an exact bounded prefix router,
     but a second nonidentity router on the same transported star label
     must delete the petal inserted by the first.  No complementary-shore
     inverse suffix or growing fresh-representation tensor has been
     certified.
   * The positive-density clean suffix \(C_8\) bank has strand
     displacements \((1,1,1,2)\), so no common equal-distance exterior
     cut exists.  Its exact five-row \(D_3\) completion is not a split
     module: the prefix palette fails at the first internal cut and the
     suffix palette fails at the second.

Consequently no coefficient-one theorem is proved here.  The endpoint
Latin/displacement equations and the algebraic composition law are
solved; intermediate \(X/Y\) ownership is conditional.  For the
split-braid architecture developed below, the missing sufficient object is
a positive-density, port-closed, palette-uniform exterior router library
whose total legal physical address range has size at least \(C_r/p\) and
one common hash that loads every such address at most \(p\);
a regular central orbit of that order is one sufficient realization.
A joint code--phase compiler could distribute this range between its
central orbit and genuinely distinct phase addresses.  A cross-context
target-collision estimate is then still required.  The known local routers
do not form such a library.

## 1. Product phases and exact ownership

Let \(E,J\) be disjoint coordinate blocks.  Let

\[
             c\longmapsto O_c\in{E\choose e},
             \qquad c\in\mathcal C,                         \tag{1.1}
\]

be injective.  Let \(\mathcal D\) be a finite child-row set and let

\[
             \xi_t:\mathcal D\longrightarrow\mathcal L_t
                   \subseteq {J\choose r},
             \qquad 0\le t\le r,                            \tag{1.2}
\]

be bijective at every phase.  In the MSW application, \(\mathcal D\) is
\(\mathcal D_r\), and the \(\mathcal L_t\)'s are the Chung--Feller flaw
layers.  In particular,

\[
                         \mathcal L_t\cap\mathcal L_{t+1}
                         =\varnothing.                         \tag{1.3}
\]

The complete product phase is

\[
                         V_t(c,u)=O_c\mathbin{\dot\cup}\xi_t(u).
                                                                  \tag{1.4}
\]

A completely general filling-dependent phase reindexing is a map

\[
 F_t=(\alpha_t,\beta_t):
       \mathcal C\times\mathcal D\longrightarrow
       \mathcal C\times\mathcal D,                           \tag{1.5}
\]

and the displayed row state is

\[
                         Z_t(z)=V_t(F_tz).                     \tag{1.6}
\]

No locality or bounded hash alphabet is assumed.

At phase \(t\), exact lower ownership is equivalent to

\[
                         F_t\in\operatorname{Sym}
                           (\mathcal C\times\mathcal D).       \tag{1.7}
\]

For a prescribed upper palette \(\mathcal Y\), exact upper ownership is
the literal multiset identity

\[
 \mathop{\dot\bigcup}_{t,z}
       \{Z_t(z)\cup Z_{t+1}(z)\}=\mathcal Y.                  \tag{1.8}
\]

Thus phasewise Latin ownership is necessary but does not by itself prove
the adjacent-union ledger.

## 2. Statewise phase rigidity

### Theorem 2.1 (no exterior braid in synchronized fixed-rank phases)

Assume (1.3), every \(F_t\) is a permutation, and every consecutive pair
in (1.6) is a Johnson edge.  Then

\[
                         \boxed{\alpha_{t+1}(z)=\alpha_t(z)}   \tag{2.1}
\]

for every row \(z\) and every \(t\).  After reindexing rows by \(F_0\),

\[
 F_0=1,
 \qquad
 F_t(c,u)=(c,\beta_{t,c}(u)),
 \qquad
 \beta_{t,c}\in\operatorname{Sym}(\mathcal D).               \tag{2.2}
\]

Hence the factor splits contextwise.  A nonlocal full-word hash does not
move the collar while the synchronized product phases are retained.

#### Proof

Johnson distance is additive on disjoint fixed-rank blocks:

\[
\begin{aligned}
 1=d_J(Z_t(z),Z_{t+1}(z))
  ={}&d_J(O_{\alpha_t(z)},O_{\alpha_{t+1}(z)})\\
    &+d_J(\xi_t(\beta_t(z)),
                  \xi_{t+1}(\beta_{t+1}(z))).                 \tag{2.3}
\end{aligned}
\]

The second term is at least one by (1.3).  It is therefore exactly one,
and the exterior term is zero.  Injectivity in (1.1) proves (2.1).

Normalize \(F_0=1\).  Equation (2.1) gives
\(\alpha_t(c,u)=c\).  A permutation preserving its first coordinate
restricts to a permutation on every context fibre, giving (2.2).
\(\square\)

### Corollary 2.2 (complete stationary context fibres are gauge)

Suppose every child row is replicated over all \(c\in\mathcal C\).  If a
phase-independent hash assigns a permutation \(\gamma_u\) of
\(\mathcal C\) to child filling \(u\), then

\[
 \{(O_{\gamma_u(c)},\xi_0(u),\ldots,\xi_r(u)):c\in\mathcal C\}
 =
 \{(O_c,\xi_0(u),\ldots,\xi_r(u)):c\in\mathcal C\}.            \tag{2.4}
\]

Thus it is a row relabelling and changes no physical target multiset.

Theorem 2.1 identifies the only escape: at some physical step the child
phase must stall, its rank must change, or a cross-block exchange must be
made.  A global braid must spend literal exterior-moving collars.

## 3. The exact boundary cocycle

Let \(|J|=2r\), and let

\[
                         u\longmapsto P_u\in{J\choose r}       \tag{3.1}
\]

be injective.  Consider a length-\(r\) segment with left and right ports

\[
\begin{aligned}
 Z_0(c,u)&=O_c\mathbin{\dot\cup}P_u,\\
 Z_r(c,u)&=O_{\rho(c,u)}\mathbin{\dot\cup}
                    (J\setminus P_{\tau(c,u)}).                \tag{3.2}
\end{aligned}
\]

### Theorem 3.1 (distance-balanced boundary Latin cocycle)

If both boundary product families are owned once and every segment in
(3.2) is a Johnson geodesic of length \(r\), then

\[
             \Psi=(\rho,\tau)\in
             \operatorname{Sym}(\mathcal C\times\mathcal D),  \tag{3.3}
\]

and, statewise,

\[
 \boxed{
 d_J(O_c,O_{\rho(c,u)})
       =|P_u\setminus P_{\tau(c,u)}|.}                         \tag{3.4}
\]

The target of a window swallowing the entire segment is

\[
 \boxed{
 \bigcap_{t=0}^rZ_t(c,u)
  =(O_c\cap O_{\rho(c,u)})\mathbin{\dot\cup}
      (P_u\setminus P_{\tau(c,u)}).}                           \tag{3.5}
\]

If the common value in (3.4) is \(s\), at least \(s\) of the physical
Johnson transitions touch exterior coordinates.

#### Proof

Right-boundary ownership and injectivity of the product coordinates give
(3.3).  The endpoint distance is

\[
\begin{aligned}
 d_J(Z_0,Z_r)
 &=d_J(O_c,O_{\rho(c,u)})+|P_u\cap P_{\tau(c,u)}|\\
 &=d_J(O_c,O_{\rho(c,u)})
      +r-|P_u\setminus P_{\tau(c,u)}|.                        \tag{3.6}
\end{aligned}
\]

It equals the geodesic length \(r\), proving (3.4).

A shortest Johnson path never removes a coordinate common to its
endpoints and never inserts a coordinate outside their union.  Hence its
full intersection is its endpoint intersection, which is (3.5).  Finally,
each coordinate of \(O_c\setminus O_{\rho(c,u)}\) must be removed in a
distinct transition.  \(\square\)

Equations (3.3)--(3.5) are necessary, not sufficient.  Intermediate
lower phases and the complete upper palette still have to close.

### Lemma 3.2 (logical inverse is not physical collar return)

Let \(Z_0,\ldots,Z_L\) be a Johnson geodesic and let \(E\) be any
coordinate block.  If

\[
                         Z_s\cap E=Z_t\cap E
                         \qquad(s<t),                           \tag{3.7}
\]

then no coordinate of \(E\) changes membership between times \(s\) and
\(t\).

#### Proof

On a Johnson geodesic every coordinate changes membership at most once:
a deletion followed by reinsertion, or an insertion followed by deletion,
adds two transitions without increasing endpoint distance.  Equality
(3.7) gives even change parity for every exterior coordinate, so its
number of changes is zero.  \(\square\)

Thus a prefix router and a logical inverse suffix cannot install a
physical collar and later return to the same set.  A legal split module
instead routes from \(R_c\) through \(Q_{\rho_a(c)}\) to the physically
complementary shore \(E\setminus R_c\); only the *row label* has zero
holonomy.

## 4. An explicit global Dyck boundary braid

The next theorem solves (3.3)--(3.4) on asymptotically all Dyck roots.

### Theorem 4.1 (near-spanning stable fringe cubes)

There is an absolute \(\delta_0>0\) such that, for every
\(d\le\delta_0r\), all but \(e^{-\Omega(r)}C_r\) roots in
\(\mathcal D_r\) partition into disjoint \(2^d\)-element cubes.  Every
cube is generated by \(d\) disjoint physical replacements

\[
                         1100\longleftrightarrow1010,            \tag{4.1}
\]

and its selected replacement sites are stable under every combination of
the toggles.

#### Proof

In the plane-binary-tree model, (4.1) interchanges the two trees having
exactly two internal nodes.  Let \(F(z,u)\) count trees by internal nodes
and by size-two fringe roots.  Catalan recursion with the two size-two
trees marked at their root gives

\[
                         F(z,u)=1+zF(z,u)^2+2(u-1)z^2.           \tag{4.2}
\]

At \(u_0=1/2\), the quadratic discriminant is

\[
                         D(z)=1-4z+4z^3.                         \tag{4.3}
\]

On \(0\le z\le17/64\), one has \(D'(z)=-4+12z^2<0\), while

\[
                         D(17/64)={817\over65536}>0.             \tag{4.3a}
\]

The nonnegative series \(F(z,u_0)\) has its radius at a positive real
singularity by Pringsheim's theorem.  Equations (4.3)--(4.3a) show that
this radius is greater than \(17/64\).  Set

\[
 \varrho={17\over64},
 \qquad
 \boxed{\delta_0={1\over2}\log_2{17\over16}>0.}                 \tag{4.4}
\]

If \(f_{r,k}\) counts trees with exactly \(k\) size-two fringe roots,
then

\[
\begin{aligned}
 \sum_{k<d}f_{r,k}
 &\le 2^{d-1}[z^r]F(z,1/2)\\
 &\le F(\varrho,1/2)2^{d-1}\varrho^{-r}.                       \tag{4.5}
\end{aligned}
\]

Since \(C_r=\Theta(4^rr^{-3/2})\), (4.4)--(4.5) are
\(e^{-\Omega(r)}C_r\).

For every remaining tree, choose the first \(d\) size-two fringe roots in
preorder.  Equal-size fringe subtrees are disjoint.  Toggling one chosen
root changes neither the existence nor the preorder position of the
others: both local shapes have the same size, retain their own size-two
root, and contain no proper size-two fringe root.  The chosen sites are
therefore stable, their orbits are \(d\)-cubes, and those orbits partition
the good roots.  \(\square\)

### Theorem 4.2 (global carry cocycle)

For every \(d=o(r)\), there is a permutation

\[
                         \tau:\mathcal D_r\longrightarrow\mathcal D_r
                                                                  \tag{4.6}
\]

such that, outside \(e^{-\Omega(r)}C_r\) exceptional fixed roots,

1. every \(\tau\)-orbit has length \(2^d\);
2. every root \(P_z\) has a carry mask \(a(z)\in\mathbb F_2^d\) with

   \[
                \tau(P_z)=P_{z+a(z)},
                \qquad d_J(P_z,\tau(P_z))=|a(z)|;               \tag{4.7}
   \]

3. for \(d\) exterior orientation pairs, the map

   \[
                (x,P_z)\longmapsto(x+a(z),\tau(P_z))             \tag{4.8}
   \]

   is a bijection.

#### Proof

Identify every good cube from Theorem 4.1 with \(\mathbb F_2^d\).  Order
the bits from least to most significant.  If \(j\) is the first zero,
toggle bits \(1,\ldots,j\); on the all-one word toggle all bits.  This is
addition by one modulo \(2^d\), hence a \(2^d\)-cycle.  Its mask is
constant on the coordinate cylinder through which it acts.

Each toggled fringe site changes one selected child coordinate, so the
local Johnson distance equals the mask weight.  Translate the exterior
orientation by the same mask.  On every cylinder, both the local carry
and the exterior translation are bijections; distinct cylinders map to
distinct complemented cylinders.  Thus (4.8) is a bijection.  Fix the
exceptional roots.  \(\square\)

To interpret (4.8) as the boundary map in Theorem 3.1, set

\[
 O_x=\{e_i^{x_i}:1\le i\le d\}.
\]

Then

\[
 d_J(O_x,O_{x+a(z)})=|a(z)|
   =d_J(P_z,P_{z+a(z)}),                                      \tag{4.9}
\]

so the endpoint

\[
 O_x\cup P_z
   \longmapsto
 O_{x+a(z)}\cup(J\setminus P_{z+a(z)})                         \tag{4.10}
\]

has Johnson distance \(r\).  This is the promised exact two-port
cocycle.

## 5. A literal diagonal realization and its collision floor

Assume that \(Q_r\) has an exact factor into simple isometric
\(C_{2r}\)-cycles.  This divisibility-admissible hypothesis is necessary
for the construction below; in particular \(2r\mid2^r\).  The previously
proved syndrome construction supplies such a factor when
\(r=2^t\) with \(t\ge1\).  The case \(r=1\) has no simple \(C_2\).
Under this hypothesis, the boundary equations above are attained by a
literal orientation-cube packet.  Take pairwise disjoint pairs

\[
 E_i=\{e_i^0,e_i^1\},\quad H_i=\{h_i^0,h_i^1\}\quad(1\le i\le d),
\]

and

\[
 A_j=\{a_j^0,a_j^1\}\quad(1\le j\le r-d).
\]

An owner is

\[
 K\cup\{e_i^{x_i}\}_i\cup\{h_i^{z_i}\}_i
      \cup\{a_j^{y_j}\}_j.                                  \tag{5.1}
\]

Let \(a(z)\) satisfy the exact stability equation

\[
 a(z')=a(z)\quad\hbox{whenever}\quad
 z'|_{\operatorname{supp}a(z)}
      =z|_{\operatorname{supp}a(z)}.                           \tag{5.2}
\]

For a mask support \(S\), make the \(E_i\)-axis active for \(i\in S\),
the \(H_i\)-axis active for \(i\notin S\), and every \(A_j\)-axis
active.  Freeze the other \(d\) axes.  Equation (5.2) partitions the
owner block into disjoint active \(Q_r\)-facets.  Install an arbitrary
exact isometric \(C_{2r}\)-factor in every facet.

### Proposition 5.1 (exact diagonal packet)

The resulting packet owns every selected lower state and adjacent-union
token once.  Every half-cycle is a Johnson geodesic and has endpoint map

\[
 (x,z,y)\longmapsto
 (x+a(z),z+\mathbf1+a(z),y+\mathbf1).                         \tag{5.3}
\]

Its swallowed target is

\[
 \Phi(x,z)=K
  \cup\{e_i^{x_i}:i\notin\operatorname{supp}a(z)\}
  \cup\{h_i^{z_i}:i\in\operatorname{supp}a(z)\}.              \tag{5.4}
\]

#### Proof

Within one stable cylinder, the free coordinates are the active axes just
listed, exactly \(r\) of them.  Distinct cylinders and frozen
orientations give equal or disjoint \(Q_r\)-facets which exhaust (5.1).
Cycle-factor ownership is therefore exact.  An adjacent-union token
recovers its changed pair and its underlying cube edge, so distinct factor
edges give distinct upper tokens.

An isometric \(C_{2r}\) uses every active direction once in each
half-cycle.  This proves (5.3).  Active pairs contribute no coordinate to
the full intersection, while every inactive pair contributes its fixed
orientation, giving (5.4).  \(\square\)

For a single Dyck root cube and exterior cube, restrict to
\(y=y_0\), the fixed non-fringe orientation of that Dyck cube, and to its
left-port occurrences.  Then (5.4) gives exactly \(2^d\) targets, every
one with multiplicity \(2^d\).  Thus its exact cap-\(p\) excess is

\[
                         2^d(2^d-p)_+.                          \tag{5.5}
\]

Indeed, on a mask cylinder with support \(S\), the target records that
cylinder and \(x|_{S^c}\).  The coordinates \(z|_{S^c}\) and \(x|_S\)
remain free, giving
\(2^{d-|S|}2^{|S|}=2^d\) preimages.  The number of targets is
\(\sum_{\text{cylinders}}2^{d-|S|}=2^d\), because the source cylinders
partition \(\mathbb F_2^d\).

Without the restriction \(y=y_0\), the target (5.4) is blind to all
\(r-d\) coordinates of \(y\), and every target in the complete
orientation packet has multiplicity \(2^r\), not \(2^d\).

### Proposition 5.1A (direct Dyck-phase anchoring is sparse)

The factor in Proposition 5.1 contains

\[
                         {2^{r+d}\over2r}                       \tag{5.5a}
\]

isometric cycles.  The displayed Dyck ports, including all exterior
orientations \(x\), number only \(2^{2d}\).  Therefore the ratio of
displayed ports to factor cycles is

\[
                         2r\,2^{d-r}.                           \tag{5.5b}
\]

For disjoint size-two fringe moves \(2d\le r\), and hence

\[
                         2r\,2^{d-r}
                         \le2r\,2^{-r/2}=o(1).                  \tag{5.5c}
\]

#### Proof

There are \(2^d\) active \(Q_r\)-facets, each containing
\(2^r/(2r)\) factor cycles, which proves (5.5a).  A displayed port is
indexed by \((x,z)\in\mathbb F_2^d\times\mathbb F_2^d\), proving its
count.  Each selected size-two fringe uses two disjoint child nodes, so
\(2d\le r\).  \(\square\)

Thus one cannot promote Proposition 5.1 to a Chung--Feller factor merely
by declaring the displayed fringe roots to be phase zero.  Nor has a
simultaneous installation of these packets over all good cubes been
proved.  The packet may still be usable as a segment of longer global
rows whose Dyck roots lie outside it.

This local split is useful when \(d\le\lfloor\log_2p\rfloor\), but the
aggregate Catalan alphabet is too small.

### Theorem 5.2 (fixed-frame, fixed-background aggregate fringe-braid alphabet obstruction)

Fix one child block of semilength \(r\), one common physical pair frame
on its \(2r\) child coordinates, one common set of \(d\) exterior pairs,
and one fixed background \(K\) shared by every counted occurrence.
Consider any family of diagonal braids obtained from \(d\) disjoint
size-two fringe moves.  Let \(\mathscr A_{r,d}\) be the set of physical
swallowed targets.  Then

\[
 |\mathscr A_{r,d}|
   \le {2(r+d)\choose d}
   \le {3r\choose \lfloor r/2\rfloor}
   \le 2^{3rH_2(1/6)}
   =2^{(2-\eta)r},                                    \tag{5.6}
\]

where

\[
                         \eta=2-3H_2(1/6)>0.                    \tag{5.7}
\]

If at least one such fixed-background occurrence is realized for every
good Dyck root of Theorem 4.1, then its cap-\(p\) raw overload is at least

\[
 \boxed{
 \left((1-e^{-\Omega(r)})C_r
       -p\,2^{(2-\eta)r}\right)_+.}                            \tag{5.8}
\]

Along every sequence \(r\to\infty\) satisfying

\[
                         r\ge{2\over\eta}\log_2p+O(1),          \tag{5.9}
\]

the right side of (5.8) is \((1-o(1))C_r\).

#### Proof

If \(s=|a(z)|\), target (5.4) contains \(d-s\) varying exterior
coordinates and \(s\) coordinates from
\(P_z\setminus P_{z+a(z)}\).  Its variable part therefore has exactly
\(d\) coordinates chosen from at most \(2d+2r\) physical coordinates.
The remaining background is the same set \(K\) for every counted
occurrence, so it does not enlarge the target support.  This gives the
first inequality in (5.6).  Disjoint size-two fringes use two child nodes
each, so \(d\le r/2\); monotonicity in \(d\) gives the second inequality,
with the floor covering odd \(r\).  Since
\(\lfloor r/2\rfloor/(3r)\le1/6\), the entropy bound gives the third.

Positivity in (5.7) is exact:

\[
 3H_2(1/6)<2
 \quad\Longleftrightarrow\quad
 6^6<16\cdot5^5,
\]

and \(46656<50000\).

There are \((1-e^{-\Omega(r)})C_r\) good occurrences and at most the
number of bins in (5.6).  For integral loads,

\[
 \sum_T(\mu(T)-p)_+
   \ge\sum_T\mu(T)-p|\operatorname{supp}\mu|,                  \tag{5.10}
\]

which is (5.8).  Finally,
\(C_r=\Theta(2^{2r}r^{-3/2})\), while (5.9) makes
\(p r^{3/2}2^{-\eta r}=o(1)\).  \(\square\)

Thus the diagonal braid is a genuine nonlocal, exterior-moving integral
seed, but its fixed-background version is not a coefficient-one
construction.  It needs either more than \(r/2\) independent target
coordinates or a root-dependent global exterior address whose target
information is not confined to one fixed carrier.

More generally, if the occurrences use at most \(L\) possible background
sets, then the right side of the support bound in (5.6) is multiplied by
\(L\), and (5.8) becomes

\[
 \left((1-e^{-\Omega(r)})C_r
       -pL\,2^{(2-\eta)r}\right)_+.                            \tag{5.11}
\]

No bound follows from this argument when the background is allowed to
encode the root injectively.  That possibility is exactly part of the
global exterior-moving collar problem.  The argument also gives no bound
when the child/exterior pair frame itself varies with the root, because
the ambient target alphabet used in (5.6) is then no longer common.

## 6. The exact split-braid compiler

The positive global algebraic mechanism is now stated precisely.

Let \(|E|=2s\), and let \(R_c\in{E\choose s}\) be distinct exterior
roots.  Let

\[
 P_u=B_0(u),B_1(u),\ldots,B_r(u)=J\setminus P_u,
 \qquad u\in\mathcal D_r,                                  \tag{6.1}
\]

be one exact rooted child factor.  Fix a cut \(0\le k\le s\).  For each
code \(a\in\mathcal A\), suppose there are exterior geodesics

\[
 R_c=A_0^a(c),A_1^a(c),\ldots,A_s^a(c)=E\setminus R_c.          \tag{6.2}
\]

For the actual Chung--Feller phase chart with \(r\ge1\), the phase families
\(\{B_t(u):u\in\mathcal D_r\}\) are pairwise disjoint.  Moreover,

\[
 \{P_u:u\in\mathcal D_r\}
 \cap
 \{J\setminus P_v:v\in\mathcal D_r\}
 =\varnothing,                                                \tag{6.2a}
\]

because every nonempty Dyck word begins with \(1\), whereas its complement
begins with \(0\).  The compiler theorem below does not need (6.2a), but
the necessity statement in Proposition 6.2 does.

Write \(U_i^a(c)=A_i^a(c)\cup A_{i+1}^a(c)\).  The family is a
**split exterior braid module** when:

1. for every two codes, the complete prefix palettes

   \[
   \biguplus_{c,\,0\le i\le k}\{A_i^a(c)\},
   \qquad
   \biguplus_{c,\,0\le i<k}\{U_i^a(c)\}                    \tag{6.3}
   \]

   are equal as physical multisets;
2. the analogous complete suffix palettes for \(k\le i\le s\) and
   \(k\le i<s\) are code-independent; and
3. there are distinct central states \(Q_c\) and permutations
   \(\rho_a\in\operatorname{Sym}(\mathcal C)\) such that

   \[
                         A_k^a(c)=Q_{\rho_a(c)}.                 \tag{6.4}
   \]

Choose any hash \(h:\mathcal D_r\to\mathcal A\).  For each \((c,u)\),
join, counting each common seam state once,

\[
\begin{array}{ll}
\text{prefix:}&A_i^{h(u)}(c)\cup P_u,\quad0\le i\le k,\\
\text{child:}&Q_{\rho_{h(u)}c}\cup B_t(u),\quad0\le t\le r,\\
\text{suffix:}&A_i^{h(u)}(c)\cup(J\setminus P_u),\quad k\le i\le s.
\end{array}                                                    \tag{6.5}
\]

### Theorem 6.1 (triangular hash compiler)

Assume that (6.5) with one constant code is a literal exact product
packet.  Then (6.5) is a literal integral exact replacement for every
hash \(h\).  Every row is a length-\((s+r)\) geodesic from

\[
 R_c\cup P_u
 \quad\hbox{to}\quad
 (E\setminus R_c)\cup(J\setminus P_u),                         \tag{6.6}
\]

and the complete lower and adjacent-union multisets are independent of
\(h\).

#### Proof

Every prefix and suffix step changes only \(E\), every child step changes
only \(J\), and (6.4) makes both joins literal.  There are \(s+r\) moves,
equal to the Johnson distance between the complementary endpoints (6.6),
so every row is geodesic.

Fix \(u\).  The prefix and suffix palettes are code-independent by
(6.3) and its suffix analogue, after adjoining the injective tags
\(P_u\) and \(J\setminus P_u\).  In the child, the map

\[
                         c\longmapsto\rho_{h(u)}c                \tag{6.7}
\]

is a permutation.  Thus every child phase has exactly the product palette

\[
 \{Q_d\cup B_t(u):d\in\mathcal C, u\in\mathcal D_r\}.         \tag{6.8}
\]

The same argument applies to child adjacent unions and to the prefix and
suffix upper palettes.  The two seam lower palettes are each present in
two displayed pieces but are counted only once in the joined path; this
subtraction is code-independent by (6.7).  There is no extra seam edge.
Hence the entire physical \(X/Y\) multiset equals the exact constant-code
baseline.  \(\square\)

The central owner map is the triangular Latin shear

\[
 \Lambda_h(c,u)=(\rho_{h(u)}c,u),
 \qquad
 \Lambda_h^{-1}(d,u)=(\rho_{h(u)}^{-1}d,u).                    \tag{6.9}
\]

No averaging or fractional selection occurs.

### Proposition 6.2 (frozen-tag necessity)

Within the separated three-piece architecture (6.5), palette uniformity
is not merely a convenient sufficient condition.  Suppose the child port
\(P_u\) is frozen through the exterior prefix, \(J\setminus P_u\) is
frozen through the suffix, \(u\mapsto P_u\) is injective, the child phase
families are pairwise disjoint, and the root/complement tag families obey
(6.2a).  If a filling-dependent code choice preserves the complete
physical lower and upper ledgers, then for every used code and every
filling assigned that code, its prefix and suffix physical palettes must
separately equal the baseline palettes.

#### Proof

Every prefix lower state and upper token has \(J\)-restriction exactly
\(P_u\).  These restrictions are distinct for different \(u\).  Hence a
prefix defect in the fibre tagged by \(P_u\) cannot cancel a defect from
another filling, a suffix defect, or a nonseam child phase: use
injectivity, (6.2a), and phase disjointness, respectively.  The shared
phase-zero seam itself has a code-independent complete central palette.
The equality of the global physical ledger therefore restricts to
equality in every individual \(P_u\)-fibre.  The suffix argument is
identical using the injective tags \(J\setminus P_u\) and the phase-\(r\)
seam.  For upper tokens, exterior-prefix and exterior-suffix edges have
\(J\)-restriction of size \(r\), whereas child edges have
\(J\)-restriction of size \(r+1\), so no hidden cross-piece cancellation
is possible.
\(\square\)

Thus a whole-factor trade with equal *total* \(X/Y\) ledger is not enough:
its two sides must agree separately before and after the child cut.

### Theorem 6.3 (exact fibre formula and regular-action balance)

For fixed exterior root \(c\), a window swallowing the child excursion in
(6.5) has target \(Q_{\rho_{h(u)}c}\), and

\[
 \mu_c(Q_d)=|\{u:\rho_{h(u)}c=d\}|.                            \tag{6.10}
\]

If a finite group \(G\) acts regularly on \(\mathcal C\), the code
alphabet contains \(G\), and \(\rho_g(c)=g\cdot c\), there is one hash
such that, simultaneously for all \(c,d\),

\[
                         \mu_c(Q_d)
                         \le\left\lceil{C_r\over|G|}\right\rceil.
                                                                  \tag{6.11}
\]

#### Proof

The full intersection of the child path \(B_0(u),\ldots,B_r(u)\) is
empty, so its stationary exterior \(Q_{\rho_{h(u)}c}\) is exactly the
swallowed target.  This proves (6.10).

Partition \(\mathcal D_r\) among the elements of \(G\), with class sizes
differing by at most one, and let \(h\) record the class.  For fixed
\(c,d\), regularity gives a unique \(g\) with \(g\cdot c=d\).  Thus
\(\mu_c(Q_d)=|h^{-1}(g)|\), proving (6.11).  \(\square\)

The exact range-capacity inequality is

\[
 \sum_d(\mu_c(Q_d)-p)_+
     \ge (C_r-pM_c)_+,
 \qquad M_c=|\{\rho_a(c):a\in\mathcal A\}|.                   \tag{6.12}
\]

This proves (0.4) for the fixed-phase compiler (6.5).  It controls one
exterior context.  It does not bound collisions between different product
packets or parent contexts.  More generally, if an independently proved
joint compiler supplies \(B_c\) distinct physical target addresses for
that context, including genuinely distinct phase addresses, the universal
capacity condition is \(B_c\ge\lceil C_r/p\rceil\).  Formula (0.4) is the
special case \(B_c=|G|\); arbitrary cyclic row shifts cannot be counted as
extra addresses without a literal joint ownership proof.

## 7. Why the certified local routers do not supply the module

### 7.1 The five-row \(D_3\) pentagon is not split

The two certified exact \(D_3\)-port factors are

\[
\begin{array}{c|c}
\text{old}&
123,136,146,456;\ 124,126,156,356;\ 125,145,345,346;\\
&135,235,245,246;\ 134,234,236,256,\\[1mm]
\text{new}&
123,126,156,456;\ 124,234,345,356;\ 125,235,236,346;\\
&135,136,146,246;\ 134,145,245,256.
\end{array}                                                    \tag{7.1}
\]

Both exhaust all twenty lower states and all fifteen upper tokens, with
fixed roots and complementary endpoints.  Nevertheless they fail the
split condition at every nontrivial cut.

At cut \(k=1\), the phase-one lower palette agrees, but the old prefix
upper palette is

\[
 \{1234,1235,1236,1245,1246\},                                \tag{7.2}
\]

whereas the new prefix upper palette is

\[
 \{1234,1235,1236,1345,1356\}.                                \tag{7.3}
\]

At cut \(k=2\), the phase-two lower palette agrees, but the old suffix
upper palette is

\[
 \{1356,1456,2356,2456,3456\},                                \tag{7.4}
\]

whereas the new suffix upper palette is

\[
 \{1246,1456,2346,2456,3456\}.                                \tag{7.5}
\]

Cuts \(0\) and \(3\) expose only the fixed root or complementary endpoint
palette and have no nontrivial central routing.  By Proposition 6.2, a
child-filling hash cannot choose between the two pentagon factors while
its child port tag remains frozen.  Whole-packet exactness does not repair
the side-resolved upper defects.

### 7.2 Cyclic overlay of the smallest moving \(C_6\)

Let \(x_0,\ldots,x_{\ell-1}\) be distinct exterior coordinates on a
directed cycle, with \(\ell\ge2\), and let \(k,a_0,a_1,a_2\) be common
local coordinates.  For context edge \(x_j\to x_{j+1}\), either shore of
the smallest moving-exterior \(C_6\) has lower states

\[
\begin{aligned}
 S_j^i&=B\cup\{x_j,k,a_i\},\\
 T_j^i&=B\cup\{x_j,a_i,a_{i+1}\},\\
 T_{j+1}^i&=B\cup\{x_{j+1},a_i,a_{i+1}\},
 \qquad i\in\mathbb Z_3.                                    \tag{7.6}
\end{aligned}
\]

### Theorem 7.1 (exact cyclic-overlay obstruction)

In the union of one complete router on every directed context edge, every
\(T_j^i\) occurs exactly twice, so the lower duplicate excess is exactly
\(3\ell\).  The conclusion is independent of all trade-shore choices.

If the two occurrences are identified, \(T_j^i\) has the three incident
upper tokens

\[
                         V_{j-1}^i,\quad U_j^i,\quad V_j^i,     \tag{7.7}
\]

and hence degree three.  If the incidence through \(U_j^i\) is deleted to
retain the directed exterior conveyor, the two consecutive moves are

\[
                         x_{j-1}\mapsto x_j,
                         \qquad x_j\mapsto x_{j+1}.             \tag{7.8}
\]

They have length two but endpoint Johnson distance one when
\(\ell\ge3\), and zero when \(\ell=2\).  Thus the conveyor is not
geodesic.

#### Proof

The terminal triangle state of packet \(j-1\) is literally

\[
 B\cup\{x_j,a_i,a_{i+1}\}=T_j^i,                              \tag{7.9}
\]

the internal triangle state of packet \(j\).  Distinct \((j,i)\) give
distinct states, and no \(S\)-state equals a \(T\)-state because every
\(S\)-state contains \(k\).  This proves the exact multiplicity.

The three incidences in (7.7) are respectively the incoming exterior
collar, the star-to-triangle collar, and the outgoing exterior collar.
Deleting the middle one leaves (7.8), which inserts and then deletes
\(x_j\).  The endpoint-distance calculation proves the last assertion.
\(\square\)

For \(\ell\ge3\) all upper tokens in the complete union are distinct; for
\(\ell=2\) the exterior collars \(V_0^i,V_1^i\) are also duplicated.
Thus no hidden upper cancellation repairs the lower failure.

This theorem closes only the same-triangle direct cycle.  It does not rule
out fresh triangles, rank staggering, a fused compound router, or a true
split module.

### 7.3 Paired \(C_6\) and clean suffix \(C_8\)

The paired star-to-star \(C_6\) has a complete exact local \(X/Y\) ledger
and absolute twists \(\tau,\tau^{-1}\).  It therefore supplies a genuine
two-code bounded prefix router.  On each strand, however, its row-varying
output petal was inserted during that packet.  A following nonidentity
router on the same transported star label must change that petal and hence
remove it.  The same coordinate then has history

\[
                         0\longrightarrow1\longrightarrow0,    \tag{7.10}
\]

which is impossible on a Johnson geodesic.  Changing the common hub does
not change this petal history.  This argument does not rule out routers on
independent tensor labels; such a construction would still need a literal
complementary-shore inverse suffix with code-independent side palettes.

The positive-density clean suffix \(C_8\) bank acts by four-cycles on
distinct strands, but one router has local port displacements

\[
                         (1,1,1,2).                              \tag{7.11}
\]

Indeed its four local roots and their images are

\[
 124\mapsto134,\qquad
 123\mapsto124,\qquad
 125\mapsto123,\qquad
 134\mapsto125,                                                \tag{7.12}
\]

whose Johnson distances are exactly (7.11).  The corresponding abstract
row semilengths are \(r,r+2,r-1,r-1\).
Therefore no single exterior distance can place its four strands at one
equal-length split cut.  Using its actual abstract row lengths instead
would require exterior motions \((1,3,0,1)\), still inconsistent.  A
formal four-copy norm-zero cocycle exists, but its literal crossing seams
and palette-uniform prefix/suffix path covers have not been constructed.
The exact pentagon completion repairs endpoint length and ownership but,
by (7.2)--(7.5), is not the required split module.

These are statewise failures of the present router seeds, not a universal
no-go for larger global braids.

## 8. The exact remaining gate for the split-braid route

For a split module at cut \(k\), define its central distance graph

\[
 \mathcal H_k\subseteq\mathcal C_{\rm root}\times
                         \mathcal C_{\rm centre},
 \qquad
 c\sim d\Longleftrightarrow d_J(R_c,Q_d)=k.                    \tag{8.1}
\]

Every code permutation \(\rho_a\) is a perfect matching in
\(\mathcal H_k\).  If a regular group \(G\) is realized, these matchings
are pairwise edge-disjoint.  Since an \(s\)-set has at most
\({s\choose k}^2\) neighbours at Johnson distance \(k\), a necessary
condition for the isolated fixed-phase regular-action threshold is

\[
                 {s\choose k}^{\!2}
                 \ge |G|
                 \ge\left\lceil{C_r\over p}\right\rceil.       \tag{8.2}
\]

Let

\[
                         W=\binom{2m}{m}                         \tag{8.3}
\]

be the ambient middle width.  We use as an imported, previously verified
input the fixed-frame Gaussian Hall cut: a candidate with all but
\(o(W)\) protected occurrences confined to one physical frame has a
linear target deficit at a fixed Gaussian depth.  This report does not
reprove that outer theorem; the input is the audited fixed-frame part of
MATH_THEOREM_FULL_INTERNAL_QUARTET_ATLAS_GAUSSIAN_HALL_CUT_20260726.md.

A sufficient completion theorem for the split-braid route would construct,
for a growing range of \(r\), all of the following inside one exact
factor.

1. A positive-density family of port-closed product occurrences.
2. On each occurrence, a split exterior braid module with literal
   code-independent prefix and suffix \(X/Y\) palettes.
3. At least \(C_r/p\) legal physical code--phase addresses per protected
   context, and one common all-depth hash loading each address at most
   \(p\), with a simultaneous ownership proof.  A regular central action
   of order at least \(C_r/p\) is the fixed-phase sufficient version.
4. Physical frame motion on \(\Omega(W)\) protected occurrences, as
   required by the imported fixed-frame Gaussian Hall cut.
5. A common all-depth choice whose cross-context collision excess and
   residual owner leave are \(o(W)\).

Items 1--3 are the exact geometric realization of the algebraic shear
(0.2) within architecture (6.5).  Interleaved child/exterior moves and
other cross-block braids lie outside Proposition 6.2 and could provide a
different sufficient architecture.  Items 4--5 are the outer literal Hall
requirement.  Density of local switches, endpoint monodromy, or a balanced
one-context hash alone does not imply them.

## 9. Audit and proved/conditional boundary

The decisive identities were checked independently in the following
ways.

* The product-phase proof was rederived from the pointwise distance sum
  (2.3); it does not use the upper ledger and therefore cannot be repaired
  by an upper-palette cancellation.
* The compiler proof was audited with both seam states subtracted exactly
  once.  The inverse in (6.9) verifies integrality phase by phase.
* The cyclic \(C_6\) indices were independently traced.  Every one of the
  \(3\ell\) triangle states has multiplicity exactly two; for a simple
  context cycle of length at least three, the upper tokens are distinct.
* The Dyck fringe estimate uses the explicit marked Catalan equation
  (4.2), the positive-radius gap (4.3), and stable preorder selection.  No
  independence assumption is used.  An independent audit checked the
  marking equation, the exact radius witness \(17/64\), the carry
  permutation, and the \(2^d\) fibre count.
* The aggregate obstruction is the literal support inequality (5.10).
  It counts physical target labels, not formal hash values.  The audit
  also identified and enforced its necessary fixed-frame and
  fixed-background hypotheses; (5.11) records the exact
  \(L\)-background extension.
* The two pentagon side palettes (7.2)--(7.5) were independently
  recomputed; their failures are upper-token failures, while all phase
  lower palettes agree.

### Proved

1. Fixed-rank synchronized phase hashes freeze the exterior context.
2. A near-spanning set of Dyck ports admits a global boundary carry
   satisfying the exact Latin and displacement equations.
3. At every dimension admitting an exact isometric
   \(C_{2r}\)-factor of \(Q_r\), stable diagonal orientation packets
   realize that cocycle literally, cube by cube.  Their displayed Dyck
   ports hit only the \(o(1)\) fraction (5.5c) of the packet cycles, so
   this is not a near-spanning MSW installation.
4. In one fixed physical frame, if a fixed-background (or an explicitly
   \(L\)-bounded-background) disjoint-fringe occurrence is realized for
   every good root, it has the exponential alphabet obstruction (5.8) or
   (5.11).
5. A palette-uniform split module composes with an arbitrary nonlocal hash
   to an exact integral product packet.
6. Regular actions give the simultaneous fibre bound (6.11).
7. By themselves, the certified pentagon, direct cyclic minimal \(C_6\),
   paired \(C_6\), and clean suffix \(C_8\) do not provide the complete
   split module, for the exact reasons in Section 7.

### Unproved

1. Existence of a growing palette-uniform split exterior router atlas in
   the PBBS/MSW factor.
2. A physical code--phase address range of size at least \(C_r/p\) on
   positive-density port-closed occurrences, together with one
   simultaneous cap-\(p\) hash; in the fixed-phase compiler, a regular
   orbit of that size supplies both.
3. A crossing-frame packing satisfying the full all-depth physical target
   ledger with \(o(W)\) collision excess.
4. The coefficient-one contiguous-OR theorem.

The precise boundary is therefore:

\[
\boxed{
\begin{gathered}
\text{a nonlocal exterior-moving Dyck endpoint cocycle exists, and the}\\
\text{triangular split-module compiler is exact;}\\
\text{the fixed-frame/background fringe realization and all presently certified}\\
\text{local MSW seeds fail to supply a complete global split atlas;}\\
\text{interleaved or root-dependent global braids remain open, and no}\\
\text{coefficient-one conclusion is claimed.}
\end{gathered}}
\]
