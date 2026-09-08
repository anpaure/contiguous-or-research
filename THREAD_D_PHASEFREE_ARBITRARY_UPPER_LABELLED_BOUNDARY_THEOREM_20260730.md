# Thread D: exact arbitrary-upper labelled boundaries for the phase-free rail master

Date: 2026-07-30

This note closes the arbitrary-width upper-separation interface for the
phase-free two-rail option circuit of
`MATH_THEOREM_K16_JOINT_QUOTIENT_PATH_PHASE_HISTORY_MODEL_20260730.md`.
It does not assert that the resulting `K=16` master is satisfiable, and it
does not address the lower fixed-depth rows or the final compiler.

## 1. Physical and quotient variables

Let `K=2R`, `n=K-1`, and let `rho` rotate the first `n` coordinates while
fixing the top coordinate.  A phase-free transition option `a` is one
literal Johnson dart between two quotient owners, with its relative phase
already included.  Selecting `x_a=1` activates all physical darts

\[
   \rho^j e_a,\qquad j\in\mathbb Z_n.
\]

The executable atlas removes precisely the options whose source and target
are the same quotient owner, matching the `AddCircuit` master.  Every other
allowed physical Johnson dart has exactly one option label.  Thus labels,
not physical dart copies, are the correct projection variables.

## 2. Accumulated-union automaton

Fix a strict upper target `U`, with `|U|>R`.  Its state set is

\[
  \mathcal V_U=\{(X,S): X\in {U\choose R},\ X\subseteq S\subseteq U\}.
\]

Every `(X,X)` is an unconditional start.  A state with `S=U` is accepting.
An allowed physical dart `e=(X,Y)`, where `Y` is also contained in `U`,
induces

\[
 (X,S)\longrightarrow(Y,S\cup Y),
\tag{2.1}
\]

and this automaton transition carries the unique quotient-option label
`lambda(e)`.

### Theorem 2.1 (literal acceptance)

For an integral owner-perfect successor assignment, the automaton accepts
if and only if some nonempty cyclic interval of physical middle states has
union exactly `U`.

#### Proof

A literal interval contained in `U` follows (2.1), and its second component
is its running union.  Conversely, an accepting automaton path follows
selected physical successor darts, because every physical middle owner has
one selected successor.  Its states form a consecutive chronology interval
inside `U`, and acceptance says their union is `U`.  A repeated lap can be
deleted: a second visit to the same physical owner cannot contribute an
element not already accumulated on the first lap.  Hence a witness of at
most one cyclic lap always exists.  QED.

## 3. Exact quotient-option boundary row

At an integral incumbent `x`, let `R_U` be all automaton states reachable
from all starts using selected transitions.  Suppose no accepting state is
reachable.  Define

\[
 B_U(R_U)=\{\lambda(e):
       \text{some copy of (2.1) labelled }\lambda(e)
       \text{ leaves }R_U\}.
\tag{3.1}
\]

The braces in (3.1) are essential: parallel physical copies with one option
label are counted once.

### Theorem 3.1 (sound generalized CEGAR row)

The clause

\[
             \boxed{\ \sum_{a\in B_U(R_U)}x_a\ge1\ }
\tag{3.2}
\]

is valid for every phase-free master assignment that covers `U`, and it is
violated by the incumbent.  If the boundary is empty, `U` is unreachable in
the entire option atlas and (3.2) is an exact infeasibility row.

#### Proof

All starts belong to `R_U`, and no accepting state does.  Any accepting path
under another assignment must therefore first leave `R_U`.  Its first
boundary transition carries a label in (3.1), so that assignment selects at
least one variable in (3.2).  In the incumbent, a selected boundary label
would activate the particular physical copy leaving a reachable state and
make its destination reachable.  Therefore no boundary label is incumbent-
selected, and the incumbent violates (3.2).  QED.

This is stronger than the full-tour no-good: it retains only the option
labels capable of crossing the frozen accumulated-union reachability cut.
It is a necessary row, not by itself a sufficient encoding of coverage;
repeated exact separation supplies the full finite cut family.

## 4. Equivariant orbit compression

Rotation transports `(X,S)` to `(rho X,rho S)` and carries every physical
dart copy to another copy with the same option label.  Consequently

\[
 B_{\rho^jU}(\rho^jR_U)=B_U(R_U).
\tag{4.1}
\]

Thus one representative row is both necessary and sufficient for a missing
target orbit.  This remains true for a target with a nontrivial stabilizer;
one must use its actual orbit size for reporting, but must not multiply the
existence row by that size.

## 5. Exact event-stream oracle

The literal audit avoids an `O(W^2)` interval scan.  For a fixed start state,
find the first future occurrence of each coordinate absent from that state.
The interval union changes only at these first-arrival positions.  Sorting
them and adding all tied arrivals enumerates all and only distinct upper
unions from that start.  Precomputing next occurrences over the doubled
cyclic chronology gives an `O(KW+K^2W)` oracle and also returns a literal
start/end witness for every covered target.

This recurrence includes cyclic wrap, arbitrary width up to one complete
lap, tied insertions, and the full ground set.  It is not a fixed-`q`
witness approximation.

## 6. Executable validation

The implementation is

```text
scratch/threadD_upper_accumulated_union_separator_20260730.py
SHA-256 6130ed3c6380c4a62dc82547a05d2513adf4d03f57de21abdb67603ff035940f
```

The solver-free K8/K10 replay is

```text
scratch/threadD_upper_accumulated_union_separator_k8_k10_20260730.audit.json
SHA-256 f8f8463ed7d5768be0b5c41be346be18ac76a67edef898ea332525ddf899a186
payload SHA-256 d62fd13e338e049bb8ba041a2bb11d1f995f8850d396dce39832eeb1a68d3b31
```

It consumes the retained materialized carriers

```text
scratch/k8_phasefree_solve.json
SHA-256 5bc4d118085da9efc3c6b74ad4efd4ef1f342581a1e943fb63db91d44fad605f

scratch/k10_phasefree_solve.json
SHA-256 10b6c4a98b49b42f951441d7af17df2cc3f69c5c2b2f4ced155d758ca3fc22a9
```

Exact results are:

| carrier | strict-upper targets | covered | missing | missing orbits |
|---|---:|---:|---:|---:|
| K8 | 93 | 93 | 0 | 0 |
| K10 | 386 | 377 | 9 | 1 |

The K10 hole orbit has representative `687`, rank `7`, and orbit size `9`.
Its reachable automaton has `28` states.  There are `238` physical boundary
copies, which deduplicate to exactly `153` quotient-option labels.  Every
translated target produces the same row, with option-list SHA-256

```text
3cd15439839401fc23a8b06798e84c8f4b5526ef9586df989ab5feb3a1ebe0fb
```

No selected K10 option occurs in that boundary.  Hence the fresh K10
q1+resident carrier is not compiler-ready: independently of its three lower
q2 holes, it fails this exact arbitrary-width upper row.

## 7. Integration boundary

For a decoded missing orbit representative, the CP-SAT master may install

```python
model.AddBoolOr([choice[a] for a in boundary_option_ids])
```

and resume.  Rows are scoped to the current phase-free option atlas,
including its quotient-self-loop omission, but not to the incumbent tour.
They remain valid before or after circuit connectivity, one-block, voltage,
q1, and residence constraints are imposed.

A resource-limited CEGAR run is `UNKNOWN`.  A CP-SAT `INFEASIBLE` status is
still a trusted-solver, scoped result unless accompanied by a separately
replayable formal proof.  No K16 solve was run for this note.
