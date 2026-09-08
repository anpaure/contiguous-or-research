# Facet absorbers: the exact star-decomposition reduction, a consecutive-size repair, and the named-target gate

Date: 2026-08-02  
Status: exact reductions and local theorems.  This note does **not** prove the
new growing-rank star-decomposition lemma isolated in Section 5, nor the
global named-target packing.  Consequently it does not prove an upper bound
for `nu(k)`.

## 0. Outcome

Put

\[
 c=r-d-1,\qquad q=d+2,\qquad W=\binom{k}{r},
 \qquad 2\le q\le r.
\]

The star-orientation and divisibility statements in Sections 1--2 assume
`k>=r+1`.  The literal primitive constructions from Section 3 onward are
used in their source regime `d>=2` (hence `q>=4`) and `c>=1`; the canonical
sufficiently-large regime satisfies these hypotheses.  The algebraic
partial-simplex calculation itself remains valid at `q=2,3`.

The facet-owner hypergraph from the OFHT note has a simpler exact dual
description.  After complementing every rank-`r` owner, a facet block is a
`q`-edge star in the complete `(k-r)`-uniform hypergraph.  Thus a perfect
owner matching is exactly an orientation of every `(k-r)`-set to one of its
facets such that every facet receives a multiple of `q` sets.  Equivalently,
it is a decomposition of the complete rank-`r` hypergraph into the
`q`-facet partial simplex `F_(r,q)`.

For `q<=r`, the only design divisibility condition of `F_(r,q)` is

\[
                         q\mid W.                       \tag{0.1}
\]

This calculation is exact, but it is not an existence proof in the present
regime: both `r` and `q` grow with `k`, and `k` is only about `2r`.  The
usual fixed-pattern design theorems do not supply the required uniform
statement.

The scalar divisibility can be removed without leaving owners.  Besides the
length-`q` facet absorber there is an explicit length-`q+1` common-core
absorber.  It realizes the same primitive pair using `d+1`, rather than `d`,
short buffers.  Since `gcd(q,q+1)=1`, every sufficiently large `W` has

\[
                  W=Aq+B(q+1),\qquad 0\le B<q.          \tag{0.2}
\]

Thus two module sizes remove the only scalar owner divisibility row.  The
remaining whole-layer owner-only input is stated precisely in Section 5.

For the primitive subinventory, no external matching theorem is needed.
A maximal facet matching leaves at most `(q-1)W/(r+1)` owners.  Meanwhile
the canonical multiplicity of `g_(d-1,d+1)` is at most `A_(d+1)`, and

\[
 {qA_{d+1}\over W}\longrightarrow
                  {\pi\over2}e^{-\pi/4}<0.717.
\]

Thus every canonical adjacent-buffer primitive can be assigned a disjoint
facet absorber for all sufficiently large `k`.  This is an exact
subinventory packing, not an `o(W)`-leave conclusion.

Named targets are not a bounded-conflict afterthought.  The complete target
deck of one facet module is computed in Section 6.  Two vertex-disjoint
owner blocks can share a rank-`(r-1)` target, and in the middle-level regime
`Theta(k)` pairwise owner-disjoint blocks can share that one target.  Hence
a pairwise owner-disjoint block matching does not imply a target-simple
packing.  More
strongly, that family has a rank-`(c+2)` pigeonhole obstruction for every
choice of cyclic orders once its size exceeds `Theta(q)`; the natural
`Theta(k)` family is therefore unlabelable when `q=Theta(sqrt(k))`.  Section 8
gives a proof-safe local ordering criterion which is sufficient to avoid all
previously used targets; no global theorem establishing that criterion is
claimed.

## 1. Complementation gives a star decomposition

Let `O=binom([k],r)`.  The `q`-uniform facet hypergraph has edges

\[
 B(Z,V)=\{Z-\{v\}:v\in V\},
 \qquad Z\in\binom{[k]}{r+1},\quad V\in\binom Zq.        \tag{1.1}
\]

Put `a=k-r`.  Complementing owners sends (1.1) to

\[
 \overline{B(Z,V)}
   =\{K+\{v\}:v\in V\},\qquad K=[k]-Z,\quad |K|=a-1.   \tag{1.2}
\]

This is a `q`-edge star in the complete `a`-uniform hypergraph, with common
core `K`.

### Theorem 1.1 (exact star-orientation equivalence)

The following objects are equivalent.

1. A perfect matching in the facet hypergraph (1.1).
2. A decomposition of `binom([k],a)` into `q`-edge stars with
   `(a-1)`-cores.
3. A map

   \[
              \phi:\binom{[k]}a\longrightarrow\binom{[k]}{a-1},
              \qquad \phi(E)\subset E,                    \tag{1.3}
   \]

   such that every fibre of `phi` has cardinality divisible by `q`.

#### Proof

Complementation is a bijection and (1.2) proves the equivalence of the first
two statements.  Given a star decomposition, send every edge to its star
core.  Conversely, for every core `K`, partition the fibre `phi^(-1)(K)`
into `q`-sets.  Each part is a star of the form (1.2).  \(\square\)

The last formulation is useful because it displays the integrality missing
from the uniform fractional owner cover.  It is a degree-constrained
orientation of the Boolean incidence graph, not an ordinary bipartite
matching.

