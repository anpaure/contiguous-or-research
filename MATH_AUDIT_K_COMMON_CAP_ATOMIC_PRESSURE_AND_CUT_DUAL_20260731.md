# Independent audit of atomic common-cap pressure and cut duals

Date: 2026-07-31  
Audited file:
`MATH_THEOREM_K_COMMON_CAP_ATOMIC_PRESSURE_AND_CUT_DUAL_20260731.md`  
Method: two independent proof audits; no finite search

## 1. Atomic graph and pressure direction

The canonical event for a bad set fixes one candidate in each of its target
parts.  Two events must be lopsided neighbours exactly when they prescribe
different candidates in a common part.  Compatible events agree wherever
they overlap.  Conditioning on the first event can only activate compatible
events and therefore can only reduce the probability of avoiding them.  The
lopsidependency direction in Lemma 2.1 is correct.

For activities \(t_v\), put \(x_F=\prod_{v\in F}t_v\).  The proof of
Theorem 3.1 obtains

\[
 \Pr(A_F)\le x_F\prod_{v\in F}\Psi_t(v).
\]

The candidate products can count one opposing event more than once.  Since
all factors \(1-x_G\) lie below one, this repeated counting makes the product
smaller.  Hence the inequality has the correct direction for the atomic
lopsided local lemma.  The part-capacity condition

\[
       \sum_{v\in D_S}t_v\Psi_t(v)\ge1
\]

is therefore a valid integral sufficient theorem.

## 2. Cluster-expansion audit

For the ordinary part-intersection dependency graph, all events using a
fixed part form a clique.  An independent family in the closed neighbourhood
of \(F\) uses mutually disjoint target parts, so its monomial is represented
in

\[
       \prod_{S\in\operatorname{parts}(F)}(1+T_S).
\]

This is an upper bound on the closed-neighbourhood independence polynomial,
including the singleton \(\{F\}\).  Thus

\[
       B_S\ge1+T_S
\]

is a correct cluster-expansion sufficient condition.  With one arity \(j\),

\[
 \max_{t>1}{t-1\over t^j}={(j-1)^{j-1}\over j^j};
\]

the pair constant is \(1/4\).  The atomic Jensen constant is asymptotically
\(1/(je)\) when \(m\to\infty\).  These criteria are complementary: the
cluster cut is stronger for uniform counts, while atomic pressure retains
candidate heterogeneity.

## 3. Cut dual and integrality scope

Let \(A\) be the aggregate cell/conflict-row matrix and let \(\Delta\) be
the product of the target simplices.  Fractional feasibility is

\[
       A\Delta\cap(b-\mathbb R_{\ge0}^{\mathcal R})\ne\varnothing.
\]

If these convex sets are disjoint, separation has a nonnegative normal
\(z\), because the second set is a down-set.  Minimizing the separating
functional over \(\Delta\) separates by target parts.  This proves exactly

\[
 \sum_S\min_{v\in D_S}q_z(v)
 \le\sum_Rz_Rb_R
 \qquad(z\ge0).
\]

Thus a strict reverse inequality is an exact rational certificate of
fractional infeasibility.  It is not an integral criterion in general.
Binary parts on odd cycles, with the two equal-value pairs forbidden on
each edge, have the all-\(1/2\) fractional point but no integral
transversal.  The minimal integral obstruction support is unbounded even at
rank two.

If the augmented part/cell/conflict matrix is totally unimodular, the right
sides are integral and the fractional criterion becomes integral.  Total
unimodularity therefore is a valid carrier-specific route, but the odd-cycle
family proves it cannot follow from bounded conflict rank.  The Hall-kernel
and Rado statements are correctly presented only as sufficient structured
alternatives.

## 4. Verdict

The focused theorem is proof-safe after the following incorporated scope
qualifications:

- the asymptotic Jensen implication assumes \(m\to\infty\);
- the explicit uniform formulas are sufficient specializations, not
  equivalents of the nonuniform pressure theorems; and
- owner orientation removes empty-letter cuts but does not supply any
  pressure, TU, or Hall-kernel bound.

The remaining all-dimensional task is genuinely carrier-specific: prove
one atomic/cluster pressure inequality or construct a TU/laminar/Hall
kernel for the PBBS/Pascal occurrence atlas.

