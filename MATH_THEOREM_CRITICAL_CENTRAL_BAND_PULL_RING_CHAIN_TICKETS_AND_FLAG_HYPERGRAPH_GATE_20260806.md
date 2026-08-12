# Critical central band, universal pull-ring chain tickets, and the exact flag-hypergraph gate

**Date:** 2026-08-06  
**Method:** pure mathematics; no computation, search, solver, or remote work  
**Status:** unconditional exact central-band chain factor, unconditional
literal pull-ring embedding theorem, an exact common-core compatibility
gate for independently prescribed ring chains, and an exact fractional
flag-hypergraph factor with elementary Boolean switchers.  The note does
**not** prove the complete critical chain factor, a perfect matching in the
flag hypergraph, or `nu(k) <= B(k)+O(1)`.

## 1. Parameters

Work on an odd ground set

\[
                         n=2r-1
\]

and put

\[
 W={n\choose r}={n\choose r-1},\qquad
 \Lambda=\sum_{s=1}^{r-1}{n\choose s}.
\]

Let `d` be the triangular depth,

\[
 d=\min\left\{q:qW+{q+1\choose2}\ge\Lambda\right\},
 \qquad D=d+1,
\]

and set

\[
                         c=r-d-1.
\]

Thus `c` is the core size in a depth-`d` pull ring.  As `r` tends to
infinity,

\[
 {d\over\sqrt r}\longrightarrow A:={\sqrt\pi\over2}.
\]

## 2. An exact critical-depth central band

### Theorem 2.1 (top-`d` band factor)

The Boolean band

\[
                 \mathcal B_d=\bigcup_{j=1}^{d}{[n]\choose r-j}
\]

has a partition into exactly `W` chains, every chain has size at most `d`,
and the chains attach bijectively to the rank-`r` owners.  The number of
covered strict-lower targets is

\[
                         \sum_{j=1}^{d}{n\choose r-j}.       \tag{2.1}
\]

Among all unions of `d` complete strict-lower ranks, this is the largest
possible one.

#### Proof

For each `2 <= j <= d`, the inclusion graph

\[
 {[n]\choose r-j}\longrightarrow {[n]\choose r-j+1}
\]

has a matching saturating its lower shore.  This follows either from the
normalized-matching property of the Boolean lattice or directly by edge
counting and Hall.  Choose these matchings independently.  Their union is
a collection of vertex-disjoint directed paths, because every vertex has
outdegree one below the top rank and indegree at most one.  Rank increases
strictly along every edge, so no directed cycle is possible.  Every path
ends in rank `r-1`, and the paths partition the displayed band.  Hence
there are exactly `|binom([n],r-1)|=W` paths and every path has at most `d`
vertices.

The rank-`r-1`--rank-`r` incidence graph is regular with equal shores, so it
has a perfect matching.  Use it to attach the `W` path tops to distinct
owners.  Finally the binomial rank sizes increase up to rank `r-1`, so the
top `d` ranks maximize (2.1) among all choices of `d` complete lower ranks.
\(\square\)

### Corollary 2.2 (exact asymptotic coverage)

The band factor covers the limiting fraction

\[
 \boxed{
 {\displaystyle\int_0^A e^{-x^2}\,dx
  \over
  \displaystyle\int_0^\infty e^{-x^2}\,dx}
 =\operatorname {erf}(A)
 }
                                                               \tag{2.2}
\]

of the strict lower ideal.  This is about `0.79`.

#### Proof

Uniformly for `j=O(sqrt(r))`, the central-binomial product formula gives

\[
 { {2r-1\choose r-j}\over W}
                         =e^{-j^2/r+o(1)}.
\]

Consequently (2.1), divided by `W sqrt(r)`, tends to
`int_0^A exp(-x^2)dx`, while `Lambda/(W sqrt(r))` tends to
`int_0^infty exp(-x^2)dx=A`.  Divide the two limits. \(\square\)

This is a genuine coefficient-one positive region.  The residual lower
tail is the hard part: scalar capacity, ordinary containment Hall, and
complete-rank selection are already known not to decide its critical
chainization.

## 3. Pull-ring endpoint chains

Take an even period `L` with

\[
                         D<L\le r+d.
\]

