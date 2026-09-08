# Audit of the upper-12874 D4 provider-core extension and benchmark

Date: 2026-07-31  
Lane: D  
Status: exact extension/composition theorem and deterministic launch design; no D4 census result is claimed here

## 1. Frozen inputs and the exact new scope

The parent word is

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

The complete deletion census has hole-count histogram

```text
1:1, 2:3, 3:3, 4:184, 5:931, ... .
```

Thus

```text
D3 = {deletions with at most 3 holes}, |D3|=7,
D4 = {deletions with at most 4 holes}, |D4|=191,
E4 = D4 minus D3,                    |E4|=184.
```

The exact D3 delete-plus-two-substitution theorem is already frozen.  A new
H100 run should therefore enumerate only `E4`; rerunning the seven D3 cases
would be duplicate computation.  A completed `E4` provider-first census,
composed with the D3 theorem and the already global all-joint theorem, would
close arbitrary two substitutions after exactly the 191 deletions in `D4`.
It would not close the other 12,683 deletions or prove a global radius-two
theorem around the parent word.

The frozen ledgers are

```text
scratch/k16_upper12874_delete_sub1_all12874_20260730/summary.tsv
  SHA-256 cb974199018493433ddfce8674b295323a87631dc61d996f10d24732b9e8ced5

scratch/k16_upper12874_delete_basins_le4_20260730.tsv
  SHA-256 62148666bdbe577c7184112e3f6cc8b6f2c8c856c8113fbbff2a3626fbfcbb01
  191 data rows, of which 184 have exactly four comma-separated holes.
```

## 2. Why the D3 engine extends exactly to D4

Fix a deletion word `W`, its original hole set `H`, and a proposed final
word with two distinct changed sites.

### Lemma 2.1 (provider/all-joint dichotomy, arbitrary `|H|`)

If some final witness of an original hole contains exactly one changed site,
then applying that edit alone to `W` supplies an original hole.  Otherwise
every final witness of every original hole contains both sites.  Hence every
completion is in the union of the provider-first and all-joint branches.

The proof does not depend on `|H|`.

### Lemma 2.2 (complete first-provider bank, arbitrary `|H|`)

At a first site `p`, a value `u` supplies `h in H` iff for some suffix/prefix
context OR `s`,

```text
s subset h,        h minus s subset u subset h,        u != 0.
```

Taking the union of these Boolean intervals over all `h in H` enumerates
every partial provider.  The literal implementation deduplicates values at
each site and rejects the incumbent.  Adding a fourth hole only adds another
member to this union; it changes no inference.

### Lemma 2.3 (seeded second-position completeness, arbitrary debt count)

After the first edit, let `D` be the exact intermediate hole set and put

```text
U = AND {t : t in D}.
```

Every completing second value is a nonzero submask of `U`.  For any seed
`t in D`, the bits `t minus U` must already occur in the maximal
`t`-compatible context around the second site.  The source seed list contains
all sites having that property before the first edit.  A one-cell edit can
change this context only in the old/new compatible components incident with
the first site and their adjacent separators; the engine adds a superset of
exactly those sites.  This proves completeness of the candidate-position
list for any number of debts.  Choosing a strongest seed changes only speed.

### Lemma 2.4 (full target core, arbitrary debt count)

For a candidate second site `q`, let `R(q)` consist of every nonzero target
whose current witnesses all contain `q`, with current holes included at every
site, and set `J(q)=AND R(q)`.  A completing second value exists iff the
single maximal value `J(q)` completes, except for the standard incumbent
coatom check.  The suffix/prefix banks are built in the literally first-edited
word, so intervals containing both edits use the exact `u OR v` cross term.
Again no bound on `|H|` occurs.

Together these lemmas prove that changing the input assertion from `1..3`
holes to `1..4` holes is an exact D4 extension.  The current files satisfy
this narrow-diff audit:

```text
scratch/threadD_search_k16_upper12874_d3_provider_core_20260731.cpp
  SHA-256 7b1c17bbd1276a8cd4184e47f56dc4e6c66f84cc084bd155a4896ec308acd9aa

scratch/threadD_search_k16_upper12874_d4_provider_core_20260731.cpp
  SHA-256 83a65fc1df68bc7fa3cc1808f30975956b31c39d1d6adcc4e9c04f6a9dba694a
```

Their diff consists only of the `D3` to `D4` symbol/schema rename and the
input bound `base_holes.size() > 3` to `> 4`.  No search or pruning expression
changed.

## 3. Exact D4 composition contract

The independent composer must verify all of the following.

1. Recompute every deletion word from the frozen source, using source index
   `d` and post-deletion indices thereafter.  Recompute its complete interval
   OR coverage and exact holes; do not merely trust the materialization
   ledger.  The current materializer authenticates bytes and expected rows,
   but does not independently recompute the hole sets.
2. Verify that the new result IDs are exactly the 184 `E4` IDs, without
   duplicates, and that every engine audit reports the four expected holes.
3. Require terminal exit code `1`, status
   `PASS_EXHAUSTED_NO_COMPLETION`, and `positions_claimed=12873` for every
   negative row.  Timeout, signal, resource failure, absent audit, or a
   missing row is `UNKNOWN`.
