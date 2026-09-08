# Copy-before-erase for the residual first connector

**Date:** 2026-08-06  
**Method:** the fixed-head visible cart, a private bounded reservoir, and the
proved first-clock component router; no search or computation  
**Status:** proposed closure, pending independent audit together with the
three-row collar record.  It addresses the sole residual left when the first
connector is excluded from the bulk complement pass.

## 1. The residual is a bounded extreme bank

Write the first connector as `C(a_1)`, and let `C(a)|C(b)` be the fixed head
collar.  Put `epsilon(c)=c-1`.  Centrality gives

\[
 \sum_i\epsilon(a_i)=0.
\tag{1.1}
\]

After deleting the first connector and the two fixed collar connectors, the
work tape has imbalance

\[
 -\bigl(\epsilon(a_1)+\epsilon(a)+\epsilon(b)\bigr).
\tag{1.2}
\]

The noncrossing marked-corridor pass complements all balanced pairs and leaves
exactly the absolute value of (1.2) unmatched extremes, all of one type.  Thus
there are at most three residual work connectors.  Their ordered occurrences
are recovered by the deterministic cancellation stack.  Complementing this
bounded bank, the fixed collar, and the first connector pays exactly zero net
mass, as required by (1.1).

## 2. Ordering the information transfers

Retain the fixed double head and the three-row collar record `R_(a,b)` from
the copy-before-erase collar theorem.  Also reserve a bounded private work
reservoir of capacity at least twelve.

When the residual bank is nonempty, perform the following operations in
order.

1. **Write the remote target first.**  Keep the first clock in its current
   unordered row and keep `R_(a,b)` fixed.  Use the fixed-head visible cart to
   locate its at most three unmatched work connectors.  In their deterministic
   order, use simple paths inside the work component to change those
   connectors, the `G_1` coordinate of the first connector, and all other
   still-unwritten work coordinates to their target values.  Put the resulting
   bounded mass discrepancy in the private reservoir.  The work-component mass
   is fixed during each path, so the first clock only toggles inside its
   unordered row.
2. **Retire the head.**  Keep the row record fixed and use the prepaid
   teardown collar to replace the double head by
   `C^*(a)|C^*(b)`.  The literal target collar now records `(a,b)`; the
   completed residual bank and (1.2) record `a_1`.
3. **Write the first clock last.**  Hold the target collar and residual target
   bank fixed.  Release the residual reservoir through the component-mass ladder,
   route the first clock to its required target row and endpoint, and align the
   root flag.  The aperture-retirement theorem then writes the exact boundary
   predecessor and takes its final root edge.
4. Retire the three-row collar record.  Its information is now duplicated in
   the literal target collar.

If the residual bank is empty, omit step 1 and use the same head retirement
and clock collar.

## 3. Exact labelled conclusion

### Conditional Theorem 3.1 (residual first-connector handoff)

Assume the copy-before-erase collar theorem, the fixed-head visible-cart
theorem, and an occurrence-labelled version of the bounded reservoir/component
route in step 1.  Then the four-stage schedule above gives a directed
occurrence-labelled path from every flagged source state to the exact
complemented target state.  Paths for different sources are pairwise
vertex-disjoint and avoid the old promotion/aperture linkage.

#### Proof

Before the head is retired, the pair

\[
                    (R_{a,b},\ \hbox{fixed head berth})
\tag{3.1}
\]

recovers the excluded collar, while the marked tape and cancellation stack
recover every other source connector and the bounded residual occurrences.
Thus the deterministic work-component path in step 1 is source- and
stage-decodable.  It is disjoint from the first clock, so its selected row is
unchanged.  The double-head transport atom labels every active local window.

After step 1, the residual target bank is fixed.  After step 2, the literal
target collar is fixed as well.  These pieces retain all information which the
clock row record is about to lose: the target collar identifies `(a,b)`, and
the signed residual count together with (1.2) identifies `a_1` (including the
empty-bank case).  Consequently the mass-ladder route in step 3 remains
source-decodable even while it changes the first selected row.

The component router proves reachability of the requested work, reservoir,
clock, and root configuration.  Choosing one deterministic simple route for
each decoded source makes its literal state determine the microstep.  The
non-one root flag, or its already audited root-one/boundary-one intermediate,
separates every nonterminal state from the old linkage.  Finally the
aperture-retirement collar and root exit are already occurrence-injective.
Hence equality of two route states forces equality of source, stage, and
microstep.  \(\square\)

The extra occurrence-labelled reservoir premise is load-bearing.  Choosing a
deterministic simple path separately for every decoded source does not by
itself make the resulting family disjoint: two such paths may meet after their
source labels have been overwritten.  The scalar component router proves
reachability, not this joint path-bank assertion.

## 4. Consequence

Together with the marked-corridor/LIFO theorem and a literal
copy-before-erase collar, Conditional Theorem 3.1 would remove the last
bounded odd connector charge.  At present the common missing row is the
bounded occurrence-labelled register/reservoir path bank, so the odd
quiet-source counterflow package remains open.
