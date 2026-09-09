# Exact finite results through dimension 22

The supplied words below prove six new finite equalities. Together with
the previously retained cases, `nu(k)=B(k)` is established through `k=22`.
Here `nu(k)` is the shortest word of nonzero k-bit masks whose ordinary
contiguous interval ORs include every nonzero k-bit mask.

| k | Optimal word and length nu(k) | Nonempty targets | Endpoint lower bound B(k) |
|---:|---:|---:|---:|
| 17 | [24,313](answers/k17_optimal24313.word) | 131,071 | 24,313 |
| 18 | [48,623](answers/k18_optimal48623.word) | 262,143 | 48,623 |
| 19 | [92,381](answers/k19_optimal92381.word) | 524,287 | 92,381 |
| 20 | [184,759](answers/k20_optimal184759.word) | 1,048,575 | 184,759 |
| 21 | [352,719](answers/k21_optimal352719.word) | 2,097,151 | 352,719 |
| 22 | [705,435](answers/k22_optimal705435.word) | 4,194,303 | 705,435 |

All six ordinary gaps are zero. The raw SHA-256 values are in the
[answer inventory](answers/README.md). These are user-supplied
constructions, independently verified from their literal files; no claim
is made to have reproduced the search that found them.

## A self-contained lower bound

Fix a rank `s` and let `M=binom(k,s)`. Choose one witness interval for each
of its M distinct targets. Distinct equal-rank witnesses cannot contain
one another: containment of intervals implies containment of their ORs,
and equal-sized distinct sets cannot contain one another. Thus both their
left endpoints and their right endpoints are distinct and, in the same
order, strictly increasing. In particular, the word length N satisfies
`N>=M`.

Write `N=M+t`. Number the ordered witnesses `I_i=[ell_i,r_i]`, using
one-based positions. Their endpoints satisfy

\[
i\le\ell_i\le r_i\le i+t,\qquad 1\le i\le M.
\]

Every valid interval of length `t+1` is `[i,i+t]` for some `1<=i<=M`,
and therefore contains `I_i`. Every longer interval contains one of
these windows. Consequently every target of rank less than s must use
an interval of length at most t. The number of such intervals is

\[
\sum_{j=1}^{t}(N-j+1)=tM+\frac{t(t+1)}2.
\]

The sum is zero when `t=0`. Hence, putting

\[
L_s=\sum_{j=1}^{s-1}\binom{k}{j},\qquad
\tau_s=\min\left\{t\ge0:\ L_s\le t\binom{k}{s}+\frac{t(t+1)}2\right\},
\]

where t is an integer, we obtain

\[
\nu(k)\ge B(k):=\max_{1\le s\le k}\left(\binom{k}{s}+\tau_s\right).
\]

For `k=0`, the empty word gives `B(0)=nu(0)=0`. For the six new cases,
the maximizing rank and its exact arithmetic are:

| k | Maximizing s | M | L_s | tau_s | M+tau_s |
|---:|---:|---:|---:|---:|---:|
| 17 | 9 | 24,310 | 65,535 | 3 | 24,313 |
| 18 | 9 | 48,620 | 106,761 | 3 | 48,623 |
| 19 | 10 | 92,378 | 262,143 | 3 | 92,381 |
| 20 | 10 | 184,756 | 431,909 | 3 | 184,759 |
| 21 | 11 | 352,716 | 1,048,575 | 3 | 352,719 |
| 22 | 11 | 705,432 | 1,744,435 | 3 | 705,435 |

The verifier computes every rank with exact integers and checks the
defining inequality at tau_s and its failure at tau_s-1 when tau_s>0.
Complete coverage by a word of length B(k) proves optimality.

## Complete literal verification

The standard-library [verifier](verify_word.py), for Python 3.10 or later,
uses an exact suffix recurrence. At endpoint i, every nonempty suffix is
either the single new letter or a suffix ending at i-1 with that letter
appended. Applying OR and deduplicating therefore enumerates every
ordinary interval OR. Keeping the latest start for an equal OR retains
a genuine shortest suffix witness and does not change the target set.

