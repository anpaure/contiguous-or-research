# Prime cyclic quotient audit: voltage objects, the two-loop law, and the exact-cover dual

Date: 2026-07-26

## 0. Verdict

Let

\[
        p=2m+1
\]

be prime, and let translation by \(1\) act on the odd graph

\[
        O_m=KG(p,m).
\]

The prime-cyclic construction has an exact and rather rigid normal form.

* The quotient has

  \[
       T={1\over p}{p\choose m}=C_m
  \]

  vertices, is \((m+1)\)-regular as a voltage multigraph (loops counted
  twice), has \(T(m+1)/2\) edge orbits, and has exactly \(m\) loop edge
  orbits.
* A translation-invariant exact wreath factor is exactly a partition of
  the quotient vertices into nonzero-voltage AP loops and simple
  zero-voltage \(p\)-cycles.
* Since

  \[
        C_m\equiv 2(-1)^m\pmod p,
  \]

  such a factor is impossible when \(m\) is odd.  When \(m\) is even it
  must use **exactly two** AP loops and \((T-2)/p\) zero-voltage
  \(p\)-cycles.
* For \(m=6,p=13\), the first nontrivial instance is therefore exactly:
  choose two of six AP loops, then partition the remaining \(130\) of
  the \(132\) quotient vertices into ten simple zero-voltage
  \(13\)-cycles.

This is a complete reduction, not a construction.  The exact remaining
problem is a perfect matching problem in a \(p\)-uniform cycle
hypergraph.  Its fractional Hall condition has the explicit Farkas dual
in Section 6.  Neither regularity of the quotient graph nor an ordinary
circulation proves the integral matching.

There are two rigorous obstructions to tempting algebraic shortcuts:

1. odd \(m\) is arithmetically impossible;
2. a physical cycle obtained as the translate orbit of one middle set is
   necessarily an AP wreath and hence gives only a quotient loop.  Thus
   cyclic Berge/difference-orbit decompositions do not supply the free
   zero-voltage cycles needed here.

No unrestricted construction or obstruction is proved for even
\(m\ge6\).  In particular, the canonical MSW factor cannot simply be
assumed translation-equivariant.

## 1. The regular prime cover

Write \(G=\mathbb Z_p\), and let \(G\) act by translation.  No nonzero
translation fixes a nonempty proper subset of \(G\): such a fixed subset
would be a union of orbits of a \(p\)-cycle.  Hence the action is free on
the vertices of \(O_m\), and

\[
        |V(O_m/G)|={1\over p}{p\choose m}=T.
\tag{1.1}
\]

The action is also free on undirected edges.  Indeed, if a nonzero
translation \(t\) fixes an edge \(\{A,B\}\), it either fixes \(A\), which
is impossible, or swaps \(A\) and \(B\).  In the latter case \(2t\)
fixes \(A\); this is again impossible because \(p\) is odd.  Since
\(O_m\) has degree \(m+1\), the quotient voltage multigraph \(Q=O_m/G\)
therefore has

\[
   |E(Q)|={1\over p}{ {p\choose m}(m+1)\over2}
          ={T(m+1)\over2}.
\tag{1.2}
\]

Every fibre vertex has the same \(m+1\) incident darts, so \(Q\) is
\((m+1)\)-regular when a loop contributes two to the degree.  Parallel
edges and loops must be retained; replacing \(Q\) by a simple graph
destroys the covering data.

Choose a representative \(A_v\) for each quotient vertex.  A quotient
dart \(v\to w\) has voltage \(a\in G\) when

\[
                 A_v\cap(A_w+a)=\varnothing.
\tag{1.3}
\]

The reverse dart has voltage \(-a\).  Changing representatives changes
the edge voltages by a coboundary, so the total voltage of a closed walk
is intrinsic.

## 2. Lift classification

Let \(\overline C\) be a closed quotient walk of length \(\ell\) and
total voltage \(a\).  One circuit around \(\overline C\) sends a starting
phase \(x\) to \(x+a\).  Consequently:

