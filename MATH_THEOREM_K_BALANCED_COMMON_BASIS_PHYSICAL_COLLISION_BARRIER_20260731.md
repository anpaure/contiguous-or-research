# Uniform common bases do not control the physical side forests

Date: 2026-07-31  
Lane: K, physical realization after the automatic two-coordinate common basis  
Status: rigorous negative theorem for marginal/random representative selection;
exact conflict-hypergraph and alteration bounds; no negative claim about a
structured all-dimension side-forest construction

## 0. Verdict

The uniform-marginal common-basis distribution closes the synchronized
incidence row, but its one-point information is insufficient for the physical
row.

For one punctured diagonal shore, put

\[
 M=\binom{2n}{n},\qquad
 N=\binom{2n}{n+1}=\binom{2n}{n-1}=n\operatorname {Cat}_n,
 \qquad
 P=\binom{2n}{n+2}.
\]

A saturating diagonal matching has (P) diamonds and lifts to a graph on
the (N) rank-((n+1)) physical vertices.  Its uniform atom density is

\[
             \theta={1\over\binom{n+2}{2}}
                    ={2\over(n+1)(n+2)}.                 \tag{0.1}
\]

There are three exact conclusions.

1. Coordinate-symmetrizing the standard BTK diagonal matching gives exact
   marginal (0.1) on every allowed diamond.  Every sample has at least

   \[
      \binom{2n-3}{n-4}
      =\left({(n-2)(n-3)\over4n(2n-1)}\right)N
      =(1/8-o(1))N.                                  \tag{0.2}
   \]

   degree-above-two vertices, and its overload satisfies the stronger

   \[
      \sum_W(d(W)-2)_+
      \ \ge\ \binom{2n-2}{n-4}
      =\left({(n-1)(n-2)(n-3)\over
                   2n(2n-1)(n+2)}\right)N
      =(1/4-o(1))N.                                  \tag{0.3}
   \]

2. More generally, any random saturating matching whose local cylinder
   probabilities through one physical vertex are product-like through order
   six has at least

   \[
                         (4/43-o(1))N                 \tag{0.4}
   \]

   degree-above-two vertices in expectation.  Thus an ordinary random or
   pseudorandom perfect-matching law is pointed in the wrong direction: the
   successful law must deliberately suppress all physical triples.

3. The anchor row is genuinely smaller.  Under a two-point joint
   decorrelation hypothesis, its expected excess is at most
   (2\Lambda\operatorname {Cat}_{n+1}).  The contracted seam graph has
   cycle rank at most (2\operatorname {Cat}_{n+1}) deterministically.
   Hence anchor repair and contracted-cycle repair are Catalan-scale, while
   unstructured side-degree repair is central-layer scale.

The independent-boundary absorber can therefore be the last local augmentor
only after a structured representative theorem has reduced side overload to
(O(N/n)=O(\operatorname {Cat}_n)).  It cannot turn a generic random
diagonal matching into a side forest.

## 1. The exact physical-triple conflict hypergraph

Fix a physical set (W\in\binom{[2n]}{n+1}).  Every allowed diagonal
diamond incident with (W) has the unique form

\[
       (D,U)=(W-\{a\},W\cup\{b\}),\qquad
       a\in W,\ b\notin W.                            \tag{1.1}
\]

Thus the local candidates form the cells of
(K_{n+1,n-1}).  In a saturating diagonal matching, selected local cells
have distinct rows and distinct columns: repeating a row repeats (D),
and repeating a column repeats (U).

### Lemma 1.1 (compatible local sets)

The number of compatible (k)-sets of candidate diamonds through (W) is

\[
                  A_k=k!\binom{n+1}{k}\binom{n-1}{k}. \tag{1.2}
\]

In particular, maximum physical degree at most two is equivalent to
avoiding the (A_3) compatible triples at every (W).

#### Proof

Choose (k) rows, (k) columns and a bijection between them.  Three
selected diamonds through (W) are outer-compatible exactly under this
condition, and their presence is exactly the assertion (d(W)\ge3).
\(\square\)

Call the resulting 3-uniform conflict hypergraph ({\cal T}_n); its
vertices are allowed diagonal diamonds and its hyperedges are compatible
triples through a common physical vertex.

### Lemma 1.2 (critical atom degree)

Every candidate diamond belongs to exactly

\[
              \Delta_{\cal T}
              =4\binom n2\binom{n-2}{2}              \tag{1.3}
\]

