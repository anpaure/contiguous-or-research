# Fixed-root prescribed-parent sector ports: complete diagnostic

Date: 2026-09-09. Status: one reviewed, bounded h100 execution completed.

The fixed-root entrance construction is valid separately at every one of
the 4,862 bit0 ports of the verified optimal19 period. Its prescribed first
11-state map is not injective: there are 375 pairs of ports with the same
first11 state. Consequently all these prescribed entrances cannot be used
simultaneously with distinct child owners. This is a failure of the
specified simultaneous entrance assignment, not an obstruction to other
deletions, other port subsets, or dimension21 existence.

## Exact scope and formula

The input is `answers/k19_optimal92381.word`, SHA-256
`1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414`.
Its checked period C has length 92,378, and the full word is C+C[:3].
Set R_i=C_i OR C_(i+1) OR C_(i+2), and let U_i also include C_(i+3),
with all indices cyclic. The checker re-established the complete distinct
rank9 and rank10 decks, U_i=Phi(R_i), the strict Johnson successor, and
the parent's residence-three property. This is not another full-cube
verification.

At every index i whose inserted coordinate is bit0, let u=bit0,
d=R_i minus R_(i+1), and e=R_(i+1) minus R_(i+2). With new bits a=bit19
and b=bit20, the prescribed four-state entrance is

    R_i+a,
    U_i,
    R_(i+1)+b,
    (R_(i+1) intersect R_(i+2))+a+b.

The three inserted coordinates are u,b,a and the deletions are a,d,e.
The checker evaluated all three actual child Phi updates and deletion
ages using the actual preceding parent states with the new10 block held
fixed. Thus the parent-age domination required by Section7 of the
[excursion proof](CANONICAL_PHI_BALANCED_BLOCK_BARRIER_AND_MINIMAL_RUN_SECTOR_EXCURSION_20260909.md)
was tested literally. All deletion ages had certified lower bound four,
using an age counter capped at q+1=4. Their exact possibly larger ages
are not claimed.

## Complete counts

| Quantity | Exact result |
|---|---:|
| Fixed bit0-root ports | 4,862 |
| Distinct00 states | 4,862 |
| Distinct01 states | 4,862 |
| Distinct first11 states | 4,487 |
| First11 states with one provider | 4,112 |
| First11 states with two providers | 375 |
| Ports belonging to collision pairs | 750 |
| Repeated first11 occurrence excess | 375 |
| Maximum first11 multiplicity | 2 |

For example, the zero-based parent indices 3,763 and 42,017 both have
first11 old facet 4,511 and child state 1,577,375. The full report includes
every port and every collision group, not only this example.

The source certifies that the 00 and 01 maps are injective; these facts
also follow from the general Phi and parent-permutation proof. The first11
collision is exactly the remaining facet obstruction in the prescribed
entrance formula. No later buffer walk was evaluated, so this report does
not state whether all noncolliding entrances can subsequently coexist.

## Execution and provenance

The root, frontier, and structure agents independently read the prepared
source and passed it before execution. These are internal reviews, not
external formal certification. Root authorized exactly one execution on
h100/arboghast, with CPU30 seconds, wall45 seconds, address space1GiB and
individual file size128MiB. The script enforces these caps, and an external
`timeout 45s` also bounded the command. The one execution returned exit0,
`PASS_FIXED_PORT_DIAGNOSTIC`, with every interface check true. Measured
CPU time was 0.33715706 seconds; wall time was 0.3375362982042134 seconds.

No retries, changed deletion choices, alternate roots, subset search,
optimization, word modifications, or dimension21 construction occurred.
No mathematical process remains live.

Prepared source:
`scratch/audit_k19_fixed_root_prescribed_parent_sector_ports_20260909.py`.
Executed source SHA-256:
`c8bdcd0161aaa3f7ce676636223de8f37f1d8b3f4fb72afa0ad0c42dfe7f832e`.

Full copied artifacts are in
`scratch/k19_fixed_root_parent_sector_ports_20260909/`:

- `checker.py`: exact executed source;
- `run_started.json`: source hash and declared resource caps;
- `run.log`: exact standard-output summary;
- `fixed_root_parent_sector_port_certificate.json`: complete checks/counts;
- `all_prescribed_parent_ports.json`: all 4,862 entrance records;
- `all_first11_collision_groups.json`: all 375 collision pairs;
- `execution_provenance.md`: exact execution command and copy record.

Remote work directory:
`/home/amodo/exact-b-k19-fixed-root-sector-ports-20260909/`.

