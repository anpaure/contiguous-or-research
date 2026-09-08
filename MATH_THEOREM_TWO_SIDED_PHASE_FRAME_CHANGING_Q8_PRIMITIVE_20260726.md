# A two-sided phase-frame-changing `Q_8` primitive

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The phase-synchronized crossed construction admits a choice for which both
the successor and predecessor direction relations are exact.

Use the standard common-phase `Q_4` factor, let

\[
                         K=(1\ 2\ 3\ 4),
 \qquad                  S=(2\ 4),                            \tag{0.1}
\]

and form the corrected `Q_8` maps `P_0,P_1` below.  Then

\[
 \delta^+_{P_1}=\Xi^+\delta^+_{P_0},
 \qquad
 \delta^-_{P_1}=\Xi^-\delta^-_{P_0}                         \tag{0.2}
\]

at the same owner, where

\[
 \begin{aligned}
 \Xi^+(Li)&=R(Si),&\Xi^+(Ri)&=L(Si),\\
 \Xi^-(Li)&=R(SKi),&\Xi^-(Ri)&=L(SKi).
 \end{aligned}                                             \tag{0.3}
\]

Both `Xi+` and `Xi-` are fixed-point-free involutions, because

\[
                         S=(2\ 4),
 \qquad                  SK=(1\ 4)(2\ 3).                    \tag{0.4}
\]

Every component of both factors is an isometric `C_16`.  Moreover, in an
actual `P_1` cycle the ambient adjacent-direction perfect matching changes
with phase parity: the even and odd matchings are distinct, and their union
is the Hamilton eight-cycle of the first-half direction word.  Forward and
backward aligned windows use the same parity-indexed matching.  This is an
exact two-sided frame primitive, not merely an outgoing twist.

The primitive is still bounded and retains the bottom `Q_4` two-wire
partition.  It therefore does not by itself solve outer integral mixing or
literal physical support recovery.

## 1. Construction

Let `G` be the standard common-phase `Q_4` factor with direction word

\[
                         1234\,1234.
\]

Write its outgoing and incoming direction functions as `delta+` and
`delta-`.  In phase notation `c in Z_4`,

\[
                         \delta^+(c)=d(c),
 \qquad                  \delta^-(c)=d(c-1)=K^{-1}d(c).       \tag{1.1}
\]

For `(u,v) in Q_4^L x Q_4^R`, let

\[
                         \epsilon=|u|+|v|\pmod2
\]

and define

\[
 P_0(u,v)=
 \begin{cases}
  (G(u),v),&\epsilon=0,\\
  (u,G(v)),&\epsilon=1,
 \end{cases}                                              \tag{1.2}
\]

\[
 P_1(u,v)=
 \begin{cases}
  (u,v+e_{S\delta^+(u)}),&\epsilon=0,\\
  (u+e_{S\delta^+(v)},v),&\epsilon=1,
 \end{cases}
 \qquad S=(2\ 4).                                        \tag{1.3}
\]

The shorewise translation argument proves that `P_1` is a neighbour
permutation.  Since `S` preserves the two syndrome-column classes
`{1,3}` and `{2,4}`, Proposition 3.2 of the phase-synchronized associator
theorem applies.  Every `P_1` phase pair evolves as

\[
                         (c,c')\longmapsto(c-1,c'+1)         \tag{1.4}
\]

after two moves.  Hence every coordinate on each child side is used once
before complement, proving that `P_1` is an isometric `C_16`-factor.
The same is true of `P_0`.

## 2. Exact successor and predecessor frames

### Theorem 2.1 (two-sided frame identity)

Equations (0.2)--(0.4) hold at every owner.

#### Proof

At an even owner, `P_0` leaves by `L delta+(u)` and `P_1` leaves by
`R S delta+(u)`.  At an odd owner the identical relation holds with `L,R`
interchanged and `u` replaced by `v`.  This proves the successor identity
with `Xi+`.

