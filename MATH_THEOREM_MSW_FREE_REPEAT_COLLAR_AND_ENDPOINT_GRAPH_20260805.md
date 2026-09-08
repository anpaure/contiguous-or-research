# Free-repeat balanced collars and the canonical MSW endpoint graph

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, finite search, or solver  
**Status:** unconditional local collar theorem, exact endpoint
characterization, and a uniform non-isolation theorem.  The global
orientation/matching/spanning-path selection remains open.

## 0. Outcome

The original balanced collar chose its repeated left seam to be a second
copy of the first stem colour.  That specialization is unnecessary.

Let

\[
 M_j=Q\cup\{\lambda_{j+1},\ldots,\lambda_h\}
       \cup\{\rho_1,\ldots,\rho_j\},
       \qquad0\le j\le h,                             \tag{0.1}
\]

where `|Q|=r-h`, and let the right endpoint `N` be any of the already
audited generalized balanced endpoints.  For arbitrary

\[
                 q\in Q,\qquad p\notin M_0,           \tag{0.2}
\]

put

\[
                 P=M_0-\{q\}+\{p\}.                  \tag{0.3}
\]

Then `P-M_0-M_1-...-M_h-N` is a literal trace-compatible collar.  Its left
seam has

\[
                 P\cap M_0=M_0-\{q\},\qquad
                 P\cup M_0=M_0\cup\{p\}.             \tag{0.4}
\]

If the stem lies in an upper-exact forest, the union in (0.4) already has
one provider.  Adding the seam therefore costs exactly one upper
multiplicity unit, regardless of `p`.  The pivot singleton, the two lower
rays, and the flat monotone-pivot compiler are unchanged.

The qualification is physical: the predecessor component must expose the
literal boundary letter

\[
                         D=(Q-\{q\})\cup\{p\},         \tag{0.5}
\]

and that pin must coexist with residence, guards, and the global common-cap
state.  Owner adjacency alone does not prove those rows.

For the canonical MSW complementary geodesic factor, let `Q_h^+(x)` be the
upstep positions of the Dyck endpoint `x` which survive the first `h`
deletions, and let `Q_h^-(x)` be the downstep positions of `x` which survive
as `1`-positions at the anti-Dyck endpoint `bar(x)` under the first `h`
reversed deletions.

The free-repeat endpoint graph has the following exact description.

* From the forward endpoint `x`, choose `q in Q_h^+(x)` and a downstep
  `p` of `x`.  The predecessor `x-q+p` is Dyck exactly under the interval
  height condition in Theorem 2.1 below; there is one explicitly
  characterized anti-Dyck exception.
* From the reverse endpoint `bar(x)`, choose `q in Q_h^-(x)` and an upstep
  `p` of `x`.  The mirror interval-height condition in Theorem 3.1 is exact.

Most importantly, if

\[
                              h\le r-2,                \tag{0.6}
\]

then **every signed MSW component has at least `r-h-1` endpoint
predecessors**.  In particular the primitive-component zero-neighbourhood
from the first-upper-repeat face disappears completely.

Thus the terminal problem is now a genuine global selection problem rather
than a local obstruction:

> Choose one orientation per MSW path and distinct predecessor endpoints so
> that the resulting component permutation is one directed spanning path,
> while simultaneously realizing the boundary letters (0.5) in one
> resident common-cap state.

The local degree theorem does not by itself imply Hall, a one-cycle
permutation, or the physical pins.

## 1. The free-repeat collar

### Theorem 1.1 (free-repeat seam algebra)

Assume `h>=2`, `r-h>=1`, and use the owner stem (0.1).  Let `P` be (0.3).
Then:

1. `P` has rank `r`, is distinct from every `M_j`, and is Johnson adjacent
   to `M_0`.
2. The left seam has the intersection and union (0.4).
3. Its lower colour is distinct from every internal stem intersection.
4. The source letter (0.5), followed by

   \[
                    \{\lambda_1\},\ldots,\{\lambda_h\},
   \tag{1.1}
   \]

   realizes `P` as the preceding depth-`h` owner.  Replacing `D` by the
   entering core letter `Q` gives `M_0`.

#### Proof

The exchange in (0.3) proves rank and Johnson adjacency.  Every `M_j`
contains all of `Q`, whereas `P` omits `q`, so `P` is not a stem owner.
Equation (0.4) is immediate.

Every internal intersection `M_(j-1) cap M_j` contains all of `Q`; the left
seam intersection omits `q`, proving Item 3.  Finally

\[
 D\cup\{\lambda_1,\ldots,\lambda_h\}=P,
 \qquad
 Q\cup\{\lambda_1,\ldots,\lambda_h\}=M_0,           \tag{1.2}
\]

