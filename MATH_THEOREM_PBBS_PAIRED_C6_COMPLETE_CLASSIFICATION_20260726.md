# The natural PBBS lift: complete classification and packing of alternating hexagons

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, or web lookup is
used.

## 0. Outcome

Put

\[
 n=2r+1,\qquad {\cal X}=\binom{[n]}r,\qquad
 {\cal C}=\binom{[n]}{r-1},
\]

\[
 W=|{\cal X}|=\binom{2r+1}r,\qquad
 N=|{\cal C}|=\frac r{r+2}W,\qquad
 B=\frac W{2r+1}=\operatorname {Cat}_r.
\tag{0.1}
\]

Let \(f\) be the canonical cyclic-parenthesis/PBBS permutation of
\({\cal X}\), and use its natural two perfect matchings in the Middle
Levels incidence graph,

\[
 M_0(U_Z)=f^{-1}(Z),\qquad M_1(U_Z)=f(Z),\qquad U_Z=[n]\setminus Z.
\tag{0.2}
\]

The legal exchange digraph for switching \(M_1\) has an unexpectedly
explicit complete triangle atlas.

> **Main theorem.** For every \(r\ge2\), its directed triangles are in
> bijection with the cores
>
> \[
> C\in\binom{[2r+1]}{r-1}
> \]
>
> whose cyclic binary word is not a rotation of
>
> \[
>                         000(10)^{r-1}.             \tag{0.3}
> \]
>
> Thus the exact number of legal alternating \(C_6\)'s is
>
> \[
>                         N-(2r+1).                  \tag{0.4}
> \]

Every such triangle is the star triangle on the three forward-unmatched
zeros of its core. No top-type Johnson triangle is legal. The support
hypergraph is linear and has maximum vertex degree at most \(r\), and hence
contains a physically vertex-disjoint family of size at least

\[
 \frac{N-(2r+1)}{3r-2}
   =\left(\frac23+o(1)\right)B.                     \tag{0.5}
\]

The natural PBBS lift has at most \(B\) components. Therefore (0.5) is
strictly larger, asymptotically, than the at most \(B/2\) hexagons needed
by a three-way loose-forest fusion. There is no scalar supply or physical
packing shortage.

The component quotient is not settled by this abundance. For every
\(r\ge4\), an explicit legal core has its three star vertices in three
different \(f^{-2}\)-components, certified by their distinct conserved
peak-pruning profiles. This refutes a tempting universal
two-component obstruction, but does not prove quotient connectivity.

Every compatible selected hexagon changes only three opposite
triple-union occurrences. Consequently any \(O(B)\)-switch
Hamiltonization using this atlas would retain

\[
                         \beta_r=O(B).               \tag{0.6}
\]

No such Hamiltonization is claimed here.

## 1. Matching conventions and the exchange digraph

Write a set as a cyclic \(0/1\) word, with \(1\) an opening symbol and
\(0\) a closing symbol. Repeated cyclic deletion of adjacent \(10\)
pairs is the forward matching. On a word in \({\cal X}\), it leaves one
zero. Denote that zero by \(p(Z)=r_+(Z)\). Then

\[
                         f(Z)=Z^c\setminus\{p(Z)\}.
\tag{1.1}
\]

The inverse is given by reverse \(01\)-matching:

\[
                         f^{-1}(Z)=Z^c\setminus\{r_-(Z)\}.
\tag{1.2}
\]

The legal exchange digraph \(D_f\) has vertex set \({\cal X}\). In the
center parameterization of (0.2), it has an arc

\[
 Z\longrightarrow X
\quad\Longleftrightarrow\quad
 f(Z)\cap X=\varnothing,\qquad X\notin\{Z,f^2(Z)\}.
\tag{1.3}
\]

Indeed, the first condition says that the \(M_1\)-edge at \(U_Z\) may be
moved to \(U_X\), while \(X=f^2(Z)\) would make that moved edge equal the
fixed \(M_0\)-edge at \(U_X\).

Taking complements in (1.1) gives

\[
                         f(Z)^c=Z\cup\{p(Z)\}.       \tag{1.4}
\]

Consequently every nonloop candidate in (1.3) has the form

\[
                         X=Z-a+p(Z)\qquad(a\in Z).
\tag{1.5}
\]

