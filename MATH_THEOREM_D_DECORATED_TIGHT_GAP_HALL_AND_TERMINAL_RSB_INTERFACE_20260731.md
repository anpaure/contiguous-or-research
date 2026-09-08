# Decorated tight enumerations: exact gap--Hall gluing and the terminal RSB interface

Date: 2026-07-31  
Status: dependency-clean implication and recursive preservation theorem; exact
`K17` counter-calibration; no all-dimension decorated enumeration or optimal-word
construction is claimed

## 0. Verdict

The new parent-induced `K17` cycle closes the finite owner/lower-`q1` gate,
but it also fixes the logical scope of the direct SCD/tight-enumeration lane.

1. A **linear decorated tight enumeration** gives exactly the central
   Catalan object: every middle owner, every immediate lower colour, every
   immediate upper colour, and a spanning `Cat_m`-path forest.
2. It does not by itself give a single ordering of those paths, residence,
   deeper shadows, an opening, or a common-cap compiler.  The shortest
   honest word implication appends one correlated terminal RSB certificate
   on the same physical chronology.
3. Gap--Hall/interlacing *is* stable under a precise recursive gluing rule.
   With a fixed decoration, palette transparency and boundary alternation
   carry an explicit perfect matching of the new gap graph.  If lower
   representatives may change, the exact update is a vertex-capacitated
   alternating-path flow, not a scalar assertion that the glue is
   decorable.
4. The authenticated `K17` carrier, viewed as an `ML(17)` trace for the
   corresponding `K18` Catalan lift, is an ordinary central tight
   enumeration but not a decorated one: its two turn maps miss `1891` and
   `1623` colours.  As a `K17` chronology it therefore refutes the weaker
   shortcut

   \[
   \text{owner Hamiltonicity + exact lower }q1
   \Longrightarrow \text{turn decoration or terminal RSB},
   \]

   not any implication whose hypothesis is a genuine decorated tight
   enumeration.
5. Odd diamond lifting consumes exactly one unit of every old-coordinate
   run.  A regenerative node must therefore export parent run margin
   `d+2`, or an occurrence-labelled compensation bank hitting every
   length-`d+1` run and carrying its exact downstream effect.
6. That occurrence bank also decides inherited upper providers and macro
   endpoints.  The smallest lossless state is the labelled relation
   `(selector, upper multiplicities, surviving run packets, induced macro
   paths)`, chosen before the conditional port `b`-flow; separate marginal
   optimization is not sound.

Moreover, `605` length-three runs are sealed strictly inside the current
`1430` macros.  The stronger parent-level audit finds `165` length-three
patterns forced under **every** rank-six occurrence transversal, while the
exact simultaneous optimum is `180`.  An attaining transversal has `12`
surviving packets on each of the `15` old coordinates; the independently
verified bound-`179` DRAT proves that the coordinatewise floor `11` cannot
be attained simultaneously.  The extra `15` are therefore a
cross-coordinate integral-correlation tax, not fifteen further fixed
singletons and not automatically fifteen distinct actuators.  Thus no
permutation, reversal, new `b`-flow completion, or different occurrence
selection for this fixed parent can repair flat depth-three residence.  In
the unmodified occurrence-transversal/port-flow `A/X/Y` template this branch
is closed.  A continuation must instead supply one of the newly explicit
recursive exits: a different parent with the extra run unit, a cut/facet or
value-changing compensation bank hitting every critical packet, or a
genuinely nonflat compiler.

## 1. The central decorated object

Fix `m>=2`, put

\[
 \Omega=[2m-1],\qquad
 Q={2m-1\choose m-1}={2m-1\choose m},
 \qquad P={2m-1\choose m-2},
\]

and let `F` be a spanning two-factor of `ML(2m-1)`.  On one component write

\[
 A_0,B_0,A_1,B_1,\ldots,A_{s-1},B_{s-1},A_0,
 \qquad A_i\subset B_i\supset A_{i+1}.
 \tag{1.1}
\]

Its two turn maps are

\[
 \ell_i=A_i\cap A_{i+1}\in{\Omega\choose m-2},
 \qquad
 u_i=B_{i-1}\cup B_i\in{\Omega\choose m+1}.
 \tag{1.2}
\]

Choose occurrences `I` on the `A` shore which represent every upper turn
colour once.  The cyclic gaps between consecutive selected `A` occurrences,
taken componentwise, form a set `G_I` of size `P`.  Define the gap--colour
graph

\[
 \Gamma_I\subseteq G_I\times{\Omega\choose m-2},
 \qquad
 G\sim L
 \Longleftrightarrow
 \ell_j=L\text{ at some `B` occurrence in }G.
 \tag{1.3}
\]

