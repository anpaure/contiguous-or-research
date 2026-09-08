# Gaussian-annulus multiscale audit: exact recurrences and the additive no-go

Date: 2026-07-26

Method: pure mathematics only.

## 0. Verdict

Put

\[
 n=2m+1,\qquad W={n\choose m},\qquad B=\operatorname {Cat}_m=W/n.
\]

The proved PBBS compiler covers every central half-width
`h=o(sqrt(m))` with length `W+o(W)`, while the product-SCD exterior word
has length `o(W)` only when its cutoff is `H/sqrt(m)->infinity`.  This
note tests whether geometric intermediate scales can bridge the annulus

\[
                  h<q\le H.                              \tag{0.1}
\]

There are three exact conclusions.

1. **An auxiliary multiscale word cannot do it additively.**  A word of
   length `L` realizes at most `L` distinct targets of any fixed rank.
   Since

   \[
     {n\choose m-h-1}=(1-o(1))W\qquad(h=o(\sqrt m)),       \tag{0.2}
   \]

   every annulus module whose witnesses stay inside the module has length
   `(1-o(1))W`, even if its internal windows cross arbitrarily many
   geometric-scale seams.

2. **Appending after the paid PBBS baseline gives no fixed-rank capacity
   bonus at all.**  If a baseline word misses `M` targets at one rank, a
   suffix of length `E` can add at most `E` new targets at that rank,
   including every window crossing the baseline/suffix seam.  Thus
   `E>=M`.  An `o(W)` suffix is possible only if the baseline
   already misses `o(W)` targets at every annular rank.

3. **The exact product-SCD geometric recurrence telescopes.**  Partitioning
   chain pairs according to dyadic or arbitrary cutoff scales changes
   neither the catalog nor its total cost.  For an inner cutoff
   `h=o(sqrt(m))`, the exact normalized total is

   \[
                         2\sqrt2+o(1)                    \tag{0.3}
   \]

   in even dimension, and the same after the trimmed odd lift.  Cross-depth
   sharing is already maximal inside each emitted chain-pair gadget; a
   geometric partition only repartitions its positive summands.

There is a parallel PBBS statement.  Even an ideal variable-radius
multiscale cut/collar system costs at least the total trace mass of every
edge-disjoint residence packing.  Thus a critical Gaussian packing of
trace mass `Omega(B)` cannot be converted into `o(B)` cost by choosing
geometric collar radii.

Even interior insertions do not rescue a *geometric number* of scale
blocks.  If `K` auxiliary blocks of total length `E` are inserted in a
paid baseline, then at one fixed rank they create at most

\[
             2E+(n+1){K+1\choose2}                       \tag{0.3b}
\]

new targets.  Hence an `o(W)` insertion which repairs `Theta(W)` missing
targets needs

\[
                         K=\Omega(\sqrt{W/n}),            \tag{0.3c}
\]

not `O(log m)` geometric ports.

Consequently the Gaussian annulus cannot be closed by concatenating
independent shell words, by appending a product-SCD shell hierarchy, or by
replacing one fixed collar radius with dyadic radii.  The surviving escape
is genuinely nonadditive and macroscopically distributed: an in-place
insertion/replacement or braid must reuse the already paid `W` baseline
positions at at least exponentially many physical ports, or alter the
baseline globally.  Equivalently, one must share chain words across
different chain pairs, not merely share depths inside one pair.

## 1. The fixed-rank capacity of a literal word

Let

\[
                         Q=(Q_1,\ldots,Q_L)              \tag{1.1}
\]

be an arbitrary word of set-valued letters, and write

\[
 {\cal U}_r(Q)=
 \left\{\bigcup_{i=a}^bQ_i:
             1\le a\le b\le L,\ 
             \left|\bigcup_{i=a}^bQ_i\right|=r
 \right\}.                                               \tag{1.2}
\]

No disjointness, singleton, monotonicity, or ownership assumption is made
on the letters.

