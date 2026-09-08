# PBBS tight-return transversals: the all-zero-slot lift already fails at height three

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Put

\[
 N=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil .
\]

The harmonic Pascal-fan envelope has the formally critical order
\(1/H\).  A tempting counterdirection is therefore to start at a mountain,
put zero in every forced inverse slot, and recursively lift the tight
return fan.  This note proves that this is not a valid construction: the
obstruction occurs already in the first nontrivial orientation step.

There is an exact \(\tau\)-cycle of semilength-three cores

\[
 F_0=110100,qquad F_1=110010,qquad F_2=101100,
 \qquad \tau F_i=F_{i+1\pmod3},                 \tag{0.1}
\]

for which the tight gap-five start set is

\[
                         J_2=\{F_0,F_2\}.       \tag{0.2}
\]

Only the oriented adjacent pair

\[
                         F_2\longmapsto F_0      \tag{0.3}
\]

extends to a tight gap-seven parent.  The other tight child start \(F_0\)
has a terminal-zero parent

\[
                         D_0=1110011000,
 \qquad \partial D_0=F_0,\qquad d(D_0)=1,       \tag{0.4}
\]

but \(D_0\) has no return at gap seven.  In contrast,

\[
                         D_2=1100111000,
 \qquad \partial D_2=F_2,                       \tag{0.5}
\]

is the corresponding tight gap-seven parent.

Thus the conditions

\[
 \boxed{
 \text{tight child return}+\text{terminal free slot }0}
                                                               \tag{0.6}
\]

are not sufficient for the next tight return.  One must orient the child
phase so that the whole ordered adjacent child fan closes.  In particular,
the zero-value Pascal capacity product is only an upper envelope; it is not
an attained recursive lower family.

More generally, if a height-\(h\) tight return is peak-deleted \(j\)
times, its exact triangular fan contains the \(j+1\) tight child starts at
the consecutive quotient phases \(0,1,\ldots,j\).  Consequently every
bottom-up construction to height \(h\) requires a compatible growing run
of ordered adjacent-deletion orientations at every inverse level.  Fixed
depth marginals do not compose: at Gaussian height this is an
\(H\)-memory intersection condition, not a product of one-slot
occupancies.

This is a rigorous obstruction, not a decision of \(ST_A\).  No
asymptotic lower bound

\[
 \overline\nu_H=\Omega_A(B_m/\sqrt m)
\]

is proved here.  The largest audited explicit long-cycle lower families
remain below that scale.  Conversely, the example below prevents using
the harmonic \(\Theta(1/H)\) capacity as such a lower bound without a new
simultaneous orientation theorem.

## 1. Exact block-rotation data

For a Dyck word written in its canonical first-maximum factorization

\[
                         D=P1R0S,
\]

recall

\[
 \delta(D)=|P|+1,\qquad d(D)=|S|+1,
 \qquad \tau D=S1P0R.                            \tag{1.1}
\]

For \(F_0=110100\), the first maximum is reached at its second bit and
the first subsequent return to zero is the last bit.  Hence

\[
 F_0=(1)1(010)0,qquad
 (\delta(F_0),d(F_0))=(2,1),qquad
 \tau F_0=110010=F_1.                            \tag{1.2}
\]

For \(F_1=110010\), the first subsequent return after the marked second
bit occurs at the fourth bit, leaving the suffix \(10\).  Thus

\[
 F_1=(1)1(0)0(10),\qquad
 (\delta(F_1),d(F_1))=(2,3),qquad
 \tau F_1=101100=F_2.                            \tag{1.3}
\]

Finally, \(F_2\) first reaches height two at its fourth bit and returns
to zero at its last bit.  Therefore

\[
 F_2=(101)1(0)0,qquad
 (\delta(F_2),d(F_2))=(4,1),qquad
 \tau F_2=F_0.                                   \tag{1.4}
\]

This proves the cycle (0.1), including every voltage and deficit needed
below.

## 2. The exact tight-start orientation on the core cycle

A height-two root \(F\) starts a zero-winding tight return precisely when

\[
                         d(F)+d(\tau F)=\delta(\tau^2F).       \tag{2.1}
\]

