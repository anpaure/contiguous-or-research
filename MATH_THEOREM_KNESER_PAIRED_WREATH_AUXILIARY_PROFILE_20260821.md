# The paired-Kneser auxiliary hypergraph of punctured wreaths

## 1. Statement and scope

Put
\[
        b=2r+1,\qquad r\ge 2,
\]
and let \(G=KG(b,r)\).  Thus the vertices of \(G\) are the
\(r\)-subsets of \([b]\), and two vertices are adjacent when they are
disjoint.  Every edge \(e=\{X,Y\}\) of \(G\) has a unique *hole*
\[
        h(e)=[b]\setminus(X\cup Y).
\]

A wreath is an unoriented cyclic order
\(C=(c_0,c_1,\ldots,c_{b-1})\), considered modulo rotation and reversal,
with windows
\[
        W_i(C)=\{c_i,c_{i+1},\ldots,c_{i+r-1}\},
        \qquad i\in\mathbb Z_b.
\]
A *punctured wreath* is a pair \((C,W_s(C))\), where the indicated window
is called dirty.  After rotating indices so that the dirty window is
\(W_0\), associate to it
\[
 {\cal F}(C,W_0)
   =\bigl\{\{W_i,W_{i+r}\}:1\le i\le r\bigr\}.                 \tag{1.1}
\]
The members of (1.1) are pairwise vertex-disjoint edges of \(G\), and
their holes are exactly the elements of \(W_0\).

Let \({\cal J}_r\) be the \(r\)-uniform hypergraph whose vertices are the
edges of \(G\) and whose hyperedges are the sets (1.1).  Then:

**Theorem 1.1 (exact auxiliary profile).**

1. The map from punctured wreaths to \(E({\cal J}_r)\) is injective.
   In particular, \({\cal J}_r\) is simple and
   \[
        |E({\cal J}_r)|=\frac{b!}{2}.                         \tag{1.2}
   \]

2. \({\cal J}_r\) is regular of degree
   \[
        D_r=r(r!)^2.                                         \tag{1.3}
   \]

3. Suppose two vertices of \({\cal J}_r\) occur in one of its
   hyperedges at positions \(i<j\) in (1.1), and put \(d=j-i\).
   Their codegree depends only on \(d\) and is
   \[
     \lambda_{r,d}
       =(r-d)((r-d)!)^2(d-1)!d!,\qquad 1\le d\le r-1.         \tag{1.4}
   \]
   Pairs which do not have one of these compatible intersection types
   have codegree zero.  Consequently
   \[
        C_2({\cal J}_r)
          =\lambda_{r,1}
          =(r-1)((r-1)!)^2,
        \qquad
        \frac{C_2({\cal J}_r)}{D_r}
          =\frac{r-1}{r^3}.                                  \tag{1.5}
   \]

4. For every \(F\in E({\cal J}_r)\), the internal pair-codegree sum is
   the same number
   \[
     S_r:=\sum_{\{e,f\}\in\binom F2}\deg_{{\cal J}_r}(e,f)
       =\sum_{d=1}^{r-1}(r-d)^2((r-d)!)^2(d-1)!d!.            \tag{1.6}
   \]
   In particular,
   \[
        \frac{S_r}{D_r}
          =\frac1r-\frac{2}{r^2}+O(r^{-3}).                  \tag{1.7}
   \]

5. More generally, let \(2\le t\le r\), and suppose a compatible
   \(t\)-set of vertices occurs at positions
   \(i_1<\cdots<i_t\).  Put
   \(d_j=i_{j+1}-i_j\) and \(a=i_t-i_1=\sum_jd_j\).  Its
   codegree is
   \[
     (r-a)((r-a)!)^2
       \prod_{j=1}^{t-1}(d_j-1)!d_j!.                        \tag{1.8}
   \]
   Consequently the maximum \(t\)-codegree is
   \[
       C_t({\cal J}_r)
          =(r-t+1)((r-t+1)!)^2.                              \tag{1.9}
   \]

The gain in (1.5), especially
\(rC_2({\cal J}_r)/D_r=O(1/r)\), is specific to retaining
the Kneser pairing.  If the pairs are forgotten and a punctured wreath is
viewed merely as its \(2r\) clean target windows, disjoint target pairs
have codegree-to-degree ratio \(\Theta(1/r)\), not \(\Theta(1/r^2)\).

