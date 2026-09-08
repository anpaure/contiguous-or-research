# Two-projection cursor gluing and composable endpoint credit

Date: 2026-09-09. Pure proof by `exact_equality_structure`.

Status: exact local gluing, endpoint-service, and accounting theorems.
No computation, new literal word, or all-dimensional attainment is
claimed. The interface below permits arbitrarily many marked/unmarked
runs. It is necessary and sufficient for the **specified synchronized
projected trajectories and endpoint appointments**; it does not assert
that a covering family of those trajectories exists at length B(k).

## 1. Retained results and the narrower addition here

The following existing records were read before this derivation:

* `scratch/EXACT_MANY_RUN_RECENCY_CURSOR_AND_PROTECTED_WITNESS_COMPILER_20260909.md`,
  Sections 2–7: the single-tag two-threshold cursor, exact segment
  compatibility, and the complete protected-interval compiler.
* `scratch/PAIRED_ENDPOINT_CATALAN_RUN_BOUND_INDEPENDENT_AUDIT_20260909.md`,
  Sections 1–3: shared right endpoints inject into unmarked runs, giving
  the Catalan-scale run requirement and its run-start coupling.
* `scratch/EXACT_TWO_SIDED_LIFT_JOINT_RECENCY_COMPILER_AND_SCOPE_20260908.md`,
  Sections 3–5: coupling the prefix and suffix orders of ONE permuted
  middle word requires its full cell-incidence matrix. That is a
  different coupling from the two overlapping alphabet projections here.
* `MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`,
  Sections 1, 6–7, and 9: event queues and protected compiler records
  already form a composable finite seam interface.
* `MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`,
  Sections 5–7, and
  `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`,
  Sections 4–7: preserving owners alone does not give the common-cap,
  all-rank, or regenerative Pascal construction.

Consequently a generic assertion that full states or protected witnesses
compose would add nothing. The more specific additions here are:

1. two overlapping projected recency states need at most ONE additional
   trit, located precisely at a shared empty-old gap;
2. the four target sectors have explicit prefix tests, and both-tag
   coverage is exactly an intersection of projected ENDPOINT sets;
3. uniquely assigned paired targets carry only one open-run credit bit
   through a seam, with an exact additive slack identity.

There is no register containing arbitrary past intervals. Lower targets
are protected by local endpoint appointments. Choosing a complete family
of appointments remains part of the construction input.

## 2. The shared old state and two cursors

Let the physical alphabet be X union {x,y}, with x,y not in X. All
recency partitions are ordered most-recent block first. A recency state
records the seen coordinates; unseen coordinates do not appear. Its
nonempty prefix unions are exactly its nonempty suffix-OR targets.

Consider two states P_x on X union {x} and P_y on X union {y}. Deleting
their tag coordinates must leave the SAME old recency state

    P=(A_1|...|A_m),
    D_j=A_1 union ... union A_j,  0<=j<=m,  D_0=empty.

Write S_X=D_m for the seen old support. For each seen tag z in {x,y},
its single-tag cursor is

    B_z = old coordinates strictly more recent than z,
    C_z = old coordinates at least as recent as z.             (2.1)

Both are in the enlarged old prefix chain {D_0,...,D_m}. Either
B_z=C_z=D_j, placing z in the empty-old gap after D_j, or
(B_z,C_z)=(D_(j-1),D_j), tying z to the nonempty old block A_j.
These are exactly the cursor cases established in the many-run note.

If z is unseen, retain an absent-z flag. For exclusion tests below one
may set B_z=S_X; an inclusion test for an absent tag always fails. No
value of C_z is needed for an absent tag.

## 3. Exact gluing: only one possible ambiguity

**Gluing theorem.** States P_x,P_y are restrictions of a joint recency
state if and only if their old restrictions agree. If they agree, the
joint state is unique except when BOTH tags are seen and

    B_x=C_x=B_y=C_y=D_j                                (3.1)

