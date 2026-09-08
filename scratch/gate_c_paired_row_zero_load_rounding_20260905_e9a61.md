# Paired-Position Row Rounding for the Zero-Load Objective

Date: 2026-09-05. Independent scratch work, suffix `e9a61`.

## 0. Result and Boundary

This note does not prove the asymptotic conjecture. It develops a specific
positive rounding mechanism, rather than another degree/codegree argument
or another independent-sampling benchmark.

The architecture uses full permutation-cycle rows. Each row has `n=2b`
cyclic starts and costs exactly `n+2H` literal set-valued letters after
band compilation. It is therefore enough to select about `W(n)/n` rows.
Complementation couples the two sides of the Gaussian band automatically.

The new positive assertions are:

1. Reversing independently the `b` consecutive coordinate pairs in one
   row gives `2^b` literal row variants. Every band target in their union
   belongs to a unique positional window form and depends on at most two
   orientation bits.
2. Relative to all the other rows, the orientations preserving every
   already attained per-target integer cap form an explicitly computable
   Boolean subcube. No SAT or matching hypothesis is needed for this claim.
3. If `A_1` and `A_2` are the total weights of newly useful targets depending
   on one and two free bits, there is a deterministic, no-loss row update
   gaining at least `A_1/2+A_2/4`. Its physical position count is unchanged.
4. Without imposing no-loss protection, the exact best row in this entire
   `2^b`-element family can be found for the simultaneous Gaussian-band
   zero-load objective in `2^{O(H)} poly(n)` operations, when `n` is
   divisible by four. The proof folds the near-antipodal interaction graph
   into a bounded-width cyclic graph and gives a shortest-path rounding.
5. Assigned old witnesses permit simultaneous updates of all rows with no
   coverage loss. There is an exact formula and deterministic rounding for
   the expected newly covered holes; the memberships inside each row are
   correlated, not independently thinned target tokens.

The missing theorem is that suitably chosen/reassigned witnesses and row
frames continue to expose sufficiently many useful targets, or that the
loss-allowing exact row oracle escapes all positive-density local minima.
Neither assertion follows merely from the lemmas below.

## 1. Full Rows and Their Exact Cost

Let `n=2b>=8`, let `1<=H<=b-2`, and put

\[
 \ell=b-H,\qquad u=b+H,\qquad W=\binom{2b}{b}.
                                                               \tag{1.1}
\]

A row is a permutation `w=(w_0,...,w_(n-1))` of the ground coordinates,
read cyclically. Its rank-`s` deck is

\[
 S_s(w)=\{I_s^w(a):a\in\mathbb Z_n\},\qquad
 I_s^w(a)=\{w_a,\ldots,w_{a+s-1}\}.                    \tag{1.2}
\]

For `1<=s<n`, all `n` targets in this deck are distinct. A proper arc of a
directed cycle has a unique directed entering boundary, which its label
set recovers.

The actual compiled block is

\[
 B_j(w)=\{w_j,\ldots,w_{j+\ell-1}\},
           \qquad0\le j<n+2H.                         \tag{1.3}
\]

The source prefix has `n+u-1` letters. All letters of (1.3) are nonempty,
and every designated target has the exact witness

\[
 I_s^w(a)=\bigcup_{j=a}^{a+s-\ell}B_j(w),
       \qquad0\le a<n,\quad\ell\le s\le u.             \tag{1.4}
\]

Thus a list of `t` rows compiles separately and concatenates to exactly

\[
                    t(n+2H)                           \tag{1.5}
\]

letters. Row replacement does not change this cost. It creates no new
fragment boundaries, and there is no cost per orientation bit or rank.

Write `a_s(T)` for the number of selected rows whose deck contains `T`.
Full rows have the useful exact identity

\[
 a_{n-s}(\Omega\setminus T)=a_s(T).                    \tag{1.6}
\]

Indeed the complement of the length-`s` window at start `a` is the
length-`n-s` window at start `a+s`. In particular the designated lower
and upper hole counts are identical, not merely equal in expectation.

For the conjecture one may ignore the single middle rank and optimize
twice the lower-band zero count. All results below also allow arbitrary
rank weights, omitted ranks, and integer per-target caps.

