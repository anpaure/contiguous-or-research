# A single boundary cut is the sharp residence escape for a folded-C8 host fan

Date: 2026-08-01  
Lane: A, folded-C8 owner host / terminal birail compiler  
Status: unconditional all-depth owner-link obstruction, exact cut criterion,
exact palette and common-`Q` completion tests, and a conditional folded-C8
boundary-rail theorem.  The existence of the required physical rail is not
proved.  In particular, host-address separation `d` alone is insufficient.

## 0. Result and exact boundary

Let `d>=2`.  Suppose `d+1` consecutive rank-`r` Johnson owners

\[
                         T_0,T_1,\ldots,T_d                         \tag{0.1}
\]

share a proposed source host `X` of size `r-d+1`.  Then

\[
 T_i=X\mathbin{\dot\cup}A_i,\qquad |A_i|=d-1,\qquad
 A_i=A_{i-1}-x_i+y_i.                                      \tag{0.2}
\]

Thus the affected owner fan is a length-`d` path in one
`(d-1)`-subset link.  Only `d-1` transitions can be fresh one-way swaps.
The `d`th transition necessarily removes a coordinate inserted earlier and
therefore creates an internal positive owner run of length at most `d-1`.
An entirely internal host fan cannot meet a residence floor `d`, hence
cannot meet the required floor `d+1`.

A global cut is the sharp possible escape.  If the first `d-1` transitions
are fresh and the sole recycled removal is the omitted boundary edge, all
retained rail transitions are monotone: every noncore coordinate trace is a
prefix or a suffix.  The sole short run is clipped at the global boundary.
More generally, one cut works if and only if its edge belongs to the
clipping set of every short run created by the rail.

This qualification is essential.  At `d=4`, the link path

\[
 abc\to xbc\to ubc\to uyc\to uvc                       \tag{0.3}
\]

has two separated internal singleton runs, `x` and `y`.  No one cut clips
both.  Hence the identity `p_R-p_L=d` does not by itself construct a
resident boundary rail.

There is a second, independent endpoint obstruction.  For a simple coatom
rail `T_i=X union (D\setminus{x_i})`, pinning the bare rank-`r-d+1` core
`X` at a source endpoint cannot reconstruct the first owner: the endpoint
cap must also contain `T_0\setminus T_1`; the reversed direction is needed
at the other endpoint.  Thus a positive folded rail must orient these two
directions inside `X_L,X_R` (or enlarge the endpoint caps).  Moving the bare
core to the cut is not sufficient.

For the aligned folded C8, the two host addresses do satisfy
`p_R-p_L=d`.  Their two incident owner-start intervals therefore meet in
one start, so they have exactly the geometry of the two ends of one possible
boundary rail.  Once such a rail is physically present, the canonical two
ray marginals have zero antitone Hall defect.  The exact remaining theorem
is the simultaneous existence of:

1. one cut clipping the short-run arcs of both host fans, with certified
   endpoint halos;
2. an injective strict owner chronology at that cut;
3. exact lower-palette recycling of the single cut colour `chi` and either
   an upper-safe host face or one explicit upper sidecar;
4. the mixed-row maximal-`Q` equalities in both phases; and
5. one protected, matching-closed background completion.

These five clauses are necessary and sufficient for the proposed
single-boundary-rail implementation.  None follows from address separation
or from the scalar antitone theorem alone.

## 1. The host-link residence theorem

Let `T_0,...,T_d` be distinct consecutive vertices of `J(Omega,r)` and let

\[
             X\subseteq\bigcap_{i=0}^dT_i,\qquad |X|=r-d+1.   \tag{1.1}
\]

Since each `T_i` has rank `r`, put `A_i=T_i\setminus X`.  Strict Johnson
adjacency gives the unique notation

\[
 A_i=A_{i-1}\setminus\{x_i\}\cup\{y_i\},
 \qquad x_i\in A_{i-1},\quad y_i\notin A_{i-1}.          \tag{1.2}
\]

Call transition `i` **fresh one-way** when

\[
                         x_i\notin\{y_1,\ldots,y_{i-1}\}. \tag{1.3}
\]

An internal positive run of a coordinate is a maximal string of consecutive
owners containing it which meets neither endpoint of the displayed linear
owner path.

