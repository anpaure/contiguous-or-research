# `k=17`: incidence-bimatching support, the five-label deletion-spine state, and exact trimmed opening

Date: 2026-08-01  
Lane: K / free-type exact-mass companion and fixed-`e55` sufficient probe on the actual `Z_17` owner quotient  
Status: unconditional equivalence and exact model reduction.  It does not
assert that the final incidence cycle or suffix-colour exact cover exists.

## 0. Verdict

Fix the authenticated 1430-position type word

```text
scratch/k17_age_type_euler_word_20260801.tsv
SHA256 e55bea5534c80560755dbc34a1f40e5cb9e67bca23e82d72caf902d2a1fd39f8
```

The physical arc/rooted-order gate admits a substantially smaller exact
normal form.

1. A lower-`q1`-rainbow quotient owner Hamilton cycle is a connected
   degree-two subgraph of the **9-regular rank-8/rank-9 incidence
   multigraph**.  The actual atlas has only `12,870` voltage-labelled
   incidences.  The former `102,960` Johnson darts are ordered pairs of
   incidences through a rank-8 orbit; `16` of them are quotient loops and
   cannot occur in a 1430-orbit Hamilton cycle.

2. Once that cycle is oriented **and passes the four-deletion spine test**,
   the next four deleted coordinates are
   forced into the four age classes.  Only five labels remain free.  At a
   position of type `c=(c_0,c_1,c_2,1)` the residual menu has exactly

   \[
       {5!\over(c_0-1)!(c_1-1)!(c_2-1)!}
   \]

   elements, at most `30`.  Over the fixed word there are exactly `5,494`
   local residual states, and `739` positions are forced.  Adjacent
   survivor inclusions and `2,424` exact suffix-orbit rows are the entire
   remaining age/lower-colour system.

3. The monodromy is the signed sum of the two incidence-matching shifts.
   A nonzero sum modulo `17` is exactly a one-cycle physical lift.

4. Rooting may be postponed.  All strict-upper witnesses have an exact
   first-growth description, with at most eight undominated witness orbits
   per quotient start.  On expanded source intervals the three appended
   wrap letters give a **3-trimmed** cyclic witness core; under the exact
   source-to-owner conversion this is precisely the ordinary owner-block
   cut core.  An upper-safe opening is therefore an exact `1430`-cut
   post-audit involving at most
   `8*1430=11,440` undominated witness orbits.

Thus a named root and a 24,310-position physical expansion are unnecessary
inside the main selector.  The remaining global row is the correlated
selection of the incidence Hamilton cycle and the rank-2 through rank-7
suffix exact cover.  No local comparator statement is used.

## 1. The actual incidence quotient

Let `G=<rho>=Z_17`.  Fix representatives `T_O` for rank-9 owner orbits
`O` and `Q_F` for rank-8 facet orbits `F`.  Both orbit sets have size

\[
             N={1\over17}{17\choose9}
              ={1\over17}{17\choose8}=1430.          \tag{1.1}
\]

An incidence is a triple

\[
             e=(O,F,s),\qquad \rho^sQ_F\subset T_O. \tag{1.2}
\]

Parallel incidences are retained.  Every owner has nine lower facets and
every facet has nine upper extensions, so this is a 9-regular bipartite
multigraph with

\[
                         9N=12870                    \tag{1.3}
\]

edges.

### Theorem 1.1 (incidence factorization)

The following objects are equivalent.

1. An oriented quotient Hamilton cycle on all rank-9 owner orbits whose
   rank-8 Johnson intersections use every rank-8 orbit once.
2. A connected spanning degree-two subgraph of the incidence multigraph,
   together with one of its two orientations.
3. Two disjoint incidence perfect matchings `D,H`, from owners to facets
   and from facets to owners, such that the permutation

   \[
                     \pi=H\circ D                    \tag{1.4}
   \]

   is one cycle on the owner orbits.

#### Proof

