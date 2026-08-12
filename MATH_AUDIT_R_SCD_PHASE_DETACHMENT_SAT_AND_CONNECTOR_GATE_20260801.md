# Audit of the SCD phase-detachment SAT and its Catalan connector gate

Date: 2026-08-01  
Lane: R / four-row SCD C-phase detachment  
Status: exact independent audit.  The five saved models for `m=4,...,8`
are genuine Catalan path forests, but acyclicity is **not** implied by the
SAT encoding.  A complete clause-satisfying cyclic model already exists at
`m=4`.  The subsequent component-joining problem is an exact
endpoint-colour matching plus graphic-independence problem.

## 0. Verdict

The encoder

`scratch/search_scd_global_seed_detachment_sat_20260801.cpp`

has the following exact scope.

1. Its target, provider, head, tail and release rows force the advertised
   upper and lower palettes and physical maximum degree two.  The apparent
   omission of collisions between a retained provider tail and a new
   auxiliary tail is harmless: the former never contains `z`, whereas the
   latter always contains `z`.
2. It has no graphic, subtour, component-count or potential row.  This is
   a substantive omission.  The explicit `m=4` assignment in Section 4
   satisfies every DIMACS clause and every palette/degree row but has one
   directed and undirected cycle.
3. Independently replayed saved models for `m=4,5,6,7,8` nevertheless have
   zero cycles and exactly
   `Cat_m=14,42,132,429,1430` components.  Thus these five witnesses are
   valid forests; what is invalid is the inference "SAT implies forest."
4. A simple strict-potential subcatalogue is sufficient for automatic
   acyclicity (Section 5), but it excludes the reversed-long phases used by
   the saved witnesses.  Those witnesses require literal replay or added
   graphic cuts.
5. A Catalan forest is not yet one spanning path.  Joining its `C=Cat_m`
   components requires `C-1` endpoint-to-endpoint Johnson edges, distinct
   missing lower colours and a tree after component contraction.  Upper
   colours may and generally must repeat.  Section 7 gives the exact
   necessary-and-sufficient 0--1 gate.

No equality or all-dimensional existence theorem follows from the present
finite SAT data.

## 1. Fixed objects and notation

Let

\[
 G=[2m-3],\qquad \Omega=G\mathbin{\dot\cup}\{a,z\},
 \qquad W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad C=W-U=\operatorname {Cat}_m.
\]

The standard Greene--Kleitman central rows are `S<L` on a short chain and

\[
 R<S<L<U\quad\hbox{or}\quad R<S<L<U<W
\]

on a long chain.  The fixed bijection `M_0` from rank-`(m-1)` roots to
rank-`m` owners is exactly the map rebuilt independently in the checker.
An original `a`-provider indexed by `L` has root tail `aS`; an original
`z`-provider indexed by `U` has root tail `L`.

Every selected target replaces one original provider edge by two rooted
edges

\[
       t_1\longrightarrow h_1,\qquad t_2\longrightarrow h_2.      \tag{1.1}
\]

The first realizes a formerly missing upper target (`aU` or `W`), while
the second retains the selected provider's old upper colour (`azL` or
`zU`).

## 2. What the CNF does and does not encode

For each option variable `x_o`, the CNF contains precisely:

* exactly one option for every target;
* at most one option for every original provider `(kind,provider)`;
* at most one selected new edge entering each root (`head1` and `head2`);
* at most one selected auxiliary tail `tail2` at each root;
* if a selected new edge enters the head of an original provider, at least
  one option using that provider must be selected, thereby releasing its
  old edge.

It contains no cycle or component clause.

### Lemma 2.1 (the omitted retained-tail row is redundant)

The displayed clauses imply that every final root has outdegree at most
one, even though `tail1` and retained provider tails are not inserted into
the explicit `new_tail_vars` table.

#### Proof

Every `tail1` is exactly the tail of the provider being removed.  Provider
capacity makes selected `tail1` roots distinct; an unselected provider
retains its edge, while a selected provider does not.  Original provider
tails have one of the two signatures

\[
                         aS\quad\hbox{or}\quad L,                \tag{2.1}
\]

and therefore do not contain `z`.  Every auxiliary `tail2` has one of the
signatures

\[
                         azR,\quad zS,\quad zV,                 \tag{2.2}
\]

and therefore contains `z`.  Thus no auxiliary tail can collide with a
selected or retained original tail.  Explicit `tail2` capacity handles
collisions within (2.2).  \(\square\)

