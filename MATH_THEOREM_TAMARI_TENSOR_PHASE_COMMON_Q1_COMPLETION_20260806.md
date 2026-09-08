# The tensored Tamari phases have one common exact q1 completion

**Date:** 2026-08-06  
**Method:** support substitution and the polynomial protected two-factor
extension theorem; no computation or search  
**Status:** unconditional for every tensor semilength `r>=16`.  This is an
exact spanning q1-factor theorem, not a shortest-wreath, Hamilton, residence,
all-width, or compiler theorem.

## 0. Verdict

Let `P^-` and `P^*` be the two four-wreath tensors from
`MATH_THEOREM_TENSORED_FOUR_ROW_TAMARI_WREATH_TRANSPORT_20260806.md` at
semilength `r`.  Their middle-vertex supports agree exactly.  Consequently
their middle-level incidence lifts are two simple 2-regular graphs on the
same protected lower and upper shore sets.

For every `r>=16`, there is one simple residual two-factor `R`, supported
on the complementary shore sets, such that

\[
                         P^-\dot\cup R,
             \qquad      P^*\dot\cup R                 \tag{0.1}
\]

are both spanning simple q1 two-factors.  Equivalently, after alternating
edge-colouring `R`, the same pair of residual perfect matchings completes
both alternating incidence matchings of both phases.

The four protected wreaths are saturated cycle components, so both factors
in (0.1) have exactly

\[
                         4+c(R)                         \tag{0.2}
\]

components.  The extension theorem does not bound `c(R)`.

## 1. Incidence lift and common deleted shores

Put

\[
 \Omega=[2r+1],\qquad
 G=ML_{r+1}
  =\left({\Omega\choose r},{\Omega\choose r+1};\subset\right).
                                                               \tag{1.1}
\]

For an odd-graph cycle `C` on rank-`r` vertices, its bipartite incidence
lift has lower shore `V(C)` and upper shore

\[
                         \overline {V(C)}
   =\{\Omega-X:X\in V(C)\}.                           \tag{1.2}
\]

Indeed, if consecutive odd-graph vertices `X,X'` are disjoint, then
`X' subset Omega-X` and `X subset Omega-X'`.  The bipartite double cover of
an odd `(2r+1)`-cycle is one even `(4r+2)`-cycle.

Let `Z^-` and `Z^*` be the unions of the four lower supports of the two
Tamari phases.  The tensor theorem proves equality of the aggregate path-
state and adjacent-union ledgers.  Those are exactly the two kinds of
rank-`r` vertices in the four odd wreaths, so

\[
                         Z^- = Z^*=:Z.                 \tag{1.3}
\]

The four wreaths are disjoint in either phase.  Their upper incidence
shore is therefore, in either phase,

\[
                         Y=\{\Omega-X:X\in Z\}.        \tag{1.4}
\]

Write the two incidence lifts as `Q^-` and `Q^*`.  Each is a disjoint
union of four even cycles and is 2-regular on the same vertex set `Z+Y`.

### Lemma 1.1 (identical deletion by both alternating colours)

For either phase `epsilon in {-,*}`, properly two-colour the cycles of
`Q^epsilon` and call the two matching classes
`F_0^epsilon,F_1^epsilon`.  Then, for both `i=0,1`,

\[
 V(F_i^\epsilon)\cap{\Omega\choose r}=Z,
 \qquad
 V(F_i^\epsilon)\cap{\Omega\choose r+1}=Y.           \tag{1.5}
\]

Thus every colour and both phases leave the identical residual graph

\[
                   G_0=G[\mathcal L-Z,\mathcal U-Y]. \tag{1.6}
\]

#### Proof

Each colour of an alternatingly coloured even cycle is a perfect matching
between that cycle's two shores.  Taking the four disjoint cycles proves
(1.5), and (1.6) follows. \(\square\)

Fixed row endpoints are useful for retaining named orientations and
occurrence roles, but are not needed for the shore identity (1.5): common
support and 2-regularity already force it.

## 2. Exact exposure of a fixed wreath

Use the cyclic-window form of a shortest wreath.  If `q` is a cyclic order
on `2r+1` points, its protected lower vertices are its cyclic `r`-intervals
and its protected upper vertices are the complementary cyclic
`(r+1)`-intervals.

### Lemma 2.1 (two hits per star per wreath)

For one shortest wreath:

1. any rank-`r` set is contained in at most two protected upper vertices;
2. any rank-`(r+1)` set contains at most two protected lower vertices.

#### Proof

Two distinct cyclic `(r+1)`-intervals on a `(2r+1)`-cycle have intersection
of size at least `r` only when their starting points are adjacent.  Three
cyclic starts cannot be pairwise adjacent on a cycle of length at least
five.  Hence one `r`-set lies in at most two such intervals, proving the
first assertion.  Complementation gives the second. \(\square\)

For four disjoint wreaths, Lemma 2.1 gives the two all-occurrence exposure
bounds

