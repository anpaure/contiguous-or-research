# Audit of the phase-separated forced-ring obstruction

## 1. Verdict

The main combinatorial obstruction in
`THREE_BOX_PHASE_SEPARATION_RESEARCH.md` is sound, but the manuscript is not
yet self-contained enough to certify Proposition 4 exactly as written.

The results separate as follows.

1. The endpoint normal form, the heterogeneous run-cover lemma, the exact
   avoidance ledger, and all uses of them are correct.
2. The explicit run certificate for the nested order `\mathcal O_a` is
   correct.  In fact every assigned one-sided span is at most `2a`, not merely
   `2a+1`, and the actual certificate has
   `C_\alpha\le 2a`, `C_\beta\le a`.  Thus Theorem 3 is valid and can be
   sharpened.
3. The binary run claims for even and odd side batches in Proposition 4 are
   correct for every permutation of the radii and every independent block
   reversal.
4. The sentence called a "direct scan" in lines 358--362 is a proof gap, not
   a false claim.  A nine-block-window argument supplied below proves a
   stronger span bound `5a` (hence the stated `6a`).
5. Three repairs are needed around the architectural interpretation:

   * `B` must be the number of **maximal** side-homogeneous batches (equivalently,
     adjacent batches must have different side types).  Otherwise an order
     with few actual switches can be artificially subdivided into many
     batches, and `B=\Omega(a)` does not imply linearly many switches.
   * The center `(0,0,0)`, which is not one of the `6a` side blocks, must be
     placed or handled.  For an arbitrary center position, split the affected
     batch at the center and regard the two pieces as separate local batches.
     This increases the batch count by at most one and is absorbed by the
     existing `O(aD)` term.
   * Lines 204--206 incorrectly say that choosing the **later** copy of every
     repeated corner produces the fixed half-open blocks in (3.1).  No cyclic
     half-open convention can choose the later copy at every corner.  The
     needed and valid statement is to choose the copy designated by the
     half-open partition; depending on the two incident blocks' positions,
     that copy can be earlier or later.

After those changes, Proposition 4 and its consequence `BD=\Omega(a^2)` are
proved.  The overall conclusion--boundedly many macroscopic side phases and
the perfectly nested phase order both fail at surface error--is therefore
certified under the explicitly stated factorable-band and exact-rainbow-arc
hypotheses.

## 2. Line-by-line audit map

| Source lines | Status | Audit |
|---|---|---|
| 5--11 | Correct | `|\mathcal H_a|=3a^2+3a+1`.  It is the middle rank of the translated box `[0,2a]^3`. |
| 13--39 | Correct after later proofs | Equations (1.1)--(1.3) follow from Lemma 2, Lemma 1, and the avoidance ledger.  The word "exact" in line 22 should mean an explicit inequality, not a sharp one; the same certificate gives a stronger linear coefficient. |
| 42--60 | Correct interpretation | The heterogeneous issue is real, and the two no-go conclusions do not rule out all `O(a)` arc schedules. |
| 64--85 | Correct | Distinct equal-rank targets are incomparable.  Sorting selected witness intervals by left endpoint makes both endpoint sequences strictly increasing, so the normal form (2.1)--(2.2) follows.  It would help to say explicitly that an antichain of intervals on `[N]` has size at most `N`, hence `D=N-M_a\ge0`. |
| 88--94 | Correct with a missing displayed hypothesis | An internal run must satisfy `2\le u\le v\le M_a-1`.  Coordinatewise factorability gives (2.3). |
| 99--127 | Correct | The congestion definitions match exactly the adjacent increments occurring in the two telescoping differences. |
| 129--162 | Correct, but define "one-sided span" | It should explicitly mean `v_i+1-i` when `i<u_i` and `i-(u_i-1)` when `i>v_i`.  With that definition, (2.6) follows. |
| 164--182 | Correct | Equation (2.9) and the `\Omega(a^2)` congestion consequence have the stated constants and asymptotics. |
| 186--202 | Correct | The six half-open blocks partition the radius-`s` ring into `6s` distinct vertices, and adjoining each omitted endpoint gives the six side trails. |
| 203--206 | Needs wording repair | Six side trails per radius give `6a` trail blocks and `6a` repeated-endpoint overhead.  However, "later copy" does not generally produce the particular half-open sets `B_{k,s}`; choose the designated half-open copy instead. |
| 208--230 | Correct | (3.2) is a permutation of `\mathcal H_a`; deleting radii greater than `s` gives exactly `\mathcal O_s`.  The advertised outer/inner phase separation follows. |
| 234--276 | Correct | Every cited threshold support is an internal maximal run, all assignments avoid their own index, and the run-length sum is exactly `a^3-a`.  The span bound can be sharpened from `2a+1` to `2a`. |
| 278--309 | Correct | (3.6), (1.1), (3.8), and `D\ge(1-o(1))a^{3/2}` all follow.  A stronger coefficient is available from the actual congestions. |
| 311--316 | Correct | The certificate indeed uses long positive-wall runs before the center and singleton threshold runs after it. |
| 323--327 | Definition incomplete | Specify that, after deleting the center, every `B_{k,s}` occurs exactly once, blocks are intact, and `B` is the number of maximal constant-`k` runs in the resulting block sequence. |
| 329--338 | Correct after that definition | The proof yields `BD=\Omega(a^2)` under `D=O(a)` and therefore `B=\Omega(a)`. |
| 342--356 | Correct away from the center | The threshold table gives the stated binary block words.  Even runs have at most three vertices; odd runs meet at most two blocks and have at most `2a-2` vertices. |
| 358--363 | Repairable proof gap | The deletion count is right, and the scan claim is true, but it needs the nine-block proof in Section 7 below.  An arbitrary center is handled by one additional artificial batch boundary. |
| 364--384 | Correct after the scan repair | The assigned `\lambda` budget, unassigned-index charge, congestion term, and avoidance term give (4.5), uniformly in the radius permutations and reversals. |
| 386--390 | Requires maximal batches | Only for maximal batches does `B=\Omega(a)` mean a linear number of genuine side-type switches. |
| 392--438 | Correct conditional summary | These lines accurately preserve the surviving irregular and near-rainbow possibilities once the preceding definition repairs are made. |

