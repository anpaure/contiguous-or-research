# Independent audit of the fixed K16 length-12,874 radius-one no-go

Date: 2026-07-30

## Verdict and exact scope

**PASS.**  Let (w) be the fixed raw word

```text
scratch/ad_k16_ripple_insert12874_onehole_20260730.word
```

of length `12874` and SHA-256

```text
5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db.
```

Its exact nonzero missing-mask family is the singleton

\[
                         \{0x287d\}.
\]

No word obtained from this fixed word by changing at most one position to an
arbitrary nonzero 16-bit mask is universal.  This is a source-relative
radius-one theorem.  It is not a two-edit no-go and not a global impossibility
for all length-12,874 words.

## Exact witness-extrema criterion

For a covered target (t), let

\[
 L_t=\max\{\ell:[\ell,r]\text{ is an old witness of }t\},\qquad
 R_t=\min\{r:[\ell,r]\text{ is an old witness of }t\}.
\]

Replacing position (p) destroys every old witness of (t) if and only if

\[
                            L_t\le p\le R_t.                 \tag{1}
\]

Indeed, (p) belongs to every old interval precisely when it is at least
every left endpoint and at most every right endpoint.  If (L_t>R_t), no
single position meets all old witnesses of (t).

The independent checker computes (R_t) in a left-to-right suffix-OR pass and
(L_t) in a separate right-to-left prefix-OR pass.  This differs from the
primary driver's one-pass extrema ledger.  Both directional chains have
maximum size 12 and agree on coverage of all 65,535 nonzero labels.

At position (p), put

\[
 A_p=\{0x287d\}\cup\{t:L_t\le p\le R_t\}.
\]

Every target in (A_p) requires a new witness through the replacement value
(u).  Consequently

\[
                       0\ne u\subseteq\bigcap_{t\in A_p}t     \tag{2}
\]

is necessary.  Conversely, every new interval through (p) has the exact
form

\[
                         a\lor u\lor b,                       \tag{3}
\]

where (a) is an old suffix OR ending at (p-1), or zero, and (b) is an
old prefix OR beginning at (p+1), or zero.  Thus a value satisfying (2)
repairs the word if and only if every member of (A_p) occurs among the
labels (3).  Equations (1)--(3) give an iff test for one arbitrary
substitution.

## Exact census

The independent replay obtains:

```text
initial hole                         0x287d
covered targets vulnerable somewhere 51287
minimum / maximum |A_p|              3 / 20
maximum suffix or prefix states       12
maximum left-right join bases         58
explicit necessary submasks tested    77303
passing substitutions                 0
```

The per-position necessary-submask histogram is

| candidate values at a position | number of positions |
|---:|---:|
| 0 | 245 |
| 1 | 1820 |
| 3 | 4553 |
| 7 | 4422 |
| 15 | 1646 |
| 31 | 183 |
| 63 | 2 |
| 127 | 3 |

The position counts sum to `12874`, and the exact number of explicitly tested
values is

\[
1(1820)+3(4553)+7(4422)+15(1646)+31(183)+63(2)+127(3)
=77303.
\]

Every one of the other (65535) masks at a position is excluded by the
necessary containment (2), so `77303` is an exhaustive pruned census, not a
restricted search neighborhood.

## Comparison with the primary audit

The independent result agrees exactly with the primary report on:

* the one-hole family;
* the vulnerable-target count;
* minimum and maximum residual sizes;
* the full residual-size and submask-count histograms;
* the maximum state and join-base counts;
* `77303` tested necessary replacements; and
* zero passing candidates.

No mathematical or implementation error was found.  One inert schema caveat
is that the primary driver's `candidate_sha256`, if a candidate existed,
would hash the compact JSON integer list rather than the raw emitted word
bytes.  Since the exact candidate family is empty, this does not affect the
no-go or any retained artifact.

## Frozen artifacts

Primary driver:

```text
scratch/audit_ad_k16_12874_one_substitution_exact_20260730.py
SHA-256 1651c3552a44085e04281f9916c44cf6aa59c36f6390c127a516fa729f52e75e
```

Primary report:

```text
scratch/ad_k16_12874_one_substitution_exact_20260730.audit.json
file SHA-256    84ad2928982987351603975fbf1ea2f3d3fee83c6bc95bf541ce0ef83f76bf6d
payload SHA-256 1cbcd5e161999aa00f70952c0daabe88e8ec1bb3dec033981910eff2cb5081f7
```

Independent checker:

```text
scratch/audit_ad_k16_12874_one_substitution_independent_20260730.py
SHA-256 7ee896a045f26b8b5e64fb4347ee87205134ac373e4d77376691e21b1ac3eadc
```

Independent report:

```text
scratch/ad_k16_12874_one_substitution_independent_20260730.audit.json
file SHA-256    c2b73b316276ac58aa5e0bec2c99451b0c0054c9d3fea2aaf5c26826ee332141
payload SHA-256 b74ac89a3135fadc9453f200cc33d18778859df7e1f4a92fa4602781d0a3b8e5
```

The independent local-light replay completed in 0.37 seconds and used no SAT
solver or heavy search.
