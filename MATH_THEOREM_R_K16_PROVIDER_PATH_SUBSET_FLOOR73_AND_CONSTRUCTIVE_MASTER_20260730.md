# K16 provider-path subset theorem: floor 73 and the first live connector master

Date: 2026-07-30  
Status: proved solver-independent lower bound in the frozen additive seam
catalogue; exact constructive reduction at equality 73; finish-chain patch
audited solver-free.  No radius-73 carrier or `K=16` word is claimed.

## 1. Frozen class

The source factor is

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

and the authenticated seam catalogue is

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

It has `12,870` transition ports, `211,604` nonold direction-coherent
positive-collar-safe seams, and `5,425` provider seams.  The defect bank
consists of 45 zero-baseline lower-`q2` targets and 48 zero-baseline fixed
upper-`q3` targets.

The theorem concerns a balanced selection using this source-relative
`q<=3`/upper-width-four provider classification whose isolated
seam gains cover all 93 targets.  This condition is necessary in the
four-separated additive `q<=3` master.  It is not asserted for an unrestricted
nonseparated trade, where a multi-seam window may create a target absent from
every isolated seam signature.

The older combined `WIDTH45` model uses the same physical seam columns but
classifies 150 further seams as width-five singleton providers.  That changes
the provider digraph and its strong components.  The floor 73 does not
automatically transfer to that combined provider classification.

## 2. The 33-target path-subset certificate

Let `G` be the directed graph of provider seams on the transition ports.  The
following 33 defects form the certified subset `E`:

```text
33609 34069 34450 35370 35461 36132 36969 37389 37972 38154 39496
41170 41285 41633 42010 42115 43089 43176 43540 46224 46811 49572
49802 50498 51252 51462 53410 53584 53825 54312 56173 59680 60854
```

### Lemma 2.1 (provider cycles miss `E`)

No provider arc internal to a strong component of `G` hits a member of `E`.
Hence every provider-only directed cycle misses `E`.

#### Proof

Every directed-cycle arc is internal to one strong component.  The exact
catalogue replay checks all 5,425 provider arcs and finds zero internal arcs
with an `E` hit.  The fresh audit records

```text
internal_target_subset_provider_arcs = []
```

as a literal list, not only a count.

### Lemma 2.2 (two targets per provider path)

Every physical provider path hits at most two distinct members of `E`.

#### Proof

Contract the strong components of `G`.  The condensation has `12,804`
vertices and `5,350` ordered pairs and is acyclic.  For every ordered pair,
retain every distinct physical-seam `E`-hit mask.  Starting with mask zero at
every component, propagate exact unions through the condensation DAG.

Motion inside a strong component is granted for free.  This can only enlarge
the family of paths, since entry/exit compatibility and vertex-disjointness
are discarded.  Thus the dynamic program is an over-approximation of
physical provider paths.  It has `14,300` exact union states, and its maximum
mask cardinality is two.  Therefore every physical path also hits at most two
members of `E`.

The displayed maximizing relaxed path uses seams `194796` and `165933` and
hits `60854` and `59680`, showing the bound two is attained in the relaxation.

## 3. Sharp current seam floor

### Theorem 3.1 (nonprovider floor 17; total floor 73)

Let a balanced selected port permutation service all 93 defects.  If `p` of
its seams are providers and `z` are nonproviders, then

\[
                       p\ge56,qquad z\ge17,
                       \qquad p+z\ge73.              \tag{3.1}
\]

#### Proof

The independently audited provider edge-cover theorem gives `p>=56`.

Delete the `z` nonprovider arcs from the selected port cycles.  What remains
is a union of provider cycles and at most `z` nonempty provider paths.
Provider cycles miss `E` by Lemma 2.1, and each provider path covers at most
two members of `E` by Lemma 2.2.  All 33 members must nevertheless be
covered, so

\[
                         33\le2z.
\]

Thus `z>=ceil(33/2)=17`; adding `p>=56` proves (3.1).

Within the frozen `q<=3`/upper-width-four classification, this supersedes the
earlier additive floors 66 and 70.  It uses no cut
separation, physical reverse-edge, q1, survivor, residence, or arbitrary-upper
row beyond the initial isolated-seam service premise.

