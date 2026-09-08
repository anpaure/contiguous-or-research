# The suspended hex is the multislice triangle router, and loose packet trees are exact flexible absorbers

Date: 2026-07-31  
Status: exact target-hypergraph geometry, exact local/flexible absorption,
and a resource-private logarithmic-tree packing theorem.  This does **not**
align a Delcourt--Postle leave with the bank, preserve a frozen pointwise
common cap, or give a standard arbitrary-deletion robustly matchable graph.

## 0. Verdict

The alternatives inside one suspended transparent `C6` are much more useful
than a list of three unrelated target atoms.  They form one exact three-port
hole router.

Ignoring literal slot labels, a target atom is a three-colouring

\[
              x=(D,P,R),\qquad |D|=n,quad |P|=2,quad |R|=n-2,       \tag{0.1}
\]

of a `2n`-set, where the corresponding outer diamond is
`(D,D union P)`.  A suspended hex through `x` chooses

\[
                    b\in D,\qquad a\in P,\qquad c\in R              \tag{0.2}
\]

and cyclically rotates the colours of `b,a,c`.  The two rotations and `x`
are exactly the three atoms of one old phase.

This gives a three-uniform hypergraph `H_n` with the following exact
parameters for every `n>=3`.

* It has

  \[
       A_n=\binom{2n}{n}\binom n2                                  \tag{0.3}
  \]

  vertices, degree `2n(n-2)`, pair codegree at most one, and

  \[
       |E(H_n)|={A_n\,2n(n-2)\over3}.                               \tag{0.4}
  \]

* Its two-section is `4n(n-2)`-regular, connected, and has diameter exactly
  `n`.  Its triangles are precisely the packet triples: there are no Berge
  triangles, although Berge four-cycles already occur at `n=3`.
* For every coordinate `z`, the half-set `{x:z in D(x)}` has normalized
  edge boundary exactly `1/n`.  Thus this is not a constant-expansion
  network.  A fixed-coordinate quotient gives an explicit eigenvalue
  `1-3/(2n)+O(n^(-2))`.
* Through one canonical literal target there are exactly `n-2` packets which
  are pairwise private outside that target; this is best possible in the
  canonical-slot catalogue.

The local identity composes exactly.  If packet triples form a clean loose
three-uniform tree with `e` packets, then its `2e+1` target atoms are a
fully flexible one-hole boundary: **any one** of those targets may be the
hole.  The other `2e` target atoms split into the two-atom old states of all
packets, and activating any packet incident with the hole fills it.  This
is a literal resource identity, not only an outer-palette statement.

For every

\[
       (e-1)(10n-2)<n(n-2),                                       \tag{0.5}
\]

every abstract loose packet tree of order `e` has such a clean embedding.
If `v=2e+1`, the symmetric orbit of one embedding contains at least

\[
                         {P\over6v^2},
       \qquad P=\binom{2n}{n+2},                                  \tag{0.6}
\]

pairwise-resource-disjoint copies.  Taking `e=ceil(log n)` for sufficiently
large `n` therefore gives `h` independent flexible absorbers using
`O(h log n)` packets whenever

\[
                          h\le {P\over6(2\lceil\log n\rceil+1)^2}. \tag{0.7}
\]

This is a genuine resource-private **product-robust** template: one arbitrary
hole may be chosen in each tree.  It is not a standard robustly matchable
template for an arbitrary `h`-subset of the union of all ports.  A loose
tree has exactly one hole by counting, so two holes in one component are an
exact obstruction.  Also, diameter `n` rules out an `O(log n)` universal
router between arbitrary prescribed target atoms.  Correlated planting is
still needed, but the three-way/local-flexibility supply is now proved.

## 1. The target multislice and its packet lines

Let `Omega` have order `2n`.  Write a geometric target atom as

\[
                 x=(D,P,R),\qquad D\dot\cup P\dot\cup R=\Omega,    \tag{1.1}
\]

with the sizes in (0.1).  Its canonical literal lift is