### Lemma 1.1 (one target per start at a fixed rank)

For every `r`,

\[
                         |{\cal U}_r(Q)|\le L.            \tag{1.3}
\]

#### Proof

Fix the left endpoint `a`.  As `b` increases, the unions in (1.2) form a
nested sequence.  Two nested finite sets of the same cardinality are
equal.  Thus this left endpoint produces at most one distinct rank-`r`
target.  Sum over `a`. \(\square\)

### Corollary 1.2 (the additive annulus lower bound)

Any self-contained word covering all rank-`r` subsets of an `n`-set has
length at least `{n choose r}`.  In particular, if `h=o(sqrt(m))`, then a
self-contained module covering the first lower annular rank `m-h-1` has
length

\[
 {2m+1\choose m-h-1}=(1-o(1)){2m+1\choose m}=(1-o(1))W.  \tag{1.4}
\]

The estimate follows either from the exact quotient product or from

\[
 \log {W\over {n\choose m-h-1}}
       ={(h+1)(h+2)\over m}+o(1)=o(1).                  \tag{1.5}
\]

Importantly, Lemma 1.1 already counts intervals crossing all internal
seams between geometric-scale submodules.  Such cross-scale windows do not
evade (1.4).

## 2. Exact capacity of one appended seam

Let `A=(A_1,...,A_L)` be the paid baseline and
`D=(D_1,...,D_E)` an appended multiscale suffix.  Put `Q=A||D`.

### Lemma 2.1 (one-seam append bound)

At every rank `r`,

\[
 |{\cal U}_r(Q)\setminus{\cal U}_r(A)|\le E.             \tag{2.1}
\]

Consequently, if `A` misses `M_r(A)` of the rank-`r` targets and `Q`
covers them all, then

\[
                              E\ge M_r(A).               \tag{2.2}
\]

#### Proof

Every interval not wholly inside `A` has its right endpoint at one of the
`E` positions of `D`.  Fix such a right endpoint.  As the left endpoint
moves left, the interval unions form a nested chain, and therefore contain
at most one distinct rank-`r` set.  Summing over the `E` possible right
endpoints proves (2.1), and (2.2) follows.
\(\square\)

The same result holds when `D` is itself a concatenation of arbitrarily
many scale modules: regard their total concatenation as one suffix.  If
suffixes are appended on both sides of a baseline whose total union is the
ground set, an interval of nonfull rank cannot cross both sides, and the
same argument applies separately at the two exterior seams.

Equivalently, for an arbitrary recursive append hierarchy

\[
 Q^{(j+1)}=Q^{(j)}\Vert D_j,\qquad |D_j|=e_j,
\]

the exact fixed-rank deficit recurrence is

\[
 M_r(Q^{(j+1)})\ge M_r(Q^{(j)})-e_j.                    \tag{2.3}
\]

Therefore

\[
 \sum_{j<J}e_j\ge M_r(Q^{(0)})-M_r(Q^{(J)}).            \tag{2.3a}
\]

This is the scale-independent recurrence requested by a dyadic-band
scheme: changing the scale ratio cannot make one appended letter remove
more than one deficit at a fixed rank.

### Theorem 2.2 (a geometric number of interior ports is still too small)

Split the paid baseline into `K+1` consecutive blocks and insert `K`
auxiliary words, of total length `E`, in the intervening gaps.  Let `Q`
be the resulting word and `A` the original baseline.  Then, at every rank
`r`,

\[
 |{\cal U}_r(Q)\setminus{\cal U}_r(A)|
 \le 2E+(n+1){K+1\choose2}.                              \tag{2.4}
\]

#### Proof

First consider intervals with at least one endpoint in an inserted word.
Those whose right endpoint is new contribute at most `E` targets, one for
each right endpoint, by the nested-chain argument of Lemma 2.1.  Among the
remaining intervals, the left endpoint is new and the right endpoint is
old; fixing the left endpoint and moving the right endpoint again gives a
nested chain, hence at most `E` further targets.

