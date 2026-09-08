# K17 occurrence296+C6: rebased pure-hex master and certified arity-two escalation

Date: 2026-07-31  
Status: exact base-fibre reduction, scoped forest-first pure-C6 no-go, and
escalation theorem; no arity-two packet, compiler, K17 word, or all-dimension
claim

## 0. Verdict

Let `F*` be the authenticated occurrence296+C6 incidence factor represented
by

```text
scratch/k17_opt28_occ296_c6_localmin_verified_20260731.residual.json
  SHA-256 6fcc91d45b2090b26b612020340a21088a2367c5c0bccd10d3d3614042c60fe4

scratch/k17_opt28_occ296_c6_localmin_verified_20260731.owner_cycle.word
  SHA-256 a47aa9d7c8b86ca3912c8c82262969332727d27bf427ee8783ccb1a8ce664b49
```

It is a one-cycle degree-two owner/colour factor with all `24,310` rank-nine
owners and all `24,310` lower-q1 colours exactly once.  The literal marked
packet contains `4,108` owners and remains fixed.  Its currently audited
physical defects are

```text
strict nonflat D2 / D3                         503 / 503
literal inversion mismatches / missing bits   748 / 776
upper holes rank 10 / 11 / 12            1585 / 824 / 116
upper holes rank 13 through 17                       0.
```

The ambient incidence-hex identities survive the change of base, but their
applicability, orientation, residence action, and provider action do not.
They must all be evaluated again on `F*`.

That re-evaluation is now finite and exact.  The boundary-correct audit scans
all `2,333,760` Boolean C6 identities, finds `45,024` identities applicable
to `F*`, and retains `28,121` columns after the literal marked-owner guard.
These are the complete one-step, base-applicable, marked-safe columns, not
merely the old hazard-active subcatalogue.

There are two exact outer faces:

1. keep the full composed degree-two factor and demand one cycle; or
2. freeze only the selected packet-side structure and solve a fresh asymmetric
   residual `b`-flow.

On either face, rank-ten provider composition is not the sum of isolated
hex deltas when two selected hexes change opposite endpoints of one lower
colour.  There is an exact quadratic cross term, or equivalently an exact
endpoint-pair AND formulation.

Finally, a pure-hex obstruction authorizes arity-two split/merge promotion
only for components occurring in a replayed core, with any outside helper
drawn from an explicit resource/socket halo.  Rado applies only after the
entire guarded packet-installability relation has genuinely been proved to
be a matroid, normally a strict gammoid.

## 1. Ambient hex identities and base-relative applicability

Let `Gamma` be the bipartite incidence graph between rank-eight colours and
rank-nine owners.  For a rank-seven set `K` and distinct labels `a,b,c`
outside `K`, put

```text
colours: K+a, K+b, K+c,
owners:  K+ab, K+bc, K+ca.
```

The induced incidence hex has two alternating three-incidence phases,
denoted `P_eta^0,P_eta^1`.  These two phase sets depend only on the Boolean
incidence geometry, not on a chosen factor.

### Lemma 1.1 (identity persistence and orientation rebase)

An oriented hex `(eta,epsilon)` is a legal one-step toggle of `F*` if and
only if

\[
 P_\eta^\epsilon\subseteq F^*,\qquad
 P_\eta^{1-\epsilon}\cap F^*=\varnothing.             \tag{1.1}
\]

Its signed column is

\[
 \Delta_\eta=
 \mathbf1_{P_\eta^{1-\epsilon}}
 -\mathbf1_{P_\eta^\epsilon}.                         \tag{1.2}
\]

Every incidence-hex identity stored for an earlier base remains an algebraic
zero-degree identity, but its old applicability and orientation metadata are
invalid on `F*` until (1.1) is rechecked.

#### Proof

Each phase has degree one at the same three owners and three colours, so
their signed difference is zero at every incidence vertex.  Replacing one
phase by the other is a simple-factor move precisely when all removed
incidences are present and all added incidences are absent.  This is (1.1).
Nothing in this argument refers to the old factor.  \(\square\)

### Full-universe caveat

