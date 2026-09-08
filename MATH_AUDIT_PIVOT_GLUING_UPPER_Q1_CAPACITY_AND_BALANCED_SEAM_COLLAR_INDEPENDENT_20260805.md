# Independent audit: upper-q1 capacity and the balanced seam-collar bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Audited source:**
`MATH_THEOREM_PIVOT_GLUING_UPPER_Q1_CAPACITY_AND_BALANCED_SEAM_COLLAR_20260805.md`,
SHA
`4c8bcea15a45611fc920cb7033837d8bc5a642af1b5ba3887eb7c52e0e273444`.

## Verdict

`GO`; no source correction is required.  The component/collar transition
ledger, the impossibility of component-internal upper-q1 completeness at
the stated Catalan scale, every local owner/upper/lower collar formula, the
two-shore deletion bounds, the minimum-degree extraction, and the greedy
construction of the exact even and odd collar banks are correct.

In particular, the proof of Theorem 2.4 has no hidden within-collar reuse:
at each step the forbidden neighbours listed in the source include every
previously chosen resource, and the resulting lambda/rho normal form makes
all other resources new.  The hypothesis `r>=4s+8` is stronger than the
two minimum-degree inequalities actually needed and is therefore safe in
both parities.

This audit does **not** turn the owner/upper-disjoint bank into the
simultaneously low-star-spread bank of Theorem 2.3, construct the punctured
ordered four-transversal, or prove a protected trace factor or an
all-dimensional upper bound.

## 1. Exact transition capacity

Let the `c` nonempty components have a total of `W-bs` owners.  Their
numbers of internal transitions sum to

\[
                 E_{\rm comp}=W-bs-c.
\tag{1.1}
\]

The `b=c-1` bridges contribute `b(s-1)` internal transitions and `2b`
seams, so

\[
 E_{\rm collar}=b(s+1),\qquad
 E_{\rm comp}+E_{\rm collar}=W-1.
\tag{1.2}
\]

If an interval of distinct rank-`r` owners has rank-`r+1` union `Z`, then
any two consecutive owners in it are distinct rank-`r` subsets of `Z`.
Their union is therefore exactly `Z`.  Thus a q1 target can be charged to
an adjacent transition, and one transition can be charged only its own
union.  Consequently the collars must provide at least

\[
 D_U=U-E_{\rm comp}=U-W+bs+c
\tag{1.3}
\]

distinct q1 colours.  If all `U` colours occur, precisely `U` of the
`W-1` transitions are first providers and the remaining

\[
                       R_U=W-1-U
\tag{1.4}
\]

are either above-q1 transitions or repeat providers.  Finally

\[
 E_{\rm collar}-D_U
 =b(s+1)-(U-W+bs+c)=W-1-U.
\tag{1.5}
\]

For `k=2r`, write `C=W/(r+1)`.  Since `U=W-C`, `c=C`, and
`b=C-1`, (1.3)--(1.5) give

\[
                    D_U=bs,qquad R_U=b.
\tag{1.6}
\]

Hence the component transitions alone are short by `bs>0`, and internal
upper-q1 completeness is impossible.  A sharp collar bank must provide
`s` new colours and spend one repeat per collar, with no further waste.

For `k=2r-1`,

\[
 c={W\over2r-1}=\operatorname{Cat}_{r-1},\qquad
 {U\over W}={r-1\over r+1},
\tag{1.7}
\]

and direct substitution gives

\[
 D_U=s(c-1)+c-{2W\over r+1},\qquad
 R_U={2W\over r+1}-1.
\tag{1.8}
\]

Since `c~W/(2r)`, the positive term `s(c-1)` dominates the
`Theta(W/r)` correction whenever `s=Theta(sqrt r)`.  Thus the odd
component-internal obstruction is also genuine for all sufficiently large
`r`.

## 2. Collar formula and palette audit

Let `|Q|=r-h`, let the lambda and rho rails be disjoint from one another
and from `Q`, and put

\[
 M_j=Q\cup\lambda_{j+1..h}\cup\rho_{1..j}.
\tag{2.1}
\]

Then

\[
 M_j=M_{j-1}-\{\lambda_j\}+\{\rho_j\},
\tag{2.2}
\]

