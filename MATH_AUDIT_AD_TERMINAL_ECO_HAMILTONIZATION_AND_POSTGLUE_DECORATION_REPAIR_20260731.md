# Audit of terminal ECO Hamiltonization and post-glue decoration repair

Date: 2026-07-31  
Status: independent proof audit; central serial implication and post-glue
equivalence **PASS**; corrected Stage-A definition audited and one
proof-expansion supplied below; no all-dimension existence or downstream
contiguous-OR claim

## 0. Audited statement and verdict

The audited source is

```text
MATH_THEOREM_AD_TERMINAL_ECO_HAMILTONIZATION_AND_POSTGLUE_DECORATION_REPAIR_20260731.md
```

at the terminal source snapshot SHA-256

```text
a58f05b535ba6eb9a2fec85ff01721477a66e970c4bfe1230d4f7375965ab26e
```

Its central implication is correct:

> A pairwise port-disjoint family of strict ECO hypermerges whose
> component--atom incidence graph is a tree produces one undecorated
> Hamilton cycle.  Any subsequent literal circuit packet with Hamilton
> endpoint may then be forgotten except for that endpoint.  If the endpoint
> has one Catalan decoration on the forest side of the exact binary-trace
> criterion, its diamond lift is a spanning two-sided-rainbow
> `Cat_m`-path forest.

No decoration, owner matching, occurrence-router path, or common decorated
Boolean cube is needed during the first stage.  This is a genuine weakening
of the **interface on a fixed raw bank**.  It is not a proof that the raw
bank or the final repair exists in every dimension.

The latest source already incorporates the necessary definition correction.
Every selected atom is a positive-rank strict hypermerge in the previously
frozen sense, and hence

   \[
                         r_t=|S_t|\in\{2,3\}.                    \tag{0.1}
\]

An atom with `r_t=1` is a rethread/split candidate, not a hypermerge.  The
displayed proof could be generalized to a connectivity-preserving unary
rethread, but then “strict ECO incidence hypertree” and “every atom is
component-progressing” would no longer have their established meanings.

The current source now includes the explicit induction that the physical
component partition equals the connected-component partition induced by
the already exposed atom nodes in the incidence tree.  Lemma 2.1 below
independently replays that proof.

## 1. Numerical normalization

Fix `m>=2`, put `Omega=[2m-1]`, and set

\[
 Q=\binom{2m-1}{m-1},\qquad
 P=\binom{2m-1}{m-2},\qquad
 K=Q-P.                                                        \tag{1.1}
\]

The ratio

\[
                         \frac P Q=\frac{m-1}{m+1}               \tag{1.2}
\]

gives

\[
 K=\frac{2Q}{m+1}=\operatorname {Cat}_m,\qquad
 2Q=(m+1)K,\qquad P+Q=mK.                                     \tag{1.3}
\]

Thus all three numerical identities used in the source are exact.  In
particular, `2Q` is the full rank-`m` layer size on
`Omega union {infinity}`, and `P+Q` is the size of either rank-`m-1` or
rank-`m+1` colour shore on that enlarged ground set.

## 2. Stage A: exact component-partition induction

Let `F_0` be a spanning two-factor with initial component set `V`.  For
every selected ECO atom `t`, let `S_t subseteq V` be the set of initial
components containing its three old factor edges.  Assume:

* distinct atoms have disjoint six-port sets;
* all old atom edges lie in `F_0`;
* each atom is a strict hypermerge on `S_t`, with `|S_t|` equal to two or
  three; and
* the bipartite incidence graph `B(V,T)` is a tree.

For `U subseteq T`, let `B_U` be the incidence forest on vertex set
`V union U` containing precisely the incidences of atoms in `U`.  Define
two members of `V` to be `U`-equivalent when they lie in the same component
of `B_U`.

### Lemma 2.1 (subset component invariant)

After toggling the atoms of `U` in any executable order, two initial factor
components lie in the same physical component if and only if they are
`U`-equivalent.

#### Proof

For `U=empty`, both partitions are the original component partition.
Assume the assertion for `U` and expose an unused atom `t`.  Any two
distinct neighbours of `t` in `B` lie in distinct components of `B_U`:
otherwise their path in `B_U`, together with their two incidences through
`t`, would be a cycle in the tree `B`.

By the induction hypothesis, the physical blocks containing the members of
`S_t` are therefore pairwise distinct.  Strict hypermerge faithfulness says
that toggling `t` replaces exactly those blocks by their union and splits no
other block.  This is exactly the change in the incidence partition caused
by adjoining node `t` and its incident edges to `B_U`.  The assertion follows
by induction. \(\square\)

