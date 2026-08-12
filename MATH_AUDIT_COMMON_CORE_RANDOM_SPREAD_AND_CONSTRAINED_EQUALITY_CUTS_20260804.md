# Independent audit: random spread and constrained equality-cut closure

**Date:** 2026-08-04  
**Verdict:** the original random-spread draft was **NOT GO** because it
counted the deterministic top endpoints as a bounded per-star exposure and
silently conflicted with the common-`G_2` three-trace orientation.  The
revised alternative-random theorem is **GO through Sections 1--6**.  The
separate constrained-spread theorem, which retains common `G_2`, is also
**GO**.  Neither result closes positive-defect cuts in general.

No computation, finite search, or solver output is used in this audit.

## 1. Audited artifacts

| role | file | SHA-256 at audit |
|---|---|---|
| revised alternative-random theorem (Sections 1--6) | `MATH_THEOREM_COMMON_CORE_RANDOM_TRACE_SPREAD_AND_LOW_EXPANSION_ORE_LOCALIZATION_20260804.md` | `d6875ab5e876aa3f1805ec387065be2b2bd1e07b5e3b27dbc120dff3e027eb65` |
| constrained common-`G_2` theorem | `MATH_THEOREM_COMMON_CORE_EQUALITY_CUTS_CONSTRAINED_SPREAD_COMPLETE_20260804.md` | `b07682e2aee1b5d3017e96fc1483b17a91be8d249673a2c4b49433610867eb5e` |
| exact singleton/common-`G_2` input | `MATH_THEOREM_COMMON_CORE_MINIMAL_RESERVOIR_SINGLETON_ORE_AND_RESIDENCE_SPLIT_20260804.md` | `bfc9b6cc16c19e06ea8c455d688099e90fd8c80bd476b71fdbbbff1c1f91ae87` |
| hybrid resident reservoir | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |
| equality classification | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |

## 2. Fail-closed findings on the original draft

### 2.1 The endpoint-exposure assertion was false

Let `x=K`.  Every first top-path owner is `K\cup\{a_i\}`.  It is an
endpoint and its unique protected lower neighbour is `B\cup\{a_i\}`, not
`K`.  Therefore

\[
                         e_P(K)=m.
\]

This contradicts the original asserted bound `e_P(K)<=6m/log m` for all
sufficiently large `m`.  The revised theorem correctly defines
`e_P^priv`, excludes the top endpoints from it, and adds their entire
`2m` contribution in the general cut estimate.

### 2.2 Uniform triples and common `G_2` are different constructions

If every noninterval triple uses the same internal deletion window `G_2`,
then every vertex

\[
 x=(K\setminus G_2)\cup R,
 \qquad R\in{E\choose2},
\]

can receive up to `m-2` triple-path singleton losses.  Thus the uniform
constant-star proof cannot be claimed simultaneously with common `G_2`.
The revised random theorem explicitly abandons `G_2`; its constant bound
then proves singleton safety independently.  The constrained theorem
instead retains `G_2` and prices this exceptional family exactly.

These are scope corrections, not counterexamples to either corrected
construction.

## 3. Audit of the revised alternative-random theorem, Sections 1--5

### 3.1 Random-window marginals

For a trace of size `q`, put `n=m-1` and `h=m-q`.  A uniformly ordered and
cut copy of `K` is `Sym(K)`-invariant.  Each of the `q` owner windows is
therefore uniform in `binom(K,h)`.  The windows are distinct, so a fixed
owner is used with probability

\[
                         {q\over{n\choose h}}.
\]

The same argument restricted to the two endpoints gives
`2/binom(n,h)`.  Nonconsecutive windows differ by at least two exchanges,
because both `h` and the complementary deletion width are at least two in
the private low range.  Thus one path contributes at most one singleton
loss and one private-endpoint exposure to any fixed lower vertex.  Section
1 is GO.

### 3.2 Star means and the constant union bound

For a lower vertex with external size `s`, a foreign trace must be
`S\cup\{z\}`.  Its unique required `K`-part gives the means

\[
 (m-s){s+1\over{m-1\choose s}},
 \qquad
 (m-s){2\over{m-1\choose s}}.
\]

On `2<=s<=m-3`, the first expression has endpoint maximum
`6/(m-1)`, and the second is smaller.  Multiplying the sixth-moment tail by

\[
 {m\choose s}{m-1\choose s}
 ={m\over m-s}{m-1\choose s}^2
\]

gives exactly the summand displayed in the revised proof.  The endpoint
terms tend to zero and the central terms are smaller by polynomial powers.
Adding the fixed top and own-trace constants yields `R_0=10`.  Section 2
is GO.

### 3.3 Adaptive high-tail packing

A monotone geodesic raises either fixed-star load by at most one.  The sum
of singleton loads equals `(m-2)` times the number of protected internal
owners; the endpoint sum has the same required polynomial bound.  Hence
the critical-star forbidden owner bank has size `2^{m+o(m)}`, while every
high target has resource denominators `2^{2m-o(m)}` and there are only
`2^{o(m)}` high targets.  The strengthened greedy union bound remains
strict.  Section 3 is GO.

### 3.4 Exact path-forest identity and endpoints

At a protected degree-two owner with `a` selected facets and `t` protected
facets in the cut, the summed singleton loss is `a-t`.  Its direct cut
loss is the same for `a<=1` and is `2-t` for `a>=2`; the difference is
`(a-2)_+`.  A protected endpoint contributes only when `a>=2` and its
protected facet is outside.  This proves the exact identity in Section 4.

