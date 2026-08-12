# RP_A: plane-tree sector transport and the obstruction to unrooted rerooting charges

Date: 2026-07-25

Method: pure mathematics only. No web search, computation, or finite search is used.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B_r=\operatorname{Cat}_r,
\]

and let \(\tau=\phi^2\) be the even-time PBBS permutation of Dyck roots of
semilength \(r\). This report identifies the exact plane-tree action of
\(\tau\) and closes the proposed *local unrooted-rerooting charge* route to
\(\mathrm{RP}_A\).

The conclusions are as follows.

1. On the ordinary contour tree, \(\tau\) is a first-deepest-spine
   **sector transport**, not rerooting. Forests on the two sides of that
   spine move in opposite directions, and the terminal root forest crosses
   the root seam. The spatial cocycle is exactly one plus twice the size of
   that terminal root forest.

2. The ordinary contour tree changes unrooted isomorphism type on an
   infinite family. Adding a plant edge does not repair this. The natural
   Stanley--Kreweras noncrossing-incidence tree also changes unrooted degree
   multiset on an infinite family. Thus the ordinary contour, planted, and
   stated Stanley--Kreweras incidence encodings do not turn \(\tau\) into
   rerooting of a fixed unrooted tree.

3. A short omitted-label return has a different exact tree meaning. After
   simultaneous leaf pruning, it is an adjacent-particle passage whose
   final entry is made by the immediate predecessor of the initially
   selected contour particle. The physical separation is the occupancy of
   one distinguished root slot.

4. There is no vanishing contraction for one fixed reduced passage, or for
   any bounded local menu, after normalizing by the entire inverse-pruning
   fibre. For a central gap-seven fibre, a family of quotient-edge-disjoint
   parent intervals all having the same reduced tree, the same five-edge
   passage, and the same complete downstream pruning chain has normalized
   size

   \[
      \frac{1}{18}-o(1).
   \]

   Hence every fixed bounded menu of reduced tree edges or child-return
   marks has congestion bounded away from zero.

5. A uniform per-physical-component vanishing-density statement is false
   even before taking a global limit: one genuine PBBS component of length
   \(3N\) contains

   \[
      2\left\lfloor\frac{3N-1}{9}\right\rfloor
   \]

   pairwise edge-disjoint gap-five intervals. This exceptional component
   is globally negligible, so it is not a counterexample to
   \(\mathrm{RP}_A\).

6. The first viable vanishing-density statement lives instead at the
   two-dimensional Pascal saddle

   \[
      d=\frac r2,
      \qquad k=\frac r6,
   \]

   where \(d\) is the first-pruned rank and \(k\) is the number of peaks of
   the pruned core. \(\mathrm{RP}_A\) forces the Gaussian-weighted density
   of bounded-slot predecessor passages across every fixed saddle tube to
   tend to zero. This is an aggregate, peak- and slot-weighted theorem on
   long parent-rank quotient cycles; it is not supplied by an unrooted-tree
   invariant.

The numerical residence theorem remains open. What is closed here is the
specific rerooting/orbit-edge architecture, including every uniform local
fixed-core capacity-normalized version.

## 1. Dyck quotient normalization

For a Dyck word \(D\in\mathcal D_r\), mark the first up-step which reaches
the global maximum and write

\[
 D=P\,1\,Q.
\]

Put

\[
 \delta(D)=|P|+1,
 \qquad
 \phi(D)=\overline Q\,0\,\overline P,
\tag{1.1}
\]

where the bar interchanges zero and one. If \(u\in\mathbb Z_N\) is the
coordinate of the unmatched zero, one PBBS step is

\[
 (u,D)\longmapsto
 (u+\delta(D)\pmod N,\phi D).
\tag{1.2}
\]

Refine the marked factorization by taking the displayed zero to be the
first return to height zero after the marked up-step:

\[
 D=P\,1\,R\,0\,S.
\tag{1.3}
\]

Then \(S\) is Dyck and direct substitution in (1.1) gives

\[
 \boxed{
 \begin{aligned}
  \delta(D)&=|P|+1,\\
  \delta(\phi D)&=|R|+1,\\
  \tau D:=\phi^2D&=S\,1\,P\,0\,R.
 \end{aligned}}
\tag{1.4}
\]

Since

\[
 |P|+1+|R|+1+|S|=2r=N-1,
\]

putting

\[
 d_0(D)=|S|+1
\tag{1.5}
\]

gives the exact even-time skew product

\[
 \boxed{
 (u,D)\longmapsto
 (u-d_0(D)\pmod N,\tau D).}
\tag{1.6}
\]

After quotienting the step-two factor by coordinate rotation, directed
edges are indexed by the \(B_r\) Dyck roots. If \(H\log N=o(r)\), the
number \(Z_H\) of quotient edges on cycles of length at most \(H+1\)
satisfies

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(r)).
\tag{1.7}
\]

On the remaining cycles, let \(\overline\nu_H\) be the maximum number of
pairwise quotient-edge-disjoint nonwrapping residence intervals. The deck
inequality

\[
 N\overline\nu_H\le \nu_H(P_r)
\tag{1.8}
\]

shows that, for fixed \(A>0\) and

\[
 H_A=\lceil A\sqrt r\rceil,
\]

the physical assertion \(\nu_{H_A}(P_r)=o_A(B_r)\) requires

