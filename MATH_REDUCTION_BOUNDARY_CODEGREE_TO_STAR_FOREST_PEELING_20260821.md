# A conditional star-forest peeling reduction and its matching counterexample

**Date:** 2026-08-21  
**Status:** the conditional reduction is exact, but its star-forest input
is false.  Proposition 2.1 gives a uniform matching counterexample.  The
full boundary-codegree gate remains open and is not disproved by it.

## 1. Setup

Let `e` be the identity directed punctured configuration, let `D=D_M`, and
let `B(T)` be the boundary graph of a nonempty target family `T subseteq e`.
Every target is one edge of the maximum-degree-four graph `B_r` from
`MATH_REDUCTION_PUNCTURED_BOUNDARY_POLYMER_TO_ANNEALED_REGENERATION_20260821.md`.
For `A in T`, define

\[
 \rho_T(A):={\deg(T)\over\deg(T\setminus\{A\})},\qquad
 h_T(A):=\left|V(A)\setminus V(B(T\setminus\{A\}))\right|.       \tag{1.1}
\]

Thus `h_T(A)` is the number, zero, one, or two, of boundary cuts which
disappear when `A` is removed.  All denominators in (1.1) are positive,
because the base configuration itself contains every subfamily of `e`.

The desired boundary-codegree inequality is

\[
 {\deg(T)\over D}\le C^{|T|}r^{2-|V(B(T))|}.                    \tag{1.2}
\]

## 2. The reduced gate

> **Disproved star-forest peeling gate `SP(C)`.**  There is an absolute constant `C`
> such that every star forest `B(T)` with `|T|>=2` contains an edge `A`
> satisfying
> \[
>                         \rho_T(A)\le C r^{-h_T(A)}.             \tag{2.1}
> \]
> Equivalently, one may state the only two nontrivial cases explicitly:
> a leaf edge in a component with at least two edges may be peeled at cost
> `C/r`, or an isolated edge may be peeled at cost `C/r^2`:
> \[
> \begin{array}{c|c|c}
> \text{edge type}&h_T(A)&\rho_T(A)\\ \hline
> \text{nontrivial-star leaf}&1&\le C/r,\\
> \text{isolated component}&2&\le C/r^2.
> \end{array}                                                   \tag{2.2}
> \]

The assertion is existential: only one correctly priced peel is required
at each star-forest state.  Requiring every forward exposure to have this
price is false even in the exact `r=5` census.

### Proposition 2.1 (a matching defeats every isolated-edge peel)

For `r>=4`, put

\[
                         T_r=\{M_1,M_2,\ldots,M_r\}.             \tag{2.3}
\]

The edges `{i,i+r}`, `1<=i<=r`, are pairwise endpoint-disjoint, so
`B(T_r)` is a matching and `h_{T_r}(A)=2` for every `A in T_r`.  Nevertheless

\[
 \min_{A\in T_r}\rho_{T_r}(A)
   ={r+1\over6(r+2)},
 \qquad
 r^2\min_{A\in T_r}\rho_{T_r}(A)\longrightarrow\infty.         \tag{2.4}
\]

Consequently `SP(C)` is false for every absolute `C`.

#### Proof

The labelled Venn cells of the `r` consecutive middle windows have sizes
`2,1` and `2(r-1)` further singleton cells.  Their positional starts must
form a block of `r` consecutive cuts, in either orientation: indeed,
`|M_i intersect M_j|=r-|i-j|` fixes every cyclic start distance, and the
adjacent signs must agree to avoid repeating a start.  Exactly
`b-r=r+1` translations in each orientation avoid the punctured start.
The exact Venn-cell formula therefore gives

\[
                         \deg(T_r)=2(r+1)\,2!=4(r+1).             \tag{2.5}
\]

Deleting an endpoint window leaves `r-1` consecutive starts.  Its two
large Venn cells have sizes `3,2`, all others being singletons, and there
are `2(b-r+1)=2(r+2)` retained placements.  Thus

\[
             \deg(T_r\setminus\{M_1\})
              =\deg(T_r\setminus\{M_r\})
              =2(r+2)\,3!\,2!=24(r+2).                         \tag{2.6}
\]

