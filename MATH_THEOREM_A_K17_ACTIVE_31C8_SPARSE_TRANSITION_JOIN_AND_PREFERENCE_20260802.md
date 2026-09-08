# `k=17`: sparse active-`C8` transition join, exact `3+1`/role sieve, and launch preference

**Date:** 2026-08-02  
**Lane:** A/D, pure theorem and light frozen-ledger audit  
**Status:** exact finite generator and comparison theorem.  No SAT instance is
built or solved.  The theorem concerns the frozen round-02 incidence factor,
the five zero-265 rows, and an authenticated q1 core library only.

## 1. Outcome

The raw two-family simple-`C8` count `49,008,960` is not the right launch
universe.  Activity can be joined from the selected incidence factor before
any path, q1, or successor replay.  Because every rank-eight lower row has
selected incidence degree two, the complete join has the following rigorous
bounds:

\[
\begin{array}{c|r|r}
\text{family}&\text{three/two-transition prefix rows}
             &\text{canonical active packets}\\ \hline
\texttt{STAR}&1,555,840&388,960\\
\texttt{OCTAHEDRAL}&5,445,440&1,361,360\\ \hline
\text{total}&\boxed{7,001,280}&\boxed{1,750,320}.
\end{array}                                                   \tag{1.1}
\]

The frozen star census already gives the exact sharper count `54,463` for
active protected star keys.  Hence, without assuming any unbuilt
octahedral census,

\[
 |\mathcal C_{8}^{\rm active}|
 \le 54,463+1,361,360=\boxed{1,415,823}.                      \tag{1.2}
\]

It also gives `500` active protected star keys meeting the original
`114930` socket dependency cone.  Therefore the complete two-family root-hit
class obeys the conservative bound

\[
 |\mathcal C_{8}^{\rm active,root}|
 \le 500+1,361,360=\boxed{1,361,860}.                         \tag{1.3}
\]

Alignment, true role relocation, the other unconditional-core cones, and
joint zero-265 replay only decrease these numbers.  Thus the active `C8`
join is already below the requested `10^7` frontier, whereas the exact
primary-anchor radius-three universe has `2,909,465,711` supports.

Nothing in (1.1) has yet imposed the old-turn/component realization, final
path validity, aligned `3+1` order, immutable forced-role relocation,
literal chronology/residence if that physical subface is claimed, any of
the five zero-265 rows, any unconditional-core hit, or any successor-core
test.  The prefix columns count rooted transition-join rows; the canonical
columns count closed active directed cycles after the opposite-incidence
anti-join and rotation quotient.

There is no complete active aligned role-relocating two-family artifact in
the frozen tree: the existing exact active count is star-only, and its
numeric `role_rethread` field is not an immutable-role classification.  The
finite join below is the missing launch object.

## 2. Frozen incidence contract

Let `X=[17]`.  Let `F` be the selected rank-eight/rank-nine Boolean incidence
factor.  A selected incidence is written `(C,T)`, where

\[
       C\in {X\choose8},\qquad T\in {X\choose9},\qquad C\subset T.
\]

The frozen factor file has `48,620` selected incidence rows, `24,310`
distinct lower rows, and exactly two selected owners at every lower row.
Thus

\[
                         d_F(C)=2.                            \tag{2.1}
\]

Every incidence has an immutable id and a protected-state bit.  A changed
incidence is legal only when the declared protected state permits its
Boolean status to change.  In the present factor the protected incidences
are selected, so this specializes to the familiar rule that no removed
incidence is protected; the generator should nevertheless use the symmetric
status-change formulation.

An active simple `C8` consists of four distinct lower rows `C_i` and four
distinct circuit owners `T_i=C_i union C_(i+1)`, with indices modulo four.
For one directed phase it removes

\[
                         e_i^-=(C_i,T_i)
\]

and adds

\[
                         e_i^+=(C_i,T_{i-1}).                 \tag{2.2}
\]

Activity means that every `e_i^-` is selected and mutable and every `e_i^+`
is unselected and mutable.  Toggling all eight statuses is atomic.  The four
proper slot subsets are not intermediate banks and receive no zero-265 or
q1 verdict.