* if \(a=0\), the lift consists of \(p\) closed walks of length \(\ell\);
* if \(a\ne0\), the lift is one closed walk of length \(p\ell\).

Here primality is used only to say that every nonzero \(a\) has order
\(p\).

Every \(p=2m+1\) cycle of \(O_m\) is a wreath.  One elementary recovery
is as follows.  For consecutive disjoint \(m\)-sets \(A_i,A_{i+1}\), let
\(z_i\) be the unique point outside \(A_i\cup A_{i+1}\).  On every edge
not omitting a fixed coordinate \(z\), membership of \(z\) toggles.
Closure of the odd cycle forces every coordinate to be omitted an odd
number of times; the \(p\) omission counts sum to \(p\), so every
coordinate is omitted exactly once.  Reading the omissions in edge order
recovers a cyclic coordinate order, and the \(A_i\) are its middle
intervals (taken in odd-graph step order).

It follows that the admissible quotient objects lifting to wreaths are
exactly:

1. simple quotient \(p\)-cycles of total voltage zero, each lifting to a
   full orbit of \(p\) wreaths;
2. quotient loops of nonzero voltage, each lifting to one
   translation-fixed wreath.

A nonzero-voltage quotient cycle of length \(p\) lifts to length \(p^2\)
and is unusable.

## 3. Loops are precisely the AP wreaths

A quotient loop represented by voltage \(t\ne0\) is an \(m\)-set \(A\)
satisfying

\[
                     A\cap(A+t)=\varnothing.
\tag{3.1}
\]

Read membership in \(A\) around the cyclic order
\(0,t,2t,\ldots,(p-1)t\).  Equation (3.1) says that the \(m\) marked
positions form an independent set of maximum size in \(C_{2m+1}\).
There are \(m+1\) unmarked positions, so the gaps between consecutive
marked positions consist of \(m-1\) single gaps and one double gap.
Thus, up to translation,

\[
              A=\{0,2t,4t,\ldots,2(m-1)t\}.
\tag{3.2}
\]

This is exactly an arithmetic-progression wreath.  Replacing \(t\) by
\(-t\) reverses the same geometric wreath.  Hence there are

\[
                         {p-1\over2}=m
\tag{3.3}
\]

underlying quotient loops.  They lie at distinct quotient vertices:
if two AP loop vertices coincided, the two AP wreaths would have the same
middle support; the induced Johnson-adjacency cycle on that support
recovers the cyclic order up to reversal, so the two loops would be the
same.

Equivalently, count directly: for every \(t\ne0\) there are \(p\)
maximum independent sets satisfying (3.1), giving \(p(p-1)\) directed
loop incidences; division by two orientations and then by the orbit size
\(p\) again gives \(m\) loop edge orbits.

The same argument shows why a direct translate-orbit construction is too
small.  If

\[
       A,A+t,A+2t,\ldots,A+(p-1)t
\]

is itself an odd-graph \(p\)-cycle, then already
\(A\cap(A+t)=\varnothing\), so (3.2) applies.  Therefore every physical
wreath whose vertices form a single translate orbit is AP and projects
to a loop.  The free quotient \(p\)-cycles cannot arise this way; their
chronology must be nonlinear in the translation phase.

## 4. The sharp Catalan congruence

The quotient vertex count is the Catalan number

\[
       T=C_m={1\over m+1}{2m\choose m}.
\]

Modulo \(p=2m+1\),

\[
 {2m\choose m}={p-1\choose m}\equiv(-1)^m,
 \qquad (m+1)^{-1}\equiv2,
\]

and hence

\[
                       T\equiv2(-1)^m\pmod p.
\tag{4.1}
\]

Suppose a translation-invariant exact factor contains \(f\) fixed
wreaths.  Every other wreath occurs in a free orbit of size \(p\), so

\[
                         f\equiv T\pmod p.
\tag{4.2}
\]

The fixed wreaths are precisely the \(m\) AP wreaths from Section 3, so
\(0\le f\le m<p\).  Therefore:

* if \(m\) is odd, (4.1) gives \(f=p-2=2m-1>m\), which is impossible;
* if \(m\) is even, (4.1) and (4.2) force \(f=2\).

