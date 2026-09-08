# Dense boundary-rectangle chronology exists but is homologically null: the exact state graph and recharge-capacity wall

Date: 2026-07-27

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Put

\[
 n=2m,\qquad M=m+H,\qquad d=m-3H+1,
 \qquad N=\binom{2m}{M},\qquad W=\binom{2m}{m},              \tag{0.1}
\]

and assume the calibrated common-core relation

\[
                         MN=(1+o(1))W,\qquad H=o(m).          \tag{0.2}
\]

Take as input the exact collar-neutral two-top rectangle from
`MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md`.
At each of its two tops the physical move swaps only the first two
letters of one rooted exposed word.  The two local unit transfers add to
one hypersimplex rectangle at the middle, while every protected
nonmiddle row cancels exactly.

The dense chronological composability question has a sharp answer for
this primitive.

1. **Exact local state graph.**  At a fixed rooted top, the rectangle
   option graph is a disjoint union of copies of $K_2$.  Changing a
   compatible companion or merely re-describing the core/filler
   certificate can create a parallel use of the same intrinsic edge.
   Changing the actual rooted word or ordered tail instead lands in
   another disjoint $K_2$; it is not a free state transition.

2. **Endpoint capacity.**  In an arbitrary chronology using only these
   rectangles,

   \[
       \boxed{
       {1\over2}\|\mu_0^{\rm final}-\mu_0^{\rm initial}\|_1
       \le N.}                                               \tag{0.3}
   \]

   Every closed circuit is load-null.  Thus using each top
   $10^{100}$ times, or merely $\Theta(m)$ times, produces no more net
   action than one odd toggle per top.

3. **A genuine dense circuit.**  In one petal star with $2p$ tops,
   where $p=\Theta(m)$ is even, there is an explicit chronology of
   $p^2$ distinct rectangle occurrences which uses every top exactly
   $p$ times, preserves every protected nonmiddle load after every
   step, and returns every top path to its initial state.  Hence dense
   chronological reuse itself is possible.  Its endpoint middle action
   is exactly zero.

4. **Recharge-capacity inequality.**  Enlarge the chronology by
   arbitrary globally middle-neutral recharge moves which may reset a
   top's literal boundary state.  If $c_U$ is the number of such
   state-changing recharge incidences at top $U$, and $C=\sum_Uc_U$,
   then

   \[
       \boxed{
       {1\over2}\|\mu_0^{\rm final}-\mu_0^{\rm initial}\|_1
       \le N+C.}                                             \tag{0.4}
   \]

   Consequently a displacement of total variation $(1-o(1))W$ forces

   \[
                         C\ge(1-o(1))W,                      \tag{0.5}
   \]

   or average recharge incidence

   \[
                         {C\over N}\ge(1-o(1))M=\Theta(m)    \tag{0.6}
   \]

   per top.  If every available neutral recharge packet contributes at
   most eight reset incidences, at least $(1-o(1))W/8$ such packets are
   necessary.

5. **Static Boolean capacity.**  If many local unit toggles are required
   to coexist as one conformal Boolean bank, sharp one-window chronology
   improves the existing per-top bound from $2H+2$ to

   \[
                         \boxed{r_U\le2H},\qquad R\le HN=o(W). \tag{0.7}
   \]

   For the unaugmented rectangle primitive itself, the stronger bound is
   one local edge per boundary orbit.

6. **Statewise installation obstruction.**  The master-order chamber
   contains no source shore of the displayed two-top rectangle family:
   the two paths induce opposite cyclic orientations on a common tail
   triple.  Even after granting free path reversal and both endpoint
   swaps, the calibrated four-top router cannot enter this chamber for
   $H\ge11$.  Thus the explicit high-energy master-order state cannot
   start this rectangle system or its calibrated four-top recharge
   augmentation.

