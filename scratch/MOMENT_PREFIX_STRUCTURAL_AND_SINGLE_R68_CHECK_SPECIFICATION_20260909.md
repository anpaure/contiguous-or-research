# Height-moment prefix audit: structural checks and one r=68 frontier

2026-09-09. Prepared by `exact_b_finite_frontier`.
**Status: the reviewed standalone checker, all structural checks, and the
complete priority-free r=68 replay PASS.** This independently certifies
the ten-parts-per-million bound at k=137 and138 only. No uniform starting
threshold or unprovided band is asserted.

The supplied document is `/Users/amir.nuriyev/Downloads/MOMENT_PREFIX_ADVANCE.md`.
Its claimed 3,356-case collection and predecessor transcript were not supplied.
This independent task does not regenerate that band or assume its reported
successes. It checks the new finite formulas and attempts just their first
claimed dimension, r=68, corresponding to k=137 and the following even lift.

Source: [verify_moment_prefix_structure_and_r68_20260909.py](verify_moment_prefix_structure_and_r68_20260909.py).
It imports only the Python standard library; it does not import either
user-named verifier or generator. Execution is restricted to `ssh h100`,
hostname `arboghast`, under 60 CPU seconds, 90 wall seconds, and 1 GiB.

## Exact structural checks

The program computes the triangular table through a=100:

    K(a,b)=binom(a,b)binom(a,b+1)/a,
    H(a,0)=1,
    H(a,b)=K(a,b)+sum_c binom(a+c,2b)H(b,c), b>0,

with c ranging from max(0,2b-a) through b-1. Adjacent fibre coefficients
are advanced by exact integer ratios. Every associated K mass identity
and every Catalan row sum is checked. It saves every exact K,H table cell
and an outward rational enclosure for H(100,50)/K(100,50). The illustrative
decimal16.42824502 is compared with error below one unit in its eighth
decimal place; the actual rounded value is computed rather than assumed.

For an independent combinatorial comparison, the code enumerates all
23,713 nonempty Dyck roots through semilength10. It computes their heights
directly from partial sums, removes all peaks simultaneously, and verifies
that height drops by exactly one. Every pruning-size class count and
height total must agree with K and H.

It also enumerates every middle-layer bridge through semilength9, a total
of125,475 binary words. For each fixed cut it computes the maximum and
minimum partial sums and checks both exact reflection tail formulas.
Rotation immediately after the first global minimum gives a Dyck root
after its final unmatched zero is removed. Each Dyck root must occur
exactly2a+1 times, and its height must not exceed the original bridge's
partial-sum range. This checks the finite rotation weighting used by the
reflection bound without using a uniform-cycle assumption.

For every a≤100 and every0≤t<a, exact rational arithmetic verifies that
the geometric two-tail bound G_a(t) dominates the full finite binomial
tail B_a(t). Every table class must satisfy H(a,b)≤2tK(a,b)+B_a(t).
For the directly enumerated roots it also verifies the total positive
height excess bound. Finally it checks the supplied integer heuristic
choice of t and its resulting upper cap against every exact table value.

Ordered weak composition rows arising through core size9 are independently
enumerated; their least cyclic periods are found by direct rotation tests.
Their exact histograms must equal divisor-inversion row counts. Complete
prefix trees through r=9 then check the one-row integrated height-weight
identity, its primitive-baseline-plus-correction form, and its domination
by the simpler moment bound. At terminal leaves the exact cycle counts,
height histograms, period histograms, and unrounded native collar charge
must match the previously verified partition census. That input is pinned
by SHA-256

    43b52c9d3ed72b9901dc7c6aca96a4ce8f46a12e322fc01c181da1a3412869b2.

The numerical checks do not themselves constitute a new all-dimensional
proof of the retained inverse-pruning bijection or corridor theorem.
Those are explicit inherited mathematical inputs.

## The single r=68 attempt

The frontier begins with every class `(s,a,b,w,P,beta)=(0,68,b,1,137,0)`,
b=0,...,67. All exact masses wK(a,b) are retained and sum to Cat_68.
Every nonterminal refinement includes all permitted next sizes and all
positive ordered-row least-period classes. There is no sparse omitted
mass, reserve, primitive approximation, or fixed-size probability model.

All core sizes are at most68, so every height total in this attempt is
from the exact table. At a nonterminal prefix define

    M_d=sum_c chi(2b+1,a-2b+c;d)K(b,c),
    R_d=sum_c chi(2b+1,a-2b+c;d)H(b,c).

With the exact period update P_d, its chosen charge is the ceiling of

    sum_d w((2s+1)M_d+2R_d)/P_d.

The sum is formed as an exact rational before rounding. It is checked
against the simple moment charge and the previous deterministic height
cap. Every symmetric-row class is included explicitly. Terminal b=0
includes the final one-slot denominator before being charged.

Largest integer charge chooses the next prefix, with node id breaking
ties. This is only an efficiency rule; no proof uses rounded-charge
monotonicity. The run stops at `100000*U<Cat_68` or a fixed cap of10,000
refinements or1,000,000 generated nodes. Soft time reserves leave room
for saving and replaying the complete current frontier before the hard
limits. A proposed split exceeding the node limit is not committed.

