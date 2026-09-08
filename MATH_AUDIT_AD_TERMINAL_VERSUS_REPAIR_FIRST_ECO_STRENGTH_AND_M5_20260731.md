# Audit of terminal-ECO repair versus the repair-first private collar

Date: 2026-07-31  
Status: exact theorem-scope audit; exact project-`m=5` component replay;
the same-bank common-specialization error was identified and is corrected in
the current audited source; no all-`m` existence theorem

## 0. Verdict

The serial implication in
`MATH_THEOREM_AD_TERMINAL_ECO_HAMILTONIZATION_AND_POSTGLUE_DECORATION_REPAIR_20260731.md`
is sound:

\[
 \text{literal strict ECO Hamiltonization}
 \longrightarrow
 \text{terminal Hamilton repair}
 \longrightarrow
 \text{one forest-side joint decoration}
\]

implies a Catalan linear matching.  The project-`m=5` instance in its
Section 4 is also exact.  The two raw standard ECO atoms are port-disjoint
strict binary merges and their component incidence graph is a path on the
three raw components.

The initial version of the strength comparison contained one load-bearing
error: it treated support disjointness and edgewise commutation as if they
preserved component supports and incidence-tree rank across a repair.  The
repaired `m=5` fixture is itself the counterexample to that inference:

* before repair, the terminal ECO basis is the two-atom set
  \(\{g_0,g_1\}\);
* after repair, \(g_0,g_1\) are parallel component joins, and either
  singleton is a basis;
* the two-atom repaired state is still Hamilton and decorated, but the
  second toggle is a rethread, not another edge of an incidence tree.

Thus the operations commute as symmetric differences and both architectures
exist at `m=5`, but their selected incidence-tree bases are different.  The
current audited source has removed the false same-bank claim and states this
distinction explicitly in Section 5.4.  A valid same-bank reversal theorem,
if later needed, must require component faithfulness and the incidence-tree
condition on **both** sides of the repair rectangle.

The current source also adds the exact alternating-circuit universality
theorem.  It is sound: the red and blue degrees of the symmetric difference
of two spanning two-factors agree at every vertex; pairing red and blue
half-edges decomposes it into edge-disjoint alternating closed trails, and
toggling them preserves degree two.  In the bipartite middle-levels graph
these may be split into simple alternating even cycles.  Consequently the minimal
existential central gate is just an accepting decorated Middle Levels
Hamilton cycle.  Terminal-ECO and repair-first private-collar constructions
are incomparable **staged refinements** above that common weaker gate.

## 1. Exact raw `m=5` component audit

Let \(F_0\) be the canonical `ML(9)` factor.  Its component orders are

\[
                         36,\quad72,\quad144.                    \tag{1.1}
\]

The two standard atoms used by the positive terminal construction are

\[
\begin{aligned}
 g_0&=(11001010,10101010),\\
 g_1&=(11001100,10101100).
\end{aligned}                                                    \tag{1.2}
\]

Their literal port sets are

\[
\begin{aligned}
 V(g_0)&=\{83,85,87,89,91,93\},\\
 V(g_1)&=\{51,53,55,57,59,61\},
\end{aligned}                                                    \tag{1.3}
\]

so they are disjoint.  Relative to the three components in the audit's
order, \(g_0\) meets the components of orders `36` and `144`, while
\(g_1\) meets those of orders `72` and `144`.  Literal traversal of all
four subset factors gives

\[
\begin{array}{c|c}
X&\text{component orders of }F_0\triangle X\\ \hline
\varnothing&36,72,144\\
\{g_0\}&72,180\\
\{g_1\}&36,216\\
\{g_0,g_1\}&252.
\end{array}                                                      \tag{1.4}
\]

Consequently each singleton toggle is a strict merge of its two raw
components.  After either first toggle, the other strict toggle merges the
two remaining components.  The component--atom incidence graph is the
path

