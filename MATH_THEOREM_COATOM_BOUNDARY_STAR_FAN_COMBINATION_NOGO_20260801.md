# Boundary coatom transport is exact, but one star fan cannot self-repay the opposite chain

Date: 2026-08-01  
Lane: one-cell seam plus prepared coatom-chain compiler  
Status: exact combined verdict.  The boundary transporter gives zero
one-packet deep return deficiency, but the proposed one-cell self-repayment
and the claimed extra typed credit are false.  The smallest obstruction is
`d=2`.

## 0. Verdict

The following part of the proposed package is true.

* Two prepared global coatom endpoint traces give literal phase-switched
  cells for all `2(d-1)` deep packet-chain targets.
* Combining those boundary cells with the packet's native cells covers all
  OLD and NEW deep targets in either terminal phase under one actual
  antecedent.

The attempted one-cell strengthening is false in its local form.

1. If the two fans of the inserted source are assigned the two canonical
   coatom chains, the `d-1` destroyed crossing values are forced.  They are
   not any of the distinct opposite-phase chain targets.
2. With a typed target assigned to the shared singleton fan, the seam has
   only `d-1` unused-address credit after the displacement ledger, not `d`
   unused addresses in addition to the socket.
3. The star payload cannot be an arbitrary phase base.  It must lie in the
   intersection of both fan bases and must contain every coordinate for
   which the star is the unique carrier source.

Thus a valid simple flat seam must use the incomparable coatom crossing
normal form and route its displaced targets through an exterior augmenting
return.  The exact remaining object is still an open exterior ear; it is
not manufactured by fan cardinality.

## 1. The positive boundary part

Let

\[
 B^-=J\cup\{a\},\qquad B^+=J\cup\{b\},
 \qquad G=\{g_1,\ldots,g_d\},                              \tag{1.1}
\]

with all displayed parts disjoint.  The boundary-carving theorem gives, in
the terminal phase, the two chains

\[
 B^-\cup\{g_1,\ldots,g_h\},\qquad
 B^+\cup\{g_{d-h+1},\ldots,g_d\},
 \qquad1\le h\le d-1,                                     \tag{1.2}
\]

and swaps `a,b` in the other phase.  It constructs the complete antecedent,
not only marginal caps, and proves `D^dA=T`.  Orienting its two shores
opposite to the packet's native shores gives the exact local matching

\[
\begin{array}{c|cc}
 &\text{packet-native bank}&\text{global boundary bank}\\ \hline
 0&\text{OLD chains}&\text{NEW chains}\\
 1&\text{NEW chains}&\text{OLD chains}.
\end{array}                                                 \tag{1.3}
\]

So item (i) is valid, conditional on the prepared endpoint owners.  It does
not require the one-cell seam.

## 2. Exact failure of lost-crossing self-repayment

Insert one source `*` at an internal cut and put `A_*=Z`.  Let `L_h,R_h`
be its two fan values and `C_i`, `1<=i<=d-1`, the values of the old
length-`d` crossing cells destroyed by the insertion.  The exact seam
identity is

\[
                  Z\cup C_i=L_{i+1}\cup R_{d-i+1}.            \tag{2.1}
\]

To make the fans, excluding their common singleton, equal the two chains
in (1.2), their inclusion order is forced:

\[
\begin{aligned}
 L_{h+1}&=Z\cup\{b\}\cup\{g_1,\ldots,g_h\},\\
 R_{h+1}&=Z\cup\{a\}\cup\{g_{d-h+1},\ldots,g_d\}.
\end{aligned}                                               \tag{2.2}
\]

Here necessarily `Z subseteq J`; the common singleton belongs to every
target on both shores.  Substituting complementary levels into (2.1) gives

\[
 \boxed{Z\cup C_i=Z\cup\{a,b\}\cup G
             \quad(1\le i\le d-1).}                           \tag{2.3}
\]

Every opposite-phase deep chain target is a proper subset of the right side
of (2.3) outside `Z`: it omits one of `a,b` and at least one member of `G`.
The star-hidden criterion says that coordinates outside `Z` have no further
freedom.  Therefore

\[
 C_i\ne S
 \quad\text{for every opposite-phase deep chain target }S.   \tag{2.4}
\]

This refutes item (ii) in the proposed local assignment.

### Smallest counterexample

At `d=2`, use

\[
 A_{-1}=\{b,g_1\},\qquad A_0=\{z\},\qquad
 A_1=\{a,g_2\}.                                             \tag{2.5}
\]

The two non-singleton fans are

\[
 \{z,b,g_1\},\qquad\{z,a,g_2\},                             \tag{2.6}
\]

while the unique destroyed crossing cell is

\[
                         C_1=\{a,b,g_1,g_2\}.                 \tag{2.7}
\]

Neither opposite-phase chain target equals (2.7).  Copying `z` to a side
source only adds `z` to (2.7) and still does not repair the mismatch.  Thus
the obstruction begins at the first depth having a destroyed crossing
cell; it is not an asymptotic or Hall-capacity issue.

## 3. Why simple flatness points to an exterior ear

Equation (2.3) also gives a topology obstruction.  The crossing carrier
owners are `Z union C_i`.  Under the direct chain-fan assignment they are
all equal.  For `d>=3` there are at least two such owners, so the central
row repeats an owner and is not simple.

There is a carrier-valid local normal form.  For disjoint `Z,{x}` and
`F={f_1,...,f_d}`, take

\[
 C_i=\{x\}\cup(F-\{f_{i+1}\}),\qquad1\le i\le d-1.          \tag{3.1}
\]