For consecutive owners `T_i,T_(i+1)`, their intersection `Q_i` is a
rank-8 facet incident with both.  Alternating

\[
 T_0,Q_0,T_1,Q_1,\ldots,T_{N-1},Q_{N-1},T_0
\]

gives a connected degree-two spanning incidence subgraph.  Conversely,
every connected finite degree-two graph is a cycle; its bipartition makes
it alternate between all owner and facet vertices.  The two parity classes
of its edges are the matchings `D,H`.  Orienting the alternating cycle
makes `D` the outgoing owner-to-facet matching and `H` the continuing
facet-to-owner matching, proving (1.4).  The facet vertices occur once, so
the lower colours are exactly rainbow.  `square`

At a facet orbit the two selected incidences choose the union of their two
rank-9 endpoints, hence one rank-10 upper-turn orbit.  There are

\[
              N{9\choose2}=51480                    \tag{1.5}
\]

possible local turn choices.  Requiring their `1144` rank-10 target orbits
to be covered is the exact immediate-upper row.  It is useful pruning, but
does not replace the arbitrary-width upper audit below.

### Voltage

Suppose the outgoing incidence at `O_i` is `(O_i,F_i,s_i)` and the head
incidence at the same facet is `(O_(i+1),F_i,t_i)`.  If the physical source
owner is `rho^g T_(O_i)`, their common physical facet is
`rho^(g+s_i)Q_(F_i)`.  Therefore the target phase is

\[
                  g'=g+s_i-t_i,                     \tag{1.6}
\]

and the quotient dart voltage is `v_i=s_i-t_i`.  Its total monodromy is

\[
                  V=\sum_{i=0}^{N-1}(s_i-t_i)
                    \pmod {17}.                     \tag{1.7}
\]

The physical lift has `gcd(17,V)` components.  Since `17` is prime, it is
one 24,310-owner cycle exactly when `V!=0`.

## 2. Exact nested-flag propagation

Orient a selected incidence cycle and align its physical representatives.
Write

\[
 H_i=T_i\cap T_{i+1},\qquad
 \alpha_i=T_i-H_i,qquad
 T_{i+1}=H_i+\beta_i.                               \tag{2.1}
\]

At position `i` let the prescribed type be
`c^i=(c^i_0,c^i_1,c^i_2,1)` and write the age flag as

\[
 P_i=C_{i,0}
  \subset Q_i=C_{i,0}\cup C_{i,1}
  \subset H_i=C_{i,0}\cup C_{i,1}\cup C_{i,2}
  \subset T_i.                                      \tag{2.2}
\]

The sizes are

\[
       (|P_i|,|Q_i|,|H_i|,|T_i|)
       =(c^i_0,c^i_0+c^i_1,8,9).                   \tag{2.3}
\]

The oldest class is `C_(i,3)={alpha_i}`.

### Lemma 2.1 (one-step flag criterion)

Put

\[
                         D_i=H_i-Q_i=C_{i,2}.        \tag{2.4}
\]

For the fixed oriented owner cycle, the age partitions are literal and
consistent exactly when

\[
 \begin{split}
 &|D_i|=c^i_2,\qquad \alpha_{i+1}\in D_i,\\
 &Q_i=H_i-D_i,\qquad P_i\subset Q_i,\quad |P_i|=c^i_0,            \tag{2.5}\\
 &D_{i+1}\subset Q_i-P_i,\qquad
   Q_{i+1}-P_{i+1}\subset P_i                                    \tag{2.6}
 \end{split}
\]

cyclically, with all labels compared in the same accumulated-voltage
gauge.

Concretely, if `p_(i+1)=p_i+v_i`, compare the physical flags on
`rho^(p_i)T_i`.  The last-to-first test compares the last flag with
`rho^V` times the first flag, where `V=p_N`; it is not an unshifted
diagonal test on the chosen canonical representatives.

#### Proof

The three survivor requirements are

