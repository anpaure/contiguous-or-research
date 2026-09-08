# Complete canonical-Phi sector law and an explicit 01-strip extension

2026-09-09. Pure proof by `exact_equality_structure`. No mathematical
execution, source search, or new word construction was performed.

This gives the complete fixed-gap sector law and an explicit path cover
which extends the new disjoint q=3 excursion bank through the ENTIRE01
sector. It does not complete the child middle factor, establish the
remaining age-compatible connections, or prove all-rank OR coverage.

**Later scope resolution:** the sector law and whole01 path/cycle cover
remain valid. However, retaining all first root entrances in the enlarged
bank precludes a spanning strict canonical-Phi completion of residence
at least2. At least Cat_(r-1) of the Cat_r first incidences must change;
see the independently reviewed
[all-root entrance obstruction](Q3_ALL_ROOT_ENTRANCE_BANK_FORCES_ONE_STEP_RUNS_20260909.md).
The residual equal-count graph is therefore not sufficient as a fixed
residence-compatible completion template.

## 1. Fixed physical gap and old prefix classes

The old alphabet has n=2r+1 sites in their fixed linear order, followed
by adjacent new sites a,b. A child lower state has size r+1. Its sector
is the two-bit word at a,b. Put

    M=binomial(n,r)=binomial(n,r+1),
    A=binomial(n,r-1)=binomial(n,r+2),
    b=M-A=Cat_(r+1).

The child lower and upper layers both have size3M+A.

For any old mask X let m(X) be the minimum of its ones-minus-zeros
prefix walk, INCLUDING the empty prefix. Partition the old rank-r and
rank-(r+1) layers as

    B={L: |L|=r, m(L)=-1},
    F={L: |L|=r, m(L)<=-2},
    G+={U: |U|=r+1, m(U)=0},
    G-={U: |U|=r+1, m(U)<=-1}.                         (1.1)

Here m(U)>=0 means exactly m(U)=0. Their sizes are

    |B|=|G+|=b,   |F|=|G-|=A.                         (1.2)

For G+, reflect a walk ending at+1 through its first visit to-1. This
bijection takes its complement to walks ending at+3, counted by
binomial(n,r+2)=A. Thus |G+|=M-A. The canonical old Phi bijection raises
the first minimum by one: it maps B bijectively to G+ and F to G-.
This proves the other counts. Finally

    M-A=2M/(r+2)=binomial(2r+2,r+1)/(r+2)=Cat_(r+1).

These are classes at the PHYSICALLY FIXED insertion gap. They cannot
be replaced by cyclically rerooted copies independently for each state.
The fixed-root port family I={0D:D Dyck of semilength r} has size Cat_r
and is a proper subfamily of B in the relevant dimensions.

## 2. The complete outgoing canonical matching

Let Phi denote the old middle matching. Let J(K) add the first-minimum
zero of an old (r-1)-set K. Then J is a bijection from that entire layer
onto F. Let J+(U) add the first-minimum zero of U in G-. Then J+ is a
bijection from G- onto the entire old rank-(r+2) layer.

The proof of both assertions is the same exact inverse. If a word has
first negative minimum m at position j, raising that zero to one makes
the new minimum m+1, LAST attained at j-1. The inverse deletes the
up-step immediately after the last minimum. For J the input ends at-3
and the image has minimum<=-2. For J+ the input ends at+1 with negative
minimum, and every output ends at+3, so its last minimum precedes the
end and the inverse exists. This extends the already recorded J proof
without a new matching-existence assumption.

The child Phi matching is exactly:

| Child lower state | Condition | Added site | Child upper state |
|---|---|---|---|
| L10, |L|=r | any L | old Phi site | Phi(L)10 |
| K11, |K|=r-1 | any K | old J site | J(K)11 |
| L01, |L|=r | L in B | a | L11 |
| L01, |L|=r | L in F | old Phi site | Phi(L)01 |
| U00, |U|=r+1 | U in G+ | b | U01 |
| U00, |U|=r+1 | U in G- | old J+ site | J+(U)00 |

