# K16 RF495 oriented-anchor Hall obstruction

Date: 2026-07-30  
Status: unconditional for the authenticated fixed seed-5/self RF495
`4/9/5` fibre.  This is a solver-free fibre theorem, not a global K16 lower
bound.

## 1. Result

The authenticated RF495 layout has eighteen editable cells in three
disjoint interval chains

\[
C_L=\{0,1,2,3\},\qquad
C_M=\{4,\ldots,12\},\qquad
C_R=\{13,\ldots,17\}.
\]

Its two fixed bodies cover 65,465 of the 65,535 nonzero masks.  The complete
literal atlas contains 6,089 potential intervals for the remaining seventy
targets.  Every such interval has nonempty editable support contained in
exactly one of (C_L,C_M,C_R); there are no cross-chain supports.

The main conclusion is:

> **Theorem 1.1 (fixed-fibre no-go).**  No assignment of nonzero values to
> the eighteen editable cells makes the authenticated fixed seed-5/self
> RF495 word universal at length 12,873.

The proof is a deficiency-one Hall obstruction on the residual rank-eight
targets.  It uses the full physical interval endpoints, not quotient support
endpoints and not a SAT verdict.

## 2. Oriented-anchor Hall lemma

Let (w_0,\ldots,w_{N-1}) be one fixed completed word.  Let
\(\mathcal A\) be an antichain of target masks.  Suppose every literal
interval available to a target in (\mathcal A\) is assigned a key
\(\kappa\), with the property that any two intervals having the same key are
nested by containment.

Then every simultaneous realization of (\mathcal A\) induces an injection
from (\mathcal A\) into the key set.  More generally, if (K(T)) is the set
of keys available to (T), then every subfamily satisfies

\[
 |\mathcal X|\leq\left|\bigcup_{T\in\mathcal X}K(T)\right|.
 \tag{2.1}
\]

### Proof

Choose one realizing literal interval for every target.  If two chosen
intervals have the same key, they are nested.  OR is monotone under interval
containment, so their two outputs are comparable by set inclusion.  Distinct
members of an antichain are incomparable, a contradiction.  Thus the chosen
keys are distinct, and ordinary Hall gives (2.1).  ∎

This lemma concerns literal intervals in the common realized word.  Their
bookkeeping decomposition into a fixed OR and editable-cell OR is irrelevant:
nested full intervals still have nested outputs.

## 3. The authenticated oriented anchors

For residual rank-eight provider rows, assign keys as follows.

- A row supported in (C_L) is keyed by its physical **left** endpoint.
  The possible keys are

  \[
  (L,0),(L,1),(L,2),(L,3).
  \]

  The left collar begins at word position zero, so intervals with the same
  key have a common left endpoint and are nested.

- A row supported in (C_M) is keyed by its physical **right** endpoint.
  The possible keys are

  \[
  (M,6434),(M,6435),\ldots,(M,6444).
  \]

- A row supported in (C_R) is also keyed by its physical **right**
  endpoint.  The possible keys are

  \[
  (R,12868),(R,12869),\ldots,(R,12872).
  \]

Intervals with a common right endpoint are nested.  The three key types are
kept distinct.  Thus there are exactly

\[
4+11+5=20                                             \tag{3.1}
\]

oriented anchors.

The complete raw rank-eight layer has 1,770 literal rows, all represented in
the model and all distinct as semantic `(target,fixed OR,Q)` rows.  Their
typed split is

\[
258\text{ left}+1182\text{ middle}+330\text{ right}=1770.
\tag{3.2}
\]

Every row passes the stated anchor classification; there are zero
cross-chain rows and zero nesting violations.  Although middle-chain
endpoints at other ranks can extend beyond 6444, the bound in (3.1) is the
exact rank-eight bound and is not asserted at other ranks.

## 4. Full-fibre deficiency

The seventy residual targets contain the following twenty-one distinct
rank-eight masks:

```text
18e7 19e6 1c67 1e74 1f54 319e 398e
39c6 8b6a 9867 98e6 99c6 9b4a 9b52
9b54 9c63 9e54 9e64 b18e b19c b986
```

They form an antichain because they are distinct and have one common rank.
Every universal completion of the fixed layout must realize all twenty-one:
the fixed bodies do not realize any residual target, and the raw atlas is the
complete census of literal intervals touching an editable cell that could
realize one.

By Section 3, their realizing intervals would inject into only twenty
oriented anchors.  Lemma 2.1 would give

\[
21\leq20,                                             \tag{4.1}
\]

which is impossible.  This proves Theorem 1.1.

## 5. Every proper chain face also has deficiency one