\[
              36\;--\;g_0\;--\;144\;--\;g_1\;--\;72.           \tag{1.5}
\]

This proves, rather than merely infers from the terminal Hamilton count,
all four Stage-A rows: literal old edges, port disjointness, incidence-tree
rank, and strict component progress in either order.

The raw Hamilton endpoint misses exactly

\[
 \{73,146,292\}\quad\text{below},\qquad
 \{219,365,438\}\quad\text{above}.                              \tag{1.6}
\]

The displayed three `C10` packet is literal and Hamilton-safe on this
endpoint.  Its augmented deficit is

\[
                 3\longrightarrow2\longrightarrow1\longrightarrow0,
                                                                    \tag{1.7}
\]

on both palettes and on the augmented occurrence matching.  The terminal
matching has order `210`, marks `84` occurrences on each shore, and its
binary trace is on the forest side.  Hence Section 4's terminal conclusion
is exact.

## 2. The repaired component audit and the basis change

Apply the same three `C10` circuits before the standard glues.  The prepared
factor \(F_*\) has component orders

\[
                              120,132.                            \tag{2.1}
\]

Both \(g_0\) and \(g_1\) meet both repaired components.  The exact repaired
cube is

\[
\begin{array}{c|c|c}
X&\text{component orders of }F_*\triangle X&\text{trace/gap row}\\ \hline
\varnothing&120,132&\text{forest/forest}\\
\{g_0\}&252&\text{forest/forest}\\
\{g_1\}&252&\text{forest/forest}\\
\{g_0,g_1\}&252&\text{forest/forest}.
\end{array}                                                      \tag{2.2}
\]

Thus the postrepair component ground has rank one.  Either singleton is a
component basis.  Selecting both gives the incidence graph \(K_{2,2}\),
not a tree: after the first atom has merged the two components, the second
atom is a Hamilton rethread.  In particular,

\[
 \{g_0,g_1\}\text{ is the raw basis},\qquad
 \{g_0\}\text{ or }\{g_1\}\text{ is a repaired basis}.          \tag{2.3}
\]

The repair supports are vertex-disjoint from both standard ECO supports,
so the terminal edge set

\[
 F_0\triangle g_0\triangle g_1\triangle C_1\triangle C_2
       \triangle C_3                                             \tag{2.4}
\]

is independent of the written order.  Equation (2.4) does **not** make
the component histories independent of the order.  This is the precise
distinction between endpoint commutation and incidence-tree transport.

The authenticated repair-first private collar selects one of the two
singletons; the compiled channel is explicitly available for \(g_1\).
The full two-label state is a useful decorated bonus endpoint, but it is
not the selected repair-first incidence hypertree.  Conversely, applying
only \(g_1\) (or only \(g_0\)) before the repair does not Hamiltonize the
raw three-component factor.  Therefore no one selected bank witnesses both
architectures in this fixture.

## 3. Exact logical comparison

Write `TER(F,S,P,D)` for the terminal antecedent:

1. \(S\) is a strict disjoint incidence hypertree on the raw factor \(F\);
2. its endpoint is Hamilton;
3. \(P\) is a literal terminal repair sequence on that endpoint; and
4. only the final endpoint carries the forest-side decoration \(D\).

Write `PRI(F,P,T,D,R)` for the nondegenerate repair-first antecedent:

1. \(P\) produces a prepared factor \(F_*\), possibly with several
   components and with no decorated intermediate prefixes;
2. \(T\) is a strict incidence hypertree on \(F_*\);
3. the same occurrence-labelled decoration \(D\) is valid on the declared
   \(T\)-cube and owns every forced port; and
4. \(R\) supplies the simultaneous private/laminar occurrence state.

The word “nondegenerate” excludes the vacuous reclassification in which
one calls the entire terminal construction a repair, stops at an already
Hamilton decorated factor, and chooses the empty collar.

With these fixed stage classes:

* `TER` has no implication to `PRI`.  Its terminal packet may alter every
  component support, owner gap and router bank of the raw atoms.  It need
  not leave any nonempty prepared collar.
* `PRI` has no implication to `TER`.  Its repair may create its useful
  atoms or change their component effects; its selected postrepair basis
  need not Hamiltonize the raw factor.
* For the **central CLMT conclusion**, `TER` uses the weaker gluing
  interface once a raw terminal bank is fixed: no decoration, owner or
  router state is carried through Stage A.
* For recursive or downstream use, `PRI` exports strictly more prepared
  state.  `TER` postpones all occurrence work to one terminal Hamilton
  cycle and supplies no residence, deep-shadow, socket, voltage or compiler
  preservation.

The project-`m=5` ledger (1.4), (2.2) gives a physical illustration of this
incomparability: the same literal switches commute, but the graphic basis
changes from two atoms to one.

There is a weaker common implication.  If either staged architecture ends
in a Hamilton cycle with a forest-side joint decoration, then it proves the
Decorated Middle Levels existential statement.  Conversely, alternating-
circuit universality reaches any such accepting cycle from any fixed
Hamilton cycle through spanning two-factors.  This does not reconstruct a
raw ECO incidence tree, a repaired private collar, owners, or routes, so it
does not reverse either stronger staged certificate.

## 4. Correct common-specialization theorem

For a repair prefix \(P_{\le j}\) and an ECO subset \(X\subseteq S\), put

\[
                    F_{j,X}=F\triangle P_{\le j}
                                  \triangle\bigtriangleup_{t\in X}t. \tag{4.1}
\]

The same selected bank \(S\) supports both orders if all of the following
are supplied.

1. **Literal rectangle.**  Every cell of the required rectangle (4.1) is a
   spanning two-factor and every next declared operation is alternating.
   Pairwise support disjointness is one sufficient local commutation row,
   but is not the whole assertion.
2. **Bottom incidence tree.**  \(S\) is a strict component-faithful
   incidence hypertree on \(F_{0,\varnothing}=F\).
3. **Top incidence tree.**  The same \(S\) is a strict component-faithful
   incidence hypertree on \(F_{s,\varnothing}=F\triangle P\).
4. **Top private decoration.**  One forest-side occurrence decoration,
   literal owner matching, and simultaneous route state is valid on the
   top ECO cube.
5. **Right terminal repair.**  The right boundary starting at
   \(F_{0,S}\) ends at the same decorated Hamilton cell \(F_{s,S}\).

Under Items 1--5, the bottom-then-right boundary is a terminal certificate
and the left-then-top boundary is a repair-first private-collar
certificate, with the same final factor.  This follows directly from the
two incidence-tree theorems and equality of the symmetric difference in
(4.1).

No item in this list follows merely from support disjointness.  In
particular, a remote repair can change the component partition without
touching a port, as (1.4)--(2.2) demonstrate.  The project-`m=5` full bank
passes Items 1, 2 and the terminal endpoint rows but fails Item 3; either
singleton passes Item 3 but fails Item 2.  Hence `m=5` proves coexistence
of the two architectures, not this same-bank common specialization.

## 5. Optional downstream audit: path tilings plus local channels

The path integrality statement of item 2201B combines with the exported
local-channel oracle without loss only on the robust, private face.

Fix a repaired component path and an owner-aligned atom bank.  If every
atom passes

\[
 \operatorname{maxflow}
  (N_{t,Q}-B_{t,Q}-V_t(Q);S_t,T_{t,Q})=\rho(t)                  \tag{5.1}
\]

for all of its at most four ownership states \(Q\), with a literal
unit/grouped semantic map and preallocated pairwise-disjoint sink and child
banks, then (5.1) is a unary filter on tile arcs.  Deleting failed arcs from
the path-tiling DAG preserves its unit-flow integrality.