### Theorem 1.1 (sharp link-length obstruction)

Among the `d` transitions (1.2), at most `d-1` are fresh one-way.  Therefore
some coordinate has an internal positive run of length between `1` and
`d-1`.  Consequently a fully internal fan (0.1) violates every positive-run
floor at least `d`.

#### Proof

As long as transitions are fresh one-way, each removed coordinate belongs
to `A_0`: no previously inserted coordinate is removed.  The removed
coordinates are distinct because a removed coordinate cannot return before
being counted among the `y` values.  Since `|A_0|=d-1`, at most `d-1`
transitions are fresh.

Choose a nonfresh transition `i`, so `x_i=y_j` for some `j<i`, and choose
the last such insertion `j`.  On

\[
                         A_{j-1},A_j,\ldots,A_{i-1},A_i
\]

the coordinate `x_i` has trace

\[
                              0,1^{\,i-j},0.             \tag{1.4}
\]

The run is internal and `1<=i-j<=d-1`.  This proves the claim. \(\square\)

The numerical bound is sharp.  With disjoint sets

\[
 O=\{o_1,\ldots,o_{d-1}\},\qquad
 N=\{n_1,\ldots,n_{d-1}\},                              \tag{1.5}
\]

the path

\[
 A_i=(O\setminus\{o_1,\ldots,o_i\})
       \cup\{n_1,\ldots,n_i\},\qquad0\le i\le d-1,    \tag{1.6}
\]

has `d-1` transitions and every coordinate trace is a prefix or suffix.

### Corollary 1.2 (one-return boundary escape)

Suppose (1.6) supplies the first `d-1` transitions of a cyclic fan and the
`d`th transition removes one of the `n_j`.  Cut the global owner cycle at
that `d`th edge.  Then every retained transition of this fan is one-way, so
the opened rail creates no internal positive run.  The removed coordinate's
short run is a clipped boundary run.

This is a residence theorem only under the usual clipped-boundary
convention, or when certified exterior halos extend every endpoint run to
the required length.  If endpoint runs are constrained exactly like
internal runs, cutting proves nothing.  Reclosing the omitted edge restores
Theorem 1.1's obstruction.

## 2. Exact multi-run cut criterion

Embed the link walk in a cyclic owner chronology.  For a maximal cyclic
positive run `R`, let `Clip(R)` be the set consisting of the two boundary
edges of `R` and all cyclic edges internal to `R`.  Cutting an edge in
`Clip(R)` makes `R` meet a linear endpoint (or splits it between both
endpoints).  Cutting any other edge leaves `R` internal.

Let `B_rho` be the family of positive runs of length less than the required
residence floor `rho` whose creation is charged to the proposed rail.

### Theorem 2.1 (one-cut min--max)

A single global cut removes every rail-created internal residence defect if
and only if

\[
                         \bigcap_{R\in B_\rho}Clip(R)\ne\varnothing. \tag{2.1}
\]

The legal cut edges are exactly this intersection.

#### Proof

After cutting at `e`, a cyclic run is internal precisely when it contains
neither endpoint of the opened word.  By definition this is equivalent to
`e notin Clip(R)`.  Intersect over the short runs. \(\square\)

The path (0.3), extended outside the displayed block without `x` or `y`,
has `Clip(x) cap Clip(y)=emptyset`; it is therefore a minimal warning that
one cut is not automatic.  The one-return normal form of Corollary 1.2 has
one charged short run and hence satisfies (2.1).

For two folded hosts `X_L,X_R`, put `B_rho=B_rho^L union B_rho^R`.  The
phrase **one boundary rail** means exactly that (2.1) holds for this union.
Two individually cuttable fans need not have a common legal cut.

### Theorem 2.2 (explicit one-return double-rainbow ear)

Let `d>=3`.  Take pairwise disjoint

\[
 A=\{a_1,\ldots,a_{d-1}\},\qquad
 B=\{b_1,\ldots,b_{d-1}\},\qquad \{c\},               \tag{2.2}
\]

all disjoint from `X`, and define

\[
\begin{aligned}
 S_0&=A,\\
 S_i&=(A\setminus\{a_1,\ldots,a_i\})
       \cup\{c,b_1,\ldots,b_{i-1}\},&&1\le i<d,\\
 S_d&=B.
\end{aligned}                                           \tag{2.3}
\]

