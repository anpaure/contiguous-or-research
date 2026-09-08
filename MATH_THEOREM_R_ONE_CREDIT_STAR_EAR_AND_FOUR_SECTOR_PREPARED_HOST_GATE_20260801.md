# One-credit star ear: exact fan/common-cap closure and the four-sector prepared-host gate

Date: 2026-08-01  
Lane: R, additive-constant Pascal compiler  
Status: exact local theorem and exact conditional four-sector embedding.
Fan carving is characterized by a necessary-and-sufficient fan--crossing
trace condition.  The one-credit exchange additionally assumes an
independent duplicate-native bank and every collateral return.  A cyclic four-sector child preserves its
natural q1 palette and all old upper witnesses once the required coatom arc
and typed stutter cut have been planted.  Existence of those prepared hosts
in every dimension is not proved.  In fact the canonical two-sided fresh-q1
coatom glue fails the crossing/native condition already at `d=2`.  Hence
this note does not claim `nu(k)<=B(k)+O(1)`.

## 0. Verdict

The cardinality behind the proposed one-cell ear is correct but is not, by
itself, a physical construction.  One inserted source position has

\[
 2d-1\quad\hbox{fan cells},\qquad d-1\quad\hbox{destroyed crossing cells}.
\]

Two endpoint transporters have `2(d-1)` old deep-chain targets.  If an
additional prepared terminal native bank carries the `d-1` targets formerly
pinned on the destroyed crossings, the fan arms carry all old targets and
their common singleton carries one new typed target.  On this local bank the
new matching has one more edge than the old matching.  Section 4 proves that
the canonical fresh transporters do not themselves supply this native bank
for any `d>=2`.  In addition, every selected shorter crossing pin which does
not contain the star payload needs a basis-neutral return; Section 2 records
this triangular collateral exactly.

The load-bearing condition is the exact star-hidden trace identity.  Write
the two old chains as

\[
 S=O^L_0\subset O^L_1\subset\cdots\subset O^L_{d-1},\qquad
 S=O^R_0\subset O^R_1\subset\cdots\subset O^R_{d-1},
\tag{0.1}
\]

and let `N_i`, `1<=i<=d-1`, be the targets on the destroyed crossing cells.
Then the literal fan carving exists if and only if

\[
 \boxed{
 N_i\setminus S
   =(O^L_i\cup O^R_{d-i})\setminus S
       \quad(1\le i\le d-1),}
\tag{0.2}
\]

and, for every `s in S`, the zero set

\[
             \{i:s\notin N_i\}
\tag{0.3}
\]

is an interval.  Thus the two endpoint bases may be chosen freely only when
the crossing/native bank is chosen from (0.2)--(0.3).  They cannot be chosen
independently of a frozen crossing bank.

Under (0.2)--(0.3), the cap-free local word and all local pins are explicit.
With literal caps and mixed exterior rows, common-`Q` is decided exactly by
the maximal-word test in Section 3; it cannot be inferred from the local
marginals.  The remaining global theorem is a prepared-host statement: a
cyclic four-sector factor must contain a prescribed coatom incidence arc and
a collar-disjoint typed stutter cut, and its protected upper/common-cap
state must survive both.

## 1. The exact two-sided fan carving

Fix `d>=2`.  Around an inserted source position `0=*`, use the fan cells

\[
 L_j=[-j+1,0],\qquad R_j=[0,j-1],\qquad 1\le j\le d.
\tag{1.1}
\]

Thus `L_1=R_1={0}`.  The old destroyed length-`d` crossing cells are

\[
 I_i=[-i,-1]\cup[1,d-i],\qquad 1\le i\le d-1.
\tag{1.2}
\]

All cells in this note are occurrence-labelled.  Equal set values at two
different physical cells remain two different cells.

### Theorem 1.1 (literal two-sided carve)

Let `S` be nonempty, let the chains (0.1) be strict, and let
`N_1,...,N_(d-1)` be prescribed sets.  There are nonzero source letters
`A_t`, `-(d-1)<=t<=d-1`, such that

\[
 A_0=S,\qquad
 \bigcup_{t\in L_{h+1}}A_t=O^L_h,\qquad
 \bigcup_{t\in R_{h+1}}A_t=O^R_h
       \quad(1\le h\le d-1),
\tag{1.3}
\]

and

\[
                    \bigcup_{t\in I_i}A_t=N_i
                    \quad(1\le i\le d-1)
\tag{1.4}
\]

if and only if (0.2)--(0.3) hold.

