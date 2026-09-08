# Independent audit: K17 common basis, branch--flow, and literal one-ticket extension

**Date:** 2026-08-02  
**Audited note:**
`MATH_THEOREM_K17_THREE_LEVEL_COMMON_BASIS_AND_SOCKET_NON_TU_BRANCH_FLOW_20260802.md`  
**Audited snapshot SHA256:**
`dd51f41de8bb24ac9198f263f695481e75ebf90a10e053880c079e2eb3ffed10`  
**Verdict:** PASS for the compressed three-level normal form and the stated
marginal socket predicates.  The exact literal one-ticket test is a
presentation-minor common-basis test, not ordinary receiver contraction.

## 1. Counts and the common-basis equivalence

Let

\[
 L=\bigcup_{i=1}^6{[17]\choose i},\qquad
 M={[17]\choose7},\qquad R={[17]\choose8}.
\]

Direct binomial evaluation gives

\[
 |L|=21777,\quad |M|=19448,\quad |R|=24310,
\]

and hence

\[
 |R|-|M|=4862,
 \quad |L|-4862=16915,
 \quad |M|-16915=2533,
 \quad 2533+4862=7395.
\]

The theorem is exact only for the displayed normal-form chains

\[
 \ell-m-r,\qquad \ell-r,\qquad m-r.                 \tag{1.1}
\]

Its strengthened wording in the audited snapshot explicitly includes this
restriction and correctly says that tables correspond to triples
`(C,mu_L,mu_7)`, not to the receiver set `C` alone.

For a common basis `C` of

\[
 M_L,\qquad N=M_7^*\oplus U_{16915,M},
\]

the direct-sum ranks force

\[
 |C\cap M|=16915,\qquad |C\cap R|=4862.
\]

The complement `B=R-(C cap R)` is a basis of `M_7`, so a representing
matching `M -> B`, together with a representing matching `L -> C`, produces
all chains in (1.1).  Conversely, the two edge families of any table (1.1)
are exactly these two representing matchings.  This verifies both directions
of Theorem 2.1.

The dual rank formula is also correct:

\[
 r_{M_7^*}(X)=|X|-19448+r_{M_7}(R-X).                \tag{1.2}
\]

Substituting (1.2) into Edmonds' criterion gives exactly

\[
 r_{M_L}(X)+4862-|X_R|+r_{M_7}(X_R)
 +\min\{16915,|M-X_M|\}\ge21777.                    \tag{1.3}
\]

Thus the static receiver allocation is genuinely a two-matroid common-basis
problem.

## 2. Non-TU socket row

For binary `x`, the literal implication

\[
 x_{mr}\le p_{mr}+z_m                                  \tag{2.1}
\]

is exact.  If one middle `m` has two negative choices `r_1,r_2`, the exact-one
row and the two implications have, on columns
`x_(m,r_1),x_(m,r_2),z_m`, the submatrix

\[
 \begin{pmatrix}
 1&1&0\\
 1&0&-1\\
 0&1&-1
 \end{pmatrix},
 \qquad \det=2.                                      \tag{2.2}
\]

So the literal implication matrix is not TU in general.  The audited note
also correctly distinguishes (2.1) from the aggregate row

\[
 z_m+\sum_{r:p_{mr}=1}x_{mr}\ge1.                    \tag{2.3}
\]

They are equivalent on integral exact-one `x`, but (2.3) is stronger in the
fractional relaxation: (2.1) bounds `z_m` by the largest negative-edge
fraction whereas (2.3) bounds it by their sum.

The two-by-two objective-gap example in the note is valid.  The all-half
point has negative-edge objective one, while every integral feasible
matching has objective zero.

## 3. Exact branch--flow conditions

### 3.1 Fixed `x`

Let `R_0` be the roots missed by `x`, and let

\[
 D_M=\{m:p_{m,r(x,m)}=0\}.
\]

The remaining problem is exactly a matching from all `L` into
`M disjoint_union R_0` which saturates every vertex of

\[
 D=R_0\mathbin{\dot\cup}D_M.                         \tag{3.1}
\]

All `L-R_0` edges are filtered by `q`.  This is a bipartite circulation with
unit lower bounds on the vertices in `D`; no other condition is missing.
Equivalently, add `2533=|M disjoint_union R_0|-|L|` dummy left vertices,
join each dummy to every optional receiver `M-D_M`, and ask for a perfect
matching.  This gives an ordinary Hall/min-cut certificate.

### 3.2 Fixed `y`

Put

\[
 C_R=\{r:\sum_l y_{lr}=1\},\qquad
 S_M=\{m:\sum_l y_{lm}=0\},\qquad B=R-C_R.
\]

Then completion is exactly a perfect matching `M -> B`, with edges out of
`S_M` restricted to `p=1` and all edges out of `M-S_M` unrestricted.  The
cardinality check `|B|=|M|` is necessary.  Subject to it, Hall's inequalities

\[
 |N(Q)\cap B|\ge |Q|\qquad(Q\subseteq M)             \tag{3.2}
\]

