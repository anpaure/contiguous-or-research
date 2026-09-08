# The global-coordinate potential dies at the first nontrivial dimension

Date: 2026-07-31  
Status: exact finite theorem for the coordinate-induced potential
catalogue; no claim about middle-owner-dependent potentials.

## 1. The fixed catalogue

Fix a total order

\[
                         1<2<\cdots<2m.                 \tag{1.1}
\]

For every Boolean diamond \(L\subset U\), write
\(U\setminus L=\{a,b\}\) with \(a<b\), and retain only the oriented atom

\[
                         L+a\longrightarrow L+b.        \tag{1.2}
\]

The common potential

\[
                         \varphi(X)=\sum_{x\in X}x       \tag{1.3}
\]

strictly increases on every retained atom.  Consequently an exact choice
which uses every lower and upper resource once and every tail and head
resource at most once is automatically an acyclic ordered
four-transversal.

All total coordinate orders give isomorphic catalogues, by relabelling the
ground set.

## 2. Exact verdict

### Theorem 2.1

The catalogue (1.2) has exactly two ordered four-transversals at \(m=2\)
and none at \(m=3\).  Hence no potential induced solely by one global total
order of ground coordinates can prove the ordered-four-transversal theorem
in every dimension.

#### Proof

The recurrence used for the exact count is stated independently of any SAT
encoding.  A state is

\[
                  (R,U_*,T_*,H_*),                     \tag{2.1}
\]

where \(R\) is the set of lower resources not yet assigned and
\(U_*,T_*,H_*\) are the already used upper, tail and head resources.
Choose any \(L\in R\).  For every pair \(a<b\) outside \(L\) whose three
resources

\[
               L+a+b,\qquad L+a,\qquad L+b             \tag{2.2}
\]

are unused, recurse after deleting \(L\) and inserting those three
resources.  If no such pair exists the state contributes zero; the empty
state contributes one.

Every completion has exactly one atom over the chosen lower resource, so
the branches are disjoint and exhaustive.  Memoization and choosing a
currently shortest row change only evaluation order, not the recurrence.
Exact integer evaluation gives

\[
\begin{array}{c|c|c|c}
m&\text{candidate atoms}&\text{states evaluated}&\text{solutions}\\ \hline
2&12&11&2\\
3&90&5601&0.
\end{array}                                             \tag{2.3}
\]

The standard-library reproducer named below implements (2.1)--(2.2)
literally with integer bitsets.  This proves the count. \(\square\)

## 3. Exact boundary

The result independently verifies the first nontrivial negative case of
the coordinate-order probe.  It does not use, and therefore does not
authenticate, the separately reported \(m=4\) count.

More importantly, it does not obstruct Theorem 3.1 of
MATH_THEOREM_A_CATALAN_ORDERED_FOUR_TRANSVERSAL_ODD_CIRCUIT_ROUNDING_20260731.md.
That theorem permits an arbitrary potential on middle owners.  It only
shows that a successful common potential cannot be a fixed additive order
of the ground coordinates.

## 4. Mechanical audit

The exact recurrence is implemented in

scratch/audit_thread_a_global_coordinate_potential_m3_20260731.py.

Its JSON output is frozen in

scratch/thread_a_global_coordinate_potential_m3_20260731.audit.json.
