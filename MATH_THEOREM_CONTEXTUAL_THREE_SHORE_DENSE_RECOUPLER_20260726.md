# Contextual three-shore recoupling: dense exact factors and the remaining outer Hall gate

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

An earlier proof of the transition-density lower bound used only unequal
fixed-block shore sizes and was invalid: selected windows form an edge
cover, not a matching of target shores.  The corrected occurrence-capacity
theorem in Section 10 of
`MATH_THEOREM_FIRST_ELIGIBLE_B4_SCD_PACKET_FACTOR_20260726.md` restores the
same order of necessity by comparing the invariant shore imbalance with
the finite budget of (W) directed starts. Against that corrected lower
bound, the following positive construction is valid. There is an explicit
local three-shore resolver on 24 middle owners. Tensoring it in the canonical
first-eligible packets gives, for every packet-dependent shore schedule,

1. exact middle ownership on all retained owners;
2. physical isometric \(C_{2h}\)'s;
3. injective lower and upper consecutive-shadow maps on the whole packet
   simultaneously through depth \(h/2\); and
4. a tunable density of changed-shore transition labels and, after an
   affine dispersion of direction pairs, a \((1-o(1))\)-fraction of
   invariant-breaking windows at Gaussian depth--but not the
   Gaussian-scale transport magnitude required for coverage.

The audit distinguishes two notions which must not be conflated. A
periodic shore schedule of period \(L\asymp\sqrt m\), whose phase is an
arbitrary function of the frozen packet exterior, realizes

\[
             \Omega(h/\sqrt m)\quad\hbox{sites per strip}.       \tag{0.1}
\]

changed-frame labels per strip. Under the sibling direction schedule,
these labels preserve the corrected block invariant and do not escape the
obstruction. Affine dispersion breaks the invariant only by a short
distance and is also insufficient. The successful transport geometry must
cluster the two directions of many local blocks in the same Gaussian
window. The exact ownership identity for such a construction is isolated
in `MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`.

What remains is genuinely outer.  One must choose the packet-constant shore
schedules and the affine conjugates of the cell factors so that shadows of
different packets cover almost all physical targets.  The local theorem
below gives injectivity inside every packet, but not the required global
component-Hall matching.

## 1. The three exact local shores

Use eight coordinates split as

\[
 A=\{a,b,c,d\},\qquad R=\{u,v,w,x\}.
\]

Put

\[
 \mathcal X=\binom A2,qquad
 \mathcal Y=\{uw,ux,vw,vx\},\qquad
 \mathcal V=\{X\cup Y:X\in\mathcal X,\ Y\in\mathcal Y\}.       \tag{1.1}
\]

Thus \(|\mathcal V|=24\), and every member has rank four.  Let

\[
 M_0=ab\mid cd,\qquad M_1=ac\mid bd,\qquad M_2=ad\mid bc       \tag{1.2}
\]

be the three perfect matchings of \(A\).  For \(M_j=Z_j^0\mid Z_j^1\),
the four special two-sets in \(\mathcal X\setminus M_j\) form a physical
square; denote it by \(Q_j\).  The reservoir states \(\mathcal Y\) form
the physical square \(Q_R\).  Define

\[
 \mathscr D_j=
 \{Q_j\cup Y:Y\in\mathcal Y\}
 \ \dot\cup\ 
 \{Z_j^0\cup Q_R,\ Z_j^1\cup Q_R\}.                 \tag{1.3}
\]

### Lemma 1.1 (three-shore owner identity)

Each \(\mathscr D_j\) partitions the same 24-owner support \(\mathcal V\)
into six physical \(Q_2=C_4\)'s.

#### Proof

The four main cells use the four special states outside \(M_j\), once at
each reservoir orientation.  The two reservoir cells use the two states
in \(M_j\), at all four reservoir orientations.  Hence all six special
two-sets, and therefore all 24 products in (1.1), occur exactly once.
Every displayed cell is a product of two disjoint coordinate pairs. \(\square\)

At rank two in the special block this is the atomic frame recoupler:
the three resolutions

\[
 \binom A2=(\mathcal X\setminus M_j)\ \dot\cup\ M_j              \tag{1.4}
\]

replace one active \(Q_2\) and two passive owners by another such
resolution.  No smaller common rank-two support contains two distinct
physical \(Q_2\)'s together with all owners omitted by both: two distinct
squares in \(J(4,2)\) have union \(\binom A2\).  The reservoir square in
(1.3) is what upgrades this six-owner atom to six equal-dimensional cells,
so it can be tensored without variable-dimensional seams.

Relative to shore zero, call a main cell in shore one or two
**recoupled**.  Both directions of such a cell use a different special
pair frame.  Reservoir cells retain the common \(Q_R\) directions.

## 2. Context-dependent tensor shores preserve exact ownership

