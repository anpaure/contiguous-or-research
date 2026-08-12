# Cyclic-window rotors give resident full-union shields with literal source antecedents

**Date:** 2026-08-05  
**Method:** cyclic interval calculus, coordinatewise depth inversion, and
protected Ore--Ryser; no computation or search  
**Status:** unconditional local and unrooted factor theorem.  In the odd
middle-level host, a cyclic window rotor is owner-simple, lower/upper-q1
rainbow, biresident, and every minimum-length owner block is a full-ground
shield.  It has an explicit cyclic nonempty depth-`d` source antecedent.
Every fixed number of pairwise resource-disjoint rotors can be protected in
one spanning two-factor.  Because a protected rotor is a saturated factor
component, this does not attach its shield blocks to PBBS bodies.

## 1. The cyclic owner rotor

Let

\[
                         \Omega=\{z_0,\ldots,z_{n-1}\},
 \qquad                  n=2m-1,                            \tag{1.1}
\]

with subscripts read modulo `n`.  Put

\[
 T_i=\{z_i,z_{i+1},\ldots,z_{i+m-1}\},                    \tag{1.2}
\]

and

\[
 I_i=T_i\cap T_{i+1}=\{z_{i+1},\ldots,z_{i+m-1}\}.        \tag{1.3}
\]

### Theorem 1.1 (resident q1-rainbow rotor)

For `m>=3`, the alternating cyclic sequence

\[
 T_0,I_0,T_1,I_1,\ldots,T_{n-1},I_{n-1},T_0              \tag{1.4}
\]

is a simple incidence cycle in `ML_m`.  Its projected owner cycle has the
following properties.

1. The owners `T_i` are pairwise distinct rank-`m` sets.
2. The lower colours `I_i` are pairwise distinct rank-`(m-1)` sets.
3. The upper colours
   
   \[
                    U_i=T_i\cup T_{i+1}
                       =\{z_i,\ldots,z_{i+m}\}             \tag{1.5}
   \]
   
   are pairwise distinct rank-`(m+1)` sets.
4. Every `m` consecutive owners have union `Omega`.
5. Every coordinate has one positive owner run of length `m` and one zero
   gap of length `m-1`.

Consequently the cycle is positively and zero-resident at every depth

\[
                              d\le m-2,                    \tag{1.6}
\]

and every `m`-owner block is a shortest full-union shield.

#### Proof

The transition is

\[
                         T_{i+1}=T_i-z_i+z_{i+m},
\]

so (1.4) is an incidence cycle.  Cyclic intervals of a fixed length
strictly between zero and `n` are distinct; this proves the three palette
claims from (1.2), (1.3), and (1.5).

The owners `T_i,...,T_(i+m-1)` together contain the cyclic coordinate
interval from `z_i` through `z_(i+2m-2)`, which is all `n=2m-1`
coordinates.  A fixed coordinate `z_a` lies in precisely the owners with
starts

\[
                         a-m+1,\ldots,a,
\]

so its positive run and zero gap have lengths `m` and `n-m=m-1`.
Condition (1.6) makes both at least `d+1`.

Finally, a rank-`m` Johnson path of `ell` owners has union rank at most
`m+ell-1`.  Full union rank `2m-1` therefore requires `ell>=m`, and the
displayed blocks attain equality.  \(\square\)

The block `T_0,...,T_(m-1)` is exactly the sharp geodesic with permanent
core `\{z_(m-1)\}`, outgoing bank `z_0,...,z_(m-2)`, and incoming bank
`z_m,...,z_(2m-2)`.

## 2. Explicit nonempty source antecedent

Let `D` denote consecutive union.  We now construct a cyclic source word
`A=(A_0,...,A_(n-1))` satisfying

\[
                              D^dA=T.                       \tag{2.1}
\]

For coordinate `z_a`, choose the integer lift of its owner run

\[
 s_a=a-m+1,\qquad e_a=a.                                  \tag{2.2}
\]

Starting at `s_a+d`, take pins spaced by `d+1` while they do not exceed
`e_a`, and adjoin the final pin `e_a` if it is not already present:

\[
 P_a=\{s_a+d+t(d+1):t\ge0,\ s_a+d+t(d+1)\le e_a\}
       \cup\{e_a\}.                                      \tag{2.3}
\]

Reduce pins modulo `n` and put

\[
                         A_p=\{z_a:p\in P_a\pmod n\}.      \tag{2.4}
\]

### Theorem 2.1 (literal rotor inversion)

For every `0<=d<=m-2`, the source letters (2.4) are all nonempty and satisfy
(2.1).

#### Proof

One source occurrence at position `p` is present in the owner starts
`p-d,...,p`.  The first pin in (2.3) covers

\[
                         [s_a,s_a+d].
\]

Successive regularly spaced pins cover the immediately adjacent intervals
of length `d+1`.  If the final regular pin is below `e_a`, its distance from
`e_a` is at most `d`; the extra pin `e_a` overlaps the preceding coverage
and ends it exactly at `e_a`.  Thus the owner starts covered by the pins of
`z_a` are exactly `[s_a,e_a]`, the run (2.2).  This proves (2.1)
coordinatewise.

