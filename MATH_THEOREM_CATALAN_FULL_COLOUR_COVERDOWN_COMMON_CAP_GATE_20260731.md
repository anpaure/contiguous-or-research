# Full-colour cover-down: exact common-cap closure and the protected-cap rigidity gate

Date: 2026-07-31  
Status: exact deterministic exchange theorem and exact finite obstruction.  No
zero-defect cover-down theorem is claimed.

## 0. Verdict

Fix an admissible puncture set `Q` and one shore of its four-uniform
capacity-slot hypergraph `G_Q`.  The full Delcourt--Postle colouring is a
useful distributed reservoir, but it does not create an additional
``common-cap'' degree of freedom.

There are two sharply different meanings of common-cap compatibility.

1. **Existential Boolean cap.**  If a selected atom set is an exact outer
   matching, respects the physical slots, and projects to a linear forest,
   then its common two-step cap is automatic.  Every atom already records
   its bottom, its cap, and the two opposite intermediate corners.  Thus
   arbitrary inter-colour exchanges need no extra cap constraint beyond
   the ordinary outer, slot, and graphic rows.
2. **Pointwise protected cap.**  If the cap map is prescribed at a bottom,
   then the physical diamond edge at that bottom is forced.  A
   cap-preserving exchange can only change its slot lift; it cannot repair
   physical degree or topology there.  Therefore a cover-down may freeze a
   protected subbank of caps, but freezing the whole cap map leaves no
   physical exchange freedom.

The exact obstruction that survives the full colouring is a host cut.  A
set of cap targets whose every surviving atom uses physical corners in a
set `W` requires two units per target, while `W` has only its residual slot
capacity.  This cut is invariant under every alternating recolouring.  The
authenticated `n=3` common-basis fixture violates it by exactly one
(`8>7`).  Hence a statement asserting zero-defect cover-down from the full
colouring for **every** fixed admissible `Q` is false without a host-cut
hypothesis.  This finite obstruction is not a counterexample to the
asymptotic Delcourt--Postle theorem.

The downstream word-compiler common cap is a different object.  Nothing
here promotes the Boolean two-step cap to a literal maximal-envelope
compiler.

## 1. The occurrence-labelled slot model

Use the notation

\[
 \mathcal D\subseteq {[2n]\choose n},\qquad
 \mathcal V={[2n]\choose {n+2}}.
\]

The physical owner bank is
`X=binom([2n],n+1)`.  Each owner `x` has residual capacity

\[
 c(x)=\begin{cases}1,&x\text{ is an inherited seam anchor},\\
                    2,&\text{otherwise}.
       \end{cases}                                      \tag{1.1}
\]

An occurrence-labelled atom is

\[
 e=(D,V,(x,i),(y,j)),                                  \tag{1.2}
\]

where `D subset V`, `V-D={a,b}`, `x=D+a`, `y=D+b`, and
`1<=i<=c(x)`, `1<=j<=c(y)`.  Its outer edge is `DV` and its physical edge
is `xy`.  In particular

\[
                  x\cap y=D,\qquad x\cup y=V.          \tag{1.3}
\]

Different slot lifts of one pair `(D,V)` are parallel occurrences.  Two
such occurrences meet in both outer resources, so no slot matching can
contain both.

Let `K` denote any already frozen central-plus-seam physical forest.  Its
incidences have already been deducted from the residual capacities in
(1.1), so a slot matching whose union with `K` is acyclic has combined
maximum degree at most two.

## 2. Existential common caps are exchange-closed

### Theorem 2.1 (automatic common-cap closure)

Let `S` be a matching in `G_Q` which contains exactly one atom at every
\(D\in\mathcal D\) and exactly one atom at every
\(V\in\mathcal V\).  Suppose
also that

\[
                        K\cup p(S)                    \tag{2.1}
\]

is a forest, where `p` is physical projection.  Then there are injections

\[
 f_0,f_1:\mathcal D\longrightarrow\mathcal X          \tag{2.2}
\]

and a bijection

\[
 \pi:\mathcal D\longrightarrow\mathcal V             \tag{2.3}
\]

such that, for every `D`,

\[
 f_0(D)\ne f_1(D),\quad
 f_0(D)\cap f_1(D)=D,\quad
 f_0(D)\cup f_1(D)=\pi(D).                            \tag{2.4}
\]

Every anchor occurs in the combined images of `f_0,f_1` at most once.
Thus `S` is already a pointwise common-cap diamond factor.

#### Proof

The outer matching defines `pi(D)` as the unique cap paired with `D`; cap
saturation makes `pi` bijective.  Slot matching gives physical degree at
most two and anchor degree at most one.  Since (2.1) is a forest, every
nontrivial physical component is a path.  Orient each path and take the
tail and head of the edge indexed by `D` as `f_0(D),f_1(D)`.  Outdegree
and indegree at most one make both maps injective.  Equation (1.3) gives
(2.4).  The anchor assertion is exactly (1.1).  \(\square\)

Consequently, if an alternating exchange produces another set satisfying
the three hypotheses of Theorem 2.1, common-cap compatibility requires no
separate test.  In particular, protected seams and anchors are already
encoded as capacity-one slot vertices.