\[
 \boxed{
 \overline\nu_{H_A}=o_A(B_r/N).}
\tag{1.9}
\]

This is the scale used below.

## 2. Exact action on the contour plane tree

Let \(T(D)\) be the rooted ordered plane tree whose contour word is \(D\).
Let

\[
 v_0,v_1,\ldots,v_h
\]

be the path from the root \(v_0\) to the first deepest leaf encountered by
the contour. At \(v_i\), \(0\le i<h\), split the ordered children around
the path child \(v_{i+1}\). Let \(\mathcal A_i\) be the child forest before
\(v_{i+1}\), and let \(\mathcal B_i\) be the child forest after it. Write
\(A_i,B_i\) for their concatenated contour words.

### Theorem 2.1 (first-deepest-spine sector transport)

The contour has the exact form

\[
 \boxed{
 D=A_0\,1\,A_1\,1\cdots1\,A_{h-1}\,1\,0B_{h-1}0\cdots0B_1\,0B_0.}
\tag{2.1}
\]

Moreover \(A_{h-1}=\varnothing\), and

\[
 \boxed{
 \tau D
 =B_0\,1\,A_0\,1\,A_1\,1\cdots1\,A_{h-1}
   \,0\,0B_{h-1}0\cdots0B_1.}
\tag{2.2}
\]

If \(b_0(T)=|E(\mathcal B_0)|\), then the even-time cocycle is

\[
 \boxed{d_0(D)=2b_0(T(D))+1.}
\tag{2.3}
\]

When \(h=1\), the displayed ranges
\(B_{h-1},\ldots,B_1\) are empty; the terminal forest \(B_0\) occurs only
in its separately displayed position.

#### Proof

At each spine vertex, the contour first traverses \(\mathcal A_i\), then
descends the spine edge, and, after returning on that edge, traverses
\(\mathcal B_i\). This gives (2.1). An earlier child of \(v_{h-1}\)
would itself be a leaf at depth \(h\), encountered before \(v_h\), so
\(A_{h-1}=\varnothing\).

The last displayed up-step in (2.1) is exactly the first step attaining
height \(h\). In the factorization (1.3), therefore,

\[
 \begin{aligned}
 P&=A_0\,1\,A_1\,1\cdots1\,A_{h-1},\\
 R&=0B_{h-1}0\cdots0B_1,\\
 S&=B_0.
 \end{aligned}
\]

Here the displayed expression for \(R\) is empty when \(h=1\).

Substitution in \(\tau D=S1P0R\) proves (2.2). Finally
\(|B_0|=2|E(\mathcal B_0)|\), and (2.3) follows from (1.5). \(\square\)

Formula (2.2) has a literal geometric reading. Every \(\mathcal A_i\)
moves from depth \(i\) to depth \(i+1\). Every \(\mathcal B_i\),
\(1\le i<h\), moves from depth \(i\) to depth \(i-1\). The terminal
root forest \(\mathcal B_0\) crosses the root seam. This is a cut-and-graft
sector transport, not a change of root in a fixed tree.

The final odd step also has a tree expression. Since

\[
 |P|+1=h+2\sum_{i=0}^{h-1}|E(\mathcal A_i)|,
\]

define

\[
 \delta(T)=h+2\sum_{i=0}^{h-1}|E(\mathcal A_i)|.
\tag{2.4}
\]

For \(T_j=T(\tau^jD)\), an omitted-label return after \(2s+1\) PBBS
steps is equivalent to

\[
 \boxed{
 \sum_{j=0}^{s-1}\bigl(2b_0(T_j)+1\bigr)
 \equiv \delta(T_s)\pmod N.}
\tag{2.5}
\]

Equivalently, for a unique integer \(w\ge0\),

\[
 \sum_{j=0}^{s-1}\bigl(2b_0(T_j)+1\bigr)
 =\delta(T_s)+wN.
\tag{2.6}
\]

It is the first return exactly when the corresponding congruence fails at
every earlier time. Thus a return compares root-sector sizes along a
sequence of topology-changing trees; it is not the return of a root to an
edge of one fixed unrooted tree.

### Corollary 2.2 (ordinary and planted rerooting are impossible)

There is a particularly transparent all-rank family. For \(d\ge3\), put

\[
 E_d=(10)^{d-2}1100=E(d-2,1,0)
\]

in the notation of Section 3. Formula (3.4) below gives

\[
 \tau E_d=1(10)^{d-1}0.
\tag{2.7}
\]

The first contour tree is a broom: the root has \(d-2\) leaf children and
one final child which itself has one leaf child. The second is a star rooted
at one of its leaves. Their unrooted degree multisets are

\[
 \{d-1,2,1^{\,d-1}\}
 \quad\text{and}\quad
 \{d,1^d\},
\tag{2.8}
\]

so they are nonisomorphic for every \(d\ge3\).

For \(r\ge3\), put

\[
 D_r^\star=110100(10)^{r-3}.
\tag{2.9}
\]

Then

\[
 \tau D_r^\star=(10)^{r-3}110010.
\tag{2.10}
\]

The unrooted degree multisets of the two contour trees are

\[
 \{r-2,3,1^{\,r-1}\}
 \quad\text{and}\quad
 \{r-1,2,1^{\,r-1}\},
\tag{2.11}
\]

respectively. They differ for \(r=3\) and for every \(r\ge5\). Hence
\(\tau\) is not rerooting of the ordinary unrooted contour tree.

