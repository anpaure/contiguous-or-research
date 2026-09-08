# A translated rank-tight nine-turn packet, and the exact downstream guards

Date: 2026-07-31  
Status: all-size conditional packet theorem; exact commuting `m=5` positive
cube; exact downstream independence counterexamples; no all-`m` packet-supply
theorem

## 0. Verdict

The first viable width in the stateless Catalan turn ledger is not merely a
numerical threshold.  It is attained by a literal symmetric packet.

At the standard `m=5` `ML(9)` root there is one alternating `C10` circuit
whose first two coordinate rotations give three pairwise vertex-disjoint
circuits.  The three circuits repair the complete stabilizer-three orbit of
missing lower colours and the complete stabilizer-three orbit of missing
upper colours.  Every one of the eight switch subsets is Hamiltonian, and
its augmented occurrence matching has deficiency exactly equal to its
number of remaining palette holes.  Consequently every order of the three
switches is legal and has the exact staircase

```text
(3,3,3) -> (2,2,2) -> (1,1,1) -> (0,0,0).
```

Each switch replaces exactly three turn occurrences on each shore.  The
three negative banks are private, so the compound changes exactly nine turn
occurrences per shore.  This realizes the first width not excluded by the
stateless recursion lower bound: width at most eight leaves
`Omega(Cat_m)` central defect.

The algebraic invariant is **matching-floor tightness**.  If the two
augmented shores have order `N`, let `h_- , h_+` be their isolated palette
holes, put `b=max(h_-,h_+)`, and define

```text
xi = N - matching_rank - b.
```

Always `xi>=0`.  The `m=5` cube has `h_-=h_+` and `xi=0` in every state.
Equivalently, after the isolated hole vertices are deleted, the augmented
graph has a perfect matching.  A unit switch reduces all three defects by
one precisely when it fills one hole on each shore and preserves this
floor-tight core.

This yields a general translated-packet lemma.  A full cyclic defect orbit
is repairable by translates of one prototype provided that its signed loss
banks, augmenting modules, and physical supports are private and the literal
subset topology is safe.  Arbitrary bounded defect sets require the exact
shore and compatibility Hall inequalities; translation by itself is not a
substitute.

The `m=5` cube also pads verbatim to every `m>=5` as a private local atom.
It services exactly one three-partition block of holes.  A greedy packing
lemma reduces simultaneous installation to a candidate-supply inequality;
for bounded carried debt the required placement density is only `O(m/N)`,
whereas an extensive `Theta(N/m)` stateless debt becomes critical under
full-depth radius-`Theta(m)` halo separation.

There is also a sharp negative conclusion.  Central rank-tightness—even
together with disjoint physical supports—does not protect residence, deeper
providers, or compiler Hall.  The new `m=5` translated endpoint admits a
perfect decoration and a `42`-path Catalan forest, but that deterministic
forest contains `34` internal runs of length two and misses one internal
depth-two upper target.  Independently, the frozen K17 packet `3836` improves
palette support and augmented rank by the same amount while losing named
rank-five and rank-eleven providers; packet `919` is all-depth
support-monotone but creates a new length-two run.  Thus the full recursive
atom must be a **guarded rank-tight translated cube**, not merely a palette
cube.

The exact all-`m` remaining statement is the supply of such guarded cubes.
This note proves their composition once supplied and proves the first
commuting translated base.  It does not prove that every dimension supplies
the prototype or the private downstream guards.

## 1. Matching-floor tightness

Let `A` be a bipartite augmented occurrence graph with two shores of order
`N`.  Suppose `h_-` declared palette colours on the left shore and `h_+`
declared palette colours on the right shore have load zero.  These vertices
are isolated in `A`.  Put

\[
 b(A)=\max\{h_-,h_+\},\qquad
 \xi(A)=N-\nu(A)-b(A),                              \tag{1.1}
\]

where `nu(A)` is the maximum matching order.

### Lemma 1.1 (hole floor)

