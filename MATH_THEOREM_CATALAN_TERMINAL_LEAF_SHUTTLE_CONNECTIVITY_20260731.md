# The terminal leaf-shuttle theorem for fixed-rotation ECO atoms

Date: 2026-07-31  
Status: exact all-dimension component-connectivity theorem; no disjoint
hypertree, simultaneous-toggle, decoration, router, residence, shadow,
voltage, or compiler theorem

## 0. The theorem

Use the paper parameter `n`.  The canonical middle-levels factor has one
component for each unrooted plane tree with `n` edges.  A fixed-rotation ECO
parent is

\[
                         D=1u0v\in\mathcal D_{n-1}.
\]

Retain it when `u` is empty or does not end in the primitive leaf `10`.
These are exactly the terminal vertices of the common collision forest

\[
                    1p100v\longrightarrow1p010v.                  \tag{0.1}
\]

### Theorem 0.1 (terminal ECO connectivity)

For every `n>=2`, the component-hypergraph two-section of the retained
fixed-rotation ECO bank is connected.  In fact only its first two old-edge
roles are needed: the graph

\[
       [1u100v]\;--\;[1u010v],\qquad
       u=\varnothing\text{ or }u\not\equiv *10                    \tag{0.2}
\]

is connected on the `n`-edge unrooted plane trees.

The proof is local.  Every leaf pull deleted by (0.1) is the conjugate of a
terminal pull by one or two terminal pulls.  Thus it has a replacement path
of length three or five.

## 1. Safe pulls

Give a plane tree its cyclic neighbour order.  Let `x` be a leaf incident
with `p`, and let `z` be the neighbour immediately after `x` around `p`.
Delete `x`.  If the neighbour immediately before `z` at `p` is absent or is
not a leaf, call the pull of `x` across `pz` **safe**.  It moves `x` from the
corner immediately before `z` at `p` to the corner immediately after `p` at
`z`.  The inverse move is the same safe ECO edge.

If the rooted contour of the tree with `x` deleted is `D=1u0v`, the two
ends of this move have contour representatives