Suffix ORs form an inclusion chain. With nonzero letters, at most k
distinct values occur at an endpoint. The enumeration has no witness-length
cutoff and uses at most k suffix states per step. It checks mask ranges,
the complete target count, every binomial layer, the raw hash when supplied,
and equality to the all-rank lower bound. It stores no witness arrays.

Run all six files with:

```sh
for item in 17:24313 18:48623 19:92381 20:184759 21:352719 22:705435; do
  k="${item%%:*}"
  n="${item#*:}"
  python3 verify_word.py "answers/k${k}_optimal${n}.word" --k "$k"
done
```

`--sha256 HASH` checks the expected raw file identity. `--json PATH`
writes a compact report only when requested; `--allow-nonoptimal`
permits verification of a longer upper-bound word. The retained
[six-word report](answers/verification.json) records the publication check.
Earlier independent checks used both forward first-occurrence enumeration
and suffix enumeration, with separate range-OR replay of every saved witness.
The compact public check requires only these six words and this one source.

## Optimal cyclic cores and the even-dimensional lifts

Let `mu(k)` allow cyclic intervals of at most one period. The 19- and
21-dimensional files have the form `A=C+C[:3]`, where C is their initial
M letters:

| k | M=length(C)=mu(k) | length(A) | Supplied periodic lift |
|---:|---:|---:|---:|
| 19 | 92,378 | 92,381 | [184,759 letters in dimension 20](answers/k20_optimal184759.word) |
| 21 | 352,716 | 352,719 | [705,435 letters in dimension 22](answers/k22_optimal705435.word) |

Every target has an ordinary witness in A spanning at most M letters.
Reducing its start modulo M proves cyclic coverage by C. At a fixed cyclic
endpoint, suffix ORs form a chain and contain at most one target of a
given rank. Thus any universal cycle has at least `binom(k,floor(k/2))`
positions. Both displayed cores meet this bound and are optimal.

More generally, suppose `A=C+C[:d]`, with `0<=d<M`, is ordinarily universal
and C is cyclically universal. For the new coordinate `z=2^k`, form

\[
A,\ \{z\},\ C_{d\bmod M}\cup\{z\},\ldots,
C_{(d+M-2)\bmod M}\cup\{z\}.
\]

The C indices are zero-based, and the marked tail has M-1 letters
(empty when M=1).

This word has length `2M+d`. All targets omitting z occur in A, and
`{z}` occurs at the bridge. For any other target `T union {z}`, select a
cyclic witness for T of length at most M. Its ending phase appears once
among the endpoint just before the bridge and the following M-1 marked
endpoints. If it ends before the bridge, append the bridge to that suffix
of A. Otherwise its ordinary realization either lies in the marked tail
or crosses the bridge from the suffix of A. In each case its OR is exactly
`T union {z}`. This proves the lift without a construction-search premise.

For the two displayed cores, d=3, and the lifted bytes match the supplied
even-dimensional files. Reproduce both the cyclic and lift checks with:

```sh
python3 verify_word.py answers/k19_optimal92381.word --k 19 \
  --cyclic-core 92378 --lift-word answers/k20_optimal184759.word
python3 verify_word.py answers/k21_optimal352719.word --k 21 \
  --cyclic-core 352716 --lift-word answers/k22_optimal705435.word
```

The cyclic option checks the actual opening and short-witness coverage;
the lift option compares normalized decimal lines, including the final
newline, byte for byte. The 20- and 22-dimensional ordinary coverage is
also checked independently by the six-word command above.

The first open dimension remains 23. The next lower-bound targets are
`B(23)=1,352,082` and `B(24)=2,704,159`; neither is claimed attained.
These finite equalities and lifts establish no all-dimension constructor
and use no asymptotic PBBS premise.
