# Concise audit of the original two compact missing-theorem formulations

> **Subsequent status correction (2026-07-24).**  This audit verified that
> the original DRAY statement was a sufficient target; it did not prove the
> statement.  DRAY has since been disproved by
> `MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md`, independently audited in
> `MATH_ATTACK_F_DRAY_CONSTRUCTION_AUDIT_20260724.md`.  The current status is
> recorded in `TWO_COMPACT_MISSING_THEOREMS_20260724.md`.

Source audited: TWO_COMPACT_MISSING_THEOREMS_20260724.md

Date: 2026-07-24

## Verdict

At the time of this audit, both boxed hypotheses matched the audited DRAY
and \(\mathrm{AD}_A\) reductions. Either hypothesis, with the quantifiers
below made explicit, would imply
\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]
The DRAY hypothesis was subsequently disproved; the \(\mathrm{AD}_A\)
hypothesis remains unproved and is not known necessary.

No normalization or coefficient is wrong. Four formal corrections are
required:

1. in Problem A, state \(t\in\mathbb N\);
2. distinguish the primitive DRAY quantifier from its equivalent
   nonprimitive gcd extension;
3. in Problem B, state explicitly that for every fixed \(A\) and all
   sufficiently large \(m\), one common forest and one common set of
   compatibility choices exist, with all little-\(o\) terms taken as
   \(m\to\infty\);
4. line 76 should say “a literal word of length **at most**” the displayed
   quantity.

## Problem A

The exact audited hypothesis is:

> For every fixed primitive integer triple
> \[
> 0<a<b,\qquad c>2b,
> \]
> as \(t\to\infty\) through positive integers,
> \[
> g_3(at,bt,ct)
> =(at+1)(bt+1)+o_{a,b,c}(t^2).
> \]

The source states the box formula for every fixed integer triple and then
says primitive triples suffice. These formulations are compatible. If
\((a,b,c)=d(a',b',c')\), the primitive statement applied along
\(s=dt\) gives the displayed nonprimitive statement. Thus primitivity is a
reduction, not an extra missing case.

The width claim is exact. Since \(0<a<b\) and \(c>2b\),
\[
c>a+b,
\]
so the third chain is at least the sum of the first two and
\[
w(at,bt,ct)=(at+1)(bt+1).
\]

The quantifier “pointwise for every fixed primitive triple” is sufficient.
The audited scale-first, mesh-second cone extension does not require a rate
uniform in \((a,b,c)\). Boundary dominant rays are handled by closure and
zero-side children by the slice word.

The proved implication is
\[
\mathrm{DRAY}
\Longrightarrow
(g_4-w_4)_+=o(R^3)
\Longrightarrow
\nu(k)=W(k)+o(W(k)).
\]
The hook identity, exact width telescope, short-side slice construction, and
truncated-moment four-block SCD aggregation are already proved inputs.

For terminological precision, line 20 may say “a finite word of box points
covering every nonzero box point by contiguous coordinatewise maxima.”
Whether zero entries are syntactically allowed does not change \(g_3\):
deleting a zero entry preserves every old witness after contraction.

## Problem B

The even-dimensional normalization is correct:
\[
W_e=\binom{2m}{m},\qquad
N_{1,e}=\binom{2m}{m-1},\qquad
H=\lceil A\sqrt m\rceil.
\]
It must not be replaced by the odd exact-factor normalization
\(\binom{2m+1}{m}\).

The exact existential quantifier is:

> For every fixed \(A>0\), for all sufficiently large \(m\), there exists one
> oriented spanning Johnson linear forest in \(J(2m,m)\), together with one
> compatible collection of orientations, cuts, boundary dummies, initial
> upper singleton/residual orders, and forced cut-colour prescriptions, such
> that the two boxed estimates hold as \(m\to\infty\).

For sufficiently large \(m\), \(H\le m/2\), as required by the finite
adaptive-MTF theorem.

The certified-edge condition is correctly separated by sign. More
explicitly, the same certified edge subset \(E_{\rm cert}\) must satisfy
\[
e=|E_{\rm cert}|,
\]
the lower colours
\[
T\cap T'\qquad(TT'\in E_{\rm cert})
\]
must be pairwise distinct, and the upper colours
\[
T\cup T'\qquad(TT'\in E_{\rm cert})
\]
must be pairwise distinct separately. Distinct ordered lower-upper pairs
alone do not justify \(2(N_{1,e}-e)\).

The quantities \(c\) and \(\rho_H\) have the correct meaning:

* \(c\) is the component count of the original oriented linear forest;
* \(\rho_H\) counts its internal positive coordinate runs of length at most
  \(H\);
* the entry edge of each such run is cut, producing exactly
  \(c+\rho_H\) components.

All tilded support defects must be evaluated after the same orientation,
cuts, dummy choices, and residual orders. They are the canonical-support
defects of this chosen construction, not invariants of the unoriented
forest and not necessary defects for arbitrary literal words.

The audited length statement is the upper bound
\[
L_{\rm band}\le
W_e+(2H+1)(c+\rho_H)+2(N_{1,e}-e)
+\sum_{q=2}^{H}
(\widetilde M_q^-+\widetilde M_q^+).
\]
Accordingly, “of length” in line 76 should be “of length at most.”

The two boxed estimates imply
\[
(2H+1)(c+\rho_H)=o(W_e),
\]
because \(2H+1\le3H\), and every other excess term is explicitly \(o(W_e)\).
Hence
\[
L_{\rm band}=W_e+o(W_e).
\]
Applying the audited fixed-\(A\) diagonalization and product-SCD tails gives
the global coefficient-one theorem.

This implication uses only the linear physical reset charge. It does not
claim that all cutting loss is \(O(H\rho_H)\); possible
\(H^2\rho_H\)-scale deterioration is already included in the tilded support
defects required to be \(o(W_e)\).

## Correct final form

After the four formal edits, the note states exactly two independent
sufficient problems:
\[
\mathrm{DRAY}\Longrightarrow\text{coefficient one},
\qquad
\{\mathrm{AD}_A\text{ for every fixed }A\}
\Longrightarrow\text{coefficient one}.
\]
There is no claimed converse, equivalence, or necessity. This matches the
audited handoff.
