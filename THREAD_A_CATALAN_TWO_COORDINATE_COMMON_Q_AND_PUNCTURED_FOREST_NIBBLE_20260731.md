# Two-coordinate collar: automatic common \(Q\), punctured near-matchings, and the forest/absorber gates

Date: 2026-07-31  
Status: the existing exact common-\(Q\) theorem is independently rederived
for every \(n\ge3\); the physical slot hypergraph has uniformly small
codegrees and a sharp absorber-support lower bound.  The original argument
below proves \(P-o(P)\) side forests for random quasirandom `Q`.  The later
Delcourt--Postle audit
`MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`
strengthens this to **every** common-basis `Q`, without regularity: puncturing
only deletes atoms, the edge ledger remains `e/(DP)=1-o(1)`, and fixed-girth
conflict degrees are uniform.  Exact punctured-side completion remains open.

## 1. Verdict and notation

Use the two-coordinate recursion and inherited ports from
MATH_THEOREM_CATALAN_TWO_COORDINATE_PORT_INHERITANCE_AND_SIDE_FOREST_GATE_20260731.md.
Put

\[
 M=\binom{2n}{n},\quad N=\binom{2n}{n-1},\quad
 P=\binom{2n}{n-2},\quad K=\operatorname {Cat}_n,
\]
\[
 C=M-P=\operatorname {Cat}_{n+1},\qquad
 R=P-K=N-C.                                           \tag{1.1}
\]

Let \(F\) be any oriented parameter-\(n\) Catalan path forest.  The common
basis assertion below is also proved in
MATH_THEOREM_CATALAN_TWO_COORDINATE_COMMON_BASIS_AUTOMATIC_20260731.md;
Sections 2--4 give an independent contraction-matroid proof, including the
exceptional base \(n=3\).  The unconditional conclusions of this note are:

1. For every \(n\ge3\), there is \(Q\subseteq F\), \(|Q|=C\), such that

   \[
   D^-=\binom{[2n]}n\setminus t(Q),\qquad
   D^+=\binom{[2n]}n\setminus h(Q)                    \tag{1.2}
   \]

   simultaneously admit the required saturating matchings to ranks
   \(n+2\) and \(n-2\).
2. For every such \(Q\), the exact four-resource physical-slot hypergraph
   is \((1+o(1))2n^2\)-regular away from \(o(P)\) vertices and has maximum
   codegree \(O(n)\).  Its short physical-cycle conflicts cost only
   \(O(n\log n)=o(n^2)\) choices locally.
3. Exact cap-two and exact graphic-forest representatives exist separately.
4. Any two-terminal absorber for a far residual pair has support
   \(\Omega(n)\).
5. If \(Q\) is instead uniform among all \(C\)-subsets of \(F\), then with
   probability \(1-o(1)\) both shores have physical side forests of size
   \(P-o(P)\).

Items 1 and 5 have different quantifiers.  Their exact intersection is the
quasirandom-common-basis lemma isolated in Section 6.  Thus the common
diagonal-incidence gate and the unconditioned asymptotic physical gate are
separately closed, but their correlation and the zero-leave theorem remain.
No \(K17\) claim is made.

## 2. The two contraction matroids

Orient each component of \(F\) as a path.  Let \(E^-\) and \(E^+\) be its
unused-tail and unused-head banks.  Then

\[
 |E^-|=|E^+|=K.                                       \tag{2.1}
\]

For \(q=t_qh_q\in Q\), inherit the ports

\[
 p^-(U_q)=t_q,\qquad p^+(L_q)=h_q.                   \tag{2.2}
\]

These maps are legal and injective, and replacing \(q\) by its two seam
incidences preserves every central physical degree.

Let \(T_\uparrow\) be the rank-\(P\) transversal matroid on
\(\mathcal X=\binom{[2n]}n\) induced by matching into rank-\((n+2)\)
supersets.  Let \(T_\downarrow\) be its complement-dual lower version.
The duals of the two rank-\(C\) deletion matroids are