Choose a core `K` of size `c` and distinct private labels
`f_0,...,f_(L-1)` outside `K`.  For every `x in K`, choose an omission set
`I_x` whose cyclic connected components have length at most `d`, and put

\[
 A_t=\bigl(K-\{x:t\in I_x\}\bigr)\cup\{f_t\}.
                                                               \tag{3.1}
\]

Every length-`D` window has union

\[
 K\cup\{f_t,...,f_{t+d}\},                           \tag{3.2}
\]

so these are distinct rank-`r` owners forming a Johnson cycle.  The ring is
state-balanced.  For a proper cyclic interval `J`, its source union is

\[
 U(J)=F_J\cup(K-H(J)),\qquad
 F_J=\{f_t:t\in J\},\qquad
 H(J)=\{x\in K:J\subseteq I_x\}.                    \tag{3.3}
\]

Fix an endpoint `e`, and put

\[
                         J_q=[e-q+1,e]\qquad(1\le q\le d).
\]

The values `U(J_1) subset ... subset U(J_d)` are a strict inclusion chain:
the private interval gains one new label at each step, while `H(J_q)` can
only decrease.

## 4. Exact one-chain aperture

Let

\[
                  S_1\subsetneq S_2\subsetneq\cdots
                    \subsetneq S_\ell,qquad 1\le\ell\le d,  \tag{4.1}
\]

be a named strict Boolean chain.  We ask that it occur at the consecutive
widths

\[
                         a+1,a+2,...,a+\ell,
 \qquad 0\le a\le d-\ell.                            \tag{4.2}
\]

### Theorem 4.1 (sharp pull-ring endpoint embedding criterion)

The chain (4.1) has a literal realization

\[
                         U(J_{a+j})=S_j
                         \qquad(1\le j\le\ell)       \tag{4.3}
\]

in a pull ring of the form (3.1) if and only if

\[
                         |S_1|\ge a+1,
 \qquad                  |S_\ell|\le c+a+\ell.       \tag{4.4}
\]

The ring can be chosen with every `I_x` either empty or one cyclic interval
of length at most `d`.

#### Proof: necessity

The private part of `U(J_(a+j))` consists of exactly `a+j` labels.  At the
first displayed width these give `a+1` members of `S_1`.  At each later
width exactly one new private label appears; it was not present in the
preceding target because private labels are disjoint from `K`.  This proves
the first inequality.  The remaining members of `S_ell` all lie in the
`c`-set `K`, proving the second.

#### Proof: sufficiency

Choose `a+1` distinct elements of `S_1` and call their set `F_1`.  For
`2<=j<=ell`, choose

\[
                         g_j\in S_j\setminus S_{j-1}
\]

and put `F_j=F_(j-1) union {g_j}`.  Thus

\[
                         F_j\subseteq S_j,
 \qquad |F_j|=a+j,
\]

and a private label chosen at a later step is absent from every earlier
target.  The residual sets

\[
                         R_j=S_j\setminus F_j
\]

are nested.  By (4.4), `|R_ell|<=c`.  Choose a `c`-set `K` containing
`R_ell` and disjoint from `F_ell`, and place the labels of `F_j` on the
nested phase interval `J_(a+j)` in their order of appearance.  Complete the
private cycle with fresh labels outside `K`.

For `x in K`, let `e_x` be the first index `j` for which `x in R_j`.
If it exists, set

\[
                         I_x=J_{a+e_x-1},             \tag{4.5}
\]

where `J_0` is empty.  If `x` never enters `R_ell`, set

\[
                         I_x=J_{a+\ell}.              \tag{4.6}
\]

All these intervals have length at most `a+ell<=d`.  Since the `J_q` are
nested,

\[
 J_{a+j}\subseteq I_x
 \quad\Longleftrightarrow\quad x\notin R_j.
\]

Equation (3.3) now gives (4.3) coordinate by coordinate. \(\square\)

### Corollary 4.2 (every full critical chain is a literal ticket)

Every strict chain of `d` nonempty targets ending at rank at most `r-1`
has a literal pull-ring realization at widths `1,...,d`.

Indeed take `a=0,ell=d`.  Strictness gives `|S_1|>=1`, while
`|S_d|<=r-1=c+d`.

### Corollary 4.3 (the central-band chains sit on the sharp face)

Let a chain of Theorem 2.1 have length `ell`.  It occupies the consecutive
ranks

