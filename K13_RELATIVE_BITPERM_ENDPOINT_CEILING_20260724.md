# Exact ceiling for the k13 relative-bit-permutation endpoint family

## Result

For the 926-entry word in `k12_optimal_nonzero.txt`, consider every candidate
of the form

```text
base || 4096 || (4096 | pi(base[1])) || ... || (4096 | pi(base[924]))
```

where `pi` is any permutation of the twelve old bit coordinates.  The lifted
copy may also be reversed before deleting its two endpoints.  No candidate in
either orientation covers all 4096 upper residues.  In fact its upper-residue
score is always at most

```text
4094 / 4096.
```

This covers all `12! = 479001600` relative bit maps.  The ceiling is a set
invariant, so an exhaustive lexicographic RunPod enumeration is unnecessary.

## 1. The four relative holes

The ORs of all intervals wholly inside `base[1..924]`, including residue zero
for the new singleton, cover exactly 4092 residues.  The four holes, written as
sets of bit positions, are

```text
A =  801 = {0,5,8,9}
B =  881 = {0,4,5,6,8,9}
C = 1616 = {4,6,9,10}
D = 1876 = {2,4,6,8,9,10}.
```

Thus `A` is a proper subset of `B`, and `C` is a proper subset of `D`.
Reversing the lifted internal word does not change its interval-OR family.  A
bit permutation `pi` changes the four holes to `pi(A), pi(B), pi(C), pi(D)`.

## 2. What a crossing interval can repair

The distinct suffix ORs of the unchanged lower copy are

```text
801, 881, 889, 1913, 3961, 3963, 4091, 4095.
```

Only the first two have size at most six.  Therefore a crossing interval that
repairs one of the four transformed holes must use lower suffix `A` or `B`.
Put

```text
X = pi^{-1}(A),   |X|=4,
Y = pi^{-1}(B),   |Y|=6.
```

Necessarily `X` is a subset of `Y`.

If a transformed rank-four hole `pi(E)`, where `E` is `A` or `C`, is repaired,
the lower suffix must be the rank-four set `A`, already equal to the target.
Consequently `X=E`.  At most one of the two rank-four holes is repaired.

Every repaired transformed rank-six hole `pi(F)`, where `F` is `B` or `D`,
must contain the chosen lower suffix.  Pulling back by `pi`, it follows in all
cases that `X` is a subset of `F` (if suffix `B` is used, then `Y=F` and still
`X subset Y`).

Now:

* if the rank-four hole `pi(A)` is repaired, then `X=A`; but `A` is not a
  subset of `D`, so `pi(D)` cannot be repaired;
* if the rank-four hole `pi(C)` is repaired, then `X=C`; but `C` is not a
  subset of `B`, so `pi(B)` cannot be repaired;
* if neither rank-four hole is repaired, only the two rank-six holes remain.

In every case at most two of the four holes are repaired.  Hence the score is
at most `4092+2=4094` for every permutation and for both orientations.

## 3. Exact all-permutation quotient

For completeness, crossing coverage depends on `pi` only through the nested
pair `(X,Y)`.  There are

```text
C(12,4) C(8,2) = 13860
```

such pairs, and each is induced by exactly

```text
4! 2! 6! = 34560
```

bit permutations.  Exhausting these 13,860 pairs gives the following exact
score distributions over all `12!` maps:

| lifted orientation | score 4092 | score 4093 | score 4094 |
|---|---:|---:|---:|
| forward | 467,735,040 | 10,229,760 | 1,036,800 |
| reversed | 462,101,760 | 15,897,600 | 1,002,240 |

The executable audit is
`scratch/audit_k13_relative_bitperm_endpoint_ceiling.py`.  It independently:

1. derives the four internal holes from the supplied base word;
2. derives the suffix and forward/reverse prefix chains;
3. exhausts all 13,860 nested-pair quotient states;
4. expands the quotient histogram to exactly `12!` maps;
5. runs the original direct evaluator logic on the identity, all 66 bit
   transpositions, and all 440 oriented 3-cycles in both orientations.

Run it with

```bash
python3 scratch/audit_k13_relative_bitperm_endpoint_ceiling.py \
  k12_optimal_nonzero.txt
```

## 4. Audit of the sampling program

`scratch/k13_relative_bitperm_endpoint_search.cpp` correctly evaluates this
specific family:

* `add(0)` represents the literal high singleton;
* the rolling OR chains enumerate all intervals within lifted positions
  `1..924`;
* lower suffixes alone cover crossings ending at the singleton;
* lower suffix OR lifted prefix covers every other crossing interval;
* the writer emits exactly `926+1+924=1851` entries.

Its `make_permutation` routine is deterministic random sampling, not a
lexicographic enumeration, and different indices can generate the same map.
That is acceptable for sampling but cannot certify exhaustion.  The invariant
above proves the complete result instead.  Therefore this program can never
write a candidate: its success test requires score 4096, whereas its family has
the proved ceiling 4094.

## Scope

The no-go result applies only to the endpoint-deleted, single-interface,
relative-bit-permuted lift described above.  It does not exclude:

* another deletion pair;
* edits to one or more retained lifted entries;
* a non-bit-permutation relabeling;
* multiple interfaces or a different k13 architecture.
