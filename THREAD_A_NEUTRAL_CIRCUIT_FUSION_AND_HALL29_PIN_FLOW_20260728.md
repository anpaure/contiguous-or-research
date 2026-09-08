# Thread A: neutral circuit hypertrees and the Hall-29 pin flow

Date: 2026-07-28

Status: unconditional degree-two circuit calculus, a protected-support
fusion theorem, exact direction and phase constraints, and a sharp audit of
the existing 24-pin witness.  No PBBS connector atlas or `k=15` compiler is
constructed.

## 0. Outcome

The direct-fusion lane has two logically different layers.

1. A signed endpoint change may preserve the two diamond shores and every
   owner degree **in total**.
2. A legal sequence requires a decomposition into dynamically applicable
   circuit packets, each of which preserves those quantities separately.

The first condition is the linear kernel

\[
                         Cg=Lg=Dg=0.                 \tag{0.1}
\]

It does not imply the second.  The exact positive sufficient object is an
edge-disjoint **neutral circuit hypertree**.  It joins all factor components,
keeps degree two and both diamond shores at every prefix, and preserves
depth-three support provided actual protected occurrences, rather than
target multiplicities, avoid its collars.

For a pure three-way `C6` hypertree on the canonical `k=15` PBBS factor,
the component count `c=73` forces exactly

\[
                         (73-1)/2=36                 \tag{0.2}
\]

literal `C6` packets.  This is only a topology count.  The Hall-29 compiler
interface is rooted and address-sensitive.  Its exact test requires a
35-target matching using the six old cells and 29 new cells, with at least
13 new nonsingleton cells.  The current displayed 24-pin witness is
complementary to one target at each old cell and has 22 nonsingleton new
addresses, so it passes this incidence relaxation.  It is still not a
controller rethreading: all 24 positive incidences require statewise rank
compensation, coordinatewise congruent deletions, and one literal final
chronology.

Thus neither the `36` topology count nor the `24` pin count is a construction.
The remaining certificate must couple the neutral hypertree, its component
phases, actual protected collars, and the full named target--cell matching.
It must also close the erosion-controller incidence ledger: named pins are
positive controller incidences and cannot be added without coordinatewise
congruent deletions.  The separated single-state version using only the
1,602 retained Hall-service pins is ruled out exactly: its 1,318-arc
replacement digraph is acyclic.  The larger theoretical UNIT graph is not
acyclic and can supply auxiliary deck circulation.  In the displayed
24-pin witness, ten pins do not admit even one isolated replacement, so any
realization must already use a non-isolated service block on those pins.

## 1. Exact degree-two circuit space

Let

\[
 \mathcal R=\binom{\Omega}{s-1},\qquad
 \mathcal A=\binom{\Omega}{s},\qquad
 \mathcal U=\binom{\Omega}{s+1}.
\]

A diamond cell is `(R,U)` with `R subset U` and `|U setminus R|=2`.
Its lift is the Johnson edge between the two intermediate `s`-sets.
Work with distinguishable copies throughout.  For a signed cell-copy vector
`g`, let

\[
 (Lg)_R=\sum_{U\supset R}g_{R,U},\qquad
 (Cg)_U=\sum_{R\subset U}g_{R,U},                 \tag{1.1}
\]

\[
 (Dg)_A=\sum_{R\subset A\subset U}g_{R,U}.        \tag{1.2}
\]

When `|Omega|=2s+1`, define the odd copy-incidence matrix

\[
 M_{X,N}(g)=
 \sum_{\substack{R\subset X\subset U\\U=\overline N}}g_{R,U}.
 \tag{1.2a}
\]

Let `z` be a binary exact owner 2-factor table and let `F=G_z` be its
lifted 2-factor.  Write `g=g^+-g^-` with disjoint nonnegative supports.

### Theorem 1.1 (exact neutral endpoint criterion)

Assume

\[
 g^-\le z,\qquad g^+\le1-z.                       \tag{1.3}
\]

Then `z'=z+g` is another binary owner 2-factor table with exactly the same
`R`-row and `U`-column vectors as `z` if and only if (0.1) holds.

Moreover, the red old edges `supp(g^-)` and blue new edges `supp(g^+)`
decompose conformally into edge-disjoint closed alternating circuits in the
lifted owner graph.  Toggling those circuits in any order preserves degree
two.  Every intermediate table has the original two shore vectors if and
only if every chosen circuit vector `g_Q` separately satisfies

\[
                         Lg_Q=Cg_Q=0.               \tag{1.4}
\]

For a literal undirected odd-factor lift, each packet must additionally
satisfy the transpose condition

\[
                         M(g_Q)=M(g_Q)^{\mathsf T}.  \tag{1.5}
\]

#### Proof

The inequalities (1.3) are exactly deletion availability and insertion
simplicity.  Equations `Lg=0` and `Cg=0` say precisely that every row and
column has its old multiplicity.  Equation `Dg=0` says that each owner loses
and gains the same number of incident edge copies, so its degree remains
two.  This proves the first assertion in both directions.