A perfect matching `M` of `Gamma_I` chooses one lower turn *colour* for
every `I`-gap.  For every matched pair `(G,L)`, choose a literal occurrence
`j in G` with `ell_j=L`; call this occurrence realization `sigma`, and let
`J` be the resulting set of selected `B` occurrences.  Then exactly one
member of `J` lies in every `I`-gap, so the selected shore types alternate
on every marked component.  The matching is the exact gap--Hall certificate,
while `sigma` is indispensable for the physical mark trace.

Call `(F,I,M,sigma)`, equivalently `(F,I,J)`, **linear** when every marked
factor component contains an unmarked occurrence and its cyclic mark trace
is outside the unique cycle face

\[
 \text{every positive zero-run has length two and every one-run is odd}.
 \tag{1.4}
\]

Unmarked components use either residual cross-matching phase.  When `F` is
one Hamilton cycle, this is the linear decorated tight-enumeration subclass.
The factorwise definition is weaker and is sufficient for the theorem
below.

### Theorem 1.1 (the complete automatic consequence)

A linear decorated occurrence tuple `(F,I,M,sigma)` determines a perfect matching of the
Boolean diamond graph between ranks `m-1` and `m+1` of
`Omega union {infinity}`.  Its Johnson lift is a spanning linear forest on
the rank-`m` layer with exactly

\[
 {2m\choose m}-{2m\choose m-1}=\operatorname{Cat}_m
 \tag{1.5}
\]

path components.  Every rank-`(m-1)` intersection and every rank-`(m+1)`
union occurs exactly once among its edges.

#### Proof

The selected `A` turns use every upper colour avoiding `infinity` once, and
the selected `B` turns use every lower colour containing `infinity` once.
The pair `(M,sigma)` selects `J`.  Alternation leaves even residual paths on
every marked factor component, and their forced matchings supply the
remaining cross diamonds; an unmarked component uses its chosen residual
phase.  Thus every unselected lower and upper occurrence lies on exactly
one residual matching edge, and both shores of the diamond graph are used
exactly once.

The Johnson lift of one diamond `(L,U)` is the edge formed by the two
rank-`m` sets strictly between `L` and `U`; its intersection is `L` and its
union is `U`.  Therefore the two immediate palettes are exact.  The lift is
spanning because every rank-`m` owner is an occurrence of the middle-levels
factor.  Componentwise trace condition (1.4), together with the explicit
exclusion of wholly marked components, is exactly the assertion that the
maximum-degree-two lift has no cycle.  It has

\[
 W={2m\choose m}\quad\text{vertices},\qquad
 N={2m\choose m-1}\quad\text{edges},
\]

so Euler's identity gives `W-N=Cat_m` paths.  \(\square\)

This theorem is the exact contribution of a decorated tight enumeration to
the direct SCD/ordered-four-transversal lane.  No chronology, residence, or
compiler statement is hidden in it.

## 2. The shortest dependency-clean word implication

Theorem 1.1 itself lives in dimension `K=2m`, on
`Omega union {infinity}`, with `r=m`.  More generally, let a
`K`-dimensional direct construction independently supply a spanning central
forest; put `r=ceil(K/2)`, `W=binom(K,r)`, and let `d` be the deadline depth
in the exact lower bound `B(K)=W+d`.  Suppose either kind of central forest
is physically rethreaded and opened to a linear rank-`r` chronology

\[
                         T=(T_0,\ldots,T_{W-1}).
 \tag{2.1}
\]

The data below must refer to this *same* physical ordering, occurrence set,
and opening.

* `T` is a permutation of the middle layer.
* Every internal positive coordinate run satisfies depth-`d` residence,
  with only the two declared endpoint arms exempt.
* Every required upper target occurs as the union of one consecutive
  interval of `T`; arbitrary widths, rather than fixed-width proxies, are
  used.
* A chain-aligned staircase and its baseline maximal envelopes realize every
  scheduled row before capping.  The exact maximal-common-cap fibre is
  nonempty and contains one injective assignment of all lower targets to
  physical lower cells while preserving every middle/protected row.

Call these four fields, together with the opening and literal endpoint
identifiers, a **terminal R-certificate**.

### Theorem 2.1 (decorated-central plus terminal R implies the word)

If a central forest from Theorem 1.1, or a direct one-SCD
ordered-four-transversal forest, admits a terminal R-certificate, then the
maximal-common-cap construction produces a universal word of length `W+d`.
Wherever the deadline lower bound `nu(K)>=B(K)` has been proved, this gives
`nu(K)=B(K)`.

#### Proof

Residence and the exact compiler fibre produce a nonempty word `A` with

\[
                         D^dA=T,
 \tag{2.2}
\]

and cover every target below rank `r`.  Middle ownership is Condition 1.
For every `q>=1`, associativity and idempotence of union give

\[
 (D^qT)_i=T_i\cup\cdots\cup T_{i+q};
 \tag{2.3}
\]

