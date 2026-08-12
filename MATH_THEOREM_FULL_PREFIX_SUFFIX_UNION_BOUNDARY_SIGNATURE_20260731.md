# Full prefix/suffix-union signatures and arbitrary-width upper preservation

Date: 2026-07-31  
Lane: root, protected-upper compression interface  
Status: exact replacement theorem and exact scope audit.  The typed/topological
condition used by the current buffered-hex route is insufficient and must be
upgraded for arbitrary-width upper preservation.  Packet abundance under the
upgraded signature remains open.

## 0. Verdict

For a finite word `X=(x_1,...,x_h)` of bit masks, define its full OR-boundary
signature

\[
 \Sigma_\vee(X)=
 \left(h;(P_j(X))_{j=0}^{h};(S_j(X))_{j=0}^{h}\right),          \tag{0.1}
\]

where

\[
 P_j(X)=\bigvee_{i=1}^{j}x_i,\qquad
 S_j(X)=\bigvee_{i=h-j+1}^{h}x_i,\qquad P_0=S_0=0.              \tag{0.2}
\]

For a coordinate `z`, let `f_X(z)` and `l_X(z)` be its first and last
occurrence positions in `X`, using `infinity` and `-infinity` when absent.
Then

\[
 z\in P_j(X)\iff f_X(z)\le j,\qquad
 z\in S_j(X)\iff l_X(z)\ge h-j+1.                               \tag{0.3}
\]

Hence two equal-length slots have the same full signature iff

\[
                  f_X(z)=f_{X'}(z),\qquad l_X(z)=l_{X'}(z)       \tag{0.4}
\]

for every coordinate `z`.  This **endpoint-time characterization** is a
compact proof-safe representation: one first/last occurrence pair per
coordinate reconstructs both monotone sequences exactly.

If a fixed slot `X` is replaced by `X'` with
`Sigma_vee(X)=Sigma_vee(X')`, then every contiguous interval which meets the
exterior of the slot has exactly the same OR after replacement under the
natural endpoint correspondence.  The assertion is simultaneous over all
interval widths.  Only intervals wholly internal to the slot can change.

Thus an `O(D)`-long packet with an identical full signature reduces the
arbitrary-width protected-upper audit to its internal `O(D)` support.  It
does not reduce the number of internal interval labels below `O(D^2)`, and it
does not help if the replaced slot itself has unbounded length.

The specific buffered-hex composition condition currently records the same
typed boundary state, component connectivity, endpoint type, and (in the
fixed-skeleton version) typed ports/local connectivity.  It does **not**
require (0.1).  That condition is sufficient for topology but not for
contiguous-OR upper transport.  The protected-upper theorem therefore needs
the new explicit predicate `OR-boundary-equivalent`.  This is a scope
correction to that buffered route, not a claim that every repository use of
“boundary signature” is weak; some later packet notes already carry literal
boundary words or full halos.

## 1. One-slot replacement theorem

Let

\[
                         W=L\,X\,R,\qquad W'=L\,X'\,R            \tag{1.1}
\]

with `|X|=|X'|=h`.  Identify exterior positions literally and identify the
`j`th position of `X` with the `j`th position of `X'`.

### Theorem 1.1 (full-signature crossing preservation)

If `Sigma_vee(X)=Sigma_vee(X')`, every interval of `W` which is not wholly
contained in the interior slot `X` has the same OR as its corresponding
interval in `W'`.

#### Proof

Intervals disjoint from the slot are unchanged.  Every interval meeting both
the left exterior and the slot has the form

\[
                 L[i..|L|],X[1..j]
\]

or continues through all of `X` into a prefix of `R`.  Its OR is respectively

\[
 \operatorname{OR}(L[i..|L|])\vee P_j(X)                         \tag{1.2}
\]

or

\[
 \operatorname{OR}(L[i..|L|])\vee P_h(X)
             \vee\operatorname{OR}(R[1..k]).                     \tag{1.3}
\]

Equations (0.1)--(0.2) make these expressions identical for `X'`.  The
right-exterior case is symmetric and uses `S_j(X)`.  These cases exhaust all
intervals not wholly internal to the slot.  \(\square\)

### Corollary 1.2 (disjoint packet bank)

Replace pairwise-disjoint fixed slots `X_1,...,X_t` by equal-length slots
`X'_1,...,X'_t` with `Sigma_vee(X_i)=Sigma_vee(X'_i)` for every `i`.  Then
every interval which is not wholly contained in any single replaced slot
preserves its OR.

#### Proof

Apply Theorem 1.1 one slot at a time.  An interval crossing several slots is
a suffix of the first slot, all intervening slot totals and fixed gaps, and a
prefix of the last slot.  Every factor is preserved by (0.1).  \(\square\)

For a cyclic chronology, fix the opening and physical address map and take
every active slot nonwrapping.  A wraparound interval contributes the same
terms, including `S_a(X) vee P_b(X)` when the opening representation meets a
slot from both sides.  If the opening moves, its prefix/suffix correction
belongs to the exceptional endpoint ledger; equality of local signatures
does not authenticate a reroot.

## 2. Internal windows are the exact residual

Full boundary equality does not force internal equality.  For example,

