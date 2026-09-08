# A compatible two-adjacent-scale MSW rectangle cube

Date: 2026-07-26

## 0. Outcome

The two adjacent recursive MSW rectangle catalogues do admit a joint exact
Boolean subcube large enough to absorb the worst Catalan overshoot.

The only cross-scale conflict is the suspended three-root pattern

\[
 110010S\;\longleftrightarrow\;101010S
 \;\longleftrightarrow\;101100S.                        \tag{0.1}
\]

The two elementary rectangles share the middle root and modify adjacent
phases.  Applying both precomputed modifications makes the shared path
non-geodesic; this is a genuine `Y`-ownership obstruction.  All such
conflicts form a matching.  Delete one switch from each matching edge.
Every remaining affected phase-edge slab is disjoint, so arbitrary choices
of the remaining switches preserve the full `X`- and `Y`-ownership ledgers
and the rooted ports.

If

\[
 M_r=H_{m,r+1}\Cat_{r-1},\qquad
 M_{r+1}=H_{m,r+2}\Cat_r,                               \tag{0.2}
\]

then the number of deleted conflicts is exactly

\[
 E_r=H_{m,r+2}\Cat_{r-1}.                               \tag{0.3}
\]

The compatible cube therefore has

\[
                         C_r=M_r+M_{r+1}-E_r             \tag{0.4}
\]

bits.  Exact arithmetic gives

\[
                         C_r>{D_r\over4},                \tag{0.5}
\]

where `D_r=H_(m,r)(Cat_r/2-p)` is the certified plateau demand and `r`
is minimal with `Cat_r>=4p`.  Thus the physical conflict deletion still
leaves enough switches for the cardinality tuning theorem.  The Catalan
overshoot and the adjacent-scale compatibility gate are both closed.

What remains is not exact-factor legality or scalar capacity.  It is the
common multidepth four-arm drain theorem: the compatible cube must have a
fractional/product state with small mean `PCap`.

**Corrected subsequent fractional audit.**  The obstruction for the
four-units-per-bit restriction (5.1) applies only to that selected
`L`-bit subcube.  It cannot be propagated to the full compatible cube by
discarding the extra legal variables.  On the full cube put

\[
 B=C_r=M_r+M_{r+1}-E_r.
\]

One hereditary suffix arm of every retained bit is dual-neutral on the
canonical overloaded set, so the correct full-cube fixed-cut residual is

\[
 D_r-3B,
\]

not `D_r-3L`.  It is positive exactly when

\[
 {\Cat_r\over p}>
 \left({1\over2}-{3B\over H_{m,r}\Cat_r}\right)^{-1}
 ={64\over11}+O(r^{-1}+r/m).                           \tag{0.6}
\]

Thus the suffix cut gives a full multidepth obstruction in every fixed
margin regime `Cat_r/p>=64/11+epsilon`, after the sparse two-boundary
remainder is included.  At or below the exact threshold in (0.6) this
witness does not close the route.  The preceding scale `r-1` then has an
isolated distinguished-arm ledger
`(Cat_(r-1),Cat_(r-2))` straddling `p`, but positive-density parent
contexts coalesce onto common ordered suffix arcs.  Its exact packet gain,
the fixed-depth integral suffix flow, and the surviving synchronized
four-arm gate are audited in
`MATH_AUDIT_MSW_FULL_TWO_SCALE_DUAL_AND_PRECEDING_SCALE_20260726.md`.
No bounded-menu closure follows from the tuned-subcube lower bound.

---

## 1. Tree form of the two elementary rectangles

Encode an ordered binary tree by

\[
            N(L,R)\longleftrightarrow 1\,w(L)\,0\,w(R).
                                                                    \tag{1.1}
\]

Let `bullet=N(emptyset,emptyset)`, encoded by `10`.  The scale-`r`
elementary rectangle is the local replacement between the two roots

\[
\begin{aligned}
 A_r(S)&=N(\bullet,S)                  &&\longleftrightarrow1100S,\\
 B_r(S)&=N(\varnothing,N(\varnothing,S))&&\longleftrightarrow1010S,
\end{aligned}                                             \tag{1.2}
\]

where `S in D_(r-1)`.  It changes one path phase after the start of the
size-`r+1` block and the two incident path edges.

At the next scale the roots are

\[
                         A_{r+1}(R)=1100R,qquad
                         B_{r+1}(R)=1010R,               \tag{1.3}
\]

with `R in D_r`.