which proves the literal slide. `square`

### Theorem 1.2 (upper accounting)

Let `F` be an upper-exact Catalan path forest containing the nonrepeated
stem `M_0-...-M_h-N`.  Adding the seam `PM_0` preserves every old upper
target and creates exactly one multiplicity excess.

For `b` component-joining seams, the resulting spanning path has exactly
`b` total upper multiplicity excess, even if several seams have the same
union.

#### Proof

The new union `V=M_0 union {p}` has rank `r+1`.  Upper exactness of `F`
gives one old edge whose union is `V`.  No old edge is removed, so the seam
adds one further occurrence and loses nothing.  Summing occurrence counts
over `b` added edges proves the second assertion; equality of two seam
values changes where the excess is located, not its total. `square`

### Proposition 1.3 (what is and is not compiler-neutral)

Changing `p` in (0.5) leaves the pivot letter, both adjacent lambda/rho
banks, every stem owner `M_j`, the two new lower rays, and all escaped
maximal crossing cells unchanged.  Therefore the local flat
monotone-pivot matching proof is unchanged.

It does **not** follow that the full compiler is automatically feasible.
The complete construction must still certify:

1. the predecessor trace ends with the literal boundary letter `D`;
2. all intervals reaching farther into that predecessor satisfy their
   occurrence guards and caps;
3. the seam lower colour `M_0-q` is compatible with the global lower
   matching; and
4. the terminal endpoint run of the new label `p` has the required
   residence continuation.

#### Proof

In the local source order, `D` lies immediately before the `h` lambda
letters.  Every new short ray containing the pivot has length at most `h`
and therefore does not reach `D`.  The old width-`h` crossing cells and the
new length-`(h+1)` pivot-owner windows are consequently independent of the
choice of `p`, except for the single preceding owner `P` itself.  This is
exactly the local data used by the flat pivot compiler.

Intervals extending one position farther do see `D`, and the pivot theorem
does not price their address, cap, or occurrence semantics.  Nor does an
owner-layer Johnson edge provide a source-boundary occurrence.  The four
listed rows are therefore genuine additional hypotheses. `square`

## 2. Forward endpoint graph

Let `x` be Dyck, with height

\[
                         H_x(t)=\sum_{i\le t}(2x_i-1). \tag{2.1}
\]

For an upstep position `q` and a downstep position `p`, write

\[
                            y=x-q+p                    \tag{2.2}
\]

for the word obtained by changing `x_q=1` to zero and `x_p=0` to one.

### Theorem 2.1 (exact forward criterion)

The word `y` in (2.2) is Dyck if and only if either

\[
 p<q,                                                   \tag{2.3}
\]

or

\[
 q<p\quad\text{and}\quad
       \min_{q\le t<p}H_x(t)\ge2.                     \tag{2.4}
\]

It is anti-Dyck if and only if

\[
 q=1,\qquad p=2r,qquad \max_t H_x(t)\le2.             \tag{2.5}
\]

Thus the predecessor endpoint set for the forward stem at `x` consists
exactly of the words (2.2) satisfying (2.3)--(2.5), with the additional
core restriction `q in Q_h^+(x)`.

#### Proof

If `p<q`, the exchange raises the height by two on `[p,q-1]` and changes it
nowhere else, so `y` is Dyck.  If `q<p`, it lowers the height by two on
`[q,p-1]`; Dyckness is therefore exactly (2.4).

An anti-Dyck result must begin in zero, forcing `q=1`.  The height is then
`H_x-2` before `p` and `H_x` from `p` onward.  Since `H_x>=0`, anti-Dyckness
forces `H_x(t)=0` for every `t>=p`.  A nonempty continuation changes height
by one at its first step, so `p=2r`.  The remaining condition is precisely
`H_x<=2` before the end. `square`

### Corollary 2.2 (uniform forward aperture)

If `h<=r-2`, every forward target has at least

\[
                              r-h-1                   \tag{2.6}
\]

distinct Dyck predecessor endpoints.

#### Proof

The core `Q_h^+(x)` contains `r-h` upstep positions.  Fix any
`q in Q_h^+(x)` with `q!=1`.

If some downstep occurs before `q`, choose one as `p`; (2.3) applies.  If
not, `q` lies in the initial run of upsteps.  Choose the first downstep
after that run.  The height on `[q,p-1]` is at least `q>=2`, so (2.4)
applies.  Different choices of `q` yield different exchanged words because
the symmetric difference with `x` recovers `q` and `p`.  At most the one
position `q=1` is discarded, giving (2.6). `square`

## 3. Reverse endpoint graph

