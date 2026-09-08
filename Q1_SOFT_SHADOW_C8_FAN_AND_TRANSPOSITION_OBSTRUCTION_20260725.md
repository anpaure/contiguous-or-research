# Depth-one soft shadows: exact rectangle averages, one-token fans, and the transposition obstruction

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The depth-one endpoint ledger and the ambient `C_8` rectangle lattice fit
together exactly, but they do not by themselves give a currently supported
descent.

1. For a uniformly random coordinate transposition, the expected number of
   old holes sent to old duplicate targets is the actual Johnson boundary

   \[
    {e_J(\mathcal H,\mathcal D_2)\over\binom n2},
   \]

   not the full-relabel mean `|H||D_2|/N_1`.  The endpoint multiplicity cap
   controls `|D_2|` but supplies no Johnson-boundary estimate.
2. For a fixed hole, the exact average change under all algebraic
   rectangles is determined by the load-one density in its Johnson
   neighborhood and the hole density in its distance-two sphere.  Global
   duplicate mass alone cannot make that average negative.
3. There are integral, capped, point-regular depth-one load profiles of the
   correct total mass in which holes have no duplicate Johnson neighbors.
   They are not asserted to be exact-wreath shadows; they prove that the
   scalar endpoint and point-margin ledgers alone cannot imply a
   transposition supply.
4. On any fixed-core bipartite sector, every point-balanced deficit has an
   exact one-token rectangle schedule.  If the rectangles in that schedule
   admit sequentially legal exact-factor `C_8` lifts, the schedule transforms
   the current factor to the prescribed balanced load.  Thus, in this
   sector, load nonnegativity is solved and the remaining obstruction is
   precisely lift support in the current exact-factor fibre.

## 1. Endpoint graph and the duplicate cap

Put

\[
 n=2m+1,\qquad r=m-1,
 \qquad \mathcal R=\binom{[n]}r.
\]

For an exact wreath factor `F`, let `mu(R)` be the number of cyclic
rank-`r` occurrences of `R`.  Subdivide every tight Johnson edge of every
wreath at its lower intersection colour.  Equivalently, make a graph
`G_F` on `R` by letting each middle owner join its predecessor and successor
facets.  Then

\[
 \boxed{\deg_{G_F}(R)=2\mu(R).}
 \tag{1.1}
\]

The incident middle extensions at one `R` use distinct points of
`[n] setminus R`, so

\[
 \boxed{0\le\mu(R)\le M_m:=\left\lfloor{m+2\over2}\right\rfloor.}
 \tag{1.2}
\]

Also

\[
 \sum_R\mu(R)=W,
 \qquad
 \sum_{R\ni x}\mu(R)={rW\over n}\quad(x\in[n]).
 \tag{1.3}
\]

Let

\[
 \mathcal H=\{R:\mu(R)=0\},
 \qquad
 \mathcal D_2=\{R:\mu(R)\ge2\},
 \qquad h=|\mathcal H|,quad d_2=|\mathcal D_2|.
\]

The exact excess ledger gives

\[
 \sum_{R\in\mathcal D_2}(\mu(R)-1)=h+W-N_1,
\]

and hence

\[
 \boxed{
 d_2\ge {h+W-N_1\over M_m-1}.}
 \tag{1.4}
\]

This is a cardinality statement.  It contains no spatial information in
the Johnson graph on `R`.

## 2. Full relabeling versus one transposition

For a coordinate permutation `sigma`, put

\[
 A_\sigma^{(2)}
 =|\{R\in\mathcal H:\mu_{\sigma F}(R)\ge2\}|.
\]

Uniform averaging over all of `S_n` gives

\[
 \mathbb E_{\sigma\in S_n}A_\sigma^{(2)}
 ={h d_2\over N_1}.
 \tag{2.1}
\]

The transposition average is different.

### Proposition 2.1 (exact transposition supply)

Let `tau` be uniform over the `binom(n,2)` coordinate transpositions.  Then

\[
 \boxed{
 \mathbb E_\tau A_\tau^{(2)}
 ={e_J(\mathcal H,\mathcal D_2)\over\binom n2},}
 \tag{2.2}
\]

where `e_J` is the number of Johnson edges with one endpoint in `H` and
the other in `D_2`.

#### Proof

For `R in H`,

\[
 \mu_{\tau F}(R)=\mu_F(\tau^{-1}R).
\]

