# Exact regularity and codegrees of the central resident rail hypergraph

**Date:** 2026-08-13  
**Status:** unconditional exact owner-hypergraph theorem and exact
multiple-choice factor formulation.  It proves an exact fractional perfect
matching and the sharp pair-codegree scale.  It does not invoke a
fixed-uniformity nibble diagonally when the rank grows.

## 1. The parameterized central rail hypergraph

Put

\[
 q=d+1,\qquad c=R-q,\qquad r=2q+1,
 \qquad W={k\choose R}.                              \tag{1.1}
\]

Assume `q>=2`, `c>=0`, and `k-R>=q+1`, so that the following choices
exist.  The vertices of `H_cent` are the named owners

\[
 \mathcal V={ [k]\choose R}.                         \tag{1.2}
\]

A parameterized hyperedge consists of

* a core `C`, `|C|=c`;
* a toggle set `T subset [k]\setminus C`, `|T|=r`; and
* a directed cyclic order `sigma` on `T`, modulo rotation.

Its owner support is

\[
 E(C,T,\sigma)=
 \left\{
 C\cup\{\sigma_i,\sigma_{i+1},\ldots,\sigma_{i+q-1}\}:
 i\in\mathbb Z_r
 \right\}.                                          \tag{1.3}
\]

Parallel parameterized edges with the same support are retained.  They do
not change the possible matchings and make every orbit count literal.
Every edge has exactly `r` distinct owners.  By the period-`2q+1`
residence theorem, it is a simple, closed, biresident pure rail with both
immediate palettes and every proper interval row simple.

## 2. Exact vertex degree

### Theorem 2.1

`H_cent` is exactly `D`-regular, where

\[
 \boxed{
 D={R\choose q}{k-R\choose q+1}q!(q+1)! .}
                                                            \tag{2.1}
\]

Equivalently,

\[
 \boxed{D=(R)_q(k-R)_{q+1}.}                            \tag{2.1a}
\]

#### Proof

Fix an owner `A`.  If `A` occurs in a rail, its core is obtained by
choosing the `q` petal labels of `A`, so there are `binom(R,q)` choices of
`C`.  The toggle set must contain the petal `P=A\setminus C` and has
`q+1` additional labels outside `A`, giving `binom(k-R,q+1)` choices of
`T`.

For fixed `P subset T`, the number of directed cyclic orders modulo
rotation in which `P` is a cyclic interval is

\[
 q!(q+1)! .                                           \tag{2.2}
\]

Indeed, contract `P` to one cyclic block.  The block and the `q+1`
remaining points have `(q+1)!` cyclic orders, and the labels within `P`
have `q!` linear orders.  Multiplication gives (2.1).  `square`

Equivalently, the total number of parameterized edges is

\[
 |\mathcal E|
 ={k\choose c}{k-c\choose r}(r-1)!,                  \tag{2.3}
\]

and the identity `r|E|=WD` follows by double counting incidences.

## 3. Exact owner-pair codegrees

For owners `A,B`, put

\[
 t=R-|A\cap B|,
\]

their Johnson distance.

### Theorem 3.1

If `1<=t<=q`, the codegree is

\[
 \boxed{
 \lambda_t
 ={R-t\choose q-t}{k-R-t\choose q+1-t}
   2(q-t)!(t!)^2(q+1-t)! .}                           \tag{3.1}
\]

Equivalently,

\[
 \boxed{
 {\lambda_t\over D}
 ={2(t!)^2\over (R)_t(k-R)_t}.}                       \tag{3.2}
\]

If `t>q`, the codegree is zero.

#### Proof

Both owners contain the core, so `C subset A\cap B`.  Conversely, once
`C` is chosen, their two petals are `P=A\setminus C` and
`Q=B\setminus C`.  Thus there are

\[
 {R-t\choose c}={R-t\choose q-t}                     \tag{3.3}
\]

possible cores.  The union `P\cup Q` has size `q+t`, so a central toggle
set containing it needs `q+1-t` further labels outside `A\cup B`; there
are

\[
 {k-R-t\choose q+1-t}                                \tag{3.4}
\]

choices.

It remains to count cyclic orders of `T` in which both `P` and `Q` are
`q`-intervals.  Their intersection, their two differences, and the
outside of their union have sizes

\[
 q-t,\quad t,\quad t,\quad q+1-t.                    \tag{3.5}
\]

