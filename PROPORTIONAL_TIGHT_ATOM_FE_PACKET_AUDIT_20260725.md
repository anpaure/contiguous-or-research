# Proportional tight atoms: blocker incidence and the central-packet blindness obstruction

Date: 2026-07-25

Method: pure mathematics only.  No web search, finite search, solver, or
computer experiment is used.

## 0. Verdict

This note audits the proposed route from the `b` shortest augmenting paths
in the middle inclusion graph to the cylinder-fibre inequality (FE) in
`PROPORTIONAL_TIGHT_ATOM_MATCHING_EXPANSION_20260725.md`.

Two exact facts are proved.

1. There is a closed blocker-incidence formula for the boundary fibres.
   A near-saturating atom matching blocks a `1-o(1)` fraction of all
   boundary-core candidates, counted over all ordered boundary types.
   The formula supplies no positive lower bound on the number of completely
   unblocked cores in one type.
2. A shortest-path augmentation in the one-parent middle inclusion graph
   need not retain even the first physical compatibility condition.  Every
   perfect middle matching contains `b` flags no two of which can be
   consecutive in a tight atom.  Starting from the empty atom matching,
   these may be chosen as `b` shortest (length-zero) augmenting paths.

Consequently the central shortest-path operation does not itself constrain
the blocker sets in (FE) and does not provide central ladders which can be
completed.  A proof of (FE) would have to use an additional two-parent
ladder/interval expansion theorem; it cannot be obtained from the stated
one-parent augmentation plus transitivity or first-moment averaging.

This is a no-go for that inference, not a counterexample to (FE) for every
shortest-path packet and not a counterexample to the proportional atom
matching lemma.  No positive proof of (FE) is obtained here.

## 1. Parameters and the exact boundary-candidate system

Use

\[
n=2m+1,\qquad W=\binom nm,\qquad
b=\lfloor m^{3/4}\rfloor,\qquad
p=\left\lfloor\frac Wb\right\rfloor,
\]

\[
N_q=\binom n{m+q},\qquad
b_q=\left\lfloor\frac{N_q}{p}\right\rfloor,
\qquad -H\le q\le H+1,
\]

and

\[
\kappa=\sum_{q=-H}^{H+1}b_q.
\tag{1.1}
\]

Let `Omega` be the collection of all boundary-core candidates

\[
\Omega=\{(y,C):y:Y_{\rm pos}\hookrightarrow[n],\ 
 C\in\tbinom{[n]\setminus\operatorname{im}y}{c}\}.
\]

With the notation of the source report,

\[
G=(n)_R,\qquad F=\binom{2c}{c},\qquad |\Omega|=GF.
\tag{1.2}
\]

The candidate `(y,C)` denotes the proportional atom `e(y,C)`.  The
candidate family is coordinate-transitive, and every candidate contains
exactly `b_q` vertices of rank `m+q`.

## 2. Exact blocker-incidence formula

Let `M_0` be any atom matching of size `t`.  For `omega=(y,C) in Omega`,
put

\[
X_{M_0}(\omega)
=|e(y,C)\cap V(M_0)|.
\tag{2.1}
\]

Because `M_0` is a matching, this is simultaneously the number of target
vertices of `e(y,C)` already occupied by `M_0`; no occurrence multiplicity
is hidden in (2.1).

### Theorem 2.1 (exact global blocker incidence)

One has

\[
\boxed{
\sum_{\omega\in\Omega}X_{M_0}(\omega)
=tGF\sum_{q=-H}^{H+1}\frac{b_q^2}{N_q}.}
\tag{2.2}
\]

If

\[
Z(M_0)=|\{\omega\in\Omega:X_{M_0}(\omega)=0\}|
\tag{2.3}
\]

is the total number of unblocked boundary-core candidates over all ordered
types, then

\[
\boxed{
Z(M_0)\le
GF\left(1-
\frac{t}{\kappa}
\sum_{q=-H}^{H+1}\frac{b_q^2}{N_q}
\right).}
\tag{2.4}
\]

Writing `Q=2H+2` for the number of ranks,

\[
\boxed{
\frac{\kappa-Q}{p}
\le
\sum_{q=-H}^{H+1}\frac{b_q^2}{N_q}
\le\frac{\kappa}{p}.}
\tag{2.5}
\]

In particular, if `M` has size `p-ell`, `J subseteq M`, and
`M_0=M\setminus J`, then