## 2. There is only one partial-simplex divisibility row

Let `F_(r,q)` be the rank-`r` hypergraph on an `(r+1)`-set `Z` whose edges
are `Z-{v}`, `v in V`, for a fixed `q`-set `V subset Z`.  A perfect matching
in (1.1) is the same as an `F_(r,q)`-decomposition of the complete
rank-`r` hypergraph on `[k]`.

For `0<=i<r`, let

\[
 g_i(F)=\gcd\{\deg_F(S):S\in\binom{Z}{i}\}.             \tag{2.1}
\]

### Lemma 2.1 (exact divisibility lattice)

If `2<=q<=r`, then

\[
                       g_0(F_{r,q})=q,
 \qquad                g_i(F_{r,q})=1\quad(1\le i<r).  \tag{2.2}
\]

Consequently the standard `F_(r,q)`-divisibility conditions for the complete
rank-`r` host reduce exactly to `q | binom(k,r)`.

#### Proof

For `S in binom(Z,i)`, an edge `Z-{v}` contains `S` exactly when
`v notin S`.  Therefore

\[
                         \deg_F(S)=q-|S\cap V|.          \tag{2.3}
\]

For `i=0` this is always `q`.  Suppose `1<=i<r`.  If
`i<=r+1-q`, both `|S cap V|=0` and `|S cap V|=1` occur, so the degree set
contains the consecutive integers `q,q-1`.  If `i>r+1-q`, its minimum
possible intersection with `V` is

\[
                         t_0=i-(r+1-q)\le q-2,
\]

because `i<=r-1`.  Both `t_0` and `t_0+1` occur, and (2.3) again gives two
consecutive positive degrees.  Their gcd is one.  \(\square\)

This lemma removes possible hidden coordinate, pair, or higher-link
congruences.  It does not assert that the necessary divisibility condition
is sufficient when the pattern grows with the host.

## 3. A consecutive-size absorber

Assume here `k>=r+2`, `d>=2`, and `c>=1`.  The common-core construction in the sharp
primitive-lift theorem works for every cycle length greater than `d+1`.
The first length beyond the facet absorber is particularly useful.

Choose

\[
 |G|=c-1,\qquad b\notin G,
 \qquad U=\{u_0,\ldots,u_q\},\quad |U|=q+1,             \tag{3.1}
\]

all disjoint, and fix a cyclic order on `U`.  Put

\[
 S_0=G+\{u_0\},\qquad
 S_i=G+\{b,u_i\}\quad(1\le i\le q).                   \tag{3.2}
\]

There is one state of type

\[
 P=(c,2,1,\ldots,1)
\]

and `q` states of type

\[
 H=(c+1,1,\ldots,1).
\]

Let `K=G+{b}`.  Every owner is

\[
          K\ \dot\cup\ (q-1\hbox{ consecutive tags of }U)
       =K\cup\bigl(U-\{u_i,u_{i+1}\}\bigr).            \tag{3.3}
\]

Thus the owner block is

\[
 C(K,U,\pi)=
 \{K\cup(U-\{u_i,u_{i+1}\}):i\in\mathbb Z/(q+1)\}.    \tag{3.4}
\]

### Theorem 3.1 (length-`q+1` primitive absorber)

The block (3.4) consists of `q+1` distinct rank-`r` owners and carries a
literal owner-simple cycle.  After designating one `H` as the primitive
high role, the remaining `q-1=d+1` copies of `H` are short buffers.  Marking
the primitive pair fully and every buffer at ranks `c+2,...,r-1` gives an
injective lower target deck inside the module.

#### Proof

The literal type calculation is the common-core calculation: at the unique
`P` position the preceding `H` contributes `{b,u_q}` to age one, while at
an `H` position the current source refreshes both `G` and `b`; every older
source then contributes only its private tag.  A `(d+1)=(q-1)`-window in a
cycle of length `q+1` omits exactly two consecutive tags, proving (3.3).
Different omitted adjacent pairs give different owners.

Every marked prefix above rank `c+1` is `K` together with a proper cyclic
interval of private tags.  At a fixed interval length these sets are
distinct.  The ranks `c` and `c+1` occur only on the designated primitive
roles.  Hence the complete marked deck is injective.  \(\square\)

### Corollary 3.2 (scalar divisibility repair)

If `W>=q^2-1`, set

\[
 B=W\bmod q\quad(0\le B<q),\qquad
 A={W-(q+1)B\over q}.                                  \tag{3.5}
\]

Then `A,B` are nonnegative integers and

\[
                         W=Aq+B(q+1).                   \tag{3.6}
\]

Thus the two literal module sizes `q,q+1` remove the scalar owner-count
divisibility without any owner leave.

The corollary is arithmetic only.  It does not assert that the corresponding
owner blocks can be selected disjointly.

## 4. Exact owner packing for the canonical primitive subinventory

An exact factor of the whole owner layer is difficult, but the aggregate
rotor decomposition does not require every owner to lie in a primitive
facet absorber.  For a prescribed subinventory a maximal-matching argument
is already strong enough.

### Theorem 4.1 (maximal facet-packing bound)

The facet hypergraph has a matching leaving at most

