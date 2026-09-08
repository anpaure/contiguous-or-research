# Exact finite heat-bath ledger for the full MSW component hierarchy

## 1. Quantity audited

For the complete interaction-component decomposition of the MSW factor under
`tau=(2 3)`, put at rank `r`

\[
 A_r=\left\|\sum_K\Delta_{K,r}\right\|_2^2,
 \qquad
 V_r=\sum_K\|\Delta_{K,r}\|_2^2.                    \tag{1.1}
\]

The exact heat-bath identity says that the expected quadratic-energy change
is `(V_r-A_r)/4`.  Thus `A_r-V_r>0` is strict contraction.

`msw_transposition_components.cpp` was extended to accumulate both integers
directly from the independently reconstructed interaction graph.  All runs
were performed remotely in visible RunPod `tmux` session `msw_heat`; no
enumeration was run on the Mac.

## 2. Stable sign pattern through m=10

For every audited `m=3,...,10`, the first lower rank has

\[
                        A_{m-1}-V_{m-1}<0.             \tag{2.1}
\]

The exact values are

\[
\begin{array}{c|rrrrrrrr}
m&3&4&5&6&7&8&9&10\\ \hline
A_{m-1}-V_{m-1}
&-4&-8&-20&-48&-124&-340&-984&-2972.
\end{array}
\]

In contrast, for every audited `m>=5` and every

\[
                         2\le r\le m-2,
\]

one has strict contraction `A_r-V_r>0`.  At `m=10`, the complete nontrivial
ledger is

\[
\begin{array}{c|rrrrrrrr}
r&2&3&4&5&6&7&8&9\\ \hline
A_r-V_r
&37131936&13725044&3946552&1197228&358564&97096&14156&-2972.
\end{array}
\]

The corresponding ledgers for `m=5,...,9` show the same single sign change
between `r=m-2` and `r=m-1`.

## 3. Mathematical implication

This is not a proof of the all-`m` sign law.  It is, however, a sharply
targeted structural conjecture:

> **MSW heat sign conjecture.**  For `tau=(2 3)` and all sufficiently large
> `m`, full component resampling strictly contracts every lower-rank
> quadratic discrepancy below the first shadow, and strictly expands the
> first-shadow quadratic discrepancy.

If proved, the larger component hierarchy already supplies the **bulk**
multirank smoother missing from the size-two charts.  The remaining job is
then exactly top-shadow protection: combine it with a circuit invisible at
rank `m-1`, or reserve an adjacent-shadow construction/absorber whose gain
dominates the negative value in (2.1).

This pattern also explains why the local charts alone looked contradictory.
Their disjoint first-shadow squares have `A=V` and make no expected progress.
The strict deeper contraction comes from positive alignment among effects of
the larger nonlocal components.

