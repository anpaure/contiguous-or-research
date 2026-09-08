# Canonical-Phi sector excursions with a controlled minimal run

2026-09-09. Pure constructive proof by `exact_b_induction`, developed from
root's requested all-dimensional residence lane. No mathematical execution,
search, word modification, or commit was performed.

This note gives a real finite Phi-directed path with growing residence
parameter q. It is not a spanning construction or an induction proving
nu(k)=B(k). The endpoint and global ownership problems are explicit below.

## 1. What was already known, and what is different here

The following prior sources were read before developing this construction:

* `MATH_THEOREM_LONG_RUN_MIDDLE_LEVELS_RESIDENCE_REDUCTION_20260802.md`:
  the exact relation between flip gaps and projected residence;
* `MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`
  and `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`:
  the four old-rank sectors, event queues, and the still-open joint braid;
* `MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`:
  repetitions can improve residence but incur a genuine extra-owner cost;
* `MATH_THEOREM_ADJACENT_TERMINALS_HAVE_A_MINIMAL_SIX_OWNER_RESIDENT_TWO_CHANNEL_CABLE_20260814.md`
  and `MATH_THEOREM_QGON_RESIDENT_LONGRAIL_ROLE_CONVERTER_AND_SERIAL_GATE_20260801.md`:
  explicit resident rails with freely specified insertion/deletion clocks;
* `PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md`,
  Section6: the already recorded relation between coincident boundary pins
  and a minimal-length positive owner run.

The contribution here is narrower: **every insertion is forced by the
specific canonical matching Phi**, yet a deterministic adjacent-rank
excursion with arbitrary q is possible. Its new-coordinate run is exactly
minimal, and its age interface is fully charged. The old general resident
rails did not impose these particular canonical insertions.

The literal17 and literal19 certificates prove that retaining Phi is a
real successful finite restriction. They do not supply the all-r sector
allocation or endpoint matching used nowhere as an assumption below.

## 2. Matching and age conventions

On an odd cyclic alphabet, Phi adds the unique unmatched zero of the
cyclic 10-parenthesis matching. Equivalently, in any fixed linear reading,
it flips the zero at the first global minimum of the ones-minus-zeros
prefix walk. Its exact lexical identification is in
`PBBS_PHI_LEXICAL_MATCHING_AND_PUBLISHED_HAMILTON_RESIDENCE_AUDIT_20260909.md`,
Section3.

A Phi-directed lower step is

    X -> Phi(X) minus {v},     v in X.                    (2.1)

It inserts one absent coordinate and deletes one present coordinate.
For a currently present coordinate, its age is the number of consecutive
lower states ending at the current state that contain it. Ages may be
truncated at q. A q-admissible step deletes only a coordinate of age at
least q. This is precisely the local rule ensuring that every positive
lower run which closes has length at least q.

At any state of a Johnson history there are at most q-1 present
coordinates of age less than q: each was inserted in one of the preceding
q-1 transitions, which insert at most one coordinate each. We use this
elementary bound to guarantee deletion choices. The input is a legitimate
age history, not a fresh initialization in which arbitrary ages are declared.

## 3. Why balanced Dyck-block insertion cannot amplify residence

Take an old cyclic lower state L of size r on 2r+1 old sites. Insert a
contiguous Dyck block D with s ones and s zeros at a fixed physical gap.
All parentheses of D match internally, so removing D leaves exactly the
old matching. Thus

    Phi_new(L,D)=(Phi_old(L),D).                         (3.1)

Consider the induced Phi-directed graph whose states have old weight r
and an inserted Dyck block of weight s. Every insertion in (3.1) is old.
To keep the old weight equal to r, the deletion must also be old. The
inserted block therefore cannot change at all, even if the allowed state
family contains many different Dyck blocks of that length.

The induced graph is a disjoint union of copies of the old Phi graph.
There is no internal waiting step, change of Dyck block, connection
between the copies, or residence amplification. This excludes the specific
balanced-block product recursion. It does not exclude excursions through
other old ranks or through a non-Dyck block, which is the correction next.

## 4. The upper-sector-only correction fails at root-aligned ports

Fix the old cyclic root immediately before the beginning of a Dyck word D
of semilength r. Thus the old lower state is L=0D, with old root u being
that first zero. Add adjacent new coordinates a,b after D, initially10.
The complete child lower state is

    A=0D10,       |A|=r+1.                              (4.1)

Leaving the10 sector by deleting a forces

    A -> U=1D00,                                       (4.2)