### Corollary 2.2 (terminal Hamiltonization)

The simultaneous symmetric difference is one Hamilton cycle, and every
ordering of the selected atoms is executable.

#### Proof

Port disjointness means that every atom replaces one perfect matching of
its six ports by the other and no operation changes a pending atom's old
edges.  Hence every subset state is a spanning two-factor and the toggles
commute.  Lemma 2.1 applies in every order.  At the full set, `B(V,T)` is
connected, so the physical factor is connected.  A connected spanning
two-factor is one Hamilton cycle. \(\square\)

The rank identity

\[
                \sum_{t\in T}(|S_t|-1)=|V|-1                    \tag{2.1}
\]

also follows immediately from the incidence-tree edge count.  It is a
check on the proof, not a substitute for component faithfulness.

### Why strictness is load-bearing

Port disjointness alone certifies only simultaneous degree two.  When the
three old edges lie on three distinct cycles, the alternating ECO matching
joins the three opened paths into one cycle, so ternary strictness is
automatic.  When two old edges lie on one cycle and the third on another,
the first cycle opens into two paths; the literal new pairing must be
checked to ensure that all three paths become one cycle.  Support size two
and incidence acyclicity do not decide that pairing.  The source correctly
keeps the binary strictness audit as a separate hypothesis.

## 3. Stage B: exact decoration and trace ledger

Write the terminal Hamilton cycle as

\[
 A_0,B_0,A_1,B_1,\ldots,A_{Q-1},B_{Q-1},A_0,                   \tag{3.1}
\]

with `|A_i|=m-1`, `|B_i|=m`, and
`A_i subset B_i superset A_{i+1}`.  Let

\[
 \ell_i=A_i\cap A_{i+1},\qquad u_i=B_{i-1}\cup B_i.            \tag{3.2}
\]

If `I` and `J` biject onto all upper and lower turn colours and their marks
alternate by rail type, then

\[
                          |I|=|J|=P.                             \tag{3.3}
\]

Deleting the `2P` marked positions from the `2Q`-cycle leaves even paths.
Their perfect matching is unique and has

\[
                      |R|=\frac{2Q-2P}{2}=Q-P=K                 \tag{3.4}
\]

cross edges.  The diamond lift consequently has

\[
 |E|=|I|+|J|+|R|=2P+K=P+Q=mK,                                 \tag{3.5}
\]

on

\[
                         |V|=2Q=(m+1)K                          \tag{3.6}
\]

vertices.  The perfect-diamond equivalence proves that every lower colour
in `binom(Omega union {infinity},m-1)` and every upper colour in
`binom(Omega union {infinity},m+1)` occurs exactly once.  This enlarged
ground-set qualification is implicit in the source and should be retained
whenever the palette claim is quoted.

Now write the cyclic binary mark word as

\[
                 1^{a_1}0^{b_1}\cdots1^{a_s}0^{b_s},            \tag{3.7}
\]

where alternation of mark types implies every positive zero-run has even
length `b_i>=2`.  The exact trace theorem says that the physical degree-two
graph contains a cycle if and only if

\[
                  b_i=2\text{ for all }i,qquad
                  a_i\text{ is odd for all }i.                   \tag{3.8}
\]

It then contains exactly one cycle.  Therefore, **under the preceding
alternating-decoration conditions**, the forest alternative is exactly

\[
 \boxed{\text{some positive zero-run has length at least four, or some
 marked run has even length}.}                                  \tag{3.9}
\]

This is precisely Item 4 in the source.  The qualification “under Items
1--3” is logically load-bearing: (3.9) is the negation of (3.8) only after
the residual zero-runs are known to be positive and even.

When (3.9) holds, maximum degree two plus acyclicity makes the lift a
spanning linear forest.  Euler's identity gives

\[
                 c=|V|-|E|=2Q-(P+Q)=Q-P=K.                       \tag{3.10}
\]

Thus every Stage-B count and the exact `K`-component conclusion are
correct.  Isolated vertices, if present, are counted as path components and
cause no exception.

## 4. Repair packets need only be terminally Hamiltonian

Let

\[
 C=C^{(0)},C^{(1)},\ldots,C^{(s)}=C^*                           \tag{4.1}
\]

be literal spanning two-factors, with each transition the symmetric
difference with an even circuit alternating with the preceding factor.
The central serial implication uses only that `C^*` is Hamiltonian.  It
does not use Hamiltonicity of an intermediate state, commutation of the
circuits, disjointness from the ECO ports, or preservation of any Stage-A
occurrence mark.  Hence the source is correct to call an everywhere
Hamilton-safe packet merely a stronger convenient certificate.

