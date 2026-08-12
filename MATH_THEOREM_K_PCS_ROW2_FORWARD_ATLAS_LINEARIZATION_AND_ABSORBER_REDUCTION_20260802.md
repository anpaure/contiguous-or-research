# `PCS` Row 2: forward full-colour atlas, exact linearization, and a private absorber

**Date:** 2026-08-02  
**Lane:** K, protected Catalan--pivot / `PCS(m,d)` Row 2  
**Status:** exact all-parameter reduction and unconditional protected
occurrence supply; quantitative prospective absorber for `O(d)` defects;
no all-`m` integral linearization, residence, deeper-shadow, compiler, or
regeneration theorem

## 0. Result

Put

\[
 \Omega=[2m-1],\qquad
 \mathcal L={\Omega\choose m-1},\quad
 \mathcal V={\Omega\choose m},\quad
 \mathcal U={\Omega\choose m+1},
\]

and

\[
 W=|\mathcal L|=|\mathcal V|,\qquad
 U=|\mathcal U|,\qquad C=W-U=\operatorname {Cat}_m.       \tag{0.1}
\]

Fix the literal `3d`-turn pivot successor path and its correlated predecessor
matching phase.  The immediate-upper occurrence problem has an unconditional
solution **before** port capacities are imposed:

> for every perfect extension `M_0` of the pivot predecessor phase, there is
> a directed acyclic candidate atlas which contains the complete pivot
> successor path and at least one rooted incidence of every colour in the
> full rank-`m+1` shore.

Thus the boundary/`D` colours have no separate local occurrence obstruction.
The exact remaining Row-2 selector is only

\[
 \boxed{\text{one near-perfect tail--head matching in that atlas which
 covers every upper colour and contains the pivot.}}                 \tag{0.2}
\]

The acyclic atlas makes graphic independence and subtour cuts automatic.
After (0.2), the selected arcs form one rooted Hamilton path; expanding
`M_0` gives the lower-rainbow Johnson owner path and the corrected endpoint
aperture.  Contracted graphic--Rado is downstream and collapses to literal
nonemptiness of the colour families on that path.

Two complementary sufficient routes are also exact.

1. A protected upper-covering two-factor plus a full-task-transparent strict
   pull incidence tree Hamiltonizes without losing a colour.  Catalan
   redundancy then supplies a safe nonpivot opening.
2. For a controlled `p`-defect prospective factor, every missing full-shore
   target has a fixed-slot gain-one hex catalogue of size
   `2(m-1)(m-2)`.  These packets can be made pairwise private whenever
   `|B|+12(p-1)<m-2`.

The second result closes packet supply for `p+|B|=O(d)` when
`d=O(sqrt(m))`; it does not plant the required off phases or bind the new
target provider to the common `M_0`.

The independently replayed K17 factor with all `19,448/19,448` immediate
upper colours is positive finite evidence that the full-shore row can close.
A strict protected sequence keeps both opened palettes complete while its
opened short-run debt falls from `5,588` to `2,169`.  The terminal state is
an augmented `h=1` lollipop, not the ordinary rooted path in (0.2), and
remains nonresident with deeper holes.

## 1. Pivot-compatible rooted arcs

For a perfect containment matching

\[
                         M_0:\mathcal L\longrightarrow\mathcal V,
                         \qquad L\subset M_0(L),               \tag{1.1}
\]

identify a rooted vertex `L` with its owner `T=M_0(L)`.  Write

\[
                  \rho(T)=T-M_0^{-1}(T).                       \tag{1.2}
\]

The rooted-link arcs are exactly

\[
       T\longrightarrow T^x=T-\{\rho(T)\}+\{x\},
       \qquad x\in\Omega-T,                                  \tag{1.3}
\]

and the immediate-upper colour of this arc is

\[
                              c(T,x)=T\cup\{x\}.               \tag{1.4}
\]

For `m>=3d+1`, the pivot predecessor shore has `3d<=m-1` incidences and
extends to a perfect `M_0`.  Relative to every such extension, the pivot
successor shore is one simple directed path `P_1`, with distinct upper
colours.

### Lemma 1.1 (complete colour fibres)

For `R in \mathcal U`, let `T_z=R-{z}` for `z in R`.  The arcs of colour
`R` are exactly

\[
              T_z\longrightarrow R-\{\rho(T_z)\},\qquad z\in R.       \tag{1.5}
\]

They form a loopless functional digraph on the `m+1` facets of `R`, have
no directed two-cycle, and consequently contain a directed cycle of length
at least three.

#### Proof

