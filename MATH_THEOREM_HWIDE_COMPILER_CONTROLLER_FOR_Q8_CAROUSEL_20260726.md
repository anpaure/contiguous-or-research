# An \(H\)-wide compiler controller removes the quadratic \(Q_8\) turnaround loss

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

The quadratic turnaround obstruction for a bounded \(Q_8\) seam is sharp
but not terminal.  It can be bypassed at the packet-carrier level by
placing a proved literal trace compiler, of width \(\Theta(H)\), across
the two antipodal turnarounds.

The construction uses three exact ingredients.

1. The phasewise \(Q_8\) splice is an exact isometric \(C_{16}\)-factor.
2. The recursive local compiler gives exact cyclic factors whose literal
   forward and backward traces are injective through length \(H\) in the
   coordinate-disjoint Johnson interface.
3. A doubled-permutation word remains isometric after the eight \(Q_8\)
   seam directions are inserted once in each half.

Let the compiler first-half word be \(\kappa\), and split it cyclically as

\[
                         \kappa=BA,\qquad |A|,|B|\ge H. \tag{0.1}
\]

Let

\[
 \Sigma=w_0,\rho_0,w_1,\rho_1,\ldots,w_7,\rho_7,
\qquad |\rho_t|=L,                                  \tag{0.2}
\]

be the long payload core.  The macro first-half word is

\[
                         \Pi=B\,\Sigma\,A,           \tag{0.3}
\]

and the complete cycle word is \(\Pi\Pi\).

At both global turnarounds, the local word is \(AB\), a cyclic interval
of the compiler word \(\kappa\kappa\), with at least \(H\) controller
directions on each side.  Therefore every protected turnaround window is
decoded literally by the compiler.  The remaining \(Q_8\) seams occur
inside one half of the doubled word: their two payload collars have the
same orientation.  A direct collar ledger gives only \(O(1)\) possible
literal collisions per seam and depth.

For a complete family of \(M\) tagged macrocycles, with owner mass

\[
                         G=2DM,\qquad
 D=|\Pi|=r+8+8L,                                    \tag{0.4}
\]

where \(r=|\kappa|\), the exact additional seam-collision ledger is

\[
 \boxed{
 \sum_{q=1}^{H}\bigl(E_q^-+E_q^+\bigr)
 \le 64HM
 ={32H\over D}\,G.}                                 \tag{0.5}
\]

Here \(E_q^\pm\) counts collisions created by the controller and carousel
interfaces; inherited payload collisions are excluded and must be zero
or separately charged by the payload theorem.

Choose the compiler with \(r=O(H)\), take \(L\) even, reserve four
additional split-pair slots for the frozen base-cycle tags, and choose
\(L\) so that \(D=\Theta(m)\) and \(D+4\le m\).  Whenever

\[
                         \sqrt m\ll H=o(m),          \tag{0.6}
\]

equation (0.5) is \(o(G)\).  Thus an owner-disjoint packing of these
carriers on \(G=W-o(W)\) owners would have \(o(W)\) aggregate seam
collision even though \(H/\sqrt m\to\infty\).

This is an exact local-controller theorem, not the constant-one theorem.
The unresolved global statements are carrier packing and cross-macrocycle
target coverage.

## 1. The compiler input at the required scale

Use the theorem in
\[
\texttt{MATH\_ATTACK\_S\_PARITY\_COMPLETE\_MAPPING\_TRACE\_ENTROPY\_CUT\_20260726.md}.
\]

For

\[
                         n=4\cdot2^t
\]

it gives exact factors on \(Q_{2n}\) into isometric \(C_{4n}\)'s.  In the
coordinate-disjoint Johnson realization, every literal lower and upper
trace is injective, in both orientations, through physical length

\[
                         {n\over2}-1.                \tag{1.1}
\]

Given \(H\), take the least such \(n\) with

\[
                         n\ge2(H+1).                 \tag{1.2}
\]

Then

\[
                         2(H+1)\le n<4(H+1).         \tag{1.3}
\]

Put

\[
                         r=2n.                      \tag{1.4}
\]

One controller cycle has word \(\kappa\kappa\), where \(\kappa\) is a
permutation of its \(r\) physical directions.  Split \(\kappa=BA\) with

\[
                         |A|=|B|=n.                 \tag{1.5}
\]

Equations (1.2) and (1.5) give much more than the required \(H\)-buffer
on both sides.

The phrase literal injectivity in this note always uses the
support-revealing coordinate-disjoint Johnson interface.  A controller
trace of \(d\) moves has lower and upper controller ranks differing from
the middle controller rank by \(d\); hence its literal target determines
\(d\) as well as the unique start.  This depth recognition is needed at
mixed controller-payload boundaries.

## 2. Exact macrocycle and owner support

Let

\[
                         C=(x_0,\ldots,x_{15})
\]

be one cycle of the exact phasewise \(Q_8\) splice, with direction word

\[
                         w_0\cdots w_7w_0\cdots w_7. \tag{2.1}
\]