\[
 \mathcal A_F^*\cong (T_\uparrow/E^-)|_{t(F)},\qquad
 \mathcal B_F^*\cong (T_\downarrow/E^+)|_{h(F)}.      \tag{2.3}
\]

Hence \(Q\) is a common deletion basis exactly when

\[
 S=F\setminus Q,\qquad |S|=R,                         \tag{2.4}
\]

is a common basis of the two contractions in (2.3).

## 3. Uniform density of a two-step contraction

### Lemma 3.1 (the convex deficiency curve)

For \(b=\binom{x}{n}\), define

\[
 g(b)=\binom{x}{n-2},\qquad \Phi(b)=(b-g(b))_+.       \tag{3.1}
\]

For \(n\ge4\), \(g\) is concave, \(\Phi\) is convex and nondecreasing, and

\[
 \Phi(K)=0,\qquad \Phi(M)=M-P=C.                     \tag{3.2}
\]

#### Proof

Write \(s_j(x)=\sum_{i<j}(x-i)^{-1}\).  Differentiating generalized
binomial coefficients gives

\[
 {dg\over db}=
 {\binom{x}{n-2}s_{n-2}(x)\over\binom{x}{n}s_n(x)}.  \tag{3.3}
\]

Put \(u_i=(x-i)^{-1}\) and
\(\mu_j=\sum_{i<j}u_i^2/\sum_{i<j}u_i\).  The logarithmic derivative of
(3.3) is

\[
 -(u_{n-2}+u_{n-1})+\mu_n-\mu_{n-2}
 \le -u_{n-2}<0,                                     \tag{3.4}
\]

because \(\mu_n\le u_{n-1}\).  Thus \(g\) is concave and \(\Phi\) convex.
The zero crossing is \(x=2n-2\), or \(H=\binom{2n-2}{n}\).  The inequality
\(K\le H\) is equivalent to \(n^2-4n+1\ge0\), so \(\Phi(K)=0\) for
\(n\ge4\).  At \(b=M\), \(g(M)=P\).  Beyond the crossing, (3.3) is below
one and decreasing, proving monotonicity.  \(\square\)

### Lemma 3.2 (uniform-density contraction)

Let \(T\) be either two-step transversal matroid and let \(E\) be any
independent \(K\)-set.  For \(n\ge4\),

\[
 \boxed{r_{T/E}(A)\ge {R\over N}|A|}
 \qquad(A\subseteq\mathcal X\setminus E).             \tag{3.5}
\]

#### Proof

Lovász--Kruskal--Katona gives
\(|\mathcal N(\mathcal B)|\ge g(|\mathcal B|)\).  The transversal-rank
deficiency formula and monotonicity of \(\Phi\) therefore give

\[
 r_T(\mathcal A)
 =|\mathcal A|-\max_{\mathcal B\subseteq\mathcal A}
 (|\mathcal B|-|\mathcal N(\mathcal B)|)
 \ge|\mathcal A|-\Phi(|\mathcal A|).                 \tag{3.6}
\]

Convexity below the chord joining the two points in (3.2) gives

\[
 \Phi(K+|A|)\le {C\over M-K}|A|={C\over N}|A|.        \tag{3.7}
\]

Since \(E\) is independent,

\[
 r_{T/E}(A)=r_T(E\cup A)-K
 \ge |A|-\Phi(K+|A|)
 \ge {R\over N}|A|.
\]

\(\square\)

## 4. The common-\(Q\) theorem

### Theorem 4.1 (automatic common diagonal basis)

For every \(n\ge4\) and every oriented child forest \(F\), the two matroids
in (2.3) have a common basis \(S\) of size \(R\).  Hence \(Q=F\setminus S\)
simultaneously satisfies both diagonal incidence gates.

#### Proof

For every \(Z\subseteq F\), Lemma 3.2 gives

\[
 r_-(Z)+r_+(F\setminus Z)
 \ge {R\over N}|Z|+{R\over N}(N-|Z|)=R.              \tag{4.1}
\]

