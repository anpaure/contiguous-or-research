# Recharge source allocation: the static matching cut and the exact resolvable-flow gate

Date: 2026-07-27

Method: pure mathematics only. No computation, search, solver, web input,
or probabilistic black box is used.

## 0. Outcome

Put

\[
 n=2m,\qquad M=m+H,\qquad \kappa=4H-1,\qquad
 d=M-\kappa=m-3H+1,
\tag{0.1}
\]

Also define the certified direction capacity

\[
                         g=M-8H-3=m-7H-3.
\tag{0.1a}
\]

Indeed, relative to a fixed third position, there are exactly \(g\)
positions whose two open cyclic arcs from it both contain at least
\(4H+1\) labels.  These are the uniformly certified remote positions
from the local recharge theorem.  In the calibrated regime \(g>0\) and
\(g=m-O(H)\).

Write also

\[
 N=\binom{2m}{M},\qquad W=\binom{2m}{m},\qquad
 \lambda=\frac WN.
\tag{0.2}
\]

Assume the calibrated regime

\[
 H=o(m),\qquad M\le\lambda=M+O(H).
\tag{0.3}
\]

Thus

\[
 dN=W-O(HN)=W-o(W).
\tag{0.4}
\]

Use the literal three-top collar-neutral recharge packet from
`MATH_THEOREM_THREE_TOP_COLLAR_NEUTRAL_REROOTING_AND_LINEAR_RECHARGE_20260727.md`.
One packet has three source paths on three distinct rank-\(M\) tops,
their common squarefree support has \(3d\) middle owners, and switching
the packet changes one literal rectangle direction at each of the three
tops while preserving every protected aggregate trace exactly.

The global source-allocation conclusions are as follows.

1. The role-labelled packet orbit is a \((3+3d)\)-uniform resource
   hypergraph.  Its exact top and owner degrees are

   \[
       D_T=3(m-H)M!,\qquad
       D_X=\frac{3d(m!)^2}{(m-H-1)!},\qquad
       \frac{D_X}{D_T}=\frac d\lambda<1.
   \tag{0.5}
   \]

2. No matching in this hypergraph can solve the recharge problem.  A
   matching has at most \(N/3\) packets and therefore exposes at most

   \[
                              N=o(W)
   \tag{0.6}
   \]

   useful rectangle directions.  This remains true even if the matching
   covers \(W-o(W)\) middle owners.  In fact a top-perfect matching
   would use exactly \(dN=W-o(W)\) owners but still expose only \(N\)
   directions.

3. Fresh-catalyst schedules do not evade the cut.  Any chronology in
   which each recharge step introduces two previously unused companion
   tops is a forest.  If it begins with \(r\) roots and has \(T\) steps,
   then

   \[
                              r+2T\le N.
   \tag{0.7}
   \]

   Even crediting all three top-directions of every packet, it exposes
   at most \(3T\le3N/2=o(W)\) directions.

4. Consequently any construction exposing \(gN-o(W)=W-o(W)\) distinct
   directions must use at least

   \[
       \left(\frac{2g}{3}-1\right)N-o(W)
       =\left(\frac23-o(1)\right)W
   \tag{0.8}
   \]

   companion incidences at tops which have already appeared.  Recycled
   companion cycles are required on positive \(W\)-scale; fresh
   catalysts can only seed the circulation.

5. There is no fractional top/owner capacity obstruction after this
   necessary reuse is admitted.  Giving every role-labelled packet the
   common weight \(g/D_T\) loads every top exactly \(g\), every owner
   exactly

   \[
                              \frac{gd}{\lambda}<g,
   \tag{0.9}
   \]

   and has total packet weight \(gN/3\).  Counting three directions per
   packet gives exactly \(gN=W-o(W)\) units of quotient direction mass.

6. The fractional point is not yet a source schedule.  Repeating one
   packet \(g\) times obeys the quotient top/owner capacities but repeats
   the same three directions and alternates the same two shores.  The
   exact remaining object is a **resolvable state flow**: about \(g\)
   successive top/owner matchings whose target shore at one time is the
   literal source shore at the next, with every top-direction used at
   most once.

Thus the requested ordinary source matching has a sharp linear
obstruction.  The local recharge theorem has not failed; rather, its
fresh-companion realization has the wrong global topology.  A
coefficient-one proof must build a cyclic/recurrent packet flow, not a
matching or a forest of fresh companions.

## 1. The source-packet resource hypergraph

Let

\[
 {\cal U}=\binom{[2m]}M,\qquad {\cal X}=\binom{[2m]}m.
\tag{1.1}
\]

