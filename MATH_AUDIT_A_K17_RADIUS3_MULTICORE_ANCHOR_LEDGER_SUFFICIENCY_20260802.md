# `k=17`: radius-three multicore anchor-ledger sufficiency audit

**Date:** 2026-08-02  
**Status:** pure finite audit.  No SAT instance, proof search, or broad
radius-three enumeration was run.  The present artifacts do **not** support
an exact prelaunch join of at most `10^7` radius-three packets.

## 1. Verdict

The repository authenticates many q1 contradictions, but it does not yet
contain the occurrence-labelled causal data needed to intersect their exact
radius-three anchor hypergraphs.

The only complete radius-three **pre-generation omission certificate** now
available is the root-fan statement

\[
                         S\cap A_{21}\ne\varnothing .       \tag{1.1}
\]

After distinct-base compatibility and exact canonicalization, (1.1) leaves

\[
                    \boxed{2,909,465,711}                   \tag{1.2}
\]

packets.  The 13 primary profiles, four alternate profiles, and 3,664
bank-specific exact cores are valuable contradiction certificates, but none
currently exports an authenticated native `A3` table.  Consequently they may
be applied after direct reconstruction, but they cannot yet justify omitting
packets from the generator.

This is a certificate-sufficiency obstruction, not a lower bound on the true
number of q1-open packets.  The true multicore join may be much smaller.

## 2. Exact palette locality on the frozen recut face

Let `R` be the complete `16,667`-row primitive recut catalogue.  For a
recut `g` on base `b`, write

* `old(g)` for the lower colour of the selected cut of `b`; and
* `new(g)` for the lower colour of the replacement cut.

A direct join of the complete projection ledger to the cut-choice table gives
the following exact finite facts.

\[
\begin{array}{c|r}
\text{quantity}&\text{value}\\ \hline
|R|&16667\\
\text{bases admitting a recut}&3803\\
\text{baseline selected colours (base plus extra cuts)}&7612\\
\text{candidate-cut lower colours}&20477\\
|\{old(g):g\in R\}|&3803\\
|\{new(g):g\in R\}|&16667\\
\{new(g)\}\cap\{\text{baseline selected colours}\}&\varnothing
\end{array}                                                 \tag{2.1}
\]

All 7,612 baseline selected colours are distinct.  All 20,477 candidate-cut
lower colours are distinct.  Thus the old colours are injective by base, the
new colour map `g -> new(g)` is globally injective, and no primitive new
colour is selected anywhere in the baseline, including the fixed base-cut
bank.

### Lemma 2.1 (unique palette supplier)

For a compatible distinct-base packet `S`, every new colour has exactly one
possible positive supplier recut.  Every removed old colour is controlled by
the unique changed base which selected it.  In particular, palette status has
no inclusion-minimal binary or ternary compensation support on this face.

#### Proof

The selected-colour multiplicity obeys

\[
 m_S(c)=m_0(c)+\sum_{g\in S}
 \bigl({\bf1}_{new(g)=c}-{\bf1}_{old(g)=c}\bigr).          \tag{2.2}
\]

The baseline-selected and candidate-cut distinctness assertions in (2.1)
make every positive summand for a new colour unique and confine every
negative summand for an old colour to its unique old base.  Distinct-base
compatibility allows at most one of that base's alternatives in `S`.  Hence
a palette change is unary. \(\square\)

### Corollary 2.2 (only one possible ternary atom mechanism)

In the occurrence-labelled q1 atlas, the legality of an atom factors through
its tail occurrence, head occurrence, and selected lower colour.  Therefore
an inclusion-minimal ternary atom on this frozen face can only have the form

\[
 \{g_{\rm tail},g_{\rm head},s(c)\},                       \tag{2.3}
\]

where the first two recuts create the two endpoint states and `s(c)` is the
unique supplier of the previously unselected colour `c`.  If `c` is selected
in the baseline, atom activation has support at most two.  Endpoint creators
or the supplier may coincide, which only lowers the support.

This sharply reduces the *shape* of the missing ternary table.  It does not
give its size, because the per-core tail/head creator tables have not been
materialized.

