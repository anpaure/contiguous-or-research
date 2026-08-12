# `k=17` shuffle201: synchronized flag--transition circulation and the moving Hall shore

Date: 2026-08-01  
Lane: R / chronology-first OFHT  
Status: exact compact formulation, exact fixed-face obstruction, and a
proof-safe support-two construction.  This is not an owner-exact OFHT factor
or a `k=17` word.

## 0. Verdict

The independently authenticated rooted factor

```text
scratch/k17_rank8_rooted_static_shuffle201_20260801.certificate.tsv
SHA256 d44b60611a3c9e4ba1533a774762fce825d327dcc7536cdcd9c10522404b1ad3
```

has exact type and lower-target ledgers and literal chronology

```text
root turns / labelled state arcs              970 / 7760
packet matching / zero-out / zero-in          556 / 723 / 826.
```

There is an exact variable-eliminated model for the **collapsed packet-root
cycle-cover relaxation**: put a binary variable on each literal transition
between two complete row flags, impose one outgoing transition per root,
impose flow conservation at every row flag, and impose the type/target
resource rows on the tail flags.  A second formulation on full aligned
attachment states adds the root/owner transversal and is the exact
occurrence model.  Keeping these two levels separate is essential: row-flag
balance alone may splice two different attachment states.  Neither model is
ownerwise nibbling or an independent-endpoint union.

On the face fixing each row's type and assigned middle-suffix orbit, even
after freeing every literal middle-suffix phase and every residual inner
target, and then relaxing target one-use and common endpoint menus, the
permissive packet graph has

```text
menus / packet arcs / loops                    16925 / 7462 / 2
zero-out / zero-in                                  21 / 80
maximum matching                                      1335
Hall tail / neighbourhood                         1169 / 1074
deficiency                                               95.
```

Thus this whole fixed face is impossible.  Any packet-perfect repair changes
at least 48 complete row flags.  More specifically it changes the assigned
middle-suffix orbit or type on at least 24 rows when target resources may
migrate between the outer and inner stages, and on at least 48 rows if that
stage division is preserved.  Consequently a root-disjoint bank of resource
circuits of complete-row support at most two needs at least 24 nontrivial
circuits before packet perfection is even possible.

The old `1206/1080` shore is genuinely crossed: in the shuffle201 permissive
graph its old tail has 1322 neighbours.  But only 603 packet arcs are common
to the old and new fixed-face graphs, and the new `1169/1074` shore appears.
Therefore turn count, one fixed Hall shore, and ownerwise coverage are not
monotone potentials for this problem.  Every Hall cut must be priced inside
the resource-exact selection.

There is nevertheless a proof-safe construction.  The complete support-one
and support-two resource-circuit catalogue around shuffle201 has 2541 and
213714 moves, respectively.  The final reverse-tie selection has 42 unary
and 407 binary pairwise root-disjoint circuits.  It changes 856 roots,
preserves the full static resource ledger, and improves the
literal packet chronology to

```text
turns / matching / zero-out / zero-in          1855 / 954 / 234 / 445.
```

This is a strict exact improvement, but still only a necessary packet-level
relaxation.  The independently rebuilt common root--owner both-live graph
has matching only `718/1430`, so it does not supply the common owner-state
transversal, one cycle, upper shadows, opening, or compiler.

## 1. Exact common resource ledger

Let `P` be the 1430 rank-eight root orbits.  A complete row flag at root
`p` is

\[
                A_f\subset B_f\subset Q_p,
\tag{1.1}
\]

with ordered difference sizes equal to one of the nine certified types

\[
(1,5,2),(1,6,1),(2,5,1),(3,3,2),(3,4,1),
(4,3,1),(5,1,2),(5,2,1),(6,1,1).
\tag{1.2}
\]

For each necklace target `theta` of rank `2,...,7`, define

\[
 r_\theta(f)=
  {\bf1}_{[A_f]=\theta}+{\bf1}_{[B_f]=\theta},
\tag{1.3}
\]

and for each type `t` define `r_t(f)={\bf1}_{t(f)=t}`.  The exact demands
are

\[
 \sum_f r_t(f)=m_t,
 \qquad
 \sum_f r_\theta(f)=1,
\tag{1.4}
\]

where

\[
(m_0,\ldots,m_8)=(139,297,8,20,20,140,127,237,442).
\tag{1.5}
\]