The complete simple-`C8` classification has disjoint `STAR` and
`OCTAHEDRAL` families.  They are recovered from the rank of
`intersection_i C_i`, so the family tag is physical and no key can occur in
both joins.

## 3. The star transition join

Fix `S in binom(X,7)` and put `Y=X minus S`, so `|Y|=10`.  Define the
selected mutable transition relation

\[
 R_7(S;a,b)\quad\Longleftrightarrow\quad
 (S\cup\{a\},S\cup\{a,b\})\in F
 \text{ and this incidence is mutable}.                     \tag{3.1}
\]

Here `a,b in Y` and `a != b`.  By (2.1), for fixed `(S,a)`,

\[
                 |\{b:R_7(S;a,b)\}|\le2.                    \tag{3.2}
\]

Form a rooted prefix by the three-way join

\[
 R_7(S;a_0,a_1)\Join R_7(S;a_1,a_2)
                  \Join R_7(S;a_2,a_3),                     \tag{3.3}
\]

requiring the four petals to be distinct.  Close it only when

\[
 R_7(S;a_3,a_0)                                               \tag{3.4}
\]

holds and each opposite incidence

\[
 (S\cup\{a_i\},S\cup\{a_{i-1},a_i\})                        \tag{3.5}
\]

is unselected and mutable.

### Theorem 3.1 (star bijection and bound)

The closed tuples (3.3)--(3.5), modulo cyclic rotation but not reversal,
are in bijection with the active oriented star `C8` keys.  The prefix join
has at most `1,555,840` rows and the canonical active output has at most
`388,960` rows.

#### Proof

For an active star put `C_i=S union {a_i}`.  Its removed incidences give
the four transitions in (3.3)--(3.4), while activity of its added opposite
matching is precisely the anti-join (3.5).  Conversely those rows construct
the literal alternating octagon and its active phase.

There are `binom(17,7)` choices of `S`, ten rooted first petals, and by
(3.2) at most two choices at each of the first three transitions.  Hence

\[
 {17\choose7}\,10\,2^3=1,555,840.                            \tag{3.6}
\]

Every active directed four-cycle occurs at each of its four rooted cyclic
rotations.  The petals are distinct, so those rotations are distinct.
Division by four gives

\[
                    1,555,840/4=388,960.                     \tag{3.7}
\]

Reversal is the other toggle phase and is deliberately not identified.
\(\square\)

## 4. The octahedral transition join

Fix `S in binom(X,6)` and put `Y=X minus S`, so `|Y|=11`.  For an unordered
pair `{a,b}` define

\[
 A_S(\{a,b\})=
 \{c\in Y\setminus\{a,b\}:
 (S\cup\{a,b\},S\cup\{a,b,c\})\in F
 \text{ and is mutable}\}.                                  \tag{4.1}
\]

Again (2.1) gives

                         |A_S(\{a,b\})|\le2.                \tag{4.2}

Start with an ordered pair `(a0,a1)`.  Join

\[
 a_2\in A_S(\{a_0,a_1\}),\qquad
 a_3\in A_S(\{a_1,a_2\}),                                  \tag{4.3}
\]

with all petals distinct.  Close the word when

\[
 a_0\in A_S(\{a_2,a_3\}),\qquad
 a_1\in A_S(\{a_3,a_0\}),                                  \tag{4.4}
\]

and anti-join the four opposite incidences

\[
 (S\cup\{a_i,a_{i+1}\},
  S\cup\{a_{i-1},a_i,a_{i+1}\}).                            \tag{4.5}
\]

### Theorem 4.1 (octahedral bijection and bound)

The closed tuples (4.3)--(4.5), modulo cyclic rotation but not reversal,
are in bijection with the active oriented octahedral `C8` keys.  The prefix
join has at most `5,445,440` rows and the canonical active output has at
most `1,361,360` rows.

#### Proof

For an octahedral word put

\[
 C_i=S\cup\{a_i,a_{i+1}\},\qquad
 T_i=S\cup\{a_i,a_{i+1},a_{i+2}\}.
\]

Then (4.3)--(4.4) are exactly the four selected removed incidences and
(4.5) is exactly the unselected added matching.  This proves the bijection.

