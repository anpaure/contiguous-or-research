# Audit synthesis of the nine GPT-Pro candidate responses

**Date:** 2026-08-13  
**Status:** proof-safe comparison.  None of the nine responses proves
\(\nu(k)\le B(k)+O(1)\), but several contain genuine advances.  The strongest
new positive statement is an exact short-period two-state realization of the
special insertion-star macro in the owner/immediate-palette projection.  The
strongest new structural statement is the literal width-two rigidity of every
minimal-aperture resident rail.

## 1. Executive verdict

The responses materially improve the proof frontier in four places.

1. A period-\(2q+1\) pure rail is genuinely two-sided resident.  The
   Mütze--Standke--Wiechert minimum-odd-cycle factor therefore gives an exact
   positive rail factor of every fixed central shell \((C,T)\),
   \(|T|=2q+1\).
2. The special insertion-star current admits a literal short-period,
   owner-simple two-state realization by closed resident rails, including
   simple immediate lower and upper palettes.  Its remaining difference is
   the explicit conformal pair \(B^+,B^-\); this is not yet a one-owner
   absorber.
3. The pair \(B^+-B^-\) has an exact normal form as \(q(q-1)\) Johnson
   squares.  Every adjacent square has a literal four-rail common-reserve
   lift, and arbitrary squares telescope along exact-distance context paths
   at the level of nonnegative integer multiplicities.
4. Every minimal-aperture resident rail is a literal \(q\)-window shift
   register.  Its rank-\(R+1\) adjacent-union tickets are injective, so a
   zero-all-width switch cannot live on one such rail.  A literal resident
   \(q\)-step phase reset nevertheless exists.

The claimed global common-reserve theorem does **not** survive audit.  Its
last squarefree-packing step uses a false safe-order estimate.  For a fixed
context transition the rail core is unique, and a compatible forbidden owner
occurs with probability \(1/(q-1)\), not factorially small.  A family of only
\(q-1\) forbidden owners can block every local order.  Moreover every internal
path seam repeats one compulsory rank-\(R-1\) and one rank-\(R+1\) ticket.

Thus the global proof is still open at the same three joint gates:

\[
 \boxed{\text{squarefree positive owner/flag factor}}
 \longrightarrow
 \boxed{\text{occurrence-safe connected socket state}}
 \longrightarrow
 \boxed{\text{typed common-cap cut}}.
\]

## 2. Results promoted as proof-safe

### 2.1 Central resident shell factor

For \(q\ge2\), a period-\(2q+1\) toggle order gives the trace
\(1^q0^{q+1}\) on every toggle coordinate.  All proper cyclic interval decks
are simple.  Hence the odd-graph \(C_{2q+1}\)-factor partitions each complete
shell

\[
 \{C\cup Q:Q\in{T\choose q}\},\qquad |T|=2q+1,
\]

into exactly \(\operatorname{Cat}_q\) legal resident rails.  This is a true
positive factor, but only of one shell; fixed-core divisibility and global
overlapping-core allocation remain.

Proof and audit:

- `MATH_THEOREM_PERIOD_2Q_PLUS_1_PURE_RAIL_RESIDENCE_AND_CENTRAL_WREATH_FACTOR_20260813.md`
- `MATH_AUDIT_PERIOD_2Q_PLUS_1_PURE_RAIL_RESIDENCE_AND_CENTRAL_WREATH_FACTOR_20260813.md`

### 2.2 Minimal-aperture rigidity and resident reset

If \(H_t=F\sqcup J_t\), \(|J_t|=q\), is a closed resident Johnson walk,
then every nonconstant positive run has length exactly \(q\) and

\[
 H_t=F\cup\{x_{t-q+1},\ldots,x_t\}.
\]

For a legal pure rail of period \(m\ge q+2\), the adjacent unions

\[
 U_t=F\cup\{x_{t-q+1},\ldots,x_{t+1}\}
\]

