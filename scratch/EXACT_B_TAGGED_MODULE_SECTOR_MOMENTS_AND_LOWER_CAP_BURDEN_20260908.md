# Tagged-module sector moments, divisibility, and the exact lower-cap burden

2026-09-08. Pure derivation; no mathematical program was executed.

Status: proved necessary equations and restrictions for a specified module
bank, plus an explicit legal capping operation. Neither an integral complete
middle-layer partition nor an all-dimensional attaining word is supplied.
The decisive conclusion is a no-go theorem for the specified **frozen flat
owner chronology**: even arbitrary antecedent changes respecting its
protected neighboring owners cannot produce a length-B(17) universal word.
The allowed pulse cap changes occurrence counts but does not escape that
permitted-label obstruction.
Section 5 first treats literal width-three preservation. Section 7 proves
the stronger protected-endpoint restriction, which also applies to arbitrary
common-cap shrinking while the stated envelope and owner requirements are
fixed. Common-cap shrinking is permitted, but removing a repeated occurrence
need not create any new target at its endpoint.

## 1. The architecture under examination

Fix three hubs a_0,a_1,a_2 in a k-coordinate ground set, and put v=k-3.
The remaining v coordinates are called nonhubs. Fix owner rank R and owner
window width q=d+1. Each primitive tagged module has:

* a permanent nonhub core K of size R-q-1;
* N-1 distinct nonhub positional symbols, together with one
  distinguished next hub a_(i+1), making N distinct positional symbols;
* N>q, with one old cycle for each permanent hub a_i; and
* exactly the tagged source form of EXACT_B_TAGGED_CONTEXT_FUSION_20260908.md.

More explicitly, after removing the permanent a_i and K, the old cycle is
a cyclic ordering of N distinct symbols, one of which is a_(i+1), and all
others are nonhubs. One nonhub symbol is the L-screen coordinate c. The
other N-2 symbols occur in the C,D context positions, whose source letters
contain K. The screens contain no K. Assume q>=4; then every window of
width q or q-1 contains a context position, so its union contains K.

The width-q owners consequently have rank R. Exactly q of the N owners
contain the next hub, while N-q contain only the permanent hub. The
width-(q-1) intervals have rank R-1, with q-1 double-hub occurrences and
N-q+1 single-hub occurrences. These assertions are occurrence counts and
do not assume a global partition.

Consider a collection of M such three-cycle modules, with periods N_j,
which partitions all rank-R targets having exactly one or two of the
three fixed hubs. No zero-hub or three-hub target is assigned to this bank.
All equations below concern this explicit complete mixed-hub partition.

## 2. Exact middle-sector equations

Put

    A=binom(v,R-1), B=binom(v,R-2).

There are A targets for each singleton hub and B for each unordered hub
pair. In a three-cycle module each unordered hub pair is used by exactly
one old cycle. Hence a complete mixed-sector partition must satisfy

    q M = B,
    sum_j (N_j-q) = A,
    sum_j N_j = A+B.                                      (1)

In particular, q must divide B. Mixing periods cannot change this condition.
It depends only on the single occurrence of the next hub in each primitive
old source cycle, not on how its base coordinates are ordered.

At k=17,R=9,q=4,

    A=binom(14,8)=3003,
    B=binom(14,7)=3432,
    M=858, sum N_j=6435.                                  (2)

If only periods seven and eight are used, their counts are necessarily

    M_7=M_8=429.                                          (3)

These are necessary integral counts, not a construction of the named
target partition.

At k=19,R=10,d=3,q=4, one instead has

    B=binom(16,8)=12870,

which is not divisible by four. Therefore no period mixture of this fixed
three-hub, fixed-width module architecture can partition its entire mixed
middle sector in dimension 19. This does not rule out varying hub sets,
exceptional owner widths, partial modules, or another source form in which
a hub has a different residence count.

## 3. Point-incidence equations beyond the total counts

For a module, list the N-1 nonhub positional symbols in their linear order
after the distinguished next-hub screen, as z_1,...,z_(N-1). Define

    u_N(t)=max(0,min(t,N-q)-max(1,t-q+1)+1),
    v_N(t)=[q-t]_+ + [q-(N-t)]_+.

The symbol z_t occurs in exactly u_N(t) single-hub owner windows and
v_N(t) double-hub owner windows. Their sum is q. A core coordinate occurs
in all N-q single-hub and all q double-hub owners.

