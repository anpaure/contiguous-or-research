# `k=17`: occurrence-labelled q1-core persistence and exact two-recut separation

## 1. Scope and frozen input

This note is a symbolic theorem for screening the joint-zero-265-clean children of the
authenticated `round02` cut bank.  It uses the following finite facts only as
input:

* the complete single-recut face is q1-infeasible;
* all 65 compatible pairs of the twelve individually visible socket escapes
  are q1-infeasible;
* the latent geometry--lower-colour supplier join has been included, so the
  current Hamming-two catalogue is not restricted to pairs of visible arms;
* the anchored sweep contains 349,642 compatible pairs, of which 169,426 pass
  the joint zero-265 ledger.

No q1 conclusion about those 169,426 banks is inferred from the counts.  The
purpose of the theorem below is to decide, without rebuilding a full q1 CNF,
exactly those children which retain an already authenticated obstruction core.

The statement is deliberately occurrence-labelled.  A physical occurrence is
identified by its immutable base, side, endpoint-owner masks, orientation and
cut data.  A mutable dense-piece number is never an identifier.

## 2. The seam formula and a core trace

For a final bank `B`, let

* `O(B)` be its oriented physical occurrences;
* `E(B)` be its complete set of legal directed seam atoms;
* `gamma(e)` be the lower-colour resource of `e`;
* `tau(e),eta(e)` be its tail and head socket occurrences; and
* `R(e)` be the complete tuple of resources used by `e` (tail socket, head
  socket, lower colour, and any fixed protected resource row).

The q1 formula `F(B)` consists of the orientation, endpoint exact-one, colour
capacity and protected-resource clauses generated from this complete atlas.
The optional rank-ten clauses strengthen `F(B)`; they are irrelevant once a
q1-unsatisfiable subformula has survived.

An **authenticated core** `K` stores more than a set of masks.  It stores

1. its occurrence-labelled Boolean literals, with the complementation map;
2. every positive exact-one row used by the proof and the *complete effective
   atom list* of that row;
3. every capacity/conflict clause used by the proof, with its resource label;
4. for every atom deleted as locally impossible, a retained forcing
   certificate proving that atom false; and
5. either its literal CNF clauses or one of the semantic certificates in
   Sections 4 and 5.

The **core trace** `Tr_K(B)` is the restriction of these data to a new bank,
after applying the canonical occurrence map.  In particular, a positive row
is part of the trace with its entire effective atom set, not merely with its
old atoms.

## 3. General persistence and separation

### Theorem 3.1 (literal core persistence)

Let `K` be an authenticated unsatisfiable CNF core of `F(B)`.  Suppose that for
a new bank `B'` there is an injection `phi` from the variables of `K` to
occurrence-labelled variables of `F(B')` such that

1. `phi(not x)=not phi(x)`;
2. every occurrence and resource label recorded by `K` has the same physical
   meaning after `phi`; and
3. for every clause `C` of `K`, the clause `phi(C)` occurs in `F(B')` (possibly
   as a clause derived from a retained forcing certificate).

Then `F(B')` is unsatisfiable.

#### Proof

The clauses `phi(K)` form a subformula of `F(B')`.  By injectivity and
complement preservation they are isomorphic to `K`, hence unsatisfiable.  A
formula containing an unsatisfiable subformula is unsatisfiable.  \(\square\)

The word "clause" is load-bearing.  If an old binary positive clause
`a or b` becomes `a or b or c`, the old clause is absent unless the retained
core also forces `c=false`.

### Exact two-recut separation

For a possible seam `e`, write its legality in the factored form

\[
  1_{e\in E(B)}=G_B(e)\,P_B(\gamma(e)),                 \tag{3.1}
\]

where `G_B(e)` is the endpoint/Johnson/age predicate and `P_B(c)` says that
the lower colour `c` is selected.  For two recuts `g,h` in distinct bases, a
seam can change because of an individual geometry change, an individual
palette change, or the cross term

\[
\begin{split}
 J_K(g,h)=\{e:\;&e\text{ meets a row or resource of }K,\\
             &G_{B_g}(e)=1,\ P_{B_g}(\gamma(e))=0,\
               P_{B_{gh}}(\gamma(e))=1\}\quad\cup(g\leftrightarrow h).
                                                               \tag{3.2}
\end{split}
\]

This is the latent geometry--supplier join.  It must be computed even when
neither singleton child has a legal escape.

Define `Dist_K(g,h)` to hold when at least one of the following occurs in the
joint child:

