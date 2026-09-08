# Doubly-rainbow Hamilton cycles on odd ground: the paired-matching gate and its minimal exchange

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Put

\[
 n=2m+1,\qquad
 {\cal X}=\binom{[n]}m,\qquad
 {\cal U}=\binom{[n]}{m+1},\qquad
 {\cal L}=\binom{[n]}{m-1},
\]

\[
 W=|{\cal X}|=|{\cal U}|,\qquad
 N=|{\cal L}|={m\over m+2}W,\qquad
 D=W-N={2W\over m+2}=o(W).                                  \tag{0.1}
\]

For a Hamilton cycle \(C\) of \(J(n,m)\), every edge has a lower color
\(X\cap Y\in{\cal L}\) and an upper color \(X\cup Y\in{\cal U}\).
Because \(C\) has \(W=|{\cal U}|\) edges, upper rainbowness means that
every upper color occurs exactly once.  Lower completeness means that
every lower color occurs at least once; its unavoidable repeat mass is
exactly \(D\).

This note does not prove the final asymptotic construction.  It isolates
an exact smaller theorem and proves its complete local exchange calculus.

1. Fix one perfect matching \(M_0\) of the middle-level incidence graph.
   Delete it.  The residual graph is \(m\)-regular and bipartite.
   Every residual incidence edge has a canonical lower color, and every
   lower color class has exactly \(m+2\) edges.
2. A second perfect matching \(M_1\) gives an upper-rainbow spanning
   \(2\)-factor.  It is one Hamilton cycle exactly when the permutation
   \(M_1^{-1}M_0\) is one \(W\)-cycle.  Its lower colors are complete
   exactly when \(M_1\) meets every one of the \(N\) canonical color
   classes.
3. The uniform fractional perfect matching on the residual graph gives
   every lower color load

   \[
                                {m+2\over m}=1+{2\over m}.     \tag{0.2}
   \]

   Hence all degree equations and all lower covering inequalities are
   fractionally feasible, with the exact total excess \(D\).  There is
   no LP/Hall cut at this level.
4. The first possible perfect-matching exchange is an alternating
   \(6\)-cycle; there are no alternating \(4\)-cycles.  A legal
   \(6\)-cycle flip multiplies the monodromy by a \(3\)-cycle and changes
   exactly three paired-deletion colors.  It preserves Hamiltonicity
   precisely in one of the two cyclic orders described in Theorem 7.2.

Thus the exact minimal remaining theorem is:

> **Paired-matching Hamilton-surjection theorem.**  For some perfect
> matching \(M_0\) of the middle-level incidence graph, find a perfect
> matching \(M_1\) in its complement such that
> \(M_1^{-1}M_0\) is one cycle and \(M_1\) meets every canonical lower
> color class.

Its \(o(W)\)-defect version asks that only \(o(W)\) color classes be
missed.  The known upper-rainbow Hamilton cycle supplies the cyclic
matching pair but not the color surjection.  The known lower-rainbow
cycle supplies the color surjection in a repeated-upper ledger but not
the matching pair.  The theorem above is exactly the missing common
refinement.

## 1. The middle-level incidence graph

Let \(B_m\) be the bipartite graph with shores \({\cal U}\) and
\({\cal X}\), where \(X\sim U\) when \(X\subset U\).  Both shores have
size \(W\), and \(B_m\) is \((m+1)\)-regular.

An upper-rainbow Johnson Hamilton cycle

\[
                         X_0X_1\cdots X_{W-1}X_0             \tag{1.1}
\]

lifts uniquely to the alternating Hamilton cycle

\[
 X_0,U_0,X_1,U_1,\ldots,X_{W-1},U_{W-1},X_0,\qquad
                         U_i=X_i\cup X_{i+1},                 \tag{1.2}
\]

of \(B_m\).  Conversely, suppressing the \({\cal U}\)-shore of a
Hamilton cycle in \(B_m\) gives an upper-rainbow Hamilton cycle in
\(J(n,m)\).

Color the edges of the even cycle (1.2) alternately.  Its two color
classes are edge-disjoint perfect matchings \(M_0,M_1\) of \(B_m\).
This proves the following exact equivalence.

### Theorem 1.1 (paired-perfect-matching normal form)

