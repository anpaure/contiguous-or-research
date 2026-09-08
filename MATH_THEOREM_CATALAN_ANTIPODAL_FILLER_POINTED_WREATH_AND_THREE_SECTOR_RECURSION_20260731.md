# Antipodal Catalan fillers are pointed wreath factors, and their exact three-sector recursion

Date: 2026-07-31  
Status: exact equivalences and conditional all-parameter recursion; explicit independently replayed instances at parameters `1,2,3,4`, forming a literal recursive chain `1 -> 2 -> 3 -> 4`.  No all-parameter residual-factor theorem is claimed.

## 0. Result

Put

\[
 C_n=\frac1{n+1}\binom{2n}{n},\qquad
 M_n=\binom{2n}{n}=(n+1)C_n,\qquad
 N_n=\binom{2n}{n-1}=nC_n.
\]

Here `n` is the half-size parameter of the even core.  In the original odd
ground-set notation it corresponds to `k=2n+1`, after adjoining the
distinguished point `infinity`; thus `n=(k-1)/2` (for example `k=15` means
`n=7`).

An **antipodal-geodesic Catalan filler** (`AGCF`) on a `2n`-set
`Omega` is a partition of `binom(Omega,n)` into `C_n` Johnson paths

\[
 X_0,X_1,\ldots,X_n=\overline {X_0}
\]

such that the `N_n` intersections `X_(i-1) cap X_i` enumerate
`binom(Omega,n-1)` and the `N_n` unions `X_(i-1) cup X_i` enumerate
`binom(Omega,n+1)`.

The exact conclusions are:

1. A single complement geodesic is equivalent to a pointed cyclic order.
   Its `n+1` point-avoiding middle intervals are its vertices, and its `n`
   point-containing middle intervals are the complements of its upper turn
   colours.  Consequently **vertices plus upper turns exact** is exactly an
   exact pointed wreath factor on `2n+1` coordinates.  The lower-turn rainbow
   is one additional, genuinely nonautomatic condition.
2. Equivalently, an AGCF is one middle-vertex path factor whose two alternating
   lifts to ranks `(n-1,n)` and `(n,n+1)` are simultaneously spanning
   antipodal cube geodesics.
3. Equivalently, its edges are a perfect matching between the rank-`n-1` and
   rank-`n+1` shores of the two-step containment graph, whose Johnson lift is
   a `C_n`-path forest with complementary endpoints.
4. There are explicit AGCFs at `n=2,3,4`.  The `n=4` existence is a full
   20,160-geodesic exact-cover result, not a two-parent MSW artefact.
5. There is an exact recursive split.  Extend every child path by one `c/z`
   tag-swap edge.  What remains is a three-sector complement-geodesic factor
   on three equal vertex shores of size `N_n`, with

   \[
      C_{n+1}-C_n=\frac{3N_n}{n+2}
        =\sum_{a+b+c=n-1}C_aC_bC_c                         \tag{0.1}
   \]

   residual paths.  Its three constant-tag blocks have internal lengths
   `(a,b,c)`.  This residual factor is the exact missing inductive object.
6. The explicit certificates realize the split literally at every step
   `1 -> 2 -> 3 -> 4`.  At each step the residual paths have composition
   multiplicities `C_a C_b C_c` for every `a+b+c=n-1`.

Thus the universal filler is not merely a wish for a residence-clean forest.
It is a sharply recognizable strengthening of the exact wreath factor, and
the recursion reduces it to one ordered three-level path-factor theorem.

## 1. From one complement geodesic to one pointed wreath

Let `Omega` have size `2n`, let `infinity` be a new point, and let

\[
 X_i=X_{i-1}-a_i+b_i\qquad(1\le i\le n)                 \tag{1.1}
\]

be a Johnson geodesic from `X_0` to its complement.  Minimality implies that
`a_1,...,a_n` enumerate `X_0` and `b_1,...,b_n` enumerate its complement.
Define the cyclic order

\[
       \pi=(a_1,a_2,\ldots,a_n,b_1,b_2,\ldots,b_n,\infty). \tag{1.2}
\]

### Theorem 1.1 (pointed-wreath dictionary)

