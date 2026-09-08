# Protected Catalan--pivot connector birth and the prepared-scaffold gate

**Date:** 2026-08-02  
**Lane:** K, protected Catalan connector / monotone-pivot `B+1` bridge  
**Status:** unconditional local infinite-family packet, exact born-connector
theorem, and exact all-width/residence composition criterion.  Existence of
the prepared global Hamilton scaffold is not proved.

## 0. Outcome

Let

\[
 W={2m-1\choose m},\qquad
 U={2m-1\choose m+1},\qquad
 C=W-U=\operatorname {Cat}_m .                         \tag{0.1}
\]

For every `d>=1` and `m>=3d+1`, the sharp monotone-pivot construction gives
a literal rank-`m` Johnson path `P` of `3d+1` owners with the following
properties:

* its `3d` lower transition colours are distinct;
* its `3d` upper transition colours are distinct;
* its predecessor incidence phase extends to a perfect matching `M_0`;
* the successor phase contracts to one directed rooted path;
* every non-clipped positive run internal to `P` has length at least `d+1`;
* the central source insertion preserves every old interval-OR occurrence,
  at every width, and creates the exact two nested lower rays.

Thus the pivot is already a legal protected seed in every rooted resource.
The Catalan-scale connector is not a second object if one constructs the
final chronology prospectively:

> **Born-connector principle.**  An upper-turn-surjective alternating
> Hamilton path containing `P` automatically contains an upper-exact rooted
> Catalan forest `Q_0` containing the protected successor phase and the
> remaining `C-1` edges automatically form the compatible directed
> free-port Hamilton path through the `C` components of `Q_0`.

No four-matroid extension and no post-hoc connector search remain on this
face.  Conversely, a rooted Catalan forest plus a compatible `C-1`-edge
free-port connector path is exactly such a Hamilton path.

The physical source row also has an exact prospective formulation.  Start
with a nonflat pre-insertion word `A^-` and insert `X` at one cut.  If

1. `X` is contained in the union of the two old letters adjacent to the
   cut;
2. `A^-` already witnesses every required upper target at every width;
3. the final depth-`d` row is the protected upper-turn-surjective Hamilton
   owner path plus one controlled boundary nonowner; and
4. the two clipped residence interfaces of `P` match the two ambient bulk
   interfaces,

then the final word retains every old upper witness, is resident, and its
owner layer contains the required `Q_0` and all `C-1` connectors.  The
residence condition is a finite two-boundary state, not a global new row.

This is the sharp constructive reduction supplied here.  The sole central
existence gate is now a **prepared temporal Hamilton scaffold** satisfying
items 2--4 jointly.  The corrected fractional pull-clock/age circulation
proves marginal fractional feasibility but does not produce that integral
scaffold.  The terminal global common cap and regeneration remain separate.

## 1. The unconditional protected pivot seed

Work in the middle-levels incidence graph

\[
 \operatorname {ML}_m=
 { [2m-1]\choose m-1}\ \cup\ { [2m-1]\choose m}.
                                                               \tag{1.1}
\]

The sharp pivot collar of
`MATH_THEOREM_SHARP_PIVOT_APERTURE_AND_RESIDENT_GEODESIC_PACKET_20260801.md`
uses `m+3d` coordinates.  Hence it embeds in `[2m-1]` whenever

\[
                         m\ge3d+1.                    \tag{1.2}
\]

Write its owner path as

\[
             P=(V_0,V_1,\ldots,V_{3d}),               \tag{1.3}
\]

and put

\[
 I_i=V_i\cap V_{i+1},\qquad
 R_i=V_i\cup V_{i+1}\quad(0\le i<3d).                \tag{1.4}
\]

The explicit collar theorem gives pairwise distinct `I_i`, pairwise
distinct `R_i`, and internal positive residence threshold `D=d+1`.

Define the two incidence phases

\[
 P_0=\{I_iV_i:0\le i<3d\},\qquad
 P_1=\{I_iV_{i+1}:0\le i<3d\}.                       \tag{1.5}
\]

### Proposition 1.1 (infinite-family protected rooted seed)

