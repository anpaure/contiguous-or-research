# K17 `P*`: complete fresh-ticket host-menu no-go and the exact replacement interface

**Date:** 2026-08-02  
**Status:** exact finite theorem on the frozen planted `K17` object.  The
canonical fresh-ticket menu is exhausted before any endpoint-packing or
chronology constraint is imposed.  The current inverse parent, fixed outer
matching, and fixed `1,748`-short shore admit no complete phase-specific
ticket bank in either s7 owner phase.  This is a scoped obstruction to the
current host, not an all-`k` obstruction and not a lower bound on the size of
a carried regenerative state.

## 1. Frozen object and the two independent phase axes

Let

* `P*` be the inverse parent;
* `T` be the planted target table
  `constructed_common_basis_b5_host.tsv`;
* `mu` be `phase0_outer_matching.tsv`, the exact matching from `P*` to `T`;
* `S` be the `1,748` short rows in
  `regenerated_selected_tickets.tsv`; and
* `Omega^0,Omega^1` be the two owner maps
  `round047.s7.phase0.tsv` and `round047.s7.phase1.tsv`.

Both s7 phases in this note use the **same target table `T`** and the same
matching `mu`; only the owner map changes.  The alternate local B5 child
`phase1_child.tsv` is a different axis and is not substituted into the
phase-one census below.

Every row of `S` has target chain `L subset R` of length two.  Every legal
long endpoint in `T` is either one of the `16,898` identity-core hard rows
or one of the `17` fixed-soft rows.  Hence the lower used at a hard receiver
`h` is the actual lower delivered there by `mu`, namely

\[
 P^*[\mu^{-1}(h)].\operatorname{bottom}=T[h].\operatorname{bottom}.
                                                               \tag{1.1}
\]

For the identity core `mu^{-1}(h)=h`.  A soft row uses its native singleton
lower.  Thus a fixed endpoint host has no hidden bottom-token choice.

The ticket face is the canonical physical `P1--P2` face

\[
 q\in\{7,8\},\qquad \alpha,\beta\in\{0,1,2,3\},\qquad\beta\le\alpha.
                                                               \tag{1.2}
\]

There are two short choices and ten reset-monotone flag pairs for every
fixed host triple.

## 2. Completeness of the finite host menu

Fix an s7 owner phase `phi` and a short row `s in S`.  Write `O_phi(s)` for
its rank-nine owner and `R_s` for its rank-eight root.

### Lemma 2.1 (complete adjacent-host enumeration)

Every canonical predecessor endpoint belongs to the list

\[
 \{p_x:R_{p_x}=O_\phi(s)\setminus\{x\},\ x\in O_\phi(s)\},
                                                               \tag{2.1}
\]

after deleting rows which are not long.  Every canonical successor endpoint
belongs to

\[
 \{u_y:O_\phi(u_y)=R_s\cup\{y\},\ y\notin R_s\},             \tag{2.2}
\]

again after the long-row filter.  Before that filter each list has exactly
nine rows, and therefore each has at most nine valid long hosts.

For every pair of distinct surviving hosts, (1.2), the four long flags, and
the actual fixed-matching endpoint lowers exhaust all canonical fresh-ticket
possibilities at `s`.

#### Proof

A predecessor-to-short adjacency joins a rank-eight predecessor root to the
rank-nine short owner.  Their difference is one point, so the predecessor
root has exactly the form (2.1).  The target table has one row at each root,
hence this identifies every possible predecessor row.  Dually, a
short-to-successor adjacency joins `R_s` to a rank-nine successor owner,
which has exactly the form (2.2); the owner map is a bijection, so this
identifies every possible successor row.

The long target row fixes its middle and root.  Equation (1.1) fixes its
lower under the given matching.  The four long permutations, the two short
addresses and the ten pairs `beta<=alpha` are exhaustive by definition of
the canonical face.  Validity is then exactly the five-envelope predicate
of
`MATH_THEOREM_K17_PSTAR_FRESH_TICKET_LOCAL_INTERFACE_AND_HOST_MUTABILITY_20260802.md`,
including the canonical short lower `U-L` in cell three for `q=7` and cell
one for `q=8`.  No further local variable remains.  \(\square\)