More generally, if an inclusion in (0.1) is not strict, nonzero side letters
exist precisely when every empty left increment at distance `t` can be
filled by a coordinate already in `O^L_(t-1)` whose `N`-trace contains
`[t,d-1]`, and every empty right increment can be filled by a coordinate
already in `O^R_(t-1)` whose `N`-trace contains `[1,d-t]`.

#### Proof

Apply Theorem 2.1 of
`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md` with

\[
 L_{h+1}=O^L_h,\qquad R_{h+1}=O^R_h,\qquad C_i=N_i.
\]

For a coordinate outside `S`, its crossing membership is forced by the fan
first-appearance thresholds.  The frozen identity becomes exactly (0.2).
For a coordinate in `S`, copies on the old side positions do not change a
fan union, and its crossing zero set is programmable exactly when it is an
interval.  This is (0.3).

For completeness, put

\[
 X_t=O^L_t\setminus O^L_{t-1},\qquad
 Y_t=O^R_t\setminus O^R_{t-1}.
\tag{1.5}
\]

Start with

\[
 A_0=S,\qquad A_{-t}=X_t,\qquad A_t=Y_t.
\tag{1.6}
\]

For each `s in S`, realize its interval zero set by the left and right
threshold copies in the proof of the frozen theorem.  These copies do not
alter (1.3), because `s` is already present at `0`.  Equations
(0.2)--(0.3) then give (1.4).  Strictness makes every `X_t,Y_t` nonempty, so
all letters in (1.6) are nonzero.  In the nonstrict case a copied old
coordinate can fill an empty source position without changing a fan exactly
when the displayed suffix or prefix of its forced crossing trace is already
one; this gives the final criterion.  \(\square\)

### Corollary 1.2 (arbitrary bases are prospective, not frozen)

Let `B_0,B_1` be any two sets allowed at the first left and right side
positions of a prepared seam envelope, with all resulting fan values of
rank strictly below the middle rank.  They may be inserted into
`O^L_1\setminus S` and `O^R_1\setminus S`, respectively, and extended by
arbitrary strict nested increments.  This creates a legal local fan word if
each increment and programmed copy lies in its own position envelope and the
native crossing targets are then defined by (0.2), with star-coordinate
traces chosen according to (0.3).

For a fixed native bank `N`, however, a coordinate in `B_0\setminus S`
must occur in every `N_i` after its left threshold, and a coordinate in
`B_1\setminus S` must occur in every `N_i` before its right threshold.
Failure of either requirement is a one-coordinate obstruction.  Hence
“arbitrary endpoint bases and arbitrary crossing targets” is false.

#### Proof

The positive assertion is Theorem 1.1.  The negative assertion is (0.2)
coordinate by coordinate.  \(\square\)

The smallest nonlinear-looking failure is already linear in one trace.  At
`d=4`, constant fan chains cannot coexist with a nonstar coordinate whose
crossing trace is `0,1,0`; and a star coordinate with that trace has zero
set `{1,3}`, which violates (0.3).

### Theorem 1.3 (complementary coatom bases and hidden-code capacity)

Let `F={f_1,...,f_d}` and prescribe the complementary chains

\[
 O^L_h=B_L\cup\{f_1,\ldots,f_h\},\qquad
 O^R_h=B_R\cup\{f_{d-h+1},\ldots,f_d\},
 \qquad 1\le h<d,
\tag{1.7}
\]

where `F` is disjoint from `B_L union B_R`.  Put

\[
                    G=F\cup((B_L\cup B_R)\setminus S).
\tag{1.8}
\]

With unrestricted local caps, (1.7) has a common typed star `S` and
crossing targets `N_i` if and only if

\[
 \varnothing\ne S\subseteq B_L\cap B_R,\qquad
 G\subseteq N_i\subseteq G\cup S
       \quad(1\le i<d),
\tag{1.9}
\]

and every `s in S` has an interval zero trace across the `N_i`.  With
literal caps, (1.9) remains necessary and becomes sufficient exactly when
the maximal-letter test of Theorem 3.1 below passes.

If the `d-1` crossing targets are pairwise distinct, then necessarily

\[
                         |S|\ge\left\lceil{d-1\over2}\right\rceil.
\tag{1.10}
\]

The bound is sharp at the trace level.

#### Proof

Every coordinate of `B_L\setminus S` first appears at left distance one,
and every coordinate of `B_R\setminus S` first appears at right distance
one, so all belong to every crossing.  The filler `f_j` has complementary
left/right thresholds; at every crossing index at least one threshold has
been reached.  Hence every coordinate of `G` is forced into every `N_i`,
and (0.2) excludes every coordinate outside `G union S`.  Coordinates of
`S` are governed exactly by (0.3).  This proves (1.9) and its converse.

