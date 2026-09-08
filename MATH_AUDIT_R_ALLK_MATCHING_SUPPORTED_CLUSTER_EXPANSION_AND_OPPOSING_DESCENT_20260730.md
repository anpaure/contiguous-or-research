# Independent audit: matching-supported cluster expansion, injection measures, and PBBS stable banks

Date: 2026-07-30  
Audited file:
`MATH_THEOREM_R_ALLK_MATCHING_SUPPORTED_CLUSTER_EXPANSION_AND_OPPOSING_DESCENT_20260730.md`  
Method: three independent hand audits plus a final line-by-line reconciliation.
No finite search, SAT, web access, or remote computation was used.

## 1. Verdict

The abstract matching, alteration, permanent-minor, complete-injection,
cluster, and deterministic-descent theorems are **valid with the scopes now
stated**.  The PBBS application remains conditional.  In particular, the
report does **not** prove `nu(k)<=B(k)+O(k)`.

The decisive corrected boundary is:

1. Lu--Szekely applies to uniform injections in a complete common cylinder.
2. It does not survive arbitrary target-specific list conditioning or
   arbitrary edge weights.
3. In a list graph the exact replacement is a spread capacitated matching,
   a permanent-minor/conditional-marginal distortion bound on every relevant
   conflict, and an `O(k)` bound for the complete all-arity weighted conflict
   polynomial.
4. Existing PBBS results prove none of those three quantitative properties
   after the same physical unit closure.

## 2. Weighted matching identities

**Verdict: valid.**

For a weighted bipartite graph `G`, structurally zero edges must first be
removed.  If `F` is an extendable partial matching, fixing `F` leaves exactly
the saturating matchings of `G\ominus F`; hence

\[
 \Pr(F\subseteq M)={a(F)Z_{G\ominus F}\over Z_G},
 \qquad
 x_e={a_eZ_{G\ominus e}\over Z_G}.
\]

Cancellation gives the displayed permanent-minor ratio.  The sequential
identity is just the chain rule in the endpoint-deleted graphs.  No
independence or negative association is used.

The maximum-entropy statement is valid precisely for a point in the
relative interior of the convex hull of saturating-matching incidence
vectors.  The entropy-maximizing distribution is unique; its edge-weight
parameters need not be unique because of affine/gauge relations.  A boundary
point must be treated on its minimal face.

## 3. Spread matching criterion

**Verdict: valid.**

For an edge cap `u`, the flow network with capacities

\[
 s\to L:1,qquad L\to R:u,qquad R\to t:1
\]

has a saturating flow if and only if every cut `A subseteq L`,
`B subseteq R` satisfies

\[
 |B|+u e(A,R\setminus B)\ge |A|.
\]

This is an exact capacitated Hall theorem.  It proves existence of some
spread fractional point, not automatically a relative-interior point.
One must either move to its minimal face or prove strict slack where needed.

The PBBS scalar surplus `sigma+k` checks only one aggregate count.  It does
not imply these cuts, not even the individual degree inequalities obtained
by taking `A={S}` and `B=emptyset`.

## 4. Full-conflict alteration

**Verdict: valid.**

For a matching law, same-target and same-interval conflicts have probability
zero.  If the complete remaining physical conflict family is `mathcal E`,
then

\[
 \mathbb E Z
 =\sum_{E\in\mathcal E}\Pr(E\subseteq M)
 \le\sum_E C_0^{|E|}\prod_{e\in E}x_e.
\]

Some integral matching has at most the floor of this expectation.  Deleting
one target part from every conflict occurring in that matching hits all
remaining minimal conflicts, and literal appending gives the theorem's
length bound.  This proof needs neither Lu--Szekely nor an LLL.

The weighted-link identity

\[
 \Theta=\sum_e x_e\Xi(e)
\]

is exact by double counting.  Since `sum_e x_e=|L|` is exponential, a
constant link bound is not enough for additive `O(k)` alteration; the
weighted average must be `O(k/|L|)`.

## 5. Complete uniform injections

**Verdict: valid.**

For `K_(L,N)` and a size-`j` prescribed partial injection,

\[
 \Pr(F)={1\over(N)_j},\qquad x_e={1\over N},
 \qquad {\Pr(F)\over\prod x_e}={N^j\over(N)_j}.
\]

The bound

\[
 \log {N^j\over(N)_j}
 \le {j(j-1)\over2(N-j+1)}
\]

is correct.  Thus the common per-edge cylinder factor through arity `rho`
may be taken as

\[
 \exp\!\left({\rho-1\over2(N-\rho+1)}\right).
\]

The Lu--Szekely theorem gives a negative-dependency graph joining precisely
incompatible canonical partial injections in this **uniform complete**
space.  The dual domain/range bucket proof is valid: an independent family
inside one resource bucket must use one common alternative edge, and the
resulting cluster independence polynomial is bounded by the product of the
two socket factors for every edge of the event.