\[
 C_{i+1,3}\subset C_{i,2},\quad
 C_{i+1,2}\subset C_{i,1},\quad
 C_{i+1,1}\subset C_{i,0}.                          \tag{2.7}
\]

Here `C_(i+1,3)={alpha_(i+1)}`, `C_(i,2)=D_i`,
`C_(i,1)=Q_i-P_i`, and `C_(i,0)=P_i`, giving (2.5)--(2.6).
Conversely, (2.5)--(2.6) give all three survivor inclusions.  The remaining
coordinates of `C_(i,0),C_(i,1),C_(i,2)`, together with `beta_i`, are
exactly the refreshed class `C_(i+1,0)` because both sides partition
`T_(i+1)=T_i-alpha_i+beta_i`.  Hence the full literal age update follows.
`square`

This already gives a small layered model.  At the `1144` positions with
`c_2=1`, `D_i={alpha_(i+1)}` is forced.  At the other `286` positions,
`c_2=2` and only the second member of `D_i` is chosen.  The number of local
`(D_i,P_i)` options is

\[
 {7\choose c^i_2-1}{8-c^i_2\choose c^i_0}.         \tag{2.8}
\]

It is at most `140`, and its sum over the fixed word is exactly `29,890`.
Without suffix-colour rows, (2.6) is an ordinary cyclic layered-path
dynamic program.

## 3. The four-deletion spine and the five-label state

The local menu contracts further before any exact-cover search.

For `0<=q<=3`, pull the future deleted label at step `i+q` back through
the accumulated quotient voltages into the gauge of `T_i`, and call it
`a_(i,q)`.  Thus `a_(i,0)=alpha_i`.

### Theorem 3.1 (deletion-spine normal form)

Every consistent age decoration satisfies

\[
             a_{i,q}\in C_{i,3-q}\qquad(0\le q\le3). \tag{3.1}
\]

Consequently the four `a_(i,q)` are distinct members of `T_i`.  Failure of
this condition at one position rules out the owner cycle independently of
all palette and upper rows.

If the condition holds, remove these four forced anchors from the four age
classes.  The remaining five labels of `T_i` are partitioned into residual
sets of sizes

\[
                    (c^i_0-1,c^i_1-1,c^i_2-1,0).    \tag{3.2}
\]

Hence the exact local residual menu size is

\[
                  n(c^i)={5!\over
                    (c^i_0-1)!(c^i_1-1)!(c^i_2-1)!}. \tag{3.3}
\]

Adjacent survivor inclusions are necessary and sufficient for these local
residual flags to form the full age decoration.

#### Proof

Equation (3.1) for `q=0` is `C_(i,3)={alpha_i}`.  For `q=1`, the next
oldest singleton survives from `C_(i,2)` by (2.7).  Iterating (2.7) twice
and three times gives `q=2,3`.  Disjointness of the age classes makes the
anchors distinct.  Removing one anchor from each class leaves (3.2), and
the multinomial count is (3.3).  Re-inserting the anchors converts the
adjacent residual inclusions back into (2.7), so Lemma 2.1 proves
sufficiency.  `square`

For type IDs `0,...,8`, the menu sizes are

\[
                         5,1,5,30,10,10,5,5,1.       \tag{3.4}
\]

Using the exact masses in the fixed word gives

\[
                         \sum_i n(c^i)=5494.         \tag{3.5}
\]

Types `1` and `8` contribute `297+442=739` completely forced positions.
The exact histogram is

```text
domain 1: 739 positions
domain 5: 511 positions
domain10: 160 positions
domain30:  20 positions
```

Each local choice emits the two still-unforced proper suffixes

\[
        C_{i,0},\qquad C_{i,0}\cup C_{i,1},          \tag{3.6}
\]

while the rank-8 suffix is already `H_i`.  Requiring every target orbit at
ranks `2,...,7` exactly once gives `2424` exact-cover rows.  Therefore,
after fixing the owner cycle, the complete age/lower inner model has one
choice among at most `30` states per layer, adjacent support clauses, and
those `2424` rows.  No fresh partition witness per arc is sound or needed.