Two recursion nodes in one tree are disjoint or nested.  A proper subtree
of `A_(r+1)(R)` has size at most `r`.  The root `B_(r+1)(R)` has one
distinguished size-`r+1` child, namely

\[
                         N(\varnothing,R)\longleftrightarrow10R.
                                                                    \tag{1.4}
\]

This child is a side of a scale-`r` rectangle if and only if

\[
                         R=10S,                           \tag{1.5}
\]

in which case `10R=1010S=B_r(S)`.  It can never equal `A_r(S)`, whose
word starts with `11`.

### Lemma 1.1 (complete cross-scale overlap classification)

A scale-`r` affected slab and a scale-`r+1` affected slab overlap in one
row if and only if, after a common one-hole context is suppressed, their
three roots are exactly

\[
 X=110010S,qquad Y=101010S,qquad Z=101100S,             \tag{1.6}
\]

with the large rectangle `X<->Y` and the small rectangle `Y<->Z`.
Their modified phases are adjacent.  Every elementary switch belongs to
at most one such cross-scale pair.

#### Proof

Disjoint recursion nodes have disjoint phase blocks.  If the nodes are
nested, their sizes differ by one, so the smaller is a size-`r+1` child
of the larger.  Equations (1.3)--(1.5) show that this occurs only on the
`B` side with `R=10S`, producing (1.6).  The child starts one pair-position
after the larger root; both rectangles modify the phase one step after
their own starts, so the phases are adjacent.

Conversely (1.6) visibly contains the nested `B_r(S)` child.  A tree node
has a unique parent.  Only the `B_r(S)` row, not the `A_r(S)` row, can be
the child (1.4), so the conflict has degree one on both sides.  \(\square\)

---

## 2. The local commutator is not a legal path factor

The obstruction can be checked at `S=emptyset` and then suspended through
an arbitrary common context.  On the five `D_3` roots, use the canonical
MSW paths

\[
\begin{array}{c|c}
110010&125-145-345-346\\
101010&135-235-245-246\\
101100&134-234-236-256.
\end{array}                                               \tag{2.1}
\]

The first rectangle, induced by the coordinate swap `(2 3)`, changes the
shared `101010` row to

\[
                         135-145-245-246.                 \tag{2.2}
\]

The second, induced by `(4 5)`, changes it to

\[
                         135-235-236-246.                 \tag{2.3}
\]

Applying both precomputed phase changes would give

\[
                         135-145-236-246.                 \tag{2.4}
\]

But the consecutive middle states `145` and `236` are disjoint, rather
than differing in one coordinate.  Their union has size six, not four.
Thus the required intervening `Y`-vertex does not exist.  Phasewise
`X`-ownership is still merely permuted, but the complete `Y`-incidence
ledger is not a path factor.

Adding a common spectator context preserves the Johnson distance of the
two local states.  Therefore every suspended conflict (1.6) has the same
obstruction.  The two operations have no legal commutator inside the
precomputed equal-length path category; they must not both be retained in
one Boolean cube.

This is exactly the minimal nonlaminar `D_3` crossing previously seen in
the component partitions

\[
 \{110010,101010\},qquad\{101010,101100\}.               \tag{2.5}
\]

---

## 3. Construction of the compatible cube

Let `mathcal E_r` and `mathcal E_(r+1)` be the full literal parent
catalogues.  Form their cross-scale conflict graph using Lemma 1.1.  It is
a matching.  For every matching edge delete either endpoint, and retain
all unmatched switches.  Call the retained family `mathcal C_r`.

### Theorem 3.1 (two-scale exact Boolean cube)

Every subset of `mathcal C_r` can be applied simultaneously to the
canonical MSW factor.  Every outcome is an exact rooted middle path
factor, with complete `X` ownership, complete `Y` ownership, and the same
root-to-complement ports.

#### Proof

Within one scale this is the fixed-scale cube theorem: equal-size tree
nodes are disjoint, and switches sharing a row act in disjoint affected
phase-edge slabs.

Across the two scales, Lemma 1.1 lists every possible overlap of affected
slabs.  One endpoint of each such pair was deleted.  Therefore any two
retained cross-scale switches either use different rows or change disjoint
phase-edge slabs in a common row.  Each local rectangle preserves the two
incident inclusion matchings.  Products on disjoint slabs commute and
preserve those matchings independently.  Hence every global phase ledger,
both `X` and `Y`, remains a perfect ownership ledger.  The rectangles are
interior, so the rooted ports are unchanged.  \(\square\)