so `M_0,...,M_h` is a simple Johnson geodesic.  For arbitrary
`q_-,q_+ in Q` and `z notin M_h`, `z!=lambda_h`, set

\[
 P=(Q-\{q_-\})\cup L\cup\{\rho_1\},\qquad
 N=(Q-\{q_+\})\cup R\cup\{z\}.
\tag{2.3}
\]

The two seams are also Johnson edges.  The internal and seam upper colours
are

\[
 U_j=Q\cup\lambda_{j..h}\cup\rho_{1..j},\quad
 P\cup M_0=U_1,
 \quad M_h\cup N=U_*=M_h\cup\{z\}.
\tag{2.4}
\]

The rho-prefix length distinguishes `U_1,...,U_h`.  Only `U_h` among them
contains all of `R`, and `U_h=M_h union {lambda_h}`; hence the condition
`z!=lambda_h` makes `U_*` new.  There are exactly `s=h+1` distinct q1
colours in the `h+2=s+1` transition slots, with the sole repeat being the
left-seam copy of `U_1`.

The lower colours are

\[
 (Q-\{q_-\})\cup L,qquad
 Q\cup\lambda_{j+1..h}\cup\rho_{1..j-1},qquad
 (Q-\{q_+\})\cup R.
\tag{2.5}
\]

Every internal value contains all of `Q`, while the seam values omit
`q_-` and `q_+`, respectively.  Internal rho-prefix lengths distinguish
the internal values, and disjointness of the two rails (with `h>=2`)
distinguishes the two seams.  The endpoint owners are not pivot owners
because each omits a member of `Q`; they are distinct from one another
because `P` contains all `h` lambda labels while `N` contains at most the
single lambda label `z`.  Thus all `s+2` owners and all claimed local
palettes are distinct.

The source realization is literal: preced the lambda singleton state by
`(Q-{q_-}) union {rho_1}`, insert `Q`, and follow the rho singleton state
by `(Q-{q_+}) union {z}`.  Under Theorem 2.4's much stronger size
hypothesis these letters are nonempty; in fact the displayed endpoint
owners already verify the trace windows directly.

## 3. Residual incidence-graph accounting

### 3.1 Even case

In the containment graph between ranks `r` and `r+1` of `[2r]`, owner and
upper degrees are `r` and `r+1`, and the initial edge count is `Wr`.
One complete collar reserves `s+2` owner vertices and `s` distinct upper
vertices.  Therefore, after `t` already selected collars, deletion of
their vertices removes at most

\[
 tA_e,qquad
 A_e=(s+2)r+s(r+1)=(2s+2)r+s
\tag{3.1}
\]

edges.  Double-counting owner-upper incidences only makes this an
overestimate, which is in the safe direction.  If `t<W/(r+1)`, then

\[
\begin{aligned}
 |E(G_t)|
 &>W\left(r-{A_e\over r+1}\right)\\
 &=W\left(r-2s-2+{s+2\over r+1}\right)
 >W(r-2s-2).
\end{aligned}
\tag{3.2}
\]

The two shores contain fewer than `2W` vertices, so their residual average
degree is greater than `r-2s-2`.

### 3.2 Odd case

For `[2r-1]`, the two degrees are `r-1` and `r+1`, the edge count is
`W(r-1)`, and the per-collar deletion bound is

\[
 A_o=(s+2)(r-1)+s(r+1)=2r(s+1)-2.
\tag{3.3}
\]

Using

\[
 {A_o\over2r-1}=s+1+{s-1\over2r-1}
\tag{3.4}
\]

shows that, for `t<W/(2r-1)`,

\[
 |E(G_t)|
 >W\left(r-s-2-{s-1\over2r-1}\right)
 >W(r-s-3).
\tag{3.5}
\]

Again the two shores have fewer than `2W` vertices, so the residual average
degree exceeds `r-s-3`.

### 3.3 Minimum degree

If a graph with fewer than `2W` vertices has more than `Wa` edges, then it
has a nonempty subgraph of minimum degree greater than `a/2`: otherwise
delete vertices of current degree at most `a/2`; if every vertex were
deleted, each edge would be charged once and the original graph would have
at most `aW` edges.

