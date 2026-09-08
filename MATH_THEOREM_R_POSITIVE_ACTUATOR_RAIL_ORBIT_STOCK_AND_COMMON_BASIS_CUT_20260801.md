# Positive actuator rails, orbit-compressed stock, and the exact common-basis cut

Date: 2026-08-01

Status: unconditional local physicalization and exact conditional global
stock criteria.  The theorem turns every strict-positive age actuator body
into a literal owner-simple Johnson strand with injective adjacent palettes.
It also gives necessary-and-sufficient resource-orbit and common-matching
tests for compressing many copies.  It does **not** prove that the required
guard-complete orbit seed exists in the canonical Catalan/PBBS host.

## 0. Result and scope

The arbitrary-hole collapse theorem and its parity-sweep refinement have
removed the higher-hole age-algebra gate.  Their types have nonempty oldest
class, so they avoid the empty-oldest-class obstruction affecting the older
single-hole completion actuator.

In addition,
`MATH_THEOREM_AGE_LEVEL_CANONICAL_ACTUATOR_STOCKING_20260801.md` proves that
all canonical bad, donor and reservoir *profiles* fit simultaneously in the
original `W` named rows by an exact complete-bipartite `b`-matching.  Thus no
profile-capacity Hall row remains here.  The present note starts at the
strictly stronger occurrence question: order those stocked rows as literal
owner-moving traces while retaining palettes and guarded compiler data.

The later theorem
`MATH_THEOREM_MONOTONE_ROTOR_FRACTIONAL_TRACE_CIRCULATION_20260801.md`
closes the **unconditioned invariant fractional** trace gate outright by a
different monotone-rotor realization.  Therefore no further rank-only or
fractional trace-balance inequality is part of the present frontier.  If the
specific actuator rows above are imposed as lower bounds, their conditioned
residual circulation is still separate; alternatively one may abandon that
decomposition and round the rotor realization directly.

The integral sequel
`MATH_THEOREM_AGGREGATE_MONOTONE_ROTOR_SEMIGROUP_AND_BUFFER_ROUNDING_20260801.md`
now also closes, for every `k>=31`, the integer residue in the aggregate
age-type/signature quotient.  Its output has total formal type-occurrence
mass `W`, but a primitive mixed package can fail to have a one-copy labelled
lift.  Thus it does not make the occurrence question below redundant: the
first rotor-specific physical gate is the Named Rotor Flag-Colouring problem,
which must simultaneously rethread the primitive type slots, use every named
owner once, and biject the nested marked flags to the residual named targets.

This gate is now sharpened by
`MATH_THEOREM_R_NRFC_LABELLED_COMPATIBILITY_HALL_AND_OWNER_SYMMETRY_LIMIT_20260801.md`.
For a fixed owner/flag state transversal it is exactly one ordinary
cycle-cover Hall cut; selecting that transversal jointly with its nested
target rows is OFHT.  Complete-layer symmetry does not imply OFHT.  The
primitive adjacent-buffer pair needs a chronology of length at least `d+2`;
the companion facet module realizes this sharply using `d` additional low
roles.  Therefore the large Ferrers buffers supply ample scalar mass but no
dimension-independent private-buffer physicalization.  Their globally
disjoint owner/target packing remains part of the present occurrence gate.

The remaining physical question has three logically separate parts.

1. Can one actuator body be realized on distinct literal owners, with its
   lower and upper adjacent colours also distinct?
2. Can all required copies be selected without repeating any owner, palette
   colour, guarded witness, or addressed compiler resource?
3. After the forced packet assignments, does the remaining common-cap or
   common-basis system still have an integral completion?

Theorem 2.1 answers the first question positively for every strict-positive
body of at most `d` transitions.  Theorem 3.1 is an exact orbit criterion,
Theorem 3.2 is an exact conditional concatenation, and Proposition 3.3 is a
nonsharp sufficient spread bound.  Theorems 4.1--4.2 give exact min--max
answers to two separately specified forms of the third question.  What is
not proved is one seed
satisfying all of these conditions simultaneously with the complete upper,
deep-shadow, residence-boundary and compiler guards of the Catalan host.

