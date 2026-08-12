# `B_5` address transport: double-coset obstruction, relay holonomy, and the exact bounded-defect host gate

**Date:** 2026-08-02  
**Status:** unconditional abstract transport and deficiency theorems, with an
exact specialization to the one planted K17 module.  Existence of an
all-`k` phase-common host satisfying the resulting conditions remains
**UNPROVED**.  Section 6 proves only a conditional `B+1`/`B+O(1)`
implication; no unconditional chronology or new value of `nu(k)` is claimed.

## 0. Outcome

A nontrivial bottom relay cannot keep both the named bottom shore and the
physical suffix-slot shore pointwise fixed.  The exact local condition is a
paired-interface equation in the automorphism group of the **carried**
protected host.  It becomes a double-coset condition only when the bottom and
slot actions factor.  Literal pointwise address preservation is the special
case in which both shores are fixed, and then every nonidentity `C10` or `C6`
is impossible.  Internalizing an address is sufficient only when its induced
permutation extends to an automorphism of every exterior consumer; deck
equality alone is not sufficient.

For a factorized slot interface this recovers the usual clone condition as
an equivalence, not merely a sufficient test: the five slots of a `C10`, or
the three slots of a `C6`, must lie in one complete-column clone class.
Allowing transport on the bottom/address shore can evade that conclusion,
but then the corresponding bottom/address permutation must itself be a
protected automorphism.

Local transports glue along a relay network exactly when their groupoid
holonomy is trivial on every closed walk and agrees with every fixed boundary
pin.  A relay path has no internal holonomy obstruction and carries one
unfixed terminal port.  Consequently a path cover of `p` opened modules by
`c` clean relay chains leaves exactly `c` live `P2` sidecars; bounded sidecar
requires `p-c` legal relay identifications, not merely `p` independently
openable modules.

Finally, full rooted Hall is stronger than is needed on the host-selection
row.  Under complete opener-footprint privacy, the exact number of unopened
compressed cycles is the Hall deficiency

\[
 \delta=\max_{I} (|I|-|N(I)|).
\]

Thus an additive-constant route may leave `delta=O(1)` only if those bounded
cycles have a separately certified bounded literal serialization repair;
an exact forest needs `delta=0`.  Without opener-footprint privacy the exact
object is a set-packing hypergraph and ordinary Hall is not sufficient.

For one compatible regenerative spine, an automorphism of every unused
compatibility column is stronger than necessary.  It is enough to transport
one selected complete certificate: its current and earlier-prefix matchings,
its carry, aperture, reset/history/residence and upper/source/supplier
witnesses, and every capacity-one address which that certificate actually
uses.  The universal rank-oracle condition remains the appropriate stronger
form when every carry must work.  Realizing arbitrary phase vectors is a
different requirement, governed by serial/hypercube coherence of the chosen
transports.

The weakest host-side replacement is therefore an incumbent-aligned bank
whose carried-interface matching changes satisfy the paired-interface test
(the double-coset test on a proved factorized interface),
whose uncovered cyclic nullity plus rooted deficiency is bounded, and whose
safe relay graph has bounded path-cover number and admissible holonomy.
The terminal compiler need not be part of the phase-common automorphism: by
phase decoupling and bounded eviction it may instead have a uniformly
bounded complete damage set.  This is a genuine weakening of the earlier
pointwise address/history/reset/residence/compiler formulation.

## 1. The exact two-shore transport criterion

Let `B` be a set of named bottom tokens and `V` a set of physical suffix
slots of the same cardinality.  Two modes of one bottom relay are bijections

\[
                         \mu_0,\mu_1:B\longrightarrow V.       \tag{1.1}
\]

Let `R^0,R^1` be the complete relational structures carried to the next
transition in the two modes, apart from the distinguished occupied-pair
relation (1.1).  They include every address, state, reset,
aggregate-history, residence, source, upper, supplier, or other occurrence
relation that is actually read later.  Relations and functions are
interchangeable here by replacing a function with its graph.  Let `E` be
the exterior objects which must remain pointwise fixed, and let

\[
 I_{01}=\operatorname{im}\left(
   \operatorname{Iso}_E(R^0,R^1)\longrightarrow
   \operatorname{Sym}(B)\times\operatorname{Sym}(V)
                         \right).                    \tag{1.2}
\]

Thus `(alpha,beta) in I_01` means that some isomorphism of the two **full**
carried structures fixes `E` pointwise and restricts to `alpha` on `B` and
`beta` on `V`.  This definition includes all internal-address and
propagated-history guards; equality of unary signatures is not silently
substituted for it.  When `R^0=R^1=R`, this restriction set is the group

\[
 G=\operatorname{im}\bigl(\operatorname{Aut}_E(R)
       \longrightarrow\operatorname{Sym}(B)\times
                         \operatorname{Sym}(V)\bigr).
\]

### Theorem 1.1 (protected matching transport)

There is a protected equivalence from mode zero to mode one fixing `E`
pointwise if and only if there is `(alpha,beta) in I_01` such that

\[
                         \boxed{\ \beta\mu_0=\mu_1\alpha\ }.   \tag{1.3}
\]

#### Proof

An old occupied pair `(b,mu_0(b))` is sent by an isomorphism restricting to
`(alpha,beta)` to

\[
             (\alpha b,\beta\mu_0(b)).                         \tag{1.4}
\]

