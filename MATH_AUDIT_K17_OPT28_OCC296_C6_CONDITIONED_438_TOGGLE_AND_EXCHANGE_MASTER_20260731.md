# Audit of the `K17` OPT28 occ296+C6 conditioned toggle bank and exchange master

Date: 2026-07-31  
Lane: H/A, conditioned occurrence base changes plus marked-preserving edge exchange  
Status: **scoped final: exact conditioned catalogue, three bounded master runs, and a strict componentwise outside-face improvement obtained by split-relative two-C6 residence repair plus one provider C6; no edge-disjoint-master no-go, upper-complete carrier, common cap, or `K17` word is claimed**

## 0. Scope and current verdict

This lane is based on the independently authenticated occurrence296+C6
checkpoint

```text
scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
  SHA-256 a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49
```

and not on the older OPT28 owner cycle `a736ef9d...`.  The checkpoint is one
Johnson Hamilton cycle on all `24310` rank-nine owners, has every rank-eight
edge colour exactly once, and contains the frozen `4108`-owner marked path.
Its literal two-bank zipper has

```text
maximal-envelope empty positions                      0
maximal-envelope replay mismatching rows            748
maximal-envelope missing row-bit obligations        776
strict D2 / D3 short runs                       503 / 503
upper holes rank 10 / 11 / 12              1585 / 824 / 116
upper holes rank 13 through 17                        0.
```

The exact face constructed in this lane consists of:

1. either the authenticated zero-toggle base or at most one of `438` labelled
   occurrence toggles, rebuilt as a complete balanced owner factor by a
   conditioned residual b-flow; and
2. the complete marked-preserving, lower-colour-preserving exchange face on
   that checkpoint, with `545721` off-source edge columns.

The raw occurrence rows are **base changes, not fibre circuits**.  A raw row
is never added as an affine marginal delta to the `a47aa9d...` cycle.  Only a
post-b-flow symmetric difference that independently gives a simple
degree-two factor with the exact lower palette is eligible for the exchange
master.

The conditioned catalogue is complete in its declared labelled-toggle scope:
all `438` rows have balanced exact-lower factor certificates, `232` of the
declared representatives are connected, and an independent verifier replays
all rows.  None of the `232` connected representatives preserves the full
standalone residence guard, so exchange compensation is still necessary.

The final scoped verdict has three parts.

1. The unhinted soft-support run, the fully hinted soft-support run, and the
   min-edit run produce no strict guarded upper-frontier improvement over the
   authenticated zero-toggle baseline.  All are bounded searches; none is an
   UNSAT or completeness result for the `545721`-column master.
2. A complete targeted screen around `z2851_c0_p6328` finds an exact
   split-relative pair of C6 circuits that restores the residence guard and
   retains ranks `13`--`17`.  Every residence-passing pair consumes a lower
   colour whose edge was installed by the split, so it lies outside the
   current edge-disjoint split/exchange face.  Its upper tuple is not better
   than the baseline's provider-first tuple.
3. Starting from the best such split-relative two-C6 composite, a complete
   `13960`-packet native support-two C6 shell has a unique guard-passing
   provider packet.  The resulting one-cycle carrier is componentwise no
   worse than the authenticated base in residence and all upper ranks, and is
   strictly better in replay rows, missing bits, and rank-twelve holes.  The
   added provider C6 is edge-disjoint relative to the two-C6 composite, but
   the whole construction remains outside the original 438-toggle master
   because its residence-repair prefix already reuses split-installed
   colours.

This note therefore claims neither an upper-complete carrier nor a common-cap
matching, compiler, or `K17` word.

## 1. The old `441` screen and the exact `438` correction

The old radius-one file

```text
scratch/k17_opt28_complement_radius1_columns_20260731.json
  SHA-256 d2f77df2c97f95f63cb724ad991cd7ae8d3b21b6dbd1f80c34f8df59016da2ac
```

contains `441` alternatives whose changed construction links avoid the
marked macro nodes.  Node-disjointness is weaker than preservation of the
complete frozen marked packet.  Rebuilding all macro signatures and
comparing the full `134` frozen marked component signatures leaves exactly
`438` valid rows.  The three excluded node-disjoint rows are

```text
z= 2883: (component,position) (0,1389) -> (0,4525)
z=14944: (component,position) (0,1808) -> (0,5315)
z=20112: (component,position) (0,1395) -> (0,3910).
```

Thus `441` is the exact count for the weaker changed-link screen, while
`438` is the exact count for full marked-component preservation.  No master
in this lane accepts the three excluded rows.

