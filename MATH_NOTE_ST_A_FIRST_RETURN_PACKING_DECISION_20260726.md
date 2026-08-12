# The Gaussian PBBS residence gate: exact first-return and packing decision boundary

Date: 2026-07-26

Method: pure mathematics only.  No computation, experiment, or external
input is used.

## 0. Verdict

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil ,
\]

where \(A>0\) is fixed.  Let \(\overline\nu_H\) be the maximum
quotient-edge-disjoint family of eligible PBBS residence intervals on the
quotient cycles of length greater than \(H+1\).

The statement

\[
 \boxed{\overline\nu_H=o_A(B_m/\sqrt m)}             \tag{ST_A}
\]

is **not presently proved or disproved by the cited PBBS residence
reductions**.  In particular, the local saturation theorem in
`MATH_AUDIT_CMS_AND_CRITICAL_RESIDENCE_SATURATION_20260726.md` is not a
global counterexample: its saturating inverse fibre has
\(\exp(o(m))\) roots and hence negligible Catalan mass.

There are two distinct missing asymptotics.

1.  If \(R_H\) denotes the number of genuine long-cycle roots which start
    an eligible first return, the exact inverse-fibre formula below does
    not currently yield an asymptotic for \(R_H\).
2.  Even an asymptotic for \(R_H\) does not determine the maximum packing.
    It is also necessary to control short-lag clustering of those roots
    along the actual PBBS quotient cycles.

The exact theorem proved here is the following decision boundary.  Put

\[
 \mathcal C_H=\sum_{t=1}^{H+1}
   |E_H\cap\tau^{-t}E_H|,                         \tag{0.1}
\]

where \(E_H\) is the set of eligible long-cycle roots and
\(R_H=|E_H|\).  Then

\[
 \boxed{
 {R_H^2\over R_H+2\mathcal C_H}
 \le \overline\nu_H\le R_H,}
                                                               \tag{0.2}
\]

and, without using any PBBS correlation,

\[
 \boxed{\overline\nu_H\ge {R_H\over 2H+3}.}       \tag{0.3}
\]

Consequently:

* if \(R_H/B_m\) has positive lower limit \(\rho_A\), then

  \[
   \liminf_{m\to\infty}
   {\sqrt m\,\overline\nu_H\over B_m}
   \ge {\rho_A\over2A}>0,                        \tag{0.4}
  \]

  and \((ST_A)\) is false;

* more sharply, if

  \[
   \liminf {\sqrt m R_H\over B_m}=\kappa_A>0,
   \qquad
   \limsup {\mathcal C_H\over R_H}\le\chi_A<\infty,
  \]

  then

  \[
   \boxed{
   \liminf {\sqrt m\,\overline\nu_H\over B_m}
   \ge {\kappa_A\over1+2\chi_A}>0,}             \tag{0.5}
  \]

  so \((ST_A)\) is again false;

* conversely, \((ST_A)\) implies \(R_H=o(B_m)\), and if
  \(R_H\ge c_AB_m/\sqrt m\), it forces

  \[
     \mathcal C_H/R_H\longrightarrow\infty.      \tag{0.6}
  \]

Thus a claimed negative answer must prove both a first-return lower bound
and a nonclustering estimate.  A claimed positive answer at critical start
density must prove divergent PBBS clustering.  Neither conclusion follows
from the reciprocal-height estimate, the minimal-return fixed-core normal
form, or the local inverse-fibre saturation.

## 1. Exact root-start census

For a normalized Dyck root \(D\in\mathcal D_m\), let \(G(D)\) be the
first positive odd return gap of its omitted physical coordinate.  An
eligible residence has

\[
 G(D)=2s+1,\qquad s+1\le H,
\]

and its full quotient trace contains \(s+2\le H+1\) consecutive
transition edges.

Let \(\partial D=F\in\mathcal D_d\), let
\(k=\operatorname {pk}(F)\), and let \(t\) be the terminal inverse
peak-insertion occupancy.  In the reduced PBBS rooted at \(F\), write