## 3. Exact root-fan consequence

The root obstruction is the occurrence-labelled dual fan at sockets
`115442,115186` with sole colour `114930`.  Its frozen unfiltered projection
has:

* 12 selected noncore socket escapes;
* 67 recuts creating 154 new raw, still-unselected arm occurrences; and
* zero nonanchor endpoint-creator/lower-supplier pairs after the complete
  inverse supplier join.

The 12 visible escapes and nine central alternatives form `A21`.  They lie on
13 bases.  Joining their primitive keys to the projection also shows that
their 21 new lower colours are pairwise distinct, a special case of (2.1).

### Theorem 3.1 (no anchor-free ternary root breaker)

Every radius-three packet which destroys the root fan meets `A21`.  More
particularly, there is no `A21`-disjoint primitive ternary root-fan breaker.

#### Proof

Outside `A21`, neither central role changes.  The direct central seam remains
residence-illegal.  A new noncore arm therefore has one fixed central endpoint
and at most one recut-created outside endpoint.  If its colour is already
selected after the endpoint creator, that creator is one of the twelve
visible anchors.  Otherwise Lemma 2.1 supplies one unique positive colour
recut, so the arm already appears on the creator--supplier pair.  The frozen
nonanchor pair join is empty.  Hence an `A21`-disjoint triple cannot break the
fan. \(\square\)

`A21` is a complete hitting/generator family, not the exact inclusion-minimal
semantic disturbance hypergraph.  For example, the clean central recut
`1834:9924->9923` retains the same fan.  Enlarging a hitting family is safe;
calling every member a minimal disturbance would not be.

## 4. Authenticated core inventory and its boundary

There is no frozen authoritative `L0` manifest enumerating every
unconditional entry and every allowed embedding.  The radius-three launch
specification itself lists that manifest as a required prospective input.
The current useful inventory is as follows.

### 4.1 The 13 profiled one-recut contexts

The primary and alternate child-core ledgers identify these proof forms.  The
last column is the number of Hamming-two rows left for exact build after the
primary/alternate persistence-filter union; it is **not** an `A3` size.

| profile | anchor recut | stored proof form(s) | H2 residue |
|---:|:---|:---|---:|
| 0 | `540:2838->2842` | fan `F118996` | 288 |
| 1 | `3680:19815->19818` | fan `F115308` | 380 |
| 2 | `1284:6831->6832` | fan `F115308` | 380 |
| 3 | `3613:19443->19445` | fan `F115308` | 380 |
| 4 | `1379:7364->7380` | fan `F115308` | 380 |
| 5 | `1801:9773->9771` | `F115308` plus pendant `117348` | 431 |
| 6 | `3254:17426->17428` | lower `14820`; alternate bow tie `35275/35786` | 30 |
| 7 | `1532:8180->8181` | `F115308`; alternate bow tie `31844/32352` | 46 |
| 8 | `2251:12065->12067` | `F115308`; alternate bow tie `35275/35786` | 31 |
| 9 | `3029:16232->16234` | fan `F115308` | 380 |
| 10 | `3344:17953->17957` | fan `F115308` | 380 |
| 11 | `2251:12065->12066` | lower `87145`; alternate `F115308` | 34 |
| 12 | `1834:9924->9923` | retained root fan | 524 |

The residue counts sum to `3,664`.

The twelve locally copied primary semantic manifests have only the schema

```text
kind    index    orientation_or_mask
```

with `piece`, `out`, `in`, and `colour` rows.  The filter reconstructs a
profile dynamically and computes `dependency_bases`, structural lower masks,
and complete restricted rows in memory.  It does not serialize those sets.
Its persistence predicate is explicitly documented in source as
**sufficient, not necessary**.  A failed predicate is therefore an
`EXACT_BUILD` promotion, not proof that a unary causal anchor occurred.

Moreover, for each Hamming-two bank the source scans only a profile whose
anchor recut occurs in that bank (and a second such profile if the partner is
also a profiled anchor).  It is not a simultaneous intersection over all 13
profiles.  Its input consists only of joint-zero-265-clean pairs, so it also
cannot justify discarding a dirty singleton or pair which a third recut
repairs.