members of ({\cal T}_n).  Consequently

\[
                         \Delta_{\cal T}\theta^2\longrightarrow4. \tag{1.4}
\]

#### Proof

A diamond has two physical endpoints.  At either endpoint, after fixing
its row and column, choose two of the remaining (n) rows, two of the
remaining (n-2) columns, and one of the two bijections.  This gives
(2\binom n2\binom{n-2}{2}) triples at each endpoint.  A triple cannot be
counted at both endpoints, since three distinct Johnson edges cannot all
have the same two endpoints.  Equation (1.4) follows from (0.1).
\(\square\)

Thus the physical cap-two row is not a sparse afterthought at the uniform
fractional point.  Its conflict activity is at a nonzero critical constant.

There is a second useful calibration.  In an independent Bernoulli atom
model, triple events would depend only through shared atoms and the local
lemma would have ample slack; that model does not satisfy the outer
exact-one rows.  In the canonical random-injection dependency graph, two
specified matching events are adjacent when they conflict on a lower or
upper outer vertex.  A fixed lower outer vertex is incident with
\(\binom n2\) atoms and a fixed upper one with
\(\binom{n+2}{2}\) atoms.  Hence one triple event has

\[
  (3+o(1))n^6
\]

conflicting triple events, while its product-scale probability is
\((8+o(1))n^{-6}\).  Thus \(pD\to24\), so the naive symmetric local-lemma
argument has no slack.  This does not rule out an asymmetric or
structure-specific local lemma.

## 2. Why ordinary pair-collision energy cannot work

### Proposition 2.1 (pair-collision floor)

For every (P)-edge graph (G) on the (N) physical vertices, and every
(n\ge4),

\[
       \sum_W\binom{d_G(W)}2
       \ \ge\ 2P-N
       ={n(n-4)\over n+2}\operatorname {Cat}_n
       ={n-4\over n+2}N.                              \tag{2.1}
\]

This is compatible with (G) being a linear forest.

#### Proof

The total degree is (2P), and

\[
 {2P\over N}={2(n-1)\over n+2}\in[1,2).
\]

Among nonnegative integer degree sequences with this total, convexity of
(\binom d2) makes the minimum occur using only degrees one and two.  It
then equals (2P-N).  A path forest with few isolated vertices has exactly
this sort of degree profile, so the quantity is not a defect certificate.
\(\square\)

The first correct local defect is instead

\[
              \Omega_2(G)=\sum_W(d_G(W)-2)_+,         \tag{2.2}
\]

or, equivalently for zero testing, the compatible-triple family
({\cal T}_n).

## 3. Exact BTK side-matching obstruction

Use the standard left-to-right BTK bracketing on (B_{2n}).  Every chain
which reaches rank (n+2) contains a unique segment

\[
                  L\lessdot T\lessdot U,\qquad
       |L|=n,\quad |T|=n+1,\quad |U|=n+2.             \tag{3.1}
\]

Match (L) to (U), and let (H) be the opposite rank-((n+1)) corner
of the diamond.  These (P) flags saturate every rank-((n+2)) set and
use distinct rank-(n) sets.  Write

\[
                    q(W)=|\{L:H(L)=W\}|.              \tag{3.2}
\]

### Theorem 3.1 (off-central BTK fibre law)

For (0\le j\le n-1),

\[
     \left|\left\{W\in\binom{[2n]}{n+1}:q(W)=j\right\}\right|
        =\binom{2n-j-1}{n-j-1}.                       \tag{3.3}
\]

If (G_{\rm BTK}) is the lifted physical graph, then

\[
 d_{G_{\rm BTK}}(W)=\mathbf1_{W\text{ is an on-chain }T}+q(W), \tag{3.4}
\]

and hence (0.2)--(0.3) hold for every \(n\ge4\).  Moreover
\(G_{\rm BTK}\) is acyclic: oriented from \(T\) to \(H\), every edge
strictly increases the coordinate-sum potential.

#### Proof

For a binary word (W), put

\[
 S_t=\#\{0\text{s in the first }t\text{ positions}\}
     -\#\{1\text{s in the first }t\text{ positions}\}.
\]

Exactly as in the central BTK fibre bijection, the preimages in (3.2) are
in bijection with returns to the global minimum of (S_t) after its first
visit: changing the closing 1 of such a primitive minimum-level excursion
to 0 produces (L), whose first two free zeros are the opening and changed
closing positions.  Conversely the first two free zeros of any preimage
recover one such primitive excursion.