Start the same MSW path at `bar(x)`.  A core position `q in Q_h^-(x)` is a
downstep of `x`, hence a `1`-position of `bar(x)`.  Choose an upstep position
`p` of `x`, which is a zero of `bar(x)`, and put

\[
                         y'=\bar x-q+p.                \tag{3.1}
\]

### Theorem 3.1 (exact reverse criterion)

The word `y'` is anti-Dyck if and only if either

\[
 q<p,                                                   \tag{3.2}
\]

or

\[
 p<q\quad\text{and}\quad
       \min_{p\le t<q}H_x(t)\ge2.                     \tag{3.3}
\]

It is Dyck if and only if

\[
 p=1,\qquad q=2r,qquad \max_t H_x(t)\le2.             \tag{3.4}
\]

These are exactly the reverse predecessor endpoints, with
`q in Q_h^-(x)`.

#### Proof

The base height of `bar(x)` is `-H_x`.  If `q<p`, the exchange lowers it
by two on `[q,p-1]`, so anti-Dyckness is automatic.  If `p<q`, it raises
the height there by two, and remaining nonpositive is exactly (3.3).

A Dyck result must begin in one, forcing `p=1`.  After `q` its height is
again `-H_x`, so the same terminal argument as in Theorem 2.1 forces
`q=2r`; before then, nonnegativity is exactly `H_x<=2`. `square`

### Corollary 3.2 (uniform reverse aperture)

If `h<=r-2`, every reverse target has at least `r-h-1` distinct anti-Dyck
predecessor endpoints.

#### Proof

Apply the argument of Corollary 2.2 after reversing the order and
complementing the height path.  Equivalently, for every
`q in Q_h^-(x)` except possibly `q=2r`, choose an upstep after `q` if one
exists, and otherwise choose the last upstep before the final downstep run;
conditions (3.2)--(3.3) apply.  Distinct `q` again give distinct words.
`square`

## 4. The signed component graph

Let `(x,+)` denote `P(x)` oriented from `x` to `bar(x)`, and `(x,-)` the
reverse orientation.  Define a directed graph `B_(r,h)` on these `2Cat_r`
signed states:

* `(y,-)->(x,+)` when the Dyck endpoint `y` is one of the forward
  predecessors from Theorem 2.1;
* `(y,+)->(x,-)` when the anti-Dyck endpoint `bar(y)` is one of the reverse
  predecessors from Theorem 3.1;
* include the exceptional same-sign arcs arising from (2.5) and (3.4).

The global collar order asks for a directed path which contains exactly one
of `(x,+),(x,-)` for every `x in D_r` and uses every chosen state once.
Corollaries 2.2 and 3.2 prove a linear minimum indegree on each signed
shore, but this is far below the `Cat_r/2` threshold of elementary
Hamiltonicity criteria.  More importantly, choosing one sign per component
couples the two shores.

The exact remaining owner/upper-q1 theorem is therefore:

> **Free-repeat signed transversal path lemma.**  For
> `h=Theta(sqrt(r))`, the graph `B_(r,h)` has a directed path selecting
> exactly one sign of every Dyck root.

Even that combinatorial lemma would prove only the owner/upper-q1 order.
The physical theorem must additionally realize all selected boundary
letters (0.5) under residence and one common-cap compiler.

### Theorem 4.1 (without the core restriction, the order is known)

If the requirement `q in Q_h^+(x)` or `q in Q_h^-(x)` is dropped, then the
signed-transversal path exists for every `r`.

#### Proof

The transposition Gray-code theorem of Proskurowski and Ruskey gives an
ordering

\[
                       x_1,x_2,\ldots,x_C             \tag{4.1}
\]

of all Dyck words in which consecutive words differ by exchanging one `1`
and one `0`.  Orient the corresponding MSW paths with alternating signs.

If `x_i` has sign `+`, then `x_(i-1)` is a Dyck predecessor of the forward
endpoint `x_i`, and sign `-` makes that Dyck endpoint terminal.  If `x_i`
has sign `-`, then `bar(x_(i-1))` is an anti-Dyck predecessor of the reverse
endpoint `bar(x_i)`, and sign `+` makes it terminal.  Thus every Gray-code
transition becomes one free-repeat Johnson seam, and the seams form the
directed spanning path (4.1). `square`

For the transition `x_(i-1)->x_i`, let `a_i` be the `1`-position of `x_i`
which is removed to recover `x_(i-1)`, and let `b_i` be its `0`-position.
The extra condition needed by the literal collar at the **target** is

\[
 \begin{cases}
   a_i\in Q_h^+(x_i),&i\text{ has forward sign},\\
   b_i\in Q_h^-(x_i),&i\text{ has reverse sign}.
 \end{cases}                                          \tag{4.2}
\]