\[
\boxed{
\frac{Z(M\setminus J)}{GF}
\le
\frac{\ell+|J|}{p}+\frac{2H+2}{\kappa}.}
\tag{2.6}
\]

There is also the sharper central-rank inequality

\[
\boxed{
\frac{Z(M\setminus J)}{GF}
\le
\frac{W-(p-\ell-|J|)b}{W}
=\frac{\rho+(\ell+|J|)b}{W},}
\qquad W=pb+\rho,\quad0\le\rho<b.
\tag{2.7}
\]

#### Proof

Fix a rank `q`.  Coordinate transitivity and incidence counting show that
every `S in binom([n],m+q)` occurs in exactly

\[
d_q^{\Omega}=\frac{GFb_q}{N_q}
\tag{2.8}
\]

candidates.  The matching `M_0` occupies exactly `tb_q` distinct vertices
of that rank.  Summing (2.8) over its occupied vertices, and then over all
ranks, proves (2.2).

Alternatively sum available incidences.  There are `N_q-tb_q` available
vertices at rank `q`, so the total number of available target incidences
over `Omega` is

\[
\sum_q(N_q-tb_q)\frac{GFb_q}{N_q}
=GF\left(\kappa-t\sum_q\frac{b_q^2}{N_q}\right).
\tag{2.9}
\]

Every completely unblocked candidate contributes all `kappa` of its target
incidences to (2.9).  This proves (2.4).

For (2.5), write

\[
N_q=p(b_q+\theta_q),\qquad0\le\theta_q<1.
\]

Then

\[
0\le\frac{b_q}{p}-\frac{b_q^2}{N_q}
=\frac{b_q\theta_q}{p(b_q+\theta_q)}<\frac1p.
\tag{2.10}
\]

Sum (2.10) over the `Q` ranks and use (1.1).  Substituting
`t=p-ell-|J|` in (2.4) and using the lower bound in (2.5) gives (2.6).

For (2.7), use only rank zero, where `N_0=W` and `b_0=b`.  A completely
unblocked candidate uses `b` available middle vertices.  The total number
of available middle incidences in `Omega` is

\[
[W-(p-\ell-|J|)b]\frac{GFb}{W}.
\]

Divide by `b`.  This proves (2.7).  ∎

### Consequence 2.2 (what averaging can and cannot say)

At the intended stopping scale

\[
\ell\asymp \frac{p}{\sqrt m\,\omega_m},
\qquad |J|=O(\kappa\omega_m),
\]

the right side of (2.6) is `o(1)`.  Thus almost every boundary-core
candidate is blocked.  More importantly, (2.2) is an identity for the
actual interval fibres, not an independent-residual heuristic.  It gives
only a global average over boundary types.  It contains no lower bound for

\[
\max_y |\{C:e(y,C)\cap V(M\setminus J)=\varnothing\}|,
\]

which is the quantity in (FE).  A proof of (FE) must therefore establish a
new concentration of the rare survivors into at least one type; uniform
type averaging and transitivity do not establish it.

## 3. The missing two-parent central law

Write the central targets of a physical atom as

\[
P_i=\{x_i,\ldots,x_{i+m-1}\},\qquad
U_i=\{x_i,\ldots,x_{i+m}\},\qquad0\le i<b.
\tag{3.1}
\]

The one-parent matching used in the shortest-path construction consists of

\[
P_i\subset U_i\qquad(0\le i<b).
\tag{3.2}
\]

But physicality also requires

\[
P_{i+1}\subset U_i\qquad(0\le i<b-1).
\tag{3.3}
\]

Thus the central projection of one physical atom is the full alternating
ladder

\[
P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1},
\tag{3.4}
\]

not the `b` independent edges in (3.2).

Call two inclusion flags `(A,B)` and `(A',B')`, with
`|A|=|A'|=m`, *cross-compatible* if

\[
A'\subset B\quad\hbox{or}\quad A\subset B'.
\tag{3.5}
\]

Consecutive same-start flags in every physical atom are cross-compatible.

### Theorem 3.1 (every perfect middle matching has a large incompatible submatching)

Let `Q` be any perfect matching of the middle inclusion graph between
`binom([n],m)` and `binom([n],m+1)`.  Then `Q` contains a submatching
`R` of size at least