The length-`n` cyclic intervals of (1.2) are exactly

\[
 \{X_0,\ldots,X_n\}\ \dot\cup\
 \{(X_{i-1}\cup X_i)^c:1\le i\le n\},                \tag{1.3}
\]

where complements in the second family are taken inside
`Omega union {infinity}`.  The first family avoids `infinity`, and the second
family contains it.

#### Proof

The `n+1` intervals which do not meet `infinity` start at
`a_1,a_2,...,a_n,b_1`.  The interval starting at `a_(i+1)` is

\[
       \{a_{i+1},\ldots,a_n,b_1,\ldots,b_i\}=X_i.      \tag{1.4}
\]

For `1<=i<=n`, put

\[
 U_i=X_{i-1}\cup X_i
    =\{a_i,\ldots,a_n,b_1,\ldots,b_i\}.                \tag{1.5}
\]

Its complement is

\[
 \{b_{i+1},\ldots,b_n,\infty,a_1,\ldots,a_{i-1}\},    \tag{1.6}
\]

which is the corresponding point-containing length-`n` interval.  These are
all `2n+1` starts.  `square`

### Corollary 1.2 (exact factor equivalence)

A family of `C_n` complement geodesics partitions `binom(Omega,n)` and has
all upper turns distinct if and only if the associated cyclic orders form an
exact `(2n+1,n)` wreath decomposition.

The inverse is canonical after the distinguished point is fixed: the
`n+1` point-avoiding intervals of each wreath, in consecutive-start order,
form the complement geodesic; the other `n` intervals recover the upper
turns by complementation.

This is exactly the distinguished-coordinate normal form of the MSW odd-graph
factor.  The Mütze--Standke--Wiechert construction supplies this corollary
unconditionally.  It does **not** supply the next condition:

\[
 \{X_{i-1}\cap X_i:\text{all paths and }1\le i\le n\}
        =\binom\Omega{n-1}\quad\text{without repetition}.       \tag{1.7}
\]

For example, the canonical Chung--Feller parent first has lower-turn defect
at `n=3`, and its defect is already 12 at `n=4`; see
`scratch/audit_bounded_defect_msw_lower_collision_20260731.py`.  Hence an
AGCF is a pointed wreath factor with an extra transverse lower rainbow, not
a repackaging of the published factor.

## 2. Two other exact normal forms

### Theorem 2.1 (simultaneous two-level path factors)

Replace every Johnson edge `X_(i-1)X_i` first by

\[
 X_{i-1}\subset U_i=X_{i-1}\cup X_i\supset X_i,        \tag{2.1}
\]

and separately by

\[
 X_{i-1}\supset L_i=X_{i-1}\cap X_i\subset X_i.        \tag{2.2}
\]

A middle path family is an AGCF if and only if (2.1) partitions ranks
`n,n+1`, (2.2) partitions ranks `n-1,n`, and every displayed alternating
path joins complementary middle endpoints.  Every such alternating path is
a `2n`-edge hypercube geodesic.

This shows precisely why an ordinary Middle Levels path factor is only one
half of the object.

### Theorem 2.2 (diamond matching)

Let `B_n` be the bipartite graph with shores `binom(Omega,n-1)` and
`binom(Omega,n+1)`, joining `L` to `U` when `L subset U`.  The incidence
`L-U` lifts to the Johnson edge between the two intermediate `n`-sets.

An AGCF is equivalent to a perfect matching of `B_n` whose lifted graph is a
linear forest with `C_n` components and complementary endpoints in every
component.

#### Proof

Exactness of the two turn palettes is exactly the perfect-matching condition.
There are `N_n` lifted edges and `M_n` vertices, so a forest has
`M_n-N_n=C_n` components.  Complementary endpoints have Johnson distance
`n`; therefore every component has at least `n` edges.  Their total edge
count is `nC_n`, so every component has exactly `n` edges and is a geodesic.
The converse is immediate.  `square`

The matching part alone is routine; the complement pairing of its physical
components is the nonstandard integral correlation.

### Lemma 2.3 (coordinate-flux consistency)

