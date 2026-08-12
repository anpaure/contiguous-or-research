# Separated port permutations: an exact global repair master

Date: 2026-07-30
Status: proved reduction, executable exact `q<=3` master, authenticated
length-eight regression, an exact fractional `104`-cut floor, and a
machine-checked binary `105`-cut floor.  No
93-hole repair and no optimal `k=16` word is claimed here.

## 1. Motivation

Bounded port-cycle enumeration on the repaired asymmetric `k=16` carrier has
now established a sharp locality transition:

```text
no q1-safe positive cycle through length 7;
one full Z15 orbit of length-8 cycles gives a real 15-hole descent;
no all-depth-safe single cycle through length 9 on the new factor.
```

Continuing one length at a time is unnecessary.  Every collection of port
cycles is simply a permutation of the cut-edge heads.  Under a separation
condition, residence and bounded-depth shadows are local at each new seam,
so all cycle lengths can be searched simultaneously by one assignment model.

## 2. Port-permutation normal form

Let `F` be an oriented spanning two-factor of `J(k,r)`.  Index its directed
edges by `I`; write edge `i` as

\[
                         e_i=(u_i,v_i).
\]

The tails `(u_i)` and heads `(v_i)` both enumerate the middle vertices once.
For a permutation `pi` of `I`, replace the old successor edges by

\[
                         u_i v_{\pi(i)}.       \tag{2.1}
\]

Whenever all edges in (2.1) are Johnson edges and no selected edge is paired
with its reverse (so every resulting directed cycle has length at least
three), (2.1) is again a physical spanning
two-factor.  Conversely, every rethread using only the old tails and old
heads has this form.  The nonfixed indices

\[
                         C=\{i:\pi(i)\ne i\}
\]

are its cuts, and the nontrivial cycles of `pi` are exactly the
port-permutation cycles used in the finite censuses.

Thus a global master uses Booleans `x_(i,j)` for every allowed seam
`u_i -> v_j` (including `x_(i,i)` for the old edge) and the assignment rows

\[
 \sum_jx_{ij}=1\quad(i\in I),\qquad
 \sum_ix_{ij}=1\quad(j\in I).                 \tag{2.2}
\]

## 3. The separation theorem

Assume `F` has minimum positive coordinate-run length `d+1`.  Two cut indices
on one source component have cyclic cut distance equal to the number of
source transitions between their positions.  Call `C` **d-separated** if
distinct cuts on every source component have cyclic distance greater than
`d`.

At a proposed seam `u_i -> v_j`, retain the `d` unchanged source transitions
immediately before `u_i` and the `d` unchanged target-segment transitions
immediately after `v_j`.  Call the seam **d-collar-safe** if the concatenated
collar has no coordinate run of length at most `d`.  Equivalently, for every
insertion edge at or before the seam and every later deletion edge at or
after it whose transition distance is at most `d`, the inserted and deleted
coordinates differ.  There are `d` comparisons between an inherited
insertion and the seam deletion, `d` between the seam insertion and an
inherited deletion, and `d(d-1)/2` genuinely cross-collar comparisons.
Thus this is a finite family of

\[
                 2d+\frac{d(d-1)}2=\frac{d(d+3)}2
\]

comparisons.  At `d=3` there are exactly nine, which is the collar test in
the authenticated C++ seam census.

### Theorem 3.1 (global residence from separated local collars)

If `C` is d-separated and every selected nonold seam is d-collar-safe, then
the port-permuted factor has minimum positive run length at least `d+1`.

#### Proof

Cutting the source cycles at `C` produces directed source segments.  Because
the cuts are d-separated, every segment has more than `d` transitions between
its boundary seams.  Rethreading permutes whole segments; it does not change
their interiors.

Suppose a new coordinate run had length at most `d`.  It cannot lie wholly
inside a source segment, since the source factor was resident.  It therefore
crosses a new seam.  Its length bound and the segment-length bound imply that
it crosses exactly one seam.  Hence the whole run lies in that seam's retained
`d`-transition collar, contradicting d-collar safety.  QED.

### Theorem 3.2 (exact bounded-shadow additivity)

For every `1<=q<=d`, each window of `q+1` carrier states crosses at most one
selected seam.  Consequently the final fixed-depth lower and upper load of a
mask `S` is exactly