Edmonds' matroid-intersection theorem gives a common independent \(R\)-set,
which is a common basis.  Complementation in \(F\) gives \(Q\).  \(\square\)

The vector

\[
                         {R\over N}\mathbf1_F         \tag{4.2}
\]

lies in both base polytopes.  Integrality of the common-base polytope
expresses it as a convex combination of common bases.  Thus valid retained
bases have a distribution with exact marginals

\[
 \Pr(e\in S)=R/N,\qquad\Pr(e\in Q)=C/N.               \tag{4.3}
\]

No negative-dependence claim is made.

### Theorem 4.2 (the universal \(n=3\) base)

Theorem 4.1 also holds for every child forest at \(n=3\).

#### Proof

Here \((M,N,P,K,C,R)=(20,15,6,5,14,1)\).  Six triples on \([6]\) match
to the six rank-five targets exactly when their total intersection is
empty: a target is indexed by its omitted coordinate, and every proper
subfamily of at most five distinct triples satisfies Hall.

Five no-tail triples have common intersection of size at most one.  If it
is \(\{a\}\), exactly five of the fifteen used tails contain \(a\); if it
is empty, none is bad.  Thus the upper contraction has at most five loop
edges.  Dually, five no-head triples omit at most one common coordinate,
and the lower contraction has at most five loops.  At least five of the
fifteen child edges are nonloops in both contractions.  Any one is the
common retained rank-one basis.  \(\square\)

At \(n=2\), \(C=5>N=4\) and \(R=-1\), so the five-flow recursion is
scalar-impossible.

### Proposition 4.3 (one identical inherited bank is impossible)

For nonempty \(Q\subseteq F\), \(t(Q)\ne h(Q)\).

#### Proof

Equality would make the selected directed subgraph \(Q\) balanced at every
used vertex: positive indegree would be equivalent to positive outdegree.
Every nonempty component would be a directed cycle, contradicting that
\(F\) is a path forest.  \(\square\)

Thus a single explicit SCD bank cannot be used on both inherited shores.
The two bases supplied by Theorem 4.1 are generally different.

## 5. Exact capacity-slot hypergraph for one shore

Fix a common \(Q\) and put

\[
 \mathcal D=\binom{[2n]}n\setminus t(Q),\qquad
 \mathcal A=\{U_q:q\in Q\}.                           \tag{5.1}
\]

Give each rank-\((n+1)\) physical set \(x\) residual capacity

\[
 c(x)=1\ (x\in\mathcal A),\qquad c(x)=2\ (x\notin\mathcal A). \tag{5.2}
\]

Define a four-uniform hypergraph \(\mathcal H_Q\) with vertices:

* the \(P\) sets \(D\in\mathcal D\);
* all \(P\) rank-\((n+2)\) sets \(V\); and
* slots \((x,i)\), \(1\le i\le c(x)\).

For \(D\subset V\), write \(V\setminus D=\{a,b\}\),
\(x=D+a\), \(y=D+b\), and include

\[
                       \{D,V,(x,i),(y,j)\}            \tag{5.3}
\]

for all \(i\le c(x),j\le c(y)\).

### Proposition 5.1 (slot equivalence)

Hypergraph matchings are exactly the partial side-diamond families with
distinct lower and upper colours, physical degree at most two, and anchor
degree at most one.

#### Proof

The first two vertex classes enforce the outer injections and the slots
enforce the physical capacities.  Conversely assign the incidences at each
physical vertex injectively to its available slots.  \(\square\)

The counts are

\[
 |V(\mathcal H_Q)|=2P+2N-C,\qquad
 (2N-C)-2P=C-2K={2(n-1)\over n+2}K.                  \tag{5.4}
\]

### Proposition 5.2 (exact degree ledger)

For every \(Q\),

\[
 4P\binom n2-2C(n^2-1)
 \le |E(\mathcal H_Q)|
 \le4P\binom n2,                                     \tag{5.5}
\]
\[
 \Delta(\mathcal H_Q)\le2(n+1)(n+2),\qquad
 \Delta_2(\mathcal H_Q)\le2(n+1).                    \tag{5.6}
\]