At every owner the number of incident red copies equals the number of
incident blue copies.  Pair red and blue half-edges locally and follow the
pairing until it closes.  Removing the resulting alternating circuit and
iterating gives a conformal edge-disjoint decomposition.  A circuit removes
and adds one incident edge at each of its visited owner occurrences, hence
preserves degree two.  If every circuit obeys (1.4), every partial sum has
zero `L`- and `C`-image.  Conversely, if every intermediate table has the
old shores, subtracting two consecutive prefix equations gives (1.4) for
the intervening circuit.  Finally, (1.5) is exactly the undirected
odd-incidence lift criterion. \(\square\)

The last converse is the first exact obstruction to a generic Markov
argument:

\[
 g\in\ker(C,L,D)
 \quad\not\Longrightarrow\quad
 \text{a shore-neutral alternating-circuit decomposition of }g. \tag{1.6}
\]

Endpoint neutrality may rely on cancellation between different circuits.
The common-retained-label odd `C6` is a positive packet because its two
opposite table `C6` pieces are already transpose-closed and shore-neutral.

## 2. Exact topology and successor flow

Let one applicable packet delete a matching `M^-` of old factor edges and
insert a matching `M^+` on the same exposed ports.  Delete `M^-` and
contract every maximal retained factor path, including a trivial path when
both old edges at one owner were cut.  Let `P` be the matching of ports
joined through these retained paths.  For matchings `Q_1,Q_2`, write
`kappa(Q_1,Q_2)` for the number of alternating cycles in their union.

### Theorem 2.1 (quotient component identity)

On the affected components,

\[
 c(F+g)-c(F)=\kappa(P,M^+)-\kappa(P,M^-).           \tag{2.1}
\]

Equivalently, after all old components touched by the move are cut into
retained path blocks, the new factor is connected on that region if and
only if the quotient formed by the added edges is connected.

#### Proof

Before insertion, the affected old cycles are exactly the alternating
cycles of `P union M^-`.  After insertion, the new cycles are exactly the
alternating cycles of `P union M^+`.  Re-expanding contracted paths changes
no component count. \(\square\)

In an oriented `r`-cut packet, write the old arcs as

\[
                         t_i\longrightarrow h_i
 \qquad(1\le i\le r)
\]

and install `t_i -> h_{pi(i)}`.  The head permutation makes all indegrees
and outdegrees one.  If `sigma` is the old successor monodromy, the new one
has the form

\[
                         \sigma'=\pi\sigma.          \tag{2.2}
\]

A supplied final successor matrix `H` is one directed cycle exactly when it
has row and column sums one and satisfies the subtour cuts

\[
 \sum_{A\in I,\ B\notin I}H_{A,B}\ge1
 \qquad(\varnothing\ne I\subsetneq\mathcal A).      \tag{2.3}
\]

Thus (2.3), not a component-count potential, is the exact final flow test.

The permutation sign gives

\[
 (-1)^{c(F+g)-c(F)}=\operatorname{sgn}(\pi).         \tag{2.4}
\]

Indeed, for a permutation on `N` symbols,
`sgn(sigma)=(-1)^(N-c(sigma))`; divide this identity for
`sigma'=pi sigma` by the identity for `sigma`.

A clean `C6` has `pi` a 3-cycle and therefore preserves component-count
parity.  The parity-changing two-cut transposition is a table rectangle,
but an isolated rectangle has `Dg ne 0`.  Consequently:

### Corollary 2.2 (smallest parity obstruction)

An even-component exact owner factor cannot be fused to one component by
clean `C6` packets alone.  For a clean **single alternating** `2r`-circuit,
parity breaking forces even `r`; the `r=2` circuit is the nonphysical
isolated rectangle, so such a parity breaker has even arity at least four.
This does not cover a compound derangement, such as cycle type `2+3` on
five cut ports.  Existence of a usable neutral arity-four packet is not
asserted.

## 3. Exact protected-support ledger

Here “depth three” means a window of three owners, i.e. trace depth `q=2`.
The signed theorem treats both the lower intersection and upper union
labels.  Compiler depth `q=3` uses four owners and a larger footprint.

Let

\[
                         F_0,F_1,\ldots,F_T          \tag{3.1}
\]

be an actual sequence of applicable neutral packets, with oriented
successors `sigma_t`.  At an owner `A`, define the two signed three-owner
labels

\[
 \lambda_t^-(A)=\sigma_t^{-1}A\cap A\cap\sigma_tA,
 \qquad
 \lambda_t^+(A)=\sigma_t^{-1}A\cup A\cup\sigma_tA. \tag{3.2}
\]

Only correct-rank labels are admitted.  Let `d_{t,S}^epsilon` and
`a_{t,S}^epsilon` count, with occurrence multiplicity, the actual old and
new labels at owners whose ordered triple changes at step `t`.

