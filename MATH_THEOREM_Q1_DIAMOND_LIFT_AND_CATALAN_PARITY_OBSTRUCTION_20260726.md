# The depth-one diamond lift and the Catalan parity obstruction

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Let

\[
 {\cal L}=\binom{[n]}{m-1},\qquad
 {\cal M}=\binom{[n]}m,\qquad
 {\cal U}=\binom{[n]}{m+1}.
\]

A Johnson edge is equivalent to a rank-two Boolean interval
\((R,U)\), where \(R\in{\cal L}\), \(U\in{\cal U}\), and \(R\subset U\).
The two middle members of that interval are the endpoints of the edge.
This identifies the requested two-sided depth-one cycle with a matching in
the lower--upper interval graph whose middle lift is one cycle.

The reformulation gives a strict obstruction to the strongest exact
version.  On the even ground \(n=2m\), put

\[
 W=\binom{2m}m,\qquad
 N=\binom{2m}{m-1},\qquad
 D=W-N={W\over m+1}=\operatorname {Cat}_m.
\]

If a Johnson cycle of length \(N\) has all its intersections distinct and
all its unions distinct, then its coordinate-swap multigraph is
\(D\)-regular and has even degree at every vertex (equivalently, every
component has a balanced orientation).  Consequently \(D\) must be even.  Since
\(\operatorname {Cat}_m\) is odd exactly when \(m=2^a-1\), no exact
two-sided core, even as a disconnected two-factor, exists in those
dimensions.

This does **not** obstruct the asymptotic target.  If one lower colour and
one upper colour are omitted, the coordinate parity and first-moment
obstructions can be repaired; when \(D\) is odd, the two omitted colours
must be complementary.  This does not construct a compatible middle lift.
It shows that these obstructions cost only one additional owner.  Thus the
exact theorem is false infinitely often, while the requested cycle with
\(o(W)\) missing colours remains open.

On the odd ground \(n=2m+1\), an exact lower-saturating, upper-injective
core is not ruled out by parity, but its two leave families obey an exact
coordinate law derived below.  Gregor--Mička--Mütze Corollary 2 supplies
the lower projection and the middle cycle, but supplies neither the upper
matching nor these leave equations.

## 1. The flag graph and its middle lift

Let \(\Gamma_{n,m}\) be the bipartite graph with shores \({\cal L}\) and
\({\cal U}\), in which \(R\sim U\) when \(R\subset U\).  If

\[
                         U\setminus R=\{a,b\},
\]

define the middle lift of the flag \((R,U)\) to be

\[
 \lambda(R,U)=
 \big\{R\cup\{a\},R\cup\{b\}\big\}.                 \tag{1.1}
\]

This is an edge of \(J(n,m)\), with intersection \(R\) and union \(U\).
Conversely, every Johnson edge gives exactly one such flag.  For
\(F\subseteq E(\Gamma_{n,m})\), let \(\Lambda(F)\) be the graph on
\({\cal M}\) with edge set \(\{\lambda(R,U):(R,U)\in F\}\).

### Theorem 1.1 (exact incidence equivalence)

A simple Johnson cycle \(P\) has pairwise distinct intersection colours
and pairwise distinct union colours if and only if its flag set \(F(P)\)
is a matching of \(\Gamma_{n,m}\) and \(\Lambda(F(P))=P\).

More precisely:

1. the lower colours exhaust \({\cal L}\) exactly when the matching
   saturates \({\cal L}\);
2. the upper colours exhaust \({\cal U}\) exactly when it saturates
   \({\cal U}\);
3. a flag matching gives one Johnson cycle exactly when its lift is
   connected and has degree two on its support;
4. replacing “connected” by no condition gives the corresponding
   vertex-disjoint cycle factor.

#### Proof

The bijection (1.1) identifies the two projections of a flag with the
intersection and union colours of the Johnson edge.  Therefore distinctness
on the two colour shores is exactly the matching condition.  The remaining
claims are the definition of a cycle and a two-factor in the lifted graph.
\(\square\)

