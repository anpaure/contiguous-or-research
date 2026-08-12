# Independent audit of `CENTRAL_EULER_UPPER_UNIVERSALITY.md`

## Verdict

The central graph theorem is correct.  For every upper target $y$, the
lexicographically selected-cover graph restricted below $y$ really does
have a component of coordinatewise maximum $y$.  The reverse-greedy proof
works for all boundary cases allowed by its hypotheses, including $s=2$,
zero coordinates of $y$, and coordinates with value $s-1$.

The exact induced-subgraph identity and the excursion criterion are also
correct.  The surface-complexity lemma has the right conclusion, but its
degree argument omits possible increments in zero coordinates between the
first and second positive coordinates.  A corrected incidence count still
gives maximum degree three.  Its trail-count paragraph also needs to cut
transition cycles arising inside components which are not globally
Eulerian; there are only $O(m^2)$ such cycles, so the stated asymptotic
conclusion survives.

The cubic intact-line theorem is **not proved under its stated hypothesis**.
Its proof uses the extra fact that every lower-central point occurs, whereas
the theorem only assumes coverage of targets of rank at least $2m$.  The
proof is valid after adding either of the equivalent hypotheses

* every natural line occurs at least once, or
* the word also covers every point of $V_m$ (hence covers every target of
  rank at least $2m-1$).

Under that corrected scope, the constant $11/192$ is correct.

The finite checker in the source was inspected and rerun through $m=8$;
it passes exactly as reported.  A separate checker which directly executes
the general reverse-greedy construction and audits the degree claim is
`scratch/audit_central_euler_upper_universality.py`.  It checks 32,928
instances with $2\le t\le5$, $2\le s\le7$, and all admissible $y$,
and checks the balanced degree claim through $m=10$.

## 1. Selected edges and induced subgraphs

For a rank-$s$ point $z$, let $p<q$ be its first two positive
coordinates and put

\[
 e_z=\{z-e_p,z-e_q\}.
\]

The endpoints are distinct and

\[
 (z-e_p)\vee(z-e_q)=z.                         \tag{1}
\]

It follows immediately that, for every coordinatewise upper bound $y$,

\[
 \{z-e_p,z-e_q\}\subseteq[0,y]
 \quad\Longleftrightarrow\quad z\le y.         \tag{2}
\]

Thus equation (2.3) in the source is the genuine vertex-induced restriction
of the selected edges.  There is no hidden implication in either direction.
The fact that the finite checker stores only vertices incident with a
selected edge is harmless: the path in Theorem 1 is nontrivial, since a
single rank-$(s-1)$ point cannot have maximum equal to a target of rank at
least $s$.

For a nonempty family of vertices contained in $[0,y]$, its maximum is
exactly $y$ if and only if it meets

\[
 F_i(y)=\{v:v_i=y_i\}
\]

for every coordinate $i$.  When $y_i=0$, every allowed vertex already
lies in $F_i(y)$, so zero coordinates cause no exception.

## 2. Reverse-greedy theorem

Put $S=s-1$.  Because $|y|\ge s>S$, reverse-greedy filling produces a
rank-$S$ point $x\le y$.  If $p$ is its first positive coordinate,
then

\[
 x_i=0\ (i<p),\qquad x_i=y_i\ (i>p),\qquad
 0<x_p\le y_p.                                  \tag{3}
\]

The following invariant makes every boundary case explicit.  Immediately
before coordinate $i$ is processed, all coordinates before $i$ are
zero.  If $x_i<y_i$, then $x_i<S$, because $y_i\le S$.  Hence some
later coordinate is positive.  Let $q>i$ be the first such coordinate.
Then

\[
 z=x+e_i\le y
\]

has first two positive coordinates $i,q$, and its selected edge joins

\[
 x=z-e_i,qquad x+e_i-e_q=z-e_q.                 \tag{4}
\]

Repeating (4) must reach $x_i=y_i$: whenever it has not done so, the total
mass $S$ guarantees another positive donor to the right.  Coordinates
strictly after $p$ attain their facets at the initial point, and each
coordinate $p,p-1,\ldots,1$ attains its facet when processed.  A coordinate
with $y_i=0$ needs no move.

Every move transfers one unit from $q$ to $i<q$, so

\[
 \Phi(x)=\sum_j jx_j
\]

