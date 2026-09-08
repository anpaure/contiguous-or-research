# One spare serializes basis exchange, not compiler augmentation

Date: 2026-08-01  
Status: exact fixed-common-cap matching theorem, exact all-cut ceiling for the
one-cell seam, and sharp counterexamples.  The result does **not** prove the
missing exterior-provider Hall inequality or `nu(k) <= B(k)+O(1)`.

## 0. Outcome

There are three different uses of an empty physical compiler cell.

1. A closed alternating cycle changes assignments on one fixed cell basis.
   The returned-catalyst router can serialize these cycles.
2. An alternating path between two matchings of the same size moves the empty
   cell.  Under a strict Hall condition, one empty cell can be moved through
   the entire fixed-cap matching fibre.
3. An augmenting path increases matching rank.  Its terminal cell is consumed.
   A net gain of `h` requires `h` **distinct cells which were unused in the
   initial matching**, regardless of how the moves are serialized.

The fresh-q1 endpoint transporter belongs to item 2: it changes the target
carried by the same physical length-`d` cell.  The returned catalyst belongs
to item 1.  Their composition cannot supply item 3.

For an odd-dimensional flat compiler the q1 row has `W+1` physical cells for
`W` q1 targets.  Its unique spare can therefore move a q1 matching basis, but
as an exterior-ear sink it has strict-gammoid rank at most one.  For two
source tasks the sharp all-cut defect may already be one, even when either
task is individually routable.

The one-cell interval identity is the first available operation which could
change this count.  **Conditional** on a phase selector which repays the
`d-1` destroyed crossing pins at native cells and matches both old chains on
the fans in one cap state, using the typed singleton leaves `d-1` additional
physical addresses.  Consequently such a selector has residual exterior-ear
rank at most `d-1`, and the exact remaining condition is

\[
 \boxed{\delta_{\rm seam}(U)=
   \max_{X\subseteq U}\bigl(|X|-r_{\mathcal M_\theta}(P_X)\bigr),
   \qquad r_{\mathcal M_\theta}(P_X)\le d-1.}               \tag{0.1}
\]

Here `theta` is one fixed legal complete cap state.  The star-hidden fan
theorem proves the interval identity and the typed edge once its forced-mask
test passes; it does not prove the assumed native repayment or any residual
provider edge.  Indeed, the canonical complementary coatom/twisted-cube
OLD-fan/NEW-crossing selector is trace-infeasible.  In the carrier-valid
local normal form its destroyed crossing targets are the incomparable coatoms

\[
             C_i=\{x\}\cup(F-\{f_{i+1}\}),                 \tag{0.2}
\]

so the direct nested-fan return is impossible.  A genuinely nonlocal
provider bank is still required.

The positive consequence is a quantifier reduction.  If a regenerative
induction already maintains at most an absolute `H` source tasks, then one
seam has enough *cardinality* for all of them once `d-1>=H`.  The missing row
is only the bounded-source common-state Hall condition, not a large-source
near-isometry.  Cardinality alone, however, supplies no such condition.

## 1. Fixed-cap matching notation

Fix one legal complete cap state `theta`.  Let

\[
                     G_\theta=(L,C;E)                       \tag{1.1}
\]

be its literal target-to-physical-cell incidence graph.  Every edge in
`G_theta` is already trace guarded and coexists with all protected rows of
`theta`; taking a union over different cap states is not allowed.

For a matching `M`, write

\[
                Q(M)=\{c\in C:c\hbox{ is used by }M\}.       \tag{1.2}
\]

A closed quadratic packet changes `M` on an alternating cycle and preserves
`Q(M)`.  An open alternating path between equal-size matchings replaces one
cell of `Q(M)` by one cell outside it.  An augmenting path increases both
`|M|` and `|Q(M)|` by one.

## 2. Exact one-spare exchange theorem

Assume `|C|=|L|+1` and let `M` saturate `L`.  Denote its unique unused cell
by `s`.  Form the **exchange digraph** `D_M` on `C` by putting an arc

\[
 c\longrightarrow M(u)
 \quad\Longleftrightarrow\quad uc\in E, c\ne M(u).          \tag{2.1}
\]

