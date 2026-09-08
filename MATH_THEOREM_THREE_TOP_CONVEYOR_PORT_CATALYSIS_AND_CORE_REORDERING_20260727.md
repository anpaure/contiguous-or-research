# Three-top conveyors as literal port catalysts

## Exact core transpositions, bounded collateral, and the deletion-distance obstruction

Date: 2026-07-27

Scope: constant-one Gaussian-annulus program; pure mathematics only.
No computation, search, solver, or external theorem is used.

## 0. Outcome

The three-top/two-base promotion conveyor is a genuine literal
port-changing move which preserves the complete squarefree middle-owner
set.  It therefore crosses the ordered-port and maximal ordered-core
sectors left invariant by common-template cycle and placeholder-cube
moves.

The exact conclusions are as follows.

1.  On a chosen focal top, one conveyor swaps two labels in a fixed
    cyclic order.  Every other label remains in its old position.  The
    two companion tops absorb the exact middle-owner collateral.

2.  At protected depth \(\delta\le H\), with safe port length

    \[
                            L=H+\delta-1,
    \]

    one conveyor changes exactly \(6L\) top-indexed ordered ports across
    its three frames.  All other ports remain literally unchanged.

3.  If the old three frames occur in a global squarefree middle factor,
    replacing them by the new three frames preserves that global factor
    exactly.  Thus this is not an unpaired clone move.

4.  For \(M\ge16H\), any prescribed transposition on a focal cyclic
    order is the product of three admissible conveyor transpositions
    through one buffer position.  With three distinct outside labels,
    this uses one focal top and six companion tops.  Squarefreeness is
    preserved after every one of the three switches.  The companions
    are changed, not returned; this is a bounded-collateral catalyst,
    not a free reusable catalyst.

5.  A top-disjoint bank of \(t\) conveyors reroutes exactly \(3Mt\)
    distinct middle-owner incidences and changes exactly \(6Lt\) ports.
    Its port/owner ratio is

    \[
                            \frac{2L}{M}=O(H/m)=o(1).           \tag{0.1}
    \]

    Hence a hypothetical bank acting on \(\Theta(W)\) middle owners
    would have only \(o(W)\) changed-port boundary at Gaussian
    \(H=o(m)\).  There is no port-count obstruction to positive-density
    use.  Converting this count to word length still requires an
    \(O(1)\)-cost splice or a shared-collar theorem.

6.  Boundedly many conveyors do not collapse the whole ordered-core
    state space.  If a fixed top is touched \(b\) times, deleting at
    most \(2b\) labels makes its final cyclic order identical to its
    initial order.  There are pairs of cyclic orders whose deletion
    distance is \(M-O(\sqrt M)\), and they require
    \(M/2-O(\sqrt M)\) touches of that top.

Thus the earlier three-label ordered-core obstruction is crossed by
boundedly many conveyors, but arbitrary core mixing is not.  The exact
remaining positive gate is a squarefree matching problem for the
prescribed companion frames.  No theorem here supplies a
\(\Theta(W/M)\)-sized bank of such literal packets.

## 1. Admissible positional transpositions

Put

\[
                         n=2m,\qquad M=m+H,
\tag{1.1}
\]

and assume \(H\ge2\) and \(M\ge8H\).  Let \(U\) be an \(M\)-set with
a rooted cyclic order \(\pi\).  For two positions \(p,q\), let the two
**open cyclic gaps** be the numbers of positions strictly between
\(p,q\) on the two arcs of the cycle.

Call \(p,q\) **conveyor-admissible** when both open gaps have size at
least

\[
                         s=4H-2.                               \tag{1.2}
\]

This is exactly the room required by the two-base construction: each
arc receives two inner arms of total size \(2H-2\), two outer arms of
total size \(2H\), and a possibly empty filler block.

### Lemma 1.1 (an arbitrary admissible frame is a conveyor base)

Let labels \(x,y\in U\) occupy conveyor-admissible positions in \(\pi\).
Then the labels of \(U\setminus\{x,y\}\) can be partitioned into the
eight arms and two filler blocks of the two-base conveyor so that