\[
                         {q-1\over r+1}W                 \tag{4.1}
\]

owners uncovered.  Consequently it contains `t` disjoint facet blocks for
every integer `t` satisfying

\[
                tq\le W-{q-1\over r+1}W.                \tag{4.2}
\]

#### Proof

Take a maximal matching and let `R` be its uncovered owner family.  If some
`(r+1)`-set `Z` had at least `q` facets in `R`, those facets would form an
edge disjoint from the matching, contradicting maximality.  Hence every
`Z` contains at most `q-1` members of `R`.  Double-counting containments
`T subset Z`, with `T in R`, gives

\[
 (k-r)|R|
 \le(q-1)\binom{k}{r+1}
 =(q-1){k-r\over r+1}W.
\]

This proves (4.1).  The resulting matching has at least the number of edges
in (4.2); discard surplus matching edges to obtain exactly `t`.  \(\square\)

This is still only an `O(qW/r)=o(W)` leave as a whole-layer theorem.  Its
use here is different: it packs an exact prescribed number of primitive
modules.

For the canonical aggregate vector, recall

\[
 n_s=\binom{k}{s}-b_s,\qquad
 A_\ell=n_{r-\ell}-n_{r-\ell-1}.                         \tag{4.3}
\]

Every copy of the primitive `g_(d-1,d+1)` consumes one occurrence at
coordinate `d+1`; therefore its multiplicity `t` in any aggregate
decomposition satisfies

\[
                              t\le A_{d+1}.              \tag{4.4}
\]

### Theorem 4.2 (all canonical adjacent-buffer primitives pack exactly)

For all sufficiently large `k`, every collection of at most `A_(d+1)`
primitive adjacent-buffer packets has pairwise owner-disjoint length-`q`
facet absorbers.  In particular, once `d` short buffers have been allocated
to every such primitive, this owner selection adds no occurrence leave.

#### Proof

We show that (4.2) holds with `t=A_(d+1)`.  Write `r=ceil(k/2)`.  The central
binomial estimate gives, in either parity,

\[
 {\Lambda\over W}={\sqrt{\pi r}\over2}+O(1),
 \qquad {d\over\sqrt r}\longrightarrow {\sqrt\pi\over2}. \tag{4.5}
\]

Indeed, for `k=2r`, symmetry gives

\[
 \Lambda={2^{2r}-\binom{2r}{r}\over2}-1,
\]

while for `k=2r-1` it gives `Lambda=2^(2r-2)-1`; in both cases
Stirling's formula

\[
 \binom{2r}{r}={4^r\over\sqrt{\pi r}}(1+O(r^{-1}))
\]

proves the first relation.  The triangular term `d(d+1)/(2W)` is
exponentially small, so the defining minimality of `d` proves the second.

For large `k`, in fact `c-1>d` (equivalently `r>2d+2`), and hence the
Ferrers correction vanishes at both `c` and `c-1`.  Thus

\[
 A_{d+1}=\binom{k}{c}-\binom{k}{c-1}.                   \tag{4.6}
\]

Put `h=d+1`.  Direct products give, in both parities,

\[
 {\binom{k}{c}\over W}
       =\exp\left(-{h^2\over r}+O(h/r+h^3/r^2)\right)
       \longrightarrow e^{-\pi/4}.                     \tag{4.7}
\]

For completeness, in the even case the product is

\[
 \prod_{j=0}^{h-1}{r-j\over r+j+1};
\]

in the odd case it is

\[
 \prod_{j=1}^{h-1}{r-j\over r+j}.
\]

Expanding `log(1+x)=x+O(x^2)` uniformly for `j<=h=O(sqrt(r))`
gives (4.7).

Finally,

\[
 {A_{d+1}\over\binom{k}{c}}
 =\begin{cases}
   (2d+3)/(r+d+2),&k=2r,\\
   (2d+2)/(r+d+1),&k=2r-1.
  \end{cases}                                           \tag{4.8}
\]

Combining (4.5)--(4.8),

\[
 {qA_{d+1}\over W}
   \longrightarrow {\pi\over2}e^{-\pi/4}<0.717.        \tag{4.9}
\]

On the other hand, the right side of (4.2), divided by `W`, tends to one
because `(q-1)/(r+1)=O(r^(-1/2))`.  Therefore (4.2) holds with
`t=A_(d+1)` for all sufficiently large `k`, and Theorem 4.1 completes the
proof.  \(\square\)

Theorem 4.2 is an exact packing theorem for the entire canonical inventory
of this one primitive type, not an approximate nibble.  It does not choose
the named targets of those blocks and does not pack the other rotor
packages.

## 5. The remaining whole-layer owner input

The exact owner theorem needed by this route can be isolated without any
target or chronology language.

> **Mixed middle-level star-decomposition lemma (external input).**  In the
> canonical regime `r=ceil(k/2)`, `q=d+2` and `q=O(sqrt(k))`, let `A,B` be
> as in (3.5).  For all sufficiently large `k`, the rank-`r` layer has a
> partition into `A` blocks of the form `B(Z,V)` and `B` blocks of the form
> `C(K,U,pi)`.

