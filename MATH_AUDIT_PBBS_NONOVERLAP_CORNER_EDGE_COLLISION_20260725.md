# Audit of the PBBS nonoverlap-corner edge charge

Date: 2026-07-25  
Method: pure mathematics only; no computation, search, solver, or external input

Audited report:
MATH_ATTACK_PBBS_NONOVERLAP_CORNER_EDGE_COLLISION_20260725.md.

## 0. Verdict

The phase-lattice dichotomy, the minimal-corner shield bounds, the
first-maximum suffix tail, the two-colour quotient-edge injection, and the
critical-order sparse-corner conclusion all pass.

In particular, the following statements are valid with the quantifiers in
the source:

\[
 \sum_{I\in\mathcal P}\kappa_R(I)
 \le 2\mathcal T_m(2R-1),                         \tag{0.1}
\]

\[
 \mathcal T_m(L)
 \le C B_m\left(L^{-1/2}+m^{-1/4}\right),         \tag{0.2}
\]

\[
 \sum_{I\in\mathcal P}
 \#\{c\in\mathcal C(I):|c|_1\ge\rho s(I)\}
 \le C_{\alpha,\rho}B_m m^{-1/4},                 \tag{0.3}
\]

and, for every critical-order packing,

\[
 \frac{\sum_I|\mathcal C(I)|}{\sum_I s(I)}
 \longrightarrow0.                               \tag{0.4}
\]

There was one factual error in the final example description.  The
audited explicit strip family has two minimal nonoverlap corners, not one:

\[
 \boxed{(t+1,0)\quad\text{and}\quad(0,s-u).}       \tag{0.5}
\]

This sentence has been corrected in the source.  The correction does not
change any estimate or residual statement.

No coefficient-one conclusion follows.  Persistent-overlap returns and
cross-interval incidence between the sparse corner roots remain open.

## 1. Phase-lattice and shield audit

For outer coordinates

\[
 t=a,\qquad u=s-b-1,\qquad r=a+b,
\]

put

\[
 X_a=\sum_{j<a}|T_j|,
 \qquad
 Y_b=\sum_{j=s-b}^{s-1}|S_j|.
\]

The exact outer ledger is

\[
 B_{t,u}=r+X_a+Y_b,
 \qquad S_{t,u}=r.
\]

Since

\[
 \Delta_{t,u}=B_{t,u}-\Lambda
\]

and the free-monoid alternative is

\[
 \Delta_{t,u}\ge r
 \quad\text{or}\quad
 \Delta_{t,u}\le-r,
\]

the two branches are exactly

\[
 X_a+Y_b\ge\Lambda                                \tag{1.1}
\]

and

\[
 X_a+Y_b\le\Lambda-2r.                            \tag{1.2}
\]

Thus the nonoverlap set is an upper ideal.  Its minimal elements are an
antichain and have pairwise distinct first and second coordinates.

Let \((a,b)\) be minimal nonoverlap.  If \(a>0\), its predecessor
\((a-1,b)\) is overlap, so

\[
 X_{a-1}+Y_b\le\Lambda-2(r-1),
 \qquad
 X_a+Y_b\ge\Lambda.
\]

Subtracting gives

\[
 |T_{a-1}|\ge2r-2.                                \tag{1.3}
\]

The identical vertical argument gives

\[
 b>0\Longrightarrow |S_{s-b}|\ge2r-2.            \tag{1.4}
\]

The source's word identities are also correctly oriented.  Extending the
corner pair one phase to the left or right and using the overlap branch
gives

\[
 \overline T_{a-1}0=Z_cH_L,
 \qquad
 0S_{s-b}=H_RZ_c,
\]

with

\[
 \operatorname {net}(Z_c)=-r,
 \qquad
 \operatorname {net}(H_L)
 =\operatorname {net}(H_R)=r-1.
\]

Hence the delimiter-restored sector lengths are at least \(2r-1\).
Finally,

\[
 d(D_j)=|S_j|+1,
 \qquad
 d(\phi D_j)=|T_j|+1                              \tag{1.5}
\]

are the exact primal and dual sector identities.  Therefore the shields
charged later are sectors of actual quotient roots, not formal blocks.