strictly decreases.  The walk is consequently a simple selected-edge path.
All its vertices are below $y$, and collectively they meet every facet,
so their maximum is $y$.  There are at most $tS$ moves.  This proves
Theorem 1 exactly as stated.

In particular, setting $s=2m$ is valid because $m\le2m-1$.  Corollary 2
therefore holds for every $m\ge1$, not merely for the checked range.

## 3. Excursion criterion

Let $W=(w_0,\ldots,w_h)$ be one trail word.  An interval has maximum $y$
exactly when

1. every one of its letters is at most $y$, and
2. its letters meet every facet $F_i(y)$.

Enlarging such an interval to its maximal consecutive run of letters below
$y$ preserves both properties.  Conversely, a facet-spanning maximal
$y$-run is itself a witness.  Lemma 3 is therefore an exact equivalence.

Adjacent letters in a $y$-run are endpoints of an edge whose colour is
their maximum, hence that edge also lies below $y$ by (1).  Thus each run
is a path in $G_m[y]$.  Connectivity of $G_m[y]$ does not force its edges
to occur in a single run of an Euler word, so the document correctly leaves
the simultaneous excursion lemma open.

When several trail words are concatenated, the lemma certifies witnesses
contained within one trail.  New cross-trail intervals may create additional
witnesses, but none is needed for the conditional implication in Section 6.

## 4. Corrected degree and surface count

Assume first $m\ge2$, and let $p<q$ be the first two positive coordinates
of $v\in V_m$.  Every possible incident middle colour is $z=v+e_i$ for a
coordinate with $v_i<m$.  The vertex $v$ is an endpoint of the selected
edge below $z$ precisely when the added coordinate $i$ is one of the
first two positive coordinates of $z$.  Therefore

\[
 \deg(v)=\#\{i\le q:v_i<m\}.                     \tag{5}
\]

Indeed, for $i<p$ the selected pair is $(i,p)$; for $p<i<q$ it is
$(p,i)$; for $i=p$ or $q$ it contains $i$; and for $i>q$ the first
two positives remain $(p,q)$, so $v$ is not selected.

If $q\le3$, (5) gives degree at most three.  If $q=4$, the only positive
coordinates are $p,4$, and

\[
 v_p+v_4=2m-1.
\]

Since both are at most $m$, one equals $m$, making at least one of the
four candidate increments illegal.  Again the degree is at most three.
For $m=1$, the four lower vertices form $K_4$, so the maximum degree is
also three.  This separately repairs the small case in which a lower vertex
has only one positive coordinate.

The source proof's list "before $p$, or at $p$ or $q$" omits the
legal increments strictly between $p$ and $q$.  In particular, its
sentence for $p=1$ is not a complete incidence argument, although the
degree-three conclusion is correct.

Outside

\[
 B=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\},
\]

we have $p=1,q=2$, both increments are legal, and (5) gives degree exactly
two.  Fixing $(v_3,v_4)$, these vertices form one contiguous segment of the
$(1,2)$-coordinate line, with consecutive points joined.  Hence

\[
 c(G_m-B)\le(m+1)^2.
\]

Since $|B|=O(m^2)$, adding $B$ back proves that the number of components,
the number of isolated vertices, and the number of vertices of degree other
than two are all $O(m^2)$.

There is one small omitted justification in the trail paragraph.  Pairing
the two half-edges at every degree-two vertex and one pair at every
degree-three vertex partitions the graph edges into open transition trails
and transition cycles.  The open trails number half the odd-degree vertices.
A transition cycle which meets a degree-three vertex can be charged
injectively to such a vertex, because its unique paired transition belongs
to only one cycle.  A transition cycle with no degree-three vertex is an
entire degree-two graph component and can be charged to that component.
After cutting every transition cycle, the number of trail words is at most

\[
 \frac{o(G_m)}2+\#\{v:\deg(v)=3\}+c(G_m)=O(m^2). \tag{6}
\]

Thus the claimed word length $|Z_m|+O(m^2)$, conditional on the open
simultaneous excursion property, is sound.  One must cut cycles created by
the transition pairing even inside a graph component which has odd
vertices; cutting only globally all-even components is not quite enough.

The canonical orientation is also correct: an edge from $z-e_p$ to
$z-e_q$ moves one unit from $q$ to $p<q$ and strictly decreases
$\Phi$.  Outside $B$, the two incident edges give one incoming and one
outgoing edge.

