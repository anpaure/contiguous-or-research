# `k=17`: pure refinement is socket-support monotone, but singleton closure is not q1 matching

Date: 2026-08-01  
Status: exact theorem for the deliberately relaxed two-block residence and
immediate lower/upper projection.  It gives a monotone repair operation, a
conditional two-cut support-cover theorem, a fixed-socket lower bound, a
finite joint recut selector, and an unrestricted literal finite upper bound.  It does
**not** prove an exact-resident chronology, a connected Hamilton carrier,
the deeper upper deck, a compiler, or `nu(17)=24313`.

## 1. Socket form of the relaxed seam predicate

Let a cut factor path be

\[
 P=(T_0,T_1,\ldots,T_{m-1}),\qquad |T_i|=r.
\]

It has a left socket at `T_0` and a right socket at `T_{m-1}`.  At either
socket, look inward along the path.  For a coordinate `x` in the endpoint
owner, let

\[
 a_P(x)=
 \begin{cases}
 \infty,&x\text{ occurs in every owner of }P,\\
 \min\{d+1,\text{length of its inward endpoint run}\},&\text{otherwise}.
 \end{cases}                                             \tag{1.1}
\]

For coordinates absent from the endpoint put `a_P(x)=0`.

Consider sockets `s=(A,a)` and `t=(B,b)` belonging to different pieces.
Assume `A` and `B` are distinct Johnson neighbours, and write

\[
 A-B=\{p\},\qquad B-A=\{q\},\qquad C=A\cap B.
\]

### Theorem 1.1 (exact socket criterion)

The oriented seam from `s` to `t` passes the relaxed necessary two-block
residence predicate if and only if

\[
 \begin{aligned}
 &C\text{ is a selected deleted lower colour},\\
 &a(p)\ge d+1,\qquad b(q)\ge d+1,\\
 &a(x)+b(x)\ge d+1\quad(x\in C),                         \tag{1.2}
 \end{aligned}
\]

where `infinity` satisfies every inequality.  The relation is symmetric.

#### Proof

At a seam, `p` is deleted, `q` is inserted, and every `x in C` continues
through the seam.  A non-all deleted endpoint run is legal exactly when its
length exceeds `d`; the same holds for the inserted run.  A continuing run
has length `a(x)+b(x)` and is legal exactly when this exceeds `d`.  The code's
`all` exception is precisely the value `infinity`.  These are all coordinate
cases in `relaxed_pair_resident`.  \(\square\)

Define the **socket graph** `S(C)` to have the two physical sockets of every
piece as vertices and an edge for every pair satisfying (1.2).  Label an
edge `st` by

\[
 \ell(st)=A\cap B,\qquad u(st)=A\cup B.                  \tag{1.3}
\]

The first label has rank `r-1` and the second rank `r+1`.

### Corollary 1.2 (local orientation row and global socket matching)

Considered locally, a piece has an incoming and outgoing seam in one common
orientation if and only if both of its physical sockets are nonisolated in
`S(C)`.  This is only a pair of singleton statements: the two chosen seams
may compete with choices required by other pieces or colours.

More strongly, selecting one seam at every physical socket produces an
alternating union of piece paths and seam edges.  Every component is a cycle
and can be oriented consistently.  Conversely, every common-orientation
cycle cover selects one edge at every socket.

#### Proof

In forward orientation the left socket is incoming and the right socket is
outgoing; reversing the piece swaps the roles.  Since (1.2) is symmetric, a
socket that supports one direction supports the reverse direction after the
two incident pieces are reversed.  Thus one orientation works precisely
when each of the two sockets has an edge.  Degree one at each socket makes
the union with the fixed internal piece paths 2-regular, and hence a union of
orientable cycles.  \(\square\)

This explains the dense audit exactly.  Its 187 zero tail states and 187
zero head states are not two unrelated shores: they are the two directed
views of exactly 187 isolated physical sockets.  The `44/143` left/right
origin split records which old outer socket is isolated.