The graph \(\Gamma_{2m,m}\) is regular of degree
\(\binom{m+1}{2}\), so it has a perfect matching.  The matching condition
alone is therefore not the gate.  The gate is that its lift be 2-regular,
and preferably connected.

## 2. Two exact coordinate identities

For a family \({\cal A}\) of sets and a coordinate \(x\), write

\[
 d_{\cal A}(x)=|\{A\in{\cal A}:x\in A\}|.
\]

For a flag family \(F\), projections are counted with their flag
multiplicities and are denoted \(F_-\) and \(F_+\).  Let \(G(F)\) be the
multigraph on \([n]\) having the two-set \(U\setminus R\) as one edge for
each \((R,U)\in F\).

### Lemma 2.1 (endpoint and swap ledgers)

For every coordinate \(x\),

\[
 \sum_{X\ni x}d_{\Lambda(F)}(X)
       =d_{F_-}(x)+d_{F_+}(x),                       \tag{2.1}
\]

and

\[
 d_{G(F)}(x)=d_{F_+}(x)-d_{F_-}(x).                 \tag{2.2}
\]

If \(\Lambda(F)\) is a union of cycles, every degree in \(G(F)\) is
even.  More strongly, orienting each lifted cycle orients \(G(F)\) so that
the indegree and outdegree of every coordinate agree.  Thus \(G(F)\) is
componentwise Eulerian after isolated coordinate vertices are discarded;
no connectedness of \(G(F)\) is asserted.

#### Proof

For one flag \((R,U)\), the number of its two middle members containing
\(x\) is two, one, or zero according as \(x\in R\),
\(x\in U\setminus R\), or \(x\notin U\).  This is exactly
\({\bf1}_{x\in R}+{\bf1}_{x\in U}\), proving (2.1).  Also
\({\bf1}_{x\in U\setminus R}={\bf1}_{x\in U}-{\bf1}_{x\in R}\),
which proves (2.2).

Along an oriented Johnson cycle, a coordinate is inserted as often as it
is deleted.  Its total number of appearances among the swap pairs is
therefore twice either number and is even.  The assertion holds component
by component. \(\square\)

The Euler condition (2.2) is often the shortest obstruction.  Identity
(2.1) additionally determines the coordinate degrees of the owner leave.

## 3. Even ground: the Catalan obstruction

Assume \(n=2m\).  Suppose \(P\) has length \(N\) and both colour maps are
bijective.  Its flag set is then a perfect matching of
\(\Gamma_{2m,m}\).  Thus

\[
 d_{F_-}(x)=\binom{2m-1}{m-2},\qquad
 d_{F_+}(x)=\binom{2m-1}{m}.
\]

### Theorem 3.1 (Catalan parity obstruction)

For every coordinate \(x\),

\[
 d_{G(F)}(x)
 =\binom{2m-1}{m}-\binom{2m-1}{m-2}
 ={1\over m+1}\binom{2m}m
 =D.                                                   \tag{3.1}
\]

If the lift is a union of cycles on its support, then \(D\) is even.  If \({\cal E}\)
is the family of the \(D\) unused middle owners, then necessarily

\[
                         d_{\cal E}(x)=D/2             \tag{3.2}
\]

for every coordinate.

#### Proof

Equation (3.1) follows from (2.2) and the binomial identity

\[
 \binom{2m-1}{m}-\binom{2m-1}{m-2}
 ={2\over m+1}\binom{2m-1}{m-1}
 ={1\over m+1}\binom{2m}m.
\]

Lemma 2.1 makes this degree even.  For (3.2), apply (2.1).  The full middle
layer has coordinate degree \(\binom{2m-1}{m-1}\), which equals the full
upper coordinate degree.  If \({\cal A}={\cal M}\setminus{\cal E}\) is
the cycle support, then

