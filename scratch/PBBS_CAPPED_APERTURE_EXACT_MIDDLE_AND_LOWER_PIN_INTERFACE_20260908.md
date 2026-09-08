# Capped PBBS apertures: exact middle witnesses and a lower-target interface

2026-09-08. Independent pure-proof note by exact_equality_structure.
No mathematical computation was run. This gives a concrete cyclic source
bank and exact permitted local edits; it does not construct a B(17)-word.

The inputs are the proved height/residence and strict-corridor statements
in PBBS_HEIGHT_ADAPTIVE_FINITE_WORD_AND_RANGE_BOUND_INDEPENDENT_AUDIT_20260908.md
and PBBS_STRICT_HEIGHT_CORRIDOR_AND_INTERLEAVED_HEIGHT_INDEPENDENT_AUDIT_20260908.md.
The endpoint argument is MASTER_HANDOFF.md Section 2, also recorded in
EXACT_B_CRITICAL_INTERVAL_RIGIDITY_20260908.md. All three scratch notes
were read in full for this audit. Section 8 below separates the new
conclusions from these inherited inputs.

## 1. Exact ranks of every short source interval

Let n=2r+1, let A_i be one physical g=f^2 cycle of period v, and put
X_i=[n] minus A_i. The owners X_i are distinct (r+1)-sets, consecutive
owners are Johnson neighbors, and every positive coordinate run in X
has length at least h+1, where h is the invariant normalized Dyck height.

Choose any integer aperture 1<=H<=h and define

    D_i^H = intersection_(j=0)^H X_(i+j).

Then, for every 0<=q<=H,

    |intersection_(j=0)^q X_(i+j)| = r+1-q.                 (1.1)

Indeed each of the q transitions removes one coordinate. A coordinate
removed in this interval must have been present in X_i: otherwise it
entered after i and then had a positive run of length at most q-1<h+1.
The removed coordinates are distinct for the same reason. Thus precisely
q initially present coordinates disappear from the intersection.

The coordinate-run erosion identities, with H in place of h, are

    union_(j=0)^H D_(i-j)^H = X_i,

    union_(j=0)^(H-q) D_(i-j)^H
       = intersection_(j=0)^q X_(i+j),       0<=q<=H.       (1.2)

A positive owner run [a,b] becomes exactly the positive source run
[a,b-H], which proves these identities coordinate by coordinate.
Combining (1.1) and (1.2), every cyclic source interval of length ell,
1<=ell<=H+1, has exactly

    rank = r-H+ell.                                        (1.3)

Every interval of length H+2 contains the two consecutive owner windows
of length H+1, and their union has rank r+2. Every longer interval has
rank at least r+2 as well. Consequently:

* Every cyclic middle-rank (r+1) witness has length exactly H+1.
* Its label is its corresponding owner X_i.
* Each middle label in this component occurs exactly once per period.
* The literal source has period exactly v: a shorter period would give
  a shorter period for the recovered owner sequence.

The middle witness is inclusion-minimal: removing either endpoint gives
rank r. There is no shorter or longer middle witness hidden elsewhere
in the same cyclic source. Distinct components have disjoint middle
labels because the physical g-cycles partition the middle layer.

## 2. What can remain unchanged in an attaining B(17)-word

Suppose a universal word has length W+d, where W is the number of
rank-s targets. Select one interval witness for each rank-s target.
Order these intervals by left endpoint. Their right endpoints have the
same strict order, and the i-th selected interval lies inside [i,i+d].
Two consequences hold without assuming flat middle windows:

    EVERY rank-s physical witness has length at most d+1;    (2.1)

    EVERY physical interval of length at least d+1
    has rank at least s.                                   (2.2)

For (2.1), include the particular witness under consideration in the
selected family. For (2.2), an interval of length d+1 starting at a
contains the a-th selected witness; its possible starts satisfy a<=W.
Longer intervals contain one of these intervals.

At k=17, s=9, W=24310 and B(17)=W+3. Thus every middle witness has
length at most four, and every four-letter OR has rank at least nine.

The native height-adaptive source uses H=h. By (1.3), when h>=4,
every four-letter OR has rank 12-h<=8. Therefore:

    No four consecutive unchanged letters of a native
    height-h>=4 source can occur in a B(17)-attaining word. (2.3)

In particular these cycles cannot be retained as literal periods or long
literal blocks. Their native middle witnesses have length h+1>=5,
also excluded by (2.1). Even an entrywise reduction of these letters
cannot fix their deficient four-letter ranks: reduction only lowers ORs.
Fragments of at most three letters are not ruled out by this argument;
their seams still have to satisfy the global target and endpoint budget.

