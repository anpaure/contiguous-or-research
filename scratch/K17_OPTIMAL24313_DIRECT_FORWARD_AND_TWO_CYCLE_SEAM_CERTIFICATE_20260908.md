# Exact k17 optimum: independent direct-forward and two-cycle verification

2026-09-08. The actual supplied word was independently checked by `exact_b_finite_frontier`, using direct forward interval-OR scans only. Every requested literal and seam claim passed.

\[
\boxed{\nu(17)=B(17)=24,313.}
\]

This is a finite exact result. Its proof needs neither the asymptotic coefficient-one arguments nor the unavailable quotient-row/search package.

## 1. The actual word and exhaustive upper-bound check

The supplied file is `/Users/amir.nuriyev/Downloads/k17_optimal24313.word`. A byte-identical copy is retained at
[k17_optimal24313.word](k17_optimal24313_forward_20260908/k17_optimal24313.word).

Its SHA-256 is exactly

`7d85f8494084c7eb3f4b196159f3a5b5b020a0170e26ad0e34c6087bda525ff9`.

It has exactly 24,313 nonzero integer letters, each in `[1,131071]`. The independent checker starts at every left endpoint, advances the right endpoint one position at a time, and accumulates bitwise OR. It stops a scan only after reaching the full set, because every longer extension then has the same OR. Near the end of the word it scans to the actual final position. No wrapped interval is used.

The scan visits exactly **552,396** ordinary intervals and finds every one of the **131,071** nonempty masks. The number of distinct targets at each rank r is exactly `binom(17,r)`. One concrete nonwrapping interval is retained for every target.

This checker uses neither the suffix recurrence nor a segment tree. The root agent performs a separate check using those different algorithms.

## 2. Matching lower bound

Let `W=binom(17,9)=24310`. A word covering all W distinct nine-sets needs at least W positions: the suffix unions ending at one position are nested and therefore contain at most one distinct nine-set.

Suppose its length is N=W+t. Select one interval for each nine-set and order them by left endpoint. Distinct selected intervals cannot contain each other, so their right endpoints have the same strict order. With one-based indices, their endpoints obey

\[
i\le\ell_i\le r_i\le i+t.
\]

Thus every window `[a,a+t]`, `1<=a<=W`, contains the selected nine-set interval indexed by a. Any interval of length at least t+1 therefore contains a nine-set. Targets of rank below nine must use intervals of length at most t, of which there are

\[
tW+\binom{t+1}{2}.
\]

There are

\[
\sum_{r=1}^{8}\binom{17}{r}=65535
\]

distinct required lower targets. For t≤2 the available interval count is at most

\[
2W+3=48623<65535.
\]

Consequently N≥W+3=24313. The actual checked word attains that lower bound. The endpoint proof, including the valid window range and t=0 case, was separately reviewed by `exact_b_induction`.

## 3. The exact split and five seam witnesses

Let V be the first 86 letters and Z the remaining 24,227. Each block was scanned separately by the same direct forward algorithm:

| Block | Length | Distinct internal targets | Forward intervals scanned |
|---|---:|---:|---:|
| V | 86 | 639 | 1,911 |
| Z | 24,227 | 130,747 | 549,866 |

Their internal target union has size 131,066. Its exact five missing masks are

\[
27299,\quad27303,\quad27315,\quad27319,\quad29363.
\]

The last three letters of V and first three of Z are exactly

\[
(19076,19106,8834\mid25249,689,12849).
\]

Direct OR accumulation verifies the following five crossing intervals. Global positions are **one-based and inclusive**.

| Target | Rank | Local interval in the six letters | Global interval |
|---:|---:|---|---|
| 27299 | 8 | [2,4] | [85,87] |
| 27303 | 9 | [1,4] | [84,87] |
| 27315 | 9 | [2,5] | [85,88] |
| 27319 | 10 | [1,5] | [84,88] |
| 29363 | 9 | [3,6] | [86,89] |