Consequently every nonhub coordinate x must satisfy both named point rows

    sum_(j:x in K_j) (N_j-q)
       + sum_(j:x=z_(j,t)) u_(N_j)(t) = binom(v-1,R-2),

    q * #{j:x in K_j}
       + sum_(j:x=z_(j,t)) v_(N_j)(t) = binom(v-1,R-3).       (4)

These equations are independently checkable from the cyclic interval
incidence. Adding them gives the useful congruence

    sum_(j:x in K_j) N_j = B mod q.                         (5)

Here a nonhub coordinate not used in a module contributes zero, and a
positional coordinate contributes q to the sum of the two rows.

For the k=17 seven/eight mixture, the two right sides of (4) are both
1716, and

    u_7=(1,2,3,3,2,1), v_7=(3,2,1,1,2,3),
    u_8=(1,2,3,4,3,2,1), v_8=(3,2,1,0,1,2,3).

Equation (5) requires every nonhub coordinate to belong to a multiple of
four of the 429 period-seven cores. Their total core-incidence count is
4*429=1716. Therefore these cores cannot have uniform degree across the
14 nonhub coordinates, since 1716 is not divisible by 14. In particular,
any selected module bank invariant under a coordinate-transitive action on
the nonhubs, preserving the period types, is impossible.

This is a symmetry restriction and an exact set of point equations. It
does not assert that all named-target equations are satisfiable, nor does
it identify the point equations with a sufficient design criterion.

## 4. The adjacent-rank occurrence imbalance

Under the middle-sector equations (1), the old bank has, for each permanent
hub, exactly

    sum_j (N_j-(q-1)) = A+B/q                              (6)

single-hub rank-(R-1) interval occurrences. There exist only

    binom(v,R-2)=B

distinct targets of that type. Thus each hub forces at least

    E=[A+B/q-B]_+                                         (7)

repeated occurrences in this one fixed-width row. This is an occurrence
pigeonhole count; it does not rely on independence or on an assumed design.

In odd dimension k=2r+1 with R=r+1,

    A/B=(r-1)/r,
    E=[B(1/q-1/r)]_+.

At k=17, (6) is 6435-3*858=3861, while B=3432. Therefore

    E=429 per hub, or at least 1287 repeats in total.       (8)

The conclusion holds for every period mixture satisfying (1), not just
429 periods of each of seven and eight. At width three the double-hub
bank simultaneously has only 3*858=2574 occurrences per unordered pair,
whereas the complete rank-eight double-hub sector has binom(14,6)=3003
targets. Its deficit of 429 per pair is the opposite side of the same
type imbalance. Additional sources or changed interval labels are needed;
middle count balance alone does not close the adjacent rank.

## 5. Literal preservation obstruction and precise capping burden

The following endpoint fact is useful. If a length-n word covers all W_s
targets of rank s, and a selected collection of fixed-width cells has D
repeated target occurrences beyond its distinct labels, then

    n >= W_s + D.                                         (9)

Indeed, those cells have distinct right endpoints. At one right endpoint
all interval ORs form a chain, so that endpoint can represent at most one
rank-s target. The D repeated endpoints cannot supply another rank-s
target; the n endpoints can therefore cover at most n-D different targets.

Apply this to a larger cyclic source which retains the module bank's
literal width-three occurrence multiset, even if the bank supplies only
its mixed-hub sector. The bank's repeated rank-eight count is at least
1287. Cutting the cyclic word once and taking one traversal destroys at
most two width-three cells. Adding prefix/suffix collars cannot remove
surviving occurrences. Hence, if no other old rank-eight cell is changed,
the resulting linear word retains at least 1285 repeated rank-eight
occurrences and, if universal, must have length at least

    24310+1285=25595.                                     (10)

If the opening retains every cyclic width-three cell, the bound is instead
24310+1287=25597. Neither statement assumes that the larger source's
period equals the mixed-sector bank's size.

For a length-24313 universal word, the fixed-width repeat budget is only
24313-24310=3. To reach it, at least 1284 of the originally forced repeated
cell occurrences must be removed or changed to another label. A single
cut can account for at most two; at least 1282 additional cells must then
change. If every cyclic width-three cell survives the opening, at least
1284 cell labels must change. A change to one old physical source letter
can affect at most three old width-three cells, so a shrink-only correction
with fixed occurrence addresses must edit at least 428 source positions.

