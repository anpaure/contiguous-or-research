# Fresh FIFO blocks are synchronized Boolean chains: exact exchange kernel and payload-atlas gate

**Date:** 2026-08-05  
**Method:** literal FIFO event calculus, integral path-flow switching, and
coordinatewise interval hitting; no computation or search  
**Status:** unconditional local normal form and sharp obstruction.  A fresh
depth-sized FIFO block is exactly a maximal chain in the synchronized product
of two Boolean lattices.  The complete integer fibre with prescribed owner
loads is connected by lifted alternating-cycle switches and vertex splices.
However, a one-copy owner chronology contains at most one path in a fixed
endpoint fibre, so none of those fixed-fibre switches is locally available:
an integral rounding theorem must change endpoints or use an external
absorber.  Positively, one lower block has explicit owner-disjoint `h`-fold
FIFO lifts, and a `2/3` mixture has exactly the required asymptotic duplicate
ledger up to one separator per macro.  Arbitrary payloads give an exact
coordinatewise interval-hitting criterion for named targets, not an arbitrary
independent target atlas.

## 1. A fresh depth-`d` FIFO block

Put `t=r-d`.  Choose pairwise disjoint sets

\[
 C,A,X,B\subseteq[k],\qquad |C|=t-d,\qquad |A|=|X|=|B|=d.       \tag{1.1}
\]

The lower state at the beginning of the block is

\[
                         S_0=C\mathbin{\dot\cup}A,              \tag{1.2}
\]

and the incoming ordered FIFO queue is

\[
                         Q_0=(x_1,\ldots,x_d),                  \tag{1.3}
\]

where `(x_1,...,x_d)` is an ordering of `X`.  Choose independently an
ordering `(a_1,...,a_d)` of `A` and an ordering `(b_1,...,b_d)` of `B`.
At transition `j`, delete `a_j` from the lower state and insert `b_j`.

### Theorem 1.1 (synchronized-chain normal form)

For `0<=j<=d`, the resulting queue, lower state, and owner are

\[
\begin{aligned}
 Q_j&=(x_{j+1},\ldots,x_d,a_1,\ldots,a_j),\\
 S_j&=C\cup\{a_{j+1},\ldots,a_d\}
          \cup\{b_1,\ldots,b_j\},\\
 T_j&=C\cup A\cup\{x_{j+1},\ldots,x_d\}
          \cup\{b_1,\ldots,b_j\}.                            \tag{1.4}
\end{aligned}
\]

Every transition is a legal delay-`d` FIFO transition.  Conversely, every
FIFO block in which

1. the `d` queue heads are distinct;
2. the next `d` lower deletions are distinct and belong to the initial lower
   state; and
3. the next `d` lower insertions are distinct and fresh outside the initial
   owner,

has the form (1.4), after relabelling.

#### Proof

Before transition `j`, the element `a_j` has not yet been deleted and hence
lies in `S_(j-1)`.  The fresh element `b_j` lies in neither `S_(j-1)` nor
`Q_(j-1)`.  The FIFO update therefore gives

\[
 Q_j=Q_{j-1}-x_j+a_j,
 \qquad
 S_j=S_{j-1}-a_j+b_j.
\]

Induction gives the first two rows of (1.4).  Their disjoint union gives the
third row; the deleted `a_i`'s merely move from the lower state into the
queue and hence all of `A` remains in every owner.  The converse follows by
naming the successive queue heads, lower deletions, and fresh insertions.
\(\square\)

The deletion order of `A` is invisible in the owner row.  It changes the
lower states and is exported as the final ordered queue

\[
                         Q_d=(a_1,\ldots,a_d).                  \tag{1.5}
\]

Thus it is genuine lower-side freedom, but not closed local freedom: it is
the incoming queue order seen by the next block.

## 2. The synchronized Boolean chain

Let

\[
 \mathcal Z_j(X,B)={X\choose j}\times{B\choose j},
 \qquad 0\le j\le d.                                          \tag{2.1}
\]

Join `(R,I) in Z_j` to `(R+x,I+b) in Z_(j+1)` whenever
`x in X\R` and `b in B\I`.  Write `Z_d(X,B)` for this layered directed
graph.  The owner map is

\[
 \Theta(R,I)=C\cup A\cup(X\setminus R)\cup I.                 \tag{2.2}
\]

