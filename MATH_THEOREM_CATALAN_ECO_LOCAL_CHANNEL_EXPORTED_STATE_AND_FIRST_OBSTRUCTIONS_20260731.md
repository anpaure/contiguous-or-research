# The ECO local-channel row is an exported linkage state

Date: 2026-07-31  
Status: exact data-separation theorem; exact ownership-resolved max-flow
criterion; exact first binary and rank-two separators; exact repaired
project-`m=5` singleton pass; no all-dimension channel construction

## 0. Verdict

The fixed-rotation ECO word determines the six port occurrences, the two
possible support conflicts and the component rank

\[
                         \rho(Z)=|\mathcal C(Z)|-1.
\]

It does **not** determine the occurrence-linkage network, the source set, the
sink bank or the child-router exclusions.  Consequently the local-channel
lemma in
`MATH_THEOREM_CATALAN_ECO_OCCURRENCE_CONFLICT_PATH_AND_ROUTER_GATE_20260731.md`
cannot be proved from ECO genealogy alone.

This failure is already ownership-sensitive at paper parameter `n=3`.  The
binary atom `D=1100` and its neighbour `1010` share the old factor edge on
the two ports

```text
1100100  1101100
```

and have `rho=1`.  Two directed routers with exactly the same atom, ownership
bit, component effect and terminals can route the source before ownership;
after the shared edge is assigned away, one still routes and the other does
not.  The distinction is only the internal directed network.

The grouped-rank version first appears at `n=5`.  The atom

```text
D = 11010010
```

meets three factor components, has `rho=2`, and has both a predecessor and a
successor in the ECO conflict path.  Assigning both shared old edges away
leaves exactly the two ports

```text
11010001100  11010011100.
```

There is a residual router in which these two sources have disjoint direct
paths to distinct sinks, and another in which each source is individually
routable to its own sink but the two paths share one capacity-one vertex.
The former has linkage rank two and the latter rank one.  Thus even
individual routability of all unit sources is insufficient.

The strongest literal positive file is sharply smaller.  The repaired
project-`m=5` atom `g1=Z(101100)` is binary, has no fixed-rotation support
conflict, and its compiled postrepair network explicitly contains

```text
s_g1 -> z_g1.
```

It therefore passes the ownership-resolved local test with rank one.  This
is a finite singleton bypass: toggling `g1` changes component orders
`120+132 -> 252`, and the separately authenticated socket file closes the
result.  It is not a physical all-`m` route construction, and it supplies no
rank-two atom or child-bank induction.

The positive project-`m=4` merge fixture exports ports, coherence,
component orders and a leaf-peelable gap splice, but no directed occurrence
network/source/sink tuple.  Its local-channel status is therefore
**undecidable from that artifact**, not negative.

## 1. Exact ownership-resolved interface

Fix one selected atom `Z`.  Let `E_sh(Z)` be its at-most-two
genealogy-shared old edges.  For every ownership state

\[
                         Q\subseteq E_{\rm sh}(Z),
\]

where the edges in `Q` are assigned away, an exact exported local-channel
state consists of:

1. a finite directed unit-vertex-capacity network `N_(Z,Q)`;
2. a set `S_Z={s_1,...,s_rho}` of **distinct** unit sources;
3. a local sink bank `T_(Z,Q)` with unit sink capacities;
4. the literal embedding of every network vertex in the parent occurrence
   router;
5. the forbidden child-router vertex bank `B_(Z,Q)`;
6. the deletion map for the two ports of every edge in `Q`; and
7. the semantic map from the `rho` source channels to the `rho` edges of
   the chosen component unit expansion `R_Z`.

The last field is load-bearing for a ternary atom.  If the physical
operation is all-or-none and no surviving suboperation realizes one unit
edge independently, two abstract paths must not be promoted to two live
component edges.  In that case the exported object must instead carry the
grouped atomic kill relation.

Split every allowed network vertex into an in/out pair with a capacity-one
arc.  Attach a supersource to every member of `S_Z`, and every allowed sink
to a supersink, all with capacity one.  Delete

\[
 B_{Z,Q}\cup V(Q)
\]

before taking the flow, where `V(Q)` is the set of assigned-away port
occurrences.

### Theorem 1.1 (exact local-channel oracle)

For a fixed ownership state `Q`, the required `rho(Z)` unpaired channels
exist if and only if

\[
 \boxed{\operatorname {maxflow}
   (N_{Z,Q}-B_{Z,Q}-V(Q);S_Z,T_{Z,Q})=\rho(Z).}       \tag{1.1}
\]

The complete ownership-robust local-channel row holds if and only if (1.1)
holds for all at most four states `Q`.

#### Proof

Integral max flow in the vertex-split network is exactly a family of
vertex-disjoint directed paths from the distinct sources to distinct sinks.
Every such path family gives a flow of value `rho`, and integrality
decomposes every value-`rho` flow into such paths.  There are at most two
shared edges, hence at most four ownership states.  The semantic unit-edge
map is an explicit hypothesis rather than a consequence of max flow. \(\square\)

