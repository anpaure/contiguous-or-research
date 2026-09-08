# Exact state fibers and one-step compatibility for the MTF--chain program

This note attacks the missing move-to-front lemma in
`GLOBAL_MTF_SCD_HANDOFF.md`.  It is entirely finite and combinatorial; no
search is used.

The main positive result is an exact characterization of when one chain can
be followed by another in one move-to-front update.  The characterization is
particularly simple: after deleting the update set, the two chains must be
mutually nested.  The main negative result is equally important.  This
pairwise transition relation does **not** compose automatically, because a
multi-element update coalesces the new first block.  In particular, repeated
full-minimum updates are confined to a very sparse one-loss graph.

Throughout, a saturated chain is written

\[
  C=(B=B_0\subset B_1\subset\cdots\subset B_h),
  \qquad B_i=B\cup\{e_1,\ldots,e_i\}.
\]

Put

\[
  E(C)=(e_1,\ldots,e_h),\qquad
  Z(C)=[k]\setminus B_h.
\]

For a chain `C` and a set `X`, write

\[
  C-X=\{S\setminus X:S\in C\},
\]

with duplicate consecutive sets suppressed.

## 1. The exact state fiber

Let `OP(U)` denote the set of ordered partitions of `U` (and let the empty
ordered partition be the unique member of `OP(emptyset)`).

### Lemma 1 (fiber theorem)

An ordered partition `Pi` exposes every nonempty member of `C` as a prefix
union if and only if it has the form

\[
  \Pi=(P_1,\ldots,P_a,
       \{e_1\},\ldots,\{e_h\},
       Q_1,\ldots,Q_b),                         \tag{1}
\]

where `(P_1,...,P_a)` is an ordered partition of `B` and
`(Q_1,...,Q_b)` is an ordered partition of `Z(C)`.

#### Proof

The prefix giving `B` forces all blocks before the first increment to
partition `B`.  Consecutive chain members differ by the one element `e_i`, so
there must be exactly one intervening block, namely the singleton `{e_i}`.
After the top of the chain has appeared, all remaining blocks lie in `Z(C)`
and are unrestricted.  The converse is immediate.  ∎

Thus, if `a(n)` is the ordered Bell number, the full state fiber has size

\[
  a(|B|)a(|Z(C)|).
\]

For a symmetric chain beginning and ending in ranks `r` and `k-r`, this is
`a(r)^2`.  The singleton-state subfiber, in which every block is a singleton,
has size `(r!)^2`.

The freedom to split `B` is real and important.  Treating `B` as one block is
only a convenient sufficient state, not the full fiber.

## 2. A fixed-state transition criterion

For an ordered partition `Pi=(R_1,...,R_s)`, let `Pi-X` be the ordered list

\[
  (R_1\setminus X,\ldots,R_s\setminus X)
\]

after empty blocks are deleted.  Its prefix unions form a chain.

Let

\[
  D=(A,A\cup\{f_1\},\ldots,A\cup\{f_1,\ldots,f_g\}).
\]

### Lemma 2 (fixed-state test)

If `A` is nonempty, a state `Pi` can be updated in one step to expose `D` if
and only if the prefix chain of `Pi-A` contains `D-A`.  Whenever any update
works, the canonical update `X=A` works.

If `A` is empty, the update is forced to be `X={f_1}`, and the prefix chain
of `Pi-{f_1}` must contain

\[
  \varnothing,\{f_2\},\{f_2,f_3\},\ldots,
  \{f_2,\ldots,f_g\}.
\]

#### Proof

Suppose first that `A` is nonempty.  If `M_X(Pi)` exposes `D`, its first block
`X` must be contained in `A`.  Removing that first block from every target
prefix shows that `Pi-X` contains `D-X` as prefix unions.  Now delete the
additional elements `A\setminus X` from both the residual ordered partition
and those target prefixes.  The result is exactly that `Pi-A` contains
`D-A`.  Conversely, if `Pi-A` contains `D-A`, then

\[
  M_A(\Pi)=(A,\Pi-A)
\]

exposes `D`.

If `A` is empty, the first nonempty member of `D` is `{f_1}`.  The new first
block is therefore forced to be exactly `{f_1}`, after which the same
deletion argument applies.  ∎

This lemma permits canonicalizing **one specified transition**.  It does not
permit canonicalizing all transitions of a tour simultaneously, because
replacing `X` by the whole minimum changes the state inherited by the next
step.

