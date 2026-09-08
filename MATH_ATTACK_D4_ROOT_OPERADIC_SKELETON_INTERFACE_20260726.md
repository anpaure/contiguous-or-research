# Root-aligned four-node operadic skeletons: the spectator-interface obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Fix five ordered spectator trees

\[
                         (A_0,A_1,A_2,A_3,A_4)          \tag{0.1}
\]

and vary a four-node binary skeleton through the fourteen elements of
\(D_4\).

The abstract operadic statement is positive: the five spectators remain in
the same left-to-right input slots for all fourteen skeleton shapes. They
are neither reordered nor identified in the free nonsymmetric binary
operad.

The factor interface is negative. After passage to the physical Dyck-word
coordinates, a nonempty spectator in one of the three interior slots is
shifted when the skeleton changes. The fourteen ports do not form one
affine \(D_4\) face with fixed spectator coordinates, and the natural
extension of the explicit \(G_4\) path does not preserve Johnson
adjacency. Consequently its \(Y\)-union colours also fail.

The obstruction is literal. Take

\[
                         (A_0,A_1,A_2,A_3,A_4)
                           =(\epsilon,10,\epsilon,\epsilon,\epsilon).
                                                               \tag{0.2}
\]

Four expanded skeleton ports have common selected-coordinate intersection
of size one, whereas any common affine suspension of a \(D_4\) port family
with one spectator node would have intersection size two. Moreover the
first edge

\[
                         1234\longrightarrow1238       \tag{0.3}
\]

of the displayed \(G_4\)-row expands to two \(5\)-sets at Johnson distance
two, not one.

More generally, this single edge proves that the natural leaf-slot
expansion can be a Johnson lift only if

\[
                         A_1=A_2=A_3=\epsilon.          \tag{0.4}
\]

The number of ordered spectator tuples satisfying (0.4) is only

\[
                         [z^{s-4}]C(z)^2=C_{s-3}.       \tag{0.5}
\]

Even granting every such tuple as a legal disjoint packet, its fourteen
ports cover at most

\[
                         14C_{s-3}
                           =\left(\frac7{32}+o(1)\right)C_s         \tag{0.6}
\]

root incidences. Therefore the proposed direct operadic suspension cannot
give a \(B=14\) packetization covering \(1-o(C_s)\).

This is a coordinate-absorption obstruction, not spectator reordering:
the ordered inputs survive abstractly, but their up/down-step positions are
absorbed into the changing skeleton chronology. A new collective
five-input path factor could conceivably reroute the internal states instead
of expanding the \(G_4\) path statewise. Such an object would be a new
operadic \(X/Y\)-composition theorem, not a suspension of the existing
factor.

The proposed Catalan one-big-fringe repair does make the abstract fibres
disjoint, but its concentration premise is false.  If \(k\) is the size of
the context outside the unique minimal fringe subtree larger than \(s/2\),
then \(k/s\) has a nondegenerate limiting density on \((0,1/2)\).  In
particular, a cutoff \(L\to\infty\), \(L=o(s)\), retains only
\[
                  \left(\frac4{3\pi}+o(1)\right)(L/s)^{3/2}=o(1)
                                                               \tag{0.7}
\]
of the roots, rather than discarding \(o(1)\).  Recursion therefore still
needs a uniform near-factor theorem for pointed macroscopic contexts, and
a packet which crosses the marked-hole ancestry still encounters the
five-input \(X/Y\) obstruction.

## 1. Ordered slots do survive abstractly

Use the standard recursive encoding of a binary tree,

\[
                         T=1\,T_L\,0\,T_R.              \tag{1.1}
\]

A four-node skeleton has five leaves. Substituting \(A_i\) into its
\(i\)-th leaf is the defining composition in the free nonsymmetric binary
operad.

### Lemma 1.1 (abstract slot preservation)

For every \(S\in D_4\), the substituted tree

\[
                         S(A_0,A_1,A_2,A_3,A_4)         \tag{1.2}
\]

contains the spectators in the order \(A_0,A_1,A_2,A_3,A_4\). Distinct
skeletons give distinct substituted trees.

#### Proof

Nonsymmetric operadic composition preserves the planar order of inputs by
definition. Collapsing each marked spectator subtree in (1.2) back to a
leaf recovers \(S\), so two different skeletons cannot give the same marked
substitution. \(\square\)

