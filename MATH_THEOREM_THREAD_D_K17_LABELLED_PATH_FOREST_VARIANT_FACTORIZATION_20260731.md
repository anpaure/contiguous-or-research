# Labelled path-forest variants: the exact component rethread catalogue

Date: 2026-07-31  
Status: dimension-uniform exact factorization and sharp local obstructions;
no repaired `K17` chronology or word is claimed

## 0. Verdict

The `724` short owner runs trapped in `257` fixed complementary components
cannot be repaired by reordering those components.  The right local object
is not a scalar “variant bit.”  It is a **resource-exact labelled path
forest** on a chosen packet of old components.

For a packet with owner set `O`, lower-colour set `L`, and `t` input
components, the exact local equations below select:

* every owner in `O` once;
* every lower colour in `L` once, either on an internal Johnson edge, at one
  nonempty path endpoint, or as one empty port component; and
* an acyclic directed path cover.

They imply, rather than assume, that the output has exactly `t` components.
Consequently:

1. a one-component catalogue contains only one-component rethreads;
2. a genuine split cannot be a resource-neutral one-component operation;
3. every genuine split must be accompanied by a merge in the same packet;
   and
4. the first exact split catalogue is the two-component catalogue.

This is the missing structural meaning of the earlier “six-socket” escape.
The `106` relaxed floor is only a lower bound on the number of components
which cannot be left in their old state when whole-bank migration is also
allowed.  With the marked bank fixed at `4108` owners, all `257` defective
components must instead be touched by a nonidentity labelled-forest packet.

The output of a local catalogue entry has a canonical compositional
signature: exact owner and colour resources, labelled endpoint sockets, a
capped run transfer, a literal depth-two collar, and an interval-union
transfer.  These signatures compose along the residual `U`-owner connector
cycle.  Common-cap feasibility does **not** reduce to another bounded scalar
signature: the exact target-labelled host relation (or the final global
rank-three recourse) must remain.

## 1. Resource packet

The theorem is stated at general owner rank `r`.  Let `O` be a finite set of
rank-`r` owners and let `L` be a finite set of rank-`r-1` lower colours.
Assume that `O,L` are the unions of the resources of `t` disjoint input path
components.  A nonempty input component

\[
       q_1,\ldots,q_s
\]

with endpoint colours `c_-,c_+` contributes the owner set
`{q_1,...,q_s}` and the colour set

\[
 \{c_-,q_1\cap q_2,\ldots,q_{s-1}\cap q_s,c_+\}.       \tag{1.1}
\]

An empty port component at colour `c` contributes no owner and the singleton
colour set `{c}`.  Exact lower rainbowness of the input gives disjoint colour
sets, and therefore

\[
                         |L|=|O|+t.                  \tag{1.2}
\]

For `K17`, take a packet of the `4871` complementary components after the
fixed marked packet is contracted.  The two marked-to-complement boundary
facets are outside the packet and are handled by the outer connector state.

## 2. The exact labelled path-forest equations

For distinct owners `u,v in O` with Johnson distance one and
`u cap v in L`, use a directed internal-edge variable

\[
                         x_{uv}\in\{0,1\}.           \tag{2.1}
\]

For `c in L`, `u in O`, `c subset u`, use endpoint variables

\[
               s_{cu},e_{cu}\in\{0,1\},             \tag{2.2}
\]

meaning respectively that `c` is the incoming/start socket of the path
whose first owner is `u`, or the outgoing/end socket of the path whose last
owner is `u`.  Finally, `z_c` selects the empty component at colour `c`.

Impose the owner rows

\[
 \sum_{v}x_{vu}+\sum_{c\subset u}s_{cu}=1
       \qquad(u\in O),                               \tag{2.3}
\]

\[
 \sum_{v}x_{uv}+\sum_{c\subset u}e_{cu}=1
       \qquad(u\in O),                               \tag{2.4}
\]

