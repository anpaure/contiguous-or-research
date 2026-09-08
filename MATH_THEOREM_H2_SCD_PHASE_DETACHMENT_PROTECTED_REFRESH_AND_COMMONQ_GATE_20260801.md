# SCD phase detachment with a protected rolling refresh: atom closure and the exact common-Q gate

Date: 2026-08-01  
Lane: H2, protected residence refresh / SCD phase-detachment interface  
Status: exact conditional integration theorem, linear protected-resource
bound, exact all-cut/common-Q formulation, and two sharp finite
obstructions.  No all-dimensional forced-extension or acyclicity theorem is
claimed.

## 0. Verdict

Fix the refreshed plus phase of the rolling split-core packet.  Its current
bank is the union of two paths with

\[
 |P|=2t=O(h)
\]

diamonds, pairwise distinct lower and upper colours, and physical degree at
most two.  The new SCD phase-detachment support can contain this bank with
only `O(h)` extra **typed forest resources**, but not merely by superposing
the path edges on a completed SCD forest.

The correct interface has three levels.

1. Every protected diamond must be a literal old SCD seed edge or one of
   the two edges of a legal detachment atom.  If the latter is forced, its
   partner edge is forced as well.  The resulting atom closure has at most
   `2|P|=4t` diamonds and at most `16t` owner-slot/lower/upper resource
   tokens.
2. The fixed SCD matching `M_0` forces the orientation of every physical
   diamond.  The protected physical paths must have one incoming and one
   outgoing rooted edge at each internal owner.  Physical degree two and
   palette injectivity do not imply this.
3. After a forced detachment solution is selected, its path forest and the
   protected literal halos must be realized by one source/cap state `Q`.
   All-width occurrence Hall, any clean expansion all-cut, the contracted
   graphic cuts, and maximal common-cap reconstruction must be evaluated in
   this same state.

The archived unforced SAT witnesses through `m=8` all happen to be forests,
but acyclicity is not automatic.  The exact `m=4` CNF has the satisfying
positive-variable set

\[
                         \{2,14,18,22,26,32\},       \tag{0.1}
\]

whose rooted support contains the directed cycle

\[
                  38\to35\to49\to56\to44\to38.      \tag{0.2}
\]

Thus the graphic row below is logically indispensable.  This cyclic
assignment has **not** been tested for a literal chronology or common cap;
it refutes only the claim that the encoded palette/degree/release rows force
acyclicity.

The unforced SAT witnesses also prove none of the protected extension or
literal common-Q rows.  In particular, SCD chain laminarity does not make the detachment
incidence interval-convex: the `m=4` target--provider quotient already
contains the three-row Tucker matrix

\[
 \begin{pmatrix}
  1&1&0\\
  0&1&1\\
  1&0&1
 \end{pmatrix}.
\]

Thus the positive theorem below is conditional.  Its hypotheses are also
the exact surviving construction target.

## 1. The fixed-`M_0` rooted interface

Let `M_0` be the four-row SCD matching from lower roots to rank-`m`
physical owners.  A physical Johnson edge `A--B` has

\[
             \ell=A\cap B,\qquad R=A\cup B.            \tag{1.1}
\]

It is rooted-compatible with `M_0` exactly when

\[
                         M_0(\ell)\in\{A,B\}.          \tag{1.2}
\]

In that case its orientation is forced: if `M_0(ell)=A`, then

\[
                 \ell\longrightarrow M_0^{-1}(B),     \tag{1.3}
\]

and conversely if `M_0(ell)=B`.  Since `M_0` is bijective, distinct rooted
tails are precisely distinct lower colours, while indegree and outdegree at
most one imply physical degree at most two.

### Proposition 1.1 (rooted compatibility is an independent row)

An upper/lower-injective physical path need not be a rooted path under
`M_0`.

At `m=4`, with `G=[5]`, `a=6`, and `z=7`, the two physical edges

\[
 z234\longrightarrow az23,
 \qquad az13\longrightarrow az23                         \tag{1.4}
\]

have distinct lower colours `z23,az3` and distinct upper colours
`az234,az123`.  Undirected, they are the valid two-edge path

\[
                         z234-az23-az13.                \tag{1.5}
\]

Both `M_0` orientations enter the middle owner, however, so its rooted
indegree is two.  Hence a protected bank accepted by the anonymous
owner-slot theorem is not automatically admissible in the fixed SCD phase.

