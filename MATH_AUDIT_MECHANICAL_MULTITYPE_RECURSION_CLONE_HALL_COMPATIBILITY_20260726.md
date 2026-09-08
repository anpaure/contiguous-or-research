# Mechanical multitype promotion recursion: parent-child compatibility and the clone-Hall cut

**Dated audit: 2026-07-26. Constant-one lane only.**

## 0. Verdict

The exact cyclic mechanical atlas does not support the proposed parent-to-child common-order recursion, even if its states are duplicated into an \(\exp(\Theta(H))\)-sized alphabet and arbitrary label permutations are allowed inside the two balanced halves.

The obstruction occurs before weighted Hall.

Fix a balanced half \(P\), and let

\[
 \mathfrak m_{L,t}
\tag{0.1}
\]

denote the cyclic mechanical binary necklace of length \(L\) and weight \(t\). A one-label recursive extension of a common cyclic order has only two possible binary shadows:

\[
 \mathfrak m_{L+1,t}\longrightarrow\mathfrak m_{L,t}
 \quad\text{by deleting a \(0\),}
\tag{0.2}
\]

or

\[
 \mathfrak m_{L+1,t+1}\longrightarrow\mathfrak m_{L,t}
 \quad\text{by deleting a \(1\).}
\tag{0.3}
\]

For every sufficiently large \(L\), if

\[
 3\le |L-2t|\le L^{2/3},
\tag{0.4}
\]

neither arrow exists, even up to cyclic rotation or reversal.

For a uniformly distributed critical top, \(T=|U\cap P|\) is hypergeometric with mean \(M/2\), variance \(\Theta(m)\), and maximum point mass \(O(m^{-1/2})\). Consequently

\[
 \Pr\!\left(3\le|M-2T|\le M^{2/3}\right)=1-o(1).
\tag{0.5}
\]

Thus almost every critical root type has **zero** mechanical parent-child transition degree.

At a height-stable two-coordinate suspension, \(1/2+o(1)\) of the child critical tops contain exactly one new coordinate and project to a parent critical top. Among that entire class, only an \(o(1)\) fraction admit a mechanical common-order extension. Hence the parent-compatible configuration graph has an explicit empty-neighborhood cut on

\[
 \left({1\over2}-o(1)\right)N_H
\tag{0.6}
\]

child roots.

This is not repaired by the clone Hall theorem. Clone Hall assigns each phase independently using only its \(P/P^c\) count. A common-order recursive lift must also satisfy the lag-\(H\) label identities and, in particular, must have a compatible binary deletion shadow. The cut (0.6) says that no label permutation exists on the affected roots, regardless of the phasewise Hall assignment.

The exact mechanical multitype design is therefore refuted as an inheritance recursion. A surviving recursion must introduce nonmechanical reset states—already at a positive density of critical roots—or allow parent-to-child operations which reorder the old cyclic frame instead of extending it. Either escape leaves the mechanical atlas theorem: its exact profile biregularity and clone Hall proof must then be re-established for the enlarged, globally coupled state space.

## 1. The proposed mechanical recursion

Let

\[
 P\in\binom{[2m]}m
\tag{1.1}
\]

be the balanced half used in the mechanical atlas. For a top \(U\) of size \(L\), put

\[
 t=|U\cap P|.
\tag{1.2}
\]

The mechanical word is

\[
 b_i^{L,t}
 =
 \left\lfloor{(i+1)t\over L}\right\rfloor
 -
 \left\lfloor{it\over L}\right\rfloor,
\qquad i\in\mathbb Z_L.
\tag{1.3}
\]

It has \(t\) one-positions and \(L-t\) zero-positions. A mechanical label state consists of

1. this cyclic binary pattern, up to a distinguished phase;
2. a bijection from \(U\cap P\) to the one-positions; and
3. a bijection from \(U\setminus P\) to the zero-positions.

