# Exact \((m,d)=(10,3)\) coalesced separated-port MSW arborescence

**Date:** 2026-08-14  
**Status:** exact finite H100 certificate, independently reconstructed and
replayed. This is evidence for, not a proof of, an all-parameter
coalesced-port theorem. The frozen solve uses the equality-only forced-rail
submodel; it remains a valid certificate for the later, more general multiway
common-history gate.

## 1. Certified object

There are

\[
\operatorname{Cat}_{10}=16{,}796
\]

canonical tight MSW rows. Use the highest-valley area-increasing four-packet
DAG from
`MATH_THEOREM_MSW_HIGHEST_VALLEY_FOUR_PACKET_MONOTONE_CONNECTIVITY_20260813.md`.

For an oriented row \(w\), let

\[
 \Sigma_w(a)=\bigl(F_0(w,a),F_1(w,a),F_2(w,a)\bigr)
\]

be its literal forced-history signature at cyclic start \(a\). An edge option
from child \(u\) to parent \(v\) records endpoint orientations, endpoint
starts \((a,b)\), and equality

\[
 \Sigma_u(a)=\Sigma_v(b).
\]

The frozen sufficient CSP chooses one option for every nonmountain row, one global
orientation per row, and enforces cyclic distance at least \(4=d+1\) between
distinct used starts on a row. Several incidences may reuse one start; because
its signature is fixed after the row orientation is chosen, they coalesce into
one literal antecedent alteration. This use of coalescence is justified by
`MATH_THEOREM_COALESCED_MULTIINCIDENCE_COMMON_HISTORY_EULER_FUSION_20260814.md`.

### Theorem 1.1 (finite coalesced-port certificate)

The CSP is feasible. Its selected \(16{,}795\) options form an
area-increasing arborescence rooted at the mountain. Every row uses one global
traversal orientation. Distinct altered ports are cyclically separated by at
least one untouched position.

Consequently all \(16{,}796\) depth-three source circuits serialize into one
cyclic source word with zero added positions, preserving the complete
occurrence-labelled literal deck through width four.

## 2. Exact CSP semantics

These are the exact semantics of the **frozen equality-only submodel**, not a
claim that equality of forced signatures is necessary for common-history
fusion. The authoritative exact gate also permits nonidentical forced
signatures whose multiway forced union lies in the maximal intersection.

Let \(x_o\) be the Boolean selecting option \(o\), let \(z_v\) be the one
orientation Boolean of row \(v\), and let \(y_{v,a}\) say that start \(a\) is
used at \(v\). The solver imposes:

1. \(\sum_{o:\,\operatorname{child}(o)=u}x_o=1\) for every nonroot row
   \(u\);
2. \(x_o=1\) implies both recorded endpoint orientations equal the
   corresponding \(z_v\);
3. \(y_{v,a}=\max\{x_o:o\text{ is incident with }v\text{ at }a\}\); and
4. for every cyclic window of starts
   \(\{r,r+1,\ldots,r+d\}\), at most one of its \(y\)-variables is one.

Clause 4 is exactly pairwise cyclic distance at least \(d+1\), not merely a
one-way relaxation. Two distinct starts lie in some cyclic window of \(d+1\)
consecutive starts if and only if their minimum cyclic distance is at most
\(d\). Repeated incidences at the same start share one \(y_{v,a}\), which is
the intended coalescence rather than a capacity violation.

Every option changes an earlier zero to one and a later one to zero in one of
the four packets at a highest valley. It therefore strictly increases Dyck
area. The selected graph gives every nonmountain row exactly one outgoing
parent. Strict area increase rules out directed cycles; the mountain is the
unique row of maximum area and is the only row without a parent option.
Hence all selected paths terminate there, and the \(16{,}795\) choices form
the asserted arborescence.

## 3. Exact replay statistics

The independently replayed certificate has

\[
\begin{array}{c|rrrrr}
\text{children}&0&1&2&3&4\\ \hline
\text{rows}&5627&6229&4261&672&7,
\end{array}
\]

and

\[
\begin{array}{c|rrrr}
\text{distinct ports used}&1&2&3&4\\ \hline
\text{rows}&8565&7103&1100&28.
\end{array}
\]

The raw separated-port capacity is

