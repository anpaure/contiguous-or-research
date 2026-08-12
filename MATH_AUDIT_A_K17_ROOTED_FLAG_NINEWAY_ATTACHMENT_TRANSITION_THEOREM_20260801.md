# `k=17`: exact nine-way rooted-flag attachment and transition theorem

Date: 2026-08-01  
Lane: A / residence-first compressed chronology  
Status: exact theorem and independently replayed finite obstruction for the
authenticated rooted certificate

## 0. Verdict

Fix a rank-eight-rooted static flag certificate: one row at each rank-eight
necklace orbit, with a partition

\[
 Q=C_0\mathbin{\dot\cup}C_1\mathbin{\dot\cup}C_2.
\]

Retaining all nine aligned rank-nine incidences of every root gives exactly
`1430*9=12870` attachment states.  There is an exact local transition test
on these states.  A selection satisfying

1. one state at every root and every owner;
2. one compatible transition into and out of every selected state;

is equivalent to a pair of quotient incidence perfect matchings `D,H`
together with a literal depth-three age-compatible cycle cover.  If the
selected transition permutation is one cycle and its total phase voltage is
nonzero modulo 17, its physical lift is one cycle.

The construction automatically preserves the fixed type masses and every
certified lower flag orbit at ranks two through eight.  It does **not** make
the upper rank-ten palette, higher upper shadows, a safe linear opening, or
the common compiler automatic.

The old deficiency `1341` attached one particular owner matching and hence
does not obstruct this joint nine-way selector.  Likewise, the later `202`
universal zero-row obstruction belongs to a different switched flag file
(SHA `908651...`), not to the rooted certificate of SHA `ad9e15...`.
Those finite verdicts cannot be transported between the two flag tables.
The present table has now been replayed directly.  Its complete nine-way
transition catalogue has only 912 root-level turns, 761 zero-out roots,
848 zero-in roots, and packet-support matching number 530.  Therefore this
particular rooted certificate admits no transition cycle cover.  The
failure is in the flag partitions, not in a prematurely frozen owner
attachment.

## 1. The aligned incidence multigraph

Let `R` and `O` be the rank-eight and rank-nine necklace orbits on
`Z_17`.  Choose representatives `Q_q`, `T_o`.  An aligned incidence is a
triple

\[
 e=(q,o,\sigma),\qquad \rho^\sigma Q_q\subset T_o.       \tag{1.1}
\]

Because 17 is prime and both ranks are proper, the cyclic actions are free.
The incidence multigraph is 9-regular on both shores and has 12,870 edges.
Parallel aligned incidences, if present, are distinct edges.

For the fixed rooted flag at `q`, define the state carried by `e` as

\[
 C_j(e)=\rho^\sigma C_{q,j}\quad(0\le j\le2),\qquad
 C_3(e)=T_o-\rho^\sigma Q_q=\{\alpha_e\}.             \tag{1.2}
\]

Thus the state is a literal four-class partition of its owner.  A state
transversal is a set `S` of 1,430 incidence edges satisfying

\[
 |S\cap\delta(q)|=1\quad(q\in R),\qquad
 |S\cap\delta(o)|=1\quad(o\in O).                    \tag{1.3}
\]

Equivalently, `S` is an incidence perfect matching.  This is the exact
meaning of the statement that the selected states make `D` perfect; a
cycle through arbitrary attachment states without (1.3) does not suffice.

## 2. Exact rotated transition criterion

Let `e=(q,o,\sigma)` be a current state.  Let

