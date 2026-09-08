# `k=17`: audit of the octahedral `3+1` topology ledger

**Date:** 2026-08-02  
**Status:** exact conditional permutation lemma, independent audit of the
implemented half-edge DSU, and component-layer counterexample.  No
enumeration or SAT result is claimed.

## 1. Audited object

The source audited here is

```text
scratch/threadD_k17_round02_octa31c8_static_filter_20260802.cpp
SHA-256 5a0472788c1e9c053c498c540f4a4c53eafe2ff9050680e2bf0508b564225275
```

In `incidence_positions`, a component is traversed as

```text
owner_i -- lower_i -- owner_(i+1).
```

The incidence `(lower_i,owner_i)` receives position `2i`, and
`(lower_i,owner_(i+1))` receives position `2i+1`.  The patched function
`topology_ledger` retains a `3+1` component pattern and first performs an
eight-half-edge DSU reconstruction.  It then records whether the three
positions on the repeated component have equal parity, constructs
`strand_next` when they do, and sets

```text
new_return[i] = strand_next[index of new_owner[i] among old_owner[*]].
```

The audit separates three questions which must not be conflated:

1. Does this calculate the formal cut-permutation topology?
2. Does it certify the declared literal directed order?
3. Are its component ids taken in the component layer to which the launch
   theorem refers?

## 2. Exact conditional lemma

### Lemma 2.1 (parity and first return)

Assume all four removed incidences are genuine turns of one fixed
two-regular component layer.  Write the selected old transition at slot `i`
as

```text
x_i -- lower_i -- y_i,
```

where `y_i=old_owner[i]`, and suppose the packet is interpreted as one
directed head switch.  On a component containing more than one selected
slot, such a direction exists if and only if the incidence positions of all
its `y_i` half-edges have equal parity.

After choosing that direction, let `s(i)` be the index of the next cut tail
reached by following the retained old strand from `y_i`.  If

```text
new_owner[i] = old_owner[h(i)],
```

then the first-return permutation after the atomic switch is

```text
i |-> s(h(i)).
```

Consequently, in a `3+1` pattern, the switch is a two-component-to-one
fusion if and only if `s o h` is a four-cycle.

#### Proof

In the stored traversal, an odd-position incidence is traversed
`lower -> owner`; an even-position incidence is traversed `owner -> lower`.
Reversing the whole component interchanges these two roles.  Hence one
component direction makes every changed owner the head precisely when all
corresponding parities agree.  In that direction, increasing incidence
position (odd case), or decreasing incidence position (even case), lists
the cut slots in their old first-return order.  This is exactly the cycle
stored by `strand_next`.

The new turn from `x_i` ends at `y_(h(i))`; the retained strand beginning
there ends at `x_(s(h(i)))`.  Thus the new return is `s o h`, exactly the
assignment made by `new_return`.  Its cycle count is the number of new
components meeting the four switched turns.  QED.

For the octahedral packet, owner balance makes `h` a four-cycle (one of the
two orientations according to phase).  Thus the implementation's
`cycle_count(new_return)==1` is an exact formal topology test under the
hypotheses of Lemma 2.1; the order of composition in the source is correct.

## 3. What parity does not certify

Equal parity certifies existence of a convenient orientation.  It does not
authenticate an already fixed directed occurrence order.  In particular,
the current code is free to reverse the repeated component according to the
observed parity and never compares its resulting word with an immutable
direction/alignment manifest.  Therefore it can accept a physically
two-to-one octagon which is outside a declared role-oriented directed face.

This is harmless only if the output status is interpreted as

```text
UNKNOWN_FORMAL_ORIENTATION_EXISTS
```

and every survivor is later checked against the missing direction, role,
age, and protected-successor manifests.  It is not a certificate for
`PASS_STATIC_FILTER` or for a literal `3+1` packet.

Conversely, relative to the same authenticated raw cycle-cover layer, this
orientation-existence test is a safe superset of a literal directed face:
every literal directed head switch necessarily has equal parity and the
same physical `s o h` cycle count.  The missing direction manifest creates
false positives, not false negatives, at this conditional stage.

This statement concerns the **topology predicate only**.  A generic
immutable role can change in a joint endpoint--colour or
protected-successor field outside an incomplete unary cone.  The patched
source therefore uses `move_touches_cone` only as a reported statistic, not
as an omission filter.  It also reports the two reconstructed socket
fingerprints but does not reject a row merely because they persist; such a
row receives `UNKNOWN/MISSING_GENERIC_ROLE_MANIFEST`.  Hence missing generic
role/dependency manifests now enlarge the emitted formal stream instead of
silently pruning it.