For each of `binom(17,6)` cores there are `11*10` ordered first pairs and,
by (4.2), at most `2^2` choices in (4.3).  Thus the prefix count is

\[
 {17\choose6}\,11\,10\,2^2=5,445,440.                        \tag{4.6}
\]

Every active directed word occurs under its four rooted rotations, so the
canonical output is at most

\[
                    5,445,440/4=1,361,360.                   \tag{4.7}
\]

As in the star case, reversal is the opposite phase. \(\square\)

Theorems 3.1 and 4.1 prove (1.1).  They use only the degree-two selected
incidence ledger, not a probabilistic sparsity assumption.

## 5. Exact no-duplicate key

For either family, rotate the directed petal word to its lexicographically
least cyclic rotation.  Do not compare it with its reversal.  The canonical
key is

```text
C8:<family>:<core>:<directed-rotmin-word>:<removed-incidence-ids>:<added-incidence-ids>
```

with the four removed and four added immutable ids listed in directed slot
order.  The full lower and owner masks are repeated in the record.

### Lemma 5.1 (physical uniqueness)

Each active physical simple `C8` has exactly one such key, and the key
recovers its family, support, active phase, and all eight status changes.

#### Proof

The intersection of the four lower rows is the unique core: it has rank
seven in the star family and rank six in the octahedral family.  Removing
the core recovers the petal singleton or consecutive-pair system.  The
removed matching orients that cyclic system.  A directed cycle has one
least rotation, while its reversal is the other phase.  Immutable incidence
ids then recover the literal status toggle. \(\square\)

## 6. The exact active aligned-`3+1` join

For an active key `Q`, let

\[
             \delta_i=(C_i,T_i^-,T_i^+)                     \tag{6.1}
\]

be its four changed slots.  Let `R_i` be the other selected owner at the
lower row `C_i`.  A slot whose lower row is cut from the declared component
factor supplies no old adjacency and cannot be one of the four advertised
`3+1` turns.

Use immutable component occurrence keys.  For every genuine old turn,
record its old component key and its directed position in that component.
The component filter is:

1. all four old turns exist literally;
2. their component-key multiplicities are `3+1`; and
3. on the repeated component, the three slot positions occur in the
   directed cyclic order prescribed by the active phase.

Equivalently, on a cycle-cover representation, if `s` is the old
first-return permutation on the four cut slots and

\[
                         h=(0\ 1\ 2\ 3),                     \tag{6.2}
\]

then, after rotating slot names,

\[
                  s=(0\ 1\ 2)(3),\qquad c(sh)=1.             \tag{6.3}
\]

The opposite order gives three new components and is rejected from the
aligned face.  Numeric component ids are not part of this test.

Let a forced-role fingerprint contain its owner mask, occurrence side,
orientation, ordered owner trace, endpoint labels, and every named q1
resource used by the role.  Rebuild the affected components after the
atomic toggle.  The role-relocation predicate is

\[
 \operatorname{RoleKey}_{B_Q}(r)
       \ne \operatorname{RoleKey}_{B_0}(r)                   \tag{6.4}
\]

for at least one declared forced role `r`, with disappearance or
internalization represented by an explicit terminal symbol.  Touching the
old component or changing its dense number does not satisfy (6.4).

### Theorem 6.1 (complete active `3+1`/role sieve)

Semijoining the active keys of Sections 3--4 with (6.3) and (6.4) emits
every atomic active aligned role-relocating simple `C8`, exactly once.

#### Proof

The two transition joins enumerate every active simple `C8` by the complete
classification.  Conditions (6.3) and (6.4) are the literal definitions of
the declared component and role subface on immutable occurrences.  They
only reject keys outside that subface.  Lemma 5.1 prevents duplicates.
\(\square\)

## 7. Base locality and exact palette rows

Let `Omega(Q)` be the union of the old occurrence components incident with
the four triples `(R_i,T_i^-,T_i^+)`, closed under the four changed lower
rows.  Rebuild those components jointly and let `widehat Omega(Q)` also
contain every old/new upper-union resource, orientation complement, guard,
and blocker changed by the rebuild.

