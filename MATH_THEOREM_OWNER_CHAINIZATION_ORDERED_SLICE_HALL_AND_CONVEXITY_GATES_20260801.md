# Owner chainization is an ordered-slice Hall problem

Date: 2026-08-01  
Status: unconditional exact reduction, conditional laminar/convex positive
theorems, and scoped obstructions.  This note does **not** prove an
all-dimension depth-`D` chain factor for the complete Boolean lower ideal.

## 0. Verdict

Let

\[
 r=\lceil k/2\rceil,
 \qquad {\cal L}=\{S\subseteq[k]:1\le |S|<r\},
 \qquad {\cal O}=\binom{[k]}r .
\]

A depth-`D` anchored chain factor is exactly the same object as an ordered
partition

\[
                 {\cal L}=A_1\mathbin{\dot\cup}\cdots
                    \mathbin{\dot\cup}A_D                  \tag{0.1}
\]

together with `D` ordinary containment matchings

\[
 A_i\longrightarrow A_{i+1}\quad(1\le i<D),
 \qquad A_D\longrightarrow{\cal O},                         \tag{0.2}
\]

each saturating its left shore.  Thus, once the common time slices are
chosen, ordinary Hall is complete and there is no further cross-row
integrality gate.  The unresolved correlation is precisely the choice of
the one ordered partition (0.1).

Laminar successor rows reduce to laminar Hall cuts; interval-convex rows
reduce to interval cuts; Ferrers rows are solved by the antitone greedy
matching.  These are genuine positive faces, but the raw Boolean rank
incidence is not interval-convex already from rank one to rank two on four
coordinates.  Moreover any cover-edge/adjacent-rank chronology forces
depth at least `r-1`, so symmetric-chain and normalized-adjacent-matching
machinery cannot by itself reach

\[
 D=\left\lceil |{\cal L}|/|{\cal O}|\right\rceil
   =\Theta(\sqrt{k}).                                          \tag{0.3}
\]

The full Boolean depth-`D` question therefore remains an integral,
rank-jumping slice-selection problem.  Neither the ideal slot theorem nor
the exact fractional owner-chain theorem settles it.

## 1. Exact ordered-slice equivalence

An **anchored chain factor of depth `D`** is a family

\[
                       (C_T:T\in{\cal O})                     \tag{1.1}
\]

such that the nonempty `C_T` partition `L`, every `C_T` is a strict
inclusion chain of at most `D` targets, and every member of `C_T` is
contained in `T`.  Empty owner chains are allowed.

### Theorem 1.1 (ordered-slice Hall normal form)

A depth-`D` anchored chain factor exists if and only if there is an ordered
partition (0.1) and injections

\[
 f_i:A_i\hookrightarrow A_{i+1}\quad(1\le i<D),
 \qquad f_D:A_D\hookrightarrow{\cal O},                       \tag{1.2}
\]

such that

\[
 S\subsetneq f_i(S)\quad(i<D),
 \qquad S\subsetneq f_D(S).                                  \tag{1.3}
\]

For a fixed ordered partition, existence is therefore equivalent to the
independent Hall rows

\[
 |N_{A_{i+1}}(X)|\ge |X|quad(X\subseteq A_i),
 \qquad
 |N_{\cal O}(X)|\ge |X|\quad(X\subseteq A_D).                 \tag{1.4}
\]

#### Proof

Given (1.1), write a nonempty owner chain as

\[
 S_1^T\subsetneq\cdots\subsetneq S_q^T\subsetneq T,
 \qquad q\le D.
\]

Right-align it in the `D` target slices: put `S_j^T` in
`A_(D-q+j)`.  Map each member to the next member of its owner chain and map
the last member to `T`.  Disjointness of the owner chains makes all these
maps injective.

Conversely, take the union of the maps in (1.2).  Every target has exactly
one outgoing arc and every target or owner has at most one incoming arc.
Slice indices strictly increase, so there is no directed cycle.  Every
component is consequently a directed path which ends at a distinct owner.
The path contains at most one target from each of the `D` slices, hence at
most `D` targets.  Transitivity of inclusion puts every target on the path
inside its terminal owner.  The paths give (1.1).  Finally, (1.4) is Hall's
theorem applied separately to the graphs in (1.2).  The separate choices
do not conflict: a target's use as a right mate in row `i-1` and as a left
vertex in row `i` is exactly its role as an internal path vertex.  \(\square\)

This equivalence is also the clean boundary between static chainization
and physical serialization.  It chooses target times and owner-ended
paths, but it does not impose the inter-owner countdown law of one OR
word.