Let \(f_i:{\cal U}\to{\cal X}\) be the bijection defined by \(M_i\).
The union \(M_0\cup M_1\) is one Hamilton cycle of \(B_m\) if and only if

\[
                         \sigma=f_1^{-1}f_0                 \tag{1.3}
\]

is one \(W\)-cycle on \({\cal U}\).

When the matchings are edge-disjoint, define

\[
 \lambda(U)=f_0(U)\cap f_1(U)\in{\cal L}.                     \tag{1.4}
\]

The projected Johnson cycle is lower-complete if and only if

\[
                         \lambda({\cal U})={\cal L}.          \tag{1.5}
\]

#### Proof

Starting from \(U\), two alternating steps in \(M_0\cup M_1\) give

\[
 U\stackrel{M_0}{\longmapsto}f_0(U)
   \stackrel{M_1}{\longmapsto}f_1^{-1}f_0(U)=\sigma(U).
\]

Thus alternating components are in bijection with cycles of \(\sigma\).
At \(U\), the two selected middle facets are \(f_0(U)\) and \(f_1(U)\);
their projected Johnson edge has union \(U\) and intersection (1.4).
This proves both assertions. \(\square\)

Theorem 1.1 includes connectivity exactly; no separate subtour
qualification remains.

## 2. Fixing the first matching produces canonical lower-color classes

Fix an arbitrary perfect matching \(M_0\), with bijection \(f_0\), and
put

\[
                              G_0=B_m-M_0.                    \tag{2.1}
\]

Then \(G_0\) is \(m\)-regular and bipartite.  Give an edge \(UX\in G_0\)
the color

\[
                              c_0(UX)=f_0(U)\cap X.            \tag{2.2}
\]

Both \(f_0(U)\) and \(X\) are distinct \(m\)-facets of \(U\), so this is
an \((m-1)\)-set.

### Theorem 2.1 (exact color-class census)

For every \(L\in{\cal L}\),

\[
                    E_L:=\{UX\in E(G_0):c_0(UX)=L\}
\]

has exactly

\[
                              |E_L|=m+2                       \tag{2.3}
\]

edges.  At every \(U\in{\cal U}\), the \(m\) incident edges of \(G_0\)
have pairwise distinct colors.

#### Proof

Fix \(L\).  For each of the \(m+2\) middle supersets
\(Y=L\cup\{a\}\), let \(U=f_0^{-1}(Y)\).  Since \(f_0(U)=Y\subset U\),
write \(U=Y\cup\{b\}\), where \(b\notin Y\), and put

\[
                              X=L\cup\{b\}.                    \tag{2.4}
\]

Then \(X\subset U\), \(X\ne Y=f_0(U)\), and \(Y\cap X=L\).
Different \(Y\)'s give different \(U\)'s, so this constructs \(m+2\)
distinct edges of color \(L\).

Conversely, an edge \(UX\) of color \(L\) has
\(f_0(U)=L\cup\{a\}\) for a unique \(a\), so it is the edge produced
from that \(Y=f_0(U)\).  This proves (2.3).

For fixed \(U\), write \(f_0(U)=U\setminus\{b\}\).  The other facets are
\(U\setminus\{a\}\), \(a\in f_0(U)\), and their colors are
\(f_0(U)\setminus\{a\}\), which are distinct. \(\square\)

Consequently the paired-matching Hamilton-surjection theorem is
equivalently:

\[
 \boxed{
 \begin{array}{c}
 \text{find a perfect matching }M_1\subseteq G_0,\\
 M_1\cap E_L\ne\varnothing\quad(L\in{\cal L}),\\
 f_1^{-1}f_0\text{ is one }W\text{-cycle}.
 \end{array}}                                                \tag{2.5}
\]

This is the exact minimal finite theorem promised in Section 0.

## 3. The integer program and the absence of a fractional cut

For \(e\in E(G_0)\), introduce \(x_e\in\{0,1\}\).  Ignoring only the
one-cycle condition, the exact covering-matching system is

\[
 \sum_{e\ni U}x_e=1\quad(U\in{\cal U}),\qquad
 \sum_{e\ni X}x_e=1\quad(X\in{\cal X}),                       \tag{3.1}
\]

\[
                         \sum_{e\in E_L}x_e\ge1
                                      \quad(L\in{\cal L}).     \tag{3.2}
\]

