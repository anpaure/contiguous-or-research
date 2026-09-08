# Exact `B` versus `B+1`: the zero-charge co-instantiation frontier

**Date:** 2026-08-03  
**Status:** proof-safe synthesis and conditional implications.  No new
unconditional upper bound is claimed.  In particular, the all-dimensional
statements `nu(k)=B(k)`, `nu(k)<=B(k)+1`, and `nu(k)<=B(k)+O(1)` remain open.

## 0. Verdict

The latest selector, lower-rounding, topology, all-width, diagonal-router,
and common-cap theorems fit into one short implication once their scopes are
kept literal.

The verified finite status remains

\[
                  \nu(k)=B(k)\qquad(0\le k\le16),
\]

with `k=17` the first unresolved dimension.

For a fully materialized terminal certificate `C` in dimension `k`, define

\[
                    \tau(C)=c(C)+R(\mathcal H(C)).       \tag{0.1}
\]

Here the scaffold has length `B(k)+c(C)`, `H(C)` is the complete set of
targets still absent after the final literal replay, and `R(H)` is the
minimum length of a repair word for `H`.  Then:

\[
\begin{array}{c|c}
\text{uniform terminal conclusion}&\text{required charge}\\ \hline
\nu(k)=B(k)&\tau=0,\\
\nu(k)\le B(k)+1&\tau\le1,\\
\nu(k)\le B(k)+O(1)&\sup_k\tau<\infty.
\end{array}                                               \tag{0.2}
\]

This exposes an important asymmetry between the two current branches.

* The monotone-pivot branch already spends its one unit on the inserted
  letter.  Therefore a `B+1` proof through this branch requires **zero
  terminal omission**.
* The exact-`B` branch has no physical slack at all.  It requires zero
  omission, zero structural zero, zero marginal router defect, and a genuine
  zero-charge opening.

An `O(1)` router defect is enough only for an additive-constant theorem.  It
does not prove either sharp statement.

After the new exact reductions, the strongest missing theorem for `B+1` is
one **Protected Pivot-Path Coinstantiation theorem**.  For exact `B`, within
the current diagonal/folded-ticket architecture, it is one **Protected
Converter-Cycle Coinstantiation theorem**.  Both are single-object existence
theorems: separate solutions of their lower, owner, upper, topology, and cap
projections do not compose.

## 1. The terminal-charge implication

### Theorem 1.1 (direct terminal charge)

Suppose that for every sufficiently large `k` there is one fully
materialized literal scaffold `Z_k` of length `B(k)+c_k` and one final replay
showing that exactly the targets in `H_k` are absent.  Then

\[
                       \nu(k)\le B(k)+c_k+R(H_k).       \tag{1.1}
\]

Consequently:

1. if `c_k+R(H_k)=0`, then `nu(k)=B(k)` by the general lower bound;
2. if `c_k+R(H_k)<=1`, then `nu(k)<=B(k)+1`;
3. if `sup_k(c_k+R(H_k))<infinity`, then `nu(k)<=B(k)+O(1)`.

#### Proof

Append a shortest repair word for `H_k` to `Z_k`.  Appending letters cannot
destroy an already existing interval witness, and the repair word supplies
every missing target.  The resulting universal word has the length in
(1.1).  The three consequences are immediate.  `square`

### Theorem 1.2 (regenerative spine form)

One compatible infinite odd auxiliary spine with odd terminalizations and
adjacent even taps, all satisfying `tau<=q`, gives the corresponding bound

\[
                       \nu(k)\le B(k)+q                 \tag{1.2}
\]

for every sufficiently large `k`.  The finitely many smaller dimensions can
be handled separately.

The quantifier order is

\[
 \exists (g_m,\mathcal C_m^{\rm odd},\mathcal C_m^{\rm ev})_{m\ge m_0}
 \quad\forall m\ge m_0,                                \tag{1.3}
\]

not `forall m exists a good transition`.  The terminal repair is paid only
in the requested terminal dimension and is not exported as new debt.

Theorem 1.2 is exactly the bounded-charge reset-spine reduction specialized
to a sharp charge `q`.  It is an implication, not an existence proof.

## 2. What the newest theorems actually close

### 2.1 Anonymous lower capacity is exact

The optimal residual matching-rank bank and every prescribed collar-column
bank admit an exact joint row decomposition.  The row sums differ by at
most one; if the total load is at most `dW`, every row has load at most `d`.
The fixed-residual problem has the exact Gale value

