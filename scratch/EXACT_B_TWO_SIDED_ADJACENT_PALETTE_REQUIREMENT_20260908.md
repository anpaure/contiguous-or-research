# Both adjacent-rank palettes have only endpoint-sized exceptions

Date: 2026-09-08.

Status: elementary necessary condition, not an attaining construction.
The lower-side argument is already in MASTER_HANDOFF.md Section 3.12.
This note records its upper-side companion and a concrete recapture
condition for assembling the current k17 owner components.

For the frozen 306-owner prefix with its one-pivot schedule, the sharp
consequence at the end of this note is at least 59 required new rank-ten
adjacency colors. The earlier 53 count below is the coarser consequence
available without using the precise deadline gaps.

## Statement

Let a linear set-valued word A have length n=W+t and cover every rank-r
target, where W=binom(k,r). Choose one interval J_i=[a_i,b_i] for each
rank-r target T_i, ordered by its left endpoint. Distinct rank-r targets
cannot have nested witnesses, so both a_i and b_i increase strictly.

Let P_minus be the distinct rank-(r-1) sets among

    T_i intersect T_(i+1),  0 <= i < W-1,

and P_plus the distinct rank-(r+1) sets among

    T_i union T_(i+1),     0 <= i < W-1.

If A also covers the corresponding adjacent rank, then

    binom(k,r-1) - |P_minus| <= 2t,                 (1)
    binom(k,r+1) - |P_plus|  <= 2t.                 (2)

No common physical interval length, Johnson adjacency, critical-witness
uniqueness, or maximal-envelope hypothesis is needed.

## Proof

At a fixed left endpoint all interval ORs form an inclusion chain, so
there is at most one distinct target of any fixed rank there. The same
holds at a fixed right endpoint. There are t positions outside the
selected start set {a_i} and t outside the selected end set {b_i}.
Consequently at most 2t targets of a specified rank can have a chosen
witness using at least one unselected endpoint.

Consider a witness whose endpoints are both selected, [a_j,b_i].

If its rank is r-1, then j>i: otherwise it contains J_j and has rank at
least r. With j>i, the interval lies inside J_i and J_(i+1). Its OR S
therefore lies inside T_i intersect T_(i+1). Since S has rank r-1 and
the two distinct owners have rank r, this intersection is exactly S.
This is the existing lower-side argument.

If its rank is r+1, then j<i. For j=i it equals J_i and has rank r;
for j>i it is contained in J_i and has rank at most r. When j<i, it
contains both J_j and J_(j+1). Their distinct rank-r unions lie inside
its rank-(r+1) OR S, forcing T_j union T_(j+1)=S.

Thus a target absent from its adjacent palette must use an unselected
endpoint in every witness. Charge one witness for each missing target
to such an endpoint. At most one distinct target of the given rank can
be charged to each endpoint, proving both inequalities.

## Odd middle-layer efficiency

For k=2r-1 with r>=2, binom(k,r-1)=W. Let b be the number of non-Johnson steps in
the linear chronology and let e_minus count repeated lower colors among
its Johnson steps (total occurrences minus distinct colors). Then

    b + e_minus = W-1-|P_minus| <= 2t-1.           (3)

In particular, an exact k17 word has at most five non-Johnson steps and
repeated lower-color occurrences combined. This is the linear-path form
of the already recorded cyclic palette restriction, not a new existence
theorem. The actual 306-owner prefix already spends three non-Johnson
steps; its precise remaining lower-color interface is in
K17_PBBS_PREFIX_RANK8_PROVIDER_INTERFACE_20260908.md.

## A rank-ten recapture condition for canonical-component assembly

Suppose all canonical k17 owner cycles are cut once and their complete
owner lists concatenated to form one chronology. Let H be a set of
rank-ten targets that disappear from every retained internal adjacent
union after those cuts. Each new seam contributes at most one distinct
rank-ten adjacent-union color. If the resulting owner chronology is
realized by a universal word of length W+3, inequality (2) forces at
least

    max(0, |H|-6)

different members of H to reappear as new-seam union colors. Physical
endpoints can account for at most the remaining six. Capping the source
without changing the chronology cannot remove this necessity.

The complete fixed cut-core census shows that 59 original cycles lose
at least one globally exclusive rank-ten target at every cut. These
targets from different cycles are distinct. Therefore the unmodified
one-cut-per-cycle assembly needs at least 53 such rank-ten recaptures
at its new seams. This counts required colors, not extra letters.

The new mountain C6 certificate replaces its two affected components
by two components that remain unsafe at every cut already at rank ten.
It preserves their entire local upper support. Hence the same 59-cycle,
53-seam requirement applies after that particular replacement as well.
This is a count over all new seams relative to that all-cycle factor,
including any seams already fixed in a prefix. It is not a claim that 53
additional Q seams remain necessary after the 306-owner stage; credit
from the prefix would first have to be evaluated in the actual chronology.
More general rethreadings can change the cut bank and require their own
census; this note does not constrain them by the old count.