Two proper `q`-arcs in a directed `(2q+1)`-cycle whose symmetric
difference has size `2t` can occur in two relative orientations.  After
choosing one, each of the four displayed blocks is consecutive; their
internal orders are arbitrary.  Hence the exact order count is

\[
 2(q-t)!(t!)^2(q+1-t)!.                              \tag{3.6}
\]

Multiplying (3.3), (3.4), and (3.6) proves (3.1).  Dividing by (2.1)
and cancelling falling factorials proves (3.2).  If `t>q`, no common
`c`-core exists and the codegree is zero.  `square`

### Corollary 3.2 (maximum pair codegree)

If

\[
 (t+1)^2<(R-t)(k-R-t)\qquad(1\le t<q),               \tag{3.7}
\]

then the ratios in (3.2) strictly decrease with `t`.  In particular, in
the central regime `R,k-R >> q`,

\[
 \boxed{
 {\Delta_2\over D}={2\over R(k-R)}=\Theta(k^{-2}).}  \tag{3.8}
\]

Indeed,

\[
 {\lambda_{t+1}\over\lambda_t}
 ={(t+1)^2\over(R-t)(k-R-t)}.                         \tag{3.9}
\]

Since `r=2q+1=Theta(sqrt(k))` in the target regime,

\[
 \boxed{
 r^2{\Delta_2\over D}
 ={2(2q+1)^2\over R(k-R)}=O(k^{-1}).}                \tag{3.10}
\]

This is the exact collision parameter, not an asymptotic orbit heuristic.

## 4. Exact fractional and integral factor equations

Introduce one binary variable for every parameterized central rail:

\[
 x_{C,T,\sigma}\in\{0,1\}.                           \tag{4.1}
\]

An exact central-rail owner factor is precisely a solution of

\[
 \boxed{
 \sum_{\substack{C\subset A,\ |C|=c\\
                  T\supset A\setminus C,\ |T|=r\\
                  A\setminus C\text{ is a }q\text{-window of }\sigma}}
 x_{C,T,\sigma}=1
 \quad\text{for every }A\in{[k]\choose R}.}         \tag{4.2}
\]

There are no additional owner-overlap constraints: equations (4.2) say
exactly that every owner lies in one selected edge, hence selected rail
supports are pairwise disjoint.

Regularity gives the exact fractional solution

\[
 \boxed{x_{C,T,\sigma}=1/D}                           \tag{4.3}
\]

for every parameterized rail.  Thus the named-owner fractional checkpoint
is exact without choosing shells first.

There is also an exact multiple-choice version.  Given labelled shell
tokens `j` with fixed `(C_j,T_j)`, introduce

\[
 x_{j,\sigma}\in\{0,1\}.
\]

Choosing exactly one cyclic order for every token and partitioning all
owners is equivalent to

\[
 \boxed{
 \sum_{\sigma}x_{j,\sigma}=1\quad(j\in\mathcal J),}  \tag{4.4}
\]

\[
 \boxed{
 \sum_{j,\sigma:
       A\in E(C_j,T_j,\sigma)}x_{j,\sigma}=1
 \quad(A\in{[k]\choose R}).}                        \tag{4.5}
\]

For a fixed shell token, the uniform order distribution gives owner `A`
the load

\[
 {r\over{r\choose q}}
 \mathbf1\{C_j\subset A,\ A\setminus C_j\subset T_j\}.       \tag{4.6}
\]

Consequently the natural fractional point `x_{j,sigma}=1/(r-1)!`
satisfies (4.4), while (4.5) is satisfied exactly if and only if

\[
 \boxed{
 \sum_j {r\over{r\choose q}}
 \mathbf1\{C_j\subset A,\ A\setminus C_j\subset T_j\}=1
 \quad\text{for every named owner }A.}               \tag{4.7}
\]

Equation (4.7), not a point-degree average, is the exact simultaneous
role-flow checkpoint for a frozen multiple-choice shell system.

## 5. Divisibility boundary

Every central rail has exactly `r=2q+1` owners.  Therefore

\[
 \boxed{2q+1\mid W}                                  \tag{5.1}
\]

is necessary for an exact central-only factor.  It is not automatic.  At
`k=17`, for example, `R=9`, `d=3`, `q=4`, and

\[
 W={17\choose9}=24310\equiv1\pmod9.                  \tag{5.2}
\]

Hence no central-only factor exists there, despite exact regularity and
the exact fractional solution.  More generally, any central matching
leaves a number of owners congruent to `W mod (2q+1)`.

