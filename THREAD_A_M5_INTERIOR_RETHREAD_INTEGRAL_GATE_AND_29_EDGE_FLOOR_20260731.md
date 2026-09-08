# The `m=5` interior-rethread gate as an exact integral object

Date: 2026-07-31  
Status: exact rigidity theorem, exact palette/Hall/graphic reduction, exact
`29`-edge support floor, an independently verified residence-clean
rethread, and a literal counterexample to scalar long-run slack; the
all-depth connector/compiler problem remains open

## 0. Verdict

There are two inequivalent meanings of “preserve the fixed joint
decoration.”

* If it means preserving the accepted lower--upper diamond pairing
  pointwise, then the interior-rethread gate is empty: that pairing uniquely
  determines all `210` physical Johnson edges.  The `31` short runs cannot
  move at all.
* The weakest nontrivial interpretation is to preserve the lower and upper
  palettes (and declared occurrence ports) while allowing the lower--upper
  pairing to change along alternating circuits.  On this face the gate is an
  exact integer matching-plus-graphic-plus-window problem.

For item 2183's actual `42`-path carrier, every repair on the second face
must delete at least `29` old decorated edges.  Palette exactness forces the
same number of additions, so the old and new joint decorations have
symmetric difference at least `58`.  This is an exact interval-packing dual,
not a counting heuristic.

The residence layer is nevertheless feasible.  Item 2188 supplies an
independently replayed perfect diamond matching changing `119` partners;
its lift is again a `42`-path forest and has no internal run of length one
or two.  It leaves exactly `21` deeper flag targets plus endpoint joining
and compiler compatibility.  Thus the `29` bound is a support floor, not a
residence no-go.

Coordinatewise protected long-run slack cannot be the sole sufficient
hypothesis.  A protected Johnson slice gives a two-deadline obstruction even
when either coordinate separately has arbitrarily long legal continuation.
This is a local obstruction, not a global nonexistence theorem for Catalan
linear matchings.  Beyond the unconditional interval min--max (4.3), an
exact positive min--max for coupled repair atoms survives on a private
separable face, where it is ordinary capacitated Hall.

## 1. Rigidity of a pointwise fixed decoration

Let

\[
 \mathcal L=\binom{[10]}4,\qquad
 \mathcal X=\binom{[10]}5,\qquad
 \mathcal U=\binom{[10]}6,
\]

and let `B` be the rank-4/rank-6 containment graph.  If
`e=(L,U)` is a diamond, write `U-L={a,b}` and define

\[
                 \psi(e)=\{L+a,L+b\}\in E(J(10,5)). \tag{1.1}
\]

### Theorem 1.1 (fixed-pair rigidity)

The map `psi` is injective.  Consequently a fixed perfect diamond matching
`P` fixes its physical forest `F=psi(P)` pointwise.  No nonempty interior
edge exchange preserves `P`.

#### Proof

For a Johnson edge `{X,Y}`, its unique inverse diamond is

\[
                         L=X\cap Y,\qquad U=X\cup Y. \tag{1.2}
\]

Thus (1.1) is injective.  Applying it to every member of `P` proves the
claim.  \(\square\)

In particular, “fixed decoration” in a nontrivial rethread theorem must mean
fixed marked-occurrence/port data transported through transparent moves, or
fixed palette marginals.  It cannot mean the full paired matching `P`.

## 2. The exact palette-preserving exchange object

