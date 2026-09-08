# Odd two-bank regeneration: exact path, Hall, and connectivity gates

Date: 2026-07-31  
Status: dimension-uniform conditional theorem; solver-free `K17` obstruction
for the repaired whole-component face; independently replayed three-path
fallback; no `K17` word or all-dimension construction is claimed

## 0. Verdict

The six occurrence swaps are a genuine and useful repair, but they do not
finish the whole-component two-bank construction.

* Rebuilding the macro forest after the six swaps gives `1430` macro edges,
  `5005` components, and a marked closure of `106` components, `154` macros,
  and `3815` owner tokens.  Every marked component has zero strict internal
  `D2<3` and `D3<4` run debt.
* The next gate already fails without SAT.  The exact catalogue of
  one-pure-`U` joins between oriented marked components has `412` geometric
  arcs, `312` residence-clean arcs, and `140` distinct `U` labels.  Its weak
  component sizes are `99,2,2,2,1`, so any spanning marked path needs at
  least four adjacency units outside that catalogue.  The singleton is the
  component containing macro `18`; it has no clean incident arc in either
  orientation.
* An independent tail/head projection has matching number `103` and Hall
  deficiency three, providing a second exact obstruction.  The
  unconditioned port flow is saturated (`10010/10010`), but that is only a
  marginal statement before a marked path has consumed its labels and port
  capacities.
* The singleton obstruction has a sharp local repair: the complete
  one-unmarked-component census contains `110` residence- and capacity-safe
  Steiner packets.  This proves that one internal complement component is
  necessary and sufficient locally.  It does not connect the other weak
  components or prove a global marked path.
* The clean-atom construction remains the sharp fallback.  Its augmented
  `4740`-arc catalogue has six forced endpoint nodes, so every cover has at
  least three paths.  The saved cover attains three, with mandatory-atom
  lengths `19,2,85`, literal lengths `898,78,4834`, `192` distinct pure-`U`
  owners, and `89` distinct optional atoms.  Its `5810`-token concatenation
  is `D2/D3` clean.  The two new adjacencies have symmetric-difference ranks
  `6` and `10`, so neither is a Johnson/one-`U` join: they are exactly two
  **non-port boundary obligations**, not two already constructed sockets.

The dimension-uniform lesson is that internal cleanliness, residual Hall,
and connected pair completion are three separate hypotheses.  The smallest
noncircular regenerative state carries a bounded-path clean-atom cover,
literal currents for every non-port boundary obligation, and the residual
pair-column connectivity instance.  Scalar residence debt or unconditioned
flow is not enough.

## 1. Pascal port ledger

Fix `r>=2`, let `|Omega|=2r-1`, and put

\[
 \mathcal T_r={\Omega\choose r},\qquad
 \mathcal U_r={\Omega\choose r+1},
\]

\[
 M_r=|\mathcal T_r|,\qquad N_r=|\mathcal U_r|,\qquad
 B_r=M_r-N_r=\operatorname{Cat}_r.                 \tag{1.1}
\]

A **Pascal-exact macro datum** consists of a loopless linear forest
`P` on \(\mathcal T_r\) with `B_r` macro edges, together with a literal
child-owner path expanding each macro edge.  The macro interiors partition
the three tagged owner sectors and their non-port lower incidences exactly;
the remaining pure-owner sector is \(\mathcal U_r\).

Since `P` is a forest,

\[
             |\pi_0(P)|=M_r-B_r=N_r.                \tag{1.2}
\]

A pure owner \(U\in\mathcal U_r\) can connect two distinct exposed ports
`T,T'` precisely when both are facets of `U`.  Equivalently,

\[
          U=T\cup T',\qquad |T\triangle T'|=2.       \tag{1.3}
\]

The literal owner word on the left component, the singleton owner `U`, and
the literal owner word on the right component must additionally pass every
declared boundary residence test.  Condition (1.3) alone is only geometric.

An occurrence swap inside one fixed lower fibre preserves one selected
occurrence in that fibre, the count `B_r` of macro edges, and all four owner
sector cardinalities.  If the rebuilt quotient remains loopless and
acyclic, (1.2) is preserved.  The swap need not preserve component closure,
port degrees, connector neighbourhoods, or residence.  Thus occurrence
swaps are **cardinality-neutral, not structure-neutral**.

## 2. Exact marked-path contraction

Let `C_1,...,C_s` be marked components of `P`.  Assume each oriented
component word is internally safe through the required derivative depth.
Make a labelled directed connector graph whose arc