An arc means that, when `c` is empty, target `u` may move from its current
cell `M(u)` into `c`, making `M(u)` the new empty cell.

### Theorem 2.1 (reachability of the spare)

For `t in C`, the following are equivalent.

1. There is an `M`-alternating path from the spare `s` to `t` whose flip is
   another `L`-saturating matching.
2. `t` is reachable from `s` in `D_M`.

Let `R` be this reachable cell set and `U=C-R`.  If `U` is nonempty, then

\[
 Y=M^{-1}(U)\quad\hbox{satisfies}\quad N(Y)=U,qquad |N(Y)|=|Y|.  \tag{2.2}
\]

Conversely, every nonempty `Y subseteq L` with

\[
             |N(Y)|=|Y|,qquad s\notin N(Y)                  \tag{2.3}
\]

is sealed from the spare: no cell of `N(Y)` is reachable from `s`.

Consequently the spare reaches every physical cell if and only if

\[
 \boxed{|N(Y)|\ge |Y|+1\qquad
        (\varnothing\ne Y\subseteq L).}                     \tag{2.4}
\]

#### Proof

A directed walk

\[
 s=c_0\to c_1\to\cdots\to c_j=t
\]

records targets `u_i` with `M(u_i)=c_i` and `u_i c_(i-1) in E`.
Moving these targets in reverse order is exactly an alternating-path flip;
the empty cell moves from `s` to `t`.  The converse reads any such path in
the same way.  This proves the first equivalence.

Every cell in `U` is matched because `s in R`.  Put `Y=M^(-1)(U)`, so
`|Y|=|U|`.  If `u in Y` had a neighbour `c in R`, (2.1) would make `M(u)`
reachable, a contradiction.  Hence `N(Y) subseteq U`; the matching gives
the reverse cardinality inequality, so equality holds.  Conversely, a
matching saturating a tight set `Y` uses every cell of `N(Y)`.  No
alternating path starting outside `N(Y)` can enter it without leaving an
unmatched cell inside, which tightness forbids.  Equivalently, the first
arc entering `M(Y)` would originate at a neighbour of `Y` outside `N(Y)`.
This proves (2.2)--(2.3), and (2.4) follows.  \(\square\)

Condition (2.4) is the exact all-cut theorem for **moving one spare inside a
saturated fixed-cap fibre**.  It is stronger than ordinary Hall by one unit.

### Corollary 2.2 (all equal-rank basis changes are serializable)

Assume (2.4).  Let `M'` be any other matching saturating `L`.  Then `M` can
be changed into `M'` inside the same state `theta` by one alternating path
(if their spare cells differ) and a collection of alternating cycles.  The
path moves the spare; the cycles preserve its location.

If every cycle has a physically certified returned-catalyst route and every
path edge has a physically certified endpoint-transporter route, the same
decomposition is a literal serial carrier route.  After every path flip the
underlying graph `G_theta` still satisfies (2.4), so the spare can be moved
again.

#### Proof

The symmetric difference of two left-saturating matchings has degree zero
or two at every target.  It is therefore a disjoint union of alternating
cycles and, when the two spare cells differ, one alternating path between
them.  Flip its components.  The physical statement is exactly the stated
certification hypothesis.  \(\square\)

This is the strongest correct “one movable spare is reusable” statement.
It concerns equal-cardinality bases.

## 3. Net rank gain consumes exterior cells

### Theorem 3.1 (exterior-cell conservation)

For arbitrary matchings `M^-` and `M^+` on the same cell shore,

\[
 \boxed{|Q(M^+)\setminus Q(M^-)|
          \ge |M^+|-|M^-|.}                                 \tag{3.1}
\]

In particular, if the terminal compiler rank improves by `h`, its symmetric
difference with the initial matching contains `h` vertex-disjoint augmenting
paths ending at `h` distinct initially unused cells.  No serialization of
closed cycles or equal-rank spare moves can reduce this number.

#### Proof

Since a matching uses one distinct cell per edge,

\[
 |M^+|-|M^-|=|Q(M^+)|-|Q(M^-)|
 =|Q(M^+)\setminus Q(M^-)|-|Q(M^-)\setminus Q(M^+)|,
\]