It is an occupied pair of mode one for every `b` exactly when its second
coordinate is `mu_1(alpha b)`, which is (1.3).  This proves necessity.
Conversely, an isomorphism represented by an element of `I_01` satisfying
(1.3) maps the complete old matching graph onto the complete new matching
graph while fixing every exterior object and mapping every relation of
`R^0` to its mate in `R^1`.  It is the required protected equivalence.
\(\square\)

On a common host `R^0=R^1=R`, if the carried structure has independent shore automorphism groups
`G_B,G_V`, so that `G=G_B\times G_V`, equation (1.3) is equivalently the
double-coset condition

\[
                            \mu_1\in G_V\mu_0G_B.              \tag{1.5}
\]

The formulation (1.3), not (1.5), is the correct one when histories or
addresses impose joint bottom-slot relations.

### Theorem 1.2 (selected-certificate version)

Fix one complete certificate `C_0` in mode zero.  It contains one current
placement (with the local occupied-pair relation distinguished), one
completion of the earlier prefix, one realized carry, one
accepted endpoint/aperture and reset state, the full selected aggregate
history and residence state, selected upper/source/supplier witnesses, and
every capacity-one cell used by these objects.  Let `I_01^sel` be the paired
bottom/slot restrictions of maps which fix the declared exterior, send every
selected object of `C_0` other than that distinguished local matching to a
legal mode-one object, and are injective on all selected physical cells.

The selected certificate transports through the relay if and only if some
`(alpha,beta) in I_01^sel` satisfies

\[
                         \beta\mu_0=\mu_1\alpha.       \tag{1.6}
\]

No equality of unused compatibility columns or unused history states is
required.  If, instead, occurrencewise transport must work for every carry
and exterior state, then the complete-structure condition of Theorem 1.1 is
required.  For universal **rank-level reserve-carry feasibility** alone, the
weakest condition is the two rank conjugacies

\[
 r_{L^1}(\phi X)=r_{L^0}(X),\qquad
 r_{K^1}(\phi X)=r_{K^0}(X)\quad(X\subseteq H),       \tag{1.7}
\]

together with transport of the occupied support.  Transport of every
boundary relation must be added for the corresponding protected universal
claim.  These rank identities preserve all matroid-intersection cuts but do
not assert equality of presenting graphs or transport every presenting
matching.

#### Proof

The occupied-pair relation in the selected certificate transports exactly
under (1.6), by the proof of Theorem 1.1.  Every other selected object and
every used capacity-one cell transports by the definition of `I_01^sel`.
These objects constitute a complete witness, so unused graph edges and
unused states are irrelevant.  Conversely, any transported selected
certificate restricts to a member of `I_01^sel`, and its occupied matching
forces (1.6).  The rank-level universal statement is the exact rank-oracle
criterion for the two contracted matroids; Theorem 1.1 remains the stronger
occurrencewise statement.  \(\square\)

This is the logical quantifier needed by the earlier one-compatible-spine
reduction.  It does not produce that spine.

### Corollary 1.3 (the two gauges and the raw pointwise no-go)

If bottoms are fixed pointwise, then the only possible slot transport is

\[
                    \beta=\mu_1\mu_0^{-1}.                    \tag{1.8}
\]

If slots are fixed pointwise, then the only possible bottom transport is

\[
                    \alpha=\mu_1^{-1}\mu_0.                   \tag{1.9}
\]

If both shores are fixed pointwise, (1.3) holds if and only if
`mu_0=mu_1`.  Hence no nonidentity `C10` or `C6` can be protected under that
raw interpretation.

This separates two legitimate but different repair strategies.

1. **Token gauge:** fix each named bottom and transport the suffix slots by
   (1.8).  Then the complete slot-inherited owner/history/residence column
   must be equivariant under that slot cycle.
2. **Root gauge:** fix each physical suffix slot and transport the bottom,
   lower, and induced tail/address objects by (1.9).  Then every consumer of
   those named objects must be equivariant under the bottom/address cycle.

One may also use a mixed element `(alpha,beta)`, but it still has to satisfy
the full relational condition (1.3).  Merely declaring changed addresses
"internal" does not manufacture such an automorphism.

### Definition 1.4 (exact unmatched-port obstruction)

For either the complete or selected interface put

\[
 \delta_{\rm if}=
 \min_{(\alpha,\beta)\in I}
 \bigl|\{b\in B:\beta\mu_0(b)\ne\mu_1\alpha(b)\}\bigr|,       \tag{1.10}
\]

with value `+infinity` when `I` is empty.  This is exactly the least number
of assignment ports not transported by an allowed interface map, and
`delta_if=0` is equivalent to exact transport.  It is not automatically a
source-length or sidecar-token count: one repair gadget might cover several
ports.  For the clean `B+1` route, `delta_if=0` is the proof-safe condition
unless every mismatched port is proved to lie in the dependency closure of
the already charged reset token.

On the raw assignment-only interface, where `(id,id)` is the allowed map,
fixing both shores gives one 5-cycle and one 3-cycle, hence `delta_if=8` for
an opened one-socket module; `p` complete-footprint-disjoint modules have
`delta_if=8p`.  On a protected fixed-shore interface the value is 8 when an
exterior-fixed map exists and `+infinity` otherwise, so it is at least 8.
At physical-root resolution this is eight changed occurrence columns, or
sixteen changed scalar lower/tail fields, per module.  Thus charging `O(1)`
fresh pointwise-address exceptions per actuator is sharply linear and cannot
prove a bounded sidecar.

