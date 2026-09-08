# The punctured boundary-codegree gate via Venn-gap refinement

**Date:** 2026-08-21  
**Status:** analytic theorem

## 1. Statement

Put `b=2r+1`, and let `e` be the identity directed punctured
configuration.  Thus its targets are the cyclic intervals

\[
 M_i=\{i,\ldots,i+r-1\},\qquad
 L_i=\{i,\ldots,i+r-2\},\qquad i\ne0,
\]

with layer tags retained.  Represent a target of length `k` and start `i`
by the boundary edge `\{i,i+k\}` on the cut circle.  For
`T\subseteq e`, write

\[
 t=|T|,\qquad q=|V(B(T))|,
 \qquad D_M=(b-1)r!(r+1)!.
\]

### Theorem 1.1 (boundary-codegree gate)

There is an absolute constant `C` such that, for every `r>=2` and every
`T\subseteq e` with `t>=2`,

\[
 \boxed{\qquad
       {\deg(T)\over D_M}\le C^t r^{2-q}.
       \qquad}                                             \tag{1.1}
\]

For example, the proof below permits
`C=32(3e)^2`; no optimization is intended.

The estimate is global.  In particular, it does not assert that every
boundary vertex can be paid for by a separate reverse conditional
probability.  The matching family
`\{M_1,\ldots,M_r\}` shows that such a pointwise peeling statement is
false.

## 2. Positional multiplicity costs only `4^t`

For `k,h` in `\{r,r-1\}` and an intersection size `a`, let
`m_{k,h}(a)` be the number of relative cyclic starts of a length-`h` arc
when the start of a length-`k` arc is fixed.  The elementary two-arc
calculation gives

\[
 m_{k,h}(a)=
 \begin{cases}
 b-k-h+1,&a=0,\\
 2,&0<a<\min(k,h),\\
 |k-h|+1,&a=\min(k,h).
 \end{cases}                                             \tag{2.1}
\]

Consequently

\[
 m_{r,r}(a)\le2,qquad
 m_{r,r-1}(a)\le3,qquad
 m_{r-1,r-1}(a)\le4                              \tag{2.2}
\]

for distinct targets.

In particular, the disjoint cases have respectively `2,3,4` relative
starts in the layer patterns `MM,ML,LL`; all proper positive overlaps have
two, and the only cross-layer containment case also has two.

Let `n_sigma`, `sigma in {0,1}^T`, be the labelled Venn-cell sizes of
`T` in the identity order, and put

\[
                         V(T)=\prod_\sigma n_\sigma! .          \tag{2.3}
\]

Choose one target of `T` as an anchor.  Its retained positional start has
at most `b-1` choices.  Once that start is fixed, (2.2), applied only to
the intersection size with the anchor, gives at most four possible starts
for each remaining target.  Therefore the number `P(T)` of retained
ordered positional start tuples having the prescribed labelled Venn
signature satisfies

\[
                         P(T)\le(b-1)4^{t-1}.                    \tag{2.4}
\]

For a fixed positional tuple, labels can be assigned independently inside
corresponding Venn cells in exactly `V(T)` ways.  Conversely, every proper
nonempty target has a unique cyclic start in a fixed word.  This is the
within-layer simplicity used here: two start tuples cannot count the same
word.  Hence

\[
                         \deg(T)=P(T)V(T).                       \tag{2.5}
\]

## 3. Venn cells versus elementary boundary gaps

List the `q` distinct boundary cuts of `B(T)` cyclically.  They partition
the `b` coordinate positions into positive elementary gaps of lengths

\[
                   g_1,\ldots,g_q,qquad \sum_i g_i=b,
\]

on each of which the complete membership vector is constant.  Put

\[
                         G(T)=\prod_{i=1}^q g_i!.                \tag{3.1}
\]

Different gaps may have the same membership vector, so `V(T)` may exceed
`G(T)`.  The following lemma bounds exactly that merging loss.

### Lemma 3.1 (constant Venn-gap refinement loss)

For every nonempty `T`,

\[
                         V(T)\le8^{t-1}G(T).                    \tag{3.2}
\]

#### Proof

Expose the targets one at a time, and write `R=V/G`.  For one target its
two Venn cells are exactly its two elementary gaps, so `R=1`.

Suppose an additional target `A` is exposed.  If an old Venn cell `C` of
size `n_C` contains `p_C` labels of `A`, its factorial contribution is
multiplied by

\[
                         {p_C!(n_C-p_C)!\over n_C!}
                         ={1\over {n_C\choose p_C}}.             \tag{3.3}
\]

A new boundary cut which divides an old elementary gap of size `g` into
parts `a,g-a` multiplies `G` by `1/{g\choose a}`.