Likewise, a cut-killed rank-ten target `U` is a zero row exactly when

\[
             u^{-1}(U)=\varnothing                       \tag{1.4}
\]

in the same socket graph.  Thus the 187 endpoint rows and the 78 rank-ten
rows are two label projections of one edge-extension problem.

From this point onward assume the authenticated ambient factor is
**lower-rainbow**: its factor gaps have pairwise distinct lower labels and
use every required lower colour once.  Thus uncut gaps supply the unselected
colours internally, and selected gaps are in bijection with `K(C)`.

### Theorem 1.3 (exact bow-tie/three-resource core)

Let `K(C)` be the selected deleted lower colours.  A common-orientation
lower-q1-exact cycle cover exists if and only if there is a set
`M subset E(S(C))` such that

\[
 \deg_M(s)=1\quad(s\text{ a physical socket}),\qquad
 |M\cap\ell^{-1}(K)|=1\quad(K\in K(C)).                 \tag{1.5}
\]

It is immediate-upper complete exactly when, in addition,

\[
 \#\{\text{uncut internal factor edges labelled }U\}
   +|M\cap u^{-1}(U)|\ge1
 \quad\left(U\in\binom{[17]}{r+1}\right).              \tag{1.6}
\]

#### Proof

If `M` satisfies the socket degrees, its union with the fixed piece paths is
2-regular.  Orient each alternating cycle; this gives one common orientation
per piece and one incoming/outgoing seam at every piece.  The second family
in (1.5) is exactly lower-colour bijectivity, while (1.6) is the complete
internal-or-crossing upper-support ledger.  Conversely, forgetting the
directions of any such cycle cover gives `M` and all three displayed rows.
\(\square\)

Thus the three perfect pairwise projections `TH`, `TC`, and `CH`, and even
absence of every singleton zero, are only necessary projections of (1.5).
The full row is a coloured perfect matching on the socket graph.  Its
smallest obstruction can be a two-physical-edge/four-directed-seam bow tie.

## 2. Pure refinement cannot create a new relaxed zero

Suppose a currently resident piece `P` is split at one of its internal
factor gaps into `P_L,P_R`.  Retain every old cut and add the new gap colour.

### Theorem 2.1 (refinement monotonicity)

Under pure refinement:

1. every old outer socket persists, and its age vector can only increase in
   the coordinatewise order with `infinity` as the largest value;
2. every old socket edge remains legal;
3. the two new internal sockets have their old factor adjacency as a legal
   socket edge;
4. the new edge has the deleted factor colour as lower label and the former
   internal factor union as upper label.

Consequently pure refinement creates neither a new isolated physical socket
nor a new rank-`r+1` zero-provider target.  Both zero sets are monotone
decreasing under any sequence of further cuts.

#### Proof

Look at an old outer socket.  If an endpoint run ends before the new cut,
its length is unchanged.  If it reaches the new cut, it occupies the entire
new child and its value changes to `infinity`.  This proves part 1, and every
inequality in (1.2) is monotone in the age vectors, proving part 2.

For the two new sockets, consider one coordinate at the restored old factor
gap.  If its run crosses the gap and meets neither old outer boundary, that
run was internal to the old resident piece and therefore has length at least
`d+1`.  If it meets an old outer boundary, it occupies the whole
corresponding child and receives value `infinity`.  If the coordinate is
deleted or inserted at the gap, the same argument applies to its one-sided
run.  Hence (1.2) holds for the old factor adjacency.  Its intersection and
union are exactly the deleted factor lower colour and the old internal upper
colour.  This proves parts 3 and 4 and the conclusion.  \(\square\)

This is the repair lemma that the prospective unary-support discussion was
missing at the **relaxed socket** level.  Splitting destroys an intact
two-ended *piece state*, but it does not destroy either old physical socket
or any relaxed seam incident with that socket.  Exact cyclic residence is
different: an all-one child exports state through its other boundary, so the
full product automaton is still required downstream.

