# Audit of the K17 `M7/ML/N` common-basis normal form

Date: 2026-08-02

This is a pure-mathematics wording and cardinality audit.  No finite run is
used.

## 1. Cardinalities

Put

\[
 L=\bigcup_{s=1}^{6}{[17]\choose s},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Then

\[
 |L|=21{,}777,\qquad |M|=19{,}448,\qquad |R|=24{,}310.
\]

Let `M7` be the rank-19,448 transversal matroid on ground set `R` presented
by the containment graph between `M` and `R`.  Its dual has rank

\[
 r(M7^*)=24{,}310-19{,}448=4{,}862.
\]

Let `ML` be the rank-21,777 transversal matroid on
`E=M disjoint-union R` presented by the containment graph between `L` and
`E`, and put

\[
 N=M7^*\oplus U_{16{,}915}(M).
\]

Thus

\[
 r(N)=4{,}862+16{,}915=21{,}777=r(ML).
\]

For a basis `C` of `N`, writing `C_M=C cap M` and `C_R=C cap R`,

\[
 |C_M|=16{,}915,\quad |C_R|=4{,}862,
 \quad |R-C_R|=19{,}448.
\]

The residual middle count and the length-two count are

\[
 |M-C_M|=2{,}533,qquad 2{,}533+4{,}862=7{,}395.
\]

All stated cardinalities are consistent.

## 2. Independence versus basis saturation

The proof-safe transversal wording is directional.

- A set `I subset E` is independent in `ML` iff the bipartite containment
  graph has a matching **saturating `I`**, equivalently an injection from
  `I` to distinct members of `L` contained in their receivers.  This need
  not saturate `L`.  If `I` is an `ML` basis, then
  `|I|=|L|=21,777`, so the matching is bijective and also saturates `L`.
- A set `Q subset R` is independent in `M7` iff a containment matching
  saturates `Q` into distinct members of `M`.  Only when `Q` is an `M7`
  basis, of size `|M|=19,448`, does that matching also saturate every member
  of `M`.
- A basis of the direct sum `N` saturates both summands: `C_R` is an
  `M7^*` basis and `C_M` is a size-16,915 basis of the uniform summand.
  Mere `N`-independence does not force either displayed cardinality.

Accordingly, phrases such as "match `L` into `C`" and "match `M` into
`R-C_R`" are justified after `C` and `R-C_R` have been proved bases, not
from transversal independence alone.

## 3. Required normal-form definition

Here **no-singleton three-level table** must explicitly mean a chain
partition of the compressed three-level poset in which all members of `L`
form one antichain level.  Equivalently, every chain has exactly one of the
following forms:

\[
 \ell\subset m\subset r,\qquad
 \ell\subset r,\qquad
 m\subset r,
 \tag{NF}
\]

where `ell in L`, `m in M`, and `r in R`.  In particular, a chain may not
contain two comparable members of `L`.

The length histogram alone does not imply `(NF)`.  For a generic Boolean
inclusion-chain partition, let

- `a` count chains of type `L-L-R`;
- `b` count chains of type `L-M-R`;
- `c` count chains of type `L-R`;
- `d` count chains of type `M-R`.

The target counts and histogram permit

\[
 (a,b,c,d)=(a,16{,}915-a,4{,}862-a,2{,}533+a)
 \quad(0\le a\le4{,}862).
\]

Thus `(0,7,395,16,915)` does not force `a=0`.  A statement about arbitrary
Boolean inclusion chains is therefore broader than the common-basis proof.
The theorem is exact after replacing it by the compressed-level normal form
`(NF)`.

## 4. Proof-safe common-basis equivalence

The corrected theorem language is:

> There exists an exact no-singleton normal-form table `(NF)` iff `ML` and
> `N` have a common basis.  More precisely, normal-form tables correspond to
> triples `(C,mu_L,mu_7)`, where `C` is a common basis, `mu_L` is a perfect
> representing matching between `L` and `C`, and `mu_7` is a perfect
> representing matching between `M` and `R-C_R`.

This is an existence equivalence, not generally a bijection between tables
and the element sets `C`: one common basis may admit several representing
matchings and hence several tables.

Given the triple, members of `C_M` produce the 16,915 chains
`ell-m-r`; members of `C_R` produce 4,862 chains `ell-r`; and members of
`M-C_M` produce 2,533 chains `m-r`.  Conversely, a normal-form table defines
`C_M` as the middles with low predecessors and `C_R` as the roots with direct
low predecessors.  Its two edge families are precisely the two perfect
representing matchings.

Since `ML` and `N` have the same rank 21,777, Edmonds' formula gives

\[
 \max\{|I|:I\text{ is common independent}\}
 =\min_{X\subseteq E}\bigl(r_{ML}(X)+r_N(E-X)\bigr).
\]

Hence a common basis exists exactly when every term on the right is at least
21,777.  This min--max statement is correct.

## 5. Scope

Weighted matroid intersection may select the common-basis element set and
ordinary matching algorithms may then recover representing matchings.  It
does not enforce socket labels shared by those matchings, occurrence
compatibility, protected endpoints, supplier state, topology, residence,
upper/source/compiler closure, or chronology.

The current literal witness audit has the consistent counts
`ML matching=21,777`, `M7 matching=19,448`,
`|C_M|=16,915`, and `|C_R|=4,862`; it witnesses the normal-form theorem but
is not needed for the abstract equivalence.
