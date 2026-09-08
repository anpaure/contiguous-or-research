# Root-skeleton bracketing hypergraphs: exact census and recursive overlap

Date: 2026-07-26

Method: pure mathematics only.

## 0. Definition and verdict

Let \(\mathcal H_{s,t}\) have vertex set \(\mathcal D_s\). For every
ordered \((t+1)\)-tuple of binary trees

\[
                         (A_0,\ldots,A_t),
 \qquad \sum_i|A_i|=s-t,                               \tag{0.1}
\]

put one hyperedge consisting of the \(C_t\) bracketings of these fixed
inputs by all size-\(t\) binary skeletons. The desired D4 skeleton
hypergraph is \(\mathcal H_{s,4}\).

The exact audit gives:

* \(\mathcal H_{s,4}\) is 14-uniform, has average degree tending to
  \(35/8\), and maximum degree at most \(14\);
* growing \(t=o(\sqrt s)\) raises the average degree to
  \(2^t/\sqrt{\pi t}\), but it does not create low codegrees;
* a pair differing by one root associativity move can have codegree
  asymptotic to one quarter of the average degree;
* the proposed reduction through a minimal \(>s/2\) fringe core with
  bounded outside context is false: that outside context is linear-scale
  with high probability.

No recursive exact tiling, near-perfect matching theorem, or
positive-density unmatched obstruction is proved here. In particular the
fixed-\(t\) matching problem remains a genuine bounded-degree packing
problem, while the growing-\(t\) version has a hierarchical high-codegree
obstruction to a direct nibble.

## 1. Exact edge and degree counts

The number of ordered spectator forests in (0.1) is the Catalan
convolution

\[
\begin{aligned}
 E_{s,t}
  &=[z^{s-t}]C(z)^{t+1}\\
  &=\frac{t+1}{2s-t+1}
       \binom{2s-t+1}{s-t}.                            \tag{1.1}
\end{aligned}
\]

Every forest gives \(C_t\) distinct bracketings, so double counting
vertex-edge incidences gives

\[
 \boxed{
 \bar d_{s,t}
 =\frac{C_tE_{s,t}}{C_s}.}                            \tag{1.2}
\]

For fixed \(t\), or uniformly for \(t=o(\sqrt s)\),

\[
 \frac{E_{s,t}}{C_s}
 =\frac{t+1}{2^t}
    \exp\!\left(O\!\left(\frac{t^2}{s}\right)\right), \tag{1.3}
\]

and therefore

\[
\boxed{
 \bar d_{s,t}
 =\frac{\binom{2t}{t}}{2^t}
    \exp\!\left(O\!\left(\frac{t^2}{s}\right)\right)
 \sim\frac{2^t}{\sqrt{\pi t}}.}                       \tag{1.4}
\]

At \(t=4\), this is

\[
                         \bar d_{s,4}\longrightarrow
 \frac{\binom84}{16}=\frac{35}{8}.                    \tag{1.5}
\]

For a fixed skeleton shape \(S\in\mathcal D_t\), a tree \(T\) has at most
one expression \(S(A_0,\ldots,A_t)\), by unique parsing in the free binary
operad. Hence

\[
                         1\le d_{\mathcal H_{s,t}}(T)
                         \le C_t.                     \tag{1.6}
\]

The lower bound follows by taking any rooted ancestor-closed set of \(t\)
internal nodes and using its frontier subtrees as spectators.

For \(t=4\), (1.1) specializes to

\[
 E_{s,4}
 =\frac5{2s-3}\binom{2s-3}{s-4},                     \tag{1.7}
\]

recovering the \(35/8\) average.

## 2. Growing skeletons retain macroscopic codegrees

The high overlap is recursive, not accidental.

### Proposition 2.1 (root-rotation codegree)

Let \(U\in\mathcal D_{s-2}\), and form the two trees

\[
 T_L=((\bullet\,\bullet)\,U),\qquad
 T_R=(\bullet\,(\bullet\,U)),                         \tag{2.1}
\]

where \(\bullet\) denotes an empty spectator. Then

\[
 \deg_{\mathcal H_{s,t}}(T_L,T_R)
 \ge d_{\mathcal H_{s-2,t-2}}(U).                    \tag{2.2}
\]

Consequently

\[
 \Delta_2(\mathcal H_{s,t})
 \ge\bar d_{s-2,t-2}
 =\left(\frac14+o(1)\right)\bar d_{s,t}               \tag{2.3}
\]

whenever \(t\to\infty\) and \(t=o(\sqrt s)\).

#### Proof

Take any \((t-2)\)-skeleton representation of \(U\), with its ordered
\((t-1)\)-tuple of frontier spectators. Prepend the two empty spectators.
Using the outer skeleton \(((\bullet\bullet)S_U)\) gives \(T_L\), while
using \((\bullet(\bullet S_U))\) gives \(T_R\). They are two of the
\(C_t\) bracketings of the same \((t+1)\)-tuple, hence lie in one common
edge. Distinct representations of \(U\) give distinct spectator forests,
proving (2.2).

