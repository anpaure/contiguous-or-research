# Audit of the full hook envelope and three-dimer obstruction

**Date:** 2026-08-06  
**Audited source:**
`MATH_THEOREM_PBBS_FULL_HOOK_ENVELOPE_TOKEN_SLIDE_AND_THREE_DIMER_OBSTRUCTION_20260806.md`  
**Method:** independent symbolic replay of the leaf offsets, envelope
update, no-wrap inequality, forced-dimer order, and largest-gap cost; no
computation or search  
**Verdict:** **PASS.**  The target
`{0,-1,-4,-5,-8,-9}` has no native single-hook interval ticket for every
odd `n>=13` once `d>=6`.  Therefore the proposed all-low hook-interval
Hall theorem is false.  The positive parity-compatible run construction
and its eventual largest-gap budget bound are also correct.

## 1. Envelope replay

The `i`-th free leaf in slot `c_i` occurs at offset `c_i+2i`.  Allowing
`c_i=p`, rather than stopping at `p-1`, extends the previously audited
zero-terminal formula verbatim.  The last `z` such offsets are

\[
 n-2z,n-2z+2,\ldots,n-2,
\]

so the first terminal leaf is exactly the known exit deletion `q-2z`.
The envelope update removes this exit and inserts the next entrance root
`q-2z-1`.  Hence

\[
 P_{i+1}=P_i-\{q_i-2z_i\}+\{q_i-2z_i-1\}
\]

and the union of selected envelopes is exactly `P_0` plus the later
selected roots.  No new independent filler bank appears at later times.

## 2. Monotonicity replay

For `ell<=d` and total terminal mass at most `b`, the lifted displacement
is

\[
 2\sum z_i+\ell\le2b+d=2m-d-2<2m+1=n.
\]

Thus the path cannot wrap and all inserted roots occur in strict cyclic
order.

## 3. Forced dimers

For a maximal dimer `{a,a-1}`, independence forbids both coordinates in
`P_0`.  If the lower coordinate is absent from `P_0`, its only possible
appearance is as an inserted root, forcing predecessor token `a`.  If the
lower coordinate is in `P_0`, the upper coordinate would have to be an
inserted root with predecessor `a+1`, contradicting maximality.  Thus the
transition `a -> a-1` is forced.

After this transition the root is `a-1`.  Continuing to the next pure
dimer forces its top as the next departing token.  The required jump is
`2z`, so its cyclic distance must be even.  Strict no-wrap order forbids
skipping a dimer.  Hence every odd outgoing dimer must be terminal, and at
most one can occur.

For the displayed target the first two outgoing distances are both three.
This is an exact contradiction, independent of the mass budget or number
of hook components.

## 4. Positive cost replay

For `r` nontrivial runs of total size `A`,

\[
 \sum D_j=n-A+r.
\]

If all bridged distances are even, the constructed word uses
`ell=A-r+1` cells and cost

\[
 Z=(n-A+r-D_*)/2.
\]

The inequality `Z<=b` is exactly

\[
 D_*\ge2d+3-A+r.
\]

For the largest gap,

\[
 D_*\ge2(n-d)/d=(16/\pi+o(1))d,
\]

whereas `A>=2r` makes the required right side at most `2d+2`.  The
eventual largest-gap claim therefore has a strict linear margin.

## 5. Scope

The obstruction is confined to one contiguous interval on one native
height-`d+1` hook component.  It does not obstruct:

* another PBBS action partition;
* a protected seam between two hook intervals;
* a parity-changing local packet; or
* the general `B(k)+O(1)` conjecture.

It does show that component multiplicity cannot repair the present Hall
graph: the obstructed targets have empty neighbourhoods.