* a recorded core occurrence, orientation complement or forced role changes;
* a core atom is deleted or changes a resource label;
* a new effective atom enters a positive row used by `K`;
* a resource capacity or conflict used by `K` changes;
* a forcing certificate for a formerly dead atom ceases to hold; or
* the cross set `J_K(g,h)` is nonempty.

### Theorem 3.2 (exact persistence/separation dichotomy)

If `Dist_K(g,h)` is false, then `Tr_K(B_{gh})=Tr_K(B)` and `K` persists in
`B_{gh}`.  Conversely, if the occurrence-labelled trace of `K` changes, at
least one of the six displayed disturbance events occurs.

#### Proof

Each clause generator in the q1 formula is determined by (i) the physical
occurrences and their two orientations, (ii) the complete legal atom set, and
(iii) the resource labels and capacities.  The first, second, fourth and
fifth disturbance events are exactly the possible changes to (i) and (iii)
or to an old atom.  By (3.1), a new atom entering a recorded row is either an
individual geometry/palette change or the cross term (3.2); these are the
third and sixth events.  If none occurs, every recorded clause and forcing
certificate is identical, so Theorem 3.1 applies.  Conversely, tracing the
first changed datum in the clause-generation order yields one of the six
events.  \(\square\)

This is a separation theorem, not a claim that every q1 obstruction belongs
to the current library.

## 4. The retained dual-fan filter

Let `s,t` be two distinct forced socket demands and let `c` be a unit-capacity
lower colour.  The triple `(s,t;c)` is a **closed dual fan** in `B` when

1. the two occurrence-labelled forced roles `s,t` are present;
2. no legal atom satisfies both socket demands at once; and
3. every legal atom satisfying either one of the two demands uses colour `c`.

### Theorem 4.1 (dual-fan persistence, necessary and sufficient for the named
certificate)

The named certificate `(s,t;c)` proves `F(B)` unsatisfiable if the three
conditions above hold.  For a new bank `B'`, the same occurrence-labelled fan
certificate persists if and only if those three conditions and the unit
capacity of `c` still hold in the *complete* new atlas.

#### Proof

Because no atom covers both demands, any solution must choose two distinct
atoms, one for each demand.  Both consume `c`, contradicting its unit
capacity.  Conversely, a changed forced role, an atom covering both demands,
or an incident atom of another colour invalidates this particular two-demand,
one-colour proof.  (It need not make the global instance feasible.)  \(\square\)

Thus new arms of the same colour do **not** disturb the fan.  A direct seam or
even one different-colour arm does disturb this certificate and sends the bank
to rebuilding; global feasibility is not asserted.

For two recuts the complete fan test must include:

* central-role relocation;
* a locally dirty singleton escape repaired by the other recut; and
* a seam in `J_K(g,h)`, where one recut supplies endpoint geometry and the
  other supplies its lower colour.

The twelve clean singleton escapes alone are therefore not a complete fan
disturbance list.  The frozen latent-supplier join is precisely what makes the
current Hamming-two catalogue complete.

## 5. The implication-bicycle filter

After retained dead-atom certificates are applied, suppose every choice row
used by a core has effective size at most two.  Its exact-one and resource
conflict clauses define the usual implication digraph `I(B)`: a binary clause
`u or v` gives `not u -> v` and `not v -> u`.

An occurrence-labelled **implication bicycle** consists of a literal `x` and
directed paths

\[
                 x\leadsto\neg x,
       \qquad \neg x\leadsto x.                         \tag{5.1}
\]

### Theorem 5.1 (bicycle persistence)

Let `Q` be an authenticated bicycle in `I(B)`.  If a complement-preserving
occurrence map into `B'` preserves every directed arc of the two paths in
(5.1), then `F(B')` is unsatisfiable.  This test is necessary and sufficient
for persistence of that particular occurrence-labelled bicycle embedding.

#### Proof

Every satisfying assignment of a 2-CNF is closed under implication.  If `x`
is true, the first path forces `not x`; if `x` is false, the second path forces
`x`.  Conversely, the stored bicycle embedding is present exactly when all
its vertices, complementation pairs and arcs are present.  \(\square\)

A resource-conflict clause between two retained atoms remains binary when
other atoms are added.  A positive exact-one row behaves differently: adding
a third live atom widens its positive clause and removes the corresponding
binary implications.  Such an atom may be ignored only when a retained
certificate forces it false.  Equality of row degrees is not a substitute
for equality of effective atom identities.

## 6. The core-library filter

Let `L` be a finite collection of independently authenticated literal cores,
closed dual fans and implication bicycles.  For a final joint bank `B'`:

1. construct canonical occurrence labels for the dependency cone of each
   library core;
2. include every individual geometry/palette delta and every latent join
   (3.2);
3. apply the appropriate literal, fan or bicycle persistence test; and
4. reject `B'` as q1-infeasible as soon as one certificate survives.

Only banks rejected by none of the library certificates require a full q1
rebuild.  Rank-ten clauses need be built only after this q1 screen.

### Theorem 6.1 (soundness and exact completeness boundary)

The library filter has no false positive: every rejected bank contains an
explicit authenticated q1 contradiction.  It is complete for the following
property:

> some member of `L` has an occurrence-preserving literal embedding in the
> final bank, or satisfies its stored semantic fan/bicycle predicate there.

It is not complete for q1 infeasibility.  A bank which is not rejected may
retain a differently embedded old core, create a new core, or be globally
infeasible for a reason absent from `L`; it must be rebuilt.

#### Proof

Soundness is Theorems 3.1, 4.1 and 5.1.  The canonical scan checks every
stored occurrence embedding and all of its trace data, so it finds every
library certificate in the displayed class.  Nothing in those theorems says
that `L` contains all unsatisfiable cores.  \(\square\)

## 7. Unsafe shortcuts and false-positive boundary

The following are **not** sound persistence tests:

* unchanged owner masks without unchanged occurrence/side/orientation roles;
* unchanged provider degree without unchanged provider identities;
* survival of the old atoms without checking for new atoms in a positive row;
* equality of colour multisets without equality of resource incidence;
* checking the two singleton children but omitting the latent join (3.2);
* discarding a locally bad singleton recut before its joint compensation is
  evaluated;
* using mutable dense-piece numbers as physical identities; or
* retaining a binary implication after its positive row acquires a third live
  candidate.

Any of these shortcuts can label a genuinely core-disturbing bank as
"persistent" and is therefore a false-positive risk.  The exact filter has
zero such false positives because it uses the final joint atlas in the core
dependency cone.  Its deliberate error is one-sided: failure to recognize an
unsatisfiable bank merely promotes that bank to full rebuilding.

## 8. Consequence for the frozen Hamming-two sweep

The 169,426 joint zero-265-clean children are screened against the
occurrence-labelled core library.  A retained dual fan or bicycle gives a
proof-safe q1-UNSAT verdict without regenerating the million-variable master.
The frozen 13-profile filter certifies 164,323 rows UNSAT and promotes 5,103
to exact building.  The promoted class originally included all 49 clean
banks supported by the seven dirty central anchors.  A later canonical
rebuild and independently checked DRAT audit proves those 49 UNSAT, leaving

\[
       169426=164323+49+5054.                            \tag{8.1}
\]

Thus the present fresh-build frontier is 5,054 clean-anchor banks.  A child
which changes every stored core trace—including a joint-only endpoint seam,
a palette--geometry join or central-role relocation—must receive a fresh
exact q1/rank-ten test.  Any promoted UNSAT verdict should be proof retained
together with the final bank hash, its canonical atom map, the trimmed core,
and the generator metadata needed to add the new core to `L`.

`EXACT_BUILD` is an inconclusive promotion label, never a SAT verdict.  This
theorem does not claim that one of the Hamming-two banks is feasible,
does not infer topology or residence from q1, and does not close circuit or
rethread faces outside the one-for-one two-recut catalogue.

## 9. Guarded-minor strengthening and the complete cross term

The literal-injection formulation above has the following useful
strengthening.  A core atom may be mapped either to the same
occurrence-labelled final atom or to the constant zero.  For every positive
core row, resolve the final provider clause against named retained blockers
for all providers outside the mapped row.  If the resulting simplified core
is unsatisfiable and every exclusion/incidence/unit clause retains its
physical provenance, then the final formula entails that core and is
unsatisfiable.  Deleting an arm can therefore strengthen a certificate; it
need not count as a disturbance.

This **guarded core-minor criterion** is proof-safe because the named blocker
derivations recover every positive core leaf, while the remaining leaves are
literal final clauses.  Substituting these leaves into the stored resolution
refutation gives a final refutation.  It is stronger than exact trace equality
and remains zero-false-rejection.

There are two distinct joint-only atom sets for recuts `g,h`:

\[
\begin{split}
 J^{GP}_K(g,h)=\{e:\;&e\text{ meets a core row},\ G_{B_g}(e)=1,\
 P_{B_g}(\gamma(e))=0,\ P_{B_{gh}}(\gamma(e))=1\}\cup(g\leftrightarrow h),
                                                               \tag{9.1}\\
 J^{EE}_K(g,h)=\{e:\;&e\text{ meets a core row},\
 \tau(e)\text{ is created by }g,\ \eta(e)\text{ is created by }h\}
 \cup(g\leftrightarrow h),                                  \tag{9.2}
\end{split}
\]