which implies (3.1).  The standard symmetric-difference decomposition has
exactly the matching-size difference in augmenting path components, and
their terminal cells are distinct.  Closed cycles and balanced paths have
zero contribution to the size difference.  \(\square\)

### Corollary 3.2 (one-spare rank ceiling)

Suppose the only physically certified old-unused endpoint is one q1 spare
`s`.  Then every terminal route built from

* fixed-basis quadratic/catalyst cycles,
* equal-rank fresh-q1 endpoint transports, and
* open paths ending at `s`

has compiler-rank gain at most one.  If the spare is returned unused, the
gain is zero.

Equivalently, a strict gammoid with one sink has

\[
       r_{\mathcal M}(P_X)\le\min\{|X|,1\},qquad
       \max_X(|X|-r_{\mathcal M}(P_X))\ge(|U|-1)^+.          \tag{3.2}
\]

Thus one q1 spare cannot prove the exterior-ear contraction inequality for
an unbounded source set.

The bound is sharp.  Give each task a private entrance and a private path to
one final cut vertex `s`.  Every task is individually routable, but no two
paths can be vertex-disjoint and no two net augmentations can both consume
the same terminal cell.

## 4. Exact implication of the one-cell fan seam

Use the typed seam of

`MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`.

Its two fans have `2d-1` cells.  The two old-only coatom chains occupy
`2(d-1)` of them.  The common singleton star is the one remaining fan cell.
When it is assigned one hard task, and the `d-1` destroyed crossing pins are
repaid at native new-phase cells, exactly `d-1` other old addresses become
unused.  Let this address set be `F_*`.

Fix one legal complete terminal cap state `theta` containing the literal fan,
native and star assignments.  For each residual source task `u`, let `P_u`
be its physically certified entrances into a directed return network ending
at `F_*`.  The network may use returned catalysts and closed occurrence
cycles, but every nonreturning resource and every cap/trace guard is a
vertex of the network.  Let `M_theta` be its strict gammoid.

### Theorem 4.1 (sharp seam rank formula and ceiling)

The maximum number of additional source tasks simultaneously repairable in
the same cap state is

\[
 \min_{X\subseteq U}\bigl(|U-X|+r_{\mathcal M_\theta}(P_X)\bigr),
 \qquad P_X=\bigcup_{u\in X}P_u,                             \tag{4.1}
\]

and the exact residual is (0.1).  Moreover,

\[
 \boxed{r_{\mathcal M_\theta}(P_X)
        \le\min\{|X|,d-1\}.}                                \tag{4.2}
\]

If all internal route resources are returned/private and the only
competition is at the addresses `F_*`, (4.1) reduces to ordinary Hall in
the bipartite provider graph

\[
                 H_\theta\subseteq U\times F_*              \tag{4.3}
\]

and

\[
 \delta_{\rm seam}(U)=
       \max_{X\subseteq U}(|X|-|N_{H_\theta}(X)|)^+.         \tag{4.4}
\]

#### Proof

Equation (4.1) is Rado's transversal theorem for the entrance sets in the
strict gammoid.  The sink bank has size `d-1`, so every vertex-disjoint path
family has size at most `d-1`, proving (4.2).  Under the stated privacy
hypothesis, choosing disjoint routes is equivalent to choosing distinct
terminal addresses, which is exactly matching in (4.3); Hall's deficiency
formula gives (4.4).  \(\square\)

The ceiling is attainable in the abstract: take `d-1` sinks and give every
task a private entrance to every sink.  Then

\[
                r(P_X)=\min\{|X|,d-1\}.                     \tag{4.5}
\]

It is also possible for the seam rank to be zero: make every fixed free cap
omit one coordinate required by every residual task.  Hence the address
count alone gives no positive rank lower bound.

### Corollary 4.2 (the exact remaining provider theorem)

Once the four hypotheses of the exact phase-selector theorem hold, the
one-cell seam plus endpoint-chain carving proves one rank gain—the typed
star task—and enough endpoint *cardinality* for `d-1` further gains.  The
canonical two-chain coatom packet fails before this point: its fans force
every crossing to contain both phase labels, so no crossing is a native
NEW-chain target.  Even for a revised selector which passes that test, the
remaining assertion is precisely