The theorem does **not** by itself produce a target-disjoint matching.
A matching in \({\cal J}_r\) can use two different Kneser edges which
share a target endpoint.  One must either restrict \(V({\cal J}_r)\) to
a Kneser matching \(P\), or impose those shared-endpoint pairs as a
conflict system.  This separation is essential.

## 2. The coordinate normal form

Normalize the dirty window to
\[
 D=(d_0,d_1,\ldots,d_{r-1})=(c_0,c_1,\ldots,c_{r-1})
\]
and write the complementary ordered block as
\[
 E=(e_0,e_1,\ldots,e_r)=(c_r,c_{r+1},\ldots,c_{2r}).
\]
For \(1\le i\le r\), put
\[
 \begin{split}
 A_i&=\{d_i,\ldots,d_{r-1}\}\cup\{e_0,\ldots,e_{i-1}\},\\
 B_i&=\{d_0,\ldots,d_{i-2}\}\cup\{e_i,\ldots,e_r\}.
 \end{split}                                                   \tag{2.1}
\]
Empty ranges are omitted.  Directly from the window definition,
\[
        \{W_i,W_{i+r}\}=\{A_i,B_i\},
        \qquad h(\{A_i,B_i\})=d_{i-1}.                       \tag{2.2}
\]
This proves that (1.1) consists of \(r\) vertex-disjoint Kneser edges
and that its hole set is \(D\).

## 3. Injectivity

Let only the unordered set \(F={\cal F}(C,W_0)\) be given.  The holes
of its Kneser edges first recover the dirty set \(D\).

For the edge with hole \(h\in D\), restrict its two endpoints to
\(D\setminus\{h\}\).  Equation (2.1) says that the resulting unordered
bipartition is precisely
\[
  \bigl\{\{d_0,\ldots,d_{i-2}\},
          \{d_i,\ldots,d_{r-1}\}\bigr\}
       \quad\text{when }h=d_{i-1}.                            \tag{3.1}
\]
Thus these restrictions give the betweenness relation of the linear
order on \(D\): an element \(h\) is strictly between \(x\) and \(z\)
exactly when \(x,z\) lie in different parts of (3.1).  The betweenness
relation of a finite linear order determines that order up to reversal
(its two endpoints are the elements which are never between two others,
and deleting either endpoint gives the same statement inductively).
Hence (3.1) recovers
\((d_0,\ldots,d_{r-1})\) up to reversal.

Choose one of those two directions.  It uniquely orients the edge with
hole \(d_{i-1}\): call \(A_i\) the endpoint containing the suffix
\(d_i,\ldots,d_{r-1}\).  The outside traces
\[
        A_i\setminus D=\{e_0,\ldots,e_{i-1}\},
        \qquad 1\le i\le r,                                  \tag{3.2}
\]
form a strictly nested chain.  Their consecutive differences recover
\(e_0,e_1,\ldots,e_{r-1}\), and the one remaining element is \(e_r\).
The other choice of direction reverses the full cyclic order, which is
the same wreath.  Therefore the punctured wreath is uniquely recovered
from \(F\), proving Theorem 1.1(1).

## 4. Degree

There are \((b-1)!/2\) unoriented cyclic orders and \(b\) choices of a
dirty window, giving \(b!/2\) punctured wreaths.  The odd graph has
\[
        |E(G)|=\frac{\binom br(r+1)}2                         \tag{4.1}
\]
Kneser edges.  Coordinate permutations act transitively on these edges,
and every hyperedge of \({\cal J}_r\) has size \(r\).  Double counting
incidences and using
\(\binom br=b!/(r!(r+1)!)\) gives
\[
 \deg_{{\cal J}_r}(e)
   =\frac{(b!/2)r}{\binom br(r+1)/2}
   =r(r!)^2,                                                   \tag{4.2}
\]
which is (1.3).

There is also a direct check useful below.  Fix a Kneser edge and place
it at position \(i\) of (2.2).  On each of its two endpoints, choosing
which elements occur before the cut and then ordering both sides gives
exactly \(r!\) possibilities.  Hence there are \((r!)^2\)
configurations at each of the \(r\) positions.