The conclusion is definitive for the collar-neutral rectangle basis
alone: it cannot implement the required dense displacement.  The only
surviving route is a new middle-neutral state-reset edge (for example a
tail change or re-rooting), used in $(1-o(1))W$ total top incidences,
hence $\Theta(m)$ times per top on average, and satisfying the full
companion, owner, tag, and precedence ledgers.  No such useful circuit
is constructed here, and no coefficient-one conclusion is claimed.

## 1. The local boundary involution

Fix a rank-$M$ top $U$.  Its intrinsic literal rooted option is the
exposed word

\[
                         p=(U;u,v,\tau),                     \tag{1.1}
\]

where $u,v$ are its first two labels and $\tau$ is the complete ordered
tail beginning at position three.  Define

\[
                         Lp=(U;v,u,\tau).                    \tag{1.2}
\]

The local half of every rectangle in the source theorem is precisely
$p\leftrightarrow Lp$.  It changes one middle owner and, before pairing
with its companion top, has one unit derivative

\[
                         \delta_0(p)=e_{Y(p)}-e_{X(p)}.       \tag{1.3}
\]

At nonmiddle protected depths it has a vertical collar; the second top
of the rectangle carries its exact negative.

### Theorem 1.1 (fixed-root option graph)

Let $\mathcal G_U^\square$ be the graph whose vertices are literal
rooted path options at $U$ and whose edges are the local halves of all
rectangles in the certified fixed-root boundary-swap catalogue,
allowing arbitrary compatible companion tops.  Put

\[
                         \iota(p)=(U;\{u,v\},\tau).           \tag{1.4}
\]

Then

\[
                         \boxed{
 \mathcal G_U^\square=\bigsqcup_{\iota}K_2,\qquad
 K_2(\iota)=\{p,Lp\}.}                                      \tag{1.5}
\]

Parallel rectangle occurrences may join the same two vertices, but no
third vertex belongs to one component.

#### Proof

Every local move changes $(u,v,\tau)$ to $(v,u,\tau)$ and fixes every
letter and position of $\tau$.  Its reverse is the same physical move.
Thus it preserves $\iota$, and the fibre of $\iota$ has exactly the two
states $p,Lp$.  Changing the companion or merely changing an auxiliary
$Q/P$, filler-role, or tag certificate may give a parallel certified
occurrence of this same intrinsic edge; it does not create a new
neighbor.  Changing the actual rooted word or ordered tail changes
$\iota$ and gives another disjoint $K_2$.  This proves (1.5).
$\square$

If an implementation regards identical words with different tags as
distinct catalogue tokens, those tokens give parallel copies projecting
to the same intrinsic $K_2$.  They do not create a state edge between
different $\iota$-fibres and do not alter the middle endpoint bound.

The word *rooted* is essential.  Reversing or re-rooting the retained
path is a different physical chronology state unless a separate legal
transition is supplied.  Granting a free right-end toggle as well would
replace $K_2$ by components of at most four states and would only change
the constants below by a factor two.

## 2. Parity normal form and the global endpoint ceiling

Consider any finite chronology of physical two-top rectangles.  For a
boundary orbit $\mathcal O=\{p,Lp\}$, let $t_{\mathcal O}$ be its
number of local toggles and let $\epsilon_{\mathcal O}\in\{0,1\}$ be
the initial shore bit.

### Theorem 2.1 (middle parity normal form)

The endpoint middle-deck derivative is

\[
 \boxed{
 \Delta_0^{\rm end}
 =\sum_{\mathcal O:\ t_{\mathcal O}\ {\rm odd}}
   (-1)^{\epsilon_{\mathcal O}}\delta_0(\mathcal O).}        \tag{2.1}
\]

Every protected nonmiddle aggregate load is unchanged after every
two-top rectangle macro.  In particular, if every top returns to its
initial rooted path, then the endpoint load is unchanged at every row.

#### Proof

Within one $K_2$ component the successive local middle derivatives
alternate