\[
 \boxed{r_{\mathcal M_\theta}(P_X)\ge |X|-O(1)
        \quad\hbox{for every residual }X}                    \tag{4.6}
\]

in one legal terminal cap state.

The carrier-valid local crossing family is (0.2), a family of incomparable
coatoms.  Corollary 4.1 of the star-hidden theorem proves that assigning
these crossings directly down one nested fan would collapse the middle
owners.  Therefore (4.6) must use nonlocal exterior providers; it cannot be
deduced from the fan identity itself.

For a bounded-state induction the requirement is much weaker.  If
`|U|<=H` for an absolute `H`, then for `d-1>=H` capacity (4.2) is harmless,
and it suffices to prove the finite all-cut row

\[
                    r_{\mathcal M_\theta}(P_X)=|X|
                 \qquad(X\subseteq U).                       \tag{4.7}
\]

This identifies the best present target: a bounded-source, common-state
provider theorem for the incomparable coatom crossings, followed by the
already proved returned-catalyst cycle router.  An all-source near-isometry
is not needed if bounded regenerative state is maintained from the base.

### Theorem 4.3 (the surviving boundary bank is not that provider theorem)

Let `e_1 subset e_2 subset ... subset e_m` be nested physical intervals in
one literal terminal word `A`.  Their values

\[
                         V_j=\bigcup_{p\in e_j}A_p            \tag{4.8}
\]

are nested.  Consequently, if `C_1,...,C_h` are distinct targets of one
rank, at most one of them can be realized on the cells `e_j`.  More
generally, `p` disjoint nested fan/boundary banks directly realize at most
`p` members of a uniform antichain.

In particular, the carrier-valid seam crossings

\[
                  C_i=\{x\}\cup(F-\{f_{i+1}\})              \tag{4.9}
\]

form a uniform antichain.  In any selector satisfying the conditional ledger,
the `d-1` surviving exterior addresses arise from one transported nested
endpoint bank.  Even after a
candidate-dependent relabelling, one fixed terminal cap word can assign at
most one of the `C_i` directly to that bank.  Marginally choosing a different
relabelling for every `C_i` chooses different cap states and cannot be
combined.

#### Proof

Interval inclusion gives `V_j subseteq V_(j+1)`.  Two distinct members of
one uniform layer are incomparable, so no two can occur in this chain.
Equation (4.9) omits a different filler at every index, hence its members
are distinct and have equal cardinality.  The last assertion is just the
quantifier order: one literal terminal word has one nested value chain,
regardless of how many alternative relabellings exist prospectively.
\(\square\)

The returned-catalyst router does not contradict Theorem 4.3.  It can move
the incomparable targets to nonnested **used** cells by closed alternating
cycles, but it preserves the used physical basis.  To exploit the nested
free bank, a route must therefore start with its chain values, leave the
bank, and end on nonnested exterior provider cells.  Those open nonlocal
paths are precisely the unproved edges of `M_theta` in (4.1).

Thus the finite-`H` provider lemma is not obtained merely by reserving
private coordinate relabellings.  For `H>=2`, it must certify nonnested
exterior cells (or use at least `H` separately planted typed stars); a
single nested boundary bank plus returned fixed-basis cycles is
insufficient.

The proved asymmetric one-chain selector illustrates the same point even
more sharply.  Its unused opposite fan has `d` distinct addresses, but all
nonsingleton cells have the identical literal value `B_0 union B_1`.
Therefore that whole address bank has direct target rank one.  Physical
address multiplicity and provider rank are different quantities already in
the first positive seam model.

### Theorem 4.4 (collar-disjoint finite-state bypass)

There is an exact alternative when the number of residual tasks is already
bounded.  Let `A` be a baseline source word, and suppose `h` typed one-cell
seam replacements are planted in physical collars `J_1,...,J_h` such that

1. the distance between distinct collars is greater than `d`;
2. replacement `j` agrees with `A` outside `J_j` and literally passes every
   depth-`d` owner window meeting `J_j`;