This single statement would close the owner-only divisibility and matching
row exactly.  It is deliberately not cited as a consequence of the usual
fixed-`F` design theorem: here the uniformity `r`, the pattern size `q`, and
the pattern itself all grow with `k`, while the host has only `k about 2r`
coordinates.  Lemma 2.1 verifies the complete divisibility lattice, but a
uniform absorption theorem in this regime is still required.

Likewise, regularity and pair-codegree alone do not prove this lemma.  For
the `q`-blocks they give

\[
 D=(k-r)\binom r{q-1},\qquad
 {\lambda\over D}={q-1\over r(k-r)},                    \tag{5.1}
\]

which supports an approximate nibble.  An `o(W)` leave is not an
additive-constant result, and no step below promotes (5.1) to an exact
factor.

## 6. The exact named-target deck of a facet block

Fix a `q`-block `B(Z,V)`, put

\[
                         C=Z-V,\qquad |C|=c,             \tag{6.1}
\]

and choose a cyclic order `sigma` of `V`.  Choose `b in C`, choose the
private tag `w in V` of the unique `P` source, and choose a different tag
`h in V-{w}` for the primitive `H` role.  The targets consumed by the local
module are exactly:

\[
\begin{array}{c|c|c}
\text{rank}&\text{targets}&\text{multiplicity}\\ \hline
c &(C-\{b\})+\{w\}&1\\
c+1&C+\{h\}&1\\
c+j,\ 2\le j\le q-2
  &C\cup I,\ I\text{ a cyclic }j\text{-interval of }\sigma&q.
\end{array}                                               \tag{6.2}
\]

#### Proof

The first two rows are the source prefixes of the designated `P` and `H`
roles.  For a high rank, the source window has already refreshed `b`; its
common part is `C=G+{b}`, and its private part consists of `j` consecutive
tags.  Moving around the `q` states gives all `q` cyclic intervals and no
repetition because `1<=j<q`.  \(\square\)

Formula (6.2) is the resource row which an owner matching omits.

### Lemma 6.1 (exact labeling degrees)

Regard a complete labeling of the fixed block as a tuple

\[
                         (b,\sigma,w,h),                 \tag{6.3}
\]

where `b in C`, `sigma` is an oriented cyclic order of `V` modulo rotation,
`w in V` is the tag at the unique `P` position, and `h in V-{w}` designates
the primitive `H`.  The number of labelings is

\[
                         L=cq(q-1)(q-1)!.                \tag{6.4}
\]

For a fixed target `P`, the number `d_B(P)` of block labelings which emit
it is as follows.

\[
\begin{array}{c|c|c|c}
\text{rank}&\text{condition on }P&d_B(P)&d_B(P)/L\\ \hline
c
 &P=(C-\{b\})+\{w\}
 &(q-1)(q-1)!&1/(cq)\\
c+1
 &P=C+\{h\}
 &c(q-1)(q-1)!&1/q\\
c+j,\ 2\le j\le q-2
 &P=C\cup I,\ I\in\binom Vj
 &cq(q-1)j!(q-j)!&q/\binom qj.
\end{array}                                               \tag{6.5}
\]

Targets not satisfying the displayed condition have degree zero.

#### Proof

There are `c` choices for `b`, `(q-1)!` oriented cyclic orders, `q`
choices for `w`, and `q-1` choices for `h`, proving (6.4).  A rank-`c`
target fixes `b,w`, leaving every cyclic order and every `h!=w`.  A
rank-`(c+1)` target fixes `h`, leaving `b,w,sigma`.

For the high row, a fixed `j`-set `I` is an interval in exactly

\[
                         j!(q-j)!                       \tag{6.6}
\]

oriented cyclic orders: equivalently, multiply the total `(q-1)!` orders
by the interval probability `q/binom(q,j)`.  The choices of `b,w,h` are
then free, proving the last row.  \(\square\)

### Lemma 6.2 (exact labeling codegrees)

Distinct targets of the same low rank `c` or `c+1` have codegree zero.
For a rank-`c` target indexed by `(b,w)` and a rank-`(c+1)` target indexed
by `h`, their codegree is `(q-1)!` if `h!=w`, and zero otherwise.

Let `P_I=C union I` be a high target of rank `c+j`.  Its codegree with a
rank-`c` target `(b,w)` is

\[
                         (q-1)j!(q-j)!,                  \tag{6.7}
\]

and its codegree with a rank-`(c+1)` target `C+{h}` is

\[
                         c(q-1)j!(q-j)!.                 \tag{6.8}
\]

For two distinct high targets `P_I,P_J`, possibly at different ranks, put

\[
 N_{\rm cyc}(I,J)=
 \#\{\sigma:I\text{ and }J\text{ are both intervals of }\sigma\}.
\]

Their exact codegree is

\[
                         cq(q-1)N_{\rm cyc}(I,J).        \tag{6.9}
\]

In particular, at rank `r-1` write `I=V-e`, `J=V-f` for two distinct
pairs `e,f in binom(V,2)`.  Then

\[
 N_{\rm cyc}(I,J)=
 \begin{cases}
   2(q-3)!,&|e\cap f|=1,\\
   4(q-3)!,&e\cap f=\varnothing.
 \end{cases}                                             \tag{6.10}
\]

#### Proof

