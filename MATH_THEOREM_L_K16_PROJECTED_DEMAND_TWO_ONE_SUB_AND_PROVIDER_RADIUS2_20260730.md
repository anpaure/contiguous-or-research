# K16 projected demand-two gate: exact one-substitution and provider-first radius-two exclusions

Date: 2026-07-30

## Theorem, status, and exact scope

Let `W` be the authenticated universal K16 word

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

Delete its zero-based position `p=1`, whose raw value is `0x2800`, and call
the resulting length-12,873 word `D`.  Literally,

```text
scratch/k16_upper12874_delete_p1_optimal_onehole.word
scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649.
```

The two files are identical and equal `W[:1]+W[2:]`.

Project away the new phase coordinate, bit 15:

\[
                 \pi(v)=v\mathbin{\&}\mathtt{0x7fff}.
\]

For a projected word `u` and a nonzero old mask `m`, let

\[
 c_u(m)=\#\{[i,j]:0\le i\le j<|u|,\quad
                    \bigvee_{t=i}^{j}u_t=m\}                 \tag{1}
\]

be the **literal interval-occurrence multiplicity**.  Then:

1. every nonzero old mask has `c_pi(W)(m)>=2`;
2. `u=pi(D)` has exactly one deficient old mask,
   `H=0x2c6d`, and `c_u(H)=1`;
3. no arbitrary replacement of one projected cell, by any mask in
   `0x0000..0x7fff`, makes `c(m)>=2` for every nonzero old mask.

The third assertion is a complete solver-free census.  It includes projected
zero.  This is necessary because a projected-zero cell may later receive
phase tag one and therefore be a nonzero K16 cell.

This is an occurrence-multiplicity obstruction, independent of any choice of
phase tags.  It is not by itself a physical K16 coverage theorem and it does
not exclude an unrelated projected trace or two substitutions whose new
`H` occurrence is genuinely joint.

The 52 `H` installers found inside the one-step domains `I_q` below are only a
strict **demand-admissible subfamily** of the first-provider branch.  An
intermediate edit may create debts that the second edit later repairs, so the
one-step cut `x subseteq I_q` cannot be imposed on it.  The complete first-
provider family instead has 40,216 non-noop edits with `x subseteq H`.  Its
exact second-stage normal form and complete negative production census are
proved below.

## Why demand two is a necessary phase-free condition

For each nonzero old mask `m`, a K16 lift must realize both raw targets

\[
                         m,\qquad m\mathbin\vert\mathtt{0x8000}.
\]

Their witness intervals are distinct because their raw ORs differ.  After
forgetting bit 15, both intervals have projected OR `m`.  Consequently every
phase-tagged K16 lift requires at least two projected occurrences of every
old mask.  This proves the necessity of (1) without making any assumption
about how the tag bits will be assigned.

It also proves `c_pi(W)(m)>=2` directly from the authenticated universality of
`W`.  The exact recurrence below independently reproduces the multiplicities.

## Projection convention and its numerical ambiguity

The distinguished projection deletes bit 15 because the construction treats
that coordinate as the new `z`/phase tag over the old 15 coordinates.  The
multiplicity data alone do **not** identify this coordinate.  As a deliberate
ambiguity audit, delete and compact each one of the 16 coordinates in turn.
For every coordinate:

* the projection of `W` has minimum nonzero-target multiplicity two; and
* the projection of `D` has exactly one target of multiplicity one.

For deleted coordinates 14 and 15, that deficient projected label is
literally `0x2c6d`.  Thus the phrase “project to 15 bits” is insufficient on
its own; the old-coordinate/new-tag convention is part of this theorem's
scope and selects bit 15.  The audit packet records the deficient compacted
label for all 16 choices.

Using the canonical encoding “one decimal line, single spaces, trailing
newline”, the distinguished projected traces have hashes

