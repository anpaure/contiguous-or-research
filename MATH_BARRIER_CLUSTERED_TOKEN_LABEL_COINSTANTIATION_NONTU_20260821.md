# A minimal non-TU face in token--label coinstantiation

**Status (2026-08-21).**  Every assertion below is proved.  The first joint
relaxation which assigns physical extension slots to both middle labels and
upper labels is already a three-partite matching polytope.  Its incidence
matrix contains a `3 by 3` minor of determinant `-2`, and a restricted
three-column face has fractional value `3/2` but integral value `1`.

This is **not** a no-go theorem for the full dense order-bank problem.  Extra
columns in the full orbit hypergraph may support a near-perfect matching.
The result only proves that total unimodularity, ordinary network-flow
integrality, or bare two-matroid intersection does not follow from the three
capacity families alone.

## 1. The tokenwise orbit relaxation

Fix disjoint `11`-sets

\[
 A=\{a_1,\ldots,a_{11}\},\qquad
 B=\{b_1,\ldots,b_{11}\}.
\]

Take upper offset `q=1`, payload split `r=5`, and the next-`A` phase type
`z=1`.  A labelled flag of this type is a pair

\[
 U\subset V,qquad
 |U\cap A|=5,quad |U\cap B|=6,quad
 |V\cap A|=|V\cap B|=6.                              \tag{1.1}
\]

The group `Sym(A)\times Sym(B)` is transitive on these flags.  Thus any one
physical factor-order occurrence slot of type `(r,q,z)=(5,1,1)` can be sent
to any flag (1.1) if its labels are allowed to be conjugated independently.

The **tokenwise orbit relaxation** has a variable `x_(o,U,V)` for every
physical slot `o` and every individually realizable flag `(U,V)`.  Its three
unit-capacity row families are

\[
 \sum_{U,V}x_{o,U,V}\le1,\qquad
 \sum_{o,V}x_{o,U,V}\le1,\qquad
 \sum_{o,U}x_{o,U,V}\le1.                            \tag{1.2}
\]

They enforce, respectively, one assignment per physical slot, one use per
middle target, and one use per upper target.  This relaxation deliberately
drops the requirement that different slots use one common conjugation or
belong to compatible tight-cycle factors.  Every column has one `1` in each
of the three row families.

## 2. The determinant-two minor

Put

\[
 U_1=\{a_1,\ldots,a_5,b_1,\ldots,b_6\},
\]

\[
 V_2=U_1\cup\{a_6\},\qquad
 U_2=V_2\setminus\{a_1\},\qquad
 V_1=U_1\cup\{a_7\}.                                \tag{2.1}
\]

Then `(U_1,V_1)`, `(U_2,V_2)`, and `(U_1,V_2)` are all flags of type
(1.1).  For two distinct same-type physical slots `o_1,o_2`, consider the
three allowed columns

\[
 e_1=(o_1,U_1,V_1),\qquad
 e_2=(o_1,U_2,V_2),\qquad
 e_3=(o_2,U_1,V_2).                                  \tag{2.2}
\]

On the three rows `o_1,U_1,V_2`, their incidence matrix is

\[
 \begin{pmatrix}
  1&1&0\\
  1&0&1\\
  0&1&1
 \end{pmatrix},
 \qquad \det=-2.                                     \tag{2.3}
\]

### Theorem 2.1

The token--middle-label--upper-label incidence matrix is not totally
unimodular.  On the restricted subinstance (2.2), the fractional vector

\[
 x_{e_1}=x_{e_2}=x_{e_3}={1\over2}                   \tag{2.4}
\]

is feasible and has value `3/2`, whereas every integral feasible set has
size at most one.

#### Proof

Equation (2.3) proves failure of total unimodularity.  In (2.4), the rows
`o_1,U_1,V_2` have load one and the remaining used rows `o_2,U_2,V_1` have
load one half, so all constraints (1.2) hold.  Any two columns in (2.2)
conflict: `e_1,e_2` share `o_1`, `e_1,e_3` share `U_1`, and `e_2,e_3` share
`V_2`.  Hence the restricted integral optimum is one.  \(\square\)

## 3. Exact scope

The three row families in (1.2) are three partition matroids.  Their
intersection has no general two-matroid or bipartite-flow integrality, and
the determinant-two face is the smallest possible witness.

The witness does not assert that the full orbit hypergraph has matching
number one or even a positive-density deficit.  It also does not embed a
failure inside one fixed tight-cycle factor: the tokenwise relaxation allows
each column to use its own conjugation.  A dense-system proof may still work
by exploiting the many additional orbit columns, augmenting switches, or a
global common-order structure.  What is ruled out is the inference

\[
 \text{fractional slot/label balance}
 \quad\Longrightarrow\quad
 \text{integral coinstantiation by total unimodularity}.
\]