First suppose the two new cuts lie in different old gaps.  In each old
Venn cell, fix the actual labels of `A` in every whole old gap and in the
part of the cell away from the split gaps.  Independently choosing the
prescribed number of labels from every split gap, and adjoining that fixed
set, injects into the `p_C`-subsets of the cell.  This remains an injection
when both endpoint gaps belong to the same old Venn cell.  Thus

\[
       \prod_{\substack{\text{split gaps }H\subseteq C}}
             {|H|\choose |A\cap H|}
       \le {n_C\choose p_C}.                           \tag{3.4}
\]

Multiplying (3.4) over the old cells shows that `R` cannot increase.
If exactly one endpoint is a new cut, the same argument uses its one split
gap.  If both endpoints are old cuts, `G` is unchanged while (3.3) can
only decrease `V`.  Thus coincident old endpoints cause no loss.

It remains to treat two new cuts in one old gap.  Once the first target
has been exposed, every old gap lies inside one of its two complementary
arcs and therefore has size at most `r+2`.  Write the three new pieces of
the old gap as `x,y,z`, where `y` is the segment between the new cuts
which stays inside the old gap.  Since `A` has length `k` in
`\{r-1,r\}`, necessarily

\[
                         y\in\{k,b-k\}.                         \tag{3.5}
\]

The gap-refinement factor is

\[
                  {g!\over x!y!z!}
                    ={g\choose y}{g-y\choose x}.                \tag{3.6}
\]

The old gap belongs to a Venn cell of size `n>=g`.  If the length-`k`
arc is the middle segment, that cell is split with its selected part of
size `y`.  If the complement of the arc is the middle segment, its
*unselected* part has size `y`, and binomial symmetry gives the same
denominator `{n\choose y}`.  In either case this is at least
`{g\choose y}`.  Now `g<=r+2`; if `y=k`, then `g-y<=3`, while if
`y=b-k`, then `g-y<=1`.  Hence the uncancelled factor in (3.6) is at most

\[
                         {g-y\choose x}\le2^{g-y}\le8.          \tag{3.7}
\]

Thus every added target multiplies `R` by at most eight, proving (3.2).
`square`

## 4. Factorial majorization of the gaps

Because a first target has complementary boundary distances at most
`r+2`, every elementary gap satisfies

\[
                              1\le g_i\le r+2.                  \tag{4.1}
\]

Factorials are log-convex: if `u>=v>=2` and `u<r+2`, moving one unit from
`v` to `u` does not decrease `u!v!`.  Since
`2r+1<2(r+2)`, repeated transfers give

\[
 G(T)\le
 \begin{cases}
 (r+2)!(r-q+1)!,&2\le q\le r,\\
 (2r-q+2)!,&r+1\le q\le2r+1.
 \end{cases}                                             \tag{4.2}
\]

For `(n)_m=n!/(n-m)!` and `1<=m<=n`, the elementary inequality

\[
                         (n)_m\ge(n/e)^m                         \tag{4.3}
\]

follows from
`(n choose m)>=(n/m)^m` and `m!>=(m/e)^m`; the case `m=0` is trivial.

If `q<=r`, (4.2)--(4.3) give

\[
 {G(T)\over r!(r+1)!}
 \le {r+2\over(r)_{q-1}}
 \le3e^{q-1}r^{2-q}.                                   \tag{4.4}
\]

If `q>=r+1`, put `m=q-r-1`.  Then

\[
 {r!(r+1)!\over(2r-q+2)!}
       =r!(r+1)_m
       \ge(r/e)^{q-1},                                  \tag{4.5}
\]

and therefore

\[
 {G(T)\over r!(r+1)!}
       \le e^{q-1}r^{1-q}
       \le e^q r^{2-q}.                                \tag{4.6}
\]

Combining the two ranges, it is harmless to record

\[
 {G(T)\over r!(r+1)!}
       \le(3e)^q r^{2-q}.                              \tag{4.7}
\]

## 5. Completion

Equations (2.4), (2.5), (3.2), and (4.7), together with
`D_M=(b-1)r!(r+1)!`, imply

\[
 {\deg(T)\over D_M}
 \le4^{t-1}8^{t-1}(3e)^q r^{2-q}.                     \tag{5.1}
\]

Every target contributes two boundary endpoints, so `q<=2t`.  Thus

\[
 {\deg(T)\over D_M}
 \le \bigl(32(3e)^2\bigr)^t r^{2-q},                  \tag{5.2}
\]

which proves Theorem 1.1. `square`

## 6. Computational regression evidence

The independent all-subset census

`scratch/research_punctured_boundary_codegree_gate_20260821.cpp`

enumerates every directed word, performs the exact superset zeta
transform, and tests `r^(q-2) deg(T)/D_M` for every target subfamily at
`r<=5`.  It is not used in the proof.  At `r=5`, the largest required
per-target constant was below `2.16`, far below the deliberately coarse
constant in (5.2).
