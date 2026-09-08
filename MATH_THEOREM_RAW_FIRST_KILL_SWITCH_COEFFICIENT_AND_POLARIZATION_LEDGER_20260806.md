# Raw first-kill switch coefficient and the polarization ledger

> **RETRACTED LINEAGE -- DO NOT CITE.**  Independent audit found that this
> draft identifies the coordinate-switched covariance candidates with the
> two future-potential square edges.  Those are different roles.  It also
> replaces the full changed-resource set of `C-tau C` by the subset met by
> the earliest blocker.  Sections 2--5 therefore do not prove their stated
> conclusions.  The corrected result is
> `MATH_THEOREM_RAW_SWITCH_FOUR_ROLE_COEFFICIENT_AND_UNANCHORED_CHANGE_OBSTRUCTION_20260806.md`.

**Date:** 2026-08-06  
**Method:** exact hypothetical-survivor coefficients, a Hilbert-space
polarization inequality, and the earliest-blocker partition; no computation
or search  
**Status:** closes the coefficient mismatch in the raw (unconditioned)
Johnson-switch argument.  It does not compare future fugacities with an
arbitrary separator-cylinder Doob transform.  That comparison is no longer
needed for the bottom/Haxell use after the annealed quarantine composition.

This note uses the notation of
`MATH_THEOREM_RANK_COMPENSATED_DOUBLET_CLOCK_AND_ROOTED_OVERLAP_REDUCTION_20260806.md`
and
`MATH_THEOREM_ADAPTIVE_JOHNSON_BELLMAN_VALUE_AND_EQUIVARIANT_HIDING_OBSTRUCTION_20260806.md`.

## 1. Hypothetical-survivor coefficient

At the pre-transition state `i`, let `E` and `F` be available atomic
doublets and let `Q` be a live pair root contained in both.  Recall

\[
 c_i(Q,E,F)=\xi_{E,i}\xi_{F,i}
 \left({p_i\over p_*}\right)^{m_N(E,F;Q)}
 \left({p_{s,i}\over p_{s,*}}\right)^{m_S(E,F)}.
\tag{1.1}
\]

If both `E,F` survived the next accepted doublet, their next coefficient
would be

\[
                 c_i^+(Q,E,F)=c_i(Q,E,F)R_i(E,F;Q).
\tag{1.2}
\]

This is the exact identity `(FP6)` in the parent note.  It is a
counterfactual coefficient: it is defined even on a transition which in
fact kills one of `E,F`.

Let

\[
 \widetilde c_i^+(Q,E,F)=\xi_{E,i}^+\xi_{F,i}^+
\tag{1.3}
\]

be the corresponding **bare** post-rescaling product, with both edges
hypothetically retained.  Since `p_(i+1)>=p_*` and
`p_(s,i+1)>=p_(s,*)`,

\[
 \boxed{\widetilde c_i^+(Q,E,F)\le c_i^+(Q,E,F).}
\tag{1.4}
\]

The same assertion holds for the one-root coefficient in (1.5) of the
joint-Lyapunov note and for every fixed marked entry pattern: the omitted
factor is a product of future-survival ratios, all at least one.

### Lemma 1.1 (a live coordinate switch has equal coefficients)

Let `tau` be a coordinate transposition and put `F=tau E`.  While both
`E,F` are available,

\[
 \boxed{
   \omega_F=\omega_E,\qquad a_F(i)=a_E(i),\qquad
   \xi_{F,i}=\xi_{E,i}.}
\tag{1.5}
\]

Their hypothetical post-rescaling coefficients are equal as well.  If a
root or marked pattern is carried by `tau`, its future-fugacity coefficient
is unchanged.

#### Proof

The host is a complete coordinate orbit.  A coordinate transposition
preserves the orbit, the multiplicity `h`, every non-slot and slot count,
and the base weight.  The compensation in (2.1) of the parent note depends
only on those counts and on the two deterministic densities.  This proves
(1.5).  Intersection and union cardinalities are also coordinate
invariants, proving the last assertion.  \(\square\)

Thus there is no coefficient imbalance before a switch boundary is born.

## 2. The first-kill coefficient is already in the future potential

Let `G` be the doublet accepted at transition `i`.  Suppose

\[
              E\cap G=\varnothing,
              \qquad F\cap G\ne\varnothing.
\tag{2.1}
\]

The transition probability is `a_G(i)/X(i)`.  Define the true bare
switch-birth coefficient by

\[
 b_i(Q,E,F;G)=
 {a_G(i)\over X(i)}\widetilde c_i^+(Q,E,F).
\tag{2.2}
\]

This is exactly the coefficient multiplying the post-rescaling boundary
quadratic form: `E` is present and the hypothetical mate `F` is absent.

### Theorem 2.1 (raw first-kill domination)

For every transition satisfying (2.1),

\[
 \boxed{
 b_i(Q,E,F;G)
 \le {a_G(i)\over X(i)}
       c_i(Q,E,F)R_i(E,F;Q).}
\tag{2.3}
\]

The coefficient on the right is precisely the coefficient of the
`(Q,E,F)` cross-term which is lost from the next future-overlap potential
when `G` kills `F`.  There is no extra density, time, or cylinder factor.

#### Proof

Multiply (1.4) by the transition probability.  If both edges survived,
their term in the next potential would have coefficient `c_iR_i` by
(1.2).  On (2.1) it is absent, so this same coefficient occurs with a
negative sign in the one-step drift.  \(\square\)