Take \(r\) disjoint eight-blocks carrying copies of \(\mathcal V\).  In a
canonical first-\(r\)-eligible packet the owner support is

\[
                         \mathcal P\cong\mathcal V^r.             \tag{2.1}
\]

The first-eligible definition makes the selected block set and the
exterior constant on \(\mathcal P\).  Consequently a shore vector may be
an arbitrary function of that frozen packet data:

\[
 \epsilon(\mathcal P)=
 (\epsilon_1(\mathcal P),\ldots,\epsilon_r(\mathcal P))
 \in\{0,1,2\}^r.                                      \tag{2.2}
\]

Tensoring (1.3) in the selected shores partitions \(\mathcal P\) into

\[
                         6^r\quad Q_{2r}\text{-cells}.            \tag{2.3}
\]

Let

\[
                         h=2r
\]

be a power of two.  On each cell install an affine conjugate of the
recursive nonlinear factor \(F_h\).  Its cycles have length \(2h=4r\),
and its forward and reverse encoded-shadow maps are injective through
depth \(h/2=r\).

### Theorem 2.1 (contextual exact packet factor)

For every packet-dependent shore field (2.2), the resulting cycles

1. partition every owner in every retained packet exactly once;
2. are physical isometric \(C_{2h}\)'s; and
3. have injective physical lower and upper shadow maps on each entire
   packet, simultaneously for every \(q\le h/2\).

The canonical packet union omits only \(e^{-\Omega(m)}W\) middle owners
when \(r=o(m)\) lies below a fixed positive multiple of \(m\).

#### Proof

Lemma 1.1 makes (2.3) an exact product partition, independently in every
packet and independently of its chosen shore vector.  The recursive
factor partitions every cell into physical \(C_{2h}\)'s.

Inside one cell, both signed shadow maps are injective through \(h/2\).
For two different product cells, choose a local block where their six-cell
labels differ.  Two main cells retain different reservoir two-sets; two
reservoir cells retain different special two-sets.  A main and a reservoir
cell have different special/reservoir cardinality signatures as soon as a
local direction is used, and have disjoint owner supports if none is used.
Thus their local lower images are disjoint for arbitrary local depths
\(0,1,2\), and the same is true of upper images.  Hence different product
cells have disjoint physical shadow images.  This proves packet-wide
injectivity.

The final leave estimate is the standard first-eligible Chernoff bound:
one unbiased eight-block is eligible with probability \(24/256=3/32\),
and conditioning the total rank to be middle costs only a polynomial
factor. \(\square\)

## 3. Exact transition density

Suppose a packet shore vector has

\[
 t(\mathcal P)=\#\{i:\epsilon_i(\mathcal P)\ne0\}                 \tag{3.1}
\]

recoupled slots.  At one such slot, four of the six local cells are main
and two are reservoir.  All product cells contain the same number of
owners and the same number of \(C_{2h}\)'s.  A recoupled main cell has two
marked directions, and every direction occurs exactly twice on a physical
\(C_{2h}\).  A reservoir cell has no marked direction.  Therefore the
exact packet-average number of affected transition positions per strip is

\[
              4\cdot\frac46\,t(\mathcal P)
              =\boxed{\frac83t(\mathcal P)}.           \tag{3.2}
\]

Choose the recursive direction tree so that the two directions of every
local slot are siblings.  Every window of at most \(r=h/2\) transitions
uses at most one direction from a local slot.  A window avoiding all
marked transitions consequently uses distinct slots, and in every slot it
uses an old-shore main direction or a reservoir direction.  It is native
for the old fixed-label ledger.

This does **not** make the marks in (3.2) a certificate for the corrected
occurrence theorem.  Every main or reservoir cell is active on a
four-block at local middle rank two.  A one-direction local window has
lower rank one and upper rank three, independently of which shore was
chosen.  It therefore preserves the stronger invariant

\[
 Z=\#\{\text{rank-four blocks}\}
   -\#\{\text{rank-zero blocks}\}.                   \tag{3.2a}
\]

### Corollary 3.1 (periodic/Markov density calibration)

Let \(L=L(m)\), and let the frozen exterior of packet \(\mathcal P\)
choose a phase \(s(\mathcal P)\in\mathbb Z/L\mathbb Z\).  Put a nonzero
shore at slots

\[
 i\equiv s(\mathcal P)\pmod L,                       \tag{3.3}
\]

allowing the choice between shores one and two to be any finite-state
function of the frozen exterior between successive eligible blocks.  Use
shore zero elsewhere.  Then

\[
 t(\mathcal P)=\frac rL+O(1),\qquad
 \text{affected sites/strip}
 =\frac{4h}{3L}+O(1).                                 \tag{3.4}
\]

In particular \(L\asymp\sqrt m\) gives

