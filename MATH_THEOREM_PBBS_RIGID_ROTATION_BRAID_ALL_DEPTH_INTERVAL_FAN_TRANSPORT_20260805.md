# The rigid full-rotation braid transports the entire single-soliton fan at every depth

**Date:** 2026-08-05  
**Method:** exact intersection calculus on the alternating `R_1,R_0` output
cycle; no computation or search  
**Status:** unconditional for `m>=4`.  Although the full rigid rotation
orbit is not a one-cycle fusion, its braid component recreates every
lower cyclic-interval target formerly carried by the single-soliton PBBS
component, and hence every paired complementary upper target.  The
two-soliton shore remains open.

## 1. Rigid rows and the output braid

Work on `Z_n`, `n=2m+1`, and rotate sets additively.  The two relevant q1
row types are

\[
 \begin{aligned}
 R_0(x)&=\{x+1,x+2,\ldots,x+m-1\},\\
 R_1(x)&=\{x+1,\ldots,x+m-2\}\cup\{x+m\}.
 \end{aligned}                                                   \tag{1.1}
\]

In the terminal factor after all rigid clean-`C6` rotations, the braid
cycle on the `P_0,P_2` owners has q1 row sequence

\[
 R_1(x),R_0(x-1),R_1(x-2),R_0(x-3),\ldots                    \tag{1.2}
\]

as `x` decreases around `Z_n`.  This is the row form of the two-edge phase
map `P_0(x)->P_2(x-1)->P_0(x-2)`.

The basic paired intersection is

\[
                         R_1(y)\cap R_0(y-1)
                         =\{y+1,\ldots,y+m-2\}.                 \tag{1.3}
\]

The exceptional point `y+m` in `R_1(y)` is deleted by `R_0(y-1)`.

## 2. Every interval rank occurs

### Theorem 2.1 (all-depth braid fan)

For every `1<=q<=m` and every cyclic interval `I` of rank `m-q`, there is
a segment of exactly `q` consecutive q1 rows in (1.2) whose intersection
is `I`.  More precisely, select only the `R_1`-starting segments when `q`
is even and only the `R_0`-starting segments when `q` is odd.  This
distinguished parity subfamily has exactly `n` segments at each depth and,
for `q<m`, supplies every cyclic interval exactly once.  The other `n`
segments of the `2n`-row braid are not used in the occurrence bank.

More explicitly, for `q=2h`,

\[
 \begin{aligned}
 &\bigcap_{j=0}^{h-1}
   \bigl(R_1(x-2j)\cap R_0(x-2j-1)\bigr)\\
 &\hspace{35mm}=\{x+1,x+2,\ldots,x+m-2h\},
 \end{aligned}                                                   \tag{2.1}
\]

which has rank `m-2h`.  For `q=2h+1`,

\[
 \begin{aligned}
 &R_0(x-1)\cap
   \bigcap_{j=1}^{h}
   \bigl(R_1(x-2j)\cap R_0(x-2j-1)\bigr)\\
 &\hspace{35mm}=\{x,x+1,\ldots,x+m-2h-2\},
 \end{aligned}                                                   \tag{2.2}
\]

which has rank `m-(2h+1)`.  At rank zero the displayed interval is empty.

#### Proof

By (1.3), the `j`-th pair in (2.1) is the ordinary integer interval

\[
                         [x-2j+1,\ x-2j+m-2].                   \tag{2.3}
\]

The largest left endpoint occurs at `j=0`, and the smallest right endpoint
at `j=h-1`; their intersection is (2.1).  For (2.2), include the initial
interval

\[
                         R_0(x-1)=[x,x+m-2]                     \tag{2.4}
\]

and use the pairs (2.3) for `j=1,...,h`.  The largest left endpoint is
`x`, while the smallest right endpoint is `x-2h+m-2`, giving (2.2).

All spans have length below `n`, so the integer calculation descends
unambiguously to cyclic intervals in `Z_n`.  Varying `x` supplies every
rotation of the interval at the stated rank. `square`

## 3. Comparison with the old single-soliton component

The old single-soliton q1 sequence is

\[
                         \ldots,R_0(x+1),R_0(x),R_0(x-1),\ldots. \tag{3.1}
\]

The intersection of any `q` consecutive rows is a cyclic interval of rank
`m-q`, and all such intervals occur as the phase varies.  For `q<m` they
are the `n` distinct rotations of that interval; for `q=m` every phase has
the common empty intersection.  In particular every lower whole-fan target
whose chosen corridor lies entirely on the single-soliton component is in
this family.

### Corollary 3.1 (complete single-soliton bank transport)

Every named lower target formerly witnessed by a single-soliton corridor
has a target-equal replacement on the terminal braid cycle.  The
replacement may have a different occurrence address, but the map is
bijective after indexing both families by `(q,I)`.

Complementing the owners gives the same assertion for every paired proper
upper target.  Thus puncturing **all** `n` single-soliton edges in the full
rotation orbit creates no lower or paired-upper support hole at any depth.

#### Proof

For `q<m`, the old and new target families are both exactly the set of all
cyclic intervals of rank `m-q`, once each under the `(q,I)` indexing.  At
`q=m`, choose any one of the old and new empty-intersection occurrences.
Apply Theorem 2.1 and then complement intersections to unions. `square`

## 4. Consequence for the polynomial leave

The full rigid rotation orbit cuts `n` single-soliton edges and `2n`
two-soliton edges.  Corollary 3.1 removes the entire inverse-fan leave of
the first `n` cuts.  Therefore the unresolved fixed-bank leave is supported
only on the two-soliton edge orbits and has the sharper bound, on each of
the lower and paired-upper shores,

\[
                         2n\binom{m+1}{2}=O(m^3)                \tag{4.1}
\]

before subtracting the automatically transported q1/q2 rows and any
overlap between inverse fans.  If lower and upper obligations are counted
as separate objects, the combined raw bound is
`4n*binom(m+1,2)`.

This is a support theorem, not complete physical compilation.  The braid
cycle and the residual `t->t+3` cycles still need compatible source
antecedents, residence, cap routes, and a terminal opening.

## 5. Scope

Proved:

1. the exact all-depth q1-row intersection formulas (2.1)--(2.2);
2. target-equal replacement of the complete single-soliton lower bank;
3. simultaneous replacement of its paired upper complements; and
4. localization of every remaining named whole-fan casualty to the
   two-soliton shore.

Not proved:

1. alternate witnesses for the two-soliton inverse-fan leave;
2. a common-history source decoration of the entire overlapping braid;
3. zero-gap residence, typed common cap, or linear opening;
4. `nu(k)<=B(k)+O(1)`.
