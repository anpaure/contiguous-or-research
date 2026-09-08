# Every direct suffix-compatible `D_3`--Tamari overlap collides on the owner shore

**Date:** 2026-08-06  
**Method:** pure mathematics; exhaustive cyclic/reflection alignment of the
four suffix-stable `D_3` companion edges with the two Tamari shores, followed
by literal rank-four window comparison  
**Status:** unconditional no-go for the direct seven-row adapter which
identifies the Tamari companion pair `A,L` with one persistent `D_3` edge
and retains the other three `D_3` rows.  It does **not** exclude replacing a
colliding `D_3` row, a non-base-respecting high-dimensional identification,
or a larger helper trade.

## 1. The proposed overlap

Suspend the anchored `D_3` pentagon once, from semilength three to
semilength four, and denote the fresh deletion and insertion labels by
`u,v`.  Its suffix-stable companion edges are

\[
                         12^-,\quad54^-,\quad14^+,\quad32^+.
\tag{1.1}
\]

The port-restored Tamari packet has four rows `A,L,C,D`; on either shore
`-` or `*`, its unique companion edge is `A--L`.  The direct overlap asks
to identify `A,L` with the two rows of one edge in (1.1), transport the
forced helper rows `C,D` by the same coordinate relabelling, and retain the
other three rows of the `D_3` factor.  Since two rows are identified, the
putative partial factor has seven named rows.

A necessary condition is that every rank-four owner occur at most once.
The theorem below shows that this already fails before any q1 completion
is considered.

## 2. One explicit alignment

For the negative edge `12^-`, use the common-tail normal form

\[
\begin{aligned}
 r_1&=(4,5,v,\infty,2,3,1,u,6),\\
 r_2&=(5,3,v,\infty,4,2,1,u,6).
\end{aligned}
\tag{2.1}
\]

Identify `L^-` with `r_1` and `A^-` with `r_2`.  The forced coordinate map
from the Tamari labels to (2.1) is

\[
\begin{array}{c|ccccccccc}
x&1&2&3&4&5&6&7&8&\infty\\ \hline
\phi(x)&6&u&\infty&3&1&5&v&4&2.
\end{array}
\tag{2.2}
\]

Applying the same map to the two helper rows gives

\[
\begin{aligned}
 C&=(1,v,u,6,3,4,5,\infty,2),\\
 D&=(u,\infty,6,v,3,4,5,1,2).
\end{aligned}
\tag{2.3}
\]

The helper `C` and the untouched negative `D_3` row 3 both contain the
cyclic rank-four window

\[
                              \{3,4,6,u\}.
\tag{2.4}
\]

Thus even this first seven-row overlap is not a simple owner partial
factor.

## 3. Exhaustion of the proof-relevant symmetries

Both a persistent `D_3` edge and the Tamari edge `A--L` are native
inverse-pair normal forms.  Once their two ordered rows are identified,
the common `X,Y` blocks and the four active positions determine the
coordinate map.  Up to simultaneous cyclic rotation, there are exactly
two maps: the two choices induced by reversing the native alignment (or,
equivalently, exchanging the two oriented identifications of the edge).

There are four choices in (1.1), two Tamari shores, and two such
identifications.  The following table gives one literal collision for all
sixteen cases.  An entry `C:3; S` means that the forced Tamari helper `C`
and the untouched `D_3` row 3 both contain the rank-four owner `S`.

\[
\begin{array}{c|c|c|c}
\text{D3 edge}&\text{Tamari shore}&\text{alignment 0}&\text{alignment 1}\\ \hline
12^-&-&C:3;\{3,4,6,u\}&C:5;\{1,3,4,u\}\\
12^-&*&C:4;\{1,3,\infty,v\}&C:3;\{2,6,\infty,v\}\\
54^-&-&D:3;\{1,2,5,u\}&C:1;\{4,5,\infty,v\}\\
54^-&*&D:1;\{2,5,\infty,v\}&C:2;\{1,2,6,u\}\\
14^+&-&C:5;\{2,5,6,u\}&C:3;\{1,2,5,u\}\\
14^+&*&C:2;\{1,2,\infty,v\}&C:2;\{5,6,\infty,v\}\\
32^+&-&D:5;\{1,3,4,u\}&C:1;\{4,5,\infty,v\}\\
32^+&*&D:1;\{3,4,\infty,v\}&C:4;\{1,3,6,u\}.
\end{array}
\tag{3.1}
\]

Every row named after the colon is outside the identified `D_3` edge, so
it is one of the three rows which the direct adapter proposes to retain.

### Theorem 3.1 (direct overlap no-go)

No suffix-stable `D_3` edge can be identified with the Tamari edge `A--L`,
on either Tamari shore and in either cyclic/reflection alignment, while
retaining all three other `D_3` rows in a simple owner factor.

#### Proof

The normal-form rigidity above makes the sixteen entries of (3.1)
exhaustive.  Each displayed set is a cyclic length-four window of both a
forced helper and an untouched `D_3` row.  Hence the corresponding owner
has multiplicity at least two, contradicting owner capacity one.
\(\square\)

## 4. Common suspension does not repair the collision

Under a further common-tail tensor, a base owner `S` at a fixed tail state
is carried to `S union T`, where `T` is the same labelled tail contribution
for every row in the aligned cylinder.  Therefore

\[
                         S=S'\quad\Longrightarrow\quad
                         S\cup T=S'\cup T.
\tag{4.1}
\]

Every collision in (3.1) consequently persists in the corresponding
base/tail owner shore in every later common suffix dimension.

### Corollary 4.1

Merely tensoring a direct seven-row `D_3`--Tamari overlap cannot produce a
protected q1 completion in higher dimension: it already fails to be a
simple owner partial factor.

## 5. Exact scope and next admissible adapters

The no-go is deliberately narrow.  It rules out

\[
 \boxed{
 \text{identify }A,L\text{ with one persistent D3 edge}
 +\text{ retain all other D3 rows}
 +\text{ add the forced }C,D.}
\tag{5.1}
\]

It does not rule out:

1. deleting or rerouting the particular untouched `D_3` row named in
   (3.1);
2. absorbing the helper collision inside a larger exact trade;
3. identifying a genuinely non-base high-dimensional slot whose common
   blocks are not the suspended base blocks; or
4. using the Tamari slot transport serially rather than as a simultaneous
   row overlap.

Thus the Tamari packet remains a candidate **dynamic slot transporter**,
but not a plug-in four-row helper for the unchanged suspended pentagon.
