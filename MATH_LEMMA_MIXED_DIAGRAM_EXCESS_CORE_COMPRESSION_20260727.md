# Mixed row--column diagrams compress at fixed excess

Date: 2026-07-27

Method: pure mathematics only.

## 0. Outcome

Let \(\Gamma=(R,C;E)\) be a finite bipartite multidiagram.  The row
vertices represent link/configuration copies and the nonempty column
vertices represent selected-edge or compensation-resource events.  Define

\[
 \omega(\Gamma)=|E|-|C|
 =\sum_{c\in C}\bigl(d_\Gamma(c)-1\bigr).
\tag{0.1}
\]

Delete every column of degree one and its incident edge, and call the
remaining diagram \(\Gamma_{\ge2}\).  Then

\[
 \boxed{
 |C(\Gamma_{\ge2})|\le\omega(\Gamma),\qquad
 |E(\Gamma_{\ge2})|\le2\omega(\Gamma),\qquad
 |R(\Gamma_{\ge2})|\le2\omega(\Gamma).}
\tag{0.2}
\]

Thus a diagram may contain arbitrarily many private one-incidence columns
while its complete correlation core has size \(O(\omega)\).  In
particular, the order-\(\Theta(m)\) private-star meshes which obstruct a
buffer indexed by total witness order have \(\omega=0\).

If a generator step adjoins one new nonempty column incident with exactly
\(t\) existing or new row copies, then

\[
 \boxed{\omega(\Gamma')-\omega(\Gamma)=t-1.}
\tag{0.3}
\]

Consequently one-incidence columns are triangularly neutral and may be
absorbed into the reference drift, while every genuinely common event
raises \(\omega\).  A finite buffer indexed by \(\omega\), unlike one
indexed by total witness order, is not crossed by adding arbitrarily many
private columns.

This is a structural lemma, not the missing regeneration theorem.  To
close ACLE one must still prove that, after summing all private columns,
every physical core of excess \(r\) receives the expected
\((\operatorname{poly}(r)/m^2)^r\) endpoint factor and that the stopped
generator preserves those bounds.

## 1. Core-size proof

Let

\[
 C_2=\{c\in C:d_\Gamma(c)\ge2\}.
\]

Every \(c\in C_2\) contributes at least one to the sum in (0.1), so

\[
 |C_2|\le\sum_{c\in C_2}(d(c)-1)\le\omega(\Gamma).
\tag{1.1}
\]

Moreover,

\[
\begin{aligned}
 |E(\Gamma_{\ge2})|
 &=\sum_{c\in C_2}d(c)\\
 &=\sum_{c\in C_2}(d(c)-1)+|C_2|\\
 &\le\omega(\Gamma)+\omega(\Gamma)
 =2\omega(\Gamma).
\end{aligned}
\tag{1.2}
\]

Every row retained in \(\Gamma_{\ge2}\) is incident with at least one of
these edges, hence its number is at most \(|E(\Gamma_{\ge2})|\).  This
proves (0.2).

## 2. Generator increment

Adjoining a new column of degree \(t\) increases \(|C|\) by one and
\(|E|\) by \(t\).  Therefore

\[
 \Delta\omega=t-1,
\]

which is (0.3).  The identity remains true when some of the incident rows
coincide in the underlying physical catalogue, provided the equality
partition is applied first and \(t\) denotes the number of incidences in
the resulting multiplicity diagram.

## 3. Relevance to the repaired-ring process

In the compensated slow-bite generator, a column of degree one is a
selected edge or compensation resource killing only one displayed link
copy.  Summed over all such columns, these terms are the exact
first-moment/reference hazard.  Columns of degree at least two are the
breadth, quadratic-variation, and drift-coherence corrections.  The first
degree-two column is the tree term proved in
`MATH_THEOREM_FIRST_COLUMN_BREADTH_ENERGY_REPAIRED_RING_20260727.md`; two
degree-two columns closing a cycle give the first \(C_4\) term proved in
`MATH_THEOREM_FIRST_C4_DRIFT_COHERENCE_SCALE_20260727.md`.

The compression (0.2) shows why those calculations plausibly extend with
constants depending on \(\omega\), rather than on the unbounded number of
private columns.  Proving that extension dynamically is the exact next
step.
