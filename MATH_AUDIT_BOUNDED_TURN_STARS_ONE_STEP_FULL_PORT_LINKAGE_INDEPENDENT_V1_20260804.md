# Independent audit: arbitrary bounded-turn one-step full-port linkage

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Audited theorem:** `MATH_THEOREM_BOUNDED_TURN_STARS_ONE_STEP_FULL_PORT_LINKAGE_20260804.md`  
**Audited theorem SHA-256:** `5899c6f8f40504d58ffa96e94d17a100e4d77fc59fa0a4363489c1528e9392f3`  
**Self-audit SHA-256:** `90fd331a2ed9db8f1fbd7ffe74befbca7a8dd913990d7f8ef5f413d2e5a744cb`

## Verdict

**GO at the stated Boolean-value and explicitly occurrence-lifted scope.**
The final version includes the necessary typed-edge and private-prefix
premises in its cap-level corollary.  Pairwise source separation is not
needed for the value-level linkage when

\[
 1\le p\le\left\lfloor\frac{m+2}{4}\right\rfloor.
\]

## Independent replay

### 1. Exact overlaps

For rank-$m-1$ turns at Johnson distance $d$, their union has rank
$m-1+d$.  Consequently their owner stars intersect in one value exactly
when $d=1$, and otherwise are disjoint.  Their rank-$m+1$ terminal clouds
intersect in $m-1$, one, or zero values for $d=1$, $d=2$, or $d\ge3$,
respectively.

At $d=1$, the common terminal family is a vertex-star in each of the two
$K_m$ representations.  Any subset of a Hamilton cycle meets that star in
at most two edges.  At $d=2$ the cloud intersection has size one.  Hence a
cycle-supported terminal bank from one earlier source forbids at most two
edges at the current source.

### 2. Dirac induction and shared-port deduplication

At stage $i$, at most $2(i-1)$ edges are forbidden, so the residual graph
has

\[
 \delta(H_i)\ge m-1-2(i-1)=m-2i+1.
\]

The assumed range gives $m-2i+1\ge m/2$, and Dirac supplies a Hamilton
cycle.  Orienting it assigns distinct outgoing cycle edges to all newly
seen owner coordinates.  A port already present in an earlier star keeps
its old assignment; its current outgoing edge is simply unused.  Thus
shared owner values are deduplicated rather than assigned twice.

Every new terminal avoids the old terminal bank, and the terminals newly
assigned at this stage remain a subset of one Hamilton cycle.  This closes
the induction invariant used by the overlap bound.  At termination every
distinct owner in the union has exactly one terminal, all owner endpoints
are distinct, and all terminal endpoints are distinct.  The displayed
one-edge incidence paths are therefore globally vertex-disjoint.

### 3. Deletion corank

If a unit-capacity bank meets $h_F$ displayed suffix paths, all unhit paths
survive, so

\[
 r_{\Gamma_F}(P_0)\ge |P_0|-h_F.
\]

Because the displayed paths are vertex-disjoint, one deleted capacity
meets at most one path and $h_F\le|F|$.  Extra routes in the residual
gammoid can only improve this rank lower bound.

### 4. Near-full typed application

The corrected corollary separately assumes all physical facts not implied
by Boolean containment: distinct occurrence materialization, a legal typed
edge for each displayed owner-terminal pair, completion-stable empty/private
source prefixes, distinct unit capacities, legal compensation-disjoint
sinks, and survival of the source/prefix resources.  With at most $m-p$
displayed suffix paths hit, the full owner-port corank is at most $m-p$,
so the frozen near-full owner-gammoid theorem applies in its valid range.

## Scope boundary

The theorem removes pairwise source separation and the need to assume raw
full owner-port rank.  It does not construct the required occurrence lift,
typed containment edges, private prefixes, or a regenerative compensation
linkage with at most $m-p$ path hits.  Those physical cap-state rows remain
premises; no all-dimensional upper bound follows from the value-level
linkage alone.