Along the crossing index, one star coordinate has trace `1^*0^*1^*` and
therefore changes at most twice.  If `n` consecutive states are pairwise
distinct, every one of their `n-1` boundaries changes a bit.  The apparent
possibility `n=2|S|+1` would use both changes of every bit and return to the
initial state, so in fact `n<=2|S|`.  Put `n=d-1` to obtain (1.10).  Sharpness
is obtained by turning all `|S|` bits off successively and then the first
`|S|-1` bits on successively.  \(\square\)

For a two-phase endpoint macro whose bases are exchanged between phases,
one phase has `(B_L,B_R)=(B_1,B_0)` and the other has `(B_0,B_1)`.  A
single typed star works in both only if

\[
                         \varnothing\ne S\subseteq B_0\cap B_1.
\tag{1.11}
\]

Thus the exact answer to “arbitrary bases inside the seam envelope” is:
the bases themselves are harmless, but their common typed part, their
forced outside bank `G`, and the native crossing code must be selected
jointly.  Empty `B_0 intersection B_1`, insufficient hidden rank (1.10), or
one failed literal cap is a complete obstruction for that cut.

## 2. Exact one-credit matching exchange

The following formulation separates the proved matching arithmetic from the
host-planting problem.

There is one further affected family besides the `d-1` destroyed cells.
For `u,v>=1` with `u+v<=d-1`, an old shorter crossing interval

\[
 I_{u,v}=[-u,-1]\cup[1,v]
\tag{2.1}
\]

remains in the short band after insertion, but its transported hull has
union

\[
                         C_{u,v}\cup S.
\tag{2.2}
\]

Thus a selected old pin on this cell transports unchanged if and only if
its target contains `S`.  Every other selected shorter crossing pin needs a
distinct terminal return and must be included in the matching-loss ledger.
This triangular-collar condition is part of common-`Q`, not a separate
marginal count.

Assume a pre-switch matching has, on a private local bank,

1. one old native cell for every `O^L_h` and every `O^R_h`,
   `1<=h<=d-1`; and
2. the crossing cell `I_i` matched to `N_i`, `1<=i<=d-1`.

Thus its local size is

\[
                         2(d-1)+(d-1)=3(d-1).
\tag{2.3}
\]

Assume throughout this section that the displayed target values
`S,O^L_h,O^R_h,N_i` are pairwise distinct.  The two terminal occurrences
of a fixed `N_i` are distinct cells carrying the same target, not two target
copies.

Assume as an additional prepared-bank hypothesis that the terminal phase has
two occurrence-labelled native copies of each `N_i`.  Only one copy is
needed by the matching.  Assume also that
the old native incidences in item 1 are absent in the terminal phase, and
that the crossing cells in item 2 are destroyed by the insertion.

Fix every exterior old matching edge throughout this comparison.  All local
old and terminal cells are source-disjoint from that exterior matching, or
their joint literal replay is part of the hypotheses.

### Theorem 2.1 (core one-credit exchange)

Suppose (0.2)--(0.3) and the envelope/trace-hit hypotheses of Section 3
hold.  Let `S` be one previously unmatched strict lower target.  Then the
terminal local matching

\[
 \begin{array}{rcl}
 O^L_h&\longmapsto&L_{h+1},\\
 O^R_h&\longmapsto&R_{h+1},\\
 N_i&\longmapsto&\hbox{one terminal native copy of }N_i,\\
 S&\longmapsto&\{0\}
 \end{array}
\tag{2.4}
\]

has size

\[
                       2(d-1)+(d-1)+1=3d-2.
\tag{2.5}
\]

All cells and all targets in (2.4) are distinct.  Relative to the retained
old matching,

\[
                  \ell=3d-3,\qquad \alpha_{\rm local}=3d-2
                         =\ell+1.
\tag{2.6}
\]

The unused second native copy of each `N_i` leaves exactly `d-1` additional
physical addresses.  They are not additional matching credits unless other
unmatched targets have legal incidences there.

#### Proof

Theorem 1.1 gives all unions in (2.4) literally.  The two arms use

\[
 L_2,\ldots,L_d,R_2,\ldots,R_d,
\]

which are `2d-2` distinct cells.  Their common singleton is the only fan
cell left and has union `S`.  The chosen native cells are disjoint from the
fan bank and from each other by occurrence labels.

All `3d-3` old local matching edges are absent after the phase change, so
deleting them gives `ell=3d-3`.  Every edge in (2.4) is then a one-edge
augmenting path: its target and its terminal cell are both unmatched in the
retained matching.  The paths are vertex-disjoint.  There are `3d-2` of
them.  On the declared local target bank no larger family exists, proving
(2.6); in a larger global graph this remains the lower bound
`alpha>=ell+1`.  The second native copies are unused and number `d-1`.
\(\square\)

