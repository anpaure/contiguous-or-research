# Selector-fibre complete designs: exact nested-flag marginals and the grouping gate

Date: 2026-07-26

Method: pure mathematics only.  No random labeling, nibble, solver, or
web input is used.

## 0. Result

Let \(Q_S\) be one large product status cell in the rank-twisted
macroblock tiling.  Reserve \(t\) axes as selectors.  For each selector
value \(z\in\mathbb F_2^t\), choose an active \(r\)-set \(A_z\) among
the remaining \(n=S-t\) axes and an affine conjugate \(g_z\) of the
certified \(Q_r\) compiler.  Freeze the other \(n-r\) axes in all
orientations.

This always partitions \(Q_S\) exactly into \(Q_r\) packets.  Moreover,
there is a deterministic labeling with the following properties.

1. Put

   \[
          K=\binom nr\,|\operatorname{Aff}(Q_r)|
            =\binom nr\,2^r r!.                      \tag{0.1}
   \]

   All but fewer than \(K\) selector labels split into complete batches
   containing every pair
   \((A,g)\in\binom{[n]}r\times\operatorname{Aff}(Q_r)\) the same
   number of times.
2. On the good batches, every ordered, signed nested deletion flag of
   every depth \(q\le H<r\) has exactly the same aggregate
   multiplicity.  This is an integral complete-design identity, not
   uniformity in expectation.
3. If

   \[
       t\ge\log_2K+\log_2H+\omega(1),                 \tag{0.2}
   \]

   the exceptional selector fibres have owner mass \(o(|Q_S|/H)\).
   Since

   \[
       \log_2K
       =r\log_2(n/r)+r\log_2r+O(r),                  \tag{0.3}
   \]

   the proposed scale
   \(t\asymp r\log(S/r)+r\log r=o(S)\) has sufficient room after an
   \(O(r)+\log H+\omega(1)\) slack term.
4. Exact uniform use of all \(2^t\) labels, with no exceptional batch,
   is generally arithmetically impossible.  Already at depth one it
   requires

   \[
                         {2^t r\over n}\in\mathbb Z. \tag{0.4}
   \]

   An odd prime in \(n/\gcd(n,r)\) cannot be removed by increasing
   \(t\).
5. Most importantly, exact aggregate flag marginals are not literal
   target Hall.  The selector coordinates are frozen and hence are
   recoverable from every lower or upper target produced inside the
   fibre.  Conditional on a fixed \(z\), there is only one column
   \((A_z,g_z)\), not the average of the \(K\) columns.  This is the
   integral grouping obstruction.

Thus the selector construction removes abstract support Poisson holes
with negligible loss.  The remaining theorem is a selector-conditioned
flow/matching statement coupled to the exact rank-twisted compatibility
polynomials, not an orthogonal-array marginal calculation.

## 1. Exact owner refinement

Write

\[
                 Q_S=Q_t\times Q_n,\qquad n=S-t.     \tag{1.1}
\]

For a selector value \(z\in Q_t\), choose \(A_z\in\binom{[n]}r\).
For every orientation \(y\in Q_{[n]\setminus A_z}\), the set

\[
                 \{z\}\times Q_{A_z}\times\{y\}      \tag{1.2}
\]

is a physical \(Q_r\).  As \(y\) varies, (1.2) partitions the whole
selector fibre \(\{z\}\times Q_n\); as \(z\) varies, the selector
fibres partition \(Q_S\).  Hence arbitrary choices of \(A_z\) and
compiler conjugates preserve ownership exactly.

No boundary or seam is created: each packet in (1.2) receives a complete
cyclic compiler factor.

## 2. Complete batching of active sets and conjugates

Let

\[
 \Omega=\binom{[n]}r\times
        \bigl(\mathbb F_2^r\rtimes\mathfrak S_r\bigr),\qquad
 |\Omega|=K.                                         \tag{2.1}
\]

Write

\[
                         2^t=aK+b,\qquad 0\le b<K.   \tag{2.2}
\]

Assign every \(\omega\in\Omega\) to exactly \(a\) selector labels, and
assign the remaining \(b\) labels arbitrarily.  This is a deterministic
labeling.  The first \(aK\) labels are the good labels.

The exceptional owner fraction inside \(Q_S\) is exactly

