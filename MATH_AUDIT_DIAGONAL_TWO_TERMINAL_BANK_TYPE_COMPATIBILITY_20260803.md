# Audit of the diagonal two-terminal banks and the canonical cross-ray type

**Date:** 2026-08-03  
**Status:** line-by-line pure-mathematical audit and scope correction.  The
native q1/q2 and first-exit interval banks are valid.  They solve a raw
two-address supply problem for a nested upper Hasse type; they do **not**
instantiate the canonical folded-C8/two-cross-ray terminal tickets without
a new type-preserving conversion theorem.

## 0. Verdict

The two audited constructions prove real occurrence geometry.

1. Under the stated q2 rank-one hypothesis, every seam has the literal
   chain

   \[
              P_i\subset T_i\subset R_i\subset U_i,
   \]

   with four distinct interval addresses and two terminal addresses
   `(q_i,u_i)`.
2. On a sufficiently long simple cyclic Johnson row, every immediate upper
   `R_i` has a first exit at distance at most `r+1`.  Its plateau-end and
   first-exit addresses `(w_i,v_i)` are distinct, and their values form the
   Hasse pair `R_i subset V_i`, `|V_i-R_i|=1`.
3. Under the respective short-interval hypotheses, the `W` bundles are
   pairwise disjoint as **interval occurrences**.  Thus a complete state
   which independently declares these nested-upper pairs to be legal
   tickets really does have a deterministic rank-`W` two-coordinate bank.

However, the canonical terminal objects in the zero-block and folded-C8
theorems have a different invariant type.  A canonical antidiagonal ticket
is a pair of separately addressed prefix/suffix ray occurrences, normally
in opposite phases, with incomparable values whose intersection is a fixed
core and whose union is a fixed cap.  The new banks are same-phase nested
upper intervals differing by one element.  Therefore:

\[
 \boxed{
 \text{the new theorems provide candidate two-cell banks, not a canonical
 two-cross-ray lifting.}}
\]

They remove the scalar/address objection "there is only one native
`W`-bank".  They do not remove terminal membership, paired-type,
background, or all-cut linkage obligations.

## 1. Audit of the fixed q1/q2 ladder

Assume

\[
 T_i=\bigcup_{h=i}^{i+d}A_h,qquad
 P_i=\bigcup_{h=i+1}^{i+d}A_h=T_i\cap T_{i+1},
\]

with ranks `r` and `r-1`.  Then

\[
 P_i\cup A_i=T_i,qquad
 P_i\cup A_{i+d+1}=T_{i+1}.
\]

Since consecutive owners are distinct rank-`r` sets with rank-`r-1`
intersection,

\[
 R_i=T_i\cup T_{i+1}
\]

has rank `r+1`.  The further assumption

\[
 U_i=R_i\cup A_{i+d+2},qquad |U_i|=r+2,
\]

is exactly one additional Boolean cover.  The two displayed phase chains
follow by adding the left and right source endpoints in the asserted order.
No distributive-law shortcut is being used: the equality defining `P_i` is
an explicit hypothesis.

The addresses have lengths `d,d+1,d+2,d+3`.  Since `d<W-3`, all are proper
oriented cyclic intervals, their start and length determine them uniquely,
and no two address families collide.  Thus the address-disjointness proof is
correct.  It prices interval occurrences, not their constituent singleton
source positions; the theorem says this explicitly.

The conditional rank assertion is also correct in its proper scope.  If a
fixed cap state treats the entire record

\[
                       (p_i,o_i,q_i,u_i)
\]

as one legal conjunctive route and all other shared resources have already
been resolved, the single representatives are mutually disjoint and have
rank `W`.  This is a new deterministic bundle system.  It is not, merely by
that construction, the canonical cross-ray Rado system.

## 2. Audit of the first-exit bank

The original statement omitted the hypothesis needed to prove that the
first exit exists for an arbitrary simple cyclic subrow.  A row consisting
of all `r+1` facets of one `(r+1)`-set can remain inside that top forever.
The theorem has therefore been patched to assume

\[
                              W>r+1.                         \tag{2.1}
\]

This is automatic under its later hypothesis `d+r+2<W` and in the intended
complete middle layer.

Under (2.1), only `r+1` distinct rank-`r` owners lie below `R_i`, while the
cyclic row has more owners.  Hence a forward exit exists.  The first two
owners lie below `R_i`, and at most `r+1` consecutive distinct owners can do
so, giving

\[
                              2\le h_i\le r+1.
\]

The last inside owner and the first outside owner are Johnson adjacent.
Exactly one coordinate is inserted, and it must lie outside `R_i`; hence

\[
 |R_i\cup T_{i+h_i}|=r+2.
\]

The interval-union identity

\[
 \bigcup_{j=0}^{h}T_{i+j}
 =\bigcup_{t=i}^{i+d+h}A_t
\]

then proves the plateau and first-exit values.  Under `d+r+2<W`, every
address is a proper oriented cyclic interval.  Starts distinguish indices,
and the one-unit length difference distinguishes `w_i` from `v_i`, so the
two `W`-banks are indeed disjoint.

Thus the corrected occurrence theorem is valid.  The phrase "first exit"
does not itself supply a cross-ray ticket: it supplies the nested pair

\[
                         R_i\subset V_i,qquad |V_i-R_i|=1.
\]

## 3. Exact incompatibility with the canonical folded-C8 type

Suppress the fixed active labels in the folded-C8 notation and put

\[
 C_3=K\cup\{z,a_3\},qquad C_1=K\cup\{z,a_1\}.
\]

For `1<=j<d`, the two canonical antidiagonals use value pairs

\[
 \begin{aligned}
  &(C_3\cup F[1,j],\ C_3\cup F[j+1,d]),\\
  &(C_1\cup F[1,j],\ C_1\cup F[j+1,d]).
 \end{aligned}                                           \tag{3.1}
\]