A transposition either fixes `R` or sends it to one Johnson neighbor.  A
fixed `R` remains a hole.  For each Johnson neighbor `S` of `R`, the unique
transposition exchanging the two coordinates of `R triangle S` maps `R`
to `S`.  Sum over `R in H`. \(\square\)

Thus (1.4) cannot be inserted into (2.2).  A positive transposition route
requires a new estimate of the form

\[
 e_J(\mathcal H,\mathcal D_2)
 \gg {h d_2\over N_1}\binom n2,
 \tag{2.3}
\]

or at least the weaker scale needed by the component-switch drift.  Such an
estimate is not a consequence of the known endpoint cap.

## 3. Exact rectangle average at one hole

Fix `R in H`.  An elementary rectangle having `R` on its positive diagonal
has the form

\[
 \Delta=e_R+e_S-e_T-e_U,
 \tag{3.1}
\]

where

* `S` is at Johnson distance two from `R`; and
* `T,U` are Johnson neighbors of `R`.

Choose uniformly from all such oriented rectangles.  The opposite cell
`S` is uniform on the distance-two sphere of `R`, and each of the two
negative cells is uniform on the Johnson neighborhood of `R`.  Put

\[
 h_2(R)={|\mathcal H\cap\Gamma_2(R)|\over|\Gamma_2(R)|},
 \qquad
 \ell_1(R)={|\{T\sim R:\mu(T)=1\}|\over r(n-r)}.
 \tag{3.2}
\]

If the two negative cells have positive load, the exact hole-count change
is

\[
 \boxed{
 \Delta H
 =-1-\mathbf1_{\{S\in\mathcal H\}}
 +\mathbf1_{\{\mu(T)=1\}}
 +\mathbf1_{\{\mu(U)=1\}}.}
 \tag{3.3}
\]

Ignoring rectangles which are load-illegal because a negative cell is a
hole, the formal unconditioned average is

\[
 \boxed{\mathbb E\Delta H=-1-h_2(R)+2\ell_1(R).}
 \tag{3.4}
\]

In particular:

* two duplicate negative cells always give strict descent;
* one duplicate and one load-one negative give descent only when the
  opposite positive cell is also a hole; and
* two load-one negative cells never give strict descent.

The global lower bound (1.4) says nothing about either local quantity in
(3.2).  This is the exact failure of the naive rectangle average.

There is also an exact version with legality included.  Let
`R_+(R)` be the oriented rectangles in (3.1) whose two negative cells have
positive load, choose uniformly from `R_+(R)`, and put

\[
 h^{\rm leg}_2(R)=\Pr(S\in\mathcal H),
 \qquad
 d^{\rm leg}_-(R)=
 \mathbb E\bigl[
  \mathbf1_{\{T\in\mathcal D_2\}}+
  \mathbf1_{\{U\in\mathcal D_2\}}
 \bigr].
 \tag{3.5}
\]

On a legal rectangle a positive negative-cell load is either one or at
least two, so (3.3) is equivalently

\[
 \boxed{
  \mathbb E[\Delta H\mid\mathcal R_+(R)]
  =1-h^{\rm leg}_2(R)-d^{\rm leg}_-(R).}
 \tag{3.6}
\]

Thus the exact one-hole fan criterion is

\[
 \boxed{
  h^{\rm leg}_2(R)+d^{\rm leg}_-(R)>1.}
 \tag{3.7}
\]

This criterion exposes both missing inputs: legality can bias the opposite
cell, and duplicate mass must be visible on the two legal negative slots.

### 3.1 A packet-forced legal rectangle inventory

The cyclic packetization does force many legal source pairs, although it
does not force them to point toward holes.  In one oriented row
`(x_j)_(j in Z_n)`, write

\[
 C_j=\{x_j,x_{j+1},\ldots,x_{j+m-2}\}.
\]

Put

\[
 K_j=\{x_{j+2},\ldots,x_{j+m-2}\},
\]

and

\[
 R_j=K_j\cup\{x_j,x_{j+m-1}\},
 \qquad
 S_j=K_j\cup\{x_{j+1},x_{j+m}\}.
\]

Then

\[
 \boxed{
  e_{R_j}+e_{S_j}-e_{C_j}-e_{C_{j+2}}}
 \tag{3.8}
\]

