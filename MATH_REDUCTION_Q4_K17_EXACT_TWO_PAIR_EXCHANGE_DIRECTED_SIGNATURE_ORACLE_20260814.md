# The q4 k17 owner descent has an exact two-pair exchange oracle on 1,431 outgoing-pair score faces

**Date:** 2026-08-14

**Status:** exact algebraic and algorithmic reduction.  It gives a complete
negative-two-exchange oracle for any finite candidate pool and an exact
thresholded interface for streamed target-row catalogues.  No search result
or owner cover is asserted.

## 0. Result

Let `ell` be the current load vector on the 680 nonfixed owner rows.  Let
`P,Q` be two distinct selected reflected-pair configurations and `N,M` two
distinct unselected configurations.  All are ten-row sets.  Define

```text
a(N) = sum_(x in N) [(ell_x+1-1)^2-(ell_x-1)^2]
     = sum_(x in N) (2 ell_x-1),

r(P) = sum_(x in P) [(ell_x-1-1)^2-(ell_x-1)^2]
     = sum_(x in P) (3-2 ell_x).                              (0.1)
```

For the unordered outgoing pair `R={P,Q}`, put

```text
c_R    = r(P)+r(Q)+2|P intersect Q|,
h_R(N) = a(N)-2|N intersect P|-2|N intersect Q|.              (0.2)
```

> **Theorem 0.1 (exact two-pair score).**  The simultaneous exchange
> `P,Q -> N,M` has energy change
>
> ```text
> Delta_2(R;N,M)
>   = c_R+h_R(N)+h_R(M)+2|N intersect M|.                     (0.3)
> ```

There are only `binom(54,2)=1,431` outgoing faces.  For one face let

```text
                         m_R=min_N h_R(N).                     (0.4)
```

Then:

1. if `c_R+2m_R>=0`, this face has no negative two-pair exchange;
2. otherwise a candidate can occur in a negative exchange only if

   ```text
                         h_R(N)<-c_R-m_R.                      (0.5)
   ```

Thus a complete stream may discard every candidate failing `(0.5)`.  This
is an exact threshold, unlike retaining an arbitrary top `K`.

## 1. Proof of the score identity

Write the signed change vector of the one-swap atom `P->N` as

```text
                              d_(P,N)=1_N-1_P.                  (1.1)
```

For any integer row-change vectors `d,e`, expansion of the square gives

```text
 Phi(ell+d+e)-Phi(ell)
 = [Phi(ell+d)-Phi(ell)] + [Phi(ell+e)-Phi(ell)]
   +2<d,e>.                                                   (1.2)
```

Consequently

```text
Delta_2
 =delta(P,N)+delta(Q,M)
  +2(|N intersect M|+|P intersect Q|
     -|N intersect Q|-|P intersect M|).                       (1.3)
```

The one-swap identity is

```text
delta(P,N)=r(P)+a(N)-2|P intersect N|.                         (1.4)
```

Substitution of `(1.4)` into `(1.3)` gives `(0.3)`.  This proof permits
overlap between `P,Q` and between `N,M` as row sets; only the configuration
indices themselves must be distinct.

Since the last term of `(0.3)` is nonnegative, `(0.4)` proves assertion 1.
If `N` belongs to a negative pair, replace `h_R(M)` by the lower bound
`m_R` and discard the nonnegative overlap term.  This gives the strict
necessary inequality `(0.5)`, proving assertion 2.

The equivalent directed-atom form is sometimes useful:

```text
g_(P,Q)(N)=delta(P,N)-2|N intersect Q|,

Delta_2=g_(P,Q)(N)+g_(Q,P)(M)
        +2|N intersect M|+2|P intersect Q|.                   (1.5)
```

Formula `(0.2)` is the symmetric compression
`g_(P,Q)(N)=r(P)+h_R(N)`.

## 2. Exact finite-pool algorithm

Represent every candidate by a 680-bit row mask.  Precompute for every
candidate `N`:

```text
a(N), and the 54-vector i_P(N)=|N intersect P|.                (2.1)
```

For every `P<Q`, compute `h_R(N)=a(N)-2i_P(N)-2i_Q(N)`, its minimum
`m_R`, and the constant `c_R`.  Apply `(0.4)` and `(0.5)`.  Only surviving
faces and candidates reach a pair test.  For them evaluate `(0.3)` by one
machine-mask intersection count.

This is already exact.  A bucket/bitset implementation avoids a large
surviving Cartesian product.  Bucket the retained candidates by integer
`h_R`.  For each row `x`, retain a bitset of bucket members containing
`x`.  Given a ten-row mask `N` and one score bucket `B`, the existence of a
candidate `M` with `|N intersect M|<=t` is tested by enumerating
`S subset N`, `|S|=t`, and checking

```text
             B minus union_(x in N-S) incidence(x)            (2.2)
```

after clearing `N` itself and all selected configurations.  Enumerate `S`
in increasing size.  The first nonempty test gives the exact minimum
intersection with that score bucket.  There are at most `2^10=1,024`
subset tests, and score buckets stop as soon as their zero-overlap lower
bound reaches the incumbent best value.

The two incoming configurations must be distinct and unselected.  Allowing
an outgoing configuration to be re-added only reproduces a zero- or
one-exchange state, so excluding all selected indices loses no genuinely
new two-exchange; at a certified one-exchange local optimum it cannot hide
a negative move.

## 3. Streamed target-row interface

For a complete target-row generator, an exact two-pass interface suffices.

1. First pass: compute `m_R` for every outgoing face under consideration.
2. Freeze the thresholds `(0.5)`.
3. Second pass: emit exactly the candidates passing at least one surviving
   face threshold, tagged by `(R,h_R)`.
4. Run the exact overlap test `(2.2)` on those finite banks.

No claim of completeness may be attached to a fixed top-5,000 or
top-100,000 bank for this purpose.  Completeness comes from the face minima
and strict threshold `(0.5)`.

At a one-exchange local optimum, every `delta(P,N)>=0`.  In the directed
form `(1.5)`, a negative two-exchange therefore requires the cross-blocker
gain

```text
 |N intersect Q|+|P intersect M|
 -|N intersect M|-|P intersect Q|                              (3.1)
```

to exceed half the two individual deltas.  This explains why the threshold
banks are naturally indexed by outgoing defect/blocker signatures rather
than only by the hole contained in an incoming mask.

## 4. Scope

The oracle is exact for two reflected-pair replacements with the 35 chosen
self lifts held fixed.  A two-self exchange or a mixed pair/self exchange
has the same quadratic identity but different group constraints and should
be catalogued separately.  The reduction does not assert that any negative
two-pair move exists, that target-row streams have already supplied the
face minima, or that descent reaches energy zero.

## 5. Independent H100 replay

The verifier exhausts all 80 scalar choices of one row load and four
membership bits, compares direct and formula energy on 12,915 synthetic
two-exchanges, checks every negative endpoint against the strict threshold,
replays 7,182 subset-bitset minimum-intersection queries against direct
minima, and supplies fifteen nonvacuous dead-face certificates from an
exact synthetic cover.  It does not inspect or search the q4 owner pool.

```text
scratch/verify_q4_k17_exact_two_pair_exchange_signature_oracle_20260814.py
sha256 6ec8dd1381ecf6f447c6df70b807b27cece5f1b9e7b615ffdd6bb9cefc32eb06

scratch/verify_q4_k17_exact_two_pair_exchange_signature_oracle_20260814.h100.out
sha256 7c6e8bcaa91653e34173d73de034b6ead8ad1ef9dee57111bda6fe6ee66f3360
status PASS
```