Once `C^*` and its accepting decoration are supplied, all Stage-A and
intermediate data disappear from the proof.  Applying Corollary 2.2 and
then the ledger of Section 3 proves the serial theorem with quantifiers

\[
 \exists T\quad\exists\mathcal R(T)\quad
 \exists(I,J)\text{ on the endpoint of }\mathcal R(T).           \tag{4.2}
\]

There is no hidden universal decoration quantifier over the ECO cube.

### Theorem 4.1 (alternating-circuit universality audit)

For any two spanning two-factors `F,F'` of the same graph, there is a
finite sequence of alternating **closed-trail** toggles from `F` to `F'`,
all of whose intermediate states are spanning two-factors.  If the ambient
graph is bipartite, as `ML(2m-1)` is, the trails may be recursively split
into simple alternating even cycles.

#### Proof

Colour `F-F'` red and `F'-F` blue.  At each vertex the red and blue degrees
are equal: both are `2-d`, where `d` is the number of common incident
factor edges.  Pair the red and blue half-edges locally.  Following these
pairings decomposes the symmetric difference into edge-disjoint closed
alternating trails.  Splitting at a repeated transition state gives
edge-disjoint alternating circuits (allowing the standard closed-trail
meaning of circuit).

Before one such circuit is processed, all of its red edges are still in the
current factor and all of its blue edges are still absent, because the
circuits are edge-disjoint.  Toggling it exchanges equally many incident
red and blue edges at every visited vertex, so degree two is preserved.
After all circuits are toggled, the current factor is `F'`. \(\square\)

The closed-trail convention is material in an arbitrary nonbipartite
graph.  On vertices `v,a,b,c,d`, let

\[
 R=\{va,vb,cd\},\qquad B=\{ab,vc,vd\},\qquad
 H=\{ac,bd\}.                                                    \tag{4.3}
\]

Then `F=H union R` and `F'=H union B` are both five-cycles.  Their
symmetric difference is two odd triangles meeting at `v`; neither triangle
is alternating, while their six-edge bow-tie traversal is one alternating
closed trail.  Thus the arbitrary-graph theorem is exact with “circuit” in
the standard closed-trail sense.  If “circuit” is intended to mean a simple
cycle, its general statement must be restricted to bipartite graphs.  This
does not weaken the middle-levels corollary.

Consequently, from any fixed Hamilton cycle `C_0`, existence of a terminal
repair packet ending at an accepting Hamilton cycle is **equivalent** to
existence of an accepting Hamilton cycle.  Intermediate states need not be
Hamiltonian.  This validates the new direct simplification in the source:
ordinary Middle Levels Hamiltonicity makes Stage A optional for bare
existence, and the weakest middle-levels-resolvable target is the Decorated
Middle Levels Theorem itself.

This equivalence does not make every Catalan linear matching
middle-levels-resolvable.  It only removes the choice of the initial
Hamilton cycle and the circuit route once an accepting Hamilton endpoint
in this sufficient subclass exists.

## 5. Exact project-`m=5` calibration

For `m=5`,

\[
                       (Q,P,K)=(126,84,42),                       \tag{5.1}
\]

so the physical lift has `252` vertices, `210` edges and `42` path
components.  The frozen three-`C10` theorem independently supplies:

* two port-disjoint strict standard glues from the three-component raw
  factor to a Hamilton cycle;
* lower, upper and augmented deficiencies
  `(3,3,3)->(2,2,2)->(1,1,1)->(0,0,0)`;
* a final perfect augmented matching of order `210`;
* `84` marks on each rail, alternating in cyclic order; and
* a binary trace on the linear-forest side.

Therefore the project-`m=5` fixture is a literal positive instance of the
terminal order

\[
       \text{two raw ECO glues}\longrightarrow
       \text{three sequential `C10` repairs}\longrightarrow
       \text{one terminal decoration}.                           \tag{5.2}
\]

The stronger facts that the repair circuits are disjoint from the ECO
ports, commute with the glues, and support one common transported
decoration are unnecessary for (5.2).  They belong to the stronger
repair-first prepared-collar certificate.

## 6. Comparison with the repair-first private collar

There are three distinct interfaces.

1. **Minimal terminal route.**  Supply one accepting decorated Hamilton
   cycle.  By Theorem 4.1, the starting Hamilton cycle and the intervening
   circuit packet impose no additional existential restriction.