In particular, every directed triangle of \(D_f\) is a triangle of the
Johnson graph \(J(2r+1,r)\).

## 2. The two Johnson triangle types

Three distinct pairwise adjacent \(r\)-sets have exactly one of the
following forms.

* **Star type:**

  \[
  C+x_0,\quad C+x_1,\quad C+x_2,\qquad |C|=r-1.
  \tag{2.1}
  \]

* **Top type:**

  \[
  K+ab,\quad K+bc,\quad K+ca,\qquad |K|=r-2.
  \tag{2.2}
  \]

To see completeness, write two vertices as \(P+a,P+b\), where
\(|P|=r-1\). A third common Johnson neighbour either contains \(P\),
giving (2.1), or omits one \(x\in P\), in which case adjacency to both
vertices forces it to be \(P-x+a+b\), giving (2.2).

### Lemma 2.1 (top triangles are impossible)

No directed triangle of \(D_f\) has top type.

#### Proof

Let the common \((r+1)\)-set in (2.2) be \(Q\). If \(Z\to X\) is one
of its directed sides, then \(X\setminus Z=\{p(Z)\}\) by (1.5), and
hence

\[
                         Z\cup\{p(Z)\}=Q.
\]

Equation (1.4) gives \(f(Z)=Q^c\). Applying this to two distinct sources
of the alleged directed triangle gives the same \(f\)-image for two
distinct sets, contradicting the bijectivity of \(f\). \(\square\)

## 3. The unique star candidate on a core

We first record the forward clean-label fact used in the converse below.

### Lemma 3.0 (forward survivors only disappear)

Let a cyclic word \(C\) have \(2t+1\) more zeros than ones, and let
\(U_+(C)\) be its \(2t+1\) forward-unmatched zeros. Change at most \(t\)
zeros of \(C\) to ones. Every forward-unmatched zero of the resulting
word belongs to \(U_+(C)\).

#### Proof

It is enough to change one zero at a time. Cut the old word at its
forward-unmatched zeros,

\[
 0_{z_0}D_0\,0_{z_1}D_1\cdots0_{z_{d-1}}D_{d-1},
\]

where every \(D_i\) is a forward Dyck word. If a displayed \(z_i\) is
changed, contract the unchanged Dyck blocks: the new one consumes one of
the other displayed zeros. If an internal zero of some \(D_i\) is
changed, retain every old noncrossing pair except the pair incident with
that zero. After contracting the retained pairs, the new one and the
released old one consume two displayed zeros. In either case all
surviving unmatched zeros are among the \(z_i\). Iteration proves the
claim. \(\square\)

Fix \(C\in{\cal C}\). Its word has three more zeros than ones. Let
\(z_0,z_1,z_2\) be its three forward-unmatched zeros in cyclic order.
Cutting at these zeros gives the unique decomposition

\[
 0_{z_0}D_0\,0_{z_1}D_1\,0_{z_2}D_2,              \tag{3.1}
\]

where every \(D_i\) is a possibly empty Dyck word. Indices in this
section are modulo three. Put

\[
                         Z_i=C\cup\{z_i\}.          \tag{3.2}
\]

### Lemma 3.1 (forward survivor cycle)

\[
                         p(Z_i)=z_{i+2}.             \tag{3.3}
\]

Thus the only possible directed star triangle on core \(C\) is

\[
                         Z_0\to Z_2\to Z_1\to Z_0. \tag{3.4}
\]

#### Proof

Retain the canonical forward matching of every \(D_j\) and contract all
of its pairs. Flipping \(z_i\) changes the three-symbol residual word

\[
                         0_{z_i}0_{z_{i+1}}0_{z_{i+2}}
\]

to \(1_{z_i}0_{z_{i+1}}0_{z_{i+2}}\). Forward reduction pairs the new
one with \(z_{i+1}\) and leaves \(z_{i+2}\). This proves (3.3).

Conversely, if \(C+x_0,C+x_1,C+x_2\) form a directed star triangle, each
successor label is the forward survivor of the preceding vertex.
Lemma 3.0 puts all three successor labels in
\(\{z_0,z_1,z_2\}\). Since the vertices are distinct, they exhaust that
set, and (3.3) fixes the orientation. \(\square\)

## 4. Exact collision with the fixed matching

For \(u\in[n]\setminus C\), put