It is injective on the union of the layers.  Equation (1.4) says that a
fresh FIFO owner block is precisely the image under `Theta` of a maximal
directed path from `(\varnothing,\varnothing)` to `(X,B)`.  Such a path is specified by
an ordering of `X` and an ordering of `B`, so there are `(d!)^2` paths.

Fix nonnegative integer loads `m(v)` on all vertices of `Z_d`.  A chain
packing with load `m` is a nonnegative integer vector `(n_P)` on maximal
paths satisfying

\[
                         \sum_{P\ni v}n_P=m(v)                 \tag{2.3}
\]

for every vertex `v`.

There are two elementary load-preserving operations.

* **Vertex splice.**  If two selected paths meet at a vertex `v`, exchange
  their suffixes after `v`.
* **Rank-cycle switch.**  In the bipartite graph between `Z_j` and
  `Z_(j+1)`, take a simple alternating cycle
  \[
   u_1v_1u_2v_2\cdots u_hv_hu_1.                              \tag{2.4}
  \]
  If one selected path uses each edge `u_i v_i`, write that path as a
  prefix ending at `u_i`, followed by `u_i v_i`, followed by a suffix
  beginning at `v_i`.  Replace it by the same prefix, the edge
  `u_i v_(i-1)`, and the suffix formerly beginning at `v_(i-1)` (indices
  cyclically).

### Theorem 2.1 (exact integral chain-fibre connectivity)

Any two chain packings with the same vertex-load vector `m` are connected
by vertex splices and rank-cycle switches through nonnegative integer chain
packings with the same loads.  Equivalently, the integer kernel of the
maximal-path versus vertex-incidence matrix of `Z_d(X,B)` is generated by
the signed vectors of these two operations.

#### Proof

For a chain packing, let `f_j(e)` be the number of selected paths using edge
`e` between layers `j` and `j+1`.  Its degrees on the two shores are the
prescribed vertex loads.  Hence, for two packings with the same loads,
`f_j-f'_j` is an integral zero-margin vector on that bipartite graph.

Every integral zero-margin vector on a bipartite graph decomposes into
signed simple alternating cycles.  More precisely, begin at an edge with
`f_j>f'_j`; the zero row and column sums alternately supply an edge of the
opposite sign until a vertex repeats.  Removing the resulting alternating
cycle and iterating gives the decomposition.  Choose one currently selected
path through every negative edge of such a cycle and perform the
rank-cycle switch.  The prefixes and suffixes are merely permuted, so all
vertex loads and all edge loads at ranks other than `j` are unchanged,
while the `L1` distance from `f_j` to `f'_j` decreases.  Repetition makes
the edge-load vectors agree at every rank.

It remains to compare two decompositions into maximal paths of the same
layered integral edge flow.  At each internal vertex, a decomposition is a
bijection between its incoming edge occurrences and its outgoing edge
occurrences.  Two such bijections differ by transpositions.  A
transposition is exactly a vertex splice of the corresponding two paths.
Working through the vertices layer by layer transforms one decomposition
into the other without changing any edge load.  This proves connectivity
and the kernel statement. \(\square\)

The synchronized graph has genuine quadratic switches.  If `1<=j<=d-2`,
take

\[
 |R|=j-1,\quad |I|=j,
 \quad x_1,x_2\in X\setminus R,
 \quad b_1,b_2\in B\setminus I.                               \tag{2.5}
\]

Then the two lower vertices

\[
 (R+x_1,I),\qquad(R+x_2,I)
\]

and the two upper vertices

\[
 (R+x_1+x_2,I+b_1),\qquad(R+x_1+x_2,I+b_2)
\]

form a `C4`.  Thus, unlike the one-bank Boolean incidence graph, the first
owner-changing circuit can be quadratic.  At `d=2` there is no internal
rank supporting such a cycle; the internal vertex load already determines
the path.

## 3. The one-copy endpoint obstruction

The preceding connectedness theorem is an abstract chain-packing theorem,
not yet an owner-Hamilton rounding theorem.

### Proposition 3.1 (fixed-endpoint exchanges are unavailable at owner load one)

Every maximal path of `Z_d(X,B)` contains the same two endpoint owners

\[
 C\cup A\cup X,qquad C\cup A\cup B.                           \tag{3.1}
\]

A directed owner chronology which uses every owner at most once can
therefore contain at most one directed block from this fixed endpoint
fibre.  For one selected path, its vertex-incidence vector determines it
uniquely.  Consequently no nontrivial move from Theorem 2.1 can be applied
inside one fixed endpoint fibre of an owner-bijective chronology.