There is a second, symmetric core condition at the predecessor endpoint if
the seam itself is to meet the owner-run residence floor.  It is isolated
in Theorem 4.2 below.  Consequently the owner-level frontier can be stated
more narrowly than the general graph problem, but the fully resident
frontier needs both endpoints.

> **Alternating core-safe Dyck Gray-code lemma.**  There is a transposition
> Gray code (4.1), and a choice of its initial parity, satisfying (4.2) at
> every transition.

The classical Gray-code theorem establishes the spanning order; the new
content is solely the alternating MSW-core safety of its exchanged
positions.

### Theorem 4.2 (exact two-sided residence condition)

Consider a forward seam

\[
                    y=x-q+p\longrightarrow x,         \tag{4.3}
\]

where the predecessor path `P(y)` is oriented from `bar(y)` to `y` and the
target path `P(x)` is oriented from `x` to `bar(x)`.  The two coordinate
runs clipped at the seam have length at least `h+1` if and only if

\[
                         q\in Q_h^+(x),
             \qquad    p\in Q_h^+(y).                 \tag{4.4}
\]

For the reverse seam, with predecessor `P(y)` oriented forward and target
`P(x)` oriented backward, the exact condition is

\[
                         q\in Q_h^-(x),
             \qquad    p\in Q_h^-(y),                 \tag{4.5}
\]

where `q` is the downstep of `x` removed from `bar(x)` and `p` is the
downstep of `y` present at the predecessor terminal `bar(y)`.

#### Proof

At the forward target, `q` is absent in the predecessor owner and present
from `M_0` through the complete stem exactly when it belongs to the target
core; this gives the first condition in (4.4).

At the predecessor, `p` is present in the terminal Dyck owner `y` and
absent immediately after the seam.  Traverse `P(y)` forward from `y` to
`bar(y)`.  If `p` is the `j`-th deleted upstep, then on the reverse
orientation it is inserted `j` owner steps before the terminal endpoint.
Its terminal run has at least `h+1` owners exactly when `j>h`, i.e. exactly
when `p` was not among the first `h` forward deletions.  This is
`p in Q_h^+(y)`.

The reverse assertion is the complement statement.  A downstep of `y`
present at `bar(y)` has a terminal run of length at least `h+1` in the
forward orientation exactly when it is not among the first `h` deletions
of the reversed path, which is membership in `Q_h^-(y)`. `square`

Thus the genuinely resident combinatorial target is stronger than (4.2):

> **Alternating bi-core-safe Dyck Gray-code lemma.**  Consecutive roots
> exchange a `1` which belongs to the plus cores of both incident roots on
> every forward seam, and exchange a `0` which belongs to the minus cores
> of both incident roots on every reverse seam, with the two seam types
> alternating.

Corollaries 2.2 and 3.2 prove large one-sided target neighbourhoods, but do
not prove that enough of those neighbours pass the predecessor-core test.
No minimum-degree or Hall claim for this bi-core graph is made here.

The companion theorem
`MATH_THEOREM_MSW_CORE_RECURSION_BICORE_LEAF_ROTATIONS_AND_AREA_OBSTRUCTION_20260805.md`
now gives an exact recursive description of both cores and completely
solves the bi-core test for contextual leaf rotations.  If the rotation
splits semilength `r` into apertures `ell` and `r-ell`, it is plus-safe
exactly when `ell>h` and minus-safe exactly when `r-ell>h`.  Thus every
leaf rotation has a safe sign for `r>2h`.  The same companion theorem also
proves that leaf rotations cannot be the whole spanning construction:
for odd `r=2m+1>=5`, area-parity imbalance forces at least
`Cat_m-1` nonadjacent, parity-preserving transpositions in any Hamilton
path.  The remaining Gray-code problem is therefore concentrated on those
long transitions.

## 5. Revised verdict

The previous primitive no-go is valid but narrowly scoped: it concerns the
choice `p=rho_1`, which forces the left seam to repeat the first stem upper
colour.  Once `p` is free, every signed canonical MSW component has many
endpoint predecessors at Gaussian depth.  There is no local empty-neighbour
obstruction.

What remains is global correlation, in two successive layers:

1. a signed transversal Hamilton-path problem in the explicit endpoint
   graph `B_(r,h)`; and
2. a typed boundary-letter/common-cap/residence lift of the selected arcs.

This is a genuine improvement over an arbitrary protected middle-levels
cycle problem, but neither layer is proved here.

## Reference for Theorem 4.1

F. Ruskey and A. Proskurowski, *Generating binary trees by
transpositions*, Journal of Algorithms **11** (1990), 68--84.  In Dyck-word
language their generation theorem is a Hamilton path in the graph whose
edges exchange one `1` and one `0`.
