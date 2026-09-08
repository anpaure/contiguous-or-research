# Hostile audit: MSW mixed monotone blocks and the cross-component-only seam gate

**Date:** 2026-08-13  
**Verdict:** **PASS.**  The MSW factor gives the asserted mixed
`q/(q+1)` owner-perfect augmented matching directly.  The `q+1` case has
exactly `q` transitions, but their `2q` physical coordinates are distinct, so
it is genuinely monotone.  The global lower complement is exactly the set of
cut MSW edges.  No generic augmented-hypergraph perfect-matching theorem is
needed.  
**Method:** direct arithmetic, cyclic-interval, and exact incidence-ledger audit;
no finite search or solver.

## 1. Frozen source

Audited and lightly normalized theorem:

`MATH_THEOREM_MSW_MIXED_MONOTONE_BLOCK_FACTOR_AND_CROSS_COMPONENT_ONLY_SEAM_GATE_20260813.md`

Original SHA-256:

`53012a43852cb67134d3957b5a809e2c5e6c1001e581faf4a27ada3876ff1686`

Final source SHA-256:

`4cc95399f355d0db5e9ea711ae3c0dad8e63baf6edbcf003a4489f7f9c45cb77`

The source changes only make the threshold explicit (`R>=16`), state the
integer domain of `d`, normalize notation, and link the primary MSW source.

## 2. Imported MSW factor

Put `m=R-1`, so the ground size is

\[
                         k=2m+1.                         \tag{2.1}
\]

The
[Mütze--Standke--Wiechert theorem](https://arxiv.org/abs/1603.02525)
constructs a `C_k`-factor of the odd graph on rank-`m` sets, with exactly
`Cat_m` cycles of length `k`.  In its tight-order form, each component is
the `k` cyclic `m`-windows of one cyclic coordinate order.  These component
supports partition the rank-`m` layer.

Complementing one tight deck gives the rank-`R=m+1` owner cycle

\[
 T_i=\{x_i,x_{i+1},\ldots,x_{i+R-1}\},\qquad i\in\mathbb Z_k. \tag{2.2}
\]

Its edge intersection is

\[
 T_i\cap T_{i+1}=\{x_{i+1},\ldots,x_{i+R-1}\},          \tag{2.3}

another cyclic `m`-window in the same deck.  The map from starts in (2.2)
to starts in (2.3) is a cyclic shift, so each deck uses exactly the same
rank-`m` support as its lower edge-label set.  Consequently, across the
MSW factor, both owners and immediate-lower colours occur exactly once.

The number of components is

\[
 {W\over k}={1\over R}{2R-2\choose R-1}
            =\operatorname {Cat}_{R-1}.                 \tag{2.4}

This confirms that the post-theorem fusion gate is Catalan-scale.

## 3. Exact arithmetic

Since

\[
 \Lambda=2^{2R-2}={4^R\over4},\qquad
 W={1\over2}{2R\choose R},                              \tag{3.1}

the standard central-binomial bound

\[
 {2R\choose R}\ge {4^R\over2\sqrt R}                  \tag{3.2}

gives

\[
                         {\Lambda\over W}\le\sqrt R.    \tag{3.3}

At `t=ceil(Lambda/W)`, already `tW>=Lambda`, so the nonnegative
triangular term can only make the minimal `d` smaller.  Hence

\[
                         q=d+1\le\sqrt R+2.              \tag{3.4}

For every `R>=16`,

\[
 q(q-1)\le(\sqrt R+2)(\sqrt R+1)
          =R+3\sqrt R+2\le2R-1=k,                       \tag{3.5}

and `2<=q<=R-1`.  The lower bound follows because `t=0` cannot satisfy
the defining inequality.  Since `gcd(q,q+1)=1`, the Frobenius number is

\[
                         q(q-1)-1.                       \tag{3.6}

Thus every `k>=q(q-1)` has a representation

\[
                         k=aq+b(q+1),\qquad a,b\ge0.     \tag{3.7}

The arithmetic in the theorem is therefore exact, with the explicit
sufficient threshold `R>=16`.  The construction itself applies at every
smaller parameter for which `q<=R-1` and (3.7) happen to hold.

## 4. The `q+1` endpoint case

This is the only potentially delicate monotonicity point.  A segment with
`s` owners has `s-1` transitions.  For `s in {q,q+1}`, put `ell=s-1<=q`.
Starting at `T_i`, these transitions delete

\[
                         x_i,\ldots,x_{i+\ell-1}          \tag{4.1}

and insert

\[
                         x_{i+R},\ldots,x_{i+R+\ell-1}.  \tag{4.2}

Both lists are individually injective.  After rotating the coordinate
indices so `i=0`, the first lies in `[0,ell-1]` and the second in
`[R,R+ell-1]`.  Since `ell<=q<=R-1`, the latter endpoint is at most
`2R-2=k-1`; there is no wrap, and the two lists are disjoint.  Therefore
all transition supports are pairwise coordinate-disjoint.  Every segment,
including a `q+1`-owner segment, is exactly a monotone exchange path.

## 5. Owner and lower ledgers after cutting

Cutting a cycle into consecutive segments changes no owner occurrence, so
all selected blocks partition the owner layer.  On a component with `a+b`
blocks, exactly `a+b` old edges are cuts, and all other old edges are
internal.  Since the original lower edge labels are globally exact,

* all internal lower colours are globally distinct;
* no cut colour appears internally; and
* the unused lower-colour set is exactly the set of cut-edge labels.

Each block, regardless of whether its owner size is `q` or `q+1`, has
exactly one following cut.  Thus the phrase “one missing colour per block”
remains literal in the mixed packing.  Restoring each original cut edge
uses every omitted colour once and recovers exactly the starting MSW
component.

## 6. Residence audit

In the owner cycle (2.2), each coordinate is present on exactly `R`
consecutive vertices and absent on exactly `R-1` consecutive vertices.
The arithmetic gives `q<=R-1`, so both run lengths are at least `q`.
Restoring the original cuts therefore gives `q`-biresident components.

The open segments are not independently resident; as established in the
monotone-path audit, they have only boundary-clipped runs.  The theorem does
not make the false local claim: its residence assertion is explicitly for
the components after the old MSW cuts are restored.

## 7. Exact consequence and remaining gate

The mixed augmented owner-plus-internal-lower hypergraph already has an
explicit owner-perfect matching: take all segments cut from the MSW factor.
The old cuts provide a rainbow legal seam cycle separately inside every
wreath.  Thus the following gates are closed:

* exact mixed `q/(q+1)` owner packing;
* global injectivity of internal lower colours;
* exact one-ticket-per-block deficit; and
* `q`-resident fusion inside each wreath.

What remains is not another matching nibble.  It is a cross-wreath
rethreading theorem which replaces selected old cuts by new seams while
simultaneously preserving:

1. owner and lower exactness;
2. the `q`-transition-collar condition;
3. connectivity across all `Cat_(R-1)` wreaths; and
4. the upper/source occurrence requirements.

The published middle-levels/odd-graph Hamiltonizations prove connectivity
of related MSW factors, but their existing invocation does not certify the
mesoscopic `q`-collar condition or repair the canonical upper-deck holes.
The theorem correctly leaves those issues open.

**Final verdict: PASS.**