This is only a scalar obstruction.  Two consecutive legal periods, for
example `2q+1` and `2q+2`, have gcd one, so a mixed-period architecture can
remove it.  Alternatively a terminal correction must have cardinality
congruent to `W` modulo `2q+1`.  Neither observation supplies the required
positive mixed factor or absorber.

If instead one partitions owners by whole central shells

\[
 \{C\cup Q:Q\in{T\choose q}\},                       \tag{5.3}
\]

the Mütze--Standke--Wiechert theorem factors each shell into
`Cat_q` central rails.  A shell contributes

\[
 {2q+1\choose q}=(2q+1)\operatorname{Cat}_q          \tag{5.4}
\]

owners.  Thus a shell allocation has the stronger scalar and point-degree
divisibilities implicit in (5.4); these are artifacts of grouping rails
into complete shells, not necessary conditions for the individual-rail
system (4.2).

## 6. Nibble boundary with growing uniformity

Equations (3.8)--(3.10) are excellent approximate-matching geometry, but
one must keep theorem quantifiers straight.

The classical Pippenger theorem says that for every **fixed** rank `r`
and error `epsilon>0`, there is a codegree tolerance `mu(r,epsilon)>0`
such that an almost-regular `r`-graph with codegrees at most `mu D` has a
matching leaving at most `epsilon` of its vertices.  This does not permit
substitution of `r=2q+1 -> infinity` unless an explicit lower bound on
`mu(r,epsilon)` is supplied.

Modern quantitative forms show the same issue explicitly.  For example,
the Delcourt--Postle nibble theorem has a parameter

\[
 \beta\le {1\over8r}
\]

and produces a relative leave `D^{-beta/(16r)}`, but its threshold
`D_beta` depends on `r` and `beta` with no cited uniform estimate adequate
for the diagonal sequence here.  Ehard--Glock--Joos obtain error exponent
`epsilon=delta/(50r^2)`, again with a degree threshold depending on `r`
and `delta`.  These results strongly support the route but do not, as
stated, certify it for `r=Theta(sqrt(k))`.

A 2025 quantitative result of Gould--Kelly makes the same hierarchy
visible.  In their notation the uniformity is `kappa+1`, and Theorem 1.4
assumes

\[
 {1\over D}\ll {1\over A}\ll\gamma\ll {1\over\kappa}.
                                                               \tag{6.1}
\]

It leaves at most

\[
 W B^{-1+\gamma}\log^A D,                            \tag{6.2}
\]

where `B` is bounded in particular by `sqrt(D/D_2)` and by higher
codegree ratios.  Our exact pair formula gives

\[
 \sqrt{D/D_2}=\sqrt{R(k-R)/2}=\Theta(k).             \tag{6.3}
\]

However, the displayed hierarchy is again a fixed-`kappa` asymptotic
statement, not an explicit diagonal estimate.  Worse, (6.2) is not
formally `o(W)` after merely substituting `kappa=Theta(sqrt(k))`: any
choice forced by `1/A << gamma << 1/kappa` makes `A` grow, and the factor
`log^A D` needs a uniform threshold analysis.  The theorem is therefore
not cited here as completing the diagonal nibble.

Accordingly the following implication remains a precise missing lemma:

> **Diagonal central nibble lemma.**  If a sequence of exactly regular
> `r`-graphs satisfies `r->infinity`, `r^2 Delta_2/D->0`, and has the
> central-rail degree growth (2.1), then it has a matching leaving `o(W)`
> vertices (preferably a quantitatively pseudorandom leave).

The condition `r^2 Delta_2/D=o(1)` is not asserted here to be sufficient
for arbitrary hypergraphs without proof.  A direct random-greedy/martingale
analysis tailored to (1.3), or a literature theorem with explicit uniform
thresholds, is still required.

## 7. Exact conclusion

The central owner-ordering gate has no degree imbalance and no pairwise
pseudorandomness defect:

\[
 \boxed{
 \text{exact regularity},\quad
 \text{exact fractional factor},\quad
 {\Delta_2\over D}={2\over R(k-R)},\quad
 r^2{\Delta_2\over D}=O(k^{-1}).}
\]

What remains is genuinely integral:

1. prove a diagonal growing-rank near-perfect matching theorem;
2. arrange a cover-down/absorber compatible with the residue modulo
   `2q+1`; and
3. retain the compulsory lower, upper, socket, history, and cap tickets.

No exact or bounded-leave central factor follows from the formulas alone.
