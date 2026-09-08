# Catalan-matroid aligned cubes give an asymptotically spanning bi-core-safe path cover

**Date:** 2026-08-05  
**Method:** pure mathematics; no finite computation, enumeration, or solver  
**Status:** unconditional all-dimensional path-cover theorem.  It does not
yet join the `o(Cat_r)` paths into one spanning path.

## 0. Outcome

Let `T_r` be the basis graph of the Catalan matroid: its vertices are Dyck
words of semilength `r`, and two vertices are adjacent when one is obtained
from the other by exchanging one `1` and one `0`.

For every root `x`, let

\[
 D_h^+(x)=\{\pi_2(x),\pi_4(x),\ldots,\pi_{2h}(x)\}
\]

be its first `h` forward MSW departure labels, and let

\[
 D_h^-(x)=
 \{\pi_{2r-1}(x),\pi_{2r-3}(x),\ldots,
   \pi_{2r-(2h-1)}(x)\}
\]

be its first `h` reverse departure labels.  A transposition

\[
 y=x-\{a\}+\{b\},\qquad x_a=1,\quad x_b=0,
\]

can enter the forward signed root `(x,+)` with target-core safety exactly
when `a notin D_h^+(x)`, and can enter `(x,-)` exactly when
`b notin D_h^-(x)`.  Full clipped residence also requires the exchanged
source coordinate to survive at `y`.

The following global result holds.

### Theorem (bi-core-safe Catalan path cover)

If `h=o(r)`, then the Dyck roots admit a collection of vertex-disjoint
directed paths which

1. covers every one of the `Cat_r` roots exactly once;
2. assigns one sign to every root and alternates signs along each path;
3. uses only **bi-core-safe**, clipped-resident free-repeat MSW seams; and
4. has

   \[
   O\!\left({h\over r}\operatorname {Cat}_r\right)
   +o(\operatorname {Cat}_r)                         \tag{0.1}
   \]

   path components.

For the Gaussian collar depth `h=Theta(sqrt(r))`, the number of components
is

\[
 O\!\left({\operatorname {Cat}_r\over\sqrt r}\right)
 =o(\operatorname {Cat}_r).                          \tag{0.2}
\]

Equivalently, there is a disjoint union of signed transposition cycles
covering all but `o(Cat_r)` transition positions safely; deleting the
unsafe positions yields the paths above.

The construction uses large induced hypercubes inside the Catalan basis
graph.  It bypasses the doubly forbidden mountain edge and does not assume
that an arbitrary Proskurowski--Ruskey Gray code is safe.

## 1. Aligned Catalan cubes

Partition the first `4M` bit positions into fixed consecutive blocks of
length four, where

\[
 M=\left\lfloor {r\over2}\right\rfloor.
\]

Call a block **active** when it is either

\[
 1100\qquad\text{or}\qquad1010.                     \tag{1.1}
\]

Both words in (1.1) are Dyck words of semilength two.  They have relative
height sequences

\[
 (1,2,1,0)qquad\text{and}\qquad(1,0,1,0),           \tag{1.2}
\]

respectively.  Therefore replacing one by the other inside any Dyck word
preserves every prefix inequality: throughout the block the new relative
height is nonnegative, and after the block the height is unchanged.

The replacement exchanges only the two middle bits of the block, so it is
one Catalan-matroid basis exchange.

### Lemma 1.1 (full-cube classes)

Fix all inactive blocks, the final zero or two leftover positions, and the
set of active block positions.  If this data admits one Dyck word and there
are `m` active blocks, then all `2^m` choices of `1100` versus `1010` are
Dyck words.  Under the active-block toggles they induce a full hypercube
`Q_m` in `T_r`.

#### Proof

Each toggle preserves the Dyck property by (1.2), leaves every other block
unchanged, and keeps its own block active.  The `m` toggles commute because
their supports are disjoint.  Hence every subset of them is legal, giving
all vertices and edges of `Q_m`. `square`

These full cubes partition the entire set of Dyck roots.

## 2. Target and source fault ledgers

Give a cube `Q_m` its usual parity bipartition, according to the number of
active blocks in state `1010`.  Choose either phase and assign sign `+` to
one parity class and sign `-` to the other.  Adjacent cube vertices then
always have opposite signs.

For an active block, its mate differs in the two middle coordinates.  At a
target word `x`, exactly one of those coordinates is a `1` and exactly one
is a `0`.

### Lemma 2.1 (one-sided direction bounds)

At every signed vertex, at most `h` active-block directions fail its own
target-core test, and at most `h` active-block directions fail its own
source-core test.

#### Proof

At a `+` target, the incoming forward seam tests the middle `1` coordinate
against `D_h^+`.  At a `-` target, the incoming reverse seam tests the
middle `0` coordinate against `D_h^-`.

The roles cross for outgoing seams.  A `+` source feeds a reverse seam and
therefore tests its middle `0` coordinate against `D_h^-`; a `-` source
feeds a forward seam and tests its middle `1` coordinate against
`D_h^+`.

In every one of these four cases, distinct aligned blocks use distinct
coordinates and the relevant forbidden set has size `h`.  Hence each
target ledger and each source ledger rejects at most `h` directions.
`square`

The source-failure set for an edge cannot in general be bounded by looking
only at the target: it belongs to the mate's MSW core.  The proof below
avoids that invalid inference by averaging incoming and outgoing cycle
directions separately.

## 3. A nearly safe Hamilton cycle in every large cube

### Lemma 3.1 (two-sided automorphism averaging)

Let every signed vertex of `Q_m`, `m>=2`, have at most `h` forbidden
target directions and at most `h` forbidden source directions.  Then
`Q_m` has a directed Hamilton cycle with at most