\[
 \mu'_q(S)=\mu_q(S)
       -\sum_i c_iD_{i,q}(S)
       +\sum_i\sum_{j\ne i}x_{ij}A_{ij,q}(S), \qquad
 c_i=1-x_{ii},                                 \tag{3.1}
\]

where `D_(i,q)` is the occurrence-labelled list of old q-windows destroyed by
cut `i`, and `A_(i,j,q)` is the list of new q-windows crossing seam `(i,j)`.

Equivalently, put

\[
 K_{ii,q}=0,\qquad K_{ij,q}=A_{ij,q}-D_{i,q}\quad(j\ne i). \tag{3.2}
\]

Then

\[
                 \mu'_q=\mu_q+\sum_{i,j}x_{ij}K_{ij,q}.     \tag{3.3}
\]

The diagonal convention is essential: an old choice `x_(i,i)=1` is not a
new seam.  Formula (3.1) would be false for the identity permutation if an
`A_(i,i)` term were included.

#### Proof

The separation bound gives at most one cut in a q-window.  Every unaffected
window is unchanged.  Every affected old window is assigned to its unique
cut, and every new window to its unique seam.  Therefore no occurrence is
double-subtracted or double-added, proving (3.1).  QED.

This theorem is occurrence-level: repeated masks retain their multiplicity.
Thus the exact cover rows are simply `mu'_q(S)>=1`, not a heuristic set union.

## 4. The exact finite `k=16` master

Use the full length-eight-orbit factor

```text
scratch/k16_asymmetric_len8_orbit_repair_20260730.json
SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204
```

as source.  Its authenticated `d=3` seam graph contains

```text
12,870 old choices,
211,604 nonold directed seams,
5,425 seams providing at least one residual lower-q2 or upper-q3 mask.
```

The global model consists of:

1. the assignment equations (2.2);
2. `c_i = 1-x_(i,i)` and pairwise cut-separation rows on every source cycle;
3. the exact physical no-two-cycle rows (a directed carrier two-cycle would
   duplicate one undirected Johnson edge rather than form a simple 2-factor);
4. every literal lower-q1 and upper-q1 cover row from (3.1);
5. every fixed lower/upper q2 and q3 cover row from (3.1), including the 93
   residual masks (the 48 arbitrary rank-11 holes are also exactly the 48
   fixed upper-q3 holes);
6. optionally an edit budget or objective minimizing the number of nonold
   seams.

The executable defaults the total-cut upper bound to `W`; hence the exact
master itself has no artificial edit-radius or port-cycle-length bound.
Smaller `--radius-max` values are explicitly scoped experiments, not verdicts
about the full separated class.

Only upper width four is used in item 5.  A previous implementation draft
also inserted width-five terms while retaining only four-separated cuts.
That was incorrect: a width-five window can contain two cuts at source
distance four, so its losses and gains are not seam-additive.  Width five and
every longer window are handled exclusively by the physical replay in
Section 5.

The full length-eight orbit repair is the fixed-assignment regression witness
for the same port-permutation equations built on its preceding
triangle-repaired source.  It is a 15-hole descent, not a complete repair of
that source.  Therefore an implementation must reconstruct its exact
successor map and reproduce its signed `q<=3` hole profile before being used
on the 93-hole source.

In item 3, “two-cycle” is physical.  If `u_i -> v_j` is selected, its reverse
is the unique allowed seam `v_j -> u_i`, located through the tail index of
`v_j` and the head index of `u_i`.  It is not generically `x_(j,i)`.  In
particular, a transposition of two head indices can be a valid port trade and
must not be forbidden merely because it is a two-cycle of the permutation.
Assignment plus the physical no-two-cycle rows gives a simple spanning
two-factor; it does not impose connectivity, Hamiltonicity or voltage.

The model searches arbitrary products of port cycles; it has no cycle-length
bound.  It strictly contains every separated length-`L` census for every `L`.

### Exact provider floor

Every admissible seam hits at most two of the 93 zero-baseline defects.  Make
a graph on those defects, joining two targets when one seam hits both.  The
exact catalogue has 119 distinct edges and 18 isolated vertices.  Hence a
matching has size at most `(93-18)/2=37`; an explicit 37-edge matching attains
the bound.  Because every remaining target has a singleton provider, the
minimum provider-only seam cover is exactly

\[
                            93-37=56.             \tag{4.1}
\]

This proves `cut_count>=56` before assignment, separation, q1, survivor or
residence constraints are imposed.  The executable also inserts the
redundant exact aggregate rows