The target coordinate in (1.3) is deliberately common to the two stages.
At rank six, 286 targets occur as `B` and 442 as `A`, exhausting all 728
rank-six target orbits.  At rank seven all 1144 target orbits occur as `B`.
At ranks two through five the exact target counts are `8,40,140,364`.
Rank-one `A` is slack and has no tight target row.

Relative to any incumbent factor `x^0`, a signed row replacement is an exact
resource circuit precisely when the sum of its removed vectors `(r_t,
r_theta)` equals the sum of its inserted vectors.  This includes stage
migration automatically; treating the `A` and `B` copies of a rank-six
target as different resources would be incorrect.

### Theorem 1.1 (conditional outer-shell Rado decomposition)

An outer shell at root `p` is a literal pair `h=(t,B)` with `B subset Q_p`
and sizes prescribed by `t`.  Fix one shell at each root.  For
`s=2,...,6`, let `P_s` be the shells whose type has `|A|=s`.  Let

\[
 T_s=\{\hbox{all rank-}s\hbox{ target orbits}\}\quad(2\le s\le5),
\tag{1.6}
\]

and let `T_6` be the rank-six target orbits not consumed by a selected
rank-six `B` shell.  Form a labelled bipartite graph `G_s`: its left shore
is `P_s`, its right shore is `T_s`, and a labelled edge `(h,theta;A)` exists
when `A in theta` and `A subset B_h`.

The selected shells extend to a complete exact static factor if and only if

1. their type multiplicities are (1.5);
2. their `B` target orbits are pairwise distinct; and
3. every `G_s`, `2<=s<=6`, has a perfect matching.

Rank-one rows then choose an arbitrary local singleton in `B`.

#### Proof

There are 1144 selected rank-seven `B` shells, so distinctness uses every
rank-seven target once.  There are 286 selected rank-six `B` shells.  The
remaining `728-286=442` rank-six targets equal the number of type-eight
rows needing rank-six `A`.  At ranks two through five the left-shore sizes
are respectively `8,40,140,364`, exactly the complete target-bank sizes.
Therefore a perfect matching in each `G_s` assigns every common target once,
and its edge label supplies a literal `A subset B` phase.  Together with the
shells this gives (1.4).  The converse matchings are read directly from any
exact factor.  `square`

Thus a proposed outer `B`/type circuit has a proof-safe completion oracle:
five bipartite matching tests, with the rank-six donor bank recomputed after
the proposal.  This is an exact conditional flow/Rado reduction.  It does
not select the chronology, and the dependence of `T_6` on the outer shell
selection is why the entire problem is not one fixed matching instance.

## 2. The synchronized transition-circulation theorem

For every root `p`, let `Omega_p` be its complete literal **row flags**
(1.1), and put `Omega=union_p Omega_p`.  Let `E` be the complete multiset of
individually literal aligned transitions after the attachment state is
forgotten.  A member

\[
                 \tau=(f,g;\iota)\in E
\tag{2.1}
\]

records its tail flag `f`, head flag `g`, and the physical aligned incidence
`iota`; parallel incidences are retained.  Write `tail(tau)=f` and
`head(tau)=g`.

### Theorem 2.1 (variable-eliminated collapsed packet master)

There is a resource-exact rooted flag factor together with a literal directed
cycle cover in the **collapsed row-flag packet graph** if and only if there
are binary variables `y_tau` satisfying

\[
\begin{aligned}
 \sum_{\tau:\,\operatorname{root}(\operatorname{tail}\tau)=p}y_\tau
    &=1 &&(p\in P),\\
 \sum_{\tau:\,\operatorname{tail}\tau=f}y_\tau
 -\sum_{\tau:\,\operatorname{head}\tau=f}y_\tau
    &=0 &&(f\in\Omega),\\
 \sum_{\tau} r_j(\operatorname{tail}\tau)y_\tau
    &=b_j &&(j\text{ a type or tight target resource}).
\end{aligned}
\tag{2.2}
\]

Here `b_j` is given by (1.4).  The attachment incidence has been projected
out of the state identity: two selected arcs may enter and leave the same
row flag through different attachment states.  Thus Theorem 2.1 is the exact
packet-root relaxation optimized in the finite audits, but it is not yet an
occurrence-owner chronology.

#### Proof

The first line chooses exactly one outgoing transition at each root.  Sum
the statewise balance equations over `Omega_p`; exactly one transition also
enters root `p`.  Since the variables are binary, one state `f_p` has one
outgoing transition.  Its balance equation forces one incoming transition
at that same state.  Every other state at `p` has neither.  Thus one common
complete row flag is used on the two sides of the chronology.  The final
line gives exactly (1.4), and every selected transition is literal by the
definition of `E`.