A rank-((n+1)) word has two more unmatched 1s than unmatched 0s.  If it
has (a) unmatched 0s, it has (a+2) unmatched 1s.  In the canonical
unmatched-symbol decomposition there are (2a+3) Dyck blocks.  The block
at the global minimum is required to have exactly (j) primitive factors;
the other (2a+2) blocks are arbitrary.  With (C(z)=1+zC(z)^2), the
generating function, counted by the number (n-1) of zeros, is

\[
 (zC(z))^j\sum_{a\ge0}z^aC(z)^{2a+2}
 ={z^jC(z)^{j+1}\over\sqrt{1-4z}}.                   \tag{3.5}
\]

Using

\[
 [z^s]\,{C(z)^b\over\sqrt{1-4z}}=\binom{2s+b}{s}
\]

gives (3.3).  Formula (3.4) is the literal on-chain/opposite-corner degree
decomposition.

If \(a<b\) are the next two free-zero positions of \(L\), then
\(T=L+a\), \(H=L+b\), and
\(\sum H-\sum T=b-a>0\).  The tails \(T\) are distinct, so this orientation
has outdegree at most one.  An undirected cycle in a graph with an
outdegree-at-most-one orientation would force exactly one outgoing cycle
edge at every cycle vertex and hence a directed cycle, contradicting the
strict potential.  Thus the obstruction below is purely branching, not a
hidden cycle defect.

Every \(W\) with \(q(W)\ge3\) has degree above two.  The first
hockey-stick identity gives

\[
 \sum_{j=3}^{n-1}\binom{2n-j-1}{n-j-1}
 =\binom{2n-3}{n-4}.
\]

Division by \(N=\binom{2n}{n-1}\) gives the factor in (0.2).

Moreover,

\[
 \Omega_2(G_{\rm BTK})
 \ge\sum_{j=3}^{n-1}(j-2)\binom{2n-j-1}{n-j-1}
 =\binom{2n-2}{n-4}.                                 \tag{3.7}
\]

For the last identity, write
\((j-2)_+=\sum_{t=3}^{j}1\), interchange the finite sums, and use the
same tail hockey-stick identity.  Division by \(N\) gives the factor in
(0.3).
\(\square\)

### Corollary 3.2 (uniform marginals retain the obstruction)

Apply a uniformly random coordinate permutation to (G_{\rm BTK}).  The
resulting distribution saturates every rank-((n+2)) outer set and has

\[
              \Pr((L,U)\text{ is selected})=\theta  \tag{3.6}
\]

for every allowed \(L\subset U\), while every sample retains the
bad-vertex bound (0.2) and overload bound (0.3).

#### Proof

The coordinate group is transitive on allowed incidences.  Each sample
contains (P) of the (P\binom{n+2}{2}) incidences, proving (3.6).
Overload is invariant under relabelling.  \(\square\)

This is a one-shore theorem.  It does not assert that this particular BTK
basis is the tail complement of a prescribed common bank (Q).  Its exact
scope is stronger than needed for the marginal warning: even exact outer
saturation together with uniform diagonal-atom marginals does not imply
any physical cap-two estimate.

## 4. Locally product random perfect matchings are physically bad

Let \({\bf M}\) be a probability distribution on saturating diagonal
matchings, with marginal \(\theta\) on every atom.  Say it is
((6,\varepsilon))-locally product if for every physical (W) and every
compatible (S) of (k=3,4,5,6) incident atoms,

\[
 (1-\varepsilon)\theta^k
 \le \Pr(S\subseteq{\bf M})
 \le (1+\varepsilon)\theta^k.                         \tag{4.1}
\]

This is a hypothesis, not a claim about the uniform perfect-matching law
of the Boolean incidence graph.

### Theorem 4.1 (six-local product barrier)

Under (4.1), the expected number of physical vertices of degree at least
three is at least

\[
 N\,{(1-\varepsilon)^2\mu_n^2\over(1+\varepsilon)B_n}, \tag{4.2}
\]

where

\[
 \mu_n=A_3\theta^3,
 \qquad
 B_n=A_3\theta^3+12A_4\theta^4
                 +30A_5\theta^5+20A_6\theta^6.       \tag{4.3}
\]

