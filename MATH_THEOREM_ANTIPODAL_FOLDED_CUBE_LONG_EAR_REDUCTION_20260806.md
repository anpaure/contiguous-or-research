# Antipodal folded-cube ordering and the long-ear reduction

**Date:** 2026-08-06  
**Method:** an explicit Hamilton cycle in the antipodal quotient of the
cube; no computation or search  
**Status:** unconditional trace-order theorem.  It replaces every local
Gray seam in the common-core reservoir by an almost-antipodal seam.  It
does not yet pack the corresponding physical Johnson ears or prove their
palette and residence constraints.

## 1. The antipodal quotient has an elementary Hamilton cycle

Let `m>=3`, let `E={1,...,m}`, and identify subsets of `E` with vectors in
`F_2^m`.  Write `bar T=E-T`.  The antipodal quotient has one vertex
`[T]={T,bar T}` for every complementary pair.

Choose in each pair the unique representative not containing coordinate
`m`.  These representatives form the ordinary `(m-1)`-cube on
`E-{m}`.  Let

\[
 R_0,R_1,\ldots,R_{2^{m-1}-1}
 \tag{1.1}
\]

be any cyclic binary reflected Gray ordering of that cube, with
`R_0=emptyset`.  Thus

\[
                         |R_i\mathbin\triangle R_{i+1}|=1
 \tag{1.2}
\]

cyclically.

### Theorem 1.1 (antipodal long-seam ordering)

The cyclic word

\[
 R_0,\bar R_0,R_1,\bar R_1,\ldots,
 R_{2^{m-1}-1},\bar R_{2^{m-1}-1}
 \tag{1.3}
\]

contains every subset of `E` exactly once.  Consecutive traces in (1.3)
have Hamming distance alternately `m` and `m-1`.

After deleting `emptyset` and `E`, the remaining nonempty proper traces
still have a cyclic ordering in which every consecutive Hamming distance
is at least `m-2`.

#### Proof

Every complementary pair has exactly one representative avoiding `m`, so
(1.3) is a permutation of `2^E`.  The seam `R_i,bar R_i` has distance
`m`.  By (1.2), `R_(i+1)=R_i triangle {e}` for one coordinate `e`; hence
`bar R_i` agrees with `R_(i+1)` only at `e` and their distance is `m-1`.

The two deleted traces occur consecutively as `R_0=emptyset,bar R_0=E`.
Their two exterior neighbours are `bar R_(2^(m-1)-1)` and `R_1`.
Both `R_(2^(m-1)-1)` and `R_1` are distinct cube neighbours of `R_0`, so
they differ in two coordinates.  Taking the complement of the first shows

\[
 |\bar R_{2^{m-1}-1}\mathbin\triangle R_1|=m-2.
\]

Every other seam retains distance `m` or `m-1`.  \(\square\)

This proof also gives a Hamilton cycle of the folded cube: the quotient
vertices are simply the Gray cycle (1.1).  No external Hamiltonicity
theorem is needed.

## 2. Almost-disjoint physical endpoint pairs

Retain the common-core split

\[
 K\mathbin{\dot\cup}E=[2m-1],\qquad |K|=m-1.
 \tag{2.1}
\]

For a trace `T`, a rank-`m` owner with exact external trace `T` has the
form

\[
                         O(T,W)=T\cup W,
 \qquad W\in {K\choose m-|T|}.                       \tag{2.2}
\]

### Lemma 2.1 (minimum-intersection endpoints)

Let `T,T'` be two consecutive traces in the ordering of Theorem 1.1.
There are `K`-sets `W,W'` of the sizes prescribed in (2.2) such that

\[
 |O(T,W)\cap O(T',W')|\le2.                          \tag{2.3}
\]

Consequently the two owners have Johnson distance at least `m-2`.

#### Proof

For subsets of an `(m-1)`-set having sizes `u,v`, the minimum possible
intersection is

\[
                         \max(0,u+v-(m-1)).           \tag{2.4}
\]

