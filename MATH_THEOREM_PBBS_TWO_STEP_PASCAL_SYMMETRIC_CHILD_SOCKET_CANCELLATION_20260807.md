# Two-step Pascal descent cancels the first off-middle negative socket row

**Date:** 2026-08-07  
**Status:** unconditional algebraic theorem for the complete binomial
histogram.  It repairs the *socket-tail sign* of the first two off-middle
children.  It does not by itself prove their whole-job price inequalities,
and therefore does not prove $FC_D$.

## 1. Formal states and their two-step split

For integers $k,r,t$, put $D=r-t$ and define the formal socket tails

\[
 K^{(k,r,t)}_q=
 \mathbf 1_{q\le D}
 \left\{{k\choose r}-{k\choose t+q-1}\right\}.
 \tag{1.1}
\]

As usual, a binomial coefficient outside its natural range is zero.  For
the complete lower histogram define also

\[
 \Gamma^{(k,r,t)}(q)
 =K^{(k,r,t)}_q-{k\choose t-q}.
 \tag{1.2}
\]

Pascal's identity holds separately for $K$ and for $\Gamma$.  Applying
it twice to a middle state, and writing

\[
 k=2r,\qquad R=r-1,\qquad t=r-D,
 \tag{1.3}
\]

gives, coordinatewise in $q$,

\[
\begin{split}
 X^{(2r,r,r-D)}={}&
 X^{(2R,R+1,R+1-D)}
 +2X^{(2R,R,R-D)}\\
 &+X^{(2R,R-1,R-1-D)},
 \qquad X\in\{K,\Gamma\}.
\end{split}
 \tag{1.4}
\]

The first and last terms are the symmetric distance-one children.  The
upper child is not a physical socket state: at its terminal coordinate,

\[
 K^{(2R,R+1,R+1-D)}_D
 ={2R\choose R+1}-{2R\choose R}<0.
 \tag{1.5}
\]

The next theorem shows that it is wrong to discard that child in
isolation: its symmetric partner cancels the defect exactly.

## 2. Exact symmetric-pair tail formula

For $0\le s\le R$, let $P_s(R,D)$ denote the sum of the two formal
states

\[
 (2R,R+s,R+s-D),\qquad (2R,R-s,R-s-D).
 \tag{2.1}
\]

For $q\le D$, put

\[
 \ell=D-q+1,\qquad B_j={2R\choose j}.
 \tag{2.2}
\]

### Theorem 2.1 (symmetric chord identity)

The aggregate socket tail of $P_s(R,D)$ is

\[
 \boxed{
 K^{P_s}_{q}
 =2B_{R-s}-B_{R-s+\ell}-B_{R-s-\ell}.}
 \tag{2.3}
\]

It is zero for $q>D$.  Hence its sign is exactly the midpoint-concavity
sign of the $2R$-th binomial row on the chord of radius $\ell$ centred
at rank $R-s$.

#### Proof

The two owner ranks have the same size $B_{R-s}$.  The two collar ranks
subtracted at tail $q$ are

\[
 R+s-\ell,\qquad R-s-\ell.
\]

By symmetry $B_{R+s-\ell}=B_{R-s+\ell}$, which proves (2.3).
\(\square\)

There is a useful exact local test.  At $\ell=1$, division by
$B_{R-s}$ gives

\[
 \frac{B_{R-s+1}+B_{R-s-1}-2B_{R-s}}{B_{R-s}}
 =\frac{2(2s^2-R-1)}{(R-s+1)(R+s+1)}.
 \tag{2.4}
\]

Thus the unit chord is midpoint-concave if and only if

\[
                         2s^2\le R+1.
 \tag{2.5}
\]

More generally, if the binomial row is discretely concave throughout the
integer interval
$[R-s-\ell,R-s+\ell]$, then (2.3) is nonnegative.  Formula (2.4), shifted
along the row, gives the elementary sufficient condition

\[
                         2(s+\ell)^2\le R+1.
 \tag{2.6}
\]