## 5. Exact pair codegrees

Take positions \(i<j\), and put \(d=j-i\).  With the endpoint
orientations of (2.1), their four intersections have the pattern
\[
 \begin{array}{c|cc}
      &A_j&B_j\\ \hline
 A_i  &r-d&d-1\\
 B_i  &d&r-d
 \end{array}.                                                  \tag{5.1}
\]
Together with the two distinct holes, this is the compatible type of
the pair and determines \(d\).

For a fixed \(i\), the two same-side intersections of size \(r-d\)
must be split at the outside/dirty cuts.  Choosing and ordering the two
parts contributes \((r-d)!\) on each side.  The two cross intervals
have respective sizes \(d-1\) and \(d\), contributing
\((d-1)!d!\).  Thus a fixed pair of positions contributes
\[
        ((r-d)!)^2(d-1)!d!                                   \tag{5.2}
\]
punctured wreaths.  There are \(r-d\) choices of \(i\), proving (1.4).

For completeness, (1.4) is largest at \(d=1\).  Indeed
\[
 \frac{\lambda_{r,d}}{\lambda_{r,1}}
  =\frac{r(r-d)}{(r-1)\binom{r-1}{d-1}\binom rd}\le1,         \tag{5.3}
\]
with equality only at \(d=1\).  This proves (1.5).

The same cut count proves the full profile.  For positions
\(i_1<\cdots<i_t\), each internal gap \(d_j\) contributes a dirty
interval of size \(d_j-1\) and an outside interval of size \(d_j\).
The two end regions have combined cut size \(r-a\), just as the two
same-side regions in the pair count, and the first position can be
translated in \(r-a\) ways.  This gives (1.8).  To maximize it, write
\(u=r-a\), so that \(u+d_1+\cdots+d_{t-1}=r\), with every variable at
least one.  The integer sequences
\[
        u\longmapsto u(u!)^2,
        \qquad d\longmapsto(d-1)!d!
\]
are log-convex.  Hence their product on this integer simplex is maximized
at a vertex: all excess above one lies either in \(u\) or in one gap.
Put \(v=r-t+1\).  Those two values are respectively
\(v(v!)^2\) and \((v-1)!v!\), and the former is \(v^2\) times the latter.
Thus all gaps equal one at the maximum, proving (1.9).

Inside a fixed hyperedge, exactly \(r-d\) unordered pairs of positions
have distance \(d\).  Summing (1.4) proves (1.6).  The \(d=1\) term,
after division by (1.3), is
\[
        \frac{(r-1)^2}{r^3}
        =\frac1r-\frac2{r^2}+\frac1{r^3}.                    \tag{5.4}
\]
Using (5.3), or just cancelling consecutive factorials in (1.6), the
sum of all \(d\ge2\) terms is \(O(r^{-3})D_r\).  This gives (1.7).

## 6. Exact identities for an invariant random Kneser matching

This section records what symmetry does, and does not, determine about
the proposed random-\(P\) compression.

Let \(P\) be any random maximum matching of \(G\) whose law is invariant
under coordinate permutations.  An iid-continuous-weight maximum
matching has this invariance, although it is not the uniform law on
maximum matchings.  Put
\[
 Q=|E(G)|,\qquad m=|P|=\left\lfloor\binom br/2\right\rfloor,
 \qquad q_1=\Pr(e\in P)=m/Q.                                  \tag{6.1}
\]
Here \(m=\lfloor\binom br/2\rfloor\): the odd graph is connected and
vertex-transitive, so the standard vertex-transitive matching theorem
gives a matching missing at most one vertex.
All punctured-wreath configurations are in one coordinate-permutation
orbit, so
\[
        q_r:=\Pr(F\subseteq P)                                \tag{6.2}
\]
is independent of \(F\in E({\cal J}_r)\).  If
\({\cal H}_P={\cal J}_r[P]\), then exactly
\[
 \begin{split}
  \mathbb E|E({\cal H}_P)|&=\frac{b!}{2}q_r,\\
  \mathbb E[\deg_{{\cal H}_P}(e)\mid e\in P]
     &=D_r\frac{q_r}{q_1}.                                   \tag{6.3}
 \end{split}
\]