For every augmented occurrence graph,

\[
                         \xi(A)\ge0.                 \tag{1.2}
\]

If `h_-=h_+=b`, then `xi(A)=0` if and only if deleting the isolated hole
vertices on both shores leaves a bipartite graph with a perfect matching.

#### Proof

A matching omits every isolated vertex.  It therefore has order at most
`N-h_-` and at most `N-h_+`, hence at most `N-b`.  This proves (1.2).  When
the hole counts agree, equality means that all `N-b` remaining vertices on
both shores are matched, which is exactly a perfect matching of the reduced
core. \(\square\)

Call `A` **floor-tight** when `xi(A)=0`.

### Lemma 1.2 (rank-tight unit reset)

Suppose `h_-=h_+=b>0` and `A` is floor-tight.  Let one legal physical switch
produce `A'`, fill exactly one old palette hole on each shore, and create no
new palette hole.  Then the following are equivalent.

1. The three defects satisfy
   \[
       (h_-,h_+,N-\nu): (b,b,b)\longmapsto(b-1,b-1,b-1).
   \]
2. `A'` is floor-tight.
3. The reduced nonhole core of `A'` has a perfect matching.

Relative to any declared common-core matching, condition 3 is equivalently
certified by a complete family of vertex-disjoint augmenting paths reaching
all newly exposed sinks.

#### Proof

The new hole floor is `b-1`.  Lemma 1.1 gives
`nu(A')<=N-(b-1)`.  Equality is simultaneously statements 1 and 2, and the
second part of Lemma 1.1 gives statement 3.  The augmenting-path formulation
is Berge's theorem, or max-flow after orienting a common-core matching.
\(\square\)

Thus the equality of the three `m=5` staircase coordinates is not a
coincidence: the third coordinate is forced once the first two decrease and
the nonhole core remains perfect-matchable.

## 2. The three-entry signed turn algebra

For one turn shore, let `mu(c)` be its occurrence load.  A switch has a
signed derivative `Delta` of total sum zero.  Assume its reduced signed bank
has exactly three negative and three positive units, all of size one.

There is a local way to recognize the number three.  Let an alternating
`C_(2t)` have circuit vertices `v_0,...,v_(2t-1)`, and let `w_i` be the
unchanged factor neighbour of `v_i` outside the circuit.  On either shore,
the old and new local turn multisets are

\[
 P^0=\{\tau(w_i,v_i,v_{i-1})\},\qquad
 P^1=\{\tau(w_i,v_i,v_{i+1})\},                    \tag{2.1}
\]

with the indices restricted to the `t` vertices on that shore and with
`tau` equal to intersection or union as appropriate.  No turn outside the
circuit changes.  Therefore the number of reduced negative units, and also
the number of reduced positive units, is exactly

\[
                    t-|P^0\wedge P^1|,              \tag{2.2}
\]

where the meet is multiset intersection.

For each circuit in Theorem 5.1, `t=5` and the two local turn multisets have
multiset intersection two on **each** shore.  Hence (2.2) gives three
replaced occurrences.  Those two conserved turn tokens are the local
algebra behind the `3+3+3` packet width; the defect decrease itself uses the
following reserve and rank conditions.

### Lemma 2.1 (one defect unit plus collateral circulation)

Suppose exactly one positive unit lands at an old hole `h`, every negative
unit leaves a colour of load at least two, and no other old hole is touched.
Then the switch lowers palette defect by exactly one and creates no new
hole.  At occurrence level its signed bank decomposes into one donor-to-hole
transport and a circulation or surplus-to-covered transports on the other
two units.

#### Proof

Every negative colour retains at least one occurrence.  The positive unit
at `h` creates one new support member, while positive units at already
covered colours do not change support.  Hence support increases by one.
Pair the three labelled negative units with the three positive units.  The
pair ending at `h` is the defect transport; the other pairs have covered
targets and surplus sources. \(\square\)