for the same empty-old gap. In that case exactly three joint states
are possible at this gap:

    ... | x | y | ...,
    ... | y | x | ...,
    ... | {x,y} | ... .                                (3.2)

Every other block is fixed. In particular, two tags tied to the same
NONEMPTY old block are necessarily tied to each other; they do not
create an ambiguity.

**Proof.** The nonempty old blocks have a fixed order. Each projection
places its tag either in one such block or in a specific gap. Tags in
different locations therefore have forced relative order. Tags tied
to the same old block must belong to that very block in the joint
partition. If they occupy the same gap, there is no old coordinate
between them to record their order, so the three alternatives (3.2)
are possible and exhaust the ordered partitions on the two tags.
Deleting the other tag verifies both projected states in each case.
Absent tags are simply not inserted. QED.

This is a compression RELATIVE TO the two prescribed projected states:
it replaces an independent full joint-state object by one trit only
when (3.1) holds. It does not compress away the old partition P itself.

The trit is necessary. On X={a}, the three histories

    (a,y,x),   (a,x,y),   (a,{x,y},{x,y})

have terminal joint states (x|y|a), (y|x|a), and ({x,y}|a), respectively.
All three give terminal projected states (x|a) and (y|a). At the common
empty prefix gap, the first exposes singleton x but not singleton y,
the second exposes y but not x, and the third exposes neither. All
three expose {x,y}. Every displayed physical letter is nonempty.

## 4. Exact four-sector suffix formulas

For D in {D_0,...,D_m}, consider the full target

    D union T,  T subseteq {x,y}.

Discard the empty full target when D=T=empty. If a tag in T is unseen,
the target is absent. Subject to that convention, its presence as a
suffix union at this endpoint is characterized as follows:

    T=empty:  D subseteq B_x intersect B_y.                    (4.1)

    T={x,y}:  C_x union C_y subseteq D.                        (4.2)

    T={x}:    C_x subseteq D subseteq B_y,                     (4.3)
              with the exception stated below.

    T={y}:    C_y subseteq D subseteq B_x,                     (4.4)
              with the symmetric exception.

The only exception in (4.3) occurs when both tags occupy the common
empty-old gap D, as in (3.1). Then x must be STRICTLY more recent than
y. A tie is not enough. Equation (4.4) instead requires y strictly
more recent than x. If the excluded tag is absent, no exception arises
and its B value is S_X.

**Proof.** A prefix avoiding a tag must stop before its block and thus
has old part contained in its B threshold. A prefix including a tag
must include its block and thus has old part containing its C threshold.
These give the necessary inequalities. In the glued partition, they
also specify a permissible cut unless the desired cut tries to separate
two tags in the same empty-old gap. The appropriate strict order in
(3.2) is then exactly the remaining condition. If both tags are tied
to the same nonempty old block, the one-tag inequalities already fail:
C_x=C_y strictly contains B_x=B_y. There is therefore no omitted
nonempty-block exception. A cut before both, after both, or at an
unambiguous old block supplies all remaining cases. QED.

For any fixed full rank r, these formulas give its exact four-sector
candidate chain by taking |D|=r, r-1, r-1, or r-2, respectively. A joint
recency chain cannot contain two distinct targets of the same full rank;
the tests above are compatible with this chain constraint automatically.

## 5. The missing both-tag obligation is endpoint synchronization

Fix a synchronized physical word, allowing zero letters in either of
its projections. For an old set D, let

    E_x(D)={t : D union {x} is a suffix target in projection P_x at t},
    E_y(D)={t : D union {y} is a suffix target in projection P_y at t}.

The exact joint both-tag endpoint set is

    E_xy(D)=E_x(D) intersect E_y(D).                           (5.1)

In particular D+x+y is covered if and only if this intersection is
nonempty. The assertion includes D=empty.

**Proof.** A joint D+x+y witness projects to the two required witnesses
at the same endpoint, giving necessity. Conversely, choose two projected
witness intervals ending at a common endpoint. They are nested as
intervals of physical positions. Their old ORs are both D; their union,
which is the larger interval, contains both tags and no old coordinate
outside D. Its joint OR is exactly D+x+y. Equivalently, (4.2) is the
conjunction of the two single-tag inclusion thresholds. QED.

