# Aligned multi-site `C6` fusion and the exact fan-holonomy gate

**Date:** 2026-08-05  
**Method:** cut-path permutation calculus and complete-state transport; no
computation or search  
**Status:** corrected unconditional topology/relative-holonomy reduction.
Raw pointwise state return is incompatible with fusion once physical
occurrence tags are retained.  The usable condition is identity of the
tag-normalized relative holonomy, or more generally invariance of the
complete planted deck.  Existence of the required nongauge PBBS actuator is
not asserted.

**Correction notice.**  The first version used `H=I` while simultaneously
including physical old-cycle tags in the state.  But the tag projection of
`H` is translation by `k` in `Z_3`; hence raw `H=I` forces `3|k`.  It also
multiplied active-frame signs without the intersite gauge maps.  The
correct equations below follow
`MATH_AUDIT_PBBS_ALIGNED_KSITE_RAW_TAG_AND_RELATIVE_HOLONOMY_20260805.md`.

## 1. Aligned sites on three cycles

Let `C_0,C_1,C_2` be three directed cycles.  On each `C_i` choose `k`
directed edges

\[
 e_{i,0},e_{i,1},\ldots,e_{i,k-1}
\]

in this cyclic order, with pairwise disjoint supports.  At every site `j`
perform the same positive clean-`C6` reconnection

\[
 \operatorname{tail}(e_{i,j})\longmapsto
 \operatorname{head}(e_{i+1,j}),
 \qquad i\in\mathbb Z_3.                         \tag{1.1}
\]

### Theorem 1.1 (aligned `k`-site topology)

The reconnected factor has exactly

\[
                         \boxed{\gcd(3,k)}          \tag{1.2}
\]

cycles on the union of the three old cycles.  In particular it is one
cycle if and only if `3` does not divide `k`.

#### Proof

Cut all `3k` edges.  Let `P_(i,j)` be the old directed path on `C_i` from
the head at site `j` to the tail at site `j+1`, with site indices modulo
`k`.  After traversing `P_(i,j)`, reconnection (1.1) enters
`P_(i+1,j+1)`.  After one full circuit through the `k` site positions, the
cycle index has advanced by `k` in `Z_3`.  Thus the return action on the
three possible cycle indices is translation by `k`, which has
`gcd(3,k)` orbits.  The paths `P_(i,j)` partition the old cycles, so there
are no additional orbits. `square`

For `k=1,2,4,5,...` with `3` not dividing `k`, this is a fusion.  For
`k=3`, three coherent sites close their local order-three phase but return
three cycles; this is the first monodromy lock.

## 2. Complete fan state

At a cut occurrence retain the complete data needed to evaluate every
named whole-fan path meeting that cut:

\[
 \Omega=(R,(A(u))_{u\ge0},(B(v))_{v\ge0},\text{occurrence tags}), \tag{2.1}
\]

where `R` is the central q1 row and `A(u),B(v)` are the truncated left and
right intersection histories.  A clean `C6` site, together with its
declared complete context transport, is a bijection between the three
incoming state fibres and the three outgoing state fibres.  Denote that
map by

\[
                         S_j:\Omega_j\longrightarrow\Omega'_j. \tag{2.2}
\]

The old-to-new target current at the site is exactly the difference of the
two triangular decks

\[
 {\cal D}(\Omega)
 =\{A(u)\cap B(v):u,v\ge0,\ u+v<m\},              \tag{2.3}
\]

with the correct-rank and named-occurrence restrictions retained.  This is
the diagonal-to-shifted pairing law of the selected-edge puncture theorem.

Let

\[
 E_j:\Omega'_j\longrightarrow\Omega_{j+1}         \tag{2.4}
\]

be the literal transport along the three path segments between sites `j`
and `j+1`.  It includes actual coordinate labels, path orientation, and
occurrence tags; equality merely of rank histograms is insufficient.

Put `T_j=E_jS_j`.  If `p` is the physical old-cycle tag, positivity of the
site and transport within the receiving old cycle give

\[
                         p(T_j\omega)=p(\omega)+1.       \tag{2.5}
\]

### Theorem 2.1 (raw tag and deck-stabilizer criterion)

Put

\[
 H=(E_{k-1}S_{k-1})\cdots(E_1S_1)(E_0S_0).         \tag{2.6}
\]

Its physical tag projection is translation by `k` in `Z_3`.  In
particular,

\[
                         H=I\Longrightarrow3\mid k.      \tag{2.7}
\]

Let `Xi_0` be the planted bank of the three incoming complete states.  The
aligned replacement has zero signed current whenever

\[
                         {\cal D}(H\Xi_0)
                         ={\cal D}(\Xi_0)                \tag{2.8}
\]

under the declared terminal occurrence identification.  Thus raw identity
is sufficient but is not necessary: a deck-preserving permutation of the
three complete state occurrences is allowed.

If the aligned typing supplies a literal pure-tag map `widehat tau`, define

