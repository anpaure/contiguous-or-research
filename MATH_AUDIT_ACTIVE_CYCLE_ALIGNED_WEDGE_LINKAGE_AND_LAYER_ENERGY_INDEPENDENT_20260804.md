# Independent audit: active cycle-aligned wedge linkage and layer energy

**Date:** 2026-08-04  
**Method:** independent symbolic replay; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_ACTIVE_CYCLE_ALIGNED_WEDGE_LINKAGE_AND_LAYER_ENERGY_20260804.md`  
**Audited theorem SHA-256:**
`427fbd30f4208b81d56218e199fb050a7d1bda5463a7a1dba49a0b8ca242e01d`  
**Author self-audit:**
`MATH_AUDIT_ACTIVE_CYCLE_ALIGNED_WEDGE_LINKAGE_AND_LAYER_ENERGY_SELF_20260804.md`  
**Author self-audit SHA-256:**
`c6a2936389eaee9722bd2c0546a48b6b5f940df1f6a2c8f8d51df232359214c6`

**Verdict:** **GO under the theorem's explicit selection-stable activity,
private-resource, and protected-factor premises.**  No mathematical
correction is required.

## 1. Sequential owner and terminal exclusions

Two distinct lower turns have at most one common rank-`m` owner, so at
stage `i` the set `F_i` of current owner coordinates already present in an
earlier complete star has size at most `i-1`.

The number of edges of `K_m` incident with a set of `q` vertices is

\[
 \binom m2-\binom{m-q}2=B_q(m).
\]

Thus old owners forbid at most `B_(i-1)(m)` current wedge edges.

For terminals, the set first assigned at one earlier source is a subset
of one Hamilton cycle in that source's terminal graph.  At exchange
distance one, its overlap with the current terminal cloud is one vertex
star, so the cycle contributes at most two edges.  At distance two it
contributes at most one, and farther away zero.  Hence

\[
 |E_i|\le2(i-1).
\]

The coefficient two is not an artefact of the proof: for an adjacent
source, a Hamilton cycle has exactly two edges in the common vertex star,
and both may belong to its newly assigned set when the corresponding
ports are new.  Thus `+2` per earlier source is the best uniform bound
available from the pairwise overlap lemma alone.  The sum may overlap the
old-owner exclusion, but adding the two cardinality bounds is a valid
worst-case union bound.

Therefore a menu strictly larger than

\[
 B_{p-1}(m)+2(p-1)
\]

contains an edge outside both forbidden banks at every stage.  Both of its
owner endpoints are new relative to all earlier stars, and its terminal
has not been assigned earlier.

## 2. Ore forcing of the distinguished active edge

Deleting `E_i` from `K_m` gives

\[
 \delta(G_i)\ge m-1-|E_i|
 \ge m-2i+1.
\]

Since

\[
 i\le p\le\left\lfloor{m+1\over4}\right\rfloor,
\]

one has

\[
 m-2i+1\ge{m+1\over2}.
\]

Thus every nonadjacent pair in `G_i` has degree sum at least `m+1`.
Ore's Hamilton-connected theorem applies: `G_i` has a Hamilton path
between the prelabelled active endpoint `a_i` and the other endpoint
`b_i`.

The chosen active edge `e_i=a_i b_i` lies in `G_i`.  For `m>=3`, a
Hamilton path whose endpoints are `a_i,b_i` cannot itself use `e_i`: if
it did, both path endpoints would already have their unique path edge and
no third vertex could occur.  Adding `e_i` therefore creates a simple
Hamilton cycle containing the distinguished edge.  Orienting that cycle
so that `a_i -> b_i` makes `e_i` the outgoing assignment at the already
chosen active side.  This proves exactly

\[
 \phi(L_i+a_i)=L_i+a_i+b_i.
\]

There is no hidden use of an unspecified cycle edge or a post hoc choice
of active orientation.

## 3. Full-port induction and distinctness

Only owner coordinates new at stage `i` receive outgoing cycle-edge
assignments.  Outgoing edges of an oriented Hamilton cycle are distinct,
and the entire cycle avoids `E_i`, so all new terminals are mutually
distinct and avoid every old terminal.  Previously seen owners retain
their assignments.  The newly assigned set remains a subset of one
Hamilton cycle, preserving the exact invariant required at later stages.

Avoidance of `F_i` by both endpoints gives global distinctness of the
`2p` selected owners.  Injectivity of `phi` gives distinctness of selected
q1 terminals.  These statements concern values; the theorem separately
assumes the selection-stable occurrence/type privacy needed to infer
coexisting active physical paths.

## 4. Protected-factor and occurrence step

The selected wedge bank has lower degree two, upper degree one, and
exactly `2p` incidence edges.  Under degree compatibility and

\[
 |P_*|+2p\le m-2,
\]

the small protected-factor theorem applies.  At each selected lower turn,
the two protected incidences exhaust factor degree two, so its literal q1
union is the preselected terminal `Z_i`.  Distinct selected owner values
also prevent two selected turns from being consecutive in a factor
component: consecutive lower turns would share their intervening owner.

The occurrence/private-branch conclusion correctly relies on the stated
premise that the distinguished active-side certificate survives arbitrary
unprotected completion and factor orientation.  It is not inferred from
value distinctness alone.

## 5. Layer-energy arithmetic and the extra terminal charge

If fixed inactivity deletes at most

\[
 \binom{r_i}2+t_i
\]

wedge edges, then the strengthened active-menu row follows from

\[
 \binom{r_i}2+t_i
 <\binom{m-p+1}2-2(p-1)=T_*.
\]

The subtraction `2(p-1)` is exactly the dynamic reserve for earlier
Hamilton-cycle terminal assignments.  Those assignments are selected
after the fixed active menus are exposed, so they cannot be silently
absorbed into `t_i`; reserving them separately is necessary and
proof-safe.

For an integer `R`, a failing source with `r_i<R` must satisfy

\[
 t_i\ge T_*-\binom{R-1}2=S_R^*.
\]

Markov counting therefore gives precisely

\[
 \left\lfloor{I\over R}\right\rfloor
 +\left\lfloor{J\over S_R^*}\right\rfloor.
\]

With `R=floor(m/2)+1` and `p=O(sqrt m)`, direct expansion yields

\[
 S_R^*={3m^2\over8}-O(m^{3/2})\ge{m^2\over4}
\]

eventually.  Hence `I<=Am,J<=Dm^2` gives the displayed bound
`floor(2A)+floor(4D)`.  Reindexing retained sources can only lower both
the menu threshold and the Hamilton-connectedness burden; the factor edge
budget still has to be checked with the retained count, exactly as the
theorem states.

## 6. Scope verdict

The theorem correctly proves the correlation

\[
 \text{chosen active wedge}
 \to\text{Hamilton cycle through its distinguished edge}
 \to\text{injective Boolean suffix}
 \to\text{literal factor q1 occurrence}.
\]

It does not prove activity-menu existence, typed/phase legality, hidden
bank pricing, product-cap compatibility, or nonaccumulating regeneration.
Those exclusions are explicit in both theorem and self-audit.

**Independent verdict:** GO.