\[
                         1u100v,\qquad1u010v.                      \tag{1.1}

The pull is safe exactly when `u` is empty or does not end in `10`.
Therefore safe pulls are precisely the edges (0.2).

Without the safety restriction, these are all elementary plane-tree leaf
pulls.  Every standard MMM auxiliary adjacency is such a pull: delete its
distinguished moved leaf and root the remaining tree at the oriented edge
crossed by that leaf.  Hence the unrestricted pull graph contains the
connected standard MMM auxiliary graph.

It remains only to replace every unsafe pull by safe ones.

## 2. The leaf-shuttle lemma

### Lemma 2.1 (three/five-pull replacement)

Let `x` be an unsafe leaf to be pulled from `p` across `pz`.  In the tree
with `x` deleted, write the cyclic order at `p` locally as

\[
                         \ldots,a,b,z,\ldots,                      \tag{2.1}

where `b` is a leaf; `b` is the blocker.  Then the unsafe pull of `x` has a
label-preserving replacement by either three or five safe pulls.  Every
vertex and every cyclic order outside the displayed local neighbourhood is
fixed.

#### Proof

Temporarily move `b` off `p`, perform the now-safe pull of `x`, and undo the
temporary moves.

First inspect the corner of `a` facing `p`.

1. **The `a`-corner is terminal.**  This includes the case where `a` is a
   leaf.  Pull `b` from its root-side corner at `p` into the child-side
   corner at `a`.  This is safe by the terminal hypothesis.  The vertex `a`
   is now a nonleaf immediately before `z` at `p`, so pull `x` across `pz`
   safely, then undo the pull of `b`.  This is the three-pull word

   \[
                             R\,X\,R^{-1}.                         \tag{2.2}
   \]

2. **The `a`-corner is nonterminal.**  Let `c` be the leaf immediately
   before `p` at `a`, and let `d` be the neighbour immediately before `c`.

   * If `d` is a leaf distinct from `p`, pull `c` into `d`.  This move is
     safe because `d` had no child-side predecessor.  The vertex `d` is now
     nonleaf, so the corner at `a` facing `p` is terminal.  Pull `b` into
     `a`.
   * If `d=p` or `d` is a nonleaf, pull `c` out across `ap`.  This is safe:
     after deleting `c`, its predecessor is absent or is the nonleaf `d`.
     The leaf `c` lands between `a` and `b` at `p`.  Pull `b` into `c`, which
     is safe because `c` was a leaf.

   In either subcase, two safe pulls have replaced the blocker `b` by a
   nonleaf immediately before `z`.  Pull `x` across `pz`, then undo the two
   preparatory pulls in reverse order.  This is

   \[
                         R_1R_2\,X\,R_2^{-1}R_1^{-1}.              \tag{2.3}
   \]

All inverse moves use the same terminal ECO atoms.  The central move changes
only the two corners of `pz`; it does not change the child-side terminal
certificate of either preparatory atom.  Direct inspection of the cyclic
orders shows that (2.2) and (2.3) end at exactly the labelled target of the
original unsafe pull.  No outside branch moves.  \(\square\)

The two cases are exhaustive.  In particular, the apparent recursive
problem stops after one level: if the last child `c` blocks entry into `a`,
then either its predecessor is a leaf, which can absorb `c` for free, or its
predecessor is already the nonleaf certificate needed to export `c`.

For `n=3,4`, the few degenerate bare-leaf cases are immediate under
unrooted plane isomorphism (or one terminal edge).  Lemma 2.1 applies
literally with fixed vertex labels from `n=5` onward.

## 3. Proof of Theorem 0.1

Take the connected unrestricted plane-tree leaf-pull graph.  If one of its
edges is safe, it belongs to (0.2).  If it is unsafe, Lemma 2.1 replaces it
by a path of safe pulls.  Replacing every edge of a standard MMM spanning
tree in this way gives a walk-connected spanning subgraph of (0.2).
Therefore (0.2), and hence the retained ECO component two-section, is
connected for every `n`.  \(\square\)

This replacement proves connectivity, not a conflict-free spanning tree:
different replacement paths may reuse the same physical vertices.  It also
does not assert that selecting the corresponding hexagons simultaneously
Hamiltonizes the factor.  Those are separate incidence-hypertree and
physical-support questions.

## 4. Exact census and audit

The number of unsafe parents is

\[
                         \operatorname{Cat}_{n-2},                 \tag{4.1}

because they are `D=1p100v` with `p,v` of total semilength `n-3`.
The deterministic shuttle has the exact finite census

\[
\begin{array}{c|c|c}
n&\text{three-pull}&\text{five-pull}\\ \hline
5&3&2\\
6&9&5\\
7&28&14\\
8&90&42\\
9&297&132\\
10&1001&429\\
11&3432&1430\\
12&11934&4862
\end{array}                                                        \tag{4.2}

Thus in these rows the five-pull case has size
`Cat_(n-3)` and the three-pull case has size
`Cat_(n-2)-Cat_(n-3)`.  The count is calibration; Theorem 0.1 uses only the
local exhaustive case split in Lemma 2.1.

Run

```text
python3 scratch/audit_catalan_terminal_leaf_shuttle_20260731.py
```

The script does no search.  It reconstructs each blocked labelled source,
applies the case split in Lemma 2.1, verifies terminality before every pull,
and checks equality with the labelled target after the third or fifth pull.
Its output is

```text
scratch/catalan_terminal_leaf_shuttle_20260731.audit.json
```

The earlier connectivity audit

```text
scratch/audit_catalan_terminal_eco_component_connectivity_20260731.py
```

independently unions only the retained two-role edges and finds one
component through `n=12`.

## 5. Relation to the current central target

This theorem closes a physical component-supply question.  Under the newer
minimal central reduction, Hamilton connectivity is not required: a
globally palette-bijective, componentwise alternating decorated two-factor
already yields the perfect diamond matching and Catalan path forest.  Thus
Theorem 0.1 is now optional for minimal Catalan Linear Matching existence.

It remains useful for the stronger Hamilton/post-glue architecture.  It
does not preserve a chosen alternating SDR or transparent decoration, and
it does not solve pairwise physical disjointness.  If decoration is carried
through the glue, the exact joint-alternating-SDR and transparent-gluing-tree
conditions must still be imposed.  If decoration is repaired after glue,
those conditions are deliberately deferred.