## 4. The component layer must remain part of the theorem scope

The current `incidence_positions` is built from

```text
dense_cycles(factor, factor.ends),
```

whereas the round-02 physical model also has a fixed cut set `model.is_cut`
and 7,612 opened path components.  The patched audit payload explicitly
declares

```text
RAW_RANK8_RANK9_SELECTED_INCIDENCE_FACTOR_CYCLES
```

as the topology layer.  Thus a lower row in `model.is_cut` remains a real
incidence of this raw factor, while its effect on the subsequently opened
path bank is separately replayed by `score_target` and
`physical_pieces_after`.

### Counterexample 4.1 (not a safe path-layer superset)

Take one raw factor cycle and open it at two fixed cuts into paths `P,Q`.
Choose three genuine internal changed incidences on `P` and one on `Q`, in
the aligned order.  This is a literal `3+1` pattern in the opened path
layer, but all four incidences have the same raw-cycle component id.
The current `by_component.size()!=2` test rejects it.

In the opposite direction, choose a raw-cycle `3+1` key for which one of the
four lower rows is a fixed opening cut.  The current topology ledger counts
that incidence as a turn although it is no adjacency in the opened path
layer; the downstream path replay ignores it.

Thus the patched test is a safe formal raw-factor superset because its launch
contract now explicitly declares the uncut dense factor cycles.  The same
ledger must not be reused as a completeness filter for an opened-path `3+1`
contract; Counterexample 4.1 remains the sharp reason.

## 5. Audit of the implemented constant-size verifier

The patched source implements the required half-edge quotient.  Its exact
algorithm is as follows.

1. **Authenticate the layer.**  Bind the candidate to either the raw
   two-factor or the opened path forest, including its content hash.  If the
   layer is the opened forest, reject an advertised turn whose lower row is
   cut.
2. **Authenticate the toggle.**  Verify all four old incidences are selected,
   all four opposite incidences are absent, the old incidences are mutable,
   and the four owner/lower degree balances are exact.
3. **Delete the four old incidences.**  Give each deleted edge two labelled
   boundary half-edges.  From the authenticated ordered component trace,
   connect half-edges joined by each retained strand.  For a cycle this is
   obtained by sorting the at most four deleted positions; for a path, add
   its two terminal boundary symbols.
4. **Add the four new incidences.**  Join the lower half-edge of slot `i` to
   the owner half-edge whose immutable owner key equals `new_owner[i]`.
   A DSU on at most eight switch half-edges (plus at most four path-terminal
   symbols) now gives the exact touched-component count and partition.
5. **Topology gate.**  Require exactly two old touched components with
   multiplicities `3+1` and exactly one new touched component.  Independently
   replay the full changed factor for rows that survive later filters.
6. **Directed gate.**  If an authenticated direction manifest exists,
   compare every removed half-edge side and the repeated cyclic word with
   the phase-specific expected word.  If it does not exist, parity may be
   retained only as the necessary `ORIENTATION_EXISTS` prefilter and the row
   must remain `UNKNOWN_MISSING_DIRECTION_MANIFEST`.

For the implemented endpoint numbering, node `2i` is the lower half-edge and
`2i+1` is the old-owner half-edge.  At an even incidence position the
canonical traversal is `owner -> lower`, so its after-half is `2i` and its
before-half is `2i+1`; at an odd position these roles reverse.  The source's
`after_left` and `before_right` formulas are therefore exact.  Joining
`2i` to `2h(i)+1` is exactly the inserted incidence.  Counting the resulting
DSU roots gives the touched-component count after the toggle.

On every parity-consistent raw-cycle row the source also demands agreement
between this DSU result and `cycle_count(strand_next o h)`.  This is a useful
independent constant-size cross-check.  Mixed-parity physical fusions are
retained as formal `UNKNOWN` rows rather than being rejected as though the
absent direction manifest were known.

## 6. Exact scope conclusion

The formulas in `topology_ledger` contain no permutation-order bug, and the
new DSU independently certifies physical raw-factor two-to-one fusion.  The
parity/permutation subledger proves the conditional **formal
orientation-exists two-to-one fusion** lemma above.  Neither test, by itself,
proves literal directed alignment.  With the raw component layer now
declared, the present topology filter may safely promote its rows as
`UNKNOWN`; it must not use this raw-cycle ledger as a completeness filter for
an opened-path face.  No q1, residence, upper, dependency-library, or global
`k=17` conclusion follows from this audit.