## 1. Age transitions and literal partitions

Fix a ground set `Omega` of order `k`, owner rank `r`, and depth `d`.  An
age type is

```text
c=(c_0,...,c_d),       c_i>=0,       sum_i c_i=r.
```

The directed age relation is

```text
c -> c'   iff   c'_(i+1)<=c_i for 0<=i<d.          (1.1)
```

A labelled state of type `c` on an owner `T` is an ordered partition

```text
T=C_0 dotunion ... dotunion C_d,       |C_i|=c_i.  (1.2)
```

If the next owner is

```text
T'=T-{alpha}+{beta},                                (1.3)
```

then a literal transition to a state of type `c'` exists precisely when
`alpha in C_d` and there are survivor sets

```text
S_i subseteq C_i,       |S_i|=c'_(i+1)  (0<=i<d).  (1.4)
```

Indeed, put

```text
C'_(i+1)=S_i,
C'_0=(C_d-{alpha}) union {beta}
     union union_(i=0)^(d-1)(C_i-S_i).              (1.5)
```

The sets in (1.5) partition `T'`, and their sizes are `c'`.  Conversely,
every literal shift has exactly this form.  In particular, a changing-owner
transition requires `c_d>0`.

## 2. Every strict-positive short body has a literal rainbow owner rail

### Theorem 2.1 (strict-positive open-rail theorem)

Let

```text
c^0 -> c^1 -> ... -> c^ell                         (2.1)
```

be a legal age path satisfying

```text
ell<=d,        c^t_i>=1 for all t,i,        k-r>=ell. (2.2)
```

Then there are pairwise distinct rank-`r` owners

```text
T_0,T_1,...,T_ell                                  (2.3)
```

and literal partitions of the prescribed types such that consecutive
owners are Johnson adjacent.  Moreover, the `ell` lower colours

```text
T_t intersect T_(t+1)
```

are pairwise distinct, and the `ell` upper colours

```text
T_t union T_(t+1)
```

are pairwise distinct.

Every finite coordinate run wholly internal to the **owner-membership
sequence** (2.3) has length at least `d+1`.  Runs clipped at either open
endpoint are not covered by this assertion.  This is not a source-letter
residence theorem: the canonical spelling may place a coordinate in only
one source letter while it remains in `d+1` consecutive owner windows.

### Proof

Choose distinct deletion labels

```text
alpha_0,...,alpha_(ell-1) in T_0
```

and put `alpha_t` in initial class `C_(d-t)`.  These classes are distinct
and nonempty by (2.2).  Fill the remaining positions of (1.2) arbitrarily.
Choose distinct labels

```text
beta_0,...,beta_(ell-1) in Omega-T_0
```

and define

```text
T_(t+1)=T_t-{alpha_t}+{beta_t}.                    (2.4)
```

At time `u`, each future deletion label `alpha_t`, `t>=u`, has age

```text
d-t+u.                                             (2.5)
```

These ages are distinct.  Delete `alpha_u` from the oldest class.  In each
younger class include its possible future deletion label among the
survivors.  This consumes at most one place, while every target class is
positive.  Fill the remaining survivor quotas using (1.1), and apply
(1.5).  Induction constructs every state in (2.3).

No inserted `beta_t` is later deleted.  Hence all owners are distinct.  The
two adjacent colours at edge `t` are exactly

```text
K_t=(T_0-{alpha_0,...,alpha_t})
      union {beta_0,...,beta_(t-1)},

U_t=(T_0-{alpha_0,...,alpha_(t-1)})
      union {beta_0,...,beta_t}.                   (2.6)
```

Their counts of retained initial labels determine `t`, so each family is
injective.  A born label starts in age zero and cannot leave the owner
before it reaches age `d`; the pre-aged `alpha_t` labels supply the matching
left owner history.  Thus no finite owner-membership run wholly inside the
collared strand is shorter than `d+1`.  The assertion does not concern
consecutive appearances in the underlying source letters.  QED.

### Corollary 2.2 (application to the arbitrary-hole packet)

