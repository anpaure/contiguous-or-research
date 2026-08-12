# PBBS primitive-return recursion: exact audit and inverse-fibre formula

Date: 2026-07-25

This note uses only the proved equality-particle dynamics.  It does **not**
use the retracted assertion that a primitive Dyck root of height (h)
returns at gap (2h+1).

## 1. Setup

For a normalized Dyck root (X), let (G(X)) denote the first positive
return time of its omitted physical coordinate.  Let \(\partial X\) be
simultaneous peak deletion and let \(\tau=\phi^2\) be the two-step Dyck
quotient map.

Let (D) be a nontrivial primitive Dyck word of semilength (r), and put

\[
 F=\partial D,
 \qquad |F|_{\rm semi}=d,
 \qquad k=\operatorname{pk}(F).
\]

Pruning a nontrivial unary-root plane tree leaves a unary-root tree, so
(F) is primitive.  In the inverse peak-deletion description of
(F\mapsto D), both root corners contain no newly inserted leaf.  In
particular the terminal corner has occupancy (t=0).

## 2. Exact recursion

### Theorem 2.1

If

\[
 2+G(\tau F)<2r+1,
\]

then

\[
 \boxed{G(D)=2+G(\tau\partial D).}
 \tag{2.1}
\]

Consequently, for every (H<r+1),

\[
 \boxed{
 G(D)\le 2H-1
 \iff
 G(\tau\partial D)\le 2H-3.
 }
 \tag{2.2}
\]

### Proof

Use the equality-particle PBBS of the proved renormalization theorem.
Label the distinguished particle by (a) and its immediate predecessor by
(b=a-1).  Let

\[
 0<B_1(F)<B_2(F)<\cdots
\]

be the positive selection times of (b) in the reduced PBBS starting from
(F).

Because (D) is primitive, the root of its plane tree has one child.
Thus the predecessor and distinguished equality particles are physically
adjacent: the terminal inverse occupancy is (t=0), so their spacing is
(2t+1=1).  The exact terminal-spacing kernel therefore says that the
first outer repeated physical coordinate occurs at the second selection of
(b):

\[
 G(D)=B_2(F),
 \tag{2.3}
\]

provided this event occurs before one full outer wrap.

A primitive Dyck root has two-step spatial deficit one.  Hence, after two
reduced PBBS updates from (F), the selected particle is (b), and the
normalized reduced root is \(\tau F\).  Therefore

\[
 B_1(F)=2.
 \tag{2.4}
\]

Starting at time two, the next selection of this same persistent particle
(b) is exactly the next omitted-coordinate return in the reduced PBBS
rooted at \(\tau F\).  Spatial translation does not change a return gap, so

\[
 B_2(F)-B_1(F)=G(\tau F).
 \tag{2.5}
\]

Equations (2.3)--(2.5) prove (2.1).  If either side of (2.2) holds, the
displayed time is at most (2H-1<2r+1), so the no-wrap hypothesis is
automatic; (2.2) follows.  \(\square\)

The phase condition is essential only for (2.3): before the outer
circumference, no particle can make a full circuit and the immediate
predecessor is the unique possible second entrant.  Equation (2.5) is a
statement about the persistent particle identity and is invariant under the
spatial phase shift at time two.

## 3. Exact primitive inverse fibre

### Proposition 3.1

For fixed primitive (F\in\mathcal D_d) with (k) peaks, the number of
primitive semilength-(r) roots (D) satisfying \(\partial D=F\) is

\[
 \boxed{
 K^{\rm prim}_r(F)
 =\binom{r+d-k-2}{2d-2}.
 }
 \tag{3.1}
\]

Equivalently,

\[
 \boxed{
 \sum_{r\ge0}K^{\rm prim}_r(F)x^r
 ={x^{d+k}\over(1-x)^{2d-1}}.
 }
 \tag{3.2}
\]

### Proof