## 3. Exact packet tests

Let `S` be a current legal slot matching and let a packet replace
\(A\subseteq S\) by an equally large occurrence set `B` disjoint from
`S-A`.
Write

\[
                         S'=S-A+B.                    \tag{3.1}
\]

### Theorem 3.1 (outer, slot, and graphic packet criterion)

The packet is a legal exact-cap side exchange if and only if all three
following rows hold.

1. **Outer row.**  `S'` has the required lower and upper loads.  When `S`
   and `S'` are both outer-perfect, their occurrence-labelled outer
   symmetric difference is a disjoint union of even alternating circuits;
   parallel two-circuits are precisely slot relifts of a fixed `(D,V)`.
2. **Slot row.**  `B` is a matching and uses no slot occupied by `S-A`.
   If only unlabelled physical edges are specified, this is equivalent to

   \[
        d_{p(S-A)}(x)+d_{p(B)}(x)\le c(x)\qquad(x\in\mathcal X). \tag{3.2}
   \]

3. **Graphic row.**  Contract every component of

   \[
                       K\cup p(S-A).                  \tag{3.3}
   \]

   Then the images of `p(B)` contain neither a loop nor a cycle.

If the rows hold, Theorem 2.1 supplies the resulting common cap
automatically.

#### Proof

The symmetric difference of two perfect matchings in the bipartite outer
incidence multigraph is exactly a disjoint union of even alternating
circuits.  The slot statement is the definition of a hypergraph matching;
with interchangeable slots, (3.2) is necessary and sufficient for a slot
assignment.  A set of edges added to a forest remains acyclic exactly when
its images after contracting the old forest are loopless and acyclic.
These statements are separately necessary and sufficient and exhaust the
resources of (1.2).  The final assertion is Theorem 2.1.  \(\square\)

This is also an exact serialization rule.  An ordered packet list is legal
if and only if Theorem 3.1 holds after every **whole** packet.  To verify
the graphic row inside one packet, one may conceptually delete its old
edges and then add each new edge between two distinct current contracted
components, with all outer and slot resources private outside the named
alternating circuit.  The conceptual intermediate sets need not be
outer-perfect; the packet is switched simultaneously.  Such private ears
can be checked in any order compatible with their component-contraction
forest.  This is a deterministic sufficient lemma, not a theorem that the
full colouring contains enough such ears.

### Proposition 3.2 (exact bichromatic recolouring test)

Fix two colours `alpha,beta` in a full conflict-free colouring.  On their
atoms form the bipartite graph `J_(alpha,beta)` which joins opposite-colour
atoms whenever they share any vertex of `G_Q`.  Let `Z` be a set of atoms
whose two colours are to be interchanged.  Then the recoloured classes are
still slot matchings if and only if `Z` is a union of connected components
of `J_(alpha,beta)`.

They remain conflict-free for the configuration hypergraph `H_L` if and
only if, in addition, no member of `H_L` is monochromatic after the swap.
These latter tests are genuinely higher-rank and do not follow from the
component condition.

#### Proof

At a host resource incident with one of the two colours, swapping its sole
atom is harmless.  If the resource sees one atom of each colour, swapping
exactly one makes them equal-coloured and swapping both or neither is safe.
Thus the swap indicator must be constant on every edge, equivalently on
every connected component, of `J_(alpha,beta)`.  This condition is plainly
sufficient for all host resources.  The second assertion is exactly the
definition of an `H_L`-avoiding colour class.  Since configurations have
orders `3,...,L`, their monochromaticity is not a pairwise resource
condition.  \(\square\)

The Delcourt--Postle colouring adds only a reservoir statement: every
colour class is a slot matching avoiding the declared short physical
cycles.  Swapping a component of the bichromatic **line-conflict** graph
preserves the matching rows, but it need not preserve the higher-rank
configuration constraints: a formerly bichromatic physical cycle can
become monochromatic.  Even after those configurations are rechecked, the
cross-conflict component need not be a path or a circuit, and the swap need
not satisfy the outer or graphic rows above.  Therefore the colouring
theorem alone supplies no serializable ear system.

## 4. Protected-cap rigidity