An equivalent independently generated rational dual assigns weight `1/2` to
the 33 displayed targets and zero to the other 15 cycle-unserviceable targets.
Exact replay over all relaxed provider-path masks verifies total path weight
at most one.  Its old status string under-read `33/2` as a weaker floor; the
fresh subset audit records the correct integer ceiling 17 directly.

## 4. Equality normal form at radius 73

### Theorem 4.1 (provider shape and 17-path profile)

At radius 73 necessarily

\[
                         p=56,qquad z=17.            \tag{4.1}
\]

The 56 providers have exactly one of two service shapes:

1. 37 defect-disjoint two-hit providers plus 19 one-hit providers;
2. 36 defect-disjoint two-hit providers, one two-edge star on three defects,
   plus 18 one-hit providers.

Deleting the 17 nonproviders leaves exactly 17 nonempty provider paths and
some provider cycles.  Consequently no two selected nonproviders are
consecutive.  If `Q_i` is the set of distinct `E` targets hit by path `i`,
then exactly one of the following occurs:

```text
|Q_i| profile 2^16 1, no repeated E target; or
|Q_i| profile 2^17, exactly one repeated E-target occurrence.
```

#### Proof

The provider shape is the equality case of the 93-vertex edge-cover theorem:
18 pair-graph-isolated targets force at least 18 singletons, while 56
providers force 37 or 38 two-hit seams.  Essentiality makes the selected
two-hit graph a star forest, yielding precisely the two cases.

Sixteen provider paths cover at most 32 members of `E`; hence deleting 17
nonproviders must create exactly 17 nonempty paths.  Put

\[
 \Delta=\sum_{i=1}^{17}(2-|Q_i|),\qquad
 \Omega=\sum_i|Q_i|-33.
\]

Then `Delta+Omega=34-33=1`.  Both terms are nonnegative.  This gives exactly
the two displayed profiles and also proves every path hits at least one
member of `E`.

## 5. Exact constructive master at the first live radius

The equality structure eliminates all `211,604` seam variables from the
first stage.

### 5.1 Provider skeleton

Use one Boolean for each of the 5,425 providers.  At every transition port
record Boolean provider indegree and outdegree, their union `c_v`, and the
path-start/end indicators.  Enforce

\[
 \sum y_a=56,qquad
 \sum s_v=\sum t_v=17,qquad
 \sum c_v=73,                                        \tag{5.1}
\]

all 93 defect rows, every cyclic four-transition separation row, and every
physical provider reverse-edge row.  The 33-target theorem implies the exact
path profile of Theorem 4.1; it can be used as a redundant propagation
constraint or as a path-column branching rule.

### 5.2 Seventeen-by-seventeen connector circulation

For a fixed skeleton, let `s_1,...,s_17` and `t_1,...,t_17` be its starts and
terminals.  Retain `ij` when the catalogue contains the zero-hit seam
`t_i->s_j`.  Binary connector variables satisfy

\[
               \sum_jz_{ij}=1,qquad\sum_iz_{ij}=1.  \tag{5.2}
\]

There are at most 289 variables.  Add physical reverse-edge conflicts and
the complete signed occurrence rows through `q=3`:

\[
 \mu^0_\alpha-sum_{v:c_v=1}D_{v\alpha}
 +\sum_{a:y_a=1}A_{a\alpha}
 +\sum_{ij}A_{ij,\alpha}z_{ij}\ge1.                 \tag{5.3}
\]

The pure assignment rows are integral, but (5.3) and reverse-edge conflicts
destroy the ordinary matching guarantee.  Endpoint Hall is therefore only a
necessary test; the connector variables remain binary.

### 5.3 Finite Benders schedule

For each provider skeleton:

1. solve the exact connector problem;
2. if connector-infeasible, lift a Hall cut when available, otherwise block
   only that provider skeleton;
3. if `q<=3` succeeds, enumerate connector assignments and physically replay
   all lower depths and arbitrary upper widths;
4. block only each replay-failing connector assignment until the skeleton is
   exhausted.

The sets of skeletons and connector assignments are finite, so exhaustive
termination is a proof inside the frozen radius-73 separated class.

The prepared H100-only driver is

```text
scratch/solve_k16_radius73_provider_path_benders_20260730.py
```

It authenticates both the binary ledger and source-factor hashes, exposes the
selected seam list at top level for the independent binary checker, and has
explicit worker and address-space caps.  It has been syntax-checked but not
launched.  The radius-66 driver was deliberately retired after Theorem 3.1.

