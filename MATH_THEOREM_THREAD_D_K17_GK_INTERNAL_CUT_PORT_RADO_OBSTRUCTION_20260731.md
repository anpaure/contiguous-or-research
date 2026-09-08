# The internal-cut port face has an exact 35-row Rado obstruction

Date: 2026-07-31  
Status: exact solver-free obstruction for the **internal--internal-cut,
336-UU-slot face only**; not a no-go for the later mixed terminal/internal
cut model

## 1. Object and scope

Start with the authenticated two-cut Greene--Kleitman forest on the
rank-seven layer of `B_17`.  It has `10152` edges, `5224` path components,
`10448` degree-one vertices and `4928` degree-two vertices.  Let

\[
 {cal Y}=\{D:\ |D|=6,\ D\text{ is absent from the seed and no original
 endpoint contains }D\}.
\]

The literal census gives `|Y|=674`.

This note considers only cuts of a seed edge whose two ends have seed degree
two.  Such a cut exposes two side-labelled ports

\[
       p=(v,n_v;e),
\]

where `e` is the deleted edge and `n_v` is the unique retained seed neighbour
of `v`.  Two selected cuts must be vertex-disjoint.  The later mixed model
which also cuts a terminal seed edge is not represented here: a terminal cut
has a different boundary-turn ledger.

## 2. Exact cut and port catalogues

There are exactly `1888` eligible internal--internal seed cuts.  Their
vertex-conflict graph has `564` edges and independence number `1424`.
Thus selecting `169` vertex-disjoint cuts is not itself a scalar obstruction.

A Layer-1 service incidence is

\[
        (p,D),\qquad D\in{cal Y},\quad D\subset v.       \tag{2.1}
\]

Among the `3776` side-labelled ports there are `1820` such incidences,
`1144` nonempty port menus and only `340` reachable hard colours.  The
port-degree histogram is

\[
 0^{2632}1^{868}2^{47}3^{106}4^{75}5^{48}.             \tag{2.2}
\]

Exactly `501` cuts have a nonempty menu on both sides; their maximum
vertex-disjoint subfamily has size `394`.

## 3. Literal local q8/h9 refinement

For every Layer-1 incidence `(p,D)` the exhaustive local catalogue chooses
an unused rank-seven neighbour `w` and records

\[
 q_8=v\cup w,
 \qquad
 h_9=n_v\cup v\cup w.                                 \tag{3.1}
\]

If `q8` is an old edge colour, its unique seed edge must be cut.  If `h9` is
an old turn, at least one of the two incident seed edges at its unique centre
must be cut.  The catalogue stores every inclusion-minimal, pairwise
vertex-disjoint dependency set.

There are `3572` locally feasible concrete `(p,D,w)` rows.  Their minimum
cut-dependency histogram is

\[
             1^{3061}2^{438}3^{73}.                   \tag{3.2}
\]

Most importantly, **every one of the 1820 containment incidences has a
one-cut realization**: selecting the port's own cut already makes its chosen
`q8` and boundary `h9` legal.  Hence local dynamic freshness does not shrink
the Layer-1 graph.  This is not a simultaneous packing statement; different
rows may still collide globally.

## 4. Exact Rado obstruction at the obsolete `c=169` face

Let `G` be the bipartite graph from the `674` hard colours to all `3776`
ports using (2.1).  Exact Hopcroft--Karp replay gives

\[
                  \nu(G)=303.                         \tag{4.1}
\]

The canonical Dulmage--Mendelsohn alternating closure contains `524` hard
rows and only `153` port neighbours, hence has deficiency `371`.

Now grant the old schedule its `336` internal--internal service positions
as **completely universal** providers.  This strictly relaxes the physical
ear problem: endpoint, turn, internal-owner and global collision constraints
are all discarded.  Even then the same DM shore satisfies

\[
                 524>153+336,                         \tag{4.2}
\]

and therefore the combined transversal rank is only

\[
                 303+336=639<674.                     \tag{4.3}
\]

Thus the internal--internal-cut model with exactly `336` UU hard-service
slots is infeasible.  The deficiency is `35`.  This conclusion is stronger
than enforcing `c=169`: it was obtained after dropping the cut-count,
vertex-disjointness and paired-port activation rows altogether.

The DM witness has additional structure: its `153` neighbouring ports come
from `153` distinct cuts, at most one side of each cut.

## 5. What this does not prove

The obstruction is tied to the `336`-UU-slot face and to cuts whose two seed
ends both have degree two.  It does **not** apply without a fresh audit to:

1. a longer-ear ledger with more UU hard-service positions;
2. a mixed model containing terminal endpoint--internal cuts;
3. a cut count such as `c=312` whose exact terminal/internal decomposition
   and surviving-turn formula have been certified separately; or
4. any nonflat/value-changing reroute.

In particular, the corrected prefix ledger is `7401` length-three owners
plus `16909` length-four owners.  Nothing here assumes that all prefix owners
have length four.

## 6. Reproducibility

Source:

```text
scratch/audit_threadD_k17_gk_cut_port_service_20260731.py
```

Generated files:

```text
scratch/threadD_k17_gk_cut_port_service_20260731.audit.json
scratch/threadD_k17_gk_cut_port_cuts_20260731.tsv
scratch/threadD_k17_gk_cut_port_options_20260731.tsv
scratch/threadD_k17_gk_cut_port_dm_witness_20260731.tsv
```

The audit rebuilds the forest from the two pivot maps, independently checks
all cardinalities, constructs a maximum matching, and verifies the DM
neighbour set literally.  It runs in well under one second and needs no SAT
solver.