This proves a genuine statewise obstruction for all odd \(m\), and the
exact two-loop law for every possible even-\(m\) construction.  At
\(m=2,p=5\), the two loops are the entire factor.  At \(m=6,p=13\),

\[
             T=C_6=132=2+10\cdot13,
\tag{4.3}
\]

so the first nontrivial target is two loops plus ten free cycles.

## 5. Exact-cover formulation

Let \(\mathscr Z\) be the set of simple zero-voltage \(p\)-cycles of
\(Q\), and let \(\mathscr L\) be its \(m\) AP loops.  Let
\(A\in\{0,1\}^{V(Q)\times(\mathscr Z\sqcup\mathscr L)}\) be the
object--vertex incidence matrix: a cycle column has \(p\) ones and a loop
column has one.

For even \(m\), an invariant exact factor exists if and only if the
integer system

\[
 \boxed{
       Ax=\mathbf1,
       \qquad \sum_{L\in\mathscr L}x_L=2,
       \qquad x\in\mathbb Z_{\ge0}^{\mathscr Z\sqcup\mathscr L}}
\tag{5.1}
\]

is feasible.  The equations \(Ax=\mathbf1\) automatically force every
coordinate of \(x\) to be \(0\) or \(1\), so no separate binary
constraint is needed.

Equivalently, fix two distinct loops \(L_1,L_2\), delete their quotient
vertices, and delete every cycle meeting either vertex.  On the
remaining \(T-2\) vertices, form the \(p\)-uniform hypergraph

\[
       \mathcal H_{L_1,L_2}
       =\{V(C):C\in\mathscr Z,\,
                    V(C)\cap\{v(L_1),v(L_2)\}=\varnothing\}.
\tag{5.2}
\]

Then (5.1) is feasible if and only if at least one of the
\(\binom m2\) hypergraphs (5.2) has a perfect matching.  Thus the prime
cyclic lane is not an ordinary graph \(2\)-factor problem: graph
regularity can produce cycles of the wrong lengths and nonzero voltages.
The correct object is a perfect matching in the catalogue of already
closed, already zero-voltage \(p\)-cycles.

A completely explicit generator for the columns is the layered voltage
network with states

\[
                         (v,a,j)\in V(Q)\times G\times\{0,\ldots,p\}.
\]

A quotient dart \(v\xrightarrow{b}w\) gives an arc

\[
                  (v,a,j)\longrightarrow(w,a+b,j+1).
\]

Length-\(p\) paths from \((v,0,0)\) to \((v,0,p)\) which visit \(p\)
distinct quotient vertices are precisely the oriented columns in
\(\mathscr Z\).  This generates candidates, but the final
column-selection problem remains the hypergraph perfect matching (5.2).

## 6. The exact fractional Hall/Farkas gate

The LP relaxation of (5.1) has a clean dual certificate.  Introduce a
real weight \(y_v\) for each quotient vertex and a real scalar
\(\alpha\) for the equation selecting two loops.  Farkas' lemma gives:

> **Fractional feasibility criterion.**  The nonnegative real relaxation
> of (5.1) is feasible if and only if every \((y,\alpha)\) satisfying
>
> \[
>       \sum_{v\in V(C)}y_v\ge0
>              \quad(C\in\mathscr Z),
>       \qquad y_{v(L)}+\alpha\ge0
>              \quad(L\in\mathscr L)
> \tag{6.1}
> \]
>
> also satisfies
>
> \[
>                  \sum_{v\in V(Q)}y_v+2\alpha\ge0.
> \tag{6.2}
> \]

For a fixed loop pair, the criterion simplifies.  The fractional perfect
matching polytope of (5.2) is nonempty if and only if

\[
 \boxed{
   \left[
      \sum_{v\in V(C)}y_v\ge0\quad
      \hbox{for every }C\in\mathscr Z
      \hbox{ avoiding }L_1,L_2
   \right]
   \Longrightarrow
   \sum_{v\notin\{v(L_1),v(L_2)\}}y_v\ge0.}
\tag{6.3}
\]

