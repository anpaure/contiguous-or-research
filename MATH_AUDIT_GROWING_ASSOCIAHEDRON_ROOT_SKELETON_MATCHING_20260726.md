# Growing associahedron fibres: enumeration, codegrees, and a fractional matching obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Let \(\mathcal D_s\) be the Catalan family of ordered binary trees with
\(s\) internal nodes.  For \(1\le t\le s\), define
\(\mathcal H_{s,t}\) on vertex set \(\mathcal D_s\) as follows.  An edge is
indexed by an ordered forest

\[
                    \mathbf A=(A_0,\ldots,A_t),
       \qquad \sum_{i=0}^t |A_i|=s-t,                         \tag{0.1}
\]

and is

\[
                    e_{\mathbf A}
                       =\{P[\mathbf A]:P\in\mathcal D_t\}.      \tag{0.2}
\]

Every edge has size \(C_t\), and the number of edges is

\[
 E_{s,t}=[z^{s-t}]C(z)^{t+1}
   =\frac{t+1}{2s-t+1}\binom{2s-t+1}{s-t}.                    \tag{0.3}
\]

There is no fractional-to-integral near-perfect matching theorem under
the hypothesis \(t\to\infty\) alone.  The growing sequence \(t=s-1\)
already satisfies

\[
                  \nu(\mathcal H_{s,s-1})
                    =\nu^*(\mathcal H_{s,s-1})=2,              \tag{0.4}
\]

whereas every edge has \(C_{s-1}\) vertices.  Hence even a fractional
matching covers at most

\[
                    2C_{s-1}
                       =\left(\frac12+o(1)\right)C_s.           \tag{0.5}
\]

The obstruction is the interval geometry of cherries: the \(s\) edges
are indexed by the \(s\) adjacent leaf pairs; consecutive pairs give
disjoint edges and every two nonconsecutive pairs occur simultaneously
in a tree.