\[
                   (C_i^\epsilon,U,C_j^\delta)       \tag{2.1}
\]

is present exactly when:

1. the exposed ports satisfy (1.3);
2. the concatenation `W(C_i^epsilon),U,W(C_j^delta)` passes the literal
   residence transducer; and
3. its two lower incidences respect their available capacities.

### Theorem 2.1 (count-neutral marked contraction)

Suppose (2.1) contains a directed Hamilton path through the `s` marked
components using `s-1` pairwise-distinct pure-owner labels.  Adding those
connectors to `P` gives a forest `H` in which the marked bank is one path,
and

\[
 |E(H)|=B_r+s-1,\qquad
 |\pi_0(H)|=N_r-s+1.                                 \tag{2.2}
\]

Exactly `N_r-s+1` pure owners remain.  With

\[
                       d_H(T)=2-\deg_H(T),            \tag{2.3}
\]

the residual current is automatically balanced:

\[
 \sum_{T\in\mathcal T_r}d_H(T)
 =2M_r-2(B_r+s-1)=2(N_r-s+1).                         \tag{2.4}
\]

#### Proof

Every selected connector joins two different components along a path on
the marked component set.  It therefore reduces the component count by one
and creates no cycle.  This proves (2.2).  Each connector consumes exactly
one pure owner.  The degree sum in a forest is twice its edge count, so
(2.3) gives (2.4).  \(\square\)

Equation (2.4) is not a Hall theorem.  It is only the total-current row.
Nor does internal cleanliness imply the hypothesis of Theorem 2.1: the
`K17` component `77` below is the smallest possible counterexample.

### Corollary 2.2 (Steiner-packet neutrality)

Suppose instead that the marked path contains all `s` marked components and
exactly `h` pairwise-distinct unmarked macro components as internal Steiner
objects.  Then it uses `s+h-1` distinct pure owners and leaves

\[
 |\pi_0(H)|=N_r-s-h+1,qquad
 |\mathcal U_r\setminus U(H)|=N_r-s-h+1,              \tag{2.5}
\]

\[
             \sum_Td_H(T)=2(N_r-s-h+1).               \tag{2.6}
\]

The proof is identical to Theorem 2.1: the selected component graph is a
tree path on `s+h` vertices.  Thus an optional complement component costs
no scalar owner/halfport slack.  It changes the correlated port, label,
Hall, and topology instance and must be retained in the exported state.

### Theorem 2.3 (three solver-free actuator lower bounds)

Let `G` be the undirected projection of the standard clean connector
catalogue on `n` marked components.  Let `c(G)` be its number of weak
components, let `l(G)` be the number of vertices of degree at most one, and
let `B_G` be the tail/head bipartite projection of the directed catalogue.
If a spanning marked path uses `q` adjacencies outside the standard
catalogue, then

\[
 q\ge
 \max\left\{
 c(G)-1,
 \left\lceil{l(G)-2\over2}\right\rceil,
 n-1-\nu(B_G)
 \right\}.                                             \tag{2.7}
\]

#### Proof

Every outside adjacency can merge at most two weak components, proving the
first bound.  A Hamilton path has only two endpoints.  Every other vertex
of catalogue degree at most one needs at least one incident outside
adjacency; one such adjacency can service at most two of these vertices,
which proves the second bound.  Finally the `n-1` directed path adjacencies
have pairwise-distinct tails and heads.  At most `nu(B_G)` of them can come
from the standard catalogue, proving the third bound.  \(\square\)

These are lower bounds on **marked adjacency units**.  One compound physical
actuator may export several units, but its full signed current and literal
support must then be charged once as a compound column.

## 3. Exact residual Hall theorem

After a marked path and any fixed socket currents have been installed, let
`b_U in {0,1,2}` be the unused incidence supply of a remaining pure owner
`U`, let `A_U` be its allowed residual facets, and let `d(T)` be the exact
remaining demand of port `T`.  Assume total balance

\[
                         \sum_T d(T)=\sum_U b_U.       \tag{3.1}
\]

### Theorem 3.1 (capacitated facet Hall)

There is an integral residual incidence assignment if and only if, for
every \(Q\subseteq\mathcal T_r\),

\[
 \boxed{
   \sum_{T\in Q}d(T)
   \le
   \sum_U \min\bigl(b_U,|A_U\cap Q|\bigr).
 }                                                       \tag{3.2}
\]

#### Proof

Use the network

\[
              s\longrightarrow U\longrightarrow T\longrightarrow t
\]