\[
 t_*=\max\left\{
 h_1^\downarrow,
 \max_{1\le x\le W}
 \left\lceil{
   \sum_{i\le x}h_i^\downarrow+
   \sum_j(m_j-W+x)_+
  \over x}\right\rceil
 \right\}.                                             \tag{2.1}
\]

Equitable residual loading minimizes every collar cut.  Thus there is no
remaining scalar or anonymous rank-incidence obstruction.

Separately, named targets of every rank can be assigned to distinct
containing owner/rank ports with the same equitable owner-load histogram.
What remains open is the intersection of these facts: the targets assigned
to one owner must form one named inclusion flag in the prescribed anonymous
rank pattern, and those flags must be realized by one sliding literal
chronology.

There is now an exact named lift on a substantial face.  On the theorem's
`2r`-coordinate model, the cross-SCD sparse-top theorem attaches pairwise
disjoint residual rank blocks `B_j` below a collar bottom `t` whenever

\[
 |B_j|\le d-(r-t),
 \qquad
 \sum_j {\binom{2r}{\max B_j}\over W}
 \le {\binom{2r}{t}\over W}.                           \tag{2.2}
\]

It produces literal named owner flags of length at most `d`.  In particular,
on that parity model the complete central `d`-rank band
`r-d,...,r-1` has an exact named-flag realization.  The theorem deliberately
does not chainize the entire strict lower ideal, and it does not by itself
supply the other parity: the remaining lower ranks need multi-depth sockets,
serial cross-chain splicing, or a jointly selected collar.  Thus the lower
gate has shrunk, but it has not disappeared.

### 2.2 The abstract cap-two upper palette exists

For every owner semilength there is a simple Catalan duplicate family `D`
such that `1+1_D` is the exact cap-two immediate-upper multiplicity target.
It can avoid a small protected colour bank.  Row-fixed Ryser transport
reaches this target in the abstract incidence matrix while fixing protected
rows.

This closes the target palette, not the literal occurrence selector.  It
does not choose compatible tail/head occurrences, prove that the selected
owner graph is one component, lift every Ryser square to a Boolean circuit,
or preserve the all-width deck.

For a fixed first factor there is also an exact integral selector reduction:
choose a rainbow base `Q`, then an integral residual head-colour master `J`,
then pass one all-subset predecessor-fibre Hall system.  This replaces a
vague "rainbow completion" by an exact finite min-max.  It does not prove
that a suitable correlated pair `(Q,J)` exists for every Boolean instance,
and functionality alone does not make the selector one Rado matroid.

### 2.3 The raw protected owner atlas has full rank

For every fixed predecessor matching, the complete rooted-link digraph is
strongly connected.  A fixed protected pivot forest therefore extends to a
graphic spanning tree.  Moreover, for every strict order extending the
pivot paths, each immediate-upper colour has both a forward and a backward
rooted occurrence.  Hence the full forward atlas is simultaneously
pivot-containing, upper-surjective, and acyclic.

This removes graphic-rank and raw colour-supply obstructions.  It does not
select distinct tails and heads.  Indeed, once a strict order is fixed, a
`W-1` edge tail/head-injective set is forced to be the consecutive Hamilton
path in that order.  The genuine remaining choice is the Hamilton order (or
the full occurrence selector), not a positive-density matching inside one
frozen forward atlas.

### 2.4 Component topology has exact Hall criteria

After an upper-exact rooted forest `Q_0` is fixed, its free component ports
form a bipartite graph `B`.  If `C` is the component count, then

\[
 \delta(B)=C-\nu(B)                                    \tag{2.3}
\]

is the minimum path-component count among connector matchings.  A state
with one path plus cycles exists iff `delta(B)<=1`.  A direct Hamilton path
exists iff a suitable ordered prescribed-endpoint port graph satisfies
Hall.  This is an exact max-flow gate.

If only one path plus cycles is obtained, palette-preserving switches cannot
change the path count on a fixed port fibre.  Serial protected quaternary
octagons remove the cycles only under an additional literal accessibility
hypothesis.

### 2.5 Arbitrary-width upper coverage has an exact retained-channel gate

Immediate-upper surjectivity is not arbitrary-width coverage.  On the
rooted-forest face, one must choose one old witness of every higher target
so that the union of their edge sets and the protected pivot uses at most
one occurrence of each immediate-upper colour.  This is the rainbow witness
bank.