```text
pi(W):  d8ecb75b0af69252225f09d4e8da3e53006f59babc2b47e05be43cba1f4951aa
pi(D):  23995bd3e5259239e7d4d111dfae80b0ec29f15ef61ed3c4f016ba020e69af39.
```

## Authenticated projected multiplicities

The exact ending-interval recurrence stores, for every right endpoint, each
distinct OR together with its full multiplicity.  Summing those states gives:

| projected trace | length | minimum `c(m)`, `m!=0` | number with `c=1` | number with `c=2` | number with `c=3` | total intervals |
|---|---:|---:|---:|---:|---:|---:|
| `pi(W)` | 12,874 | 2 | 0 | 24,942 | 248 | 82,876,375 |
| `u=pi(D)` | 12,873 | 1 | 1 | 24,943 | 250 | 82,863,501 |

The unique deficient row of `u` is

```text
c_u(0x2c6d)=1.
```

The two literal `0x2c6d` intervals of `pi(W)` are the inclusive zero-based
intervals

```text
[1,4] and [6439,6442].
```

After deleting `p1`, the sole remaining occurrence is

```text
[6438,6441].
```

The interval totals in the last column equal `n(n+1)/2`, an independent
counter identity for the complete recurrence.

## Exact one-substitution identity

Fix a projected position `q`.  For every mask `a`, let `L_q(a)` be the number
of suffixes of `u[0:q]` whose OR is `a`, and include the empty suffix once at
OR zero.  Likewise, let `R_q(b)` count prefixes of `u[q+1:n]`, including the
empty prefix once at OR zero.  For a prospective replacement value `x`, set

\[
 N_{q,x}(m)=
   \sum_{a\vee x\vee b=m}L_q(a)R_q(b).                       \tag{2}
\]

Every interval counted in (2) contains `q`, and every interval containing
`q` is represented by one unique left-suffix/right-prefix pair.  Therefore
`N_{q,x}(m)` is exactly the new crossing multiplicity of `m`.  In particular,
the old crossing multiplicity is `N_{q,u_q}(m)`.  The number of avoiding
occurrences is

\[
 A_q(m)=c_u(m)-N_{q,u_q}(m),                                 \tag{3}
\]

and the exact post-substitution multiplicity is

\[
 c_{u[q\leftarrow x]}(m)=A_q(m)+N_{q,x}(m).                  \tag{4}
\]

Define the exact occurrence demand

\[
 d_q(m)=\max\{0,2-A_q(m)\}.                                  \tag{5}
\]

Equations (4)--(5) prove the necessary-and-sufficient decision criterion

\[
 u[q\leftarrow x]\text{ passes demand two}
 \quad\Longleftrightarrow\quad
 N_{q,x}(m)\ge d_q(m)\quad\text{for every nonzero }m.        \tag{6}
\]

This identity retains interval multiplicities.  It does not merge witnesses
to a Boolean present/absent flag.

## Complete submask cut

If `d_q(m)>0`, at least one required new occurrence of `m` contains the
replacement cell.  Hence `x` can contain no bit outside `m`.  Thus every pass
must satisfy

\[
 x\subseteq I_q,
 \qquad
 I_q=\bigcap_{d_q(m)>0}m.                                    \tag{7}
\]

The target `H` has global multiplicity one and is demanded at every position:
the demand is one outside its sole witness interval and two inside it.
Consequently

\[
                       I_q\subseteq H=\mathtt{0x2c6d},        \tag{8}
\]

whose popcount is eight.  Enumerating every submask of `I_q`, including zero,
is therefore exhaustive.

There is a sharper exact decision.  If `x subseteq I_q subseteq m` and an
outside context `s` obeys `s OR x=m`, then automatically `s OR I_q=m`.
Consequently

\[
                 N_{q,x}(m)\le N_{q,I_q}(m)
       \qquad(x\subseteq I_q,\ d_q(m)>0).                  \tag{9}
\]

Thus the service constraints are simultaneously upward-monotone inside the
entire feasible subcube, and

