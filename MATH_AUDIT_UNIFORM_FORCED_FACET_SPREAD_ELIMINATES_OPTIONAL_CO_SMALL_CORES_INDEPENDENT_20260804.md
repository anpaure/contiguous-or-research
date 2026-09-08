# Independent audit: uniform forced-facet spread and optional co-small closure

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`  
**Audited SHA-256:**
`051c700a605f4820108846f9d5d2d220c01d00adcb0c4a7fec0dcbcfd8b9ffde`  
**Method:** pure mathematics; no finite search, solver, or remote
computation  
**Verdict:** **GO at the stated optional co-small scope.**

The new theorem really does close the optional co-small residual-factor
gate for the co-selected reservoir.  It does not close the separately
retained small-cut, chronology, global residence, upper-host, or compiler
gates.

## 1. Random cross-trace marginal

Fix a rank-(m) owner (U), put (S=U\cap E), and let (|S|=e).
Deleting (a\in S) gives a lower facet (L_a) with exact external trace

\[
 T_a=S\setminus\{a\},\qquad q=|T_a|=e-1.
\]

Whenever this is a randomized noninterval low trace, its path has
(q-1=e-2) distinct immediate lower colours.  Their (K)-parts have rank

\[
 m-e
\]

in the ((m-1))-set (K).  Symmetry of the random order and disjointness
of the path positions therefore give exactly

\[
 \Pr(L_a\in Z_P)
 =\frac{e-2}{\binom{m-1}{m-e}}
 =\frac{e-2}{\binom{m-1}{e-1}}.
\]

Different external deletions (a) give different traces (T_a), and the
construction chooses the orders of different low traces independently.
Events associated with cyclic traces are deterministic-top events and are
not included in (Y_U); treating all (e) coordinates in the triple
union bound merely overcounts.  The random contribution is possible only
for

\[
 3\le q\le m-d-1,
\]

equivalently (4\le e\le m-d).  Thus the probability estimate in (1.2)
has the right numerator, denominator, independence, and range.

## 2. Global owner union bound

The number of owners with (|U\cap E|=e) is

\[
 \binom me\binom{m-1}{m-e}
 =\binom me\binom{m-1}{e-1}.
\]

Writing (B_e=\binom{m-1}{e-1}) and using
(inom me=(m/e)B_e), the expected number of owners with at least three
random cross-trace hits is at most

\[
 \Sigma_m=
 \sum_{e=4}^{m-d}
 \frac me\,
 \frac{\binom e3(e-2)^3}{B_e},
\]

exactly as in the theorem.

The three asymptotic ranges are valid:

1. for fixed (4\le e\le8), the summand is
   (O(m^{-(e-2)}));
2. for (9\le e\le m/4), unimodality gives
   (B_e\ge\binom{m-1}{8}=\Theta(m^8)), while one numerator is
   (O(m^6)), so the whole range is (O(m^{-1}));
3. for (m/4<e\le m-d), the minimum denominator occurs at an endpoint
   and is at least
   
   \[
    \min\left\{
      \binom{m-1}{\lfloor m/4\rfloor-1},
      \binom{m-1}{d}
    \right\}.
   \]
   The first term is exponential.  Since (d\to\infty) and
   (d=O(\sqrt m)), the second is (omega(m^8)).  With at most (m)
   terms of numerator (O(m^6)), this range is (o(1)).

Hence (Sigma_m=o(1)).  The older lower-star and endpoint bad-event
families also have total probability (o(1)) on the same independent
low-trace probability space.  A union bound, not an independence claim
between those aggregate families, co-selects all properties.

## 3. Pre-high load seven

For a fixed owner, all facets obtained by deleting a (K)-coordinate have
the same external trace.

- If that trace is noninterval, the same-trace adjacency theorem bounds
  the relevant low path by two facets.
- If it is cyclic, the explicit top path has at most one lower colour of
  that exact trace, so the same displayed upper bound two remains valid.

Among external deletions, the cyclic one-point completion lemma allows at
most two deterministic top traces in the ordinary range.  Direct counting
gives at most three when (|S|\le3), and when (S=E) the resulting
co-singleton traces have size (m-1), while the top lower palette stops at
external size (m-2).  Thus the deterministic cross-trace contribution is
at most three.  The newly co-selected random low contribution is at most
two.  These are disjoint trace classes, so

\[
 z_U\le2+3+2=7
\]

before the high-tail paths.

## 4. One high geodesic adds at most two facets

The lower colours of one high monotone geodesic satisfy

\[
 |L_t\triangle L_s|=2|t-s|.
\]

Two distinct rank-((m-1)) facets of one rank-(m) owner differ by one
exchange, hence have symmetric difference two.  They can therefore occur
only at consecutive indices.  Three colours cannot all be pairwise
consecutive, so a geodesic contributes at most two facets below any one
owner.  This verifies the exact increment used by the induction.

## 5. Critical-owner forbidden-bank size

Every rank-((m-1)) protected lower colour has exactly (m) rank-(m)
owner supersets, giving

\[
 \sum_U z_U=m|Z_P|.
\]

Throughout the greedy construction, the total low palette has

\[
 |Z_P|=O(m2^m):
\]

there are at most (2^m) low traces, every path has (O(m)) edges, and
the top and subexponential high banks are smaller.  Hence the number of
owners with (z_U\ge8) is (O(m^2 2^m)).  Forbidding all (m) facets of
each adds at most

\[
 O(m^3 2^m)
\]

lower resources.

A fixed candidate high path has at most (m) lower-colour positions, and
the symmetric lower-resource denominator is (2^{2m-o(m)}).  The new
failure contribution is therefore

\[
 \frac{O(m^4 2^m)}{2^{2m-o(m)}}
 =2^{-m+o(m)}<1.
\]

It can be unioned with the previous owner/lower/upper collision and
lower-star critical banks at each deterministic greedy stage.  A critical
owner receives no new facet.  A noncritical owner begins the stage with
load at most seven and gains at most two, so the invariant (z_U\le9)
holds after every stage.

## 6. Chao--Yu contradiction

The cap gives

\[
 g_U=m-z_U\ge m-9.
\]

For the inclusion-minimal positive optional core (B^-), a positive owner
has capacity

\[
 a_U=(b_U-(g_U-c_U))_+\in\{1,2\}.
\]

The exact minimal-core ledger gives

\[
 \sum_Ua_U>2|B^-|.
\]

Since every positive (a_U\le2), the positive-owner family (Q) obeys

\[
 |Q|>|B^-|.
\]

Also (c_U\le2), so every (U\in Q) contains at least

\[
 b_U\ge g_U-c_U+1\ge m-10
\]

members of (B^-).  The audited Chao--Yu threshold-shadow corollary with
(D_0=m-10) now gives

\[
 |B^-|\ge\binom{2m-21}{m-11}+1
          =2^{2m-o(m)}.
\]

The independently proved co-small localization has

\[
 |B^-|=O(m^2 2^m)=2^{m+o(m)},
\]

a contradiction for all sufficiently large (m).  The exact
optional-complement/factor equivalence then closes every optional co-small
cut for this co-selected reservoir.

## 7. Scope

The proof is asymptotic and depends on (d\to\infty),
(d=O(\sqrt m)), as its reservoir construction already does.  It changes
the reservoir selection; it does not prove the same cap for an arbitrary
previously frozen reservoir.  It closes the optional part of the co-small
factor gate only.  In particular it does not establish:

- the separate small-cut completion;
- one connected globally resident carrier;
- arbitrary-width upper chronology in that carrier; or
- the terminal lower compiler.

Within that scope, the random union bound, deterministic load ledger,
high-tail greedy augmentation, and sharp-shadow contradiction all pass.