Conversely, orient every edge of a collapsed row-flag packet cycle cover.  Put
`y_tau=1` on its labelled transitions.  The common state at a packet gives
flow conservation, and exact static resources give the last line.  `square`

This is smaller than a formulation with separate flag variables: the
selected-state indicator is recovered as

\[
 x_f=\sum_{\tau:\,\operatorname{tail}\tau=f}y_\tau
    =\sum_{\tau:\,\operatorname{head}\tau=f}y_\tau.
\tag{2.3}
\]

It is a resource-constrained zero-one circulation on collapsed flags, not an ordinary
min-cost flow.  Root choice, type mass, and common target use are simultaneous
partition/resource systems; no total-unimodularity or matroid-intersection
claim is made for their literal Boolean submatrix.  The already proved
generic common-state chronology schema is non-TU, so an additional theorem
would be required before replacing (2.2) by an ordinary flow.

For the exact occurrence model let `widehat Omega` be the aligned attachment
states

\[
             s=(p,f,O,\sigma),
\tag{2.4}
\]

where `p` is the root, `f` its row flag, and `(O,sigma)` is one of its nine
owner/phase incidences.  Let `widehat E` be the established literal directed
state-arc multiset.  Write `D(s)=O` for the selected attachment-owner orbit.

### Theorem 2.2 (exact attachment-state resource circulation)

There is a resource-exact occurrence-owner quotient cycle cover if and only
if binary `z_alpha`, `alpha in widehat E`, satisfy

\[
\begin{aligned}
 \sum_{\alpha:\,\operatorname{root}(\operatorname{tail}\alpha)=p}z_\alpha
    &=1 &&(p\in P),\\
 \sum_{\alpha:\,\operatorname{tail}\alpha=s}z_\alpha
 -\sum_{\alpha:\,\operatorname{head}\alpha=s}z_\alpha
    &=0 &&(s\in\widehat\Omega),\\
 \sum_{\alpha:\,D(\operatorname{tail}\alpha)=O}z_\alpha
    &=1 &&(O\text{ an owner orbit}),\\
 \sum_\alpha r_j(f(\operatorname{tail}\alpha))z_\alpha
    &=b_j &&(j\text{ a type or tight target resource}).
\end{aligned}
\tag{2.5}
\]

Under the established state-arc convention, each selected arc's `H`
incidence pairs its tail root with the attachment-owner orbit of its head
state.  Hence one outgoing arc per tail root, state balance, and the owner
transversal in the third line make `H` exact on both shores.  An explicit
one-per-`H`-label row may be retained as a redundant fail-closed check.  The
proof is the same flow-conservation argument as Theorem 2.1, now on full
attachment states:
exactly one state is used at each root and owner, and that same state carries
the incoming and outgoing arcs.  Neither theorem asserts connectedness;
subtour or voltage rows remain additional.  `square`

Both circulation theorems are exact only on their respective
**full-support feasibility** faces.  They must
not be used to score a deficient intermediate factor: in a maximum
bipartite transition matching the unmatched left and right states may be
different, so statewise flow balance is then too strong.  The exact partial
collapsed packet objective keeps `x` and uses

\[
 \sum_{\tau:\,\operatorname{tail}\tau=f}y_\tau\le x_f,
 \qquad
 \sum_{\tau:\,\operatorname{head}\tau=f}y_\tau\le x_f,
 \qquad
 \max\sum_\tau y_\tau .
\tag{2.6}
\]

At objective 1430 all selected left and right capacities are saturated, so
(2.6) becomes Theorem 2.1.  Below 1430, (2.6), not a circulation surrogate,
is the transition-matching score used throughout this note.

For partial occurrence-state scoring, use binary selected-state variables
`x_s` and impose the translated rows

\[
 \sum_{s:\,\operatorname{root}(s)=p}x_s=1,\qquad
 \sum_{s:\,D(s)=O}x_s=1,\qquad
 \sum_s r_j(f(s))x_s=b_j.
\]

Together with `out(s)<=x_s` and `in(s)<=x_s`, maximize the state-arc
matching.  At 1430 these inequalities saturate and recover Theorem 2.2.
The finite numbers `556`, `954`, and the Hall shores below concern the
collapsed packet objective (2.6), not this stronger attachment-state
problem.

## 3. Exact Hall/min-cut decomposition

For column generation it is useful to restore `x_f` and separate the
transition matching.  The static master is

