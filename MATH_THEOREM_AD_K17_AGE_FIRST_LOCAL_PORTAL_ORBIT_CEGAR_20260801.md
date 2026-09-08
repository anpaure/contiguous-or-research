# Age-first K17 higher-shadow CEGAR by local ordered-turn portals

Date: 2026-08-01  
Lane: AD  
Status: proved local cut theorem and exact ordered-turn/root layer; implementation
and regression scope recorded below.  This note does **not** assert a K17 word.

## 0. Scope and authoritative host

The host in this note is

```text
scratch/build_k17_incidence_bimatching_age_skeleton_20260801.cpp
```

It chooses two directed incidence roles, `D` and `H`, in the
rank-9/rank-8 necklace incidence graph and couples them to the four age
classes and the lower suffix flags.  This is the age-first host.  In
particular, it is not the unordered 51,480-turn incidence host, and it is
not complement-dual candidate 1911.  Candidate 1911 is nonresident and is
used below only to calibrate the old trim-3 oracle: its best opening has
1,989 physical holes, represented by 98 rank-11 and 19 rank-12 orbit rows.
No clause computed from that candidate is imported into the age-first
master.

There is currently no frozen SAT assignment of the full age-first host
which is simultaneously connected, primitive-voltage, and upper-safe.
Consequently the deliverable here is an exact incremental interface: it
accepts only a SAT assignment of that host, replays it, and then emits
semantic clauses for precisely the upper failures it finds.

## 1. Ordered turns and the exact opening companion

Write an incidence orbit as

\[
 e=(o(e),f(e),s(e)),
\]

meaning that the physical copy with owner phase \(g\) is

\[
 \rho^g O_{o(e)}\supset \rho^{g+s(e)}F_{f(e)}.
\]

An ordered nonloop turn is a pair

\[
 a=(d,h),\qquad f(d)=f(h),\quad o(d)\ne o(h).
\]

Its phase-\(g\) physical owner transition is

\[
 X=\rho^gO_{o(d)},\qquad
 Y=\rho^{g+s(d)-s(h)}O_{o(h)}.                 \tag{1.1}
\]

Let \(D_d,H_h\) be the two host role variables and add

\[
 z_a\longleftrightarrow(D_d\wedge H_h).        \tag{1.2}
\]

The exact incidence catalogue has 102,944 such ordered nonloop turns.  A
selected pair of perfect matchings has exactly 1,430 selected `z` atoms,
one through each selected `D` incidence and its unique selected `H`
incidence at that facet.

For every rank-10 rotation orbit \([Q]\), add

\[
 \bigvee_{a:\,[X_a\cup Y_a]=[Q]} z_a.          \tag{1.3}
\]

For each ordered turn introduce a root variable \(o_a\), impose

\[
 o_a\Rightarrow z_a,
 \qquad \sum_a o_a=1,                           \tag{1.4}
\]

and impose the cut-colour restitution row

\[
 o_a\Rightarrow
 \bigvee_{b\ne a:\,[X_b\cup Y_b]=[X_a\cup Y_a]}z_b.       \tag{1.5}
\]

The normalized root copy is the copy whose common facet has canonical
phase zero; equivalently its tail and head owner phases are \(-s(d)\) and
\(-s(h)\).  Equation (1.5) is exact.  One selected turn orbit supplies
every one of the 17 physical phases of its rank-10 colour orbit.  Opening
this canonical-facet copy removes exactly one phase.  That phase survives if and only if a
different selected turn orbit of the same colour is present.

### Theorem 1.1 (exact size)

The ordered companion adds exactly

\[
 3(102944)-1=308831
\]

variables and

\[
 8(102944)+1141=824693
\]

clauses.

#### Proof

There are \(1430\cdot9^2=115830\) ordered same-facet incidence pairs.
The forbidden same-owner pairs comprise the 12,870 diagonal pairs and the
two orientations of each of the eight parallel-incidence unordered loops,
for 12,886 in total.  Hence the ordered nonloop count is
\(115830-12886=102944\).

There are 102,944 `z` atoms, 102,944 roots, and 102,943 Sinz auxiliaries.
The conjunction definitions use three clauses per turn.  The eager
rank-10 deck uses 1,144 rows.  Root implication uses 102,944 rows; exact-one
uses \(3n-3\) rows for \(n=102944\); and restitution uses another 102,944
rows.  Thus the clause count is

\[
 3n+1144+n+(3n-3)+n=8n+1141=824693.\qedhere
\]

The older unordered-turn opening layer is not substitutable: the age
direction distinguishes `(d,h)` from `(h,d)`.

## 2. Trim-3 is an ordinary opened-owner path