Fix item 2183's perfect matching `P` and forest `F=psi(P)`.  Let `P'` be a
second perfect matching of `B`, and put

\[
                    R=P\setminus P',\qquad
                    A=P'\setminus P.                 \tag{2.1}
\]

The set `R` consists of deleted diamonds and `A` of added diamonds.

### Theorem 2.1 (alternating-circuit/Hall/graphic normal form)

The following statements hold.

1. `P triangle P'` is a disjoint union of alternating even circuits in `B`.
2. For every middle owner `X`,
   \[
   d_{\psi(P')}(X)-d_F(X)
    =|\{e\in A:X\in\psi(e)\}|
     -|\{e\in R:X\in\psi(e)\}|.                    \tag{2.2}
   \]
3. If the exact deleted set `R` is prescribed, put
   \[
   B_R=B[L(R),U(R)]\setminus R,                     \tag{2.3}
   \]
   where `L(R)` and `U(R)` are the lower and upper endpoints of the deleted
   matching edges.  A palette completion with exactly those deletions exists
   if and only if
   \[
                   |N_{B_R}(S)|\ge |S|
             \quad(S\subseteq L(R)).                \tag{2.4}
   \]
4. Delete `psi(R)` from `F` and contract every resulting tree component.
   Then `psi(P')` is acyclic if and only if the multigraph induced by
   `psi(A)` on the contracted components is loopless and acyclic.  If also
   every middle degree is at most two, it is again a `42`-path forest.

#### Proof

The symmetric difference of two perfect matchings is a disjoint union of
alternating even circuits, proving 1.  Equation (2.2) is direct incidence
accounting.

After retaining `P-R`, precisely the shores `L(R)` and `U(R)` are unmatched.
An added set is therefore exactly a perfect matching of (2.3).  Hall's
theorem gives (2.4), proving 3.

The graph `F-psi(R)` is a forest.  Adding one of the new edges creates a
cycle exactly when it is a loop after contraction or when the contracted
new edges close a cycle.  Expanding contracted tree paths proves both
directions of 4.  Since `|A|=|R|`, the edge count remains `210`; an acyclic
graph on `252` vertices therefore has `42` components.  The degree bound
makes those components paths.  \(\square\)

Thus palette completion alone is a bipartite-flow problem once `R` is fixed.
Choosing an `R` that admits a Hall completion `A` and simultaneously meets
the degree, graphic, residence and flag constraints is the integral
correlation gate.

## 3. Exact window and residence rows

Suppose an old Hamilton opening is cut at `s` adjacencies and its retained
fragments are reoriented/reordered using `s` new adjacencies.  At depth `q`,
only windows crossing an old or new seam can change.  Hence on either the
union or intersection shore there are at most `qs` lost occurrences and
`qs` gained occurrences.

For a target `T`, let `h^+_(q,T)` and `h^-_(q,T)` be its old upper-union and
lower-intersection multiplicities and let `Delta` denote the signed change.
Exact all-depth preservation is

\[
 h^+_{q,T}+\Delta^+_{q,T}\ge1,\qquad
 h^-_{q,T}+\Delta^-_{q,T}\ge1                       \tag{3.1}
\]

for every target and depth.  Protecting one named witness per target is a
stronger sufficient face of (3.1), not an equivalent requirement.

Here a depth-`q` window means a `q`-edge window, and this `qs` accounting
excludes any separately declared endpoint halo.  For depth-two residence,
an internal positive run is illegal exactly when
the coordinate trace contains `010` or `0110`.  Every old run-two defect
`rho=(X_0,X_1,X_2,X_3)` in the `42`-path forest has trace `0110` and edge
span

\[
 S_\rho=\{X_0X_1,X_1X_2,X_2X_3\}.                  \tag{3.2}
\]

Retaining all three edges preserves that four-vertex subpath up to reversal,
so every repair must satisfy the covering row

\[
                   |\psi(R)\cap S_\rho|\ge1.         \tag{3.3}
\]

These rows only destroy old defects.  The final chronology must separately
forbid every newly selected `010` and `0110` window.

## 4. The exact `29`-edge floor at `m=5`

### Theorem 4.1 (interval packing equals interval covering)

For the item 2183 carrier, the `31` sets `S_rho` form length-three intervals
on the edge lines of eighteen path components.  Their transversal and
packing numbers are

\[
                              \tau=\nu=29.           \tag{4.1}
\]

Consequently every residence repair has

\[
                 |R|\ge29,\qquad |A|\ge29,
                 \qquad |P\mathbin\triangle P'|\ge58.  \tag{4.2}
\]

#### Proof

The incidence matrix of intervals against points on a line has the
consecutive-ones property and is totally unimodular.  Equivalently, greedy
right-endpoint stabbing and greedy interval packing have equal value on each
path.

In this fixture only two pairs of the `31` intervals overlap.  One pair has
start edges `9,11` on canonical path 1; the other has starts `1,2` on path
6.  All remaining intervals are pairwise edge-disjoint.  Choosing one member
from each overlapping pair and all other intervals gives `29` disjoint
spans.  Greedy right-endpoint stabbing gives `29` old edges meeting every
span.  Hence (4.1) holds.

Every repair must hit each span by (3.3), so `|R|=|psi(R)|>=29`.  Both `P` and `P'`
are perfect matchings of the same size, hence `|A|=|R|`; injectivity of
`psi` prevents deleting and physically re-adding the same edge under a
different diamond name.  This proves (4.2).  \(\square\)

There is also an exact protected-edge version.  If `Q subset E(F)` is an
undeletable set, let `E_0=E(F)-Q`.  Unless some `S_rho subset Q`, the common
integer optimum is

\[
 \begin{split}
 \tau_Q
 &=\min\left\{\sum_{e\in E_0}z_e:
       \sum_{e\in S_\rho\cap E_0}z_e\ge1\ (\rho),\ z_e\ge0\right\}\\
 &=\max\left\{\sum_\rho w_\rho:
       \sum_{\rho:e\in S_\rho}w_\rho\le1\ (e\in E_0),\ w_\rho\ge0\right\}.
                                                               \tag{4.3}
 \end{split}
\]

Both programs have integral optima.  Indeed, deleting the columns `Q` from
an interval matrix preserves the consecutive-ones property and total
unimodularity.  If some `S_rho subset Q`, the primal is infeasible and
`tau_Q=+infinity`.  Thus (4.3), not a scalar run surplus, is the exact
min--max theorem for the residence-only face.  It is the largest
unconditional flow face currently present in the actual carrier.

### Theorem 4.2 (the residence/palette/graphic face is feasible)

There is a perfect diamond matching `P_*` such that `psi(P_*)` is a
spanning `210`-edge, `42`-path forest with exact lower and upper palettes and
no positive coordinate run of length below three bounded strictly inside a
path.  Relative to `P`,

\[
 |P-P_*|=|P_*-P|=119,                               \tag{4.4}
\]

and the alternating-cycle half-length histogram is

\[
             2^9 3^7 4^5 5^2 6^2 7^3 8^1 9^1.     \tag{4.5}
\]

#### Proof

This is the independently replayed certificate of item 2188.  Its listed
bijection from rank-4 to rank-6 colours verifies the two palettes; lifting
the diamonds verifies maximum degree two, acyclicity and `42` components.
Literal path traversal gives internal run histogram

\[
                         3^{42}4^7 5^3 6^4 7^8 9^1,
\]

so every row (3.3) and every no-new-`010/0110` row is met.  The half-lengths
in (4.5), counted with multiplicity, sum to `119`, proving (4.4).  The
certificate and independent replay
are frozen in
`MATH_THEOREM_CATALAN_M5_RESIDENCE_CLEAN_INTERIOR_RETHREAD_20260731.md`.
\(\square\)

The internal fragments of `P_*` miss `21` deep targets: lower/upper misses
`6/10` at depth two, `2/2` at depth three and `0/1` at depth four.  Theorem
4.2 therefore settles the residence-only subsystem, not the all-depth gate.

## 5. An exact 0--1 extended formulation

### Theorem 5.1 (exact central-chronology formulation)

The central Hamilton chronology, palette, internal residence and all-depth
support gate can be written without ambiguity as a finite integral model.
Let `V=binom([10],5)` and let positions be `0,...,251`.  Use binary variables

* `p_(X,i)`: middle set `X` occupies position `i`;
* `a_(X,Y,i)`: the Johnson arc `X->Y` is used from positions `i` to `i+1`
  (`0<=i<=250`);
* `f_(X,Y,i)<=a_(X,Y,i)`: that adjacency is one of the `210` decorated
  diamond edges; and
* `w_(pi,i)`: the directed Johnson window `pi` occurs at position `i`.

The assignment and arc-flow rows are

\[
 \sum_Xp_{X,i}=1,\quad \sum_ip_{X,i}=1,              \tag{5.1}
\]

\[
 \sum_{Y:XY\in J}a_{X,Y,i}=p_{X,i},\qquad
 \sum_{X:XY\in J}a_{X,Y,i}=p_{Y,i+1}.               \tag{5.2}
\]

For every rank-4 colour `L` and rank-6 colour `U`, impose

\[
 \sum_{i,XY:X\cap Y=L}f_{X,Y,i}=1,qquad
 \sum_{i,XY:X\cup Y=U}f_{X,Y,i}=1.                  \tag{5.3}
\]

For every directed Johnson arc and `0<=i<=250`, also impose explicitly

\[
                         f_{X,Y,i}\le a_{X,Y,i}.     \tag{5.3a}
\]

The `f`-variables therefore select a perfect diamond matching.  Since they
are a subgraph of the Hamilton path described by `p,a`, their `210` edges
automatically form a spanning linear forest with `252-210=42` components
(isolated vertices counted as length-zero paths).

Occurrence-labelled marks require more than a support atlas.  For each
declared port `r`, let `A_r` be its exhaustive set of allowed labelled
occurrences `alpha=(X,Y,i)`.  Introduce binary `g_(r,alpha)` and impose

\[
 \sum_{\alpha\in A_r}g_{r,\alpha}=1,qquad
 g_{r,\alpha}\le f_\alpha,qquad
 \sum_r g_{r,\alpha}\le c_\alpha f_\alpha,          \tag{5.3b}
\]

where `c_alpha` is the declared occurrence capacity (usually one).  These
are the exact identity/link rows.  Merely setting `f=0` outside the union of
the atlases is only a support relaxation.  Setting the paired matching
itself pointwise instead reduces to Theorem 1.1 and admits no move.

For each relevant flag depth `1<=q<=5`, each Johnson window
`pi=(X_0,...,X_q)` and `0<=i<=251-q`, standard product linearization gives

\[
 w_{\pi,i}\le p_{X_j,i+j}\ (0\le j\le q),\qquad
 w_{\pi,i}\ge\sum_{j=0}^q p_{X_j,i+j}-q.            \tag{5.4}
\]

The upper/lower covering rows sum `w` over windows with the required union
or intersection and demand at least one.  For every coordinate, set `w=0`
on all length-three traces `010` and length-four traces `0110`.  These are
exactly the internal depth-two residence constraints.

Equations (5.1)--(5.4), the mark rows, the window covers and the two
forbidden trace families are an exact integral formulation of the **central
Hamilton chronology** gate.  A Hamming objective against the frozen
chronology minimizes changed adjacencies.  This is an exact equivalence of
integer points, not a claim that its LP relaxation is integral.

The full fixed-chronology compiler can also be appended exactly, without
treating source cells as extra middle owners.  Put

\[
              t_{i,x}:=\sum_{X:x\in X}p_{X,i}
              \quad(0\le i<252,\ x\in[10]),          \tag{5.5}
\]

and introduce source bits `s_(j,x)` for `0<=j<254`.  The source letter
`A_j={x:s_(j,x)=1}` is nonempty and lies in its clipped maximal envelope
exactly when

\[
 \sum_xs_{j,x}\ge1,\qquad
 s_{j,x}\le t_{i,x}
 \quad\bigl(\max(0,j-2)\le i\le\min(251,j)\bigr).    \tag{5.6}
\]

Impose, for every `i,x`,

\[
                       \sum_{j=i}^{i+2}s_{j,x}\ge t_{i,x}.       \tag{5.7}
\]

Containment (5.6) supplies the reverse coordinatewise inclusion, so
(5.6)--(5.7) are exactly `D^2A=T`, including both clipped endpoints.

Let `I_2` be all source intervals of length one or two.  For every nonempty
`S subset [10]` with `|S|<5`, introduce binary `z_(S,I)` and impose

\[
 \sum_{I\in I_2}z_{S,I}\ge1,\qquad
 \sum_{j\in I}s_{j,x}\ge z_{S,I}\ (x\in S),\qquad
 s_{j,x}\le1-z_{S,I}\ (j\in I,\ x\notin S).         \tag{5.8}
\]

Rows (5.8) say exactly that one length-at-most-two source interval has union
`S`.  Thus (5.5)--(5.8) are the unrestricted common compiler
`COMP_2(T)`, not independent rankwise Hall assignments.  Source cells are
differently typed; they do not enter the internal `010/0110` rows, and
boundary runs of `T` may legitimately have length one or two.  The simple
independent port-to-occurrence capacity identities are imposed by (5.3b);
more elaborate recursive socket correlations require their own exact
linking rows.

This is the specialization `d=2,r=5,W=252` of the audited fixed-chronology
equivalence in
`THREAD_A_ODD_K_TWO_BOUNDARY_SEAM_COMPILER_THEOREM_20260729.md`, Theorem
3.1.

No longer interval is needed for a rank-below-five target: every source
interval of length at least three contains a complete three-cell window
whose union is one rank-five member of `T`.  This also proves directly that
(5.8) loses no compiler witness.

On the item 2188 central connector face, forbid `f` on every edge outside
`psi(P_*)`; the palette rows then select all `210` edges of `psi(P_*)` at
their chronology-determined positions.  The remaining **central
chronology** variables choose only the component order, orientations of the
nonsingleton components and `41` consecutive exposed-port Johnson seams.
Indeed, contracting the `42` fixed path components inside any containing
Hamilton path leaves a connected acyclic maximum-degree-two graph with `41`
edges, hence a path; conversely, any such exposed-port joining expands to a
Hamilton path.  The product rows (5.4) together with the target-cover rows
record the `21` two-sided deep services, while (5.5)--(5.8) decide the exact
compiler.

## 6. Why there is no general matroid/flow min--max

Three independent obstructions remain even before all-depth covering.

1. A feasible deleted set must close into alternating matching circuits; its
   subsets need not be completable.  The diamond graph contains a
   `K_(2,2)`: take two rank-4 sets with a common rank-3 core and two distinct
   rank-6 supersets of their rank-5 union.  Its two-edge swap is feasible,
   whereas deleting either one matched edge alone has no exact palette
   completion.  Hence the natural deleted-set family is not hereditary.
2. The residence rows (3.3) are upward covering constraints, not matroid
   independence constraints.
3. For one lower colour with three extensions, the middle-incidence rows
   contain
   \[
   \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
   \qquad |\det|=2,                                  \tag{6.1}
   \]
   so the natural resource matrix is not totally unimodular.

Therefore the natural deleted-edge variables do not give an ordinary flow
or two-matroid-intersection formulation.  This does not rule out a larger
problem-specific integral extended formulation; it identifies the exact
correlations such a theorem must resolve.

There is one sharp positive flow face.  Let `D` be defects, `Rcal` private
repair ports of capacities `b_r`, and `G subset D x Rcal` the candidate
atoms.  Assume atoms on distinct available ports commute, each atom repairs
only its indexed defect, creates no new defect or flag loss, and all
conflicts are port capacities.  Then

\[
 \max |\text{repaired defects}|
 =\min_{S\subseteq D}
   \left(|D\setminus S|+\sum_{r\in N(S)}b_r\right),  \tag{6.2}
\]

and all defects are repairable if and only if

\[
                   |S|\le\sum_{r\in N(S)}b_r
                    \quad(S\subseteq D).             \tag{6.3}
\]

This is capacitated Hall/max-flow.  Coordinatewise slack checks only a small
subfamily of (6.3) and are not sufficient.

## 7. Literal failure of scalar long-run slack

The failure is already local in a protected Johnson slice.  Let the required
run length be `rho>=3`, fix a protected core `C` of size `r-2`, and restrict
legal states to

\[
                  \mathcal S_C=C+\binom{\Lambda}{2}. \tag{7.1}
\]

Choose distinct `x,y,z_0,...,z_(rho-2)` and freeze

\[
 P_0=C+\{z_0,z_1\},\qquad
 P_i=C+\{x,z_i\}\ (1\le i\le\rho-2),\qquad
 X=C+\{x,y\}.                                      \tag{7.2}
\]

These are consecutive Johnson states.  At `X`, the current `x`-run has
length `rho-1` and the `y`-run has length one.  Every distinct successor of
`X` in (7.1) is `C+{x,u}` or `C+{y,u}`.  It retains exactly one of `x,y`, so
one deficient run necessarily terminates below `rho`.

Nevertheless either coordinate separately has an arbitrarily long legal
continuation by keeping it and successively changing the other exterior
point.  Thus even unbounded per-coordinate long-run slack does not imply a
simultaneous repair.

More generally, in `C+binom(Lambda,s)`, a distinct successor of `C+Q`
retaining every active deadline in `A subseteq Q` exists if and only if

\[
                              |A|\le s-1,             \tag{7.3}
\]

assuming an unused entering point exists.  This is the missing mixed
deadline cut: a Johnson step must delete one member of `Q`, so the saturated
set `A=Q` cannot survive.  Singleton coordinate checks cannot see (7.3).

## 8. Exact remaining lemma

Theorem 4.2 closes the old run-span transversal problem at support `119`.
For the residence-clean forest `F_*`, the exact remaining **two-sided
all-depth** gate requested here is:

> Find an integer solution of (5.1)--(5.8) whose decorated support is
> `psi(P_*)`.  Equivalently, use every one of the `42` components once,
> orient every nonsingleton component, order them, and join each consecutive
> exposed-port pair by one of `41` Johnson seams, so that the central
> chronology has no internal `010/0110`, its crossing windows cover all
> `21` internal deep debts, and its same ordered target word `T` admits a
> nonempty source word satisfying the full common compiler `COMP_2(T)`.

No old internal flag witness is lost when whole components of `F_*` are
retained: reversal preserves unions/intersections, and seams only add
crossing windows.  Thus the `21` displayed debts are the complete deep-flag
service list for this fixed-forest face: `13` upper and `8` lower.  Central
residence and service are correlated through the same oriented endpoints,
while (5.5)--(5.8) impose the clipped endpoints and the literal common
source chronology.  Separate marginal matchings do not imply a common
chronology.  Additional recursive socket/port identities, if required, are
covered by (5.3b) only on its declared independent-capacity face; correlated
socket states require additional exact link rows.

For bare contiguous-OR equality, arbitrary-width upper completeness plus
`COMP_2(T)` is sufficient by the fixed-chronology compiler theorem.  On that
weaker face only `12` upper masks are absent internally: `10` of rank seven
and `2` of rank eight.  The thirteenth depth-aligned upper debt, mask `1007`,
already has the longer internal witness

\[
       460,397,271,79,590,844,868
\]

on canonical component `4`, whose union is `1007`; it is a flag-depth debt,
not an arbitrary-width upper hole.  The `8` lower-intersection debts are
likewise required here because the assignment explicitly asks to retain the
complete two-sided depth-aligned flag tower.  Thus `21` is not asserted to
be the globally minimal equality service list.

For general `m`, item 2187R proves that aggregate residence is ample: every
coordinate has exactly `Cat_m` runs before joining and a cyclic joining has
average run length exactly `m`, while the required floor is
`Theta(sqrt(m))`.  Section 7 proves that this scalar margin cannot by itself
yield a redistribution theorem.  A uniform result must control the mixed
deadline cuts exemplified by (7.3), together with alternating-palette,
graphic, flag and endpoint-state constraints.  The private-port Hall theorem
(6.2)--(6.3) is sufficient only when those correlations have already been
made separable.

## 9. Audit

The exact interval certificates are frozen in

```text
be209385f159228f5d7a56de1ae35fbd0e099919ad6e0cb0062fe1f6dd1dd1c7  scratch/audit_thread_a_m5_interior_rethread_span_floor_20260731.py
cf74af22042f16bf0dcddf4e48a13f05506afe2e59f639aeafb058d52d4fc96b  scratch/thread_a_m5_interior_rethread_span_floor_20260731.audit.json
```

The audit reconstructs all `31` occurrence-labelled `0110` spans from the
canonical `42` paths, verifies their coordinate ledger, and exports both a
`29`-edge transversal and `29` pairwise edge-disjoint spans.  Its canonical
payload SHA-256 is
`6c8461620a66a26c92c3694692b210436834033a7f0379efe19714a28ee30e23`.
The positive residence-clean witness imported in Theorem 4.2 is independently
frozen by item 2188; its audit JSON SHA-256 is
`92dd8af189e6160c7a1d19fff4481c29b57e0efda109db172d5dbdaf19a85d7d`
and its canonical payload SHA-256 is
`cdb66ea668f03597fb684a9ab4beeebb083f6d0339418ae35ae0846cad7cea14`.
