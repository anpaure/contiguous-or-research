# Full rigid-orbit fan support already gives an owner-path occurrence SDR

**Date:** 2026-08-05  
**Method:** exact-value occurrence separation, transported q1-section
accounting, and sliding-window source identities; no computation or search  
**Status:** unconditional at the owner-factor level for `m>=4`, and
conditional only on the existence of a stated terminal antecedent for the
source-level upper lift.  The complete rigid-rotation fan-support theorem
has no remaining target-to-owner-path Hall obstruction.  The unresolved
capacity is the lower source compiler and its typed common-cap routes, not
the choice of owner intervals.

## 1. Input support theorem

Let `F^+` be the terminal two-factor obtained by the full coordinate orbit
of the canonical rigid clean `C6` on `n=2m+1` coordinates.  The exact braid,
residual-block, and residual-seam calculations prove:

* every named strict-lower whole-fan target `S` has a consecutive owner
  interval `I` in `F^+` with

  \[
                         \operatorname{int}(I)=S;             \tag{1.1}
  \]

* the replacement has the same q1-row width as the old named corridor; and
* on the complemented owner factor, `bar I` has

  \[
                         \operatorname{uni}(\overline I)
                           =[n]\setminus S.                    \tag{1.2}
  \]

The construction is exhaustive: the old single-soliton fans move to the
alternating braid, two-soliton corridors avoiding `E_1` remain inside one
literal residual block, and every remaining `E_1` inverse-fan target moves
to a braid segment or a residual seam.

## 2. Exact-value support implies an occurrence SDR

The following elementary observation is the relevant capacity theorem.

### Lemma 2.1 (value fibres separate distinct tasks)

Let `cal I` be any family of physical interval occurrences and let

\[
                         v:{\cal I}\longrightarrow{\cal T}    \tag{2.1}
\]

be their literal value map.  If every target `T in cal T_0` has a nonempty
fibre `v^(-1)(T)`, then arbitrary choices

\[
                         b(T)\in v^{-1}(T)                     \tag{2.2}
\]

form an injection `b:cal T_0 -> cal I`.

#### Proof

If `b(T)=b(T')`, applying the single-valued map `v` gives `T=T'`.
`square`

There is no Hall condition hidden here.  Two distinct exact set values
cannot be carried by the same physical interval occurrence.

### Theorem 2.2 (rigid-orbit owner-path SDR)

The terminal factor `F^+` has an occurrence-injective bank containing:

1. one owner-path intersection occurrence for every named strict-lower
   whole-fan target; and
2. one complemented owner-path union occurrence for every paired proper
   upper target.

The bank may be chosen width-preservingly.  Distinct bank paths may share
owners or q1 edges without creating a capacity conflict.

#### Proof

Apply Lemma 2.1 to the nonempty replacement fibres supplied by (1.1), and
then to (1.2).  The depth is determined by target rank:

\[
 |S|=m-q,
 \qquad
 |[n]\setminus S|=m+1+q.                         \tag{2.3}
\]

Hence two different depth types cannot be attached to the same literal
target in this named bank.  The empty lower target is not an obligation;
the full upper target is chosen once from any displayed width-`m`
replacement.

Overlapping witness intervals do not add graph edges.  They are subpaths
of the already fixed degree-two factor, and an edge may belong to many
different interval occurrences.  Capacity one applies to the complete
interval address, not separately to every internal edge.  `square`

This removes the phrase “occurrence-capacitated reassignment” from the list
of open gates **at the owner-path level**.

## 3. Owner and q1 capacity are already exact

Write rotated objects as `X(t)=rho^tX`.  The full rethread replaces

\[
 E_i(t):P_i(t)\longrightarrow Q_i(t)
\]

by

\[
 N_i(t):P_i(t)\longrightarrow Q_{i+1}(t).
\]

The old occurrence carrying row `R_i(t)` is `E_i(t)`.  The new occurrence
carrying exactly the same row is

\[
                         N_{i-1}(t),                              \tag{3.1}
\]

with the port index read modulo three.  Thus

\[
                         E_i(t)\longmapsto N_{i-1}(t)             \tag{3.2}
\]

is a bijection on the `3n` changed selected q1 occurrences.  Every
unchanged section occurrence is fixed.

### Proposition 3.1

The full rigid-orbit rethread preserves:

1. owner degree two and graph simplicity;
2. exactly one selected occurrence of every q1 row; and
3. all owner-path witness capacity required by Theorem 2.2.

#### Proof

Degree two and simplicity hold after every step of the authenticated
descending serial order, hence in the terminal factor.  Equation (3.2)
replaces the unique old selected occurrence of each changed row by one new
occurrence of that same row.  No new edge duplicates an old or new edge by
the terminal simplicity theorem.  Finally, selecting subpaths of this
factor does not change its degrees. `square`

Thus the complete target-support result and the immediate owner/q1
capacity result are already compatible; they do not require a second
matching.

## 4. Conditional lift of the upper bank to literal source intervals

There is also no new untyped occurrence matching once a terminal
antecedent has been fixed.

Let one cyclic component of the **actual upper-owner chronology** be

\[
                         V_i=\bigcup_{h=0}^{d}A_{i+h},            \tag{4.1}
\]