The strict first-passage theorem then makes this the first consecutive
return of physical gap five.

Using (1.2)--(1.4), at the three phases the two sides of (2.1) are

\[
\begin{array}{c|ccc}
F&F_0&F_1&F_2\\ \hline
d(F)+d(\tau F)&4&4&2\\
\delta(\tau^2F)&4&2&2.
\end{array}                                      \tag{2.2}
\]

Hence exactly \(F_0\) and \(F_2\) are tight starts, proving (0.2).
In the cyclic order (0.1), there is exactly one ordered adjacent pair of
tight starts, namely \((F_2,F_0)\).  The pair \((F_0,F_1)\) fails because
\(F_1\) is not tight.

This distinction is the first adjacent-deletion orientation datum.  The
one-point statement that the phase \(F_0\) is tight forgets whether its
successor supplies the second child required by a tight parent fan.

## 3. A terminal-zero parent over the wrong orientation fails

Consider

\[
                         D_0=1110011000.          \tag{3.1}
\]

Its adjacent peaks are the third--fourth and seventh--eighth bits.
Simultaneous deletion of those two peaks gives

\[
                         \partial D_0=110100=F_0.                \tag{3.2}
\]

The word is primitive, so its terminal root suffix is empty and

\[
                         d(D_0)=1.                \tag{3.3}
\]

Equivalently, the terminal free inverse slot over \(F_0\) has occupancy
zero.

This is not a bad choice from a larger inverse fibre.  Both \(F_0\) and
\(F_2\) have semilength \(d=3\) and exactly \(k=2\) peaks.  At parent
semilength \(m=5\), the inverse peak-insertion excess is therefore

\[
                         y=m-d-k=0,
\]

and the exact weak-composition fibre has size

\[
                         \binom{m+d-k}{2d}
                         =\binom 66=1.             \tag{3.3a}
\]

Thus the displayed terminal-zero lift is the unique lift at this first
nontrivial inverse level.  No alternative slot assignment or integral
rounding can repair the wrong child orientation here.

The exact block rotations are

\[
\begin{aligned}
 D_0&=1110011000,\qquad &(\delta,d)&=(3,1),\\
 D_1:=\tau D_0&=1110001100, &(\delta,d)&=(3,5),\\
 D_2:=\tau^2D_0&=1100111000, &(\delta,d)&=(7,1),\\
 \tau^3D_0&=D_0.&&
\end{aligned}                                    \tag{3.4}
\]

For a zero-winding step-two return at time \(s\), the exact integer
equation is

\[
                         \sum_{i=0}^{s-1}d(\tau^iD_0)
                         =\delta(\tau^sD_0).       \tag{3.5}
\]

At \(s=1,2,3\), respectively, (3.4) gives

\[
                         1\ne3,\qquad
                         1+5=6\ne7,\qquad
                         1+5+1=7\ne3.             \tag{3.6}
\]

The ambient circumference is eleven, and every displayed number is
strictly between zero and eleven.  Hence none of these failed integer
equalities can be repaired by a nonzero winding congruence.  In
particular \(D_0\) does not return at gap seven.

This proves (0.4) and the failure of (0.6) directly, without invoking a
counting relaxation.

## 4. The correctly oriented parent

The phase \(D_2\) in (3.4) satisfies

\[
                         \partial D_2=101100=F_2.                \tag{4.1}
\]

Starting at \(D_2\), the three deficits in cyclic order are

\[
                         1,1,5,
\]

and the endpoint is again \(D_2\), whose first-maximum position is seven.
Thus

\[
                         1+1+5=7=\delta(\tau^3D_2).             \tag{4.2}
\]

The strict first-passage variable is positive at the two proper prefixes,
and the height-gap theorem excludes an earlier return.  Therefore \(D_2\)
starts the tight gap-seven return.  This is also the \(d=3\) instance of
the audited complete gap-seven classification

\[
                         \partial D=(10)^{d-2}1100.              \tag{4.3}
\]

