# An all-`k` pinning theorem and the limits of simple absorbers

This note continues `GLOBAL_PINNING.md`.  Its purpose is narrower: find a
pin-survival theorem that can be used inside a recursive, near-width ordered
chain construction, and determine which tempting simplifications are
mathematically impossible.

The main positive result is the **negative merge-forest theorem**.  It turns
pinning into a hierarchical certificate compatible in form with Catalan path
components: local negative pieces may be recursively merged into negative
roots, and separated roots leave the required clean cuts.  The main negative
results show that:

* laminarity without a rule for abutting pieces is insufficient;
* one coatom root per coordinate is impossible for every `k>=3`; and
* any universal array needs exponentially many coordinate-run components in
  total, so an `O(poly(k))` family of global absorber cuts cannot suffice.

All theorems below are proved.  The existence of a Catalan recursion satisfying
their hypotheses remains open.

## 1. Setup

For every nonempty mask `S subseteq [k]`, prescribe a distinct interval

\[
 I_S=[\ell(S),r(S)]\subseteq[n].                                    \tag{1.1}
\]

The ordered orthogonal-chain normal form supplies such cells, but Sections
1--4 need only the intervals and labels.  Fix a coordinate `b`.  Put

\[
 \mathcal N_b=\{I_S:b\notin S\},\qquad
 U_b=\bigcup\mathcal N_b,qquad Z_b=[n]\setminus U_b.                \tag{1.2}
\]

The bit survives exactly when every positive interval meets `Z_b`.

Call the system **containment-monotone** when

\[
 I_X\subseteq I_Y\quad\Longrightarrow\quad X\subseteq Y.           \tag{1.3}
\]

This is necessary for every actual interval-OR array, although it is not
implied by abstract orthogonality alone.

Two integer intervals are called **linked** if they overlap or abut.  Thus
`[a,c]` and `[c+1,d]` are linked: together they leave no legal integer point.

## 2. The component-root theorem

### Definition 1 (rooted negative component)

A connected component `C` of `U_b` is rooted if there is a negative assigned
mask `R_C` such that

\[
 I_{R_C}=C.                                                         \tag{2.1}
\]

It is enough to require `C subseteq I_(R_C) subseteq U_b`; equality then
follows because `C` is a maximal connected component of `U_b`.

### Theorem 2 (component-root pinning theorem)

If the assigned system is containment-monotone and every component of every
`U_b` is rooted, then all coordinates are pinnable.  The canonical maximal
factor

\[
 A_j=\bigcap_{S:j\in I_S}S                                          \tag{2.2}
\]

realizes every assigned mask.

#### Proof

Fix `b` and a positive mask `S`.  If `I_S` did not meet `Z_b`, then the
connected interval `I_S` would be contained in one component `C` of `U_b`.
By rootedness,

\[
 I_S\subseteq C=I_{R_C}.
\]

Containment monotonicity would give `S subseteq R_C`, impossible because
`b in S` and `b notin R_C`.  Thus every positive interval meets `Z_b`.
Doing this independently for every coordinate proves pin survival, and (2.2)
is the canonical maximal factor from the exact completion theorem.  QED.

The theorem is global in conclusion but local in what a recursion must
provide: one negative root for each connected barrier component.

## 3. A hierarchical certificate: the negative merge forest

Requiring the final components in advance is inconvenient in a recursive
construction.  The following certificate builds them by binary merges.

### Definition 3 (negative merge forest for `b`)

A negative merge forest is a rooted forest whose nodes are negative assigned
masks and which satisfies:

1. Every negative assigned interval occurs at a leaf or is contained in the
   interval of some leaf/node represented in the forest.
2. If a node `R` has children `X,Y`, then their intervals are linked and

   \[
      \operatorname{hull}(I_X\cup I_Y)\subseteq I_R.                \tag{3.1}
   \]

