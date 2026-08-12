# Left-anchored variable windows: an exact maximal-shadow theorem

## Status and point of the result

This note proves a sufficient construction theorem.  It does **not** prove
that the required central rows exist for every `k`.

The new point is that, for a left-anchored monotone interval schedule, the
maximal coordinatewise factor has no additional lower-pin obstruction for
consecutive meets.  Once the prescribed central row is factorable, every
consecutive meet whose physical core is nonempty is realized **exactly**.
Consecutive joins are realized exactly as well.  This extends the familiar
fixed-delay erosion identity to the one-switch schedule and, more generally,
to every schedule

\[
 I_i=[i,\rho_i],\qquad \rho_1<\rho_2<\cdots<\rho_M.
\]

Consequently, all bulk meet shadows and all join shadows transfer without a
second pin-labeling problem.  An exact boundary count below then shows that
the maximal factor alone can **never** attain the rank-count length when
`d>=2`: sparse boundary pinning is genuinely necessary.  Thus the theorem is
both a reduction and a no-go result for the tempting maximal-factor shortcut.

The second half of the note proves a general portal-rank obstruction.  It
shows exactly how many shortened portals can rise above the first upper
layer.  This generalizes the `k=11` one-defect theorem to arbitrary `k,r`.

## 1. General left-anchored schedule

Let

\[
 I_i=[i,\rho_i]\subseteq[n],\qquad 1\le i\le M,
\tag{1.1}
\]

where

\[
 i\le \rho_i,\qquad
 \rho_1<\rho_2<\cdots<\rho_M.
\tag{1.2}
\]

Prescribe target sets

\[
 C_1,\ldots,C_M\subseteq[k].
\]

For a coordinate `x`, let

\[
 Z_x=[n]\setminus\bigcup_{i:x\notin C_i}I_i
\tag{1.3}
\]

be its legal physical positions, and define the maximal factor

\[
 A_j^{\max}=\{x:j\in Z_x\}.
\tag{1.4}
\]

Thus every factor realizing the prescribed intervals is coordinatewise
contained in `A^max`.

For a maximal 1-run `[a,b]` in the incidence word

\[
 (1_{x\in C_1},\ldots,1_{x\in C_M}),
\]

use the boundary conventions

\[
 \rho_0=0,
 \qquad
 b=M\Longrightarrow b\text{ has no right zero constraint}.
\]

If `1<a` and `b<M`, the part of `Z_x` that can serve this run is exactly

\[
 K_{a,b}=[\rho_{a-1}+1,b].
\tag{1.5}
\]

For a left-boundary run replace its left endpoint by `1`; for a
right-boundary run replace its right endpoint by `n`.  In particular, an
internal run is realizable exactly when

\[
 \rho_{a-1}+1\le b.
\tag{1.6}
\]

This is the left-anchored specialization of the general interval-stabbing
factorization criterion.

## 2. Exact maximal-shadow theorem

### Theorem 2.1

Assume the row `C_1,...,C_M` is factorable on the intervals (1.1), or
equivalently that every internal coordinate run obeys (1.6).  Then the
maximal factor (1.4) has the following properties.

1. It realizes the central row:

   \[
   \bigcup_{j\in I_i}A_j^{\max}=C_i.
   \tag{2.1}
   \]

2. Let `1<=p<=q<=M`.  If the common physical core

   \[
   J_{p,q}:=\bigcap_{i=p}^qI_i=[q,\rho_p]
   \tag{2.2}
   \]

   is nonempty, then

   \[
   \bigcup_{j=q}^{\rho_p}A_j^{\max}
      =\bigcap_{i=p}^q C_i.
   \tag{2.3}
   \]

3. The union of the physical central intervals is the ordinary interval

   \[
   H_{p,q}:=\bigcup_{i=p}^qI_i=[p,\rho_q],
   \tag{2.4}
   \]

   and

   \[
   \bigcup_{j=p}^{\rho_q}A_j
      =\bigcup_{i=p}^q C_i.
   \tag{2.5}
   \]

   Here (2.5) holds for **every** factor `A` realizing the central row, not
   only for the maximal factor.