are pairwise distinct.  Consequently every all-width-neutral compound
switch must match changed edges across rails with literally equal \(U_t\).
This is an actual-column character, not a generic parity gadget.

The phase-reset path

\[
 X_t=F\cup\{a_{t+1},\ldots,a_q,z_1,\ldots,z_t\},\qquad0\le t\le q,
\]

is Johnson, owner-simple, palette-simple, shielded, and extends to a
two-sided resident pure rail.  The missing object is a cross-rail reset braid
whose complete ticket current is zero and whose socket action is odd.

Proof and audit:

- `MATH_THEOREM_MINIMAL_APERTURE_WIDTH2_RIGIDITY_AND_RESIDENT_Q_RESET_20260813.md`
- `MATH_AUDIT_MINIMAL_APERTURE_WIDTH2_CHARACTER_Q_RESET_AND_SERPENTINE_WRAP_20260813.md`

### 2.3 Conditional phase-clock dilation

The clock dilation is locally correct if the input bank already has the
required phase-, width-, and endpoint-cut-refined current identities.  Its
automatic spanning-host conclusion is presently justified only in the
central odd ambient \(k=2R-1\).  Ordinary all-width current equality and an
uncoloured or merely properly phased two-factor do not imply the refined
hypothesis.  The even ambient has unequal incidence shores and needs a
separate host theorem.

Proof and audit:

- `MATH_THEOREM_PHASE_CLOCK_DILATION_RESIDENT_ALLWIDTH_LOCAL_AND_CENTRAL_ODD_HOST_20260813.md`
- `MATH_AUDIT_PHASE_CLOCK_DILATION_HOST_SCOPE_20260813.md`

The previously audited complementary-square bank remains the strongest
unconditional resident all-width phased-host theorem currently available.

## 3. Exact positive progress which does not close the owner gate

### 3.1 Short-period insertion-star two-state packing

The short-period construction makes the \(2q-1\) signed insertion/star rails
simultaneously owner-simple.  After retaining their common unchanged decks,
it gives two nonnegative squarefree rail packings

\[
 R_H\sqcup B_H^+,
 \qquad
 R_H\sqcup\{H\}\sqcup B_H^-.
\]

Every rail is closed and resident; owner and immediate-palette occurrences
are simple.  This is a genuine actual-column realization of the special
macro, but the two states differ by the macro \(Y_H\), not by the lone owner
\(e_H\).  Closing a one-owner absorber still requires a common reserve for

\[
 Z_H=e_H-Y_H=B^+-B^-.
\]

The exact remaining compulsory current is visible already in the width
ledger

\[
 D_{q-1}=\mathbf1_{H-x},\qquad
 D_q=\mathbf1_H,\qquad
 D_{q+1}=\mathbf1_H+e_x.
\]

Its second difference is zero, whereas an arbitrary nested triple
\(H-x,H,H+y\) has second difference \(e_y-e_x\).  Thus the insertion-star
mechanism alone cannot install all literal Ferrers tickets.

This result and the adjacent-square result below are audited together in
`MATH_AUDIT_THREE_CONFORMAL_RESERVE_CANDIDATES_SHORT_PERIOD_SQUARE_AND_PERIODM_20260813.md`.

### 3.2 Square normal form and adjacent-square lift

The special residue has an exact decomposition into \(q(q-1)\) currents

\[
 e_{K+p}+e_{L+x}-e_{K+x}-e_{L+p}.
\]

For adjacent \((R-1)\)-contexts \(K,L\), two varying cores and four legal
closed rails give a literal common owner reserve of size \(2M-4\).  The
identity is resident and point-neutral.  Along a context path these identities
telescope and produce a nonnegative **multiset** reserve.

The adjective multiset is essential.  It does not imply one squarefree owner
matching, and the literal four-rail lift repeats proper lower palettes.  It is
therefore a positive algebraic normal form, not yet an absorber usable inside
the global factor.

## 4. The failed period-\(M\) common-reserve proof

