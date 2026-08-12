# The first two non-singleton `BDR_3959` return shells

Date: 2026-07-30

Status: **PASS TWO EXACT LENGTH-TWO/LENGTH-THREE NO-GOS; SCOPED TOKEN FLOOR
FOUR FOR CO-LOCATED AND SEQUENTIAL FIXED-FLANK ARCHITECTURES**.

The frozen source is

```text
scratch/k16_rf_halo_j_family_20260730/rank1_j3959.targets
SHA-256 edc3a3770f90140259f5e1d82c055bac634f49973aeaaff8cb06e42b18c581ee.
```

The frozen 112-row upper near-atom is

```text
scratch/threadA_k16_rf_halo_j3959_buffer_20260730/
  j3959.upper_buffer_112.targets
SHA-256 7bbb357ca2ff6bb9d1c917107561d9aac1de4de5a2ee453036a83f8b0bab09c8.
```

This note keeps that upper ray fixed.  It closes the first two
non-singleton return shells without enumerating arbitrary pairs or triples of
word positions.

## 1. Exact architecture and separation from the contiguous-block lane

In the upper near-atom the unresolved depth-three socket is

```text
...4ec5,46e5,6665,2c6d,287d,6879
       | return tokens |
   6a71,6b61,7b60,7f40,7f10,7e90,7c92,7893,7193...
```

at candidate positions `3841..3855`.  The complete upper witness cluster is
at `12710..12826` and begins

```text
eb60,ea61,ca71,4a79,4e78,...,6d70,4679.
```

For `ell=2,3`, an **exterior-token return** does the following.

1. Choose `ell` individually occurrence-labelled rank-eight rows outside
   both protected intervals.
2. Delete those occurrences, retaining the order of every other row.
3. Insert their values in a chosen order immediately after the fixed
   `6879` and before the fixed `6a71`.
4. Preserve the complete target multiset.

No adjacency or contiguity of the source tokens is assumed.  The move deletes
only the selected singleton occurrences and retains every intervening row,
so it is definitionally different from Lane K's whole contiguous-source-
block moves.  The complete physical filter additionally leaves only tokens
whose source collars are pairwise more than six rows apart; that separation
is used to make the source-closure signatures independent.

The frozen-outside-matching requirement is deliberately relaxed in this
no-go.  Every surviving tuple already fails exact middle replay and
arbitrary-upper completeness, so none can reach the Hall test.

## 2. Coordinatewise destination equation

At constant depth three, for target rows `T_i`,

\[
 E_p=T_{p-3}\cap T_{p-2}\cap T_{p-1}\cap T_p,
 \qquad
 T_i=E_i\cup E_{i+1}\cup E_{i+2}\cup E_{i+3}.          \tag{2.1}
\]

Consequently exact replay through the fixed socket is a separate binary
condition at every coordinate.  For a proposed `ell`-bit coordinate trace,
the auditor tests only (2.1), then combines the allowed coordinate states
subject to rank eight in every returned row.  This is a finite rank dynamic
program, not a search over physical row tuples.

## 3. Complete two-token shell

Write the returned rows as `X,Y`.  Equation (2.1) gives the exact table

| coordinates | allowed `(X_b,Y_b)` |
|:---|:---|
| `0,4,14` | `11` |
| `1,2,7,8,10,12,15` | `00` |
| `3,11` | `10,11` |
| `5` | `01,11` |
| `6,13` | `00,01,10,11` |
| `9` | `00,01,11` |

Imposing `|X|=|Y|=8` leaves exactly 17 ordered value pairs.  Equivalently,

```text
X in {6a59,6a39,6879,4a79},
Y in {6a71,6a39,6279,6879,4a79},
```

with the remaining bit-nine monotonicity condition.

The masks `6879,4a79,6a71` are the unique protected left flank, service
pivot, and right flank.  Every other mask in the display also occurs
uniquely.  Requiring distinct exterior occurrences leaves exactly