If ownership or a child resource is co-designed with the tiling, the
natural relaxation is already nonintegral on two backbone edges.  Let
\(x\) be one length-two tile and let \(y,z\) be the two corresponding
length-one tiles.  Suppose \(y,z\) cannot coexist because both require the
same owned old edge, or the same unit child sink.  The active rows are

\[
             x+y=1,\qquad x+z=1,\qquad y+z\le1.                 \tag{5.2}
\]

Their coefficient matrix at equality is

\[
 \begin{pmatrix}1&1&0\\1&0&1\\0&1&1\end{pmatrix},
 \qquad |\det|=2,                                                \tag{5.3}
\]

and \((x,y,z)=(1/2,1/2,1/2)\) is a fractional vertex.  Integrally the only
tiling is \(x=1\).  This is the smallest tile/resource coupling
obstruction: one backbone edge has no nontrivial long-versus-short tiling
choice.

An exact extended formulation remains available.  Scan the component path
and carry, at each frontier, (i) every live conflict-edge ownership bit,
(ii) every used capacity-one sink/adhesion bit, and (iii) every live child
exclusion.  Enrich a tile transition by one literal local linkage signature
for its induced \(Q\).  The resulting state graph is acyclic, and its unit
source--sink flow polytope is integral.  Its size is exponential in the
maximum number of ownership/resource incidences crossing the scan.  The
fact that the ECO conflict graph is a path forest does not itself bound this
frontier width in the unrelated component-path order.  Therefore this DP
is exact but not yet a compact all-`m` theorem.

## 6. Current-source verdict

The current revision of the audited theorem incorporates the material
correction found above.

1. Section 5.4 now records the raw basis \(\{g_0,g_1\}\), the repaired
   singleton bases, and the fact that the full repaired pair is a dependent
   parallel/rethread state.
2. It claims endpoint commutation and coexistence of the two architectures,
   not reversal of one common selected hypertree.
3. Sections 5.1--5.3 distinguish the minimal decorated-Hamilton existence
   route, the transparent route, and the stronger private-collar route.
4. Theorems 1.1, 2.1, 3.1 and 3.2, and Corollary 3.3 pass this audit with
   their stated central-only scope.
5. Section 1 now explicitly excludes \(r_t=1\) neutral/splitting atoms from
   the incidence-hypertree bank.  This hypothesis is necessary: such an
   atom has zero component rank and strict positive component progress does
   not follow from incidence acyclicity.
6. Section 6 correctly scopes the boundary-window seam count \(s\) to two
   already fixed literal rank-\(m\) owner chronologies after decoration,
   physical diamond lift and connector closure.  It does not identify
   \(s\) with the number or support size of the preceding middle-levels
   alternating circuits.

No substantive correction remains.  The bi-admissible rectangle in
Section 4 of this audit is retained as the exact theorem needed if a future
argument again tries to reverse one fixed selected bank.

The audited theorem source had SHA-256

```text
a58f05b535ba6eb9a2fec85ff01721477a66e970c4bfe1230d4f7375965ab26e
```

at this final replay.

## 7. Audited sources

* `MATH_THEOREM_AD_TERMINAL_ECO_HAMILTONIZATION_AND_POSTGLUE_DECORATION_REPAIR_20260731.md`
* `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`
* `MATH_THEOREM_CATALAN_M5_REPAIR_FIXED_ROTATION_ECO_INTEGRATION_20260731.md`
* `MATH_THEOREM_AD_ECO_OWNER_ROUTED_HYPERTREE_GATE_20260731.md`
* `MATH_THEOREM_CATALAN_ECO_LOCAL_CHANNEL_EXPORTED_STATE_AND_FIRST_OBSTRUCTIONS_20260731.md`
* `scratch/catalan_private_triple_standard_m5_refutation_20260731.audit.json`
* `scratch/catalan_standard_m5_three_c10_private_repair_independent_20260731.audit.json`
* `scratch/catalan_m5_repair_fixed_rotation_eco_integration_20260731.audit.json`