## 2. Laminar and convex rows

Fix one row with left shore `X`, right shore `Y`, and successor
neighbourhoods `N(x) subseteq Y`.

### Lemma 2.1 (laminar row)

Suppose the distinct neighbourhoods belong to a laminar family `F` on
`Y`.  Then `X` has an SDR in `Y` if and only if

\[
 \bigl|\{x\in X:N(x)\subseteq J\}\bigr|\le |J|
                       \qquad(J\in{\cal F}).                  \tag{2.1}
\]

#### Proof

Necessity is immediate.  For sufficiency, process the inclusion forest of
`F` bottom-up.  At a node `J`, its proper maximal children are disjoint.
They have already accommodated every item whose neighbourhood lies in a
child.  Inequality (2.1) leaves enough unused points of `J` for the items
whose smallest neighbourhood node is `J`.  Continuing to the roots gives
an SDR.  \(\square\)

### Lemma 2.2 (interval and Ferrers rows)

Suppose `Y` is linearly ordered and every `N(x)` is an interval.  Then an
SDR exists if and only if

\[
 \bigl|\{x:N(x)\subseteq J\}\bigr|\le |J|                    \tag{2.2}
\]

for every interval `J` of `Y`.

Indeed, if Hall fails, take a violating family of intervals and split its
union into interval components.  One component contains more of the
chosen intervals than points, yielding (2.2).  The converse is necessary.

In the Ferrers special case `N(x)=[a(x),|Y|]`, it is enough to check the
suffixes:

\[
        |\{x:a(x)\ge j\}|\le |Y|-j+1.                         \tag{2.3}
\]

Sorting by decreasing `a(x)` and taking the latest still-free point gives
the matching.  Equivalently, every concordance-removing `2x2` exchange
moves toward the antitone greedy state.

Applying Lemma 2.1 or 2.2 independently in all `D` rows of Theorem 1.1 is
an exact integral chainization theorem.  Thus a laminar/convex chronology
is sufficient; it is not merely a fractional relaxation.

## 3. Raw Boolean incidence is not one convex row

### Proposition 3.1 (the `K_4` consecutive-ones obstruction)

For `k>=4`, there is no ordering of the two-sets in which the collection
of two-set supersets of every singleton is an interval.

#### Proof

Restrict to singletons `1,2,3,4`.  The neighbourhoods

\[
 N(i)=\{\{i,j\}:j\ne i\}
\]

have pairwise nonempty intersections, with

\[
                         N(i)\cap N(j)=\{\{i,j\}\}.            \tag{3.1}
\]

If the four neighbourhoods were intervals in one order, pairwise
intersection and the Helly property for intervals would give a common
point.  That point would be one two-set belonging to all four singleton
stars, which is impossible.  \(\square\)

This rules out a single global interval/Ferrers ordering of the complete
rank-one-to-rank-two incidence.  It does not rule out an adaptively chosen
slice partition which splits those ranks among different rows.

## 4. Cover edges and untouched SCDs are too deep

### Proposition 4.1 (rank-jump necessity)

If every selected target-successor arc is a Boolean cover relation, then
every chain containing a singleton has `r-1` lower targets before reaching
its rank-`r` owner.  Hence every such factor has maximum depth at least
`r-1`.

#### Proof

A cover step raises rank by exactly one.  Starting at rank one and ending
at a rank-`r` owner therefore visits target ranks
`1,2,...,r-1`.  All singletons are targets, so at least one such chain is
present.  \(\square\)

Thus normalized matchings between adjacent ranks, even when they are all
integral and compatible, produce the wrong depth whenever `D<r-1`.
Coefficient-one depth requires genuine rank jumps and cross-chain
rephasing.

There are two quantitative versions of the same warning for even
`k=2m`.  Put

\[
 W=\binom{2m}m,
 \qquad b_j=\binom{2m}{m-j}.
\]

The local central limit estimate is

\[
 b_{\lfloor x\sqrt m\rfloor}/W=e^{-x^2}+o(1),
 \qquad
 D=\left(\int_0^\infty e^{-x^2}\,dx+o(1)\right)\sqrt m.       \tag{4.1}
\]

If whole consecutive ranks are put into capacity-`W` slices, let
`a=sqrt(log 2)`.  Each of the `(a+o(1))sqrt(m)` ranks with `b_j>W/2`
needs its own slice.  Only the last such slice can meet the remaining
rank tail, whose mass is

\[
 \left(\int_a^\infty e^{-x^2}\,dx+o(1)\right)W\sqrt m.
\]

Consequently the number of slices is at least