### Corollary 2.2 (no-casualty joint targeting)

Any family of further cuts whose new socket edges hit the 187 isolated
sockets and the 78 missing upper labels repairs those rows simultaneously;
no previously live socket or upper target has to be guarded against a new
zero at this projection.

Interactions can create additional providers, but never delete a provider.
Thus branch-and-cut on further refinements may use only positive zero-row
cuts at this stage.

### Corollary 2.3 (q1 matching feasibility is also refinement-monotone)

In the present lower-rainbow factor, if a cut bank has a set `M` satisfying
(1.5)--(1.6), every pure refinement has one as well.

#### Proof

For one new cut, retain every edge of `M` on the persistent old outer
sockets and add the canonical old factor edge between the two new internal
sockets.  By Theorem 2.1 this edge is legal; it uses exactly the newly selected
lower colour and restores exactly the upper union lost when that internal
factor edge was cut.  Hence (1.5)--(1.6) remain true.  Iterate for several
cuts. \(\square\)

There is no converse implication: an UNSAT bank can acquire alternative
cross edges under refinement, and no theorem here makes UNSAT persistent.
Monotonicity says that once the bow-tie core is solved, further pure
refinement cannot destroy that q1 solution; it does not say singleton support
alone solves the core.

### The authenticated zero/zero counterexample

The current zero-singleton bank has no isolated socket, no lower-colour zero,
no rank-ten zero, and all three pairwise projections perfect, but its exact
system (1.5) is UNSAT.  The verified 14-clause/five-lemma core in
`MATH_THEOREM_K17_DENSE_ZERO265_Q1_BOWTIE_UNSAT_CORE_20260801.md` consists of
three pieces, two degree-two colours, and four seams.  Choosing one seam of
each colour either overloads one socket state or forces opposite orientations
of the central piece.  All four seams share the same upper label, so (1.6)
cannot see the contradiction.

Accordingly the next cut CEGAR column must add an alternative seam for one
core colour, change the central socket incidence, or replace one selected
colour.  This is a fixed-bank obstruction, not a no-go for further
refinement or cut exchange.

### Theorem 2.4 (two-cut endpoint-singletonization cover)

Let `S_raw(C)` be the socket graph obtained by retaining the Johnson and
selected-lower-colour conditions but omitting all age inequalities in
(1.2).  For a physical socket `s` on a nonsingleton resident piece, let
`b(s)` be the first retained factor gap inward from that socket.  For a
singleton piece put \(b(s)=\varnothing\).  Call `s` **freely isolable** when
\(b(s)=\varnothing\) or `b(s)` is an allowed, unprotected extra cut.

For a raw socket edge `e=st`, put

\[
 B(e)=\{b(s),b(t)\}\setminus\{\varnothing\}.             \tag{2.1}
\]

Let `I_0` be the current isolated-socket bank and `U_0` the current
rank-`r+1` zero-label bank.  The task set serviced by `e` is

\[
 R(e)=\bigl(\{s,t\}\cap I_0\bigr)
       \mathbin\cup
       \bigl(\{u(e)\}\cap U_0\bigr).                    \tag{2.2}
\]

Suppose \(E_*\subseteq E(S_{\rm raw}(C))\) consists of edges with freely
isolable ends and satisfies

\[
                    I_0\mathbin{\dot\cup}U_0
                       \subseteq\bigcup_{e\in E_*}R(e).  \tag{2.3}
\]

Then cutting

\[
                         D_* =\bigcup_{e\in E_*}B(e)     \tag{2.4}
\]

eliminates every row of `I_0` and `U_0` in the relaxed socket projection,
creates no new isolated socket or upper-label zero, and uses at most

\[
                              |D_*|\le2|E_*|             \tag{2.5}
\]