Native cycles of heights h<=3 have middle witness length h+1<=4, so
they pass this particular local rank test. This is not a statement that
they can all be opened and concatenated at a total cost of three letters.

The aperture replacement H=min(h,3) is a genuine recoding: D_i^H contains
D_i^h, so it enlarges source letters and removes the old long flat middle
windows. It is not an entrywise cap of the original height-h source.

## 3. A complete capped source bank on seventeen coordinates

On every g-cycle choose H_C=min(h_C,3), and retain its entire cyclic word
D^H. The total number of cyclic source positions is exactly W=24310.
The bank contains every rank-nine target exactly once as a cyclic
interval, of length H_C+1, and every letter is nonempty.

Its exact short rank rows are:

| component height | aperture | letter rank | pair rank | triple rank | four-window rank |
| --- | --- | --- | --- | --- | --- |
| 1 | 1 | 8 | 9 | at least 10 | at least 10 |
| 2 | 2 | 7 | 8 | 9 | at least 10 |
| at least 3 | 3 | 6 | 7 | 8 | 9 |

The cyclic bank covers ALL targets of ranks six through seventeen.
Here is the exact transfer, which also identifies usable witnesses.

For a nonempty lower target S of rank r-q, the strict corridor gives
B_0,...,B_q of height h>=q+1 with intersection S. On its interleaved
component there are q+2 upper owners whose intersection is S. If
q<=2, then H=min(h,3)>=q+1, so (1.2) supplies S by an interval of length

    H-q.                                                   (3.1)

At r=8 these are exactly ranks eight, seven and six. All middle owners
give rank nine. For every upper target S^c of rank r+1+q, the original
corridor gives q+1 upper owners with union S^c. The exact owner identity
gives their union as a source interval of length

    H+q+1,      0<=q<=r-1.                                 (3.2)

Unlike an intersection witness, this union transfer imposes no q<=H
condition. The strict corridor has h>=q+1, so its chosen witness length
is at most H+h. The full target is the union of the bank, since the
middle owners already collectively contain every coordinate.

There are NO rank-one through rank-five witnesses in this unchanged
bank: every source letter has size at least six. This remains true under
ordinary concatenation and copying collars. At k=17 the missing lower
layer contains exactly

    binom(17,1)+...+binom(17,5) = 9401

targets. It is the full set of holes of the cyclic bank, not a claim
about an unverified partial list of low-rank targets.

## 4. An explicit finite opening, and what its cost does not solve

For each capped component emit one period followed by its first H+h-1
letters. This realizes every cyclic interval of length at most H+h.
Indeed H+h<=2h<=2r<2r+1<=v, so the required collar is shorter than a
period. Equations (3.1) and (3.2) therefore survive in these ordinary
linear words. Concatenating them gives a nonzero finite word covering
exactly every target of ranks six through seventeen, of length

    W + sum_C (H_C+h_C-1).                                 (4.1)

The word cannot cover a lower target because its letters all have rank
at least six. Its joins add no extra charge or assumed witnesses.

Formula (4.1) is a legal finite compiler input and witness bank, but its
collar sum has not been reduced to three. A B(17) construction still
needs a legal common chronology/opening that retains all middle and
upper witnesses within 24313 positions, together with the lower-target
edits described next. Cyclic coverage alone does not authorize dropping
these collars.

## 5. Exact entrywise-capping criterion for the new bank

Fix a component and its aperture H. Let E_i be arbitrary nonempty letters
with E_i subset D_i^H. We ask to preserve every prescribed middle window:

    union_(j=0)^H E_(i-j) = X_i.                            (5.1)

For one nonconstant coordinate x, let [a,b] be a positive owner run.
The available source positions for this run are exactly [a,b-H].
Condition (5.1) is equivalent to the following three requirements:

1. Retain x at both positions a and b-H (one position if they coincide).
2. Between consecutive retained x-positions within this source run,
   the index difference is at most H+1.
3. Use no x-position outside the available source runs, as already
   enforced by E_i subset D_i^H.

To see necessity, the owner windows at a and b have only the displayed
source endpoints available for x. A gap of H+2 or more between retained
positions leaves some H+1 consecutive source positions without x.
For sufficiency, the retained position t covers owner indices [t,t+H].
The endpoint and gap conditions make these integer intervals cover all
of [a,b], and no other owner positions. A permanently positive coordinate
instead requires the same maximum-gap condition around the whole cycle.