## 2. Two-Bit Window Geometry

Pair consecutive positions in a row:

\[
 P_i=\{w_{2i},w_{2i+1}\},\qquad i\in\mathbb Z_b.
\]

For `x in {0,1}^b`, let `w_x` reverse pair `i` exactly when `x_i=1`.
The row `w_0` is the original row. These are genuine permutations of the
same ground set; no letter repetitions or cleanliness issues arise.

### Lemma 2.1 (unique positional forms)

For every `2<=s<=n-2`:

1. `I_s^(w_x)(a)` depends only on the pairs split by the positional interval
   `[a,a+s-1]`. There are at most two such pairs.
2. The sets obtainable from different starts `a` are disjoint families.
3. A target obtainable at start `a` prescribes exactly one value of each
   split-pair bit and imposes no condition on any other bit.

Consequently one can enumerate the entire union of these `2^b` row decks
by at most four target variants per positional window.

#### Proof

A whole pair inside or outside the interval is invariant under its
reversal. A split pair contributes either its first or its second member,
which reverses when its bit reverses. This proves assertions 1 and 3.

Here is the positional uniqueness, including both parities. Subscripts on
the pair indices below are cyclic.

For `s=2r`, an even start `2i` contains the `r` full pairs
`P_i,...,P_(i+r-1)` and no split pair. An odd start `2i+1` splits
`P_i,P_(i+r)` and contains the `r-1` intervening full pairs. The occupancy
signature recovers the start. For `r=1`, the two split pairs are adjacent
in the directed pair cycle; because `b>=4`, their unordered pair has only
one such forward adjacency. For `r>1`, the intervening full-pair run
distinguishes the two possible endpoint orientations. The case `r=b-1`
is also unambiguous: the full run goes around the longer, not the empty,
arc between the two split pairs.

For `s=2r+1`, an even start has `r` full pairs followed by one split pair;
an odd start has one split pair followed by `r` full pairs. Here
`1<=r<=b-2`. Within either type the full run recovers its start. If the
two types had the same signature, the split pair would be the same and
the full runs of length `r` immediately before and after it would be
equal. A nonempty proper cyclic interval of pair indices has a unique
start. Equality of those two starts would force `r=b-1`, excluded here.

The signature records only whether a pair is empty, split, or full, and
is independent of the orientation bits. Thus it also prevents equality
between variants at different starts. QED.

The restrictions excluding singleton and co-singleton ranks matter for
this uniqueness statement. The Gaussian band in (1.1) satisfies them.

## 3. The No-Loss Face Is a Subcube

Fix all rows except one. Let `c(T)` be the number of those other rows
containing a controlled target `T`. Set a nonnegative integer cap
`kappa(T)` for every controlled target. Its capped attained load is

\[
        C_x(T)=\min\{c(T)+\mathbf1_{T\in S(w_x)},\kappa(T)\},
                                                               \tag{3.1}
\]

where `S(w_x)` denotes the union of the controlled-rank decks. Cap one is
ordinary coverage. A skipped rank can be assigned cap zero.

Call an old row target `T in S(w_0)` protected if `c(T)<kappa(T)`.
Let `P` be the union of the split-pair indices of all protected targets.

### Theorem 3.1 (exact no-loss characterization)

\[
 \boxed{C_x(T)\ge C_0(T)\text{ for every controlled }T
        \quad\Longleftrightarrow\quad x_i=0\ (i\in P).}
                                                               \tag{3.2}
\]

Thus the full set of no-loss row variants is one explicitly determined
Boolean subcube. For cap one, only targets unique to the current row
create pins.

#### Proof

If `T` was absent from `w_0`, the new row can only increase its old load
`c(T)`. If `T` was present but `c(T)>=kappa(T)`, the other rows alone
already attain its cap, so it imposes no restriction.

The remaining targets are precisely the protected ones. For each such
target the old capped load is `c(T)+1`; preserving it requires that the
new row still contain `T`. By Lemma 2.1, that same target cannot reappear
at another start, and it remains at its unique start exactly when every
split-pair bit keeps its old value zero. Taking the union of these
requirements gives (3.2), both necessarily and sufficiently. QED.