Then `X union S_0,...,X union S_d` is a simple rank-`r` Johnson path.
Its `d` lower intersection colours and its `d` upper union colours are
separately pairwise distinct.  The only nonmonotone coordinate is `c`, with
positive trace `0,1^(d-1),0`.  Cutting any internal edge of that `c`-run
therefore gives an abstract owner rail with no internal residence defect.

#### Proof

For `1<=i<d`, step `i` removes `a_i`; step one adds `c`, and step `i>=2`
adds `b_(i-1)`.  The last step removes `c` and adds `b_(d-1)`.  Hence every
step is Johnson and all displayed sets are distinct.  The lower colours
have strictly decreasing `A` part and strictly increasing `B` part; the
upper colours have the analogous strict progression.  Thus neither shore
repeats.  The trace assertion is immediate, and Theorem 2.1 proves the cut
claim. \(\square\)

At `d=2`, both link-edge intersections equal `X`, so this particular
double-rainbow ear is impossible.  Theorem 2.2 is an abstract owner/palette
construction only: identifying its endpoints with the folded hosts and
passing the ambient common-`Q` rows remain the physical gate.

## 3. Exact owner and lower-palette ledger

For a strict Johnson rail put

\[
 \ell_i=T_{i-1}\cap T_i
     =X\mathbin{\dot\cup}(A_{i-1}\cap A_i),\qquad
 u_i=T_{i-1}\cup T_i
     =X\mathbin{\dot\cup}(A_{i-1}\cup A_i).             \tag{3.1}
\]

Thus each `ell_i` has rank `r-1` and each `u_i` has rank `r+1`.  The common
host and the link path do not by themselves make either palette distinct.

Consider replacement of an old cyclic rail `R` by a new cyclic rail `R'`,
with unchanged exterior owners, and let `e` be the common global cut.  Write
`Low(R-e)` and `Up(R-e)` for the occurrence multisets of intersection and
union colours on every changed retained edge, including the two rail/exterior
interfaces.

### Theorem 3.1 (simple-owner/immediate-palette criterion)

Assume the old and new rails have the same number of owner vertices.  The
replacement is a simple strict-owner, lower- and upper-palette-exact opened
carrier
if and only if all of the following hold.

1. Every new owner has rank `r`, every retained adjacency has symmetric
   difference two, no new owner repeats another new or exterior owner, and
   the new rail owner-occurrence set equals the removed rail owner-occurrence
   set whenever exact spanning ownership (rather than only a simple owner
   path) is required.
2. The cut is legal by (2.1), with endpoint halos satisfying the declared
   boundary residence convention.
3. The two exact signed palette equations hold:

\[
 Low(R'-e)=Low(R-e),\qquad Up(R'-e)=Up(R-e).             \tag{3.2}
\]

If declared protected sidecar occurrences are permitted, their colour
counters are added to the appropriate shores of (3.2).  If only support
surjectivity is required on one shore, replace its multiset equality by
equality of supports.

#### Proof

Clause 1 is exactly the definition of a simple strict Johnson owner path.
Clause 2 is Theorem 2.1.  The only lower and upper `q1` values on owner edge
`T_{i-1}T_i` are the two values in (3.1), so equality of the complete
retained occurrence counters is necessary and sufficient for exact palette
preservation. \(\square\)

In particular, if both cyclic phases are lower-rainbow and are opened on a
common edge of colour `chi`, their retained palettes have the same sole
hole `chi`.  One certified occurrence of `chi` is then necessary and
sufficient for lower-palette completion.  This statement applies to the
upper-safe folded cut.  On the aligned folded cut an upper value is also
lost; recycling `chi` alone does not repair that upper casualty.

The source-index separation has one exact geometric consequence on the
intended internal face.  If `[p_L-d,p_R]` lies inside the legal owner-start
range, a source position `p` lies in owner windows with starts `[p-d,p]`.
Hence positions `p_L` and `p_R=p_L+d` have incident start intervals

\[
                  [p_L-d,p_L],\qquad[p_L,p_L+d],        \tag{3.3}
\]

