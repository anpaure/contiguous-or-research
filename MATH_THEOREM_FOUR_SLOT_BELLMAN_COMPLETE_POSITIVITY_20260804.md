# Complete positivity of four-slot Bellman clocks

**Date:** 2026-08-04  
**Status:** unconditional pure-mathematical corollary of the independently
audited branch theorems listed below.  It proves the finite Bellman
inequality for every table with at most four active slots.  It does not prove
the all-slot Bellman inequality or `nu(k) <= B(k) + O(1)`.

Put

\[
 A={\sqrt\pi\over2},
\]

and let `K` be the Rayleigh signed-tail kernel used in the smooth
configuration dual.  Let

\[
 0=c_0\le c_1\le\cdots\le c_n,
 \qquad c_{i+j}\ge c_i+c_j\quad(i+j\le n),
 \qquad c_n\ge A,
\]

where `n <= 4`, and define

\[
 V_0=0,
 \qquad
 V_m=\max_{1\le j\le\min(m,n)}(c_j+V_{m-j}).
\]

## Theorem

Every such table satisfies

\[
                         \boxed{\sum_{m\ge0}K(V_m)>0.}
\]

Consequently, if a finite internally superadditive Bellman table has
nonpositive functional, then its grid size is at least five.

## Proof

The cases `n <= 3` are the previously proved one-, two-, and three-slot
theorems.  It remains to take `n=4` and write

\[
 (c_0,c_1,c_2,c_3,c_4)=(0,x,y,z,T).
\]

Internal superadditivity gives `x <= y/2`.  Hence at least one of

\[
                         {y\over2},\qquad {z\over3},\qquad {T\over4}
\]

has maximal generator efficiency.  The efficiency-normal-form theorem
therefore covers all four-slot tables by the three branches below; the
branches overlap harmlessly at ties.

1. If `y/2` is maximal, the exact clock is a two-coset tail plus one finite
   transient.  The complete two-efficient theorem proves its functional
   strictly positive.

2. If `z/3` is maximal, the exact clock is an effective three-coset tail
   with every transient retained.  Its two faces are `w=y` and `w=2u`.
   On `w=y`, strict period monotonicity reduces the subcritical domain to
   `P+u=A` and `P+u=2y`; both boundary theorems prove positivity.  The
   independently audited `w=2u` theorem proves positivity on the other
   face.  First-crossing deletion covers the normalized endpoint range.

3. If `T/4` is maximal, the exact clock is a four-state Apéry tail with a
   literal finite head through capacity eight.  The threshold-face theorem
   and the scalar-gate theorem prove the entire branch strictly positive.

These branches exhaust all possibilities, so the four-slot functional is
strictly positive.  Together with the `n <= 3` results this proves the
theorem. \(\square\)

## Proof dependencies and frozen hashes

| role | file | SHA-256 |
|---|---|---|
| efficiency partition | `MATH_THEOREM_FOUR_SLOT_BELLMAN_EFFICIENCY_NORMAL_FORMS_20260804.md` | `2bc644a1fdfef612ed9a0181326a5da25ce3e4952ed4f001c06875aec09dbb5d` |
| two-efficient closure | `MATH_THEOREM_FOUR_SLOT_TWO_EFFICIENT_NORMALIZED_SUBRANGE_AND_PULSE_GATE_20260804.md` | `47819d25abf75877b6bc723ed593354bb0e76582635996227ac9c48812b986c8` |
| independent two-efficient audit | `MATH_AUDIT_FOUR_SLOT_TWO_EFFICIENT_FULL_INDEPENDENT_20260804.md` | `20dcdbb21cd71ed2bacd6c637ff59ee23ffa2dec6ed1da61cf42f05af07d2fbb` |
| three-efficient reduction | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_PULSE_NORMAL_FORMS_20260804.md` | `0b46d0b2e073cc9eab4171198e2b4686ce08ef055887fd3f72cd0a506cdfef35` |
| first `w=y` boundary | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_20260804.md` | `7e1a12d5cce9a16b6fd9a1b65d7d9d625d114c5b8810fa7f2d6baf95bfed722b` |
| independent first-boundary audit | `MATH_AUDIT_FOUR_SLOT_THREE_EFFICIENT_THRESHOLD_SURFACE_CLOSURE_INDEPENDENT_20260804.md` | `090494f7180f211752635415294b4fd5f341cded2362de9c46aaf19eb6aea1c4` |
| second `w=y` boundary | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_20260804.md` | `6a44b458c013e3c553be3925f9439960b139262175aaf79bbb9fb50054f6c7d7` |
| independent second-boundary audit | `MATH_AUDIT_FOUR_SLOT_THREE_EFFICIENT_WY_SECOND_BOUNDARY_CLOSURE_INDEPENDENT_20260804.md` | `5db0e5ebe3b5ab3bab6fff6930fe6f7c406486a4853e0b80e7eeac5223396cd8` |
| `w=2u` closure | `MATH_THEOREM_FOUR_SLOT_THREE_EFFICIENT_W2U_PERIOD_BOUNDARY_CLOSURE_20260804.md` | `64451d508cc73c5ac5baf04bd749695358eea7fffb3d4c93a8c5eafa8c3bfae1` |
| independent `w=2u` audit | `MATH_AUDIT_FOUR_SLOT_THREE_EFFICIENT_W2U_PERIOD_BOUNDARY_CLOSURE_INDEPENDENT_20260804.md` | `c86adbe63511b8102bab86576893c3da9a6fd438ef3bd2430b0714ab885490c9` |
| four-efficient Apéry theorem | `MATH_THEOREM_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_20260804.md` | `8fc1405920daea3e597a105d04b9b63e42867a4db1cf9c9515f2a73cd6584cda` |
| independent Apéry normal-form audit | `MATH_AUDIT_FOUR_SLOT_APERY_EXACT_NORMAL_FORM_AND_THRESHOLD_FACE_INDEPENDENT_20260804.md` | `740996898d0961e09b65662de54f72bc281c49cce2b287225cddcec59654499c` |
| four-efficient scalar gate | `MATH_THEOREM_FOUR_SLOT_APERY_SCALAR_GATE_CLOSURE_20260804.md` | `2b334fc6670ec73d4eba0f9de7a211b5e64f38a77f205ee822bebc4f3a79e776` |
| independent scalar-gate audit | `MATH_AUDIT_FOUR_SLOT_APERY_SCALAR_GATE_CLOSURE_INDEPENDENT_20260804.md` | `4dc1f99d6626cd23130f08f56e9cc94d1458c5b253901636ee9e508d938b2bd5` |

The independent audit of the second `w=y` boundary explicitly rechecks the
exhaustion of all three maximal-efficiency branches and records the same
four-slot consequence.