\[
 \alpha_C(u)=r_+(C+u),\qquad
 \beta_C(u)=r_-(C+u).                              \tag{4.1}
\]

The side \(Z_i\to Z_{i+2}\) in (3.4) is excluded from \(D_f\) precisely
when

\[
                         \beta_C(z_{i+2})=z_i.       \tag{4.2}
\]

Indeed, with \(T=[n]\setminus C\), equations (1.1)--(1.2) and (3.3)
give

\[
 f(Z_i)=T\setminus\{z_i,z_{i+2}\},                 \tag{4.3}
\]

\[
 f^{-1}(Z_{i+2})
 =T\setminus\{z_{i+2},\beta_C(z_{i+2})\}.          \tag{4.4}
\]

The two sets are equal exactly under (4.2), and that equality is
equivalent to \(Z_{i+2}=f^2(Z_i)\), the forbidden fixed-\(M_0\) collision.

We now determine exactly when (4.2) occurs.

### Lemma 4.1 (rightmost-maximum criterion)

For every \(j\in\mathbb Z/3\mathbb Z\),

\[
 \boxed{
 \beta_C(z_j)=z_{j+1}
 \iff
 D_j=D_{j+1}=\varnothing\ \text{ and }\
 \operatorname {ht}(D_{j+2})\le1.}
\tag{4.5}
\]

#### Proof

Rotate the word of \(C+z_j\) to start at the flipped symbol \(z_j\):

\[
 1D_j\,0_{z_{j+1}}D_{j+1}\,0_{z_{j+2}}D_{j+2}.     \tag{4.6}
\]

Give \(1\) height \(+1\) and \(0\) height \(-1\). In a cyclic word with
one more zero than one, reverse matching leaves the zero step following
the rightmost global maximum of the prefix height. This follows by
rotating to that step and applying ordinary linear \(01\)-stack matching.

Write \(h_i=\operatorname {ht}(D_i)\). The maximum prefix heights in the
three displayed regions of (4.6) are respectively

\[
                         1+h_j,\qquad h_{j+1},
                         \qquad h_{j+2}-1.          \tag{4.7}
\]

The pre-step height at \(z_{j+1}\) is \(1\). For this to be the rightmost
global maximum, the first entry in (4.7) must equal \(1\), forcing
\(h_j=0\), hence \(D_j=\varnothing\). After \(z_{j+1}\), any nonempty
Dyck word \(D_{j+1}\) reaches height \(1\), producing a later occurrence
of the same maximum (and height at least two would exceed it). Thus
\(D_{j+1}=\varnothing\). Finally, the last region must stay strictly
below height \(1\); by (4.7) this is exactly \(h_{j+2}\le1\).

Conversely, under these three conditions, the prefix immediately before
\(z_{j+1}\) has height \(1\), all earlier prefixes have height at most
\(1\), and all later prefixes have height at most \(0\). It is therefore
the rightmost global maximum, proving (4.5). \(\square\)

### Corollary 4.2 (the exceptional core family)

For \(r\ge2\), the star triangle (3.4) is illegal if and only if the cyclic
word of \(C\) is a rotation of \(000(10)^{r-1}\).

#### Proof

The total semilength of \(D_0,D_1,D_2\) is \(r-1\). Under (4.5), the
single remaining block has semilength \(r-1\) and height at most one. The
unique such Dyck word is \((10)^{r-1}\). Conversely this word satisfies
(4.5), so one side of (3.4) collides with \(M_0\).

At most one index \(j\) satisfies (4.5), because \(r-1>0\). Therefore
every other core has all three sides legal. \(\square\)

The cyclic word in (0.3) has a unique cyclic run of four zeros: its final
zero together with its initial three zeros. Hence it has full period
\(2r+1\), and its rotations give exactly \(2r+1\) distinct labelled cores.
Together with Lemmas 2.1 and 3.1, this proves (0.4) and the complete
classification in the main theorem. At \(r=2\), all
\(N=5=2r+1\) cores are exceptional, so there is no directed triangle;
this also agrees with the exchange outdegree \(r-1=1\).

## 5. Physical packing

Let \({\cal H}_r\) be the \(3\)-uniform hypergraph on \({\cal X}\) whose
edges are the vertex triples (3.2) of legal directed triangles.

### Lemma 5.1 (linearity and degree)

\({\cal H}_r\) is linear and