The old count `44,917` was the set of hexes alternating on the old factor,
not the ambient set of all Boolean incidence-hex identities.  Consequently,
a complete `F*` catalogue must rescan the ambient identities.  Some old-active
hexes can become inactive or reverse orientation, and previously inactive
identities can become applicable.

Moreover, even after rebasing, the master must not retain only the hexes
which hit a current hazard.  An applicable hex with zero immediate hazard
gain can be a **return hex** needed to:

* cancel an incidence-resource conflict;
* change the opposite endpoint of a colour;
* destroy a defect created by another selected hex;
* restore a protected provider; or
* merge/split factor components in the required direction.

Therefore inactive return hexes cannot be omitted from a claimed complete
pure-hex master unless a proved dominance theorem transforms every feasible
selection using them into one not using them while preserving incidence
balance, packet guards, residence, topology, and every protected provider.
An active-only UNSAT result is scoped to that restricted atlas and cannot by
itself certify the need for arity two.

### Audited rebased census

```text
ambient C6 identities                              2,333,760
applicable identities                                  45,024
marked-owner-safe columns                              28,121
hazard-active columns                                   2,100
rank-ten isolated-provider-active columns               8,252
cycle-preserving / split-2 / split-3            13,875/10,620/3,626
removed incidence resources / nontrivial cliques 35,744/25,575
added incidence resources / nontrivial cliques   63,825/18,225
```

All `296` inherited forest hazards have support.  An exact edge-disjoint
interval packing has size `197`, hence every pure-hex cover uses at least
`ceil(197/3)=66` columns.  The present rank-ten layer has `1,585` holes;
`10` have no **single-column** isolated provider.  This is not a compound
no-go because two columns changing opposite endpoints have the cross term
in Theorem 3.1.

Against the old `5,433` active rows, `3,476` retain their orientation, none
reverse, and `1,957` become inapplicable.  Across the full old/new marked-safe
atlases, `15,452` identities keep orientation, `111` reverse, `12,370` are
old-only, and `12,558` are new-only.  Copying old applicability or orientation
bits is therefore unsound.

## 2. Exact base-relative incidence master

Let `H*` be any declared set of applicable oriented hexes on `F*`, and let
`y_h` be its selection variable.  For every incidence `e`, define

\[
 x_e=\mathbf1_{e\in F^*}+\sum_{h\in H^*}\Delta_h(e)y_h. \tag{2.1}
\]

### Theorem 2.1 (incidence bounds are exact)

The selected columns compose to a simple degree-two owner/colour factor if
and only if

\[
                         0\le x_e\le1                 \tag{2.2}
\]

for every incidence appearing in a column.  No separate owner-degree,
colour-degree, or lower-palette equation is needed.

For columns oriented directly against `F*`, (2.2) is equivalent to

\[
 \sum_{h:e\in P_h^-}y_h\le1\quad(e\in F^*),\qquad
 \sum_{h:e\in P_h^+}y_h\le1\quad(e\notin F^*).       \tag{2.3}
\]

#### Proof

Every column has zero signed degree at all owners and colours.  Hence the
affine vector (2.1), whenever binary, has exactly the degree vector of `F*`,
namely degree two everywhere.  Conversely, a simple selected factor has
binary incidence vector and satisfies (2.2).  In a common base-relative
orientation every removed incidence belongs to `F*` and every added
incidence lies outside it, giving (2.3).  \(\square\)

### Packet and old-defect rows

Every literal incidence used by one of the `134` protected packet signatures
must be fixed.  Avoidance of all protected owners is sufficient for a
packet-side-only signature.  If a signature also records the exterior end of
a boundary colour, that incidence needs its own fixed guard.

For an inherited strict run `rho` with final-edge support `E(rho)`, retaining
all those edges preserves the run.  Thus the old-hit row is necessary.  It is
not sufficient, because selected columns can create new strict runs.  Once a
candidate factor contains a new internal run with final factor-edge variables
`b_e`, its exact lazy cut is

\[
                    \sum_{e\in E(\rho)}b_e\le |E(\rho)|-1. \tag{2.4}
\]