Now take `F=tau E`.  By the earliest-blocker decomposition (1.14) in the
adaptive-Bellman note, every oriented boundary has a unique transition at
which (2.1) first holds.  Before that transition both candidates are live,
so Lemma 1.1 applies.  Consequently (2.3) charges every boundary birth once
and only once.  The future fugacity is not being compared to the law of the
first blocker: it is the exact coefficient of the killed hypothetical
survivor.

## 3. Polarization uses the killed mate before any static injection

Let `R` be the pristine positive-semidefinite Johnson resolvent and write
`||z||_R^2=<z,Rz>`.  The elementary inequality

\[
 \boxed{
 [\|u\|_R^2-\|v\|_R^2]_+
 \le \|v\|_R^2+2\|u-v\|_R^2}
\tag{3.1}
\]

holds for all `u,v`.

Indeed, with `delta=u-v`,

\[
 \|u\|_R^2-\|v\|_R^2
 =2\langle v,R\delta\rangle+\|\delta\|_R^2
 \le \|v\|_R^2+2\|\delta\|_R^2.
\tag{3.2}
\]

At a first kill, take `u` to be the surviving switch functional and `v`
the transposed mate.  The first term on the right of (3.1), with the
coefficient (2.3), is paid by the diagonal future-potential term killed
with `F`.  Only the switch Dirichlet energy

\[
                         \|u-v\|_R^2
\tag{3.3}

remains.  This is the precise signed advantage over the absolute
`(JRES)` estimate: the large symmetric part is paid at the unique kill and
is not occupied at every later stopped state.

For a complete transposition orbit, the average of (3.3) is exactly

\[
       2\alpha_q\langle z,Bz\rangle
\tag{3.4}
\]

by Theorem 1.3 of the adaptive-Bellman note.  Hence no inverse Johnson-gap
factor remains in the boundary injection.

## 4. Exact first-entry split

For a first-kill tuple put

\[
 J(G;E,F)=(G\cap(F-E))\cap
             (\mathcal L\mathbin{\dot\cup}\mathcal R),
 \qquad j=|J(G;E,F)|.
\tag{4.1}
\]

All non-slot blockers lie here because `E cap G` is empty.  Each
`x in J` is `tau y` for a unique changed resource `y in E-F`, and `(x,y)`
is one Johnson edge.  Slot-only terms remain in the separate slot ledger.

Write the switch innovation as a sum of its changed-resource innovations,

\[
                         z=\sum_{x\in J}z_x.
\tag{4.2}
\]

Its resolvent energy has the exact expansion

\[
 \|z\|_R^2=
   \sum_{x\in J}\|z_x\|_R^2
   +2\sum_{\{x,y\}\subseteq J}\langle z_x,Rz_y\rangle.
\tag{4.3}
\]

The diagonal terms are one-entry terms.  The resistance identity (1.5) of
the adaptive-Bellman note removes the resolvent on each of them.  With
coefficient (2.3), their first-entry map is exactly the rooted-overlap
injection used in `(ROc)`.  The earliest-blocker restriction can only
delete nonnegative rooted tuples, so `(ROc)` pays their total.

For the correlated terms, use

\[
 2|\langle z_x,Rz_y\rangle|
 \le\|z_x\|_R^2+\|z_y\|_R^2.
\tag{4.4}

Every such term is indexed by an unordered first-two-hit pair
`{x,y} subseteq G cap(E union F)`.  After the `E,F` future coefficient is
inserted, the density change of variables in `(FP9)`, together with the
already proved global-rate reconstruction, bounds the selection-time sum
by `1+o(1)` times the complete-host kernel

\[
                         K_{p_*}(j)=\int_{p_*}^1p^{2-j}\,dp
\tag{4.5}

from `(FE3.2)`.  Moreover

\[
 { |J(G;E,F)|\choose2}
 \le {j(G;E,F)\choose2}.
\tag{4.6}

Thus the map

\[
 (Q,E,F,G,\{x,y\})
 \longmapsto (Q,E,F,G,\{x,y\})
\tag{4.7}

is coefficient-preserving before the harmless global-rate factor, and is
an injection into the summands of `(FE3.3)`.  This is
termwise, so the fact that two hits determine the same coordinate
transposition causes no independence loss.  Proposition `(FE3)` pays the
whole correlated part, with its spare factor `1/d`.

Equations (4.3)--(4.7) also apply to the finitely many size-two and
size-three marked patterns, using the cluster-rooted versions (6.6) and
(7.3) of the joint-Lyapunov note.

## 5. Consequence for the raw bottom estimate

The unweighted switch-boundary ledger now has no unpriced coefficient:

1. internal live switch pairs use the exact complete-orbit cancellation;
2. the symmetric part at a first kill is paid by the killed diagonal term;
3. the remaining one-entry switch energy injects into `(ROc)`;
4. every correlated multiple-entry term injects termwise into `(FE3)`;
5. every switch pair has at most one positive boundary birth.

Together with the already proved root/owner/slot and marked-entry ledgers,
the raw one-sided Bellman value has the required scale

\[
                         V(S_0)=O(M/d^4).
\tag{5.1}

Therefore the parent stopped-transfer chain gives `(DROOT)`, `(ASE)`, and
`(AIB)`, and Proposition 7.1 of the rank-compensated note yields

\[
 \boxed{\mathbb E(B_0+B_1)=O(M/d^2).}
\tag{5.2}

By the annealed quarantine--Haxell theorem, no separator-cylinder
`h`-transform comparison is needed for this bottom use.

## 6. Scope

This theorem is about the raw selected-relation/quarantine architecture.
It does not prove a weighted `(JCYL)` estimate for an arbitrary terminal
event, and it must not be used to claim that a terminally conditioned clean
law retains hereditary cylinders.  It also does not address terminal
component joining, the PBBS payload bridge, or the odd-dimensional
reservoir.
