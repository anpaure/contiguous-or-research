# Inverse rematerialization, derived address state, and the exact `B+O(1)` scope

**Date:** 2026-08-02  
**Status:** proof-safe implication and quantifier audit.  The abstract lemma
below is exact, and its `k=17` hypotheses are authenticated by the frozen
inverse-parent artifacts.  It removes inherited selected source/address
labels from the *carried* regenerative sidecar.  It does **not** make the
`1,748` ticket geometries a bounded state, prove phase-common occurrence
closure, construct a chronology, or imply a new bound on `nu(k)`.

## 1. Derived-ticket-state lemma

Let `T^0` be an exact compressed-normal target-partition table, with hard
`LMR` identity core `H`, `LR` rows `A`, and `MR` rows `B`.  Choose equally
large sets

\[
                  F\subseteq A,\qquad S\subseteq B
\]

and a matching

\[
       \phi:S\longrightarrow F,\qquad
       \ell_{\phi(s)}\subsetneq m_s.                         \tag{1.1}
\]

Keep the identity matching on `H`.  Let `P` be the origin-form parent
obtained by putting bottom `ell_(phi(s))` below the suffix `m_s subset r_s`,
stripping the rows of `F` to free roots, and leaving the other rows fixed.
Let `mu^0` be the complete outer matching consisting of the identity edges
on `H` and the edges `s -> phi(s)`.

Suppose a second local mode is obtained by a receiver permutation `kappa`
such that

\[
                         \mu^1=\kappa\mu^0                 \tag{1.2}
\]

is legal and rematerializes an exact table `T^1`.  Let `E subset H` be a set
of endpoint hosts fixed by `kappa`.  For `h in E`, define its selected source
label from the new parent rather than by transport from an old ledger:

\[
                    u^*(h)=(\mu^0)^{-1}(h).                  \tag{1.3}
\]

Then:

1. `P,mu^0,mu^1` are one common static outer parent and two exact local
   materializations;
2. for every `h in E`,
   \[
       (\mu^0)^{-1}(h)=(\mu^1)^{-1}(h)=h;                    \tag{1.4}
   \]
3. every ticket whose non-token geometry replays in the fixed rows of the
   two modes acquires a common literal source/receiver pin by replacing its
   old token label with `u^*(h)` at each real endpoint;
4. consequently, the inherited source-token permutation and its ambient
   orbit are **derived data**, not a regenerative state coordinate.

### Proof

The identity edges on `H` and (1.1) are a perfect matching from the native
hard bottoms of `P` to the occupied receivers of `T^0`; hence they
rematerialize `T^0` row by row.  Equation (1.2) gives the second exact local
materialization.  If `h in E subset H`, the identity core gives
`(mu^0)^(-1)(h)=h`.  Since `kappa(h)=h`, (1.2) gives

\[
 (\mu^1)^{-1}(h)=(\mu^0)^{-1}\kappa^{-1}(h)=h,
\]

which is (1.4).  Thus the same parent bottom is placed at the same endpoint
in both modes.  Replacing an inherited token name by (1.3) makes every
token/source/receiver equation literal.  All remaining ticket equations are
exactly the assumed common replay of its non-token geometry.  No inherited
source-label orbit is used.  \(\square\)

The lemma is deliberately static.  A chronology or a different owner phase
may change the non-token ticket geometry, and then clause 3 must be proved
again by a phase-specific occurrence selection.

## 2. Exact `k=17` instance

For the planted `B_5` table the reduced matching (1.1) has size `1,748`.
The resulting parent and regenerated ledger have hashes

```text
inverse_parent.tsv
  a146debfe42ef678b3ea64666f219504f8b26f77aec169724b3d8f3b5f268a12

regenerated_selected_tickets.tsv
  cb2b0660c2d42f2351ef884ecf3148d7feac57214b311c3109886aeb563fdc2e

regenerated_physical.audit.json
  1dd0d9d1c4e6a9690bc84bf00b0bd938403335c5ec659cde7a1acca814389b48
```

They prove:

* `1,748` selected tickets and `3,495` real endpoint pins regenerate on one
  parent in both **local** `B_5` modes;
* every real source label is its endpoint row, so the selected real
  source/address sidecar has size zero;
* only `572/3,495` inherited source labels happened already to agree; the
  other `2,923` were genuinely reconstructed, showing that this is
  rematerialization rather than transport;