This is a necessary-and-sufficient condition, coordinate by coordinate;
it includes interactions among multiple edits. It does not assume that
checking each modified letter separately is sufficient for simultaneous
edits.

Every cap satisfying (5.1) retains the ENTIRE cyclic upper deck. In fact,
the union of any consecutive owner windows is still realized by the
same union of their source intervals. The capped source OR is a subset
of the old OR and contains every required owner in that union, hence
equals the original upper target. Lower intersection witnesses do not
have this automatic preservation property and must be explicitly kept
or recaptured.

## 6. Forced pins and an actual safe local surgery

Let u_i be the unique coordinate entering X_i from X_(i-1), and let v_i
be the unique coordinate leaving X_(i+H) on the next transition. Define

    Pin_i = {u_i,v_i}.                                     (6.1)

Both coordinates belong to D_i^H by the residence bound. They are exactly
the coordinates for which i is respectively the first or last position
of an available source run. Therefore every cap preserving (5.1) must
contain Pin_i at position i.

There is also a converse for ONE-position edits:

    Replacing only D_i^H by any S satisfying
    Pin_i subset S subset D_i^H
    preserves every middle owner and every cyclic upper target. (6.2)

Proof: a removed coordinate is not an endpoint of its source run, so it
occurs at both neighboring source positions. Every H+1 window containing
i also contains at least one of those neighbors, since H>=1. Thus no
owner loses that coordinate. All other coordinates and windows are
unchanged. The new letter is nonempty because Pin_i is nonempty.

The same independent replacement rule is safe for a set of edit positions
with cyclic pairwise separation at least H+1: an H+1 window then contains
at most one edited position. Without that separation, use the exact
run-gap test in Section 5.

The pins coincide exactly when that coordinate's positive owner run has
length H+1. Thus for h>3 and H=3 they are necessarily distinct, because
every positive run has length at least h+1>4. These components can supply
two-element local caps but cannot supply a singleton letter while their
middle windows remain frozen. A singleton witness must contain a singleton
letter, so no longer interval evades this restriction.

For H=h, a coincident-pin singleton host is exactly a minimum positive
residence h+1, equivalently an omitted-label gap 2h+1. At k=17 gap three
is absent. Gap-five roots, however, are explicitly available at height
two: PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md Corollary 18.4 gives

    D=(10)^a 1(10)^b 0,  a>=0, b>=1, a+b=7.

Their height is two. The corresponding projected run has length three,
so the H=2 source has a one-pin host. Physical rotation gives such an
individual host for every named coordinate. Replacing that host alone
by its singleton is a literal zero-length-cost operation preserving all
middle and upper targets.

This proves individual singleton insertability, not simultaneous coverage
of all singletons or all 9401 lower targets. Different edits may remove
the same lower witness or interact through the run-gap constraints.

## 7. Exact remaining requirements for a construction

The new bank provides explicit owner windows of length two, three or four;
all upper targets have explicit source windows (3.2); ranks six through
eight have the strict-corridor source windows (3.1). It therefore supplies
substantially more than an unverified middle-only chronology.

An exact completion through this bank has two concrete unresolved tasks:

* Realize a legal linear arrangement at total length W+3, keeping one
  witness for each middle owner and the requisite upper support. The
  multiple cycle collars in (4.1) are an explicit unpaid cost here.
* Choose simultaneous nonempty lower caps and assigned intervals so that
  all 9401 targets of ranks one through five occur, all targets of ranks
  six through eight remain or are recaptured, and the owner run-gap
  constraints hold. Once owner preservation holds within a retained
  cyclic block, its upper support is automatic; no separate guess about
  upper transport under those entrywise caps is required.

Boundary recoding can change the run conditions, but then its actual
owner and target windows must be included in the finite compiler. This
note neither rules out such recoding nor silently treats it as free.

## 8. What is inherited and what is new here

Inherited are the PBBS height/residence bound, the complete strict-height
corridor, the erosion recovery identities, the g-cycle partition, and the
general interval endpoint bound. The run formulation of a flat central
compiler is also already in MASTER_HANDOFF.md Section 3.2.

The new derived conclusions are the exact source rank formula (1.3), the
unique native middle witness length and the resulting three-letter limit
on unchanged high-height fragments at B(17), the explicit capped bank
covering precisely ranks six through seventeen, its finite opening cost,
and the exact two-pin local surgery that preserves its complete upper
deck while exposing the lower-target assignment problem. None proves
nu(17)=24313 or nu(k)=B(k) in all dimensions.
