# AD audit: saturated tri-window semantic atlas and repeat-free handoff contract

Date: 2026-07-30  
Lane: AD  
Status: **exact schema/completeness audit; no search verdict and no claim that
the seed-5 self-pair is best among all authenticated runs**

## 1. Verdict

The frozen seed-4 S4 bundle is an exact, complete semantic atlas for its own
4/9/5 collar. Its provider semantics and maximal-core theorem transfer
verbatim to an ordered pair from {seed1,seed5}. Its freezer and current
maximal-core executable do not transfer verbatim:

* the freezer is hard-coded to one self-parent, three S4 facet masks and S4
  file names;
* the executable is hard-coded to 69 residual targets, holes
  0x31ce,0x7bce, and the S4 provider-pair frontier.

The transferable object is the complete target-labelled incidence family

\[
                         (T,F,Q),                                      \tag{1.1}
\]

where \(T\) is a fixed-body residual target, \(Q\) is the nonempty set of
collar cells in one literal interval, and \(F\) is the OR of its fixed cells.

## 2. Exact S4 audit

The seed-4 word is

\[
[4\text{ free}]+P[6:6436]+[9\text{ free}]
 +(0x8000\vee P[7:6432])+[5\text{ free}].                            \tag{2.1}
\]

Seed 4 is not depth-two repeat-free, so this is a semantic calibration only.
The frozen bundle replays:

| quantity | value |
|---|---:|
| length/free cells | 12,873 / 18 |
| fixed-body covered nonzero masks | 65,466 |
| residual targets | 69 |
| map shapes \((F,Q)\) | 389 |
| target-labelled providers | 5,867 |
| literal potential intervals | 5,876 |
| omitted/extra semantic providers | 0 / 0 |
| incumbent coverage | 65,533 |
| incumbent holes | 0x31ce, 0x7bce |

Authoritative S4 files:

    scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/host_atlas.audit.json
      SHA-256 9304c90e9196d06f2eaad195f090b8f30d708ec7acc426d0edaab6b2cda24718
      payload e392f8e505d975f5ac64263cabb6ea3edca1c9a5dcf435c4af660879c2dfe0db
    scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/residual_witness_incidence.tsv
      SHA-256 5df821abdd06e74a7aa1f8206aa0bc483d55afb0afaaf8c7cd042fd52def8cd5
    scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/model.map.json
      SHA-256 fc2c4f185e294b963c391af56379e4dfbfbf9655a2b7457aa798a7d854ff73f2

The completeness comparison is correctly target-labelled: for every residual
\(T\), it scans every physical interval meeting a free cell, retains it
exactly when \(F\subseteq T\), collapses by \((F,Q)\), and compares with the
map witnesses for \(T\). Comparing only the unlabelled shape table is
insufficient.

## 3. Ordered-pair semantics and maximal-core theorem

For length-6,438 parents \(X,Y\), put

\[
A=X[6:6436],\qquad B=0x8000\vee Y[7:6432].                             \tag{3.1}
\]

The ordered free positions are

    0,1,2,3,
    6434,6435,6436,6437,6438,6439,6440,6441,6442,
    12868,12869,12870,12871,12872.

Let

\[
{\cal C}_{\rm fix}=\operatorname{Cov}(A)\cup\operatorname{Cov}(B),\qquad
{\cal R}=\{1,\ldots,0xffff\}\setminus{\cal C}_{\rm fix}.               \tag{3.2}
\]

Each Cov uses intervals wholly inside that one body. It does not use the
incumbent collar or intervals in the concatenation.

Choose one row \(h_T=(T,F_T,Q_T)\) for every \(T\in{\cal R}\), and set

\[
K_p=\bigcap_{T:p\in Q_T}T,                                             \tag{3.3}
\]

with empty intersection 0xffff. The selection is realizable by nonzero
literal collar masks iff

\[
K_p\ne0\quad\text{for every used }p,\qquad
F_T\vee\bigvee_{p\in Q_T}K_p=T\quad(T\in{\cal R}).                     \tag{3.4}
\]

When (3.4) holds, assigning \(K_p\) gives an integral literal realization.
This is the exact maximal-core handoff; no fractional completion occurs.

