# Independent audit: minimal common-core reservoir, singleton Ore, and residence split

**Date:** 2026-08-04  
**Verdict:** **FINAL GO after correction**, with the scope stated in
Section 9 below.  The audit is purely deductive: no search, solver, sampled
enumeration, or H100 computation was used.

## 1. Frozen inputs

| role | file | SHA-256 |
|---|---|---|
| audited theorem | `MATH_THEOREM_COMMON_CORE_MINIMAL_RESERVOIR_SINGLETON_ORE_AND_RESIDENCE_SPLIT_20260804.md` | `bfc9b6cc16c19e06ea8c455d688099e90fd8c80bd476b71fdbbbff1c1f91ae87` |
| common-core damage and top paths | `MATH_THEOREM_COMMON_CORE_UPPER_DAMAGE_AND_DISJOINT_WITNESS_RESERVOIR_20260804.md` | `3aaaf6388256954b2579581353f3c1e456198d6f7a4ebd0a9de951945695f983` |
| weighted protected Ore identity | `MATH_THEOREM_PROTECTED_ORE_WEIGHTED_BOUNDARY_AND_CUT_THINNESS_20260804.md` | `4bb0621bdac66579eefba12c8b270d6334c517468d7f0deba277943f0bfc8891` |
| near-shadow localization | `MATH_THEOREM_PROTECTED_ORE_NEAR_SHADOW_LOCALIZATION_20260804.md` | `c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0` |
| hybrid clipped-resident packing | `MATH_THEOREM_COMMON_CORE_HYBRID_CLIPPED_RESIDENT_WITNESS_RESERVOIR_20260804.md` | `f9cd82ff39c3fb6979bd2c70e92223af6f7bb171d4ede422a023b7d2c6809314` |

The theorem was reread after all corrections and its dependency hashes
were checked byte for byte.

## 2. Minimal private geodesics

Put `n=m-1` and `p=q-1`.  An owner

\[
 V_j=(K\setminus D_j)\cup T
\]

has rank

\[
 n-p+q=(m-1)-(q-1)+q=m.
\]

Consecutive deletion windows differ by one leaving and one entering
coordinate, so consecutive owners differ by one deletion and one
insertion.  Their immediate colours are

\[
 V_j\cap V_{j+1}
  =(K\setminus(D_j\cup D_{j+1}))\cup T
\]

and

\[
 V_j\cup V_{j+1}
  =(K\setminus(D_j\cap D_{j+1}))\cup T.
\]

The two omitted sets are cyclic windows of lengths `p+1` and `p-1`,
respectively.  Since `p<=n-2`, the displayed sequence uses distinct
windows in both ranks.  Thus the owners, lower colours, and upper colours
are simple.

The complements of the `p+1` consecutive `p`-windows are `p+1`
consecutive windows of length `n-p`.  Their union covers the cycle because

\[
 (n-p)+p=n.
\]

Equivalently, the deletion windows have empty total intersection.  Hence
the owner union is exactly `K union T`.  It takes at least `q-1` Johnson
edges to grow a rank-`m` cumulative union to rank `m+q-1`; the construction
uses exactly that many.  The claimed geodesic minimality is exact.

For `q=2`, the two displayed owners are adjacent, their union is
`K union T`, and they use one lower and one upper colour.  Exact external
trace `T` separates every resource rank between distinct private paths and
from the cyclic-interval top bank.

## 3. Correction to the cyclic deletion lemma

The original unqualified deletion lemma was false when `D` is the whole
ambient cycle: every deletion then leaves a cyclic co-singleton.  This was
a real statement-level error, although it did not destroy the singleton
theorem.

The frozen version now assumes

\[
 2\le |D|\le n-1.
\]

Its proof is exact.  If `D` has at least three cyclic components, one
deletion cannot leave one component.  If it has two components, the
deleted point must be an entire singleton component, giving at most two
choices.  If it has one component, only an endpoint may be deleted,
again giving at most two.  The addition assertion follows by taking
complements.  The full-cycle case is handled separately in the singleton
proof.