\[
                         {b\over2^t}< {K\over2^t}.   \tag{2.3}
\]

Condition (0.2) makes (2.3) \(o(1/H)\).  Formula (0.3) follows from
Stirling:

\[
\begin{aligned}
 \log_2\binom nr&=r\log_2(n/r)+O(r),\\
 \log_2(2^rr!)&=r+r\log_2r+O(r).
\end{aligned}                                       \tag{2.4}
\]

For \(S=\Theta(m)\) and \(r=m^\alpha\) with \(\alpha<1\), this \(t\)
is \(m^\alpha\log m=o(m)\).

## 3. Exact nested-flag marginals

Fix a certified isometric compiler factor on \(Q_r\).  Every start
vertex \(x\in Q_r\) has a return-free ordered direction list

\[
                 \tau_q(x)=(i_1,\ldots,i_q)          \tag{3.1}
\]

for each \(q<r\).  Its lower deletion flag also records, on those
directions, which endpoint is deleted; encode this by
\(\varepsilon_q(x)\in\mathbb F_2^q\).  The upper insertion flag is
encoded analogously.

Let

\[
        \mathbf j=(j_1,\ldots,j_q)                   \tag{3.2}
\]

be an ordered tuple of distinct physical axes in \([n]\), and let
\(\varepsilon\in\mathbb F_2^q\).  We count occurrences of the signed
flag \((\mathbf j,\varepsilon)\) over one complete batch \(\Omega\).

First choose the active set \(A\supseteq\{j_1,\ldots,j_q\}\), in

\[
                         \binom{n-q}{r-q}            \tag{3.3}
\]

ways.  For each base start \(x\), exactly \((r-q)!\) coordinate
permutations send \(\tau_q(x)\) to \(\mathbf j\).  After that
permutation is fixed, exactly \(2^{r-q}\) translations give the
prescribed endpoint-sign vector on the \(q\) used axes.  Finally, the
\(n-r\) inactive orientations produce \(2^{n-r}\) parallel packets.
Since there are \(2^r\) base starts, the exact multiplicity is

\[
 \boxed{
 M_q=\binom{n-q}{r-q}\,
      2^{n-r}\,2^r\,(r-q)!\,2^{r-q}
    =\binom{n-q}{r-q}2^{n+r-q}(r-q)!.}              \tag{3.4}
\]

It is independent of \((\mathbf j,\varepsilon)\).  Multiplication by
the batch count \(a\) gives the good-label multiplicity.

The same calculation at \(q=H\) is an exact equality for full nested
flags

\[
 J_1\subset J_2\subset\cdots\subset J_H,             \tag{3.5}
\]

because (3.5) is equivalent to one ordered \(H\)-tuple.  Truncating
(3.5) proves every lower-depth marginal simultaneously.  Upper flags
have the same count by replacing deleted endpoint signs with inserted
endpoint signs.

As a check, multiplying (3.4) by the number
\((n)_{\underline q}2^q\) of ordered signed \(q\)-flags gives

\[
 \binom nr\,2^rr!\,2^n,                              \tag{3.6}
\]

the total number of starts over all selector fibres in one complete
batch.

Thus no abstract support flag has a Poisson hole on the good labels.

## 4. Divisibility without an exceptional batch

Suppose instead that all \(2^t\) labels are required to give an exact
uniform \(q\)-subset marginal using only active \(r\)-sets.  If
\(c_q(J)=|\{z:J\subseteq A_z\}|\), double counting gives

\[
             c_q(J)=2^t{\binom rq\over\binom nq}     \tag{4.1}
\]

for every \(J\in\binom{[n]}q\).  Every number in (4.1) must be an
integer.  At \(q=1\) this is (0.4).

More generally, an exact \(H\)-design requires, for every
\(0\le i\le H\),

\[
       2^t{\binom{r-i}{H-i}\over
                  \binom{n-i}{H-i}}\in\mathbb Z.     \tag{4.2}
\]

These are genuine odd-prime obstructions because \(2^t\) changes only
the two-adic valuation.  Complete batching avoids them by placing fewer
than \(K\) labels in the exceptional set, whose owner mass is negligible
under (0.2).

For floor/ceiling rather than exact uniform marginals, write

