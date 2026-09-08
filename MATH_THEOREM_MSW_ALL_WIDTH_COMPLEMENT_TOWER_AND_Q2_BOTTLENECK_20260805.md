# The MSW all-width complement tower and the exact q2 bottleneck

**Date:** 2026-08-05  
**Method:** pure mathematics; exact geodesic identities and counting; no
computation, search, or solver  
**Status:** unconditional reduction and exact scalar ledger.  The complete
arbitrary-width upper deck of the canonical complementary-geodesic factor is
equivalent to surjectivity of every adjacent-intersection row of one derived
path factor on the rank-`(r-1)` layer.  The first row is exact.  The first
unproved row is `q=2`, where the available occurrence surplus is only a
`2/r` fraction of the target layer.  This note does not prove that row
surjective.

## 1. Canonical complementary geodesics

Let `Omega` have order `2r`.  The Mütze--Standke--Wiechert factor consists
of

\[
 C=\operatorname {Cat}_r={1\over r+1}{2r\choose r}
\tag{1.1}
\]

pairwise vertex-disjoint complementary Johnson geodesics which partition
the rank-`r` layer.  On one path choose disjoint ordered rails

\[
 \lambda_1,\ldots,\lambda_r,
 \qquad
 \rho_1,\ldots,\rho_r,
\tag{1.2}
\]

whose union is `Omega`.  Its owners are

\[
 M_j=\{\lambda_{j+1},\ldots,\lambda_r\}
       \cup\{\rho_1,\ldots,\rho_j\},
 \qquad 0\le j\le r.
\tag{1.3}
\]

For `1<=q<=r` and `0<=i<=r-q`, define the consecutive owner union

\[
 U^{(q)}_{i}=\bigcup_{j=i}^{i+q}M_j
\tag{1.4}
\]

and its complement

\[
 L^{(q)}_{i}=\Omega\setminus U^{(q)}_{i}.
\tag{1.5}
\]

Path labels are suppressed in (1.3)--(1.5); every assertion below is
applied to every one of the `C` paths.

## 2. Exact complement-tower identities

### Theorem 2.1 (closed form)

For every admissible `q,i`,

\[
 \boxed{
 U^{(q)}_{i}
   =\{\lambda_{i+1},\ldots,\lambda_r\}
       \cup\{\rho_1,\ldots,\rho_{i+q}\},}
\tag{2.1}
\]

and

\[
 \boxed{
 L^{(q)}_{i}
   =\{\lambda_1,\ldots,\lambda_i\}
       \cup\{\rho_{i+q+1},\ldots,\rho_r\}.}
\tag{2.2}
\]

In particular, their ranks are `r+q` and `r-q`, respectively.

#### Proof

Across `M_i,...,M_(i+q)`, the lambda rail only loses labels and the rho
rail only gains labels.  The union therefore contains the lambda suffix
already present in `M_i` and the rho prefix present by `M_(i+q)`, proving
(2.1).  The two displayed rail blocks are disjoint and have respective
orders `r-i` and `i+q`.  Taking their complement in (1.2) gives (2.2) and
the rank assertions. \(\square\)

### Theorem 2.2 (adjacent derivative recursion)

For `q<r`,

\[
 \boxed{
 U^{(q+1)}_i=U^{(q)}_i\cup U^{(q)}_{i+1},
 \qquad
 L^{(q+1)}_i=L^{(q)}_i\cap L^{(q)}_{i+1}.}
\tag{2.3}
\]

Thus arbitrary-width upper coverage by the owner factor is equivalent to
surjectivity of every row in the iterated adjacent-intersection tower

\[
 (L^{(1)}_i)_i,quad
 (L^{(2)}_i)_i,quad\ldots,quad(L^{(r)}_i)_i.
\tag{2.4}
\]

#### Proof

The union identity is associativity applied to consecutive owner windows.
The intersection identity follows either by complementation or directly
from (2.2): intersecting indices `i` and `i+1` retains the lambda prefix
through `i` and the rho suffix beginning at `i+q+2`, which is exactly
`L^(q+1)_i`. \(\square\)

## 3. The first row is an exact path factor

For `q=1`, the `U^(1)_i` are precisely the edge unions of the MSW paths.
The canonical factor enumerates every rank-`(r+1)` set exactly once.
Complementation therefore gives the following.

### Corollary 3.1

The values `L^(1)_i`, over all paths and all `0<=i<r`, enumerate
`binom(Omega,r-1)` exactly once.

On each original path they form the Johnson geodesic

\[
 L^{(1)}_i
 =\{\lambda_1,\ldots,\lambda_i\}
   \cup\{\rho_{i+2},\ldots,\rho_r\},
 \qquad0\le i<r,
\tag{3.1}
\]