## 5. Cubic intact-line theorem: corrected scope

For a transverse label $(c,d)$, the complete natural fibre should be
defined for all feasible

\[
 R=2m-1-c-d
\]

as

\[
 \{(a,R-a,c,d):\max(0,R-m)\le a\le\min(m,R)\}.  \tag{7}
\]

Formula (7.1) in the source is its untruncated form in the range used by the
counting argument.  These fibres partition $V_m$.

Now assume an intact line-block word contains every natural fibre at least
once and covers all targets of rank at least $2m$.  Equivalently for the
intended application, assume it covers $V_m$ as well as the upper half.
The equivalence follows because all letters have rank $2m-1$: an interval
whose maximum is $v\in V_m$ can contain only the letter $v$, since
$u\le v$ and $|u|=|v|$ imply $u=v$.

For

\[
 \frac m4\le R\le\frac m2,qquad
 c+d=2m-1-R,qquad c,d\le m-2,                   \tag{8}
\]

there are exactly $R-2$ ordered pairs $(c,d)$, up to the harmless
integer endpoints.  For every $R<a\le m$, the target

\[
 y=(a,0,c,d)
\]

has rank at least $2m$.

Every letter in a witness for $y$ has second coordinate zero.  A
nontrivial complete fibre has at most one such letter.  The only singleton
fibres with second coordinate zero have labels $(m,m-1)$ and
$(m-1,m)$, neither of which is below the $(c,d)$ in (8).  Hence a witness
must use the zero-coordinate endpoints at one seam between two adjacent
block occurrences.  A fixed seam has one fixed maximum and therefore serves
at most one target.

The number of required distinct seams is

\[
 \begin{aligned}
 N_m
 &=\sum_{R=\lceil m/4\rceil}^{\lfloor m/2\rfloor}
       (R-2)(m-R)\\
 &=\left(\int_{1/4}^{1/2}x(1-x)\,dx+o(1)\right)m^3\\
 &=\left(\frac{11}{192}+o(1)\right)m^3.          \tag{9}
 \end{aligned}
\]

There are only $O(m^2)$ fibre types.  Therefore (9) forces
$N_m-O(m^2)$ occurrences beyond one copy of each fibre.  The first copies
have total length $|V_m|$, and every extra occurrence has positive length.
Finally,

\[
 |Z_m|-|V_m|=m+1,                                \tag{10}
\]

which follows directly from the two adjacent coefficients of
$(1+x+\cdots+x^m)^4$.  Equations (9)--(10) give

\[
 |W|\ge |Z_m|+\left(\frac{11}{192}+o(1)\right)m^3.
\]

This proves the corrected theorem and verifies its constant.

What does **not** follow from the source proof is that upper-half coverage
alone forces one occurrence of every natural fibre.  A middle target has
several lower covers, and its representation need not use a prescribed
lower vertex.  Therefore the baseline $|V_m|$ cannot be inserted from the
stated upper-only hypothesis.  The original Theorem 5 should be replaced by:

> **Corrected Theorem 5.** If an intact line-block word covers every point
> of rank at least $2m-1$, then
> \[
> \[
> |W|\ge |Z_m|+(11/192+o(1))m^3.
> \]
> \]

The weaker upper-only version may or may not be true, but it is not proved
by the current argument.

## 6. Exact surviving mathematical status

The audited ledger is:

* **proved:** the selected edge below every middle point has the right
  adjacent maximum;
* **proved:** every upper target has a facet-spanning component in its
  selected induced graph;
* **proved after the degree-proof repair:** all graph branching and trail
  overhead are $O(m^2)$;
* **proved:** a word witnesses $y$ exactly when one of its maximal
  $y$-runs spans every facet;
* **open:** one transition system which supplies such a run for all upper
  targets simultaneously;
* **proved under the corrected lower-layer hypothesis:** intact natural-line
  blocks incur the cubic penalty $11m^3/192+o(m^3)$;
* **not proved:** that cubic additive penalty from upper-half coverage alone;
* **not addressed here:** the separate lower-half factor/pinning problem
  required for a universal max-word.

Thus the strongest positive result in the source survives the audit: the
upper-half obstruction has been reduced to a genuine simultaneous
transition problem on an $O(m^2)$-branching kernel.  The only retraction is
the scope of the intact-line lower bound, not the central component theorem.
