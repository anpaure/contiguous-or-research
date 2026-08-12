# Orbit-flow common-cap compilers and the product-LLL collision barrier

Date: 2026-07-31  
Lane: uniform compiler / Pascal--PBBS interface  
Status: unconditional abstract theorems plus an exact K16 audit; no all-`k`
guard bank is asserted

## 0. Verdict

There is a genuinely dimension-uniform way to discharge the fractional-Hall
part of the common-cap compiler whenever the carrier, schedule, pins, and
guarded candidate bank retain a group action:

> **Hall in an invariant guarded bank is exactly a capacitated flow on its
> target and cell orbits.**

In the especially relevant free cyclic case, the capacitated flow is just an
ordinary matching in the quotient target--cell graph.  This removes all
exponentially many physical Hall cuts at once; the remaining construction
problem is to produce the guarded bank and its quotient matching.

There is also a sharp negative conclusion.  The independent-target atomic
LLL from
`MATH_AUDIT_COMMON_CAP_CARTESIAN_AND_ATOMIC_LLL_EXISTENCE_20260731.md`
cannot be the primary coefficient-one tool if same-cell collisions are left
inside the bad-event family.  On a balanced regular candidate graph, its
uniform-profile inequality fails from collision events alone, even when a
perfect matching exists and there are no common-cap conflicts whatsoever.
Asymptotically, the same calculation needs more than `2e` cells per target,
whereas the optimal compiler has ratio `1+o(1)`.

Thus the correct order is:

1. obtain a matching, fractionally or integrally, by orbit flow / Hall; and
2. make that matching automatically safe by guards, or study cap conflicts
   under a matching measure rather than independent target choices.

The exact K16 instance confirms both points.  Its successful marginal graph
has average normalized load `0.817`, but the naive `1/deg(S)` weights place
load `9.975` on one cell and load `3.047` on a genuine interior cell.

## 1. Invariant guarded banks

Use the interval-compiler notation of the corrected master note.  Let
`L` be the lower targets, `C` the physical lower cells, and let

\[
                         H\subseteq L\times C
\tag{1.1}
\]

be a candidate bank carrying a complete guard system in the sense of
Theorem 4.1 of
`MATH_THEOREM_R_COMMON_CAP_GUARD_PRUNING_ROBUST_HALL_LIFT_20260731.md`.
Thus every matching in `H` is a valid literal common-cap compiler.

Let a finite group `Gamma` act on `L` and `C`, and suppose it preserves
`H`.  Write

\[
 L=\bigsqcup_{a\in A}L_a,
 \qquad
 C=\bigsqcup_{b\in B}C_b                         \tag{1.2}
\]

for the target and cell orbits.  Put

\[
 E_{ab}=H\cap(L_a\times C_b),                     \tag{1.3}
\]

and join orbit nodes `a,b` in the quotient support graph exactly when
`E_ab` is nonempty.

### Theorem 1.1 (orbit-transport guarded compiler)

The following are equivalent.

1. `H` has a fractional matching saturating every target and using every
   cell with capacity at most one.
2. There are numbers `f_ab>=0`, supported on the quotient edges, such that

   \[
   \sum_b f_{ab}=|L_a|\quad(a\in A),
   \qquad
   \sum_a f_{ab}\le |C_b|\quad(b\in B).             \tag{1.4}
   \]
3. Every set `I` of target-orbit nodes satisfies the weighted quotient Hall
   inequalities

   \[
   \sum_{a\in I}|L_a|
       \le
   \sum_{b\in N(I)}|C_b|.                            \tag{1.5}
   \]

Whenever these conditions hold, `H` contains an integral matching
saturating all lower targets, and hence a literal common-cap compiler.

Moreover, a quotient flow gives an explicit symmetric fractional matching:

\[
 x_e={f_{ab}\over |E_{ab}|}
 \qquad(e\in E_{ab}).                                \tag{1.6}
\]

#### Proof

