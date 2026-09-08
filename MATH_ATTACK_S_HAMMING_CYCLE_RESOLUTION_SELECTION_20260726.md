# Linear-code cycle resolutions: exact interval designs, affine phase blocks, and the target-selection obstruction

Date: 2026-07-26

Method: pure mathematics only. No computational or finite-search claim is used.

## 0. Outcome

Let \(\ell=2^t\ge4\), and consider the linear-translate resolutions of an
isometric \(2\ell\)-cycle in an orientation cube. The exact conclusions are:

1. Every full-dimensional isometric \(2\ell\)-cycle has direction word
   \(\sigma\sigma\), where \(\sigma\) is a cyclic order of the \(\ell\)
   directions. Therefore a fixed \(q\)-set \(D\), \(1\le q<\ell\), occurs
   consecutively exactly twice on a component if and only if \(D\) is a
   cyclic \(q\)-interval of \(\sigma\), and otherwise it never occurs.

2. A vertex-resolution class contains \(2^s/(2\ell)\) components in
   \(Q_s\). Hence its directional load on \(D\) is
   \[
       n_{\rho,q}(D)=
       \begin{cases}
       2^s/\ell,&D\text{ is a cyclic interval of the active order},\\
       0,&\text{otherwise}.
       \end{cases}                                      \tag{0.1}
   \]
   The \(\ell\) affine translate classes of one linear system all have this
   same directional histogram. Phase-class selection has no directional
   balancing power.

3. For a full \(Q_\ell\) system with kernel \(K\), put
   \(L=K\oplus\langle\mathbf1\rangle\). For an interval direction set
   \(D\), let
   \[
                         h_D=\dim(L\cap V_D).             \tag{0.2}
   \]
   A selected phase class contains
   \(2|K|/2^{h_D}\) distinct affine \(D\)-faces, each with multiplicity
   \(2^{h_D}\). A fixed affine \(D\)-face lies in exactly
   \(2^{q-h_D}\) of the \(\ell\) phase classes. The phase--face incidence
   graph is a disjoint union of complete bipartite graphs. Across all
   \(\ell\) phases, every affine \(D\)-face has total occurrence
   multiplicity exactly \(2^q\).

4. At a face-simple depth, \(h_D=0\). Then a physical face is available in
   exactly \(2^q\) phases, while every chosen phase covers one entire block
   of \(2^\ell/\ell\) faces. Thus even perfect directional balance is not
   labelled shadow balance: the remaining phase choices are highly
   correlated block choices.

   In the parity-resolved Hamming system the \(\ell\) phase labels split
   into two shores of size \(\ell/2\), and either shore is an edge
   resolution. Within one shore a face is available in
   \(2^{q-1-h_D}\) classes and has aggregate multiplicity \(2^{q-1}\).

5. For \(R\) replicated copies of one face-simple Hamming system, exact
   once-only coverage of every affine face belonging to every cyclic
   \(q\)-interval is equivalent to a common-transversal problem in the
   shore syndrome space. Necessarily \(R=\ell/2^q\). If \(B_I\) is the
   even-syndrome subspace belonging to interval \(I\), the selected class
   labels must meet every coset of every \(B_I\) exactly once. This condition
   is both necessary and sufficient.

   This is conditional on one syndrome system having both the parity-shore
   property and face-simplicity at the stated depth. The two ingredients
   occur separately in the existing constructions; their simultaneous
   growing-depth compatibility is not proved here.

6. Averaging over all active coordinate sets, cyclic orders, and affine
   phases gives a perfectly uniform fractional face incidence. In a source
   cube of dimension \(h\), a fixed affine \(q\)-face has average load
   \[
                              p_{h,q}=\frac{2^q}{\binom hq}. \tag{0.3}
   \]
   Consequently a fixed lower target of pair type \((f,q)\), with
   \(h=m-2f\), has uniform fractional load
   \[
       \boxed{\lambda_{f,q}
        =\frac{2^q\binom{f+q}{q}}{\binom{m-2f}{q}}
        =\frac{V_f}{T_{f,q}}.}                           \tag{0.4}
   \]

7. Formula (0.4) is also the decisive no-go. For every integral selection
   of one resolution class per source fibre, independently of its code,
   active frame, cyclic order, or phase,
   \[
           \sum_{T\in\mathcal O^-_{f,q}}L_q(T)=V_f.       \tag{0.5}
   \]
   Therefore at least \((T_{f,q}-V_f)_+\) targets of type \((f,q)\) are
   missed. Exact unit balance is possible only if
   \[
                         \binom{m-2f}{q}
                    =2^q\binom{f+q}{q}.                  \tag{0.6}
   \]
   In particular, for \(f=0\) and \(\binom mq>2^q\), every such selection
   misses at least
   \[
                         2^{m-q}\bigl(\binom mq-2^q\bigr) \tag{0.7}
   \]
   labelled rank-\(m-q\) targets. Thus one class per fixed-pair fibre cannot
   balance every \(q\)-target.

8. On the Gaussian scale \(q=A\sqrt m+o(\sqrt m)\), the obstruction has an
   explicit positive limiting density. Writing \(N_q=\binom{2m}{m-q}\),
   \[
    \frac1{N_q}\sum_f(T_{f,q}-V_f)_+
       \longrightarrow
       \boxed{\kappa(A)=
       \Phi(A/2)-e^{A^2}\Phi(-3A/2)>0}                  \tag{0.8}
   \]
   for every fixed \(A>0\). Hence Hamming-parameter resolution-class
   selection does not supply a coefficient-one fixed-frame shadow design.
   Mixing pair frames, or leaving the fixed-pair architecture, remains
   necessary.

