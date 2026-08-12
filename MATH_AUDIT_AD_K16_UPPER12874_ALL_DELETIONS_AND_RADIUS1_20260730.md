# Independent audit of the K16 length-12874 deletion census and best-basin radius one

Date: 2026-07-30  
Lane: AD  
Status: **PASS, with strictly source-relative scope**

## 1. Frozen objects

The independently replayed word is

- `answers/k16_upper12874.word`, length (12874), SHA-256
  `631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e`.

The audited producer artifacts are

- deletion driver `scratch/audit_ad_k16_upper12874_deletion_census_20260730.py`,
  SHA-256 `fc8ce6aec17be6ad7a0bb072fd04332361394896e7dbe4312d55178656baf348`;
- deletion JSON `scratch/k16_upper12874_deletion_census.audit.json`,
  SHA-256 `c2990f25c9ef15d7c3a4ddc5eda5f5ca4ce60e75dabe93dfc8c4988b349cd619`,
  internal payload SHA-256
  `b117af6ec989f01ec619c6f9c902ef77a249b4c9abd4f40164c3b6199f3cc995`;
- best deletion word `scratch/k16_upper12874_best_delete.word`, length (12873),
  SHA-256 `a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649`;
- radius-one driver
  `scratch/audit_ad_k16_12873_phase_delete_one_substitution_exact_20260730.py`,
  SHA-256 `cbfcce2d1d52904364b260b0507875fe59df96ded8ee46b138b7a01591cf6ec6`;
- radius-one JSON `scratch/k16_12873_phase_delete_radius1.audit.json`,
  SHA-256 `475f35023004eb7402bfb7da42135b26f277a8bf3ccf3eb904b89af4d31196f2`,
  internal payload SHA-256
  `cfe4702fb00ae7271c9183f5bc98c1e0eb0d8b682bc1a27b36ac079754a09293`.

The independent implementation is

- `scratch/audit_ad_k16_upper12874_deletion_radius1_independent_20260730.py`,
  SHA-256 `fbae8e0b42c9a3c4a4e7a35554f33c249f95f657a108e98b2b841e6c8570e30d`;
- independent JSON
  `scratch/ad_k16_upper12874_deletion_radius1_independent_20260730.audit.json`,
  SHA-256 `2c3cc484afbf2fd07aae1a9c99f8c110ece941b7f7608f44fce0c0d7c4360fe6`,
  internal payload SHA-256
  `be708b9fd2212cf360ff420189a72302a7f0a4fce29f79109d20645d3fc57a13`.

The independent code does not import either producer's recurrence core. It
pins every input and producer hash above and reconstructs the producer's
complete deletion-record digest.

## 2. Exact cut criterion

Let (w=(x_0,\ldots,x_{n-1})).  For a nonzero target mask (t), let

\[
 \lambda_t=\max\{i:\bigvee_{k=i}^{j}x_k=t\text{ for some }j\},\qquad
 \rho_t=\min\{j:\bigvee_{k=i}^{j}x_k=t\text{ for some }i\}.
\]

### Lemma 2.1 (all witnesses cross one position)

Assume (t) occurs. Every interval witnessing (t) contains position (p)
if and only if

\[
                 \lambda_t\le p\le\rho_t.
\]

#### Proof

The intersection of all witness intervals has left endpoint equal to the
maximum witness start (lambda_t) and right endpoint equal to the minimum
witness end (ho_t). Thus (p) belongs to every witness exactly on the
stated integer interval. (square)

Both extrema were computed independently. A forward suffix-OR recurrence
records the first right endpoint at which each target occurs; a backward
prefix-OR recurrence records the last left endpoint at which it occurs. The
largest state-chain sizes were (11) forward and (12) backward.

### Lemma 2.2 (exact deletion join)

Delete (x_p). Put

\[
 A_p=\{\bigvee_{k=i}^{p-1}x_k:0\le i<p\},\qquad
 B_p=\{\bigvee_{k=p+1}^{j}x_k:p<j<n\}.
\]

The targets lost by the deletion are exactly

\[
 \{t:\lambda_t\le p\le\rho_t\}
 \setminus \{a\mathbin\vee b:a\in A_p, b\in B_p\}.
\]

#### Proof

A target outside the first set has an old witness avoiding (p), which
survives unchanged. Every new interval created by closing the cut consists
of a nonempty suffix on the left followed by a nonempty prefix on the right,
and hence has OR (a\vee b). Conversely every such pair is a literal new
interval. (square)

This proof uses Boolean OR labels, not multiplicity deltas. For the stronger
record-level comparison, the independent audit also formed the union of all
removed labels (a\vee x_p\vee b), with either side optionally empty, and
all added labels (a\vee b), with both sides nonempty. That union is exactly
the key set retained by the producer's delta dictionary, including a label
whose net delta cancels. The resulting digest of all 12,874 detailed records
is exactly

