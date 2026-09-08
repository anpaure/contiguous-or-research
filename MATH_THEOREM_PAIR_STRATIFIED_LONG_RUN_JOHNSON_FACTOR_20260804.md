# Pair-stratified long-run Johnson factor outside an exponentially small set

**Date:** 2026-08-04  
**Status:** unconditional almost-spanning residence theorem and exact barrier.
It does **not** assert one Hamilton component, immediate-palette
surjectivity, upper decoration, or a lower compiler.

## 1. Pair cells are cubes

Partition `[2r]` into ordered pairs

\[
P_i=\{a_i,b_i\}\qquad(1\le i\le r).
\]

For an `r`-set `T`, let `D(T),E(T),S(T)` be the pair indices on which `T`
has respectively two, zero, and one elements.  Necessarily

\[
 |D(T)|=|E(T)|=t,\qquad |S(T)|=m=r-2t.
\]

Fix disjoint `D,E` of size `t`.  The owners with `D(T)=D,E(T)=E` form an
induced copy of `Q_m`: its `m` bits record which member of each singleton
pair is chosen.  Flipping one cube bit exchanges `a_i` and `b_i`, hence is
one Johnson edge.  Conversely, a Johnson edge that stays in the same cell
must make exactly this exchange.

The number of owners in all cells of singleton dimension `m` is

\[
 N_m=\binom r m\binom{r-m}{(r-m)/2}2^m
     ={r!\over t!^2m!}2^m.                                      \tag{1.1}
\]

## 2. Long-run factor on the good cells

Let `L=L(r)` and put

\[
 M=L+\lceil3\log_2r\rceil.
\]

For every cell with `m\ge M`, apply the cyclic cube Gray code of
Goddyn--Gvozdjak.  Its minimum same-bit transition separation is at least

\[
 m-3\log_2m\ge L.                                                \tag{2.1}
\]

Under the cube embedding, a bit transition toggles both physical
coordinates of its singleton pair.  Those two coordinates therefore have
exactly the same transition gaps as the cube bit.  Coordinates in double
or empty pairs are constant on the cell.  Consequently every selected
Johnson cycle has cyclic positive and negative coordinate runs at least
`L`.

Taking one such cycle in every good cell gives a vertex-disjoint Johnson
cycle factor on every owner whose singleton dimension is at least `M`.

## 3. Exponentially small uncovered owner mass

For every `m`,

\[
 N_m\le 2^r\binom r m,
\]

because the middle binomial coefficient in (1.1) is at most `2^{r-m}`.
Also

\[
 \binom{2r}{r}\ge {4^r\over 2r+1}.
\]

Hence, for `1\le M\le r/2`, the uncovered proportion is at most

\[
 {\sum_{m<M}N_m\over\binom{2r}{r}}
 \le (2r+1)2^{-r}\sum_{m<M}\binom r m
 \le (2r+1)2^{-r}\left({er\over M}\right)^M.            \tag{3.1}
\]

In particular, if `L=O(\sqrt r)`, then `M=O(\sqrt r)` and (3.1) is

\[
 \exp\{-(\log2)r+O(\sqrt r\log r)\}=e^{-\Omega(r)}.       \tag{3.2}
\]

Thus the residence scale needed by the OR problem is achieved on all but
an exponentially small fraction of central owners.

## 4. Exact obstruction to fibrewise completion

This almost-spanning factor cannot be made spanning by choosing better
cube cycles independently.  If `r` is even, the `m=0` cells are singleton
vertices.  If `r` is odd, the minimum cells have `m=1` and induce `Q_1`,
which has no simple spanning cycle.  Therefore every spanning Johnson
cycle or cycle factor must use edges between distinct `(D,E)` cells.

Moreover, the construction has many components and does not price the
immediate palettes.  On a fibre edge the swapped coordinates belong to one
fixed pair; the consecutive intersection has that pair empty and the
consecutive union has it double.  Selecting one Hamilton cycle from each
cube does not by itself make these colours surjective or occurrence-exact.

The remaining residence theorem is therefore a **run-transparent
cross-cell splicing lemma**: join the good cube cycles, absorb every small
cell, and keep all same-coordinate transition gaps at least `L`.  The
exponentially small owner count does not make this an additive-small error,
because every owner is mandatory.

## 5. Consequence and scope

For `L=d(k)+1=Theta(sqrt(k))`, pair stratification plus long-run cube codes
removes residence from `1-e^{-Omega(k)}` of the middle layer.  It does not
prove a resident Hamilton carrier.  What remains is sharply localized to
cross-cell splicing and the palette/upper/compiler gates; no improvement of
the within-cube Gray code can remove that obstruction.

Primary source: L. Goddyn and P. Gvozdjak, *Binary Gray Codes with Long Bit
Runs*, Electronic Journal of Combinatorics 10 (2003), R27,
doi:10.37236/1720.
