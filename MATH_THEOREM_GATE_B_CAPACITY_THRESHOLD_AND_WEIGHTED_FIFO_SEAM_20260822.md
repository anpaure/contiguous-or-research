# Gate B: the sharp punctured-bank capacity threshold and a multiplicity-weighted FIFO seam criterion

**Date:** 2026-08-22  
**Status:** unconditional.  Part I proves an obstruction to the direct route
at its currently stated stopping density.  Part II gives a strictly sharper,
exactly computable sufficient statistic for the FIFO route.  Neither part
assumes an abstract chain assignment in place of literal cyclic rows.

## 1. The direct punctured bank

Fix an integer `r>=2` and put

\[
 b=2r+1,\qquad
 \mathcal M={ [b]\choose r},\qquad
 \mathcal L={ [b]\choose {r-1}},
\]

\[
 A=|\mathcal M|={b\choose r},\qquad
 L=|\mathcal L|={b\choose {r-1}}
   ={r\over r+2}A.                                \tag{1.1}
\]

For a permutation `w=(w_0,...,w_(b-1))`, with subscripts read modulo
`b`, write

\[
 I_k^w(s)=\{w_s,w_{s+1},\ldots,w_{s+k-1}\}.       \tag{1.2}
\]

Its directed punctured configuration is

\[
 E(w)=\{I_r^w(s):s\ne0\}\ \dot\cup\
       \{I_{r-1}^w(s):s\ne0\}.                   \tag{1.3}
\]

The shore tags in (1.3) are understood, so a set on the two shores is not
identified with itself.  Let `P` be any matching of these configurations,
and put `p=|P|`.  Since every member of `P` contains exactly `2r` lower
targets and those targets are disjoint, there is a unique residual fraction
`x in [0,1]` satisfying

\[
                 2rp=(1-x)L.                     \tag{1.4}
\]

For `1<=q<=r-1`, define the two literal same-start inventories

\[
 \mathcal S_q^-(P)=
 \{I_{r-q}^w(s):E(w)\in P,\ s\ne0\},
\]

\[
 \mathcal S_q^+(P)=
 \{I_{r+1+q}^w(s):E(w)\in P,\ s\ne0\},           \tag{1.5}
\]

where these are indexed occurrence multisets.  Their distinct-target hole
counts are

\[
 h_q^-(P)={b\choose {r-q}}-|\operatorname{supp}\mathcal S_q^-(P)|,
\]

\[
 h_q^+(P)={b\choose {r+1+q}}-|\operatorname{supp}\mathcal S_q^+(P)|.
                                                               \tag{1.6}
\]

Complementation makes the two target-layer sizes equal.  Set

\[
                     B_q={b\choose {r-q}}
                         ={b\choose {r+1+q}}.      \tag{1.7}
\]

The support in (1.6) counts **distinct holes**.  Repetitions can only make
that support smaller than its indexed occurrence multiset; no
multiplicity is counted as a hole in what follows.

## 2. Exact occurrence conservation

### Theorem 2.1 (rank-volume lower bound)

For every matching `P` and every `1<=q<=r-1`, one has

\[
 \boxed{
 h_q^-(P)\ge [B_q-(1-x)L]_+,
 \qquad
 h_q^+(P)\ge [B_q-(1-x)L]_+ .}                   \tag{2.1}
\]

Consequently, for every `1<=H<=r-1`,

\[
 \boxed{
 \sum_{q=1}^H\bigl(h_q^-(P)+h_q^+(P)\bigr)
 \ge 2\sum_{q=1}^H[B_q-(1-x)L]_+.}               \tag{2.2}
\]

#### Proof

For each fixed depth and shore, every selected configuration supplies one
indexed target at each of its `2r` retained starts.  Hence both multisets
in (1.5) have exactly

\[
                         2rp=(1-x)L               \tag{2.3}
\]

occurrences.  A multiset with `n` occurrences has support of size at most
`n`, even if all repeated occurrences are ignored when holes are counted.
Subtracting this upper bound for the support from the layer size `B_q`
gives (2.1); summation gives (2.2).  \(\square\)

This bound uses no independence, no pair-codegree estimate, and no
assumption on how the matching was generated.  It therefore survives all
conditioning in an adaptive nibble.

## 3. The one-third residual threshold

The relevant binomial ratios admit a particularly transparent estimate.
For `q>=1`,