because Phi(A) adds u. All prefixes of 1D have positive height, and the
two final zeros first reach0 and then-1. Consequently Phi(U) inserts b.

If the next deletion is u, the newly inserted u has a positive run of
length one. Any q>=2 rule forbids this. Therefore the next deletion must
be an old one d from D, leading to

    B=(1D-d)01.                                        (4.3)

Every prefix of 1D-d has height at least-1, and its total height is-1.
The new a-zero first takes the walk to-2, so Phi(B) must insert a.
If the11 sector is forbidden, its only available deletion is b, returning
to10. But b was inserted only in the preceding transition, so this also
closes a positive run of length one.

Thus a q>=2 recursion cannot repair these root-aligned exits using only
the10,00,01 sectors. The lower old-rank sector11 is genuinely required
for this specific correction; this is not a statement about every possible
port at an arbitrary fixed gap.

## 5. A positive q-resident excursion through both adjacent ranks

### Theorem

Let q>=2 and r>=q+2. Suppose the child state A=0D10 has a valid Johnson
age history, with a of age at least q. Then there is a Phi-directed,
self-avoiding path of **q+2 transitions** from A to a different state

    A_out=L_out10

such that:

1. every coordinate run closed by the path has length at least q;
2. the old root u remains present after the first transition;
3. b has a positive lower run of exactly q states, closed by the last step;
4. a has age q at the output;
5. the output's full age vector is determined by the explicit steps below.

The path uses one00 state, one01 state and q-1 states in11 between its
two10 endpoints. The old weights in these sectors are respectively
r+1,r,r-1. These are distinct child middle-layer owners, not repeated
copies of an old owner.

### Construction and existence of every choice

At A at least r-(q-1) old coordinates of L have age at least q. Choose
two distinct such coordinates d,e; they exist since r>=q+2. Use

    X_0=L+a=0D10,
    X_1=L+u=1D00,
    X_2=L+u-d+b=(1D-d)01,
    X_3=L+u-d-e+a+b=(1D-d-e)11.                        (5.1)

The inserted labels are u,b,a and the deleted labels are a,d,e.
Section4 proves that all three insertions are exactly Phi's choices.
The deleted coordinates are already old enough, and no newly inserted
coordinate is deleted. The state X_3 contains both new coordinates and
the protected old root u.

For every child state K11 with |K|=r-1, the old word has total height-3.
The two final up-steps reach-2 and-1, so the first global minimum occurs
at an old site. Hence Phi inserts an old coordinate, which we denote
by kappa(K).

Perform q-2 further steps inside11. At each step insert kappa(K) and
delete an old coordinate other than u whose current age is at least q.
Such a deletion always exists: of the r-1 old coordinates, at most q-1
are young, and protecting u removes at most one further choice. Thus
there are at least

    (r-1)-(q-1)-1=r-q-1>=1                           (5.2)

permitted deletions. Choosing the least eligible physical coordinate
makes this a deterministic construction if no branching family is wanted.

After these q-2 steps, b has age 2+(q-2)=q. Apply Phi once more, which
again inserts an old coordinate, and delete b. This returns to10. The
other new coordinate a has age 1+(q-2)+1=q at the endpoint. The protected
u remains present, so the old output L_out differs from the initial L,
which omitted u.

The q=2 case has no internal11 step: (5.1) followed immediately by the
final deletion of b gives four transitions. Formula (5.2) is needed only
when there are internal steps; the stated r>=q+2 is a uniform conservative
condition, not a claimed sharp threshold.

### Simplicity and exact run count

A nontrivial closed Johnson walk of at most q transitions cannot obey
the age rule: the coordinate inserted on its FIRST transition was absent
at its initial state, so must be deleted again before the state returns,
closing a positive run of length at most q-1. Therefore the q-1 consecutive
states in11 cannot repeat. The00 and
01 states occur just once, and the10 endpoints are different because u
is retained. States in different sectors are distinct. This proves
self-avoidance of the whole path.

The coordinate b is absent at X_0,X_1, present at X_2,...,X_(q+1), and
absent at X_(q+2). Its positive lower run therefore has exactly q states.
Because all lower states are distinct and Phi is a perfect matching,
all intervening upper owners Phi(X_i) are distinct too. Their b-run is
exactly the q+1 owners indexed1,...,q+1. The first neighboring owner lacks
b, and any further Phi-directed continuation cannot immediately reinsert
b: that would repeat the last upper owner. Thus this is a controlled
minimal upper run, not just a lower estimate on residence.

