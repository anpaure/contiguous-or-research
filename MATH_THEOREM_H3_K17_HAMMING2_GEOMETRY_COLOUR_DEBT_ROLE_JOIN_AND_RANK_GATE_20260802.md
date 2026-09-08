# H3: the complete round02 Hamming-two join is geometry times colour, followed by debt, role rank, and global q1 rank

Date: 2026-08-02  
Status: exact theorem for the frozen `k=17` round02 one-for-one recut face.
The frozen Thread-D projection supplies 67 noncentral geometry movers and
154 directed relaxed-resident raw socket-seam occurrences whose lower colours are
not selected in their singleton children.  Those finite counts are inputs,
not recomputed here.  Thread D's adopted inverse join has no compatible
nonanchor creator--supplier pair, proving 21-anchor completeness on this
face.  Its complete generator has 349,642 banks, of which 169,426 pass the
joint zero-265 ledger.  The later exact-q1 audit closes all 49
joint-zero-265-clean
banks containing one of the seven locally dirty central anchors.  No
enumeration or solver is rerun in this note.

## 1. Exact face and the occurrence ledger

Let `C` be the frozen round02 cut bank and let `U` be its 16,667 valid
one-for-one extra-cut recuts.  A move \(i\in U\) changes one base piece `B_i`,
removes the selected lower colour `o_i`, and inserts the lower colour `n_i`.
Two moves are compatible when they change distinct bases.  Write

\[
                    C_{ij}=C\oplus i\oplus j.             \tag{1.1}
\]

The theorem uses the 154 raw seam **occurrences**, not merely their colours.
For a noncentral mover `i`, an occurrence record is

\[
 \omega=(i;y,\rho;B,\sigma,\epsilon,\eta,w;\ell,u).       \tag{1.2}
\]

Here

* `y` is one of the two central owner occurrences `s,t`;
* `rho in {O,I}` is the directed central socket role;
* `(B,sigma,epsilon,eta,w)` identifies the leaf base, child side,
  orientation, physical socket side, and owner occurrence;
* `ell=y cap w` and `u=y cup w` are the lower and upper masks; and
* the directed seam is Johnson-legal and passes the frozen relaxed two-block
  residence predicate in `C_i`, is absent from the baseline raw atlas, and
  has `ell` unselected in `C_i`.

In particular \(\ell\ne114930\); the core colour `114930` is already selected
and cannot be the missing colour in a cross activation.

Mutable rebuilt piece numbers are not occurrence labels.  On this face the
in-memory key used by
`scratch/audit_threadA_k17_round02_dualfan_hamming2_projection_20260802.cpp`
contains the required central socket, direction, leaf base, child side,
orientation, leaf owner, lower mask and upper mask.  Its scalar TSV output,
however, exports per-move counts and deduplicated colour lists rather than
the 154 rows (1.2).  Therefore a proof-grade instantiation of the join below
requires either

1. a hashed 154-row export retaining the complete key (1.2), or
2. a literal final rebuild of every retained pair.

The accepted `67/154` cardinality alone is not an occurrence-level join
certificate.  Thread D's frozen theorem additionally authenticates its
inverse join and literal final-net rebuild, so its finite 21-anchor
corollary is accepted here.  For reuse outside that frozen run, the scalar
TSV alone is insufficient: retain a hashed occurrence ledger or repeat the
literal rebuild.  The older anchor-completeness projection, which identifies
a raw row only by socket, direction, lower colour and other owner, is at most
an overinclusive pair generator when separated from that final replay.

## 2. Roles and central states are different objects

Define the immutable identity of a forced role by

\[
 \operatorname{rolekey}=(\text{factor owner occurrence},
                         \text{boundary gap/side}),       \tag{2.1}
\]

and record its inward ordered path and age vector as a separate state.
Equality of an entire path is too strong for role identity.

The frozen one-for-one face has three branches.