For any source position `p`, take

\[
                         a=p+m-1-d\pmod n.
\]

Then `p=s_a+d` is the first pin of `z_a`.  Hence `z_a in A_p`, so every
source letter is nonempty.  \(\square\)

This is a cyclic source antecedent for the rotor component itself.  It does
not prescribe a source state compatible with an external PBBS splice.

## 3. Fixed rotor banks

### Lemma 3.1 (fixed-bank disjointness and exposure)

For every fixed `q` and all sufficiently large `m`, there are `q` coordinate
images of the rotor whose owner, lower-q1, and upper-q1 vertex sets are
separately pairwise disjoint.

For the union `P` of their incidence cycles,

\[
 |E(P)|=2q(2m-1)=O_q(m),                                  \tag{3.1}
\]

and

\[
 \ell_P(x)\le2q\quad(x\in\mathcal L),
 \qquad
 z_U:=|N(U)\cap Z_P|\le2q\quad(U\in\mathcal U).           \tag{3.2}
\]

#### Proof

A uniform coordinate permutation sends each rotor vertex uniformly through
its rank layer.  One rotor has `2m-1` vertices in each of the owner, lower,
and upper palettes.  After a fixed number of choices, the expected collision
count is polynomial divided by a central binomial coefficient, hence tends
to zero.  Greedy orbit avoidance gives the disjoint bank.

Two distinct cyclic length-`m` windows whose starts have cyclic distance
`delta` intersect in at most `m-delta`.  A rank-`m-1` lower vertex can
therefore lie below at most two adjacent rotor owners.  Dually, a rank-`m`
owner contains at most two adjacent cyclic length-`m-1` rotor facets.  This
proves (3.2); (3.1) is the incidence-cycle length.  \(\square\)

### Theorem 3.2 (unrooted resident-rotor factor extension)

For every fixed `q` and all sufficiently large `m`, the `q` disjoint rotor
cycles from Lemma 3.1 are contained in one spanning two-factor of `ML_m`.

#### Proof

Apply the all-cut proof of
`MATH_THEOREM_FIXED_SHARP_SHIELD_BANK_EXTENDS_TO_MIDDLE_LEVELS_TWO_FACTOR_20260805.md`
with the bounds (3.1)--(3.2).  The general protected-Ore near-shadow theorem
puts one side of a failed cut in `O_q(m^2)`.  The forced-facet load `2q`
and the sharp optional partial-shadow theorem exclude the co-small side.

On the small side there are no endpoint terms, because every protected
component is a cycle.  At one lower vertex the singleton protected loss is
at most `2q`, so the exact protected crossing identity gives

\[
                         \lambda_P(A)\le2q|A|.              \tag{3.3}
\]

For completeness, this inequality can be checked owner by owner.  At a
protected owner let `a` be the number of all selected facets below it and
let `k` be the number of its two protected facets which are selected.  The
sum of the singleton-loss contributions there is `a-k`.  Its contribution
to `lambda_P(A)` is zero for `a=0`, is one exactly when `a=1,k=0`, and is
`2-k` for `a>=2`; in every case it is at most `a-k`.  Summing proves (3.3)
from the singleton bound.

Kruskal--Katona gives

\[
 \sigma(A)>{(m-2)(m-4)\over4(m-1)}|A|
\]

throughout the `O_q(m^2)` small range.  This exceeds (3.3) for fixed `q`
and all sufficiently large `m`.  No failed cut remains, and protected
Ore--Ryser supplies the residual two-factor.  \(\square\)

## 4. The exact topology boundary

Theorems 1.1--3.2 prove that full-union shields, depth-`d` source
factorization, biresidence, q1 simplicity, and unrooted factor planting are
simultaneously compatible.

They do **not** yet give the four shielded PBBS continuation arcs.  Every
vertex of a protected rotor cycle already has protected degree two.
Therefore, in every spanning two-factor containing it, that rotor remains a
saturated connected component.  It cannot attach to a PBBS body.

Opening a rotor removes this saturation and exposes shielded arcs, but it
also changes the cyclic source boundary and the residence runs which crossed
the removed edge.  The precise remaining theorem is therefore a rooted
opening/graft statement:

> choose four opened rotor arcs (or eight oriented geodesic blocks), attach
> their endpoints to the four PBBS continuation bodies, and prove that the
> pin antecedents, seam residence, owner/lower-q1 factor, and common-history
> cut permutation coexist.

This is a topology/state obstruction, not a local shield-supply or scalar
factor-extension obstruction.

## 5. Dependencies

The abstract localization and sharp geodesic are in

`MATH_THEOREM_FULL_UNION_SHIELDS_LOCALIZE_ALL_EXTERIOR_SPLICE_DAMAGE_20260805.md`.

The fixed-exposure all-cut factor proof is in

`MATH_THEOREM_FIXED_SHARP_SHIELD_BANK_EXTENDS_TO_MIDDLE_LEVELS_TWO_FACTOR_20260805.md`.