For the rolling bank this gives the first exact test: every protected edge
must satisfy (1.2), and every internal protected owner must receive one
incoming and one outgoing forced orientation.

## 2. Detachment atoms and the smallest protected closure

Write `p` for an old SCD seed provider.  It has one rooted edge

\[
                         e_p=(t_p,h_p)                 \tag{2.1}
\]

and one old upper colour `c_p`.  A detachment option `omega` for a missing
upper target `r(omega)` replaces `e_p` by two rooted edges

\[
 e_{\omega,1}=(t_p,h_{\omega,1}),\qquad
 e_{\omega,2}=(\ell_{\omega,2},h_{\omega,2}).        \tag{2.2}
\]

The pair retains `c_p` and adds `r(omega)`.  It is one indivisible atom for
the palette ledger.

Let `x_omega` select options and put

\[
 y_p=1-\sum_{\omega:p(\omega)=p}x_\omega.            \tag{2.3}
\]

The final SCD support is

\[
 F(x)=\{e_p:y_p=1\}\ \dot\cup\!
       \bigcup_{\omega:x_\omega=1}
       \{e_{\omega,1},e_{\omega,2}\}.               \tag{2.4}
\]

The target, provider, and rooted-cap equations are

\[
\begin{aligned}
 \sum_{\omega:r(\omega)=R}x_\omega&=1
       &&(R\text{ in the missing }a/0\text{ shores}),\\
 y_p+\sum_{\omega:p(\omega)=p}x_\omega&=1,\\
 \deg^+_{F(x)}(v)&\le1,\\
 \deg^-_{F(x)}(v)&\le1.                              \tag{2.5}
\end{aligned}
\]

The last two rows include the release implication: a new incoming edge may
enter an old provider head only when that provider is switched away.

### Definition 2.1 (atom-closed lift)

An atom-closed lift of the protected bank `P` is a solution of (2.5) such
that

\[
                              P\subseteq F(x),        \tag{2.6}
\]

where equality is as literal physical owner edges with their fixed rooted
orientation.  If a protected edge is an old seed edge, (2.6) forces
`y_p=1`.  If it occurs only in a detachment option, (2.6) forces at least
one such `x_omega=1`, and therefore forces both edges in (2.2).

### Theorem 2.2 (linear atom-closure cost)

Suppose every protected edge is assigned to a distinct legal old edge or
detachment atom and the forced assignments satisfy (2.5).  Let
`widehat P` contain `P` and the partner edge of every forced atom.  Then

\[
 |\widehat P|\le2|P|=4t.                              \tag{2.7}
\]

Counting lower colour, upper colour, and two labelled owner slots per
diamond, its typed protected footprint has size at most

\[
                         4|\widehat P|\le16t=O(h).    \tag{2.8}
\]

If the residual phase-detachment system has a solution containing these
forced atoms and `F(x)` is acyclic, it is an exact upper-complete,
lower-injective physical path forest containing the refreshed bank.  No
separate upper-leave cover-down is needed at the central `q1` layer.

#### Proof

An option containing a protected edge adds at most its one partner edge.
This proves (2.7)--(2.8).  Equations (2.5) give lower/tail injectivity and
owner cap two.  Every unused seed provider contributes its old upper once,
and every used provider atom retains that same upper while adding its
unique target.  Hence the original exact SCD palette proof is unchanged.
If the resulting functional graph is acyclic, it is a path forest. \(\square\)

The hypotheses are load-bearing.  An edge absent from the old-edge/option
catalogue is a literal one-edge obstruction.  A present edge can still
force an incompatible partner, provider, head, or tail.  The existing
unforced SAT solutions do not prove that an arbitrary `O(h)` bank has an
atom-closed lift.

### Proposition 2.3 (acyclicity is not implied by the detachment CNF)

The original `m=4` phase-detachment CNF has 38 variables and 282 clauses.
Assignment (0.1), with every other variable false, satisfies every clause.
It selects exactly one option for each of the six missing targets, respects
provider, new-head, new-tail, and release constraints, and has maximum
rooted indegree and outdegree one.  Nevertheless its five-cycle is (0.2),
with physical owner cycle

\[
                  46-39-51-57-60-46.                 \tag{2.9}
\]