Then the owners `Z union C_i` are distinct equal-rank coatoms of one fixed
set.  But the values (3.1) are pairwise incomparable, not one nested fan.
They cannot be paid by the native opposite-phase chain through a local
chain identification.  They need a nonlocal alternating return or an
exterior basis-changing ear.

The global endpoint carving from Section 1 remains useful: it pays the
packet chains while the eventual exterior-ear network is asked only to
route the incomparable displacement family (3.1).  It does not eliminate
that family.

## 4. Exact programmable-socket condition

Fix all nonstar sources around a proposed cut.  Let `P_*` be the maximal
star envelope.  Define the star-mandatory carrier mask

\[
 M_*=\bigcup_{i:\,*\in[i,i+d]}
 \left(T_i-\bigcup_{p\in[i,i+d]-\{*\}}A_p\right).             \tag{4.1}
\]

Let `mathcal P_*` be the selected protected lower pins whose physical cells
contain the star, let `S(I)` be the target on such a cell, and put

\[
 U_I=\bigcup_{p\in I-\{*\}}A_p,\qquad
 M_{\rm pin}=\bigcup_{I\in\mathcal P_*}(S(I)-U_I).             \tag{4.2}
\]

Replacing the star by a nonempty typed target `S_tau` preserves the carrier
and every protected pin if and only if

\[
 \boxed{
 M_*\cup M_{\rm pin}\subseteq S_\tau\subseteq
 P_*\cap\bigcap_{I\in\mathcal P_*}S(I).}                     \tag{4.3}
\]

If the two fan chains themselves are protected, (4.3) includes

\[
                         S_\tau\subseteq B^-\cap B^+=J.       \tag{4.4}
\]

#### Proof

Every star-containing carrier window already receives from the nonstar
sources the second term in (4.1).  Its missing coordinates are exactly the
corresponding summand of `M_*`, so its part of the lower inclusion in (4.3)
is necessary and sufficient for positive carrier replay.  The upper inclusion is the
maximal-envelope condition and prevents an extra carrier coordinate.

A protected cell containing the star has final union `U_I union S_tau`.
This equals `S(I)` exactly when

\[
                   S(I)-U_I\subseteq S_\tau\subseteq S(I).
\]

Intersecting these conditions over all protected cells and adjoining the
carrier condition gives (4.3).  The fan minima give (4.4).  \(\square\)

This is a full coordinatewise trace/common-cap criterion.  Merely assuming
that an endpoint owner or `P_*` contains `B_0,B_1` is insufficient.  For
example, at `d=2`, bases `B_0={z,a}`, `B_1={z,b}` are both contained in a
common star envelope, but setting `A_*=B_0` contaminates the fan whose
target uses `B_1`.  Only a subset of `{z}=B_0 cap B_1` can be hidden.

## 5. The exact credit count

The fan bank has `2d-1` cells.  Two strict chains consume `2d-2`; their
shared singleton is the only fan surplus.  Assigning `S_tau` to that
singleton consumes the surplus.

Independently, a one-cell insertion has net short-band gain

\[
                         (2d-1)-(d-1)=d.                      \tag{5.1}
\]

If the `d-1` destroyed pins are made redundant elsewhere, an untyped seam
has `d` unmatched-address credit.  After the singleton is assigned to the
typed task, only

\[
                              d-1                              \tag{5.2}
\]

addresses remain free.  Thus “`d` genuinely free cells plus one typed
socket” overprices the seam by one.  One may say instead that there are `d`
credits **before** choosing the task, one of which can be typed.

In the canonical coatom-chain attempt the stronger problem is (2.4): the
destroyed pins are not actually made redundant by the native new-chain
bank.  Hence even the premise needed to realize the credit count is absent.

## 6. Corrected combined theorem

The strongest unconditional local statement is therefore:

> Given two prepared global endpoint coatom traces, one packet's OLD/NEW
> deep chain discrepancy has terminal deficiency zero.  A separate inserted
> source supplies a typed socket precisely under (4.3), and supplies at most
> `d-1` additional unused addresses after the task is assigned.  Its
> `d-1` displaced crossing targets must be routed through a nonlocal
> augmenting return; they cannot be identified with the native opposite
> coatom chain.

This is not yet a `B+1` construction.  It reduces the missing theorem to an
exterior matching for the incomparable coatom family (3.1), together with
host planting of the two boundary traces and the star cut in one terminal
cap state.

## 7. Audit

The dependency-free audit checks (2.2)--(2.4), the `d=2` obstruction, the
credit count, and the carrier-valid coatom normal form for every
`2<=d<=40`:

```text
scratch/audit_coatom_boundary_star_fan_combination_nogo_20260801.py
scratch/coatom_boundary_star_fan_combination_nogo_20260801.audit.json
```

It reports

```text
PASS_CANONICAL_COATOM_CHAIN_STAR_FAN_COMBINATION_NOGO
```

with canonical payload SHA-256

```text
31c571ffbbb78e314cd3cb80515bc755c9231371b83fb18efb6801dae78ba541
```

Dependencies:

* `MATH_THEOREM_COATOM_TWO_PHASE_BOUNDARY_CHAIN_CARVING_20260801.md`;
* `MATH_THEOREM_ONE_CELL_STAR_HIDDEN_FAN_TRACE_20260801.md`;
* `MATH_THEOREM_R_ALLK_PASCAL_STUTTER_COMPILER_AND_MIXED_COVER_GATE_20260730.md`.