#### Proof

Without anchor punctures, every \(D\) has \(\binom n2\) supersets and four
slot assignments for each.  One anchor lies on at most
\((n+1)(n-1)=n^2-1\) such diamonds and deletes at most two assignments on
each, proving (5.5).

A \(D\)-vertex has degree at most \(4\binom n2\), a \(V\)-vertex at most
\(4\binom{n+2}2\), and a slot at most \(2(n^2-1)\).  A pair \(D,V\) leaves
at most four choices, \(D,(x,i)\) at most \(2(n-1)\), \(V,(x,i)\) at most
\(2(n+1)\), and two slots at most one.  This proves (5.6).  \(\square\)

### Corollary 5.3 (deterministic almost regularity)

For every \(Q\), all but \(O(n^{-2/3}|V(\mathcal H_Q)|)\) vertices have
degree \(2n^2+O(n^{5/3})\).

#### Proof

The unpunctured class-degree offsets from \(2n^2\) are \(O(n)\) per vertex.
By (5.5), aggregate puncture loss is

\[
 O(Cn^2)=O(Pn),\qquad {C\over P}={4n+2\over n(n-1)}.
\]

Thus total positive degree deficit is \(O(|V(\mathcal H_Q)|n)\).
Every exceptional vertex contributes at least \(n^{5/3}\), so Markov gives
the claim.  \(\square\)

The plus shore is its complement-dual.

## 6. Uniform-\(Q\) forest theorem and the conditioning gap

Put

\[
 p_0={C\over N}={2(2n+1)\over n(n+2)}\le {5\over n},
 \qquad s_n={4n\over\log n}.                         \tag{6.1}
\]

Choose \(Q\) uniformly among all \(C\)-subsets of \(F\), without imposing
the common-basis condition.

### Lemma 6.1 (simultaneous local concentration)

With probability \(1-o(1)\), on both shores simultaneously, the following
five bounds hold for every possible local label:

\[
\begin{array}{c|c}
\text{count}&\text{upper bound}\\ \hline
\text{anchor supersets of a fixed }D&s_n\\
\text{removed }D\subset V&20n\\
\text{anchor facets of a fixed }V&s_n\\
\text{removed facets below a fixed }x&s_n\\
\text{anchor Johnson neighbours of a fixed }x&30n.
\end{array}                                           \tag{6.2}
\]

#### Proof

Tail/head injectivity and the two outer-colour bijections make each count
hypergeometric under the uniform sample.  Their numbers of eligible child
edges are at most

\[
 n,\quad\binom{n+2}{2},\quad n+2,\quad n+1,\quad n^2-1,         \tag{6.3}
\]

so their means are at most \(5,3n,6,6,5n\), respectively.  For a
hypergeometric variable of mean \(\mu\),

\[
 \Pr(X\ge t)\le(e\mu/t)^t.                           \tag{6.4}
\]

At \(t=s_n\), each bounded-mean row has failure probability
\(\exp(-(4-o(1))n)\).  The second row at \(20n\) is at most
\(e^{-17n}\), and the fifth at \(30n\) is at most \(e^{-23n}\).
There are only \(O(4^n)\) labels on both shores.  Since
\(4>\log4\), the union bound proves the claim.  \(\square\)

### Lemma 6.2 (all-vertex regularity)

On the event of Lemma 6.1, both slot hypergraphs obey, at every vertex,

\[
 d(v)=\bigl(1+O(1/\log n)\bigr)D_0,qquad
 D_0=2n^2,qquad \Delta_2\le2(n+1).                  \tag{6.5}
\]

#### Proof

A retained \(D\)-resource loses at most \(2s_n(n-1)\) from
\(4\binom n2\).  A \(V\)-resource loses at most

\[
                         4(20n)+2s_n(n+1)             \tag{6.6}
\]

from \(4\binom{n+2}2\).  An extant slot loses at most

\[
                         2s_n(n-1)+30n                \tag{6.7}
\]

