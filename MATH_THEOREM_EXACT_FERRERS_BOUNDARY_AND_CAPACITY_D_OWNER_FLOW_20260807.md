# The Ferrers boundary admits an exact capacity-\(d\) containment flow

**Date:** 2026-08-07  
**Status:** unconditional integral theorem.  It closes ordinary containment
Hall with the exact boundary rank profile.  It does not make the targets
assigned to one owner into a nested physical suffix flag.

## 1. Setup

Fix \(k\) and a middle rank \(R\).  Put

\[
 W={k\choose R},
 \qquad
 \Lambda=\sum_{s=1}^{R-1}{k\choose s}.
\tag{1.1}
\]

Let \(d\) be a nonnegative integer.  For every \(1\le s<R\), prescribe an
integer boundary multiplicity

\[
 0\le b_s\le{k\choose s},
\tag{1.2}
\]

and assume

\[
 \boxed{
 \sum_{s=1}^{R-1}\left({k\choose s}-b_s\right)\le dW.}
\tag{1.3}
\]

The optimal triangular Ferrers boundary is the intended example.

## 2. Exact integral assignment

### Theorem 2.1

There exist:

1. a boundary family \(\mathcal B_s\subseteq{[k]\choose s}\) of exactly
   \(b_s\) distinct targets at every rank \(s\);
2. an assignment of every target in

   \[
   \bigcup_{s=1}^{R-1}
   \left({[k]\choose s}\setminus\mathcal B_s\right)
   \]

   to a containing rank-\(R\) owner;

such that no owner receives more than \(d\) targets.

Equivalently, the residual lower ideal has a containment matching into \(d\)
labelled copies of every owner, while the boundary uses exactly the prescribed
rank profile.

#### Proof

If (d=0), condition (1.3) forces (b_s=\binom{k}{s}) for every
(s<R).  Take every lower target into the boundary; there is no residual
owner assignment.  Hence assume (d\ge1) below.

Create a bipartite network.  Its left vertices are all strict-lower targets.
Its right vertices are:

* \(b_s\) boundary slots of type \(s\), each adjacent to every rank-\(s\)
  target;
* \(d\) labelled slots \((T,i)\) for every owner
  \(T\in{[k]\choose R}\), where a target \(S\) is adjacent exactly when
  \(S\subset T\).

All right capacities are one.  Require every left vertex and every boundary
slot to be saturated.

We first give a fractional feasible flow.  Write

\[
 C_s={k\choose s},
 \qquad
 A_s={k-s\choose R-s}.
\]

A rank-\(s\) target sends \(1/C_s\) to each of its \(b_s\) boundary slots.
It sends the remaining mass uniformly to the \(dA_s\) labelled owner slots
that contain it; thus each such edge receives

\[
 \frac{1-b_s/C_s}{dA_s}.
\tag{2.1}
\]

Every target sends total mass one, and every boundary slot receives
\(C_s(1/C_s)=1\).

Fix one labelled owner slot \((T,i)\).  Its incoming load is

\[
 \begin{aligned}
 \sum_{s=1}^{R-1}
 {R\choose s}
 \frac{1-b_s/C_s}{dA_s}
 &=
 \frac1{dW}
 \sum_{s=1}^{R-1}(C_s-b_s)\\
 &\le1.
 \end{aligned}
\tag{2.2}
\]

Here we used the exact identity

\[
 C_sA_s=W{R\choose s}.
\tag{2.3}
\]

Therefore the required bipartite flow with integer lower and upper
capacities is fractionally feasible.  The node-edge incidence matrix of a
bipartite network is totally unimodular, so the feasible flow polytope has
an integral point.  At such a point every target chooses one right slot,
every prescribed boundary slot is used once, and every owner uses at most
its \(d\) slots.  This is the desired assignment.  \(\square\)

### Corollary 2.2 (optimal triangular boundary)

Let \(d=d(k)\) be the deadline in the lower-bound formula and choose Ferrers
column counts \(b_s\) with

\[
 \sum_s b_s=(\Lambda-dW)_+.
\]

Then

\[
 \sum_s\left({k\choose s}-b_s\right)\le dW,
\]

so Theorem 2.1 gives an exact rank-profiled boundary and an exact
capacity-\(d\) residual containment assignment.

No \(d+1\)-st ideal owner slot is needed.

## 3. Exact boundary of the remaining lower problem

The theorem closes all lower obstructions that depend only on:

* rank totals;
* ordinary containment Hall cuts;
* the exact Ferrers boundary multiplicities;
* or the number \(d\) of available suffix slots per owner.

The surviving condition is strictly stronger.  If one owner receives
targets

\[
 S_1,\ldots,S_t,\qquad t\le d,
\]

then a literal trace requires them, after ordering, to be one nested flag

\[
 S_1\subset S_2\subset\cdots\subset S_t\subset T,
\]

with age classes compatible across consecutive owners of the same carousel.
The integral flow above does not enforce comparability or cross-owner
regeneration.

Thus the lower-side continuation is now precisely a **conditioned nested
flag flow**, not a capacity or containment matching problem.