where `A` is a cyclic source word.  For a `q`-edge owner interval

\[
                         I=(V_i,V_{i+1},\ldots,V_{i+q}),         \tag{4.2}
\]

define

\[
                         \Psi(I)=(A_i,A_{i+1},\ldots,A_{i+d+q}). \tag{4.3}
\]

### Theorem 4.1 (upper source-cell lift)

For every interval (4.2),

\[
                         \operatorname{OR}(\Psi(I))
                           =\bigcup_{j=0}^{q}V_{i+j}.             \tag{4.4}
\]

If all used widths are shorter than the source-component period, `Psi` is
injective on physical owner-interval addresses.  Consequently the complete
owner-path upper SDR of Theorem 2.2 lifts to a complete occurrence-injective
source-interval upper bank on every terminal component for which an
antecedent (4.1) exists.

#### Proof

The union of the sliding windows in (4.2) is exactly the union of source
letters with indices from `i` through `i+d+q`, which proves (4.4).  The
source interval records the same start `i`, and its width `d+q+1`
determines `q`.  Therefore equal source addresses imply equal owner-path
addresses.  Apply Theorem 2.2. `square`

For the alternating braid component, exact biresidence already supplies
such a cyclic antecedent for every deadline `d<=m-2`.  The corresponding
statement for every residual component, and the compatibility of their
linear joins, remain separate.

## 5. Why this does not yet give the lower compiler

An owner-path intersection occurrence is not automatically a literal
source-OR cell for the same lower target.  Under a strong row identity and
for `q<=d`, one may have

\[
 \bigcap_{j=0}^{q}V_{i+j}
      =\bigcup_{h=q}^{d}A_{i+h},                              \tag{5.1}
\]

which would send the path to the short source cell
`(A_(i+q),...,A_(i+d))`.  But (5.1) is an additional coordinate-history
condition, not a consequence of target support.  Moreover the strict-lower
compiler assigns all lower ranks jointly and is not confined to the direct
rows `q<=d`.

For the full rigid rotation rail, the exact generalized-screen payload
equation is unsatisfiable.  Hence the old common-history compiler matching
cannot simply be stamped on every moving packet and declared transported.
A fresh terminal lower matching, or a different compound source lift, is
still required.

## 6. Typed common-cap capacity remains genuinely open

Even distinct valid source cells need not have disjoint typed routes to a
shared common cap.  For example, two cells can carry two different target
values while both have only one common unit-capacity suffix sink.  The
owner-path SDR is then perfect but the typed route system has deficiency
one.

Therefore target support plus Lemma 2.1 does not imply the required
occurrence-labelled common-cap assignment.  After a terminal antecedent and
all phase pins are fixed, the remaining exact condition is the corresponding
matching/gammoid all-cut inequality on the literal cell-to-sink incidence
graph.  Occurrence types, phase flags, structural zeros, and shared suffix
capacities must be included before applying Hall or Rado.

## 7. Quantifier audit of the polynomial-leave reduction

The linear-cut leave theorem is valid with the following quantifiers kept
explicit.

1. The named one-corridor-per-target bank is fixed before the cut set.
2. `E_0` is the complete set of old factor edges deleted by the rethread;
   any additional deletion must be included in `E_0`.
3. The inverse-fan union bound does not require the punctures to be
   disjoint; overlap only lowers the number of distinct casualties.
4. The full rigid orbit is a genuine serial rethread, so its `3n` old-edge
   set satisfies item 2.
5. The later braid/block/seam theorem repairs a superset of the actually
   named casualties.  Restricting back to one task per target value and
   applying Lemma 2.1 is therefore legitimate.

No target-support or owner-path occurrence quantifier remains unresolved.

## 8. Exact remaining gate

After the full support closure, the proof obligations are:

1. produce compatible cyclic antecedents for the residual components and
   join/open the `1+gcd(n,3)` components at bounded literal charge;
2. build one fresh occurrence-labelled strict-lower compiler on the
   terminal source word (or a compound transport not ruled out by the
   rigid-rail payload obstruction); and
3. route that compiler through the typed shared common cap with bounded
   deficiency.

The upper bank itself requires no further target-to-occurrence matching
once item 1 supplies the antecedents: Theorem 4.1 lifts its already exact
owner-path SDR.

## 9. Dependencies and scope

The support input is

`MATH_THEOREM_PBBS_RIGID_ROTATION_E1_FAN_COMPLETE_SUPPORT_REPAIR_20260805.md`.

The exact serial degree/q1 transport is

`MATH_THEOREM_PBBS_RIGID_C6_SERIAL_ROTATION_ORBIT_TOPOLOGY_NOGO_20260805.md`.

The polynomial leave and private-prefix separation are

`MATH_THEOREM_PBBS_LINEAR_CUT_ORBIT_POLYNOMIAL_WHOLE_FAN_LEAVE_20260805.md`.

The full-rail source obstruction is

`MATH_THEOREM_PBBS_RIGID_ROTATION_RAIL_GENERALIZED_SCREEN_PAYLOAD_NOGO_20260805.md`.

This note does not prove residual biresidence, a bounded-charge component
splice/opening, a terminal lower compiler, or typed common-cap routing.  It
does prove that none of those missing statements is an owner-path support or
owner/q1 occurrence-capacity problem.
