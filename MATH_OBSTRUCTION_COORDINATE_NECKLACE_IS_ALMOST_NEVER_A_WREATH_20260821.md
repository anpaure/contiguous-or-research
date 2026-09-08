# Coordinate-translation necklaces are almost never cyclic-window wreaths

**Status (2026-08-21).**  The exact characterization below is proved.  It
applies to the coordinate-necklace diagonal `d`-factor supplied by the GK
orientation-biregularity theorem.  At every central rank, only an
exponentially small fraction of those necklaces can be decks of a cyclic
order.  Thus that explicit diagonal factor is not a physical wreath factor.

This does not rule out a different GK `d`-factor chosen simultaneously with
actual wreath decks, nor a different product-atom construction.  It is an
exact obstruction to reinterpreting the coordinate-translation
factorization itself as the missing physical lift.

## 1. Translation necklaces and tight adjacency

Let `b` be prime, identify the label set with `Z_b`, and let
`X subset Z_b` have size `r`, where

\[
                         2\le r\le b-2.                    \tag{1.1}
\]

Its coordinate-translation necklace is

\[
                    \mathcal N(X)=\{X+s:s\in\mathbb Z_b\}. \tag{1.2}
\]

The action is free, so this necklace has `b` distinct vertices.  A rank-`r`
cyclic-window deck consists of the `b` consecutive `r`-windows of one cyclic
order.  Consecutive vertices of such a deck have symmetric difference two.

### Lemma 1.1 (one tight translation forces an arithmetic interval)

For `d ne 0`,

\[
 |X\mathbin\triangle(X+d)|=2                              \tag{1.3}
\]

if and only if, for some `a`,

\[
            X=\{a,a+d,a+2d,\ldots,a+(r-1)d\}.              \tag{1.4}
\]

#### Proof

Because `b` is prime, addition by `d` is one cycle on `Z_b`.  Read the
indicator of `X` in the order
`a,a+d,...,a+(b-1)d`.  The quantity in (1.3) is exactly the number of
zero--one transitions in this cyclic binary word.  It equals two precisely
when the ones form one nonempty proper cyclic run, which is (1.4).
The converse is immediate.  \(\square\)

### Theorem 1.2 (exact wreath-compatible necklaces)

The necklace `N(X)` can be the rank-`r` window deck of a cyclic order if and
only if `X` is an arithmetic interval as in (1.4).

#### Proof

If `N(X)` is a cyclic-window deck, two consecutive windows are translations
`X+s` and `X+t` with symmetric difference two.  Translating back and using
Lemma 1.1 with `d=t-s` proves that `X` is an arithmetic interval.

Conversely, if (1.4) holds, order the labels cyclically with common
difference `d`.  Its rank-`r` windows are exactly the sets `X+jd`, and
`j -> jd` permutes `Z_b`; hence the deck is `N(X)`.  \(\square\)

## 2. Exact count and central consequence

For (1.1), every arithmetic-interval subset has exactly two oriented
descriptions: its two endpoints may be chosen as the start, with directions
`d` and `-d`.  Therefore there are

\[
                         {b(b-1)\over2}                     \tag{2.1}
\]

arithmetic-interval `r`-subsets and exactly

\[
                         \boxed{{b-1\over2}}                \tag{2.2}
\]

wreath-compatible coordinate necklaces.  On the other hand, all
`r`-subsets form

\[
                         {1\over b}{b\choose r}             \tag{2.3}
\]

coordinate necklaces.  Hence the compatible fraction is exactly

\[
             \boxed{{b(b-1)\over2{b\choose r}}}.            \tag{2.4}
\]

Uniformly on every central band `r=b/2+o(b)`, (2.4) is
`exp(-Theta(b))`.  Equivalently, only `b(b-1)/2` of the
`N_r=binom(b,r)` row vertices, and the same number of column vertices, lie
in a coordinate necklace which is itself a cyclic-window deck.

### Corollary 2.1 (the explicit necklace `d`-factor is nonphysical)

The coordinate-necklace diagonal factor from the GK orientation theorem
partitions every shore into the necklaces (1.2) and then uses diagonal
perfect matchings between necklace pairs.  At a central split, all but an
`exp(-Theta(b))` fraction of its necklace blocks have at least one shore
which is not any cyclic-order window deck.  Consequently this explicit
factor cannot be relabelled blockwise into physical two-wreath product atoms
on more than an exponentially small source fraction.

The conclusion concerns this coordinate-translation decomposition only.
An actual wreath factor partitions the same Boolean shore into different
`b`-vertex tight cycles, so Theorem 1.2 is not a nonexistence theorem for a
jointly chosen max-weight wreath-diagonal factor.

## 3. H100 audit

The checker
`scratch/audit_coordinate_necklace_wreath_compatibility_20260821.py`
enumerates all subsets at every prime `b<=13`, verifies Lemma 1.1 for every
nonzero translation, constructs the positive cyclic orders, and checks the
exact counts (2.1)--(2.4) at every rank in (1.1).  The asymptotic statement
uses the standard central binomial estimate; it is not a finite
extrapolation.
