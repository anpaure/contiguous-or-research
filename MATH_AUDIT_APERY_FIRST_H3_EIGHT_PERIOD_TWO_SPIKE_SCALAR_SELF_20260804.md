# Self-audit: first depth-three period and two-spike scalar

**Date:** 2026-08-04  
**Target:** MATH_THEOREM_APERY_FIRST_H3_EIGHT_PERIOD_TWO_SPIKE_SCALAR_20260804.md  
**Target SHA-256:** 6bd6f88141be70ea8f6e5305f491c2745699baf32daf913f6d67253178b7eb92  
**Verdict:** **PASS / GO in the stated classification and sufficient-subchamber scope.**

This is a proof self-audit, not an independent-authorship audit. No
enumeration, solver, numerical search, Python, or H100 computation was used.

## 1. Overlap combinatorics

For increasing left and right endpoints, \(r\) half-open intervals overlap
exactly when some consecutive \(r\)-block has latest left endpoint below
its earliest right endpoint. Substituting

\[
 X_j=s_{j+1}/A,\qquad Y_i=(A-s_{h-i})/A
\]

gives \(s_{i+r}+s_{h-i}<A\). For \(r=3\), subtracting from
\(A=P+s_1\) cancels the first gap and gives precisely

\[
 \gamma_{h-i+1}+\cdots+\gamma_h
 >
 \gamma_2+\cdots+\gamma_{i+3}.
\]

The indices and the strict inequality agree with the half-open convention.

## 2. Minimum period and period-eight chamber

Depth three implies \(u\ge3\). The previously audited disjoint-ray
inequality \(u+1<h-u\) then gives \(h\ge8\).

At \(h=8\), \(u=3\). The overlap condition is \(X_3<Y_1\), namely
\(s_4+s_7<A\). With

\[
 L=\gamma_2+\gamma_3+\gamma_4,\qquad T=\gamma_8,
\]

this is \(T>L\). Conversely it gives

\[
 A-2s_4=\gamma_5+\gamma_6+\gamma_7+T-L>0.
\]

The other midpoint condition is

\[
 2s_5>A
 \quad\Longleftrightarrow\quad
 L+\gamma_5>T+\gamma_6+\gamma_7.
\]

Thus the two displayed inequalities are necessary and sufficient. Since
every gap is at least \(a\), they imply
\(\gamma_8>3a\) and \(\gamma_5>2a\), proving genuine multidefectness.

## 3. Two-spike honesty

After subtracting the baseline from

\[
 (a,a,a,a,b,a,a,t),
\]

the two excess positions are five and eight. Prefixes of lengths one
through four have zero excess. Prefixes of lengths five through seven have
excess \(b-a\). Every cyclic block of those latter lengths contains at
least one excess position, and blocks containing only position eight have
excess \(t-a\). Therefore all prefix-minimum inequalities hold exactly
when \(t\ge b\). This is equivalent to cyclic superadditivity.

Substitution into the exact period-eight chamber gives
\(t>3a\) and \(b>t-a\). The example \(b=t=4a\) satisfies every inequality,
so it is a symbolic counterexample to the proposed universal \(H\le2\)
bound.

## 4. Scalar normalization

Writing

\[
 v=t/a,\qquad \eta=(t-b)/a
\]

converts the honest depth-three domain to \(v>3\) and
\(0\le\eta<1\). The total period and exact threshold are

\[
 P=(6+2v-\eta)a,\qquad A=(7+2v-\eta)a.
\]

The shift list in the theorem follows by literal partial sums. Reflection
of the last three shifts gives complements

\[
 (v+1)a,\quad(v+2)a,\quad(v+3)a,
\]

while \(F(a)+F(P)=\rho(a)\). This verifies every term and sign in
\(\mathcal E(v,\eta)\).

The size-nine exact carry is a legal configuration of value \(A\). Repeating
it gives a lower comparison to the literal clock, and above \(A\) the kernel
is increasing. Hence \(\Phi(W)\ge\mathcal E(v,\eta)\) has the correct
direction.

## 5. Closed subchamber

The condition \(v\le(9+\eta)/2\) is exactly \(D\le16\). Thus \(4/D\ge1/4\).
Also \(D>12\), so \(2/D,3/D<1/4\). Since \(v>3\),
\((v+1)/D>1/4\), and \((v+3)/D<1/2\) follows from \(\eta<1\).

Therefore quarter-half monotone decrease pairs
\(f(4/D)\ge f((v+1)/D)\). The two early values each exceed \(57/1400\);
the two remaining reflected compact values are below \(61/1000\).
All reflected theta points are at least \(1/4\), hence positive, and the
singleton theta term exceeds \(-1/20000\).

The rational margin is

\[
 {43\over1000}+2{57\over1400}-2{61\over1000}-{1\over20000}
 ={333\over140000}>0.
\]

The arithmetic and inequality directions check.

## 6. Scope

The theorem does not compress every \(h=8,H=3\) word to the two-spike
face and does not sign the residual scalar \(v>(9+\eta)/2\). It also does
not address larger periods, higher overlap depth, overshoot, later crossing,
or finite physical shoulders. Subject to those exclusions, the result is
proof-safe.