In particular, as \(n\to\infty\) and \(\varepsilon=o(1)\), (4.2) is

\[
                         (4/43-o(1))N.                \tag{4.4}
\]

#### Proof

For fixed (W), let (d=d_{\bf M}(W)) and (X=\binom d3).  Lemma 1.1
and (4.1) give

\[
                  \mathbb EX\ge(1-\varepsilon)A_3\theta^3.
\]

The exact polynomial identity

\[
 \binom d3^2=\binom d3+12\binom d4+30\binom d5+20\binom d6
\]

and the upper half of (4.1) give
(\mathbb EX^2\le(1+\varepsilon)B_n).  Paley--Zygmund at threshold zero
therefore proves (4.2), since (X>0) exactly when (d\ge3).  Summing over
all (W) is legitimate without independence between different vertices.

Finally

\[
                         A_k\theta^k\longrightarrow {2^k\over k!}.
\]

Thus (mu_n\to4/3) and

\[
 B_n\to {4\over3}+12{2\over3}+30{4\over15}+20{4\over45}
       ={172\over9}.
\]

The quotient is ((16/9)/(172/9)=4/43).  \(\square\)

So local pseudorandomness is not a sufficient physical hypothesis.  It is
a rigorous obstruction: a good representative distribution must have
strong negative three-way correlation at every physical star.

## 5. Exact alteration lower bound

### Proposition 5.1 (overload is 2-Lipschitz per replaced diamond)