\[
 (D,D\cup P;(D+p,1),(D+q,1)),\qquad P=\{p,q\}.                    \tag{1.2}
\]

Fix `b in D`, `a in P`, and `c in R`, and put `s=P-{a}`.  Define

\[
\begin{aligned}
 x_0&=(D,P,R),\\
 x_1&=(D-b+a,\ P-a+c,\ R-c+b),\\
 x_2&=(D-b+c,\ P-a+b,\ R-c+a).                                  \tag{1.3}
\end{aligned}
\]

The set `{x_0,x_1,x_2}` is a packet line.  In the notation of the suspended
hex theorem, take `K=D-b` and orient `(a,s)` as the two elements of `P`.
Then (1.3) is exactly `{e_b,e_a,e_c}`.  Conversely every old suspended-hex
phase has this form.

### Theorem 1.1 (exact regular linear hypergraph)

The packet lines form a three-uniform hypergraph `H_n` satisfying
(0.3)--(0.4), with

\[
                         d_{H_n}(x)=2n(n-2),
       \qquad \Delta_2(H_n)=1.                                  \tag{1.4}
\]

Consequently its two-section `G_n` is `4n(n-2)`-regular.

#### Proof

There are `binom(2n,n)binom(n,2)` partitions (1.1).  Through a fixed
partition, (0.2) has `n*2*(n-2)` choices.

Two distinct vertices on a packet line differ on exactly three coordinates,
one from each colour, and their colours are cyclically permuted.  The
difference support and the orientation recover the third vertex.  Hence a
pair lies on at most one packet line.  Double counting incidences proves
(0.4), and linearity says that every incident line contributes two distinct
two-section neighbours. `square`

### Proposition 1.2 (all graph triangles are packet lines)

`H_n` has no Berge triangle.  Equivalently every triangle of `G_n` is the
three vertices of one packet line.

#### Proof

Let three pairwise adjacent colourings be `x,y,z`.  Their three pairwise
Hamming distances are all three.  At any coordinate either all three colours
agree, exactly one colouring differs, or all three colours differ.  If `u`
coordinates have the second form and `v` the third, then

\[
                              2u+3v=9.                            \tag{1.5}
\]

Thus either `(u,v)=(0,3)` or `(3,1)`.  The first case is one packet line.
In the second case, look at the coordinate where all three colours differ
and label its successive colours `0,1,2`.  Adjacency `x-y` and `y-z` must
both use the same cyclic orientation forced by `0->1->2`.  At the unique
coordinate where `x=z` but `y` differs, this would require simultaneously
`x+1=y` and `y+1=x` modulo three, a contradiction. `square`

Berge four-cycles do exist.  At `n=3`, write a state as `(D|P|R)` on
`{0,...,5}`.  The following four packet lines meet consecutively in four
different states:

```text
{(034|25|1),(134|05|2),(234|15|0)}
{(013|45|2),(023|15|4),(034|25|1)}
{(013|45|2),(123|05|4),(134|25|0)}
{(023|45|1),(123|05|4),(234|15|0)}.
```

Adding `n-3` fixed `D`-coordinates and `n-3` fixed `R`-coordinates suspends
this example to every `n>=3`.

## 2. Connectivity, diameter and the exact slow cut

### Theorem 2.1 (diameter)

For every `n>=3`, `G_n` is connected and

\[
                              diam(G_n)=n.                        \tag{2.1}
\]

#### Proof

Fix an initial and a target colouring.  Make the directed mismatch
multigraph on the three colour names: every miscoloured coordinate gives an
arc from its present colour to its target colour.  Equal colour-class sizes
make this digraph Eulerian.  It decomposes into directed three-cycles and
antiparallel two-cycles.

A directed three-cycle is corrected by one legal move.  A collection of
`q>0` antiparallel pairs is corrected in at most `q+1` legal moves.  One
explicit carry proof is as follows.  A single pair is cleared in two moves
using a correctly coloured element of the third class.  For parallel pairs,
retain the displaced third-colour element after the first move; every next
pair is cleared in one further move, and the last move returns the carry.
Pairs on two different unordered colour pairs are spliced by the two-move
identity