where (9.2) is intersected with the final Johnson, age and selected-colour
predicates.  The first is geometry-change times lower-colour supply; the
second is a genuine two-endpoint/two-lock seam.  References above to the
latent cross term are to be read as the union of (9.1) and (9.2).  A
singleton-child union omits both types and is not a complete separator.

### Theorem 9.1 (exact two-row fan test)

Let `r,s` be the two required rows of any stored successor fan.  After
removing atoms killed by retained blockers, let `A_r,A_s` be their complete
final provider sets.  Put `a~b` when `a` and `b` have a common completion
through all retained endpoint, orientation, colour and protected-resource
rows.  Then the named fan subsystem is feasible exactly when

\[
             \{(a,b)\in A_r\times A_s:a\sim b\}\ne\varnothing. \tag{9.3}
\]

Hence emptiness of (9.3) is an exact persistent UNSAT certificate.  The
one-colour dual fan of Section 4 is its simplest specialization.  This
formulation also covers the stored four-atom bow ties and makes clear that a
new provider matters only if it participates in a compatible transversal.

#### Proof

Any solution selects one effective provider for each required row, and the
selected pair must extend through the shared hard theory, so it gives a pair
in (9.3).  Conversely, `~` was defined by existence of precisely that common
completion.  Thus (9.3) is equivalent to feasibility of the named subsystem.
Its emptiness contradicts every global solution.  \(\square\)

For implication bicycles, the corresponding exact test is entailment of each
stored arc by the final formula.  Equivalently, retain only arcs with intact
clause provenance and test whether some literal and its complement remain in
one strongly connected component.  Provider deletion may create a stronger
unit; provider enlargement destroys a binary coverage implication unless all
new providers have named blockers.

With these strengthenings, the proof-safe candidate set for full rebuilding
is exactly the intersection, over the stored library, of the banks which
destroy every occurrence-labelled guarded-minor embedding of that core.
This is complete relative to the library and still deliberately incomplete
for global q1 infeasibility.

## 10. Symbolic critical-pair set

For a stored core `K`, let

* `Occ_K` be the recuts changing a core occurrence, orientation or role;
* `Clause_K` be the recuts changing an old atom, exclusion, implication,
  unit, or named blocker used by the guarded minor;
* `Geom_K(c)` be the **unfiltered** recuts creating raw endpoint geometry of
  colour `c` into a positive core row; and
* `Pal(c)` be the recuts changing the selected multiplicity of `c`.

Let `End_K` be the unordered pairs whose two new endpoint states support an
atom in a positive core row.  Define

\[
\begin{split}
 \mathfrak D_K={}&\{\{g,h\}:g\text{ or }h\in Occ_K\cup Clause_K\}\\
 &\cup\bigcup_c\bigl(Geom_K(c)\bowtie Pal(c)\bigr)\cup End_K,       \tag{10.1}
\end{split}
\]

where `bowtie` keeps distinct-base pairs and the final multiplicity test.

### Theorem 10.1 (critical-pair separation)

Every pair outside `D_K` retains the guarded core minor `K`.  Every pair
which changes that guarded-minor trace belongs to `D_K`.  Consequently a
bank can reach full rebuilding only if it lies in

\[
                    \bigcap_{K\in\mathcal L}\mathfrak D_K.         \tag{10.2}
\]

#### Proof

The first line of (10.1) contains every unary change to a recorded clause or
its occurrence/provenance.  If neither recut makes such a change, a new atom
in a positive core row can arise only by the factored geometry--palette join
(9.1) or the two-endpoint join (9.2), which are the second line.  These are
all clause constructors of the final q1 theory.  Thus a pair outside
`D_K` leaves every guarded-minor leaf entailed and the core persists.  Reading
the first changed leaf in the opposite direction places every trace-changing
pair in one of the same sets.  Finally, a bank avoiding `D_K` for even one
library core is already refuted, proving (10.2).  \(\square\)

The sets in (10.1) are conservative only when blocker entailment is replaced
by a syntactic footprint test: that replacement can send an actually
persistent bank to rebuilding, but it cannot justify rejection.  In
particular, `Geom_K(c)` must not be filtered by singleton zero-265
admissibility, and `Pal(c)` must track multiplicity rather than mere mask
presence.