```text
selected lower-provider seams >= 45,
upper service multiplicity       >= 48,
selected hitful seams            >= 56,
selected zero-hit seams          >= 17,
provider service slots           >= 93,
weighted defect service          >= 1899,
weighted defect service          <= 20 * cut_count,
cut_count                        >= 105.
```

The zero-hit row comes from a stronger solver-free port theorem.  In the
directed graph of the 5,425 provider seams, only 75 arcs lie in nontrivial
strong components; those cycle-eligible arcs can service only 45 of the 93
defects.  More sharply, remove the `z` selected zero-hit seams from a balanced
port permutation.  What remains is at most `z` directed provider paths plus
provider cycles.  Exact topological dynamic programming on the condensation
DAG enumerates all 2,506 attainable distinct-target masks in a relaxation
that gives SCC interiors for free and permits different paths to overlap.
Among the 48 cycle-unserviceable defects is an explicit 33-element set `S`
such that every attainable path mask meets `S` in at most two members.
Assigning weight one half to each member of `S` is therefore an exact rational
cover dual: total demand is `33/2`, while every provider path has capacity at
most one.  Thus `z>=ceil(33/2)=17`,
and every repair has at least

\[
                              56+17=73.              \tag{4.2}
\]

cuts.  This is already a theorem at the balanced-port plus 93-demand layer,
before separation, reverse-edge, q1 or survivor rows are imposed.
An exact integer set-cover replay finds a 17-mask cover in this permissive
path universe.  Improving (4.2) therefore requires coupling path service to
provider cost, vertex-disjointness, physical connectors, or another omitted
global constraint.

The missing coupling has an exact integer potential certificate.  Give the
seven defect phase blocks weights

```text
11, 22, 36, 19, 18, 16, 23
```

whose total over all 93 physical targets is `1899`.  There is an integer
potential `phi` on all 12,870 ports, with `0<=phi<=20`, such that every one
of the 5,425 provider seams `u->v` satisfies

\[
          \operatorname{weight}(\operatorname{hits}(u,v))
             \le 20+\phi(v)-\phi(u).               \tag{4.3}
\]

On a selected provider cycle the potential telescopes to zero.  On a
selected provider path it contributes at most 20.  Deleting `z`
nonproviders from the selected port cycles leaves at most `z` provider
paths.  Thus a selection with `p` providers satisfies

\[
  1899\le\text{weighted service}\le20(p+z)=20\,\text{cut_count}.
\]

Consequently every repair in this source-relative class has

\[
                         \text{cut_count}\ge\lceil1899/20\rceil=95. \tag{4.4}
\]

This solver-independent scalar floor subsumes (4.1)--(4.2).  The split rows
remain in the executable because they are useful propagation constraints.

The equality case of (4.4) is impossible.  Define the nonnegative integer
reduced cost of every physical seam `e:u->v` by

\[
 \rho(e)=20+\phi(v)-\phi(u)-\operatorname{weight}(\operatorname{hits}(e)),
                                                        \tag{4.5}
\]

using zero hit weight for a nonprovider.  Summing (4.5) around the selected
port cycles cancels all potentials.  If exactly 95 seams were selected, then

\[
 1900=\text{gained weighted service}+\sum_e\rho(e).
\]

All target weights are at least 11, so no target can be served twice.  Every
target is therefore served exactly once and the total reduced cost is one.
In particular every selected seam has `rho<=1`.

The complete `rho<=1` graph has 3,558 arcs and fifteen nontrivial SCCs, all
of size five.  Only 90 arcs lie on a directed cycle, including only 60
providers.  Those 60 providers miss 63 required defects; target `33337`
alone is a singleton Hall witness.  Since every selected seam in a port
permutation lies on a selected directed cycle, a 95-seam assignment is
impossible.  Consequently the intermediate source-relative floor is

\[
                         \text{cut_count}\ge96.          \tag{4.6}
\]

The equality-face argument is not the final floor.  Three distinguished
weight-23 targets are

```text
46811, 56173, 60854.
```

No seam hits two of them.  Give each catalogue seam its reduced cost `rho`
from (4.5).  Exact shortest-path replay in the complete directed seam graph
gives minimum closed-walk costs 17 for a specified singleton, 39 for a
specified pair and 55 for the triple.  The three required provider
occurrences are partitioned among selected port cycles, so every possible
partition costs at least