2. **Transparent gluing route.**  Supply one decoration already on the
   component factors and a gluing list preserving its two local colour
   multisets, alternating boundary mark types, and a forest-side trace
   guard.  This implies an accepting terminal cycle, but an accepting
   terminal cycle need not expose any decoration on an earlier factor.
3. **Repair-first private collar.**  In addition to transparent transfer,
   carry a leaf-forest owner matching, component-faithful merge state, and
   private/laminar occurrence routes on the same labels.

Thus, on a fixed dynamically transparent gluing construction, private
collar implies transparent gluing implies a terminal accepting cycle.  No
reverse implication is valid without extra transported data.

The transparent interface quoted in the source is exact.  A hexagon toggle
changes neighbour pairs only at its six ports, so a fixed selected
occurrence set preserves the two turn-colour bijections if and only if the
selected local turn-colour multisets agree separately on the two shores.
Deleting the old matching leaves at most three retained path fragments.
Reversal preserves alternation inside each fragment, so global alternation
after reconnection is equivalent to the last/first shore types being
opposite at every new seam.  These two tests preserve a decoration, but
they do not alone preserve forest topology: one must additionally retain a
trace breaker, or carry the exact bit excluding the unique cycle face.  If
leaf-peelability is demanded, the changed gap edges must also be loopless
and acyclic after contraction of the unchanged gap forest.  These are
stronger dynamic hypotheses than terminal existence.

The frozen project-`m=4` census is consistent with this separation: `31`
alternating hexagons, `16` Hamilton endpoints, `10` decorable endpoints,
and only `6` common-decoration transfers.  The counts are imported from
the independently audited finite theorem; they are not needed in the
general implication.

For a **fixed raw strict bank and its fixed endpoint**, the terminal
interface asks strictly fewer during gluing: no upper transversal, gap
matching, owner alignment, occurrence linkage, prefix decoration, or
commuting repair cube.

The complete existential architectures are nevertheless incomparable
without extra hypotheses.

* Repair-first preparation may change the factor components and create a
  new strict ECO bank.  It need not leave any strict bank on the raw factor,
  so it need not imply Stage A.
* A terminal packet may overlap the raw ECO ports and destroy every old
  owner/socket/router certificate.  It need not imply a repair-first
  prepared cube.

On the common specialization where the **same selected ECO bank** is
component-faithful and incidence-tree independent on both sides of a
support-disjoint repair rectangle, and one final decoration transports over
the whole cube, the repair-first certificate may be executed in the
opposite order and implies the terminal certificate.  The project-`m=5`
fixture proves both architectures and endpoint commutation, but it does
**not** lie in this same-bank specialization: the raw basis is
`{g0,g1}`, whereas after repair either singleton is a basis and the pair is
a dependent rethread state.

## 7. Proved and unproved scope

The following are proved by the audited implication:

1. strict disjoint incidence-hypertree Hamiltonization;
2. terminal postglue decoration lift;
3. exact palette, edge, vertex and component counts;
4. alternating-circuit universality and the exact postglue equivalence;
5. serial quantifier separation; and
6. the project-`m=5` calibration.

The following do not follow:

1. an all-`m` strict ECO incidence hypertree;
2. an all-`m` terminal repair packet or accepting decoration;
3. preservation of all-depth upper/lower shadows;
4. residence, endpoint sockets, voltage or component closure beyond the
   central path forest; or
5. any compiler Hall statement or literal contiguous-OR word.

In particular, the terminal theorem is a clean central CLMT reduction, not
a coefficient-one theorem.

## 8. Dependencies independently checked

The audit uses the exact statements in:

* `MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`
  (SHA-256
  `a9779950d781b1914fca6eafca6212da2b21e1560c8b68bfb2cfaae85759d1a8`);
* `MATH_THEOREM_CATALAN_ECO_COMPATIBLE_HYPERTREE_PRIVATE_COLLAR_20260731.md`
  (SHA-256
  `90be9fe0e77b7050a1dd130244c1f668a5d8254973e1f44d9e6189304660a93e`);
  and
* `MATH_THEOREM_CATALAN_STANDARD_M5_THREE_C10_PRIVATE_REPAIR_20260731.md`
  (SHA-256
  `1be05f74fbbc0f050117d3d04e9720bc972d5838c623af2636b838a4884dbd66`);
  and
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`
  (SHA-256
  `3c5007b3759e94a635593eaf83980dd93819c7f3d9bf8e280ab50fa46678b6e2`).

No computational search is used in this audit.  The finite `m=5` claims
are imported only at their frozen, independently audited scope.