For radius above 73, first keep `z=17` and increase provider count; this
retains the 17-by-17 endpoint problem.  Only then increase `z` and permit
zero-length provider blocks representing consecutive nonproviders.  This is
an exact search schedule, not a claim that the `z=17` strata are feasible.

## 6. Finish-chain patch

The independently audited carrier-to-word patch fixes:

1. the keyword-only `linearize_even_ct_cycle` call;
2. the exact cut law: deleted seam `p=(T_p,T_(p+1))` gives forward start
   `p+1` and reverse start `p`;
3. fixed-path dispatch (`path`, not a falsely relabelled `cycle`);
4. the compiler scope: at most two missing lower-`q1` targets are merged into
   exact boundary-SDR rows, while every arbitrary-upper loss is hard.

The upper assertion has a short proof.  If `D^dA=T`, a source interval of
length at most `d` lies in one rank-`r` middle window and cannot have upper
rank.  A longer source interval has the same union as the corresponding
middle interval.  Thus an upper target absent from the linear middle path
cannot be recovered at the source boundary.

Audited source files are

```text
scratch/k16_finish_chain_patch_20260730/ct_handoff.py
scratch/k16_finish_chain_patch_20260730/cutscan16.py
scratch/k16_finish_chain_patch_20260730/comp3.py
scratch/k16_finish_chain_patch_20260730/sandwich2.py
scratch/test_k16_finish_chain_integration_20260730.py
```

The final adapter uses `middle_path` as the direct COMP3
JSON key; `sandwich2` remains only a sound positive-witness fallback because
its restricted host catalogue is not a completeness theorem.  The patched
COMP3 route is authoritative.

The patch is installed both in the local `opusproblem/work` directory and in
`~/or15/work` on the H100 host, with recoverable
`.pre_finish_patch_20260730` backups.  Installed hashes are

```text
ct_handoff.py  ff85c33f19901db576670a6485814d0986e4640062bff313853217502176e831
cutscan16.py   fa44126112fd9c604e15541435ae6f6d9dececf0581bf0dd96f6ce375d2b72b9
sandwich2.py   126173c22262c51f90c3e6740b31484d635fb9b9c6f94f60e7d46e3a2ad6b098
comp3.py       27299d722bc78b4bf14f62ceb50d210e9e762f6b71f2270bd8b4c5ff1ba55bb0
```

Solver-free checks give

```text
PASS_K16_FINISH_CHAIN_INTEGRATION
26 legacy COMP3 tests: OK
```

No compiler solve was run.

## 7. Mandatory positive replay

A radius-73 `q<=3` endpoint still must pass, on one common physical
chronology:

1. exact middle ownership and simple Johnson edges;
2. four-separation, collars, and positive residence four;
3. every fixed lower depth;
4. every arbitrary-width upper union, including multi-seam windows;
5. required connectivity/voltage and a legal linear cut;
6. exact integrated `COMP_3`, including literal source `{z}=32768`;
7. independent replay of the fresh `12,873`-letter word.

## 8. Fresh authoritative certificate

```text
scratch/audit_ad_k16_provider_path_subset_floor73_20260730.py
  SHA-256 fc7413559ee1de8653eccb49c86a2f41b7e3fb5f39d077d1cd7fa451221b13e5

scratch/ad_k16_provider_path_subset_floor73_v2_20260730.audit.json
  SHA-256 00404a022a84cefc4249930726775ccb57a57cc75a2be0098a4499dca2fe24fd
  payload  225f9e86c8b156dabc519e7f24a5a61dffa5b34eb194a203faa53c6ab1d2b385

scratch/ad_k16_provider_path_subset_floor73_v2_20260730.resource.txt
  SHA-256 6ffd86ed6619ebbbc098f7aba03656fa5bbfba154cdfceb35fcf60f8d6d1400a
  one CPU, 3.03 seconds wall, 346,952 KiB maximum RSS, exit 0
```

The current exact boundary is therefore: the frozen `q<=3`/upper-width-four
separated additive class has no repair below radius 73.  At equality,
construction is equivalent
to a 56-provider, 17-path skeleton with one of two defect-cover shapes and a
binary 17-endpoint connector circulation.  Existence at radius 73, all-depth
survival, and compilation remain open.