\[
 2\left(\binom{2m-1}{m-1}-d_{\cal E}(x)\right)
 =\binom{2m-1}{m-2}+\binom{2m-1}{m}.
\]

Rearrangement and (3.1) give (3.2). \(\square\)

### Corollary 3.2 (infinitely many exact failures)

If \(m=2^a-1\), no exact two-sided rainbow core, even as a disconnected
two-factor on its support, exists.

#### Proof

Legendre's formula gives

\[
 v_2\binom{2m}m=s_2(m),
 \qquad
 v_2(\operatorname {Cat}_m)=s_2(m)-v_2(m+1),        \tag{3.3}
\]

where \(s_2(m)\) is the number of ones in the binary expansion of \(m\).
If \(t=v_2(m+1)\), then the binary expansion of \(m\) ends in exactly
\(t\) ones.  Hence \(s_2(m)\ge t\), with equality precisely when
\(m=2^t-1\).  The Catalan number is therefore odd precisely in those
dimensions, contradicting Theorem 3.1. \(\square\)

This is stronger than the obstruction to a complement-invariant cycle:
it excludes every exact two-sided cycle factor.

### Corollary 3.3 (the first upper collision cannot be solitary)

Assume \(m=2^a-1\ge3\).  Every lower-perfect Johnson cycle of length
\(N\) has upper collision excess either zero or at least two, and the zero
case is impossible by Corollary 3.2.  Hence its upper collision excess is
at least two.

#### Proof

Let \(u(U)\) be the upper-colour load.  There are \(N\) occurrences and
\(N\) upper targets.  Collision excess one would therefore mean that one
upper target \(U_0\) is missing, one target \(U_1\) has load two, and all
others have load one.  Reduce the coordinate swap degrees modulo two.
Relative to the all-upper baseline, whose difference from the all-lower
baseline is the odd constant \(D\), the two exceptional targets would have
to satisfy

\[
                         {\bf1}_{U_0}+{\bf1}_{U_1}
                         ={\bf1}_{[2m]}                 \tag{3.4}
\]

over \(\mathbb F_2^{[2m]}\).  Thus \(U_1=[2m]\setminus U_0\).  This is
impossible because both \(U_i\) have size \(m+1\), whereas the complement
of one has size \(m-1\). \(\square\)

The constant lower bound two is sharp only as a parity statement; no
claim of a matching cycle with exactly two collisions is made.

## 4. Exact deficiency law and why parity does not defeat \(o(W)\)

Still take \(n=2m\).  Suppose a Johnson cycle has injective lower and
upper colours and length \(N-t\).  Let \({\cal A}_-\subset{\cal L}\) and
\({\cal A}_+\subset{\cal U}\) be the omitted colour families; each has
size \(t\).  Let \({\cal E}\subset{\cal M}\) be the omitted owner family,
of size \(D+t\).

### Theorem 4.1 (coordinate deficiency identity)

For every coordinate \(x\),

\[
 \boxed{
 2d_{\cal E}(x)
   =D+d_{{\cal A}_-}(x)+d_{{\cal A}_+}(x).}          \tag{4.1}
\]

Equivalently, the swap degree is

\[
 d_{G(F)}(x)
   =D+d_{{\cal A}_-}(x)-d_{{\cal A}_+}(x),          \tag{4.2}
\]

and its required evenness is exactly the parity condition in (4.1).

#### Proof

Substitute the selected coordinate degrees

\[
 \binom{2m-1}{m-2}-d_{{\cal A}_-}(x),\qquad
 \binom{2m-1}{m}-d_{{\cal A}_+}(x)
\]

and the used-middle degree
\(\binom{2m-1}{m-1}-d_{\cal E}(x)\) into (2.1).  The constant difference
is (3.1), giving (4.1).  Equation (4.2) follows directly from (2.2).
\(\square\)

