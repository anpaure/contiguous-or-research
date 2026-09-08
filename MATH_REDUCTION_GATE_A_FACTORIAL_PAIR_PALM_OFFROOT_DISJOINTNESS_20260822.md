# Gate A: factorial pair-Palm mass is asymptotically off-root disjoint

**Date:** 2026-08-22  
**Status:** proved product-reference factorial-Palm estimate; the
cutoff-tail leakage and the disjoint-cell signed determinant remain open

## 0. Outcome

Fix \(m\) and sample an ordered \(m\)-carrier from the
survival-weighted product-reference label law at one root.  For any two
specified carrier positions \(a\ne b\),

\[
 \boxed{
 \Pr\bigl((F_a\cap F_b)-\{v\}\ne\varnothing\bigr)
 =O_m\left({1\over rx^3}+{1\over r^2x^4}\right).}        \tag{0.1}
\]

The estimate is uniform for \(x\ge r^{-\alpha}\), \(y\ge x\), provided

\[
 \alpha<{1\over3(m-1)}.                                  \tag{0.2}
\]

At \(m=12\), the first-pair marginal of this carrier law is exactly the
ordered-pair factorial Palm law \(\Pi_{12}\).  Hence

\[
 \boxed{\Pi_{12}\{\tau\ne(0,0)\}
       =O((rx^3)^{-1})=o(1)}                              \tag{0.3}
\]

whenever \(\alpha<1/33\).

This is a real localization, but not a tail-relative closure.  If
\(S=d\Pi_c/d\Pi_{12}\) up to normalization, then one still-open leakage is

\[
 \Pi_c\{\tau\ne(0,0)\}
 ={ \mathbb E_{\Pi_{12}}[
       S\mathbf1_{\{\tau\ne(0,0)\}}]\over
    \mathbb E_{\Pi_{12}}S}.                              \tag{0.4}
\]

The denominator in (0.4) may be a very small cutoff-tail mass.  Therefore
(0.3) cannot be divided by it.  Small leakage probability alone also does
not control an unbounded kernel: a tail-relative uniform-integrability
estimate for \(q_0K/z\) is required.  Even after that estimate, the signed
within-cell determinant on the dominant cell \(\tau=(0,0)\) still has to
be controlled.

## 1. Rooted overlap kernels

Let \(\mathcal F_v\) be the \(D\) punctured catalogue rows containing a
fixed target \(v\).  Condition on retaining \(v\).  Every other lower
target is retained independently with probability \(x\), every other
middle target with probability \(y\ge x\), and every row
\(F\in\mathcal F_v\) has the same conditional survival probability

\[
 w=\Pr(F\text{ survives}\mid v\text{ survives}).          \tag{1.1}
\]

For distinct \(F,G\in\mathcal F_v\), put

\[
 t(F,G)=|(F\cap G)-\{v\}|.                                \tag{1.2}
\]

For fixed \(c\ge1\), define

\[
 R_c=\max_F{1\over D}\sum_{G\ne F}
                   \{x^{-c\,t(F,G)}-1\},                  \tag{1.3}
\]

\[
 Q_c=\max_F{1\over D}\sum_{\substack{G\ne F\\t(F,G)>0}}
                   x^{-c\,t(F,G)}.                        \tag{1.4}
\]

The proved rooted boundary-polymer estimate gives, whenever
\(c\alpha<1/2\),

\[
 R_c,\ Q_c
 =O_c\left({1\over rx^{3c}}+{1\over r^2x^{4c}}\right).    \tag{1.5}
\]

For orientation, (1.5) follows by expanding
\((1+(x^{-c}-1))^{t(F,G)}\), double-counting the common target
subfamilies, applying the punctured boundary-codegree theorem, and
enumerating connected subgraphs of the maximum-degree-four boundary
graph.  With \(a_c=x^{-c}-1\), the resulting envelope is
\(O_c(a_c/r+a_c^3/r+a_c^4/r^2)\), which implies (1.5).

## 2. Survival-weighted carrier tuples

For an ordered tuple
\(\gamma=(F_1,\ldots,F_m)\in\mathcal F_v^{\underline m}\), let

\[
 q_\gamma^*
 =\Pr(F_1,\ldots,F_m\text{ survive}\mid v\text{ survives}). \tag{2.1}
\]

If a nonroot target \(u\) belongs to \(n_u\) members of \(\gamma\), then

\[
 {q_\gamma^*\over w^m}
 =\prod_{\substack{u\ne v\\n_u\ge2}}p_u^{\,1-n_u}.        \tag{2.2}
\]

Since \(p_u\ge x\) and
\(n_u-1\le\binom{n_u}{2}\),

\[
 1\le {q_\gamma^*\over w^m}
 \le x^{-\sum_{1\le a<b\le m}t(F_a,F_b)}.                \tag{2.3}
\]

Let

\[
 \pi_m(\gamma)={q_\gamma^*\over
           \sum_{\gamma'}q_{\gamma'}^*}                  \tag{2.4}
\]

be the conditional survival-weighted carrier-label law.

### Theorem 2.1 (factorial carrier overlap sparsity)

Assume (0.2).  For every specified \(a\ne b\), equation (0.1) holds.
Consequently the probability that any two of the \(m\) carrier rows have
a nonroot common target is \(O_m((rx^3)^{-1})\).