The even residual graph therefore has a subgraph of minimum degree greater
than

\[
 {r-2s-2\over2}\ge s+3,
\tag{3.6}
\]

and the odd residual graph has one of minimum degree greater than

\[
 {r-s-3\over2}>s.
\tag{3.7}
\]

Both inequalities follow from `r>=4s+8`.  This hypothesis also implies
`r-h>=1` and leaves at least `h` exterior labels in either parity, so all
local collar data exist.

## 4. Fresh geodesic inside the residual subgraph

Let `H` be either residual minimum-degree subgraph.  Choose an owner
`M_0`.  At stage `j`, the current owner has the form

\[
 M_{j-1}=(M_0-\{\lambda_1,\ldots,\lambda_{j-1}\})
              \cup\{\rho_1,\ldots,\rho_{j-1}\}.
\tag{4.1}
\]

Among its available upper neighbours, at most `j-1` add one of the
previously deleted original labels.  Therefore an available neighbour

\[
 U_j=M_{j-1}\cup\{\rho_j\},\qquad \rho_j\notin M_0,
\tag{4.2}
\]

exists.  The new rho label is automatically different from every earlier
rho label because those labels are already in `M_{j-1}`.  At `U_1`, all
facets except the one deleting `rho_1` differ from `M_0`; the degree bound
gives two distinct such facets, defining `q_-` and `lambda_1`.

For `j>=2`, the bad facets of `U_j` delete one of its `j` inserted rho
labels or delete the protected label `q_-`.  There are at most `j+1<=s`
of them.  Since the upper degree in `H` is greater than `s`, an available
facet deletes a fresh original label

\[
 \lambda_j\in M_0-
  \{q_-,\lambda_1,\ldots,\lambda_{j-1}\},
\tag{4.3}
\]

and produces `M_j`.  The number of rho labels in `M_j-M_0` is exactly
`j`, so these owners cannot repeat earlier `M_i`; every `M_j` contains
`q_-`, so none equals `P`, which omits it.  Similarly, the form of (4.2)
shows that the upper vertices `U_j` are new.

At `M_h`, only the neighbour which adds `lambda_h` is forbidden.  Choose

\[
 U_*=M_h\cup\{z\},\qquad z\ne\lambda_h.
\tag{4.4}
\]

It cannot equal `U_j` for `j<h` because it contains all of `R`, and cannot
equal `U_h` by (4.4).  At most the `h` rho labels and `z` are outside
`Q`; since the degree of `U_*` is greater than `s=h+1`, an available facet
deletes some `q_+ in Q`, producing `N`.  Every pivot owner contains `q_+`,
so `N` is not one of them.  Finally `N` contains all of `R`, whereas `P`
contains only `rho_1`; `h>=2` makes `P!=N` even if `q_+=q_-` or `z` is a
lambda label.

This proves that one full generalized balanced collar lies in the
residual graph and uses no resource twice.  Deleting its `s+2` owner and
`s` upper vertices makes the induction literal, so there is no ordering or
reuse gap between successive collars.

## 5. Exact iteration counts

The even value

\[
 c={W\over r+1}=\operatorname{Cat}_r
\tag{5.1}
\]

and the odd value

\[
 c={W\over2r-1}=\operatorname{Cat}_{r-1}
\tag{5.2}
\]

are integers.  To construct the required `c-1` collars, apply the preceding
step at `t=0,1,...,c-2`.  Every such `t` satisfies the strict hypotheses
`t<W/(r+1)` in the even case and `t<W/(2r-1)` in the odd case.  Thus the
proof reaches exactly the claimed parity-appropriate bridge count.  (The
edge lower bound happens to remain valid for one further induction step;
the theorem neither needs nor claims that extra collar.)

## 6. Scope of the conclusion

Theorem 2.4 unconditionally gives a Catalan-scale bank with globally
disjoint owner, endpoint-owner, and new upper-q1 resources.  It does not
control cross-collar lower-q1 colours, low-containment-star density, the
ordered endpoint realization by a complementary forest, residence, or any
upper interval wider than q1.  The exact even complement therefore remains
the punctured prescribed-end ordered-four-transversal of Theorem 3.1; the
resource bank proved here does not solve that integral correlation.
