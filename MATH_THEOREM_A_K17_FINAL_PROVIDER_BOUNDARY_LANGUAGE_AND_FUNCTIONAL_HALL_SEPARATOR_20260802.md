# `k=17`: final-provider boundary language and the complete functional-Hall separator

**Date:** 2026-08-02  
**Lane:** A, pure theorem/audit  
**Status:** proof-audited symbolic reduction for the frozen round02
Hamming-two face.  No SAT instance is built or solved here.

## 1. Frozen finite input and purpose

The following ledger is taken as authenticated input:

\[
169426=164323+49+5054.                                      \tag{1.1}
\]

Here `164323` joint-clean banks retain an authenticated semantic q1 core,
the `49` dirty-central banks are independently exact-q1 UNSAT, and `5054`
clean-anchor banks survive the current persistence filter.  This note makes
no new finite claim about those `5054` banks.  It gives a proof-safe semantic
separator to be applied to D's literal final-provider reconstruction.

The point is to strengthen the library in three ways which equality of the
old core trace misses:

1. a new local atom may be forced dead by the unchanged exterior;
2. the same obstruction may reappear on different occurrence-labelled
   endpoints or colours; and
3. a disturbed small core may still lie behind a new fan, implication
   bicycle, or functional Hall shore.

None of the tests below uses equality of masks, equality of provider degrees,
or mutable rebuilt-piece numbers.

## 2. The native q1 object and the reconstruction contract

For a final bank `B`, let `P(B)` be its physical path pieces and

\[
             S(B)=\{(p,\epsilon):p\in P(B),\epsilon\in\{0,1\}\}
                                                                  \tag{2.1}
\]

its oriented states.  The complete final atom atlas is

\[
 \mathcal A(B)\subseteq S(B)\times S(B)\times C(B),             \tag{2.2}
\]

where an atom `e=(t(e),h(e),c(e))` is one literal Johnson/residence-legal
directed seam with selected lower colour `c(e)`.  A q1 selection is a set
\(M\subseteq\mathcal A(B)\) satisfying

* exactly one of `(p,0),(p,1)` is selected for every piece `p`;
* a selected state has exactly one outgoing and exactly one incoming atom,
  and an unselected state has neither; and
* every selected lower colour occurs on exactly one chosen atom.

These are precisely the native orientation, tail, head and lower-colour rows
of the exact q1 formula.  Sequential-counter variables are an encoding
device and are not part of the semantic object.

### Definition 2.1 (proof-grade final-provider reconstruction)

A reconstruction of `B` is **proof-grade** when it exports:

1. every oriented state by an immutable occurrence key and its complete
   ordered owner trace;
2. every atom of (2.2), including geometry--palette and two-endpoint atoms
   which exist only after both recuts;
3. the literal tail, head and lower-colour resource of every atom;
4. the final active orientation and colour rows, with multiplicity; and
5. a bijective audit from those native objects to the emitted q1 variables
   and clauses.

The key may contain a base, side, endpoint owners, orientation and cut data;
it may not be a mutable dense-piece number.  Omitting an atom is safe only
with a retained physical impossibility or blocker certificate.

All later theorems are conditional on this contract.  In particular, a
singleton-child union is not a reconstruction of a two-recut bank.

## 3. Resource-relabelled guarded minors

The old persistence test fixes the canonical occurrence map.  A stronger
test permits an obstruction to move.

An authenticated core `K` has literal variables with complementation,
positive exact-one rows, negative capacity/conflict clauses, and named
blockers for omitted providers.  A **typed guarded-minor embedding** of `K`
in the final bank consists of

* a complement-preserving injection of core literals into final
  occurrence-labelled atom/orientation literals;
* maps of tail rows to tail rows, head rows to head rows, colour rows to
  colour rows, and orientation pairs to orientation pairs;
* preservation of all incidences and all equalities among shared resources;
* preservation of every negative clause, either literally or as an entailed
  final clause; and