For two turn shores, one physical switch may pair one such lower transport
with one upper transport.  Lemma 1.2 supplies the independent occurrence-
correlation row: palette monotonicity does not by itself imply rank
tightness.

## 3. A private rank-tight cube

Let a state have equal defect banks `H_-`,`H_+` of size `d`.  Let
`t_1,...,t_d` be physical switches.  For each switch retain:

* its serviced pair `(ell_i,u_i) in H_- x H_+`;
* its complete signed turn banks;
* its physical support;
* a private augmented alternating module; and
* its old/new topology port matching.

### Definition 3.1 (private rank-tight cube)

The switches form a private rank-tight cube when:

1. `i -> ell_i` and `i -> u_i` are bijections onto the two defect banks;
2. every negative turn unit uses declared surplus capacity, and negative
   banks are disjoint (or obey an explicitly supplied aggregate reserve
   inequality);
3. the augmented modules are vertex-disjoint relative to one common core,
   and selecting switch `i` adds one private augmentation which activates
   its two hole vertices;
4. every subset of switch supports is a legal factor state with the declared
   topology; and
5. the signed derivatives superpose.

### Theorem 3.2 (cube reset)

If the initial augmented graph is floor-tight and
`t_1,...,t_d` form a private rank-tight cube, then for every subset `S`

\[
 h_-(S)=h_+(S)=N-\nu(A_S)=d-|S|,\qquad \xi(A_S)=0. \tag{3.1}
\]

In particular the all-new state has complete palettes and a perfect
augmented occurrence matching.  Every ordering of the switches is a legal
rank-tight repair order.

#### Proof

Private signed reserves and bijectivity service exactly the holes indexed by
`S` and no others, so both hole counts are `d-|S|`.  Start with a perfect
matching of the initial reduced core.  Toggle the private alternating module
of every member of `S`; disjointness makes these augmentations simultaneous
and increases matching order by `|S|`.  Thus the matching order is
`N-d+|S|`, which meets the hole upper bound.  Hence (3.1) holds.  Literal
subset topology safety makes every chain through the Boolean cube a legal
physical order. \(\square\)

Private augmented modules are sufficient, not necessary.  The exact weaker
condition is simply floor-tightness of every visited subset state plus a
legal maximal chain.  This is what the finite audit uses.

The private-linkage clause cannot be replaced by disjointness of the newly
added edges.  Let

```text
left  = {b,s1,s2},     right = {a,t1,t2},
common edges = {b-a,b-t1}.
```

The common matching `{b-a}` has rank one.  Macro `e1` adds `s1-a`, and by
itself raises the rank to two using the augmenting path
`s1-a-b-t1`.  Macro `e2` adds `s2-t1`, and by itself raises the rank to two
using the direct augmentation at `t1`.  The two added edges have disjoint
endpoint sets.  Together, however, the rank is still only two: both
augmentations require the same right-side resource `t1`, while `t2` remains
isolated.  Thus two individually rank-tight units need not form a
rank-tight two-cube.  The exact necessary condition is the joint
vertex-disjoint augmenting linkage, equivalently the common-core min-cut.

## 4. Translation and arbitrary bounded debt

Let a cyclic group `G=<rho>` act on the two colour shores and on the
physical catalogue.  Suppose

\[
 H_-=(\ell_i:i\in\mathbb Z_q),\qquad
 H_+=(u_i:i\in\mathbb Z_q)                          \tag{4.1}
\]

are defect orbits, possibly stabilized in the ambient coordinate action.

### Theorem 4.1 (guard-free translated central reset)

Assume one prototype `t` and its translates
`t_i=rho^i t`, `i in Z_q`, satisfy Definition 3.1 and service

\[
                         \ell_i\longmapsto u_{i+s}  \tag{4.2}
\]

for one fixed shift `s`.  Then their all-new state repairs both complete
orbits and has a perfect augmented matching.  Every subset and every order
is centrally legal.

#### Proof