At tail `T_z`, inserting `z` is the unique outgoing rooted arc whose union
is `R`; (1.3) gives (1.5).  This proves functional outdegree one.  A loop
would require `z in T_z`.  An opposite pair between two facets would require
their common rank-`m-1` coatom to be matched by `M_0` to both facets.  Both
are impossible.  Every finite functional digraph contains a directed cycle,
which therefore has length at least three.  \(\square\)

The lemma includes every colour containing any distinguished boundary root.
No quotient shore is removed.

## 2. A protected acyclic atlas with every colour

Choose an injective real potential `phi` on the rooted vertices which is
strictly increasing along `P_1`, and put

\[
        E_\phi=\{T\to T':\phi(T)<\phi(T')\}.                      \tag{2.1}
\]

### Theorem 2.1 (protected forward full-colour atlas)

The atlas `E_phi`

1. contains every arc of `P_1`;
2. contains at least one arc of every `R in mathcal U`; and
3. has no directed cycle.

#### Proof

The first and third statements follow from the choice of `phi`.  On the
directed cycle in a colour fibre from Lemma 1.1, not every edge can point
from larger to smaller potential: strict decrease around a closed directed
cycle is impossible.  Hence that fibre has a forward edge.  \(\square\)

This is occurrence availability, not a matching.  Many atlas arcs can share
a tail or a head.

There are two useful independent checks.

* For every fixed `M_0`, the upper-colour partition matroid and the rooted
  graphic matroid have a common integral set containing one arc of every
  upper colour.  It is a `Cat_m`-component graphic forest, but it need not
  obey tail/head capacity and the proved unprotected statement need not
  contain `P_1`.
* The full Hamilton system has a common strict fractional point: constant
  arc weight `(W-1)/(W(m-1))` has tree mass `W-1`, tail and head load
  `(W-1)/W<1`, and colour load
  `(m+1)(W-1)/(W(m-1))>1`.

Thus ordinary graphic rank and fractional capacity do not locate the
integral obstruction.

## 3. Exact three-role linearization

For an arc set `Q`, let `delta^+(v),delta^-(v)` be its tail and head stars,
and let `E_R` be the full colour fibre.

### Theorem 3.1 (exact Row-2 residual)

For the fixed pivot phase `(M_0,P_1)`, the following are equivalent.

1. There is a rooted lower-rainbow Johnson Hamilton owner path containing
   the pivot collar and carrying at least one occurrence of every full
   immediate-upper colour.
2. There are an injective potential `phi` increasing along `P_1` and
   `Q subset E_phi` such that
   \[
   \begin{aligned}
      &P_1\subseteq Q,\qquad |Q|=W-1,\\
      &|Q\cap\delta^+(v)|\le1,qquad
       |Q\cap\delta^-(v)|\le1 &&(v),\\
      &|Q\cap E_R|\ge1 &&(R\in\mathcal U).             \tag{3.1}
   \end{aligned}
   \]

If a rooted source `s_*` and sink `t_*` are prescribed, add

\[
 \phi(s_*)=\min\phi,\qquad \phi(t_*)=\max\phi,
 \qquad Q\cap\delta^-(s_*)=Q\cap\delta^+(t_*)=\varnothing.   \tag{3.2}
\]

For the corrected terminal aperture, take `t_*=o` and require
`M_0(o)` to be the intended endpoint owner.

#### Proof

Given the path, order the rooted vertices along it and use that order for
`phi`; all rows in (3.1) follow.

Conversely, an undirected cycle in `Q` would, under the tail/head capacity
rows, have exactly one entering and one leaving arc at every cycle vertex.
It would therefore be a coherent directed cycle, impossible in `E_phi`.
Thus `Q` is a forest.  It has `W` spanning vertices and `W-1` edges, so it
is connected.  The port capacities make it one directed Hamilton path.
Expanding every rooted vertex by its `M_0` incidence yields a spanning
alternating Middle Levels path; its owner projection is Johnson, and its
`W-1` intersections are precisely the rooted vertices other than the sink.
Every upper colour occurs by the last row of (3.1).  Finally
`o subset M_0(o)` is the endpoint aperture.  The endpoint statement (3.2)
is the same argument with the path extrema fixed.  \(\square\)

Therefore the first unresolved integral object is a **three-role coloured
near-perfect matching**, not occurrence supply, graphic Rado, or subtour
elimination.  It is not ordinary bipartite Hall: the same chosen edge must
simultaneously serve its tail, head, and colour roles.

Once `Q` exists, it is itself the replayed path support `S`.  Every residual
upper family in the protected Rado theorem is nonempty, and every subset of
`S` is graphic-independent.  Rado then only selects representatives already
born on the path; it creates no colour occurrence.

