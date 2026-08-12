# Rotor rigidity of a prescribed Johnson cycle

Date: 2026-07-25

## 0. Result

Let

\[
X_{i+1}=X_i-r_i+a_i
\]

be a directed Johnson cycle (or path) on one fixed rank.  Suppose its
outgoing first lower facet at (X_i) is frozen to

\[
L_1(X_i)=X_i\cap X_{i+1}=X_i-r_i.
\]

There is essentially no freedom left in a radius-(H) rotor run.  Away
from its terminal boundary, rotor compatibility forces

\[
d_t(X_i)=r_{i+t-1},\qquad
L_q(X_i)=\bigcap_{j=0}^{q}X_{i+j}.
\]

Consequently, rechoosing the deeper paths in the abstract balanced-flow
extension cannot make a prescribed saturating Johnson cycle physical
unless its actual consecutive-intersection shadows are already close to
the desired loads.

The local physical obstruction has an exact description.  A coordinate
which is added at transition (u) and next removed at transition (v)
has **short residence** when the cyclic gap (v-u) is at most (H).
A collection of deleted cycle edges supports radius-(H) rotor runs on all
remaining components if and only if the deleted edges hit every such
short-residence interval.  Thus the least possible number of runs on a
prescribed cycle is the circular-interval transversal number, with the
usual one cut needed to linearize an otherwise compatible cycle.

This also settles the deletion-signature question for this route.  The
formal words

\[
(r_i,r_{i+1},\ldots,r_{i+H-1})
\]

have **exactly zero** prefix/suffix signature imbalance on every cycle.
They can nevertheless fail the lower-core support condition.  Hence the
small signature space is not the missing theorem for a saturating-cycle
lift: the obstruction is support/residence, followed by the actual
multidepth shadow loads.

## 1. State convention

A radius-(H) useful state above a middle owner (X) begins

\[
(L;z_1,\ldots,z_{2H};R),
\]

where

\[
X=L\cup\{z_1,\ldots,z_H\},
\qquad |L|=|R|=m-H.
\]

Its ordered lower deletion word is

\[
d_t(X)=z_{H+1-t}\qquad(1\le t\le H),
\]

so

\[
L_q(X)=X\setminus\{d_1(X),\ldots,d_q(X)\}.
\]

For an owner-changing rotor edge (X\to Y=X-r+a), the standard
move-to-front calculation gives

\[
d_1(X)=r,
\]

and

\[
d(Y)=(d_2(X),\ldots,d_H(X),x)
\tag{1.1}
\]

for some

\[
x\in L_H(X).
\tag{1.2}
\]

The entering coordinate (a\notin X) may lie either in the active upper
singleton queue or in the tail.  That choice changes the upper word but
does not change (1.1)--(1.2).

## 2. Forced consecutive intersections

### Theorem 2.1 (run rigidity)

Let

\[
X_s,X_{s+1},\ldots,X_t
\]

be one radius-(H) rotor run, and suppose every retained transition is the
prescribed Johnson transition

\[
X_{i+1}=X_i-r_i+a_i.
\]

Then, whenever (i+q\le t) and (q\le H),