```text
(6a59@4718,6a39@4513),
(6a59@4718,6279@5058),
(6a39@4513,6279@5058).
```

### Theorem 3.1 (no two-token return)

None of these three occurrence-labelled returns has exact middle replay.
Their upper-hole sets are respectively

```text
{6a3b,6b39},
{6379,7279,7a79},
{6379,6a3b,6b39,7279,7a79}.
```

#### Proof

The destination socket passes (2.1) by construction.  The failures are at
the source closures.  Each donor is essential to two exact length-four
positive runs in the source:

| donor | first critical run | second critical run |
|:---|:---|:---|
| `6a59@4718` | bit 13, `[4715,4718]` | bit 0, `[4718,4721]` |
| `6a39@4513` | bit 13, `[4510,4513]` | bit 3, `[4513,4516]` |
| `6279@5058` | bit 14, `[5057,5060]` | bit 4, `[5058,5061]` |

Deleting the donor shortens each run from four to three, which cannot be
reconstructed at depth three.  The three source collars are pairwise
disjoint, so the other deletion and the exact destination insertion cannot
repair them.  Full contiguous-union replay gives the stated upper holes. ∎

## 4. Complete three-token shell

For a three-row return, equation (2.1) gives:

| coordinates | allowed three-bit patterns |
|:---|:---|
| `0` | `011,111` |
| `1,2,7,8,10,12,15` | `000` |
| `3` | `100,110,111` |
| `4,14` | `111` |
| `5` | `001,011,101,111` |
| `6,13` | every pattern except `010` |
| `9` | `000,001,011,111` |
| `11` | `100,101,110,111` |

The rank-eight dynamic program leaves exactly 84 ordered mask triples.
Protection and physical occurrence availability reduce these to exactly
seven:

```text
6a78,6a59,6a39
6a78,6a59,6279
6a78,6a39,6279
6a78,6279,6a39
6a59,6a39,6279
6a59,6279,6a39
6a39,6a59,6279.
```

Here the fourth possible exterior token is `6a78@3142`; in the upper
near-atom the corresponding candidate position is `3030`.  The other
candidate positions are

```text
6a39@4400, 6a59@4605, 6279@4945.
```

### Theorem 4.1 (no three-token return)

None of the seven triples has exact middle replay.  Every triple also has a
nonempty upper-hole set.  Therefore a co-located fixed-socket singleton-token
return block has cardinality at least four.

#### Proof

The new token has the two critical source runs

```text
6a78@3142: bit 5 on [3140,3143], bit 6 on [3139,3142].
```

Together with the three rows of Theorem 3.1, the complete source-deletion
signatures are:

| donor | bad middle rows | upper holes created |
|:---|---:|:---|
| `6a78` | 4 | none |
| `6a59` | 6 | none |
| `6a39` | 6 | `6a3b,6b39` |
| `6279` | 4 | `6379,7279,7a79` |

All four source positions are pairwise more than six apart.  Hence the
source-deletion signatures are disjoint and add without cancellation.  The
destination is exact by the pattern table, so every full replay has the
nonempty union of the relevant source signatures.  Every allowed triple
contains `6a39` or `6279`, giving a nonempty upper-hole set as well.  ∎

The previously proved singleton-return lemma closes `ell=1`.  Combining it
with Theorems 3.1 and 4.1 proves the advertised floor four.

## 5. Complementary sequential fixed-flank chains

The co-located floor is not a general return-length theorem.  A sequential
chain inserts its first token into the original `4a79` socket, then inserts
token `i+1` into token `i`'s unique source gap.  Every immediate source flank
is frozen, and all token source collars are required to be pairwise more than
six rows apart.  This is again distinct from a contiguous donor block.

The old singleton equation forces the first exterior token to be

```text
6a39@4513.
```

At its source gap the exact rank-eight filler set is

```text
683b,692b,6939,6a2b,6a39,6b29.
```

Removing the self-return leaves five two-token chains.