The root and owner lists in Lemma 2.1 are exact **before** the long-row
filter; the theorem does not claim that all nine rows on either side are
valid long endpoints.

## 3. Complete local census and no-bank theorem

For `phi in {0,1}`, let `M_phi(s)` be the set enumerated in Lemma
2.1 which passes the exact five-envelope predicate.

### Theorem 3.1 (fixed-matching fresh-ticket local no-go)

The exact menu census is

\[
\begin{array}{c|rrrrrr}
 &\sum_s|M_\phi(s)|&q=7&q=8&
 |\{s:M_\phi(s)\ne\varnothing\}|&
 |\{s:M_\phi(s)=\varnothing\}|&
 \text{distinct endpoint hosts}\ \hline
\phi=0&1432&867&565&966&782&2318\\
\phi=1&1428&853&575&965&783&2298.
\end{array}                                                  \tag{3.1}
\]

Across the two phases the `1,748` shorts split as

\[
\begin{array}{c|rrrr}
 &\text{positive in both}&\text{only phase 0}&
   \text{only phase 1}&\text{zero in both}\\ \hline
 \text{short rows}&799&167&166&616.
\end{array}                                                  \tag{3.2}
\]

Consequently the current tuple `(P*,T,mu,S)` has no phase-specific
`1,748`-ticket bank in either owner phase.  This failure occurs before
endpoint-host privacy, source-token privacy, global cell/address
injectivity, history, reset, residence, supplier, compiler, or chronology
is tested.

#### Proof

Lemma 2.1 makes the enumerated menu complete.  Direct evaluation gives
(3.1)--(3.2).  Since `782` phase-zero shorts and `783` phase-one shorts have
degree zero in the local ticket hypergraph, no selection can cover the
whole shore in either phase.  Adding packing constraints can only delete
candidates, so the conclusion already follows at the local stage.

An independent C++ implementation reconstructs the root and owner
bijections, checks the fixed matching lower at every occupied long receiver,
adds the canonical short lower explicitly, and reevaluates every envelope.
It obtains the same candidate and short-set counts.  Its zero-set TSV is
byte-identical to the primary audit's TSV.  \(\square\)

## 4. The minimum mutable host interface on the current shore

Keep the old regenerated predecessor and successor hosts as the reference
triple, but allow `q,alpha,beta` to vary throughout (1.2).  The exhaustive
short partition by the minimum endpoint-host motion needed for *some* local
ticket is

\[
\begin{array}{c|rrrrr}
 &\text{fixed hosts}&\text{predecessor must change}&
 \text{successor must change}&\text{both must change}&
 \text{zero even if both change}\\ \hline
\phi=0&520&152&136&158&782\\
\phi=1&501&165&129&170&783.
\end{array}                                                  \tag{4.1}
\]

There is no nonfixed row on which both alternative one-sided changes work:
after the fixed-host class is removed, the predecessor-only and
successor-only positive classes are disjoint.  Equivalently, allowing only
the predecessor host to change
gives `672/666` positive shorts in phases zero/one, while allowing only the
successor host to change gives `656/630`.

The first column recovers the earlier fixed-host counts `520/501`; the
fixed-host two-phase overlap remains `332`.  Thus arbitrary address/flag
reselection repairs nothing on a frozen triple, one-sided host motion repairs
only `152+136` or `165+129` more shorts, and even two-sided host motion leaves
the degree-zero sets in (3.1).

Therefore the minimal interface which can possibly repair a degree-zero
short must change at least one item outside the endpoint-host/flag menu:

1. the short shore or its target middle;
2. the rematerialized child/outer-matching geometry, hence an actual lower
   delivered to a candidate long host (changing only its source label does
   not affect local validity);
3. the selected-factor owner/adjacency allocation; or
4. the canonical `q in {7,8}`, `beta<=alpha` ticket face itself.

The theorem does not assert that any one of these changes is sufficient.

## 5. Exact shore-replacement lower bounds

Let

\[
 Z_\phi=\{s\in S:M_\phi(s)=\varnothing\}.
\]

Then

