# Five-slot Bellman clocks: exact maximum-efficiency Apéry normal forms

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical reduction.  It preserves every
finite transient of every five-slot Bellman clock and reduces the four
maximum-efficiency branches to explicit finite Gaussian gates.  It does
**not** prove five-slot positivity, the all-slot Bellman inequality, or an
OR-word upper bound.

Put

\[
 A={\sqrt\pi\over2}
\]

and let

\[
 K(x)=
 \begin{cases}
 1-e^{-(A-x)^2}-e^{-(A+x)^2},&0\le x\le A,\\
 -e^{-(A+x)^2},&x>A.
 \end{cases}
\tag{0.1}
\]

Consider a nonnegative internally superadditive table

\[
 (c_0,c_1,c_2,c_3,c_4,c_5),\qquad c_0=0,
\tag{0.2}
\]

so that

\[
 c_{i+j}\ge c_i+c_j\qquad(i+j\le5),
\tag{0.3}
\]

and assume `c_5>=A`.  Its Bellman clock and functional are

\[
 V_0=0,\qquad
 V_m=\max_{1\le j\le\min(m,5)}(c_j+V_{m-j}),
\tag{0.4}
\]

and

\[
 \Phi(c)=\sum_{m\ge0}K(V_m).
\tag{0.5}
\]

For a period `P>0` and shifts `s_1,...,s_(h-1)`, write

\[
 \mathcal L_h(P;s_1,\ldots,s_{h-1})
 =\sum_{q\ge0}\left(K(qP)+\sum_{r=1}^{h-1}K(qP+s_r)\right).
\tag{0.6}
\]

All displayed Gaussian series converge absolutely.

## 1. First crossing and the four efficiency branches

The already-proved first-crossing theorem and complete positivity for at
most four slots immediately give the following normalization.

### Proposition 1.1 (first possible five-slot obstruction)

If a five-slot table has nonpositive Bellman functional, then it may be
chosen with

\[
 c_1,c_2,c_3,c_4<A\le c_5.
\tag{1.1}
\]

Moreover, at least one of the sizes

\[
 h\in\{2,3,4,5\}
\tag{1.2}
\]

has maximal efficiency:

\[
 {c_h\over h}=\max_{1\le j\le5}{c_j\over j}.
\tag{1.3}
\]

Thus it is enough to analyze four distinguished-maximizer branches.  Ties
may be assigned to any one of their maximizing sizes, or to the least such
size to make the partition disjoint.

#### Proof

If the first index `N` with `c_N>=A` satisfies `N<=4`, deletion after that
index does not increase the Bellman functional.  The remaining prefix has
at most four slots and therefore has strictly positive functional.  Hence
a nonpositive example must have first crossing at five, proving (1.1).

Internal superadditivity gives `c_2>=2c_1`, so size one is never strictly
more efficient than size two.  This proves (1.2)--(1.3). \(\square\)

## 2. Availability-filtered Apéry theorem

The next statement is the exact normal form used in every branch.  Unlike
an eventual-periodicity statement, it also records every transient caused
by an optimal residue witness arriving too late to fit a small capacity.

Fix any maximizer `h` from (1.3), and put

\[
 \lambda={c_h\over h},\qquad P=h\lambda=c_h,
 \qquad d_j=c_j-j\lambda\le0.
\tag{2.1}
\]

On the residue set `Z/hZ`, allow a directed step labelled `j` for every

\[
 j\in\{1,2,3,4,5\}\setminus\{h\}.
\]

The step adds `j mod h`, has ordinary capacity `j`, and reduced weight
`d_j`.  Let `mathcal P_r^(h)` be the finite set of simple directed paths
from zero to residue `r`; simple means that no residue vertex is repeated.
For a path `Q`, put

\[
 \ell(Q)=\sum_{j\in Q}j,
 \qquad
 d(Q)=\sum_{j\in Q}d_j.
\tag{2.2}
\]

For `r=0`, the empty path is included and is the only simple path from zero
to zero.  Define the availability-filtered residue value

