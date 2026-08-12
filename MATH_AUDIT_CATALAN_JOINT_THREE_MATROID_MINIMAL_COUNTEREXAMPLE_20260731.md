# Minimal three-row obstruction for joint Catalan gluing catalogues

Date: 2026-07-31  
Status: exact abstract-catalogue counterexample and exhaustive minimality audit;
not a claim that the three abstract labels are jointly realizable by one
physical Catalan collar

## 1. The catalogue

Let the selectable gluing labels be

\[
                         T=\{a,b,c\},
\]

and require two labels.  Each label carries one factor-component edge, one
effective gap-attachment edge and one boundary-linkage source signature.

The component graph has

\[
 a=C_0C_1,\qquad b=C_1C_2,\qquad c=C_1C_2.          \tag{1.1}
\]

Thus `b,c` are parallel in its graphic matroid.  The contracted gap graph has

\[
 a=G_0G_1,\qquad b=G_1G_2,\qquad c=G_0G_1,          \tag{1.2}
\]

so `a,c` are parallel in the gap graphic matroid.  Finally take the
width-two directed-linkage network with sinks `s,t` and direct arcs

\[
                         a\to s,\qquad b\to s,
                         \qquad c\to t.              \tag{1.3}
\]

A set of labels is linkage-feasible when its source vertices admit
vertex-disjoint paths to distinct sinks.  This is a gammoid restriction (and
has the usual strict-gammoid realization after vertex splitting).  Its only
parallel pair is `a,b`.

Every singleton is admissible in all three rows.  Hence this is a
nondegenerate local catalogue: the obstruction is not obtained by declaring
one label a loop.

## 2. Exact cyclic obstruction

### Theorem 2.1

Each marginal row has rank two, and every pair of rows has a common
two-label basis, but the product of all three rows has rank one.

More precisely, the rank-two bases are

\[
\begin{array}{c|c}
\text{row}&\text{bases}\\ \hline
M_{\rm comp}&ab,ac\\
M_{\rm gap}&ab,bc\\
M_{\rm link}&ac,bc.
\end{array}                                           \tag{2.1}
\]

Consequently the three pairwise products have the unique bases

\[
 M_{\rm comp}\cap M_{\rm gap}:ab,\qquad
 M_{\rm comp}\cap M_{\rm link}:ac,\qquad
 M_{\rm gap}\cap M_{\rm link}:bc,                    \tag{2.2}
\]

while no pair is independent in all three.

#### Proof

In (1.1), exactly `bc` is a two-edge graphic circuit.  In (1.2), exactly
`ac` is a two-edge graphic circuit.  In (1.3), exactly `ab` competes for one
sink.  This gives (2.1), hence (2.2), and the three forbidden pairs exhaust
all two-subsets of `T`.  All singletons survive.  Therefore the joint rank is
exactly one.  \(\square\)

This is the smallest Borromean correlation failure of the three coordinates:
deleting any row restores a rank-two solution, but the three together do not
admit the required component-tree size.

The three rank inequalities already display the integral obstruction:

\[
 x_b+x_c\le1,\qquad x_a+x_c\le1,\qquad x_a+x_b\le1. \tag{2.3}
\]

Their coefficient matrix has determinant `2`.  The half-vector
\(x_a=x_b=x_c=1/2\) is feasible with value \(3/2\), whereas the largest
integral joint set has value `1`.  Thus adjoining the active gammoid row to
the two graphic rows destroys the integral two-matroid face even though the
gap catalogue has exactly one effective edge per label.

## 3. Sharp minimality under local admissibility

### Proposition 3.1

Among loopless catalogue rows, three labels are the minimum possible ground
size for the following property:

1. three matroids are individually feasible at target rank `r`;
2. every two of them have a common independent `r`-set; and
3. all three have no common independent `r`-set.

The minimum parameters are `|T|=3`, `r=2`, attained by (1.1)--(1.3).

#### Proof

For `|T|=1`, looplessness gives a common singleton.  For `|T|=2`, target
rank one again has either singleton available in every row.  At target rank
two the only candidate is all of `T`; individual rank-two feasibility makes
that set independent in every row.  Hence failure is impossible below three
labels.  Theorem 2.1 supplies the three-label example.  \(\square\)

The companion audit additionally enumerates every labelled matroid on one,
two and three elements.  There are respectively `2,5,16`, of which `1,2,6`
are loopless.  It finds no earlier failure and finds exactly six ordered
triples at the first parameters, the six permutations of the cyclic
parallel-pair pattern.

The loopless condition is essential to the stated minimality.  Without it,
different rows can reject different labels by loops, which is not a genuine
locally admissible gluing catalogue.

## 4. Consequence for the polynomial face

If any one of the three rows is automatic or implied by another, the
remaining problem is ordinary two-matroid intersection: graphic--graphic,
graphic--gammoid, or gap-graphic--gammoid.  In particular, private sockets
make the gap row automatic, while a supplied fixed linkage makes the gammoid
row automatic.

Theorem 2.1 proves that the face cannot be enlarged merely by retaining all
three oracle rows and checking every marginal or every pairwise product.
Even the strongest one-effective-gap-edge catalogue can contain the cyclic
parallel-pair obstruction.  A positive all-dimension theorem must therefore
provide additional alignment--for example a private-socket row, one fixed
linkage signature, or a structural implication between two rows--or carry
their exact product in a bounded-width dynamic state.

This abstract fixture does **not** prove that the obstruction occurs in a
specific middle-levels or Catalan collar.  It identifies the exact
matroid-theoretic pattern that a physical catalogue theorem must exclude.

## 5. Independent exchange warning

Even before the third row becomes active, the family of sets simultaneously
independent in two matroids need not itself be a matroid.  On the same three
labels, let the component row make `a,b` parallel, let the gap row make `a,c`
parallel, and let the linkage gammoid be free through rank two.  Then

\[
                         I=\{a\},\qquad J=\{b,c\}
\]

are jointly independent, but neither `I+b` nor `I+c` is.  Thus exchange
fails.  This does not harm polynomial two-matroid intersection; it only
forbids replacing the product by one ordinary matroid oracle.

## 6. Reproducer

Run

```text
python3 scratch/audit_catalan_joint_three_matroid_minimal_counterexample_20260731.py
```

It reconstructs both graphic rows and the directed-linkage gammoid, checks
all subsets, verifies (2.1)--(2.3), audits the exchange fixture, and performs
the exhaustive labelled-matroid minimality census for `|T|<=3`.

