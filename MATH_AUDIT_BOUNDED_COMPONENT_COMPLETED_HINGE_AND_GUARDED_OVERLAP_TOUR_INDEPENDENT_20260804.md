# Independent audit: completed hinges and guarded overlap tours

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_BOUNDED_COMPONENT_COMPLETED_HINGE_AND_GUARDED_OVERLAP_TOUR_20260804.md`  
**Audited theorem SHA256:**
`3b8087d7e2fd1bb219d536db0f8e184b10548571546a53171cf6d39455c8f8de`  
**Verdict:** **GO**, relative to the theorem's explicit product-separable
connector atlas and jointly completed-hinge hypotheses.  The history
distance, weighted-tour formula, zero-cost head-permutation criterion,
common-core characterization, sharp obstructions, and bounded terminal
charge all check.

No search, solver, or finite computational enumeration is used.

## 1. Exact order-`d` history distance

After `s<d` shifts, an order-`d` history retains exactly its final `d-s`
letters.  Therefore a transition from `u` to `v` in `s` appended letters
requires

\[
 \operatorname{suffix}_{d-s}(u)
 =\operatorname{prefix}_{d-s}(v).
\]

The largest possible retained part has length `ov(u,v)`, so

\[
                         s\ge d-\operatorname{ov}(u,v).
\]

Appending the unmatched suffix of `v` attains the bound.  Lemma 1.1 and
the inequality `gamma>=delta_d` are correct.  The latter is only a lower
bound because a shortest history path may fail residence, witness, cap, or
compiler guards.

## 2. Weighted overlap-tour formula

Once a cut `p_i` is fixed in each directed component, every allowed linear
splice induces a unique order of the retained component bodies.  It pays
the sum of the opening charges and at least the minimum declared connector
charge between each consecutive pair.  This proves the lower bound in
(2.1).

Conversely, cuts, an order, and minimizing connector macros construct the
concatenated path.  The product-separability assumption is exactly what is
needed to add their charges and infer joint physical legality.  Adding the
last-to-first connector gives the cyclic formula.  Thus Theorem 2.1 is
exact relative to the declared atlas.

The qualifier cannot be removed.  Two individually legal connector macros
may consume one common capacity-one resource; then their scalar costs do
not compose.  The theorem and Proposition 5.3 explicitly preserve this
boundary.

Corollary 2.2 follows by choosing the certified Hamilton path: it has at
most `C-1` joins.  If the component count is `Theta(d)`, even unit cost per
join gives `Theta(d)`, so the stated warning is necessary.

## 3. Completed-hinge component permutation

Remove the selected occurrence-labelled packet

\[
                         a_i\longrightarrow h_i
\]

from component `C_i`.  Its retained body is a directed path from `h_i` to
`a_i`.  Replacing the removed packet by

\[
                         a_i\longrightarrow h_{\pi(i)}
\]

makes the next component encountered after `C_i` equal to `C_(pi(i))`.
Hence the output components are in bijection with the permutation cycles of
`pi`.  They form one factor cycle exactly when `pi` is one cycle.

The directed compatibility graph records precisely whether each replacement
belongs to the role's completed rectangle.  Therefore one-cycle fusion using
the fixed tails and heads is equivalent to a directed Hamilton cycle in
that graph.

The simultaneous legality clause is load-bearing and is present: mutable
resources are private by role and shared ledgers depend only on the
multiset of tails and heads.  A head permutation preserves that multiset.
Without this joint completion condition, individual rectangles would not
prove simultaneous fusion.

For Corollary 3.3, take a nonempty proper union `S` of current permutation
cycles.  If no cross pair permits the mutual head exchange, every ordered
pair in `S times ([c]-S)` fails at least one of the two menu tests.  The
number of first failures is

\[
 \sum_{i\in S}|([c]-S)-M_i|,
\]

and the number of second failures is

\[
 \sum_{j\notin S}|S-M_j|.
\]

Thus `mathcal D(S)>=|S|(c-|S|)`, contrary to (3.6).  A legal two-switch
between different cycles merges them, and the fixed menus permit iteration.
This verifies the zero-cost cut-expansion certificate.

## 4. Minimal complete regenerative history state

For `0<=K<=d`, `delta_d(u_i,v_j)<=K` is equivalent to equality of the
length-`d-K` suffix of `u_i` and prefix of `v_j`.  If this holds for every
ordered exit--entry pair, fixing either index shows that all these words
are one common core `R`.  Conversely, that common core supplies overlap
`d-K` for every pair.  Theorem 4.1 is exact.

The conclusion is deliberately for a complete all-pairs router.  A single
chosen Hamilton path may use different long overlaps at different joins;
the weighted tour is then the weaker exact formulation.

The nonhistory state in Definition 4.2 cannot be omitted.  Proposition 5.2
gives a minimal logical separation: two ports can have identical histories
but lie in distinct invariant cap-flag classes, making guarded connector
cost infinite.

## 5. Sharp component-count obstruction

For distinct source letters `x,y`, no nonempty suffix of `x^d` is a prefix
of `y^d`.  Hence each directed bare transition has distance `d`.  A linear
two-component splice needs one such transition and costs at least `d`; a
cyclic splice needs both directions and costs at least `2d`.

This validates the sharp claim that even two components do not imply a
constant sidecar.  It also identifies the needed regenerative invariant:
an actual literal overlap of length `d-O(1)`, or a zero-cost completed hinge
which avoids adding a reset path.

## 6. Compiler and terminal accounting

The final-state complete damage set contains every reference matching edge
which ceases to be literal.  Deleting those matching edges, and the edges
whose cells are reused by `h` new tasks, loses at most `b+h` old targets.
The new task cells are pairwise distinct and avoid the damage bank, so their
edges may be inserted simultaneously.  This is exactly the bounded-eviction
lemma.

Appending the casualty masks and a repair word for the remaining hole
family destroys no old witness.  Adding the initial excess `s` and fusion
charge `Gamma` proves

\[
 \nu(k)\le B(k)+s+\Gamma+b+h+R(H).
\]

No compiler is required to persist through intermediate hinges or pulls;
only the final damage accounting is used.  Conversely, marginal cell
legality without a complete damage set would not justify the bound, and the
theorem does not make that inference.

## 7. Final scope and verdict

Combining the bounded pull rescue with this theorem gives a valid
additive-constant implication only after one proves one of:

1. a jointly completed hinge family whose component graph has a directed
   Hamilton cycle; or
2. a product-separable guarded overlap tour of bounded **total** charge.

For `p=O(d)`, bounded per-join charge is insufficient unless almost every
join is zero-cost.  Full carrier guards and bounded final compiler/target
damage remain separate premises.

All theorem directions and quantitative constants check.  The precise
regenerative state is the long literal overlap core together with the full
guard boundary signature; bounded component count alone is not that state.