In any exact two-palette selection, every coordinate occurs in exactly
`C_n` edge supports:

\[
 \binom{2n-1}{n}-\binom{2n-1}{n-2}=C_n.               \tag{2.3}
\]

An AGCF realizes this minimum pathwise: every coordinate flips once in every
one of its `C_n` components.  Thus there is no scalar coordinate-count
obstruction; only the distribution of those flips among components remains.

## 3. The exact recursive split

Assume an AGCF `G` at parameter `n`.  Orient every child path

\[
 P=(X_0,\ldots,X_n=\overline {X_0})                   \tag{3.1}
\]

and let `E` be the set of its selected terminal endpoints `X_n`.  Then
`|E|=C_n` and `E` contains exactly one endpoint from every child component.
Adjoin new coordinates `c,z` and extend (3.1) to

\[
 \widehat P=(c+X_0,c+X_1,\ldots,c+X_n,z+X_n).         \tag{3.2}
\]

Every path (3.2) is an `(n+1)`-edge complement geodesic.  Collectively they
consume the following resources exactly:

\[
\begin{array}{c|c}
\text{middle vertices}&c+\binom\Omega n,\quad z+E\\
\text{lower colours}&c+\binom\Omega{n-1},\quad E\\
\text{upper colours}&c+\binom\Omega{n+1},\quad c+z+E.
\end{array}                                                    \tag{3.3}
\]

What remains has three equal middle shores

\[
 V_0=\binom\Omega{n+1},\qquad
 V_1=z+\left(\binom\Omega n\setminus E\right),\qquad
 V_2=c+z+\binom\Omega{n-1},                                  \tag{3.4}
\]

each of cardinality `N_n`.  Its lower resource banks are

\[
 \left(\binom\Omega n\setminus E\right),\quad
 z+\binom\Omega{n-1},\quad c+z+\binom\Omega{n-2},             \tag{3.5}
\]

of sizes `N_n,N_n,P_n`, and its upper resource banks are

\[
 \binom\Omega{n+2},\quad z+\binom\Omega{n+1},\quad
 c+z+\left(\binom\Omega n\setminus E\right),                 \tag{3.6}
\]

of sizes `P_n,N_n,N_n`, where

\[
 P_n=\binom{2n}{n-2}=\frac{n-1}{n+2}N_n.                       \tag{3.7}
\]

### Theorem 3.1 (three-sector recursion)

Suppose the resources (3.4)--(3.6) admit a path factor `R_n(E)` such that

1. every component is a complement geodesic;
2. every component has tag trace
   `00...00, 01...01, 11...11`; and
3. every remaining lower and upper colour is used once.

Then the paths (3.2) together with `R_n(E)` form an AGCF at parameter
`n+1`.  Conversely, every AGCF containing all extended paths (3.2) and no
`c`-only vertex elsewhere induces exactly such a residual factor.

#### Proof

The resource lists are disjoint and exhaust the ambient middle and turn
layers.  A residual path cannot use the absent `c`-only sector.  Since its
endpoints are complementary, the two tag coordinates each flip once, in the
only possible order `00 -> 01 -> 11`; all old coordinates also flip once.
Union with (3.2) therefore gives the required vertex partition, both exact
palettes, and complementary geodesic components.  Restriction proves the
converse.  `square`

The number of residual components is forced:

\[
 K'_n=C_{n+1}-C_n=\frac{3n}{n+2}C_n=\frac{3N_n}{n+2}.           \tag{3.8}
\]

The residual edge count is

\[
 3N_n-K'_n=\frac{3(n+1)}{n+2}N_n=2N_n+P_n,                    \tag{3.9}
\]

exactly the size of either palette in (3.5)--(3.6).  In particular
`n+2` divides `3N_n`; there is no divisibility obstruction.

If a residual path has `a,b,c` internal edges in its three tag blocks, then

\[
                         a+b+c=n-1.                             \tag{3.10}
\]

The Catalan identity

\[
 K'_n=\sum_{a+b+c=n-1}C_aC_bC_c                                \tag{3.11}
\]

follows from `[x^(n-1)]C(x)^3`, or from the first-return split