from \(2(n^2-1)\).  These are \(O(n^2/\log n)\), while the unpunctured
class-degree offsets from \(2n^2\) are \(O(n)\).  The codegree assertion
is (5.6).  \(\square\)

### Theorem 6.3 (standard spread-nibble input)

This is the sole imported asymptotic matching theorem in this note.  We use
the standard *spread* form of the fixed-uniformity random nibble:
an all-vertex \((1+o(1))D\)-regular \(r\)-graph with
\(\Delta_2=o(D)\) has a random matching leaving \(o(v)\) vertices, and
for every pairwise disjoint edge set \(S\) of size at most \(D^{o(1)}\),

\[
                 \Pr(S\subseteq M)\le(L(D)/D)^{|S|},                 \tag{6.8}
\]

where \(L(D)=(\log D)^{O_r(1)}\).  The cylinder estimate follows directly
from the usual implementation: expose all activation coins in advance,
run \(O(\log\log D)\) rounds, and stop while the residual degree is
\(D/(\log D)^{O_r(1)}\).  A fixed original edge has total activation
probability at most \(L(D)/D\); selection implies activation, and the
activation coins of distinct edges are independent.

### Theorem 6.4 (unconditioned asymptotic punctured forests)

For uniform \(Q\), with probability \(1-o(1)\), both shores admit side
linear forests of size \(P-o(P)\), respecting both outer injections and
all physical/anchor capacities.

#### Proof

Apply the spread nibble with \(D=D_0\) to both hypergraphs on the event of
Lemma 6.1.  A physical rank-\((n+1)\) vertex has Johnson degree
\(\Delta_J=n^2-1\).  The number of physical simple \(\ell\)-cycles is at
most \(N\Delta_J^{\ell-1}\), and each has at most \(4^\ell\) slot lifts.
Incompatible lifts have probability zero; (6.8) gives

\[
 \mathbb E C_\ell
 \le N\Delta_J^{\ell-1}4^\ell(L(D_0)/D_0)^\ell
 \le {N\over D_0}(3L(D_0))^\ell                    \tag{6.9}
\]

for all sufficiently large \(n\) and \(\ell\ge3\).  Take
\(g=\lfloor(\log D_0)^{1/3}\rfloor\).  Then
\((3L(D_0))^g=D_0^{o(1)}\), so

\[
                  \mathbb E\sum_{3\le\ell\le g}C_\ell
                  \le ND_0^{-1+o(1)}=o(N).           \tag{6.10}
\]

By Markov, for some deterministic \(\varepsilon_n\downarrow0\), the number
of short cycles is at most \(\varepsilon_nP\) with probability \(1-o(1)\).
Intersect this with the standard high-probability \(o(P)\)-leave event and
choose one outcome.  The selected physical graph has maximum degree two, hence
its cycles longer than \(g\) are vertex-disjoint and number at most
\(P/g=o(P)\).  Delete one atom from every cycle.  Proposition 5.1 gives
the asserted side forests.  A union bound in Lemma 6.1 and two applications
of the nibble handle both shores.  \(\square\)

### Corollary 6.5 (pointwise quasirandom side forest)

Every fixed \(Q\) satisfying all five bounds (6.2) on both shores admits
side linear forests of size \(P-o(P)\) on both shores.

#### Proof

The proofs of Lemma 6.2 and Theorem 6.4 are pointwise after (6.2) is fixed.
\(\square\)

### Corollary 6.6 (unconditioned partial attachment forest)

For the \(Q\) in Theorem 6.4, adjoin \(F-Q\) and every inherited seam.
Keeping all seams, delete at most \(2C=o(P)\) further side atoms so that
the complete physical support is a linear forest.

#### Proof

Replacing each \(q\in Q\) by two seam leaves turns \(F\) into a path
forest.  Each side support is a forest and meets it only in its \(C\)
anchors.  The two unions raise cycle rank by at most \(2C\).  Every cycle
contains a side edge because the central-plus-seam graph was already a
forest, so a spanning-forest extension deletes at most \(2C\) side atoms.
Finally \(C/P=(4n+2)/(n(n-1))=O(1/n)\).  \(\square\)

