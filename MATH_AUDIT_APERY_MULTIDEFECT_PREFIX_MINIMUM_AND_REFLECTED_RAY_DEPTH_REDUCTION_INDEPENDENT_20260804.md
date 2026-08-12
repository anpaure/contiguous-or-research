# Independent audit: multidefect prefix minima and reflected-ray depth

**Date:** 2026-08-04  
**Verdict:** **GO as a pure-mathematical reduction after one scope-only
patch.**  The cyclic block-minimum theorem, deficit gauge, exact-first-carry
comparison, reflected-ray identity and ordering, overlap-depth loss bound,
theta quadrature, scalar margin, and all integer consequences replay
exactly.  The source does not prove that every multidefect clock has small
overlap depth or terminal ray coverage, and it makes no all-grid or OR-word
claim.

## 1. Exact source binding and patch

Audited source:

`MATH_THEOREM_APERY_MULTIDEFECT_PREFIX_MINIMUM_AND_REFLECTED_RAY_DEPTH_REDUCTION_20260804.md`

Current SHA-256:

`28c714f8eae3ae56c22a1c7c643f583e73b891e1abf2f66e4e866d831b7eb21e`

The supplied lineage SHA was

`843497f6d0a7a409165f20b0dbfab513e3b5a63d9e73a708c5f947665192945f`.

The only patch was in Theorem 1.1's proof.  The honest Apéry inequalities
are indexed by residues below `h`, so they directly prove the block bound
only for `1<=t<h`.  The endpoint `t=h` is instead the literal identity

\[
                         B_{r,h}=P=s_h.
\]

The theorem statement was already correct; the patch makes its proof's
index scope exact.  No formula, bound, or downstream conclusion changed.

## 2. Cyclic block minima and the deficit gauge

For `t<h`, the two cases of the block sum are

\[
 B_{r,t}=s_{r+t}-s_r
 \quad(r+t<h),
\]

and

\[
 B_{r,t}=P+s_{r+t-h}-s_r
 \quad(r+t\ge h).
\]

The two honest Apéry inequalities give `B_(r,t)>=s_t` in precisely these
two cases.  For `t=h`, Section 1 above supplies equality.  Summing over all
`r` counts each cyclic gap exactly `t` times, so

\[
                         hs_t\le tP,
\]

and hence `s_t<=tP/h`.  At `t=1`, each one-gap block is at least
`s_1=gamma_1`, proving every `gamma_j>=gamma_1`.

Put `p=P/h` and `d_t=tp-s_t`.  For `r+t<h`,

\[
 d_{r+t}\le d_r+d_t
 \iff s_{r+t}\ge s_r+s_t.
\]

For `r+t>=h`, using `hp=P`,

\[
 d_{r+t-h}\le d_r+d_t
 \iff P+s_{r+t-h}\ge s_r+s_t.
\]

Thus cyclic subadditivity is exactly equivalent to the honest Apéry rows.
Finally,

\[
 p-(d_j-d_{j-1})=s_j-s_{j-1}
\]

for `j<h`, while at `j=h`, with `d_h=d_0=0`, the same expression is

\[
 p+d_{h-1}=P-s_{h-1}=\gamma_h.
\]

The gauge and gap formulas are therefore exact in every cyclic position.

## 3. Exact-first-carry comparison

The prefix-average inequality at `t=1` gives `a=s_1<=P/h`.  Together
with `P+a=A`, this is equivalent to

\[
                         0<\alpha={a\over A}\le{1\over h+1}.
\]

At capacity `(h+1)q+r`, with `0<=r<=h`, the construction consisting of
`q` size-`h+1` carries of value `A` and the displayed size-`r` generator
has value `qA+s_r`, where `s_h=P`.  It is exact at `q=0`; for `q>=1`,
both this value and the true Bellman value are at least `A`.  Since `K` is
increasing on that tail,

\[
 K(W_{(h+1)q+r})\ge K(qA+s_r).
\]

Summing the `h+1` residue classes gives exactly

\[
 E(s)=C+\sum_{r=1}^{h-1}F(s_r)+F(P).
\]

No finite availability term is deleted: the endpoint residue `r=h` is
the explicit `F(P)` term.

## 4. Reflected-ray indexing and ordering

For upper-ray index `i`, the carry row with residues `i+1` and `h-i`
has sum `h+1`, hence

\[
 s_{i+1}+s_{h-i}\le P+s_1=A.
\]

Therefore

\[
 X_i={s_{i+1}\over A}le {A-s_{h-i}\over A}=Y_i.
\]

The late residue `s_(h-i)>A/2` gives `Y_i<1/2`, and strict positivity of
`s_(i+1)` gives `X_i>0`.  In particular `X_u<1/2<s_(h-u)/A`; strict
increase of the residues forces

\[
                         u+1<h-u,
\]

so the early indices `2,...,u+1` and late indices `h-u,...,h-1` are
disjoint.

The first reflected point obeys

\[
 A-s_{h-1}=a+\gamma_h\ge2a.
\]

Successive reflected points differ by

\[
 (A-s_{h-i-1})-(A-s_{h-i})=\gamma_{h-i}\ge a.
\]

