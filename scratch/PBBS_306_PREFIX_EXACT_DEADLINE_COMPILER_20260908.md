# Exact one-pivot source geometry for the 306-owner PBBS sector

Date: 2026-09-08. Author/reviewer: Codex subagent `exact_b_induction`.

Status: proved explicit conditional source construction and exact seam
tests. No seam path, full upper transport, or lower common-cap solution is
claimed. The intact 306-owner sector is independently reviewed below.

## 1. Independent review of the bad-sector theorem

Reviewed source:
`scratch/PBBS_EXACT_THREE_RUN_COMPONENT_SECTOR_20260908.md`.

Its proof is valid, using the exact run/return dictionary and gap-five
classification retained in
`MATH_THEOREM_PBBS_EXACT_RUN_SPECTRUM_FLAT_ANTECEDENT_NOGO_AND_FULL_UPPER_DECK_20260813.md`,
Sections 1–3. Those sections explicitly state that the upper-middle
complement row has no positive runs of lengths one or two, and classify all
length-three runs by the displayed gap-five roots.

The new sector proof closes both containment directions: the relevant
roots lie in the invariant defect-one class, and the explicit map

\[
 f(x,y,z,u)=(y,z,x,u+2(x+1))
\]

shows that a component contains a gap-five root exactly when its triple
has a zero coordinate. Its third power shifts the physical root by one.
Every boundary triple has a cyclic orbit of size three, including the
triples with two zero coordinates, so each component has exactly `3n`
states. Fixed triples are interior when `r>=3`, and are correctly excluded.
The boundary count `3(r-2)` therefore gives `r-2` components. Because
`3n` is odd, taking `f^2` does not split them.

At `r=8`, the six 51-cycles contain 306 owners and all 119 positive
three-runs; every other intact component has positive runs of length at
least four. This review did not rerun the source's independent original-map
verification, but checked its general algebra and its imported premises.

## 2. An explicit schedule, not an extra-length allowance

Put `W=24310`, `N=W+3=24313`. More generally let `0<=L<W`. Suppose

\[
 T=(T_0,\ldots,T_{W-1})
\]

is a Johnson path through all rank-nine subsets of `[17]`. Define

\[
 h_i=\begin{cases}2,&i<L,\\3,&i\ge L,\end{cases}
 \qquad I_i=[i,i+h_i].                                      \tag{2.1}
\]

Define the literal maximal source by

\[
 \boxed{A_p=\bigcap_{i:\ p\in I_i}T_i\quad(0\le p<N).}      \tag{2.2}
\]

Every physical position belongs to at least one owner interval. The
intervals containing it form a consecutive set of at most four owner
indices. Because the path is Johnson and every owner has size nine,

\[
                         |A_p|\ge6.                         \tag{2.3}
\]

Thus (2.2) always gives a nonzero word. The only issue for middle replay is
whether each coordinate can survive its owner windows.

### Exact run condition

The source (2.2) satisfies

\[
                  \bigcup_{p\in I_i}A_p=T_i\quad\text{for all }i          \tag{2.4}
\]

if and only if each *internal* maximal positive coordinate run `[a,b]`
in `T` satisfies

\[
 b-a+1\ge\begin{cases}3,&a\le L,\\4,&a>L.\end{cases}        \tag{2.5}
\]

Runs touching either global endpoint have no lower-length restriction.
Equivalently, there are no internal runs of length one or two, and every
internal run of length three starts at an index at most `L`.

Proof. For an internal run `[a,b]`, the previous absent owner ends at
`a-1+h_(a-1)`, and the next absent owner starts at `b+1`. Hence all allowed
positions for its coordinate are exactly

\[
                         [a+h_{a-1},b].                      \tag{2.6}
\]

The owner endpoints are increasing, and `h_(a-1)<=h_a`. If (2.6) is
nonempty, it meets every interval `I_i` for `a<=i<=b`; if empty, the
coordinate cannot be supplied. This proves the length requirement
`b-a+1>=h_(a-1)+1`, which is (2.5). Initial runs may use the first physical
position, and terminal runs may use the end of the last owner interval, so
they always have the required one-sided coverage. Forbidden coordinates
are excluded by the intersections in (2.2). This proves necessity and
sufficiency.

The exact boundary is `a<=L`, not `a<L`: a three-run beginning at `L`
still sees the shallower previous owner interval.

## 3. Complete seam guards for one opened block per component