the exact colour rows

\[
 z_c+\sum_{u:c\subset u}(s_{cu}+e_{cu})
 +\sum_{\substack{\{u,v\}\subset O\\u\cap v=c}}
                  (x_{uv}+x_{vu})=1
       \qquad(c\in L),                               \tag{2.5}
\]

and the acyclicity rows

\[
             \sum_{u,v\in A}x_{uv}\le |A|-1
 \quad(\varnothing\ne A\subseteq O).                \tag{2.6}
\]

The sums in (2.3)--(2.4) range only over available Johnson neighbours in
`O`.  An outer connector owner incident with socket `(c,u)` must contain
`c` and be different from `u`; that constraint belongs to the outer
connector matching, not to (2.3)--(2.6).  An empty component selected by
`z_c` exports two distinct socket *occurrences* with the same label `c`, but
uses the lower colour `c` only once.

### Theorem 2.1 (labelled path-forest equivalence)

The integral solutions of (2.3)--(2.6) are in bijection with the oriented
path forests which:

1. cover every owner in `O` exactly once;
2. use every colour in `L` exactly once among internal intersections,
   nonempty path endpoints, and empty components; and
3. have exactly `t` components, where `t=|L|-|O|` is the number of input
   components.

The literal facet block of a nonempty output path

\[
 u_1,\ldots,u_m
\]

is

\[
 \Phi=(c_-,u_1\cap u_2,\ldots,u_{m-1}\cap u_m,c_+), \tag{2.7}
\]

and an empty output has `Phi=(c)`.  The `Phi` blocks of all outputs
partition `L`.

#### Proof

Rows (2.3)--(2.4) give every owner one predecessor-or-start and one
successor-or-end.  Thus every connected component of the selected directed
graph is a directed path or a directed cycle.  Row (2.6) excludes the
cycles.  Row (2.5) says exactly that every internal edge colour, endpoint
colour, or empty-component colour is used once.  It also excludes the two
orientations of one undirected edge simultaneously.

Let `p` be the number of nonempty paths and `e=sum_c z_c`.  The paths have
`|O|-p` internal edges and `2p` endpoint colours, so (2.5) gives

\[
 |L|=(|O|-p)+2p+e=|O|+p+e.                          \tag{2.8}
\]

By (1.2), `p+e=t`.  Formula (2.7) and (2.5) prove the partition claim.
Conversely, orient any such path forest and set precisely its internal,
endpoint, and empty variables.  All rows follow.  \(\square\)

This theorem is an exact catalogue representation: it generates whole
component variants without first enumerating exponentially many literal
orders.

## 3. Sharp arity and circuit consequences

### Corollary 3.1 (one-component catalogue)

For `t=1`, every integral solution is one nonempty path (unless `O` is
empty, when it is one empty port).  Hence the smallest resource-neutral
actuator on one old component is a same-resource rethread, not a split.

In particular, for an old nonempty component `C`, the exact arity-one atlas
is the set of rainbow Hamilton paths on `O_C` whose two socket colours and
internal edge colours partition `L_C`.  It may change terminal owners and
socket labels, but it changes neither the global owner set, the global
lower palette, nor the component count.

### Corollary 3.2 (split forces merge)

Suppose a resource-neutral packet genuinely splits the owners of one input
component between at least two output components.  Then the packet contains
at least two input components, and at least one output component contains
owners from at least two input components.

#### Proof

Theorem 2.1 preserves the number of components.  If one input component has
incidence with two output components and no output mixes inputs, the number
of output components is strictly larger.  Therefore some output must mix
inputs, which is a merge, and the packet has arity at least two.  \(\square\)

For a single internal cut in one component coupled to one merge with a
second component, the transient path cover exposes the two old endpoint
sockets of each component and the two new cut sockets: six labelled socket
occurrences.  This is the precise minimal single-cut realization of the
previous “six-socket exchange.”  It is not a claim that every higher-order
actuator has literal support six.

