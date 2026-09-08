# Thread A: two-export controller circulation with position conflicts

Date: 2026-07-28

Status: exact algebraic closure theorem and one explicit positive `k=15`
crossed closure.  The positive circuit preserves the exact middle deck and
creates the advertised singleton `6308`, but it is not all-shore safe.
Here “target-safe” means this literal singleton/controller-envelope service;
preservation of the frozen physical-cell catalogue is not asserted.

## 0. Result

For a target-safe adjacent two-state controller block, the deck obstruction
is its signed two-arc boundary.  With separated auxiliary UNIT edits, exact
deck closure is equivalent to a unit-capacitated integral circulation.  With
changed-source capacity one, an inclusion-minimal completion is necessarily
one of two forms:

* **direct:** two paths `r_1 -> q_1` and `r_2 -> q_2`;
* **crossed:** two paths `r_1 -> q_2` and `r_2 -> q_1`.

Controller positions impose an additional interval conflict system which
ordinary reachability does not see.  Close operations can nevertheless be
used if each connected conflict cluster is promoted to one compound module
and its actual boundary is recomputed.

This promotion closes the first of the three `6308` rows.  There is an
explicit crossed 20-cycle which preserves the full middle deck, the
controller rank/path profile, maximal erosion, and coordinate incidences,
and has

\[
                         P'_{3152}=6308.
\]

It loses three upper and fourteen lower first-shore colours.  Thus it is an
exact controller/deck service circuit, not yet an all-shore Hall trade.

## 1. Boundary of a local controller module

Let

\[
 T_0,\ldots,T_{W-1}
\]

be an exact deck: its values are distinct and exhaust the middle layer.
Let a **certified module** `M` be a finite simultaneous controller edit for
which the controller ranks and adjacencies, all affected four-window
unions, all affected middle adjacencies, and maximal erosion have been
checked.  Suppose it changes precisely the middle positions `S_M` and

\[
                         T'_q=T_{\rho_M(q)}
                         \qquad(q\in S_M).
\]

Write `e_v` for the standard basis vector indexed by the old deck and put

\[
 \partial M=
 \sum_{q\in S_M}\bigl(e_{\rho_M(q)}-e_q\bigr).       \tag{1.1}
\]

Two modules are **collar-disjoint** when their complete controller,
four-window, middle-adjacency, and erosion dependency collars are disjoint.
For depth three, distance at least eight between every pair of edited
controller positions is a sufficient condition.

### Theorem 1.1 (module boundary criterion)

Let `M_1,...,M_t` be collar-disjoint certified modules.  Their simultaneous
application is a legal maximal controller chronology.  It enumerates the
same exact middle deck if and only if

\[
                         \sum_{j=1}^t\partial M_j=0. \tag{1.2}
\]

Any protected controller-envelope predicate whose complete dependency
collar avoids all modules is unchanged.

#### Proof

Collar-disjointness makes every local controller, union, adjacency, and
erosion equation belong to at most one module.  Hence the local
certificates superpose.  At an old deck value `T_v`, the change of its
multiplicity is exactly the `v`-coordinate of the sum in (1.2).  Since the
old multiplicity is one, every value again has multiplicity one precisely
when every coordinate of that sum is zero.  An avoided controller predicate
uses the same indexed controller states as before. \(\square\)

This theorem also gives the exact treatment of position conflicts.  A set
of close UNIT edits cannot be added by summing their advertised isolated
arcs.  Instead, take the connected components of the position-conflict
graph, recompute each component simultaneously, and use (1.1) for its
actual boundary.  Theorem 1.1 applies once the resulting compound modules
are collar-disjoint.

## 2. Two-export closure and the two pairings

Let a certified service block `B` export two distinct replacements

\[
                         q_1\longrightarrow r_1,
                         \qquad
                         q_2\longrightarrow r_2,      \tag{2.1}
\]

where the four endpoints are distinct.  An isolated ambient UNIT operation
`e` has a physical label

\[
                         (p_e,x_e,y_e;q_e,r_e)
\]

and deck arc `q_e -> r_e`.  The physical label must not be discarded:
parallel state arcs can have different controller positions and therefore
different conflicts.

### Theorem 2.1 (two-export separated-collar circulation)

Assume every selected auxiliary operation is collar-disjoint from `B` and
from every other selected operation.  The simultaneous edit preserves the
exact deck if and only if

\[
 \bigl(e_{r_1}-e_{q_1}\bigr)
 +\bigl(e_{r_2}-e_{q_2}\bigr)
 +\sum_e\bigl(e_{r_e}-e_{q_e}\bigr)=0.              \tag{2.2}
\]