Theorem 2.1 is the core-bank calculation.  It is a full local compiler
calculation only if every selected shorter crossing pin satisfies (2.2), or
if the following return condition is added.

### Corollary 2.2 (full triangular-collar one-credit criterion)

Let `R_ret` be the family of all additional old matching edges displaced by
the carrier change, including every selected shorter crossing pin which
fails the containment in (2.2), and put `r_ret=|R_ret|`.  Suppose all
members of `R_ret` have pairwise vertex-disjoint basis-neutral alternating returns.  Require
these returns to be disjoint from (2.4), require all exterior old matching
edges to remain fixed, and require the declared affected fibre to be closed:
its only newly exposed target is `S` and it has no undeclared augmenting
sink.  If the returns, (2.4), and the typed star coexist in one terminal
common-cap state, then

\[
 \ell=3d-3+r_{\rm ret},\qquad
 \alpha_{\rm local}=\ell+1.
\tag{2.7}
\]

In the unrestricted terminal graph `alpha>=ell+1`; equality there is not
claimed if further exterior augmentations exist.

#### Proof

Delete the old edges on the two chains, the destroyed bank, and the
`r_ret` displaced pins.  The fan/native assignment (2.4) restores the
first two banks, each basis-neutral return restores one collateral target,
and the singleton adds `S`.  Hence the terminal matching has exactly one
more edge than the deleted old matching.  Closedness gives the reverse
bound in the declared fibre.  \(\square\)

This is the precise meaning of the one-credit claim.  The unique fan surplus
is consumed by the typed singleton `S`; it is not simultaneously a second
free task.  The remaining `d-1` addresses come from the redundant terminal
native copy of the common new chain, exactly as in Corollary 3.1 of the
frozen star-hidden theorem.

## 3. Literal common-`Q` and nonzero conditions

Let `T^+` be the proposed terminal middle chronology.  For each source
position `p`, write

\[
 P_p=\bigcap_{p-d\le j\le p}T^+_j
\tag{3.1}
\]

with the usual clipped endpoint convention.  Extend the local letters from
Theorem 1.1 by the unchanged exterior source word.

The local rows cannot be checked after discarding their frozen exterior OR.
Let `J` be the local-position part of any selected physical row, let `T_J`
be its target, and let `E_J` be the OR of its frozen exterior positions.
Rows wholly inside the collar have `E_J=emptyset`.  Put

\[
 K_p=P_p\cap\bigcap_{J\ni p}T_J.
\tag{3.2}
\]

### Theorem 3.1 (exact maximal-word common-cap test)

There is a word of nonempty letters `A_p subseteq P_p` satisfying

\[
                 E_J\cup\bigcup_{p\in J}A_p=T_J
                 \qquad\hbox{for every selected row }J
\tag{3.3}
\]

if and only if

\[
 E_J\subseteq T_J,\qquad K_p\ne\varnothing,
\tag{3.4}
\]

for every row and position, and

\[
                 T_J=E_J\cup\bigcup_{p\in J}K_p
                 \qquad\hbox{for every }J.
\tag{3.5}
\]

When feasible, `A_p=K_p` is the unique componentwise maximal word.

#### Proof

Any feasible `A_p` is contained in `P_p` and in every target row containing
`p`, hence `A_p subseteq K_p`.  This gives one inclusion in (3.5); the
definition of `K_p` gives the other.  Nonempty letters force
`K_p!=emptyset`.  Conversely (3.4)--(3.5) say directly that the maximal word
`A_p=K_p` is nonzero, cap-legal, and realizes every target.  \(\square\)

For the wholly local fan/crossing rows this specializes to

\[
\begin{aligned}
 K_0={}&P_0\cap S\cap\bigcap_{h=1}^{d-1}O^L_h
                    \cap\bigcap_{h=1}^{d-1}O^R_h,\\
 K_t^-={}&P_{-t}\cap\bigcap_{i=t}^{d-1}N_i
                       \cap\bigcap_{h=t}^{d-1}O^L_h,\\
 K_t^+={}&P_t\cap\bigcap_{i=1}^{d-t}N_i
                      \cap\bigcap_{h=t}^{d-1}O^R_h
             \qquad(1\le t<d).
\end{aligned}
\tag{3.6}
\]

The exact reconstruction equations are

