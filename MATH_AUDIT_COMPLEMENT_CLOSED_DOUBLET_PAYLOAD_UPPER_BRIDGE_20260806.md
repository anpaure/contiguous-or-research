# Audit: complement-closed doublets, payload thinning, and the PBBS upper bridge

**Date:** 2026-08-06  
**Method:** rank, occurrence, and resource audit; no computation or search  
**Status:** the polynomial complement-paired repair is valid.  A local
complement-closed balanced doublet is not a complete arbitrary-upper
compiler.  The only proof-safe positive route is to install the payload
atlas in the same owner chronology as the PBBS whole-fan baseline (with a
polynomial paired repair bank).

## 1. Claims which survive the audit

The following statements are exact.

1. If two source antecedents have the same labelled depth-`d` derivative,
   then every corresponding source interval of width at least `d+1` has
   the same OR value.  Therefore owner-invisible payload thinning is also
   invisible to the complete long/upper deck.
2. In the balanced middle-level incidence graph, the whiskered geodesic
   for an upper target `Z` and its complemented incidence path are
   resource-disjoint.  The first has owner union `Z`; the second has owner
   intersection `[n]-Z`.
3. The random-permutation proof for polynomial upper-backup paths survives
   after adjoining the complementary path.  Avoidance probabilities merely
   acquire the symmetric exact-value terms, and both exposure expectations
   remain `O(M/R^2)=o(1)` when `M=O(R^(3/2))`.
4. Hence the `O(R^3)` PBBS puncture leave has one polynomial protected bank
   repairing its paired lower-intersection and upper-union values in the
   same simple factor.

The exact proofs are in

`MATH_THEOREM_COMPLEMENT_PAIRED_BACKUP_AND_PAYLOAD_UPPER_BRIDGE_20260806.md`.

## 2. Why the endpoint whiskers are necessary

For an owner geodesic `V_0,...,V_s`, the internal facets

\[
                         L_i=V_i\cap V_{i+1}
\]

need not have union equal to the owner union.  A coordinate used only at
`V_0` or only at `V_s` is absent from every internal facet.  Therefore the
naive inference

\[
 \bigcap_i\overline{L_i}
       =\overline{\bigcup_iV_i}
\]

is false in general.

Adding one facet `L_-` at `V_0` distinct from `L_0`, and one facet `L_+`
at `V_s` distinct from `L_(s-1)`, gives

\[
 L_-\cup L_0=V_0,
 \qquad L_{i-1}\cup L_i=V_i,
 \qquad L_{s-1}\cup L_+=V_s.
\]

This is the precise reason the dual path in the theorem has `s+2` owners,
not merely `s`.

## 3. Rank and parity audit for an exact complement supermacro

### Even ground set

For `k=2r`, complementation preserves the owner rank.  If an owner path is
paired with its literal complement, every owner intersection on one half
has the complementary owner union on the other half.

This does not permit pairing an already spanning factor with its
complement: both halves use the complete owner set and every owner is
doubled.  A valid supermacro factor must select one local representative
from every complement pair and include its dual before enforcing owner
capacity.

The lower projection also changes nontrivially.  For the dual owner path,

\[
 P_i^{\rm dual}
 =\bigcap_{h=0}^{d}\overline{T_{i+h}}
 =\overline{\bigcup_{h=0}^{d}T_{i+h}}.
\]

It is not `overline(P_i)`, which has the wrong rank.  Thus owner-disjointness
does not certify lower-resource disjointness; the dual lower row must be
part of the superedge ledger.

### Odd ground set

For `k=2R-1`, a rank-`R` owner complements to rank `R-1`.  There is no
same-shape pointwise complement macro on the owner shore.  The balanced
incidence construction of the main theorem is the correct replacement:
endpoint facets become complementary rank-`R` owners and the old owners
become complementary rank-`(R-1)` lower vertices.

Therefore a proposed odd complement-closed doublet which simply replaces
every owner by its complement has a literal rank error.

## 4. Why deep payload complements are not exported locally

Let `k=2r`, and let a deep payload target have rank `s<r-d`.  Its
complement has rank `2r-s`.  A path of `ell` rank-`r` Johnson owners has
union rank at most `r+ell-1`, so any witness needs

\[
                         \ell\ge r-s+1>d+1.
\]

A deadline-sized macro and its deadline-sized dual are too short.  More
fundamentally, payload thinning does not change the owner trace at all.
If the payload value was not an owner intersection before thinning, its
complement cannot appear by complementing that unchanged owner path.

This disproves the proposed implication

\[
 \text{bottom macro with a complete deep payload atlas}
 \Longrightarrow
 \text{the exact dual macro has the complete upper deck}.
\]

What complement closure gives locally is exactly the top-`d` dual fan.
The all-depth baseline must still come from the PBBS whole-fan section or
another genuinely global owner-intersection construction.

## 5. Why the polynomial paired bank is enough on the PBBS face

The PBBS whole-fan section already carries the exponential lower/
complementary-upper baseline.  The rethread punctures only `O(R)` selected
edges, and the inverse-fan theorem compresses every affected named target
to an `O(R^3)` bank with `O(R^(3/2))` targets per rank stratum.

This is precisely the range of the paired-packing theorem.  Hence no
exponential dual macro bank is needed **after the canonical PBBS baseline
has been retained**.  The paired bank repairs the named puncture leave;
the unchanged section carries every other target.

The paired forest still needs a common resident source completion.  Its
existence as a simple factor does not manufacture source histories.
However, once one literal lower compiler exists, terminal compiler
functoriality and common-history fusion remove the terminal common-cap
matching from this step.

## 6. Exact remaining theorem

The strongest remaining bridge is not an arbitrary source homotopy between
the bottom factor and the PBBS factor.  It is the following relative
construction.

> **PBBS-relative protected payload macroization.**  Keep the PBBS
> whole-fan section and its polynomial complement-paired repair bank in one
> resident owner factor.  On the same factor, expose a block-structured
> rank-`(r-d)` projection with a canonical-lock transversal outside the
> blocks and a complete named deep-target payload atlas inside them.  Fuse
> the source components at palette-safe common histories and choose an
> upper-safe linear opening.

This theorem would bypass both the canonical PBBS deep remote selector and
the terminal common cap.  Current balanced-doublet rounding does not prove
the word “relative”: it chooses a new owner factor and lower projection,
whereas the PBBS section is an exponentially structured prescribed bank.

## 7. Scope exclusions

This audit does not claim:

* a complement-closed integral balanced-doublet factor;
* a complete named bottom payload atlas;
* a source homotopy preserving an arbitrary near-saturated compiler;
* resident antecedents for the unprotected factor cycles;
* an upper-safe final cut; or
* `nu(k)<=B(k)+O(1)`.

It does close one real issue: polynomial PBBS upper repair and its paired
lower owner-intersection repair can be selected as one protected forest.
The remaining lower obstruction is the literal payload macroization on
that same factor, not another upper-target matching.