\[
 \mathcal D_{n+1}=10\mathcal D_n\ \dot\cup\
 \{11P0Q0R:|P|/2+|Q|/2+|R|/2=n-1\}.                           \tag{3.12}
\]

This supplies the right recursive indexing: child extensions correspond to
the first class in (3.12), while residual paths should correspond to the
ordered triples in the second.  What remains unproved is the **labelled
coordination theorem** assigning the physical old coordinates so that the
three vertex shores and both palettes are simultaneously exact.

The residual is therefore not an arbitrary SAT object.  It is an ordered
three-level path-factor instance: after deleting the tags, every component is
a Johnson path in rank `n+1`, a downward inclusion edge, a Johnson path in
rank `n`, a second downward inclusion edge, and a Johnson path in rank
`n-1`.  The exact matching relaxation is a banded lower/upper diamond
matching, but complement-connectedness is an additional global condition.

### Theorem 3.2 (three tight forests plus two containment seams)

Every residual factor in Theorem 3.1 decomposes uniquely into three spanning
linear forests on `V_0,V_1,V_2`, each with exactly `P_n` edges and
`K'_n=N_n-P_n` components, together with `K'_n` seams of each type

\[
        A\supset X:\quad A\ --\ (z+X),
 \qquad X\supset L:\quad (z+X)\ --\ (c+z+L).          \tag{3.13}
\]

After suppressing the fixed tags, their exact palettes have the following
forced form.

* The `V_0` forest uses every rank-`n+2` union.  Its rank-`n`
  intersections together with the first-seam labels `X` partition
  `binom(Omega,n)\E`.
* The `V_1` forest has `P_n` rank-`n-1` intersections and `P_n`
  rank-`n+1` unions.  These, together with the second-seam labels `L` and
  first-seam labels `A`, partition the corresponding complete levels.
* The `V_2` forest uses every rank-`n-2` intersection.  Its rank-`n`
  unions together with the second-seam labels `X` partition
  `binom(Omega,n)\E`.

The component pairings must join initial `A` to terminal
`c+z+(Omega\A)`.  Conversely, three forests and two componentwise seam
matchings satisfying this ledger and complementary-end condition give
`R_n(E)`.

#### Proof

Every residual path crosses each sector boundary once, so it contains one
nonempty block from each sector forest.  There are `K'_n` edges of each
seam type.  In the `V_0` lower bank, for example, the seams consume
`K'_n` of the `N_n` resources, leaving
`N_n-K'_n=P_n` internal edges; the rank-`n+2` upper bank has exactly
`P_n` resources and is wholly internal.  The same count on the two other
sectors gives `P_n` internal edges in each.  A forest on `N_n` vertices
with `P_n` edges has `K'_n` components.

The first edge in (3.13) is Johnson exactly when `X subset A`; its
intersection is `X` and its union is `z+A`.  The second is Johnson exactly
when `L subset X`; its intersection is `z+L` and its union is `c+z+X`.
These identities give the displayed palette partitions.  Complementarity
of the full endpoints gives `L=Omega\A`.  Reversing the argument proves
the converse. `square`

This factorization separates the remaining difficulty cleanly.  Each
sector alone is a one- or two-sided tight-enumeration problem; the open row
is their common endpoint-containment matching with complementary outer
ends.  Three separately good forests do not suffice.

### Lemma 3.3 (canonical ternary anatomy of one residual path)

Let a residual path have composition `(a,b,c)`.  Its old coordinate set
has a canonical ordered partition

\[
 \Omega=Q_0\ \dot\cup\ \{s\}\ \dot\cup\ Q_1\ \dot\cup\
          \{t\}\ \dot\cup\ Q_2,                              \tag{3.14}
\]

where `|Q_0|=2a`, `|Q_1|=2b`, and `|Q_2|=2c`.  The coordinates in `Q_i`
are exactly those flipped by internal edges of tag sector `i`; `s` is
removed at the `00 -> 01` seam and `t` at the `01 -> 11` seam.  After
deleting all fixed old coordinates, each sector block is itself a
complement Johnson geodesic on its `2a`, `2b`, or `2c` moving coordinates.

#### Proof

