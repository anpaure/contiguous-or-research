# Exact `j3959` support-seven core/one-ray census

Date: 2026-07-30

Status: **proved scoped no-go; not a K16 no-go**.

This note closes the fixed-endpoint support-seven extension of the frozen
`j3959` macro-buffered path-replacement family.  It enumerates every
seven-cut core and every row with six incident cuts plus one retained
provenance ray of length one, two, or three.  All 461,244 connected paths
have exactly one deadline-qualified orientation, but none satisfies the
exact maximal-envelope equations.  The next disjoint stratum is the
two-external-cut/two-ray or detached-packet class described in Section 6.

## 1. Frozen inputs and scope

```text
target chronology
  scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
  SHA edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee

macro atlas
  scratch/k16_j3959_alternative_upper_service_blocks_20260730.audit.json
  SHA 2f1b37317f7ad99271a459647aea58fdd41d863efa23f8f315336c08ffefb101
```

Collapse the three adjacent duplicate pairs in the 12,873-row target deck.
The result is a path `P` on 12,870 distinct rank-eight masks.  For an
audited six-row macro `M` and one of the 56 direct children `Y`, force

\[
 F=E(M)\mathbin\cup\{\mathtt{6879}-Y\},\qquad
 F_0=F\cap E(P),\qquad F_+=F\setminus E(P).
\]

Every edge in `F_0` is protected.  The global endpoints and target multiset
are fixed.  The declared census includes precisely:

1. seven red edges in the forced-support incident pool; or
2. six such incident edges plus the exit of one retained source-path ray of
   length one, two, or three starting at `V0`, `4d39`, `6879`, or `Y`.

It excludes a second ray, an arbitrary detached cut, changed endpoints,
substitutions, longer `6f79` witnesses, and different internal macro words.

## 2. Exact incidence compression

At every vertex put `d(v)=d_(F_+)(v)`.  Let `C_inc` be the unprotected base
edges incident with the eight forced vertices, and let `tau(M,Y)` be the
minimum size of a subset of `C_inc` whose incidence degrees dominate `d`.
The complete 5,166-by-56 atlas factors exactly as follows.

| macro/child stratum | pairs | `tau` | `|F_+|` |
|:--|--:|--:|--:|
| canonical `M0`, `Y=4f29` | 1 | 4 | 3 |
| canonical `M0`, other `Y` | 55 | 5 | 3 |
| 310 two-overlap macros, `Y=4f29` | 310 | 6 | 4 |
| same 310 macros, other `Y` | 17,050 | 7 | 4 |
| 4,855 one-overlap macros, `Y=4f29` | 4,855 | 8 | 5 |
| same 4,855 macros, other `Y` | 267,025 | 9 | 5 |

For any seven-cut row write

\[
 C=R\cap C_{\rm inc},\qquad O=R\setminus C_{\rm inc},\qquad o=|O|.
\]

Edges in `O` pay no forced degree.  Therefore

\[
                    \tau(M,Y)\le 7-o.                 \tag{2.1}
\]

Thus the eligible pair counts at `o=0,1,2,3,>=4` are respectively at most

```text
17,416; 366; 56; 1; 0.
```

This is the exact reason the present core/one-ray census is finite, and it
also isolates the next two-external-cut stratum to the 56 canonical pairs.

## 3. Lossless return-port criterion

Removing seven base edges produces eight path intervals.  Contract these
intervals and insert `F_+`.  Reject an `F_+` edge internal to one interval
and reject a cycle, with parallel edges counted as a cycle.  If the
resulting forced quotient has components `K_1,...,K_t`, then

\[
                       t=8-|F_+|.
\]

For every occurrence vertex define

\[
                \delta_R(v)=d_R(v)-d_{F_+}(v).
\]

The residual port multiset has exactly

\[
        \sum_v\delta_R(v)=2(7-|F_+|)=2(t-1)          \tag{3.1}
\]

labelled copies.  A return completion is equivalent to a perfect matching
of these copies such that no matched pair is a loop, a base edge, a forced
edge, or a repeated return, and the return edges connect all `K_i`.  The
component graph then has `t-1` edges and is automatically a tree.  Restoring
the path intervals gives one spanning path with the original endpoints.
Conversely, every valid path yields this matching uniquely as an edge set.

The lossless topological signature is therefore

\[
 \Sigma_{\rm top}(F,R)=
 \left(R;
   \{(v,\operatorname{seg}_R(v),K(v))^{\delta_R(v)}\};F_+\right). \tag{3.2}
\]

Labelled pairings that yield the same return-edge set are deduplicated.
This criterion is what the production quotient test and the independent
occurrence implementation both use.

## 4. Exact census and gate ledger

Across all 289,296 macro/child pairs the exact support-seven census is:

| object | count |
|:--|--:|
| eligible macro/child pairs | 17,416 |
| core red templates | 67,366 |
| one-ray red templates | 10,569 |
| all red templates | 77,935 |
| labelled residual-port pairings | 1,529,025 |
| legal deduplicated return sets | 1,383,497 |
| connected core paths | 310,156 |
| connected one-ray paths | 151,088 |
| all connected paths | 461,244 |
| oriented chronologies | 922,488 |

The independent implementation also partitions the red rows into 46 exact
endpoint-signature classes.  Each representative records all seven cuts,
absolute residual occurrences, cut-segment IDs, forced roles, component
multiplicities, and the ray selector where present.  It is therefore a
lossless return generator rather than a coarse profile count.

