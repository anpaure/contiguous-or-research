# Many-run recency lifts and the exact protected-witness compiler

Date: 2026-09-09. Pure proof by `exact_b_induction`.

Status: exact finite state identities and necessary-and-sufficient
compatibility theorems. No mathematical execution or new word is claimed.
These results permit arbitrarily many marked and unmarked segments; they
do not propose a one- or two-seam19 construction. The unresolved issue is
constructing compatible trajectories at the exact B(k) budget uniformly
in k, rather than checking a supplied trajectory.

## 1. Relation to the existing MTF and Pascal results

The following sources were read before deriving this interface:

* `GLOBAL_MTF_SCD_HANDOFF.md` gives the exact recency update, the SCD-tour
  sufficient condition, and its charged W+k-1 initialization bound.
* `MTF_SCD_INDUCTION_INDEPENDENT_AUDIT.md`, Sections 3–5, proves the lower,
  upper, and singleton-new-coordinate lifts, closed-walk splicing, and
  the reset-cost recurrence. Its parity propagation does not establish
  an exact all-dimensional tour from a finite base.
* `MATH_THEOREM_GENERALIZED_PASCAL_BRAID_LINEAR_MODEL_20260729.md` gives
  exact middle-owner and adjacent-shadow equations. Residence and literal
  all-rank compilation remain additional conditions there.
* `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`
  records the Catalan shore mismatch and the unresolved regenerative
  factor/port/compiler requirements.
* `MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`
  and `MATH_THEOREM_AD_PASCAL_EVENT_STREAM_BRAID_AND_DUAL_GAP_20260729.md`
  track residence, event queues, and common-cap constraints; neither
  permits an uncharged reset or infers all-rank coverage from q1 counts.