This is the exact Hall-type gate.  It is stronger than vertex degree
regularity and cannot in general be reduced to subset cardinalities for
a \(p\)-uniform hypergraph.

Even (6.1)--(6.3) settle only the fractional problem.  The incidence
matrix in (5.1) is not known to be a network matrix or totally
unimodular, and no normality theorem is available here.  An integral
proof must therefore do one of the following:

1. construct the cycle matching explicitly;
2. prove a special integral decomposition theorem for this catalogue;
3. supply an absorber/rounding theorem which respects both length \(p\)
   and zero voltage.

Replacing a cycle column by its individual quotient edges turns the
problem into a circulation, but loses exactly the two constraints that
matter: component length and component voltage.  Thus “solve a flow” is
not, by itself, a completion of the prime-cyclic lane.

There is one further pitfall.  Translate-averaging an arbitrary exact
middle factor gives a fractional cover by **row orbits**, but a row orbit
need not be middle-transversal: its quotient walk may repeat vertices.
Such an orbit is not a column of \(\mathscr Z\).  Therefore this averaging
does not prove fractional feasibility of (5.1) or (5.2).  It proves
fractional feasibility only in a larger catalogue of zero-voltage closed
walks with repeated quotient vertices, which is insufficient for an
invariant exact factor.

## 7. Why existing cyclic difference-family results do not close it

There are two different notions of cyclic Hamilton cycle in the
literature which must not be conflated.

* A Katona--Kierstead/tight Hamilton cycle is a wreath: its edges are all
  consecutive \(m\)-windows of one cyclic coordinate order.  This is the
  notion used by Bailey and Stevens in their formulation of wreath and
  Hamilton-decomposition conjectures.
* A Berge Hamilton cycle only asks for an alternating sequence of
  distinct vertices and hyperedges with consecutive vertices incident
  to the corresponding hyperedge.  Petecki's cyclic Hamiltonian
  decomposition theorem is explicitly a theorem about **Berge** cycles.

The second notion is much weaker.  Arbitrary translate orbits can be
useful for Berge decompositions, whereas Section 3 proves that a
translate orbit which is an odd-graph/tight wreath must be AP.  Those
objects furnish only the \(m\) loop columns and cannot cover the
\(T-m\) generic quotient vertices.  Hence a cyclic Berge difference
family cannot be inserted into (5.1).

The difference-pattern machinery in Bailey--Stevens is a genuine tight
framework, but the cited constructions concern special fixed
uniformities (notably the developed \(k=3\) cases); it does not prove the
growing-uniformity, zero-voltage cycle factor (5.1).  The known MSW
factorization proves that some exact middle wreath factor exists, but it
does not provide the additional translation invariance required here.

Primary references for this distinction:

* R. F. Bailey and B. Stevens, *Hamiltonian decompositions of complete
  \(k\)-uniform hypergraphs*,
  <https://www.math.mun.ca/rbailey00/papers/hamhyp.pdf>.
* P. Petecki, *On cyclic Hamiltonian decompositions of complete
  \(k\)-uniform hypergraphs*, Discrete Mathematics 325 (2014), 74--78,
  <https://doi.org/10.1016/j.disc.2014.02.020>.

## 8. Precise surviving theorem

For primes \(p=2m+1\equiv1\pmod4\), prove that for some pair of AP loops
\(L_1,L_2\), the cycle hypergraph \(\mathcal H_{L_1,L_2}\) in (5.2) has
a perfect matching.

That statement is necessary and sufficient for a translation-invariant
exact middle wreath factor.  To advance the constant-one problem rather
than only the middle factor, the selected perfect matching must in
addition satisfy the simultaneous lower-necklace covering or balanced
load conditions.  Those colors are attached to the same cycle columns,
so independent rankwise flows do not compose.

The prime quotient has therefore achieved a real simplification--a
factor-\(p\) reduction and a sharp voltage normal form--but not an
asymptotic weakening.  The remaining object is an integral nonlinear
zero-voltage cycle resolution.  No cited difference-family theorem, no
ordinary quotient circulation, and no canonical-MSW equivariance
supplies it.