Thus the two synchronized projected states already determine the whole
both-tag sector. The extra trit affects only the exclusive single-tag
sectors. What separate projected COVERAGE forgets is the coincidence of
the service times in (5.1).

For a minimal failure, take the physical word

    ({a,x}, {b}, {a,y}).

Its projections represent a+x and a+y, respectively, but a+x+y is absent:
any interval containing both tags crosses b. A version with UNIVERSAL
projections is obtained by listing all nonempty subsets of {a,b,x} as
literal letters, then inserting {b}, then listing all nonempty subsets
of {a,b,y}. Both projections are universal. Nevertheless neither {x,y}
nor {a,x,y} is a joint target, since every interval containing both tags
crosses the intervening b. Hence even full coverage in each projection
does not provide the joint induction step.

There is a distinct single-tag failure. If the actual terminal state is
(y|x|a), projection P_x exposes singleton x but the full state does not.
Exclusive sectors need the exclusion threshold and, at (3.1), the trit.

## 6. Synchronized updates and the small order latch

Let the next projected letters be U_x subseteq X+x and U_y subseteq X+y.
They can be the restrictions of ONE physical letter precisely when

    U_x intersect X = U_y intersect X = U,

and their union V is nonempty. In this case the physical letter is
uniquely

    V=U union (x if x in U_x) union (y if y in U_y).            (6.1)

An individual projected letter is allowed to be zero. For example V={y}
gives a zero P_x update. Such a time slot is retained and charged; it
cannot be deleted from one trajectory while maintaining synchronization.

The old state updates by the usual move-to-front set rule. For each tag z:

* if the new physical letter contains z, set B_z=empty, C_z=U and mark
  z seen;
* otherwise, if z was seen, set
  B_z <- B_z union U and C_z <- C_z union U;
* otherwise retain the absent-z flag.

The relative last-update order of the two seen tags obeys a three-value
latch:

* both updated: tie;
* only x updated: x before y;
* only y updated: y before x;
* neither updated: retain their order.

If their current locations force the order, it is reconstructed from
the projected states. Only in the shared-gap case is the latch stored
as additional data. An old-only update can erase separating old blocks
and create (3.1); the previous forced order then supplies the trit.
It is not legal to choose a new trit freely whenever (3.1) reappears.

**Synchronized trajectory theorem.** Given a realizable incoming state,
two projected update sequences lift to a nonempty physical sequence with
exactly those trajectories if and only if their old letters agree at
every charged time and (6.1) is nonempty at every time. The lifted word
and all its outgoing states are uniquely determined. Any prescribed
intermediate or outgoing trit must equal the latch value above.

**Proof.** Projection commutes with the recency update, including zero
projected updates. Therefore (6.1) reproduces the specified projections
and the last-update order. Induct on the physical update count. Conversely
every actual letter has exactly these restrictions, and its actual
tag order obeys the stated latch. QED.

In particular a seam is transparent to the entire promised suffix deck
when the two projected boundary states and the possible shared-gap trit
agree. Equality of only the projected states can fail by the example
in Section 3. For a smaller prescribed target palette some unequal
states can suffice; no necessity of full boundary equality for that
weaker problem is claimed.

## 7. Protected lower targets as endpoint appointments

A fragment consists of synchronized update sequences, an incoming
compressed state, and a list of pairs (t,S) meaning that the full target
S must be a suffix target after its t-th update. Call these endpoint
appointments. Include any required middle owners or lower-rank targets
in this list, and test them by (4.1)–(4.4).

This is an exact local service test. It covers a witness that starts in
the incoming history as well as one lying wholly inside the fragment.
No past interval start needs to be stored: a recency prefix itself
guarantees an ordinary suffix interval in every history realizing that
state. If an explicit witness is wanted after compilation, choose its
actual suffix interval in the concatenated history.

