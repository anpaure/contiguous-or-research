# Audit of the dimension-uniform Pascal Shadow--Braid interface

Date: 2026-07-31  
Status: PASS for the exact conditional theorem; the recursive existence
hypothesis remains open

## Verdict

The dimension-uniform Shadow--Braid compiler lemma is correct after making
all five inputs literal: exact middle ownership, exact arbitrary-width upper
witnesses, a legal resident chain-aligned P/Q schedule, simultaneous pins,
and one residual integral common cap.  If the resulting physical length is
\(B(k)\), these hypotheses construct an optimal contiguous-OR word.

The component-neutral extension is also exact at its stated level.  For
\(M=\binom{2r-1}{r}\), \(b=\operatorname{Cat}_r\), and \(N=M-b\), a
\(c\)-path cover of the \(U\)-sector placed in internal Catalan gaps has

\[
 (N-c)+2c+(b-1-c)=M-1
\]

untagged lower-q1 slots.  This is a slot identity; an all-but-one palette
requires joint injectivity of the internal, port, and direct-seam colours.
The direct separated cap-two residual graph cannot provide the required
macro cover because its selected \(AA\) vertices form sealed cycles.  The
nonvacuous recursive object is the coupled cap-two/socket factor of
Theorem 2.3, required to be an acyclic \(b\)-path cover with one \(X\) and
one \(Y\) endpoint per component.

The odd-spine induction is also logically correct only in its stated
conditional form.  Its base package must have length \(B(2r_0-1)\), and each
instance of CSB\(_r\) must produce lengths \(B(2r)\) and \(B(2r+1)\) plus the
auxiliary factor and event/port data for the next odd package.  CSB\(_r\) is
not proved; it is terminal integral compiler feasibility, not a weak
probabilistic premise.

## Exact checks

The deterministic audit verifies:

1. the odd-to-even, even-to-odd, and four-sector binomial/Catalan identities
   for semilengths \(2\le r\le256\);
2. the exact parity recurrence for the staircase depth through dimension
   512, including \(d_{15}=d_{16}=d_{17}=3\);
3. the local facet and union run transforms with their necessary singleton
   exclusions, and the Catalan new-tag condition
   \(g\ge d,\ g\ge\lceil(u+2)/2\rceil\);
4. the all-\(r\) component-neutral and residual-sector identities, including
   the necessary colour-injectivity and endpoint-compatibility gates;
5. the K15-to-K17 owner-level factor ledger: sectors
   \(5005+3\cdot6435\), 24,310 distinct lower-q1 colours, 17 components,
   1,739 upper-q1 holes, 4,045 total upper holes, 60 direct-formula
   occurrence conflicts, the 61-deletion Hamilton-repair floor, and the
   independent 49-cut residence floor for the frozen 19,170-cycle; and
6. the frozen K17 component instance: the cyclic untagged bank
   \(4268+1474+693=6435\), its derived linear count 6,434, and the literal
   residual graph with 1,430 balanced \(X\)-to-\(Y\) paths plus 15 sealed
   \(AA\) cycles of total size 5,005; and
7. the K16 protected-reroot interface: block lengths \(6389,6437,44\), all
   39,197 old interval values internally protected, six new upper values,
   the singleton `0x8000` schedule, the common-cap replay, and literal
   coverage of all 65,535 nonzero masks by `answers/k16.word`.

The referee audit additionally checked the four-sector degree ledger, the
component-neutral slot/palette distinction, the coupled residual degree and
endpoint equations, the arbitrary-start safe-corridor criterion, common-cap
semantics, upper transfer, and the conditional odd-spine proof.  Witness
spans in the reroot ledger are internal cut supports, and the parity
transport formulas are explicitly bulk formulas away from singleton
collapses and turn collars.

## Scope boundary

The audit does not construct CSB\(_r\), a balanced coupled residual K17
factor, or a K17
word.  Pascal counts prove owner flow; protected rerooting exactly verifies a
candidate braid; neither proves that one common candidate satisfying upper,
residence, pins, and common-cap compilation exists in every dimension.

## Frozen artifacts

- `MATH_THEOREM_DIMENSION_UNIFORM_PASCAL_SHADOW_BRAID_INDUCTION_20260731.md`
  SHA-256 `a0b90eccd3d3cfd311eee68bce7e2dbacfd08d378a6b5913df24c42b1210906e`.
- `scratch/audit_dimension_uniform_pascal_shadow_braid_induction_20260731.py`
  SHA-256 `3af4db6755414efeb99b5dab0900df741863b69cc3d34e043fab3de5ecd6ee47`.
- `scratch/dimension_uniform_pascal_shadow_braid_induction_20260731.audit.json`
  SHA-256 `056db46dcd608756be5c2575969da38837727605c41e30e595045d35aaa5e77d`,
  normalized payload
  `db3739284e37b196c9667300fefdbe2e755de66473c24f8ae1513abbd3544671`.

All dependencies and their exact hashes are embedded in the JSON audit.