The head-capacity and release rows analogously imply indegree at most one.
Since `M_0` is bijective, physical owner degree is at most two.

### Lemma 2.2 (palette exactness is structural)

Every clause-satisfying assignment has all `U` rank-`(m+1)` upper colours
exactly once and `U` distinct rank-`(m-1)` lower colours.

#### Proof

The first edge of (1.1) realizes the chosen target, and target equality
uses every `aU` and every all-`G` `W` once.  The second edge has the same
upper colour as the removed provider.  Provider capacity plus retention of
every unused provider uses each `azL` and `zU` once.  These four upper
signature classes are disjoint.

Every generated rooted edge is a Johnson edge whose lower intersection is
its root tail.  Lemma 2.1 makes all final tails distinct, hence all lower
colours are distinct.  The fixed edge count is `U`.  \(\square\)

Thus the only missing central-owner row is graphic independence.  It is
not implied by the palette or degree equations.

## 3. Independent replay of the saved models

The independent checker

`scratch/audit_scd_global_seed_detachment_sat_models_20260801.cpp`

rebuilds the SCD and `M_0` rather than trusting the generator's decoded
edge list.  It checks every DIMACS clause; validates every option's literal
set identities; restores every unselected provider; checks Johnson
legality, both palettes, root in/outdegree and physical degree; and finally
uses an independent disjoint-set replay to require zero undirected cycles
and exactly `Cat_m` components.

The authenticated results are:

| `m` | selected / clauses | final edges | upper/lower | max in/out/owner | components | cycles | selected phases |
|---:|---:|---:|---:|---:|---:|---:|:---|
| 4 | 6 / 282 | 21 | 21/21 | 1/1/2 | 14 | 0 | `aD-long 4, aD-short 1, zR 1` |
| 5 | 28 / 3890 | 84 | 84/84 | 1/1/2 | 42 | 0 | `aD-long 14, aD-short 7, zR 7` |
| 6 | 120 / 40440 | 330 | 330/330 | 1/1/2 | 132 | 0 | `aC 23, aD-long 37, aD-short 24, zA 19, zR 17` |
| 7 | 495 / 352275 | 1287 | 1287/1287 | 1/1/2 | 429 | 0 | `aC 108, aD-long 132, aD-short 90, zA 45, zR 120` |
| 8 | 2002 / 2711250 | 5005 | 5005/5005 | 1/1/2 | 1430 | 0 | `aC 473, aD-long 498, aD-short 316, zA 137, zR 578` |

These are exact witness statements, not a theorem for other models or
other `m`.

## 4. Complete `m=4` cyclic countermodel

Put `G=[5]`.  Select the following five `a` target/provider pairs:

\[
\begin{array}{c|c|c}
\text{target}&\text{provider }L&\text{phase}\\ \hline
a1235&123&\text{reversed long D}\\
a1245&125&\text{reversed long D}\\
a1345&145&\text{short D}\\
a2345&345&\text{short D}\\
a1234&234&\text{reversed long D}.
\end{array}                                                     \tag{4.1}
\]

Their first physical arrows form the directed cycle

\[
 a123\longrightarrow a125\longrightarrow a145\longrightarrow
 a345\longrightarrow a234\longrightarrow a123.                \tag{4.2}
\]

For the sole target `W=12345`, use provider `U=1234` and delete coordinate
`2` from its filler.  In the generated option map, the six positive
variables are exactly

\[
                            \{2,14,18,22,26,37\}.                \tag{4.3}
\]

Every target/provider/tail/head/release clause passes.  Restoring the
unused providers gives 35 owner vertices and 21 edges with all 21 upper
and all 21 lower colours distinct, root maximum in/outdegree one and owner
maximum degree two.  Nevertheless (4.2) is one directed and undirected
cycle, so the graph has 15 components rather than `Cat_4=14`.

The literal model is

`scratch/r_scd_detachment_audit_20260801/phase_m4_cycle_countermodel.out`.

The original decoder reports

```text
selected=6 edges=21 max_in=1 max_out=1 max_phys=2
upper/lower=21/21 components=15 cycles(dir,undir)=1,1
```

but returns success, because cycles/components are printed rather than
included in its final failure condition.  The independent checker rejects
the same model at its forest gate.

### Corollary 4.1 (required correction)

Any use of this CNF as a forest existence proof must add either exact
graphic/subtour cuts or a proved strict potential.  In final-edge
variables the exact row is