The low rows follow by fixing their displayed parameters and counting the
remaining cyclic orders and choices.  For (6.7), `(b,w)` is fixed, `h` has
`q-1` choices, and (6.6) counts `sigma`.  Equation (6.8) is analogous:
`h` is fixed, while `b` and `w!=h` have `c(q-1)` choices.  Equation (6.9)
is the definition of `N_cyc`, with the independent `b,w,h` choices restored.

At rank `r-1`, emitting `P_I` means that the omitted pair `e` is an edge of
the cyclic order.  If `e,f` meet, contract their three-vertex path; its two
orientations and the remaining vertices give `2(q-3)!` oriented cycles.  If
they are disjoint, contract both edges independently; their four
orientations give `4(q-3)!`.  \(\square\)

For two different owner blocks, label choices are independent.  Therefore
if the same named target `P` is possible in both, the exact number of pairs
of block labelings colliding at `P` is the product of their two degrees in
(6.5).  This is the relevant cross-block codegree for an independent
labeling attempt.

### Lemma 6.3 (exact scalar target capacity)

If `t` facet modules have globally distinct targets and the available named
target inventories at ranks `s` have sizes `N_s`, then

\[
 t\le N_c,\qquad t\le N_{c+1},\qquad
 tq\le N_{c+j}\quad(2\le j\le q-2).                    \tag{6.11}
\]

For the canonical residual deck in the separated range `c>d`, this implies

\[
                         tq\le n_{c+2}=\binom{k}{c+2},  \tag{6.12}
\]

and

\[
                         {n_{c+2}\over W}
                         \longrightarrow e^{-\pi/4}.    \tag{6.13}
\]

#### Proof

Equation (6.2) counts one target at ranks `c,c+1` and `q` targets at every
higher displayed rank, proving (6.11).  In the separated range the Ferrers
correction vanishes at these ranks, and the binomial coefficients increase
up to rank `r`, so the smallest high inventory is at `c+2`.  This proves
(6.12).  The same product expansion as (4.7), now at distance `d-1` from
the middle, proves (6.13).  \(\square\)

Thus a target-feasible primitive inventory occupies asymptotically at most
`e^(-pi/4)W` owners in facet modules, well below the owner-packing capacity
in Theorem 4.1.  In particular, the upper bound `t<=A_(d+1)` used in
Theorem 4.2 is deliberately owner-only; taking equality there would exceed
the rank-`(c+2)` target inventory because the limit in (4.9) is larger than
the limit in (6.13).

## 7. Owner-disjoint blocks can have large target collisions

### Theorem 7.1 (sharp top-rank collision family)

Let `P` be a fixed rank-`(r-1)` target.  In any owner-disjoint collection of
facet blocks whose chosen decks contain `P`, the number of blocks is at most

\[
                         \left\lfloor{k-r+1\over2}\right\rfloor. \tag{7.1}
\]

If there are enough coordinates, this bound is attained.  In particular,
for the middle levels it is `Theta(k)`.

#### Proof

If a block targets `P` at rank `r-1`, (6.2) writes

\[
                         P=C\cup I,qquad |I|=q-2.
\]

The two tags outside `I` are consecutive in the selected cyclic order.  The
two corresponding owners both contain `P`.  Distinct owner blocks in a
matching use disjoint owners, while exactly `k-r+1` rank-`r` owners contain
`P`.  This proves (7.1).

For equality, write `P=C dot-union I` with `|C|=c`, `|I|=q-2`, and partition
as many coordinates outside `P` as possible into pairs `{a_t,b_t}`.  Put

\[
 Z_t=P+\{a_t,b_t\},\qquad V_t=I+\{a_t,b_t\},             \tag{7.2}
\]

and choose a cyclic order of `V_t` in which `a_t,b_t` are adjacent.  Every
block then targets `P`.  Blocks from different pairs are owner-disjoint:
an owner in block `t` contains at least one of `a_t,b_t` and neither member
of any other outside pair, so it cannot equal an owner from block `t'`.
This attains (7.1).  \(\square\)

The same family gives more than a large potential codegree: sufficiently
many of its blocks cannot be labeled target-simply at all.

### Theorem 7.2 (forced rank-`(c+2)` target collision)

Assume `q>=5` and take `m` owner-disjoint blocks from the equality
construction (7.2), so they have a common decomposition

\[
                         P=C\ \dot\cup\ I,qquad |I|=q-2, \tag{7.3}
\]

and two private outside tags per block.  If all module target decks are
globally simple, then necessarily

\[
                         m(q-4)\le\binom{q-2}{2}.        \tag{7.4}
\]

Consequently, if

\[
 m>\left\lfloor{\binom{q-2}{2}\over q-4}\right\rfloor, \tag{7.5}
\]

there is no choice of `b,w,h` and no choice of cyclic orders which removes
all named-target collisions.  For canonical middle-level parameters, the
maximal value `m=floor((k-r+1)/2)=Theta(k)` violates (7.5) for all
sufficiently large `k`, since `q=Theta(sqrt(k))`.

#### Proof

Fix one of the blocks.  Its cyclic order has vertex set

\[
                         I\ \dot\cup\ \{a_t,b_t\}.
\]