This is stronger than a sufficient protection rule: within this particular
row family there are no additional no-loss variants outside the subcube.
It is not a characterization of all permutation-row replacements.

## 4. A Positive No-Loss Augmentation

Let `F=[b]-P` be the free bits from Theorem 3.1. Define `A` to be the
targets absent from `S(w_0)`, below cap among the other rows, and obtainable
in some pinned-compatible variant. Such a target has a unique form. Let
`d(T)` be the number of free bits in that form.

Necessarily `d(T)` is one or two: if it were zero, the target would already
belong to `S(w_0)`. Assign nonnegative weights `omega(T)` and put

\[
 A_j=\sum_{T\in A:\ d(T)=j}\omega(T),\qquad j=1,2.
\]

### Theorem 4.1 (quarter-weight augmentation)

There is a deterministically constructible no-loss row variant for which

\[
 \boxed{\sum_T\omega(T)(C_x(T)-C_0(T))
               \ge \frac{A_1}{2}+\frac{A_2}{4}
               \ge\frac14\sum_{T\in A}\omega(T).}       \tag{4.1}
\]

It uses exactly the same `n+2H` output positions as the old row.

#### Proof and Rounding

Choose the free bits independently and uniformly, keeping every pin zero.
Every realization is no-loss by Theorem 3.1. A newly useful target `T`
requires one specified pattern on its `d(T)` free bits, hence appears with
probability `2^(-d(T))`. Its appearance increases its capped load by
exactly one. Sum these gains to obtain the first expression in (4.1).
No independence between target events is required.

For a deterministic choice, expose free bits one at a time. For each
candidate value of the next bit, the conditional expected gain is the sum
over useful targets of zero if their pattern has already failed, or
`omega(T) 2^(-r(T))` if `r(T)` prescribed bits remain unexposed. Choose
the value with greater conditional expectation. Its value is at least
the average of the two choices. At the end the actual gain is at least
the initial expectation. All useful patterns have size at most two, so
they can be enumerated directly from the at-most-four variants per window.
Finally apply the literal compiler (1.3). QED.

For unit weights, even a single accessible hole guarantees at least one
hole is removed, by integrality. This statement is simultaneous across
the whole controlled rank set and does not charge one fragment per rank.

The set `A` can be empty. The theorem does not deduce availability from
the number of holes alone.

### An Explicit Nontrivial Update

Take two identical rows on 16 coordinates and control ranks 6 through 10.
Keep one row unchanged. It protects every old target, so every bit of the
other row is free. At each odd controlled rank there are 16 new one-bit
alternatives. At each even controlled rank there are eight sensitive
windows, each with three new two-bit alternatives; the eight full-pair
windows are invariant. Lemma 2.1 makes all those alternatives distinct.
Thus `A_1=32`, `A_2=72`, and Theorem 4.1 guarantees gain at least 34.

In fact reversing every consecutive pair in the second row gains exactly
56 band targets: all 32 odd-rank windows and eight windows at each of the
three even ranks change. No more are possible in this row family because
the other 24 window forms are invariant. The old 80 band targets remain
covered, and the new family covers 136, using the same two literal blocks
of total length `2(16+4)=40`. This is a concrete no-loss construction,
not an asymptotic near-cover claim.

## 5. An Exact Loss-Allowing Row Oracle

The preceding face is deliberately conservative. There is also an exact
algorithm over all `2^b` variants, allowing the loss of an old unique target
if other gains compensate for it.

Let `phi_T` be any specified real-valued per-target function on
nonnegative integer loads. In particular use the convex hinge

\[
 \phi_T(a)=\omega(T)(\kappa(T)-a)_+,                   \tag{5.1}
\]

and for zero loads take `kappa=1`. Since each row has at most one
occurrence of any target,

\[
 \sum_T\phi_T(c(T)+\mathbf1_{T\in S(w_x)})
  =\sum_T\phi_T(c(T))
       +\sum_{s\text{ controlled}}\sum_{a=0}^{n-1}
               w_s(I_s^{w_x}(a)),                    \tag{5.2}
\]