Thus there is no abstract permutation of the five slots. The issue is
whether the marked slots define one common physical coordinate interface
after the marks are forgotten.

## 2. The canonical expansion on balanced words

Let \(x\) be a binary word with four ones and four zeros. Number its zeros
from left to right. Define

\[
                         \mathsf E_{\mathbf A}(x)       \tag{2.1}
\]

by inserting \(A_i\) immediately before the \((i+1)\)-st zero for
\(0\le i\le3\), and appending \(A_4\) after the word.

### Lemma 2.1

If \(x\in D_4\), then \(\mathsf E_{\mathbf A}(x)\) is exactly the Dyck word
of the operadic substitution (1.2).

#### Proof

For the one-node skeleton \(10\), the two leaf substitutions give

\[
                         1A_0\,0A_1,                   \tag{2.2}
\]

which is the stated zero-slot rule. Under the recursion (1.1), the zeros of
the left subtree occur first, followed by the root zero, followed by the
zeros of the right subtree. These are precisely the separators preceding
the leaves in planar order. Induction on the skeleton proves (2.1).
\(\square\)

Formula (2.1) is also the unique direct statewise extension which retains
the same ordered zero slots for an arbitrary balanced intermediate word.
The proposed suspension of the explicit \(D_4\) path factor would therefore
send each local \(X\)-state \(x\) to \(\mathsf E_{\mathbf A}(x)\).

## 3. Failure of a common affine port interface

Take the spectator tuple (0.2). Expanding four Dyck ports gives

\[
\begin{array}{c|c|c}
P&\mathsf E_{\mathbf A}(P)&
       \text{up-step positions}\\ \hline
1234&1111010000&\{1,2,3,4,6\}\\
1357&1011001010&\{1,3,4,7,9\}\\
1245&1101110000&\{1,2,4,5,6\}\\
1236&1110100100&\{1,2,3,5,8\}.
\end{array}                                             \tag{3.1}
\]

Their four up-step sets have intersection \(\{1\}\). Every Dyck word begins
with an up-step, so the intersection of all fourteen expanded ports is
exactly

\[
                              \{1\}.                    \tag{3.2}
\]

### Theorem 3.1 (affine port obstruction)

The fourteen ports obtained from (0.2) are not a common affine \(D_4\)
port family.

#### Proof

A common suspension through one fixed spectator node would have a
decomposition

\[
                         P^{\rm glob}=A^+\cup\iota(P),  \tag{3.3}
\]

where \(A^+\) is the fixed selected spectator coordinate, the local
injection \(\iota:[8]\hookrightarrow[10]\) has image disjoint from
\(A^+\), and \(P\) ranges over \(D_4\). The intersection of all local
\(D_4\) ports is the singleton \(\{1\}\). Hence the intersection of all
sets in (3.3) has size

\[
                         |A^+|+1=2.                    \tag{3.4}
\]

This contradicts (3.2). \(\square\)

Thus the spectator's selected coordinate cannot be kept in a fixed
exterior set. Its physical word position is absorbed into the changing
skeleton.

## 4. An explicit Johnson-edge obstruction

The first row of the noncanonical factor begins

\[
                         1234\longrightarrow1238.       \tag{4.1}
\]

As binary words these states are

\[
                         x=11110000,\qquad x'=11100001. \tag{4.2}
\]

Under the spectator tuple (0.2),