* for every mapped positive row, a blocker proof for every final provider
  outside the mapped core row.

The resource maps need not fix endpoint masks or colour names.  They must be
typed and incidence-preserving.

This statement is about a decoded native core.  If a stored proof core still
contains sequential-counter or other encoding auxiliaries, then either those
variables and their defining clauses must also be mapped clause by clause, or
the proof must first be re-expressed as an authenticated native resource core.
The visible native incidences alone do not certify an arbitrary auxiliary
DRAT core.

### Theorem 3.1 (mobile guarded-core persistence)

If an authenticated UNSAT core has a typed guarded-minor embedding in the
final provider system, then the final q1 formula is UNSAT.

#### Proof

Resolve each enlarged final positive row against the certified blockers of
its extra providers.  The remaining positive clauses, negative clauses and
complement pairs are an isomorphic copy of `K`.  Substituting the final
literals into the stored refutation proves a contradiction.  Resource names
play no logical role beyond the incidences preserved by the embedding.
\(\square\)

Thus a `reference_endpoint` or `palette_toggle` flag is a reason to search
for a new embedding, not a reason by itself to rebuild the full formula.
This theorem is complete for embeddings of a stored abstract core and is
not complete for q1 infeasibility.

## 4. Exact exterior boundary language

The most useful common interface is obtained by eliminating the unchanged
exterior once.

Fix any finite family `B` of final banks, for example the `5054` survivors.
Put every state, atom, resource row or incidence which changes anywhere in
the family into the **variable region**.  Every unchanged atom and clause is
in the **exterior**.  Every row or orientation pair meeting both regions is
an **interface resource**.  If an object cannot be proved unchanged, it is
put in the variable region.  This convention is conservative only in size,
not in logic.

For an exterior partial selection `M0`, its boundary signature records, on
every interface resource,

* its used tail, head and colour capacity;
* its chosen boundary orientation bits; and
* every protected Boolean state occurring in a cross clause.

Let `E` be the set of signatures realized by exterior selections satisfying
all exterior-only rows.  For a final bank `B`, let `I_B` be the set of
signatures realized by variable-region selections satisfying all
interior-only rows.  Say two signatures are complementary when together
they satisfy every interface exact-one, at-most-one, orientation and
protected row.

### Theorem 4.1 (exact boundary gluing)

The final q1 formula of `B` is feasible if and only if there are
\(e\in E\) and \(i\in I_B\) with complementary boundary signatures.

#### Proof

Restricting any q1 selection to the exterior and variable atoms gives the
two signatures and satisfies every interface row jointly.  Conversely,
the union of two selections with complementary signatures satisfies every
exterior-only, interior-only and interface row.  These are all native q1
rows, so the union is a q1 selection. \(\square\)

The theorem remains true if the interface is the whole formula; a useful
small interface is an additional structural fact, not an assumption.  The
exterior language is fixed across the chosen finite family and can therefore
support a reusable core library.

## 5. Exact blockers and fan compatibility

A final atom `a` is **exterior-blocked** if no signature in `E` is compatible
with its occurrence/resource footprint and implied orientation.  More
generally, a tuple `T` of atoms is blocked if no exterior signature is
compatible with their joint footprint.  By Theorem 4.1 every such statement
is an entailed clause

\[
                         \bigvee_{a\in T}\neg a.          \tag{5.1}
\]

This includes singleton blockers, but also pair and higher blockers invisible
to unit propagation.

Blocker closure repeatedly performs the following sound operations:

1. delete every atom with an entailed singleton blocker;
2. force the sole live provider of an exact-one row;
3. after forcing an atom, delete every competitor on each resource it uses;
4. add any newly exposed tuple blocker from the exterior language; and
5. stop at contradiction or at the least fixed point.

The operator is monotone on the set of deleted/forced literals, hence its
least fixed point is independent of processing order.

