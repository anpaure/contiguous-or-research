# A logarithmic-degree physical side-forest cut obstruction

Date: 2026-07-31  
Status: complete abstract obstruction and exact cut certificate.  This is
not a Boolean counterexample.

## 0. Verdict

The following data do **not** imply forest-compatible diagonal
representatives:

* both diagonal incidence shores have perfect matchings;
* the representative hypergraph has degree `Theta(m)`;
* its pair-codegree is `O(m^(1/3))`;
* it has a uniform fractional incidence matching with every physical
  socket load at most two; and
* the number of physical sockets exceeds the number of selected edges by
  `Theta(N m^(-2/3))`.

There is an explicit probabilistic-method family at precisely these
scales in which every integral incidence matching either has physical
degree at least three or contains a physical cycle.  The obstruction is a
one-unit **graphic cut deficit** in each of `Theta(N/m)` disjoint blocks.
Consequently any exterior independent-boundary absorber must alter at
least one representative in every bad block.

This proves that the uniform-marginal common-basis theorem and additive
cost averaging cannot by themselves finish the physical row.  A positive
theorem must impose a cutwise physical-expansion/augmentor condition.  It
does not refute the Boolean collar, whose additional containment geometry
may supply exactly those cross-cut augmentors.

## 1. Representative systems and their two physical cuts

Let `L,R` be equal incidence shores and let `V` be the physical socket
set.  A representative atom is

```text
                 (ell,r; {x,y}),
```

where `ell in L`, `r in R`, and `x!=y` belong to `V`.  A diagonal
incidence matching chooses one atom at every member of `L` and `R`.  Its
physical lift is the graph on `V` consisting of the chosen edges `{x,y}`.

For `W subseteq V`, every physical graph of maximum degree two obeys

\[
 \sum_{e\text{ chosen}} |e\cap W|\le 2|W|.           \tag{1.1}
\]

If `B subseteq V` is the seam-anchor set and anchors have side degree at
most one, the sharper inequality is

\[
 \sum_{e\text{ chosen}} |e\cap W|
       \le 2|W|-|B\cap W|.                           \tag{1.2}
\]

Every physical forest also obeys

\[
 |\{e\text{ chosen}:e\subseteq W\}|\le |W|-1
       \qquad(\varnothing\ne W\subseteq V).          \tag{1.3}
\]

Thus a family of atoms may pass incidence Hall perfectly while failing a
physical capacity cut (1.1), an anchor cut (1.2), or a graphic cut (1.3).

For a fixed incidence instance define

\[
 \begin{aligned}
 \mu_W&=\min_M\sum_{e\in M}|e\cap W|,\\
 \gamma_W&=\min_M|\{e\in M:e\subseteq W\}|,
 \end{aligned}                                      \tag{1.4}
\]

where the minima range over all diagonal incidence matchings.  Hence

\[
 \mu_W>2|W|-|B\cap W|                                \tag{1.5}
\]

is a solver-free degree obstruction, while

\[
 \gamma_W>|W|-1                                     \tag{1.6}
\]

is a solver-free forest obstruction.  Each minimum in (1.4) is an
ordinary minimum-cost bipartite perfect matching.  These are necessary
cut certificates, not a sufficient simultaneous characterization.

## 2. A balanced low-codegree labeling lemma

### Lemma 2.1

Let `b` be sufficiently large and let

\[
                       b\le s\le b+2b^{1/3}.          \tag{2.1}
\]

There is a map

\[
 \sigma:[b]\times[b]\longrightarrow { [s]\choose2} \tag{2.2}
\]

with the following properties.

1. For every socket `v`,

   \[
          b\le |\{(i,j):v\in\sigma(i,j)\}|\le 2b.   \tag{2.3}
   \]

2. For every row `i`, column `j`, and socket `v`,

   \[
   \begin{aligned}
    |\{j:v\in\sigma(i,j)\}|&\le b^{1/3},\\
    |\{i:v\in\sigma(i,j)\}|&\le b^{1/3}.            \tag{2.4}
   \end{aligned}
   \]

3. Every socket pair occurs at most three times.

When `s=b`, (2.3) may be strengthened to equality `2b` at every socket.
Moreover, after identifying both copies of `[b]` on the incidence shores,
one may prescribe

\[
                  \sigma(i,i)=\{i,i+1\}\pmod b,      \tag{2.8}
\]

so the diagonal incidence matching lifts to a Hamilton cycle on the
sockets.

### Proof

First construct a loopless multigraph `H` on `[s]` with exactly `b^2`
edges, maximum edge multiplicity at most three, and degrees differing by
at most one.

For `s=b`, take two copies of `K_b` and one Hamilton cycle.  It has
`b(b-1)+b=b^2` edges, multiplicity at most three, and degree exactly
`2b`.

For `b<s<=b+2b^(1/3)`, start with one copy of `K_s` and add an
almost-regular simple graph with

\[
                 b^2-{s\choose2}                     \tag{2.5}
\]

