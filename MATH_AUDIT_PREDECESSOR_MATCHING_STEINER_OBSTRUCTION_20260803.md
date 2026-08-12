# Audit of the predecessor-matching Steiner obstruction

**Date:** 2026-08-03  
**Audited candidate:**
`MATH_THEOREM_PREDECESSOR_MATCHING_STEINER_OBSTRUCTION_20260803.md`  
**Input SHA-256:**
`f50eacc29a8eb3090e797c852361683c10da71f74536874b40381529229cbeec`  
**Verdict:** **GO**, with one proof-explication patch that does not change
the statement: the exact local `L1 = 2 * missing-image` identity is now
displayed in the quantitative corollary.  The patched theorem SHA-256 is
`218d5bc378dadc166c44bb0e9ca0a74b06c9cb71c20fae6193833a6410167297`.

No computation or finite search was used.

## 1. Matching/occurrence equivalence: PASS

For a predecessor matching `M_0`, every middle set `V` has the unique
lower facet

\[
 q(V)=M_0^{-1}(V),\qquad V=q(V)\cup\{a(V)\}.
\]

For `R` of rank `m+1` and `x in R`, the rooted tail, lower colour, and head
are exactly

\[
 T=R-x,\qquad Q=R-\{x,f_R(x)\},\qquad H=R-f_R(x).
\]

The tails in one colour fibre are automatically distinct.  The heads are
distinct exactly when `f_R` is injective, hence a permutation.  Since
`f_R(x) != x`, every such permutation is a derangement and every rooted
edge is nonloop.

For each `y`,

\[
 L\in\mathcal D_y
 \quad\Longleftrightarrow\quad
 M_0(L)=L\cup\{y\}.
\]

Thus the union of the labelled incidences from all `D_y` is literally
`M_0`, not merely a projection of it.

The converse also passes.  The only subtle step is special to the
parameters `S(b-1,b,2b)`: every `(b+1)`-set contains exactly one block.
The theorem now proves this correctly.  Complements of the blocks form a
second `S(b-1,b,2b)`, because complementary block intersections have the
same sizes and the block count saturates all `(b-1)`-sets.  The complement
of a `(b+1)`-set therefore lies in one complementary block, giving an
original block inside it; uniqueness follows from the intersection bound.
This validates

\[
 \boxed{
 M_0\text{ with all }f_R\text{ permutations}
 \iff
 (\mathcal D_y)_y\text{ are punctured Steiner systems and }
 \mathcal I\text{ is one global perfect matching}.}
\]

The global perfect-matching requirement is essential; independently
existing Steiner systems do not imply it.

## 2. Steiner parameters and divisibility: PASS

If every `f_R` is a permutation, each `m`-set in the punctured
`(2m-2)`-point ground set contains exactly one block of `D_y`.  Two blocks
cannot share an `(m-2)`-subset.  Counting block--`m`-set incidences gives

\[
 |\mathcal D_y|(m-1)=\binom{2m-2}{m}
                    =\binom{2m-2}{m-2}.
\]

Counting `(m-2)`-subsets inside the blocks then saturates the entire
`(m-2)`-layer exactly once.  Hence

\[
 \mathcal D_y\cong S(m-2,m-1,2m-2),
 \qquad
 |\mathcal D_y|=\operatorname{Cat}_{m-1}.
\]

For a fixed `j`-subset, the standard derived-design parameter is

\[
 \lambda_j=
 {\binom{v-j}{t-j}\over\binom{b-j}{t-j}}.
\]

With `ell=t-j`, the substitution is exactly

\[
 A_\ell(m)={1\over\ell+1}\binom{m+\ell}{\ell},
 \qquad0\le\ell\le m-2.
\]

No index or endpoint is missing.

## 3. The iff-prime arithmetic: PASS

The identity

\[
 A_\ell(m)={1\over m}\binom{m+\ell}{\ell+1}
\]

