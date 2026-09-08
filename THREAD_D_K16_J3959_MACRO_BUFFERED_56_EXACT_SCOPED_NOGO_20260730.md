# Exact j3959 macro-buffered support-5/6 census

Date: 2026-07-30

Status: **proved scoped no-go; not a K16 no-go**.

This note closes the smallest fixed-endpoint support-five/support-six
path-replacement class around the frozen `j=3959` chronology after adding
the full atlas of 5,166 alternative upper-service blocks.  Every row is
target-multiset preserving, uses the direct `6879--Y` witness for `6f79`,
and either has no external exit or one retained provenance ray containing
one, two, or three buffer vertices.  No chronology in this class satisfies
the exact maximal-envelope equations at the scalar deadline, so no Hall
claim is reached.

## 1. Frozen inputs

```text
target
  scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
  SHA edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee

macro atlas
  scratch/k16_j3959_alternative_upper_service_blocks_20260730.audit.json
  SHA 2f1b37317f7ad99271a459647aea58fdd41d863efa23f8f315336c08ffefb101
  payload a736c39b447d4fd9bbcaf77d7a8058ae3157bf6fad7f75107db159796378d4f3
```

The target has length 12,873, exactly 12,870 distinct rank-eight masks,
flats at `6433,12869,12871`, scalar capacity 32,176, exact maximal-envelope
replay, and upper holes

```text
4e79, 6f79, ca79, ea79, eb79.
```

Every atlas row is the ordered block

\[
 M=(V_0,V_1,V_2,\mathtt{4a79},\mathtt{4e39},\mathtt{4d39})
\]

and satisfies

\[
\begin{aligned}
V_2\vee\mathtt{4a79}&=\mathtt{ca79},\\
V_1\vee V_2\vee\mathtt{4a79}&=\mathtt{ea79},\\
V_0\vee V_1\vee V_2\vee\mathtt{4a79}&=\mathtt{eb79},\\
\mathtt{4a79}\vee\mathtt{4e39}&=\mathtt{4e79}.
\end{aligned}
\]

The final edge `4e39--4d39` retains the lower provider.  All 5,166 blocks
are internally depth-two resident.  They are not assumed to have a valid
outer collar.

## 2. Exact red/blue path normal form

Collapse each adjacent flat pair to obtain a 12,870-vertex path (P).
For one macro and one of the 56 masks (Y) with

\[
 Y\subseteq\mathtt{6f79},\qquad
 Y\vee\mathtt{6879}=\mathtt{6f79},
\]

force the undirected forest

\[
 F=E(M)\cup\{\mathtt{6879}-Y\}.
\]

Write (F_0=F\cap E(P)) and (F_+=F\setminus E(P)).  Every edge in
(F_0) is protected.  A support-(k) row, (k\in\{5,6\}), consists of
(k) red base edges (R\subseteq E(P)\setminus F_0) and a return graph
(J), where

\[
 d_R(v)\ge d_{F_+}(v),\qquad
 d_J(v)=d_R(v)-d_{F_+}(v).                         \tag{2.1}
\]

Loops, repeated returns, old base edges, and forced returns are rejected.
The graph

\[
 (E(P)\setminus R)\cup F_+\cup J                 \tag{2.2}
\]

must be connected.  Equations (2.1)--(2.2) preserve every vertex degree,
so connectedness is necessary and sufficient for one fixed-endpoint
Hamilton path.  The undirected formulation automatically includes both
traversals of (M); this matters, since most noncanonical completions use
the reverse traversal.

The optional buffer is one endpoint ray.  Starting at one of

```text
V0, 4d39, 6879, Y,
```

retain exactly one to three source-path vertices and cut the far exit edge.
The incident cuts still pay all forced degrees.  This definition is exact
for the declared one-ray class.  It does not include two simultaneous rays
or an arbitrary detached packet.

The detailed necessity/sufficiency proof is

