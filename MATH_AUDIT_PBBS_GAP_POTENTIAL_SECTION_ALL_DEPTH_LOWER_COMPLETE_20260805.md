# Audit of the PBBS gap-potential all-depth lower section

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_GAP_POTENTIAL_SECTION_ALL_DEPTH_LOWER_COMPLETE_20260805.md`  
**Method:** adversarial line-by-line symbolic replay; no computation

## Verdict

The one-sided fixed-factor theorem is proof-safe.

The decisive restriction statement is exact.  If a rank-`(m-q)` target
uses the global-maximum corridor boundary `A_0,C_0`, then the first q1 core

\[
 K_0=S+\{C_0,\ldots,C_{q-2}\}
\]

has forward survivors `A_0,A_1,A_2` and reverse survivors
`C_(q-1),C_q,C_(q+1)`.  The induced six-symbol word has potential values,
after normalizing at `C_(q-1)`,

\[
                         0,-1,\le-1.               \tag{0.1}
\]

Thus the fixed q1 gap-potential rule chooses the fan's first edge.  This
closes the common-section quantifier: the q1 rule is defined once from each
rank-`(m-1)` core, while the target fan is used only to prove that the
already-defined rule contains a witness.

## 1. Checks of the induced order

Write `d=2q+1`.  The backward corridor inequality `y_2<=2` means that
`A_1,A_2` occur in the last three `C`-gaps before `C_0`; the earliest
possible gap begins at

\[
                         C_{d-3}=C_{2q-2}.          \tag{1.1}
\]

For `q>=2`, this is not earlier than `C_q`.  Hence the open gap
`C_(q-1),C_q` has no retained `A`.  For `q>=3`, (1.1) is not earlier
than `C_(q+1)`, so the next open gap also has none.  At `q=2`, only
`A_2` can lie in the next gap.  Therefore the first induced gap has size
zero and the sum of the first two has size at most one, proving (0.1).

At a shared coordinate the expansion is `C_x,A_x`.  Thus equality at the
left endpoint of a gap places the `A` after that `C`, exactly as the proof
requires; it cannot move an `A` into the preceding open gap.  The selected
boundary itself is never a shared coordinate because its symbol order is
`A,C`.

The `q=1` case is the definition of the section, using the corridor theorem
with three symbols of each type.  The `q=2` edge case is covered by the
one-possible-`A_2` calculation above.  No separate asymptotic or generic
position hypothesis is used.

## 2. Quantifier and collision checks

For every q1 core `K`, the section first fixes one start `sigma(K)`.  For a
deeper target `S`, the corridor constructs a core `K_0(S)` and proves

\[
                         \sigma(K_0(S))=B_0(S).    \tag{2.1}
\]

It does not redefine the section.

If two rank-`(m-q)` targets `S,S'` produced the same core, then (2.1)
would give the same selected start.  Its deterministic depth-`q`
intersection has one value, so `S=S'`.  Thus the proof automatically
contains the fixed-depth injection required by Hall.

If targets at different depths reuse one core, their values are the
corresponding intersections of one deterministic future tower.  They are
therefore compatible rather than competing choices.  This is exactly why
one root occurrence suffices at all depths.

The construction uses no coordinate conjugate, randomization, or
rotation-equivariant choice.  A least-coordinate tie rule is allowed, so
the known obstruction to rotation-equivariant sections is irrelevant.

## 3. Ledger check

There are exactly

\[
                         M=N_1={2m+1\choose m-1}
\]

selected starts.  Full support at depth `q` gives `D_q=N_q`.  If `G_q`
is correct occurrence mass, then

\[
 G_q\ge N_q,
 \qquad
 E_q=G_q-D_q=G_q-N_q,
\]

so the forced repeat floor is the same number and

\[
                         \widetilde E_q=0.         \tag{3.1}
\]

Also `b_q=M-G_q<=N_1-N_q`.  For `q>=2`, subtracting the zero-hole
identity at consecutive depths gives

\[
 (b_q-b_{q-1})+(E_q-E_{q-1})=N_{q-1}-N_q.         \tag{3.2}
\]

The restriction `q>=2` is necessary because the selected family is not a
full depth-zero middle-owner deck.  The theorem states that restriction.

## 4. Compiler and upper-phase scope

For fixed `(X,q)`, the cyclic interval occurrence is named by its start
and depth.  Since PBBS component lengths are at least `2m+1` and
`q<=m`, two different pairs `(X,q)` cannot denote the same cyclic interval
cell.  Surjectivity at every depth therefore gives an integral occurrence
SDR simply by choosing one preimage per target.

This does not say those cells survive opening or Ferrers deletion.  It is
an SDR in the uncut PBBS intersection deck only.

Finally, the selected family has `N_1<W` starts, so it cannot cover the
`W` rank-`(m+1)` q1 upper targets by itself.  Hence no tie rule can make
the thinned lower section alone two-sided complete.  A valid two-sided
construction must retain or rebuild a separate owner/upper bank.  This is
consistent with, and sharper than, merely saying the shifted phase remains
open.
