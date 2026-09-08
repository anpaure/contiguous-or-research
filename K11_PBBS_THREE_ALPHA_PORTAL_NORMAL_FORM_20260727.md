# A normal form for three-alpha PBBS portal candidates

Date: 2026-07-27

Method: cancellation-graph and Johnson-geometry analysis; no computational
search.

## 0. Outcome

After the one- and two-alpha obstructions, every support-minimal
three-alpha portal candidate has a small core-overlap graph:

- a path of three rank-four cores in \(J(11,4)\);
- a Johnson-star triangle;
- a Johnson-top triangle.

Moreover, the simplest path realization—a monotone sequence of three
ordinary executable alpha switches—is impossible for the alternating PBBS
component. Therefore any genuine three-alpha portal must use either

- a fork in which two alphas separately supply two defects of the portal
  alpha;
- a cyclic cancellation pattern;
- or a double cancellation at one shared lower row.

The fork case is realized explicitly in
K11_PBBS_EXPLICIT_THREE_ALPHA_FORK_PORTAL_20260727.md. Thus this normal form
both removes the ordinary sequential-repair architecture and identifies the
geometry of the sharp construction.

## 1. Cancellation graph

Let \(A_0,A_1,A_2\) be three signed alpha vectors. Form a directed
cancellation graph \(\Gamma\) on \(\{0,1,2\}\): an edge \(i\to j\), labelled
by a diamond \(d\), means that \(d\) occurs negatively in \(A_i\) and
positively in \(A_j\), so it cancels in the total signed sum.

For a support-minimal portal sum:

1. the component of \(\Gamma\) containing the alpha with the surviving
   alternating negative chord contains all three vertices; otherwise that
   component would be a one- or two-alpha portal, already excluded;
2. hence the underlying graph of \(\Gamma\) is a path or a triangle;
3. a cancellation between alphas with distinct cores \(R_i,R_j\) occurs on
   a common lower row
   \[
   Y=R_i+a=R_j+b,
   \]
   so \(|R_i\cap R_j|=3\): the two cores are adjacent in \(J(11,4)\);
4. if the same pair of alphas cancels diamonds on two distinct lower rows,
   then \(R_i=R_j\), because the intersection of those two rows recovers the
   core.

Thus every genuinely changing-core three-alpha candidate has a connected
core graph in \(J(11,4)\), and every pair of distinct cores shares at most
one cancellation row.

## 2. The two Johnson-triangle geometries

Three pairwise adjacent four-sets have exactly two possible forms.

### Star type

There is a common three-set \(K\) and distinct \(a,b,c\) such that

\[
R_0=K+a,\qquad R_1=K+b,\qquad R_2=K+c.
\tag{2.1}
\]

The three pairwise cancellation rows are distinct:

\[
K+a+b,\qquad K+b+c,\qquad K+c+a.
\tag{2.2}
\]

### Top type

There is a common five-set \(Y\) and distinct \(a,b,c\in Y\) such that

\[
R_0=Y-a,\qquad R_1=Y-b,\qquad R_2=Y-c.
\tag{2.3}
\]

All three pairs meet on the same lower row \(Y\).

These are the standard star/top cliques of the Johnson graph. Consequently
a cyclic three-alpha cancellation has only two core geometries: three
different shared rows as in (2.2), or one common shared row as in (2.3).

## 3. Path and fork normal forms

Suppose the core graph is a path

\[
R_0-R_1-R_2.
\]

At a leaf, every unavailable negative diamond must lie on its unique
cancellation row. In particular, if \(A_0\) contains the surviving
alternating chord, then \(A_0\) must be one of the complete one-missing
nearly-alpha families classified in
K11_PBBS_CHANGING_CORE_TWO_ALPHA_CLASSIFICATION_20260727.md.

There are then two path mechanisms.

### Monotone chain

\(A_1\) inserts the unique missing diamond of \(A_0\), deletes the current
PBBS chord at that row, and has exactly one new missing negative diamond.
Then \(A_2\), executable in the preceding state, inserts that new diamond.
This is an ordinary three-step availability chain.