The last two bijections are the common permutation whose interval windows must realize all grouped clone assignments.

Use nested balanced halves under a two-coordinate suspension:

\[
 P'=P\sqcup\{a\},
\qquad
 (P')^c=P^c\sqcup\{b\}.
\tag{1.4}
\]

Suppose a child top contains exactly one new coordinate and its old-coordinate projection is the parent top \(U\).

- If the new coordinate is \(b\), the child binary word has length \(L+1\) and weight \(t\); deleting \(b\) must give the parent word.
- If the new coordinate is \(a\), it has length \(L+1\) and weight \(t+1\); deleting \(a\) must give the parent word.

This gives exactly (0.2)--(0.3).

### Proposition 1.1 (binary compatibility is necessary)

Assume the child common cyclic order is obtained from the parent common cyclic order by a parent-to-child label permutation preserving \(P/P^c\), followed by insertion of the new label. Then its binary patterns satisfy (0.2) or (0.3), up to cyclic rotation. Allowing reversal adds only reversal of both necklaces.

#### Proof

A \(P/P^c\)-preserving permutation changes the labels occupying the one- and zero-positions but not the cyclic binary word. Deleting the inserted child label from the child cyclic order leaves the permuted parent cyclic order. Taking \(P/P^c\)-indicators gives (0.2) or (0.3). \(\square\)

Thus failure at the binary necklace level cannot be repaired by any choice of actual labels.

## 2. Euclidean gap form of a central mechanical necklace

We need one elementary structural fact.

### Lemma 2.1 (mechanical gap reduction)

Let

\[
 {L\over3}<t<{L\over2},
\qquad
 r=L-2t.
\tag{2.1}
\]

In \(\mathfrak m_{L,t}\):

1. every \(1\) is isolated;
2. the zero-gap between successive ones has length \(1\) or \(2\);
3. exactly \(r\) of the \(t\) zero-gaps have length \(2\); and
4. around the cycle, the indicator of those length-\(2\) gaps is the mechanical necklace

\[
 \mathfrak m_{t,r},
\tag{2.2}
\]

up to rotation.

The complementary statement holds for \(L/2<t<2L/3\), with zeros and ones interchanged.

#### Proof

Successive one-positions of \(\mathfrak m_{L,t}\) have cyclic spacings

\[
 \left\lfloor{L\over t}\right\rfloor
 \quad\text{or}\quad
 \left\lceil{L\over t}\right\rceil.
\tag{2.3}
\]

Under (2.1), these values are \(2\) and \(3\), so the intervening zero-gaps have lengths \(1\) and \(2\). There are \(L-t=t+r\) zeros; giving one zero to every one-gap leaves exactly \(r\) extra zeros, proving item 3.

Write \(L=2t+r\). The \(j\)-th cyclic one-spacing is

\[
 2+
 \left(
 \left\lfloor{(j+1)r\over t}\right\rfloor
 -
 \left\lfloor{jr\over t}\right\rfloor
 \right),
\tag{2.4}
\]

after a cyclic choice of origin. The parenthesized increments are exactly \(\mathfrak m_{t,r}\), proving item 4. Complementation proves the last assertion. \(\square\)

We also use the immediate spacing consequence:

### Lemma 2.2 (balanced marker spacings)

If \(s\) marked positions form \(\mathfrak m_{k,s}\) on a cyclic set of \(k\) positions, the cyclic distance between consecutive marks is

\[
 \left\lfloor{k\over s}\right\rfloor
 \quad\text{or}\quad
 \left\lceil{k\over s}\right\rceil.
\tag{2.5}
\]

This is (2.3) applied at the reduced scale.

## 3. The central deletion obstruction

### Theorem 3.1 (no mechanical one-symbol parent)

For all sufficiently large \(L\), let \(t\) satisfy

\[
 3\le |L-2t|\le L^{2/3}.
\tag{3.1}
\]

Then neither of the following is possible, even after cyclic rotation or reversal:

1. deleting a zero from \(\mathfrak m_{L+1,t}\) to obtain \(\mathfrak m_{L,t}\);
2. deleting a one from \(\mathfrak m_{L+1,t+1}\) to obtain \(\mathfrak m_{L,t}\).

#### Proof

By complementation it suffices to treat \(t<L/2\). Put

\[
 r=L-2t.
\tag{3.2}
\]

The hypothesis gives \(3\le r\le L^{2/3}\), and hence \(r=o(t)\). For large \(L\), all three words below lie in the central range of Lemma 2.1.

**Deleting a zero.** The child \(\mathfrak m_{L+1,t}\) has imbalance \(r+1\). Its \(t\) zero-gaps have lengths \(1\) or \(2\), and their long-gap markers form \(\mathfrak m_{t,r+1}\). To obtain the parent, deletion must shorten one long zero-gap from length \(2\) to length \(1\). Thus the parent marker set \(\mathfrak m_{t,r}\) would be obtained by removing one marker from \(\mathfrak m_{t,r+1}\).

Removing one marker merges its two adjacent marker spacings. By Lemma 2.2 the merged spacing is at least

\[
 2\left\lfloor{t\over r+1}\right\rfloor.
\tag{3.3}
\]

But every spacing in \(\mathfrak m_{t,r}\) is at most

\[
 \left\lceil{t\over r}\right\rceil.
\tag{3.4}
\]

The estimates

\[
 2\left\lfloor{t\over r+1}\right\rfloor
 -
 \left\lceil{t\over r}\right\rceil
 \ge
 {t(r-1)\over r(r+1)}-3
 >0
\tag{3.5}
\]

hold for \(3\le r\le L^{2/3}\) and large \(L\). This contradiction proves item 1.

**Deleting a one.** The child \(\mathfrak m_{L+1,t+1}\) has \(t+1\) isolated ones and imbalance \(r-1\). Deleting one of its ones merges the two adjacent zero-gaps. In order that every parent zero-gap still have length at most \(2\), both child gaps must have length \(1\); their merger creates one new long parent gap.

At the long-gap-marker level, remove that new marker from the parent \(\mathfrak m_{t,r}\) and replace its one gap-position by the two unmarked child positions. The two marker spacings adjacent to the removed parent marker therefore merge into a child spacing of at least

\[
 2\left\lfloor{t\over r}\right\rfloor+1.
\tag{3.6}
\]

Every spacing of the child marker necklace \(\mathfrak m_{t+1,r-1}\) is at most

\[
 \left\lceil{t+1\over r-1}\right\rceil.
\tag{3.7}
\]

Now

\[
 2\left\lfloor{t\over r}\right\rfloor+1
 -
 \left\lceil{t+1\over r-1}\right\rceil
 \ge
 {t(r-2)\over r(r-1)}-3
 >0
\tag{3.8}
\]

for \(3\le r\le L^{2/3}\) and large \(L\). This is the second contradiction.

Rotation and reversal preserve all cyclic gap spacings, so they do not affect either argument. Complementation handles \(t>L/2\). \(\square\)

### Remark 3.2

The exceptional perfectly or nearly balanced types

\[
 |L-2t|\le2
\tag{3.9}
\]

may possess deletion edges. The theorem says that these exceptional types carry asymptotically negligible root mass.

## 4. Almost every critical root type is incompatible

Fix \(P\in\binom{[2m]}m\), and choose a uniformly random critical top

\[
 U\in\binom{[2m]}M.
\]

Put

\[
 T=|U\cap P|.
\tag{4.1}
\]

The mechanical-atlas census gives

\[
 \Pr(T=t)
 ={ \binom mt\binom m{M-t}\over\binom{2m}M}
 ={ \binom mt\binom m{t-H}\over N_H}.
\tag{4.2}
\]

Also

\[
 \mathbb ET={M\over2},
\qquad
 \operatorname{Var}T
 ={M(m-H)\over4(2m-1)}
 =\Theta(m).
\tag{4.3}
\]

### Proposition 4.1 (incompatible types have mass \(1-o(1)\))

\[
 \Pr\!\left(
 3\le|M-2T|\le M^{2/3}
 \right)=1-o(1).
\tag{4.4}
\]

#### Proof

The hypergeometric mass function in (4.2) is log-concave and its central value is \(O(m^{-1/2})\), by the elementary central-binomial estimate. Therefore

\[
 \Pr(|M-2T|\le2)=O(m^{-1/2}).
\tag{4.5}
\]

Chebyshev's inequality and (4.3) give

\[
 \Pr(|M-2T|>M^{2/3})
 \le {4\operatorname{Var}T\over M^{4/3}}
 =O(m^{-1/3}).
\tag{4.6}
\]

Subtracting (4.5)--(4.6) from one proves (4.4). \(\square\)

Combining Proposition 4.1 with Theorem 3.1 shows that an \(o(1)\) fraction of critical tops have any one-symbol mechanical parent.

## 5. The explicit parent-compatible Hall cut

Consider a height-stable suspension from \(B_{2m}\) to \(B_{2m+2}\), so the critical top size rises from \(M\) to \(M+1\). Exactly one of the two new coordinates lies in the enlarged balanced half \(P'\).

Let \(\mathcal B\) be the child critical tops containing exactly one new coordinate and whose projected parent type satisfies (4.4).

### Proposition 5.1 (size of the bad child shore)

\[
 |\mathcal B|
 =\left({1\over2}-o(1)\right)
   \binom{2m+2}{M+1}.
\tag{5.1}
\]

#### Proof

The proportion of child tops containing exactly one new coordinate is

\[
 {2\binom{2m}M\over\binom{2m+2}{M+1}}
 ={1\over2}+o(1).
\tag{5.2}
\]

Conditional on the old-coordinate projection, that projection is uniform on \(\binom{[2m]}M\). Proposition 4.1 removes only an \(o(1)\) fraction. \(\square\)

For \(H_m=\lfloor\sqrt{m\log m}\rfloor\), height increments occur only \(H_m=o(m)\) times up to level \(m\). Thus height-stable suspensions have density one; they cannot be bypassed as a sparse exceptional set in an induction.

Form the parent-compatible configuration graph as follows.

- Its left vertices are child root selectors together with their mechanical phase clones.
- A right configuration consists of a parent mechanical common order, a \(P/P^c\)-preserving parent-to-child label permutation, and insertion of the unique new label.
- Incidence means that deleting the new label from the child common order gives the permuted parent common order and that all assigned phase targets are the corresponding cyclic intervals.

### Theorem 5.2 (empty-neighborhood clone-Hall cut)

Every root in \(\mathcal B\) has degree zero in the parent-compatible configuration graph. Consequently

\[
 N(\mathcal B)=\varnothing,
\qquad
 |\mathcal B|=\left({1\over2}-o(1)\right)N_H^{\rm child}.
\tag{5.3}
\]

#### Proof

For a child containing the new \(P^c\)-coordinate, the binary shadow of a parent-compatible order would give the deletion in item 1 of Theorem 3.1. For a child containing the new \(P\)-coordinate, it would give item 2. Its projected type satisfies (4.4), so both are impossible. Proposition 1.1 says that no label permutation can repair this binary failure. Therefore there is no incident right configuration. \(\square\)

This is a literal violated Hall cut, not a first-moment deficit.

## 6. Why the \(\exp(\Theta(H))\) alphabet does not help

The state alphabet proposed in the question may contain cyclic shifts, reversals, distinguished phases, and many actual label permutations of the mechanical patterns. None changes the preceding cut.

1. Cyclic shifts and reversals preserve the gap-spacing invariants in Theorem 3.1.
2. A permutation inside \(P\) and inside \(P^c\) changes actual labels but leaves the binary necklace unchanged.
3. Parallel copies of one binary state duplicate vertices of degree zero; they do not create a transition edge.
4. The clone Hall theorem allows every phase clone to choose any target of the correct profile, but a grouped common order must satisfy the lag-\(H\) equalities

   \[
   J_{i+1}\setminus J_i
   =J_{i+H}\setminus J_{i+H+1}.
   \tag{6.1}
   \]

   A parent-compatible grouped order first has to pass the binary deletion test. The roots in \(\mathcal B\) fail before (6.1) is even evaluated on actual labels.

Therefore the exact mechanical alphabet has insufficient **transition support**, not insufficient cardinality. Enlarging it by \(\exp(\Theta(H))\) copies of the same mechanical necklaces cannot satisfy the common-order clone coupling.

## 7. Scope and possible escape

The theorem rules out the exact multitype design in which

1. the fixed balanced half \(P\) is inherited;
2. every recursive state uses the exact all-length mechanical word (1.3);
3. child common orders extend parent common orders by label permutations and insertion/deletion of the new coordinates; and
4. clone assignments are required to remain the interval rows of those inherited orders.

It does not rule out either of the following changes.

### 7.1 Nonmechanical reset states

Insert the new binary symbol into the parent word and retain the resulting child word even when it is not the canonical mechanical word. Such a word has interval discrepancy at most two rather than one. A successful proof would need a new profile census and a new clone Hall theorem for this enlarged state family. Since a positive proportion of roots need these states at every height-stable step, they are not an \(o(W)\)-sized absorber.

### 7.2 Full old-label reorderings

Permit a child transition to reorder the old cyclic frame rather than restrict to it. This can restore the mechanical child word, but one-hole reconstruction says that a repaired middle deck fixes the old order up to reversal. The move therefore discards the inherited grouped clone assignment and must solve a new global permutation coupling on that root. Calling the move recursive provides no reduction of the original gate.

Changing the balanced half between parent and child is a third formal escape, but it abandons the fixed-\(P\) profile cells whose biregularity proves the mechanical clone Hall theorem. That Hall theorem would again have to be rebuilt.

## 8. Final theorem-grade decision

### Theorem 8.1 (mechanical recursive coupling no-go)

At every height-stable critical suspension, the exact mechanical-pattern parent-to-child configuration graph has an empty-neighborhood shore containing

\[
 \left({1\over2}-o(1)\right)
\]

of all child critical roots. This remains true after arbitrary cyclic shifts, reversal, distinguished-phase choices, and \(P/P^c\)-preserving label permutations.

Hence the \(\exp(\Theta(H))\)-state mechanical alphabet from the global atlas cannot satisfy the clone Hall common-order coupling by recursive label insertion. The obstruction is a zero transition degree for almost every central root type, not a lack of phasewise Hall capacity.

Any viable nonconfluent multitype recursion must enlarge the binary state space beyond exact mechanical words or perform positive-density full frame resets. Either change leaves the proved mechanical-atlas clone Hall theorem and reopens its profile and grouping gates.

## 9. Dependency ledger

This audit uses:

- MATH_THEOREM_GLOBAL_PROMOTION_MECHANICAL_ATLAS_AND_CLONE_HALL_20260726.md for the exact mechanical pattern, profile cells, clone Hall theorem, and lag-\(H\) common-order criterion;
- MATH_AUDIT_GLOBAL_RECURSIVE_SCD_TO_PROMOTION_RING_FACTORIZATION_20260726.md for the nonconfluent multitype recursion target;
- MATH_AUDIT_CALIBRATED_FULL_TOP_PROMOTION_RING_SWITCHES_TAIL_AND_LOCALITY_20260726.md for one-hole order reconstruction.

No generic matching theorem is invoked. The obstruction is proved by the exact cyclic gap structure of the mechanical words.