\[
                         \Delta({\cal H}_r)\le r.   \tag{5.1}
\]

#### Proof

If two distinct star triples shared two \(r\)-sets, the intersection of
those two sets would recover their common \((r-1)\)-core, so the two cores,
and hence the triples, would be equal. Thus distinct hyperedges share at
most one vertex.

A fixed \(Z\in{\cal X}\) can occur only for a core \(C=Z-x\) with
\(x\in Z\). There are \(r\) such cores, proving the degree bound. \(\square\)

### Corollary 5.2 (disjoint hexagon reservoir)

\({\cal H}_r\) has a matching of size at least

\[
                         \frac{N-(2r+1)}{3r-2}.      \tag{5.2}
\]

#### Proof

Greedily choose a hyperedge and delete all edges meeting it. By linearity
and (5.1), one choice deletes at most

\[
                         1+3(r-1)=3r-2
\]

hyperedges. This proves (5.2).

The three upper vertices of the corresponding incidence hexagon are
\(U_{Z_i}\), and its three lower vertices are \(f(Z_i)\). Since \(Z\mapsto
U_Z\) and \(f\) are bijections, vertex-disjoint hyperedges give physically
vertex-disjoint alternating hexagons. \(\square\)

Using (0.1), the quotient of (5.2) by \(B\) is

\[
 \frac{(2r+1)r}{(r+2)(3r-2)}-o(1)=\frac23+o(1),    \tag{5.3}
\]

which proves (0.5).

## 6. Component scale and triple-union stability

The paired monodromy of (0.2) is \(f^{-2}\). If an \(f\)-orbit has
length \(\ell(2r+1)\), it contributes \(\gcd(2,\ell)\le\ell\) monodromy
components. PBBS coordinate homomesy gives

\[
                         \sum_{\text{\(f\)-orbits}}\ell=B,
\]

and hence

\[
                         c(F_{\rm PBBS})\le B.       \tag{6.1}
\]

The centered PBBS Johnson factor has complete opposite triple-union
support. Equivalently, after complementation its opposite colours are
the PBBS angle colours \(f^{-1}(A)\cap f(A)\), every rank-\((r-1)\) set
occurring at least once. Thus its raw triple-union defect is exactly

\[
 \beta_r(F_{\rm PBBS})
   =W-N=\frac{2W}{r+2}<4B.                          \tag{6.2}
\]

One factor-alternating hexagon replaces one incidence edge at each of
three upper slots. On the opposite shore, only its three lower vertices
can acquire a different pair of adjacent upper neighbours. Therefore
only three opposite triple-union occurrences change. After any ordered
compatible family of \(s\) hexagon switches,

\[
                         \beta_r\le\frac{2W}{r+2}+3s.\tag{6.3}
\]

In particular \(s=O(B)\) proves (0.6). This is the exact quantitative
reason that a Catalan-size connector forest would close the surviving
GMM base gate.

## 7. Genuine three-component connectors exist

One might suspect that every legal star triple meets at most two PBBS
components. That obstruction is false.

For a Dyck word \(D\), let \(\partial D\) be obtained by simultaneously
deleting every peak \(10\). Define its peak-pruning profile

\[
 {\bf a}(D)=(a_1(D),a_2(D),\ldots),\qquad
 a_s(D)=\operatorname {pk}(\partial^{s-1}D),
\tag{7.1}
\]

padded by zeros.

### Lemma 7.1 (profile calculus)

The profile \({\bf a}(D)\) is invariant on a PBBS orbit of the physical
state represented by the rooted word \(0D\). For Dyck words \(P,Q,D\),

\[
 {\bf a}(PQ)={\bf a}(P)+{\bf a}(Q),                 \tag{7.2}
\]

and, writing \(h=\operatorname {ht}(D)\),

\[
 {\bf a}(1D0)={\bf a}(D)+{\bf e}_{h+1}.             \tag{7.3}
\]

#### Proof

The exact first-\(10\)-elimination semiconjugacy
(Theorem 7.2 of MATH_ATTACK_Y12_DIRECT_ALL_DEPTH_PBBS_DYCK_GATE_20260725.md)
says that the equal-edge
particles left after deleting all current peaks carry the rooted word
\(0\partial D\) and evolve by the smaller PBBS rule. The number of peaks
itself is invariant. Iterating this statement proves invariance of every
coordinate in (7.1).

