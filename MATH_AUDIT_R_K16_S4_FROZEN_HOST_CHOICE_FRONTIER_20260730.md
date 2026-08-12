# Independent audit: frozen S4 tri-window host-choice frontier

Date: 2026-07-30  
Lane: R  
Verdict: **PASS, with the scope correction stated in Section 1.**

## 1. Exact scope

The audited object is the frozen S4 self-pair word

\[
[4\text{ free}]+P[6:6436]+[9\text{ free}]
+(0x8000\vee P[7:6432])+[5\text{ free}],
\]

where `P=k15seed_4.word`.  The collar positions are

\[
\{0,1,2,3\}\cup\{6434,\ldots,6442\}
\cup\{12868,\ldots,12872\}.
\]

This is an exact OR-collar countermodel and calibration instance.  It is **not**
an equality-valid repeat-free parent pair: seed 4 has a repeated rank-seven
trace.  Nothing below proves a length-12873 word or promotes S4 to one of the
twelve valid repeat-free provenance pairs.

## 2. Independently authenticated input

The independent checker authenticates and uses:

| file | SHA-256 |
|---|---|
| `frozen_atlas/k15seed_4.word` | `57a8370c1df54e2f79eb3af269f57b3b9840546cbb6c4862d6cf2adbcd94b2ae` |
| `frozen_atlas/lead_score2.cells` | `ddc6675f0e5a3946e215bfdd389732b5965829d643c83772fe8b4218150133ad` |
| `frozen_atlas/lead_score2.word` | `598e31a5dbec81df3e2dc1a8447e4697109850e480ba41a2cb86013715c38760` |
| `frozen_atlas/model.map.json` | `fc2c4f185e294b963c391af56379e4dfbfbf9655a2b7457aa798a7d854ff73f2` |

It reconstructs the 12,873 cells directly from the parent and 18 collar
cells and obtains the frozen word byte for byte.

## 3. Fixed-only facets

### Proposition 3.1

Each of the three named masks has exactly one literal interval in the frozen
word, and that interval is wholly inside the fixed lower body:

| target | assembled interval | cells |
|---|---:|---|
| `0x4c71` | `2300..2302` | `0x4421,0x0010,0x0c61` |
| `0x4879` | `5581..5583` | `0x0808,0x0050,0x4021` |
| `0x4c39` | `6243..6245` | `0x4029,0x4c21,0x4810` |

Consequently arbitrary changes to the 18 collar cells cannot erase these
three witnesses.

### Audit proof

For every start position the checker accumulates the interval OR and stops as
soon as it contains a bit outside the target.  This monotone stopping rule is
complete.  Exactly the three rows above survive, one for each target, and no
row meets a free position.

## 4. The complete 69-row semantic atlas

The two fixed bodies cover exactly 65,466 of the 65,535 nonzero masks.  Their
complement has 69 targets.  For each such target `T`, the checker independently
scans every literal interval meeting a collar cell.  If `F` is the OR of its
fixed cells and `Q` its physical free-cell set, the interval is a semantic
option precisely when

\[
F\subseteq T.
\]

Collapsing intervals by `(T,F,Q)` gives exactly 5,867 options.  The independent
scan has zero omitted and zero extra options relative to `model.map.json`.
The frozen incumbent realizes 77 of these options and misses exactly

\[
S=0x31ce,\qquad L=0x7bce.
\]

There are 79 options for `S` and 83 for `L`.

## 5. Exact maximal-core lemma

For a selected family of semantic options

\[
\mathcal W=\{(T_i,F_i,Q_i):i\in I\},
\]

define, for every incident free cell `p`,

\[
C_p=\bigcap_{i:p\in Q_i}T_i.
\]

### Lemma 5.1

The selected options have a simultaneous nonzero cell assignment if and only
if

1. `C_p` is nonempty for every incident `p`; and
2. for every `i`,
   \[
   F_i\vee\bigvee_{p\in Q_i}C_p=T_i.
   \]

