# Audit of the full-base SCD extension and first literal Hall gate

**Date:** 2026-08-07  
**Object audited:** `MATH_THEOREM_SINGLE_BULGE_FULL_BASE_SCD_EXTENSION_AND_FIRST_LITERAL_HALL_GATE_20260807.md`  
**Method:** direct base/bridge reconstruction, greedy incidence recount, and
independent Edmonds matroid-intersection derivation  
**Verdict:** **PASS.**  In particular, formula (5.1) is necessary and
sufficient exactly for the stated three-component spanning-forest relaxation.
It is necessary but not sufficient for the literal three equal-path problem;
the source states this scope correctly.

## 1. Complete base inventory

Put \(P=C_0-H\), so \(|P|=s-1\).  At each of the \(3(d-1)\) low phases,
the first marked value (formula (2.6) in the hinge theorem with \(q=1\)) is

\[
                         P+f_u.
\]

At each of the three high phases, the first bridge value in formula (2.9)
is likewise

\[
                         P+g_u=P+f_u.
\]

Thus all \(3d=K\) phases supply exactly the star

\[
                         \{P+x:x\in F\}.
\]

After selecting its \(K\) petals there are \(v-K\ge d\) labels outside
\(P\cup F\), enough for the reset bank.  The literal-lift assertion is
therefore correct.

## 2. Greedy base packing and SCD extension

At termination of the greedy packing, every unused center is incident with
at least \(v-K+1\) used rank-\(s\) targets.  Counting center--target
incidences gives

\[
                         (C-M)(v-K+1)\le MKs,
\]

which rearranges to (2.1).  Multiplication by \(K/V\) and \(Cv=Vs\)
gives (2.2).  The asymptotic loss is

\[
                         O(K/v)+O(v/(Ks))=O(1/d).
\]

For Theorem 3.1, distinct rank-\(s\) sets lie in distinct chains of any
fixed symmetric-chain decomposition.  A chain containing rank \(s\) ends
at rank at least \(n-s>m-1\).  Truncation therefore produces the claimed
pairwise disjoint saturated segments.  No literal-alignment conclusion is
smuggled into this abstract extension.

## 3. Two-layer greedy path packing

At an unused center \(P\), the available vertices are precisely the unused
rank-\(s\) petals, and an available graph edge is precisely an unused
rank-\((s+1)\) color.  A path on

\[
                         R=3(d-1)
\]

vertices, split into three consecutive blocks of \(d-1\) vertices, leaves
exactly

\[
                         3(d-2)=R-3
\]

within-block path edges.  The three further available vertices provide the
high petals because \(K=R+3\).

At termination, a center with fewer than \(v/2\) available petals sees more
than \(v/2\) used rank-\(s\) targets.  Otherwise, Erdos--Gallai for a graph
with no path on \(R\) vertices gives

\[
 e(G_P)\le{(R-2)a\over2},
\]

so the number of blocked pairs is

\[
 {a\choose2}-{(R-2)a\over2}
   ={a(a-R+1)\over2}\ge {v^2\over16}
\]

under \(a\ge v/2\) and \(R\le v/4\).  A used rank-\((s+1)\) target contains
exactly \(\binom{s+1}{2}\) rank-\((s-1)\) centers.  This reproduces
(4.8)--(4.10) and hence (4.4).  Dividing its denominator by \(R\) gives

\[
                         2+8=10,
\]

so (4.5) is correct.

## 4. Independent derivation of the graphic cut

For star \(i\), let \(M_i\) be the graphic matroid of \(K_{L_i}\),
truncated to rank \(R-3\).  Its rank on \(A_i\subseteq E_i\) is

\[
 r_i(A_i)=\min\{R-3,R-c_i(A_i)\},                    \tag{4.1}
\]

because the ordinary graphic rank is \(R-c_i(A_i)\), with isolated
vertices included in \(c_i\).  For the direct sum \(\mathsf G_3\),

\[
 r_{\mathsf G_3}(A)=\sum_i r_i(A_i).                 \tag{4.2}
\]

The color constraint is a partition matroid \(\mathsf C\).  Its rank on
\(B\subseteq E\) is exactly

\[
                         r_{\mathsf C}(B)=|\kappa(B)|. \tag{4.3}
\]

Let

\[
                         K_0=\sum_i(R-3).
\]

Edmonds' matroid-intersection min--max theorem says that a common independent
set of size \(K_0\) exists if and only if

\[
 r_{\mathsf G_3}(A)+r_{\mathsf C}(E-A)\ge K_0
 \qquad(A\subseteq E).                               \tag{4.4}
\]

For one summand,

\[
 (R-3)-\min\{R-3,R-c_i(A_i)\}
    =\max\{0,c_i(A_i)-3\}.                           \tag{4.5}
\]

Substituting (4.2)--(4.5) into (4.4) gives exactly

\[
 |\kappa(E-A)|
   \ge\sum_i\max\{0,c_i(A_i)-3\}.                   \tag{4.6}
\]

Thus (5.1) is both necessary and sufficient for a common independent set of
total size \(K_0\).  Since each summand has rank cap \(R-3\), total size
\(K_0\) forces exactly \(R-3\) selected edges in every star.  An acyclic
graph on \(R\) vertices with \(R-3\) edges has exactly three connected
components.  Therefore the common independent set is precisely a
three-component spanning forest in every star, with globally distinct
colors.

This equivalence does **not** impose maximum degree two or component sizes
\(d-1,d-1,d-1\).  Hence it does not characterize three equal Hamilton-path
pieces.  The theorem explicitly calls it a forest relaxation and retains
those two physical conditions as extra rows.  Its necessity/sufficiency
scope is exact.

## 5. Bridge Hall rows

At fixed bridge offset \(r\), every endpoint chooses one target from

\[
                         \mathcal N_r(e)
   =\{A_e+J:J\subseteq H_i,\ |J|=r\}.
\]

Distinctness at that rank is an ordinary system-of-distinct-representatives
problem, so (6.3) is the exact rowwise Hall condition.  It is only necessary
for the full literal chain system because choices at successive offsets must
be nested and all endpoints of a ring share one \(H_i\).  This limitation is
also stated correctly.

## 6. Final audit boundary

The source proves, without an unpriced assumption:

1. an almost-spanning complete-base star packing;
2. a theta-sized two-row literal packing;
3. an abstract one-SCD extension of all chosen bases; and
4. the exact matroid-Hall condition for the forest relaxation of a frozen
   first marked row.

It does not prove literal SCD alignment, the three equal-path condition for a
frozen family, or coherent shared-\(H\) bridge completion.  Those omissions
are explicit, so no correction is required.

