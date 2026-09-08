# Audit of synchronized PBBS collars and polynomial protected extension

**Date:** 2026-08-06  
**Method:** set-union algebra, explicit sliding-window Johnson paths, and
direct substitution into the protected Ore localization; no computation
or search  
**Status:** corrected and strengthened.  The common-excess cancellation,
multi-cut argument, and polynomial protected-factor inequality are valid.
The original collar proof did not establish distinct lower `q1` colours;
the explicit resident sliding-window construction below repairs that gap
and proves `alpha,beta=O(sqrt(r))` for a deadline-scale ladder once the
prospective cross-pentagon resource-disjoint planting is made.

## 1. Files audited

1. `MATH_THEOREM_PBBS_SYNCHRONIZED_INCOMING_COLLAR_CANCELS_COMPLETE_UPPER_CURRENT_20260805.md`
2. `MATH_THEOREM_POLYNOMIAL_PROTECTED_FOREST_EXTENSION_FROM_TWO_EXPOSURES_20260805.md`

After the correction, their SHA256 values are respectively

```
61a13eeb7154db1bf080b1365f371d9b5f56cbed22cd589f8e059c8f44f2d9fc
456d99ea7a3ea824ac93ce88bbe7646f92f0df97d0daa2b83b027c4ca58bd26a
```

## 2. Common-excess cancellation is exact

At old cut role `j`, a one-cut interval has value

\[
                         A_j(u)\cup B_j(v).
\]

After the head permutation, the unchanged outgoing arc beginning at
`Q_j` is preceded by `P_{sigma^{-1}(j)}`.  If

\[
 A_i(u)=P_i\cup C_u,
 \qquad
 P_{\sigma^{-1}(j)}\cup Q_j=P_j\cup Q_j,
\]

then `Q_j subseteq B_j(v)` gives

\[
 A_j(u)\cup B_j(v)
 =C_u\cup P_j\cup Q_j\cup B_j(v)
 =A_{\sigma^{-1}(j)}(u)\cup B_j(v).
\]

The role permutation is invertible, so this is an occurrence-address
bijection, not merely support domination.  The explicit collars supply
the common profile through their full length.  For deeper penetration the
suffix union has already become the full ground set, so the same statement
continues trivially.

An interval crossing at least two cut edges contains the complete
terminal collar of an intervening whole arc.  Its value is therefore the
full ground set before and after rethreading.  This proves the stated
multi-cut claim.  It uses the fact that the head switch permutes whole
arcs; it would not be valid for a surgery cutting inside a collar.

## 3. Gap in the original collar proof

Five owner-disjoint simple Johnson paths do not automatically have a
2-bounded incidence lift.  Two nonconsecutive Johnson edges may have the
same rank-one-lower intersection.  The original greedy proof controlled
owner vertices but did not forbid this lower-colour collision.  Therefore
its later claim that the protected incidence bank was a path forest did
not follow.

The corrected theorem replaces the greedy path by a literal sliding
window.  For a desired residence depth `delta`, choose

\[
 5\le\delta\le r-6,
 \qquad
 D_i\subseteq G,\quad |D_i|=\delta-2,
 \qquad K_i=G\setminus D_i,\quad |K_i|=r-\delta.
\]

The set `D_i` contains a private tag `g_i` and no other role tag.  Order
`D_i` with `g_i` first, append the three elements of `X_i`, and then append
one common ordering `c_1,...,c_{r+3}` of `E`, with the three repeated
`X_i` labels separated from their initial occurrences by at least `r-2`.
The states are

\[
 S_i(t)=K_i\cup
 \{w_{i,t+1},\ldots,w_{i,t+\delta+1}\},
 \qquad 0\le t\le r+3.
\]

They are rank-`r+1` Johnson adjacent and satisfy

\[
 S_i(0)=P_i,
 \qquad
 \bigcup_{s=0}^{t}S_i(s)=P_i\cup\{c_1,\ldots,c_t\}.
\]