\[
                         \pi=\omega^+(x,y).                    \tag{1.3}
\]

The opposite focal frame is

\[
                         \omega^-(x,y)=\tau_{xy}\pi,           \tag{1.4}
\]

where \(\tau_{xy}\) swaps the positions of \(x,y\) and fixes every
other position.

#### Proof

Read clockwise from \(x\) to \(y\).  Put the first \(H-1\) labels in
\(A^+\), the next \(H\) in \(\widehat A^+\), the last \(H-1\) before
\(y\) in the reversed \(B^-\) arm, and the preceding \(H\) in the
reversed \(\widehat B^-\) arm.  The remaining labels on this arc form
\(F_1\).  Perform the analogous construction on the other arc to obtain
\(B^+,\widehat B^+,\widehat A^-,A^-\), and \(F_2\).

The gap hypothesis makes both filler lengths nonnegative, and the
resulting word is exactly \(\omega^+(x,y)\).  Replacing plus by minus
interchanges only the labels in the two placeholder positions, proving
(1.4). \(\square\)

Choose any auxiliary label \(a\notin U\), put

\[
 C=U\setminus\{x,y\},qquad
 U_0=U,\qquad U_1=C\cup\{x,a\},\qquad U_2=C\cup\{a,y\}.       \tag{1.5}
\]

The old packet is