The inverse leaf-insertion construction for a (d)-edge core has (2d+1)
ordered child slots.  One new leaf is compulsory at each of the (k) old
leaves.  Since (F) is primitive, its root has one core child.  The lift is
primitive exactly when no new leaf is inserted in either root corner,
before or after that child.  Hence the remaining free mass

\[
 y=r-d-k
\]

is distributed among (2d-1) slots.  Stars and bars gives

\[
 \binom{y+2d-2}{2d-2}
 =\binom{r+d-k-2}{2d-2}.
\]

Summing over (y\ge0) gives (3.2).  \(\square\)

## 4. Exact primitive short-return enumeration

Let

\[
 \mathcal P_d=\{F\in\mathcal D_d:F\text{ is primitive}\}.
\]

For (2H-1<2r+1), Theorem 2.1 and Proposition 3.1 give the exact identity

\[
 \boxed{
 R^{\rm prim}_r(H)
 =\sum_{d=1}^{r-1}
   \sum_{F\in\mathcal P_d}
   \mathbf1_{\{G(\tau F)\le2H-3\}}
   \binom{r+d-\operatorname{pk}(F)-2}{2d-2},
 }
 \tag{4.1}
\]

apart from the rank-one root, which is handled separately.  Here
(R^{\rm prim}_r(H)) counts primitive semilength-(r) roots whose first
return gap is at most (2H-1).

This is a genuine reduction, but not yet a contraction.  The indicator is
evaluated at the dynamically rerooted child \(\tau F\), and the Pascal
weight in (4.1) can retain a constant fraction of a central inverse fibre.
Replacing the indicator by bounded height, primitivity, or an inherited
terminal-slot condition loses the required (1/r) scale.

Equivalently, introduce the peak-refined child series

\[
 A_H(u,v)=
 \sum_{d\ge1}\ \sum_{F\in\mathcal P_d}
 \mathbf1_{\{G(\tau F)\le2H-3\}}
 u^d v^{\operatorname{pk}(F)}.
 \tag{4.2}
\]

Then the whole primitive outer class has the exact ordinary generating
function

\[
 \boxed{
 \sum_{r\ge0}R^{\rm prim}_r(H)x^r
 =(1-x)A_H\!\left({x\over(1-x)^2},x\right).
 }
 \tag{4.3}
\]

Thus no multiplicity or inverse-fibre information is lost: the sole
unknown in the primitive lane is the peak-refined short-return mass of the
dynamically rerooted set \(\tau\mathcal P_d\).

Thus the coefficient-one residence route now asks for a weighted packing
or counting estimate for precisely the right side of (4.1), together with
its nonprimitive analogue.  The false height formula is neither needed nor
available.

## 5. Immediate sanity check

For

\[
 D=1110011000,
 \qquad F=\partial D=110100,
 \qquad \tau F=110010,
\]

the cutoff equivalence (2.2) does not predict the false gap seven: a return
by time seven would require the nonprimitive child (110010) to return by
time five, which it does not.  In fact the candidate value
\(2+G(110010)\) lies beyond the outer circumference in this example, so
the unconditional equality (2.1) is deliberately not invoked.  The need
to inspect the dynamically recanonicalized child is exactly what the
retracted sector-shift proof missed.

## 6. Exact iteration of \(T=\tau\partial\) and the first-loss boundary

The one-step formula can be iterated, but only while the dynamically
rerooted pruned word remains primitive. This condition has a literal word
description.

Let \(X\) be a nontrivial primitive Dyck word and write \(X=1U0\).
Decompose \(U\) into primitive components. Let \(Q\) be the first
component attaining the largest component height, and write

\[
 U=AQC,\qquad Q=L1R0,                              \tag{6.1}
\]

where the displayed one is the first step of \(Q\) attaining that height.

### Proposition 6.1 (primitive phase image)

With this notation,

\[
 \boxed{\tau X=VC,\qquad V=11AL0R0,}              \tag{6.2}
\]

where \(V\) is primitive and

\[
 \operatorname{ht}(V)>\operatorname{ht}(C).       \tag{6.3}
\]

Consequently