Therefore neither functional orientation nor the SCD option grammar gives
a hidden potential valid on every satisfying assignment.  A positive
potential may certify a restricted option face or one decoded witness, but
the general integration theorem must retain explicit graphic independence.
No source/common-cap conclusion follows from this cycle witness.

### Theorem 2.4 (exact potential replacement and a sufficient SCD guard)

For a fixed functional support `F(x)`, acyclicity is equivalent to the
existence of integer heights `pi_v` such that

\[
                    \pi_v\ge\pi_u+1
             \qquad(uv\in F(x)\text{ oriented }u\to v).  \tag{2.10}
\]

When `F(x)` is a forest, distance from the source of each directed path
gives such heights.  Conversely, summing (2.10) around a directed cycle is
impossible.  Thus (2.10) is an exact witness-dependent potential row and
can also serve as the local path-address coordinate in a literal component
chronology.

There is a useful stronger SCD sufficient condition.  Orient a physical
owner edge `A->B` as forced by `M_0`, and write

\[
                         A-B=\{r\},\qquad B-A=\{s\}.       \tag{2.11}
\]

Form the coordinate-precedence digraph `H_x` with arc `r->s` for every
selected physical edge.  If `H_x` is acyclic, choose topological coordinate
weights with `w_s>w_r` on every arc.  Then

\[
                         \Phi_w(A)=\sum_{i\in A}w_i          \tag{2.12}
\]

strictly increases along every rooted edge.  Since rooted outdegree is at
most one, a minimum-`Phi_w` vertex of an undirected cycle would have two
outgoing cycle edges, a contradiction.  Hence this guard implies a
physical forest.

This guard is sufficient, not necessary.  Exhaustively at `m=4`, only 64
of the 2,252 degree-feasible assignments have acyclic `H_x`, while all five
frozen forest witnesses `m=4,...,8` have a coordinate-precedence cycle.
The canonical Greene--Kleitman weights `w_i=i` leave no feasible `m=4`
completion at all.  The frozen witnesses instead have exact post-hoc path
heights `3,5,7,13,20`.  Thus no coordinate relabelling proves automatic
acyclicity for the observed solutions; either (2.10), the contracted
graphic cuts, or a deliberately restricted potential-positive catalogue
must remain.

## 3. Forest tokens versus literal source halos

The fixed source interface of the refreshed bank remains the one from
item2468H2:

\[
 J^-=[0,h+t],\qquad J^+=[3h-t,4h],                   \tag{3.1}
\]

together with `[X]`, active `K2` cells, selected singleton aliases, ordered
`h`-letter boundary overlaps, signed ages, and complete prefix/suffix OR
signatures.  Fixing every pivot ray fills the whole `4h+1`-letter packet.

The partner edges in `widehat P` need only be protected as typed forest
resources until the global chronology and source word are selected.  If
one insists on pinning their literal addresses in advance, a second cost
appears.  A depth-`h` path component with `e` edges occupies exactly
`h+e+1` source positions.  Thus `c` disjoint pinned components with `E`
total edges require

\[
                             E+c(h+1)                 \tag{3.2}
\]

positions before overlaps between their external collars are proved.
Consequently (2.8) is an `O(h)` **typed-token** theorem, while an `O(h)`
literal-address theorem additionally needs `c=O(1)`, nesting in the two
existing halos, or a common-Q chronology which shares the collars.  With
`c=Theta(h)`, naive address pinning costs `Theta(h^2)`.

This distinction is important: anonymous forest retention can protect
`widehat P`, but it cannot manufacture the all-width source interface.

### Theorem 3.1 (two-component literal refresh transport)

Assume the two oriented refreshed paths occur as contiguous subpaths of at
most two components of an acyclic `F(x)`.  Give those components
depth-`h` source blocks, fix the refreshed letters on (3.1), `[X]`, the
active `K2` cells and the selected singleton aliases, and apply the
component maximal-source/common-cap test to every remaining source
position.  If its maximal word reconstructs every owner, internal lower,
terminal and guard row, then:

1. the complete declared refreshed literal interface is retained in the
   SCD component sources;
2. every arbitrary-width interval lying wholly inside either fixed halo
   retains exactly its refreshed OR value;
3. the pivot singleton/source occurrences and signed residence runs remain
   literal; and
4. every interval crossing a fixed boundary is determined by the exported
   complete prefix/suffix OR signature.

The two fixed component collars use at most

