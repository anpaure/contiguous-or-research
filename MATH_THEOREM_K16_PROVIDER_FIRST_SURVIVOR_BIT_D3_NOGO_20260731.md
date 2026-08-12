# K16 provider-first survivor-bit index and exact D3 radius-two no-go

Date: 2026-07-31  
Status: exact scoped theorem; independent one-thread/four-thread replay  
Global bracket: `12873 <= nu(16) <= 12874` (unchanged)

## 1. Result

Fix the verified universal word

```text
answers/k16_upper12874.word
length 12874
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e.
```

For each of the seven deletions whose deletion word has at most three holes,
there is no universal length-12873 word obtained by changing two distinct
surviving cells to arbitrary nonzero 16-bit masks.  The deletion indices are

```text
D3 = {0, 1, 3, 6389, 6441, 12871, 12873}.
```

The previously frozen all-joint theorem closes the branch in which every
original deletion hole has a final witness containing both changed sites.
The new census closes the exact complementary provider-first branch, including
all partial providers.  The old one-substitution theorem closes no-op corners.

This is not a global radius-two theorem: the other 12,867 deletions remain
outside the present provider-first census.

## 2. Exact first-edit notation

Let `W` be one deletion word, `H` its nonempty hole set, and replace the cell
at position `p` by `u`.  For a target `t`, let `C_t(p)` be the OR of

1. the maximal suffix immediately to the left of `p` consisting of cells
   contained in `t`; and
2. the maximal prefix immediately to the right of `p` consisting of cells
   contained in `t`.

Define the Boolean service interval

```text
I_t(p) = [ t minus C_t(p), t ].                         (2.1)
```

If `t` is absent before the edit, the edit supplies `t` exactly when
`u in I_t(p)`.  If `t` is present and all its witnesses contain `p`, the
edit preserves `t` exactly when `u in I_t(p)`.  A covered target can become
missing only in this latter, vulnerable case.

Let `V_p` be the exact set of vulnerable covered targets.  It is obtained from
the witness core

```text
K(t) = intersection of every interval witnessing t.
```

Thus `t in V_p` iff `p in K(t)`.

## 3. Survivor-bit theorem

Let `D(p,u)` be the exact nonempty missing family after the first edit.  A
second substitution can complete the word only if

```text
J(p,u) = intersection D(p,u) != 0,                     (3.1)
```

because its nonzero new cell is contained in every target it repairs.

> **Theorem (survivor-bit characterization).** A genuine first edit `(p,u)`
> is provider-first and satisfies (3.1) iff there is a coordinate bit `b`
> such that
>
> 1. `u` services at least one original hole;
> 2. `u in I_h(p)` for every `h in H` with `b notin h`; and
> 3. `u in I_t(p)` for every `t in V_p` with `b notin t`.

**Proof.** If `b in J(p,u)`, every target missing after the edit contains
`b`.  Hence every original hole and every vulnerable covered target not
containing `b` must have been supplied or preserved, proving 2--3; provider
first gives 1.

Conversely, conditions 2--3 say that every original hole or vulnerable target
not containing `b` remains covered.  Those are the only targets whose status
can change.  Consequently every member of `D(p,u)` contains `b`, so
`b in J(p,u)`.  Condition 1 gives provider-first.  QED.

This is an exact provider-position index, not a heuristic quotient.  It does
not identify two literal first values or discard their distinct transition
profiles.

## 4. Boolean-interval compression

For fixed `(p,b)`, conditions 2--3 are an intersection of Boolean intervals.
Put

```text
L_{p,b} = OR   { t minus C_t(p) :
                 t in V_p union H and b notin t },
U_{p,b} = AND  { t :
                 t in V_p union H and b notin t }.       (4.1)
```

The mandatory bit-safe domain is exactly `[L_{p,b},U_{p,b}]`; it is empty iff
`L_{p,b}` is not a submask of `U_{p,b}`.  If some original hole omits `b`,
the provider condition is already included.  Otherwise intersect this base
interval with the small union

```text
union_{h in H} I_h(p).                                  (4.2)
```

Therefore the complete set of provider-first edits with nonzero intermediate
debt intersection is a union of at most 16 small Boolean-interval banks per
physical position.  This avoids the unsound supplied-hole/debt quotient from
the earlier obstruction theorem: literal values remain distinct, but only
values surviving the necessary second-cell intersection are emitted.

The independent D3 index audit constructs witness cores from the complete
interval enumeration, evaluates (4.1)--(4.2), enumerates each union once, and
then checks every literal provider submask directly.  The symbolic and direct
sets agree exactly on all seven deletion words.

## 5. Exact counts

| deletion | holes | all providers | `J != 0` | second positions | pair checks |
|---:|---:|---:|---:|---:|---:|
| 0 | 2 | 42,491 | 41,470 | 13,581 | 36,407 |
| 1 | 1 | 27,064 | 27,064 | 251,932 | 646,720 |
| 3 | 2 | 41,749 | 40,907 | 266 | 1,997 |
| 6389 | 3 | 68,555 | 64,267 | 12 | 16 |
| 6441 | 3 | 103,102 | 101,134 | 169 | 1,097 |
| 12871 | 3 | 1,133,158 | 1,124,558 | 6,107 | 34,396 |
| 12873 | 2 | 79,413 | 78,956 | 1,775 | 20,908 |
| **total** | | **1,495,532** | **1,478,356** | **273,842** | **741,541** |

Only `2,754` of the `1,478,356` surviving first edits have a debt
intersection disjoint from the original common-hole mask.  This empirical
concentration is not used as a theorem or pruning rule.

For each retained first edit, the exact second-position engine chooses a debt
whose required context is strongest, indexes every source position able to
supply that context, and adds precisely the compatible components whose
status can change because of the first edit.  At a retained second position it
forms

```text
lower = OR_{t in D(p,u)} (t minus C_t(q)),
upper = intersection D(p,u),                            (5.1)
```

enumerates every genuine nonzero value in `[lower,upper]`, and evaluates the
full signed two-site multiplicity delta.  A zero-hole row would then receive a
literal replay; none occurred.

The one-thread local and four-thread H100 runs agree on every mathematical
count for the six remotely rerun deletions.  Deletion 1 was additionally
replayed locally and matches the previously audited 27,064-row transition
census.

## 6. Authentication

Primary audit:

```text
scratch/k16_provider_first_survivor_bit_d3_20260731.audit.json
  SHA-256 260ea3fff384437c9bcd8db3f1926d2dce304915cb59ddee99c38c3601bc7b39
```

Symbolic/direct survivor-bit census:

```text
scratch/audit_k16_provider_first_survivor_bit_d3_20260731.cpp
scratch/k16_provider_first_survivor_bit_d3_20260731.tsv
scratch/audit_k16_provider_first_survivor_bit_d3_results_20260731.py
```

Exact replay outputs:

```text
scratch/k16_provider_first_survivor_bit_d3_20260731/
```

The audit authenticates the source and all seven derived deletion-word hashes,
checks symbolic interval unions against direct provider/debt intersections,
checks all terminal statuses and empty solution records, and compares the
one-thread and four-thread mathematical ledgers.

## 7. Scope

The result proves a D3 neighborhood theorem for one fixed length-12874 parent.
It does not prove `nu(16)=12874`, does not exclude two substitutions after any
of the other 12,867 deletions, and does not cover three or more substitutions,
reordering, a different parent, or a structurally unrelated length-12873 word.