Hence the complete consecutive-intersection and consecutive-union triangles
of the prescribed row are literal contiguous-subarray ORs of one common
factor wherever the intersection core is nonempty.

### Proof

Statement (2.1) is the standard maximal-factor consequence of (1.6).  For
completeness, fix a coordinate `x` and a positive run `[a,b]`.  Its legal
component is (1.5), with the stated boundary modifications.  Condition
(1.6) says that this component meets every `I_i`, `a<=i<=b`.  Thus every
positive target sees `x`, and a negative target sees none because all of its
positions were deleted in (1.3).

Now fix `p<=q` with `q<=rho_p`.  If `x` is absent from one of
`C_p,...,C_q`, every position of the common core `J_(p,q)` lies in that
negative target interval, so it is excluded from `Z_x`.  Hence the left side
of (2.3) omits `x`.

Conversely, suppose `x` lies in every `C_p,...,C_q`, and let `[a,b]` be the
positive run containing this block.  Then

\[
 a\le p\le q\le b.
\]

For an internal run, its legal component is
`K=[rho_(a-1)+1,b]`.  Strict increase of the right endpoints gives

\[
 \rho_{a-1}+1\le\rho_p,
\]

while `q<=b`.  Factorability gives the remaining cross inequality
`rho_(a-1)+1<=b`, and nonemptiness of the core gives `q<=rho_p`.
Therefore

\[
 [\rho_{a-1}+1,b]\cap[q,\rho_p]\ne\varnothing.
\]

The boundary-run versions are easier.  Thus some legal occurrence of `x`
lies in `J_(p,q)`, proving (2.3).

Finally, consecutive integer intervals whose left endpoints advance by one
have no gap, so (2.4) follows from (1.2).  Each `I_i` is contained in
`H_(p,q)`, and central realization gives the inclusion from right to left in
(2.5).  In the other direction, every physical position of `H_(p,q)` lies
in at least one `I_i`, `p<=i<=q`.  In every factor realizing `C_i`, an entry
at such a position is contained in `C_i`; otherwise that central interval
would be contaminated.  No extra coordinate can therefore appear.  This
proves (2.5) for arbitrary factors.  ∎

## 3. The exact single-switch corollary

Let

\[
 M=\binom kr,qquad n=M+d,qquad0\le\sigma\le M,
\]

and use the one-switch schedule

\[
 I_i=\begin{cases}
 [i,i+d-1],&i\le\sigma,\\
 [i,i+d],&i>\sigma.
 \end{cases}
\tag{3.1}
\]

The right endpoints are strictly increasing.  The factorability condition in
Theorem 2.1 becomes the exact mixed-delay rule

\[
 |[a,b]|\ge
 \begin{cases}
 d,&a\le\sigma+1,\\
 d+1,&a\ge\sigma+2
 \end{cases}
\tag{3.2}
\]

for every internal coordinate 1-run.  Boundary runs remain unrestricted.

The feasible consecutive meet depths are explicit.  A block beginning at
`p` has a nonempty core precisely when

