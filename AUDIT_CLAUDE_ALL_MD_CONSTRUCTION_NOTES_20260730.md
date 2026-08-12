# Complete audit of Claude's Markdown construction notes

Date: 2026-07-30  
Scope: every `.md` file under
`/Users/amir.nuriyev/Downloads/opusproblem/work`, read completely.

## 1. Exhaustive manifest

Exactly seven Markdown files were present:

| file | lines | SHA-256 |
|---|---:|---|
| `BIWORD_ENGINE_AUDIT_20260729.md` | 270 | `9a274784e0d7eb4b6f9d857e7cedb9a2b985c4a8e422a0c5050b1ba3de625a3f` |
| `GENERAL_CONSTRUCTION.md` | 520 | `2c235216b696735775cf4f0fdb5a596128a3363a7df7daafce3af705fce8206d` |
| `LEDGER.md` | 2416 | `eca012f2131967bc4b16661e5be61150d47b0e9118befecaf599a06b19a59212` |
| `ODD_TWO_EXISTENCE_REDUCTION_20260730.md` | 222 | `7e95dcd5b7aa677b6caee7de2b5d7554c07b7115ed0f85c88970b542bdeb3c64` |
| `OVERHEAD_FORMULA_NOTES_20260730.md` | 81 | `f3875fad04198d4b453324d7387438f1916a5ddf7d6260c94ad3ad64235d3d5c` |
| `THEORY_SYNTHESIS_20260730.md` | 66 | `dcd0c4d0899e8610994dd6d5154ee02265cd30f88fb87c0c0e3f6684a60cb6ee` |
| `WEDGE_SPILL_NOTES_20260730.md` | 162 | `bdcc69f8b049b97e51a45f22d879b7953eccfe259c8f9dd8ef78df8e43454f84` |

This audit concerns the notes.  It does not claim that every Python/C++
program in Claude's directory has been line-audited.

The ledger was reread after its final 45-line append.  That append records
the validated positive K10 cut-to-compiler chain, the failure of the cheap
braided-complement generalization at K10/K12/K15, the negative
affine/quadratic height-function probes, and Claude's final ranking of the
odd multi-spiral, even-K, and K17 construction problems.

## 2. Construction facts that survive reconciliation

### 2.1 Carrier/compiler separation

The carrier-to-word formulation is exact once all interfaces are included:
middle ownership, residence, upper survival, boundary handling, and the
literal lower COMP_d/Hall system.  The saved compilers are strong positive
oracles: a compiled word is independently replayable.  Failure of a
restricted one-core or sandwich catalogue is not automatically a complete
negative oracle unless the note proves that catalogue complete.

### 2.2 Multi-component odd architecture

The `k=13` and `k=15` optima really use two components before opening, while
`k=11` has a one-component spiral.  Dropping connectivity during factor
construction and restoring it at the seam is a genuine reusable mechanism.
The c-space/permutation parametrization is an effective coordinate system,
not yet an all-k existence proof.

### 2.3 Even bilayer normal form

The `(c,t)` class sums, generalized start/end transversality, residence, and
two simultaneous layer bijections give a sound sufficient equivariant
normal form.  The BIWORD audit correctly distinguishes permanent exact
middle/q1 rows from capped q2/upper heuristics and distinguishes carrier
PASS from compiler PASS.  No K16 existence theorem follows from a stalled
CEGAR run.

### 2.4 Direct raw-splice route

Raw words formed from two K15 bodies and free collar cells do not need a
flat carrier or residence proof.  A literal SAT completion at length 12,873
is sufficient.  The fixed seed5/self `4/9/5` fibre is now closed by the
later oriented-anchor Hall theorem, but seed1/self, other trims, two-parent
layouts, punctured bodies, and interleaved architectures are outside that
scope unless separately decided.

## 3. Claims in the notes which must not be used as theorems

### 3.1 Unrestricted wedge kill shape

`WEDGE_SPILL_NOTES` and Sections 4/6 of `GENERAL_CONSTRUCTION` and
`ODD_TWO_EXISTENCE_REDUCTION` claim that a killed wedge is governed only by
one-sided rank-`r+2` three-ORs.  This is false without an additional global
hypothesis.  The project has an explicit odd-middle `J(9,5)` rank-`r+3`
counterexample which suspends to every larger odd-middle rank.

The corrected theorem is the fixed-width outward-ray classification in
`MATH_THEOREM_R_PROTECTED_WEDGE_RAYS_AND_PRODUCT_SPILL_20260730.md`.

### 3.2 COMP_d automaticity

The `81/81`, `11/11`, `24/24`, and `8/8` compile data are compelling finite
evidence.  They do not prove that every positive-slack admissible opening has
a feasible COMP_d system.  The lower Hall quantifier remains part of the
general theorem.

### 3.3 Two-existence reduction

`ODD_TWO_EXISTENCE_REDUCTION` is conditional, not a completed reduction to
two already-proved existence statements.  Its E2 wedge argument uses the
false unrestricted kill-shape lemma, and its final compiler step is measured
rather than universal.  The corrected interfaces are: assigned fixed-width
support, seam/socket existence and residence, upper repair, q1 boundary SDR,
and lower COMP_d Hall.

### 3.4 Splice overhead formula

`OVERHEAD_FORMULA_NOTES` is an excellent diagnostic decomposition of rescue
capacity, punctures, head/tail demand, flats, stalls, jumps, and ghosts.  Its
formula is conjectural.  Double-duty collar cells explicitly defeat the
naive additive lower bound, so only the complete finite fibres or a new
non-double-counting theorem can decide the K16 overhead.

### 3.5 Architecture classification

Known even optima are heavily interleaved.  Therefore even a complete UNSAT
classification of all h=1 doubled-splice fibres would not prove
`nu(16)=12874`; it would redirect the SAT search to interleaved factors.

## 4. New synthesis obtained from the complete read

The corrected fixed-width theorem leaves an `O(k)` list of possible lost
outward-ray targets after cutting a wedge.  Those targets are not unrelated:
they form one nested ray tower.  Root's
`MATH_THEOREM_ROOT_FIXED_WIDTH_WEDGE_SEAM_RAY_ABSORPTION_20260730.md`
proves the following stronger interface.

Cut the right wedge flank, giving start `S`, end `E`, and wedge union
`U=E union S`.  If the incoming endpoint `B` of the preceding opened
component satisfies

```text
B union S = U,
```

then every selected fixed-width witness crossing the cut is recreated by
the seam interval `B,S,...` at its original depth.  Hence all upper depths
are repaired simultaneously.  Under an assigned fixed-width tower, the
upper-SPILL gate becomes a directed facet-socket cycle problem on component
openings.

This theorem is currently under independent audit.  Even if sound, it does
not prove socket-cycle existence, seam residence, q1 boundary eligibility,
or lower compiler Hall.  It does, however, identify a substantially sharper
general construction target than an unstructured zero-SPILL inequality.

## 5. Resulting priorities

1. Decide the direct seed1/self 18-cell raw-splice fibre with independent
   literal replay.
2. Search matching-protected carrier moves only when they preserve the full
   lower matching, not a fixed shore score.
3. Prove or refute the facet-socket cycle lemma for protected two-component
   factors and audit the all-depth seam absorption theorem.
4. Keep lower COMP_d Hall separate until a universal theorem is proved.
5. Preserve an interleaved even-K search lane; do not equate splice UNSAT
   with global K16 optimality.