## 6. List and weighted counterexamples

**Verdict: valid and decisive.**

The six-cycle list graph has exactly two perfect matchings.  Compatible
canonical edge events chosen from opposite matchings are mutually exclusive,
so

\[
 \Pr(A\mid\overline B)=1>\Pr(A)=1/2.
\]

Therefore list conditioning destroys the Lu--Szekely negative-dependency
graph even in a 2-regular graph.

The weighted complete `3` by `3` matrix in the theorem has permanent
`29/8`; direct enumeration of its six permutation weights gives

\[
 \Pr(11)=\Pr(22)=12/29,quad
 \Pr(11,22)=4/29,quad
 \Pr(11\mid\overline{22})=8/17>12/29.
\]

Thus arbitrary weighted complete injections also fail the same lopsided
claim.  The weighted `K_(2,2)` example correctly shows that maximum entropy
alone does not bound permanent-minor distortion.  It is not claimed to
disprove every stronger marginal-cap theorem.

Adding forbidden mappings as unary events in the complete uniform space is
formally legal.  Under the theorem's chosen activities it forces

\[
 \left(1+{cf_s\over N-1}\right)
 \left(1+{cg_I\over N-1}\right)\le c
\]

at every relevant allowed edge before physical conflicts are charged.  This
is correctly presented as a necessary condition for that particular
dual-bucket certificate, not as a universal impossibility theorem.

## 7. General one-position stable bank

**Verdict: valid after the stated hypotheses were made explicit.**

Let `a=(S,{p})` be a one-position candidate with
`F_p subseteq S subseteq P_p`, `W>=d+2`, and `|S|<=c_0-2`.  In the one-sided
`d+2` stable corridor choose `y in C\setminus S` and

\[
 U=C\setminus(S\cup\{y\}).
\]

At the anchor endpoint, `(U union {y}) cap F_p=emptyset` follows from
`F_p subseteq S`; at every other block boundary it follows because those
coordinates lie in both neighboring erosion states.  Hence
`(U union {y}) cap F(J)=emptyset`.  The labels

\[
 R_h=F(J_h)\cup Z_h
\]

for ordered distinct nonempty `Z_h subseteq U` are valid, strict, pairwise
distinct, and different from `S`.  All labels omit `y`, and the intervals
partition a `d+1` window, so the full family violates its `y` row.

Every proper subfamily occupies at most `d` positions.  The exact
run-component/positive-guard normal form from handoff item 1986 proves it
compatible: no deletion component can exceed `d`, and disjoint candidate
intervals preserve every selected positive guard.  Thus the count

\[
 (2^{|U|}-1)_{j-1}
\]

is correct.  In particular, singleton omission does not remove analogous
banks around retained low-rank one-position candidates.

This proof uses the certified cores
`F_p=(P_p\setminus P_(p-1)) union (P_p\setminus P_(p+1))` with the stated
endpoint convention.  It does not license arbitrary enlarged cores.

## 8. Stable-composition generating function

**Verdict: valid.**

For a fixed chart and ordered composition
`ell_1+...+ell_t=d`, the cylinder bound and socket sums give

\[
 C_0x_a\prod_h(C_0\lambda_{\ell_h}).
\]

Summing all positive ordered compositions is exactly

\[
 C_0x_a[z^d]{A(z)\over1-A(z)}.
\]

After at most `R_*` charts per anchor and total anchor mass `X_1`, this is
the theorem's bound.  If all socket masses are at most `lambda`, the exact
coefficient is

\[
 \sum_{t=1}^d(C_0\lambda)^t{d-1\choose t-1}
 =C_0\lambda(1+C_0\lambda)^{d-1}.
\]

The series is formal; no analytic convergence assumption is needed.
The bound `R_*<=2k` is valid when a chart is fixed by anchor, direction,
and omitted stable coordinate, as in the stated construction.

The length-one marginal lower bound is valid only under its explicit
reservation hypotheses: all `W` forced facet columns are longer than one,
there are no other omissions, and a residual matching saturates every
remaining target.  If `f_1` forced columns have length one, subtract `f_1`
from the displayed right side.  The theorem now records this caveat.

## 9. Final implication boundary

Combining the valid statements yields the following conditional theorem.
In one upper-complete, deadline-resident physical chronology, if after
`O(k)` omissions and exact unit closure:

1. every capacitated Hall cut holds for a spread parameter `u=O(1/M)`;
2. the resulting fractional point has a matching-measure realization;
3. every relevant conflict prefix has bounded conditional marginal
   distortion, equivalently the required permanent-minor ratio; and
4. the complete all-arity weighted conflict polynomial is `O(k)`,

then

\[
                         \nu(k)\le B(k)+O(k).
\]

Items 1977 and 1986 make the native obstruction and the complete run/guard
conflict family explicit, respectively.  They do not prove conditions
1--4 for a common PBBS/Pascal chronology.  This is the precise unproved
boundary.