\[
 \sum_{f\in\Omega_p}x_f=1,\qquad
 \sum_f r_j(f)x_f=b_j,\qquad x_f\in\{0,1\}.
\tag{3.1}
\]

For any state family `X subset Omega`, let `Gamma^+(X)` be its literal head
neighbourhood in `E`.  A selected static factor extends to a packet cycle
cover if and only if

\[
       \sum_{f\in X}x_f
       \le
       \sum_{g\in\Gamma^+(X)}x_g
       \qquad(X\subseteq\Omega).
\tag{3.2}
\]

Indeed (3.2) is Hall's theorem on the selected copy of the state bipartite
graph.  A maximum matching supplies a violated set when one exists; the
usual alternating-reachability shore, equivalently a source--sink min-cut,
is an exact separation oracle.  This is the required chronology-first
decomposition: resource circuits generate or price columns of (3.1), while
the full matching, rather than ownerwise degree coverage, generates cuts
(3.2).

More generally the exact partial score is the Hall min--max

\[
 M(x)=1430-
 \max_{X\subseteq\Omega}
 \left(
   \sum_{f\in X}x_f-
   \sum_{g\in\Gamma^+(X)}x_g
 \right)_+.
\tag{3.3}
\]

Thus the matching deficit itself, not the number of dead rows, is the exact
cost-to-go oracle for a proposed resource-circuit selection.

Equivalently, introduce one integer score variable `M` and add the separated
family

\[
 M+\sum_{f\in X}x_f-
       \sum_{g\in\Gamma^+(X)}x_g\le1430
       \qquad(X\subseteq\Omega).
\tag{3.4}
\]

Maximizing `M` subject to (3.1) and (3.4) optimizes the full packet
transition matching exactly.  The same maximum-closure/min-cut oracle
separates these rows.  This reduced Benders form uses only selected flags,
the static resource equations, one scalar objective, and guarded Hall cuts;
transition variables are needed only to materialize a matching witness.

For a circuit bank `C` around an incumbent, one may instead use binary
`z_c`, the root-conflict rows

\[
                  \sum_{c:\,p\in\operatorname{supp}(c)}z_c\le1,
\tag{3.5}
\]

and the affine selected-state indicators.  Each circuit has zero resource
signature, so (3.1) is automatic.  The Hall separator (3.2) remains exact.
Independent greedy scores of circuits are not exact because a circuit can
delete the only transition supporting a different circuit's gain.

## 4. The fixed-face obstruction and its row price

Freeze at each shuffle201 root its type and assigned `B` necklace orbit.
Free all contained phases of that orbit and every assignment from the exact
residual `A` target banks.  Finally, independently union the endpoint menus,
discarding global `A` one-use and common-menu consistency.  Call the resulting
packet graph `U_1`.  Every consistent exact factor on this face is a subgraph
of `U_1`.

The independent exact replay gives

\[
 \nu(U_1)=1335,\qquad |S_1|=1169,\qquad
 |N_{U_1}(S_1)|=1074.
\tag{4.1}
\]

There is also a literal singleton cut at row 34:

```text
Q=1013, type=8, assigned B-orbit representative=501,
possible source C1 masks={4,16,32,64}, outdegree=0.
```

### Theorem 4.1 (shuffle201 outer/type edit floor)

Let a packet-perfect repaired factor differ from shuffle201 in assigned
`B` orbit or type on the row set `R`.  Then

\[
                         |R|\ge24.
\tag{4.2}
\]

If no tight target migrates between the old `A` and `B` stages, then

\[
                         |R|\ge48.
\tag{4.3}
\]

In every case at least 48 complete row flags differ from shuffle201.

#### Proof

A perfect matching sends at least
`|S_1|-|N_{U_1}(S_1)|=95` tails of `S_1` outside the old neighbourhood.
Let `K` be the rows which receive, as their new `A` target, a target that
belonged to the old `B` stage.  Exact target use maps every member of `K`
injectively to the old row whose `B` target it receives, and that old row
must lie in `R`.  Hence `|K|<=|R|`.

If neither endpoint of an escaping matched edge belongs to `R union K`,
both endpoint types and `B` orbits are fixed and their `A` targets remain in
the old residual bank.  Their endpoint menus therefore occur in the union
defining `U_1`, a contradiction.  A row is used at most once as matching
tail and once as matching head, so

\[
 95\le2|R\cup K|\le4|R|.
\tag{4.4}
\]