are necessary and sufficient.

### 3.3 Fixed `(x,h,d)` Benders recourse

The low recourse selects exactly the receiver set

\[
 T(h,d)=\{m:h_m=1\}\mathbin{\dot\cup}\{r:d_r=1\}.
\]

The master equations force `|T(h,d)|=21777=|L|`.  Therefore a matching
saturating `L` automatically saturates all selected receivers.  Hall's
theorem gives exactly

\[
 \sum_{m\in N_M(S)}h_m+
 \sum_{r\in N_R^q(S)}d_r\ge |S|\qquad(S\subseteq L), \tag{3.3}
\]

with one min-cut separator.  Hence Theorem 4.1 is exact, including at
fractional master points.

## 4. Smallest exact one-ticket extension criterion

There are two different notions and they must not be conflated.

### 4.1 Receiver-only ticket

If a ticket merely forces one ground element `e` into the receiver set and
does **not** prescribe its representing matching edge, then it extends iff
`e` is nonloop in both matroids and

\[
 r_{M_L/e}(X)+r_{N/e}((E-e)-X)\ge21776
 \quad\text{for every }X\subseteq E-e.              \tag{4.1}
\]

This is ordinary common contraction.

### 4.2 Literal chain ticket

A literal ticket fixes matching edges, so (4.1) is too weak: contraction may
rematch the forced receiver to another witness.  The exact criterion uses
**presentation minors**.  Let `G_L` be the low/receiver containment graph and
`G_7` the middle/root containment graph.  In every case below, first require
the residual `G_7` presentation to have the displayed full rank.

#### Direct ticket `tau=(l,r)`

Delete low witness `l` and receiver `r` from `G_L`, and delete root `r` from
`G_7`.  On

\[
 E_tau=M\mathbin{\dot\cup}(R-r)
\]

put

\[
 A_tau=T(G_L-l_L-r_R),\qquad
 N_tau=T(G_7-r_R)^*\oplus U_{16915,M}.              \tag{4.2}
\]

The residual `G_7` rank must be `19448`; then both matroids in (4.2) have
rank `21776`.  The edge `l-r` extends iff they have a common basis.

#### Middle ticket `tau=(m,r)`

Delete receivers `m,r` from `G_L`, and delete source `m` and root `r` from
`G_7`.  On

\[
 E_tau=(M-m)\mathbin{\dot\cup}(R-r)
\]

put

\[
 A_tau=T(G_L-m_R-r_R),\qquad
 N_tau=T(G_7-m_L-r_R)^*\oplus U_{16915,M-m}.        \tag{4.3}
\]

The residual `G_7` rank must be `19447`; then both desired ranks are
`21777`.  The edge `m-r` extends iff (4.3) has a common basis.

#### Three-chain ticket `tau=(l,m,r)`

Delete `l` on the low witness shore, receivers `m,r`, source `m` on the
middle shore, and root `r`.  On the same ground as (4.3), put

\[
 \begin{aligned}
 A_tau&=T(G_L-l_L-m_R-r_R),\\
 N_tau&=T(G_7-m_L-r_R)^*\oplus U_{16914,M-m}.
 \end{aligned}                                      \tag{4.4}
\]

Again the residual `G_7` rank must be `19447`; both desired ranks are now
`21776`.  The literal pair of edges `l-m,m-r` extends iff (4.4) has a common
basis.

In all three cases the common-basis condition is the single exact family

\[
 r_{A_tau}(X)+r_{N_tau}(E_tau-X)\ge rho_tau
 \qquad(X\subseteq E_tau),                           \tag{4.5}
\]

where `rho_tau` is the displayed residual rank.  This is polynomially
separable by the same two matching oracles as the unpinned theorem.  It is
the smallest proof-safe static prefilter for one literal ticket.  Its scope
ends before occurrence-history, shared-resource, supplier, chronology,
residence, upper, and compiler constraints.

## 5. Minimal exact master schema

For the marginal socket face, the smallest useful exact master is:

1. binary `x_(m,r),h_m,d_r` with (4.1) of the audited theorem;
2. low-flow Hall cuts (3.3), generated lazily;
3. explicit representing `y` only when a branch is decoded;
4. for every literal occurrence ticket `tau,s`, a binary state variable
   implying its selected `x/y` edges and its named resource uses;
5. capacity rows on shared occurrence resources and exact selected-state
   supplier Hall cuts; and
6. the presentation-minor test (4.5) as an exact one-ticket prefilter or
   branch infeasibility certificate.

Receiver-only common-basis weights may guide the outer search.  They cannot
replace items 4--6 because those depend on representing edges and occurrence
states.

## 6. Scope-safe conclusion

The common-basis theorem, dual-rank formula, determinant-two obstruction,
and both conditioned branch flows are correct on the audited snapshot.  The
new exact deduction is the literal-ticket criterion (4.2)--(4.5).  It closes
only extendability inside the compressed static three-level table.  It does
not establish a socket-complete K17 selector, topology, residence, upper
coverage, common cap/compiler feasibility, or a word.
