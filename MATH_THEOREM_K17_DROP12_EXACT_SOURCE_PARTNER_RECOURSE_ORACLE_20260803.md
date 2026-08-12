# K17 drop-12 exact source/partner recourse oracle

**Date:** 2026-08-03

**Status:** proof-safe reduction and checker specification on the canonical
drop-12 parent.  This note proves an exact occurrence oracle and a lossless
directed-rescue prefilter.  It does not report the result of the full
52,568,203-child computation, a supplier contraction, a chronology, or a K17
word.

## 1. Frozen face and the complete partner domain

The parent is the fixed-ten final table with SHA-256

```text
fa49188250bf194c8218d8afb5bf5f9220e4a73fd1267824bc7ed0b2868bbb7c.
```

The canonical transfer catalogue has SHA-256

```text
790fae940cd80c05e35656027dcb57139180b54c77f567c9b5333ab5d4581434
```

and contains 114,594 LLR transfers.  Excluding transfers whose LR or LMR
endpoint meets the 7,256-row structural endpoint-forbidden bank (7,213
private rows, the 23-row incumbent occurrence union, and 20 incumbent
transfer endpoints, pairwise disjoint) leaves exactly
112,621 fixed-bank-safe partners.  Anchoring one coordinate at each of the
468 authenticated unary supplier-rank-16,878 sources, and requiring the two
endpoint pairs to be disjoint, leaves exactly 52,664,349 directed
source/partner incidences (out of 52,706,628 before endpoint disjointness).
When both coordinates are sources the same unordered child is seen in both
directions.  There are 96,146 such reverse duplicates, hence 52,568,203
unique child tables.  An implementation must choose and state one convention:
scan all 52,664,349 directed incidences, or canonicalize the unordered pair
while retaining both possible source-role labels.  A directed loop that
expects 52,568,203 without deduplication is erroneous.  The 3,483
parent-common helpers are a useful sufficient subface, not the complete
domain.

Structural endpoint immutability and occurrence-provider availability are
different constraints.  The ten incumbent LR endpoints are already LLR long
rows in the fixed-final table and remain legal occurrence providers; the ten
incumbent LMR donors are now MR/nonlong.  Thus incumbent endpoints are
excluded when selecting a new transfer, but the ten materialized incumbent
LLR hosts must not be removed from the long-state bank.

The ten incumbent occurrence tickets reserve 20 distinct physical rows in
each phase.  Their union has 23 rows; 17 rows occur in both phases and have
the same flag in both.  An exact pair checker must enforce the 20 reservations
phase by phase.  Excluding the 23-row union in both phases is safe but not
lossless: a row reserved only in phase 1 may be used in phase 0 provided its
flag agrees with the phase-1 incumbent reservation, and conversely.

This creates an audit prerequisite.  The existing 468-source
`raw_common_state=0` ledger was produced with the stronger global 23-row
exclusion.  It is an exact no-go on that restricted face, but does not by
itself prove one-transfer common-state zero after the six
opposite-phase-only opportunities are restored.  The 468 sources must first
be repriced with the phase-specific rule above.  Any newly common source is a
one-transfer supplier-rank-16,878 candidate and must be promoted directly;
only sources still common-free may use the forced-rescue reduction below.

The corrected phase-specific rerun again found zero common sources.  Its
global occurrence exclusion is exactly the 7,213 private rows; it does not
insert the 20 incumbent endpoints into that bank.  Consequently the ten
materialized incumbent LLR hosts are admitted, while the ten MR donors are
excluded naturally by chain length.  The self-contained frozen H100 root is

```text
/home/amodo/or15/work/codex_019fc363_k17_drop12_def20_source_fullpartner_20260803
```

and its principal hashes are

```text
audit JSON                  a1b67315af62cbe222aede6e4b9f5dd5a85ebf6100d831f220e8b46bc3c6faf6
empty positive ledger       b8fc3ec81082a23d9f86d98b3f51e0a8586a9d1806e8a1c4a49dac7cd43535b5
checker source              ff7c84e8c7701493b31b33d6a4019ac9c873ef697c137a3a31b073c25eff8331
frozen manifest             94101008273ed54928cd818daab8142bf03b007fba106477c71009b4d0ffcb03
```

The frozen manifest binds every consumed canonical input, both phase
reservation files, source, binary, output, and transcript.  An independent
implementation under
`/home/amodo/or15/work/audit_independent_k17_drop12_phase20_019fc3fc_20260803`
agrees byte-for-byte on the empty positive ledger (source `92d929b0...`, audit
`22947f62...`).  Therefore the hypothesis of Theorem 4.1 is established for
all 468 sources.