\[
 \boxed{\ \exists x\subseteq I_q\text{ passing (6)}
       \quad\Longleftrightarrow\quad I_q\text{ passes (6)}.\ } \tag{10}
\]

One literal maximal value per position decides the one-substitution gate.
The full submask enumeration below is retained as an independent cross-audit,
not because the smaller theorem needs it.

The exact position histogram of `popcount(I_q)` is

```text
popcount:    0     1     2     3     4    5  6
positions: 250  1838  4458  4467  1658  199  3.
```

It gives the exact cross-audit row identity

\[
        \sum_q 2^{|I_q|}=90,582
          =77,709\text{ nonzero-value rows}
           +12,873\text{ zero-value rows}.                 \tag{11}
\]

There are 577 no-op rows among these; retaining them makes the census an
at-most-one-substitution census and cannot introduce a false exclusion.

Applying (6) to all 90,582 rows gives

```text
passing rows: 0
status: NO_PASS.
```

Independently, applying (10) to the 12,873 maximal values gives the same zero
passes.  This is the smallest exact solver-free one-cell decision.

## Literal projected zero: additive multiplicity is mandatory

The delete projection has one literal zero cell:

```text
u[6436]=0x0000,
```

coming from raw source cell `0x8000` at original position 6437.  A literal
zero suffix or prefix and the empty suffix or prefix are different interval
choices even though both have OR zero.  Their multiplicities must therefore
be **added** when the state maps are joined.  A dictionary overwrite at key
zero loses one occurrence and corrupts the contexts immediately to the left
and right, notably `q=6435` and `q=6437`.

The frozen audit uses additive merging and then replays every retained
provider state from scratch.  This warning is part of the implementation
contract for both the one-substitution census and the radius-two continuation.

## Exact 52-row demand-admissible `H`-provider subfrontier

The cut (7) is complete when the same edit must satisfy every demand and be a
final one-step pass.  Among those one-step-domain values, exactly 52 rows
restore `H` to multiplicity at least two.  They use only three positions:

```text
q=0:     16 rows
q=6437:  32 rows
q=6442:   4 rows.
```

Every subfamily provider was fully replayed on all 32,767 old nonzero masks.
Each listed residual target has the displayed multiplicity zero or one, and
every unlisted target has multiplicity at least two.  The exact packet
partition is:

| first position | first projected values | row count | exact `mask:count` residuals |
|---:|---|---:|---|
| 0 | `0x0800 | s`, `s subseteq 0x0069` | 16 | `0x4879:1, 0x6879:1` |
| 6437 | `0x0869,0x0868,0x0849,0x0848,0x0829,0x0828,0x0809,0x0808` | 8 | `0x2879:0, 0x287d:0` |
| 6437 | the other 24 submasks of `0x0869` | 24 | `0x2879:0, 0x287d:0, 0x4879:1` |
| 6442 | `0x0009,0x0008` | 2 | `0x1009:1,0x142d:1,0x146d:1,0x346d:1,0x5429:1,0x542d:1,0x546d:1` |
| 6442 | `0x0001,0x0000` | 2 | the preceding seven plus `0x5629:1,0x562d:1,0x56a9:1,0x56ad:1` |

The second row is deliberately written literally.  Equivalently, its eight
values are the submasks of `0x0869` containing both bits `0x0800` and
`0x0008`.  The third row contains all remaining submasks of `0x0869`.

The intersections of the residual packets, and hence simple upper bounds on
the last-value domains, are respectively

```text
0x4879 (128 submasks),
0x2879 (128 submasks),
0x0879 ( 64 submasks),
0x1009 (  8 submasks),
0x1009 (  8 submasks).
```

These 52 rows are useful as a small exact subfamily, but they are **not** the
complete `H`-provider frontier for radius two.  In particular, the residual
packets in this table cannot justify discarding an edit outside `I_q`: such an
edit may lose an additional target and rely on the second edit to restore it.

## Complete first-provider census: 40,216 rows