\[
 \boxed{
 \tau X\text{ is primitive}
 \iff C=\varnothing
 \iff Q\text{ is the terminal primitive component of }U.}
                                                               \tag{6.4}
\]

If \(C\ne\varnothing\), then \(V\) is the unique tallest first
primitive component of \(\tau X\), and

\[
 \boxed{d(\tau X)=|C|+1>1.}                       \tag{6.5}
\]

#### Proof

In the canonical first-maximum factorization of \(X\), the prefix before
the marked step is \(1AL\), the block after it and before the final return
is \(R0C\), and the terminal Dyck suffix is empty. Exact block rotation
therefore gives

\[
 \tau X=1(1AL)0(R0C)=VC.
\]

The word \(V\) has total height zero. Every proper prefix is positive:
this is the strict positivity of the primitive component \(Q\), shifted
upward by the two initial steps, with the Dyck forest \(A\) inserted at a
fixed positive baseline. Hence \(V\) is primitive. Its marked step reaches
height \(1+\operatorname{ht}(Q)\), whereas \(C\), read from height zero,
has height at most \(\operatorname{ht}(Q)\). This proves (6.3). The rest,
including (6.5), follows from the canonical terminal suffix definition
\(d(Y)=|S_Y|+1\). \(\square\)

Peak deletion commutes with the two-step quotient map. Therefore

\[
 \boxed{T^jD=\tau^j\partial^jD}                   \tag{6.6}
\]

whenever both sides are nonempty. At a primitive state \(X_j=T^jD\),
Proposition 6.1 says exactly when \(X_{j+1}\) stays primitive: in the
inner word of \(\partial X_j\), the first maximum-attaining primitive
component must be terminal.

### Corollary 6.2 (iterated primitive recursion)

Put \(X_0=D\) and \(X_{j+1}=TX_j\). Suppose
\(X_0,\ldots,X_{\ell-1}\) are primitive and every displayed candidate
return is below the circumference of its current outer state. Then

\[
 \boxed{G(D)=2\ell+G(X_\ell).}                    \tag{6.7}
\]

In particular, under a bound \(G(D)\le H\), whenever
\(H-2j<2|X_j|_{\rm semi}+1\),

\[
 G(X_j)\le H-2j
 \iff G(X_{j+1})\le H-2j-2.                       \tag{6.8}
\]

#### Proof

Equation (6.6) follows by induction from
\(\partial\tau=\tau\partial\). Apply Theorem 2.1 at each primitive
state and telescope. \(\square\)

The first loss of primitivity is now localized exactly. If \(X_j\) is
primitive but \(X_{j+1}\) is not, Proposition 6.1 makes \(X_{j+1}=VC\)
first-dominant with \(C\ne\varnothing\). The proved zero-winding
necessity theorem says that every zero-winding return root has \(d=1\).
Equation (6.5) gives the following boundary statement.

The one-step persistence and loss classes also have exact ordinary
generating functions. Let \(C_h(z)\) count Dyck words of height at most
\(h\), with \(C_{-1}=0\). A primitive component of exact height \(h\)
has series

\[
 z\bigl(C_{h-1}(z)-C_{h-2}(z)\bigr).
\]

Before the first height-\(h\) component, all components have height at
most \(h-1\). Components after it may have height at most \(h\). Hence

\[
 \boxed{
 P_{\rm keep}(z)
 =z+z^2\sum_{h\ge1}
 C_{h-1}(C_{h-1}-C_{h-2}),}                       \tag{6.8a}
\]

and

\[
 \boxed{
 P_{\rm loss}(z)
 =z^2\sum_{h\ge1}
 C_{h-1}(C_{h-1}-C_{h-2})(C_h-1).}                \tag{6.8b}
\]

Here \(P_{\rm keep}\) counts primitive \(X\) for which \(\tau X\) is
primitive, while \(P_{\rm loss}\) counts primitive \(X\) for which it is
not. The decomposition is exhaustive and gives

\[
 P_{\rm keep}(z)+P_{\rm loss}(z)=zC(z).
                                                               \tag{6.8c}
\]