### Corollary 1.5 (serial and hypercube quantifiers)

For a prescribed serial order of modules, suppose all phase structures
`R^0,...,R^p` live on one frozen typed universe and, for every `j`, there is
an exterior-fixed isomorphism `f_j:R^(j-1)->R^j` satisfying (1.3) for the
`j`th matching change.  Then every prefix phase is protected-equivalent to
the initial phase by the composite `f_j ... f_1`.

For an independently toggleable bank, a checkable stronger condition is a
common background `R` and automorphisms `tau_1,...,tau_p` which satisfy
(1.3), preserve both local modes of every other module, and commute
pairwise.  Then

\[
                       \tau_1^{\epsilon_1}\cdots
                       \tau_p^{\epsilon_p}             \tag{1.11}
\]

gives a protected realization of every phase vector
`epsilon in {0,1}^p`.

#### Proof

The serial assertion is closure of isomorphisms under composition.  In the
second assertion, preservation of every other local mode means each factor
changes only its selected matching relation; commutativity makes (1.11)
independent of order.  Thus the product changes exactly the modules with
`epsilon_j=1` and preserves the common exterior.  \(\square\)

Separate two-phase witnesses on separately chosen hosts do not satisfy the
serial hypothesis.  Likewise, individual local transports do not imply a
path-independent hypercube.  A square commutator must act identically for a
universal coordinate trivialization, and must at least fix the selected
state for a selected certificate.  A fixed serial order can remain valid
without commuting generators.

## 2. Clone classes are exact on a factorized frozen exterior

Assume temporarily that `R^0=R^1=R`, that the bottom shore is pointwise
fixed, and that the slot-dependent part of the carried structure has no
relation containing two movable slots.  For `v in V`, let `c(v)` be
its complete column against the pointwise-fixed exterior: all colours,
function values, and incidences in carried relations containing `v` and
otherwise only exterior objects.  Put

\[
                            v\sim w\iff c(v)=c(w).              \tag{2.1}
\]

Then the slot automorphism group fixing the exterior is exactly the direct
product of the symmetric groups on the equivalence classes of `sim`.

### Theorem 2.1 (cyclewise clone equivalence)

In token gauge, a relay whose relative slot permutation
`rho=mu_1 mu_0^{-1}` is one cycle is protected if and only if every slot in
that cycle has the same complete column.  In particular:

* a saturated `C10` is protected exactly when its five slots form one
  complete-column clone class; and
* a rooted `C6` is protected exactly when its three slots form one
  complete-column clone class.

#### Proof

By Corollary 1.3, token gauge forces `beta=rho`.  A permutation belongs to
the product of the symmetric groups on the clone classes exactly when each
of its cycles is contained in one class.  The relative permutations of the
two circuits are respectively a 5-cycle and a 3-cycle.  \(\square\)

The factorization hypothesis is load-bearing.  If a propagated history
contains two or more internal occurrences, unary column equality need not
preserve it; Theorem 1.1 must then be applied to the complete relational
structure.

### Theorem 2.2 (coherent-orbit criterion under an allowed symbol action)

Let `rho` permute the movable slots and let `sigma:V->Sigma` be one
slot-inherited subcolumn.  There is a bijection `g` of `sigma(V)` satisfying

\[
                         \sigma(\rho v)=g\sigma(v)\qquad(v\in V)       \tag{2.2}
\]

if and only if

\[
 \sigma(v)=\sigma(w)\quad\Longleftrightarrow\quad
 \sigma(\rho v)=\sigma(\rho w)\qquad(v,w\in V).              \tag{2.3}
\]

When `rho` is an `ell`-cycle, the resulting `g` satisfies `g^ell=1` on
`sigma(V)`.  Equation (2.2) is only a subcolumn test: `g` must still extend
to one allowed automorphism of every carried relation.

#### Proof

Any bijection `g` preserves equality, proving necessity.  Under (2.3), set
`g(sigma(v))=sigma(rho v)`.  The equivalence makes this well-defined and
injective; finiteness makes it bijective.  Iterating around an `ell`-cycle
gives `g^ell sigma(v)=sigma(v)`.  \(\square\)

Thus clone equality is the identity-action case.  A nonconstant cycle can
be transported only when it is a coherent orbit of an automorphism with
semantic meaning; an arbitrary renaming of colour names is not enough.

### Proposition 2.3 (injective decoder obstruction)

Suppose the carried structure contains the graph of an injective map
`d:V -> E` into pointwise-fixed exterior names.  Then every slot
automorphism fixing `E` is the identity.  The analogous statement holds on
the bottom/address shore.

#### Proof

For an allowed `beta`, preservation of the graph of `d` gives
`d(beta v)=d(v)`.  Injectivity gives `beta v=v` for every `v`.  \(\square\)

This includes literal named-address preservation as a special case.  It
also proves a quantitative zero: if either shore is fixed and the other has
an injective frozen decoder, the maximum number of nonidentity protected
circuits is **zero**, no matter how many uncoloured sockets the host
contains.

## 3. The literal `B_5` transport cycles

For a saturated `C10`, use cyclic rim coordinates `k_i`, physical suffix
slots `v_i`, and old bottoms