The old-base figures `5,433` active columns, `724` hazard rows, and the
pure-hex floor `151` do not transfer to `F*`.  The current row bank, support
degrees, and disjoint-interval packing must all be recomputed.

## 3. Exact rank-ten provider composition

Use the same boundary-correct linear zipper normalization as the authenticated
occ296+C6 materialization.  Every exposed rank-ten provider is then the union
of the two rank-nine endpoints selected at one lower colour.  The one omitted
linear closing edge is treated as unexposed.

Fix an exposed lower colour `c` whose endpoints in `F*` are `a,b`.  A hex
`h` changing `a` to `u` has isolated signed target delta

\[
 \delta_h(T)=
 \mathbf1_{u\cup b=T}-\mathbf1_{a\cup b=T}.           \tag{3.1}
\]

Suppose a second compatible hex `g` changes the opposite endpoint `b` to
`v`.  The actual final provider is `u union v`, not either isolated gain.

### Theorem 3.1 (exact two-endpoint correction)

For every target `T`, the required pair correction is

\[
 \kappa_{hg}(T)=
 \mathbf1_{u\cup v=T}
 -\mathbf1_{u\cup b=T}
 -\mathbf1_{a\cup v=T}
 +\mathbf1_{a\cup b=T}.                              \tag{3.2}
\]

Thus the exact rank-ten load is

\[
 \mu_T(y)=\mu_T^*+
 \sum_h\delta_h(T)y_h+
 \sum_{c}\sum_{\substack{h,g\text{ changing opposite}\\
                           \text{endpoints of }c}}
      \kappa_{hg}(T)y_hy_g.                           \tag{3.3}
\]

Incidence-capacity rows permit at most one selected change of each baseline
endpoint, so no higher-order term occurs.

#### Proof

If neither endpoint, only `a`, or only `b` changes, (3.3) is exactly the
corresponding isolated delta.  If both change, adding (3.1) and its
`b -> v` analogue counts the old pair twice negatively and counts the two
mixed old/new pairs positively.  Adding (3.2) cancels those three erroneous
terms and leaves

\[
             \mathbf1_{u\cup v=T}-\mathbf1_{a\cup b=T},
\]

the true change.  There are only two incidences at a colour.  \(\square\)

An equivalent linear formulation introduces final-incidence variables
`x_(c,u)` and

\[
 z_{cuv}=x_{cu}\wedge x_{cv}.                         \tag{3.4}
\]

Since every colour has final degree two, exactly one unordered endpoint pair
is selected, and

\[
                 \mu_T=\sum_{c,\{u,v\}:u\cup v=T}z_{cuv} \tag{3.5}
\]

is exact.  Formula (3.5) remains correct when the endpoints are chosen by a
forest-first residual flow.

Let

\[
 G_{10}=|\{T:\mu_T^*=0,\ \mu_T>0\}|,
 \qquad
 L_{10}=|\{T:\mu_T^*>0,\ \mu_T=0\}|.                \tag{3.6}
\]

Because `F*` has exactly `1,585` rank-ten holes, its final rank-ten hole
count is exactly

\[
                         1585-G_{10}+L_{10}.           \tag{3.7}
\]

This is the correct rank-ten objective.  Isolated column scores are exact
only on a face where at most one endpoint of every colour can change.
Ranks eleven and twelve still require the target-labelled accumulated-union
product or literal interval replay.

## 4. The two exact topology faces

### 4.1 Full-cycle face

Keep every final incidence in (2.1).  The result is a two-factor by Theorem
2.1.  Install component/subtour cuts until it is one cycle, anchor its
orientation on the unchanged marked interval, and apply the exact residence,
rank-ten endpoint-pair, arbitrary-upper, and inversion replays.  No residual
pairing is released.

This face is called cycle-preserving only after the global one-cycle row is
passed.  Individual hexes are degree-preserving but can split or merge cycle
components.

### 4.2 Forest-first asymmetric face

After composing selected hexes, freeze only:

1. every final incidence at a protected/tagged owner and every protected
   packet-side incidence;