### Proposition 3.3 (incidence-circuit normal form)

Let `Gamma_r` be the bipartite incidence graph between rank-`r-1` colours
and rank-`r` owners.  Regard a lower-rainbow owner factor as the incidence
subgraph in which a colour is joined to the two endpoints of its owner edge.
The signed difference of two same-degree, palette-preserving factors is a
balanced red-blue graph at every owner and every colour.  It therefore
decomposes conformally into simple alternating circuits.

The graph `Gamma_r` has no four-cycle.  Indeed, two distinct rank-`r-1`
colours `c,d` have at most one common rank-`r` owner, namely `c union d`
when that union has rank `r`.  Consequently the smallest nonzero
zero-current circuit has six incidence variables, and every support-six
circuit is exactly

\[
 K+a,K+b,K+c
 \quad\leftrightarrow\quad
 K+ab,K+bc,K+ca,                                    \tag{3.1}
\]

where `|K|=r-2` and `a,b,c` are distinct outside `K`.  Toggling the two
phases is the incidence-hex variant.

Equivalently, in the owner-edge exchange notation, deleting the old edge of
colour `c` and adding a different edge of that colour gives the signed
owner-degree column

\[
 b(c;uv)=\mathbf 1_u+\mathbf 1_v
          -\mathbf 1_{a_c}-\mathbf 1_{b_c}.          \tag{3.2}
\]

A set of such columns is zero-current exactly when

\[
                         \sum b(c;uv)=0.             \tag{3.3}
\]

There is no nonidentity one- or two-column packet in the Boolean incidence
geometry.  Three columns are minimal and give (3.1).

#### Proof

At every incidence vertex the red and blue degrees agree.  Pair a red and a
blue half-edge successively; this decomposes the signed support into
alternating closed walks, and splitting repeated vertices gives conformal
simple alternating circuits.  The no-four-cycle argument above excludes
support four.  A simple six-cycle has three colours whose common
intersection is a rank-`r-2` set `K`; their three remaining labels give
(3.1).  Reading its changed colour endpoints as owner edges gives three
columns satisfying (3.3).  \(\square\)

This theorem does **not** say that hexagons generate every factor change.
The conformal decomposition may contain simple alternating circuits of
length eight or more which do not themselves decompose into legal
incidence hexagons on the current factor face.

### Proposition 3.4 (boundary-current trail normal form)

For a local component packet, degrees need not close before its exported
sockets are attached.  After adjoining one formal boundary vertex to every
exported socket occurrence, the signed incidence difference decomposes
conformally into:

* simple alternating circuits; and
* alternating trails whose endpoints are precisely the nonzero entries of
  the signed boundary-current vector.

Thus a zero-current component rethread is a circuit packet, while a genuine
split exports paired trail endpoints.  Socket labels without the signed
current and its trail-end pairing are not a complete local signature.

#### Proof

At every nonboundary owner and colour the signed red-blue degree is zero.
Pair opposite-colour half-edges there.  The paired walks either close or
terminate at boundary half-edges.  Splitting a repeated internal vertex
gives simple circuits and trails without changing signs.  Conversely their
union realizes exactly the displayed boundary current.  \(\square\)

Thus the exact catalogue should be generated in the following order:

1. zero-current circuit entries, beginning with the three-column incidence
   hexagons of Proposition 3.3 and assigning each circuit to the smallest
   input packet containing its changed resources;
2. arity-one same-resource path rethreads not already represented by those
   circuits;
3. arity-two labelled path forests, which are the smallest genuine
   split/merge packets; and
4. larger packets only for components not serviced at smaller arity.

This is a completeness hierarchy, not a claim that hexagons or arity two
must suffice at `K17`.

## 4. K17 service rows and the 257/106 distinction

For every one of the `724` inherited strict owner runs, let `H` be its old
edge interval from the entering zero edge through the exiting zero edge.
Any repaired facet block must satisfy