That theorem is source-relative to the older occurrence choice and factor.
It does **not** say that the same `438` rows are the complete radius-one
neighbourhood of the later occurrence296+C6 checkpoint.

## 2. The transported labelled-toggle face

Let `o_z` be the occurrence retained for lower colour `z` in occurrence296.
For each of the `438` safe old rows, compare `o_z` with the row's labelled
`old` and `new` occurrences.  The induced face around occurrence296 has the
exact partition

```text
current occurrence = labelled old, toggle old -> new       234
current occurrence = labelled new, toggle new -> old       196
current occurrence is a third site, toggle third -> new       8
total                                                       438.
```

The last eight rows deliberately choose the old row's declared `new` site;
they do not enumerate every alternative from the third current site.
Consequently this is an exact **labelled 438-toggle face**, not a claim of a
complete new radius-one census around occurrence296.

Every toggle preserves the selected marked-component signatures at the
macro level, but it changes the fixed macro forest, its port-demand vector,
and generally invalidates the saved residual `U` assignment.  Its raw fixed
edge differences therefore have no independent factor semantics.

## 3. Conditioned residual b-flow and the exported column

For each labelled toggle `t`, the producer performs the following literal
construction.

1. Replace exactly the declared physical occurrence and rebuild all `1430`
   macro words from the authenticated parent chronology.
2. Recompute the fixed port forest and the complete residual demand vector.
   The residual demand is again integral with entries in `{0,1,2}` and total
   `9744`.
3. Starting from the occ296+C6 residual assignment, repair the demand by
   alternating incidence paths while protecting the two incidences leaving
   the marked object path.
4. Apply quotient cycle switches to the resulting balanced assignment.
5. Materialize the full owner graph and compare it literally with the
   authenticated `a47aa9d...` base.

An exported row must pass all of the following exact conditions before it is
called a balanced column:

- `24310` simple rank-nine owners and `24310` owner edges;
- degree two at every owner;
- every rank-eight edge colour exactly once;
- all `4107` marked-path edges and both marked/complement cross edges fixed;
- equal removed/added edge counts; and
- identical removed/added rank-eight colour multisets.

The exported column is the complete pair

\[
          (E_t^- , E_t^+)=(E_0\setminus E_t, E_t\setminus E_0),
\]

not the original occurrence delta.  Signed owner-degree, lower-colour, and
rank-ten union rows are independently recomputed from `(E_t^-,E_t^+)`.
They must agree with the declared metadata.  Ranks eleven/twelve and
residence are not treated as context-free affine effects of an isolated
edge.

### Bounded connectivity scope

For each toggle the current producer runs **at most** `64` deterministic
repair trials.  It stops at the first connected trial.  If none connects, it
exhausts all `64` and retains the best balanced representative ordered by

```text
(component count, alternating-path moves + 2*cycle switches, trial index).
```

Thus the chosen representative is not optimized for residence or upper
coverage.  A connected row receives a literal chronology.  A row whose best
representative remains disconnected is recorded as a balanced disconnected
factor with chronology-dependent fields undefined.

Failure to connect after the declared maximum of `64` trials is **SEARCH
UNKNOWN**, not a theorem that no connected residual b-flow exists.  Its
component count is not a minimum over the full toggle fibre.  Likewise, a
connected row's residence/upper metrics belong to that certified
representative, not to an optimum over all conditioned residual b-flows.
Conversely, every connected row is a literal positive certificate and can be
independently replayed.

The completed full-run census is

```text
conditioned balanced rows emitted                               438
connected representatives                                      232
disconnected representatives after 64 declared trials           206
component-count profile                           1:232,2:126,3:57,4:20,5:3
rows passing the hard residence non-regression gate                0
connected rows retaining every rank13--17 target                  222
standalone provider-frontier-eligible rows                          0
best connected catalogue column                     z2851_c0_p6328
best connected residence-first score
                         [0,748,776,505,1587,827,115,-252815,-150228,-6].
```

Every row obtains a balanced representative, so the number of balanced-factor
search-unknown rows is zero.  The `206` disconnected representatives remain
connectivity-unknown beyond this declared 64-trial catalogue.  The component
profile and literal metrics are properties of the selected representatives,
not minima over their full conditioned fibres.

## 4. Literal chronology score and guard order

Only connected factors have an ordered complement rail.  For such a factor,
rotate through the frozen marked path, construct the literal facet zipper,
and recompute residence, maximal envelopes, inverse replay, and all upper
intervals through rank seventeen.