This theorem concerns exact factor legality.  At a lower target depth,
two retained switches can still be the opposite boundaries of one long
intersection window, so their histogram effects need not add.  The
nonadditive saturation/rounding theorem was designed for precisely this
situation.

---

## 4. Exact count of conflicts

For every aligned size-`r+2` parent context and every `S in D_(r-1)`,
there is one conflict, obtained by taking `R=10S` in (1.5).  This
parametrization is injective by uniqueness of the parent node.  Therefore

\[
\boxed{
 E_r=H_{m,r+2}\Cat_{r-1}.}                               \tag{4.1}
\]

The compatible cube size is

\[
\boxed{
 C_r=M_r+M_{r+1}-E_r.}                                  \tag{4.2}
\]

Put `a=m-r`.  Using

\[
 \rho_{m,r}={M_r\over H_{m,r}\Cat_r}
 ={a(r+1)\over4(2a-1)(2r-1)},                           \tag{4.3}
\]

one obtains

\[
 {C_r\over M_r}
 =1+{3(a-1)(r-1)\over2(2a-3)(r+1)}.                    \tag{4.4}
\]

The exact comparison with the worst Catalan demand is

\[
\boxed{
 64\rho_{m,r}{C_r\over M_r}-7
 ={(40a-42)r+36a^2-80a+21
   \over(2a-1)(2r-1)(2a-3)}>0}                          \tag{4.5}
\]

for `a>=2`.  To verify (4.5), write

\[
 64\rho_{m,r}{C_r\over M_r}
 ={8a[(7a-9)r+a-3]
   \over(2a-1)(2r-1)(2a-3)}                             \tag{4.6}
\]

and subtract seven.  The numerator in (4.5) is positive already at
`a=2`, where it equals `38r+5`, and increases thereafter.

If `r` is minimal with `d=Cat_r>=4p`, then `d<16p`, and

\[
 {D_r\over4M_r}
 ={1/2-p/d\over4\rho_{m,r}}
 <{7\over64\rho_{m,r}}.                                 \tag{4.7}
\]

Equations (4.5)--(4.7) prove

\[
\boxed{
                         C_r>{D_r\over4}.}               \tag{4.8}
\]

Thus deleting every physical cross-scale conflict still leaves strictly
more than the worst required count.

---

## 5. Tuned saturation through the plateau window

Let `Q=[r,H]`, `c_q=W-N_q`, and assume `c_H<D_r`.  Choose any

\[
 L=\left\lfloor{D_r-c_H\over4}\right\rfloor             \tag{5.1}
\]

bits of the compatible cube.  This is possible by (4.8).  The canonical
plateau theorem gives, for every `q in Q`,

\[
 K_{q,p}(F_{MSW})-c_q
 \ge D_r-c_H\ge4L.                                      \tag{5.2}
\]

Hence the exact scalar saturation defect of this physical `L`-bit cube is

\[
\boxed{
 \sum_{q\in Q}
 \left(4L-[K_{q,p}(F_{MSW})-c_q]\right)_+=0.}           \tag{5.3}
\]

For `H=O(p^(1/4))`, `c_H/W=O(p^(-1/2))`, while
`D_r/W=Theta((log p)^(-3/2))`; thus `c_H=o(D_r)`.

Combining (5.3) with the all-on saturation theorem gives:

### Corollary 5.1 (physical Gaussian-rounding implication)

If some product distribution on this tuned exact cube has

\[
 \sum_{q=r}^{H}
 \bigl(K_{q,p}(\mathbb E\mu_q)-(W-N_q)\bigr)_+=o(W),     \tag{5.4}
\]

then the all-on state of the same cube is an integral exact factor with
`PCap_[r,H]=o(W)`.  No depth-dependent rounding loss remains.

---

## 6. Remaining theorem

The following former gates are now closed for the recursive trade lane:

* exact middle ownership for a two-scale family;
* cross-scale overlap classification;
* the noncommuting adjacent-phase obstruction;
* deletion of all conflicts at only the exact matching cost (4.1);
* sufficient capacity after that deletion;
* scalar tuning and Gaussian-window integral rounding.

The one remaining gate is fractional/dynamic and genuinely four-armed:

> On the tuned compatible cube, find a product mean satisfying (5.4), or
> prove the coherent multidepth weighted-potential dual for such a mean.

The distinguished marked arm alone cannot do this; its intrinsic cap tail
is conserved.  The other three prefix/suffix arms must provide the drain.