2. both final incidences of every selected-touched colour; and
3. no unrelated incidence at a pure fixed-other owner.

Let the frozen graph be `K_y`.  For a free owner `u` and lower colour `c`,
put

\[
 b(u)=2-\deg_{K_y}(u),\qquad d(c)=2-\deg_{K_y}(c).     \tag{4.1}
\]

Let `N(u)` be the set of allowed residual colours after fixed and forbidden
incidences are removed.

### Theorem 4.1 (exact asymmetric residual Hall criterion)

The frozen graph has a degree-two residual completion if and only if total
owner and colour demand agree and, for every colour set `S`,

\[
 \sum_{c\in S}d(c)
 \le
 \sum_u\min\{b(u),|N(u)\cap S|\}.                    \tag{4.2}
\]

#### Proof

Use a capacitated network with source-to-owner capacity `b(u)`, unit
owner-to-colour arcs for legal incidences, and colour-to-sink capacity
`d(c)`.  The max-flow/min-cut theorem gives exactly (4.2), and integrality
gives a literal incidence completion.  \(\square\)

A frozen zero-socket cycle or a frozen internal residence/inversion failure
is an immediate obstruction.  Endpoint run states are exported to the
residual connector.  Rank-ten loads must be evaluated from the completed
incidences by (3.5), not from pre-flow hex scores.

Every frozen path exports its first and last three owners.  Every
marked/complement transition additionally exports the adjacent owners, their
lower colour, the two incidences, and the three-owner trace window on each
side.  Marked interiors are tested at token threshold three; complementary
owner interiors are tested at threshold four, exactly facet-token threshold
three after erosion.  These collars are obligations, not residence
certificates: the residual chronology must consume and literally replay all
of them.

If the frozen graph is already the full spanning cycle, no residual connector
can absorb a collar.  Orient the cycle by the fixed marked packet, form its
literal physical zipper row, and test that whole row at threshold three.  For
a bad token interval `[s,e)`, retain the factor edges determining the extended
window `[s-1,e]`: marked-owner token `i` is determined by factor edges
`i-1,i`, whereas complementary facet token `j` is determined by factor edge
`a-1+j`.  Retaining all their incidences retains the same bad window, so the
local lazy cut

\[
       \sum_{f\in E(s,e)}x_f\le |E(s,e)|-1            \tag{4.3}
\]

is sound.  The full-cycle face requires the same physical-row replay; a
complement-interior scan alone misses the two marked/facet boundaries.

Every feasible full-cycle selection is feasible in the forest-first face by
choosing its released incidences again.  The converse need not hold.

## 5. Exact pure-hex cores

For the LP consisting only of hazard-cover and resource-capacity rows, a
Farkas certificate has nonnegative hazard multipliers `alpha_r` and resource
multipliers `beta_q` satisfying

\[
 \sum_{r\in R_h}\alpha_r
 \le \sum_{q:h\text{ consumes }q}\beta_q
 \quad(h\in H^*),
 \qquad
 \sum_r\alpha_r>\sum_q\beta_q.                       \tag{5.1}
\]

For the integral lazy master, an exact conflict core must additionally
include every final-edge residence guard, rank-ten endpoint-pair row, packet
guard, and topology row used in the proof.  Solver timeout, failure to find a
cover, or UNSAT of an active-only catalogue is not such a core.

Given a replayed core `C`, define its principal component support `K(C)` as
the old components meeting at least one of:

* a hazard or final-edge motif in `C`;
* a capacity incidence in `C`;
* a protected provider/witness occurrence in `C`;
* a packet/socket guard in `C`; or
* the literal support of a topology cut in `C`.

An option supported wholly outside all variables of `C` cannot invalidate
the core.  Therefore only packets with a principal input in `K(C)` need be
promoted.  A helper outside `K(C)` is allowed only through an explicitly
enumerated resource/socket halo.  Omitting all outside helpers is complete
only if a separate separation theorem proves that none can couple to the
core.