3. The intervals of distinct roots are separated by at least one integer
   position:

   \[
      r(R)+1<\ell(R')\quad\text{or}\quad r(R')+1<\ell(R).           \tag{3.2}
   \]

The definition permits a node to have more than two children by choosing any
binary bracketing.

### Theorem 4 (negative merge-forest theorem)

A containment-monotone assigned system is pinnable if, for every coordinate
`b`, it admits a negative merge forest.

#### Proof

Induction from the leaves shows that each node interval contains the connected
hull of all negative intervals below it.  Condition (3.2) says different root
intervals lie in different connected components.  Condition 1 says every
negative interval lies below a root.  Since every root is itself negative,
the root intervals are therefore exactly the connected components of `U_b`.
Theorem 2 applies.  QED.

### Corollary 5 (pairwise hull closure)

Suppose the system is containment-monotone and has this property for every
coordinate:

> whenever two negative assigned intervals are linked, some negative assigned
> interval contains their hull.

Then it is pinnable.

#### Proof

In each connected component, sort the negative intervals by left endpoint
and merge linked intervals successively using the assumed hull interval.
This constructs one merge tree per component.  Distinct components have a
missing integer position between them, so their roots satisfy (3.2).  Apply
Theorem 4.  QED.

### Corollary 6 (gapped laminar criterion)

If, for every `b`, the negative assigned intervals form a laminar family and
any two disjoint maximal members have at least one integer position between
them, then pinning follows from containment monotonicity.

#### Proof

Every connected component has a unique maximal negative interval.  It is its
root, so Theorem 2 applies.  QED.

Plain laminarity is not enough: the negative singleton intervals
`[1,1],[2,2],...,[h,h]` are pairwise disjoint and hence laminar, but together
they cover `[1,h]`.  The gap or merge requirement is essential.

## 4. A Catalan-block version

The merge theorem has a direct formulation for a recursive central skeleton.
Suppose an ordering is assembled from consecutive blocks

\[
 B_1\Vert B_2\Vert\cdots\Vert B_t,                                  \tag{4.1}
\]

for example the path components of a two-sided Catalan forest followed by
recursive bridge joins.

### Theorem 7 (recursive block-root criterion)

Assume containment monotonicity.  Pinning is guaranteed if, for every bit
`b`, the recursion supplies the following data.

1. Inside each leaf block, all negative intervals belonging to that block are
   dominated by one negative block-root interval.
2. Whenever two consecutive negative rooted blocks become linked after a
   bridge is inserted, the recursion designates a negative parent interval
   containing the hull of the two child roots.
3. At the end, distinct surviving negative roots have a clean integer
   separator between them.

#### Proof

The leaf roots and designated bridge parents are exactly a negative merge
forest.  Apply Theorem 4.  QED.

This is strong enough to serve as an all-`k` pinning lemma: it incurs no extra
array positions.  What remains is a combinatorial construction of the block
roots simultaneously for all coordinates.  In particular, a Catalan
linearization theorem should carry, at every component join, not only its two
middle-layer colours but also the negative-root signatures needed by item 2.

The condition is more realistic than demanding one global root per bit.  The
latter is impossible, as shown next.

## 5. A sharp obstruction to one-coatom rooting

The largest mask omitting coordinate `b` is the coatom

\[
 C_b=[k]\setminus\{b\}.
\]

A tempting construction rule is

\[
 I_S\subseteq I_{C_b}\qquad\text{whenever }b\notin S,               \tag{5.1}
\]

so that `I_(C_b)` is the unique negative root for `b`.

### Theorem 8 (coatom-root impossibility)

For `k>=3`, no pinnable interval system representing every singleton mask can
satisfy (5.1) simultaneously for all coordinates.

#### Proof

Write `J_b=I_(C_b)`.  For distinct `a,b`, the singleton `{a}` omits `b`, so

\[
 I_{\{a\}}\subseteq J_b.                                           \tag{5.2}
\]