\[
 h=(q,o',\tau)                                      \tag{2.1}
\]

be another aligned incidence through the **same old root**, distinct from
`e`.  Its owner orbit `o'` may equal `o`: a different aligned phase can be
a genuine physical changing-owner incidence even when the quotient owner
orbit is the same.  Put

\[
 \delta=\sigma-\tau\pmod {17}.                       \tag{2.2}
\]

Then

\[
 \rho^\delta(T_{o'}-\{\beta_h\})
   =\rho^\sigma Q_q,
 \qquad \beta=\rho^\delta\beta_h,                   \tag{2.3}
\]

where `beta_h` is the coordinate omitted by `h`.  Hence, in the current
physical gauge,

\[
 T_o=\rho^\sigma Q_q+\alpha_e,qquad
 \rho^\delta T_{o'}=\rho^\sigma Q_q+\beta.           \tag{2.4}
\]

Let `f=(q',o',\sigma')` be a prospective next attachment state and write

\[
 \widetilde C_j=\rho^\delta C_j(f)\quad(0\le j\le3).
\]

### Theorem 2.1 (literal transition iff)

There is a literal depth-three age transition from `e` to the aligned copy
of `f` through `h` if and only if

\[
 \widetilde C_1\subseteq C_0(e),\qquad
 \widetilde C_2\subseteq C_1(e),\qquad
 \widetilde C_3\subseteq C_2(e).                     \tag{2.6}
\]

Under (2.4) and (2.6), both

\[
 \beta\in\widetilde C_0,                              \tag{2.5}
\]

and the age-zero refresh identity are forced:

\[
 \widetilde C_0
 =\{\beta\}\mathbin{\dot\cup}
   \bigl(C_0(e)-\widetilde C_1\bigr)
   \mathbin{\dot\cup}
   \bigl(C_1(e)-\widetilde C_2\bigr)
   \mathbin{\dot\cup}
   \bigl(C_2(e)-\widetilde C_3\bigr).                \tag{2.7}
\]

#### Proof

In a literal update the unique old age-three coordinate `alpha_e` is
deleted, the coordinate `beta` enters at age zero, and every retained
coordinate either advances one age or is refreshed to age zero.  This gives
(2.5)--(2.6).

Conversely, (2.4) says that the next owner is the old root plus `beta`.
The four `widetilde C_j` partition that owner.  By (2.6), their classes of
ages one, two and three lie disjointly in the corresponding preceding old
classes.  Since `beta` is outside the old root, it lies in none of those
three survivor cells and is therefore forced into `widetilde C_0`.  Taking
the complement of `widetilde C_1 dotcup widetilde C_2 dotcup
widetilde C_3` inside the next owner gives exactly (2.7).  Thus every other
retained coordinate is refreshed and the update is literal.  `square`

Condition (2.5) is a useful fail-closed defensive replay row, but it is
encoding-redundant once (2.4), the complete prematerialized target
partition, and all three containments (2.6) are enforced.

### Corollary 2.2 (root-cycle normal form)

Along one lifted quotient lap, write two consecutive selected roots in the
running physical gauge as `Q_i,Q_(i+1)`.  A transition between their selected
states necessarily has

\[
 T_{i+1}=Q_i\cup Q_{i+1},\qquad
 \alpha_{i+1}=C_{3,i+1}=Q_i-Q_{i+1},\qquad
 \beta_i=Q_{i+1}-Q_i.                              \tag{2.8}
\]

Consequently it is compatible if and only if the roots are Johnson
adjacent and

\[
 Q_i-Q_{i+1}\subseteq C_{2,i},\qquad
 C_{2,i+1}\subseteq C_{1,i},\qquad
 C_{1,i+1}\subseteq C_{0,i}.                        \tag{2.9}
\]

Here the first set in (2.9) is a singleton.  The entering singleton
`Q_(i+1)-Q_i` then lies in `C_(0,i+1)` automatically: the latter root is
partitioned by its first three classes, while its classes one and two are
subsets of `Q_i`.

Thus the whole object may equivalently be written as a quotient cyclic
ordering of the rooted rows, with compatible phase alignments, such that

\[
 \{[Q_{i-1}\cup Q_i]:0\le i<1430\}=\mathcal O_9     \tag{2.10}
\]

as a multiset without repetition, and (2.9) holds at every step.  Equation
(2.10), not adjacency alone, is the exact owner-bijection row.  It is the
remaining global correlation after the local age conditions have been
compressed.  In the running physical gauge the closing condition is

\[
                         Q_{1430}=\rho^\Delta Q_0,              \tag{2.11}
\]

where `Delta` is the total voltage.  The untwisted equality
`Q_(1430)=Q_0` holds only at zero voltage; equation (2.10) is correctly an
owner-orbit statement.

#### Proof

The `H` edge at `Q_i` and the selected `D` edge of the next state are two
facets of the same rank-nine owner, giving the union in (2.8).  The
coordinate omitted by the next `D` edge is the element of
`Q_i-Q_(i+1)`, and the coordinate entering through `H` is the element of
`Q_(i+1)-Q_i`.  Substituting these identities in Theorem 2.1 yields (2.9).
Conversely (2.8)--(2.9) reconstruct the `D` and `H` incidences and invoke
Theorem 2.1.  Distinct use of every owner is precisely (2.10).  `square`

## 3. Why the second matching is automatic

Select a state transversal `S` and a directed transition set `Y` such that
every selected state has exactly one outgoing and one incoming transition,
and no unselected state is incident with a selected transition.  Define

* `D` to contain the selected state incidence `T_o--Q_q`;
* `H` to contain the old-root incidence `Q_q--T_{o'}` used by the selected
  outgoing transition from that state.

### Theorem 3.1 (two-perfect-matching equivalence)

`D` and `H` are perfect matchings of the quotient incidence multigraph.
Moreover, the directed cycles of `Y` are exactly the alternating cycles of
`D union H`, after contracting each selected `D` edge.

#### Proof

Equation (1.3) gives one selected `D` edge at every root and owner.  For
`H`, the unique outgoing transition at the state rooted at `q` gives one
`H` edge at `q`.  The unique incoming transition at the unique selected
state owned by `o'` gives one `H` edge at `o'`.  Thus `H` is also perfect.
Following a selected `D` edge from an owner to its rooted state and then the
selected `H` edge through that root reaches exactly the owner of the next
state.  Hence contraction identifies the two cycle decompositions.
`square`

This proof pinpoints two necessary qualifications:

* outgoing compatibility alone does not make `H` perfect; the incoming
  equations are also required;
* a cycle cover is not a Hamilton cycle.  One must additionally exclude
  every proper directed subtour.

For a selected quotient cycle `e_0,...,e_(1429)`, let `delta_i` be (2.2).
Starting with any physical phase `phi_0`, set

\[
 \phi_{i+1}=\phi_i+\delta_i.
\]

Theorem 2.1 then holds literally at every physical step.  Its total voltage

\[
 \Delta=\sum_i\delta_i\pmod {17}                     \tag{3.1}
\]

determines the lift.  Since 17 is prime, one quotient cycle lifts to one
physical cycle if and only if `Delta != 0`; `Delta=0` gives 17 translated
cycles.

## 4. Automatic lower flags and residence

Every selected state is only a rotation of its fixed rooted row.  Therefore
selecting one state at every root preserves, orbit for orbit,

\[
 C_0,\qquad C_0\cup C_1,\qquad Q=C_0\cup C_1\cup C_2,
\]

and hence all lower target multiplicities certified at ranks two through
eight.  The multiset of row types is unchanged as well.  Across a literal
transition, the old root is

\[
 Q=T-C_3=T\cap T',                                  \tag{4.1}
\]

so the rank-eight turn palette is exactly the rooted palette.

The same literal recurrence gives depth-three positive residence.  A newly
inserted coordinate begins in age zero.  Before it can be deleted it must
occur successively in ages one, two and three; a refresh only delays this.
Thus every cyclic positive owner run has length at least four.

No corresponding upper conclusion follows from `D,H` being perfect.  The
rank-ten colour is `T_i union T_(i+1)`, not an incidence shore of either
matching, and must still be constrained explicitly.  Higher upper shadows,
a safe opening, and source/common-cap compatibility remain separate.

## 5. Exact finite formulation

Use one binary `z_e` per attachment state and one binary `y_(e,f,h)` per
transition satisfying Theorem 2.1.  The complete local formulation is

\[
 \sum_{e\in\delta(q)}z_e=1,\qquad
 \sum_{e\in\delta(o)}z_e=1,                          \tag{5.1}
\]

\[
 \sum_{(e,f,h)}y_{e,f,h}=z_e,qquad
 \sum_{(g,e,h)}y_{g,e,h}=z_e.                       \tag{5.2}
\]

Equations (5.1)--(5.2) are necessary and sufficient for the quotient
cycle-cover object.  Hamiltonicity requires directed subtour cuts, and a
connected physical lift requires (3.1) to be nonzero.  Upper rows are not
implicit in this model.

The source

```text
scratch/build_k17_rooted_flag_attachment_cycle_20260801.cpp
```

implements (5.1)--(5.2).  Its phase convention is correct: an incidence
stores `shift sigma` with `rot(Q,sigma)=T-owner-minus-complement`; for an
old-root `H` incidence of shift `tau`, it uses
`delta=sigma-tau`.  Thus (2.3) holds.  Its test that the `H` complement lies
in the unrotated next `C0` is equivalent, after the same rotation, to
(2.5); this is a sound redundant defensive test.  The three bit-subset tests
are exactly (2.6).  The omitted explicit equality (2.7) is forced and need
not be encoded.

The builder excludes quotient owner self-transitions.  This is harmless
for the intended 1,430-state Hamilton cycle, but it makes the generated
cycle-cover model a loop-free subclass: a nonzero-phase state self-loop
could represent a separate physical 17-cycle in a weaker disconnected
objective.

## 6. Exact comparison with earlier obstructions

There are three distinct quantifier faces.

1. **Frozen attachment.**  The `89/1430` matching and deficiency `1341`
   in the rooted-factor note first choose one owner attachment per row and
   only then expose transitions.  This is one fixed `z` in (5.1).  It is
   not a bound on the optimum over all state transversals.

2. **All attachments of another flag table.**  The `202` universal dead
   packet rows and packet-support maximum `1158/1159` were computed after
   opening all 12,870 states, but for switched GKS flag certificates with
   SHAs `908651...` and `0a5add...`.  They are valid all-attachment
   obstructions for those tables only.

3. **The present rooted certificate.**  The certificate
   `scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv`, SHA
   `ad9e15f7...`, has different literal partitions (already its first row
   differs from the switched files).  Its full transition model was
   therefore replayed independently rather than inferred from either prior
   face.  The exact census is

   ```text
   attachment states                    12,870
   root-level phase-labelled turns          912
   labelled state arcs                    7,296
   zero-out / zero-in roots             761 / 848
   zero-out / zero-in states          7,329 / 12,010
   packet-support maximum matching          530
   packet loops                               0
   ```

   The factor-eight identity is exact: for a fixed geometric root turn with
   entering coordinate `beta`, precisely the eight old attachments
   `alpha != beta` yield state arcs.  Thus even the scalar count
   `912<1430` proves that some root has no outgoing turn; the independent
   replay strengthens this to 761 named zero-out roots.  This violates the
   singleton Hall row before owner exactness, subtours, or voltage are
   imposed.

   The smallest explicit singleton cut is root `0`:

   ```text
   Q=255, type=8, (C0,C1,C2)=(159,64,32).
   ```

   Across all 81 choices of entering coordinate and next deleted coordinate,
   every candidate fails the forced refresh/entering test (and often one or
   more survivor containments).  Hence all nine attachment states of this
   root have zero outdegree.  This one row alone is a solver-free
   infeasibility certificate.

Thus the compressed construction and its phase algebra are correct, and
they correct the quantifier error in the old frozen-attachment diagnostic,
but the authenticated rooted flag table still fails decisively.  A live
lane must alter the rooted partitions (for example by exact containment
switches) while retaining the static flag tower, then rerun the same
nine-way criterion.  On any positive future table, single-cycle/voltage,
upper, opening, and compiler gates would remain.

## 7. Frozen audit artifacts

```text
scratch/build_k17_rooted_flag_attachment_cycle_20260801.cpp
  SHA256 0c51a28c4c7ab3766d828d40031381272631eda5d1cd64bb70cac25b8f69ed59

scratch/audit_threadA_k17_rank8_rooted_nine_attachment_transition_20260801.cpp
  SHA256 0db4dcefb7fd65f48e4a8aaf39ffb10cd538a337a396bd150957bf28ea813c66

scratch/threadA_k17_rank8_rooted_nine_attachment_transition_20260801/rooted9.stats.json
  SHA256 8118ad6b6487d7d82cce9a6147ff0436e01437d43308460bb19ab63c92d06252

scratch/threadA_k17_rank8_rooted_nine_attachment_transition_20260801/rooted9.transitions.tsv
  SHA256 375d015b66201e1b94cb383e2f924387aa172b1c02fc3e657b492b52eaa228cc

scratch/threadA_k17_rank8_rooted_nine_attachment_transition_20260801/independent.audit.json
  SHA256 167fd9a1955ec5d7e1a6c563d86734f3e3d9495d212112988fb2e5e58659eb65
```

The builder and independent audit agree on every displayed global count.
The independent audit additionally reconstructs the type masses and every
rank-two-through-eight suffix orbit directly from the input certificate.