Every other target already has an internal witness in V or Z. These five equalities therefore give a second finite decomposition of the upper-bound proof: the two internal censuses plus one join.

## 4. The two genuine cyclic words reconstructed from the literal file

Define Q as the first 85 letters and R as `word[86:-2]` in zero-based Python slicing. Their lengths are 85 and 24,225. The file itself verifies

\[
\text{word}=Q\Vert Q_0\Vert R\Vert R_0\Vert R_1.
\]

In particular, the 86th letter equals the first letter of Q, and the final two letters equal the first two letters of R. This decomposition uses exactly three copied positions beyond the total cyclic length W=24,310.

The independent cyclic checks are also direct forward scans: use a doubled period, start at each original cyclic position, and stop upon the full set or after one period, whichever comes first. They establish

| Cyclic word | Period length | Distinct cyclic targets | Direct intervals scanned |
|---|---:|---:|---:|
| Q | 85 | 664 | 2,210 |
| R | 24,225 | 130,748 | 550,409 |

Their target union is all 131,071 nonempty masks. Across Q and R together, all 24,310 cyclic three-letter windows are distinct eight-sets, and all 24,310 cyclic four-letter windows are distinct nine-sets. Both decks enumerate their complete layers exactly once.

Thus the claimed two-cycle opening mechanism is verified directly from the actual delivered word. The original quotient generator, its phase labels, and the asserted search history are not required for this conclusion and were not independently regenerated.

## 5. Exact ordinary short-window census

The checker separately accumulates every ordinary window of lengths one through five, without wrapping:

| Window length | Number of windows | Ranks present | Distinct targets |
|---:|---:|---|---:|
| 1 | 24,313 | 1 through 6 | 21,777 |
| 2 | 24,312 | 7 only | 19,448 |
| 3 | 24,311 | 8 only | 24,310 |
| 4 | 24,310 | 9 only | 24,310 |
| 5 | 24,309 | 10 only | 19,448 |

The literal-letter occurrence counts at ranks one through six are respectively 17, 136, 680, 2,381, 6,189 and 14,910; their distinct counts are exactly the required binomial layer sizes. The report retains all these occurrence and distinct-target counts separately.

The nine-layer capacity is saturated: every four-letter window is a different nine-set, and there are exactly W such windows. The first three endpoints cannot support a nine-set suffix, since their entire prefix has rank at most eight. Every later endpoint has its fresh four-letter nine-set; longer suffixes have rank at least ten because every five-letter window has rank ten.

Higher ranks were included in the exhaustive full-word scan, rather than inferred from the short-window table.

## 6. Reproducible artifacts and execution record

- [Independent direct-forward verifier](verify_k17_optimal24313_direct_forward_20260908.py).
- [Complete report](k17_optimal24313_forward_20260908/k17_optimal24313_direct_forward_certificate.json).
- [One direct-forward interval witness for every target](k17_optimal24313_forward_20260908/k17_optimal24313_direct_forward_witnesses.json).
- [Byte-identical word](k17_optimal24313_forward_20260908/k17_optimal24313.word).

The proof text supplied by the user was read at `/Users/amir.nuriyev/.codex/attachments/75a4f2eb-4f95-4711-8ce2-041c4ed52851/pasted-text.txt`; none of the user's verifier code was used.

The script ran once on h100 (`arboghast`) with limits of 30 CPU seconds, 45 wall seconds and 1 GiB address space. It returned PASS in approximately 0.406 seconds. All mathematical operations were exact integer OR scans, counts and binomial coefficients. Only elapsed-time metadata uses floating point.

Remote artifacts are in `/home/amodo/exact-b-k17-optimal24313-forward-20260908/`. No mathematical process remains running.

This closes the exact dimension-17 case. Combined with the previously established cases it extends attainment through k=17; it does not prove equality in every dimension.
