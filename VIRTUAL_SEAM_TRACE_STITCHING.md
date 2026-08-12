# Virtual-seam trace stitching: what is proved and what remains

## 1. Verdict

Put

\[
 P_m=[0,m]^4,\qquad S=2m-1,
\]

and let `G_m` be the lexicographic selected-cover graph: its vertices are
the rank-`S` points and its edge of colour `z`, `|z|=S+1`, joins the two
lower covers obtained by subtracting from the first two positive
coordinates of `z`.

The all-upper **Virtual-Seam Excursion Lemma remains open**.  I do not have
an all-`m` signed ordering of the forced arms which covers every
`|y|>=S+1`, and I do not have an obstruction to such an ordering.

There are, however, two proof-grade advances.

1. A bounded-copy repair covers every fixed-depth upper band at
   width-plus-surface cost.  For each fixed `q`, there is an explicit word
   of length

   \[
       |\{z\in P_m:|z|=2m\}|+O_q(m^2)                 \tag{1.1}
   \]

   covering every target of rank `2m-1,...,2m+q`.  Uniformly, its excess is
   `O(m^2 q^5)`.  Thus `q=o(m^{1/5})` already gives `o(m^3)` excess while
   the depth tends to infinity.
2. If no selected edge is copied and the word is only a signed ordering of
   refinements of the forced arms, then a quadratic number of virtual seams
   is genuinely necessary.  More precisely, at least

   \[
                   {(m-2)(m-3)\over45}               \tag{1.2}
   \]

   seams must be used by witnesses already in rank `2m+1`.

So the corrected architecture cannot be a nearly Eulerian word with a
small number of exceptional joins.  Either it must exploit a positive
quadratic density of the available seams, or it must insert a quadratic
library of local boundary traces.  Both costs are still surface order.

Finite signed forced-arm orders covering the entire upper half exist for
`m=2,3,4`; these are diagnostics, not an induction.

## 2. Forced arms and the surface kernel

Let

\[
 K_m=\{v\in V(G_m):\deg(v)\ne2\}.
\]

Cut at every vertex of `K_m`, and cut each residual all-degree-two cycle
once.  The resulting edge-disjoint paths are the forced arms.  The exact
lexicographic degree calculation gives, for `m>=2`,

\[
 |K_m|=2m^2+2,\qquad |\mathcal A_m|=2m^2+m+4.         \tag{2.1}
\]

There is one residual degree-two component, so after adding its chosen cut
vertex the cut set `K_m^*` satisfies

\[
                         |K_m^*|\le2m^2+3.            \tag{2.2}
\]

Writing every arm as a vertex word and concatenating them in arbitrary
orientations has length

\[
                  |E(G_m)|+|\mathcal A_m|
              =   |Z_m|+2m^2+m+4.                    \tag{2.3}
\]

Every middle colour occurs as an internal adjacent maximum.  Every
rank-`S` vertex occurs as a singleton (or may be appended literally if one
uses a variant with isolated vertices).  What fails is only the simultaneous
upper trace order.

## 3. A completely explicit first-upper-layer repair

The first useful positive result needs no global arm ordering.

### Theorem 1 (all local turns suffice)

There is a word of length

\[
                         |Z_m|+O(m^2)                 \tag{3.1}

\]

covering every target of ranks `2m-1`, `2m`, and `2m+1`.

### Proof

Start with any concatenation of the forced-arm words.  At every degree-three
vertex `v`, let its incident selected edges have other endpoints
`u_1,u_2,u_3`.  For every unordered pair `{i,j}`, append the three-letter
turn gadget

\[
                         (u_i,v,u_j).                 \tag{3.2}

\]

At the one artificial cut in the residual degree-two component, append the
analogous gadget for its two incident edges.

There are `m(m+1)+2` degree-three vertices.  Hence (3.2) adds at most

\[
                   9\bigl(m(m+1)+2\bigr)+3           \tag{3.3}

\]

letters.

Let `y` have rank `2m+1`.  The lexicographic component theorem supplies a
path in `G_m[y]` whose vertex maximum is `y`.  One edge cannot have maximum
`y`, because every edge colour has rank `2m`.  Take two consecutive edges
on a facet-spanning subpath.  Their distinct colours are `y-e_i` and
`y-e_j` for two positive coordinates of `y`, so their maximum is `y`.