### Theorem 3.1 (time-expanded support identity)

For every signed target `(epsilon,S)` and every prefix `t`,

\[
 m_t^\epsilon(S)=m_0^\epsilon(S)+
 \sum_{j=1}^{t}
 \bigl(a_{j,S}^\epsilon-d_{j,S}^\epsilon\bigr).     \tag{3.3}
\]

Therefore final support is equivalent to the inequalities (3.3) at
`t=T`, whereas support at every intermediate factor is equivalent to them
for every prefix `1<=t<=T`, together with the correct-rank tests.

#### Proof

At one step, every unaffected ordered triple occurs on both sides and
cancels.  The changed triples contribute exactly `a-d`.  Induction
telescopes this identity.  Positivity of the resulting integer
multiplicity is exactly support. \(\square\)

The deltas in (3.3) must be evaluated in their actual current contexts.
A static sum of initial-context `C6` ledgers is invalid when packets share
an affected owner.  At the four-owner compiler depth, even edge-disjoint
seams have a mixed term when two seams are separated by only two retained
vertices: the window consisting of one left vertex, those two retained
vertices, and one right vertex is absent from both separate one-seam
ledgers.  This is the smallest multiseam obstruction.  Retained fragments
of length at least three eliminate this interaction at four-owner depth.

There is a strong noncircular sufficient certificate.  For every required
signed target choose one actual occurrence and call its supporting owner
triple its protected footprint.  A packet is protector-compatible when no
deleted transition meets any selected footprint.  Equivalently, with
protector variables `r_{S,o}` and packet variables `y_Q`, impose

\[
 \sum_{o\in\operatorname{Occ}(S)}r_{S,o}=1,
 \qquad
 r_{S,o}+y_Q\le1
 \quad\text{whenever }Q\text{ meets }\operatorname{dep}(o). \tag{3.4}
\]

The same construction may protect actual four-owner occurrences by using
their larger footprints.

## 4. Positive neutral-circuit hypertree theorem

Let `mathcal C` be the `c` initial components of `F_0`.  Let `mathcal Q`
be a fixed catalogue of literal circuit packets.  A packet `Q` is
**admissible** when:

1. it is individually neutral as in (1.4), physical as in (1.3), and has
   the required odd transpose lift;
2. it deletes exactly one old edge from each of `h_Q>=2` distinct initial
   components `S_Q subseteq mathcal C`, and its positive alternating half
   cyclically joins the resulting paths;
3. its deleted and added copies are disjoint from those of every other
   selected packet;
4. it is protector-compatible in the sense of (3.4).

For selected packets, form the bipartite incidence graph

\[
 I_y\quad\text{on}\quad
 \mathcal C\ \dot\cup\ \{Q:y_Q=1\},                \tag{4.1}
\]

joining `C` to `Q` when `C in S_Q`.

### Theorem 4.1 (protected neutral hypertree fusion)

If `I_y` is a tree, the selected packets can be ordered so that every
prefix is an exact degree-two factor with the original `R/U` shores and all
chosen protected targets.  The final factor is one cycle.

The tree condition is equivalent to the finite cut/count system

\[
 \boxed{\sum_Q(h_Q-1)y_Q=c-1,}                      \tag{4.2}
\]

