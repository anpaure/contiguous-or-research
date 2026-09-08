# Fixed-rotation ECO path backbones

Date: 2026-07-31  
Status: exact path master, literal positive certificates through paper
parameter `n=10`, and exact refutations of the terminal-only and global-phase
strengthenings; no all-`n` path theorem

## 0. Scope and verdict

Let `F_n` be the canonical Merino--Mička--Mütze factor in the middle-levels
graph on ground size `2n+1`.  Its components are indexed by free plane trees
with `n` edges.  Restrict to the fixed-coordinate coherent ECO atoms

\[
                 Z(D),\qquad D\in\mathcal D_{n-1},
\]

from `MATH_THEOREM_CATALAN_COHERENT_ECO_HEX_SUPPLY_20260731.md`.

The new conclusions are:

1. after the literal component-faithfulness filter, the mixed binary/ternary
   ECO skeleton admits a **component path** whose selected atoms are
   independent in the common physical-port/forced-owner collision forest for
   every `3<=n<=10`;
2. toggling each selected family literally Hamiltonizes `F_n` in all eight
   cases;
3. the attractive terminal-only strengthening is false already at `n=6`;
4. choosing one global parity of the collision forest is also false at the
   even cases `n=6,8`; the phase must be chosen separately on different
   collision paths; and
5. the all-`n` statement remains open.  Existing ordered-tree or free-plane-
   tree generators do not supply the exact quotient, 2/3-tile, collision-
   phase and physical-compatibility conditions proved necessary here.

The finite theorem is on the raw canonical factor.  Under the current
repair-after-glue architecture, it settles only the component topology and
physical Hamiltonization rows.  A final repair must still create the joint
alternating SDR and the owner/router/residence/deep-shadow/compiler state.

## 1. The exact path object

Let `V_n` be the component set of `F_n`.  For a fixed-rotation atom `t`, let

\[
                  S_t\subseteq V_n
\]

be the set of old factor components containing its three old matching edges.
Only supports of size two or three are relevant.

### Definition 1.1 (literal component faithfulness)

An atom is **faithful at the base state** when

\[
   c\bigl(F_n\triangle Z(t)\bigr)
       =c(F_n)-(|S_t|-1).                              \tag{1.1}
\]

For a three-touch atom this is the expected clean phase.  A two-touch atom
has a genuine phase: merely touching two components does not imply (1.1).
This filter is essential.  The first unfiltered `n=8` abstract path found by
the search failed the final literal replay for exactly this reason.

Let `Gamma_n` be the common collision graph of the fixed-rotation atoms.
The coherent-ECO theorem proves that its physical-port, lower-owner and
upper-owner versions coincide and form a path forest.

### Definition 1.2 (ECO path certificate)

An ECO path certificate consists of:

1. an ordering `v_1,...,v_q` of `V_n`;
2. a partition of the `q-1` path edges into intervals of one or two
   consecutive edges;
3. one faithful binary atom for every one-edge interval, with support
   `{v_i,v_(i+1)}`;
4. one faithful ternary atom for every two-edge interval, with support
   `{v_i,v_(i+1),v_(i+2)}` and declared middle `v_(i+1)`;
5. independence of all selected atoms in `Gamma_n`; and
6. the literal final replay

\[
        F_n\triangle\bigtriangleup_{t\in\mathcal S}Z(t)
              \quad\hbox{is one cycle}.               \tag{1.2}
\]

Condition 6 is retained explicitly.  Individual faithfulness and abstract
incidence-tree rank do not in general rule out an interleaving phase among
several physical toggles.

### Proposition 1.3 (fixed-path integrality)

For a fixed order `v_1,...,v_q` and any prefiltered mutually compatible atom
bank, selecting the binary/ternary tiles in items 2--4 is an integral unit-
flow problem.

#### Proof

Index the path edges by `1,...,q-1`.  A binary atom is an interval `[i,i]`
and a ternary atom is `[i,i+1]`.  Map `[a,b]` to the directed arc
`a-1 -> b` on nodes `0,...,q-1`.  Covering each path edge once is exactly one
unit of source--sink flow.  The node--arc matrix is totally unimodular.
This is Theorem 3.1 of
`MATH_AUDIT_AD_ECO_COMPONENT_TREE_TILING_AND_BRANCH_OBSTRUCTION_20260731.md`.
\(\square\)

Thus a path backbone removes the determinant-two branching obstruction.
What remains upstream is choosing the order and the collision-path phases;
what remains downstream is the literal replay (1.2).

## 2. Literal finite theorem

### Theorem 2.1

For every `3<=n<=10`, the fixed-rotation coherent-ECO bank contains an ECO
path certificate.

The exact census is:

| `n` | plane-tree components | faithful candidates | binary selected | ternary selected | atoms selected |
|---:|---:|---:|---:|---:|---:|
| 3 | 2 | 2 | 1 | 0 | 1 |
| 4 | 3 | 4 | 2 | 0 | 2 |
| 5 | 6 | 14 | 1 | 2 | 3 |
| 6 | 14 | 41 | 3 | 5 | 8 |
| 7 | 34 | 132 | 19 | 7 | 26 |
| 8 | 95 | 428 | 28 | 33 | 61 |
| 9 | 280 | 1430 | 87 | 96 | 183 |
| 10 | 854 | 4861 | 291 | 281 | 572 |

In every row

\[
             b+2t=|V_n|-1,                            \tag{2.1}
\]

the selected atoms have pairwise disjoint physical ports and forced-owner
resources, their supplied component edges are exactly one Hamilton path, and
the literal symmetric difference (1.2) is one Hamilton cycle.

