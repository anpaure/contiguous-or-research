# Audit of the concentric-ring monotone-band obstruction

## 1. Verdict

The core obstruction in `THREE_BOX_SPIRAL_BAND_OBSTRUCTION.md` is correct.
For any central witness order consisting of contiguous complete hexagonal
rings, with physical length `M_a+O(a)`, coordinatewise factorability forces

\[
                  Q\leq3a^3+O(a^2)
\]

physical intervals avoiding every middle witness.  The lower half contains

\[
                  4a^3+O(a^2)
\]

distinct targets, so no such monotone band can be universal.

The proof applies to outward or inward radius order, reversed traversal,
arbitrary corner cuts, and indeed any permutation of the complete ring
blocks.  It does **not** apply once arcs from different radii are genuinely
interleaved.

One sentence in the broad `O(a)`-repetition extension needs a repair:
inserted `1` occurrences can lengthen a selected maximal run beyond `a+1`.
Charging these extensions explicitly costs only `O(a^2)`, so the theorem and
its leading constant remain valid.  The unmodified closed spiral has no such
issue because its repeated cut vertices do not extend the two selected
internal positive-extreme sides.

## 2. Exact avoidance ledger

Let physical positions be `[1,N]`, and let

\[
 I_i=[\ell_i,r_i],\qquad
 \ell_1<\cdots<\ell_L,quad r_1<\cdots<r_L.
\]

For a physical start `x`, let `i` be the first index with `ell_i>=x`.  The
interval `[x,y]` avoids every complete `I_j` exactly up to `y=r_i-1`, so it
has `r_i-x` allowed endpoints.  Therefore the exact count is

\[
\begin{split}
 Q={}&\sum_{x=1}^{\ell_1}(r_1-x)
 +\sum_{i=2}^L\left(\Delta_iw_i+{\Delta_i\choose2}\right)\\
 &+{N-\ell_L+1\choose2},                            \tag{2.1}
\end{split}
\]

where

\[
 w_i=r_i-\ell_i,qquad \Delta_i=\ell_i-\ell_{i-1}.
\]

The last term counts starts strictly after `ell_L`; the displayed binomial is
`(N-ell_L)(N-ell_L+1)/2`.

In monotone-band form

\[
 \ell_i=i+\alpha_i,qquad r_i=i+\beta_i,qquad
 0\leq\alpha_i\leq\beta_i\leq D,
\]

one has

\[
 \Delta_i=1+(\alpha_i-\alpha_{i-1}),qquad
 \sum_i(\Delta_i-1)\leq D.
\]

Hence

\[
 \sum_i(\Delta_i-1)w_i\leq D^2,
 \qquad
 \sum_i{\Delta_i\choose2}=O(D^2).
\]

If `N-L=O(D)`, both boundary terms in (2.1) are also `O(D^2)`, proving

\[
                         Q\leq\sum_iw_i+O(D^2).       \tag{2.2}
\]

This part is exact.  Every below-middle witness must be counted by `Q`, since
an interval containing one complete middle witness has an OR containing a
middle-rank mask.

## 3. Factorability inequality

For an internal positive incidence run `[u,v]`, all positions through
`r_(u-1)` are forbidden by the preceding zero interval and every position
from `ell_(v+1)` onward is forbidden by the following zero interval.  A legal
pin exists only if

\[
                  r_{u-1}+1\leq\ell_{v+1}-1,
\]

equivalently

\[
 r_{u-1}+2\leq\ell_{v+1},qquad
 \beta_{u-1}-\alpha_{v+1}\leq v-u.                  \tag{3.1}
\]

Earlier zero intervals end still earlier and later zero intervals start still
later, so the immediate neighboring zeros give the exact separation gate.
Necessity in Lemma 2 is correct.

## 4. Density of selected extreme runs

On every radius-`s` ring the three positive extreme sides

\[
                         x=s,\qquad y=s,qquad z=s
\]

are threshold incidence runs of `s+1` vertices.  A cut meets at most one of
these sides, so two remain internal under either traversal orientation.