```text
17 + 17 + 17 = 51,   39 + 17 = 56,   or   55.
```

Thus every feasible selected permutation has total reduced cost `R>=51`.
On the other hand, telescoping (4.5) around all selected cycles and using
weighted service at least 1899 gives `R<=20C-1899`.  Therefore
`51<=20C-1899`, and another intermediate source-relative floor is

\[
                         \boxed{\text{cut_count}\ge98}.   \tag{4.7}
\]

The shortest-path calculation is deliberately permissive: return paths may
repeat vertices and different distinguished cycles may overlap.  Hence its
51-unit cost is a valid lower bound for physical vertex-disjoint selected
cycles.  This argument is solver-independent and supersedes the floors
95--97.

The final scalar dual is considerably simpler.  There are positive integer
weights `b_t in {1,2,4}` on all 93 defects, of total 207, and an integer
potential `y_v in {-4,-3,-2,-1,0,1,2}` on the ports such that every seam
`e:u->v` satisfies

\[
                 b(H(e))\le2+y_v-y_u.                 \tag{4.8}
\]

Exact integer replay verifies (4.8) on all 211,604 seams.  Summing around a
balanced selected seam circulation cancels `y`; servicing every target gives
`2C>=207`, and hence the solver-independent fractional floor

\[
                         C\ge104.                       \tag{4.9}
\]

An exact denominator-four primal circulation of value `207/2=103.5` proves
that this fractional dual is tight.

At equality `C=104`, exact telescoping leaves only two integer cases:

1. every target is serviced once and total dual slack is one;
2. one price-one target is serviced twice, all others once, and total slack
   is zero.

Both cases are infeasible even after physical port capacity is omitted.
Deterministically emitted CNFs and independently checked compact DRAT proofs
certify the two UNSAT statements.  Therefore the current canonical
source-relative binary floor is

\[
                         \boxed{C\ge105}.               \tag{4.10}
\]

Equation (4.9) is an unconditional exact rational dual certificate.  The
one-step improvement (4.10) is a machine-checked finite theorem for binary
endpoint-balanced seam selections; it still omits separation, reverse-edge,
q1, survivor, residence and deeper-shadow rows.

The dependency-free certificate chain is