### Lemma 7.1 (atomic locality)

Every occurrence and factor incidence outside `widehat Omega(Q)` is
identical before and after `Q`.  Every changed q1 atom has a tail or head in
the rebuilt occurrence support, or uses one of the explicitly listed
old/new resources in `widehat Omega(Q)`.

#### Proof

Only the four lower-row endpoint assignments (6.1) change.  Removing those
assignments separates the factor into unchanged components.  Reconnecting
them can alter only components incident with their old or new endpoints.
The q1 atlas is occurrence-labelled; an atom with both endpoint occurrences
and all resources outside that closure has the same geometry, orientation,
capacity, and guards in both banks. \(\square\)

The selected cut/lower-colour **membership bank** is fixed by a
successor-incidence `C8`.  Consequently its selection indicator and
multiplicity vector are invariant.  There is no creator--supplier selection
join analogous to an independent recut packet.

This does **not** make the q1 `zero_lower` coordinate invariant.
`zero_lower` counts selected-colour provider atoms, and endpoint geometry
can delete the last provider of a fixed selected colour.  Its exact delta is
obtained by removing and rebuilding every q1 atom incident with
`Omega(Q)`.  A selected colour whose complete atom row avoids that support
is unchanged by Lemma 7.1.

The rank-ten/upper resource change is nevertheless not automatically zero.
For each noncut changed lower row,

\[
 m_Q^{\rm factor}(U)=m_0^{\rm factor}(U)+\sum_{i=0}^3
 \left({\bf1}_{R_i\cup T_i^+=U}
      -{\bf1}_{R_i\cup T_i^-=U}\right).                    \tag{7.1}
\]

Formula (7.1) is the direct internal-factor contribution and is supported on
at most eight named union values.  The complete `zero_rank10` row also
contains the upper values of rebuilt q1 atoms.  Precisely,

\[
 m_Q^{\rm upper}(U)=m_0^{\rm upper}(U)
       +\Delta_Q^{\rm factor}(U)+\Delta_Q^{\rm atom}(U),     \tag{7.2}
\]

where (7.1) is `Delta_factor` and `Delta_atom` is the exact
occurrence-labelled atom difference on `Omega(Q)`.  The lower-provider,
tail, head, orientation, and complete rank-ten zero rows are all recomputed
from these local atom deltas; every outside contribution is copied
literally.  No scalar degree or owner mask replaces this replay.

If exact **direct-factor** immediate-upper multiplicity, rather than mere
zero coverage, is part of a later declared interface, its proof-safe filter
is equality of the two four-element multisets in (7.1).  The known
common-exterior and antipodal classifications may then be used.  They may
not replace the atom term in (7.2), and they may not be imposed when the
frozen row requires only nonzero coverage.

## 8. Multiple unconditional-core cones

For an unconditional q1 certificate `K`, let `D(K)` be its complete
occurrence-labelled dependency cone.  It contains demanded roles and rows,
all effective providers and full footprints, capacities, orientation and
complement data, guards, blockers, and every permitted transported trace.

Define `Hit_K(Q)` by direct comparison on `widehat Omega(Q)`:

\[
 \operatorname{Hit}_K(Q)
 \quad\Longleftrightarrow\quad
 \text{the atomic before/after replay changes a datum of }D(K). \tag{8.1}
\]

For a genuinely joint endpoint--endpoint or endpoint--colour event, the
record contains the circuit key, all participating slots, the final atom,
and its complete footprint.  It is not replaced by the union of four
singleton deltas.

### Theorem 8.1 (core-cone intersection)

If `Q` escapes every unconditional stored trace, then

\[
                    \forall K\in\mathcal L_0,
                    \quad \operatorname{Hit}_K(Q).           \tag{8.2}
\]

Hence the proof-safe pre-q1 catalogue is the exact semijoin

\[
 \mathcal J_{31}=
 \mathcal J_{\rm active}
 \ltimes \texttt{ALIGNED31}
 \ltimes \texttt{ROLE_RELOCATED}
 \ltimes\bigcap_{K\in\mathcal L_0}\texttt{HIT}_K.           \tag{8.3}
\]

