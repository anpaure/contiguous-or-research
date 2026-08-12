# Pascal-sector determinants and the two-copy cycle obstruction

Date: 2026-07-31  
Status: exact sector/constant-term identities, an exact triangular
orientation gauge, an exact deletion-contraction boundary state, and a
general obstruction to the naive \(\mathcal E_{m-1}^2\) induction. No
all-\(m\) Catalan Linear Matching existence claim is made.

## 0. Verdict

Splitting the noncancelling enumerator at one distinguished coordinate
produces four literal Pascal sectors. Outer matching makes their sizes
rigid:

\[
                  P,\quad P,\quad K,
 \qquad K=\operatorname{Cat}_m.
\]

If every cross-rail atom is oriented in the same direction, the directed
forest determinant becomes block triangular. This is a genuine
simplification, and the resulting class is nonempty at \(m=2,3\).
However it is not a harmless orientation gauge: it is equivalent to
requiring exactly one cross edge in every physical path component. None of
the 1,728 decorations of the frozen positive repaired \(ML(7)\) cycle has
this property.

More decisively, distinguishing two coordinates does **not** expose two
copies of the previous Catalan enumerator which can simply be multiplied
and completed. If both embedded \(\mathcal E_{m-1}\) copies are selected,
outer-palette arithmetic forces \(\operatorname{Cat}_m\) cross edges
between their two middle rails. The induced subgraph already has at least
as many edges as vertices, hence contains a cycle. Thus the most direct
Pascal product contribution is identically zero in every dimension.

Any induction must use boundary-deficient previous objects and carry
endpoint/reachability state; scalar nonvanishing of \(\mathcal E_{m-1}\)
is insufficient.

## 1. The one-coordinate four-sector split

Let

\[
 \Omega=\Omega_0\sqcup\{\infty\},\qquad|\Omega_0|=2m-1,
\]

and put

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P=\operatorname{Cat}_m.                       \tag{1.1}
\]

Split the middle layer into rails

\[
 \mathcal X_0=\binom{\Omega_0}{m},\qquad
 \mathcal X_1=\infty+\binom{\Omega_0}{m-1},
 \qquad |\mathcal X_0|=|\mathcal X_1|=Q.            \tag{1.2}
\]

An ordered atom \(q=(L,U,T,H)\) lies in exactly one of four sectors:

| sector | \(L\) | \(U\) | tail | head |
|---|---:|---:|---:|---:|
| \(\mathsf A\) | \(0\) | \(0\) | \(0\) | \(0\) |
| \(\mathsf B\) | \(1\) | \(1\) | \(1\) | \(1\) |
| \(\mathsf D\) | \(0\) | \(1\) | \(1\) | \(0\) |
| \(\mathsf R\) | \(0\) | \(1\) | \(0\) | \(1\) |

Here \(0/1\) records absence/presence of \(\infty\). There is no sector
with \(L\) containing \(\infty\) and \(U\) avoiding it.

### Theorem 1.1 (forced Pascal multidegree)

Every ordered Catalan linear matching \(F\) satisfies

\[
 |F\cap\mathsf A|=P,\qquad
 |F\cap\mathsf B|=P,\qquad
 |F\cap(\mathsf D\cup\mathsf R)|=K.                 \tag{1.3}
\]

#### Proof

There are \(P\) upper colours avoiding \(\infty\), and only
\(\mathsf A\)-atoms can use them, so all \(P\) are used by
\(\mathsf A\). Dually, the \(P\) lower colours containing \(\infty\)
can only be used by \(\mathsf B\). The remaining \(Q-P=K\) lower colours
avoiding \(\infty\) and upper colours containing \(\infty\) are paired by
cross atoms. \(\square\)

If sector variables \(a,b,d,r\) are inserted into the exact positive
enumerator from the companion determinant theorem, then

\[
 \mathcal E_m(a,b,d,r;z)
 =a^P b^P\sum_{j=0}^{K}d^j r^{K-j}\mathcal E_{m,j}(z), \tag{1.4}
\]

where \(\mathcal E_{m,j}\) counts solutions having exactly \(j\)
\(\mathsf D\)-atoms. Equation (1.4) is an exact sector decomposition, not
an asymptotic balance statement.

## 2. Exact constant-term and block-determinant formulas

Recall the four determinant polynomials

\[
 p_\lambda,\quad p_\upsilon,\quad p_\eta,\quad p_{\rm df}
\]

from the noncancelling enumerator theorem. Coefficientwise Hadamard
intersection has the literal constant-term form

\[
\begin{split}
 \mathcal E_m(z)
 =\Bigl(&\operatorname{CT}_{x,y,w}\,
 p_\lambda(zxyw)\,
 p_\upsilon(x^{-1})\,
 p_\eta(y^{-1})\,
 p_{\rm df}(w^{-1})\Bigr)_{[N]}.                   \tag{2.1}
\end{split}
\]