Cut one edge of each base or parity-sweep cycle in
`MATH_THEOREM_R_ARBITRARY_HOLE_PARITY_SWEEP_MARK_ACTUATOR_20260801.md`.
Every resulting path has at most `d` transitions and every displayed age
coordinate is positive.  Hence each constituent has a literal
owner-simple, lower-`q1`-injective, upper-`q1`-injective open realization
whenever `k-r>=d`.

This is a local theorem.  It neither makes the palettes of different
strands disjoint nor joins their endpoints.  It also says nothing about
arbitrary-width upper witnesses or common-cap addresses not recorded in
the age state.

## 3. Exact orbit-compressed stock

Let a finite group `Gamma` act on `Omega`, and hence on every set-valued
resource.  A *resource species* records both the semantic role and the rank:
owner, lower colour, upper colour, a named deep witness, an addressed source
cell, and so on are different species even when their underlying subsets
coincide.

For a literal packet `P`, let `R(P)` be its finite occurrence-labelled list
of typed resources.
Call `P` **orbit-simple** when, within each species,

1. different seed occurrences have different resource values;
2. every `R in R(P)` has trivial stabilizer in `Gamma`; and
3. no two distinct resource values in `R(P)` lie in the same
   `Gamma`-orbit.

### Theorem 3.1 (orbit-stock criterion)

The translated packets

```text
{gP:g in Gamma}                                    (3.1)
```

have pairwise distinct resources in every declared species if and only if
`P` is orbit-simple.

### Proof

Suppose `gR=hR'` for resources of the same species.  Then `R,R'` are in the
same orbit, so orbit-simplicity gives `R=R'`; trivial stabilizer then gives
`g=h`.  Thus all resources in (3.1) are distinct.

Conversely, a nontrivial stabilizer makes two translates of the same
resource equal.  Two seed occurrences already having the same resource
value collide in the identity translate.  Finally, two distinct resource
values in one orbit become equal in suitable translates.  Each failure
contradicts injectivity of (3.1).  QED.

This criterion is sharp.  In particular, a cyclic full-orbit construction
can contain at most one singleton resource of any one species in its seed,
because all singletons form one orbit.  The canonical multi-hole actuator
passes this first numerical test: its distinguished terminal row contributes
one rank-one marked target per repaired unit.  Orbit-simplicity of all its
other physical and guarded resources is a separate condition, not a
consequence of the age algebra.

### Theorem 3.2 (unit-voltage concatenation)

Assume `Gamma=<sigma>` is cyclic and `P` is an orbit-simple literal open
packet.  Suppose the last state of `gP` has a legal guarded transition to
the first state of `g sigma P` for every `g`, and suppose the connector
resources form additional orbit-simple species disjoint from `R(P)`.
Then

```text
P, sigma P, ..., sigma^(|Gamma|-1)P                (3.2)
```

with those connectors is one literal cyclic packet bank.  It retains every
declared resource exactly once and incurs no component count proportional
to `|Gamma|`.

### Proof

Equivariance reduces legality to the one connector from `P` to `sigma P`.
Since `sigma` generates `Gamma`, the translated packets and connectors form
one directed cycle.  Theorem 3.1 gives resource injectivity.  QED.

The hypothesis in Theorem 3.2 is genuinely physical.  Common-entry fusion
of the age-type cycles proves only that the *types* of crossed edges are
legal.  A nondegenerate Johnson `C4` cannot preserve a strict lower
intersection palette under the corresponding two-edge switch; the exact
proof is Lemma 3.4 of
`MATH_THEOREM_R_LAMINAR_ACTUATOR_STOCK_COMMON_ENTRY_FUSION_AND_EMPTY_OLDEST_CLASS_HOST_OBSTRUCTION_20260801.md`.
Thus a seed connector must be prospective, or must carry a `C6`/longer
palette transport.  Type-level fusion is not a substitute for (3.2).

### Proposition 3.3 (non-equivariant spread bound)

Let one packet be internally simple: its declared resources are pairwise
distinct within every species/rank class.  Suppose it contains `M_s`
resources of class `s`.  There exist `H` coordinate relabellings with no
repeated declared resource if

```text
(H-1) sum_s M_s^2/binom(k,s) < 1.                  (3.3)
```

### Proof

