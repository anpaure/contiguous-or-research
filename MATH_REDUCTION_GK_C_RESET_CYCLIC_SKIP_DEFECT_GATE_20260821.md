# The cyclic-skip defect gate for `c`-reset GK/FIFO macros

**Status (2026-08-21).**  This note proves a counting reduction for the
fixed interleaved Greene--Kleitman compiler with `c` reset steps per
`b`-scale macro.  Three explicit structural estimates, stated in
Hypothesis 3.1, would imply that every reset width whose seam cost is
`o(W_b)` has only `o(W_b)` recurrent source support.  Those estimates are
not proved here.  Exact finite graphs support them after small winding
resonances are separated.

This is therefore a rigorous conditional no-go, not an unconditional
physical obstruction.  It does not address variable macro lengths,
nonperiodic reset placement, or a different symmetric-chain
decomposition.

## 1. The exact `c`-reset macro graph

Fix `1<=c<b` and put `s=b-c`.  An ordered macro start is

\[
 q=(p_1,\ldots,p_s,R_1,\ldots,R_c)=(P,R),           \tag{1.1}
\]

with distinct entries in `[0,2b-1]`.  Run `s` strong GK first-successor
steps, in the sense of Theorem 2.1 of

`MATH_REDUCTION_GK_STRONG_FIFO_MACRO_RESET_CORE_20260821.md`.

If their forced additions are `F=(f_1,...,f_s)`, FIFO gives endpoint

\[
                       (R,F).                        \tag{1.2}
\]

Then make `c` legal arbitrary FIFO resets, producing the next start
`(F,R')`.  This gives a finite directed graph `G_(b,c)`.  Its directed
cycle support is exactly the family usable by a cyclic compiler with this
fixed block pattern.  Sequential reset legality is important: at reset
`j`, the new letter must avoid the remaining old sentinels, all of `F`,
and the previously appended new sentinels.

Every forced addition is below the current source maximum.  Consequently,
if `m` is the largest coordinate used anywhere on a directed cycle, `m`
never occurs in a forced block `P`; whenever it occurs, it is a reset
sentinel.  This is the same maximum-label argument as Proposition 3.1 of
the cited note.

## 2. Cyclic skip defect

Put

\[
                         M=2b-1.                     \tag{2.1}
\]

For a forced block `P=(p_1,...,p_s)` on a directed cycle, define `d_i` by

\[
 p_{i+1}-p_i\equiv-d_i\pmod M,
 \qquad d_i\in\{1,3,5,\ldots,M-2\}.                 \tag{2.2}
\]

The odd representative always exists.  Away from `k=1`, consecutive
strong additions decrease and have opposite parity.  At a flat
`k=1 -> k=1` transition they increase by an even amount; modulo the odd
number `M`, this is again a negative odd step.

Define

\[
 \eta(P)=\sum_{i=1}^{s-1}{d_i-1\over2},
 \qquad
 D(P)=\sum_i d_i=s-1+2\eta(P).                       \tag{2.3}
\]

Call `P` **nonwinding** when `D(P)<M`.  In that case the modular walk in
(2.2) has a strictly decreasing lift, and `eta(P)` is literally the total
number of skipped coordinate pairs between consecutive entries.

For every `K>=1`, the number of ordered prefixes with `eta(P)<=Kc` is at
most

\[
 M {s-1+Kc\choose Kc}.                               \tag{2.4}
\]

Indeed, after choosing `p_1`, put `e_i=(d_i-1)/2`.  The nonnegative vector
`(e_i)` has sum at most `Kc` and determines all later entries modulo `M`.
Allowing repeated entries only enlarges the upper bound.  After choosing
the `c` ordered sentinels, the number of low-defect starts is therefore at
most

\[
 N_{\rm low}(b,c;K)
 \le M {s-1+Kc\choose Kc}(2b)^c
 =\exp(O_K(c\log b)).                                \tag{2.5}
\]

## 3. Three exact analytic gates

### Hypothesis 3.1 (winding, adjacent defect, and reverse multiplicity)

There are absolute constants `A,B,K` such that, whenever

\[
                         b\ge A c^2,                  \tag{3.1}
\]

the following hold on the directed cycle support of `G_(b,c)`.