At the other end, if $\ell\ge2s$, reflection places both endpoint ranks
weakly below $R-s$, and monotonicity of the lower half of the binomial
row again makes (2.3) nonnegative.  Only the finite band

\[
 1\le\ell<2s,\qquad 2(s+\ell)^2>R+1
 \tag{2.7}
\]

can require a sharper chord calculation.  This is the exact curvature
gate for extending the pairing to more distant states.

## 3. The distance-one pair is always a genuine socket profile

### Theorem 3.1 (first off-middle cancellation)

Let $R\ge1$ and $1\le D\le R+1$.  The aggregate tails of the
distance-one pair $P_1(R,D)$ are nonnegative integers and are
nonincreasing in $q$.  Consequently there are nonnegative integral
socket multiplicities

\[
 M_q=K^{P_1}_q-K^{P_1}_{q+1}\quad(1\le q\le D),
 \qquad K^{P_1}_{D+1}=0,
 \tag{3.1}
\]

whose conjugate tails are exactly $K^{P_1}$.

At the terminal coordinate the cancellation has the explicit positive
value

\[
 \boxed{
 K^{P_1}_D
 =2{2R\choose R-1}-{2R\choose R}-{2R\choose R-2}
 ={2(R-1)\over(R+1)(R+2)}{2R\choose R}\ge0.}
 \tag{3.2}
\]

For $R>1$ it is strictly positive, even though the upper summand in
(1.5) is strictly negative.

#### Proof

For $s=1,\ell=1$, (3.2) follows from

\[
 {B_{R-1}\over B_R}={R\over R+1},\qquad
 {B_{R-2}\over B_R}={R(R-1)\over(R+1)(R+2)}.
 \tag{3.3}
\]

For $\ell\ge2$, reflect the upper endpoint in (2.3):

\[
 K^{P_1}(\ell)
 =2B_{R-1}-B_{R+1-\ell}-B_{R-1-\ell}\ge0,
 \tag{3.4}
\]

because both displayed endpoint ranks are at most $R-1$.  Moreover the
right side is nondecreasing with $\ell$ once $\ell\ge2$.  The remaining
first step is also increasing, since

\[
 K^{P_1}(2)-K^{P_1}(1)
 =(B_R-B_{R-1})+(B_{R-2}-B_{R-3})\ge0.
 \tag{3.5}
\]

Here coefficients below rank zero are interpreted as zero.  Because
$\ell=D-q+1$ decreases as $q$ increases, the $q$-tails are
nonincreasing.  Equations (3.1) now give the claimed integral socket
profile. \(\square\)

### Corollary 3.2 (the full signed row need not become positive)

The cancellation in Theorem 3.1 is exactly a socket-tail cancellation,
not coefficientwise positivity of the complete signed kernel.  For the
symmetric distance-$s$ pair and $q\le D$,

\[
\begin{split}
 \Gamma^{P_s}(q)={}&K^{P_s}_q
 -{2R\choose R+s-D-q}
 -{2R\choose R-s-D-q}.
\end{split}
 \tag{3.6}
\]

In particular,

\[
 \boxed{
 \Gamma^{P_1}(D)
 ={2(R-1)\over(R+1)(R+2)}{2R\choose R}
 -{2R\choose R+1-2D}-{2R\choose R-1-2D}.}
 \tag{3.7}
\]

This coefficient can be negative.  At the actual depth-four descent
parameters $R=24,D=4$, for example,

\[
 K^{P_1}_4=2282138106804,
 \qquad
 \Gamma^{P_1}(4)=-3055543457052.
 \tag{3.8}
\]

Thus two-step pairing removes the obstruction to interpreting the
aggregate *socket supply* physically, but a proof of the paired all-price
inequality would still have to use the min-plus restrictions on the
increment sequence.  In fact Section 4 shows that even the restricted
standalone paired inequality is false.  A coefficientwise
nonnegative-$\Gamma$ induction is therefore certainly impossible.

