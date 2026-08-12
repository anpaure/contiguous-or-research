# Independent audit: twisted-C6 polynomial-core Theorem 5.1

**Date:** 2026-08-02  
**Status:** proof replay of Theorem 5.1 in
MATH_THEOREM_K_TWISTED_C6_RESIDUAL_ORE_CURVATURE_AND_POLYNOMIAL_CORE_20260802.md.
Verdict: **PASS**, subject to the theorem's stated pump
external-one-incidence hypothesis and the earlier full-Boolean
capacity-two inequality. One dependency in the prose should be made
explicit, but there is no logical gap.

## 1. Protected minimality really gives \(\mathcal M_P(S)<q\)

Let \(H\subseteq Q\) be edge-minimal nonextendable, let \(S\) be a strict
Ore cut, and put \(T=(L-F)\setminus S\).

If an edge \(e\in H\) has its lower endpoint in \(S\), deleting \(e\) from
the protected bank increases the left demand on \(S\) by one. The right
side of the same Ore inequality increases by at most one. Since the old
failure is strict and integral, it remains a failure, contradicting
minimality. Hence every lower endpoint of \(H\) lies in \(T\), and

\[
             h:=|E(H)|\le \min\{q,2|T|\}.                    \tag{1.1}
\]

For each right vertex \(Y\),

\[
 \min\{2-d_H(Y),d_{G_P-H}(Y,S)\}
 \ge \min\{2,d_{G_P}(Y,S)\}-d_H(Y).                        \tag{1.2}
\]

No edge of \(H\) is incident with \(S\), so the left demand of \(S\)
remains \(2|S|\). Summing (1.2) and applying the strict Ore failure gives

\[
 \sum_{Y\in R-O}\min\{2,d_{G_P}(Y,S)\}-h<2|S|,
\]

or

\[
                         \mathcal M_P(S)<h\le q.            \tag{1.3}
\]

Thus the use of \(\mathcal M_P(S)<q\) in Theorem 5.1 is valid. The stronger
bound \(h\le2|T|\) remains needed in the next step.

## 2. The small-shore exclusions

Write

\[
 s=|S|,\qquad t=|T|,\qquad D=(m-1)(m-2).
\]

If \(s\le(m-2)(m-3)\), Lemma 4.1 gives

\[
 \mathcal M_P(S)\ge m-3\ge q\ge h,
\]

contradicting (1.3). Hence

\[
                         s>(m-2)(m-3).                      \tag{2.1}
\]

If \(t\le D/2\), Lemma 4.2 gives

\[
 \mathcal M_P(S)\ge\min\{m-3,2t\}.
\]

By (1.1), \(h\le q\le m-3\) and \(h\le2t\), so the right side is at least
\(h\), again contradicting (1.3). Therefore

\[
                         t>D/2.                              \tag{2.2}
\]

The published proof says that (2.1)--(2.2) follow from Lemmas 4.1--4.2
after invoking Lemma 3.1. That is correct. For readability, the derivation
of (2.2) should explicitly cite the second inequality in (1.1); the weaker
display \(\mathcal M_P(S)<q\) alone would not exclude the range
\(2t<q\).

## 3. Spectral localization and exhaustion by two cases

Let

\[
 g(S)=|N_{ML_m}(S)|-|S|.
\]

The full capacity-two inequality and deletion of the \(p\) owners give

\[
 \mathcal M_P(S)
 \ge {m-2\over m-1}g(S)-2p.                              \tag{3.1}
\]

When the stated full inequality is only invoked for \(g(S)\ge m-1\), the
remaining case is automatic because

\[
 m-1<
 G={m-1\over m-2}(2p+q).
\]

Thus (1.3) always implies

\[
                         g(S)<G.                            \tag{3.2}
\]

For reference, (3.1)'s full-graph term can be re-derived directly. If
\(u=|N(S)|=s+g\) and the reached right degrees sum to \(ms\), then

\[
 \#\{Y:d(Y,S)\ge2\}
 \ge {ms-u\over m-1}
 =s-{g\over m-1}.
\]

Therefore

\[
 \sum_Y\min\{2,d(Y,S)\}
 \ge u+s-{g\over m-1}
 =2s+{m-2\over m-1}g.
\]

The rank-\((m-1)\)/rank-\(m\) incidence graph is \(m\)-regular with second
singular value \(m-1\). Tanner's bound gives

\[
 g(S)\ge
 {n\,s(N-s)\over ns+(m-1)^2N}
 \ge {n\over2m^2}\min\{s,N-s\}.                           \tag{3.3}
\]