with transition

\[
 L^{(1)}_{i+1}
   =L^{(1)}_i-\{\rho_{i+2}\}+\{\lambda_{i+1}\}.
\tag{3.2}
\]

Consequently the complete `q=1` complement row is a spanning
`C`-component path forest on the rank-`(r-1)` layer.  Each component has
`r` vertices and `r-1` edges.  Its two endpoints are complementary inside
the punctured ground set

\[
 \Omega\setminus\{\rho_1,\lambda_r\}.
\tag{3.3}
\]

The `q=2` upper gate is therefore exactly the assertion that the edge
intersections of this derived path forest cover every rank-`(r-2)` set.

#### Proof

Only (3.3) needs comment.  The first endpoint is
`{rho_2,...,rho_r}` and the last is `{lambda_1,...,lambda_(r-1)}`; these
partition the displayed `2r-2` element ground set.  All other statements
follow from (2.2), (2.3), and the exact MSW upper-q1 palette. \(\square\)

This derived object is not a standard smaller MSW factor on one common
ground set: the puncture pair `{rho_1,lambda_r}` varies with the component.
That variation is the exact obstruction to invoking a naive induction on
`r`.

## 4. Exact occurrence surplus at every width

Put

\[
 W={2r\choose r},
 \qquad
 T_q={2r\choose r-q}={2r\choose r+q}.
\tag{4.1}
\]

There are exactly

\[
 N_q=C(r-q+1)={W(r-q+1)\over r+1}
\tag{4.2}
\]

`q`-window occurrences.  Hence the occurrence/target ratio is

\[
 \boxed{
 R_q={N_q\over T_q}
 =\begin{cases}
 1,&q=1,\\[1mm]
 \displaystyle\prod_{j=2}^{q}{r+j\over r-j+2},&2\le q\le r.
 \end{cases}}
\tag{4.3}
\]

#### Proof

Every one of the `C` geodesics has `r-q+1` consecutive `(q+1)`-owner
windows.  Also

\[
 {T_q\over W}
 =\prod_{j=0}^{q-1}{r-j\over r+j+1}.
\tag{4.4}
\]

Substitute (1.1), (4.2), and (4.4), then cancel the factors `r+1` and
`r-q+1`. \(\square\)

In particular,

\[
 \boxed{R_2={r+2\over r}=1+{2\over r}.}
\tag{4.5}
\]

Equivalently, if the `q=2` palette is surjective, its total multiplicity
excess is forced to be

\[
 N_2-T_2={2\over r}T_2
 ={2W(r-1)\over(r+1)(r+2)}.
\tag{4.6}
\]

Thus `q=2` has no count deficit, but only a vanishing relative reserve.
No averaging argument can turn (4.5) into literal surjectivity without
controlling where those repeats occur.

For `q=o(r^(2/3))`, taking logarithms in (4.3) gives

\[
 \log R_q={q(q-1)\over r}+O\!\left({q^3\over r^2}\right).
\tag{4.7}
\]

At the Gaussian deadline `q~sqrt(pi*r/4)` appropriate to a `2r`-coordinate
problem,

\[
 R_q\longrightarrow e^{\pi/4}>2.
\tag{4.8}
\]

So the deadline-scale rows have comfortable scalar surplus even though the
first nontrivial derivative row is nearly tight.

## 5. Exact frontier

For the canonical MSW owner factor, the arbitrary-width upper problem is
not an additional collection of unrelated palettes.  It is one nested
derivative question:

> **Punctured-geodesic intersection-tower theorem.**  Prove that every
> rank-`(r-q)` set occurs among the values `L^(q)_i` for every
> `1<=q<=r`, or construct a safe rethreading of the MSW factor for which
> this holds while retaining its complementary stems and endpoint
> interfaces.

The theorem is known automatically only at `q=1`.  The exact first gate is
the lower-q1 palette of the derived punctured path forest in Corollary 3.1.
It has relative reserve `2/r`, much smaller than the constant reserve at
the deadline scale.  Hence a proof which starts only from aggregate
deadline capacity misses the genuinely tight upper row.

This note proves no `q=2` surjectivity, no rethreading, no residence across
component seams, no lower trace compiler, and no `B(k)+O(1)` conclusion.

## 6. Dependencies

1. the canonical MSW complementary-geodesic factor;
2. its exact upper-q1 palette, as frozen in
   `MATH_THEOREM_MSW_ENDPOINT_AUGMENTED_HAMILTONIZATION_EQUIVALENCE_20260805.md`;
3. elementary binomial identities.