The hard residence non-regression gate is the baseline vector

```text
maximal-envelope empty positions                  <= 0
maximal-envelope replay mismatching rows          <= 748
maximal-envelope missing row-bit obligations      <= 776
strict D2 short runs                              <= 503.
```

Equivalently, the guard is the ordered `0/748/776/503` vector.  The catalogue
producer records the following residence-first diagnostic score for each
connected representative:

\[
\begin{split}
(&\#\text{empty envelopes},
  \#\text{replay rows},
  \#\text{missing row bits},
  \#\text{D2 short runs},\\
 &h_{10},h_{11},h_{12},
  -\text{host redundancy},
  -\text{envelope volume},
  -\text{minimum envelope size}),
\end{split}
\]

where `h_r` is the exact number of missing rank-`r` interval targets.  This
tuple selects the catalogue's reported `lexicographic_best_connected` row;
it does not choose the residual b-flow representative and is not the
master's post-guard frontier order.

The master first requires **both** the residence non-regression guard and
zero holes at every rank `13` through `17`.  Only candidates passing those
joint guards enter the provider frontier.  The exact master frontier tuple is

```text
(h10,h11,h12,h13,h14,h15,h16,h17,
 replay rows, missing row bits, D2 short runs,
 -host redundancy, -envelope volume, -minimum envelope size).
```

The high-rank entries are necessarily zero on this accepted frontier; they
are retained in the tuple for literal auditability.  Hence upper gains at
ranks `10`--`12` are never purchased by losing a rank-`13`--`17` witness or
by violating `0/748/776/503`.

The baseline source score begins

```text
(0, 748, 776, 503, 1585, 824, 116, ...),
```

with zero holes at ranks `13`--`17`.  Among the `232` connected catalogue
representatives, the unique best residence-first row is
`z2851_c0_p6328` with

```text
[0,748,776,505,1587,827,115,-252815,-150228,-6].
```

It fails the standalone residence gate because `505>503`.  In fact no
connected representative passes all four residence inequalities.  Exactly
`222` retain every rank-`13`--`17` target, but the intersection with the
residence-pass set is empty, so the standalone provider-eligible count is
zero.

The independent coordinatewise minima of upper holes over the connected
representatives are `1580/818/112` at ranks `10/11/12`.  These are three
separate marginal minima; they need not occur in one row and, because no row
passes residence, are not accepted-frontier values.

## 5. Complete exchange face relative to the new cycle

Freeze the marked path and its two cross edges in the `a47aa9d...` cycle.
There are `20201` complement-internal rank-eight colour groups.  For every
such colour `c`, every pair of complement owners containing `c`, other than
the incumbent pair, is one off-source replacement column.  The exact count
is

```text
mutable lower-colour groups                       20201
off-source exchange columns                      545721
columns including implicit keeps                 565922.
```

The canonical complete exchange stream, regenerated relative to the new
occ296+C6 cycle, has SHA-256

```text
a0d5efb22115745fab920bd26215a8cbc8ac2b711f0a14834f6a03a189f2bed5.
```

This stream is source-relative: the same dimension counts on an older cycle
do not authorize reuse of its incumbent pairs, column IDs, or signed deltas.

For each lower-colour group the master chooses its incumbent edge or one
off-source edge and always imposes exact signed owner-degree equations.
The complete catalogue also supplies exact signed rank-ten provider rows,
including losses of incumbent last providers, but whether they are hard is a
solver mode choice:

- the default provider-descent mode leaves all `19448` rank-ten rows relaxed
  and scores rank-ten holes only after literal connected replay; and
- `--require-rank10-complete` adds all `19448` exact linear-zipper rank-ten
  rows as hard constraints.

There is also an exact soft-support objective
`rank10_then_min_exchanges`.  It introduces one Boolean for each of the
`19448` linear-zipper rank-ten labels, with the exact equivalence

```text
covered[S] iff final linear owner-edge load(S) >= 1.
```

It lexicographically maximizes the number of distinct covered rank-ten labels
and only then minimizes literal changed edges.  The maximum edit tie-break
range is `20217` (`20201` mutable colours plus at most `16` removed edges in
one split), so the rank-ten weight `20218` makes one additional covered label
dominate every possible edit-cost increase.  Ranks eleven/twelve do not enter
this affine objective and remain literal post-replay quantities.

Ordinary component cuts enforce that a returned factor is one cycle.  The
default relaxed mode is a search for improving literal providers, not an
exact rank-ten-complete decision problem.

## 6. Combined toggle/exchange master

