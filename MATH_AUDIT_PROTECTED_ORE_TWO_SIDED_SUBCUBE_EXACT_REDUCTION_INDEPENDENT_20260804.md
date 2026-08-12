# Independent audit: exact protected Ore ledger for two-sided subcubes

**Date:** 2026-08-04  
**Verdict:** **GO after two corrections.**  The exact owner-fibre, slack,
clique-defect, and protected-loss identities are correct.  The original
path paragraph incorrectly suggested that the support restriction could
increase the core-exit current, and the original endpoint paragraph cited
two incompatible reservoir choices as though they were one bank.  The
corrected theorem fixes both points and proves a new quantitative
two-boundary safe region for one constant-spread reservoir.

This audit is independent of the author's self-audit.  No computation,
search, or solver result is used.

## 1. Audited artifacts

| role | file | SHA-256 |
|---|---|---|
| corrected theorem | `MATH_THEOREM_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_20260804.md` | `6499abf7abf9536bdfcf421206ad1e56d3b3f9d2ce05258b92cb8873ddb26dd7` |
| superseded self-audit with correction notice | `MATH_AUDIT_PROTECTED_ORE_TWO_SIDED_SUBCUBE_EXACT_REDUCTION_SELF_20260804.md` | `b151aa0181265b176bf28d392325add7b85a8dbeae897a532e1f10e44489d967` |
| one-bank constant-spread input | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |

The theorem's pre-correction SHA was
`1b3f25ca9f2e2546859f0461a2e45ee39b55dbd76a08b57c828a4c8794f12e20`.
It must not be cited for Section 4 or for a simultaneous endpoint claim.

## 2. Owner fibres and scalar identities

Put `r=m-1-c`, `v=s-c`, and `u=2m-1-s`.  A selected lower vertex is `C`
plus an `r`-subset of `S minus C`, so its number is

\[
 a={v\choose r}.
\]

An owner wholly in `S` is `C` plus an `(r+1)`-subset and has exactly
`r+1=m-c` selected facets.  An owner with one point outside `S` has exactly
one selected facet.  This independently gives

\[
 |N(A)|={v\choose r+1}+u{v\choose r}
\]

and

\[
 \sigma(A)=2{v\choose r+1}+(u-2){v\choose r}.
\]

Since

\[
 { {v\choose r+1}\over {v\choose r}}
 ={v-r\over r+1}={m-u\over m-c},
\]

the normalized formula is exact.  Only the internal fibres can have size
between two and `m-1`; each has deficit `c`.  Therefore

\[
 b(A)=c{v\choose r+1}.
\]

At `c=0` this reduces to `u(m-2)/m`; at `u=0` it reduces to
`2c/(m-c)`.  All formulas, including the zero binomial boundary cases,
are GO.

## 3. Protected-loss identity

At an internal owner `U`, every facet stays in `S`, and a facet `U-z`
fails the core condition exactly when `z in C`.  Since the owner has at
least two selected facets, its protected loss is exactly the number of
protected core-deleting incidences.  This is `xi_P(C,S)`.

At an outside owner `U=F+z`, `F` is the unique selected facet.  The local
loss is one exactly when the owner has protected degree two and `UF` is
not protected.  This is `theta_P(C,S)`.  The two owner classes are disjoint
and exhaustive, proving

\[
 \lambda_P(A)=\xi_P(C,S)+\theta_P(C,S).
\]

The original self-audit was correct through this identity.

## 4. First correction: the core current never splits

On one protected path, the positions whose owners contain every coordinate
of `C` form an interval `I`, because they are an intersection of coordinate
occurrence intervals.  An incidence counted by `xi` deletes a coordinate
of `C`; the adjacent owner is therefore outside `I`.  It is one of the at
most two boundary edges of `I`.

The extra requirement that the inside owner lie in `S` can suppress one of
these incidences.  It cannot turn an interior edge of `I` into a
core-deleting edge.  Hence

\[
 \xi_P(C,S)\le2|\mathscr P(C)|.
\]

The old suggestion that intersecting with the support condition could
split the core current was false.  It confused components of
`I intersect {U:U subseteq S}` with boundary edges of the unsplit
core-star interval `I`.

The frozen principal-star trace count applies unchanged: if
`rho=m-c`, the low paths meeting the core star are at most
`H_rho(m)=sum_(j<=rho) binom(m,j)`, with `m` top paths and at most `H_d`
high paths.  This validates (4.1)--(4.3).

## 5. Boundary-current truncation

Every outside owner counted by `theta` supplies one distinct singleton
loss occurrence at its unique selected facet `F`.  For a fixed `F` there
are only `u` outside extensions.  Therefore the sharp directly available
bound is

\[
 \theta_P(C,S)
 \le\sum_{F\in A}\min\{\ell_P(F),u\}.
\]

For the alternative-random bank, the frozen simultaneous cap is
`ell_P(F)<=R_0=10`.  Combining this with the core-current bound gives

\[
 \lambda_P(A)
 \le \min\{10,u\}{v\choose r}
 +2\bigl(H_{m-c}(m)+m+H_d\bigr),
\]

which is exactly (4.6).  Dividing by `a=binom(v,r)` and using the exact
normalized slack proves (4.7).

If `u>=13` and `a>=2N`, where

\[
 N=H_{m-c}(m)+m+H_d,
\]

then the left side of (4.7) is at least eleven and the right side at most
eleven.  If `u<=10`, subtracting `u` gives

\[
 {2(c-u)\over m-c}\ge {2N\over a},
\]

equivalent to (4.9).  Thus all three displayed sufficient regions are GO.

## 6. Second correction: endpoint quantifiers

The constrained common-`G_2` bank and the alternative-random constant-
spread bank are different physical reservoirs.  The original theorem
cited complete-support closure from the former and principal-star closure
from the latter, which did not prove simultaneous endpoint closure for one
bank.

The corrected theorem consistently chooses the alternative-random bank.
Its own Section 5 proves every zero-defect complete-support cut, and its
Section 6 proves every principal up-star.  Both endpoints and the new
interior estimate therefore refer to the same protected bank.  The
corrected quantifier is GO.

## 7. Sharpest tractable next inequality

The strongest current two-boundary target is not a new scalar estimate;
the scalar is already exact.  It is the pathwise boundary-current bound

\[
 \boxed{
 \theta_P(C,S)
 \le \sum_{F\in\mathcal A(C,S)}
       \min\{\ell_P(F),u\},
 \qquad
 \xi_P(C,S)\le2|\mathscr P(C)|.}
\]

For the present bank this yields the exact sufficient inequality (4.7).
Any further improvement must exploit correlation between the two terms:
a path which spends one of its two core exits near the support boundary
should have fewer saturated outside misses on the same two-sided subcube.
A sharp next lemma would be

\[
 \boxed{
 \xi_P(C,S)+\theta_P(C,S)
 \le \min\{10,u\}|A|+2|\mathscr P(C)|-\eta_P(C,S),}
\]

where `eta_P(C,S)` is an explicitly counted overlap credit for boundary
owners whose protected incidence already realizes a core exit.  Such a
credit is not proved here; without a literal joint path analysis it must
not be assumed.

## 8. Scope

The corrected theorem proves exact identities for every two-sided subcube
and a sufficient safe region for one constant-spread reservoir.  It does
not prove:

1. safety of every two-sided subcube;
2. reduction of every positive-defect family to a two-sided subcube;
3. factor component placement;
4. residence-collar gluing; or
5. common-cap compatibility.