* `FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Section 11, states the
  abstract tagged double-cover criterion.

The addition here is an explicit two-threshold state for an arbitrarily
interleaved new coordinate, followed by an exact elimination of all
marked-target witness choices for a fixed projected trajectory. The final
test protects one old witness per target and forbids those protected
positions from absorbing an entire marked-target support. It includes
all ranks, zero projections, literal nonemptiness, and total length.
It does not assert that an optimal protected family always exists.

## 2. Fixed projection and tag convention

Fix a finite sequence of old projections

    U_1,...,U_N,  U_i subseteq X.

Zero projections are allowed. Choose tags b_i in {0,1} and form physical
letters

    V_i=U_i union ({z} if b_i=1, otherwise empty).        (2.1)

Every zero projection must have b_i=1; otherwise the physical letter
would be empty. A universal word must have at least one zero projection,
since its singleton target {z} requires one literal {z}. This condition
also applies when starting from an initialized trajectory: its actual
initializing word and any singleton bridge must be included in (2.1)
and charged in N.

Let P_t be the ordered recency partition of the seen old coordinates
after U_1,...,U_t. It need not yet cover all of X. Its nonempty prefix
unions are exactly the distinct nonempty old suffix ORs at that endpoint.
An empty update leaves P_t unchanged; a nonempty update U prepends U,
removes its coordinates from the previous blocks, and discards empties.
Forgetting z commutes with these updates, so P_t is independent of the
tag choices.

## 3. Exact moving-cursor identity

Suppose at least one tag has appeared by time t, and let q<=t be its last
index. Define

    B_t=union_(j=q+1)^t U_j,
    C_t=union_(j=q)^t U_j=B_t union U_q.                 (3.1)

An empty union is zero. The exact suffix target deck of V at endpoint t
splits as follows:

    old targets:    D in Pref(P_t), D subseteq B_t;
    marked targets: D union {z}, D in Pref(P_t), C_t subseteq D;
    singleton {z}: present at this endpoint iff C_t=empty.       (3.2)

Before the first tag, all of Pref(P_t) is old and there is no marked
suffix target.

**Proof.** A suffix avoids z exactly when it starts after q. Its largest
possible union is B_t. If a current old suffix union D is strictly below
B_t, no witness for it can start at or before q, since such a suffix
contains C_t and hence B_t. If D=B_t, the suffix q+1,...,t witnesses it.
This proves the old half; when B_t=empty it has no nonempty target.

A suffix contains z exactly when it starts at or before q, so its old
projection contains C_t. Conversely, if a current suffix union D is
strictly above C_t, its witness cannot start after q, where the union is
at most B_t<=C_t. If D=C_t, the suffix q,...,t works. The empty projected
case is exactly C_t=empty. This proves (3.2). QED.

The cursor has an exact update with no state reset:

* On a marked update U, set (B,C)=(empty,U).
* On an unmarked update U, set (B,C)=(B union U,C union U).

In both cases update P by the ordinary old-coordinate recency rule.
These formulas include a marked zero update, which places z alone at
the front and exposes every existing old prefix with z.

Adjoin the empty prefix to the old prefix chain. At every reached state,
B and C are either the same member of this enlarged chain or consecutive
distinct members. If B=C, z is a singleton block
immediately after the old prefix B. If B is strictly below C, z is tied
with the old block C minus B. This can also be seen directly from last
occurrence times: all coordinates updated after q precede z, remaining
coordinates of U_q tie with it, and all older coordinates follow it.
Thus (P,B,C) determines the complete recency state including z.

## 4. Where simultaneous old/marked service is possible

At a fixed endpoint after z has appeared, an old target D and its marked
copy D union {z} are BOTH exposed if and only if

    B_t=C_t=D,  D nonempty.                              (4.1)

Indeed (3.2) requires C_t subseteq D subseteq B_t and B_t subseteq C_t.
There can be at most one such paired target at that endpoint. The condition
B_t=C_t is exactly U_q subseteq B_t: the old projection of the last
marked letter has been absorbed by later unmarked updates. Once this
happens, it persists throughout the rest of that unmarked run, though
the shared boundary target B_t may grow.

This is the literal mechanism for serving the two copies of one old
target at a single endpoint. It cannot be assumed merely because two
independent old chains cover that target. For example, the two-letter
projection (empty,{a}) with tags (1,0) gives physical word ({z},{a});
at the second endpoint it exposes both {a} and {a,z}. The singleton
bridge is a charged position, not a free initial state.

The lower/upper lifts in the older MTF notes are extreme cursor positions.
A marked nonempty update puts z in the first old block; after subsequent
unmarked updates have refreshed all old coordinates, B=C=X puts z in a
final singleton block. Intermediate cursor states are what permit many
segments without requiring a reset between every lower and upper run.

## 5. Exact segment compatibility

Suppose prescribed pieces give old recency trajectories, tag choices,
and initial/final cursor states. Two consecutive pieces concatenate with
no extra letter and retain their full promised suffix decks exactly when
the first piece's final augmented state (P,B,C), or absent-z state, is
the second piece's specified initial augmented state. Given this equality,
the deterministic update identities reproduce every later state and its
literal suffix witnesses. Conversely, a construction claiming those exact
states must satisfy it at the join.

This is a full-state compatibility condition; named-target coverage alone
can survive some unequal states and is not claimed equivalent to equality.
When compatible pieces cover every old and marked target through their
actual decks, their concatenated word is universal. Its length is the
literal initialization length plus the sum of all piece update lengths.
There is no extra join cost in this equality case. Any nonmatching join
requires an actual bridging word and its charged length; the criterion
does not supply that word for free.

## 6. Eliminate every marked-target witness choice

For each nonempty D subseteq X, let I_D be the family of all ordinary
intervals of positions whose projected OR is D. Define its full position
support

    H_D=union_{I in I_D} I.                              (6.1)

Let T={i:b_i=1} be the marked positions. Then the marked copy of D is
covered if and only if

    T intersect H_D is nonempty.                        (6.2)

Necessity follows from a marked witness containing some tagged position.
For sufficiency, if a tagged position belongs to H_D, one of its defining
intervals has projected OR D and contains z, so its physical OR is D+z.
All other tags in that interval add the same coordinate z and are harmless.

The support H_D can be described without enumerating witness intervals.
Consider the maximal consecutive runs all of whose projections U_i are
subsets of D. Keep precisely those runs whose total OR is D. Their union
is H_D: every D-witness is contained in one such run, and each kept whole
run itself witnesses D and contains every one of its positions.

The old target D, in contrast, requires one entire interval in I_D to
avoid T. This asymmetric simplification is important: independent choices
of a lower and upper target witness are not needed once H_D is known.

## 7. Complete protected-witness compiler

One may additionally specify fixed unmarked positions Z_0 and fixed
marked positions Z_1, disjoint. Let Z_empty={i:U_i=empty}; these positions
are necessarily marked. Assume Z_empty is nonempty, as required for {z}.

**Theorem.** Tags respecting those fixed choices make (2.1) a nonempty
universal word if and only if one can choose a projected witness interval
J_D in I_D for every nonempty D such that, on putting

    F=Z_0 union union_D J_D,

the following conditions hold:

    F intersect (Z_1 union Z_empty)=empty;
    H_D minus F is nonempty for every nonempty D.        (7.1)

On success an explicit valid choice is

    b_i=0 for i in F, and b_i=1 for every i outside F.    (7.2)

**Proof.** Given a successful tagging, choose one old witness J_D for
each target. Their union with Z_0 is contained in the unmarked positions,
so it avoids Z_1 and all zero projections. Every marked D-witness meets
T, so H_D has a position outside this F. Thus (7.1) is necessary.

Conversely, choose (7.2). Every J_D remains an entirely unmarked literal
witness, and it contains no zero projection by the first condition.
Every position outside F is a nonempty marked physical letter, including
all prescribed marked positions. By the second condition and (6.2), every
marked target D+z is covered. A zero-projection position lies outside F
and witnesses {z}. All fixed choices hold. This constructs a universal
word of EXACT length N. QED.

Thus, for a fixed projected trajectory, the complete remaining choice is
one family of protected old intervals whose union does not exhaust ANY
marked-target support. Marking every other position is a valid maximal
completion; it does not require a separate compatibility choice for each
upper witness. This reduction includes an initialized old word by placing
all its positions in Z_0, with its literal length still included in N.

This is an exact finite constructive condition, not a claim that the
protected family can be selected by an ordinary matching or flow. The
union constraints couple the choices for different targets.

## 8. A precise naive-lift obstruction and the surviving gate

If a projected target D has just one interval witness J, then H_D=J.
Protecting an old D-witness forces all of H_D into F and violates (7.1).
Thus NO tagging of that fixed projection can cover both D and D+z.
One cannot take a uniquely witnessing old word, choose arbitrary tags,
and assume that its two copies are automatically supplied.

The stronger fixed-unmarked-trace obstruction for the checked18 word is
proved separately in
`scratch/EXACT_INTERLEAVED_LIFT_RUN_START_BUDGET_AND_FIXED_TRACE_CUT_CORES_20260909.md`.
Its unique rank-nine endpoints forbid every internal marked insertion,
once the stated literal premises are checked. That result concerns a
different restriction: the complete unmarked subsequence is fixed. In
the present compiler the projected trajectory itself may be redesigned,
including necessary zero slots and redundant target occurrences, but
every added position is paid in N.

The existing entrance/exit theorem also requires at least 541 transitions
of each type per coordinate for an exact19 word, and the new joint run
budget constrains the ranks at those run starts. Consequently, neither
few-segment recoding nor simply increasing the number of cuts in the
rigid18 trace is a viable exact19 induction step.

The surviving general route is concrete: construct a new projected
trajectory of the required total length, with compatible recency cursors
and a protected witness family satisfying (7.1) at all ranks. Equations
(3.2) and (7.1) allow every proposed step to be checked and literally
compiled. Existence of such a family at B(k+1) uniformly in k is still
the missing constructive theorem; it is not supplied by the present
equivalences or by the earlier Pascal middle-layer counts.

Independent internal review: `exact_equality_structure` read Sections 3
and 6–7 in full and reported PASS on 2026-09-09. Its sole wording
correction, explicitly adjoining the empty prefix in the cursor-position
description, is incorporated above. No external or proof-assistant
certification is claimed.