## 3. Exact existential compatibility of two chains

Call `X` an admissible anchor for `D` if

* `emptyset != X subseteq A` when `A` is nonempty;
* `X={f_1}` when `A` is empty.

Two set-chains are *cross-nested* when every member of one is comparable by
inclusion with every member of the other, equivalently when their union is a
single chain after duplicates are removed.

### Theorem 3 (quotient-chain criterion)

There exist an exposing state `Pi` for `C` and a nonempty update `X` such
that `M_X(Pi)` exposes `D` if and only if, for some admissible anchor `X` of
`D`, the quotient chains

\[
  C-X\quad\hbox{and}\quad D-X                 \tag{2}
\]

are cross-nested.

When the minimum `A` of `D` is nonempty, this is equivalent simply to

\[
  C-A\quad\hbox{and}\quad D-A
  \quad\hbox{being cross-nested}.              \tag{3}
\]

#### Proof: necessity

Assume `Pi` exposes `C` and `M_X(Pi)` exposes `D`.  The residual ordered
partition `Pi-X` has a prefix chain.  Every member of `C-X` is a prefix union
of `Pi-X`, because every member of `C` was a prefix union of `Pi`.  Every
member of `D-X` is also a prefix union of `Pi-X`, after the new first block
`X` is removed.  Hence both quotient chains lie in one prefix chain and are
cross-nested.  The first block condition makes `X` an admissible anchor.

#### Proof: sufficiency

Assume (2).  Extend the union of the two quotient chains to a maximal chain
of `2^{[k]\setminus X}`; equivalently choose a permutation `rho` of
`[k]\setminus X` whose prefix sets contain both quotient chains.

Because `rho` contains `C-X`, insert the elements of `X` into `rho` at their
positions prescribed by `C`: elements of `X cap B` go in the initial
`B`-part, elements `e_i in X` go at their respective singleton-increment
positions, and elements of `X cap Z(C)` go in the final part.  This produces
a permutation `pi` of `[k]` whose prefix chain contains `C` and whose deletion
of `X` is `rho`.

Apply the update `X` to the singleton ordered partition `pi`.  The resulting
state is

\[
  (X,\rho_1,\rho_2,\ldots),
\]

and it exposes `D` because `rho` contains `D-X` and `X` is an admissible
anchor.  This proves sufficiency.

Finally, if `A` is nonempty and some `X subseteq A` works, deleting the
additional common set `A\setminus X` preserves every inclusion relation in
(2).  Therefore the full anchor `A` works, proving (3).  ∎

The theorem is exact even though the witnessing predecessor state can always
be chosen to be a singleton permutation.  The successor state generally is
not a singleton permutation: its first block is the whole update set `X`.

## 4. The fence form of the criterion

Suppose the target minimum `A` is nonempty and put

\[
  F_j=\{f_1,\ldots,f_j\},\qquad F=F_g.
\]

The sets comparable with **every** member of

\[
  \varnothing=F_0\subset F_1\subset\cdots\subset F_g=F
\]

are exactly