Let \(Y\) be one controller cycle with word \(\kappa\kappa\).  Adjoin
eight disjoint payload blocks \(D_t\), each of size \(L\), and choose one
ordered payload path

\[
                         \rho_t=(d_{t,1},\ldots,d_{t,L})
\]

on each block.

Use the first-half word \(\Pi\) from (0.3), and repeat it.  Start at the
chosen base and controller owners with all payload bits zero.

### Theorem 2.1 (exact \(H\)-wide macrocycle)

The word \(\Pi\Pi\) defines an isometric \(C_{2D}\), where

\[
                         D=r+8+8L.
\]

If distinct macros use disjoint \(Q_8\) cycles or disjoint controller
cycles, their owner supports are disjoint.  Consequently any family of
such macros is an exact cyclic factor of its declared union.

#### Proof

The word \(\Pi\) contains every controller direction once, every \(Q_8\)
direction once, and every payload direction once.  Thus it is a
permutation of all \(D\) active directions.  The doubled-permutation
criterion proves that \(\Pi\Pi\) is a simple isometric \(C_{2D}\).

Every macro owner projects to its selected \(Q_8\) cycle and its selected
controller cycle.  If either projected cycle differs, two macro supports
cannot meet.  The cycles themselves partition their union exactly.
\(\square\)

This is complete cyclic packet factorhood: every declared owner belongs
to one whole macrocycle, and no shore or depth is chosen fractionally.
It is not a claim that the declared union is the full Cartesian product
of the two child factors.

Under the standard split-pair realization, every active cube coordinate
records the orientation of one physical pair.  Toggling it is one Johnson
exchange and preserves the middle rank.  The controller, payload, and
four frozen tag-pair blocks are coordinate-disjoint, so the displayed
macrocycles are literal middle-owner cycles after adjoining one fixed
exterior set to reach the ambient rank.

## 3. Frame compatibility

Inside \(\Sigma\), the seam edge \(w_t\) uses carousel shore
\(t\bmod4\).  The source identity

\[
                         \Xi_t^-=\Xi_{t+1}^+         \tag{3.1}
\]

places \(\rho_t\) in one fixed legal frame between consecutive seam
edges.  Here \(L\) is chosen even, so \(w_t\) occurs at position
\(t(L+1)\), whose parity is \(t\); this is the parity convention used by
the phase-indexed frame ledger.  (For odd \(L\), an additional phase
reset would be required.)  The eight seam edges make two complete turns
of the four-stage carousel, so \(\Sigma\) begins and ends in the same
frame.

The controller block may therefore use that common entrance/exit frame.
No frame mismatch occurs at either \(B|\Sigma\) or \(\Sigma|A\).  The
second copy of \(\Pi\) has the identical frame ledger.

## 4. The two turnarounds are controller-internal

There are two places at which the payload orientations reverse:

1. the boundary between the first and second copies of \(\Pi\); and
2. the cyclic boundary between the second copy and the first.

At either boundary, the controller projection is

\[
                         A\,B.                       \tag{4.1}
\]

This is a cyclic interval of \(\kappa\kappa=BABA\).

### Lemma 4.1 (turnaround decoding)

Every forward or backward window of at most \(H\) moves which meets a
global turnaround is contained wholly in the controller word \(AB\) and
is decoded literally.

#### Proof

There are \(|A|\ge H\) controller moves immediately before the boundary
and \(|B|\ge H\) immediately after it.  Hence an \(H\)-window meeting the
boundary cannot reach \(\Sigma\).  Its controller projection is an
ordinary consecutive window of the certified cycle \(Y\).  Literal
forward and backward injectivity from Section 1 recovers its start.
\(\square\)

Thus the two fibres of size \(q\) in the bounded-carousel obstruction
have disappeared: their targets are replaced by distinct certified
controller targets.

## 5. Mixed controller-core boundaries

Consider a protected window meeting \(B|\Sigma\) or \(\Sigma|A\), but not
a global turnaround.  It contains \(d\ge1\) consecutive controller moves
and \(q-d\) core moves.

### Lemma 5.1 (mixed-boundary decoder)

Under the support-revealing controller interface, every such signed
window is decoded uniquely.

#### Proof

Restrict its literal target to the controller coordinates.  This is the
literal trace of exactly \(d\) consecutive controller moves.  Its
controller rank determines \(d\), and the compiler theorem recovers the
unique controller start, orientation, and cycle.  The macro construction
then fixes the adjacent \(Q_8\) cycle, the boundary, and the number
\(q-d\) of core moves.  Hence it fixes the macro start.

A target from a window with no controller move has controller rank zero
relative to its frozen controller owner, while the present target has
positive controller depth.  Thus the same restriction also separates
mixed windows from core-only windows. \(\square\)

This is where raw augmented injectivity would be insufficient.  The
literal controller rank, supplied by the coordinate-disjoint Johnson
interface, is essential.

## 6. Homogeneous \(Q_8\) seam ledger

Every \(Q_8\) seam inside the first copy of \(\Sigma\) lies between two
increasing payload runs.  Its antipodal copy lies between the
corresponding two decreasing runs.  The opposite-orientation turnaround
of the obstruction note no longer occurs at a \(Q_8\) seam.

