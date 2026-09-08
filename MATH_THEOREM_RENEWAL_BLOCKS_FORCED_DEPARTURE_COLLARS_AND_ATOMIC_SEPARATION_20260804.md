# Renewal blocks, forced-departure collars, and the exact atomic separation

**Date:** 2026-08-04  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact normal forms for a fixed oriented coatom
factor.  The result gives (i) a renewal-block path criterion equivalent to
the flag-interval run automaton, (ii) a canonical accepting flag table on
every resident factor, and (iii) an exact future-intersection forcing
theorem for every right-aligned consecutive top collar.  It also gives a
rank-identical good/bad pair proving that an atomic rank histogram, owner
containment, and endpoint apertures do not determine literal
serializability.  It does not construct the required residual lower flag
bank or prove `nu(k)<=B(k)+O(1)`.

## 0. Outcome

Fix a cyclic oriented Johnson walk

\[
 Q_{i+1}=Q_i-\{\alpha_i\}+\{\beta_i\},
 \qquad |Q_i|=q=r-1,                                  \tag{0.1}
\]

and a depth `d>=2`.  Assume every positive coordinate run has length at
least `d`, no coordinate belongs to every `Q_i`, and `q>=d`.  The
non-ubiquity hypothesis is the same cyclic-run convention used in the
flag-interval serialization theorem; it is automatic for the complete
coatom-layer factors in the intended application.  The inequality `q>=d`
keeps the displayed full threshold flags nonempty and is likewise
automatic in that application.  For `0<=j<d`, put

\[
 I_{i,j}=\bigcap_{u=0}^{j}Q_{i+u}.                    \tag{0.2}
\]

Then:

1. every run automaton is equivalently a path through admissible renewal
   blocks; its last renewal is forced exactly `d` positions from the end;
2. the time-to-departure ages

   \[
   a_i^*(x)=\max\{0,d-\tau_i(x)\},                    \tag{0.3}
   \]

   where `tau_i(x)` is the remaining length of the present positive run,
   give a literal source spelling on every resident factor;
3. the resulting full flags are exactly

   \[
   F_t^i=I_{i,d-1-t},\qquad 0\le t<d;                \tag{0.4}
   \]

4. much more rigidly, in **every** literal spelling, if a right-aligned
   flag at root `Q_i` contains the consecutive top collar ranks

   \[
   q-h,q-h+1,\ldots,q
   \qquad(1\le h<d),                                  \tag{0.5}
   \]

   then its rank-`q-j` member is forced to be `I_(i,j)` for every
   `1<=j<=h`.

Consequently a collar-saturated, right-aligned flag table on this fixed
factor can be literal only if its selected roots form nested banks

\[
 R_{d-1}\subseteq\cdots\subseteq R_1,                \tag{0.6}
\]

such that

\[
 i\longmapsto I_{i,j}
 \quad\hbox{is a bijection}\quad
 R_j\longrightarrow {[k]\choose q-j}.               \tag{0.7}
\]

This is the exact dynamic collar gate missing from an atomic histogram.
The histogram fixes only the cardinalities
`|R_j|=binom(k,q-j)`; it says nothing about the simultaneous colour
bijections (0.7).

The canonical ages (0.3) prove that (0.7) is also sufficient for the
**collar part alone**: all sets in (0.7) occur at their declared literal
suffix addresses in one common spelling.  This does not solve the
coefficient-one lower deck, because the unselected canonical thresholds
have central ranks and generally create many duplicate values.  Residual
ranks below `r-d` still require noncanonical renewals co-selected with the
named targets.

## 1. Exact renewal-block normal form

Consider one positive run of one coordinate, with positions
`0,1,...,ell-1`.  Let the fixed flag/address table give an allowed age
interval

\[
 J_t=[L_t,U_t]\cap\mathbb Z\subseteq\{0,\ldots,d-1\}
 \qquad(0\le t<\ell).                                \tag{1.1}
\]

An age path starts at zero, ends at `d-1`, and at every survival step
either resets to zero or increments by one.

### Theorem 1.1 (renewal-block path criterion)

The run is accepting if and only if there are renewal positions

\[
 0=z_0<z_1<\cdots<z_s=\ell-d                       \tag{1.2}
\]

such that

