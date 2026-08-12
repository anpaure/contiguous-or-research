# Fixed typed repair banks do not automatically extend to a guarded same-parity child

Date: 2026-08-01
Lane: H2, finite-bank `O(1)` recursion
Status: dimension-uniform no-go for the unqualified statement; exact
conditional composition theorem and surviving gate

## 0. Verdict

The following three proved statements do not compose by themselves.

1. A fixed bank of pairwise four-typed-resource-disjoint target atoms can be
   planted in private Boolean `C6` packets before the valid
   Delcourt--Postle forest is selected.
2. A diamond-ready Pascal parent has a child owner two-factor whose q1
   colours are exact.
3. A selector-separable packet bank repairs all but its Hall deficiency.

The missing quantifier is joint.  Typed compatibility does not imply a
rooted q1 opening, residence compatibility, preservation of interval
witnesses, or a common compiler state.

The unqualified finite-`H` statement is false even asymptotically.  For
every owner rank `m>=7` there are four mutually typed-compatible repair tasks
and four mutually typed-compatible named one-edge rails such that the rails
form a saturated Johnson `C4`.  Any degree-two factor preserving all four
rails has that `C4` as a closed component and therefore has no connected
spanning factor or Hamilton opening.  For `m>=40`, the central target bank
simultaneously lies inside the guaranteed range of the fixed-`H` planting
theorem.  Thus central C6
planting can succeed while the required q1 factor/opening sidecar is
impossible.

There is a second, independent mismatch.  A fixed bank supplies exactly `H`
gain-one switches.  If the Delcourt--Postle body has deficit `h`, activation
leaves deficit `h-H`.  The conclusion `h=o(N)` permits `h` to tend to
infinity, so a fixed bank cannot turn that theorem into `O(H)` leave.  The H2
cover-down theorem still needs packet records for all but `O(H)` of the
**actual** leave.

A positive finite-`H` composition interface does hold after adding the exact rooted and
guard-complete hypotheses.  In particular, if one old compiler matching is
changed only on at most `aH` target rows, `bH` cells, and `qH` new target
rows, the same cap state has matching deficiency at most

\[
                              (a+b+q)H.                 \tag{0.1}
\]

This gives the requested absolute `O(H)` common-cap conclusion when
`a+b+q` is uniform over the recursive depths; otherwise the exact statement
is `O_d(H)`.  It does not
construct the rooted q1 target, jointly place the available resident long
collars, preserve interval witnesses, or produce the growing leave-aligned
selector bank.

No Joos--Mubayi--Smith exact theorem is used.

## 1. Exact formulation of the refuted statement

An ordered rank-`m` Boolean atom is

\[
 e=(L,U;T_{\rm tail},H_{\rm head}),\qquad
 |L|=m-1,\quad |U|=m+1,                                  \tag{1.1}
\]

where `L\subset T,H\subset U`.  A **weakly compatible task bank** consists
of `H` legal target atoms which are pairwise disjoint on the four typed
resource shores.  A task may additionally name

* physical q1 edges which must remain in the factor/opening sidecar;
* residence rails or exact run-collar states;
* occurrence-labelled interval witnesses for upper targets of any width;
  and
* target rows, cells, and a cap state for the terminal compiler.

Weak compatibility asks only that the named literal resources do not repeat
within their types.  It does not assume a rooted Hamilton extension or one
common chronology.

For fixed `H`, let `FH(H)` denote the assertion that there is `m_0(H)` such
that, for every `m>=m_0(H)` and every weakly compatible bank, one may choose
packet options and a same-parity child which

1. realizes all target gains with legal tail/head capacity;
2. has the exact q1 palette and one connected spanning factor/Hamilton-opening
   sidecar;
3. preserves all named residence rails and all named upper witnesses; and
4. has common-cap matching deficiency `O(H)`, with an absolute coefficient
   independent of `m`, `H`, and every recursive deadline depth/template in
   the asserted class.

The phrase “preserves q1” in `FH(H)` includes the connected factor-opening
sidecar used by the H2 cover-down theorem.  If it means only an unordered,
possibly disconnected q1 two-factor, the obstruction below is not
applicable, but that weaker state is not a recursive spanning chronology.

## 2. A dimension-uniform four-task obstruction

Let the cyclic indices below be modulo four.  For `m>=7`, choose a core `K`
of size `m-2` and eight distinct labels

\[
 z_0,\ldots,z_3,w_0,\ldots,w_3
\]

outside `K`.  This uses `m+6<=2m-1` labels.