The map `i -> i+s` is a permutation of `Z_q`; therefore the translated
macros service both defect orbits bijectively.  Apply Theorem 3.2. \(\square\)

More generally, if a set `S` of shifts is allowed, the orbit compatibility
graph is a balanced `|S|`-regular Cayley graph.  Any one shift is already a
perfect matching.  This makes the **full-orbit** assignment automatic.

It does not repair an arbitrary bounded pair of partial defect sets.  For
example, on `Z_5` with only shift zero allowed, lower defects `{0,1}` and
upper defects `{0,2}` have equal cardinality, but lower defect `1` has no
allowed upper neighbour.  The sharp general condition is Hall:

\[
 |N(X)|\ge |X|\qquad(X\subseteq H_-).                \tag{4.3}
\]

If donor occurrence capacities are not private, shore Hall must be imposed
before (4.3).  If macro supports conflict beyond common endpoints, a second
compatibility/packing condition is required.  If augmented routes share a
sink, their rank gains need not add.  Hence translation solves assignment
only on full balanced orbits; it does not eliminate the physical,
correlation, or topology rows.

## 5. The exact commuting translated packet at `m=5`

Use coordinate masks on `Z_9`.  At the standard transparent root the missing
turn palettes are

```text
lower: 73,146,292
upper: 219,365,438.
```

They are two orbits of order three.  Let `rho` rotate every mask by one
coordinate.  Take the prototype circuit

```text
77 109 105 107 106 362 330 334 332 333
```

and its first two translates:

```text
149 157 153 155 154 218 210 214 212 213
298 314 306 310 308 436 420 428 424 426.
```

### Theorem 5.1 (literal translated three-cube)

The three `C10` supports are pairwise vertex-disjoint.  Their serviced
pairs are

```text
73  -> 365
146 -> 219
292 -> 438,
```

which is a fixed cyclic offset between the two defect orbits.  On each
shore, every switch has signed profile `(-1)^3(+1)^3`; every negative colour
has root load two; and the three negative banks are pairwise disjoint.

All eight subset states are Hamilton cycles.  A state with `s` selected
switches has exactly `3-s` holes on each shore, augmented matching
deficiency `3-s`, and correlation debt `xi=0`.  Hence all six orders of the
three switches give the rank-tight staircase and terminate at a perfect
augmented matching.

#### Proof

Every assertion is a literal enumeration of the three displayed circuits,
the turn counter formulas, factor components, and the augmented matching
graph.  The independent audit reconstructs all eight states rather than
inferring commutativity from disjoint support. \(\square\)

This packet is stronger than the previously frozen private relay packet:
the old relay had one circuit which was not Hamilton-safe at the root,
whereas this translated cube is safe in every subset state.  Conversely the
old packet has separately audited private standard-glue ports; those are not
inferred for the new cube.

The complete root-safe `C10` census also shows that topology is a genuine
extra hypothesis in Theorem 4.1.  There are `31` rank-tight singleton
macros.  Exactly `10` prototypes have their first two translates in the same
singleton catalogue.  Of those, `7` admit at least one legal three-step
repair chain, but only `3` have all eight subset states safe.  Thus translated
rank-tight singleton data do not automatically form a cube; the displayed
prototype is one of the three full cubes.

Each circuit changes three turn occurrences per shore and the signed banks
do not cancel across circuits.  Therefore the compound has exact turn width
nine on each palette.  This matches the earlier arithmetic theorem: a
sectorwise stateless binary recursion with width at most eight has
`Omega(Cat_m)` collision defect.  The finite packet shows that the threshold
`nine` is attainable centrally; it does not show that width nine suffices in
every dimension.

### 5.2 Dimension-free padding, and its exact block shape

The local packet itself is not confined to `m=5`.  Let `m>=5`, choose a
fixed set `H` of size `m-5`, and inject the nine active coordinates into
`[2m-1]\H`.  Replacing every base mask `S` by