But `{a}` contains coordinate `a`; under (5.1), the entire forbidden union
for `a` is `J_a`.  Pin survival therefore gives a point

\[
 x_a\in I_{\{a\}}\setminus J_a.
\]

By (5.2),

\[
 x_a\in\bigcap_{b\ne a}J_b\setminus J_a.                           \tag{5.3}
\]

Thus every interval `J_a` is essential in the following strong sense: the
intersection of all the other intervals contains a point outside `J_a`.

In a family of intervals, at most two members can be essential this way.  To
see this, write `J_a=[u_a,v_a]`.  A point in the intersection of the other
intervals but to the left of `J_a` can exist only if `u_a` is the unique
largest left endpoint.  A point to the right can exist only if `v_a` is the
unique smallest right endpoint.  There is at most one interval of each type.
For `k>=3`, (5.3) demands at least three essential intervals, a contradiction.
QED.

Therefore an all-`k` pinning proof must use multiple negative components or a
hierarchical merge structure.  A single coatom interval per coordinate cannot
be the missing theorem.

## 6. Interval-matrix integrality and the exact absorber min-max theorem

For a fixed `b`, compress the ordered left chains to their shortest positive
transition intervals

\[
 \mathcal J_b=\{[p,c_p(b)]:c_p(b)<+\infty\},                         \tag{6.1}
\]

and list the clean positions as

\[
 Z_b=\{z_1<z_2<\cdots<z_s\}.
\]

Each trace `J cap Z_b` is an interval in this ordered list of clean positions.

### Theorem 9 (integral absorber min-max theorem)

Assume every member of `mathcal J_b` has a nonempty clean trace.  Then

\[
 \min\{|P|:P\subseteq Z_b,\ P\cap J\ne\varnothing
                    \text{ for all }J\in\mathcal J_b\}
 =
 \max\{|\mathcal Q|:\mathcal Q\subseteq\mathcal J_b,
       \{Q\cap Z_b:Q\in\mathcal Q\}\text{ are pairwise disjoint}\}.
                                                                    \tag{6.2}
\]

Equivalently, the clean-position versus transition-interval incidence matrix
has the consecutive-ones property, its covering polyhedron is integral, and
the right-endpoint greedy algorithm returns an optimal absorber set.

#### Proof

Order the traces by increasing last clean point.  Greedily choose that last
point for the first unhit trace.  The traces that cause greedy choices are
pairwise disjoint: after choosing `z`, every remaining causing trace begins
strictly after `z`.  Hence the number of greedy points is at most the packing
maximum on the right of (6.2).  Conversely, any hitting set needs a different
point for every pairwise-disjoint trace, so its size is at least the packing
maximum.  Equality follows.  The same argument is the elementary integral
proof behind total unimodularity of interval matrices.  QED.

This theorem is useful after an ordering is proposed: it proves that no
fractional/integral gap remains in choosing sparse coordinate pins.  It also
clarifies the limitation of an LLL or nibble argument.  Integrality can choose
among clean positions, but it cannot create a clean position in a transition
interval whose negative barriers already cover it.

## 7. Exponential component complexity is unavoidable

The merge theorem must not be misread as saying that only a bounded number of
roots or absorber cuts are needed.

For an actual array, let `P_b subseteq[n]` be the positions containing bit
`b`, and let `rho_b` be the number of nonempty contiguous runs of `P_b`.  Put

\[
 R=\sum_{b=1}^k\rho_b.                                               \tag{7.1}
\]

### Theorem 10 (coordinate-run lower bound)

If the interval ORs realize all `2^k-1` nonzero masks, then

\[
 \boxed{R\ge \sqrt{2^k-1}-1}.                                       \tag{7.2}
\]

If zero is also realized, the slightly cleaner bound
`R>=sqrt(2^k)-1` holds.  The nonzero bound in (7.2) also holds for the total
number of clean-set components in the canonical maximal factor of any
pinnable witness assignment.

#### Proof