\[
\begin{aligned}
 S&=K_0,\\
 O^L_h&=K_0\cup\bigcup_{t\le h}K_t^-,\\
 O^R_h&=K_0\cup\bigcup_{t\le h}K_t^+,\\
 N_i&=\bigcup_{t\le i}K_t^-\cup
      \bigcup_{t\le d-i}K_t^+.
\end{aligned}
\tag{3.7}
\]

All `K`-sets in (3.6) must be nonempty.  For a mixed row one must instead
use its actual `E_J` in (3.5); replacing it by a wholly local equality is
unsound.

### Corollary 3.2 (exact typed-star row)

Freeze all nonstar source letters.  For every star-containing carrier window
and protected pin `J`, let `U_J` be its nonstar union and `T_J` its required
target.  Put

\[
 M_*=\bigcup_J(T_J\setminus U_J),\qquad
 P_*^{\rm all}=P_0\cap\bigcap_JT_J.
\tag{3.8}
\]

The singleton can be the typed target `S` while preserving every such row
if and only if

\[
 U_J\subseteq T_J\quad\hbox{for every }J,\qquad
 M_*\subseteq S\subseteq P_*^{\rm all},\qquad S\ne\varnothing,
\tag{3.9}
\]

where `M_*` may be empty; only `S` must be nonempty.  For a target common to
two terminal phases, use the union of their mandatory sets and the
intersection of their upper caps.

#### Proof

At each row the star must supply every coordinate missing from `U_J` and
must introduce no coordinate outside `T_J`.  Intersect these lower and upper
requirements over all rows.  \(\square\)

### Corollary 3.3 (explicit prepared-host sufficient condition)

The local one-credit exchange is a literal terminal compiler block provided
that:

1. `A_p subseteq P_p` at every changed source position;
2. every coordinate of every affected middle owner is hit by at least one
   of its `d+1` source positions, so `D^dA=T^+` there;
3. every other selected lower pin is collar-disjoint, direct replay shows
   that its union is unchanged, or it is restored by one of the
   basis-neutral returns in Corollary 2.2; and
4. the terminal native occurrences used in (2.4) are pairwise distinct,
   have literal union `N_i` in this same source word, and are source-disjoint
   from the fan collar and the fixed exterior matching, unless their joint
   overlap has been replayed explicitly.

Under these conditions the full terminal pin table has a common nonzero
source word.  In particular it has neither a positive-cover core nor an
empty-position core from Theorem 5.1 of
`MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`.

#### Proof

Theorem 1.1 explicitly assigns every changed nonzero source letter and
computes every local target union.  Items 1--2 say that the same letters
give exactly the declared terminal middle row.  Item 3 preserves every
other selected lower witness, and item 4 preserves injectivity.  Therefore
the displayed global source word itself realizes all central and lower
positive requirements and is nonempty at every position.  This is stronger
than the existential common-`Q` test, so neither obstruction core can
occur.  \(\square\)

Equivalently, one may verify the maximal-word equalities (3.4)--(3.5)
directly.  The envelope condition cannot be weakened to `S subseteq P_0`.
Every side
increment and every extra copy used to program (0.3) must lie in its own
position envelope.  This is the exact place where a prospective seam code
may fail in a frozen carrier.

### Corollary 3.4 (literal `B(k)+1` consequence)

Assume:

* before the local exchange, the compiler matching covers every strict
  lower target except `S`;
* the hypotheses of Corollary 2.2 and either Theorem 3.1 or Corollary 3.3
  hold;
* `T^+` has length `W+1`, contains every middle owner, and is
  upper-complete and depth-`d` resident.

Then there is a universal word of length

\[
                         W+d+1=B(k)+1.
\tag{3.10}
\]

#### Proof

Corollary 2.2 augments the lower matching by one and Section 3 realizes it
in one nonzero common-cap word.  The middle and upper hypotheses are exactly
items 1--2 of the one-cell seam-credit theorem.  Apply Theorem 6.1 of the
stutter/compiler note.  \(\square\)

No asymptotic conclusion follows until the prepared-host hypotheses are
constructed in a dimension-uniform Pascal child.

## 4. Fresh-q1 endpoint transporters at a protected opening

The q1 row is separate from the deep fan count.  The `2(d-1)` fan targets
are the `q>=2` chain values.  A rank-`(m-1)` B1 hole cannot occupy the
singleton while both chains are strict: every fan target contains the star
letter, whereas the first deep target has rank at most `m-2`.

There is nevertheless no local owner or q1-palette collision in preparing
the two fresh endpoint blocks.

Let the child ground set have size `2m-1`, let owners have rank `m`, and
assume `m>=d+4`.  Protect a q1 edge

\[
 A=Q\cup\{\alpha\},\qquad B=Q\cup\{\beta\},\qquad A\cap B=Q.
\tag{4.1}
\]