## 4. Catalogue completeness

For every seed-1/seed-5 ordered pair,

\[
\bigvee A=0x7fff,\qquad \bigvee B=0xffff.                              \tag{4.1}
\]

Thus an interval meeting two free windows contains a saturated fixed body
and realizes only a fixed-body-covered mask. Every residual provider meets
exactly one free window.

| ordered pair \((X,Y)\) | residual targets | exact \(E_{\rm cat}=E_{\rm esc}\) |
|---|---:|---:|
| (1,1) | 73 | 5 |
| (1,5) | 70 | 6 |
| (5,1) | 73 | 5 |
| (5,5) | 70 | 7 |

Hence maxext=40 is complete for all four pairs. This is parent-specific, not
a consequence of repeat-freeness alone.

The new atlas must still pass the stronger direct acceptance test:

1. reconstruct the skeleton from the two parent hashes;
2. recompute (3.2) without an extension cutoff;
3. for every residual \(T\), scan all intervals until fixed OR first contains
   a bit outside \(T\);
4. collapse survivors by \((F,Q)\);
5. require exact target-labelled equality with the map witnesses.

Both set differences must be empty. Every stored representative endpoint
must reconstruct its exact \(F,Q\). The map payload hash must replay after
removing its payload_sha256 field. Stale paths embedded in copied stats are
never authority; copied-file hashes are.

## 5. Exact 70-option maximal quotient

There are

\[
\binom52+\binom{10}2+\binom62=10+45+15=70                            \tag{5.1}
\]

nonempty contiguous free intervals \(Q\).

### Theorem 5.1

For every residual \(T\) and every \(Q\), the legal rows with that
\((T,Q)\) have a unique greatest fixed OR.

### Proof

The interval \(Q\) alone gives \(F=0\). If \(Q\) is internal, that is the
only fixed contribution. If it touches one boundary, contributions form one
monotone prefix/suffix OR chain. If it is the whole window, its two shore
extensions are independent monotone chains. The union of the greatest legal
state on each shore is legal and contains every other two-shore union.
Plateaux are collapsed by \((F,Q)\). QED.

Replacing a row by this greatest same-\((T,Q)\) row preserves its cell caps
and only removes demanded bits. Conversely every reduced row is a raw
physical row. Therefore the exact reduced master has

\[
                            70|{\cal R}|                               \tag{5.2}
\]

rows: 5,110 for 73 targets and 4,900 for 70 targets.

For the frozen seed-5 self map, an independent read-only grouping found
4,900 \((T,Q)\) classes, zero failures of unique greatest fixed OR, and
4,900 reduced rows. The raw map has 6,081 rows.

## 6. Required repeat-free bundle

For the ordered pair winning the literal-hole inventory, freeze:

| file | exact role |
|---|---|
| x_parent.word, y_parent.word | ordered parents, separately hashed |
| collar.cells | 18 cells in manifest free-position order |
| assembled.word | exact 12,873-cell reconstruction |
| model.map.json, model.stats.json | copied exact map/stats |
| fixed_layout.tsv | position, segment, parent index, fixed/incumbent value |
| residual_targets.tsv | residual targets and host counts |
| residual_witness_incidence.tsv | every raw target-labelled \((T,F,Q)\) |
| residual_maximal_provider_incidence.tsv | greatest row per \((T,Q)\) |
| residual_potential_literal_intervals.tsv | intervals before collapse |
| residual_incumbent_literal_hosts.tsv | actual incumbent residual hosts |
| host_atlas.audit.json | all hashes, counts, zero/zero completeness |
| README.md | reconstruction and exact scope |

The raw incidence TSV must include:

    target_dec target_hex target_rank witness_variable shape_index
    fixed_or_dec fixed_or_hex needed_bits_dec needed_bits_hex
    forbidden_bits_dec forbidden_bits_hex free_positions free_qmask18
    representative_left representative_right
    incumbent_or_dec incumbent_or_hex incumbent_realizes_target

free_qmask18 bit \(j\) means free_positions[\(j\)]. The reduced TSV must add
raw_class_size and the list or digest of dominated witness IDs, and pass:

1. exactly 70 rows per residual target;
2. one row for every \((T,Q)\);
3. its \(F\) contains every raw \(F\) in that class;
4. it is itself a raw physical row;
5. needed_bits equals \(T\mathbin{\&}\mathord{\sim}F\).

The manifest must bind ordered parents, collar, map, stats, assembled word,
producer, body slices/free positions, fixed coverage, residual histogram,
raw/literal/reduced counts, incumbent literal holes, full replay count,
payload/representative checks, zero omitted/extra counts, and the applicable
\(E_{\rm cat}\) certificate hash.

## 7. Maximal-core solver contract

The provider solver may consume the reduced TSV after verifying the dominance
certificate. A SAT selection decodes to the eighteen maximal cores and must
then be replayed over all 65,535 nonzero masks.

Current executable:

    scratch/search_r_k16_s4_host_frontier_20260730.cpp
    SHA-256 5242edd11e1750ff963b757daa9b1bae53ade04c9d5d1259e275baa2c9a2ad69

It is not a repeat-free driver without changes:

* lines 44 and 220--221 require 69 targets;
* lines 314--358 hard-code the two S4 holes and five frontier counts;
* line 471 prioritizes those holes;
* lines 634--635 hard-code S4 proof scope;
* budget3 from line 660 is S4-only.

A generic full mode obtains target count and incumbent holes from the hashed
manifest, checks Q_count=70, removes every S4 frontier assertion, and binds
proof/assignment to incidence and manifest hashes. UNSAT is scoped to one
ordered pair and this 4/9/5 fibre; SAT is promoted only after full replay.

## 8. Reuse boundary

Reusable as written:

    scratch/build_k16_triwindow_dimacs_20260730.py
    SHA-256 a14198849c66d6612262742b9ac83f5a7992ac6fcf506fc5667f61d7756fcf9e

It accepts ordered \(X,Y\). Use maxext=40, with the full scan as final
completeness audit.

Template only:

    scratch/freeze_k16_s4_495_host_atlas_20260730.py
    SHA-256 2c5040378b203db53e8257d5229dd36a14cb30fc5fb350c91ef1d52dfdae8822

Parameterize/delete SPECIAL_TARGETS (line 25), the one seed-4 input (line
114), the self-parent assertion (124--127), and one-parent reconstruction
(146--153). The general freezer uses \(X[6:6436]\) and
\(0x8000\mathbin{|}Y[7:6432]\). It must not inherit S4 protected-facet tables.

## 9. Ready seed-5 self-pair inputs

If inventory selects (5,5), these inputs are ready:

    scratch/k15_repeatfree_parents_20260730/k15seed_5.word
      4e9afded73e1ebad4c53408839e755e15e89ce0ed7888cf788c6db1a92bf2ca6
    scratch/k16_triwindow_rf495_lead_20260730/model/model.map.json
      af3818bcc249b84cb3f99e8fd0b90aca7c4031e57bd2013570514beb4377a6b0
    scratch/k16_triwindow_rf495_lead_20260730/model/model.stats.json
      62561f184eafe8d97ee8e8e9c9048d69ce2cf5841be0c91eafe1f03477149664
    scratch/k16_triwindow_rf495_lead_20260730/lead_score3.cells
      6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
    scratch/k16_rf495_triwindow_score3_20260730.word
      9771f928d2a405308eabbbc780a2f810f77d8faef4f10d56cbb4e50381f518d6

The map has 70 residual targets, 395 shapes and 6,081 raw providers. The
incumbent covers 65,532 masks and has exactly

    0x18e7, 0x3de7, 0x9e20.

The cap audit authenticates this map and its 227 full useful unlabelled
signatures. The new atlas must still emit and compare all 6,081
target-labelled rows.

rf495_source_provider_atlas.audit.json is not a substitute: it is a
source-relative one-cell/service atlas for the three holes, not a complete
one-provider-per-residual-target atlas.

## 10. Boundary

This note proves the schema, completeness criterion, same-support reduction
and maximal-core handoff. It does not choose the inventory winner, solve the
70/73-target system, or change the K16 bracket.