\[
                         \delta_0,-\delta_0,
                         \delta_0,-\delta_0,\ldots.           \tag{2.2}
\]

Their sum is zero for even $t_{\mathcal O}$ and the signed first term
for odd $t_{\mathcal O}$.  Sum independently over all top orbits.
At a protected nonmiddle row, the two local halves of each physical
rectangle have exact opposite derivatives with synchronized tags, so
the aggregate derivative of that macro is zero without any parity
argument.
$\square$

At the middle, every surviving odd orbit contributes one unit transfer
and hence has $\ell^1$-norm two.  A one-path-per-top endpoint table has
at most one current orbit at each top.  The triangle inequality in
(2.1) gives

\[
 {1\over2}\|\Delta_0^{\rm end}\|_1
 \le\#\{\text{odd top orbits}\}\le N,                       \tag{2.3}
\]

which is (0.3).  Under (0.2), $N=(1+o(1))W/M=o(W)$.

This is stronger than counting rectangle occurrences.  It applies to
an arbitrarily long chronology and to arbitrary re-pairing of a current
top with new companions.

## 3. An explicit $\Theta(m)$-reuse circuit

The parity theorem does not say that long chronological circuits are
unavailable.  They exist in their strongest possible combinatorial
form.

Fix one common $(M-1)$-set