After `j` packets have been selected, choose a uniformly random coordinate
permutation for the next one.  For a fixed new rank-`s` resource and a fixed
old one, equality has probability `1/binom(k,s)`.  A union bound over at
most `j M_s^2` pairs gives failure probability at most the left side of
(3.3) with `H-1` in place of `j`.  Hence a legal next relabelling exists;
iterate.  QED.

Condition (3.3) is only a sufficient spread estimate.  It becomes tight at
low ranks and does not by itself stock an extreme `Theta(k)` block.  The
orbit criterion is the appropriate exact replacement when a compatible
free symmetry is available.

### Corollary 3.4 (one complete open-body bank in a protected factor)

Work in the odd middle-levels host on a ground set of order `k=2r-1`.
One arbitrary-hole parity-sweep packet cuts into at most three
strict-positive paths, each of length at most `d`, with total length at most
`3d`.  Put

```text
eta=(d+1)^2/binom(k,r)
     +d^2/binom(k,r-1)^(-1)+d^2/binom(k,r+1)^(-1),  (3.4)
```

and, for fixed forbidden banks of respective orders `f_0,f_-,f_+`, put

```text
theta=f_0(d+1)/binom(k,r)
      +f_-d/binom(k,r-1)+f_+d/binom(k,r+1).         (3.5)
```

If

```text
k-r>=d,             theta+2eta<1,             6d<=r-2, (3.6)
```

then all local owner, lower-`q1`, and upper-`q1` resources of that packet
have pairwise-disjoint literal realizations avoiding the fixed banks, and
their incidence lift is contained in a spanning middle-levels two-factor.

### Proof

For a prescribed path of length `ell`, the family of monotone geodesic
owner paths in Theorem 2.1 has order

```text
binom(k,r)(r)_ell(k-r)_ell.                         (3.7)
```

Double counting under `Sym(k)` shows that the fraction using a fixed owner,
lower colour, or upper colour is, respectively,

```text
(ell+1)/binom(k,r),
ell/binom(k,r-1),
ell/binom(k,r+1).                                  (3.8)
```

The union bound first removes at most a `theta` fraction for the fixed
banks and at most an `eta` fraction for each previously selected path.
There are at most three paths, so (3.6) permits greedy selection.

The incidence lift of a Johnson path of length `ell` has `2ell` edges.
The selected paths are owner/lower-disjoint, hence their union has maximum
degree at most two.  Its total incidence-edge count is at most
`6d<=r-2`; the small
protected-factor theorem therefore extends it to a spanning two-factor.
QED.

Corollary 3.4 stocks all `O(d)` roles of one actuator without appending new
owners.  It does not stock an unbounded multiplicity block, prescribe the
factor's component order, or preserve deep-shadow/common-cap guards.

The resource-disjoint part does extend to the complete polynomial-size
actuator bank, although protected-factor extension does not follow.

### Corollary 3.5 (all canonical actuator bodies have dispersed owner/q1 stock)

Assume the triangular regime

```text
r=ceil(k/2),       d=Theta(sqrt(k)).                  (3.9)
```

Let `A(k)<=k` arbitrary-hole packets be prescribed, so that cutting their
constituent cycles gives at most `Q<=3k` strict-positive paths.  Let the
fixed forbidden owner/lower/upper banks have polynomial order in `k`.
Then, for all sufficiently large `k`, every path has a simultaneous literal
lift and all selected owner, lower-`q1`, and upper-`q1` resources are
pairwise distinct and avoid the fixed banks.

### Proof

Here `k-r>=d` eventually.  All three binomial denominators in (3.4)--(3.5)
are exponential in `k`, whereas `d`, `Q` and the forbidden-bank orders are
polynomial.  Hence

```text
theta+(Q-1)eta=o(1)<1.
```

Apply the greedy proof of Corollary 3.4 to all `Q` paths.  QED.

Thus the complete `O(kd)` occurrence stock creates no owner or adjacent-
palette collision.  The strands are still disconnected protected data;
Corollary 3.5 does not place their union in one spanning factor.

## 4. Exact common-cap and common-basis completion

Resource injectivity does not imply that a background compiler matching
survives.  The following two min--max statements are the exact missing
quantifiers.

