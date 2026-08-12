# K16 H1 radius four: exact installer-portal literal-join exclusion

Date: 2026-07-30

Status: exact negative theorem for the remaining installer-pair branch of the
frozen finite catalogue.  The complete 128-shard literal run and independent
packet/partition audit both pass.  Scope remains local to the authenticated
source and the 7,099-action catalogue.

## 1. Frozen scope and the disjoint branch split

The source and move catalogue are

```text
scratch/k16_h2_to_h1_p0.h1.word
SHA-256 ba4bf6d38e1510d06ee64c03c5f13e9a2a4f276882d930d0b5435caf7bcc1e7a
length 12,873; unique hole H=0x2c6d;

scratch/k16_h1_radius4_mitm_catalogue_20260730.tsv
SHA-256 19a48659bdd50abf0a17d3baa3755b79fa88ab7c69a1361dd39a51eb9cd2d4a0
7,099 genuine nonzero replacements on 288 positions; 479 values.
```

Only final words with four distinct edited positions and one listed value at
each position are in scope.  There is no intermediate-hole cap and no use of
the old 775,506 source-positive repair bank.

Give every catalogue action `(position,value)` its unique ID in increasing
lexicographic order.  For a four-action set `F`, call a two-subset an
`H`-installer when applying that two-subset alone to the source installs `H`.
The exact-four catalogue universe has the disjoint partition

1. no two-subset of `F` is an `H`-installer;
2. at least one two-subset of `F` is an `H`-installer.

The first branch is the independently audited primitive triple/four packet
branch.  In the second branch enumerate every installing pair as a portal.
This deliberately permits the same final four-action set to occur through
more than one portal; it avoids a hidden WLOG assumption and does not affect
completeness or the validity of a negative exhaustion.

The uncapped census contains 3,997,398 installing pair actions.  The already
audited positionless SOS test rejects 158,090 of them and leaves 3,839,308.
The theorem below is the exact literal decision procedure for those survivors.

## 2. Stateful pair identity and the six endpoint orders

Fix one portal `P` and put `u=w^P`.  Let `D(P)` be the exact nonempty set of
labels absent from `u`.  For two disjoint repair sites `r,s`, with proposed
values `x,y`, partition intervals changed after `u` into those meeting

```text
r but not s,     s but not r,     both r and s.
```

Their signed columns depend respectively on `x`, `y`, and `x OR y`, so on all
65,536 labels

\[
 M(u^{r\leftarrow x,s\leftarrow y})-M(u)
   =A_r^P(x)+B_s^P(y)+C_{rs}^P(x\lor y).                 \tag{2.1}
\]

After sorting the four positions, their roles have exactly the six oriented
words

```text
PPRR, RRPP, PRPR, RPRP, PRRP, RPPR.
```

Equation (2.1) is a partition by literal interval incidence, not an endpoint
order assumption, and therefore applies to all six words.  In particular the
argument below neither assumes a separated support nor deletes the joint
`C(x OR y)` term.

## 3. A rare debt is an exact repair-pair anchor

For a target `T`, let

\[
 \mathcal S_T=\{e=(q,z): e\text{ is a catalogue action},
                                      \ z\subseteq T\}.  \tag{3.1}
\]

Choose deterministically

\[
 T_*(P)=\mathop{\rm argmin}_{T\in D(P)}|\mathcal S_T|,  \tag{3.2}
\]

breaking ties by the numerical target.  This is the *rare-debt anchor*.

### Theorem 3.1 (anchor completeness)

If a disjoint repair pair `R={e,f}` completes portal `P`, then at least one of
`e,f` lies in `S_{T_*}`.

#### Proof

The state `u` has no `T_*` witness.  Hence every final `T_*` witness contains
at least one repair site: a witness avoiding both repair sites would already
exist in `u`.  Every edited value met by an interval whose OR is `T_*` is a
submask of `T_*`.  Thus at least one repair action belongs to (3.1).  QED.