Adding a plant leaf does not repair the action. Indeed,

\[
 10110010\overset{\tau}{\longmapsto}10110100,
\tag{2.12}
\]

while the planted unrooted degree multisets are

\[
 \{4,2,1,1,1,1\}
 \quad\text{and}\quad
 \{3,3,1,1,1,1\}.
\tag{2.13}
\]

The shape change can be made to occur at the start of a genuine short
return. For \(d\ge3\) and \(r\ge2d-1\), set

\[
 \widehat D_{r,d}
 =(10)^{r-(2d-1)}(1100)^{d-2}111000.
\tag{2.14}
\]

Its first maximum occurs in the final mountain, and (2.2) gives

\[
 \tau\widehat D_{r,d}
 =1(10)^{r-(2d-1)}(1100)^{d-2}11000.
\tag{2.15}
\]

The two unrooted degree multisets are

\[
 \{r-d,2^d,1^{\,r-d}\}
 \quad\text{and}\quad
 \{r-d+1,2^{d-1},1^{\,r-d+1}\},
\tag{2.16}
\]

whose maximum degrees differ. Moreover,
\(\partial\widehat D_{r,d}=E_d\) and
\(\widehat D_{r,d}\) has empty final root slot. The exact predecessor-slot
criterion of Section 4 therefore makes \(\widehat D_{r,d}\) a gap-seven
return root. Thus topology change occurs inside the short-return class
itself, not only elsewhere in the PBBS state space.

At \(r=4\), the three words

\[
 11010010,
 \quad10110100,
 \quad10110010
\]

form an exact three-cycle under \(\phi\), and hence also under
\(\tau=\phi^2\). A fixed next-corner rerooting on an \(r\)-edge plane
tree has order dividing \(2r=8\); after adding a plant edge its order
divides \(2(r+1)=10\). Thus \(\tau\) is not conjugate to either canonical
cyclic rerooting action.

## 3. The noncrossing-incidence tree also changes

One might hope that (2.2) is rerooting after replacing the contour tree by
the natural noncrossing-partition incidence tree. The next theorem rules
this out on an infinite family.

Label the up-steps of \(D\in\mathcal D_d\) by \(1,\ldots,d\) from left
to right. Match down-steps to up-steps as parentheses. For every maximal
descent, form the block of labels on the up-steps matched to that descent.
These blocks form the noncrossing partition \(\pi(D)\). Regard \(\pi\) as
a permutation whose cycles are its blocks in cyclic increasing order, put

\[
 \gamma=(1\,2\,\cdots\,d),
 \qquad
 \kappa=\pi^{-1}\gamma,
\tag{3.1}
\]

and form the bipartite incidence graph \(\mathcal K(D)\): black vertices
are cycles of \(\pi\), white vertices are cycles of \(\kappa\), and edge
\(i\) joins the two cycles containing \(i\). The identity
\(\pi\kappa=\gamma\) makes this graph connected, while the noncrossing
cycle identity

\[
 \#\operatorname{cyc}(\pi)+\#\operatorname{cyc}(\kappa)=d+1
\]

shows that its \(d\) edges join \(d+1\) vertices. Hence it is a plane
bipartite tree. Its vertex degrees are the corresponding cycle sizes.

For \(a,c\ge0\), \(b\ge1\), and \(a+b+c=d-1\), put

\[
 E(a,b,c)=(10)^a\,1(10)^b0\,(10)^c.
\tag{3.2}
\]

### Theorem 3.1 (infinite incidence-tree obstruction)

For (3.2),

\[
 \pi(E(a,b,c))=(a+1,\,a+b+1)
\tag{3.3}
\]

with every other point fixed, and

\[
 \boxed{
 \phi E(a,b,c)=E(b-1,c+1,a),
 \qquad
 \tau E(a,b,c)=E(c,a+1,b-1).}
\tag{3.4}
\]

For every \(d\ge4\), take

\[
 D_d=E(0,2,d-3)=110100(10)^{d-3}.
\tag{3.5}
\]

Then \(\mathcal K(D_d)\) and \(\mathcal K(\tau D_d)\) are nonisomorphic
even after forgetting the root and the bipartite colors.

#### Proof

All descents in (3.2) are singletons except the two-step descent formed by
the last zero of the final middle peak and the displayed extra zero. Its
two matching up-steps have labels \(a+b+1\) and \(a+1\), proving (3.3).

The first maximum-reaching up-step has

\[
 P=(10)^a1,
 \qquad
 Q=0(10)^{b-1}0(10)^c.
\]

Substituting into \(\phi(D)=\overline Q0\overline P\), using
\(1(01)^t=(10)^t1\) and \((01)^t0=0(10)^t\), gives the first identity in
(3.4); applying it twice gives the second.

For \(D_d\), the unique nontrivial black block is \(\{1,3\}\), whose
cyclic separation is two. For \(\tau D_d=E(d-3,1,1)\), it is
\(\{d-2,d-1\}\), whose separation is one.

If \(\pi\) is one transposition of cyclic separation \(s\), rotate labels
so it is \((1,s+1)\). Direct multiplication gives

\[
 \pi^{-1}\gamma
 =(1\,2\,\ldots\,s)(s+1\,s+2\,\ldots\,d).
\tag{3.6}
\]

Thus the white-degree multisets of the two incidence trees are

