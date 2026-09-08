# Product-SCD tails cannot absorb the Gaussian annulus by local baseline sharing

Date: 2026-07-26

## 0. Result

Put

\[
  W_m={2m\choose m}.
\]

Fix arbitrary symmetric-chain decompositions of two disjoint (m)-cubes.
The factor-blind exterior construction associates to every ordered pair of
half-cube chains a word (L(C)\Vert R(D)).  Two natural attempts to reuse
the middle baseline are:

1. credit every middle set which is already represented internally by its
   product-SCD gadget; or
2. replace the middle baseline independently inside each product box by an
   arbitrary word whose letters remain in that box.

Neither attempt crosses a fixed Gaussian cutoff.  More precisely, if

\[
  H=A\sqrt m+o(\sqrt m),\qquad 0\le A<\infty,
\]

then:

* even after granting one unit of free baseline credit for every internal
  middle witness of every canonical tail gadget, the remaining normalized
  charge tends to a strictly positive function (G(A));
* every product-box-local word covering the middle diagonal and even just
  the lower exterior has length at least

\[
  (1+J(A)+o(1))W_m,
\]

where (J(A)>0) for finite (A), and (J(0)=\sqrt2).

Thus the product-SCD tail cannot be fused to PBBS by independent gadget or
independent box substitutions.  Any successful Gaussian-annulus fusion
must use witnesses which cross product boxes (a genuinely nonlocal braid),
or it must solve the PBBS fixed-window packing gate by another method.

This is a limitation of two precisely defined fusion architectures, not a
lower bound for arbitrary contiguous-OR words.

## 1. Exact diagonal credit in one canonical gadget

Let a half-cube symmetric chain of minimum rank (a) run through ranks

\[
  a,a+1,\ldots,m-a.
\]

As in the audited product-SCD tail, put

\[
 A_m(a)={m\choose a}-{m\choose {a-1}},
 \qquad
 w_m(a)=
 \begin{cases}
 m,&a=0,\\
 m-2a+1,&a>0.
 \end{cases}
\]

For chains (C,D) of minimum ranks (a,b), the canonical word is

\[
  \mathcal G(C,D)=L(C)\Vert R(D),
  \qquad |\mathcal G(C,D)|=w_m(a)+w_m(b).             \tag{1.1}
\]

### Lemma 1.1 (exact number of internal middle witnesses)

The number of distinct rank-\(m\) sets represented by intervals wholly
inside \(\mathcal G(C,D)\) is

\[
  d_m(a,b)=m-2\max\{a,b\}+1.                         \tag{1.2}
\]

These represented middle sets are disjoint as ((C,D)) ranges over chain
pairs.

#### Proof

The entries of (L(C)) are the reversed increment blocks of (C), and
the entries of (R(D)) are the forward increment blocks of (D).  An
interval crossing their common seam has union (C_i\cup D_j).  It has
rank (m) exactly when

\[
 i+j=m,
 \quad a\le i\le m-a,
 \quad b\le j\le m-b.
\]

The permitted values of (i) form

\[
 [\max(a,b),m-\max(a,b)],
\]

which has the size in (1.2).  If (a=0) or (b=0), the two extreme
solutions are represented by an interval wholly in one half when needed;
the same count remains valid.  Finally, the products (C\times D)
partition the Boolean cube, so middle sets belonging to different chain
pairs are distinct.  \(\square\)

For (r=m-H-1), define the canonical internal-credit residual

\[
 \begin{split}
 E_m(H):={}&\sum_{a+b\le m-H-1}A_m(a)A_m(b)\\
 &\qquad\cdot
 \bigl(w_m(a)+w_m(b)-d_m(a,b)\bigr).                 \tag{1.3}
 \end{split}
\]

The actual word consisting of all canonical gadgets, followed by every
middle set not already represented internally, has length exactly

\[
  W_m+E_m(H).                                         \tag{1.4}
\]

It covers the middle layer and both exterior tails.  Equation (1.4) also
gives the most optimistic possible ledger for a PBBS splice which credits
only gadget-internal middle witnesses: it grants the physical deletion of
the corresponding PBBS baseline owner for free.

### Theorem 1.2 (fixed-Gaussian internal-credit obstruction)

If (H/\sqrt m\to A<\infty), then

\[
  \boxed{
  {E_m(H)\over W_m}\longrightarrow
  G(A):={64\over\sqrt\pi}
  \int_{u+v\ge A}uv\max(u,v)e^{-2(u^2+v^2)}\,du\,dv.} \tag{1.5}
\]

In particular (G(A)>0) for every finite (A), and