\[
 {2h\over m}2^m                                      \tag{3.1}
\]

arcs which fail at least one of the two endpoint-core tests.

#### Proof

Fix one directed Hamilton cycle of `Q_m`.  The parity-preserving
automorphism group of the cube is transitive on directed edges ending in
either fixed parity class.  Equivalently, after applying a uniformly random
parity-preserving cube automorphism, the incoming edge direction at every
fixed target vertex is uniform on the `m` coordinate directions.

If `R_{in}(v)` is the target-forbidden direction set at `v`, the
probability that its incoming cycle arc fails at the target is

\[
 {|R_{in}(v)|\over m}\le {h\over m}.
\]

Similarly, if `R_{out}(v)` is its source-forbidden set, the outgoing cycle
direction is uniform and fails at the source with probability at most
`h/m`.  Summing over all vertices and applying the union bound, the
expected number of cycle arcs failing either endpoint is at most
`(2h/m)2^m`.
Some automorphic image of the cycle attains at most this expectation.
`square`

Delete every rejected arc from that directed Hamilton cycle.  If none is
rejected, delete one arbitrary arc merely to open the cycle.  The remaining
arcs form a directed path cover, every retained arc is bi-core-safe at
both endpoints, and the number of paths is at most

\[
 1+{2h\over m}2^m.                                   \tag{3.2}
\]

Because cube parity is the chosen MSW sign, every retained path alternates
signs and hence is a path in the signed free-repeat endpoint graph.

## 4. Almost every Dyck root belongs to a large cube

An arbitrary four-bit block has `16` possible states, exactly two of which
are active.  Put `ell=2r-4M`, so `ell` is zero or two.  Consequently the
number of all binary words whose `M` aligned blocks contain fewer than
`M/16` active blocks is at most

\[
 2^\ell\sum_{j<M/16}{M\choose j}2^j14^{M-j}.         \tag{4.1}
\]

The factor `2^ell` accounts for the possible final two bits when `r` is
odd.
If `Z` is binomial with parameters `(M,1/8)`, (4.1) is at most

\[
 2^\ell16^M\Pr[Z<M/16]
 \le 4^r\exp(-M/64),                                 \tag{4.2}
\]

by the elementary multiplicative Chernoff bound.

This bound counts all binary words, so it also bounds the Dyck words in
small cubes.  On the other hand,

\[
 \operatorname {Cat}_r
 ={1\over r+1}{2r\choose r}
 \ge {4^r\over(r+1)(2r+1)},                          \tag{4.3}
\]

because the central binomial coefficient is at least the average of the
`2r+1` binomial coefficients.  Dividing (4.2) by (4.3) shows that the number
`L_r` of Dyck roots in cubes with `m<M/16` satisfies

\[
 L_r=o(\operatorname {Cat}_r).                       \tag{4.4}
\]

Furthermore, every large cube has at least `2^(M/16)` vertices.  Hence the
number of large cube classes is at most

\[
 2^{-M/16}\operatorname {Cat}_r
 =o(\operatorname {Cat}_r).                          \tag{4.5}
\]

## 5. Proof of the path-cover theorem

Use singleton paths for all roots in small cubes.  In each large cube use
the path cover from Lemma 3.1.  The covers are vertex-disjoint because the
cube classes partition the roots.

Let `p_r` be the resulting number of paths.  Equations (3.2), (4.4), and
(4.5) give

\[
\begin{aligned}
 p_r
 &\le L_r
    +2^{-M/16}\operatorname {Cat}_r
    +{32h\over M}\operatorname {Cat}_r\\
 &=O\!\left({h\over r}\operatorname {Cat}_r\right)
    +o(\operatorname {Cat}_r).
\end{aligned}                                        \tag{5.1}
\]

Every nonsingleton path has alternating signs.  By Lemma 2.1, every
retained directed edge satisfies the exact two-ended core condition for its
sign.  By the free-repeat two-sided residence theorem, it therefore gives
a clipped-resident seam between the corresponding canonical MSW
components.  This proves all four assertions of the theorem. `square`

## 6. Catalan-matroid interpretation

The upstep set of a Dyck word is a basis of the Catalan matroid.  Each
active-block toggle exchanges the two middle ground elements of one
four-element interval.  Lemma 1.1 therefore exhibits an induced Boolean
subposet of bases, and the cube edges are literal basis-graph four-cycle
directions.

The useful feature is not generic Hamiltonicity of a matroid basis graph.
It is the product structure: an `m`-cube has a transitive family of
Hamilton cycles, while each MSW endpoint core deletes at most `h`
directions at its own endpoint.  Automorphism averaging charges target
failures to incoming cycle directions and predecessor failures to outgoing
cycle directions, converting the combined local ratio `2h/m` into the
global path-cover defect.

## 7. Exact boundary of the result

This theorem improves the global safe-Gray status from isolated local
degree bounds to a spanning path cover with `o(Cat_r)` components.  It also
shows that doubly forbidden individual edges do not create a
positive-density obstruction: the aligned cubes route around almost all of
them.

It does **not** yet prove the signed-transversal Hamilton-path lemma.  At
Gaussian depth the residual number of paths is still of order at most
`Cat_r/sqrt(r)`, far larger than `O(1)`.  Joining those paths requires a
second-level absorber or a new family of cross-cube safe exchanges.

Nor does the theorem price the literal boundary letters, residence tails,
deeper upper shadows, or the common-cap compiler.  It is an owner/upper-`q1`
safe-path theorem only.

The sharpened next target is now:

> Build cross-cube safe absorbers which merge a positive fraction of the
> remaining aligned-cube paths per round while preserving their signed
> endpoint phases.

Geometric contraction of the path count, followed by a bounded terminal
absorber, would close the combinatorial safe-Gray gate.