### Former Hypothesis 6.7 (superseded for asymptotic side forests)

The hypothesis below was the bridge in the original spread-nibble proof.
It is not needed after the arbitrary-`Q` conflict-free coloring theorem,
which uses only Proposition 5.2's edge-count, maximum-degree and codegree
rows plus the short-cycle conflict bounds.  It is retained as a record of
the former route and may still be useful for stronger distributional
conclusions.

For every sufficiently large \(n\) and every child forest \(F\), the
common-basis family of Theorem 4.1 contains a member \(Q\) satisfying the
five bounds (6.2) on both shores.

Theorem 4.1 supplies common bases and even a distribution with exact
one-point marginals, but it supplies no negative dependence or local tail
bounds.  Theorem 6.4 supplies the physical forests for almost every
unconditioned \(Q\), but does not show that such a \(Q\) is a common basis.
Hypothesis 6.7, together with Corollary 6.5, is therefore a sufficient and
sharply localized bridge; it is not proved, and it is not asserted to be
necessary for an asymptotic
forest realization.

**Update (superseded as an asymptotic requirement).**  The arbitrary-`Q`
Delcourt--Postle theorem cited in the status paragraph proves `P-o(P)` side
forests directly for every common basis.  Hypothesis 6.7 remains a meaningful
quasirandomness statement, but is no longer needed for the asymptotic forest
bridge.  It still would not imply exact zero-leave completion.

### Proposition 6.8 (every uniform-\(Q\) Hall cut is mean-safe)

Assume \(n\ge4\) and fix one shore.  Let \(S=F\setminus Q\) be a uniform
\(R\)-subset, let
\(E\) be the \(K\) unused endpoints, and put \(D=E\cup t(S)\).  For
\(T\subseteq\binom{[2n]}{n+2}\), define

\[
 A_T=\{x:N(x)\subseteq T\},\qquad k_T=|A_T|,
 \qquad e_T=|E\cap A_T|.                             \tag{6.11}
\]

Then Hall is equivalent to

\[
                         |D\cap A_T|\le|T|\quad(T\subseteq Y),       \tag{6.12}
\]

and, writing \(r=R/N\),

\[
 |D\cap A_T|\ \mathrel{\overset{d}{=}}\
 e_T+\operatorname {Hypergeom}(N,k_T-e_T,R),          \tag{6.13}
\]
\[
                         \mathbb E|D\cap A_T|\le|T|.                 \tag{6.14}
\]

#### Proof

For \(B=Y\setminus T\), the vertices of \(D\) outside \(N(B)\) are
exactly \(D\cap A_T\).  Since \(|D|=|Y|=P\), the ordinary Hall inequality
\(|N(B)\cap D|\ge|B|\) is equivalent to (6.12).  Formula (6.13) is the
uniform sampling law on the \(N\) used endpoints.

If \(k_T<K\), the small-family shadow theorem gives
\(|T|\ge|N(A_T)|\ge k_T\ge|D\cap A_T|\).  If \(k_T\ge K\), the convex
deficiency curve gives

\[
 |T|\ge|N(A_T)|\ge k_T-\Phi(k_T)
 \ge rk_T+(1-r)K.                                   \tag{6.15}
\]

On the other hand, (6.13) has mean
\(rk_T+(1-r)e_T\le rk_T+(1-r)K\), proving (6.14).  The lower shore is the
complement-dual argument.  \(\square\)

Thus a uniform \(Q\) has no expected Hall overload on any cut.  This does
not bound the probability that *some* cut overloads.  Replacing \(T\) by
\(N(A_T)\) leaves \(A_T\) unchanged and can only strengthen (6.12), so it
would suffice to prove, over the distinct closed cuts \(T=N(A_T)\),

\[
 \sum_{T\ne Y}
 \Pr\!\left[\operatorname {Hypergeom}(N,k_T-e_T,R)
       \ge |T|-e_T+1\right]=o(1).                    \tag{6.16}
\]