\[
 \omega^+(x,y),\qquad(\omega')^+(x,a),\qquad
 (\omega')^+(a,y),                                             \tag{1.6}
\]

and the new packet replaces all three plus frames by their minus
frames.

### Theorem 1.2 (literal focal-transposition catalyst)

Packet replacement (1.6) has the following simultaneous properties.

1. Its old and new middle incidence vectors are equal and squarefree.
2. On the focal top \(U\), it performs exactly \(\tau_{xy}\).
3. On each companion top, it also performs one label transposition.
4. At every \(1\le q\le H\), it has the exact one-sided annular
   derivative of the two-base conveyor, while the opposite signed
   derivative is zero.

#### Proof

Lemma 1.1 identifies the chosen focal frame with the direct edge of the
three-top conveyor.  The endpoint telescope makes the path through
\(a\) equal to the second positional-base derivative.  The audited
inner-arm cancellation gives exact middle equality, and the disjoint
context argument gives squarefreeness on both shores.  Equation (1.4)
proves the focal action; the two companion frames are likewise changed
from plus to minus within one fixed positional base.  The all-depth
derivative is exactly the one already calculated for the conveyor.
\(\square\)

This theorem changes the induced order on any previously protected core
which contains \(x,y\).  If \(U\) lies in a maximal placeholder cell
with fixed core \(C_0\) and \(x\in C_0\), at least one companion top
omits a label of \(C_0\) and lies outside that cell.  Thus the move
crosses the cell boundary which made the old ordered-core histogram
invariant.

## 2. Exact safe-port census

Fix \(1\le\delta\le H\), put

\[
                         \ell=H+\delta,
             \qquad     L=\ell-1\le2H-1.                      \tag{2.1}
\]

For a cyclic frame, mark every ordered length-\(L\) interval as a safe
de Bruijn port.

### Lemma 2.1 (one swapped frame changes exactly \(2L\) ports)

Let two placeholder positions have both open gaps at least \(4H-2\).
Swapping their two labels changes exactly \(2L\) marked ordered ports.

#### Proof

No length-\(L\) interval contains both placeholder positions because
\(L\le2H-1<4H-2\).  Each position belongs to exactly \(L\) cyclic
length-\(L\) intervals, so the two families are disjoint and contain
\(2L\) intervals in total.

An interval containing neither position is unchanged.  An interval
containing one position has a different label in that same ordered
slot, and hence changes. \(\square\)

### Theorem 2.2 (exact packet port boundary)

The old and new three-top conveyor packets differ at exactly

\[
                             6L                               \tag{2.2}
\]

top-indexed ordered ports.  Every other marked port agrees literally.

Moreover, at every one of the changed ports there is a safe continuation
which attaches to exactly one shore.

#### Proof

Apply Lemma 2.1 independently on the three distinct tops.  Top identity
prevents cancellation between their port signatures, giving \(6L\).

At a changed exit port \(v\ne v'\), choose a label outside the support
of \(v\); this is possible since \(L<M\).  The injective \(\ell\)-word
with tail \(v\) is a continuation of one shore and not the other.  The
entry statement is symmetric. \(\square\)

Thus the conveyor does not make the old cycle-Markov quotient into a
splice congruence.  Instead it gives a literal lift between two
representatives, identifies the exact middle-owner collateral, and
localizes all required re-collaring to \(6L=O(H)\) ports.

## 3. Squarefree embedding and simultaneous switches

A global frame table is **middle-squarefree** if no middle owner occurs
in two selected frames.

### Theorem 3.1 (squarefree replacement principle)

Suppose a middle-squarefree global table contains the three old frames
of one conveyor packet.  Replacing them by the new packet preserves the
complete global middle-owner set and middle squarefreeness.

#### Proof

The old packet contributes \(3M\) distinct middle owners, and the new
packet contributes exactly the same set, again without repetition.
Every external frame was disjoint from the old set by global
squarefreeness, and is therefore disjoint from the new set. \(\square\)

### Corollary 3.2 (a disjoint catalyst bank)

Let a middle-squarefree table contain \(t\) old conveyor packets whose
top triples are pairwise disjoint.  Any subcollection may be switched
simultaneously.  If all \(t\) are switched, then

\[
 \begin{aligned}
  \text{distinct packet middle owners}&=3Mt,\\
  \text{changed ordered ports}&=6Lt,\\
  \frac{\text{changed ports}}{\text{packet owners}}
     &=\frac{2L}{M}.
 \end{aligned}                                                  \tag{3.1}
\]

In particular, if \(3Mt=\Theta(W)\) and \(H=o(m)\), then

\[
                         6Lt=O(HW/m)=o(W).                     \tag{3.2}
\]

#### Proof

Theorem 3.1 applies packet by packet.  Top-disjointness and initial
global squarefreeness make their middle supports disjoint.  The exact
counts follow from Theorem 2.2.  Finally \(L\le2H-1\) and
\(M=m+H\). \(\square\)

This proves that neither the number of changed literal ports nor the
need to leave a maximal placeholder cell forces an \(\Omega(W)\)
**port-count** toll.  It does not prove that repairing one changed port
has constant word cost.  Also unproved is the existence of the assumed
packet bank in a single coefficient-one squarefree factor.

There is nevertheless no shortage of disjoint **top triples**.

### Proposition 3.3 (a positive-density potential top resolution)

Fix three coordinates \(x,a,y\).  For every

\[
 C\in\binom{[n]\setminus\{x,a,y\}}{M-2},
\tag{3.3}
\]

form the top triple

\[
 C\cup\{x,y\},\qquad C\cup\{x,a\},\qquad C\cup\{a,y\}.        \tag{3.4}
\]

These triples are pairwise top-disjoint and partition all rank-\(M\)
tops containing exactly two of \(\{x,a,y\}\).  Their covered fraction
of the full top layer is

\[
 \frac{3\binom{n-3}{M-2}}{\binom nM}
 =\frac{3M(M-1)(n-M)}{n(n-1)(n-2)}
 =\frac38+o(1)                                                 \tag{3.5}
\]

when \(M=n/2+o(n)\).

#### Proof

A top containing exactly two fixed coordinates determines its omitted
member of the triple and the unique residual set \(C\), so (3.4)
partitions this stratum.  The displayed count and factorial
simplification give (3.5). \(\square\)

Each triple in (3.4) can be decorated as a conveyor independently at
the level of literal frame availability.  Proposition 3.3 does not make
their middle decks mutually disjoint.  Hence top capacity is
positive-density, while simultaneous middle-squarefree decoration is
the unresolved constraint.

## 4. Bounded-collateral core reordering

Regard the positions of a cyclic frame as \(\mathbb Z_M\), and join two
positions when they are conveyor-admissible.

### Lemma 4.1 (admissible transpositions generate the full symmetric group)

If \(M\ge8H\), the graph of conveyor-admissible position pairs is
connected.  More precisely, every adjacent positional transposition is
a product of three admissible transpositions.

#### Proof

Put \(s=4H-2\).  For adjacent positions \(p,p+1\), choose

\[
                         z=p+s+2\pmod M.                       \tag{4.1}
\]

The two open gaps between \(p,z\) have sizes \(s+1\) and
\(M-s-3\), both at least \(s\) because \(M\ge8H=2s+4\).  The gaps
between \(p+1,z\) have sizes \(s\) and \(M-s-2\), again both at least
\(s\).  Hence both pairs are admissible.  The group identity

\[
             (p\ z)(p+1\ z)(p\ z)=(p\ p+1)                    \tag{4.2}
\]

proves the assertion.  Adjacent transpositions generate
\(S_M\). \(\square\)

For the Gaussian regime one can sharpen this to a uniform three-move
statement.

### Lemma 4.2 (one common far buffer)

If \(M\ge16H\), every two positions \(p,q\) have a position \(z\)
which is conveyor-admissible with both.  Consequently

\[
                         (p\ z)(q\ z)(p\ z)=(p\ q).            \tag{4.3}
\]

#### Proof

For a fixed position, fewer than \(2(4H-1)\) positions fail the open-gap
condition.  The union of the two forbidden sets for \(p,q\) has size
less than \(16H\).  Since \(M\ge16H\), a permissible \(z\) exists;
at equality, the strict forbidden-set bound still leaves one position.
Identity (4.3) is immediate. \(\square\)

### Theorem 4.3 (seven-top focal transposition gadget)

Assume \(M\ge16H\), and prescribe any two labels \(x,y\) in a focal
frame on \(U\).  Choose a common far buffer label \(z\in U\) as in
Lemma 4.2 and three distinct auxiliary labels

\[
                         a_1,a_2,a_3\notin U.                  \tag{4.4}
\]

There is an explicit sequence of three conveyors which

1. swaps \(x,y\) on the focal top and restores \(z\) to its old
   position;
2. uses six pairwise distinct companion tops, hence seven tops in all;
3. preserves the global middle-owner set and squarefreeness after every
   step whenever the seven prescribed old frames occur in a
   middle-squarefree table; and
4. performs at most \(18L\) ordered-port edits.

#### Proof

Apply Theorem 1.2 successively to the focal positional pairs

\[
                         (p,z),\qquad(q,z),\qquad(p,z),         \tag{4.5}
\]

where \(p,q\) are the positions initially occupied by \(x,y\).  At each
step the current labels in the displayed positions are used as the two
placeholders.  Equation (4.3) gives the final focal permutation.

Use auxiliary label \(a_i\) at step \(i\).  The two companion tops at
one step are obtained by replacing one of the two current focal labels
by \(a_i\).  Different auxiliary labels make all six companions
distinct, while none equals \(U\).  The assumption \(M\ge16H\) implies
\(m-H=n-M\ge3\), so the auxiliaries exist.

Apply Theorem 3.1 after each switch.  Finally Theorem 2.2 gives at most
\(3\cdot6L=18L\) port edits. \(\square\)

The six companion frames finish in their opposite orientations.  The
theorem does not restore them.  Therefore it is a bounded-collateral
core-reordering theorem, not a closed seven-top identity acting only on
the focal frame.

### Corollary 4.4 (the maximal ordered-core invariant is crossed)

At \(M\ge16H\), any transposition of two labels in the protected core
of a maximal placeholder cell can be realized on a focal top by three
conveyors, provided the six prescribed companion frames are available;
the companions lie outside or across the cell boundary.  Thus the
cornerwise ordered-core histogram is not invariant on any global fibre
which contains this bounded catalyst configuration.

In particular, the even/odd three-label core sectors used by the
ordered-core antisymmetrizer are separated by only bounded conveyor
distance, subject to availability of the prescribed companions.  One
selected frame needs at most three conveyors; applying one fixed odd
transposition to all three frames on an antisymmetrizer shore needs at
most nine.

## 5. What boundedly many conveyors still cannot do

For cyclic orders \(\pi,\rho\) on the same top, define their deletion
distance

\[
 d_{\rm del}(\pi,\rho)=
 \min\{|S|:\operatorname{ord}_{U\setminus S}(\pi)
        =\operatorname{ord}_{U\setminus S}(\rho)
        \text{ up to rotation/reversal}\}.                    \tag{5.1}
\]

### Theorem 5.1 (hereditary core stability)

If a sequence of conveyor moves touches one fixed top \(b\) times, and
changes its frame from \(\pi\) to \(\rho\), then

\[
                         d_{\rm del}(\pi,\rho)\le2b.           \tag{5.2}
\]

#### Proof

At every touch, the conveyor swaps exactly two labels and fixes every
other positional label on that top.  Let \(S\) be the union of all
labels used as placeholders at those \(b\) touches.  Then \(|S|\le2b\),
and every label outside \(S\) remains forever in its original position.
Deleting \(S\) from the initial and final orders gives the same induced
cyclic order. \(\square\)

This is an exact invariant for bounded move sequences.  It is much
weaker than the old full ordered-core histogram, because one touch can
already change a three-label parity sector, but it prevents bounded
uniform diameter.

### Proposition 5.2 (orders at linear conveyor distance)

For infinitely many \(M\), there are cyclic orders \(\pi,\rho\) on an
\(M\)-set satisfying

\[
                         d_{\rm del}(\pi,\rho)\ge M-8\sqrt M. \tag{5.3}
\]

Consequently every conveyor sequence between them touches that top at
least

\[
                         \frac M2-4\sqrt M                    \tag{5.4}
\]

times.

#### Proof

Take \(M=k^2\) labels \((i,j)\in[k]^2\).  Let \(\pi\) be row-major
order and \(\rho\) column-major order.  A common linear subsequence of
these two orders is a chain in both coordinates, and has length at most
\(2k-1\).  A common subsequence of one cyclic rotation of \(\pi\) and
one cyclic rotation of \(\rho\) splits at the two wrap points into at
most four such chains, and therefore has length less than \(8k\).

If one order is reversed, the corresponding pieces are decreasing in
one coordinate and increasing in the other, so the same \(8k\) upper
bound remains valid.  Hence every common cyclic subsequence up to
dihedral symmetry has length less than \(8k\).  Deleting a set \(S\)
which makes the orders equal would leave a common cyclic subsequence of
length \(M-|S|\), proving (5.3).  Combine with Theorem 5.1 to obtain
(5.4). \(\square\)

### Corollary 5.3 (statewise positive-density obstruction)

Suppose two frame tables differ by pairs of orders satisfying (5.3) on
\(R\) distinct tops.  Every conveyor route between the tables has at
least

\[
                         \frac{R(M-8\sqrt M)}6                \tag{5.5}
\]

moves.

#### Proof

The sum of top-touch counts is three times the number of conveyor moves.
Apply (5.4) at all \(R\) tops and sum. \(\square\)

If \(R=\Theta(W/M)\), the lower bound is \(\Theta(W)\) moves.  This is a
genuine statewise obstruction to a uniformly bounded-per-cell
core-mixing theorem.  It is not yet an obstruction to coefficient one,
because no theorem forces the desired initial and final factors to be
deletion-far on \(\Theta(W/M)\) tops.

## 6. The fixed-common-core collateral parity

There is also an exact but chart-local collateral invariant.  Fix one
\((M-2)\)-set \(C\).  Index its pair tops by edges \(uv\) of the outside
label set.  For a sequence of conveyors all having common core \(C\),
let \(t_{uv}\in\mathbb F_2\) record whether top \(C\cup\{u,v\}\) is
touched an odd number of times.

### Proposition 6.1 (star parity)

For every outside label \(u\),

\[
                         \sum_{v\ne u}t_{uv}=0\pmod2.          \tag{6.1}
\]

In particular, conveyors with one fixed common core cannot change only
one pair top and return all companion tops.

#### Proof

One conveyor touches the three edges of a triangle on outside labels.
Every vertex of that triangle has degree two.  Hence every star sum in
(6.1) changes by zero.  It is zero before any moves and remains zero.
\(\square\)

Changing common cores, as in Theorem 4.3, escapes this one-chart parity,
but leaves the bounded-collateral and deletion-distance statements in
force.

## 7. Exact global gate

Define the **conveyor packet hypergraph** of a squarefree frame table
\(\mathcal F\) as follows.

* Its vertices are the selected literal frames of \(\mathcal F\).
* A hyperedge is a triple which, for some common \((M-2)\)-core and
  labels \(x,a,y\), is exactly the old shore (1.6) of a two-base
  conveyor.

Because \(\mathcal F\) has one frame per selected top, a matching in
this hypergraph is precisely a top-disjoint bank to which Corollary 3.2
applies.

### Theorem 7.1 (exact reduction)

A matching of size \(t\) in the conveyor packet hypergraph yields an
exact middle-squarefree family of \(2^t\) frame tables, all with the
same middle-owner set, in which each chosen packet may be switched
independently.  The total port boundary between any two such tables is
at most \(6Lt\).

If

\[
                         t=\Theta(W/M),                         \tag{7.1}
\]

then this gives positive middle-owner-mass core/port reordering with
\(o(W)\) changed-port boundary.  It gives \(o(W)\) literal word toll
only under a separate \(O(1)\)-cost port-splice or shared-collar lemma.

#### Proof

Matching hyperedges have disjoint frame/top sets.  Global
squarefreeness makes their owner supports disjoint, while Theorem 3.1
makes each switch preserve its own exact owner support.  Therefore all
switches commute and all \(2^t\) choices remain squarefree.  Sum the
port bound of Theorem 2.2.  Equation (3.2) proves the final assertion.
\(\square\)

Theorem 7.1 is the reusable positive reduction.  It also isolates what
is not proved by the local conveyor theorem: a general squarefree factor
need not contain even one prescribed \(\omega/\omega'\) triple, and no
matching or switching theorem currently gives (7.1).

## 8. Final verdict

The three-top conveyor passes the local catalyst audit.

* One move changes literal ordered ports and one focal core order.
* It preserves the exact complete middle-owner support and
  squarefreeness.
* The changed-port boundary is exactly \(6(H+\delta-1)\).
* Three moves give any focal transposition at Gaussian scale, with six
  changed companion frames.
* A positive-density disjoint packet bank would have only \(o(W)\)
  changed-port boundary; its word-length toll remains conditional on a
  collar compiler.

It does **not** supply a free quotient or a closed focal switch.  The
companions carry real collateral, a fixed-core bank obeys star parity,
and boundedly many touches preserve all but boundedly many labels of
each ordered core.  Hence it crosses the former three-label obstruction
but does not prove global core mixing.

The constant-one frontier is now the matching statement (7.1), or a
different construction which manufactures the prescribed companion
frames while maintaining one common squarefree middle factor.

## 9. Dependency ledger

The literal three-top exchange, exact middle support, squarefreeness,
and all-depth derivatives are in
`MATH_THEOREM_THREE_TOP_TWO_BASE_PROMOTION_CONVEYOR_20260726.md`.
The ordered-port splice-noncongruence is in
`MATH_THEOREM_SAFE_DEBRUIJN_FULL_CYCLE_MARKOV_QUOTIENT_PORT_NONCONGRUENCE_20260726.md`.
The maximal placeholder-cell ordered-core invariant is in
`MATH_THEOREM_MAXIMAL_PLACEHOLDER_CELL_ORDERED_CORE_INVARIANT_20260726.md`.