Under (1.2), `P_0` extends to a perfect matching `M_0` of `ML_m`.  For every
such extension, the rooted links of `P_1` form one directed path and their
upper labels are the pairwise-distinct colours `R_i`.

#### Proof

The `I_i` and `V_i` in `P_0` are separately distinct, so `P_0` is a
matching of size `3d`.  From (1.2), `3d<=m-1`; the protected small-matching
extension theorem therefore extends it to a perfect matching `M_0`.

For `i<3d-1`, one has `M_0(I_(i+1))=V_(i+1)`.  Consequently the rooted link
of `I_iV_(i+1)` is

\[
                         I_i\longrightarrow I_{i+1}.   \tag{1.6}
\]

The last link ends at the new vertex `M_0^{-1}(V_(3d))`, which cannot equal
an earlier `I_i` by injectivity of `M_0`.  Thus the links form one directed
path.  At `I_i` the two owners are `V_i,V_(i+1)`, so the rooted upper label
is `R_i`; these labels are distinct by the collar construction. \(\square\)

The proposition is unconditional for every pair `(m,d)` satisfying (1.2).
It proves a protected common-independent seed, not its global upper-exact
extension.

## 2. The Catalan connector is born inside one Hamilton path

Fix `M_0`.  For an incidence `e=LV` outside `M_0`, put

\[
 \operatorname {up}(e)=M_0(L)\cup V,\qquad
 \lambda(e):L\longrightarrow M_0^{-1}(V).             \tag{2.1}
\]

### Theorem 2.1 (protected born-connector theorem)

Let `Q` be a matching in `ML_m-M_0` satisfying

\[
 |Q|=W-1,\qquad
 \lambda(Q)\text{ is graphic-independent},\qquad
 \operatorname {up}(Q)={ [2m-1]\choose m+1},          \tag{2.2}
\]

and suppose `P_1 subseteq Q`.  Then there is a decomposition

\[
                         Q=Q_0\mathbin{\dot\cup}Q_1   \tag{2.3}
\]

such that

1. `P_1 subseteq Q_0`;
2. `up:Q_0 -> binom([2m-1],m+1)` is a bijection;
3. `lambda(Q_0)` is a forest with exactly `C` directed-path components;
4. `|Q_1|=C-1`; and
5. after contracting the components of `lambda(Q_0)`, the links of `Q_1`
   form their directed free-port Hamilton path.

Conversely, any `Q_0,Q_1` satisfying items 2--5 has union `Q` satisfying
(2.2).  Expanding the `M_0` edges gives one alternating Hamilton path of
`ML_m` containing the whole incidence lift of `P`.

#### Proof

Because `Q` is a matching of size `W-1`, its rooted graph has indegree and
outdegree at most one.  Graphic independence makes its `W-1` links a
spanning tree on `W` vertices; hence it is one directed spanning path.

Choose one edge of `Q` carrying every upper colour.  For each protected
colour `R_i`, choose its prescribed edge in `P_1`.  These protected choices
are compatible because the `R_i` are distinct.  Call the selected set
`Q_0`.  It has `U` edges and is a subset of the rooted path, so it is a
forest.  On all `W` rooted vertices it has

\[
                         W-U=C                         \tag{2.4}
\]

components, each a directed path.  Put `Q_1=Q-Q_0`.  Then

\[
                         |Q_1|=(W-1)-U=C-1.            \tag{2.5}
\]

Deleting `Q_0` from the full directed rooted path records the old components
in their path order.  The remaining edges use their unique free outgoing
and incoming ports and join them in that order; after contraction they are
the directed Hamilton path asserted in item 5.

Conversely, a forest plus a free-port component path is a spanning rooted
tree of maximum degree two, hence a rooted Hamilton path.  The edge count is
`U+C-1=W-1`, and `Q_0` already carries every upper colour.  Expanding
`M_0` proves the incidence statement. \(\square\)

This theorem is stronger than a post-hoc connector existence statement:
once the final path is chosen prospectively, the Catalan representatives
and the entire Catalan-scale tree are literal subsets of it.

### Corollary 2.2 (safe owner-layer opening from a cycle)

Suppose an upper-turn-surjective alternating Hamilton cycle contains the
protected pivot path.  Then, under (1.2), one may delete a nonprotected
redundant upper-provider edge and obtain the path in Theorem 2.1.