An `(n+1)`-edge Johnson geodesic between complementary subsets changes
`2n+2` coordinate bits, exactly the ambient number, so every coordinate
flips exactly once.  The tags `z,c` flip at the two sector seams.  Each seam
also deletes one old coordinate, called `s,t`; every remaining old
coordinate flips internally in exactly one sector.  An internal sector of
`a` Johnson edges flips `2a` distinct old coordinates, and its two endpoint
restrictions on those coordinates are complements.  The other sectors are
identical. `square`

### Corollary 3.4 (the Catalan type quotas balance every bank in total)

Give type `(a,b,c)` the forced multiplicity `C_aC_bC_c`, summed over
`a+b+c=n-1`.  If `K'_n` is as in (3.8), symmetry among the three indices
gives

\[
 \sum_{a+b+c=n-1}aC_aC_bC_c
 =\sum bC_aC_bC_c=\sum cC_aC_bC_c
 =\frac{n-1}{3}K'_n=P_n.                                  \tag{3.15}
\]

Consequently each tag sector receives

\[
       P_n+K'_n=N_n                                      \tag{3.16}
\]

vertex occurrences, each internal forest receives `P_n` edges, and each
seam family receives `K'_n` edges.  Thus the Catalan-triple prescription
matches all nine bank cardinalities exactly.  This is an aggregate ledger,
not an integral labelled factor theorem: the remaining problem is to
correlate the actual masks and complementary outer endpoints.

## 4. Exact finite recursion through `n=1 -> 2 -> 3 -> 4`

The bottom two steps are frozen together in

```text
scratch/catalan_antipodal_geodesic_filler_n1_to_n3_recursive_20260731.witness.txt
scratch/audit_catalan_antipodal_geodesic_filler_n1_to_n3_recursive_20260731.py
```

For `n=1 -> 2`, on old coordinates `{1,2}` with `c=0,z=3`, the child
extension is `3 5 12` and the sole residual path is `6 10 9`.  Its
composition histogram is

\[
                    (0,0,0):1=C_0C_0C_0.                 \tag{4.1}
\]

For `n=2 -> 3`, use old coordinates `{1,2,3,5}`, `c=0,z=4`, and relabel
the child coordinates by `(0,2,1,3)`.  Two paths are literal child
extensions and the other three are the three-sector residual.  Their exact
histogram is

\[
 (1,0,0):1,\qquad(0,1,0):1,\qquad(0,0,1):1,              \tag{4.2}
\]

again exactly `C_aC_bC_c`.  The independent replay verifies the child
coordinate conjugacy, endpoint transversals, residual shores, both exact
palettes, complement endpoints, and one flip of every coordinate on every
path.  Run it with

```text
python3 scratch/audit_catalan_antipodal_geodesic_filler_n1_to_n3_recursive_20260731.py
```

For `n=3 -> 4`, the child is the five-path parameter-three AGCF from

```text
scratch/catalan_antipodal_geodesic_filler_n3_20260731.audit.json
```

On old coordinates `0,...,5`, put `c=6,z=7`.  The certificate

```text
scratch/catalan_antipodal_geodesic_filler_n3_to_n4_recursive_20260731.witness.txt
```

contains five literal extensions (3.2) and nine residual paths.  The latter
all have monotone tag trace and their block-composition multiplicities are

\[
\begin{array}{c|cccccc}
(a,b,c)&(2,0,0)&(0,2,0)&(0,0,2)&(1,1,0)&(1,0,1)&(0,1,1)\\ \hline
\#&2&2&2&1&1&1,
\end{array}                                                     \tag{4.3}
\]

which is exactly `C_a C_b C_c`.  Thus the Catalan triple law is not only a
counting suggestion: this recursive instance realizes it physically.

Independently replay with

```text
python3 scratch/audit_catalan_antipodal_geodesic_filler_n3_to_n4_recursive_20260731.py
```

The replay checks all 70 middle vertices, all 56 lower colours, all 56 upper
colours, every complement endpoint, every coordinate flip, the child
projection, the endpoint transversal, the exact residual vertex set, and
the histogram (4.3).

The separate full-catalogue `n=4` existence certificate is in