\[
                         2t+2(h+1)+O(1)=O(h)          \tag{3.3}
\]

literal positions.  In particular, the `Theta(h^2)` internal interval
addresses require no separate protected tokens: they are consequences of
the retained source block.  Only crossing/exterior target assignment
remains in the occurrence Hall system of Section 4.

#### Proof

A contiguous component path with `e` edges has `e+h+1` source positions.
There are two refreshed paths and `2t` total edges, giving (3.3).  The
maximal-source equations make the fixed and free letters one common source
word.  Every wholly internal interval therefore has literally the same
ordered letters and OR as in the refreshed packet.  Boundary-crossing ORs
are exactly the exterior contribution union the appropriate fixed prefix
or suffix, so the complete signatures determine them.  Signed residence
is part of the same fixed trace.  \(\square\)

The contiguity and common-source hypotheses are load-bearing.  A protected
edge can be present abstractly while its component order cuts through a
halo, and an `O(h)` atom closure can fragment over `Theta(h)` components.
Neither case has the linear literal bound (3.3).

## 4. Exact all-cut/common-Q composition

Fix an atom-closed solution `x` whose support is a forest, and fix a path
chronology extending the refreshed paths.  Let `H` be the hard row family:

* every protected owner/lower/upper row;
* every declared arbitrary-width halo witness;
* the pivot singleton and source occurrences;
* terminal, seam, and mixed exterior guards; and
* every pinned detachment collateral.

There is an exact graph-level all-width prefilter before any source choice.
For a physical forest edge `e=AB`, put `lambda(e)=A union B`.  A rank-
`(m+q)` target `X` has a width-`q` owner witness exactly when some
consecutive `q` edges `e_1,...,e_q` of one forest component satisfy

\[
       \lambda(e_j)\subseteq X\quad(1\le j\le q),
       \qquad\bigcup_{j=1}^q\lambda(e_j)=X.          \tag{4.0}
\]

Thus upper exactness at `q1` does not settle any deeper row.  For `q=2`,
(4.0) is the exact contact condition that two incident edge labels are
facets of `X`.  Every occurrence admitted to the residual graph below must
first pass (4.0).

For one component owner path `O_0,...,O_s`, a depth-`h` source block has
positions `0,...,s+h`.  Before additional rows are imposed, its maximal
letters are

\[
 K_p^0=\bigcap_{\max(0,p-h)\le i\le\min(s,p)}O_i.    \tag{4.0a}
\]

The component is source-realizable exactly when every `K_p^0` is nonempty
and every owner reconstructs from the union of its `h+1` consecutive
maximal letters.  Its internal lower-q1 rows are then automatic; the
terminal unused lower root is a separate suffix equation.  In the
component containing the refreshed bank, the fixed letters on (3.1) and
their complete boundary signatures are intersected into (4.0a).  This is
the relative component version of the maximal common-cap equations below,
and it shows why an anonymous detached path forest is not yet a compiler.

Let `C_p` be the point cap and `D_p` the mandatory subset at free source
position `p`.  For a selected residual occurrence matching `M`, define

\[
 K_p(x,M)=C_p
  \cap\!\bigcap_{R\in H:p\in I_R} R
  \cap\!\bigcap_{(T,I)\in M:p\in I}T.               \tag{4.1}
\]

One maximal common source exists exactly when

\[
 D_p\subseteq K_p(x,M)\ne\varnothing                \tag{4.2}
\]

at every free position, the fixed positions pass the analogous tests, and
every hard or selected row reconstructs:

\[
                 B_R\cup\bigcup_{p\in I_R}K_p(x,M)=R.\tag{4.3}
\]

Equivalently, let `Q_H(P,x)` be the literal source states satisfying all
hard rows and the exact seam test.  For `Q` in this set, let `G_{x,Q}` be
the occurrence graph of all released and still-unassigned all-width
targets after deleting the protected and already selected cells.  Put

\[
 \boxed{
 \delta(P)=
   \min_{\substack{x:\ P\subseteq F(x),\ F(x)\text{ forest}\\
                   Q\in Q_H(P,x)}}
   \max_{Y}\bigl(|Y|-|N_{G_{x,Q}}(Y)|\bigr).}        \tag{4.4}
\]

The targetwise literal occurrence gate closes exactly when
`delta(P)<=0`.  The order of quantifiers in (4.4) is essential: taking the
union of occurrence edges legal under different `x` or different cap
states `Q` is invalid.