### Theorem 3.1 (universal fractional barycenter)

For every first matching \(M_0\), the relaxation of (3.1)--(3.2) has
the feasible point

\[
                              x_e={1\over m}
                              \quad(e\in E(G_0)).              \tag{3.3}
\]

Every lower covering row has the same strict value

\[
                              x(E_L)={m+2\over m}.             \tag{3.4}
\]

#### Proof

The graph \(G_0\) is \(m\)-regular, so (3.3) satisfies both perfect
matching shores in (3.1).  Equation (3.4) follows from Theorem 2.1.
\(\square\)

Thus the bipartite perfect-matching polytope contains a completely
symmetric point satisfying every physical lower-cover inequality.  The
slack \(2/m\) per lower color is exactly the scalar excess:

\[
 \sum_{L\in{\cal L}}\left({m+2\over m}-1\right)
 ={2N\over m}=D.                                             \tag{3.5}
\]

The equality follows from \(N=mW/(m+2)\).  Therefore neither a
fractional Hall cut nor a first-moment shortage can refute (2.5).
The obstruction, if one exists, is an integral colored-matching or
monodromy obstruction.

## 4. Exact lower-defect ledger

For a perfect matching \(M_1\subseteq G_0\), put

\[
 \ell(L)=|M_1\cap E_L|,\qquad
 h(M_1)=|\{L\in{\cal L}:\ell(L)=0\}|.                         \tag{4.1}
\]

Since \(M_1\) has \(W\) edges,

\[
 \sum_L\ell(L)=W.
\]

### Proposition 4.1 (forced-excess identity)

\[
 \boxed{
 h(M_1)=\sum_{L\in{\cal L}}(\ell(L)-1)_+-D.}                  \tag{4.2}
\]

Thus lower completeness is equivalent to repeat excess exactly \(D\),
and the asymptotic target is repeat excess \(D+o(W)\).

#### Proof

If \(S=\{L:\ell(L)>0\}\), then

\[
 \sum_L(\ell(L)-1)_+=W-|S|,\qquad h=N-|S|.
\]

Subtract and use \(W-N=D\). \(\square\)

This is the correct one-sided objective.  It does not penalize the
unavoidable \(D\) repeats.

## 5. The exact point ledger and its feasibility

Assume now that \(M_0\cup M_1\) is a spanning \(2\)-factor; connectivity
is not needed.  The upper load is \({\bf1}_{\cal U}\), the middle degree
is two at every owner, and the lower load is \(\ell\).  The point
valuation identity gives, for every coordinate \(v\),

\[
 \sum_{L\ni v}\ell(L)
   =2\binom{2m}{m-1}-\binom{2m}{m}.                           \tag{5.1}
\]

If \(\ell\ge{\bf1}_{\cal L}\), define the repeat multiset

\[
                              r=\ell-{\bf1}_{\cal L}.          \tag{5.2}
\]

Then

\[
 \sum_Lr(L)=D,\qquad
 \sum_{L\ni v}r(L)=\kappa\quad(v\in[n]),                     \tag{5.3}
\]

where

\[
 \boxed{
 \kappa=
 2\binom{2m}{m-1}-\binom{2m}{m}-\binom{2m}{m-2}
 ={D(m-1)\over2m+1}.}                                       \tag{5.4}
\]

Thus every exact solution has a regular lower-repeat multidesign.  This
necessary condition is numerically feasible even with no repeated block
in the repeat family.

### Theorem 5.1 (simple regular repeat family)

There is a family \({\cal Q}\subseteq{\cal L}\) of size \(D\) such that

\[
                         |\{L\in{\cal Q}:v\in L\}|=\kappa
                                      \quad(v\in[n]).          \tag{5.5}
\]

#### Proof

The first expression in (5.4) proves that \(\kappa\) is an integer.
Among all \(D\)-element subfamilies of \({\cal L}\), choose one minimizing
the sum of squares of its point degrees.

Suppose coordinates \(a,b\) have degrees \(d_a\ge d_b+2\).  The number
of selected blocks containing \(a\) but not \(b\) exceeds the number
containing \(b\) but not \(a\).  The coordinate swap

\[
                         L\longmapsto L-a+b                    \tag{5.6}
\]