\[
 z_{v+1}-z_v\le d                                    \tag{1.3}
\]

and

\[
 t-z_v\in J_t
 \quad(z_v\le t<z_{v+1}),                            \tag{1.4}
\]

while on the final block

\[
 t-(\ell-d)\in J_t
 \quad(\ell-d\le t<\ell).                            \tag{1.5}
\]

Equivalently, make a directed acyclic graph whose vertices are possible
renewal positions.  Put an arc `z->z'` when
`1<=z'-z<=d` and (1.4) holds, and put the unique kind of terminal arc from
`ell-d` to a sink when (1.5) holds.  Acceptance is exactly reachability of
the sink from zero.

#### Proof

In an age path, record precisely the positions having age zero.  Between
two consecutive such positions the age is

\[
                         0,1,\ldots,z'-z-1.
\]

It cannot reach `d`, so the gap is at most `d`.  Since the terminal age is
`d-1`, the last zero is forced to occur at position `ell-d`; any later zero
would make the terminal age too small, while an earlier last zero would
make it too large.  Membership in the fixed age intervals is exactly
(1.4)--(1.5).

Conversely, give position `t` the distance from the latest selected
renewal.  Equations (1.3)--(1.5) keep every age in
`{0,...,d-1}`, produce only reset/increment transitions, start at zero, end
at `d-1`, and respect every `J_t`.  This is an accepting path. `square`

Thus an address table does not create a hidden global state.  Its exact
effect on one coordinate is to declare which renewal blocks are locally
admissible.

### Theorem 1.2 (right-aligned age-first collapse)

Fix one literal age spelling `a_i(x)` on the oriented factor and fix a
declared flag length `m_i`, with

\[
                         c_i=d-m_i.                  \tag{1.6}
\]

There is at most one right-aligned flag of that length compatible with the
spelling.  It is

\[
 S^i_j=\{x\in Q_i:a_i(x)\le c_i+j-1\},
 \qquad 1\le j\le m_i.                              \tag{1.7}
\]

It is a strict flag precisely when the sets in (1.7) are nonempty and
strictly increasing.  Conversely, whenever they are strict, (1.7) is a
compatible right-aligned flag.

#### Proof

Right alignment declares address `c_i+j-1` for member `j`.  In any literal
age spelling, the suffix union at address `u` is exactly the age sublevel
set

\[
                         \{x:a_i(x)\le u\}.
\]

This proves uniqueness and (1.7).  If the displayed sets are strict, they
form a legal flag and marking those literal thresholds proves the converse.
`square`

Thus on the right-aligned face the order of construction can be reversed:

\[
 \boxed{
 \text{renewal positions on coordinate runs}
 +\text{ one cutoff }c_i\text{ per root}
 \Longrightarrow
 \text{the complete named flag table}.}             \tag{1.8}
\]

There is no residual choice of target names after the ages are fixed.  For
a target family `T`, define the induced occurrence deck

\[
 \mathcal D(a,c)=
 \bigl\{\{x\in Q_i:a_i(x)\le u\}:
             c_i\le u<d\bigr\}.                     \tag{1.9}
\]

Here occurrences are kept distinct, while `Val(D)` denotes their set of
distinct values.  The maximum number of distinct targets from `T` carried
by this table is exactly

\[
                         |\mathcal T\cap\operatorname{Val}(\mathcal D)|,
                                                               \tag{1.10}
\]

and its exact named deficiency is

\[
                         |\mathcal T\setminus
                           \operatorname{Val}(\mathcal D)|.
                                                               \tag{1.11}
\]

Indeed every occurrence has one functional set value, and occurrences of
different values cannot compete.  The co-selection problem is therefore
not a second target-to-flag Hall matching after ages are selected; it is the
construction of renewal positions and cutoffs whose **literal value deck**
has the required support.

## 2. The canonical time-to-departure spelling

For `x in Q_i`, let `tau_i(x)` be the number of roots in the remainder of
its current positive run, counting `Q_i` itself.  Thus `tau_i(x)=1` exactly
when `x=alpha_i`.

### Theorem 2.1 (canonical resident spelling)

If every positive run has length at least `d`, the ages (0.3) satisfy all
literal shift equations.  Their threshold flags obey (0.4), and