\[
 \beta_r(m)=
 \max\{d(Q):Q\in\mathcal P_r^{(h)},\ \ell(Q)\le m\}.
\tag{2.3}
\]

For `m congruent r mod h`, the family in (2.3) is nonempty: it contains the
simple path obtained by reducing the exact fill by `m` size-one steps.

### Theorem 2.1 (exact availability-filtered clock)

For every `m>=0`, with `r=m mod h`, one has

\[
 \boxed{V_m=\lambda m+\beta_r(m).}
\tag{2.4}
\]

Every path in `mathcal P_r^(h)` has at most `h-1` edges.  Consequently, if

\[
 M_h=\max(\{1,2,3,4,5\}\setminus\{h\}),
 \qquad L_h=(h-1)M_h,
\tag{2.5}
\]

then all residue witnesses are available once `m>=L_h`.  Explicitly,

\[
 (L_2,L_3,L_4,L_5)=(5,10,15,16).
\tag{2.6}
\]

Put

\[
 \beta_r=\max_{Q\in\mathcal P_r^{(h)}}d(Q),
 \qquad s_r=r\lambda+\beta_r,
 \qquad s_0=0.
\tag{2.7}
\]

Then

\[
 0\le s_r<P\qquad(1\le r<h),
\tag{2.8}
\]

and

\[
 \boxed{V_{qh+r}=qP+s_r\quad\text{whenever }qh+r\ge L_h.}
\tag{2.9}
\]

Finally define the formal lattice value

\[
 \widehat V_{qh+r}=qP+s_r\qquad(q\ge0,\ 0\le r<h).
\tag{2.10}
\]

The Bellman functional has the exact finite-head decomposition

\[
 \boxed{
 \Phi(c)=
 \mathcal L_h(P;s_1,\ldots,s_{h-1})
 +\sum_{m=0}^{L_h-1}\bigl(K(V_m)-K(\widehat V_m)\bigr).
 }
\tag{2.11}
\]

No transient is omitted in (2.11).

#### Proof

Take any exact-fill configuration of capacity `m`.  Reading its generators
in any order gives a residue walk from zero to `r=m mod h`, of reduced
weight equal to its value minus `lambda m`.  A size-`h` step is a zero
loop.  More generally, whenever the walk repeats a residue, the intervening
closed segment has capacity divisible by `h` and nonpositive reduced
weight.  Delete that segment.  Iterating leaves a simple path `Q` with

\[
 \ell(Q)\le m,
 \qquad d(Q)\ge\text{the original reduced weight}.
\]

This proves the upper bound in (2.4).

Conversely, if `Q` contributes to (2.3), then `m-ell(Q)` is a nonnegative
multiple of `h`.  Padding `Q` by that many size-`h` generators produces an
exact fill of capacity `m`; the padding has zero reduced weight.  This
proves equality in (2.4).

A simple path on `h` residue vertices has at most `h-1` edges, proving
(2.5)--(2.6).  For `r<h`, the path of `r` size-one steps is simple, so

\[
 s_r\ge r\lambda+r(c_1-\lambda)=rc_1\ge0.
\]

All reduced weights are nonpositive, hence `beta_r<=0` and
`s_r<=r lambda<P`.  This proves (2.8).  Once `m>=L_h`, every simple path is
available, giving (2.9).  Splitting the full sum into the formal lattice and
the finitely many capacities below `L_h` proves (2.11). \(\square\)

## 3. The size-two-efficient branch: two pulses only

Write

\[
 (c_1,c_2,c_3,c_4,c_5)=(x,y,z,w,T)
\]

and suppose `y/2` is maximal.  Put

\[
 s=T-2y.
\tag{3.1}
\]

Internal superadditivity and maximal efficiency imply

\[
 x\le z-y\le s\le {y\over2},
 \qquad w=2y.
\tag{3.2}
\]

Indeed, `z>=x+y`, `T>=y+z`, `T<=5y/2`, and
`2y<=w<=2y`.

### Theorem 3.1 (exact two-efficient normal form)

The complete Bellman clock is

