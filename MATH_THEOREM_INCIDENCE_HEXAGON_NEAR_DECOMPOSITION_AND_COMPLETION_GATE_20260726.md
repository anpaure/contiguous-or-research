# Incidence hexagons admit a near-decomposition, but fixed-exterior twists are metrically impossible

Date: 2026-07-26

Method: pure mathematics only.

## 0. Result

Put \(J=[2r]\), let

\[
 \mathcal L=\binom Jr\setminus\overline{\mathcal D_r},
 \qquad
 \mathcal Y=\binom J{r+1},
 \qquad
 N:=|\mathcal L|=|\mathcal Y|=rC_r.                    \tag{0.1}
\]

For an \((r-1)\)-set \(K\), call it ballot-eligible when every extension
\(K+a\), \(a\notin K\), belongs to \(\mathcal L\).  Section 3.6 of
MATH_THEOREM_TWISTED_PORT_MONODROMY_COMPOSITION_20260726.md proves that
the number of eligible cores is

\[
 Z_r=\frac{r(r-1)}{r+2}C_r.                            \tag{0.2}
\]

Define the six-uniform hypergraph \(\mathcal H_r\) on
\(\mathcal L\mathbin{\dot\cup}\mathcal Y\) by putting in, for every
eligible \(K\) and every three distinct \(a,b,c\notin K\), the edge

\[
 \{K+a,K+b,K+c;\ K+ab,K+bc,K+ca\}.                    \tag{0.3}
\]

Then \(\mathcal H_r\) has a matching which covers all but \(o(N)\)
vertices of each shore.  Equivalently it contains

\[
                    \left(\frac13-o(1)\right)rC_r      \tag{0.4}
\]

pairwise vertex-disjoint incidence hexagons.  In particular the geometric
hexagon supply touches \(\Omega(C_r)\) path-row candidates with an
enormous margin.

The proof is a genuine fixed-uniformity nibble.  All but \(O(N/\sqrt r)\)
vertices have degree

\[
                         \left(\frac12+o(1)\right)r^3, \tag{0.5}
\]

and every pair codegree is at most \(r(r-1)=o(r^3)\).

This geometric theorem does not give literal switches in one minimum
wreath factor.  There are two independent obstructions.

First, choosing one alternating half in every packed hexagon prescribes a
partial matching from \(\mathcal L\) to \(\mathcal Y\).  Such a partial
matching need not extend to a perfect outgoing incidence matching.  There
is already a one-hexagon counterexample: an upper vertex of incidence
degree one forces its unique lower neighbour, while a legal packed
hexagon can match that lower vertex elsewhere.

Second, even a successfully completed clean hexagon produces a
nonidentity three-cycle of path tails.  In an ordinary fixed-exterior
\(r\)-step slab this is forbidden by Johnson geodesicity.  If the row
starting at \(O\cup P\) is sent to
\(O\cup(J\setminus\tau(P))\), its endpoint distance is

\[
                              |P\cap\tau(P)|<r          \tag{0.6}
\]

for every moved port, while a contiguous \(r\)-step segment of a minimum
wreath must have distance \(r\).  Thus the packed hexagons are only
abstract incidence-ledger circuits unless a new exterior-moving packet is
constructed.

Thus the remaining exact object is an extendable, strand-compatible,
exterior-moving subhypergraph of \(\mathcal H_r\).  The ballot and nibble
calculation proves near-perfect geometric packing, but supplies no degree
lower bound inside that physical subhypergraph.

## 1. The ballot core ledger

For \(K\in\binom J{r-1}\), put

\[
 m_K=|\{a\notin K:K+a\in\overline{\mathcal D_r}\}|,
 \qquad
 d_K=r+1-m_K.                                          \tag{1.1}
\]

Thus \(K\) is eligible exactly when \(m_K=0\).  There are

\[
 \left|\binom J{r-1}\right|=rC_r=N                    \tag{1.2}
\]

cores.  Every barred port contains exactly \(r\) cores, so