For a provider-first two-edit trace, the first edit is required only to make
`c(H)>=2`.  Since every new `H` occurrence contains the edited cell, its value
must obey

\[
                              x\subseteq H.                 \tag{11a}
\]

Unlike (7), no intersection with the other first-step demands is sound here.
Conversely, enumerating all 256 submasks of `H` is a complete value domain for
testing whether the first edit installs `H`.

Let `B_q(s)` be the multiplicity of outside OR `s=a OR b` from a left suffix
and right prefix around `q`, again including empty choices additively.  On the
eight-bit subcube of `H`, define the superset zeta transform

\[
 Z_q(t)=\sum_{s\supseteq t}B_q(s).
\]

For every `x subseteq H`, the exact number of new crossing `H` intervals is

\[
            N_{q,x}(H)=Z_q(H\setminus x).                  \tag{11b}
\]

Indeed, `s OR x=H` holds exactly when `s` contains every bit of `H` absent
from `x`.  The old word has one `H` interval.  Thus the first edit must supply
one new occurrence when `q` is outside `[6438,6441]`, and two when `q` lies
inside that sole witness.  Formula (11b) decides the provider condition
without inspecting any unrelated target.

An independent complete census gives the exact identities

```text
positions * H-submasks, including no-op: 3,295,488 = 12,873 * 256
literal no-ops:                              577
non-noop rows:                         3,294,911
H-installing non-noop rows:               40,216
H-rejected non-noop rows:               3,254,695.
```

Every one of the 12,873 positions has at least one installer.  The `H`-demand
histogram is `1:12869, 2:4`.  The exact histogram of the number of non-noop
installers at a position is

```text
installers:      1   2   4   8  16  32  64 128 160 192 256
positions:   11776  42 159 255 255 198 143  41   1   1   2.
```

The weighted sum of this histogram is 40,216.  All 40,216 positive zeta
queries were also resummed directly from the literal outside-OR bank.  Their
canonical packet SHA-256 is

```text
c9924e384066990155424bb30b5b82d6994b16a33ac9fe362e93c503ed7f4adb.
```

## Exact provider-first radius-two normal form

The provider-first family consists of ordered two-edit traces in which the
first edit is one of the complete 40,216 rows above, so it already restores
demand two for `H`.  The 52-row packet is a strict subfamily of this class.
Provider-first remains a strict, explicitly scoped branch of the arbitrary
projected radius-two ball: a final `H` interval that genuinely needs both
edits need not have a provider-first ordering.

Fix a provider `P=(q,x)` and write

\[
                         u^P=u[q\leftarrow x].
\]

Its complete multiplicity vector need not be recomputed from all intervals.
The exact sparse first-edit delta is

\[
 c_{u^P}(m)=c_u(m)-N_{q,u_q}(m)+N_{q,x}(m).                 \tag{12}
\]

Let `R(P)` be the masks whose right side in (12) is below two.  Their counts
are exactly zero or one.  Unlike the five residual packets of the 52-row
subfamily, `R(P)` is provider-dependent throughout the complete 40,216-row
family.

For a prospective second position `r` and last value `y`, construct the exact
left/right distributions in the **actual first-edited state** `u^P`.  Define
the outside context bank and the new through-`r` multiplicity by

\[
 B^P_r(s)=\sum_{a\vee b=s}L^P_r(a)R^P_r(b),
 \qquad
 N^P_{r,y}(m)
   =\sum_{s\vee y=m}B^P_r(s).                               \tag{13}
\]

\[
 A^P_r(m)=c_{u^P}(m)-N^P_{r,u^P_r}(m),
 \qquad
 d^P_r(m)=\max\{0,2-A^P_r(m)\}.                             \tag{14}
\]

Exactly as in (4)--(6), the final projected trace passes if and only if

\[
               N^P_{r,y}(m)\ge d^P_r(m)
               \quad\text{for every nonzero }m.             \tag{15}
\]

Every possible last value lies in the exact submask domain