\[
 \{2,d-2\}
 \quad\text{and}\quad
 \{1,d-1\},
\tag{3.7}
\]

while both black-degree multisets are \(\{2,1^{d-2}\}\). For \(d=4\),
the uncolored total degree multisets are

\[
 \{2,2,2,1,1\}
 \quad\text{and}\quad
 \{3,2,1,1,1\}.
\]

For \(d\ge5\), the maximum degrees are \(d-2\) and \(d-1\). Therefore
the unrooted uncolored trees are nonisomorphic. \(\square\)

Color swapping, reflection, and the opposite Kreweras convention cannot
repair a difference in the uncolored degree multiset. Hence the natural
incidence tree supplies no hidden rerooting invariant.

## 4. The actual tree mark: a predecessor slot after leaf pruning

Simultaneous Dyck-peak deletion is simultaneous deletion of every leaf edge
of the contour tree. Let

\[
 E=\partial D\in\mathcal D_d,
 \qquad k=\operatorname{pk}(E),
 \qquad p=2d+1.
\tag{4.1}
\]

Every inverse tree is obtained from the core tree \(T(E)\) by inserting
new leaf children in its ordered child slots. A vertex with \(c\) existing
children has \(c+1\) slots, so the total number of slots is

\[
 \sum_v(\deg^+(v)+1)=d+(d+1)=2d+1.
\tag{4.2}
\]

Every old core leaf must receive at least one new child. After removing
these \(k\) mandatory leaves, the free slot vector is

\[
 \mathbf n=(n_0,\ldots,n_{p-1})\in\mathbb Z_{\ge0}^{p},
 \qquad
 \sum_jn_j=r-d-k.
\tag{4.3}
\]

Here \(n_0=z_*(D)\) is the occupancy of the final root slot, after the
last existing root child. Consequently the full inverse-fibre capacity is

\[
 \boxed{
 P_r(E)=\binom{r+d-k}{2d}.}
\tag{4.4}
\]

The \(p\) equality particles of the physical word are the distinguished
root contour site together with the directed contour sites of \(E\). Label
them cyclically so that particle \(0\) is selected at time zero and
particle \(-1\) is its immediate predecessor. Let

\[
 \kappa_t(E)\in\mathbb Z_p
\]

be the selected particle at time \(t\) in the reduced PBBS, with
\(\kappa_0=0\), and put

\[
 C_j(g)=\#\{0\le t<g:\kappa_t(E)=j\}.
\tag{4.5}
\]

### Theorem 4.1 (short return = predecessor passage = final root slot)

Assume \(d\ge1\) and \(g<N\). A lift \(D\) of \(E\) has its next
occurrence of the time-zero omitted physical label exactly at time \(g\)
if and only if

\[
 \boxed{
 \begin{aligned}
  &\kappa_g(E)=-1,\\
  &\kappa_h(E)=0\quad\text{for some }1\le h<g,\\
  &C_{-1}(g)=2z_*(D)+1.
 \end{aligned}}
\tag{4.6}
\]

For a reduced passage prescribing \(z=z_E(g)\), the exact number of
parent starts is

\[
 \boxed{
 K_r(E,z)
 =\binom{r+d-k-z-1}{2d-1}.}
\tag{4.7}
\]

#### Proof

The two particles \(-1,0\) initially have physical separation

\[
 q_0=2z_*(D)+1.
\tag{4.8}
\]

Indeed, with an empty final root slot they occupy adjacent physical contour
edges. Every extra terminal leaf appends one peak \(10\) and increases the
separation by two.

At time zero, particle \(0\) enters the physical edge whose label is to
return. Before time \(N\), cyclic particle order is preserved and no
particle can make a full circuit. Hence only the immediate predecessor
\(-1\) can be responsible for the next returned occurrence. Particle \(0\)
must first be selected again and vacate the edge.

More precisely, if \(x_j(t)\) is the physical edge occupied by particle
\(j\) immediately before update \(t\), then

\[
 x_j(t)=x_j(0)+C_j(t),
 \qquad
 \lambda_t=x_{\kappa_t}(t)+1
\]

on compatible integer lifts. Since
\(q_0=x_0(0)-x_{-1}(0)\), the equality
\(\lambda_g=\lambda_0\) is exactly
\(\kappa_g=-1\) and \(C_{-1}(g)=q_0\). The intervening reselection of
particle \(0\) is exactly the second line of (4.6). The same
no-overtaking argument shows that no earlier particle can create the
returned occurrence. Notice that \(C_{-1}(g)\) counts the \(q_0\)
predecessor moves strictly before time \(g\); the selection at time \(g\)
is the following selection, at which the returning omitted label is read.

Condition (4.6) fixes exactly the single slot \(n_0=z\). The remaining
\(2d\) slots form a weak composition of \(r-d-k-z\), giving (4.7).
\(\square\)

The first reselection of particle \(0\) is itself a return event in the
PBBS on \(\partial D\). Repeating the argument gives nested adjacent-particle
passages on

\[
 T(D),\quad \partial T(D),\quad \partial^2T(D),\ldots.
\]

The marked contour particle changes from level to level. There is no
single unrooted tree edge being revisited.

## 5. Exact capacity projection and its sharp local failure

Peak deletion is a semiconjugacy:

\[
 \partial(\tau D)=\tau(\partial D).
\tag{5.1}
\]