Equivalently, the two service arcs and the selected auxiliary arcs form an
Eulerian directed graph.  If changed-source capacity is one and the
auxiliary set is inclusion-minimal, then for a unique pairing type
`sigma in S_2` the auxiliaries are two vertex-disjoint paths

\[
                         r_i\leadsto q_{\sigma(i)}
                         \qquad(i=1,2).              \tag{2.3}
\]

For `sigma=id` the completion is direct and the two service arcs lie in two
cycles.  For the transposition the completion is crossed and both service
arcs lie in one cycle.

#### Proof

Equation (2.2) is Theorem 1.1 written for one two-arc module and one-arc
modules.  It is also equality of indegree and outdegree at every deck
vertex.  Source capacity one makes every nontrivial Eulerian component a
directed cycle.  An auxiliary-only cycle can be deleted without affecting
the service block or (2.2), so minimality excludes it.  Removing the two
distinguished service arcs from the remaining cycle or cycles leaves
exactly the two paths (2.3).  If the distinguished arcs lie in different
cycles the pairing is direct; if they lie in one cycle it is crossed.  The
converse follows by adjoining the two service arcs to the stated paths.
\(\square\)

## 3. Exact position-conflict flow system

For the strict separated architecture, delete every auxiliary operation
whose controller position is within seven of a service-block position.
Binary variables `z_e` satisfy the unlabelled two-unit flow equations

\[
 \sum_{e:q_e=v}z_e-\sum_{e:r_e=v}z_e
 =1_{\{v=r_1\}}+1_{\{v=r_2\}}
  -1_{\{v=q_1\}}-1_{\{v=q_2\}}                    \tag{3.1}
\]

and the source/target capacities

\[
 \sum_{e:q_e=v}z_e\le1,
 \qquad
 \sum_{e:r_e=v}z_e\le1.                            \tag{3.2}
\]

The deliberately imposed distance-eight separation rule is exactly enforced
by

\[
 \sum_{e:\ a\le p_e\le a+7}z_e\le1
 \qquad\text{for every integer }a.                 \tag{3.3}
\]

Equations (3.1)--(3.3) are necessary and sufficient for a separated
auxiliary closure.  Any auxiliary cycles in a solution may be deleted; the
remaining flow decomposes as (2.3).  If one wants to prescribe direct or
crossed pairing, replace `z_e` by two commodity variables and give commodity
`i` source `r_i` and sink `q_{sigma(i)}` while retaining the common
capacities (3.2)--(3.3).

The earlier reachability test drops both (3.2) and (3.3).  It therefore
proves only that each endpoint can be routed separately, not that both can
be routed by one legal controller edit.

### Necessary cut conditions

Put `R={r_1,r_2}` and `Q={q_1,q_2}`.  Summing (3.1) over a deck-vertex set
`U` gives

\[
 z\bigl(\delta^+(U)\bigr)-z\bigl(\delta^-(U)\bigr)
 =|R\cap U|-|Q\cap U|.                              \tag{3.4}
\]

Let `kappa_B(F)` be the largest subset of an arc family `F` satisfying the
deck-vertex capacities and the eight-position inequalities, after deleting
all service-collar conflicts.  Every separated closure must satisfy

\[
 \boxed{
 \kappa_B\bigl(\delta^+(U)\bigr)
 \ge \max\{0,|R\cap U|-|Q\cap U|\}}
 \qquad(U\subseteq V).                              \tag{3.5}
\]

Two elementary specifically two-route no-go certificates are:

1. a deck vertex which is unavoidable for both paths of a fixed pairing; or
2. an eight-position window `I` such that every first path and every second
   path of that pairing uses an operation positioned in `I`.

The first contradicts (3.2), the second (3.3).  Proving one of these for
both pairings rules out that service block in the separated model.  These
cut conditions are necessary, not claimed sufficient in the presence of
arbitrary path-conflict side constraints.

## 4. The three `k=15` reachability rows

The audited two-state census is restricted to distinct flat-interior
positions `3<=p<q<=W-2` with `q-p<=7`, one-coordinate-for-one-coordinate
theoretical UNIT insertions, and at least one retained Hall-service pin.  It
omits boundary edits, non-UNIT insertions, same-position multiswaps, and
larger state replacements.  Within that scope it has

\[
 1{,}011{,}150\to30{,}442\to28{,}379\to27{,}838
\]

raw, controller-legal, rank-legal, and fully local-legal blocks.  No
rank-legal block is locally deck-closed.  Exactly 59 retain an advertised
target envelope.  Only the following three pass the uncapacitated ambient
reachability relaxation, and each creates the singleton target `6308`:

\[
\begin{array}{c|c|c}
\text{controller swaps}&\text{exported deck arcs}&
\text{strictly forbidden auxiliary positions}\\ \hline
(3151,+12-13),(3152,+11-13)&
3148\to685,\ 3149\to4452&[3144,3159]\\
(3266,+12-6),(3267,+11-6)&
3263\to3120,\ 3264\to3121&[3259,3274]\\
(3268,+2-6),(3269,+12-6)&
3268\to2236,\ 3269\to2237&[3261,3276].
\end{array}                                           \tag{4.1}
\]

The stored two-state reproducer checks maximal erosion at the two edited
positions.  A separate full affected-collar audit verifies that all 27,838
blocks satisfy the omitted erosion equalities.  This distinction matters
for the scope of the finite certificate.

## 5. An explicit feasible crossed closure for the first row

For the first row of (4.1), use the crossed return

\[
                         685\leadsto3149,
                         \qquad
                         4452\leadsto3148.            \tag{5.1}
\]

Besides the two service swaps, the auxiliary swaps are

\[
\begin{aligned}
&(688,+13-0),\
&(4452,+9-10),(4726,+8-2),(5103,+13-7),(5738,+7-8),\\
&(461,+6-3),(3156,+14-4),(2795,+3-5),(4096,+4-12),\\
&(901,+12-7),(6079,+0-13),(4713,+13-3),(3170,+5-6),\\
&(4359,+8-11),(1432,+7-14),(2095,+10-9),\\
&(3196,+2-8),(686,+3-12).
\end{aligned}                                         \tag{5.2}
\]

The close pairs `{3151,3152,3156}` and `{686,688}` violate the strict
distance-eight rule.  Treat each as one compound module.  Every two
positions belonging to different resulting modules are at distance at
least eight.  Direct local recomputation gives the actual module boundaries
listed by the following single deck cycle:

\[
\begin{aligned}
3148&\to685\to3149\to4452\to4726\to5100\to5738\to461\\
&\to3153\to2792\to4096\to901\to6079\to4710\to3170\\
&\to4359\to1429\to2095\to3196\to686\to3148.         \tag{5.3}
\end{aligned}
\]

### Theorem 5.1 (first exact target-safe interacting circulation)

The swaps (5.2), together with the service swaps

\[
                         (3151,+12-13),
                         \qquad(3152,+11-13),        \tag{5.4}
\]

produce a rank-correct Johnson controller `P'` whose four-window unions
form an exact Johnson ordering of the complete rank-eight deck and whose
maximal erosion is exactly `P'`.  Coordinatewise controller incidence is
unchanged, and

\[
                         P'_{3152}=6308
                         =\{2,5,7,11,12\}.           \tag{5.5}
\]

Thus `A'=P'` is a literal physical word with the advertised singleton
occurrence at cell 3152.  This is a feasible crossed algebraic closure; it
was certified by the displayed list, not by an existence search.

#### Proof

For each of the two compound modules and each remaining singleton module,
direct substitution verifies the controller ranks and adjacencies,
rank-eight four-window unions, middle Johnson adjacencies, and maximal
erosion.  Distinct modules are collar-disjoint.  Their actual boundaries
concatenate as (5.3), so their sum is zero.  Theorem 1.1 gives the exact
middle deck.  In (5.2)--(5.4), every coordinate is added as many times as
it is deleted, proving zero controller-incidence change.  Direct
substitution at 3152 gives (5.5), and `D^3P'=T'` by the four-window
definition.  The fact that `(6308,3152)` is an advertised Hall record is an
input from the audited atlas; the present certificate verifies its literal
realization. \(\square\)

The proof-safe checker is

```text
python3 scratch/audit_thread_a_k15_target6308_crossed_20cycle.py
```

It performs no search; it checks only the displayed certificate and the
claimed ledgers.  It proves equality with the loaded middle deck; the fact
that this loaded deck is the complete rank-eight layer is a separately
audited input.

## 6. Exact remaining obstruction

Deck closure is not shore closure.  The circuit of Theorem 5.1 loses the
upper first-shore colours

\[
                         9661,\ 23257,\ 31457         \tag{6.1}
\]

and the lower first-shore colours

\[
\begin{gathered}
3000,4796,5301,7352,10992,12476,13217,15144,\\
19160,23065,31280,31297,31304,31392.                 \tag{6.2}
\end{gathered}
\]

It gains no new first-shore colour on either side.  These are distinct-
support statements at `q=1`, not multiplicity, all-depth, or fixed-cell
ledgers.  Therefore Theorem 5.1 proves the requested middle-deck circulation
and one target-safe singleton service, but not the resident/all-upper
`k=15` trade.  The smallest demonstrated necessary next gate is a second
interacting circulation which restores (6.1)--(6.2) without creating new
losses and while retaining `6308`, the exact deck, fixed cells, and every
deeper required ledger; alternatively one needs a different closure with
those properties.