\[
 {B_q\over L}
 =\prod_{j=1}^{q-1}{r-j\over r+j+2},              \tag{3.1}
\]

where an empty product is one.  Since

\[
 {r-j\over r+j+2}
 =1-{2j+2\over r+j+2}
 \ge1-{2j+2\over r},                              \tag{3.2}
\]

and `prod(1-u_j)>=1-sum u_j` for `0<=u_j<=1`, (3.1)
gives, whenever `q<=r`,

\[
 \boxed{
 {B_q\over L}\ge
 1-{(q-1)(q+2)\over r}.}                          \tag{3.3}
\]

### Theorem 3.1 (Gaussian-band capacity obstruction)

Assume `0<x<=1`, `rx>=64`, and put

\[
 Q=\min\left\{H,\left\lfloor{\sqrt{rx}\over4}\right\rfloor\right\}.
                                                               \tag{3.4}
\]

Then

\[
 \boxed{
 \sum_{q=1}^H\bigl(h_q^-(P)+h_q^+(P)\bigr)
 \ge {7\over4}xLQ.}                              \tag{3.5}
\]

In particular, if

\[
 H\ge\left\lfloor{\sqrt{rx}\over4}\right\rfloor,
\]

then

\[
 \boxed{
 \sum_{q=1}^H\bigl(h_q^-(P)+h_q^+(P)\bigr)
 \ge {7\over32}L\sqrt r\,x^{3/2}.}              \tag{3.6}
\]

#### Proof

For `1<=q<=Q`, the definition of `Q` and `rx>=64` give

\[
 {(q-1)(q+2)\over r}
 \le {q(q+2)\over r}
 \le {x\over16}+{1\over2}\sqrt{x\over r}
 \le {x\over8}.                                  \tag{3.7}
\]

The last inequality uses
`sqrt(x/r)=x/sqrt(rx)<=x/8`.  Equations (3.3) and
(3.7) imply

\[
 B_q-(1-x)L\ge {7x\over8}L.                       \tag{3.8}
\]

Apply (2.2) at these `Q` depths to obtain (3.5).  If `H` is at least the
untruncated value in (3.4), then, writing `y=sqrt(rx)>=8`,

\[
 \left\lfloor{y\over4}\right\rfloor
 \ge {y\over8}.                                   \tag{3.9}
\]

Substitution in (3.5) proves (3.6).  \(\square\)

### Corollary 3.2 (sharp necessary density scale)

Suppose `rx->infinity` and

\[
 H\ge\left\lfloor{\sqrt{rx}\over4}\right\rfloor.
\]

If the physical all-depth requirement

\[
 \sum_{q=1}^H(h_q^-+h_q^+)=o(A)                  \tag{3.10}
\]

holds, then necessarily

\[
                         \boxed{x=o(r^{-1/3}).}    \tag{3.11}
\]

In particular, for any fixed `alpha<=1/3`, a residual density

\[
                         x=r^{-\alpha}(1+o(1))     \tag{3.12}
\]

cannot satisfy (3.10) for

\[
 H=\left\lceil\sqrt{b\log b}\right\rceil.        \tag{3.13}
\]

For `alpha<1/3`, the lower bound divided by `A` even grows as
`Omega(r^((1-3alpha)/2))`; at `alpha=1/3` it stays bounded below by a
positive constant.

#### Proof

By (1.1), `L/A=r/(r+2)=1-o(1)`.  Thus (3.6) and (3.10)
force

\[
                         \sqrt r\,x^{3/2}=o(1),
\]

which is equivalent to (3.11).  Under (3.12), condition (3.13) is much
larger than `sqrt(rx)/4`, and the stated powers follow directly from
(3.6).  \(\square\)

The current stopped punctured-nibble theorem uses a fixed exponent
`alpha<1/3` (indeed a much smaller exponent).  Corollary 3.2 shows that
its output cannot, by itself, pass the currently stated Gate B.  This is
an occurrence-capacity obstruction, not a failure of a proposed
concentration proof.

The exponent `1/3` is sharp for this numerical obstruction alone.  Indeed,
from (3.1) and `1-u<=exp(-u)`,

\[
 {B_q\over L}
 \le \exp\left\{-{(q-1)(q+2)\over2(r+1)}\right\}. \tag{3.14}
\]

If `0<x<=1/2` and `B_q>(1-x)L`, then (3.14) and
`-log(1-x)<=2x` imply