\[
 B_i=C+a+k_i,qquad \mu_0(B_i)=v_i,qquad
 \mu_1(B_{i+2})=v_i.                                      \tag{3.1}
\]

Indices are modulo five.  Its token-gauge slot transport and root-gauge
bottom transport are

\[
 v_i\longmapsto v_{i-2},qquad
 B_i\longmapsto B_{i+2},                                  \tag{3.2}
\]

both 5-cycles.  If

\[
 T_i=C+a+k_i+k_{i+1}                                      \tag{3.3}
\]

is the old induced co-middle/tail at physical slot `v_i`, then root gauge
forces

\[
                             T_i\longmapsto T_{i+1}.        \tag{3.4}
\]

Thus the five literal tail names also form a 5-cycle.  The rooted opener
has the identical statement with 3-cycles on its three shores.

Equation (3.4) explains exactly what four-row deck equality supplies: a
bijection of the tail deck.  It supplies no invariance of a consumer which
distinguishes two members of that deck.

## 4. Gluing transports: the holonomy obstruction

Local equivariance does not by itself imply a phase-common global host when
modules share relay ports or propagated histories.  The missing condition
is ordinary groupoid holonomy.

Let `Q` be a graph.  A vertex `x` carries a port fibre `S_x`.  Every oriented
edge `e:x->y` carries a bijection `g_e:S_x->S_y`, with
`g_(reverse e)=g_e^{-1}`.  A global choice of address coordinates is a
family of bijections `psi_x:S_x0->S_x` from one base fibre in each connected
component satisfying

\[
                            \psi_y=g_e\psi_x.          \tag{4.1}
\]

Some vertices may have prescribed boundary coordinates.

### Theorem 4.1 (exact cocycle/coboundary criterion)

A global choice (4.1) exists if and only if:

1. the ordered product of the `g_e` around every closed walk is the
   identity; and
2. for every path between two prescribed boundary vertices, its ordered
   product carries the first prescribed coordinate to the second.

#### Proof

Necessity follows by telescoping (4.1) around a closed walk or along a path
between pins.  For sufficiency, choose a spanning tree in each component,
start at a base vertex, and define `psi` by transport along the unique tree
path.  A nontree edge gives a fundamental cycle, so condition 1 makes its
definition agree with the tree definitions.  Condition 2 gives agreement
with every boundary pin.  \(\square\)

In particular, a relay path is automatically free of internal holonomy.
If one endpoint is fixed and the other is the carried output, its composite
transport may be stored at that one output port.  If both endpoints are
fixed, the composite must equal the prescribed boundary transport.  This
is the exact address/history condition which component-count telescoping
does not see.

For one selected boundary state, the universal identity condition can be
weakened.  Choose a base vertex in each component and transport its selected
state along a spanning tree.  A coherent selected section exists if and only
if that base state is fixed by every fundamental-cycle holonomy and the
transported endpoint states satisfy the declared reset relation.  Thus an
open-path endpoint monodromy may be nontrivial and still be accepted; a
nontrivial closed holonomy may not be ignored.  This is the groupoid form of
the selected-certificate quantifier in Theorem 1.2.

### Theorem 4.2 (partial-map gluing and global address collisions)

Let `theta_i:D_i->E_i` be the partial occurrence maps supplied by local
modules on one frozen physical universe.  They glue to one injective map on
`union_i D_i` if and only if

1. `theta_i=theta_j` on every actual intersection `D_i intersect D_j`; and
2. `theta_i(x)=theta_j(y)` implies `x=y` for every pair of patches.

If each `theta_i` is a bijection onto `E_i`, surjectivity onto `union_i E_i`
is automatic, so the glued map is a bijection.

#### Proof

The two conditions are plainly necessary.  The first makes
`theta(x)=theta_i(x)` well-defined on the union, and the second makes it
injective.  Every point of `union_i E_i` has a preimage in its local patch,
proving the last sentence.  \(\square\)

The intersections here are the **actual global source/address
intersections**, not just declared relay atoms.  With full depth-`d`
overlaps, two nonadjacent component blocks can still meet whenever the
intervening total depth-cell length is below `d`.  Such an extra
intersection can create an image collision or a holonomy cycle even when
the abstract relay graph is a path.  Therefore the clean relay identity
removes abstract atom-level holonomy only; the final source must still pass
Theorem 4.2 and whole-prefix history replay.

### Corollary 4.3 (exact sidecar count for a clean path forest)

Suppose `p` opened one-socket modules are joined by `e` legal one-atom
relays whose module graph is a disjoint union of directed paths.  Then

\[
                         c=p-e                              \tag{4.2}
\]

path components remain, and the exact topology has one live `P2` sidecar
per component.  Thus a sidecar bound `C` requires `e>=p-C`, equivalently a
path cover by at most `C` clean relay chains.  The explicit clean B5 relay
theorem attains equality in (4.2).

#### Proof

An isolated opened module has one `P2`.  Every legal relay identifies the
current output atom of one path with the input atom of a different path and
reduces the number of path components and live `P2`s by one.  A path forest
with `p` vertices and `e` edges has `p-e` components.  Induction using the
two-socket relay identity proves the topology assertion.  \(\square\)

This corollary is restricted to a clean path forest.  It does not assert
that arbitrary branching or cyclic relay overlaps are legal.