If source--sink pairings are prescribed, replace the unpaired max-flow row
by the pairing-resolved linkage relation.  If the source identities or the
network change with `Q`, all four literal states must be exported; a scalar
rank at `Q=empty` is insufficient.

## 2. First binary data separator

At paper `n=3`, put `Z=Z(1100)` and `Z'=Z(1010)`.  Their port supports
intersect exactly in the old edge

\[
       e=\{1100100,1101100\},                       \tag{2.1}
\]

and `rho(Z)=1`.  Let `p=1101000` be any private port of `Z`, and fix one
abstract source `s` and sink `z`.

Consider two unit-capacity networks.  The private router has the path

\[
                         s\longrightarrow p\longrightarrow z,     \tag{2.2}
\]

while the public router has

\[
                     s\longrightarrow1100100\longrightarrow z.  \tag{2.3}
\]

Both have linkage rank one before ownership.  Assigning (2.1) to `Z'`
deletes both shared ports.  Network (2.2) still has rank one; (2.3) has rank
zero.  All ECO data outside the directed network are identical.  This is the
first possible separator because paper `n=2` has no support conflict.

## 3. First rank-two data separator

At paper `n=5`, take `D=11010010`.  Its two neighbours are
`11010100` and `11001010`; the shared old edges are

\[
\begin{split}
 e_1&=\{11010100100,11010101100\},\\
 e_2&=\{11010010100,11010110100\}.                 \tag{3.1}
\end{split}
\]

The atom meets the three components with representatives

```text
1010101100  1010110100  1010111000
```

and therefore has `rho=2`.  After assigning both edges in (3.1) away, its
residual ports are

\[
                    p=11010001100,\qquad q=11010011100.            \tag{3.2}
\]

With distinct sinks `z_1,z_2`, the private network

\[
                         p\to z_1,\qquad q\to z_2                 \tag{3.3}
\]

has rank two.  The bottleneck network

\[
                 p\to x\to z_1,\qquad q\to x\to z_2             \tag{3.4}
\]

has rank one, although each source is separately routable to a distinct
named sink.  Thus the rank-two row is a genuinely joint local linkage test.

This is a data-separation obstruction, not a proof that the literal ECO
atom fails in every prepared router: (3.3) proves that its port data are
compatible with a passing export.

## 4. Literal finite files

### 4.1 Repaired project-`m=5`

The authenticated file

```text
scratch/catalan_m5_repaired_parallel_catalogue_20260731.audit.json
```

exports the fixed network

```text
vertices  s_g0 s_g1 z_g0 z_g1
arcs      s_g0->z_g0, s_g1->z_g1
sinks     z_g0 z_g1.
```

For the selected singleton `{g1}`, `D=101100` has no conflict neighbour and
`rho=1`; hence there is only the empty ownership state and (1.1) is one.
The independent physical audits additionally verify the six ports
`51,53,55,57,59,61`, the merge `120+132 -> 252`, and the final Hamilton
socket closure.  The source file explicitly qualifies this network as a
compiled representation of the pre-certified finite cube, not a globally
private physical alternating route for an all-dimensional family.

### 4.2 Project-`m=4`

The item-2171 file

```text
scratch/threadD_item2192_catalogue_jointness_20260731.audit.json
```

authenticates the coherent merge on ports `19,21,23,25,27,29`, with common
labels `(d,e)=(6,0)` and component orders `28+42 -> 70`.  The separate
leaf-peelable file authenticates its matching/gap state.  Neither file names
a directed router, sources, sinks or child exclusions.  The max-flow oracle
therefore has no input.  Socket connectors from the decorable `ML(7)` lift
are a different occurrence-cycle coordinate and must not be substituted for
this missing linkage state.

## 5. Consequence for the all-dimension programme

The ECO conflict-path theorem has completely reduced **bank ownership**.
The remaining channel claim is neither a Catalan enumeration nor another
global packing theorem.  It is an exported finite relation at every atom:

\[
 \boxed{
   Q\longmapsto
   (N_{Z,Q},S_Z,T_{Z,Q},B_{Z,Q},\text{unit-edge semantics})
   \quad\text{with flow value }\rho(Z).}             \tag{5.1}
\]

A recursive proof may establish (5.1) by reserving literal private tubes,
or it may propagate the full pairing-resolved boundary-linkage signature.
Without one of those exports, the all-`m` ECO local-channel lemma is
underdetermined.  The repaired project-`m=5` singleton shows that a finite
repair can compile the relation directly; it does not show that raw ECO
genealogy supplies it uniformly.

## 6. Audit

Run

```text
python3 scratch/audit_catalan_eco_local_channel_exported_state_20260731.py
```

The audit reconstructs the two literal ECO separators, evaluates all tiny
vertex-capacitated flows, and cross-checks the authenticated project-`m=4,5`
files.  It does not fabricate a router for project `m=4` or promote the
compiled project-`m=5` arc to a physical all-dimensional route.