## 4. Exact external-chord ledger

For a completed rooted owner path and `R in mathcal U`, let

* `u_R` be the multiplicity of `R` as an adjacent-owner union;
* `a_R` count owner-path endpoints contained in `R`;
* `m_R=1_(o subset R)` for the omitted root; and
* `g_R` count used roots `L subset R` whose two incident owners both lie
  outside `R`.

Then

\[
 u_R-1=g_R-(h_m+a_R-m_R),\qquad
 h_m={m+1\choose2}-2(m+1)+1.                              \tag{4.1}
\]

Consequently Row 2 is equivalent, on a completed path, to

\[
                         g_R\ge h_m+a_R-m_R
                         \qquad(R\in\mathcal U),              \tag{4.2}
\]

and the total surplus is exactly

\[
         \sum_R(g_R-h_m-a_R+m_R)=C-1.                         \tag{4.3}
\]

At K17 (`m=9`), the generic threshold is `26` and the entire slack is only
`4861`.  This explains why all scalar and fractional rows can pass while
integral full-colour rounding remains tight.

## 5. Cycle-cover plus transparent pull tree

The exact turn-factor route is an alternative sufficient certificate.  A
turn table chooses one pair of rank-`m` owners above every lower root and is
balanced when every owner occurs twice.  Balanced tables are exactly
spanning Middle Levels two-factors; their upper task at root `L` is the
union of the chosen owner pair.

### Theorem 5.1 (transparent factor-to-path implication)

Assume a phase-oriented two-factor `F`:

1. contains the pivot predecessor/successor phases;
2. has an eligible occurrence of every full-shore immediate-upper task;
3. admits a pairwise incidence-vertex-disjoint family of strict one-phase
   pulls whose component--pull incidence graph is a tree;
4. each pull preserves the complete eligible task-label multiset and avoids
   the pivot; and
5. `b` factor turns are ineligible and `C-b+1>3d`.

Then the pulls produce one upper-covering Hamilton cycle containing the
pivot, and a redundant eligible provider outside the pivot can be cut to
give the rooted Row-2 path with the corrected aperture.

#### Proof

Root the component--pull incidence tree.  In parent-first order, every
strict pull sees one accumulated parent component and otherwise fresh child
components, so it merges them and does not split an earlier component.
Disjoint supports preserve later pulls.  Task transparency retains every
upper occurrence.

There are `W-b` eligible occurrences covering `U` tasks.  If `s` task
classes are repeated, the occurrences in repeated classes number

\[
                         (W-b)-U+s=C-b+s.                       \tag{5.1}
\]

Under the displayed strict inequality there is a repeat, so `s>=1`; at
least `C-b+1>3d` redundant eligible occurrences exist.  One lies outside
the `3d` pivot roots.  Delete its non-`M_0` incidence.  Its duplicate keeps
the task, the incidence cycle becomes one rooted path, and the omitted root
is contained in its retained `M_0` endpoint owner.  \(\square\)

For the unguarded rank-`m+1` colour shore `b=0`; `Cat_m>=m` for `m>=3`
and `m>=3d+1` make the safe opening automatic.  Named occurrence tasks not
determined by the rank-`m+1` value need their own eligibility alphabet and
are not counted silently here.

The missing factor/pull assertion is `PUTP(m,d)`: construct the factor and
the strict transparent incidence tree in Theorem 5.1.  Static connectivity
of the coherent-ECO two-section is insufficient; simultaneous port
compatibility, strict prefix merging, and task transparency are essential.

The unmodified canonical lexical shortcut is impossible for all `m>=12`.
Its audited missing-colour count exceeds the maximum `3(C_r-1)` values
changeable by a canonical pull spanning tree.  This no-go is scoped to the
lexical base and canonical pulls; it does not exclude a nonlexical repaired
factor.

## 6. A quantitative prospective full-colour absorber

For a prescribed diamond target `A` on the odd host, fix the canonical
auxiliary owner-slot section of the suspended gain-one hex catalogue.

### Theorem 6.1 (private gain-one bank)

Every target has exactly

\[
                            2(m-1)(m-2)                          \tag{6.1}
\]

canonical packets.  Any non-target named lower, upper, or owner-slot
resource lies in at most `2(m-1)` of them.  Hence `p` pairwise-resource-
disjoint targets admit pairwise-private packets avoiding an external bank
`B` whenever

\[
                         |B|+12(p-1)<m-2.                        \tag{6.2}
\]