**Appointment composition theorem.** For specified projected fragments,
the following conditions are necessary and sufficient for their
literal concatenation to realize their specified trajectories and all
their appointments without extra join letters:

1. their projected letters agree on X and produce nonempty joint letters;
2. each outgoing compressed state agrees with the next specified
   incoming state, including the shared-gap trit when it is needed;
3. every appointment passes its sector-prefix test at its specified time.

The initial state must be produced by an actual initializing word, whose
length is charged, or be the empty state of an empty history. An appointed
target at a fragment's time zero belongs to the preceding history and
cannot be counted again as a new endpoint of that fragment.

**Proof.** Section 6 gives the literal concatenation and all reached
states. Section 4 supplies the promised suffix targets. A literal
interval already completed in an earlier fragment is not changed by
appending later letters. This proves sufficiency. Necessity follows
from restricting any concatenation claiming those same trajectories
and appointments. QED.

This preserves any prescribed projected middle-rank chains because the
whole projected trajectories agree. It also preserves all NAMED full
lower witnesses appointed in the actual joint sectors. A projected
lower witness is not automatically a full lower witness: the excluded
tag tests still apply.

For all-rank coverage, every nonempty full target must receive at least
one actual appointment somewhere in the paid construction. For exact
middle accounting, select one appointment per middle target, with the
named target families partitioned across fragments. Verifying that
partition is an explicit global combinatorial obligation; it is not
replaced by the compressed boundary state.

## 8. Additive middle-owner slack

For a fixed full rank r, let a fragment have ell new physical updates
and a_r distinct assigned rank-r appointments. At most one rank-r target
can be appointed at any one endpoint. Define

    delta_r=ell-a_r >=0.                                      (8.1)

If the named rank-r families of all fragments and the paid initializer
partition the complete rank-r layer, then

    N-binomial(|X|+2,r)=sum_fragments delta_r.                 (8.2)

The initializer is included on the right as one paid fragment. For two
middle layers carry both delta values. These are ordinary endpoint
deficits, not uncharged seams or assumed flat-window identities.

Equation (8.2) makes a literal length claim reviewable: an exact B(k)
construction must exhibit the appropriate complete named layers and
the exact sum of its local endpoint deficits. Boundary-state matching
alone gives neither requirement.

## 9. A one-bit paired-run credit that survives fragmentation

This section turns the already proved paired-endpoint injection into
an exact seam ledger. It does not claim a new global run inequality.

Fix one coordinate z of a physical word, and write Y for all other
coordinates. Fix s>=1. Choose one appointment for each target in some
old rank-s family and one for each target in some z-containing
rank-(s+1) family. Within each family a named target is assigned at most
once in the complete construction. Arbitrary additional target
occurrences or redundant protected appointments are allowed, but they
are not credited again in this chosen ledger.

At a shared endpoint, the two chosen targets must be D and D+z. The
single-tag cursor on the full old alphabet Y satisfies

    B_z=C_z=D,  |D|=s.                                       (9.1)

The endpoint lies in an unmarked run following a marked letter.
During one such run B_z is increasing. Thus it has at most one DISTINCT
rank-s value. Because chosen old targets are distinct, that run can
support at most one shared appointment. This is precisely the injection
proved in the paired-endpoint audit.

For clarity, these full-old-alphabet thresholds need no additional state.
When z=x and Y=X union {y}, the cursors (2.1) give them directly as

    Bhat_x = B_x union ({y} if y is strictly before x),
    Chat_x = C_x union ({y} if y is before or tied with x).     (9.1a)

An unseen y is not inserted. The order is either forced by the two
projected locations or supplied by their one shared-gap trit. Exchange
x and y for the other coordinate. In (9.1) use these hatted thresholds
when the chosen coordinate's old alphabet includes the other tag.

Carry one bit c for the presently open unmarked run:

* before any z has appeared, c=0;
* a marked-to-unmarked transition creates c=1;
* a shared chosen appointment requires c=1 and (9.1), then consumes it;
* a marked letter expires any unused c and resets c=0;
* any other unmarked update leaves c unchanged.

