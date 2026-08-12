# The nonlocal Haar suspension is reduced to coherent suffix-cylinder sealing

## Status

**Rebased correction (2026-08-06).**  The phase-coherent sealing lemma
stated below is false if every lifted component is required to stay inside
one fourteen-row suffix cylinder and the outside MSW completion is left
untouched.  The exact terminal-endpoint criterion and the port-transversal
contradiction are proved in
`MATH_THEOREM_HAAR_FOUR_SWITCH_DYCK_SUFFIX_CYLINDER_SEALING_GATE_20260806.md`.
At least one preparatory component must enlarge into other suffix sectors or
force a reselection of the completion.  The telescoping statements below
remain correct conditionally for any such enlarged coherent lift.

The rank-four nonlocal Haar circuit consists of three preparatory
interaction-component switches and one final four-row switch.  The final
four-row packet now has an all-dimensional common-tail tensor, and its
complete contiguous union/intersection current is a finite collection of
nested rails.

This note records the exact remaining interface.  If the four base switches
admit one phase-coherent ported suffix lift, then all intermediate all-width
currents telescope automatically and the resulting large-dimensional move
has precisely the already-audited finite Tamari rail current.  Existing MSW
suffix and prefix functors prove this for one canonical component at a time;
they do not prove the phase-coherent lift after the preparatory switches have
made the factor noncanonical.

No computation or search is used.

## 1. General suffix extension ledger

Let `P=(P_0,...,P_s)` be a complement geodesic on a `2s`-set and let
`R=(R_0,...,R_t)` be a complement geodesic on a disjoint `2t`-set.  Its
suffix extension is

\[
 P\star R=(P_0+R_0,\ldots,P_s+R_0,
            P_s+R_1,\ldots,P_s+R_t).
\tag{1.1}
\]

For two finite path families `A,B`, the extensions `A star R` and
`B star R` have equal state and adjacent-union ledgers provided that

1. `A,B` have equal aggregate state ledgers;
2. `A,B` have equal aggregate adjacent-union ledgers; and
3. their terminal endpoint multisets agree.

Indeed, base states and edges acquire the common set `R_0`; every junction
or tail state and edge is the appropriate fixed function of the terminal
endpoint and the common path `R`.  This is the ledger mechanism used by the
ported Tamari tensor.

The same endpoint argument works for every contiguous chord.  Chords wholly
inside the common tail agree pointwise.  Cross-tail chords are the finite
base endpoint currents transported on `R_0 union R_j` and
`R_0 intersection R_j`.  Hence no new dimension-growing current is created.

## 2. Telescoping through a phase sequence

Consider exact factor phases

\[
             F_0\longrightarrow F_1\longrightarrow\cdots
             \longrightarrow F_4
\tag{2.1}
\]

realizing the three preparatory Haar switches and the final switch.  Suppose
every row occurrence in all five phases has been opened and suffix-extended
with one common tail system so that each arrow is a literal exact-factor
component switch after extension.

For any fixed chord type, let `C(F_i)` be its signed occurrence ledger.
The aggregate current of the whole sequence is

\[
 \sum_{i=0}^3(C(F_{i+1})-C(F_i))=C(F_4)-C(F_0).
\tag{2.2}
\]

Thus intermediate all-width damage cancels identically.  Common rows in
the two endpoint factors cancel, and after the port-restored decomposition
the remaining endpoint current is exactly the ten finite currents and their
nested-tail transports in
`MATH_THEOREM_TAMARI_TENSOR_COMPLETE_CHORD_RAIL_CURRENT_20260806.md`.

Consequently there is no additional all-width-current lemma to prove once
the coherent literal lift (2.1) exists.

## 3. What the current context theorems prove

The suffix-lifting lemma in `MSW_COMPONENT_HIERARCHY_REDUCTION.md` says:
if one canonical MSW root family `X` has a transposition-invariant path
union and transposition-invariant endpoint family, then appending a Dyck
suffix produces a closed connected lifted component.  Its proof uses the
literal decomposition

\[
 P(xR)=\{zR:z\in P(x)\}\ \cup\
        \{\overline x w:w\in P(R),\ w\ne R\}.
\tag{3.1}
\]

`MSW_PREFIX_CONTEXT_FUNCTOR.md` supplies the corresponding owner-incidence
transport for canonical capped roots.  These are exact one-phase results.

They do not imply (2.1).  After the first preparatory switch the incumbent
factor is noncanonical, and the next interaction component is recomputed in
that changed factor.  The current theorems do not provide simultaneously:

1. one compatible opening of every row in every phase;
2. endpoint invariance for every recomputed component;
3. closure against interaction edges leaving the proposed suffix cylinder;
4. preservation of the same physical tail rails through all four arrows.

The obstruction is visible already at the base endpoint interface.  The
completed Haar factors are weakly Dyck-transversal but not canonically
port-transversal; some selected Dyck roots are internal path states.  The
ported four-row replacement repairs the final changed packet, not the ten
common completion rows or all preparatory phases.

## 4. Exact remaining lemma

> **Phase-coherent suffix-cylinder sealing lemma.**  The complete rank-four
> Haar factor sequence admits openings and a common suffix extension such
> that every lifted preparatory/final switch is a closed interaction
> component in its current phase, all unchanged rows agree literally, and
> the protected tail rails are retained from `F_0` to `F_4`.

This lemma would suspend the entire nonlocal circuit to every larger
semilength.  By Section 2, its all-width accounting is then automatic.

The existing MSW prefix/component theorems establish the lemma's
single-canonical-phase special case only.  They do not presently establish
the phase-coherent noncanonical statement.