### Proof

Necessity follows because every feasible cell at `p` must be a nonzero subset
of every incident target, hence a subset of `C_p`.  Thus the union attainable
by option `i` is bounded above by the expression in (2).

Conversely assign the literal mask `C_p` to every incident cell.  Condition
(1) makes every assigned cell nonzero; by definition it is a subset of each
incident target.  Condition (2) then realizes every selected interval
exactly.  Unused collar cells may be assigned any nonzero value.  This proves
the integral criterion without SAT or relaxation.

## 6. Exact provider-pair displacement theorem

Call an `(S,L)` option pair compatible when it passes Lemma 5.1.  For such a
pair `P`, call a currently covered residual target `T`
**incumbent-displaced** when every incumbent-realized option of `T` fails
Lemma 5.1 after adjoining `P`.

### Theorem 6.1

Among the `79*83=6,557` raw provider pairs:

- exactly 5,692 are compatible;
- every compatible pair incumbent-displaces at least three of the other 67
  residual targets;
- exactly nine pairs attain three.

The nine pairs form the Cartesian product of the following three small and
three large options:

| target | shape | fixed OR | physical free positions |
|---|---:|---:|---|
| `0x31ce` | 36 | `0x0000` | `{6437,6438,6439}` |
| `0x31ce` | 68 | `0x0000` | `{12871,12872}` |
| `0x31ce` | 69 | `0x0000` | `{12872}` |
| `0x7bce` | 2 | `0x0000` | `{0,1,2}` |
| `0x7bce` | 3 | `0x0000` | `{0,1,2,3}` |
| `0x7bce` | 133 | `0x6308` | `{0,1,2,3}` |

For small shape 36 the displaced set is

\[
\{0x73cc,0xb0cc,0xb0ce\};
\]

for small shape 68 or 69 it is

\[
\{0x3cc8,0x3ce8,0x73cc\}.
\]

The complete displacement histogram over all 5,692 compatible pairs is in
the audit JSON.  Its entries sum to 5,692.

### What the lower bound means

It proves that any completion using one of the two-hole provider pairs must
abandon incumbent hosts for at least three protected residual targets.  It
does **not** say that three new hosts suffice for the entire 69-row system.
It is unrelated to the number of maximal complement runs, whose minimum is
one in the separate geometric decomposition.

## 7. Immediate Hall and positive checks

For every one of the nine attaining pairs:

- each of the three displaced targets has at least 44 individually compatible
  semantic alternatives (the exact counts range from 44 to 76); and
- the two hole options plus one alternative for each displaced target pass
  Lemma 5.1 jointly.

Thus there is no singleton empty-list obstruction at the three-compensator
level, and the five selected rows themselves have an integral common core.
This is a genuine positive local substructure.

There is no informative ordinary target-to-option Hall test here: semantic
option variables are target-labelled, so distinct targets do not compete for
an option vertex.  The obstruction, if any, is the higher-order intersection
of their cell caps.  The positive five-row checks do not decide whether one
can choose compatible hosts for all remaining 64 protected rows.  That is the
precise surviving host-choice problem.

## 8. Artifacts

- `scratch/audit_r_k16_s4_host_choice_frontier_independent_20260730.py`  
  SHA-256 `ebf76071c15d5f09eb75262aba4830dcbc864b6b3f558276a4ccc3162d485931`
- `scratch/k16_triwindow_s4_495_lead_20260730/frozen_atlas/host_choice_frontier.independent.audit.json`  
  SHA-256 `f374631a9b4ccac3a543758a5d8ba060f1efb5a1fb40898d597b396e9ce5681c`  
  payload SHA-256 `f9befe5a29e8d6b020ba2ebf6fbbd9c7e830abd87ed1faaaad9516ec3ddd7bbd`

The checker used 1.17 wall seconds and negligible memory locally.  No SAT,
finite search over cell assignments, or remote computation was used.
