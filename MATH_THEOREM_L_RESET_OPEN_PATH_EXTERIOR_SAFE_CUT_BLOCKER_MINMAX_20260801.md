# Exterior safe cuts in the global-reversal quotient: exact blocker min--max

**Date:** 2026-08-01  
**Lane:** L, complete-reversal exterior upper deck  
**Status:** exact arbitrary-width interval-OR theorem, exact compensation
min--max for the bare all-cut payload, and exact integration of the canonical
`d`-overlap/Ferrers twin-bank payment.  The bare opening has quadratic debt,
but the protected local module now pays it with `O(d)` reserved owner
positions and no source positions beyond the necessary `M+d`.  The remaining
blocker problem concerns exterior all-width targets and global embedding.
Global reversal removes the need for a fixed-address cross-phase compiler;
one-oriented residence, compilation and cap feasibility remain separate.

## 0. Inputs and conclusion

The following five frozen results are the relevant inputs.

1. `MATH_THEOREM_RESET_OPEN_PATH_PHASE_COMMON_Q1_HOST_20260801.md`
   embeds the opened `4d+2`-root reset path as one common undirected path in
   a spanning middle-levels two-factor for `m>=8d+4`.  Here the reset packet
   is specialized to `r=m`, `k=2m-1`; this threshold implies the packet's
   coordinate-supply hypotheses.
2. `MATH_THEOREM_AD_RESET_RETURN_RAIL_LINEAR_OPENING_AND_WHOLE_COPY_FUSION_20260801.md`
   proves that the two packet phases are realized by reversing the whole
   containing component, and gives the exact prefix/suffix crossing current
   against a fixed exterior.
3. `MATH_THEOREM_RESET_RETURN_RAIL_LINEARIZATION_COLLATERAL_20260801.md`
   proves a separate quadratic cut debt in the maximal source antecedent.
   That is a source/compiler-row statement and is not silently identified
   with the owner-word upper statement proved here.
4. `MATH_THEOREM_GLOBAL_REVERSAL_QUOTIENT_INDUCTION_AND_RELATIVE_PHASE_OBSTRUCTION_20260801.md`
   proves that one complete oriented child state--source, witnesses,
   compiler, caps, endpoint data and sidecar--may be reflected as a whole.
   Thus a reversal-closed existential induction needs one oriented
   certificate, not a fixed-address certificate in both phases.
5. `MATH_THEOREM_RESET_RETURN_DOVERLAP_AND_UPPER_FERRERS_TWIN_BANK_20260801.md`
   proves that the canonical `d`-overlap has exactly two upper Ferrers
   triangles as its leave and gives explicit `2d`- and `3d`-owner Johnson
   banks covering every member of that leave.

Let `P` be the protected opened packet path and let `C` be the two-factor
component containing it.  After projecting away the alternating lower
vertices, `C` is an undirected Johnson cycle of rank-`m` owner roots.  Let
`R` be the complementary owner path between the endpoints of `P`.

Fix a nonempty bank `K` of allowed cut gaps on `R`.  All q1, topology and
endpoint restrictions on a legal cut must already have been used to define
`K`.  For a bank `T` of old arbitrary-width target masks, consider all old
cyclic witness arcs which avoid the interior of `P`.

The exact answer is:

\[
 \boxed{
 b^*=\min_{c\in K}\#\{S\in T:c\in B_S\},
 }
 \tag{0.1}
\]

where `B_S` is the intersection of the internal-gap sets of all
packet-avoiding witnesses of `S`.  A target with no such witness has
`B_S=K`.  Thus a cut/orientation with at most `b` unsupported old targets
exists if and only if `b^*<=b`.

Orientation does not occur in (0.1).  Global reflection sends an allowed
cut `c`, its blocker family, and every surviving witness arc to their
reflected copies with the same OR.  One may therefore solve (0.1) in one
oriented complete child and reflect the result.  Orientation remains real
for a named one-sided socket or for relative phases of several components,
but not for this globally reflected arbitrary-width witness row.

