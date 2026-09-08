# Parity projection turns common-path rounding into a colored Hall problem

**Status (2026-08-21).**  The reductions and identities below are proved.
They do not produce the missing integral palette selection.  They replace
the informal requirement to "round two rank parities with the same paths"
by one projected path matching plus explicit, rank-separated Hall
deficiencies.  They also isolate the central obstruction as an
almost-rainbow, queue-coherent middle-level path packing.

## 1. Legal traces and their transition colors

Let `pi` be a permutation of `[n]`, let `C_k(pi)` be its first-`k` set, and
fix `f`.  A legal tail-MTF step moves a letter from a position at least `f`
to the front.  Consider one free core

\[
 \pi_0\longrightarrow\pi_1\longrightarrow\cdots
 \longrightarrow\pi_a,                                 \tag{1.1}
\]

and retain the first step of its fixed exit bridge, writing the resulting
state as `pi_(a+1)`.  All these steps are legal.

### Lemma 1 (one-step reconstruction)

For every `1<=k<f` and `1<=t<=a+1`,

\[
 C_{k-1}(\pi_{t-1})
   =C_k(\pi_{t-1})\cap C_k(\pi_t),                      \tag{1.2}
\]

\[
 C_{k+1}(\pi_t)
   =C_k(\pi_{t-1})\cup C_k(\pi_t).                     \tag{1.3}
\]

#### Proof

Write the old state as `(p_1,...,p_n)` and suppose that `x`, in position at
least `f`, is moved to the front.  Since `k<f`, the old and new first-`k`
sets are

\[
 \{p_1,\ldots,p_k\},\qquad \{x,p_1,\ldots,p_{k-1}\}.
\]

Their intersection and union are respectively the old first-`(k-1)` set
and the new first-`(k+1)` set.  This proves both identities.  \(\square\)

The same argument iterates.  If all indicated times lie in a legal
trajectory and `k+r<f`, then

\[
 C_{k+r}(\pi_t)=\bigcup_{h=0}^{r}C_k(\pi_{t-h}),         \tag{1.4}
\]

while, for `r<k`,

\[
 C_{k-r}(\pi_{t-r})=\bigcap_{h=0}^{r}C_k(\pi_{t-h}).    \tag{1.5}
\]

Thus the time-ordered trace at one rank determines every nearby rank trace.
Parity projection is useful not because the other parity is independent,
but because it expresses every omitted rank using only a one-step color.

## 2. Exact parity projection

Use the fixed-endpoint palette parameters

\[
 n=2m+1,\qquad
 K=\{m-H,\ldots,m+1+H\},\qquad \max K<f,                \tag{2.1}
\]

and let

\[
 P=\{k\in K:k\equiv m\pmod 2\},\qquad Q=K\setminus P. \tag{2.2}
\]

The choice of `P` makes the central rank `m` a projected resource and the
other central rank `m+1` an upward transition color.

For a core `i` of length `a_i`, write

\[
 A_{i,k,t}=C_k(\pi_{i,t})\qquad(0\le t\le a_i+1).       \tag{2.3}
\]

For `q in Q`, define its derived color at core time `t` as follows.

- If `q-1 in K`, put

  \[
  B_{i,q,t}=A_{i,q-1,t-1}\cup A_{i,q-1,t}.              \tag{2.4}
  \]

- The only remaining possibility is `q=min K`.  Then `q+1 in P`; put

  \[
  B_{i,q,t}=A_{i,q+1,t}\cap A_{i,q+1,t+1}.              \tag{2.5}
  \]

The state at `a_i+1` in (2.5) is supplied by the first step of the already
present exit bridge, so no extra physical step is introduced.

### Proposition 2 (lossless parity projection)

For every `q in Q` and `1<=t<=a_i`,

\[
 B_{i,q,t}=C_q(\pi_{i,t}).                              \tag{2.6}
\]

Consequently the selected paths in the `P`-projection, with their temporal
order retained, determine all omitted-rank core observations exactly.  If
the core is band-simple, then

