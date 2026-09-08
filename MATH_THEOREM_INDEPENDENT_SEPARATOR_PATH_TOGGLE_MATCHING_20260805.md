# Independent separator choices on a path have a canonical matching with at most one critical state

**Date:** 2026-08-05  
**Method:** explicit discrete-Morse toggle recursion; no computation or
search  
**Status:** unconditional graph theorem, prepared for the shifted-quiet
necklace exit collision fibres.  Identifying those physical fibres with
independent-set path products remains to be proved.

## 1. The independent-set toggle graph

For a finite graph `H`, let `I(H)` be the graph whose vertices are the
independent sets of `H`; two independent sets are adjacent when their
symmetric difference is one vertex.  This is the literal graph obtained
when a collection of locally legal separator insertions may be toggled one
at a time and two overlapping insertions are incompatible.

Let `P_t` be the path on ordered vertices `1,...,t`.

### Theorem 1.1 (path toggle matching)

The graph `I(P_t)` has an explicit matching with

\[
 \begin{cases}
  0& t\equiv1\pmod3,\\
  1& t\equiv0,2\pmod3
 \end{cases}                                                   \tag{1.1}
\]

unmatched vertices.  In the one-critical cases the critical independent
set is unique under the recursion below.

#### Proof

Pair every independent set `S` not containing vertex `2` by toggling
vertex `1`:

\[
                         S\longleftrightarrow S\triangle\{1\}. \tag{1.2}
\]

This is legal because `2` is absent, and it is an involution.  The only
unpaired sets contain `2`; then independence forces `1,3` to be absent.
Deleting the fixed pattern

\[
                              0,1,0                              \tag{1.3}
\]

identifies the residual toggle graph with `I(P_(t-3))` on vertices
`4,...,t`.  Repeat.

The bases are

\[
 I(P_0)=\{\varnothing\},\qquad
 I(P_1)=\{\varnothing,\{1\}\},\qquad
 I(P_2)=\{\varnothing,\{1\},\{2\}\}.             \tag{1.4}
\]

The first has one critical state, the second is perfectly paired, and the
third leaves `{2}` after pairing `emptyset<->{1}`.  Recursion by three
proves (1.1). `square`

The matching uses only one-site toggles and is therefore a literal matching
inside any physical fibre whose separator compatibility graph is a path.

## 2. Products of independent separator paths

Let

\[
                         H=P_{t_1}\sqcup\cdots\sqcup P_{t_s}.   \tag{2.1}
\]

Then

\[
                         I(H)=I(P_{t_1})\square\cdots\square
                              I(P_{t_s}).                        \tag{2.2}
\]

### Corollary 2.1 (path-forest separator matching)

The product (2.2) is perfectly matched if at least one `t_i` is `1` modulo
three.  Otherwise it has a matching with exactly one critical state, the
tensor of the unique critical states of all factors.

#### Proof

Use the first factor having a perfect matching and extend its matching over
all other coordinates.  If no factor is perfect, take the graded tensor of
the matchings in Theorem 1.1.  Every noncritical tensor is paired in its
first noncritical coordinate; only the tensor of all critical coordinates
remains. `square`

### Corollary 2.2 (odd symmetry quotient)

Suppose an odd-order group acts on the path forest by permuting equal path
components with their order preserved.  The quotient of (2.2) has a
matching of deficiency at most one, and is perfect whenever one invariant
factor block contains a perfect local matching.

#### Proof

Partition each factor `I(P_(t_i))` into the disjoint matching edges of
Theorem 1.1 and its possible singleton critical state.  Their Cartesian
products partition (2.2) into cubes: choose in each coordinate either one
matched edge or the critical singleton.  The group permutes these cubes.
For one orbit of cubes, quotient a representative cube by its odd-order
stabilizer.  If the cube has positive dimension, the odd-group hypercube
quotient theorem gives a perfect matching using literal one-coordinate
toggles.  The only zero-dimensional cube is the tensor of all local
critical states, and it exists only when every factor has one.  Its orbit
contributes one quotient vertex.  This proves the assertion. `square`

This uses the exact odd-group hypercube-quotient theorem on disjoint cells;
it is not the translation-invariant free-fermion operator already known to
cancel on the original necklace quotient.

## 3. Separator-normal-form target

The shifted-quiet exit has the local form

\[
                  (o,2,0)\longleftrightarrow(o,1,1),
                  \qquad o\ \hbox{odd}.                         \tag{3.1}
\]

Different exits collide because deleting one zero merges two macroblocks
and may change which later exits are recognizable.  A sufficient exact
normal-form theorem would be:

1. fully merge every legal shifted-quiet separator to a canonical cyclic
   base `B`;
2. prove every preimage of `B` is obtained by inserting separators at an
   independent set of a canonically determined conflict graph `H_B`;
3. prove `H_B` is a disjoint union of rooted paths (or that its only cycle
   is one explicitly controlled exceptional face); and
4. prove a one-vertex toggle is exactly the adjacent transfer (3.1).

Under these four statements, the fibres partition automatically by the
value of the normalization map, and Corollaries 2.1--2.2 match every fibre
with deficiency at most one.  The sole remaining critical tensors are then
explicit and can be compared with the already recursive all-unit face.

## 4. Scope

Proved here:

1. a canonical literal matching of every independent-set path fibre;
2. exact deficiency zero/one by path length modulo three;
3. tensor and odd-symmetry-quotient extensions; and
4. the precise normal-form statement that would absorb shifted-quiet exit
   collisions.

Not proved here:

1. confluence of the physical separator rewrite (3.1);
2. that its conflict graph is a path forest;
3. absorption of the residual critical tensors;
4. PBBS halo compatibility or a universal-word bound.