Fix one role-labelled collar-neutral recharge template.  A labelled
copy \(P\) consists of an injection of its \(M+1\) active roles—the
\(M-2\) common-core positions and the three endpoint roles
\(x,a,y\)—into \([2m]\).  It has:

* a set \({\cal U}(P)\subset{\cal U}\) of three tops;
* a source triple \({\cal S}^-(P)\) of one rooted path on each top;
* a target triple \({\cal S}^+(P)\) on the same tops; and
* a common middle-owner support

  \[
                         {\cal O}(P)\subset{\cal X},
                         \qquad |{\cal O}(P)|=3d.
  \tag{1.2}
  \]

The exact local theorem gives

\[
 \operatorname{mid}{\cal S}^-(P)
 =\operatorname{mid}{\cal S}^+(P)=1_{{\cal O}(P)},
\tag{1.3}
\]

and both triples are squarefree.  At each of the three tops, the old
and new states have different first-two-swap traces.  Denote these
three directed resources by

\[
                         {\cal R}(P)=\{r_0(P),r_1(P),r_2(P)\}.
\tag{1.4}
\]

The **source resource hypergraph** \({\cal H}_{\rm rec}\) has vertex
set \({\cal U}\dot\cup{\cal X}\), and one edge

\[
                 E(P)={\cal U}(P)\dot\cup{\cal O}(P)
\tag{1.5}
\]

for every role-labelled copy.  Hence every edge has rank

\[
                              3+3d.
\tag{1.6}
\]

The two shores give the same edge in this projection.  Shore choice is
a state transition decorating (1.5), not another top/owner column.

## 2. Exact orbit degrees and the favorable size bias

There are exactly

\[
 |{\cal P}|=(2m)_{M+1}=\frac{(2m)!}{(m-H-1)!}
\tag{2.1}
\]

role-labelled copies, with harmless multiplicity when two copies induce
the same unlabelled resource edge.  The symmetric group is transitive on
tops and on owners.  Incidence counting therefore gives

\[
 ND_T=3|{\cal P}|,
 \qquad
 WD_X=3d|{\cal P}|.
\tag{2.2}
\]

Since

\[
 N=\frac{(2m)!}{M!(m-H)!},
 \qquad
 W=\frac{(2m)!}{(m!)^2},
\tag{2.3}
\]

we obtain

\[
 \boxed{
 D_T=3(m-H)M!,\qquad
 D_X=\frac{3d(m!)^2}{(m-H-1)!}.}
\tag{2.4}
\]

Dividing the two incidence identities in (2.2) yields the more useful
form

\[
                         \boxed{\frac{D_X}{D_T}
                                      =\frac{dN}{W}
                                      =\frac d\lambda.}
\tag{2.5}
\]

Because \(d=M-(4H-1)\) and \(\lambda=M+O(H)\),

\[
 \frac d\lambda=1-\Theta(H/m)
\tag{2.6}
\]

up to the harmless choice of the calibrated constant.  Thus owner
capacity is slightly more abundant than top capacity in the quotient
problem.  This is the exact size bias supplied by puncturing
\(4H-1\) phases.

## 3. The static matching cut

Let \({\cal M}\) be any matching in \({\cal H}_{\rm rec}\).  Top
disjointness and owner disjointness give respectively

\[
                    3|{\cal M}|\le N,
 \qquad
                    3d|{\cal M}|\le W.
\tag{3.1}
\]

Since \(W/d=(\lambda/d)N>N\), the top inequality is the sharper one:

\[
                         |{\cal M}|\le\frac N3.
\tag{3.2}
\]

One packet changes at most one rectangle direction at each of its three
tops.  Therefore

\[
             \left|\bigcup_{P\in{\cal M}}{\cal R}(P)\right|
             \le3|{\cal M}|\le N=o(W).
\tag{3.3}
\]

There are \(g\) uniformly certified remote direction slots per top,
hence

\[
                              gN=W-o(W)
\tag{3.4}
\]

top-position direction slots in the calibrated target.  Even granting
that all directions in (3.3) are useful and distinct, the missing
direction mass is at least

\[
                         (g-1)N=W-o(W).
\tag{3.5}
\]

This is the first quantitative obstruction.

### Owner coverage does not measure direction supply

Suppose, optimistically, that a matching has \(N/3-o(N)\) packets.
Its used owner mass is

\[
                 3d|{\cal M}|=dN-o(W)=W-o(W),
\tag{3.6}
\]

because

\[
                 W-dN=(\lambda-d)N=O(HN)=o(W).
\tag{3.7}
\]

