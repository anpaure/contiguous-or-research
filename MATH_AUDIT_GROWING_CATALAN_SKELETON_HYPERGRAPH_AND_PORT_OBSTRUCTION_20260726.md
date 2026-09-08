# Growing Catalan skeleton packets: exact census, high codegrees, and a port-interface obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(\mathcal T_s\) be the ordered full binary trees with \(s\)
internal nodes, so \(|\mathcal T_s|=C_s=\operatorname {Cat}_s\).
For \(t\le s\), fix an ordered \((t+1)\)-tuple of spectator trees

\[
                         \mathbf A=(A_0,\ldots,A_t),
 \qquad \sum_{i=0}^{t}|A_i|=s-t,                       \tag{0.1}
\]

and let

\[
 E_{\mathbf A}
 =\{S(A_0,\ldots,A_t):S\in\mathcal T_t\}.              \tag{0.2}
\]

Here the right side is nonsymmetric operadic substitution into the
ordered leaves of the \(t\)-node skeleton \(S\).  Every edge has exactly
\(C_t\) vertices.

The proposed average-degree calculation is correct.  If
\(\mathcal H_{s,t}\) is the resulting \(C_t\)-uniform hypergraph on
\(\mathcal T_s\), then

\[
 |E(\mathcal H_{s,t})|
 =\frac{t+1}{2s-t+1}\binom{2s-t+1}{s-t},               \tag{0.3}
\]

and its average degree is

\[
 \boxed{
 \overline d_{s,t}
 =\binom{2t}{t}\frac{(2s-t)!\,s!}{(s-t)!\,(2s)!}
 =\binom{2t}{t}\prod_{i=0}^{t-1}\frac{s-i}{2s-i}.}     \tag{0.4}
\]

Consequently, if \(t=o(\sqrt s)\),

\[
                 \overline d_{s,t}
                 =(1+o(1))\frac{2^t}{\sqrt{\pi t}}.    \tag{0.5}
\]

This does not yield a near-perfect matching theorem.  The hypergraph is
not pseudorandom at the scale required by a nibble: it has degree-one
vertices and, when \(2^t\ll s\), distinct vertex pairs with codegree
\(C_{t-2}\gg\overline d_{s,t}\).

There is a more decisive obstruction to using these edges as
shape-respecting path-factor packets.  The literal operadic port interface
for \(E_{\mathbf A}\) requires a fixed set \(W\) and a fixed coordinate
injection \(\iota\) such that

\[
 \operatorname {port}\bigl(S(\mathbf A)\bigr)
     =W\mathbin{\dot\cup}\iota(\operatorname {port}(S))
                    \qquad(S\in\mathcal T_t).           \tag{0.6}
\]

For \(t\ge3\), (0.6) forces

\[
 \boxed{
 A_0\text{ is a mountain tree},\qquad
 A_1=\cdots=A_{t-2}=\varnothing,}                      \tag{0.7}
\]

while only \(A_{t-1},A_t\) remain unrestricted.  Hence the number of
skeleton edges which can even pass this port test is at most

\[
 B_{s-t}:=[z^{s-t}]\frac{C(z)^2}{1-z}
          =\sum_{j=0}^{s-t}C_{j+1}.                    \tag{0.8}
\]

If \(t\to\infty\) and \(t=o(s)\), the union of all such edges has size at
most

\[
 C_t B_{s-t}
 \le\left(\frac{16}{3\sqrt\pi}+o(1)\right)
              \frac{C_s}{t^{3/2}}
 =o(C_s).                                              \tag{0.9}
\]

Thus growing the skeleton does not repair the bounded-seed coverage
problem in its proposed shape-respecting form.  Almost all roots lie
outside every skeleton packet having the common fixed-coordinate port
interface which transports the row indexed by \(S\) to the inflated row
indexed by \(S(\mathbf A)\).  The obstruction occurs before the \(X/Y\)
ledgers.

An arbitrary reindexing of the Catalan ports, or a collective
row-dependent construction, is not ruled out by (0.6).  Either would
require a new common-port isomorphism and a new \(X/Y\) proof; it is not
the prescribed operadic substitution of a local \(\mathcal D_t\) factor.
At that point one is already constructing a genuinely new
\(\mathcal D_s\) path factor.  This is the correct pivot.

The suggested heavy-spine canonicalization does not evade this conclusion.
Even with one spectator larger than the skeleton and every other spectator
combined, its depth varies across the \(C_t\) bracketings.  The first
\(t\) heavy nodes therefore do not select a common edge.