is an elementary rectangle.  Both negative cells are actual cyclic
first-shadow occurrences, so (3.8) is load-legal in the shadow of the
current factor.  Across all rows there are exactly `W` labelled rectangles
of this form.

Let `xi(S)` be the number of times `S` occurs among the two positive cells
`R_j,S_j` of this labelled inventory, and let

\[
 \mathcal L_1=\{S:\mu(S)=1\}.
\]

Cyclic translation inside each row also gives the exact margins

\[
 \sum_S\xi(S)=2W,
 \qquad
 \sum_{S\ni x}\xi(S)={2rW\over n}\quad(x\in[n]).
 \tag{3.8a}
\]

Every labelled occurrence `C_j` is a negative cell in exactly two
rectangles, at indices `j` and `j-2`.  Therefore the sum of the hole-count
changes obtained by evaluating all labelled rectangles at the original
load is exactly

\[
 \boxed{
  \sum_{(C,j)}\Delta H(C,j)
  =2|\mathcal L_1|-\sum_{S\in\mathcal H}\xi(S).}
 \tag{3.9}
\]

Thus this forced inventory contains a strictly improving rectangle whenever

\[
 \sum_{S\in\mathcal H}\xi(S)>2|\mathcal L_1|.
 \tag{3.10}
\]

Equation (3.9) is exact, but (3.10) is a very strong exposure demand.  The
endpoint ledger fixes the first term and gives no lower bound on the cross
exposure `xi(H)`.  Moreover, load-legality of (3.8) still does not imply
that the rectangle is the increment of a currently alternating exact-factor
`C_8`.  Hence packetization supplies a macroscopic legal load inventory,
but two additional bridges remain: positive exposure to holes and physical
exact-factor lift support.

### 3.2 All interior facets and the exact long-exchange drift

There is a larger packet-forced inventory whose positive histogram is
completely explicit.  For every row start `j` and
`1<=t<=m-2`, put

\[
\begin{aligned}
 A_{j,t}&=C_j-\{x_{j+t}\}+\{x_{j+m-1}\},\\
 B_{j,t}&=C_{j+t+1}-\{x_{j+m-1}\}+\{x_{j+t}\}.
\end{aligned}
 \tag{3.11}
\]

Then

\[
 L_{j,t}=e_{A_{j,t}}+e_{B_{j,t}}-e_{C_j}-e_{C_{j+t+1}}
 \tag{3.12}
\]

is a point-balanced two-occurrence **long symmetric exchange**.  Both
negative occurrences are present in the current row, so (3.12) is a legal
nonnegative load move.  For `t=1` it is the elementary rectangle (3.8).
For `t>1` it is not itself an elementary four-cell rectangle: its two
negative cells are at Johnson distance `t+1`.

Let `M_j={x_j,...,x_{j+m-1}}`.  The first positive cell is the interior
facet

\[
 A_{j,t}=M_j-\{x_{j+t}\},
\]

and the second is

\[
 B_{j,t}=M_{j+t}-\{x_{j+m-1}\},
\]

whose deleted position in `M_{j+t}` is `m-1-t`.  Hence, as `(j,t)` varies,
every interior facet incidence `(M,R)` occurs once among the `A` cells and
once among the `B` cells.

For a lower target `R`, there are exactly `m+2` parent middle sets.  Exactly
`2 mu(R)` of those parent incidences are the two endpoint facets selected
by the current wreath cycles.  Therefore the number of interior parent
incidences is `m+2-2mu(R)`.  If `Xi` is the complete positive histogram of
(3.12), we obtain the pointwise identity

\[
 \boxed{
  \Xi(R)=2\bigl(m+2-2\mu(R)\bigr).}
 \tag{3.13}
\]

This is an endpoint statistic; it does not require the depth-two load.

There are `W(m-2)` labelled long exchanges.  Every pointed cyclic
first-shadow occurrence is a negative cell `m-2` times in the first slot
and `m-2` times in the second slot.  A negative cell creates a hole exactly
when its old target has load one.  A positive cell repairs a hole exactly
when its target lies in `H`.  Summing over the whole inventory and using
(3.13) gives

\[
 \boxed{
  \sum_{(C,j,t)}\Delta H(C,j,t)
  =2(m-2)|\mathcal L_1|-2(m+2)|\mathcal H|.}
 \tag{3.14}
\]

Consequently this inventory contains a strictly hole-improving long
exchange whenever

