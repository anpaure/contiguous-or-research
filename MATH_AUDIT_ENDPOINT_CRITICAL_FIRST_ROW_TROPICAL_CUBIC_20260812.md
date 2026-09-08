# Audit of the endpoint-critical first-row tropical cubic

**Date:** 2026-08-12
**Audited file:**
`MATH_THEOREM_ENDPOINT_CRITICAL_FIRST_ROW_TROPICAL_CUBIC_AND_LATE_STAIRCASE_SATURATION_20260812.md`
**Verdict:** **PASS self-audit.**  The theorem is a literal first-row
normal form and an exact inverse identity.  It does not prove positivity of
the resulting one-profile covariance.

## 1. Collapse at the first crossing

For total size \(n+r<2n\), a partition containing \(n\) collapses to
\((n,r)\).  A partition not containing \(n\) has a first part crossing
level \(n\).  Its earlier parts have total \(a<n\); its later parts have
total

\[
 c=n+r-a-b< n.
\]

Internal superadditivity is applicable separately to both groups because
their totals are below \(n\).  Thus the replacement \((a,b,c)\) preserves
total size and weakly increases reward.  Zero groups are represented by
\(v_0=0\).  This checks every boundary case, including \(r=0\) and
\(n=2\).

Subtracting the common linear density gives the min-plus form

\[
 f_r=\min\{e_r,e_a+e_b+e_c:a+b+c=n+r\}.
\]

The equality uses ordinary total size, not merely congruence modulo \(n\),
so no finite-availability information has been dropped.

## 2. Inverse identity

For \(0<z<1\), density gives \(C(1+z)>n\), while the literal partition
\((n,C_0(z))\) gives \(C(1+z)\le2n\).  Any feasible inverse triple gives a
literal partition and hence cannot have total size below \(C(1+z)\).

If the first hitting index is below \(2n\), the crossing collapse gives a
three-part certificate.  If it equals \(2n\), \((n,n,0)\) is a
three-part certificate.  Replacing each part reward by its left-inverse
index can only lower the total index; a strict lowering would contradict
the definition of the first hitting index.  This proves both inequalities
in the inverse formula, including repeated phase values and the terminal
case \(C_0(z)=n\).

The discrepancy formula follows by subtracting \(n(1+z)\).  The overshoot
penalty

\[
 n(x_1+x_2+x_3-1-z)

\]

is indispensable; deleting it would be a false residue-only relaxation.

## 3. Saturation argument

If \(v_j\) is strictly above \(v_{j-1}\) and every nontrivial
superadditivity inequality with total \(j\) is strict, then a small
coordinatewise decrease of \(v_j\) preserves the whole table polytope.
Every inequality having \(v_j\) on its right is relaxed.  The tropical
cubic is coordinatewise nondecreasing, so all first-row phases weakly
decrease.  On the region \(B'<0\), decreasing \(v_j\) strictly decreases
\(-B(v_j)\); because \(H_2'<0\), it also weakly decreases every
\(-H_2(p_r)\).  Therefore a minimizer must satisfy the claimed plateau or
additive equality.

The endpoint \(v_n=1\) is fixed and is correctly excluded.  The phrase
"unique zero" in the source means the unique zero of \(B'\) in the open
interval; \(B'(0)=0\) is the harmless boundary zero.

For the early-phase statement, increasing \(v_j\) can affect only finitely
many constraints and finitely many expressions in the tropical maximum.
If no displayed constraint is tight and no maximizing expression uses
\(v_j\), a common positive perturbation radius exists.  On \(B'>0\), the
direct term then strictly decreases and every tail term stays fixed.  This
checks the complementary saturation theorem without a differentiability
assumption on the max function.

## 4. Scope

The proved degree-three certificate is an integer saturation theorem for
the one-dimensional first-row Bellman signature.  It neither proves
normality of the occurrence-labelled packet semigroup nor supplies
disjoint Boolean target witnesses.  The remaining analytic statement is
exactly the nonnegativity of

\[
 \int_0^1\left[U_0B'+(\mathcal T_nU_0)H_2'\right].

\]