## 3. Endpoint and heterogeneous run-cover lemma

Let the selected witnesses be

\[
 I_i=[\ell_i,r_i],\qquad 1\le i\le M_a.
\]

If two selected intervals had the same left endpoint, the one with smaller
right endpoint would be contained in the other; equal right endpoints give
the symmetric contradiction.  More generally, after sorting by increasing
left endpoint, a weakly decreasing pair of right endpoints would give interval
containment.  Interval containment implies containment of the represented OR
targets, while distinct members of `\mathcal H_a` are incomparable.  Hence
both endpoint sequences are strictly increasing.  Every increasing
`M_a`-subset of `[N]`, where `N=M_a+D`, has its `i`th entry between `i` and
`i+D`, proving (2.1)--(2.2).

For an internal threshold run `[u,v]`, the zero witnesses `I_{u-1}` and
`I_{v+1}` forbid the relevant Boolean coordinate on all their physical
positions.  A positive witness in the run needs a pin strictly between those
two forbidden intervals.  Thus

\[
 r_{u-1}+2\le \ell_{v+1},
 \qquad
 \beta_{u-1}-\alpha_{v+1}\le v-u.
\]

This verifies (2.3) for every coordinate threshold, not just an extreme one.

For an assigned index `i<u_i`, monotonicity and the run inequality give

\[
 w_i\le \beta_{u_i-1}-\alpha_i
     \le \lambda_i+\alpha_{v_i+1}-\alpha_i.
\]

The last difference expands as

\[
 \sum_{i<t\le v_i+1}(\alpha_t-\alpha_{t-1}),
\]

so its multiplicity is exactly controlled by `C_\alpha`.  For `i>v_i`,

\[
 w_i\le \lambda_i+\beta_i-\beta_{u_i-1},
\]

and the expansion uses exactly the indices `u_i\le t\le i` appearing in
`C_\beta`.  The total variations of both monotone offset sequences are at
most `D`, and every unassigned width is at most `D`.  This proves (2.5).

If the forward span is `v_i+1-i\le h`, a fixed `\alpha` increment can be
charged by at most the preceding `h` integer indices.  If the backward span
is `i-(u_i-1)\le h`, the same statement holds for `\beta`.  Hence
`C_\alpha,C_\beta\le h`, proving (2.6).  There is no hidden homogeneity
assumption: the run and threshold may vary with `i` exactly as claimed.

## 4. Avoidance ledger and numerical constants

For completeness, the exact number `Q` of nonempty physical intervals
containing no complete selected witness is

\[
\begin{split}
 Q={}&\sum_{x=1}^{\ell_1}(r_1-x)
 +\sum_{i=2}^{M_a}
   \left(\Delta_iw_i+{\Delta_i\choose2}\right)\\
 &+{N-\ell_{M_a}+1\choose2},
 \qquad \Delta_i=\ell_i-\ell_{i-1}.
\end{split}
\]

Writing `e_i=\Delta_i-1=\alpha_i-\alpha_{i-1}`, the four excess terms over
`\sum_iw_i` are bounded, respectively, by

\[
 D(D+1),\qquad D^2,\qquad \frac{D(D+1)}2,
 \qquad \frac{D(D+1)}2.
\]