Scope of Section 5 alone: its occurrence-removal argument concerns
retaining the old literal width-three row. A common-cap compiler may
shrink rank-eight intervals while preserving every width-four middle
owner, and the next section supplies a concrete legal shrink operation.
However, Section 7 proves that under the frozen envelope/owner hypotheses
such shrinking cannot change the rank-eight label permitted at an endpoint;
that stronger obstruction remains even after occurrences disappear.
Surgeries that change adjacency can alter the permitted labels and old
cell addresses. The source-position lower bound in this section is
explicitly limited to fixed-address letter shrinking.

## 6. Explicit legal pulse cap on a period-seven module

In a k=17 primitive period-seven cycle, index positions modulo seven with
the R screen at position zero. Its L screen is at some other position.
Choose one core coordinate kappa in K. It originally occurs at all five
context positions and at neither screen.

Among the two pairs of positions

    {1,5}, {2,6},

at least one avoids the L screen; both avoid R, and they are disjoint, so
L cannot block both. Keep kappa only at the two positions of one accepted
pair, deleting it from the other three context letters. Repeat this same
base-letter modification in all three ports of the module.

The two cyclic distances between the retained occurrences are three and
four. Every four-position window therefore retains kappa, so every
rank-nine owner is exactly unchanged. The only three-position window
which loses kappa is the unique gap of length three. For the two choices
its positions are respectively {2,3,4} or {3,4,5}; neither contains R.
It is consequently a single-hub rank-eight interval, which shrinks to
rank seven. All other width-three interval labels remain unchanged.

Source letters remain nonempty because their tag and positional symbol
remain. The new base words still have the tagged-context form, so the
fusion theorem remains applicable to the capped bank. Since every
width-four owner is unchanged, every source interval of width at least
four also has the same union: it is a union of its consecutive
width-four owner windows. This holds in the fused word as well: its
per-width interval correspondence depends only on the screen positions and
fringe offsets, so each new width-four owner maps to the same unchanged
old width-four owner before and after capping.

For a putative 429+429 period mixture, applying this operation to all
429 period-seven modules shrinks exactly 429 single-hub rank-eight
occurrences for each hub, 1287 in total, with no loss of middle owners
or upper source targets. Thus there is an explicit capping freedom large
enough to meet the numerical occurrence-removal count in Section 5. It
does not meet the permitted-label requirement in Section 7.

This does not prove named rank-eight coverage. The retained 3432
single-hub rank-eight occurrences per hub can still repeat some targets
and miss others. The pulse cap also does not create the missing 429
double-hub rank-eight targets per pair. It fixes the type totals, but
Section 7 shows that each removed rank-eight occurrence becomes a
rank-eight-dead endpoint under the frozen owner/envelope requirements.
Consequently this pulse operation does not repair the endpoint capacity
obstruction for that fixed chronology.

## 7. Protected endpoints: shrinking cannot create a different face

### Lemma 7.1 (permitted-label endpoint bound)

Let E be a fixed source envelope, let A be any word with A_i subseteq E_i,
and let p be a right endpoint with a prescribed length-q owner ending there.
Suppose

    OR_E([p-q+2,p])=S_p, |S_p|=R-1,
    OR_A([p-q+1,p])=T_p, |T_p|=R.

Then every rank-(R-1) interval of A ending at p, if any exists, has label
exactly S_p.

Indeed, a suffix of length at most q-1 is contained in the displayed
envelope suffix, so its OR is a subset of S_p and can have rank R-1 only
by equaling S_p. A suffix of length at least q contains the prescribed
rank-R owner and cannot have rank R-1.

Now let P be any collection of distinct protected endpoints satisfying
these hypotheses, and put

    D_P=|P|-|{S_p:p in P}|.

If A covers all W_(R-1)=binom(k,R-1) targets of rank R-1, then

    n >= W_(R-1)+D_P.                                    (11)

The protected endpoints together can supply at most their |P|-D_P
permitted labels. Each remaining endpoint can supply at most one further
rank-(R-1) label. This proves (11), even when some or all protected
endpoints cease to represent S_p after capping. Their missing occurrences
do not increase the list of labels those endpoints are allowed to serve.

### Owner-pair version without a separately fixed envelope

The same conclusion holds for every antecedent of two prescribed neighboring
rank-R owners

    T^- = OR_A([p-q+1,p]),
    T^+ = OR_A([p-q+2,p+1]),

whenever T^- intersect T^+=S_p has rank R-1. The overlap suffix
[p-q+2,p] is contained in both owners, so its OR is a subset of S_p;
the rest of the proof is unchanged. This version permits any changes of
source letters consistent with the two owner requirements, not just
shrinking a particular initial source.

### Corollary 7.2 (frozen tagged chronology cannot be capped to equality)