\[
             |E(Q)|\le |Q|-1\qquad(\varnothing\ne Q\subseteq V). \tag{4.4}
\]

For (4.2), the five selected variables in (4.1) require their sum to be at
most four.  In option variables a lazy cycle clause must also allow a
retained edge on the cycle to be released; merely forbidding the currently
selected replacement variables is not sufficient for a general cycle
containing retained providers.

## 5. A valid strict-potential subcatalogue

Give `i in G` weight `i`, give `a` weight zero, give `z` weight `2m-2`, and
put

\[
                              \Phi(T)=\sum_{x\in T}w(x).          \tag{5.1}
\]

Retain only options satisfying:

1. an `a` first exchange `x -> y` has `y>x`;
2. every long `a` provider uses the aligned C phase (whose second exchange
   is `rho -> x` with `rho<x`); the short D phase is allowed;
3. a `z` first exchange `y -> v` has `v>y`;
4. the second `z` exchange is oriented from the smaller of `t,y` to the
   larger.

Then every final physical arrow strictly raises `Phi`.  The retained
provider increments are `w(z)-x` and `w(z)-y`; the short second increment
is `x-w(a)=x`; the aligned long increment is `x-rho`; and the two first
increments are `y-x` and `v-y`.  A `Phi`-minimum vertex on an undirected
cycle would have two outgoing arrows, contradicting Lemma 2.1.

This is a correct automatic-acyclicity theorem, but not an audit shortcut
for the five saved models: they use reversed-long D phases.

## 6. Universal endpoint--hole cocycle

Let `F` be any spanning degree-at-most-two graph with the exact full upper
palette and an injective lower palette of size `U`.  Let `H` be its family
of `C` missing lower colours.  For coordinate `q`, define

\[
 H_q=|\{K\in H:q\in K\}|,
 \qquad
 E_q=\sum_{T\ni q}(2-d_F(T)),                                  \tag{6.1}
\]

where endpoint holes are counted as occurrence slots (a singleton
component contributes two).

### Theorem 6.1 (endpoint--hole cocycle)

For every coordinate `q`, independently of phases and independently of
whether `F` has cycles,

\[
                    \boxed{E_q=H_q+2\operatorname {Cat}_{m-1}.} \tag{6.2}
\]

#### Proof

For every Johnson edge with owners `T,T'`, lower `K=T cap T'` and upper
`R=T union T'`, coordinatewise