\[
 y\subseteq J^P_r,
 \qquad
 J^P_r=\bigcap_{d^P_r(m)>0}m.                               \tag{16}
\]

The maximal-intersection argument (9)--(10) applies verbatim in the actual
first-edited state:

\[
 \boxed{\ \exists y\subseteq J^P_r\text{ satisfying (15)}
       \quad\Longleftrightarrow\quad J^P_r\text{ satisfies (15)}.\ } \tag{17}
\]

Every member of `R(P)` is demanded for every `r`; consequently

\[
                         J^P_r\subseteq\bigcap_{m\in R(P)}m.
\]

Only a sparse target family is needed to construct (14).  A target outside
`R(P)` and outside the labels of old intervals through `r` keeps at least two
avoiding occurrences, hence has zero demand.  Thus the exact active family is
contained in

\[
 R(P)\ \cup\
 \operatorname{supp}\!\left(N^P_{r,u^P_r}\right).           \tag{18}
\]

Equations (12)--(18) give a sound sparse decision procedure: construct the
actual dynamic demand family and test the single literal maximum `J^P_r`.
They account automatically for losses created by the second edit.  Enumerating
smaller submasks is unnecessary.  Testing only `R(P)`, reusing a baseline
marginal context, or grouping by the residual intersection alone would be
unsound.

There is, however, an exact equivalence compression.  Associate to every
ordered provider/site pair `(P,r)` the canonical signature

\[
 \Sigma(P,r)=
 \left(
   \{(s,B^P_r(s)):B^P_r(s)>0\},
   \{(m,d^P_r(m)):d^P_r(m)>0\}
 \right),                                                    \tag{19}
\]

with both lists sorted by mask.  If two pairs have identical signatures,
then (13), (15), and (16) give identical feasibility for every last value
`y`; one submask decision suffices for the entire signature class.  The
mapping back to every represented `(P,r)` must be retained so that a positive
class can be materialized and replayed literally.  This signature is a sound
grouping; equal first residual sets or equal marginal gains are not.

If `r=q`, then

\[
             (u[q\leftarrow x])[q\leftarrow y]
                      =u[q\leftarrow y],                    \tag{20}
\]

which is already one of the radius-one rows excluded above.  Therefore the
genuinely two-site provider-first census may and should require `r!=q`; no
radius-two candidate is lost by this same-site removal.

## Complete provider-first radius-two exclusion

The exact production census is complete and negative.  It first groups the
40,216 providers into 6,540 exact residual signatures.  For a provider `P`,
put

\[
                         K(P)=\bigcap_{m\in R(P)}m.
\]

At a fixed second site, any value serving all first-state residuals is a
submask of `K(P)`.  Replacing such a value by `K(P)` preserves all of its
residual witnesses, so a residual-serving value exists if and only if the
single literal value `K(P)` serves every residual.  This is an exact necessary
service gate, not a heuristic value choice.

Outside the finite non-full-OR halo between the two edit sites, the literal
through-site context bank has already rejoined the baseline bank.  Residual
service can therefore be cached exactly by residual signature and second
site there.  Every halo context is instead reconstructed literally by
subtracting the old first-edit crossing mass and adding the new mass.  At
each service survivor, the engine discards the residual cache, rebuilds the
complete actual dynamic demand family, forms `J^P_r`, and invokes (17).

The 64-of-64 residual-signature shards reproduce the exact global counters

```text
first providers:                              40,216
residual signatures:                           6,540
distinct ordered second-site rows:       517,660,352
raw arbitrary nonnoop second values:  16,962,176,753,984
signature/site cache tests:                84,189,420
literal halo contexts:                      1,542,757
residual-service survivors:                   286,013
residual-service rejections:              517,374,339
exact dynamic maximal-J tests:                286,013
maximal-J no-op rows:                          10,352
passing rows:                                       0.
```

The identities

\[
 517660352=40216\cdot12872,
 \qquad
 16962176753984=517660352\cdot32767
\]

