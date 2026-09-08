# Independent audit: nested intersection banks, Pascal recursion, and the natural-Ucycle boundary

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_NESTED_INTERSECTION_BANK_SUPPORTED_CHAIN_EQUIVALENCE_PASCAL_RECURSION_AND_UCYCLE_NOGO_20260804.md`  
**Method:** independent first-principles proof reconstruction; no computation,
finite search, or solver  
**Verdict:** **INDEPENDENT_GO**.  No source correction is required.  The
theorem is an exact reformulation/sufficient-face/no-go package and does not
claim the still-open supported resident factor.

## 1. Forced-intersection ranks and indexing

For

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},
 \qquad
 I_{i,j}=\bigcap_{u=0}^jQ_{i+u},
\]

residence at least `d` implies

\[
 I_{i,j}=Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\}
 \qquad(0\le j<d).
\tag{1.1}
\]

Indeed, a coordinate entering after `Q_i` and departing among these first
`j` transitions would have a positive run shorter than `d`; the same
argument prevents one coordinate from departing twice in the interval.
Thus the displayed departing coordinates are distinct members of `Q_i`,
and every other member survives.  Consequently

\[
 |I_{i,j}|=q-j.
\tag{1.2}
\]

Every positive prefix column therefore contains one member in each of the
distinct layers `q-1,...,q-h`; the band in the theorem is exactly
`q-d+1,...,q-1`.  All later uses of `j+1` and `j+2` respect their declared
ranges: the shift lemma uses `j<d-1`, and the two-parent pull identity uses
`j<d-2`.

## 2. Supported-chain equivalence

Given nested banks, the height

\[
 h(i)=\max\{j:i\in R_j\}
\]

satisfies `R_j={i:h(i)>=j}`.  Hence at layer `j` the selected prefix
columns contribute precisely `phi_j(R_j)`; its bijectivity is exactly one
copy of every member of that layer.  Distinct ranks are disjoint, so this
is an exact cover of the whole band.

Conversely, every saturated chain in a band partition has a unique top
`S` of rank `q-1`.  A supporting root belongs to the fibre
`phi_1^(-1)(S)`.  Fibres of different tops are disjoint, so choosing one
supporting root independently for every chain cannot repeat a root.  The
chosen heights recover the nested banks.  This proves all three directions
of Theorem 1.1.

The zero-one column system needs no separate root-capacity row: two
positive columns belonging to one root both contain `I_(i,1)`, violating
the equality row of that top.  Restricting columns by `h<=c(i)` proves the
capacitated/seam-safe version without introducing a cross-top matching.
For a fixed chain partition the support tests are therefore genuinely
local to the pairwise disjoint top fibres.

## 3. Abstract chainization and protected-top reservation

Below the Boolean middle, normalized matching gives at every consecutive
interface an inclusion matching saturating the lower rank.  Choosing the
interfaces independently yields indegree and outdegree at most one, and
every non-top vertex has one upward edge.  Since rank strictly increases,
the components are saturated chains ending in the declared top layer.

For Proposition 1.2A, a lower rank-`s` vertex has degree
`a=k-s`, an upper rank-`s+1` vertex has degree `b=s+1`, and two distinct
lower vertices have at most one common upper neighbour.  For
`X` of size `x`, if `d_Y` is its upper-neighbour multiplicity, then

\[
 \sum_Yd_Y=ax,
 \qquad
 \sum_Y{d_Y\choose2}\le{x\choose2}.
\]

Cauchy--Schwarz gives

\[
 |N(X)|\ge {a^2x\over a+x-1}.
\]

The exact numerator for surplus `a-1` is

\[
 a^2x-(a+x-1)^2
 =(x-1)\bigl(a(a-2)-(x-1)\bigr),
\]

so the small-family range is correct.  In the complementary range,
biregular edge counting gives surplus at least `(a-b)x/b`.  Taking the
floor of the smaller bound therefore permits deletion of every prescribed
top family of size at most `eta_s` while retaining Hall.

At the odd central interface `(a,b)=(m+3,m-1)` and at the even interface
`(a,b)=(m+3,m-2)`.  In both cases the first bound is `a-1=m+2` and the
second is strictly larger, so the stated reserve is exact.  The conclusion
correctly reserves named top **values** as singleton chains; it does not
reserve prescribed root occurrences.

## 4. Forced top fibres

If `u` fibres of `phi_1` are singleton and the other `n_1-u` nonempty
fibres have size at least two, then

\[
 N\ge u+2(n_1-u),
\]

which gives `u>=2n_1-N`.  Every singleton root is forced into `R_1`.
Since exactly `n_1-n_j` members of `R_1` are absent from `R_j`, at least
`|A|-(n_1-n_j)` members of any `A subseteq U` remain in `R_j`; injectivity
of `phi_j` there gives the claimed image cut.

The consecutive binomial ratios are

\[
 {n_1\over N}={m\over m+2}
 \quad(k=2m+1,q=m),
 \qquad
 {n_1\over N}={m-1\over m+2}
 \quad(k=2m,q=m-1),
\]

and reproduce both displayed singleton-root bounds.  Hence the
`O(N/k)` exceptional-top interpretation is valid in the central regime.

## 5. Partition-matroid quotient orientation

In the capacity-one partition matroid `M_j`, independence is exactly
injectivity of `phi_j`; a set of cardinality `|X_j|` is a base exactly when
`phi_j` is bijective.  This proves the nested-base formulation.

The quotient direction in Theorem 2.2 is correct.  If
`M_(j+1)` is a quotient of `M_j`, every `M_(j+1)`-independent set is
`M_j`-independent and a base of the quotient extends to a base of `M_j`.
Starting with a base of `M_(d-1)` and extending successively toward `M_1`
therefore gives the required nested bases.

For loopless capacity-one partition matroids, quotient means precisely that
every coarse `M_(j+1)` part is a union of fine `M_j` parts.  Equivalently,
equal `phi_j` values force equal `phi_(j+1)` values, which is exactly

\[
 \phi_{j+1}=p_j\circ\phi_j.
\]

Surjectivity of `phi_(j+1)` makes `p_j` surjective, and actual intersection
nesting forces `p_j(S) subset S` with one deletion.  Conversely, such a
factorization makes the required coarse partition and hence the quotient.

The abstract Boolean scaffold also checks out: normalized matching injects
the complete rank-`s-1` layer into containing rank-`s` sets; declaring
those designated parents and deleting arbitrarily elsewhere gives a
surjective deletion map.  This proves only existence of abstract quotient
maps, not their compatibility with one physical factor.

## 6. Pull identity and both no-go theorems

The entering point `beta_i` survives all roots used in the shift identity.
Every other point in `I_(i+1,j)` was already present in `Q_i`, because the
step introduces only `beta_i`.  Hence

\[
 I_{i+1,j}=I_{i,j+1}\mathbin{\dot\cup}\{\beta_i\}.
\]

Combining this with the two quotient factorizations gives the stated
physical pull identity on exactly the transitions used by the factor.

For a hypothetical complete pull-equivariant atlas, take any rank-`s` set
`S`, let `delta` be the point deleted by `p_s`, and set
`T=p_s(S)`, `beta=delta`.  The left side of the proposed identity is `T`
and omits `delta`, while the right side contains `delta`.  This is an
immediate contradiction.  The theorem rules out transition-independent
commutation, not a sparse selected set of compatible pulls.

For minimum deletion, write `S=T+delta` with `delta=min S`.  Compatibility
after replacing `delta` by `beta` requires the next deletion to remove
`min T`, so `beta` is retained and

\[
 \beta>\min T>\delta.
\]

The rank-set sum strictly increases on every compatible transition;
maximum deletion gives the reversed strict potential.  Thus neither
extreme rule supports a cyclic coherent factor.  No claim is made for an
arbitrary deletion atlas.

## 7. Pascal splice and seam distance

The two owner sectors are the disjoint Pascal decomposition

\[
 {[k]\choose q}
 = {[k-1]\choose q}
 \mathbin{\dot\cup}
   \bigl(\{z\}\star{[k-1]\choose q-1}\bigr).
\]

With `dist(i)` interpreted as the number of **internal** sector transitions
available before the outgoing seam, `h(i)<=dist(i)` is exactly the
condition that `Q_i,...,Q_(i+h(i))` remains in one sector.  In particular,
the last root has cap zero and the preceding root has cap one, as stated.

At depth `j`, the first child cover supplies every `z`-free
rank-`q-j` set once.  The lifted second child keeps `z` through the selected
window and supplies every `z`-containing rank-`q-j` set once after stripping
`z`.  These two families are disjoint and exhaust the layer by Pascal's
identity.  Child nestedness persists under their union.  Thus Theorem 4.1
is exact under its explicit hypotheses.

The theorem assumes, rather than proves, both legal cyclic seams and global
residence of the splice.  It also assumes supported child covers with the
triangular caps.  Its advertised conditional scope is therefore accurate.

## 8. Natural singleton-window identities

In a singleton word, one occurrence of a symbol lies in exactly `q`
consecutive length-`q` windows.  Distinctness inside every window forces
cyclic spacing between two occurrences to be at least `q`; equality would
make the Johnson step drop and add the same symbol and hence repeat the
window set.  Thus the spacing is greater than `q`, and every positive
coordinate-incidence run has length exactly `q`.

The positional intersection of `Q_i,...,Q_(i+j)` is the suffix at positions
`i+j,...,i+q-1`.  A symbol outside that suffix could belong to every window
only if a replacement occurrence bridged the exiting one with spacing
exactly `q`, already excluded.  Therefore

\[
 I_{i,j}=\{w_{i+j},\ldots,w_{i+q-1}\}.
\]

This verifies both the resident Johnson-cycle statement and the exact
multi-radius suffix-chain reformulation.  Ordinary natural-Ucycle
existence controls only the top window radius and does not supply that
nested exact cover.

## 9. Infinite even-central omission bound

Let `m=2^a-1`, `k=2m`, and `q=m-1`.  Kummer's theorem gives

\[
 v_2{2m\choose m}=a=v_2(m+1),
\]

so the Catalan number `C_m` is odd.  The complete layer size and one-point
degree are

\[
 N={2m\choose m-1}=mC_m,
 \qquad
 D={qN\over k}={qC_m\over2}
   \equiv {q\over2}\pmod q,
\]

where `q` is even.  In a cyclic singleton-window packing, a coordinate
occurring `t_x` times lies in exactly `q t_x` distinct windows.  Therefore
its omitted degree satisfies

\[
 h_x=D-qt_x\equiv q/2\pmod q,
 \qquad h_x\ge q/2.
\]

If `H` sets are omitted, double counting their incidences gives

\[
 qH=\sum_xh_x\ge 2m(q/2)=mq,
\]

and hence `H>=m=k/2`.  This proves the infinite-family lower bound for
every distinct natural singleton-window packing, not only for an attempted
complete Ucycle.

For odd central parameters,

\[
 {2m+1\choose m}=(2m+1)C_m,
\]

so this divisibility obstruction disappears, but no suffix-chain exact
cover follows.

## 10. Literature and scope boundary

The cited tight-Euler theorem proves natural subset Ucycles for each fixed
uniformity only beyond a threshold depending on that uniformity.  It cannot
be specialized along the diagonal `n=2q+1`.  The 2026 all-parameter
constructions explicitly use shorthand-frequency or difference/bounded-
weight representations, rather than windows whose symbols are the ground-
set elements.  They therefore do not imply the Johnson and intersection
identities audited in Section 8.

The source proves exactly:

* supported-chain/nested-bank equivalence;
* independent top-fibre support tests, including height caps;
* the linear protected-value reserve;
* a quotient-chain sufficient face and its abstract Boolean scaffold;
* complete-atlas and extreme-gradient pull no-gos;
* a conditional triangular Pascal splice; and
* the infinite-family natural-Ucycle omission bound.

It does not construct a resident supported-chain factor, seam-safe Pascal
openings, the residual low-rank cover, an upper-complete connected host, or
an additive bound for `nu(k)`.  No source correction is required.