There is also a terminology correction. The kernels supplied by the general
linear-cycle construction have the parameters of a codimension-\((t+1)\)
code, but for \(t\ge2\) they are not Hamming or extended-Hamming codes in
general: their first \(\ell-1\) syndrome columns necessarily repeat, so the
kernel contains a word of weight two. The incidence theorems below apply to
these linear-code resolutions and, a fortiori, to any genuine Hamming-based
subfamily satisfying the same transversal hypotheses.

Indeed, in the construction of `LINEAR_CYCLE_TILING.md`, the first
\(\ell-1\) syndrome columns are
\[
                         c_i=u_i+u_{i-1}\in\mathbb F_2^t
                         \qquad(1\le i<\ell).             \tag{0.9}
\]
They are nonzero. If they were all distinct, they would exhaust the
\(\ell-1\) nonzero vectors of \(\mathbb F_2^t\). Their sum would then be
zero for \(t\ge2\), whereas telescoping (0.9) gives
\(\sum_i c_i=u_{\ell-1}\ne0\). Hence \(c_i=c_j\) for some \(i\ne j\),
and \(e_i+e_j\) is a weight-two kernel word.

## 1. Direction-word rigidity

Let \(C=(x_0,x_1,\ldots,x_{2\ell}=x_0)\) be an isometric cycle in
\(Q_\ell\). Write \(w_i\) for the coordinate flipped on
\(x_i x_{i+1}\), with indices modulo \(2\ell\).

### Lemma 1.1 (isometric word normal form)

There is a permutation \(\sigma=(\sigma_0,\ldots,\sigma_{\ell-1})\) of
the coordinates such that
\[
                             w=\sigma\sigma.             \tag{1.1}
\]

#### Proof

Every arc of length at most \(\ell\) on an isometric \(2\ell\)-cycle is a
hypercube geodesic. Hence every \(\ell\) consecutive direction letters are
distinct, and therefore form the complete coordinate set. Comparing the
two length-\(\ell\) windows beginning at \(i\) and \(i+1\), the letter lost
from the first equals the letter entering the second. Thus
\(w_{i+\ell}=w_i\) for every \(i\). The first \(\ell\) letters are a
permutation, proving (1.1). \(\square\)

For \(1\le q<\ell\), the \(q\)-subsets obtained from cyclic length-\(q\)
intervals of \(\sigma\) are all distinct. Indeed their binary incidence
words on the cyclic order have one nonempty run of ones and one nonempty run
of zeros, whose two boundary positions determine the interval.

### Corollary 1.2 (one-component interval count)

For a fixed \(q\)-set \(D\), the number of starts on \(C\) whose next
\(q\) direction letters have set \(D\) equals two if \(D\) is a cyclic
interval of \(\sigma\), and zero otherwise. For \(q=\ell\), the complete
active set occurs at all \(2\ell\) starts.

## 2. One resolution class and its unavoidable design margins

First take \(Q_\ell\). A resolution class \(\rho\) partitions its vertices
into
\[
                             N=\frac{2^\ell}{2\ell}       \tag{2.1}
\]
isometric \(2\ell\)-cycles. The same formulas hold in \(Q_s\) after
fibering over \(s-\ell\) spectators, with
\(N=2^s/(2\ell)\).

For a class whose components all use the cyclic order \(\sigma\), let
\(n_{\rho,q}(D)\) count starting vertices whose next \(q\) directions have
set \(D\). Corollary 1.2 gives (0.1).

Fix the common active \(\ell\)-set \(A\) (so the remaining \(s-\ell\)
coordinates are spectators). For a general resolution in which component
orders on \(A\) may vary, let
\(c_{\rho,q}(D)\) count components on which \(D\) is a cyclic interval.
Then
\[
                         n_{\rho,q}(D)=2c_{\rho,q}(D),    \tag{2.2}
\]
and the interval multihypergraph obeys the exact identities
\[
       \sum_Dc_{\rho,q}(D)=N\ell=2^{s-1},               \tag{2.3}
\]
\[
       \sum_{\substack{D\ni i\\D\subseteq A}}c_{\rho,q}(D)=qN,
       \qquad
       \sum_{\substack{D\ni i\\D\subseteq A}}n_{\rho,q}(D)
             =\frac{q2^s}{\ell}
       \qquad(i\in A).                                \tag{2.4}
\]
Indeed every cyclic order has \(\ell\) intervals of length \(q\), and
each coordinate belongs to exactly \(q\) of them. Thus every class gives a
\(1\)-design in direction space, but need not give a \(q\)-subset-balanced
design. In particular:

* at \(q=1\), every class is perfectly direction-balanced;
* at \(q=2\), the multiplicities \(c_{\rho,2}\) form a regular multigraph,
  being the sum of the Hamilton cycles supplied by the components;
* for \(2\le q\le\ell-2\), fixed point margins do not force equal
  \(q\)-set loads.

## 3. The linear translate classes

From this section onward assume \(\ell=2^t\ge4\). Let
\(V=\mathbb F_2^\ell\), and let
\[
 P_\sigma=\{p_i,\mathbf1+p_i:0\le i<\ell\},
 \qquad
 p_i=e_{\sigma_0}+\cdots+e_{\sigma_{i-1}}.             \tag{3.1}
\]
Suppose \(K\le V\) has codimension \(t+1\), with \(P_\sigma\) a complete
transversal for \(V/K\). Then
\[
                         |K|=\frac{2^\ell}{2\ell},      \tag{3.2}
\]
and \(\mathbf1\notin K\), because \(0,\mathbf1\in P_\sigma\) represent
different \(K\)-cosets.

