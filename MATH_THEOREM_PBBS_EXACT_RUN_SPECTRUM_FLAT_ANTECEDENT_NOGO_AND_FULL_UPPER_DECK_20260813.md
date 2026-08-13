# PBBS has a complete upper deck but no growing-depth flat antecedent: the exact run--return spectrum

**Date:** 2026-08-13  
**Status:** unconditional reduction from the audited PBBS return and flag
theorems.  The canonical PBBS owner factor covers every upper width, but its
minimum positive coordinate residence is exactly `3`.  Thus it cannot be
used unchanged as the depth-`d` full-aperture carrier when
`q=d+1>=4`.  The exact missing modification is a short-return-free,
flag-preserving rethreading, not an additional upper-shadow theorem.

## 0. Verdict

Put

\[
 n=2m+1,
 \qquad
 f:{[n]\choose m}\longrightarrow {[n]\choose m}
\]

for the canonical cyclic-parenthesis/PBBS permutation.  On an `f`-orbit
write

\[
 A_t=f^t(A_0),
 \qquad
 \lambda_t=[n]\setminus(A_t\cup A_{t+1}).          \tag{0.1}
\]

The complement-centered owner factor consists of the rank-`m+1` states

\[
 X_t=A_t^c
\]

with directed successor `t -> t+2`.  If an `f`-orbit is even this gives
two cycles; if it is odd it gives one.

The exact conclusions are:

1. If two consecutive occurrences of one omitted label have cyclic
   `f`-gap `g=2s+1`, they create exactly one positive coordinate run of
   length

   \[
   s+1={g+1\over2}                                  \tag{0.2}
   \]

   and exactly one zero run of length

   \[
   s={g-1\over2}                                    \tag{0.3}
   \]

   in the complete step-two owner factor.  Every nonconstant coordinate
   run arises uniquely this way.

2. PBBS has exactly

   \[
   n(m-1)                                           \tag{0.4}
   \]

   consecutive gap-five starts and exactly

   \[
   n(2^{m-1}-m)                                     \tag{0.5}
   \]

   consecutive gap-seven starts.  Hence the owner factor has exactly the
   same respective numbers of positive runs of lengths `3` and `4`.
   In particular its minimum positive run is exactly `3`; its minimum
   zero run is exactly `2`.

3. A cyclic set trace has a flat `q`-antecedent if and only if every
   proper positive coordinate run has length at least `q`.  Therefore the
   canonical PBBS owner chronology has no flat `q`-antecedent for any

   \[
   q\ge4.                                           \tag{0.6}
   \]

   This includes the target regime `q=d+1 asymp sqrt(m)`.

4. Nevertheless PBBS already covers the complete upper deck.  For every
   width `1<=w<=m+1`, every rank-`m+w` target occurs as the union of `w`
   consecutive complement-centered owners.  For `w>=2`, its number of
   correct-rank designated occurrences lies between

   \[
   1
   \quad\hbox{and}\quad
   {2w-1\choose w-1}.                              \tag{0.7}
   \]

Thus PBBS and the long-aperture MSW construction have complementary
strengths: PBBS has the complete all-width deck but fails growing
residence, while the MSW wreath chronology has flat growing residence but
does not automatically cover its second shadow.

## 1. Centered recurrence

Adjacent PBBS states are disjoint and omit one coordinate.  The standard
recurrence is

\[
 A_{t+2}
 =A_t\setminus\{\lambda_{t+1}\}\cup\{\lambda_t\}. \tag{1.1}
\]

After complementation,

\[
 \boxed{
 X_{t+2}
 =X_t\setminus\{\lambda_t\}\cup\{\lambda_{t+1}\}.}
                                                               \tag{1.2}
\]

Thus, on the step-two owner graph, `lambda_t` is deleted on the edge
starting at `X_t`, and it is inserted on the edge starting at `X_(t-1)`.

Fix a coordinate `x`.  Consecutive occurrences of `x` in the cyclic
omitted-label word have odd separation.  Indeed, `x` is absent at both
ends of an edge labelled `x`; at every intervening edge not labelled `x`,
its membership in the odd-graph state is complemented.  Returning to an
absent endpoint therefore requires an even number of ordinary flips, so
the edge-index gap is odd.  The audited PBBS no-gap-one/no-gap-three
theorems strengthen this to