\[
 |Z_0|=782,\quad |Z_1|=783,\quad
 |Z_0\cap Z_1|=616,\quad |Z_0\cup Z_1|=949.                 \tag{5.1}
\]

If `T`, `mu`, and the owner maps are fixed and repair is attempted only by
replacing rows of the current shore, at least `782` current rows must be
deleted for phase zero and at least `783` for phase one.  A single shore
which is locally positive in both phases must delete at least the `949` rows
in `Z_0 union Z_1`; at most `799` current rows can survive.

These are necessary deletion counts, not a construction.  No replacement
rows are selected here, and no matching or inverse-parent rematerialization
for a replacement shore is proved.

## 6. Bounded-state consequence and exact remaining hypothesis

The large counts in (4.1)--(5.1) concern **bulk child data**.  They do not
prove that `782`, `783`, or `949` occurrences must be carried across a
regenerative transition.  A different parent/shore/matching could be
reconstructed independently in each child while exporting only a bounded
connector.  Conversely, the current `(P*,T,mu,S)` cannot instantiate such a
theorem: it has no complete local bank to which a connector/reset state can
be attached.

The weakest proof-safe replacement hypothesis is now:

1. reconstruct phase-valid bulk shores and outer matchings for which every
   selected short has positive canonical local degree;
2. select full private ticket matchings, including endpoint hosts, actual
   outer sources, and global cell/address capacity;
3. designate a bounded exported connector/aperture/reset set; and
4. prove an exterior-fixed dependency isomorphism on that bounded set,
   including actual addresses, aggregate histories, residence, supplier,
   upper/common-cap and non-evicted compiler rows.

Only after items 1--2 may the number of phase-local ledger differences be
quotiented away as bulk reconstruction.  Items 1--4 are **UNPROVED**.  The
present theorem proves that item 1 fails for the frozen `P*`, `mu`, and `S`.

## 7. Proof boundary

The following statements are **PROVED**:

1. completeness of the adjacent-host menu in Lemma 2.1;
2. the exact tuple, positive-short and zero-short censuses (3.1)--(3.2);
3. nonexistence of a complete local bank on the frozen shore in either s7
   phase, before packing;
4. the exact minimum endpoint-host mutability partition (4.1); and
5. the necessary shore-deletion counts (5.1).

The following statements are **UNPROVED**:

1. existence of a replacement shore or a rematched inverse parent;
2. a size-`1,748` private endpoint/source/cell matching on any replacement;
3. a bounded exported connector/reset dependency closure;
4. selected `z=6`, endpoint aperture, history, residence, supplier,
   upper/common-cap and compiler closure;
5. an all-`k` regenerative host; and
6. every new bound on `nu(k)`.

## 8. Frozen artifacts

Primary producer:

```text
scratch/audit_k17_inverse_parent_fresh_ticket_phase_menus_20260802.py
scratch/k17_planted_b5_inverse_outer_parent_20260802/
  fresh_ticket_phase_menus.audit.json
  fresh_ticket_fixed_matching_zero_sets.tsv
```

Independent implementation:

```text
scratch/verify_k17_inverse_parent_fresh_ticket_fixed_matching_menus_independent_20260802.cpp
scratch/k17_planted_b5_inverse_outer_parent_20260802/
  fresh_ticket_fixed_matching_menus.independent.audit.json
  fresh_ticket_fixed_matching_zero_sets.independent.tsv
```

The two zero-set TSVs are byte-identical.  Final replay hashes are

```text
primary source
  f185347ad0c24e275388699cda35a4fec34c94c78bb57d5f9a633d4b4823d077
primary JSON
  694a7ac1ec82e5198ba6c994ab10e4282fff91920e0a7d8c996171e3f432528c
primary zero-set TSV
  741105d600055b6d5fe6515b028fd3438484dceb4d3fd956e83f86970ae68c3c
independent C++ source
  b4b69ed639437a9f719f5f815ef85f18af985cf3a44fb8d9c93fb0ea9a42c427
independent JSON
  f73e5331adc8dd14e39415a60fcce3ffb7ccbdcb22e7845d14d1bf9fbb1ca516
independent zero-set TSV
  741105d600055b6d5fe6515b028fd3438484dceb4d3fd956e83f86970ae68c3c
```