All products and inverses in (2.1) are coordinatewise over the atom
variables. A monomial survives the constant term exactly when the same
atom set was chosen in all four factors.

Now order the physical rows as \(\mathcal X_1,\mathcal X_0\). For
same-rail sectors put

\[
 L_{\mathsf B}=C_{\mathsf B}Z_{\mathsf B}T_{\mathsf B}^{*},
 \qquad
 L_{\mathsf A}=C_{\mathsf A}Z_{\mathsf A}T_{\mathsf A}^{*}. \tag{2.2}
\]

For a down-cross atom \(q\in\mathsf D\), put its positive tail diagonal
entry into \(D_{\downarrow}\) and its head-tail incidence into
\(R_{\downarrow}\). Define \(D_{\uparrow},R_{\uparrow}\) analogously for
\(\mathsf R\). Direct substitution into
\(p_{\rm df}=\det(I+CZT^{*})\) gives

\[
 p_{\rm df}=
 \det\begin{pmatrix}
 I+L_{\mathsf B}+D_{\downarrow}&-R_{\uparrow}\\
 -R_{\downarrow}&I+L_{\mathsf A}+D_{\uparrow}
 \end{pmatrix}.                                    \tag{2.3}
\]

### Corollary 2.1 (one-way triangularization)

If all up-cross variables are set to zero, then

\[
 p_{\rm df}\big|_{\mathsf R=0}
 =
 \det(I+L_{\mathsf B}+D_{\downarrow})\,
 \det(I+L_{\mathsf A}).                             \tag{2.4}
\]

If all down-cross variables are zero, the dual factorization holds:

\[
 p_{\rm df}\big|_{\mathsf D=0}
 =
 \det(I+L_{\mathsf B})\,
 \det(I+L_{\mathsf A}+D_{\uparrow}).                \tag{2.5}
\]

Thus the directed-cycle filter is railwise under a one-way gauge. The
three partition Hadamard factors in (2.1) still correlate the two rail
forests and their cross endpoints; triangularity does not by itself prove
nonvanishing.

## 3. What the orientation gauge really requires

### Theorem 3.1 (one-way gauge criterion)

For an undirected Catalan linear matching \(F\), the following are
equivalent.

1. Its path components can be coherently oriented so that every cross edge
   points from \(\mathcal X_1\) to \(\mathcal X_0\).
2. Every physical path component of \(F\) contains exactly one cross edge.

#### Proof

A coherent orientation on a path which crosses from rail \(1\) to rail
\(0\) cannot later cross in the same direction again: returning to rail
\(1\) would require an oppositely oriented cross edge. Thus an all-down
orientation gives at most one cross edge per path.

Every Catalan linear matching has exactly

\[
 |\mathcal X|-|F|=K
\]

path components, and Theorem 1.1 gives exactly \(K\) cross edges. Hence
at most one means exactly one in every component.

Conversely, if every path contains one cross edge, orient that path so its
cross edge points from rail \(1\) to rail \(0\). The orientations are
coherent and all cross edges point down. \(\square\)

The criterion is nonvacuous but restrictive. Exact finite census gives:

* at \(m=2\), the 24 ordered solutions split as 6 all-down, 6 all-up, and
  12 mixed;
* at \(m=3\), 31,464 of the 458,544 undirected linear matchings have one
  cross edge in each of their five components; each supplies one all-down
  and one all-up orientation;
* on the fixed repaired positive \(ML(7)\) cycle at \(m=4\), none of its
  1,728 Catalan decorations has one cross edge per component. The minimum,
  over those decorations, of the largest cross load of a component is two.

The last statement is scoped to that positive middle-levels fibre. It does
not prove that the one-way class is empty at \(m=4\).

## 4. Two embedded previous enumerators force a cycle

Distinguish two coordinates \(x,y\), and write

\[
 \Omega=\Omega'\sqcup\{x,y\},\qquad|\Omega'|=2m-2.
\]

Atoms in which \(x\) is present in all four sets and \(y\) is absent from
all four form a literal copy of the parameter-\((m-1)\) ordered atom
catalogue after deleting \(x\). Denote it by
\(\mathcal Q_{m-1}^{x\bar y}\). There is a second copy
\(\mathcal Q_{m-1}^{y\bar x}\).

### Theorem 4.1 (two-copy cycle no-go)

For every \(m\ge3\), no Catalan linear matching at parameter \(m\) contains
both a complete Catalan linear matching supported on
\(\mathcal Q_{m-1}^{x\bar y}\) and one supported on
\(\mathcal Q_{m-1}^{y\bar x}\).

The formal \(m=2\) boundary version has the same cycle obstruction.

#### Proof

Put

\[
 K'=\operatorname{Cat}_{m-1},\qquad
 M'=\binom{2m-2}{m-1}=mK',\qquad
 N'=\binom{2m-2}{m-2}=(m-1)K'.                    \tag{4.1}
\]