\[
                         \alpha(Q^\epsilon),
                         \beta(Q^\epsilon)\le8.       \tag{2.1}
\]

The protected edge count is

\[
 |E(Q^\epsilon)|=4(4r+2)=8(2r+1).                   \tag{2.2}
\]

## 3. One common simple residual factor

The proof of
`MATH_THEOREM_POLYNOMIAL_PROTECTED_FOREST_EXTENSION_FROM_TWO_EXPOSURES_20260805.md`
uses only the following properties of its protected graph:

* every used lower vertex has protected degree two;
* every unused lower vertex has protected degree zero;
* every upper vertex has protected degree at most two; and
* the two exposure bounds and protected edge count obey its exact
  inequality.

Acyclicity of the protected owner paths is never used in the Ore--Ryser,
near-shadow, or optional-core argument.  Therefore the same theorem applies
verbatim to a disjoint union of protected incidence cycles such as
`Q^epsilon`.

Use the theorem's parameter

\[
                         R=r+1.                       \tag{3.1}
\]

Equations (2.1)--(2.2) give

\[
 D_\alpha,D_\beta\ge R-8-1=r-8,                     \tag{3.2}
\]

and its exact localization quantity is

\[
\begin{aligned}
 M_R(e)
 &= {R(R-1)\over2R-1}\,8(2r+1)\\
 &=8r(r+1).                                          \tag{3.3}
\end{aligned}
\]

At `r=16`,

\[
 {2(r-8)-1\choose r-8}={15\choose8}=6435
     >8\cdot16\cdot17=2176.                          \tag{3.4}
\]

When `r` increases by one, the binomial term is multiplied, with
`D=r-8`, by

\[
 { {2D+1\choose D+1} \over {2D-1\choose D} }
       =4-{2\over D+1}>3,                            \tag{3.5}
\]

whereas `8r(r+1)` is multiplied by `(r+2)/r<2`.  Hence (3.4) and the exact
extension inequality hold for every `r>=16`.

Apply the protected two-factor theorem to `Q^-`.  It gives a spanning
simple two-factor

\[
                         K^-=Q^-\dot\cup R,           \tag{3.6}

where every edge of `R` lies in the residual graph `G_0`: all vertices of
`Z+Y` already have degree two in `Q^-`.  Since `Q^*` is also 2-regular on
exactly `Z+Y`,

\[
                         K^*=Q^*\dot\cup R            \tag{3.7}

is a spanning simple two-factor as well.  This proves (0.1).

Alternately colour every component of `R`, obtaining edge-disjoint perfect
matchings `R_0,R_1` of `G_0`.  Lemma 1.1 then gives, simultaneously for
both phases,

\[
                         F_i^\epsilon\dot\cup R_i
 \quad(i=0,1),                                       \tag{3.8}

two perfect matchings whose union is (3.6) or (3.7).  This is the promised
common residual pair.

## 4. Components and stronger/weaker variants

Every protected vertex has degree two inside its Tamari incidence cycle.
No residual edge can meet it.  Therefore the four packet cycles are
isolated components in both phases, and the remaining components are
literally those of `R`.  This proves the exact count (0.2), including
equality between the two phase component counts.

The Hamilton-anchored matching theorem can instead choose a common
**coloured multigraph** residual pair with polynomially many components
and polynomially many common-edge two-cycles.  It does not currently give
a simple polynomial-component completion.  Conversely, the simple
two-factor theorem used above gives no bound on `c(R)`.  Combining both
properties remains a separate graph problem.

The same proof applies to the two fourteen-row common-tail partial factors
(`H=14`).  Then

\[
 e=28(2r+1),\qquad \alpha,\beta\le28,qquad
 M_R(e)=28r(r+1),                                   \tag{4.1}

and the exact criterion holds from `r=38` onward because

\[
 {19\choose10}=92378>28\cdot38\cdot39=41496.        \tag{4.2}

The resulting factors have `14+c(R)` components.

## 5. What shortest-wreath structure does and does not do

The common-completion substitution itself needs only:

1. two simple 2-regular bipartite protected graphs;
2. the same protected shore sets; and
3. one extension theorem for either protected graph.

It does not use complement geodesics, cyclic intervals, or fixed endpoints.
Shortest-wreath structure is used upstream to prove common support,
simplicity, and the constant exposure bound of Lemma 2.1.

The residual factor `R` is an arbitrary middle-levels incidence
two-factor.  Its components need not be bipartite lifts of shortest odd-
graph wreaths, need not have the required all-width OR deck, and need not
be resident.  Thus this theorem closes the exact owner/q1 factor host for
the Tamari phase switch, but it does **not** solve the cross-box
shortest-wreath completion problem in
`MATH_THEOREM_TAMARI_BASE_FACTOR_COMMON_TAIL_PARTIAL_SUSPENSION_20260806.md`
or the all-k carrier construction.