with capacities `b_U`, `1`, and `d(T)`.  A cut separating a port set `Q`
from the sink can receive from owner `U` at most the smaller of `b_U` and
\(|A_U\cap Q|\).  Thus (3.2), together with (3.1), is exactly the
max-flow/min-cut criterion for saturating all port demands.  Integral
capacities give an integral assignment.  \(\square\)

For the ordinary post-path instance `b_U=2` for every unused owner.
Every socket current must be subtracted before applying (3.2).  Testing the
unconditioned forest instead is not a valid proxy for the conditional flow.

## 4. Degree flow does not give one complementary path

An integral flow chooses two facets for every unused pure owner but may
close several disjoint cycles.  The exact connected formulation keeps the
pairing.

For each owner `U`, let \(\mathcal A_U\) be the allowed final two-facet
columns after its fixed incidences, residence guards, provider guards, and
socket currents have been applied.  Use a Boolean `z_(U,a)` for
\(a\in\mathcal A_U\).  Require

\[
 \sum_{a\in\mathcal A_U}z_{U,a}=1                         \tag{4.1}
\]

for every owner, and

\[
 \deg_H(T)+
 \sum_{U,a:\,T\in e(U,a)}z_{U,a}=2                       \tag{4.2}
\]

for every port.  If `Q` is a nonempty proper union of components of `H`,
require

\[
 \boxed{
 \sum_{U,a:\,|e(U,a)\cap Q|=1}z_{U,a}\ge2.
 }                                                        \tag{4.3}
\]

### Theorem 4.1 (pair columns plus cuts are exact)

Equations (4.1)--(4.3) are feasible if and only if the fixed partial forest
extends, using the declared pair columns, to one connected degree-two
quotient.

#### Proof

Equations (4.1)--(4.2) use every owner once and fill every port to degree
two.  Therefore every final quotient component is a cycle and every cut has
even cardinality.  Condition (4.3) excludes every proper union of such
components, hence forces one connected cycle.  Conversely a connected
completion selects one column per owner, satisfies every degree row, and
crosses every proper component union at least twice.  \(\square\)

If the marked bank from Theorem 2.1 is one path, its internal ports are
saturated.  A connected completion can meet it only at its two ends, so it
is one cyclic interval and the complementary objects form the other
interval.  Opening one crossing gives the desired two-bank linear order.

The matrix in (4.1)--(4.3) is not asserted totally unimodular.  The Hall
network of Section 3 is an exact projection, while component connectivity
and pair-dependent guards remain integral correlation rows.

Before filtering, the natural pair atlas has at most

\[
              N_r {r+1\choose2}                       \tag{4.4}
\]

columns.  Connectivity cuts are exponentially many but have an exact
min-cut/lazy separator.  Literal residence at a join is decided by prefix
and suffix collars of the required depth, an `O(kd)` boundary signature.

## 5. Bounded-path fallback and non-port obligations

The marked objects need not first form one physical port path.  Suppose a
resource-disjoint clean-atom selection gives `p` literal Johnson paths.
Choose an order and orientation of those paths and concatenate their owner
traces.  There are exactly `p-1` new internal adjacencies.  If `q` of them
are already legal unused-resource port connectors, then

\[
                 p-1-q                                \tag{5.1}
\]

are non-port boundary obligations.  The two outer ends are the ordinary
marked/complementary interfaces and are not counted.  A cyclic marked-only
order would require one additional join.

Formula (5.1) counts obligations, not gadgets or added cells.  One compound
complementary rethread may discharge several obligations, and a single
obligation may require growing support.  To feed Theorem 3.1, a **port-lift
certificate** must realize those adjacencies physically, restore every
opened owner/lower incidence, leave all degrees at most two, and export the
exact residual currents.  Trace cleanliness alone is not such a
certificate.

For exact coefficient one, the port lift and socket columns must be
slot-preserving: an `O(1)` number of sockets with positive literal cost gives
only an `O(1)` additive theorem.  For a uniform exact induction the useful
target is therefore `p_r=O(1)` together with zero-cost substitutions and a
terminal common-cap certificate.

### 5.1 Actuator-column state

A proof-safe component actuator column must store, rather than merely score,

\[
 \bigl(
 \text{marked ends and orientations},
 \text{internal component set},
 \text{pure-owner labels},
 \Delta d(T),
 \text{literal row segment},
 \text{protected-witness delta},
 \text{compiler collar}
 \bigr).                                               \tag{5.2}
\]