edges.  For large `b`, the number in (2.5) lies between zero and
`binom(s,2)`.  An almost-regular simple graph with any prescribed edge
count is obtained, for example, by taking initial cyclic distance classes
and then an initial segment of the next class.  Its degrees differ by at
most two; to balance exactly, whenever `deg(u)>=deg(v)+2`, choose a
neighbour `w!=v` of `u` which is not adjacent to `v` and replace `uw` by
`vw`.  Such a `w` exists by the degree inequality, the move preserves
simplicity, and the sum of squared degrees strictly decreases.  Iteration
ends with all degrees differing by at most one.  The resulting multigraph has multiplicity at
most two and socket degrees equal to `2b^2/s+O(1)`, which lie in `[b,2b]`.

Distinguish repeated copies of an edge of `H`, and assign the `b^2`
distinguished edges uniformly at random to the `b^2` cells of
`[b]x[b]`.  Socket degrees and socket-pair multiplicities are fixed by
`H`.  For a fixed row and socket, the number of incident assigned labels
is hypergeometric with mean at most two.  The standard sampling-without-
replacement tail bound gives, for `k=b^(1/3)`,

\[
 \Pr(X\ge k)\le (2e/k)^k.                            \tag{2.6}
\]

The same holds for a fixed column and socket.  There are fewer than
`4b^2` such events, and

\[
                 4b^2(2e/b^{1/3})^{b^{1/3}}<1        \tag{2.7}
\]

for all sufficiently large `b`.  Hence some assignment satisfies every
row and column bound.  When `s=b`, first assign the distinguished
Hamilton-cycle copy to the diagonal cells as in (2.8), and randomly assign
the remaining two copies of `K_b` to the off-diagonal cells.  The random
part has mean below two; the deterministic diagonal label contributes at
most one incidence to a fixed row/socket or column/socket pair.  Thus the
bad event at threshold `k=b^(1/3)` is bounded by the hypergeometric tail at
`k-1`, namely `(2e/(k-1))^(k-1)`.  Its union bound over fewer than `4b^2`
events still tends to zero.  This proves the strengthened statement as
well.  The resulting assignment is `sigma`. `square`

The immaterial `O(1)` balancing detail in the second construction can
also be avoided by using the usual round-robin decomposition of `K_s`
into matchings and filling the last class symmetrically.

## 3. The pseudorandom graphic-cut obstruction

### Theorem 3.1

There is an infinite family of representative systems with outer shore
size `mathcal N`, physical socket size

\[
              \mathcal N+\Theta(\mathcal N m^{-2/3}),\tag{3.1}
\]

and `m=Theta(log mathcal N)`, satisfying all of the following.

1. The incidence projection is regular of degree `m` and has many perfect
   matchings.
2. Every vertex of the representative hypergraph has degree `Theta(m)`.
3. Its maximum pair-codegree is `O(m^(1/3))`.
4. The constant weight `1/m` on every representative atom is a fractional
   diagonal incidence matching, and every physical socket has fractional
   load at most two.
5. There is an integral diagonal incidence matching whose physical lift
   has maximum degree two on every tight module.
6. No integral diagonal incidence matching has a physical lift which is a
   linear forest.  This remains false with no seam anchors at all.

### Proof

Fix a large integer `b`, put `a=floor(b^(1/3))`, and make a paired module.

* The **tight module** has incidence shores `L_0,R_0` of order `b` and a
  socket set `V_0` of order `b`.
* The **reserve module** has incidence shores `L_1,R_1` of order `b` and a
  socket set `V_1` of order `b+2a`.

For each `i=0,1`, use Lemma 2.1 to label every edge of the complete
bipartite graph `L_i--R_i` by one physical edge of `V_i`.  Regard the
result as the representative atom

\[
                    (\ell,r;\sigma_i(\ell,r)).       \tag{3.2}
\]

There are no atoms between different modules.  Repeat this paired module
`t` times on disjoint vertex sets.

The outer shores both have order

\[
                         \mathcal N=2tb,              \tag{3.3}
\]

while the socket set has order

\[
 t(b+b+2a)=\mathcal N+2ta
          =\mathcal N+\Theta(\mathcal N b^{-2/3}).   \tag{3.4}
\]

Every outer vertex has degree `b`.  Lemma 2.1 gives physical degrees
between `b` and `2b`.  A pair consisting of two outer vertices has
codegree at most one; an outer/socket pair has codegree at most `b^(1/3)`;
and a socket/socket pair has codegree at most three.  Thus the maximum
pair-codegree is at most `b^(1/3)`.

Give every atom weight `1/b`.  Each outer vertex receives weight one.
Every socket receives its candidate degree divided by `b`, hence load at
most two.  This proves the fractional statement.

On each tight module, the prescribed diagonal matching (2.8) lifts to a
Hamilton cycle and therefore has physical maximum degree two.  Thus the
tight local degree row is integrally feasible; acyclicity, not degree, is
the unavoidable failure there.

This fractional point is not claimed to satisfy the graphic inequalities:
on a tight module it has weight `b=|V_0|` internally, exactly one above
the forest bound.  The example isolates a graphic-cut obstruction after
incidence and degree capacity have both been fractionalized.