Each pair has the exact invariants

\[
 \begin{aligned}
  X\cap Y&=C_e,\\
  X\cup Y&=C_e\cup F[1,d],\\
  |X\mathbin\triangle Y|&=d,
 \end{aligned}                                           \tag{3.2}
\]

and both differences are nonempty.  The values are incomparable.  The two
physical cells are adjacent disjoint prefix/suffix intervals and normally
belong to opposite phase words.

Both diagonal constructions instead have

\[
 X\subset Y,qquad |Y-X|=1,qquad |X\mathbin\triangle Y|=1, \tag{3.3}
\]

and use nested intervals in one phase word.  For `d>=2`, (3.2) and (3.3)
cannot be related by a map preserving Boolean meet/join, containment,
phase, ray role, or interval incidence.  This is a type obstruction, not a
counting obstruction.

A new terminal theory is free to declare `(R_i,U_i)` or `(R_i,V_i)` an
accepted dual-role type.  Alternatively a physical conversion gadget could
translate the canonical cross ticket into this nested-upper ticket.  What
is invalid is inferring either declaration from the existence of two
addresses.

## 4. Comparison with the common-cap Rado/gammoid theorem

In
`MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md`,
the index `p in {0,1}` denotes the two required physical occurrence
coordinates in the union of the canonical cross matchings.  It does not
denote q1 versus q2 upper width.  Each port record retains ray, role,
physical address, flag, endpoint, guard, and terminal type.  Each Rado
representative is a complete canonical route, and the paired relation
`K_i^c` must retain the two-coordinate correlation.

Consequently the new deterministic pairs prove a common rank `W` only
after all of the following are established in one state `c`:

1. each nested-upper bundle belongs to the intended complete typed menus;
2. its two occurrences form a legal pair in `K_i^c`;
3. every shared cross-system capacity has already been allocated;
4. frozen or adaptively contracted background routes coexist with every
   selected bundle; and
5. terminal interchange is legal for this complete occurrence type.

Items 1--2 fail for the unmodified canonical folded-C8 type by Section 3.
Items 3--5 are explicitly outside both diagonal occurrence theorems.  Thus
the Rado/gammoid all-subset/all-cut requirement is not discharged.

The deterministic bank is nevertheless useful: if a future theorem proves
the new type and state, it automatically supplies product closure and
removes the need to intersect two marginal matroids for those particular
bundles.  The residual logical-ticket problem then becomes one Hall graph
between tickets and accepted seam bundles.

## 5. Comparison with zero-block collapse

The zero-block theorem says the abstract canonical birail defect is exactly
the number of zero--zero pairs, and zero defect is equivalent to two cross
perfect matchings.  Its addressed audit stresses that one cross edge is a
paired **two-cell** ticket; it may not be collapsed to one cell.

The diagonal theorems meet only that numerical two-cell requirement.  They
provide two native cells per seam.  They do not identify those cells with
the four canonical shores `L_0,L_+,R_0,R_+`, do not prove either canonical
cross matching, and do not transport the prefix/suffix target values in
(3.1).  Therefore they do not make the zero-block Hall theorem applicable
to the canonical tickets.

Conversely, the zero-block theorem does not forbid a nested-upper terminal
architecture.  It simply supplies no acceptance theorem for it.

## 6. Patched claims and exact remaining theorem

The two diagonal theorem files were patched as follows.

1. Their status now says they close the raw interval-address count for a
   nested-upper type, not the canonical cross-ray gate.
2. The q1/q2 rank-`W` statement is explicitly scoped to a newly accepted
   nested-upper bundle system.
3. The first-exit theorem now includes `W>r+1`, the missing hypothesis for
   existence on an arbitrary simple cyclic row.
4. Both files record the exact type mismatch (3.2)--(3.3).

The proof-safe next theorem is

> **Nested-upper terminal conversion theorem.**  In one complete
> cap/background state, convert every required canonical cross-ray ticket
> to an accepted q1/q2 or first-exit nested-upper bundle while preserving
> ticket label, both physical roles, phase/endpoint semantics, all guards,
> and every shared capacity; or construct the regeneration directly with
> the nested-upper ticket as its native logical type.

Without that theorem, the two diagonal banks are candidate capacity, not a
completed terminal router.

## 7. Frozen file hashes

After the scope corrections, the audited files have SHA-256 values

```text
dbd2f671d07e1e4c09ecadbbade9e9ea0a55e1dfca4054ead15fd09fbe8a7151
  MATH_THEOREM_DIAGONAL_Q1_Q2_TWO_COORDINATE_UPPER_LADDER_ROUTER_20260803.md
25dc0c20f14254a9f9419caa41912c5fdc480f6fb3178e20822a6e6cd8a89ab0
  MATH_THEOREM_DIAGONAL_FIRST_EXIT_SECOND_TERMINAL_BANK_20260803.md
108c4b0ad2adc99d9e9c91df9f1bfdb9f816494670f7473c51e7751f134177cc
  MATH_THEOREM_TERMINAL_COMMON_CAP_TWO_CROSS_RAY_RADO_GAMMOID_V2_20260803.md
7090a0622a03af5cab9944803d8d3dd8880f820cad9cfccee8dd32c21a58cba2
  MATH_THEOREM_ZERO_BLOCK_BIRAIL_COLLAPSE_AND_C8_CROSSMATCH_GATE_20260801.md
ccc29b2ae8a5f4036d2a707a84091f0c08b669a378a441fd4e5d3f4da50d88d5
  MATH_AUDIT_ZERO_BLOCK_BIRAIL_CROSSMATCH_AND_ADDRESSED_TRANSPORT_SCOPE_20260801.md
```