1. **Noncentral fixed state.**  If both recuts are outside bases 1834 and
   1835, the role keys, central endpoint states and ages at `s,t` are fixed.
   The direct `s--t` seam remains residence-illegal and its colour 114930
   remains selected.
2. **Central-state, same role.**  A base-1834 recut can change the path and
   ages behind `s` while retaining the same terminal owner occurrence and
   forced boundary role.  These moves require a literal rebuilt raw atlas;
   they are not role relocations and are not certified by the 154
   noncentral records.
3. **True role relocation.**  The owner-stable audit identifies
   `1835:9933->9932` as the sole one-recut change of the old central role key.
   The old dual fan then loses a premise, but this is only promotion: the new
   forced role system must be rebuilt and saturated.  Under the corrected
   Lane-L local ledger this singleton has tail, head and common-orientation
   zero rows, although its emitted q1 formula is UNSAT.

If both central bases are changed, true role relocation takes precedence in
the classification.  Two noncentral recuts cannot relocate either central
role.  Nor can they create the direct `s--t` seam, because both endpoint
states, its selected colour, and its failed residence predicate stay fixed.

## 3. Exact geometry--colour join

Let `Omega_i` be the occurrence records (1.2) of mover `i`, and let

\[
                  \Omega=\mathop{\dot\bigcup}_i\Omega_i,
                  \qquad |\Omega|=154.                   \tag{3.1}
\]

For `omega in Omega_i`, define its supplier set by

\[
 \Sigma(\omega)=
 \left\{j\in U:
 \begin{array}{l}
  B_j\ne B_i,\quad i,j\text{ compatible and noncentral},\\
  n_j=\ell(\omega),\\
  \text{the final selected-cut multiplicity of }\ell(\omega)
       \text{ in }C_{ij}\text{ is exactly one}
 \end{array}
 \right\}.                                                \tag{3.2}
\]

The last condition prevents a colour collision.  State survival is
automatic in the strict noncentral distinct-base branch; in any enlarged
move class it must be tested explicitly.

The occurrence-labelled latent join is

\[
 {\cal J}_{\rm lat}=
 \{(i,j,\omega):\omega\in\Omega_i, j\in\Sigma(\omega)\}. \tag{3.3}
\]

### Theorem 3.1 (sound and complete joint-only activation)

Every triple `(i,j,omega)` in (3.3) activates that directed selected-colour
occurrence in the final relaxed socket atlas of `C_ij`.

Conversely, let `i,j` be compatible noncentral recuts and let `e` be a
noncore seam occurrence at `s` or `t` which is present in `C_ij` but absent
from `C,C_i,C_j`.  Then exactly one ordering of the pair has

\[
                    e=\omega\in\Omega_i,\qquad
                    j\in\Sigma(\omega).                  \tag{3.4}
\]

Thus (3.3) is complete for joint-only atom activation on the frozen
noncentral Hamming-two face.

#### Proof

For a central--leaf seam, a noncentral recut changes raw geometry only when
it changes the base containing the leaf occurrence.  Hence for
`omega in Omega_i` and a compatible noncentral supplier `j`,

\[
        R_{C_{ij}}(\omega)=R_{C_i}(\omega)=1.             \tag{3.5}
\]

The seam colour is absent after `i`, while (3.2) inserts it exactly once in
the joint palette.  Raw persistence and the selected-colour guard therefore
activate the same directed occurrence in `C_ij`.  This proves soundness.

Conversely, the leaf of a joint-only seam lies in at most one changed base;
call its recut `i`.  Its raw predicate already holds in `C_i`.  Since the
seam is absent from `C_i`, its colour is not selected there.  A one-for-one
second recut changes the selected palette only by its new colour, so

\[
 K(C_{ij})\setminus K(C_i)\subseteq\{n_j\}.               \tag{3.6}
\]

Final activation forces \(n_j=\ell(e)\) and multiplicity one.  The other
ordering cannot move the same leaf occurrence because the bases are
distinct.  Hence (3.4) is unique.  \(\square\)

Pair deduplication may occur only after retaining the complete witness list
`{omega}`.  Distinct directed occurrences can have the same mover, owner
mask and lower colour.

