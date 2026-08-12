# Independent audit of the fixed-core skip-port common-base absorber

**Date:** 2026-08-02  
**Status:** PASS after the scope and quantifier corrections recorded below.  
**Audit mode:** read-only review of the theorem and verifier, plus independent
exact finite replays.  No K17 nested-address SAT was launched.

## 1. Audited artifacts

The verdict applies to:

* `MATH_THEOREM_A_FIXED_CORE_SKIP_PORT_COMMON_BASE_AND_TORSION_ABSORBER_20260802.md`,
  SHA-256
  `38c8ced8e336faa6c23a455b777962f5189385f15e00a2d318460572b50c447e`;
* `scratch/a_fixed_core_common_base_absorber_20260802/audit_a_fixed_core_common_base_absorber_20260802.py`,
  SHA-256
  `0e61480feea2b70d0329158a4cad04185cf4d59c07d6aa2eff6b864a1bcf780a`;
* `scratch/a_fixed_core_common_base_absorber_20260802/audit.json`,
  SHA-256
  `9284286e3e5a0ae2efeec01c581f5d5b9fcbf4b04587d564e1ffcee219f684d4`.

## 2. Theorem-by-theorem verdict

### 2.1 Skip-port exact cover: PASS

For every decorated row, its skip column covers both private ports.  If the
skip is absent, exact port coverage forces exactly one incoming and one
outgoing completed transition.  The incoming column is the unique column
which carries that row's named target/owner bundle.  Thus the physical rows
are exact precisely when the selected decorated rows satisfy the target and
owner equations of the joint master.  Conversely, skips complete every
unused row.  This proves the stated equivalence.

The construction gives a directed cycle cover, not one directed cycle; the
theorem keeps that topology row separate.  Protected macros are covered only
when represented by complete literal columns and contracted on the same
literal face, as now stated.

### 2.2 Cone, lattice, semigroup, and integral faces: PASS

For a zero-one residual demand and nonzero zero-one columns, every
nonnegative integral representation is automatically binary and
support-disjoint.  Hence cone membership is fractional feasibility,
semigroup membership is one-copy feasibility, and lattice membership is a
genuine necessary intermediate row.  Normality, or normality at the one
specified demand, gives the claimed implication.

The stronger faces are correctly qualified:

* total unimodularity applies to the same residual matrix and integral
  demand;
* the matroid route requires an exact two-matroid base formulation and an
  integral, payload-transparent lifting fibre;
* protected restrictions must already be deletions, contractions, or
  compatible direct sums in those two matroids; a third matroid is not
  silently added; and
* the hinge/rectangle route is applied only after one common integral table
  has been fixed.

The Hoffman cylinder condition was also checked independently by exhaustive
enumeration for up to three rotor states and three roles.  Its sign and its
complementary upper cuts agree with the stated condition.  The final version
correctly uses a separate rotor-state vertex set and assumes zero total
boundary.

Corollary 2.4 is now proof-safe.  The complementary interval banks supply
only a central four-resource subtable; the corollary separately assumes an
embedding into one exact decorated owner--payload table, transparency of all
central labels and surviving guards, and a fresh Hoffman check after any
cycle-edge deletion.  It also distinguishes fixed Johnson tail/head labels
from variable rotor-state endpoints.  The static graph claim is exact: for
`c` cyclic components, deleting one edge per component creates defect `c` in
each outer palette.

### 2.3 Ticket quotient and common-mode requirement: PASS

The exact quotient is the full finitely generated group

\[
       \mathbb Z^V/\Lambda(A_0)\cong
       \mathbb Z^f\oplus G_{\rm tor},
\]

not merely the finite saturation quotient.  This correctly retains ticket
deltas outside the real span and permits their free components to cancel.
Equation (3.2) is exactly the condition that the residual demand belongs to
the bulk column lattice.  It is restricted to jointly realizable mode tuples
and to a common bulk catalogue.  Mode-dependent catalogues are explicitly
excluded from the one-quotient test.

After the free coordinates are cleared, `d_i-1` independent binary tickets
in a pure generator class of each `Z/d_i` factor suffice: activate the
canonical representative number `0,...,d_i-1` of tickets in that factor.
This is only a torsion statement and does not assert cone membership or
normality.

The common-mode warning is necessary.  The displayed five-row example has
bulk determinant `-2`; its default residual demand has the unique coefficient
vector `(1/2,1/2,1/2,1/2)`, while the alternative has the unique integer
vector `(-1,0,0,1)`.  The bulk semigroup is normal because the four columns
are independent, yet neither mode is integrally feasible.  Thus cone,
lattice, and normality must be tested on the same mode and matrix, exactly as
Theorem 6.1 now requires.