#### Proof

If (8.1) fails, Lemma 7.1 leaves every load-bearing occurrence, provider,
resource, capacity, guard, blocker, and transported embedding of `K`
unchanged.  Its authenticated contradiction therefore persists.  Taking
the contrapositive for each `K` proves (8.2). \(\square\)

This is a necessary prefilter.  A changed datum need not destroy every
transport of the core, so the complete unconditional semantic scan remains
mandatory after (8.3).

For a materialized enlarged unary reverse-cone table `A_K` of selected
transition roots, every active completion containing a fixed root has at
most four directed completions in either family.  Therefore

\[
        |\{Q:\operatorname{Hit}_K(Q)\}|\le4|A_K|,            \tag{8.4}
\]

provided `A_K` includes every root having at least one joint completion
which can change `D(K)`.  Formula (8.4) is a useful anchor bound; shrinking
`A_K` to singleton deltas is not proof-safe.

For the original dual fan, the selected lower palette is fixed.  Thus a
breaker must change a forced-role fingerprint or the endpoint geometry,
orientation, or resource table in the authenticated 16-piece socket cone.
The frozen star prefilter count `500` is a valid instance of (8.2).  No
corresponding octahedral artifact currently exists, which is why (1.3) uses
the complete octahedral upper bound.

## 9. Exact launch order and preference criterion

Put

\[
 R_3=2,909,465,711,
 \quad J_8=7,001,280,
 \quad M_8=1,415,823                              \tag{9.1}
\]

where `M8` uses the frozen exact star count and the theorem-only
octahedral upper bound.  Then

\[
 {R_3\over J_8}>415.56,
 \qquad
 {R_3\over M_8}>2054.96.                                 \tag{9.2}
\]

Thus the active-C8 face is preferable at the generator level.  More
generally, let `c8` be a uniform upper bound on complete per-packet local,
core, and footprint work, and let `c3` be a lower bound on the corresponding
radius-three work.  The count-certified sufficient condition is

\[
                         {c_8\over c_3}
               < {R_3\over M_8}.                            \tag{9.3}
\]

If generation-prefix cost dominates, replace `M8` by `J8`, giving the first
ratio in (9.2).  If footprint counts vary, the exact comparison is

\[
 \sum_{Q\in\mathcal J_{31}}
   \left(c_{\rm local}(Q)+
     \sum_{P\in\Sigma_{B_Q}(U_0)}c_{\rm succ}(Q,P)\right)
 <
 \sum_{S\in\mathcal J_3}
   \left(c_{\rm local}(S)+
     \sum_{P\in\Sigma_{B_S}(U_0)}c_{\rm succ}(S,P)\right).  \tag{9.4}
\]

The join counts alone do not bound footprint multiplication, so (9.4) must
be audited if the two implementations have radically different footprint
families.  An atomic `C8` needs one before/after replay, whereas radius three
needs all eight subset banks for its causal certificate; no cost advantage
from that fact is assumed in (9.2).

The complete protected star face already has a scoped negative theorem.  On
the frozen instance the genuinely unenumerated correlated work is therefore
the octahedral join of Section 4, with at most `5,445,440` prefix rows and
`1,361,360` canonical active packets before the `3+1`, role, cone, and
zero-265 filters.  For a proof-complete two-family manifest, D should still
import and independently replay the star rejection rather than silently
omit that family.

### Proposition 9.1 (smallest genuinely new simple circuit face)

Within protected simple incidence circuits on the frozen factor, the next
genuinely unenumerated correlated face is the active octahedral `C8` join.

#### Proof

The rank-eight/rank-nine Boolean incidence graph has no simple `C4`, since
two distinct rank-eight vertices have at most one common rank-nine
neighbour.  The complete protected `C6` catalogue and the complete protected
star-`C8` catalogue already have scoped negative round-02 theorems.  The
simple-`C8` classification leaves exactly the octahedral family.  Moreover,
when the desired component action is a two-to-one aligned fusion, the
cut-permutation parity formula forbids the two-component use of a `C6`,
whereas an aligned `3+1` `C8` realizes it.  Section 4 is therefore the
smallest missing simple correlated generator, without making any claim
about circuit-plus-recut or nonsimple moves. \(\square\)