\[
 B=R\cup\{a,b,z,z'\}\cup F,\qquad |B|=M-1,                  \tag{3.1}
\]

with the data of the two-top rectangle.  Its petal tops are

\[
                         U_x=B\cup\{x\},
 \qquad x\in X=[2m]\setminus B,                              \tag{3.2}
\]

where

\[
                         |X|=m-H+1.                          \tag{3.3}
\]

Choose disjoint sets $X_0,X_1\subseteq X$ with

\[
                         |X_0|=|X_1|=p,                      \tag{3.4}
\]

where, exactly,

\[
                         p=2\left\lfloor{m-H+1\over4}\right\rfloor
                         =\Theta(m).                          \tag{3.5}
\]

Fix one common ordered $Q/P$ certificate and one identical phase-tag
schedule $\lambda$ on all $2p$ petals.  These data are available in the
source rectangle and make every edge of the complete bipartite atlas
simultaneously compatible at every protected depth.

For $x\in X_0$, install the type-zero word

\[
                         (a,b,x,F,z,z',\rho),                \tag{3.6}
\]

and for $y\in X_1$ install

\[
                         (b,a,y,F,z',z,\rho).                \tag{3.7}
\]

Write one state bit at every petal, equal to zero in (3.6)--(3.7) and
one after its first-two-letter swap.  Every pair $xy\in X_0\times X_1$
supports the same rectangle direction

\[
 \Gamma=
 e_{R\cup\{b,z'\}}-e_{R\cup\{a,z'\}}
 +e_{R\cup\{a,z\}}-e_{R\cup\{b,z\}}.
\]

### Lemma 3.1 (petal-star transition rule)

An edge $xy$ is chronologically applicable exactly when its endpoint
bits agree.  If both are zero it flips them to one and adds $\Gamma$ at
the middle.  If both are one it flips them to zero and adds
$-\Gamma$.  Every protected nonmiddle load is unchanged.

#### Proof

Equal zero bits are the source shore in the two-top construction; equal
one bits are its reverse shore.  Mixed bits contain one old and one new
local option and are not a rectangle shore.  The source theorem gives
the middle signs and exact nonmiddle cancellation.  The auxiliary petal
labels disappear from the exceptional middle complements, so the same
$\Gamma$ occurs for every edge of the petal star.  $\square$

If $S\subseteq X_0$ and $T\subseteq X_1$ are the sets of one-bits,
then a move adds a pair $x\in X_0\setminus S$, $y\in X_1\setminus T$
or removes a pair $x\in S$, $y\in T$.  Hence $|S|-|T|$ is invariant.
Starting from the zero shore, the reachable state set is exactly

\[
        \{(S,T):S\subseteq X_0,\ T\subseteq X_1,\ |S|=|T|\},
                                                               \tag{3.8}
\]

because any equal-size pair $(S,T)$ can be built along a matching
between $S$ and $T$.  More strongly, if $\mathcal L(S,T)$ denotes its
middle load, then

\[
 \boxed{\mathcal L(S,T)=\mathcal L(\varnothing,\varnothing)
                         +|S|\Gamma.}                         \tag{3.9}
\]

Thus the whole petal state graph has an exact height potential; every
state-graph circuit is owner-load null.

Partition $X_0$ into pairs $A_1,\ldots,A_{p/2}$ and $X_1$ into pairs
$B_1,\ldots,B_{p/2}$.  For

\[
 A_i=\{x_1,x_2\},\qquad B_j=\{y_1,y_2\},                   \tag{3.10}
\]

execute the four edges of their $K_{2,2}$ block in the order

\[
                         x_1y_1,\quad x_2y_2,\quad
                         x_1y_2,\quad x_2y_1.               \tag{3.11}
\]

### Theorem 3.2 (dense null circuit)

Perform (3.11) for all $(p/2)^2$ pair-blocks, in any order.  Then:

1. every step is a legal two-top rectangle transition;
2. every edge of $K_{p,p}$ is used exactly once;
3. every top is used exactly $p=\Theta(m)$ times;
4. the chronology contains $p^2=\Theta(m^2)$ rectangle steps;
5. every protected nonmiddle load is constant after every step; and
6. every path and every middle load return exactly to their initial
   states.

#### Proof

At the start of one block all four bits are zero.  The first two,
vertex-disjoint, edges in (3.11) are zero-zero moves and make all four
bits one.  The last two edges are one-one moves and return all four bits
to zero.  Thus every block is a legal four-step circuit and blocks may
be concatenated arbitrarily.

The Cartesian products $A_i\times B_j$ partition the edge set of
$K_{p,p}$, proving Item 2.  Every vertex has degree $p$, proving Item 3,
and edge counting gives Item 4.  Lemma 3.1 proves Item 5.  One block has
middle increments

\[
                         \Gamma,\Gamma,-\Gamma,-\Gamma,      \tag{3.12}
\]

and restores all four paths.  Summing blocks proves Item 6.
$\square$

The circuit is therefore dense but homologically null.  Its peak middle
excursion inside one block is $2\Gamma$.

There is also an exact owner-capacity warning.  On the zero shore, the
two forced common owners

\[
                         R\cup\{z,z'\},\qquad R\cup\{a,b\}
\]

each have multiplicity $2p$.  The two negative $\Gamma$-cells

\[
                         R\cup\{a,z'\},\qquad R\cup\{b,z\}
\]

have multiplicity $p$, one across each petal class; every remaining
cross-petal owner is distinct.  Indeed, outside these exceptional
phases the owner retains its petal label $x$ or $y$, and the injective
window path distinguishes phases within one petal.  Hence the initial
middle repeat excess
is exactly

\[
                         2(2p-1)+2(p-1)=6p-4.               \tag{3.13}
\]

Thus the dense circuit is a literal one-path-per-top chronology but not
an occurrence-squarefree owner factor.  Starting from a $0$-$1$ owner
load, two disjoint positive edges with the same $\Gamma$ cannot both be
applied before a negative edge restores the donors.  Dense chronology
does not by itself solve the owner-capacity gate.

## 4. The state-segment recharge inequality

We now allow a second class of physical moves.  A **recharge move** is
globally middle-neutral, but at a touched top it may change the complete
intrinsic rooted boundary state $p$.  This includes a change to another
$\iota$-fibre, a re-rooting or tail change, and also a reset from $p$ to
$Lp$ inside the same fibre.  The last case must be counted: it breaks
the alternation just as surely as an orbit change.  Conveyors and
moving-hole routers are examples only when their complete source shores
are literally present.

Consider a chronology containing boundary rectangles and recharge
moves.  At top $U$, mark every recharge incidence which changes its
intrinsic literal boundary state.  The remaining boundary swaps split
into at most $c_U+1$ consecutive segments, where $c_U$ is the number of
marked incidences at $U$.  A recharge incidence that fixes the intrinsic
rooted word (and only changes an auxiliary certificate) is immaterial
for this alternation bound and need not be marked.

### Theorem 4.1 (dynamic recharge capacity)

Let $C=\sum_Uc_U$.  If every recharge move has zero aggregate middle
derivative, then the full endpoint displacement satisfies

\[
                         \boxed{
 {1\over2}\|\Delta_0^{\rm end}\|_1\le N+C.}                 \tag{4.1}
\]

#### Proof

Within one segment at one top, all boundary swaps lie in one $K_2$
orbit.  Their local derivatives alternate, so the segment sum is either
zero or one signed unit transfer.  Its half-$\ell^1$ norm is at most
one.  Therefore the sum $b_U$ of all boundary-swap derivatives at $U$
satisfies

\[
                         {1\over2}\|b_U\|_1\le c_U+1.        \tag{4.2}
\]

Recharge moves sum to zero globally at the middle.  Hence

\[
                         \Delta_0^{\rm end}=\sum_Ub_U.       \tag{4.3}
\]

The triangle inequality, (4.2), and the $N$ available tops prove
(4.1).  $\square$

### Corollary 4.2 (necessary dense recharge)

If

\[
                         {1\over2}\|\Delta_0^{\rm end}\|_1
                         \ge(1-o(1))W,                       \tag{4.4}
\]

then, under (0.2),

\[
                         C\ge(1-o(1))W,
 \qquad {C\over N}\ge(1-o(1))M.                            \tag{4.5}
\]

If every recharge packet has arity at most $a$ and contributes at most
one marked before/after reset at each touched top, the number of recharge
packets is at least

\[
                         {(1-o(1))W-N\over a}.                \tag{4.6}
\]

In particular $a\le8$ gives $(1-o(1))W/8$ packets.

A compound packet with internal boundary moves must instead be refined
at those moves and every intervening local reset counted; its applicable
arity is the number of resulting reset incidences, not merely the size
of its displayed shore.

This is an endpoint capacity theorem, not an additive seam-cost claim.
The recharge traces may telescope along a genuine state trajectory.
It bounds the unlabelled aggregate middle-load vector only.  A
middle-neutral reassignment of providers can have large labelled
Hamming distance while contributing zero to (4.1).
What (4.5) rules out is any architecture in which only $o(W)$ genuine
local state resets are hidden behind $\Theta(W)$ repeated rectangle
uses.  Counting only changes of the orbit invariant $\iota$ would be
incorrect, because a middle-neutral recharge could reset $Lp$ to $p$
inside one $K_2$ and restart the same sign.

## 5. Static Boolean capacity from the sharp one-window locus

The static Boolean problem is stronger than choosing one long path
through the state graph.  Suppose a bank of toggles is indexed by
$[R]$, every Boolean shore $S\subseteq[R]$ is represented by one literal
path per top, and the middle deck at top $U$ has the additive form

\[
 \mathcal B_U(S)=\mathcal B_U(\varnothing)
 +\sum_{j\in S:\,j\sim U}(e_{Y_{Uj}}-e_{X_{Uj}}).            \tag{5.1}
\]

Let $r_U$ be the number of incident toggles.

### Lemma 5.1 (sharp one-window collar)

Assume $H\ge3$ and $d\ge2H+1$.  If two injective length-$d$ tight paths
on one top have middle decks differing by one unit transfer, the removed
source occurrence lies in one of the phases

\[
                         \{1,\ldots,H\}\cup
                         \{d-H+1,\ldots,d\}.                 \tag{5.2}
\]

All $2H$ phases in (5.2) are attainable by some one-window path
replacement.

#### Proof

Complement to the two $H$-window decks, and call the old-only window
$J_i$.  Their intersection-$(H-1)$ graphs are paths.  When $1<i<d$,
the two common components are aligned because $J_{i-1},J_{i+1}$ are
the unique cross-component pair of maximum intersection $H-2$.
Suppose $H+1\le i\le d-H$.  Any replacement window adjacent to both
$J_{i-1}$ and $J_{i+1}$ must contain

\[
 J_{i-1}\cap J_{i+1}
\tag{5.3}
\]

and one label from each of the two two-element endpoint differences.
Unless it is $J_i$ itself, it contains the extreme letter just before
$J_i$ or just after it.  Each such extreme letter already occurs in
exactly $H$ common windows.  The replacement would make its window
frequency $H+1$, impossible in an injective word.  Hence (5.2).

For phases $2,\ldots,H$, swap word positions $i-1,i$; only window $i$
changes.  At phase one, replace the first word label by an unused top
label.  Reverse the word for the last $H$ phases.  $\square$

### Theorem 5.2 (static Boolean capacity)

Under (5.1),

\[
                         \boxed{r_U\le2H},
 \qquad                       \boxed{R\le HN}.               \tag{5.4}
\]

#### Proof

Compare the empty shore with every singleton shore.  Lemma 5.1 assigns
the negative source $X_{Uj}$ of each incident toggle to one of the
$2H$ base-path occurrences in (5.2).

Two toggles cannot have the same source.  Otherwise the Boolean shore
containing both would subtract that one base occurrence twice; neither
toggle's nontrivial target equals its own source, so the resulting deck
would have coefficient $-1$ there.  Thus the source-occurrence map is
injective and $r_U\le2H$.  Double-counting the two incident tops of
every rectangle gives

\[
                         2R=\sum_Ur_U\le2HN.                 \tag{5.5}
\]

This proves (5.4).  $\square$

Under (0.2), $HN=(H/M+o(1))W=o(W)$.  This corrects the loose
$2H+2$ collar count in
`MATH_THEOREM_L_STATIC_COLLAR_NEUTRAL_RECTANGLE_CAPACITY_20260727.md`.
The constant $2H$ is sharp for the individual source-phase locus and
therefore for this counting argument.  No conformal Boolean bank
attaining $r_U=2H$ is constructed or claimed.
It does not bound adaptive reinstallation after the base path changes;
that is exactly the role of Theorem 4.1.

## 6. Statewise master-order walls

The explicit master-order state used in the collision lower bound is
even more rigid than (0.3).  Fix a directed cyclic order $\sigma$ of the
ground coordinates.  At every top $U$, let $\pi_U=\sigma|_U$ be the
literal cyclic frame selected by the master state, with its audited
common-core cut.  Let $e_U$ be its exposed first-two pair.  Define the
**one-swap master chamber**

\[
              \mathfrak C_\sigma
              =\prod_U\{\pi_U,s_{e_U}\pi_U\}.               \tag{6.1}
\]

### Theorem 6.1 (no rectangle shore in the master chamber)

For all sufficiently large calibrated $m$, no shore of the displayed
two-top collar-neutral rectangle family lies in $\mathfrak C_\sigma$.
Hence the literal master-order state cannot make even a first move from
that family.

#### Proof

Choose any common tail label

\[
                         r_*\in F\cup R_{\rm act};           \tag{6.2}
\]

this set is nonempty once $H=o(m)$ and $m$ is sufficiently large.  The
two rectangle words are

\[
 (a,b,x,F,z,z',\rho),\qquad (b,a,y,F,z',z,\rho).             \tag{6.3}
\]

On the common triple $\{z,z',r_*\}$ they induce opposite directed
cyclic orientations.  Swapping either exposed first pair does not alter
that triple.  But restrictions of one directed cyclic order $\sigma$
to the same common triple must agree.  Therefore neither rectangle
shore can consist of master-frame restrictions, even after the allowed
first-two swaps.  $\square$

This checks an implication scope hidden by the load-distance lower
bound: the master-order state is not merely far from a low-collision
load; the unaugmented rectangle dynamics cannot leave it.

The wall survives a substantially more generous relaxation.  Grant at
each top, for free, reversal of the exposed word, its left-end swap, and
the reversal-conjugate right-end swap.  Outside

\[
 E_U=\{w_1,w_2,w_{\ell-1},w_\ell\},                         \tag{6.4}
\]

the current word has the same **dihedral** cyclic order as
$\sigma|_U$; here $\ell$ is the exposed-word length.  Thus two current
tops must give the same dihedral order on
every common four-set avoiding $E_U\cup E_V$.

### Corollary 6.2 (the calibrated four-top router cannot recharge the
master chamber)

Assume $H\ge11$.  In the calibrated four-top router, write its common
visible blocks as

\[
 Y=(y_0,\ldots,y_{r-2}),\qquad
 T=(t_0,\ldots,t_{s-3H+1}).                                 \tag{6.5}
\]

Then

\[
 |Y|=r-1\ge2H+1,\qquad |T|=s-3H+2\ge H-1.                 \tag{6.6}
\]

No checkerboard shore of that router, including the post-boundary shore,
belongs to the enlarged dihedral master chamber.  Consequently a
chronology starting at the master state and using arbitrary free word
reversals, both endpoint swaps, and calibrated four-top routers has

\[
                 {1\over2}\|\Delta_0^{\rm end}\|_1\le2N=o(W). 
                                                               \tag{6.7}
\]

#### Proof

Every checkerboard shore contains an adjacent $\alpha^\circ$-top and
$\beta^\circ$-top.  At most eight labels of their common ground set lie
in the two endpoint sets (6.4).  By (6.6) and $H\ge11$, choose two
$Y$-labels and two $T$-labels outside those endpoint sets.  The two
words induce, after naming the selected labels in their forward block
orders,

\[
 (y_i,y_j,t_p,t_q),\qquad (y_i,y_j,t_q,t_p).                 \tag{6.8}
\]

These cyclic orders are neither rotations nor reversals of one another:
their unordered diagonal pairings differ.  This contradicts the
dihedral master invariant.  The post-boundary swap only touches (6.4),
so the same witness remains.

Each granted reversal or endpoint-swap generator preserves the enlarged
dihedral chamber.  If a router ever fired, the state immediately before
the first router would still lie in that chamber, contradicting the
preceding witness.  Hence no router fires.

Free reversal changes no unordered tight-window deck.  A left- or
right-end swap replaces at most one middle window, so each top differs
from its master deck by at most two unit replacements.  Summing over
the $N$ tops proves (6.7).  $\square$

There is no hidden free re-rooting in the middle path monomial.  If
$d\ge H+1$, the intersection-$(H-1)$ graph of an injective tight
$H$-window deck is the path $P_d$, so it orders the windows up to
reversal.  The consecutive differences recover $w_i$ and $w_{i+H}$ for
$1\le i<d$; these positions cover the whole exposed word.  Thus the
word is determined up to reversal.  A genuine tail change or new path
endpoint is a new physical recharge and remains outside this theorem.

## 7. Source audit and implication scope

Four qualifications of the positive rectangle theorem are material for
dense recycling.

1. On either raw two-path shore, the two paths share exactly two middle
   owners, at phases one and three.  Thus the unpunctured rectangle is a
   legal one-option-per-top coefficient move but is not an
   occurrence-squarefree exact-owner packet.
2. The equality
   $\ker_{\mathbb Z}A=\langle\text{rectangles}\rangle$ is a signed
   lattice statement.  It supplies no nonnegative chronological order
   and no linear bound on the number of rectangles in a decomposition;
   one symmetric exchange may require a Johnson path of length
   $\Theta(m)$.
3. The normalization $N=(1+o(1))W/m$ uses the calibrated relation
   $MN=(1+o(1))W$.  The scale statement
   $H=(1+o(1))\sqrt{m\log m}$ alone does not determine that leading
   constant without the corresponding exponent calibration.
4. Exact chronological installation additionally requires, at every
   top, a directed option trail; globally compatible pairing of its
   half-edges; an acyclic common precedence order; identical companion
   tag schedules; and owner capacity after every prefix.  Signed collar
   cancellation proves none of these conditions.

## 8. Exact boundary

The following are proved.

1. The rectangle-only option graph is a product of two-state boundary
   orbits.
2. Every closed rectangle circuit is load-null and every endpoint
   displacement has total variation at most $N=o(W)$.
3. A concrete $p^2$-step circuit uses every one of $2p$ tops
   $p=\Theta(m)$ times with zero nonmiddle action and zero endpoint
   action.
4. Any augmented chronology reaching unlabelled middle-load variation
   $(1-o(1))W$ needs $(1-o(1))W$ genuine local boundary-state resets,
   averaging $\Theta(m)$ per top.
5. A conformal static Boolean bank has at most $2H$ local unit slots per
   top and at most $HN=o(W)$ rectangles.
6. The master-order chamber contains no source shore of the displayed
   rectangle family, and its dihedral enlargement contains no
   calibrated four-top router shore.

The following remain open.

1. A literal tail-changing recharge circuit with the capacity (0.5).
2. Simultaneous companion completion and frozen-core compatibility for
   those recharges.
3. A low-collision final owner table and prefixwise nonnegative owner
   chronology.
4. Cancellation or useful endpoint placement of every recharge's
   signed traces and tags.
5. Coefficient one.

Thus the requested $\Theta(m)$-reuse circuit exists only in a null
homology class.  The exact capacity obstruction is not the number of
chronological rectangle occurrences; it is the number of times the
literal local boundary state is genuinely reset.

## Source dependencies

The literal rectangle identity is in
`MATH_THEOREM_NONCLOSED_BOUNDARY_RECTANGLE_LIFT_AND_DENSE_RECYCLING_GATE_20260727.md`.
The exact option-flow and synchronized-trail criteria are in
`MATH_THEOREM_COLLAR_NEUTRAL_RECTANGLE_BANK_LITERAL_SPLICE_AND_INSTALLABILITY_20260727.md`.
The earlier static capacity bound is in
`MATH_THEOREM_L_STATIC_COLLAR_NEUTRAL_RECTANGLE_CAPACITY_20260727.md`.
The master-order state is in
`MATH_THEOREM_PSI_TWO_BASE_EXCHANGE_FLATNESS_AND_ISOLATED_HIGH_STATE_20260727.md`.
The four-top words used in Corollary 6.2 are in
`MATH_THEOREM_K_CALIBRATED_FOUR_TOP_BOUNDARY_ROUTER_AND_SHARP_CLOSED_CHRONOLOGY_20260727.md`;
only their audited literal word patterns are used here, not any positive
closed-catalyst interpretation.

## Independent audit

An independent adversarial proof audit checked the intrinsic-versus-
certificate quotient, middle/nonmiddle tag scope, the complete
$K_{p,p}$ chronology, the exact $6p-4$ repeat census, same-orbit reset
quantifier in Theorem 4.1, the $2H$ phase locus, and the $H\ge11$
dihedral witness.  The corrections found by that audit are incorporated
above.  The certified implication scope is exactly unlabelled middle-
load capacity for the displayed rectangle/T4 families; it does not
assert provider-labelled control, an occurrence-squarefree factor, or
coefficient one.
