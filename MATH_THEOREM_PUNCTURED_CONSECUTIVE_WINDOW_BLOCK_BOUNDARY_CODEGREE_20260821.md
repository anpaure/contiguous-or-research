# Consecutive window blocks satisfy the punctured boundary-codegree scale

**Date:** 2026-08-21  
**Status:** exact analytic theorem

Let `b=2r+1`, let

\[
 M_i=\{i,\ldots,i+r-1\},\qquad
 L_i=\{i,\ldots,i+r-2\},                              \tag{0.1}
\]

and puncture positional start zero.  Put

\[
 D_M=2r\,r!(r+1)!.                                    \tag{0.2}
\]

For `2<=k<=r`, define `T_k^M={M_1,...,M_k}`.  For
`2<=k<=r-1`, define `T_k^L={L_1,...,L_k}`.  Then

\[
\begin{aligned}
 \deg(T_k^M)&=2(b-k)(r-k+2)!(r-k+1)!,                 \tag{0.3}\\
 \deg(T_k^L)&=2(b-k)(r-k+3)!(r-k)!.                   \tag{0.4}
\end{aligned}
\]

Every boundary edge in either family is endpoint-disjoint from every
other one, so `v(T)=2k`.  Nevertheless both families obey the proposed
global boundary-codegree inequality with the absolute per-target constant
`e^2`:

\[
 \boxed{\qquad
 {\deg(T_k^M)\over D_M},\ {\deg(T_k^L)\over D_M}
     \le (e^2)^k r^{2-2k}.
 \qquad}                                               \tag{0.5}
\]

Thus the long boundary matching which destroys pointwise isolated-edge
peeling is fully compatible with the aggregate boundary gate.  Its cost
must be charged blockwise.

## 1. Exact middle-block count

For the `k` consecutive middle targets, the non-singleton labelled Venn
cells have sizes

\[
                         r-k+2,\qquad r-k+1,            \tag{1.1}
\]

and the remaining `2(k-1)` nonempty cells are singletons.  Indeed, the
first non-singleton cell is outside all `k` windows and the second lies in
all of them; the intervening membership states are the proper prefixes
and suffixes of `[k]`.

Also

\[
                         |M_i\cap M_j|=r-|i-j|.         \tag{1.2}
\]

For length-`r` arcs on the odd cycle, (1.2) fixes the undirected cyclic
distance between every two positional starts.  Adjacent starts therefore
differ consistently by `+1` or consistently by `-1`; a sign change would
repeat a start.  Hence there are two orientations of the labelled block.
For either orientation, exactly `k` of the `b` translations use punctured
start zero, leaving `b-k` translations.

The exact Venn-cell labelling formula now gives (0.3).  Directed-deck
injectivity makes the count multiplicity-free.

## 2. Exact lower-block count

The same argument applies to the `k` consecutive lower targets.  Their
two non-singleton Venn cells have sizes

\[
                         r-k+3,\qquad r-k,              \tag{2.1}
\]

with `2(k-1)` singleton cells.  In the stated range every pairwise
intersection is positive, so there is no zero-intersection distance
ambiguity; the intersections fix the consecutive start metric up to its
two orientations.  There are `b-k` retained translations in each.  This
proves (0.4).

The boundary endpoints are `{i,i+r}` in the middle case and
`{i,i+r-1}` in the lower case.  In the stated ranges all `2k` endpoints
are distinct, proving `v(T)=2k`.

## 3. Uniform boundary-gate constant

For integers `0<=m<=n`, write `(n)_m=n!/(n-m)!`.  For `1<=m<=n`, the
elementary bounds

\[
 {n\choose m}\ge(n/m)^m,
 \qquad m!\ge(m/e)^m
\]

give

\[
                         (n)_m\ge(n/e)^m.              \tag{3.1}
\]

Using (0.3),

\[
 r^{2k-2}{\deg(T_k^M)\over D_M}
 ={b-k\over r}
   {r^{2k-2}\over (r)_{k-2}(r+1)_k}
 \le2e^{2k-2}\le e^{2k}.                              \tag{3.2}
\]

For `k>=3`, (0.4) similarly gives

\[
 r^{2k-2}{\deg(T_k^L)\over D_M}
 ={b-k\over r}
   {r^{2k-2}\over (r)_{k-3}(r+1)_{k+1}}
 \le2e^{2k-2}\le e^{2k}.                              \tag{3.3}
\]

At `k=2`, the left side of (3.3) is

\[
                         {2r-1\over r-1}\le3<e^4.     \tag{3.4}
\]

Equations (3.2)--(3.4) prove (0.5).  \(\square\)

## 4. Sharp endpoint of the middle family

At `k=r`, (0.3) gives

\[
                         \deg(T_r^M)=4(r+1),           \tag{4.1}
\]

and Stirling's formula yields

\[
 \left(r^{2r-2}{\deg(T_r^M)\over D_M}\right)^{1/r}
 =\left({2r^{2r-3}\over(r!)^2}\right)^{1/r}
 \longrightarrow e^2.                                 \tag{4.2}
\]

Thus `e^2` is asymptotically sharp for this block family.