\[
                         (q-1)(q+2)<4(r+1)x.       \tag{3.15}
\]

There are therefore only `O(1+sqrt(rx))` positive summands in the
rank-volume expression on the right of (2.2), and each is at most `xL`.
Consequently

\[
 2\sum_{q=1}^H[B_q-(1-x)L]_+
 =O\bigl(Ax(1+\sqrt{rx})\bigr)=o(A)                \tag{3.16}
\]

when `x=o(r^(-1/3))`, uniformly in `H`.  This says only that raw capacity
then ceases to obstruct the theorem; it does not make the occurrences
distinct.

### Corollary 3.3 (restoring the punctures does not change the threshold)

For any asymptotic sequence of punctured matchings, complete each selected
permutation to its full cyclic row by also using the start `s=0`.  The
resulting full bank has

\[
bp=\left(1+{1\over2r}\right)(1-x)L              \tag{3.17}
\]

occurrences at every rank.  Whenever `x>=2/r`, its effective occurrence
deficit relative to `L` is at least `3x/4`.  Hence the conclusion
`x=o(r^(-1/3))` remains necessary for Gaussian-band `o(A)` holes.

#### Proof

The effective deficit is

\[
 1-{bp\over L}
 =x-{1-x\over2r}
 \ge x-{1\over2r}\ge {3x\over4}.                 \tag{3.18}
\]

If `x=o(r^(-1/3))` there is nothing to prove.  Otherwise, on some
subsequence `x>=epsilon r^(-1/3)` for a fixed `epsilon>0`.  Along that
subsequence `x>=2/r`, the effective deficit in (3.18) has `r` times that
deficit tending to infinity, and Theorem 3.1 applies.  Changing an
absolute constant does not change the exponent `1/3`.  Indices with
`x<2/r` already have `x=O(1/r)=o(r^(-1/3))`.  \(\square\)

### Corollary 3.4 (size of a required cover-down)

Suppose `x>>r^(-1/3)`.  Merely removing the rank-volume obstruction by
adjoining full physical rows requires

\[
                         \Omega(xL/b)
                         =\Omega(x\operatorname{Cat}_r)       \tag{3.19}
\]

additional rows.  Conversely, `O(x Cat_r)` additional rows are enough
only to repair the **numerical occurrence count**.  This is not a
construction theorem: the new rows must still respect the central target
capacities and must place their windows on distinct missing targets at all
relevant depths.

#### Proof

Each new full row adds exactly `b` indexed occurrences at every depth.
To change a deficit of order `xL` to `o(r^(-1/3))L` therefore needs at
least `(x-o(r^(-1/3)))L/b` rows.  Since

\[
 {L\over b}={r\over r+2}{A\over b}
            =(1-o(1))\operatorname{Cat}_r,        \tag{3.20}
\]

this is (3.19).  The same arithmetic shows that this order of magnitude
can supply enough raw occurrences, but arithmetic alone says nothing
about their distinctness or legality.  \(\square\)

Thus the direct architecture needs one of two new inputs before order
correlations can possibly close Gate B:

1. continue the central matching/cover-down to residual
   `x=o(r^(-1/3))`; or
2. add `Theta(x Cat_r)` compatible physical rows by a separate integral
   cover-down theorem.

## 4. FIFO paths and literal surviving windows

We now give a sharper statistic for the independent FIFO alternative.
This part does not repair the direct capacity obstruction above.

Put `n=2m+1`.  Let

\[
 P_*=(X_0,X_1,\ldots,X_N),\qquad X_i\in{[n]\choose m},             \tag{4.1}
\]

be a simple Johnson path, oriented by

\[
 X_{i+1}=X_i-\{r_i\}+\{a_i\}.                    \tag{4.2}
\]

A cyclic FIFO row is a permutation `C` of `[n]` with states

\[
                         I_C(i,m)=\{C_i,\ldots,C_{i+m-1}\}.       \tag{4.3}
\]

Transition `i` prescribes the two phase ports

\[
                         C_i=r_i,\qquad C_{i+m}=a_i              \tag{4.4}
\]

with phases modulo `n`.  Two ports **conflict** if they assign unequal
labels to one phase or assign one label to distinct phases.  For every
conflicting pair on transition indices `i<j`, form the integer interval
`[i,j]`.  Also include every interval of `n` consecutive transitions.
Call the resulting family `C_FIFO`.

