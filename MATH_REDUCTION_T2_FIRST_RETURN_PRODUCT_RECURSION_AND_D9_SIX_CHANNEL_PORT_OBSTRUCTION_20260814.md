# The frozen `D5` suffix tree has an all-`s` first-return recurrence, but its fixed zigzag port defeats every finite endpoint-phase bank

**Date:** 2026-08-14

**Status:** exact symbolic suffix-topology theorem and exact terminal-resource
obstruction.  The 41-edge `D5` label tree is the `s=5` instance of an
all-semilength first-return product recurrence seeded by the frozen `D3/D4`
trees.  The recurrence always gives a spanning tree on `D_s`.  Its canonical
zigzag split port has degree `s-2`, however, so an owner-disjoint bank of
circuits anchored at the six changed `T2` prefix owners is impossible from
`D_9` onward (and the four phases used by the frozen `D5` solution already
fail from `D_7` onward).  A finite number of extra endpoint phases cannot
repair this fixed-port recurrence.  This is not a suffix-topology no-go:
the Proskurowski--Ruskey transposition Hamilton path has maximum degree two
at every semilength.  Thus one may either rotate the product-tree ports
inside the large canonical matchings between consecutive first-return
blocks, or discard this product-tree specialization and use the Hamilton
path.  In either case the remaining theorem is a fresh, non-conjugate
actuator/resource compiler.  No rotating-port SDR or all-`s` q2-safe
actuator compiler is claimed here.

## 0. Outcome

Write a Dyck word in first-return form

\[
                         X=1U0V,
 \qquad |U|=i,\quad |V|=j,\quad i+j=s-1.             \tag{0.1}
\]

Let

\[
 P_r=1^r0^r,
 \qquad
 Q_r=(10)^r                                                   \tag{0.2}
\]

be the mountain and zigzag roots.  Given suffix trees `T_i` on `D_i`, the
following three constructors build `T_s`.

1. In every fixed right fibre `V in D_j`, put a copy of `T_i` on `U`.
2. At the mountain reset root `U=P_i`, put one copy of `T_j` on `V`.
3. Join consecutive split blocks by the zigzag edge

   \[
   1Q_i0Q_j
      \longleftrightarrow
   1Q_{i+1}0Q_{j-1},
   \qquad j\ge1.                                      \tag{0.3}
   \]

For `s=5`, using the frozen `T_3,T_4`, this gives exactly

```text
26 child_D4 edges
 8 child_D3 edges
 3 child_D2 edges
 4 consecutive-split bridges,
```

and the four bridges are exactly those in the frozen `D5` theorem.

This solves the suffix-label topology recursively, but not the actuator
recursion.  Indeed the vertex `Q_s` inherits all incidences of `Q_(s-1)` in
the split-zero child copy and receives one new split bridge.  Hence

\[
                    \deg_{T_s}(Q_s)=s-2                         \tag{0.4}
\]

for the frozen `D3/D4` seeds and every `s>=3`.  Every endpoint-anchored
actuator incident with `Q_s` consumes one of the distinguished prefix-owner
ports over `Q_s`.  Pairwise owner-disjointness therefore needs at least
`s-2` prefix channels.  There are only six changed `T2` prefix owners, so
the canonical recurrence has the unconditional cut

\[
        \boxed{s=9:\quad \deg(Q_9)=7>6.}                       \tag{0.5}
\]

The cut occurs before auxiliary-resource, q2-support, component-action, or
residence constraints are imposed.

It is only a cut on the fixed-zigzag product recurrence.  The classical
Proskurowski--Ruskey theorem supplies a Hamilton path in the full Dyck
transposition graph, and hence an abstract suffix tree of maximum degree
two for every `s`.  Endpoint channel colouring is therefore trivial after
changing the label tree.  What remains nontrivial is assigning compatible
post-`T2` alternating circuits to that bounded-degree path: already at
`D_4`, the shortest candidates in the two productive channels on the
standard path have no pairwise resource-disjoint transversal.