\[
 |I_{i,j}|=q-j\qquad(0\le j<d).                      \tag{2.1}
\]

#### Proof

An entering coordinate begins a run of length at least `d`, so its age in
(0.3) is zero.  A departing coordinate has `tau=1`, hence age `d-1`.
For a survivor,

\[
                         \tau_{i+1}(x)=\tau_i(x)-1.
\]

If `2<=tau_i(x)<=d`, its age increments by one.  If
`tau_i(x)>=d+1`, its old and new ages are both zero, so the transition is a
legal refresh.  Therefore (0.3) is a literal age spelling.

For `0<=j<d`, the future departures

\[
             \alpha_i,\alpha_{i+1},\ldots,\alpha_{i+j-1}       \tag{2.2}
\]

are distinct members of `Q_i`.  Indeed, a coordinate entering after
`Q_i` and departing by time `i+j-1` would have a positive run shorter than
`d`; the same applies to a coordinate departing twice in that interval.
Every element of `Q_i` not listed in (2.2) remains present through
`Q_(i+j)`.  Hence

\[
 I_{i,j}=Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\},     \tag{2.3}
\]

which proves (2.1).

At `Q_i`, the coordinate `alpha_(i+u)` has remaining run length `u+1`
and therefore age `d-1-u`, for `0<=u<d`.  All other coordinates have age
zero.  The coordinates of age at most `t` are consequently

\[
 Q_i-\{\alpha_i,\ldots,\alpha_{i+d-t-2}\}
 =I_{i,d-1-t},
\]

with the empty deletion list when `t=d-1`.  This is (0.4). `square`

The construction is the terminal-refresh choice in every coordinate run:
refresh at every early state, and then use the forced final block of
length `d`.

### Corollary 2.2 (exact canonical central deck)

The canonical spelling covers every target in the central collar layers

\[
 {[k]\choose r-d}, {[k]\choose r-d+1},\ldots,
 {[k]\choose r-1}                                   \tag{2.4}
\]

if and only if, for every `0<=j<d`,

\[
 \{I_{i,j}:i\in\mathbb Z_N\}
       \supseteq {[k]\choose q-j}.                  \tag{2.5}
\]

This is literal occurrence coverage in one common source word, not merely
rank coverage.  It does not assert that the other short intervals of that
word have zero duplicate waste.

## 3. Every right-aligned consecutive top collar is forced

Fix any literal depth-`d` spelling of the same oriented resident factor;
it need not be the canonical spelling.  Write its age classes at `Q_i` as

\[
 Q_i=C^i_0\mathbin{\dot\cup}\cdots
          \mathbin{\dot\cup}C^i_{d-1}.              \tag{3.1}
\]

### Lemma 3.1 (future-departure queue)

For `0<=u<d`,

\[
                         \alpha_{i+u}\in C^i_{d-1-u}.             \tag{3.2}
\]

#### Proof

The coordinate `alpha_(i+u)` is already in `Q_i` by the residence argument
in Theorem 2.1.  At `Q_(i+u)` it has terminal age `d-1`.  Trace its age
backward through the `u<d` survival steps.  A positive target age can only
come from the preceding age minus one; a reset would leave fewer than
`d-1` subsequent increments before departure.  Therefore its age at
`Q_i` is exactly `d-1-u`. `square`

### Theorem 3.2 (forced-departure collar)

Suppose a prescribed flag at `Q_i` is embedded right-aligned and its top
`h+1` members have consecutive ranks

\[
 S_{q-h}\subset S_{q-h+1}\subset\cdots
       \subset S_q=Q_i,
 \qquad |S_s|=s,\quad 1\le h<d.                     \tag{3.3}
\]

Then for every `1<=j<=h`,

\[
                         \boxed{S_{q-j}=I_{i,j}.}     \tag{3.4}
\]

#### Proof

Right alignment places the displayed consecutive top members at the
consecutive addresses

\[
                         d-h-1,d-h,\ldots,d-1.
\]

Their successive rank differences are one.  Hence every age class
`C^i_(d-h),...,C^i_(d-1)` is a singleton.  Lemma 3.1 puts the distinct
coordinate `alpha_(i+u)` in `C^i_(d-1-u)`, so

\[
 C^i_{d-1-u}=\{\alpha_{i+u}\}\qquad(0\le u<h).      \tag{3.5}
\]

