# Independent audit: the `B+1` dual join tree, reserve Hall, and blocker LLL

**Date:** 2026-08-04  
**Audited theorem:**
`MATH_THEOREM_BPLUS1_OCCURRENCE_SECTION_DUAL_JOIN_TREE_RESERVE_HALL_AND_BLOCKER_LLL_20260804.md`  
**Theorem SHA-256:**
`9e329db1beeb6614a7ea43e5e18b72fea9619c2c57882b010d977376b49677b9`  
**Method:** independent symbolic recheck from the occurrence definitions.
No finite search, solver, enumeration, or random experiment is used.

## 0. Verdict

**GO at the stated abstract fixed-factor and restricted-menu scopes.**

The four-cycle example really is a joint-selector no-go after all marginal
target and cycle checks pass.  The target-choice dual is exactly equivalent
to rainbow witness selection.  Generalized arc consistency is exact on the
stated running-intersection tree.  Immutable reserve Hall is sufficient for
selector-independent forest extension and is correctly not claimed
necessary for unrestricted extension.  The local-lemma probabilities and
dependency scopes are correct under the explicit within-target
colour-disjointness hypothesis.

Nothing in the theorem proves that the abstract obstruction is Boolean
realizable or that a Boolean all-parameter factor satisfies any positive
host hypothesis.

## 1. Four-cycle obstruction audit

The cycle has edge colours

\[
                         u(e),u(a),u(f),u(b)=R,A,R,B.
\]

Hence an upper-exact section must keep the unique `A` and `B` edges and one
of the two `R` edges.  It automatically deletes the other `R` edge, so it
breaks the unique old cycle without any additional choice.

The unique witness of `X` is `{e,a}` and therefore forces the surviving
`R` occurrence to be `e`.  The unique witness of `Y` is `{f,b}` and forces
it to be `f`.  Either target alone is realized by one of the two sections;
the pair is impossible.  Thus the example does not hide an individually
nonrainbow witness, a protected-pivot conflict, or a component-omission
failure.

Deleting either target relation restores feasibility.  The theorem limits
its minimality statement to this cross-target forced-literal mechanism and
does not assert a classification of all minimal unsatisfiable CSPs.  The
explicit warning that the four-cycle need not be a rooted Boolean factor is
essential and present.

## 2. Dual-CSP audit

Every admissible witness uses at most one occurrence of a fixed colour, so
`rho_I(R)` is a well-defined partial value.  Pivot compatibility is already
enforced when the menus are filtered: if the pivot fixes `(R,p)`, every menu
witness using `R` also uses `p`.

After one witness is chosen for every target, the union is rainbow exactly
when, colour by colour, all defined `rho` values agree.  Relation
`mathcal C_R` imposes precisely this condition.  A witness which does not
use `R` contributes an undefined value and correctly imposes no `R`
restriction.  Unary relations `mathcal D_X` ensure that every target
variable is present even in degenerate scope bookkeeping.  Their natural
join is therefore nonempty exactly when a protected rainbow selector
exists.

This dual equivalence does not yet impose component omission.  The theorem
adds that row only through reserve Hall or through the component bad events
of the local lemma, so no condition is silently dropped.

## 3. Running-intersection audit

For a tree edge `ij`, running intersection makes `S_i cap S_j` the full set
of target variables shared between the two sides.  If a global tuple exists,
each of its relation restrictions always supports the adjacent restriction,
so none can be deleted by semijoin pruning.

Conversely, in a nonempty fixed point every surviving relation tuple has a
supporting tuple across every incident tree edge.  Rooting the tree and
choosing supports recursively gives adjacent separator agreement.
Running intersection then makes all appearances of each target variable
connected, so the local tuples glue to one global witness assignment.  The
proof also justifies the stronger statement that any surviving core tuple
can be prescribed at the root.

For a laminar scope family, all scopes containing a fixed target form a
chain.  The inclusion forest, with disjoint roots joined across empty
separators, is consequently a join tree.  Equality of the two separator
projections means every tuple on either endpoint has support on the other,
so no pruning occurs.  These implications have the correct directions.

The four-cycle correctly prevents an overclaim: its dual scopes are
laminar, but `mathcal C_R` is empty because the two singleton witness
domains demand different `R` occurrences.  Thus structural laminarity alone
does not imply existence.  The six-cycle `RS,ST,RT` example also correctly
shows that disjoint literal witness intervals can acquire a three-cycle of
scopes after repeated colours identify remote occurrences.

## 4. Immutable-reserve Hall audit

The menu envelope `A` contains every edge that any declared witness choice
or the pivot can use.  Therefore an occurrence in

\[
                         (E(K)\cap E_R)-A
\]

is deletable for every menu selector.  Capacitated Hall assigns every old
component one such reserve colour, with colour `R` used at most
`b_R=mu_R-1` times.  Components are edge-disjoint, so choosing a concrete
reserve occurrence for every assignment gives distinct designated edges
even when several components use the same colour.