In particular, `[H0]=[H3]` and `[H1]=[H2]` in the reversal quotient.  The
one-attachment/two-predecessor returns are unnecessary merely to compare the
two representatives; they remain physical data if they attach the selected
oriented child.

Consequently, even the stronger phase-common q1 host does **not** imply
`b^*=O(1)`.
A proof-safe positive `O(1)` theorem requires exactly an exterior witness
dispersion hypothesis.  One convenient sharp scalar form is

\[
                    \sum_{S\in T}|B_S|=O(|K|).             \tag{0.2}
\]

Under (0.2), averaging gives `b^*=O(1)`.  No residence or compiler
conclusion is bundled into this statement.

For the packet-internal source deck, the current conclusion is stronger:
the canonical overlap plus protected twin banks has zero local leave.  Thus
the bare-cut optimum of Section 5 remains an exact obstruction theorem for
an unprotected opening, but it is no longer the live construction target.

## 1. Cyclic witnesses and their blocker cores

A proper cyclic owner interval `J` in a factor component has two boundary
gaps.  Write

\[
 g(J)=\{\text{cycle gaps strictly internal to }J\}.        \tag{1.1}
\]

Cutting at `c` leaves `J` as a contiguous interval if and only if
`c notin g(J)`.  A whole-component interval is never endangered, so by
convention it has `g(J)=emptyset`.

An interval is **packet-avoiding** if it uses no edge of `P` and no internal
root of `P`; either common endpoint may be used.  Intervals on other factor
components are automatically packet-avoiding.  Let

\[
                         W_S^{ext}                         \tag{1.2}
\]

be the complete bank of old packet-avoiding cyclic witness intervals whose
owner union is `S`.  An old witness on a component which is not being cut,
or a whole-component witness, may be represented by an interval with empty
gap set.

Define the **mandatory-cut core**

\[
 B_S=
 \begin{cases}
 K\cap\displaystyle\bigcap_{J\in W_S^{ext}}g(J),
       &W_S^{ext}\ne\varnothing,\\[2mm]
 K,    &W_S^{ext}=\varnothing.
 \end{cases}                                               \tag{1.3}
\]

Thus `c in B_S` means that every old packet-avoiding witness of `S` is
split by the cut.  If only a named subbank of witnesses is used in (1.3),
the resulting core gives a sufficient casualty bound; it is exact when the
bank is complete.

Because all witnesses lying in `R` are ordinary intervals in one linear
order, every nonempty `B_S` is itself an interval of cut gaps when `K` is a
contiguous subpath.  This convexity is useful algorithmically but is not
needed for the theorem.

## 2. Exact one-component min--max

### Theorem 2.1 (exterior safe-cut blocker theorem)

For `c in K`, put

\[
                         D(c)=\#\{S\in T:c\in B_S\}.       \tag{2.1}
\]

Open `C` at `c` in one oriented complete child.  Exactly `D(c)` targets in
`T` have no surviving old packet-avoiding witness.  Reflecting the complete
child maps `c` and all its witness addresses bijectively to the opposite
representative and leaves the count unchanged.  Hence the least casualty
count on the reversal orbit is (0.1).

In particular, a cut losing at most `b` targets exists if and only if

\[
 K\not\subseteq
 \bigcup_{A\in {T\choose b+1}}\ \bigcap_{S\in A}B_S.      \tag{2.2}
\]

For `b=0`, this is the usual forbidden-cut formula
`K not subset union_S B_S`.

#### Proof

A witness `J` survives the opening precisely when `c notin g(J)`.  Thus all
packet-avoiding witnesses of `S` are lost precisely when `c` lies in their
intersection (1.3).  Global reflection replaces every surviving interval
by its reflected arc and `c` by the reflected cut; neither the union nor the
casualty indicator changes.  Summing the indicators proves (2.1) and
(0.1).

A point `c` belongs to the right side of (2.2) exactly when it belongs to at
least `b+1` blocker cores, equivalently when `D(c)>=b+1`.  This proves
(2.2).  \(\square\)

The theorem is an exact min--max only for the promised witness type.  A
target counted as a casualty may be recreated by a new boundary-crossing
interval; that can only improve the final word and is not assumed here.