## 5. Rooted opening deficiency and the required bank size

Let `P` be a selected family of protected-transport-good closed compressed
sockets (clone-good sockets are the identity-action special case).  For
each target opener `i in P`, let `A_i` be the set of third coordinates `z`
for which the following have all been proved on the same frozen host:

1. the structural rooted `C6` exists;
2. the corrected endpoint aperture holds;
3. its mode change satisfies Theorem 1.1 for the carried relational host;
4. its phase-specific occurrence witnesses and propagated histories exist;
   and
5. its complete footprint is private from every other opener except for the
   declared `z` resource.

### Theorem 5.1 (deficiency form of protected rooted Hall)

Under item 5, the maximum number of sockets which can be opened
simultaneously with distinct third coordinates is

\[
 |P|-\delta,\qquad
 \delta=\max_{I\subseteq P}\bigl(|I|-|\bigcup_{i\in I}A_i|\bigr). \tag{5.1}
\]

If every selected compressed socket is otherwise disjoint, exactly
`delta` compressed cycles remain unopened after a maximum choice.

#### Proof

The simultaneous choice is a matching from `P` to the coordinate shore in
the graph `i~z iff z in A_i`.  The bipartite deficiency theorem gives
(5.1).  Every successful rooted `C6` opens its one compressed cycle into a
forest, while a failed opener leaves exactly that one cycle.  Disjointness
makes these nullities additive.  \(\square\)

Hence `delta=O(1)` is sufficient on the rooted-Hall row of an
additive-constant route, provided the resulting bounded cycles receive a
bounded literal serialization repair; `delta=0` is needed for an exact
all-opened forest.  If item 5 fails, set packing is an exact reformulation
only after each hyperedge contains a private opener-identity token and every
capacity-one/global address, history and cap conflict is represented by a
shared resource.  Otherwise one has a general compatibility/0--1 packing
problem followed by global replay, and (5.1) is only a necessary marginal
test.

Now let the cyclic part of the old host have graphic nullity `Z`.  Suppose
it splits as a forest background, `a` disjoint one-socket old footprints,
`b` disjoint three-socket old footprints, and an uncovered part of nullity
`Z_0`.  Then

\[
                         Z=Z_0+5a+15b.                       \tag{5.2}
\]

After all compressors and a maximum compatible opener family, if `u` of
the `a+b` compressed components remain unopened, the final nullity is

\[
                              Z_{final}=Z_0+u.                \tag{5.3}
\]

In particular, a final bound `Z_final<=C` requires

\[
                  5a+15b\ge Z-C,qquad u\le C,               \tag{5.4}
\]

and therefore at least `max{0,ceil((Z-C)/15)}` bounded-size B5 modules.  Thus an
extensive bank is quantitatively necessary whenever `Z` is unbounded.

Equation (5.3) is a topology/nullity theorem only.  Serialization of the
resulting forest and the terminal compiler remain separate.

## 6. The weakest phase-common host condition for `B+O(1)`

Let `R_car` contain exactly the auxiliary structure read by the next
Pascal transition.  It includes the complete reserve-carry occurrence
interface, its two compatibility graphs and named occupied support, as well
as every carried address, state, reset, aggregate history, residence,
supplier, and upper/source identity actually read next.  It need not contain
a terminal-only compiler matching or a terminal-only upper witness.

### Theorem 6.1 (compiler-relaxed protected bank criterion)

Fix one transition and one incumbent placement.  Suppose a selected B5 bank
has all of the following properties.

1. Partition the bank into isolated modules and certified relay-chain
   composites.  Their **composite** old shores are pairwise disjoint
   submatchings of the incumbent placement.  Every certified phase of one
   composite is a perfect matching on the same complete shores.  Modules
   inside one relay chain may share the declared relay atom; they are not
   incorrectly treated as disjoint.  Distinct composites are shore-disjoint.
2. In one specified serial order, every selected local mode change satisfies
   the selected-certificate Theorem 1.2 for the two successive restrictions
   of `R_car` on the same frozen typed host; the resulting local transports
   satisfy the boundary and holonomy conditions of Theorem 4.1 and the
   actual-address gluing conditions of Theorem 4.2.  If every carry/state is
   required, use Theorem 1.1 instead.  If arbitrary phase vectors are
   required, use the coherent-hypercube condition of Corollary 1.5.
3. After the whole bank toggle and a maximum compatible protected opener
   **set packing**, the actual residual graphic nullity of the bank together
   with its background is at most `C_0`.  When complete module footprints
   form the private direct-sum decomposition of Section 5, this is computed
   by (5.2)--(5.3) and the Hall deficiency (5.1).  Without that privacy,
   neither shore-disjoint assignments nor marginal Hall imply nullity
   additivity, and the actual set packing/graph condition is required.
4. Every private `P2` produced by an opened module either belongs to a
   certified clean relay path or is declared exceptional.  The number of
   relay-path components plus exceptional `P2`s is at most `C_1`, and every
   path satisfies Theorem 4.1 at its fixed boundary pins.  For now the
   explicit certified relay theorem covers one-socket modules; any use of a
   three-socket output here needs its own literal relay certificate.
5. In the separately chosen terminal plus phase, all genuinely new literal
   task identities are deduplicated and distinct on the left shore, and have
   distinct certified cells outside the complete packet damage set.  The
   union of those cells with that damage set meets at most `C_2` cells of one
   reference compiler matching.