3. its two fans, lost-crossing reassignment, and typed star target `S_j`
   pass one exact local common-cap replay; and
4. every protected short pin meeting `J_j` is included in that replay.

Then all `h` replacements may be made simultaneously.  The resulting word
has `h` additional source positions and realizes all `S_j`; no
strict-gammoid provider matching between the collars is required.

#### Proof

An interval of source positions of length at most `d+1` meets at most one
collar.  Hence every depth-`d` owner window and every short compiler cell is
either unchanged or belongs to exactly one of the already verified local
replays.  Define the global source word by using the local replacement on
each collar and the baseline elsewhere.  The preceding observation proves
all central and protected lower equalities literally, coordinate by
coordinate.  Nonzeroness is local as well.  Each insertion adds one source
position, proving the length assertion.  \(\square\)

Thus, if a regenerative step exposes at most an absolute `H` hard tasks and
can **plant** `H` protected typed collars, it may pay them directly at
additive cost `H`.  This is a valid `O(1)` strategy and is strictly weaker
than making one seam route all `H` tasks.  What remains unproved is the host
theorem which produces those collar-disjoint prepared coatom fragments while
preserving the owner/q1/upper chronology.  Theorem 4.4 removes no such
planting obligation.

### Proposition 4.5 (typed-star rank obstruction)

The phrase “any fixed typed targets” in such a host theorem is false.  If a
typed singleton star `S` is the common base of a strict left fan chain

\[
       S=L_1\subsetneq L_2\subsetneq\cdots\subsetneq L_d
\]

and every `L_h` is a strict lower target below a rank-`r` carrier, then

\[
                         |S|\le r-d.                          \tag{4.10}
\]

The same conclusion follows from either shore alone.  Thus a one-cell typed
star cannot directly absorb a target of rank `r-q` with `q<d`.  In the
prepared complementary coatom glue the exact menu is smaller still:
`S subseteq G=K union {infinity,c}`, where `|G|=r-d-2`.

#### Proof

Every strict inclusion raises cardinality by at least one, so

\[
                   |L_d|\ge |S|+d-1.
\]

Since `L_d` is a strict lower target, `|L_d|<=r-1`, proving (4.10).
The coatom value follows from `|K|=r-d-4`.  \(\square\)

Consequently the collar-disjoint bypass applies only after a regenerative
normalization has converted every residual hard task into a low-rank typed
socket (or into an abstract address task whose star guard has such a low-rank
representative).  Higher-rank compiler holes still require nonlocal
alternating paths.  Coordinate-menu abundance and physical separation
cannot remove this rank obstruction.

## 5. Sharp small counterexamples

Two examples distinguish the claims.

### 5.1 A spare which cannot enter a balanced block

Let

\[
 L=\{a,b\},\quad C=\{0,1,2\},\quad
 E=\{a0,a1,b2\},\quad M=\{a0,b2\}.                          \tag{5.1}
\]

The spare is `1`.  It can exchange with `0`, but cell `2` lies in the tight
block `N({b})={2}` and is unreachable.  Thus ordinary Hall and one spare do
not imply full exchange reachability; the missing condition is exactly
(2.4).

### 5.2 Every task individually routable, no pair routable

Take two task entrances `p_1,p_2`, one sink `s`, and arcs

\[
                         p_1\to s,\qquad p_2\to s.            \tag{5.2}
\]

Each singleton has gammoid rank one, while

\[
                   r(\{p_1,p_2\})=1.                         \tag{5.3}
\]

This is the sharp obstruction to replacing the all-cut condition by
single-task tests or by serial reuse of one q1 spare.

## 6. Audit

The dependency-free audit exhausts every bipartite graph with
`1<=|L|<=3`, `|C|=|L|+1`, and every left-saturating matching.  It verifies
Theorem 2.1, the strict-Hall equivalence (2.4), the exterior-cell
conservation law, both sharp counterexamples, and the one-sink/`d-1`-sink
rank ceilings:

```text
python3 scratch/audit_one_spare_exchange_and_exterior_ear_rank_20260801.py
```

The audit is combinatorial.  It does not claim that the required provider
edges in (4.6) exist in the physical coatom host.
