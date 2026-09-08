# The 24-owner two-seed Q2 completion classification

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Verdict

Let

\[
 A=\{a,b,c,d\},
 \qquad R_1=\{u,v\},
 \qquad R_2=\{w,x\},                                  \tag{0.1}
\]

and let the 24-owner pair-frame carrier be

\[
 \mathcal V=\left\{X\cup Y:
 X\in\binom A2,
 |Y\cap R_1|=|Y\cap R_2|=1\right\}.                  \tag{0.2}
\]

There are three different notions of a ``two-seed completion'', and they
have different answers.

1. **A four-factor menu exists.**  The carrier \(\mathcal V\) has four
   distinct partitions into six physical Q2 cells.  Hence four exact
   local factor corners can be written on the same owner set.  Exactness
   of four isolated Q2 corners is not the obstruction.  A common
   phase-compatible suspension of those four arbitrary tilings is not
   asserted.

2. **Two canonical pair-frame associators do not give a faithful Boolean
   square.**  Up to coordinate relabelling preserving \(\mathcal V\), the
   canonical factor has only three states, one for each perfect matching
   of \(A\).  Two nontrivial commuting involutions cannot act faithfully
   on these three states.  Every canonical four-corner diagram folds along
   a diagonal, and its second signed move cancels or becomes type-neutral.

3. **No factor menu on this 24-owner carrier can accumulate two forward
   Q2 death bits.**  Relative to the old matching

   \[
       P_0=ab\mid cd\mid uv\mid wx,                   \tag{0.3}
   \]

   every lower physical edge of \(\mathcal V\) has local full-pair type
   zero or one.  In any Q2 factor, at most eight of the 24 edge occurrences
   have type one.  The old canonical shore attains eight and the new shore
   attains zero.  Thus every possible final factor satisfies

   \[
      \sum f_{P_0}(\text{old lower edges})
       -\sum f_{P_0}(\text{final lower edges})\le8.   \tag{0.4}
   \]

   The total same-carrier drift is at most \(8/24=1/3\), regardless of
   how many intermediate exact tilings are inserted.  The upper statement
   is identical by complementation.  In particular the two-exposure
   architecture cannot be realized on one copy of \(\mathcal V\): the
   averaged three-halves schedule demands \(1/2+o(1)=12/24+o(1)\), while
   a corner exposing two full canonical Bernoulli-\(1/3\) erasures would
   demand \(2/3=16/24\).

If two 24-owner packets have different but overlapping owner supports,
their additive union has multiplicity two on the overlap in all four shore
states.  If their owner supports are disjoint, their switches commute but
no owner sees both seeds.  Therefore the first possible positive object is
strictly larger than a 24-owner packet: it must be a new nonadditive joint
carrier whose lower shadows can hold two independently removable full-pair
opportunities with multiplicity-weighted incidence at least one half per
occurrence on average, and whose four resolutions retile every common owner
once.  The two opportunities may coexist on one occurrence, so this is not
a union-density condition.

## 1. The three canonical factor states

