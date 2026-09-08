# Relative fan holonomy, pure-gauge lock, and triangular-deck stabilizers

**Date:** 2026-08-05  
**Method:** complete-state transport and framed monodromy; no computation or search  
**Status:** corrected unconditional algebraic reduction.  This file supersedes
the earlier signed-frame calculation.  Physical strand transport and internal
fan voltage are distinct actions.  Absolute frame signs cannot cancel the
internal voltage; a useful fused macro needs a genuinely nongauge actuator, or
a planted deck stabilized by the residual voltage.

## 1. Two actions which must not be identified

At every positive clean-`C6` site the physical old-cycle tag is translated by

\[
                         \tau=(0\ 1\ 2).                 \tag{1.1}
\]

Independently, after factoring out that pure tag transport, the diagonal-to-
shifted fan rethread has a normalized relative action `r`: it shifts the left
history index while the central/right index is held fixed.  The q3 flag deck
already distinguishes `r` from `tau`.

For `k` aligned positive sites, the raw complete-state holonomy `H` has tag
projection `tau^k`.  Consequently

\[
                         H=I\quad\Longrightarrow\quad3\mid k. \tag{1.2}
\]

Raw pointwise identity is therefore incompatible with topology fusion, which
requires `3` not dividing `k`.  The correct zero-current condition is deck
invariance after the unavoidable tag permutation is factored out.

## 2. Correct relative holonomy

Assume a literal pure-tag transport `widehat tau` has been fixed, and define

\[
                         \overline H=\widehat\tau^{-k}H. \tag{2.1}
\]

Let `Xi` be the planted complete occurrence-labelled fan bank and let
`mathcal D(Xi)` be its full triangular target deck.  Serial site currents are
coboundaries, so their transported sum is

\[
                         \mathcal D(H\Xi)-\mathcal D(\Xi). \tag{2.2}
\]

Hence a macro has zero complete fan current whenever

\[
                         \mathcal D(H\Xi)=\mathcal D(\Xi), \tag{2.3}
\]

or equivalently whenever `overline H` lies in the stabilizer of the planted
deck under the declared pure-tag identification.  Relative identity
`overline H=I` is a strong sufficient condition, not a necessary one.

## 3. Pure frame changes do not alter the relative exponent

Let the normalized internal action of a coherent site be `r`.  Choose an
absolute active frame `phi_s` at site `s`.  In a common ambient notation its
relative site action is

\[
                         R_s=\phi_s r\phi_s^{-1}.         \tag{3.1}
\]

If the path to the next site merely changes frames, its relative transport is

\[
                         E_s=\phi_{s+1}\phi_s^{-1}.       \tag{3.2}
\]

With cyclic indexing `phi_k=phi_0`, all intermediate frames telescope:

\[
 (E_{k-1}R_{k-1})\cdots(E_0R_0)
   =\phi_0r^k\phi_0^{-1}.                               \tag{3.3}
\]

Thus a formal sign word such as `(+,+,-,-)` does not give exponent zero.
Calling a site reflected changes gauge and is undone by the intersite frame
map.  A different exponent requires a literal nongauge history actuator.

If coherent `r` has order three and is visible on the planted deck, pure-gauge
sites have relative pointwise return only for `3|k`; aligned topology fuses
only for `3` not dividing `k`.  This is the corrected coherent monodromy lock.

## 4. Exact triangular-deck stabilizer

Let the left and right histories be

\[
 \mathcal L_i=(L_i(u))_u,\qquad
 \mathcal R_i=(R_i(v))_v,
\]

and, on the affected triangular index set `Omega`, put

\[
 M_{ij}=\sum_{(u,v)\in\Omega}[L_i(u)\cap R_j(v)].        \tag{4.1}
\]

The old diagonal deck is `D_id=sum_i M_ii`.  A relative permutation `pi` of
left histories gives `D_pi=sum_i M_(pi(i),i)`.  Therefore

\[
 \operatorname{Stab}_{\rm multi}(M)
 =\left\{\pi\in S_3:
          \sum_iM_{\pi(i),i}=\sum_iM_{ii}\right\}.      \tag{4.2}
\]

If the cells `(i,u,v)` are occurrence-addressed, the exact stabilizer is

\[
 \operatorname{Stab}_{\rm occ}(M)
 =\left\{\pi:
 L_{\pi(i)}(u)\cap R_i(v)=L_i(u)\cap R_i(v)
 \text{ for every }i,(u,v)\in\Omega\right\}.            \tag{4.3}
\]

The occurrence version must be used whenever compiler addresses or protected
paths are load-bearing.

## 5. The q3 diagnostic

For a q2-neutral clean `C6`, let `d` be the common first deletion and `e_i`
the second-deletion flag.  The q3 left-only deck is

\[
                         \sum_i[K-\{d,e_i\}+a_i].        \tag{5.1}
\]

Because each term contains its unique active label `a_i`, its stabilizer is

\[
 \left\{\pi\in S_3:e_{\pi(i)}=e_i\text{ for every }i\right\}. \tag{5.2}
\]

Thus a coherent cyclic relative shift is q3-invisible exactly when all three
flags agree.  The complete triangular deck imposes the analogous condition at
every deeper history coordinate.

## 6. Reflection is not the missing actuator

Active reflection sends the old clean shore to the new shore and conversely;
it reverses physical phase together with history indexing.  The two owner
families cannot be restored by a coordinate automorphism because

\[
                         \bigcap_iP_i=K,
 \qquad                  \bigcap_iQ_i=K+c               \tag{6.1}
\]

have different ranks.  PBBS spatial reversal likewise conjugates the positive
map to its inverse and reverses physical voltage.  Neither operation supplies
an inverse **relative** actuator while retaining positive physical voltage.

## 7. Correct remaining local target

The smallest aligned fusion count is `k=2`.  Its raw tag action is `tau^2`,
so raw `H=I` is impossible.  After tag normalization, a two-site solution
requires

\[
                         \overline T_1\overline T_0=I,   \tag{7.1}
\]

or membership of this product in the planted triangular-deck stabilizer.
Two coherent copies joined only by frame transport give `r^2`, not identity.

A four-site fusion is a fallback only after a separate theorem rules out every
literal two-site nongauge inverse.  The formal frame word `(+,+,-,-)` is not
such a theorem.

Thus the exact unresolved object is a positive aligned site family whose
tag-normalized complete-history product stabilizes the planted occurrence
deck.  Owner labels, both histories, q2 halos, residence, source contexts, and
the compiler occurrence map must all participate in that same product.

## 8. Scope

Proved here:

1. raw tag projection `tau^k` and the incompatibility of raw identity with
   fusion;
2. the exact tag-normalized deck-stabilizer criterion;
3. pure-gauge telescoping to `phi_0 r^k phi_0^-1`;
4. the exact multiset and occurrence triangular-deck stabilizers; and
5. the q3 equal-flag diagnostic and the reflection no-go.

Not proved:

1. a literal nongauge inverse actuator;
2. a two- or four-site complete-state-returning PBBS macro;
3. simultaneous residence/source/common-cap planting; or
4. any unconditional all-`k` upper bound.

This corrected statement agrees with
`MATH_THEOREM_PBBS_ALIGNED_KSITE_FUSION_AND_FAN_HOLONOMY_GATE_20260805.md`
and
`MATH_AUDIT_PBBS_ALIGNED_KSITE_RAW_TAG_AND_RELATIVE_HOLONOMY_20260805.md`.