the upper-service field therefore covers every target above rank `r`.
All three rank ranges are covered by literal intervals of the same `A`.
The construction has length `W+d`, proving the claim.  \(\square\)

Theorem 2.1 is deliberately conditional.  Replacing the terminal
R-certificate by the Cartesian product of four nonempty marginal
projections is invalid: the opening which repairs residence can destroy a
sole upper witness, and a marginal target--cell perfect matching need not
admit any common cap.  The smallest noncircular inductive invariant is thus

\[
 (\text{central decoration/forest},\ 
   \text{one correlated terminal R relation}),
 \tag{2.4}
\]

not a fixed SCD or a decorated tight enumeration alone.

## 3. Fixed-decoration gluing preserves gap--Hall exactly

Let `Z` be a Boolean incidence hexagon, and suppose toggling its two
alternating matchings carries a spanning middle-levels factor `F` to another
spanning factor

\[
                         F'=F\mathbin\triangle Z.
 \tag{3.1}
\]

Deleting the old hexagon matching cuts the affected factor components into
at most three retained fragments.  Orient those fragments as they are read
in `F'`.

### Theorem 3.1 (transparent fixed-decoration recursion)

Let `D=(I,J)` be a joint decoration of `F`.  The same selected occurrences
form a joint decoration of `F'` if and only if:

1. at the six hexagon vertices, the selected turn-colour multisets agree
   before and after, separately on the two shores; and
2. after fragments with no selected occurrence are discarded, the last
   selected shore type on each retained fragment is opposite to the first
   selected shore type on the next fragment of every output component.

Whenever these conditions hold, the exact gap--Hall inequalities for `F'`
hold without a separate Hall check.

#### Proof

Only neighbour pairs at the six hexagon vertices change, so Condition 1 is
necessary and sufficient for the two globally bijective selected palettes
to survive.  Reversal preserves alternation inside each retained fragment;
the only new possible equal-type adjacencies are the new seams.  Condition 2
is therefore necessary and sufficient for componentwise alternation.

Now traverse one output component between consecutive selected `I`
occurrences.  Alternation puts exactly one selected `J` occurrence in that
gap.  Assign to the gap the lower colour represented by that occurrence.
Every gap receives one colour, and global lower bijectivity uses every
colour once.  This is an explicit perfect matching of the new gap--colour
graph.  Hence all its Hall cuts, and equivalently the cyclic discrepancy-one
interlacing inequalities, hold.  \(\square\)

Linearity is an additional exact row.  An unmarked output component is
accepted by its residual cross phase; a wholly marked component is rejected;
and a partially marked component must contain an unmarked occurrence and
remain outside (1.4), or retain a protected literal trace breaker proving
that fact.  This full three-case predicate is not implied by palette
transparency.

### Corollary 3.2 (recursive gluing tree)

A dynamically tested sequence of valid toggles satisfying Theorem 3.1 at
every step preserves one joint alternating SDR and its exact gap--Hall
matching.  If the toggles merge a component tree, the endpoint is a linear
decorated Hamilton cycle once the full three-case trace row above passes.
If they do not merge all components, the weaker accepting decorated
two-factor already implies Theorem 1.1; Hamiltonicity is unnecessary for
the central conclusion.

The proof is induction.  The selected `J` occurrences furnish the next
step's gap matching explicitly, so there is no accumulation of unverified
Hall inequalities.

## 4. Exact reoptimization when a fixed decoration is too rigid

Theorem 3.1 freezes both representative sets.  There is a weaker exact
transfer which fixes the upper transversal but permits the lower
representatives to move.

Let `Gamma` and `Gamma'` be the old and new gap--colour graphs for the same
upper occurrence set `I`, after checking that `I` is still an upper-turn
transversal.  Gaps carry occurrence-labelled interval identities; a changed
gap is treated as a new vertex.  Let `M` be an old perfect matching and put