The current exact composition face selects either no conditioned toggle or
at most one of the `438` balanced conditioned columns.  It may simultaneously
select any compatible set from the complete `545721` exchange stream.

All `438` balanced rows are admitted.  Standalone disconnection after the
declared 64-trial producer search and standalone residence regression are
diagnostics, not master exclusions: exchange columns may reconnect a
disconnected base or compensate its chronology.  Connectivity cuts and the
`0/748/776/503` plus rank-`13`--`17` guards are applied only to the final
composed factor.

For a selected conditioned column, every lower colour touched by its
complete factor symmetric difference is frozen against a simultaneous
exchange.  This makes the composition literal and edge-disjoint.  Exchanging
an edge installed by a toggle would require a toggle-relative exchange
catalogue and is outside the present master.  Likewise, composing two raw
occurrence toggles requires a jointly rebuilt macro forest and conditioned
b-flow; it is not licensed by adding two single-toggle deltas.

The linear part of every master mode contains:

- one choice equation for every mutable lower colour;
- exact signed degree rows for every complement owner;
- the immutable marked path and cross edges; and
- lazy component cuts.

In optional exact-decision mode it additionally contains all exact signed
rank-ten rows, including incumbent last-provider losses.  In relaxed
provider-descent mode it contains **zero** hard rank-ten provider rows.  Its
available CP objectives are feasibility only, `min_exchanges` (the default),
and the exact rank-ten-support objective `rank10_then_min_exchanges` from
Section 5.  None includes ranks eleven/twelve or residence affinely.
Connected candidates are rescored by literal replay and excluded one exact
choice at a time.

Every relaxed-rank-ten run is seeded with the authenticated zero-toggle,
no-exchange base as a legal connected fallback.  That fallback has full
frontier tuple

```text
(1585,824,116,0,0,0,0,0,748,776,503,-252803,-150224,-6).
```

A solver-produced candidate replaces it only by strict lexicographic
improvement of this complete 14-entry tuple after passing the joint
residence/high-shadow gate.  Thus a bounded soft-support run cannot report an
upper-worse or guard-failing row as its best accepted frontier merely because
the baseline was not emitted by CP-SAT.

The final master also installs the same authenticated base as a **full**
solver hint on every relaxed-rank-ten face: all `545721` exchange variables,
all `20201` changed-colour variables, and all `438` split variables are
explicitly hinted zero.  When the support channel is present, all `19448`
coverage variables receive their exact base values: `17863` covered and
`1585` missing.  The hint bootstraps only the first solver call and
`model.clear_hints()` removes it after round zero, so it is not a permanent
restriction.  Each resolved round emits a concise flushed JSON progress row
containing status and any available topology/frontier diagnostics.

Each connected incumbent is then decoded to a literal owner chronology and
tested in the following order:

1. exact degree, lower palette, marked path, cross edges, and one-cycle
   topology;
2. the joint eligibility gate consisting of the hard residence guard
   `0/748/776/503` **and** exact retention of every rank-`13`--`17` target;
3. for eligible candidates, the provider-frontier tuple beginning with exact
   holes at ranks `10`--`17` and then the replay/residence tie-breakers from
   Section 4; and
4. maximal-envelope/common-cap preflight diagnostics.

If `--require-rank10-complete` is set, step 3 necessarily begins with
`h10=0`; otherwise rank-ten is literal post-replay descent and may remain
positive.

### Completed unhinted rank-ten-soft primary

The first primary used master SHA `f21caf30...`, objective
`rank10_then_min_exchanges`, one worker, and a 60-second per-round bound.  Its
literal outcome is

```text
solver rounds attempted                                      1
round 0 status                                          UNKNOWN
round 0 solver wall time                           60.177120811 s
component cuts added                                         0
connected solver candidates evaluated                        0
emitted frontier origin                       baseline_fallback
emitted selection                       no split, no exchanges.
```

Thus this run is a scoped **UNKNOWN**, not a feasible nontrivial master
selection and not an UNSAT result.  The output status
`ROUND_LIMIT_WITH_RESIDENCE_HIGH_SHADOW_GUARDED_UPPER_FRONTIER` means only
that the authenticated fallback was retained after the bounded solver round.
Its emitted cycle is the zero-toggle occurrence296+C6 baseline with score

```text
(0,748,776,503,1585,824,116,-252803,-150224,-6),
```

and full provider-frontier tuple

```text
(1585,824,116,0,0,0,0,0,748,776,503,-252803,-150224,-6).
```