## 6. Exact endpoints and what cannot yet be claimed

The full endpoint family is parameterized by the two initial aged deletions
d,e and the q-2 subsequent aged deletions. Put

    K_0=L+u-d-e,
    K_j=K_(j-1)+kappa(K_(j-1))-delta_j,  1<=j<=q-2.

Then the old endpoint is exactly

    L_out=K_(q-2)+kappa(K_(q-2)).                      (6.1)

This formula makes the output concrete. It does **not** prove that a
prescribed old successor can be attained. To land at a named old T, the
deletion choices must satisfy the actual equation (6.1)=T, as well as
their ages. There is no independent relabeling of the output and no
unproved Hall assertion.

The full truncated age vector is an exact boundary invariant: every
continuation deleting only age-q coordinates preserves the run guarantee.
Returning to10 also restores the identity (3.1) for the next old step,
and a is already old enough. But a predetermined parent successor may
delete a coordinate made young by this excursion. Matching the output
state AND this age vector to the next prescribed piece remains necessary.

The controlled b-run is the known necessary geometric ingredient for a
singleton host in a q/q+1-window compiler. It is not by itself permission
to cap that source position to {b}: the lower q-window row has its own
retained-coordinate gap requirement, and simultaneous caps still require
an actual compiler proof. No complete target-prefix deck, arbitrary old
upper witness, or lower-target palette is claimed preserved by this path.

Finally, disjoint ownership of many excursions has not been established.
Different ports may select the same00/01/11 states, and splicing a detour
into an existing parent cycle can orphan its bypassed old states. The
remaining all-r task is an integral sector allocation with the endpoint
and age constraints, followed by all-rank compilation and a safe opening.

The positive local result avoids both defects of the simplest attempt:
its inserted block is not frozen throughout, and its new coordinate has
exactly the useful minimal run. It does not close those global tasks.

## 7. An injective parent-following entrance and the precise next collision

The first two adjacent-rank sectors admit a stronger simultaneous statement
when the input is an actual q-resident old Phi factor with successor sigma.
For this corollary the child's incoming old-coordinate ages must agree with
or dominate those in that parent history. One concrete way to ensure this
is to lift the actual parent predecessor history with the balanced10 block
held fixed. An unrelated valid child age history is not sufficient for
choosing the parent's prescribed deletion.
Write

    sigma(L)=Phi_old(L)-d(L).

At each root-aligned port L=0D choose the initial deletion d=d(L), rather
than choosing an unrelated aged coordinate. The resulting00 and01 states
in (5.1) have old parts exactly

    Phi_old(L),    sigma(L),                            (7.1)

respectively. Both maps are injective over the entire old factor, hence
also over every subset of fixed-root ports. Thus these00 and01 states
have no inter-port collisions. This closes their ownership constraint
without a new matching argument or numerical census.

It is compatible with the age rule. The parent deletes d at age at least
q, and the child delays this deletion by one step. For the third step one
may choose e=d(sigma(L)). Since q>=2, the parent cannot delete the newly
inserted u on its next transition. Hence e belongs to L minus{d}.
Its age at sigma(L) is at least q, so its age at L is at least q-1;
the child deletes it two steps later, at age at least q+1.

This e can have initial age q-1, so this is an additional permissible
choice beyond the simpler sufficient initial-age-q selection in Section5.
The rest of that proof is unchanged. The first11 old part becomes

    K_0=sigma(L)-d(sigma(L))
       =sigma(L) intersect sigma²(L).                  (7.2)

Therefore the next exact ownership issue is the multiplicity of the
specified parent-facet map (7.2) on the root-aligned ports, followed by
collisions among the internal11 paths. Equation (7.1) must not be
discarded into a generic Hall hypothesis; those two maps are already
injective. Equation (7.2), however, has not been proved injective.

There is a small local warning against inferring (7.2) from Phi alone.
On seven sites labelled0,...,6, with common old root0, consider

    {1,2,3} -> {0,1,3} -> {0,3,6},
    {1,3,4} -> {0,3,4} -> {0,2,3}.                    (7.3)

The four outgoing Phi owners are, in the same order,

    {0,1,2,3}, {0,1,3,6}, {0,1,3,4}, {0,2,3,4}.

Their first-minimum roots are0,6,0,2 respectively, so every displayed
edge is a legal canonical-Phi step. All six lower vertices and all four
upper owners are distinct. The newly inserted root0 survives the next
transition in both paths, but both specified successor facets are{0,3}.
Balanced Dyck-block insertion embeds these same finite canonical edges
in larger old ranks, by Section3.