```text
       01,10,12,21  ->  01,20,12,01  ->  11,00,22,11,
```

with colour names cyclically relabelled as necessary.  Iterating these two
identities proves the `q+1` bound.

Let `c` be the number of directed three-cycles after a circulation
decomposition and `q` the number of antiparallel pairs.  They use
`3c+2q<=2n` coordinates.  Unless `c+q=n`, the preceding correction costs at
most `c+q+1<=n`.  Equality forces `c=0` and every coordinate to be
miscoloured.  Balance with class sizes `(n,2,n-2)` then forces exactly two
`D<->P` pairs and `n-2` `D<->R` pairs.  They clear in exactly `n` moves:
first use one `D->P`, one `P->D`, and one `R->D`; the second `D->P` move
creates a single carry in `P`; pass that carry successively through the
`n-2` `D<->R` pairs and close it on the last pair.  In token notation this
is

```text
 (d0,p0,r0)+,
 (d1,d0,p0)+,
 (x0,p1,r1)-,
 (x1,r1,r2)-, ...,
 (x_(n-3),r_(n-3),d0)-,
```

with the evident shortened last line at `n=3`.  Here `d_i:D->P`,
`p_i:P->D`, `x_i:D->R`, and `r_i:R->D`; each displayed triple lists its
current `D,P,R` tokens.  This proves the upper bound and connectivity.

For the lower bound, choose two states whose `D`-classes are disjoint.
Every legal move replaces exactly one member of `D`, so at least `n` moves
are necessary. `square`

### Theorem 2.2 (coordinate bottleneck and quotient spectrum)

For a fixed coordinate `z`, put

\[
                    S_z=\{x:z\in D(x)\}.                          \tag{2.2}
\]

Then `|S_z|=|V(G_n)|/2`, and every vertex of `S_z` has exactly `4(n-2)`
neighbours outside it.  Hence

\[
 {e(S_z,S_z^c)\over 4n(n-2)|S_z|}={1\over n}.                    \tag{2.3}
\]

The colour of `z` is an equitable three-state quotient of simple random
walk on `G_n`, with transition matrix

\[
 Q_n=\begin{pmatrix}
 1-1/n&1/(2n)&1/(2n)\\
 1/4&1/2&1/4\\
 1/(2(n-2))&1/(2(n-2))&1-1/(n-2)
 \end{pmatrix}.                                                   \tag{2.4}
\]

Besides `1`, its eigenvalues are

\[
 \lambda_\pm={3n^2-10n+4\ \pm
 \sqrt{n^4-8n^3+20n^2-16n+16}\over4n(n-2)},                     \tag{2.5}
\]

so

\[
                         \lambda_+=1-{3\over2n}+O(n^{-2}).       \tag{2.6}
\]

In particular the spectral gap of the full graph is at most
`1-lambda_+=Theta(1/n)` and its conductance is at most `1/n`.

#### Proof

The coordinate `z` lies in `D` in exactly half the states.  It leaves `D`
exactly when it is selected as `b`; there are two choices of `a`, `n-2`
choices of `c`, and two rotations.  This proves (2.3).  Conditional on its
current colour, `z` is selected with probabilities `1/n`, `1/2`, and
`1/(n-2)`, and the two rotations send it to either other colour equally.
This is (2.4).  Its characteristic polynomial has nontrivial root sum

\[
 {3n^2-10n+4\over2n(n-2)}
\]

and product

\[
 {2n^2-9n+8\over4n(n-2)},
\]

which gives (2.5)--(2.6). `square`

The diameter and cut are relevant scope warnings.  Any chain of packet
routers carrying a hole from target `x` to target `y` projects to a path in
`G_n`.  Some prescribed pairs therefore require at least `n` packets.  The
multislice graph does not supply an `O(log n)`-radius universal target bank.