The independent decoder verifies one cycle, exact lower q1, the frozen
marked/cross bank, the complete literal residence/high-shadow replay, and
the empty selection.  It does not convert the solver `UNKNOWN` into a search
completeness statement.

### Final fully hinted rank-ten-soft run

The final master has SHA `a25abaff...`.  It preserves the exact composition
and objective semantics above, installs the full authenticated relaxed-base
hint, uses `model.clear_hints()` after round zero, and flushes one live JSON
row after every resolved CEGAR round.  The independent composition audit
authenticates that the hint is sound and does not filter any of the `438`
standalone-disconnected or residence-regressing balanced toggle rows.

The two-round `rank10_then_min_exchanges` run gives

```text
round 0       FEASIBLE, one connected baseline, no split/exchange
              residence/high-shadow eligible, no strict improvement
round 1       UNKNOWN
component cuts                                             0
connected solver candidates                               1
best emitted frontier                       baseline_fallback.
```

The exact zero-toggle choice is excluded after round zero by one final-choice
no-good, but the second 60-second call returns `UNKNOWN` before another
candidate.  Therefore this is a scoped bounded result, not a no-go for the
soft-support objective.  The emitted cycle is again the authenticated
baseline and the independent decoder replays it exactly.

### Final min-edit run

The `min_exchanges` run used the same final master for `18:53.24` wall time.
It resolved `19` rounds, added `16` component cuts, and literally evaluated
five connected candidates.  Their exact connected chronology rows are

| round | changes | eligible | replay / missing / D2 | upper holes `10/11/12` |
|---:|---:|:---:|:---:|:---:|
| 0 | 0 | yes | `748/776/503` | `1585/824/116` |
| 4 | 3 | yes | `747/775/502` | `1586/823/116` |
| 6 | 3 | yes | `748/776/503` | `1586/826/117` |
| 9 | 3 | no | `749/777/504` | `1585/824/115` |
| 11 | 3 | no | `751/779/505` | `1585/825/115` |

All five use the zero-toggle state.  Exactly three, including the baseline,
pass the residence/high-shadow eligibility gate.  Neither eligible
three-exchange row is a strict full-tuple improvement because both increase
the leading rank-ten hole count from `1585` to `1586`.  The two rows that
preserve or improve rank-ten fail residence.  Round 17 reaches a disconnected
five-exchange incumbent; after its cut, round 18 returns `UNKNOWN`.  No
connected five-edge row is evaluated.

Thus the min-edit run also emits `baseline_fallback`, with no strict guarded
frontier improvement.  Its `19` rounds and `16` cuts are an exact trace of
this bounded chronology, not an exhaustive search of all three-, four-, or
five-edge compounds.

Any `UNKNOWN`, timeout, or bounded-candidate termination remains a scoped
search outcome.  It is neither UNSAT for the complete exchange polytope nor
an unrestricted `K17` obstruction.

## 7. The targeted `z2851` split-relative C6-pair theorem

The best standalone conditioned representative `z2851_c0_p6328` has score

```text
[0,748,776,505,1587,827,115,-252815,-150228,-6].
```

Its residence excess is localized to four newly created short motifs.  The
complete targeted bank of native support-two balanced C6 circuits whose
changed lower colours directly meet one of those motif rows or boundary
colours contains

```text
native balanced C6 circuits                              51
one-cycle C6 outputs                                     28
single-C6 residence passes                                0.
```

Among their `1132` compatible unordered pairs, `431` give one owner cycle.
Exactly `3` pass the residence vector `0/748/776/503`; exactly `2` of those
also retain every rank-`13`--`17` target.  The three residence-passing pairs
all reuse at least one split-installed lower colour, with overlap union

```text
{2995,19251,26931}.
```

More precisely, their overlap sets are `{2995,26931}`,
`{19251,26931}`, and `{2995,19251}` respectively.

Consequently none is expressible in the current edge-disjoint master, which
freezes a split-touched colour against a subsequent base-relative exchange.
This is an exact obstruction of the **composition encoding**, not of the
physical composite.

The best accepted physical composite is the `z2851` split followed by C6
pair `f57ce4a06e0a1b91`.  It is one cycle, preserves the marked path and exact
lower q1, and has literal replay

```text
empty / replay / missing / D2                 0 / 746 / 774 / 503
upper holes ranks 10 / 11 / 12                    1588 / 826 / 114
upper holes ranks 13 through 17                               0
signed residence-first tuple
        [0,746,774,503,1588,826,114,-252807,-150226,-6].
```