Choose distinct

\[
                    u,v\in\Gamma\setminus(A\cup B).
\tag{4.2}
\]

This is possible because the outside bank has size `m-2`.  For the left
fresh transporter, take the formal role `b_L=alpha`, choose the roles
`infinity,c,a,x,f_1,...,f_(d-1)` in `Q`, put the remaining `m-d-4`
members of `Q` in its fixed core, and take `f_0=u`.  Its coatom support is

\[
                         H_L=A\cup\{u\}.
\tag{4.3}
\]

The first owner is `A`, and one length-`d` alternative is `Q`.  Reverse the
construction at `B`, using the formal role `b_R=beta` and exterior label
`v`, to obtain support

\[
                         H_R=B\cup\{v\}.
\tag{4.4}
\]

### Lemma 4.1 (local occurrence and palette separation)

The two coatom owner blocks are disjoint.  Their internal q1 colours are
pairwise distinct across the two blocks and are distinct from `Q`.

#### Proof

By (4.2),

\[
                           H_L\cap H_R=Q.
\]

A common rank-`m` owner would be contained in their rank-`(m-1)`
intersection, impossible.  Every left internal coatom intersection contains
`alpha`, which is absent from `H_R`; every right internal intersection
contains `beta`, which is absent from `H_L`.  The opening colour `Q`
contains neither.  Consecutive omitted pairs within one coatom path are
different, so its internal colours are distinct.  \(\square\)

Thus a terminal q1-rainbow carrier may contain the prescribed segment

\[
 T_d^L-\cdots-T_1^L-A-B-T_1^R-\cdots-T_d^R
\tag{4.5}
\]

without a local collision.  The two fresh length-`d` cells are two physical
occurrences capable of carrying the one B1 target `Q`; a matching uses only
one.  This is the local endpoint interface of Corollary 2.6 of the
exterior-ear note and Corollary 3.2 of the q1-sidecar note.  It does not
identify their `q>=2` terminal chains with the crossing bank of Theorem 2.1.

### Theorem 4.2 (canonical endpoint chains do not repay the crossings)

Take the complementary canonical chains, with `G,{a},{b},F` pairwise
disjoint and `|G|+d+2=m`,

\[
 O^L_h=G\cup\{b\}\cup\{f_1,\ldots,f_h\},\qquad
 O^R_h=G\cup\{a\}\cup\{f_{d-h+1},\ldots,f_d\},
 \qquad S\subseteq G.
\tag{4.6}
\]

Then every compatible crossing satisfies

\[
       \{a,b,f_1,\ldots,f_d\}\subseteq N_i
       \qquad(1\le i<d).
\tag{4.7}
\]

No target in a canonical phase-swapped new prefix or suffix chain contains
both active labels and the complete filler bank.  Consequently no destroyed
crossing cell is a canonical `NEW` target, already when `d=2`.  A one-credit
implementation needs an independent native/cross-packet bank whose
variation is encoded only by interval-zero traces inside `S`, or a
noncanonical transporter.

#### Proof

For crossing `i`, the left fan contributes `b,f_1,...,f_i` and the right
fan contributes `a,f_(i+1),...,f_d`.  Equation (0.2) gives (4.7).  Hence
all crossing targets contain both active labels and the complete filler
bank.  In the literal canonical endpoint sources they also contain all of
`G`, so all equal the full rank-`m` set
`U=G union {a,b} union F`.  They are not strict lower targets.  The
star-spanning diagonal owners are likewise all `U`; for `d>=4` their
multiplicity excess is at least two, incompatible with an owner-complete
chronology of length `W+1`.  A canonical terminal prefix target omits one active label
and a filler suffix; a canonical suffix target omits the other active label
and a filler prefix.  Thus equality is impossible for every `d>=2`.  When
`d>=3`, Theorem 1.3 additionally forces all variation among distinct
crossings to lie in `S`.
\(\square\)

### Theorem 4.3 (one-chain asymmetric phase selector)

The obstruction is genuinely two-sided.  Let `C` be nonempty,
`B_0=C union {a}`, `B_1=C union {b}`, and
`F_i={f_1,...,f_i}`.  In phase `epsilon`, set

\[
 A_0=B_\epsilon,\quad A_{-t}=C\cup\{f_t\},\quad
 A_{+1}=B_{1-\epsilon},\quad A_{+t}=C\ (t\ge2).
\tag{4.8}
\]

Then, for `1<=i<d`,

\[
 C_i=B_{1-\epsilon}\cup F_i,\qquad
 L_{i+1}=B_\epsilon\cup F_i,
\tag{4.9}
\]