Put
\[
                         L=K\oplus\langle\mathbf1\rangle. \tag{3.3}
\]
Translation stabilizes the cycle vertex set \(P_\sigma\) precisely by
\(0\) and \(\mathbf1\). Indeed, for \(\ell\ge3\) the displayed cycle is
induced, so a stabilizing translation induces a dihedral automorphism of
it and preserves every edge-direction label. A nontrivial translation has
no fixed vertex. A reflection through opposite edges is also impossible:
it would interchange the two cycle edges adjacent to one of its fixed
edges, although those edges have distinct coordinate labels and translation
preserves labels. Hence the induced automorphism is a rotation. Since a
translation has order at most two, the rotation is by \(0\) or by
\(\ell\) positions. The latter is exactly translation by
\(\mathbf1\).

Consequently the complete translate family splits into exactly
\[
                             |V/L|=\ell                 \tag{3.4}
\]
resolution classes
\[
             \mathcal R_a=\{P_\sigma+a+k:k\in K\},
             \qquad a\in V/L.                           \tag{3.5}
\]
Every \(\mathcal R_a\) partitions \(V\), because \(P_\sigma\) is a
transversal for \(K\). These \(\ell\) classes resolve all distinct
translates of the cycle.

The restriction \(\ell\ge4\) is necessary for this distinct-class census:
when \(\ell=2\), the base \(C_4\) is the whole of \(Q_2\), so every
translation stabilizes its vertex set. Nothing in the asymptotic
constant-one application uses this degenerate case.

All classes in (3.5) have the same word \(\sigma\sigma\). Therefore:

### Proposition 3.1 (phase selection is direction-inert)

For \(1\le q<\ell\) and a fixed \(q\)-set \(D\), every one of the
\(\ell\) classes has \(2|K|=2^\ell/\ell\) occurrences of \(D\) if
\(D\) is a cyclic interval of \(\sigma\), and zero otherwise. Across all
\(\ell\) classes the corresponding total is \(2^\ell\) or zero.

Thus selecting one of the \(\ell\) translate classes cannot change any
direction-set histogram.

## 4. Exact affine-face blocks

Fix a cyclic interval \(D\) of size \(q<\ell\), and write
\(V_D=\operatorname{span}\{e_i:i\in D\}\). Let \(F_0\) be the affine
\(D\)-face spanned by the corresponding window in the first half of
\(P_\sigma\). The two half-cycle occurrences and all kernel translates in
class \(\mathcal R_a\) span exactly
\[
                       F_0+a+l,qquad l\in L.             \tag{4.1}
\]
Here faces are identified modulo translation by \(V_D\).

Set
\[
                         h_D=\dim(L\cap V_D).             \tag{4.2}
\]

### Theorem 4.1 (phase--face block decomposition)

For the direction interval \(D\):

1. one phase class contains
   \[
                         \frac{|L|}{2^{h_D}}
                         =\frac{2|K|}{2^{h_D}}            \tag{4.3}
   \]
   distinct affine \(D\)-faces;
2. every such face occurs with multiplicity \(2^{h_D}\);
3. a fixed affine \(D\)-face lies in exactly
   \[
                              2^{q-h_D}                   \tag{4.4}
   \]
   of the \(\ell\) phase classes;
4. the bipartite incidence graph between phase classes \(V/L\) and affine
   faces \(V/V_D\) is a disjoint union of complete bipartite graphs, indexed
   by \(V/(L+V_D)\), with side sizes
   \[
             2^{q-h_D}\quad\text{and}\quad
             2^{\ell-t-h_D};                             \tag{4.5}
   \]
5. across all phase classes, every affine \(D\)-face has total occurrence
   multiplicity \(2^q\).

#### Proof