#### Proof

There are `W` upper-turn occurrences and `U` upper colours, so the total
excess is `C`.  If `s` colours are repeated, the number of occurrences of
repeated colours is `C+s>=C+1`.  For `m>=3`, `C>=m`; hence (1.2) gives
`C+1>3d=|P_1|`.  Some redundant-provider edge lies outside `P_1`.
Deleting it preserves every upper colour and opens the rooted cycle into a
path.  Apply Theorem 2.1. \(\square\)

Corollary 2.2 concerns the owner/immediate-upper layer.  A physical cyclic
word may lose wrapping witnesses at the cut; all-width preservation needs
the occurrence condition in Section 4 or a directly linear construction.

### Theorem 2.3 (alternative unrooted closed-shore test)

There is also a non-tautological prospective test before either matching
phase is fixed.  Let `F_0` be a Johnson linear forest on the rank-`m`
owners such that

* its edge unions biject onto all rank-`m+1` upper colours;
* its edge intersections are distinct rank-`m-1` lower roots; and
* it contains every protected owner edge of `P`.

Thus `F_0` has `U` edges and `C` components.  Among the `C` lower roots not
used by `F_0`, choose the one omitted root `o` and the two intended owner
endpoints `s,t`, subject to

\[
                         o\subset s\quad\hbox{or}\quad o\subset t. \tag{2.5a}
\]

Let `A` be the lower
roots unused by `F_0` other than `o`, and put

\[
 c_T=2-\mathbf1_{T=s}-\mathbf1_{T=t}-\deg_{F_0}(T).
                                                               \tag{2.6}
\]

Assume `c_T>=0` and the automatic total identity

\[
                         \sum_Tc_T=2|A|=2(C-1).        \tag{2.7}
\]

For an owner shore `Y`, let

\[
 \begin{aligned}
 I_A(Y)&=|\{L\in A:N(L)\subseteq Y\}|,\\
 J_A(Y)&=|\{L\in A:|N(L)-Y|=1\}|,
 \end{aligned}                                         \tag{2.8}
\]

where `N(L)` is the `m`-owner containment star of `L`.  Then one can choose
one Johnson edge on every root in `A`, meeting the owner degree demands
(2.6), if and only if

\[
          2I_A(Y)+J_A(Y)\le\sum_{T\in Y}c_T
                    \qquad\text{for every owner shore }Y.       \tag{2.9}
\]

Such a choice is the desired `C-1`-edge Catalan connector precisely when,
in addition, its edges have contracted graphic rank `C-1` over `F_0`.
In that case the union is one owner Hamilton path; its incidence lift
becomes a spanning alternating Middle Levels path only after adjoining the
omitted lower endpoint `o` at an endpoint owner containing it.  Under
(2.5a), that lift determines the alternating matching `M_0` and recovers
the rooted decomposition of Theorem 2.1.

#### Proof

Use the integral network with capacity two from the source to each residual
root, unit arcs from a root to each containing owner, and capacity `c_T`
from owner `T` to the sink.  A value-`2|A|` integral flow selects two
distinct containing owners at every root, hence one Johnson edge, and meets
all owner degrees by (2.7).  Minimizing a cut rootwise for fixed `Y`, a root
costs two units when its whole star is trapped in `Y`, one when exactly one
owner escapes, and zero otherwise.  Max-flow/min-cut is therefore exactly
(2.9).

The selected `C-1` Johnson edges join the `C` components of `F_0`.  Their
union with `F_0` has `W-1` edges and the prescribed path degree sequence.
It is the Hamilton connector if and only if it is acyclic, equivalently if
the contracted selected edges have graphic rank `C-1`.

The incidence lift has one unmatched lower root, namely `o`.  Recovering a
spanning alternating path requires adjoining the incidence `os` or `ot` at
an owner endpoint, which is possible exactly under (2.5a).  The parity class
containing that endpoint incidence is then the perfect matching `M_0`.
Without the containment the unrooted owner path may still exist, but it
misses the physical lower vertex `o` and the claimed perfect `M_0` does not
follow.
\(\square\)