Now fix a target owner `(u,v)`.  If its total parity is even, its `P_0`
predecessor is odd and enters in right direction

\[
                         R\delta^-(v).
\]

Its `P_1` predecessor is obtained by the inverse translation in (1.3) and
enters in left direction

\[
                         L S\delta^+(v).
\]

By (1.1), if `i=delta-(v)` then `delta+(v)=Ki`; hence the latter direction
is `L SKi`.  At an odd target, the same calculation interchanges `L,R`.
This is exactly the predecessor identity with `Xi-`.

Finally `S^2=1`.  Direct multiplication gives `SK=(1 4)(2 3)`, also an
involution.  A cross-side permutation built from an involution squares to
the identity and has no fixed coordinate.  Thus both maps in (0.3) are
fixed-point-free involutions. \(\square\)

The distinction `Xi+ != Xi-` is necessary here.  Requiring one common
relative permutation would force `S K=S`, hence `K=1`, which is impossible
for a nondegenerate isometric parent cycle.

### Corollary 2.2 (four-stage frame carousel)

Put

\[
                         S_j=S K^j\qquad(j\in\mathbb Z_4),       \tag{2.1a}
\]

with `S=(2 4)`.  Every `S_j` is a reflection in the dihedral group
`S_2 wr S_2`, hence every forced crossed map `P_1^(j)` is an isometric
`C_16`-factor.  If `Xi_j^+,Xi_j^-` denote its successor and predecessor
frames, then

\[
                         \boxed{\Xi_j^-=\Xi_{j+1}^+}            \tag{2.1b}
\]

cyclically modulo four.

#### Proof

The phase-only classification contains the full dihedral group generated
by `S,K`.  Since `S` is a reflection, all `S K^j` are reflections and are
involutions.  Theorem 2.1 gives

\[
                         \Xi_j^-=\operatorname{cross}(S_jK)
                         =\operatorname{cross}(S_{j+1})
                         =\Xi_{j+1}^+.
\]

After four stages `S_4=S`, so the interfaces close. \(\square\)

Thus the failure of one shore to have `Xi+=Xi-` produces a finite
phase-synchronized holonomy rather than an open seam.  Four bounded cells
have formally compatible interfaces: every predecessor frame is literally
the next successor frame.  This is a frame-level composition statement;
an owner-support substitution theorem for four cells is still required
before calling the carousel one global exact factor.

## 3. The actual cycle changes pair frame

Let the first-half direction word of one `P_1` component be

\[
                         \omega=(w_0,w_1,\ldots,w_7).          \tag{3.1}
\]

Equation (1.3) makes it alternate right and left directions.  Define

\[
 \begin{aligned}
 M_0(\omega)&=\{\{w_0,w_1\},\{w_2,w_3\},
                  \{w_4,w_5\},\{w_6,w_7\}\},\\
 M_1(\omega)&=\{\{w_1,w_2\},\{w_3,w_4\},
                  \{w_5,w_6\},\{w_7,w_0\}\}.
 \end{aligned}                                             \tag{3.2}
\]

### Proposition 3.1 (phase-alternating ambient matching)

Both `M_0,M_1` are perfect matchings between the left and right direction
sets.  They are distinct, and

\[
                         M_0\cup M_1=C_8[\omega].              \tag{3.3}
\]

At a phase of parity `eta`, every aligned forward completed-pair window
uses edges of `M_eta`; every aligned backward/predecessor completed-pair
window ending at that phase also uses edges of `M_eta`.

#### Proof

The word alternates sides and contains every one of the eight directions
once, so (3.2) gives two left-right perfect matchings.  Consecutive edges
of a cyclic word alternate between the two matchings, proving (3.3) and
their distinctness.

A forward aligned window beginning at `t` groups

\[
 \{w_t,w_{t+1}\},\{w_{t+2},w_{t+3}\},\ldots,
\]

