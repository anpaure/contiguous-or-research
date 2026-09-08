# Independent audit: serial one-phase terminal reduction and passive types

**Date:** 2026-08-04  
**Method:** pure-mathematical audit; no computation, search, or solver  
**Primary theorem audited:**
`MATH_THEOREM_PASSIVE_TERMINAL_TYPE_ELIMINATION_AND_DIRECT_IBC_ICA_CLOSURE_20260804.md`  
**Companion synthesis audited:**
`MATH_THEOREM_SERIAL_ONE_PHASE_FORCED_RAY_TERMINAL_REDUCTION_20260804.md`  
**Verdict:** `GO` as exact conditional reductions.  Passive terminal
acceptance and the opposite packet phase can both be removed from a final
direct-ray readout.  One global terminal antecedent and its guard-pruned
residual Hall inequalities remain indispensable.

## 1. Quantifier audit

The serial-safe theorem permits a sequence

\[
                         T^{(0)}\to\cdots\to T^{(s)}
\]

in which no intermediate lower compiler exists.  It preserves the owner
set, safe topology, residence, and upper interval-union deck.  Therefore a
final proof is allowed to:

1. choose one terminal endpoint of the last `P/Q` packet edge;
2. construct one antecedent for that endpoint only; and
3. solve the lower compiler only in that endpoint word.

There is no logical need to intersect the phase-`P` and phase-`Q` compiler
graphs.  In particular, the pointwise union of the separately constructed
antecedents need not be an exact antecedent and need not support a common
matching.

This does not say that two phases may be mixed inside one terminal word.
The final word uses exactly one phase and one state.

## 2. Direct-ray audit

For one fixed phase the aligned theorem supplies the values

\[
 J+x_\epsilon+P_j,qquad J+y_\epsilon+S_j,qquad1\le j<d,
\]

at pairwise distinct physical interval addresses.  Within each family the
filler support is strictly nested, while the two families have different
active labels.  Hence these are `2(d-1)` distinct target rows and distinct
cell columns: a literal partial matching.

They are strict-lower targets.  Since `|K|=r-d-4` and `|J|=r-d-2`, their
ranks are respectively

\[
                         r-d-1+j,qquad r-j-1,
\]

both at most `r-2` for `1<=j<d`.

Consequently the direct-ray Corollary 3.2 of the passive-type theorem is
sound provided “solve the complementary target/cell problem” means:

> solve it in the exact occurrence graph of the same global antecedent, or
> in a guard-pruned Cartesian bank proved to realize one common word.

Ordinary marginal Hall before pin/trace pruning would not suffice.

## 3. Forced-edge and fact-coalescence audit

Let `Pi` be any forced target/cell facts carried by a complete deterministic
bundle, and let `B_*` be its remaining noncoalescible occurrence footprint.
After identical address/value/state facts are coalesced, a full matching
exists exactly when the graph obtained by deleting

\[
       L(\Pi),\qquad C(\Pi),\qquad B_*
\]

has a matching saturating the residual target shore.  This is ordinary
forced-edge contraction.  Coalescence is sound because one interval address
has one literal OR value; attaching its own ordinary witness role does not
create another physical occurrence.

The reduction does not make native routes free.  If a native route is kept
for compensation, topology, or a later interface, all route interiors and
exclusive occurrences remain in `B_*`.  If it serves only to encode the
ray targets, it may be omitted and the exact ray occurrences used directly.

## 4. Ideal-pin audit

The largest prefix ray lies in one first-block owner window and the largest
suffix ray lies in one second-block owner window.  Thus all prefix targets
can occupy `d-1` distinct ideal slots of the first owner and all suffix
targets `d-1` distinct ideal slots of the second.  This is a legal ideal
partial matching of size `2(d-1)`.

The arbitrary-ideal-pins theorem extends it whenever

\[
       2(d-1)\le(d+1-\Lambda/W)(k-r+1),
\]

which holds for all sufficiently large `k` because the right side is
`Theta(k)` and `d=Theta(sqrt(k))`.

This proves only that containment and ideal owner capacity are not the
obstruction.  It does not choose nested chains, physical endpoints, one
source prefix, or a guard word.

## 5. Exact remaining Hall row

After fixing the ray pins, form the pinned envelope

\[
 E_p^\Pi=E_p\cap\bigcap_{(S,C)\in\Pi:p\in C}S.
\]

One must find a globally nonempty antecedent `A` which realizes every owner
row and every pin equality.  In its exact occurrence graph the residual
deficiency is

\[
 \delta(A,\Pi)=
 \max_{X\subseteq L\setminus L(\Pi)}
       (|X|-|N_{H_A^\Pi}(X)|)_+.
\]

Equivalently, relative to a marginal pinned graph `G^Pi`, if `ell_A(X)` is
the neighbor loss under all trace and guard pruning and
`sigma_G(X)=|N_G(X)|-|X|`, then

\[
                   \delta(A,\Pi)\le C
 \iff
                   \ell_A(X)\le\sigma_G(X)+C
 \quad\text{for every }X.
\]

This is the exact physical gate left after the ideal theorem.  It combines:

1. prefix-realizable physical chainization;
2. nonempty source and owner traces;
3. ray-pin traces and residence-frontier guards; and
4. Hall after all those incidences have been pruned.

Neither fact coalescence nor ideal Hall proves this row.

## 6. Passive versus active type

The passive-type theorem is correct at final readout.  A cut/polarity label
which is determined by one already selected complete physical record, adds
no literal or capacity constraint, and has no future consumer may be
adjoined or erased conservatively.

Typing remains necessary in either of two circumstances.

1. A routing theorem chooses among alternative terminals.  Two crossed
   routes `s_1->t_2`, `s_2->t_1` give a full untyped linkage but no linkage
   to prescribed terminal types `t_1,t_2`.
2. A later inductive transition distinguishes phase, polarity, endpoint, or
   guard labels.  Erasing the label can identify two states with different
   continuation sets.

The direct-ray terminal theorem avoids both: target identities stay at
their literal ray occurrences and there is no downstream transition.  A
regenerative proof may also avoid active types if its next lift is proved to
factor through the type-free physical record; otherwise it must retain and
verify them.

## 7. Scope corrections to retain when citing the passive theorem

The passive theorem is `GO` with four explicit qualifications.

1. Its aligned antecedent is locally constructed; a final all-`k` use still
   needs a compatible **global** antecedent of the whole carrier.
2. Internal bundle disjointness does not imply disjointness or compatibility
   with the complementary background.
3. “Complementary matching” means a same-word or completely guard-certified
   matching, not marginal Hall in individually sound cells.
4. No common phase state or regenerative continuation is constructed.

These qualifications are already consistent with the theorem's status and
frontier sections.  No unconditional `B(k)+O(1)` conclusion follows from
the semantic reduction alone.