Every split and every final leaf is saved. The independent priority-free
replay starts again from all initial Narayana classes, regenerates every
complete split, and recomputes beta with `Fraction`. It derives each
integrated charge directly by summing its c/d height contributions,
rather than using the generator's cached M_d,R_d table. It consumes
every final leaf once, checks its complete state and charges, and freshly
sums both root mass and U. A final certificate is written only after
that replay passes. A hard interruption or incomplete replay is not
reported as a verified result.

If the strict test passes, it certifies only

    nu(137)<1.00001W(137),
    nu(138)<1.00001W(138)

for the retained constructor and exact even lift. It would not establish
the claimed uniform threshold137, the unprovided cases r=69,...,3423,
or the construction-specific predecessor failure at r=67. No actual
137-coordinate literal word is being materialized.

## Completed structural results

The exact table has5,050 cells. Its illustrative entry is

    H(100,50)=1639452428304777052039247303159019375898856879930188151279,
    K(100,50)=99794739256977899071474889425225225330079579752931446368.

Exact integer division gives

    16.428245020843044252579122292728
       <= H(100,50)/K(100,50)
       < 16.428245020843044252579122292729.

Its nearest eight-decimal value is16.42824502, agreeing with the supplied
illustration. The preceding deterministic class-height cap was51.

All23,713 directly enumerated Dyck roots through semilength10 passed
every pruning-class count and height-total comparison. All125,475 middle
bridges through semilength9 passed the two reflection counts, canonical
root rotation multiplicities, and height-versus-range inequalities.
The exact finite checks also passed5,050 rational geometric-tail bounds,
338,350 class-height tail comparisons, and every tested integer Hhat cap.

The direct ordered-row enumeration covered2,575 weak compositions across
36 distinct slot/mass cases. Every least-period histogram agreed with
divisor inversion. The complete small-prefix audit visited288 states
and checked184 integrated-period correction identities. At r=1,...,9,
all full terminal period/height histograms and unrounded native charges
agreed with the independently verified partition census.

These are the actual independently executed scopes. They are not a claim
to have reproduced the larger user-reported row or transcript collection.

## Completed single r=68 certificate

The fixed traversal reached its strict target after162 refinements and
2,571 generated nodes. The complete final frontier has2,409 leaves,
including2,388 unfinished leaves whose entire masses remain charged.
The maximum processed prefix depth is three. There were no sparse
reserves, omitted children, approximate heights, or suppressed symmetry
classes.

The exact integers are

    Cat_68=86218923998960285726185640663701108500,
    U=860872256709126171307785011672491.

The replay freshly reconstructs every split and consumes every final
leaf once, obtaining the same Catalan mass and integer U. Its exact
positive margin is

    Cat_68-100000*U=131698328047668595407139496452008500>0.

Consequently

    U/Cat_68 < 0.000009984725125072396316850761 < 0.00001.

The resulting integer construction upper bound at k=137 is

    W(137)=11811992587857559144487432770927051864500,
    N <= 11812110527356728294772901937473650995767.

The exact even lift supplies the same relative bound at138. This is a
charge certificate for the retained finite construction; the huge words
were not materialized. It leaves the unprovided cases r=69,...,3423 and
the construction-specific r=67 lower-collar certificate unverified.

## Execution and reproducible artifacts

Root and `exact_equality_structure` independently read the complete source
before the one authorized run. It executed only on h100 under60CPU
seconds,90wall seconds and1GiB, with30CPU/40wall build-reserve cutoffs.
The complete structural audit, frontier generation and final replay took
**1.5315 CPU seconds and1.5325 wall seconds**. There was no retry,
alternative priority, additional dimension, or band enumeration.

The source SHA-256, independently read before execution, is

    6f1f556319147121250420d4715a21e0a7cbf3a679392b3b7b8b210a11c17132.

Artifacts:

* [Complete certificate](moment_prefix_structural_and_r68_20260909/moment_prefix_complete_certificate.json).
* [Structural certificate](moment_prefix_structural_and_r68_20260909/structural_certificate.json).
* [Every exact table cell](moment_prefix_structural_and_r68_20260909/exact_height_table_through100.jsonl), rows `[a,b,K,H]`.
* [r68 summary](moment_prefix_structural_and_r68_20260909/r68_frontier/summary.json).
* [Every split](moment_prefix_structural_and_r68_20260909/r68_frontier/splits.jsonl).
* [Every retained leaf](moment_prefix_structural_and_r68_20260909/r68_frontier/final_leaves.jsonl).

The complete report SHA-256 is

    4a72d1ed42e689b59eff6e7b80bf082e5cc7044b436731a18313834794df16d4.

The exact table SHA-256 is

    ea5cda37eae19665debafd9df93e1b9fbad049c22162ffe43420de3439cf459c.

The split log SHA-256 is

    a971bc255d40a18d0c7dd853de10dc06cdec8e255545f9c0a162f59f678b5ff4,

and the final-leaf SHA-256 is

    147c7c06c846043e0ceb30a936aa9a7877c6cf7d77a0ee9a4558c784f737e5b4.

Remote directory:
`/home/amodo/exact-b-moment-prefix-structural-and-r68-20260909/`.
The sole mathematical command was
`python3 /home/amodo/verify_moment_prefix_structure_and_r68_20260909.py`.