Then the bank itself consumes zero movable-frontier Hall slack, preserves
the selected carried certificate and realized carry, leaves at most `C_0`
cyclic defects and `C_1` relay sidecars, and incurs only bounded terminal
compiler eviction.  In the universal version it preserves the complete
reserve-carry interface.  In particular, a phase-common terminal compiler
column is not a necessary part of the host-side hypothesis.

#### Proof

Delete each complete chain shore once from the incumbent matching.  Item 1
then gives the same residual matching, and reattaching any certified chain
phase covers the same shore; this is the chain-level incumbent-aligned
zero-slack argument.  Item 2 transports the selected carry completion and
every selected relation of `R_car` (or, in the universal version, conjugates
the two contracted matroids and all boundary relations).  Item 3 directly
bounds the actual remaining cyclic nullity; equations (5.2)--(5.3) justify
its advertised calculation only on the private direct-sum face.  Theorem
4.1 and Corollary 4.3 give at most `C_1` boundary-compatible live `P2`
topology ports.  They become carried tokens or source-position costs only
through the explicit realization and charge in Theorem 6.2.  Finally, bounded compiler
eviction deletes only the old matching edges in the complete damage set and
the certified new task cells.  Terminal-phase decoupling prevents this
terminal choice from becoming carried debt.  \(\square\)

The theorem isolates only the host-side implication.  An unconditional
`B(k)+O(1)` result additionally requires a literal chronology and a uniform
construction satisfying items 1--5; those existence statements are all
**UNPROVED**.

### Theorem 6.2 (conditional regenerative bound from selected transport)

Put `B(k)=W+d`.  Assume, from some base dimension onward, one compatible
infinite odd spine

\[
                 (S_i,Z_i,\phi_i)_{i\ge0},qquad
       \phi_i:(S_i,Z_i)\longrightarrow(S_{i+1},Z_{i+1}),       \tag{6.1}
\]

of selected certificates, with the required even terminal children.  Thus
each displayed output is literally the next input, not an independently
chosen bounded state.  For a finite target family `H`, let `R(H)` be the
minimum length of a repair word whose interval unions cover `H`, with
`R(emptyset)=0`; literal listing gives `R(H)<=|H|`.  At each transition
assume all of the following **existence clauses**, none of which is proved
here.

1. After the selected B5 bank and every bounded residual topology repair
   have been serialized, there is one globally replayed literal source `A`.
   Define its actual source-position charge by

   \[
                         \chi=|A|-(W+d).                       \tag{6.2}
   \]

   All uncontracted serialization insertions are included in this number,
   and `chi<=a`.  The source satisfies the phase-specific endpoint
   aperture, actual global address injectivity, and whole-prefix history,
   residence, cap and upper/source replay.  For the one-credit case, exactly
   one nonowner pivot/reset cell occurs and every connector has full literal
   depth-`d` overlap, so `a=chi=1`.
2. The pivot insertion has nonempty letter `X` with
   `X subseteq A_(-1) union A_1`; the final depth-band chronology is flat of
   owner rank; the singleton and the two literal rays satisfy all distinct
   task/ray, release and cap hypotheses of the flat monotone-pivot theorem.
   Hence every old arbitrary-width witness survives and the strict-lower
   reference compiler has zero matched damage from the pivot.  More
   explicitly, the singleton `X` is a strict-lower target outside the old
   bank, while the distinct logical ray targets form the old target set `R`
   whose reference edges are released and reassigned to the new ray cells.
   Any repeated displayed ray value is deduplicated before this statement
   and is treated as a protected duplicate witness, not as a second matching
   vertex.
3. The B5 bank satisfies Theorem 6.1 on the same frozen host.  Its carried
   assignment-interface defect is zero in the sense of (1.10).  A declared
   token set `Z_i` has size at most a fixed `s`, and the selected transport
   maps its entire dependency closure bijectively to that of the next
   `Z_(i+1)`; `Z_i` is transported state, not permission to leave an invalid
   matching port.  Every actual overlap passes Theorem 4.2, every closed
   holonomy fixes the selected state, and every open-path endpoint monodromy
   is accepted by the next reset relation.
4. Every auxiliary aligned birail sequence uses one literal base/profile
   system.  Its signed lower action therefore telescopes to its endpoint
   rails, which are included in the selected boundary state.  In the terminal
   accepted state the canonical simple-positive ray shores have the two
   literal cross matchings.  Their union is one capacity-one cell bank in a
   common terminal cap state: all its cells are mutually distinct and are
   disjoint from the transported background compiler.  Thus zero-block
   collapse makes `H_ray` empty.  Signed telescoping alone is not used as an
   occurrence matching.
5. In the terminal plus state, `D` is a complete compiler damage set and the
   genuinely new hard tasks use distinct cells `b_i` outside `D`.  Put

   \[
   H_{comp}=\{T:\text{the reference cell of }T
                         \text{ lies in }D\cup\{b_i\}\},       \tag{6.3}
   \]

   and let `H_up,H_ray,H_ap` be the residual upper, ray and aperture target
   holes.  For

   \[
                    H=H_{up}\cup H_{comp}\cup H_{ray}\cup H_{ap},        \tag{6.4}
   \]

   the literal repair complexity satisfies `R(H)<=c`.  The auxiliary child
   independently closes every exported row involving `H`, so this terminal
   omission is not carried.