The implementation iterates the global list `S_{T_*}` and skips actions whose
position lies in `P`.  Orient every repair pair as follows.  If exactly one
endpoint belongs to `S_{T_*}`, it is the first action `e`.  If both do, the
smaller action ID is first.  Theorem 3.1 and this tie-break enumerate every
feasible repair pair once for each fixed portal.  Different installing portal
subsets of the same final four actions remain intentionally duplicated.

This is a literal-action cut.  Its global anchor-list size is

\[
 N(P)=\min_{T\in D(P)}|\mathcal S_T|                 \tag{3.3}
\]

The portal-overlap actions in this list are skipped, so it produces at most
`N(P)` exact three-edit prefixes before additional SOS zeros, instead of all
24,348,717 repair pairs.

### Safe optional refinement

For a fixed debt set, make a graph on the 479 catalogue values, joining `x,y`
exactly when

\[
       x\subseteq T\ \hbox{or}\ y\subseteq T
       \quad\hbox{for every }T\in D(P).                 \tag{3.4}
\]

Here equal values at distinct physical positions are allowed; represent a
compatible equal-value pair by a loop, which forces that value into every
cover.  For every debt `T`, its submask-value set is a vertex cover of this
looped graph, by (3.4).  Any independently verified smaller vertex cover may
replace (3.2):
enumerate literal actions whose values lie in that cover and orient an edge by
action ID when both endpoints lie in it.  This is only a speed refinement;
the single rare-debt cover is already complete and solver-free.

## 4. Optional pre-prefix SOS zero

Let the anchored action be `e=(r,x)`.  A safe optional cut before constructing
its exact triple state is

\[
 U_x(P)=\bigcap_{T\in D(P):\ x\not\subseteq T}T,        \tag{4.1}
\]

where the empty intersection is `0xffff`.  Every possible second value `y`
must obey `y subseteq U_x(P)`.  This is just (3.4) with `x` fixed.

A 16-bit subset SOS whose payload is a 288-position bitset can therefore
reject `e` if no position outside `P` and `r` has a literal domain value below
`U_x(P)`.  A zero is a proof.  A positive result is only an overapproximation
and must be expanded through the literal domain at each set position; neither
a value representative nor a Pareto dominator may be replayed in place of its
dominated actions.  The current engine takes this zero-only pre-prefix cut and
then uses the same position-SOS table after constructing the exact triple,
with the generally different and exact hole upper bound `U(v)` from (5.1).

## 5. Exact last-cell inverse on the literal triple state

Apply the anchored action literally and put

\[
                       v=u^e=w^{P\cup\{e\}}.
\]

Compute the exact hole set `D(v)`.  Fix a prospective fourth position `q`
outside the three already edited positions.  For `T in D(v)`, remove the
incumbent at `q` and let `c_q^v(T)` be the OR of the maximal contiguous
`T`-compatible collar about `q` in the literal state `v`.  Define

\[
 U(v)=\bigcap_{T\in D(v)}T,\qquad
 L_q(v)=\bigvee_{T\in D(v)}\bigl(T\setminus c_q^v(T)\bigr). \tag{5.1}
\]

### Theorem 5.1 (literal last-cell inverse)

For a nonzero genuine catalogue action `f=(q,y)`, every current hole of `v`
is restored after `f` if and only if

\[
                         L_q(v)\subseteq y\subseteq U(v). \tag{5.2}
\]

#### Proof

Fix `T in D(v)`.  Since `v` has no `T` witness, every `T` witness created by
changing only `q` contains `q`.  Such an interval forbids every bit outside
`T`, so `y subseteq T`.  After removing `q`, every compatible witness is
contained in the maximal collar.  Conversely the full collar is itself an
allowed fixed interval.  Therefore a `T` witness exists exactly when

\[
       T\setminus c_q^v(T)\subseteq y\subseteq T.
\]

Intersecting the upper bounds and unioning the mandatory lower bits over all
holes gives (5.1)--(5.2).  QED.

### Why this retains `C(x OR y)`