```text
scratch/threadD_k16_j3959_macro_buffer_path_normal_form_20260730.md
SHA a14e2ee05d89fedfcecfd7e280d2f5d702f8caa62fb3dc9cce071131cf3a6632.
```

## 3. Incidence-cover compression of the 5,166-block atlas

For a forced pair let (d=d_{F_+}).  Vertices with (d(v)=2) force both
incident base cuts.  After those cuts, let (U) be the unsatisfied
demand-one vertices and let (H_U) be the allowed base-path graph induced
by (U), with protected edges deleted.  Then the minimum number of red
edges needed even before returns is

\[
 k_{\min}=|M_2|+|U|-\nu(H_U),                     \tag{3.1}
\]

where (M_2) is the set of distinct mandatory base cuts.  Formula (3.1) is
both a lower bound and an attainable edge cover because (H_U) is a union
of paths.

The complete (5166\cdot56=289296) audit gives

| (k_{\min}) | pairs |
|---:|---:|
| 4 | 1 |
| 5 | 55 |
| 6 | 310 |
| 7 | 17,050 |
| 8 | 4,855 |
| 9 | 267,025 |

Thus only 366 pairs can occur at support at most six.  The 56 canonical
pairs use

```text
M0 = eb60,ea61,ca71,4a79,4e39,4d39.
```

Every one of the 310 noncanonical pairs is forced to `Y=4f29` and exactly
six cuts.  Its complete core has 589 red sets, 1,767 legal return rows, and
800 connected paths on 301 macros; nine macros have no completion.  Of the
800 paths, 297 traverse the macro forward and 503 in reverse.

Every noncanonical completion has two returns and four distinct residual
outside endpoint occurrences.  Therefore a phrase such as “three buffers”
cannot be interpreted as “at most three outside endpoints”; that
interpretation would silently erase the entire new macro core.  The
one-to-three restriction in this theorem refers only to the optional
retained provenance ray.

The independent occurrence-level audit is

```text
scratch/audit_threadD_k16_j3959_macro_forced_edge_core56_20260730.py
  SHA ec0d307857600df51ae0163addc258122b3d52b0aa892ab158e5906bebc0acac
scratch/threadD_k16_j3959_macro_forced_edge_core56_20260730.audit.json
  SHA 164517abd99394678a34ad994026697a2ac1658a7c8eaa7ea17f88e960087bf3
  payload f36008b563c17bd425f56293ef7d53d8d507c084106b4f38f9be2df14e440d31.
```

## 4. Full native census

Across all 289,296 macro/child pairs, the exact one-ray selector census is

\[
42\cdot12+7434\cdot15+281820\cdot18=5,184,774.
\]

After forced-degree filtering and red-set fingerprinting:

| class | red templates |
|:---|---:|
| core, support 5 | 114 |
| core, support 6 | 980 |
| one ray, support 5 | 12 |
| one ray, support 6 | 1,356 |
| **total** | **2,462** |

At most six deficit stubs remain.  The 2,462 rows have exactly 28,350
labelled stub pairings, of which 22,841 give legal return-edge sets.  Exactly
6,960 connected witness rows remain, giving 13,920 oriented chronologies.
These are witness rows rather than a claim of global cross-macro graph
deduplication; any duplication only repeats the same negative replay and
does not affect completeness.

The exact gate ledger is

| gate | count |
|:---|---:|
| oriented witness chronologies | 13,920 |
| exact three-flat multiset | 13,920 |
| scalar capacity at least 26,332 | 6,960 |
| exact nonempty maximal envelope | **0** |
| staged named-upper pass | 0 |
| staged all-upper pass | 0 |
| Hall calls | 0 |

The last three zeros must be read in order.  The named upper services are
built into (F); the production executable deliberately invokes the upper
and Hall stages only after exact middle replay.  Since the envelope gate is
empty, Hall is neither run nor needed for this scoped no-go.

The final engine and result are