The witness bank extends to an upper-exact rooted forest exactly when the
component-omission inequalities

\[
 |Y|\le
 \sum_{R:N_R^\sigma\cap Y\ne\varnothing}(\mu_R-1)
 \qquad(Y\subseteq\operatorname {Comp}(F))             \tag{2.4}
\]

hold.  Ordered component-port Hall then adds connectors without deleting
the protected bank, so every selected higher witness survives.  A cycle
switch route must instead avoid the bank or explicitly redeliver every
cut witness.

For an already all-width-complete Hamilton cycle, a q1-safe opening is
all-width safe only when the cut also avoids every higher forced-cut core.
The duplicate-provider count alone is not enough.

### 2.6 The monotone pivot is exactly upper-transparent

At a cut satisfying

\[
                         X\subseteq A_{-1}\cup A_1,    \tag{2.5}
\]

inserting the pivot letter `X` preserves the OR of every old source
interval.  The sharp-aperture geodesic creates one singleton and two
complete lower rays, and the local pivot compiler assigns those ray targets
with zero local loss once the transported background matching is fixed
away from them.

Thus the pivot itself does not reopen the all-width gate and does not need
the folded-cross value/phase converter.

### 2.7 The one-token pivot overlay has no token-orbit obstruction

On the odd same-parity pivot route, the scalar recurrence satisfies

\[
                         d_{m+1}-d_m\in\{0,1\}.
\]

The fresh sharp-aperture relay compresses the persistent pivot boundary to
one rank-`(R-1)` token `H`.  At child rank `R` and depth `D`, its exact set
of possible outputs is

\[
 \mathcal S_D(H)=
 \left\{J:\ |J|=R-1, |H\cap J|=R-D\right\}.           \tag{2.6}
\]

The graph on tokens joining exact-distance pairs in (2.6) is connected.  A
coordinate bank `F` can be avoided by one relay exactly when

\[
 |F\cap H|\le D-1,
 \qquad
 |F\setminus H|\le R-D+1.                              \tag{2.7}
\]

Consequently every fixed-size coordinate bank can be flushed for large
`R`.  Aligning the outgoing token with the opened seam also coalesces the
missing q1 colour, pivot aperture colour, and missing wrap-router entry into
one logical boundary ticket.

These results close token-coordinate reachability and bounded-bank
avoidance only.  They do not plant a fresh child owner host, choose the
all-width chronology, fix a cap state, or create the occurrence router.

### 2.8 The common-cap algebra is exact only after one state is fixed

After one complete cap/guard/occurrence state `c`, one transported-background
model, and one allocation of shared capacities are fixed, the two physical
occurrence coordinates give Rado matroids `R_0^c,R_1^c` on a common logical
ticket set.  Their exact common deficiency is

\[
 \delta(c)=
 \max_{J_0\cap J_1=\varnothing}
 \left(
 |J_0|-r_{N_0^c}(A_0^c(J_0))+
 |J_1|-r_{N_1^c}(A_1^c(J_1))
 \right).                                              \tag{2.8}
\]

Structural zeros separate exactly.  A balanced regular incidence factor
gives a complete compiler only when every claim has a private physical
claim-to-port prefix and the entire active port bank has one simultaneous
typed suffix linkage to distinct unused sinks in that same state.  The
abstract factor alone does not prove this rank condition.

In particular, the `h=2` protected middle-levels factor supplies the
abstract regular incidence pattern only (after a ticket-to-left-shore
injection).  It does not supply the capacity-faithful physical port map,
private literal prefixes, or the typed simultaneous suffix linkage.

On the native interval-diamond face, already materialized upper-turn
occurrences give a source-free dual-role terminal bank of full rank in one
occurrence coordinate.  This avoids the artificial source-position cut,
but only if the cap permits the same upper-turn occurrence to keep its
upper-witness role and serve as the ticket terminal.  It does not prove the
second coordinate or global product closure.

## 3. The `B+1` branch

### 3.1 The shortest proof-safe implication

For one dimension, suppose there is a final literal source `Z` of length
`B(k)+1` with a distinguished nonempty pivot letter `X`.  Let `A` be the
length-`B(k)` source obtained by deleting that occurrence of `X`.  Assume
that the following data are certified jointly:

1. the exact balanced named lower flags and their physical interval cells;
2. the depth-`d` row of `Z` consists of every middle owner once in an upper-exact
   rooted Catalan forest carrying a rainbow witness bank for every higher
   target, together with the one controlled boundary nonowner forced by the
   `B+1` scaffold;
3. a protected component-port Hamilton path containing the sharp-aperture
   pivot collar, satisfying residence, and assigning the boundary
   nonowner's endpoint/cap role;
4. the source `A` satisfies (2.5) at the pivot cut, its selected all-width
   witnesses are protected through the insertion, and the new local windows
   of `Z` satisfy the flat owner-window conditions;
5. one transported background lower matching disjoint from the pivot cells,
   with the singleton and both pivot rays assigned literally; and
6. no target omitted after the final replay.

View `Z` as the certified insertion of `X` into `A`.  Items 2--3 give every
middle and upper target; the rainbow bank and (2.5) retain every
arbitrary-width upper witness.  Items 1,4--5 give every strict-lower target.
The result has length `B(k)+1` and is universal.  Therefore

\[
                         \nu(k)\le B(k)+1.              \tag{3.1}
\]

No canonical folded-cross converter is used in this implication.  Nor is a
two-coordinate Rado compiler needed if Item 5 is supplied directly as one
literal matching.  If the common-cap machinery is used instead, its menus
must encode the actual pivot/background tickets in one fixed state; the
canonical folded-ticket theorem cannot be imported by name alone.

### 3.2 The single strongest missing theorem for `B+1`

> **Protected Pivot-Path Coinstantiation theorem `PPC(1)`.**  There exists
> one compatible odd spine with adjacent even taps such that every terminal
> branch materializes Items 1--6 above in one source word and exports the
> next auxiliary state literally.  On the odd branch the exported pivot
> interface is only the one token of (2.6); the child host, all-width bank,
> and common cap are rebuilt and accepted child-natively.

`PPC(1)` implies `nu(k)<=B(k)+1` for all sufficiently large `k` by Theorem
1.2, and the finite prefix can be checked separately.

This is the strongest honest missing theorem because its individual
projections are now mostly understood:

* anonymous balanced rows are exact;
* rank-separated named containment is exact;
* the complete central `d`-rank band and every sparse-top face satisfying
  (2.2) have exact named flags;
* the pivot token transition sphere is connected and fixed coordinate banks
  are exactly avoidable by (2.7);
* component-port topology is exact Hall;
* all-width retention is rainbow-bank plus component-omission Hall;
* the pivot insertion and local ray compiler are exact.

What is not known is that one literal object lies in the intersection of
these projections and regenerates.  Calling the missing statement only
"balanced flags" or only "a Catalan path" hides this correlation.

Since this branch has scaffold excess `c=1`, `PPC(1)` must have
`H=emptyset`.  Even one terminal casualty would give charge at least two
and prove only `B+2` through this branch.

## 4. The exact-`B` branch

### 4.1 What the current diagonal/cap-two architecture would need

Within the present exact branch, one needs in one literal state:

1. exact balanced named lower flags at depth `d`, including the prescribed
   triangular boundary cells, with no omitted lower target;
2. a q1-exact cyclic diagonal owner row and a literal cap-two occurrence
   selector realizing the protected `1+1_D` target;
3. one Hamilton component, residence, and every arbitrary-width upper
   witness, with an all-width-safe opening only if a linear terminal word is
   required;
4. the canonical folded terminal tickets lifted to complete occurrence
   bundles in both physical coordinates;
5. a type-preserving common-cap converter/router with zero structural zeros,
   zero marginal rank loss, global product closure, and exact background;
6. literal odd regeneration and an even terminal tap; and
7. no omitted target and no extra position.

The diagonal interval diamonds close a valuable subrow: for a q1-exact
row, each native lower port has a private route to a matched upper-turn
occurrence.  A q1/q2 ladder even gives two native terminal addresses.  But
these native tickets are nested upper Hasse pairs.  The canonical folded
ticket is an incomparable opposite-ray pair.  They are not the same typed
object.

The first-exit boundary diamond converts the types exactly only in the
codimension-one case `d=2,j=1`.  For a general folded ticket, every
cap-preserving Hasse/diamond fan has at least `d` edges and `d+1` Boolean
values, and its longest branch has length `max(j,d-j)`.  This is not an
extra word-length lower bound, but it rules out treating the missing
converter as a bounded local socket.

