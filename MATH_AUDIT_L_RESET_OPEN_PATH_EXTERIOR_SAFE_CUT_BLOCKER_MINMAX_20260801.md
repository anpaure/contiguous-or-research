# Independent audit of the opened-reset blocker theorem in the reversal quotient

**Date:** 2026-08-01  
**Lane:** L independent proof/scope replay  
**Verdict:** PASS with the scope stated in the audited theorem.  No finite
computation is used.

Audited file:

`MATH_THEOREM_L_RESET_OPEN_PATH_EXTERIOR_SAFE_CUT_BLOCKER_MINMAX_20260801.md`.

The scope rebase also imports
`MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`.
The current construction rebase additionally imports
`MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`.

## 1. Exterior blocker identity

Fix the undirected factor component containing the protected packet path,
an allowed cut bank `K`, and the complete bank of packet-avoiding old
witness arcs for each target `S`.  An arc survives a cut `c` exactly when
`c` is not one of its internal gaps.  Consequently all such witnesses of
`S` fail exactly on

\[
 B_S=K\cap\bigcap_{J\in W_S^{ext}}g(J),
\]

with `B_S=K` when the witness bank is empty.  Therefore the casualty count
at `c` is exactly

\[
 D(c)=\sum_S {\bf1}_{c\in B_S},
\]

and minimizing over `K` proves the theorem's formula.  A point has load at
least `b+1` exactly when it lies in an intersection of some `b+1` blocker
cores, proving the stated covering criterion.  Double counting the pairs
`(c,S)` proves the average bound.  These implications are reversible when
the witness banks are complete.

Reversing the whole complete state reflects the cut and each surviving arc;
its OR and its internal-gap set are unchanged.  Thus orientation correctly
drops out of this row.  A rooted matching decomposition, endpoint pair and
sidecar must be reflected with it.  A named one-sided socket remains real
unless its reflected socket is also admissible.

## 2. All-cut compensation payload

For the maximal antecedent, the frozen all-cut theorem says that every
width `w<=2d` interval value is injective in its start and width, has rank
`r-d+w-1`, and has no witness at another width.  Exactly `w-1` such intervals
cross a fixed cut.  Writing `t=w-1` gives exactly

\[
 t\text{ casualties of rank }r-d+t
 \quad(1\le t\le2d-1),
\]

and total

\[
 \sum_{t=1}^{2d-1}t=d(2d-1).
\]

Thus an empty ambient witness bank makes every corresponding blocker equal
to the full admissible cut bank, and the compensation optimum is exactly
`d(2d-1)`.  Seam choice and orientation cannot reduce it.  The theorem is
careful not to assert global absence: an ambient chronology may already
contain duplicate witnesses.

## 3. Audit of the canonical local payment

The `d` copied suffix cells give a word of length `M+d`, so applying `D^d`
produces exactly `M` windows.  They are the cyclic owner windows in rotated
order and hence are coefficient one.  Every crossing interval of source
width at most `d` is restored literally.  A longer interval contains a
rank-`r` owner, so no target below rank `r` can remain missing; every rank-`r`
target is one of the restored owner windows.

More precisely, in the old width-`w` casualty bank the overlap restores a
crossing witness whenever its left suffix has size at most `d`.  For
`d+2<=w<=2d`, the residual count is

\[
 \sum_{w=d+2}^{2d}(w-d-1)=\binom d2,
\]

with `t` masks of rank `r+t`, `1<=t<d`; these are exactly the corresponding
subtriangle of the `X`-gap leave and are paid by `P_X`.  The final `X` row
and the whole `U`-gap triangle require the full two-bank module when the
entire cyclic deck, rather than only the old guaranteed family, is protected.

The frozen deck classification leaves exactly the two nonempty contiguous-
gap families in `X` and `U`.  A gap with complementary size `t` has `t`
placements, giving `t` targets at ranks `r+t` and `r+d+t`.  Therefore the
two triangles have total size

\[
 2\sum_{t=1}^d t=d(d+1).
\]

The central-interval formulas on the `2d`- and `3d`-owner paths reproduce
these masks literally.  Four marker signatures separate both banks from
one another and from the packet at owner and q1 level.  Their internal run
classification is resident; the only deficiencies are the two nested
one-sided profiles covered by the displayed collars.

Consequently, when these protected paths stay contiguous and the external
cut avoids their interiors, each former packet casualty has a protected
bank witness.  Its blocker core is empty and the exact local compensation
value is `beta*=0`.  This does not contradict Section 2: the bare word and
the protected twin-bank module have different witness systems.

The cost statement is also scoped correctly.  The overlap uses exactly the
`M+d` source positions forced by `M` depth-`d` owners.  The repair consumes
`5d` raw, at most `7d` collared, reserved owner positions in a future
coefficient-one host.  Existence of those positions inside one globally
upper-complete chronology remains unproved.

## 4. Scope checks

1. The phase-common host is specialized to `r=m`, `k=2m-1`; `m>=8d+4`
   supplies the local coordinate inequalities.  Its common certificate is
   undirected q1 support only.
2. Whole-copy reversal transports every linear interval only when both
   exterior pieces are exchanged and reversed with the packet.  It is not a
   fixed-socket local switch.
3. Keeping the component cyclic preserves the cyclic deck but merely delays
   the compulsory opening ledger.
4. The rank-graded payload belongs to the maximal source antecedent.  It is
   not automatically an owner-word upper no-go.
5. Endpoint run ages are a separate residence test.  OR witnesses do not
   certify them.
6. In a fixed literal word, distinct target masks cannot use the same
   interval occurrence.  Before the word is fixed, one oriented child still
   requires its own occurrence-labelled compiler matching and nonempty cap.
   The opposite quotient representative receives their reflected addresses.
   Hall in the fixed-address intersection `G^+ intersection G^-` is needed
   only for a local switch against a frozen exterior, not for existential
   reversal-quotient induction.
7. Global reversal itself does not pay the opening debt, remove a hole, merge a
   component, or choose relative phases.  With `c` independently phased,
   individually labelled components, `c-1` phase bits survive.  If reversal
   permutes component labels, it still removes at most one simultaneous bit.
8. A degree-only rainbow completion is unavailable: the Wdowinski
   counterexamples cover the relevant `Delta+1` regime.  The fixed-`M0`
   Boolean lower/root--head--graphic correlation remains a joint condition;
   disjoint second-facet projection does not close it.

## 5. Exact quotient interface

The low-debt cut theorem composes with the global quotient precisely when
the induction state retains the full source and owner chronologies, complete
upper-witness bank, compiler/cap certificate, ordered endpoints and every
named guard/sidecar; reflects all occurrence addresses; swaps endpoint-age
records and any unordered fresh-coordinate pair; and satisfies state
closure, transition equivariance, orbit-totality and invariant charged debt.
Only one representative of each input orbit must extend.  A frozen right
socket, fixed physical compiler address, or selective packet flip is outside
this face.

Accordingly the proof-safe conclusion is exactly conditional: construct one
oriented child containing the packet and collared twin banks, preserve the
exterior blocker row, join the protected paths, and supply one terminal
compiler/cap; then reflect the completed tuple.  The bare packet still has a
quadratic cut debt, but the canonical protected module pays it locally.