For each chosen packet the three-edge on phase has exactly the resource
multiset of its two-edge off phase plus the target lower colour, target
upper colour, and two target owner slots.

#### Proof

Write the target lower set as `D`, its upper set as `D+p+q`, choose
`b in D`, `c` outside the upper set, and one of the two orders of `p,q`.
There are `(m-1)(m-2)2` choices.  Literal parameter recovery gives maximum
non-target load `2(m-1)`.  Before choosing the packet for one target, the
external bank, the other target resources, and the eight auxiliaries of
earlier packets forbid at most `|B|+12(p-1)` resources.  Under (6.2) they
kill fewer candidates than (6.1), so greedy selection succeeds.  The
on/off resource identity is the direct six-atom calculation frozen in the
companion theorem and audit.  \(\square\)

This is prospective.  The two off atoms must already be planted and the
target slots free.  Moreover the target upper is supplied by a new atom
whose rooted tail/head must be bound to the same `M_0`; the bookkeeping
target edge is not retained.  Local resource repair therefore does not
prove (3.1).  The exact remaining absorber clause `DOP(m,d,p)` is:

> plant the private off phases in one pivot-compatible graphic factor so
> that their on phases bind to the same predecessor phase, pass the port
> capacities, and retain a tree-coherent transparent pull tree.

For `p,|B|=O(d)` and `d=O(sqrt(m))`, (6.2) is eventually automatic.  Thus
packet abundance and privacy are no longer the asymptotic obstruction;
correlated physical planting is.

## 7. K17 full-shore calibration

The independently replayed model

```text
/home/amodo/or15/work/root_k17_fullq1_ordinary_circulation_20260802/
  fullq1_13.best.model
SHA-256 e7ea3841cde04129e3b0af008da0ab2ca2deb8936f09ae22d43a9174ac888a31
```

has a connected guarded `h=1` augmented incidence factor whose ordinary
diamonds cover all `19,448/19,448` rank-ten colours.  Both licensed linear
openings and both cyclic seam palettes remain `19,448/19,448`.  The
ordinary contracted factor has two components, while the augmented factor
is connected through the exceptional lollipop state.

This is positive evidence for prospective full-shore factor birth and for
transparent opening: the 36 `D`-superset colours need no exceptional
provider.  It is not an instance of Theorem 3.1, because the augmented
degrees duplicate `D` and omit `M` rather than giving an ordinary rooted
near-perfect matching.

The independently replayed strict descendant

```text
/home/amodo/or15/work/root_k17_q1zero_residence_oracle_20260802/
  checkpoint_fullq1_res2169/model
SHA-256 3107fc58bbf222bb5e00e6ff9ceb79d23623a156811591a033912f90ab29354d
```

retains both full opened palettes, the frozen protected branch, every guard,
and augmented connectivity.  Its opened run histogram is `(1361,808)`, so
its exact residence debt is `2,169`; its rank-11/12/13 holes are
`1516/267/4`.  The independent audit JSON has SHA-256
`a84e1c54a77ae925c06e3ca68b6aaf0189d667c9e0cdc9de0f114e938db90184`.
It therefore still does not prove residence, the erosion/source row, deeper
upper completeness, compiler feasibility, a K17 word, or an all-`m`
theorem.  In particular the protected finite branch is not a certified
literal `3d` `PCS` pivot collar/history state.

## 8. Exact remaining theorem and scope

The exact Row-2 residual after all unconditional reductions is:

> **Protected coloured linearization `PCL(m,d)`.**  For some perfect
> extension `M_0` of the pivot predecessor phase, choose a compatible
> potential and a near-perfect matching `Q` satisfying (3.1), with the
> required endpoint extrema if the aperture is named.

Equivalently one may prove the stronger sufficient `PUTP(m,d)`, or a
controlled-defect `DOP(m,d,p)` followed by `PUTP`.

Unconditional here:

* the protected forward atlas contains every full-shore colour;
* graphic plus colour selection is integral without port caps;
* the complete Hamilton system is fractionally feasible;
* (3.1) is the exact remaining integral selector;
* the external-chord threshold and total Catalan slack are exact;
* transparent pull-tree plus safe-opening implication is exact; and
* the fixed-slot private absorber supply and packing inequality are exact.

Open:

* `PCL`, `PUTP`, or `DOP` for all sufficiently large `m`;
* a rooted ordinary-path extraction from the K17 augmented factor;
* full-row residence and global address/history replay;
* higher upper witnesses, preword deletion, common-cap/lower compiler, and
  regeneration; and
* any `PCS`, `B+1`, equality, or all-k conclusion.
