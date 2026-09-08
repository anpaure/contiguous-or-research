# Protected transversal-lift role defect and the local orbit-absorption obstruction

**Date:** 2026-08-13  
**Status:** unconditional exact residual-role theorem and sharp
orbit-symmetry obstruction.  The protected lift creates a submiddle
point-role perturbation, but that perturbation cannot be implemented by any
signed combination of whole regular cyclic orbit blocks.  Any positive
construction must break orbit symmetry and use a genuinely nonuniform
core/support flow.  Integral named ordering remains open.

## 0. Setting

Put

\[
 k=2p+1,\qquad R=p+1,\qquad c=R-q,
 \qquad W={k\choose R},\qquad K={W\over k}=\operatorname {Cat}_p. \tag{0.1}
\]

Partition `[k]-{z}` into pairs `P_i={a_i,b_i}`.  Let `H` be a cyclic
Hamilton Gray code of `Q_p`, let `h_i` be its number of direction-`i`
transitions, and let `(Y,Z)` be the owner and lower shores of its
transversal lift.  Thus

\[
                         \sum_{i=1}^ph_i=2^p.          \tag{0.2}
\]

Every `h_i` is positive and even.

For a residual pure-rail shell bank, write

\[
 U_x=|\{j:x\in T_j\}|,
 \qquad
 K_x=\sum_{j:x\in C_j}N_j.                            \tag{0.3}
\]

These are respectively toggle-support degree and weighted core load.

## 1. Exact protected point loads

### Lemma 1.1 (lift shore degrees)

For every matched pair `P_i={a_i,b_i}`,

\[
 z_{a_i}=z_{b_i}=2^{p-1},                              \tag{1.1}
\]

\[
 y_{a_i}=y_{b_i}=2^{p-1}+{h_i\over2},                 \tag{1.2}
\]

while

\[
                         y_z=z_z=0.                    \tag{1.3}
\]

#### Proof

Among all cube vertices, each endpoint choice in pair `P_i` occurs in
exactly `2^(p-1)` transversal facets, giving `(1.1)`.  A direction-`i`
lifted owner contains both endpoints of `P_i`; every other lifted owner
contains the endpoint selected by its cube state.  The `h_i` direction
transitions split equally between entering and leaving each bit value on a
cycle.  Hence each physical endpoint gains `h_i/2` over its transversal
count, proving `(1.2)`.  The lift omits the sentinel. \(\square\)

### Theorem 1.2 (exact residual role targets)

If a pure-rail shell bank completes the protected lift exactly on the owner
and lower shores, then necessarily

\[
 \boxed{
 U_{a_i}=U_{b_i}=K-{h_i\over2},
 \qquad U_z=K,}                                       \tag{1.4}
\]

and

\[
 \boxed{
 K_{a_i}=K_{b_i}
 =cK-\left(2^{p-1}-{(q-1)h_i\over2}\right),
 \qquad K_z=cK.}                                      \tag{1.5}
\]

Conversely `(1.4)--(1.5)` are exactly the simultaneous residual
ground-point equations for the two shores.

The support and weighted-core defects relative to the uniform unprotected
role vector are therefore

\[
 d^T_{a_i}=d^T_{b_i}={h_i\over2},qquad d^T_z=0,       \tag{1.6}
\]

\[
 d^C_{a_i}=d^C_{b_i}
 =2^{p-1}-{(q-1)h_i\over2},qquad d^C_z=0.            \tag{1.7}
\]

They obey

\[
 \sum_xd_x^T=2^p,qquad
 \sum_xd_x^C=c\,2^p.                                  \tag{1.8}
\]

#### Proof

The two-shore residual equations are

\[
 K_x+qU_x={R\over k}W-y_x,
 \qquad
 K_x+(q-1)U_x={R-1\over k}W-z_x.                      \tag{1.9}
\]