The group is transitive on each `L_a` and each `C_b`.  Therefore every
vertex of `L_a` has the same degree into `C_b`, and every vertex of `C_b`
has the same degree from `L_a`.  Those two degrees are

\[
 {|E_{ab}|\over |L_a|},
 \qquad
 {|E_{ab}|\over |C_b|}.                              \tag{1.7}
\]

With (1.6), a fixed target in `L_a` receives total weight

\[
 \sum_b {|E_{ab}|\over|L_a|}
              {f_{ab}\over|E_{ab}|}
 ={|L_a|}^{-1}\sum_b f_{ab}=1.                       \tag{1.8}
\]

A fixed cell in `C_b` receives

\[
 \sum_a {|E_{ab}|\over|C_b|}
              {f_{ab}\over|E_{ab}|}
 ={|C_b|}^{-1}\sum_a f_{ab}\le1.                    \tag{1.9}
\]

So (2) implies (1).

Conversely, average any feasible fractional matching over `Gamma`.  Sum its
averaged edge weights over every block `E_ab`; call the result `f_ab`.
Summing the target equations over `L_a` gives the first equation in (1.4),
and summing cell capacities over `C_b` gives the second.  Thus (1) implies
(2).

The equivalence of (2) and (3) is the integral max-flow/min-cut theorem on
the network

\[
 s\longrightarrow a\longrightarrow b\longrightarrow t
\]

with source capacities `|L_a|`, infinite middle capacities on quotient
edges, and sink capacities `|C_b|`.  Finally, a fractional matching
saturating one side of a bipartite graph implies ordinary Hall; bipartite
matching integrality supplies an integral matching.  The complete guard
system makes every such matching a literal compiler.  QED.

### Corollary 1.2 (free cyclic quotient matching)

Suppose every target orbit and every cell orbit has the same size `g`.
Then (1.5) is ordinary Hall in the unweighted quotient support graph.
Consequently it is enough that this quotient graph have a matching
saturating its target-orbit nodes.

This is also constructive without invoking a global integrality theorem.
For a matched pair `(L_a,C_b)`, the invariant nonempty block `E_ab` is a
regular bipartite graph with equally many vertices on its two sides, so it
has a perfect matching.  The union of these blockwise perfect matchings is a
physical lower-perfect matching.

### Corollary 1.3 (typed biregular transport)

Suppose target and cell orbits have been grouped into types, and every
nonempty target-type/cell-type block is biregular with the same block
support for all orbits of those types.  Any transportation table moving the
total target-orbit mass of each type into the available cell-orbit capacity
of its allowed types gives the weights (1.6), hence a compiler.

In particular, if every target type can use every cell type and total cell
capacity is at least total target demand, proportional transport by cell
type satisfies (1.4).  This last conclusion requires genuine block
biregularity; rank counts or average candidate counts alone do not imply it.

## 2. A collision-free orbit-shift LLL

The orbit-flow theorem also supplies a valid probabilistic route when a
complete guard bank is too strong.  The essential change from independent
target choices is to randomize *within perfect matchings*, so cell collisions
are absent identically.

Assume `Gamma=C_g` acts freely on every target and cell orbit.  Fix a
matching `phi` from target-orbit nodes to distinct cell-orbit nodes in the
quotient candidate graph.  Choose basepoints and identify every paired orbit
with `C_g`.  Invariance says that the candidate block paired with target
orbit `a` is described by a nonempty difference set

\[
 D_a=\{\delta\in C_g:
       (a,i)\sim(\phi(a),i+\delta)\text{ for every }i\in C_g\}.
\tag{2.1}
\]

For one choice `Delta_a in D_a` per target orbit, put

\[
 M_\Delta=\{((a,i),(\phi(a),i+\Delta_a)):
             a\in A,\ i\in C_g\}.                    \tag{2.2}
\]

This is a physical lower-perfect matching for every `Delta`: within one
paired block, translation by `Delta_a` is a bijection, and different target
orbits use different cell orbits.