## 2. The literal two-transfer long-state bank

For a transfer (x), write (h_x) for its old LR host, (d_x) for its old
LMR donor, and (H_x^\phi(a)) for the flag-(a) LLR long state created at
(h_x) in phase \(\phi\).  Let \({\cal L}_0^\phi\) be the fixed-final bank of
available base LMR long states after removing global private rows.

For endpoint-disjoint transfers (x,y), simultaneous materialization gives
exactly

\[
 {\cal L}_{x,y}^\phi=
 \bigl({\cal L}_0^\phi\setminus\{d_x,d_y\}\bigr)
 \cup\{H_x^\phi(a),H_y^\phi(a):0\le a<4\}.                 \tag{2.1}
\]

There are no other changed long states.  Thus pair-local occurrence pricing
does not require rebuilding an unrelated global object: it is exactly two
deletions and two four-flag insertions in each phase.

## 3. Exact phase and two-phase options

For the new MR short at (d_x), a phase-(\phi\) option is

\[
 w=(k;p,a;s,b),\qquad k=(q,a,b),                          \tag{3.1}
\]

where the predecessor state \((p,a)\) and successor state \((s,b)\) lie in
\({\cal L}_{x,y}^\phi\), and the exact incoming, outgoing, and literal
five-cell predicates all hold.  If (p=s), then (a=b).  A row may fill both
sides of one short in this equal-flag case; its phase footprint is still one
physical row.

The option must avoid every row reserved by an incumbent occurrence in phase
\(\phi\).  If it uses in phase \(\phi\) a row reserved only in phase
\(1-\phi\), its flag must equal that incumbent flag.  This is the precise
phase-specific reservation rule.

A two-phase option for (x) is

\[
 o_x=(k,w_x^0,w_x^1)                                     \tag{3.2}
\]

with the same declared key (k) in both phases, such that every physical row
used in both phases receives the same flag.  Let \({\cal O}_x(x,y)\) be the
set of all such options.  Alternative tuples for one key must all be retained;
one frozen or first witness is not an exact substitute.

For an option (o), write (F_\phi(o)\) for its one- or two-row physical
footprint in phase \(\phi\), and (\gamma_o(v)\) for the unique flag assigned
to a row used by (o) in either phase.

## 4. Directed-rescue lemma

### Theorem 4.1

Let (x) have no common declared occurrence state in its fully materialized
one-transfer child.  If \({\cal O}_x(x,y)\ne\varnothing\), then every option
in \({\cal O}_x(x,y)\) uses the newly created host (h_y) in at least one of
its four phase-specific predecessor/successor roles.

### Proof

Relative to the one-transfer child for (x), adding (y) deletes the old
long row (d_y) and adds the four states at (h_y).  Deletion cannot create
an occurrence.  An option which uses no state at (h_y) and is valid after
the deletion was already valid before the deletion, contradicting the
one-transfer common-state no-go. \(\square\)

Hence the first lossless screen for an anchored pair (x,y) is not “both
roles lie among the two new hosts.”  It is only

\[
 h_y\in F_0(o_x)\cup F_1(o_x).                           \tag{4.1}
\]

The other role may be any surviving base long row.  If (y) also has no
one-transfer common state, the reciprocal condition

\[
 h_x\in F_0(o_y)\cup F_1(o_y)                            \tag{4.2}
\]

is forced as well.  If (y) is parent-common, (4.2) is not forced: it may
retain any surviving old option.  Nevertheless its complete child-local menu
must be regenerated because deleting (d_x) can kill a frozen witness and an
alternative witness may survive.

## 5. Exact two-color compatibility theorem

For a fixed anchored pair (x,y), make a bipartite graph with shores
\({\cal O}_x(x,y)\) and \({\cal O}_y(x,y)\).  Join (o_x,o_y) exactly when

\[
 F_\phi(o_x)\cap F_\phi(o_y)=\varnothing
 \quad(\phi=0,1),                                        \tag{5.1}
\]

and

\[
 \gamma_{o_x}(v)=\gamma_{o_y}(v)
 \quad\text{for every row used by both options across phases}. \tag{5.2}
\]

### Theorem 5.1

The two transfers admit a joint occurrence packing, together with the ten
fixed incumbent tickets, if and only if this option graph has an edge.

### Proof

A joint packing restricts to one same-key two-phase option for each new short.
Unit phase capacity gives (5.1), and the single physical flag address gives
(5.2).  Conversely, an edge supplies all four exact phase witnesses, respects
the phase-specific incumbent reservations by the definition of each option,
and satisfies every remaining capacity and flag-coalescing condition. \(\square\)