```text
scratch/k16_defect_provider_edge_cover_20260730.audit.json
SHA-256 7e0d51edfa2c933eea20808e43ea1445672cfe25e60f68afe3ed11e05c56ed27

MATH_THEOREM_K16_PROVIDER_PORT_CYCLE_FLOOR57_20260730.md

scratch/k16_defect_service_structure_v4_20260730.audit.json
SHA-256 91d70c1efdf4bd062b20838a467159602bf1ef3e244cf208f38ab5caa81fd2b3

MATH_THEOREM_K16_PROVIDER_PATH_CAPACITY_FLOOR66_20260730.md
SHA-256 08b21042d785e64d766bf1a03b85a0112b0d2875695658a05900cd2d65bdbcc8

scratch/k16_defect_service_structure_floor66_20260730.audit.json
SHA-256 31314bc077f81fc311b58d3aba483a0a06a77d2d05a4d4d424db606db3e0c4c8

MATH_THEOREM_K16_PROVIDER_PATH_MASK_COVER_FLOOR70_20260730.md
SHA-256 80406b29ab59afe42a31607fb01e304bb815a3b29a137b4fc404c67fd28f09ec

scratch/k16_defect_service_structure_floor70_20260730.audit.json
SHA-256 411fb4b3423ef12ae2865b141f85186d8f02346709822b01633a3cdd440f8290

scratch/audit_k16_defect_service_structure_20260730.py
SHA-256 c4b32c1009296c17672634d410bcdbc0d66a073c78e14452b49d6571d92791e9

scratch/k16_defect_service_structure_floor70_20260730.resource.txt
SHA-256 d812ce5449da51d8710cb5a170cbcc75a0f3a38e849d26addf9e67242d7a20c7

MATH_THEOREM_K16_PROVIDER_PATH_DUAL_FLOOR73_20260730.md
SHA-256 042beb816e938b99952651ee5737835e74b93a51112676c9adfb996a6c536862

scratch/k16_provider_path_dual_floor73_20260730.audit.json
SHA-256 38aa93ee5a737c9aeed30b9d23ba89c282774e5440a0d6d06dd2fa26a581ac4d

scratch/audit_k16_provider_path_dual_floor73_20260730.py
SHA-256 eb2c6e9e2851a70eb9ab032fb7809e0d9ef1fdbdfd8a400d8505294a7ac8fee9

scratch/k16_provider_path_dual_floor73_20260730.resource.txt
SHA-256 ff577624d6ca91f14ec2dbbcfeefb027e744e454e409361e6e535251fae7b0dc

MATH_THEOREM_K16_PROVIDER_WEIGHT_POTENTIAL_FLOOR95_20260730.md
SHA-256 3ccdc4175c1c1bbb2e5f0f7ea720be535c02643f6ab53b3eb2054e1de6451f48

scratch/k16_provider_weight_potential_floor95_20260730.audit.json
SHA-256 7d64defc48cdacbde21aeab3757d051bc2a63623f263d110eb5922749db44e56

scratch/audit_k16_provider_weight_potential_floor95_20260730.py
SHA-256 294893b2c3bf678c4f1c67b7615e1230a0510720347df273e4a21c4d4f95fed6

scratch/k16_provider_weight_potential_floor95_20260730.resource.txt
SHA-256 3cc55f33415009028fbcf7da035cce4552122971e6c8910746aa014c57d289da

scratch/k16_provider_weight_potential_floor95_20260730.stdout.txt
SHA-256 5e450e3116f9d3cf27d29e09da1f7b64b35f00f2d6d02e3def83ca00f2c3763b

MATH_THEOREM_K16_PROVIDER_WEIGHT_POTENTIAL_FLOOR96_20260730.md
SHA-256 221224e9232859fa73ae0e359e121e4fb7c867c281751787ed4dceb666350a7e

scratch/audit_ad_k16_provider_weight_potential_floor95_independent_20260730.cpp
SHA-256 26a2af36e42df7078ef5e9297c9b8ebc10738542b8e54ea843397bac2533d144

scratch/k16_provider_weight_potential_floor96_independent_final_20260730.audit.json
SHA-256 a57e445f266ff88287429712d7701ab70a2957d61de6008ef21a7048c0192a3d

scratch/k16_provider_weight_potential_floor96_independent_final_20260730.resource.txt
SHA-256 08d78a9890f04b49cbe9429813ae23b5934c7a3169ae6cad4ab5f34c2203651a

MATH_THEOREM_K16_SPECIAL_CYCLE_COST_FLOOR98_20260730.md
SHA-256 872fbe2de3d3c67fc921464b5531341c945928ba40d1a9d7efd21cccbaf49ba4

scratch/k16_exact96_special_cycle_cost_20260730.audit.json
SHA-256 3cf4a5156439c79a950427ca98349b3ec0ef452489bc69637e44a294299c9a9e

scratch/audit_k16_exact96_special_cycle_cost_20260730.py
SHA-256 154036ed7aed97e86fd1ead9eb6d555e5d2ac4483201a2673aec57370ccaf861

scratch/k16_exact96_special_cycle_cost_20260730.resource.txt
SHA-256 c9baf10ab33f57116a1b9d1bf701add0206260401b05f2f8c283fbb1a11001ae

scratch/k16_floor97_target_cycle_cost_independent_20260730.audit.json
SHA-256 9dca9e7085a583e85de918361a0ebca17ed7a0c63b10c60f0c125c197126744e

MATH_THEOREM_K16_DIRECT_DUAL_AND_EQUALITY_FLOOR105_20260730.md
SHA-256 c10b3bd2c7844f34cee262f254bdb11627e7211bf51e7b708b68d5d8bd7d2017

scratch/k16_floor105_proof_bundle_20260730.manifest.json
SHA-256 05aacd9f090cc5e09905bdd694bc195eacf2b01dec945fe67ff804e186509b37

scratch/k16_direct_cut_dual_scale2_floor104_20260730.audit.json
SHA-256 a89f9166a1f6eade1db20ea3b76d15aad2187eac48e23e0566b6968972b18bb2

scratch/k16_floor104_scaled_primal_D4_independent_20260730.audit.json
SHA-256 ce286af2cfc56732bc57a4621e808b49d83f3e3c9cb0959b8a6da19860d84ae0

scratch/k16_floor104_no_repeat_drat_bundle_20260730.audit.json
SHA-256 c60888ce8123d09ca5c07563e105bbd3aecdc87efc6395e5a15267862deb3119

scratch/k16_floor104_repeat_weight1_drat_bundle_20260730.audit.json
SHA-256 396b42079d0672fa89b13f0afd5341f7bcbfd7bd08807dff5ba0f647e200f15b
```