#### Proof

The solver uses one choice variable for every binary atom and three
middle-choice variables for every ternary atom.  An `AddCircuit` constraint
with one dummy vertex forces the supplied ordinary edges to be a Hamilton
path; common-resource conflicts forbid adjacent atoms of `Gamma_n`.

This only proposes a certificate.  The independent audit discards the model
and reconstructs every selected atom from its Dyck word, verifies (1.1),
resource disjointness, the path-edge partition, equation (2.1), and finally
replays every physical symmetric difference and counts the resulting factor
components.  The result is one in all eight cases.  \(\square\)

## 3. Terminal atoms do not suffice

Write a parent word as

\[
                       D=1u0v.
\]

The common collision-path orientation is

\[
          1p\,10\,0v\longrightarrow1p\,0\,10v.        \tag{3.1}
\]

Call an atom terminal when it has no outgoing edge, equivalently when `u`
does not end in `10`.  Terminal atoms are automatically collision-independent.

### Theorem 3.1 (terminal-bank no-go)

At `n=6`, the terminal-bank component two-section has no Hamilton path.
Consequently it has no ECO path certificate.

#### Proof

There are fourteen plane-tree components and twenty-eight faithful terminal
atoms.  Delete the component with canonical contour key

\[
                         101010101100.                 \tag{3.2}
\]

The remaining two-section has three connected components of sizes

\[
                            1,2,10.                    \tag{3.3}
\]

For every graph with a Hamilton path and every vertex `x`, deleting `x`
leaves at most two components: remove `x` from the spanning path.  Equation
(3.3) contradicts this necessary condition. \(\square\)

So a proof cannot simply take all sinks (or, by reversal, all sources) of
the collision forest.

## 4. One global collision phase does not suffice

The collision forest has a canonical bipartition.  If `D=1u0v`, its parity
is the parity of the number of initial primitive peaks `10` in `v`; move
(3.1) changes it.

### Theorem 4.1 (global-phase no-go)

Neither fixed parity gives a component Hamilton path at `n=6`, and neither
does at `n=8`.

#### Proof

The following explicit cuts violate the Hamilton-path toughness inequality

\[
                       c(G-X)\le |X|+1.                \tag{4.1}
\]

| `n` | parity | deleted component keys | component sizes of `G-X` | `|X|+1` |
|---:|---:|---|---|---:|
| 6 | 0 | `101010101100` | `1,2,10` | 2 |
| 6 | 1 | none | `1,1,12` | 1 |
| 8 | 0 | `1010110011001100`, `1010101010101100` | `1,1,1,90` | 3 |
| 8 | 1 | none | `1,1,2,3,88` | 1 |

Every profile is reconstructed directly from the faithful fixed-rotation
atom supports. \(\square\)

By contrast, parity zero alone does contain literal certificates at the
audited odd values `n=5,7,9`.  This is evidence for an odd/even recursive
split, not an all-`n` theorem.  Even dimensions require a componentwise
choice of phases on different collision paths.

## 5. What known Gray codes do and do not give

Three nearby results should not be conflated with Theorem 2.1.

1. Sawada's generation of rooted and free plane trees lists every
   isomorphism class in constant amortized time, but the order is not an ECO
   path with the local tile and collision conditions above.
2. Pull Gray codes for ordered rooted trees operate on all Catalan rooted
   objects.  The components here are free plane trees, i.e. root-rotation
   classes, and a rooted Gray code does not descend to an orbit-transversal
   path with fixed-rotation independent parent atoms.
3. The MMM middle-levels proof supplies a component-spanning tree of standard
   leaf pulls.  A spanning tree is enough for cycle joining, but it is not a
   component path and retains the determinant-two mixed-tile obstruction.

Relevant primary references are:

* J. Sawada, *Generating rooted and free plane trees*, ACM Trans.
  Algorithms 2 (2006), 1--13;
* P. Lapey and A. Williams, *Pop & Push: Ordered Tree Iteration in
  O(1)-Time*, ISAAC 2022;
* A. Merino, A. Mička and T. Mütze, *On a combinatorial generation problem
  of Knuth*, J. ACM 71 (2024).

The exact missing combinatorial statement is therefore:

> **Fixed-rotation ECO path conjecture.**  For every `n`, choose one parity
> independently on each component of the collision path forest and choose
> faithful surviving binary/ternary atoms which tile a Hamilton path on the
> free plane trees, with a physically compatible simultaneous toggle.

This is strictly narrower than the earlier compatible-hypertree target: the
bare tile LP becomes integral.  It is also genuinely stronger than every
currently imported Gray-code theorem.

## 6. Reproduction and exact boundary

Search:

```text
python3 scratch/search_catalan_eco_path_backbone_cpsat_20260731.py N \
  --bank all --seconds 600 --workers 8 --output OUTPUT.json
```

Independent replay:

```text
python3 scratch/audit_catalan_eco_path_backbone_20260731.py
```

The replay output is

```text
scratch/catalan_eco_path_backbone_20260731.audit.json
```

Proved:

1. the exact fixed-path unit-flow reduction;
2. literal path-backbone witnesses through `n=10`;
3. the terminal-bank `n=6` no-go; and
4. the global-parity `n=6,8` no-go.

Open:

1. an all-`n` ECO component path;
2. a closed-form collision-path phase rule;
3. an all-`n` physical noninterleaving proof for the selected tiles; and
4. after Hamiltonization, the final repair that creates the joint
   alternating SDR and all downstream protected state.