This is the minimal reciprocal occurrence condition.  It is pair-local and
does not assume that either transfer keeps a selected frozen tuple.

## 6. Lossless incremental construction

For one-transfer (x), retain the complete phase tuple sets
\({\cal B}_x^\phi(k)\), not merely their first elements.  For partner (y),
put

\[
 {\cal S}_x^\phi(k;y)=
 \{w\in{\cal B}_x^\phi(k):d_y\notin F_\phi(w)\},          \tag{6.1}
\]

and let \({\cal G}_x^\phi(k;y)\) be every exact tuple in the joint child
which uses (h_y).  Then

\[
 {\cal W}_x^\phi(k;x,y)=
 {\cal S}_x^\phi(k;y)\cup{\cal G}_x^\phi(k;y).           \tag{6.2}
\]

Equation (6.2) is exact by (2.1).  The host-admitting phase-specific audit
proves that all 468 sources remain common-free, so Theorem 4.1 permits
discarding every two-phase combination which uses no member of
\({\cal G}_x^0\cup{\cal G}_x^1\).  Therefore the cheapest proof-safe order is:

\[
 {\cal O}_x(x,y)\ne\varnothing
 \quad\Longleftrightarrow\quad
 \exists k\;\Bigl[
   {\cal G}_x^0(k;y)\bowtie {\cal W}_x^1(k;x,y)
   \;\cup\;
   {\cal W}_x^0(k;x,y)\bowtie {\cal G}_x^1(k;y)
 \Bigr]\ne\varnothing,                                  \tag{6.3}
\]

where \(\bowtie\) means cross-phase flag-compatible pairing.  The forward
direction is Theorem 4.1; the reverse direction is immediate.  Formula (6.3)
is a lossless source-side implementation: it never enumerates a base/base
two-phase pair, yet it allows the non-helper role to be any surviving base or
new-host row.  It is strictly larger than the positive-only screen that puts
both source roles among the two new hosts.

The proof-safe execution order is:

1. authenticate the completed host-admitting phase-specific unary no-go;
2. enumerate the 112,621 fixed-bank-safe partners and assert either the exact
   52,664,349 directed-incidence census or the explicitly deduplicated
   52,568,203 unique-child census;
3. build only the source options using the partner host in at least one phase;
4. reject a pair if this source option set is empty;
5. only for a survivor, build the partner's complete child-local option set;
6. test Theorem 5.1;
7. only for an occurrence-positive pair, materialize both transfers and run a
   fresh complete supplier maximum matching.

No positive one-mode Hall credit may be added across the pair; the supplier
replay remains mandatory.

## 7. Exact bitset implementation of the option graph

Index the partner options by bits.  Precompute bitsets

\[
 U_{\phi,v}=\{j:v\in F_\phi(o_j)\},
 \qquad
 V_{v,c}=\{j:o_j\text{ assigns row }v\text{ a flag different from }c\}.
\]

For a source option (o), its incompatible partner options are exactly

\[
 \bigcup_{\phi=0}^1\ \bigcup_{v\in F_\phi(o)}U_{\phi,v}
 \ \cup\ 
 \bigcup_{v\in\mathrm{dom}(\gamma_o)}V_{v,\gamma_o(v)}.  \tag{7.1}
\]

Thus one bitset subtraction tests whether (o) has a compatible partner.
Equation (7.1) is an exact implementation of (5.1)--(5.2), not a relaxation.

## 8. Required checker outputs and scope

A fail-closed checker should emit and hash-bind:

* the 112,621-partner, 52,664,349 directed-incidence, and 52,568,203
  unique-child domain ledgers, including the 96,146 reverse-duplicate audit;
* a directed source-rescue ledger with complete option signatures;
* the exact option-graph-positive pair ledger and one literal edge witness per
  positive pair;
* simultaneously materialized child tables for any promoted pair;
* replay of the ten incumbent occurrences plus the two new options; and
* a fresh complete child supplier matching/Hall audit.

A zero after the directed-rescue step is a no-go for the complete anchored
domain only if the unary source first passed the phase-specific common-zero
audit, the other role was allowed to range over every surviving base long row and the
20 incumbent reservations were enforced phase-specifically.  A zero from the
smaller changed-host-only/frozen-helper screen is not such a no-go.

Phase 1 remains transported-owner evidence.  Even a supplier-rank-16,878
child would not establish chronology, residence, arbitrary upper coverage,
common-cap compilation, a length-24,313 word, or \(\nu(17)=B(17)\).