\[
 M_0=M\cap E(\Gamma'),
 \tag{4.1}
\]

where only literally persistent gap vertices are identified.  Let `X` be
the unmatched new gap vertices and `Y` the unmatched lower-colour vertices.
They have the same cardinality.

Orient every edge of `Gamma'` outside `M_0` from gap to colour and every
edge of `M_0` from colour to gap.  Split vertices to capacity one, attach a
source to `X` and `Y` to a sink, and call the resulting network `A(M_0)`.

### Theorem 4.1 (matching-repair gluing criterion)

The new gap graph `Gamma'` has a perfect matching if and only if

\[
       \operatorname{maxflow} A(M_0)=|X|=|Y|.
 \tag{4.2}
\]

Thus (4.2), together with upper-palette preservation, is an exact
representative-changing gluing rule for gap--Hall and interlacing.

#### Proof

A value-`|X|` integral flow is a family of pairwise vertex-disjoint
`M_0`-alternating paths from the unmatched gaps to the unmatched colours.
Toggling membership along those paths augments `M_0` to a perfect matching
of `Gamma'`.

Conversely, let `M'` be a perfect matching of `Gamma'`.  The symmetric
difference \(M'\mathbin\triangle M_0\) is a disjoint union of alternating
cycles and alternating paths.  Every unmatched vertex of `M_0` is an
endpoint of one path; discard the cycles and orient the paths from `X` to
`Y`.  They give a value-`|X|` flow in `A(M_0)`.  \(\square\)

The flow chooses colours, not their literal occurrences.  If a matched
colour occurs more than once in its gap, different realizations `sigma'`
can have different traces.  Therefore linearity requires an
occurrence-labelled refinement of the flow, or an existentially correlated
choice of `sigma'` followed by the full trace predicate.  The colour flow
alone makes no residence or trace claim.

The flow may also travel through the whole old gap graph, so Theorem 4.1 is
not by itself a bounded-width recursion.  The exact recursive object is the
relation of feasible boundary tuples `(I,M,sigma,trace-state)`, composed by
natural join and existential projection.  Privacy, laminarity, or a
leaf-peelable forest may compress this relation, but cannot be silently
assumed.

This relational qualification is necessary.  In the audited `ML(7)`
fixture, two vertex-disjoint toggles have nonempty adjacent
common-decoration sets (of sizes `576` and `1620`) while the three-way
intersection is empty.  Therefore a Boolean label saying “this glue is
transparent for some decoration” is not compositional.

## 5. The authenticated `K17` cycle as a test case

Let

```text
scratch/k17_parent_induced_macro_port_cycle_20260731.cycle
SHA-256 39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
```

be the new carrier, and write its rank-nine owners cyclically as `O_i`.
Put

\[
                         A_i=O_{i-1}\cap O_i.
 \tag{5.1}
\]

The `A_i` enumerate all rank-eight sets.  Therefore

\[
 A_i,O_i,A_{i+1},O_{i+1},\ldots
 \tag{5.2}
\]

is a Hamilton cycle of `ML(17)`, equivalently an ordinary tight enumeration
of the equal central levels.  Viewing this `ML(17)` cycle as a possible
decorated trace would produce a central forest in dimension `18`, not `17`.
Its two decoration turn maps are

\[
 u_i=O_{i-1}\cup O_i,
 \qquad
 \ell_i=A_i\cap A_{i+1}
       =O_{i-1}\cap O_i\cap O_{i+1}.
 \tag{5.3}
\]

The exact images have sizes

\[
 |\operatorname{im}u|=17557,
 \qquad
 |\operatorname{im}\ell|=17825,
 \qquad
 {17\choose10}={17\choose7}=19448.
 \tag{5.4}
\]

Thus the fixed cycle misses `1891` upper and `1623` lower turn colours.
Neither turn transversal exists, so the gap--Hall problem fails before its
matching layer and this fixed `ML(17)` trace supports no decorated-cycle
ordered-four-transversal for the `K18` Catalan lift.  This scope is exact:
it does not exclude another factor, an alternating-circuit rethread, or a
direct non-trace four-transversal.  As a `K17` object, the same file is only
a flat rank-nine chronology with exact lower-`q1` intersections.

The same literal audit gives

\[
\begin{array}{c|c}
\text{row}&\text{defect}\ \hline
\text{lower }q=2,3&1623,1013\\
\text{upper ranks }10,11,12,13&1891,910,128,3\\
\text{positive runs of lengths }2,3&1063,1829.
\end{array}
 \tag{5.5}
\]

The best single opening leaves `2889` internal short runs.  More strongly,
the fixed-macro audit identifies `605` length-three runs whose four support
edges lie strictly inside one macro.  They survive every macro permutation,
macro reversal, and replacement of the integral port `b`-flow.

This fixed-macro statement has now been strengthened to the whole
occurrence-transversal fibre.  Write

\[
 C_i=T_i\cap T_{i+1}
 \tag{5.6}
\]

on the two old parent cycles.  An internal `A`-shore length-three run for
an old coordinate `x` is a cyclic pattern

\[
 x\notin C_{i-1},\quad
 x\in C_i\cap C_{i+1}\cap C_{i+2},\quad
 x\notin C_{i+3}.
 \tag{5.7}
\]

It survives exactly when the four physical rank-six-coloured edges
`i-1,i,i+1,i+2` are retained.  There are `1425` such patterns, `95` for
each old coordinate.  In `165` patterns all four rank-six colours have a
unique physical occurrence.  Hence all four edges are forced under every
transversal; the distribution is exactly `11` forced patterns for each of
the fifteen old coordinates.

Equivalently, the exact occurrence CNF has one choice of occurrence for
each rank-six colour and one negative clause for every pattern (5.7).  A
unique-colour edge contributes no variable.  The `165` forced patterns
therefore become `165` literal empty clauses.  This is a solver-free
certificate that **no** rank-six occurrence transversal of this fixed
parent gives flat depth-three-resident macros.  Occurrence selection and
port flow are both closed as residence repairs in this literal `A/X/Y`
template.  A flat repair on the same parent must leave that template and
provide a certified cut/facet/value-changing compensation bank; alternatively
one may change the parent chronology or use a nonflat compiler.

The empty clauses do not give the sharp numerical debt.  If `v_R` is the
indicator that all four retained edges of packet `R` survive, then the exact
coupled occurrence problem is

\[
 \min\left\{\sum_R v_R:
   \text{one physical occurrence is selected for every rank-six colour}
\right\}=180.                                      \tag{5.8}
\]

For each fixed old coordinate the restricted minimum is `11`; one witness
transports to every coordinate by cyclic rotation of the frozen parent.
There is, however, no single occurrence transversal attaining those fifteen
restricted minima at once.

The upper bound is a literal transversal whose independently reconstructed
`1430` macro paths contain `180` internal short runs, with profile `12` on
each old coordinate.  For the lower bound, the `165` empty-clause packets
are fixed and a sequential counter asks whether at most `14` of the other
`1260` packets survive.  The resulting bound-`179` CNF is UNSAT; its retained
DRAT proof is independently verified with a `5531`-clause core and `99145`
resolution steps.  Thus the gap `180-165=15` is caused by the shared
one-occurrence-per-colour choices.  It must not be read as fifteen additional
packets that are individually forced, nor as a lower bound of `180` on the
size of a future cut/facet actuator bank, since one actuator can hit several
packets.  Nor may an induction retain only the scalar `180`: it must retain
the occurrence-labelled residual packet family and the exact effects of the
actuators chosen against it.

The upper-rank-ten holes split by new-coordinate tag

\[
                 \text{none}/Y/X/XY=618/623/650/0.
 \tag{5.9}
\]

This is not a capacity no-go for a different port-turn covering; it is
separate from the sealed residence obstruction.  Finally, only `78/1430`
current macro port pairs are Johnson pairs.  The successful unrestricted
`b`-flow is therefore outside the complement-dual/coupled-tight sufficient
subclass.

Consequently the new carrier closes precisely

\[
             \text{middle ownership + immediate lower palette},
 \tag{5.10}
\]

not the decoration or terminal R-certificate.

## 6. The one-unit residence tax and the amended recursive state

The gap--Hall state is not by itself regenerative under an odd diamond
lift.  Let

\[
 T_0,T_1,\ldots,T_{s-1},T_0
 \tag{6.1}
\]

be a cyclic Johnson component and put

\[
                         C_i=T_i\cap T_{i+1}.
 \tag{6.2}
\]

### Theorem 6.1 (exact one-unit residence tax)

For every coordinate `x` whose cyclic indicator on a component is
nonconstant, every positive cyclic run of length `ell>=2` in `T` becomes a
positive run of length exactly `ell-1` in `C`; a length-one run disappears,
and every positive `C`-run arises uniquely in this way.  An all-zero trace
stays all zero, while an all-one trace stays all one and pays no unit loss.
Consequently a flat child
compiler of depth `d`, which needs internal run length at least `d+1`, has
automatically safe unmodified `A`-shore macro interiors when the parent
exports minimum proper-run length at least `d+2`.  New connector collars
remain a separate part of the terminal residence check.

#### Proof

Write `b_i=1` when `x in T_i`.  The indicator of `x in C_i` is

\[
                         b_i b_{i+1}.
 \tag{6.3}
\]

A proper cyclic block of `ell` consecutive ones in `b` has exactly `ell-1`
consecutive adjacent pairs `11`, bordered by pairs containing a zero.
Conversely every proper run of adjacent `11` pairs has one unique parent
block of ones.  The two constant traces give the two stated exceptions.
The `A`-shore owner `C_i union {u,v}` has the same old-coordinate indicator
as `C_i`, proving the claim.  \(\square\)

The theorem gives an exact dichotomy for the recursive state.

1. **Margin state.**  Export the stronger proper-run certificate

   \[
              \min\operatorname{proper\mbox{-}run}(T)\ge d+2.
   \tag{6.4}
   \]

2. **Compensated state.**  Export every occurrence-labelled proper parent
   run of length `d+1`, together with an explicit cut/facet/nonflat actuator
   bank which hits its `d+1` spanning trace edges and whose literal
   transition proves that the induced child word `0 1^d 0` is not left as
   an internal forbidden run.

More exactly, let `S` be the set of retained physical trace edges and, for
each minimum parent run `R`, let `P_R` be its closed packet of `d+1`
spanning trace edges.  Let `H` be the support of certified actuators which
really break or absorb such a packet.  The exact inherited-macro condition
is the simultaneous hitting system

\[
             P_R\cap\bigl((E\setminus S)\cup H\bigr)\ne\varnothing
             \qquad\text{for every }R.
 \tag{6.5}
\]

For `H=emptyset`, this says that a fixed occurrence transversal must omit at
least one spanning edge of every minimum run.  Pointwise statements that an
edge *can* be omitted are insufficient because all choices are coupled by
the one-occurrence-per-colour constraints.  Even (6.5) certifies only the
inherited `A`-shore macro interiors: later seams, other shores, new
coordinates, and actuator side effects remain in the terminal residence
relation.  Therefore a recursive compensation object must retain the
actuator's exact boundary run effect and join it with the same opening,
upper-witness, and common-cap relation used by the terminal R-certificate.

Equivalently, the residence coordinate exported by a recursive node is

\[
 \mathcal E_d=
 \left\{
 \begin{array}{ll}
  \textsf{margin},&\min\operatorname{proper\mbox{-}run}(T)\ge d+2,\\
  (S,\mathcal K,\Delta_{\mathcal K}),&
    \mathcal K\text{ hits every length-}(d+1)\text{ run and }
    \Delta_{\mathcal K}\text{ is its exact run transition.}
 \end{array}
 \right.
 \tag{6.6}
\]

### Proposition 6.2 (occurrence coherence before `b`-flow)

The same occurrence transversal `S` also controls inherited upper service
and the macro endpoints seen by the later port flow.  Put

\[
 Z_i=(T_i\cap T_{i+1})\cap(T_{i+1}\cap T_{i+2}),
 \qquad U_i=T_i\cup T_{i+1},
\]

and, for one depth-two fibre `Z`, let `u_Z` be the number of its physical
occurrences whose parent upper union `U_i` occurs nowhere else.  Since `S`
retains exactly one occurrence in each `Z`-fibre, its exact deleted-provider
ledger is

\[
 D_{\rm up}(S)=
 \sum_Z\left(u_Z-\sum_{e\in E_Z^{\rm uniq}}\mathbf1[e\in S]\right)
 =\sum_Z(u_Z-1)^++\eta(S),
\]

where `eta(S)` counts positive-`u_Z` fibres in which `S` retains no unique
provider.  Consequently the exact marginal minimum is

\[
                         \sum_Z (u_Z-1)^+.
\]

Indeed, at most one such provider survives in a fibre, and retaining one
whenever `u_Z>0` attains the sum.  This is destroyed *internal-witness*
debt, not a final child-hole lower bound: a later port may recreate the
colour.

On the unactuated flat `A` shore, the residence objective on the same
selector is

\[
 D_{\rm res}(S)=
 \sum_{P\in\mathcal P_{\min}}
       \prod_{e\in P}\mathbf1[e\in S],
\]

and the selected endpoints give a literal port-demand vector
\(\mathcal D_{\rm port}(S)\).  Thus the actual occurrence master exposes
the triple

\[
             (D_{\rm res}(S),D_{\rm up}(S),\mathcal D_{\rm port}(S))
\]

for one common `S`; adding actuators augments this same state by their exact
packet and boundary transitions.

For lossless recursion the aggregates are still too coarse.  For every
labelled upper target `U` and minimum-run packet `R`, define

\[
 p_U(S)=\sum_{e:U_e=U}\mathbf1[e\in S],
 \qquad
 r_R(S)=\prod_{e\in P_R}\mathbf1[e\in S],
\]

and let `Pi(S)` be the induced labelled macro paths, endpoints, and port
demands.  The exact occurrence-coherence relation is

\[
 \mathcal O_T=
 \{(S,\mathbf p(S),\mathbf r(S),\Pi(S)):
      |S\cap E_Z|=1\text{ for every depth-two fibre }Z\}.
\]

Retaining `S` itself is safest.  A compressed state may identify two
selectors only when their full labelled
`(p,r,Pi)` data agree; equality of the scalar debts is insufficient.

Residence hyperclauses, provider rewards, and induced port demands use the
same variables.  They must therefore be optimized in one occurrence layer
before the endpoint `b`-flow.  Their marginal optima cannot be added and need
not occur at one common transversal.  \(\square\)

For the authenticated parent,

\[
 u_Z:0^{1835}1^{2685}2^{465}3^{20},
 \qquad \sum_Z(u_Z-1)^+=505.
\]

The octahedral `r2` parent has profile
`0^{1735}1^{2865}2^{405}`, hence unique-provider debt `405`, and its
separate exact residence optimum is `150` instead of `180`.  This is a
strictly better pair of marginals, not yet a joint occurrence/port/compiler
certificate.  The `150` value is imported from the occurrence-coherence
theorem's authenticated census; this note does not supply a separate frozen
lower-bound certificate for it.

The amended noncircular induction state is thus

\[
 \boxed{
 (\text{central factor/decoration},\
  (S,\mathbf p(S),\mathbf r(S),\Pi(S))\in\mathcal O_T,\
  \mathcal E_d,\
  \text{one correlated terminal R relation}).}
 \tag{6.7}
\]

This is one joint state, not a Cartesian product of residence, provider, and
port marginals.  Equivalently, occurrence selection and any
endpoint-changing actuator form the master, while the compatible `b`-flow is
occurrence-dependent recourse.

The alternatives in (6.6) are a disjunction inside one physical relation,
not independent scalar promises.  The compensation quantifier is

\[
 \exists\text{ one physical }(S,\mathcal K,\Delta_{\mathcal K},o,\ldots)
 \quad\forall R\quad\exists e\in P_R
 \text{ hit by that same realization},
 \tag{6.8}
\]

not a separate realization for every run.  A compensation set may share
edges between several minimum runs, and no count of bad runs is by itself a
lower bound on the number of required actuators.  For an opening-indexed
state, a cyclic packet may be omitted from the internal hitting obligation
only when the same protected opening certifies that it remains one of the
two exempt endpoint arms; otherwise its state stays exposed.

For the authenticated `K15` parent and `d=3`, every proper parent run has
length at least four, but there are exactly `1425` proper length-four runs.
The `165` unique-colour packets from Section 5 are forced under every
rank-six occurrence transversal, exactly eleven per old coordinate.  The
coupled optimum is nevertheless `180`: one optimum has profile `12^{15}`,
and no transversal with total debt at most `179` exists.  This is precisely
why the recursive state must retain one correlated occurrence realization;
fifteen coordinatewise choices cannot be pasted together.  Hence this
parent exports neither the margin state (6.4) nor a compensation state
implemented only by occurrence reselection and port flow.  A different
parent chronology must export run length at least five, or the same parent
must carry an actual cut/facet/value-changing compensation bank;
alternatively the child compiler must be nonflat.

This residence amendment is orthogonal to Theorems 3.1 and 4.1.  A gluing
step can preserve the joint turn SDR and every gap--Hall cut while spending
the one-unit residence margin.  Any recursive decorated/SCD construction
must therefore transport \(\mathcal E_d\) alongside its decoration relation.

## 7. Rebase of the direct SCD lane

A one-SCD construction which proves an injective acyclic central map, or a
fixed SCD pair which realizes an ordered four-transversal, enters this note
at Theorem 1.1.  It need not be converted into the stronger decorated
middle-levels trace form.  Conversely, an SCD chain partition does not
supply turn interlacing or any field of the terminal R-certificate merely
because its rank marginals are exact.

The finite `K17` owner/`q1` macro problem should therefore not be rebuilt by
SCD or complement-dual tight enumeration: the literal Hamilton carrier now
solves it.  Nor can the current fixed parent be rescued by changing its
rank-six occurrence transversal or its port flow; the exact minimum internal
debt is `180`, of which `165` packets form the solver-free fixed core.  This
closes only the unactuated retained-edge flat-residence fibre.  The useful
all-dimension SCD target is instead

\[
 \boxed{
 \text{one central ordered-four-transversal forest}
 \quad+\quad
 \text{one nonempty correlated terminal R relation on its lift}.}
 \tag{7.1}
\]

Within the stronger trace-recursive route, Theorems 3.1 and 4.1 identify the
exact missing induction: construct a gluing tree whose correlated
decoration/matching relation has a linear accepting root, then regenerate
or transport a terminal R relation.  Neither root nonemptiness is proved
here.  In particular no all-`K` equality claim follows from this note.

## 8. Authoritative dependencies and replay

The central equivalence and trace scope are taken from:

* `MATH_THEOREM_CATALAN_MIDDLE_LEVELS_TRACE_DECORATION_EQUIVALENCE_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORATED_TWO_FACTOR_MINIMAL_TRACE_TARGET_20260731.md`;
* `MATH_THEOREM_CATALAN_ALTERNATING_TURN_SDR_HALL_AND_M4_COUNTEREXAMPLE_20260731.md`;
* `MATH_THEOREM_CATALAN_DECORABLE_ML7_AND_HEXAGON_TRANSFER_20260731.md`;
* `MATH_THEOREM_CATALAN_FEASIBLE_DECORATION_RELATION_COMPOSITION_AND_ML7_OBSTRUCTION_20260731.md`;
* `MATH_THEOREM_CATALAN_TERMINAL_DECORATION_AND_RSB_JOINT_TRANSITION_20260731.md`;
* `MATH_SYNTHESIS_SHORTEST_ALLK_CHAIN_AND_EXACT_MISSING_THEOREM_20260731.md`;
* `MATH_THEOREM_ODD_DIAMOND_RESIDENCE_TAX_20260731.md`; and
* `MATH_THEOREM_ODD_DIAMOND_OCCURRENCE_COHERENCE_20260731.md`.

The finite calibration is taken from:

* `MATH_THEOREM_K17_PARENT_INDUCED_MACRO_PORT_HAMILTON_CYCLE_20260731.md`;
* `MATH_THEOREM_K17_FIXED_MACRO_RESIDENCE_OBSTRUCTION_20260731.md`;
* `scratch/k17_parent_induced_macro_port_cycle_20260731.audit.json`;
* `scratch/k17_parent_induced_macro_port_cycle_20260731.verify.json`;
* `scratch/k17_fixed_macro_residence_obstruction_20260731.audit.json`;
* `scratch/k17_macro_residence_20260731.cnf`;
* `scratch/k17_macro_residence_20260731.map.json`;
* `scratch/audit_k17_macro_residence_occurrence_transversal_independent_20260731.py`;
* `scratch/k17_macro_residence_occurrence_transversal_independent_20260731.audit.json`;
* `scratch/k17_macro_residence_optimal_20260731.json`;
* `scratch/verify_k17_macro_residence_optimum_20260731.py`;
* `scratch/k17_macro_residence_optimal_20260731.verify.json`;
* `scratch/k17_macro_residence_bound179_20260731.map.json`;
* `scratch/k17_macro_residence_bound179_20260731.cnf`;
* `scratch/k17_macro_residence_bound179_20260731.drat`;
* `scratch/k17_macro_residence_bound179_20260731.dratcheck.txt`; and
* `scratch/k15_octahedral_translation_descent_r2.factor.json`.

The independent carrier verifier, fixed-macro residence audit,
occurrence-transversal CNF builder, and separate occurrence audit were rerun
during this note's preparation.  The CNF/map replay was byte-identical and
contained the declared `165` empty clauses; the independent audit rebuilt
the `1425/165/11` pattern counts without importing the builder.  The optimum
witness replay independently reconstructed all `1430` macro paths and the
balanced `12^{15}` debt profile.  The retained bound-`179` proof log reports
`s VERIFIED`, a `5531`-clause core, `409` retained lemmas, and `99145`
resolution steps.  This note audits that log and the proof-package hashes;
it does not rerun the DRAT checker.  The older
fixed-macro audit JSON certifies only the first frozen macro bank;
its scope string still lists occurrence changes as open.  That sentence is
superseded by the parent-level theorem, CNF/map, and independent occurrence
audit listed here.  The current primary SHA-256 values are:

```text
cycle                              39cc3abe6a8991dc101a585123989deab863030060c00d3e0a2a60cd73252de6
carrier theorem                    4e7475659e309cbcae4c899994b0e7bab748edf04599ce723c930ca2413f703e
carrier primary audit              3f5a2fa4053604c34a2e1439a8f1506213296062571c7c5208dda9b6ba33204d
carrier independent replay         688b5c678e1ef5729af51a7b14b858b981571846194897399784397520fde96d
fixed-macro residence theorem      b8f303475a169f6ad07f24a44c3ffa5989bf728687f7b2fe9735c7adb90d81fd
odd-diamond residence-tax theorem  ff3ec04346f9f0d7adaedac548f61a863066df397a2d257a88b6df47015b8498
occurrence-coherence theorem       c2b0920221070de61ced078a30099e6dba8d421fd2de76070e16483456ace24e
fixed-macro residence audit        0c0079d71350b80c1af8ca6f20b130725a8d1ec529b0ca547bfcb1970204d38b
occurrence-transversal CNF          3c66f122f094c02afc140127c51710d0ef1c404dc604e15c898f69f7a4349764
occurrence-transversal map          1d16bf9453627528370cda64f71c4088f54c4bc8c0c2b23510f7e17ea905f224
independent occurrence audit        c20a3e781854f0866ff3d47448fcb9e35eb381fbfc4d31cb6578d32a21a4a806
optimum occurrence witness           8ecf43e13bfb7e0c204847f3c480dadc76af39dec979d245dc73bd5a5b5717b4
independent optimum replay           71ffd874fe520daf8609902cf2f12df181a55b1b38d3299633bb95c7e5e89a10
bound-179 map                        f5b4095a131ad77ebb0a6d95d62a4a94a66852dc2979180759001ac08ec05466
bound-179 CNF                        4cbf25a3f4d322c54ce91b068dc08e49223e86019d3dfccc51f065a3860cf19c
bound-179 DRAT                       8d55ea0215b62b43aaba7a94eda194555227ffdb0a73eb174d227afa0695c018
bound-179 verification log           78bd2f06aa9938999374176d676dec9337fcb61a231a3f7287bfb6468f25d465
octahedral r2 parent                  13c5ecaddc94bd4a240c9b2ce348f5db4508cb340658b2b0f4797b8c80472dfb
```
