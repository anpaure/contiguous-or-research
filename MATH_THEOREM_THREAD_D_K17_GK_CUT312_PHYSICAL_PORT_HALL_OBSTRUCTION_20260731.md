# The frozen `c=312` exposure certificate fails the physical partner Hall row

Date: 2026-07-31  
Status: exact solver-free no-go for one fixed lexicographic-optimal cut and
colour-assignment certificate; not a no-go for the joint cut master

## 1. The authoritative `c=312` ledger

The frozen certificate is

```text
scratch/k17_gk_cut312_certificate_20260731.json
```

Its literal dependency-free replay gives the following two different
partitions of the same `312` cuts.

By seed endpoint degrees:

\[
        90\text{ endpoint--internal}+222\text{ internal--internal}=312.
                                                               \tag{1.1}
\]

By the number of assigned hard colours:

\[
        244\text{ single-assignment}+68\text{ double-assignment}=312,
                                                               \tag{1.2}
\]

and `244+2*68=380` colours are assigned.  Every endpoint--internal cut is
necessarily single-assignment; among the internal--internal cuts, `154` are
single and `68` are double.

The earlier provisional split `214+98` is neither (1.1) nor (1.2), and is
not present in the frozen certificate.  It is superseded for this artifact.

The cuts destroy

\[
                 90+2\cdot222=534                  \tag{1.3}
\]

old turns.  They leave `5536` seed components.  With `1535` new owners, the
correct completion ledger is

\[
 (x_1,x_2,x_3,x_4)=(4336,905,252,42),               \tag{1.4}
\]

giving `5535` joins, `7070` new edges and `12515` new turns.  The naive sum
of `(j+1)x_j` is `12605`; the `90` isolated terminal vertices remove one
boundary turn each, yielding `12515`.

## 2. Exact local physicalization catalogue

Fix all `312` cuts and all `380` colour-to-port assignments in the
certificate.  For an assigned port `(v,n_v;e)` with hard colour `D`, a
physical first neighbour can only be:

1. an unused rank-seven owner `w` containing `D`; or
2. an unassigned exposed internal port containing `D`.

No original endpoint contains `D` by definition.  An assigned exposed port
already spends its unique new incidence and cannot be used again.

For each candidate the audit checks

\[
 q_8=v\cup w,
 \qquad
 h_9=n_v\cup v\cup w,                                \tag{2.1}
\]

against the **dynamic** palettes: an old `q8` is available exactly when its
unique seed edge is one of the `312` cuts, and an old `h9` is available
exactly when at least one of its two incident seed edges was cut.  A direct
exposed-port join is also checked at the second boundary.

The complete catalogue has `670` options.  Its row-degree histogram is

\[
             1^{202}2^{114}3^{31}4^{19}5^{13}6^1.    \tag{2.2}
\]

There are no zero rows.  There are also exactly zero legal direct joins to
the `154` unassigned exposed internal ports; every surviving option uses a
genuinely unused rank-seven owner.  During filtering, `659` candidates lose
their retained old `q8` and three lose a retained old boundary `h9`.

## 3. The physical partner obstruction

Build the bipartite graph from the `380` fixed assignments to their allowed
unused first neighbours.  Its exact matching rank is

\[
                         368<380.                     \tag{3.1}
\]

The canonical alternating closure gives a Hall shore of `77` assignments
with only `65` unused-neighbour values:

\[
                          77>65.                      \tag{3.2}
\]

Thus this fixed exposure assignment cannot be lifted even to disjoint first
neighbours.  This failure precedes simultaneous `q8/h9` bundle collisions,
ear ordering and component connectivity.  Separately projecting the same
options onto `q8` and onto the service-port `h9` gives full ranks `380` and
`380`; the first obstruction is specifically the rank-seven partner shore.

## 4. Exact surviving gate

This does not contradict optimality of the upstream exposure problem.  That
problem optimized only cuts and colour-to-exposed-vertex assignments.  The
weakest live master must select simultaneously:

* the vertex-disjoint cut set;
* the hard-colour assignment;
* one first-neighbour value per assigned port; and then
* globally distinct `q8/h9` bundles and a component path.

The present no-go applies only to the one frozen assignment.  Another
assignment on the same cut set, another optimal `312`-cut set, or more cuts
remain open.

## 5. Reproducibility

```text
scratch/audit_threadD_k17_gk_cut312_physical_ports_20260731.py
scratch/threadD_k17_gk_cut312_physical_ports_20260731.audit.json
scratch/threadD_k17_gk_cut312_physical_port_options_20260731.tsv
scratch/threadD_k17_gk_cut312_physical_port_dm_20260731.tsv
```

The audit reconstructs the entire seed forest and replays every selected cut
without importing OR-Tools or trusting the upstream scalar summary.
