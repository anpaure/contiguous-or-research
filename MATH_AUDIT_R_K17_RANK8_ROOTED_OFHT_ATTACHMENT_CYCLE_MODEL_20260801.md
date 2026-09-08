# Audit of the `k=17` rank-eight-rooted OFHT attachment-cycle model

Date: 2026-08-01  
Lane: R, finite specialization of OFHT  
Verdict: the proposed `1,430 x 9 = 12,870` state model is an exact
quotient-level multiple-cycle NRFC/OFHT model **provided** aligned incidence
phases are not collapsed and every transition is tied to its complete two
endpoint states.  The second incidence matching `H` is then automatic; it
does not need an independent matching layer.  Connectivity, nonzero voltage,
upper shadows, and the compiler remain outside the cycle-cover model.

For the authenticated rooted certificate of SHA `ad9e15f7...`, the complete
model has now also been independently replayed and is decisively
infeasible: 761 roots have no outgoing turn, 848 have no incoming turn, and
root 0 alone is an explicit singleton Hall obstruction.  Thus the model is
correct but this fixed static flag table is not a dynamic seed.

The resulting corrected model agrees with Sections 1--5 of
`MATH_THEOREM_K17_PACKET_STATE_TRANSVERSAL_CYCLE_MINMAX_AND_GKS_ALTERNATING_REPAIR_20260801.md`;
the derivation below independently checks the proposed smaller description.

## 1. Frozen static input and complete attachment states

Let `K` run through the 1,430 certified packets.  Packet `K` consists of a
rank-eight root and its fixed literal partition

\[
 Q_K=C_{K,0}\mathbin{\dot\cup}C_{K,1}
                  \mathbin{\dot\cup}C_{K,2}.                  \tag{1.1}
\]

The packet roots run through every rank-eight `Z_17` orbit exactly once,
and the fixed packets cover every required lower suffix orbit exactly once.

Fix one representative `T_O` of each rank-nine owner orbit.  A complete
attachment state is

\[
                         s=(K,O,a),                            \tag{1.2}
\]

where

\[
                         \rho^aQ_K\subset T_O.                 \tag{1.3}
\]

It carries

\[
 C_i(s)=\rho^aC_{K,i}\quad(0\le i<3),\qquad
 C_3(s)=T_O\setminus\rho^aQ_K.                                \tag{1.4}
\]

The last cell is a singleton.  The quotient incidence graph is a
9-regular **multigraph**, so every packet has exactly nine states and there
are exactly 12,870 states.

### Audit warning 1.1 (parallel alignments are state data)

The state is not merely the pair `(root orbit, owner orbit)`.  Two aligned
incidences with the same orbit endpoints can be distinct parallel edges and
have different `a`.  Collapsing them destroys both the literal cells (1.4)
and the later voltage labels.  A sound implementation keys a state by the
packet, owner orbit, and aligned incidence/phase.

A selected state vector `z` must obey

\[
 \sum_{s:K(s)=K}z_s=1\quad(K),\qquad
 \sum_{s:O(s)=O}z_s=1\quad(O).                                \tag{1.5}
\]

These are exactly one packet/root and one rank-nine owner orbit.

## 2. Why the raw successor menu has size at most 72

Work in the physical gauge of a source state `s`.  Put

\[
 Q_s=C_0(s)\dot\cup C_1(s)\dot\cup C_2(s),\qquad
 C_3(s)=\{\alpha\},\qquad T_s=Q_s\cup\{\alpha\}.               \tag{2.1}
\]

A changing-owner depth-three transition must delete `alpha`.  Its next
owner is therefore

\[
                         T'=Q_s\cup\{\beta\},
       \qquad \beta\in[17]\setminus T_s.                       \tag{2.2}
\]

There are eight choices of `beta`.  Each rank-nine `T'` has nine aligned
rank-eight subsets.  Because the packet roots contain every free rank-eight
orbit once, each such subset determines one packet together with one
alignment phase.  Thus there are

\[
                              8\cdot9=72                         \tag{2.3}
\]

raw phase-labelled target candidates per source state, before age
compatibility is imposed.  Several candidates can project to the same pair
of quotient state IDs; their phase/voltage labels must still be retained.

## 3. Exact literal arc criterion

Let `t` be a candidate target state and rotate its **whole** attachment
state through the phase `v` which puts its owner at `T'`.  Write

\[
                         D_i=\rho^v C_i(t)\quad(0\le i\le3).    \tag{3.1}
\]

### Theorem 3.1 (complete-state transition test)

There is a literal transition from `s` to the phase-`v` copy of `t` if and
only if (2.2) holds and

\[
                         D_{i+1}\subseteq C_i(s)
                         \qquad(0\le i<3).                     \tag{3.2}
\]

Equivalently, one may additionally check the redundant refresh identity