## 2. Audit of the long-suffix tail

Let

\[
 b_{m,j}=\#\{D\in\mathcal D_m:d(D)=2j+1\}.
\]

Cut a Dyck word immediately after the first primitive component attaining
its global height \(h\).  The part after the cut is exactly the canonical
terminal suffix and is an arbitrary height-\(h\)-capped Dyck word.
Consequently

\[
 b_{m,j}=\sum_{h\ge1}A_{m-j,h}C_h(j),             \tag{2.1}
\]

and in particular

\[
 b_{m,j}\le B_{m-j}B_j.                           \tag{2.2}
\]

For \(J\le j\le m/2\), Catalan estimates give

\[
 \frac{b_{m,j}}{B_m}
 \le
 C\frac{m^{3/2}}
 {(j+1)^{3/2}(m-j+1)^{3/2}}
 \le C(j+1)^{-3/2}.
\]

Summing gives the term \(O((J+1)^{-1/2})\).

For \(j=m-n>m/2\), every nonzero term in (2.1) has \(h\le n\), whence

\[
 b_{m,m-n}\le B_nC_n(m-n).                        \tag{2.3}
\]

If \(n>\sqrt m\), discarding the cap in (2.3) and using Catalan estimates
gives

\[
 \sum_{\sqrt m<n<m/2}
 \frac{B_nB_{m-n}}{B_m}
 \le C\sum_{n>\sqrt m}n^{-3/2}
 =O(m^{-1/4}).                                    \tag{2.4}
\]

If \(n\le\sqrt m\), the path-graph spectral expansion gives, uniformly
for \(q=m-n\ge m/2\),

\[
 C_n(q)
 \le
 C4^q(n+1)^{-3}
 \exp\left(-c\frac{q}{(n+1)^2}\right).            \tag{2.5}
\]

Indeed, after pairing the endpoint eigenmodes, the normalized summands
are bounded by

\[
 C(n+1)^{-3}k^2
 \exp\left(-c\frac{qk^2}{(n+1)^2}\right),
\]

whose sum has the form (2.5).  Multiplying by

\[
 B_n\le C4^n(n+1)^{-3/2},
 \qquad
 B_m\ge c4^m m^{-3/2},
\]

shows that the normalized \(n\)-th contribution is at most

\[
 Cm^{3/2}(n+1)^{-9/2}
 \exp\left(-c\frac{m}{(n+1)^2}\right).            \tag{2.6}
\]

On the dyadic range

\[
 2^{-k-1}\sqrt m<n+1\le2^{-k}\sqrt m,
\]

the sum of (2.6) is

\[
 O\left(m^{-1/4}2^{7k/2}e^{-c4^k}\right).
\]

The series over \(k\) converges.  Combining this with (2.4) proves

\[
 \sum_{j\ge J}b_{m,j}
 \le
 CB_m\left((J+1)^{-1/2}+m^{-1/4}\right).          \tag{2.7}
\]

Taking \(J=\lceil(L-1)/2\rceil\) proves (0.2).  There is no missing
coefficient, endpoint mode, or rank range in this argument.

## 3. Audit of the two-colour charge

For a corner \(c=(a,b)\), the source charges

\[
 \chi_I(c)=
 \begin{cases}
  (D_{a-1},-),&a>0,\\
  (D_{s-b},+),&a=0.
 \end{cases}                                      \tag{3.1}
\]

There is no corner \((0,0)\), so the second case has \(b>0\).  Equations
(1.3)--(1.5) imply, when \(a+b\ge R\),

\[
 d(\phi D_{a-1})\ge2R-1
 \quad\text{or}\quad
 d(D_{s-b})\ge2R-1,                               \tag{3.2}
\]

according to the colour.

The injection is exact.

1. Within one interval, horizontal charges have distinct \(a\)-coordinates,
   hence distinct support roots \(D_{a-1}\).
2. There is at most one corner with \(a=0\).
3. The two colours distinguish that possible vertical charge from every
   horizontal charge.
4. Nonwrapping makes all support roots distinct within one return.
5. Quotient-edge-disjointness makes the support roots of different
   selected returns distinct.