Thus it is a genuine residence repair: replay and missing-bit debts each drop
by two and D2 returns to the allowed floor.  It is **not** a provider-first
upper improvement over the authenticated base because its leading rank-ten
hole count is `1588>1585`.  The exact common-cap matching remains unsolved.

The targeted completeness is limited to support-two C6 circuits that directly
touch the four new `z2851` motifs and to their compatible pairs.  It excludes
support-four circuits, unrelated compensation moves, and a split-relative
regeneration of the full `545721` exchange bank.

## 8. Complete one-C6 provider shell after the residence repair

Take the independently replayed `f57ce4a06e0a1b91` composite from Section 7
as the fixed reference.  Its upper holes are

```text
(h10,h11,h12,h13,...,h17)=(1588,826,114,0,0,0,0,0).
```

The complete native support-two balanced C6 one-path shell around this cycle
contains `13960` packets.  A single C6 adds three owner edges.  To reach
`h10<=1585` from `1588`, it must provide three distinct currently missing
rank-ten targets and lose no uniquely supported rank-ten target.  The exact
direct rank-ten net-gain census has only three `+3` rows, so this condition
reduces the complete shell to three necessary candidates without discarding
any possible one-C6 rank-ten success.  Literal all-gate replay of those three
finds exactly one accepted packet: index `1815`.

Packet `1815` has lower colours

```text
{13114,5946,70458},
```

removes

```text
{13118,14138}
{38714,71482}
{70459,78650}
```

and adds

```text
{13118,78650}
{14138,38714}
{70459,71482}.
```

Its three new rank-ten targets are

```text
{46906,71483,78654},
```

and it loses no rank-ten target.  The final owner factor is one cycle, keeps
the literal marked prefix, and has every lower-q1 colour exactly once.  Its
literal audit is

```text
empty / replay / missing / D2 / D3       0 / 746 / 774 / 503 / 503
upper holes ranks 10 / 11 / 12                    1585 / 824 / 115
upper holes ranks 13 through 17                               0.
```

Relative to the authenticated occurrence296+C6 base, the bounded defect
comparison is

| coordinate | base | final | change |
|---|---:|---:|---:|
| replay mismatching rows | 748 | 746 | -2 |
| missing row-bit obligations | 776 | 774 | -2 |
| D2 short runs | 503 | 503 | 0 |
| D3 short runs | 503 | 503 | 0 |
| rank-10 holes | 1585 | 1585 | 0 |
| rank-11 holes | 824 | 824 | 0 |
| rank-12 holes | 116 | 115 | -1 |
| rank-13--17 holes | 0 | 0 | 0 |

Hence the final carrier is a strict componentwise improvement in this exact
bounded defect vector.  It is not upper complete and does not pass exact D2
inversion: `746` replay rows, `774` missing bits, and `503` short runs remain.
The rank-three common-cap instance is therefore still uninstantiable and
UNSOLVED.

This positive is **outside the original edge-disjoint 438-toggle master**.
The first stage is the split-relative two-C6 residence repair, which consumes
split-installed colours.  Packet `1815` is then an edge-disjoint native C6
relative to that repaired composite.  The theorem is complete only for one
additional native support-two C6 packet around the frozen f57 cycle; it does
not cover support-four circuits, two-or-more additional C6 packets, or a
regenerated split-relative full exchange bank.

## 9. Common-cap status

The scalar marked-cell slack is `7401-4108=3293`, but this count is not a
common-cap matching theorem.  The exact cap instance is fail-closed until a
connected chronology has

```text
empty envelopes = replay rows = missing bits = D2 short runs = 0
and upper holes rank10 through rank17 = 0.
```

Even after those gates pass, the rank-three common-cap matching must still
be built and solved.  In the present lane its status is

```text
exact common-cap feasibility: UNSOLVED.
```

Host redundancy, envelope volume, minimum envelope size, and the scalar
rank10--12 short-demand margin are preflight guards only.  None is renamed as
the exact common-cap Hall value.

## 10. Frozen audit artefacts

Frozen inputs and exact source-relative stream:

```text
a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49  scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4  scratch/k17_opt28_occ296_c6_localmin_verified_20260731.residual.json
d2f77df2c97f95f63cb724ad991cd7ae8d3b21b6dbd1f80c34f8df59016da2ac  scratch/k17_opt28_complement_radius1_columns_20260731.json
a0d5efb22115745fab920bd26215a8cbc8ac2b711f0a14834f6a03a189f2bed5  canonical 545721-column exchange stream
```

Conditioned catalogue, independent replay, and master-semantics package:

```text
76fcde0b997af7b5215c9a4e8b3e32732aa471a6a9cf05eb0e86f881b5b9045c  scratch/build_k17_opt28_conditioned_radius1_split_bflow_columns_20260731.py
15c3f05b7babb082b4c6c28c06efe59efa246945a3966fd4d92b70cc644b6e78  scratch/k17_opt28_occ296_c6_conditioned_438_split_bflow_columns_20260731.json
55e79c8ad00b94cf68503c32495c2a7201aa9ff6a547ce63070ddb02a45ce525  conditioned catalogue payload
fb654a9e820291c3bef7d063ae7b89e9301bb49279a1f097c8c78c2a6df99f7d  scratch/audit_k17_opt28_conditioned_radius1_split_bflow_columns_independent_20260731.py
e07ad331552bc08134af8e13d060ad597c151d8850df34304beb1f7f5cccfd49  scratch/k17_opt28_occ296_c6_conditioned_438_split_bflow_columns_independent_20260731.audit.json
9b3c4a336c292d3ea57e2d7a97e5e97e8d39f5745317b0e48a226b2b9a7832ae  independent audit payload
3c0b8a3dad3a2262358e254287aa4728234aa4e48d0b620f337954bfbd3c9e5d  scratch/verify_k17_opt28_marked_exchange_split_master_result_independent_20260731.py
fa215917b8215c38a07c4afd29c5012e6397bd9886d857795968fe69b9914f17  scratch/audit_k17_opt28_exchange_master_rank10_objective_semantics_20260731.py
fe5502ee7358c12f9741d62619cc3ff011e44fa40262ce09a7f71a8b63a7e96e  scratch/k17_opt28_exchange_master_rank10_objective_semantics_20260731.audit.json
dc7328fbe9b2c22c9fe475b2cb4331e59933e87080086687a8ed39789bef1e78  objective-semantics audit payload
6c308f5ebd8aadd5f625a8d4f90f6e60aa5b57f90e870b1e1434a2bd23014212  scratch/k17_opt28_occ296_c6_conditioned_exchange_master_validate_20260731.json
6fde7191d10172d4683ae19d72427aadef09fb9d8f65695d5339cfcca8d60a73  validation payload
```

The completed unhinted rank-ten-soft run and its independent replay are

```text
f21caf30f1d791131cffa61ee160223fdf20e02e59e006b65a51e39d8e88de1a  unhinted master used for the scoped primary
263be57a663cdf6d88444bfe2a4eafbfe36086dbfa2acedd8a2a3dd3b1b5a2e7  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_master_20260731.result.json
834720b0b8a4d18a77ff3a121b0428d0899de9526f970adfcd850ded76a1bdb3  unhinted result payload
2e3a6db08734217edbed419a9b084c5cafba447ecfaf5818b12c7317de988b5e  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_master_20260731.cycle
a4d05fd362b63272018860aaeb03ee2a4570111a6d791f449ec88fd2cf0e0479  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_master_20260731.independent.audit.json
f397b3e538c071382b195dcb8e7115326a10773c0370904c6aa02d9c5ee0071e  independent decoder-audit payload
```

The final full-hint/live-row master freeze is

```text
a25abaff27e7ceb89c16adcdcc7452b4234d501fbb9a9966d0650c9ff274aea2  scratch/solve_k17_opt28_marked_exchange_split_master_20260731.py
c9e779e0a4d91221b57b942d85faf2d0a836451374999f810dafd87c595c7cbd  scratch/audit_k17_opt28_master_composition_semantics_20260731.py
bf4815ba598f2ea4db2aa51a9f1293550991ccdb3c63a2147e5b0ceca3130855  scratch/k17_opt28_master_composition_semantics_20260731.audit.json
d2ceb41a6bd289ca67ae491e743cb7ee4e3f69bb7d58b2317e29ef16efc906ec  composition-semantics audit payload
```

The completed fully hinted rank-ten-soft run is

```text
9f0e4f5b1ede64655166bce3fe696d812df01e7a700c3b7705e19d870a13dfcb  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_fullhint_master_20260731.result.json
6cadf2a2033f7b618d566ebf31577140455af7bd38d76da195c6d84b3f0e8cee  full-hint result payload
2e3a6db08734217edbed419a9b084c5cafba447ecfaf5818b12c7317de988b5e  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_fullhint_master_20260731.cycle
cccd84f1418b6d6eb21602863084b3e3d0c27ce9900e40d026f1899c208ae8b9  scratch/k17_opt28_occ296_c6_conditioned_rank10soft_fullhint_master_20260731.independent.audit.json
04c2ff08de1aee8dca8b98af9a8908f29605554341d2e37fdcbaf2895dfa7d10  full-hint independent-audit payload
```

