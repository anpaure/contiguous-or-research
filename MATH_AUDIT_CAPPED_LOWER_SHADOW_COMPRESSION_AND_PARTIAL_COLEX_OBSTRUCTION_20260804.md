# Self-audit: capped lower shadows and the partial-colex obstruction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_CAPPED_LOWER_SHADOW_COMPRESSION_AND_PARTIAL_COLEX_OBSTRUCTION_20260804.md`  
**Method:** independent symbolic derivation inside this note.  No search,
solver, or sampled computation is used.  
**Verdict:** author self-audit **GO**, pending independent review.

## 1. Complement and capped-shadow identity

For `X` of rank `m-1` and `U` of rank `m` on `2m-1` points,

\[
 X\subset U\iff\bar X\supset\bar U.
\]

Thus the owner multiplicity `a_U` is exactly the lower-facet degree of
`bar U` in the complement `m`-family.  If `S` is the ordinary lower-shadow
size and `q_1` is the number of degree-one facets, the capacity-two mass is

\[
                         q_1+2(S-q_1)=2S-q_1.
\]

This verifies Theorem 1.1.

## 2. Incidence and Kruskal--Katona bounds

The exact incidence count is `mf=sum_D d(D)`.  Subject only to `S` and
`q_1`, its maximum is

\[
                         q_1+m(S-q_1),
\]

so `q_1<=m(S-f)/(m-1)`.  Therefore

\[
 2S-q_1-2f\ge {m-2\over m-1}(S-f).
\]

Equality requires all nonunique degrees to equal `m`.  Substitution of
the exact KK shadow and the Lovasz shadow is directionally correct.  On
the face `q_1=0`, the identity is exactly `2(S-f)`, so an initial colex
segment that is two-covered attains the conditional bound.

## 3. Shift audit

For a paired facet `C+i,C+j`, let the outside extension sets before a
shift be `R_i,R_j`.  After shifting they are `R_i union R_j` and
`R_i intersection R_j`; the possible common extension `C+i+j` is present
on both sides and is unchanged.  Hence the new degree pair majorizes the
old pair with the same sum.  Since `min(2,t)` is concave, the pair's capped
mass cannot increase.  Facets using neither or both shift coordinates
retain their degrees.  This proves the shift theorem without assuming
colex extremality.

## 4. Two-level colex census

For

\[
 F_{t,u}={{[t]}\choose m}\cup
 \bigl(\{z\}+{{[u]}\choose {m-1}}\bigr),
\]

the three facet types and degrees are

\[
\begin{array}{c|c|c}
\text{facet}&\text{condition}&d\\ \hline
D\subset[t]&D\not\subset[u]&t-m+1\\
D\subset[u]&|D|=m-1&t-m+2\\
\{z\}\cup J&J\in{{[u]}\choose {m-2}}&u-m+2.
\end{array}
\]

All are at least two under the stated hypotheses.  The two displayed
shadow layers are disjoint, and there are no others.  This checks
(4.3)--(4.4).  Every second-block member is adjacent to a first-block
member by replacing `z`, proving connectedness.

For `m=4q,t=5q,u=5q-1`, put `f_0=binom(5q,4q)`.  The exact ratios are

\[
 f_1/f_0=4/5,
 \quad
 {\binom{5q}{4q-1}\over f_0}={4q\over q+1},
 \quad
 {\binom{5q-1}{4q-2}\over f_1}={4q-1\over q+1}.
\]

They give

\[
 {\sigma\over f}
 ={2(27q-13)\over9(q+1)}
 ={54m-104\over9m+36}
 =6-{320\over9m+36}.
\]

The size estimate uses
`binom(5q,q)<=(5e)^q<16^q`, so
`f=(9/5)f_0<2^(m+1)`.  The second block is exactly `4f/9`, verifying the
macroscopic-distance statement.  Since all positive degrees are `q+1`
or `q+2`, the family is positive-defect for sufficiently large `q`.

Writing
`C_0=[n]-[t]` and `C_1=[n]-([u] union {z})`, complementation gives the
union of the two principal stars on `C_0,C_1`.  The two cores exchange
`t` and `z`.  The part of the second star selecting `z` is already in the
first star, while the part omitting `z` is exactly the complement of the
second colex block.  This verifies the two-centre description and its
explicit scope warning.

For `t=alpha m+O(1),u=t-1`, both lower-shadow/member ratios tend to
`1/(alpha-1)`, so the slack ratio tends to
`2(2-alpha)/(alpha-1)`.  Solving it below 15 gives
`alpha>19/17`.  Standard binomial entropy gives exponent
`alpha H_2(1/alpha)`, verifying the localized range condition.

## 5. Heavy-facet reduction

If `f>=2m` and `sigma<15f+2m`, then

\[
                         \Psi_2=\sigma+2f<18f.
\]

With `L=ceil(m/72)`, every light facet has degree at most `L-1<m/72`.
There are at most `Psi_2` positive facets, so light raw incidence is less
than `mf/4`.  Heavy incidence is consequently greater than `3mf/4`.

If at most half the members had at least `m/2` heavy facets, the total
would be at most `3mf/4`; hence more than half do.  For one member, each
Johnson neighbour is indexed by its unique common facet, so its induced
degree is the sum of `d(D)-1`.  At `m>=144`,
`ceil(m/72)-1>=m/144`, giving `m^2/288`.  All constants and strict
inequalities are consistent.

## 6. Co-small tail

For `C=L-A`, complement it to the `m`-family `G`.  At a facet of degree
`d`, the baseline contribution is `2d/m`.  It agrees with the weighted
boundary for `d<=m-2`, exceeds it by one at `d=m-1`, and by two at `d=m`.
Summation gives

\[
 \sigma(L-C)=2|C|-n_{m-1}(G)-2n_m(G).
\]

Thus the same constant-15 lower bound is categorically unavailable on the
co-small side.

## 7. Scope verdict

The theorem supplies a sharp obstruction, not protected Ore extension.
It invalidates a sigma-only completion strategy and replaces it by a
precise structural target: protected crossings of shifted partial-colex
families with dense Johnson neighbourhoods.  No claim is made about the
protected bank's loss on that class.