#### Proof

The endpoint assertion is (2.2) at the bottom and top vertices.  Two
same-oriented paths in the chronology would give two successors at the
first endpoint (and two predecessors at the second), contradicting the
one-copy directed owner condition.  Finally, a single path uses one vertex
at each layer, and those vertices are nested along the unique displayed
edges; its vertex set therefore reconstructs the path. \(\square\)

Thus the exact local kernel has been identified, but it also gives a sharp
local no-go: a useful owner-neutral exchange must change endpoint fibres,
release and reabsorb endpoint owners, or pass through an external absorber.
The static two-containment-transversal theorem and the uniform fractional
queue circulation do not supply that endpoint-changing circuit.

The invisible deletion order in (1.5) does not evade the obstruction.  It
preserves the current block's owners but changes the ordered queue exported
to the next block, and hence changes the next block's owner path.  Any use
of this freedom must close its queue-order holonomy over a compound packet.

### Theorem 3.2 (exact `h`-fold punctured duplicate lift)

There is nevertheless an explicit endpoint-changing local supply theorem.
Choose pairwise disjoint sets

\[
 C,A,B,U,X_1,\ldots,X_h
\]

with

\[
 |C|=t-d,\qquad |A|=|X_c|=d,\qquad |B|=d-1,
 \qquad U=\{u_1,\ldots,u_h\}.                                  \tag{3.2}
\]

This requires only

\[
                         t+(h+1)d+h-1\le k.                    \tag{3.3}
\]

Order `A=(a_1,...,a_d)`, `B=(b_1,...,b_(d-1))`, and each
`X_c=(x_1^c,...,x_d^c)`.  Define the common lower block

\[
 S_j=C\cup\{a_{j+1},\ldots,a_d\}
          \cup\{b_1,\ldots,b_j\},
 \qquad 0\le j<d.                                             \tag{3.4}
\]

For copy `c`, put

\[
 Q_j^c=(x_{j+1}^c,\ldots,x_d^c,a_1,\ldots,a_j),
 \qquad
 T_j^c=S_j\mathbin{\dot\cup}Q_j^c                            \tag{3.5}
\]

for `0<=j<d`.  At the last transition delete `a_d` and insert `u_c`,
giving

\[
 S_d^c=C\cup B\cup\{u_c\},\qquad
 Q_d^c=(a_1,\ldots,a_d),\qquad
 T_d^c=C\cup A\cup B\cup\{u_c\}.                             \tag{3.6}
\]

Then:

1. every displayed transition is a legal delay-`d` FIFO transition;
2. all `h(d+1)` owners `T_j^c` are pairwise distinct; and
3. the first `d` lower values `S_0,...,S_(d-1)` occur identically in all
   `h` copies, while the terminal lower states are distinct.

Thus one copy may supply a complete anchor occurrence of a depth-sized
lower block and the other `h-1` copies are literal owner-disjoint duplicate
occurrences of that entire block.

#### Proof

For `j<d`, equations (3.4)--(3.5) are the FIFO induction from Theorem 1.1.
All inserted `b_j` and `u_c` are fresh outside the current owner, so the
last transition is legal as well and gives (3.6).

Within one copy, the pair

\[
 (|T_j^c\cap B|,|T_j^c\cap X_c|)=(j,d-j)
\]

distinguishes the internal owners.  For distinct copies `c,c'`, every
internal owner of copy `c` contains a nonempty suffix of `X_c`, while no
owner of copy `c'` contains an element of `X_c`.  The terminal owners contain
no queue-bank element and are distinguished by `u_c`.  A terminal owner
cannot equal an internal owner for the same reason.  This proves pairwise
owner disjointness.  The lower identities are explicit in (3.4)--(3.6).
\(\square\)

For `h=2`, condition (3.3) is `r+2d+1<=k`; for `h=3`, it is
`r+3d+2<=k`.  Both hold in the central regime for all sufficiently large
`k`.  The theorem is dynamic: it is stronger than merely assigning the same
lower label to two containing owners.

### Corollary 3.3 (the `2/3` multiplicity ledger closes up to separators)

Assume, as an additional input, that the rank-`t` layer has been partitioned
into `B_0=M/d` fresh Johnson blocks of `d` vertices (ignore a final block of
fewer than `d` vertices when divisibility fails).  Put