## 4. Singleton Ore audit

For a lower vertex `x`, write

\[
 R=x\cap E,\qquad D=K\setminus x,\qquad |R|=|D|=s.
\]

An owner over `x` contributes to `lambda_P({x})` only if it is an internal
protected owner and neither incident protected lower colour equals `x`.
Counting all internal protected neighbours is therefore a valid
overcount.  The cases are:

| `s` | external additions | `K`-additions | total bound |
|---:|---:|---:|---:|
| `0` | first top endpoints only | none | `0` |
| `1` | at most two cyclic-pair top interiors | private pairs have no interior | `2` |
| `2`, `D=F_2` | at most two top interiors | at most one | `3<=m-2` for `m>=5` |
| `2`, `D=G_2` | at most `m-2` private-triple interiors | none because `b notin G_2` | `m-2` |
| `2`, other `D` | none | at most one | `1` |
| `3` | at most `m-3` | at most one | `m-2` |
| `4<=s<=m-2` | at most `m-s` | at most two by the corrected lemma | `m-s+2<=m-2` |
| `m-1` | full external trace is absent | the co-singleton top owner is an endpoint | `0` |

At `m=4`, the apparently dangerous length-three top owner is itself an
endpoint, so the direct bound is at most two.  The common choice of the
internal deletion window `G_2`, disjoint from `b` and different from
`F_2`, is precisely what prevents the `s=2` top and private debts from
adding.  Hence

\[
 \lambda_P(\{x\})\le m-2=\sigma(\{x\})
\]

for every lower vertex.

## 5. Co-small cuts and the exact residual Hall system

If `A=mathcal L setminus X` and `|X|<=m-2`, every upper owner has at least
two facets in `A`.  Therefore

\[
 \sigma(A)=2W-2|A|=2|X|.
\]

At such an owner the protected loss is exactly the number of protected
incidences into `X`, so

\[
 \lambda_P(A)=e_P(\mathcal U,X)
 \le D_P(X)\le2|X|.
\]

The co-small theorem is exact for every maximum-degree-two bank.

For the path bank, every selected lower colour and every internal owner is
already saturated.  Removing these vertices leaves demand two on every
remaining lower vertex, capacity two on every unused owner, and capacity
one on every endpoint owner.  Capacitated bipartite Hall gives exactly the
displayed residual inequality in Theorem 3.2.  If `J` is the number of
protected Johnson edges, then

\[
 2|U_2|+|U_1|=2J=2|L_2|,
\]

so total residual upper capacity and lower demand both equal `2W-2J`.
Thus saturation of all lower demands also saturates the upper shore; no
extra balance condition is missing.

## 6. Singleton-slack identity

At an owner of protected degree two, with `a` selected facets and `t`
protected incidences into them, the sum of its singleton losses is
`a-t`.  Its direct cut loss agrees for `a<=1` and equals `2-t` for
`a>=2`; the difference is `(a-2)_+`.

An owner of protected degree zero contributes neither loss.  An endpoint
owner contributes direct loss exactly when `a>=2` and `t=0`, and
contributes no singleton loss.  Hence

\[
 \lambda_P(A)=\sum_{x\in A}\ell_P(x)
 -\sum_{U:d_P(U)=2}(a_U-2)_++E_1(A).
\]

Regularity gives

\[
 \sigma(A)=(m-2)|A|-\sum_U(a_U-2)_+.
\]

Subtracting yields Theorem 3.3 exactly.  Therefore the remaining
multi-vertex obstruction is precisely the unsaturated-clique overlap debt,
not an omitted scalar term.

## 7. Frozen near-shadow localization

The dependency with SHA
`c96700cbaa6b540428bc97cbaab16c546423162c600df7859d22bc27068553c0`
proves