## 4. The finite-state Pascal pattern

The symmetric states close exactly under two-step descent.  With the
convention $P_{-s}=P_s$, Pascal's identity gives, coordinatewise for
both $K$ and $\Gamma$,

\[
 \boxed{
 P_s(R,D)=P_{s+1}(R-1,D)+2P_s(R-1,D)+P_{s-1}(R-1,D).}
 \tag{4.1}
\]

Indeed, the three grandchildren of the $+s$ state have distances
$s+1,s,s-1$ from the new middle rank, with coefficients $1,2,1$;
the grandchildren of the $-s$ state pair with them symmetrically.

For $s=0$, (1.4) is exactly

\[
 P_0(R,D)=2P_1(R-1,D)+2P_0(R-1,D),
 \tag{4.2}
\]

because $P_0$ consists of two identical middle states.  Thus the
negative child in one-step Pascal descent is not an intrinsic obstruction:
the natural state space is the half-line of symmetric distances, and its
transition kernel is the finite-band stencil $(1,2,1)$.

What remains unresolved is equally precise.  Although $P_1$ has a
genuine aggregate socket partition, its two canonical job histograms are
still separately prescribed.  Nonnegative socket tails do not imply its
all-price inequality.
For larger $s$, even socket physicality is controlled by the explicit
finite curvature band (2.7).  Therefore (4.1) supplies a viable paired
induction state and identifies its next gate, but it is not an induction
proof of $FC_D$.

### Proposition 4.1 (standalone pair positivity is false)

For a formal state $X$ and a closed covering price $\psi$, write

\[
 \mathfrak F(X;\psi)
 =\sum_q\Gamma^X(q)
       \bigl(\psi(q)-\psi(q-1)\bigr).
 \tag{4.3}
\]

Take the actual depth-four parent $(k,r,t)=(50,25,21)$.  Its two-step
central child is $(48,24,20)$ and its outer pair is $P_1(24,4)$.  Hence
(1.4) gives the exact identity

\[
 \boxed{
 \mathfrak F(P_1(24,4);\psi)
 =M_{50}(\psi)-2M_{48}(\psi),}
 \tag{4.4}
\]

where $M_k$ is the complete binomial margin.  On the thirteen exact
depth-four fan rays, the paired margins are

\[
\begin{array}{c|rrrrrrr}
i&1&2&3&4&5&6&7\\ \hline
\mathfrak F(P_1;\psi_i)
&1200026854079&381599184541&-280118481243
&1897283818727&-570294445018&417138483405
&1435708053510
\end{array}
\tag{4.5}
\]

\[
\begin{array}{c|rrrrrr}
i&8&9&10&11&12&13\\ \hline
\mathfrak F(P_1;\psi_i)
&-2855680888673&-849678390145&628359006127
&2634361504655&1273364569925&701696721973
\end{array}
\tag{4.6}
\]

Every entry is reproduced by (4.4) from the depth-four worksheet.  In
particular the pair fails on rays $3,5,8,9$, including the linear volume
price $\psi_8(L)=L$.  Thus an induction that asks every symmetric state
$P_s$ to satisfy its own all-price inequalities is false.  The parent is
positive because the two central children in (1.4) subsidize the negative
outer pair.  Any viable Pascal invariant must retain a weighted cone of
central and off-middle states, not merely replace individual children by
standalone symmetric pairs.

## 5. Exact conclusion

The prior one-step obstruction was real but too local.  Two Pascal steps
split a middle state into two central copies plus a symmetric distance-one
pair; the latter has an honest integral socket profile, with terminal
surplus (3.2).  The correct all-depth program is consequently:

1. retain symmetric pairs rather than individual off-middle children;
2. retain enough central mass to subsidize the negative pair margins in
   (4.5)--(4.6), seeking an invariant cone or potential under (4.1); and
3. control the finitely many chord defects in (2.7) as the distance state
   grows.

No claim beyond those three exact reductions is made here.