\[
                         \sum_Km_K=rC_r=N.             \tag{1.3}
\]

Using (0.2), the number of bad cores is

\[
 N-Z_r=\frac{3r}{r+2}C_r.                              \tag{1.4}
\]

The total number of allowed lower extensions through bad cores is

\[
 \begin{aligned}
 \sum_{K:m_K>0}d_K
 &=r|\mathcal L|-Z_r(r+1)\\
 &=\frac{r(2r+1)}{r+2}C_r.                             \tag{1.5}
 \end{aligned}
\]

The first equality double counts pairs \(K\subset X\), \(X\in\mathcal L\).
Equations (1.4)--(1.5) are the concentration input below: bad cores are
rare, and their allowed incidences have average only \(O(1)\) per lower
vertex.

The number of hyperedges is exactly

\[
                  |\mathcal H_r|=Z_r\binom{r+1}{3}.    \tag{1.6}
\]

The core of a hexagon is the intersection of its three lower vertices, so
no edge is counted twice.

## 2. Exact vertex degrees

For \(X\in\mathcal L\), define

\[
 b(X)=|\{x\in X:X\setminus\{x\}\text{ is a bad core}\}|. \tag{2.1}
\]

Every eligible core \(K=X-x\) contributes
\(\binom r2\) choices of the other two labels.  Therefore

\[
 \boxed{
 d_{\mathcal H}(X)=(r-b(X))\binom r2.}                 \tag{2.2}
\]

Double counting allowed incidences through bad cores and using (1.5)
gives

\[
 {1\over|\mathcal L|}\sum_{X\in\mathcal L}b(X)
 =\frac{2r+1}{r+2}<2.                                  \tag{2.3}
\]

Consequently all but \(O(N/\sqrt r)\) lower vertices satisfy

\[
 b(X)\le\sqrt r,\qquad
 d_{\mathcal H}(X)
 =\left(1+O(r^{-1/2})\right)
       \frac{r^2(r-1)}2.                               \tag{2.4}
\]

For \(Y\in\mathcal Y\), define

\[
 b(Y)=|\{\{a,b\}\subset Y:Y\setminus\{a,b\}
                         \text{ is a bad core}\}|.      \tag{2.5}
\]

An eligible core \(K=Y-\{a,b\}\) contributes \(r-1\) choices of the
third label.  Hence

\[
 \boxed{
 d_{\mathcal H}(Y)=
 \left(\binom{r+1}{2}-b(Y)\right)(r-1).}               \tag{2.6}
\]

Every bad core lies in \(\binom{r+1}{2}\) upper vertices.  By (1.4),

\[
 {1\over|\mathcal Y|}\sum_{Y\in\mathcal Y}b(Y)
 =\frac{3r(r+1)}{2(r+2)}.                              \tag{2.7}
\]

Markov's inequality shows that all but \(O(N/\sqrt r)\) upper vertices
satisfy

\[
 b(Y)\le r^{3/2},\qquad
 d_{\mathcal H}(Y)
 =\left(1+O(r^{-1/2})\right)
       \binom{r+1}{2}(r-1).                            \tag{2.8}
\]

The two reference degrees in (2.4) and (2.8) differ by a factor
\(1+1/r\).  Thus, with \(D=r^3/2\), the maximum degree is
\((1+o(1))D\), and all but \(O(N/\sqrt r)\) of the \(2N\) vertices have
degree \((1+o(1))D\).

As a check, both shores have the same exact average degree

\[
 {3|\mathcal H_r|\over N}
 =\frac{r(r-1)^2(r+1)}{2(r+2)}
 =\left(\frac12+O(r^{-1})\right)r^3.                  \tag{2.9}
\]

## 3. Exact pair codegrees

The following list is exhaustive.

### Proposition 3.1

For distinct vertices of \(\mathcal H_r\):