## 10. Launch-ready survivor specification

D should freeze the following occurrence-labelled artifacts.

1. `selected_factor.tsv`: immutable lower/owner incidence ids, selected
   status, protected status, and the exact degree-two audit.
2. `star_transitions.tsv` and `oct_transitions.tsv`: the relations (3.1)
   and (4.1), with source incidence ids.
3. `active_prefix.audit.json`: exact prefix counts, closure failures,
   opposite-incidence anti-join failures, rotation duplicates, and the
   bounds (1.1).
4. `active_c8.tsv`: canonical key, family, core, directed word, all eight
   incidence ids, and the other selected owner `R_i` at every lower row.
5. `component31.tsv`: four immutable old component keys and positions, the
   repeated component, directed order, return permutation, and the verdict
   for (6.3).
6. `role_relocation.tsv`: old and final forced-role fingerprints and the
   literal reason for relocation, disappearance, or internalization.
7. `locality.tsv`: `Omega(Q)`, every rebuilt occurrence, and every resource
   in `widehat Omega(Q)`.
8. `palette_delta.tsv`: proof that the selected lower membership bank is
   unchanged, the q1 lower-provider atom delta, the eight-term direct upper
   delta (7.1), the rebuilt-atom upper delta in (7.2), and all five unsummed
   zero-265 values.
9. `core_hits.tsv`: one row per `(packet,core,datum,event)`, including every
   joint slot set and full footprint; absence of a complete row is
   `UNKNOWN`, not a rejection.
10. `core_scan.tsv`, `footprints.tsv`, and `survivors.tsv`: the same complete
    unconditional and successor-library semantics as the frozen radius-three
    launch specification.  A survivor is
    `LIBRARY_OPEN_NOT_Q1_VERDICT` only.
11. `independent.audit.json` and `SHA256SUMS`: independent regeneration of
    both families, strict key-order comparison, no duplicates, all component
    and role fingerprints, local rows, and library decisions.

### Theorem 10.1 (finite survivor completeness)

Assume the frozen factor/protection table, component occurrence map, forced
roles, zero-265 ledger, and core manifests are complete and independently
replayed.  Generate Sections 3--4, apply (8.3), rebuild each retained bank
atomically, and then apply the exact zero-265, unconditional-core, and
footprint-successor tests.  Every active aligned role-relocating simple `C8`
which is joint-zero-265 and open relative to the declared q1 library occurs
exactly once in `survivors.tsv`.

#### Proof

Theorems 3.1 and 4.1 enumerate the complete active simple-`C8` class.
Lemma 5.1 gives unique physical keys.  Theorem 6.1 selects exactly the
declared `3+1` role-relocation subface.  Theorem 8.1 omits no packet that can
escape every unconditional core.  Lemma 7.1 makes the local and q1 rebuild
complete, and the final footprint condition is the literal finite
successor-cover complement. \(\square\)

## 11. Frozen evidence and boundary

The light ledger checks used here are:

* factor SHA-256
  `7c022f4050d6358bc5047532113814fdb46412db0018a0254cc82e056720d8df`;
* round-02 bank SHA-256
  `48670b1bf5388ed4c8f47a408e4659c145ec26dc3d6a6bb31cd379a1e70ad649`;
* star census source SHA-256
  `1f0e3a9aa9e4389aa4ad689bd67c78b0c10e96066511000773abf0f5b9fd3e5a`;
* star census audit SHA-256
  `3645537503ccd4319dcf95a9887dc5d27896de0819525595945fae243b3f79dc`;
* exact factor degree audit: `48,620` rows, `24,310` lower rows, no
  lower row of degree other than two; and
* exact star census rows: `54,463` active protected keys and `500` meeting
  the original dependency cone.

No octahedral active count, aligned-`3+1` count, or owner-stable role count
is asserted from the old census.  Bounds (1.1)--(1.3) are theorems, not
estimates.  Passing the final library scan is not q1 feasibility.  Circuit
plus recut moves, two circuits, nonsimple `C8`s, and longer alternating
circuits remain outside this face.