The same argument closes every nonempty proper chain face of the
authenticated lead.  Frozen chains retain their lead values; the table gives
the rank-eight targets still mandatory for the active chains.

| active chains | mandatory rank-eight targets | oriented anchors | defect |
|---|---:|---:|---:|
| left | 5 | 4 | 1 |
| middle | 12 | 11 | 1 |
| right | 6 | 5 | 1 |
| left + right | 10 | 9 | 1 |
| left + middle | 16 | 15 | 1 |
| middle + right | 17 | 16 | 1 |
| all three | 21 | 20 | 1 |

The two-chain obstruction cores are explicitly:

```text
left+right (10):
18e7 19e6 1e74 319e 398e 39c6 8b6a 9b4a 9b52 9b54

left+middle (16):
18e7 19e6 1c67 1f54 319e 398e 39c6 9867
98e6 99c6 9c63 9e54 9e64 b18e b19c b986

middle+right (17):
18e7 1c67 1e74 1f54 8b6a 9867 98e6 99c6 9b4a
9b52 9b54 9c63 9e54 9e64 b18e b19c b986
```

The initially proposed common-right-endpoint argument for `left+right` is
not valid: that face has twelve physical right endpoints for ten targets.
The corrected invariant uses four physical left-start anchors on (C_L)
and five physical right-end anchors on (C_R), giving the sharp (10>9)
obstruction.  The distinction is load-bearing.

## 6. Literal and semantic scope

The raw literal table has 6,089 rows.  Eight duplicate physical intervals
collapse to identical semantic providers, leaving 6,081 semantic rows.  No
collapse occurs in the decisive rank-eight layer, so the proof neither loses
nor invents an endpoint.  It also does not use maximal same-`Q` dominance,
the old sharp-root cuts, the diagnostic `D^3` middle-row equality, or a
solver status.

The theorem closes precisely the authenticated fixed seed-5/self parent,
ordering, fixed bodies, and `4/9/5` collar fibre.  Therefore the unrestricted
RF495 run for this exact fibre is redundant.  It does **not** close another
parent pair, another collar placement, a different literal-word
architecture, or the global question whether `nu(16)=12,873`.

## 7. Authenticated data and replay

Inputs:

```text
scratch/k16_triwindow_rf495_repeatfree_frozen_atlas_20260730/
  host_atlas.audit.json
  residual_potential_literal_intervals.tsv
  residual_witness_incidence.tsv
  lead_score3.cells
```

Input SHA-256 values:

```text
host atlas audit     024b67240db0a98f7c18c43e1c87a85af2d67624c50878e7aa80474f11f95194
literal intervals    c8f7381486c0412f9f3d34a724d6bbfdc60c210fbf1a2bb2aaa647fad3f0e6dc
semantic incidence   a3ca5b14a5e6286cbcb96e6ca3c827979a525f697eabf6f0704c4fcde982113c
lead cells           6f90ca3f682ad1565977d53f0d3a30496ae01f38a7816f411375e5f6b415745c
```

Primary light replay:

```text
scratch/audit_k16_rf495_three_chain_separator_hall_20260730.py
scratch/k16_rf495_three_chain_separator_hall_20260730.audit.json
```

It parses all raw rows, reconstructs every frozen-face mandatory family,
checks every oriented anchor and pairwise nesting class, and records the
deficiency-one certificate for all seven nonempty chain unions.  It performs
no cell Cartesian product and invokes no solver.

```text
primary replay source  bb798d4fcc361811b09798f225f15d4b974bebdbcaf0111be3c5c28adfa2e059
primary replay JSON    b08d43b2e54079fb30612b0c71be5f0494d23248e556315eb7dc03225dd47bd4
```

A separately implemented audit reads the 6,089-row literal table directly,
does not use the semantic table, checks 108,841 same-anchor rank-eight
interval pairs for nesting, reconstructs all seven face target sets, and also
exhibits an eleven-colour assignment showing why the weaker all-right-endpoint
condition does not close `left+right`.

```text
scratch/audit_k16_rf495_oriented_anchor_hall_independent_20260730.py
  SHA 9b536f6a4ac7ff852de7c1e7947919ffa807a9951b2f4075651615b90dc69351
scratch/k16_rf495_oriented_anchor_hall_independent_20260730.audit.json
  SHA b1c1698fa5909babfadec63f4c031fca8b139ba100d3a3fd92c843f70c825b58
  payload 006ab46092f82ecd8ca613caf8789271c0b3734a33bfc6feebcd99f15998d808
```

Both replays return `PASS_SOLVER_FREE_UNSAT` for the full fixed fibre.
