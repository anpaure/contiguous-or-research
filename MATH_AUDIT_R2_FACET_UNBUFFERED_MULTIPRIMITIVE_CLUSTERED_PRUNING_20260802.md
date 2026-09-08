# R2 audit: unbuffered multi-primitive clustered pruning

**Date:** 2026-08-02  
**Verdict:** `PASS` for the stated owner/marked-lower-deck and aggregate
semigroup claim.  The corrected longer-cycle immediate-upper extension also
passes.  Neither result joins the separate cycles into one chronology.

## 1. Literal ranks, parity, and injectivity

Put `q=d+2`, `c=r-q+1`,

\[
 m_0=\lceil q/2\rceil,\qquad L=2m_0.
\]

Then `L=q` for even `q` and `L=q+1` for odd `q`, and in both cases
`L>d+1=q-1`.  With `|X|=c-1`, support
`A={beta} disjoint-union V`, `|V|=L`, and alternating sources

\[
 S_t=X+z_t\quad(P),\qquad S_t=X+\beta+z_t\quad(H),
\]

the source ranks are exactly `c` and `c+1`.  A prefix of `j` consecutive
sources, `2<=j<=q-2`, has rank

\[
 (c-1)+1+j=c+j,
\]

and an owner window of `d+1=q-1` sources has rank

\[
 (c-1)+1+(q-1)=r.
\]

Every window of length at least two contains an `H`, hence contains
`beta`.  At each fixed marked rank the tag set is a cyclic interval of
proper length `<L`, so different starts give different resources.  This
proves literal owner injectivity and marked-lower-deck injectivity in both
parities.  The cycle has `m_0` occurrences of each type, hence exactly
`m_0` copies of `g_(d-1,d+1)` and no short-buffer occurrence.

The exact per-cycle named-cylinder count is

\[
 2m_0+L(q-3)+L=L(q-1)=\Theta(q^2),
\]

consisting of the two primitive low rows, all marked central rows, and the
owner row.

## 2. Exact trace saving and pruning asymptotics

Every resource is uniquely `X disjoint-union R` with `R subseteq A`, so its
intersection with `[k]-A` is exactly `X`.  For a second reservoir with
support `A'`, footprint `R'`, and core `X'`, put `E=A'-A`.  A collision

\[
 X\cup R=X'\cup R'
\]

forces

\[
 X\cap E=R'\cap E,
\]

because `R cap E` and `X' cap E` are empty.  Crucially, after `R'` is fixed
this necessary trace is independent of every first footprint `R` and of
`X'`.  Therefore the union bound has only `L(q-1)=Theta(q^2)` second
footprints, not its square.

Writing `Q=|A|=L+1`, `M_L=binom(k-Q,c-1)`, `b=|E|`, one fixed trace has
relative size `O(2^{-b})` uniformly in the canonical range.  Also