authenticate the complete ordered-site and arbitrary-value envelopes.  The
service partition is `286013+517374339=517660352`.  Every one of the 286,013
survivors received its exact dynamic maximal test; none passed, so no
candidate trace or phase-tag instance was emitted.

It follows that

\[
 \boxed{\text{No projected demand-two radius-two trace exists in which the
 first edit alone installs }H.}
\]

The same-site case is already excluded by (20).  Thus this closes the entire
projected **provider-first** radius-two family, not merely the 52-row
demand-admissible subfamily.

The production ran under the unique H100 directory

```text
/home/amodo/or15/work/laneL_k16_projected_allprovider_grouped64_20260730_b80ea86e
```

with frozen lineage

```text
scratch/search_projection_engine_k16_deletep1_allprovider_service_grouped_20260730.cpp
SHA-256 b80ea86efa7ac01cafd9eab58f023b55d1948f8c103e70a97bfe5057085428c6

scratch/search_projection_engine_k16_deletep1_demand2_one_sub_20260730.cpp
SHA-256 8aadcb1004cf14b5ee03c655e5e6e61df0a78b2651dbf4956b494f7517371daf

executed grouped binary, remote authenticated
SHA-256 d1b1f0e1e8cee311a2e3d0d30636a84760131d987c8bd0a9ccb746cf0c360ef1

scratch/l_k16_projected_demand2_all_h_providers_20260730.tsv
SHA-256 470ec35113a37e0a58612d64df9b56fc16d8f9f1baeeb6cafc6faf59017636d3
```

The fail-closed 64-shard merger checks the signature-modulo partition, all
40,216 provider rows, all 6,540 signatures, every survivor TSV, all global
counter identities and the empty candidate set:

```text
scratch/audit_projection_engine_k16_deletep1_allprovider_radius2_shards_20260730.py
SHA-256 1c9e2a71bef451059a66e7fcbfca87220ab6afe5e8ebe4de2df6c26c6b9d7563

scratch/l_k16_projected_allprovider_grouped64_20260730/merge.v2.audit.json
SHA-256 c24c0b196899de5127c71fddad2212c94766bc6576eda41ba178306baa269523
payload/canonical SHA-256 b3ac7e0a45fb0052d47c25a954ede32060ce4797d39158a7d1325dd20a0dddac.
```

A separate fail-closed cross-audit joins these signature shards to an
independently partitioned 64-shard contiguous-provider residual-service
census.  For every provider index `0..40215` it proves that the contiguous
report's `service_feasible_sites` is exactly the grouped survivor TSV's
`survivor_count`.  Both families independently sum to 517,660,352 sites and
286,013 survivors.  The common per-provider service vector has SHA-256

```text
e23277c707e7763d68145cb956f9372a4abe3a89b8c25e94364da81effa4cf41.
```

Its artifacts are

```text
scratch/search_l_k16_projected_all_provider_residual_service_shard_20260730.cpp
SHA-256 25a2e2fe0d2ddf51f2853cd57e27542464c9a65d1ce51c7ba095a40fe6dc13cc

scratch/audit_l_k16_projected_residual_service_vs_grouped_survivor_shards_20260730.py
SHA-256 803ed61ade92e60ba3e427dd8823e27cf725169dba42f32685ed5e9534d25f5c

scratch/l_k16_projected_allprovider_grouped64_20260730/service_cross_audit.v2.json
SHA-256 9fca93e04c9a0357b1c4cc7e6780179a6293db678bb1504e36db980e498c184d
payload SHA-256 ec4617410bd8bb32651eae70986cffdfaccd18bc1e779e7bd02615b983b0cbe2.
```

This cross-audit authenticates the complete residual-service reduction; it
does not claim to be a second recomputation of all 286,013 dynamic maximal-J
decisions.

