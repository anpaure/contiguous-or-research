# Audit of selective component switching and the near-trade relaxation

Date: 2026-07-25

Method: pure mathematics only.

## 0. Verdict

The proposed pivot from fair component coins to selective switching contains
one useful correction and two overstatements.

* For one exact ownership component, duplicate splitting and fair-cube
  leakage are indeed irrelevant: the exact criterion is simply that the
  component repairs more old holes than it opens.
* The scalar quantity \(\sum_K|f_K-n_K|\) does **not** by itself force an
  improving component.  One also needs positive signed mass.
* Pairwise sparsification can batch already-positive components, but it
  cannot create a positive component when every one-component drift is
  nonpositive.  Its crude pair-risk bound is \(O(m^2W)\), not
  \(O(m^2h)\), without an additional support restriction.

The relaxation from exact component trades to one partial relabeling
near-trade is valid and genuinely enlarges the search space.  Its exact
middle cost is an owner-overlay diagonal cut.  However, vanishing
conductance solves only the middle-layer bill; it does not imply shallow
shadow improvement, and growingly many near-trade rounds cannot be composed
without a summable-boundary or cancellation theorem.

Thus the remaining gate is best described as **productive
fragmentation**, not fragmentation alone.

## 1. Exact components and connected overlays

Let \(F,G\) be exact wreath factors and let \(K\) range over the connected
components of their middle-owner overlay.  The two shores of \(K\) are the
minimal nonempty subfamilies drawn from \(F,G\) which partition the same
middle-owner block.  Choosing either shore in every component gives an
exact factor.

If the overlay is connected, its component cube has only the two vertices
\(F,G\).  In particular, if \(G=\sigma F\), then
\[
 H_q(G)=H_q(F)
\]
for every \(q\), so that fixed coupling has no improving component
selection.  This proves that fragmentation is necessary for an exact
two-factor component-switch argument.

It does not prove that a generic overlay is connected; that remains a
prediction unless a connectivity or spectral-gap theorem is supplied.

## 2. What selective switching actually removes

For one component \(K\), let
\[
 f_K=\#\{\text{old holes repaired by switching }K\},
\qquad
 n_K=\#\{\text{old covered targets opened by switching }K\}.
\]
The exact drift is
\[
 \boxed{H_1(F_K)-H_1(F)=n_K-f_K.}
\tag{2.1}
\]
Thus a legal improving component exists exactly when
\[
 g_K:=f_K-n_K>0
\tag{2.2}
\]
for some \(K\).

For this one-component test, it is true that a single new occurrence fills
an old hole; the fair-coin duplicate-splitting term \(\Xi\) is unnecessary.
The price is that the complete damage count \(n_K\) must be controlled.

Put
\[
 G_+=\sum_{K:g_K>0}g_K.
\]
The proposed \(L^1\) anticoncentration
\[
 \sum_K|g_K|\ge cW/m
\tag{2.3}
\]
does not imply \(G_+>0\): all \(g_K\) may be negative.  Indeed
\[
 G_+={1\over2}\left(\sum_K|g_K|+\sum_Kg_K\right),
\tag{2.4}
\]
and relabeling invariance of the two opposite cube vertices does not force
\(\sum_Kg_K=0\).  Hole count is nonlinear under simultaneous component
switches.  The exact aggregate identity for an involutive bridge is
\[
 \sum_Kg_K
 =\sum_{\substack{\text{exclusive pairs }P\\s_P\ge2}}s_P-D_{\rm common},
\tag{2.5}
\]
which can have either sign.

Therefore the valid selective target is \(G_+>0\), or a quantitative lower
bound on the right side of (2.4), not (2.3) alone.

## 3. Pairwise sparsification

Suppose \({\cal G}=\{K:g_K>0\}\) is nonempty.  For
\({\cal S}\subseteq{\cal G}\), Bonferroni gives
\[
 H_1(F)-H_1(F_{\cal S})
 \ge\sum_{K\in{\cal S}}g_K
   -\sum_{\{K,L\}\subseteq{\cal S}}(c_{KL}+\ell_{KL}),
\tag{3.1}
\]
provided

* \(c_{KL}\) counts old holes fillable by both \(K,L\); and
* \(\ell_{KL}\) is chosen so every target which can first become a hole
  only after at least two switches is charged to at least one selected
  pair.