Peak deletion acts independently on a concatenation of Dyck words:
their boundary is \(01\), never a peak, and remains a Dyck-component
boundary after every round. This proves (7.2).

Inside \(1D0\), the outer pair cannot become a peak until every pair of
\(D\) has disappeared. Simultaneous leaf pruning empties \(D\) after
exactly \(\operatorname {ht}(D)\) rounds. The outer pair is deleted in
the following round, proving (7.3). \(\square\)

Return to the core decomposition (3.1). Since the forward survivor of
\(Z_i\) is \(z_{i+2}\), cutting immediately after that survivor gives the
normalized Dyck root

\[
                         E_i=D_{i+2}\,1D_i0\,D_{i+1}.
\tag{7.4}
\]

### Theorem 7.2 (action-separated star triangle)

Put \(h_i=\operatorname {ht}(D_i)\). Then

\[
 {\bf a}(E_i)
 ={\bf a}(D_0)+{\bf a}(D_1)+{\bf a}(D_2)
   +{\bf e}_{h_i+1}.                                \tag{7.5}
\]

Consequently, if \(h_0,h_1,h_2\) are pairwise distinct, the three vertices
of the legal star triangle lie in three distinct \(f\)-orbits, and hence
in three distinct \(f^{-2}\)-components.

#### Proof

Apply (7.2)--(7.3) to (7.4), obtaining (7.5). Pairwise distinct heights
put the added unit in three distinct profile coordinates, so the three
profiles differ. Lemma 7.1 then separates the PBBS orbits. \(\square\)

For every \(r\ge4\), take

\[
 D_0=\varnothing,\qquad D_1=10,\qquad
 D_2=1^{r-2}0^{r-2}.                                \tag{7.6}
\]

Their semilengths sum to \(r-1\), and their heights are
\(0,1,r-2\), which are pairwise distinct. Only one block is empty, so
Corollary 4.2 says the associated star triangle is legal. Theorem 7.2
therefore supplies an explicit component-transversal connector in every
dimension \(r\ge4\).

This also identifies the flaw in a tempting contrary argument. The
identity

\[
                         \tau(P1R0S)=S1P0R
\]

uses the unique **first-deepest** factorization \(P1R0S\) of a normalized
Dyck word. The displayed factorization in (7.4) is an arbitrary
three-block factorization and need not be first-deepest. Applying the
identity to it without checking that condition is invalid.

There is also no obstruction at the coarser action-profile level. Let
\({\mathfrak G}_r\) have as vertices the profiles (7.1) realized by
semilength-\(r\) Dyck words, joining two profiles when they occur in one
legal star triangle.

### Corollary 7.3 (action-profile connectivity)

For every \(r\ge3\), \({\mathfrak G}_r\) is connected.

#### Proof

Give a profile the potential

\[
                         \Psi({\bf a})
 =\sum_{s\ge1}(s-1)a_s.                            \tag{7.7}
\]

Its unique zero is the alternating profile \(r{\bf e}_1\).

Take any other realized profile. Choose a Dyck realization having a
nonleaf primitive component first, and write it as

\[
                         E=1D0\,Q,\qquad D\ne\varnothing,
\tag{7.8}
\]

where \(Q\) is Dyck. This reordering of primitive components does not
change the profile, by (7.2). Use the core blocks

\[
                         D_0=\varnothing,\quad D_1=D,\quad D_2=Q.
\]

The star state \(E_1\) in (7.4) is \(E\), while \(E_0=Q10D\). By (7.5),
the profile move is

\[
 {\bf a}(E_1)\longmapsto{\bf a}(E_0)
 ={\bf a}(E_1)-{\bf e}_{h+1}+{\bf e}_1,
\qquad h=\operatorname {ht}(D)\ge1,                \tag{7.9}
\]

and decreases \(\Psi\) by \(h\).

Corollary 4.2 makes this triangle legal except when
\(Q=\varnothing\) and \(D=(10)^{r-1}\). The exceptional profile is

\[
                         (r-1){\bf e}_1+{\bf e}_2.
\]

For it, choose instead

\[
 D_0=\varnothing,\qquad D_1=(10)^a,\qquad
 D_2=(10)^b,
\]