\[
 \boxed{
  (m+2)|\mathcal H|>(m-2)|\mathcal L_1|.}
 \tag{3.15}
\]

The criterion is exact and usually demanding: a small positive density of
holes does not make the uniform long-exchange average negative.

#### Depth-two phase refinement

Although the full histogram `Xi` is already determined by `mu_1`, the
nearest-interior histogram `xi` from (3.8) has a useful depth-two
description.  Let

\[
 D_j=\{x_j,\ldots,x_{j+m-3}\}
\]

be a pointed depth-two interval.  Its `m+3` possible one-point extensions
are ordered by the complementary cyclic arc.  Define `eta_a(R)` to count
the extensions

\[
 D_j\cup\{x_{j+a}\}=R,
 \qquad a\in\{m-2,m-1,\ldots,2m\}.
\]

Then, pointwise,

\[
 \boxed{
  U\mu_2:=\sum_{D\subset R}\mu_2(D)
  =\sum_{a=m-2}^{2m}\eta_a(R),}
 \tag{3.16}
\]

\[
 \boxed{
  \eta_{m-2}(R)+\eta_{2m}(R)=2\mu_1(R),}
 \tag{3.17}
\]

and

\[
 \boxed{
  \xi(R)=\eta_{m-1}(R)+\eta_{2m-1}(R).}
 \tag{3.18}
\]

Thus `xi` is a two-phase refinement of the upper incidence of the pointed
depth-two occurrence measure, not the ordinary unpointed upper incidence
transform by itself.

For first-shadow holes, the adjacent phases in (3.17) vanish.  Therefore

\[
 \sum_{a=m-1}^{2m-1}\eta_a(\mathcal H)
 =\sum_{R\in\mathcal H}(U\mu_2)(R).
 \tag{3.19}
\]

If `M_2` is the number of missing depth-two targets, then among the
`(m-1)|H|` facet incidences `D subset R`, at most `(m+3)M_2` use a missing
`D`.  Hence

\[
 \boxed{
  \sum_{a=m-1}^{2m-1}\eta_a(\mathcal H)
  \ge (m-1)|\mathcal H|-(m+3)M_2.}
 \tag{3.20}
\]

In particular, if `M_2=o(W)` while `|H|=Theta(W)`, almost every
first-shadow hole has linearly many covered depth-two facets, and some
nonadjacent cyclic phase has `Omega(W)` total exposure to the holes.
The factorial floor bound may be substituted into (3.20): with the
unhalved depth-two floor energy

\[
 Q_2=\sum_D(\mu_2(D)-c_2)(\mu_2(D)-c_2-1),
\]

one has

\[
 M_2\le {Q_2\over c_2(c_2+1)}.
 \tag{3.21}
\]

Equations (3.19)--(3.21) are the exact bridge to the growing band.  They do
not single out the nearest phase `xi`; the exposure can be concentrated in
more distant phases.

#### Physical lift status

For `t>1`, (3.12) is not a `C_8` increment.  The ambient rectangle lattice
expresses it as a signed sum of elementary rectangles, but lattice
generation does not provide a nonnegative sequential decomposition in the
current load, and even a load-legal elementary step need not be a currently
alternating exact-factor `C_8`.  Therefore no bounded sequence of legal
wreath-factor trades implementing every `L_{j,t}` is presently proved.

In fact a sequence of elementary `C_8` rectangles cannot have length
bounded independently of `t`.  Let `D_{r,2}` be down-incidence from
rank `r=m-1` sets to coordinate pairs.  The negative cells in (3.12) are
at Johnson distance `t+1`.  Apart from the exchanged coordinates, their
two difference sets each have size `t`.  A direct pair count gives

\[
 \boxed{\|D_{r,2}L_{j,t}\|_2^2=4t.}
 \tag{3.22}
\]

Indeed the nonzero pair coordinates are the pairs of either exchanged
coordinate with one of those `2t` remaining difference coordinates, with
the two signs, for `4t` unit entries.  An elementary rectangle has exactly
four unit pair coordinates and hence `D_{r,2}`-norm two.  By the triangle
inequality, every signed decomposition of `L_{j,t}` into `s` elementary
rectangles satisfies

\[
 \boxed{s\ge\sqrt t.}
 \tag{3.23}
\]