Write the runs of all coordinates as intervals `[u,v]`.  An array interval
`[p,q]` contains bit `b` exactly when, for at least one `b`-run,

\[
 p\le v\quad\text{and}\quad q\ge u.                                \tag{7.3}
\]

Across all runs there are at most `R` threshold values of type `v` on the
`p`-axis and at most `R` threshold values of type `u` on the `q`-axis.  They
partition the `(p,q)` plane into at most `(R+1)^2` regions, and every interval
whose endpoint pair lies in one region has the same `k`-bit OR signature.
Therefore the number of distinct interval ORs is at most `(R+1)^2`.  Covering
all `2^k-1` nonzero masks forces (7.2); covering zero as well gives the stated
strengthening.  Applying the same argument to the canonical clean-position
sets `Z_b` proves the second statement.  QED.

If `c_b` is the number of connected components of the forbidden union `U_b`,
then `Z_b` has at most `c_b+1` components.  Hence any pinnable universal
assignment satisfies

\[
 \sum_{b=1}^k c_b\ge \sqrt{2^k-1}-1-k.                              \tag{7.4}
\]

### Consequences

1. A proof using `O(poly(k))` total coordinate absorbers or negative roots is
   impossible.
2. One-pin-per-coordinate and one-root-per-coordinate schemes fail by an
   information bound even before Theorem 8's sharper interval obstruction.
3. A Catalan-scale hierarchy is not ruled out.  For `k=2m`, the number of
   Catalan components is

   \[
      \operatorname{Cat}_m
      =\Theta\!\left(\frac{2^k}{k^{3/2}}\right),                    \tag{7.5}
   \]

   which is exponentially larger than the necessary scale `2^(k/2)` in
   (7.2).  Thus Catalan recursion has enough combinatorial entropy; the
   difficulty is coordinating its roots across all bits, not their raw count.

## 8. Bandwidth alone cannot prove pinning

The rank-slack argument puts lower witnesses in intervals of length at most
`d`.  This geometric fact by itself gives no clean cut.

### Proposition 11 (bounded-length barriers can percolate arbitrarily far)

For every `d>=1` and every `h`, an interval of length `h` can be covered by
negative intervals of length at most `d`, even with overlap multiplicity one
when `d=1`.

#### Proof

For `d=1`, use the `h` negative singleton intervals.  For general `d`, split
the target interval into consecutive blocks of length at most `d`.  QED.

Thus neither small delay, low overlap, laminarity, nor a bounded local
dependency degree is sufficient for an LLL-style argument.  A successful
probabilistic proof must control the probability of an entire negative bridge,
not merely individual interval conflicts.

## 9. What an all-`k` Catalan pinning proof must establish

The proved results isolate a concrete theorem target.

Let a two-sided Catalan skeleton be linearized into ordered path blocks and
bridges.  To obtain pin survival without adding length, it is enough to prove:

### Catalan negative-root target (open)

For every coordinate `b`, the negative intervals internal to the path blocks
can be assigned negative roots, and the bridge recursion can merge every pair
of linked roots into a negative parent, until the surviving roots are
separated by clean positions; simultaneously the selected interval system is
containment-monotone.

Theorem 7 would then prove all coordinate pins at once.  Theorem 9 would
produce canonical sparse pins, and the resulting array entries would be
obtained by stacking the independently selected bit pins.

The obstructions delimit what is required:

* roots must be hierarchical rather than one coatom per bit (Theorem 8);
* their total complexity must be exponential (Theorem 10);
* adjacent negative blocks must be merged or deliberately separated
  (Proposition 11 and Corollary 6); and
* a local merge certificate is enough—one does not need to inspect every
  positive mask once containment monotonicity is present (Theorem 4).

This is a substantially more specific mathematical task than “solve the pin
SAT instance.”  It asks for a recursive negative merge forest carried by the
same Catalan joins that linearize the two-sided middle-layer skeleton.