\[
       \sum_{uv\in H}(x_{uv}+x_{vu})\le |H|-1.       \tag{4.1}
\]

This is necessary because retaining all edges in `H` preserves the old
`0 1^2 0` or `0 1^3 0` subword, possibly reversed.  It is not sufficient:
the new path order must also pass the exact capped-run and maximal-envelope
tests in Section 5.

The exact frozen hazard audit refines these rows as follows.

```text
arbitrary-adjacency interval transversal = disjoint packing       452
strict-macro rows: 227, restricted interior macro sites           155
tag/macro-join rows: 497, restricted existing join sites           305
```

The last two restricted optima are not additive: a mixed nonlocal packet
may hit rows from both classes.  The figure `452` is an unconditional lower
bound on the number of **distinct old owner adjacencies absent from the
final factor**, independent of how those deletions are packeted.  A
compatible pure-hex family deletes at most three old owner edges per hex,
so it contains at least

\[
                         \left\lceil452/3\right\rceil=151        \tag{4.2}
\]

hexes.  This is a packet-count bound only for the pure minimum-support hex
face; a larger circuit still pays its actual number of deleted old
adjacencies.

The `724` rows meet `257` fixed complement components.  If the marked owner
bank remains exactly the authenticated `4108` owners and packet supports do
not cross into it, each of those `257` components must belong to the support
of a nonidentity forest solution.  Otherwise all its old internal edges,
and hence at least one bad run, remain.

The earlier `106` floor concerns a weaker two-mode catalogue.  A
length-three-only component may instead be migrated wholesale to the direct
owner bank, where length three is residence-legal, at cost `c_C=|w_C|+1`.
A length-two component is still illegal in either bank.  With migration
variables `m_C`, rethread-service variables `r_C`, and owner-slot reserve
`3293`, the exact necessary rows are

\[
 r_C=1\quad(C\text{ contains a length-two run}),     \tag{4.3}
\]

\[
 r_C+m_C\ge1\quad(C\text{ has only length-three defects}),
                                                               \tag{4.4}
\]

\[
                 \sum_C c_Cm_C\le3293.              \tag{4.5}
\]

The audited sorted-cost calculation for (4.3)--(4.5) gives at least
`82+24=106` rethreaded components.  Equations (4.3)--(4.5) do not make the
rethreads independent, and they do not relax the component-conservation
theorem.  A migrated or split packet must still export its real sockets,
palette, run state, upper state, and cap effect.

## 5. The regenerative block signature

For every oriented output path block `B`, retain the following exact state.

### 5.1 Resource/socket state

\[
\mathsf S_0(B)=
 (O_B,L_B,c_-,u_1,c_+,u_m,\epsilon_B,\partial j_B),  \tag{5.1}
\]

where `epsilon_B` records the empty case.  Socket occurrences, not merely
their labels, are distinct, and `partial j_B` is the signed boundary current
with the trail-end pairing from Proposition 3.4.  The outer residual-owner column
`U:h -> h'` is legal exactly when the two socket labels are distinct facets
of `U`, each terminal owner is different from `U`, and the physical
occurrences have not been used.

### 5.2 Residence/inversion state

For every coordinate store its first and last bit, leading and trailing
positive-run length capped at three, and its internal short-run tokens.
Also store the first and last two literal rows of `Phi(B)` and whether all
strictly internal maximal-envelope rows replay.  Denote this state by

\[
                         \mathsf R_3(B).              \tag{5.2}
\]

Concatenation is the associative capped-run product.  The two-row literal
collars are sufficient because a new depth-two seam can change only the
five-row replay halo.  An entry is internally admissible only when its
internal defect set is empty.  Outer composition then detects every newly
created `0-1-0` or `0-1-1-0` collar and every empty three-window envelope.