### Nonmonotone path

At some shared row, both opposite diamonds cancel, or the middle alpha has
two defects whose cancellations use different incidence patterns. This is
not representable as a sequence in which each next alpha is already
executable before the previous one.

If the alternating alpha begins with two missing negative diamonds instead
of one, its two neighbours must supply them separately. This is the
**fork** normal form. Its core graph need not contain the edge
\(R_1R_2\).

## 4. The monotone three-alpha chain is impossible

By reflection, consider the spare-\(0\) one-missing family. For
\(x\in\{3,5,7,9\}\), put

\[
R_x=Z-x,\qquad Y_x=R_x+10.
\]

The portal alpha \(A_0\) is missing

\[
d_x=(Y_x,\{0,x-1\}).
\]

If \(A_1\) inserts \(d_x\) while deleting the current PBBS chord at \(Y_x\),
write its core as \(S=Y_x-y\), \(y\in R_x\). The two remaining negative
conditions are

\[
\epsilon_S(v_x)=\{0,x-1\},
\qquad
\epsilon_S(0)=\{x-1,y\},
\tag{4.1}
\]

where \(v_x=x+1\) for \(x=3,5,7\), and \(v_9=9\).

The first condition always fails, as proved in the two-alpha audit. For a
three-alpha chain, exactly one of the two conditions in (4.1) must fail.
Exact cyclic reduction shows that the second condition holds only for

\[
(x,y)=(3,9),\qquad(5,9),\qquad(7,9).
\tag{4.2}
\]

The remaining missing rows and the two pairs exchanged there are

\[
\begin{array}{c|c|c|c}
x&L_x&\text{missing negative}&\text{opposite positive}\\ \hline
3&\{1,4,5,7,10\}&\{0,2\}&\{2,9\}\\
5&\{1,3,6,7,10\}&\{0,4\}&\{4,9\}\\
7&\{1,3,5,8,10\}&\{0,6\}&\{6,9\}.
\end{array}
\tag{4.3}
\]

For \(x=3,5\), the current PBBS chord at \(L_x\) shares no endpoint with
the missing pair, so an ordinary executable alpha cannot replace it by that
pair. A double-cancellation completion would have to delete the opposite
positive in the last column of (4.3); direct reduction of its two remaining
negative rows gives no chart.

For \(x=7\), the current chord at \(L_7\) is \(\{6,7\}\), so the only
possible final executable alpha has spare \(6\). Writing its core as
\(L_7-z\), its next required negative pair is

\[
\epsilon_{L_7-z}(7)=\{0,6\}.
\tag{4.4}
\]

For \(z=1,3,5,8,10\), the forward survivors of these five rows are

\[
2,\ 4,\ 6,\ 8,\ 0.
\]

The sole entries compatible with one endpoint have full endpoint pairs
\(\{4,6\}\) and \(\{0,9\}\), never \(\{0,6\}\). Thus (4.4) also fails.

The boundary \(x=1\) was already eliminated by the endpoint table

\[
\{0,2\},\{3,4\},\{4,6\},\{6,8\},\{1,8\},
\]

and reflection handles the reverse family. Therefore:

### Theorem 4.1

There is no monotone three-alpha availability chain from the alternating
PBBS component.

## 5. Three-alpha target and resolution

Every three-alpha portal must exhibit at least one genuinely
nonconformal feature:

1. a fork supplying two defects of the alternating alpha;
2. a star-type cyclic cancellation on three distinct shared rows;
3. a top-type cyclic cancellation concentrated at one shared row;
4. a double cancellation at one row embedded in a nonmonotone path.

The first item is realized by the explicit fork certificate.  The other
three remain relevant only for classifying all portals or finding variants
with better equivariance, residence, or higher-depth behavior.

Every candidate still lives on at most three adjacent rank-four cores. The
star/top dichotomy is the useful dimension reduction: there is no fourth
core geometry to audit.
