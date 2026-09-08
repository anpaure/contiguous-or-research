# Independent audit: K17 three-level common basis and algorithmic scope

**Date:** 2026-08-02  
**Status:** PASS after two wording corrections; pure-mathematics audit, no
finite search.

## 1. Cardinality and dual audit

For

\[
 L=\bigcup_{i=1}^6{[17]\choose i},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8},
\]

the sizes are

\[
 |L|=21777,\qquad |M|=19448,\qquad |R|=24310.
\]

The rank-seven/root transversal matroid `M7` has rank `19448`, hence its
dual on `R` has rank `4862`.  Therefore

\[
 N=M7^*\oplus U_{16915,M}
\]

has rank `4862+16915=21777`, equal to the rank of the low-receiver
transversal matroid `ML` on `E=M disjoint-union R`.

A basis `C` of `N` necessarily has

\[
 |C_M|=16915,\qquad |C_R|=4862.
\]

The complement `B=R-C_R` has size `19448`; `C_R` is a dual basis exactly
when `B` is an `M7` basis.  Perfect representing matchings `L -> C` and
`M -> B` then give

\[
 16915\ (L-M-R),\quad 4862\ (L-R),\quad
 2533\ (M-R),
\]

and hence histogram `(0,7395,16915)`.  The converse reads the same two
matchings from such a table.  This proves the claimed equivalence for the
**compressed three-level normal form**.

The qualifier is load-bearing.  The same histogram permits `a>0` chains of
type `L-L-R`; those are not encoded by the two transversal matchings.  The
root theorem has now been corrected to state compressed-normality
explicitly.

## 2. Edmonds and weighted applicability

For `X=X_M disjoint-union X_R`,

\[
\begin{aligned}
r_N(E-X)
 &=r_{M7^*}(R-X_R)+\min(16915,|M-X_M|)\\
 &=4862-|X_R|+r_{M7}(X_R)
   +\min(16915,|M-X_M|).
\end{aligned}
\]

Thus Edmonds' common-basis condition is exactly

\[
r_{ML}(X)+4862-|X_R|+r_{M7}(X_R)
+\min(16915,|M-X_M|)\ge21777
\]

for every `X subset E`.  Both nontrivial ranks are bipartite-matching
oracles, so ordinary weighted matroid intersection is a polynomial exact
algorithm for additive **ground-element** costs.

For this presentation the same weighted problem has a simpler specialized
implementation.  Put receiver cost `w_m` on every `y_lm`, receiver cost
`w_r` on every `y_lr`, and zero cost on `x_mr` in the base TU system.  Every
member of `C` receives exactly one `y` edge, so one integral min-cost flow
has objective `sum_(v in C) w_v` and returns both representing matchings.
Complementary root-bank costs are equivalent up to the constant total root
weight.  This does not change the edge-labelled socket limitation below.

This covers receiver/root membership costs, including a complementary cost
on `B=R-C_R`.  It does not cover a cost or constraint depending on which
matching edge represents a chosen receiver.  Forcing/deleting protected
elements is valid through common contractions/deletions only after checking
common independence and that both residual ranks equal the required
remaining basis cardinality.  Equality of the two residual ranks alone is
insufficient if both have fallen below the target.  These qualifications are
now explicit in the main theorem.

## 3. Conditional matching oracles

### Fixed `x`

An injective `x:M->R` leaves exactly `4862` roots `R0`.  The available right
shore for `y` is `V=M disjoint-union R0`.  Every vertex of `R0` is mandatory,
as is every middle whose selected `x` edge is marginally socket-negative.
A matching must saturate all `L` and these mandatory receivers.  This is
exactly a lower-bound bipartite flow.  At K17,

\[
 |V|-|L|=24310-21777=2533,
\]

so adjoining 2533 dummy left vertices adjacent to all optional receivers is
an equivalent perfect-matching formulation.

### Fixed `y`

Here `y` must first satisfy all low degrees and receiver capacities; it does
not by itself satisfy the final root equalities.  If `C_R` is the set of
roots hit directly by `y`, then `x` must be a perfect matching between `M`
and `B=R-C_R`.  Consequently `|B|=|M|` is essential.  Middles without a low
predecessor use only marginally socket-positive edges; all other middle rows
are unrestricted.  This is again one exact bipartite matching/Hall oracle.

The theorem wording was tightened from the ambiguous phrase “right degrees”
to “right-receiver capacity inequalities.”

## 4. Non-TU audit

There are two independently valid determinant-two certificates.  For the
integer-equivalent aggregate short-positivity row `E_m`, one low-degree row
`A_l`, and one root-degree row `C_r`, on columns
`(y_lm,y_lr,x_mr)` for a legal `l subset m subset r` with positive `m-r`,
the coefficient submatrix is

\[
\begin{pmatrix}
1&0&1\\
1&1&0\\
0&1&1
\end{pmatrix},
\qquad \det=2.
\]

For the literal implications `x_(m,r_i)<=z_m` themselves, take two
socket-negative roots.  The exact-one middle row and the two implications,
on `(x_(m,r_1),x_(m,r_2),z_m)`, give

\[
\begin{pmatrix}
1&1&0\\
1&0&-1\\
0&1&-1
\end{pmatrix},
\qquad \det=2.
\]

Therefore both natural socket-augmented matrices are not TU.  This proves only
that the base matching-integrality proof cannot simply be inherited; it is
not an infeasibility theorem and does not exclude a different extended
formulation.

The compact branch--Benders formulation in the theorem is exact for the two
unary marginal predicates.  Its low recourse is a capacitated bipartite
matching with receiver capacities `(h_m,d_r)`.  Since their sum is
`16915+4862=21777=|L|`, Hall is exactly

\[
 \sum_{m\in N_M(S)}h_m+\sum_{r\in N_R^q(S)}d_r\ge|S|
 \qquad(S\subseteq L),
\]

and one minimum cut separates it.  This remains only a projection once the
predicates depend on selected occurrence state or share physical resources.

## 5. Exact scope

**Closed:** compressed-normal static target allocation; receiver-set
optimization by weighted common basis; exact Hall separators after fixing
either matching shore.

**Open:** selection of the two representing matchings together with
occurrence-labelled socket DNFs, shared endpoint/resource capacities,
supplier Hall, topology, residence, upper/source/common-cap/compiler rows.
The common-basis solution is therefore an outer allocator and warm seed,
not a selected-state certificate.
