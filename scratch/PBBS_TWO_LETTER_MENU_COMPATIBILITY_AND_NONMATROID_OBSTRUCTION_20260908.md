# Pinned two-letter menus: exact compatibility, a genuine bank counterexample, and sound relaxations

2026-09-08. Pure-proof note by `exact_b_induction`; no mathematical
computation was run for this note. The fixed-bank source, pin, anchor,
and rank statements are from
`PBBS_EXACT_SHORT_TARGET_CAPS_AND_CAPACITATED_MATCHING_REDUCTION_20260908.md`,
`PBBS_CAPPED_APERTURE_EXACT_MIDDLE_AND_LOWER_PIN_INTERFACE_20260908.md`,
and the completed catalogue
`K17_TRIPLE_PRESERVING_SHORT_HOSTS_AND_CANONICAL_ANCHOR_MENU_CERTIFICATE_20260908.md`.
All were read for this task. The finite catalogue counts below are
attributed to that executed certificate, not to a new execution.

The result is an exact constructive block rule and an obstruction to
independent-slot or matroid-exchange reasoning. It does not assert a
complete capped bank or a length-B(17) word.

## 1. Every two-position block has three distinguishable output channels

Take adjacent native H=3 letters D and F. Each has size six and their
union has size seven. Write

    D=K union {a},   F=K union {b},   |K|=5,   a != b,

where a,b are not in K. Let their forced pins be P and Q. The source
run ending at the first position forces a into P; the source run
starting at the second forces b into Q. Thus

    a in P subset D,    b in Q subset F.

With full anchors on either side of the editable block, every pair of
caps

    P subset E subset D,    Q subset G subset F             (1.1)

preserves all native triples simultaneously with all other legal block
choices. Both pairs touching an anchor remain their original rank-seven
targets. The only variable lower targets of this block are

    E, G, E union G.                                        (1.2)

These three outputs are ALWAYS distinct. Their channels can be read
from membership of a,b:

* E contains a and omits b;
* G contains b and omits a;
* E union G contains both a and b.

Consequently a specified target has at most one possible output channel
in a given two-position block. This is useful for a necessary channel
matching, but does not make the choices in the three channels
independent. A full menu uniquely determines both literal caps E,G.

## 2. Exact compatibility and a constructive companion rule

The following tests are necessary and sufficient for prescribed
channel outputs. Unspecified channels are free to take other values.

For a left literal A alone, the test is P subset A subset D; choose
E=A and G=F. For a right literal B alone, use Q subset B subset F.
Prescribing both literals imposes only those two individual tests;
their union output is then A union B.

For a pair target U alone, the exact test is

    P union Q subset U subset D union F.                   (2.1)

One explicit realization is

    E=D intersect U,   G=F intersect U.                    (2.2)

For a left literal A and pair target U simultaneously, the exact test
is (2.1), P subset A subset D, and A subset U. The explicit companion is

    E=A,   G=F intersect U.                               (2.3)

To check the union equality, U minus F is exactly {a}, since a belongs
to P subset U. That coordinate is already in A. Every other coordinate
of U is supplied by F intersect U. This proves E union G=U. The
right-literal version is symmetric.

Finally, three prescribed outputs A,B,U are compatible exactly when

    P subset A subset D,   Q subset B subset F,
    A union B=U.                                          (2.4)

Thus inserting a new left target while keeping a named pair target is
constructive and involves no new coordinates or added positions. It
may change the right literal. If that right literal is also required
at this block, its preservation is precisely the additional equation
in (2.4); it is not supplied by separate host tests.

A useful conditional interpolation is the following. Suppose the
current pair target U must remain, the new left target A is eligible
and lies in U, and the current right literal is G. Then

    E'=A,   G'=G union (U minus A)

is a valid pair preserving U. Indeed U minus A lies in F because A
contains the only coordinate a of U outside F. This version retains
every coordinate of the former right literal, although it need not
retain that literal as an exactly equal one-letter target.

## 3. A counterexample inside the actual canonical anchor frame

Use the canonical height-eight component, cycle0 in
`k17_height_adaptive_20260908/height_adaptive_canonical_cycles.json`.
Coordinates in this paragraph are zero-based. The displayed stored
owners give, by direct set intersection,

    D_i={8-i,9-i,...,13-i} modulo17.

In the fixed anchor frame 0,3,6,..., the first editable block consists
of positions1,2, between full anchors0 and3. Its letters and pins are

    D_1={7,8,9,10,11,12},   P={7,12},
    D_2={6,7,8,9,10,11},    Q={6,11}.

The private channel coordinates are a=12 and b=6. Consider the three
small targets

    A={7,8,12},
    B={6,9,11},
    C={6,7,10,11,12}.

They pass all individual host tests:

* A is an eligible left literal.
* B is an eligible right literal.
* C is an eligible pair target; for example choose
  E={7,10,12}, G={6,11}.

All these choices are nonempty pinned caps and preserve every native
triple with the fixed anchors. A can use only the left channel because
it contains12 but not6. B can use only the right channel. C contains
both private coordinates, so it can use only the pair channel.