```text
scratch/threadD_k16_j3959_macro_buffer_pathreplace_20260730.cpp
  SHA 5818f8b9e725f7ef58ad195a23efef1bce7d3824c6940a9aa654e03ac0529b60
scratch/threadD_k16_j3959_macro_buffer56_20260730/macro_frozen_result.json
  SHA d80401ba8403531144d3f66e81361a42583ec305a28a2a08f6e46bfbea2ff1a6
scratch/threadD_k16_j3959_macro_buffer56_20260730/
  macro_frozen_out/pre_hall_manifest.tsv
  SHA 76e0f636be916da1a3735477ad3c76b8ed491c2a7d6d1373fb3837c6818d3df1.
```

The H100 run used one CPU, 8.97 seconds wall time, and 4,608 KiB maximum
RSS.  Exit status was zero.  The empty pre-Hall manifest contains only its
header.

## 5. Independent full replay of the noncanonical core

A separate Python implementation reconstructs all 589 red sets, all 1,767
legal two-return rows, all 800 paths, and both orientations.  It recomputes
the maximal envelopes and, more strongly than the staged production run,
runs the arbitrary-width upper oracle on every one of the 1,600 rows.

It reproduces the production counts exactly and proves:

* all 1,600 rows contain the five named upper targets;
* no row preserves every upper target; the collateral upper-hole count is
  between 4 and 16;
* 356 reverse orientations are structurally envelope-exact, but all 356
  fail the scalar deadline;
* no deadline-qualified row is envelope-exact;
* among deadline-qualified rows, the minimum reconstruction defect is 13,
  with zero empty envelope cells.

The best deadline-qualified row has capacity 32,188, thirteen bad rows and
six collateral upper holes.  Its service block begins

```text
a359,ea58,ca59,4a79,4e39,4d39.
```

This separates the obstruction cleanly: reverse traversal can repair the
maximal-envelope equations only by moving the flat phase too far and losing
the scalar budget; the deadline orientation retains budget but has a
positive residence/reconstruction defect.

```text
scratch/audit_threadD_k16_j3959_noncanonical_macro_k6_full_replay_20260730.py
  SHA 87afd4142c1efe22ea34d2cf69b9934d399e08c754d478e9bb4aa4b9fadf1280
scratch/threadD_k16_j3959_macro_buffer56_20260730/
  independent_full_replay_v2.audit.json
  SHA bcdd42454e32301c5454bcfe0e9d6d6bdcdb5f2e5b92ca1684854b43fedfe783
  payload 79b361710da3fca7e5a306abad585f874ff5c0df816a44d9dbaee51ce9870ee1.
```

The independent replay used one H100 CPU, 37.81 seconds wall time and
33,260 KiB maximum RSS.

## 6. Exact conclusion and surviving search gate

The new 5,166-block macro atlas does not rescue any fixed-endpoint
support-five/support-six row in the declared one-ray class.  This conclusion
is stronger than the old canonical O5/O4 no-gos, because all 310
noncanonical pairs that can possibly fit six cuts have now been enumerated
and independently replayed.

It does **not** exclude:

1. support at least seven;
2. two simultaneous external rays or a detached return packet;
3. changed physical endpoints;
4. a longer-width or two-row witness for `6f79` rather than `6879--Y`;
5. a different internal service word, or substitution rather than pure
   target-multiset rethreading; or
6. the independently live depth-three donor-absorber architecture.

The smallest faithful continuation is therefore not another canonical O5
or direct `X x Y` transplant.  It is either a support-seven completion of
one of the 310 incidence-admissible noncanonical macros, or a two-ray/local
donor absorber that can retain the reverse orientation's exact envelope
while restoring at least the lost scalar phase.  Hall remains downstream:
it should be invoked only after such a row passes exact middle replay and
arbitrary-upper survival.

The complete command/resource ledger is
[RUN_MANIFEST.md](scratch/threadD_k16_j3959_macro_buffer56_20260730/RUN_MANIFEST.md).