Now take any integral incidence perfect matching.  Its restriction to
each tight module selects exactly `b` physical edges, all lying on the
`b` vertices of `V_0`.  If some socket has degree at least three, the
physical degree row fails.  Otherwise the selected physical graph has
maximum degree two and total degree `2b` on `b` vertices, so every vertex
has degree exactly two.  It is a nonempty union of cycles and is not a
forest.  Equivalently, for `W=V_0`,

\[
                         \gamma_W=b=|W|,              \tag{3.5}
\]

which violates the graphic cut (1.3) by exactly one.

Finally choose, for example, `t=ceil(e^b/b)`.  Then
`b=Theta(log mathcal N)`, and (3.1)--(3.4) have exactly the asserted
scales. `square`

### Corollary 3.2 (absorber-intervention floor)

In the construction of Theorem 3.1, any enlargement which obtains a
physical linear forest while still matching every incidence vertex must
touch every tight module by a new atom.  Since one new atom can touch at
most two incidence modules, an unrestricted enlargement needs at least

\[
                         \lceil t/2\rceil
                          =\Theta(\mathcal N/\log\mathcal N)          \tag{3.6}
\]

selected new cross-cut atoms.  If the diagonal incidence partner of every demand is
kept within its original module and only its physical representative is
altered, the sharper lower bound is `t`.

### Proof

If a tight module is untouched, it still contributes `b` selected edges
supported on its `b` sockets, and the proof of Theorem 3.1 forces a degree
violation or a cycle.  Thus all `t` tight modules must be touched.  A new
atom has only one left and one right incidence endpoint, so it touches at
most two modules.  This proves `ceil(t/2)`.  Under module-preserving
incidence it touches only one tight module, proving the sharper statement.
`square`

This is the scale on which an independent-boundary absorber must be
distributed.  Total socket surplus does not help unless its sockets are
reachable across every tight graphic cut.

The underlying obstruction already appears at `b=3`: three incidence
assignments supported on three physical sockets cannot form a forest.  If
their maximum degree is at most two, all three sockets have degree two and
the lift is a triangle (or a multigraph cycle).  Lemma 2.1 is only the
large-`b` balancing step which embeds this elementary Euler defect into
the requested logarithmic-degree, low-codegree scale.

## 4. Why balanced common-basis marginals do not control conflicts

The obstruction above occurs after the common basis has already been
chosen.  There is also a separate logical limitation in using only the
balanced common-basis distribution.

### Proposition 4.1

Let `2<=C<=N/2`.  There are two identical rank-`C` matroids on an
`N`-element set, a distribution on their common bases with exact marginal
`C/N` at every element, and a conflict graph of maximum degree

\[
                          O(N/C)                      \tag{4.1}
\]

such that every common basis contains at least `floor(C/2)` conflict
pairs.

### Proof

Take both matroids to be the uniform matroid `U_(C,N)`.  Its uniform base
distribution has marginal `C/N`.

Partition the ground set into `g=floor(C/2)` classes whose sizes differ by
at most one, and make each class a clique of the conflict graph.  Its
maximum degree is at most `ceil(N/g)-1=O(N/C)`.  If a basis puts `q_i`
elements in class `i`, convexity gives

\[
 \sum_i {q_i\choose2}\ge \lfloor C/2\rfloor,         \tag{4.2}
\]

because `sum q_i=C` and there are only `floor(C/2)` classes.  Thus every
common basis has the claimed number of conflicts. `square`

At the Catalan density `C/N=Theta(1/n)`, the degree in (4.1) is
`Theta(n)=Theta(log N)`.  Therefore even a logarithmic conflict degree and
exact uniform marginals do not imply a conflict-free common basis.  The
usual local-lemma heuristic is invalid here unless its dependency graph
also respects the fixed-cardinality/common-basis constraint; disjoint
pair events are not a lopsided dependency graph under arbitrary
conditioning on the complements of other pair events.

## 5. Consequence for the Boolean programme

Theorems 3.1 and 4.1 are abstract.  They do not show that the Boolean
containment instance has a bad tight module.  They prove exactly which
extra fact a positive Boolean theorem must establish.

One sufficient cutwise hypothesis is:

> For every physical socket set `W` whose current representative minimum
> reaches the graphic boundary `gamma_W=|W|`, the independent-boundary
> bank contains an `M`-ready atom crossing `W`, and such atoms admit a
> system of distinct representatives over all inclusion-minimal tight
> cuts.

After one crossing alteration per minimal tight cut, one must still check
degree cuts (1.2) and the contracted `Gamma` graphic cuts.  The
independent-boundary absorber supplies the correct local `1 -> 2`
operation, but Theorem 3.1 shows that its required global interface is a
**cut-covering linkage**, not an additive count of available collars.

The sharp remaining Boolean question is thus whether containment geometry
and the balanced-subcube reserve guarantee a disjoint crossing bank for
all tight physical cuts.  Uniform common-basis marginals, degree,
pair-codegree, and scalar surplus do not answer it.
