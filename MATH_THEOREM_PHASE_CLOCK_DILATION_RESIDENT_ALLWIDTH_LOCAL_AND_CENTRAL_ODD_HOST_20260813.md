# Phase-clock dilation: a proof-safe resident all-width local actuator and its central-odd host scope

**Date:** 2026-08-13  
**Status:** proved local dilation theorem under an explicitly refined base-current hypothesis; automatic spanning-host consequence proved only on the central odd middle-levels graph.

## 1. Refined base hypothesis

Let `C^0,C^1` be two closures of one finite literal actuator.  Its owner
occurrences form a common simple rank-`rho` deck

\[
        v\longmapsto V_v\in {X\choose\rho},\qquad |X|=a,
\]

with a common phase map `epsilon(v) in {0,1}` such that every edge of
either closure joins opposite phases.  Let `e_0` be the number of owner
occurrences, equivalently the number of directed edges in either closure.
Assume the base immediate-lower and immediate-upper occurrence palettes
are simple.

The all-width hypothesis used below is deliberately stronger than an
unlabelled all-width identity.  For a base interval `I`, retain the tuple

\[
 \xi(I)=\bigl(|I|,\epsilon(\text{first}(I)),
              \text{first occurrence},\text{last occurrence},
              \text{two endpoint-cut types}\bigr).              \tag{1.1}
\]

The occurrence names may be replaced by any coarser endpoint types which
still determine the clock contribution in Section 4.  We require

\[
 \#\{I\subset C^0:\operatorname{OR}_X(I)=T,\ \xi(I)=\xi\}
 =
 \#\{I\subset C^1:\operatorname{OR}_X(I)=T,\ \xi(I)=\xi\}       \tag{1.2}
\]

for every base union `T subseteq X` and every retained signature `xi`.
This is the **phase-and-endpoint-refined all-width identity**.  It is an
explicit hypothesis; forgetting phase or either endpoint cut is not
enough for the argument below.

Assume finally that the two base closures have the desired common socket
labels and socket actions `pi_0,pi_1`.

## 2. Construction

Fix `h>=2`, an ambient rank `R`, and an ambient ground size `k` satisfying

\[
       R\ge \rho+h,
       \qquad k-R\ge a-\rho+h.                      \tag{2.1}
\]

Choose disjoint sets

\[
 X,\qquad U=\{u_0,\ldots,u_{2h-1}\},\qquad C,
 \qquad |C|=R-\rho-h.                               \tag{2.2}
\]

Condition (2.1) is exactly the disjoint-placement condition, since

\[
 |C\sqcup X\sqcup U|=R+(a-\rho)+h\le k.            \tag{2.3}
\]

Put, with indices modulo `2h`,

\[
             D_t=\{u_t,u_{t+1},\ldots,u_{t+h-1}\}. \tag{2.4}
\]

Replace each base occurrence `v` by the owner block

\[
 \Gamma_v=
 \begin{cases}
 (C\cup V_v\cup D_0,\ldots,C\cup V_v\cup D_h),
       &\epsilon(v)=0,\\
 (C\cup V_v\cup D_h,\ldots,C\cup V_v\cup D_{2h}),
       &\epsilon(v)=1,
 \end{cases}                                       \tag{2.5}
\]

where `D_(2h)=D_0`.  Consecutive blocks are joined at their common clock
anchor: `D_h` on a phase-`0` to phase-`1` edge, and `D_0` on a phase-`1`
to phase-`0` edge.  Applying this replacement to `C^0` and `C^1` gives
the two lifted closures `C^0[h],C^1[h]`.

## 3. Local phase-clock theorem

