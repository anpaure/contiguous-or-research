# Independent audit: rolling-reset three-return strict-gammoid obstruction

**Date:** 2026-08-01  
**Audited file:**
`MATH_THEOREM_L_ROLLING_RESET_THREE_RETURN_STRICT_GAMMOID_OBSTRUCTION_AND_PRIVATE_SINK_GATE_20260801.md`  
**Verdict:** PASS after the scope corrections recorded below.  The audit is
symbolic; no finite search was used.

## 1. Direct reset endpoints

The opened-reset theorem gives the owner-attachment endpoints

\[
                         (T_0,T_{N-1})
\]

and predecessor endpoints

\[
             (T_0^-,T_{N-1}^+),\qquad
             (T_0^+,T_{N-1}^-).
\]

All three forget to the same adjacent root pair.  Their unique common
rank-\((r+1)\) owner is

\[
                         U_{N-1}=T_0\cup T_{N-1}.
\]

Thus the direct owner return recloses the reset component, while the two
direct predecessor returns are the two orientations of that same owner and
form the closed doubleton.  Proposition 1.3 is correct: the strict-gammoid
compiler reserve cannot remove this earlier owner-resource obstruction.

Proposition 1.2 is independently correct as well.  A strict stutter fixes
its incoming predecessor, outgoing successor, and owner in both phases, so
its symmetric difference has zero boundary in both chronology matchings.
Disjoint union preserves zero boundary.  Thus the item2552L sidecar can
protect compiler cells but cannot itself be any of the three reset returns.
The weak pivot instead has a nonzero internal owner-resource current; its
two-edge old/new paths have the same external endpoints, so it does not by
itself carry a reset-return endpoint boundary either.

## 2. Fixed-cap Hall and the minimal 3-circuit

After deleting occurrence cells \(D\), Hall is

\[
 |N(A)-D|\ge |A|
 \quad\Longleftrightarrow\quad
 |D\cap N(A)|\le |N(A)|-|A|
 \qquad(A\subseteq\mathcal T).
\]

Hence equation (1.2) is exact under the stated deletion-only fixed-cap
interface.

For one target adjacent to three cells, the compiler transversal matroid is
\(U_{1,3}\) and the safe-deletion dual is \(U_{2,3}\).  Every proper
hazard subfamily is safe; deleting all three cells violates the singleton
target cut by \(3>2\).  With one matched cell and two unmatched cells, every
two sources have disjoint alternating paths to the two sinks, whereas all
three do not.  This verifies Theorem 2.1 and its minimality among singleton
three-return hazards.

## 3. Matroid scope

The three rank-two partition matroids with parallel classes

\[
 ab|cd,\qquad ac|bd,\qquad ad|bc
\]

have pairwise common bases but no joint base.  Adding a common coloop gives
the asserted rank-three example.  The warning against pairwise
matroid tests is therefore correct.

The prospective formula \(P\cap L\cap K\) is exact only under both explicit
hypotheses now stated in the theorem:

1. each compiler packet has a matroidal single-cell (or otherwise proved)
   pullback; and
2. the typed chronology choices are represented by one literal gammoid.

Source privacy alone does not imply (2), and multi-cell packet union does
not imply (1).

On the stronger separated typed-corridor face, each type has its own
strict gammoid truncated to rank one.  Their direct sum has rank at most
three, and every size-three independent set contains exactly one member of
each type.  Intersecting this return gammoid with the singleton-hazard
pullback of \(M_\theta^*\) is therefore ordinary two-matroid intersection.
The pullback parallelizes equal hazard-cell images; the theorem explicitly
treats such equality as a physical resource conflict, so it does not
mistakenly count one shared deletion twice.
Edmonds' formula gives exactly

\[
 \min_{X\subseteq E}
 \bigl(r_{L_{\rm ret}}(X)+r_K(E-X)\bigr)\ge3.
\]

For the \(U_{2,3}\) compiler example this row fails at
\(X=\varnothing\), where its two terms are \(0+2\).

This audit uses all hypotheses stated in the theorem: fixed flag table and
cap, pairwise-disjoint corridor interiors, prescribed typed sinks, and
aligned-column compatibility of every realized triple.  Without the typed
sinks, the two crossed arcs \(a\to B,b\to A\) give an unpaired rank-two
linkage but fail the prescribed pairs \(a\to A,b\to B\).

## 4. Positive sufficient conditions

The private-sink theorem is exactly the strict-gammoid linkage
representation: simultaneous compiler safety is equivalent to one joint
vertex-disjoint relocation into distinct unmatched-cell sinks.  Pairwise
vertex-disjoint private relocation blocks are sufficient.  For an allowed
deletion family, a fourth private block proves the adaptive all-\(F\) row.
A constant-height conclusion additionally requires a uniform bound on the
relocation-path lengths and surviving packet guards; this condition is now
explicit.

The root-slot specialization is sound only with literal injected slot
fibres, plus the residual-matching avoidance clause of the trace-guarded
root-slot definition.  A root name attached to an arbitrary hazard cell is
not sufficient.  The theorem now states the literal containment condition.
For \(B+1\) private copies per type, the count

\[
                 |P_0|+3a(B+1)+b_{\rm del}\le m+1
\]

correctly certifies one matching avoiding the complete copy/deletion union.
It remains conditional on literal distinct injected fibres, on each
deletable resource hitting at most one copy while shared endpoints/cap/guards
are protected, and on the separate aligned chronology corridors.  The count
alone is a compiler statement and does not bound return length.

## 5. Scope-safe conclusion

The note proves two independent negative gates:

1. direct same-neighbour reset closure fails at the unique owner; and
2. externally disjoint return paths can still fail at a compiler
   \(U_{2,3}\) cut.

It conditionally closes the second gate by joint private-sink linkage or a
genuine trace-guarded root-slot lift.  It does not construct the required
external chronology paths, a physical pivot/root-slot embedding, or a
regenerative common-cap compiler.