Thus a packet matching may be almost perfect as an owner cover and
simultaneously miss almost every required rectangle direction.  The
identity of the owner shores, though essential for legal switching,
does not multiply the number of exposed top states.

No strengthening of a one-layer Hall theorem can remove (3.5): it is
the total top row of the incidence matrix.

## 4. Fresh companions form a subcritical forest

The local recharge theorem constructs a length-\(t\) schedule at one
focal top by using two fresh companion tops at each step.  The following
count applies to any arrangement of such schedules, not only to one
star.

### Theorem 4.1 (fresh-catalyst forest cut)

Consider a chronological family of recharge steps.  Initially mark
\(r\) tops as roots.  Assume that each step uses one previously present
focal top and introduces two companion tops not used in any earlier
step.  If the family has \(T\) steps, then

\[
                              r+2T\le N.
\tag{4.1}
\]

Consequently it exposes at most

\[
                              3T\le\frac32(N-r)=o(W)
\tag{4.2}
\]

distinct rectangle directions.

#### Proof

The roots and the two companions introduced at different steps are all
distinct.  They are rank-\(M\) tops, of which there are only \(N\),
proving (4.1).  A recharge packet changes only its three incident top
directions, giving (4.2). \(\square\)

The coefficient-one owner cut says the same thing in another unit.  A
source table on \(r+2T\) distinct tops has \(d(r+2T)\) distinct owners.
Since \(dN\le W\), this is compatible with (4.1) but cannot improve it.

### Corollary 4.2 (positive-density recycling is necessary)

Let a chronology have \(T\) recharge steps and touch at most \(N\)
tops.  Count the two companion incidences at every step.  At most \(N-r\)
of these can be first appearances, so at least

\[
                              2T-(N-r)
\tag{4.3}
\]

companion incidences reuse an already present top.

To expose \(gN-o(W)\) directions, even at the optimal rate of three
new directions per step one needs

\[
                              T\ge\frac{gN-o(W)}3.
\tag{4.4}
\]

Substitution in (4.3) gives

\[
 \#\{\text{reused companion incidences}\}
 \ge\left(\frac{2g}{3}-1\right)N-o(W)
 =\left(\frac23-o(1)\right)W.
\tag{4.5}
\]

Thus the fresh-catalyst freedom is locally sufficient but globally
subcritical by a factor \(\Theta(m)\).  Almost all useful recharge mass
must lie in a companion circulation.

## 5. The exact symmetric fractional circulation point

The obstruction disappears at the level of total capacities once tops
and owners may be reused \(g\) times.  Give every role-labelled packet
the common weight

\[
                              z_P=\frac g{D_T}.
\tag{5.1}
\]

At a fixed top the load is exactly

\[
                              D_Tz_P=g.
\tag{5.2}
\]

At a fixed owner it is

\[
                         D_Xz_P=\frac{gd}{\lambda}<g.
\tag{5.3}
\]

The total packet weight is, by \(ND_T=3|{\cal P}|\),

\[
             \sum_{P\in{\cal P}}z_P
             =\frac{g|{\cal P}|}{D_T}
             =\frac{gN}{3}.
\tag{5.4}
\]

Crediting the three incident directions gives

\[
                           3\sum_Pz_P=gN=W-o(W).
\tag{5.5}
\]

The pointwise owner slack is

\[
                   g-\frac{gd}{\lambda}
                   =\frac{g(\lambda-d)}{\lambda}
                   =\Theta(H),
\tag{5.6}
\]

and the relative slack is \(\Theta(H/m)=o(1)\).  Thus the quotient
top/owner LP has exactly the required scale and no hidden Gaussian
capacity deficit.

This proves a fractional source-packing theorem.  It is stronger than
an average-degree heuristic: every top constraint is met with equality
and every individual owner constraint has the explicit slack (5.6).

## 6. Why quotient rounding is insufficient

An integral \(g\)-matching in the resource hypergraph would be a
multiset of packets satisfying

\[
 \deg(U)\le g\quad(U\in{\cal U}),\qquad
 \deg(X)\le g\quad(X\in{\cal X}).
\tag{6.1}
\]

Even a perfect solution of (6.1) does not give \(gN\) useful
directions.  Fix one packet \(P\) and take it with multiplicity \(g\).
This vector satisfies (6.1) on its own resources, after scaling to that
component, but it alternates the same two shores and exposes only the
same three top-directions.  More generally, quotient multiplicity does
not distinguish repeated uses of one rectangle context from distinct
position-three labels.

Therefore every correct relaxation needs a third resource shore:

\[
                 {\cal A}=\{(U,\rho):
                    \rho\text{ is an admissible rooted rectangle
                    direction on }U\}.
\tag{6.2}
\]