Standard high-degree nibble hypotheses also fail maximally in every
regime.  There are distinct vertices \(T,T'\) having identical incident
edge sets, and therefore

\[
             \lambda_t(T,T')=d_t(T)=d_t(T').                    \tag{0.6}
\]

Thus the maximum normalized pair codegree is one, even when the average
degree is exponentially large.

These statements do not rule out a theorem in a restricted mesoscopic
regime such as

\[
                       t\to\infty,\qquad s-t\to\infty,
                       \qquad t=o(s).                           \tag{0.7}
\]

They identify what such a theorem must add: it must contract the exact
equal-neighbourhood blocks and prove expansion or a matching theorem in
the resulting quotient.  Raw degrees, average codegrees, and a fractional
matching in an uncontracted auxiliary system do not by themselves provide
the desired rounding.

## 1. Exact incidence model

Write a tree as \(N(L,R)\), and regard the empty tree as a leaf.  An
operadic decomposition

\[
                             T=P[A_0,\ldots,A_t]                 \tag{1.1}
\]

is equivalent to choosing an ancestor-closed set \(I\) of exactly \(t\)
internal nodes of \(T\), containing the root.  The induced outer tree is
\(P\), while the \(t+1\) ordered components hanging from the frontier of
\(I\) are \(A_0,\ldots,A_t\).

### Lemma 1.1 (edge size)

For fixed \(\mathbf A\), the map

\[
                    P\longmapsto P[\mathbf A],
                    \qquad P\in\mathcal D_t,                    \tag{1.2}
\]

is injective.  Consequently every edge of \(\mathcal H_{s,t}\) has
exactly \(C_t\) vertices.

#### Proof

At the root, a skeleton whose left side has \(j+1\) input leaves contributes
exactly

\[
                              j+\sum_{i=0}^j|A_i|                \tag{1.3}
\]

internal nodes to the resulting left subtree.  This quantity is strictly
increasing in \(j\).  Hence the size of the resulting left subtree
recovers the root split of \(P\).  Applying the same argument recursively
to the two sides recovers all of \(P\).  \(\square\)

### Lemma 1.2 (number of edges)

Equation (0.3) holds.

#### Proof

The first equality is the ordered-forest census.  The standard Lagrange
coefficient formula

\[
                  [z^n]C(z)^k
                    =\frac{k}{2n+k}\binom{2n+k}{n}              \tag{1.4}
\]

with \(n=s-t\) and \(k=t+1\) gives the second equality. \(\square\)

For \(T\in\mathcal D_s\), let \(d_t(T)\) be its degree in
\(\mathcal H_{s,t}\).  Equivalently, \(d_t(T)\) is the number of
size-\(t\) ancestor ideals in \(T\).

Define

\[
                         D_T(u)=\sum_{j=0}^{s}d_j(T)u^j,
                         \qquad d_0(T)=1.                        \tag{1.5}
\]

Then

\[
                  D_{N(L,R)}(u)=1+uD_L(u)D_R(u).                \tag{1.6}
\]

Indeed, a nonempty ancestor ideal contains the root and independently
chooses an ancestor ideal, possibly empty, in each child.

Summing (1.5) over all trees gives the exact bivariate identity

\[
\begin{aligned}
 \sum_T z^{|T|}D_T(u)
   &=C(z)C\!\left(uzC(z)\right),\\
 \sum_{s\ge t}\left(\sum_{T\in\mathcal D_s}d_t(T)\right)z^s
   &=C_tz^tC(z)^{t+1}.                              \tag{1.7}
\end{aligned}
\]

In particular,

\[
                   \sum_{T\in\mathcal D_s}d_t(T)
                       =C_tE_{s,t},\qquad
                   \overline d_{s,t}
                       =\frac{C_tE_{s,t}}{C_s}
                       =\binom{2t}{t}\frac{(s)_t}{(2s)_t}.       \tag{1.8}
\]

Here \((x)_t=x(x-1)\cdots(x-t+1)\).  For each fixed skeleton shape a tree
has at most one decomposition, so

\[
                              1\le d_t(T)\le C_t.                 \tag{1.9}
\]

The degrees are highly nonuniform.  Every comb tree has

\[
                               D_T(u)=1+u+\cdots+u^s,             \tag{1.10}
\]

and hence \(d_t(T)=1\) for every \(t\le s\).  On the other hand the maximum
degree is at least the average in (1.8), which is exponentially large in
the principal growing regimes below.

More strongly, when \(s>t\), choose an oriented comb of \(t\) connector
nodes and put an arbitrary size-\((s-t)\) tree after its final continuation.
The size-\(t\) ancestor ideal is forced to be that comb.  These
constructions are distinct and give at least

\[
                              2^tC_{s-t}                          \tag{1.11}
\]

degree-one vertices.  For \(t=o(s)\), their fraction is
\((1+o(1))2^{-t}\), so this stratum vanishes when \(t\to\infty\) but
prevents literal regularity.

## 2. Uniform asymptotics

Put

\[
                              n=s-t,\qquad k=t+1.                 \tag{2.1}
\]

### 2.1 The one-big-jump and moderate-\(t\) range

From (1.4),

\[
 \frac{E_{s,t}}{C_n}
  =\frac{k(n+1)}{2n+k}
       \prod_{j=1}^{k}\frac{2n+j}{n+j}.                          \tag{2.2}
\]

If \(k=o(n^{2/3})\), expansion of the logarithm in (2.2) gives

\[
 E_{s,t}
   =k2^{k-1}C_n
       \exp\!\left\{
          -\frac{k(k+1)}{4n}
          +O\!\left(\frac{k}{n}+\frac{k^3}{n^2}\right)
            \right\}.                                           \tag{2.3}
\]

Thus, uniformly for \(t\to\infty\), \(t=o(s^{2/3})\),

\[
 \boxed{\;
 \overline d_{s,t}
   =\frac{2^t}{\sqrt{\pi t}}
      \exp\!\left\{
        -\frac{t^2}{4s}
        +O\!\left(\frac1t+\frac{t}{s}+\frac{t^3}{s^2}\right)
           \right\}. \;}                                        \tag{2.4}
\]

In particular, if \(t=o(\sqrt s)\), then

\[
                         \overline d_{s,t}
                           \sim\frac{2^t}{\sqrt{\pi t}}.          \tag{2.5}
\]

Formula (2.3) is the growing-\(k\) form of the Catalan one-big-jump
census.  In the sharper range \(t^2=o(s)\), one spectator contains
\(s-t-O_{\mathrm p}(t^2)\) nodes under the edge measure; the other
\(t\) spectators have their critical \(1/2\)-stable total scale \(t^2\).
This explains the factor \(2^t\) in (2.5), but supplies no disjointness
between different forest fibres.

### 2.2 Linear skeletons

Let \(t/s\to\rho\in(0,1)\).  Stirling's formula in (0.3) yields

\[
 E_{s,t}
  \sim
   \frac{\rho}
        {\sqrt{2\pi s(1-\rho)(2-\rho)}}\,
   \exp\!\{s\Psi(\rho)\},                                      \tag{2.6}
\]

where

\[
              \Psi(\rho)
                =(2-\rho)\log(2-\rho)
                   -(1-\rho)\log(1-\rho).                       \tag{2.7}
\]

Consequently

\[
 \boxed{\;
 \overline d_{s,t}
  \sim
   \frac{\exp\{s\Phi(\rho)\}}
        {\sqrt{2\pi\rho s(1-\rho)(2-\rho)}} ,\;}                 \tag{2.8}
\]

with

\[
 \Phi(\rho)
   =(2-\rho)\log(2-\rho)
       -(1-\rho)\log(1-\rho)
       -(1-\rho)\log4.                                         \tag{2.9}
\]

The rate \(\Phi\) is positive on \(0<\rho<1\); its derivative is

\[
                         \Phi'(\rho)
                           =\log\frac{4(1-\rho)}{2-\rho},         \tag{2.10}
\]

so its unique maximum occurs at \(\rho=2/3\).

### 2.3 The near-diagonal range

For \(t=s-r\), (0.3) becomes

\[
 E_{s,s-r}
   =\frac{s-r+1}{s+r+1}\binom{s+r+1}{r}.                         \tag{2.11}
\]

For fixed \(r\),

\[
             E_{s,s-r}\sim\frac{s^r}{r!},\qquad
             \overline d_{s,s-r}
                \sim\frac{s^r}{4^rr!}.                          \tag{2.12}
\]

Large average degree therefore persists right up to the diagonal.  The
matching obstruction in Section 4 shows why this statistic is misleading.

## 3. Exact pair-codegree audit

For distinct \(T,T'\in\mathcal D_s\), write

\[
                 \lambda_t(T,T')
                    =|\{e\in\mathcal H_{s,t}:T,T'\in e\}|.       \tag{3.1}
\]

If \(I\) is a size-\(t\) ancestor ideal of \(T\), let
\(\partial(T,I)\) denote its ordered frontier forest.  Lemma 1.1 gives
the exact arbitrary-pair formula

\[
 \lambda_t(T,T')
   =\left|\left\{(I,I'):
       \begin{array}{l}
        |I|=|I'|=t,\\
        \partial(T,I)=\partial(T',I')
       \end{array}\right\}\right|.                              \tag{3.2}
\]

No frontier forest can occur twice for the same tree, since that would
write the tree as \(P[\mathbf A]=P'[\mathbf A]\) with \(P\ne P'\),
contrary to Lemma 1.1.  Thus (3.2) counts edges without multiplicity and
immediately gives

\[
                 \lambda_t(T,T')\le
                    \min\{d_t(T),d_t(T')\}.                      \tag{3.3}
\]

The universal identities are

\[
\begin{aligned}
 \sum_{\{T,T'\}\subset\mathcal D_s}\lambda_t(T,T')
   &=E_{s,t}\binom{C_t}{2},\\
 \sum_{T'\ne T}\lambda_t(T,T')
   &=d_t(T)(C_t-1).                                             \tag{3.4}
\end{aligned}
\]

Hence the average codegree of an unordered vertex pair is

\[
 \overline\lambda_{s,t}
   =\frac{E_{s,t}\binom{C_t}{2}}{\binom{C_s}{2}}
   =\overline d_{s,t}\frac{C_t-1}{C_s-1}.                       \tag{3.5}
\]

When \(s-t\to\infty\), this average can be tiny.  It does not control the
maximum.

The complete second incidence moment also has an exact algebraic form.
Put

\[
 A(z,u)=\sum_Tz^{|T|}D_T(u)=C(z)C(uzC(z))
\]

and

\[
 B(z;u,v)=\sum_Tz^{|T|}D_T(u)D_T(v).
\]

Multiplying the two recursions (1.6) at \(u\) and \(v\) gives

\[
 B(z;u,v)
   =A(z,u)+A(z,v)-C(z)+uvzB(z;u,v)^2.                           \tag{3.6}
\]

Consequently

\[
\begin{aligned}
 [z^su^tv^t]B(z;u,v)
    &=\sum_{T\in\mathcal D_s}d_t(T)^2,\\
 \sum_{\substack{e,f\in\mathcal H_{s,t}\\e\ne f}}|e\cap f|
    &=\sum_{T\in\mathcal D_s}d_t(T)(d_t(T)-1).                  \tag{3.7}
\end{aligned}
\]

Thus the exact intersection moment needed by any weighted rounding can be
studied through one quadratic algebraic series.  The saturated pairs below
show why its first-moment normalization cannot imply a maximum-codegree
bound.

### Theorem 3.1 (saturated codegree and equal neighbourhoods)

For every \(2\le t\le s\), there are distinct \(T,T'\in\mathcal D_s\)
such that

\[
                  N_{\mathcal H}(T)=N_{\mathcal H}(T'),\qquad
                  \lambda_t(T,T')=d_t(T)=d_t(T').                \tag{3.8}
\]

#### Proof

Let \(B\in\mathcal D_{s-2}\), and use \(\epsilon\) for the empty tree.
Set

\[
          T=N\!\left(N(\epsilon,B),\epsilon\right),\qquad
          T'=N\!\left(\epsilon,N(B,\epsilon)\right).             \tag{3.9}
\]

These are the two bracketings of the ordered triple
\((\epsilon,B,\epsilon)\).  In both trees the two displayed connector
nodes are ancestors of every internal node of \(B\), and there are no
other internal nodes outside \(B\).

If \(t\ge2\), every size-\(t\) ancestor ideal consists of these two
connector nodes together with a size-\((t-2)\) ancestor ideal of \(B\).
The resulting frontier forest is, in both cases,

\[
        (\epsilon,\ \text{frontier forest of the ideal in }B,\
          \epsilon).                                            \tag{3.10}
\]

Thus the same forest edge contains \(T\) and \(T'\), and this construction
bijects all edges incident with either vertex.  In particular,

\[
                    d_t(T)=d_{t-2}(B)
                       =d_t(T')=\lambda_t(T,T').                 \tag{3.11}
\]

\(\square\)

Therefore

\[
                \max_{T\ne T'}
                   \frac{\lambda_t(T,T')}
                        {\min\{d_t(T),d_t(T')\}}=1.              \tag{3.12}
\]

These are not a negligible exceptional family.  As \(B\) ranges over
\(\mathcal D_{s-2}\), the pairs in (3.9) are mutually vertex-disjoint:
the root orientation distinguishes the two shores and \(B\) is recovered
from either tree.  They therefore occupy

\[
                         2C_{s-2}
                            =\left(\frac18+o(1)\right)C_s         \tag{3.13}
\]

vertices.  A near-perfect proof cannot discard all saturated pairs; it
must quotient or resolve them as blocks.

If \(\Delta_{a,b}=\max_{B\in\mathcal D_a}d_b(B)\), the same construction
also gives the absolute lower bound

\[
                    \Delta_2(\mathcal H_{s,t})
                       \ge\Delta_{s-2,t-2}.                      \tag{3.14}
\]

This becomes explicit when the common spectator is large enough to carry
a complete binary prefix of depth \(t-2\).  Every
\((t-2)\)-node skeleton then occurs as one of its ancestor ideals, while
the general upper bound in (1.9) gives equality:

\[
                    d_{t-2}(B)=C_{t-2}.                          \tag{3.15}
\]

Such a \(B\) exists whenever

\[
                         s-2\ge2^{t-2}-1.                        \tag{3.16}
\]

Extra nodes may be attached below a frontier leaf of the complete prefix.
Therefore

\[
 \boxed{\quad
       2^{t-2}\le s-1
       \quad\Longrightarrow\quad
       \Delta_2(\mathcal H_{s,t})\ge C_{t-2}.
       \quad}                                                    \tag{3.17}
\]

For \(t\to\infty\), \(2^t=o(s)\), this is exponentially larger than the
mean degree:

\[
            \frac{C_{t-2}}{\overline d_{s,t}}
                 \sim \frac{2^{t-4}}{t}.                         \tag{3.18}
\]

This is not merely a large-codegree estimate: the two vertices are
indivisible twins for every matching or fractional matching.  Similar
blocks arise by placing a common nonempty tree below several empty
connector leaves and varying their associahedral bracketing.

The twins themselves need not cause uncovered mass, because an edge covers
an entire twin block at once.  They do prove that no Pippenger--Spencer,
Rödl-nibble, or generic bounded-codegree rounding theorem applies before
these blocks and their higher analogues are contracted.

## 4. A sharp fractional obstruction at \(t=s-1\)

Here \(s-t=1\).  The ordered forest in (0.1) has exactly one one-node tree
and \(s-1\) empty trees.  Hence there are \(s\) edges

\[
                         e_0,e_1,\ldots,e_{s-1},                  \tag{4.1}
\]

where \(e_i\) is the set of trees having a cherry on consecutive inorder
leaf positions \(i,i+1\).  Contracting that cherry gives a bijection with
\(\mathcal D_{s-1}\), so

\[
                              |e_i|=C_{s-1}.                     \tag{4.2}
\]

Their intersections are exact:

\[
 |e_i\cap e_j|=
 \begin{cases}
  0,&|i-j|=1,\\
  C_{s-2},&|i-j|\ge2.
 \end{cases}                                                    \tag{4.3}
\]

For the second line, contract the two disjoint cherries; the inverse
expands the two prescribed nonoverlapping leaf positions.

### Theorem 4.1 (integral and fractional matching numbers)

For \(s\ge2\),

\[
                      \nu(\mathcal H_{s,s-1})
                        =\nu^*(\mathcal H_{s,s-1})=2.             \tag{4.4}
\]

#### Proof

By (4.3), two distinct edges are disjoint exactly when their indices are
consecutive.  No three indices are pairwise consecutive, while
\(e_i,e_{i+1}\) are disjoint.  Thus the integral matching number is two.

For the fractional statement, assign nonnegative weights \(x_i\) to the
edges.  The matching constraints are

\[
                         \sum_{i\in\operatorname{Ch}(T)}x_i\le1
                         \qquad(T\in\mathcal D_s),                \tag{4.5}
\]

where \(\operatorname{Ch}(T)\) is the set of cherry positions of \(T\).
All even positions are pairwise disjoint leaf pairs and can occur
simultaneously in one tree; construct it by first contracting those pairs,
choosing any binary tree on the contracted leaves, and then expanding the
pairs.  The same holds for all odd positions.  Applying (4.5) to these
two trees gives

\[
                       \sum_{i\ {\rm even}}x_i\le1,\qquad
                       \sum_{i\ {\rm odd}}x_i\le1.                \tag{4.6}
\]

Hence \(\sum_i x_i\le2\).  Conversely, assigning weight one to two
consecutive edges is feasible because those edges are disjoint.  Therefore
\(\nu^*=2\). \(\square\)

It follows exactly that the largest integral or fractional covered mass is

\[
                  2C_{s-1}
                    =\frac{s+1}{2s-1}C_s,                        \tag{4.7}
\]

and the uncovered fraction tends to \(1/2\).

Notice the discontinuity: at \(t=s\), there is one edge, namely all of
\(\mathcal D_s\), so a perfect matching is trivial.  At \(t=s-1\), even
the fractional optimum loses asymptotically half the vertices.  Thus
monotonicity in the skeleton size is unavailable.

## 5. Consequences for a growing-\(t\) rounding theorem

The sequence \(t=s-1\to\infty\) proves that neither the exact edge census
nor the condition \(t\to\infty\) implies a matching with \(o(C_s)\)
uncovered vertices.  The obstruction precedes integrality: the natural
fractional matching polytope itself has a constant deficit.

In a mesoscopic regime satisfying (0.7), Section 4 no longer applies
directly.  But Sections 1 and 3 leave two nonnegotiable requirements.

1. **Degree regularization.**  Degrees range from one to at least
   \(\overline d_{s,t}\), which is \(2^t/\sqrt{\pi t}\) when
   \(t=o(\sqrt s)\).  A proposed fractional point must control individual
   tree loads, not merely the average incidence (1.8).

   In the same range the edge rank is

   \[
                    C_t\sim\frac{4^t}{\sqrt\pi t^{3/2}},
       \qquad \frac{C_t}{\overline d_{s,t}}\sim\frac{2^t}{t}.     \tag{5.1}
   \]

   Thus the rank grows exponentially faster than the degree.  Fixed-rank
   nibble theorems are not uniform in the parameters present here; a
   projective-plane-type fractional/integral cut cannot be excluded by a
   small *average* pair codegree.

2. **Quotient codegrees.**  Before rounding, one must contract vertices
   with identical incident-edge sets, including the blocks in Theorem
   3.1.  On the quotient one must prove a genuinely new estimate such as

   \[
       \max_{\mathcal B\ne\mathcal B'}
          \lambda(\mathcal B,\mathcal B')
              =o\!\left(\min\{d(\mathcal B),d(\mathcal B')\}\right),
                                                                    \tag{5.2}
   \]

   together with the additional intersection-moment control required when
   the edge size \(C_t\) grows.  No such estimate follows from (3.5),
   whose smallness is compatible with the saturated pairs (3.8).

There is a useful exact conditional reduction.  Suppose a collection of
blocks \(\mathfrak B\) partitions all but \(\eta C_s\) vertices, every
edge is a union of blocks, and the quotient hypergraph admits a fractional
matching missing at most \(\eta C_s\) vertex mass together with a rounding
theorem losing \(o(C_s)\).  Lifting the quotient matching gives the desired
root-skeleton matching.  The equal-neighbourhood relation is the maximal
incidence-preserving contraction available without further choices, but it
is not yet known to make the quotient regular or low-codegree.

Accordingly, the exact remaining positive problem is:

> Prove, for a specified regime such as \(t\to\infty\),
> \(s-t\to\infty\), \(t=o(s)\), that the contracted associahedron-fibre
> hypergraph has a near-perfect fractional matching and sufficiently small
> weighted quotient codegrees for growing-rank rounding.

Without those additional hypotheses and that contraction, the desired
theorem is false by Theorem 4.1.