Choose \(U\) of degree at least the average and use (1.4). \(\square\)

Thus the usual small-codegree hypothesis does not emerge when the
skeleton grows. The problematic pairs are exactly those which share a
large spectator and differ only in a bounded outer associativity pattern.
Any matching proof must quotient or recurse through these clusters rather
than treat edges as pseudorandom.

The degree distribution is also strongly nonregular:

\[
 \frac{\max d}{\bar d}
 \le\frac{C_t}{\bar d}
 =\Theta\!\left(\frac{2^t}{t}\right),                 \tag{2.4}
\]

and comb-prefix trees give low-degree strata. This does not prove a
matching obstruction, but rules out a direct regular-design inference
from (1.4).

## 3. The minimal-giant truncation is reversed

Every tree \(T\in\mathcal D_s\) has a unique minimal fringe subtree
\(U\) with

\[
                              |U|>\frac s2.             \tag{3.1}
\]

Uniqueness holds because two such fringe subtrees are nested, and at most
one child of any node can have size \(>s/2\). Put

\[
                              c=s-|U|.                 \tag{3.2}
\]

The hope was that \(c\) is tight, allowing a finite induction over the
outside one-hole context. The exact count says the opposite.

There are

\[
                         (c+1)C_c=\binom{2c}{c}        \tag{3.3}
\]

binary one-hole contexts with \(c\) internal nodes. For \(U\) to be
minimal in (3.1), both of its children must have size at most
\(h=\lfloor s/2\rfloor\). Hence the number of choices for \(U\), when
\(|U|=s-c\), is

\[
 B_{s,c}
 =\sum_{\substack{i+j=s-c-1\\i,j\le h}}C_iC_j.        \tag{3.4}
\]

The decomposition \(T=C[U]\) is unique, so

\[
 \boxed{
 \#\{T:s-|U(T)|=c\}
 =\binom{2c}{c}B_{s,c}.}                              \tag{3.5}
\]

### Proposition 3.1 (no bounded outside core)

For every \(L=o(s)\),

\[
 \frac1{C_s}
 \#\{T:s-|U(T)|\le L\}
 =O\!\left(\left(\frac Ls\right)^{3/2}\right)
 =o(1).                                               \tag{3.6}
\]

#### Proof

For \(c\le L=o(s)\), the indices in (3.4) are both
\(s/2+O(L)\), and there are \(O(c+1)\) terms. Uniform Catalan estimates
give

\[
 B_{s,c}
 =O\!\left((c+1)\frac{4^{s-c}}{s^3}\right).           \tag{3.7}
\]

Together with
\(\binom{2c}{c}=O(4^c/\sqrt{c+1})\) and
\(C_s=\Theta(4^s/s^{3/2})\), the probability mass at \(c\) is
\(O(\sqrt{c+1}/s^{3/2})\). Summing through \(L\) proves (3.6).
\(\square\)

So a uniform Catalan tree reaches its minimal \(>s/2\) fringe only after
a linear-scale outside context. Restricting to \(c\le L=o(s)\) retains
only \(o(C_s)\) vertices rather than \(1-o(C_s)\). The proposed
finite-context induction cannot prove a near-perfect root-skeleton
matching.

## 4. Divisibility and component cautions

An exact perfect matching in \(\mathcal H_{s,t}\) requires

\[
                              C_t\mid C_s.             \tag{4.1}
\]

More strongly, every connected component used independently must have
cardinality divisible by \(C_t\). No classification of the components for
fixed \(t\ge4\) is currently proved. The global residue in (4.1) is less
than \(C_t\), and is therefore negligible when \(C_t=o(C_s)\); it cannot
by itself obstruct a near-perfect matching.

There is no free transitivity or regularity: the degree of a tree is the
number of rooted ancestor-closed \(t\)-node skeletons it contains, and
depends on its top shape. Fixed-\(t\) root-associativity moves can also
have nontrivial components (the \(t=2\) root-rotation graph already does),
so connectivity should not be assumed from the ordinary full rotation
graph.

At present there is neither:

* a component residue theorem forcing \(\Omega(C_s)\) unmatched vertices,
  nor
* a recursive selection which chooses one disjoint skeleton fibre for
  \(1-o(C_s)\) vertices.

The exact surviving problem is a hierarchical matching theorem which
handles the recursive codegree clusters in Proposition 2.1. A direct
nibble, a bounded-context giant-core induction, and scalar divisibility
do not settle it.

## 5. Exact marked-spectator quotient

The natural contraction of a high-codegree cluster can be written
exactly. Fix a tree \(U\) of size \(s-c\) and mark one occurrence of it
as a spectator. Contracting that occurrence identifies a tree \(T=C[U]\)
with a binary one-hole context \(C\) of size \(c\). Thus the marked
quotient has

\[
                         V_c^\bullet=(c+1)C_c
                         =\binom{2c}{c}                \tag{5.1}
\]