Each packet contains three direction atoms \({\cal R}(P)\subset{\cal
A}\), and these atoms require capacity one.  The local theorem supplies
\(g\) mutually different certified atoms along one focal schedule, but the
three atoms of different packets are synchronized by their companion
source states.

There is a second, independent defect.  A packet may be counted after
another packet at a top only if its literal source path equals the
current target path.  Top degree in (6.1) records neither this equality
nor its chronology.  Thus ordinary dependent rounding, even if it
preserved every top and owner capacity, would not prove applicability.

## 7. The exact resolvable state-flow formulation

Let \({\cal S}\) be the set of all rooted length-\(d\) path states on
rank-\(M\) tops.  For \(s\in{\cal S}\), write

\[
                         U(s)\in{\cal U},\qquad
                         O(s)\subset{\cal X},\quad |O(s)|=d.
\tag{7.1}
\]

A **coefficient-one table** is a set \({\cal T}\subset{\cal S}\)
such that

\[
 |\{s\in{\cal T}:U(s)=U\}|\le1
 \quad(U\in{\cal U}),
\tag{7.2}
\]

and the owner sets \(O(s)\), \(s\in{\cal T}\), are pairwise disjoint.

Every recharge packet is a directed hyperarc

\[
               P:\quad {\cal S}^-(P)\longrightarrow{\cal S}^+(P)
\tag{7.3}
\]

with three states on each side, the same three tops, and

\[
       \dot\bigcup_{s\in{\cal S}^-(P)}O(s)
       =\dot\bigcup_{s\in{\cal S}^+(P)}O(s).
\tag{7.4}
\]

Thus firing \(P\) inside a coefficient-one table preserves the complete
owner incidence vector exactly.

### Definition 7.1 (resolvable source packing, RSP)

An RSP of length \(L\) consists of coefficient-one tables

\[
                         {\cal T}_0,{\cal T}_1,\ldots,{\cal T}_L
\tag{7.5}
\]

and, for each \(0\le j<L\), a top-disjoint packet family \({\cal
M}_j\) such that:

1. every source state of \({\cal M}_j\) lies in \({\cal T}_j\);
2. \({\cal T}_{j+1}\) is obtained by simultaneously replacing all
   source triples by their target triples;
3. all unfired states are unchanged;
4. the direction atoms used over all layers are distinct; and
5. the total number of direction atoms is \(gN-o(W)\).

By (7.4), every table in an RSP has exactly the same owner incidence
vector.  No additional owner rounding is needed after \({\cal T}_0\)
is installed.

Conversely, any literal chronology of collar-neutral recharge packets
in a coefficient-one table canonically gives an RSP by grouping
simultaneously applicable, top-disjoint firings into successive layers.
Thus RSP is an exact reformulation, not a sufficient surrogate.

### Necessary circulation scale

If \(a_U\) is the total number of used direction atoms at top \(U\),
then an RSP satisfying item 5 obeys

\[
                 \sum_Ua_U=gN-o(W),\qquad 0\le a_U\le g.
\tag{7.6}
\]

Hence all but \(o(W)\) of the total top-direction capacity, in the
precise weighted sense \(\sum_U(g-a_U)=o(W)\), must be used.  The
average top participates in

\[
                              g-o(m)=\Theta(m)
\tag{7.7}
\]

distinct state transitions.  This is the precise sense in which a
positive result must be recurrent rather than fresh.

## 8. What the cuts do and do not prove

The following statements are proved.

1. The exact source-resource hypergraph and its top/owner degrees.
2. A linear missing-direction obstruction for every ordinary matching.
3. The stronger forest obstruction for every fresh-companion schedule.
4. The necessity of \((2/3-o(1))W\) recycled companion incidences.
5. The exact symmetric fractional \(g\)-fold packing with pointwise
   owner slack \(\Theta(H)\).
6. The direction-reuse error in the quotient \(b\)-matching LP.
7. The exact stateful RSP formulation of the remaining global gate.

The following are not proved.

1. An integral rounding of the \(g\)-fold fractional point with distinct
   direction atoms.
2. A decomposition into chronologically applicable packet layers.
3. An initial near-perfect coefficient-one table containing the first
   source layer.
4. A global RSP with \(gN-o(W)\) directions.

Accordingly, there is a decisive obstruction to the source **matching**
requested in the prompt, but not yet to the source **circulation**.  The
next positive target is a resolvable triangle-flow on path states in
which switched companion rows become later source rows on positive
density.  Any construction which continues to allocate two new tops to
each recharge is quantitatively incapable of coefficient one.