Fixing `x` first does not replace (2.1) by a source-relative marginal.  It
changes the literal reference state from `u` to `v=u^e`.  If a final witness
through `q` can meet the anchored site, its maximal collar in `v` contains the
literal value `x`; its condition therefore depends on `x OR y`.  If an
incompatible fixed cell separates the two sites, that value is absent from
the collar and the condition is one-sided.  These are exactly the joint and
one-sided classes of (2.1), selected by the actual endpoint geometry.  Thus
(5.2) is an exact sequential elimination of `y` from
`A(x)+B(y)+C(x OR y)` for the current holes, simultaneously for all six
endpoint words.  No marginal compression or additivity assumption occurs.

## 6. Literal expansion, collateral, and within-portal orientation

Precompute the SOS position table

```text
SUBPOS[U] = 288-bit set of positions q having some literal y subseteq U,
DOM[q]    = the literal values available at physical position q.
```

Only positions in `SUBPOS[U(v)]` need to be visited.  At such a position, the
exact inverse values are the literal rows

\[
 \{y\in DOM[q]: L_q(v)\subseteq y\subseteq U(v)\}.       \tag{6.1}
\]

Every row in (6.1) is its literal `(q,y)` action.  If both repair actions lie
in the rare-debt anchor set, discard the orientation with the larger first
action ID.  No lexicographically first-portal condition is imposed: the outer
loop has already authenticated `P` as an installing pair and intentionally
admits the other installing pairs from the same final support.

The inverse condition protects exactly the labels absent from the triple
state.  It need not protect a previously covered label whose last witness is
destroyed by `f`.  Consequently every literal survivor of (6.1) must receive
the exact ten-class `four_delta` test on all affected multiplicities.  Every
row which that test declares universal must then receive

1. construction of the literal modified word; and
2. a literal replay checking every nonzero mask `1..65,535`.

A SAT or solver candidate, if any auxiliary solver is used, has the identical
replay obligation.  No profile representative is a candidate certificate.

If `D(v)` is empty, the implementation must not treat (5.1) as an ordinary
inverse query and silently skip the row.  It must either enumerate all
remaining fourth actions with the same final checks, or cite and authenticate
an independently complete radius-three no-go whose scope contains this exact
triple prefix.  A self-contained implementation should take the former path.

## 7. Completeness of the full finite decision

### Theorem 7.1

The union of

1. the audited no-two-installer primitive packet decision; and
2. the all-installer-pair procedure of Sections 2--6

decides every exact-four word in the frozen catalogue.

#### Proof

The branch split of Section 1 is exhaustive and disjoint.  In the installer
branch every final action set has at least one portal `P`, and every such
portal is enumerated.  The SOS-zero filter retained for this branch is
necessary by (3.4).  Theorem 3.1 selects at least one repair endpoint, and the
action-ID rule selects exactly one when both qualify.  After that literal
endpoint is fixed, Theorem 5.1 retains its partner at the exact physical
position whenever all triple-state holes are restored.  Repetition through a
different installing portal changes only multiplicity of enumeration.
Finally, exact multiplicities and literal replay are equivalent to
universality.  Hence no completion is omitted and no reported completion is
false.  QED.

## 8. Implementation cost and independent audit obligations

The principal triple-prefix work is bounded above by

\[
\sum_{P\ \mathrm{SOS\ survivor}} N(P)       \tag{8.1}
\]

exact triple deltas, not `3,839,308 * 24,348,717` pair tests.  For each triple,
first form `U(v)` and restrict to positions in `SUBPOS[U(v)]`; only those
positions need collars.  The dense 65,536 by 288 SOS position table uses about
2.25 MiB before alignment.  Literal lower-bound checks are then direct loops
over `DOM[q]`; no superset-profile representative is stored.

Maximal collars may be obtained either by literal outward scans or by an
audited index: for each target, a source-bad-position bitset supplies nearest
incompatible predecessors/successors; the three fixed edits toggle at most
three bits; range OR is evaluated on source subranges split at those edits.
The indexed answer must be compared with literal scans in the independent
audit.

The retained all-six-order proof-primitive regression is