Selecting every \(K\in{\cal G}\) independently with probability \(p\)
therefore gives
\[
 \mathbb E[H_1(F)-H_1(F_{\cal S})]
 \ge pG_+-p^2\Lambda,
\qquad
\Lambda=\sum_{K<L}(c_{KL}+\ell_{KL}).
\tag{3.2}
\]
Optimizing \(p\) yields
\[
 \boxed{
 \mathbb E[H_1(F)-H_1(F_{\cal S})]
 \ge\min\left({G_+\over2},{G_+^2\over4\Lambda}\right).}
\tag{3.3}
\]

This is a valid batching lemma.  It does not establish \(G_+>0\); if
\(G_+>0\), (2.1) already gives a strict one-component descent.

At depth one every target has load at most
\[
 M_m=\left\lfloor{m+2\over2}\right\rfloor.
\]
Consequently
\[
 \sum_{K<L}c_{KL}\le h\binom{M_m}{2}.
\tag{3.4}
\]
For pair-created holes among all previously covered targets, however, the
same argument gives only
\[
 \sum_{K<L}\ell_{KL}\le (N_1-h)\binom{M_m}{2}
 =O(m^2W),
\tag{3.5}
\]
not \(O(m^2h)\).  An \(O(m^2h)\) estimate requires an additional theorem
restricting which covered targets meet the selected positive components.

Even the corrected finite bound (3.5) means leakage affects the rate rather
than logical feasibility once \(G_+>0\).  It does not remove the sign and
renewal problems.

## 4. One-shot near-trades are valid

Let \(F\) be exact, \(\sigma\in S_n\), and \(A\subseteq F\).  Put
\[
 {\cal P}=(F\setminus A)\sqcup\sigma A,
\qquad
 U(A)=\bigsqcup_{C\in A}{\cal W}_m(C).
\]
Then
\[
 \boxed{
 M_0({\cal P})
 =\text{middle duplicate excess}
 ={1\over2}|U(A)\triangle\sigma U(A)|
 ={1\over2}\partial_\sigma(A).}
\tag{4.1}
\]
At depth one,
\[
 \boxed{
 H_1({\cal P})-H_1(F)=D_1-R_1.}
\tag{4.2}
\]
The exact designated first-band OR cost changes by
\[
 \boxed{
 \Delta L_1=\partial_\sigma(A)+2(D_1-R_1).}
\tag{4.3}
\]
Thus a one-shot near-trade is profitable precisely when
\[
 \boxed{R_1-D_1>{1\over2}\partial_\sigma(A).}
\tag{4.4}
\]

For a balanced positive-density cut, the middle bill is \(o(W)\) exactly
when
\[
 {\partial_\sigma(A)\over
 n\min(|A|,|F\setminus A|)}=o(1).
\tag{4.5}
\]
This proves the useful part of the proposed conductance reformulation.

But conductance alone is not sufficient.  The exact fixed-band condition is
\[
 \boxed{
 \partial_\sigma(A)+2\sum_{q\le H}M_q({\cal P})=o(W),}
\tag{4.6}
\]
together with the established seam and tail estimates.  A zero-boundary
component union may retain a linear frozen shadow defect.

## 5. Why near-trade rounds do not compose for free

After one nonexact near-trade, middle sets have holes and duplicate owners,
so the regular exact-owner overlay needed for the next round no longer
exists.

For pairwise disjoint replacements from one common exact baseline, if
\(d_t\) is the signed middle-incidence update of round \(t\), then
\[
 \boxed{
 M_0^{\rm final}
 ={1\over2}\left\|\sum_td_t\right\|_1
 \le {1\over2}\sum_t\partial_t.}
\tag{5.1}
\]
Thus \(o(1)\) conductance per round is not enough for a growing number of
rounds.  One needs either
\[
 \sum_t\partial_t=o(W)
\tag{5.2}
\]
or a direct cancellation theorem for the final signed update.  Shallow
holes likewise can be repaired and later reopened, so only the final common
histograms establish coefficient one.

## 6. Correct surviving gate

The selective exact-factor route needs a bridge with **productive
fragmentation**:
\[
 \exists K:\quad f_K>n_K,
\tag{6.1}
\]
renewable until the desired multidepth objective is small.

The one-shot near-factor route needs a cut satisfying simultaneously
\[
 \partial_\sigma(A)=o(W),
\qquad
\sum_{q\le H}M_q((F\setminus A)\sqcup\sigma A)=o(W).
\tag{6.2}
\]

These are narrower and more accurate than “fragmentation alone.”  Spectral
nonexpansion supplies the first condition in (6.2), not the second.