\[
\boxed{\frac{W}{2m+1}}
\tag{3.6}
\]

whose distinct flags are pairwise not cross-compatible.  In particular,
for all sufficiently large `m`, `R` contains `b` flags, and no two of
those `b` flags can be consecutive same-start flags in one proportional
atom.

#### Proof

Make a conflict graph on the `W` edges of `Q`, joining
`e=(A,B)` to `e'=(A',B')` when (3.5) holds.  The upper set `B` has exactly
`m+1` lower neighbours.  One is `A`; each of the other at most `m` lower
neighbours is the lower endpoint of one edge of `Q`.  Thus at most `m`
other matching edges satisfy `A' subset B`.  Symmetrically, `A` is
contained in exactly `m+1` upper sets, one of which is `B`, so at most `m`
other matching edges satisfy `A subset B'`.  The conflict graph therefore
has maximum degree at most `2m`.

Greedy independent-set selection gives an independent set of size at
least `W/(2m+1)`.  Since `W/(2m+1)>b` for all sufficiently large `m`,
choose any `b` of its edges.  Independence is exactly pairwise failure of
(3.5).  Equation (3.3) shows that no two can be consecutive in a physical
atom.  ∎

### Corollary 3.2 (the shortest central augmentation is not a lift certificate)

Start with the empty atom matching.  Then its one-parent middle matching is
empty, and every edge of `Q` is a length-zero augmenting component in the
symmetric difference.  The `b` edges supplied by Theorem 3.1 may therefore
be chosen among the `b` shortest augmenting paths.  They add exactly the
central quota of one atom, but they cannot be the same-start central flags
of any physical atom.

Hence the quantitative facts

\[
\text{net central gain }b,
\qquad
\text{number of touched old atoms }0
\]

do not imply even central-ladder realizability of the gained flags.  The
failure occurs before any Gaussian-depth or boundary-core completion is
considered.

This corollary does not say that the empty matching lacks an atom extension;
of course it has many.  It proves the exact logical point: the particular
shortest-path output is not a physical certificate, and its path-length
bound supplies no restriction on the fibre blockers used in (FE).

### Proposition 3.3 (exact fragmentation after a `b`-path switch)

There is nevertheless an exact two-parent object canonically left by the
switch.  Let `J` be the owners of all old one-parent flags deleted on the
chosen `b` augmenting paths.  Let `R'` consist of

1. every old same-start flag of an atom in `J` which was not deleted, and
2. every new perfect-matching flag inserted on the chosen paths.

Then `R'` is a matching of size

\[
|R'|=(|J|+1)b.
\tag{3.7}
\]

Let `L_J` be the old cross-edge matching

\[
P_{i+1}\subset U_i
\qquad(0\le i<b-1)
\]

from the atoms in `J`.  Thus

\[
|L_J|=|J|(b-1).
\tag{3.8}
\]

Regard `R' union L_J` as an edge-coloured bipartite multigraph if an
`R'`-edge and an `L_J`-edge happen to have the same endpoints.  Every
component is an alternating cycle or an alternating path beginning and
ending with an `R'`-edge, and the number of path components is exactly