Within a ring, and from the second selected side to the first selected side of
the next complete ring block, the distance is `O(a)`.  This remains true if
the ring blocks are permuted: one traverses at most the remainder of one
`6s`-cycle, the beginning of one `6t`-cycle, and one selected side.  Reversal
only exchanges prefixes and suffixes.  The final uncharged suffix is one ring
block and therefore `O(a)`.

Thus every nonfinal index can be assigned a following internal run `[u,v]`
with

\[
 i\leq u-1,qquad v+1-i\leq C a+O(1),qquad v-u\leq a, 
                                                               \tag{4.1}
\]

for an absolute constant `C`.  The exact numerical `5` is suitable for the
standard outward order; only `O(a)` is needed for arbitrary block order.

## 5. Charging audit

For the run assigned to `i`, monotonicity and (3.1) give

\[
\begin{split}
 w_i&=\beta_i-\alpha_i
 \leq\beta_{u-1}-\alpha_i\\
 &\leq(v-u)+\alpha_{v+1}-\alpha_i
 \leq a+\alpha_{v+1}-\alpha_i.                     \tag{5.1}
\end{split}
\]

Write `delta_j=alpha_j-alpha_(j-1)`.  A fixed increment `delta_j` appears in
`alpha_(v(i)+1)-alpha_i` only if

\[
                         i<j\leq v(i)+1.
\]

By (4.1), at most `Ca+O(1)` indices `i` can charge it.  Since
`sum_j delta_j<=D`,

\[
 \sum_i(\alpha_{v(i)+1}-\alpha_i)=O(aD).             \tag{5.2}
\]

The final `O(a)` indices contribute `O(aD)`.  Therefore

\[
                         \sum_iw_i\leq aL+O(aD).      \tag{5.3}
\]

With `L=3a^2+O(a)` and `D=O(a)`, equations (2.2) and (5.3) yield

\[
                         Q\leq3a^3+O(a^2).           \tag{5.4}
\]

The charging is not circular and does not multiply-count targets: it bounds
the sum of all physical avoidance capacities before those intervals are
assigned to targets.

## 6. Repair for arbitrary extra occurrences

Suppose `R=O(a)` extra occurrences are inserted arbitrarily.  A chosen
extreme-side run can then have

\[
                         v-u\leq a+e_\rho,
\]

where `e_rho` is the number of inserted `1` occurrences extending that
particular maximal run.  The selected run blocks are disjoint, so

\[
                         \sum_\rho e_\rho\leq R=O(a).
\]

Every run is charged by only `O(a+R)=O(a)` preceding indices.  Consequently

\[
 \sum_i e_{\rho(i)}
   \leq O(a)\sum_\rho e_\rho=O(a^2).                 \tag{6.1}
\]

Extra occurrences in gaps enlarge the charging radius in (4.1) by at most
`R=O(a)`, so (5.2) remains `O(aD)`.  Boundary extras contribute `O(aD)`.
Thus the correction in (6.1) is lower order and (5.4) is unchanged.

Alternatively, if the extras are duplicate middle witnesses, select only one
witness for each of the `M_a` distinct middle targets.  The remaining open
ring blocks still contain two internal extreme sides, and their strict
endpoint family has the same `D=O(a)` normal form.

## 7. Scope

The theorem covers:

* outward or inward ordering of the radii;
* either orientation on every ring;
* arbitrary corner cuts and coordinate relabelings;
* any permutation of complete contiguous ring blocks; and
* `O(a)` repetitions or auxiliary occurrences, with the correction above.

It does not cover:

* an ordering that genuinely interleaves arcs from many radii;
* a central skeleton not containing two `O(a)`-dense internal extreme runs
  per `O(a)` occurrences;
* physical witness order different from the ring order; or
* constructions whose total endpoint slack is not `O(a)`.

The conclusion is therefore sharp in architectural scope:

> Perfect shadow completeness of the concentric rings is compatible with a
> factorable upper-half word, but any width-plus-perimeter monotone band whose
> middle witness order keeps whole rings contiguous has too little avoidance
> capacity to encode the lower half.