\[
                  \Theta(h/\sqrt m)                  \tag{3.5}
\]

affected sites per strip, while retaining every conclusion of Theorem
2.1.  Taking a positive density of nonzero shores gives \(\Theta(h)\)
affected sites.

This proves only that the old-label change density can be realized exactly
by a context-dependent periodic or Markov shore schedule.  It does not
escape (3.2a), and hence it does not route the corrected outer deficit.

### Proposition 3.2 (shore changes with sibling directions are inert)

For the sibling direction schedule and every \(q\le r\), every lower/upper
window in every shore has

\[
                         Z(L)=Z(U).                   \tag{3.6}
\]

Consequently, at \(q=\lfloor c\sqrt m\rfloor\) for every sufficiently
small fixed \(c>0\), the corrected occurrence-capacity theorem gives

\[
                         M_q^-+M_q^+=\Omega(W)         \tag{3.7}
\]

for any near-spanning union of these packet factors.

#### Proof

A \(q\)-window uses at most one direction in every local slot.  In its
active four-block the local lower/upper ranks are therefore one and three;
in the other four-block of the eight-coordinate slot they are both two.
Untouched blocks have identical restrictions on both signs.  Hence no
rank-zero or rank-four count changes, proving (3.6).  Apply Theorem 10.1
and Corollary 10.3 of the first-eligible B4 note with \(B_q^Z=0\). \(\square\)

The obstruction disappears if the two directions of a local slot are
dispersed rather than made siblings.

### Theorem 3.3 (affine pair dispersion breaks the invariant)

Fix one \(Q_h\)-cell, with (h=2r), and conjugate its recursive factor by a
uniform random permutation of the (h) cube directions.  For every fixed
directed depth-(q) start, (q\le r), the probability that its direction set
contains no complete local direction pair is

\[
 p_0(h,q)=\frac{2^q\binom rq}{\binom{2r}q}
 =\prod_{j=0}^{q-1}\frac{2(r-j)}{2r-j}
 \le \exp\!\left(-\frac{q(q-1)}{2h}\right).          \tag{3.8}
\]

There is therefore a deterministic direction conjugate in every cell for
which at most (p_0(h,q)) of its directed starts preserve (Z).  These
choices may be made independently over all cells and all packets without
changing middle ownership or either packet-wide shadow injectivity.

If

\[
 q=\lfloor c\sqrt m\rfloor,\qquad
 \sqrt m\ll h=o(m),                                   \tag{3.9}
\]

then (p_0(h,q)=e^{-\Omega(m/h)}=o(1)).  Thus a
deterministic exact near-factor exists in which

\[
                         B_q^Z=(1-o(1))W.              \tag{3.10}
\]

#### Proof

Every cycle window of the recursive factor uses (q) distinct directions.
After a uniform coordinate permutation, that direction set is a uniform
(q)-subset of the (2r) directions.  It contains no complete member of the
fixed perfect matching into (r) local pairs precisely when it chooses
(q) distinct pairs and one endpoint of each, proving the equality in
(3.8).  The product bound follows from

\[
 \frac{2(r-j)}{2r-j}=1-\frac{j}{2r-j}
 \le e^{-j/h}.
\]

If a window contains both directions of (d\ge1) local cells, each such
active four-block has lower rank zero and upper rank four.  All partial or
untouched cells contribute equally to (Z) on the two signs, so

\[
                         Z(U)-Z(L)=2d>0.              \tag{3.11}
\]

Hence (Z)-preservation is exactly the no-complete-pair event.  Averaging
the number of preserving starts over the random direction conjugate gives
(p_0) times the number of cell vertices, so some conjugate attains at most
that value.  Direction conjugacy preserves the exact recursive cycle
factor and its two-sided trace injectivity.  Summing independently chosen
good conjugates over all cells proves (3.10); (3.9) makes the exponent in
(3.8) tend to infinity. \(\square\)

Theorem 3.3 passes the binary escape count of Corollary 10.3, but it fails
the stronger bounded-Lipschitz transport test of Theorem 11.2.  Under the
same uniform direction conjugate, the expected number (d) of completed
local pairs in a (q)-window is

\[
 \mathbb Ed=
 r\frac{q(q-1)}{h(h-1)}
 =\frac{q(q-1)}{2(h-1)}.                              \tag{3.12}
\]

At (q=\Theta(\sqrt m)) and (\sqrt m\ll h=o(m)), this is
(\Theta(m/h)=o(\sqrt m)), whereas Corollary 11.3 requires average
(\Omega(\sqrt m)).  Thus random affine dispersion makes almost every
window change (Z), but moves it too short a distance.  It is not an outer
solution.

The exact successor target is a **pair-clustered rainbow factor**: retain
packet-wide two-sided trace injectivity while arranging that a typical
Gaussian window contains (\Theta(q)) complete local direction pairs.  No
such factor is proved here.