Two values \(l,l'\in L\) in (4.1) give the same face exactly when
\(l-l'\in V_D\). This proves (4.3) and the multiplicity assertion.

A face \(x+V_D\) belongs to class \(a+L\) exactly when
\[
                         x-F_0-a\in L+V_D.               \tag{4.6}
\]
Thus incidence is possible precisely within a common coset of \(L+V_D\),
and inside such a coset it is complete. The number of phase vertices in one
component is
\[
                         |(L+V_D)/L|=2^{q-h_D},          \tag{4.7}
\]
while the number of face vertices is
\[
                         |(L+V_D)/V_D|=2^{\ell-t-h_D}.  \tag{4.8}
\]
This proves (4.4)--(4.5). Multiplying the number of incident phases in
(4.4) by the within-phase multiplicity \(2^{h_D}\) gives \(2^q\). \(\square\)

At the face-simple depths of the field-enumerated construction in
`CUBE_SHADOW_TILING.md`, one has \(h_D=0\) for every relevant cyclic
interval. Theorem 4.1 then says that a phase support is one whole block of
\(2^\ell/\ell\) faces, and the \(2^q\) phases in the same component have
identical face support. This is much more rigid than independently choosing
each face.

### 4.1 The two Hamming edge-resolution shores

The Hamming parity construction adds the following structure to the total
phase quotient. Let
\[
              \Psi:V\longrightarrow A\cong\mathbb F_2^t,
              \qquad \ker\Psi=L,                         \tag{4.9}
\]
so that \(A=V/L\) is the set of the \(\ell\) phase labels. There is a
nonzero functional
\[
                   \varepsilon:A\longrightarrow\mathbb F_2
 \quad\text{with}\quad
                   \varepsilon(\Psi(e_i))=1
                   \quad(i\in[\ell]).                    \tag{4.10}
\]
Equivalently, \(\varepsilon\Psi(x)=|x|\pmod2\). Put
\[
                     A_0=\ker\varepsilon,
                     \qquad A_1=\varepsilon^{-1}(1).     \tag{4.11}
\]
Both shores have \(\ell/2\) phase classes.

For an interval \(I\), set
\[
 r_I=\dim(\ker\Psi\cap V_I),
 \qquad
 B_I=\Psi(V_I)\cap A_0.                                 \tag{4.12}
\]
Since \(\varepsilon\) is nonzero on \(\Psi(V_I)\),
\[
                         \dim B_I=q-1-r_I.               \tag{4.13}
\]
If \(F=x+V_I\) is an affine \(I\)-face and \(p_j\) is the prefix at the
start of this interval, its admissible labels in shore \(A_0\) are exactly
\[
       S_I(F)=A_0\cap\bigl(\Psi(x+p_j)+\Psi(V_I)\bigr),  \tag{4.14}
\]
an affine coset of \(B_I\), and hence
\[
                              |S_I(F)|=2^{q-1-r_I}.       \tag{4.15}
\]
If a selected class label lies in this set, the face occurs with
multiplicity \(2^{r_I}\); otherwise it does not occur.

### Corollary 4.2 (each shore resolves the cube edges)

For \(q=1\), one has \(r_I=0\), \(B_I=0\), and every physical edge has
exactly one admissible label in \(A_0\) and one in \(A_1\). Consequently
the \(\ell/2\) vertex factors indexed by either shore partition all edges
of \(Q_\ell\). Thus the correct census is:

* \(\ell\) syndrome-translated vertex classes in total;
* two edge resolutions, each containing \(\ell/2\) of those classes.

Since phase does not change direction words, a fixed \(q\)-set has, across
one edge-resolution shore, directional occurrence count
\[
       2^{\ell-1}\,
       \mathbf1_{\{D\text{ is a cyclic }q\text{-interval}\}}             \tag{4.16a}
\]
for \(q<\ell\). Fibering in \(Q_s\) multiplies this by
\(2^{s-\ell}\).

For general \(q\), summing (4.15) times the within-class multiplicity over
one shore gives
\[
                         2^{q-1-r_I}2^{r_I}=2^{q-1}      \tag{4.16}
\]
occurrences of every affine interval face. Across both shores this is the
\(2^q\) total in Theorem 4.1.

There is an equivalent parity statement. For the fixed interval phase
\(j\), the starts supplied by all classes in one shore are exactly one
parity shore of \(Q_\ell\). Every affine \(q\)-face has \(2^{q-1}\)
vertices of that parity, which gives (4.16) directly.

### Theorem 4.3 (exact replicated-fibre selection criterion)

Assume face-simplicity through depth \(q\), so \(r_I=0\) for every cyclic
\(q\)-interval \(I\). Take \(R\) replicated copies of the same Hamming
system and, in each copy, select one class label from \(A_0\). Let
\(n(a)\) be the number of selected copies carrying label \(a\).

Here “replicated” means that the copies are identified with the same
labelled affine-face catalogue. It is a local incidence theorem. If the
copies are placed on disjoint physical subcubes, their spectator labels
make their face catalogues different; if they are superposed on the same
cube, they use every middle owner \(R\) times. Thus the theorem is not by
itself a coefficient-one owner packing.

It also assumes, rather than proves, simultaneous parity-shore and
face-simple structure for the chosen syndrome system.

For a positive integer \(c\), the resulting windows cover every affine
face in every interval direction \(I\) exactly \(c\) times if and only if
\[
                  \sum_{a\in b+B_I}n(a)=c
        \quad\text{for every interval }I
        \text{ and every coset }b+B_I\subseteq A_0.      \tag{4.17}
\]
Necessarily
\[
                              R=c\frac{\ell}{2^q}.        \tag{4.18}
\]
For \(c=1\), this says exactly that the multiset of selected labels is a
common transversal of the coset partitions
\[
                              A_0/B_I                    \tag{4.19}
\]
for all cyclic \(q\)-intervals \(I\). In particular its labels are distinct.

#### Proof

At face-simple depth, (4.14) is one coset of \(B_I\), and a selected label
in that coset contributes exactly one occurrence to the corresponding face.
All faces with the same admissible-label coset have identical support.
Therefore their common load is the left side of (4.17), proving necessity
and sufficiency. There are
\[
                        |A_0/B_I|
                           =\frac{\ell/2}{2^{q-1}}
                           =\frac{\ell}{2^q}              \tag{4.20}
\]
cosets. Summing (4.17) over them gives (4.18). \(\square\)

The weighted version without face-simplicity is equally exact: replace the
right side of (4.17) by \(c/2^{r_I}\). In particular, unit occurrence
coverage cannot use a face with \(r_I>0\), since every nonzero contribution
from one class then has multiplicity at least two.

### Corollary 4.4 (Fourier form and a common-complement sufficient condition)

Let \(\widehat{A_0}\) be the character group. Equation (4.17) is equivalent
to
\[
       \widehat n(\chi)=0
       \quad\text{for every nontrivial }\chi
       \text{ which annihilates at least one }B_I,        \tag{4.21}
\]
together with the total mass (4.18). This follows by Fourier transforming
the convolution \(n*1_{B_I}\).

A sufficient integral construction for \(c=1\) is a subspace
\(C\le A_0\) such that
\[
                             A_0=C\oplus B_I              \tag{4.22}
\]
for every interval \(I\). Selecting every label of \(C\) once gives the
required common transversal. This condition is sufficient, not asserted
necessary; nonlinear common transversals may exist.

### Corollary 4.5 (sharp rank-two invariant)

At \(q=2\), write
\[
                       b_i=\Psi(e_{\sigma_i})
                          +\Psi(e_{\sigma_{i+1}})\in A_0. \tag{4.23}
\]
Then \(B_{I_i}=\langle b_i\rangle\). A common once-only transversal exists
if and only if the vectors \(b_i\) have no odd zero-sum relation.
Equivalently, there exists a linear functional
\[
                         \chi:\langle b_i:i\rangle
                                  \longrightarrow\mathbb F_2
                         \quad\text{with}\quad
                         \chi(b_i)=1\ \text{for every }i. \tag{4.24}
\]

#### Proof

A set \(C\subseteq A_0\) is a transversal of every coset of
\(\langle b_i\rangle\) precisely when its sign function
\(g=1_C-1_{A_0\setminus C}\) satisfies
\[
                              g(x+b_i)=-g(x)              \tag{4.25}
\]
for every \(i,x\). An odd relation among the \(b_i\) would iterate (4.25)
back to \(g(x)=-g(x)\), impossible. Conversely, if there is no odd
relation, assigning every generator \(b_i\) the value one defines a
consistent homomorphism \(\chi\) on their span. On each coset of that span,
choose one of the two signs and put
\(g(x+h)=(-1)^{\chi(h)}g(x)\). Then (4.25) holds, and its positive shore is
a common transversal. \(\square\)

This is an exact storage invariant: the even cyclic relation
\(\sum_i b_i=0\) causes no obstruction because \(\ell\) is even, but any
additional odd relation rules out the entire rank-two replicated-class
scheme.

Writing \(a_i=\Psi(p_i)\), so that
\(\Psi(e_{\sigma_i})=a_{i+1}+a_i\), gives
\[
                              b_i=a_i+a_{i+2}.            \tag{4.26}
\]
Thus (4.24) is equivalently the existence of a linear functional whose
binary trace \(y_i=\chi(a_i)\) along the prefix-syndrome order satisfies
\[
                              y_{i+2}=y_i+1.              \tag{4.27}
\]
The trace must therefore have one of the four-periodic forms determined by
\((y_0,y_1,1-y_0,1-y_1)\). This gives a directly checkable symbolic
rank-two obstruction without enumerating resolution classes.

## 5. Counts over cyclic orders and active coordinate frames

There are \((\ell-1)!\) directed cyclic orders on a fixed labelled active
set. A fixed \(q\)-set \(D\) is a cyclic interval in exactly
\[
                              q!(\ell-q)!                 \tag{5.1}
\]
of them: contract \(D\) to one cyclic block and order its elements
internally. Hence
\[
              \Pr_\sigma(D\text{ is an interval})
                    =\frac{\ell}{\binom\ell q}.          \tag{5.2}
\]
Combining (5.2) with Proposition 3.1, the mean directional occurrence load
of \(D\) in one uniformly chosen order class is
\[
                               \frac{2^\ell}{\binom\ell q}. \tag{5.3}
\]

More generally, work in \(Q_s\), choose an active set \(A\) of size
\(\ell\), fibre over the other coordinates, and use one phase class on each
active fibre. In the full \(S_s\)-indexed coordinate-permutation orbit of
one such resolution, a fixed \(q\)-set \(D\) has total occurrence count
\[
                              2^s q!(s-q)!                \tag{5.4}
\]
for \(1\le q\le\ell\). For \(q<\ell\), this follows because the base
class has \(\ell\) interval sets, each has \(q!(s-q)!\) coordinate
permutations mapping it to \(D\), and every contributing class supplies
\(2^s/\ell\) occurrences. The case \(q=\ell\) follows directly by mapping
the whole active set to \(D\).

If one takes every active set, every unoriented cyclic order on it, and all
\(\ell\) phases, then a fixed \(D\) has total occurrence
\[
              \frac{2^{s-1}q!(s-q)!}{(s-\ell)!}.          \tag{5.5}
\]
Choosing any one phase for each active-set/order pair divides (5.5) by
\(\ell\) and remains exactly direction-balanced, since phases do not change
direction words.

Dividing this selected directional total by the \(2^{s-q}\) affine faces
with direction set \(D\) gives the forced average physical-face load
\[
             \boxed{
             \mu_{s,\ell,q}
               =\frac{2^{q-1}q!(s-q)!}
                      {\ell(s-\ell)!}.}                  \tag{5.6}
\]
Therefore exact affine-face balance in this one-class-per-order experiment
requires
\[
                         \mu_{s,\ell,q}\in\mathbb Z.     \tag{5.7}
\]
For \(s=\ell=4,q=1\), the forced average is \(3/2\), so exact balance is
impossible despite exact directional balance. Integrality is only a first
cut: when (5.7) holds, the phase choices must still solve the simultaneous
affine-coset equations of Theorem 4.3.

### Proposition 5.1 (exact direction-level selector criterion)

Let \(\mathcal G\) be a multiset of \(R\) active-support/cyclic-order
geometries in \(Q_s\), and choose an arbitrary syndrome phase class for
each geometry. For \(q<\ell\) and \(D\in\binom{[s]}q\), put
\[
 c_q(D)=|\{g\in\mathcal G:D\text{ is a cyclic interval of }g\}|.
 \tag{5.8}
\]
Then its unlabelled direction load is exactly
\[
                         N_q(D)=\frac{2^s}{\ell}c_q(D). \tag{5.9}
\]
Consequently all \(q\)-direction sets have equal load if and only if
\(c_q(D)\) is constant, in which case necessarily
\[
                         c_q(D)=\frac{R\ell}{\binom sq}. \tag{5.10}
\]
In particular \(\binom sq\mid R\ell\) is necessary. The complete symmetric
orbit supplies such a design simultaneously for every \(q<\ell\).

#### Proof

Formula (5.9) is (0.1) summed over the selected geometries; the phase label
does not occur. Every geometry contains exactly \(\ell\) cyclic
\(q\)-interval sets, so summing \(c_q(D)\) over \(D\) gives \(R\ell\).
This proves (5.10) and the criterion. Symmetric-group transitivity proves
the last assertion, with the exact multiplicity already evaluated in
(5.4). \(\square\)

This proposition concerns a histogram of direction labels. If the \(R\)
objects are distinct physical subcubes, their affine faces have different
spectator labels; summing their direction histograms does not balance those
labelled faces or their Boolean intersection targets.

Equations (5.3)--(5.5) are direction-set statements only. They do not imply
equal incidence on the \(2^{s-q}\) affine faces having direction set
\(D\).

## 6. The uniform fractional affine design

Let \(\mathscr R_h\) be any family of face-simple resolution classes closed
under translations and coordinate permutations of \(Q_h\). The affine
group is transitive on the
\[
                              2^{h-q}\binom hq             \tag{6.1}
\]
affine \(q\)-faces. Every resolution class has \(2^h\) depth-\(q\)
starting windows. Therefore a uniform random class hits a fixed affine face
with probability
\[
                               p_{h,q}
                              =\frac{2^h}{2^{h-q}\binom hq}
                              =\frac{2^q}{\binom hq}.      \tag{6.2}
\]
Without face-simplicity, (6.2) remains the exact expected occurrence
multiplicity, but not the hit probability.

Now fix a lower rank-\(m-q\) target of pair type \((f,q)\). It has
\(f+q\) empty coordinate pairs and exactly
\[
                              d_{f,q}=\binom{f+q}{q}       \tag{6.3}
\]
candidate source faces, lying in distinct source fibres of dimension
\[
                              h=m-2f.                     \tag{6.4}
\]
Uniform fractional class weights in every source fibre therefore give the
target load
\[
                        \lambda_{f,q}=d_{f,q}p_{h,q}
                        =\frac{2^q\binom{f+q}{q}}
                               {\binom{m-2f}{q}}.         \tag{6.5}
\]

Using
\[
 T_{f,q}=\frac{m!}{f!(f+q)!(m-2f-q)!}2^{m-2f-q},
 \qquad
 V_f=\frac{m!}{f!^2(m-2f)!}2^{m-2f},                    \tag{6.6}
\]
direct division gives
\[
                              T_{f,q}\lambda_{f,q}=V_f. \tag{6.7}
\]

### Theorem 6.1 (exact fractional boundary)

The complete affine orbit of the linear-code resolution gives a uniform
fractional load on every labelled target inside each fixed pair type, and
that load is exactly \(\lambda_{f,q}=V_f/T_{f,q}\). It gives fractional
unit coverage of type \((f,q)\) if and only if (0.6) holds. In particular,
full symmetry does not remove the pair-type bias; it merely distributes the
available type mass uniformly.

### 6.1 Exact labelled class-selection equations

The affine support law can be inserted directly into the target assignment,
without any averaging, but the variables must index literal active
subcubes rather than whole source strata. Fix in every source orientation
stratum \(\sigma=(F_0,E_0,R)\) a physical partition into coordinate
\(Q_\ell\)-subfibres
\[
                  \beta=(\sigma,A_\beta,\zeta_\beta),
 \qquad |A_\beta|=\ell,                                \tag{6.8}
\]
where \(A_\beta\subseteq R\) is the active coordinate set and
\(\zeta_\beta\) records the spectator orientation on
\(R\setminus A_\beta\). For each \(\beta\), fix its Hamming quotient
\(\Psi_\beta\), cyclic order, and one edge-resolution shore
\(A_{0,\beta}\). Introduce binary variables
\[
                         x_{\beta,a}\in\{0,1\},
                         \qquad a\in A_{0,\beta},         \tag{6.9}
\]
with the one-class equation
\[
                         \sum_{a\in A_{0,\beta}}
                              x_{\beta,a}=1
                         \qquad(\text{every }\beta).     \tag{6.10}
\]

Let \(T=(F,E,S,\theta)\) be a lower target of type \((f,q)\). For each
\(D\in\binom Eq\), its candidate source stratum is
\[
                         \sigma_D=(F,E\setminus D,S\cup D), \tag{6.11}
\]
and its candidate affine face \(\mathcal F_D(T)\) is the one with free
directions \(D\) and residual orientation \(\theta\). Let
\(\beta_D(T)\) be the unique member of the fixed physical subfibre
partition which contains all of \(\mathcal F_D(T)\), if such a member
exists. (For a common active set in \(\sigma_D\), this is equivalent to
\(D\subseteq A_{\beta_D}\), and the spectator word is then forced by
\(\theta\).) Put
\[
 \mathcal D(T)=\{D\in\binom Eq:\beta_D(T)\text{ exists and }D
                   \text{ is a cyclic interval in }\beta_D(T)\}. \tag{6.12}
\]
For \(D\in\mathcal D(T)\), let \(p_{j(D)}\) be its interval prefix and
let \(z_{T,D}\) be any vertex of the candidate face, expressed in the
local coordinates of \(\beta_D(T)\). Define
\[
 S^-_{T,D}
  =A_{0,\beta_D(T)}\cap
   \left(
     \Psi_{\beta_D(T)}(z_{T,D}+p_{j(D)})
       +\Psi_{\beta_D(T)}(V_D)
   \right),                                             \tag{6.13}
\]
\[
 r_{T,D}=\dim(\ker\Psi_{\beta_D(T)}\cap V_D).           \tag{6.14}
\]
The exact lower-target occurrence equation is
\[
 \boxed{
   \sum_{D\in\mathcal D(T)}
       2^{r_{T,D}}
       \sum_{a\in S^-_{T,D}}x_{\beta_D(T),a}=1.}        \tag{6.15}
\]
The upper equation is identical after replacing the candidate-fibre rule by
the complementary full-pair rule and using the corresponding affine face.

### Proposition 6.2 (necessity and sufficiency)

Equations (6.10), (6.15), and their upper analogues are necessary and
sufficient for a selection of one shore class per fibre to give every
specified lower and upper target exactly one consecutive-window occurrence,
relative to the fixed physical \(Q_\ell\)-subfibre partitions.

#### Proof

Equations (4.14)--(4.15) give all and only the class labels which contain
the physical candidate face, and give its exact within-class multiplicity. Distinct
candidate sets \(D\) lie in distinct source fibres, so their contributions
add exactly as in (6.15). Equation (6.10) is precisely the selection of one
class. No further incidence is hidden: the direction interval condition
gives consecutiveness, and the affine face fixes every outside orientation.
The same argument applies to upper faces. \(\square\)

At face-simple depth every nonempty coefficient in (6.15) is one and every
allowed-label set is an affine \((q-1)\)-flat in the shore syndrome space.
Thus the remaining integral problem is a multiple-choice affine-subspace
exact-cover system. Ordinary direction balance records only which of these
sets are empty; it discards the decisive affine cosets.

## 7. Integral class selection: the capacity identity

Choose an arbitrary legal resolution class in every labelled source fibre
of one fixed coordinate-pair frame, at a depth \(q\) for which every source
owner under discussion has a geodesic \(q\)-window. No symmetry, randomness,
common kernel, or common direction word is assumed. Let \(L_q(T)\) be the number of
depth-\(q\) windows whose lower shadow is the labelled target \(T\).

Every source vertex in a type-\(f\) fibre begins exactly one geodesic
depth-\(q\) window, and its lower target has type \((f,q)\). Conversely no
other source type produces a target in \(\mathcal O^-_{f,q}\). Hence (0.5)
holds:
\[
                    \sum_{T\in\mathcal O^-_{f,q}}L_q(T)=V_f. \tag{7.1}
\]

If a Catalan/SCD radius label activates only some starts at depth \(q\),
the left side of (7.1) is at most \(V_f\). Hence every coverage lower bound
below remains valid, and can only become stronger, in the radius-thinned
constant-one formulation.

Let
\[
 H_{f,q}=|\{T:L_q(T)=0\}|,
 \qquad
 X_{f,q}=\sum_T(L_q(T)-1)_+.                             \tag{7.2}
\]
Then the exact hole--excess identity is
\[
                         H_{f,q}-X_{f,q}=T_{f,q}-V_f.    \tag{7.3}
\]
Therefore
\[
                         H_{f,q}\ge(T_{f,q}-V_f)_+.      \tag{7.4}
\]
This proves (0.6)--(0.7) and the asserted universal no-go.

There is also an exact integrality floor for attempted equal-load balance.
Put \(\lambda=V_f/T_{f,q}=k+\theta\), where
\(k\in\mathbb Z_{\ge0}\) and \(0\le\theta<1\). For every integer load
vector of sum \(V_f\),
\[
       \sum_T|L_q(T)-\lambda|
             \ge2T_{f,q}\theta(1-\theta),               \tag{7.5}
\]
\[
       \sum_T(L_q(T)-\lambda)^2
             \ge T_{f,q}\theta(1-\theta).               \tag{7.6}
\]
Indeed the convex minimum at fixed integer sum uses only the values
\(k,k+1\), in proportions \(1-\theta,\theta\). Thus exact equal target
load is impossible unless \(\lambda_{f,q}\) is an integer, even in the
over-capacity types.

The same conclusions hold for upper targets by complementation.

## 8. Exact Gaussian-scale missing density

The fixed-frame deficit can be sharpened from positivity to an explicit
limit. Let
\[
                       N_q=\binom{2m}{m-q},
 \qquad
                       \pi_{m,q}(f)=\frac{T_{f,q}}{N_q}. \tag{8.1}
\]
Suppose
\[
                              q=A\sqrt m+o(\sqrt m),
                              \qquad A>0.                 \tag{8.2}
\]
Define
\[
                  f_* =\frac{(m-q)^2}{4m},
 \qquad
                  Z_m=\frac{4(f-f_*)}{\sqrt m}.          \tag{8.3}
\]

### Lemma 8.1 (type central limit and load profile)

Under \(\pi_{m,q}\),
\[
                              Z_m\Rightarrow Z,
                              \qquad Z\sim N(0,1),        \tag{8.4}
\]
and uniformly for bounded \(Z_m\),
\[
                       \log\lambda_{f,q}
                         =-A^2+2AZ_m+o(1).                \tag{8.5}
\]

#### Proof

The exact type weights are the coefficients obtained by marking full pairs:
\[
 \sum_fT_{f,q}u^f
   =[x^{m-q}](1+2x+ux^2)^m.                              \tag{8.6}
\]
Stirling expansion of the factorial expression (6.6), at
\(f=f_*+z\sqrt m/4\), gives
\[
               \log\frac{T_{f,q}}{T_{\lfloor f_*\rfloor,q}}
                      =-\frac{z^2}{2}+o(1)               \tag{8.7}
\]
uniformly on bounded \(z\), while the ratio test gives Gaussian tail
tightness. This proves (8.4). Equivalently, the full-pair count has variance
\(m/16+o(m)\); the shift \(q=O(\sqrt m)\) changes its centre but not its
leading variance.

For the load, use
\[
 \lambda_{f,q}
   =\prod_{j=1}^{q}
       \frac{2(f+j)}{m-2f-j+1}.                           \tag{8.8}
\]
Substitute \(f=f_*+z\sqrt m/4\). Taylor expansion of each logarithm about
\(m/2\), summed for \(1\le j\le q\), gives
\[
 \begin{aligned}
 \log\lambda_{f,q}
  &=\frac2m\sum_{j=1}^q
       \bigl(\sqrt m(-2A+z)+A^2+3j-1\bigr)+o(1)\\
  &=-A^2+2Az+o(1).
 \end{aligned}                                           \tag{8.9}
\]
The quadratic Taylor terms sum to \(o(1)\), because the leading
\(\sqrt m\) parts of numerator and denominator are opposite and their sum
is only \(O(j+1)\). This proves (8.5). \(\square\)

### Theorem 8.2 (sharp type-capacity deficit)

Under (8.2),
\[
 \frac1{N_q}\sum_f(T_{f,q}-V_f)_+
     \longrightarrow
     \mathbb E\bigl(1-e^{-A^2+2AZ}\bigr)_+              \tag{8.10}
\]
and this expectation equals the constant in (0.8):
\[
                    \kappa(A)
                       =\Phi(A/2)-e^{A^2}\Phi(-3A/2).    \tag{8.11}
\]

#### Proof

By (6.7), the normalized summand is
\(\pi_{m,q}(f)(1-\lambda_{f,q})_+\). Lemma 8.1 and bounded convergence
give (8.10). The integrand is positive precisely for \(Z<A/2\). Exponential
tilting of the standard normal gives
\[
 \mathbb E[e^{-A^2+2AZ}\mathbf1_{Z<A/2}]
       =e^{A^2}\Phi(A/2-2A)
       =e^{A^2}\Phi(-3A/2),                              \tag{8.12}
\]
which proves (8.11). Positivity also follows directly because the integrand
in (8.10) is strictly positive on a set of positive Gaussian measure.
\(\square\)

## 9. What random class selection can and cannot prove

Assume face-simplicity and choose, independently in every source fibre, a
uniform class from a full affine-symmetric reservoir, including active-frame
and cyclic-order variation. For a fixed type-\((f,q)\) target, its
\(d_{f,q}\) candidate faces lie in distinct fibres. Hence its load has the
exact binomial law
\[
                         L_q(T)\sim
                         \operatorname{Bin}
                         \left(\binom{f+q}{q},
                               \frac{2^q}{\binom{m-2f}{q}}\right),          \tag{9.1}
\]
with mean \(\lambda_{f,q}\).

This gives a valid positive statement in the high-load region. If
\(\mathcal T\) is any finite collection of targets and
\(L=\log(2|\mathcal T|)+1\), Bernstein's inequality and a union bound give
an integral choice of one class per fibre satisfying simultaneously
\[
             |L_q(T)-\lambda_{f,q}|
                \le 2\sqrt{\lambda_{f,q}L}+2L
                \qquad(T\in\mathcal T).                  \tag{9.2}
\]
Thus relative balancing follows where \(\lambda_{f,q}\gg m\).

But (9.1) also shows why independent Hamming-class selection does not solve
the central shadow problem: at typical central types
\(\lambda_{f,q}=O(1)\), so the miss probability stays of constant order.
The deterministic identity (7.3), not the probabilistic estimate, is the
stronger obstruction in every under-capacity type.

## 10. Precise proved boundary

The following statements are proved.

1. The direction-set incidences of every isometric-cycle resolution are
   exactly (2.2)--(2.4).
2. The linear translate system has exactly \(\ell\) phase classes, all
   direction-inert relative to one another; the parity system splits them
   into two \(\ell/2\)-class edge resolutions.
3. Its complete affine phase incidence is the block design in Theorem 4.1,
   and exact replicated-fibre balance is equivalent to the common-transversal
   equations (4.17).
4. The complete labelled lower/upper selection problem is exactly the
   multiple-choice affine-coset system (6.10), (6.15), and its upper analogue.
5. Full symmetry gives the exact fractional target load (6.5).
6. No integral selection of one class per fixed-pair fibre can cover every
   \(q\)-target whenever any type has \(\lambda_{f,q}<1\); the exact hole
   floor is (7.4), and the Gaussian limiting floor is (8.11).

What is not proved is an integral labelled balancing theorem after mixing
different coordinate-pair frames. The pair-preserving affine orbit has the
biased degrees (6.5). Full ground-coordinate conjugation is known to remove
that type bias fractionally, but it does not select owner-disjoint integral
factors. The fixed-frame capacity cannot be repaired by any choice among its
phase classes. A coefficient-one construction must route under-capacity
targets through other pair frames while preserving one integral middle
owner and the literal consecutive-window realization.

## 11. Independent audit ledger

The decisive calculations were rederived independently in both the
\(K\oplus\langle\mathbf1\rangle\) quotient model and the parity-syndrome
model. The audit made and checked the following corrections.

1. There are \(\ell\) syndrome-translated **vertex factors**, while one
   edge resolution is a shore containing \(\ell/2\) of them. Thus the
   affine-face totals are \(2^q\) over all vertex factors and \(2^{q-1}\)
   over one shore. Calling a whole shore “one class” would be a factor-two
   error.
2. The distinct-\(\ell\)-class statement needs \(\ell\ge4\). At
   \(\ell=2\), the base \(C_4\) is all of \(Q_2\) and has a larger
   translation stabilizer.
3. The parity functional in (4.10) is an extra property of the
   parity-alternating construction, not a consequence of an arbitrary
   code-transversal kernel. The common-transversal theorem separately
   assumes face-simplicity.
4. The labelled equations initially indexed a whole \(Q_h\) source
   stratum. Equations (6.8)--(6.15) now index the literal active
   \(Q_\ell\)-subfibre, including its active set and spectator orientation.
5. The Gaussian normalization was checked in both units:
   with \(D_{m,q}:=\sum_f(T_{f,q}-V_f)_+\),
   \[
    \frac{D_{m,q}}{N_q}\to
       \Phi(A/2)-e^{A^2}\Phi(-3A/2),
    \qquad
    \frac{D_{m,q}}{W}\to
       e^{-A^2}\Phi(A/2)-\Phi(-3A/2).
   \tag{11.1}
   \]
   These are the same statement because \(N_q/W\to e^{-A^2}\).

No step of the fixed-frame impossibility uses the conditional
face-simplicity/parity compatibility or the replicated-fibre abstraction;
it follows solely from the integral type identity (7.1).