For a compatible pair \(e,f\) of type \(d\), put
\(q_{2,d}=\Pr(e,f\in P)\).  The unconditional identity is
\[
 \mathbb E\!\left[
   {\bf1}_{\{e,f\in P\}}\deg_{{\cal H}_P}(e,f)\right]
   =\lambda_{r,d}q_r,                                        \tag{6.4}
\]
where the codegree is extended by zero off \(P\).  Thus, when
\(q_{2,d}>0\),
\[
 \mathbb E[\deg_{{\cal H}_P}(e,f)\mid e,f\in P]
    =\lambda_{r,d}\frac{q_r}{q_{2,d}}.                        \tag{6.5}
\]
Equations (6.3)--(6.5) are the exact expectation identities available
from invariance.

These are orbit statistics not evaluated by symmetry alone.  An invariant
law may mix orbit-uniform laws, and no formula for \(q_r\) or
\(q_r/q_{2,d}\) in terms of \(q_1\) follows without an additional theorem
showing the relevant orbit statistic is constant.  The iid-weight
optimizer weights orbits by their normal cones, not uniformly.
Consequently an asymptotic concentration theorem
for \({\cal H}_P\) requires a genuine random-matching switching or
correlation argument; it cannot be inferred just from (1.3)--(1.7).

## 7. Endpoint-conflict counts

Let \(X\) be a fixed target vertex of \(G\).  Double counting target
incidences gives the exact number
\[
 \Theta_r
   =\frac{(b!/2)(2r)}{\binom br}
   =r\,r!\,(r+1)!
   =(r+1)D_r                                                  \tag{7.1}
\]
of punctured configurations containing \(X\) as a clean window.

For distinct targets \(X,Y\), put \(s=|X\cap Y|\) and \(d=r-s\).
An oriented circle in which \(X=W_0\) and \(Y=W_d\) consists of four
ordered blocks of sizes \(d,s,d,s+1\).  Accounting also for the opposite
cyclic direction and then quotienting reversal shows that exactly
\[
        (d!)^2s!(s+1)!                                       \tag{7.2}
\]
wreaths contain both targets.  The dirty window can then be any of the
other \(b-2=2r-1\) windows, so their common configuration count is
\[
        (2r-1)(d!)^2s!(s+1)!.                                \tag{7.3}
\]
It is maximized at \(s=0\), where it is
\((2r-1)(r!)^2\), a \(\Theta(1/r)\) fraction of (7.1).

Declare two \({\cal J}_r\)-hyperedges to be in endpoint conflict if
some Kneser edge in the first and some Kneser edge in the second share
an \(r\)-set endpoint.  A fixed \({\cal J}_r\)-edge has \(2r\) clean
endpoints, so (7.1) gives the elementary conflict-degree bound
\[
        \Delta_{\rm conf}\le 2r\Theta_r
          =2r(r+1)D_r.                                       \tag{7.4}
\]
Equations (7.1)--(7.4) make clear why ordinary matching in
\({\cal J}_r\) is not enough and why simply forgetting the Kneser pairs
loses the extra factor of \(r\) in (1.5).

## 8. The remaining positive gate

For a fixed maximum Kneser matching \(P\), every hyperedge of
\({\cal H}_P\) automatically has disjoint target endpoints, and a
matching in \({\cal H}_P\) gives a family of target-disjoint wreaths with
one dirty window each.  A matching covering all but \(o(|P|)\) pair
vertices would therefore cover all but \(o(\binom br)\) central targets;
the one dirty window per chosen wreath costs only
\(O(\binom br/b)=o(\binom br)\).

The exact profile above removes the projective-plane-scale local
obstruction: \(rC_2/D_r=o(1)\), and the stronger internal overlap
identity is (1.6).  What remains unproved is that the iid-weight random
maximum matching makes \({\cal H}_P\) sufficiently near-regular (and
keeps its restricted codegrees sufficiently small) with high probability
for a growing-rank nibble, or an explicit deterministic choice of \(P\)
with those properties.  Upper-band alignment is a later and separate
problem.