\[
\begin{aligned}
 \mathsf E_{\mathbf A}(x)
    &=1111010000,
 &X&=\{1,2,3,4,6\},\\
 \mathsf E_{\mathbf A}(x')
    &=1110100001,
 &X'&=\{1,2,3,5,10\}.
\end{aligned}                                          \tag{4.3}
\]

Therefore

\[
                         |X\cap X'|=3.                 \tag{4.4}
\]

Both sets have size five, so their Johnson distance is two.

### Theorem 4.1 (failure of the \(X/Y\) interface)

The statewise operadic expansion of \(G_4\) through (0.2) is not a
complementary Johnson path factor.

#### Proof

Consecutive states of a size-five complementary geodesic must intersect in
four coordinates. Equation (4.4) gives intersection three on the very first
edge. Equivalently their union has size seven rather than six, so there is
no legal adjacent-union \(Y\)-colour either. \(\square\)

This failure occurs before questions of global ownership, packet overlap,
or cap descent.

## 5. The general interior-spectator obstruction

For arbitrary spectators, the two words in (4.2) expand as

\[
\begin{aligned}
 \mathsf E_{\mathbf A}(x)
  &=1111\,A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0\,A_4,\\
 \mathsf E_{\mathbf A}(x')
  &=111\,A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0\,1\,A_4.
\end{aligned}                                          \tag{5.1}
\]

Put

\[
                         M=A_0\,0\,A_1\,0\,A_2\,0\,A_3\,0.        \tag{5.2}
\]

After their common initial \(111\) and before their common suffix \(A_4\),
the two words are \(1M\) and \(M1\). Their Hamming distance is the number
of bit changes around the string

\[
                         1,m_1,m_2,\ldots,m_{|M|},1.    \tag{5.3}
\]

### Lemma 5.1

If at least one of \(A_1,A_2,A_3\) is nonempty, then the two expansions in
(5.1) have Hamming distance at least four and Johnson distance at least
two.

#### Proof

Every nonempty Dyck spectator starts with \(1\) and ends with \(0\). Before
each of \(A_1,A_2,A_3\) lies the displayed separator \(0\). Thus a nonempty
interior spectator creates a \(0\to1\) transition inside \(M\). Also \(M\)
ends with the final displayed \(0\), followed by the terminal \(1\) in
(5.3), giving a second \(0\to1\) transition. In a binary string beginning
and ending with \(1\), the number of \(1\to0\) transitions equals the
number of \(0\to1\) transitions. Hence (5.3) has at least four bit changes.

The two expanded sets have equal cardinality, so their Johnson distance is
half their Hamming distance. \(\square\)

### Corollary 5.2 (necessary spectator restriction)

The direct statewise suspension of the explicit \(G_4\) factor can be
legal only if

\[
                         A_1=A_2=A_3=\epsilon.          \tag{5.4}
\]

This condition is only necessary. A complicated \(A_0\) can create further
bit changes, so not every tuple satisfying (5.4) is asserted to work.

## 6. Exact coverage ceiling

Let \(s=4+\sum_i|A_i|\), where sizes count internal tree nodes. The number
of ordered five-spectator tuples of total size \(s-4\) is

\[
\begin{aligned}
 E_s&=[z^{s-4}]C(z)^5\\
    &=\frac5{2s-3}\binom{2s-3}{s-4}.                  \tag{6.1}
\end{aligned}
\]

Each tuple gives a fourteen-element root-skeleton edge. Thus the full
skeleton hypergraph has average vertex degree

\[
                         \frac{14E_s}{C_s}
                              \longrightarrow\frac{35}{8}.         \tag{6.2}
\]

Its edges overlap: once spectator marks are forgotten, one large tree may
admit several top-skeleton decompositions. The bounded average degree in
(6.2) supplies no near-perfect matching theorem.

The obstruction above is stronger for the direct \(G_4\) suspension.
Condition (5.4) leaves only the two outer spectators free. Their number is

\[
\begin{aligned}
 E_s^{\rm adm}
   &\le[z^{s-4}]C(z)^2\\
   &=C_{s-3}.                                           \tag{6.3}
\end{aligned}
\]

Even if every admissible edge were legal and the edges could be chosen
without overlap, the number of covered roots would be at most

\[
                         14C_{s-3}.                    \tag{6.4}
\]

Since \(C_{s-3}/C_s\to4^{-3}\),

\[
 \boxed{
        \frac{\text{covered roots}}{C_s}
            \le\frac7{32}+o(1).}                       \tag{6.5}
\]

This rules out a \(B=14\) parent-aligned packetization covering
\(1-o(C_s)\) via the proposed statewise operadic suspension.

## 7. The exact surviving possibility

The negative result has precise scope.

1. The fourteen skeleton shapes do preserve the five abstract ordered
   spectator slots.
2. They do not preserve one common affine port ground after physical
   Dyck-word expansion.
3. Expanding the internal states of the existing \(G_4\) factor violates
   Johnson adjacency and therefore the \(X/Y\) ledger interface.
4. Restricting to spectator tuples which pass even the first-edge test
   leaves at most a \(7/32+o(1)\) root-incidence fraction.

A possible repair must replace the statewise expansion by a new collective
factor. For every spectator tuple it would need to construct fourteen
global complementary geodesics whose endpoints are the operadically
grafted ports, and then prove common global \(X\)- and \(Y\)-ownership
ledgers. Such paths may reroute spectator exchanges in a row-dependent
order; they are not obtained by applying \(\mathsf E_{\mathbf A}\) to the
five states of each local \(G_4\) row.

Even after such a new five-input factor theorem, the overlapping
fourteen-uniform skeleton hypergraph would still require a matching
covering \(1-o(C_s)\). Neither assertion follows from the finite \(D_4\)
certificate.

Thus the successor gate is negative for the proposed suspension and remains
open only after replacing it by a genuinely new operadic \(X/Y\)-factor
construction.

## 8. Audit of the minimal-big-fringe recursive matching proposal

There is a natural canonical decomposition which at first appears to
remove the overlap in the root-skeleton hypergraph.  For a tree
\(T\in\mathcal D_s\), let \(U(T)\) be the minimal fringe subtree satisfying

\[
                              |U(T)|>s/2,                         \tag{8.1}
\]

and let \(K(T)[\,]\) be the one-hole context obtained by contracting
\(U(T)\) to a leaf.  Put

\[
                              k(T)=|K(T)|=s-|U(T)|.                \tag{8.2}
\]

The canonicalization itself is valid.  Fringe subtrees are either nested
or disjoint; two of size greater than \(s/2\) cannot be disjoint.  Since
the root is eligible, the eligible fringe subtrees form a nonempty chain
and have a unique minimal member.  Moreover, any size-preserving
rebracketing of \(K(T)\) which leaves the marked hole and \(U(T)\) intact
keeps \(U(T)\) canonical.  Its two children still have size at most
\(s/2\), the material outside it has size \(k(T)<s/2\), and every ancestor
is larger than it.  Consequently distinct fixed-\(U\) fibres cannot
collide.

The proposed truncation fails, however, because \(K(T)\) is not small in
the Catalan measure.  The following exact census identifies the error.

### Proposition 8.1 (exact context-size census)

Let \(A_{s,k}\) be the number of trees \(T\in\mathcal D_s\) for which
\(k(T)=k\), and put \(h=\lfloor s/2\rfloor\).  Then

\[
 A_{s,k}
  =(k+1)C_k
     \sum_{\substack{a+b=s-k-1\\0\le a,b\le h}} C_aC_b,
 \qquad 0\le k\le\lceil s/2\rceil-1.                 \tag{8.3}
\]

#### Proof

A one-hole binary-tree context with \(k\) internal nodes is a size-\(k\)
tree with one of its \(k+1\) leaves distinguished, giving
\((k+1)C_k\) choices.  Write \(a,b\) for the sizes of the two children of
the inserted tree \(U\).  It has size \(s-k\), so
\(a+b=s-k-1\).  It is the minimal fringe subtree larger than \(s/2\) if
and only if both children have size at most \(h\).  This gives (8.3), and
the uniqueness just proved makes the construction bijective.  \(\square\)

### Proposition 8.2 (the outside context has a macroscopic law)

If \(L=L(s)\to\infty\) and \(L=o(s)\), then

\[
 \frac1{C_s}\sum_{k\le L}A_{s,k}
   =\left(\frac4{3\pi}+o(1)\right)
      \left(\frac Ls\right)^{3/2}=o(1).               \tag{8.4}
\]

More generally \(k(T)/s\) converges on \(0<\alpha<1/2\) to the probability
density

\[
 f(\alpha)
   =\frac{2\sqrt\alpha}
          {\pi(1-\alpha)^2\sqrt{1-2\alpha}}.           \tag{8.5}
\]

In particular, for every fixed \(0<c<1/2\), the fraction with
\(k(T)>cs\) tends to the positive number
\(\int_c^{1/2}f(\alpha)\,d\alpha\).  A cutoff can discard only \(o(C_s)\)
trees if it approaches the full macroscopic range \(s/2\); a slowly
growing sublinear cutoff does the opposite of what was proposed.

#### Proof

For \(k=o(s)\), the sum in (8.3) has \(k+2\) terms when \(s\) is even and
\(k+1\) terms when \(s\) is odd.  Uniformly for \(k\le L=o(s)\), both
indices in every term equal \(s/2+O(L)\).  The Catalan asymptotic

\[
                         C_j\sim\frac{4^j}{\sqrt\pi j^{3/2}}       \tag{8.6}
\]

therefore gives, after summing over \(k\le L\),

\[
 \frac{A_{s,k}}{C_s}
   =\left(\frac2\pi+o(1)\right)
       \frac{\sqrt k}{s^{3/2}}                                  \tag{8.7}
\]

away from a fixed initial range of \(k\).  Since
\(\sum_{k\le L}\sqrt k\sim(2/3)L^{3/2}\), (8.4) follows; the fixed initial
range is \(O(s^{-3/2})\).

For completeness take \(k/s\to\alpha\in(0,1/2)\), set \(a=xs\), and use
(8.6) in the Riemann sum in (8.3).  One obtains

\[
 \frac{A_{s,k}}{C_s}
   =\frac1s\left(f(\alpha)+o(1)\right),                       \tag{8.8}
\]

where

\[
\begin{aligned}
 f(\alpha)
 &=\frac1{4\pi\sqrt\alpha}
   \int_{1/2-\alpha}^{1/2}
       \frac{dx}{[x(1-\alpha-x)]^{3/2}}\\
 &=\frac{2\sqrt\alpha}
          {\pi(1-\alpha)^2\sqrt{1-2\alpha}}.
\end{aligned}                                                   \tag{8.9}
\]

The substitution \(t^2=\alpha/(1-\alpha)\) gives

\[
                         f(\alpha)\,d\alpha
                            =\frac{4t^2}{\pi\sqrt{1-t^2}}\,dt,
                            \qquad 0<t<1,                       \tag{8.10}
\]

whose integral is one.  Standard endpoint truncation using (8.3) then
upgrades the local limit (8.8) to the asserted weak limit.  Its expansion
\(f(\alpha)\sim(2/\pi)\sqrt\alpha\) at zero also recovers (8.4).
\(\square\)

This explains the apparent conflict with the Catalan one-big-jump
principle.  In a *fixed finite* five-fold Catalan composition conditioned
on its total size, one of the five inputs contains all but a tight
remainder.  The subtree in (8.1) is instead the **minimal** subtree above
half size.  Reaching it requires descending the successive giant-child
spine until the accumulated outside context is macroscopic.  The two
objects are not interchangeable.

There are two further gates even if one abandons the false cutoff.

First, (8.3) gives only a disjoint canonical fibration.  A near-factor of
the pointed contexts is still required.  If \(R_k\) pointed size-\(k\)
contexts are left uncovered, the induced number of uncovered size-\(s\)
trees is exactly

\[
 \sum_{k< s/2}
 R_k\!\!\sum_{\substack{a+b=s-k-1\\a,b\le\lfloor s/2\rfloor}}
 C_aC_b.                                                       \tag{8.11}
\]

Thus uniqueness prevents cross-fibre overlap, but supplies neither the
fourteen-element packets nor a small residual.  Recursing on \(k<s/2\)
is a legitimate induction scheme only after a uniform near-factor theorem
for **pointed** contexts has been proved.

Second, the \(X/Y\) interface splits sharply according to the position of
the local rebracketing.  A \(D_4\) switch wholly inside a fixed part of
\(K(T)\) and away from the marked-hole ancestry is wrapped by one common
one-hole context; the existing unary context theorem makes that switch
legal after \(U\) is restored.  It is then an interior/fringe switch, not
the desired five-input parent-aligned suspension.  If the four-node
skeleton meets the marked-hole ancestry, restoring \(U\) becomes a
five-input substitution rather than a common outer one-hole context.  In
the moving or interior input slots the physical \(U\)-coordinates shift
among the fourteen rows; Sections 3--5 then show that the common affine
port can fail and that even the displayed first edge can lose Johnson
adjacency.  The exceptional aligned suffix slots form only the sparse
subfamilies already bounded in Section 6.  Canonical selection of \(U\)
changes none of these calculations.

Hence the one-big-fringe construction has a valid no-overlap skeleton but
does not yield the proposed near-perfect parent-aligned packetization:
its small-context tail estimate is false, and the only recursively lifted
switches already certified by the \(X/Y\) theorem are the common-context
interior switches.  A packet crossing the serviced hole still requires
the genuinely new collective five-input factor isolated in Section 7.