\[
 U_{i,q}:=\{B_{i,q,t}:1\le t\le a_i\}                  \tag{2.7}
\]

has size `a_i`.

#### Proof

Equation (2.4) is (1.3) with `k=q-1`, and (2.5) is (1.2), shifted one time
forward, with `k=q+1`.  Band-simplicity gives the last assertion.  \(\square\)

This is the precise sense in which the two parities need not be rounded by
two independently chosen matchings.  There is one path choice.  Its
`P`-rank observations are resources, and its `Q`-rank observations are
deterministic colors of transitions between those resources.

## 3. After the path choice, the omitted ranks decouple

We now specialize to the length-at-most-`W` palette normalization.  Let all
cores have length `a`, let there be `s` slots, and put

\[
 N=sa,\qquad M_k={n\choose k}.                           \tag{3.1}
\]

For every rank `k`, choose real quotas `r_(i,k)` and discard/dummy quotas
`h_(i,k)` satisfying

\[
 r_{i,k}+h_{i,k}=a.                                     \tag{3.2}
\]

At either middle rank take `h_(i,k)=0`, so the total real quota is `N`.
At every outer rank choose the balanced quotas from the fractional palette
construction, so

\[
 \sum_i h_{i,k}=N-M_k,qquad \sum_i r_{i,k}=M_k.         \tag{3.3}
\]

Suppose one legal path has now been fixed in every slot.  Fix `q in Q` and
form a bipartite graph `G_q`: its left vertices are the slots, slot `i` has
demand `r_(i,q)`, its right vertices are the real rank-`q` targets, and `i`
is adjacent precisely to the targets in `U_(i,q)` from (2.7).  A completion
at rank `q` is a capacitated matching that assigns `r_(i,q)` distinct
observed targets to every slot, using no target twice.

For `I subseteq [s]`, define the duplicate mass of the corresponding block
family by

\[
 Q_q(I)=\sum_{i\in I}|U_{i,q}|-
          \left|\bigcup_{i\in I}U_{i,q}\right|
       =a|I|-\left|\bigcup_{i\in I}U_{i,q}\right|.      \tag{3.4}
\]

### Theorem 3 (exact colored-Hall deficiency)

The maximum number `mu_q` of pairwise distinct rank-`q` claims that can be
made subject to the slot capacities is

\[
 \mu_q=\sum_i r_{i,q}-\delta_q,                         \tag{3.5}
\]

where

\[
 \begin{aligned}
 \delta_q
  &=\max_{I\subseteq[s]}
      \left(\sum_{i\in I}r_{i,q}
       -\left|\bigcup_{i\in I}U_{i,q}\right|\right)_+  \\
  &=\max_{I\subseteq[s]}
      \left(Q_q(I)-\sum_{i\in I}h_{i,q}\right)_+ .     \tag{3.6}
 \end{aligned}
\]

In particular, the fixed paths admit a complete rank-`q` decoration if and
only if every block subfamily obeys

\[
 Q_q(I)\le\sum_{i\in I}h_{i,q}.                         \tag{3.7}
\]

#### Proof

Replace slot `i` by `r_(i,q)` clones having the same neighborhood.  The
defect form of Hall's theorem says that the maximum matching leaves

\[
 \max_X(|X|-|N(X)|)_+
\]

left clones unmatched.  For a fixed set of represented slots, this
quantity is maximized by taking every clone of each represented slot.
Hence the maximum may be taken over slot sets `I`, giving the first line of
(3.6) and (3.5).  Substituting `r_(i,q)=a-h_(i,q)` and (3.4) gives the
second line.  Vanishing deficiency is exactly Hall's condition.  \(\square\)

The dummy vertices introduce no further restriction.  At an outer rank
every slot is adjacent to every dummy, the balanced construction has
`h_(i,q)<=N-M_q`, and the quotas sum to the number `N-M_q` of dummies.
After the real assignment, partition the dummy set into labeled pieces of
sizes `h_(i,q)` and give the `i`th piece to slot `i`.