Let `B` be the exact minimal common-cap conflict clutter after unary
propagation.  A physical conflict is **shift-consistent** when all of its
edges coming from one paired orbit block have the same difference.  Such a
conflict induces the atomic event specifying those differences; an
inconsistent conflict has probability zero.  If one difference value by
itself creates a conflict through several translated edges, delete that
value from `D_a` before continuing.

### Theorem 2.1 (orbit-shift atomic compiler criterion)

Choose the remaining `Delta_a` independently and uniformly from `D_a`.
Suppose `|D_a|>=M` for every `a`, where `M>1`.  For a value `(a,delta)`, let
`Dtilde_j(a,delta)` count shift-consistent atomic conflict events on `j`
distinct orbit variables which prescribe some value of `Delta_a` different
from `delta`.

If some `1<c<M` satisfies

\[
 \prod_{j\ge2}
   \left(1-(c/M)^j\right)^{\widetilde D_j(a,\delta)}
 \ge {1\over c}                                      \tag{2.3}
\]

for every retained value, then some `M_Delta` is a literal common-cap
compiler.  It is enough to verify the additive inequality

\[
 \sum_{j\ge2}\widetilde D_j(a,\delta)
 { (c/M)^j\over1-(c/M)^j}
 \le\log c.                                          \tag{2.4}
\]

#### Proof

Equation (2.2) proves matching and cell capacity deterministically.  A
shift-consistent event on `j` orbit variables has probability at most
`M^(-j)`.  Give it LLL charge `(c/M)^j`.  In the standard lopsidependency
graph for atomic events on independent variables, an event is adjacent only
to another event which prescribes a different value of a shared variable.
Condition (2.3) is therefore precisely the product estimate in the proof of
the atomic lopsided criterion from the audit; (2.4) implies it via
`log(1-x)>=-x/(1-x)`.  The lopsided LLL gives a shift vector avoiding every
realizable member of the complete conflict clutter.  The exact
conflict-clutter theorem then makes `M_Delta` a common-cap compiler.  QED.

The theorem is dimension-uniform and has no collision term.  Its new,
checkable PBBS/Pascal quantities are:

1. the number of allowed differences in each paired orbit block; and
2. the alternative shift-conflict profile `Dtilde_j`.

Bounded physical conflict rank gives bounded `j`, but does not by itself
bound `Dtilde_j`; the latter remains the real probabilistic inequality.

### Corollary 2.2 (quarter-domain branching test)

Suppose the hypotheses of Theorem 2.1 hold and, for some `D>=1`,

\[
              \widetilde D_j(a,\delta)\le D^{j-1}
              \qquad(j\ge2)                           \tag{2.5}
\]

for every retained value.  If

\[
                         M\ge4D,                       \tag{2.6}
\]

then a common-cap compiler exists.

#### Proof

Take `c=2`.  Since `M>=4`, every denominator in (2.4) is at least `3/4`.
With `x=2D/M<=1/2`, the left side of (2.4) is at most

\[
 {4\over3}\sum_{j\ge2}D^{j-1}(2/M)^j
 ={4\over3}{2\over M}{x\over1-x}
 \le {32D\over3M^2}
 \le {2\over3D}
 \le {2\over3}<\log2.                                \tag{2.7}
\]

Apply Theorem 2.1.  QED.

Condition (2.5) has a direct enumeration interpretation: after fixing one
alternative shift value, every new orbit variable in a minimal conflict can
be exposed with at most `D` continuations.  Thus a concrete uniform target
for a Pascal/PBBS quotient is

\[
 \boxed{\text{allowed shift domain at least four times the quotient
 conflict branching.}}                               \tag{2.8}
\]

This is stronger than necessary, but it has absolute constants and charges
no physical matching collisions.

## 3. Pascal/PBBS interface

Theorem 1.1 applies verbatim to a cyclically equivariant Pascal or PBBS
carrier provided all of the following objects are equivariant under the
same action:

1. the middle chronology and physical schedule;
2. every positional cap and reserved pin;
3. the retained candidate bank; and
4. its complete guard system.