Let \(F\) be a physical Hamilton owner cycle and let \(e_*\) be the
canonical-facet-phase-zero copy selected by the root.  Put

\[
 P=F-e_*.
\]

The already-audited source convention is

\[
 \operatorname{int}_3([a,b+3])=[a,b).           \tag{2.1}
\]

Thus the strict-upper source test is exactly the ordinary nonwrapping
owner-interval test on \(P\).  The emitted source start, which is shifted
by two source positions, is separate metadata and must never be used as the
owner cut.

For an upper target \(U\), define

\[
 V_U=\{X\in\tbinom{[17]}9:X\subset U\}.          \tag{2.2}
\]

### Theorem 2.1 (component criterion)

The opened chronology covers \(U\) if and only if some connected component
\(C\) of the induced path \(P[V_U]\) satisfies

\[
 \bigcup_{X\in C}X=U.                            \tag{2.3}
\]

The cyclic chronology covers \(U\) if and only if the analogous statement
holds for \(F[V_U]\).

#### Proof

Every interval with OR \(U\) uses only owners contained in \(U\), hence is
contained in one induced component.  Conversely, an induced component is a
literal contiguous interval.  If its owner union is \(U\), that whole
component is a witness.  If a subinterval already has union \(U\), the
union of the containing component is both a subset and a superset of
\(U\), hence equals \(U\).  The cycle case is identical. \(\square\)

This criterion depends only on the owner order, not on which direction the
path is read.  The age direction is nevertheless fixed elsewhere and is
not freely reversible.

## 3. Exact local portal cuts

Fix an incumbent selected factor \(F^*\).  In the opening case also fix its
selected root atom \(o_*\), delete only that one physical turn copy, and
write \(P^*=F^*-e_*\).  Suppose that a physical target \(U\) is missing.
Let

\[
 C_1,\ldots,C_t
\]

be the components of \(P^*[V_U]\).  In the cyclic-hole case use the
components of \(F^*[V_U]\) instead.  By Theorem 2.1 every component union
is a proper subset of \(U\).

Build the labelled physical portal graph \(G(U,o_*)\) as follows.

* Its vertices are all owners in \(V_U\).
* It contains every physical copy of every master-allowed ordered turn
  whose two endpoints lie in \(V_U\).
* In the opening case the exact canonical-facet-phase-zero root copy is
  omitted.  The other 16 copies of the same quotient turn are retained.
* Every edge is labelled by its quotient atom \(z_a\).

For a set \(K\) of quotient labels, let \(G-K\) delete every edge whose
label lies in \(K\).  In the opening case require that \(K\) omit the root
atom and every atom otherwise forced true by the root assumptions.  This is
automatic for the incumbent-false banks used below.

Here `connected component` deliberately means weak/undirected connectivity:
the two endpoints of an ordered turn are joined after forgetting its
orientation.  This over-approximates directed chronology.

### Theorem 3.1 (undirected cover-separator characterization)

In the monotone **undirected label-reachability relaxation**, the clause

\[
 \neg o_*\ \vee\ \bigvee_{a\in K}z_a            \tag{3.1}
\]

is valid for the target \(U\) if and only if every connected component
\(C\) of \(G(U,o_*)-K\) has

\[
 \bigcup_{X\in C}X\ne U.                         \tag{3.2}
\]

For a cyclic hole the root literal is omitted and the undeleted cyclic
portal graph is used.

#### Proof

If (3.2) holds and the root stays fixed while every `z` in \(K\) is false,
every possible selected interval inside \(U\) lies in one component of
\(G-K\), whose union is proper.  Hence \(U\) cannot be covered.  This proves
the clause.

Conversely, if a component of \(G-K\) has owner union \(U\), enable every
edge label outside \(K\).  The undirected relaxation then has a connected
set with union \(U\) while (3.1) is false.  This proves necessity only for
that relaxation.  A weakly connected directed graph need not contain a
directed interval visiting the required owners, so no converse is claimed
for directed chronology, accumulated-union reachability, or the full
degree/age/topology master. \(\square\)

Let \(B_U\) be all quotient labels having a nonroot physical copy joining
two distinct incumbent components \(C_i,C_j\).  Then \(B_U\) satisfies
(3.2), because after deleting those labels no component can leave one old
\(C_i\).  Every label in \(B_U\) is false in the incumbent: a selected
nonroot edge would already join the two components.  The only selected edge
which can cross after opening is the deleted root copy, and that copy was
explicitly excluded.