The restrictions of \(\tau\) therefore give bijections between successive
inverse fibres along every reduced \(\tau\)-orbit.

Let \(\mathcal P\) be any pairwise quotient-edge-disjoint family of
nonwrapping rank-\(r\) short-return intervals. For a reduced transition
edge \(e\), count projected occurrences with multiplicity and call the
result \(L_e(\mathcal P)\).

### Theorem 5.1 (exact capacitated mass transport)

For every reduced edge \(e\),

\[
 \boxed{L_e(\mathcal P)\le P_r(e),}
\tag{5.2}
\]

and

\[
 \boxed{
 \sum_eL_e(\mathcal P)=\sum_{I\in\mathcal P}|I|,
 \qquad
 \sum_eP_r(e)=B_r.}
\tag{5.3}
\]

In particular,

\[
 \sum_{I\in\mathcal P}|I|\le B_r.
\tag{5.4}
\]

#### Proof

A parent quotient edge above \(e\) is determined uniquely by \(e\) and
its inverse-tree slot vector. Semiconjugacy transports that vector
bijectively along the reduced trace. Because the parent intervals are
edge-disjoint, all slot vectors counted above a fixed reduced occurrence
are distinct; there are at most \(P_r(e)\). This proves (5.2). Double
counting parent trace edges proves the first identity in (5.3). The inverse
fibres partition \(\mathcal D_r\), proving the second. \(\square\)

The universal estimate (5.4) has no pointwise \(o(1)\) improvement.

### Theorem 5.2 (constant normalized congestion over one reduced passage)

Let

\[
 E_d=(10)^{d-2}1100,
 \qquad d\ge2.
\tag{5.5}
\]

This core has \(k=d-1\) peaks and a gap-seven predecessor passage with
\(z=0\). Hence

\[
 P_r(E_d)=\binom{r+1}{2d},
 \qquad
 K_r(E_d,0)=\binom r{2d-1},
\tag{5.6}
\]

and

\[
 \boxed{
 \frac{K_r(E_d,0)}{P_r(E_d)}=\frac{2d}{r+1}.}
\tag{5.7}
\]

Choose \(d=d(r)\) with \(2d-1=r/2+O(1)\). Assume
\(H\ge4\) and \(H\log N=o(r)\). After discarding parent starts on quotient
cycles of length at most \(H+1\), the remaining gap-seven intervals contain a
pairwise quotient-edge-disjoint family \(\mathcal P_{r,d}\) such that

\[
 \boxed{
 \frac{|\mathcal P_{r,d}|}{P_r(E_d)}
 \ge\frac1{18}-o(1).}
\tag{5.8}
\]

Every member has the same reduced five-edge passage and

\[
 \partial D=E_d,
 \qquad
 \partial^2D=10,
 \qquad
 \partial^3D=\varnothing.
\tag{5.9}
\]

#### Proof

Equation (5.7) is the quotient of the two binomial coefficients in (5.6),
and tends to \(1/2\) under the stated choice of \(d\). A gap-seven
residence interval uses five consecutive quotient edges. On a long cycle,
one such interval can conflict only with starts at the four preceding, its
own, and the four following edge positions. Greedy selection therefore
retains at least one ninth of the starts. The discarded short-cycle term
is \(Z_H=\exp(o(r))\), whereas \(K_r(E_d,0)=\exp((\log2+o(1))r)\).
Thus

\[
 |\mathcal P_{r,d}|
 \ge\frac19(K_r(E_d,0)-Z_H)
 =\left(\frac1{18}-o(1)\right)P_r(E_d).
\]

The gap-seven classification gives \(\partial D=E_d\), and direct peak
deletion gives \(\partial E_d=10\). Semiconjugacy makes the complete
reduced ordered trace identical for every lift. \(\square\)

### Corollary 5.3 (bounded local tree-edge menus cannot contract)

Suppose every parent in Theorem 5.2 is charged to one element of a fixed
menu of at most \(C\) marks determined by its reduced passage, where \(C\)
is independent of \(r\). Then one mark receives at least

\[
 \left(\frac1{18C}-o(1)\right)P_r(E_d)
\tag{5.10}
\]

charges. This applies to the distinguished child return, the predecessor
return, their complete two-level pruning trace, or any bounded menu of
canonical reduced tree edges.

The conclusion does **not** rule out an artificial slot-vector-dependent
assignment spread over \(\Theta(d)\) unrelated edges. Constructing such an
assignment with globally bounded capacities would be a new capacitated
Hall theorem; it is not a rerooting invariant furnished by the return
geometry.

There is also a sharp statement when the menu is enlarged to the full edge
or corner set of the fixed reduced core. An arbitrary assignment of the
members of \(\mathcal P_{r,d}\) to the \(d\) edges of \(T(E_d)\) has some
edge of load at least

\[
 \boxed{
 \left(\frac1{18}-o(1)\right)\frac{P_r(E_d)}d.}
\tag{5.11}
\]

Since a \(d\)-edge plane tree has exactly \(2d\) corners, an arbitrary
assignment to all its corners has some corner of load at least

\[
 \boxed{
 \left(\frac1{36}-o(1)\right)\frac{P_r(E_d)}d.}
\tag{5.12}
\]