where \(a,b\ge1\) and \(a+b=r-1\). This is possible for \(r\ge3\).
The core is legal because only one block is empty, and its profiles are
\((r-1){\bf e}_1+{\bf e}_2\) and \(r{\bf e}_1\).

Repeated strict descent in (7.7) reaches \(r{\bf e}_1\), proving
connectivity. \(\square\)

Thus any obstruction to the component loose-forest gate must use the
angle/phase coordinates inside a fixed PBBS action sector; soliton
content alone cannot provide a closed quotient cut.

There is also an exact pointwise activity classification. Represent a
physical center \(Z\) by

\[
                         0_pD,
\tag{7.10}
\]

where \(p\) is its forward-unmatched zero and \(D\) is Dyck. Factor

\[
                         D=F_1F_2\cdots F_k,\qquad
                         F_j=1A_j0
\tag{7.11}
\]

into primitive Dyck factors.

### Lemma 7.4 (exact star incidence of a center)

\(Z\) lies in the star candidate obtained by deleting an occupied
coordinate \(x\) if and only if \(x\) is the first up-step of one of the
primitive factors \(F_j\). For that deletion, the three core blocks are

\[
 P_j=F_1\cdots F_{j-1},\qquad A_j,\qquad
 S_j=F_{j+1}\cdots F_k.                              \tag{7.12}
\]

#### Proof

If \(x\) is the first up-step of \(F_j=1A_j0\), delete it. The canonical
forward matchings inside \(P_j,A_j,S_j\) remain, while the root \(p\),
the deleted coordinate \(x\), and the closing zero of \(F_j\) are
unmatched. Thus these are the three survivor blocks (7.12), and \(Z\)
is one of the associated star vertices.

Conversely, scan the normalized Dyck word with the ordinary stack. If an
up-step \(x\) starts at positive height, then after changing it to a zero
the stack is nonempty at \(x\), so that new zero is matched and cannot be
one of the three forward survivors. Hence a deletable star coordinate
must start at height zero, exactly the first up-step of a primitive
factor. \(\square\)

### Corollary 7.5 (inactive centers and component activity)

For \(r\ge3\), a center has legal-\(C_6\) degree zero if and only if its
normalized root is

\[
                         D=1(10)^{r-1}0.             \tag{7.13}
\]

There are exactly \(2r+1\) such physical centers. Nevertheless every
\(f^{-2}\)-component has an incident legal \(C_6\).

#### Proof

By Lemma 7.4 and Corollary 4.2, the candidate belonging to \(F_j\) is
illegal exactly when two of \(P_j,A_j,S_j\) are empty and the third has
height at most one.

If \(k\ge3\), every interior factor has both \(P_j,S_j\ne\varnothing\),
so it gives a legal candidate. If \(k=2\), both endpoint candidates can
be illegal only when both primitive factors are \(10\), which has
semilength two and is excluded by \(r\ge3\). If \(k=1\), there is one
candidate, and it is illegal exactly when
\(A_1=(10)^{r-1}\). This proves (7.13). The unmatched root coordinate is
recoverable from a physical state, so its \(2r+1\) choices give exactly
\(2r+1\) inactive centers.

For the root (7.13), its canonical first-deepest factorization gives

\[
                         \tau D=1100(10)^{r-2}.      \tag{7.14}
\]

The word on the right has at least two primitive factors and is not the
inactive word (7.13), so it has a legal candidate. The physical
step-two PBBS map \(f^2\) applies this quotient map together with a
coordinate displacement. Hence every inactive center has an active
center in its own \(f^{-2}\)-component. Every component therefore has a
legal-\(C_6\) portal. \(\square\)

The same calculation usually gives an action-crossing portal. For the
first primitive factor, the blocks are
\(\varnothing,A_1,F_2\cdots F_k\). If this candidate is legal and
\(A_1\ne\varnothing\), (7.5) separates its wrapped and empty-block
profiles. If \(A_1=\varnothing\), legality forces the suffix height to be
at least two, and wrapping that suffix again gives a distinct profile.

## 8. Exact remaining component-quotient gate

Let \({\cal P}_r\) be the partition of \({\cal X}\) into cycles of
\(f^{-2}\). Project every hyperedge of \({\cal H}_r\) to the blocks of
\({\cal P}_r\), retaining a hyperedge only when its three entries are
distinct. Call the resulting physical quotient multihypergraph
\({\cal Q}_r\).