Thus even algebraically the full inventory requires mesoscopic, not
uniformly bounded, `C_8` sequences at distant phases.  The missing lift is
precisely a mesoscopic fan/alternating-circuit theorem with sequential
support; the long-exchange drift identity alone does not supply it.

## 4. A capped point-balanced zero-boundary model

The preceding logical gap is real even after point margins are imposed.
The construction below is a scalar endpoint-load model; no claim is made
that it is the shadow of an exact wreath factor.

Work on the cyclic ground set `Z_n`.  For an `r`-set `S`, let `kappa(S)` be
the number of cyclic runs of consecutive points of `S`.  One Johnson
exchange consists of one `1 -> 0` flip and one `0 -> 1` flip in the cyclic
incidence word.  Each flip changes the number of one-runs by at most one,
so

\[
 S\sim_J T\quad\Longrightarrow\quad
 |\kappa(S)-\kappa(T)|\le2.
 \tag{4.1a}
\]

The number of cyclic incidence words with `r` ones, `n-r` zeroes and
exactly `k` one-runs is

\[
 {n\over k}\binom{r-1}{k-1}
              \binom{n-r-1}{k-1}.
 \tag{4.1b}
\]

Indeed, choose positive compositions of the one and zero counts into `k`
runs, choose the starting position of a distinguished one-run, and divide
by the `k` possible distinguished one-runs.  Stirling's formula applied to
(4.1b) gives a central window of width `Theta(sqrt(n))`, and every fixed
set of run counts in that window has only `O(N_1/sqrt(n))` members.

Fix any constant `0<eta<1/3`.  We may therefore choose an integer threshold
`t=t(n)` so that

\[
 \mathcal H=\{S:\kappa(S)\le t\}
 \quad\hbox{has}\quad
 |\mathcal H|=(\eta+o(1))N_1,
 \tag{4.1c}
\]

while

\[
 \mathcal G=\{S:\kappa(S)\ge t+3\}
 \quad\hbox{has}\quad
 |\mathcal G|=(1-\eta-o(1))N_1.
 \tag{4.1d}
\]

By (4.1a), there is no Johnson edge from `H` to `G`.  Both families are
translation-invariant, and hence point-regular.

Put

\[
 \delta=W-N_1={2W\over m+2}.
\]

The integer `r delta/n` is integral, and, with
`g=gcd(n,r)=gcd(3,m-1)`, this says `n/g` divides `delta`.  The complement
family `G` is translation-invariant and, since `eta<1/3`, contains more
than `|H|+delta` sets for all large `m`.  Select in it a
translation-regular family `E` of size `|H|+delta`: use full orbits of
size `n`, and, when `g=3`, at most two orbits of size `n/3` coming from
aperiodic subsets of the quotient by the order-three subgroup.  The
divisibility needed for this selection holds because both `r|H|/n` and
`r delta/n` are integral.  The fixed-width loss in (4.1d) is `o(N_1)`, so
there are exponentially many allowed full and quotient orbits.

Define

\[
 \mu_*(R)=
 \begin{cases}
 0,&R\in\mathcal H,\\
 2,&R\in\mathcal E,\\
 1,&\text{otherwise}.
 \end{cases}
 \tag{4.1e}
\]

Then

\[
 \boxed{
 \sum_R\mu_*(R)=W,
 \qquad
 \sum_{R\ni x}\mu_*(R)={rW\over n},
 \qquad
 0\le\mu_*(R)\le2\le M_m.}
 \tag{4.2a}
\]

The hole family `H` and duplicate family `E` have no Johnson edges between
them.  Hence

\[
 e_J(\mathcal H,\mathcal D_2)=0.
 \tag{4.3a}
\]

Some Johnson neighbors of a hole may themselves be holes, so not every
algebraic rectangle based at that hole is load-legal.  But in every
**load-legal** such rectangle the two negative neighbors are nonholes; since
no duplicate is adjacent to `H`, both negative loads are then exactly one.
Equation (3.3) consequently gives

\[
 \Delta H=1-\mathbf1_{\{S\in\mathcal H\}}\in\{0,1\}.
 \tag{4.4a}
\]

Thus no such rectangle reduces the hole count, despite
`|H|=Theta(N_1)`.  Equations (4.2a)--(4.4a)
prove that total mass, uniform point margins, the exact endpoint
multiplicity cap, and global duplicate supply do not force even one useful
transposition/rectangle at a hole.