### Corollary 3.2 (frozen 21-anchor completeness)

Let `A` be the twelve selected-colour singleton escapes together with all
nine central recuts.  The adopted D join proves that every one of the 154
new raw unselected occurrences either has no compatible supplier or can be
activated only in a pair already meeting `A`; there is no compatible
nonanchor creator--supplier pair.  It also finds no dirty noncentral
selected-colour singleton escape.  Therefore every Hamming-two child which
destroys the original dual fan contains an anchor in `A`.

This is the finite theorem which discharges the two abstract loopholes in
the earlier conditional 21-anchor statement.  It is exact only for this
frozen face and says nothing yet about q1 feasibility.

## 4. One activated arm is not yet a breaker

For a final bank `D`, rebuild every active seam occurrence and its complete
resource footprint: the two physical socket occurrences, lower colour,
orientation/capacity resources, protected resources and directed role.
Let `F(D)` be the exact forced socket-role demands obtained from the final
orientation clauses, keyed by (2.1), and define

\[
 \rho(D)=\max\{|\operatorname{sat}_{F(D)}(Q)|:
              Q\text{ is a resource-disjoint active seam family}\}.       \tag{4.1}
\]

Here `sat_F(Q)` is the set of forced demands covered by `Q`; a direct seam
may therefore saturate two forced demands.  Put

\[
                         d_{\rm role}(D)=|F(D)|-\rho(D).   \tag{4.2}
\]

When the old two roles persist, `d_role(D)=0` exactly when either a legal
direct `s--t` seam exists or there are arms `su,tv` with distinct outside
physical socket occurrences, distinct lower colours and disjoint residual
resources.  For a role relocation, (4.1) is applied to the newly rebuilt
role set.  A relocation flag alone is not a local completion.

### Lemma 4.1 (exact forced-role separator)

The final forced-role subsystem is feasible if and only if

\[
                            d_{\rm role}(D)=0.             \tag{4.3}
\]

For the persistent two-role branch this is the direct-or-two-arm criterion
above.

#### Proof

Every local feasible selection restricts to a resource-disjoint seam family
whose saturated-demand set in (4.1) is `F(D)`.  Conversely a maximizing
family saturating `|F(D)|` demands is a literal local selection satisfying
all forced roles.  With two roles, a saturating family has either one seam
covering both or two compatible arms, giving the displayed specialization.
\(\square\)

## 5. Occurrence-labelled debt cancellation

Use a common final-net universe of occurrence/activity rows.  It contains
all lower-colour, physical tail, physical head, coherent-orientation,
rank-ten support, new-fragment and newly active colour demands.  For a row
`r` and bank `D`, let `a_r(D)` be its activity, `z_r(D)` its number of legal
occurrence-labelled providers, and

\[
                         w_r(D)=z_r(D)-a_r(D).             \tag{5.1}
\]

For a pair `i,j`, define

\[
\begin{aligned}
 \Delta_r(i)&=w_r(C_i)-w_r(C),\\
 \Delta_r(j)&=w_r(C_j)-w_r(C),\\
 \Delta_r^{\rm int}(i,j)
   &=w_r(C_{ij})-w_r(C_i)-w_r(C_j)+w_r(C).
\end{aligned}                                             \tag{5.2}
\]

Then

\[
 w_r(C_{ij})=w_r(C)+\Delta_r(i)+\Delta_r(j)
                     +\Delta_r^{\rm int}(i,j).            \tag{5.3}
\]

The interaction term contains cross-created seams, destruction of a unary
witness whose old neighbour is recut, colour-activity changes and new
fragment demands.  It cannot be replaced by complementary singleton debt
vectors.

Define the exact local debt

\[
 L(i,j)=\sum_{r:\,a_r(C_{ij})>0}\bigl(-w_r(C_{ij})\bigr)_+. \tag{5.4}
\]