One then checks only the weighted quotient cuts (1.5).  This statement is
uniform in the dimension and allows nonfree actions: stabilizers merely
change the orbit capacities `|L_a|,|C_b|`.

For `Gamma=C_p` with `p` prime, every nonempty proper coordinate subset has
a free translation orbit.  Indeed invariance under one nonidentity
translation forces invariance under all of `C_p`, hence the subset is empty
or full.  Therefore, if the physical cells are also free and the guarded
bank is equivariant, Corollary 1.2 reduces the lower compiler to an ordinary
matching of necklace-orbit nodes.

This is a sufficient route, not a claim that the canonical PBBS chronology
already supplies the hypotheses.  In particular, opening components,
rerooting, a singleton pin, and a tail-start P/Q schedule generally break
the cyclic action.  Those defects must either be absorbed before applying
the theorem or contracted as an explicit boundary problem.  Scalar Pascal
identities do not manufacture an invariant guard bank.

The gain is exact localization of the missing theorem:

> construct an equivariant guarded incidence bank and prove weighted Hall
> on its orbit graph.

No physical subset Hall inequalities and no random collision analysis then
remain.

The invariant-witness lemma in
`MATH_SYMMETRIC_HALL_UNCROSSING_20260727.md` already proves, for free
actions, that a physical Hall failure has an orbit-union witness.  Theorem
1.1 is its capacitated nonfree form, gives the explicit fractional weights
(1.6), and places the conclusion behind the exact common-cap guard
interface.  The genuinely new probabilistic addition here is Theorem 2.1:
it randomizes cyclic shifts of blockwise perfect matchings and therefore
removes collisions before applying the conflict-clutter LLL.

The stored K11 bulk compiler is a positive calibration of the deterministic
quotient statement.  In its first-derivative normal form the strict-low
targets form six translation orbits; the 63 nonempty quotient cuts have
minimum margin two.  This proves its cyclic bulk Hall gate.  As already
recorded in the exact compiler theorem, the linear cut is separate: some K7
cuts fail even though the cyclic bulk is symmetric.  Orbit flow therefore
removes the bulk Hall quantifier but does not erase the boundary-flag gate.

## 4. Why independent-choice LLL is the wrong first step

The atomic LLL theorem in the cited audit is correct.  Its uniform-list
corollary, however, includes same-cell collision events because target
variables are sampled independently.  At coefficient-one density those
events alone consume more than the entire LLL budget.

### Theorem 4.1 (balanced regular collision barrier)

Let `G` be an `M`-regular bipartite graph with equally many target and cell
vertices, where `M>=2`.  Independently let every target choose one of its
`M` neighboring cells uniformly.  Include the atomic bad event that two
targets choose the same cell.

For every candidate `e` the size-two alternative-event count in Corollary
4.2 of the audit satisfies

\[
 \text{collision subcount in }\widetilde D_2(e)=(M-1)^2. \tag{4.1}
\]

Consequently, for every `1<c<M`, the collision term alone in (4.4) is

\[
 { (M-1)^2(c/M)^2\over1-(c/M)^2}
 = { (M-1)^2c^2\over M^2-c^2}
 \ge c^2-1
 >\log c.                                             \tag{4.2}
\]

Thus the uniform-profile atomic-LLL criterion cannot certify this instance,
even if every edge is guarded and there are no cap-conflict events at all.

#### Proof

Fix `e=(S,C_0)`.  For each of the `M-1` alternative cells `C` adjacent to
`S`, regularity gives `M-1` other targets adjacent to `C`.  Pairing the
alternative assignment `S->C` with any one of those assignments gives a
distinct collision event in the alternative-event family of `e`, proving
(4.1).

For the first inequality in (3.2), cross-multiplication gives the identity

\[
 c^2(M-1)^2-(c^2-1)(M^2-c^2)=(M-c^2)^2\ge0.           \tag{4.3}
\]

Finally `c^2-1>log c` for `c>1`, since both sides agree at one and the
derivative of their difference is `2c-1/c>0`.  QED.

