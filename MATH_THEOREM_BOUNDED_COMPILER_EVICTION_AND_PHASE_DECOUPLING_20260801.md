# Bounded compiler eviction and terminal-phase decoupling

Date: 2026-08-01  
Status: exact implication for the additive-constant problem.  It replaces
zero-defect terminal U5 by a bounded literal damage certificate.  It does
not construct the required tickets or prove that their total damage is
bounded in a Pascal child.

## 1. Exact bounded eviction

Fix one **final** legal cap state and physical word.  Let `L` be the old
lower targets and `C` the physical compiler cells.  Write `H` for the
bipartite realization graph: `S-c` is an edge exactly when cell `c` has
literal union `S` in this final word.  Let `M_0` be a matching saturating
all targets in `L` in a reference state.

Suppose a selected packet bank introduces hard tasks
`tau_1,...,tau_h`, together with pairwise-distinct certified cells
`b_1,...,b_h`.  Let `D subset C` be a **complete damage set**: every edge
of `M_0` whose literal realization fails in the final packet state has its
cell in `D`.  Assume

1. every `tau_i-b_i` is a literal edge of the final realization graph;
2. `b_i notin D` for every `i`; and
3. the cells `b_i` are pairwise distinct.

### Theorem 1.1 (bounded-eviction lemma)

There is a matching which covers every task `tau_i` and every old target
except at most

\[
             |D\cap C(M_0)|+h                            \tag{1.1}
\]

old targets.  More sharply, the exact casualty set is contained in the old
targets matched by `M_0` to `D union {b_1,...,b_h}`.

#### Proof

Delete from `M_0` every edge whose cell lies in
`D union {b_1,...,b_h}`.  Every retained edge is still a literal edge by
the definition of the complete damage set.  Add all `tau_i-b_i`.  Their
cells are distinct, avoid `D`, and no retained old edge uses them, so the
result is a matching.  Only the deleted old edges are casualties, proving
(1.1).  \(\square\)

No Hall calculation is present because all interactions have already been
priced in the complete literal damage set.  This qualification is
essential.  A cell which is legal for one packet in isolation is not a
ticket: adding its target to a common-cap assignment can shrink source
letters and invalidate remote matched cells.  Those cells must appear in
`D` before Theorem 1.1 applies.

### Corollary 1.2 (terminal repair)

If the rest of a length-`B(k)+s` physicalization is complete, then

\[
 \nu(k)\le B(k)+s+|D\cap C(M_0)|+h.                  \tag{1.2}
\]

#### Proof

Apply Theorem 1.1, and append each casualty mask as one literal letter.
Appending destroys no existing witness.  \(\square\)

Thus exact U5 deficiency zero is stronger than necessary for
`B(k)+O(1)`.  What is required is a uniform bound on the number of
**matched** cells in the complete damage set, not a perfect matching after
every packet phase.

## 2. Regenerative sidecar form

Let a carried sidecar be a set `S` of unresolved literal target identities.
Suppose an odd-to-odd transition, given `|S|<=c`, chooses its packet bank and
final cap state so that

* all tasks induced by `S` and the transition receive certified cells;
* the complete packet damage set meets at most `c-h` other matched cells,
  where `h` is the number of genuinely new certified task cells which were
  formerly occupied; and
* the resulting casualty identities form the next sidecar `S'`.

Then Theorem 1.1 gives `|S'|<=c`.  This is a bounded invariant state, not an
additive recurrence.  At the requested terminal dimension, Corollary 1.2
pays `|S'|` once.

The inequality must bound the **total output sidecar**, including debt
inherited from `S`.  A statement which creates `c` new casualties in
addition to the old `c` gives linear accumulation and does not imply an
additive constant.

## 3. Terminal-phase decoupling

The bounded-spine theorem distinguishes an auxiliary state carried to the
next dimension from the terminal physicalization used only at the current
dimension.  This gives the following exact weakening.

### Theorem 3.1 (phase-decoupling principle)

Suppose a bounded two-phase sidecar has:

1. a minus phase carrying precisely the declared auxiliary signature used
   by the next Pascal transition;
2. a plus phase from which the current terminal word is physically compiled;
3. a legal odd successor constructed from the minus signature; and
4. a terminal plus-state charge at most `C` after bounded eviction.

Then no terminal common-cap assignment has to survive the minus-to-plus
toggle.  The minus and plus phases may use different compiler matchings and
different cap states.  Likewise, an upper-witness identity need be common
to both phases only when that identity is explicitly part of the carried
auxiliary signature.

If the same four conditions hold uniformly along one odd spine and for its
even terminal children, then

\[
                         \nu(k)\le B(k)+C             \tag{3.1}
\]

in every subsequent dimension.

#### Proof

The transition relation reads only the declared minus-phase auxiliary
signature.  Compile and repair the plus phase independently at the current
dimension.  Terminal compiler choices are not inputs to the next
transition, so their change creates no carried debt.  Move to the legal odd
successor and repeat.  The terminal charge is paid separately in each
requested dimension and never added to a later word length.  This is exactly
the bounded-cost odd-spine theorem.  \(\square\)

For the collared Boolean-hex sidecar, immediate lower/upper/tail/head
resources are phase-common and residence is phase-safe by the long-rail
theorem.  Theorem 3.1 removes the need for a **phase-common** terminal
compiler.  It does not prove that the plus phase has bounded compiler
damage, nor that the minus and plus states separately possess whatever
upper-provider data their respective roles require.

## 4. Corrected pull--cell reduction

A regenerative pull--cell lemma sufficient for `B(k)+O(1)` may therefore
use the following weaker U5 row:

> Each selected packet carries one literal task cell and its complete
> damage set; the union of those damage sets meets only `O(1)` cells of one
> reference compiler matching, and the output casualty identities form the
> next bounded sidecar.

This row is strictly weaker than demanding a zero-defect packet-preserving
perfect matching.  It is also strictly stronger than marginal cell
legality.  The current mixed-coatom packet theorem proves neither the
complete-damage bound nor the claimed quadratic full-ticket menu for every
prescribed action.  The best audited prescribed-action menu is only linear,
and some endpoint-breaker actions have no proved action-invisible menu.

Consequently bounded eviction sharpens the missing theorem but does not
close it.