For an implemented assumption core, this support is computed relative to the
complete unguarded structural system.  Form its factor graph with column and
definition variables on one shore and removed/added incidence cliques, touch
definitions, and endpoint-pair AND definitions on the other.  Start with all
variables in guarded core rows and take connected-component closure.  An
unguarded constraint outside this closure shares no variable with the core
and cannot affect its feasibility.  The provenance components in this
closure are therefore a certified safe promotion scope.  Merely unioning the
component labels printed on guarded rows is not.  A helper outside the closure
is admitted only by explicitly adding its resource/socket edges to the halo
and recomputing the closure.

## 6. Lossless arity-two split/merge signature

For an arity-two packet `p`, retain

\[
 \Xi(p)=
 (B_p,\mathcal P_p;
  O_p,C_p,I_p^-,I_p^+;
  \partial j_p,\pi_p;
  H_p,G_p;
  \mathsf R_3(p);
  \mathsf E_{10}(p);
  \mathsf U_{12}(p)).                                \tag{6.1}
\]

The fields are:

* `B_p`: the two provenance-labelled input components;
* `P_p`: the oriented output path forest;
* `O_p,C_p,I_p^-,I_p^+`: exact owner, lower-colour, and signed incidence
  resources;
* `partial j_p,pi_p`: signed socket current and the pairing of alternating
  trail ends;
* `H_p`: the exact core obligations serviced;
* `G_p`: required/forbidden incidences and protected packet/provider tickets;
* `R_3(p)`: internal defect set and both endpoint collars;
* `E_10(p)`: the endpoint-labelled transition at every touched lower colour;
  and
* `U_12(p)`: the target-labelled prefix, suffix, and interval transfer.

The endpoint-labelled `E_10` field cannot be replaced by isolated gained and
lost target sets: two separately selected packets can change opposite
endpoints of one colour and create the cross term (3.2).

The packet is closed guarded only when its interior owner/colour derivative
is zero, all nonzero current is advertised at sockets, its internal residence
and inversion tests pass, every guard is satisfied, and its provider ledger
is composed with all other selected packets through (3.5) and the exact
upper transfer product.

Resource-neutral arity-two labelled path forests preserve the total number
of input components.  Hence any genuine split of one input is accompanied by
a merge involving the other input.  This is why arity two, rather than an
independent split flag, is the first exact split/merge layer.

## 7. Guarded Rado theorem and its qualifications

Fix one core and first group every correlated service/casualty derivative
into one atomic obligation.  Let `A_i` be the guarded packet options realizing
obligation `i`.

Suppose physical installability is represented exactly by vertex-disjoint
routes in one directed unit-capacity network `N`: its vertices encode all
incidence resources, occurrence tickets, sockets, protected witnesses,
endpoint-colour resources, topology ports, and fixed guards.  Suppose also
that every independent route family decodes to one common legal packet
selection with the advertised joint derivative.  Then the installable packet
families form the strict gammoid `M(N)`.

### Theorem 7.1 (exact guarded Rado cut)

All atomic core obligations have distinct jointly installable
representatives if and only if

\[
 r_{M(N)}\left(\bigcup_{i\in X}A_i\right)\ge |X|
                  \qquad\text{for every }X.           \tag{7.1}
\]

When (7.1) fails, a violating `X` and a minimum vertex separator of size
strictly below `|X|` form a replayable Rado core.

#### Proof

This is Rado's independent-transversal theorem.  Strict-gammoid rank is the
maximum number of vertex-disjoint source-to-sink routes and equals minimum
separator capacity.  \(\square\)

Three qualifications are essential.

1. One arity-two packet cannot be cloned as two representatives for its two
   serviced components.  Use a fixed principal/helper convention or group
   the complete derivative as one obligation.
2. Arbitrary incidence set packing, pairwise provider cross terms, and
   selection-dependent guards are not automatically matroids.  They must be
   encoded exactly in `N` or retained in the integral packet master.
3. If `N` is only a sufficient routed atlas, its min-cut excludes only that
   atlas.  It is not an unrestricted arity-two obstruction.

After packet selection, the socket current still feeds the separate residual
Hall system (4.2); Rado rank does not imply residual degree completion or
one-cycle topology.