Induction gives the exact minorant `Y_i>=(i+1)alpha`.

The reflection identity pairs `F(a)+F(P)=g(alpha)`, and for each
`1<=i<=u` pairs

\[
 F(s_{i+1})+F(s_{h-i})
 =f(X_i)-f(Y_i)+g(Y_i).
\]

The unused indices are exactly `u+2,...,h-u-1`.  This reproduces (3.6)
with no missing or duplicated train term.

If `u=0`, the same first pair gives

\[
 E(s)=C+g(\alpha)+\sum_{r=2}^{h-1}f(s_r/A)>43/1000-1/20000>0,
\]

so the separate `u=0` closure is also valid.

## 5. Overlap-depth loss

For one interval,

\[
 f(X_i)-f(Y_i)=-\int_{X_i}^{Y_i}f'(t)\,dt.
\]

Summing and using the half-open overlap count gives exactly

\[
 T=-\int_0^{1/2}f'(t)D(t)\,dt.
\]

Where `f'<=0`, the integrand is nonnegative.  On the increasing portion,
`D<=H`, so the total loss is at most `H` times the total positive
variation of `f`.  The one-mode theorem permits only monotone behaviour or
one rise followed by one fall; hence that positive variation is at most

\[
                         \sup f-f(0)=\sup f-C.
\]

Using `sup f<61/1000` gives

\[
 T\ge-H(\sup f-C)>-H(61/1000-C)
\]

when `H>0`, with the weak form literal at `H=0`.  This verifies both the
sign and the multiplicity in (4.3): the loss depends on maximum overlap
depth, not the number of intervals.

## 6. Theta count and quadrature

There are exactly `u+1` theta terms:

\[
                         g(\alpha),g(Y_1),\ldots,g(Y_u).
\]

Thus the uniform absolute bound gives `Theta>-(u+1)/20000`.

For the stronger chamber, monotonicity of `g` and
`Y_i>=(i+1)alpha` give

\[
 \Theta\ge\sum_{j=1}^{u+1}g(j\alpha).
\]

Since `(u+1)alpha<=Y_u<1/2`, right-endpoint quadrature gives

\[
 \alpha\sum_{j=1}^{u+1}g(j\alpha)
 \ge\int_0^{(u+1)\alpha}g(t)\,dt.
\]

The zero half-interval mean rewrites the last integral as minus the
terminal integral.  Because `g` is increasing,

\[
 \int_0^{(u+1)\alpha}g
 \ge-\{1/2-(u+1)\alpha\}g(1/2).
\]

Under `(u+2)alpha>=1/2`, the coefficient is at most `alpha`; division
gives `Theta>=-g(1/2)>-1/20000`.  Every inequality remains valid when
some `X_i=Y_i`.

## 7. Scalar margin and integer implications

The middle train terms are nonnegative.  Combining their omission with
the compact and theta bounds gives

\[
\begin{aligned}
 E(s)
 &>C-H(61/1000-C)-{\tau\over20000}\\
 &=(H+1)C-{61H\over1000}-{\tau\over20000}\\
 &>{43(H+1)-61H\over1000}-{\tau\over20000}\\
 &={860-360H-\tau\over20000}.
\end{aligned}
\]

Thus `360H+tau<=860` implies strict positivity even at equality.

For `H<=2` and terminal coverage, `tau=1`, so the numerator is at least

\[
                         860-720-1=139.
\]

Without terminal coverage, `tau=u+1`.  A nonpositive depth-two clock
requires

\[
 720+u+1>860\iff u\ge140,
\]

while a depth-one clock requires

\[
 360+u+1>860\iff u\ge500.
\]

Finally `u+1<h-u` is equivalent to `h>2u+1`; integrality gives
`h>=2u+2`.  Hence the two cases force respectively

\[
                         h\ge282,\qquad h\ge1002.
\]

With terminal coverage, `tau=1`, and nonpositivity forces `H>=3`.
Every numerical and integer implication in Sections 5--6 is therefore
correct.

## 8. Dependency binding and exact scope

The source's dependency hashes match the current workspace:

| role | SHA-256 |
|---|---|
| honest cyclic Apéry theorem | `324f040f5604767fc867c78806c8a7ab7524d6ed82cabe77bc3e2e0ea36121ba` |
| one-defect classification | `9b7b3f459d979205d111fe0be1f2e21ba3ce783056b16fd021716e841f67622e` |
| Euclidean compact-train theorem | `7540343eab8e110d950c7e19a6dea33aefc2e17a89f7c90b93966a4ed653b738` |
| all-period long-wrap theorem | `24f440d2b516618f7798b5f4e053de0f5b3253ad1825e7685e2494bddacf8ecd` |
| independent long-wrap audit | `ab249d01d769f42e9ca26cf17d4170397b021fe5d0714e3e20127d57a614a85b` |

The theorem applies only to the pure periodic formal clock at exact first
carry.  It does not cover threshold overshoot, a later first crossing, the
finite shoulder from a physical clock to its formal Apéry clock, or the
endpoint-critical branch.  It supplies a sufficient small-depth/terminal-
coverage closure and necessary residual inequalities; it does not prove
that the residual high-depth geometries exist or do not exist.