\[
 (m-1)\sigma(A)=(m-2)(|N(A)|-|A|)
 +\sum_{U:2\le a_U\le m-1}(m-a_U).
\]

Combining its strict integer failure inequality with the singleton and
co-small closure gives exactly Corollary 3.4.  Every remaining failed cut
must be multi-vertex, have complement at least `m-1`, have shadow surplus
and loss at least `m-1`, satisfy the displayed clique-defect inequality,
and lie in the spectral/Kruskal--Katona small-or-co-small cardinality
region.  The theorem correctly presents these as necessary conditions,
not as a proof that all such cuts pass.

## 8. Residence split and adaptive high-tail packing

On a minimal fixed-trace path, complements of the deletion windows are
cyclic windows of length

\[
 h=m-q.
\]

Any internal positive run of a `K` coordinate has length `h`; the common
external trace meets both endpoints.  Thus the low range
`q<=m-d-1` has no internal positive run shorter than `d+1`.  Endpoint runs
remain exported.

For a high target with `q=m-h`, `1<=h<=d`, the monotone geodesic has a
common core of size `h+1`, an outgoing set and incoming set of size `q-1`,
and `q` owners.  Outgoing coordinates have prefix runs, incoming
coordinates suffix runs, and core coordinates occur throughout.  It is
therefore clipped resident, but this does not itself construct compatible
ambient collars.

For one monotone geodesic, a fixed rank-`m-1` lower vertex can lie below at
most two consecutive owners: otherwise two owners containing it would be
at Johnson distance at least two.  If it lies below two consecutive
owners, their shared incidence is exactly that lower vertex, so neither
owner contributes singleton loss.  Consequently one new path increases
any singleton loss by at most one.

If `N_int` is the number of current internal protected owners, every one
contributes exactly one unit to each of its `m-2` non-path facets.  Hence

\[
 \sum_x\lambda_P(\{x\})=(m-2)N_{\rm int},
 \qquad |X_{\rm crit}|\le N_{\rm int}.
\]

Avoiding every owner over a critical lower vertex adds at most
`m N_int=O(m^2(2^m+H_d))` forbidden owner resources.  The exact symmetric
hitting probabilities from the frozen hybrid theorem multiply this by at
most another factor `m`, whereas the uniform owner/lower/upper supply is
`2^{2m-o(m)}`.  The resulting union bound is

\[
 {O(m^3(2^m+H_d))\over2^{2m-o(m)}}=2^{-m+o(m)}<1.
\]

Thus one can avoid every current critical star while retaining all prior
resource-disjointness.  Critical losses stay fixed; each noncritical loss
is at most `m-3` and rises by at most one.  Induction proves singleton
safety for the entire high tail.  For fixed `C`, this argument is uniform
for `d<=C sqrt(m)` and sufficiently large `m`.

## 9. Corrections and fail-closed scope

The following corrections were required before the verdict.

1. The cyclic deletion lemma now excludes the full ambient cycle and the
   singleton proof treats `s=m-1` separately.
2. The residence section now claims only clipped internal residence.
   Compatible endpoint collars remain open.
3. The residual Hall proof now records equality of total residual demand
   and capacity.
4. `W`, `H_d`, the asymptotic quantifier, and the exact frozen
   near-shadow restrictions are stated explicitly.

The audited theorem proves:

- geodesic-minimal private witnesses with simple owner/lower/upper
  resources;
- every singleton protected Ore cut;
- every cut with complementary lower shore at most `m-2`;
- the exact residual capacitated Hall formulation and singleton-slack
  identity;
- an adaptive high-tail packing preserving singleton safety and clipped
  internal residence.

It does **not** prove the remaining multi-vertex protected Ore cuts,
compatible endpoint collars, a spanning two-factor, component placement,
global cyclic residence, or the common cap.  Subject to this exact scope,
the corrected theorem is **FINAL GO**.