\[
 \left\lfloor\frac{21}{4}\right\rfloor=5,
\]

so every selected row is within capacity. Exactly \(5{,}695\) rows reuse at
least one selected port; maximum incidence multiplicity at one port is three.
Thus coalescence is materially used by the solution.

The chosen orientation is the reversed canonical orientation at all rows in
this solver representative. Globally reversing every component traversal
gives the equivalent all-forward solution with the corresponding reversed
cyclic starts.

## 4. Independent verification and provenance

The checked repository sources are:

- `scratch/dump_msw_highest_valley_port_csp.cpp`, the catalogue generator;
- `scratch/solve_msw_highest_valley_port_csp.py`, the CP-SAT encoder; and
- `scratch/verify_msw_highest_valley_port_solution.py`, the small replay.

The successful solve used an earlier generator byte-string whose only
semantic difference from the checked repository generator is that it always
emits both orientations. The checked generator has an optional final
`canonical` flag but, with no such flag, H100 regenerated a byte-identical CSP
instance. The successful solve used an earlier solver byte-string whose only
later repository change avoids reading Boolean values when CP-SAT returns no
solution; that change does not affect this `OPTIMAL` run. Both exact run-source
hashes and current checked-source hashes are frozen below.

The hostile replay
`scratch/audit_msw_m10_d3_coalesced_port_certificate_20260814.py` does not trust
option legality from the generator. It independently reconstructs all Dyck
roots, MSW tight orders, both orientations, forced-history signatures, every
highest-valley four-packet parent, and Dyck area. It then checks every one of
the \(417{,}208\) catalogue records and every selected record before checking
the tree, orientations, port separation, coalescence statistics, and
histograms.

All compilation, enumeration, solving, replay, regeneration, comparison, and
hashing ran through SSH on H100. The successful independent replay printed

```text
PASS m=10 d=3 n=21 vertices=16796 catalogue_options=417208 selected=16795 root=0 oriented0=0 oriented1=16796 reused_vertices=5695 maximum_reuse=3 maximum_distinct_ports=4
catalogue_packet_hist {'001': 63016, '0011': 16628, '01': 274548, '011': 63016}
selected_packet_hist {'001': 329, '0011': 598, '01': 15403, '011': 465}
child_hist {0: 5627, 1: 6229, 2: 4261, 3: 672, 4: 7}
distinct_port_hist {1: 8565, 2: 7103, 3: 1100, 4: 28}
```

## 5. Frozen H100 SHA-256 ledger

The successful computational artifacts and exact checked-source hashes are:

| artifact | SHA-256 |
|---|---|
| exact successful-run generator | `58fb5526a3e37404a64656ad0cfa75c28be91baf8807c81169b8d60fac79d148` |
| exact successful-run solver | `c6016cbebb8898c27e4a8c07c1eddd5b35572626e5d71ebb199deabffaa01216` |
| small replay verifier | `b6244e10887aee1cf9ec8d674ded2bdffd061312f7168734e07b52a67f203252` |
| CSP instance | `6d06e8ac4ae2fd0c1d9a89d3d6a4271084cdbc104fcf26de0e4bfb7676dff68d` |
| selected solution | `be6fcd8ae00a5097ce0701ae9a68c9617df3c890cdc9922cc68699ede330803e` |
| small replay output | `af38f50c829a93b60623e05734ffb40e126600d4f6dc6f07e727ebc4ac3617d5` |
| checked repository generator | `84aa2e6fe52fadc1a5fd9df41ee7a02874b3894059500d78a6c6c19d0be40306` |
| checked repository solver | `e4815e2f2712197ee2a88211996a7b917fecd48a58ca6c54657816c38ba02e20` |
| hostile replay | `a254cb9aa23a30b8e370ae8717b41efa56c352f6c1bae62a99099d7a4a43c9ae` |
| hostile replay output | `89f3ba684a71f2b5425ef50a7337a9a4eab89e6521886a4f5728827cde5c9166` |

## 6. Scope

The certificate does not prove a coalesced-port selection for arbitrary
\((m,d)\), preserve source intervals longer than \(d+1\), repair the explicit
canonical upper-portal hole, or supply a linear opening cap. It closes the
exact finite simultaneous source gate at the first monotone threshold
\(m=3d+1=10\).