\[
                         r-\ell,...,r-1.
\]

It embeds at the final widths

\[
                         d-\ell+1,...,d.
\]

For this embedding (4.4) is tight at the top: take `a=d-ell` and note

\[
                         |S_\ell|=r-1=c+d=c+a+\ell.
\]

Thus the central-band chain factor and the literal pull-ring aperture fit
exactly; the unresolved issue is grouping the tickets into common physical
rings.

## 5. Several independently prescribed chains in one ring

The one-chain theorem can be planted simultaneously when the prescription
arcs are separated.

### Theorem 5.1 (separated-arc simultaneous embedding)

For `1<=i<=h`, let

\[
 S^i_1\subsetneq\cdots\subsetneq S^i_{\ell_i}
\]

be a chain intended for widths `a_i+1,...,a_i+ell_i`, and put
`q_i=a_i+ell_i<=d`.  Suppose:

1. the cyclic ring contains pairwise disjoint arcs of lengths `q_i`, with
   at least one unused phase between consecutive arcs;
2. for every `i` there is a nested private flag

   \[
    F^i_j\subseteq S^i_j,\qquad |F^i_j|=a_i+j,
   \]

   gaining one new element at each step; the flags belonging to different
   `i` are disjoint; and
3. the common residual bank satisfies

   \[
   R=\bigcup_i\bigl(S^i_{\ell_i}\setminus
                           F^i_{\ell_i}\bigr),\qquad |R|\le c, \tag{5.1}
   \]

   and `R` is disjoint from every private flag.

Then one pull ring realizes all `h` prescribed chains simultaneously.

#### Proof

Choose one common core `K` containing the union in (5.1), place each private
flag on its own arc, and complete `K` and the private cycle with fresh
labels.  For each `x in K`, perform the construction (4.5)--(4.6) separately
inside every prescription arc and let `I_x` be the union of the resulting
local omission intervals.  The gap between prescription arcs keeps these
as different cyclic components; every component has length at most `d`.
Equation (3.3) is local on each arc and gives every prescribed value.
\(\square\)

For full `d`-chains, each independent prescription consumes `d` phases and
one separating phase.  Therefore this direct independent planting has

\[
                         h\le\left\lfloor {L\over d+1}\right\rfloor
                         \le\left\lfloor {r+d\over d+1}\right\rfloor
                         =\Theta(r/d).                       \tag{5.2}
\]

The ring itself has `L` endpoint chains.  Hence only `Theta(r/d)` of them
can be prescribed independently by disjoint apertures; the other `L-h`
chains are necessarily correlated by the same omission runs.  This is the
precise limitation of treating the ring as a collection of private local
tickets.

### Proposition 5.2 (common-core gate at the top rank)

If a width-`d` endpoint value in a pull ring has rank `r-1`, then it is

\[
                         K\cup F_J,qquad |J|=d.       \tag{5.3}
\]

In particular all rank-`r-1` width-`d` values in one ring contain the same
`c`-set `K`.

#### Proof

Equation (3.3) gives size

\[
                         d+c-|H(J)|=r-1-|H(J)|.
\]

Rank `r-1` forces `H(J)` empty, proving (5.3). \(\square\)

Consequently a ringwise proof of the complete critical chain factor must
do more than find the chains individually.  It must partition the entire
rank-`r-1` layer into cyclic groups with a common `(r-d-1)`-core and then
choose one common omission language per group which makes **all** lower
endpoint values globally one-copy.  Theorem 4.1 closes the local ticket;
Proposition 5.2 is the exact new global design gate.

### Proposition 5.3 (full ring-table rigidity)

Fix `K` and the cyclic private labels.  A complete proposed endpoint table

\[
                         (S_{e,q}:e\in\mathbb Z_L, 1\le q\le d)
                                                               \tag{5.4}
\]

comes from one pull ring if and only if the following hold.

1. `S_(e,1)={f_e} union R_e` for some `R_e subseteq K`;
2. for every `x in K`, the cyclic zero set

   \[
                         I_x=\{e:x\notin R_e\}         \tag{5.5}
   \]

   has all connected components of length at most `d`; and
3. every higher cell is forced by

   \[
                  \boxed{S_{e,q}=\bigcup_{t=e-q+1}^{e}S_{t,1}.} \tag{5.6}
   \]