The K19/K21 bounds are used only as scalar row-footprint bounds.  The final
corollary counts the actual distinct short rows in a completed bank; it does
not equate a possibly multi-row macro block with one short row.

### 2.4 Parity determinant and direct sum: PASS with the stated abstract scope

The even `2x2x2` tensor has rank four.  All twelve nonzero maximal minors
have absolute determinant two, so its column lattice has exact saturation
index two.  Half-weighting all four columns gives the unit demand, while the
resource equations force a half-integral coefficient and exclude an exact
cover.  Adding `001` changes the maximal-minor gcd to one and supplies the
exact cover `{001,110}`.

For \(A\oplus I_b\), every nonzero maximal minor is a maximal minor of
\(A\) times the identity determinant.  The index and infeasible parity
component therefore persist for every `b`.  The finite verifier constructs
these block matrices and checks `b=0,...,4`; the general statement follows
from the block-diagonal proof.  The theorem correctly calls the identity
summands dummy neutral capacity, not literal four-flag reset blocks.

### 2.5 Protected DM circuit descent: PASS

The potential is now the protected rank

\[
 \nu_P(B)=|F_P|+\nu(G_B^P),
\]

where forced transition edges are retained and their endpoints and conflicts
are removed before the residual matching is computed.  Therefore reaching
`W` gives a perfect matching which extends the protected reset bank, rather
than an unrelated perfect matching.

The local augmentation certificate is also correctly strengthened: a full
maximum matching of the old residual graph must survive in the new graph
before an augmenting path proves a rank gain.  Retaining only its edges
outside the circuit support would not suffice.  The finite descent and the
load/union-bound lemma then follow directly.  Orbit-count recouplings remain
insufficient unless they lift to literal resource-zero circuits on this
protected face.

### 2.6 Conditional absorber theorem: PASS

Theorem 6.1 now quantifies one common ticket mode `mu`.  The same `P_mu`
must satisfy ROTS legality and reset conditions, define the residual literal
matrix and demand used for cone and lattice membership, and be the protected
bank embedded in the starting decorated table for the circuit branch.
Fractional orbit feasibility is used only when the contracted bank remains
invariant under the quotient subgroup; otherwise literal fractional
feasibility is required.

On that one face, normality or either structured integral face yields a
semigroup representation.  Alternatively, the protected circuit theorem
constructs a perfect transition matching from the supplied decorated table.
Reinserting the same protected columns gives the joint master by the
skip-port equivalence.

## 3. Corrections required during the audit

The initial draft was not accepted unchanged.  The audit required:

1. one common ticket mode for cone and lattice, supported by the exact
   determinant-two counterexample;
2. the full cokernel with its free part, rather than assigning every ticket
   delta to a finite quotient without a span hypothesis;
3. a fixed bulk catalogue, jointly realizable ticket tuples, and explicit
   mode-dependent-matrix scope;
4. a residual-symmetry qualification before orbit feasibility is lifted;
5. protected matching rank and survival of the entire old maximum matching
   in the circuit certificate;
6. an actual block-diagonal direct-sum replay and dummy-capacity scope;
7. the exact-table, four-label transparency, endpoint distinction, and
   post-deletion retest in the central bi-packing insertion; and
8. actual short-row footprint rather than block count in the K19/K21 scalar
   corollary.

All eight corrections are present in the audited theorem hash above.

## 4. Finite replay and scope

The verifier reports `PASS` and independently confirms:

* no integral even-parity cover and half-weight fractional feasibility;
* maximal-minor gcds `2` before and `1` after the odd bridge;
* direct-sum index `2` and infeasibility for `b=0,...,4`;
* exact equality of skip-port and master arc selections on the tiny test;
* determinant `-2` and zero integral semigroup representations in the
  common-mode counterexample.

The script is a finite replay of these certificates, not a computational
proof of the matroid, Hoffman, or all-k circuit hypotheses.  Those parts were
audited from their proofs and assumptions.

This note proves no ROTS supply, no K19/K21 generator-ticket bank, no
unit-normality theorem, and no literal circuit abundance theorem.  The
restricted Boolean `C10` Smith-two example gives compatible evidence that a
literal nested state catalogue can carry the same residue obstruction, but
it is not a full K11, K19, or K21 no-go.  No new K17 nested-address search was
performed.

**Final verdict:** PASS for the exact reformulations, conditional rounding
theorems, and stated scope.  The live Boolean gate remains the construction
of a common protected K19/K21 mode satisfying the literal cone/lattice row
and either unit-normality or protected DM-circuit supply.