Every private endpoint counted there is exposed at each of at least two
selected facets, giving the factor `1/2`.  The deterministic top bank has
exactly `2m` endpoints and is priced globally.  Therefore

\[
                         \lambda_P(A)\le15|A|+2m
\]

is valid.  Section 4 is GO after the top-bank separation.

### 3.5 One-support formula and additivity

For `A_S=binom(S,m-1)`, with `t=|S|` and `u=2m-1-t`, the only mixed
owners have exactly one selected facet.  Thus the cut loss is exactly the
number `theta_P(S)` of saturated boundary owners missing that facet, and

\[
\begin{aligned}
 \sigma(A_S)
 &=2{t\choose m}+u{t\choose m-1}-2{t\choose m-1}\\
 &={u(m-2)\over m}{t\choose m-1}.
\end{aligned}
\]

The constant star bound closes `u(m-2)/m>=10`.  The remaining
`1<=u=O(1)` range has binomial slack `2^{2m-o(m)}`, while the whole
reservoir has only `2^{m+o(m)}` internal owners.  Distinct equality
supports have disjoint upper shadows, so both sides add.  Section 5 is GO
for the explicitly stated alternative-random reservoir.

### 3.6 Principal up-stars

For `A_C=\{x:C\subseteq x\}` and `r=m-|C|\ge2`, an owner has either zero or
exactly `r` selected facets.  Its protected loss is therefore exactly the
number of protected Johnson-path edges crossing the owner up-star.  Every
coordinate has an interval of occurrences along each of the three path
types, so each path crosses at most twice.  A low path can meet the star
only when its trace contains `C\cap E` and its size is at most
`m-|C\cap K|`, giving the stated `H_r(m)` path count.

Direct counting yields

\[
 |A_C|={m+r-1\choose r-1},\qquad
 \sigma(A_C)={2(m-r)\over r}|A_C|.
\]

For `r<=m/10`, the constant-load estimate applies.  For
`m/10<=r<=m/2`, the ratio to `binom(m,r)` is exponentially large; for
`m/2<=r<=m-1`, its entropy exponent is
`(3/2)H_2(1/3)>1`, beating the entire `2^m` low bank even after the
`2/m` coefficient.  Section 6 is GO.

## 4. Audit of the constrained common-`G_2` theorem

### 4.1 Random part

Randomizing only traces `q>=4` leaves `s>=3`.  One foreign path has the
same uniform marginal as above, total mean at most two, and contributes at
most one.  The `6m/log m` threshold beats the fewer-than-`4^m` star events.
The high-tail greedy choice can avoid both random-critical stars and the
total-critical stars of the frozen singleton theorem.  Both forbidden
banks remain `2^{m+o(m)}`.  Thus the common-`G_2` singleton invariant and
the random-load invariant coexist.

### 4.2 Exact concentration face

The sole internal owner of a three-trace path is

\[
                         (K\setminus G_2)\cup T.
\]

Outside the family

\[
 \mathcal B=\{(K\setminus G_2)\cup R:R\in{E\choose2}\},
\]

at most the own trace contributes to a singleton; on `mathcal B` there
are at most `m-2` external completions.  This proves the envelope in the
constrained theorem.

If `|S|=m-1+c` with `c\ge1`, then either
`A_S\cap\mathcal B` is empty or

\[
 {|A_S\cap\mathcal B|\over|A_S|}
 \le{{c+2\choose2}\over{m-1+c\choose c}}
 \le {3\over m}.
\]

The last ratio is exact at `c=1` and decreases, since its consecutive
ratio is `(c+3)/(m+c)<=1`.  Hence the fixed concentration costs fewer
than three units per selected facet on every nonsingleton support clique.

### 4.3 Two-range closure

The exact support formula then gives

\[
 \theta_P(S)\le(R_m+7){t\choose m-1}.
\]

This closes complements of size
`u>=m(R_m+7)/(m-2)`.  For the remaining `u=o(m)`, the central binomial
slack is `2^{2m-o(m)}` and dominates the complete `2^{m+O(log m)}`
protected bank.  The singleton support itself is the already frozen
common-`G_2` theorem.  Additivity over separated supports is exact.
Therefore every `b(A)=0` cut passes in the constrained construction.

### 4.4 Stability corollary

Toggling one lower vertex changes the protected local loss by at most one
at each of its `m` owner-neighbours, and changes `sigma` by at most `m+2`.
Thus `sigma-lambda` is `(2m+2)`-Lipschitz in lower-vertex Hamming distance.
The positive-margin equality cuts therefore have the explicit
positive-defect neighbourhood stated in the theorem.  This conclusion is
GO but does not close all `b>0` families.

## 5. Final scope

The following statements are now proof-safe:

1. the alternative fully spread reservoir closes all singleton cuts,
   all moderately expanding cuts, and all `b=0` cuts;
2. the constrained reservoir retains common `G_2` and still closes every
   `b=0` cut;
3. a quantitative Hamming neighbourhood of every positive-margin equality
   cut is also safe.

The following are **not** proved:

1. every positive-defect near-shadow cut is safe;
2. the protected factor has the required component distribution;
3. endpoint collars coexist in the ambient chronology; or
4. the common-cap/compiler gate.