Let \(P=\{p,p'\}\) be a perfect matching of the four-set \(A\), where
\(p,p'\in\binom A2\) are its two edges.  Let

\[
 C_P=\{X\in\binom A2:|X\cap p|=|X\cap p'|=1\}         \tag{1.1}
\]

in its natural four-cycle order, and let

\[
 Q_R=(uw,vw,vx,ux).                                   \tag{1.2}
\]

Define

\[
 \mathscr D_P=
 \{C_P\cup Y:Y\in\{uw,vw,vx,ux\}\}
 \mathbin{\dot\cup}
 \{p\cup Q_R,p'\cup Q_R\}.                           \tag{1.3}
\]

The first four cells cover the four special two-sets splitting \(P\), at
every reservoir state.  The last two cells cover the two matching edges
\(p,p'\), through all reservoir states.  Thus \(\mathscr D_P\) is an
exact partition of \(\mathcal V\) into six physical Q2 cells.

The three perfect matchings

\[
 P_0=ab\mid cd,
 \qquad P_1=ac\mid bd,
 \qquad P_2=ad\mid bc                              \tag{1.4}
\]

give the three canonical states.  Replacing \(\mathscr D_{P_i}\) by
\(\mathscr D_{P_j}\), \(i\ne j\), is the reciprocal six-for-six
pair-frame associator.

### Lemma 1.1 (intrinsic recognition of the frame)

Every coordinate relabelling which preserves \(\mathcal V\) preserves
the special four-set \(A\) and the unordered reservoir-pair set
\(\{R_1,R_2\}\).  Consequently every relabelled canonical pair-frame
factor on the same carrier is one of the three factors (1.3), up to cell
orientation.

#### Proof

For two coordinates \(i,j\), put

\[
 c(i,j)=|\{Z\in\mathcal V:i,j\in Z\}|.                \tag{1.5}
\]

Directly from (0.2),

\[
 c(i,j)=
 \begin{cases}
 0,&\{i,j\}=R_1\text{ or }R_2,\\
 4,&i,j\in A,\\
 6,&\text{otherwise}.
 \end{cases}                                         \tag{1.6}
\]

Thus \(R_1,R_2\) are the unique coordinate pairs never appearing
together in a carrier owner.  Their complement is intrinsically \(A\).
Every relabelling preserving the carrier must preserve this structure.

In a canonical packet representation, the two reservoir pairs are exactly
the coordinate pairs whose two endpoints never occur together.  Hence they
must be \(R_1,R_2\), and the special block must be \(A\).  Its old pair
frame is one of the three perfect matchings (1.4), giving (1.3). \(\square\)

In a contextual embedding with a frozen outside core, core coordinates
have carrier degree 24 and unused coordinates have degree zero, whereas
the eight active coordinates have degree 12.  Hence the same intrinsic
classification survives unchanged.

### Theorem 1.2 (no faithful canonical V4 square)

There is no four-corner diagram of four distinct canonical pair-frame
states on \(\mathcal V\) in which the two reciprocal seed switches are
independent commuting involutions.

#### Proof

By Lemma 1.1 the state set has size three.  Its permutation group is
\(S_3\).  Two distinct nonidentity involutions in \(S_3\) are
transpositions, and distinct transpositions do not commute.  Equal
involutions encode the same seed, while an identity does not encode a
trade.  Hence no faithful \(C_2^2\) action exists.

Equivalently, colour the four vertices of a Boolean square by
\(P_0,P_1,P_2\), requiring adjacent colours to differ.  With only three
colours, two opposite vertices have the same colour.  If the two neighbours
of the base use the two different nonbase colours, the fourth corner is
forced to equal the base. \(\square\)

There is a degenerate exact square:

\[
 \mathscr F_{00}=\mathscr D_{P_0},\quad
 \mathscr F_{10}=\mathscr D_{P_1},\quad
 \mathscr F_{01}=\mathscr D_{P_2},\quad
 \mathscr F_{11}=\mathscr D_{P_0}.                   \tag{1.7}
\]

Every edge of (1.7) is a reciprocal canonical associator and every corner
is exact.  But the double switch returns to the base factor.  Thus (1.7)
has no second forward signed action and demonstrates why ``all four
corners exact'' is weaker than independent two-seed completion.

## 2. Four distinct exact Q2 corners do exist

The canonical three-state obstruction is not an obstruction to arbitrary
Q2 tilings of \(\mathcal V\).  Besides (1.3), define the vertical factor

\[
 \mathscr D_V=\{X\cup Q_R:X\in\binom A2\}.            \tag{2.1}
\]

It consists of six reservoir squares and plainly partitions
\(\mathcal V\).

There is also an all-mixed factor.  Partition the six special vertices by
the three Johnson edges

\[
 \{ab,ac\},\qquad\{ad,bd\},\qquad\{bc,cd\},           \tag{2.2}
\]

and partition the reservoir four-cycle by the two edges

\[
 \{uw,vw\},\qquad\{vx,ux\}.                           \tag{2.3}
\]

For every edge in (2.2) and every edge in (2.3), take their Cartesian
product.  This gives six disjoint four-vertex cells covering
\(6\cdot4=24\) owners.  Each cell is a physical Q2: one direction is a
special-coordinate Johnson swap and the other flips one reservoir pair,
and their coordinate supports are disjoint.  Denote this factor by
\(\mathscr D_M\).

Thus, for example,

\[
 \mathscr D_{P_0},\quad\mathscr D_{P_1},\quad
 \mathscr D_V,\quad\mathscr D_M                       \tag{2.4}
\]

are four distinct exact six-Q2 factors on the same owner carrier.  Any
whole-factor replacement between two of them preserves every middle owner
exactly once.  Therefore bare four-corner exactness is possible.

This is a local Q2 statement.  Unlike the canonical pair
\(\mathscr D_{P_0},\mathscr D_{P_1}\), the four factors in (2.4) have not
been given one common phase colouring which suspends every corner to the
same long-cycle occurrence support.

These four factors do not form two copies of the signed canonical
associator.  Their lower type-one edge counts relative to (0.3) are,
respectively,

\[
                  8,\qquad0,\qquad8,\qquad4.          \tag{2.5}
\]

For \(\mathscr D_M\), the twelve special-direction edges have type zero.
Among its twelve reservoir-direction edges, each of the two special
vertices \(ab,cd\) occurs over the two reservoir matching edges, giving
four type-one occurrences.  Hence (2.5).

In particular no orientation of the menu (2.4) makes both bits contribute
the canonical \(8\)-unit forward drift independently.

## 3. The same-carrier signed-action invariant

Let \(\mathscr F\) be any partition of \(\mathcal V\) into physical
cycles, in particular any six-Q2 factor.  Direct every cycle arbitrarily;
the 24 depth-one lower occurrences are its 24 undirected cycle edges,
each counted once.

Let

\[
 S=\{Z\in\mathcal V:ab\subseteq Z\text{ or }cd\subseteq Z\}.       \tag{3.1}
\]

Since every reservoir state splits both reservoir pairs,

\[
                         |S|=2\cdot4=8.              \tag{3.2}
\]

### Lemma 3.1 (eight-edge ceiling)

For every factor \(\mathscr F\) on \(\mathcal V\), at most eight lower
edge occurrences have one full \(P_0\)-pair.

#### Proof

The intersection of adjacent middle owners has size three, so it contains
at most one full \(P_0\)-pair.  It contains one precisely when both edge
endpoints lie in \(S\): the common full pair is then \(ab\) or \(cd\).

The union of the cycles of \(\mathscr F\) is a 2-regular graph on the 24
owners.  The sum of its degrees over the eight vertices of \(S\) is 16.
Every edge internal to \(S\) contributes two to this sum, so there are at
most eight such edges.  These are exactly the type-one lower occurrences.
\(\square\)

The old canonical factor \(\mathscr D_{P_0}\) attains equality: its two
reservoir squares at \(ab\) and \(cd\) supply eight type-one edges.  The
new factor \(\mathscr D_{P_1}\) has none.  Therefore:

### Theorem 3.2 (no two accumulated deaths on 24 owners)

For every finite sequence of exact physical factors

\[
 \mathscr D_{P_0}=\mathscr F^{(0)},
 \mathscr F^{(1)},\ldots,\mathscr F^{(r)}             \tag{3.3}
\]

on the same carrier \(\mathcal V\), the total decrease between the first
and final lower full-pair ledgers is at most eight:

\[
 \sum_e f_{P_0}(\cap e;\mathscr F^{(0)})
 -\sum_e f_{P_0}(\cap e;\mathscr F^{(r)})\le8.        \tag{3.4}
\]

Consequently the average type displacement is at most \(1/3\), no matter
how many intermediate exact shores are called ``layers'', when only the
old and final edges at one fixed physical phase are counted.

#### Proof

The initial sum equals eight.  Every final summand is nonnegative; Lemma
3.1 additionally shows that every intermediate and final sum is at most
eight.  Thus (3.4) is immediate. \(\square\)

Adjoining an arbitrary frozen outside core adds the same number of full
\(P_0\)-pairs to every one of the 24 old and final edge occurrences.  It
cancels from (3.4).  The ceiling is therefore unchanged in every contextual
embedding whose exterior is genuinely frozen.

Complementation preserves \(\mathcal V\).  An upper edge union has rank
five and hence at least one full local pair.  Subtracting this forced one,
complementation identifies its excess full-pair count with the lower type
of the complementary edge.  The upper excess can therefore decrease by
at most eight as well.  The obstruction is two-sided.

The chronology content is important.  A final depth-one occurrence is one
physical edge and has one rank-three intersection.  Replacing its factor
several times does not concatenate several deletions; only the final edge
is present.  To raise the death density beyond \(1/3\), the common carrier
must expose a fresh death-eligible family among starts not already depleted
by the first seed.  On \(\mathcal V\), the old factor has only the eight
type-one starts in (3.2), and no exact final edge can decrease any of the
other sixteen type-zero starts.  Intermediate shore labels therefore add
no chronological capacity.

Theorem 3.2 is a net old-versus-final ledger theorem; it does not bound the
sum of absolute changes along an oscillating time sequence of factors.  If
a literal long window traverses several time-separated repartitions, its
vertical or contextual connectors become additional owners and edges.
That object is a factor on a larger carrier such as
\(\mathcal V\times\{\text{time states}\}\), and is deliberately outside
the 24-owner theorem.

## 4. Partial owner overlap

Let seed \(i\in\{1,2\}\) have owner support \(U_i\), with both shores
\(\mathscr F_i^0,\mathscr F_i^1\) covering every owner of \(U_i\) once.
For bits \((\eta_1,\eta_2)\), the additive corner

\[
                  \mathscr F_1^{\eta_1}\cup
                  \mathscr F_2^{\eta_2}               \tag{4.1}
\]

has middle-owner multiplicity

\[
                  \mathbf1_{U_1}+\mathbf1_{U_2},      \tag{4.2}
\]

independently of the bits.  Thus:

* if \(U_1\cap U_2\ne\varnothing\), every overlap owner has multiplicity
  two in all four corners, so (4.1) is not an exact factor;
* if \(U_1\cap U_2=\varnothing\), all four additive corners are exact on
  \(U_1\dot\cup U_2\), even if their coordinate sets overlap, but no
  physical owner is exposed to both signed seeds.

This proves that ordinary packing cannot realize the needed average
visibility \(3/2\).  Removing one copy on the overlap would destroy one
completed packet support.  A legal repair has to retile the overlap
jointly; it is a new nonadditive factor, not a union of the two certified
24-owner trades.

If two packet rows happen to be physically identical, declaring the two
labelled copies to be one row is likewise a nonadditive quotient, not the
union (4.1).  The coincidence need not persist after either shore switch,
so all four quotient corners must then be rechecked from scratch.  Such a
quotient is covered by the larger joint-retile escape, not by the packing
lemma.

## 5. Exact implication boundary

The local two-seed question is now separated as follows.

* Weak menu exactness: **yes**, by (2.4).
* Four distinct canonical pair-frame states: **no**, by Theorem 1.2.
* Two accumulating canonical signed deaths on one 24-owner carrier:
  **no**, by Theorem 3.2.
* Additive packing of owner-overlapping packets: **no**, by (4.2).
* Owner-disjoint packing: **yes**, but it supplies visibility at most one
  per owner in one simultaneous additive menu and cannot meet the
  three-halves schedule in that architecture.  Sequentially changing the
  packet partition and then fusing the stages is a larger-carrier problem,
  not ruled out here.

The smallest surviving design must enlarge the local carrier.  It needs:

1. fresh removable contributions with multiplicity-weighted incidence at
   least \(1/2-o(1)\) per occurrence for the averaged three-halves
   schedule, and \(2/3-o(1)\) for a corner exposing two complete canonical
   layers (an independent two-bit model would in particular have some local
   type-two occurrences, but that is not logically necessary);
2. four nonnegative exact factor corners whose two signed differences
   remove two distinct local contributions rather than reverse one
   another;
3. one-copy middle ownership at every corner, including the overlap; and
4. a physical direction chronology making one or two seed moves visible
   in the same depth increment.

These requirements rule out the existing 24-owner Q2 packet itself, but
they do not rule out a larger nonproduct carrier built from two overlapping
frames and retiled from scratch.