## 1. The skeleton hypergraph

Use the recursive tree operation \(N(L,R)\), with the empty tree
\(\varnothing\) as a leaf.  The Dyck encoding is

\[
                  w(N(L,R))=1\,w(L)\,0\,w(R).          \tag{1.1}
\]

If \(S\) has \(t\) internal nodes, it has \(t+1\) ordered leaves.
Replacing its \(i\)-th leaf by \(A_i\) gives the tree
\(S(A_0,\ldots,A_t)\), whose size is (0.1).

### Lemma 1.1 (fixed-tuple injectivity)

For every fixed ordered tuple \(\mathbf A\), the map

\[
                  S\longmapsto S(\mathbf A)            \tag{1.2}
\]

from \(\mathcal T_t\) to \(\mathcal T_s\) is injective.  Therefore every
edge (0.2) has cardinality exactly \(C_t\).

#### Proof

Suppose the left child of the skeleton root has \(r\) internal nodes.
It contains the first \(r+1\) skeleton leaves, so after substitution its
size is

\[
                    r+\sum_{i=0}^{r}|A_i|.             \tag{1.3}
\]

As a function of \(r\), (1.3) is strictly increasing: the next increment
is \(1+|A_{r+1}|>0\).  Hence the root split of the inflated tree uniquely
determines \(r\).  The same argument applied recursively to the two
children recovers the whole skeleton \(S\).  \(\square\)

## 2. Exact edge and incidence counts

Let

\[
                    C(z)=\sum_{r\ge0}C_rz^r
                         =1+zC(z)^2.                   \tag{2.1}
\]

An edge is indexed by an ordered \((t+1)\)-tuple of trees of total size
\(s-t\).  Hence

\[
 |E(\mathcal H_{s,t})|=[z^{s-t}]C(z)^{t+1}.            \tag{2.2}
\]

The standard Lagrange coefficient identity

\[
 [z^n]C(z)^k=\frac{k}{2n+k}\binom{2n+k}{n}             \tag{2.3}
\]

gives (0.3).

Since every edge has \(C_t\) vertices, double counting incidences gives

\[
 \overline d_{s,t}
   ={C_t|E(\mathcal H_{s,t})|\over C_s}.                \tag{2.4}
\]

Substituting (0.3) and the Catalan formula yields

\[
 \overline d_{s,t}
 =\frac{(2t)!}{(t!)^2}
   \frac{(2s-t)!}{(s-t)!}
   \frac{s!}{(2s)!},
\]

which is (0.4).

For \(t=o(s)\),

\[
 \prod_{i=0}^{t-1}\frac{s-i}{2s-i}
 =2^{-t}\exp\left(
       -\frac{t(t-1)}{4s}
       +O\left(\frac{t^3}{s^2}\right)\right).           \tag{2.5}
\]

Together with

\[
                       \binom{2t}{t}
                       =(1+O(t^{-1}))\frac{4^t}{\sqrt{\pi t}},
\]

this proves (0.5) when \(t=o(\sqrt s)\).

## 3. Exact degrees

For a tree \(T\), let \(\mathcal I_t(T)\) be the family of
ancestor-closed sets of exactly \(t\) internal nodes.  Such a set is a
rooted skeleton prefix.  Cutting immediately below it leaves an ordered
frontier of \(t+1\) spectator subtrees.

### Proposition 3.1 (degree formula)

\[
                         d_{\mathcal H}(T)=|\mathcal I_t(T)|.     \tag{3.1}
\]

Equivalently, define the prefix polynomial recursively by

\[
 P_{\varnothing}(u)=1,\qquad
 P_{N(L,R)}(u)=1+uP_L(u)P_R(u).                        \tag{3.2}
\]

Then

\[
                         d_{\mathcal H}(T)=[u^t]P_T(u). \tag{3.3}
\]

#### Proof

An operadic decomposition \(T=S(\mathbf A)\) determines the \(t\)
internal nodes belonging to \(S\); they are ancestor-closed.  Conversely,
an ancestor-closed \(t\)-set contracts to a \(t\)-node skeleton and its
ordered frontier is the unique tuple \(\mathbf A\).  Lemma 1.1 prevents
duplication.  This proves (3.1).

For (3.2), an ancestor-closed set is empty, or it contains the root and
independent ancestor-closed sets in the two children.  Taking
coefficients proves (3.3).  \(\square\)