Open each canonical PBBS component at one edge, choose its orientation, and
concatenate the resulting owner blocks. Put the six bad 51-cycles first,
so their total length is `L=306`. All blocks have length at least 17.

For a block `B` and coordinate `x`, let `s_x(B)` be its terminal positive
run length and `p_x(B)` its initial positive run length, each capped at
four. An endpoint omitting `x` gives value zero.

Require every new seam to be a Johnson adjacency. For two successive
blocks `B,C`, put

\[
                         t_x=s_x(B)+p_x(C).                   \tag{3.1}
\]

The following pair-local guards give exactly the needed short-run
condition for this whole-block order:

* At a seam between two of the first six blocks, require, for every `x`,
  `t_x=0` or `t_x>=3`.
* At the seam between the sixth bad block and the first good block,
  require the same `t_x=0` or `t_x>=3`.
* At every later seam between good blocks, require `t_x=0` or `t_x>=4`.

Proof. All old internal runs in the first six blocks have length at least
three, and all old internal runs in later blocks have length at least
four. A new short run meeting one seam is exactly the positive suffix of
the left block followed by the positive prefix of the right block; a zero
arm is allowed. The capped values determine precisely whether its length
is at most three. A run of length at most three cannot cross two seams,
because every block has at least 17 owners.

At an early seam its starting index is less than `L`. At the bad-to-good
seam it starts at most `L`, including a length-three positive prefix on the
good block when the preceding endpoint omits that coordinate. At a later
seam, any newly created run of length at most three starts strictly after
`L`, since a full good block of length at least 17 separates that seam
from the pivot. Therefore these three cases are exactly (2.5).

Consequently, **an actual block order/cut/orientation choice meeting these
Johnson and age guards immediately produces the explicit word (2.2)** of
length 24,313 with complete middle coverage. This is a finite source
construction once its stated input is supplied, not a claim that the
input exists.

The guards are stronger than Hamming-distance-two seam compatibility and
cannot be replaced by it. They are the specialized, explicitly bounded
version of the run-summary calculus in
`MATH_THEOREM_A_K17_PROTECTED_PBBS_OPENING_MAX_POSITION_CUT_CHARGE_20260731.md`.

## 4. Exact lower-cell inventory and the remaining compiler

For schedule (2.1), the literal intervals which contain no full owner
interval are precisely

\[
 \{[p,p]:0\le p\le W+2\},
\]

\[
 \{[p,p+1]:0\le p\le W+1\},
\]

\[
 \{[p,p+2]:L\le p\le W\}.                         \tag{4.1}
\]

Indeed a start below `L` first contains its rank-nine owner at length
three; a start at least `L` first contains one at length four. The final
three starts give only the indicated truncated suffix intervals. Thus the
atlas size is

\[
 (W+3)+(W+2)+(W+1-L)=3W+6-L.                        \tag{4.2}
\]

At `L=306`, it contains exactly **72,630** cells. There are **65,535**
nonempty targets below rank nine, leaving **7,095** cells of scalar slack.
Equivalently, the schedule consumes 306 of the handoff's 7,401 deadline
slack. This changes no source length: it removes 306 candidate triple
cells from the depth-three lower atlas.

The maximal source (2.2) has every letter of size at least six. Therefore
it does not by itself cover the targets below rank six. The source must be
shrunk by one common-cap assignment that preserves (2.4) and realizes
every lower target in (4.1). Separate rankwise Hall matchings or 7,095
unused cells do not establish such an assignment.

For any word reproducing the owners on their intervals, a lower-rank
target cannot use a witness outside (4.1), since such an interval contains
a rank-nine owner. Thus this is the exact residual lower compiler for this
schedule, with no uncharged witness category.

## 5. The upper boundary is separate and real

An intact PBBS factor has all upper targets, but concatenating opened
components can remove the only selected occurrence of a target. The
rank-eight single-soliton mountain component has 17 globally unique q1
intersection colours; after complementation these give 17 upper-rank-ten
edge witnesses. This is proved in
`MATH_THEOREM_PBBS_SINGLE_SOLITON_FORCED_CYCLE_OBSTRUCTION_20260805.md`.
At least one is destroyed when that component is opened, and a new seam or
another edited occurrence must recreate it. No choice of its old cut alone
can retain all those edge witnesses.