whose first indices all have parity `t`.  A backward aligned window ending
at `t` groups

\[
 \{w_{t-2},w_{t-1}\},\{w_{t-4},w_{t-3}\},\ldots,
\]

whose first indices have the same parity `t`.  This proves the two-sided
matching assertion. \(\square\)

For example, with initial phase pair `(0,0)`, the first-half word is

\[
 R1,L4,R2,L3,R3,L2,R4,L1.                              \tag{3.4}
\]

Thus

\[
 \begin{aligned}
 M_0&=\{R1L4,R2L3,R3L2,R4L1\},\\
 M_1&=\{R2L4,R3L3,R4L2,R1L1\}.
 \end{aligned}                                             \tag{3.5}
\]

Their union is visibly one alternating eight-cycle, not four inert wire
pairs.

### Proposition 3.2 (the whole factor is a `K_(4,4)` one-factorization)

Use zero-based direction labels `r,l in Z_4` on the right and left child.
For `gamma in Z_4`, put

\[
 M_\gamma=\bigl\{\{Rr,L(-r-\gamma)\}:r\in\mathbb Z_4\bigr\}.  \tag{3.6}
\]

The four `M_gamma` are pairwise edge-disjoint and partition all sixteen
edges of `K_(4,4)`.  Every `P_1` component alternates between two consecutive
members of this factorization.  Precisely, if its even starting phases are
`c,c'` and

\[
                         \sigma=c+c'\pmod4,
\]

then `sigma in {0,2}` is invariant and the component alternates between

\[
                         M_\sigma\quad\text{and}\quad M_{\sigma+1}. \tag{3.7}
\]

Both values of `sigma` occupy exactly half the owners.  Hence the complete
exact `P_1` factor realizes the full cross matching one-factorization with
balanced owner mass.

#### Proof

In zero-based labels the reflection `S=(2 4)` acts by `i -> -i`.  Under
(1.4), after `t` two-move blocks the phases are `c-t,c'+t`.  The first-half
word therefore has entries