At most four cycle edges meet one of the two private vertices, because
each has cycle degree two.  Hence at least `q-4` cycle edges have both ends
in the common set `I`.  By (6.2) with `j=2`, these edges emit at least
`q-4` distinct rank-`(c+2)` targets from the common pool

\[
                         \{C\cup e:e\in\binom I2\},      \tag{7.6}
\]

whose size is `binom(q-2,2)`.  Global target simplicity makes the selected
subsets of this pool disjoint across the `m` modules, giving (7.4).
Neither `b`, `w`, nor the primitive-`H` designation changes these high
targets.  This proves (7.5).

Finally, in the canonical regime `m=Theta(k)` while the right side of
(7.5) is `Theta(q)=Theta(sqrt(k))`.  \(\square\)

The lower bound `q-4` is itself sharp for one block: placing the two private
vertices nonadjacently makes all four of their incident cycle edges
distinct.  Theorem 7.2 is not a no-go for a co-designed owner matching; it
is a sharp warning that no universal theorem can label every already
selected owner-disjoint subinventory afterwards.

More generally, suppose `m` blocks have a common core `C` and their tag
sets all contain a common `u`-set `I`.  Each block has `p=q-u` other tags.
A cyclic order has at most `2p` edges incident with those other tags, and
therefore at least `(2u-q)_+` edges wholly inside `I`.  The same rank-`(c+2)`
pool argument gives the necessary common-core overload cut

\[
                         m(2u-q)_+\le\binom u2.          \tag{7.7}
\]

Theorem 7.2 is the case `u=q-2`.  This cut concerns selected interval
targets, not merely potential-menu intersections.

The owner budget also gives a general potential-collision cap.

### Lemma 7.3 (owner-budget collision cap)

For `2<=j<=q-2`, an owner-disjoint collection can use a fixed rank-`(c+j)`
target in at most

\[
 \left\lfloor
 {\binom{k-c-j}{q-1-j}\over q-j}
 \right\rfloor                                           \tag{7.8}
\]

facet modules.

#### Proof

A module whose deck contains `P` has `P=C union I`, `|I|=j`.  Exactly the
`q-j` owner facets indexed by `V-I` contain `P`.  There are

\[
              \binom{k-(c+j)}{r-(c+j)}
              =\binom{k-c-j}{q-1-j}
\]

rank-`r` owners containing `P`.  Owner-disjointness proves (7.8).
\(\square\)

Thus target conflicts can have growing multiplicity even after the owner
matching has been made exact.

## 8. A proof-safe local collision-avoidance criterion

Suppose some targets have already been used.  For a fresh owner block
`B(Z,V)` and `C=Z-V`, define, for `2<=j<=q-2`,

\[
 {\cal F}_j=\{I\in\binom Vj:C\cup I
                   \text{ is an already used rank-}(c+j)\text{ target}\}.
                                                               \tag{8.1}
\]

### Lemma 8.1 (cyclic-order union bound)

If

\[
             \sum_{j=2}^{q-2}|{\cal F}_j|
                    {q\over\binom qj}<1,                \tag{8.2}
\]

then `V` has a cyclic order for which none of the high targets in (6.2) was
previously used.

#### Proof

Choose a cyclic order uniformly.  By symmetry, a fixed `j`-set is a cyclic
interval with probability

\[
                         {q\over\binom qj},               \tag{8.3}
\]

because every cyclic order has exactly `q` such intervals and all `j`-sets
have the same probability.  The expected number of forbidden intervals is
the left side of (8.2).  If it is below one, some order has zero forbidden
intervals.  \(\square\)

After fixing that order, put

\[
 A_1=\{h\in V:C+\{h\}\text{ is unused at rank }c+1\},   \tag{8.4}
\]

and

\[
 A_0(w)=\{b\in C:(C-\{b\})+\{w\}
                         \text{ is unused at rank }c\}.  \tag{8.5}
\]

If some `w in V` has `A_0(w)` nonempty and `A_1-{w}` nonempty, choosing
`b in A_0(w)` and `h in A_1-{w}` completes a target-disjoint facet module.
This is immediate from (6.2).

Lemma 8.1 is a sufficient local extension theorem, not a consequence of an
arbitrary owner matching.  The forced family in Theorem 7.2 shows why a
global ordering/selection theorem is still needed.

### Theorem 8.2 (an exact LLL-spread criterion)

Let `M` be any owner-block matching.  For a named target `P`, let `mu(P)` be
the number of blocks of `M` in whose potential target menu `P` occurs, and
for a block `B` put

\[
 R_B=\sum_{P\text{ possible in }B}(\mu(P)-1),
 \qquad R=\max_{B\in M}R_B.                              \tag{8.6}
\]

If

\[
                         4e(2R-1)\le(q-1)^2,            \tag{8.7}
\]

then independent choices of complete labelings have positive probability
of producing globally distinct named targets.  In particular, a
target-simple labeling exists.

#### Proof

For every target `P` and every pair of blocks which can emit it, make the
bad event that both blocks emit `P`.  By (6.5), the largest probability
that one block emits one specified target is

\[
                         {2\over q-1};                   \tag{8.8}
\]

it occurs at `j=2` or `j=q-2`.  The two block choices are independent, so
every bad event has probability at most