\[
                              H\cup S                 \tag{5.1}
\]

embeds `ML(9)` on ranks four/five into `ML(2m-1)` on ranks `m-1,m`.
Containment, alternating circuits, turn intersections and turn unions all
commute with (5.1).  Therefore the entire translated three-cube, including
every signed bank and every local factor component, pads verbatim to every
`m>=5`.

This is a dimension-free **local atom**, not a global factor theorem.  To
insert it into a spanning factor, the embedded base cycle must be a declared
factor component or boundaried module, and its augmented matching resources
must be private from the surrounding core.

The holes serviced by one padded atom have an exact geometry.  Partition
the active nine-set into the three triples

\[
 Q_0=73,\qquad Q_1=146,\qquad Q_2=292.              \tag{5.2}
\]

The lower holes are `H union Q_i`, and, with cyclic indices, the paired
upper holes are

\[
                       H\cup Q_i\cup Q_{i-1}.        \tag{5.3}
\]

### Proposition 5.2 (padded local atom)

For every `m>=5`, equations (5.1)--(5.3) give a literal copy of the complete
eight-state translated packet inside `ML(2m-1)`.  If that copy is installed
as a private factor module with the padded defect colours and augmented
resources declared private, it is a rank-tight three-defect reset in the
ambient dimension.

#### Proof

Union with a fixed set is injective and commutes with containment,
intersection and union on masks containing that set.  It therefore sends
every base factor edge, alternating circuit and turn value to the
corresponding padded object.  The factor component and all eight switch
states are graph-isomorphic to the audited base states.  With private
palette and augmented resources, the ambient graph is their direct sum with
the unchanged outside core, so matching ranks and defects add and the local
rank-tight reset survives. \(\square\)

Thus any two lower holes repaired by the same padded atom intersect in
exactly `H`, of size `m-5`, and their three active remainders are disjoint.
This is a sharp obstruction to using this one atom for arbitrary bounded
debt: a proposed lower-hole triple with pairwise intersection larger than
`m-5`, for example, cannot be a coordinate conjugate of (5.2).  A uniform
construction must prove that its defects decompose into these
three-partition blocks, supply a richer finite gadget basis, or fall back to
the general Hall router of Section 4.

Padding also does not by itself prove the density hypothesis used below.
For one *fixed* serviced block, `H` and the active nine-set are already
determined by the holes.  Coordinate conjugation only permutes those nine
active coordinates (and permutations inside the always-present or always-
absent sets do not change any mask), so this bare gadget yields only a
dimension-independent finite menu for that block.  Abundant candidates must
come from alternative factor embeddings, alternative local cubes, or from
designing the carried debt blocks rather than accepting arbitrary holes.
The natural stateful target is consequently stronger and cleaner: maintain
the central debt itself as a bounded union of private three-partition
blocks, each with a reserved guarded module.

There is nevertheless a much broader **unit** supply statement.

### Proposition 5.3 (every nested defect pair has a padded unit macro)

Let `m>=5`, let `L` have rank `m-2`, let `U` have rank `m+1`, and suppose
`L subset U`.  Then a coordinate-conjugate padded copy of one switch in
Theorem 5.1 has positive defect gains exactly `(L,U)`.

The number of labelled embeddings obtained by this construction is

\[
 E_m={m-2\choose3}^2(3!)^3=\Theta(m^6).             \tag{5.4}
\]

Consequently the number of distinct complete boundaried support patterns
(the circuit together with the unchanged external factor edge at every
circuit vertex) is at least `E_m/9!`, hence is also `Omega(m^6)`.

#### Proof

Choose a triple `Q_0 subset L` and put `H=L\Q_0`; there are
`binom(m-2,3)` choices.  Put `Q_2=U\L`, which is a triple.  Choose a triple
`Q_1 subset Omega\U`; there are another `binom(m-2,3)` choices.  The three
`Q_i` are disjoint.  Map the three base triples in (5.2) bijectively to
them, in `(3!)^3` ways, and pad every mask by `H`.  The selected prototype
gain becomes