It remains to consider intervals with two old endpoints.  If both lie in
the same old block, the interval was already present in `A`.  For every
fixed pair of distinct old endpoint blocks, the intervening whole blocks
have fixed union.  The possible left suffixes and right prefixes are two
nested Boolean chains.  Their distinct rank-`r` unions form an antichain
in the product and number at most `n+1`.  There are
`{K+1 choose 2}` pairs of old endpoint blocks.  Summing proves (2.4).
\(\square\)

### Corollary 2.3 (port-count lower bound)

If the baseline misses `M_r(A)=Theta(W)` rank-`r` targets, the final word
covers the rank, and `E=o(W)`, then

\[
                         K=\Omega(\sqrt{W/n}).            \tag{2.5}
\]

In particular, inserting one block at each of `O(log m)` geometric scales
cannot bridge the annulus.  This does not exclude a distributed PBBS
compiler with exponentially many short ports: `sqrt(W/n)=o(W)`.  It does
exclude the proposed small-scale hierarchy as a mechanism by itself.

### Corollary 2.4 (necessary annulus profile of an appendable baseline)

Let `A_m` be any `W+o(W)` central baseline and let a suffix of length
`o(W)` be required to close an annulus `h<q<=H`.  Necessarily

\[
 \max_{h<q\le H}
 \left(
 {n\choose m-q}-|{\cal U}_{m-q}(A_m)|
 \right)=o(W),                                         \tag{2.6}
\]

and likewise on the upper side.  Thus an append-only annulus proof must
first establish that the paid baseline already near-covers every annular
rank.  This is essentially the missing simultaneous-support statement,
not a consequence of geometric scale selection.

An **interior** insertion is not governed by the one-seam estimate, but
Theorem 2.2 shows that a bounded or logarithmic number of insertion sites
is still inadequate.  A genuinely distributed in-place replacement
remains a real escape.

## 3. The product-SCD recurrence is exactly telescoping

Work first in even dimension `2m`.  For a half-cube SCD chain `C`, let
`a(C)` be its minimum rank and `w(C)=w_m(a(C))` its increment-word length.
For an ordered pair `(C,D)`, the gadget `L(C)||R(D)` covers the full product
of the two chains.  In particular, it simultaneously covers every depth
at which that pair has a target.

Define the exact shell density

\[
 \Delta_m(s)=
 \sum_{a+b=s}A_m(a)A_m(b)\bigl(w_m(a)+w_m(b)\bigr),     \tag{3.1}
\]

with the sum restricted to `0<=a,b<=floor(m/2)`.  The exact product-SCD
tail length satisfies

\[
 L_m(r)=\sum_{s=0}^r\Delta_m(s),\qquad
 L_m(r)-L_m(r-1)=\Delta_m(r).                           \tag{3.2}
\]

The formula is equivalent to

\[
 L_m(r)=2\sum_aA_m(a)w_m(a)C_m(r-a)                    \tag{3.3}
\]

from the audited tail theorem.

Choose arbitrary geometric or nongeometric cutoffs

\[
 h_0<h_1<\cdots<h_J,qquad r_j=m-h_j-1.                 \tag{3.4}
\]

Use the outer module with chain-pair minima `s<=r_J`, and for each
annular scale use the pairs `r_{j+1}<s<=r_j`.  These modules cover the
whole exterior outside `h_0`: a target belongs to a unique half-chain
pair, and that pair is placed in exactly one module.  Their exact total
length is

\[
 \begin{aligned}
  L_m(r_J)+\sum_{j=0}^{J-1}
       \bigl(L_m(r_j)-L_m(r_{j+1})\bigr)
       &=L_m(r_0).                                      \tag{3.5}
 \end{aligned}
\]

Thus neither the scale ratio nor the number of scales changes the cost.
The fixed-Gaussian audit gives