## 3. One hex is a three-port router and terminator

Let one packet have old phase

\[
                         O=\{x_0,x_1,x_2\}                        \tag{3.1}
\]

and new phase `N`.  For `i in Z_3`, put

\[
                         H_i=O-\{x_i\}.                           \tag{3.2}
\]

### Theorem 3.1 (exact three-way boundary)

For every `i,j`, `H_i` and `H_j` are legal two-atom matchings and

\[
 res(H_i)=res(O)-res(x_i).                                       \tag{3.3}
\]

Thus `H_i -> H_j` transports the exact four-resource hole from `x_i` to
`x_j`, while

\[
                            H_i\longrightarrow N                 \tag{3.4}
\]

is a gain-one completion of the hole `x_i`.

#### Proof

The three old atoms are pairwise disjoint, and the new phase uses exactly
their complete resource union.  Equations (3.3)--(3.4) are therefore
literal multiset identities. `square`

This is not the zero-boundary sparse-cycle rerouter.  A complete old/new
hex toggle has zero boundary, but the three *punctured old states* have
three different nonzero four-resource boundaries.  That is the source of
target mobility.

### Proposition 3.2 (sharp canonical private fan)

Fix a canonical target `x=(D,V=D+p+q)`.  Among its `2n(n-2)` canonical
packet lines there are exactly `n-2` which can be selected pairwise so that
their complete supports meet only in `res(x)`.  In particular a private fan
of order `n-2` exists and no larger canonical fan exists.

#### Proof

Index a packet through `x` by `(b,c,a)`, where `b in D`, `c notin V`, and
`a in {p,q}`.  Besides the two target owners, its owner bank contains

\[
                         V-b\qquad\hbox{and}\qquad D+c.           \tag{3.5}
\]

Two port-private packets must therefore have different `b` and different
`c`.  Since `c` has only `n-2` values, the fan has order at most `n-2`.

Conversely choose all `n-2` values of `c`, inject them into distinct values
of `b`, and use an arbitrary orientation at each pair.  The two auxiliary
lower colours are

\[
                  D-b+a,\qquad D-b+c,                            \tag{3.6}
\]

the two auxiliary upper colours are

\[
                  V-b+c,\qquad V-a+c,                            \tag{3.7}
\]

and the four auxiliary owners are

\[
          D-b+a+c,\quad V-b,\quad D+c,\quad D-b+c+(P-a).         \tag{3.8}
\]

Typed-set comparison shows that distinct `b` and distinct `c` make every
resource in (3.6)--(3.8) distinct across packets. `square`

## 4. Clean loose packet trees

A **clean loose packet tree** is a collection `T` of packet lines such that

1. its packet hypergraph is a loose three-uniform hypertree: the lines can
   be ordered so that the first is arbitrary and every later line meets the
   preceding union in exactly one target vertex; and
2. all distinct target vertices appearing in the tree form a matching in
   the literal four-resource host.

Thus a tree of `e` packets has `v=2e+1` distinct target vertices.

### Theorem 4.1 (flexible one-hole orientation)

Let `T` be a clean loose packet tree and let `r` be any one of its target
vertices.  There is a choice of one punctured old state on every packet such
that the chosen target atoms partition

\[
                             V(T)-\{r\}.                          \tag{4.1}
\]

Moreover every packet incident with `r` omits `r`.  Activating any one of
those incident packets produces a literal perfect matching of the complete
resource union of `V(T)`.

#### Proof

Induct on the number of packets.  Peel a leaf packet
`{w,u_1,u_2}`, where `w` is its attachment vertex and `u_1,u_2` are its
two leaf vertices.

If `r` is outside `{u_1,u_2}`, orient the leaf packet to omit `w` and select
`u_1,u_2`; apply induction to the smaller tree with the same hole `r`.
If `r=u_1`, select `w,u_2` and apply induction to the smaller tree with hole
`w`; the case `r=u_2` is symmetric.  These choices partition every vertex
except `r`.  In particular every packet containing `r` must omit it.