The right side of (2.9) is literally the free induced-path endpoint supply
of `F_0`, with the two named final endpoints subtracted.  Explicitly,

\[
 \sum_{T\in Y}c_T
 =2\kappa(F_0[Y])-|\partial_{F_0}Y|
   -\mathbf1_{s\in Y}-\mathbf1_{t\in Y},              \tag{2.10}
\]

where isolates count as induced components.  Thus the newest closed-shore
theorem closes every marginal port/degree inequality.  It still does not
imply the contracted graphic rank, and it does not construct `F_0`; both
must be selected prospectively.  This unrooted formulation must not be
silently mixed with a previously fixed `M_0`: before the final path is
chosen, a residual root is free to choose both of its owner endpoints.

### Corollary 2.4 (cycle-cover escape under the endpoint guard)

Every integral flow satisfying (2.6)--(2.9) is a disjoint union of one
`s`--`t` owner path and zero or more owner cycles.  Suppose its components
admit a protected-compatible incidence tree of degree-preserving maximum
connector mergers which leaves `F_0` and `P` fixed, preserves the selected
lower-root multiset, never uses `o`, and preserves the two degree-one
endpoints.
Then the mergers produce one owner Hamilton path.  Under (2.5a), adjoining
`o` at the containing endpoint gives the spanning alternating Middle Levels
path of Theorem 2.1.

#### Proof

The final degree vector is one at `s,t` and two elsewhere.  Hence exactly
one connected component contains degree-one vertices, necessarily both of
them; that component is an `s`--`t` path and every other component is a
cycle.  The incidence-tree merger argument decreases the component count
to one while preserving the degree vector.  A connected graph with exactly
two degree-one vertices and every other degree two is one path.  Since the
mergers avoid `o` and preserve `s,t`, condition (2.5a) survives, and the
same endpoint incidence completes the alternating lift. \(\square\)

This corollary is conditional on a literal safe merger basis.  The
closed-shore inequalities alone supply the path-plus-cycles factor and no
cross-component merger.

## 3. Residence is an exact two-boundary state

Set `D=d+1`.  For a binary word `b`, call it internally `D`-resident if
every maximal 1-run meeting neither global endpoint has length at least
`D`.  For a nonempty fragment `F`, record

\[
 \sigma_D(F)=
 (b_{\rm first},b_{\rm last},
  \min(D,p(F)),\min(D,s(F)),\mathbf1_{F\equiv1},g(F)), \tag{3.1}
\]

where `p(F),s(F)` are its leading and trailing 1-run lengths and `g(F)`
records whether every internal 1-run is good.  Take the product of these
states over all coordinates.

### Lemma 3.1 (clipped-state composition)

Whether a concatenation of internally `D`-resident fragments is internally
`D`-resident is determined exactly by their states (3.1).  In particular,
for `B^- P B^+`, after the bulk fragments are fixed, residence of the whole
word is an exact condition on the two clipped endpoint states of `P`.

#### Proof

Every maximal 1-run of a concatenation is either internal to one fragment
or is obtained by joining a suffix 1-run of one fragment to the prefix
1-run of the next.  Internal runs are certified by `g`.  A joined run has
length `s(F)+p(G)` unless one fragment is all-one, in which case the same
addition propagates through it.  For testing the threshold `D`, every
summand may be clipped at `D`; the all-one bit records exactly when
propagation is required.  If the endpoint bits differ, the clipped run on
the 1-side terminates at that seam and its stored length decides legality.
No other run changes. \(\square\)

For the explicit pivot collar, all non-clipped internal runs are already
good; only its two endpoint signatures remain to be supplied by the
ambient bulk.  Thus residence is not an additional Catalan-scale matching
problem.

This is the positive-residence convention used by the pivot theorem.  If a
later interface requires simultaneous positive and zero residence, apply
the same state and lemma also to the complemented coordinate trace.

## 4. All-width upper inheritance is monotone

Let a source word `A^-` have adjacent letters `A_-1,A_1` at the chosen cut,
and insert a nonempty letter `X` to obtain `A^+`.

### Lemma 4.1 (all-width transport)

If