The bit at a fragment boundary is inherited, not re-created. Whether
the previous physical letter contains z is already read from the first
block of the full recency state (with a separate empty-history case).
Thus counting the exit at the first update of a fragment is unambiguous.
For the two-projection setting that full state is recovered by the
compressed interface; no previous letters have to be retained.

For a fragment define:

    R = number of marked-to-unmarked transitions at its new updates,
        including a transition across its incoming boundary;
    h = number of shared chosen appointments at its new endpoints;
    e = number of UNUSED credits expired by marked updates;
    c_in,c_out = its incoming and outgoing credit bits.

The exact conservation identity is

    h+c_out+e = R+c_in.                                      (9.2)

**Proof.** A created bit is consumed once, expired once, or is the
outgoing bit. An incoming bit has the same alternatives. No transition
creates a bit while an old one remains: the preceding marked letter
has reset it. Sum these elementary updates. QED.

Conversely, every actual once-per-target paired appointment schedule
admits this bit evolution: the run injection prevents requesting a
second credit in the same run. The bit is therefore an exact local
accounting device for such chosen schedules, rather than an additional
restriction on the word's ordinary target occurrences.

Let a and b count the two chosen families' appointments in this fragment,
and let u count new endpoints assigned NEITHER family. Since no endpoint
has more than one assignment in either family,

    ell-a-b = u-h.

Combining with (9.2) gives the exact local slack identity

    ell-a-b+R+c_in-c_out = u+e >=0.                          (9.3)

The c terms telescope over arbitrarily many fragments. Starting from
the empty history gives c_initial=0, hence the familiar global bound

    a_total+b_total <= N+R_total,

with an explicit unused-final-credit correction if desired. Reversal
gives the incoming-run version. A seam inside an existing unmarked run
does not earn a new overlap, even if each piece separately exposes the
same paired rank-s value.

A concrete cross-boundary service is the word

    ({a,z},{b}) || ({a}),  with s=2.

At the displayed boundary, the open unmarked run has c=1, B_z={b},
C_z={a,b}; no paired rank-two appointment is yet possible. The next
letter makes B_z=C_z={a,b}. It simultaneously serves {a,b} by positions
2–3 and {a,b,z} by positions 1–3, consuming the inherited bit. The second
fragment has ell=1, a=b=1, R=0, c_in=1, c_out=0, and u=e=0, so (9.3)
holds with equality. Resetting its input or refusing crossing suffixes
would discard this legal one-position paired service.

For several fixed coordinate/rank ledgers use one such bit for each.
It is not necessary to record the old names of the serviced targets
inside this bit; once-per-target ownership is established separately
by the explicit named-family partition. The bit does not certify that
partition. This separation is essential to the scope of (9.3).

## 10. The constructive interface and what it does not settle

The resulting seam data are:

    the common old state P;
    each projected tag cursor or absence flag;
    one trit only at a shared empty-old gap;
    the selected open-run credit bits and additive endpoint deficits.

Together with the actual synchronized fragment updates and endpoint
appointments, these give a literal, necessary-and-sufficient local
compiler. They admit any number of coordinate runs without resetting
the state, and they expose a specific test for the previously missing
both-tag targets: common service endpoints in (5.1). There is no
independent all-history register or unexplained crossing-witness rule.

This changes the useful induction question from independent projected
coverage to SYNCHRONIZED target service: construct projected fragments
whose endpoint intersections cover the both-tag sector, whose cursor
exclusions and trit cover the exclusive sectors, and whose exact
deficits and inherited run credits fit the paid budget. The existing
Pascal/event records do not supply that family merely from their
owner counts, and this note does not supply it either.

The still missing all-dimensional statement is existence of those
compatible named target allocations and trajectories, with a
regenerating interface and total length B(k). The currently verified
equalities at17 and18 are retained; no equality at19 or at all k follows
from the local gluing theorem alone.