The production gate ledger is:

| exact gate | rows |
|:--|--:|
| three adjacent flat pairs, hence `G=0` | 922,488 |
| scalar capacity at least 26,332 | 461,244 |
| exact nonempty maximal-envelope reconstruction | **0** |
| staged five named upper witnesses | 0 |
| arbitrary-width upper complete | 0 |
| pre-Hall rows | 0 |

The phrase “no flat/capacity pass” would be imprecise: every chronology has
the correct flat structure and exactly one orientation of each connected
path passes the scalar capacity threshold.  The empty gate is exact
maximal-envelope reconstruction.  Consequently no Hall call or literal
word claim is licensed in this scope.

For expanded length `n`, let `s_1,s_2,s_3` be the first-copy positions of
the three flat pairs.  Literal depth summation gives

\[
 C_{\rm fwd}=3+\sum_j s_j,
 \qquad C_{\rm rev}=3n-C_{\rm fwd}.                \tag{4.1}
\]

In collapsed coordinates, a marked vertex at position `i` with `b` earlier
marked vertices has `s=i+b`, exactly as used by the engine.  Since

\[
 2\cdot26332>3\cdot12873,
\]

at most one orientation can qualify.  Full literal carrier replay asserts
agreement with (4.1), so this optimization cannot remove a valid row.

## 5. Reproducibility and independent checks

```text
production source
  scratch/threadD_k16_j3959_macro_buffer_pathreplace_support7_20260730.cpp
  SHA 400ced694b2b67adcc760b24718a89148307648dc80e3a98fcaaaffca57dec5c

production result
  scratch/threadD_k16_j3959_macro_support7_20260730/production_final_result.json
  SHA 6c286c394b14a0dcf31aba7d1aceb509a57c2150a4fec3cf7da885dfdbda5c0b

catalogue-only result
  scratch/threadD_k16_j3959_macro_support7_20260730/catalogue_final_result.json
  SHA 64363a287b6f527cb938d64ba86450a9dcd884fb8bff9dceadf03835ac9a6f94

independent occurrence result
  scratch/threadD_k16_j3959_macro_support7_independent_20260730/
    support7_occurrence.audit.json
  SHA 78021cab2adbca3b7a6e2393de35438191521419355a3938e694b42037fe5aed
  payload 1c7bccec7268bf840417285d636d1c037d0942934c231d6f5392525c6f1b3c0b

endpoint-signature theorem
  scratch/threadD_k16_j3959_support7_endpoint_signature_theorem_20260730.md
  SHA af790ca7c9a511219c49b974103fdd5a47da423ccd7fabefa92a1b9b518fe889
```

The independent occurrence run used one H100 CPU for 56.28 seconds and
75,776 KiB RSS.  Production used one H100 CPU for 143.69 seconds and
4,608 KiB RSS; both exited zero.  The empty pre-Hall manifest has SHA
`76e0f636be916da1a3735477ad3c76b8ed491c2a7d6d1373fb3837c6818d3df1`.
The launcher, not the executable, verifies input hashes.  The complete
command and resource ledger is
`scratch/threadD_k16_j3959_macro_support7_20260730/RUN_MANIFEST.md`, SHA
`d4d4f1e4b9e1f168bc91ef32a270ef3e38efce7d36ec1276a3bfb94c972e0a58`.

## 6. Exact next stratum: two rays and detached boundaries

Equation (2.1) leaves only the 56 canonical `(M0,Y)` pairs when two cuts
are external.  Each has a five-edge incident cover `C`.  The complete
two-external-cut quantifier is

\[
 e_L<e_R,\qquad
 e_L,e_R\in E(P)\setminus(C_{\rm inc}\cup F_0),\qquad
 R=C\cup\{e_L,e_R\}.                              \tag{6.1}
\]

A compatible pair of protected provenance rays is tagged `two-ray`; all
other rows are detached.  An intact detached packet additionally has no
edge of `C` strictly between `e_L` and `e_R`, but this is a subfamily, not a
replacement for the general quantifier (6.1).

The endpoint theorem gives exact pre-Hall pruning.  For every oriented path
interval store:

1. its length, flat offsets, incoming-to-outgoing depth map, capacity, and
   exact reconstruction collars containing six expanded masks on each side
   of a seam (or the equivalent pending-row streaming state); and
2. the associative upper monoid

\[
 (O,\operatorname{Pref},\operatorname{Suff},\operatorname{Seen}),
\]

where cross-component intervals are exactly

\[
 \{s\vee p:s\in\operatorname{Suff}(X),
                 p\in\operatorname{Pref}(Y)\}.      \tag{6.2}
\]

Together with (3.2), these summaries decide phase, exact envelope replay,
and arbitrary-width upper survival before materializing a chronology or
calling Hall.  The next search therefore has a finite, proof-safe endpoint
state space; it is not another free buffer search.

The six-mask width is sharp for the raw-collar representation.  An envelope
cell at `j` depends on target rows `j-3,...,j`, while reconstruction of row
`r` uses cells through `r+d_r`, with `d_r<=3`.  Hence row `r` depends on
targets `r-3,...,r+3`.  A seam can affect rows `-3,...,2`, so the union of
their dependency ranges is `-6,...,5`: six masks from each side.  Merely
storing three masks per side is not exact.  When two seams are fewer than
six rows apart, their collars are evaluated jointly rather than treated as
independent tests.
