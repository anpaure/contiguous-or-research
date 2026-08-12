# Independent audit: all-low rolling-collar bank `q1` factor extension

**Date:** 2026-08-06  
**Audited theorem:**
`MATH_THEOREM_ALL_LOW_ROLLING_COLLAR_BANK_Q1_FACTOR_EXTENSION_20260806.md`  
**Audited theorem SHA-256:**
`9f77950a39b9f03c3eb588d1a9ded10c13675e03ec58440df5d06c65250e7bd8`  
**Verdict:** **GO / proof-safe as stated.**  No correction to the theorem is
required.  This audit is mathematical and used no computation or search.

## 1. Halo-orbit check

For a target `S`, every role in the full factor halo has rank `m-1`, `m`,
or `m+1`, and its intersection with the pointwise-fixed target has size at
most `|S|<=d`.  After that intersection pattern is fixed, the complement
part has size `m+O(d)` inside a ground set of size `2m-O(d)`.  Hence every
role orbit under `Sym([2m-1]-S)` has size

\[
 \binom{2m-O(d)}{m+O(d)}=2^{2m-o(m)}.
\]

One collar has `O(md)` full-neighbourhood roles, and the number of targets
is `L_d=2^{o(m)}`.  Thus the total union-bound budget is
`O(m^2d^2L_d^2)=2^{o(m)}`, against collision probability
`2^{-2m+o(m)}` for each ordered role pair.  The halo-disjoint selection is
valid.  Including full one-neighbourhoods is exactly what prevents an
ambient lower vertex or owner from accumulating exposure from two
different collars.

## 2. Exposure check

For one collar, if `i<j`, then

\[
 |T_i\cap T_j|\le m-(j-i).
\]

A rank-`m-1` lower vertex can lie below both only for `j-i<=1`, so it lies
below at most two protected owners.  Similarly

\[
 |I_i\cup I_j|\ge m-1+(j-i),
\]

and a rank-`m` owner contains at most two protected lower colours.  Full
halo disjointness prevents cross-collar addition.  Therefore

\[
 \ell_P(x)\le2,\qquad e_P^{\rm priv}(x)\le2,
 \qquad z_U\le2
\]

uniformly over the entire subexponential bank.  The overlap and separated
window cases both have the required inequality; no wraparound is used.

## 3. Small-shore loss check

The exact path-forest identity gives

\[
 \lambda_P(A)
 \le\sum_{x\in A}\ell_P(x)+E_1(A).
\]

Every endpoint owner counted by `E_1(A)` contains at least two selected
facets.  Each such incidence is counted by `e_P^{priv}`, so

\[
 2E_1(A)
 \le\sum_{x\in A}e_P^{\rm priv}(x)
 \le2|A|.
\]

Consequently `E_1(A)<=|A|` and

\[
 \lambda_P(A)\le3|A|.
\]

Near-shadow localization and `|E(P)|=2^{o(m)}` reduce the small side to
`a=|A|=2^{o(m)}`.  Writing `a=binom(m+t,m)`, this forces `t=o(m)`.
Lovasz--Kruskal--Katona then gives

\[
 {\sigma(A)\over a}
 \ge {m-2\over m-1}
 \left({m\over t+1}-1\right)\longrightarrow\infty,
\]

uniformly on the localized range.  It eventually dominates the constant
three.  The small-side closure is sound.

## 4. Co-small threshold check

The exact optional gap is

\[
 g_U=m-z_U\ge m-2.
\]

For a positive optional owner, residual capacity `c_U<=2` gives the forced
facet count

\[
 b_U(B^-)
 \ge g_U-c_U+1
 \ge(m-2)-2+1=m-3.
\]

Thus the theorem's threshold `D=m-3` is exact.  Together with
`|Q|>|B^-|`, the sharp one-sided partial-shadow theorem yields

\[
 |B^-|\ge\binom{2m-7}{m-4}+1=2^{2m-o(m)},
\]

whereas near-shadow localization makes the entire co-small complement
`2^{o(m)}`.  This contradiction is valid.

## 5. Scope

The theorem unconditionally closes the simultaneous protected
owner/lower-`q1` factor-extension gate for all low rolling collars, for all
sufficiently large parameters satisfying `4d+4<=m`.

It does not:

1. improve the finite `k=17` interval (the size hypothesis fails there);
2. connect the residual two-factor;
3. prove global positive/zero-gap residence;
4. prove the complete upper deck; or
5. close the terminal common cap.

Accordingly it is a genuine all-bank gate closure, but not yet a proof of
`nu(k)<=B(k)+O(1)`.