1. If \(X,X'\in\mathcal L\), then

   \[
   \lambda(X,X')=
   \begin{cases}
   r-1,&|X\cap X'|=r-1
        \text{ and }X\cap X'\text{ is eligible},\\
   0,&\text{otherwise}.
   \end{cases}                                         \tag{3.1}
   \]

2. If \(Y,Y'\in\mathcal Y\), then \(\lambda(Y,Y')=0\) unless
   \(|Y\cap Y'|=r\).  In the latter case, writing \(R=Y\cap Y'\),

   \[
   \lambda(Y,Y')
    =|\{z\in R:R-z\text{ is eligible}\}|\le r.         \tag{3.2}
   \]

3. If \(X\in\mathcal L\), \(Y\in\mathcal Y\), and
   \(|X\cap Y|=r-1\), then \(\lambda(X,Y)\le1\).

4. If \(X\subset Y\), then

   \[
   \lambda(X,Y)
    =(r-1)|\{x\in X:X-x\text{ is eligible}\}|
    \le r(r-1).                                        \tag{3.3}
   \]

5. In every other lower--upper case, the codegree is zero.

#### Proof

Two lower vertices in one hexagon share its unique \((r-1)\)-core.
Once they are fixed, the third label has \(r-1\) choices, proving (3.1).

Two upper vertices in a hexagon share the core and one of its three new
labels, so their intersection has size \(r\).  For each possible common
new label \(z\in R\), the core is \(R-z\), and the third upper vertex is
then forced.  This proves (3.2).

If \(|X\cap Y|=r-1\) and \(X\not\subset Y\), their union determines the
three labels and their intersection determines the core, giving at most
one edge.

Finally suppose \(Y=X+b\).  Choose the label \(x\in X\) for which
\(K=X-x\).  If \(K\) is eligible, the third label can be any of the
\(r-1\) elements outside \(K\) other than \(x,b\).  Summing over \(x\)
gives (3.3).  The set geometry of (0.3) excludes all remaining cases.
\(\square\)

In particular

\[
                         \max_{u\ne v}\lambda(u,v)
                         \le r(r-1)=o(D).              \tag{3.4}
\]

## 4. The fixed-uniformity nibble

We use the following standard form, recorded with the hypotheses needed
here.

### Lemma 4.1 (almost-regular nibble)

Fix \(k\).  Let \(\mathcal G_n\) be \(k\)-uniform hypergraphs with
reference degrees \(D_n\to\infty\).  Suppose

\[
 \Delta(\mathcal G_n)\le(1+o(1))D_n,\qquad
 |\{v:d(v)<(1-o(1))D_n\}|=o(|V(\mathcal G_n)|),        \tag{4.1}
\]

and

\[
                         \Delta_2(\mathcal G_n)=o(D_n). \tag{4.2}
\]

Then \(\mathcal G_n\) has a matching which leaves \(o(|V|)\) vertices
uncovered.

#### Proof sketch

Run the semi-random nibble in rounds.  In a round, independently mark
each surviving edge with probability \(\eta/D_n\), where \(\eta>0\) is
fixed and small, retain marked edges meeting no other marked edge, and
delete their vertices.  The expected one-round survival factor of every
nonexceptional vertex is \(1-\Theta(\eta)\).

For a fixed vertex, the covariance terms in its marked-edge count are
bounded by \(O(\Delta_2/D_n)\); (4.2) therefore gives concentration around
the same survival factor uniformly outside an \(o(|V|)\) set.  The degree
and codegree hypotheses are inherited, with both scaled by the appropriate
survival powers.  Iterating a fixed number of rounds leaves an arbitrarily
small fixed fraction of vertices.  Letting that number tend to infinity
slowly with \(n\), while keeping the accumulated concentration error
\(o(1)\), leaves \(o(|V|)\) vertices.  The retained edges over all rounds
are disjoint.  The original exceptional set is already \(o(|V|)\), so it
does not affect the conclusion.  \(\square\)

Apply the lemma with \(k=6\), \(D=r^3/2\).  Equations (2.4), (2.8), and
(3.4) verify every hypothesis.  We obtain a matching missing
\(o(2N)\) vertices.  Since every edge contains exactly three vertices
from each shore and both shores have size \(N\), it misses \(o(N)\) on
each shore.  This proves (0.4).

In any completed \(\mathcal D_r\)-port factor, each path row contains
exactly \(r\) vertices of \(\mathcal L\).  Therefore the lower vertices
of this geometric packing meet at least

\[
                         \frac{N-o(N)}r=(1-o(1))C_r    \tag{4.3}
\]

distinct path rows, regardless of how the factor is completed.  This is
the requested \(\Omega(C_r)\) row scale.  It does not say that the three
lower vertices of an individual hexagon lie on three distinct rows.

## 5. Why a geometric hexagon is not yet a switch

Let \(G_r\) be the incidence graph between \(\mathcal L\) and
\(\mathcal Y\).  Given a vertex-disjoint hexagon packing, choose one of
the two cyclic incidence matchings on every hexagon.  Their union \(Q\)
is a partial matching in \(G_r\).

It extends to an outgoing perfect matching if and only if the residual
graph satisfies Hall:

\[
 |N_{G_r-V(Q)}(A)|\ge|A|
 \qquad\text{for every }A\subseteq\mathcal L\setminus V(Q).       \tag{5.1}
\]

Nothing in Sections 1--4 enforces (5.1).

### Proposition 5.1 (one prescribed incidence can destroy completion)

For every \(r\ge3\), \(G_r\) has an upper vertex of degree one.  Put

\[
 Y_*=\{2\}\cup\{r+1,r+2,\ldots,2r\},\qquad
 X_*=Y_*\setminus\{2r\}.                               \tag{5.2}
\]

Then \(X_*\in\mathcal L\), every other \(r\)-subset of \(Y_*\) belongs
to \(\overline{\mathcal D_r}\), and hence

\[
                         N_{G_r}(Y_*)=\{X_*\}.          \tag{5.3}
\]

Consequently any partial matching which matches \(X_*\) to an upper
vertex other than \(Y_*\) has no perfect-matching completion.

#### Proof

Use the nonpositive-path characterization of
\(\overline{\mathcal D_r}\).  Deleting \(2\) from \(Y_*\) gives the word
\(0^r1^r\), which is nonpositive.  If
\(q\in\{r+1,\ldots,2r-1\}\) is deleted, the remaining word has its only
early up-step at position \(2\); its prefix height never exceeds zero.
Thus these \(r\)-sets are also barred.

Deleting \(2r\) gives \(X_*\).  At prefix \(2r-1\), this word has all
\(r\) of its up-steps and only \(r-1\) down-steps, so its height is one.
It is not nonpositive and hence belongs to \(\mathcal L\).  This proves
(5.3).  The completion obstruction is immediate.  \(\square\)

There are legal geometric hexagons in the unrestricted six-vertex
hexagon system containing \(X_*\) but not \(Y_*\).  For example take

\[
 K=X_*\setminus\{2\}=\{r+1,\ldots,2r-1\}
\]

and the three labels \(1,2,3\).  The lower extensions
\(K+1,K+2,K+3\) all lie in \(\mathcal L\), while none of the three upper
vertices is \(Y_*\).  Either cyclic orientation therefore matches
\(X_*=K+2\) away from \(Y_*\), so this single hexagon cannot be part of
any completing outgoing matching.

This particular core is not ballot-eligible, because \(K+2r\) is barred.
Thus the example proves that geometric legality plus vertex-disjointness
does not formally imply matching extendability, but it does not rule out
a stronger extension theorem for the eligible-core subhypergraph
\(\mathcal H_r\).  Such a theorem would have to prove the residual Hall
inequalities (5.1); they are not consequences of the degree/codegree
census.

## 6. The abstract path-factor completion gate

Suppose a packed hexagon family and its orientations do satisfy (5.1), so
that \(Q\) extends to an outgoing perfect matching \(M^+\).  Three further
conditions remain before the hexagons even become valid abstract
path-factor switches.

1. The opposite three incidence edges of every hexagon must be absent from
   the incoming matching \(M^-\); otherwise the six-cycle is not
   \(F\)-alternating.
2. The degree factor \(M^+\cup M^-\) must have no cycle component and
   must pair every Dyck root with a barred endpoint.
3. For a clean three-cycle router, the three selected edges must lie on
   three distinct strands.  Folded configurations instead require the
   exact strand-diagram test.

One safe way to guarantee all three conditions is to start from a completed
path factor and pack only its already alternating, strand-admissible
hexagons.  But the high-degree calculation in Sections 1--4 is for all
geometric hexagons; it gives no degree or codegree lower bound after this
restriction.

Equivalently, if \(M_0\) is a known completing outgoing matching, a packed
hexagon is automatically compatible with \(M_0\) only when its three upper
vertices are exactly the \(M_0\)-images of its three lower vertices.  That
condition is precisely an \(M_0\)-alternating directed three-cycle.  The
ballot theorem guarantees a directed cycle of unspecified length in every
eligible core, but does not guarantee a three-cycle, distinct strands, or
positive row degree.

At this stage the result is still only an abstract middle-levels
\(b\)-factor/path ledger.  The next section records the independent
metric obstruction to installing it in a wreath.

## 7. Fixed-exterior geodesicity kills every nonidentity hexagon twist

Let a nominal local slab use coordinates \(J\), \(|J|=2r\), and a fixed
exterior \(O\).  A clean completed hexagon on three root strands induces
a three-cycle \(\tau\) of their port labels.  The row indexed by \(P\)
would have local boundary states

\[
                       O\cup P,\qquad
                       O\cup(J\setminus\tau(P)).        \tag{7.1}
\]

Their Johnson distance is

\[
 d_J\bigl(O\cup P,O\cup(J\setminus\tau(P))\bigr)
                              =|P\cap\tau(P)|.          \tag{7.2}
\]

For a moved port \(P\ne\tau(P)\), the right side is strictly less than
\(r\).  But every contiguous \(r\)-step segment of a minimum wreath is
geodesic, so its endpoint distance must be \(r\).  Therefore:

### Theorem 7.1 (fixed-exterior hexagon obstruction)

No clean incidence hexagon inducing a nonidentity three-cycle can be
installed as an ordinary fixed-exterior \(r\)-step wreath slab.  This
remains impossible after adjoining a later inverse hexagon.

#### Proof

Equation (7.2) contradicts geodesicity on the first moved row.  A later
inverse operation cannot repair a nongeodesic earlier subpath; metric
defects are nonnegative and add over disjoint slabs.  \(\square\)

There is one exact escape.  Let the left and right exteriors be
\(O_L,O_R\), of equal size, and put

\[
                              e=|O_L\setminus O_R|.
\]

Then

\[
 d_J\bigl(O_L\cup P,
          O_R\cup(J\setminus\tau(P))\bigr)
                         =e+|P\cap\tau(P)|.             \tag{7.3}
\]

An \(r\)-step geodesic can therefore exist only when

\[
                    \boxed{e=|P\setminus\tau(P)|}       \tag{7.4}
\]

on every moved row.  A common three-cycle packet additionally needs the
same exterior toll \(e\) to satisfy (7.4) for all three ports, and it must
reprove all crossing-collar \(X/Y\) ledgers.  The geometric hexagon
packing controls none of these data.

The proved boundary is therefore sharp:

* the six-uniform incidence-hexagon hypergraph has a near-perfect integral
  matching;
* this matching geometrically covers \(N-o(N)\) lower row states and upper
  colours;
* arbitrary packed hexagons need not extend even to an outgoing incidence
  matching, already for one edge;
* after successful abstract path completion, every nonidentity
  fixed-exterior hexagon twist is still metrically impossible; and
* proving \(\Omega(C_r)\) literal three-cycle switches requires an
  exterior-moving packet satisfying (7.4), a completion-aware packing,
  and a full crossing-collar theorem.