Use these labels on the odd Pascal ground `Gamma` of size `2m-1`.  For the
fixed-bank theorem, regard the same target atoms inside the even ground
`Gamma union {infinity}` of size `2m`; the extra coordinate is unused by the
displayed atoms.

Define four protected q1 rail owners

\[
 X_i=K+z_i+z_{i+1}                                      \tag{2.1}
\]

and the directed rail atoms

\[
 p_i=\bigl(K+z_{i+1},\ K+z_i+z_{i+1}+z_{i+2};\
             (X_i)_{\rm tail},(X_{i+1})_{\rm head}\bigr). \tag{2.2}
\]

Independently define target owners

\[
 Y_i=K+w_i+w_{i+1}                                      \tag{2.3}
\]

and four repair targets

\[
 t_i=\bigl(K+w_{i+1},\ K+w_i+w_{i+1}+w_{i+2};\
             (Y_i)_{\rm tail},(Y_{i+1})_{\rm head}\bigr). \tag{2.4}
\]

Task `i` has target `t_i` and names the one-edge rail `p_i` for
preservation.

### Theorem 2.1 (uniform rooted-q1 no-go)

The eight atoms in (2.2)--(2.4) are mutually disjoint on every typed resource
shore.  In particular the four targets meet the hypothesis of the fixed-bank
planting theorem.  Nevertheless no connected spanning degree-two factor or
Hamilton-opening sidecar can contain all four named rails `p_i`.

Hence `FH(4)` is false.  The failure persists for every `m>=40`, where

\[
                     m-1>12\cdot4-10                         \tag{2.5}
\]

and the central target packets are guaranteed to plant.

#### Proof

The four lower colours `K+z_(i+1)` are distinct.  The four upper colours
`K+z_i+z_(i+1)+z_(i+2)` are distinct because they are the four consecutive
triples of a labelled `C4`.  Tails `X_i` are distinct, as are heads
`X_(i+1)`.  The same statements hold for the `w` bank, and no `z` resource
equals a `w` resource.  Thus all typed resources are distinct.

Physically, the protected edges are

\[
                  X_0X_1,X_1X_2,X_2X_3,X_3X_0.             \tag{2.6}
\]

Every `X_i` already has its two factor edges in (2.6).  Any degree-two graph
containing all four therefore has this `C4` as a connected component.  Since
`binom(2m-1,m)>4`, it cannot be one spanning cycle, and no edge outside the
cycle can be opened or spliced into it while the four rails remain fixed.
This proves the no-go. \(\square\)

The obstruction is deliberately guard-level: each task and each named rail
is individually legal, and all typed resources are private.  What fails is
the omitted rooted-topology condition.  Adding residence, upper-witness, or
compiler requirements cannot repair that earlier failure.

### The sharp finite protected cut

There is also an authenticated smaller obstruction at owner rank three.
In `J(5,3)`, four protected edges have eight distinct owners, four distinct
lower colours, and four distinct adjacent-upper colours, yet no q1-rainbow
Hamilton cycle contains them.  Exhaustion shows that every protected set of
at most three edges with those injectivity properties does extend, while
this size-four set does not.  Thus even a protected matching, rather than a
closed protected cycle, needs a rooted target hypothesis.  This finite cut
does not by itself refute a theorem stated only for sufficiently large
`m`; Theorem 2.1 supplies the dimension-uniform refutation when arbitrary
named rails are allowed.

## 3. A fixed packet bank cannot close an unbounded DP leave

Let `B^-` be the `2H`-atom off bank from the fixed-bank theorem and let `F`
be its Delcourt--Postle body.  Put

\[
                  h=N-|F\cup B^-|.                         \tag{3.1}
\]

Activation replaces `2H` off atoms by `3H` on atoms, so the final deficit is
exactly

\[
                  N-|F\cup B^+|=h-H.                       \tag{3.2}
\]

The proved bulk estimate is

\[
 |F|\ge N-ND^{-\alpha_g}-{N\over g+1}-18H,\qquad
 D=m(m+1),                                                 \tag{3.3}
\]

which is an `N-o(N)` statement after diagonalizing `g`.  It is not an
`N-O(H)` statement.

### Proposition 3.1 (selector cardinality is necessary)

If a body has deficit `h` and the desired residual deficit is at most `CH`,
then every gain-one cover-down uses at least

\[
                              h-CH                          \tag{3.4}
\]

packet records.  In particular a bank of only `H` records can succeed only
when `h<=(C+1)H`.

#### Proof

Each selected packet increases the matching order by exactly one.  This is
also the order equation in the H2 selector-separable theorem. \(\square\)