\[
 q-p\le
 \begin{cases}
 d-1,&p\le\sigma,\\
 d,&p>\sigma.
 \end{cases}
\tag{3.3}

### Corollary 3.1 (single-switch maximal-shadow construction)

Suppose `C_1,...,C_M` is a permutation of the rank-`r` layer and satisfies
(3.2).  Assume:

* every nonempty set of rank below `r` occurs as a consecutive intersection
  `C_p intersect ... intersect C_q` satisfying (3.3); and
* every set of rank above `r` occurs as a consecutive union
  `C_p union ... union C_q`.

Then the maximal factor (1.4) covers every nonempty subset of `[k]` by a
contiguous OR and has `M+d` positions before deletion of possible empty
entries.

If `M+d=B(k)`, deleting empty entries and applying the proved lower bound
forces the resulting length to remain `B(k)`.  Hence it is an optimal
nonzero word and

\[
 \nu(k)=B(k).
\]

### Why this is weaker than the saturated-braid conjecture

Corollary 3.1 does **not** require all short windows to have distinct values,
nor does it require every short cell to be assigned in advance.  It asks only
for coverage by the consecutive meet triangle.  In exchange, it uses the
coordinatewise maximal factor, which is more restrictive than allowing an
arbitrary sparse pinning.  Thus it is a genuine sufficient route, not a
necessary normal form.

The main all-dimensional construction problem has been reduced to one row:

> Find a permutation of one Boolean layer obeying the asymmetric run rule
> (3.2), complete feasible consecutive meets below it, and complete
> consecutive joins above it.

Once such a row is found, both pin survival and upper-witness preservation
are automatic by Theorem 2.1.

There is, however, an exact arithmetic warning: at the rank-count length,
the nontrivial meet cores alone are always short by a quadratic boundary
term.  The following proposition identifies that term and repairs the
sufficient theorem.

### Proposition 3.2 (the exact boundary reservoir)

Assume

\[
 0\le\sigma\le M-d
\tag{3.4}
\]

and that `sigma` is the arithmetic defect

\[
 \sigma=dM+\binom{d+1}{2}-L,
 \qquad
 L=\sum_{s=1}^{r-1}\binom ks.
\tag{3.5}
\]

The number of nontrivial feasible meet cores `J_(p,q)`, `p<q`, is

\[
 N_{\rm meet}
 =dM-\sigma-\binom{d+1}{2}
 =L-d(d+1).
\tag{3.6}
\]

Moreover, the physical short intervals of lengths at most `d` split into
three disjoint classes:

1. the `sigma` shortened central intervals `I_1,...,I_sigma`;
2. the `N_meet` nontrivial meet cores; and
3. a boundary reservoir `mathcal R` of exactly

   \[
   |\mathcal R|=d(d+1)
   \tag{3.7}
   \]

   cells.

The reservoir has a concrete description.  Half of it consists of all short
intervals whose right endpoint lies in

\[
 \{1,2,\ldots,d-1,\ \sigma+d\};
\tag{3.8}
\]

the other half consists of all intervals contained in the terminal `d`
positions

\[
 [M+1,M+d].
\tag{3.9}
\]

Each half has `binomial(d+1,2)` cells.

#### Proof

For `p<=sigma`, a nontrivial meet block beginning at `p` has one of the
`d-1` lengths `2,...,d`.  Condition (3.4) prevents right-boundary
truncation.  For `sigma<p<=M-d`, it has `d` possible nontrivial lengths.
For the final `d` starting positions, the numbers are
`d-1,d-2,...,0`.  Therefore

\[
\begin{aligned}
 N_{\rm meet}
 &=\sigma(d-1)+(M-d-\sigma)d+\binom d2\\
 &=dM-\sigma-\binom{d+1}{2}.
\end{aligned}
\]

Substitution of (3.5) gives the second equality in (3.6).

There are `dM+binomial(d+1,2)=L+sigma` physical short intervals in total.
After deleting the `sigma` shortened central cells and the `N_meet` cores,
the remainder has size `d(d+1)`.

For the geometric description, the central right endpoints are

\[
 d,d+1,\ldots,\sigma+d-1,
 \quad
 \sigma+d+1,\ldots,M+d.
\]

The omitted left/switch endpoint columns in (3.8) contain

\[
 \binom d2+d=\binom{d+1}{2}
\]

short cells.  At the right boundary, a putative meet core would have left
index `q>M`; these are exactly the intervals contained in (3.9), again
numbering `binomial(d+1,2)`.  Every other short cell has the unique form
`[q,rho_p]` for a feasible central block, or is one of the shortened central
cells.  This proves the partition.  ∎

Proposition 3.2 shows that the literal hypothesis of Corollary 3.1 is too
strong at equality: nontrivial central meets can cover at most
`L-d(d+1)` of the `L` lower masks.  Exactly `d(d+1)` lower masks must use
the boundary reservoir.

For the two live finite schedules this reservoir is tiny and explicit.

* At `k=11`, `(M,d,sigma)=(462,3,369)`.  The twelve cells are

  \[
  [1,1],[1,2],[2,2],
  \quad[370,372],[371,372],[372,372],
  \quad\{[u,v]:463\le u\le v\le465\}.
  \tag{3.9a}
  \]

* At `k=14`, `(M,d,sigma)=(3432,2,392)`.  The six cells are

  \[
  [1,1],
  \quad[393,394],[394,394],
  \quad[3433,3433],[3433,3434],[3434,3434].
  \tag{3.9b}
  \]

### Corollary 3.3 (corrected rank-count construction theorem)

Under (3.4)--(3.5), let `C_1,...,C_M` be a rank-`r` permutation satisfying
the mixed run rule (3.2), and let `A^max` be its maximal factor.  Suppose:

1. the nontrivial feasible meet cores realize `L-d(d+1)` distinct lower
   masks;
2. the `d(d+1)` reservoir intervals in (3.8)--(3.9) realize exactly the
   remaining lower masks, without collision;
3. the consecutive unions of the central row cover every upper mask.

Then `A^max` is universal.  If `M+d=B(k)`, it is an optimal word and
`nu(k)=B(k)`.

The proof is immediate from Theorem 2.1 and the reservoir partition.  This
is the formal boundary-reservoir form of the sufficient theorem: all bulk
lower pins and all upper witnesses are automatic from one central row, while
the exceptional lower-label problem has size only `d(d+1)=O(d^2)`,
independent of `M`.  The next proposition shows that the **maximal** factor
cannot pass this exceptional gate for `d>=2`.

### Proposition 3.4 (maximal boundary collapse)

For the maximal factor of any factorable row on (3.1), the reservoir in
Proposition 3.2 assumes at most

\[
 (d-1)+d+d=3d-1
\tag{3.10}
\]

distinct OR-values.  Consequently, at the rank-count length it covers at
most

\[
 L-(d-1)^2
\tag{3.11}
\]

distinct lower masks.  In particular, for every `d>=2`, the maximal factor
cannot be universal.

#### Proof

For `1<=t<=d-1`, the central intervals containing physical position `t` are
exactly `I_1,...,I_t`.  Hence

\[
 A_t^{\max}=C_1\cap\cdots\cap C_t.
\tag{3.12}
\]

These sets decrease with `t`.  Therefore every interval `[u,v]` with
`1<=u<=v<=d-1` has OR equal to `A_u^max`.  The entire left triangular part
of the reservoir has at most `d-1` values.

Under (3.4), all central intervals meeting the terminal physical position
`M+s`, `1<=s<=d`, belong to the late regime.  Directly from (3.1),

\[
 A_{M+s}^{\max}
   =\bigcap_{i=M+s-d}^{M}C_i.
\tag{3.13}

These sets increase with `s`.  Thus every interval in the terminal tail
`[M+1,M+d]` has OR equal to the maximal factor entry at its right endpoint.
The terminal triangular reservoir has at most `d` values.

The switch column contributes only its `d` physical cells, hence at most `d`
further values.  This proves (3.10).

There are only `L-d(d+1)` nontrivial meet cores, so even granting them all
distinct lower values and no collision with the reservoir, the total number
of distinct lower masks is at most

\[
 L-d(d+1)+(3d-1)=L-(d-1)^2.
\]

Every lower mask must use a short interval by the rank-count lemma.  For
`d>=2`, at least one lower mask is therefore absent.  ∎

The loss is `1,4,9,...` for delays `2,3,4,...`.  It is a boundary phenomenon,
not a defect in the bulk meet identity.  A successful exact construction
must shrink the maximal factor near the two ends and/or switch so that
nested boundary values separate, while preserving the bulk meet witnesses
and central pins.

### Corollary 3.5 (sparse lower repairs preserve every upper join)

Fix the central row and schedule.  Suppose its consecutive unions cover all
sets above rank `r`.  Then **every** factor realizing that same central row
already covers all those upper sets, by (2.5).  In particular, one may shrink
the maximal factor to separate boundary-reservoir values without rechecking
or preserving individual upper intervals; it is enough to preserve the
central row itself.

Thus the remaining exact pin problem is one-sided:

\[
 \text{sparsify }A^{\max}\text{ to recover the missing lower masks while
 preserving the central intervals.}
\]

Upper-shadow coverage cannot be damaged by such a central-preserving sparse
repair.

### Theorem 3.6 (exact localization of the remaining pin problem)

Assume the hypotheses and notation of Proposition 3.2.  Let the nontrivial
meet cores realize `L-d(d+1)` distinct lower masks, and assign the remaining
`d(d+1)` lower masks bijectively to the reservoir cells.  Denote the assigned
label of a reservoir cell `K` by `S_K`.

For a coordinate `x`, let `Z_x` be its central legal set (1.3), and put

\[
 Z'_x=Z_x\setminus
       \bigcup_{K\in\mathcal R:\ x\notin S_K}K.
\tag{3.14}
\]

Then the central row, all selected meet-core labels, and all reservoir labels
are simultaneously realized if and only if the following positive-pin
conditions hold:

\[
\begin{array}{ll}
 I_i\cap Z'_x\ne\varnothing,
   &x\in C_i,\\[1mm]
 J_{p,q}\cap Z'_x\ne\varnothing,
   &x\in C_p\cap\cdots\cap C_q
     \quad\text{for every selected meet core},\\[1mm]
 K\cap Z'_x\ne\varnothing,
   &x\in S_K
     \quad\text{for every reservoir cell}.
\end{array}
\tag{3.15}
\]

When (3.15) holds, one may simply take

\[
 A'_j=\{x:j\in Z'_x\}.
\tag{3.16}
\]

If the central consecutive unions cover the upper ideal, this `A'` is a
universal optimal word at length `B(k)`.

Moreover, (3.15) is a genuinely local test.  Define

\[
 \Omega=[1,d-1]\ \cup\ [\sigma+1,\sigma+d]\
          \cup\ [M+1,M+d].
\tag{3.17}
\]

Then

\[
 |\Omega|\le3d-1,
\tag{3.18}
\]

and `Z'_x` differs from `Z_x` only inside `Omega`.  Hence every central or
meet-core condition already having a legal pin outside `Omega` survives
automatically.  Only `O(d)` central intervals and `O(d^2)` meet cores, those
intersecting the three zones in (3.17), can require a new check.  The size of
the residual pin instance is therefore `O(kd^2)`, independent of the middle
layer size `M`.

#### Proof

Reservoir intervals are the only newly assigned intervals not already
realized as central targets or exact maximal meet cores.  A reservoir label
omitting `x` forbids `x` precisely on that physical interval, which gives
(3.14).  Negative constraints from a meet-core label are redundant: if
`x` is absent from the intersection `C_p cap ... cap C_q`, one central target
in the block already excludes `x` from every position of the common core.

After all negative constraints have been imposed, the coordinatewise
interval-stabbing theorem says exactly that every interval whose label
contains `x` must retain a point of `Z'_x`.  These are the three lines of
(3.15).  Coordinates are independent, so (3.16) realizes every prescribed
label simultaneously.  Corollary 3.5 then supplies every upper target.

Every reservoir interval is contained in one of the three zones in (3.17),
so (3.18) and the support claim follow.  A central interval has length at
most `d+1`, and a meet core has length at most `d`.  Only `O(d)` such central
intervals and `O(d^2)` such short intervals can intersect a union of three
`O(d)` zones.  All other positive-pin conditions are unchanged from the
factorable maximal row and therefore already hold.  ∎

Theorem 3.6 is the precise noncomputational payoff of the slack split.  It
does not prove that a valid reservoir assignment always exists, but it shows
that its pin obstruction is a bounded boundary problem rather than a global
`k times M` labeling problem.

## 4. A general portal-rank obstruction under short-band saturation

The preceding sufficient theorem deliberately drops short-band
distinctness.  If one retains the stronger saturated-braid clauses, a sharp
general rigidity theorem holds.

Assume `d>=2`, `0<=sigma<=M`, and that:

1. all physical windows of lengths at most `d` have distinct OR-values;
2. those values are exactly every nonempty mask of rank below `r`, together
   with `sigma` rank-`r` masks; and
3. the latter masks are

   \[
   P_i=R_d(i),\qquad1\le i\le\sigma.
   \tag{4.1}
   \]

Put

\[
 \mathcal F=
 \{R_{d-1}(i):1\le i\le\sigma\}
 \mathbin{\dot\cup}
 \{R_d(i):\sigma+1\le i\le M+1\}.
\tag{4.2}
\]

This family has `M+1` physical cells.

### Theorem 4.1 (top-lower-layer localization)

Every rank-`(r-1)` short-window value occurs in `mathcal F`.  Consequently

\[
 \binom{k}{r-1}\le M+1,
\tag{4.3}
\]

and exactly

\[
 \delta:=M+1-\binom{k}{r-1}
\tag{4.4}

cells of `mathcal F` have rank at most `r-2`; every other cell of
`mathcal F` has rank exactly `r-1`.

### Proof

A short cell of length at most `d-2` can be enlarged to a containing
length-`(d-1)` cell.  The larger cell is still a lower mask, and distinctness
makes containment strict.  Hence the smaller cell has rank at most `r-2`.

Consider a length-`(d-1)` cell not among the first `sigma` such cells.  It
can be enlarged to a nonselected length-`d` short cell: enlarge to the right,
except for the final boundary cell, which is enlarged to the left.  The
length-`d` cell is a lower mask, so strictness again bounds the original rank
by `r-2`.

The only remaining noncentral short cells of length `d` are precisely the
second family in (4.2).  Therefore all rank-`(r-1)` values lie in
`mathcal F`.  Since all short values are distinct and every rank-`(r-1)` mask
must occur, (4.3)--(4.4) follow.  ∎

### Theorem 4.2 (portal-height budget)

For `1<=i<sigma`, let

\[
 U_i=R_{d+1}(i)=P_i\cup P_{i+1}.
\]

All but at most `delta` of these internal portals have rank exactly `r+1`.
Indeed, whenever the shared cell `R_(d-1)(i+1)` has rank `r-1`,

\[
 R_{d-1}(i+1)=P_i\cap P_{i+1},
 \qquad |U_i|=r+1.
\tag{4.5}

If, in addition, the remaining central masks are distinct rank-`r` windows
`Q_i=R_(d+1)(i)`, `i>sigma`, the analogous statement holds for adjacent
`Q_i`: among all early and late internal transitions combined, at most
`delta` can rise above rank `r+1`.

### Proof

The shared physical overlap is contained in the intersection of the two
distinct rank-`r` endpoints.  If it has rank `r-1`, the intersection can be
neither smaller nor larger, proving (4.5).  Theorem 4.1 leaves only `delta`
lower-rank candidate overlaps in the entire early/late candidate family. ∎

If all `sigma` portal cells (the `sigma-1` internal cells and the switch
cell) are required to be pairwise distinct strict upper masks, Theorem 4.2
gives the necessary capacity bound

\[
 \boxed{
 \sigma\le \binom{k}{r+1}+\delta+1.
 }
\tag{4.6}

The first term counts possible ordinary rank-`(r+1)` portal values, `delta`
counts exceptional internal heights, and the final `1` is the switch cell.

For odd `k=2m+1` with the upper middle rank `r=m+1`, one has

\[
 \binom{k}{r-1}=\binom kr=M,
 \qquad\delta=1.
\tag{4.7}

Thus the entire saturated band has one and only one top-layer defect, and at
most one internal portal can rise above rank `r+1`.  Any distinct-upper
portal interpretation must satisfy

\[
 \sigma\le\binom{k}{r+1}+2.
\tag{4.8}

This is a general obstruction, not a peculiarity of `k=11`.

For example:

* `k=5,r=3,d=2,sigma=8` violates (4.8), since
  `binomial(5,4)+2=7`;
* `k=11,r=6,d=3,sigma=369` violates it by `37`, since the right side is
  `330+2=332`;
* for the upper-middle `k=23` rank-count term,
  `M=binomial(23,12)=1,352,078`, `d=4`, and
  `sigma=1,214,019`, whereas
  `binomial(23,13)+2=1,144,068`.

These violations do **not** refute Corollary 3.1 or the broad version in
which portal values may repeat and higher masks are delegated to longer
windows.  They rigorously refute the slogan that each unit of arithmetic
slack can be converted into a different immediate upper portal.

## 5. Odd-dimensional middle-level forest forced by saturation

Assume `1<=sigma<M`.  Under (4.7), suppose in addition that the remaining
`M-sigma` rank-`r` masks
are the long central windows

\[
 Q_i=R_{d+1}(i),\qquad\sigma<i\le M.
\]

The `M+1` candidate cells in (4.2) consist of all `M` rank-`(r-1)` masks and
one lower-rank defect.  Before removing that defect, their physical
incidences form two alternating paths:

\[
 E_1-P_1-E_2-P_2-\cdots-E_\sigma-P_\sigma,
\tag{5.1}
\]

and

\[
 H_{\sigma+1}-Q_{\sigma+1}-H_{\sigma+2}-\cdots-Q_M-H_{M+1}.
\tag{5.2}

After deleting the unique defect cell, the genuine rank-`(r-1)`/rank-`r`
incidences form a spanning linear forest in the middle-levels graph.  It has
two components if the defect is an endpoint of (5.1) or (5.2), and three
components if the defect is internal.

This follows just by counting: before deletion (5.1)--(5.2) have `2M+1`
vertices, `2M-1` edges, and two components.  Deleting a candidate vertex of
degree one or two leaves `2M` genuine middle-level vertices and respectively
two or three components.

Hence an odd-dimensional saturated single switch is not an arbitrary central
permutation.  It is a two- or three-component spanning middle-level forest,
plus one lower defect, with the mixed run rule (3.2) and all deeper shadows
still to be satisfied.

## 6. Exact remaining mathematical target

The maximal-shadow theorem removes one formerly separate gate:

\[
 \text{factorable left-anchored central row}
 +\text{ bulk consecutive meets and complete joins}
 +\text{ the }d(d+1)\text{-cell boundary reservoir}
 \Longrightarrow\text{ one common universal factor}.
\]

There is no additional coordinatewise pin conflict for the bulk meet
witnesses before boundary labels are imposed.  After the boundary labels are
imposed, Theorem 3.6 confines the exact residual conflict to `O(kd^2)` local
pin conditions.

What remains unproved is the central-row existence statement.  In the
single-switch geometry it asks for a permutation of the rank-`r` layer that
simultaneously has:

1. the mixed run lower bounds (3.2);
2. `L-d(d+1)` lower masks as distinct feasible consecutive intersections
   with depths (3.3);
3. the remaining `d(d+1)` lower masks on the explicit reservoir
   (3.8)--(3.9), passing the local test (3.15);
4. all upper masks as consecutive unions; and
5. in the saturated odd case, the two-/three-component middle-level forest
   forced by Section 5.

This is the next lemma to attack.  It is strictly stronger than ordinary
middle-level Hamiltonicity but cleaner than a separate central-path search
followed by a global `k times M` lower-pin problem.