For a depth-`d` all-dimension state, replace the cap three by `d+1` and keep
the first/last `d` literal rows.  A facet-mode owner path must export one
extra unit of run length relative to a direct owner-mode path, exactly as in
the odd-diamond residence-tax theorem.

### 5.3 Upper interval state

For a rank cutoff `h`, store

\[
 \mathsf U_h(B)=(\cup B,P_h(B),S_h(B),I_h(B)),        \tag{5.3}
\]

where `P,S,I` are the target-labelled multisets of unions of prefixes,
suffixes, and intervals, truncated above rank `h`.  The exact product is

\[
 I_h(AB)=I_h(A)\uplus I_h(B)
       \uplus(S_h(A)*P_h(B)),                         \tag{5.4}
\]

with the analogous prefix/suffix formulas.  Thus component variants can be
deduplicated before the outer connector solve by their transfer state.

At the present `K17` gate, `h=12` treats the three missing upper ranks.
Exact preservation of ranks `13,...,17` requires either `h=17` or explicit
protected witness tickets disjoint from the packet support.  Their current
zero-hole status alone is not a preservation proof.

### 5.4 Common-cap state

The block exports its literal two-row collars and its internal maximal
envelopes.  After the complete row `Z` is assembled, run the exact
target-to-singleton/adjacent-pair matching with the rank-three common-cap
conflict rows.

There is no sound replacement by a scalar number of hosts.  Two options can
have identical resource counts, socket counts, run states, and marginal
host degrees but different target-labelled rank-three conflicts.  The known
determinant-two common-cap obstruction distinguishes them.  Hence an exact
regenerative state must retain either:

1. the target-labelled internal host relation plus its boundary-conditioned
   matching relation; or
2. the literal block/envelope data and defer one global common-cap recourse.

The second is the smallest practical `K17` catalogue state.

### 5.5 Qualification of the minimum-hex state

The six incidence variables of a hexagon determine its factor change, but
they do not by themselves determine every downstream shadow/compiler
effect.  After the hexagon reconnects long retained fragments:

* residence is genuinely collar-local, through `R_3`;
* a newly gained arbitrary-width upper provider may use an arbitrarily long
  suffix and prefix of two fragments, so it requires `U_h`, not only the
  length-`d` socket collars; and
* a five-row cap halo is sufficient only when one fixed cap and its selected
  matching are transported on all unchanged fragment interiors.  For
  existential common-cap feasibility, the full target-labelled rank-three
  recourse remains necessary.

Accordingly, the bounded six-socket state in
`MATH_THEOREM_THREAD_D_K17_OPT28_MINIMAL_HEX_VARIANT_STATE_20260731.md`
is exact as an incidence/component column and as a residence collar.  Its
arbitrary-shadow/common-cap clause must be read with the `U_h` and guarded
fixed-cap qualifications above; literal collars alone are not complete for
those two gates.

## 6. Factorization and minimality theorem

### Theorem 6.1 (packet-to-global physicalization)

Partition the complement input components into packets.  For each packet
choose an integral solution of (2.3)--(2.6), and suppose:

1. packet owner and lower-colour resources are the original disjoint
   resources, so their unions preserve every complement owner and colour;
2. every output block is internally residence/inversion admissible;
3. the residual owner connector matching uses every output socket occurrence
   and every residual owner exactly once, is physically Johnson-legal, and
   together with the fixed marked packet forms one cycle;
4. the product of the `R_3` signatures is exact at every seam;
5. the product of the `U_h` signatures supplies and preserves every required
   upper target; and
6. the assembled literal row passes the exact common-cap recourse.

Then the expanded chronology preserves the fixed marked packet, every
rank-`r` owner, and every rank-`r-1` lower colour, and it is physically
valid through the stated residence, upper, and compiler gates.

Conversely, every marked-preserving, resource-exact component rethread
admits this factorization: take each connected packet of old components
touched by its new internal path edges, orient the resulting path forest,
and read off (2.1)--(2.6) and the signatures above.