is a bijection between the two full classes.  Hence some selected
\(L\ni a,\ b\notin L\) has \(L-a+b\) unselected.  Replacing \(L\) by
\(L-a+b\) decreases the degree-square sum by

\[
                         2(d_b-d_a)+2<0,
\]

a contradiction.  All degrees therefore differ by at most one.  Their
average is

\[
                         {D(m-1)\over2m+1}=\kappa,
\]

an integer, so they all equal \(\kappa\). \(\square\)

Theorem 5.1 rules out the point ledger as the missing obstruction.
The regular repeat family still has to be realized by one perfect
matching and one-cycle monodromy.

## 6. The legal exchange digraph

Fix edge-disjoint perfect matchings \(M_0,M_1\), with bijections
\(f_0,f_1\).  Define a directed graph \(D(M_0,M_1)\) on \({\cal U}\) by
putting an arc

\[
 V\longrightarrow U
\]

when

\[
 f_1(V)\subset U,\qquad V\ne U,\qquad f_1(V)\ne f_0(U).       \tag{6.1}
\]

The last inequality is precisely what prevents a flip from making the
two matchings share an edge.

### Theorem 6.1 (exact exchange degree)

The digraph \(D(M_0,M_1)\) is \((m-1)\)-in-regular and
\((m-1)\)-out-regular.  It has no directed \(2\)-cycle.

Every directed cycle

\[
                         U_0\to U_1\to\cdots
                              \to U_{r-1}\to U_0              \tag{6.2}
\]