\[
 \boxed{
 V_{2q}=qy,\qquad
 V_1=x,\qquad V_3=z,\qquad
 V_{2q+1}=qy+s\quad(q\ge2).
 }
\tag{3.3}
\]

Consequently

\[
 \boxed{
 \Phi=
 \mathcal L_2(y;s)
 +K(x)-K(s)
 +K(z)-K(y+s).
 }
\tag{3.4}
\]

Thus this branch is an effective two-state Gaussian clock with exactly two
finite pulses.  Formula (3.4) is an exact reduction, not a positivity claim.

#### Proof

All even fills are bounded above by density `y/2` and are attained by size
two.  Modulo two, every nonempty simple path consists of one odd step.
The size-five step dominates the size-three and size-one reduced weights
because

\[
 T-y\ge z,\qquad T-2y\ge x.
\]

It first becomes available at capacity five.  Before then, internal
superadditivity gives `V_1=x` and `V_3=z`; from capacity five onward,
size-two padding proves the odd formula in (3.3).  Subtracting the two
formal odd lattice entries at capacities one and three gives (3.4).
\(\square\)

## 4. The size-three-efficient branch: five pulses

Suppose `p=c_3` has maximal efficiency.  Put

\[
 a=c_4-p,\qquad b=c_5-p.
\tag{4.1}
\]

Then

\[
 a\ge c_1,\qquad b\ge c_2,
 \qquad 0\le a\le {p\over3},
 \qquad 0\le b\le {2p\over3}.
\tag{4.2}
\]

Define the two eventual shifts

\[
 \boxed{
 s_1=\max\{a,2b-p\},
 \qquad
 s_2=\max\{b,2a\}.
 }
\tag{4.3}
\]

### Theorem 4.1 (exact three-efficient normal form)

The finite values needed before stabilization are

\[
\begin{array}{c|ccccccccccc}
m&0&1&2&3&4&5&6&7&8&9&10\\ \hline
V_m&0&c_1&c_2&p&c_4&c_5&2p&V_7&V_8&3p&3p+s_1,
\end{array}
\tag{4.4}
\]

where

\[
 V_7=\max\{p+c_4,c_5+c_2\},
 \qquad
 V_8=\max\{2c_4,p+c_5\}.
\tag{4.5}
\]

Thereafter

\[
 \boxed{
 \begin{aligned}
 V_{3q}&=qp,\\
 V_{3q+1}&=qp+s_1&& (q\ge3),\\
 V_{3q+2}&=qp+s_2&& (q\ge2).
 \end{aligned}}
\tag{4.6}
\]

The exact functional is

\[
\boxed{
\begin{aligned}
 \Phi={}&\mathcal L_3(p;s_1,s_2)\\
 &+K(c_1)-K(s_1)
  +K(c_4)-K(p+s_1)
  +K(V_7)-K(2p+s_1)\\
 &+K(c_2)-K(s_2)
  +K(c_5)-K(p+s_2).
\end{aligned}}
\tag{4.7}
\]

Thus this branch is an effective three-state Gaussian lattice with exactly
five finite pulses.

#### Proof

Modulo three, size four dominates size one as a residue-one step because
`c_4>=p+c_1`, and size five dominates size two as a residue-two step
because `c_5>=p+c_2`.  A simple residue-one path is either one
residue-one step or two residue-two steps; a simple residue-two path is
either one residue-two step or two residue-one steps.  Translating the
reduced weights gives exactly (4.3).

The double size-five witness for `s_1` has capacity ten, while the double
size-four witness for `s_2` has capacity eight.  Availability filtering
therefore gives (4.4)--(4.6).  At capacity seven the only undominated
residue-one candidates are `3+4` and `2+5`; at capacity eight the only
undominated residue-two candidates are `4+4` and `3+5`, proving (4.5).
Comparing the five exceptional entries with the formal three-lattice gives
(4.7). \(\square\)

## 5. The size-four-efficient branch: twelve linear Apéry forms

Suppose `P=c_4` has maximal efficiency, and put