\[
 \boxed{
 \sum_{Q:\ S_Q\cap I\ne\varnothing,\ S_Q\setminus I\ne\varnothing}
 y_Q\ge1
 \quad(\varnothing\ne I\subsetneq\mathcal C).      \tag{4.3}
\]

together with the packet edge-packing constraints.

#### Proof

Root `I_y` at one component and process circuit nodes outward.  When `Q`
is processed, its parent component lies in the already fused aggregate and
each of its other incident component nodes is still a fresh cycle.  Its old
edges are still present by packet disjointness.  Deleting one edge from
each of these `h_Q` cycles gives `h_Q` paths, and the positive half of `Q`
joins them cyclically into one.  Thus the fused aggregate absorbs
`h_Q-1` fresh components.  Induction ends with one component.

Every packet separately satisfies (1.4), so both shores and degree two are
preserved at every prefix.  Every protected footprint avoids all deleted
transitions, so it remains wholly inside a retained path and survives,
possibly reversed.  Intersections and unions are invariant under reversal.

The theorem preserves the designated supports.  It does not assert that
every newly formed `q=2` or `q=3` collar has the intended rank, avoids a
short return, or satisfies residence; those literal changed-collar tests
remain additional hypotheses for a compiler chronology.

For the equivalence, the incidence graph has

\[
 |E(I_y)|=\sum_Qh_Qy_Q,\qquad
 |V(I_y)|=c+\sum_Qy_Q.
\]

Equation (4.2) is exactly `|E|=|V|-1`.  The component cuts (4.3)
make the hypergraph, hence its incidence graph, connected.  A connected
graph with one fewer edge than vertices is a tree.  The converse is
immediate. \(\square\)

For `C6` packets, `h_Q=3`; hence `c` must be odd and exactly `(c-1)/2`
packets are selected.  At `k=15`, `c=73`, giving (0.2).  For the literal
common-retained `C6`, the three-owner lower ledger changes only at its six
named projected states.  Thus one exact sufficient audit for a putative
36-packet family's **lower** `q=2` support is to choose every lower protected
occurrence outside the union of those at most `216` state occurrences.
Upper `q=2` protectors require their own signed changed-state ledger.  No
analogous six-state claim is valid for four-owner `q=3` windows.

### Directed coherence

Give every initial component a reference orientation and every packet a
reference traversal.  For an incidence `C--Q`, let
`sigma_{C,Q} in F_2` record whether the deleted arc required by `Q` agrees
with the component reference.  Coherent directions are variables
`epsilon_C,eta_Q in F_2` satisfying

\[
                         \epsilon_C+\eta_Q=\sigma_{C,Q}. \tag{4.4}
\]

They exist if and only if the `sigma`-sum around every cycle of `I_y` is
zero.  In particular a hypertree is automatically direction-coherent.  The
smallest directed obstruction is an incidence `C4` with odd `sigma`-sum:
two packets may be undirectedly compatible across two components but have
no common successor orientation.

## 5. Rooted phase and named compiler pins

Named positions are not functions of the unrooted circuit-space vector.
After all old cut arcs are deleted, let `mathcal B` be the retained path
blocks, with lengths `ell_b`.  If the directed quotient has successor
permutation `pi`, choose a root phase `theta_b in Z/NZ` for each block.
Their exact transport equations are

\[
                         \theta_{\pi(b)}=
                         \theta_b+\ell_b\pmod N.     \tag{5.1}
\]

A local collar event at intrinsic offset `a` of block `b` has absolute
address `theta_b+a`.  Inconsistent equations of the form
`p-(theta_b+a)` are therefore a literal address obstruction.

There cannot be a cycle-space-only pin map: even with `g=0`, rotating the
root of a nonconstant factor changes which physical erosion word is called
position `p`.  Reversal creates the analogous ambiguity.  A theorem which
emits pins must therefore output a rooted, oriented final chronology.

For such a chronology

\[
                         \rho=(T_0,\ldots,T_{W-1}),
\]

put

\[
 P_p(\rho)=
 \bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T_i.          \tag{5.2}
\]

For a physical cell `J=[s,s+d]`, `d in {0,1,2}`, define

\[
 E_J(\rho)=\bigcup_{p\in J}P_p(\rho),               \tag{5.3}
\]

\[
 C_{i,x}(\rho)=\{p\in[i,i+3]:x\in P_p(\rho)\},     \tag{5.4}
\]

with boundary truncation, and

\[
 M_J(\rho)=
 \{x:\exists i,\ x\in T_i,\ 
       \varnothing\ne C_{i,x}(\rho)\subseteq J\}.  \tag{5.5}
\]

The exact lower compiler edge is

\[
 \boxed{
 S\sim_\rho J
 \iff
 S\subseteq E_J(\rho),\quad
 M_J(\rho)\subseteq S,\quad
 S\cap P_p(\rho)\ne\varnothing\ (p\in J).}         \tag{5.6}
\]

Thus making one coordinate enter one erosion position is not an exact cell
certificate.

At an orientation-coherent new seam

\[
 \cdots,L_{-2},L_{-1},L_0\mid R_1,R_2,R_3,\cdots
\]

placed after absolute index `b`, only three four-owner erosion positions
change locally, and

\[
 P'_{b+j}=
 \left(\bigcap_{a=0}^{3-j}L_{-a}\right)
 \cap
 \left(\bigcap_{a=1}^{j}R_a\right)
 \qquad(j=1,2,3).                                  \tag{5.7}
\]

A baseline unit **controller incidence** `(p,x)` is emitted at this seam
exactly when the corresponding four owners in (5.7) all contain `x`.  A
physical compiler pin additionally requires `x in A'_p` in the final
pinning and the complete cell predicate (5.6).  In a fixed intrinsic
block chart, a depth-`d` cell's envelope/nonempty predicate can change at
only `d+3` starts around one inserted seam, and its full mandatory predicate
at only `d+9` starts.  Hence the inserted-seam side of one literal `C6`,
with three new seams, meets at most

\[
                         3(9+10+11)=90              \tag{5.8}
\]

intrinsically named depth-zero/one/two cells, before overlaps and apart from
the opening root collar.  This is not a bound on the symmetric difference
of globally named old/new cells: deleted-seam collars also disappear, and a
block permutation transports absolute addresses.

#### Proof of (5.7)--(5.8)

A four-owner window avoiding the seam remains inside one inherited path and
is unchanged.  A window crossing it uses `4-j` owners from the left and `j`
from the right, giving (5.7).  The three possible values of `j` are the only
changed erosion positions.  A cell `[s,s+d]` meets one of these positions
only for `s in [b+1-d,b+3]`, giving `d+3` envelope starts.  Expanding the
four-position incidence sets in (5.4), only indices
`i in [b-2,b+3]` can change.  If a nonempty `C_{i,x}` is contained in
`J=[s,s+d]`, then `i in [s-3,s+d]`.  These intervals can meet only for
`s in [b-d-2,b+6]`, exactly `d+9` starts.  Summing `9,10,11` over the
three permitted physical depths and then over the three `C6` seams gives
(5.8). \(\square\)

An exact finite formulation may use binary rooted slot variables `w_{i,A}`
and binary transition variables `h_{i,A,B}`:

\[
 \sum_Aw_{i,A}=1,\qquad \sum_iw_{i,A}=1,            \tag{5.9}
\]

\[
 \sum_Bh_{i,A,B}=w_{i,A},\qquad
 \sum_Ah_{i,A,B}=w_{i+1,B},                         \tag{5.10}
\]

with `h_{i,A,B}=0` unless `AB` is a selected final factor edge, and with a
wrap equation in the cyclic case.  Equations (5.2)--(5.6) are then literal
finite predicates on `w`; no phase inference is hidden.

### Theorem 5.1 (controller-incidence balance for circuit pins)

Let `T` be a depth-`d` resident rank-`r` carrier, let `P` be its full
maximal erosion controller indexed by `0<=j<W+d`, including the clipped
boundary states, and for a coordinate `x` let

\[
 t_x=|\{i:x\in T_i\}|,\qquad
 p_x=|\{j:x\in P_j\}|,
\]

while `i_x` is the number of internal maximal `x`-runs in `T`.  Then

\[
 \boxed{p_x=t_x-d i_x+d u_x,}                       \tag{5.11}
\]

where `u_x=1` if `x` lies in every carrier state and `u_x=0` otherwise.
In particular, when no coordinate spans the whole carrier,
`p_x=t_x-d i_x`.

Consequently, if `T` and `T'` are both depth-`d` resident Johnson paths
enumerating the exact middle deck, and `P,P'` are their controllers, then

\[
                         p'_x-p_x\equiv0\pmod d      \tag{5.12}
\]

for every coordinate: an exact deck has `u_x=u'_x=0`.  Under an anchored
position comparison, additionally assume the two controllers have the same
prescribed positionwise rank/boundary profile, and put

\[
 A_j=P'_j\setminus P_j,\qquad B_j=P_j\setminus P'_j,
\]

and let `A_x,B_x` count the positions at which `x` is respectively added
and deleted.  The exact controller constraints include

\[
 |A_j|=|B_j|\quad(j\text{ arbitrary}),              \tag{5.13}
\]

\[
                         A_x-B_x\equiv0\pmod d
                         \quad(x\text{ arbitrary}).  \tag{5.14}
\]

#### Proof

An internal carrier run `[a,b]` erodes to `[a+d,b]` and loses exactly `d`
controller incidences.  A run meeting exactly one boundary is clipped and
loses none.  A run spanning the whole carrier occurs in all `W+d`
controller states and therefore contributes `d` incidences beyond its
`W` carrier incidences.  Summing proves (5.11).  In an exact middle deck,

\[
                         t_x=\binom{k-1}{r-1}
\]

is independent of the chronology and no coordinate is universal, so
subtracting (5.11) for `T,T'` gives (5.12).  Equation (5.13) is the assumed
equality of the prescribed ranks of `P_j,P'_j`.  Finally

\[
 p'_x-p_x=A_x-B_x,
\]

and (5.14) follows from (5.12). \(\square\)

At `k=15,r=8,d=3`,

\[
 \binom{14}{7}=3432\equiv0\pmod3,
\]

so every depth-three-resident exact-deck controller has `p_x=0 mod 3`
coordinatewise.  A named
pin which changes `x notin P_p` into `x in P'_p` is one positive incidence
in `A_x`; it must be balanced by (5.13) at that position and by (5.14)
globally.  This is independent of the diamond-row and protected-target
ledgers.

Controller incidence is still not physical pinning.  If `A'` is a word
with `D^dA'=T'` and `[u,v]` is an internal maximal `x`-run of `P'`, put

\[
 Q_x=\{j\in[u,v]:x\in A'_j\}.
\]

Then the exact coordinatewise lift condition is

\[
 u,v\in Q_x,\qquad q_{i+1}-q_i\le d+1
 \quad\text{for consecutive }q_i,q_{i+1}\in Q_x.    \tag{5.15}
\]

Indeed an occurrence at physical position `q` covers the carrier interval
`[q-d,q]`; these intervals cover the whole corresponding carrier run if
and only if the endpoint and gap conditions hold.  Every named physical
pin `(p,x)` additionally requires `p in Q_x`.  Boundary controller runs
obey the analogous clipped one-sided endpoint condition.

## 6. Exact test against the `k=15` Hall-29 interface

The frozen carrier has `W=6435`.  Its residual Hall core consists of 35
targets.  A minimal retained repair must use all six old cells

\[
\begin{array}{c|c}
15899&2420,2932\\
16597&4877,4909\\
18079&17683,21779\\
18088&2676,10868\\
18090&9524,9588\\
18985&19568,27760
\end{array}                                           \tag{6.1}
\]

and exactly 29 distinct new cells.  At least 13 of those new cells have
physical length two or three.  In this retained architecture all 1,489
peeled reservations must remain legal.  If they are rematched, the peeled
core and candidate graph must instead be recomputed.

Let `G_old` be the six-cell graph in (6.1).  Given a rooted final chronology,
choose a set `mathcal J_new` of exactly 29 cells, disjoint from the six old
cells and all frozen reservations.  Let `G_new(rho,mathcal J_new)` join a
residual target `S` to `J in mathcal J_new` exactly when (5.6) and all
frozen reservation/deadline conditions hold.  The exact retained
address-matching layer is

\[
 \boxed{
 \nu\bigl(G_{\rm old}\cup
 G_{\rm new}(\rho,\mathcal J_{\rm new})\bigr)=35,}     \tag{6.2}
\]

using all six old cells and 29 distinct new cells, with the length floor
above.  This is exact for the address-matching layer once the rooted
carrier and its individual cell predicates are supplied; simultaneous
realization by one common controller word remains an additional condition.
The six old pairs, 1,489 frozen reservations, and the 13-nonsingleton floor
are asserted only in this retained architecture.  A surgery which rematches
those data must recompute the peeled core and its candidate graph.

The positive-defect UNIT atlas is a restricted search architecture, not a
necessary model for arbitrary rethreadings.  For the designated UNIT
realization of one of its addresses, exposing the assigned pin is an
optimistic necessary local condition.  That assigned incidence is not
necessary for a broader surgery of the same address, and even within the
UNIT model it remains insufficient for the exact predicates, common
controller, and owner realization.

The audited unit-pin census proves that any 29-address matching in this
optimistic graph needs at least 24 distinct pins.  Equality uses all five
compatible double gains.  The current displayed 24-pin witness has 24
distinct erosion positions and 24 distinct uniquely missing middle-owner
indices.
Under an anchored, collar-local realization, one `C6` changes at most nine
positions of the form (5.2), so at least three `C6` packets would be needed.
This last bound is deliberately scoped: a global block permutation changes
absolute phases, so old names `(p,x)` must then be transported by (5.1) or
the atlas recomputed.

The coordinate multiplicities of those 24 named positive controller
incidences, in coordinate order `0,...,14`, are

\[
 (3,0,1,2,4,4,1,0,1,2,3,0,2,1,0).                 \tag{6.3}
\]

Therefore an anchored realization forces at least 24 controller deletions,
one at each of the 24 selected positions.  If these are the only positive
additions, there are exactly 24 such deletions and their coordinate vector
must have coordinate residues

\[
 (0,0,1,2,1,1,1,0,1,2,0,0,2,1,0)\pmod3.           \tag{6.4}
\]

With extra controller additions, their incidences must be added to the
left side before applying (5.14).  Thus (6.4) is a conditional equality
profile, while (5.13)--(5.14) are the unconditional exact constraints.

### Proposition 6.1 (the current 24-pin witness passes only the incidence relaxation)

The current authoritative witness in
`MATH_K15_HALL29_UNIT_PIN_COVER_20260728.md` supplies 24 UNIT pins serving
29 distinct new target/cell addresses.  Its complementary old assignments
are

\[
\begin{array}{c|c}
2932&15899\\
4877&16597\\
21779&18079\\
2676&18088\\
9588&18090\\
19568&18985
\end{array}.                                          \tag{6.5}
\]

Together these cover all 35 residual targets exactly once and avoid the
1,489 retained cells.  The new-cell physical-length profile is

\[
                         (n_1,n_2,n_3)=(7,15,7),      \tag{6.6}
\]

so 22 new cells are nonsingletons.  Hence the sharp 24-pin count, the six
old choices, and the 13-nonsingleton floor are jointly feasible in the
UNIT incidence relaxation.  They do not supply a controller satisfying
the seam/chronology realization behind (5.7), the constraints
(5.13)--(5.14), or one common physical pinning.

#### Proof

The displayed certificate has 29 distinct new targets and cells; (6.5)
uses the complementary six targets, one at each old cell.  Direct comparison
with the retained lists gives disjointness and complete coverage.  The
length profile sums to 29 and has `15+7=22` nonsingletons.  The final
sentence follows because the UNIT certificate specifies only demanded
positive incidences, not the compensating controller deletions or a legal
successor chronology. \(\square\)

### Theorem 6.2 (retained-service isolated UNIT cycle no-go)

Restrict a UNIT pin `(p,x)` to an isolated rank-preserving controller edit

\[
                         P'_p=P_p-y+x,\qquad
                         P'_j=P_j\ (j\ne p).          \tag{6.7}
\]

Require the two controller adjacencies at `p`, all four affected middle
unions, and every affected middle Johnson adjacency to remain legal.  Of
the 1,602 UNIT pin types in the retained Hall-service atlas:

\[
\begin{array}{c|r}
\text{type}&\text{count}\\ \hline
\text{one admissible isolated edit}&1318\\
\text{no admissible isolated edit}&283\\
\text{boundary pin outside the flat model}&1.
\end{array}                                           \tag{6.8}
\]

Every admissible edit replaces exactly one middle state

\[
                         T_q\longmapsto T_{q'},qquad q'\ne q. \tag{6.9}
\]

The resulting retained-service 1,318-arc digraph `q -> q'` on 2,295
indices is acyclic.  Consequently no nonempty pairwise
distance-at-least-eight family of edits (6.7) drawn only from this retained
atlas preserves the exact middle deck.  Only 14 of the 24 pins in the
displayed complementary witness admit even one edit of form (6.7), and no
one of the 1,318 isolated edits retains an address it advertises.

#### Proof

For a UNIT pin, exactly one of the four old middle states containing
`P_p` omits `x`.  In a locally legal replacement, adding `x` changes that
union.  Rank preservation forces the deleted `y` to disappear there, while
legality of the other three unions forces it to remain in them.  Hence
exactly one middle state changes, proving (6.9).

The counts and acyclicity in (6.8)--(6.9) are the exhaustive certificate in
`scratch/audit_k15_unit_pin_isolated_cycle_nogo.py`: Kahn elimination removes
all 2,295 vertices.  At separation eight the affected controller, union,
and adjacency collars are disjoint, so selected source indices `q` are
distinct and their replacements interact only through the deck multiset.
Exact-deck preservation requires every removed value `T_q` to be restored
by exactly one selected incoming arc.  Thus the selected arcs would form a
nonempty disjoint union of directed cycles, contradicting acyclicity.
The companion exhaustive certificate
`scratch/audit_k15_full_unit_compensation_cycles.py` recomputes every
advertised target envelope after the forced deletion and finds none
retained, proving the last assertion.
\(\square\)

The theorem is deliberately restricted.  It eliminates independent
Hall-service collars, including any attempt to realize the 24-pin witness
as 24 separated one-state swaps.  It does not apply to auxiliary UNIT
operations outside the retained atlas: the full theoretical graph has
10,370 locally admissible arcs and nontrivial directed cycles.  It also
does not exclude overlapping controller edits, multi-state alternating
deck circuits, global block rethreading, non-UNIT records, or a different
carrier.

### Proposition 6.3 (exact closed interacting deck-circuit target)

Let `J` be an arbitrary controller support in `0,...,W+2`.  Prescribe
states `P'_p` for `p in J` and leave every other controller state fixed,
using the full clipped rank profile

\[
              |P'_p|=8-\min\{3,p,W+2-p\}
              \qquad(0\le p\le W+2).                \tag{6.10a}
\]

Put

\[
                         T'_i=\bigcup_{p=i}^{i+3}P'_p. \tag{6.10}
\]

This modification is a depth-three-resident Johnson chronology enumerating
the same exact middle deck (possibly in a different order) if and only if
all of the following hold:

1. `P'` obeys the graded controller adjacency law: `P'_(p+1)` is obtained
   from `P'_p` by one deletion for `0<=p<3`, by one Johnson swap for
   `3<=p<W-1`, and by one addition for `W-1<=p<W+2`;
2. every `T'_i` has rank eight and
   `|T'_i triangle T'_(i+1)|=2`;
3. `P'` is the actual maximal erosion of `T'`:

   \[
   P'_p=\bigcap_{i=\max(0,p-3)}^{\min(p,W-1)}T'_i
   \qquad(0\le p\le W+2);                            \tag{6.11}
   \]

4. there is a permutation `phi` of `0,...,W-1` such that

   \[
                              T'_i=T_{\phi(i)}\quad(0\le i<W); \tag{6.12}
   \]

5. the statewise and coordinatewise controller balances
   (5.13)--(5.14) hold.  This last item is redundant under 1--4 but is
   retained as an exact derived pruning constraint.

The pin requirement adds `x in P'_p` and, for a physical lift,
`x in A'_p` for every selected `(p,x)`.  Any nontrivial solution supported
on pairwise distance-at-least-eight singleton edits would induce a directed
cycle in the graph of Theorem 6.2 and is therefore impossible.

#### Proof

Conditions 1--3 say that `P'` reconstructs a legal depth-three-resident
Johnson chronology and is its genuine maximal controller, including both
clipped boundary collars.
The old states `T_i` are all distinct and exhaust the rank-eight layer, so
the reconstructed chronology is the same exact deck precisely when its
state map is a permutation, which is (6.12).  Condition 5 is a necessary
consequence of the controller ranks and Theorem 5.1.  Conversely it adds
no new states; 1--4 already give an exact ordering of the deck, while 5 records its
required controller incidence closure.  The final assertion is Theorem
6.2. \(\square\)

Thus the next positive search object is not a collection of pin arcs but a
closed interacting pair `(P',phi)` satisfying (6.10)--(6.12), the neutral
factor-circuit flow, and the physical pinning rule (5.15) simultaneously.

### Corollary 6.4 (physical service forces a genuinely interacting collar)

For any solution of Proposition 6.3, let

\[
                         K=\{i:T'_i\ne T_i\}.
\]

Then `phi` restricts to a derangement of `K`, and the directed replacement
arcs

\[
                         i\longrightarrow\phi(i)     \tag{6.13}
\]

are a disjoint union of directed cycles.  If every connected controller
support cluster were a single flat Hall-service UNIT edit and distinct
clusters were at distance at least eight, all arcs (6.13) would belong to
the acyclic retained graph of Theorem 6.2, which is impossible unless `K`
is empty.  Moreover, no isolated Hall-service edit retains its advertised
target.  Hence a physical repair must contain a genuinely interacting
**service** cluster.  Its exported deck imbalance may still be closed by
distant, separated auxiliary UNIT operations from the ambient graph.

For the displayed 24-pin witness, at least ten named pins must occur in
such a non-isolated mechanism, because only fourteen of the twenty-four
admit an isolated edit at all.

#### Proof

Since the old middle states are distinct, `T'_i=T_i` is equivalent to
`phi(i)=i`.  Thus `K` is invariant under `phi`, and a permutation restricted
to its nonfixed points decomposes into directed cycles of length at least
two.  Under the separated-service-only hypothesis, Lemma 1.1 of the
isolated UNIT no-go identifies every arc with an arc of its retained
replacement digraph.  The resulting nonempty directed cycle contradicts
acyclicity.  The physical-service conclusion also uses the exhaustive
zero-retained-address statement in Theorem 6.2.  The last sentence is the
audited fourteen-of-twenty-four census. \(\square\)

This is the requested non-histogram calibration.  A hypothetical 36-`C6`
PBBS hypertree has ample raw seam capacity, and the revised 24-pin witness
passes the retained incidence flow.  The unsolved obstruction is its
physical lift.  A positive certificate must provide simultaneously:

1. the neutral and physical packet conditions (1.3)--(1.5);
2. hypertree cuts (4.2)--(4.3) and the direction equations (4.4);
3. actual prefix support or protected occurrences through the required
   depth;
4. rooted block phases (5.1) or slot variables (5.9)--(5.10);
5. controller rank, congruence, and physical pinning constraints
   (5.13)--(5.15);
6. a 35-target matching (6.2), including at least 13 nonsingleton new cells;
7. the exact predicates (5.6), all 1,489 reservations, and the upper,
   residence, endpoint, and owner conditions.

## 7. Proved/open boundary

Unconditionally proved here:

1. `ker(C,L,D)` is the exact endpoint-neutral degree-two space, while an
   exact sequence needs circuitwise shore neutrality;
2. the quotient matching formula (2.1) and one-cycle flow cuts (2.3);
3. the exact time-expanded support identity (3.3);
4. the protected neutral hypertree theorem and its cut formulation;
5. the direction cocycle and its smallest unbalanced-incidence-`C4`
   obstruction;
6. the `C6` component-parity obstruction and the arity-four lower bound for
   a clean single-circuit parity breaker;
7. the rooted phase and seam-to-pin equations;
8. the controller congruence and statewise rank constraints;
9. compatibility of the revised 24-pin equality witness with the six old
   Hall-cell choices and the 13-nonsingleton floor;
10. the acyclic replacement-digraph no-go for separated isolated UNIT edits
    drawn only from the retained Hall-service atlas; and
11. the resulting exact deck-cycle decomposition and forced interacting
    service collar, including the ten-of-twenty-four lower bound for the
    displayed witness.

Not proved:

1. a 36-packet common-retained `C6` hypertree in the canonical `k=15` PBBS
   factor;
2. a neutral parity bridge when it is needed;
3. a protected all-depth or residence-safe realization of such a family;
4. overlapping or multi-state closed deck circuits realizing all required
   named pins while preserving both shores;
5. any rooted phase assignment whose exact pin graph satisfies (6.2); or
6. a common literal controller/owner extension.

Accordingly, direct degree-two fusion remains viable but unclosed.  Its
minimum finite gate is no longer a scalar load condition: it is the joint
feasibility of the neutral-hypertree, protected-collar, rooted-phase, and
35-target address-flow systems above.  The companion note
`THREAD_A_K15_TWO_EXPORT_CONFLICT_CIRCULATION_20260728.md` constructs one
exact interacting deck circuit serving `6308`; its remaining first-shore
losses show why that positive controller closure does not close this gate.