1. **No winding.**  Every forced block `P` has `D(P)<M`.
2. **Adjacent-low property.**  If a macro maps forced prefix `P` to
   forced output `F`, then
   \[
                         \min\{\eta(P),\eta(F)\}\le Kc. \tag{3.2}
   \]
3. **Reverse multiplicity.**  For fixed output block `F` and fixed ordered
   old sentinel tuple `R`, at most `(2b)^(Bc)` strong macro starts `(P,R)`
   have output `F`.

The bracket interpretation suggests `K=2`: every unit of `eta` is one
matched pair in a cyclic Dyck block between consecutive additions; over a
full `b-c` sweep, an unanchored pair is consumed, while the two sides of
the seam offer only `2c` persistent anchors.  This is motivation, not a
proof of (3.2).

### Theorem 3.2 (conditional recurrent-support bound)

Under Hypothesis 3.1, the number of ordered macro states on directed
cycles of `G_(b,c)` is

\[
                 \exp(O_{K,B}(c\log b)).              \tag{3.3}
\]

Their union contains at most

\[
                 b\exp(O_{K,B}(c\log b))              \tag{3.4}
\]

distinct middle sources.

#### Proof

Call a cyclic vertex low when its prefix has `eta<=Kc`.  Equation (2.5)
bounds all low vertices.  By (3.2), every high vertex has low forced output
`F`.  Choose that low `F`, choose its old sentinel tuple `R` in at most
`(2b)^c` ways, and invoke reverse multiplicity to recover at most
`(2b)^(Bc)` high predecessors.  This proves (3.3).  A macro contains at
most `b` source states, giving (3.4).  \(\square\)

### Corollary 3.3 (conditional failure throughout the cheap-seam range)

Let

\[
 H=\Theta(\sqrt{b\log b}),\qquad
 c=o(b/H).                                            \tag{3.5}
\]

If Hypothesis 3.1 holds uniformly in this range, then the recurrent source
union is `o(W_b)`, where `W_b=binomial(2b,b)`.  In fact

\[
 c\log b=o(b),\qquad
 b\exp(O(c\log b))=\exp(o(b))=o(W_b).                \tag{3.6}
\]

Meanwhile the sacrificed reset-chain incidence cost is at most

\[
                  O(cH W_b/b)=o(W_b).                 \tag{3.7}
\]

Indeed, among each `b`-transition macro only its `c` reset positions are
sacrificed, and each such position carries at most `H` target incidences;
on a `W_b`-scale source ledger this is the fraction `c/b` charged in
(3.7).

Thus, conditionally, every reset width cheap enough for the retirement
ledger is far too small to give near-total recurrent source support.

## 4. Exact diagnostics and the small winding resonance

The exact graph builders are

* `scratch/research_gk_length_b_macro_reset_core_20260821.py` for `c=1`;
* `scratch/research_gk_two_reset_macro_core_20260821.py` for `c=2`;
* `scratch/research_gk_c_reset_macro_core_20260821.py` for general `c`.

They enforce full strong-prefix compatibility, sequential reset legality,
and exact SCC support.  The data show:

* at `c=1`, recurrent prefixes have `eta<=1` in the tested stable range;
* at `c=2`, the maximum is `eta=10` at `b=8,9,10`, but drops to `eta=4`
  by `b=13` and remains `4` through `b=17` in the extended diagnostic;
* the exceptional `c=2` blocks wind around the `M`-cycle.  For example,
  at `b=8`, `eta=10` gives `D=25>M=15`;
* once adjacent blocks are both nonwinding, the exact recurrent scans give
  `min(eta(P),eta(F))<=2c` through the tested range;
* the largest observed reverse multiplicity for fixed `(F,R)` is `13` at
  `(c,b)=(1,15)` and `209` at `(c,b)=(2,13)`, consistent with a `b^c`
  bound.

These observations explain the three clauses of Hypothesis 3.1 but do not
replace their proofs.  In particular, the sharper claim that every
recurrent prefix has at most `2c+1` ordinary descending coordinate
intervals is false: at `(c,b)=(2,8)`, the recurrent prefix

\[
                        (4,12,9,6,3,0)                \tag{4.1}
\]

has six such intervals.