\[
 {L_m(m-h_0-1)\over {2m\choose m}}\longrightarrow2\sqrt2
       \qquad(h_0=o(\sqrt m)).                          \tag{3.6}
\]

The trimmed odd lift doubles numerator and asymptotically doubles the
middle width, so (3.6) has the same normalized constant in odd dimension.

Equation (3.5) is stronger than the observation that separate tail words
are wasteful.  One gadget already shares all depths belonging to its chain
pair.  Geometric scales cannot add more cross-depth sharing inside that
model.  A saving must identify structure **between different chain pairs**
or replace letters already paid for by the central baseline.

## 4. Variable-radius PBBS collars also retain the packing obstruction

The fixed-height clustered-seam theorem proves that at a Gaussian cutoff a
critical residence packing forces `Omega(B)` quotient charge.  Allowing a
different geometric radius at every cut does not remove this obstruction.

Consider the following idealized model, which is at least as permissive as
independent local dominance collars.  A facility is a cut edge `e` with a
chosen radius `R_e>=1` and cost `R_e`.  A residence interval `I` may be
served by `e` only if

\[
                         e\in I,\qquad |I|\le R_e.       \tag{4.1}
\]

### Lemma 4.1 (multiscale facility lower bound)

For every pairwise edge-disjoint residence packing `P`, every serving
facility system satisfies

\[
                         \sum_eR_e\ge\sum_{I\in P}|I|.  \tag{4.2}
\]

#### Proof

Assign to each `I in P` one facility which serves it.  Two edge-disjoint
intervals cannot be assigned the same cut edge.  The assigned facilities
are therefore distinct, and each has radius at least `|I|`.  Summing gives
(4.2). \(\square\)

In particular, the simple fixed-core critical-saturation certificate in
`MATH_AUDIT_CMS_AND_CRITICAL_RESIDENCE_SATURATION_20260726.md` has packed
trace mass `Omega_A(B)`.  Lemma 4.1 forces `Omega_A(B)` cost even after
arbitrary dyadic radius choices.  If nearby cuts are clustered, the
stronger span inequality

\[
 \sum_J(7H+3S_J-3)\ge\sum_{I\in P}|I|                  \tag{4.3}
\]

from
`MATH_THEOREM_CLUSTERED_SEAM_CRITICAL_PACKING_OBSTRUCTION_20260726.md`
applies.  Hence both singleton multiscale collars and the established
clustered generalization remain critical under a critical packing.

## 5. Exact remaining positive target

The preceding results do **not** disprove a multiscale annulus bridge.
They locate the form it must take.

A successful construction must violate at least one additive premise
above.  Concretely it must do one of the following.

1. Insert or replace `o(W)` letters *inside* the paid baseline so that
   `Theta(W)` old start positions acquire new annular witnesses.
2. Recode one baseline block into a braid in which the same physical
   letters serve many different SCD chain pairs; sharing only the depths
   of one pair is already exhausted by (3.5).
3. Prove directly that the existing PBBS baseline satisfies the
   near-coverage condition (2.4), and then use an `o(W)` suffix only for
   the true residual.
4. Establish `(ST_A)`; this removes the critical packed trace mass before
   any collar is charged.

Therefore a geometric sequence of cutoffs by itself is not a new lane.
The mathematically distinct gate is a **baseline-changing annulus braid**.
The correct recurrence for such a future construction must contain a
negative replacement-credit term

\[
 E_{j+1}\le E_j+\Delta_j-\operatorname {credit}_j,       \tag{5.1}
\]

where the credits come from deleted/reused baseline positions and satisfy

\[
 \sum_j\operatorname {credit}_j
   =\sum_j\Delta_j-o(W).                                \tag{5.2}
\]

Neither scale telescoping (3.5) nor local erosion credit supplies (5.2).
Producing that nonlocal credit, while retaining the middle witnesses, is
the exact Gaussian-annulus problem.