which meet only at `p_L`.  This is why the aligned folded hosts can be the
two ends of one rail rather than two unrelated internal sockets.  Equation
(3.3) says nothing about (2.1), owner injectivity, or (3.2).

## 4. Exact boundary maximal-`Q` theorem

Let the opened owner path be `T_0,...,T_(W-1)`.  Its source line has
positions `0,...,W+d-1`; owner `T_i` uses `[i,i+d]`.  Let `V` be the live
source positions of the boundary rail.  For every required owner, upper,
lower-pin, or protected-matching row `R`, record:

* its target `S_R`;
* its frozen exterior union `E_R`;
* its live position set `J_R subseteq V`; and
* a literal cap `P_v` at each `v in V`.

Assume every frozen exterior source letter is nonempty and is contained in
its rebuilt cap; equivalently, include every frozen cap/owner restriction
among the exact rows below.

Define

\[
 K_v=P_v\cap\bigcap_{R:\,v\in J_R}S_R.                 \tag{4.1}
\]

### Theorem 4.1 (necessary and sufficient common-`Q` test)

There are nonempty source letters `Q_v subseteq P_v` satisfying every row

\[
                   E_R\cup\bigcup_{v\in J_R}Q_v=S_R     \tag{4.2}
\]

if and only if

\[
 E_R\subseteq S_R,\qquad K_v\ne\varnothing,\qquad
 S_R=E_R\cup\bigcup_{v\in J_R}K_v                       \tag{4.3}
\]

for every row `R` and live position `v`.  When feasible, `Q_v=K_v` is the
unique componentwise maximal solution.

#### Proof

Any solution of (4.2) has `Q_v subseteq S_R` for every incident row, hence
`Q_v subseteq K_v`.  This proves necessity of nonemptiness and the
right-to-left containment in the reconstruction equality.  The other
containment follows from (4.1).  Conversely, (4.3) makes `Q_v=K_v` a
nonempty cap-legal solution of every row. \(\square\)

For owner rows alone, the unclipped maximal boundary envelopes are

\[
 \widehat Q_j=\bigcap_{i=0}^{j}T_i\quad(0\le j<d),
 \qquad
 \widehat Q_{W+j}=\bigcap_{i=W+j-d}^{W-1}T_i
                         \quad(0\le j<d).              \tag{4.4}
\]

Therefore a nonnative internal host may become cap-legal at a boundary:
only the clipped prefix or suffix owner family in (4.4) constrains it.  A
desired host `H` at one endpoint is legal exactly when `H` lies in the
corresponding intersection and all incident owners still satisfy the union
equalities (4.3).  Containment alone is not sufficient.

For two folded phases, one physical cap vector must pass (4.3) separately
for both complete row families.  Pointwise containment of `X_L,X_R` is not
a common-`Q` proof.  Moreover, target-to-cell injection is not part of
Theorem 4.1; after fixing the `2d-2` diagonal ray cells, the transported
background cells must still satisfy residual Hall in the same cap state.

### Corollary 4.2 (bare coatom-core endpoint obstruction)

Let `D={x_0,...,x_(d-1)}` be disjoint from `X` and consider the simple
coatom rail

\[
                   T_i=X\cup(D\setminus\{x_i\}),
                   \qquad0\le i<d.                    \tag{4.5}
\]

For boundary caps `H_L,H_R`, exact reconstruction of the first and last
owner rows requires

\[
 T_0\setminus T_1=\{x_1\}\subseteq H_L,
 \qquad
 T_{d-1}\setminus T_{d-2}=\{x_{d-2}\}\subseteq H_R.   \tag{4.6}
\]

Consequently the bare core choice `H_L=H_R=X` fails.  The minimal displayed
repairs are `X union {x_1}` and `X union {x_(d-2)}`, or an owner ordering in
which the required endpoint directions already lie in the proposed folded
host caps.

#### Proof

At the left boundary, all source positions other than the first contribute
at most `T_0 cap T_1` to `T_0`; therefore the first source cap must contain
`T_0 setminus T_1`.  The reversed argument gives the right condition.  This
is also the two endpoint instances of (4.3). \(\square\)

Thus moving a rank-`r-d+1` common core to the boundary removes the internal
link pigeonhole but does not automatically reconstruct the endpoint owners.
This endpoint-direction row is part of `SBR_d`'s maximal-`Q` clause.