Every required rank-ten seam is Johnson, but a Johnson seam also changes
the rank-eight palette. The two requirements must hold on the same
owner edges. Neither these counts nor the separate existence of suitable
edges supplies a compatible spanning chronology, upper-rank coverage, or
the common lower compiler.

## Fixed-prefix credit: none against the 59 unsafe cycles

A bounded h100 check now evaluates all five new seams of the actual
306-owner prefix. Their union ranks, in order, are

    15, 13, 12, 10, 10.

The two rank-ten colors are 111958 and 128340. The first is not globally
exclusive to an original cycle. The second is exclusive to cycle 69,
which is not among the 59 cycles unsafe at every cut. Neither color is
an exclusive rank-ten target of one of those 59 cycles. After the mountain
C6 the same conclusion holds: the affected cycles' new exclusive target
lists also contain neither color.

Therefore the five already fixed prefix seams receive ZERO credit against
the particular 59-color lower bound used above. If Q is obtained by
opening each remaining whole cycle once, at least 53 additional seams
(inside Q or at P/Q) must supply lost exclusive rank-ten colors. This is
now a verified bound for the fixed prefix, not an inference that ignores
its existing seams. Internal edges retained inside a prefix block cannot
supply a globally exclusive target of a different original cycle.

The exact diagnostic is

    scratch/audit_k17_prefix_rank10_recapture_credit_20260908.py
    scratch/k17_prefix_rank10_recapture_credit_20260908.json.

It reads the existing complete cut inventories and the literal prefix;
it checks only its five prescribed seams. Mathematical execution was only
on h100. This does not exclude rethreading within remaining cycles, which
can change both their exclusive support and the relevant cut obligations.

## Only one possible upper exception per depth increase

The consecutive-start geometry gives a sharper upper theorem. Suppose

    I_i=[i,r_i], r_i=i+h_i, 0 <= i < W,

where the depths h_i are nondecreasing and the word ends exactly at
r_(W-1). Let J be the number of strict depth increases, including a
possible increase at the final owner. Then at most J distinct rank-(r+1)
targets of the word can be absent from P_plus. Each such target must have
a witness of the form

    [i,b], where r_i < b < r_(i+1).                (4)

Proof: if a witness ends at r_i, a start at least i makes it a subinterval
of I_i, so its rank is at most r. A start at most i-1 makes it contain
I_(i-1) and I_i, forcing its rank-(r+1) value into the adjacent-union
palette. An endpoint before r_0 also gives a subinterval of I_0 and
cannot have rank r+1. In a gap r_i<b<r_(i+1), a start at least i+1 is
inside I_(i+1); a start at most i-1 contains I_(i-1) and I_i. The only
remaining start is i. Its intervals (4), as b varies in this one gap,
are nested and supply at most one target of the given rank. These cases
cover the whole word. Nonempty gaps correspond exactly to strict depth
increases, proving the assertion. No exclusion of a final depth increase
is needed for this upper theorem.

For the k17 one-pivot schedule there is one gap, after owner 305, and its
only exceptional upper cell is

    [305,308].

Its union contains P_305=103765. Thus an exceptional rank-ten target must
be one of the eight rank-ten supersets of P_305. The exact diagnostic
listed above checks all eight. Only 103767 is exclusive to any original
cycle, and that cycle is 69, which is not among the 59 unsafe cycles.
The mountain replacement introduces no new exclusive supplier for these
eight targets. None can therefore pay for a lost exclusive rank-ten
target from one of the 59 unsafe cycles.

## The fixed-prefix requirement is at least 59 new adjacencies

Combining the preceding facts gives a stronger conclusion. For the fixed
prefix and one-pivot schedule, each of the 59 unsafe cycles forces a
different rank-ten target to be supplied by a new adjacency in Q or at
P/Q. Neither the existing prefix seams nor the one exceptional physical
upper cell supplies any of those targets. Thus at least 59 new adjacency
colors, rather than merely the coarse 53, must be supplied.

This last necessity also allows rethreading within Q. Indeed, a linear
path on all owners omits at least one edge of each reference cycle. For
one of the 59 cycles, choose any omitted edge. Cutting there alone loses
an exclusive rank-ten target, by the complete census. Such a target has
exactly one adjacent-union witness edge in the entire reference factor:
every owner has rank nine, so every longer rank-ten occurrence contains
an adjacent rank-ten occurrence; if another witness edge existed, cutting
the chosen edge could not lose the target. Therefore no retained old
edge can recover it. Different reference cycles give different targets.
The only remaining possibility is a new adjacency of the final path.

Here "new" means absent from the specified reference factor, either the
original factor or the factor with the audited mountain C6. It does not
mean a new physical letter. A rethreading can supply these adjacencies,
but cannot avoid this count while keeping this prefix and this physical
schedule. The necessary lower-color providers and these upper colors
must coexist on the same final owner chronology.