These formulas count only the phase geometry; they impose no return
condition.

### Corollary 6.3 (positive-winding boundary)

If primitivity is first lost at \(X_{j+1}\), then every
sub-circumference residual return at \(X_{j+1}\) has positive winding:

\[
 \sum_{h=0}^{s-1}d(\tau^hX_{j+1})
 =\delta(\tau^sX_{j+1})+a(2r_{j+1}+1),
 \qquad a\ge1.                                    \tag{6.9}
\]

Thus the primitive recursion has no unidentified zero-winding boundary.
Its sole unclassified branch is the positive-winding return problem for a
word whose first primitive component is uniquely tallest.

## 7. Exact weighted target and absence of a primitive-slot saving

Formula (4.1) is equivalent to the exact series (4.3). For comparison,
the complete inverse fibre over the same core has size

\[
 F_r(F)=\binom{r+d-k}{2d}.
\]

The exact fraction retained by requiring the lift to be primitive is

\[
 \boxed{
 {K^{\rm prim}_r(F)\over F_r(F)}
 ={(2d)(2d-1)\over(r+d-k)(r+d-k-1)}.}              \tag{7.1}
\]

On the two-dimensional inverse-Pascal saddle

\[
 d={r\over2}+O(\sqrt r),\qquad
 k={r\over6}+O(\sqrt r),
\]

the ratio tends to \(9/16\). Hence the two root-corner zero conditions
cost only a constant fraction at the dominant saddle. They cannot supply
the missing factor \(r^{-1/2}\), let alone the quotient factor \(r^{-1}\).

The exact root-count consequence of \((RP_A)\) is

\[
 R_r(\lceil A\sqrt r\rceil)=o_A(B_r/\sqrt r),      \tag{7.2}
\]

because greedy interval packing loses at most \(2H+1=O_A(\sqrt r)\)
starts. Its primitive subproblem is the literal weighted estimate

\[
 \boxed{
 \sum_{d=1}^{r-1}\sum_{F\in\mathcal P_d}
 \mathbf1_{\{G(\tau F)\le2A\sqrt r-3\}}
 \binom{r+d-\operatorname{pk}(F)-2}{2d-2}
 =o_A(B_r/\sqrt r).}                               \tag{7.3}
\]

Equations (6.7)--(6.9) split (7.3) exactly into a
persistent-primitive branch and a positive-winding first-dominant boundary
branch. No argument using only height, inherited empty slots, or the
unweighted number of pruned cores can prove (7.3), because (7.1) shows
that the exact Pascal kernel retains constant mass in the saddle tube. A
proof must bound the positive-winding boundary in (6.9), or show that its
short intervals cluster on quotient cycles strongly enough to beat the
greedy \(O(\sqrt r)\) loss.

## 8. The first-loss sector is Catalan-dense, but its positive winding has an exact charge

The first-dominant boundary in Corollary 6.3 is not a small static class.
For every primitive Dyck word \(Q\) of semilength \(d-2\) and height at
least two, form

\[
 X(Q)=1\,Q\,10\,0.                                 \tag{8.1}
\]

Then \(X(Q)\) is primitive. In its inner word \(Q10\), the first
maximum-attaining component lies in \(Q\) and is not terminal. Hence
\(\tau X(Q)\) is nonprimitive and first-dominant by Proposition 6.1.
The construction is injective and supplies

\[
 \operatorname{Cat}_{d-3}-O(1)=\Theta(\operatorname{Cat}_d) \tag{8.2}
\]

first-loss cores. Thus neither primitivity nor the first-dominant shape
has a vanishing Catalan density.

There is nevertheless an exact dynamical charge for the only returns which
can survive at this boundary. For a return of step-two length \(s\), write

\[
 D_j=\tau^jD,\quad
 a_j=\delta(D_j),\quad
 b_j=\delta(\phi D_j),\quad
 c_j=d(D_j),\quad
 \widehat c_j=d(\phi D_j).
\]

The block identities are

\[
 c_j=N-a_j-b_j,qquad
 \widehat c_j=N-b_j-a_{j+1},
\]