### Theorem 4.1 (equivariant residual common-cap theorem)

Let `G=(L,R,E)` be a finite bipartite allowed-cell graph, and let `Gamma`
act by automorphisms preserving its shores.  Let `F` be a `Gamma`-invariant
forced matching supplied by an orbit packet, and delete its incident
vertices.  Write the residual graph as `G_F`.

For every residual edge orbit `eta` and vertex orbit `O`, let

```text
d^L_(eta,O)=number of eta-edges at one left vertex of O,
d^R_(eta,O)=number of eta-edges at one right vertex of O.  (4.1)
```

These numbers are well defined.  Then `G_F` has a matching saturating both
shores if and only if there are nonnegative numbers `w_eta` satisfying

```text
sum_eta d^L_(eta,O) w_eta=1   for every left orbit O,
sum_eta d^R_(eta,O) w_eta=1   for every right orbit O. (4.2)
```

### Proof

If a perfect matching exists, average its incidence vector over `Gamma`.
The result is a `Gamma`-invariant fractional perfect matching, constant on
each edge orbit, and gives (4.2).

Conversely, assign weight `w_eta` to every edge in orbit `eta`.  Equations
(4.2) give a fractional perfect matching of `G_F`.  The bipartite matching
polytope is integral, so `G_F` has an integral perfect matching.  QED.

Thus an orbit-compressed common-cap audit is a finite quotient
transportation system.  Merely checking pointwise nonempty caps, total
capacity, or separate marginal Hall systems is weaker than (4.2).

### Theorem 4.2 (forced common-basis cut)

Let `M_1,M_2` be matroids of common rank `R` on a finite ground set `E`, and
let `F` be a forced set independent in both.  There is a common basis
containing `F` if and only if

```text
min_(X subseteq E-F)
 [r_(M_1/F)(X)+r_(M_2/F)((E-F)-X)] >= R-|F|.       (4.3)
```

### Proof

Contract `F` in both matroids.  A common basis containing `F` is exactly a
common independent set of order `R-|F|` in the two contractions.  Edmonds'
matroid-intersection min--max theorem gives (4.3).  QED.

Theorem 4.2 applies to a prepared private/aligned host face genuinely
described by two matroids.  It must not be applied to the general grouped
three-resource face, which contains matroid three-parity/three-dimensional
matching.  In that face (4.3) is only a relaxation.

### Theorem 4.3 (exact protected two-factor cut)

Let `G=(L,U,E)` be a balanced bipartite incidence host, and let `P subset E`
be a prescribed protected bank with maximum degree at most two.  Put

```text
b(v)=2-d_P(v),       G_0=G-P.                         (4.4)
```

Then `P` extends to a spanning two-factor of `G` if and only if, for every
`S subseteq L`,

```text
sum_(x in S)b(x)
 <= sum_(y in U) min{b(y),d_(G_0)(y,S)}.             (4.5)
```

### Proof

The completion is exactly a bipartite `b`-factor in `G_0`.  The total
demands on the two shores agree because `G` is balanced and every edge of
`P` contributes once on each shore.  The bipartite Ore--Ryser theorem is
therefore equivalent to (4.5).  QED.

For the full dispersed bank of Corollary 3.5, (4.5) is the exact remaining
protected-host cut.  Pairwise resource disjointness does not imply it.  For
the one-packet bank of Corollary 3.4 it follows from the stronger size bound
`|P|<=r-2` supplied by the small protected-factor theorem.

## 5. The exact protected-stock theorem and the remaining seed

### Theorem 5.1 (conditional zero-accumulation stock theorem)

Fix one arbitrary-hole actuator body and a cyclic group `Gamma`.  Suppose
there is a seed packet `P` satisfying all of the following.

1. `P`, including every internal join, is already one literal open packet.
   Its translates introduce no source cells beyond their main owner bank.
   Equivalently, every internal collar cell has been counted as an ordinary
   bank owner/resource rather than as excess length.
2. Every owner, adjacent palette colour, protected upper/deep witness and
   addressed compiler cell used or returned by `P` is included in `R(P)`,
   and `P` is orbit-simple for those species.
