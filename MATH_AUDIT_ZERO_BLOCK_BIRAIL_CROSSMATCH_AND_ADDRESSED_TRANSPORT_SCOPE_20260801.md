# Audit of zero-block birail collapse, folded-C8 cross tickets, and full-block transport

Date: 2026-08-01  
Lane: independent proof/scope audit  
Status: `GO` for the abstract zero-block theorem, its repetition bounds, and
the cross-matching criterion.  The folded antidiagonals are only paired
cross-phase occurrence tickets.  Full-block background transport is exact
under the explicit target-deletion, side-cell, guard, and cap hypotheses
below.  Host planting and regenerative closure remain open.

## 0. Verdict

The three files are mathematically consistent after four scope corrections.

1. The identity `delta(pi)=t(pi)` is correct for nonnegative **integer**
   thresholds with simple positive multiplicities.  The robust bounds with
   repetition excess, and with deletion of exceptional paired indices, are
   also correct.
2. For the canonical four equal blocks, zero defect is equivalent to the two
   cross subgraphs having perfect matchings.  This is an abstract pairing
   theorem; it does not create addressed compiler cells.
3. A folded antidiagonal edge is a pair of separately addressed ray
   assignments, normally in opposite phases.  Collapsing it to one
   right-hand cell undercounts **cell consumption** by a factor of two and
   mixes endpoint states.
4. Full-block lifting removes the residual background Hall test only after
   the old matching is restricted away from the targets reassigned to private
   side cells, every lifted cell remains guard/deadline admissible, and the
   packet cap is contraction-exact.  It does not plant the typed host or make
   the refinement length-neutral.

The current zero-block theorem already contains most of these qualifications.
Its opening status sentence should say that background transport is not
proved **unconditionally**; Section 3.1 does prove it conditionally on an
actual admissible typed full-block host.

## 1. Simple-positive collapse

Let the two shores carry nonnegative integer thresholds `x_i,y_j`, let `pi`
be a full pairing, and put

\[
 C_\pi(a,c)=\#\{i:x_i\le a,\ y_{\pi(i)}\le c\},\qquad
 \delta(\pi)=\max_{a,c\ge0}(C_\pi(a,c)-a-c)_+,                 \tag{1.1}
\]

and

\[
 t(\pi)=\#\{i:x_i=0,\ y_{\pi(i)}=0\}.                         \tag{1.2}
\]

Assume every positive threshold occurs at most once on each shore.

### Theorem 1.1

For every pairing,

\[
                              \delta(\pi)=t(\pi).              \tag{1.3}
\]

#### Proof

The corner `(0,0)` gives `delta(pi)>=t(pi)`.  At any corner `(a,c)`, remove
the `t(pi)` zero--zero pairs.  Charge every remaining counted pair to its
positive left threshold when it has one, and otherwise to its positive right
threshold.  A positive left threshold is charged at most once and there are
at most `a` possible positive integer values not exceeding `a`; similarly
there are at most `c` usable right values.  Hence

\[
                         C_\pi(a,c)\le t(\pi)+a+c,              \tag{1.4}
\]

which proves the reverse inequality.  \(\square\)

The integer-threshold hypothesis is load-bearing for the estimate "at most
`a` distinct positive values below `a`."  It is satisfied by the canonical
birail thresholds.  The statement is not a theorem for arbitrary real-valued
thresholds without replacing `a,c` by the corresponding support-count
functions.

### Repetition bound

If

\[
 e_L=\sum_{s\ge1}(\mu_L(s)-1)_+,
 \qquad
 e_R=\sum_{s\ge1}(\mu_R(s)-1)_+,                              \tag{1.5}
\]

then at a corner `(a,c)` there are at most `a+e_L` positive left tickets and
at most `c+e_R` positive right tickets.  The same charging proof gives

\[
                 t(\pi)\le\delta(\pi)
                    \le t(\pi)+e_L+e_R.                        \tag{1.6}
\]

If deleting a set `E` of at most `e` paired indices makes both positive
marginals simple, apply (1.4) to the undeleted pairs and charge every deleted
pair directly to `E`.  Since the undeleted zero--zero count is at most the
original `t(pi)`, this yields

\[
                         \delta(\pi)\le t(\pi)+e.               \tag{1.7}
\]

This proves exactly the stated deletion formulation.  Merely changing `e`
numeric marginal entries, without naming paired exceptional indices, does
not imply (1.7).

## 2. Exact cross-matching criterion

Let a bipartite allowed-pair graph have shores

\[
 L=L_0\dot\cup L_+,qquad R=R_0\dot\cup R_+,qquad
 |L_0|=|L_+|=|R_0|=|R_+|=m.                                  \tag{2.1}
\]