### Corollary 2.2 (sharp average blocker bound)

There is a cut `c in K` with

\[
 D(c)\le
 \left\lfloor {1\over |K|}\sum_{S\in T}|B_S|\right\rfloor. \tag{2.3}
\]

#### Proof

Double-count incidences `(c,S)` with `c in B_S`:

\[
 {1\over|K|}\sum_{c\in K}D(c)
   ={1\over|K|}\sum_{S\in T}|B_S|.                       \tag{2.4}
\]

At least one cut has load no larger than the average. \(\square\)

The scalar implication is sharp using only the core sizes: a regular family
of blocker sets has constant load equal to the average.

### Corollary 2.3 (density-matched `O(1)` exterior cut)

Suppose `T=E dotunion G`, where

\[
 |E|\le h,\qquad |G|\le a|K|,\qquad |B_S|\le q
       \quad(S\in G).                                     \tag{2.5}
\]

Then some common cut preserves a packet-avoiding old witness for all but at
most

\[
                              h+\lfloor aq\rfloor          \tag{2.6}
\]

targets.  In particular, fixed `a,q,h` give an `O(1)` exterior upper debt.

The load parameter is the size of the **intersection core** `B_S`, not the
length of one witness.  Long witnesses are harmless when their compulsory
gap intersection is short.

### Corollary 2.4 (two-disjoint-witness certificate)

If all but `h` targets have two packet-avoiding witnesses `J_1,J_2` with

\[
                         g(J_1)\cap g(J_2)\cap K=\varnothing, \tag{2.7}
\]

then every allowed cut loses at most `h` targets.  Witnesses on two
different factor components satisfy (2.7) automatically.

This is the cleanest coefficient-one protected-witness interface: it needs
no choice of orientation and no probabilistic argument.

## 3. Several factor components

The preceding statement extends without loss when several factor
components are opened.  Let component `i` have a nonempty allowed cut bank
`K_i`.  For each target `S`, let

\[
 B_{S,i}=K_i\cap\bigcap_{J\in W_{S,i}^{ext}}g(J)           \tag{3.1}
\]

on every component carrying at least one old packet-avoiding witness of
`S`.  If a component has no witness of `S`, omit it from the product.  A
whole-component or cut-immune witness gives `B_{S,i}=emptyset` and makes
`S` automatically safe.

### Theorem 3.1 (product blocker min--max)

For one selected cut `c_i in K_i` per component, the exact casualty count is

\[
 D(c_1,\ldots,c_t)=
 \sum_{S\in T}
   \prod_{i:\,W_{S,i}^{ext}\ne\varnothing}
      {\bf1}_{\{c_i\in B_{S,i}\}},                       \tag{3.2}
\]

with an additional unit for every target having no packet-avoiding witness
on any component.  Therefore the optimum is the minimum of (3.2) over the
Cartesian product of cut banks.  Moreover, independent uniform cuts give

\[
 \min D\le
 \#\{S:W_S^{ext}=\varnothing\}
 +\sum_{S:W_S^{ext}\ne\varnothing}
   \prod_{i:\,W_{S,i}^{ext}\ne\varnothing}
       {|B_{S,i}|\over|K_i|}.                             \tag{3.3}
\]

#### Proof

A target loses all named exterior witnesses exactly when every component
carrying such a witness cuts all its local witnesses.  This is the product
indicator in (3.2).  Taking expectations under independent uniform cuts
gives the right side of (3.3), and some deterministic cut tuple does no
worse. \(\square\)

This product form is the precise benefit of placing duplicate witnesses on
different components.  It does not control the new join intervals created
when the opened components are concatenated.

## 4. Application to the phase-common reset host

The protected-factor theorem supplies the common undirected path `P` and a
spanning q1 two-factor.  It supplies none of the following data:

* a packet-avoiding witness for every old arbitrary-width target;
* a bound on `|B_S|` or on the total blocker mass;
* a long candidate cut bank on the component containing `P`; or
* a bounded number of components.