\[
                         g\ge5.                    \tag{1.3}
\]

## 2. Exact run--return dictionary

### Theorem 2.1 (positive and zero spectra)

Let `lambda_t=lambda_(t+g)=x` be consecutive occurrences on a lifted
`f`-orbit, where `g=2s+1`.  Then:

* `x` is present on the step-two owner vertices

  \[
  X_{t+1},X_{t+3},\ldots,X_{t+g},                  \tag{2.1}
  \]

  a maximal positive run of `s+1=(g+1)/2` states;
* on the other step-two arc, `x` is absent on

  \[
  X_{t+2},X_{t+4},\ldots,X_{t+g-1},                \tag{2.2}
  \]

  a maximal zero run of `s=(g-1)/2` states.

As the coordinate, orbit, and consecutive return vary, (2.1) gives every
nonconstant positive run exactly once and (2.2) gives every nonconstant
zero run exactly once.

#### Proof

By (1.2), the occurrence at `t` inserts `x` on the edge

\[
 X_{t-1}\longrightarrow X_{t+1},                  \tag{2.3}
\]

whereas the next occurrence deletes it on

\[
 X_{t+g}\longrightarrow X_{t+g+2}.                \tag{2.4}
\]

There is no intervening occurrence of `x`, so no intervening transition
can toggle it.  This gives (2.1), whose number of terms is

\[
 {t+g-(t+1)\over2}+1={g+1\over2}.                 \tag{2.5}
\]

Starting instead immediately after the deletion at `t`, the coordinate
is absent until its insertion at `t+g`; the intervening vertices are
exactly (2.2), whose number is `(g-1)/2`.

Conversely, the left and right boundary transitions of any maximal
positive run are respectively an insertion and a deletion of its
coordinate.  Formula (1.2) labels both by consecutive occurrences of that
coordinate in the omitted-label word.  The same argument applies to a
zero run.  This proves both bijections. `square`

### Census check from componentwise homomesy

If the underlying `f`-orbit has length `L=ell*n`, componentwise PBBS
homomesy says that each coordinate occurs exactly `ell` times in its
omitted-label word.  If its consecutive gaps are `g_1,...,g_ell`, then

\[
 \sum_i g_i=L.                                     \tag{2.6}
\]

Theorem 2.1 gives total positive and zero occupation

\[
 \sum_i{g_i+1\over2}=\ell(m+1),
 \qquad
 \sum_i{g_i-1\over2}=\ell m,                       \tag{2.7}
\]

exactly the required site-homomesy counts for the rank-`m+1`
complemented owner trace.  This independently checks both off-by-one
terms in (0.2)--(0.3).

## 3. The first two exact spectral atoms

The audited PBBS return classification gives:

\[
 M_5=n(m-1),                                       \tag{3.1}
\]

because the normalized gap-five roots are exactly

\[
 D=(10)^a1(10)^b0,
 \qquad a\ge0, b\ge1, a+b=m-1,                  \tag{3.2}
\]

and each has `n` spatial phases.  The next exact return census is

\[
 M_7=n(2^{m-1}-m).                                 \tag{3.3}
\]

Applying Theorem 2.1 proves

\[
 \boxed{N_3^+=n(m-1),\qquad
        N_4^+=n(2^{m-1}-m).}                       \tag{3.4}
\]

Here `N_r^+` denotes the number of coordinate-labelled proper positive
runs of length `r` in the full complement-centered owner factor.  It also
gives `N_2^0=M_5`, where the superscript `0` denotes zero runs.

Equivalently, on the uncomplemented rank-`m` centered row the same
gap-five returns give exactly `n(m-1)` positive runs of length `2`.
Thus there is no ambiguity between the two possible middle-shore
conventions: the upper-middle rank-`m+1` owner trace has minimum positive
run `3`, while the lower-middle rank-`m` trace has minimum positive run
`2`.

The first equality in (3.4) proves that the minimum positive run is at
most three; (1.3) and (0.2) prove it is at least three.  The analogous
argument gives minimum zero run exactly two.

The gap-seven atom shows that the failure is not merely a fixed finite
exception.  Once `q>=5`, the canonical chronology contains at least

\[
 N_3^++N_4^+
 =n(2^{m-1}-1)                                     \tag{3.5}
\]

short positive runs.

### Corollary 3.1 (incidence distance from a flat trace)

