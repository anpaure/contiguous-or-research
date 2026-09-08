# Audit: Catalan/C8 components versus the superpolynomial correlation scale

Date: 2026-07-26

Method: independent pure-mathematics audit. No computation, search, solver,
or web input is used.

Audited report:

`MATH_THEOREM_K_CATALAN_C8_COMPONENTS_VERSUS_SUPERPOLYNOMIAL_CORRELATION_SCALE_20260726.md`.

## 0. Verdict

The component censuses and their constants pass after the scope
qualifications now incorporated in the report.

At the critical height one must assume

\[
             H^2/m=\log m+o(1),
\]

not merely \(H=(1+o(1))\sqrt{m\log m}\). Then, with

\[
 R_m=\binom mH,
\]

the required correlation scale satisfies

\[
 \log R_m
 =\left(\frac12+o(1)\right)
    \sqrt m(\log m)^{3/2}.
\]

Both ambient Catalan mechanisms contain literal ownership components
larger than \(R_m\). The remaining obstruction is targetwise promotion
root-star alignment, not component cardinality.

## 1. MSW/PBBS hierarchy

For \(F_m\) versus \((2\ 3)F_m\), the exact side size and multiplicity
at level \(j\) are

\[
       s_j=C_j+C_{j+1},\qquad k_{m,j}=C_{m-j-2}.
\]

The unique top component has

\[
 \frac{s_{m-2}}{C_m}
 =\frac{C_{m-2}+C_{m-1}}{C_m}
 =\frac5{16}+o(1),
\]

so it exceeds \(R_m\) exponentially.

If

\[
 j_\star=\min\{j:C_j+C_{j+1}\ge R_m\},
\]

then

\[
 j_\star
 =\left(\frac1{4\log2}+o(1)\right)
    \sqrt m(\log m)^{3/2}.
\]

The exact number of qualifying components is

\[
       \sum_{j=j_\star}^{m-2}C_{m-j-2}.
\]

Their one-shore root mass is

\[
 \sum_{j=j_\star}^{m-2}
       (C_j+C_{j+1})C_{m-j-2}
 =\left(\frac58+o(1)\right)C_m.
\]

Indeed the complementary mass tends

\[
 \sum_{j\ge0}(C_j+C_{j+1})4^{-j-2}
 =\frac18+\frac14=\frac38.
\]

The ownership-component conclusion is literal because the two shores
partition the same complete resource block; it is not inferred from root
connectivity alone.

## 2. Extensive fixed-slot C8 cubes

For \(u\) disjoint slots, the eligible set \(J(x)\) is invariant under
the toggles and the component through \(x\) is exactly \(Q_{|J(x)|}\).
For each \(0\le h\le u\), inclusion--exclusion gives

\[
 K_{m,u}(h)=
 \binom uh\sum_{r=0}^{u-h}(-1)^r
       \binom{u-h}{r}2^rC_{m-2h-2r}.
\]

In particular there are \(C_{m-2u}\) all-active cubes of side \(2^u\).
The first possible dimension satisfying \(2^u\ge R_m\) is

\[
 u_\star
 =\left(\frac1{2\log2}+o(1)\right)
    \sqrt m(\log m)^{3/2}=o(m).
\]

At this minimal dimension the qualifying root mass is sparse:

\[
 \frac{2^{u_\star}C_{m-2u_\star}}{C_m}
 =R_m^{-3+o(1)}.
\]

For fixed linear \(u=\alpha m\), the Catalan moment census gives
\(|J(x)|=(\alpha/8+o(1))m\) on \(1-o(1)\) of the roots, so almost
all root mass then lies in components much larger than \(R_m\).

The cube is a genuine ownership component: every selected slab edge has
a unique transferred resource, fixed ports give diagonal edges, and no
resource edge leaves the toggle orbit.

## 3. Promotion-star scope

The block-factor theorem applies targetwise. If \(r_B(D)\) is the
intersection of block \(B\) with the provider star \(\mathcal R(D)\),
then, under independent blocks and uniform single-root frame marginals,

\[
 \Pr(D\text{ missed})
 \ge
 \exp\!\left(
   -\frac{R_mp_m}{1-p_m\max_Br_B(D)}
 \right).
\]

Thus an \(o(W)\)-hole product law needs almost every provider star to be
almost wholly contained in one block. A component of total size at least
\(R_m\) does not imply this hereditary property.

For the natural fixed-slot coordinate transport,

\[
 |\Gamma A\cap\mathcal R(D)|\le2^H,
\]

and the \(2m\) packet starts give at most

\[
                         2m\,2^H=o(R_m)
\]

direct providers in any star. Therefore the direct independent-component
controller, if it has the required uniform marginals, retains

\[
                    \mathbb EZ\ge(e^{-1}-o(1))W.
\]

This conclusion does not apply to a global mask, to rowwise ECAP packet
selection, or after several components controlling one promotion root are
merged into a global dependency block.

Finally, the \(\Omega(R_mm/H)\) ambient-row comparison is valid only
for disjoint ambient certificates across promotion rings; unrestricted
reuse remains part of the missing multirow braid.

## 4. Certified boundary

Certified:

1. raw MSW and C8 component size is not the obstruction;
2. the exact spectra and threshold constants in the main report are
   correct;
3. qualifying MSW components carry \((5/8+o(1))C_m\) roots;
4. natural fixed-slot C8 components are targetwise too thin for the
   independent promotion-root controller.

Open:

1. an incidence-preserving map from the root-scale MSW component to
   almost-monochromatic promotion provider stars;
2. a globally completed multirow braid with uniform promotion-frame
   marginals and nested all-depth traces; and
3. any constant-one conclusion from this lane.