The degrees are far from uniform.  If the top \(t\) internal nodes form a
unary chain leading to an arbitrary residual tree \(B\) of size \(s-t\),
then the size-\(t\) prefix is unique.  There are

\[
                              2^t C_{s-t}               \tag{3.4}
\]

such degree-one trees.  For \(t=o(s)\), their proportion is
\((1+o(1))2^{-t}\).  This tends to zero if \(t\to\infty\), so it is not by
itself a near-perfect-matching obstruction, but it rules out any literal
regularity assertion.

## 4. Exact codegrees and the failure of a small-codegree nibble

For \(K\in\mathcal I_t(T)\), write
\(\operatorname {Fr}(T,K)\) for its ordered frontier tuple.

### Proposition 4.1 (pair codegree)

For \(T,U\in\mathcal T_s\),

\[
 \boxed{
 \lambda_t(T,U)=
 \left|\left\{(K,L)\in\mathcal I_t(T)\times\mathcal I_t(U):
   \operatorname {Fr}(T,K)=\operatorname {Fr}(U,L)\right\}\right|.}
                                                               \tag{4.1}
\]

Moreover the average pair codegree is exactly

\[
 {1\over\binom{C_s}{2}}\sum_{\{T,U\}}\lambda_t(T,U)
 =\overline d_{s,t}\frac{C_t-1}{C_s-1}.                \tag{4.2}
\]

#### Proof

A common hyperedge is exactly a common ordered frontier tuple.  By
Lemma 1.1, each occurrence of that tuple gives a unique skeleton prefix
on either tree.  This proves (4.1).  Double count triples consisting of
an edge and an unordered pair of its vertices to obtain

\[
 \sum_{\{T,U\}}\lambda_t(T,U)
 =|E(\mathcal H_{s,t})|\binom{C_t}{2}.
\]

Use (2.4) to obtain (4.2).  \(\square\)

The tiny average in (4.2) hides very large exceptional codegrees.  Let
\(B\) be any tree and put

\[
 T=N(N(\varnothing,B),\varnothing),\qquad
 U=N(\varnothing,N(B,\varnothing)).                    \tag{4.3}
\]

For \(t\ge2\), every \(t\)-node prefix of either tree must contain the two
displayed internal nodes and then choose a \((t-2)\)-node prefix of \(B\).
Both choices expose the same frontier

\[
                (\varnothing,\operatorname {Fr}(B,K),\varnothing).
\]

Consequently

\[
          d_{\mathcal H}(T)=d_{\mathcal H}(U)
          =\lambda_t(T,U)=[u^{t-2}]P_B(u).              \tag{4.4}
\]

If \(B\) contains a complete binary prefix of depth \(t-2\), then every
\((t-2)\)-node skeleton occurs and

\[
                         \lambda_t(T,U)=C_{t-2}.        \tag{4.5}
\]

Such a \(B\) exists whenever \(s-2\ge2^{t-2}-1\).  In the slowly growing
regime \(2^t=o(s)\),

\[
 {C_{t-2}\over\overline d_{s,t}}
                 =(1+o(1))\frac{2^{t-4}}{t}\longrightarrow\infty.
                                                               \tag{4.6}
\]

Thus a Pippenger--Spencer or width-two-moment argument whose hypothesis
is \(\max\lambda=o(\overline d)\) cannot be applied.  This is not itself
a Hall obstruction—the two vertices in (4.3) are twins and can be
covered together—but it proves that average degree alone is not a
packing theorem.

## 5. The common port-interface test

The hypergraph above is only a hypergraph of Dyck roots.  To suspend a
fixed \(\mathcal D_t\)-port path factor through one of its edges by the
stated shape-preserving operadic rule, without re-solving all path rows,
the local coordinate interface must be common to every skeleton shape.
The literal requirement is (0.6), where \(W\) is independent of \(S\),
\(\iota\) is injective, and the union is disjoint.

Under (0.6), Hamming distances between all inflated ports equal the
corresponding Hamming distances between their skeleton ports:

\[
 |\,\operatorname {port}(S(\mathbf A))
       \triangle\operatorname {port}(S'(\mathbf A))\,|
 =|\,\operatorname {port}(S)
       \triangle\operatorname {port}(S')\,|.            \tag{5.1}
\]

For a binary word \(v\), let \(\tau(v)\) be its number of cyclic
transitions.  The Hamming distance between \(v\) and its one-step cyclic
shift is \(\tau(v)\).

Consider the elementary rotation

\[
             N(N(A,B),C)\longleftrightarrow N(A,N(B,C)). \tag{5.2}
\]

Using (1.1), the two Dyck words differ only by comparing

\[
                         1\,w(A)\,0
              \qquad\hbox{with}\qquad
                         w(A)\,0\,1.                    \tag{5.3}
\]

These are cyclic shifts.  Therefore their Hamming distance is

\[
                              \tau(1w(A)0).             \tag{5.4}
\]

### Lemma 5.1 (mountain test)

If (0.6) holds, then

\[
 A_i\text{ is a mountain tree for }0\le i\le t-2,      \tag{5.5}
\]

and

\[
 N(A_i,A_{i+1})\text{ is a mountain tree for }
                         0\le i\le t-3.                 \tag{5.6}
\]

Consequently (0.7) holds.

#### Proof

Choose two \(t\)-node skeletons which agree outside a rotation (5.2).
First let the macro-subtree \(A\) in (5.2) be the single skeleton leaf
whose spectator is \(A_i\).  On the bare skeleton, \(w(A)\) is empty, so
the distance in (5.4) is \(\tau(10)=2\).  Equation (5.1) forces

\[
                         \tau(1w(A_i)0)=2.
\]

A Dyck word \(w\) makes \(1w0\) have exactly two cyclic transitions if
and only if \(w=1^a0^a\).  This proves (5.5).

Next take the macro-subtree \(A\) to be the one-node skeleton spanning
the consecutive leaves \(i,i+1\).  Its bare word is \(10\), so again
\(\tau(1\,10\,0)=2\).  After spectator substitution it becomes
\(N(A_i,A_{i+1})\), proving (5.6).

Finally

\[
             w(N(A_i,A_{i+1}))
                  =1w(A_i)0w(A_{i+1})
\]

is a mountain word only if \(A_{i+1}=\varnothing\) and \(A_i\) is a
mountain.  Taking \(i=0,\ldots,t-3\) gives
\(A_1=\cdots=A_{t-2}=\varnothing\), while (5.5) gives the stated
condition on \(A_0\).  \(\square\)

The last two spectators are not constrained by this necessary test.
No sufficiency is claimed: some tuples counted by (0.7) may still fail
the complete port or path interface.

## 6. Quantitative loss of all common-interface skeleton packets

There is exactly one mountain tree of each size, so its generating
function is

\[
                              M(z)=\frac1{1-z}.          \tag{6.1}
\]

Lemma 5.1 shows that the number of tuples which can pass the common port
test is at most

\[
 [z^{s-t}]M(z)C(z)^2
   =[z^{s-t}]\frac{C(z)^2}{1-z}.                       \tag{6.2}
\]

Since \(C(z)^2=(C(z)-1)/z\),

\[
 [z^n]\frac{C(z)^2}{1-z}
 =\sum_{j=0}^{n}C_{j+1}
 =\left(\frac{16}{3}+o(1)\right)C_n.                  \tag{6.3}
\]

Even if all these candidate edges were mutually disjoint, they could
cover at most \(C_tB_{s-t}\) vertices.  For \(t\to\infty\) and
\(t=o(s)\),

\[
 \frac{C_tC_{s-t}}{C_s}
 =\left(\frac1{\sqrt\pi}+o(1)\right)t^{-3/2}.          \tag{6.4}
\]

Equations (6.2)--(6.4) prove (0.9).  Thus no matching chosen from
literal common-interface skeleton packets can cover more than
\(o(C_s)\) roots.  This is stronger than failure of a particular nibble:
there are too few usable incidences before matching begins.

### Theorem 6.1 (packing bound for the physically liftable subhypergraph)

Let \(\mathcal H^{\rm op}_{s,t}\) be the subhypergraph consisting of
edges which admit the shape-respecting interface (0.6).  Then

\[
 \nu(\mathcal H^{\rm op}_{s,t})\le B_{s-t},\qquad
 C_t\nu(\mathcal H^{\rm op}_{s,t})
 \le\left(\frac{16}{3\sqrt\pi}+o(1)\right)
             \frac{C_s}{t^{3/2}}.                     \tag{6.5}
\]

In particular every integral packing of physically liftable skeleton
packets leaves \(C_s-o(C_s)\) vertices uncovered.

#### Proof

Lemma 5.1 and (6.2) give at most \(B_{s-t}\) eligible edges in the entire
subhypergraph.  A matching uses at most all of them, and each chosen edge
has \(C_t\) vertices.  Equation (6.4) gives the displayed asymptotic.
\(\square\)

This is an integral statement.  It does not pass through a fractional
matching and has no rounding loss.

## 7. The heavy-spine canonicalization is not packet-stable

One might try to avoid the matching problem by assigning every tree its
first \(t\) heavy-spine nodes.  Even the most favourable one-giant
spectator regime does not make that rule constant on a skeleton edge.

For a tuple \(\mathbf A\), suppose \(A_j=B\) satisfies

\[
                   |B|>t+\sum_{i\ne j}|A_i|.           \tag{7.1}
\]

Thus \(B\) is larger than the complete skeleton and all other spectators
together.  In every inflated tree \(S(\mathbf A)\), the child containing
\(B\) is the unique heavy child at each skeleton ancestor of \(B\).
Consequently the heavy spine reaches \(B\) after exactly

\[
                            \operatorname {depth}_S(j) \tag{7.2}
\]

skeleton nodes, where \(\operatorname {depth}_S(j)\) is the depth of the
\(j\)-th leaf in \(S\).

### Proposition 7.1 (heavy-spine depth obstruction)

For \(t\ge3\), the map taking the first \(t\) heavy-spine nodes is not
constant on any full edge \(E_{\mathbf A}\) satisfying (7.1).

#### Proof

As \(S\) ranges over \(\mathcal T_t\), the depth of a fixed leaf is not
constant.  For a boundary leaf it ranges from \(1\) to \(t\); for an
interior leaf there are again skeletons with two different depths.
Choose \(S,S'\) with

\[
                 \operatorname {depth}_S(j)
                 <\operatorname {depth}_{S'}(j).       \tag{7.3}
\]

By (7.1), both heavy spines follow the skeleton route to \(B\).  In
\(S(\mathbf A)\), the first \(t\) heavy nodes enter \(B\) after the
smaller number in (7.3) and therefore contain more internal nodes of
\(B\).  In \(S'(\mathbf A)\), they contain more skeleton ancestors and
fewer nodes of \(B\).  The resulting ancestor-closed \(t\)-sets and their
frontier tuples are different.  Thus the heavy-spine cut does not assign
the two vertices to the common edge \(E_{\mathbf A}\).  \(\square\)

Stopping at the first entrance into \(B\) does recover the same giant
spectator, but the number of selected skeleton nodes is then
\(\operatorname {depth}_S(j)\), which varies with \(S\).  It therefore
does not produce a \(C_t\)-row, fixed-\(t\) packet.  The obstruction is
not caused by ties or by small spectators; (7.1) removes both.

Accordingly the heavy-spine rule supplies neither an exact partition nor
a near-perfect matching of the \(C_t\)-uniform skeleton packets.  A more
elaborate marker could conceivably reindex whole port families, but it
would have to solve the new port-isomorphism problem explicitly.

## 8. Consequence for factors assembled from the \(\mathcal D_4\) seed

The explicit \(\mathcal D_4\) factor still has its exact root-prefix
suspension inside \(\mathcal D_t\).  It changes

\[
                         11C_{t-4}                     \tag{7.1}
\]

first-insertion targets, its support has size \(14C_{t-4}\), and its
coarse pair transfer is \(C_{t-4}\).  The \(H_4\)-orbit gives a literal
four-label menu on \(8C_{t-4}\) roots.  These proportions tend to
\(11/256\), \(7/128\), and \(1/32\), respectively.

Every use assembled from the known one-hole rooted context functor has the
same visibility restriction: right concatenation preserves the local
first edge, while left concatenation and \(J\)-wrapping hide it.  Interior
copies therefore do not turn the bounded seed into a root-scale
boundary router.

More importantly, even a hypothetical noncanonical \(\mathcal D_t\)
factor cannot be transported through enough growing-skeleton edges by the
literal shape-respecting interface: Section 6 leaves only \(o(C_s)\)
roots.  To use the other edges one must either find a non-obvious
coordinate isomorphism which reindexes the complete Catalan port family,
or construct row-dependent paths whose spectator coordinates move
collectively.  In either case the complete \(X/Y\) ledgers must be
reproved at scale \(s\).  That object is a genuinely growing
\(\mathcal D_s\) path factor, not a suspension supplied by the bounded
seed.

The remaining viable statement is therefore explicit:

> Construct growing \(\mathcal D_s\)-port factors directly, with
> root-scale first-insertion diversity and complete \(X/Y\) ownership.
> A Catalan root hypergraph and a bounded local factor do not compose
> functorially into such an object.