For `q>=5`, let `Y` be any set trace on the same indexed slots which has
all proper positive coordinate runs of length at least `q`.  Then

\[
 \boxed{
 \sum_t|X_t\mathbin\triangle Y_t|
 \ge n(2^{m-1}-1).}                                \tag{3.6}
\]

#### Proof

For every positive run `R` of `X` of length three or four, adjoin the
immediately preceding and following zero states of the same coordinate.
The resulting coordinate-labelled collars are pairwise disjoint.  Indeed,
Theorem 2.1 and (1.3) say every intervening zero run has length at least
two, so the right collar point of one positive run differs from the left
collar point of the next.

If `Y` agreed with `X` throughout one such collar, `R` would remain an
isolated positive run of length less than `q` in `Y`.  Hence every collar
contains a changed incidence.  Disjointness and (3.5) prove (3.6).
`square`

This is an aligned-incidence obstruction.  A nonlocal permutation of the
owner chronology can move exponentially many incidences without changing
the owner sets, so (3.6) does not rule out rethreading.  It does rule out a
bounded local correction of the fixed PBBS chronology.

## 4. Exact flat-antecedent criterion

Let `T=(T_i)` be any cyclic set trace.  A **flat `q`-antecedent** is a
cyclic source trace `P=(P_i)` satisfying, up to a harmless index reversal,

\[
 T_i=\bigcup_{h=0}^{q-1}P_{i-h}.                   \tag{4.1}
\]

### Lemma 4.1 (binary dilation image)

A flat `q`-antecedent exists if and only if every proper nonempty positive
coordinate run of `T` has length at least `q`.

#### Proof

Work one coordinate at a time.  Every source occurrence `p_j=1` creates
`q` consecutive ones in the dilated trace (4.1).  Connected components of
a union of cyclic `q`-intervals therefore have length at least `q`, unless
they fill the whole cycle.

Conversely, define the coordinate of `P_i` to be one precisely when it is
present in all of

\[
 T_i,T_{i+1},\ldots,T_{i+q-1}.                     \tag{4.2}
\]

On a positive run of length `r>=q`, (4.2) is one on its first `r-q+1`
starts, and dilating these starts by (4.1) recovers the whole run.  It also
recovers constant-zero and constant-one traces.  Applying this independently
to every coordinate gives a set-valued antecedent. `square`

Combining Lemma 4.1 with Theorem 2.1 gives an exact PBBS criterion:

\[
 \boxed{
 \text{PBBS is flat at aperture }q
 \Longleftrightarrow
 \text{every consecutive omitted-label gap satisfies }g\ge2q-1.}
                                                               \tag{4.3}
\]

Since (3.1) supplies gap five, (4.3) fails for every `q>=4`.  Rotation,
reversal, and component rephasing preserve the cyclic run spectrum, so
none repairs the failure.  If dual residence is also required, (0.3)
shows that a gap `g` requires `g>=2q+1`; gap five already defeats dual
`q`-residence for `q>=3`.

## 5. The complete upper deck survives abstractly

The residence failure must not be confused with an upper-support failure.
The audited all-depth PBBS fan theorem states that for every
`0<=r<=m` and every

\[
 S\in{[n]\choose m-r},
\]

some directed step-two fan has

\[
 \bigcap_{j=0}^{r}A_{t+2j}=S,                     \tag{5.1}
\]

and its correct-rank load lies in

\[
 1\le\mu_r^-(S)\le {2r+1\choose r}.               \tag{5.2}
\]

### Theorem 5.1 (all-width upper support)

For every `1<=w<=m+1` and every

\[
 U\in{[n]\choose m+w},
\]

there is a width-`w` interval of complement-centered owners whose union is
exactly `U`.  For `w>=2`, the correct-rank occurrence load satisfies

\[
 \boxed{
 1\le\mu_w^{\rm up}(U)
 \le {2w-1\choose w-1}.}                           \tag{5.3}
\]

At `w=1`, every owner occurs exactly once.

#### Proof

Put `r=w-1` and `S=U^c`, so `|S|=m-r`.  Choose (5.1).  Then

\[
 \bigcup_{j=0}^{w-1}X_{t+2j}
 =[n]\setminus\bigcap_{j=0}^{r}A_{t+2j}
 =S^c=U.                                           \tag{5.4}
\]