An independent target-to-channel flow therefore assigns A,B,C to all
three channels integrally. But no one block option realizes all three:
the literal requirements force E=A and G=B, whose union is

    {6,7,8,9,11,12} != C.

This is a concrete failure of lifting an integral **relaxed channel
assignment** to one compatible menu. It is not a claim about the
integrality gap of an unspecified configuration linear program.

There is a stronger structural warning. Define a demand family to be
independent when one cap pair covers all its targets in this block.
This family is hereditary. Both I={C} and J={A,B} are independent, and
|I|<|J|. Yet neither I union {A} nor I union {B} is independent: retaining
pair C forces both literal caps to lie inside C, whereas A contains8
and B contains9, both outside C. The matroid exchange axiom therefore
fails on this actual catalogue block.

The entire unchanged bank has no targets of these ranks, and anchor
letters have rank six. Thus these local tests are not concealing a
second short witness crossing an anchor. Other editable blocks in a
future global solution may of course supply A,B,C separately. The
counterexample is not a no-go for covering the whole bank.

## 4. Exact global constraints and sound propagation

Let O be the fixed target palette: frozen components, full anchors,
and the preserved pairs touching anchors. For each block b let
mathcal M_b be its exact menu domain. A one-position menu has one
output; a two-position menu has the three outputs in (1.2). The
fixed-bank problem is precisely

    choose M_b in mathcal M_b for every block,
    every required target outside O belongs to some chosen M_b. (4.1)

All native triples and longer ORs are already guaranteed by the menu
construction. There is no additional simultaneous cap-feasibility
constraint between these anchor-separated blocks.

The following deterministic propagation rules are sound:

1. A target with no surviving provider block proves contradiction.
2. If a target has exactly one provider block, require that target in
   that block and delete every option not containing it.
3. Accumulate all such requirements on a block and filter by their
   conjunction, never by checking each requirement against a different
   option. An empty required block domain proves contradiction.
4. Repeat until no support changes. Provider support means existence
   of at least one remaining option, counted by distinct blocks rather
   than by number of options or channels.

These implications follow from (4.1) and preserve every possible
complete selection. A replay certificate can list each newly unique
provider and the resulting domain restriction; a zero-support target
or empty domain is a finite exact contradiction.

After propagation, a flow from targets to physical output channels,
capacity one at every channel, is a necessary relaxation: choose one
witness channel for every target in any actual solution. Section3
shows why flow saturation would still not be sufficient. A deficient
flow would nevertheless be a valid obstruction to this fixed frame.

For bank coverage alone it is also safe to remove a block option whose
set of nonfixed required outputs is contained in that of another
remaining option. Keep one literal representative when these sets are
equal. Replacing the smaller set by its superset cannot lose any
required target or disturb the preserved native triples. This reduction
is scoped to (4.1): different literal representatives may matter to a
separate later chronological splice, which has not been incorporated.

## 5. A stronger Hall relaxation that respects whole menus

For any specified target family T outside O, define

    c_b(T)=max_(M in surviving mathcal M_b) |M intersect T|.

Every complete selection must satisfy

    |T| <= sum_b c_b(T).                                  (5.1)

Proof: count each target at one selected provider block; each selected
menu contributes at most its intersection size with T. Summing may
double-count actual coverage, so the result is an upper bound and is
therefore necessary.

This uses simultaneous compatibility within each block and is at
least as strong as replacing c_b by the number of its channels that
individually have a T-host. It is inexpensive to certify for one fixed
T from the saved finite domains. The previous explicit 1,768-target
Hall family is one already specified candidate; testing it would not
require a random family search. No such additional test was run here.

More generally, for any nonnegative rational weights w_t,

    sum_t w_t <= sum_b max_(M in surviving mathcal M_b)
                              sum_(t in M outside O) w_t. (5.2)

Failure yields an exact finite weighted certificate. This is a valid
dual bound even though the local feasible-demand system is not a
matroid. It does not assert that every failure of (4.1) is detected by
a particular untested set of weights.

## 6. What a legal local augmentation must preserve

For a current selection, fix a block b and let R_b be the targets in
its old menu not supplied by O or by another selected block. Replacing
the block preserves all previously covered targets exactly when its
new menu contains R_b. This condition is sufficient and necessary;
it is the appropriate test for a monotone one-block augmentation.

The private-channel rule and Section2 make the test explicit. If both
old literal targets are private to this block, retaining them fixes
both letters and therefore fixes its pair. If only its pair U and
left literal A must remain, a new right literal B is permitted exactly
when it has the right pins and A union B=U. The other cases are the
corresponding exact tests of Section2.

For a simultaneous change on a set of blocks B, remove their old
contributions and regard everything outside B as a fixed palette O_B.
The new options must cover every old required target outside O_B,
together with the desired additional targets. This is a finite
configuration-cover subproblem on B, not automatically an ordinary
alternating path. The non-matroid example shows why a blanket promise
to insert a fresh target while retaining all old local outputs is false.

The useful positive result here is the literal companion construction
(2.3), and its exact compatibility conditions when other outputs are
protected. A complete bank selection remains undecided by this note.
Even a successful selection would still leave the separate task of
putting the components into one linear chronology of length24,313;
the total24,310 cyclic positions do not include free closing collars.