3. The connector of Theorem 3.2 is literal and guard-complete; in particular
   it carries the lower-palette change rather than treating a type-level
   `C4` as transparent.
4. The forced common-cap cells form a matching and the quotient system
   (4.2) is feasible.  If a common-basis face is also required, its forced
   set satisfies (4.3).  These two completions are either on disjoint
   resources, are two descriptions of the same selectable completion, or
   are supplied with an explicit joint-compatibility certificate; separate
   marginal feasibility is not enough.
5. Every old protected witness changed by the packet has a named returned
   witness in the same translate, and these returned witnesses are among
   the orbit-simple resources in item 2.
6. The full translated incidence bank satisfies the Ore--Ryser cuts (4.5),
   unless the spanning protected factor is already included in item 1.  Its
   residual choices are resource-disjoint from item 4, or the hypothesis
   includes one joint certificate for the factor and compiler completions.

Then all `|Gamma|` actuator copies are installed in one cyclic one-copy
owner bank, with distinct lower and upper `q1` colours, no literal sidecar
proportional to `|Gamma|`, and one exact common-cap matching.  Opening the
cycle costs only the standard depth-`d` collar plus the explicitly declared
bounded endpoint state.

### Proof

Theorem 3.1 gives simultaneous injectivity of every declared physical and
guard resource.  Theorem 3.2 gives one owner chronology rather than
`|Gamma|` packet components.  Item 5 proves protected witness preservation
translate by translate.  Theorem 4.1 completes the residual common-cap
matching, Theorem 4.2 supplies the common basis when applicable, and item 6
gives the required protected two-factor.  The only linearization cost is the
ordinary collar for opening one cyclic
depth-`d` source.  QED.

This theorem is not vacuous bookkeeping: it identifies the exact finite
object whose existence would convert the uniform age actuator into a
protected Catalan stock with no accumulating sidecar.  But none of the
current quotient theorems constructs item 2 or item 3.  In particular:

* the canonical same-owner age lift repeats owners;
* independently physicalized strands need not have disjoint palettes;
* common-entry age fusion fails as a palette-transparent Johnson `C4`;
* pointwise source-cap positivity does not imply (4.2); and
* arbitrary fixed protected tickets need not extend to a Catalan factor.

Accordingly, the exact remaining seed theorem is:

> Construct one guard-complete orbit-simple positive-age seed rail whose
> endpoint voltage is a generator and whose forced common-cap/common-basis
> data pass (4.2)--(4.3).

The alternative is a sharp obstruction: exhibit one vertex-orbit equation
in (4.2), one contracted rank cut in (4.3), or one unavoidable resource
stabilizer/orbit collision from Theorem 3.1.

## 6. Correct implication boundary

Proved unconditionally:

* literal owner-simple, lower-`q1`-injective and upper-`q1`-injective
  realization of every strict-positive actuator body of at most `d`
  transitions;
* exact orbit-simplicity criterion for a full translated stock;
* exact unit-voltage concatenation once one guarded connector exists;
* exact equivariant common-cap quotient equations; and
* exact forced two-matroid common-basis rank cuts; and
* the exact Ore--Ryser cut for extending the dispersed strand bank to a
  spanning protected two-factor.

Proved conditionally:

* a zero-accumulation protected stock from one orbit-simple,
  guard-complete, unit-voltage seed satisfying the matching/rank cuts.

Not proved:

* existence of that seed in the canonical Catalan/PBBS host;
* physical fusion by bounded `C6`/longer packets for every multiplicity;
* preservation of arbitrary-width upper witnesses without the named guard
  map;
* the general grouped three-resource common-basis face; or
* `B(k)+O(1)` or exact equality for all `k`.

Neither invariant fractional circulation nor aggregate integer rank-count
rounding is on this list: they are closed by the monotone-rotor theorem and
its buffered semigroup sequel.  For the rotor route, the first missing
operation is NRFC: a one-copy occurrence-labelled rethreading and
owner/nested-target colouring of the aggregate type slots, equivalently an
OFHT transversal with zero selected-state Hall deficiency.  It is followed
by the Ore--Ryser, residence, deep-shadow and common-cap rows above.