A cut set `C subseteq {0,...,N-1}` is **FIFO-admissible** if it hits every
interval in `C_FIFO`.  Every component left after these cuts has fewer than
`n` transitions and a well-defined injective phase map (4.4).  Completing
that map to a permutation gives a literal cyclic row whose trace contains
the component.  Rebase phases at the first state of each component; this
subtracts one constant modulo `n` and therefore preserves all port
conflicts.  To see the last assertion directly, the assigned removal
phases among `0,...,m-1` are distinct elements of `X_0`; if the arc is
shorter than `m`, fill the remaining phases by the unused elements of
`X_0`.  None of those unused elements is already an arrival label: an
arrival is absent immediately before it arrives, so it cannot be an
as-yet-unremoved member of `X_0`, and injectivity prevents it from being
an earlier removed member at a distinct phase.  Equation (4.2) then
inductively agrees with (4.3).  Thus this is a physical row completion,
not merely an abstract chain completion.

For `1<=q<=m-1` and `0<=i<=N-q`, put

\[
 T_{q,i}=\bigcap_{t=0}^qX_{i+t}.                  \tag{4.5}
\]

Call `(q,i)` **valid** when `|T_(q,i)|=m-q`, and define its target
multiplicity

\[
 a_q(T)=|\{i:(q,i)\text{ is valid and }T_{q,i}=T\}|.             \tag{4.6}
\]

The path's depth-`q` hole count is

\[
 h_q^P={n\choose {m-q}}-|\{T:a_q(T)>0\}|.         \tag{4.7}
\]

The occurrence `(q,i)` survives the recut exactly when none of its `q`
internal transitions is cut, that is,

\[
                         C\cap[i,i+q-1]=\varnothing.             \tag{4.8}
\]

This criterion refers to the same consecutive states and the same cut
set used to form the physical rows.

## 5. Multiplicity-weighted seam exposure

For a cut position `c`, define its normalized depth-`H` seam load

\[
 \omega_H(c)=
 \sum_{q=1}^H
 \sum_{\substack{0\le i\le N-q\\(q,i)\ {\rm valid}\\
                   c\in[i,i+q-1]}}
 {1\over a_q(T_{q,i})}.                           \tag{5.1}
\]

Unlike the generic charge `sum_(q<=H)q`, a target occurring `a` times
charges only `1/a` at each occurrence.  The normalization is forced by the
following exact argument.

### Theorem 5.1 (weighted physical-recut ledger)

Let `C` be FIFO-admissible.  Complete every component to a cyclic FIFO row,
and let `h_(m-q)^row` be the number of rank-`(m-q)` targets missing from
the completed row bank.  Then

\[
 \boxed{
 \sum_{q=1}^H h_{m-q}^{\rm row}
 \le \sum_{q=1}^Hh_q^P+\sum_{c\in C}\omega_H(c).}               \tag{5.2}
\]

Complementation inside the same completed rows gives

\[
 h_{m-q}^{\rm row}=h_{m+1+q}^{\rm row},           \tag{5.3}
\]

and hence

\[
 \boxed{
 \sum_{q=1}^H
 (h_{m-q}^{\rm row}+h_{m+1+q}^{\rm row})
 \le2\sum_{q=1}^Hh_q^P+2\sum_{c\in C}\omega_H(c).}             \tag{5.4}
\]

#### Proof

For a path target `T` with `a_q(T)>0`, let `d_q(T;C)` be the number of its
occurrences whose interval in (4.8) meets `C`.  Before the row completions
add any new windows, `T` disappears precisely when

\[
                         d_q(T;C)=a_q(T).          \tag{5.5}
\]

Therefore the exact inherited hole count is

\[
 h_q^P+|\{T:a_q(T)>0,\ d_q(T;C)=a_q(T)\}|.        \tag{5.6}
\]

Completion can only add windows.  Moreover,

\[
 {\bf1}_{d_q(T;C)=a_q(T)}
 \le {d_q(T;C)\over a_q(T)}.                      \tag{5.7}
\]

Sum (5.7), expand every destroyed occurrence, and then union-bound the
possibly several cuts crossing its interval.  The result is exactly the
right side of (5.2).  In a cyclic row on `2m+1` labels, the complement of
a length-`(m-q)` window is a shifted length-`(m+1+q)` window.  This proves
(5.3) within the same physical rows and hence (5.4).  \(\square\)

