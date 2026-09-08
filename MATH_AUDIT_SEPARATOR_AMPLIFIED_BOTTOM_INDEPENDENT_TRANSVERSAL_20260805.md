# Audit of separator-amplified bottom independent transversal

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_SEPARATOR_AMPLIFIED_BOTTOM_INDEPENDENT_TRANSVERSAL_20260805.md`  
**Theorem SHA-256:**
`e8f60329066b56f50253e2855c25fa1e572f14c0885c109cf5bcda16b675fda3`  
**Method:** independent finite-graph, FIFO, and scalar-ledger replay; no
computation or search  
**Verdict:** **PASS** for the unconditional deterministic core.  The
product-residual tail input and occurrence-level compiler remain explicit
hypotheses.

## 1. Conflict-degree and Haxell constant

Each option uses three distinct resources: one member of \(B_0\) and two
members of \(B_1\).  An option therefore has at most

\[
 (R_0-1)+2(R_1-1)=R_0+2R_1-3
\]

neighbours in the option conflict graph.  Multiple counting of one
conflicting option only lowers this number.  Haxell's independent-
transversal theorem requires every task class to have size at least twice
the maximum degree.  The hypothesis

\[
             |\Omega_i|\ge 2(R_0+2R_1)
\]

is stronger than that requirement, so Theorem 3.1 has safe constant
margin.

After deleting high-resource options, the surviving conflict graph has
the thresholds in (4.1).  Every retained task loses at most \(\eta D\)
additional options, and the incidence charge \(B_*/(\eta D)\) correctly
bounds the number of tasks discarded for excessive loss.  Thus Corollary
4.1 follows exactly.

## 2. FIFO orientation

With

\[
 L_i=T_2^i-\{b_2^i,b_1^i\},
\]

the orientation \(x_2=a,x_1=b\) gives

\[
 T_1=L_i\cup\{a,b_1^i\}=U_a,
 \qquad T_0=L_i\cup\{a,b\}=U_0,
\]

and the opposite orientation gives \(T_1=U_b\) with the same \(T_0\).
The independent transversal reserves both possible \(B_1\) endpoints of
every selected option.  Hence either orientation may be chosen later.
Disjointness of \(B_0\) and \(B_1\) rules out cross-level owner collisions.

## 3. Banks and asymptotic constants

Under the saturated ledger

\[
 H_0=(1+o(1)){W\over d+1},
\]

the residual bank has size \((2+c+o(1))H\).  Thus fixed banks of sizes
\(\beta_0H,\beta_1H\) fit whenever
\(\beta_0+\beta_1<2+c\), for all sufficiently large \(d\) (with the
obvious integer rounding).

Writing \(\theta=(d+1)H/W\), the corrected general densities are

\[
 p_j={\beta_j\theta+o(1)\over d+1},
 \qquad
 D=\Theta(\beta_0\beta_1^2\theta^3d).
\]

The saturation assumption gives \(\theta=1+o(1)\); more generally a fixed
lower bound on \(\theta\) is enough for the claimed \(d\)-scale tails.
This condition is necessary: the inequality \(W\ge(d+1)H_0\) alone would
allow \(\theta\to0\) and would not imply exponential-in-\(d\) tails.

Double counting gives

\[
 R_0\sim D/\beta_0,
 \qquad R_1\sim2D/\beta_1,
\]

so the limiting Haxell inequality is

\[
 {1\over\beta_0}+{4\over\beta_1}<{1\over2}.
\]

The displayed choice \(\beta_0=\beta_1=20\) has left side \(1/4\), and
its bank sum is \(40\); hence every fixed \(c>38\) supplies the stated
margin.

## 4. Scope of the budget conclusion

Discarding \(O(H_0/d)\) copies loses \(O(H_0)\) owner slots and
\(O(H_0)\) lower-payload occurrences.  Under saturation this is
\(O(W/d)=o(W)\).  This is a scalar owner-capacity and unmatched-payload
count only.  It is not a physical word-length repair and does not match
the lost named targets to actual separator cells.

Accordingly the audited theorem proves:

1. the finite deterministic two-level bottom completion under its option
   degree and resource-load hypotheses;
2. the exceptional-resource cleanup bound; and
3. the stated constants in a saturated product-residual model.

It does **not** prove the factorial-moment tails for the recursive
occurrence process or the final occurrence-level compiler.
