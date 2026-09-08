# MNW q2 rectangle decomposition and a compound cylinder in the standard tree

**Date:** 2026-08-07  
**Method:** exact signed turn algebra and the published recursive MNW spanning
tree; no computation or search  
**Status:** unconditional.  Every overlap correction is one Boolean
rectangle current.  More importantly, the standard MNW tree already
contains a support-disjoint Catalan family of compound centres which create
genuinely missing canonical q2 targets.

## 1. Exact interaction correction at a doubly touched centre

Let an internal canonical rank-`m` centre be `X`, with its two selected
facets

\[
                         X+a,\qquad X+b.              \tag{1.1}
\]

Suppose one selected tuple replaces `X+a` by `X+c`, and a second selected
tuple replaces `X+b` by `X+d`.  Conflict-freeness gives distinct marked
edges; simplicity gives `c != d`.

If each move were evaluated in isolation, their combined signed current at
`X` would be

\[
 [X+\{b,c\}]+[X+\{a,d\}]-2[X+\{a,b\}].              \tag{1.2}
\]

The actual final current is

\[
                         [X+\{c,d\}]-[X+\{a,b\}].    \tag{1.3}
\]

Therefore the exact interaction correction is the rectangle

\[
 \boxed{
 [X+\{c,d\}]+[X+\{a,b\}]
 -[X+\{b,c\}]-[X+\{a,d\}].}                         \tag{1.4}
\]

### Theorem 1.1 (global q2 current decomposition)

For any conflict-free family of MNW tuples, its final signed q2 current is
the sum of the isolated tuple currents plus one correction (1.4) for every
rank-`m` centre whose two incident canonical edges are both selected.

#### Proof

Every lower centre has two incident canonical edges.  With zero changed
edges it contributes zero; with one changed edge its actual current is the
isolated current; with two changed edges the difference between the actual
current and the two isolated currents is exactly (1.4).  Distinct centres
use disjoint pairs of incidences, so summing these exhaustive local cases
proves the theorem. \(\square\)

Thus compound effects are not an uncontrolled nonlinear error.  They are
an explicit square-current bank superposed on the isolated currents.

## 2. The unique compound contact in the standard `F_4` star

Use the standard MNW spanning tree of `H_4[F_4]`.  Two of its tuples are

\[
 \tau_1=\alpha(10),
 \qquad
 \tau_4=\alpha(\varnothing)10.                       \tag{2.1}
\]

They share the root

\[
                         x=11010010.                  \tag{2.2}
\]

The canonical flip order is

\[
                   \pi(x)=(6,4,5,2,3,1,8,7).         \tag{2.3}
\]

At `x`, tuple `tau_4` is marked at coordinate six, hence path-edge position
one; tuple `tau_1` is marked at coordinate four, hence position two.  These
two edges meet at the upper centre

\[
                         U=11010110.                  \tag{2.4}
\]

The canonical lower neighbours of `U` are

\[
 X_0=11010010,
 \qquad
 X_2=11000110.                                       \tag{2.5}
\]

The alpha cycles replace them respectively by

\[
 D=10010110,
 \qquad
 C=11010100.                                         \tag{2.6}
\]

Hence the old and final coturns at `U` are

\[
 X_0\cap X_2=11000010,
 \qquad
 C\cap D=10010100.                                   \tag{2.7}

This contact is around an upper centre, so it is not yet a q2 compound
centre in semilength four.  Mirror closure swaps the incidence shores.

## 3. Mirror closure produces a genuine compound repair

Let

\[
                         F(A)=1\operatorname{revcomp}(A)1.
\]

Mirror-wrap both tuples in (2.1).  The old upper centre `U` becomes the new
lower centre `F(U)`, and (2.7) becomes its old and final q2 turns.  Thus the
actual compound-centre current contains

\[
 [F(10010100)]-[F(11000010)]
 =[1110101101]-[1101111001].                         \tag{3.1}

The positive target

\[
                         H_\gamma=1110101101          \tag{3.2}

is absent from the canonical semilength-five q2 image by the exact inverse
test.  This is the same missing target exposed independently by the isolated
mirror-gamma current.

### Theorem 3.1 (standard compound cylinder)

For every `m>=5` and every Dyck word `v in D_(m-5)`, the published standard
MNW spanning tree `T_m` contains the two tuples

\[
 1\operatorname{revcomp}(\tau_1)0v,
 \qquad
 1\operatorname{revcomp}(\tau_4)0v,                  \tag{3.3}

and their joint action creates the q2 target

\[
                         \boxed{1110101101v}.         \tag{3.4}

Every target in (3.4) is absent from the canonical q2 image.  The centres
and tuple supports for distinct `v` are disjoint.  All these compound offers
therefore coexist in one conflict-free spanning hypertree.

#### Proof

In MNW's induction, the construction of `F_(m,5)` includes

\[
 1\operatorname{revcomp}(F_4)0v
 \qquad\text{for every }v\in D_{m-5}.                \tag{3.5}

The fixed tree on `F_4` contains both tuples (2.1), proving their membership
in the same final spanning tree.  Sections 2--3 compute their compound turn
as (3.2).  Dyck suffixing appends `v` to every local vertex and turn.

The prefix (3.2) ends at height four.  A Dyck suffix read from height four
adds no eligible position to the canonical inverse test, so canonical
absence persists.  Distinct suffixes give distinct roots, centres, and
tuple supports by projection to the suffix coordinates. \(\square\)

The family has cardinality `Cat_(m-5)`.  It is therefore a positive-density
Catalan family of **actual**, not prospective, compound q2 offers already
inside one published Hamiltonization.

## 4. Exact compound capacity in an arbitrary selected hypertree

For a selected hypertree `T`, let `d_x` be the number of selected tuples
containing a Dyck root `x`.  Order their marks by their edge positions on
`P(x)`.  The lower-centred edge pairs are

\[
                         (2,3),(4,5),\ldots,(2m-2,2m-1). \tag{4.1}
\]

They are pairwise disjoint.  Consequently the number `c_x` of compound q2
centres on `P(x)` satisfies

\[
                         c_x\le \left\lfloor d_x/2\right\rfloor. \tag{4.2}
\]

If `I=sum_x d_x=sum_(tau in T)|supp tau|` is the incidence count, then

\[
                    \#\{\text{compound q2 centres}\}
                    \le \frac12 I.                  \tag{4.3}
\]

There is no positive lower bound from degree data alone: all selected marks
may avoid the pairs in (4.1).  Theorem 3.1 is stronger than a capacity
count because it identifies a linearly independent suffix-indexed bank
whose offers are simultaneously present in the standard tree.

## 5. Remaining Hall problem

The former statement "a missing q2 target can only be reached by a compound
centre" is false, because isolated mirror-beta and mirror-gamma tuples are
also support-moving.  The correct global problem is now signed:

1. isolated wrapper currents transport holes;
2. compound centres add the rectangle currents (1.4); and
3. the total selected hypertree current must avoid deleting the last
   provider of any old target.

The standard tree proves coexistence for the complete cylinder (3.4), but
it does not prove full q2 surjectivity.  What remains is a colored
spanning-hypertree theorem selecting isolated and compound currents so that
every negative unit-load occurrence is balanced by another positive term.