\[
  F_0,F_1,\ldots,F_g
  \quad\hbox{and all supersets of }F.           \tag{4}

Indeed, a set contained in `F` but not equal to a prefix crosses one of the
prefixes, while every superset of `F` contains them all.

### Corollary 4 (prefix-fence criterion)

There is a one-step existential transition `C -> D` if and only if every
member `S` of `C` satisfies

\[
  S\setminus A\in\{F_0,\ldots,F_g\}
  \quad\hbox{or}\quad F\subseteq S\setminus A. \tag{5}

Equivalently, write

\[
  Q_0=B(C)\setminus A.
\]

Then either

1. `F subseteq Q_0` (the **dominance case**); or
2. `Q_0=F_t` for some `t`, and after the source increment word is filtered by
   deleting its letters in `A`, its next letters are

   \[
     f_{t+1},f_{t+2},\ldots,f_g.                \tag{6}
   \]

   in that order, up to whichever happens first: the source chain ends or all
   of `F` has appeared.  If all of `F` appears, there is no restriction on
   later source increments.

The empty-minimum case has the identical statement after anchoring at
`{f_1}` and replacing `(f_1,...,f_g)` by `(f_2,...,f_g)`.

This criterion makes the quotient graph completely explicit.  In particular,
what at first looks like a potentially dense family of arcs has two very
different parts: dominance arcs and rigid prefix-alignment arcs.

## 5. Why pairwise density is not enough

Theorem 3 is a theorem about one edge.  A Hamilton path in this quotient
graph is not yet an MTF--SCD tour, because the witnessing state above a chain
may depend on whether the chain is being used as the head or the tail of an
edge.

The obstruction is block coalescence.  A move `M_X` makes every element of
`X` one new tied block.  Later moves may extract a subset of that block, but
they do not magically refine its residue into the singleton star blocks
needed by an unrelated target chain.

### Lemma 5 (full-minimum one-loss barrier)

Suppose the current state exposes `C` and its first block is exactly the
minimum `B` of `C`.  Let `D` be a nontrivial saturated target chain with
minimum `A` and first increment `f_1`.  If one update from this **fixed state**
exposes `D`, then

\[
  B\subseteq A
  \quad\hbox{or}\quad
  B\setminus A=\{f_1\}.                         \tag{7}

In particular,

\[
  |B\setminus A|\le 1.                          \tag{8}

#### Proof

By Lemma 2 we may test the full update `A`.  In the residual ordered
partition the first surviving block from the old state is `B\setminus A`, if
nonempty.  The target quotient chain begins

\[
  \varnothing\subset\{f_1\}\subset\cdots.
\]

Consequently that first old block must either disappear or be precisely the
first singleton increment `{f_1}`.  ∎

### Corollary 6 (central endpoint barrier)

Let `k=2m`.  Suppose the current first block is an `m`-set `P`.  If the next
target is a nontrivial symmetric chain, then necessarily its minimum is

\[
  P\setminus\{a\}
\]

for some `a in P`, its minimum rank is `m-1`, and its first increment is `a`.

#### Proof

A nontrivial symmetric chain has minimum rank at most `m-1`.  The alternative
`P subseteq A` in (7) is impossible.  The other alternative gives
`|P\setminus A|=1`, forcing `|A|=m-1` and the asserted form.  ∎

Thus an iterated last-pair path which reaches a central singleton chain cannot
be spliced in one full-minimum step to a generic long chain.  Only a very
special length-three symmetric chain can follow it.

The dominance case in Corollary 4 is especially deceptive.  It says that an
appropriately *split* source minimum contains all target star coordinates.
But a preceding full-minimum update has coalesced that same source minimum
into one block.  It therefore destroys precisely the refinement that the
next dominance transition needs.  A dense-digraph proof based only on the
existential quotient graph cannot be valid.

## 6. A universal reset and the right approximate target

There is nevertheless a cheap exact way to start any one chain.

### Lemma 7 (reverse-star reset)

From an arbitrary ordered-partition state, the chain

\[
  C=(B,B+e_1,\ldots,B+e_1+\cdots+e_h)
\]

can be exposed after at most `h+1` updates.  If `B` is empty, `h` updates
suffice.

#### Proof

Apply the singleton updates

\[
  \{e_h\},\{e_{h-1}\},\ldots,\{e_1\}.
\]

The state now begins with the singleton blocks

\[
  \{e_1\},\{e_2\},\ldots,\{e_h\}.
\]

If `B` is nonempty, apply one final update `B`.  The resulting state begins

\[
  (B,\{e_1\},\ldots,\{e_h\})
\]

and exposes `C`.  ∎

There is also an exact reset to a **prescribed state**, rather than merely to
some state exposing a prescribed chain.

### Lemma 8 (ordered-partition reset)

Let `Pi=(R_1,...,R_s)` be any prescribed ordered partition of `[k]`.  From an
arbitrary current state, the updates

\[
  R_s,R_{s-1},\ldots,R_1
\]

produce exactly the state `Pi`.  In particular the cost is `s<=k`.

#### Proof

The blocks `R_i` are disjoint and cover the ground set.  After updating them
in reverse order, their last-occurrence times are strictly ordered as
`R_1,...,R_s`; no untouched element remains.  ∎

This converts a many-component path cover into an OR construction without
making any assumption about the inherited tail of a component's first state.

### Theorem 9 (path-cover reduction)

Suppose a chain cover consists of `N` chains and all but `q` nonempty Boolean
sets lie in those chains.  Suppose further that the chains can be partitioned
into `p` genuine MTF state-paths, one state per chain.  Let `s_j` be the
number of blocks in the prescribed first state of component `j`.  Then

\[
  \nu(k)\le N-p+\sum_{j=1}^p s_j+q.             \tag{9}
\]

In particular, if every component starts in a state with at most `H` blocks,
then

\[
  \nu(k)\le N+(H-1)p+q,                         \tag{10}
\]

and unconditionally `H<=k`.

#### Proof

Use Lemma 8 to initialize the prescribed first state of every component,
including the first.  These resets cost `sum_j s_j`.  The internal arcs of
the `p` paths cost `N-p` further entries.  Finally append the `q` missed sets
literally.  This proves (9), and (10) follows immediately.  ∎

Consequently a Hamilton path is more than is necessary.  For the asymptotic
goal it suffices to find a state-transversal path cover satisfying

\[
  pH+q=o(W(k)).                                  \tag{11}
\]

This is a quantitatively useful weakening of the missing lemma.

The last-pair map alone cannot meet (11).  Its image omits `W(k-1)` Greene--
Kleitman templates, so any injective last-pair path cover has at least
`W(k-1)` starts.  Every omitted-image template ends in a star, and therefore
every state exposing it has at least two blocks in all nondegenerate
dimensions.  Formula (9) then pays at least one excess entry for each such
component.  Thus this path cover alone already has additive cost at least
`W(k-1)=(1/2+o(1))W(k)`.  New transitions must absorb almost all of these
starts.

There is a second, independent reason not to expect a uniform dense-graph
argument for the standard Greene--Kleitman decomposition.

### Proposition 10 (a half-sized dominance hole in Greene--Kleitman)

In the standard Greene--Kleitman SCD, no chain minimum contains coordinate
`1`.  Exactly `W(k-1)` chain templates have coordinate `1` as their first
star.  Every one of these target chains has zero incoming dominance arcs in
the sense of Corollary 4.

#### Proof

The first fixed symbol of a Greene--Kleitman template cannot be `1`: a fixed
block is Dyck, and a nonempty Dyck word begins with `0`.  A star is also zero
in the minimum.  Thus coordinate `1` belongs to no chain minimum.

Templates beginning with a star are in bijection with arbitrary templates in
dimension `k-1`, by deleting that first star, so there are `W(k-1)` of them.
Their target star set contains coordinate `1`.  A dominance predecessor would
need its minimum to contain the entire target star set, which is impossible.
∎

Since `W(k-1)=(1/2+o(1))W(k)`, the dominance part of the quotient graph misses
an asymptotically half-sized target family.  Any successful argument for this
specific SCD must use the rigid alignment arcs on a linear fraction of the
chains, or must replace the SCD/coordinate boundary itself.

## 7. The remaining exact global object

The preceding theorems suggest the following hierarchy.

1. **Pairwise quotient graph.**  Its arcs are characterized exactly by
   Theorem 3 or Corollary 4.  It is useful for finding candidate neighbors,
   but it forgets inherited block structure.
2. **State-fiber graph.**  Its vertices are actual ordered partitions in the
   fibers from Lemma 1.  This is the correct graph for composition.
3. **Path-cover target.**  It is enough to find a transversal state-path cover
   with `pH=o(W)`, not necessarily a Hamilton path.

A particularly clean subproblem restricts to singleton states.  A singleton
state is a permutation, and updating a singleton at position `j` performs a
prefix rotation: that symbol moves to the front and the preceding `j-1`
symbols shift right.  Hence the singleton version is a transversal Gray-code
problem:

> choose one permutation from (almost) every chain fiber so that successive
> permutations differ by one prefix rotation.

This restriction keeps every minimum fully refined and eliminates the
coalescence obstruction, but it is substantially stronger.  It is the same
last-occurrence geometry underlying Lipski's singleton-string problem, whose
small exact values already show that it is not a routine Hamiltonicity
statement.

The realistic mathematical target left by this note is therefore not “prove
the quotient graph is dense.”  It is one of the following.

* Construct a near-spanning prefix-rotation transversal in the singleton
  subfibers.
* Construct a state-transversal path cover with `o(W/H)` components while
  controlling the refinement of each new minimum.
* Give a recursion whose interfaces carry an ordered-partition state, rather
  than merely a chain label, so that no physical reset is paid at each
  recursive block.

The quotient-chain theorem supplies the exact local test for any such proof,
and Lemma 5 identifies the state information that the recursion must retain.