If \(D\) is odd, \(t=0\) is impossible.  For \(t=1\), write the omitted
colours as \(R\in{\cal L}\) and \(U\in{\cal U}\).  Equation (4.1) is
integral for every coordinate if and only if

\[
                         U=[2m]\setminus R,           \tag{4.3}
\]

and it then requires

\[
                         d_{\cal E}(x)=(D+1)/2        \tag{4.4}
\]

for all \(x\).  The numerical leave condition (4.4) is feasible: any even
number of middle sets can be chosen as a union of complementary pairs.
The incidence matching condition is feasible as well.  The graph
\(\Gamma_{2m,m}\) is connected and regular; after deleting any one vertex
from each shore, Hall's condition still holds, because every nonempty
proper lower family has at least one more neighbour than its size.

For completeness, connectivity follows by lifting every edge of the
connected graph \(J(2m,m-1)\): if \(R,R'\) differ by one exchange, their
union has size \(m\), and adjoining any further coordinate gives an upper
set adjacent to both.  In a connected \(d\)-regular bipartite graph, a
nonempty proper family \(A\) on one shore satisfies
\(|N(A)|\ge |A|+1\).  Indeed, equality \(|N(A)|=|A|\) would force all
\(d|A|\) incident edges to fill all degrees of \(N(A)\), making
\(A\cup N(A)\) a union of components.  Removing one upper vertex therefore
leaves at least \(|A|\) neighbours, which proves Hall after one vertex is
removed from each shore.

These observations do not construct the lifted cycle.  They show sharply
that the parity obstruction costs only one missing colour on each side and
one extra omitted owner.  Since \(D=O(W/m)\), this is fully compatible with
\(H|{\cal E}|=o(W)\) for \(H=o(m)\).

## 5. Odd ground: the exact coupled leave law

Now take \(n=2m+1\), and put

\[
 W=\binom{2m+1}m,\qquad
 N_-=\binom{2m+1}{m-1},\qquad
 D=W-N_-={2W\over m+2}.
\]

Suppose a cycle has length \(N_-\), exhausts the lower colours exactly,
and has distinct upper colours.  Let \({\cal E}_0\subset{\cal M}\) be its
owner leave and \({\cal E}_+\subset{\cal U}\) its upper-colour leave.
Both have size \(D\).  Define

\[
 \kappa
 =2\binom{2m}{m-1}-\binom{2m}{m-2}-\binom{2m}{m}
 ={D(m-1)\over2m+1}.                                  \tag{5.1}
\]

The first expression shows directly that \(\kappa\) is an integer.

### Theorem 5.1 (odd-ground leave coupling)

For every coordinate \(x\),

\[
 \boxed{
 d_{{\cal E}_+}(x)=2d_{{\cal E}_0}(x)-\kappa.}       \tag{5.2}
\]

In particular

\[
 d_{{\cal E}_+}(x)\equiv\kappa\pmod2,\qquad
 d_{{\cal E}_0}(x)\ge\lceil\kappa/2\rceil.          \tag{5.3}
\]

If \({\cal E}_+^c=\{[n]\setminus U:U\in{\cal E}_+\}\) is viewed as an
\(m\)-uniform family, then (5.2) is equivalently

\[
 2d_{{\cal E}_0}(x)+d_{{\cal E}_+^c}(x)=D+\kappa    \tag{5.4}
\]

for every \(x\).

#### Proof

In (2.1), the used-middle coordinate degree is
\(\binom{2m}{m-1}-d_{{\cal E}_0}(x)\), the selected lower degree is
\(\binom{2m}{m-2}\), and the selected upper degree is
\(\binom{2m}{m}-d_{{\cal E}_+}(x)\).  Rearrangement gives (5.2).
Equation (5.3) follows, and (5.4) follows from
\(d_{{\cal E}_+^c}(x)=D-d_{{\cal E}_+}(x)\). \(\square\)

The parity part of (5.3) is also exactly the Euler condition for the swap
multigraph.  Unlike the even-ground Catalan condition, it is not a
dimension-only contradiction; the upper leave is free to realize the
required parity profile.

For \(m\ge2\), there is a parallel full-owner formulation.  If a Hamilton Johnson cycle
uses every upper colour exactly once and has lower loads one or two, let
\({\cal Q}\subset{\cal L}\) be the family of the \(D\) lower colours used
twice.  Then (2.1) forces

\[
                         d_{\cal Q}(x)=\kappa         \tag{5.5}
\]

for every coordinate.  This first-moment condition is numerically
feasible: among all \(D\)-element subfamilies of \({\cal L}\), one
minimizing the sum of squared coordinate degrees has degrees differing by
at most one; since the average is
\(D(m-1)/(2m+1)=\kappa\), it is regular.  Indeed, if two degrees differed
by at least two, replacing a set containing the high-degree coordinate but
not the low-degree coordinate by the coordinate-swapped set would reduce
the square sum; such a replacement exists by comparing the two swapped
subfamilies.

Thus (5.5) is an exact necessary design law, not by itself an obstruction.

## 6. What Corollary 2 does and does not give

The saturating cycle between ranks \(m-1,m\) gives flags \(F\) such that

* the lower projection is a bijection;
* the middle lift \(\Lambda(F)\) is one cycle;
* the owner leave is \(D=O(W/m)\).

The missing assertion is precisely that the upper projection is injective,
or at least has collision excess \(o(W)\).  In flag language, Corollary 2
gives the difficult lift condition and one matching shore, but not the
other matching shore.  A perfect or saturating matching in
\(\Gamma_{n,m}\) exists abstractly by regularity/biregularity, but an
arbitrary such matching does not have a 2-regular middle lift.

For the projected lower sequence \((R_i)\), the unproved upper map is

\[
 U_i=R_{i-1}\cup R_i\cup R_{i+1}.                    \tag{6.1}
\]

Reversal preserves this multiset.  On even ground complementation produces
a second, generally different, upper-perfect cycle.  Neither operation
couples the two projections of one flag set.

## 7. Exact proved boundary

1. The preferred exact two-sided statement is false for every
   \(m=2^a-1\) on the even ground.
2. The obstruction is Euler parity of the literal coordinate exchanges,
   not merely failure of complement symmetry.
3. One missing colour per shore removes the parity obstruction, so this is
   not a quantitative obstruction to missing \(o(W)\) targets or to
   \(H E=o(W)\).
4. On odd ground the precise minimum remaining condition for the projected
   GMM core is an upper-injective (or \(o(W)\)-collision) choice satisfying
   the coupled leave law (5.2), with its middle lift remaining a single
   cycle.
5. Abstract lower--upper Hall matching and middle cycle grouping cannot be
   separated: each is easy or known alone, while their common flag set is
   the unresolved object.

## 8. Adversarial scope audit

The strongest negative claim, Corollary 3.2, uses all three hypotheses:
even ground, injectivity on both colour shores, and cyclic middle lift.
Dropping any one invalidates the conclusion.

* A path may have two unbalanced coordinate endpoints, so its swap graph
  need not be Eulerian.
* A full Hamilton owner cycle has more than \(N\) edges and may repeat
  \(D\) colours while still missing none.
* On odd ground the upper shore is larger, and its leave can absorb the
  parity vector as in (5.2).
* With one omitted colour on each even-ground shore, complementary
  omissions repair every coordinate parity as in (4.3).

Thus the Catalan obstruction cannot be promoted to a positive lower bound
of order \(W\), or even order \(W/m\), on missing colours.  Conversely,
the feasibility statements in Sections 4--5 concern only matching and
first coordinate moments.  They do not imply degree two of the middle
lift, connectivity, or literal higher-depth chronology.  No construction
of the requested asymptotic two-sided cycle is claimed.