### 4.2 The single strongest missing theorem for exact `B`

> **Protected Converter-Cycle Coinstantiation theorem `PCC(0)`.**  There
> exists one compatible odd spine with adjacent even taps such that every
> terminal branch materializes Items 1--7 above in one cap state.  In
> particular, the cap-two target is realized by literal occurrences in one
> Hamilton/all-width chronology, and the full-depth folded converter and
> both occurrence-coordinate routers have exact rank with global product
> closure.

`PCC(0)` implies `nu(k)=B(k)` by Theorem 1.2 and the lower bound.

The theorem is stated for the current diagonal/folded architecture only.
An entirely different exact construction could bypass its converter.
Within this architecture, however, neither the abstract Ryser selector nor
the native nested-upper router removes `PCC(0)`.

Exact `B` is therefore strictly stronger at the terminal interface than the
pivot route: it replaces one explicit transparent insertion by a zero-slack
cycle, a literal occurrence selector, and a growing-depth type converter.

## 5. Hidden mismatches which must remain explicit

### 5.1 State-before-graph quantifiers

The cap state, physical occurrence bank, shared-capacity allocation,
transported background model, and structural zeros must be fixed before the
Rado graphs are formed.  The valid order is

\[
 \exists c\quad\forall U\subseteq I:
 \rho_0^c(U)+\rho_1^c(I\setminus U)\ge |I|-K,          \tag{5.1}
\]

not `forall U exists c_U`, and not two different states for the two
coordinates.

### 5.2 The two coordinates are not the two ray matchings

In the common-cap theorem, `p=0,1` index the two physical occurrence
coordinates required by every ticket in the union of the two canonical
cross-ray matchings.  They are not the two matchings, not automatically the
two phases, and not automatically the q1 and q2 banks.

### 5.3 Ticket-type mismatch

Native diagonal and q1/q2 terminal pairs are nested upper Hasse pairs.
Canonical folded tickets are incomparable cross rays, normally in opposite
phases.  A deterministic paired address does not prove typed acceptance.
The native boundary diamond converts only the `d=2,j=1` case; the general
fan has depth `Theta(d)`.

### 5.4 Capacity-model mismatch

In the native interval-address model, overlapping intervals are distinct
physical cells and source letters are semantic edge labels.  The
source-free dual-role diamond then has full rank.  In the stronger model
which node-prices every boundary source occurrence, the same-looking route
family has a `W/2` cut unless source capacity is doubled or the upper
attachment is private.  A proof must choose one model consistently.

### 5.5 Abstract versus literal selectors

The simple Catalan target and row-fixed Ryser path live in an abstract
margin fibre.  A Ryser square need not be a legal Boolean `C6`, and the
target does not choose tail/head occurrences or topology.  Likewise, an
abstract protected middle-levels factor does not provide physical
claim-to-port prefixes or a full-rank typed suffix router.

### 5.6 Anonymous rows versus named flags

The exact anonymous row decomposition and the exact rank-separated named
target assignment can be different integral points.  Neither theorem makes
the targets in one owner nested, and no relabelling after the owner
chronology is fixed is justified.

### 5.7 q1 safety versus all-width safety

Duplicated immediate-upper occurrences guarantee many q1-safe cuts.  A
higher target can nevertheless have every witness cross all those cuts.
The forced-cut cores or the rainbow witness bank must be checked.

### 5.8 Marginal router rank versus product closure

Two full marginal Rado ranks do not imply a common ticket bank when
representative pairs are correlated or when the coordinates share an
unallocated capacity.  Ticketwise rectangular menus are still insufficient
if a cross-ticket constraint survives.

### 5.9 Frozen background versus contraction

Deleting one named background realization is not matroid contraction unless
a direct-sum separation is proved.  The frozen-private and adaptive-recourse
models are different and must not be mixed in one rank calculation.

### 5.10 Bounded defect versus a sharp bound

A theorem producing at most `C` structural zeros or router omissions proves
only additive charge `C`.  For `PCC(0)` every such quantity must be zero.
For the pivot branch the inserted position already consumes the entire
`B+1` budget, so its terminal omission must also be zero.

### 5.11 Odd versus all dimensions

The equal-shore odd diagonal theorem does not construct the even branch.
The even bilayer ledger is exact conditional accounting, not an even
chronology.  An all-`k` theorem needs direct certificates in both parities or
one compatible odd spine with authenticated even taps.