For a context edge \(G_iG_{i+1}\), the proposed rail order

\[
 (A_i,x,p,F_i,\omega_i)
\]

does realize exactly the current

\[
 \delta_{xp}(G_i)-\delta_{xp}(G_{i+1}).
\]

The path telescope is correct.  Section 1.7's packing argument is not.

1. The core is forced: \(D_i=G_i\cap G_{i+1}\).  There are not
   exponentially many core choices after the transition is fixed.
2. For \(a\in A_i\), the owner
   \[
   D_i\cup\{x,p\}\cup(A_i-a)
   \]
   occurs with probability \(1/(q-1)\) under a random order of \(A_i\).
   The \(q-1\) such owners hit every order.
3. Every internal seam forces the lower ticket \(G_{i+1}\) twice and the
   upper ticket \(G_{i+1}\cup\{x,p\}\) twice.  No filler ordering can remove
   these repetitions.

A single block-monotone path can be packed at owner level: nonadjacent cores
are too far apart to share an owner, and adjacent common-deck collision is
avoided by one filler-seam inequality.  What remains is a simultaneous
multicommodity routing theorem handling endpoint bridges, cross-commodity
clusters, and the forced palette tickets.

Audit:

- `MATH_AUDIT_CONFORMAL_STAR_CYCLE_RESERVE_SQUAREFREE_ASSEMBLY_20260813.md`

## 5. Other rejected or conditional claims

1. The proposed serpentine wreath has a literal wrap error.  At
   \(i=q-1\to0\), its filler windows begin at \(\varepsilon q\) and
   \((1-\varepsilon)q\), which are disjoint \((q-1)\)-windows, so the seam is
   not Johnson-adjacent.  The congruence cannot be repaired by changing one
   index; a reset seam or doubled base period is required.
2. The maximal-period and \(q\)-thick inflations require a refined phased
   endpoint-current identity which is not a conclusion of the quoted host
   theorem.  Their global host assertion also overlooks the even-\(k\)
   unequal-shore case.  They are not promoted over the already audited
   complementary-square construction.
3. The block-inflation/one-hole reserve response correctly reduces the
   special star residue to one decorated punctured insertion rail, but its
   claimed exposure inheritance and literal source subdivision are not
   proved.

## 6. Revised decisive target

The next attack should not ask for another generic absorber.  It should ask
for one of the following two concrete objects.

### Route A: close the special residual

Construct a squarefree, compulsory-ticket-safe simultaneous lift of the
\(q(q-1)\) explicit context commodities.  It must:

- choose all paths before their forced owner/ticket families are exposed;
- resolve the duplicated \(G_i\) and \(G_i+\{x,p\}\) seam tickets by a
  compound braid rather than by random filler order;
- keep both aggregate shores owner-simple; and
- preserve the literal lower flag and cap-prefix rows.

### Route B: bypass local absorption

Use the exact resident central-shell factors inside the positive
overlapping-core role flow, then prove a named cyclic-order factor directly.
The remaining binary ordering system must select one order per shell so every
rank-\(R\) owner occurs exactly once.  A growing-rank nibble is useful only if
its structured leave is then absorbed by Route A.

Neither route currently supplies the typed common-cap cut.  That cut must be
verified in the same selected occurrence state, after every bank, flag,
reserve, and fusion switch has been fixed.

## 7. Bottom line

The nine responses contain real progress but not the advertised full
breakthrough.  The owner obstruction is now far more structured:

\[
 \boxed{
 \text{special }B^+-B^-
 \;\longleftrightarrow\;
 q(q-1)\text{ explicit exact-distance context commodities}
 }
\]

and the topology obstruction is now equally concrete:

\[
 \boxed{
 \text{every changed minimal-aperture edge must be paired across rails at
 the same literal }(R+1)\text{-union}
 }.
\]

Those are substantial reductions.  The missing theorem is a joint
squarefree compound-braid/linkage theorem, not another rational-lattice or
ordinary Hall statement.