Starting with \(B_U\), one may re-enable labels greedily whenever (3.2)
remains true.  The resulting \(K_U\subseteq B_U\) is inclusion-minimal.
Therefore (3.1) is a prime positive implicate of the undirected monotone
cover relaxation.  The claim of primality is deliberately not extended to
directed chronology or the full age/matching master.  The first frozen
implementation emits the full certified bank \(B_U\); greedy prime
minimization is an optional later strengthening, not part of its present
runtime claim.

An independently checkable certificate for a generic minimized row consists
of `U`, the root and suppressed phase copy (if any), and `K_U`: reconstruct
`G-K_U` and verify that every component union is proper.  Optional
minimality witnesses re-enable each one label and exhibit a component whose
union is \(U\).  The present runtime certificate instead records the full
`B_U` atom list and clause; it makes no minimality claim.

## 4. Why ordered turn atoms are retained

It is sound but weaker to project an inactive conjunction

\[
 z_{(d,h)}=D_d\wedge H_h
\]

to one role literal which is false in the incumbent.  If a future solution
activates that turn, the chosen role becomes true.  This gives a valid
incumbent-separating clause.

It is **not** an equivalent encoding.  For example,

\[
 (D_1\wedge H_1)\vee(D_2\wedge H_2)
\]

implies \(D_1\vee D_2\), but crossed choices can satisfy the latter without
activating either turn.  The implementation therefore emits the exact
`z`-clauses (3.1).  Projection is only a documented fallback when a host
does not expose ordered turn atoms.

## 5. Cyclic holes, opening holes, and orbit compression

The separator first audits the selected factor before choosing an opening.

1. If \(F^*[V_U]\) has no component union \(U\), this is a **cyclic hole**.
   The clause is root-free.  Rotation equivariance carries the complete
   component and label certificate from \(U\) to every \(\rho^pU\), so one
   row per target orbit is lossless.
2. If the cyclic factor covers \(U\) but \(P^*\) does not, this is an
   **opening-only hole**.  Its clause must contain \(\neg o_*\).  Changing
   the root can repair the target while keeping the factor fixed, so a
   root-free clause here is false in general.

For ranks 11 through 16 the numbers of target orbits are

\[
 728,364,140,40,8,1,
\]

totalling 1,281.  Thus cyclic regeneration needs at most 1,281 rows, and
only rows for orbits actually absent from the incumbent are emitted.

The chosen root breaks rotation symmetry for opening-only holes.  Their 17
relative phases are retained explicitly.  Equal clauses are deduplicated;
if one literal support contains another for the same root, the larger
clause is Boolean-redundant and may be dropped.  A sparse phase-mask form is
equivalent to at most 17 ordinary clauses per affected orbit.  There is no
claim that a single unguarded orbit row exactly represents all opening
phases.

### Corollary 5.1 (only 126 opening-only physical targets)

Let \(Q=X_0\cup X_1\) be the rank-10 colour of the opened root edge.  If a
target \(U\) has cyclic support but loses all support after that edge is
opened, then

\[
 Q\subseteq U.                                    \tag{5.1}
\]

Indeed every cyclic witness destroyed by the opening traverses the root
edge, so both endpoint owners, hence their union, lie in \(U\).  Therefore
the number of possible opening-only targets at ranks 11 through 16 is at
most

\[
 \binom{7}{1},\binom{7}{2},\binom{7}{3},\binom{7}{4},
 \binom{7}{5},\binom{7}{6}
   =7,21,35,35,21,7,                              \tag{5.2}
\]

or 126 in total.  All larger physical deficits reported by an opening
oracle must contain cyclic-support holes.  Thus the exact lazy interface has
at most 1,281 root-free orbit rows plus 126 root-guarded physical rows per
incumbent, before literal deduplication.

The root deletes one physical copy of its quotient turn, not its whole
orbit.  In particular, \(\neg o_*\) may account only for that exact copy.

## 6. Exact incremental algorithm

On each SAT incumbent the separator performs the following fail-closed
steps.

1. Replay the complete CNF assignment and authenticate the age map and
   ordered-turn/root maps.
2. Verify the selected `D` and `H` perfect matchings, the exact selected
   `z` conjunctions, the selected rank-10 deck, the unique root and its
   distinct rank-10 provider.
3. Run the existing alternating-component and voltage audit.  The theorem
   permits cyclic upper cuts already on a cycle cover, but the first frozen
   implementation conservatively defers **all** upper separation until one
   quotient component and nonzero voltage are present.
4. Expand the 24,310 physical owners and replay their bijection.  Check the
   fixed age direction/residence state before treating the incumbent as a
   positive chronology candidate.
5. Enumerate cyclic upper holes at ranks 11--16 by first arrivals or by the
   equivalent component criterion.  Emit one root-free portal row using the
   full cross-component bank for each missing orbit.