Theorem 3 is rank-separated: once the common paths have been fixed, the
graphs `G_q` for distinct `q` share no vertices and can be completed
independently.  All cross-rank coupling is therefore in the first path
choice, not in the subsequent decoration.

### Corollary 4 (a sufficient one-parity rounding target)

Assume that one path per slot has been selected so that all required
`P`-rank claims are distinct.  Then the number of real band targets left by
optimal `Q`-rank decorations is at most

\[
 2(W-N)+\sum_{q\in Q}\delta_q.                          \tag{3.8}
\]

Here the first term is the unavoidable budget deficit at the two middle
ranks; one of those ranks is in `P` and the other is in `Q`.  Therefore

\[
 \sum_{q\in Q}\delta_q=o(W)                             \tag{3.9}
\]

together with the `P`-matching rounds the same tail-MTF paths to a
full-band defect selection with `o(W)` real leave and collision.  If every
`delta_q` is zero, the decoration is an actual augmented matching.

#### Proof

At an outer rank, (3.3) and Theorem 3 leave at most `delta_q` targets.  At a
middle rank, (3.5) supplies `N-delta_q` distinct targets out of `W`, leaving
`W-N+delta_q`.  The `P`-matching has the analogous unavoidable middle-rank
leave `W-N` and no outer-rank leave.  Summation gives (3.8).

To obtain full-size decorations when `delta_q>0`, first use a maximum
matching.  There are exactly `delta_q` unmatched left clones.  In each slot,
assign those clones arbitrary distinct further targets from its `a`-set
`U_(i,q)`; there are enough because `r_(i,q)<=a`.  These added assignments
create at most `delta_q` repeated claim occurrences and can only reduce the
target leave.  Hence total collision plus leave is at most

\[
 2(W-N)+2\sum_{q\in Q}\delta_q=o(W).                    \tag{3.10}
\]

The dummy quotas are then filled by the independent partitions described
above.  \(\square\)

## 4. The central condition is exactly an almost-rainbow path packing

Take `q=m+1`.  Its lower projected rank is `m`.  Put

\[
 A_{i,t}=C_m(\pi_{i,t}),\qquad
 B_{i,t}=A_{i,t-1}\cup A_{i,t}=C_{m+1}(\pi_{i,t}).      \tag{4.1}
\]

There are no dummies at rank `m+1`, so `h_(i,m+1)=0`.  Duplicate mass is
monotone under adding blocks.  Theorem 3 therefore reduces to

\[
 \delta_{m+1}
  =Q_{m+1}([s])
  =N-\left|\bigcup_{i=1}^sU_{i,m+1}\right|.             \tag{4.2}
\]

Thus the central omitted parity has `o(W)` defect if and only if the `N`
union colors in (4.1) have only `o(W)` repetitions.  This is the exact
almost-rainbow condition; an unspecified `o(1)` matching error is not
enough.

In the middle-level inclusion graph, each block traces the alternating path

\[
 A_{i,0},B_{i,1},A_{i,1},B_{i,2},\ldots,
 B_{i,a},A_{i,a}.                                       \tag{4.3}
\]

If the post-move `A` targets and the `B` colors were both globally distinct,
(4.3) would be a packing of middle-level paths covering `N` vertices on
each side.  Since the number of blocks is `s=o(W)`, its boundary roots are
asymptotically negligible.  However these are not arbitrary middle-level
paths.  If `x_t` is the emitted letter, their Johnson transitions satisfy

\[
 A_{i,t}=A_{i,t-1}\setminus\{x_{t-m}\}\cup\{x_t\},     \tag{4.4}
\]

and every re-entry is delayed by at least `f`.  This queue coherence is why
the ordinary Middle Levels Hamilton-cycle theorem does not solve (4.2).

