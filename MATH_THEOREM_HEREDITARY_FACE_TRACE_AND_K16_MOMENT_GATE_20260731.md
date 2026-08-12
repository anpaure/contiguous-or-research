# Hereditary face traces and the K16 moment gate

Date: 2026-07-31  
Status: **general theorem and exact rank-only audit; no K16 verdict**

## 1. Hereditary face-trace theorem

Let `A=(A_0,...,A_(L-1))` be a universal contiguous-OR word on a ground
set `V`.  For `S subseteq V`, form `A|S` by deleting every letter which is
not itself a subset of `S`, while retaining the order of all remaining
letters.

> **Theorem.** `A|S` is a universal contiguous-OR word on `S`.

**Proof.**  Fix a nonempty `T subseteq S` and choose an interval of `A`
whose OR is `T`.  Every letter in that interval is a subset of `T`, hence a
subset of `S`.  Therefore the interval lies wholly in one maximal block of
letters retained by `A|S`; it remains a contiguous interval after the other
blocks are concatenated.  Its OR is still `T`.  This holds for every
nonempty `T subseteq S`.  QED.

Consequently, with

```text
n_A(S) = number of positions i with A_i subseteq S,
```

one has the architecture-free inequalities

```text
n_A(S) >= nu(|S|)                                      (1.1)
```

for every `S subseteq V`.  Equality in (1.1) is stronger than a count: the
induced trace is an optimal word on `S`.

Equivalently, for a coordinate set `B`, the concatenation of all letters
disjoint from `B` is universal on `V minus B`.  This is the universal-word
version of the survivor-facet lemma; it requires no proposed edit or parent.

## 2. Moment hierarchy

Put `k=|V|`, and let `n_s` count letters of rank `s`.  Sum (1.1) over every
`j`-element face `S`.  A rank-`s` letter lies in exactly
`C(k-s,j-s)` such faces, giving

```text
sum_s C(k-s,j-s) n_s >= C(k,j) nu(j).                 (2.1)
```

Equivalently, summing over excluded coordinate sets of size `a=k-j`,

```text
sum_s C(k-s,a) n_s >= C(k,a) nu(k-a).                 (2.2)
```

The inequalities hold simultaneously for every `a=1,...,k-1`.

For a hypothetical optimal K16 word, `L=12873` and the ghost theorem gives
`S+J+F=3`.  Every letter of rank above eight is a jump at its own left
endpoint, so

```text
sum_(s>=9) n_s <= 3.                                  (2.3)
```

Also `n_1>=16`, since each singleton target requires an actual singleton
letter.

## 3. What the rank-only relaxation proves—and does not prove

The reproducible audit

```text
scratch/audit_k16_rank_moment_polytope_20260731.py
```

uses the proved values `nu(j)=B(j)` for `j<=15`, imposes (2.2), (2.3),
`sum n_s=12873`, and integrality.  The resulting sixteen-variable polytope
is feasible.  In particular, the hereditary inequalities do not by
themselves prove `nu(16)>=12874`.

Some exact extremal values of this relaxation are

```text
16 <= n_1 <= 12873,
22 <= n_1+n_2+n_3 <= 12873,
671 <= n_1+...+n_7 <= 12873,
0 <= n_9+...+n_16 <= 3,
12873 <= sum_s s*n_s <= 98305.
```

These broad ranges show that summing the face inequalities loses most of
their content.  The useful object is the *individual ordered trace* `A|S`,
not its rank moment.

## 4. Exact K16 calibration

For the verified length-12874 word, and for its canonical length-12873
one-hole deletion, a subset-zeta audit gives the smallest count margins

```text
min_(|S|=j) [n_A(S)-B(j)]

j:                 1  2  3  4  5  6  7  8   9   10   11   12   13   14   15
12874 word:         0  1  3  8 19 42 88 163 300 486  764 1035 1294 1065   62
12873 one-hole:     0  1  3  8 19 42 88 163 299 485  763 1034 1293 1064   61
```

The unique tightest fifteen-face of the one-hole word is `S=0x7fff`: it
contains 6499 letters, only 61 above `nu(15)=6438`.  This rigorously explains
why the top-bit phase is the narrow recursive interface, while smaller faces
have much more count room.

## 5. Constructive consequence

If a length-12873 K16 word has a coordinate `b` occurring in exactly 6435
letters, its `b`-free trace has exactly 6438 letters and is therefore an
optimal K15 word.  Such a candidate is an interleaving of

```text
an optimal K15 trace of length 6438
and 6435 b-marked letters.
```

This is an exact route into the bilayer construction.  It is not forced:
all sixteen `b`-free traces may have length at least 6439.  A general proof
must therefore either force equality for some face or construct/control the
non-tight interleaved case.

The theorem is useful as an exact search cut and as a recursive normal form,
but it leaves the authoritative bracket unchanged:

```text
12873 <= nu(16) <= 12874.
```