```text
scratch/audit_k16_radius4_cross_order_type_normal_form_20260730.py
SHA-256 4a3bf627960cd158f76c82d6f3ec31e8ee9e72d67b71d212c0b0d72a66f6f6dd

scratch/k16_radius4_cross_order_type_normal_form_20260730.audit.json
SHA-256 a8d055076f20253a083ac7f16b52f7fa199528922e070a9cfc55e798ef9f20a1
status PASS_ALL_SIX_ORDER_TYPES.
```

It checks (2.1) and literal maximal-collar equivalence independently on all
six oriented words.  The installer run must authenticate, rather than silently
replace, that proof primitive.

An authenticated run should report at least:

```text
all uncapped H portals and SOS-zero portals;
histogram and sum of N(P);
anchored triple prefixes and post-prefix zero upper bounds;
empty/nonempty triple-hole sets;
inverse positions, inverse literal values, and exact-four tests;
within-portal reverse-orientation rejections;
duplicate final rows arising from different installing portals;
full 65,535-mask replays and any candidate word.
```

An independent engine should rebuild the catalogue and source hashes, use a
different collar implementation, verify the rare-debt anchor and action-ID
orientation literally, reproduce every terminal counter, and fully replay
any positive candidate.  A negative run proves only the exact finite
catalogue radius-four theorem stated here; it does not leave the catalogue,
change the rooted word, or settle unrestricted K16.

## 9. Authenticated build and complete 128-shard result

The final producer is

```text
scratch/search_l_k16_h1_radius4_installer_lastcell_join_20260730.cpp
SHA-256 7d246a9e39a4f18858aabc0cbc7b8422c8995e0b55bd9a7efc4d06bd84f80bd5
```

Its build mode reproduced the previously audited uncapped census exactly:

```text
distinct-position pairs                         24,348,717
H-installing pairs                               3,997,398
SOS-incompatible portals                           158,090
SOS-compatible portals                           3,839,308
unique / compatible debt sets                 81,228 / 79,866
maximum portal holes                                    28
raw rare-debt anchor rows                         467,499,103
```

The deterministic portal packet and build audit are

```text
scratch/k16_h1_radius4_installer_portals_20260730.bin
SHA-256 96dce22915c141e0269a1df980334835032f186aafe93c7f60db5ffdec374eb2

scratch/k16_h1_radius4_installer_portals_build_20260730.audit.json
SHA-256 c1364ab542d8fa621e7c1803f8da183e0a189f5e4c942385b0d611b24039852e
```

The packet build took 342.12 seconds on one H100 CPU, with 55,396 KiB
maximum RSS and zero swap.  Search used executable SHA-256
`4fd25c164c536e8ccda6b9c56acce654f49d0c111e612cb152676afc8ea5df7a`.
The exact floor partition

\[
 [\lfloor 3839308i/128\rfloor,
   \lfloor 3839308(i+1)/128\rfloor),\qquad 0\leq i<128,
\]

has 76 ranges of 29,995 portals and 52 of 29,994.  An interrupted scheduler
left exactly ranges 0--31 complete; the authenticated resume began at 32 and
did not rerun them.  The final aggregate is

```text
portals processed                                3,839,308
raw anchor rows                                467,499,103
position-distinct anchor rows                  430,623,287
partner-SOS zero rows                              730,890
exact literal triple prefixes                  429,892,397
triple prefixes with zero holes                          0
nonempty-hole prefixes with zero common upper   77,014,908
candidate last positions                         1,165,201
literal inverse values                           2,360,982
canonical literal values / exact four tests      1,870,791
authenticated completions                                0
```

Every exact-four test is a literal ten-class multiplicity calculation.  Any
positive multiplicity result would construct a word, replay every nonzero
mask `1..65,535`, and emit a candidate.  All 128 shards instead have exhausted
status, process exit 1, empty `solution_edits`, and no `full_*.word` file.
Thus the candidate-replay obligation is vacuous; the independently written
all-mask verifier remains frozen at SHA-256
`6677e9b616f8daeefc5eb0bb90e5d4bc7d6d6dfb8b0ef875ad6b3470f80f221c`.