6. The transported selected state, including `Z_(i+1)`, belongs to the same
   declared successor class; reversal acts on the whole certificate, not on
   one local module in isolation.

Then the carried token count stays at most `s`, and every terminal dimension
satisfies

\[
                         \boxed{\nu(k)\le B(k)+a+c}.           \tag{6.5}
\]

In particular, `a=1`, `c=0`, `s=1`, with `Z_i` consisting of the one charged
relay output identified with the outgoing pivot/reset/aperture token (all
other carried fields being metadata in its dependency closure), and no other
terminal hole give the honest conditional conclusion

\[
                              \nu(k)\le B(k)+1.                \tag{6.6}
\]

Uniform fixed `a,c,s` give a conditional `B(k)+O(1)` bound.

#### Proof

Clause 1 gives a literal source of length at most `B+a`; in the one-credit
case this is exactly the single-credit conservation law.  Clause 2 preserves
all old interval witnesses and gives the exact singleton/two-ray lower
compiler with no old-target loss.  The chain-level incumbent alignment in
Theorem 6.1 consumes no movable-frontier Hall reserve, while Theorems
1.2, 4.1 and 4.2 transport every selected carried witness and every used
capacity-one address.  Composing the selected maps sends the whole dependency
closure of `Z_i` to that of `Z_(i+1)`, so the number of charged logical tokens
does not grow.  This says nothing about the size of their structured
metadata.

Aligned birail telescoping leaves only endpoint target-value current, and
clause 4 supplies the physical cross matchings which remove the ray
occurrence deficiency.  Bounded eviction in clause 5 leaves casualties only
in `H_comp`; the other omissions are exactly the other three displayed
families.  Append a shortest repair word for `H`.  This costs at most `c`
and destroys no existing witness.  Phase decoupling and clause 6 keep that
terminal repair out of the next auxiliary state.  Iteration along the one
compatible spine proves (6.5).  \(\square\)

The constants `C_0,C_1` in Theorem 6.1 are not automatically word-length
costs.  Clause 1 must actually serialize their bounded residual topology and
measure its contribution in `chi`.  Likewise a positive `delta_if` is only
an unmatched-port count until a literal repair theorem prices it.

### Scope of the other exact ingredients

* The sharp monotone pivot preserves every old interval value and, on its
  flat rank-`m` face with the exact released ray targets, transports the old
  compiler with zero matched damage.
  It discharges only the pivot-induced contribution to item 5 once a
  pivot-rich physical host and the exact two ray tickets are present.
  B5/host/cap changes may still contribute to the complete terminal damage
  set; both their bound and the all-`k` pivot-rich host are **UNPROVED**.
* Aligned birail telescoping cancels literal target multisets at every depth.
  It proves aggregate-history equivariance only for histories already proved
  to factor through that literal signed multiset.  It does not preserve an
  addressed occurrence relation by itself.
* Zero-block collapse converts its terminal threshold obstruction into two
  ordinary cross-Hall systems.  Physical cross-graph existence is still a
  separate host condition.
* The corrected pull clock proves fractional stationary trace membership.
  It does not give the integral phase-common host or any automorphism in
  Theorem 1.1.
* Bounded eviction and phase decoupling justify removing terminal-only
  compiler data from `R_car`; they do not remove any compiler/history datum
  which is actually read by the next transition.

## 7. Exact K17 specialization

For the planted 22-atom compressed-normal K17 module, root gauge fixes the
eight physical head/upper suffix slots and transports all eight lower and
tail resources.  The `C10` part has the 5-cycles (3.2)--(3.4), and the
rooted opener contributes the corresponding 3-cycles.  Therefore:

1. if literal lower/tail identity is a carried injective exterior decoder,
   Proposition 2.3 rejects the module;
2. if the displayed two-phase owner-increment pair is retained as a
   pointwise-fixed slot column, the nonconstant five-slot and three-slot
   lists reject token gauge by the necessary unary-colour half of Theorem
   2.1;
3. even if arbitrary bijective renaming of that pair alphabet is allowed,
   the rooted `C6` token gauge still fails Theorem 2.2.  Its values are

   \[
                    A=(14,14),\quad B=(4,4),\quad A=(14,14),       \tag{7.1}
   \]

   while the slot transport is a 3-cycle.  The two `A` slots have images of
   different signatures, so (2.3) fails;
4. the five `C10` values are all distinct, so an arbitrary five-symbol
   renaming passes the fibre test.  But exactly two pairs are diagonal and
   three are off-diagonal.  A common coordinate permutation in both phases,
   even followed by phase reversal, preserves the diagonal predicate.  A
   5-cycle preserves no nonempty proper two-slot subset, so this natural
   coordinate/reversal token gauge is impossible;
5. none of these statements rejects a mixed or physical-root transport which is a
   genuine automorphism of the full carried occurrence/history structure.

The gauge qualification is essential.  Physical-root transport fixes the
slot owner/root data but rebinds the internal lower/tail occurrence IDs;
bottom-following transport fixes lower tokens and moves suffix slots.  The
two descriptions are conjugate through the old and new matchings, but a
proof may not take fixed head/upper fields from the first gauge and slot
columns from the second without transporting every cross relation.