Let `r,s` be two required rows after closure, with complete final provider
sets `A_r,A_s`.  Define the occurrence-labelled compatibility graph

\[
 a\sim_B b
 \quad\Longleftrightarrow\quad
 a,b\text{ are resource-compatible and some exterior signature is
 compatible with }\{a,b\}.                                \tag{5.2}
\]

### Theorem 5.1 (exterior fan separator)

If the graph in (5.2) has no edge, the final q1 formula is UNSAT.

If compatibility in (5.2) is strengthened to mean that `a,b` together
extend through **all** rows other than the two displayed positive rows, then
nonemptiness is also sufficient for global q1 feasibility.

#### Proof

Every solution chooses providers `a in A_r,b in A_s`; their exterior
restriction witnesses `a~_B b`.  Thus an empty graph is impossible.  Under
the strengthened definition, an edge already includes a completion of all
remaining rows, and adding the two providers completes the formula.
\(\square\)

The ordinary one-colour dual fan and the four-atom bow tie are special cases.
New atoms matter only through their final occurrence-labelled compatibility,
not through the change in a row degree.

## 6. Entailed binary clauses and bicycle closure

Let `Q_B` contain every binary clause which is either a literal clause of
the reconstructed final formula or a boundary nogood with an independently
replayable derivation from the exterior language.  Thus
`not a or not b` is present for an incompatible provider pair, and an
enlarged positive row contributes a binary coverage clause only after all
other providers have certified blockers.

Form the implication digraph of `Q_B` in the usual way.

### Theorem 6.1 (semantic bicycle separator)

If some literal and its complement lie in one strongly connected component
of the implication digraph, the final q1 formula is UNSAT.

This criterion is invariant under occurrence-labelled, typed relabelling of
the bicycle.

#### Proof

Every clause of `Q_B` has a noncircular derivation from final literal clauses
or the separately certified exterior relation.  The two directed
paths force `x=>not x` and `not x=>x`; neither truth value is possible.
Typed relabelling preserves the two implications. \(\square\)

The converse is false in the presence of positive rows of size at least
three.  A noncontradictory binary closure therefore promotes a bank; it does
not certify feasibility.

## 7. Small resource-Hall witnesses

Fix an integral choice of one orientation per piece.  On one demand shore,
for example the selected tail states, let `X` be a set of required rows.
Let

\[
 \kappa_B(X)=\max\{|M|:M\text{ assigns distinct rows of }X\text{ to
 pairwise resource-compatible final atoms and is exterior-compatible}\}.
                                                                  \tag{7.1}
\]

Only one shore is counted in `X`; an atom's head, colour, orientation and
protected resources are capacities.  This prevents the invalid practice of
counting one seam once for each of several shores it satisfies.

### Theorem 7.1 (resource-Hall separator)

If

\[
                         \kappa_B(X)<|X|,                 \tag{7.2}
\]

then the final q1 formula is UNSAT.

Scanning every occurrence-labelled `X` with `|X|<=k` is complete for
obstructions having such a `k`-row resource-Hall witness.

#### Proof

The atoms chosen by any q1 solution on the rows `X` form an admissible family
in (7.1) of size `|X|`.  This contradicts (7.2).  The second assertion is
the definition of an exhaustive scan of that witness class. \(\square\)

A finite certificate for (7.2) must prove the displayed packing upper bound
(for example by an exact matching/min-cut certificate or an exhaustive
bounded tuple table).  Merely failing to find `|X|` atoms is not a proof.

For `|X|=2` this is the fan compatibility test.  For larger `X`, pairwise
compatibility alone is insufficient: three atoms may be pairwise compatible
but jointly consume one protected or orientation resource.  The quantity
`kappa_B` must use joint occurrence-labelled footprints.

## 8. A complete functional-Hall cylinder separator

The preceding library is sound but need not decide all `5054` banks.  The
following min--max separator is complete.