By Theorem 1.1, a perfect pairing has zero defect exactly when it avoids
`L_0 x R_0`.  In such a pairing, all `m` vertices of `L_0` must use all `m`
vertices of `R_+`; the remaining vertices are exactly `L_+,R_0`.
Consequently

\[
 \boxed{
 \delta=0\text{ is attainable}
 \iff H[L_0,R_+]\text{ and }H[L_+,R_0]
      \text{ both have perfect matchings}.}                    \tag{2.2}
\]

The union of the two cross matchings proves the converse.  If `H` has any
perfect matching, assigning cost one to `L_0R_0` and zero elsewhere makes
the exact abstract birail defect the minimum-cost perfect-matching value.
This part of the zero-block theorem is complete.

## 3. Folded antidiagonals are paired cross-phase tickets

For `1<=j<d`, the folded ray addresses are

\[
\begin{array}{c|c}
 P_0(j)&[1,j]\text{ in }G_0\\
 S_1(j+1)&[j+1,d]\text{ in }G_1\\
 P_1(j)&[1,j]\text{ in }G_1\\
 S_0(j+1)&[j+1,d]\text{ in }G_0.
\end{array}                                                   \tag{3.1}
\]

Thus each abstract edge

\[
 P_0(j)\leftrightarrow S_1(j+1)
 \quad\text{or}\quad
 P_1(j)\leftrightarrow S_0(j+1)                               \tag{3.2}
\]

specifies **two** disjoint adjacent interval occurrences.  The occurrences
are in opposite phase words.  Their common intersection/union algebra is a
useful cap label, but it does not identify the two physical addresses and
does not turn them into one capacity-one compiler cell.

A physical realization of a cross matching therefore needs one of the
following.

1. Two disjoint addressed cell banks in a single compatible endpoint state,
   with every abstract ticket expanded into two assignments; or
2. an address isomorphism between the endpoint states which transports a
   complete matching, together with separately forced assignments for both
   coordinates of each ticket.

In the second formulation each selected ticket contributes two edges to the
mandatory new bank `F^+`.  Pull both cells back through `Phi`; the resulting
forced old edges must themselves be a partial matching and must pass the
residual Hall inequalities.  The threshold cross-matching theorem alone
does none of this.

The phrase "undercounts physical capacity by two" is best replaced by
"undercounts required physical cell consumption by a factor of two."  The
former can be read as claiming that collapsing two cells makes less capacity
available, whereas the actual error is pretending that one cell can perform
two assignments.

## 4. Address transport and its finite scope

The addressed-occurrence theorem proves, for the explicit screened family
and `2<=d<=12`, equality of every fibre

\[
  (\text{width},\text{literal OR core},\text{interval common cap}).   \tag{4.1}
\]

Lexicographic pairing within each fibre is therefore a bijection of **all**
physical interval addresses.  On the unguarded one-core face it is an
isomorphism of the target--cell graphs.  This is stronger than signed-value
equality and really does transport a named old matching without collisions.

Its scope is nevertheless finite and typed:

* the explicit fibre equality is audited only through `d=12`;
* the pointwise cap candidate must belong to one legal complete cap state;
* any address-specific guard must be included in the fibre key or checked
  edge by edge;
* owner legality and both `q1` sidecars remain separate; and
* the address bijection does not realize an arbitrary threshold-ticket
  permutation.

The dimension-free part is the tautological fibre criterion and the screen
recycling lemma, not the explicit all-`d` folded fibre equality.

## 5. Full-block background transport: exact safe form

Suppose an old letter is replaced by a consecutive nonempty block with the
same total union.  Map an old interval to the expanded interval containing
every piece of each old letter it met.  This **full-block lift** is injective
and preserves the literal interval OR.

Let `M` be an old target-to-cell matching, and let `F^+` be a bank of new ray
assignments.  The no-residual-Hall conclusion is valid under all of the
following hypotheses.

1. The targets and cells used by `F^+` are separately distinct and every
   displayed assignment is legal in one complete cap/guard state.
2. Every cell used by `F^+` is a side cell outside the full-block image.
3. Every lifted old matching cell remains deadline- and guard-admissible.
4. The old matching is restricted to `L minus I`, where `I` is the set of
   targets reassigned by `F^+`.

Then

\[
 F^+\ \cup\ \Phi_{\rm full}
     \bigl(M\upharpoonright(L\setminus I)\bigr)                 \tag{5.1}
\]

is a collision-free complete matching.  Both its target banks and its cell
banks are disjoint.  Omitting the restriction `M|(L-I)` would assign every
ray-served target twice, so the statement cannot literally use the whole old
matching unchanged.

For the common-`Q` source equations one also needs phase-common piece caps
inside the old letter and blockwise contraction exactness