The load has an exact global normalization:

### Proposition 5.2 (load-mass identity)

\[
 \boxed{
 \sum_{c=0}^{N-1}\omega_H(c)
 =\sum_{q=1}^H q\,|\{T:a_q(T)>0\}|
 =\sum_{q=1}^Hq\left({n\choose {m-q}}-h_q^P\right).}            \tag{5.8}
\]

#### Proof

Every valid occurrence `(q,i)` contains exactly `q` possible cut
positions.  For a fixed target `T`, its `a_q(T)` occurrences therefore
contribute

\[
                         a_q(T)q/a_q(T)=q
\]

to the left side.  Sum over the support and use (4.7).  \(\square\)

The old bound follows by discarding the multiplicity weights:
`omega_H(c)<=sum_(q<=H)q`, so (5.4) implies the generic
`H(H+1)|C|` seam term.  The converse need not hold: (5.4) can be `o(W)`
even when that generic expression is too large, provided the compulsory
cuts lie at positions of unusually small normalized load.

## 6. An exact weighted interval statistic

For the saturating path, now take `N=binom(n,m-1)` and put

\[
 W={n\choose m},\qquad B={W\over n}=\operatorname{Cat}_m.       \tag{6.1}
\]

Define

\[
 \Lambda_H(P_*)=
 \min\left\{\sum_{c\in C}\omega_H(c):
       C\text{ is FIFO-admissible and }|C|=B-1\right\},         \tag{6.2}
\]

with value `+infinity` if no such set exists.

### Theorem 6.1 (correct sufficient statistic for the FIFO route)

If

\[
 \boxed{
 \sum_{q=1}^Hh_q^P+\Lambda_H(P_*)=o(W),}           \tag{6.3}
\]

then the same literal saturating path can be recut and completed into
exactly `B` physical cyclic rows whose aggregate lower/upper holes through
depth `H` are `o(W)`.

The statistic `Lambda_H` is computable by an exact polynomial-time dynamic
program.  Thus (6.3), unlike an abstract chain-supply condition, is a
finite physical certificate on the actual removal/arrival path.

#### Proof

Choose a minimizer in (6.2).  Its `B-1` deleted transitions make exactly
`B` nonempty path components, and FIFO admissibility completes all of them
to physical rows as in Section 4.  Apply (5.4) and (6.3).

For the algorithm, adjoin sentinel positions `-1` and `N`.  For
`-1<=u<v<=N`, call the directed gap `u->v` admissible when there is no
mandatory interval `[l,s] in C_FIFO` satisfying

\[
                         u<l\le s<v.               \tag{6.4}
\]

A sequence

\[
 -1=c_0<c_1<\cdots<c_{B-1}<c_B=N                 \tag{6.5}
\]

has all its consecutive gaps admissible if and only if
`{c_1,...,c_(B-1)}` hits every mandatory interval.  Give each interior
vertex `c` weight `omega_H(c)` and the sentinels weight zero.  A shortest
path from `-1` to `N` using exactly `B` admissible arcs minimizes (6.2).
The recurrence over the last vertex and the number of arcs takes
`O(BN^2)` arithmetic operations after the admissible-gap table is built.
This proves exact computability and the theorem.  \(\square\)

## 7. Consequences for the proof architecture

The two conclusions are logically separate and both concern literal
physical coinstantiation.

1. **Direct punctured route.**  The current residual
   `x=r^(-alpha)` with fixed `alpha<1/3` cannot meet the Gaussian-band
   Gate B, regardless of how favorable its order correlations are.
   A cover-down below `o(r^(-1/3))`, or an integral addition of order
   `x Cat_r` compatible rows, is necessary before all-depth collision
   estimates become relevant.

2. **FIFO route.**  The raw `q`-per-cut ledger is not the correct final
   statistic.  The precise sufficient statistic is the minimum
   multiplicity-normalized seam load `Lambda_H` subject to the very same
   FIFO conflict intervals and the exact row count.  Proving (6.3) remains
   open, but it is strictly sharper than demanding the impossible generic
   `H^2B=o(W)` bound and is directly checkable on any proposed rainbow
   path.

No statement above claims that raw occurrence capacity implies distinct
target coverage.  Part I is a necessary obstruction; Part II is a
sufficient physical-recut theorem.