\[
                         H=\left\lfloor{W\over d+1}\right\rfloor. \tag{3.7}
\]

At the optimal central deadline, for all sufficiently large dimensions,

\[
                         2B_0\le H\le3B_0.                     \tag{3.8}
\]

Hence one may assign multiplicity two or three to every block, with total
multiplicity `H`.  The macros then contain

\[
                         d(H-B_0)                              \tag{3.9}
\]

duplicate lower positions and use `(d+1)H` owners.  If `d` divides `M`,
the deficit from the ideal duplicate count `U=W-M` is exactly

\[
 U-d(H-B_0)=W-dH=H+\bigl(W-(d+1)H\bigr)=O(W/d).               \tag{3.10}
\]

#### Proof

The ratio in (3.8) tends to

\[
 {H\over B_0}\sim {d\over d+1}{W\over M}
       \longrightarrow e^{\pi/4},                             \tag{3.11}
\]

which lies strictly between two and three.  Therefore a `2/3` mixture with
sum `H` exists.  One of the `h` copies of a block is its anchor and `h-1`
are duplicates, giving (3.9).  Substituting `dB_0=M` and writing
`W=(d+1)H+[W-(d+1)H]` proves (3.10). \(\square\)

The divisibility remainder changes only `O(d)` lower vertices and does not
alter the `O(W/d)` scale.  Corollary 3.3 is a scalar macro ledger, not a
packing theorem.  The missing integral statement is now especially sharp:
choose the queues and terminal insertions of all these `h`-fold macros so
that owners belonging to **different** macros are also disjoint, fill the
`O(W/d)` separator owners, and join the macros into one directed cycle.

### Corollary 3.4 (independent payload copies after one anchor)

In Theorem 3.2, retain one of the `h` copies at its maximal antecedent to
anchor every value `S_0,...,S_(d-1)`.  In each of the other `h-1` copies,
the corresponding depth-sized source block may be thinned independently
between its mandatory cores and maximal envelopes.  In particular, every
free copy carries an independent arbitrary payload word on the common core,
with the same private marker addresses.

#### Proof

The copies have disjoint owner positions and are separated by their terminal
states.  The short-gap mandatory-core theorem applies to each copy
independently, while the retained copy lies outside the free bank and keeps
one occurrence of every lower value. \(\square\)

Marker addresses are repeated across the free copies, so this does not make
their named interval values automatically disjoint.  Their independently
chosen payloads must still satisfy the exact target criterion in Section 5.

### Theorem 3.5 (exact fractional `2/3` macro factor)

Let \(\mathcal P_h\) be the complete orbit, under coordinate relabelling and
all displayed order choices, of the `h`-fold macros in Theorem 3.2.  Regard
one macro as a hyperedge containing its `d` common lower vertices and its
`h(d+1)` distinct owners.  Put

\[
                         \rho={W\over M}.                       \tag{3.12}
\]

If

\[
                         2\le {\rho d\over d+1}\le3,           \tag{3.13}
\]

then the union of the `h=2` and `h=3` macro orbits has an exact fractional
factor which gives weight one to every rank-`t` lower vertex and weight one
to every rank-`r` owner.

#### Proof

Give every macro in \(\mathcal P_h\) the common weight

\[
                         w_h={M\over d|\mathcal P_h|}.          \tag{3.14}
\]

The total weighted lower incidence is `M`.  Coordinate transitivity makes
the marginal the same on every one of the `M` lower vertices, so that
marginal is exactly one.  The total weighted owner incidence is

\[
                         {M\over d}h(d+1).
\]

Coordinate transitivity on the owner layer therefore gives owner marginal

\[
                         \eta_h={h(d+1)\over \rho d}.           \tag{3.15}
\]

Set

\[
 \lambda_3={\rho d\over d+1}-2,
 \qquad
 \lambda_2=3-{\rho d\over d+1}.                               \tag{3.16}
\]

Condition (3.13) says that these numbers are nonnegative, and their sum is
one.  Weight orbit `h` by `lambda_h w_h`.  The lower marginal remains one,
while (3.15)--(3.16) give owner marginal

\[
 {d+1\over\rho d}(2\lambda_2+3\lambda_3)=1.                  \tag{3.17}
\]

This is the asserted fractional factor. \(\square\)

At the optimal central deadline, \(\rho\) tends to \(e^{\pi/4}\) and `d` tends
to infinity, so (3.13) holds in every sufficiently large dimension.  Thus
the new macro formulation has no scalar or fractional lower/owner
separator.  Its remaining obstruction is the integral matching of these
growing, correlated macro edges, followed by their chronological joining.