Complementation is occurrence-preserving, so (5.2) becomes (5.3).
For `w=1`, complementation of the PBBS middle layer is an exact owner
factor. `square`

The theorem counts designated correct-rank windows.  Many other PBBS
windows have a repeated toggle and the wrong union rank.  Complete support
therefore does not imply the pointwise dilation identity required by a flat
source.

## 6. The precise PBBS modification now required

Let the target aperture be `q=d+1`.  On every untouched PBBS fragment,
(4.3) says that a growing-depth construction must intercept every
consecutive omitted-label return arc

\[
                         g\le2q-3.                 \tag{6.1}
\]

Cutting such arcs is not by itself sufficient: some upper targets in
Theorem 5.1 can have only one designated occurrence, so an arbitrary cut
can destroy their last witness.

The exact positive replacement theorem to seek is therefore the following.

### PBBS `q`-safe flag-rethreading problem

Rethread the exact multiset of complement-centered owners into Johnson
cycles or paths so that:

1. every owner is still used exactly once;
2. every proper positive coordinate run has length at least `q`;
3. for every width `w` and every required upper target `U`, at least one
   designated width-`w` union interval from Theorem 5.1 is retained, or a
   replacement interval with the same union is created;
4. every new seam satisfies the same run condition, rather than merely
   cutting the old short-return arcs.

Conditions 1--4 are precisely enough for the owner/upper part of the
full-aperture compiler.  Indeed, Lemma 4.1 gives the maximal source

\[
 P_i=\bigcap_{h=0}^{q-1}T_{i+h},                  \tag{6.2}
\]

and every letter in (6.2) has the required rank `m-q+2`.  To check the
rank, inspect any block of `q-1` Johnson transitions.  If a coordinate
inserted inside the block were deleted again inside the block, its new
positive run would have fewer than `q` owner states.  Hence no inserted
coordinate is deleted, all `q-1` deletion labels are distinct coordinates
of the initial owner, and the common intersection loses exactly `q-1`
coordinates from rank `m+1`.

Finally, any retained width-`w` owner union becomes a literal interval
union of `q+w-1` consecutive source letters.  Thus all of Theorem 5.1's
upper targets survive in one flat, fixed-rank source word.

Equivalently, a cut-and-sew proof needs a transversal of the PBBS return
arcs (6.1), together with a **flag-safe sewing theorem** which creates no
new short run and does not erase the last designated occurrence of any
upper target.  This is stronger than component fusion and stronger than a
return-packing estimate alone.

## 7. Consequence for the current architecture

The canonical PBBS factor cannot replace the full-aperture MSW factor
unchanged: its growing-depth antecedent fails already at `q=4`, and for
`q>=5` it is exponentially far from a flat trace in the aligned incidence
metric.  On the other hand, PBBS completely eliminates the abstract
all-width upper-support gate.

The sharp hybrid target is therefore:

\[
 \boxed{
 \text{transport PBBS's designated all-width fan bank through a
 `q`-safe rethreading.}}
                                                               \tag{7.1}
\]

If such transport is proved, the flat source and every upper width follow
formally from Lemma 4.1 and Theorem 5.1.  Without it, PBBS supplies an
excellent occurrence atlas but not the resident chronology required for
`B(k)+O(1)`.

## 8. Dependencies and audit boundary

The recurrence (1.1), odd-gap rule, componentwise homomesy, no-gap-three
theorem, gap-five census, and gap-seven census are proved and independently
audited in:

* `MATH_AUDIT_PBBS_FIRST_SHADOW_THEOREM_20260726.md`;
* `MATH_AUDIT_O_PBBS_CENTERED_Q2_CHRONOLOGY_AND_RETURN_GATE_20260726.md`;
* `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

The all-depth fan support and load bound used in Section 5 are in:

* `MATH_THEOREM_PBBS_Q_FAN_SUPPORT_Q2_AND_GAUSSIAN_MULTIPLICITY_20260726.md`;
* `MATH_AUDIT_PBBS_ALL_DEPTH_FAN_AND_MULTIPLICITY_20260726.md`.

No claim is made here that the `q`-safe flag rethreading exists.  The note
proves the exact canonical no-go, preserves the positive all-upper theorem,
and isolates the modification which would turn the PBBS occurrence atlas
into a literal growing-depth carrier.