The four alternate semantic manifests used for profiles `6,7,8,11` and the
`central9923` semantic manifest are referenced by remote launch paths but are
not present in the local artifact tree.  The local union count ledger records
their effect, not their occurrence-labelled cones.

### 4.2 The 3,664 exact Hamming-two cores

The final audit authenticates 3,664 distinct banks, 3,664 verified literal
core refutations, and no unknown row.  A direct count in the proof manifest
also gives 3,664 distinct `core_sha256` values.

The retained bundle contains, per case, the bank, integer-variable
`core.cnf`, `core.lemmas`, a build audit, and checker logs.  It does not
contain a variable-to-`OccKey` map, native seam/provider rows, complete atom
footprints, blocker provenance, or a third-recut dependency table.  Thus the
cores authenticate q1 UNSAT in their two-recut banks, but they cannot yet be
used to omit a third recut by occurrence-labelled persistence.

The 65 visible-visible pair proofs and 49 compensated dirty-central proofs
have the same launch boundary: they authenticate their exact banks, but no
complete native radius-three causal table is frozen for them.

## 5. Concrete missing fields for an exact `A3` join

For each core and permitted occurrence embedding, a proof-safe prelaunch
intersection still needs all of the following.

1. Immutable source/base/cut, side, orientation, endpoint-owner, and role
   keys for every load-bearing occurrence.
2. Every positive row's complete effective `AtomKey` list and every atom's
   complete resource footprint.
3. Capacities, conflicts, complement pairs, named guards, blockers, and
   retained dead-atom derivations.
4. The base-local unary sets `Occ_K` and `Clause_K`.
5. The unfiltered endpoint creator tables `Tail_K(c)` and `Head_K(c)` and the
   unique palette supplier `s(c)` from Lemma 2.1.
6. Every two-endpoint pair and every ternary join (2.3), evaluated before any
   singleton or pair zero-265 filter.
7. The truth table on all subsets of each proposed support and its
   inclusion-minimality bit.
8. Every allowed typed embedding/transport, with a named unchanged-core or
   guarded-minor proof for negative omission.

A suitable canonical record is

```text
core_id embedding_id datum_id event_type arity
rid0 rid1 rid2 subset_truth old_value new_value
tail_occ head_occ colour full_footprint blocker_proof
```

with unused recut fields written as `-`.  Without these fields, a ternary
tail--head--supplier atom can agree with every stored singleton and pair
ledger while appearing only on the full triple.

## 6. Exact size of the closed-pair extension face

Even the simplest use of the newly closed 3,664-row portfolio is above the
target scale before its pair cores are decoded.

Let `G` be the graph on primitive recuts whose edges are the 3,664 exact
Hamming-two cases.  It has 1,205 incident primitive vertices on 472 bases.
For an edge `{u,v}`, the number of compatible third recuts is

\[
             16667-n_{base(u)}-n_{base(v)}.               \tag{6.1}
\]

Summing (6.1) over the case ledger gives

\[
                              S_1=61,006,005.              \tag{6.2}
\]

Two portfolio edges generate the same triple exactly when they form a
compatible length-two path.  If `d_b(v)` is the number of neighbours of `v`
on base `b`, their number is the directly checkable degree sum

\[
 S_2=\sum_v\left[{d(v)\choose2}-\sum_b{d_b(v)\choose2}\right]
    =708,238.                                               \tag{6.3}
\]

The subtracted terms are precisely the same-base-incompatible endpoint
pairs.  The portfolio graph has

\[
                              t(G)=0
\]

triangles, so no third inclusion--exclusion term is present.  Therefore the
number of distinct compatible triples containing at least one
exact-portfolio pair is

\[
                    \boxed{S_1-S_2=60,297,767}.            \tag{6.4}
\]

This is an exact duplicate-free count of the raw **pair-extension subface**,
not a complete radius-three generator and not a survivor count.  A decoded
pair core could reject most third recuts, but the current integer-variable
core bundles do not prove which ones.

## 7. Why `<=10^7` is not presently certified