Choose an incident packet.  Its selected old state is precisely its other
two vertices.  Remove those two atoms and insert its three-atom new phase.
The new phase uses the resource union of all three packet vertices.  Every
other selected old atom is disjoint from that union by cleanliness, so the
result is a perfect matching of all target-vertex resources. `square`

### Corollary 4.2 (the exact topological limitation)

If a loose packet forest has `e` packets and `c` components, it has
`2e+c` target vertices.  Any simultaneous punctured-old configuration uses
exactly `2e` target atoms.  If it is a matching, it therefore has exactly
one target hole in every tree component.

In particular a disjoint union of `h` clean loose trees is robust for one
arbitrary hole per tree, but not for an arbitrary `h`-subset of all its
ports: two holes in one component are impossible without omitting a packet
or adding a cyclic/non-loose exchange layer.

## 5. Every logarithmic loose tree embeds cleanly

The next estimate restores all literal resources.  Fix a canonical target
`x`.  A packet through it is indexed by `(b,c,a)` as in Proposition 3.2.
Let `z` be another target atom disjoint from `x`.

### Lemma 5.1 (one forbidden target blocks at most `10n-2` options)

At most `10n-2` canonical packets through `x` have one of their two new
target vertices sharing a resource with `z`.

#### Proof

A fixed forbidden lower colour occurs as `D-b+a` in at most `n-2` options
and as `D-b+c` in at most two, for a total at most `n`.  A fixed forbidden
upper colour occurs as `V-b+c` in at most two and as `V-a+c` in at most `n`,
for a total at most `n+2`.

A fixed canonical owner slot can occur in (3.8) in at most

\[
                  1+2(n-2)+2n+1=4n-2                            \tag{5.1}
\]

options.  The two forbidden slots of `z` therefore block at most `8n-4`
options.  Adding the three typed bounds gives `10n-2`. `square`

### Theorem 5.2 (clean embedding of any small loose tree)

Let `T_abs` be any abstract loose three-uniform hypertree with `e` edges.  If

\[
                       (e-1)(10n-2)<n(n-2),                      \tag{5.2}
\]

then `T_abs` has a clean canonical embedding in `H_n`.

#### Proof

Embed the first line arbitrarily.  In a leaf-building order, suppose `j`
lines have already been embedded and the next line is to attach at `x`.
There are `2n(n-2)` packet options through `x`.  Apart from `x`, the current
tree has `2j` target vertices.  Lemma 5.1 and the union bound show that fewer
than

\[
                           2j(10n-2)                              \tag{5.3}
\]

options meet an old resource.  For `j<=e-1`, (5.2) makes (5.3) smaller than
the catalogue.  Choose a surviving option and continue. `square`

In particular `e=ceil(log n)` satisfies (5.2) for all sufficiently large
`n`.

## 6. A resource-private product-robust bank

Fix one clean tree from Theorem 5.2, with `e` packets and `v=2e+1` target
vertices.  Let `O` be its full `Sym(Omega)` orbit.  Every orbit member uses
`v` distinct lower resources, `v` distinct upper resources, and `2v`
distinct canonical owner slots.  Put

\[
 M=\binom{2n}{n},\qquad N=\binom{2n}{n+1},\qquad
 P=\binom{2n}{n+2}.                                               \tag{6.1}
\]

### Theorem 6.1 (orbit packing)

The orbit `O` contains at least

\[
 {1\over v^2(1/M+1/P+4/N)}\ge {P\over6v^2}                       \tag{6.2}
\]

pairwise-resource-disjoint clean tree gadgets.

#### Proof

By transitivity and double counting, a fixed lower, upper, or canonical-slot
resource lies in respectively

\[
 {v|O|\over M},\qquad {v|O|\over P},\qquad {2v|O|\over N}         \tag{6.3}
\]

orbit copies.  Let `B` be a maximal disjoint subfamily of order `t`.
Every orbit copy meets a resource of a member of `B`, so the union bound and
(6.3) give