Therefore it does not imply (0.2), (2.5), or an `O(1)` exterior upper debt.
Choosing the other representative of the reversal orbit cannot fill this
logical gap.  The exact missing upper hypothesis is one of the equivalent
blocker conditions in Theorem 2.1, or a usable sufficient form such as
Corollary 2.3 or 2.4.

There are three exact interfaces.

1. **One-oriented host plus reflected certificate.**  First construct one
   completed linear chronology, including a cut and all witnesses.  Its
   global reversal transports every interval and every occurrence address.
   Therefore the opposite representative needs no fixed-address exterior or
   compiler intersection.  This removes a cross-phase compatibility gate;
   it does not create the witnesses lost while constructing the first
   oriented linear child.
2. **Dispersed duplicate exterior witnesses.**  If the old carrier gives
   (0.2), then one oriented cut leaves only `O(1)` arbitrary-width targets
   to be recreated.  If it gives the two-disjoint-witness condition outside an
   `O(1)` exceptional bank, every allowed cut works.
3. **Nonlinear cyclic contraction.**  If the containing component is kept
   cyclic, complete reversal preserves its entire cyclic interval deck.
   This postpones rather than pays the linearization cost: any later ordinary
   opening again has the blocker load of Theorem 2.1 and, on the source row,
   the payload of Theorem 5.1 unless an ambient or compensating witness bank
   has been installed by then.

The natural-cut computation in the linear-opening theorem shows why some
such hypothesis is real: against a one-sided private context the packet has
`3d+1` distinct prefix/suffix states.  That result is an exact fixed-cut
upper-deck warning, not an all-cut lower bound.

## 5. Exact compensation min--max for the item2566R payload

The source collateral theorem gives more than a warning, but on a different
row.  For each choice `s` of the common packet seam, let `L_s` be the
short-interval target family in the maximal antecedent whose unique cyclic
packet witnesses cross `s`.  Uniformly in `s`,

\[
 |L_s|=\sum_{w=2}^{2d}(w-1)=d(2d-1),                     \tag{5.1}
\]

and its rank histogram has `t` targets of rank `r-d+t`,
`1<=t<=2d-1`.  No member of `L_s` has another witness inside the cyclic
packet.

Suppose one prospective oriented **source chronology** and its complete
ambient witness bank have been specified.  The opposite quotient
representative receives the reflected chronology and witnesses
automatically; no witness is required at the same physical address in both
representatives.  Existence of this one-oriented ambient bank is additional
to the q1 host theorem.
For `T in L_s`, let `W_{s,T}^{amb}` be the complete bank of ambient source
intervals with OR `T` which avoid the opened packet, and define

\[
 B_{s,T}=
 \begin{cases}
 K_s\cap\displaystyle\bigcap_{J\in W_{s,T}^{amb}}g(J),
       &W_{s,T}^{amb}\ne\varnothing,\\[2mm]
 K_s,  &W_{s,T}^{amb}=\varnothing,
 \end{cases}                                               \tag{5.2}
\]

where `K_s` is the nonempty bank of globally admissible exterior cuts after
opening packet seam `s`.

### Theorem 5.1 (forced-payload compensation optimum)

For a fixed host chronology, the least number of item2566R targets left
without either their packet witness or a surviving ambient packet-avoiding
witness is exactly