## 5. Protected matching and cut transport

For a protected target `S`, let `W(S)` be its bank of admitted old interval
witnesses.  For a witness `I`, let `g(I)` be its internal gap set and put

\[
                           F_S=\bigcap_{I\in W(S)}g(I). \tag{5.1}
\]

A cut destroys every old witness of `S` exactly when it lies in `F_S`.
Thus a cut bank `C` contains a protected safe cut if and only if

\[
                         C\not\subseteq\bigcup_SF_S.    \tag{5.2}
\]

For a named occurrence rather than a target bank, `F_S` is simply that
occurrence's internal gap set.  If the nonempty `F_S cap C` are laminar,
(5.2) is equivalent to the maximal-member count

\[
                    \sum_{F\text{ maximal}}|F|<|C|.     \tag{5.3}
\]

When the remaining casualty-to-slot neighborhoods are intervals
`N(u)=[ell(u),r(u)]`, their exact Hall test is

\[
 \#\{u:N(u)\subseteq[i,j]\}\le j-i+1
                         \qquad\text{for every }[i,j].  \tag{5.4}
\]

Equations (5.1)--(5.4) are valid matching statements only for one
occurrence-labelled, matching-closed cap state.  Taking the union of options
from incompatible maximal words is unsound.

For literal protected-occurrence transport, let `Delta_addr` be the signed
old-to-new counter of addressed interval witnesses (start, end, width and
OR value), and let `Pi_e` retain exactly those cyclic occurrences which do
not cross the proposed cut `e`.

### Proposition 5.1 (addressed cut residue)

Every protected occurrence is preserved literally at the cut if and only if

\[
                              \Pi_e(\Delta_{addr})=0.    \tag{5.5}
\]

If only target service is required, rather than the same addresses, put the
positive part of `Pi_e(Delta_addr)` into the residual target bank and its
negative part into the released cell bank.  Exact repair is then equivalent
to Hall in that same matching-closed cap state; for convex neighborhoods it
is exactly (5.4).

#### Proof

Opening at `e` deletes precisely the wrapping cyclic occurrences and keeps
every nonwrapping occurrence with its address and value.  Hence (5.5) is
the literal signed difference after opening.  Allowing reassignment turns
its positive entries into demands and its negative entries into available
cells, so Hall is necessary and sufficient under the declared matching
closure. \(\square\)

In particular, a value/width `L1` counter without occurrence endpoints does
not decide (5.5).  The known folded graded residue therefore neither proves
nor refutes cancellation at the proposed global cut.

## 6. Folded-C8 specialization and the minimum remaining lemma

Suppress the fixed core `K` and write

\[
\begin{array}{ll}
 L_0=K+za_3f_1,&L_1=K+za_1f_1,\\
 R_0=K+za_1f_d,&R_1=K+za_3f_d,
\end{array}                                               \tag{6.1}
\]

with

\[
                         X_L=L_0\cup L_1,\qquad
                         X_R=R_0\cup R_1.                \tag{6.2}
\]

Conditional on literal occurrences of the boundary rail, the refinements

\[
 X_L\mapsto(X_L,L_\epsilon),\qquad
 X_R\mapsto(R_\epsilon,X_R)                              \tag{6.3}
\]

have one pointwise common cap, transport every contracted old interval by
full-block injection, and expose exactly `2d-2` distinct ray cells.  Those
cells form `U_(2d-2,2d-2)`.  The two threshold marginals are

\[
                      \{0^{d-1},1,\ldots,d-1\},          \tag{6.4}
\]

so `N=2d-2`, `E_L=E_R=d-1`, and the antitone birail deficiency is zero.

The only unproved physical statement is now the following.

> **Single boundary-rail lift `SBR_d`.**  There is an upper-safe folded
> selection (or an aligned selection with one certified upper sidecar) and
> one global cut such that the two host fans (6.2) satisfy the common-cut
> criterion (2.1), the owner/palette conditions of Theorem 3.1 with the cut
> colour `chi` recycled, the complete two-phase maximal-word equations
> (4.3), and the protected matching conditions (5.2)--(5.5), with endpoint
> halos extending every clipped run.

### Authenticated recut calibration