Equations (3.2) and (4.1) show exactly what the slot-only recursion
misses: \(F_0\) and \(F_2\) are both tight gap-five roots on the same
core cycle and both displayed parents have terminal value zero, but only
the phase whose successor is the other tight child closes at the next
level.

## 5. Growing-run necessity under repeated peak deletion

Let a height-\(h\) root \(D\) start a tight return, and put

\[
                         D^{(j)}=\partial^jD.
\]

The audited tight-return tower theorem gives, for every level before the
first mountain and every \(0\le a\le j\), the child interval

\[
 I_{j,a}=[2a,\,2h+1-2(j-a)]                      \tag{5.1}
\]

in the one-step chronology of \(D^{(j)}\).  Its quotient start phases are

\[
                         0,1,\ldots,j.            \tag{5.2}
\]

and its labels are consecutive in persistent particle order.  Therefore
every height-\(h\) top start projects at inverse depth \(j\) to an
ordered run of \(j+1\) correctly oriented tight child starts.  In set
notation, if \(J_j\) denotes the relevant tight-child phase set on a
fixed reduced cycle, the possible top anchors lie in

\[
                         \bigcap_{a=0}^{j}\tau^{-a}J_j.         \tag{5.3}
\]

Equation (5.3) is only a necessary condition; the transported numerical
slot values and upper closure equations can shrink it further.  It is
nevertheless enough to disprove marginal composition.  Knowledge of
\(|J_j|\), even together with the zero-value weak-composition capacity,
does not lower-bound (5.3).  The explicit cycle (0.1) is the first case:

\[
 |J_2|=2,\qquad
 |J_2\cap\tau^{-1}J_2|=1.                        \tag{5.4}
\]

At Gaussian depth \(j=\Theta(H)\), (5.3) is an \(H\)-fold chronological
intersection.  This is exactly why a fixed-depth adjacent-deletion
orientation or a product of zero-slot marginals cannot be extrapolated to
\(H=A\sqrt m\).

## 6. Packing and deck constants

Let \(\mathcal P\) be any quotient-edge-disjoint family of nonwrapping
returns on quotient cycles longer than \(H+1\).  Every quotient interval
has exactly \(N\) spatial deck lifts, and the lifts of distinct selected
quotient intervals are disjoint.  Hence

\[
                         \nu_H(P_m)\ge N|\mathcal P|.           \tag{6.1}
\]

In particular, a future simultaneous-orientation theorem producing

\[
                         |\mathcal P|\ge c_A{B_m\over H}        \tag{6.2}
\]

would give

\[
 \nu_H(P_m)
 \ge c_A{N B_m\over H}
 =\left({2c_A\over A}+o_A(1)\right)B_m\sqrt m,   \tag{6.3}
\]

and would refute \(ST_A\).  No factor two is lost in this lower deck
direction.  The short quotient cycles cannot supply (6.2): their entire
root count is at most

\[
 (2H+2)N^{2H+2}=\exp(O_A(\sqrt m\log m))
 =o(B_m/m^K)                                      \tag{6.4}
\]

for every fixed \(K\).

The finite three-cycle used in Sections 1--4 is therefore an orientation
obstruction only.  It is not counted toward the asymptotic long-cycle
packing.

## 7. Exact proved boundary

Proved here:

1. the complete height-two core cycle and its tight-start set;
2. a terminal-zero inverse parent over a tight but wrongly oriented phase
   which fails the next tight return;
3. the correctly oriented tight parent on the same outer cycle;
4. the exact necessity of growing consecutive child-start runs under the
   tight-return tower; and
5. the exact \(N\)-fold lower deck conversion.

Not proved:

1. a lower bound for the intersections in (5.3) on Catalan-weighted
   long-period cores;
2. an attained harmonic zero-slot capacity;
3. \(\overline\nu_H=\Omega_A(B_m/\sqrt m)\);
4. \(ST_A\) or its negation.

Thus the matching-critical lower route is blocked at a precise theorem:
one must prove an integral, history-preserving adjacent-deletion
orientation which leaves \(\Omega(B_m/H)\) anchors in the growing
intersections (5.3), with bounded conflict degree.  One-point tight-return
counts and zero-slot capacities do not imply such a theorem, already at
height three.