\[
                         c_q(J)\in
 \{\lfloor\lambda_q\rfloor,\lceil\lambda_q\rceil\},
 \qquad
 \lambda_q=2^t{\binom rq\over\binom nq}.             \tag{4.3}
\]

The levels cannot be rounded independently.  They obey the exact
incidence-flow identities

\[
 \sum_{x\notin J}c_{q+1}(J+x)
                         =(r-q)c_q(J)                \tag{4.4}
\]

for every \(J\in\binom{[n]}q\).  Equation (4.4) is the first integral
grouping constraint on any multidepth floor construction.

## 5. The literal selector decoder

The aggregate equality (3.4) forgets the selector label.  Literal
targets do not.

Every selector axis is frozen throughout every packet in its fibre.
Consequently, if a lower or upper target is produced from selector fibre
\(z\), its singleton orientation on all selector axes is exactly \(z\).
There is a deterministic decoder

\[
                    \operatorname{sel}(T)=z          \tag{5.1}
\]

for the contribution of this status cell.  Conditional on \(z\), the
exact flag marginal is

\[
 C_{z,q}(\mathbf j,\varepsilon)
   =\mathbf1_{\{\{j_1,\ldots,j_q\}\subseteq A_z\}}\,
     C_{g_z,q}(\mathbf j,\varepsilon),               \tag{5.2}
\]

where \(C_{g_z,q}\) is the flag count of the single chosen conjugate.
There is no average over \(\Omega\) in (5.2).

At the level of an integral flow, introduce

\[
 x_{z,\omega}\in\{0,1\},\qquad
 \sum_{\omega\in\Omega}x_{z,\omega}=1.               \tag{5.3}
\]

The symmetric fractional point
\(x_{z,\omega}=1/K\) gives the marginals (3.4), and complete batching
integralizes their sum over \(z\).  A selector-conditioned target
constraint, however, has the form

\[
 \sum_{\omega}x_{z,\omega}a_{\omega,F}
                  =a_{\omega_z,F},                  \tag{5.4}
\]

one library column.  Membership of a demanded vector in the convex hull
of the columns \(a_{\omega,\cdot}\) does not make it one column.
Equation (5.4) is the exact integral grouping obstruction.

Targets may also have compatible sources in other product status cells,
so (5.1) is not asserted to be a global invariant of the entire atlas.
But such cross-cell rescue must be entered explicitly in the Hall
ledger; aggregate orthogonal-array marginals cannot stand in for it.

## 6. Remaining selector-conditioned Hall theorem

For each product status cell \(C\), selector label \(z\), active choice
\(\omega=(A,g)\), and signed target \(T\), let

\[
 b^\pm_{C,z,\omega,q}(T)\in\{0,1\}                  \tag{6.1}
\]

record whether the exact rank-twisted compatibility condition holds and
the conjugated compiler assigns a depth-\(q\) start to \(T\).  The
remaining problem is to choose one binary row (5.3) for every pair
\((C,z)\) so that, simultaneously for \(q\le H\),

\[
 \sum_{C,z,\omega}x_{C,z,\omega}
             b^\pm_{C,z,\omega,q}(T)
       \in\{\lfloor W/N_q\rfloor,\lceil W/N_q\rceil\} \tag{6.2}
\]

for all but \(o(W)\) literal targets, with the lower and upper choices
sharing one compiler chronology.

The complete-batch theorem proves that the column sums of (6.2) are
exactly balanced after quotienting by selector labels and literal
compatibility.  It does not prove the row-grouped integral system
(5.3), (6.2).  A valid positive theorem needs either:

* an integral flow whose groups are the selector fibres and whose target
  cuts use the exact compatibility polynomials; or
* a legal further subdivision that gives several independent option
  columns to each selector-decoded target class without losing ownership.

This is strictly smaller than the original owner-packing problem and
strictly stronger than an orthogonal-array or random-marginal statement.

The exact multiple-choice primal, the floor/ceiling hypersimplex, and its
weighted Hall/Farkas dual are developed in
\`MATH_THEOREM_SELECTOR_CONDITIONED_CONFIGURATION_LP_AND_HALL_DUAL_20260726.md\`.
That audit also shows that the linear conditional direction discrepancy
is not by itself a physical Hall cut once quota resets and cross-cell
sources are included.