The known local gadget
`MATH_THEOREM_PBBS_RIGID_SINGLE_SOLITON_CLEAN_C6_Q2_PALETTE_REPAIR_20260805.md`
preserves q1 intersection, q1 union, and q2 turn multisets, but does not
prove all-width upper transport or the seam age guards above. It cannot be
silently substituted for those requirements.

If the resulting chronology is upper-complete, its upper witnesses do lift
literally: a consecutive owner block `T_i,...,T_j` is the union of the
overlapping physical intervals `I_i,...,I_j`, whose union is the interval
`[i,j+h_j]`. Hence (2.4) transports its union to the same contiguous source
interval. This shows exactly how an audited upper-complete chronology and
one successful common-cap lower compiler would give `nu(17)=24313`.

## 6. Bounded verification

A remote-only check on `ssh h100` exhaustively compared (2.4) with (2.5)
for every binary coordinate profile, every `2<=W<=9`, and every
`0<=L<W`. It checked 8,192 profiles and passed. This check specifically
tests the pivot equality and global endpoint conventions.

The same tiny remote calculation gave

```text
PASS one-pivot run/replay equivalence on 8192 binary profiles
k17 atlas 72630 lower targets 65535 spare 7095
```

The general proof is Sections 2–4. These finite checks neither construct
the missing PBBS seam path nor validate a common-cap compiler.

## 7. Applying the schedule to the constructed non-Johnson prefix

Root addition, 2026-09-08. The later finite construction in
`K17_PBBS_UPPER_CUT_CORES_AND_306_OWNER_SOURCE_STAGE_20260908.md` supplies
an actual 306-owner path P. Its three non-Johnson seams mean it does not
meet Section 2's global Johnson assumption. The following exact variant
removes that unnecessary restriction on the shallow prefix.

Suppose the remaining 24,004 owners are ordered in a path Q, without
repetition, so P followed by Q enumerates every rank-nine target. Assume:

1. every internal positive run in P has length at least three, and its
   consecutive triple intersections are nonempty;
2. Q is a Johnson path with no internal positive run shorter than four;
3. at the P/Q seam, each positive suffix length of P plus positive prefix
   length of Q is zero or at least three; and
4. P[-2] intersect P[-1] intersect Q[0] and
   P[-1] intersect Q[0] intersect Q[1] are both nonempty.

Here the endpoint lengths in item 3 are the full lengths, or their values
capped at four. Runs touching a global endpoint are exempt from the
internal-run condition as in Section 2.

Then the same intervals (2.1), with L=306, and the same formula (2.2)
produce a nonempty word of exactly 24,313 letters reproducing all owners.

Proof. The coordinatewise replay proof uses increasing starts/deadlines,
not Johnson adjacency. Items 1–3 give exactly its run condition (2.5).
Every source position in the prefix lies in at most three consecutive
owner intervals, whose intersection is nonempty by item 1. At physical
positions 306 and 307 the two mixed intersections are exactly those in
item 4. At position 308 only Q[0],Q[1],Q[2] are involved. Every later
source position uses at most four consecutive owners of the Johnson path
Q, and their intersection has size at least six. Initial and terminal
intersections are subsets of these index blocks and are nonempty as well.
Thus all source letters are nonempty and the run criterion proves replay.
QED.

The atlas (4.1) and its 7,095 scalar slack are unchanged. The prefix's
source letters need not have rank at least six; only nonemptiness is
asserted there. The displayed 306-owner P supplies item 1, but Q, its
joining and upper-coverage properties, the seam tests, and the full
lower-target compiler still have to be supplied.

### Independent review of Section 7

Reviewed by `exact_b_induction`, 2026-09-08: the variant is valid. No
additional computation was used. In zero-based indices the two mixed
physical positions are exactly

\[
 A_{306}=P_{304}\cap P_{305}\cap Q_0,
 \qquad A_{307}=P_{305}\cap Q_0\cap Q_1.
\]

Position 308 has the three-owner intersection `Q_0 intersect Q_1
intersect Q_2`; position 309 is the first four-owner Q intersection. All
other boundary intersections involve subsets of the checked consecutive
owner blocks. The run condition depends only on the owner-incidence
intervals, so it remains exact despite non-Johnson transitions inside P.
A three-run beginning at Q's first owner starts at index 306 and is
correctly permitted. Short endpoint runs of P and Q which become internal
are precisely the seam runs controlled by item 3; the two global endpoints
remain exempt. No hidden extra collar is required for this middle-replay
statement.