Thus `L(i,j)=0` if and only if every scoped final active support row passes.
Two individually clean children need not have `L=0`, and two individually
dirty children can have `L=0`.

## 6. Complete scoped Hamming-two criterion

For a compatible pair `p={i,j}`, construct its final bank once and assign it
to exactly one branch, in this order:

1. true role relocation;
2. central-state change with the same role key;
3. noncentral fixed state.

In branch 3, its active central arms are exactly the union of

* baseline arms which survive both recuts;
* unary arms present in one singleton and surviving the other; and
* the joint-only occurrences supplied by Theorem 3.1.

Branches 1 and 2 use a literal central rebuild rather than the 154-row
projection.

Let `b_prot(p)` be zero exactly when every literal protected socket, owner,
colour and contracted protected seam survives.  Collars, tickets, topology
and compiler objects which are not literal seam resources remain separate
guards and are not silently contracted.

### Theorem 6.1 (soundness and completeness of the local join)

A compatible pair is a locally admissible Hamming-two promotion of the
frozen q1 core if and only if

\[
                 b_{\rm prot}(p)=0,\qquad L(i,j)=0,\qquad
                 d_{\rm role}(C_{ij})=0.                 \tag{6.1}
\]

Every complete q1 solution on the frozen Hamming-two face satisfies (6.1)
and is generated by the three-branch construction above.  Conversely (6.1)
gives a literal final local selection satisfying all scoped support and
forced-role rows.  It is a promotion, not yet a global q1 solution.

#### Proof

Necessity of protection and (5.4) is immediate from any full solution.
Restricting that solution to its final forced roles proves
`d_role=0` by Lemma 4.1.  In the noncentral branch, every final central arm
is baseline, survives from a singleton, or is absent from both singletons;
Theorem 3.1 gives the last class exactly.  The central branches are complete
because their final incidence and role systems are rebuilt literally.

Conversely, (6.1) supplies every declared local support row and a
resource-disjoint family saturating all final forced roles while retaining
the literal protected bank.  That is precisely local promotion.  Global
tail/head/colour correlation outside this subsystem can still fail, so no
q1 conclusion is inferred.  \(\square\)

## 7. Efficient join and exact rank potential

Bucket all supplier recuts by their inserted colour `n_j`.  For each of the
154 occurrence records probe only the bucket of \(\ell(\omega)\).  If

\[
 J_{\rm col}=\sum_{\omega\in\Omega}|\{j:n_j=\ell(\omega)\}|,               \tag{7.1}
\]

then raw candidate generation costs

\[
                         O(|U|+154+J_{\rm col})            \tag{7.2}
\]

expected time with hashing, plus output storage.  This replaces the dense
`67|U|` product.  Pair deduplication stores all occurrence witnesses.

For a pair `p`, only rows in the union dependency cone of its two recuts,
its activated seams, and its new demands can change from the clean baseline.
If this cone has `b_p` occurrence rows, a complete sparse or bitset replay of
(5.4) costs `O(b_p)`.  The two-role rank test is the nonemptiness test in its
explicit compatibility graph; generating that graph costs at most
`O(|A_s(p)||A_t(p)|)` and is linear in its emitted edge list.  Central and
relocated branches use the same computation after their literal rebuild.

Let `Theta(p)` be the coherent integral orientation masters of the final
bank.  For `theta in Theta(p)`, let `H_p^theta` be the resulting physical
socket/colour seam hypergraph, let `N_p` be the required q1 size, and let `P`
be only a literal fixed protected seam submatching.  Define

\[
 \nu_P^{q1}(p)=\max_{\theta\in\Theta(p)}\nu_P(H_p^\theta),
 \qquad
 \delta_P(p)=N_p-\nu_P^{q1}(p).                          \tag{7.3}
\]

The exact joined-pair potential is

\[
 \Phi(p)=\bigl(b_{\rm prot}(p),L(i,j),d_{\rm role}(C_{ij}),
               \delta_P(p)\bigr)                         \tag{7.4}
\]

in lexicographic order.  Within the scoped q1 layer,