`6a2f1697d3cb5819205407e591a77faf803cd09ecdc61e70a1277d3bee54aa96`.

## 3. All-deletion result

### Theorem 3.1 (frozen-word deletion no-go)

Every one-cell deletion of the frozen length-12874 word is nonuniversal. The
minimum number of missing masks is (1), attained uniquely at zero-based
position (p=1), where the deleted letter is (10240=\mathtt{0x2800}). The
resulting length-12873 word misses exactly

\[
                   11373=\mathtt{0x2c6d}.
\]

The independent literal suffix recurrence replays that sole hole. The full
hole-count histogram is

| holes | deletions | holes | deletions | holes | deletions |
|---:|---:|---:|---:|---:|---:|
| 1 | 1 | 2 | 3 | 3 | 3 |
| 4 | 184 | 5 | 931 | 6 | 1638 |
| 7 | 1889 | 8 | 1995 | 9 | 1655 |
| 10 | 1132 | 11 | 774 | 12 | 639 |
| 13 | 738 | 14 | 499 | 15 | 366 |
| 16 | 190 | 17 | 176 | 18 | 3 |
| 19 | 58 |  |  |  |  |

The maximum number of touched labels at any cut is (83); the unique best
cut touches (17).

## 4. Exact arbitrary replacement criterion

Let (v) be the best deletion word, whose unique pre-existing hole is
(h=\mathtt{0x2c6d}). For a replacement position (p), define

\[
 R_p=\{h\}\cup\{t:t\text{ occurs in }v\text{ and }
                         \lambda_t\le p\le\rho_t\}.
\]

Let (A'_p) be zero together with the nonempty suffix ORs to the left of
(p), and let (B'_p) be zero together with the nonempty prefix ORs to its
right.

### Lemma 4.1 (replacement equivalence)

Replacing (v_p) by a nonzero mask (u) produces a universal word if and
only if

\[
 R_p\subseteq\{a\vee u\vee b:a\in A'_p, b\in B'_p\}.
\]

Moreover every successful (u) obeys

\[
                    u\subseteq\bigcap_{t\in R_p}t.
\]

#### Proof

Every target outside (R_p) has an old witness avoiding (p), hence remains
covered. Every new witness for a target in (R_p) must contain the replaced
cell and has exactly the displayed suffix-cell-prefix form; every displayed
form is a literal interval. If it equals (t), necessarily every bit of
(u) is a bit of (t). Intersecting over (R_p) gives the last condition.
(square)

Consequently it is exhaustive to enumerate the nonzero submasks of the
intersection, not all (65535) masks at every position. The audit still
covers arbitrary legal replacement masks: the submask condition is
necessary, and the displayed equality test is necessary and sufficient.
The unchanged letter is included whenever it satisfies this necessary
condition; the zero mask is correctly excluded from the word alphabet.

## 5. Best-basin radius-one result

### Theorem 5.1 (exact scoped radius-one no-go)

No word obtained from the fixed best deletion word by replacing at most one
position by an arbitrary nonzero 16-bit mask is universal.

The independent recurrence exactly reproduces:

- (51,285) vulnerable covered targets;
- residual-set size between (3) and (20);
- at most (58) distinct suffix-prefix bases at a position;
- (77,153) tested replacement masks;
- zero successful candidates.

The residual-size histogram is

`3:2, 5:1, 6:2, 7:1, 8:23, 9:221, 10:478, 11:1128, 12:1646, 13:2075, 14:2080, 15:1956, 16:1447, 17:781, 18:631, 19:223, 20:178`.

The histogram of numbers of necessary nonzero submasks per position is

`0:256, 1:1861, 3:4486, 7:4439, 15:1631, 31:197, 63:3`.

As a checksum,

\[
 1861+3(4486)+7(4439)+15(1631)+31(197)+63(3)=77153.
\]

## 6. Payload-hash audit detail

Both producer payload hashes replay. The radius-one producer hashed its two
`Counter` dictionaries while their keys were Python integers; JSON converts
those keys to strings on disk. Replaying that internal payload therefore
requires restoring integer keys before applying the producer's canonical
`json.dumps(..., sort_keys=True, separators=(",", ":"))`. This is a
serialization-type caveat, not a mathematical or certificate discrepancy.
The deletion producer had already converted its histogram keys to strings.

## 7. Exact boundary of the conclusion

The proved statements are source-relative:

1. no deletion of this particular length-12874 certificate is universal;
2. in its unique minimum-hole deletion basin, no arbitrary single
   substitution repairs universality.

This is **not** a proof that no other length-12873 word is universal. It is
also not a no-go for a deletion plus a substitution based at any of the
other 12,873 deletion positions, nor for two or more edits of the best basin.
Thus it does not by itself raise the global lower bound beyond (12873).