\[
                         X\subseteq A_{-1}\cup A_1,    \tag{4.1}
\]

then every interval-OR occurrence of `A^-` has an occurrence of the same
value in `A^+`.  Consequently, if `A^-` covers every required upper target,
then so does `A^+`.

#### Proof

An interval on one side is copied literally.  The convex hull of an old
crossing interval gains only the new letter `X`; it already contains both
`A_-1` and `A_1`, whose union contains `X`, so its OR is unchanged. \(\square\)

This statement is occurrencewise and holds simultaneously at every width.
It does not assert that the transported occurrence stays in its old width
bucket: a crossing interval gains one source position.

## 5. The prepared-scaffold composition theorem

Call `A^-` a **prepared `(m,d)` pivot scaffold** if there is a cut and an
inserted letter `X` such that:

1. (4.1) holds;
2. `A^-` covers every required upper target at every width;
3. the insertion has the exact temporal pivot form: the old `d` crossing
   depth-`d` cells have rank `m+1`, while the new `d+1` crossing cells are
   the central owners of the sharp pivot path; moreover, the `d-1` old
   crossing cells in the maximal strict-lower compiler width have the
   internal owner values `M_1,...,M_(d-1)` and hence rank `m`;
4. after insertion, the complete depth-`d` owner bank consists of all `W`
   owners once, in an alternating Hamilton-path chronology satisfying
   (2.2), together with one controlled boundary nonowner cell; that cell is
   a rank-`m-1` set `o`, is the missing lower-shore endpoint ticket of the
   incidence path, and satisfies `o subset s` or `o subset t` for the
   corresponding endpoint owner (all other lower-shore vertices are its
   consecutive owner intersections);
5. this chronology contains the full collared path `P` from Section 1; and
6. the two bulk fragments and `P` pass the clipped-state test of Lemma 3.1.

The boundary nonowner in item 4 is part of the design state; it is not
forced by the scalar `W+1` count without a value-simplicity hypothesis.

### Theorem 5.1 (Protected Catalan--pivot connector)

Every prepared `(m,d)` pivot scaffold produces, after its one insertion,

1. a resident owner chronology containing the depth-`d` pivot-rich flat
   collar;
2. an upper-exact rooted Catalan forest `Q_0` containing the protected
   successor incidences;
3. its complete compatible `C-1`-edge directed free-port connector path;
   and
4. preservation of every old all-width upper witness.

The local strict-lower compiler bank is exactly the singleton plus the two
nested pivot rays from the monotone-pivot theorem.  If those target rows and
the transported background matching are admitted in one common cap, their
matched damage is zero.

#### Proof

Item 1 is precisely assumption 6 and Lemma 3.1.  Assumptions 4--5 give the
matching `Q` of Theorem 2.1, so that theorem gives items 2--3 while retaining
the protected collar.  Assumptions 1--2 and Lemma 4.1 give item 4.

For the compiler statement, the exact band-exchange theorem deletes only
the `d-1` old crossing cells of maximal allowed width.  Under assumption 3
these cells have rank `m`, so no strict-lower background matching uses
them.  Every other old cell transports injectively and the complement is
the singleton plus the two rays.  The stated common-cap hypothesis then
invokes the maximal-letter/common-`Q` theorem. \(\square\)

## 6. The factor-first alternative and its exact physical lift

There is a valid alternative to constructing the path directly.  Fix
`M_0`, an upper-exact rooted Catalan forest `Q_0` containing `P_1`, and a
perfect matching `R` between the `C` unused rooted tails and heads.  Then

\[
                         F=M_0\cup Q_0\cup R            \tag{6.1}
\]

is an upper-turn-surjective spanning two-factor containing `P`.  Every
selected upper representative lies in `Q_0`; consequently changing or
opening only `R` edges cannot delete the designated immediate-upper bank.

The matching row is exact ordinary Hall.  Give every component of `Q_0` an
outgoing and an incoming copy, and join `K_out` to `L_in` whenever one
literal incidence uses the unique free rooted tail of `K`, the unique free
rooted head of `L`, and passes every declared state/resource guard.  Call
this occurrence-labelled graph `B(Q_0)`.  Then `R` exists if and only if