Therefore

\[
                         Q\le\sum_iw_i+3D^2+2D.
\]

The number of nonzero strictly below-middle box targets is

\[
 \frac{(2a+1)^3-(3a^2+3a+1)}2-1
 =4a^3+\frac92a^2+\frac32a-1.
\]

Every such target needs a distinct physical interval avoiding all complete
middle witnesses, so `V_a\le Q`.  This proves (2.9), and all constants used in
Theorem 3 are valid.

## 5. The explicit nested-order certificate

The sets `B_{k,s}` in (3.1) are pairwise disjoint half-open sides of the
radius-`s` hexagon.  Their total size is `6s`; summing over `s` and adjoining
the center gives

\[
 1+\sum_{s=1}^a6s=3a^2+3a+1=M_a,
\]

so (3.2) is genuinely a permutation of `\mathcal H_a`.

On its first half:

* `B_{2,s}` is exactly the maximal support run of `y\ge s`;
* `B_{4,s}` is exactly the maximal support run of `z\ge s`.

The adjacent selected vertices have the relevant coordinate at most `s-1`,
including at `s=1`, so both runs are internal.  Assigning

\[
 B_{0,s}\longrightarrow B_{2,s},\qquad
 B_{2,s}\longrightarrow B_{4,s},\qquad
 B_{4,s}\longrightarrow B_{2,s}
\]

uses runs of `s` vertices, hence `\lambda=s-1`, for each of the `3s`
assigned indices.

On the second half, the first vertices of `B_{1,s}`, `B_{3,s}`, and
`B_{5,s}` are isolated internal runs of `x\ge s`, `y\ge s`, and `z\ge s`,
respectively.  The cyclic assignment in the source therefore contributes
`\lambda=0` at all `3s` indices.  Only the center is unassigned.  Consequently

\[
 \sum_i\lambda_i=\sum_{s=1}^a3s(s-1)=a^3-a.
\]

The farthest endpoint in any one of these assignments is actually at
one-sided span `2s`, so `h=2a` is valid.  More strongly, inspecting the
charge intervals radius by radius gives

\[
                         C_\alpha\le2a,
 \qquad                    C_\beta\le a.
\]

Indeed, the two forward assignments in a three-block group can overlap an
`\alpha` increment with multiplicity at most `2s`; the single backward
assignment has `\beta` multiplicity at most `s`.  Charge intervals belonging
to different radius groups do not overlap except at a group boundary where
the next group's indices begin and hence do not satisfy the strict charging
inequality.

Thus the source's bounds are correct, but Lemma 1 directly gives the sharper
estimates

\[
 \sum_iw_i\le a^3-a+(3a+1)D
\]

and

\[
 Q\le a^3-a+(3a+3)D+3D^2.
\]

The weaker displayed source inequalities (3.6) and (1.1) therefore remain
valid.  Comparing either version with `V_a` yields
`D\ge(1-o(1))a^{3/2}`.

### Repeated-corner correction

A side trail is

\[
 b_{k,s}(0),b_{k,s}(1),\ldots,b_{k,s}(s)
 \quad\text{with}\quad
 b_{k,s}(s)=b_{k+1,s}(0).
\]

To make the distinct selected order equal to (3.2), the shared corner must be
selected from the occurrence assigned to the half-open set `B_{k,s}`.  This
cannot be described uniformly as the later occurrence.  For example, in the
order (3.2), the corner

\[
 b_{0,s}(0)=b_{5,s}(s)
\]

occurs earlier in the `B_{0,s}` trail and later in the `B_{5,s}` trail, while
the half-open convention assigns it to `B_{0,s}`.  Conversely,
`b_{0,s}(s)=b_{1,s}(0)` is assigned to the later `B_{1,s}` trail.  Selecting
the designated copy, rather than always the later copy, repairs lines
204--206 without changing the order or the run certificate.

## 6. Binary run structure in a side batch

Fix one side batch and write its intact blocks in their actual radius order as
`W_1,\ldots,W_m`, where `W_j` has length `s_j\le a`.  Reversal is allowed
independently for every block.

For even side types `k=0,2,4`, the threshold in (4.2) gives

\[
                         10^{s_j-1}
 \quad\text{or}\quad
                         0^{s_j-1}1.
\]

Thus every block contains exactly one `1`, at an endpoint.  A run can join
the endpoint `1`s of two adjacent blocks.  It can meet three blocks only when
the unique radius-one block, whose whole word is the single symbol `1`, lies
between two such endpoint symbols.  Hence every run has at most three
vertices, and at most one run in the batch can meet three blocks.

For odd side types `k=1,3,5`, the word is