Thus even the complete fixed-core edge or corner menu cannot satisfy a
uniform \(o(P_r(E)/d)\) congestion theorem. This remains a local
obstruction: the exceptional gap-seven fibre is exponentially negligible
relative to \(B_r/N\), so a global theorem may still give it exceptional
weight.

## 6. Uniform per-physical-component vanishing density is false

There is an independent obstruction to every theorem asserted separately
on each PBBS orbit.

### Theorem 6.1 (one component with density \(2/9\))

For every \(r\ge3\), the canonical PBBS has a component of exact length
\(3N\) containing at least

\[
 \boxed{
 2\left\lfloor\frac{3N-1}{9}\right\rfloor}
\tag{6.1}
\]

pairwise step-two-edge-disjoint gap-five residence intervals.

#### Proof

Put

\[
 \begin{aligned}
 D_0&=11(01)^{r-2}00,\\
 D_1&=(10)^{r-2}1100,\\
 D_2&=110(01)^{r-2}0.
 \end{aligned}
\tag{6.2}
\]

Direct use of (1.1) gives the exact \(\phi\)-cycle

\[
 D_0\longmapsto D_1\longmapsto D_2\longmapsto D_0
\]

with voltages

\[
 2,\quad N-3,\quad2.
\]

Their sum is \(N+1\equiv1\pmod N\), so the lift is one component of
length \(3N\). At times \(3j,3j+1,3j+2\), its omitted labels are

\[
 u+j,
 \qquad u+j+2,
 \qquad u+j-1
 \pmod N.
\tag{6.3}
\]

Starts in phases zero and one therefore have next equal-label gap exactly
five. Each associated residence interval uses four step-two edges. Put

\[
 J=\left\lfloor\frac{3N-1}{9}\right\rfloor.
\]

For \(0\le j<J\), choose the starts \(3+9j\) and \(4+9j\). Their
step-two edge sets are

\[
 \{2,4,6,8\}+9j,
 \qquad
 \{3,5,7,9\}+9j.
\]

These \(2J\) sets are pairwise disjoint and avoid the circular seam,
which proves (6.1). \(\square\)

The density in (6.1), relative to the \(3N\) step-two edges of this
component, tends to \(2/9\). Thus no hereditary vanishing-density theorem
imposed on every physical PBBS component, or on a certificate constant on
that entire component, can be true.

This component projects to a short quotient cycle and is removed by the
\(Z_H\) term. Likewise the exact global start counts

\[
 R_5(r)=r-1,
 \qquad
 R_7(r)=2^{r-1}-r
\tag{6.4}
\]

give only \(\Theta(N2^r)=o(B_r)\) physical gap-seven packing mass. Neither
Theorem 5.2 nor Theorem 6.1 is a counterexample to \(\mathrm{RP}_A\).
They disprove local and uniform orbitwise proof architectures, not the
aggregate long-orbit assertion.

## 7. The exact surviving vanishing-density target: the Pascal saddle

For a first-pruned core of semilength \(d\) with \(k\) peaks, the number
of such cores and the inverse-fibre capacity are

\[
 \mathsf N(d,k)=\frac1d\binom dk\binom d{k-1},
 \qquad
 P_r(d,k)=\binom{r+d-k}{2d}.
\tag{7.1}
\]

Thus the exact outer mass above the cell \((d,k)\) is

\[
 \boxed{
 \mathsf M_r(d,k)
 =\frac1d\binom dk\binom d{k-1}
  \binom{r+d-k}{2d}.}
\tag{7.2}
\]

These masses partition \(B_r\), apart from the elementary fully pruned
boundary cell.

The exponential saddle of (7.2) is

\[
 d=\frac r2,
 \qquad
 k=\frac r6.
\tag{7.3}
\]

If

\[
 u=\frac{k-r/6}{\sqrt r},
 \qquad
 v=\frac{d-r/2}{\sqrt r},
\]

then, uniformly for bounded \(u,v\), Stirling expansion gives

\[
 \boxed{
 \frac{\mathsf M_r(d,k)}{B_r}
 =\frac{9\sqrt2}{2\pi r}
 \exp\!\left[-\frac{81u^2-18uv+33v^2}{8}\right]
 (1+o(1)).}
\tag{7.4}
\]

Indeed, the entropy exponent is

\[
 \mathsf h(t)=-t\log t-(1-t)\log(1-t),
\]

and

\[
 F(x,y)=2y\mathsf h(x/y)
 +(1+y-x)\mathsf h\!\left(\frac{2y}{1+y-x}\right),
\]

with \((x,y)=(k/r,d/r)\), and its negative Hessian at
\((1/6,1/2)\) is

\[
 \frac14
 \begin{pmatrix}81&-9\\-9&33\end{pmatrix},
 \qquad \det=162.
\]

Prescribing a fixed final slot \(z\) retains the exact fraction

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\frac{2d}{r+d-k}
  \prod_{j=0}^{z-1}
  \frac{r-d-k-j}{r+d-k-1-j},
\tag{7.5}
\]

and hence, at the saddle,

\[
 \boxed{
 \frac{K_r(d,k,z)}{P_r(d,k)}
 \longrightarrow \frac34\,4^{-z}.}
\tag{7.6}
\]

This shows why fixing the return slot does not create an exponential loss
in the dangerous region.

We can state the exact necessary vanishing-density condition in the full
two-dimensional saddle. Fix \(A,a>0\) and an integer \(z_0\ge0\), and put

\[
 H=A\sqrt r+O(1).
\]