and hence

\[
 a_{j+1}-a_j-c_j=-\widehat c_j.                  \tag{8.3}
\]

If the return has winding \(w\), its terminal equation and the telescope
of (8.3) give the two exact positive ledgers

\[
 \boxed{
 \sum_{j=0}^{s-1}c_j=a_s+wN,qquad
 \sum_{j=0}^{s-1}\widehat c_j=a_0+wN.}            \tag{8.4}
\]

At a first-loss boundary \(w\ge1\), so both sums are at least \(N+1\).
Consequently, if \(\mathcal J\) is any quotient-edge-disjoint family of
such positive-winding intervals, then

\[
 N|\mathcal J|
 \le\sum_{I\in\mathcal J}\sum_{e\in I}c(e)
 \le\sum_{D\in\mathcal D_r}d(D).                 \tag{8.5}
\]

The proved one-deficit moment estimate

\[
 \sum_{D\in\mathcal D_r}d(D)=\Theta(\sqrt r\,B_r)
\]

therefore yields

\[
 \boxed{|\mathcal J|=O(B_r/\sqrt r).}             \tag{8.6}
\]

This is a genuine square-root contraction at the positive-winding
boundary, but it is still larger than the quotient target
\(o(B_r/N)\) by a factor of order \(\sqrt r\). Equations (8.2) and (8.6)
pinpoint the remaining issue: static enumeration is Catalan-dense, while
the available dynamical mass charge stops exactly at the critical
square-root scale. Any proof of \((RP_A)\) must extract one further
square-root factor from phase correlation or interval clustering.

## 9. Complete all-root classification with the inverse-Pascal weight retained

For completeness, the primitive formula sits inside an exact formula for
all roots. Fix a nonempty pruned core \(F\in\mathcal D_d\), let
\(k=\operatorname{pk}(F)\), and let \(t\) be the free occupancy of the
terminal root corner in an inverse lift. In the reduced PBBS starting at
\(F\), let

\[
 0<B_1(F)<B_2(F)<\cdots
\]

be the positive selection times of the immediate predecessor of the
distinguished particle. The initial physical spacing is \(2t+1\), so the
predecessor enters the returned edge on its \((2t+2)\)-nd selection.
Before a full outer wrap this is the first possible entrant. Hence

\[
 \boxed{G(D)=B_{2t+2}(F)}.                         \tag{9.1}
\]

Fixing the terminal occupancy to \(t\) leaves the exact inverse-fibre
weight

\[
 \boxed{
 K_r(F,t)=\binom{r+d-k-t-1}{2d-1}.}                \tag{9.2}
\]

Consequently, if \(2H-1<2r+1\), the number of semilength-\(r\) roots
whose first return is at most \(2H-1\) is

\[
 \boxed{
 R_r(H)=\epsilon_r(H)+
 \sum_{d=1}^{r-1}\sum_{F\in\mathcal D_d}\sum_{t\ge0}
 \mathbf1_{\{B_{2t+2}(F)\le2H-1\}}
 \binom{r+d-\operatorname{pk}(F)-t-1}{2d-1},}     \tag{9.3}
\]

where \(\epsilon_r(H)\in\{0,1\}\) is the completely pruned height-one
root. Equivalently,

\[
 \boxed{
 \sum_{r\ge0}R_r(H)x^r
 =E_H(x)+
 \sum_{d\ge1}\sum_{F\in\mathcal D_d}\sum_{t\ge0}
 \mathbf1_{\{B_{2t+2}(F)\le2H-1\}}
 {x^{d+\operatorname{pk}(F)+t}\over(1-x)^{2d}}.} \tag{9.4}
\]

The primitive identity (4.1) is the subcase in which \(F\) is primitive,
\(t=0\), and the second root corner is also empty. Thus (9.3) is not a
relaxation: it is the exact all-rank classification requested by the
primitive recursion, with every inverse-Pascal multiplicity retained.
The sole unknown is now the dynamic predecessor-occurrence predicate in
the indicator.