\[
       |N_{B(Q_0)}(X)|\ge |X|
       \qquad(X\subseteq\operatorname {Comp}(Q_0)).    \tag{6.1a}
\]

A perfect `R` gives a directed cycle cover of the `C` components.  Equation
(6.1a) supplies no bound on the number of cycles and no safe merger.

Let `mathcal C(F)` be its factor components.  A **physically safe merger**
is a connector-only switch with deleted/added `R` incidences which:

1. preserves every owner/lower degree and leaves `M_0,Q_0,P` fixed;
2. is a certified maximum merger on its current component footprint;
3. carries an occurrence-labelled source lift, including the ordered source
   `d`-rails, one globally consistent address/pin quotient, and a complete
   source antecedent at every altered fragment;
4. preserves the declared owner-coordinate history state and has accepting
   clipped residence states at its new seams;
5. either preserves every declared all-width witness occurrence, or exports
   its exact lost/gained occurrence ledger; and
6. preserves the declared terminal-cap rows, or exports their exact
   additive ledger.

For several mergers, require pairwise-disjoint complete occurrence supports
or the weaker hereditary applicability condition: after every acyclic
subfamily, each next merger is still literal, accepting, and maximum on the
current factor.

### Theorem 6.1 (occurrence-lifted factor-first fusion)

Suppose the factor (6.1) has an occurrence-labelled source antecedent and a
family `mathcal T` of physically safe mergers.  Let `e_z` be the original
component footprint of `z`.  If

\[
 \sum_{z\in\mathcal T}(|e_z|-1)=|\mathcal C(F)|-1,     \tag{6.2}
\]

and

\[
 \sum_{z\in\mathcal A}(|e_z|-1)
       \le |\bigcup_{z\in\mathcal A}e_z|-1
 \quad(\varnothing\ne\mathcal A\subseteq\mathcal T),  \tag{6.3}
\]

then the mergers can be ordered so that they produce one factor cycle,
retain the pivot and every `Q_0` upper representative, and preserve every
exported coordinate whose total ledger increment is zero.

Let `R_fin` be the final connector-class matching after the mergers.  If
there is an unprotected connector incidence

\[
                         e=oV\in R_{\rm fin},
 \qquad |o|=m-1,\quad |V|=m,\quad o\subset V,          \tag{6.3d}
\]

such that

* cutting `e` has an accepted depth-`d` source linearization whose global
  address/pin quotient is consistent and whose controlled boundary nonowner
  cell has literal value `o`;
* the composed owner-coordinate residence state of the resulting linear
  chronology accepts; and
* every required upper target has a retained occurrence avoiding the cut,
  or a declared replacement occurrence,

then cutting `e` gives one protected resident upper-complete Hamilton path.
Its rooted Catalan forest is still `Q_0`; its other `C-1` short-shore edges
are the Catalan connector path.

For an exact all-width ledger, use the merger order supplied below.  Let
`A_0` be the initial source chronology, let
`A_i=z_i(A_(i-1))` be the literal source rethread certified by the `i`th
switch, and define the **sequential** occurrence change

\[
       \Delta_i(S)=\mu_{A_i}(S)-\mu_{A_{i-1}}(S).      \tag{6.3a}
\]

Let `A_(q+1)=Open_e(A_q)` be the literal accepted final linearization and
define

\[
 \Delta_{\rm open}(S)=\mu_{A_{q+1}}(S)-\mu_{A_q}(S). \tag{6.3b}
\]

The third opening bullet is exactly

\[
       \mu_{A_0}(S)+\sum_{i=1}^q\Delta_i(S)
          +\Delta_{\rm open}(S)\ge1
       \qquad\text{for every required }S.             \tag{6.3c}
\]

For a pure cut, `Delta_open(S)=-L_e(S)`, where `L_e(S)` is the number of
cyclic witnesses destroyed by the cut.  The signed form (6.3c) also covers
a typed linearization which creates declared boundary occurrences.

The increments must be sequential: deltas computed independently against
one common baseline need not telescope, even for locally disjoint switches,
because one interval may cross several supports.  A strong sufficient face
is one private witness of every `S` avoiding all merger supports and the
final cut.