### Proposition 3.6 (vanishing same-shore macro codegrees)

Fix `h=2` or `h=3` and use the complete labelled macro orbit
\(\mathcal P_h\).  Let `deg_h(v)` be the number of macros containing a
resource `v`, and `codeg_h(v,w)` the number containing both.  Uniformly for
distinct resources on the same shore,

\[
 {\operatorname{codeg}_h(v,w)\over\operatorname{deg}_h(v)}
                         =O\!\left({d\over k^2}\right).        \tag{3.18}
\]

For a lower vertex `S` and an owner `T`, the analogous conditional ratio is
at most

\[
 O\!\left({d\over {k-t\choose d}}\right)                     \tag{3.19}
\]

whenever the pair can co-occur.

#### Proof

Fix a rank-`t` lower vertex `S`.  Its stabilizer is transitive on the lower
vertices at Johnson distance `ell`; their number is

\[
                         N_\ell={t\choose\ell}{k-t\choose\ell}. \tag{3.20}
\]

A macro containing `S` has only `d-1` other lower vertices.  Summing the
codegrees over one distance orbit and using transitivity therefore gives

\[
 {\operatorname{codeg}_h(S,S')\over\operatorname{deg}_h(S)}
                         \le {d-1\over N_\ell}.                \tag{3.21}
\]

All co-occurring lower pairs have `ell=O(d)`.  In the central range
`d=o(k)`, the numbers (3.20) are increasing over the relevant nonzero
distances, so `N_ell>=t(k-t)=Theta(k^2)`.

The owner calculation is identical.  There are

\[
                         {r\choose\ell}{k-r\choose\ell}       \tag{3.22}
\]

owners at distance `ell` from a fixed owner, while a macro has only
`h(d+1)-1=O(d)` other owners.

Finally, the stabilizer of a lower `S` is transitive on rank-`r` owners
with `|S\setminus T|=q`; that orbit has size

\[
                         {t\choose q}{k-t\choose d+q}.         \tag{3.23}
\]

For the co-occurring range `0<=q=O(d)`, its minimum is attained at `q=0`
for all sufficiently large central parameters and equals `{k-t choose d}`.
There are only `h(d+1)=O(d)` owners in a macro, proving (3.19). \(\square\)

These bounds are precisely the local sparsity expected by a nibble.  They
do not by themselves invoke one: the macro edge size grows like
`d=Theta(sqrt(k))`, the `h=2,3` mixture has two resource ratios, and the
final theorem needs the prescribed lower anchors, the `O(W/d)` leave, and
chronological endpoint compatibility simultaneously.

In particular, the fixed-uniformity matching theorems cannot simply be
diagonalized with requested relative leave `1/d`.  The quantifier and
growing-rank issue is the same one audited in

`MATH_AUDIT_MACROSCOPIC_COLLAR_GROWING_UNIFORMITY_MATCHING_THEOREMS_20260803.md`.

### Theorem 3.7 (terminal permutation and exact cycle merging)

Fix one `h`-fold macro from Theorem 3.2 through its penultimate states.
For an arbitrary permutation \(\pi\in\operatorname{Sym}(U)\), replace the
last transition of
copy `c` by

\[
 (S_{d-1},Q_{d-1}^c)
   \longrightarrow
 (C\cup B\cup\{u_{\pi(c)}\},A).                               \tag{3.24}
\]

Every such terminal assignment is legal.  As \(\pi\) varies, the complete
multisets of owners, lower states, and ordered queues are unchanged.  Only
the pairing between the `h` penultimate states and the `h` terminal states
changes.

Consequently, in any directed queue-state cycle cover containing the macro,
a transposition of two terminal assignments merges the two cycles containing
the corresponding last transitions when they are distinct, and splits one
cycle when both transitions lie on the same cycle.

#### Proof

Every `u_c` is fresh outside every penultimate owner.  Thus copy `c` may
delete its final queue head and lower label and insert any
\(u_{\pi(c)}\).
The terminal states are still exactly

\[
 (C\cup B\cup\{u_c\},A),\qquad1\le c\le h,                    \tag{3.25}
\]

and their owners are still exactly
\(C\cup A\cup B\cup\{u_c\}\).  All
earlier states are untouched.  This proves literal resource neutrality.

For two assignments, the operation replaces directed arcs

\[
                         p_1\to v_1,\quad p_2\to v_2
\]

by

\[
                         p_1\to v_2,\quad p_2\to v_1.          \tag{3.26}
\]

The standard directed 2-break joins two cycles when the old arcs belonged
to distinct cycles, and cuts one cycle into two when they belonged to one.
\(\square\)

Define the **macro component graph** of a cycle cover to have one vertex per
directed cycle and, for every macro, a clique on the cycles containing its
copies.  If this graph is connected, a spanning tree of it and successive
terminal transpositions merge the entire cover into one cycle without
changing any owner, lower fibre, duplicate block, or internal payload
occurrence.  Hence topology after integral macro packing is only a graphic
connectivity gate.  What is not automatic is that the macro component graph
of some owner-disjoint packing is connected.

## 4. Minimum-run singleton sites live at block boundaries

At an internal lower state `S_j`, `1<=j<d`, the incoming lower insertion is
`b_j` and the outgoing lower deletion is `a_(j+1)`.  Its mandatory source
core is therefore

\[
                         F_j=\{b_j,a_{j+1}\}.                  \tag{4.1}
\]

It has size two because `A` and `B` are disjoint.  Hence a completely fresh
block contains no internal singleton source cell.

Now concatenate two fresh blocks so that the terminal lower state of the
first is the initial lower state of the second.  If `b_d` is the last
insertion of the first block and `a'_1` is the first deletion of the next,
the shared state's mandatory core is

\[
                         F_\partial=\{b_d,a'_1\}.               \tag{4.2}
\]

### Proposition 4.1 (prescribed singleton separator)

The shared boundary is a singleton compiler site exactly when

\[
                         b_d=a'_1.                              \tag{4.3}
\]

Given any coordinate in the shared active bank, the two orders may be
chosen so that it is last inserted and first deleted.  Conditional on a
chain of fresh blocks, one may therefore place one prescribed
minimum-owner-run singleton at every block boundary.

#### Proof

Equation (4.2) is the mandatory incoming/outgoing endpoint formula.  It is
a singleton exactly under (4.3).  The last and first elements of the two
orders are freely prescribed. \(\square\)

Only `k` such sites are needed to represent all singleton targets, whereas
the duplicate-block programme has `Theta(W/d)` separators.  Thus singleton
coverage is not a scalar obstruction to a block construction.  It is a
real chronological requirement: at least `k` block boundaries must be
linked with the last-in/first-out equality (4.3).

## 5. Exact named-target criterion for an arbitrary payload block

Let `G` be any good free block of length at most `d` in the mandatory-core
theorem.  Let `F_p` be its mandatory cores and let `C_G` be the common core,
disjoint from all private incoming markers.  Choose payload letters

\[
                         H_p\subseteq C_G\qquad(p\in G)         \tag{5.1}
\]

and source letters \(A_p=F_p\cup H_p\).  For an interval
\(I\subseteq G\),
put

\[
                         F(I)=\bigcup_{p\in I}F_p.              \tag{5.2}
\]

Suppose a family \(\mathcal I\) of intervals has prescribed named target
values `Z_I`.  Define, when possible,

\[
                         R_I=Z_I\setminus F(I).                 \tag{5.3}
\]

### Theorem 5.1 (coordinatewise payload-atlas criterion)

There are payload letters (5.1) satisfying

\[
                         \bigcup_{p\in I}A_p=Z_I
                         \qquad(I\in\mathcal I)                \tag{5.4}
\]

if and only if

1. \(F(I)\subseteq Z_I\) and \(R_I\subseteq C_G\) for every assigned
   interval; and
2. for every `x in C_G`, every assigned interval `I` with `x in R_I`
   contains a position outside the union of all assigned intervals `J`
   with `x notin R_J`:
   \[
    I\cap\left(G\setminus
       \bigcup_{\substack{J\in\mathcal I\\x\notin R_J}}J\right)
       \ne\varnothing.                                       \tag{5.5}
   \]

#### Proof

For a coordinate `x in C_G`, put

\[
                         E_x=\{p:x\in H_p\}.                   \tag{5.6}
\]

Equation (5.4) is equivalent, coordinate by coordinate, to

\[
                         x\in R_I\quad\Longleftrightarrow\quad
                         E_x\cap I\ne\varnothing.              \tag{5.7}
\]

Every negative interval in (5.7) forces

\[
 E_x\subseteq G\setminus
       \bigcup_{J:x\notin R_J}J.                               \tag{5.8}
\]

Hence (5.5) is necessary for each positive interval.  Conversely, if
(5.5) holds, choose one point of the displayed difference for every
positive interval and let `E_x` be the union of the chosen points.  It
meets every positive interval and, by construction, no negative interval.
Doing this independently for every `x` and defining `H_p` through (5.6)
proves sufficiency.  The mandatory coordinates give condition 1.
\(\square\)

If all singleton intervals and all longer intervals of `G` are assigned,
condition (5.5) reduces to the transparent semilattice identity

\[
 \boxed{
                         R_[a,b]=\bigcup_{p=a}^{b}R_{\{p\}}
                         \quad\hbox{for every }[a,b]\subseteq G.}
                                                                    \tag{5.9}
\]

Indeed, the singleton assignments determine `E_x` exactly.  Thus an
arbitrary payload word lifts its own complete interval deck losslessly,
but it does **not** make the `d(d+1)/2` named targets in a block independent.
Their residuals must themselves be an interval-union deck, or, for a
partial assignment, satisfy the exact coordinate cuts (5.5).

Private incoming markers still ensure that distinct intervals have
distinct lifted values.  They solve occurrence collision, not the named
value equations.

## 6. Consequence for the integral rounding programme

The delayed-queue route now has the following exact division.

1. **Within a proposed fresh block**, the complete FIFO trajectory and its
   owner chain are (1.4).
2. **For a multiset of chains with prescribed owner loads**, Theorem 2.1 is
   the complete exchange graph and integer kernel.
3. **At owner load one**, Proposition 3.1 prevents every fixed-endpoint
   chain exchange, but Theorem 3.2 supplies literal owner-disjoint
   endpoint-changing duplicate macros.
4. **At the aggregate level**, Theorem 3.5 gives an exact fractional
   `2/3` macro factor and Proposition 3.6 gives vanishing local codegrees.
   Integral growing-rank packing is not supplied by a current black box.
5. **After an integral cycle cover is found**, Theorem 3.7 reduces joining
   it to connectivity of the macro component graph.
6. **After blocks are placed**, Theorem 5.1 is the exact named-target
   payload gate.  The arbitrary-payload recursion does not by itself prove
   a complete lower atlas.
7. **Singleton targets** may be paid at separators by (4.3), but those
   equalities must be built into the compound endpoint circuit.

The single next theorem for the **integral queue/fibre layer** is now:

> **Connected integral `2/3` macro-factor theorem.**  For every sufficiently
> large central parameter, select pairwise owner-disjoint `h=2,3` macros
> from Theorem 3.2, together with `O(W/d)` separator states, so that:
>
> 1. every rank-`r` owner occurs exactly once;
> 2. the anchor copies together with the separator states contain every
>    rank-`t` lower value;
> 3. the other copies contain `U-O(W/d)` lower occurrences in separated
>    depth-sized duplicate blocks;
> 4. the ordered queues close to a directed cycle cover whose macro
>    component graph is connected; and
> 5. at least `k` chosen terminal boundaries satisfy the last-in/first-out
>    equality (4.3).

Theorem 3.7 would turn item 4 into one owner-bijective queue cycle without
altering items 1--3 or 5.  This would close the exact integral rounding
asked for by the duplicate-block queue programme.

It would not yet finish the lower compiler.  The remaining named-target
theorem is to assign the free-copy payloads so that all target residuals
satisfy the coordinate cuts (5.5).  That target assignment can be studied
after the macro factor because Corollary 3.4 makes the payload choices
owner-invisible.

This note proves no connected integral macro factor, no complete named-target
atlas, no arbitrary-upper deck, and no universal OR word.

## 7. Dependencies

The FIFO lift and owner criterion are in

`MATH_THEOREM_DELAY_D_JOHNSON_QUEUE_LIFT_AND_DUPLICATE_BLOCK_TARGET_20260805.md`.

The exact static/fractional reductions are in

`MATH_THEOREM_DELAY_QUEUE_DUPLICATE_BLOCK_EXACT_PACKING_AND_TWO_BANK_INCIDENCE_20260805.md`.

The mandatory-core and arbitrary-payload results are in

`MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md`

and

`MATH_THEOREM_SHORT_GAP_ARBITRARY_PAYLOAD_MARKER_RECURSION_20260805.md`.