The root condition leaves (1.2).  No other current artifact supplies a
complete inclusion-minimal unary/binary/ternary anchor table with named
unchanged-core certificates.  Therefore an output of at most `10,000,000`
would presently omit at least

\[
          2,909,465,711-10,000,000=2,899,465,711          \tag{7.1}
\]

root-anchored packets without a proof-safe pre-generation reason.

The obstruction is especially sharp for ternary residues.  Lemma 2.1 removes
multi-supplier palette ambiguity, but it leaves the genuine
`tail creator + head creator + unique supplier` mechanism for every non-root
core.  Hamming-two profiles and delta ledgers contain no evidence about a
datum whose truth table is zero on all proper subsets and one on the full
triple.  Such packets cannot be removed until the tables in Section 5 are
frozen and replayed.

Accordingly:

* exact root preprocessing: **available**, leaving `2,909,465,711`;
* exact 13-profile multicore `A3` intersection: **not materialized**;
* exact 3,664 pair-core third-recut intersection: **not materialized**;
* exact complete join of size at most `10^7`: **not supported by the current
  artifacts**.

## 8. Frozen evidence

| artifact | SHA-256 | use |
|:---|:---|:---|
| `scratch/threadD_k17_round02_hamming2_anchor_20260802/projection.tsv` | `bcaa7f353d00504edb954d448d7537f7f4d2c851d929be89df98e1c66be373f8` | complete recut/new-lower and raw-arm projection |
| `scratch/threadD_k17_round02_hamming2_anchor_20260802/latent_join.audit.json` | `0ee2c01a938b58eec8cb9b26161fcf3defbaf92a8f0ab4211b6c0b97bb09e284` | empty nonanchor creator--supplier join |
| `scratch/threadD_k17_round02_anchored_two_recuts_20260802/anchors.tsv` | `eedf932033280d3bef390e49929400ea5612097fbafbf0b6ca78db709b6834c9` | 21 occurrence-labelled root anchors |
| `scratch/threadD_k17_round02_anchored_two_recuts_20260802/k17_two_cut.candidates.tsv` | `fa1133f5ffc8b70bf7d1713dfa930670508fb6bb6e1255d570f00ea851d00cc6` | cut-to-lower map used in (2.1) |
| `scratch/ad_k17_round02_frozen_cut_colours_20260802.tsv` | `4ad806b8b8ae3eecfd560abec3709de8ab74cd04f198771924d5d09b3e9b8c23` | 7,612 distinct baseline-selected lower colours |
| `scratch/threadD_k17_round02_q1_semantic_cores_remote_20260801/summary.tsv` | `3dee94a551c557fb6433a02fd78fe4d133f2a41e56f31ae8ac5d4be8642cd548` | 12 primary semantic profile proofs |
| `scratch/threadD_k17_round02_delta_signatures_20260802/counts_union.tsv` | `f184ade82dc8f63ac5bd74bf2d89aed25a9d57f05dcc830782480e6bbf3c8fa0` | primary/alternate H2 residue counts |
| `scratch/threadD_k17_round02_delta_signatures_20260802/audit.json` | `ddcd28ff60094b96426ac617a63b9e93aee0ab7c4e4c3aff0056ab8dc441bae4` | 3,664 distinct complete H2 delta keys |
| `scratch/r2_k17_exact3664_final_audit_20260802/cases.tsv` | `860924cbb256d320ee35790e98ebd1e78bf0b01cdabf1bdbf9fdaef0929fa109` | exact pair graph used in Section 6 |
| `scratch/r2_k17_exact3664_final_audit_20260802/proof_manifest.tsv` | `0706fee2c9dba89c6339ca2088c9edc021f0d5107f0c1ddf1e344129fa3f92d3` | 3,664 bank/core proof identities |
| `scratch/r2_k17_exact3664_final_audit_20260802/core_recheck/summary.tsv` | `0542f58ba29240337f0545b21013ea7d40ccc53175b17c5668cfca529c1223e4` | independent core-proof replay |

The counts in Sections 2 and 6 were obtained by small read-only joins of
these frozen ledgers.  No result file was modified and no q1 solver was run.
