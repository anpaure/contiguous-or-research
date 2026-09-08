# Self-audit: uniform forced-facet spread and optional-core elimination

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_UNIFORM_FORCED_FACET_SPREAD_ELIMINATES_OPTIONAL_CO_SMALL_CORES_20260804.md`

## Verdict

PASS.  The proof closes the optional co-small gate for the newly
co-selected reservoir.  It does not close the separate small-cut gate or
any chronology/compiler gate.

## 1. Random low-path probability

For an owner `U` with external trace `S`, `|S|=e`, deleting `a in S`
produces a lower facet with trace `S-a` of size `q=e-1` and a `K`-part of
size `m-e`.  A randomized low path of trace `q` has `q-1=e-2` distinct
immediate lower colours, each with a uniform rank-`m-e` `K`-part.  Hence

\[
 p_e={e-2\over {m-1\choose m-e}}
     ={e-2\over {m-1\choose e-1}}.
\]

Distinct deleted external coordinates give distinct trace paths, whose
orders are independent.  Thus the triple-union bound in (1.2) is valid.

The number of rank-`m` owners with external size `e` is

\[
 {m\choose e}{m-1\choose m-e}
 ={m\choose e}{m-1\choose e-1}.
\]

Using

\[
 {m\choose e}={m\over e}{m-1\choose e-1}
\]

gives exactly the sum in (1.4), with one binomial denominator remaining.

## 2. The `o(1)` estimate

For fixed `4<=e<=8`, the `e`-summand is
`O(m/binom(m-1,e-1))=O(m^{-(e-2)})`.

For `9<=e<=m/4`, the denominator is at least
`binom(m-1,8)=Theta(m^8)` and the numerator is `O(m^6)`, so the whole
range is `O(m^{-1})`.

For `m/4<e<=m-d`, binomial unimodality places the minimum denominator at
one of the endpoints.  The lower endpoint is exponential; the upper one
is `binom(m-1,d)`.  Since `d to infinity`,

\[
 {m-1\choose d}/m^8\longrightarrow\infty.
\]

The at most `m` terms, each with numerator `O(m^6)`, sum to `o(1)`.
This verifies the global union bound.

## 3. Deterministic pre-high accounting

There are three disjoint sources of protected facets below a fixed owner:

1. deleting a `K` coordinate keeps the exact external trace fixed; the
   same-trace adjacency theorem permits at most two such protected facets;
2. among external deletions, at most two traces become cyclic intervals in
   the ordinary range; there are at most three deletions when the external
   trace has size at most three, while at full external trace the resulting
   `(m-1)`-traces do not occur in the top lower palette;
3. randomized noninterval low traces contribute at most two by Lemma 1.1.

No high-tail path has yet been installed.  The resulting upper bound is
`2+3+2=7`.  The three categories do not omit a deterministic private
family: every low noninterval trace is randomized in the cited spread
construction, while cyclic and hinge traces belong to the deterministic
top bank.

## 4. High-tail preservation

Two lower colours of one monotone geodesic are facets of a common owner
only when their indices differ by one; hence one path adds at most two to
one owner load.

At any stage,

\[
 \sum_Uz_U=m|Z_P|,
\]

because each lower `(m-1)`-set has exactly `m` owner supersets.  With
`|Z_P|=O(m2^m)`, the number of load-at-least-eight owners is
`O(m^2 2^m)`.  Forbidding all their facets adds `O(m^3 2^m)` lower
resources.  After multiplying by the `O(m)` path positions, this remains
`2^{m+o(m)}` against denominator `2^{2m-o(m)}`.  It is therefore
compatible with all earlier high-tail forbidden banks.

Starting from load at most seven, a noncritical owner reaches at most
nine; a critical owner is untouched.  Induction proves the final cap
nine.

## 5. Optional-core contradiction

The cap gives `g_U>=m-9`.  In a positive optional owner,

\[
 b_U\ge g_U-c_U+1\ge m-10
\]

because `c_U<=2`.  Minimal-core strictness gives
`sum_U a_U>2|B^-|`; since `a_U<=2`, the positive-owner family has
`|Q|>|B^-|`.

The sharp partial-shadow theorem with `D_0=m-10` therefore gives

\[
 |B^-|\ge {2m-21\choose m-11}+1=2^{2m-o(m)}.
\]

The independently proved co-small localization gives
`|B^-|=O(m^2 2^m)=2^{m+o(m)}`.  These bounds are incompatible.

Finally, the optional-complement theorem identifies absence of a positive
maximizer with feasibility of every residual co-small Hall cut.  Thus the
claimed gate, and only that gate, is closed.