Combining (3.2)--(3.3) gives

\[
 u:=\min\{s,N-s\}<B={2m^2G\over n}.                       \tag{3.4}
\]

There are exactly two branches:

1. \(u=s\);
2. \(u=N-s\).

They exhaust all spectrally localized cuts. In the second branch,

\[
 N-s=|F|+|T|=p+t=|A|,                                    \tag{3.5}
\]

so it is exactly the small-curvature-support shore used in the proof, not
the residual complement \(t\) alone.

## 4. Audit of the \(u=s\) Lovász--KK branch

Complement \(S\) to a rank-\(m\) family of size

\[
 s=\binom{x}{m}.
\]

By (0.14) and (3.4),

\[
 s<B\le\binom{m+2}{3}<\binom{m+3}{3}
 =\binom{m+3}{m},
\]

so \(m\le x<m+3\). Lovász--Kruskal--Katona gives

\[
 |N(S)|\ge\binom{x}{m-1}
 =\binom{x}{m}{m\over x-m+1}
 \ge {m\over4}s.                                         \tag{4.1}
\]

The exact incidence total is \(ms\). Summing

\[
 \min\{2,j\}\ge1+{j-1\over m-1}
\]

over the upper shadow yields

\[
 \sum_{Y\in R}\min\{2,d(Y,S)\}
 \ge {ms+(m-2)|N(S)|\over m-1}
 \ge {m(m+2)\over4(m-1)}s.                              \tag{4.2}
\]

Every \(x\in S\subseteq L-F\) is incident with at most one deleted pump
owner. Hence deletion of \(O\) removes at most \(s\), not merely \(2p\).
Subtracting that loss and \(2s\) gives

\[
 \mathcal M_P(S)\ge
 {m^2-10m+12\over4(m-1)}s=a_ms.                         \tag{4.3}
\]

For \(m\ge10\), \(a_m>0\). Equations (2.1) and (0.15) imply

\[
 \mathcal M_P(S)>a_m(m-2)(m-3)\ge q,
\]

contradicting (1.3). This branch is sound.

## 5. Audit of the \(u=N-s\) Lovász--KK branch

Put

\[
 a=|A|=N-s=p+t.
\]

By (0.14) and (3.4),

\[
 a<B\le\binom{m+2}{3}=\binom{m+2}{m-1}.
\]

Write \(a=\binom{x}{m-1}\); then \(m-1\le x\le m+2\).
Let \(U\) be the rank-\(m\) owners all of whose facets lie in \(A\), and
write \(u_0=|U|=\binom{z}{m}\). If \(u_0=0\), the next bound is immediate;
otherwise Lovász--Kruskal--Katona applied to
\(\partial U\subseteq A\) gives \(z\le x\). Thus

\[
 u_0\le\binom{x}{m}
 =a\,{x-m+1\over m}
 \le {3a\over m}.                                        \tag{5.1}
\]

Let \(v_0\) count owners having exactly \(m-1\) facets in \(A\).
Counting the \(ma\) incidences out of \(A\) gives

\[
                         mu_0+(m-1)v_0\le ma.             \tag{5.2}
\]

Since the full critical charge equals \(2u_0+v_0\),
(5.1)--(5.2) yield

\[
 \begin{aligned}
 \kappa(A)
 &=2a-(2u_0+v_0)\\
 &\ge
 \left(
 2-{m\over m-1}-{3(m-2)\over m(m-1)}
 \right)a\\
 &={ (m-2)(m-3)\over m(m-1)}a
 =c_ma.                                                   \tag{5.3}
 \end{aligned}
\]

Using \(a=p+t>p+D/2\), \(\rho_O(A)\ge0\), and (0.16),

\[
 \mathcal M_P(S)
 =\kappa(A)+\rho_O(A)-2p
 >c_m\left(p+{D\over2}\right)-2p
 \ge q,
\]

again contradicting (1.3). This branch is sound.

## 6. Verdict and scope

Theorem 5.1 is proof-safe. In particular:

* protected edge-minimality gives the stronger
  \(\mathcal M_P(S)<h\le\min\{q,2t\}\), so
  \(\mathcal M_P(S)<q\) is justified;
* the spectral minimum has only the two branches treated in the theorem;
* both real-binomial parameters lie in the domains required by
  Lovász--Kruskal--Katona; and
* the coefficients \(a_m,c_m\) and all uses of (0.15)--(0.16) are
  arithmetically correct.

The only recommended edit is expository: in the sentence deriving
\(t>D/2\), cite \(|H|\le2t\) explicitly. This does not change the theorem
or its scope.

