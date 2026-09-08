# Independent proof audit: Boolean-local eligible densities and coordinate-star containers

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_BOOLEAN_LOCAL_ELIGIBLE_DENSITY_COMPRESSION_AND_COORDINATE_STAR_GATE_20260804.md`  
**Verdict:** the deterministic eligible-density bounds, convex shifting
argument, Johnson-energy estimate, top-rank spectral classification, and
principal-star boundary comparison are correct.  Their scope is
deliberately partial: compression applies to the local first moment, not
to realized path cuts or their MGF, and only the unavoidable core of a
principal star is checked deterministically.  No computation is used.

## 1. Audit map

The note adds five unconditional statements to the preceding balanced-path
and random-path reductions.

1. It bounds a realized one-rank count \(e_s(Q)\) using the full eligible
   degree profile \(h_Q(S)\), not merely \(|Q|\).
2. It proves that every convex sum of eligible degrees increases under a
   standard set compression; hence the local hypergeometric first moment
   has a shifted maximizer.
3. It identifies a quantitative first-moment deficit as a weighted
   boundary across pairs of owners with large intersection.
4. It solves the half-density extremal problem at rank \(r-1\): coordinate
   halfspaces are the unique maximizers of the local benchmark.
5. It checks that the unavoidable core of every fixed-width principal
   coordinate star fits below the optimal depth, and that the coordinate
   halfspace has a strict local-benchmark margin.

None of these statements constructs one balanced path bank satisfying all
cuts.  The audit checks that no such inference is made.

## 2. Eligible-density sandwich

At a fixed rank, visitor blocks partition all \(W\) owner labels.  If a
block of size \(j\) is captured by \(Q\), then its target has at least
\(j\) eligible owners in \(Q\).  If \(x,y\) count captured blocks of the
two allowed sizes \(m_s,m_s+1\), respectively, then

\[
 x\le a_s,\quad y\le c_s,\quad
 x+y\le A_{m_s}(Q),\quad y\le A_{m_s+1}(Q),
\tag{2.1}
\]

and disjointness of the blocks gives

\[
                         m_sx+(m_s+1)y\le|Q|.          \tag{2.2}
\]

Thus the displayed two-variable integer program is a valid upper bound.
If \(h_Q(S)=D_s\), Boolean containment forces every visitor of \(S\) into
\(Q\), proving the lower bound.

For the complement \(R\), the occupancy
\(n_S=|V_s(S)\cap R|\) satisfies

\[
 \sum_Sn_S=|R|,\qquad
 n_S\le\min\{m_s+1,h_R(S)\}.                           \tag{2.3}
\]

If only \(j\) targets are hit, their capacities must sum to at least
\(|R|\).  Sorting capacities therefore proves
\(u_s(R)\ge\kappa_s(R)\), and
\(e_s(Q)=C_s-u_s(R)\) gives the second bound.  For \(R=\varnothing\),
the natural convention is \(\kappa_s(R)=0\).

**Audit conclusion:** Theorem 1.1 is an unconditional one-rank upper/lower
sandwich.  It is not asserted sharp and does not use cross-rank nesting.

## 3. Compression proof

Under an \((i,j)\)-shift, eligible counts of targets containing neither or
both coordinates do not change.  For a paired target
\(A\cup\{i\},A\cup\{j\}\), let \(p,q\) count owner fibres with occupancy
patterns \((1,0),(0,1)\).  The shift preserves the sum of the paired
eligible counts and changes the absolute difference from \(|p-q|\) to
\(p+q\).  The new pair therefore majorizes the old pair.  This proves

\[
 \sum_S\varphi(h_{C_{ij}Q}(S))
 \ge\sum_S\varphi(h_Q(S))                              \tag{3.1}
\]

for every discretely convex \(\varphi\).

The functions

\[
 (h)_\ell=\ell!\binom h\ell
\tag{3.2}
\]

are discretely convex because their second differences are nonnegative.
The local block probability \(g_s\) is a nonnegative linear combination
of two such functions, so the compression theorem follows.  Repeated
shifts preserve cardinality and terminate, giving a shifted maximizer.

The limitation recorded in the note is essential.  An indicator threshold
\(1_{h\ge m}\), the realized block count, and
\(\log(1+(z^w-1)g_s(h))\) are not covered merely because \(g_s\) is
convex.  Thus the theorem does not compress the deterministic Hall cut or
the switching MGF.

**Audit conclusion:** the downset reduction is valid exactly for the local
first-moment functional stated.

## 4. Johnson-local energy

For \(m_s=1\), direct algebra gives

\[
 \frac hD-g_s(h)=\frac{c_s}{C_s}
                   \frac{h(D-h)}{D(D-1)}.             \tag{4.1}
\]

For \(m_s\ge2\), both hypergeometric all-success probabilities in
\(g_s(h)\) are at most the two-draw probability.  Hence

\[
 \frac hD-g_s(h)\ge\frac{h(D-h)}{D(D-1)}.             \tag{4.2}
\]

Also

\[
 \sum_S\frac{h_Q(S)}D=\frac{C_s}{W}|Q|                \tag{4.3}
\]

by incidence double counting.  Summing (4.1) or (4.2) proves the stated
first-moment gap.

For the energy identity, expanding \(h_Q(S)(D-h_Q(S))\) chooses
\(T\in Q,U\notin Q\) with \(S\subseteq T\cap U\).  A fixed ordered
cross pair contributes exactly \(\binom{|T\cap U|}{s}\).  This verifies
the direction and absence of a factor two.

If every eligible count were \(0\) or \(D\), any two adjacent owners in
the Johnson graph would have the same membership because they share an
\(s\)-subset.  Connectivity then makes \(Q\) empty or full.  Thus the
gap is strict for every nontrivial family.

**Audit conclusion:** Theorem 3.1 is a correct local-energy strengthening
of the linear incidence bound.

## 5. Top-rank spectral classification

The adjacency eigenvalues of \(J(2r,r)\) are

\[
 \theta_j=(r-j)^2-j,
\tag{5.1}
\]

so the Laplacian eigenvalues are

\[
 \mu_j=j(2r-j+1).
\tag{5.2}
\]

The first positive eigenvalue is \(2r\).  Applying it to the centered
indicator of \(Q\) gives

\[
 |\partial_JQ|\ge2r|Q|(1-|Q|/W).                      \tag{5.3}
\]

Equality puts the centered indicator in the first eigenspace, whose
functions are affine coordinate sums on the slice.  A Boolean affine
coordinate sum can have only two coefficient levels separated by one.
Unless one level occurs on a singleton coordinate or its complement,
varying the number of selected high-level coordinates makes the function
take at least three values.  Therefore the only nonconstant Boolean
equality cases are a coordinate dictator and its complement.

At \(s=r-1\),

\[
 D=r+1,\qquad m=1,\qquad c/C=1/r,                      \tag{5.4}
\]

and each cross Johnson edge has one common \((r-1)\)-set.  Hence

\[
 \frac{C_{r-1}}W|Q|-\mathcal B_{r-1}(Q)
 =\frac{|\partial_JQ|}{r^2(r+1)}.                     \tag{5.5}
\]

Substitution of (5.3) gives the claimed inequality.  At \(|Q|=W/2\),
the deficit is at least

\[
                         \frac{W}{2r(r+1)},            \tag{5.6}
\]

with equality exactly for coordinate halfspaces.

**Audit conclusion:** coordinate halfspaces are rigorously classified as
the worst half-density families for this one local rank.  No all-rank
classification is inferred.

## 6. Principal-star boundary check

For \(Q_A=\{T:A\subseteq T\}\), every owner eligible for \(S\) lies in
\(Q_A\) exactly when \(A\subseteq S\).  If \(a\in A\setminus S\), there
are enough remaining coordinates to extend \(S\) to an \(r\)-owner while
omitting \(a\).  Thus the forced core is exactly the principal lower
star, of total size

\[
 K_t=\sum_{j=0}^{r-t-1}\binom{2r-t}j.                  \tag{6.1}
\]

Pascal's identity gives

\[
 K_t=2K_{t+1}+q_{t+1},\qquad
 q_{t+1}/q_t=(r-t)/(2r-t).                             \tag{6.2}
\]

For \(z_t=K_t/q_t\), this rearranges to

\[
 z_{t+1}=z_t-\frac12+\frac{tz_t}{2(r-t)}.              \tag{6.3}
\]

Since \(z_t=O(\sqrt r)\) for fixed \(t\), iteration gives

\[
 z_t=z_0-t/2+O_t(r^{-1/2}).                            \tag{6.4}
\]

The exact triangular depth definition and \(K_0=\Lambda+1\) give

\[
 d\ge z_0-\frac{\binom{d+1}{2}+1}{W}=z_0-o(1).       \tag{6.5}
\]

Therefore \(K_t<dq_t\) for each fixed \(t\ge1\) and all sufficiently
large \(r\).  Subtracting boundary cells only helps.  At \(t=1\), the
recurrence has no error and gives \(z_1=z_0-1/2\).

Finally, the local incidence benchmark on a halfspace is at most
\(N/2\).  The exact top-rank deficit (5.6), multiplied by its boundary
weight \(N_{r-1}/C_{r-1}\), gives the strict margin in the theorem even
when \(N=dW\).

**Audit conclusion:** the forced coordinate core and the conditional
local first moment are safe.  The proof does not upper-bound additional
captured targets in one deterministic path bank, and the theorem states
this caveat explicitly.

## 7. Final verdict

The audited note proves a sharp partial reduction:

\[
 \boxed{
 \begin{array}{c}
 \text{realized one-rank cuts admit Boolean-local density bounds;}\\
 \text{local first-moment extremizers may be shifted;}\\
 \text{the first-moment loss is a Johnson-local boundary energy;}\\
 \text{coordinate halfspaces are the exact top-rank half-density cases;}\\
 \text{their forced core and local benchmark pass at optimal depth.}
 \end{array}}
\tag{7.1}
\]

The missing theorem remains uniform multi-rank control of realized
visitor blocks, either through a compatible switching law plus containers
or through a deterministic expansion theorem.  No complete all-\(Q\)
Hall result, path bank, residual-conflict lift, or final compiler follows.