For every cell

\[
 \left|d-\frac r2\right|\le a\sqrt r,
 \qquad
 \left|k-\frac r6\right|\le a\sqrt r,
\tag{7.7}
\]

let \(\eta_r(d,k)\) be the fraction of cores
\(E\in\mathcal D_d\) with \(\operatorname{pk}(E)=k\) which admit some
predecessor passage

\[
 g\le2H-1,
 \qquad z_E(g)\le z_0.
\tag{7.8}
\]

Set

\[
 u_{d,k}=\frac{k-r/6}{\sqrt r},
 \qquad
 v_d=\frac{d-r/2}{\sqrt r},
 \qquad
 Q(u,v)=81u^2-18uv+33v^2,
\tag{7.9}
\]

and

\[
 S_r(a,z_0)=
 \frac1{\sqrt r}
 \sum_{\substack{|d-r/2|\le a\sqrt r\\
                   |k-r/6|\le a\sqrt r}}
 \eta_r(d,k)e^{-Q(u_{d,k},v_d)/8}.
\tag{7.10}
\]

### Theorem 7.1 (two-dimensional saddle-passage lower bound)

\[
 \boxed{
 \frac{r\,\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A\,4^{z_0}}+o(1)\right)
 S_r(a,z_0)-o(1).}
\tag{7.11}
\]

Consequently, the quotient conclusion
\(\overline\nu_H=o(B_r/N)\), and hence \(\mathrm{RP}_A\), requires

\[
 \boxed{S_r(a,z_0)\longrightarrow0}
\tag{7.12}
\]

for every fixed \(a,z_0\).

#### Proof

For every qualifying core choose one passage satisfying (7.8). Its parent
start hyperplane has at least \(K_r(d,k,z_0)\) elements, because (4.7)
decreases with \(z\). Equations (7.4) and (7.6), uniformly in the fixed
two-dimensional tube, show that the total number of resulting parent starts
is at least

\[
 \left(\frac{27\sqrt2}{8\pi\,4^{z_0}}+o(1)\right)
 \frac{B_r}{r}
 \sum_{(d,k)\ {\rm in}\ (7.7)}
 \eta_r(d,k)e^{-Q(u_{d,k},v_d)/8}.
\tag{7.13}
\]

Different cores have disjoint inverse fibres. Discarding all starts on
short parent quotient cycles costs \(Z_H=\exp(o(r))\). After the final
greedy division and normalization, this contributes at most

\[
 \frac{rZ_H}{(2H+1)B_r}=o(1).
\]

Every remaining interval uses at most \(H+1\) quotient edges. On each long cycle, one interval can
conflict only with starts among at most \(H\) preceding, its own, and at
most \(H\) following edge positions. Variable-length greedy packing keeps
at least a \((2H+1)^{-1}\) fraction. Dividing (7.13) by
\(2H+1=2A\sqrt r+o(\sqrt r)\), multiplying by \(r/B_r\), and using
the uniform saddle asymptotic proves (7.11). Since
\(N=(2+o(1))r\), (7.12) follows from
\(\overline\nu_H=o(B_r/N)\). Equivalently, if (7.12) failed, pass to a
subsequence on which \(S_r(a,z_0)\) is bounded below and apply (7.11).
\(\square\)

For orientation, restrict to the single lattice line
\(k=\lfloor r/6\rfloor\). If \(\eta_r(d,k)\ge\eta>0\) for every
\(|d-r/2|\le a\sqrt r\), then (7.11) gives

\[
 \liminf_{r\to\infty}\frac{r\overline\nu_H}{B_r}
 \ge
 \frac{27\sqrt2\,\eta}{4\pi A\,4^{z_0+1}}
 \int_{-a}^{a}e^{-33v^2/8}\,dv>0.
\tag{7.14}
\]

Deck lifting then gives a physical \(\Omega_A(B_r)\) packing, contrary to
\(\mathrm{RP}_A\).

Condition (7.12) is averaged. It does not require pointwise vanishing in
every single lattice cell: one cell carries only \(\Theta(B_r/r)\) outer
mass, and the Gaussian-window greedy loss is \(\Theta(\sqrt r)\). The
two-dimensional tube contains \(\Theta(r)\) cells, so the critical demand
is much stronger than a rank-only or one-curve assertion.

The fixed-\(z_0\) statement can be strengthened to retain every
nonnegligible slot layer at once. Put

\[
 L_r=\lceil3\log r\rceil,
\]

and let \(\eta_r(d,k;z)\) be the fraction of cores in the cell \((d,k)\)
which admit a predecessor passage \(g\le2H-1\) prescribing the exact slot
\(z\). Define

\[
 S_r^\ast(a)=
 \frac1{\sqrt r}
 \sum_{\substack{|d-r/2|\le a\sqrt r\\
                   |k-r/6|\le a\sqrt r}}
 e^{-Q(u_{d,k},v_d)/8}
 \sum_{z=0}^{L_r}4^{-z}\eta_r(d,k;z).
\tag{7.15}
\]

### Corollary 7.2 (all surviving slot layers)

\[
 \boxed{
 \frac{r\,\overline\nu_H}{B_r}
 \ge
 \left(\frac{27\sqrt2}{16\pi A}+o(1)\right)
 S_r^\ast(a)-o(1).}
\tag{7.16}
\]