There is nevertheless a large exact aperture for a possible rotating-port
escape.  Between split blocks
`(i,j)` and `(i+1,j-1)` lies the canonical matching

\[
 \mathcal M_{i,j}
 =\left\{
  1U010W\longleftrightarrow1U100W:
  U\in\mathcal D_i,\ W\in\mathcal D_{j-1}
  \right\},                                               \tag{0.6}
\]

of size

\[
                     |\mathcal M_{i,j}|
        =\operatorname {Cat}_i\operatorname {Cat}_{j-1}.     \tag{0.7}
\]

The frozen choice `(0.3)` is only the member `U=Q_i,W=Q_(j-1)`.
Rotating among `(0.6)` is therefore the exact candidate aperture for
escaping the growing hub.  A globally bounded-load choice across all
recursive blocks is not proved here.

Every edge in `(0.6)` has the same intrinsic MSW four-rank signature.  If
`p=2i+2` is the entering coordinate and `q=2i+3` the leaving coordinate,
and the left endpoint is `x=1U010W`, the right endpoint
`y=1U100W`, then

\[
 \boxed{
 d_x(q)=i+2,
 \quad i_x(p)=1,
 \quad d_y(p)=1,
 \quad i_y(q)=2.}                                      \tag{0.8}
\]

Thus the cross-split terminal has one affine counter and one fixed
orientation state; its signature is independent of the actual `U,W` used
to rotate the port.  This is the precise finite-control interface left to an
actuator compiler.

## 1. The exact first-return product tree

Let `C_r=|D_r|=Cat_r`.  For `i+j=s-1`, let

\[
 \mathcal B_{i,j}
 =\{N(U,V):U\in\mathcal D_i, V\in\mathcal D_j\},
 \qquad
 w(N(U,V))=1w(U)0w(V).                                 \tag{1.1}
\]

Assume inductively that `T_r` is a transposition tree on `D_r` for every
`r<s`.  Inside `B_(i,j)` put