### Theorem 5.1 (sequential length-two/length-three no-go)

Among the five two-token chains, exactly two have exact middle replay and
none is arbitrary-upper-complete.  They are

```text
6a39 -> 692b: holes {693b,69bb,6a3b,6b39,6d2b,6dab},
6a39 -> 6b29: holes {6a3b,6ba9}.
```

For a third token, the exact fixed-flank external filler counts over second
tokens `683b,692b,6939,6a2b,6b29` are

```text
12,12,7,7,12,
```

giving 50 occurrence-labelled chains.  Exactly 14 have exact middle replay;
zero are arbitrary-upper-complete.  The best middle-exact states still have
two upper holes:

```text
6a39 -> 683b -> 682f: {6b39,6c3b},
6a39 -> 6a2b -> 6a4b: {6a5b,6b39}.
```

The only three one-upper-hole states all lie on the `6b29` branch and have
three or five middle errors.  Hence the fixed-flank sequential singleton
architecture also needs at least four exterior tokens.

#### Proof

At each stage the next filler is derived from the seven affected equations
(2.1) at the previous token's unique source position.  Occurrence,
protection, and collar-separation filtering gives the displayed `5` and `50`
catalogues.  Full variable-depth maximal-envelope and arbitrary-width upper
replay gives respectively

```text
stage two: 5 total, 2 middle-exact, 0 upper-complete;
stage three: 50 total, 14 middle-exact, 0 upper-complete.
```

Therefore no chain of length at most three meets both requirements.  ∎

The best exact-middle two-token checkpoint is materialized at

```text
scratch/threadA_k16_j3959_bdr_sequential_return_20260730/
  j3959.sequential_6a39_6b29.middle_exact.targets
SHA 12716e6c2c386669b8038b712dd53332c7a13265ecc8eb448e3b3cf2e93fe9ca.
```

It is the smallest surviving exact-middle state for a further upper-repair
attack, but it is not a `BDR_3959` completion because `6a3b,6ba9` are absent.

## 6. Frozen matching transport state

The fixed 112-ray move transports old cells by exact occurrence-labelled
erosion/dependency keys.  Of the frozen size-26,329 matching,

```text
25,971 edges survive unchanged,
358 enter the residual bank = 336 moved-ray interior + 22 seam/A cells.
```

All six old `9/6` shore cells and all seven cells used by the conditional
involution reroutes survive.  A later insertion at the original socket must
conservatively unfreeze thirteen further transported owners:

```text
4485,4685,46c5,4645,4665,2465,2065,
6b40,7b40,7300,7f00,5e00,7e10.
```

This is the exact **baseline** matching state for a future positive
candidate; a concrete return must additionally unfreeze and replay each of
its source collars.  It is not a Hall certificate for any present return:
every candidate has already failed middle or upper replay.

## 7. Exact boundary

The result is stronger than a frozen-matching no-go on its face: matching
constraints were never invoked.  It proves:

> **Co-located disjoint-token floor.**  In the fixed 112-ray, fixed-socket,
> residual-order architecture, an exact return block inserted wholly into
> the original `4a79` socket cannot use one, two, or three individually
> labelled exterior row occurrences.

It does not exclude:

- four or more exterior tokens;
- moving a protected socket or upper-ray row;
- changing either source flank;
- a non-residual segment rethread; or
- an interacting contiguous donor block, which belongs to Lane K's separate
  model.

Theorem 5.1 separately closes sequential fixed-flank chains of length at
most three.  The next genuinely new faces are therefore a four-token
co-located return, a four-token sequential return, an interacting-collar
chain, or a protected-flank commutator.  Frozen matching constraints enter
only after exact middle and upper replay survive.

## 8. Authenticated artifacts