\[
                         \Phi(p)=(0,0,0,0)                \tag{7.5}
\]

if and only if `p` is a protected exact-q1 completion.  Downstream residence
outside the local seam predicate, upper tickets, topology, deeper decks,
exterior windows and the terminal compiler are not coordinates of (7.4).

For a fixed master `theta` and any matching `M_p` in `H_p^theta` containing
`P`, the rank coordinate has the exact alternating-surplus form

\[
 \nu_P(H_p^\theta)=|M_p|+
 \max_X\bigl(|X|-|D_{M_p}(X)|\bigr),                     \tag{7.6}
\]

where `X` is a resource-disjoint entering seam family avoiding `P` and
`D_{M_p}(X)` is its complete incumbent blocker set.  The global coordinate
in (7.3) maximizes this value over coherent integral masters.  For a fixed
master, a bounded alternating closure of size `t` gives a fixed-parameter
rank evaluation in `2^{O(t)} poly(t)`.  Without bounded closure and a bounded
master family, the three-resource/orientation layer retains general
three-dimensional-matching difficulty; (7.6) is not a generic polynomial
algorithm or a matroid claim.

For radius `r`, let

\[
 \Theta_r=\min_{\substack{Q\subseteq U\text{ compatible}\\|Q|\le r}}
             ^{\rm lex}\Phi(Q),                          \tag{7.7}
\]

with the analogous final-net definitions for `Q`.  The radius families are
nested, so `Theta_r` is nonincreasing and first reaches zero at the least
successful Hamming radius.  This is an exact offline decision potential.
It does **not** imply that a sequence of one-for-one recuts decreases
monotonically.

## 8. Finite collapse and semantic core persistence

### 8.1 Dirty-single compensation is closed

Corollary 3.2 reduces every old-fan breaker to the 21-anchor product.  The
adopted final-net census has

\[
 349642\text{ compatible banks},\qquad
 169426\text{ joint-zero-265-clean banks}.                \tag{8.1}
\]

The role-changing anchor `1835:9933->9932` has no jointly clean partner.
Each of the seven individually dirty base-1834 anchors has the same seven
compensating partners, giving 49 distinct joint-zero-265-clean banks.  The new
exact-q1 audit canonically rebuilds all 49 bank/CNF/map triples, proves all
49 UNSAT, and independently verifies all 49 DRAT proofs.  Hence dirty-single
compensation is closed on this fixed Hamming-two face.

Removing those 49 banks leaves

\[
                         169426-49=169377                 \tag{8.2}
\]

joint-zero-265-clean candidates.  Every one contains at least one of the thirteen
individually clean anchors: the twelve visible socket escapes or the clean
central-state move `1834:9924->9923`.  Hamming two is therefore still the
minimal live radius; no Hamming-three conclusion follows yet.

### 8.2 Semantic core-persistence filter

For a clean anchor `a`, let `L_a` be its independently authenticated library
of occurrence-labelled q1 cores.  A core records its literal variables and
complements, complete effective provider sets of positive rows, resource
capacity/conflict clauses, and named blockers proving omitted atoms dead.
For a final pair `p={a,h}`, let `Tr_K(p)` be the trace of those data under the
canonical occurrence map.

### Theorem 8.1 (proof-safe semantic persistence)

If a core `K in L_a` has a complement-preserving occurrence injection into
the final q1 formula which preserves every literal clause, or if the final
formula entails the same guarded core minor after resolving named dead-atom
blockers, then the pair `p` is q1-UNSAT.

The test has no false rejection.  Failure to recognize an embedding merely
promotes the bank to full q1 rebuilding.

#### Proof

The image of a literal core is an isomorphic unsatisfiable subformula of the
final formula.  For a guarded minor, resolve every enlarged positive row
against its retained named blockers; the resulting clauses reproduce the
stored unsatisfiable core.  In either case the final formula entails an
unsatisfiable clause set.  \(\square\)

For efficient separation, define for a stored core `K`:

* `Occ_K`: recuts changing a recorded occurrence, orientation or role;
* `Clause_K`: recuts changing an old atom, resource clause, unit or named
  blocker;
* `Geom_K(c)`: unfiltered recuts creating raw geometry of colour `c` in a
  positive core row;
* `Pal(c)`: recuts changing selected multiplicity of `c`; and
* `End_K`: pairs whose two new endpoint states jointly create a core-row
  atom.

Put

\[
\begin{aligned}
 \mathfrak D_K={}&\bigl\{\{g,h\}:g\text{ or }h\in
                    \operatorname{Occ}_K\cup\operatorname{Clause}_K\bigr\}\\
 &\cup\bigcup_c\bigl(\operatorname{Geom}_K(c)
                 \bowtie\operatorname{Pal}(c)\bigr)
   \cup\operatorname{End}_K,                             \tag{8.3}
\end{aligned}
\]

where `bowtie` retains compatible distinct-base pairs with correct final
colour multiplicity.  Every pair outside `D_K` leaves the guarded core minor
unchanged.  Thus the banks needing a full q1 rebuild lie in

\[
 {\cal R}=\left\{p:
 p\in\bigcap_{a\in p\cap A_{\rm clean}}
          \ \bigcap_{K\in L_a}\mathfrak D_K\right\}.      \tag{8.4}
\]

Equation (8.4) is complete relative to the stored library, not for all q1
infeasibility.  It includes both geometry--palette cross atoms and genuine
two-endpoint atoms, and it compares effective provider identities rather
than degrees.  The sets in (8.3) can be stored as bitsets over the 169,377
remaining banks; intersecting them is linear in the bitset volume.  A bank
outside (8.4) is rejected with the surviving authenticated certificate.

### Corollary 8.2 (frozen 13-profile reduction)

The adopted semantic filter on the original 169,426 banks returns