If a residual upper root is covered by a clean expansion tree rather than
one interval occurrence, filter its witness family through this same
`P,x,Q`.  For trees of at most `T` nodes the sufficient exact all-cut is

\[
 \nu\!\left(\bigcup_{R\in I}
       \{\Xi(\mathcal T):\mathcal T\in
          \mathscr T_R^{P,x,Q}(T)\}\right)
       >(10T-5)(|I|-1)                                \tag{4.5}
\]

for every nonempty root set `I`.  After the retained forest is contracted,
the projected on-edges must separately satisfy

\[
                         |E^+[X]|\le|X|-1             \tag{4.6}
\]

for every nonempty contracted-vertex set `X`.  In a successful exact SCD
detachment there is no central-`q1` leave, so (4.5) is needed only for any
separately retained cover-down/deeper-row mechanism.  Equations
(4.1)--(4.4) remain necessary for the literal all-width compiler.

### Theorem 4.1 (conditional integration)

Assume:

1. the refreshed bank has an atom-closed lift satisfying (2.5)--(2.8);
2. the forced residual SCD detachment has an acyclic solution;
3. one state `Q` satisfies (4.1)--(4.3) with the complete boundary
   signatures of item2468H2; and
4. the residual occurrence Hall cuts in (4.4), and whenever applicable
   (4.5)--(4.6), hold in that same state.

Then the SCD support is an exact upper/lower central path forest containing
the current refreshed residence bank, and every declared all-width/pivot
witness has a simultaneous literal occurrence.  The additional protected
typed footprint is `O(h)`.  Old and refreshed phases are alternatives;
the theorem retains only the refreshed plus phase.

## 5. SCD laminarity does not give interval convexity

The phase-detachment target--provider quotient is already non-convex at
`m=4`.  In `G=[5]`, take the three missing `a`-shore targets

\[
 a1234,\qquad a1235,\qquad a1245                    \tag{5.1}
\]

and the three central provider facets

\[
                         124,\qquad123,\qquad125.    \tag{5.2}
\]

The legal-incidence matrix, in the displayed column order, is

\[
\begin{array}{c|ccc}
       &124&123&125\\ \hline
 a1234&1&1&0\\
 a1235&0&1&1\\
 a1245&1&0&1
\end{array}.                                        \tag{5.3}
\]

For every ordering of the three provider columns, one row uses the two
outer columns and misses the middle.  Since the consecutive-ones property
is inherited by deleting columns, no ordering of the full provider shore
makes every target neighborhood an interval.  This is the smallest Tucker
obstruction to deriving item2468H2's interval Hall theorem directly from
SCD chain order.

Even if an independently chosen occurrence graph becomes convex, common
cap is separate.  The two-position core with caps `{z,a}`, `{z,b}`,
singleton rows `{a}`, `{b}`, and required background union `{z,a,b}` has a
perfect convex matching but loses the positive bit `z` in (4.3).

Therefore the nested Ferrers rail remains a valid **conditional** host for
the refreshed quadratic witness grid, but neither the SCD detachment SAT
support nor SCD laminarity supplies its common ordering or its common cap.

## 6. Exact surviving gate

The next positive theorem can be stated sharply:

> Embed the current two-path refresh as an `M_0`-oriented atom-closed
> subforest of the SCD detachment catalogue; prove that the forced residual
> system has an acyclic solution; and construct one chronology/source state
> whose released all-width occurrence graph satisfies (4.4).

Failure can occur first at any of four literal rows:

1. one protected edge has no `M_0`-compatible old/option occurrence;
2. its forced partner creates a provider/head/tail collision;
3. the forced option support creates a graphic cycle; or
4. every graph solution fails one common-Q reconstruction or target Hall
   cut.

The new unforced finite SAT results are strong evidence for the second and
third rows without a protected bank.  They do not yet settle this forced
integration theorem.

## 7. Independent finite audit

The dependency-free script

```text
scratch/audit_h2_scd_phase_detachment_refresh_interface_20260801.py
```

reconstructs the standard `m=4` four-row `M_0`, verifies the rooted
two-edge obstruction (1.4), reconstructs the exact Tucker matrix (5.3),
checks all six provider orders, and replays the typed atom-closure and
common-cap arithmetic.