Kruskal--Katona controls every threshold in (6.16), but it does not count
the near-tight closed cuts; a raw union over all subsets is therefore not
a proof.

### Corollary 6.9 (a sufficient bounded-cylinder theorem)

Hypothesis 6.7 follows if the common-basis family admits a probability
distribution satisfying

\[
             \Pr(A\subseteq Q)\le(C/N)^{|A|}
             \qquad(|A|\le30n).                      \tag{6.17}
\]

It is enough to require the corresponding factorial-moment inequalities
only for the five local families in (6.2).

#### Proof

The cylinder bounds dominate the factorial moments of each local count by
those of the matching binomial law.  The usual factorial-moment Chernoff
argument reproduces (6.4) through the largest threshold \(30n\); the union
bound of Lemma 6.1 then gives (6.2) with positive probability.  \(\square\)

The exact common-base distribution in (4.3) has the correct one-point
marginals but is not known to satisfy (6.17).

## 7. The two physical marginals are separately integral

### Proposition 7.1 (cap-two marginal)

One can choose two distinct rank-\((n+1)\) facets of every rank-\((n+2)\)
set while using each facet at most twice.

#### Proof

Put weight \(2/(n+2)\) on every edge of the bipartite facet-incidence
graph.  Every upper has load two and every facet load
\(2(n-1)/(n+2)<2\).  Bipartite \(b\)-matching integrality proves the claim.
\(\square\)

### Proposition 7.2 (graphic marginal)

One can choose two distinct facets of every rank-\((n+2)\) set so that the
selected incidence graph, and hence its suppressed physical graph, is a
forest.

#### Proof

Duplicate every upper block twice and apply Rado's theorem in the graphic
matroid.  Split a family \(A\) of upper blocks into connected incidence
components \(A_i\).  Normalized matching gives

\[
 |\partial A_i|\ge
 \left\lceil{n+2\over n-1}|A_i|\right\rceil
 \ge|A_i|+1.                                         \tag{7.1}
\]

Thus the graphic rank of all incidences from \(A\) is at least
\(\sum_i(|A_i|+|\partial A_i|-1)\ge2|A|\), exactly Rado's condition.
Suppressing each degree-two upper block preserves acyclicity.  \(\square\)

These marginals do not control the prescribed intersection bank, the other
physical row, and the anchor/attachment conditions simultaneously.  That
three-way correlation is the remaining gate.

## 8. Bounded local absorption is impossible for arbitrary residual pairs

### Theorem 8.1 (alternating-distance floor)

Let \(D\in\binom{[2n]}n\) and \(V\in\binom{[2n]}{n+2}\).  Suppose an
absorber has two states in which **every resource except \(D,V\) has the
same matched status**, while the off state leaves \(D,V\) unmatched and
the on state covers them.  If \(s=|D\setminus V|\), then its symmetric
difference has at least

\[
                    2\left\lceil{s\over2}\right\rceil+1             \tag{8.1}
\]

incidence edges.

#### Proof

Project both states onto the ordinary bipartite matching between their
rank-\(n\) and rank-\((n+2)\) outer resources.  The two-terminal hypothesis
makes the symmetric-difference component containing \(D\) an alternating
\(D\)-to-\(V\) path.  Every two-edge segment
\(D_i\subset W_i\supset D_{i+1}\) replaces at most two elements of a
rank-\(n\) set.  At least \(\lceil s/2\rceil\) such segments precede the
final edge into \(V\), giving (8.1).  \(\square\)

The maximum \(s=n-2\) is attained.  Therefore a universal absorber needs
\(\Omega(n)\) support, and a resource-disjoint bank handles only \(O(P/n)\)
arbitrary far pairs.  Exact completion requires at least one of:

1. an \(o(P/n)\) leave;
2. a Hall pairing of residual endpoints at \(o(n)\) distance;
3. shared/global long absorbers; or
4. a direct zero-leave forest-compatible realization.

This no-go is only for dimension-independent, resource-disjoint local
absorption of arbitrary residual pairs.