Every inserted `c_t` persists for `delta+1` states, up to terminal
clipping.  A lower colour is the fixed core `K_i` plus a consecutive
length-`delta` block.  Only three word labels repeat, and their two
occurrences are farther apart than `delta+3`.  Equal owner windows or
equal lower blocks are therefore impossible.  The role tags separate
different paths.  This proves the genuine incidence-path-forest property.

## 4. Exposure bounds

For one corrected path, a fixed rank-`r` set contained in an owner either
uses a fixed `delta`-subset of a `(delta+1)`-window or the entire window.
There are at most `2^3` occurrence realizations, and a fixed realization
of a `delta`-set lies in at most two windows.  Hence one path contributes
at most `16` to `alpha`.

For `beta`, an owner containing one protected lower colour must contain
`K_i`; its remaining set has size `delta+1`.  Two contained consecutive
`delta`-blocks with start distance `s` have intersection at least
`delta-1`, while positional overlap plus the three repeatable labels gives
at most `delta-s+3`.  Hence `s<=4`, and at most five blocks qualify.  One
path contributes at most `5` to `beta`.

There are five collar paths per high pentagon.  Adding the five rethread
edges gives the proof-safe aggregate bounds

\[
 \alpha\le85(H-4)+O(1),
 \qquad
 \beta\le30(H-4)+O(1).
\]

Thus `H=O(sqrt(r))` gives `alpha,beta=O(sqrt(r))`.  This conclusion is
deterministic once the prospective selection makes the combined bank an
incidence path forest, with only the intended collar-to-`P_i` attachment
overlaps and with every lower colour distinct.  It preserves the pentagon
endpoints and hence all local common-deletion algebra.

## 5. Exact protected-factor audit

For one high pentagon there are five collar paths of `r+3` Johnson edges
and five rethread edges.  Their incidence lift therefore has

\[
                         10(r+4)
\]

edges.  For `N_H=H-4` high pentagons,

\[
 e=10N_H(r+4)+O(1)=O(r^{3/2}).
\]

The polynomial extension theorem is an exact consequence of the two
earlier localization theorems.  If `A` is a failed residual shore, then

\[
 \min\{|A|,W-|A|\}<M_r(e),
 \qquad
 M_r(e)={r(r-1)\over2r-1}e.
\]

On the small side, the sharp threshold gives
`|A|>=K(r-alpha-1)`.  On the large side, writing
`B=X\setminus A` gives `|B|<=W-|A|<M_r(e)`, while the optional-core
threshold gives `|B|>=K(r-beta-1)+1`.  Thus

\[
 M_r(e)\le
 \min\{K(r-\alpha-1),K(r-\beta-1)+1\}
\]

excludes both cases exactly.  No inequality direction or strictness is
lost.

For the PBBS collar file the ground size is `2r+1` and owner rank is
`R=r+1`.  The exact substitution must therefore use the polynomial
theorem's parameter `R`, not the collar file's parameter `r`:

\[
 {R(R-1)\over2R-1}e
 \le
 \min\left\{
 {2(R-\alpha-1)-1\choose R-\alpha-1},
 {2(R-\beta-1)-1\choose R-\beta-1}+1
 \right\}.
\]

With `e=O(r^(3/2))` and `alpha,beta=O(sqrt(r))`, the left side is
polynomial and the right side is `2^(2r-O(sqrt(r)))`, so the inequality
holds for all sufficiently large `r`.

## 6. Exact remaining scope

The audit does **not** prove that all height collars can already be chosen
resource-disjoint from one another and from the incumbent PBBS bank.  It
proves that after such a prospective planting:

1. the collars have zero complete upper current;
2. they are resident literal incidence paths;
3. their exposures are `O(sqrt(r))`; and
4. the entire polynomial protected bank extends to a spanning two-factor.

Still separate are the cross-pentagon prospective resource selection,
component control, absorption of clipped boundary flags, and preservation
of the typed common-cap/source-history interface.