The same construction excludes every relabeling of sub-Gaussian support
if one uses only these scalar ledgers.  Let `k=o(sqrt(n))`, replace `G` in
(4.1d) by

\[
 \mathcal G_k=\{S:\kappa(S)\ge t+2k+1\}.
 \tag{4.4b}
\]

The omitted `2k` run-count layers have total size `o(N_1)`, so `G_k` still
has density `1-eta-o(1)`.  A product of at most `k` coordinate
transpositions changes `kappa` by at most `2k`.  After choosing the
duplicate family inside `G_k`, no such relabeling sends a hole to a
duplicate.  Hence bounded or `o(sqrt(n))`-length involution/multiswap
supply cannot be deduced from total mass, point regularity, and the endpoint
cap alone.  A positive theorem at that scale must use endpoint selection or
cyclic packetization.

What is not included in this countermodel is the full owner-to-endpoint
`b`-matching and cyclic packetization of an exact factor.  A theorem using
those stronger structures remains possible, but it must genuinely use
them; it cannot be inferred from the scalar endpoint ledger.

### 4.1 The exact end-map feasibility cuts

There is a precise intermediate condition between the scalar ledger and
cyclic packetization.  Let

\[
 \mathcal M=\binom{[n]}m,
 \qquad \mathcal R=\binom{[n]}{m-1},
\]

and join `M in M` to each of its `m` facets.  An **endpoint assignment** for
`mu` chooses two distinct facets of every `M` so that `R` is chosen exactly
`2 mu(R)` times.  For `Y subseteq R`, put

\[
 t_Y(M)=|\{R\in Y:R\subset M\}|.
\]

#### Proposition 4.2 (exact endpoint Hall criterion)

An endpoint assignment for `mu` exists if and only if

\[
 \boxed{
  2\sum_{R\in Y}\mu(R)
  \le
  \sum_{M\in\mathcal M}\min\{2,t_Y(M)\}
  \quad\hbox{for every }Y\subseteq\mathcal R.}
 \tag{4.5}
\]

#### Proof

Use the facet-incidence network with source-to-`M` capacity two, every
`M`-to-`R` incidence of capacity one, and `R`-to-sink demand
`2 mu(R)`.  The total demand and total source capacity are both `2W`.
The capacitated Hall condition for satisfying all right-hand demands is
exactly (4.5): a left vertex `M` can send at most
`min(2,t_Y(M))` units into `Y`.  Max-flow integrality then gives a
zero-one endpoint assignment.  Necessity is immediate. \(\square\)

For a singleton `Y={R}`, (4.5) recovers the cap
`2 mu(R)<=m+2`.  More significantly, if `H={mu=0}` and
`Y=R setminus H`, the left side equals `2W`.  Since every summand on the
right is at most two, equality forces

\[
 \boxed{
  |\{R\subset M:R\notin\mathcal H\}|\ge2
  \quad(M\in\mathcal M).}
 \tag{4.6}
\]

Thus every middle owner must have at least two nonhole facets.  This local
two-cover condition, and the other cuts (4.5), are genuinely absent from
the scalar model above.

Choosing the two facets of each `M` makes an edge labelled by `M` in the
lower Johnson graph.  Its degree at `R` is `2 mu(R)`, so it is Eulerian.
It therefore decomposes into cycles, but the cycles need not have length
`n` and need not be cyclic-order wreaths.  Hence (4.5) characterizes the
full endpoint-selection ledger exactly, while cyclic packetization remains
a further constraint.

### 4.2 Positivity is solved by nonlocal occurrence cycles

Elementary rectangles are not a positive Markov basis for the whole
point-margin fibre.  There is nevertheless a simple exact positive Markov
basis once nonlocal occurrence-cycle moves are allowed.

#### Proposition 4.3 (point-regular balanced target at depth one)

There is a balanced depth-one vector `b` satisfying

\[
 b(R)\in\{1,2\},\qquad \sum_Rb(R)=W,
 \qquad \sum_{R\ni x}b(R)={rW\over n}\quad(x\in[n]).
 \tag{4.7}
\]

#### Proof

Write `delta=W-N_1`.  It is enough to find a point-regular family
`E subseteq R` of size `delta` and set `b=1+1_E`.  The equitable form of
Baranyai's theorem partitions a complete uniform hypergraph into
almost-regular subhypergraphs of any prescribed edge sizes.  Apply it with
one part of size `delta`.  The average degree of that part is