\[
  G(0)=2\sqrt2-1.                                     \tag{1.6}
\]

#### Proof

It is enough to write the even-\(m\) calculation; the odd parity has the
same local limit, and the boundary cases \(a=0\) or \(b=0\) contribute
only \(e^{-\Omega(m)}W_m\).

Write (m=2h), (a=h-x), and (b=h-y).  Away from the negligible
boundary cases,

\[
 \begin{split}
 w_m(a)&=2x+1,\\
 w_m(b)&=2y+1,\\
 d_m(a,b)&=2\min(x,y)+1,
 \end{split}
\]

and hence the residual contribution of this chain pair is

\[
  2\max(x,y)+1.                                       \tag{1.7}
\]

The inclusion condition is (x+y\ge H+1).  Uniformly for
(x=u\sqrt m+o(\sqrt m)) on compact (u)-ranges,

\[
 A_m(h-x)
 ={2^m\over m}\left(
  4\sqrt{2\over\pi}\,u e^{-2u^2}+o(1)
 \right).                                             \tag{1.8}
\]

For completeness, when \(m=2h+1\), put again \(a=h-x,b=h-y\).  Then,
away from the same negligible boundary,

\[
 w_m(a)=2x+2,\qquad w_m(b)=2y+2,\qquad
 d_m(a,b)=2\min(x,y)+2,
\]

while the inclusion condition is \(x+y\ge H\).  Thus the scaled summand
and the local limit are identical.

The usual Gaussian bound for central binomial coefficients dominates the
tails, so the two-dimensional Riemann sum in (1.3), divided by

\[
 {2m\choose m}\sim {4^m\over\sqrt{\pi m}},
\]

converges to (1.5).  Positivity is immediate from the integral.  At
(A=0), symmetry gives

\[
 \begin{split}
 \int_0^\infty\!\int_0^\infty
 uv\max(u,v)e^{-2(u^2+v^2)}\,du\,dv
 ={\sqrt\pi(2\sqrt2-1)\over64},
 \end{split}
\]

which proves (1.6).  \(\square\)

The full canonical product-SCD word has normalized length (2\sqrt2+o(1))
at a sub-Gaussian cutoff.  Theorem 1.2 says that its internal middle
diagonals recover exactly one unit of that coefficient, and no more:

\[
 2\sqrt2-1=G(0).                                      \tag{1.9}
\]

Thus the most literal baseline-sharing idea remains a positive constant
away from coefficient one.

## 2. A statewise obstruction to every independent box-local replacement

The preceding theorem concerns the canonical gadget.  The next result
allows an arbitrary word in every product box, but requires the letters
and witnesses assigned to a box to remain in that box.  This is exactly
the independent product-box fusion model.

For chains (C,D) of step lengths

\[
  p=m-2a,\qquad q=m-2b,
\]

identify their product with the join-semilattice

\[
  [0,p]\times[0,q]
\]

under coordinatewise maximum.  Its middle diagonal has local rank

\[
  c={p+q\over2}=m-a-b                              \tag{2.1}
\]

and width

\[
  d(p,q)=\min(p,q)+1.                                  \tag{2.2}
\]

### Lemma 2.1 (axis/start lower bound)

Let a word with letters in ([0,p]\times[0,q]) represent

1. every point of local rank (c); and
2. every point of local rank at most (c-H-1).

Put (s=c-H-1).  If (s\ge0), its length is at least

\[
 \max\left\{
 d(p,q),
 1+\min(p,s)+\min(q,s)
 \right\}.                                            \tag{2.3}
\]

If (s<0), its length is at least (d(p,q)).

If the minimum of this product box is the empty Boolean mask, the second
term in (2.3) is reduced by one, because the origin is not a required
target.  This happens for exactly one product box and changes every global
bound below by at most one.

#### Proof

The lower family contains the two axis segments

\[
 (i,0),\quad0\le i\le\min(p,s),
 \qquad
 (0,j),\quad1\le j\le\min(q,s).
\]

To obtain ((i,0)) as a coordinatewise maximum, every letter in its
witness has second coordinate zero and at least one letter is exactly
((i,0)).  Hence the word contains every displayed axis point as a
physical occurrence.  This proves the second term in (2.3).

For the first term, choose one witness for every middle-diagonal point.
Two distinct equal-rank points cannot use intervals with the same left
endpoint: enlarging an interval on the right only increases its join,
whereas distinct equal-rank points are incomparable.  Their left endpoints
are therefore distinct, and the word has at least (d(p,q)) positions.
\(\square\)

Define

