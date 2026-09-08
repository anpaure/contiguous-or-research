# A linear obstruction to pure diagonal intersection-path compression

Date: 2026-07-25

Method: exact mathematics only.

## 0. Scope

This note concerns the proposed replacement of the (2S+1)-vertex
east--south Pareto staircase by a path using unit diagonal steps and the
same kind of letters

\[
 W_{(u,v)}=\bigcap_{i=-u}^{v}X_i.
\]

It proves that this **intersection-path subclass** cannot have length
(S+O(H)), even for (H=1).  There are cyclic Johnson walks for which
any monotone rectangle-intercepting lattice path needs a positive linear
number of repeated first coordinates.  Thus merely replacing east--south
corners by diagonal steps cannot give coefficient one.

The theorem is deliberately narrower than a lower bound for arbitrary
set-valued OR words.  Facet-braid letters which are not intersections
(W_{(u,v)}) are not excluded.

## 1. Circular-run realization of a Johnson walk

Let (N=4g+2), with (g\ge2), and index owner positions by
\(\mathbb Z_N\).  For every \(s\in\mathbb Z_N\), introduce one coordinate
whose positive owner run is the forward circular arc from its start
\(s\) to its end \(e(s)\), inclusive.  If the starts and ends are both
used exactly once, then at every transition exactly one coordinate starts
and exactly one coordinate ends.  The active-coordinate sets therefore
form a cyclic Johnson walk of constant rank.

Specify (2g) of the arcs as follows, for (0\le t<g):

\[
 E_t=[2g-t,,2g-t],
 \tag{1.1}
\]

and

\[
 P_t=[g-t,,2g+1+t].
 \tag{1.2}
\]

Thus the (E_t)'s are singleton runs and the (P_t)'s are long runs.
The used starts are (1,\ldots,2g), and the used ends are
(g+1,\ldots,3g).

Complete the start--end bijection by

* singleton arcs ([s,s]) for (s=3g+1,\ldots,4g+1);
* the singleton arc ([0,0]);
* for (j=0,\ldots,g-1), the wrapping arc starting at
  (2g+1+j) and ending at (j+1).

This uses every start and every end exactly once.  Hence it gives an
exact cyclic Johnson walk (X_0,\ldots,X_{N-1}).  Cutting the circle at
zero decomposes a wrapping arc into the two maximal positive runs
([2g+1+j,N-1]) and ([0,j+1]), as usual.

For a nonwrapping positive run ([\alpha,\beta]), write its run point as

\[
 p=(-\alpha,\beta).
\]

The two distinguished families have points

\[
 e_t=(-2g+t,,2g-t)
 \tag{1.3}
\]

and

\[
 p_t=(-g+t,,2g+1+t).
 \tag{1.4}
\]

Put also

\[
 q_t=(-2g+t,,2g-t+1).
 \tag{1.5}
\]

The point (e_t) has diagonal height zero and (q_t) has diagonal
height one.  Thus the corresponding owner query and two-owner query lie
in the strip \(\alpha+\beta\le1\).

## 2. All the two-owner queries are floor-correct

### Lemma 2.1

For every (t), no maximal positive run point lies strictly southwest of
(q_t).  Consequently the lower query associated with (q_t) is
floor-correct.

#### Proof

For the singleton points (e_s), if (s<t), then

\[
 (e_s)_1<(q_t)_1,
 \qquad
 (e_s)_2\ge (e_{t-1})_2=(q_t)_2,
\]

while if (s\ge t), then ((e_s)_1\ge(q_t)_1).  Thus no (e_s) is
strictly southwest.

Every long point (p_s) has first coordinate at least (-g), whereas
((q_t)_1\le-g-1), so it lies strictly east of (q_t).

Every high singleton filler and every terminal piece of a wrapping arc
has second coordinate at least (3g+1>(q_t)_2).  Every initial piece of
a wrapping arc has first coordinate zero.  The remaining singleton at
zero also has first coordinate zero.  None is strictly southwest.

The internal-run criterion for Johnson walks now gives floor
correctness. \(\square\)

Notice also that

\[
 p_t\ge q_t
 \tag{2.1}
\]

coordinatewise.  Hence the coordinate belonging to (P_t) occurs in the
floor-correct lower target at (q_t).

## 3. Every gadget forces a repeated vertical fibre

Call a lattice path monotone southeast if its first coordinate is
nondecreasing and its second coordinate is nonincreasing.  Say that it
has the required interception property if

\[
 \Gamma\cap[q,p]\ne\varnothing
 \tag{3.1}
\]

whenever (q) is one of the required owner or floor-correct lower query
points and (p) is a run point with (p\ge q).

### Theorem 3.1

Every monotone southeast path with the required interception property
contains, for each (0\le t<g), at least two vertices whose first
coordinate is

\[
 -2g+t.
 \tag{3.2}
\]

One of them is (e_t); another has second coordinate at least
(2g-t+1).

#### Proof

Apply (3.1) first with the owner query (q=p=e_t).  The rectangle is the
singleton ({e_t}), so (e_t\in\Gamma).

Next apply (3.1) with (q=q_t) and (p=p_t), using Lemma 2.1 and
(2.1).  Let (z\in\Gamma\cap[q_t,p_t]).  Then

\[
 z_1\ge(e_t)_1,
 \qquad
 z_2\ge(e_t)_2+1.
 \tag{3.3}
\]

Because the path is southeast and contains (e_t), no vertex occurring
after (e_t) can satisfy the second inequality in (3.3).  No vertex
occurring before the first vertex on the vertical fibre
(u=(e_t)_1) can satisfy the first inequality.  Therefore the path must
contain, before (e_t), a second vertex on that same vertical fibre,
with second coordinate at least ((e_t)_2+1). \(\square\)

### Corollary 3.2

Suppose the path moves from first coordinate (-N) to first coordinate
zero by unit east or unit southeast steps (with arbitrary unit south
steps).  Then it has at least

\[
 N+1+g
 =
 \left(\frac54-o(1)\right)N
 \tag{3.4}
\]

vertices.

#### Proof

The horizontal displacement forces at least one vertex on each of the
(N+1) integer vertical fibres.  Theorem 3.1 forces one additional
vertex on each of (g) distinct fibres.  Since (N=4g+2), (3.4)
follows. \(\square\)

## 4. Consequence for the coefficient-one geometry attack

For letters (W_z=\bigcap_{i=-u}^{v}X_i), exact recovery of a lower
target by the rectangle-interception proof requires (3.1): a coordinate
whose run point is (p\ge q) can enter the OR only through a selected
path vertex in ([q,p]).  Therefore Corollary 3.2 is an exact obstruction
to every proposed compiler which

1. retains the same intersection letters (W_z);
2. replaces the east--south path only by unit east, south, and diagonal
   steps; and
3. uses the same monotone rectangular selection rule.

The obstruction already occurs at depth one, and its excess is linear in
the owner-block length, not (O(H)).

The only possible escape is genuinely set-valued fusion: a letter must
combine or split adjacent facet/pin data in a way that is not itself one
intersection (W_z).  In particular, a proof cannot consist solely of
choosing the diagonal convention more cleverly.

