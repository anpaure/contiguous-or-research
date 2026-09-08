# K16 split-pair collar interface: an exact twenty-vertex Hall signature

Date: 2026-07-30  
Status: **proved finite reduction; fail-closed audit implemented**

## 1. Frozen obstruction

The union of the eight exact, arbitrary-upper-complete split-pair carrier
incidence graphs has canonical alternating shore

```text
|U| = 20, |R| = 9, deficiency = 11.
```

It decomposes into eleven independent connected components

```text
|U_i| = |R_i| + 1.
```

Eight components are isolated zero-degree targets; the other three have
sizes `3->2`, `5->4`, and `4->3`.

## 2. Collar signature

For every physical proper-prefix cell `v` in a resulting collar chronology,
define its signature

```text
Sigma(v) = {u in U : v can host lower target u}.
```

The signature is computed after all source rows have been removed and all
collar rows inserted.  Hence:

- a lost source cell contributes no right vertex;
- a retained source cell whose envelope or mandatory mask changed uses its
  new signature, not its old signature;
- a new collar cell contributes one right vertex of capacity one, regardless
  of how many components its signature meets.

Let `Q(Sigma)` be the bipartite graph with left shore `U`, one right vertex
for every physical cell with nonempty signature, and edge `u--v` iff
`u in Sigma(v)`.

## 3. Necessary-and-sufficient criterion

> **Collar signature theorem.** The resulting collar saturates all eleven
> frozen deficient components if and only if
>
> ```text
> nu(Q(Sigma)) = 20.
> ```

Equivalently, for every `X subseteq U`,

```text
#{physical cells v : Sigma(v) intersects X} >= |X|.
```

This is exactly Hall's theorem applied after source-cell losses, so it is
both necessary and sufficient and depends only on the cell signatures.  It
requires neither SAT nor physical-move enumeration.  Since `|U|=20`, it is a
tiny exact matching audit.

The scalar count `29 >= 11` for a nineteen-row collar is only necessary:
cells have unit capacity, some may have empty signature, and lost source
cells or competing component supports can consume the apparent surplus.

## 4. No-loss component quotient

The audit independently verifies a stronger property of each of the eleven
frozen components: adjoining one new right cell to **any** one of its left
vertices makes that component perfectly matchable.  Thus, when all nine old
shore cells and their signatures are unchanged, the theorem simplifies:

> Build a bipartite graph from the eleven component-demand tokens to the new
> collar cells, joining a component to a cell when that cell's signature
> meets the component.  The collar closes the obstruction iff this quotient
> graph has a matching saturating all eleven demand tokens.

After any source-cell or source-edge loss this simplified component-touch
test is not sound; the exact twenty-vertex signature matching must be used.

## 5. Calibration on exact_229

Carrier `exact_229` itself has only eight physical cells touching `U`.  Its
signature matching is

```text
8 / 20, deficiency 12.
```

The full generalized graph has matching

```text
26307 / 26332, deficiency 25.
```

This differs from the union lower bound eleven because the union contains
incidences drawn from seven other, mutually incompatible carriers.  A collar
survivor must therefore pass both gates:

1. the twenty-vertex signature matching, which proves it has paid the frozen
   eleven-component obstruction including all source losses;
2. the complete 26,332-target generalized Hall matching.

Only a full-Hall-zero survivor is eligible for compilation and literal
65,535-mask replay.

## 6. Audit interface

The auditor reconstructs the eight basis incidence graphs, verifies the
`20->9` shore, the eleven deficiency-one components, and the any-single-port
property.  With `--candidate`, it then:

- reconstructs every resulting physical cell signature on `U`;
- reports gained, lost, and changed signatures relative to `exact_229`;
- computes the exact twenty-vertex matching and canonical witness;
- computes the complete generalized Hall matching and witness.

This is the proof/audit lane for every S4/H2 collar output.  Physical search
is deliberately outside its scope.

## Artifacts

```text
scratch/audit_k16_splitpair_collar_hall_signature_20260730.py
SHA256 d4b7283feb8d511c1a6578726645d9fa2f33ea29213e10ba5a4650c7c94f6c3e

scratch/k16_splitpair_collar_hall_signature_20260730/
  collar_signature.base.audit.json
SHA256 94b325c211ee4d0119c25ea1c4d37c59e654e34177b195ab130a4963ae17051d
payload a3f17ab44e3e0c35f02c620c8e91ecb7e7e8f440687bb0e46eb2a385c528ce4c

scratch/k16_splitpair_collar_hall_signature_20260730/
  collar_signature.exact229.audit.json
SHA256 8e2e14e1b7fd0cd476fadf274d5aad5a151207e59e1723bfdfd0be60cba22a9e
payload dfc9ac8e9fa3b662040c380796a7b3b94f27fba9babb20c959e0ba1fad3bc400
```
