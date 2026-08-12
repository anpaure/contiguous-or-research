# Strict-spiral run/quotient/compiler atlas at `k=9,11,15`

Date: 2026-07-29

Status: search-free exact audit.  This note proves two normal-form lemmas,
records the raw solution data in one reproducible format, and isolates a
finite move obstruction.  It does **not** produce a `k=15` word.

Machine-readable atlas and generator:

```text
scratch/audit_strict_spiral_solution_atlas_20260729.py
scratch/strict_spiral_solution_atlas_20260729.json
```

The JSON contains the complete ordered run/gap sequences, both residue
permutations, all quotient deletion/insertion edges, erosion load profiles,
and compiler candidate-degree histograms.  The prose below reports only the
structural comparison.

## 1. Frozen inputs and scope

| case | authoritative input | SHA-256 | status |
|---|---|---|---|
| `k=9` | `scratch/fixtures/k9_strict_spiral_optimal_128.word` | `0f282a2c...` | exact optimal word, independently covers `511/511` |
| `k=11` | `scratch/sigma_sat_k11_465.word` | `746b469a...` | exact optimal word, independently covers `2047/2047` |
| `k=15` | `scratch/fixtures/k15_residence_hint_explicit_v1.json` | `4482c3d4...` | resident strict spiral only; not a solution |

The `k=9` fixture is a byte-identical import of
`/Users/amir.nuriyev/Downloads/opusproblem/work/k09_equi_new.word` (mtime
2026-07-28 23:18:15 +0500).  Its second derivative is the external
`k9_cycle.json` up to cyclic offset three.

The carrier `T` is reconstructed as `D^d A` for the two words and from
explicit `(lower,a,b)` choices for `k=15`.  Before any statistic is accepted,
the script proves:

```text
|T|=W, every T_i has rank r, all T_i are distinct,
T is cyclic Johnson, its q1 intersections are all distinct,
T_(i+N)=rho^v(T_i) for one unit voltage v.
```

The voltages are respectively `4,2,1`.

## 2. Forced data versus free data

Let `c_i=1[0 in T_i]`, `N=W/k`, and let `v` be the strict-spiral voltage.
Then

\[
 x\in T_i \quad\Longleftrightarrow\quad
 c_{,i-(xv^{-1}\bmod k)N}=1.                 \tag{2.1}
\]

Thus one cyclic binary trace determines the whole carrier.

For a rank-`r` Johnson strict spiral with exact lower `q1`, the following are
forced:

1. `c` has exactly `N` one-runs;
2. its run starts modulo `N` form a permutation of `Z_N`;
3. its run ends modulo `N` form a permutation of `Z_N`;
4. every residue class modulo `N` has exactly `r` ones;
5. the run lengths sum to `rN`, and the gap lengths sum to `(k-r)N`.

What remains free is precisely the ordering of the two permutations, the
integer lifts giving the run/gap compositions, the quotient deletion and
insertion chronology, every erosion load below `q1`, and the compiler
incidence geometry.  The atlas labels these rather than treating them as
new invariants.

## 3. Exact comparison

| statistic | solved `k=9` | solved `k=11` | resident seed `k=15` |
|---|---:|---:|---:|
| `N` | 14 | 42 | 429 |
| minimum run / required | `3/3` | `4/4` | `4/4` |
| maximum run | 12 | 14 | 32 |
| maximum gap | 16 | 14 | 44 |
| q2 missing target orbits | **0** | **0** | **47** |
| q2 maximum-load target orbits | **1** | **1** | **18** |
| depth-`d` missing physical targets | **0** | **0** | **165** |
| zero-degree forced-port compiler targets | **0** | **0** | **165** |
| balanced two-run end swaps | 12 | 53 | 898 |
| swaps retaining middle/q1 injectivity | **0** | **0** | **0** |

The full erosion load spectra are:

```text
k=9,  q2: 1^45  2^36  3^3
k=11, q2: 1^209 2^110 3^11
k=11, q3: 1^11  2^55  3^55 4^44
k=15, q2: 0^685 1^2475 2^1575 3^270
k=15, q3: 0^165 1^795 2^930 3^735 4^315 5^63.
```

The q2 maximum-load cells in each solved case form exactly one translation
orbit: the exceptional size-three orbit represented by `{0,3,6}` at `k=9`,
and the size-eleven orbit represented by `{0,1,3,5}` at `k=11`.  The `k=15`
seed spreads maximum load over 18 orbits while leaving 47 q2 orbits empty.
This is a genuinely free difference: rank, residence, run transversality,
and q1 are already exact in all three cases.

The long-tail difference is real but secondary.  The `k=15` trace has much
larger maximum run/gap and quadratic energies, yet it has *more* small-cell
ports, not fewer: each coordinate has 112 singleton ports, versus 6 at
`k=9` and 13 at `k=11`.  All 15 singletons and all 105 pairs occur as
mandatory port masks at `k=15`.  Hence its current compiler failure is not a
scarcity of singleton/pair opportunities.

## 4. Forced-port theorem and the exact `165`

Write the cyclic Johnson transition as

\[
T_{i+1}=T_i-\{\alpha_i\}+\{\beta_i\}.
\]

If `D^d A=T`, then every two-sided interior source letter satisfies

\[
 \{\alpha_i,\beta_{i-d-1}\}\subseteq A_i.       \tag{4.1}
\]

Call the left side `F_i`, and put

\[
 P_i=T_i\cap T_{i-1}\cap\cdots\cap T_{i-d}.
\]

Residence gives `|P_i|=h=r-d`, and (4.1) gives `F_i subseteq P_i`.
In the fixed-envelope compiler, a low target `S` can be placed literally at
`i` exactly when

\[
 F_i\subseteq S\subseteq P_i.                  \tag{4.2}
\]