Let `S,S'` be two exact outer-perfect slot matchings and let
\(\pi_S,\pi_{S'}\) be their cap maps.

### Theorem 4.1 (protected-cap criterion)

For \(Z\subseteq\mathcal D\),

\[
 \pi_{S'}|_Z=\pi_S|_Z                                  \tag{4.1}
\]

if and only if every nonparallel alternating outer circuit in
\(S\mathbin\triangle S'\) avoids `Z`.  At a member of `Z`, the only allowed
occurrence-labelled change is a parallel slot relift of the same outer
pair \((D,\pi_S(D))\).

#### Proof

At `D`, each perfect matching has one incident outer edge.  If the two
edges have different cap endpoints, `D` lies on a nontrivial alternating
circuit.  If their cap endpoints agree, the outer pair is the same and
only its slot labels can differ.  Applying this independently to every
\(D\in Z\) proves the equivalence.  \(\square\)

### Corollary 4.2 (a fixed full cap map freezes the physical support)

Fix a bijection \(\pi_*:\mathcal D\to\mathcal V\) with
\(D\subset\pi_*(D)\).
There is exactly one unlabelled physical edge over every prescribed pair:
if \(\pi_*(D)-D=\{a,b\}\), it is

\[
                         (D+a)(D+b).                  \tag{4.2}
\]

Hence a side factor with cap map \(\pi_*\) exists if and only if these forced
edges satisfy the capacities (1.1) and their union with `K` is a forest.
All cap-preserving exchanges are slot relifts and leave the unlabelled
physical support unchanged.

This is the sharp common-cap compatibility gate.  Topological or degree
repair requires permission to migrate the cap of at least one bottom on
every offending physical circuit or overload.  Thus ``preserve the common
cap'' cannot mean freezing the whole pointwise map during cover-down unless
that map is already physically feasible.

The canonical BTK diagonal gives an all-parameter calibration of this
rigidity.  Its protected cap map has a physical owner `X_n` of degree at
least `n-1`; hence it violates cap two for every `n>=4`.  No packet which
preserves that pointwise map can change the overload, although the ambient
host may contain many alternative, cap-migrating diagonals.  This is an
obstruction to protected-map repair, not to existence of some other cap
map.  The exact symbolic proof is Theorem 4.1 of

```text
MATH_THEOREM_R_TWO_COORDINATE_SIDE_TURN_FOREST_AND_CAPACITY_CUT_20260731.md
```

whose SHA-256 is

```text
74dd8c45844e249f94d879469a78538dfee4b1b0b4582ea6d701c20e4cd6fe7a.
```

## 5. A colour-invariant host cut

After arbitrary forced-row propagation, let
\(\mathcal W\subseteq\mathcal V\) be residual cap targets and let
\(X_0\subseteq\mathcal X\) contain both
physical corners of every surviving atom incident with a target in
\(\mathcal W\).

### Proposition 5.1 (protected-corner capacity cut)

Every exact side factor satisfies

\[
                    2|\mathcal W|\le
                    \sum_{x\in X_0}c(x).             \tag{5.1}
\]

The inequality remains necessary after every sequence of inter-colour
Kempe switches, alternating circuits, ears, or absorber state changes that
uses only atoms of the same fixed host `G_Q`.

#### Proof

Every selected target in \(\mathcal W\) consumes two distinct corner slots,
both in `X_0`.  Slots have total capacity given by the right side.  A
recolouring changes which host atoms are selected but cannot create a new
host atom or slot, so the same count remains necessary.  \(\square\)

### Exact `n=3` obstruction

On the authenticated literal child/common-basis fixture, after two forced
targets the four residual caps are

```text
{1f,2f,37,3b}.
```

Every surviving atom for them uses only

```text
X_0={0f,17,1b,27,2b,33}.
```

Only `0f` is not an anchor.  Therefore

\[
             \sum_{x\in X_0}c(x)=2+5=7<8=2|\mathcal W|. \tag{5.2}
\]

The fixture has a genuine two-sided synchronized common deletion basis and
perfect outer incidence matchings, but its upper shore has no degree-capped
physical representative.  Thus even access to a complete proper colouring
of all host atoms cannot yield an exact colour class or exchange packet in
this host.

The retained independent replay is

```text
scratch/audit_catalan_a1_side_turn_capacity_cut_20260731.py
scratch/catalan_a1_side_turn_capacity_cut_20260731.audit.json
```

with SHA-256 values

```text
ddcad2ee21ff83d939274a79e46fc3b125977ceef119cd1219f01fe14a392ec4
398cfbecaabec84a982dc81015a56af841b456da3838417c32cc46068f33430f
```

and replay payload

```text
3f2ecae3c78afdd514d88fafdce8bf5dc68ccf7edaf7d9245c18daa226ecb934.
```

The audit returns
`PASS_INDEPENDENT_A1_SIDE_TURN_CAPACITY_CUT`.  It excludes this fixed
common basis, not every common basis of the child, and is not an
asymptotic obstruction.

## 6. Exact surviving cover-down target

For a favorable fixed common basis `Q`, an exact protected cover-down from
the full conflict-free colouring is sufficient if it supplies an ordered
packet system satisfying:

1. final saturation of both outer palettes;
2. prefix slot feasibility, including every protected seam anchor;
3. prefix graphic feasibility after contraction of the frozen
   central-plus-seam forest;
4. avoidance of the protected cap-bottom bank in every nonparallel outer
   circuit; and
5. all host cuts (5.1), including their residual versions after forced-row
   propagation.

The common Boolean cap then follows for free from Theorem 2.1.  What is
still missing is an existence theorem producing such a serializable packet
system from the distributed colour reservoir.  Delcourt--Postle controls
individual colour classes and bounded forbidden configurations; it does
not prove these correlated exact rows.

Finally, the maximal-envelope/common-cap compiler used for the eventual
contiguous-OR word has additional same-cell and blocker-cover constraints.
Those are not vertices of `G_Q`; they must be regenerated or protected by
a separate compiler theorem.  No compiler, exact Catalan side factor, or
`nu=B` statement is claimed here.
