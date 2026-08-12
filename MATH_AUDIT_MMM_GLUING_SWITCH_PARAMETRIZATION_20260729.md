# Audit of the Merino--Mička--Mütze gluing/switch family

## 0. Verdict

The released generator is essentially canonical.  For fixed `n`, desired
unit shift, and starting vertex, it does **not** search over Hamilton cycles:
it uses one deterministic plane-tree spanning tree and a deterministic list
of at most two voltage switches.  Changing the desired shift only applies a
coordinate multiplier, and changing the starting vertex only changes the
point at which the same cycle is read.

The proof contains a substantially larger family that the program does not
expose.  It can be parameterized exactly by gluing cycles in the auxiliary
multigraph on plane trees, followed by parallel-edge choices in the necklace
graph.  Every member preserves the strict quotient structure and the perfect
lower `q=1` rainbow.

For `k=15` this gives a useful, much smaller search lane:

* 34 plane-tree cycles in the initial cycle factor;
* 131 labeled gluing edges, on 81 underlying plane-tree pairs;
* choose 33 labeled edges forming a compatible spanning tree;
* at most 14 binary parallel-edge/switch choices;
* connectivity of the resulting necklace order is supplied by the gluing
  tree, rather than by an `AddCircuit` constraint on 429 lower-orbit choices.

However, exhaustive calibration at `k=11` shows that this family is still too
rigid for the known optimal carrier: among **all** labeled gluing spanning
trees whose simultaneous switch is Hamiltonian, all parallel-edge label
choices, and all unit-voltage lifts, the smallest number of forbidden short
coordinate runs is 143.  The known exact carrier has 0.  Thus the published
MMM family is a useful structured neighborhood, but it is not by itself a
uniform construction of the words in this project.

Primary sources:

* Merino--Mička--Mütze, *On a combinatorial generation problem of Knuth*,
  [arXiv:2007.07164](https://arxiv.org/abs/2007.07164), especially Sections
  3--8.
* The authors' released GNU-GPL C++ implementation, linked from
  [the Combinatorial Object Server](https://www.combos.org/middle).

No GPL source has been copied into this repository.  The audit script
[`scratch/extract_mmm_gluing_family.py`](scratch/extract_mmm_gluing_family.py)
is an independent implementation of the mathematical definitions needed for
small quotient enumeration.

## 1. Notation and the fixed base factor

Use the paper's parameter `n`, so the ground-set size in this project is

\[
                 k=2n+1.
\]

Let `A_n` and `B_n` be the binary strings of length `k` of weights `n` and
`n+1`, respectively.  Quotienting the middle-levels graph by cyclic rotation
gives the necklace graph `N_n`.

The paper defines a rotation-equivariant bijection `f` on `A_n union B_n`.
Its orbits give a cycle factor `F_n` in `N_n`.  The cycles of `F_n` are in
bijection with plane trees with `n` edges.  This base factor is fixed; there
is no choice in `f` in the paper or in the released program.

For `n=7` (`k=15`):

\[
 C_7=429\quad\hbox{central necklace classes per shore},
 \qquad |\mathcal F_7|=34\quad\hbox{plane-tree cycles}.
\]

## 2. The exact gluing variables

### 2.1 One labeled gluing operation

A gluing pair is

\[
 x=110u0v,\qquad y=101u0v,
\]

with `u,v` Dyck words, excluding the exceptional star pair.  It defines a
6-cycle `C(x,y)` in the middle-levels graph.  In the necklace graph, taking
the symmetric difference with this 6-cycle replaces three factor edges by
the other three edges.  When `[x]` and `[y]` index two distinct cycles of the
current factor, this joins them.

The auxiliary multigraph `H_n` has one vertex for each plane tree and one
labeled arc `([x],[y])` for each gluing pair.  A labeled spanning tree in
`H_n`, subject to the compatibility condition in the paper, gives a single
Hamilton cycle in `N_n`.

The resulting edge set has the exact form

\[
 E(z)=E(\mathcal F_n)\mathbin\triangle
      \bigtriangleup_{g} z_g E(C_g),                 \tag{2.1}
\]

where `z_g` selects gluing labels.  A solver formulation may use:

1. one Boolean `z_g` per labeled gluing pair;
2. at most one label for each underlying plane-tree pair;
3. exactly `|T_n|-1` selected labels;
4. graphic-matroid connectivity (a flow or lazy cut formulation);
5. the explicit interleaving conflict from Proposition 8(ii), if one wants
   the paper's inductive traversal proof rather than merely testing (2.1).

Nesting is allowed.  It changes orientation signs and voltage accounting,
not the vertex set of the quotient Hamilton cycle.

### 2.2 An automatic independent subfamily

The first spanning-tree construction in the paper gives an especially clean
subfamily.  For every non-star plane tree `T`, independently choose a gluing
pair directed to a plane tree of potential `phi(T)-1`, with the pullable
root satisfying the paper's non-leaf condition.  Since potential decreases
strictly and every non-star has one outgoing choice, the selected arcs form
an arborescence to the star automatically.  Connectivity therefore costs no
SAT variables or cuts.

The exact `k=15` menu is:

| domain size | number of plane-tree variables |
|---:|---:|
| 1 | 7 |
| 2 | 19 |
| 3 | 7 |

There are 33 variables, 66 options in total, and

\[
 \log_2 |\mathcal A_7|
   =19+7\log_2 3
   =30.0947375\ldots .                              \tag{2.2}
\]

For comparison, the full `k=15` auxiliary multigraph has 131 labels on 81
underlying pairs; their label multiplicities are

\[
                  1^{37},\ 2^{41},\ 4^3.
\]

This is the broadest natural MMM gluing-tree search, whereas (2.2) is the
connectivity-free subfamily.

## 3. The exact switch variables

A switch in the paper is a pair of parallel necklace-graph edges: the same
lower and upper necklace classes are joined by two different physical edge
orbits.  Replacing one by the other:

* leaves the necklace order unchanged;
* changes its voltage;
* changes the physical phase after that edge;
* therefore may change residence and higher shadows after lifting.

The paper classifies all switches (up to cyclic rotation and reversal).  A
maximal solver parametrization need not special-case `tau_(n,d,z)`: group all
central edge orbits by their pair of necklace endpoints and expose a label
choice whenever a selected quotient edge lies in a non-singleton group.

For `k=15`, the entire central quotient incidence graph has

\[
 3404\text{ singleton endpoint pairs},\qquad
 14\text{ double endpoint pairs}.                  \tag{3.1}
\]

Thus a fixed quotient cycle has at most 14 binary switch variables.  If its
oriented edge voltages are `delta_e`, its lift is one strict spiral precisely
when

\[
              \gcd\!\left(\sum_e\delta_e,15\right)=1. \tag{3.2}
\]

The paper proves that its canonical switches `tau_(n,1)` and `tau_(n,2)`
remain usable for any chosen gluing set.  For `n=7`, one or both always make
the total voltage a unit modulo 15.  Consequently composite `k=15` causes no
existence obstruction; it only requires the unit condition (3.2), not the
incorrect prime-only test `voltage != 0`.

## 4. Why lower `q=1` is automatic

Every Hamilton cycle in `N_n` with unit voltage lifts to a Hamilton cycle of
the full middle-levels graph.  Project this lifted cycle onto its upper shore,
obtaining the rank-`n+1` carrier `T`.

Between every two consecutive upper vertices lies exactly one lower vertex,
and every lower vertex occurs once in the middle-levels Hamilton cycle.
Therefore

\[
     \{T_i\cap T_{i+1}:i\}=\binom{[k]}n
\]

with multiplicity one.  Both the gluing variables and all parallel-edge
switches preserve this property.  This is the precise sense in which the MMM
family gives a strict spiral and a perfect `q=1` lower rainbow for free.

## 5. How the remaining objectives depend on the variables

### 5.1 Upper `q=1` is local and should be eager

At a representative lower necklace `L`, let its two selected physical upper
neighbors be

\[
                  L+a,\qquad L+b.
\]

The upper `q=1` colour is simply

\[
                  L+\{a,b\}.                        \tag{5.1}
\]

Thus upper-`q=1` orbit coverage is an exact local coverage constraint on the
gluing and parallel-edge variables.  A gluing 6-cycle changes only three
factor incidences; a parallel-edge switch changes one.  Equation (5.1) can be
encoded eagerly without reconstructing the full physical spiral.

### 5.2 Voltage labels determine the physical lift

Fix representatives of the quotient vertices.  Traversing a selected edge
adds its voltage `delta_e` to the current sheet.  The representative sequence
and the prefix sums

\[
                 s_{j+1}=s_j+\delta_{e_j}\pmod{k}   \tag{5.2}
\]

determine the physical carrier exactly.  After one quotient lap the sheet has
changed by the total voltage; the next lap is the corresponding cyclic shift.

### 5.3 Residence and lower `q=2` are short lifted motifs

For this project, `k=15` has depth `d=3`.  Residence excludes coordinate runs
of lengths 1, 2, or 3 in the lifted upper carrier.  Lower `q=2` asks that the
triple intersections

\[
                  T_i\cap T_{i+1}\cap T_{i+2}
\]

cover rank 6.  Once (5.2) is known, both are bounded-window tests.

They are not additive over plane-tree variables: changing one gluing choice
can reconnect and reverse long quotient subpaths.  Nevertheless, a failed
bounded window is controlled by the small set of gluing/switch choices that
supplies its factor edges.  It therefore yields an exact lazy motif-blocking
clause.  This is a natural CEGAR layer over the 33-variable arborescence family
or the 131-label full spanning-tree family.

### 5.4 Deeper upper shadows remain lazy OR-of-AND constraints

A missing upper target may be witnessed by many quotient windows.  As in the
existing quotient solver, its exact clause is an OR over candidate windows,
each window being an AND of the edge/gluing choices that realizes it.  There
is no reason to encode all such targets initially.

## 6. The released program is deterministic

The source audit found no hidden portfolio or gluing-choice parameter.

* `Tree::normalize()` canonically roots at centroid(s) and chooses a
  lexicographically least cyclic subtree ordering.
* `Periodic_path::select_subtree()` implements the priority list (T2).
* `Periodic_path::select_leaf()` implements the fixed rules (T3).
* `Knuth_gray_code::init_switches()` deterministically chooses the voltage
  repair from the Catalan residue.
* The command line exposes only `n`, desired unit shift, initial vertex, and
  output controls.

The complicated second spanning tree in Section 8 was designed to make
gluing nesting-free and its voltage equal to the Catalan number.  Its rules
are deliberately canonical.  The arbitrary tie choices of the simpler first
tree in Section 6 are not exposed by the program.

Therefore running the published executable with many seeds or starting
vertices is not a search strategy.  It returns cyclic starts and coordinate
automorphisms of essentially one construction.

## 7. Exact small-case calibration

The independent audit script reconstructs `f`, all plane-tree classes, all
gluing pairs and 6-cycles, all labeled spanning trees for small `n`, all
parallel-edge substitutions, quotient traversal, voltage, and the lifted
upper carrier.

### 7.1 Connectivity-free potential subfamily

| `k` | members | best missing upper-`q=1` orbits | after all parallel labels |
|---:|---:|---:|---:|
| 9 | 1 | 1 | 1 |
| 11 | 4 | 2 | 2 |
| 13 | 64 | 9 | 9 |

So the independent potential-decreasing choices alone never recover the
already-known perfect upper shadow.

For `k=11`, the known fresh exact quotient solution
`equi2_k11_rnd34.json` differs from every member of this subfamily in at least
37 of the 42 lower-orbit choices, even after all ten coordinate multipliers.

### 7.2 Full MMM gluing-tree family at `k=11`

This stronger audit enumerates all 13 labeled gluing pairs on the six plane
trees, all labeled spanning trees, retains every simultaneous symmetric
difference that is a quotient Hamilton cycle, and then enumerates every
parallel edge label.

Exact counts:

* 74 quotient-Hamilton gluing-tree occurrences;
* 1496 parallel-labeled candidate occurrences;
* 1360 candidates with unit voltage;
* minimum upper-`q=1` misses: 0;
* minimum lower-`q=2` misses: 0;
* minimum forbidden short coordinate runs: **143**;
* candidates satisfying all three gates simultaneously: **0**.

Some candidates attain both shadow minima simultaneously, but they have 165
forbidden short runs.  The best residence candidates have 143 short runs and
miss both shadow gates.  The known optimal `k=11` carrier has zero short runs.

This is an exact family-level negative result, not a statement about the one
canonical output.

Reproduction:

```sh
python3 scratch/extract_mmm_gluing_family.py 5 \
  --enumerate-all-spanning-trees
```

The analogous exact `k=9` audit also has no simultaneous pass.  The `k=15`
family is far too large for enumeration, but small enough for a dedicated
SAT/CP-SAT model on its gluing-tree variables.

## 8. Recommended use at `k=15`

The highest-value test is a staged remote CPU search:

1. **131-label model:** choose a compatible labeled spanning tree in `H_7`.
2. Derive the factor by (2.1); expose selected double-edge labels.
3. Enforce upper `q=1` using the local colours (5.1).
4. Enforce unit voltage modulo 15.
5. Add residence and lower-`q=2` motif cuts lazily.
6. Only after those pass, audit all deeper upper shadows and the weighted
   quotient compiler.

The 33-variable potential arborescence is useful as a first ablation, but its
small-case upper-shadow failures make the full 131-label tree the more honest
test.

This route is algorithmically attractive because it removes the generic
429-vertex connectivity search.  It should not be promoted to the leading
general proof architecture until it overcomes the exact `k=11` residence
failure.  A successful `k=15` member would be a new phenomenon of the larger
plane-tree gluing space, not something already implicit in the released MMM
generator.