\[
\begin{aligned}
 E^L_{i,j}
   &=\{N(U,V)N(U',V):UU'\in E(T_i),\ V\in\mathcal D_j\},\\
 E^R_{i,j}
   &=\{N(P_i,V)N(P_i,V'):VV'\in E(T_j)\}.
                                                               \tag{1.2}
\end{aligned}
\]

Finally, for `0<=i<=s-2`, put `j=s-1-i` and add

\[
 B_{i,j}=N(Q_i,Q_j)N(Q_{i+1},Q_{j-1}).               \tag{1.3}
\]

### Theorem 1.1 (all-`s` suffix-label recurrence)

The union of `(1.2)` and `(1.3)` is a spanning tree `T_s` of the Dyck
transposition graph.

#### Proof

For fixed `V`, the `E^L` edges connect the `U` fibre.  The single `T_j`
copy in `E^R`, at `U=P_i`, connects all these fibres.  Hence the graph
inside `B_(i,j)` is connected.  Its edge count is

\[
 C_j(C_i-1)+(C_j-1)=C_iC_j-1,                         \tag{1.4}
\]

so it is a tree.

The edge `(1.3)` joins block `(i,j)` to block `(i+1,j-1)`.  These `s-1`
edges make the quotient on the `s` split blocks a path.  Consequently the
whole graph is connected, and its number of edges is

\[
 \sum_{i+j=s-1}(C_iC_j-1)+(s-1)
 =C_s-s+s-1=C_s-1.                                   \tag{1.5}
\]

It remains only to check transposition adjacency.  Child edges in `(1.2)`
retain the two differing child coordinates.  For `(1.3)`, write

\[
\begin{aligned}
 N(Q_i,Q_j)&=1Q_i0\,10\,Q_{j-1},\\
 N(Q_{i+1},Q_{j-1})&=1Q_i\,10\,0Q_{j-1}.
                                                               \tag{1.6}
\end{aligned}
\]

The words differ only in positions `2i+2,2i+3`, one `0/1` exchange.
Thus every displayed edge belongs to the Dyck transposition graph. \(\square\)

### Corollary 1.2 (the frozen `D5` tree is the first nontrivial instance)

Seed `(1.2)` with the frozen four-edge `T_3`, thirteen-edge `T_4`, and the
unique one-edge `T_2`.  At `s=5`, the five split blocks contribute

\[
 13,\ 4,\ 3,\ 4,\ 13
\]

internal edges.  The four edges `(1.3)` are

```text
1010101010 -- 1100101010
1100101010 -- 1101001010
1101001010 -- 1101010010
1101010010 -- 1101010100.
```

These are exactly the role counts and split bridges frozen in
`MATH_THEOREM_T2_D5_FIRST_RETURN_RESET_PHASE_SPANNING_ACTUATOR_AND_RESIDENCE_OBSTRUCTION_20260814.md`.

This identification is label-topological.  It does not transport any of
the frozen circuits through the contexts in `(1.2)`.

## 2. The growing zigzag-port obstruction

### Lemma 2.1 (exact zigzag degree)

For the frozen `T_3,T_4` seeds and recurrence `(1.2)--(1.3)`,

\[
                         \deg_{T_s}(Q_s)=s-2
 \qquad(s\ge3).                                      \tag{2.1}
\]

#### Proof

The frozen degrees are

\[
                         \deg_{T_3}(Q_3)=1,
 \qquad                  \deg_{T_4}(Q_4)=2.          \tag{2.2}
\]

For `s>=5`, the word

\[
                    Q_s=N(P_0,Q_{s-1})=10Q_{s-1}     \tag{2.3}
\]

lies in the split-zero block.  Its internal incidences are precisely the
copy of the incidences of `Q_(s-1)` supplied by `E^R_(0,s-1)`.  There are
no left-child incidences because `T_0` is empty.  Exactly one split bridge,
`B_(0,s-1)`, is incident with `Q_s`; every other bridge has a different
split type.  Therefore

\[
                 \deg_{T_s}(Q_s)
                  =\deg_{T_{s-1}}(Q_{s-1})+1.        \tag{2.4}
\]

Equations `(2.2)--(2.4)` prove `(2.1)`. \(\square\)

### Theorem 2.2 (finite endpoint-phase no-go for the fixed port)

Let an endpoint-anchored suffix actuator for an edge `XY` contain, over
each endpoint, one distinguished owner from a bank of `k` prefix channels.
If all selected actuator owner sets are pairwise disjoint, then every
suffix vertex has degree at most `k`.

Consequently, the fixed-zigzag recurrence cannot be realized by any fixed
finite endpoint-channel bank at all semilengths.  With the actual six
changed `T2` prefix owners it fails by `s=9`; with only the four phases used
in the frozen `D5` selection it fails by `s=7`.

#### Proof

Two tree edges incident with the same suffix root `X` cannot use the same
prefix owner over `X`, because their circuits would share that owner.
Thus the channel labels on incident edges are distinct.  In particular
`deg(X)<=k`.  Applying Lemma 2.1 gives the threshold `s-2>k`. \(\square\)

The theorem permits different channels at the two ends of a circuit; the
pigeonhole argument is local to one suffix endpoint.  It also grants
perfect auxiliary-resource separation and perfect q2/topology behavior.
The failure is therefore an endpoint-owner cut, not a SAT artefact.

The scope is equally important.  It does not obstruct a different suffix
tree, a circuit that does not consume a distinguished endpoint owner, or a
recurrence that rotates its split bridge among different suffix roots.

In particular, this theorem does not contradict the Proskurowski--Ruskey
Hamilton path.  That path is an unconditional degree-two escape at the
suffix-label level.  The fixed product tree is retained because it exposes
the first-return composition laws underlying the frozen `D5` construction,
not because it is the only spanning topology.

## 3. The rotating bridge aperture and its exact state

Fix `i+j=s-1` with `j>=1`.  For `U in D_i` and `W in D_(j-1)`, define

\[
\begin{aligned}
 x(U,W)&=1U0\,10W,\\
 y(U,W)&=1U\,10\,0W.                                \tag{3.1}
\end{aligned}
\]

The first word has split `(i,j)` and the second split `(i+1,j-1)`.

### Lemma 3.1 (canonical cross-split matching)

The edges `x(U,W)y(U,W)` form a matching of size
`Cat_i Cat_(j-1)` between the two consecutive split blocks.

#### Proof

The words in `(3.1)` differ only at coordinates

\[
                         p=2i+2,
 \qquad                  q=2i+3,                    \tag{3.2}
\]

where `x_p=0,x_q=1` and `y_p=1,y_q=0`.  Both words are Dyck by their
displayed first-return decompositions.  Either endpoint uniquely recovers
`U,W`, so no endpoint occurs twice.  Counting the two independent Dyck
choices proves the formula. \(\square\)

This matching is not asserted to be the complete Johnson interface.  For
example, additional long transpositions already occur between the middle
blocks of `D_3`.  Only the matching `(3.1)` is needed for the rotating-port
escape.

### Lemma 3.2 (exact bridge rank signature)

Let `I(z),D(z)` be the MSW insertion and deletion orders of a Dyck word
`z`.  For every edge `(3.1)`, the four ranks are exactly `(0.8)`.

#### Proof

Use the first-return formula

\[
 \rho(1u0v)
  =(a,\ a-\rho(\mu u),\ 1,\ a+\rho(v)),
 \qquad a=\operatorname{length}(u)+2,               \tag{3.3}
\]

and the Dyck concatenation law.  In `x`, the coordinate `p=2i+2` is the
closing coordinate `a` of the first primitive factor, hence it is the
first insertion.  That factor has `i+1` deletions; `q` is the first upstep
of the following `10`, so it is deletion number `i+2`.  This gives

\[
                         i_x(p)=1,
 \qquad                  d_x(q)=i+2.                 \tag{3.4}
\]

For `y`, the primitive interior is `U10`.  Reverse-complement reverses the
factor order and fixes `10`, so

\[
                   \mu(U10)=10\mu(U),
 \qquad
 \rho(10\mu(U))=(2,1,2+\rho(\mu U)).                \tag{3.5}
\]

In `(3.3)` for `y`, the image of the leading `2` in `(3.5)` is `p` and
occupies the first deletion position; the image of `1` is `q` and occupies
the second insertion position.  Thus

\[
                         d_y(p)=1,
 \qquad                  i_y(q)=2.                   \tag{3.6}
\]

Equations `(3.4)--(3.6)` prove the claim. \(\square\)

The state transition under `i -> i+1` is therefore the affine law

\[
              (i+2,1,1,2)\longmapsto(i+3,1,1,2).     \tag{3.7}
\]

Finite control is enough, provided the split size is retained as an
external counter.  A strictly finite table of absolute ranks is not enough.

As a separate stem-core diagnostic, for any aperture `h>=1` the forward
sign is impossible because `d_y(p)=1`.  The reverse sign is safe exactly
when `s-h>=2`, because its two insertion ranks are `1,2`.  This statement
uses the intrinsic MSW rank criterion; it is not a claim about the q2
support current of a post-`T2` alternating circuit.

## 4. Exact inductive interface and remaining gate

At suffix-label level, only the following finite control is needed.

| state/constructor | exact role | composition law |
|---|---|---|
| `P` | mountain reset anchor for the one right-child copy | `P_(r+1)=1P_r0` |
| `Q` | canonical cross-split port | `Q_(r+1)=10Q_r` |
| `L` | child-tree edge in every fixed right fibre | `UU' -> 1U0V -- 1U'0V` |
| `R` | right-child edge at `U=P_i` | `VV' -> 1P_i0V -- 1P_i0V'` |
| `B` | consecutive-split bridge | choose one edge of `M_(i,j)` |

The frozen `D5` tree used the fixed `Q` choice in the last row.  Theorem
2.2 proves that this exact two-anchor specialization cannot be the all-`s`
actuator grammar.

A sufficient actuator-level state must additionally record, for every
selected circuit `C_e`,

\[
 \operatorname{sig}(C_e)=
 \bigl(c_e,
       O_e^\circ,
       R_e^\circ,
       \Delta_e^{(2)},
       \pi_e\bigr),                                  \tag{4.1}
\]

where `c_e` is its endpoint channel, `O_e^circ` and `R_e^circ` are its
nonterminal owner and q1-colour resources, `Delta_e^(2)` is its exact q2
current, and `pi_e` is its permutation on touched lifted components.  The
following conditions are sufficient and are exactly what the finite `D5`
verifier checked:

1. endpoint channels are proper at every suffix root;
2. all `O_e^circ` and `R_e^circ`, together with the terminal ports, are
   pairwise disjoint;
3. the sum of the q2 currents leaves every old target with load at least
   one; and
4. the product of the `pi_e` has one orbit on the touched components.

The coordinate-conjugation obstruction proves that `(4.1)` cannot be
obtained by blindly transporting the frozen `D3/D4` circuits through `L`
or `R`.  Fresh reset menus are required.

A closed local reset cycle is not, by itself, such a compiler.  The needed
operation is a **cut-open substitution functor**: it must expose the two
boundary darts of the child incidence, graft them to the prescribed target
successor heads, and prove that suppressing the inserted owners recovers
exactly the intended source/target factor wiring.  In addition, its owner
and q1 palettes must remain disjoint after all recursive substitutions, and
its boundary monodromy must compose to the permutation `pi_e` in `(4.1)`.
Without these statements a resident closed package is only a local
monodromy atom, not an all-`s` reset transition.

There are consequently two exact topology routes.

1. **Product-tree route:** choose cross-split ports from the matchings
   `M_(i,j)` and, if needed, choose the right-fibre reset anchors adaptively,
   so the recursive terminal degree remains at most six.  Existence of such
   a jointly rotating assignment inside this particular recurrence is open.
2. **Hamilton-path route:** use the Proskurowski--Ruskey transposition path,
   which already has maximum degree two.  No further suffix-label theorem is
   needed, but its edges still need fresh circuit menus and a global
   resource/q2/topology selection.  The frozen `D4` shortest-menu failure
   shows that bounded terminal degree alone does not supply that selection.

The all-semilength actuator gate is therefore

\[
 \boxed{\begin{array}{c}
 \text{fix any bounded-degree all-}s\text{ suffix tree (for example the}
 \text{ Proskurowski--Ruskey path), and}\\
 \text{prove a finite affine-state fresh-reset compiler whose}
 \ (4.1)\text{ signatures satisfy conditions 1--4.}
 \end{array}}                                             \tag{4.2}
\]

Solving the optional rotating-port problem would retain the exact frozen-D5
first-return recurrence, but it is not necessary for abstract bounded-degree
topology.  Conversely, importing the Hamilton path removes only the endpoint
degree cut; it does not prove auxiliary-resource disjointness, q2 support, or
one-orbit component action.

## 5. H100 verifier

The independent script

```text
scratch/verify_t2_suffix_first_return_recursion_and_channel_obstruction_20260814.py
```

checks through `D_9` that:

* the recurrence has `Cat_s-1` distinct transposition edges and is
  connected;
* the `D5` role census and four frozen bridges are reproduced exactly;
* `deg(Q_s)=s-2`, with degrees six and seven at `s=8,9`;
* every canonical interface matching through `D_8` has size `(0.7)` and
  no repeated endpoint; and
* every enumerated bridge has the symbolic rank signature `(0.8)`.

All substantive execution and all hashes are run through SSH on H100.