\[
 e_H(p,q)=
 \left[
 1+\min(p,s)+\min(q,s)-d(p,q)
 \right]_+,
 \qquad s={p+q\over2}-H-1,                            \tag{2.4}
\]

with (e_H=0) when (s<0).

### Theorem 2.2 (fixed-Gaussian box-local obstruction)

Suppose one chooses, independently in every product-SCD box, a box-valued
word which covers that box's middle diagonal and its lower exterior below
rank (m-H).  Concatenating these words has length at least

\[
  W_m+\sum_{a,b}A_m(a)A_m(b)e_H(m-2a,m-2b)-1.         \tag{2.5}
\]

If (H/\sqrt m\to A<\infty), then

\[
 \boxed{
 {1\over W_m}\sum_{a,b}A_m(a)A_m(b)e_H(m-2a,m-2b)
 \longrightarrow J(A),}                              \tag{2.6}
\]

where

\[
 J(A)={32\over\sqrt\pi}
 \int_0^\infty\!\int_0^\infty
 uv\,\eta_A(u,v)e^{-2(u^2+v^2)}\,du\,dv,             \tag{2.7}
\]

and, writing (M=\max(u,v)), (l=\min(u,v)),

\[
 \eta_A(u,v)=
 \begin{cases}
 0,&M\le A,\\
 2(M-A),&M>A\text{ and }M-l\le A,\\
 l+M-A,&M-l>A.
 \end{cases}                                          \tag{2.8}
\]

Consequently (J(A)>0) for every finite (A), while

\[
  J(0)=\sqrt2.                                         \tag{2.9}
\]

#### Proof

Lemma 2.1 gives a lower bound (d+e_H) in each box.  Exact width
aggregation for products of the two half-cube SCDs gives

\[
 \sum_{a,b}A_m(a)A_m(b)d(m-2a,m-2b)=W_m,              \tag{2.10}
\]

which proves (2.5).

For the limit, first take (m=2h), (a=h-x), (b=h-y), and scale
(x=u\sqrt m), (y=v\sqrt m).  If (u\le v), direct substitution in
(2.4) gives, after division by (\sqrt m),

\[
 \eta_A(u,v)=
 \begin{cases}
 0,&v\le A,\\
 2(v-A),&v>A\text{ and }v-u\le A,\\
 u+v-A,&v-u>A.
 \end{cases}
\]

This is (2.8).  Equation (1.8), Gaussian domination, and the same Riemann
sum as in Theorem 1.2 give (2.6)--(2.7).  The integrand is positive on an
open set for every finite (A).  At (A=0),

\[
 \eta_0(u,v)=u+v
\]

off a null set, and

\[
 {32\over\sqrt\pi}
 \int_0^\infty\!\int_0^\infty
 uv(u+v)e^{-2(u^2+v^2)}\,du\,dv=\sqrt2.
\]

When \(m=2h+1\), the step lengths are \(2x+1,2y+1\), the middle
width is \(2\min(x,y)+2\), and
\(s=x+y-H\).  After division by \(\sqrt m\) these unit shifts vanish,
giving the same \(\eta_A\) and the same dominated Riemann sum.

This proves the theorem.  Requiring the upper exterior as well can only
increase the minimum length.  \(\square\)

### Theorem 2.3 (positive-density cross-box witnesses are necessary)

Fix the product-SCD partition, and let \(\mathcal W\) be an arbitrary
literal Boolean word.  Every physical letter belongs to a unique product
box.  For every required target choose one witnessing interval, and call
the witness **local** if all its letters belong to the target's own
product box.

Let \(R_{\rm mid}\) be the number of middle-layer targets whose chosen
witness is not local.  In every box with \(s=c-H-1\ge0\), retain the two
axis families used in Lemma 2.1, and let \(R_{\rm ax}\) be the number of
these axis targets whose chosen witnesses are not local.  Then

\[
 \boxed{
 |\mathcal W|
 \ge W_m+\sum_{a,b}A_m(a)A_m(b)e_H(m-2a,m-2b)
       -R_{\rm mid}-R_{\rm ax}-1.}                     \tag{2.11}
\]

Consequently, if \(H/\sqrt m\to A<\infty\) and
\(|\mathcal W|=W_m+o(W_m)\), then

\[
 \boxed{
 R_{\rm mid}+R_{\rm ax}
 \ge (J(A)-o(1))W_m.}                                  \tag{2.12}
\]

Thus “cross-box” is not merely a qualitative escape: every
coefficient-one fusion must route a positive-density family of
middle/annular witnesses across the product-SCD partition.