To verify every row, the old endpoint heights in sectors10/01/00/11
are respectively-1,-1,+1,-3. Appending10 or11 cannot produce a new
minimum before an old minimum, giving the first two rows. Appending01
visits-2 at a: it is a new strict minimum exactly when the old minimum
is-1. Appending00 visits0 and then-1: the final b is the first negative
minimum exactly when the old walk is nonnegative. Ties are attained
first in the old word and therefore take the old site.

The upper inventory is completely partitioned: upper10 gets all M old
rank-(r+1) masks; upper11 gets F from lower11 and B from lower01; upper01
gets G- from lower01 and G+ from lower00; upper00 gets all A old
rank-(r+2) masks. Thus every child upper state occurs exactly once.

## 3. Every possible cross-sector lower step

A nontrivial Phi-directed lower step deletes a coordinate that was
present BEFORE the insertion. Deleting the just-inserted coordinate
would return to the same lower state and is excluded. The table gives
all possibilities:

* From10, an old deletion stays in10; deleting a enters00 at Phi(L).
* From11, an old deletion stays in11; deleting a enters01 at J(K), and
  deleting b enters10 at J(K). Both old parts belong to F.
* From01 with L in B, deleting an old coordinate enters11 at L-d;
  deleting b enters10 at the same old L in B.
* From01 with L in F, an old deletion stays in01; deleting b enters00
  at Phi(L) in G-.
* From00 with U in G+, every possible deletion is old and enters01.
* From00 with U in G-, every possible deletion is old and stays in00.

The final destination's old prefix class must be evaluated from its
actual mask; an old deletion need not preserve B/F or G+/G-. This is
why an inventory count alone does not close the sector routing.

## 4. An explicit whole-01 path cover from the parent successor

Suppose sigma is a parent canonical-Phi factor on all old rank-r
states, with sigma(L)=Phi(L)-d(L). For EVERY old upper U set

    L=Phi^(-1)(U),
    U+b -> sigma(L)+b.                                  (4.1)

This is a legal incoming incidence: sigma(L) is contained in U. It
assigns all M upper01 states injectively onto all M lower01 states.
No new Hall theorem or state search is needed.

The outgoing source of U+b depends on L:

* if L is in B, it is the lower00 state Phi(L), whose child Phi adds b;
* if L is in F, it is the lower01 state L+b, whose child Phi adds old.

Thus the resulting directed lower graph has vertices

    {00 Phi(L):L in B} union {01 L:all old L},

with sources00 Phi(B), sinks01 B, and internal01 F states. Every01
vertex has exactly one incoming edge. Every nonsink has one outgoing
edge. All M upper01 vertices are used exactly once.

More explicitly, for L in B let t>=1 be its first return time to B under
sigma. There is a path

    00 Phi(L) -> 01 sigma(L) -> ... -> 01 sigma^t(L).       (4.2)

These b paths partition every01 state on parent components meeting B.
Any parent component lying entirely in F becomes one intact01 cycle.
This proves the complete path/cycle cover, not just its degree counts.
If the parent is Hamiltonian, every component meets B and there are
exactly b paths and no such closed residual cycle.

All old-coordinate transitions after the source follow the actual
parent chronology. Under its lifted parent age history they preserve
the parent closed-run guarantees. The new b run remains open at the
sink; its age is exactly the return length t. Short return lengths must
be handled at the outgoing port rather than silently deleting a young b.
No prescribed external incoming age is supplied for a fresh source by
this path cover alone.

## 5. Extend the q=3 disjoint bank through all of01

Read the full theorem
`scratch/Q3_CANONICAL_PHI_DISJOINT_ROOT_PORT_EXCURSIONS_BY_SHADOW_HALL_20260909.md`.
Its shadow bound, age-three freedom for the second deletion, injective
J closure, and whole-bank disjointness are consistent with the complete
sector law above. Its hypothesis is a residence-three parent factor,
r>=7, and lifted parent input ages at each fixed-root port.