If suffix rows are temporarily omitted, age closure is the cyclic Boolean
product of relations of width at most `30`.  If parallel dart voltages have
not yet been fixed, attach `z^v` to each relation and multiply over the
Boolean group algebra of `Z_17`; a diagonal term of nonzero total degree is
exactly a closed age trace with connected voltage lift.

### 3.1 Free-type companion (the load-bearing model)

The displayed `e55` order is one sufficient cyclic order, not a
without-loss-of-generality choice.  A negative result for its `5494`-state
model would rule out only that subclass.

For the unrestricted companion, keep the same deletion spine but allow any
of the nine certified types at every position.  The union of their local
residual menus has

\[
                       5+1+5+30+10+10+5+5+1=72      \tag{3.7}
\]

states per layer.  Choose one state at each of the 1430 positions, impose
the same adjacent survivor inclusions, the exact type masses

\[
                 (139,297,8,20,20,140,127,237,442), \tag{3.8}
\]

and the same `2424` suffix-orbit exact rows.  These conditions are necessary
and sufficient for a free cyclic type assignment with the certified
marginals.  The selected adjacent flags themselves certify every legal
type transition, so the particular 16-entry `e55` transition ledger is not
imposed.

Thus the free inner master has only `1430*72=102960` primary option
variables before compact counters and support clauses.  A global UNSAT
claim requires this free-type model (or a proved relaxation of it), whereas
the fixed-word model is a faster sufficient-subclass probe.

## 4. Exact upper tickets and the opening

This gate depends only on the oriented owner cycle and its voltages, not on
which residual age flags solve Section 3.  The reason is the exact
derivative bijection

\[
 \operatorname{OR}(A_u,\ldots,A_v)
 =\operatorname{OR}(T_u,\ldots,T_{v-3})\qquad(v-u+1\ge4), \tag{4.0}
\]

for `T_i=OR(A_i,...,A_(i+3))`.  Conversely, owner block `[a,b]` is source
block `[a,b+3]`.  Any source interval of length at most three lies in one
rank-9 owner and cannot be strict upper.  Thus (4.0) is a bijection on the
strict-upper witness families.

### Lemma 4.1 (first-growth upper tickets)

For a physical Johnson chronology

\[
                 T_{j+1}=T_j-\alpha_j+\beta_j,
\]

one has, for every cyclic interval of owners,

\[
        \bigcup_{j=a}^{b}T_j
        =T_a\cup\{\beta_a,\beta_{a+1},\ldots,\beta_{b-1}\}. \tag{4.1}
\]

For a fixed start `a`, retain the shortest endpoint at which each new
distinct coordinate outside `T_a` first appears.  These at most eight
sets are all undominated upper witnesses from that start: a longer interval
with the same union crosses every cut crossed by the shorter one.

#### Proof

Induct on `b`.  Deleting a coordinate cannot remove it from the accumulated
union, while the only possible new coordinate at the next owner is
`beta_b`; this proves (4.1).  A rank-9 starting set can gain only its eight
complementary coordinates.  Extending a fixed-start interval only enlarges
its set of crossed cut edges.  `square`

Use the indexing convention `T_i=A_i union ... union A_(i+3)`.  The owner
block `[a,b]` in (4.1) is then exactly the source interval `[a,b+3]`.
For fixed `a`, increasing `b` while keeping the same union can only enlarge
`int_3([a,b+3])`.  Hence the first-growth representatives are also
undominated for the exact trimmed opening test, not merely for ordinary
owner-edge crossings.

Thus the quotient lift has at most

\[
                              8N=11440              \tag{4.2}
\]

undominated cyclic witness orbits for all strict upper ranks.

The actual optimal linearization repeats the first `d=3` source letters.
For source intervals, the ordinary cyclic crossing test is therefore too
strong; the exact test is trimmed as follows.