Equivalently, for `x in K`,

\[
 x\notin S_{e,q}
 \quad\Longleftrightarrow\quad[e-q+1,e]\subseteq I_x.          \tag{5.7}
\]

#### Proof

Necessity follows from (3.1): the width-one cells are the source letters,
and every longer cell is their literal interval union.  Their core-zero
sets are exactly the omission sets, so the residence hypothesis gives item
2 and (5.7).

Conversely define the source word by `A_e=S_(e,1)`.  Items 1--2 put it in
the pull-ring form (3.1), and item 3 makes every proposed cell its actual
interval union. \(\square\)

Thus the `L` bottom cells determine all `Ld` proper cells.  The sparse
prescription theorem does not turn a ring into `L` independent chain
slots: once a positive-density set of endpoint chains is prescribed, their
shared width-one row and the coordinate zero-run geometry must be solved as
one cyclic interval problem.  This is the precise cyclic/necklace gate
behind the common-core formulation.

## 6. The symmetric flag hypergraph

There is a separate direct route which does not start from an SCD or from
common-core rings.  On the zero-boundary face `Lambda<=dW`, put

\[
                         z=dW-\Lambda.
\]

Make a vertex for every rank-`r` owner, every strict-lower target, and `z`
dummy vacancies.  A hyperedge consists of

* one owner `T`;
* one strict inclusion chain of `m<=d` nonempty proper subsets of `T`; and
* `d-m` distinct dummy vacancies.

Thus every edge has exactly `d+1` vertices.

### Theorem 6.1 (exact fractional flag factor)

The symmetric flag hypergraph has a fractional perfect matching.

#### Proof

Put

\[
                         q_s={{n\choose s}\over W}
                         \qquad(1\le s<r).
\]

Then `0<=q_s<=1` and

\[
                         \sum_{s<r}q_s={\Lambda\over W}\le d.
\]

Hence `q=(q_s)` lies in the independence polytope of the rank-`d` uniform
matroid.  Choose a random rank set `R subseteq {1,...,r-1}` of size at most
`d` with marginals `Pr(s in R)=q_s`.  It may be chosen with sizes `d` and
`d-1` only.  Indeed minimality of `d` gives

\[
 (d-1)W+{d\choose2}<\Lambda\le dW,
\]

so `d-1<Lambda/W<=d`; the corresponding slab of the cube is the convex
hull of the incidence vectors of `(d-1)`- and `d`-subsets.

For each owner `T`, choose a uniform ordering of its `r` elements and use
the prefixes at ranks in `R`.  These prefixes form one chain.  When
`|R|=d-1`, choose one dummy uniformly; when `|R|=d`, choose none.  Averaging
this random edge over all `W` owners gives owner load one.  A fixed rank-`s`
target `S` receives load

\[
 { {n-s\choose r-s}\over {r\choose s}}q_s
 ={W\over {n\choose s}}q_s=1.                       \tag{6.1}
\]

The expected number of vacancies per edge is

\[
 d-\sum_s q_s={z\over W},
\]

so uniform dummy choice gives every dummy load one.  These edge weights
are the desired fractional perfect matching. \(\square\)

When `Lambda>dW`, the endpoint staircase supplies the excess inventory.
The same proof gives the known fractional triangular factor after the
boundary occurrence variables are included.  The zero-boundary statement
is isolated here only to keep the hypergraph notation literal.

## 7. Boolean-diamond switchers

The flag hypergraph has a large exact trade lattice.

### Proposition 7.1 (one-edge Johnson switcher)

Let `S,S'` be adjacent rank-`s` targets:

\[
                         |S\cap S'|=s-1,
 \qquad                  |S\cup S'|=s+1.
\]

Suppose a flag edge contains `S`, every selected lower predecessor of `S`
is contained in `S cap S'`, and every selected upper successor (including
the owner) contains `S union S'`.  Replacing `S` by `S'` gives another flag
edge with the same owner, dummies, and all other targets.  Hence the two
edge-incidence vectors differ by