```text
scratch/catalan_antipodal_geodesic_filler_n4_20260731.witness.txt
scratch/audit_catalan_antipodal_geodesic_filler_n4_20260731.py
```

and is useful evidence that the object is not confined to the recursive
face chosen above.

## 5. Relation to existing constructions and exact obstruction to the sealed lift

* **MSW / odd-graph factor.**  This supplies Theorem 1.1 through the upper
  palette, but not the lower rainbow (1.7).
* **Middle Levels.**  It supplies one of (2.1)--(2.2), not their synchronized
  common middle chronology.
* **Symmetric-chain decompositions.**  They supply abundant rank matchings,
  but an AGCF asks for two outer ranks to be paired through the same diamonds
  and for the physical lift to have complement-paired components.  Ordinary
  orthogonality or edge-disjointness does not state that condition.
* **Current strict direct-edgewise recursion.**  Its independent `c` rail is
  sealed.  A copied `n`-edge AGCF component remains an isolated `n`-edge
  component at parameter `n+1`, so it cannot itself be an AGCF component.
  The single seam in (3.2) is not optional: every child component must be
  opened to the `z` sector.  Hence the existing sealed-filler theorem cannot
  propagate this universal filler without a global rethreading.
* **Canonical Dyck endpoints.**  Freezing the `10 D_n` endpoint bank and
  filling the other Catalan class with canonical MSW residual paths does not
  work.  At `n=3`, an exhaustive 360-geodesic census proves that no AGCF has
  the canonical Dyck endpoint bank.  The 72 viable banks are instead one
  `S_6` orbit: a distinguished point plus the edges of a 5-cycle.  See
  `MATH_THEOREM_CATALAN_AGCF_N3_ENDPOINT_BANK_C5_CLASSIFICATION_20260731.md`.
  Thus the endpoint transversal is a path-dependent inductive state, not a
  fixed ballot transversal.

### What the arbitrary-common-basis near-forest theorem changes

The arbitrary-`Q` theorem in
`MATH_THEOREM_CATALAN_ARBITRARY_COMMON_BASIS_PHYSICAL_FOREST_20260731.md`
is uniform over every **admissible** puncture basis.  Therefore, after an
endpoint/seam state and a compatible common basis have been selected, every
punctured internal row has a `P_n-o(P_n)` physical forest body.  The
pointed-`C5` classification above causes no additional distributional loss:
the near-forest theorem does not require that compatible basis to be
canonical or quasirandom.  It does not itself prove that an arbitrary
endpoint bank induces such a basis.

There are two important scope distinctions.

1. The collar common basis `Q`, the path-orientation transversal `E` in
   (3.1), and the unordered endpoint-pair bank of an AGCF are related but
   are not the same object.  Uniformity over `Q` does not prescribe the
   endpoint bank.
2. Attachment pruning keeps the forced seams and makes a **partial** support
   acyclic after deleting `o(P_n)` side atoms.  It does not make every side
   component meet a seam, give the exact component count, join all three
   sectors in each component, or pair each outer endpoint with its
   complement.  Those are precisely the exact leave and one-reset topology
   conditions.

Consequently the finite `C5` theorem changes the inductive state, but not
the asymptotic body: endpoint banks must be outputs of the correlated
completion rather than a fixed Dyck input.

The shortest honest all-parameter target **within this recursion** is now:

> **Bank-flexible three-sector cover-down.**  Starting with the selected
> parameter-`n` AGCF, choose its orientation transversal `E` jointly with
> the three punctured forest rows and reserved switches so that (i) the
> `o(P_n)` leave is a disjoint union of residual candidate paths and (ii)
> every augmented component contains exactly one complementary endpoint
> reset.  The resulting bank is carried as part of the parameter-`n+1`
> state.

This is enough to induct from `n=1`.  The stronger assertion that **every**
parameter-`n` AGCF extends may be useful, but it is not required and is not
supported by the `n=3` bank classification.  In the unrestricted resource
hypergraph language, the same missing statement is the edge-aligned
cover-down theorem: leave complete candidate edges for the universal
two-by-two absorbers.  No further canonical endpoint formula is needed.