defines another perfect matching \(M_1'\subseteq G_0\) by

\[
                         f_1'(U_i)=f_1(U_{i-1})                \tag{6.3}
\]

with indices modulo \(r\), and \(f_1'=f_1\) elsewhere.

#### Proof

For fixed \(V\), the middle set \(f_1(V)\) has \(m+1\) upper cofacets.
One is \(V\).  Exactly one other is \(f_0^{-1}(f_1(V))\), because the
matchings are bijective and edge-disjoint.  Removing those two leaves
\(m-1\) legal outneighbors.

For fixed \(U\), its \(m+1\) middle facets have unique \(f_1\)-preimages.
The facet \(f_1(U)\) gives the forbidden loop, and \(f_0(U)\) gives the
unique forbidden shared \(M_0\)-edge.  This leaves \(m-1\) legal
inneighbors.

A directed \(2\)-cycle would give two distinct upper sets with two
distinct common middle facets.  This is impossible: two distinct
\((m+1)\)-sets have at most one common \(m\)-subset.  Thus there are no
directed \(2\)-cycles.

Along (6.2), equation (6.1) makes every assignment in (6.3) an incidence
edge outside \(M_0\).  The right partners are merely cyclically permuted,
so (6.3) is again a perfect matching. \(\square\)

Since there are no \(4\)-cycles in \(B_m\), Theorem 6.1 also proves that
an alternating \(6\)-cycle is the smallest possible nontrivial exchange
of one perfect matching.

## 7. Monodromy and lower-color derivative of a flip

Let

\[
                         \tau=(U_0\,U_1\,\cdots\,U_{r-1})      \tag{7.1}
\]

for the directed cycle in (6.2), and put
\(\sigma=f_1^{-1}f_0\).

### Theorem 7.1 (exact flip derivative)

The flipped monodromy and lower load are

\[
 \boxed{\sigma'=\tau\sigma,}                                  \tag{7.2}
\]

\[
 \boxed{
 \ell'-\ell=
 \sum_{i=0}^{r-1}
 \left(
 e_{\,f_0(U_i)\cap f_1(U_{i-1})}
 -
 e_{\,f_0(U_i)\cap f_1(U_i)}
 \right).}                                                    \tag{7.3}
\]

#### Proof

Equation (6.3) says \(f_1'=f_1\tau^{-1}\) on the affected vertices.
Hence

\[
 f_1'^{-1}f_0=\tau f_1^{-1}f_0=\tau\sigma.
\]

At \(U_i\), only the second selected facet changes, from \(f_1(U_i)\)
to \(f_1(U_{i-1})\).  Taking its intersection with the fixed first
facet \(f_0(U_i)\) gives (7.3). \(\square\)

The formula shows simultaneously why matching exchange is not enough:
one must control the cycle type of \(\tau\sigma\) and the signs of the
literal lower colors.

### Theorem 7.2 (minimal Hamilton-safe \(6\)-cycle)

Assume \(r=3\) and that \(\sigma\) is one \(W\)-cycle.  Then
\(\tau\sigma\) is one \(W\)-cycle exactly when the cyclic order of

\[
                              U_0,U_1,U_2                       \tag{7.4}
\]

along \(\sigma\) agrees with the orientation
\(\tau=(U_0\,U_1\,U_2)\).  In the opposite cyclic order,
\(\tau\sigma\) has three cycles.

#### Proof

Let \(p_i=\sigma^{-1}(U_i)\).  Left multiplication by \(\tau\) changes
only the three arcs entering the \(U_i\)'s:

\[
 p_0\to U_0,\ p_1\to U_1,\ p_2\to U_2
\quad\longmapsto\quad
 p_0\to U_1,\ p_1\to U_2,\ p_2\to U_0.                       \tag{7.5}
\]

If the old cyclic order is \(U_0,U_1,U_2\), the three intervening path
segments are rejoined in one cycle.  If the order is
\(U_0,U_2,U_1\), each segment closes to itself, giving three cycles.
\(\square\)

Thus even the smallest legal color trade has a sharp chronological
orientation constraint.  An arbitrary alternating \(6\)-cycle cannot be
used as an absorber.

For completeness, suppose the three old colors

\[
 D_i=f_0(U_i)\cap f_1(U_i)
\]

and the three new colors

\[
 A_i=f_0(U_i)\cap f_1(U_{i-1})
\]

are pairwise distinct.  Then Proposition 4.1 gives the exact hole change

\[
 \boxed{
 h(M_1')-h(M_1)
  =|\{i:\ell(D_i)=1\}|
   -|\{i:\ell(A_i)=0\}|.}                                    \tag{7.6}
\]

The flip is a strict lower-hole descent exactly when it fills more old
holes than it creates by removing singleton colors.

## 8. The exact remaining local-to-global theorem

The preceding reductions identify a concrete exchange statement which
would prove the asymptotic result.

### Ordered alternating-cycle descent \(\operatorname{OACD}(\varepsilon)\)

For every sufficiently large \(m\), whenever

* \(M_0,M_1\) are edge-disjoint perfect matchings of \(B_m\);
* \(\sigma=f_1^{-1}f_0\) is one cycle; and
* \(h(M_1)\ge\varepsilon W\),

the legal exchange digraph \(D(M_0,M_1)\) contains a directed cycle
(6.2) such that

\[
                         \tau\sigma\text{ is one cycle}        \tag{8.1}
\]

and the literal derivative (7.3) strictly decreases \(h\).

### Theorem 8.1 (descent sufficiency)

If \(\operatorname{OACD}(\varepsilon)\) holds for every fixed
\(\varepsilon>0\), then there are upper-rainbow Johnson Hamilton cycles
with \(o(W)\) missing lower colors.  If it holds whenever \(h>0\), there
is an exact doubly-rainbow Hamilton cycle.

#### Proof

Start from the known middle-level Hamilton cycle and its matching pair.
While \(h\ge\varepsilon W\), apply the asserted exchange.  Equations
(7.2) and (8.1) retain one Hamilton cycle; construction of
\(D(M_0,M_1)\) retains two edge-disjoint perfect matchings, hence exact
upper rainbowness; and \(h\) decreases by at least one.  The process
terminates with \(h<\varepsilon W\).  Apply this for a diagonal sequence
\(\varepsilon=\varepsilon_m\to0\).  The exact version is identical with
threshold one. \(\square\)

The theorem does not assert \(\operatorname{OACD}\).  It isolates the
first genuinely unresolved interface:

* \(D(M_0,M_1)\) has large exact degree \(m-1\), but it may have no
  directed triangles;
* a directed cycle need not be ordered so that \(\tau\sigma\) stays
  cyclic; and
* even a Hamilton-safe cycle need not have the favorable hole derivative
  in (7.3).

These three requirements, rather than marginal capacity, are the complete
conditions for the monotone alternating-cycle descent route isolated
here.  A nonmonotone trajectory or a direct global construction could
bypass \(\operatorname{OACD}\), but it must still solve the exact
paired-matching gate (2.5).