The two embedded matchings contribute \(N'\) edges on each of the two
physical middle rails

\[
 x+\binom{\Omega'}{m-1},
 \qquad
 y+\binom{\Omega'}{m-1},                            \tag{4.2}
\]

each rail having \(M'\) vertices.

The two copies saturate every lower and upper outer colour containing
exactly one of \(x,y\). Among the remaining colours, the counts are

\[
\begin{array}{c|cc}
 &\text{lower rank }m-1&\text{upper rank }m+1\\ \hline
\text{neither }x,y&M'&B\\
\text{both }x,y&B&M',
\end{array}
\qquad
 B=\binom{2m-2}{m-3}.                               \tag{4.3}
\]

Every upper colour avoiding both distinguished points must be matched from
the lower-neither sector, consuming \(B\) such lowers. Every lower colour
containing both must be matched into the upper-both sector, consuming
\(B\) such uppers. Therefore exactly

\[
 M'-B
 =\binom{2m-2}{m-1}-\binom{2m-2}{m-3}
 =\operatorname{Cat}_m=K                            \tag{4.4}
\]

remaining atoms go from lower-neither to upper-both.

For such an atom, containment and equal residual ranks force

\[
                         U=L+x+y.                    \tag{4.5}
\]

Its physical Johnson edge is \((L+x)(L+y)\), so all \(K\) forced atoms lie
between the two rails in (4.2). The physical graph induced by those rails
therefore has

\[
 2M'\text{ vertices},\qquad 2N'+K\text{ edges}.      \tag{4.6}
\]

But

\[
 (2N'+K)-2M'=K-2K'\ge0,                             \tag{4.7}
\]

with equality only at the formal \(m=2\) boundary and strict inequality
for \(m\ge3\). A forest on a nonempty set of \(2M'\) vertices has at most
\(2M'-1\) edges. Hence the induced graph contains a cycle, contradicting
linearity. \(\square\)

### Corollary 4.2 (no scalar square recursion)

No positive term of \(\mathcal E_m\) contains the product of one complete
monomial from each of the two canonical embedded copies of
\(\mathcal E_{m-1}\). In particular, the Pascal split cannot prove
\(\mathcal E_m\ne0\) by multiplying two arbitrary previous solutions and
filling only the remaining outer colours.

Within this fixed two-copy completion, if its \(K\) forced cross atoms are
retained, at least

\[
                       K-2K'+1                      \tag{4.8}
\]

internal edges must be removed before the induced two-rail edge count even
reaches the forest bound. A more general recursion may simultaneously
change the outer completion and the number of cross atoms; (4.8) is not a
lower bound for every possible Pascal braid. It explains exactly why the
literal two-full-copy product cannot be repaired by one orientation flip.

## 5. Exact deletion-contraction carries reachability state

For an atom \(q=(L,U,T,H)\), the tautological multiaffine identity is

\[
 \mathcal E_m=
 \mathcal E_m\big|_{z_q=0}
 +z_q\,\partial_{z_q}\mathcal E_m.                  \tag{5.1}
\]

The contraction term has an exact combinatorial interpretation. Delete
every residual atom sharing lower colour \(L\), upper colour \(U\), tail
\(T\), or head \(H\). Then \(\partial_{z_q}\mathcal E_m\) enumerates
residual selections satisfying all remaining palettes and:

1. the residual directed graph is acyclic; and
2. it contains no directed path from \(H\) to \(T\).

The second condition is necessary and sufficient because adding
\(q:T\to H\) creates a directed cycle exactly when the residual graph
already contains \(H\leadsto T\).

Therefore ordinary deletion-contraction is not closed on the scalar family
\(\{\mathcal E_m\}\). It is closed only after adjoining a two-terminal
reachability state. Iterating a Pascal recursion necessarily grows this
into the endpoint/linkage state already visible in the constructive trace
work.

In repair-and-glue language, the contraction state is the smallest socket
state: a repair macro is legal only if it does not create the forbidden
\(H\leadsto T\) connection, while gluing two macros composes their boundary
reachability relations. The common-core augmenting-linkage and transparent
gluing states in the constructive lane are therefore not auxiliary solver
metadata; they are forced already by exact algebraic contraction.

## 6. Consequence for the algebraic route

The Pascal split does yield a useful exact algebra:

* sector degrees are forced;
* the coefficientwise product has a literal constant-term formula;
* one-way cross orientation triangularizes the directed determinant;
* atom contraction has a precise two-terminal state.

What it does not yield is a scalar Catalan recurrence. Two full previous
enumerators cannot coexist, and the familiar positive \(m=4\) trace fibre
does not lie in the triangular gauge. This does **not** obstruct every
Pascal recursion. It says that a viable one must use boundary-deficient rail
enumerators carrying endpoint, omitted-palette, and reachability data. That
is a finite-state repair-and-glue theorem, not a formal consequence of
\(\mathcal E_{m-1}\ne0\).

Run

~~~text
python3 scratch/audit_catalan_pascal_sector_determinant_20260731.py
~~~

for the finite calibrations and binomial identity replay.