If `2<=j<=r-1`, deleting `M_j` merges two pairs of singleton Venn cells.
The Venn product is `2!2!2!=8`, and the start metric is the same block with
one internal gap, again with `2(r+2)` retained placements.  Hence

\[
             \deg(T_r\setminus\{M_j\})=16(r+2).                 \tag{2.7}
\]

Endpoint deletion minimizes the ratio, and (2.5)--(2.7) prove (2.4).
\(\square\)

This family does **not** disprove the full boundary gate (1.2).  Here
`|T_r|=r`, `|V(B(T_r))|=2r`, and

\[
 \left(r^{2r-2}{\deg(T_r)\over D_M}\right)^{1/r}
  =\left({2r^{2r-3}\over(r!)^2}\right)^{1/r}
  \longrightarrow e^2.                                          \tag{2.8}
\]

It only shows that a valid global `C^|T|` bound cannot in general be
factored into pointwise `C/r^2` isolated-edge peels.

## 3. Exact reduction

### Theorem 3.1 (conditional algebra)

If `SP(C)` were true, it would imply the boundary-codegree gate (1.2), with
`C` replaced by `max(C,2)` if necessary.

#### Proof

Suppose first that `B(T)` has an edge `A` both of whose endpoints have
degree at least two.  Then `h_T(A)=0`; moreover containment of target
families gives

\[
                         \rho_T(A)\le1.                          \tag{3.1}
\]

Otherwise every edge of `B(T)` has a degree-one endpoint.  Each connected
component is then a star: if a component had two vertices of degree at
least two, the unique path between the first two such vertices would
contain an edge with no degree-one endpoint.  Hence `B(T)` is a star
forest, and `SP(C)` supplies an edge satisfying (2.1).

Put `C_0=max(C,2)`.  Since `SP(C)` implies `SP(C_0)`, starting with `T`
we may repeatedly use (3.1) when available and `SP(C_0)` otherwise, until
one target remains.  Write the successive removed edges as
`A_s,...,A_2`, where `s=|T|`.  Boundary vertices disappear exactly once,
so

\[
                    \sum_{j=2}^s h_{T_j}(A_j)
                       =|V(B(T))|-2.                            \tag{3.2}
\]

The last one-target degree is either `D_M=D` or
`D_L=((r+2)/r)D<=2D`.  Telescoping the codegrees and using (2.1), (3.1),
and (3.2) gives

\[
 {\deg(T)\over D}
 \le2 C_0^{s-1}r^{-\sum_j h_{T_j}(A_j)}
 \le C_0^s r^{2-|V(B(T))|},                            \tag{3.3}
\]

which is (1.2).  \(\square\)

## 4. What the finite diagnostic was seeing

The graph `B_r` has maximum degree four, so each nontrivial star has at most
four edges.  Proposition 2.1 shows that many mutually boundary-disjoint
components can nevertheless lock their cyclic placements globally.  That
global correlation is exactly what the pointwise peeling price misses.

The exact star-peeling diagnostic

`scratch/research_punctured_boundary_star_peeling_gate_20260821.cpp`

enumerates all subfamilies after an exact zeta transform of all directed
words.  For `r=3,4,5`, the largest value of the *best* scaled peel
`min_A rho_T(A) r^{h_T(A)}`, maximized over all `T`, is respectively

\[
                         3,\qquad 2.8,\qquad 25/7.                \tag{4.1}
\]

A separate full-subset diagnostic,
`scratch/research_punctured_boundary_codegree_gate_20260821.cpp`, verifies
the full boundary gate with required root constants below
`2.24,2.13,2.16`, respectively.  These values are exact finite evidence
only.  At `r=5`, the worst star-peeling mask is exactly
`T_5={M_1,...,M_5}` and its value `25/7` is the first visible term of the
divergence (2.4).  The bounded full-gate constants are consistent with
(2.8).

## 5. Remaining analytic form

Theorem 3.1 remains a correct conditional implication but is unusable,
because its hypothesis fails on (2.3).  A proof of the full boundary gate
must retain an aggregate `C^{|T|}` budget across correlated components,
rather than insist that each disappearing boundary cut can be paid for by
one reverse conditional probability.  Equivalently, the remaining target
is a global Venn-factorial or entropy inequality for `deg(T)`, not a
pointwise star peel.
