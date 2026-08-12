# Audit of the correlated-row report, Section 7

Date: 2026-07-26

Audited source:
MATH_ATTACK_L_CORRELATED_ROW_NESTED_CHARGE_BARRIER_AND_LITERAL_ESCAPE_20260726.md,
Section 7.

## Verdict

Theorem 7.1 is correct for the unrestricted safe Johnson column catalogue
\(\Gamma_H\). Its five displayed conditions are necessary and sufficient
for an integral, \(H\)-safe, run-neutral successor whose final shadow
loads lie in the prescribed intervals.

The adjacent-depth marginal statement and the forced pivot

\[
                         T\to S\leftarrow T'
\]

are also correct. The following scope corrections should be made.

1. Write \(1\le j\le H\) in (7.2), and \(1\le q<H\) before (7.3).
2. In (7.4), state explicitly that \(T'\ne T\). The negative summand is
   forced because the \(T\)-summand is positive while the saturated
   \(S\)-row has nonpositive net effect.
3. Add the upper-sign analogue
   \(U\to V\leftarrow U'\), \(V\in\nabla U\).
4. “Integer circuits” at the end should mean signed memory-kernel trades.
   The equations prove that \(\delta\) is a signed circulation in the
   memory-state graph, coupled by root-fibre exchanges. They do not by
   themselves prove an edge-sign-alternating circuit decomposition.
5. The iff is not automatically an iff inside a fixed
   \(D_r\)-transversal or exact-factor fibre. If that fibre is encoded by
   extra rows \(Cz=b\), add \(C\delta=0\). If it is encoded by restricting
   \(\Gamma_H\), the overlap-circulation equivalence must be reproved for
   the restricted catalogue.
6. The abundance sentence should also retain sign compatibility
   \(\delta^-\le z\), simultaneous caps at every other depth and the
   opposite sign, quantitative sequential slack, total support/seam toll
   \(o(W)\), \(o(W/H)\) final cycles, and literal-OR linearization.

The projected pivot is necessary, not sufficient. A point-balanced signed
flow on the adjacent-rank inclusion graph is not thereby proved to lift to
one \(\delta\) satisfying the root, memory, run, cap, and optional
fixed-fibre rows. With these qualifications, Section 7 faithfully states
the exact escape certificate and does not prove its abundance.