Thus the fixed bank is a protected terminal reserve, not the growing bank
needed to align an arbitrary Delcourt--Postle leave.  The latter must satisfy
the H2 Hall condition on all but `O(H)` of the actual leave.

## 4. The exact positive finite-bank composition interface

The preceding no-go identifies the missing hypotheses.  The following
statement records the strongest proof-safe positive composition.

### Definition 4.1 (guard-complete rooted packet record)

A bank of `H` packet records is guard-complete when all of the following are
given literally.

1. **Central planting.**  The target atoms are pairwise four-typed-resource
   disjoint, `m-1>12H-10`, and selected complete C6 supports are private.
   Their closed support is deleted before the Delcourt--Postle body is
   chosen.  For type HT this costs at most `18H` resources.  For type RC the
   closed support also contains every long rail; since one collar has
   `2d+4` atoms and `2d+6` physical vertices, deleting both outer resources
   per atom and both role copies per physical vertex costs at most

   \[
                              (8d+20)H                       \tag{4.0}
   \]

   typed resources.  The asymptotic bulk conclusion needs only
   `(8d+20)H=o(N)`, which includes fixed `H` and
   `d=Theta(sqrt(m))`.
2. **One exact q1/physical sidecar type.**  One of the following two literal
   records is supplied.

   * **HT (Hamilton-transparent).**  A protected alternating-circuit route
     from the Pascal factor to an initial q1-rainbow Hamilton state
     `Sigma_0` fixes every occurrence which must survive initialization.
     There is one packet order `pi` and an occurrence-labelled sequence

     \[
       \Sigma_0,\Sigma_1,\ldots,\Sigma_H                \tag{4.1}
     \]

     such that `Sigma_i` is obtained from `Sigma_(i-1)` by replacing the
     designated **complete** old phase of packet `pi(i)` by its complete new
     phase.  Every `Sigma_i` is q1-rainbow and Hamiltonian, its cyclic
     orientation agrees with all declared tail/head directions, and every
     state has the same untouched opening edge `g`.  Equivalently, each
     packet has the literal three-rail wrapper with the unique `tau=(13)`
     endpoint pairing, or an independently checked occurrence-level
     certificate of the same statements.  A terminal rooted target merely
     containing the old packet occurrences is insufficient.

   * **RC (resident cycle collar).**  Let `e_i` be the target, let `O_i^-`
     be its two-atom actual off phase, put `O_i=O_i^- union {e_i}`, and let
     `N_i` be the three-atom on phase.  Augment the packet by an exact long
     square-collar rail `R_i=E(R_d)`, where `d<=m-2`.  There are three
     distinct states:

     \[
     A_i^-=O_i^-\cup R_i,\qquad
     \widehat G_i^-=A_i^-\cup\{e_i\}=O_i\cup R_i,
     \qquad G_i^+=N_i\cup R_i.                           \tag{4.2}
     \]

     The actual central switch is the gain-one forest move
     `A_i^- -> G_i^+`.  Only the **virtual complete** switch
     `widehat G_i^- -> G_i^+` has equal typed signature and transports q1.
     The actual off state is the resident old cycle opened at `e_i`, so all
     remaining internal runs retain length at least `d+1`.

     The `H` prepared segments are pairwise physically and resource private.
     An auxiliary occurrence-labelled Pascal sidecar contains every
     `widehat G_i^-`.  In one declared order, its virtual states are obtained
     by adjoining every still-pending target `e_j` to the corresponding
     actual central state; hence each step replaces one
     `widehat G_i^-` by `G_i^+`.  A final current-state
     quotient/endpoint-reconnection certificate proves that the terminal
     sidecar has one q1-rainbow Hamilton cycle with a designated untouched
     opening edge (or directly one opened Hamilton path).  Intermediate
     virtual states need not be Hamiltonian, although their q1 palettes are
     exact.  The sidecar exterior is not asserted to equal the
     Delcourt--Postle exterior; any use requiring that physical
     identification must supply it occurrence by occurrence.
3. **Residence guards.**  In type HT, every changed chronology collar has
   its exact run automaton, and every named residence rail is untouched or
   replaced before its last old occurrence is removed.  In type RC, the
   long-collar theorem supplies the internal run floor `d+1`; only the
   initialization route, external joins, endpoint reconnection, and any
   named rail outside the prepared collar require additional residence
   checks.
4. **Upper guards.**  For every named upper target at every required width,
   one literal interval occurrence is common to all visible states, or the
   replacement dependencies form an acyclic install-before-delete order.
   Adjacent-union equality alone is not accepted as an all-width witness.