The 128 low-priority H100 jobs used 12,678.51 aggregate user seconds and
13.27 aggregate system seconds.  Their maximum per-job RSS was 59,904 KiB;
all 128 report zero swap.  All work and artifacts stayed under the unique
`/home/amodo/or15/work/laneL_k16_radius4_installer_literal_join_20260730`
tree; the separately reserved core 28 was excluded from the production CPU
mask, and no `/dev/shm` path was used.

## 10. Independent packet, literal, and resource audits

The standalone auditor

```text
scratch/audit_l_k16_h1_radius4_installer_build_shards_20260730.py
SHA-256 2189cce5159ee3fbfd9b7c38795d2fefe023cbe7ab39375ec4ca93fec3e75118
```

parses every packet debt and portal row, authenticates strict row ordering,
recomputes every one of the 81,228 ordered-value SOS counts through the exact
16-generator meet identity, and checks the build histogram and weighted
anchor sum.  It then literally recounts 32 portal states, 16 triple states,
34 last-cell values and 696 target clauses, before enforcing the exact
128-range union and every counter identity above.  It reports

```text
PASS_INDEPENDENT_BINARY_LITERAL_AND_EXACT_SHARD_COVER
payload SHA-256 209c5a99080697904e7d4652f7ac02ff2a73b8111d85401de93f06dcac5dc268
```

in 23.37 seconds, 101,696 KiB maximum RSS and zero swap.  Its result is

```text
scratch/k16_h1_radius4_installer_build_shards_independent_20260730.audit.json
SHA-256 80b77f96611009adec7ef69a6a050ddb819dbf8ea5cf87f5d6af4f583edcab41
```

The separate resource/hash auditor has source SHA-256
`031ca69f7cc0ce83211b974dae6b1be6f8e2acf72bc3454151644c6f2999b760`.
It verifies all 128 GNU-time exit/swap records, hashes every shard JSON and
log, and reproduces the global sums.  Its result is

```text
scratch/k16_h1_radius4_installer_shard_resource_manifest_20260730.audit.json
SHA-256 f113bc8a59ecada7a6d1454b1c3b6edc38b11d713a642017f511a2f02891fc2e
payload SHA-256 e609446ae871e09ca0ea1df383d8d4d50ac1f4d79cea12f632b3e37ea6282308
shard-set SHA-256 abd178d2dc37ad71100d341dd94a04d75c7c675dcde85fc223aec2f7a84f7720
```

The byte bundle of the 128 audit/log pairs has SHA-256
`b383707db5bbe9f5fffb420abd1147ecba8121a88562c925ce2da3eebfe3687e`.

## 11. Exact conclusion and inherited boundary

### Theorem 11.1 (installer-portal exclusion)

No exact-four word in the frozen 7,099-action catalogue is universal if at
least one of its six two-action subsets installs `H=0x2c6d`.

#### Proof

The 158,090 positionless-SOS zeros are impossible by (3.4).  Every remaining
portal appears exactly once in the packet partition.  Theorem 3.1 retains a
repair endpoint, Theorem 5.1 retains its mate at its literal position and
value, and exact `four_delta` plus all-mask replay is equivalent to final
universality.  The exact negative union of all 3,839,308 retained portals
therefore leaves no completion.  QED.

Combining Theorem 11.1 with the independently closed no-two-installer packet
branch (`3b90c50f...cef6e`, `87c46b87...00c0c`, and cross-audit
`4bde7966...df16`, payload `5977ff14...fc64`) excludes every exact-four word
in the catalogue.  The complete arbitrary-value substitution-radius-three
theorem and union audit (`bb1e1075...9d63c`, result `6bfbe947...e749`, payload
`6370036d...671a`) supply the support-at-most-three boundary.  They incorporate
the exact two-site-plus-one theorem and the 144,191,783 all-joint assignments,
which strictly contain the independently checked 1,341-support nested-portal
face (`f432c830...8abb`).

Hence the precise combined statement is:

```text
no universal word within three arbitrary nonzero replacements of the source;
no universal exact-four word when all four replacements lie in the frozen
7,099-action catalogue.
```

This is not an unrestricted arbitrary-value radius-four theorem, does not
leave the fixed source/order, and does not settle K16.  The global bracket
remains

```text
12873 <= nu(16) <= 12874.
```