Assume the complete mixed-sector bank in Sections 1--4 is incorporated
into a larger flat width-four owner source as follows:

1. its old width-three rank-eight occurrence multiset is transported to
   distinct cyclic source endpoints;
2. every corresponding width-four owner has rank nine, and these owners
   remain prescribed at their physical positions during capping; and
3. the final capped source is below an envelope whose protected
   width-three suffix labels remain those old rank-eight labels, or the
   neighboring distinct owner pairs fix the same rank-eight faces.

Then the bank contributes permitted-label excess at least 1287. In the
envelope version, a single opening can discard at most three original
protected endpoint constraints near its cut: at every other endpoint both
the old length-three suffix and length-four ending owner remain wholly
inside the traversal. Prefix or suffix additions leave the retained
constraints in force. Hence, under these opening assumptions, every
universal linear result
satisfies

    n >= 24310+(1287-3)=25594.                            (12)

If all protected endpoints are explicitly restored by a copied collar
and their envelope/owner constraints are retained, the stronger bound is
24310+1287=25597. These are architecture-specific lower bounds, not lower
bounds on unrestricted universal words.

For the owner-pair alternative, the following owner must also survive.
If a copied suffix collar retains that owner at the last traversal
endpoint, at most the same three original endpoints are lost and (12)
applies. Without such a collar, discard the last traversal endpoint as
well: at most four constraints are lost and the corresponding bound is
25593. The application requires preserving the physical owner
requirements, not merely an unordered middle-label census.

The rank-eight face condition is automatic at an interior old bank cell
whenever its neighboring width-four owners are distinct rank-nine sets:
their intersection contains its old rank-eight width-three union, and two
distinct rank-nine sets cannot have an intersection larger than eight.
Thus that union is precisely their intersection. The tagged per-width
fusion retains the rank-eight suffix and the globally distinct rank-nine
owner multiset, so it retains this local face property wherever the bank
is transported into such a flat source.

At n=24313, inequality (11) permits excess at most three. Therefore at
least 1284 old endpoint permissions must cease to be the same repeated
singleton-label lists. A cut can eliminate at most three, leaving at least
1281 further protected endpoint constraints to change under the conservative
opening convention. Merely deleting rank-eight occurrences by shrinking
does not accomplish this: Lemma 7.1 keeps the same permitted label, while
possibly making that endpoint serve no rank-eight target at all.

The period-seven pulse cap in Section 6 illustrates precisely this
distinction. At its changed endpoint the shorter suffixes also have rank
at most seven, and the prescribed four-window still has rank nine. The
endpoint becomes rank-eight-dead. The cap preserves every upper owner
requirement but cannot add a missing rank-eight face.

Thus the fixed pure-module chronology requires substantial changes to its
permitted adjacent-rank faces, for example by changing owner transitions
or by adopting a different source/module family. An integral middle-layer
partition followed only by deck-preserving tagged fusions and common-cap
shrinking cannot close the exact construction under the stated hypotheses.
Varying hub sets, partial modules, other owner schedules, and non-flat
chronologies remain outside this obstruction.

## 8. Relation to previous fractional rail results

The older unified rail-queue theorem already supplies local simple owner
cycles and full-rank fractional marginal equations. The uniform-block
chainization note explicitly separates those from literal serialization,
and the KLP-interface obstruction prevents a direct exact-rounding claim
on the full named-owner space. None is used here as an integral existence
theorem.

The new content is specific and finite: the fixed-hub divisibility law,
the k=19 failure of that law, the k=17 period and point-incidence rows,
the adjacent-rank type imbalance, its endpoint-based preservation cost and
the protected-endpoint strengthening for frozen owner/envelope data,
and a literal pulse cap which alters precisely the required type of
lower cell while retaining the middle and every upper window.

The next exact construction must solve the named interval partition and
alter enough of the coupled adjacent-rank permissions. A complete mixed
middle partition followed solely by the preserved flat chronology and its
common-cap compiler cannot attain B(17) under Section 7's hypotheses.
Period mixing or symmetry averaging alone does not change that conclusion.

Review record: exact_b_induction independently checked Sections 1--6 in
`EXACT_B_TAGGED_MODULE_LOWER_CAP_BURDEN_INDEPENDENT_AUDIT_20260908.md`.
After Section 7 was added, root read it in full and checked the
permitted-label proof, its owner-pair alternative, and the conservative
three/four lost-constraint counts. These are internal mathematical reviews,
not external verification or an all-dimensional equality claim.