where `w_s(T)=phi_T(c(T)+1)-phi_T(c(T))`. The first term is constant.
For cap one, `w_s(T)=-omega(T)` on external holes and zero elsewhere.

Equation (5.2) is exact; it does not replace `phi(E a)` by `E phi(a)`.
Convexity is not needed for the identity or the oracle.

### Theorem 5.1 (folded-band shortest-path rounding)

Assume `n=4m`, so `b=2m`, and let

\[
 R=\lceil H/2\rceil+1,\qquad R<m/2.                    \tag{5.3}
\]

Given the external weights in (5.2), its exact minimum over all paired-row
variants, with any additional pinned orientation bits, can be computed in

\[
                O(mR4^{2R+1})+\operatorname{poly}(n,H)
                                                               \tag{5.4}
\]

arithmetic operations. The weight-table preparation is polynomial. In
particular this is `2^{O(H)} poly(n)`, versus `2^b` row variants.

The optimization has an exact integral unit-flow formulation on an
explicit layered acyclic graph of the same size. Any feasible fractional
flow in this formulation can be rounded to an actual row of no greater
cost.

#### Interaction Geometry

Write a window start as `a=2i+epsilon`, where `epsilon` is zero or one,
and write its rank as `s=2m+h`. Its endpoint pair index is

\[
 j=i+m+\left\lfloor\frac{\epsilon+h-1}{2}\right\rfloor
                   \pmod{2m}.                        \tag{5.5}
\]

If the initial or terminal pair is full, its bit simply does not appear
in that window's weight. Otherwise these two indices are its only
variables, by Lemma 2.1. For `|h|<=H`, the correction to `i+m` in (5.5)
has absolute value at most `R`.

Fold opposite pair indices into four-state variables

\[
              y_i=(x_i,x_{i+m})\in\{0,1\}^2,
                         \qquad i\in\mathbb Z_m.       \tag{5.6}
\]

Every window weight is now constant, unary in one `y_i`, or a two-variable
function whose folded indices have cyclic distance at most `R`. Sum the
corresponding constant, four-entry unary tables, and sixteen-entry pair
tables. This is a finite-range model on the `R`th power of a cycle, not a
generic large hypergraph. Omitted ranks remove tables and cannot enlarge
the interaction range. Pins restrict the allowed states of individual
four-state variables.

#### Dynamic Program

Fix the first `R` variables `y_0,...,y_(R-1)`; there are at most `4^R`
choices. Process the other variables in order, retaining their last `R`
values as the state. When setting `y_j`, charge its unary cost and all
pair factors whose larger ordinary index is `j`.

For a previously assigned neighbor `i<j`, either `j-i<=R`, so its value
is in the retained state, or the edge crosses the cyclic seam. In the
latter case `j-i>=m-R`, implying `i<R`; its value is among the fixed
initial variables. Thus every charged factor is known. Every factor is
charged exactly once.

There are at most `4^R` retained states and four extensions per state,
for each fixed initial assignment. Each extension evaluates `O(R)`
aggregated pair factors. This proves (5.4), and storing
predecessors reconstructs the actual orientation vector.

Each such dynamic program is a layered acyclic shortest-path graph.
Combine the initial-assignment branches at one source and sink. A
nonnegative unit flow is a convex combination of source-sink paths:
follow positive-flow arcs to the sink, subtract the minimum flow along
that path, and repeat. Acyclicity ensures termination, and flow
conservation ensures that a positive path can always be continued.
At least one path has cost no greater than the flow's average cost.
Its orientation vector gives the required literal row. QED.

This flow integrality is specific and proved. Adding the global
cross-row target-cover constraints to this network is not shown to
preserve integrality.

### Larger Consecutive Blocks

The same construction works for `n=2md` positions partitioned into
consecutive blocks of size `d`, with all `d!` orders allowed in each
block. A window depends only on its two boundary blocks. Fold opposite
blocks, giving `(d!)^2` states per folded variable and interaction radius

\[
                 R_d=\lceil H/d\rceil+1.
\]

When `R_d<m/2`, the same proof gives time