If their common vertex has degree two and is not the artificial cut, the
corresponding three vertices occur consecutively inside one forced arm.  If
the common vertex has degree three, (3.2) supplies them.  The artificial
cut is supplied separately.  Therefore `y` occurs.  The base arms already
cover ranks `2m-1` and `2m`.  QED.

This theorem identifies exactly what the failed rotation-system lemma was
missing: one physical transition at a cubic vertex is not enough, but all
three local turns cost only surface order when copied as length-three
traces.

## 4. A fixed-depth upper-band theorem

The preceding repair extends beyond one layer without solving the global
ordering problem.

### Theorem 2 (surface repair for bounded upper depth)

For integers `m>=2` and `1<=q<=2m`, there is a word covering every `y in
P_m` with

\[
                      2m-1\le |y|\le2m+q             \tag{4.1}

\]

whose length is at most

\[
 |Z_m|+2m^2+m+4
 +(2m^2+3){q+5\choose4}(3q+4)+O(m^2).               \tag{4.2}

In particular, for fixed `q` this is `|Z_m|+O_q(m^2)`, and for
`q=o(m^{1/5})` it is `|Z_m|+o(m^3)`.

### Proof

Use the arbitrary forced-arm concatenation from (2.3).  Fix an upper target
`y` and put

\[
                         D=|y|-2m.                    \tag{4.3}

\]

The reverse-greedy proof of the lexicographic component theorem gives a
directed facet-spanning path `P_y` in `G_m[y]`.

Every vertex `v` on this path has rank `2m-1`; hence

\[
 \delta=y-v\ge0,\qquad |\delta|=D+1.                 \tag{4.4}

\]

Along every directed selected edge the potential

\[
                         \Phi(v)=\sum_{i=1}^4 i v_i  \tag{4.5}

\]

strictly decreases.  For the vertices below this fixed `y`, equation
(4.4) confines `Phi` to an interval of width at most `3(D+1)`.  Therefore

\[
                         |E(P_y)|\le3(D+1).           \tag{4.6}

\]

If `P_y` avoids `K_m^*`, it lies in one forced arm and already occurs as a
contiguous interval of the base word.  Otherwise append the vertex word of
`P_y` as one repair gadget.

It remains only to count exceptional targets.  Charge one to a vertex
`v in P_y cap K_m^*`.  For a fixed `v`, every charged `y` has

\[
                    y=v+\delta,\qquad |\delta|\le q+1.
\]

Ignoring the box ceilings only increases the count, and the number of such
weak four-part compositions is at most

\[
                              {q+5\choose4}.          \tag{4.7}

\]

By (2.2), (4.6), and (4.7), the total repair length is bounded by the large
term in (4.2).  Each appended path is itself an interval below `y` with
maximum `y`; joins between gadgets do not destroy any witness.  QED.

The exponent five is not asserted to be sharp.  It comes from counting all
deficit vectors independently at every surface vertex and then appending
their paths separately.  Sharing these paths is exactly the missing global
trace-packing theorem.

## 5. A quadratic seam lower bound for edge-once arm orderings

The next theorem explains why a successful pure ordering must use its seam
set densely.

### 5.1 A quadratic hard family

For `m>=4`, consider

\[
 \begin{aligned}
 \mathcal H_1&=\{(0,a,b,c):2\le a,b,c\le m-1,
                              \ a+b+c=2m+1\},\\
 \mathcal H_2&=\{(a,0,b,c):2\le a,b,c\le m-1,
                              \ a+b+c=2m+1\}.
 \end{aligned}                                      \tag{5.1}

\]

Writing `(alpha,beta,gamma)=(m-a,m-b,m-c)` shows

\[
 |\mathcal H_1|=|\mathcal H_2|={m-2\choose2},\qquad
 |\mathcal H_1\cup\mathcal H_2|=(m-2)(m-3).         \tag{5.2}

### Lemma 3 (no hard target lies in one forced arm)

No member of (5.1) is the maximum of an interval internal to one forced
arm or to a refinement of one forced arm.

### Proof

Take `y=(0,a,b,c)` in `H_1`.  Its only rank-`2m` colours are

\[
                       z_2=y-e_2,\quad z_3=y-e_3,
                       \quad z_4=y-e_4.              \tag{5.3}

\]

The first two edges form the path

\[
                  z_2\ --_{p}\ z_3,
 \qquad p=(0,a-1,b-1,c),                             \tag{5.4}

\]

while the edge of colour `z_4` is vertex-disjoint from this path.  The
maximum of the path in (5.4) is `y`; the isolated edge has rank-`2m`
maximum and is not a witness.

At `p`, the first two positive coordinates are `2,3`, and both entries are
strictly below `m`.  The exact degree formula therefore gives

\[
                             \deg_{G_m}(p)=3.         \tag{5.5}

\]

Thus the two edges in (5.4) belong to different forced arms.  Any interval
with maximum `y` uses only letters below `y`, hence only edges of `G_m[y]`;
it cannot bypass (5.4) through a colour outside (5.3).  So no one arm
contains a witness.  Swapping coordinates `1,2` proves the same assertion
for `H_2`.  QED.

### 5.2 Constant seam congestion

Let `W` be any signed permutation of an edge-disjoint refinement of all
forced arms.  Every block has at least one selected edge, and every selected
edge occurs in exactly one block.

Suppose an interval of `W` has maximum `y` of rank `2m+1`.  Inside its arm
blocks it can traverse only selected edges whose colours are below `y`.
There are at most four such colours, namely `y-e_i` over the positive
coordinates of `y`.  Since the blocks are edge-disjoint, the interval
contains at most four within-block adjacencies.

If the interval meets `b` blocks, every one of its `b-2` strict interior
blocks contributes at least one within-block adjacency.  Hence

\[
                              b\le6.                 \tag{5.6}

\]

Choose one witness for every hard target and charge it to the leftmost seam
it crosses.  For a fixed seam, (5.6) leaves at most five choices for the
terminal block of a charged witness.

Fix one such terminal block.  As the left endpoint moves through the block
immediately before the charged seam, its suffix maxima form an inclusion
chain.  Every member has rank at least `2m-1` and at most `2m+1`; after
duplicates are deleted there is at most one member at each rank, hence at
most three members.  The terminal prefix maxima satisfy the same statement.
All complete intervening blocks are fixed.  Their maxima combined with the
two endpoint chains therefore produce at most

\[
                               3\cdot3=9              \tag{5.7}

\]

distinct rank-`2m+1` targets.

Thus at most `5*9=45` selected hard targets can be charged to one seam.
Lemma 3 and (5.2) prove:

### Theorem 4 (quadratic virtual-seam necessity)

Every edge-once signed forced-arm ordering covering the entire upper half
has at least

\[
                          {(m-2)(m-3)\over45}         \tag{5.8}

\]

distinct seams crossed by selected witnesses.

This is an architecture theorem, not a lower bound on arbitrary max words.
It also does not rule out the desired construction: the forced-arm word has
`2m^2+m+3` available seams.  It proves that the quadratic seam supply must
be used globally rather than treated as a negligible list of repairs.

## 6. Finite diagnostics

The script

```text
python3 scratch/check_virtual_seam_trace_stitching.py
```

rebuilds `G_m`, its forced arms and cut set, verifies the hard family, and
constructs bounded-depth path gadgets for `4<=m<=8`, `1<=q<=4`.

The separate exploratory signed-order search stores independently verified
full-upper orders for `m=2,3,4`:

```text
python3 scratch/search_virtual_seam_order.py 2 --verify-known
python3 scratch/search_virtual_seam_order.py 3 --verify-known
python3 scratch/search_virtual_seam_order.py 4 --verify-known
```

Their lengths are respectively `33`, `69`, and `125`, exactly
`|Z_m|+|A_m|`.  This supports, but of course does not prove, the pure
Virtual-Seam Excursion Lemma.

## 7. Correct next target

The bounded-depth proof appends one canonical path for every exceptional
pair `(surface vertex, deficit vector)`.  The full upper half fails only
because this repeats related traces separately.

The next theorem should therefore be a **kernel-cone trace-packing lemma**:

> For the `O(m^2)` vertices of `K_m^*`, pack the reverse-greedy paths for
> all upper targets whose canonical path first hits that vertex into one
> signed ordering of the forced arms, or into `O(1)` additional trace words
> per surface line, with total added length `O(m^2)` (or merely
> `o(m^3)`).

Theorem 4 says such a proof should deliberately use a quadratic family of
seams.  Theorem 2 says it only needs to replace the wasteful independent
path library by shared nested excursions.  Pure local transition pairing
is already refuted; a sparse exceptional-seam argument is now also ruled
out for the edge-once architecture.

