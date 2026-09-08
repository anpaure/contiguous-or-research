# All-ports PBBS decision: an actual Johnson 306-owner prefix

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: exact bounded finite decision and literal construction. All
mathematical execution was on `ssh h100`. This supersedes the earlier
non-Johnson shallow prefix for the one-pivot route; it does not yet give a
complete dimension-17 word or change the bound on `nu(17)`.

## 1. Result and actual files

There is a Johnson path through the same six bad 51-cycles, using every
one of their 306 owners once, with every internal positive run of length
at least three. Its nonempty maximal depth-two source has 308 letters,
minimum letter rank seven, and replays every owner exactly.

Together with the other 140 intact canonical cycles, this path preserves
all **41,225** proper upper targets. In particular it retains all **102**
rank-ten targets whose suppliers were confined to the six bad cycles.

Its 305 internal rank-eight adjacency occurrences have 305 distinct
values. Thus both the non-Johnson count `b` and the prefix-internal
duplicate excess `e_inside` are zero. The global adjacency palette of the
path plus the 140 cycles has precisely two missing rank-eight targets:

```text
43857, 46420
```

There is one global duplicate, involving an outside-cycle occurrence.
It is not a duplicate forced by the fixed prefix itself; rethreading Q
can change outside occurrences.

The literal artifacts are:

```text
scratch/badsix_allports_johnson_306_owner_path.word
scratch/badsix_allports_johnson_308_depth2_source.word
scratch/k17_pbbs_badsix_allports_johnson_decision_20260908.json
scratch/decide_k17_pbbs_badsix_all_ports_20260908.py
```

The attaining block order is shown below. All orientations are forward.
Cycle IDs and cut indices refer to the canonical ordering in
`scratch/audit_k17_pbbs_cycle_upper_cut_inventory_20260908.py`.

| order | cycle | cut |
|---:|---:|---:|
| 1 | 116 | 33 |
| 2 | 118 | 32 |
| 3 | 122 | 31 |
| 4 | 129 | 30 |
| 5 | 138 | 29 |
| 6 | 115 | 0 |

The first owner is 43613 and the last owner is 103765. The word files
contain the full literal sequences, not only this assembly description.

## 2. Why the earlier port bank was too restrictive

The earlier decision permitted only 17 safe cuts per cycle. Those cuts
required each individual opened cycle to retain every special upper target
it supplied. That sufficient condition made the jointly upper-safe bank
easy to certify, but it ruled out all six-block Johnson paths. Allowing
non-Johnson seams produced a minimum of three, which the later exact
one-pivot facet restriction excludes.

The new decision permits **all 51 cuts** and both orientations in each
of the same six cycles. It retains exactly the same short-run and envelope
guards; it relaxes only the unnecessarily individual upper-preservation
condition. Upper support is checked on the actual completed prefix,
against the actual intact outside cycles.

This is a complete finite relaxation of the known failed bank. No random
variant search, new carrier family, or unexplained heuristic was used.

## 3. Exact option graph and decision

Each of six colors has 51 cuts and two orientations, giving **612** fixed
oriented block options. At a proposed seam `B|C`, require:

1. for each coordinate, its positive suffix length in B plus its positive
   prefix length in C is zero or at least three;
2. `B[-2] intersect B[-1] intersect C[0]` is nonempty; and
3. `B[-1] intersect C[0] intersect C[1]` is nonempty.

These conditions are exact for shallow residence and nonempty crossing
triples. All blocks have 51 owners, so a run of length at most two and a
triple window cannot cross two distinct seams. The retained interiors
already satisfy the required conditions.

The option graph has **18,360** directed arcs. Give an arc cost zero
when its endpoint owners are Johnson-adjacent and one otherwise. The
dynamic-programming state is `(M,i)`, where M is the set of used cycle
colors and i is the last block option. A transition adds a compatible
unused color and its arc cost.

The reachable-state counts by number of used colors are:

```text
612, 3060, 6120, 6120, 3060, 612
```

There are 612 terminal states. Their minimum cost is **zero**. The chosen
path in Section 1 is recovered from a minimum-cost predecessor chain.

The recurrence is exact: for fixed `(M,i)`, future allowed transitions and
their costs depend only on M and i. Retaining a minimum-cost predecessor
therefore loses no possible continuation. Induction over the number of
used colors proves that every stored distance is its true minimum. Since
zero is also the trivial lower bound on non-Johnson seams, the constructed
zero-cost path certifies optimality directly.

The JSON contains every option descriptor, the full adjacency lists, every
reachable distance state, and the chosen option indices. Thus the finite
decision is replayable in full.

## 4. Literal coverage and palette verification

The verifier reconstructs the canonical factor from the original PBBS map
by finding each mask's unique cyclic Dyck root. It then materializes the
chosen path, verifies its 306 distinct rank-nine masks, and independently
scans all internal coordinate runs.

For each physical position `p` in the 308-letter source, it computes the
intersection of the path owners whose three-position windows contain p.
Every intersection is nonempty. It then checks all 306 actual identities

\[
                         E_i\cup E_{i+1}\cup E_{i+2}=P_i.
\]

Upper coverage is evaluated by literal interval ORs of the complete path
and of every intact outside cycle. For each start the scan stops only at
the full set, beyond which no proper target can occur. The resulting
support contains every canonical proper upper target. The additional
102-target check uses the supplier list and confirms that the new prefix
itself retains the entire special bank.

The verifier separately counts:

* prefix rank-eight occurrences: 305;
* prefix distinct rank-eight values: 305;
* prefix duplicate excess: 0;
* global missing rank-eight values: the two masks in Section 1; and
* global duplicate excess: 1.

The last two global counts are not silently substituted for the
prefix-only invariant used in the one-pivot restriction.

## 5. Exact resource and scope limits

The run was explicitly capped at 90 CPU seconds, 110 wall-clock seconds,
and 2 GiB address space. It completed within five seconds of the remote
execution call. All mathematical execution was on h100, under

```text
/home/amodo/exact-b-k17-badsix-all-ports-20260908/
```

The output basenames there are `badsix_all_ports_decision.json`,
`badsix_all_ports_306_owner_path.word`, and
`badsix_all_ports_308_depth2_source.word`; the local copies have the
explicit `allports_johnson` names above. The verifier imports the existing
canonical generator from

```text
/home/amodo/exact-b-k17-pbbs-inventory-20260908/audit.py
```

The new prefix passes the necessary local facet budget that ruled out the
old one. It also satisfies the shallow part of the exact 306-pivot source
schedule. Neither fact supplies the remaining 24,004-owner path Q, its
upper-safe fusions, the final boundary pins, or the full common-cap lower
compiler. Endpoint-provider analysis for the two new missing masks is the
next finite prerequisite. The old prefix files remain as records of the
failed restricted route; they have not been overwritten.

## 6. Root review and completed endpoint follow-up

Root independently read the complete verifier, the distance recurrence,
the retained result, and the literal-source coverage argument. The state
compression is valid for minimizing the stated seam cost; the selected
completed path then separately passes the actual upper-coverage and
facet checks. No inference that all minimum-cost paths preserve upper
coverage is used. No issue was identified in that internal review.

The endpoint follow-up is now recorded in
`K17_PBBS_ALLPORTS_JOHNSON_PREFIX_ENDPOINT_INTERFACE_20260908.md`.
At least one of the two missing facets must be recreated inside Q.
The same note records the 59 required new private rank-ten colors
strictly inside Q. These are additional necessary constraints on the
unfinished extension, not evidence of a complete word.