## 4. The evident block invariant is balanced in the full frame catalogue

There is no parity-count obstruction to mixing all three local frames.
This can be stated as an exact face-level theorem.

Partition \([2m]\) into \(b=m/2\) quartets (the bounded leftover when
needed is harmless).  Fix a parity vector
\(\eta\in\{0,1\}^b\), and let

\[
 \mathcal P_\eta=
 \{S:|S\cap B_i|\equiv\eta_i\pmod2\text{ for every }i\}.        \tag{4.1}
\]

Grade it by

\[
 r_\eta(S)=\frac{|S|-|\eta|}{2}.                                \tag{4.2}
\]

The local even-parity poset has level sizes \((1,6,1)\): one symmetric
chain \(\varnothing<A<B_i\) and five singleton middle chains give an SCD.
The local odd-parity poset has level sizes \((4,4)\); its inclusion graph
is \(K_{4,4}\) minus a perfect matching, hence has a perfect matching and
an SCD.  Products of symmetric-chain orders have symmetric-chain
decompositions.  Therefore \(\mathcal P_\eta\) has an SCD.

### Theorem 4.1 (exact parity-component face matching)

For every \(q\) and every parity vector for which the two layers are
nonempty, there is a bijection

\[
 \Phi_{\eta,q}:
 \mathcal P_\eta\cap\binom{[2m]}{m-q}
 \longrightarrow
 \mathcal P_\eta\cap\binom{[2m]}{m+q}               \tag{4.3}
\]

such that

\[
                         S\subset\Phi_{\eta,q}(S).                \tag{4.4}
\]

Every pair in (4.4) is the intersection/union pair of a physical
\(q\)-face in a product of local quartet pair frames chosen from
\(M_0,M_1,M_2\).

#### Proof

Complementation is rank reversal on \(\mathcal P_\eta\), because every
quartet has even size.  Thus the two levels in (4.3) are complementary
levels of equal size.  In an SCD, match the two members of each chain at
those complementary ranks.  This proves (4.3)--(4.4).

In one quartet, the local difference
\(D=\Phi(S)\setminus S\) has size zero, two, or four.  If \(|D|=2\),
choose the unique perfect matching having \(D\) as one pair; varying that
pair gives local intersection \(S\cap B_i\) and union
\(\Phi(S)\cap B_i\).  If \(|D|=4\), choose any perfect matching and vary
both pairs.  Taking the product over blocks gives a physical face of total
dimension \(q\). \(\square\)

The theorem is deliberately a face theorem, not a consecutive-window
factor.  It proves that once all three frame choices are admitted, the
frame-independent local-rank-parity components have exactly balanced
lower and upper capacities.  Hence the linear Gaussian obstruction from a
single fixed label pairing is not a universal invariant of contextual
frame recoupling.

## 5. Remaining local code and outer Hall theorems

For every retained packet \(P\), let \(\mathfrak O(P)\) be the collection
of all choices consisting of

* a packet-constant shore vector in \(\{0,1,2\}^r\); and
* one affine conjugate of \(F_h\) in each of its \(6^r\) product cells.

Every option \(o\in\mathfrak O(P)\) gives injective physical maps

\[
 \tau_{P,o,q}^{\pm}:P\longrightarrow
 \binom{[2m]}{m\pm q},\qquad q\le h/2.               \tag{5.1}
\]

The owner partition and intrapacket separation are complete, but the
bounded-Lipschitz audit adds the local pair-clustered context-code theorem
from `MATH_THEOREM_PARITY_COMPLETE_MAPPING_PAIRED_ORDER_LIFT_20260726.md`.
Assuming that local theorem, the remaining global statement is the following
multiple-choice outer Hall theorem:

> Choose one option \(o(P)\in\mathfrak O(P)\) for every packet so that
> \[
>  \sum_{q\le H}\left(
>   N_q-\left|\bigcup_P\tau^-_{P,o(P),q}(P)\right|
>  +N_q-\left|\bigcup_P\tau^+_{P,o(P),q}(P)\right|
>  \right)=o(W).                                      \tag{5.2}
> \]

The choices in (5.2) automatically preserve exact middle ownership and
whole physical cycles. Theorem 2.1 removes every intrapacket collision,
Theorem 4.1 removes the evident parity-capacity obstruction at face level,
and Theorem 11.2 of the first-eligible note supplies the additional
pair-clustering constraint which any admissible option family must meet. What is
not proved is that component-constant shore choices and consecutive affine
traces satisfy the outer Hall inequalities simultaneously at every depth.

Thus there are two sharply separated gates in this construction:

1. the parity-complete, pair-clustered trace code inside a cell; and
2. the component-constant outer Hall choice (5.2).

A periodic shore schedule or a randomly dispersed affine schedule solves
neither one by itself.
