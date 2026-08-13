# Audit of the conformal star-cycle reserve: exact telescope, failed safe-order argument, and one-path packing

**Date:** 2026-08-13  
**Audited source:** `/Users/amir.nuriyev/.codex/attachments/5ec15afb-4a96-4ec3-b3f1-a92cb96ee3e5/pasted-text.txt`  
**Frozen source SHA-256:** `37b04e2efa128da9ce6deae100bdf72de51f08453c3aaff9e1b73aaa2441fa7c`  
**Verdict:** the context-path algebra is exact, but Section 1.7 does not prove simultaneous squarefree assembly.  The owner-level theorem remains open.  A single block-monotone context path can be packed at owner level; its immediate palettes necessarily collide at every internal context.

## 1. Algebra which passes

Put

\[
                         d=q-1,qquad s=R-1=c+d.
\]

For adjacent contexts `G_i,G_(i+1)` of size `s` with

\[
 |G_i\cap G_{i+1}|=c,
\]

write

\[
 D_i=G_i\cap G_{i+1},\quad
 A_i=G_i\setminus D_i,\quad
 F_i=G_{i+1}\setminus D_i.                          \tag{1.1}
\]

Then `|A_i|=|F_i|=d`.  On the toggle ground `[k]-D_i`, the two cyclic
orders

\[
 (A_i,x,p,F_i,\omega_i),
 \qquad (A_i,p,x,F_i,\omega_i)                      \tag{1.2}
\]

differ by the adjacent transposition of `x,p`.  Their only changed
`q`-windows are

\[
 A_i+x,\ p+F_i
 \quad\longleftrightarrow\quad
 A_i+p,\ x+F_i.                                    \tag{1.3}
\]

After adjoining `D_i`, this is exactly

\[
 \delta_{xp}(G_i)-\delta_{xp}(G_{i+1}).             \tag{1.4}
\]

Summing (1.4) along a context path telescopes.  The two owners over each
internal context occur once on each shore, and the unchanged windows of
each adjacent-transposition pair give a literal common reserve.  Thus
equations (1.37)--(1.38) of the source are correct **provided** the union
of all selected rail decks is owner-simple.

The exact-distance context graph connectivity argument also passes as an
abstract path-existence statement.  It does not imply that all carousel
decks placed on those paths are mutually disjoint.

## 2. First false counting assertion: the transition core is unique

Section 1.7 lists among the unused choices

> exponentially many choices of `c`-core within a context transition.

For a fixed transition `G_i,G_(i+1)` with intersection size `c`, the core
of any rail realizing (1.3) is forced:

\[
                            D_i=G_i\cap G_{i+1}.      \tag{2.1}
\]

There is exactly one such `c`-core, not exponentially many.  Core freedom
exists only while choosing the context path; it cannot be counted again
when completing the cyclic order of a fixed path edge.

## 3. A polynomial forbidden owner bank can block every local order

The proposed union bound also has the wrong robustness scale.  Give
`A_i` a uniformly random internal order, and fix `a in A_i`.  Define

\[
 K_a=D_i\cup\{x,p\}\cup(A_i\setminus\{a\}).         \tag{3.1}
\]

This is an `R`-owner.  In every order (1.2), the `q`-window ending at
`p` consists of `x,p` and the final `d-1` members of the ordered `A_i`.
Consequently

\[
 \Pr(K_a\text{ is an unchanged owner window})={1\over d}={1\over q-1}.
                                                               \tag{3.2}
\]

More decisively, the forbidden family

\[
                         \mathcal F_A=\{K_a:a\in A_i\}          \tag{3.3}
\]

has only `d=q-1` members, but **every** completion of (1.2) contains
exactly one member of `F_A`: take `a` to be the first member of the
ordered `A_i`.  Thus no theorem saying that a local order can avoid an
arbitrary polynomial forbidden owner family is true for this block form.

The fact that the probability in (3.2) tends to zero is not enough for a
union bound over a polynomial bank.  Dangerous containments must be
removed while choosing the contexts themselves; factorially many filler
orders do not repair them afterwards.

## 4. A rigorous positive result: one block-monotone path packs at owner level

The following is the strongest unconditional packing statement extracted
from the proposed construction.

