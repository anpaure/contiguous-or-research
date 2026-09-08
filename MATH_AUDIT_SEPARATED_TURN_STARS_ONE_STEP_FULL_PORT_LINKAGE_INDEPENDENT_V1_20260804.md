# Independent audit: separated-turn one-step full-port linkage

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited theorem:** `MATH_THEOREM_SEPARATED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`  
**Audited theorem SHA-256:** `9a1d8b4e77b1ba7f8a7b8af1e334b9c112feab4ca567284d851331a96a4921e1`  
**Self-audit SHA-256:** `88c6659566a9979877411f8fdb5098d28fa706218eb66cd9ecd45ced07281f33`

## Verdict

**GO at the stated separated-source Boolean-incidence scope.**  The owner
and terminal intersection bounds, Dirac induction, disjoint linkage,
deletion-corank estimate, and near-full-gammoid application all replay
exactly.

## Independent replay

### 1. Owner and terminal cloud intersections

For two rank-$m-1$ turns at Johnson distance $d$, their union has rank
$m-1+d$.  A common rank-$m$ owner therefore forces $d\le1$, so
distance at least two makes their complete owner stars disjoint.  A common
rank-$m+1$ terminal forces $d\le2$; at $d=2$, the union already has
rank $m+1$ and is the unique common terminal.  For $d>2$, the terminal
clouds are disjoint.

### 2. Dirac induction

At source $i$, each earlier source contributes at most one already used
terminal to the current cloud.  Hence at most $i-1$ edges are removed
from the complete graph on its $m$ owner coordinates.  The residual graph
has

\[
 \delta(H_i)\ge m-1-(i-1)=m-i.
\]

Since $i\le p\le\lfloor m/2\rfloor$, this is at least $m/2$, and
Dirac's theorem applies for $m\ge3$.  Orienting the Hamilton cycle assigns
each coordinate $a$ its outgoing edge $\{a,b(a)\}$.  These $m$ cycle
edges are distinct and each associated terminal contains its assigned
owner.

Inductive avoidance makes all selected terminal values globally distinct;
the separated-source lemma makes all owner values globally distinct.
Because owners and terminals occupy different Boolean ranks, the resulting
$pm$ one-edge incidence paths are pairwise vertex-disjoint.

### 3. Deletion and gammoid corank

If a capacity bank $F$ meets $h_F$ displayed paths, every unhit path
survives and still links its owner port to its distinct sink.  Therefore

\[
 r_{\Gamma_F}(P_0)\ge |P_0|-h_F.
\]

Pairwise vertex-disjointness implies that one deleted unit-capacity vertex
meets at most one displayed path, so $h_F\le|F|$.  This proves the stated
corank inequality without assuming that the displayed paths exhaust the
residual gammoid; extra residual paths can only improve its rank.

### 4. Near-full application

Under occurrence-faithful materialization, legal typing, source/prefix
survival, and deletion of at most $m-p$ displayed paths, the residual
full-set owner-port corank is at most $m-p$.  The frozen near-full
owner-gammoid theorem applies in the stated range $1\le p\le m-1$, and
selects a globally owner/q1-terminal-distinct wedge bank with simultaneous
routes.  The conclusion is zero-defect at this fixed state.

## Scope boundary

The theorem constructs the value-level raw full-port linkage only after
the lower turns are pairwise Johnson-nonadjacent.  It does not prove that a
regenerative carrier supplies such a source family, that all selected
values have distinct compatible physical occurrences in one phase/cap
state, or that the complete priced deletion bank meets at most $m-p$
paths.  Those occurrence, separation, and regeneration rows remain open.