Subtract and use Lemma 1.1 to obtain `(1.4)`.  Substitute back and use
`c=R-q` to obtain `(1.5)`.  Equations `(1.6)--(1.8)` follow from `(0.2)`.
\(\square\)

The perturbation is submiddle in total weight: `2^p=o(W)`.  It is not
bounded, and its coordinate profile records the full Gray direction vector.

## 2. Exact orbit-local obstruction

### Theorem 2.1 (whole-orbit no-go)

A full regular cyclic orbit block of any period has constant support degree
and constant weighted core load across all ground coordinates.  Therefore
every integer combination of whole orbit blocks has a constant role vector.
The protected defect `(1.6)--(1.7)` is nonconstant whenever the direction
counts `h_i` are not all equal, and it is zero at the sentinel but positive
on every paired coordinate.  Hence:

\[
 \boxed{
 \text{no trade using only whole regular cyclic orbit blocks can implement
 the protected residual roles.}}                       \tag{2.1}
\]

This remains true for an unbounded number of orbit blocks, arbitrary legal
periods, and signed real combinations.  Any protected construction must
break at least one orbit block into non-orbit shell choices or use a
genuinely nonuniform flow.

#### Proof

In an orbit block the regular `k`-cycle translates the base core and support
through every ground point equally often.  Role vectors add under signed
combination.  Thus their span consists only of constant vectors.  Equations
`(1.6)--(1.7)` are nonconstant because their sentinel coordinate is zero
and every `h_i>0`. \(\square\)

## 3. The exact nonuniform protected support flow

Fix prospective shell periods `N_j` with total residual period

\[
                         \sum_jN_j=W-2^p.             \tag{3.1}
\]

Choose actual cores `C_j`, `|C_j|=c`.  The required weighted core equations
are exactly

\[
                         \sum_{j:x\in C_j}N_j=K_x     \tag{3.2}

\]

with `K_x` from `(1.5)`.  After the cores are fixed, choose supports
`T_j subseteq[k]-C_j`, `|T_j|=N_j`, with point degrees `U_x` from `(1.4)`.

### Proposition 3.1 (exact protected Hall gate)

For fixed cores satisfying `(3.2)`, the required supports exist if and only
if, for every `X subseteq[k]`,

\[
 \boxed{
 \sum_{x\in X}U_x
 \le\sum_j\min\{N_j,|X-C_j|\}.}                       \tag{3.3}
\]

When `(3.3)` holds, an integral support assignment exists.

#### Proof

Use the bipartite network from shell tokens to ground points, retaining
exactly the core-disjoint incidences, with token degree `N_j`, point degree
`U_x`, and unit token--point capacities.  Equation `(3.3)` is its exact
capacitated Hall condition. \(\square\)

Thus protection does not create a new congruence: it creates a nonuniform
weighted-core degree-sequence problem `(3.2)` followed by the explicit Hall
system `(3.3)`.  The cyclic-orbit construction solves neither because it is
confined to constant role vectors.

## 4. Relation to integral named ordering

Even after `(3.2)--(3.3)` are solved, one must select one cyclic order per
shell so that every residual owner and every residual lower colour occurs
once and the protected shores are avoided.  These are the protected forms
of the two-shore ordering equations.  Their complete orbit relaxation has
owner--facet normalized codegree `2/R`, so the owner-only vanishing
collision argument does not apply.

The strongest current bridge is therefore exact but conditional:

\[
 \boxed{
 \text{solve }(3.2)\text{ and }(3.3)
 \quad\longrightarrow\quad
 \text{solve the protected two-shore order system}.}   \tag{4.1}
\]

Orbit-level local trades cannot perform the first arrow.  A genuinely
nonuniform core flow is required before any incidence-aware integral
ordering theorem can be invoked.

## 5. Scope

The theorem proves the exact protected role vector and a sharp symmetry
obstruction to whole-orbit absorption.  It does not solve the weighted core degree sequence,
the protected Hall system, the integral named-order system, upper support,
residence seams, source flags, or component fusion.