The exact remaining theorem is:

> **PBBS quotient loose-forest gate (unproved).** If
> \(c(F_{\rm PBBS})\) is odd, \({\cal Q}_r\) contains a spanning loose
> tree with representatives whose physical hyperedges are vertex-disjoint.
> If it is even, it contains a physically disjoint two-block spanning
> loose forest. In the even case, one additional legal parity-changing
> circuit must join the two resulting components.

Theorem 7.2 proves that \({\cal Q}_r\) has genuine three-component edges;
it does not prove the displayed spanning condition. A dynamic sequence
which recomputes the legal exchange graph after every switch is a possible
alternative, but it too must use only \(O(B)\) changed opposite slots.
Equation (6.3) would then give \(\beta_r=O(B)\).

Even ordinary connectivity of the \(2\)-section of \({\cal Q}_r\) would
not suffice. For example, the abstract triples

\[
 \{a,b,c\},\qquad\{a,b,d\},\qquad\{a,b,e\}
\tag{8.1}
\]

have connected \(2\)-section, but every two triples overlap in two
vertices, so they contain no spanning loose tree. A selected quotient
family \({\cal F}\) must satisfy the exact loose-forest sparsity inequalities

\[
 \left|\bigcup{\cal F}'\right|\ge2|{\cal F}'|+1
 \qquad(\varnothing\ne{\cal F}'\subseteq{\cal F}),
\tag{8.2}
\]

as well as full component coverage and disjoint physical representatives.
The physical atlas \({\cal H}_r\) is linear, but quotienting different
physical states into the same \(f^{-2}\)-component can destroy linearity.
Thus a mere component-connectivity theorem would still leave a real
representative/Hall gate.

The complete local atlas, its exact exceptional family, its physical
packing rate, the component bound, and the \(3s\) edit ledger are all
proved above. What remains unproved is solely the position of these
explicit star triples relative to the long, chronology-sensitive
\(f^{-2}\)-orbits. Marginal triangle counts do not imply this quotient
statement, and no claim of Hamiltonicity or constant one is made.

## 9. Adversarial audit

The main possible failure modes have the following resolutions.

1. **Confusing top and star triangles.** Section 2 classifies both.
   Injectivity of \(f\) eliminates the top case; it says nothing about
   the star case.
2. **Using angle completeness at the wrong point.** A fixed point of
   \(\beta_C\alpha_C\) need not itself be a forward-unmatched zero. The
   proof does not make that inference. Instead Lemma 4.1 evaluates the
   three relevant survivor values exactly.
3. **Losing the rightmost-maximum tie.** Equality after the candidate
   step is forbidden: it would move the rightmost maximum later. This is
   why \(D_{j+1}\) must be empty and why
   \(\operatorname {ht}(D_{j+2})\le1\), not merely \(\le2\).
4. **Overcounting exceptional rotations.** For \(r\ge2\), the cyclic
   word has one run of four zeros and hence full period \(2r+1\).
5. **Confusing edge-disjointness with physical disjointness.** A
   hypergraph matching makes the three \(U_Z\)'s disjoint across selected
   hexagons; bijectivity of \(f\) then also separates all opposite-shore
   vertices.
6. **Overclaiming component transversality.** No bound in Sections 4--5
   controls how the three vertices of a legal star triangle lie among
\(f^{-2}\)-cycles. Section 7 gives genuine three-component triangles,
   but this does not imply global quotient connectivity.
7. **Applying the sector rotation to the wrong factorization.** The
   formula \(\tau(P1R0S)=S1P0R\) is canonical only at the first deepest
   sector. Equation (7.4) does not generally have that property.
8. **Mistaking profile connectivity for component connectivity.**
   Corollary 7.3 permits rechoosing a representative with a convenient
   primitive-component order. It proves connectivity only after collapsing
   every PBBS action sector, not connectivity of the labelled
   \(f^{-2}\)-component quotient.
9. **Mistaking portals for quotient expansion.** Corollary 7.5 gives
   incident legal triangles in every component, and usually action-crossing
   ones, but does not
   force three distinct component labels or the Hall inequalities for a
   loose spanning forest.
10. **Mistaking quotient connectivity for a loose forest.** The family
    (8.1) is the minimal repeated-pair obstruction. Physical linearity
    before quotienting does not remove it.