The complete bipartite graph `K_(N,N)` is already a sharp conceptual
counterexample: perfect matchings abound and a complete guard bank makes
the compiler trivial, but the product-choice uniform LLL fails by (3.2).
This is not a counterexample to the asymmetric atomic LLL theorem; a Dirac
distribution supported on a known matching trivially works.  It is a
counterexample to using independent uniform target choices to *find* the
matching at near-unit capacity.

### Corollary 4.2 (the asymptotic `2e` capacity tax)

More generally, let the graph be left-`M`, right-`R` biregular, with both
degrees tending to infinity and cell/target ratio

\[
                         \alpha={M\over R}.             \tag{4.4}
\]

The collision contribution to (4.4) tends to `c^2/alpha`.  Hence a
necessary asymptotic condition for that uniform-profile criterion is

\[
                         \alpha\ge {c^2\over\log c}.
\tag{4.5}
\]

Since

\[
                  \inf_{c>1}{c^2\over\log c}=2e
\quad\text{at }c=\sqrt e,                             \tag{4.6}
\]

this product-LLL route needs at least `(2e-o(1))` cells per target before
any genuine cap conflicts are charged.  The optimal contiguous-OR compiler
has ratio `1+o(1)`, so the mismatch is structural.

## 5. Exact K16 normalized-load audit

The script

```text
scratch/audit_k16_commoncap_normalized_load_20260731.py
```

reconstructs the authenticated c7be K16 schedule, pin, complete marginal
candidate graph, and exact Dulmage--Mendelsohn matching support.  It then
places weight `1/deg(S)` on every incidence, exactly as in normalized-load
Corollary 3.2 of the audit.  It does not read or use the final compiler
matching.

The results are:

| graph | targets | cells | average load | max load | cells with load `>1` |
|---|---:|---:|---:|---:|---:|
| raw marginal | 26,331 | 32,229 | 0.816997 | 7.372088 | 12,577 |
| DM-supported | 26,331 | 32,229 | 0.816997 | 9.975065 | 3,423 |

For the DM-supported graph, the length-type averages are

| cell length | count | average | maximum | count `>1` |
|---|---:|---:|---:|---:|
| 1 | 12,872 | 0.497906 | 9.975065 | 635 |
| 2 | 12,872 | 1.044269 | 6.360794 | 2,780 |
| 3 | 6,485 | 0.999250 | 3.270692 | 8 |

The failure is not confined to the two word boundaries or the singleton
pin.  After deleting a radius-ten neighborhood of all three, the maximum is

\[
                         {4387\over1440}=3.046527\ldots
\tag{5.1}
\]

at the interior length-two cell starting at position `247`.

Thus the successful K16 graph does **not** satisfy the naive normalized-load
test, and exact matching-support pruning can increase its maximum load.
What exists, of course, is a highly nonuniform fractional matching (for
example the incidence vector of the authenticated integral matching).
Any uniform proof must construct that reweighting from symmetry, transport,
or another explicit design; it cannot infer it from degrees alone.

## 6. Consequences for the general program

1. **Use orbit flow for equivariant spirals and PBBS quotients.**  The exact
   target is a guarded quotient matching, with stabilizer-weighted capacities
   in composite dimensions.
2. **Do not put cell collisions into an independent-choice LLL at
   coefficient one.**  Theorem 4.1 shows this loses before any common-cap
   event is considered.
3. **If randomness is retained, sample matchings rather than independent
   target choices.**  The orbit-shift model of Theorem 2.1 is one completely
   elementary such measure.  More general matching measures would need a
   valid negative-dependency or cylinder-probability theorem.
4. **Boundary reroots and pins are the exact symmetry-breaking residue.**
   A Pascal/PBBS induction should keep the bulk bank equivariant, contract a
   bounded boundary assignment, and recheck quotient flow.  No robustness
   assertion of this strength is proved here.

The unresolved all-dimensional statement is therefore narrower than the
previous normalized-load/LLL alternatives: construct an equivariant complete
guard bank whose weighted quotient graph satisfies (1.5), plus a controlled
boundary contraction for the linear word.