\[
 |O|\le t v^2|O|(1/M+1/P+4/N).                                  \tag{6.4}
\]

Cancel `|O|`.  Since `M,N>=P`, (6.2) follows. `square`

### Corollary 6.2 (logarithmic flexible bank)

Take `e=ceil(log n)` and `v=2e+1`.  For all sufficiently large `n` and every

\[
                         h\le\left\lfloor {P\over6v^2}\right\rfloor, \tag{6.5}
\]

there are `h` mutually private clean packet trees, using `he=O(h log n)`
hexes.  From each of their `v` ports choose an arbitrary one.  The union of
the corresponding off states is a matching, and one activation per tree
closes all `h` chosen holes simultaneously.

For a single hex (`e=1`), the stronger orbit calculation already frozen in
the suspended-hex theorem gives more than `P/54` disjoint packets.  Hence
for **every** `h=o(P)`, a three-choice-per-demand private bank of `h` packets
exists for all sufficiently large `n`.  The logarithmic tree version trades
an extra logarithmic resource cost for `Theta(log n)` target alternatives
per demand.

### Corollary 6.3 (common-basis survival, not alignment)

Under the exact uniform-marginal common-basis distribution, a fixed tree
gadget is punctured with probability at most

\[
 vp,qquad p={C\over N}={2(2n+1)\over n(n+2)}.                    \tag{6.6}
\]

Thus some common basis retains at least `(1-vp)` of every prepacked bank in
expectation, which is `1-O(log n/n)` for Corollary 6.2.  This uses no
independence.  It does not select a common basis satisfying the other
physical/cap/compiler rows, and it does not force a later DP leave to choose
one port from each surviving tree.

## 7. Exact scope of the robust-template conclusion

What is now proved is stronger than a disjoint list of fixed targets:

1. one packet has three exact alternative four-resource boundaries;
2. a clean loose packet tree routes its unique hole to any of `2e+1` target
   atoms and terminates it;
3. `Theta(P/log^2 n)` mutually private logarithmic trees exist by an
   elementary orbit packing; and
4. a linear bank of independent three-way sites exists, so local absorber
   supply is not the obstruction for any `h=o(P)`.

What is **not** proved is a standard robustly matchable graph for every
`h`-subset of one global flexible boundary.  Three exact facts explain the
gap.

* A loose tree has exactly one hole.  Arbitrary hole multiplicities across
  components violate Corollary 4.2.
* `G_n` has diameter `n` and a coordinate conductance cut `1/n`; arbitrary
  prescribed target-to-bank routing cannot have logarithmic path length.
* An arbitrary protected matching can saturate the `n`-owner transversal
  through one target, and every packet changes a pointwise common-cap map.

Therefore the right use of this theorem is **correlated planting**: make the
bulk leave choose one port from each planted tree.  It cannot be appended as
a black-box repair to an arbitrary already-produced leave.  Cyclic packet
complexes or a body-conditioned matching-indexed atlas are still required
for arbitrary-deletion robustness.

## 8. Independent audit

The dependency-free script

```text
scratch/audit_catalan_c6_multislice_router_20260731.py
```

fully enumerates `H_n` for `3<=n<=5`, and additionally runs the direct
two-section census through `n=7`.  It checks:

* the exact vertex, edge, degree and pair-codegree formulas;
* two-section connectivity and diameter `n`;
* absence of non-packet graph triangles;
* the exact fixed-coordinate cut `1/n`;
* existence of the displayed suspended Berge four-cycle; and
* the exact canonical port-private fan size `n-2` for a fixed target.

It additionally exhausts abstract loose trees through four packets and
checks the one-hole orientation and one-packet termination identities.  It
writes

```text
scratch/catalan_c6_multislice_router_20260731.audit.json.
```

The audit is finite confirmation only.  The all-`n` statements are proved
above.  It excludes common-basis alignment, arbitrary protected-slot
availability, global common-cap regeneration, and the downstream compiler.