is exact.  If `m` is prime, `0<=ell<=m-2` makes `(ell+1)!` invertible
modulo `m`; the numerator has the factor `m`, so the binomial coefficient
is divisible by `m`.

If `m` is composite, choose a prime divisor `p`.  Since `p<=m/2`,
`ell=p-1` lies in range, while

\[
 \binom{m+p-1}{p-1}
 =\prod_{i=1}^{p-1}{m+i\over i}
 \equiv1\pmod p.
\]

It is not divisible by `p`, so `A_{p-1}(m)` is nonintegral.  Therefore all
standard divisibilities hold iff `m` is prime.  This is only divisibility
admissibility; the theorem makes no design-existence claim for prime `m`.

For `k=17`, `m=9` and

\[
 A_2(9)={1\over3}\binom{11}{2}={55\over3},
\]

so the strong full-fibre local-permutation ansatz is impossible.

## 4. Universal fractional occurrence selector: PASS

Giving every rooted occurrence weight `1/(m+1)` produces:

* load `1` on each upper-colour vertex;
* load `(m-1)/(m+1)` on every tail;
* load `(m-1)/(m+1)` on every head.

For a fixed tail, the `m-1` occurrences are indexed by the exterior roots.
For a fixed head `H`, they are indexed bijectively by the `m-1` lower
facets of `H` other than `q(H)`.  The total unused capacity on either
middle shore is

\[
 {2\over m+1}\binom{2m-1}{m}=\operatorname{Cat}_m.
\]

This is exactly a fractional three-partite selector with the tail and head
roles kept as separate shores.  It supplies no integral rounding,
component control, or Hamilton topology, and the source states that scope
correctly.

## 5. Quantitative composite collision bound: PASS

For

\[
 c_y(T)=\#\{B\in\mathcal D_y:B\subset T\},
\]

the value is exactly the indegree of `y` under `f_{T+y}`.  Every block is
contained in `m-1` punctured `m`-sets, giving

\[
 \sum_T(c_y(T)-1)
 =(m-1)(|\mathcal D_y|-\operatorname{Cat}_{m-1}).
\]

For composite `m`, the vector cannot vanish.  If its signed sum is zero,
its integral `L1` norm is at least two; otherwise the signed sum is a
nonzero multiple of `m-1`, again giving `L1>=2`.  Thus every coordinate
contributes at least two.

For each fixed upper colour `R`, the indegrees of `f_R` sum to `m+1`, so

\[
 \sum_{y\in R}|\deg^-_{f_R}(y)-1|
 =2((m+1)-|\operatorname{im}f_R|).
\]

Summing the coordinate lower bounds therefore gives exactly

\[
 \sum_R((m+1)-|\operatorname{im}f_R|)\ge2m-1.
\]

At `m=9` this is at least `17`.  A fixed-point-free function on ten points
has image size at least two, so one colour contributes at most eight;
there must be at least three locally nonsimple upper colours.

## 6. Core permutations and cyclic reduction: PASS

For every `(m-2)`-core `S`, the unique block of `D_y` through `S` defines

\[
 S\cup\{\phi_S(y)\}\in\mathcal D_y.
\]

The lower-endpoint uniqueness of the global matching gives one preimage of
every value, so `phi_S` is a permutation of `X-S`.  It has no fixed point
because blocks of `D_y` avoid `y`.  A 2-cycle would map two distinct lower
sets to the same middle set `S+{y,z}`, violating upper-endpoint
injectivity.  Hence all cycles have length at least three.  This is a
necessary compatibility consequence, not a converse.

Under rotation equivariance, `D_y=y+D_0`; the two displayed endpoint
conditions are exactly the lower- and upper-perfect-matching conditions
for the orbit incidence set.  They do not assert existence.

## 7. Scope

The theorem excludes only the condition that **every rooted occurrence in
every full upper-colour fibre** be simultaneously tail- and head-simple.
It does not exclude a selector using a proper subfamily, repeated heads in
some fibres, occurrence splitting, later splicing, or the equality
`nu(k)=B(k)`.