The coefficient-one equality of each of the four typed module decks gives a
unique value-preserving bijection on that typed deck.  It proves that no
lower, upper, tail or head target value is lost.  The four bijections need
not map the four entries of one old atom to the entries of one new atom--the
topology is deliberately changed--and they do not prove that any exterior
relation is natural.

Accordingly the raw assignment-only fixed-bottom/fixed-slot interface has
`delta_if=8` (a protected fixed-shore interface has value at least 8), while
the physical-root candidate has eight lower and eight
tail typed occurrence rebindings as its seed dependency boundary.  The
5,244 direct protected rows are footprint-disjoint from that seed, but the
propagated dependency closure may be much larger.  A single module has no
relay-cycle holonomy; its endpoint/reset acceptance and actual-address
gluing are still nontrivial.

The rooted structural target has the singleton untyped menu `{6}`.  Hence
define `A^sel_(16,2)` to contain `6` exactly when there are phase-specific
witnesses on that same structural coordinate, both satisfying the corrected
endpoint aperture, together with one selected-certificate transport carrying
all used boundary tuples and capacity-one cells.  Its one-spine rooted
deficiency is exactly

\[
 \delta_{K17}=
 \begin{cases}
 0,&6\in A^{sel}_{16,2},\\
 1,&6\notin A^{sel}_{16,2}.
 \end{cases}                                               \tag{7.2}
\]

For a universal host replace `A^sel` by the stronger `A^cap`, which uses
Theorem 1.1 rather than Theorem 1.2.  Complete opener-footprint privacy makes
several such selected menus an ordinary Hall problem; without it the exact
problem is literal resource set packing only under the complete conflict
encoding stated after Theorem 5.1, and otherwise remains general
compatibility packing plus global replay.  The static common-basis
theorem proves neither branch of (7.2).

The fact that all four module resource decks avoid the 5,244 frozen private
rows removes those rows from the immediate resource-conflict shore.  It does
not prove an automorphism on the other changed ambient rows or on propagated
histories.  The exact weakest one-module remaining test is therefore:

> transport one selected complete K17 certificate through the displayed
> `C10+C6`, satisfying (1.6), actual global address injectivity and
> whole-prefix history replay in the physical-root/internal-low-tail gauge,
> and prove `6 in A^sel_(16,2)`.

The context-independent replacement is the full exterior-fixed isomorphism
of Theorem 1.1 together with `6 in A^cap_(16,2)`.

The exact global remaining test is to do this for a weighted disjoint bank
covering all but bounded cyclic nullity, with bounded rooted deficiency and
bounded holonomy-compatible relay path-cover number.  No such extensive K17
or all-`k` bank is proved here.

## 8. Independent audit and exact open clauses

The decisive reduction was rechecked with the following quantifier and cost
guards.

1. Equation (1.3), not a product of two separately chosen shore actions, is
   the general condition.  The double-coset form (1.5) is used only after
   factorization of the complete carried automorphism group is proved.
2. The selected-certificate theorem transports one complete witness.  It
   does not imply equality of unused compatibility graphs; conversely the
   rank identities (1.7) preserve universal carry cuts but do not by
   themselves give an occurrencewise isomorphism.
3. `delta_if` counts unmatched assignment ports, not source letters.  A
   positive value cannot be inserted into (6.5) without a separate literal
   repair theorem.
4. A clean relay path has no abstract cycle holonomy, but its endpoint
   monodromy must be accepted.  Short globally overlapped source blocks can
   create additional nonadjacent intersections, so Theorem 4.2 and final
   whole-prefix replay remain mandatory.
5. The topology bounds `C_0,C_1` are not length charges.  Only the actual
   post-serialization value `chi` in (6.2) enters (6.5).
6. The monotone pivot is compiler-lossless only on its flat rank-`m`, exact
   released-ray face.  Birail signed telescoping is not occurrence Hall, and
   the pull clock is only fractional.  Bounded eviction removes a
   terminal-only compiler from the common interface only when its complete
   damage is bounded and no damaged row is exported.
7. The K17 `C6` and `C10` owner-pair arguments exclude the stated token
   gauges only.  They do not exclude the physical-root/internal-low-tail
   gauge, whose full dependency closure is unknown.

Accordingly every remaining existence assertion is one of the following
explicitly **UNPROVED** clauses.

* **OPEN-A:** on the planted K17 host, one selected physical-root transport
  satisfying (1.6), actual-address/history replay, endpoint aperture and
  `6 in A^sel_(16,2)`.
* **OPEN-B:** an extensive all-`k` incumbent-aligned B5 bank on one frozen
  common-basis/carry host, with actual residual nullity, rooted set-packing
  deficiency and relay path-cover number all bounded.
* **OPEN-C:** a globally placed protected pivot/reset chronology which
  serializes that bank with uniformly bounded `chi`--with `chi=1` for the
  `B+1` route--and passes every nonadjacent overlap/address/history guard.
* **OPEN-D:** the physical birail cross-matchings, bounded complete terminal
  damage, upper/aperture closure, and a successor which independently closes
  every terminal repair row.
* **OPEN-E:** one compatible infinite sequence (6.1), including the required
  even terminal children.

Until OPEN-A--OPEN-E are supplied in the required all-dimensional form,
Theorem 6.2 is conditional and no new upper bound for `nu(k)` is claimed.