Condition (6.3c) is only the final-output requirement.  If upper
completeness is required after every intermediate switch, require
`mu_(A_0)(S)+sum_(i<=j) Delta_i(S)>=1` at every prefix `j`.  If a later switch certificate
uses a named witness, hereditary applicability must retain that literal
occurrence; an anonymous positive multiplicity is not a substitute.

#### Proof

Conditions (6.2)--(6.3) say exactly that the incidence graph between old
components and merger packets is a tree.  Root it.  The first packet merges
all components in its footprint.  Every later packet meets the accumulated
component once and introduces `|e_z|-1` new components, so its maximum-
merger certificate applies.  Hereditary applicability (or disjoint complete
supports) keeps every subsequent certificate literal.  Induction leaves
one cycle.  Since only `R` incidences change, `M_0,Q_0,P` and all selected
upper representatives survive; the exported-state assertion is additive.

Cutting the typed `R_fin` edge leaves every `Q_0` representative.  Its
retained `M_0` incidence is `oS` for `S=M_0(o)`, so the owner path endpoints
are `S,V` and in fact `o subset S cap V`.  Thus `o` is the rank-`m-1`
lower-shore endpoint required by the rooted lift, not an arbitrary
nonowner.  The three displayed
opening hypotheses are respectively the source-antecedent, residence, and
all-width occurrence conditions; (6.3c) is their exact multiplicity form.
Thus the opened chronology has the stated
physical properties.  The Catalan decomposition is Theorem 2.1. \(\square\)

For binary pulls, (6.2)--(6.3) are an ordinary compatible spanning-tree
condition.  For ternary Boolean hexes they are the loose-hypertree
conditions

\[
 |\mathcal C(F)|=2|\mathcal T|+1,\qquad
 2|\mathcal A|\le|\bigcup_{z\in\mathcal A}e_z|-1.      \tag{6.4}
\]

Thus a connected ternary 2-section is insufficient, and pure ternary
fusion cannot reduce an even number of old components to one without a
binary sidecar.

### Proposition 6.2 (the exact mismatch with a bare residual factor)

The following implications are false without the added hypotheses in
Theorem 6.1.

1. A degree- and palette-exact owner factor need not have a depth-`d`
   source antecedent.
2. A graph switch avoiding `P` need not preserve residence: it may turn a
   short clipped run into an internal run at a new seam.
3. A switch preserving every immediate-upper representative need not
   preserve deeper upper targets: their unique occurrence intervals may
   traverse the changed seam.
4. Cutting an `R_fin` edge preserves `Q_0`, but it may still destroy a unique
   long upper occurrence crossing that edge.

#### Proof

Item 1 is logical: the factor constraints record only adjacent owners and
their lower/upper labels, whereas a source antecedent requires a common
ordered chain of `d+1` source letters for every owner and equality on all
overlaps.  Those equations are absent from the factor system.

For Item 2, concatenate a fragment with a short positive clipped suffix to
a fragment beginning with zero.  The suffix becomes an internal short run,
although neither fragment-internal run changed.  Lemma 3.1 identifies the
missing boundary state.

For Items 3--4, take a target having one occurrence interval crossing the
altered or opened seam and no disjoint occurrence.  The immediate-upper
representative bank says nothing about this longer interval, so its target
is lost.  This is exactly the old-occurrence hitting ledger. \(\square\)

Pairwise source-rail legality is also insufficient.  If an intervening
component contributes fewer than `d` new source positions, then the source
images of nonadjacent blocks overlap.  All letters, pins, caps and history
states assigned to every common global address must agree.  Isolated
one-owner components already exhibit this issue; therefore Theorem 6.1's
source lift is a global quotient, not a list of independent seam checks.

Accordingly, the factor-first route is useful only with a source-lifted
switch basis.  The residual Ore/LKK theorem supplies the marginal factor
and no positive lower bound on such switches; it does not imply Theorem
6.1's physical hypotheses.

The final connector edge can be typed to the pivot compiler.  Deleting it
leaves the rank-`m-1` lower target `o` without a two-owner turn.  The pivot
bank can pay that debt only if

\[
                o=R^-_{d-1}\quad\hbox{or}\quad o=R^+_{d-1},          \tag{6.5}
\]

