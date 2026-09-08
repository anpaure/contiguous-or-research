# Self-audit: optional co-small charging LP exact factor equivalence

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_OPTIONAL_CO_SMALL_CHARGING_LP_EXACT_FACTOR_EQUIVALENCE_20260804.md`

No computation or finite search is used.  This audit checks the identities,
quantifiers, and possible circularity claim independently from the prose of
the theorem.

## 1. Total mass

For an incidence lift, every protected lower colour has degree two, so

\[
 |E(P)|=2|Z|.
\]

The two middle-level shores have equal size.  Therefore

\[
 \sum_U(2-d_P(U))
 =2|\mathcal U|-|E(P)|
 =2|\mathcal L|-2|Z|
 =2|X|.
\]

This is the exact equality used to force every charging inequality tight.
It would fail for a general protected graph having lower degree one, so
the theorem correctly states the incidence-lift hypothesis.

## 2. Ownerwise overflow

Let `s_U=g_U-c_U`.  Directly:

* `c=0`: `(b-g)_+=0` for `0<=b<=g`;
* `c=1`: `(b-g+1)_+` is one only at `b=g`;
* `c=2`: `(b-g+2)_+` is one at `b=g-1`, two at `b=g`.

Thus (1.1) agrees exactly with the frozen full/almost-full owner ledger,
including the base-unsafe cases `g=0,c>0` and `g=1,c=2`.

## 3. Complement identity

For `A=X setminus B`, the residual degree at owner `U` is `g_U-b_U`.
The lost capacity is

\[
 c_U-\min(c_U,g_U-b_U)=(b_U-g_U+c_U)_+.
\]

Hence

\[
 \begin{aligned}
 \kappa(A)-2|A|
 &=\sum_Uc_U-\Omega(B)-2|X|+2|B|\\
 &=2|B|-\Omega(B).
 \end{aligned}
\]

Vertices in `Z` have residual demand zero.  Deleting them from a lower
Hall shore leaves demand unchanged and can only lower its capped supply,
so a maximum deficiency shore can indeed be chosen inside `X`.  Therefore
the maximum over optional complements is the full residual deficiency,
not merely a lower bound on it.

## 4. Charging LP

Summing lower capacities gives total weight at most `2|X|`; summing owner
demands gives at least `sum c_U=2|X|`.  Therefore all column and row
inequalities are tight individually: if any one had slack, the summed
equality would fail.

On a row of total one, every nonnegative entry is at most one.  On a row
of total two, the near-full inequality excluding `y` is equivalent to
`w_{Uy}<=1`.  Thus the proposed LP has exactly:

* lower degree two;
* owner degree `c_U`;
* unit incidence capacities.

That is the fractional residual `b`-matching polytope.  Bipartite
incidence matrices are totally unimodular, so an integral point exists
whenever a fractional point does.  Adding that residual matching to `P`
gives degree two on both shores.  The equivalence and circularity claim
are therefore exact.

## 5. Extremal-bank derivatives

For `f_U(b)=(b-s_U)_+`,

\[
 f_U(b)-f_U(b-1)=1\iff b\ge s_U+1,
\]

and

\[
 f_U(b+1)-f_U(b)=1\iff b\ge s_U.
\]

Subtracting the modular cost `2|B|` gives (4.7)--(4.8).  Inclusion
minimality of `B^-` makes the first difference a strictly positive
integer, hence at least one and `q^- >=3`.  Inclusion maximality of `B^+`
makes the second strictly negative, hence `q^+ <=1`.

The block inequalities have the same signs and follow by comparing a
canonical extremizer with a proper deletion or addition.  No assertion is
made that these local conditions alone are sufficient for an extremizer.

## 6. Scope check

The theorem proves:

1. the generalized all-`B` charging LP is fully circular;
2. all optional-bank inequalities are exactly the residual factor Hall
   system;
3. a positive obstruction has canonical optional banks satisfying exact
   threshold closure rules.

It does **not** prove:

* that the present constant-spread reservoir extends to a two-factor;
* that every localized co-small bank is safe;
* that the canonical optional extremizer is shifted or colex;
* that no source-to-sink path exists in the shift-augmented DM quotient.

The remaining noncircular target is correctly restricted to localized
optional banks or to a direct factor construction.

**Self-audit verdict:** GO within the stated scope.