\[
 {r\delta\over n}.
\]

It is an integer: both `rW/n` (the actual wreath point margin) and
`rN_1/n=binom(n-1,r-1)` are integers.  Almost regularity therefore means
that every point degree is exactly `r delta/n`.  This proves (4.7).
\(\square\)

The following statement works at any rank.

#### Theorem 4.4 (nonnegative occurrence-cycle connectivity)

Let `x,b` be nonnegative integral load vectors on `r`-sets, with the same
total mass and the same point margins.  Then `x` can be transformed into
`b` through nonnegative integral loads by finitely many moves of the
following form.  A move selects distinct labelled occurrences and, in
each selected occurrence, replaces one present coordinate by one absent
coordinate; collectively the removed and inserted coordinate multisets
are equal.

#### Proof

Lift the occurrences of `x` and `b` to two zero-one matrices `X,Y` with
the same labelled row set.  Every row has sum `r`; the column sums agree by
hypothesis.  In the bipartite graph on row labels and coordinates, orient
every edge of `X setminus Y` from its row to its coordinate, and every edge
of `Y setminus X` from its coordinate to its row.  Equal row and column
sums make this directed graph Eulerian.  Decompose it into directed simple
cycles.  On one cycle, delete every `X setminus Y` incidence and insert
every `Y setminus X` incidence.  Each touched row loses and gains one
coordinate, and an inserted incidence was absent, so the new matrix is
again zero-one.  The move preserves every column sum and removes all
disagreements on that cycle.  Toggling all cycles changes `X` to `Y`.
Passing from labelled rows back to their histogram gives the required
nonnegative load path. \(\square\)

For the actual first-shadow load of an exact factor, (1.3) and Proposition
4.3 meet the hypotheses of Theorem 4.4.  Hence there is **no positivity or
point-margin obstruction at the load level** to reaching exact balance at
depth one.  What remains is physical: an occurrence-cycle move need not be
the shadow of an exact-factor trade.  Elementary `C_8` moves implement only
special four-cell pieces, and Section 5 below identifies one sector where
they can be scheduled.  A theorem lifting the occurrence cycles, or a
conformal decomposition of them into sequentially available `C_8` cells,
would prove the depth-one balancing theorem.

## 5. One-token rectangle fans in a fixed-core sector

There is nevertheless an exact positive scheduling theorem at the load
level.

Fix an `(r-2)`-set `K`, disjoint label sets `A,B`, and identify the cell
`(a,b)` with the target `K union {a,b}`.  Let `b_{ab}>=0` be a desired load
and `mu_{ab}>=0` a current load.  Put

\[
 d_{ab}=b_{ab}-\mu_{ab}.
\]

Assume every row and column sum of `d` is zero.  Make the directed bipartite
multigraph with a positive cell `d_{ab}>0` represented by copies of
`a -> b`, and a negative cell by copies of `b -> a`.  It is Eulerian and
decomposes into directed simple alternating cycles.  One unit cycle has

\[
 q=\sum_{i=1}^s
 \bigl(e_{a_i b_i}-e_{a_i b_{i-1}}\bigr),
 \qquad b_0=b_s.
 \tag{5.1}
\]

### Theorem 5.1 (one-token fan schedule)

For the cycle (5.1), put

\[
 R_i=
 e_{a_i b_i}+e_{a_1 b_{i-1}}
 -e_{a_i b_{i-1}}-e_{a_1 b_i}
 \qquad(2\le i\le s).
 \tag{5.2}
\]

Then

\[
 \boxed{q=\sum_{i=2}^sR_i.}
 \tag{5.3}
\]

Apply the rectangles in the descending order

\[
 R_s,R_{s-1},\ldots,R_2.
 \tag{5.4}
\]

Every intermediate load is nonnegative.  Away from the desired cycle
corrections, at most one extra unit is present, moving successively through
the anchor cells

\[
 (a_1,b_{s-1}), (a_1,b_{s-2}),\ldots,(a_1,b_1).
\]

After the fan, the deficit is reduced by exactly `q`, and its `ell_1` norm
drops by `2s`.

#### Proof

Equation (5.3) is telescoping: the anchor terms sum to

\[
 e_{a_1b_1}-e_{a_1b_s},
\]

the missing first positive and last negative cells of (5.1).