extra cuts.

In particular, if every task in \(I_0\mathbin{\dot\cup}U_0\) belongs to
`R(e)` for at
least one such raw edge, then one may choose at most one witness edge per
task and obtain

\[
                              |D_*|\le2(|I_0|+|U_0|).     \tag{2.6}
\]

#### Proof

Cutting `b(s)` makes the old endpoint owner of `s` a singleton piece.  Every
coordinate present in that owner therefore has socket age `infinity`; if
`s` was already singleton, this was true without a cut.  After making the
cuts in `B(e)` at both ends of a raw edge `e=st`, the deleted coordinate,
inserted coordinate and every common coordinate in (1.2) all meet their
inequalities.  Thus `e` is a legal relaxed socket edge.  It nonisolates its
isolated ends and supplies its upper label.

Apply this argument to every edge of `E_*`.  The cuts can be made in any
order: each is inside a currently resident descendant piece, and Theorem
2.1 preserves every edge made legal earlier while self-supplying the new
cut colour and the two new sockets.  Hence all rows covered in (2.3) are
simultaneously repaired and no new row is created.  Equations (2.5)--(2.6)
follow because every witness edge names at most two cuts. \(\square\)

The sharp optimization on this construction face is the labelled cover

\[
 \min\left\{
   \left|\bigcup_{e\in E_*}B(e)\right|:
   I_0\mathbin{\dot\cup}U_0\subseteq\bigcup_{e\in E_*}R(e)
 \right\}.                                                \tag{2.7}
\]

This is a monotone set-cover problem, not Hall: one split may activate many
socket edges, and one witness edge may service two sockets and one upper
label without consuming any of them in a final matching.  Hall becomes
relevant only after support closure, when actual seam atoms must be assigned
capacity one.

For the authenticated dense bank, `|I_0|+|U_0|=187+78=265` and the raw audit
has no socket or rank-ten singleton zero.  Therefore (2.6) gives the
conditional bound `|D_*|<=530` provided the chosen raw witnesses have freely
isolable ends.  That last protected-gap condition has not been audited for
all 265 tasks, so `530` is a theorem under the displayed cover hypothesis,
not a certified refinement of the frozen bank.

### Theorem 2.5 (canonical transparent refinement lift)

Let `C` be any segmentation into resident pieces and let `M` be a selected
socket perfect matching on `C`.  Suppose `M` uses every currently selected
deleted lower colour once.  Refine the pieces at any allowed internal gap
set `D`.  For each `g in D`, let `e_g` be the old factor edge across `g`, now
viewed as the seam between the two new internal sockets.  Then

\[
                         M_D=M\mathbin{\dot\cup}
                                  \{e_g:g\in D\}          \tag{2.8}
\]

is a socket perfect matching on the refined pieces and uses every refined
deleted lower colour once.  Expanding each old piece into its consecutive
children joined by the `e_g` preserves the contracted cycle/path topology
and the complete physical owner chronology exactly.

Consequently any exact residence, arbitrary-width interval deck, source or
compiler certificate which is a certificate of that physical owner
chronology transports literally under this canonical lift.  A certificate
which treats an old piece as an indivisible named protected atom transports
only when the chosen gaps are declared transparent for that atom.

#### Proof

Theorem 2.1 makes every `e_g` legal and gives it the new selected lower
colour `g`.  The old matching edges remain legal on the persistent outer
sockets.  Each cut creates exactly two new sockets, both incident with its
one edge `e_g`, so (2.8) is a perfect matching.  The old lower colours and
the new gap colours are disjoint and each occurs once.

Replacing an old internal factor adjacency by the identical adjacency
labelled as a seam changes only the parentheses around the owner sequence.
Hence the expanded matching has the same physical adjacent-owner word and
the same contracted topology.  Every chronology-based certificate listed
in the theorem is therefore unchanged. \(\square\)