\[
                         01^{s_j-1}
 \quad\text{or}\quad
                         1^{s_j-1}0.
\]

The radius-one block is the single symbol `0`.  Every nonempty `1`-run meets
at most two consecutive blocks.  Its number of vertices is at most
`2a-2` (in fact distinct radii make the maximum slightly smaller).  These
facts are independent of both the radius permutation and all reversals.

## 7. Repair of the arbitrary-radius/reversal direct scan

Discard the first and last four blocks of a batch.  Let `i` lie in a retained
block `W_j`; then the nine-block window

\[
                         W_{j-4},\ldots,W_{j+4}
\]

lies in the batch.

### Even batches

Each of the nine blocks contributes one endpoint `1`.  Suppose there were no
internal maximal run in this window which avoids `i`.  The nine block
singletons would then all have to belong to at most three runs:

1. the run crossing the left edge of the window;
2. the run containing `i`, if `i` itself lies in a `1`-run; and
3. the run crossing the right edge of the window.

Each such run meets at most three blocks.  Covering all nine blocks would
force all three runs to meet exactly three blocks.  But a three-block run
requires the unique radius-one block as its middle block, so at most one such
run exists.  This is impossible.  Hence a distinct maximal run lies wholly
inside the window.  It is bounded on both sides by zeros in the full batch,
so it is an internal run in the full selected-target incidence word as well.

### Odd batches

At least eight of the nine blocks have a nonempty `1`-run, since only the
unique radius-one block can be all zero.  If no internal run avoiding `i`
existed in the window, the positive portions of those eight blocks would
again have to be covered by the left-crossing run, the run containing `i`,
and the right-crossing run.  Each meets at most two blocks, so these three
runs cover at most six positive blocks, a contradiction.

In either parity, the resulting run lies strictly on one side of `i` and
inside the nine-block window.  The current block together with the at most
four intervening blocks has total physical length at most `5a`.  Consequently

\[
 v+1-i\le5a\quad(i<u),
 \qquad
 i-(u-1)\le5a\quad(i>v).
\]

This proves the source's weaker `6a` claim for every radius permutation and
every reversal.  It also explains why four discarded blocks, rather than a
bare assertion about batch boundaries, suffice.

### The center

The side blocks contain `M_a-1` targets, so the center must occur somewhere
in the full middle order.  If it lies between two blocks of one batch, split
that batch at the center for purposes of the scan.  There are then at most
`B+1` local batch segments.  Discarding four blocks at both ends removes at
most

\[
                         8a(B+1)
\]

side indices, and leave the center itself unassigned.  Selected runs lie
strictly inside a segment, so the center's threshold bit cannot extend them.
The additional `8a+1` unassigned indices contribute only `O(aD)`, already
present in (4.5).

## 8. Proposition 4 ledger after repair

Let `S=a(a+1)/2` be the number of indices of each side type.  For the three
odd side types, every assigned index has `\lambda\le2a`; for the three even
types, every assigned index has `\lambda\le2`.  Therefore

\[
 \sum_{i\in J}\lambda_i
 \le 3S(2a)+3S(2)
 =3a^3+O(a^2).
\]

The scan gives `C_\alpha+C_\beta\le10a` using the sharper `5a` span, or the
source's harmless `12a` using `6a`.  With the center repair,

\[
 M_a-|J|\le8aB+O(a).
\]

Lemma 1 and the avoidance ledger now yield

\[
 Q\le3a^3+8aBD+O(a^2+aD+D^2),
\]

exactly the asymptotic statement (4.5).  Since

\[
 V_a=4a^3+O(a^2),
\]

universality and `D=O(a)` imply

\[
                         BD=\Omega(a^2).
\]

If `B` is the number of maximal side-homogeneous batches, this gives
`B=\Omega(a)`, and hence a linear number `B-1` of genuine side changes.

## 9. Required source edits

The shortest safe repairs are:

1. In Lemma 1, define the two one-sided spans explicitly and state
   `2\le u_i\le v_i\le M_a-1` for internal runs.
2. In lines 204--206, replace "the later copy" by "the copy designated by
   the half-open partition."
3. Define a side-batched order after deleting the center; require `B` to be
   the number of maximal constant-side-type block runs.
4. State that an arbitrary center placement is treated by splitting at most
   one batch, increasing the local batch count by at most one.
5. Replace the unsupported "direct scan" sentence by the nine-block-window
   proof above.
6. Optionally replace `2a+1` by `2a` in Lemma 2 and record the sharper
   certificate congestions `C_\alpha\le2a`, `C_\beta\le a`.  This strengthens
   (3.6) and (1.1) but is not needed for the no-go theorem.

With items 1--5, every claimed obstruction in the research note has a
complete proof and the stated asymptotic conclusions follow.