#### Proof

For a box \(B\), let \(r_B^{\rm mid}\) and \(r_B^{\rm ax}\) be its two
nonlocal counts.  A locally witnessed axis point forces its exact box
letter to occur, as in Lemma 2.1.  Hence the number \(L_B\) of physical
letters of \(\mathcal W\) belonging to \(B\) is at least

\[
 1+\min(p,s)+\min(q,s)-r_B^{\rm ax}.
\]

The locally witnessed middle targets have distinct left endpoints, all
occupied by letters of \(B\), so also

\[
 L_B\ge d(p,q)-r_B^{\rm mid}.
\]

Since the maximum of two numbers is one-Lipschitz in the sum of their
downward errors,

\[
 L_B\ge d(p,q)+e_H(p,q)
             -r_B^{\rm mid}-r_B^{\rm ax}.              \tag{2.13}
\]

Every physical letter belongs to exactly one box, so summing (2.13), using
the width identity (2.10), proves (2.11).  Equation (2.12) follows from
Theorem 2.2.  \(\square\)

## 3. Exact consequence for the Gaussian annulus

The current proved constructions occupy opposite sides of the Gaussian
scale:

\[
 \begin{array}{c|c}
 \text{PBBS central compiler}&H=o(\sqrt m),\\
 \text{economical product-SCD exterior}&H/\sqrt m\to\infty.
 \end{array}
\]

Theorems 1.2 and 2.2 show that the gap cannot be closed by either of the
following literal OR operations:

1. append the canonical chain-pair gadgets and delete one old baseline
   owner for each middle set represented internally by its own gadget;
2. repartition the PBBS middle baseline by product-SCD boxes and replace
   each box independently by a word staying inside that box.

Both leave an (\Omega_A(W_m)) charge at every fixed Gaussian cutoff.
This remains true after granting all physical seams between the replacement
blocks for free.  Hence seam bookkeeping is not the missing issue in these
models.

The only possible product-SCD/PBBS fusion not covered by the obstruction is
a genuinely nonlocal construction in which a positive-density family of
middle and annular witnesses crosses product-box boundaries.  This is the
same endpoint-reuse phenomenon isolated for the PBBS nonlocal baseline
braid: independent local collars cannot pay the Gaussian annulus, while a
global rank-monotone threading is not ruled out.

## 4. Logical boundary

This note proves no lower bound on the unrestricted function \(\nu(k)\).
It does not rule out:

* the fixed-window PBBS estimate \((\mathrm{ST}_A)\);
* a nonlocal PBBS braid;
* a cross-product-box word;
* a different SCD or rotor architecture; or
* any construction whose letters assigned to one target family leave its
  product box.

It does prove that the most direct interpretation of “share the PBBS
baseline with the product-SCD tail” cannot close the exact Gaussian
annulus.  The remaining fusion theorem must be nonlocal in precisely the
same sense as the surviving PBBS braid gate.

## 5. Audit of the portal-tree chronology

The separate portal-tree construction gives a closed Johnson walk
\(\mathscr W_H\) of state-sequence length

\[
 |\mathscr W_H|=W+O(H\operatorname{Cat}_m)
\]

which contains every directed PBBS window of length at most \(H\).
This is a correct chronology theorem, but it does not evade any
obstruction in this note and it is not a literal OR word of that length.

Indeed, if the middle states \(X_i\) themselves are used as letters, every
nonempty OR has rank at least \(m\), so no proper lower target is produced.
The usual erosion letters

\[
 A_i=\bigcap_{j=0}^{H}X_{i+j}
\]

reconstruct the \(X_i\)'s and their lower shadows only under delay-\(H\)
safety.  The inserted portal excursion \(P_vP_v^{-1}\) has an immediate
reversal at its turning point: a coordinate is exchanged and exchanged
back after two consecutive transitions.  Hence it is maximally unsafe for
this factorization.

More importantly, away from the \(O(\operatorname{Cat}_m)\) portals the
walk retains the entire original PBBS chronology, including the critical
short-residence family measured by \(\nu_H(P_m)\).  Repairing the portal
turns themselves costs only \(O(H\operatorname{Cat}_m)=o_A(W)\) at fixed
Gaussian width; literalizing the untouched PBBS bulk is still exactly the
open fixed-window seam problem.

Therefore:

\[
\boxed{
\text{Johnson chronology length}
\ \not=\ 
\text{literal contiguous-OR word length}.}
\]

The portal walk is a potentially useful state-sequence input to a new
nonlocal factorization, but no coefficient-one annulus conclusion follows
from its current form.