This proves (4.2).  If there is no stage migration, `K` is empty and (4.3)
follows.  In either case the complete flags changed on all rows of
`R union K`; the first inequality in (4.4) gives at least 48 such rows.
`square`

A stronger circuit-pricing row retains the location of those changes.  If
`D` is the set of changed complete flags, then

\[
 95\le
 \sum_{p\in D}
  \bigl({\bf1}_{p\in S_1}+{\bf1}_{p\notin N_{U_1}(S_1)}\bigr).
\tag{4.5}
\]

Every escaping edge contributes its changed tail role, changed head role,
or both.  Thus (4.5) is a valid covering cut on any explicit circuit bank.
For root-disjoint circuits of support at most two, each column has coefficient
at most four, and at least 24 columns are necessary.

The same argument gives a quantitative bound at every intermediate score.
Let `M` be the maximum packet transition matching after editing the outer
orbit/type rows `R`, and let `K` be the stage-migration receivers from the
proof.  Put `D_0=R union K`.  Tails outside `S_1` contribute at most
`1430-|S_1|`, tails in `S_1` ending in its old neighbourhood contribute at
most `1074`, and every remaining matched edge consumes a changed tail or
head incidence.  Hence

\[
\begin{aligned}
 M&\le1335+
 \sum_{p\in D_0}
  \bigl({\bf1}_{p\in S_1}+{\bf1}_{p\notin N_{U_1}(S_1)}\bigr)\\
  &\le1335+2|D_0|\le1335+4|R|.
\end{aligned}
\tag{4.6}
\]

Without stage migration, `D_0=R`, and therefore

\[
                         M\le1335+2|R|.
\tag{4.7}
\]

Equations (4.6)--(4.7) are adaptive Hall/resource cuts, not asymptotic
estimates.  They can be inserted directly into a circuit master.  Their
specialization `M=1430` recovers (4.2)--(4.3).

## 5. The Hall shore moves rather than vanishes

Let `U_0` be the corresponding permissive graph for the authenticated
`ad9e...` factor.  Its canonical Hall pair has sizes `1206/1080` and
deficiency 126.  Direct comparison gives

```text
old/new edge intersection                         603
old-only / new-only edges                   6909 / 6859
old/new Hall-tail intersection                    983
old/new Hall-neighbourhood intersection           810
|N_new(S_old)|                                   1322
|N_old(S_new)|                                   1306.
```

Hence the shuffle201 outer resource shuffle crosses the old Hall cut:
`1322>=1206`.  Conversely the old graph also has no deficit on the new
tail.  The obstruction is not a fixed set of bad packets; changing the
outer resource assignment replaces the transition graph and exposes a new
cut.  The exact master must therefore impose the complete separated family
(3.2), not maximize one shore, raw turn count, zero degrees, or ownerwise
coverage.

## 6. Exact support-two positive calibration

The first selected binary circuit already shows why the outer type must be
part of the chronology move.  At roots 199 and 1428 its old rows are

```text
199:  Q=3033,  type1, A=16,   B=2777, C2=256
1428: Q=21843, type5, A=5392, B=5459, C2=16384,
```

and its new rows are

```text
199:  type5, A=2696, B=2777, C2=256
1428: type1, A=1,    B=5459, C2=16384.
```

The roots and `B` targets are unchanged.  The types are exchanged.  The two
rank-four sets `5392` and `2696` have the same necklace representative 337,
while rank-one `16 -> 1` is slack.  Hence this is a literal support-two
resource circuit.  Full transition replay changes

```text
turns / matching / zero-out / zero-in
970 / 556 / 723 / 826  ->  976 / 560 / 719 / 821.
```

Thus one bounded outer-type circuit can gain four matching units.  This is
not claimed to discharge either canonical Hall shore by itself; matching
gain and a specified shore's crossing count are different quantities.

The complete literal option and small-circuit enumeration around shuffle201
contains

```text
literal row options                              2722720
support-one resource moves                          2541
support-two resource moves                        213714.
```

An exact reverse-tie multipass greedy procedure outputs 449 pairwise
root-disjoint moves: 42 unary and 407 binary.  Their output has the exact
type and common target ledger (1.4).  An independent selector verifier
reconstructs every circuit from the authenticated source and reproduces the
final row table.  A separate independent literal replay gives 1855 packet
turns, matching 954, and zero counts
`234/445`.  Thus bounded circuits have substantial transition mobility and
give a rigorous improved factor, but this particular independently chosen
bank does not solve the Hall system.  In particular, the independently
rebuilt graph asking one attachment owner to be simultaneously live on both
sides has maximum matching 718.  This number is a necessary projection of
Theorem 2.2, not a substitute for its common-state circulation.