\[
 O\!\left(mR_d\bigl((d!)^2\bigr)^{2R_d+1}\right)
       +\operatorname{poly}(n,H)(d!)^4.               \tag{5.7}
\]

Here only the loss-allowing oracle is asserted; the exact Boolean
protection-face statement was for two-element blocks. Formula (5.7)
permits a controlled enlargement of the row neighborhood without
additional physical fragments.

## 6. Simultaneous Protected Rounding Across Rows

One cannot simply apply Theorem 3.1 to every row against the same old
list and update them all at once: two owners of a target could each rely
on the other. The following ownership construction removes that issue.

For every controlled target already covered, choose one of its current row witnesses
as its protected owner. In each row pin every pair split by a target
owned by that row. For integer caps, protect
`min(a(T),kappa(T))` distinct row witnesses instead of one. Such witnesses
exist by definition; each row contributes at most one occurrence.

Every simultaneous choice of the remaining bits preserves all protected
witnesses. Thus every old covered target remains covered, or, in the
capped version, every old attained cap remains attained.

For an old controlled hole `T`, let `J(T)` be the rows whose pinned-compatible
orientation families can contain it. In each such row, its unique form
depends on `d_i(T)` free bits, where `d_i(T)` is one or two. Define

\[
                  p_i(T)=2^{-d_i(T)}.
\]

### Theorem 6.1 (exact protected hole potential)

There is a deterministic simultaneous orientation choice, using the same
rows and the same physical budget, with weighted remaining old holes at
most

\[
 \boxed{\sum_{T\text{ old hole}}\omega(T)
                  \prod_{i\in J(T)}(1-p_i(T)).}        \tag{6.1}
\]

In particular a hole accessible in `r` rows has remaining probability at
most `(3/4)^r` in the underlying protected sampler.

#### Proof

Choose all unpinned row bits independently and uniformly. Within a row,
target occurrences have the one- or two-bit dependencies proved above.
For one fixed target, however, the events in different rows depend on
disjoint sets of bits. Its miss probability is therefore exactly the
product in (6.1). Sum over old holes; no old coverage is lost because
the assigned witnesses remain pinned.

Expose all free bits one at a time and choose the bit value minimizing
the conditional expectation of the remaining weighted hole count.
For each target and row, its conditional hit probability is zero if a
required bit has failed, or `2^(-r)` when `r` prescribed free bits remain.
The same product formula remains valid under this conditioning. Thus the
conditional expectations are explicitly computable and one of the two
choices is no greater than their average. The final integral choice
satisfies (6.1). Compile the resulting permutation rows by (1.3). QED.

This is a zero-load potential, not a quadratic proxy. Loads above one
are not penalized. Its starting object is an actual row family and actual
protected witnesses, not an arbitrary fractional cover.

## 7. The Density-Hole Interface

Use the relatively dense base dimensions `n=4m`, and set

\[
 H=\lceil\sqrt{n\log n}\rceil,\qquad
 t=\left\lfloor\frac{W(n)}{n+2H}\right\rfloor.
                                                               \tag{7.1}
\]

Then all hypotheses above hold eventually, `t>=1`, and every output of
these rounding operations is a nonempty literal word of length at most
`W(n)`. The full band is handled by one family, at no cost per Gaussian
depth or per bit.

For unit-weight zero loads, one complete sequential sweep of the exact
row oracle takes `2^{n+o(n)}` bit operations, including construction and
updating of the target-count dictionary. Indeed there are
`t=2^{n+o(n)}` rows, each oracle takes `2^{O(H)} poly(n)=2^{o(n)}` time,
and all counts have `O(n)` bits. Each update minimizes the actual
conditional designated zero count with all other rows fixed, so a sweep
cannot increase that count. This is a computational positive statement;
it does not bound the terminal number of holes.

If `Z` is its designated band zero count and `g` its actual nonempty hole
count, then

\[
                g\le Z+2^{n+1}e^{-2H^2/n}.             \tag{7.2}
\]

The binomial tail term is at most `2^(n+1)/n^2=o(2^n)`.