> **Theorem 3.1 (proof-safe phase-clock dilation).**  Under (1.2) and
> (2.1), the two lifted closures are literal subgraphs of `J(k,R)` and:
>
> 1. have the same socket actions `pi_0,pi_1` as the base actuator;
> 2. have equal literal owner-union currents at every lifted width;
> 3. have simple owner decks and simple immediate-lower and
>    immediate-upper palettes;
> 4. every nonconstant coordinate has every positive run and every zero
>    run of length at least `h` in either lifted closure;
> 5. have
>    \[
>                       e_h=(h+1)e_0;               \tag{3.1}
>    \]
> 6. for the protected-factor exposure parameters of the central
>    middle-levels host, the always-safe bounds are
>    \[
>                       \alpha_h,\beta_h\le e_h.    \tag{3.2}
>    \]
>
> Thus, for a fixed base actuator, `e_h,alpha_h,beta_h=O(h)`.

### Proof

Every owner in (2.5) has size

\[
                 |C|+|V_v|+|D_t|=R.                \tag{3.3}
\]

A clock edge deletes `u_t` and inserts `u_(t+h)`.  A block-joining edge
holds `D_0` or `D_h` fixed and performs the one deletion/insertion of the
corresponding base Johnson edge.  Hence every lifted edge is a Johnson
edge.

If two lifted owners are equal, disjointness of `C,X,U` first gives equal
base owners and equal clock sets.  Base simplicity gives the same base
occurrence.  The `h+1` members used in either half of the `2h`-cycle are
distinct, so the positions also agree.  The owner deck is simple.

On a clock edge the `U`-parts of the lower and upper tickets have sizes
`h-1` and `h+1`.  On a lifted base edge both have `U`-part `D_0` or
`D_h`, of size `h`.  Thus clock tickets cannot collide with lifted base
tickets.  Within a clock family, disjoint coordinate supports reduce
equality to equality of the simple base occurrence and of the cyclic
`(h-1)`- or `(h+1)`-interval in `U`.  Within the lifted base family,
base palette simplicity applies; the two anchors are disjoint and hence
cannot create a cross-phase collision.  Both immediate palettes are
simple.

For `x in X`, each base bit is repeated on an entire block of `h+1`
owners.  Every nonconstant base positive or zero run therefore dilates to
length at least `h+1`.

For a clock coordinate, the clock-state sequence through two consecutive
opposite-phase blocks is

\[
 D_0,D_1,\ldots,D_h,D_h,D_{h+1},\ldots,D_{2h},      \tag{3.4}
\]

followed by another `D_0`; the antipodal anchors `D_0,D_h` are both
repeated at block seams.  A point of `U` lies in exactly `h` consecutive
members of the cyclic list `D_0,\ldots,D_(2h-1)` and is absent from the
other `h`.  Exactly one of the two antipodal anchors belongs to either
arc.  Repeating both anchors therefore lengthens, rather than shortens,
both binary runs.  In particular both have length at least `h`.  Core
coordinates are constant.

Each of the `e_0` blocks contributes `h` clock edges and each of the
`e_0` base edges contributes one joining edge, proving (3.1).

For (3.2), the number of protected upper vertices and the number of
protected lower vertices are each at most the number `e_h` of protected
incidence edges.  Any unprotected lower vertex can therefore see at most
`e_h` protected uppers, and any upper vertex can see at most `e_h`
protected saturated lowers.  This crude bound is sufficient and needs no
unproved endpoint-exposure formula.  It completes the local assertions
except the all-width statement, proved next.  `square`

## 4. All-width lifting

Let `J` be an interval of a lifted closure.  Collapse each nonempty piece
of a clock block to its base occurrence.  The lifted width determines the
two exact cut offsets together with the number of whole intervening
blocks.  Since phases alternate, its retained data are determined by a
base signature `xi` from (1.1) and the two cut offsets.  Coordinate
disjointness gives

\[
 \operatorname{OR}(J)
   =C\cup \operatorname{OR}_X(\pi J)\cup K_h(\xi,\text{cuts}),   \tag{4.1}
\]

where the clock set `K_h subseteq U` is determined solely by those data.
For example,