\[
                          \bigcup_jK^P_{p,j}=A_p.                 \tag{5.2}
\]

Under (5.2), every full-block background row reconstructs automatically.
Pointwise containment of the new pieces in `A_p` is weaker than (5.2).

For the canonical two-host refinement

\[
 X_L\mapsto(X_L,L_\epsilon),\qquad
 X_R\mapsto(R_\epsilon,X_R),                                   \tag{5.3}
\]

the ray occurrences are private side cells and the block unions contract to
`X_L,X_R`.  Hence there is no separate ambient Hall gate **conditional on**
literal owner-legal placement of those old host letters, admissibility of all
full-block lifts, and one compatible source-cap state.  The remaining rows
are host geometry/residence, typed `q1` sidecars, deadlines, screen halo, and
regenerative contraction.

Refinement (5.3) adds source pieces unless those positions were already
allocated or later contracted.  Full-block transport is not a proof of
`chi=0`.  The separate immediate-left screen-recycling theorem has
zero length charge because it reuses an existing unchanged ambient letter;
even there, zero length is not zero cap or guard footprint.

## 6. Forced-edge fallback

When a packet return occupies the transported bank, a guard deletes some
full-block cells, or the host is not a genuine refinement, pull every
mandatory new assignment `(T_i,b_i)` back through the global address
isomorphism:

\[
                         a_i=\Phi^{-1}(b_i).                     \tag{6.1}
\]

After verifying that the pulled-back edges are legal and form a partial
matching, delete their target set `I` and cell set `A`.  They extend to a
complete matching exactly when

\[
 |N_{H^- -A}(Y)|\ge |Y|
                \qquad\text{for every }Y\subseteq L\setminus I. \tag{6.2}
\]

Relative to a named old matching this is equivalently a full family of
vertex-disjoint alternating paths from the newly exposed target shore to the
free-cell shore.  Cap-state compatibility must be fixed before applying
(6.2); feasible cap options do not in general form a matroid.

## 7. File and handoff consistency snapshot

At the time of this audit, the current theorem SHA-256 values are

```text
67fe4a13635252e9d53e348903ab8c2e6c8a2c4216c2bbaebd156f35bc22ae49
  MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md
69b3469d2148820a260bb5564dd0e7f6418b142cba2a4c3554bfd92060ce3f0d
  MATH_THEOREM_R_FOLDED_C8_ADDRESSED_OCCURRENCE_BIJECTION_AND_ZERO_CHARGE_SCREEN_20260801.md
4255a729724ea60d8512ac027e848a20ddae87f0b3bc657581efc0574cf821c7
  MATH_THEOREM_R_FOLDED_C8_ADDRESSED_TRANSPORT_FORCED_EDGE_HALL_AND_COMMON_CAP_GATE_20260801.md
```

The zero-block SHA agrees exactly with `MATHEMATICAL_HANDOFF.md` item
`2428ROOT` and with its `RESEARCH_INDEX.md` entry.

The address replay artefacts also agree with the hashes quoted in the R
transport theorem:

```text
247e4aa93100dd6d7d4c282daf6e2183e4ca95c70049aa0cefc807d72bf24dcc
  scratch/audit_r_folded_c8_address_bijection_and_screen_recycling_20260801.py
c7c99e1cf57ec490bd3a7136349d047a06fa6af249c1a65363cb639a26bf4cd3
  scratch/r_folded_c8_address_bijection_and_screen_recycling_20260801.audit.json
payload 8ee79f497d8ae1951dd28d16b61dfa0d7a4b5fa15e9cae455dd28df5ddf21368
```

The two newly named R theorem files are not yet listed under their own names
in either `MATHEMATICAL_HANDOFF.md` or `RESEARCH_INDEX.md`.  Handoff item
`2430R` records the earlier addressed-return/sidecar theorem with SHA
`e2ae857f...`; it must not be cited as the freeze record for the two newer
files above.  This is an indexing omission, not a contradictory hash.

There is also one rendering typo in the forced-edge theorem's equation
(3.5): a stray carriage-return control character appears inside
`{\rm compatible}`.  It has no mathematical effect but should be normalized
when that file is next frozen; doing so will change its SHA.

## 8. Proof-safe synthesis

The combined result is

\[
 \boxed{
 \begin{array}{c}
 \text{the abstract birail defect is only the zero--zero count;}\\
 \text{zero defect is two cross matchings;}\\
 \text{each cross edge expands to two addressed assignments;}\\
 \text{an actual contraction-exact full-block host transports the background;}\\
 \text{host legality, sidecars, guards, and reset remain open.}
 \end{array}}
\]

No `B(k)+O(1)` or exact all-`k` conclusion follows yet.