Thus the signed charges are injective.  Since \(\phi\) permutes
\(\mathcal D_m\), the number of minus-colour roots satisfying (3.2) is
exactly \(\mathcal T_m(2R-1)\), as is the number of plus-colour roots.
This proves (0.1), including its factor two.

## 4. Audit of the critical sparse-corner conclusion

Suppose

\[
 \alpha\sqrt m\le s(I)\le A\sqrt m.
\]

Every corner satisfying

\[
 |c|_1\ge\rho s(I)
\]

has a charged sector of length at least

\[
 2\rho\alpha\sqrt m-1.
\]

Applying the same signed injection with this common threshold, then using
(0.2), proves (0.3).  If every member of a subfamily has at least
\(\eta s(I)\) such corners, division by
\(\eta\alpha\sqrt m\) gives

\[
 O_{\alpha,\rho,\eta}(B_m m^{-3/4})
 =o(B_m/\sqrt m).                                 \tag{4.1}
\]

For fixed \(\rho>0\), antichain distinctness of the first coordinates
gives

\[
 \#\{(a,b)\in\mathcal C(I):a+b<\rho s(I)\}
 \le\lceil\rho s(I)\rceil.
\]

Hence

\[
 \sum_I|\mathcal C(I)|
 \le
 \rho\sum_I s(I)+|\mathcal P_m|
 +C_{\alpha,\rho}B_m m^{-1/4}.                   \tag{4.2}
\]

If

\[
 |\mathcal P_m|\ge cB_m/\sqrt m,
\]

then

\[
 \sum_I s(I)\ge\alpha cB_m.
\]

After division in (4.2), the last two terms are respectively
\(O(m^{-1/2})\) and \(O_{\alpha,\rho,c}(m^{-1/4})\).  Therefore

\[
 \limsup_{m\to\infty}
 \frac{\sum_I|\mathcal C(I)|}{\sum_I s(I)}
 \le\rho.
\]

Letting \(\rho\downarrow0\) proves (0.4).  Since all durations are
comparable to \(\sqrt m\), this is equivalent to

\[
 \frac1{|\mathcal P_m|}
 \sum_I\frac{|\mathcal C(I)|}{s(I)}
 \longrightarrow0.
\]

Markov's inequality then supplies a deterministic
\(\varepsilon_m\downarrow0\) such that all but \(o(|\mathcal P_m|)\)
members obey

\[
 |\mathcal C(I)|\le\varepsilon_ms(I).
\]

Thus the sparse-corner conclusion has the claimed quantifiers.

## 5. Exact correction for the explicit strip family

In the audited common-edge strip family, the only nonempty outer blocks
are \(T_t\) and \(S_u\), both of length \(L\), and

\[
 \Lambda=L.
\]

Therefore

\[
 X_a=
 \begin{cases}
  0,&a\le t,\\
  L,&a\ge t+1,
 \end{cases}
\qquad
 Y_b=
 \begin{cases}
  0,&b<s-u,\\
  L,&b\ge s-u.
 \end{cases}
\]

By (1.1), a phase pair is nonoverlap exactly when at least one exceptional
block has entered the outer ledger.  The coordinate-minimal nonoverlap
pairs are therefore precisely

\[
 (t+1,0)
 \quad\text{and}\quad
 (0,s-u).
\]

Both lie in the triangular phase domain under the construction's cap
conditions.  This proves (0.5) and explains the source correction.

The family is still sparse-corner: it has two corners, hence \(O(1)=o(s)\)
in the Gaussian window.  Nothing in (0.1)--(0.4) changes.

## 6. Final boundary

The source validly proves that any critical-order quotient-edge-disjoint
packing has, after deleting a vanishing fraction of its intervals, only
\(o(s)\) minimal nonoverlap corridors per return.  The finite same-return
phase telescope then generates the complete nonoverlap atlas from these
sparse bases.

The argument does not bound returns with no nonoverlap corner, nor does it
force two sparse bases from different support-disjoint returns to collide.
Those are exactly the persistent-overlap and cross-interval incidence
gates left open by the source.