This is a compatible local partial-matching pattern, not a proof that
both paths extend to a complete globally q-resident Phi factor. It
demonstrates exactly why the local canonical identities and open-path
residence check do not themselves prove facet injectivity. No global
counterexample or impossibility assertion is made from (7.3).

## 8. Independent internal review

`exact_equality_structure` independently read and passed Sections2--6,
including all three forced prefix minima, the aged-choice count, q=2,
self-avoidance, endpoint ages and the minimal upper b-run. In particular,
the last upper owner equals A_out+b, so injectivity of Phi alone forbids
an immediate reinsertion of b after exit. This was a pure proof review;
no mathematical program was run. Section7 was added subsequently and is
not included in that prior review status.

The same reviewer subsequently passed Section7's algebra and local
collision example, and identified the parent-age compatibility hypothesis
now stated at its start. With that hypothesis the prescribed deletions are
age-valid. Section9 below was added after that review.

## 9. The exit map is itself an explicit injection

For an arbitrary old rank-(r-1) state K on2r+1 sites, let kappa(K) be
the zero at its first global prefix minimum, and define

    J(K)=K+kappa(K).                                    (9.1)

This is exactly the old-coordinate output in the final11-to10 step.
It is injective, with an explicit inverse. In fact its image is precisely
the old rank-r words whose fixed-cut prefix minimum is at most-2.

To prove this, let m be K's global minimum and let j be its first
attainment. The total old height is-3, so m<=-3. Flipping that zero
raises all prefix heights from j onwards by2. Before j the old heights
are at least m+1 and the height at j-1 is m+1. From j onwards the new
heights are at least m+2. Thus J(K) has minimum m+1, and its LAST
attainment is exactly j-1. Recover j as the next up-step and delete it
from J(K). This recovers K uniquely.

Conversely, let a rank-r word Y have minimum g<=-2. Its total height
is-1>g, so its last minimum occurs before the end, followed by an
up-step j. Flip that step to zero. The resulting K has total height-3;
before j its height is at least g, at j it is g-1, and afterwards it is
at least g-1, because Y never revisits g after its last minimum. Hence
j is K's first global minimum and J(K)=Y. This proves the asserted image
and inverse without a matching-existence assumption.

Consequently, if several excursions have distinct final11 states, their
output10 states are automatically distinct. The output collision problem
is exactly the collision problem for those final11 states; no separate
arbitrary endpoint assignment is necessary. Furthermore protected u is
present in every output, whereas it is absent in EVERY initial fixed-root
port0D, so the entire output bank avoids the entire initial port bank.

For all fixed-root ports there are Cat_r initial states. Under the
parent-following entrance, Section7 gives exactly Cat_r distinct00 states
and Cat_r distinct01 states. The proposed excursions use (q-1)Cat_r
11 occurrences. Whether those occurrences can be made distinct is still
unproved: already the prescribed first11 facet map can collide, and later
legal age-buffer walks can meet. This is an explicit ownership problem
inside one specified rank sector, not a new conclusion from scalar counts.

The inverse in (9.1) does not solve prescribed old successor matching:
to demand output T requires that the buffer terminate at the unique
J-inverse(T), which exists only for the stated minimum class. The age
history at that endpoint remains part of the interface.

Independent internal review: the structure agent read Section9 and passed
the first/last-minimum inverse, its exact image, the distinct-exit
consequence, and separation from all fixed-root entrances. This is a
pure-proof review, not external certification; no computation was run.

## 10. The one fixed actual19 entrance diagnostic

The reviewed checker was executed once on h100 under the root's explicit
30CPU/45wall/1GiB/128MiB-file authorization. At all 4,862 bit0-root ports
of the supplied optimal19 period, the three prescribed entrance steps
pass Phi and parent-history age checks. Both00 and01 maps are injective.
The first11 map has 4,487 distinct images: 4,112 singleton images and375
images with two providers. Thus using every prescribed entrance with
distinct child owners is impossible. This does not rule out alternate
deletions, port subsets, or a dimension21 construction; none was tested.

The complete proof-scope, counts, source hash, execution log and all375
collision pairs are recorded in
[the fixed-port certificate](K19_FIXED_ROOT_PRESCRIBED_PARENT_SECTOR_PORT_CERTIFICATE_20260909.md).
This is the only mathematical execution associated with this note.