Write h=Cat_r and I={0D}. Let the selected Hall facets give distinct
K_L containing u, let K'_L=J(K_L)-u, and put O={J(K'_L):L in I}.
The q=3 bank consists of h disjoint paths

    L+a -> Phi(L) -> sigma(L)+b -> K_L+a+b
        -> K'_L+a+b -> J(K'_L)+a.                       (5.1)

Each L in I lies in B. Also sigma(L) lies in B: Phi(L)=1D has every
nonempty old prefix at height at least1; deleting one old one lowers
suffix heights by2, so sigma(L) has minimum at least-1 and ends at-1.
Therefore (4.2) at such an L is a UNIT path

    00 Phi(L) -> 01 sigma(L),                            (5.2)

and is exactly the central00-to01 edge already present in (5.1).

Keep all the other paths/cycles of Section4 alongside the q=3 bank,
omitting only the h duplicated unit paths (5.2). This introduces NO
state or upper-owner collisions: the01 cover is a disjoint partition,
its00 sources are Phi(B), and all new10/11 states lie in different
sectors. The q=3 bank's remaining disjointness is its proved theorem.

This gives a concrete enlarged path/cycle bank using the ENTIRE01
lower sector and ENTIRE01 upper sector. For a Hamilton parent it has
exactly b paths, h of which are the five-step excursions and b-h the
remaining paths (4.2). It uses

    lower states: M+b+4h,
    upper states: M+4h.

The difference b is exactly the number of lower-to-lower path components.
No path initialization or source-word collar is being counted as free:
these are middle-incidence inventory statements before literal compilation.

The unused lower states, classified exactly by sector, are

    10: M-2h,  00: A (all G-),  01:0,  11:A-2h.          (5.3)

The unused upper states are

    10:M-h,  00:A,  01:0,  11:M-3h.                     (5.4)

In upper11 the h states sigma(I) belong to B, while the two disjoint
h-state J images belong to F; this justifies the count3h without
double credit. Outputs O avoid I, and both11 banks are disjoint.

## 6. The remaining incidence problem is now explicit

For the enlarged bank with Hamilton parent, its path starts are

    10 I, and 00 Phi(B minus I).

These used states still need incoming incidences. Together with the
unused lower states, the free incoming lower inventory is

    lower10: all old rank-r masks except O             (M-h),
    lower00: all old rank-(r+1) masks except Phi(I)     (M-h),
    lower11: all old (r-1)-masks except K-bank,K'-bank (A-2h).
                                                                 (6.1)

It has size2M+A-4h, equal to the unused upper inventory (5.4).
Every remaining permitted incidence is given by plain containment:

* an upper10 state U+a can go to lower00 U or to a free lower10
  R+a with R subset U;
* an upper00 old (r+2)-set Z can go to a free lower00 U subset Z;
* an upper11 state R+a+b can go to free lower10 R+a or to free
  lower11 K+a+b with K subset R.

All lower01 inputs are already filled and may not receive another edge.
The edge returning to the upper state's own Phi-preimage is forbidden:
it would make a repeated lower state rather than a nontrivial successor.

This is a fully specified residual three-band incidence graph, with
actual removed K/K'/O sets. Its perfect matching, residence at every
socket, and component permutation are NOT proved by the equal counts.
If the parent has an F-only component, the01 cycle fixed in Section4
would also require an explicitly reopened edge before a one-cycle child
could result. No such reopening is hidden here.

The positive construction in this note is the entire01 strip and its
collision-free extension of the q=3 bank. The still missing step is
completion of (6.1) with the true age and topology conditions, followed
by all-rank source compilation and a safe opening. The new finite21/22
literal claims are separate verification tasks, not consequences of
this unfinished all-dimensional construction.