Selected columns are required to be component- and owner-disjoint, to obey
the exact port capacities after their signed currents are summed, and to
satisfy the marked path degrees and subtour rows.  The weak-component and
leaf bounds of Theorem 2.3 are valid eager cuts on these columns.  Only after
the selected current is fixed may Theorems 3.1 and 4.1 be invoked.

### 5.2 Exact common-cap preservation

Let the assembled depth-two row be `Z`.  For a slot-preserving actuator
(so row indices outside its support do not shift), define the maximal envelope

\[
 E_p=\bigcap_{i:\,i\le p\le i+2}Z_i.                 \tag{5.3}
\]

If an actuator changes `Z` only on a row-index set `I`, then it can change
`E_p` only for

\[
                       p\in I+\{0,1,2\},             \tag{5.4}
\]

and the reconstructed equations

\[
                       E_j\cup E_{j+1}\cup E_{j+2}=Z_j \tag{5.5}
\]

only for `j in I+{-2,-1,0,1,2}`.  Thus nonemptiness and exact `D2`
inversion have a finite five-row actuator collar.  Outside that collar the
baseline replay is unchanged.

After fixed singleton/pair prepins, intersect them into `E` to obtain
`B_p`.  For a residual target--cell selection `M`, put

\[
 Q_p(M)=B_p\cap
 \bigcap_{(S,J)\in M:\,p\in J}S.                    \tag{5.6}
\]

In the `K17` residual compiler, where eligible lower cells are singletons
and adjacent pairs, the selection is one-common-cap exact if and only if every `Q_p` is
nonempty and it replays every `D2` row, fixed prepin, and selected target.
Since only the singleton and its two adjacent pairs meet an interior
position, the inclusion-minimal conflict clutter has rank at most three.

Consequently actuator choice and compiler matching may be separated only
on a **guarded common-cap face**: every allowed actuator must preserve the
same permanent position bits and declared row/target hosts outside its exact
five-row collar, while its collar rows are replayed literally.  Otherwise
the actuator variables and the rank-three compiler conflicts must be solved
jointly.  Scalar slack, envelope nonemptiness, or marginal Hall alone is not
common-cap preservation.

## 6. The repaired `K17` whole-component face is closed

The independently replayed occurrence swaps are

```text
 9486: (0,4064) -> (0,5826)
16502: (0,1781) -> (0,6254)
 1675: (0,1997) -> (0,5349)
 2829: (0,2849) -> (0,6201)
22632: (0,1571) -> (0,4923)
26800: (0,2423) -> (0,5775)
```

They rebuild the full Pascal datum, not merely the marked closure:

```text
macro edges / forest components       1430 / 5005
marked components / closure macros     106 / 154
required / optional closure macros      108 / 46
marked owner tokens                         3815
strict internal D2 / D3 debt              0 / 0
```

The exact oriented endpoint catalogue has `412` geometric and `312`
residence-clean arcs.  Its undirected projection has five weak components
of sizes

\[
                         99,2,2,2,1.                  \tag{6.1}
\]

The singleton is the single-macro component with macro ID `18`, endpoints
`16638,22835`, and `111` owner tokens.  One reconstructed ordering calls it
component `77`, another calls it local component `48`; macro `18` and its
ports are the invariant identifiers.  Its six geometric incident arcs
create a strict short run and the corresponding derivative short run;
hence both orientations have zero clean indegree and zero clean outdegree.

### Corollary 6.1 (solver-free primary-face no-go)

There is no whole-component, clean one-pure-`U`-per-join Hamilton path
through the `106` repaired marked components.  Moreover, every spanning
marked path needs at least four adjacency units outside the clean one-`U`
catalogue.

#### Proof

A Hamilton path on more than one vertex gives every vertex at least one
incident selected arc, while the macro-`18` singleton has none in the
exact legal catalogue.  More generally, a path meeting all five weak
components in (6.1) needs at least four edges between them, and none of
those edges belongs to the clean catalogue.  \(\square\)

There is also an orientation-relaxed tail/head Hall witness.  The projected
bipartite matching number is `103`, with

\[
 S=\{48,54,74,76,79,92,97\},\qquad
 N(S)=\{16,32,53,85\}.                                \tag{6.2}
\]

Thus the projection already has deficiency three.  The weak-component
floor four is stronger for the number of exceptional adjacency units.