At terminal rank `|S|=h`, (4.2) collapses to `S=P_i`.  Consequently the
candidate degree of a terminal target is **exactly its depth-`d` erosion
load**.  This proves, without a solver, that the 165 missing rank-five sets
in the `k=15` seed are exactly the 165 zero-degree compiler vertices.  No
choice of one-core or matching can repair them while the carrier is fixed.

For the two solved inputs, every forced-port candidate degree is positive.
The raw compiled words also pass the linear form of (4.1) at every position
where both boundary transitions exist.  At `k=9`, one rank-three target is
not a literal source letter and is supplied by the exact `d=2` deeper-row
compiler; this cleanly distinguishes forced-port feasibility from the
stronger pure-literal model.

## 5. An exact move theorem—and why two runs are insufficient

Unwrap the `N` trace runs in cyclic order as intervals `[s_i,e_i]`.  Keep all
starts fixed.  Choose two runs `i,j` and new ends `e'_i,e'_j` such that

```text
e'_i mod N = e_j mod N,       e'_j mod N = e_i mod N,
e'_i+e'_j = e_i+e_j,
e'_a-s_a+1 >= d+1,           s_(a+1)-e'_a-1 >= 1.
```

### Lemma 5.1 (balanced endpoint swap)

Such a swap preserves the multiset of run-start residues, the multiset of
run-end residues, every class sum, total rank, Johnson adjacency, q1 rank,
and residence.  It may fail only the global orbit-injectivity conditions:
distinct middle masks and distinct q1 masks.

*Proof.* Starts do not move.  End residues are exchanged.  The zero-sum
condition preserves the number of ones, so the common residue-class sum is
unchanged.  The two inequalities preserve residence and nonempty gaps.
The run-transversal normal form then gives rank and Johnson adjacency.  None
of these local conditions prohibits two quotient columns from becoming
rotation-equivalent.  □

The exhaustive atlas census finds `12,53,898` legal balanced swaps at
`k=9,11,15`, respectively—and **zero** remains a strict injective carrier.
Every collision count is a multiple of `k`, as equivariance predicts.  At
`k=15`, one exceptional swap preserves the entire q1 rainbow but duplicates
one full orbit of 15 middle masks; most duplicate both ledgers.

This is useful negative structure.  A run-algebra optimizer based on one
end-swap at a time cannot move inside the strict-carrier state space.  The
smallest plausible repair is a collision-neutral *multi-run* move.  There is
an exact parameterization: choose a cycle `sigma` on at least three run
indices, require

```text
e'_i mod N = e_(sigma(i)) mod N,       sum_i e'_i = sum_i e_i,
```

and keep every new endpoint inside its residence/gap interval.  The proof of
Lemma 5.1 applies verbatim: this cyclic end permutation preserves all eager
run algebra.  A 3-cycle is therefore the first genuinely new scalar move;
its three orbit-collision signatures can cancel even though no transposition
does.  The quotient-dual version is an alternating Johnson-edge circuit.

The correct finite objective for such a circuit is not residence—it is
already safe—but the vector

\[
(\Delta\text{middle orbit loads},\Delta\text{q1 orbit loads},
  \Delta\text{q2 loads},\Delta\text{q3 loads}).              \tag{5.1}
\]

A useful circuit has its first two coordinates zero and transfers load from
the 18 triply loaded q2 orbits (and other repeated orbits) into the 47 holes,
while also eliminating the 11 q3 holes.  This is the deterministic move
class suggested by the solved atlas.  It is strictly smaller and safer than
free bit annealing, but genuinely larger than the now-refuted two-run lane.

## 6. Claude-folder recent-delta audit

At 2026-07-29 05:52 +0500, the only substantive files newer than the prior
05:44 snapshot were:

```text
/Users/amir.nuriyev/Downloads/opusproblem/work/GENERAL_CONSTRUCTION.md
  mtime 05:47:45, SHA d8d5b0276b7c...
/Users/amir.nuriyev/Downloads/opusproblem/work/LEDGER.md
  mtime 05:48:29, SHA 1ccd4d1ac089...
```

Files at 05:52 were Python bytecode caches only.  No new `k=13` or `k=15`
solver certificate appeared.

The new documentation records three useful ideas: the row-capacity gate
refinement, the general bit-level `sandwich2.py` compiler, and the
run-transversal c-space model.  The saved positive artifacts support only:

1. the new strict-spiral `k=9` optimum above;
2. `/Users/amir.nuriyev/Downloads/opusproblem/work/k13_flat.word` (mtime
   00:41:15, SHA `011a32e8...`) independently covers `8191/8191` at length
   1719, but its third derivative has one bad cyclic seam and no strict
   spiral voltage.  It is an alternative exact optimum/compiler result, not
   a strict `k=13` carrier certificate;
3. no `k=15` pass.  `k15_cpsat_local.log` remains 89 bytes with mtime
   00:54:47.  The docs themselves still call decorated `k=15` open and quote
   the stale bound 6459; the repo-authoritative bound is 6458.

The ledger's assertion that every missing q2 orbit has 36 candidate sites is
not accompanied there by a saved audit artifact, so this note does not use it
as proved evidence.

## 7. Reproduction

```bash
python3 scratch/audit_strict_spiral_solution_atlas_20260729.py
shasum -a 256 \
  scratch/audit_strict_spiral_solution_atlas_20260729.py \
  scratch/strict_spiral_solution_atlas_20260729.json
```

Current hashes:

```text
b7133dd474c2cff65d43319cf4b7cd7e6a1f9d7213bc74ddfd57e8486d581ad2  script
5f93128a40da68473690e4e84960d4f0fdfe988f00b2c5cc84f4582da9986240  atlas
```