6. For every target having cyclic support, suppress the chosen root copy,
   enumerate opening-only holes, and emit the guarded cross-component rows.
7. If no hole remains, return the scoped upper-pass status.  The current
   separator does not yet serialize one positive witness per target; such a
   compact positive certificate remains a verifier extension.  Rank 10 is
   eager and rank 17 is automatic.

Every emitted row is (a) valid by a stored component-union certificate and
(b) false in the incumbent.  Hence the loop is a sound proof-producing
CEGAR scheme.  UNSAT has theorem scope only after the SAT solver proof and
every semantic cut certificate are independently verified.

Filtering to first-growth turns is unsound.  Along a witness a turn
\(X\to X-x+y\) is a first-growth turn exactly when `y` has not appeared
earlier; a rank-\(q\) witness has exactly \(q-9\) such events, but neutral
router turns may be required to join them.  The component separator retains
both kinds automatically.

## 7. Regression boundary

The old candidate-1911 trim-3 report has best physical deficit

\[
 1666+323=1989.
\]

Its stored phase-core table consists of 98 nonzero rank-11 orbit rows and
19 nonzero rank-12 orbit rows.  This demonstrates the potential compression
from physical masks to orbit rows.  A full lost-phase mask alone does not
prove whether the loss is cyclic or opening-only; the new generator must
recompute that distinction.  Since candidate 1911 fails residence and two
lower colours, it is not a legal source of age-first master cuts.

The unconditional static age-flag certificates likewise have no selected
chronology, voltage, or root.  They validate the static target side of the
host but cannot be fed directly to the opening oracle.

## 8. Remaining gates

Even a positive result from this interface proves only an age-compatible,
connected primitive owner chronology whose **cyclic** lower-q1 palette is
rainbow/exact and whose upper-q1 palette is complete, together with a
source-3-trimmed strict-upper-safe
opening.  The opening itself deletes one lower-q1 facet colour; restoring
that lower address belongs to the generalized compiler.  The interface does
not prove that compiler, suffix correction, common-cap matching, or a
literal universal OR word.

## 9. Frozen implementation and structural audit

The exact sources are

```text
scratch/build_ad_k17_age_bimatching_ordered_trim3_layer_20260801.cpp
  SHA a296f14c346ca72ddc2aef0dde064427de478f217afa2c68d17530e08b92e44d
scratch/separate_ad_k17_age_bimatching_trim3_local_orbit_cuts_20260801.cpp
  SHA 84cb8ffe52419d16a502e470f1a9a2ac6bf88d14277249ded1a02f17a74722d4
scratch/verify_ad_k17_age_bimatching_trim3_local_orbit_cuts_20260801.cpp
  SHA 79edf4c4f83f33757b043bd93c79aa411a75c018b8121dbaa1bd45cf7afe64aa
scratch/compose_ad_k17_age_bimatching_cegar_cnf_20260801.cpp
  SHA 32db7b04ab6cb83cd91a2b33c1122fc6ab7fc047c8aabae664ad788b91a4c246
```

The verifier independently reconstructs the physical factor and target
components, requires the certificate's candidate bank to equal the complete
master-allowed cross-component atom bank, checks the exact root guard and
`z` clause, checks that every actual cyclic/opening hole has exactly one
semantic row, and checks the cut CNF and separator JSON.  It does not reuse
the separator's first-arrival scan for target coverage.  Its worst-case
complete scan is deliberately expensive and must run on H100 CPU.

In the unique H100 directory

```text
/home/amodo/or15/work/ad_k17_age_local_portal_a296f14c_84cb8ffe_20260801
```

the staged-rank7 age base generated 2,655,796 variables and 12,882,305
clauses.  The companion then generated exactly 102,944 atoms, 308,831 new
variables and 824,693 clauses.  Exact composition yielded 2,964,627
variables and 13,706,998 clauses.  The separator and independent verifier
both compiled with O3, `-Wall -Wextra -pedantic`, and zero warnings.  The
empty-clause regression confirms that the dedicated composer preserves an
exact empty semantic blocker.

All run hashes, timing and memory figures are frozen in

```text
scratch/ad_k17_age_bimatching_local_portal_cegar_20260801/run_manifest.json
```

This is a structural PASS only.  No SAT solve was launched in the structural
regression recorded here.  A later exact two-solver round on the composed
formula terminated `UNKNOWN` after 1,800 seconds on both solvers, with
neither a SAT nor UNSAT line; see
`MATH_AUDIT_AD_K17_AGE_FIRST_COMPANION_SAT_PORTFOLIO_20260801.md`.
No runtime cut certificate exists because no authenticated resident
connected age-first incumbent was obtained.  The exact current status of
the global K17 construction therefore remains UNKNOWN.