For a cyclic source interval `I` and an edge `e` in its oriented interior,
let `tail_e(I)` be the number of interval vertices strictly after `e`.
Define the `d`-trimmed interior

\[
       \operatorname{int}_d(I)
       =\{e\in\operatorname{int}(I):\operatorname{tail}_e(I)>d\}. \tag{4.3}
\]

### Theorem 4.2 (exact opening criterion)

Let the source cut edge be `e_c=(A_(c-1),A_c)`.  Cut the source period
before `A_c` and form

\[
 L_c=A_c,A_{c+1},\ldots,A_{c+W-1},A_c,A_{c+1},A_{c+2}. \tag{4.4}
\]

A cyclic occurrence `I` survives in `L_c` exactly when its cut edge is not
in `int_3(I)`.  For a target `S`, put

\[
       b_3(S)=\bigcap_{\operatorname{OR}(I)=S}
                    \operatorname{int}_3(I).         \tag{4.5}
\]

If `S` has no cyclic witness, define `b_3(S)` to be the whole cyclic edge
set.  Thus an already missing target correctly forbids every opening.

Then

\[
 S\text{ survives the opening at }c
 \quad\Longleftrightarrow\quad e_c\notin b_3(S).    \tag{4.6}
\]

Consequently the opening is upper-safe exactly when

\[
             e_c\notin\bigcup_{|S|>9}b_3(S).        \tag{4.7}
\]

#### Proof

If `I` does not cross the cut, its occurrence is unchanged.  If it crosses,
the part after the cut must be supplied by the repeated prefix in (4.4),
which is possible exactly when that part has at most three vertices.  This
is the negation of membership in (4.3).  A target survives if at least one
of its witnesses survives; De Morgan's law gives (4.5)--(4.6), and
intersecting the survival requirements over all targets gives (4.7).
`square`

Let `epsilon_c=(T_(c-1),T_c)` be the corresponding owner cut.  For every
owner witness `J=[a,b]` and its expanded source witness `I=[a,b+3]`,

\[
        e_c\in\operatorname{int}_3(I)
        \quad\Longleftrightarrow\quad
        \epsilon_c\in\operatorname{int}(J).         \tag{4.8}
\]

The last owner block not crossing `epsilon_c` can require exactly the three
repeated letters.  The first owner block crossing it requires those three
plus a fourth and is lost.  Therefore `int_3` must not be applied directly
to owner intervals: the 3-trimmed **source** core is exactly the ordinary
owner-block core.  If incidence dart `i` is indexed by
`T_i -> T_(i+1)`, the source cut before `A_c` corresponds to dart `c-1`.

Let the quotient dart voltages be `v_i`, put

\[
 p_0=0,\qquad p_{i+1}=p_i+v_i,\qquad V=p_N,          \tag{4.9}
\]

and extend by `p_(i+N)=p_i+V`.  The physical lift satisfies

\[
                  T_{qN+i}=\rho^{qV+p_i}T_i.         \tag{4.10}
\]

Translation by `N` positions rotates every source interval and its target
by `rho^V`.  For `V!=0`, it cycles through all 17 physical phases.  Safe-cut
status is therefore constant on each of the `N` cut orbits.  Equivalently,
for one target-orbit representative, every witness orbit supplies a 17-bit
mask of target phases for which the proposed cut edge lies in
`int_3(I)`; the target orbit survives precisely when the bitwise
intersection of those
masks is zero.  Searching for an opening requires only the `N=1430` cut
orbits.  The full target `[17]` is automatic because the linear word
contains a complete source period.

## 5. Complete reduced certificate

The fixed `e55` type word produces the required physical decorated quotient
cycle if and only if the following finite data exist.

1. A connected spanning degree-two subgraph of the actual voltage-labelled
   rank-8/rank-9 incidence quotient.
2. An orientation and cyclic alignment of `e55` for which the deletion
   spine (3.1) holds.