### 5.12 Per-dimension existence versus regeneration

Per-dimension direct certificates are enough for a nonconstructive upper
bound.  If the proof is inductive, however, `forall m exists a good child`
does not produce one infinite compatible spine.  Parent-local menus and
phase records must be rebuilt and authenticated in the exported child.

## 6. Shortest honest roadmap

The proof effort should now be split by intended sharpness.

### To prove `B+O(1)`

It suffices to prove one co-instantiated reset spine with uniformly bounded
terminal charge.  The existing Rado/private-router algebra is designed for
this level of conclusion.

### To prove `B+1`

Prove `PPC(1)`: one protected all-width Catalan Hamilton path, one balanced
named-flag source antecedent, one sharp-aperture pivot, one exact transported
background/ray compiler, and literal regeneration, all in the same state.
No terminal casualty is allowed.

### To prove exact `B`

Either prove `PCC(0)` in the current cap-two diagonal branch, including the
full-depth type converter and exact two-coordinate product closure, or find
an exact architecture which bypasses folded conversion entirely.  Every
terminal defect must be zero.

The mathematical bottleneck is therefore no longer a missing scalar count,
ordinary Hall theorem, or abstract palette.  It is the existence of one
literal, occurrence-labelled, all-width, regenerating object in the
intersection of the now-understood projections.

## 7. Authoritative inputs

This synthesis uses the following proof-safe files.

* `MATH_THEOREM_UNIFORM_COINSTANTIATED_BOUNDED_CHARGE_RESET_SPINE_REDUCTION_20260803.md`
* `MATH_THEOREM_ANTITONE_BALANCED_RESIDUAL_COLLAR_RANK_COUPLING_20260803.md`
* `MATH_THEOREM_RANK_SEPARATED_NAMED_TARGET_EQUITABLE_MATROID_INTERSECTION_20260803.md`
* `MATH_THEOREM_EQUITABLE_PATTERN_CONFIGURATION_FRACTIONAL_MATCHING_20260803.md`
* `MATH_THEOREM_CROSS_SCD_SPARSE_TOP_COLLAR_ATTACHMENT_20260803.md`
* `MATH_THEOREM_PROTECTED_SIMPLE_CATALAN_TARGET_AND_ROW_FIXED_RYSER_20260803.md`
* `MATH_THEOREM_FIXED_FACTOR_RAINBOW_COMPLETION_HEADCOLOUR_HALL_AND_NONMATROID_GATE_20260803.md`
* `MATH_THEOREM_PROTECTED_UPPER_EXACT_CATALAN_FOREST_FORWARD_ATLAS_PULL_ABSORBER_20260803.md`
* `MATH_THEOREM_BPLUS1_PROTECTED_COMPONENT_PORT_HALL_AND_OCTAGON_HAMILTONIZATION_20260803.md`
* `MATH_THEOREM_BPLUS1_ALLWIDTH_RAINBOW_WITNESS_BANK_AND_SAFE_OPENING_20260803.md`
* `MATH_THEOREM_BPLUS1_ONE_TOKEN_REGENERATIVE_OVERLAY_AND_FIXED_FIBRE_OBSTRUCTION_20260803.md`
* `MATH_THEOREM_FIRST_EXIT_BOUNDARY_DIAMOND_CONVERTER_AND_FAN_DEPTH_BARRIER_20260803.md`
* `MATH_THEOREM_DIAGONAL_INTERVAL_DIAMOND_SOURCE_FREE_DUAL_ROLE_ROUTER_20260803.md`
* `MATH_THEOREM_DIAGONAL_Q1_Q2_TWO_COORDINATE_UPPER_LADDER_ROUTER_20260803.md`
* `MATH_THEOREM_DIAGONAL_DUAL_ROLE_TWO_BOUNDARY_CAPACITY_DICHOTOMY_20260803.md`
* `MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`
* `MATH_THEOREM_REGULAR_INCIDENCE_FACTOR_PRIVATE_PORT_ROUTER_20260803.md`
* `MATH_THEOREM_BALANCED_FACTOR_EXACT_PORT_RANK_AND_FERRERS_ORTHOGONALITY_20260803.md`
* `MATH_THEOREM_EVEN_DIAGONAL_BILAYER_LITERAL_ROUTER_AND_BOUNDARY_LEDGER_20260803.md`

The unversioned first common-cap draft is formatting-failed lineage and is
not cited.