This lift is an existence monotonicity statement: it preserves a complete
old solution if one is already known.  It does not say that a new matching
which uses the extra socket edges needed to repair `I_0` or `U_0` is
orientation-, colour-, topology- or residence-compatible.

### 2.6 The exact separation after singleton support

Eliminating isolated sockets is only the singleton row of the socket perfect
matching problem.  Ignoring colours, a socket perfect matching exists
exactly under Tutte's inequalities

\[
        o\bigl(S(C)-X\bigr)\le |X|
                    \qquad(X\subseteq V(S(C))),          \tag{2.9}
\]

not merely when every socket is nonisolated.  Two disjoint triangles have
six nonisolated vertices and no perfect matching, giving the sharp abstract
counterexample.

Requiring every selected lower colour once is stronger still: a seam is a
three-resource atom `\{socket, socket, lower colour\}`, so the exact object is
a rainbow perfect matching (or a three-dimensional matching after a fixed
orientation sheet), not an ordinary Hall system or a matroid.  The retained
`k=17` zero/zero bank is a literal Boolean counterexample: it has no local
socket, common-orientation or rank-ten zero and every two-shore projection is
perfect, yet its four-seam bow tie makes the joint orientation--colour q1
formula UNSAT.

Even a rainbow socket perfect matching yields only a cycle cover.  One-cycle
topology needs subtour/graphic rows; exact residence needs the shared product
age automaton; and upper ranks eleven through seventeen need the ordered
suffix/full/prefix deck.  None of these properties follows from support
monotonicity or from (2.3).

### Theorem 2.7 (bounded iterative refinement requires rank improvement)

Let `A(C)` be the three-resource hypergraph whose seam atom `e` consumes its
two physical sockets and its selected lower colour.  Write `nu_3(C)` for its
matching number.  If `C` has `P` pieces, define the coloured-socket defect

\[
                         \delta_3(C)=P-\nu_3(C).          \tag{2.10}
\]

After `q` pure refinement cuts,

