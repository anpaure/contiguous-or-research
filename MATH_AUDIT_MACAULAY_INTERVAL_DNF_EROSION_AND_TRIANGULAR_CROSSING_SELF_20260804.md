# Self-audit: Macaulay interval erosion and triangular protected crossing

**Date:** 2026-08-04  
**Verdict:** **SELF-GO.**  The canonical decompositions, triangular shadow
law, occurrence-level gluing table, and head--tail erosion inequality have
been rederived below.  The result is an erosion theorem for initial colex
segments, not a classification of arbitrary shifted families.

No computation, search, or solver result is used.

## 1. Audited artifact

`MATH_THEOREM_MACAULAY_INTERVAL_DNF_EROSION_AND_TRIANGULAR_CROSSING_20260804.md`

SHA-256:
`c2b7156bb810306738086392238c5fb047b083b4885083a93827bb6ef16df23c`.

This is an author self-audit and is not an independent audit.

## 2. Canonical block census

The recursive colex construction fixes the pivots

\[
 Q_j=\{c_{j+1}+1,\ldots,c_m+1\}
\]

and then chooses `j` coordinates from `[c_j]`.  Strict decrease of the
`c_j` makes these sets disjoint, so the block has size `binom(c_j,j)`.
Complementation gives the exact interval between

\[
 C_j=[n]\setminus(Q_j\cup[c_j])
 \quad\hbox{and}\quad
 S_j=[n]\setminus Q_j.
\]

For `j<l`, direct comparison gives

\[
 C_l\subseteq C_j\cup\{p_l\}.
\]

Thus any member of the `C_j` star violating the `Q_j` cap enters a
higher-index star.  Iteration proves that the disjoint interval union and
the principal-star union agree.  The witnesses `p_l in C_l-C_j` and
`p_j in C_j-C_l` prove pairwise core incomparability.

The core size is

\[
 |C_j|=n-(m-j+c_j)=m-\rho_j,
 \qquad \rho_j=c_j-j+1.
\]

Hence the cited all-two-sided theorem applies exactly when `rho_j>=2`;
`rho_j=1` is the separately handled singleton endpoint.

## 3. Shadow intersections

A block facet is either

\[
 Q_j+\binom{[c_j]}{j-1}
\]

or is obtained by deleting one pivot `p_h` from `Q_j`.  An internal facet
contains `p_l=c_l+1` and therefore cannot lie in the support of `B_l`.
A boundary facet can lie there only if the deleted pivot is exactly
`p_l`.  The remaining `l-1` variable points then all lie in `[c_l]`, so
the facet is internal to `B_l` and has degree `rho_l`.  This proves (2.1)
and unique terminal internality.

Triple intersections are possible.  Accordingly the theorem uses

\[
 \sum_Dh_D\le\sum_{j<l}|\partial B_j\cap\partial B_l|,
\]

not equality.  The first draft's equality at this step was caught before
freezing and corrected; equality requires, in particular, absence of
triple intersections.

## 4. Protected local table

At a shared facet with terminal degree `rho_l>=2`, the separate shadow
mass exceeds the union shadow mass by `h`.  If protected degree is zero,
no loss term changes and the tax is `h`.  At protected degree one, a
protected boundary facet cancels one tax unit, giving `h-tau`.  At degree
two, the terminal block loss plus the singleton block losses differs from
the union loss by exactly `h`, cancelling the whole shadow tax.

When `rho_l=1`, all `h+1` pieces are singleton fibres.  The exact singleton
table gives

\[
 h-1,qquad h-t,qquad0
\]

at protected degrees zero, one, and two.  These are precisely the six rows
of (3.2).  Summation proves (3.3).

Every tax is at most `h`.  Counting all terminal--boundary pairs is bounded
by counting all block pairs.  Pair `(j,l)` has exactly `b_j` shared facets,
so

\[
 \sum_D\chi_P(D)
 \le\sum_{j=s}^{m-1}(m-j)b_j.
\]

The inequality direction correctly allows triple intersections.

## 5. Quantitative block-margin check

For one Macaulay block, the complement census has

\[
 \binom{c_j}{j-1}={j\over\rho_j}b_j
\]

internal facets of degree `rho_j` and `(m-j)b_j` boundary facets of degree
one.  Hence its exact capped slack is

\[
 \sigma(I_j)=
 \begin{cases}
  (m-2)b_j,&\rho_j=1,\\
  (m-j-2+2j/\rho_j)b_j,&\rho_j\ge2.
 \end{cases}
\]

The triangular pair bound charges at most `(m-j)b_j` to this block.  The
remaining scalar credit is therefore `(j-2)b_j` at `rho_j=1` and
`2(j/rho_j-1)b_j` at `rho_j>=2`.  Subtracting the literal interval losses
proves (3.6).  The only nonpositive credits are `rho_j>=j`, plus the
zero-credit exceptional pair `(j,rho_j)=(2,1)`.  The global incidence
bound and the frozen two-sided current bound justify both alternatives in
(3.7).

## 6. Erosion calculation

Partition the cut into one arbitrary head plus residual singleton blocks.
Adding one singleton to an existing owner fibre costs at most one unit of
margin.  This follows from the three protected degrees:

| old fibre size | maximum added gluing cost |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| at least 2 | 1 |

Thus `q` residual incidences cost at most `q`, and when the head fibre is
empty the first costs zero, leaving at most `q-1`.

There are `m|R|` residual incidences.  Every internal facet of a residual
block has empty head fibre because it cannot meet a higher-index block.
Internal facet sets of different blocks are disjoint by unique terminal
internality.  Hence one saves exactly one available charge at each of

\[
 \sum_{j=s}^r\binom{c_j}{j-1}
\]

owners, giving gluing loss at most

\[
 m|R|-\sum_{j=s}^r\binom{c_j}{j-1}.
\]

The constant-spread singleton margin contributes `(m-12)|R|`.  Since

\[
 {\binom{c_j}{j-1}\over\binom{c_j}j}
 ={j\over c_j-j+1}={j\over\rho_j},
\]

subtraction yields exactly

\[
 \mu_P(A)\ge\mu_P(A^{head})+
 \sum_{j=s}^r\left({j\over\rho_j}-12\right)b_j.
\]

No independence or generic Hall assumption enters this bound.

## 7. Two-level crossing check

For `F_(t,u)`, the only pivot is `z=t+1`.  Shared facets are exactly the
`H in binom([u],m-1)`.  The first block is terminal internal with degree
`t-m+1>=2`; the second contributes one boundary facet.  The local tax is
one at an unprotected owner, one at a degree-one owner unless that boundary
facet is protected, and zero at degree two.  This is exactly `Theta_P` in
(5.3).  For the empty bank every shared facet pays, giving the whole
second-block size.

Thus decomposition into safe interval pieces does not eliminate the
literal crossing current.  The theorem does not claim this family fails
protected Ore; bounded-DNF control can settle the union by another route.

## 8. Scope

The theorem proves an exact structural and quantitative result for initial
colex segments.  Compression only guarantees the existence of a shifted
minimizer, and shifted does not imply colex.  Long broad Macaulay runs with
`rho_j>j/12` can still make the erosion credit negative.  No claim about
those runs, arbitrary shifted families, factor topology, or the common cap
is made.

**SELF-GO** at theorem SHA
`c2b7156bb810306738086392238c5fb047b083b4885083a93827bb6ef16df23c`.