For an outer omitted rank, (3.6) is the correct replacement for the word
"rainbow": its unavoidable repeated observations are paid for by its dummy
budget.  The requirement is that **every block subfamily's** duplicate mass
stay within that subfamily's discard budget, up to total `o(W)` deficiency.
A bound only for the full family is not Hall's condition.

## 5. Two rigorous obstructions to a naive second stage

### 5.1 Independent block sampling retains the coupon defect

Under the canonical symmetric simple-core law, a fixed middle target occurs
in a length-`a` core with probability exactly `a/W`.  If the `s` slots are
sampled independently, then a fixed rank-`(m+1)` target is absent from all
of them with probability

\[
 (1-a/W)^s.                                             \tag{5.1}
\]

Consequently the expected number of missing central colors is

\[
 \mathbb E\left(W-\left|\bigcup_iU_{i,m+1}\right|\right)
   =W(1-a/W)^s
   =(e^{-N/W}+o(1))W=(e^{-1}+o(1))W.                   \tag{5.2}
\]

Equivalently,
`E delta_(m+1)=N-W+W(1-a/W)^s=(e^(-1)+o(1))W` by (4.2).
No independence within a block is assumed.  Thus
the exact fractional marginals do not by themselves produce the required
rainbow correlation.  A successful rounding must correlate different
slots at linear scale.

### 5.2 Ordered-trace-preserving switches have only boundary power

Suppose two legal cores have identical time-indexed `P`-traces

\[
 C_k(\pi_t)=C_k(\pi'_t)
 \quad(k\in P, 1\le t\le a).                           \tag{5.3}
\]

For every omitted rank reconstructed upward by (2.4), all its derived
colors at times `2,...,a` coincide; only time `1`, which uses the unrecorded
seed trace, can differ.  For the possible bottom rank reconstructed by
(2.5), times `1,...,a-1` coincide; only time `a`, which uses the first exit
state, can differ.  Hence such a switch changes at most one observation per
omitted rank per block.

Across the palette there are at most `|Q|s=o(W)` such boundary
observations.  Therefore hidden-state or endpoint switches that preserve
the ordered parity traces cannot repair a `Theta(W)` opposite-parity
defect.  Any successful method must select or reorder the parity traces in
bulk; it cannot postpone the common-path correlation until after those
traces have been fixed.

There is an even stronger typical-fiber rigidity for the canonical palette.
Theorem 4.2 and Corollary 4.3 of
`MATH_CANDIDATE_PARITY_FIBER_RIGIDITY_20260821.md` show that, with failure
probability at most `exp(-n/10+o(n))`, the induced Johnson graph on either
central-rank core deck is exactly its temporal path, and that the fractional
law may be supported entirely on such cores.  Lemma 3.1 there then says that
the **unordered** deck fixes its order up to reversal and fixes every
internal adjacent-rank union color; only one boundary replacement remains.

## 6. Exact remaining theorem

The parity language can now be stated without ambiguity.  What is still
needed is a selection of one fixed-endpoint tail-MTF path per slot such that

1. the augmented real/dummy resources at every rank in `P` form a matching;
2. the deterministic color families `U_(i,q)` satisfy
   `sum_(q in Q) delta_q=o(W)`, with `delta_q` given exactly by (3.6).

Unconditioned independent sampling is insufficient by (5.2); condition 1 is
not presently known to imply condition 2.  A post hoc lift inside fixed
trace fibers is insufficient by Section 5.2.  The missing
result is therefore a **colored parity matching theorem with queue-coherent
path edges and subfamily Hall control**.  It is one common selection
problem, not two separate matchings, and it must create global correlation
while the projected paths are chosen.

## 7. Finite audit

All finite checks were run on `ssh h100`, not on the local machine.  An
exhaustive check of 310,080 legal transition--rank instances for `4<=n<=7` verified both
prefix identities (1.2)--(1.3) at every admissible rank.  A separate
exhaustive check of 75,104 small capacitated bipartite instances compared
maximum matchings with (3.5)--(3.6) and found exact agreement.  These checks
audit the indices and deficiency normalization; the proofs do not depend on
them.