The unconditioned residual network saturates all `10010` incidences of the
`5005` pure owners.  This does not weaken Corollary 6.1: no conditional
residual instance exists until the marked path has been chosen.  A heavy
Hamilton or residual-pair solve on this exact face is therefore unnecessary.

The local singleton repair is also exact.  A complete radius-one census
finds `110` clean, capacity-feasible paths which route macro `18` through
one unmarked component and then to another marked component.  A canonical
one uses the isolated port component `16623` and pure owners `16639,18671`.
Direct repair is impossible, so one internal complement component is the
minimum local Steiner depth.  This packet does not by itself bridge all
five weak components.

The weakest live relaxations are now explicit:

1. choose a different occurrence combination which preserves zero internal
   debt and gives every marked component a legal connector neighbourhood;
2. select a resource-disjoint family of at least four compensated adjacency
   units, using Steiner packets or facet/socket rethreads, and then solve the
   conditioned path instance; or
3. use the older bounded-path atom cover and export its non-port boundary
   currents.

### 6.1 Exact radius-one occurrence no-go

The complete radius-one occurrence catalogue around the six-swap state has

```text
all neighbours                                      1430
residence-clean states                              1411
states with no isolated marked component             122
connected clean connector graphs                       0
states passing the Hamilton-path degree necessity       0
minimum number of forced leaves                        21.
```

The best weak-component shapes are `102+2+2` and `103+2+2`.  Thus every
one of the `122` no-isolate states is solver-free path-infeasible.  By
Theorem 2.3, the common leaf floor alone gives

\[
             q\ge\left\lceil{21-2\over2}\right\rceil=10       \tag{6.3}
\]

outside-catalogue marked adjacency units for any spanning path.

The high-arc move

```text
z=21006: (0,1121) -> (0,4318)
```

has `153` closure macros, `3800` owner tokens, `322` clean directed arcs,
shape `102+2+2`, and `22` forced leaves.  It illustrates why arc count and
absence of isolated vertices are poor scores: its actuator floor is still
ten.  No path CNF is needed for it or for the other `121` states.

The exact next occurrence search is radius two from only the `12`
three-component frontier states.  This note does not duplicate that census.
The appropriate forward score is the full vector

\[
 \bigl(c(G)-1,\ \lceil(l(G)-2)/2\rceil,\
       n-1-\nu(B_G),\ \text{owner-token count},\
       \text{common-cap collar state}\bigr),          \tag{6.4}
\]

not clean-arc count or isolated-component count alone.

## 7. Independently replayed three-path fallback

The current clean-atom witness is reconstructed from the parent, flow, and
forced-pattern artifacts without importing its constructor.  The audit
finds:

```text
clean / mandatory atoms                         1144 / 106
candidate arcs: direct / one-opt / two-opt   328 / 2706 / 1706
forced endpoint nodes                 76,84,92,94,100,102
minimum and attained path count                           3
mandatory nodes per path                           19,2,85
literal path lengths                           898,78,4834
selected distinct optional atoms / U owners          89 / 192
joined distinct owner tokens                            5810
joined strict D2 / D3 debt                            0 / 0
non-port join xor ranks                              6,10
```

The same six nodes remain forced endpoints in the complete augmented
`4740`-arc catalogue, so the lower bound `p>=3` is valid in exactly the
catalogue used by the witness.  All `384` selected connector halfports use
distinct rank-eight colours and stay within the frozen forest's residual
capacities.  After these connectors, the pre-socket ledger has `4813`
unused pure owners and `9626` residual halfport units.

The two arbitrary joins are not physical port edges.  In particular, the
six path endpoint ports are already saturated in the frozen ledger.  Thus
the certificate proves a minimum three-path residence trace and two
boundary obligations, while complementary socket realization, palette
restitution, conditioned Hall, connected pair completion, upper/deeper
service, and the common cap remain open.

The delegated payload prefix `7656329c` was overwritten while the
certificate was being strengthened.  The independent audit records that
lineage and verifies the current witness payload and file hashes listed in
Section 9.

## 8. Minimal dimension-uniform regenerative invariant

A uniform odd-step theorem must export the following correlated state.

1. A Pascal-exact occurrence choice and macro forest satisfying (1.1)--(1.2).
2. A clean marked atomization with literal boundary collars through the
   required derivative depth.
3. A resource-disjoint direct/Steiner packet path cover with controlled
   `p_r`; bounded live debt requires `p_r=O(1)`.
4. A physical port-lift relation for its `p_r-1-q_r` non-port obligations,
   including exact owner and lower-incidence currents.