\[
               \mathbf1_T(q)+\mathbf1_{T'}(q)
              =\mathbf1_K(q)+\mathbf1_R(q).                    \tag{6.3}
\]

The used owner-slot incidence at `q` is

\[
 2{2m-2\choose m-1}-E_q.
\]

The exact upper palette contributes `{2m-2 choose m}`, while the lower
palette contributes `{2m-2 choose m-2}-H_q`.  The two latter binomial
coefficients are equal and

\[
 {2m-2\choose m-1}-{2m-2\choose m-2}=\operatorname {Cat}_{m-1}.
\]

Summing (6.3) gives (6.2).  \(\square\)

The five replayed phase mixtures pass (6.2) automatically from their
literal palette/degree replay.  Conversely, (6.2) kills a proposed
one-stratum packet bank whenever its prescribed endpoint and lower-hole
profiles differ by anything other than the constant vector
`2 Cat_(m-1)`.  It does **not** detect the cycle in Section 4.

## 7. Exact connector gates

There are two distinct scopes.  The occurrence-level physical gate may
reverse/reown old path components and therefore uses arbitrary free
endpoint slots.  The stricter fixed-`M_0` gate may only join the canonical
sink of one directed component to the canonical source of another.  A
negative result for the first scope is strongest; a positive result in the
first scope would still need a reownership packet before it implied the
second.

Now assume `F` is one of the Catalan path forests, with path-component set
`mathcal C`, `|mathcal C|=C`.  Make every residual degree unit
`2-d_F(T)` an occurrence-labelled endpoint slot at owner `T`.

An admissible connector `e` consists of two distinct free endpoint slots
at owners `T,T'` in different components such that

\[
 |T\mathbin{\triangle} T'|=2,\qquad
 k(e)=T\cap T'\in H.                                           \tag{7.1}
\]

Its upper colour `r(e)=T union T'` is unrestricted and may repeat an old
or another connector upper colour.

### Theorem 7.1 (physical endpoint matching plus graphic gate)

There is a Johnson Hamilton path containing every edge of `F` and using
no repeated lower colour if and only if there are binary variables `x_e`
on the admissible connectors satisfying

\[
\begin{aligned}
 &\sum_e x_e=C-1,                                               &&\tag{7.2a}\\
 &\sum_{e\ni p}x_e\le1 &&\text{for every endpoint slot }p,     &&\tag{7.2b}\\
 &\sum_{e:k(e)=K}x_e\le1 &&\text{for every }K\in H,            &&\tag{7.2c}\\
 &\sum_{e:\,c_-(e),c_+(e)\in A}x_e\le |A|-1
      &&\text{for every nonempty }A\subseteq\mathcal C.        &&\tag{7.2d}
\end{aligned}
\]

Here `c_-(e),c_+(e)` are the two component endpoints of the contracted
connector.

#### Proof

Conditions (7.2b) and (7.2c) are exactly endpoint matching and missing-
lower-colour injection.  Condition (7.2d) says that the contracted
connector set is graphic-independent.  With `C-1` edges on `C` component
vertices it is therefore a spanning tree.  Each old path has only two
endpoint slots, so the spanning tree has component degree at most two and
is itself a path; orienting its components in order yields the required
Johnson Hamilton path.  The converse follows by deleting the `C-1`
intercomponent edges of any such path.  \(\square\)

This is a three-resource integral problem (two endpoint slots, one lower
colour, and a contracted graphic row), not ordinary scalar Hall or plain
matroid intersection.

If the selected connectors leave lower hole `K_0`, let `e_q` be the two
final endpoint-slot incidences and let

\[
 R_q=|\{e:x_e=1,\ q\in r(e)\}|                                 \tag{7.3}
\]

count connector upper colours with multiplicity.  Subtracting the used
connector slots from (6.2) gives the exact completion cocycle

\[
       \boxed{e_q=2\operatorname {Cat}_{m-1}
                       +\mathbf1_{q\in K_0}-R_q.}               \tag{7.4}
\]

Thus the `C-1` upper repeats are allowed, but their coordinate profile is
forced by the final two endpoint slots and the sole unused lower colour.
Set identities alone cannot replace occurrence-labelled endpoint
matching in (7.2).

Equivalently, if the final endpoint owners are `T^- ,T^+`, then

\[
 \deg_R(q)=2\operatorname {Cat}_{m-1}
   +\mathbf1_{q\in K_0}-\mathbf1_{q\in T^-}-\mathbf1_{q\in T^+}.
                                                                    \tag{7.5}
\]

If those endpoints are Johnson adjacent with

\[
 K_0=T^-\cap T^+,\qquad R_0=T^-\cup T^+,                         \tag{7.6}
\]

then `Q=R dotcup {R_0}` is a size-`C` multiset of rank-`(m+1)`
blocks with constant coordinate degree

\[
                         \deg_Q(q)=2\operatorname {Cat}_{m-1}.   \tag{7.7}
\]

This abstract repeat design always exists for every prescribed `R_0`:
after reserving it, Gale--Ryser realizes `C-1` labelled block vertices of
degree `m+1`, with residual coordinate degrees `2c-1` on `R_0` and `2c`
off `R_0`.  This is explicitly a multiset theorem; distinct labelled block
vertices may have the same neighbourhood.  Physical endpoint realization
and (7.2) remain completely separate.

## 8. Current-model connector audit

The connector test used the literal component and endpoint occurrences
reconstructed in Section 3, not merely the missing-colour sets.  The full
physical endpoint catalogue (allowing component reversal/reownership) has:

| `m` | `C` | candidate edges | dead endpoint slots | capacity upper bound | required `C-1` |
|---:|---:|---:|---:|---:|---:|
| 4 | 14 | 82 | 5 | 11 | 13 |
| 5 | 42 | 322 | 18 | 33 | 41 |
| 6 | 132 | 1326 | 50 | 107 | 131 |
| 7 | 429 | 5508 | 157 | 350 | 428 |
| 8 | 1430 | 22074 | 638 | 1111 | 1429 |

If `z_0` endpoint slots occur in no candidate, every connector set has
size at most `floor((2C-z_0)/2)`.  The table therefore proves all five
forests infeasible before lower-colour or graphic cuts.  At `m=8`, the
size-two component with roots `731,16987` (owners `1755,17115`) is wholly
unserviceable, and six missing lower colours have no endpoint provider.

This is a scoped endpoint-only no-go, not a no-go for a joint detachment
and connector choice or an interior rethread.

## 9. Joint detachment--connector model and exact `z` cut

The joint implementation

`scratch/solve_threadD_scd_detachment_hamilton_path_20260801.py`

does not freeze one forest.  It retains the full flexible ear variables,
adds every rooted connector

\[
 q\longrightarrow M_0^{-1}(q+y),\qquad y\notin M_0(q),          \tag{9.1}
\]

and imposes the combined indegree/outdegree equations including retained
providers.  One source and one sink force exactly `C-1` connectors and
every lower root except the sink exactly once.  In path mode, a strict
all-different order on the `W` roots eliminates every directed cycle and
therefore forces one Hamilton path.  This order formulation is equivalent
to lazy subtour cuts for feasibility.  Base upper colours remain exact;
connector upper colours are unrestricted repeats.

The weaker degree-only projection (one path plus possible directed cycles)
is already CP-SAT `INFEASIBLE` throughout the audited range:

| `m` | roots | ear options | rooted connector menu | status | wall seconds |
|---:|---:|---:|---:|:---|---:|
| 4 | 35 | 38 | 105 | INFEASIBLE | 0.004 |
| 5 | 126 | 262 | 504 | INFEASIBLE | 0.019 |
| 6 | 462 | 1572 | 2310 | INFEASIBLE | 0.230 |
| 7 | 1716 | 8704 | 10296 | INFEASIBLE | 1.539 |
| 8 | 6435 | 45698 | 45045 | INFEASIBLE | 5.001 |
| 9 | 24310 | 230962 | 194480 | INFEASIBLE | 23.276 |

These CP-SAT verdicts have exact replayed model semantics but no portable
proof log.  Their mathematical explanation is the following solver-free
cut.  Put

\[
 c=\operatorname {Cat}_{m-1},\qquad
 I_m=C-2c.
\]

For every flexible phase selection, the unused lower bank contains

\[
 H_z=C-c
\]

roots containing `z`, while exactly

\[
 S_z=c
\]

component-source owner tickets contain `z`.  A rooted connector from a
`z`-containing lower tail must enter a source owner containing `z`.
Because only one lower tail may remain unused, rooted completion requires

\[
 H_z-1\le S_z,
\]

but its exact deficit is

\[
                     H_z-1-S_z=I_m-1>0\qquad(m\ge4).             \tag{9.2}
\]

Thus the current joint grammar is impossible in every `m>=4` before
acyclicity.  Adding the short paired-ear layer is a genuine enlargement:
it may change the lower-hole/source-ticket ledger and is not covered by
(9.2).

The separate flexible detachment at `m=9` is positive: its authenticated
forest has 8008 selected options, 19448 exact upper/lower edges, maximum
degrees `1/1/2`, zero cycles and `Cat_9=4862` components.  This does not
contradict (9.2), which concerns rooted component completion.

## 10. Short paired-ear enlargement

The anonymous capacity-two count `I_m<=2c` does not give two physical
cut units per short chain.  In the exact upper-palette ledger, the new
first-stage variable

\[
 h_{S,U}: C_S=L_S\longrightarrow P(U)                         \tag{10.1}
\]

is an alternative realization of an existing `zU` provider colour.  The
second-stage short D relocation is already an ordinary `aU` target option.
After its displaced target occurrence is restored, only (10.1) changes
the endpoint current.

For `r` selected first-stage rethreads, exact typed counting gives

\[
 H_z=c+I_m,\qquad t_z=c-r,\qquad S_z=c+r.                       \tag{10.2}
\]

Thus each short chain supplies exactly one, not two, units of
`kappa_z=S_z-H_z+1`, and rooted completion requires

\[
                              r\ge I_m-1.                       \tag{10.3}
\]

Tail capacity gives `r<=c`.  Consequently the entire paired-ear bank
leaves the exact residual

\[
 I_m-1-c={m-5\over m+1}c-1,                                    \tag{10.4}
\]

equal to `5,32,142,571` for `m=6,7,8,9`.  It cannot repair the current
rooted grammar in those dimensions.  The exact joint extension must put
the `h` alternatives in the native `zU` provider equations and all their
arcs in the common degree/graphic rows; treating the two serial stages as
anonymous capacity-two services is unsound.

The required next actuator must have positive net signed gain

\[
                    \Delta\kappa_z=\Delta S_z-\Delta H_z       \tag{10.5}
\]

after every displaced upper provider, lower tail and source head is
restored.  Gross creation of a `z` head is not enough if the same packet
consumes another `z` source.

## 11. Swapped-stratum hybrid scope

The coordinate swap `F(a,z) -> F(z,a)` gives a genuine macroscopic
alternative, but its neutral switch cube has an exact invariant.  Close
each path by a typed dummy carrying its missing lower, terminal owner,
source owner and private upper.  The two augmented factors are perfect on
all four resource shores, so connected components of their coloured
incidence symmetric difference switch independently.

For every such component `Gamma`, equivariant dummy labels give

\[
             \Delta\kappa_a(\Gamma)+\Delta\kappa_z(\Gamma)=0.  \tag{11.1}
\]

Thus neutral conjugate switching can transfer directed connector slack but
cannot create total two-coordinate slack.  The authenticated saved
`m=4,...,9` bases all have negative `kappa_a+kappa_z`; no component subset
can make both cuts nonnegative, even before topology.  Almost all
individual nonzero components are nevertheless forest-safe, so the failure
is the invariant, not a shortage of local switches.

Topology remains exact: an augmented hybrid is a directed permutation;
after deleting dummies it is a forest iff every permutation cycle contains
a dummy.  Every all-real cycle supplies a lazy phase-flip clause.

The positive undirected two-stratum cocycle theorem is not contradicted.
It realizes `E=H+2c` but does not create directed source slack.  The next
packet must have positive

\[
             \Delta\kappa_a+\Delta\kappa_z,                    \tag{11.2}
\]

or start from a base with nonnegative sum.  More neutral switching and the
short-ear bank cannot close the lane.

## 12. Corrected implication boundary

The exact proved chain is now

\[
\begin{array}{c}
\text{phase CNF SAT}\\
\Downarrow\\
\text{exact upper palette + injective lower palette + degree at most 2}\\
\not\!\Downarrow\quad\text{forest},\\[2mm]
\text{SAT + graphic cuts (or strict potential)}\\
\Downarrow\\
\text{Catalan path forest}\\
\not\!\Downarrow\quad\text{one path},\\[2mm]
\text{Catalan path forest + (7.2)}\\
\Longleftrightarrow\\
\text{one lower-rainbow Johnson Hamilton path containing the forest}.
\end{array}
\]

Residence, deeper shadows and a literal common-cap compiler remain separate
from this central owner/palette/connector theorem.

## 13. Audited artifacts

* phase encoder:
  `scratch/search_scd_global_seed_detachment_sat_20260801.cpp`,
  SHA `16faf809cdb88942df4702874165d9f276e0e6ca182ceada33009ff229931911`;
* independent forest/cycle audit:
  `MATH_AUDIT_R_SCD_PHASE_DETACHMENT_FORESTS_CYCLE_OMISSION_AND_CONNECTOR_SCOPES_20260801.md`,
  SHA `1d378b474ee9c32517815cfd75b55683319a9fdc1008f187a2a247e39247ce6a`;
* explicit cyclic clause model:
  `scratch/r_scd_detachment_audit_20260801/phase_m4_cycle_countermodel.out`,
  SHA `69500be4c319220d8bc3c16a979a2675464bf915ed39b8da46ee1d4989a62c08`;
* exact joint degree source used for the local `m=4,...,9` regressions:
  `scratch/r_scd_detachment_audit_20260801/joint_degree_source_used.py`,
  SHA `e0c3205735ceaab5cb239cee45c4600674cb6b4d77e5aa822a3e42820e750915`;
* repeat-design theorem and independent audit:
  `MATH_THEOREM_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md`,
  SHA `1e927c75f062552789d80ad121e45c0ae502bb8ca52ee7a41d76d20a0422bc08`,
  and `MATH_AUDIT_R_CATALAN_CONNECTOR_REPEAT_DESIGN_COCYCLE_20260801.md`;
* exact paired-ear correction:
  `MATH_THEOREM_R_SCD_PAIRED_EAR_Z_CUT_SUPPLY_AND_JOINT_PATH_GATE_20260801.md`,
  SHA `f7ce2c201b33c2da7c9f17e546be627bdc8f9f93106b7fe2cf20e691c396681e`;
* exact neutral swapped-component theorem:
  `MATH_THEOREM_TWO_SWAPPED_SCD_COLORED_COMPONENT_TRANSFER_AND_SUM_COCYCLE_NOGO_20260801.md`,
  SHA `8cec59cf332669c71ed6f2d8f444aa495cbb0d449a70b75f2336f83aac5d716e`.