The construction is not evidence for independent-circuit convergence.  It
is catalogue-order maximal only for its stated greedy rule.  To be proof
complete, the same catalogue must be selected through (3.2), or directly
through the synchronized circulation (2.2).

## 7. Frozen artifacts

```text
scratch/h2_k17_rooted_flag_direct_row_shuffle201_20260801.audit.json
  SHA256 a503c6e4092493f9cad37d1485e3572a594cd65e9691f8cf25985370bac9a714

scratch/audit_r_k17_shuffle201_fixed_Borbit_global_A_union_20260801.cpp
  SHA256 e2baecbf0cf7a201526c7f04d8be3ee2665025f61aeb5ce86cee93f93f984630
scratch/k17_shuffle201_fixed_Borbit_global_A_union_20260801.audit.json
  SHA256 7881c5c5b07b908d25346821ffb79481eb3d6323b65ed875b3d08483279c9046
scratch/k17_shuffle201_fixed_Borbit_global_A_union_20260801.edges.tsv
  SHA256 73d58a2b132a5edfdf1bb4a6a754c23091c365ec0ff054100bd8ea8dd7b8cf3e

scratch/audit_r_k17_shuffle201_fixed_Borbit_comparison_20260801.py
  SHA256 aa76de5c3e491a70d3d03caa754a8284a284d1b6bf822ac53166f6a82616e81e
scratch/k17_shuffle201_fixed_Borbit_comparison_20260801.audit.json
  SHA256 e2b88f58c8c3ec39afa485e2b0746ed0eeee86b569fbca3e82780cde9f79ce8c

scratch/threadA_k17_rooted_global_support2_shuffle201_h100_20260801/
  shuffle201_reverse.candidate.tsv
    SHA256 e28a8ee5825564baf0d75720d8f3c1a53a911e9c53956aff49ed2460fd08c8dd
  shuffle201_reverse.moves.tsv
    SHA256 47b5017e4605d996657590a198fbf091b3090f5235cd75910f7b1e7cc4f4f7b3
  shuffle201_reverse.audit.json
    SHA256 2e45e0893199ca046c8dd351a1572494ed26185e9641a50c1e83cbe90a1459b2
  shuffle201_reverse.independent.audit.json
    SHA256 264ba804b98b96a216b9087a948f5e74c305f13f3be2d07270ccdd3d94e752a0
  reverse.owner.audit.json
    SHA256 b332ccc08662e3931d7e6afe59f945ce8e49df32f95311c7315b1b0c64b80e3d

scratch/laneK_k17_rooted_flag_catalogue_bind_20260801/
  shuffle201_reverse.selector_manifest.json
    SHA256 201858729a415b1a17217d9af7d34e5f606f03b41209b11bfdd94ddf8e3e4144
  shuffle201_reverse.selected_circuits.tsv
    SHA256 76141e89195968a3438b0ab5707308693f9dda41a119c7ede0951135a59fd191
  shuffle201_reverse.selector.independent.audit.json
    SHA256 a5ada1febde2daaa621bac54b0722a7429672d03b56c8aa4de20900b26d681e2
  shuffle201_reverse.owner_demand.independent.audit.json
    SHA256 c87add18cfe9da003fa63e222946bf71366e81fdcd7ccf35d34cb3539c0399fe

scratch/verify_k17_disjoint_support2_selector_20260801.cpp
  SHA256 0d0f68bc3524579b940f8797a7dacc2dd531d7417f132c92ffbf09ee906e7d23
```

The fixed-face audit is a relaxation and supplies a rigorous obstruction.
The multipass candidate is an exact static lower-resource factor and its
literal transition graph is independently replayed.  Neither artifact
asserts a simultaneous root/owner state transversal, one physical cycle,
upper-shadow support, source chronology, residence outside the rooted age
recurrence, opening, or common-cap compiler.

## 8. Exact remaining gate

The next finite gate is first the feasibility of the collapsed circulation
(2.2), and then the full attachment-state circulation (2.5), under a column
family larger than the fixed `B`-orbit face.  The support-two catalogue is a
legitimate first column bank, but it must be optimized jointly with all
separated Hall cuts.  A collapsed packet matching of 1430 would close only
the packet-root support gate; literal occurrence-owner chronology would
still require (2.5), and all physical and compiler obligations listed above
would remain.