#### Proof

By symmetry of (2.4), take \(a=1,b=2\).  The lower bound in (2.3) gives

\[
 \sum_{\gamma}q_\gamma^*\ge (D)_m w^m.                    \tag{2.5}
\]

For positive numbers \(z_1,\ldots,z_j\), the arithmetic-geometric mean
inequality gives

\[
 (z_1\cdots z_j)^{1/j}\le {1\over j}\sum_{\ell=1}^jz_\ell.
                                                                    \tag{2.6}
\]

Fix distinct \(F_1,\ldots,F_{i-1}\) and apply (2.6) with
\(z_a=x^{-(i-1)t(F_a,F_i)}\).  Then

\[
 \sum_{F_i\notin\{F_1,\ldots,F_{i-1}\}}
 x^{-\sum_{a<i}t(F_a,F_i)}
 \le D(1+R_{i-1}).                                      \tag{2.7}
\]

For the second carrier, with positive overlap required, (1.4) gives

\[
 \sum_{\substack{F_2\ne F_1\\t(F_1,F_2)>0}}
 x^{-t(F_1,F_2)}
 \le DQ_1.                                               \tag{2.8}
\]

Use the upper bound in (2.3), sum first over \(F_m\), then
\(F_{m-1}\), and continue down to \(F_2\).  Equations (2.7)--(2.8) give

\[
 \sum_{\substack{\gamma\\t(F_1,F_2)>0}}q_\gamma^*
 \le w^mD^mQ_1\prod_{j=2}^{m-1}(1+R_j).                 \tag{2.9}
\]

Under (0.2), (1.5) gives \(R_j=o(1)\) uniformly for
\(2\le j\le m-1\).  Also \(D^m/(D)_m=1+o(1)\), since the punctured root
degree is factorial in \(r\).  Divide (2.9) by (2.5) and use (1.5) at
\(c=1\).  This proves (0.1).  A union bound over the
\(\binom m2\) carrier pairs proves the last assertion.  \(\square\)

## 3. Identification of the first-pair marginal

For distinct \(F,H\in\mathcal F_v\), let

\[
 q_{FH}^*=\Pr(F,H\text{ survive}\mid v\text{ survives})
\]

and

\[
 L_{12}(F,H)
 =\mathbb E[(d_v-2)_{10}\mid F,H\text{ survive}].         \tag{3.1}
\]

Summing the survival probability of an ordered twelve-carrier over its
last ten labels gives

\[
 \sum_{F_3,\ldots,F_{12}}q_{F,H,F_3,\ldots,F_{12}}^*
 =q_{FH}^*L_{12}(F,H).                                   \tag{3.2}
\]

Therefore the first-pair marginal of \(\pi_{12}\) is

\[
 \Pi_{12}(F,H)
 ={q_{FH}^*L_{12}(F,H)\over
   \sum_{F'\ne H'}q_{F'H'}^*L_{12}(F',H')}.               \tag{3.3}
\]

Multiplying numerator and denominator by the fixed root-retention
probability gives the unconditional convention for \(\Pi_{12}\).  Thus
Theorem 2.1 gives (0.3).

## 4. Exact remaining tail-local statement

Let

\[
 E=\{(F,H):(F\cap H)-\{v\}\ne\varnothing\}.
\]

For the cutoff-tail pair law,

\[
 \Pi_c(P)={\Pi_{12}(P)S(P)\over\overline S},\qquad
 \overline S=\mathbb E_{\Pi_{12}}S,                       \tag{4.1}
\]

so (0.4) is exact.  The factorial estimate proves
\(\Pi_{12}(E)=O((rx^3)^{-1})\); a necessary new tail theorem is

\[
 \boxed{\Pi_c(E)=o(1)}                                    \tag{4.2}
\]

uniformly in the deterministic Gate-A cutoffs.  No generic inequality
deduces (4.2) from (0.3), because \(S/\overline S\) is a normalized rare
tail likelihood.  To delete the nonzero-overlap cells from the signed
\(s=2\) comparison one needs the stronger scale-aware statement

\[
 \boxed{
 {q_0\over z}\left\{
 \mathbb E_{\Pi_{12}}\bigl[|K|\mathbf1_E\bigr]
 +\mathbb E_{\Pi_c}\bigl[|K|\mathbf1_E\bigr]
 \right\}=o(1).}                                         \tag{4.3}
\]

Even (4.3) only removes the nonzero-overlap cells.  On the dominant cell
\(E^c\), the two carrier rows still have many inequivalent relative
arrangements, and the signed determinant

\[
 \mathfrak D_{(0,0)}
 ={1\over2}\sum_{P,Q\in\mathcal P_{(0,0)}}
 L_{12}(P)L_{12}(Q)
 \{K(P)-K(Q)\}\{S(P)-S(Q)\}                              \tag{4.4}
\]

need not vanish by symmetry.  The shortest remaining \(s=2\) route is
therefore:

1. prove the tail leakage (4.2);
2. strengthen it to the kernel-weighted estimate (4.3);
3. prove a tail-mass-relative favorable or \(o(z/q_0)\) bound for the
   disjoint-cell determinant (4.4); and
4. retain cancellation with the finite between-cell term whenever either
   separate bound is too strong.