## 9. Small-\(n\) audit

\[
\begin{array}{c|rrrrrr|l}
n&M&N&P&K&C&R&\text{status}\\ \hline
2&6&4&1&2&5&-1&\text{scalar obstruction}\\
3&20&15&6&5&14&1&\text{common \(Q\) universal; one full side PASS}\\
4&70&56&28&14&42&14&\text{common \(Q\) universal; one full side PASS}\\
5&252&210&120&42&132&78&\text{common \(Q\); joint physical gate open}\\
6&924&792&495&132&429&363&\text{common \(Q\); joint physical gate open}
\end{array}                                           \tag{9.1}
\]

The exact \(n=3,4\) completions for the two displayed child forests and
chosen \(Q\)'s are replayed by

    scratch/audit_catalan_two_coordinate_integral_collar_n3_n4_20260731.py
    scratch/catalan_two_coordinate_integral_collar_n3_n4_20260731.audit.json

Their SHA256 values are respectively

    09cd9aa8dd68e8cb76e1870a6b8d7f7ea2a851891efd240159781e5f30380421
    d24deca22d1a0128506ba4794baf80a8e4b79ecf9a6bcfa700897a4fbb6b6ebb

and the canonical JSON payload hash is

    8fc4f6bf575669799168fa5b0b6a7cef7915084ae16963dc9a9eb1c24dc71db1

They do not prove universal physical completion over all child forests or
all common bases.  Indeed, the parameter-three capacity fixture in
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md
exhibits a common \(Q\) whose upper shore has an exact \(8>7\) slot cut.
No \(n=5,6\) full side-forest artifact is frozen.  The canonical BTK
product-aligned rank-zero result is not a counterexample: it fixes a
strictly smaller singleton-bank/deep-flag surgery class.

## 10. Exact remaining theorem

The incidence/Hall gate is closed for all \(n\ge3\).  The smallest unproved
statement is:

> For at least one common \(Q\) from Theorem 4.1, realize both diagonal
> matchings so that their physical supports satisfy the degree/anchor rows
> and, together with \(F-Q\) and the inherited seams, form a linear forest.

Unconditionally, Sections 5 and 7 prove that the physical hypergraph is
nearly regular in aggregate and that capacity and acyclicity are each
separately integral.  The later Delcourt--Postle theorem cited in the
addendum strengthens Section 6 pointwise: **every** admissible \(Q\), hence
every synchronized common basis, has a \(P-o(P)\) physical side forest.
Thus (6.16)--(6.17) are no longer missing bridges for asymptotic
physicalization.  They may still be useful if stronger spread or exact
cover-down control is required.  Theorem 8.1 shows why the remaining leave
cannot in general be cleaned by a dimension-independent,
resource-disjoint absorber for arbitrary residual pairs.  Exact equality
needs an edge-aligned or globally shared residual theorem, followed by the
downstream common-cap coupling—not another marginal Hall argument.

## 11. Adversarial audit and scope locks

The following stronger-looking statements were explicitly tested and are
**not** used.

1. Almost-regularity only on the two outer target classes does not imply a
   near-perfect four-partite matching: a complete example with a third
   part of size \(p/2\) is a bottleneck despite target codegree \(o(D)\).
2. The aggregate estimate of Corollary 5.3 does not supply the all-vertex
   tails needed by the spread nibble for an arbitrary common basis.  This
   is exactly why Theorem 6.4 samples \(Q\) without conditioning and why
   Hypothesis 6.7 remains.
3. The \(n=3,4\) PASS artifacts are existential fixtures, not universal
   child-forest theorems.  The separate \(n=3\) \(8>7\) capacity cut shows
   that an arbitrary common basis can fail physically.
4. The absorber floor uses the explicit two-terminal status hypothesis.
   It says nothing against shared multi-demand circuits, multi-state
   absorbers, or a global rethread.
5. Neither Theorem 6.4 nor any small-\(n\) artifact proves the exact
   punctured-side theorem, Catalan Linear Matching in all dimensions, or a
   statement about \(K17\).