Passive rerooting of the currently saved folded cycles does not realize
`SBR_d`.  The remote-CPU exhaustive census over `2<=d<=12`, all common
cuts and both orientations retaining the exact two-ray support, has minimum
paired boundary radius

\[
                              4d+12.                    \tag{6.5}
\]

After requiring all sixteen upper `q1` values, the minimum is `4d+13`.
The all-sixteen-cycle and independent-phase-cut censuses retain the same
`4d+12` floor.  Thus the proposed mechanism requires a genuine owner/source
rethread; a better cut of the authenticated cycles is insufficient.  The
frozen remote artifacts are

```text
scratch/c8_folded_boundary_base_census_d2_d12.json
  SHA-256 ba5c2cc1ebe9e58a08bbc38b02379af82ee42ca49586e568d10b4c3e044eb230
scratch/c8_folded_allcycle_boundary_singletons_d2_d12.json
  SHA-256 54d2b8279d317dbf8a91bc6f5a714a76247486df11d97046c092f4cfa85bbfae
scratch/c8_folded_independent_boundary_singletons_d2_d12.json
  SHA-256 b9ac790469cca3a9c55fdc5c80cb4ed1caaf112567e2502c52236de4200c1a8d
```

No new local enumeration was run for this note.

### Theorem 6.1 (conditional boundary comparator)

If `SBR_d` holds, the selected folded-C8 comparator is a literal
owner-legal, resident, lower/upper-supported, matching-closed common-`Q`
move with zero terminal ray deficiency.  If its cut colour is recycled and
the boundary rail uses only the existing flat endpoint halo, it has zero
additional palette and source-length charge.

#### Proof

Theorem 2.1 gives residence, Theorem 3.1 gives owner and lower-palette
legality, Theorem 4.1 gives the one common source word in each phase, and
Section 5 gives protected matching transport and completion.  Equations
(6.3)--(6.4) then give the literal ray matching and zero birail deficiency.
The upper-safe alternative has no upper casualty; in the aligned
alternative the declared sidecar supplies it.  Recycling `chi` removes the
sole lower cut casualty.  No new source position is used beyond the
existing endpoint halo. \(\square\)

This theorem is deliberately conditional.  The present results prove the
local comparator and show why a boundary rail is the only sharp flat
residence escape.  They do not prove `SBR_d`, a serial recycled graded
relation, or `nu(k)=B(k)+O(1)`.

## 7. Independent adversarial audit

The main step was audited against five failure modes.

1. **Pigeonhole scope.**  The link size is exactly `d-1`; changing the host
   rank to `r-d` permits `d` monotone swaps and destroys Theorem 1.1.
2. **Multiple returns.**  The counterexample (0.3) proves that one cut does
   not repair an arbitrary link path.  The common intersection (2.1), not
   address separation, is the exact hypothesis.
3. **Endpoint convention.**  Clipping is useful only with exempt or
   certified endpoint runs.  This is explicit in `SBR_d`.
4. **Palette versus support.**  Ray Hall zero does not recreate `chi` and
   does not repair the aligned cut's upper casualty.  Both are separate
   clauses.
5. **Cap versus matching.**  The maximal-word test is coordinatewise and
   has no target-to-cell capacity.  The matching-closed residual Hall row is
   retained separately.

No computation is used in the proof.  The finite folded-C8 catalogues are
inputs only for the existence of the aligned quotient selections and their
two-ray formulas; this note makes no new finite-census claim.

The independent full closure statement is
`MATH_THEOREM_R_FOLDED_C8_SINGLE_CUT_BOUNDARY_RAIL_CLOSURE_AND_EXACT_GATES_20260801.md`;
its explicit one-return ear agrees with Theorem 2.2 and its
occurrence-addressed residue condition strengthens the protected-row clause
above.  The endpoint maximal-erosion audit is
`MATH_THEOREM_THREAD_D_BOUNDARY_COATOM_RAIL_COMMONQ_MAXIMAL_EROSION_20260801.md`;
Corollary 4.2 is its minimal endpoint-direction obstruction.  The passive
recut census is frozen in
`MATH_THEOREM_C8_INTERIOR_HOST_RESIDENCE_AND_BOUNDARY_RECUT_GATE_20260801.md`.