while every right nonsingleton fan has the one value `B_0 union B_1`.
Thus one fan carries a complete native `NEW` prefix chain and the destroyed
bank carries the opposite-phase `OLD` prefix chain; all right-fan addresses
are physically unused by these assignments.  A source-disjoint endpoint
carve may supply the opposite family in the same terminal state, conditional
on literal carrier/common-cap replay.

#### Proof

Every crossing contains `+1`, hence `B_(1-epsilon)`, and its first `i` left
positions contribute exactly `F_i`; the other positive-side letters add
only `C`.  The left fan contains the star `B_epsilon` and the same filler
prefix.  Formula (4.9) follows.  \(\square\)

This is a phase-specific one-chain construction, not the desired
two-chain packet: the right target-value menu has rank one, and the two
phases may require different source words and matchings.

Lemma 4.1 is not an extension theorem.  A fixed q1-rainbow cycle containing
only the edge `AB` need not contain the whole segment (4.5).  After the
internal owner vertices and the lower-colour vertices used by the incidence
lift of (4.5) are deleted from the middle-levels incidence graph, retain the
two exposed endpoint owners as degree-one ports.  The residual graph must
have a spanning alternating port-to-port path.  This relative Hamilton-path
condition is necessary and sufficient for extending the prescribed segment
to a q1-rainbow cycle.  No theorem currently cited here proves it in every
dimension.  The protected-q1 Hamilton extension theorem gives an explicit
`J(5,3)` q1-rainbow two-factor with four protected edges for which every
q1-rainbow extension still has two 5-cycles.  Thus even an absolute protected
bank does not make this rooted target automatic; the present coatom segment
needs its own relative-Hamilton certificate.

## 5. Four-sector planting theorem and exact remaining obstruction

Call a cyclic four-sector child **one-ear prepared** if it has all of the
following occurrence-labelled data.

1. Before the one equality stutter is inserted, it is a q1-rainbow cyclic
   owner cycle and contains the complete prescribed coatom segment (4.5),
   not merely its middle edge.  Equivalently, contracting the equality step
   in the terminal chronology recovers this cycle.
2. Its terminal owner order has length `W+1`, contains every middle owner,
   and is upper-complete with a declared witness for every upper target.
3. At a collar-disjoint source cut it admits one equality stutter of an
   owner `U`, together with a typed star target `S`, chains (0.1), and native
   values `N_i` satisfying (0.2)--(0.3).
4. The source envelopes and positive hits satisfy Theorem 3.1, and the
   independently prepared native occurrences give the phase interface of
   Theorem 2.1.  This is an additional bank, not a consequence of the two
   canonical endpoint transporters.  Every incompatible shorter crossing
   pin has a basis-neutral return as in Corollary 2.2, and the affected
   fibre is closed.  All pairwise-distinct target/cell, old-edge-absence,
   and fixed-exterior-baseline hypotheses of Section 2 are in force.
5. Every declared upper witness altered by planting (4.5) has been replayed
   in the terminal order.  The equality-stutter itself needs no new upper
   check.
6. The terminal diagonal owners and joins are valid occurrence-labelled
   owners, and the complete chronology, including the endpoint blocks and
   stutter collar, is depth-`d` resident.

### Theorem 5.1 (conditional four-sector one-ear embedding)

Every one-ear prepared child has a physical one-credit compiler macro.  Its
strict natural q1 palette is unchanged by the stutter, every old upper
witness survives the stutter, and its lower matching gains one.  If the
outside compiler was one-deficient exactly at `S`, the child has a literal
word of length `B(k)+1`.

#### Proof

The endpoint part is Lemma 4.1 and the fresh-q1 transporter theorem.  At the
star, duplicating `U` leaves the two old Johnson transitions in place and
adds one equality transition.  The equality has intersection `U` of rank
`m`, so it contributes no rank-`(m-1)` q1 colour.  Hence the strict q1
palette is unchanged.

If an old upper witness crosses the duplicated occurrence, include both
copies of `U`; its union is unchanged.  Witnesses avoiding that occurrence
are untouched.  Item 5 handles the separate issue of witnesses changed
while the prescribed endpoint arc was planted.

The fan/common-cap and matching conclusions are Theorem 1.1, Corollary 2.2,
and Section 3.  The last statement is Corollary 3.4.  \(\square\)

The same proof permits `H=O(1)` pairwise collar-disjoint ears.  Their source
supports must be separated enough that no short pin meets two collars, or
all such pins must be replayed jointly.  Their prescribed owner/q1
occurrences must also be disjoint.  Under those explicit conditions the
ear ledgers add and one global literal word certifies common-`Q`.