\[
 \left(a+\int_a^\infty e^{-x^2}\,dx+o(1)\right)\sqrt m
 =D+\left(a-\int_0^a e^{-x^2}\,dx+o(1)\right)\sqrt m,         \tag{4.2}
\]

and the last coefficient is positive.  Whole-rank batching therefore
loses `Theta(sqrt(k))`, not `O(1)`.

Likewise, simply cutting the lower halves of a symmetric chain
decomposition into blocks of length `D` creates too many paths.  There are
`b_1` original nonempty lower chains, and every chain starting below rank
`m-D` creates at least one additional fragment.  Their number telescopes
to `b_(D+1)`.  Since

\[
 b_{D+1}/W=e^{-\pi/4}+o(1),
 \qquad W-b_1=W/(m+1)=o(W),                                  \tag{4.3}
\]

the cut family has at least `(e^(-pi/4)-o(1))W` more fragments than the
available empty middle-owner slots.  Any successful SCD route must splice
fragments across different original chains.

## 5. An unconditional but nonuniform owner-chain factor

### Proposition 5.1 (SCD baseline)

For every `k`, the complete strict lower ideal has an integral anchored
chain factor of depth at most `r-1`.

#### Proof

Take a symmetric chain decomposition of `2^[k]` and restrict every chain
to its nonempty members of rank below `r`.  Every nonempty restricted
chain ends in a distinct rank-`(r-1)` set, and every rank-`(r-1)` set is
the maximum of exactly one such chain.  The maximum possible number of
retained targets is `r-1`.

Match these maxima into distinct rank-`r` owners.  In the containment
graph, a left vertex has degree `k-r+1` and a right vertex has degree `r`.
Because `r=ceil(k/2)`, the left degree is at least the right degree.  For
every left family `F`, edge counting gives

\[
 (k-r+1)|F|\le r|N(F)|,
\]

and hence Hall.  Assign each restricted SCD chain to the owner matched to
its maximum; transitivity gives owner containment.  Unmatched owners are
empty.  \(\square\)

This proves integral existence, but at linear rather than square-root
depth.

## 6. Ordinary slot Hall cannot be uncrossed in general

The following smallest example explains why Theorem 1.1 needs a shared
level choice rather than only owner-slot Hall.

Take the four Boolean targets

\[
 \{1\}\subset\{1,2\}\subset\{1,2,3\},
 \qquad \{4\},                                                \tag{6.1}
\]

and two depth-two owners

\[
 T_1=\{1,2,3,4,5\},
 \qquad T_2=\{1,2,3,4,6\}.                                   \tag{6.2}
\]

If desired, view these sets inside `[10]`; then the two owners have the
central rank `r=5`.  This remains a selected subinstance, not the complete
rank-five owner layer.

Every target is contained in both owners.  Thus the ordinary graph to the
four labelled owner slots is complete and has a perfect matching.  The
target poset has width two, total size four equals total capacity, and all
Greene--Kleitman/strong-Sperner capacity inequalities hold.

Nevertheless no two owner chains of length at most two cover (6.1).
The target `{4}` is incomparable with all three members of the displayed
three-chain, so it consumes one owner chain by itself; the other owner
would have to contain all three remaining targets.

This is a literal set-containment counterexample to a **general**
slot-to-chain uncrossing theorem.  It is not a counterexample for the
complete Boolean lower ideal: the omitted targets and owners may provide
cross-chain exchanges.  Likewise, cyclic filtered catalogues can have
Smith/parity obstructions even when every separate rank projection is
fractionally exact.  A positive complete-ideal theorem must use the full
Boolean exchange supply, not only scalar capacity, normalized matching,
or separate owner Hall.

## 7. Proof-safe frontier

Combining the ideal containment SDR and the symmetric fractional
owner-chain factor with this note gives the following exact hierarchy:

\[
\begin{array}{c}
\text{depth }D\le d+1\text{ independent owner slots}\quad\checkmark\\
\text{depth }D\le d+1\text{ fractional owner chains}\quad\checkmark\\
\text{one ordered slice partition satisfying all }D
   \text{ Hall rows}\quad ?\\
\text{one physical countdown chronology and upper/common cap}\quad ?
\end{array}                                                    \tag{7.1}
\]

The weakest exact additional static hypothesis is the existence of the
ordered slices in Theorem 1.1.  A laminar or interval-convex successor
structure proves their Hall rows integrally, but raw ranks do not have
that structure.  The complete-Boolean depth-`D` existence problem remains
open; no `d+O(1)` claim follows from the present uncrossing tools.