\[
 0<B_1(F)<B_2(F)<\cdots
\]

for the positive selection times of the immediate predecessor of the
distinguished equality particle.  The exact predecessor-passage theorem
gives, before the outer circumference,

\[
 \boxed{G(D)=B_{2t+2}(F).}                        \tag{1.1}
\]

For fixed \((F,t)\), the number of rank-\(m\) inverse lifts is

\[
 \boxed{
 K_m(F,t)=
 \binom{m+d-\operatorname {pk}(F)-t-1}{2d-1}.}   \tag{1.2}
\]

Therefore the total number \(R_H^{\rm all}\) of normalized roots which
start an eligible first return is exactly

\[
 \boxed{
 R_H^{\rm all}=\epsilon_m(H)+
 \sum_{d=1}^{m-1}\ \sum_{F\in\mathcal D_d}\ \sum_{t\ge0}
 \mathbf1_{\{B_{2t+2}(F)\le2H-1\}}
 \binom{m+d-\operatorname {pk}(F)-t-1}{2d-1},}   \tag{1.3}
\]

where \(\epsilon_m(H)\in\{0,1\}\) is the completely pruned exception.
This is the exact formula from the predecessor-occurrence reduction; it
is not a relaxation.

The short-cycle deletion does not affect any polynomial Catalan
normalization.  If \(Z_H\) is the number of quotient roots on cycles of
length at most \(H+1\), voltage-itinerary rigidity gives

\[
 Z_H\le(2H+2)N^{2H+2}
     =\exp(O_A(\sqrt m\log m)).                   \tag{1.4}
\]

Since \(B_m=\exp(m\log4-O(\log m))\), for every fixed \(K\),

\[
 Z_H=o(B_m/m^K).                                  \tag{1.5}
\]

Hence

\[
 R_H=R_H^{\rm all}+o(B_m/m^K)                    \tag{1.6}
\]

at all scales relevant here.  The unresolved part of (1.3) is precisely
the dynamic predicate
\(B_{2t+2}(F)\le2H-1\).  Marginal Dyck height, peak count, or the
one-step deficit distribution does not evaluate it.

There is an equivalent exact slope formulation.  Let \(M_s\) be the
number of normalized consecutive omitted-label gaps \(2s+1\), and let

\[
 \mathcal E_q=\sum_{s\ge1}(q-s)_+M_s
\]

be the PBBS rank-excess potential.  Discrete differentiation gives

\[
 \boxed{
 R_H^{\rm all}=\sum_{s\le H-1}M_s
              =\mathcal E_H-\mathcal E_{H-1}.}    \tag{1.7}
\]

Thus the start census is the *slope* of rank excess, not its value.  The
known nonnegativity and moment bounds for \(\mathcal E_q\) do not supply
the Gaussian-scale slope asymptotic required here.

## 2. Root starts are not a packing

Construct the conflict graph \(G_H\) whose vertices are the roots in
\(E_H\), joining two roots precisely when their actual quotient traces
share an edge.  By definition,

\[
 \alpha(G_H)=\overline\nu_H.                     \tag{2.1}
\]

Every trace has at most \(H+1\) consecutive edges and is nonwrapping.
If two traces overlap, then, in one cyclic direction, their roots differ
by \(\tau^t\) for some \(1\le t\le H+1\).  Consequently

\[
 |E(G_H)|\le\mathcal C_H.                         \tag{2.2}
\]

For every finite graph with \(R\) vertices and \(C\) edges, the
Caro--Wei bound and Cauchy--Schwarz give

\[
 \alpha(G)\ge\sum_v{1\over d(v)+1}
 \ge {R^2\over R+2C}.                            \tag{2.3}
\]

Equations (2.1)--(2.3) prove the lower bound in (0.2).

For the correlation-free estimate, each summand in (0.1) is at most
\(R_H\), so