5. **Physical composition.**  The H2 current-state quotient graphic tests
   pass in one declared serial order, including all packet rails, cut edges,
   and the protected scaffold.
6. **Compiler footprint.**  In one complete cap state `theta` which is legal
   both before and after the packet batch, let `A` be
   the old target rows whose incident graph may change, `B` the old cells
   whose incident graph may change, and `Q` the new target rows.  Outside
   `A union B`, every old target--cell edge is retained.  There are constants
   `a_d,b_d,q_d`, independent of `m` and `H` for the declared depth/template,
   such that

   \[
                     |A|\le a_dH,\quad |B|\le b_dH,\quad
                     |Q|\le q_dH.                            \tag{4.3}
   \]

   Put `C_cap(d)=a_d+b_d+q_d`.  The absolute `O(H)` conclusion requested by
   `FH(H)` requires `sup_d C_cap(d)<infinity`; without that uniformity the
   conclusion is only `O_d(H)`.

These conditions are joint.  Separate existence of a planted packet bank
and an exact Pascal factor does not supply row 2, 3, 4, or 6.
Throughout this theorem, “q1 sidecar” means the auxiliary
occurrence-labelled certificate in row 2.  It shares the declared packet
occurrences but need not share the Delcourt--Postle exterior.  A literal
child chronology identifying the two exteriors is a stronger hypothesis and
is not inferred here.

### Lemma 4.2 (common-cap Lipschitz bound)

Suppose the old compiler graph in cap state `theta` has a matching covering
all old target rows.  Under row 6 of Definition 4.1, the new compiler graph
has matching deficiency at most

\[
                              |A|+|B|+|Q|
                         \le C_{\rm cap}(d)H.                 \tag{4.4}
\]

The optimized common-cap deficiency is no larger.

#### Proof

Restrict the old matching by deleting every matched edge incident with a row
in `A` or a cell in `B`.  At most `|A|+|B|` matching edges are lost, and all
remaining edges survive in the same cap state.  Treating every new row in
`Q` as unmatched adds at most `|Q|` to the deficiency.  This proves (4.4).
The optimized deficiency is the minimum over legal cap states, so it is at
most the value in `theta`. \(\square\)

### Theorem 4.3 (conditional finite-`H` guarded interface)

Assume a guard-complete rooted packet record, and assume that the old graph
in its declared cap state `theta` has a matching covering every old compiler
row.  Then the `H` target gains can
be planted in the same-parity child so that

* all tail/head capacities and the declared terminal physical forest state
  hold;
* the q1 factor/opening sidecar is exact;
* every named residence rail and all-width upper witness is retained; and
* terminal common-cap deficiency is at most `C_cap(d)H`.

Consequently this is absolute `O(H)` exactly when the record family has
`sup_d C_cap(d)<infinity`; for one fixed depth it is `O_d(H)`.

The Delcourt--Postle bulk outside the closed packet support remains
`N-o(N)`.  If, in addition, the **post-fixed-bank actual** bulk leave has an
H2 selector-separable packet matching of deficiency at most `cH`, with
serial transparent records jointly compatible with the fixed bank, then
the remaining normalized four-resource leave is at most

\[
                              (cH,cH,2cH).                    \tag{4.5}
\]

This last assertion is a central four-resource ledger only.  It transports
the residence, upper-witness, q1-opening, and common-cap conclusions as well
only if the growing records themselves satisfy rows 2--5 and their **total**
changed compiler footprint, jointly with the fixed bank, still satisfies
row 6 with `O(H)` bounds.

#### Proof

Deleting the closed support in row 1 and rerunning the fixed-bank
Delcourt--Postle argument gives a bulk disjoint from both phases.  The extra
loss in type RC is at most `(8d+20)H`, so it is still `N-o(N)` whenever
`(8d+20)H=o(N)`.

In type HT, the protected q1 circuit route reaches `Sigma_0` and the
separately required serial sidecar sequence transports the exact owner/q1
Hamilton opening through every complete old-to-new packet phase.  In type
RC, the actual move `A_i^- -> G_i^+` gains the target, while the associated
virtual move `widehat G_i^- -> G_i^+` has equal typed signatures and
therefore transports q1.  Adjoining all still-pending targets gives the
exact virtual q1 sequence; the actual and virtual terminal states coincide.
The resident-collar theorem gives the internal run bound, and the assumed
terminal quotient/reconnection certificate supplies the connected opening.
Rows 3--4 make every remaining
residence and upper-witness assertion literal rather than marginal.  Row 5
and the H2 serial graphic theorem give the terminal physical forest.  Lemma
4.2, using the explicitly assumed old compiler matching, gives the
common-cap bound.  Finally the H2 Hall cover-down theorem applied to the
post-fixed-bank actual leave gives the central ledger (4.5).  Its other
guard conclusions require the extra joint hypotheses stated after (4.5).
\(\square\)