That final dynamic layer has a separate independent replay.  It does not use
the production engine's far cache or halo-update arithmetic.  For each of the
321 first-edited states having at least one service survivor, it materializes
the full projected word, rebuilds all counted ending and starting banks, and
constructs every retained second-site context directly.  It then rebuilds the
complete active demand family and tests the literal maximal `J` on all 286,013
contexts.  Any positive row would receive a full 32,767-mask replay; there are
zero positives.

The independent replay exactly matches all 64 production per-shard test,
no-op, pass and histogram packets, as well as every global histogram.  Its
global counts are again

```text
first-edited states replayed:     321
dynamic second-site contexts: 286,013
maximal-J no-ops:               10,352
passing rows:                        0.
```

It ran for 108.58 seconds with maximum RSS 143,352 KiB under

```text
/home/amodo/or15/work/laneL_k16_projected_allprovider_dynamic_replay_20260730_176c0e99
```

and has frozen lineage

```text
scratch/audit_projection_engine_k16_allprovider_286013_dynamic_replay_20260730.py
SHA-256 176c0e99de63f65573a0fd3fd89a367cf84d5d8143e88318e70c108056aae04e

scratch/l_k16_projected_allprovider_grouped64_20260730/dynamic_replay.audit.json
SHA-256 c338848177ed64267bb8d2af17403f822f236e644dad7e9503aaad96580e5eff
payload SHA-256 506ecf98b26e4da6727906ea6f178939126a7952c3ef27378fd87b858e7cf942

scratch/l_k16_projected_allprovider_grouped64_20260730/dynamic_replay.resource.log
SHA-256 0e3ca50927ebb16e4001caab43c12418a0b06746514fff5487a3f1673565ce4c

scratch/l_k16_projected_allprovider_grouped64_20260730/dynamic_replay.stdout
SHA-256 89453666163455014ffc500dcba1b48373fc06e56db3b6d2bad01e2504fb734a.
```

The 40,216-row residual catalogue itself has both an H100 artifact audit and
an independent local reconstruction:

```text
scratch/l_k16_projected_demand2_all_h_providers_h100_20260730.audit.json
SHA-256 cd8aab0675fa941aa1af3780cd43763d8e4586372bde0d17cf2c438b8276b098
payload SHA-256 ffd29c6aacf56da4b659649e99179d4f797915b175ce1910371684d0f7750efa

scratch/audit_l_k16_projected_demand2_all_h_providers_20260730.py
SHA-256 6e69ebc882a5c8c9702f3e907497a8c184df7aa1b348a3f91d1a682ef580e030

scratch/l_k16_projected_demand2_all_h_providers_20260730.audit.json
SHA-256 2a7795b4a201c140f2e95957561946a8e1cc8f11088888b9d2153940d45bd116
payload SHA-256 3af3051abf91ed04dfd6496ef3087b2fe95a2631bd1e9a613c9cbacfabd0097c.
```

A deterministic static audit of the grouped engine checks 1,638,400 sparse
first-delta target rows, 1,581 literal halo contexts, 292 far-bank equalities,
1,873 service rows, 64 maximal-value equivalences by literal submask brute
force, and the signature partitions at shard counts 1, 7, 64 and 7,000:

```text
scratch/audit_l_k16_grouped_provider_engine_light_20260730.py
SHA-256 1f7df5f11a42c828e852a4a63bd74190f7f31143dc2b316ae1a7420c62ec3cb4

scratch/l_k16_grouped_provider_engine_light_20260730.audit.json
SHA-256 7bbd33e48e049bee654395062c347006ccd7ff4fd831dc1f90e8aee2dc15d406
payload SHA-256 86dc529b4092ccefa51bfbdbc813250cf2cf4415f1de4087611405cf7e3f1321.
```

For completeness, the earlier 52-row demand-admissible subbranch was also
exhausted literally before the complete grouped run.  It covered 669,344
distinct second sites and 3,250,664 nonnoop dynamic-intersection values, with
zero passes.  It is now strictly subsumed by the result above.  Its frozen
lineage is