\[
                         \mathbf e_S-\mathbf e_{S'}.  \tag{7.1}
\]

#### Proof

All comparabilities not incident with the replaced rank are unchanged.
The displayed lower and upper containment hypotheses are exactly the two
comparabilities needed at that rank. \(\square\)

Such a context exists for every Johnson edge.  Indeed choose `d-1` further
rank positions from the other `r-2` strict-lower ranks.  At every chosen
rank below `s`, use a subset of `S cap S'`; at every chosen rank above `s`,
use a superset of `S union S'`; complete at the rank-`r` owner.  The lower
and upper choices can be nested, and `d<=r-1` gives enough rank positions.
The same construction works at `s=1` or `s=r-1` by putting all other
positions on the available side.  It uses a full `d`-target edge and hence
requires no dummy vacancy.

Since every Johnson graph `J(n,s)` is connected, the vectors (7.1)
generated by these switchers span
the complete zero-sum integer lattice within every rank layer.  Therefore
the direct flag model has no hidden within-rank congruence obstruction:
after rank totals and boundary divisibility are fixed, every named-target
difference is generated by literal Boolean-diamond switches.

This is precisely the local ingredient an absorber would need.  It is not
itself a perfect-matching theorem.  The uniformity is `d+1=Theta(sqrt r)`,
the edge types mix many rank patterns, and a switcher only exchanges two
possible fillings of one reserved auxiliary flag.  To derive an exact
factor one still needs a robustly matchable reservoir which provides
pairwise disjoint switcher contexts for the entire terminal leave.  The
standard small-codegree nibble yields only an almost-perfect matching
without that exact absorption row; invoking a fixed-uniformity design
theorem without checking its growing-uniformity and divisibility hypotheses
would be invalid.

There is also a sharp terminal warning against a naive `K_(d,d)` absorber.

### Proposition 7.2 (the owner interface is square-free; hexagons replace
diamonds)

The incidence graph between rank `r-1` targets and rank `r` owners is
`C_4`-free.  In particular it contains no `K_(2,2)`, hence no terminal
`K_(d,d)` switch bank.

Its first elementary assignment trade is a Boolean hexagon.  If `C` has
rank `r-2` and `a,b,c` are distinct outside `C`, then

\[
\begin{array}{c}
 C+a\ --\ C+a+b\ --\ C+b\ --\ C+b+c\ --\ C+c\ --\ C+c+a\ --\ C+a
\end{array}                                                   \tag{7.2}
\]

is an alternating `C_6`.  Its two alternating perfect matchings give an
exact three-owner reassignment trade.  If three pairwise disjoint lower
flags end at `C+a,C+b,C+c`, respectively, the same two matchings lift to a
three-edge trade in the flag hypergraph which preserves every lower target
and changes only the owner attachments.

#### Proof

Two distinct rank-`r-1` sets have a common rank-`r` superset only when their
union has rank `r`, and in that case the union is the unique common owner.
Thus two left vertices never have two common right neighbours, proving the
`C_4` assertion.  Every containment in (7.2) is immediate.  Taking alternate
edges covers its three left and three right vertices exactly once.  A lower
flag ending at one left vertex is contained in either adjacent owner, so
the owner reassignment lifts without altering that flag. \(\square\)

At the top rank, the owner in the one-edge switcher of Proposition 7.1 is
forced to be `S union S'`.  Hence many prescribed top switches cannot be
made resource-disjoint merely by counting flag contexts: swaps with the
same union collide at their unique owner.  A genuine absorber must combine
the one-edge target switchers with hexagonal (or longer) owner-routing
circuits.  This is the exact reason that fractional symmetry plus Boolean
diamonds is not yet an off-the-shelf perfect-matching proof.

## 8. Exact frontier

The results above separate three statements which had been conflated.

1. **A large coefficient-one region is exact.**  The top `d` ranks have an
   anchored depth-`d` factor, covering the fraction (2.2).
2. **Every critical chain is locally literal.**  A full `d`-chain is one
   endpoint chain of a balanced pull ring, with no target-by-target search.
3. **The remaining obstruction is global correlation.**  Ringwise, one
   must solve the common-core cyclic decomposition and make all incidental
   endpoint chains one-copy.  Directly, one must turn the fractional flag
   factor and its Johnson switchers into an exact perfect matching.

Neither the exact containment SDR nor ordinary normalized matching supplies
that last correlation.  Conversely, there is no longer a local aperture,
rank-majorisation, or within-rank lattice obstruction to blame.