\[
                         \overline H
                         =\widehat\tau^{-k}H.             \tag{2.9}
\]

Then `bar H=I` is a strong sufficient condition for (2.8).  A nonidentity
relative action on a visible independently labelled coordinate obstructs
universal pointwise return, but it can be harmless on a specially
symmetric planted deck if it lies in that deck's stabilizer.

#### Proof

Equation (2.5) iterated `k` times proves (2.7).  The site currents are
complete-state coboundaries.  Transporting them through the `E_j` maps
telescopes every intermediate deck and leaves

\[
                         {\cal D}(H\Xi_0)-{\cal D}(\Xi_0).
\]

This is zero under (2.8).  If `bar H=I`, the raw terminal action is only
the declared pure-tag permutation, which preserves the planted deck.
Complementing every intersection path gives the paired upper statement.
`square`

The theorem does not say that support might not be rescued elsewhere.
Equation (2.8), rather than raw pointwise identity, is the exact condition
for complete-state telescoping on the planted bank.

## 3. Coherent lock and the first noncoherent candidates

For the coherent resident converter, every site has the same normalized
order-three relative action `sigma`.  Flat path transport gives

\[
                         \overline H\sim\sigma^k.   \tag{3.1}
\]

Thus coherent **relative** pointwise return requires `3|k`.  Theorem 1.1
then gives three cycles, not one.  This proves:

### Corollary 3.1 (coherent relative-monodromy lock)

No number of identically typed aligned clean-`C6` sites with only
pure-gauge intersite frame transport can both return every independently
visible relative fan coordinate and fuse the three cycles.

The smallest possible escape under the corrected relative criterion is
already `k=2`, the aligned double ear.  It would require two genuinely
**nongauge** normalized transitions satisfying

\[
                         \overline T_1\overline T_0=I. \tag{3.2}
\]

Raw pointwise `H=I` is impossible here because its tag projection is
`tau^2`.

The reflected phase-balanced two-copy theorem does not supply this object:
under its set-identical/cross-context hypotheses the complete cycle type is
preserved, and disjoint relabelled copies preserve values only up to a
coordinate permutation.  That theorem is a sharp no-go for one natural
two-site realization, not for every longitudinal state-returning aligned
double.

Nor does merely calling the second active frame reflected supply an inverse
voltage.  If

\[
 R_s=\phi_s\sigma\phi_s^{-1},
 \qquad
 E_s=\phi_{s+1}\phi_s^{-1},
\]

then all frame conjugations telescope:

\[
 (E_{k-1}R_{k-1})\cdots(E_0R_0)
 =\phi_0\sigma^k\phi_0^{-1}.                     \tag{3.3}
\]

A reflected typing is gauge, not a new actuator.

A four-site word is the next topology-fusing count only if a separate
physical theorem rules out every nongauge two-site inverse.  Its corrected
relative return equation is

\[
 \overline T_3\overline T_2\overline T_1\overline T_0=I. \tag{3.4}
\]

The formal sign word with two forward and two reflected active frames does
not prove (3.4), because (3.3) includes the omitted intersite gauge maps.
A four-site proof also needs a genuine nongauge history actuator.  Actual
owner labels, all left/right histories, q2 halos, residence, and source
contexts must return relative to the unavoidable tag permutation.

## 4. Exact remaining local macro

The PBBS fan/topology problem is therefore reduced locally to the following
finite statement.

> **Relative-state-returning aligned fusion lemma.**  For some fixed `k` not
> divisible by three (preferably `k=2` or `4`), plant `k` aligned positive
> clean-`C6` sites on three PBBS cycles such that the sites use distinct
> owners and q2 resources, their intervening path transports are literal,
> and their complete relative fan holonomy (2.9) lies in the stabilizer of
> the planted triangular deck (preferably it is the identity).

If this lemma holds, Theorems 1.1 and 2.1 give a one-cycle, zero-fan-current
macro.  The strict-lower source compiler also transports through the `k`
common-history moves by the existing occurrence bijections.  A global
packing theorem, zero-gap residence, terminal common cap, and protected
linear opening would still have to be checked, but no fan target would be
exported by the macro itself.

If the lemma fails because every physically admissible positive site has
the same normalized complete-state voltage `sigma` up to pure gauge,
Corollary 3.1 is the sharp no-go:
one must use a larger packet with a genuinely different state actuator or
abandon exact local fan return in favour of a global alternative-witness
reservoir.

## 5. Scope

Proved:

1. the exact component count of any aligned `k`-site clean-`C6` family;
2. the raw tag projection and exact complete-deck stabilizer criterion;
3. the coherent topology/state monodromy lock; and
4. the exact relative state-return condition for every site count.

Not proved:

1. a literal nongauge relative-state-returning PBBS realization for any
   `3`-coprime site count;
2. simultaneous owner/q2/source/residence packing;
3. regeneration of the macro across all PBBS components; or
4. `nu(k)<=B(k)+O(1)`.