```text
scratch/search_l_k16_projected_demand2_provider_first_radius2_20260730.cpp
SHA-256 6d633c6c09c9dd43b50d8a51e9b8f96e0c2bb250dd810809fbcfc8a1304ce43b

executed scoped binary, remote authenticated
SHA-256 6b55fe1daa2df872e2d3fd0b85c05f6f8158cfce3876c8a59c40d301e9d296cb

scratch/l_k16_projected_demand_admissible52_radius2_20260730.frontier.tsv
SHA-256 1dcece999136eaa8fa2589e71e6094959c498ef1855c7e349e13efbbec7b156f

scratch/l_k16_projected_demand_admissible52_radius2_h100_20260730.audit.json
SHA-256 936831e429d3faf48cf156e7bc2cf52b575781b192f73fcd332fbc6f0165b019.
```

The complete negative result does **not** cover cross-only pairs for which
neither edit alone installs `H` but their joint geometry creates the required
new `H` occurrence.  Nor is projected demand two sufficient for consistent
16th-bit phase tagging.  These remain separate gates, so this theorem changes
no K16 bound.

## Independent one-substitution audit and hashes

The standalone independent implementation authenticates both raw words,
recomputes both projected traces, checks all 16 coordinate projections,
derives every demand and submask domain, exhausts all 90,582 rows, and fully
replays all 52 demand-admissible providers.  Its additive zero-state
assertions are fail-closed.

```text
scratch/audit_l_k16_projected_demand2_one_sub_independent_20260730.py
SHA-256 0ba641fbc3306666542ec8383e2cc7423a9ade028192ba6625988b3ae2aaa16e

scratch/l_k16_projected_demand2_one_sub_independent_20260730.audit.json
SHA-256 afe84e275b15fd2b89be66b13a55044097628a5ee845af6f6daf6dd1ee18227e
payload SHA-256 d601e428d6ee2d33632c069cc9d3e4bcd77921a3a4ced7296a06bdbfb1e6a6c9.
```

A second independent light audit discards the one-step `I_q` cut and checks
every first position and every `x subseteq H`.  It proves the complete 40,216
count by the superset-zeta formula, directly resums every positive query, and
records the full per-position histogram and counter identities.

```text
scratch/audit_l_k16_projected_complete_H_provider_count_20260730.py
SHA-256 79f8372145b123546ffa8c4557f907981767eae8828e1fa282265c9dcf2238a0

scratch/l_k16_projected_complete_H_provider_count_20260730.audit.json
SHA-256 42da9a6ff567dd256bcd6196cd4d500caac392e23d4588531dc5b4f88fc27ed5
payload SHA-256 c832c2979f237c46d0128e00ead106f7b35330c5d887b1c47c51af3713be1167.
```

The maximal-intersection audit independently reconstructs the counted context
banks, checks additive literal-zero multiplicities, proves the coordinatewise
monotonic implication, and replaces the 90,582-value one-cell enumeration by
exactly 12,873 literal maximal tests.  It again finds zero passes.

```text
scratch/audit_l_k16_projected_demand2_maximal_intersection_20260730.py
SHA-256 c75f7bb68dce23069759eeb9bdf93cfe56d75238dbb06f27fb3bca8ff2c9665c

scratch/l_k16_projected_demand2_maximal_intersection_20260730.audit.json
SHA-256 5956691b76c1b0579323c022e4e5856b5cf0bcd75aea3af89217c29faaae7865
payload SHA-256 7ab9ee326a69bc76da2a8743942015fdaf3f4bc88e4342b9ed8870396eaac561.
```

The audited conclusion at this stage is therefore exactly:

\[
 \boxed{\begin{gathered}
 \text{No one-cell projected substitution passes demand two, and}\\
 \text{no two-cell provider-first projected trace passes demand two.}
 \end{gathered}}
\]

Cross-only projected pairs and exact phase tagging remain open.  The global
K16 bracket remains

\[
                        12873\le \nu(16)\le12874.
\]