\[
  164323\text{ persistence-certified UNSAT},\qquad
  5103\text{ `EXACT_BUILD'}.                             \tag{8.5}
\]

The 49 dirty-central banks are exactly 49 rows of the second class.  After
their checked refutations, the current proof partition is therefore

\[
  169426=164323+49+5054.                                 \tag{8.6}
\]

Thus 164,372 banks are proved q1-negative and 5,054 clean-anchor banks need
a fresh q1 build under the chosen core library.  `EXACT_BUILD` means only
that this filter did not retain its selected core profile; it is not a SAT
or feasibility label.  Additional authenticated cores may reduce 5,054.

#### Proof

The semantic filter compares occurrence identities, complete effective
provider rows and resource incidences for one authenticated profile of each
clean anchor.  Theorem 8.1 makes every `PERSISTENT_UNSAT` verdict sound.
The frozen census gives (8.5), and the 49-bank proof plus subtraction gives
(8.6).  \(\square\)

### Corollary 8.2A (combined-core and exact-delta rebase)

The later combined authenticated core filters give the sharper partition

\[
  169426=165713+49+3664.                                 \tag{8.6a}
\]

The 3,664 clean-anchor exact-build rows have 3,664 distinct complete binary
anchor-relative q1 delta keys, with largest equality class one.  This rules
out reuse by literal exact-delta equality.  It does not prove 3,664 distinct
common-exterior boundary languages: the keys include the anchor id,
serialized native state records and every interior added/removed atom.

After transport to immutable round02 occurrences, let \(W\) contain the
union of all changed objects and let \(\Gamma(W)\) record every crossing
tail/head/colour capacity, orientation and protected q1 state.  Exact gluing
through proposed signatures holds precisely when the crossing conjunction
is constant on signature fibres and accepts exactly complementary pairs.
Recording a typed incidence separator \(\Gamma(W)\) is a proof-safe
sufficient condition; it need not be necessary when crossing constraints are
forced or redundant.  A nonvacuous bounded cylinder theorem additionally
needs bounded absorbed support and interior master dimension, or a uniformly
bounded family of cylinder--shore templates.  A bounded list of shore names
alone is insufficient.  Lane A's functional-Hall theorem gives a finite
bank-specific cover but no bound on these quantities.

For a fixed exterior language \(E_P\) and case response \(R_\delta\), the
existential host asks only

\[
             E_P\cap\bigcup_\delta R_\delta\ne\varnothing, \tag{8.6b}
\]

not that one selected exterior lie in every \(R_\delta\).  A common cylinder
cover is instead a compressed all-cases rejection certificate.  The exact
interface/cylinder theorem and its sharp functional-Hall obstruction are
frozen in
`MATH_THEOREM_H3_K17_3664_DELTA_COMMON_EXTERIOR_AND_CYLINDER_COVER_GATE_20260802.md`.

### 8.3 The actual minimal remaining move

The present minimal object is a joint-zero-265-clean Hamming-two bank containing an
individually clean anchor and disturbing every stored semantic core.  Only
banks in (8.4) require a fresh exact q1 formula.

If fresh checked proofs eventually reject all 3,664 banks remaining after
Corollary 8.2A, then and only then

\[
                            \Theta_2>0                    \tag{8.7}
\]

on this one-for-one face.  The next in-face radius would be three.  By the
geometry--colour factorization, a successful triple has the form

\[
 \boxed{\text{a structural pair anchor}
        +\text{ one final-net debt/rank/core closer}.}     \tag{8.8}
\]

An added cut, a base-cut exchange, or a C6/C8/q4 rethread leaves the present
metric and is incomparable with Hamming radius three.  No compiler, upper,
topology or unrestricted circuit lower bound follows from (8.7).

## 9. Frozen theorem boundary

The proved statements concern two distinct same-cardinality extra-cut
replacements of the frozen round02 bank, and the radius-three conclusion is
only within that same face.  Same-base alternatives, adding or deleting a
cut, base-cut exchanges, split/merge moves, C6/C8 circuits, q4 packets,
another dense bank and the complete `k=17` construction are outside scope.

The 67 movers and 154 raw occurrences, together with D's empty nonanchor
join, prove 21-anchor completeness.  The 349,642/169,426 census proves the
joint zero-265 ledger, and the 49-pair audit closes only the dirty-central
compensation slice.  The first semantic filter gives the historical
164,323/5,054 reduction.  The combined authenticated filters prove 165,713
of the 169,426 locally clean banks UNSAT; the checked dirty-central 49 are
separate, leaving exactly 3,664 clean-anchor exact-build rows.  Their exact
delta keys are all distinct, but a bounded common-exterior quotient remains
unproved.  None of these results proves topology,
upper/deep coverage or compiler feasibility; those gates remain literal and
separate.

The checked 49-bank proof bundle is frozen at

```text
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/proof_manifest.tsv
  SHA-256 7959c9ce00d855cd187fe24e770e785f908dee5106cef8daf75480a75d55c0b6
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/theorem.audit.json
  SHA-256 bf468abc0fd076613c81b21468f23e8e947e153eeff3d85e4bb52b15705e32f9
scratch/threadD_k17_round02_dirtycentral49_q1_20260802/THEOREM_SCOPE.txt
  SHA-256 bcda315af6bff664e7cb4a29df52479af4218e0008423a2a537bfa12316ca81d
```

The semantic-filter audit is
`scratch/threadD_k17_round02_semantic_filter_20260802/audit.json`, SHA-256
`d90115ba056c0ca9b0e98d17db652abfe0cec3883f3d49c08cac19b323a3d77a`.
The combined count ledger is
`scratch/threadD_k17_round02_delta_signatures_20260802/counts_union.tsv`,
SHA-256
`f184ade82dc8f63ac5bd74bf2d89aed25a9d57f05dcc830782480e6bbf3c8fa0`;
the 3,664-key audit is
`scratch/threadD_k17_round02_delta_signatures_20260802/audit.json`, SHA-256
`ddcd28ff60094b96426ac617a63b9e93aee0ab7c4e4c3aff0056ab8dc441bae4`.