\[
 \mathcal C_H\le(H+1)R_H.                       \tag{2.4}
\]

Substitution into (0.2) proves (0.3).  The upper bound in (0.2) is
immediate because every packed interval has a distinct start.

This also proves all the asymptotic consequences (0.4)--(0.6).  For
(0.6), substitute \(R_H\ge c_AB_m/\sqrt m\) into (0.2).  If
\(\mathcal C_H/R_H\) remained bounded on a subsequence, the normalized
packing would have a positive lower bound, contrary to \((ST_A)\).

## 3. Why a one-point asymptotic cannot decide the theorem

The distinction is not cosmetic.  Abstract interval systems on cycles
can have the same number \(R\) of starts and opposite packing behaviour.

* If the starts are separated by more than \(H+1\) edges, all intervals
  are disjoint and \(\nu=R\).
* If the starts are arranged in well-separated blocks of \(H+1\)
  consecutive positions and all intervals in a block have length
  \(H+1\), then each block contributes only one packed interval and
  \(\nu\asymp R/H\).

Thus even a theorem

\[
 R_H\sim\kappa_A B_m/\sqrt m                    \tag{3.1}
\]

would not by itself refute \((ST_A)\).  With bounded short-lag clustering
it gives the positive liminf (0.5); with clusters of diverging mean size it
can coexist with a little-oh packing.  Conversely, counting roots at a
fixed phase is not a substitute for maximizing an edge-disjoint family.

## 4. The local saturation theorem does not globalize

The mountain-core inverse fibre in
`MATH_ATTACK_U_QUOTIENT_CHRONOLOGY_SATURATION_20260725.md` has, for
\(h\asymp\sqrt m\),

\[
 P_{m,h}=\binom{m+h-2}{2h-2}
          =\exp(O(\sqrt m\log m))=\exp(o(m)).     \tag{4.1}
\]

Inside that fibre there is a genuine first-return packing of size

\[
 \left({1-e^{-4c^2}\over2c}+o(1)\right)
 {P_{m,h}\over\sqrt m},                          \tag{4.2}
\]

occupying the fraction

\[
 {1-e^{-4c^2}\over2}                             \tag{4.3}
\]

of its reciprocal-height capacity.  Equations (4.1)--(4.3) rigorously
refute any uniform fibrewise contraction.  But (4.1) is
\(o(B_m/m^K)\) for every fixed \(K\), so summing this one fibre, or all
bounded-period reduced-core fibres covered by the existing
\(3^m\)-capacity estimate, cannot give a positive lower limit in (0.4) or
(0.5).

Likewise, the factor-two minimal-return theorem only replaces arbitrary
returns by simple fixed-core sectors.  It preserves packing size up to an
absolute constant but supplies neither a lower bound for \(R_H\) nor an
upper bound for \(\mathcal C_H\).

## 5. Exact conclusion

The rigorous present conclusion is therefore:

\[
 \boxed{\text{The truth value of }(ST_A)\text{ remains open.}} \tag{5.1}
\]

The shortest analytic routes to a decision are now exact.

* To prove **false**, it is enough to establish, for one fixed \(A>0\),

  \[
   R_H\ge\kappa_AB_m/\sqrt m,
   \qquad \mathcal C_H\le\chi_AR_H,              \tag{5.2}
  \]

  with \(\kappa_A>0\) and \(\chi_A<\infty\); then (0.5) gives the
  explicit positive liminf \(\kappa_A/(1+2\chi_A)\).

* To prove **true** at a critical one-point scale, it is necessary to
  prove the divergent clustering law (0.6), and then still to convert
  that clustering into an upper bound for the maximum independent set.

Neither (5.2) nor the required positive-direction clustering theorem is
contained in the cited reductions.  Treating finite-rank census data as
an asymptotic, or identifying eligible root starts with an edge-disjoint
packing, would therefore be a mathematical error.