4. If an engine returns a candidate, replay all 65,535 nonzero masks by both
   ending-state and start-by-start interval enumeration before accepting it.
5. Authenticate the already frozen D3 composed theorem, rather than rerun
   those seven cases.
6. Authenticate

   ```text
   scratch/k16_upper12874_delete_two_sub_alljoint_global_exact_20260730.independent.audit.json
   SHA-256 e0303b3bef80d14e9bde85863347b6c78947b212eb159bac77cac005bb29bcd0.
   ```

   It covers all 12,874 deletions.  Within `E4`, 116 deletions have a
   nonempty all-joint support catalogue (227 supports and 362,134 ordered
   value pairs); the other 68 have no all-joint support.  The exceptional
   frozen deletion `d=1` belongs to D3 and is separately included in the
   authenticated global composition.
7. Authenticate the all-deletion delete-plus-one-substitution no-go before
   using it to discard an incumbent at either changed site.  Deletion alone
   is impossible because every D4 basin has at least one hole.

Only after all 184 new provider rows are terminal may the composition status
say `PASS_EXACT_D4_DELETE_TWO_SUBSTITUTION_NO_COMPLETION`.

## 4. Static workload stratification

For a deletion `d`, define the provider-envelope score

```text
B(d) = sum_{h in H_d} (2^popcount(h) - 1).
```

At any first site, the union of literal provider values is at most `B(d)`;
hence the outer provider records are at most `12873 B(d)`.  This is a rigorous
outer-loop bound, not a bound on the later candidate-site geometry.

The 184 exact-four-hole rows have the complete distribution

| `B(d)` | count | rows |
|---:|---:|---|
| 764 | 96 | ordinary lower stratum |
| 1532 | 85 | ordinary upper stratum |
| 1660 | 1 | `d=2` |
| 1916 | 1 | `d=12872` |
| 3068 | 1 | `d=6440` |

The corresponding per-row rigorous provider-record upper bounds are
`9,834,972`, `19,721,436`, `21,369,180`, `24,664,668`, and `39,494,364`.
Summed over `E4`, the static bound is 2,706,007,584 records.  It is deliberately
loose: for comparison, the completed D3 row `d=12871` has `B=4861` but only
1,133,158 actual provider records and finished in 7.03 seconds on one H100
CPU core.

The score is therefore suitable for deterministic workload stratification,
but not for a mathematical pruning rule or a guaranteed wall-time bound.

## 5. Deterministic pilot and projection cap

Use the following 13 exact-four-hole pilot rows and no D3 rows:

```text
special rows: 6440, 12872, 2

B=1532 quantiles (ranks 1,22,43,64,85 of 85):
6550, 8569, 9942, 11549, 12867

B=764 quantiles (ranks 1,25,49,73,96 of 96):
112, 2038, 3520, 4816, 6429
```

Here ranks are taken after sorting each stratum by deletion index.  Thus the
sample is reproducible, contains every exceptional workload class, and spans
both ordinary strata.  Execute the 13 shards sequentially in one low-priority
H100 CPU process, with 512 MiB address-space, 120 CPU-second per-case, and
150 wall-second per-case caps.  Any nonterminal pilot row stops the portfolio
with `UNKNOWN` for that row and `NOT_RUN` for later rows.

If every pilot row is terminal, define the operational projection

```text
T_hat = 96 * mean(wall of the five B=764 rows)
      + 85 * mean(wall of the five B=1532 rows)
      + wall(2) + wall(6440) + wall(12872),

T_guard = 4 * T_hat.
```

Proceed to all 184 rows only when `T_guard <= 3600 seconds`.  The factor four
is an operational safety margin for candidate-site geometry not measured by
`B`; neither the sample nor this projection has theorem status.  During the
full sequential run, checkpoint every 16 terminal rows and stop if the same
stratified projection from completed rows exceeds the remaining one-hour
campaign budget.  Keep exact per-deletion statuses:

```text
PASS_AUTHENTICATED_COMPLETION
PASS_EXHAUSTED_NO_COMPLETION
INCOMPLETE_TIMEOUT
UNKNOWN_RESOURCE_OR_SIGNAL
NOT_RUN_PROJECTION_CAP
```

The current runner

```text
scratch/threadD_run_k16_upper12874_d4_provider_core_h100_20260731.sh
SHA-256 6b4d9a5a27636e2dfa8d54f3afebf3ef8e49d0298511c8596d8363235f0ab7de
```

defaults to all 191 ledger rows and would duplicate D3.  For this campaign it
must be invoked with the explicit pilot list and then the explicit 184-row
`E4` list.  A global-cap exit currently marks only the next row; the composer
must derive and record every remaining row as `NOT_RUN_PROJECTION_CAP` rather
than silently omitting it.

## 6. Conclusion

There is no new mathematical obstruction in passing from D3 to D4.  The
corrected provider-core engine is proof-complete for four-hole basins, and
the global all-joint certificate already supplies the complementary branch.
What remains is a finite 184-row terminal census.  The proposed pilot makes
the launch resource-safe without weakening the exact final quantifiers; an
incomplete pilot or campaign is `UNKNOWN`, while 184 terminal negative rows
compose with the frozen certificates to close precisely D4.