\[
\boxed{
d_j(X_i)=r_{i+j-1}\quad(1\le j\le q),
}
\tag{2.1}

and

\[
\boxed{
L_q(X_i)
=X_i\setminus\{r_i,\ldots,r_{i+q-1}\}
=\bigcap_{j=0}^{q}X_{i+j}.
}
\tag{2.2}

In particular the displayed removals are distinct elements of (X_i).

#### Proof

The owner change on transition (i) forces (d_1(X_i)=r_i).  Applying
(1.1) successively gives

\[
d_j(X_i)=d_{j-1}(X_{i+1})=\cdots=d_1(X_{i+j-1})=r_{i+j-1}.
\]

These are entries of a deletion word and hence are distinct members of
(X_i), proving the first expression in (2.2).  During the next (q)
transitions exactly those (q) original coordinates leave (X_i); every
entering coordinate was absent from (X_i).  Their common intersection is
therefore the same set.  \(\square\)

There is one further forced coordinate at a nonterminal edge.  If
(i+H\le t-1), then (1.1) at edge (i), followed through the next
(H) states, gives

\[
x=r_{i+H}\in L_H(X_i).
\tag{2.3}

This is exactly the residence condition which is invisible in the mere
de-Bruijn overlap (2.1).

### Corollary 2.2 (only boundary owners can use the abstract freedom)

Suppose the vertices of a directed Johnson cycle are split into (J)
rotor runs, with the prescribed first facets on every retained edge.  For
each (q\le H), all but at most (qJ) owners have their depth-(q)
lower target forced to be their (q)-fold consecutive intersection.

#### Proof

In each run only its final (q) owners can fail to have (q) retained
outgoing transitions.  Apply Theorem 2.1 to every other owner.  \(\square\)

This has a useful quantitative consequence.  Let (b_q) be any desired
depth-(q) load vector, and let (mu_q) be the load vector of the chosen
flag table.  Complete the consecutive-intersection map arbitrarily on the
at most (qJ) boundary owners and call its load vector (kappa_q).  Then

\[
\boxed{\|\kappa_q-\mu_q\|_1\le 2qJ.}
\tag{2.4}
\]

In particular, if (mu_q=b_q), then

\[
\boxed{
J\ge {1\over 2q}\|\kappa_q-b_q\|_1.
}
\tag{2.5}

If (b_q) is allowed to range over balanced floor/ceiling vectors, the
right side is the balanced overload of the boundary-completed canonical
shadow divided by (q).  Thus one badly unbalanced canonical shadow rules
out a low-run lift even though an unrelated balanced flow extension exists.

## 3. Exact short-residence transversal

Work cyclically, with transition indices in \(\mathbb Z/L\mathbb Z\).
For every coordinate and every one of its membership runs, let (u) be the
transition at which it is added and (v) the transition at which it is
next removed.  Its residence length is the positive cyclic gap

\[
\ell=v-u.
\]

When \(\ell\le H\), associate the circular interval of transition edges

\[
I(u,v)=\{u,u+1,\ldots,v\}.
\tag{3.1}

Let \(\mathcal I_H\) be the family of all these intervals, and let

\[
\tau_H=\min\{|C|:C\subseteq\mathbb Z/L\mathbb Z,
                 C\cap I\ne\varnothing\text{ for every }I\in\mathcal I_H\}.
\tag{3.2}

### Theorem 3.1 (exact prescribed-cycle rotor deficit)

Assume (H\le m/2).  The least number of radius-(H) rotor runs whose
owner order is obtained by deleting edges of the prescribed Johnson cycle
is

\[
\boxed{J_H^{\rm cyc}=\max\{1,\tau_H\}.}
\tag{3.3}

The deeper lower flags and compatible upper flags may be chosen freely;
only the first lower facets and the retained owner transitions are fixed.

#### Necessity

Suppose a run contains both transition (u), which adds a coordinate
(a_u), and its next removal transition (v), with (v-u\le H).  On
entering (X_{u+1}), the coordinate (a_u) lies in the new lower core.
At one rotor update at most one lower-core coordinate is moved to the last
position of the length-(H) deletion queue.  It then needs (H) shifts
before it becomes the first deletion.  Therefore it cannot be removed in
any of the next (H) retained transitions.  Equivalently, (2.3) would
force a coordinate absent from (X_u) to belong to (L_H(X_u)).

Thus every short-residence interval contains a deleted cycle edge.  A
cycle also needs at least one deleted edge to become a linear run, proving

\[
J\ge\max\{1,\tau_H\}.
\]

#### Sufficiency

Choose a hitting set (C) and consider one resulting path component.
No coordinate is both added and removed inside this component at cyclic
distance at most (H).

Extend the component by (H) dummy transitions at its terminal end.  Pick
(H) distinct removal coordinates from the intersection of its final
(H+1) (or all, if fewer) actual owner sets.  This intersection has size
at least (m-H\ge H).  Pick (H) distinct entering coordinates from the
complement of the terminal owner, and never remove them in the extension.
The dummy removals were present throughout the relevant actual suffix, and
the dummy additions are new, so the extended transition sequence has no
residence of length at most (H).

For every actual owner (X_i) define

\[
d(X_i)=(r_i,r_{i+1},\ldots,r_{i+H-1})
\tag{3.4}

using the dummy removals past the terminal end.  The absence of short
residence says exactly that these are (H) distinct elements of (X_i).
Equations (1.1)--(1.2) now hold at every actual retained edge.

Initialize the first full state by taking the reverse of (3.4) as its
first (H) singleton blocks, choose any further (H) singleton blocks
from the complement of its owner, and put the remaining coordinates in
the tail.  At a retained transition, the entering coordinate is outside
the current owner and hence lies either in those active upper singleton
blocks or in the tail.  The move-to-front update produces the next lower
word in (3.4); it also preserves a length-(H) upper singleton prefix.
Induction gives genuine full radius-(H) states on the whole component.

Doing this independently on every component proves the upper bound in
(3.3).  \(\square\)

Theorem 3.1 is algorithmic.  The family \(\mathcal I_H\) consists of
circular intervals, so its minimum hitting number can be found by trying
one cut in a chosen interval and then applying the ordinary greedy
right-endpoint algorithm on the opened line.

## 4. Prefix/suffix signatures vanish formally but do not certify support

For the cycle, form the formal word

\[
w_i=(r_i,r_{i+1},\ldots,r_{i+H-1}).
\tag{4.1}

Its prefix signature is

\[
p_i=(r_i,\ldots,r_{i+H-2}),
\]

and its suffix signature is

\[
s_i=(r_{i+1},\ldots,r_{i+H-1})=p_{i+1}.
\]

Therefore, as multisets,

\[
\boxed{\{p_i:i\in\mathbb Z/L\mathbb Z\}
      =\{s_i:i\in\mathbb Z/L\mathbb Z\},}
\tag{4.2}

and the sequence imbalance is exactly zero.

The words (4.1) need not be supported by their owners.  A concrete example
already occurs in (J(7,3)) at (H=2):

\[
\begin{array}{c|c|c}
i&X_i&r_i\\ \hline
0&123&1\\
1&234&2\\
2&345&4\\
3&356&3\\
4&567&5\\
5&167&6\\
6&127&7
\end{array}
\]

with (X_7=X_0).  The entering coordinates are

\[
(4,5,6,7,1,2,3).
\]

The seven lower colors are

\[
23,34,35,56,67,17,12,
\]

so the cycle is lower-rainbow.  Every formal two-letter word
((r_i,r_{i+1})) is individually supported by (X_i), and (4.2) holds
exactly.  Nevertheless edge (X_0\to X_1) is not radius-two compatible:
the required new tail deletion is (r_2=4), while

\[
L_2(X_0)=X_0\setminus\{r_0,r_1\}=\{3\}.
\]

The coordinate (4) was added at transition (0) and removed at
transition (2).  Cutting any edge of the interval \(\{0,1,2\}\) repairs
this local obstruction, exactly as Theorem 3.1 predicts.

For arbitrarily large countermodels, take disjoint six-coordinate blocks
and in each block use the rank-three cycle

\[
123,234,345,356,156,126,123.
\]

Fixing all other block states gives disjoint lower-rainbow six-cycles in
the product rank.  Their union has zero prefix/suffix imbalance in every
component but one necessary run per six owners.  Hence even exact signature
balance does not imply a sublinear rotor path cover.

## 5. Consequence for the saturating-cycle core

Let the saturating-cycle theorem supply the lower-rainbow cycle on its
(N_1) core owners, and freeze its depth-one bijection.  The exact abstract
balanced extension of that bijection remains useful for marginal coverage,
but it has no chronological freedom on the interior of a putative rotor
run:

* its lower paths are forced to be the consecutive intersections in
  Theorem 2.1;
* its run count is at least the short-residence transversal in Theorem 3.1;
* at every depth (q), a (J)-run alignment can alter the canonical
  consecutive shadow on at most (qJ) owners.

Therefore the positive theorem still needed in this lane can be stated
sharply: choose a saturating (or merely depth-one balanced) Johnson cycle
whose short-residence transversal is (o(W/H)) **and** whose canonical
depth-(q) shadows can be completed to the desired quotas by changing only
(o(W)) owners at every fixed (q\le H).  The first condition is a genuine
long-residence refinement of the saturating-cycle theorem; it is not a
prefix/suffix balancing problem.