* the local moving interface has `22` atoms, receiver permutation support
  `8`, and one fixed-soft endpoint.

The last bullet is the only bounded object exhibited here.  The table, the
`1,748`-edge inverse matching, the `1,748` ticket geometries, and their
`3,496` endpoint hosts are bulk child data, not an `O(1)` carried state.

This distinction is forced by the independent s7 replay:

```text
regenerated_s7_owner_phase_replay.independent.audit.json
  04bb5a1e37acc647accaa71f452d74d3dbb176101b01e07b950b96e3fad8a29a
```

The fixed regenerated records pass only

\[
 520\text{ in phase zero},\qquad 501\text{ in phase one},\qquad
 332\text{ in both}.                                      \tag{2.1}
\]

Thus the large ticket bank is not itself a phase-common regenerative
certificate.

## 3. Shortest proof-safe implication toward `B(k)+O(1)`

The bounded-spine theorem separates bulk data reconstructed at each child
from the bounded sidecar carried between children.  By the lemma above, a
same-parity construction may omit inherited selected source labels from its
sidecar **provided that at every child it reconstructs**:

1. an exact target-partition table;
2. an inverse outer matching of the form (1.1); and
3. a phase-valid occurrence/ticket selection on that new table.

Under those three hypotheses, the source/address part of the regenerative
defect is zero.  If, in addition, the construction exports only a bounded
local actuator/endpoint/reset state, has bounded actual serialization
charge, and leaves bounded terminal damage, the bounded-spine theorem gives

\[
                         \nu(k)\le B(k)+O(1).                 \tag{3.1}
\]

This is a genuine simplification of the conditional all-dimensional target:
one need not conjugate or preserve a macroscopic inherited token-label
orbit.  The source labels can be recomputed from the new outer matching.
It is **not** an unconditional implication, because the three child
constructions and the bounded remaining charges are not known uniformly.

## 4. The exact gate not covered

What remains is one common **phase-specific selected dependency closure**,
not another source-label transport theorem.  It must simultaneously supply:

1. **connector/chronology:** phase-specific occurrence witnesses (including
   the singleton structural `z=6` opener), compatible shared flags and
   physical ports, one connected/opened chronology, and an `O(1)` clean
   relay/reset cover;
2. **upper/residence:** aggregate histories, legal coordinate residence, and
   named arbitrary-width upper witnesses on that actual chronology;
3. **compiler:** selected-state supplier rank, one integral common-cap/lower
   matching, and bounded complete terminal damage.

The static inverse parent proves none of these.  In particular, the
`520/501` replay counts in (2.1) fail before chronology or compiler flow is
even considered.  Therefore the correct present state ledger is

\[
\begin{array}{c|c}
\text{bulk target partition and local two-mode outer rematerialization}
  &\text{proved at }k=17\\
\text{selected real source/address labels on the local ticket bank}
  &\text{regenerated; zero extra address sidecar}\\
\text{bounded full regenerative state}
  &\text{not proved}\\
\text{phase-common connector + upper/residence + compiler closure}
  &\text{open}.
\end{array}                                                  \tag{4.1}
\]

No new value of `nu(17)`, no `B+1`, and no unconditional
`B(k)+O(1)` theorem follows.

## 5. Authoritative inputs

```text
MATH_THEOREM_K17_PLANTED_B5_INVERSE_OUTER_PARENT_AND_REGENERATED_TICKET_LEDGER_20260802.md
  7fe70f88a81bf8bbfb44aec209d7b7dba61f7de8ab5ba4a59ade9eb2cd290604

MATH_THEOREM_K17_B5_PHYSICAL_ROOT_SEED_S7_APERTURE_AND_B268_PARENT_EXCLUSION_20260802.md
  803e13a1cc77f58add8d2a024d20df1d6e21f3c641e579830d5dce2db0023acf

MATH_AUDIT_K17_STRICT_DEF84_RECOUPLED_OCCURRENCE_COMMON_STATE_GATE_20260802.md
  086570a6eea6f98f335f9b7e6324bd017ac79d6abda144180de1d2d82e900bd3

MATH_THEOREM_BOUNDED_DEFECT_REGENERATIVE_SPINE_AND_EXPLICIT_O1_CONSTANT_20260731.md
  0b069898885e643f21dfb3f9481110dfd9a177a2d11aa34eccc445faa675e11c
```
