# Equitable one-factorization at the Johnson projection

This note audits Proposition 4B of `KNESER_PROJECTION.md`.  The conclusion is
sharp.

* The proposed frequency-two theorem is false for general regular bipartite
  graphs, even when every distinguished set has the same size and average
  load strictly below two.
* Classical equitable-edge-colouring theorems solve each of the two marginal
  problems in the Boolean-lattice instance, but not their simultaneous
  coupling.
* The special graph \(H_m\) remains a legitimate open target.  It is exactly a
  common edge-colouring problem for the inclusion graph and the Johnson graph,
  or equivalently an integer-decomposition problem for a symmetric polytope.

No computation is used.

Throughout,

\[
 \mathcal A=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,
\]

\[
 N=|\mathcal A|=\binom{2m}{m-1},\qquad
 W=|\mathcal M|=\binom{2m}m,\qquad
 K=W-N=\frac{W}{m+1},
\]

and

\[
 D=\binom{m+1}{2}=\frac{m(m+1)}2.
\]

The inclusion graph \(H_m\) has the two copies of \(\mathcal A\) (the upper
copy is identified with complements of \((m+1)\)-sets) as its two parts.  It
is \(D\)-regular.

## 1. One edge set, two graph structures

An edge of \(H_m\) is an interval

\[
 e=(S,U),\qquad |S|=m-1,\quad |U|=m+1,\quad S\subset U.
\]

Writing \(U\setminus S=\{a,b\}\), associate to it the Johnson edge

\[
 j(e)=\bigl(S\cup\{a\}\bigr)\bigl(S\cup\{b\}\bigr).       \tag{1.1}
\]

This is a bijection

\[
 E(H_m)\longleftrightarrow E(J(2m,m)).                    \tag{1.2}
\]

Indeed, the inverse sends a Johnson edge \(PQ\) to
\((P\cap Q,P\cup Q)\).  For \(P\in\mathcal M\), the canonical set from
Proposition 4B is therefore exactly a Johnson star:

\[
 \mathcal Q(P)=j^{-1}\bigl(\delta_J(P)\bigr).             \tag{1.3}
\]

Consequently Proposition 4B asks for one colouring of the common edge set
with two simultaneous properties:

1. it is a proper \(D\)-edge-colouring in the \(H_m\) structure;
2. every colour has degree at most two in the Johnson structure.

The first condition says that every colour is a perfect matching of \(H_m\).
The second says that its Johnson projection is a graph of maximum degree two.
This is not an ordinary equitable edge-colouring of either graph alone.

For any colour class \(M_c\), properness in \(H_m\) gives \(|M_c|=N\), and
frequency two gives the useful identity

\[
 \sum_{P\in\mathcal M}|M_c\cap\mathcal Q(P)|=2N.          \tag{1.4}
\]

If all the summands are at most two, then

\[
 \sum_{P\in\mathcal M}
 \left(2-|M_c\cap\mathcal Q(P)|\right)=2(W-N)=2K.         \tag{1.5}
\]

Thus the Catalan defect occurs separately in every colour.

## 2. What the equitable-colouring theorems actually give

There are two different marginal theorems.

### 2.1 The inclusion-graph marginal

Kőnig's line-colouring theorem decomposes the \(D\)-regular bipartite graph
\(H_m\) into \(D\) perfect matchings.  Equivalently, de Werra's equitable
edge-colouring theorem, applied with \(D\) colours, gives one edge of every
colour at every vertex.  This proves properness in \(H_m\), but it says
nothing about the non-star subsets \(\mathcal Q(P)\).