There is also a uniform converse error estimate. Every within-block
rank-`s` interval is a length-`s` source window, whose target is already
in the full cyclic deck. A crossing interval must end among the first
`s-ell+1` positions of its last block, because that prefix alone otherwise
has rank greater than `s`. Endpoint nesting therefore gives at most
`(t-1)(s-ell+1)` additional targets at rank `s`. Consequently

\[
 Z-(t-1)(2H+1)(H+1)\le g,
 \qquad \frac{tH^2}{2^n}=O(\log n/\sqrt n)=o(1).       \tag{7.3}
\]

Thus designated and actual hole densities differ by `o(1)` uniformly
over all row updates. An update need not preserve the undesignated
cross-block targets, and no such stronger claim is used.

The useful unconditional conclusion is that one can apply the positive
rounding of Sections 3--6 at this exact budget and retain the density-hole
interface throughout. If these updates yield `Z=o(2^n)`, the proved
cylinder completion then gives coefficient one, with extension

\[
 a=\lceil n(g/2^n)^{2/3}+\sqrt n\rceil=o(n)
\]

and exact completion cost

\[
                   2^a|B|+g(\nu(a)+1).
\]

The relative bound is `1+O((g/2^n)^(2/3)+n^(-1/2))`. Relatively dense
interpolation covers all dimensions. The implication is conditional on
actually obtaining the vanishing zero count, not on time-zero marginals.

## 8. Precise Unresolved Step

These lemmas give two legal positive mechanisms at the correct physical
scale:

- A no-loss update covers at least one quarter of its currently accessible
  useful-target weight, with an exact protected parallel counterpart.
- A loss-allowing update exactly minimizes the true conditional zero-load
  objective over an exponentially large row family, with a proved
  bounded-width flow rounding rather than a generic nibble promotion.

What is not proved is a lower bound on accessible holes for the families
generated by successive updates. The protection pins may leave no useful
free bits. Likewise, an exact optimum in each paired-row neighborhood
need not be the global optimum over all row lists.

One can change a row's pairing frame without changing its current cyclic
deck by rotating the source by one position before the next oracle call;
larger blocks give the further neighborhoods in (5.7). These are legal
ways to enlarge the search, but no theorem here says they maintain
augmentation until the remaining hole density is `o(1)`.

The needed further result is therefore a witness-reassignment/row-frame
availability theorem, or a proof that the loss-allowing row oracle's
terminal zero count is `o(2^n)`. This is a concrete geometric correlation
problem. It has not been replaced by a numerical codegree condition or
by an assumption that a matching residual is independent.

## 9. Checks

The dependency-free companion script is:

```sh
python3 scratch/gate_c_paired_row_zero_load_rounding_20260905_e9a61.py
```

It checks the unique-form classification, exact no-loss faces against all
orientation choices in small instances, quarter-weight augmentation,
the folded oracle against exhaustive minimization, complement symmetry,
literal compilation and joins, and a fixed-budget multirow improvement
experiment. The experiment is a construction check, not asymptotic
evidence sufficient for the missing availability theorem.

Observed checks:

- The no-loss characterization passed 640 exhaustive orientation tests,
  including varying integer caps.
- The folded oracle agreed with exhaustive minimization in 32 cases;
  augmentation, complements, compilation, and the join bound also passed.
- The protected parallel formula agreed with all 256 assignments in a
  three-row test. Its expected gain was `69/4`; conditional-expectation
  rounding produced gain 24 with no old coverage loss.
- The explicit 16-coordinate update increased designated band coverage
  from 80 to 136 at unchanged literal length 40.
- A 64-coordinate instance optimized over `2^32` paired-position row
  variants by the folded dynamic program and gained 78 zero-load targets.
- At `n=12,H=2`, 57 rows had literal length 912 against width 924. Twelve
  sequential sweeps, alternating the pairing frame by a one-position
  rotation, gave band-hole counts
  `1362,972,758,738,704,702,692,692,678,678,678,678,678`.
  The final actual word had 947 nonempty holes across all ranks.

The final finite residual is nonzero. These data establish that the
implemented rounding performs genuine fixed-cost correlated coverage
updates, not that its asymptotic residual tends to zero.