\[
 D_0=\{\beta\}\mathbin{\dot\cup}
     \bigdotcup_{i=0}^2\bigl(C_i(s)\setminus D_{i+1}\bigr).    \tag{3.3}
\]

#### Proof

Literal age evolution gives

\[
                         D_{i+1}=C_i(s)\setminus D_0,
\]

so (3.2) is necessary.  Conversely, the target cells form a complete
partition of

\[
 T'=\{\beta\}\mathbin{\dot\cup}C_0(s)
                     \mathbin{\dot\cup}C_1(s)
                     \mathbin{\dot\cup}C_2(s).
\]

The three disjoint survivor cells in (3.2) occupy subsets of their three
old cells.  Their complement in `T'` is therefore exactly the right side of
(3.3), and completeness of the target partition forces that complement to
be `D_0`.  Hence

\[
                         D_{i+1}=C_i(s)\setminus D_0
\]

for all three ages.  This is the literal recurrence.  \(\square\)

Thus “rotated inclusions” are sufficient only because all of the following
have already been materialized and checked:

1. the exact source partition;
2. the exact rotated target partition;
3. the common-root owner equation (2.2); and
4. all three inclusions in (3.2).

If a generator uses partial/type-only states, or tests only two survivor
rows, then (3.3) must be imposed explicitly and the reduction is unsound
without it.

## 4. Exact cycle-cover equations and the induced `H` matching

For every phase-labelled legal arc `e=(s,t,v)`, use a binary variable
`y_e`.  The exact degree equations are

\[
 \sum_{e:\,\mathrm{tail}(e)=s}y_e=z_s,
 \qquad
 \sum_{e:\,\mathrm{head}(e)=s}y_e=z_s
                         \qquad(s).                           \tag{4.1}
\]

Both rows are required.  They gate every arc to both selected endpoints and
make the selected directed graph a disjoint union of quotient cycles.

The selected `z` states themselves form the first incidence perfect
matching

\[
 D:\ Q_s\longmapsto T_s.                                      \tag{4.2}
\]

Every selected outgoing arc defines

\[
 H:\ Q_s\longmapsto T'=Q_s\cup\{\beta\}.                       \tag{4.3}
\]

### Theorem 4.1 (`H` is automatic)

Under (1.5) and both equalities (4.1), the incidences (4.3) form a perfect
matching from the 1,430 root orbits to the 1,430 owner orbits.

#### Proof

The outgoing equation gives exactly one `H` incidence from every selected
packet/root.  The incoming equation gives exactly one selected predecessor
for every selected target state, and (1.5) gives exactly one selected state
over every owner orbit.  Hence every owner is the head of exactly one `H`
incidence.  \(\square\)

Therefore no separate `H`-matching constraint is missing if `H.owner` is
literally the owner of the head state on every arc.  If separate `h`
variables are introduced, they must be channelled by

\[
 h_{Q,O}=\sum_{e:\,Q(\mathrm{tail}(e))=Q,
                         O(\mathrm{head}(e))=O}y_e.             \tag{4.4}
\]

Unlinked local `H` choices would be unsound.

At the physical aligned-incidence level, `D` and `H` on a source root are
different because `beta != alpha`.  Their quotient endpoint orbits may
nevertheless coincide.  Thus imposing `H.owner != D.owner` at the orbit
level is too strong and deletes valid nonzero-phase quotient self-loops.

## 5. Phase and voltage semantics

An arc label `v` rotates the entire target state, not only its owner or only
its root.  Along a quotient cycle, successive labels are accumulated.  If
the total voltage of one quotient component is

\[
                              \Delta\in\mathbb Z_{17},          \tag{5.1}
\]

then its physical lift has

\[
                              \gcd(17,\Delta)                   \tag{5.2}
\]

components, with the convention `gcd(17,0)=17`.  Since 17 is prime, a
nonzero voltage makes that quotient component lift to one physical cycle;
zero voltage makes 17 translated cycles.  Both cases cover every physical
state in the selected orbits exactly once.

There is no requirement that the incoming and outgoing arc labels at a
quotient state be equal.  The accumulated physical phase is the gauge in
which its outgoing arc is used.  Rotation-equivariance of Theorem 3.1 then
gives a consistent lift.

### Audit warning 5.1 (twisted closure)

One must not write a nonzero-voltage quotient component as a cyclic list of
physical representatives with the untwisted identity `Q_m=Q_0`.  In one
running physical gauge the correct closing relation is

\[
                              Q_m=\rho^\Delta Q_0.               \tag{5.3}
\]

Orbit brackets close normally.  Forgetting the twist silently imposes
`Delta=0`, the opposite of the connected-lift condition.

Legal phase-labelled self-arcs should be retained for an unrestricted
cycle-cover model.  A nonzero-phase quotient self-loop lifts to a legal
17-cycle.  Excluding all same owner-orbit or same state-ID arcs gives only a
loop-free sufficient subclass.  That exclusion is harmless if the declared
target is a 1,430-vertex quotient Hamilton cycle, but it is not equivalent
to unrestricted OFHT cycle-cover feasibility.