for one of its two maximal rank-`m-1` ray cells, or if another explicit
rank-`m-1` compiler cell has literal value `o`.  The pivot singleton and the
shorter ray cells have the wrong rank.  The designated cell and transported
background must also share one cap.

The owner-edge count also does not determine physical source length.  If
component `i` exports `g_i` nonowner depth cells and consecutive source
blocks overlap in `o_i<=d` letters, then their exact source surplus is

\[
                    \sum_i g_i+\sum_i(d-o_i).                         \tag{6.6}
\]

A local `B+1` composition requires (6.6) to equal one, as well as global
address consistency.  In the direct one-credit face every internal Catalan
join has full `d`-overlap and the sole `g_i=1` cell is at a global boundary.
Immediate-upper exactness still comes from `Q_0`; deeper upper safety is
exactly (6.3c).  Thus Theorem 6.1 is an exact conditional path theorem, not
by itself a `B+1` or ambient common-cap theorem.

## 7. What is now genuinely missing

Theorem 5.1 removes three apparent extra gates:

* the protected pivot phase is unconditionally legal under (1.2);
* the rooted Catalan forest need not be extended independently once the
  Hamilton chronology is born; and
* the `C-1` connector tree is then forced by the order of that chronology.

The remaining constructive assertion is exactly the following.

> **Prepared-scaffold lemma `PCPS(m,d)`.**  For the target same-parity
> parent/child step, construct a nonflat pre-insertion word satisfying
> items 2--6 of Section 5 and the one terminal common-cap state.

Its rows must be kept distinct:

1. **integral owner/turn row:** the final owner incidence path is Hamilton
   and upper-turn-surjective;
2. **temporal row:** the `d` pre-insertion crossing cells have rank `m+1`
   and turn into the prescribed `d+1` owners;
3. **residence row:** the two clipped signatures accept;
4. **upper row:** the preword already has a complete all-width upper deck;
5. **compiler row:** the transported background plus the two rays share one
   maximal cap; and
6. **regeneration row:** the output exposes the next prepared cut.

The corrected triangular pull-clock and stationary age circulation close a
fractional marginal circulation.  They do not choose one integral owner
trace, do not impose the Hamilton/upper-turn row, and do not certify the two
residence signatures or the temporal source preimage.  Therefore they
cannot by themselves prove `PCPS(m,d)`.

Likewise, a rooted Catalan forest chosen first need not have a compatible
port Hamilton path, and a generic upper-surjective two-factor need not admit
an all-width-safe physical opening.  The prospective born-connector route
avoids both post-hoc problems, but its Hamilton scaffold is a real remaining
lemma.

The factor-first sufficient subclass has four separately missing rows:

* **PCF(`m,d`)**: an upper-exact rooted forest containing `P_1`;
* **CPH(`m,d`)**: the guarded connector Hall inequalities (6.1a);
* **CSB(`m,d`)**: a private or hereditary switch incidence tree satisfying
  (6.2)--(6.3); and
* **TOW(`m,d`)**: a globally addressed typed opening passing the composed
  owner-history residence state, (6.3c), the aperture equation (6.6), and
  the rank-`m-1` pivot endpoint-cap row (6.5).

These four rows are sufficient via Theorem 6.1 but are not necessary for
`PCPS(m,d)`: a path born prospectively need not admit a legal closing edge,
an intermediate connector cycle cover, or the chosen switch basis.

## 8. Scope

Unconditional here:

* the pivot seed for every `m>=3d+1`;
* the born-connector decomposition;
* the finite clipped-state residence test;
* all-width monotone inheritance; and
* the conditional composition Theorem 5.1; and
* the occurrence-lifted factor-first composition Theorem 6.1.

Not claimed:

* existence of `PCPS(m,d)` for all `m`;
* an all-dimensional upper-turn-surjective Hamilton path containing the
  pivot;
* a source-lifted safe-switch basis for an arbitrary Ore/LKK factor;
* a terminal common-cap/compiler for the ambient background;
* regeneration of the prepared cut; or
* `nu(k)<=B(k)+1` or `nu(k)=B(k)` beyond the authenticated finite range.