## 5. Deeper shadows: fail-closed CEGAR boundary

Theorems 3.1--3.2 are exact only through `q=d`.  Longer windows can cross
multiple seams, so their arbitrary upper unions and deeper fixed lower
intersections are not additive seam by seam.  The length-nine counterexample
shows that ignoring this boundary is unsound: a q1/lower-q2/upper-q3-safe
packing repairs seven rank-11 masks but creates fourteen rank-10 and seven
lower-q3 holes.

Accordingly every SAT assignment must be physically materialized and audited
over

```text
all fixed lower depths,
all arbitrary-width upper unions,
all cyclic positive runs,
all middle owners and Johnson edges.
```

If a deeper target is missing, add a sound CEGAR row.  The weakest always-
sound row blocks the complete selected port permutation.  Stronger witness
rows may express that at least one old witness interval survives or one new
multi-seam witness is selected, but they must be derived occurrencewise; no
independence assumption is allowed.

A `PASS` exists only after independent literal replay.  `UNSAT` has scope
only inside the d-separated port-permutation class and requires a checked SAT
proof.  Resource exhaustion is `UNKNOWN`.

## 6. Authenticated executable regression

The driver

```text
scratch/solve_k16_len8_physical_93_multicut_cegar_20260730.py
```

was run on the H100 CPU under a 1 GiB address-space cap in fixed-assignment
regression mode.  It rebuilt the `211332` admissible seams of the
triangle-repaired source, selected the known fifteen length-eight port cycles
(`120` distinct cuts), and returned

```text
PASS_LENGTH8_REGRESSION
```

The regression verifies, independently of CP-SAT:

* the selected ports are a permutation and are four-separated;
* every selected seam belongs to the collar-safe Johnson catalogue;
* the final directed edge set has no reverse-edge pair;
* the signed additive loads agree mask-for-mask with physical replay at all
  six lower/upper families through `q=3`;
* the physical successor map exactly equals frozen factor SHA-256
  `6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204`;
* the final signed profile is `0,0,45,0,0,48` holes at
  lower/upper `q=1,2,3`, exactly as audited.

Frozen evidence:

```text
scratch/k16_separated_port_master_length8_regression_20260730.audit.json
SHA-256 8611e8700845a3e25c827cd9a33225b7af50a3d6036e9e4aadb90cfdd81fad27

scratch/k16_separated_port_master_length8_regression_20260730.resource.txt
SHA-256 09c3d973e6e97f744bc724addbefe787ddd020e053ff6e552598b09dce6f4f1d
```

An independently implemented C++ binary ledger then compared all `12,870`
source records, all six baseline arrays, every source occurrence-loss row,
and all six occurrence-gain rows for every one of the `211,604` current-source
seams.  It also independently counted the physical reverse-edge rows.  The
result was

```text
PASS_FULL_211604_SEAM_CROSSCHECK
new/new reverse rows = 26,233
old/new reverse rows = 0
```

See

```text
MATH_AUDIT_K16_GLOBAL_PORT_MASTER_20260730.md
SHA-256 49f65ab78467d8bb1bc25fa2c087dc38380d3b48edef99412c6f54e0c62af738

scratch/k16_global_port_master_binary_crosscheck_20260730.audit.json
SHA-256 5608c32fa349ca78d3ccf5a956d6077bc13350be6d4e1f9b6125c9fb125b1d54
```

The current unrestricted build (default cut cap `W=12870`, including the
machine-checked floor-105 row and weighted-service rows) has `224475` variables, `112484`
constraints, and a 55 MiB text serialization.  Its frozen driver is

```text
scratch/solve_k16_len8_physical_93_multicut_cegar_20260730.py
SHA-256 1f6bdb8f1addce0ced7442d13b04e7beb574ed4d1b7857966cee230186cf3308

scratch/k16_separated_port_master_floor105_regression_20260730.audit.json
SHA-256 926ce0e049877a5d5ba25e8b9ce9bc590548717e5e0c1a4d81319710da1aad01

scratch/k16_separated_port_master_floor105_build_20260730.audit.json
SHA-256 38039a504a4d5b9fc598f276e8ab0e4e0bf89048220e6eb2aa022bb8c5d69e24

scratch/k16_separated_port_master_floor105_checkpoint_20260730.audit.json
SHA-256 76a9843319a48db0f9f5a5b9756fae084a0b86aa31086d5e5a7972d65b9caf97
```