\[
 H\cup Q_0=L,
 \qquad H\cup Q_0\cup Q_2=U.
\]

This proves existence and the labelled count.  In the base boundaried
support, the intersection of all vertex masks is empty and their union is
the complete active nine-set.  After padding, the corresponding intersection
is `H` and the union is `H` plus the active set, so both are recovered from
the physical patch.  If two labelled embeddings give one complete patch,
their quotient is therefore an automorphism of its nine active coordinates,
of which there are at most `9!`.  Dividing gives the last bound. \(\square\)

Proposition 5.3 is a dimension-uniform palette-macro supply theorem.  It is
not yet a factor-catalogue theorem: a candidate counts only after its padded
old edges are alternating in the chosen factor, its loss colours have the
required reserve, and its linkage/topology/guard records pass.  For
arbitrary bounded hole banks, the compatibility graph supplied by these
unit macros is the rank-`(m-2)` versus rank-`(m+1)` containment graph
restricted to the holes; its exact selection condition remains Hall (4.3).

## 6. Conditional packing and the minimum supply ledger

One translated three-cube changes fifteen old **middle-level factor**
seams: every `C10` replaces five old edges, and the three supports are
disjoint.  It also consumes nine negative turn-occurrence units on each
shore.  These two numbers control different resources.  After decoration,
residual matching, connector insertion, or compilation, the number of
changed seams in the final physical chronology can be larger.  Write `s`
for that authenticated physical seam count.  The value `s=15` may be used
only when the physical lift is phase-aligned so that no additional seam is
created.

Let `D=3p` lower holes and `D=3p` upper holes already be partitioned into
`p` admissible three-partition blocks of the form (5.2)--(5.3).  For block
`j`, let `C_j` be a family of complete candidate translated packets.  A
candidate includes its full physical dependency halo, its nine labelled
negative units on each shore, its augmented linkage module, and its named
compiler banks.  Declare two candidates to conflict when any of those
resources cannot be used simultaneously.

### Theorem 6.1 (greedy guarded-packet packing)

Suppose every `C_j` has at least `S` candidates and every candidate
conflicts with at most `Delta` candidates in any other one class `C_i`.
If

\[
                         S>(p-1)\Delta,              \tag{6.1}
\]

then one may select one pairwise compatible packet from every `C_j`.  If
each candidate individually satisfies the guarded reset hypotheses of
Section 7, their union repairs all `3p` defect pairs and preserves all
declared guards.

#### Proof

Choose packets one block at a time.  After `j<p` choices, at most
`j Delta <=(p-1)Delta` candidates have been forbidden in the next class,
so (6.1) leaves one choice.  Pairwise compatibility makes the signed banks,
linkage modules, halos and compiler banks direct sums.  The cube-reset and
guard theorems therefore apply componentwise. \(\square\)

The scalar private-negative-bank capacity forced by this lemma is

\[
 \sum_c(\mu_-(c)-1)^+\ge9p,
 \qquad
 \sum_c(\mu_+(c)-1)^+\ge9p.                         \tag{6.2}
\]

More exactly, for every colour `c`,

\[
       \sum_{t\ {\rm selected}}(-\Delta_t^\pm(c))^+
                         \le \mu_\pm(c)-1.           \tag{6.3}
\]

Equation (6.2) is necessary for the private nine-unit implementation, while
(6.3) is the exact capacity row.  It is not necessary for a more economical
packet with cancellations or shared rerouting.

There is a useful density calibration.  Suppose candidate packets are
translated along a chronology of length `N`, and every downstream object
used by the recursion has owner-dependency radius at most `R`.  A packet's
physical seam halo is a union of `s` intervals of length at most `R`.  For a
fixed translated support pattern, two translates can conflict only at a
difference belonging to one of at most

\[
                         s^2(2R+1)                   \tag{6.4}
\]