Let `P_B` be the finite set of integral orientation/head--colour masters:
a master chooses one orientation of every piece and assigns the selected
lower colours bijectively to the selected head states, respecting all
master-level rows.  For `p in P_B`, let `G_p` be the bipartite graph whose
left vertices are the selected tail states and whose right vertices are the
chosen `(head state,lower colour)` columns; a final atom gives the
corresponding edge.

A **master cylinder** is any subset `C subseteq P_B` specified by partial
occurrence-labelled master decisions.  A Hall cylinder certificate is a
pair `(C,X)` such that `X` is selected throughout `C` and

\[
                  |N_{G_p}(X)|<|X|\qquad(p\in C).         \tag{8.1}
\]

### Theorem 8.1 (complete cylinder-cover alternative)

The final q1 formula is UNSAT if and only if either `P_B` is empty or there
exists a finite family of Hall cylinders `(C_j,X_j)` such that

\[
                 P_B=\bigcup_j C_j                     \tag{8.2}
\]

and (8.1) holds on every cylinder.

If no such cover exists, there is a master `p` for which `G_p` has a perfect
matching; that matching is a literal q1 selection.

#### Proof

For a fixed master, the remaining q1 choice is exactly a predecessor
matching between its selected tails and head--colour columns.  Hall's theorem
says it exists exactly when no deficient `X` exists.  Hence a cover by
deficient cylinders excludes every master.  Conversely, if the formula is
UNSAT, every master has a deficient Hall shore; taking one singleton
cylinder for each master gives (8.2).  If some master is uncovered by all
deficiencies, Hall supplies its perfect matching. \(\square\)

This is an exact semantic decision theorem, not a claim that the cylinder
cover is automatically small.  Blockers, fans, bicycles and small Hall
minors are compressed ways of covering many masters at once.

## 9. Proof-safe separator for the `5054` survivors

For each clean-anchor survivor, the next audit may proceed without a generic
q1 CNF rebuild as follows.

1. Reconstruct the complete final atlas under Definition 2.1.
2. Apply exact exterior blocker closure.
3. Search for **mobile** typed guarded-minor embeddings of every stored core,
   rather than only the canonical old embedding.
4. Recompute the complete compatibility matrices of all stored forced-row
   pairs; reject an empty matrix.
5. Build the implication graph from literal and entailed binary clauses;
   reject a contradictory SCC.
6. Test the stored and newly exposed small resource-Hall shores.
7. For every remaining bank, use the functional-Hall cylinder alternative.

Each rejection carries one of four independently replayable certificates:

* a resource-relabelled guarded minor plus its blocker leaves;
* an empty occurrence-labelled fan compatibility table;
* two implication paths between a literal and its complement; or
* a Hall shore, together with the master cylinder on which it is deficient.

An exhaustive cylinder cover is a complete q1-UNSAT certificate.  A master
and perfect matching is a complete q1-SAT certificate.  No conclusion about
rank-ten tickets, deeper upper decks, residence, topology or the compiler is
part of this theorem.

## 10. Completeness and false-positive boundary

The separator has zero false UNSAT rejections provided that

1. the final provider reconstruction is complete;
2. every blocker or binary nogood is accompanied by literal clause or exact
   boundary-language provenance;
3. every compatibility/Hall computation uses joint resource footprints; and
4. every cylinder claim is checked for all integral masters in that cylinder.

The following replacements are unsound:

* mask equality for occurrence identity;
* provider-degree equality for provider-set equality;
* individual extendability for joint tuple compatibility;
* pairwise compatibility for a three-or-more-row Hall test;
* retaining a binary coverage implication after an unblocked third provider
  enters its row; or
* declaring a cylinder deficient from a sample of its masters.

The guarded-minor, fan, bicycle and bounded-`k` Hall stages are complete only
for their named certificate classes.  Passing them has no positive meaning.
The complete logical boundary is Theorem 8.1.  Its size may equal that of a
full q1 decision in the worst case; the theorem promises reusable semantic
compression, not a complexity collapse.
