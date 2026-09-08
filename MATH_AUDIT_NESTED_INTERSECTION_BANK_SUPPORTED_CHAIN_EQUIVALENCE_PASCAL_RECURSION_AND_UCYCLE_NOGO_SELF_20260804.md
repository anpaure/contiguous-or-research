# Self-audit: nested intersection banks, Pascal recursion, and the natural-Ucycle boundary

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_NESTED_INTERSECTION_BANK_SUPPORTED_CHAIN_EQUIVALENCE_PASCAL_RECURSION_AND_UCYCLE_NOGO_20260804.md`  
**Method:** independent line-by-line mathematical replay; no computation,
search, or solver  
**Verdict:** `SELF_GO`, subject to independent audit.

## 1. Rank and indexing audit

Residence gives

\[
 I_{i,j}=Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\},
 \qquad |I_{i,j}|=q-j
\]

for `0<=j<d`.  Hence every prefix column in the theorem has one member in
each of the distinct layers `q-1,...,q-h`.  The band starts at
`q-d+1`, as claimed.

The shift identity is used only for `1<=j<d-1`:

\[
 I_{i+1,j}=I_{i,j+1}+\beta_i.
\]

The derived two-parent-map identity needs `I_(i,j+2)` and is therefore
correctly restricted to `1<=j<d-2`.  No depth-three statement silently uses
a nonexistent third map.

## 2. Supported-chain equivalence audit

For a nested bank, the height

\[
 h(i)=\max\{j:i\in R_j\}
\]

has `R_j={i:h(i)>=j}`.  Thus the selected columns cover layer `j` exactly by
the values of `phi_j` on `R_j`; bijectivity is precisely exact coverage.

Conversely, a chain partition covers every rank-`q-1` top exactly once.  A
witnessing root for a chain ending at `S` lies in `phi_1^(-1)(S)`.  Fibres
for distinct `S` are disjoint, so independent local witness choices cannot
collide.  This validates Corollary 1.3 and the claim that there is no second
root-SDR after fixing the chain partition.

The exact-cover matrix does not need a root-capacity row: two nonempty
columns of the same root both contain the same top vertex and would violate
its equality row.

Imposing a root height cap merely deletes the overlong prefix columns.  A
fixed chain partition remains supportable exactly when its chain at each top
has one witnessing root inside that top's fibre and below the cap.  Since
different top fibres remain disjoint, triangular seam caps do not introduce
a cross-top Hall problem after the chain partition is fixed.

For the forced-fibre bound, if `u` top fibres are singleton, the remaining
`n_1-u` fibres contribute at least two roots, so `N>=2n_1-u`.  Every
singleton-fibre root is forced into `R_1`; since only `n_1-n_j` roots of
`R_1` can be absent from `R_j`, any subset `A` of those forced roots retains
at least `|A|-(n_1-n_j)` members.  Injectivity of `phi_j` on `R_j` gives the
claimed robust image cut.  The two displayed central ratios follow directly
from consecutive binomial ratios.

## 3. Boolean chainization audit

Below the middle, each consecutive Boolean inclusion graph has a matching
saturating the lower layer by normalized matching.  Independently choosing
one matching at each interface gives degree at most one in each direction;
every non-top vertex has an upward edge.  Hence all components are saturated
chains ending at the declared top.  This proves existence of an abstract
band-chain partition but makes no claim about forced-factor support.

For the protected-top refinement, two distinct rank-`s` sets have at most
one common rank-`s+1` superset.  Therefore Cauchy--Schwarz gives

\[
 |N(X)|\ge a^2x/(a+x-1).
\]

The exact surplus comparison is

\[
 a^2x-(a+x-1)^2
 =(x-1)(a(a-2)-(x-1)),
\]

so the small-family surplus is at least `a-1`; the biregular edge count
gives the displayed large-family surplus.  Deleting at most `eta_s` top
vertices therefore preserves Hall.  At the two central top interfaces the
first term is exactly `m+2` and the second is larger.  This reserves named
top **values** as singleton chains only; it does not prove that a prescribed
seam root has an alternate occurrence, which the theorem states explicitly.

## 4. Partition-matroid quotient audit

For a capacity-one partition matroid with no empty part, flats are unions of
parts.  Therefore `M_(j+1)` is a quotient of `M_j` exactly when its coarser
parts are unions of `M_j` parts, equivalently when `phi_(j+1)` factors through
`phi_j`.  A base of the quotient is independent in the larger matroid and
extends to a base there.  Starting at `M_(d-1)` and extending upward gives
the claimed nested bases in the correct direction.

Normalized matching gives a designated containing upper set for every lower
set.  Defining the deletion map on those designated upper sets and
arbitrarily elsewhere proves a surjective Boolean parent map.  This is only
an abstract scaffold; the theorem never infers a physical factor from it.

## 5. Pull no-go audit

Assume complete commutation

\[
 p_s(T+\beta)=p_{s-1}(T)+\beta.
\]

For an arbitrary `S`, let `delta` be the element deleted by `p_s` and take
`T=p_s(S)=S-delta`, `beta=delta`.  The left side omits `delta`; the right
side contains it.  This is an immediate contradiction.  The result rules
out only a transition-independent complete atlas.  It does not rule out a
sparse factor whose selected pulls all commute.

For minimum-deletion parent maps, a compatible pull replaces the old deleted
minimum `delta` by a new point `beta`.  The next parent identity retains
`beta`, forcing `beta>min(T)>delta`; the rank-set sum strictly increases.
Maximum deletion is the reversed strict potential.  This proves only the
extreme-parent gradient no-go, not acyclicity for arbitrary deletion maps.

## 6. Pascal splice audit

The two sectors partition the complete child owner layer:

\[
 {[k]\choose q}={[k-1]\choose q}
 \mathbin{\dot\cup}(\{z\}\star {[k-1]\choose q-1}).
\]

If height is at most forward distance to the seam, every selected future
intersection stays in one sector.  At depth `j`, the first child supplies
the `z`-free layer `binom([k-1],q-j)`, while the lifted second child supplies
`z star binom([k-1],q-j-1)`.  These are exactly the two disjoint Pascal
parts of `binom([k],q-j)`.  The theorem explicitly assumes legal seams and
global residence; it does not derive them.

## 7. Natural-Ucycle audit

In a natural singleton-window packing, repeated occurrences of one symbol
have cyclic spacing at least `q`; spacing exactly `q` would make consecutive
`q`-sets equal, so the spacing is greater than `q`.  Hence every positive
incidence run has length exactly `q`.  The common positional overlap of
`j+1` consecutive windows is the displayed length-`q-j` suffix.  A second
occurrence cannot bridge an exiting symbol without forbidden spacing `q`,
so no extra element lies in the intersection.

For `k=2m,q=m-1,m=2^a-1`, Kummer gives

\[
 v_2\binom{2m}{m}=a=v_2(m+1),
\]

so `C_m` is odd.  The complete coordinate degree is

\[
 D={q\over k}{k\choose q}=qC_m/2\equiv q/2\pmod q.
\]

Every packed coordinate degree is divisible by `q`, so every coordinate
loses at least `q/2` incidences.  Double counting omitted incidences gives
`H>=k/2=m`.  This proves an omission lower bound for the natural
singleton-window architecture only, not for block-valued or multilane
resident factors.

The primary tight-Euler theorem has quantifiers `for every fixed q` followed
by a threshold depending on `q`; substituting `k=2q+1` is not licensed.
Alternative all-parameter Ucycles in shorthand/difference representations
do not satisfy the singleton-window identity and are correctly excluded.

## 8. Scope verdict

The theorem proves:

* an exact collar selector reformulation;
* an exact local-support test after choosing a chain partition;
* a quotient/flag-matroid sufficient face;
* a complete-pull no-go;
* a conditional Pascal recursion; and
* an infinite-family natural-Ucycle omission bound.

It does not prove the supported-chain factor lemma, triangular safe openings,
residual low-rank renewal cover, connected upper-complete host, safe final
opening, or `nu(k)<=B(k)+O(1)`.  The advertised scope is therefore accurate.