Use four frozen split tag pairs to assign the sixteen \(Q_8\) base cycles
distinct four-bit orientation labels.  These pairs are never moved, so
every lower and upper target retains the label.  Hence targets belonging
to different base cycles cannot collide.  The tag pairs add only
\(O(1)\) frozen coordinates and preserve middle rank.

### Lemma 6.1 (one homogeneous seam)

Fix one tagged macrocycle, one homogeneous seam, one sign, and one depth
\(q\le H\le L\).  Among the windows meeting that seam, the literal target
determines the split of the \(q-1\) payload moves across its two sides.
The only possible collision with a window not meeting the seam is one
adjacent boundary window.  Thus this seam contributes collision excess at
most two for either sign.

#### Proof

First suppose both payload runs increase from zero to one.  If \(a\)
moves lie before the seam and \(b=q-1-a\) after it, then on the left
payload block the lower target is

\[
                         1^{L-a}0^a,                 \tag{6.1}
\]

which determines \(a\).  On the right block the upper target is

\[
                         1^b0^{L-b},                 \tag{6.2}
\]

which determines \(b\).  Since \(q\) is fixed, either signed target
determines the other parameter as well.

Two different seam-crossing starts therefore cannot collide.  A
nonseam window has a different frontier on at least one of the two
blocks, except possibly when \(a=0\) or \(b=0\).  These are the two
adjacent boundary cases, giving the stated bound.

The restrictions on all earlier and later payload blocks form,
respectively, the global all-one and all-zero parts of the payload chain.
They identify the seam index \(t\).  In the second copy the roles are
complemented, so they also identify which antipodal occurrence is being
used.  Finally the frozen split tag identifies the \(Q_8\) base cycle.
Thus no additional collision with another seam or another tagged
macrocycle is hidden in the local calculation.

For two decreasing runs, complement (6.1)--(6.2): the upper target on
the left and the lower target on the right determine the same parameters.
\(\square\)

There are sixteen occurrences of \(Q_8\) seam edges on a full
macrocycle.  Lemmas 4.1 and 5.1 leave no controller-interface collision.
Lemma 6.1 therefore gives the safe uniform bound

\[
                         E_q^-+E_q^+\le64             \tag{6.3}
\]

for the new seam collisions of one macrocycle at one depth.  The
constant is intentionally not optimized.

Windows wholly inside a payload segment retain the supplied payload
trace map.  Their inherited collisions are not included in \(E_q^\pm\).

## 7. Exact aggregate occurrence ledger

Let \(M\) complete macrocycles be selected owner-disjointly.  Their owner
mass is

\[
                         G=2DM.                      \tag{7.1}
\]

Summing (6.3) over all depths gives

\[
\begin{aligned}
 \sum_{q=1}^{H}(E_q^-+E_q^+)
 &\le64HM\\
 &= {32H\over D}\,G.                                \tag{7.2}
\end{aligned}
\]

This is an occurrence calculation.  It does not infer target holes from
the number of geometric seams, and it does not count a maximum-depth
window once on behalf of all smaller depths.

Now assume \(H=o(m)\), retain (1.2), and choose the even payload length

\[
                         L=
 2\left\lfloor{m-r-12\over16}\right\rfloor.          \tag{7.3}
\]

Then \(L\sim m/8\), \(H\le L\), the four frozen tag pairs fit, and

\[
                         m-19\le D\le m-4.           \tag{7.4}
\]

Therefore

\[
 {32H\over D}\,G=O\!\left({H\over m}\right)G=o(G).   \tag{7.5}
\]

The condition \(H/\sqrt m\to\infty\) is compatible with this calculation;
for example any

\[
                         \sqrt m\ll H\ll m
\]

works.

If an outer packing theorem supplies \(G=W-o(W)\), the aggregate seam
collision in (7.2) is \(o(W)\).

## 8. Scope and exact remaining gate

This theorem proves:

1. an \(H\)-wide owner-valid controller made from complete compiler
   cycles;
2. complete isometric macrocycles rather than open paths;
3. literal decoding at both antipodal turnarounds and all mixed
   controller boundaries; and
4. an exact \(O(H)\)-per-macrocycle, hence
   \(O(HG/m)=o(G)\), seam occurrence ledger.

It does not prove:

1. that the macro carriers pack \(W-o(W)\) middle owners;
2. that targets from different macrocycles have only the seam collisions
   counted in (7.2);
3. that the payload frame choices cover all but \(o(W)\) central targets;
   or
4. a raw-Boolean seam decoder without support recovery.

The raw-Boolean no-go in
\[
\texttt{MATH\_OBSTRUCTION\_Q8\_CAROUSEL\_LITERAL\_TURNAROUND\_SEAM\_20260726.md}
\]
remains exact.  The present positive theorem uses precisely its first
escape boundary: an \(H\)-scale controller in a literal
support-revealing Johnson interface.

The remaining coefficient-one theorem is now an outer packing and
cross-macrocycle target problem, not a local turnaround problem.