The build peaked below `588` MiB RSS on the H100.  A first deliberately
capped `256`-cut CP-SAT smoke returned `UNKNOWN` after 300 seconds without
an incumbent.  This is a search-performance datum only, not evidence for
infeasibility.

Before the potential certificate was found, the frozen full signed-`q<=3`
model returned `INFEASIBLE` at every exact cut count from `70` through
`85`.  A sparse exact-93 probe returned `UNKNOWN` after 360 seconds.  Both
experiments are now subsumed: (4.9) excludes every exact count below 104 by
an exact dual certificate, while (4.10) machine-checks the equality-104
exclusion.  The constructive frontier is therefore exact count 105 and
above.  Any `SAT` assignment still requires the complete physical
replay of Section 5.

Before the 98-floor was known, exact count 96 on the full frozen signed-`q<=3`
master, returned `INFEASIBLE` in 161.7 seconds (`562064` branches, `144`
conflicts).  This remains a trusted CP-SAT audit inside the source-relative
master, but its numerical conclusion is now strictly subsumed by (4.7).

A much weaker continuous relaxation of the same exact-96 face is already
infeasible: even after dropping seam upper bounds, separation, reverse-edge,
q1, survivor, residence and every deeper row, the nonnegative seam cone with
port balance, exact one-time service of all 93 defects, and total reduced cost
21 is infeasible.  This is useful localization of the old CP-SAT result, but
the special-cycle theorem is the cleaner exact certificate.  No exact-97 job
was launched.

```text
scratch/k16_separated_port_master_exact96_20260730.audit.json
SHA-256 5c313a0fc2b27b2c59e0cce43d6aa17424ec79d56cd8cada07752290707f92e4

scratch/k16_separated_port_master_exact96_20260730.resource.txt
SHA-256 ddcf82e47a192d35365109a7b466001573f69306c25edb9dcce6017d4b51554f

scratch/k16_exact96_no_repeat_port_cycle_cone_20260730.audit.json
SHA-256 9d00dd12bc05decc01a35690aa7edb411615ab7bd31d477d8cdde6934f289928

scratch/k16_exact96_no_repeat_port_cycle_cone_20260730.resource.txt
SHA-256 1f2305b69e745ffad9dff804974e7bf78ec50f16278210577f87a68d82932c6e
```

At the new constructive frontier, an exact reduced count-105 model retained
only dual-slack-at-most-three arcs, removed arcs outside cyclic SCCs, and
imposed binary endpoint balance, service of all 93 defects, physical port
capacity and the scale-two accounting identity.  It had 179,113 eligible
arcs and returned `UNKNOWN` after 300 seconds (`479183` branches, `385`
conflicts).  This is neither a witness nor an infeasibility result.  The exact
identity `repeat weight + dual slack = 3` gives six aggregate branches; their
LP and integer prescreens are the next reduced search.  No full count-105
physical-master solve is justified until a reduced witness is independently
replayed.

```text
scratch/k16_floor105_reduced_capacity_20260730.audit.json
SHA-256 fec7b3ee864d8a698785b47510d30a0f1eef4636c103bdc0da305eaed6cbec0c

scratch/k16_floor105_reduced_capacity_20260730.resource.txt
SHA-256 782a0cb0e4090a5c4f8886d60890165362d4eb480d23abb5685e33fcbd9085aa

scratch/solve_k16_direct_floor105_reduced_aggregate_20260730.py
SHA-256 20e1a41fa020089db9a17892ef1d3e24c34f74932b193b7225f0530d113ec1dc
```

## 7. General mathematical content

The master isolates the reusable statement behind the successful finite
repairs:

> A braid of long source segments is globally resident once each seam is
> resident in a bounded collar; within the collar depth, all shadow loads are
> exactly additive.

What remains nonlocal is precisely the long-window upper/lower shadow ledger.
A general shadow-preserving braid theorem would supply a deterministic way to
choose the port permutation so these long-window rows are also covered.  The
finite master is therefore both a stronger `k=16` search and a faithful
experimental form of the missing all-`k` theorem.
