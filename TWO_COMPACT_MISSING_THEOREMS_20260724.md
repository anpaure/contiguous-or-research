# One compact missing theorem and one disproved route

> **Superseded frontier note.**  The adaptive-forest problem below remains a
> valid sufficient theorem, but it has since been weakened and complemented
> by the independently audited survival-packet and stateful-portal gates.
> Use `CURRENT_COMPACT_MISSING_THEOREMS_20260725.md` for new model attacks.

Problem B below, by the audited reductions in `MATHEMATICAL_HANDOFF.md`,
would prove

\[
\nu(k)=(1+o(1))\binom{k}{\lfloor k/2\rfloor}.
\]

Problem A was originally proposed as a second sufficient route, but it has
since been disproved.  The original formulations were independently checked
in `TWO_COMPACT_MISSING_THEOREMS_AUDIT_20260724.md`; the disproof and its
audit are recorded below.

## Disproved Problem A: dominant three-box ray

For fixed integers

\[
0<a<b,\qquad c>2b,
\]

let \(g_3(p,q,r)\) be the minimum length of a nonzero sequence of points in
\([0,p]\times[0,q]\times[0,r]\) such that the coordinatewise maximum of
some contiguous interval equals every nonzero box point.

The proposed assertion was

\[
\boxed{
g_3(at,bt,ct)=(at+1)(bt+1)+o_{a,b,c}(t^2)
}
\qquad(t\to\infty\text{ through positive integers}).
\]

The main term is exactly the box width because \(c>a+b\).  However, the
assertion is false.  The audited finite witness-order argument in
`MATH_ATTACK_F_DRAY_CONSTRUCTION_20260724.md` proves instead

\[
\boxed{
\liminf_{t\to\infty}
\frac{g_3(at,bt,ct)-(at+1)(bt+1)}{t^2}
\ge
\frac{ab(c-2b)}{c+5a+5b}>0.
}
\]

See `MATH_ATTACK_F_DRAY_CONSTRUCTION_AUDIT_20260724.md`.  Models should not
be asked to prove the boxed ray equality above; any replacement product-box
route must share witnesses across boxes or use a genuinely different local
decomposition.

## Problem B: adaptive Johnson/MTF forest

Fix \(A>0\), put

\[
W_e=\binom{2m}{m},\qquad
N_{1,e}=\binom{2m}{m-1},\qquad
H=\lceil A\sqrt m\rceil.
\]

Construct one oriented spanning Johnson linear forest in \(J(2m,m)\) with:

- \(e\) certified edges whose lower colours are mutually distinct and whose
  upper colours are separately mutually distinct;
- \(c\) forest components;
- \(\rho_H\) internal positive coordinate runs of length at most \(H\), cut
  at their entry edges;
- compatible boundary dummies and residual orders, producing canonical
  missing-support counts \(\widetilde M_q^\pm\).

Prove

\[
\boxed{
N_{1,e}-e=o(W_e)
}
\]

and

\[
\boxed{
H(c+\rho_H)+
\sum_{q=2}^{H}
(\widetilde M_q^-+\widetilde M_q^+)=o(W_e).
}
\]

The quantifier is: for every fixed \(A\), for all sufficiently large \(m\),
one common forest and one common set of compatible boundary/residual choices
must satisfy both boxed estimates, with the \(o\)-terms taken as
\(m\to\infty\). The exact adaptive MTF theorem then constructs a literal
word of length at most

\[
W_e+(2H+1)(c+\rho_H)+2(N_{1,e}-e)
+\sum_{q=2}^{H}(\widetilde M_q^-+\widetilde M_q^+),
\]

so proving the boxed estimates for every fixed \(A\), followed by the
audited diagonalization and tails, proves the global theorem.

## Recommendation

Problem B is now the surviving compact target.  It is project-specific, but
unlike Problem A it has not been disproved.  A worthwhile alternative is to
find a new cross-box sharing theorem that bypasses the local \(g_3\) cost
rather than trying to repair the false dominant-ray statement.