offsets.  Thus one may use the conservative conflict bound

\[
                  \Delta\le s^2(2R+1)-1.            \tag{6.5}
\]

If every block has at least `rho N` candidate placements, Theorem 6.1 is
guaranteed by

\[
 \boxed{
 \rho>{(p-1)s^2(2R+1)\over N}
      \sim {s^2(2R+1)D\over3N}.}                    \tag{6.6}
\]

This is a sufficient packing density, not a lower bound on all possible
packings.  It deliberately charges every pair of seam intervals and can be
improved when the seam-difference set is sparse.

The scale comparison is informative nonetheless.

* If the carried central debt `D` and the authenticated seam count `s` are
  uniformly bounded and `R<=m`, then the required density is `O(m/N)`,
  exponentially small in the Catalan regime.  Geometric packet abundance is
  not the likely obstruction.
* If a fresh stateless recursion creates `D asymp N/m` debt and only the
  compiler-scale radius `R=Theta(sqrt(m))` is separated, (6.6) asks for
  density `Theta(m^(-1/2))`, still plausible.
* If the same growing debt requires literal separation through every depth,
  so `R=Theta(m)`, (6.6) asks for constant density (and its conservative
  constant may exceed one).  The stateless construction has no packing
  margin.  This is another reason to regenerate bounded debt rather than
  rebuild an extensive defective leaf decomposition.

Supply density alone does not bound the carried downstream debt.  With
`s` changed physical seams, at depth `q` as many as `sq` old provider occurrences
lie in the changed boundary family.  Hence one unguarded packet can expose

\[
            \sum_{q=1}^{Q}sq={sQ(Q+1)\over2}         \tag{6.7}
\]

potential last-provider losses on one shore.  For bounded `s`, this is
`Theta(m)` already for `Q=Theta(sqrt(m))` and `Theta(m^2)` for
`Q=Theta(m)`.  Similarly, a constant-size seam packet can create short runs
in many coordinates.
Therefore even uniformly bounded packet count does **not** imply uniformly
bounded RSB state.  The negative-part provider, residence-automaton and
compiler-Hall guards below are load-bearing; packing only makes their deltas
composable.

## 7. Downstream guards

Let a literal chronology have provider multiplicity `mu_q(Z)` for target
`Z` at depth `q`.  A packet `t` changes it by `Delta_{q,t}(Z)`.

### Theorem 7.1 (provider negative-part guard)

Assume the dependency halos of a family of switches are separated far
enough that their depth-`q` window deltas add.  Then every subset state
covers every target through depth `Q` if and only if

\[
 \mu_q(Z)+\sum_t\min\{0,\Delta_{q,t}(Z)\}\ge1       \tag{7.1}
\]

for every `q<=Q` and every target `Z` on both shores.

#### Proof

For a subset `S`, the load is
`mu_q(Z)+sum_(t in S) Delta_(q,t)(Z)`.  Its minimum over all subsets selects
exactly the negative deltas. \(\square\)

Disjoint switch vertices are not enough for (7.1): two depth-`q` halos may
overlap.  One must either separate the complete dependency rays or export
their joint table.

Residence has an equally exact but different guard.  For required minimum
run `D`, every retained fragment induces a partial transformation of the
capped run automaton

```text
0,1,...,D,*.
```

A packet is residence-safe precisely when the transformations around its
new seams compose without closing a state `1,...,D-1` away from a global
endpoint.  A sufficient private guard is that both phases of every separated
collar are accepted for every boundary state exported by the common core.
This condition is independent of (7.1).

For a fixed lower compiler let `K_*` be the stable cell bank and
`K_t^0,K_t^1` the private old/new banks.  Put

\[
 \sigma_0(X)=|N_{K_*}(X)|+\sum_t|N_{K_t^0}(X)|-|X|,
 \quad
 \delta_t(X)=|N_{K_t^1}(X)|-|N_{K_t^0}(X)|.         \tag{7.2}
\]