\[
                         p={4\over(q-1)^2}.              \tag{8.9}
\]

An event involving blocks `B,B'` is independent of every event involving
neither.  By (8.6), its dependency degree is at most

\[
                         D\le R_B+R_{B'}-2\le2R-2.       \tag{8.10}
\]

We recall the elementary symmetric local lemma in the exact form used here:
events of probability at most `p` and dependency degree at most `D` can all
be avoided if `ep(D+1)<=1`.  To verify this form, put `x=1/(D+1)` in the
usual inductive local-lemma criterion

\[
                         p\le x(1-x)^D.
\]

Indeed `(D/(D+1))^D>=e^(-1)`.  The criterion itself follows by induction on
the number of conditioned nonoccurring events: separate the at most `D`
neighbours of the event being bounded, use the induction hypothesis on
each conditional numerator, and cancel the nonneighbour conditions by
independence.  Multiplying the resulting conditional lower bounds gives
positive probability that no event occurs.

Substituting (8.9)--(8.10), condition (8.7) implies `ep(D+1)<=1`, proving
the theorem.  \(\square\)

The criterion is not automatic and cannot be repaired merely by improving
constants.  In the family of Theorem 7.2, every two-subset of the common
`I` is a potential rank-`(c+2)` target in all `m` blocks.  Hence already

\[
                         R\ge\binom{q-2}{2}(m-1),        \tag{8.11}
\]

which is `Theta(q^2 k)` for the maximal middle-level family, whereas (8.7)
requires `R=O(q^2)`.  More decisively, Theorem 7.2 proves that this family
has no target-simple labeling at all once `m` exceeds (7.5).

Thus a conflict-free matching theorem can work only after the owner
matching itself has been made target-spread.

### Lemma 8.3 (exact potential-target conflict degrees)

Fix a rank-`(c+j)` target `P`, with `2<=j<=q-2`.  Among all owner blocks,
the number whose potential high menu contains `P` is exactly

\[
 M_j=\binom{c+j}{j}\binom{k-c-j}{q-j}.                  \tag{8.12}
\]

A fixed block has exactly `binom(q,j)` potential targets at this rank, so
the number of block--target--block conflict incidences through this rank is
at most

\[
                         \binom qj(M_j-1).               \tag{8.13}
\]

For `j=2`, comparison with the owner degree `D` in (5.1) gives

\[
 {M_2\over D}
 ={\binom{c+2}{2}\binom{k-c-2}{q-2}
    \over (k-r)\binom r{q-1}}
 \sim {e^{\pi/4}\over2}\,q                             \tag{8.14}
\]

in the canonical regime.

#### Proof

A block with potential target `P` is determined by its core `C'` and the
part of its centre outside `P`.  Choose `C' in binom(P,c)` and choose
`q-j` points of `[k]-P`; then

\[
 Z'=P\ \dot\cup\ E,
 \qquad V'=(P-C')\ \dot\cup\ E
\]

is the unique resulting block.  This proves (8.12), and (8.13) follows by
summing over the `binom(q,j)` potential targets of one block.

For (8.14), substitute `c=r-q+1` and `a=k-r` to obtain

\[
 {M_2\over D}
 ={\binom{r-q+3}{2}\binom{a+q-3}{q-2}
    \over a\binom r{q-1}}.
\]

Here `a/r->1`, `q/sqrt(r)->sqrt(pi)/2`, and a product expansion gives

\[
 {\binom{a+q-3}{q-2}\over\binom r{q-1}}
 ={q-1\over r}\exp\left({q^2\over r}+o(1)\right).
\]

Together with
`binom(r-q+3,2)/a=(1+o(1))r/2`, this proves (8.14).
\(\square\)

The complete potential-menu conflict system is therefore much denser than
the owner codegree graph.  In fact the `R=O(q^2)` hypothesis of Theorem 8.2
is impossible at every fixed positive primitive density, regardless of how
the owner matching is selected.

### Theorem 8.4 (density obstruction to independent-label LLL)

Let `M` be any matching of `t` owner blocks and put

\[
                         \eta={qt\over W}.               \tag{8.15}
\]

Then the conflict load `R` in (8.6) obeys

\[
 R\ge {t\binom q2^2\over\binom{k}{c+2}}-\binom q2.     \tag{8.16}
\]

Consequently, along any canonical sequence on which `eta` is bounded below
by a positive constant,

\[
                         R\ge
 \left({\eta e^{\pi/4}\over4}+o(1)\right)q^3.          \tag{8.17}
\]

Thus (8.7) fails by a factor of order `q`; neither the symmetric LLL above
nor a greedy rule which forbids all potential-menu overlaps can reach
`t=Theta(W/q)`.

#### Proof

At rank `c+2`, let `mu(P)` be the number of selected blocks in whose
potential menu `P` occurs.  Every block has `s=binom(q,2)` such potential
targets, so

\[
                         \sum_P\mu(P)=ts.                \tag{8.18}
\]

The sum, over selected blocks, of their rank-`(c+2)` contributions to
`R_B` is

\[
                         \sum_P\mu(P)(\mu(P)-1).         \tag{8.19}
\]

Cauchy--Schwarz over the `binom(k,c+2)` possible targets gives