## 8. Exact boundary

This note proves:

* the base-independent C6 identity and exact `F*` applicability test;
* the complete rebased marked-safe catalogue census and resource ledger;
* exact incidence-resource balance for simultaneous rebased hexes;
* the two-endpoint rank-ten cross correction;
* exact cycle-preserving and forest-first outer faces;
* the component support legitimately certified by a pure-hex core;
* the lossless arity-two resource/guard/Rado interface; and
* the scoped forest-first pure-C6 no-go in Section 9.

It does not prove:

* that an active-only catalogue is complete;
* that pure hexes or arity-two packets repair the current `503` residence
  defects and `1,585/824/116` upper holes;
* ranks eleven/twelve or common-cap feasibility from rank-ten gains;
* a K17 word or an all-dimension regenerative construction.

A pure-hex UNSAT certificate is scoped to its exact declared catalogue and
outer face.  It excludes neither inactive return hexes omitted without a
dominance proof, newly activated sequential hexes, longer alternating
circuits, occurrence-base changes, nor a genuinely nonflat compiler.

## 9. Exact forest-first no-go and minimal local escalation core

The complete `28,121`-column master reached two exact feasible CEGAR rounds
(`197` then `208` hexes) and then `INFEASIBLE`.  Its final `1,035` guarded
obligations replay to the sufficient three-row core

```text
111  hazard 111, component 943
588  complement R3, components 943,1715
763  complement R3, components 601,943,1715.
```

The core has the following solver-free deletion-minimal proof.  Hazard `111`
uniquely forces `h=25925`.  Conditioned on `h`, the exact final-incidence sums
of rows `(588,763)` are `(6,5)`.  The complete compatible breaker bank for
row `588` is the singleton `c=26083`.  It removes
`(0x1b708,0x1f708)` but adds row 763's sole false literal
`(0x1b708,0x1b70a)`, so `{h,c}` has sums `(5,6)`.  The conditioned row-763
return bank is empty.  Therefore the three rows are jointly infeasible.

Deletion witnesses are literal:

```text
omit 111: empty selection has sums (5,4);
omit 588: {25925} has row-763 sum 5;
omit 763: {25925,26083} has row-588 sum 5.
```

The conditional two-obligation Rado rank is consequently `1`, not the
diagnostic bipartite matching size `0`.  Exact rank-ten replay gives no gain
and loses `{0x1a7ac,0x1b7c8}` under both `{h}` and `{h,c}`.

The first structural promotion halo contains only helper columns `26082` and
`26134`.  The former conflicts with `h` on removed incidence
`(108424,108488)`; the latter conflicts with `c` on removed incidence
`(124680,124682)`.  Its mapped component union is

```text
{601,943,1022,1278,1715,2775,3661,3734}.
```

This is the certified first one-hop arity-two split/merge scope, not a proof
that every possible compound helper lies there.  Full structural closure is
not a localization: it reaches `28,041/28,121` columns and `99,090`
incidence-resource nodes.

Frozen evidence:

```text
scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.result.json
  SHA 85f059f7d8d271c41179b76f63f7e43f224fde7c9276813a445203bfb3ce4ed1
scratch/threadD_k17_occ296_c6_forest_3adc26bf_20260731.core.minimized.json
  SHA 449b57349a84a3138983b13c49bf4e6ac97ba4e506bbc3b0f66e71df3249c9ca
scratch/threadD_k17_occ296_c6_core3_rado_signature_20260731.audit.json
  SHA d3f50520c9ee47b8a7572c885d72a871fdf1751ce7fcb9cdf02a2c12b5c463aa
scratch/threadD_k17_occ296_c6_core3_deletion_minimal_hand_certificate_20260731.json
  SHA 149e6d014b72e6b77e873f2f5c61eb8438cf6223bf99b9449a062299000d556a
```

The no-go is only for this frozen base, the complete base-applicable
marked-safe pure-C6 catalogue, and the declared forest-first internal rows.
It does not exclude a certified arity-two packet, a sequentially activated
nonbase C6, a longer alternating circuit, or a different occurrence base.