Let (G,G') be two saturating diagonal matchings and let

\[
 s=|E(G)\setminus E(G')|=|E(G')\setminus E(G)|.
\]

Then

\[
                         \Omega_2(G)-\Omega_2(G')\le2s. \tag{5.1}
\]

Consequently any cap-two replacement of the BTK matching changes at least

\[
                         {1\over2}\binom{2n-2}{n-4}  \tag{5.2}
\]

diamonds.  A sequence consisting only of alternating C6 switches uses at
least

\[
                         {1\over6}\binom{2n-2}{n-4}  \tag{5.3}
\]

switches, counted with multiplicity.  More generally, the sum of the
half-lengths of all alternating circuits is at least half the initial
overload.

#### Proof

Deleting one physical edge lowers the degrees of two vertices by one, so
it lowers (Omega_2) by at most two.  Adding edges cannot lower
(Omega_2).  This proves (5.1).  Apply Theorem 3.1.  A C6 switch deletes
three old diamonds and therefore lowers overload by at most six.
\(\square\)

There is also a local invariance worth recording.  A 4-cycle switch inside
one star (W) merely changes
((a_1,b_1),(a_2,b_2)) to
((a_1,b_2),(a_2,b_1)).  All four diamonds remain incident with (W), so
the switch leaves (d(W)) unchanged.  Physical overload requires a
nonlocal C6 or longer circuit, and the BTK bound shows that a Catalan-size
packet of bounded circuits cannot repair an unstructured representative.

## 6. The genuinely Catalan-scale rows

Let (B) be the seam-anchor set on this shore and put

\[
             C=|B|=\operatorname {Cat}_{n+1},\qquad
             \alpha=C/N.
\]

There is first an exact additive diagnostic when a physical graph is
frozen before the balanced common basis.  It is **not** asserted that the
same graph is a legal diagonal representative for every sampled puncture.
In the child Catalan linear
matching the upper-colour map identifies its (N) atoms bijectively with
the (N) physical vertices of the minus side (and the lower-colour map does
the same on the plus side).

### Proposition 6.1 (fixed-geometry anchor average)

Let (G) be any fixed (P)-edge side graph, independent of the random common
basis, and let

\[
             A_B(G)=\sum_{W\in B}(d_G(W)-1)_+.
\]

Under the balanced common-basis distribution,

\[
 \mathbb E A_B(G)
   ={C\over N}\sum_W(d_G(W)-1)_+,                  \tag{6.1}
\]

and therefore, for (n>4),

\[
 C\,{n-4\over n+2}
 \ \le\ \mathbb E A_B(G)\ <\ 2C.                  \tag{6.2}
\]

Thus the additive anchor charge of every fixed graph is exactly
Catalan-scale.  The lower bound also shows that this scale cannot in
general be improved to (o(C)).

#### Proof

Each physical anchor has marginal (C/N), so linearity of expectation
gives (6.1).  Since

\[
 \sum_W(d_G(W)-1)_+
 \ge \sum_W(d_G(W)-1)=2P-N
   ={n-4\over n+2}N,
\]

the lower bound follows.  The upper bound follows from

\[
 \sum_W(d_G(W)-1)_+\le\sum_Wd_G(W)=2P<2N.
\]

\(\square\)

The proposition is only an averaging identity, not a simultaneous
incidence-feasibility theorem.  It also deliberately does not apply when
(G=G_Q) is selected after seeing (Q).  In that case put

\[
 \xi_W={\bf1}_{W\in B(Q)},\qquad
 f_W=(d_{G_Q}(W)-1)_+.
\]

Then one has the exact decomposition

\[
 \mathbb E\sum_W\xi_Wf_W
  ={C\over N}\sum_W\mathbb Ef_W
    +\sum_W\operatorname {Cov}(\xi_W,f_W).          \tag{6.3}
\]

The common-basis theorem controls the first moments of the variables
\(\xi_W\),
but places no sign or size restriction on the covariance term.  This is
the precise obstruction to applying Proposition 6.1 to an adaptively
chosen diagonal matching.

Assume the joint law of (B) and ({\bf M}) satisfies the two-point
decorrelation bound

\[
 \Pr(W\in B,\ S\subseteq{\bf M})
       \le\Lambda\alpha\theta^2                  \tag{6.4}
\]

for every physical (W) and every compatible pair (S) through (W).

### Proposition 6.2 (adaptive anchor excess under decorrelation)

Under (6.4),

\[
 \mathbb E\sum_{W\in B}(d(W)-1)_+
 \le \mathbb E\sum_{W\in B}\binom{d(W)}2
 \le 2\Lambda C.                                    \tag{6.5}
\]

#### Proof

The first inequality is pointwise.  Lemma 1.1 and (6.4) give an upper
bound

\[
 N\Lambda\alpha A_2\theta^2
 =\Lambda C\,{2n(n-1)(n-2)\over(n+1)(n+2)^2}
 \le2\Lambda C.
\]

\(\square\)

This hypothesis is automatic if the anchor bank is independent of a
uniform two-point representative law.  It is not supplied by the balanced
common-basis theorem, because the diagonal matchings depend on (Q).

Finally, after the two side graphs are forests, their contracted seam graph
(\Gamma_Q) has exactly (2C) seam edges.  Therefore

\[
                         \beta(\Gamma_Q)\le2C          \tag{6.6}
\]

without randomness.  Thus a palette-preserving augmentor which can reduce
one independent contracted cycle per use would need only Catalan-order
many uses.  Existence of such augmentors at every cycle is a separate
exchange theorem.

## 7. Consequence for the independent-boundary absorber

The independent-boundary absorber is a literal local (1\to2) augmentor,
but generic distance-(\Theta(n)) corridors have disjoint-support capacity
only

\[
                         O(N/n)=O(\operatorname {Cat}_n). \tag{7.1}
\]

Theorems 3.1 and 4.1 exhibit side matchings needing (Theta(N)) physical
degree alterations.  Proposition 5.1 makes the mismatch integral rather
than heuristic: a bounded-circuit or long-corridor bank of Catalan total
support cannot repair those states.

The weakest viable positive architecture is therefore:

1. choose the common basis and diagonal representatives in one correlated
   cap-two process, equivalently avoid the conflict hypergraph
   ({\cal T}_n) from the outset;
2. prove that only (O(N/n)) anchor, endpoint and topology defects remain;
3. use nonlocal alternating circuits to clear any residual side cycles;
4. use the independent-boundary absorber only for the final outer leave and
   contracted attachment defects.

Uniform marginals pay every bounded *additive* bank cost at Catalan scale,
but physical overload is a three-way interaction and cannot be replaced by
an additive collision heuristic.

## 8. Exact scope

This note proves no obstruction to a specially constructed Boolean side
forest.  The positive fixtures at (n=3,4) remain untouched.  It also does
not prove that the uniform distribution on all Boolean saturating matchings
satisfies the local-product hypothesis (4.1).

What is closed is the proposed inference

\[
 \text{uniform-marginal common basis}
 \quad\Longrightarrow\quad
 O(\operatorname {Cat}_n)\text{ random physical repair cost}.
\]

That inference is false even for an exact coordinate-symmetric saturating
matching distribution.  Any all-(n) proof must export a cap-two or
triple-suppression invariant as part of the representative choice itself.