The canonical two-sided fresh-q1/coatom glue is not one-ear prepared:
Theorem 4.2 shows that it fails item 4 already at `d=2`, before the relative
Hamilton, residence, upper, or global compiler rows are reached.  Therefore
Theorem 5.1 is a noncanonical conditional route, not a `B(k)+1` result for
the current four-sector child.

### Proposition 5.2 (exact extra prepared-host rows)

The conclusions presently supplied by owner completeness, cyclic q1
injectivity, and upper completeness do not contain the following additional
prepared-host rows:

1. the relative Hamilton-path extension of (4.5);
2. a collar-disjoint source cut with the per-position envelopes required by
   Theorem 3.1;
3. the coupled trace identities (0.2)--(0.3), with the native bank `N`
   selected jointly rather than afterward; and
4. basis-neutral returns for every incompatible shorter crossing pin;
5. valid, owner-simple diagonal windows and terminal residence; and
6. terminal replay of upper witnesses affected by the endpoint-arc
   rethread.

In particular, a frozen four-sector native bank violating (0.2) at one
coordinate cannot be repaired by changing only the star payload.  A star
coordinate can alter its crossing trace only through an interval zero set,
so violation of (0.3) is equally final for that cut.

#### Proof

The necessity of items 2--3 is Theorems 1.1 and 3.1, and item 4 is the
triangular identity (2.2).  Item 1 is the exact
translation of a q1-rainbow cycle with a prescribed alternating incidence
segment.  Item 6 is necessary because local palette separation does not
preserve an arbitrary old interval after a global rethread.  The `d=4`
trace examples after Corollary 1.2 prove that arbitrary fan/crossing data do
not satisfy the local source-trace condition.  They are not asserted to be
complete four-sector counterexamples.  \(\square\)

Thus the strongest proved conclusion is conditional but constructive.  The
one-cell ear is no longer missing a counting, integrality, or local
common-`Q` argument.  The exact all-dimensional gate is a **prepared
occurrence host** satisfying the relative q1 path, star-trace, envelope, and
protected-upper rows simultaneously.

## 6. Adversarial audit and scope

The decisive steps were checked independently against the frozen
star-hidden trace theorem and the explicit fresh-q1 antecedents.

1. The identity is `N_i\S=(O^L_i union O^R_(d-i))\S`; the right index is
   `d-i`, not `d-1-i`.
2. The two chains use exactly `L_2,...,L_d,R_2,...,R_d`.  The common
   singleton is the only fan surplus.
3. Assigning `S` to that singleton consumes the surplus.  The remaining
   `d-1` unused addresses are the redundant second copies in the separately
   prepared native bank; they are not extra matching gains without targets.
4. Strict fan chains make the canonical source letters nonzero.  For
   nonstrict chains the prefix/suffix trace condition in Theorem 1.1 is
   necessary; nonzero cannot be inferred from set inclusion alone.
5. A B1 q1 hole of rank `m-1` cannot be put at the singleton while strict
   `q>=2` chains use both arms.  It is carried by the fresh endpoint bank (or
   by a separately proved q1 alternating linkage), not by the typed deep
   socket.
6. Protecting one q1 edge does not protect the `2d+1`-edge segment (4.5).
   The latter is an explicit hypothesis.
7. Repeating an owner preserves all old upper interval unions.  This says
   nothing about a different global owner rethread used to plant the
   endpoint arcs; those witnesses must be audited separately.
8. For the canonical complementary coatom chains, every crossing contains
   the full outside bank `a,b,f_1,...,f_d`.  Therefore the varying canonical
   new endpoint chains cannot be the required duplicate native bank, already
   at `d=2`.
9. Mixed exterior rows must retain their fixed OR contribution `E_J`; the
   exact test is (3.4)--(3.5), not the cap-free trace criterion alone.
10. Every selected shorter crossing pin not containing `S` needs a return;
    omitting this triangular bank invalidates the `ell/alpha` count.
11. The local exact checker
   `scratch/audit_one_cell_star_hidden_fan_trace_20260801.py` was rerun and
   returned

   ```text
   PASS_ONE_CELL_STAR_HIDDEN_FAN_TRACE 767150
   ```

    The triangular-collar and phase-selector audits were also rerun and
    returned

    ```text
    PASS_K_ONE_CELL_TYPED_STAR_TRIANGULAR_COLLAR d=2..40
    PASS_THREADD_ONE_CELL_STAR_PHASE_SELECTOR_EXACT_GATE
    ```

No SAT solver, remote computation, web source, or finite K16/K17 search is
used in this note.