The exact all-subset common-cap guard is

\[
 \sigma_0(X)+\sum_t\min\{0,\delta_t(X)\}\ge0
 \qquad(X\text{ a lower-target family}).           \tag{7.3}
\]

This is Hall after minimizing independently over the cube bits.  If cell
banks interact, the full joint incidence relation replaces (7.3).

### Theorem 7.2 (guarded translated reset)

A translated central cube satisfying Theorem 4.1 preserves residence,
every declared deeper provider, and lower compiler Hall in all subset states
provided:

1. its full dependency halos are separated or their joint tables are
   exported;
2. every local residence transformation is accepting on the exported
   boundary-state relation;
3. the provider inequalities (7.1) hold; and
4. the compiler inequalities (7.3) hold.

Under these assumptions the all-new state is a complete guarded reset.

#### Proof

Theorem 4.1 gives the central palettes, augmented matching, and declared
topology.  Halo separation makes the provider and compiler deltas additive,
so Theorems 6.1 and Hall's theorem give the two coverage rows.  Composition
of the capped automata gives residence. \(\square\)

This is an all-size packet theorem, but its hypotheses are a supply
specification.  No result here constructs the required guards uniformly in
`m`.

## 8. Exact independence calibrations

The deterministic perfect matching chosen by the audit at the terminal
`m=5` translated state lifts to an exact `210`-edge, `42`-path Catalan
forest on `J(10,5)`.  Thus the translated packet is compatible with the
central graphic row.  Nevertheless that forest has

```text
34 internal positive coordinate runs of length two
one internal upper depth-two hole, mask 382
no other internal deep hole.
```

This does not prove that every decoration of the translated endpoint has
those debts.  It proves that the central cube theorem alone cannot infer the
downstream rows.

Two independent K17 packets make the logical separation sharper.

* Packet `3836` gains four missing lower colours, loses none, preserves the
  complete immediate upper multiset, and raises augmented matching rank by
  four.  It nevertheless loses provider `0x08491` at rank five and provider
  `0x1b47d` at rank eleven, and creates a new length-two run collar.
* Packet `919` is inclusion-monotone on the complete cyclic flag tower and
  strictly reduces occurrence-correlation debt.  It still creates a new
  length-two run collar.

Therefore:

1. palette plus matching-rank descent does not imply provider safety; and
2. palette plus matching rank plus all-depth support monotonicity does not
   imply residence safety.

These are literal counterexamples, not merely missing implications in the
proof.

## 9. Consequences for the all-`m` construction

The central reset lane has advanced in three precise ways.

1. The defect/matching staircase is governed by one algebraic invariant,
   `xi=0`, rather than three unrelated miracles.
2. The first nontrivial repaired dimension contains a fully commuting
   translated cube of exact turn width nine.
3. Full-orbit defect assignment is automatic once one shifted prototype is
   supplied; arbitrary bounded debt is exactly a Hall problem.

What remains is not another central counting argument.  It is the following
uniform supply statement.

> **Guarded rank-tight orbit-cube supply.**  At every recursive macro
> boundary, the bounded signed defect packets admit a Hall-saturating family
> of rank-tight orbit macros whose literal subset topology is safe and whose
> dependency halos satisfy the residence, provider, and common-cap guards.

Proving this statement, or a contraction version of it, gives the stateful
`9+` reset required by the bounded-defect regenerative spine.  The `m=5`
cube proves that the central algebra and symmetry are real.  The K17 rows
prove that the guards cannot be deleted.

## 10. Reproducibility

Run

```text
python3 scratch/audit_translated_rank_tight_m5_packet_20260731.py
```

It writes

```text
scratch/translated_rank_tight_m5_packet_20260731.audit.json
```

and reconstructs the standard root, all three translated circuits, all
eight cube states, every signed bank, every augmented rank, one terminal
perfect decoration and physical forest, and the frozen K17 downstream
counterexamples.
