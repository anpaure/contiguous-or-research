# Audit: the K17 common-first support-three serial chain

Date: 2026-08-01  
Status: **PASS, in the exact rooted-static/common-attachment scope stated below**

## 1. Scope

This note independently audits the frozen serial chain

\[
2e919493\to4f5fb7f2\to18527121\to0c277832\to
b355192d\to45a0fd76\to89c9e92e.
\]

Each arrow is one primitive three-root resource circuit from the complete
declared overlapping-support-two commutator shell at its current source.
The conclusions here are only:

1. literal cumulative row lineage;
2. exact type and rank-2-through-rank-7 rooted-flag resources;
3. membership of every selected triple in the overlapping-support-two shell;
4. consistency of the frozen exact packet and common attachment-state matching
   replays; and
5. consistency of the four-shard shell-count manifests.

There is **no** claim about a selected common transversal, quotient or physical
topology, upper shadows, residence, voltage, opening, or compiler feasibility.

## 2. Exact literal-chain theorem

### Theorem 2.1

The six selected replacements have respective root supports

\[
\begin{split}
&(81,437,1380),\quad(216,558,1348),\quad(93,1251,1306),\\
&(353,365,503),\quad(449,563,1055),\quad(1001,1062,1202).
\end{split}
\]

These eighteen roots are pairwise distinct.  At every arrow:

- exactly the displayed three rows change;
- the old and new row values agree byte-for-byte with the frozen step and
  literal-ledger records;
- recomputing the complete resource vector from the row itself gives the
  displayed signed delta;
- the three deltas sum coordinatewise to zero; and
- the resulting 1,430-row table is again an exact rooted static factor.

Sequentially applying the eighteen changed rows to `2e919493...` reconstructs
`89c9e92e...` exactly.  In particular the cumulative resource delta is zero.

Moreover each selected triple admits a literal overlapping-support-two
factorization.  One independently reconstructed witness per arrow is:

| arrow | terminal root | shared root | intermediate option id |
|---|---:|---:|---:|
| `2e919→4f5` | 81 | 437 | 832220 |
| `4f5→1852` | 1348 | 558 | 1062473 |
| `1852→0c27` | 1306 | 93 | 178709 |
| `0c27→b355` | 353 | 365 | 694968 |
| `b355→45a0` | 449 | 1055 | 2008737 |
| `45a0→89c9` | 1062 | 1001 | 1907652 |

#### Proof

For a row option \(f=(t,C_0,C_1,C_2)\), the independently reconstructed
resource multiset is

\[
\mathcal R(f)=\{t\}\cup
 \bigl\{[C_0]:|C_0|\ge2\bigr\}\cup\{[C_0\cup C_1]\},
\]

where brackets mean the canonical cyclic representative.  The verifier builds
the entire resource universe directly: nine type coordinates followed by all
cyclic representatives in ranks 2 through 7, for 2,433 coordinates total.
It checks the prescribed type masses, multiplicity one of every non-type
resource, all partition and suffix-column identities, and all 1,430 ordered
rank-8 roots at every intermediate table.

For each changed row it then computes
\(\Delta(f)=\mathbf1_{\mathcal R(f)}-
\mathbf1_{\mathcal R(f_{\rm old})}\), without using the generator's delta.
The recomputed deltas agree with the frozen step ledgers and sum to zero at
each arrow.  Direct row comparison proves that no other row changed.  An
inductive overwrite of the changed rows proves the cumulative reconstruction.

Finally, for each selected triple with deltas \(v_1+v_2+v_3=0\), the verifier
regenerates all 1,904 literal options at a candidate shared root and finds the
intermediate option \(g\) listed above with
\(\Delta(g)=-v_i\).  Thus \((f_i,g)\) is a resource-zero support-two move, and
replacing \(g\) by the selected shared-root option together with the third
selected root is a second resource-zero support-two move.  This proves the
declared shell membership independently. ∎

## 3. Exact matching lineage

The independent transition-graph and packet replays give:

| table | packet matching | common matching | canonical common Hall shore | deficiency |
|---|---:|---:|---:|---:|
| `2e919493...` | 1172 | 1141 | 309 → 20 | 289 |
| `4f5fb7f2...` | 1173 | 1142 | 308 → 20 | 288 |
| `18527121...` | 1173 | 1143 | 306 → 19 | 287 |
| `0c277832...` | 1173 | 1144 | 305 → 19 | 286 |
| `b355192d...` | 1173 | 1145 | 303 → 18 | 285 |
| `45a0fd76...` | 1173 | 1146 | 301 → 17 | 284 |
| `89c9e92e...` | 1173 | 1147 | 300 → 17 | 283 |

For every arrow, the final values in one frozen replay equal the baseline
values in the next.  All six common matchings improve by exactly one.  The
packet matching improves only at the first arrow and is then retained.

The last common matching is \(1147<1430\).  Therefore this chain does **not**
produce a full common owner/root attachment-state transversal, and no topology
can be inferred from it.

## 4. Complete declared-shell manifests

Every row below is the sum of four independently completed shards of the
overlapping-support-two commutator catalogue.  `canonical` counts distinct
canonical primitive triples; `tail-touch` is the exact old-critical-tail
geometry filter; `cut+` is the exact positive old-cut test; and `gain` is full
common-matching improvement after literal replay.

| source | anchors | completion lookups | completion hits | canonical | tail-touch | cut+ | gain |
|---|---:|---:|---:|---:|---:|---:|---:|
| `2e919493...` | 202322 | 383603199 | 37206419 | 19141938 | 12948128 | 1711267 | 159 |
| `4f5fb7f2...` | 202316 | 383591803 | 37202607 | 19142330 | 12868050 | 1693259 | 136 |
| `18527121...` | 202273 | 383510277 | 37196964 | 19139420 | 12782490 | 1658932 | 134 |
| `0c277832...` | 202308 | 383576648 | 37199274 | 19141418 | 12740319 | 1660278 | 128 |
| `b355192d...` | 202367 | 383688521 | 37153186 | 19118526 | 12667903 | 1657577 | 122 |
| `45a0fd76...` | 202381 | 383715044 | 37168732 | 19125439 | 12614461 | 1677599 | 132 |

This is an exact exhaustive statement only for the declared commutator shell:
primitive support-three circuits admitting a two-step overlapping-support-two
factorization through the current table.  It is not an exhaustive statement
about the complete support-three fibre.

## 5. Frozen artifacts

Primary independent serial audit:

- `scratch/audit_threadA_k17_commonfirst_support3_serial_chain_20260801.cpp`
- `scratch/threadA_k17_commonfirst_support3_serial_chain_20260801.manifest.tsv`
- `scratch/threadA_k17_commonfirst_support3_serial_chain_20260801.audit.json`
- `scratch/threadA_k17_commonfirst_support3_serial_chain_20260801.ledger.tsv`

Per-arrow exact DM and packet/common audits are the files named
`independent.audit.json` and `packet_common.independent.audit.json` under

- `scratch/threadA_k17_2e919_dm_support3_commutator_20260801/`,
- `scratch/threadA_k17_4f5_dm_support3_commutator_20260801/`,
- `scratch/threadA_k17_1852_dm_support3_commutator_20260801/`,
- `scratch/threadA_k17_0c27_dm_support3_commutator_20260801/`,
- `scratch/threadA_k17_b355_dm_support3_commutator_20260801/`, and
- `scratch/threadA_k17_45a0_dm_support3_commutator_20260801/`.

Final SHA-256 bindings:

| artifact | SHA-256 |
|---|---|
| independent C++ verifier | `09097fd449cc7cc3cf83001be208bfae0ae2cdd1c0cedc9da4446f7b0f778ee7` |
| canonical chain manifest | `a33fe39e520bde506531a280f9d7be93c5d877db59ad9e9670d987ef22372d5d` |
| literal-chain audit JSON | `867b86d6cd75ed2d9eee2beecfc93c57f4459e9a42f0e19d332f14358dc5efd3` |
| independently recomputed row ledger | `6f1199e1f174fb0f736323796f30e610323cd391dbf3c1b75c5f5c228280cbf7` |
| graph-consistency audit JSON | `17aaf839508fed2f06df148fb2309a9e8ba1676ba6f5ee89e447bd479ca9e1bf` |
| six-shell manifest audit JSON | `42d4f78c26ae98e02681691428be58629501e400562271d22e178eabaa7fd0d4` |

The note's own hash is intentionally reported externally, avoiding a circular
self-hash.