If `T'=bar T`, put `q=|T|`.  The two `K` sizes are `m-q` and `q`, whose
sum is `m`; choose their intersection to have size one.  The external
intersection is empty, so (2.3) holds with equality one.

For the other ordinary seam, write `S=R_i` and
`R_(i+1)=S triangle {e}`.  The pair is `bar S,R_(i+1)`.  If `e notin S`,
their external intersection is `{e}` and the two `K` sizes sum to `m-1`,
so they may be disjoint.  If `e in S`, their external intersection is
empty and the two `K` sizes sum to `m+1`, so (2.4) gives a `K` intersection
of size two.  The exceptional seam created by deleting `emptyset,E` has
external Hamming distance `m-2`; the same calculation gives total
intersection at most two.  \(\square\)

## 3. Exact random-geodesic aperture

Let `A,B` be rank-`m` owners with `|A cap B|=t<=2`, and put

\[
                         q=m-t.
 \tag{3.1}
\]

A uniformly random monotone Johnson geodesic from `A` to `B` is obtained
by independently ordering `A-B` and `B-A` and swapping the two ordered
lists coordinatewise.

### Lemma 3.1 (one-resource hitting probability)

At distance `s` from `A`, every compatible rank-`m` owner occurs with
probability

\[
                         {1\over {q\choose s}^2}.     \tag{3.2}
\]

Every compatible immediate lower or upper colour at the transition from
level `s` to level `s+1` occurs with the exact probability

\[
                  {1\over {q\choose s}{q\choose s+1}}.\tag{3.3}
\]

up to the harmless choice of whether `s` is indexed before or after the
swap.

#### Proof

An owner at level `s` specifies exactly the `s` deleted coordinates and
the `s` inserted coordinates.  Each is a uniform `s`-subset of a
`q`-set, independently, proving (3.2).  A lower transition colour specifies
the first `s+1` deleted coordinates as an unordered set and the first `s`
inserted coordinates as an unordered set.  These two prefix sets are
independent and uniform, giving (3.3).  The upper colour reverses the two
prefix sizes and has the same probability.  \(square\)

The point of (3.2) is that the middle of every required ear has
`2^{2m-o(m)}` effective choices: here `q>=m-2`.  The former direct
Gray seam had only a bounded local fibre and was forced into the
bottom-layer diagonal obstruction.

## 4. The remaining packing statement

Theorem 1.1 and Lemma 2.1 reduce the central common-core chronology to the
following assertion.

> **Antipodal long-ear packing lemma.**  Choose the two physical ports of
> every clipped-resident common-core witness and a monotone geodesic for
> every consecutive antipodal seam so that:
>
> 1. all ear owners and both immediate palettes are globally distinct and
>    avoid the protected witness bank;
> 2. each witness endpoint halo is private;
> 3. the ordered swaps extend every positive and zero residence flag for
>    at least `d+1` positions; and
> 4. the resulting chronology has one component.

The total number of required ear roles is only

\[
                         O(m2^m),                    \tag{4.1}
\]

whereas the ambient owner and palette layers have size
`2^{2m-o(m)}`.  Lemma 3.1 supplies the exact middle-layer hitting
probabilities.  What is not yet proved is the endpoint-halo packing: the
probabilities in (3.2) are only polynomially small near an endpoint, so a
proof must first reserve private prefixes and suffixes (or construct them
deterministically) before applying the symmetric middle-geodesic estimate.

## 5. Scope

Proved here:

1. an explicit antipodal cyclic ordering of all traces;
2. deletion of the two forbidden traces without creating a short seam;
3. physical endpoint pairs at Johnson distance at least `m-2`; and
4. the exact random monotone-geodesic resource aperture.

Not proved here:

1. pairwise private endpoint halos;
2. simultaneous owner/lower/upper palette avoidance for all ears;
3. residence continuation along the chosen ears;
4. compatibility with the PBBS whole-fan bank or terminal cap; or
5. `nu(k)<=B(k)+O(1)`.

The gain is that the forced noncyclic ears now live in a maximum-distance
regime with exponential internal choice.  The remaining obstruction is an
endpoint-reservoir theorem, not the bottom-layer zero-spare factor.
