# Coupled toggle insertion makes the two-size rail absorber compact at every width

**Date:** 2026-08-07  
**Status:** unconditional local absorber theorem.  It gives two positive
states with a coherent \(O(d)\) named footprint, but does not prove that an
arbitrary leave can be embedded into that footprint.

## 1. One-cycle insertion identity

Let \(\tau\) be a cyclic order on a set \(T\) of size \(n\), and choose one
directed cut edge \(ab\) of the cycle.  Insert a fresh label \(z\) between
\(a,b\), obtaining a cyclic order \(\tau^z\) on \(T\cup\{z\}\).

For \(1\le\ell<n\), write

\[
 \mathcal I_\ell(\tau),\qquad
 \mathcal I_\ell(\tau^z)
\]

for the two cyclic interval families.

### Lemma 1.1 (exact insertion current)

At width \(\ell\),

\[
 \begin{aligned}
 |\mathcal I_\ell(\tau)\cap\mathcal I_\ell(\tau^z)|&=n-\ell+1,\\
 |\mathcal I_\ell(\tau)\setminus\mathcal I_\ell(\tau^z)|&=\ell-1,\\
 |\mathcal I_\ell(\tau^z)\setminus\mathcal I_\ell(\tau)|&=\ell.
 \end{aligned}
\tag{1.1}
\]

The old-only intervals are exactly the \(\ell-1\) old intervals containing
the cut edge \(ab\).  The new-only intervals are exactly the \(\ell\) new
intervals containing \(z\).

#### Proof

An old interval avoiding the directed edge \(ab\) is unchanged by insertion.
Exactly \(\ell-1\) cyclic \(\ell\)-intervals contain a fixed directed edge,
so the other \(n-\ell+1\) old intervals survive.  In the new cycle exactly
\(\ell\) intervals contain \(z\), and every interval avoiding \(z\) is one of
the surviving old intervals.  This proves all three counts and the stated
description.  \(\square\)

Adjoining a fixed core to every interval preserves the identity literally.

## 2. Coupled form of the positive unit gadget

Use the notation

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c,
\]

and assume \(M-2\ge2(q+1)\).  Choose \(D,x,y,z\) as in the positive
two-size absorber:

\[
 |D|=c-1,\qquad x,y,z\notin D.
\]

Put

\[
 T_0=[k]\setminus(D\cup\{x,y,z\}),
 \qquad |T_0|=M-2=n.
\tag{2.1}
\]

Choose a base cyclic order \(\tau\) of \(T_0\).  For the \(x\)-signature
pair, insert \(z\) at a chosen cut to obtain \(\tau_x^z\); for the
\(y\)-signature pair, insert \(z\) at a (possibly different) chosen cut to
obtain \(\tau_y^z\).

Take the two absorber states

\[
 \begin{array}{c|c|c|c|c}
 &\text{state}&\text{size}&\text{core}&\text{toggle order}\\ \hline
 Q_1^+&+&M-1&D+x&\tau_x^z\\
 Q_2^+&+&M-2&D+y&\tau\\
 Q_1^-&-&M-1&D+y&\tau_y^z\\
 Q_2^-&-&M-2&D+x&\tau.
 \end{array}
\tag{2.2}
\]

The omitted coordinates are forced by the displayed core and toggle set.

### Theorem 2.1 (compact coherent unit absorber)

At every common proper width

\[
 1\le\ell<M-2,
\]

the following hold.

1. Each state is a matching on its width-\(\ell\) target shore: its two
   component decks are disjoint by the signatures \(x\bar y\) and
   \(\bar x y\).
2. The two states have the same cardinality \(2M-3\).
3. Their coordinate-incidence difference is

   \[
   \boxed{
   \omega^+_\ell-\omega^-_\ell=e_x-e_y.}
   \tag{2.3}
   \]

4. Their width-\(\ell\) decks have a common part of size

   \[
   2(M-\ell-1),
   \tag{2.4}
   \]

   and exactly

   \[
   \boxed{2\ell-1}
   \tag{2.5}
   \]

   exclusive named values on each side.

In particular, at the owner width \(q=d+1\), the two positive
decompositions differ on exactly

\[
 \boxed{2q-1=2d+1}
\tag{2.6}
\]

owners per side.  At every lower or upper width, the footprint is the same
pair of triangular left/right extension cones and grows only linearly with
that width.

#### Proof

Items 1--3 are the positive two-size unit-residue theorem.  Compare the two
components with core \(D+x\): the plus component is obtained from the minus
component by inserting \(z\) into its toggle cycle.  Lemma 1.1 gives
\(n-\ell+1=M-\ell-1\) common values, \(\ell\) plus-only values, and
\(\ell-1\) minus-only values.

For core \(D+y\), the roles are reversed.  It contributes the same common
count, \(\ell-1\) plus-only values, and \(\ell\) minus-only values.  The two
core signatures are disjoint, so the counts add without collision.  This
gives (2.4)--(2.5).  \(\square\)

## 3. Explicit port geometry

For each signature, the shorter-state exclusive values are the old intervals
crossing one cut edge; the longer-state exclusive values are the new
intervals containing \(z\).  As the width grows, each port has two possible
one-label extensions.  Consequently the cross-width object is a triangular
two-child extension cone, not one literal inclusion chain.

At the owner width, one state has \(q\) ports containing \(z\) on the
\(x\bar y\) shore and \(q-1\) cut-crossing ports on the \(\bar x y\) shore;
the other state has the opposite allocation.  This is an occurrence-labelled
positive version of the birail unit current.

The two insertion cuts may be selected independently.  Their choice is the
remaining routing freedom for embedding a prescribed leave.

## 4. What this closes and what remains

The uncoupled positive lattice gadget had \(2M-3=\Theta(k)\) values per
state at each width but did not identify a large common reserve.  Theorem
2.1 sharpens it to

\[
 \boxed{
 \text{common reserve of size }2(M-\ell-1)
 \quad+\quad
 (2\ell-1)\text{ switch ports per state}.}
\]

Thus one unit coordinate residue can be absorbed by changing only \(O(d)\)
owners and \(O(j)\) tickets at source width \(j\), while all other values are
literally common to both positive decompositions.  The footprint is \(O(d)\)
on the owner and bounded-offset rows; it grows to \(O(j)\), not \(O(d)\), on
arbitrary long widths.

The remaining global lemma is a port-embedding statement:

> Given a small named owner/lower/upper leave satisfying the full lattice,
> find disjoint choices of \(D,x,y,z\), base orders, and insertion cuts so
> that the leave occupies the exclusive rays of a collection of compact
> unit absorbers and every non-leave exclusive port is paired internally.

This theorem does not prove that statement, common-cap feasibility, or
\(\nu(k)\le B(k)+O(1)\).
