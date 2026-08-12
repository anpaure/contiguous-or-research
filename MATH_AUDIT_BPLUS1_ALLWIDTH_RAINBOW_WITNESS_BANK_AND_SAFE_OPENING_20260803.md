# Self-audit: all-width rainbow witness bank and safe opening

**Date:** 2026-08-03  
**Audited file:**
`MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`  
**Method:** independent symbolic audit.  No computation is used.

## 0. Verdict

**GO at the stated retained-witness and fixed-factor scopes.**

The safe-cut condition is necessary and sufficient.  The rainbow-bank plus
component-omission Hall condition is necessary and sufficient for the
stronger strategy in which every higher witness is retained inside the
upper-exact forest.  The note explicitly does not claim that every final
Hamilton path must arise through that strategy.

## 1. Retained-channel audit

An old interval remains a consecutive old-owner path precisely when none of
its internal old edges is deleted.  Selecting one survivor per target and
taking their union proves the quantifier exchange.  New-seam deliveries are
correctly kept separate, so the retained criterion is not overclaimed as a
necessary condition for the final deck.

The transversal number gives the exact uniform deletion radius.  On a
linear old path, interval piercing equals disjoint interval packing.  The
theorem correctly leaves a cyclic witness family in its exact circular-arc
transversal form, where equality with packing need not hold.  The `4z+1`
octagon bound is only a strong support-size corollary and is labelled as
such.

## 2. Safe-opening audit

A cyclic witness survives a cut iff its edge interval avoids the cut.
Intersecting all witness intervals gives the exact forced core.  A q1 colour
survives deletion of one occurrence iff it has another occurrence.  Avoiding
the pivot, belonging to the duplicate-provider bank, and avoiding every
higher core are therefore jointly necessary and sufficient.

The full-ground target is correctly excluded: the whole opened Hamilton
path witnesses it regardless of the cut.  The compatible-block description
of a core follows from intersection of intervals.  Two different cyclic
blocks have disjoint internal edge sets, so their common core is empty.

## 3. Rainbow-bank audit

An upper-exact representative set contains one physical edge per immediate-
upper colour.  Any witness bank inside it must therefore use at most one
edge of each colour.  Conversely a rainbow bank can be extended independently
colour by colour to one representative of every unused colour.  This proves
the equivalence without a hidden matching assumption.

For a fixed rainbow bank, colour `R` has at least `b_R=mu_R-1` deletable
occurrences outside the bank.  A representative subset of a directed cycle
cover is a forest iff its deletion complement meets every old cycle.  The
designation of one deletion per cycle is exactly a capacitated bipartite
matching from cycles to colours, giving the stated Hall inequalities.
After designation, the colour quotas extend independently.  This verifies
both directions of the component-omission theorem.

On one Hamilton cycle, total deletion capacity is `W-U=Cat_m>0`.  Every
positive-capacity colour has an unprotected occurrence because the bank is
rainbow.  Hence the single component cut is automatic.

## 4. Connector and switch audit

Adding ordered connector edges deletes no `Q_0` edge, so every selected
witness remains.  The component-port theorem supplies topology separately.
If a later switch deletes a protected witness edge, palette equality alone
does not save the corresponding higher target; it must have another retained
old witness or an explicitly checked new witness.  Formula (6.1) is exactly
that disjunction.

The stronger rainbow-bank chain is necessary only within the internal-
witness strategy.  A general Hamilton path may create cross-component
witnesses, and the theorem says so.

## 5. Pivot and global scope audit

Under `X subseteq A_-1 union A_1`, every crossing old source interval gains
only a redundant letter, while one-sided intervals are unchanged.  Thus the
pivot preserves every already certified upper witness at every width.

No theorem here constructs the rainbow witness selector, the protected
rooted factor, the connector Hall reservoir, a source antecedent, residence,
balanced named lower flags, or a common cap.  Accordingly the file proves an
exact all-width interface, not `nu(k)<=B(k)+1`.