```text
scratch/threadA_k16_j3959_bdr_disjoint_token_return_20260730/
  audit_j3959_bdr_disjoint_token_return.py
    SHA 8040f039272c3de9e9cba3e963abf0125e6b2c02b70bf57391c354cc6f29370e
  j3959_bdr_disjoint_token_return.audit.json
    SHA 52c02be1832a6b258d945f84ef22314e30be3f73b07a291dc7d1195320325c55
    payload 1acbcf59ac28dcea5c1c30b2e9f9a0dec90503cf3984afca0bb07d1a52a0d89c
  j3959_bdr_disjoint_token_return.catalogue.tsv
    SHA 5779dfedba7a64575b2fc146645843af431df555e7249dc2d409d48f80466692
```

The audit independently derives both per-coordinate tables, the `17 -> 3`
and `84 -> 7` reductions, every source-deletion signature, every upper-hole
set, and the complete full-path replay of all ten physical candidates.

Sequential fixed-flank census:

```text
scratch/threadA_k16_j3959_bdr_sequential_return_20260730/
  audit_j3959_bdr_sequential_return.py
    SHA 85fe4e27643fb332d136212bec5959596af782db295a02d7811698e8eddb5325
  j3959_bdr_sequential_return.audit.json
    SHA 214837542b2679ca48c47b23df30a4660d622c4d137347ddb81d4ab12bb92f2f
    payload 7b9ee4845bb6b88642fde8dd784a49178ce5d1a661c2fe8998b897f8c8d81805
  j3959_bdr_sequential_return.catalogue.tsv
    SHA 0901922291230e2bb62b3844f17e98bb4d8cb94d7a9fa8bb3cc2aa81eac7418f
  j3959.sequential_6a39_6b29.middle_exact.targets
    SHA 12716e6c2c386669b8038b712dd53332c7a13265ecc8eb448e3b3cf2e93fe9ca
  j3959.sequential_6a39_683b_682f.middle_exact.targets
    SHA 1a794ca8137d33186fb61bb3cccbb5f2333fbc7acaa1765151d5e70622b1cad6
  j3959.sequential_6a39_6a2b_6a4b.middle_exact.targets
    SHA 8bbd46e2c63f0e6ead6b73c5134ee28083b193d5c1ac2956aadc5dfd703e18ee
```

Frozen matching transport:

```text
scratch/threadA_k16_j3959_bdr_disjoint_token_return_20260730/
  audit_j3959_fixed_ray_matching_transport.py
    SHA e7a03919049778f0d8598f0e35973e083d5d9a7e153bfb5afdfb0ee27c845581
  j3959.fixed_ray_matching_transport.audit.json
    SHA 1d114c64aeae23a018a8e811e17357728fc4c901ede3efd33580fc10b5783346
    payload 469b4d8944f23158c2a76acfbdab7b994119f6dbbf3c754513d4d76babadc86c
```

## 9. Independent adversarial audit

An independent reconstruction passed every substantive count and replay.
In particular, it recovered:

```text
original socket fillers: {4a79,6879,6a39};
6a39-source fillers:     {683b,692b,6939,6a2b,6a39,6b29};
third-stage raw counts:  15,15,10,10,15;
third-stage external counts: 12,12,7,7,12.
```

It independently reproduced the co-located reductions `17 -> 3` and
`84 -> 7`, the sequential replay totals `5/2/0` and `50/14/0`, both
two-hole exact-middle checkpoints, and the three one-hole but middle-bad
states.  All file and payload hashes in Section 8 recomputed exactly.

The audit also checked the logical scope.  Every enumerated move preserves
the complete occurrence multiset by construction.  The no-go is valid for
the frozen-outside-matching subfamily because it was proved on the larger
family obtained by dropping matching constraints: every member already
fails middle or upper replay.  Conversely, the `25,971/358 + 13` matching
ledger is only the exact fixed-ray/socket baseline.  A concrete future
return must additionally unfreeze and re-audit the matching cells in each
changed donor-source collar.  Thus neither theorem is a general
`BDR_3959` return-length lower bound, and no present candidate has a Hall-0
claim.