The completed min-edit run is

```text
b6b253bdd4c62da882678a17a27e6d5cab0e7bf63d1e2d943744096c41dc2ed4  scratch/k17_opt28_occ296_c6_conditioned_minedit_master_20260731.result.json
145cde6c7d7a30e4c0ba3e386aaad6b6cde0ff9df378e12fc1cc4bab7426f89e  min-edit result payload
2e3a6db08734217edbed419a9b084c5cafba447ecfaf5818b12c7317de988b5e  scratch/k17_opt28_occ296_c6_conditioned_minedit_master_20260731.cycle
931cc1645550262f5baee7be1ace7c242a8e03fa0d9591efe0cad5d9ff64b9a1  scratch/k17_opt28_occ296_c6_conditioned_minedit_master_20260731.independent.audit.json
07d355c10224391e54ca8476b6206ece7a3ff81261435991c7ac01267e982e74  min-edit independent-audit payload
```

The targeted `z2851` split-relative C6-pair package is

```text
ddd1348c455726b43d674e7964c66d83153ca14cc090b19ee77b9395d34381fc  scratch/analyze_k17_z2851_targeted_residence_circuits_20260731.py
307af49e8900528d7f637ae2370f98ec2551d9a5a68b73ae2cde14bdfa63d2f9  scratch/k17_z2851_targeted_residence_circuits_20260731.audit.json
41c4939e1baef92ec50a063ff8e07e75f81d459da2a83eef4cbdfd5338796f3e  targeted producer-audit payload
ec7dd25db159ef611ea62f1a9538d3acfdfaec394b7439fe3da2d88027139cc4  scratch/k17_z2851_c6pair_residence_guarded_20260731.composite.json
8c820913c3ff8e74797ca3575a04e9569cb031d8a36ed99fcd3b9070573dbb4e  composite payload
66b1cc3648f4a3201f5efa409f3078c81e97932437686ab8721ef98bf6efeb4c  scratch/k17_z2851_c6pair_residence_guarded_20260731.owner_cycle.word
64956ddef1b96f7abd59614b714174a1ae91fb08eaeb07cf66ad3caa18434e03  scratch/verify_k17_z2851_c6pair_residence_guarded_independent_20260731.py
56c881842d02f54e7604fbba98a701cdb4dcc6a967084b88a75be53b56f49976  scratch/k17_z2851_c6pair_residence_guarded_20260731.independent.audit.json
31deb3312ec2f51370309dbcaf9ef5b53ed6a1e4319ad63e856ceac6aaa191a1  independent composite-audit payload
```

The complete f57 one-C6 provider shell and positive certificate are

```text
78c53afa3205b32bdee9035932188355d68fccb20393070fa7c23fc3f6b6048e  scratch/k17_z2851_c6pair_residence_guarded_native_p3s2_20260731.bin
dd85c3c1aa0af4ec5bb445885ce295686ad3314fbf5f2832c3cf581cf6311493  scratch/k17_z2851_c6pair_residence_guarded_native_p3s2_20260731.meta.json
b3152abb7a99f26b2f003b23d9f12ff74d30edaeace55eea670f1d4fbf5c83b7  scratch/audit_k17_f57_native_direct_c6_shell_20260731.py
723cc996e1837e9aae602be71190054d9f0228231520550d9c3f16cbe56be5d4  scratch/k17_f57_native_direct_c6_shell_20260731.audit.json
0d81741a79d3e58e1bf2cb4e581299619bbf75e3da9114528d3429d88b9f3407  producer-audit payload
d8cefcbf0874da40807460d75da4c0c74527d717993652395379d6571fc65b14  scratch/k17_f57_native_direct_c6_shell_best_20260731.owner_cycle.word
a5fa57fe13f105ea437eeee1d4d2b32baec9942db905eac2836c50655f49aecf  scratch/verify_k17_f57_native_direct_c6_best_independent_20260731.py
3537fbde1b73bb5116997b7879f8781e2271fd9dfabd24658e39527360c1f81b  scratch/k17_f57_native_direct_c6_shell_best_20260731.independent.audit.json
1ebe4649ba622e1d8953ed5f2d0aadf15af529eff790165420c4838f0b794e29  independent positive-audit payload
```

The handoff and research index are intentionally not updated by this draft.