\[
 \bigcup_{j=0}^{t}D_j=\{u_0,\ldots,u_{h+t-1}\}
 \quad(0\le t\le h),
 \qquad \bigcup_{j=0}^{h}D_j=U,                    \tag{4.2}
\]

and the phase-one formulas are cyclic translates.

Apply (1.2) separately for every base union and every enriched endpoint
signature, and then lift the corresponding cut offsets.  This gives equal
counts for every triple

\[
      \bigl(\operatorname{OR}_X(\pi J),\xi,\text{cuts}\bigr).   \tag{4.3}
\]

Summing (4.3) over all triples whose right side in (4.1) equals a fixed
literal target `S` proves equality of the old and new target counts at
every lifted width.

No injectivity of

\[
 (T,\xi,\text{cuts})\longmapsto C\cup T\cup K_h(\xi,\text{cuts}) \tag{4.4}
\]

is required.  Distinct signatures are allowed to give the same clock
union; their equal counts are simply added on both sides.  This proves
Theorem 3.1(2).

## 5. Socket action

The exposed endpoints retain the base socket labels and meet exterior
paths at the common anchors `D_0` or `D_h`.  Clock dilation inserts no
permutation of socket names.  Consequently an old exterior return
`kappa` and a base local multiplier `s` still give

\[
                  \theta_0=\kappa,
                  \qquad \theta_1=\kappa\circ s.    \tag{5.1}
\]

In particular, the common-mate odd four-socket action survives literally
whenever it is part of the refined base actuator.

## 6. Correct spanning-host scope

The proved subexponential low-exposure phased-host theorem applies to the
middle-levels incidence graph

\[
 ML_m:\quad { [2m-1]\choose m-1} \longleftrightarrow\
                    { [2m-1]\choose m}.             \tag{6.1}
\]

Therefore its direct use here requires

\[
                         k=2R-1,qquad m=R.           \tag{6.2}
\]

Under (6.2), if the feasibility inequalities

\[
 R\ge\rho+h,
 \qquad R-1\ge a-\rho+h                             \tag{6.3}
\]

hold and the base actuator is fixed, then

\[
 e_h=O(h),\qquad \alpha_h,\beta_h=O(h).             \tag{6.4}
\]

Taking `h=d(k)+1`, the elementary estimates

\[
 \binom{k}{\lceil k/2\rceil}\ge {2^k\over\sqrt{2k}},
 \qquad \Lambda\le2^{k-1}
\]

give

\[
                 d(k)\le\left\lceil\sqrt{k/2}\right\rceil,    \tag{6.5}
\]

so `e_h=2^{o(R)}` and `alpha_h,beta_h=o(R)`.  The phased-host theorem
then embeds the protected lifted bank in a spanning two-factor of `ML_R`
for all sufficiently large odd `k=2R-1`, retaining its alternating
phases.

This is a zero-intrinsic-overhead protected bank: its vertices are middle
owners which must already be selected by the global construction.  This
does not by itself prove that the global positive owner/lower/cap factor
can reserve those owners.

For even `k=2R`, the two adjacent central shores have different sizes:

\[
                 {2R\choose R-1}<{2R\choose R}.      \tag{6.6}
\]

Hence there is no spanning two-factor on that full bipartite incidence
graph.  Neither (2.1) nor low exposure fixes this.  Even `k`, and any
noncentral `(k,R)` host, require a separately proved balanced-host
reduction or a different coinstantiation theorem.

## 7. Exact conclusion

The phase clock is a valid local method for converting a finite
phase-and-endpoint-refined all-width actuator into a two-sided
depth-resident actuator with linear protected size.  What is proved is

\[
 \boxed{\text{refined all-width local actuator}
        \Longrightarrow
        \text{resident local actuator in }J(k,R),}
\]

and, on the existing host theorem's actual domain,

\[
 \boxed{k=2R-1
        \Longrightarrow
        \text{automatic protected phased coinstantiation}.}
\]

No automatic even-dimensional or general-rank host statement is claimed.