5. Every residual Hall inequality (3.2) after those currents are subtracted.
6. One safe integral pair completion satisfying (4.1)--(4.3).
7. The two cyclic marked/complementary boundary residence tests.
8. One terminal relation carrying arbitrary-width upper/deeper service,
   baseline-exact envelopes, literal lower hosts, and a common cap.

Items 1--2 hold for the six-swap `K17` face, but item 3 fails in the clean
whole-component one-`U` class.  The one-Steiner census repairs the singleton
locally, while the weak-component theorem still forces at least four
outside-catalogue adjacency units globally.  The older atom certificate
proves a different item-3 face with `p=3`, but item 4 remains open.  Neither
route reaches items 5--8.

This invariant is noncircular: every field is either a literal finite
relation exported by the parent or an exact integral feasibility condition
at the child.  It is also minimal at the current boundary.  Removing the
path field admits component `77`; removing socket currents makes Hall
unsound; removing pair columns admits disconnected degree flows; and
removing the terminal relation confuses a central carrier with a universal
word.

## 9. Frozen provenance

Primary six-swap witness and independent gate audit:

```text
scratch/census_k17_two_bank_single_occurrence_swaps_20260731.py
SHA-256 0b2fa2802fb5562d453b8122864cbe0fe0c2c91aadd24d1b00afa3ccf0ce812d

scratch/k17_two_bank_single_occurrence_swaps_20260731.census.json
SHA-256 e9797343a3d6e841195b01b3541814562f8af8c6645f0d8e4795e2f0a9fa1d83
payload f005edf2557ea5d4b489b765c8b34f3d509c0bdced5c5e8c203df7e04e8e8a7d

scratch/audit_k17_sixswap_repaired_component_flow_gate_20260731.py
SHA-256 14b90b013dab73649b9b65097f14def799c2c4bbdb6fe8c0f60d362d8f7bf262

scratch/k17_sixswap_repaired_component_flow_gate_20260731.audit.json
SHA-256 f4ef27f5cff0da81552ab8025738de36e03ba1ec38789c36432401cb1a621ea6
payload aeb9f4741fc9553fa44594bfe0a31615c8a27fa34e4b1257bfc9adb9df2b3b5b

scratch/audit_ad_k17_sixswap_one_steiner_bridge_20260731.py
SHA-256 7d88ed612f3a2a2b7f0f489b2e697f67808df88cf0f0573029c244978c57b8c8

scratch/ad_k17_sixswap_one_steiner_bridge_20260731.audit.json
SHA-256 a494fe8cff0632552fdbea87062f03a4e5f5ea14d54129a2e9eb0de4695a3ca7
payload f1f100988c993d28c761be2b5b1ec2669d8c3150580d34d28b583c867ac51b82

scratch/audit_ad_k17_sixswap_residual_halfport_four_socket_20260731.py
SHA-256 72e22d8f039a8962241e68ade081419c1b80935b060f5fc42578f3f040b5015d

scratch/ad_k17_sixswap_residual_halfport_four_socket_20260731.audit.json
SHA-256 89a445f6732f5d9ffbf127928dc5afa04a986f3a969396188e093c95c8c27621
payload bf2da14db7870a01686425caf533e66e846d7eccee4ca5712e2ec26c634ab81d
```

Fallback clean-atom witness and independent replay:

```text
scratch/search_k17_marked_atom_phase_path_20260731.py
SHA-256 5761a6168d39faeebc3e1e8eba9d2733d81b6ecebd6edf462291c82fff33256a

scratch/k17_marked_atom_phase_path_20260731.json
SHA-256 234a34703cdef66722d6df54b936361048565915f4bf9ab523e13368d828bdec
payload 3f36ddc1a6fd02d4e8b90b3cd48576c54dc8882caa94f1066dca564732e21447

scratch/h2_independent_audit_k17_marked_atom_phase_path_20260731.py
SHA-256 333ad936c5d528e6f3b83ebae9c912bb52bbfab2a60c1ebb35ca522d4194246b

scratch/h2_independent_k17_marked_atom_phase_path_20260731.audit.json
SHA-256 eee050b70c9ac3742a1d217b218b399d032a26a5b6de99afda8ef02ec9f52217
payload 3295407b01911e11e2fe731abd296b265502d6ec3db0ea90fe834504cf4da71d
```

Both audits are solver-free.  The first was replayed locally in `0.26`
seconds; the second in `1.47` seconds.  No heavy local or remote solve was
launched because the primary repaired face is already excluded by
Corollary 6.1.