The member at address `d-j-1` is therefore

\[
 Q_i-\bigcup_{u=0}^{j-1}C^i_{d-1-u}
 =Q_i-\{\alpha_i,\ldots,\alpha_{i+j-1}\}
 =I_{i,j}
\]

by (2.3). `square`

This theorem is stronger than the birth/departure aperture test.  Once a
right-aligned collar has two or more consecutive top ranks, all of its
named values are fixed by the oriented factor, not merely contained in the
same owner.

## 4. Exact dynamic collar selector

In a collar-saturated flag family, let `h_i` be the number of consecutive
top collar steps below root `Q_i`, and put

\[
                         R_j=\{i:h_i\ge j\}.          \tag{4.1}
\]

The banks are nested.  Exact use of every target at rank `q-j` gives

\[
                         |R_j|={k\choose q-j}.        \tag{4.2}
\]

### Corollary 4.1 (nested future-intersection necessity)

Every literal right-aligned collar-saturated table satisfies

\[
 i\mapsto I_{i,j}
 \quad\hbox{bijectively maps}\quad
 R_j\longrightarrow {[k]\choose q-j}               \tag{4.3}
\]

for all `1<=j<d`.

Conversely, if nested banks (4.1)--(4.3) exist, then the canonical spelling
of Theorem 2.1 contains the declared collar target `I_(i,j)` at its literal
address `d-j-1` for every `i in R_j`.  Hence the complete selected collar
bank is simultaneously serializable.

#### Proof

Necessity is Theorem 3.2 plus exact named-target use.  For sufficiency,
use (0.4) in the one canonical source word.  Nestedness ensures that the
selected members at each root form one flag, and (4.3) gives exact named
coverage. `square`

The converse is deliberately scoped to the selected collar bank.  The
canonical spelling also has unselected thresholds, and these may duplicate
central values.  Thus Corollary 4.1 is not a zero-waste residual lower-deck
theorem.

### Corollary 4.2 (the complete depth-three collar gate is ordinary Hall)

Let `d=3`.  Put

\[
 X_1={[k]\choose q-1},\qquad X_2={[k]\choose q-2},  \tag{4.4}
\]

and make a bipartite multigraph `G_Q` with one edge for every root index
`i`, joining

\[
                         I_{i,2}\in X_2
 \quad\hbox{to}\quad I_{i,1}\in X_1.                \tag{4.5}
\]

Nested banks `R_2 subseteq R_1` satisfying (4.2)--(4.3) exist if and only
if

1. the one-step intersection deck is surjective onto `X_1`; and
2. `G_Q` has a matching saturating `X_2`, equivalently

   \[
   |N_{G_Q}(Y)|\ge |Y|\qquad(Y\subseteq X_2).        \tag{4.6}
   \]

#### Proof

If the nested banks exist, the edges indexed by `R_2` use every left colour
once and distinct right colours, so they form the required matching.
Surjectivity at depth one follows from `R_1`.

Conversely, realize a matching saturating `X_2` by its distinct root
indices and call that bank `R_2`.  Its depth-one colours are distinct.  For
every right colour in `X_1` not already used, depth-one surjectivity supplies
some root having that colour.  Choose one.  Different colours have disjoint
root fibres, and none of these new roots lies in `R_2`.  Adjoining them
gives `R_1`, on which the depth-one map is bijective. `square`

Thus the dynamic central-collar selector has no hidden three-way
integrality at depth three.  The multi-coordinate obstruction begins only
when one must preserve three or more nested intersection colours on the
same selected root bank.  This statement still concerns the collar, not
the residual ranks below `r-d`.

For a fixed candidate bank, its exact named collar defect is

\[
 \Delta_{\rm col}(R_1,\ldots,R_{d-1})
 =\sum_{j=1}^{d-1}
 \left({k\choose q-j}-
       |\{I_{i,j}:i\in R_j\}|\right),               \tag{4.7}
\]

provided the sizes in (4.2) hold.  Each summand is simultaneously the
number of repeated selected occurrences and the number of missing named
targets at that rank.  The atomic capacity inequalities contain no term
which bounds (4.7): if a fixed factor/root-load choice has positive dynamic
collar defect, rearranging only its anonymous rank histogram cannot repair
that defect.