\[
 \boxed{
 \beta^*=\min_s\ \min_{c\in K_s}
       \#\{T\in L_s:c\in B_{s,T}\}.}
                                                               \tag{5.3}
\]

Equivalently, seam `s` and exterior cut `c` leave at most `b` uncompensated
targets if and only if `c` lies in at most `b` of the cores
`{B_{s,T}:T in L_s}`.  In the absence of ambient compensation,

\[
                         \beta^*=d(2d-1).                  \tag{5.4}
\]

Hence neither packet-seam choice nor selection of the reflected
representative yields an unconditional `O(1)` source residual.  An `O(1)`
conclusion is **equivalent** to proving
that one admissible seam has an ambient compensation system whose blocker
depth has `O(1)` minimum.  The averaging bound

\[
 \min_{c\in K_s}\#\{T:c\in B_{s,T}\}
 \le {1\over|K_s|}\sum_{T\in L_s}|B_{s,T}|                \tag{5.5}
\]

is a conditional selector once such a system is constructed, not a claim
that the system exists.

#### Proof

Opening `s` destroys the unique internal packet witness of every member of
`L_s`.  Theorem 2.1, now applied to the ambient source witness banks, says
that `T` is externally compensated exactly when
`c notin B_{s,T}`.  Counting, then minimizing first over the exterior cut
and then over admissible packet seams, proves (5.3).  If all ambient banks
are empty, every core is all of `K_s`, giving (5.4).  Equation (5.5) is the
same incidence double count as Corollary 2.2. \(\square\)

Theorem 5.1 is the exact bare-opening min--max.  It does not turn the source
payload into an owner-word upper obstruction, and it does not assert that an
arbitrary q1 completion carries the one-oriented ambient source chronology
appearing in (5.2).  The next theorem supplies a concrete compensation bank.

## 6. The canonical `d`-overlap and twin banks make the local source debt zero

Let `A` be the cyclic packet antecedent and set

\[
 \widetilde A=(A_{M-d},\ldots,A_{M-1},A_0,\ldots,A_{M-1}). \tag{6.1}
\]

Assume four permanent marker coordinates and the private fillers needed by
the two one-sided residence collars.  Let `P_X` and `P_U` be the protected
`2d`- and `3d`-owner Ferrers banks from the frozen twin-bank theorem.

### Theorem 6.1 (exact local payment)

If `widetilde A`, `P_X`, `P_U` and their collars are retained as contiguous
protected pieces of one oriented chronology, with the final cut outside
their internal witness intervals, then:

1. `D^d widetilde A` consists of all `M=4d+2` packet owners exactly once;
   `widetilde A` uses exactly the necessary `M+d` source positions;
2. every target of rank at most `r` survives;
3. the exact remaining leave before adding the banks is

   \[
   \{Z^X_{i,j}:0\le i\le j<d\}\mathbin{\dot\cup}
   \{Z^U_{i,j}:0\le i\le j<d\},                           \tag{6.2}
   \]

   with `t` targets of rank `r+t` and `t` of rank `r+d+t`
   for every `1<=t<=d`, hence `d(d+1)` targets in total;
4. intervals of `P_X` and `P_U` witness every target in (6.2), so

   \[
   \operatorname{Deck}_{cyc}(A)\subseteq
   \operatorname{Deck}(\widetilde A)\cup
   \operatorname{Deck}(P_X)\cup\operatorname{Deck}(P_U); \tag{6.3}
   \]
5. the two raw banks use `5d` distinct owners and `5d-2` distinct colours
   on each q1 shore, all disjoint from the surviving opened-packet resources;
   their two collars raise the reserved-owner bank to at most `7d`;
6. all internal runs are depth-`d` resident, and the two collars close the
   only clipped boundary runs.

Consequently, for the canonical module the complete source-casualty family
has packet-avoiding protected witnesses and its updated optimum is

\[
                              \boxed{\beta_{can}=0}.       \tag{6.4}
\]

This does not change the bare-packet value `beta*` in (5.3)--(5.4).  The
overlap first changes the casualty family, and the bank witnesses then make
every residual blocker core empty.  Cut-immunity of those protected witness
arcs is part of the host hypothesis.

#### Proof

The coefficient-one overlap theorem gives items 1--3.  The two explicit
Johnson paths give one interval witness for every member of the two Ferrers
triangles; maximal erosion makes these literal source-interval witnesses,
proving (6.3)--(6.4).  The four-marker ledger proves owner/q1 disjointness,
and the run classification plus the two nested collars proves items 5--6.
\(\square\)

### Corollary 6.2 (exact exterior residual)

Delete from the old target bank every mask having a cut-immune witness
inside `widetilde A`, `P_X` or `P_U`, and call the remainder `T_ext`.  For
`S in T_ext`, form the complete exterior blocker core `B_S^{can}` as in
(1.3).  The exact remaining old-witness optimum is

\[
 b_{ext}^*=\min_{c\in K}
       \#\{S\in T_{ext}:c\in B_S^{can}\}.                 \tag{6.5}
\]

The twin-bank theorem gives no bound on (6.5).  Its targets are genuinely
ambient: exterior crossing profiles and old carrier witnesses endangered by
the eventual opening or joins.  New join-created witnesses may lower the
final debt, but must be certified in the one-oriented completed chronology.

At the owner/lower-q1 level, the opened packet plus the collared banks has
`22d-2` protected incidence edges and maximum degree two.  Hence the fixed
protected-subgraph extension theorem embeds it in a spanning q1 two-factor
when `m>=22d`.  This is only a marginal host theorem: it does not give upper
surjectivity, low component count, exterior arbitrary-width preservation or
the terminal compiler.

The phrase “zero appended letters” is local and exact: (6.1) uses no source
positions beyond the `M+d` forced by `M` depth-`d` owners.  The twin banks
must still be placed into `O(d)` reserved owner positions of the ambient
coefficient-one host.  Their existence does not itself construct that host.

## 7. Separation from residence and compilation

The safe-cut theorem proves only literal OR coverage of a specified target
bank.

* **Residence.**  Internal residence of the packet and raw twin banks is
  closed, and the two `d`-root one-sided collars close their clipped runs.
  The joins to the ambient host still require the actual endpoint-age
  inequalities in the chosen orientation.  Reflection swaps those records;
  it does not make an invalid join valid.
* **Source/antecedent deck.**  Theorem 5.1 is its exact bare compensation
  row; Theorem 6.1 supplies a concrete zero-leave payment.  The old
  `d(2d-1)` family cannot be used as a current global no-go.
* **Compiler/cap.**  Existence of an OR witness is not an occurrence-labelled
  target--cell matching.  In reversal-quotient induction, one oriented child
  needs one feasible compiler matching and one nonempty cap word; both are
  reflected addresswise to the opposite representative.  Hall in
  `G^+ intersection G^-` is required only for the stronger local-switch
  problem with a frozen exterior or a literal fixed-address certificate.
* **New joins.**  The theorem preserves old component-internal witnesses.
  It neither certifies nor needs any target created by the eventual joins.
  Likewise, the reset's three return paths disappear as a phase-comparison
  certificate, but remain required if they are the physical attachment used
  to construct the chosen oriented child.

Thus an exact additive terminal interface may use Theorem 2.1 for the
arbitrary-width upper row, the endpoint-age ledger for one-oriented
residence, and one oriented compiler/cap certificate.  Reflection transports
the completed tuple, but none of these rows may be inferred from either of
the others.

## 8. Proof-safe frontier

The strongest conclusion currently justified is

\[
 \boxed{
 \begin{array}{c}
 \text{one oriented host} + \text{exterior blocker mass }O(|K|)\\
 \Longrightarrow\text{ one oriented cut with }O(1)
 \text{ old arbitrary-width casualties.}\\
 \text{After oriented residual repair and compilation, the completed}\\
 \text{certificate reflects automatically in the quotient.}
 \end{array}}
 \tag{8.1}
\]

The local source debt is now paid by Theorem 6.1; there is no reason to
search for a luckier bare cut.  The live target is one oriented host which
embeds and joins the packet plus twin banks, completes the upper palette,
preserves the exterior arbitrary-width target bank governed by Theorem 2.1,
and admits one terminal compiler/cap.  The quotient removes the second
fixed-address proof obligation; it does not repair a hole or merge a
component.  A named one-sided socket must admit its reflected
socket, and `c` independently phased components retain `c-1` relative phase
bits when their labels are fixed individually.  If reflection permutes the
component labels, it still removes at most one simultaneous binary choice.
The still-open lower/root--head--graphic correlation is not touched by the
reversal quotient.  Nor can it be replaced by a degree-only rainbow
argument: the Wdowinski counterexamples rule out the required generic
`Delta+1` shortcut.  The Boolean fixed-`M0` equation linking each tail,
lower intersection and head remains essential; the corrected head theorem
closes only its disjoint second-facet projection.