3. One of the `5494` residual flag choices at each corresponding layer,
   satisfying adjacent survivor compatibility and all `2424` rank-2
   through rank-7 exact suffix rows.
4. Nonzero incidence monodromy (1.7).
5. A cut orbit passing the exact trimmed-core test (4.7).

Necessity follows from Theorems 1.1, 3.1, and 4.2.  Conversely, items 1--4
give one literal 24,310-owner age source cycle with every lower target
through rank nine.  Rank one is automatic because the fixed word has
positive `c_0=1` mass and there is only one singleton orbit.  Item 5
preserves every strict-upper target after the three-letter append.  This is
a sufficient fixed-word instance of the certificate required by
`MATH_REDUCTION_K17_CATALAN_ORBIT_AGE_DECORATED_RAINBOW_CYCLE_20260801.md`.

There are at most `2N` orientation/alignment choices for a fixed incidence
cycle.  Unless a named external socket is prescribed, the construction
should be solved unrooted and the upper-safe root selected afterward.

Replacing items 2--3 by the 72-state free-type system of Section 3.1 gives
the exact companion in which only the certified type masses, rather than
the `e55` order, are fixed.  Existence in either model is sufficient;
nonexistence in the fixed-word model has no implication for the free model.

## 6. Exact census and calibration

The independent O3 quotient census is

```text
scratch/audit_k17_age_bimatching_residual_state_20260801.cpp
SHA256 05d8f5d9b3c8c390ea2c0382b08b7697dc997634c0e20b28bc2c132fe75046d0

scratch/k17_age_bimatching_residual_state_20260801.audit.json
SHA256 b4e094277c5de2522c80421115522b5053e67c6c8ef2b8d3413eb35689607bce
status PASS_K17_AGE_BIMATCHING_RESIDUAL_STATE
```

It reconstructs from masks, rather than from a stored quotient atlas,

```text
owner orbits                         1430
facet orbits                         1430
incidences                          12870
degree on each shore                    9
ordered incidence pairs            102960
quotient-loop pairs                     16
nonloop directed Johnson darts      102944
fixed type positions                  1430
nested-flag states before spine       29890
formal five-label menu if spine passes 5494
forced local positions                 739
```

The H100 binary was compiled with
`g++ -O3 -std=c++20 -Wall -Wextra -pedantic`, a one-GiB virtual-memory cap,
one CPU, and a 60-second timeout.  Its SHA is
`155df2cbbe022cbaa6ef2fa913c28fab609c8ad3389a2c4b9712d03908443326`.

The materialized unit-voltage MMM quotient cycle is a useful negative
calibration, not a candidate for the inner oracle.  Its physical lift has
`5695=17*335` positive runs of length two and `1598=17*94` of length three.
It therefore fails the four-deletion spine before any type-word alignment
or suffix matching.  Connectivity, lower rainbow, and primitive voltage
alone are insufficient.

## 7. Sharp remaining boundary

This theorem closes neither the incidence-cycle selection nor the suffix
exact cover.  In particular, regularity of the incidence graph gives
2-factors but not a connected factor satisfying deletion-spine residence,
rank-10 turns, all deeper upper tickets, and the `2424` lower rows
simultaneously.

What is now closed is the state size and the quantifier order:

* no per-dart fresh age partition is allowed;
* no 102,960-dart primitive master is needed;
* no root need be guessed before the unrooted cycle is known; and
* source and owner opening cores must not be conflated: 3-trimmed source
  intervals equal ordinary owner-block intervals for the `B+3`
  linearization.

The next construction should select a deletion-spine-resident connected
incidence 2-factor while carrying the bounded residual flag state.  A
failure can now be certified separately as an incidence/voltage cut, a
local spine violation, a `5494`-state suffix exact-cover obstruction, or a
full `1430`-cut trimmed upper core.

Only the analogous failure of the free 72-state/type-mass companion is an
architecture-level obstruction; a `5494`-state failure is explicitly
fixed-`e55` scoped.