## 6. What is automatic and what is not

### 6.1 Automatic after a positive solution

1. **Owners.**  Equation (1.5), followed by the full 17-phase lift, uses
   every physical rank-nine owner exactly once.
2. **Lower targets.**  The fixed packet factor already uses every required
   rank-two-through-rank-eight target orbit exactly once.  Rotating a packet
   does not change its target orbit.  Since every nontrivial rank in
   `Z_17` is free, the full 17-phase lift gives every required physical
   lower target exactly once.
3. **Literal depth-three chronology.**  Theorem 3.1 on every selected arc
   gives one common age state at each vertex and hence a literal depth-three
   cyclic chronology.  No fresh survivor partition is chosen independently
   for its incoming and outgoing arcs.
4. **The two incidence matchings.**  `D` is (1.5) and `H` follows from
   Theorem 4.1.

The full 17-phase lift is needed for physical named coverage.  Nonzero
voltage is not: it is needed only to fuse the 17 translated lifts of a
quotient component.

### 6.2 Still outside the model

The degree equations produce a quotient cycle cover, not necessarily one
quotient cycle.  A Hamilton target additionally needs directed subtour cuts.
One physical Hamilton cycle additionally needs nonzero total voltage.

The model also does not by itself impose:

* upper-q1 or deeper upper-shadow coverage;
* a physical opening and its boundary losses;
* any nonflat or longer residence requirement beyond the literal
  depth-three age chronology; or
* the common-cap/compiler matching.

## 7. Exact verdict on the authenticated rooted table

The independent O3 replay frozen in
`MATH_AUDIT_A_K17_ROOTED_FLAG_NINEWAY_ATTACHMENT_TRANSITION_THEOREM_20260801.md`
opens all nine aligned attachments of every row of

```text
scratch/k17_rank8_rooted_static_age_flag_20260801.certificate.tsv
SHA256 ad9e15f724b5048c00cf43ae007d0e02c03c72204a5c169736461e946a166eab
```

and obtains

```text
attachment states                    12,870
root-level phase-labelled turns          912
labelled state arcs                    7,296
zero-out / zero-in roots             761 / 848
zero-out / zero-in states          7,329 / 12,010
packet-support maximum matching          530
packet loops                               0
```

The factor-eight identity is exact: each geometric root turn admits the
eight old terminal attachments different from its entering coordinate.
The 912 turns are fewer than the 1,430 roots, already forcing a zero row.
The named smallest cut is root 0,

```text
Q=255, type=8, (C0,C1,C2)=(159,64,32).
```

All of its nine attachment states have zero outdegree.  Equivalently, the
tail set consisting of the selected state at root 0 has empty neighborhood
under every possible owner transversal.  This is a solver-free singleton
Hall certificate for the frozen table.  Running a generic CNF search cannot
repair it; one must first alter the static rooted partitions while retaining
their exact lower flag tower, then regenerate the same 72-candidate
catalogue.

The independent artifacts are

```text
scratch/build_k17_rooted_flag_attachment_cycle_20260801.cpp
  SHA256 0c51a28c4c7ab3766d828d40031381272631eda5d1cd64bb70cac25b8f69ed59
scratch/audit_threadA_k17_rank8_rooted_nine_attachment_transition_20260801.cpp
  SHA256 0db4dcefb7fd65f48e4a8aaf39ffb10cd538a337a396bd150957bf28ea813c66
scratch/threadA_k17_rank8_rooted_nine_attachment_transition_20260801/independent.audit.json
  SHA256 167fd9a1955ec5d7e1a6c563d86734f3e3d9495d212112988fb2e5e58659eb65
```

## 8. Fail-closed implementation checklist

A positive CNF artifact is sound only if an independent replay checks all
of the following.

1. exactly 12,870 aligned attachment states, with parallel states retained;
2. the two exact-one rows (1.5);
3. every arc's complete source state, complete rotated target state,
   entering coordinate, owner equality (2.2), and all three inclusions
   (3.2);
4. both equalities in (4.1), with every selected arc tied to its exact two
   state IDs;
5. one stored phase/voltage label for every materialized arc (or an explicit
   second-stage choice among stored parallel labels);
6. the quotient component decomposition and voltage of each component; and
7. direct 17-phase physical replay of all 24,310 owners, all lower target
   rows, and every literal recurrence.

Under these checks, the proposed model is exactly the fixed-static-factor
specialization of OFHT.  The principal finite obstruction is then ordinary
selected-state Hall deficiency.  If the CNF is infeasible, that verdict is
scoped to this frozen static flag factor and its complete attachment/arc
catalogue; it is not a no-go for OFHT after changing the static factor.