The terminology matters.  In de Werra's theorem, equitable means that at
each *vertex of the graph being coloured*, the incident colour counts differ
by at most one.  The balanced condition controls parallel edges, and the
equalized condition controls total colour-class sizes.  None of these clauses
balances an arbitrary overlapping family of edge subsets.  See de Werra's
[bipartite equitable-colouring theorem](https://doi.org/10.1016/0012-365X(76)90056-X).

### 2.2 The Johnson-graph marginal

The Johnson graph \(J(2m,m)\) is simple and \(m^2\)-regular.  Moreover,

\[
 \frac{m^2}{D}=\frac{2m}{m+1}\in(1,2),\qquad D\nmid m^2
 \quad(m\ge2).                                             \tag{2.1}
\]

The Hilton--de Werra sufficient condition says that a simple graph has an
equitable \(k\)-edge-colouring whenever no vertex degree is divisible by
\(k\).  Applying it to the Johnson graph with \(k=D\) yields a colouring in
which every colour occurs once or twice at every middle vertex.  In the
language of \(H_m\), it balances every \(\mathcal Q(P)\) perfectly.  See
[Hilton--de Werra](https://doi.org/10.1016/0012-365X(94)90112-0).

But this Johnson colouring need not be proper at the lower- and upper-rank
vertices of \(H_m\).  Conversely, a Kőnig factorization of \(H_m\) need not
be equitable in the Johnson graph.  Proposition 4B is precisely the missing
**common** colouring.

This distinction is analogous to simultaneous edge-colouring, which is a
separate problem even for two ordinary graph structures; see
[Bousquet--Durain](https://arxiv.org/abs/2001.01463).  Our requirement is
asymmetric (proper in one graph and degree at most two in the other), so the
known simultaneous-colouring bounds do not imply the desired \(D\)-colour
statement.

## 3. Frequency two and average below two do not suffice

The natural abstract theorem suggested after Proposition 4B is false.

### Theorem 1 (uniform frequency-two obstruction)

There is a simple \(2\)-regular bipartite graph \(G\) and a family
\(\mathcal Q=\{Q_0,Q_1,Q_2,Q_3\}\) such that

* every edge of \(G\) belongs to exactly two members of \(\mathcal Q\);
* every \(Q_i\) has size three, so its average load over the two colours is
  \(3/2<2\);
* every two distinct members of \(\mathcal Q\) meet in exactly one edge; but
* every proper \(2\)-edge-colouring of \(G\) has a colour occurring three
  times in some \(Q_i\).

#### Proof

Let \(G=C_6\), and write its cyclically alternating edges as

\[
 e_1,f_1,e_2,f_2,e_3,f_3.
\]

Put

\[
\begin{aligned}
 Q_0&=\{e_1,e_2,e_3\},\\
 Q_1&=\{e_1,f_1,f_2\},\\
 Q_2&=\{e_2,f_1,f_3\},\\
 Q_3&=\{e_3,f_2,f_3\}.
\end{aligned}                                              \tag{3.1}
\]

Every displayed set has size three.  Each of the six edges occurs in exactly
two sets, and each pair of sets has a unique common edge: the incidence
pattern is the edge--vertex incidence pattern of \(K_4\).

A proper two-edge-colouring of an even cycle must alternate.  Hence
\(e_1,e_2,e_3\) all receive the same colour.  That colour has load three in
\(Q_0\), independently of the names of the two colours.  \(\square\)

This example satisfies the proposed hypotheses in their strongest natural
form: the distinguished sets are distinct, uniform and pairwise linear, and
every edge has frequency exactly two.  Thus no theorem based only on
frequency, average, and linear overlap can prove Proposition 4B.

It also shows why an alternating-cycle repair can be trapped.  The two colour
classes of \(C_6\) have only one alternating component.  The only Kempe
exchange swaps the names of the two colours on the entire cycle, leaving the
monochromatic triple in \(Q_0\).

## 4. The combined constraint system is not balanced or unimodular

One might try to regard the desired colouring as an equitable colouring of a
constraint hypergraph whose ground set is \(E(H_m)\), with constraint sets

\[
 \{\delta_{H_m}(v):v\in V(H_m)\}
 \quad\text{and}\quad
 \{\mathcal Q(P):P\in\mathcal M\}.                        \tag{4.1}
\]

Equitability on an \(H_m\)-star of size \(D\) would force one edge of each
colour.  Equitability on a \(\mathcal Q(P)\) of size \(m^2\) would force one
or two edges of each colour, which is slightly stronger than Proposition 4B
because it also forbids zero.  Thus an equitable-colouring theorem for this
hypergraph would suffice.

The standard balanced- or unimodular-hypergraph route is unavailable for a
symbolic reason already inside the \(\mathcal Q\)-rows.

### Proposition 2 (odd-cycle minor)

For every \(m\ge2\), the incidence matrix of the family
\(\{\mathcal Q(P):P\in\mathcal M\}\) contains the matrix

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},                                            \tag{4.2}
\]

whose determinant is \(2\).  In particular, the combined constraint matrix
is neither balanced nor totally unimodular.

#### Proof

Choose an \((m-1)\)-set \(C\) and three distinct elements \(a,b,c\notin C\).
Let

\[
 P_a=C\cup\{a\},\quad P_b=C\cup\{b\},\quad P_c=C\cup\{c\}.
\]

For \(x,y\in\{a,b,c\}\), let

\[
 e_{xy}=\bigl(C,C\cup\{x,y\}\bigr)\in E(H_m).
\]

Under (1.1), \(e_{xy}\) is the Johnson edge \(P_xP_y\), so it belongs to
exactly \(\mathcal Q(P_x)\) and \(\mathcal Q(P_y)\).  Restricting to the three
rows \(P_a,P_b,P_c\) and three columns \(e_{ab},e_{bc},e_{ca}\) gives (4.2).
\(\square\)

This does not disprove the desired colouring of \(H_m\).  It proves only that
the usual total-unimodularity and balanced-hypergraph explanations cannot be
invoked: the first forbidden odd cycle is present for structural reasons.

## 5. Exact effect of an alternating-cycle exchange

Let \(\chi\) be any proper \(D\)-edge-colouring of \(H_m\), and put

\[
 n_c(P)=|\chi^{-1}(c)\cap\mathcal Q(P)|.
\]

For two colours \(a,b\), their perfect matchings form a disjoint union of even
alternating cycles in \(H_m\).  Let \(C\) be one such cycle, and define

\[
 \delta_P(C)=
 |C\cap\chi^{-1}(a)\cap\mathcal Q(P)|-
 |C\cap\chi^{-1}(b)\cap\mathcal Q(P)|.                    \tag{5.1}
\]

Swapping \(a,b\) on \(C\) preserves the one-factorization and changes the two
loads by

\[
 n'_a(P)=n_a(P)-\delta_P(C),\qquad
 n'_b(P)=n_b(P)+\delta_P(C).                               \tag{5.2}
\]

For the quadratic imbalance

\[
 \Phi(\chi)=\sum_{P,c}n_c(P)^2,
\]

the exact change is

\[
 \Phi(\chi')-\Phi(\chi)
 =2\sum_P\delta_P(C)^2
  -2\sum_P\delta_P(C)\bigl(n_a(P)-n_b(P)\bigr).           \tag{5.3}
\]

There is no sign forced by frequency two.  That hypothesis says that each
individual edge contributes to two coordinates of the load vector; it does
not make an entire alternating cycle a two-sparse move.  A long cycle can
have a large, correlated vector \((\delta_P(C))_P\), and the positive square
term in (5.3) can dominate.  The \(C_6\) obstruction is the extreme case in
which the only exchange merely permutes two globally bad load vectors.

Therefore a proof by bichromatic exchanges needs a new special lemma for
\(H_m\), not merely the generic statement that two colour classes decompose
into alternating cycles.

## 6. The exact polyhedral target for \(H_m\)

Define

\[
 \mathcal P_m=\left\{
 x\in\mathbb R_{\ge0}^{E(H_m)}:
 \begin{array}{ll}
 x(\delta_{H_m}(v))=1&\text{for every }v\in V(H_m),\\
 x(\mathcal Q(P))\le2&\text{for every }P\in\mathcal M
 \end{array}
 \right\}.                                                \tag{6.1}
\]

Every integral point of \(\mathcal P_m\) is a perfect matching of \(H_m\)
whose Johnson projection has maximum degree at most two.  The uniform point

\[
 \frac1D\mathbf 1\in\mathcal P_m                           \tag{6.2}
\]

is the fractional point from Theorem 4A of `KNESER_PROJECTION.md`.

Proposition 4B is exactly the following integer-decomposition assertion:

\[
 \mathbf 1=x^{(1)}+\cdots+x^{(D)},qquad
 x^{(c)}\in\mathcal P_m\cap\{0,1\}^{E(H_m)}.              \tag{6.3}
\]

Thus either of the following would suffice:

1. prove that \(\mathcal P_m\) is integral and has the integer-decomposition
   property at the vector \(\mathbf1\); or
2. prove (6.3) directly by a symmetric decomposition theorem.

Integrality alone would not automatically imply (6.3); normality or an
explicit decomposition argument is also needed.  Proposition 2 shows why a
direct total-unimodularity proof is unavailable, but it does not rule out
integrality or normality arising from the special Boolean-lattice geometry.

## 7. What symmetry does and does not buy

The symmetric group on \([2m]\) acts transitively on the edges of \(H_m\), on
the Johnson vertices, and on all flags involved in (6.1).  Averaging any
one-factorization over this action recovers the common fractional point
\(\mathbf1/D\).  Hence all linear density tests are automatically satisfied.

This is only fractional information.  The assertion

\[
 \mathbb E\,n_c(P)=\frac{m^2}{D}<2
\]

does not imply \(n_c(P)\le2\) in any particular factorization; it does not
even exclude overload three.  The \(C_6\) example shows in
miniature that complete symmetry of the averaged load can coexist with an
unavoidable integral overload.

The useful extra structure of \(H_m\), absent from the counterexample, is
local: every \(\mathcal Q(P)\) is a canonical \(K_{m,m}\), and the restriction
of a proper \(H_m\)-colouring to it is already a proper partial colouring.
The family itself is linear,
\(\mathcal Q(P)\cap\mathcal Q(Q)=\{PQ\}\) for Johnson-adjacent \(P,Q\) and is
empty otherwise, but Theorem 1 shows that linearity alone is insufficient.
Thus a repeated colour inside \(\mathcal Q(P)\) is a matching, and an overload
is specifically a monochromatic matching of size at least three.  Any
successful proof must exploit compatibility among these overlapping
\(K_{m,m}\)'s; frequency two by itself does not encode that compatibility.

## 8. Mathematically credible next routes

The audit leaves three precise routes.

### Route A: prove normality of the symmetric polytope

Work with (6.1), not the much larger raw colouring formulation.  Seek a
Boolean-lattice uncrossing theorem showing that every minimal obstruction to
integrality can be replaced by a laminar family of Johnson-star inequalities.
The triangle (4.2) means that ordinary matrix uncrossing is insufficient, so
the proof would have to use the perfect-matching equalities essentially.

### Route B: a special alternating-cycle descent theorem

Among all one-factorizations of \(H_m\), minimize lexicographically

\[
 \left(\max_{P,c}n_c(P),
       \#\{(P,c):n_c(P)=\max n\},
       \sum_{P,c}n_c(P)^2\right).                          \tag{8.1}
\]

To prove Proposition 4B by exchanges, it is enough to show that any minimizer
with a load at least three has two colours and one alternating component for
which (8.1) decreases.  Formula (5.3) is the exact accounting identity.  The
missing lemma must use the specific Johnson triangles and canonical
\(K_{m,m}\)'s to find such a component; no frequency-two version can hold by
Theorem 1.

### Route C: couple the two known equitable colourings

One has a perfect one-factorization in \(H_m\) and, independently, a locally
\(1/2\)-equitable colouring in the Johnson graph.  A coupling theorem that
preserves the first set of margins while successively imposing the second
would prove a statement stronger than Proposition 4B: every projected colour
class would have degree one or two at every middle vertex.  Combined with
\(|M_c|=N\), each colour would then have exactly \(2K\) degree-one vertices
and no isolated vertices.  Only projected cycles would remain to be removed.

## 9. Verdict

The general equitable-factorization principle is disproved by Theorem 1.
De Werra's theorem cannot be cited for Proposition 4B: it balances graph
stars, whereas the proof needs one colouring simultaneously balanced in two
different graph structures.  The standard balanced/unimodular extension is
also blocked by the explicit Johnson triangle (4.2).

For the symmetric Boolean-lattice graph \(H_m\), no symbolic impossibility is
found.  The strongest clean formulation is (6.3): prove that the all-ones
edge vector decomposes into \(D\) integral points of the matching-plus-
Johnson-capacity polytope \(\mathcal P_m\).  That is a genuine new theorem,
not a corollary of ordinary equitable edge colouring.