vertices.

Restrict to root-skeleton edges in which the marked \(U\) is one of the
\(t+1\) frontier spectators, rather than being entered by the skeleton.
For a fixed inorder slot, the other \(t\) spectators have total size
\(c-t\). Hence the number of marked quotient edges is

\[
\begin{aligned}
 E_{c,t}^\bullet
  &=(t+1)[z^{c-t}]C(z)^t\\
  &=(t+1)\frac{t}{2c-t}
       \binom{2c-t}{c-t}.                              \tag{5.2}
\end{aligned}
\]

Every such edge still has \(C_t\) bracketings, so its average marked
degree is

\[
 \boxed{
 \bar d_{c,t}^\bullet
 =\frac{C_tE_{c,t}^\bullet}{\binom{2c}{c}}.}           \tag{5.3}
\]

This quotient is not a smaller copy on all contexts: a context whose
marked hole lies below the first \(t\) ancestor-closed nodes has degree
zero in the preserving-\(U\) subhypergraph. To cover it, a skeleton edge
must enter \(U\), thereby leaving the contracted cluster. The same
phenomenon recursively produces Proposition 2.1's large pair codegrees.
Thus contraction does not yield independent quotient blocks; it gives a
hierarchy with boundary edges between every level.

For fixed \(t\) and \(c\to\infty\), (5.3) is

\[
 \bar d_{c,t}^\bullet
 =\left(1+o(1)\right)
   \frac{C_t\,t(t+1)}{2^{t+1}c},                      \tag{5.4}
\]

so only a vanishing fraction of deep marked contexts is even incident
with a preserving-\(U\) edge. This is the quotient form of the failure
of the bounded giant-context induction.

If the same unmarked tree contains several copies isomorphic to \(U\),
forgetting the mark identifies the corresponding quotient vertices and
adds their incidence multiplicities. Working in the marked cover avoids
that ambiguity but does not change the zero-degree deep-hole obstruction.

## 6. Literal multi-hole suspension has a general density no-go

Even a future abstract near-perfect matching in
\(\mathcal H_{s,t}\) would not automatically give wreath-factor packets.
The existing context theorem needs one row-independent physical injection
of the \(2t\) skeleton coordinates and one fixed exterior port set.

Write the full prefix word of a size-\(t\) skeleton, with \(t\) ones and
\(t+1\) zero slots. Across all \(C_t\) bracketings, only the last two zero
slots have fixed absolute positions, namely \(2t\) and \(2t+1\). Every
earlier slot moves: the left and right combs already put its zero in
different positions.

### Theorem 6.1 (common-port incidence ceiling)

Under the literal token-preserving common-port interface, all spectators
in slots \(1,\ldots,t-1\) must be empty. Consequently the total number of
vertices lying in admissible \(t\)-skeleton cylinders is at most

\[
                         C_t[z^{s-t}]C(z)^2
                         =C_tC_{s-t+1}.                \tag{6.1}
\]

For \(t=o(s)\),

\[
 \boxed{
 \frac{C_tC_{s-t+1}}{C_s}
 =\left(1+o(1)\right)\frac{4C_t}{4^t}
 \sim\frac4{\sqrt\pi\,t^{3/2}}.}                      \tag{6.2}
\]

In particular this is \(7/32+o(1)\) for \(t=4\), and tends to zero for
every growing \(t\).

#### Proof

A nonempty spectator contributes physical selected and unselected
coordinates at the location of its zero slot. A common cylinder requires
those physical coordinates to occupy one fixed exterior block in every
skeleton row. A moving slot violates that requirement; equivalently, the
root words lose the fixed selected/unselected columns required by a common
port. The left- and right-comb words show that slots
\(1,\ldots,t-1\) move, while the universal terminal \(00\) shows that
slots \(t,t+1\) are fixed.

The two surviving spectators have total size \(s-t\), giving
\([z^{s-t}]C^2=C_{s-t+1}\) ordered pairs. Each cylinder contains \(C_t\)
roots. This proves (6.1), even if all cylinders are disjoint. Catalan
asymptotics give (6.2). \(\square\)

For \(t=4\), a one-node spectator in slot two already gives a literal
port-ledger counterexample: the expanded fourteen roots have only one
all-selected and one all-unselected column, whereas a common cylinder
must have two of each. Thus Theorem 6.1 is an ownership obstruction, not
merely a positional convention.

### Corollary 6.2 (no-go for the current hierarchical successor)

No choice of \(t\to\infty\) makes root-skeleton packets both
asymptotically dense and suspendable by the existing common-port \(X/Y\)
functor. Generic edges needed by any near-perfect abstract matching use
moving early spectators, while the complete literal-suspension subfamily
covers only \(O(t^{-3/2})C_s=o(C_s)\) vertices.

A row-dependent multi-input trade remains logically possible, but its
global \(X/Y\) ledgers would have to be proved from scratch. It is not a
quotient or suspension of the finite D4 certificate.