\[
                         \nu_3(C')\ge\nu_3(C)+q,
 \qquad                  \delta_3(C')\le\delta_3(C).    \tag{2.11}
\]

Suppose, moreover, that for every reachable refinement with
`delta_3>0` there is an allowed bundle of at most `q_0` further cuts which
strictly decreases `delta_3`.  Then at most

\[
                         q_0\,\delta_3(C)               \tag{2.12}
\]

additional cuts produce a lower-colour-exact socket perfect matching.

#### Proof

Take a maximum three-resource matching before a split.  The canonical edge
across the new cut uses the two new sockets and the new selected lower colour,
all disjoint from the old resource ground.  Adjoining it increases the
matching size by one.  Iterate to prove (2.11).  Under the additional
hypothesis, repeatedly choose a rank-improving bundle.  The nonnegative
integer `delta_3` decreases at least once per bundle and initially has value
`delta_3(C)`, proving (2.12). \(\square\)

The rank-improvement hypothesis is essential.  Abstractly, direct-sum a
fixed defect-one bow tie with a chain of `N` canonical refinement atoms, and
make the one alternative atom which breaks the bow tie available only after
the last refinement.  Every split has the canonical lift (2.11), every
singleton resource can remain nonisolated, and the defect stays one for
`N-1` cuts.  Thus support monotonicity alone cannot imply an
`O(delta_3)` cut bound.  In the Boolean host, proving a uniform `q_0` is an
endpoint-expansion/augmenting-refinement theorem, not a consequence of
Theorem 2.1.

## 3. Exact quantitative bounds for the authenticated bank

The augmented audit emits the rank-nine owner mask of every isolated dense
socket.  All 187 masks are distinct.  The separate rank-ten list contains
78 masks.

If the physical socket identities are frozen and repair is by adding
provider seams, a seam serving rank-ten target `U` can also repair an
isolated socket with owner `A` only if

\[
                         A\subset U.                     \tag{3.1}
\]

Give each `U` capacity two, since one seam has two endpoints, and each dead
socket capacity one.  The exact capacitated graph for the necessary
containment relaxation `A subset U` has

\[
 \begin{array}{c|r}
 \text{containment incidences}&27\\
 \text{dead sockets with no zero-upper containment}&161\\
 \text{zero uppers with no dead-socket facet}&53\\
 \text{zero uppers with fewer than two dead facets}&76\\
 \text{maximum capacitated matching rank}&26.
 \end{array}                                             \tag{3.2}
\]

### Theorem 3.1 (fixed-socket provider lower bound)

Any provider-only repair retaining the 187 current socket identities uses at
least 159 newly available undirected provider edges.

#### Proof

At least 78 provider edges are needed for the 78 distinct upper labels.  By
the capacity-two containment relaxation, those 78 edges can cover at most 26 of
the 187 dead sockets.  Every other provider edge covers at most two dead sockets.
Therefore at least

\[
       78+\left\lceil\frac{187-26}{2}\right\rceil
       =78+81=159                                        \tag{3.3}
\]

seams are necessary.  \(\square\)

This is a lower bound on newly available provider **edges**, not on extra
cuts.  One endpoint-singletonizing cut can activate many raw edges, so it
does not conflict with the cut-cover upper bound of Theorem 2.4.

This lower bound deliberately does not cover a recut that removes an old
socket identity.  It does show that the two defect banks are almost
disjoint: only 26 endpoint obligations can possibly be paid by the 78
upper-provider seams without relocating endpoints.

There is also a literal finite upper bound for the **unrestricted** relaxed
projection.  Forget protection and cut all remaining factor gaps.  This adds

\[
                         24310-7612=16698                \tag{3.4}
\]

cuts.  Every owner is then a singleton piece, so every endpoint coordinate
is `all`.  Select the original factor edge at each lower colour.  This gives
the original seven factor cycles, uses every rank-eight colour once, and
retains the factor's complete rank-ten palette.  Thus all 187 and all 78
rows vanish.  This is not exact global residence: it reconstructs the old
short runs through chains of all-one singleton pieces.  It is also not a
feasible point of the protected selector below: it cuts the authenticated
factor's 26 protected gaps.  Its role is only to prove finiteness after the
protected-face restriction is dropped.

## 4. An exact finite joint recut selector

The socket theorem gives a compact exact 0--1 formulation for selecting old
cut exchanges and/or further cuts at the relaxed q1/rank10 level.

Work separately on each fixed factor cycle.  For every factor gap `g`, use a
cut variable `c_g`, fixing protected/forbidden gaps to zero.  For every
ordered cyclic interval from gap `g` to gap `h`, use `z_{gh}` to mean that
these are consecutive selected cuts and the owners between them form one
active piece.  The diagonal `z_{gg}` denotes the whole-cycle path opened at
its sole selected cut and is allowed only when `g` is that cycle's unique
selected cut.  Impose

\[
 \sum_h z_{gh}=c_g,\qquad
 \sum_g z_{gh}=c_h,\qquad
z_{gh}+c_t\le1\quad(t\text{ strictly between }g,h).     \tag{4.1}
\]

Here every other gap is strictly between `g` and itself in the diagonal
case, equivalently

\[
 z_{gg}+c_t\le1\quad(t\ne g),\qquad \sum_g c_g\ge1
 \quad\text{on each factor cycle}.                       \tag{4.1b}
\]

For every maximal coordinate run of length `L<=d`, let `I` be all `L+1`
factor gaps incident with the run, including both boundary gaps.  Impose the
exact internal-residence hitting row

\[
                         \sum_{g\in I}c_g\ge1.           \tag{4.2}
\]

Enumerate the two socket occurrences of every possible piece `z_{gh}` and
compute their literal age vectors.  For every compatible **undirected**
socket pair belonging to distinct possible pieces, introduce a seam variable
`y_e`.  Lower-rainbow factorability gives every lower colour `l` a unique
factor gap `g(l)`.  Impose

\[
 y_e\le z_{gh},\qquad y_e\le z_{uv},\qquad y_e\le c_{g(l)}.  \tag{4.3}
\]

Every active socket is used exactly once:

\[
                  \sum_{e\ni s}y_e=z_{gh}               \tag{4.4}
\]

for each socket of piece `(g,h)`.  Every selected deleted lower colour is
used exactly once:

\[
                  \sum_{e:\ell(e)=l}y_e=c_{g(l)}.       \tag{4.5}
\]

Let `U_g` be the union of the two original factor owners across gap `g`.
The exact rank-ten support rows are

\[
 \sum_{g:U_g=U}(1-c_g)+\sum_{e:u(e)=U}y_e\ge1
 \qquad\left(U\in\binom{[17]}{10}\right).               \tag{4.6}
\]

Equations (4.4)--(4.5) are precisely the bow-tie matching (1.5), and (4.6)
is (1.6).  Equations (4.1)--(4.6) are therefore an exact finite selector for:

* a cut set hitting every old short internal run;
* the induced literal path pieces and their common physical sockets;
* one relaxed-resident seam at every socket;
* every selected lower colour exactly once; and
* complete immediate rank-ten support.

No separate orientation variables are necessary by Corollary 1.2.  One may
minimize either total cuts `sum c_g` or Hamming distance from the dense bank.
Fixing all 7,612 incumbent cuts to one gives the monotone pure-refinement
face of Theorem 2.1.  Allowing them to vary gives the exact cut-exchange
face.

#### Soundness and completeness

On each factor cycle, (4.1), including the stated diagonal convention,
selects exactly the cyclic intervals between consecutive cuts.  Equation
(4.2) is exactly the condition that every old run of length at most `d` is
hit at one of its `L+1` closed-collar gaps.  Equations (4.3)--(4.4) select a perfect matching of the
active physical sockets; Corollary 1.2 orients each alternating component.
Equation (4.5) is precisely the lower-colour bijection, and (4.6) partitions
rank-ten witnesses into surviving uncut factor edges and selected seams.
Hence every integral solution produces exactly the stated relaxed cover.
Conversely, reading the cuts, pieces and socket matching from any such cover
satisfies (4.1)--(4.6).

This selector still permits several alternating cycles.  Standard subtour
rows can require one component.  Replacing pairwise relaxed compatibility by
the full seventeen-coordinate product-state flow is necessary for exact
global residence.  Ranks 11--17 and the lower compiler remain additional
rows rather than consequences of (4.6).

## 5. Audited artifacts

```text
scratch/audit_k17_selected_extra_cut_literal_refinement_20260801.cpp
  emits first/last isolated flags and endpoint-owner masks without imposing
  the dense-bank XOR pattern on other inputs

scratch/k17_dense_refinement_socket_masks_20260801.audit.out
  SHA-256 125322bfbfdf7202b4e2bc00177f8cdc48519668dd6683a1e6b8b75c20bb5fa2

scratch/audit_k17_dense_socket_upper_overlap_bound_20260801.cpp

scratch/k17_dense_socket_upper_overlap_bound_20260801.audit.out
  SHA-256 81e70dfadaee6dc5356dffb3bc5c08c1a52a12f4e06e03bb30f2d513368c9113
```

The two C++ audits were compiled with C++20 `-O3` and run on H100 CPU under

```text
/home/amodo/or15/work/root_dense_socket_overlap_20260801
```

The overlap audit reports `PASS_K17_DENSE_SOCKET_UPPER_OVERLAP_BOUND`.

These artifacts authenticate the frozen `187/78` bank and the containment-
relaxation lower bound.  They do not instantiate or solve the joint selector
(4.1)--(4.6).
