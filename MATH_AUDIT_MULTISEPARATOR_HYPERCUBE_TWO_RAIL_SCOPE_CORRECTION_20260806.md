# Audit of the multiseparator hypercube two-rail packing theorem

**Date:** 2026-08-06  
**Primary file:**
`MATH_THEOREM_MULTISEPARATOR_HYPERCUBE_SCD_TWO_RAIL_PACKING_20260806.md`  
**Method:** exact tag matching, binomial census, weighted-load audit, and
chain-endpoint ranks; no computation or search  
**Verdict:** the exact target packing, Vandermonde census, and global
saturated-chain realization pass.  The claimed asymptotic balance of the
complete separator loads is false for the stated value of `r`, and the
global chain decomposition is not symmetric.  The theta-sized balanced
subbank remains available after a weaker capacity estimate.

## 1. Exact rows which pass

For fixed `alpha`, the edges

\[
 S\longleftrightarrow S\cup\{f(\alpha)\},
 \qquad S\subseteq D\setminus\{f(\alpha)\},           \tag{1.1}
\]

form a perfect matching of `B(D)`.  Different selector signatures partition
the full tag cube, so their union is a perfect matching of `B(H union D)`.

Section 2 must fix one SCD of `B(U)` once and for all.  On that reading,
distinct core sets of one bulk rank lie on distinct SCD chains, and the
target-disjointness proof is valid.  The condition

\[
                         2q+d\le u                    \tag{1.2}
\]

implies every individual extension condition
`2(q-|E|)+d<=u`.  Terms with `q-|E|<0` are absent, equivalently their
binomial coefficients are zero.

Both Vandermonde convolutions are exact:

\[
 \sum_{S\subseteq D\setminus\{f(\alpha)\}}
 {u\choose q-|\alpha|-|S|}
 ={u+p-1\choose q-|\alpha|},                           \tag{1.3}
\]

and then

\[
 \sum_{\alpha\subseteq H}{u+p-1\choose q-|\alpha|}
 ={n-1\choose q}.                                      \tag{1.4}
\]

Thus the exact number of charts and the all-depth marked-target packing
pass.

## 2. The complete separator loads are not balanced as claimed

The theorem takes

\[
                         r=\lceil\log_2p\rceil.       \tag{2.1}
\]

Hence `p<=2^r<2p`, so a cardinality-balanced fibre partition can contain
fibres of sizes one and two.  Uniformity of the weights gives

\[
                         w_a=(1+o(1))w_0              \tag{2.2}
\]

for all `a<=r`.  It follows that a one-signature fibre has load
`(1+o(1))w_0`, whereas a two-signature fibre has load
`(2+o(1))w_0`.  Their ratio tends to two, not one.  Therefore equation
(4.5) and the Section 7 claim of asymptotically balanced complete loads do
not follow and are false in general.

There are two clean repairs.

1. Increase the selector bank so that `2^r/p -> infinity`, for example
   `r=ceil(2 log_2 p)`.  Balanced fibre cardinalities then have relative
   error `o(1)`, and (2.2) proves the desired weighted balance.  This still
   has `r=O(log d)` and does not affect the separator-capacity inequalities.
2. Keep (2.1) but weaken the conclusion to a balanced chosen subbank, as in
   Section 5.

The second repair needs only a lower bound.  Every separator fibre is
nonempty, and (2.2) gives

\[
 N_b\ge(1-o(1))w_0
     \ge(1-o(1)){N_{\rm charts}\over2p}.              \tag{2.3}
\]

Since `N_charts/W -> e^{-pi}/2`, the right side of (2.3) is asymptotically
`e^{-pi}W/(4p)`, which is far larger than `eta W/p`.  Thus every separator
still has enough charts to choose the theta-sized subbank with counts
differing by at most one.  Equations (5.7)--(5.8) survive after replacing
the citation to (4.5) by (2.3).

## 3. The global chains are saturated but not symmetric

For a bulk symmetric chain with endpoint ranks `a,u-a`, each chain in
(3.5A) has global endpoint-rank sum

\[
                         2|E|+u+1.                    \tag{3.1}
\]

A symmetric chain of `B_n` would require endpoint-rank sum `n=r+p+u`.
Equation (3.1) equals `n` only on the exceptional tag layer
`2|E|+1=r+p`.  Consequently (3.5A) is not a global SCD.

It is, however, a genuine global saturated-chain decomposition: the two
chains partition the product of each matched tag edge with each fixed bulk
SCD chain, and these products partition `B_n`.  Under

\[
                         r+p\le2d+3,                  \tag{3.2}
\]

every chain meeting the deep band reaches its top rank `t-1`.  Splitting
from that rank therefore gives the stated top-aligned piece census, and the
two rails are actual pieces of this one saturated decomposition.  The
parameters chosen in Section 5 satisfy (3.2) for all sufficiently large
`d`, although that section explicitly cites only the weaker extension
condition `r+p<=3d+3`.

## 4. What this suffices for

The reset-count ledger needs a partition into disjoint saturated inclusion
pieces, common top ranks within each slab, and the exact piece census.  It
does not use the equality of the lower and upper rank defects of a global
SCD.  Hence the saturated decomposition above suffices for that counting
ledger and for the antichain-top static target partition.

It does not prove compatibility with a separately fixed PBBS/SCD source
chronology, the owner envelope, overlapping chart histories, or a connected
Euler trace.  Section 6 correctly leaves those physical statements open.

The proof-safe scope is therefore

\[
\boxed{
\begin{array}{l}
\text{exact tag matching and target census: proved},\\
\text{one global saturated-chain rail packing: proved},\\
\text{one global symmetric-chain rail packing: not proved and generally false},\\
\text{balanced complete separator loads at }r=\lceil\log_2p\rceil:
   \text{ false},\\
\text{theta-sized balanced subbank: valid after the lower-bound repair},\\
\text{PBBS history gluing: open}.
\end{array}}
\]