\[
 e=c_5-P,
\qquad
 d_1=e-{P\over4},
\qquad
 d_2=c_2-{P\over2},
\qquad
 d_3=c_3-{3P\over4}.
\tag{5.1}
\]

Here `e>=c_1`, so the size-five generator is the best eventual
residue-one step; all three displayed reduced weights are nonpositive.
The simple-path enumeration on `Z/4Z` gives

\[
\boxed{
\begin{aligned}
 \beta_1&=\max\{d_1,d_2+d_3,d_1+2d_2,3d_3\},\\
 \beta_2&=\max\{d_2,2d_1,2d_3,d_1+d_2+d_3\},\\
 \beta_3&=\max\{d_3,d_1+d_2,3d_1,2d_2+d_3\},
\end{aligned}}
\tag{5.2}
\]

and

\[
 s_r={rP\over4}+\beta_r\qquad(1\le r\le3).
\tag{5.3}
\]

### Theorem 5.1 (exact four-efficient gate)

The Bellman functional is exactly

\[
 \boxed{
 \Phi=
 \mathcal L_4(P;s_1,s_2,s_3)
 +\sum_{m=0}^{14}\bigl(K(V_m)-K(\widehat V_m)\bigr),
 }
\tag{5.4}
\]

where every `V_m` in the finite sum is the explicit maximum (2.4) over
simple paths of ordinary capacity at most `m`.  Hence the branch consists
of twelve displayed linear Apéry forms and fifteen completely finite head
entries.  Formula (5.4) retains the early size-one representative before
the better congruent size-five representative becomes available.

#### Proof

There are five simple paths from zero to each nonzero residue in the
complete three-step residue graph on four vertices.  Reversing the order of
the two one-intermediate paths can give the same reduced linear form, so
the distinct weights are precisely the four forms in each line of (5.2).
The largest possible ordinary capacity is three size-five steps, namely
fifteen.  Theorem 2.1 gives (5.4). \(\square\)

## 6. The size-five-efficient branch: sixteen paths per residue

Finally suppose `P=c_5` has maximal efficiency, and put

\[
 d_j=c_j-{jP\over5}\le0\qquad(1\le j\le4).
\tag{6.1}
\]

For each nonzero residue `r mod 5`, a simple path from zero to `r` is
obtained by choosing an ordered list of distinct intermediate vertices from
the other three nonzero residues.  Hence there are exactly

\[
 1+3+3\cdot2+3\cdot2\cdot1=16
\tag{6.2}
\]

simple paths to each `r`.

### Theorem 6.1 (exact five-efficient gate)

Let `beta_r` be the maximum of the sixteen corresponding linear forms in
`d_1,d_2,d_3,d_4`, and put `s_r=rP/5+beta_r`.  Then

\[
 \boxed{
 \Phi=
 \mathcal L_5(P;s_1,s_2,s_3,s_4)
 +\sum_{m=0}^{15}\bigl(K(V_m)-K(\widehat V_m)\bigr).
 }
\tag{6.3}
\]

Every `V_m` in the head is again the exact availability-filtered maximum
(2.4).  Thus the endpoint-efficient branch is a finite piecewise-Gaussian
problem: four maxima of sixteen linear forms, plus sixteen finite head
entries.  There is no unstructured infinite Bellman recursion left.

#### Proof

The path count is (6.2).  A simple path has at most four edges and every
available edge has capacity at most four, so all paths are available by
capacity sixteen.  Theorem 2.1 gives (6.3). \(\square\)

## 7. Exact frontier after the reduction

Combining the preceding sections gives a complete proof-safe reduction of
the first unresolved Bellman length:

* any nonpositive table first crosses `A` at size five;
* the size-two branch is a two-lattice plus two pulses;
* the size-three branch is a three-lattice plus five pulses;
* the size-four branch has twelve linear Apéry forms and a head below 15;
* the size-five branch has sixteen paths per residue and a head below 16.

The theorem deliberately does **not** assert that any of these finite
Gaussian gates is positive.  Establishing their signs is the next Bellman
problem.  In particular, this note does not prove the universal Bellman
inequality and does not by itself prove `nu(k)<=B(k)+O(1)`.
