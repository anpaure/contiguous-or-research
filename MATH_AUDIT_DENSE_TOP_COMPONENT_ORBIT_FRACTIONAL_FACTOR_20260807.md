# Audit of the dense-top component orbit fractional factor

**Date:** 2026-08-07  
**Audited file:**
*MATH_THEOREM_DENSE_TOP_COMPONENT_ORBIT_FRACTIONAL_FACTOR_20260807.md*  
**Verdict:** The four-palette orbit-load theorem is correct, after replacing
one false “strictly increase” statement by the central equality
\(\binom n m=\binom n{m+1}\).  The sparse-row thinning theorem is correct
only as a relaxation with fractionally **designated** cells.  It is not a
simultaneous literal component factor: unmarked suffix cells remain
physical occurrences, and exact saturation of unequal-sized rank layers
by one component orbit is ruled out by a one-line mass identity.

## 1. The four orbit loads pass

Let \(M\) be the number of distinct labelled images in the component
orbit, let every resource list have size \(L\), and put

\[
 N_a=\binom n a.
\tag{1.1}
\]

Transitivity of \(\operatorname{Sym}([n])\) on the rank-\(a\) layer makes
the degree of every rank-\(a\) resource

\[
 D_a=\frac{ML}{N_a}.
\tag{1.2}
\]

This remains true when the orbit is taken as distinct component images:
all image stabilizers are conjugate, and incidence double counting does
not depend on the chosen representative.

With

\[
 w=\frac1{D_\rho}=\frac{N_\rho}{ML},
\tag{1.3}
\]

the four loads are exactly

\[
\begin{array}{c|c}
\text{part}&\text{load per resource}\\ \hline
\text{top, rank }\rho&1\\
\text{lower \(q1\), rank }m-1&N_\rho/N_{m-1}\\
\text{owner, rank }m&N_\rho/N_m\\
\text{upper \(q1\), rank }m+1&N_\rho/N_{m+1}.
\end{array}
\tag{1.4}
\]

Since \(n=2m+1\),

\[
 N_m=N_{m+1},
\tag{1.5}
\]

not \(N_m<N_{m+1}\).  For \(q\ge2\),

\[
 \rho=m-q<m-1,
\]

so

\[
 N_\rho<N_{m-1}<N_m=N_{m+1}.
\tag{1.6}
\]

All three auxiliary loads in (1.4) are nevertheless strictly below one.
Thus Theorem 2.1 and its four-partite fractional-feasibility conclusion
are valid; only the monotonicity sentence in its proof needs correction.

The corollary excluding a separator built solely from these four
nonnegative capacity rows is also valid in that scoped packing
relaxation.  It says nothing about a fifth occurrence-linked row.

## 2. The raw sparse-row loads also pass

For the weight-\(q\) queue, each component has exactly \(L\) physical
suffix cells in every depth \(j\), of rank

\[
 r_j=m-(q-j)q,\qquad 1\le j\le q-1.
\tag{2.1}
\]

The total selected component mass in the top-normalized orbit factor is

\[
 \sum_{C'}w
 =Mw
 =\frac{N_\rho}{L}.
\tag{2.2}
\]

Therefore its total number, with fractional multiplicity, of depth-\(j\)
cells is

\[
 L\sum_{C'}w=N_\rho.
\tag{2.3}
\]

Symmetry distributes this mass uniformly over \(N_{r_j}\) targets, giving
the stated raw load

\[
 \lambda_j=\frac{N_\rho}{N_{r_j}}\ge1.
\tag{2.4}
\]

Equality occurs only at \(j=q-1\).  These calculations in the submitted
proof are correct.

## 3. What independent thinning really proves

Introduce an occurrence variable

\[
 y_{C',e,j}
\tag{3.1}
\]

which records how much of the physical depth-\(j\) cell at endpoint \(e\)
of component image \(C'\) is **designated** for the named target bank.
Setting

\[
 y_{C',e,j}
 =\alpha_j w,\qquad
 \alpha_j=\frac{N_{r_j}}{N_\rho}\le1
\tag{3.2}
\]

does give every rank-\(r_j\) target designated load exactly one.  Also
\(y_{C',e,j}\le w\), and different \(j\)'s refer to different cells.

Thus the submitted argument proves the following relaxation:

> Every sparse rank layer admits a simultaneous symmetric fractional
> designation supported on the selected component occurrences.

This may be useful for a later role-assignment LP.  It is not a literal
all-row component factor, because reducing \(y\) does not reduce the
component variable \(w\).  The unmarked fraction

\[
 (1-\alpha_j)w
\tag{3.3}
\]

of the suffix cell is still present in the literal source history and
still has the same set value.  “Different physical suffix depths” removes
competition between different \(j\)'s, but it does not erase the surplus
occurrences within one fixed \(j\).

There are only two semantics under which (3.2) is enough:

1. unmarked physical suffix cells are allowed to repeat named targets and
   consume no target capacity; or
2. the theorem is explicitly about designated-role coverage, not about
   occurrence-exact SCD target use.

Neither semantic is the ordinary one-copy target partition required by a
literal SCD factor.

## 4. Exact mass obstruction to literal simultaneous saturation

The scope failure is visible without any collision calculation.  Let
\(x_{C'}\) be arbitrary nonnegative weights on component images, not
necessarily uniform.  Every component contributes exactly \(L\) physical
cells to every sparse row.  If its top row saturates all rank-\(\rho\)
targets exactly once, then

\[
 L\sum_{C'}x_{C'}=N_\rho.
\tag{4.1}
\]

If the same literal components saturate rank \(r_j\) exactly once, then

\[
 L\sum_{C'}x_{C'}=N_{r_j}.
\tag{4.2}
\]

For \(j<q-1\),

\[
 N_{r_j}<N_\rho,
\tag{4.3}
\]

so (4.1) and (4.2) are incompatible.  This proves:

\[
\boxed{
\begin{gathered}
\text{No fractional weighting of full queue components can exactly}\\
\text{saturate both the top row and any proper sparse lower row.}
\end{gathered}}
\tag{4.4}
\]

The obstruction is occurrence-level and survives arbitrary nonuniform
weights.  Independent row thinning evades it only by ceasing to count
some physical cells as resources.

If the intended condition is coverage with repetitions allowed, then no
thinning is needed: (2.4) already gives load at least one.  If the intended
condition is capacity at most one or exact SCD occurrence once, then the
unthinned orbit factor violates that row and (3.2) does not repair it.

## 5. Recommended scope correction

Theorem 3.1 should be renamed along the lines of

> **Simultaneous sparse-row designated-mark saturation.**

Its conclusion should state explicitly that unmarked suffix occurrences
remain in the component and that no uniqueness or capacity claim is made
for them.  The status and Section 4 should not say that all fractional
obstructions for the queue's sparse lower rows have been removed.

The proof-safe final ledger is:

* four central palettes: exact fractional top saturation with all three
  auxiliary capacities strictly slack;
* sparse suffix rows: exact symmetric fractional **designations** exist;
* literal all-row target factor: impossible for this one component type
  alone by (4.4), unless surplus cells can be assigned a formally
  non-consuming role or additional component types change the per-row
  occurrence vector.

The last alternative is a genuine configuration-factor problem.  It
cannot be replaced by independent thinning of linked component cells.