\[
 \sum_P\mu(P)(\mu(P)-1)
 \ge{t^2s^2\over\binom{k}{c+2}}-ts.
\]

Some block has at least the average contribution, proving (8.16).  Now use
`t=eta W/q`, `s=(1+o(1))q^2/2`, and (6.13) to obtain (8.17).

Finally, a strategy forbidding all potential overlaps would require
`t binom(q,2)<=binom(k,c+2)`, hence only `t=O(W/q^2)`.  This is already a
factor `q` below the required positive-density scale.  \(\square\)

The obstruction concerns *independent post-labeling*.  A selected cyclic
order uses only `q` of its `binom(q,2)` potential rank-`(c+2)` targets, so a
joint block-and-order theorem may still succeed.

> **Desired facet interval-spread input for the fixed target allocation.**
> Let `t` be the canonical primitive count satisfying the scalar capacities
> (6.11).  There exist pairwise owner-disjoint blocks
> `B_i=B(Z_i,V_i)`, oriented cyclic orders `sigma_i`, and choices
> `b_i,w_i,h_i` such that, with `C_i=Z_i-V_i`,
>
> \[
> (i,I)\longmapsto C_i\cup I
> \]
>
> is injective for the cyclic `j`-intervals of every `sigma_i` and every
> `2<=j<=q-2`, while the two low targets
> `(C_i-{b_i})+{w_i}` and `C_i+{h_i}` are also globally injective in their
> respective rank species.  Every emitted target lies in the allocated
> residual family and avoids the protected/preused target bank.

This desired input is not asserted for every residual/protected allocation
satisfying only the scalar capacities.

This is exactly a matching of size `t` in the owner-plus-named-target
resource hypergraph after the primitive type inventory is fixed.  It adds
no component, residence, upper, or compiler assertion.  Theorem 4.2 proves
the owner projection; Theorem 7.2 proves that block selection and interval
selection cannot be separated; Theorem 8.4 proves that an independent-menu
strategy satisfying the displayed symmetric LLL criterion cannot establish
it at positive density.  This does not exclude every asymmetric, lopsided or
correlated LLL.  Lemma 8.1 remains a useful sufficient sequential
certificate for any proposed spread construction, but no proof of the
interval-spread input is claimed here.

## 9. Exact implication and honest boundary

The corrected triangular pull-clock theorem supplies only a symmetric
fractional marked circulation.  The integral-age theorem says that, once
integer type multiplicities have been chosen, the successor table is a TU
transportation problem; it does not choose named owners or named target
chains.  The aggregate conductor theorem separately supplies an exact
integer rotor-package multiset for the canonical profile at `k>=31`.

The results here give the following genuine zero-loss implication for the
primitive packet.

### Corollary 9.1 (target-exactness is the remaining primitive row)

For all sufficiently large canonical `k`, fix any aggregate decomposition
and let `t` be its number of primitive `g_(d-1,d+1)` packets.  Suppose its
short-role inventory reserves `d` short buffers for each primitive.  There
is an owner-disjoint family of `t` length-`q` facet absorbers.  If one such
family can be cyclically ordered and parametrized so that the target rows
(6.2) partition the allocated named target inventory, then every primitive
packet has a one-copy literal owner- and target-simple lift with **no added
occurrences**.

#### Proof

By (4.4), `t<=A_(d+1)`, so Theorem 4.2 supplies the owner-disjoint blocks.
Apply the length-`q` sharp facet construction to each block.  Owner
disjointness gives the owner degree-one row, and the assumed partition of
(6.2) gives every named-target degree-one row.  Each module is already a
literal directed cycle, so their disjoint union is the required one-copy
lift of this packet inventory.  No occurrence is appended.
\(\square\)

This closes the primitive owner-packing row unconditionally and reduces its
zero-loss labelled lift to the one global named-target selection.  It does
**not** by itself imply `nu(k)<=B(k)+O(1)`: the other rotor packages,
component fusion, upper interval deck, residence, protected pins, and
compiler cap remain separate gates.  The mixed middle-level
star-decomposition lemma is needed only by a route that attempts to cover
the whole owner layer with these two absorber types.

In particular, the low codegree (5.1) justifies neither an exact owner
factor nor the target partition.  Replacing either missing theorem by an
`o(W)`-leave nibble would leave an `o(W)` occurrence debt, not an additive
constant.

## 10. Dependencies

The length-`q` facet absorber and its owner degrees are in
`MATH_THEOREM_OFHT_EXACT_CYCLE_HYPERGRAPH_FUNCTIONAL_HALL_AND_POINTED_FACE_20260801.md`,
Section 7, with the literal construction proved in
`MATH_THEOREM_R_PRIMITIVE_MIXED_ROTOR_SHARP_BUFFERED_ONE_COPY_LIFT_20260801.md`.
The stationary fractional profile is proved in
`MATH_THEOREM_TRIANGULAR_PULL_CLOCK_CORRECTED_20260801.md`.
The fixed-multiplicity TU theorem and the warning against generic one-copy
rounding are in
`MATH_THEOREM_INTEGRAL_AGE_CIRCULATION_NORMALITY_AND_LATTICE_OBSTRUCTIONS_20260801.md`.
The exact canonical aggregate package decomposition is in
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`.