\[
 w_{2t}=R(t-c),\qquad
 w_{2t+1}=L(-c'-t-1).                                \tag{3.8}
\]

Pairing `w_(2t)` with `w_(2t+1)` gives `M_(sigma+1)`, while pairing
`w_(2t+1)` with `w_(2t+2)` gives `M_sigma`.  The phase recurrence preserves
`sigma`.  Equal total parity forces `sigma` even, and the phase-pair set is
split equally between `sigma=0` and `sigma=2`.

For fixed `Rr`, the four values `L(-r-gamma)` are distinct as `gamma`
varies, so the four matchings partition `K_(4,4)`. \(\square\)

This balanced factorization is the precise finite option catalogue supplied
by the primitive.  It does not contradict the two-frame ceiling: one cycle
uses two frames, while the two owner sectors collectively use all four.

### Corollary 3.3 (exact cross-edge degree)

Across all 256 directed phase starts of `P_1`, every one of the sixteen
unordered cross edges `{Rr,Ll}` occurs as the aligned adjacent pair exactly
sixteen times.  Equivalently, the ambient-pair marginal is the uniform
measure on `E(K_(4,4))`.

#### Proof

Each `M_gamma` occurs on one quarter of all phase starts by Proposition
3.2.  Inside `M_gamma`, the four edges occur equally: an isometric doubled
word uses every first-half adjacent edge twice per cycle.  Thus every edge
has mass `256/(4*4)=16`. \(\square\)

The two-step codegree is not independent: consecutive pair frames are
forced to be `(M_0,M_1)` or `(M_2,M_3)`.  Therefore this corollary closes
the one-pair degree gate exactly, but a scalable construction still needs
a network which disperses those deterministic pair-frame correlations.

### Corollary 3.4 (two reflection layers connect the frame state space)

For the carousel reflections `S_j=S K^j`, an even `j` has frame-transition
edges

\[
                         0-1,\qquad2-3,                       \tag{3.9}
\]

while an odd `j` has

\[
                         1-2,\qquad3-0.                       \tag{3.10}
\]

Hence two consecutive carousel layers have connected frame-transition
graph `C_4` on `{M_0,M_1,M_2,M_3}`.

#### Proof

In zero-based labels a reflection has the form `f_a(c)=a-c`.  For the even
reflection class, the phase evolution is `(c-t,c'+t)`, and the two adjacent
matching labels differ by one with sectors `{0,1}` and `{2,3}`, as in
Proposition 3.2.  For the odd reflection class the evolution reverses to
`(c+t,c'-t)`.  Substitution into the analogue of (3.8) shifts one of the
two labels, giving sectors `{1,2}` and `{3,0}`.  The union of (3.9)--(3.10)
is the four-cycle. \(\square\)

This is a finite frame-state butterfly, not yet an owner-level composition
theorem.  Corollary 2.2 supplies compatible predecessor/successor frame
interfaces; the remaining step is to realize consecutive layers on one
exact owner partition without reintroducing trace collisions.

This is the bounded frame change absent from a fixed-pair compiler: the
same actual cycle alternates between two transverse ambient pairings, and
the predecessor convention agrees exactly with the forward convention.

## 4. Sharp boundary for bounded isometric primitives

The preceding two-frame behaviour is maximal for one isometric cycle.

### Proposition 4.1 (two-frame ceiling)

Let `C` be any graph-isometric `C_(2h)` in `Q_h`.  Then its direction word
is `pi pi` for one permutation `pi` of the `h` directions.  Consequently
all decompositions of aligned consecutive windows into adjacent direction
pairs use exactly the two matchings `M_0(pi),M_1(pi)` determined by start
parity.  No third phase-dependent ambient matching can occur in one such
cycle.

#### Proof

Every `h` consecutive edges join antipodal vertices, so their directions
are all distinct.  Sliding the length-`h` window by one shows that the
entering direction equals the leaving direction.  Thus `w_(t+h)=w_t` and
the word is `pi pi`.  Adjacent pairs are then determined solely by the
parity of their first index, giving exactly (3.2). \(\square\)

Therefore a network requiring three or more ambient frames must compose
several owner-compatible primitives or leave the class of isometric
`C_(2h)` components.  A single bounded cell can provide a genuine
two-frame alternation, but not a complete moving-frame atlas.

## 5. Phase-quotient overlap is already connected

There is a finite integral-coupling warning.  Compare a carousel factor
from the even reflection class with one from the odd reflection class.
Write

\[
                         s=c+c'\pmod4,
 \qquad                  e=|u|+|v|\pmod2.                    \tag{5.1}
\]

For an even-reflection factor the cycle invariant is

\[
                         \kappa_+=s-e\pmod4,                  \tag{5.2}
\]

while for an odd-reflection factor it is

\[
                         \kappa_-=s+e\pmod4.                  \tag{5.3}
\]

Both invariants take values in `{0,2}`.

### Proposition 5.1 (connected sector overlay)

In the common-owner overlap of the two factors, the quotient graph on their
phase-sector cycle classes is `K_(2,2)`.  Even owners give the two edges

\[
                         0_L-0_R,\qquad2_L-2_R,
\]

and odd owners give

\[
                         0_L-2_R,\qquad2_L-0_R.                \tag{5.4}
\]

#### Proof

At an even owner `e=0`, (5.2)--(5.3) agree.  At an odd owner `e=1`, they
differ by two modulo four.  Every phase-pair type occurs, so all four edges
in (5.4) occur. \(\square\)

Thus phase-sum sectors do not provide independent component switches
between the two butterfly layers.  The full owner overlay may refine this
quotient through kernel translations, but no refinement can be justified
merely by the frame label.  A scalable integral construction still needs
an owner-level decomposition theorem beyond the uniform degree and
connected frame-transition results above.