The theorem is useful because its common-cap conclusion is automatic from a
bounded footprint.  The hard existence work is concentrated in the rooted
and guard-complete rows.

## 5. Precise surviving gate

For an unconditional `B(k)+O(1)` recursion, it now suffices—and is not yet
proved—to establish the following joint statement for every fixed repair
budget `H` and deadline depth `d` above a dimension threshold.

1. Choose one physical route jointly with the Pascal factor and packet
   options: either an HT rooted Hamilton target with the full serial sidecar
   sequence, or pairwise-private prepared RC long rails with a terminal
   quotient/endpoint reconnection.  Arbitrary typed-compatible immutable
   rails are impossible by Theorem 2.1, and one terminal target alone does
   not certify HT packet switches.
2. On the HT route, export a bounded-interface chronology preserving both
   residence and one literal witness for every protected upper target at
   every width.  On the RC route, plant the prepared `R_d` segments
   (collar-internal residence is automatic) and preserve the external joins
   and all-width upper witnesses through their reordered owner bank.
3. Choose a **growing** selector-separable packet bank for the actual
   Delcourt--Postle leave, of Hall deficiency `O(H)`.  The fixed `H` central
   reserve cannot replace this row.
4. Carry one cap state whose changed target/cell footprint is `O(H)`
   uniformly in the depth; then Lemma 4.2 supplies the absolute common-cap
   estimate automatically.  A depth-dependent footprint gives only
   `O_d(H)`.
5. Identify the auxiliary q1 sidecar with the literal terminal child
   chronology occurrence by occurrence, or prove a separate lift theorem
   which makes that identification unnecessary.  Segmentwise palette
   agreement alone does not identify the exteriors.
6. Regenerate the same bounded record in the next same-parity child.

The HT part of the first row is a private rooted Middle Levels extension
problem, not a consequence of ordinary Hamiltonicity.  The RC alternative
replaces it by prepared-segment packing and endpoint reconnection; it does
not make arbitrary immutable rails extendable.  The second row is the exact
Shadow--Braid occurrence relation, not adjacent-upper palette equality.  The
third is the positive-semigroup/Hall correlation missing from
Delcourt--Postle.  These are the surviving gates.

For the long square-collar subcatalogue, the resident-return theorem already
supplies Definition 4.1(3) locally at every prescribed depth `d<=m-2`: its two phases
have the same complete typed signature and the required run floor.  What is
still missing is pairwise-private prepared-segment placement and endpoint
reconnection, plus arbitrary-width upper transparency and the bounded
common-cap footprint.  Thus residence is not an intrinsic local obstruction
for that subcatalogue, but its boundary joins remain part of the joint host
record.  If the minus-segment initialization uses unrestricted q1 incidence
circuits, their exterior residence is also a separate guard.

## 6. Audit and dependencies

The dependency-free audit

```text
scratch/audit_h2_finite_h_recursive_host_rooted_q1_nogo_20260801.py
```

checks the two disjoint four-atom typed banks for every `7<=m<=64`, the
closed protected `C4`, the planting threshold for `H=4`, Proposition 3.1,
the resident-collar virtual/actual and closed-support arithmetic, and the
common-cap restriction bound.  It writes

```text
scratch/h2_finite_h_recursive_host_rooted_q1_nogo_20260801.audit.json.
```

The proof uses the following results only at their stated scopes.

* `MATH_THEOREM_BOOLEAN_HEX_PLANTED_DP_FIXED_BANK_20260801.md`;
* `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`;
* `MATH_THEOREM_O1_PROTECTED_Q1_HAMILTON_EXTENSION_CUT_20260801.md`;
* `MATH_THEOREM_H2_BOOLEAN_DIAMOND_C6_TAIL_HEAD_SIDECAR_COVERDOWN_20260801.md`;
* `MATH_THEOREM_BOOLEAN_HEX_RESIDENT_LONG_SQUARE_COLLAR_20260801.md`.

The audit does not construct a guarded recursive host.  Its no-go concerns
the unqualified universal quantifier, and its positive theorem is
conditional on the displayed joint records.