\[
 \mathbb E 2^{|A\cap A'|}
 \le \exp\!\left(Q^2/(k-Q+1)\right)=O(1).
\]

Hence the mean number of first-reservoir cycles damaged by a second is

\[
 O(M_Lq^2/2^q).
\]

Sampling `Theta(2^q/q^2)` reservoirs and deleting every cross-colliding
cycle loses only a constant expected fraction.  Since
`M_L=Theta(W/2^q)`, a sample exists with `Omega(W/q^2)` pairwise
owner/marked-deck-disjoint literal cycles.  Each contains
`m_0=Theta(q)` primitive signatures, yielding `Omega(W/q)` mutually
named-deck-disjoint primitive packages.  Those packages remain correlated
inside their length-`L` cycles; this count is not a count of separately
openable components.

## 3. Aggregate reservation and conductor

One selected cycle subtracts

\[
 m_0e_{d-1}+m_0e_{d+1}
\]

from the canonical age vector.  The resource weights of the two adjacent
coordinates are both one, so low and high resource decrease equally and
the standing slack `L_low-H_high` is unchanged.  If

\[
 t m_0\le
 \min\{A_{d-1}-Q_{r,d}-1,\ A_{d+1}-Q_{r,d}-1\},
\]

and the unchanged coordinates `A_(d-3),A_(d-2)` are at least
`Q_(r,d)+1`, the exact buffered-semigroup criterion applies to the residual
vector.  Canonically `A_(d-1),A_(d+1)=Theta(W/q)`,
`m_0=Theta(q)`, and the conductor is negligible, so a sufficiently small
constant multiple of `W/q^2` cycles fits.  No positive lower bound on
`L_low-H_high` beyond its inherited nonnegativity is needed.

This conductor is an age-semigroup conductor only.  It is not a Hall
theorem for occurrence positions, a component-joining conductor, or a
labelled lift of the residual formal decomposition.  The application is
asymptotic and uses `d>=4`, `d+1<r`, the canonical standing inequality
`L_low>=H_high`, and the four conductor-coordinate margins.

## 4. Immediate-upper parity boundary and live-file drift

For even `q`, the minimal owner-simple cycle has `L=q`.  Its owners are the
`q` facets of one `(r+1)`-set, so the union of any two distinct consecutive
owners is that same set.  Thus the stated minimal cycle does **not** have an
injective immediate-upper deck.  If that extra row is required, the
smallest alternating length must satisfy `L>q`:

\[
 m=\lfloor q/2\rfloor+1,\qquad
 L=2m=\begin{cases}q+2,&q\text{ even},\\q+1,&q\text{ odd}.
 \end{cases}
\]

The extra upper row then contributes `L` cylinders, changing the full count
to `Lq`; all trace and asymptotic estimates remain `Theta(q^2)`.

The exact user-stated lower/owner theorem is consistently frozen in
`MATH_THEOREM_FACET_ALTERNATING_PRIMITIVE_RESERVOIR_AND_PROTECTED_CHRONOLOGY_GATE_20260802.md`,
SHA-256
`2ebe28aab2e8c837297b30da2f357233862cb97b6d4c6abe20d19d698353127e`.
During this audit,
`MATH_THEOREM_FACET_UNBUFFERED_MULTIPRIMITIVE_CLUSTERED_PRUNING_AND_SOCKET_RESERVATION_20260802.md`
changed from the matching lower-deck version (observed SHA-256
`0c36425560ada2dab34e6866fd2b9165ee77aaab4b87abb13f9d65b82d87a493`)
to an attempted immediate-upper version.  The captured later snapshot has
SHA-256
`98eab0dd641f67be7131a374e955bbec40b7248e8fd89bbe66560343b5481e33`,
and is internally inconsistent: Section 0 uses the longer `m,L` and `Lq`,
while later sections still use undefined `m_0`, the old parity statements,
the old `L(q-1)` ledger, and old support-size alternatives.

The author subsequently synchronized every affected row.  The corrected
immediate-upper theorem has SHA-256
`87dacb2d1cefae06adf82bb7875303740f95bb65b1ad0aaa620adc3a76d73226`
and is frozen separately as `immediate_upper.snapshot.md`.  It uses the
longer parity above, includes the rank-`r+1` cyclic `q`-interval row, counts
`Lq` cylinders, uses `Q=q+3` for even `q` and `Q=q+2` for odd `q`, and
subtracts `m` copies at each adjacent conductor coordinate.  The same trace,
overlap-moment, pruning, and balanced-reservation proof applies, so this
corrected extension passes as well.  The intermediate `98e...` snapshot is
retained only as drift provenance and is not a theorem certificate.

## 5. Scope

The minimal-cycle pass proves separate literal cycles, pairwise distinct
owners and marked lower targets, weighted-small named-bank avoidance, and an
exact aggregate residual decomposition.  The longer corrected cycle also
proves the immediate-upper row.  Neither proves an occurrence-to-position
matching, fusion, one global chronology, join cross-windows, residence,
deeper upper deck, topology, opening, or compiler/common-cap compatibility.