\[
\boxed{|R'|-|L_J|=|J|+b.}
\tag{3.9}
\]

#### Proof

Switching along augmenting paths preserves coverage of every old endpoint
on the paths and covers the two formerly unmatched endpoints of each path.
Adding the untouched same-start flags from the owners in `J` therefore
gives (3.7), and every central vertex of every atom in `J` is incident with
one `R'`-edge.  The old cross edges form a matching on a subset of those
vertices, proving (3.8).

Consequently every vertex of the two-coloured union has one incident
`R'`-edge and at most one incident `L_J`-edge.  Its components have the
stated alternating form.  A cycle contains equally many edges of the two
colours.  Every path begins and ends in colour `R'` and therefore contains
one more `R'`-edge.  Summing the colour-count difference over components
proves (3.9).  ∎

The desired `|J|+1` central atom ladders would instead require a cross-edge
matching `L^*` of size

\[
(|J|+1)(b-1)=|J|(b-1)+(b-1)
\tag{3.10}
\]

such that `R' union L^*` is the disjoint union of exactly `|J|+1`
alternating paths, each containing exactly `b` `R'`-edges.  Moreover each
path must obey the injective FIFO law of a sliding word: along its lower
Johnson path, departed coordinates are distinct members of the initial
window and arriving coordinates are distinct coordinates outside that
window.  Arbitrary alternating paths need not obey this law.

Thus the one-parent switch has an exact, audited **cross-link cardinality
deficit** of `b-1`: any successful fixed-vertical resegmentation must use
at least `b-1` links outside the old natural seam set.  This does not say
that adding an arbitrary `b-1` links, or even some `b-1` links without
discarding old ones, is sufficient; the old union may already have cycles
or components of the wrong lengths.  Establishing a full cross matching
with balanced component lengths and FIFO compatibility is a necessary
central precursor to (FE).

The FIFO condition just invoked has the following finite exact form.

### Lemma 3.4 (exact injective-window criterion for one central ladder)

Let

\[
(A_0,B_0),(A_1,B_1),\ldots,(A_{r-1},B_{r-1})
\tag{3.11}
\]

be the edges, in some order, of an inclusion matching, with
`|A_i|=m`, `|B_i|=m+1`, where

\[
A_{i+1}\subset B_i\qquad(0\le i<r-1),
\tag{3.12}
\]

and assume `r<=m`.  Put

\[
d_i=A_i\setminus A_{i+1}\quad(0\le i<r-1),
\qquad
a_i=B_i\setminus A_i\quad(0\le i<r).
\tag{3.13}
\]

Then (3.11) is the central ladder of an injective tight word, in the given
order, if and only if

\[
\boxed{
d_0,\ldots,d_{r-2}\text{ are distinct members of }A_0,
\quad
a_0,\ldots,a_{r-1}\text{ are distinct members of }[n]\setminus A_0.}
\tag{3.14}
\]

#### Proof

In an injective tight word, the transition from `A_i` to `A_{i+1}` removes
the coordinate in word position `i` and inserts the coordinate in position
`i+m`.  Before `r<=m` transitions have occurred, every removed coordinate
belongs to the initial window, while every inserted coordinate lies outside
it; injectivity gives both distinctness assertions.

Conversely, order the initial window `A_0` by putting

\[
d_0,d_1,\ldots,d_{r-2}
\]

first, followed by the other elements of `A_0` in any order, and append

\[
a_0,a_1,\ldots,a_{r-1}.
\]

Condition (3.14) makes this word injective.  Since `A_i` and `A_{i+1}`
are distinct `m`-subsets of the same `(m+1)`-set `B_i`, one has

\[
B_i=A_i\cup A_{i+1},qquad
A_{i+1}=(A_i\setminus\{d_i\})\cup\{a_i\}
\quad(i<r-1).
\]

Induction now shows that its length-`m` window at start `i` is `A_i`, and
the length-`m+1` window there is `B_i`; the last assertion uses the appended
coordinate `a_{r-1}`.  ∎

## 4. Exact correction to the central augmentation statement

Theorem 4.1 of the source report chooses the `b` shortest among `u`
augmenting paths.  Its statement therefore requires

\[
\boxed{u=\rho+\ell b\ge b.}
\tag{4.1}
\]

In the iteration regime this is automatic because `ell>=1`.  It is not
automatic for `ell=0`, when `u=rho<b`.  The theorem should be stated for
`ell>=1` (or directly under (4.1)).  No later claimed iteration is affected.

## 5. Precise proved/unsupported boundary

### Proved

1. Equations (2.2)--(2.7) are exact for the actual boundary-type fibres
   and every actual atom matching.
2. Near saturation blocks a `1-o(1)` fraction of all boundary-core
   candidates, globally over types.
3. The one-parent shortest-path augmentation can output `b` gained flags
   with no two physically consecutive, even when all paths have minimum
   possible length zero.
4. The central augmentation theorem needs the harmless explicit hypothesis
   `u>=b`.

### Not proved

1. No example here disproves (FE) for every permissible choice of the
   shortest-path packet of a large deficient atom matching.
2. No lower bound of `|J|+1` unblocked cores in one boundary type is proved.
3. No matching of `|J|+1` full atoms is constructed.

The additional theorem genuinely needed after the central count is a
**two-parent ladder-coherent interval expansion theorem**: the exchange
must preserve or reconstruct (3.3)--(3.4) and then control every forced
union/intersection target and the endpoint collar.  This is strictly more
information than the one-parent path lengths, their touched-owner set `J`,
the `O(1/m)` local row sum, or boundary-type transitivity.