> **Lemma 4.1 (one-path owner packing).**  Let
> `G_0,...,G_t` be a block-monotone context path: for every `i`,
> `G_(i+1)` is obtained from `G_i` by deleting a block `A_i` of `d`
> points and adding a block `F_i` of `d` points, and all deleted and added
> blocks used at different steps are mutually disjoint.  Let
> `D_i=G_i cap G_(i+1)`.  Assume `d>=2` and every filler set
> \[
> \Omega_i=[k]\setminus(D_i\cup A_i\cup F_i\cup\{x,p\})        \tag{4.1}
> \]
> has at least two points.  Choose a linear order `omega_i` of `Omega_i`,
> write `a_i` for its first and `b_i` for its last point, and impose
> \[
>                              a_i\ne b_{i+1}          \tag{4.2}
> \]
> for `0<=i<t-1`.  Then the aggregate owner supports of all rails with
> orders (1.2) are simple on each shore.  The unchanged decks are also
> mutually disjoint and form a literal common owner reserve.

### Proof

For `j>=i+2`, block monotonicity gives

\[
                         \operatorname{dist}(D_i,D_j)\ge2d>q.   \tag{4.3}
\]

An `R=c+q` owner cannot contain both cores, so nonadjacent rail supports
are disjoint.

For adjacent edges,

\[
                         D_i\cup D_{i+1}=G_{i+1},                \tag{4.4}
\]

which has size `R-1`.  Hence any owner common to the two supports must be
`G_(i+1)+y` for one point `y`.

In rail `i`, a `q`-window containing the whole block `F_i` is one of

\[
                         p+F_i,\qquad F_i+a_i.        \tag{4.5}
\]

The first is the designated changed endpoint and the second is the only
unchanged possibility.  In rail `i+1`, a `q`-window containing the whole
block `A_(i+1)` is one of

\[
                         A_{i+1}+x,qquad b_{i+1}+A_{i+1},        \tag{4.6}
\]

with `x,p` exchanged on the other shore.  Thus the two intended internal
owners are `G_(i+1)+x` and `G_(i+1)+p`, once each on either shore.  The
only possible common-deck collision is

\[
                         G_{i+1}+a_i=G_{i+1}+b_{i+1},            \tag{4.7}
\]

which is excluded by (4.2).  A filler point is never `x` or `p`, so no
common owner collides with an intended endpoint.  This proves the lemma.
`square`

Condition (4.2) can be met greedily because each `Omega_(i+1)` has at
least two points.  The lemma is deliberately only a **one-path owner**
statement.  Residual-distance two-edge bridges and paths belonging to
different commodities need not have the separation (4.3).

## 5. Immediate palettes have a forced internal collision

The source claims that immediate lower and upper palette collisions can
be included in the same greedy avoidance.  For any context path of at
least two edges this is impossible for the literal rails (1.2).

At the seam between edges `i` and `i+1`, the rank-`R-1` ticket

\[
                              G_{i+1}                 \tag{5.1}
\]

occurs in both immediate-lower palettes: it is `D_i+F_i` on rail `i`
and `D_(i+1)+A_(i+1)` on rail `i+1`.  This duplicate is independent of
all orderings of `A,F,omega`.

Likewise, the rank-`R+1` ticket

\[
                              G_{i+1}\cup\{x,p\}      \tag{5.2}
\]

occurs in both immediate-upper palettes: its toggle window is
`x+p+F_i` on rail `i` and `A_(i+1)+x+p` on rail `i+1`.  It too is
forced and switch-invariant.

Therefore the one-path construction cannot simultaneously have a simple
global immediate-lower or immediate-upper palette.  Occurrence copies or
a different compound braid would be needed if those rows require named
set simplicity.

## 6. Exact remaining gate

The proposed common-reserve theorem is not yet unconditional.  A valid
completion must prove all of the following jointly:

1. pair the `q(q-1)` endpoint demands and choose their exact-distance
   context paths so that every dangerous forced owner of the form (3.1)
   is absent from all earlier and exterior decks;
2. handle residual-distance bridges and cross-commodity core clusters,
   where the one-path core separation (4.3) need not hold;
3. choose all filler seam labels so the remaining adjacent common decks
   do not collide; and
4. if literal immediate palettes are compulsory, replace the path lift by
   a gadget which resolves the unavoidable duplicate tickets (5.1)--(5.2).

What is presently proved is the conditional statement:

\[
 \boxed{\text{squarefree protected path lift}
        \Longrightarrow
        \text{owner-level common-reserve factorization}.}
\]

The source proves the algebra to the left of that implication and Lemma
4.1 proves it for one clean block-monotone path at owner level.  It does
not prove the required multicommodity squarefree lift.