## 5. Atomic rank data do not determine acceptance

The separation already occurs in one turn at depth two.

Take

\[
 Q=\{1,2,4\},\qquad Q'=\{1,3,4\}
       =Q-\{2\}+\{3\}.                               \tag{5.1}
\]

At `Q`, use the full flag

\[
                         \{1\}\subset Q.             \tag{5.2}
\]

There are two possible full flags at `Q'`, both with the same marked rank
sequence `(2,3)`:

\[
 \mathcal G:\ \{3,4\}\subset Q',
 \qquad
 \mathcal B:\ \{1,3\}\subset Q'.                  \tag{5.3}
\]

Both choices satisfy the endpoint apertures: the departing coordinate `2`
is outside the old bottom member and the newborn `3` is inside the new
bottom member.  They also have the same roots, addresses, row loads, and
rank histogram.

For `G`, the age partitions are

\[
 C_0=\{1\},\quad C_1=\{2,4\},
 \qquad
 C'_0=\{3,4\},\quad C'_1=\{1\}.                    \tag{5.4}
\]

The survivor condition `C'_1 subseteq C_0` holds, so this turn is literal.
For `B`, one has

\[
 \widetilde C'_0=\{1,3\},\qquad
 \widetilde C'_1=\{4\},                             \tag{5.5}
\]

and `{4}` is not contained in `{1}`.  The turn is impossible.

### Corollary 5.1 (sharp local rank-only separation)

No theorem whose hypotheses retain only

* the atomic rank matrix;
* per-root loads and suffix addresses;
* root/owner containment;
* birth/departure apertures

can certify even one fixed literal flagged turn.  Named difference-block
incidence, or an equivalent renewal/intersection condition, is
indispensable.  Adding a global residence hypothesis does not alter the
local transition equation, but this two-root example by itself is not a
claim about completion to an owner-exact resident factor.

The example is sharp in the sense that changing only the name of the
rank-two target toggles acceptance while every listed rank-only datum stays
fixed.

## 6. Revised co-selection frontier

The atomic histogram theorem and the present result fit together as

\[
 \begin{array}{c}
 \text{atomic Gale--Ryser schedule}\quad
   \text{(exact rank capacities)}\\
 \Downarrow\quad\text{still requires named dynamic lifting}\\
 \text{nested future-intersection collar selector (4.3)}\\
 +\ \text{noncanonical renewal blocks for ranks below }r-d\\
 \Downarrow\\
 \text{one accepting named flag table.}
 \end{array}                                         \tag{6.1}
\]

The consecutive top collar no longer has an independent Boolean
containment choice: on the right-aligned face it is forced by the factor's
future-intersection deck.  The genuine remaining freedom lies in the
residual low ranks, where renewal blocks must be chosen together with the
named targets and the protected factor.

A sufficient all-lower theorem would now be:

> **Atomic renewal lift.**  Choose the atomic rows, named nested targets,
> their root occurrences, and renewal positions so that (i) every run
> satisfies Theorem 1.1, (ii) every selected consecutive top collar obeys
> (4.3), and (iii) all but `O(1)` physical short cells have distinct
> strict-lower values.

Together with a connected protected upper-complete factor and a safe
opening, this would give the required `B(k)+O(1)` word.  Neither the atomic
histogram theorem nor the protected unflagged two-factor theorem presently
proves this renewal lift.

## 7. Dependencies

* `MATH_THEOREM_COMPLETE_LAYER_BLOCK_TWO_CUT_NOGO_AND_ATOMIC_HISTOGRAM_MAJORISATION_20260804.md`;
* `MATH_THEOREM_FLAG_INTERVAL_RUN_AUTOMATON_AND_LITERAL_SERIALIZATION_20260804.md`;
* `MATH_THEOREM_AGE_FLAG_RUN_CRITERION_AND_FULL_FLAG_REFINEMENT_20260802.md`;
* `MATH_THEOREM_ANTICHAIN_TOP_SCD_HAMILTON_OWNER_LIFT_AND_LITERAL_AGE_GATE_20260802.md`;
* `MATH_THEOREM_JOINT_START_SURPLUS_ORBIT_LIFT_AND_NAMED_COLLAR_CHAINIZATION_20260804.md`.