#### Proof

Theorem 2.1 proves local owner and colour exactness and exports precisely
the socket occurrences needed by the connector master.  Connector
set-partition and connectivity produce the one owner cycle without changing
an internal resource.  The run and interval-union products are exact
concatenation identities, not marginal estimates.  The final target-labelled
cap recourse is necessary and sufficient for the chosen literal row.

For the converse, restrict the new internal edges to the union of old
components linked by them.  Owner degree one inside each path gives
(2.3)--(2.4), exact lower rainbowness gives (2.5), and the fact that these
objects are path components gives (2.6).  The literal output determines all
three signatures.  \(\square\)

### Theorem 6.2 (canonical minimal quotient)

Declare two packet variants equivalent when they have the same exact
resource/socket state and, in every legal left/right connector context,
induce the same residence acceptance, target-labelled interval-provider
multiset through the chosen cutoff, and boundary-conditioned common-cap
relation.  This equivalence is a congruence under concatenation.  Its
equivalence classes form the unique coarsest context-exact variant
catalogue.

The concrete state in Section 5 is a proof-carrying representative of this
quotient.  Dropping any of the following is unsound:

* owner or colour identities: exact ownership/rainbowness can collide;
* socket labels or terminal owners: residual-owner legality changes;
* capped run state or literal collar: the same interiors can differ at a
  `0-1-0`/`0-1-1-0` seam or at a nonempty-envelope test;
* target identities in `U_h`: equal profile counts can cover different
  masks; or
* the target-labelled cap relation: marginal Hall and permanent bits do not
  exclude the rank-three obstruction.

#### Proof

Contextual equivalence is reflexive, symmetric, and transitive.  If two
blocks are equivalent, adjoining the same legal block on either side merely
restricts the class of contexts, so equivalence is preserved by
concatenation.  Every context-exact quotient must separate two variants
which some context distinguishes; therefore it refines this quotient.  The
listed state coordinates are exactly the resources and transfer relations
used by the distinguishing tests.  \(\square\)

## 7. Exact next catalogue

The smallest complete stratified construction is now unambiguous.

1. Install the already frozen minimum-support incidence-hex catalogue:
   `44,917` alternating hexes, `27,933` avoiding marked owners, and `5,433`
   marked-safe hazard-active columns.  These cover all `724` rows and all
   `257` bad components; each row has degree at least two.
2. For each defective component not jointly serviceable by compatible
   hexes, generate its arity-one labelled path-forest solutions satisfying
   (4.1), internal `R_3`, and the literal envelope rows.
3. Deduplicate accepting entries by the Section 5 signature.
4. Only for components with no accepting arity-one entry, generate
   arity-two packets.  These are the first genuine split/merge variants.
5. Solve exact packet set partition plus the directed residual-owner socket
   circuit.  Install upper and common-cap rows on the assembled candidates,
   not on marginal component counts.
6. Increase packet arity only when a certified Hall/service obstruction
   excludes the smaller atlas.

This catalogue is strictly smaller in logical scope than the complete
`545721` marked-preserving edge-column master: it generates only the
component packets needed to service the immutable runs, while remaining
complete at each declared packet arity.  It is also stronger than a list of
`106` variant flags, because it carries the exact split/merge, socket,
upper, and cap correlations those flags omit.

## 8. Scope

Proved here:

* an exact integral generator for every resource-neutral component
  rethread on a fixed packet;
* exact component-count conservation;
* the split-implies-merge and minimal incidence-hex theorems;
* a compositional physical/upper signature; and
* the precise target-labelled common-cap state which cannot be scalarized.

Not proved here:

* that every one of the `257` `K17` components has an accepting arity-one or
  arity-two option;
* that the `106` relaxed lower bound is attainable;
* a connected residual socket circuit after variant selection;
* complete first-three upper-shadow repair; or
* a common cap or an optimal `K17` word.