\[
                         X=(1,2,1),\qquad X'=(1,3,1)              \tag{2.1}
\]

have identical prefix and suffix OR sequences

\[
                         (0,1,3,3),                              \tag{2.2}
\]

but their middle singleton intervals have OR `2` and `3`.  This proves that
the residual internal audit cannot be omitted.

If every slot has length at most `cD+c_0`, every changed interval is supported
inside one `O(D)` slot.  Consequently:

1. arbitrary-width crossing witnesses are transported exactly by the
   signature;
2. all remaining upper effects are local to `O(D)` physical support, but may
   comprise `Theta(D^2)` internal interval occurrences; and
3. a packet must still certify every internal upper row, residence row, and
   compiler/cap consequence of that local change.

The signature is therefore the missing **compression interface**, not a
packet-existence theorem.

## 3. Why the old typed boundary state is insufficient

The buffered-hex composition condition says that the replacement has the
same typed boundary state as the old piece, preserving component connectivity
and endpoint type.  The fixed-backbone version similarly fixes typed ports
and the local connectivity relation.  Neither clause records `P_j,S_j`.

There is already a literal Johnson-path counterexample.  On ground set
`{1,2,3,4,5}`, take the two rank-two paths

\[
 X=(12,13,34),\qquad X'=(12,24,34),                              \tag{3.1}
\]

where `ij` abbreviates `{i,j}`.  The two slots have the same length, literal
endpoints, rank profile, Johnson-path connectivity relation, and total union
`1234`.  Yet

\[
                          P_2(X)=123\ne124=P_2(X').              \tag{3.2}
\]

Prepend the fixed rank-two owner `15`, which is Johnson-adjacent to the common
left endpoint `12`.  The crossing interval consisting of that exterior owner
and the first two slot owners has union `1235` before replacement and `1245`
after it.  Hence typed/topological boundary equivalence, even augmented by
equal length, literal endpoints, and equal total union, is not enough.

### Definition 3.1 (OR-boundary-equivalent packet)

A packet replacement is **OR-boundary-equivalent through its declared slot**
when:

1. it is topologically boundary-equivalent in the existing sense;
2. its slot length and fixed opening/position map agree with the off-state;
3. its complete sequences `(P_j)_(j=0)^h,(S_j)_(j=0)^h` equal those of the
   off-state; and
4. every internal interval whose OR may change is included in the packet's
   guarded upper ledger.

The sequences are taken on the actual physical chronology row in every
relevant phase.  Owner-level equality alone is insufficient if a compiler
expansion changes the physical position map.

Condition 3 can be stored as the endpoint-time table (0.4), equivalently as
the strict-increment chains with their first attainment indices.  Equality of
only the unordered prefix/suffix OR sets is insufficient for a width-indexed
compiler.  Literal sequence, or endpoint-time, equality is the proof-safe
interface.

## 4. Consequences for the two buffered routes

### Route A

In the guard-complete bounded-seam lift, require every whole-collar option to
be OR-boundary-equivalent through an `O(D)` slot.  Theorem 1.1 then removes
all arbitrary-width crossing intervals from the seam ledger.  The exact task
contains only its internal `O(D)` window support, plus complete cap/topology
tickets.  This supplies the previously missing logical implication

\[
 \text{full prefix/suffix signature}
   \Longrightarrow\text{protected-upper span }D.                \tag{4.1}
\]

What remains open is uniform `Omega(m^2)` supply of such options at every
reachable compound task and their cap/topology compatibility.

### Route B

The same signature removes crossing-upper conflicts from the protected row
energy of a dispersed reservoir.  Only internal slot windows can contribute
to its upper part, but there may be `Theta(D^2)` of them and the signature
alone does **not** prove an `O(Dm^3)` energy bound.  Prescribed-task
eligibility, a separate internal protected-row energy estimate,
positive-density OR-boundary-equivalent lifting, and complete cap/topology
row energy remain open; the raw C6 average-load extraction does not prove
them.

## 5. Exact scope

Proved here:

1. full prefix/suffix OR-sequence equality is sufficient for all-width
   crossing preservation;
2. the residual is exactly the family of internal slot intervals;
3. typed/topological boundary equivalence is strictly insufficient; and
4. with `O(D)` slot length, the upper residual has `O(D)` physical support,
   not necessarily an `O(D)`-sized row ledger or local ticket bank.

Not proved here:

1. that current ECO/C6 menus contain a positive density of
   OR-boundary-equivalent packets;
2. that their internal upper ledgers pass;
3. that complete cap/topology tickets have the needed conflict energy; or
4. that the resulting state regenerates in all dimensions.

## 6. Dependencies

* `MATH_THEOREM_BUFFERED_HEXAGON_LLL_REDUCTION_AND_MISSING_LOAD_GATE_20260731.md`;
* `MATH_THEOREM_AD_BUFFERED_HEX_GLOBAL_COMPOSITION_HAXELL_AND_BOUNDED_SIDECAR_20260731.md`;
* `MATH_THEOREM_AD_RSB_DEPTH2_EROSION_DELTA_REGENERATION_GUARDS_20260731.md`;
* `MATH_SYNTHESIS_BUFFERED_C6_TWO_ROUTE_O1_20260731.md`.