In the first step `R_s`, both nonanchor negative
`(a_s,b_{s-1})` and anchor negative `(a_1,b_s)` are genuine negative
deficit copies, so their current loads exceed their desired loads and are
at least one.  The step adds one temporary unit at `(a_1,b_{s-1})`.
At every later step, the anchor subtraction removes exactly the temporary
unit added by the preceding step.  The other negative cell is again a
genuine negative deficit copy.  Thus no load becomes negative, and only
one anchor token is outstanding.  The final step deposits that token in
the genuine positive cell `(a_1,b_1)`.  All cycle copies have then been
corrected once, proving the last assertion. \(\square\)

Repeating Theorem 5.1 over the Eulerian cycle decomposition transforms
`mu` to `b` through nonnegative rectangle moves.

### Corollary 5.2 (supported exact-factor descent)

Suppose the current load is the first shadow of an exact wreath factor
`F`.  If, at every step of the fan schedule (5.4), the required rectangle
is the first-shadow increment of a currently alternating exact-factor
`C_8`, then toggling those `C_8`'s gives a sequence of exact factors and
performs the same deficit reduction.  If this sequential-lift condition
holds for every cycle in a decomposition of `d`, the terminal exact factor
has load `b`.

The hypothesis is exactly a support condition.  The ambient MSW-orbit
theorem proves that every individual `R_i` has an exact `C_8` lift in
*some* conjugate exact factor.  It does not prove that the lifts occur in
the evolving factor required by Corollary 5.2.

## 6. Hall cuts and the minimal remaining obstruction

For the depth-one row-to-target graph of a fixed factor, with desired row
quota `a_1`, the exact hard-quota defect is

\[
 D_1(F)=\max_{\mathcal A\subseteq F}
 \bigl(a_1|\mathcal A|-|N(\mathcal A)|\bigr)_+.
 \tag{6.1}
\]

The full-family cut is

\[
 \bigl(H_1(F)-\delta_1\bigr)_+,
 \qquad a_1|F|=N_1-\delta_1.
 \tag{6.2}
\]

A conformal fan which fills holes and never subtracts the last occurrence
improves (6.2).  It need not improve every proper cut in (6.1), because a
`C_8` replaces whole wreath rows and can redistribute their private
neighborhoods.  Thus a hard-quota application must add the explicit
condition that each fan is Hall-safe (all cuts in (6.1) retain nonnegative
slack).  Soft-shadow coverage alone does not require that extra condition.

The exact minimal obstruction now has two levels.

1. **Local Johnson obstruction.**  A hole can have no duplicate neighbor,
   in which case neither a transposition nor one rectangle based at that
   hole gives descent.  Section 4 shows that the scalar endpoint ledgers do
   not exclude this.
2. **Exact-factor lift obstruction.**  Even when a fixed-core load deficit
   has the one-token schedule of Theorem 5.1, the next rectangle may have no
   alternating `C_8` in the current factor.  Ambient lattice generation is
   not sequential availability.

Equivalently, a positive theorem must supply either

\[
 \boxed{
 \text{a Johnson-dispersed duplicate boundary plus component-rich legal
 lifts,}}
\]

or a genuinely nonlocal bounded/mesoscopic trade which implements an
entire fan at once.  Point balance and the ambient rectangle lattice have
already done all they can do without this support input.

## 7. Why component richness is independent of endpoint supply

For exact factors `F,G`, their ownership overlay is an `n`-regular
bipartite multigraph: left vertices are wreaths of `F`, right vertices are
wreaths of `G`, and middle owners are its edges.  Component switching has
one independent sign per connected component.

The depth-one endpoint ledger constrains which two facet colours are
incident with each owner, but its scalar consequences (1.1)--(1.4) do not
bound the connectivity of this ownership overlay.  Abstractly, any
connected `n`-regular bipartite graph gives two partitions of the same
owner set into `n`-blocks, while the endpoint colours can be placed on the
owner incidences subject to their local matching cap.  Hence all of the
target-level supply may lie in one component in this abstract model.

This is not asserted to be a Boolean wreath realization.  It proves the
logical scope: obtaining many independently switchable components from
endpoint structure requires a new compatibility theorem linking endpoint
colours to ownership-overlay fragmentation.  Neither (1.4), the full
relabel average (2.1), nor the ambient rectangle lattice supplies it.