Consequently \(\mathrm{RP}_A\) requires

\[
 \boxed{S_r^\ast(a)\longrightarrow0}
\tag{7.17}
\]

for every fixed \(a>0\).

#### Proof

For a fixed reduced core, two different predecessor passages cannot
prescribe the same \(z\): otherwise every parent root in that one slot
hyperplane would have two different next-return times. Hyperplanes with
different \(z\)'s are disjoint. We may therefore choose and sum all exact
slot layers without double-counting parent starts.

Uniformly in the saddle tube and for \(0\le z\le L_r=O(\log r)\), the
exact product (7.5) gives

\[
 \frac{K_r(d,k,z)}{P_r(d,k)}
 =\left(\frac34+o(1)\right)4^{-z},
\tag{7.18}
\]

because every factor differs from \(1/4\) by
\(O(r^{-1/2}+(z+1)/r)\), uniformly in the fixed saddle tube, and there
are only \(O(\log r)\) factors. Summing
(7.18), using the cell asymptotic (7.4), deleting the single global
short-cycle set \(Z_H\), and applying the same \((2H+1)^{-1}\) greedy
bound as in Theorem 7.1 proves (7.16). Equation (7.17) follows from the
quotient target exactly as before. \(\square\)

## 8. A further exact reduction and the remaining gate

The Pascal kernel removes two regions before any global orbit theorem is
needed.

First, the number of outer roots whose first-pruned rank satisfies
\(d\le r/4\) is exponentially small relative to \(B_r\). Indeed, this
number is

\[
 \sum_{d\le r/4}\frac1r\binom rd\binom r{d+1},
\tag{8.1}
\]

and the entropy bound is

\[
 \exp(2r\mathsf h(1/4)+o(r))
 =e^{-c r}B_r
\tag{8.2}
\]

for some absolute \(c>0\), since \(\mathsf h(1/4)<\log2\).

Second, condition on a core of rank \(d\ge r/4\). With
\(y=r-d-k\), the uniform inverse fibre is the weak-composition simplex
(4.3), and

\[
 \Pr(n_0\ge L)
 =\frac{\binom{y-L+2d}{2d}}{\binom{y+2d}{2d}}
 \le\left(\frac35\right)^L.
\tag{8.3}
\]

The inequality follows from \(y\le3r/4\) and \(2d\ge r/2\). Taking

\[
 L=\lceil3\log r\rceil
\]

and summing over all cores gives

\[
 \#\{D:d\ge r/4,\ n_0\ge L\}
 \le(3/5)^L B_r=o(B_r/N).
\tag{8.4}
\]

Thus, after discarding \(o(B_r/N)\) possible starts, every member of a
short-return packing satisfies

\[
 \boxed{
 d\ge r/4,
 \qquad
 z_*(D)\le\lceil3\log r\rceil,
 \qquad
 C_{-1}(g)\le6\log r+O(1).}
\tag{8.5}
\]

An orbit invariant supplied here by the tree hierarchy is the
iterated pruning-rank profile

\[
 \bigl(|\partial^jD|/2\bigr)_{j\ge0},
\tag{8.6}
\]

because \(\partial\tau=\tau\partial\). The shape-change theorems show that
there is no canonical invariant transport of individual unrooted tree
edges. The gap-seven fibre shows that the profile, even together with both
nested child returns and the full reduced passage, has constant normalized
congestion.

Accordingly the exact surviving assertion is:

> **Remaining RP gate.** Prove a global, peak- and slot-weighted packing
> theorem for high-rank reduced PBBS roots whose distinguished particle
> returns and whose immediate predecessor completes the passage after only
> \(O(\log r)\) selections, with simultaneous capacity control across
> different long parent-rank quotient cycles.

Equivalently, one must control the exact Pascal-weighted passage LP, or
construct a genuinely slot-dependent global assignment. Rank-only weights,
unweighted pruning, ordinary or incidence-tree rerooting, bounded local
edge menus, and uniform per-physical-component vanishing density are all rigorously
insufficient.

## 9. Scope and audit boundary

The quantifiers and implications are as follows.

* The sector-transport formula (2.2), the return equation (2.5), the
  predecessor-slot criterion (4.6), and the capacities (4.4), (4.7) are
  exact for every admissible rank.

* The ordinary and Stanley--Kreweras shape-change families rule out those
  natural unrooted encodings. They do not rule out a newly invented,
  heavily decorated object whose definition already retains the complete
  PBBS slot dynamics.

* The \(1/18\) obstruction rules out every bounded menu determined by the
  reduced return geometry. Even all \(d\) fixed-core edges cannot have
  uniform \(o(P_r(E)/d)\) congestion. This does not rule out a growing menu
  indexed by the full parent slot vector and controlled only in aggregate.

* The density-\(2/9\) component rules out a uniform vanishing-density
  statement imposed on every physical PBBS component, or on a certificate
  constant on such a component. It lies over a short quotient cycle and
  contributes negligible global Catalan mass.

* Equations (7.12) and (7.17) are necessary averaged saddle conditions for
  \(\mathrm{RP}_A\), not sufficient conditions and not pointwise
  assertions about every cell.

* No theorem here proves or disproves \(\mathrm{RP}_A\). The advance is a
  rigorous identification of the tree dynamics, a definitive obstruction
  to the proposed rerooting/local-charge lane, and the precise weighted
  global density statement which survives it.
