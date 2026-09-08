# Compact all-length Hall obstruction for the immutable K17 GK forest

Date: 2026-07-31  
Status: exact fixed-forest NO-GO; cut-and-reroute models are outside scope.

## Theorem

Fix the authenticated two-cut Greene--Kleitman rank-seven forest with
10,152 edges, 15,376 used vertices, 5,224 path components and 4,072 unused
rank-seven vertices.  Keep every seed edge.  Permit arbitrary-length ears
whose ends are original forest endpoints and whose internal vertices are
unused.  Require every new edge union to be fresh and globally distinct and
every boundary/internal turn to have rank nine, be seed-fresh and be globally
distinct.

No such ear family covers all 2,224 missing rank-six colours.

## Compact catalogue

The literal ear catalogue through length four already has

\[
 12542, 726760, 23730328, 634069639
\]

reversal classes, so monolithic ear variables are unnecessary.  Instead use:

* one state for each seed-fresh Johnson edge between an original endpoint or
  unused vertex;
* at every unused vertex, one wedge state for a compatible pair of incident
  edges and its rank-nine turn.

An endpoint--unused edge survives only if it occurs in a surviving wedge at
the unused end; an unused--unused edge must survive at both ends.  Iterating
this support condition to the greatest fixed point gives

\[
\begin{array}{c|r|r}
&\text{raw}&\text{supported}\\ \hline
\text{edges}&148153&145117\\
\text{wedges}&4217728&4194675.
\end{array}
\]

The supported edge types are

\[
 EE=12542,qquad EU=79704,qquad UU=52871.
\]

This is an exact relaxation of every permitted ear family: each selected ear
edge survives the support peel because the actual ear supplies a compatible
wedge at every unused end.

## Rank-six to rank-eight Hall graph

Make a bipartite graph with the 2,224 missing rank-six colours on the left
and fresh rank-eight masks on the right.  Join `D` to `Q` when the supported
catalogue contains an edge with intersection `D` and union `Q`.  The exact
graph has

\[
 |L|=2224,qquad |R|=6530,qquad |E|=33564.
\]

It has 416 zero rows and maximum matching rank

\[
                         1780<2224.                \tag{1}
\]

The canonical alternating closure of a maximum matching has

\[
 |A|=584,qquad |N(A)|=140,                        \tag{2}
\]

so (2) is a deficiency-444 Hall cut.  Global rank-eight injectivity maps one
chosen provider for every covered rank-six colour to a distinct right mask.
Thus any complete ear family would give a matching saturating `L`,
contradicting (1).

The obstruction allows arbitrary ear length and drops endpoint, unused-owner,
turn-collision and component-topology constraints after the support peel.
It is therefore a genuine necessary-condition no-go, not a failure of a
particular short-ear ledger.

## Independent replay

The primary C++ catalogue was compiled and run on one H100 CPU process under
a 2 GiB address-space cap.  Catalogue execution took 0.87 seconds and
225,504 KiB maximum RSS.  Its emitted relation was replayed by an independent
matching implementation.  A second independently written C++ program also
reconstructed the edge core and the same Hall graph directly, without using
the primary producer relation.  Both obtain exactly `1780/2224` and the
`584/140` DM shore.

Primary artifacts:

```text
scratch/threadD_k17_gk_ear_compact_catalogue_20260731.cpp
scratch/threadD_k17_gk_ear_compact_catalogue_20260731.audit.json
scratch/audit_threadD_k17_gk_compact_dm_witness_20260731.py
scratch/threadD_k17_gk_compact_dm_witness_20260731.audit.json
```

Independent reconstruction:

```text
scratch/audit_independent_k17_gk_supported_ear_hall_20260731.cpp
scratch/independent_k17_gk_supported_ear_hall_20260731.audit.json
scratch/h2_audit_k17_gk_ear_compact_incidence_20260731.cpp
scratch/h2_k17_gk_ear_compact_incidence_20260731.verify.json
```

## Scope

Cutting seed edges changes the endpoint set and releases their rank-six,
rank-eight and rank-nine resources, so it changes the graph in this theorem.
The result does not obstruct the dynamic cut master.  It proves precisely
that a viable K17 GK tail must change the seed forest, not merely choose
longer ears inside the immutable endpoint/unused face.