The selected witness bank uses at most one occurrence of each colour.
Consequently at least `mu_R-1=b_R` occurrences of colour `R` remain outside
the bank.  The designated deletions can therefore be filled to the exact
quota without deleting the bank.  Their complement keeps one occurrence of
every colour and omits one designated edge of every old cycle.  This checks
all four required rows: exact colour, pivot, target survival, and forest.

The reserve Hall inequalities are necessary and sufficient if every
component must receive its designated breaking edge outside the full
envelope `A`.  They need not be necessary after a particular witness
selector is fixed, because unused edges of `A` may then become deletable.
The theorem states this limitation explicitly.

The coherent-envelope corollary is sound: `|A cap E_R|<=1` makes the union
of arbitrary menu choices rainbow, after which reserve Hall applies.  It is
a strong sufficient host property, not a purported weakest one.

## 5. Blocker-LLL audit

The random variables are the independently selected colour occurrences.
For one admissible witness, realization fixes one value in each colour of
its scope, so its probability is the product `w(I)`.  Within one target the
chosen witness scopes are assumed pairwise **colour-disjoint**, not merely
edge-disjoint.  Their realization events are therefore independent, giving

\[
                         \Pr(B_X)=\prod_I(1-w(I)).
\]

Moreover, `B_X` occurs exactly when the deletion complement meets every
witness in that restricted menu.  It is therefore the advertised restricted
blocker-transversal event.  Avoiding it is sufficient for the full target
because every restricted witness is a genuine member of the complete
witness family.

A component can be wholly selected only when its edge colours are distinct.
In that case it fixes one value of each colour coordinate and has the stated
product probability.  A repeated colour asks one coordinate to equal two
different labelled occurrences, so the event is impossible.  An occurrence
outside its protected domain likewise gives probability zero.

Each bad event is measurable with respect to its displayed colour scope.
An event is therefore mutually independent of the sigma-algebra generated
by all nonneighbours in the scope-intersection graph.  This validates the
asymmetric local-lemma application.  Avoiding target bad events retains all
targets; avoiding component bad events breaks every cycle.  The product
section already contains the pivot and exactly one occurrence per colour.

The symmetric inequality is the standard sufficient specialization with
maximum dependency degree `Delta`.  No claim is made that its parameters
hold in the Boolean instance.

In the reserve-decoupled corollary, the local lemma need only produce a
rainbow witness bank, not a forest.  Selecting one realized witness per
target gives a bank contained in a single occurrence section, hence a
rainbow bank.  Immutable reserve Hall then constructs a possibly different
section containing that bank and breaking every cycle.  Removing the
component bad events from the dependency graph is therefore valid.

## 6. Scope and overclaim audit

The theorem establishes neither a universal positive selector theorem nor a
Boolean no-go.  Its exact claims are confined to:

* dual-join equivalence for fixed restricted menus;
* semijoin completeness on an assumed running-intersection tree; and
* the exact Hall criterion for the declared immutable-reserve designation
  class.

Its existence conclusions additionally assume reserve Hall or an explicit
local-lemma inequality.  The document does not infer these from interval
counts, q1 duplicate surplus, Catalan slack, or component Hall after a
different selector.  It also leaves connector topology, switch delivery,
source chronology, residence, lower flags, common cap, and the final
`B+1` bound outside scope.

The phrase "weakest" is correctly qualified: nonempty semijoin core is
weakest only inside a fixed dual join-tree class, and reserve Hall is exact
only for immutable-reserve designations.  No globally weakest Boolean host
property is claimed.

## 7. Input-hash audit

The theorem hash at the top was recomputed after its text was frozen.  The
input hashes recorded in its ledger agree with the exact files read:

* blocker/CSP theorem:
  `e9d32b46c907ef85bf1fb791de57d6d6918fb26746521f91ef876b4d919e4c2e`;
* blocker/CSP audit:
  `818d1155e7391236f266791e0892dc98b520cf81a6399e6f5e8054ddcc1d0530`;
* all-width bank theorem:
  `f44ff6af870e6ef188444193e7c1755bb1441832f3a477a11bc0bda0505d5958`;
* all-width bank audit:
  `cee21191163d10e46452d3a8eee72ed52b6743321f97630d771e4347808c05b9`;
* protected upper-exact forest theorem:
  `b2b3c1dcfdcab1338aaffb2783f8a5edc26b8e21a1358e2604696fedaa8333d1`;
* component-port theorem:
  `401aa24568e869909e332c61d222e72d6a0310c585168484e0b30267d6739392`;
* Catalan Hamilton-path certificate:
  `a6329c0f3e5f1c7dc5e5ab76338ff52a955f874901e282dc1a17fffae4d7a503`.
