# Native compact-owner CNF for the peeled `k=15` Hall-29 architecture

Date: 2026-07-28

## 0. Scope

This is a native `-O3` C++ implementation of the positive, sufficient-only
owner architecture in
`scratch/k15_h29_one_owner_cia_audit.json`.

It encodes exactly:

- 1,489 frozen target-to-cell owner pairs;
- 35 residual targets;
- 4,057 retained residual target-to-cell options on 3,183 cells;
- exactly one option for every residual target; and
- at most one residual target on every physical cell.

The executable does **not** freeze the H29 chronology.  In a live search it
consumes signed dynamic literals `Q[p,x]` from a native chronology channel.
The fixed-H29 run below is only an independent regression fixture.

SAT is a genuine matching of the complete 1,524-target H29 DM shore inside
this peeled architecture.  UNSAT remains scoped to the architecture and the
base chronology CNF supplied to the executable.

## 1. Direct fixed-mask CNF

For a cell `(start,depth)` and constant target mask `T`, put

\[
 E=\bigcup_{p=start}^{start+depth}Q_p.
\]

In the interior,

\[
 M=E\setminus(Q_{start-1}\cap Q_{start+depth+1}),
\]

with the one-sided boundary versions already proved in the compiler audit.
Exact fit is

\[
 T\subseteq E,\qquad M\subseteq T,\qquad
 Q_p\cap T\ne\varnothing\quad(start\le p\le start+depth).
\]

The native emitter expands this directly, with no envelope or mandatory
auxiliary variables:

1. for `x in T`, one clause `OR_p Q[p,x]`;
2. for `x not in T`, every envelope source implies the applicable blocker
   on the left and/or right;
3. for each `p`, one clause `OR_{x in T} Q[p,x]`.

For a residual option, `not claim` guards every clause.  Frozen pairs are
unconditional.  Sequential at-most-one encodings are used for target and
cell rows.

## 2. Interface

Build:

```text
c++ -std=c++20 -O3 -DNDEBUG -Wall -Wextra -pedantic \
  scratch/k15_compact_owner_cnf.cpp \
  -o scratch/k15_compact_owner_cnf
```

Run:

```text
scratch/k15_compact_owner_cnf \
  BASE.cnf Q.map OWNER.flat OUTPUT.cnf CLAIM.map [Q.values]
```

`Q.map` is dense and signed:

```text
K15_QMAP_V1 6438 15
<15 signed DIMACS literals for p=0>
...
<15 signed DIMACS literals for p=6437>
END
```

The literals must be distinct base-CNF variables.  `OWNER.flat` is produced
deterministically by `scratch/export_k15_compact_owner_flat.py`.  The output
is a complete DIMACS file obtained by appending the native owner clauses to
the supplied base CNF and rewriting the header.  `CLAIM.map` maps every new
claim variable to its constant target and authoritative cell index.

The native chronology generator still has to supply the dynamic `Q` map.
Python is allowed only to serialize payloads and decode certificates.

## 3. Exact regressions

### 3.1 Known raw fixed points

`scratch/export_raw_fixedpoint_owner_fixture.py` independently extracts the
first-occurrence owner map and erosion truth from the previously verified raw
fixed-point words.  The same native predicate gives:

| case | frozen owners | native truth fits | Kissat |
|---|---:|---:|---|
| `k=11,d=3` | 1,023 | 1,023 | SAT |
| `k=13,d=3` | 4,095 | 4,095 | SAT |

Strict DIMACS audits:

- `k=11`: 5,115 variables, 41,224 clauses, 84,631 literals;
- `k=13`: 22,347 variables, 186,193 clauses, 386,633 literals.

### 3.2 Frozen H29 chronology

The current audit payload has SHA-256

```text
721a67896e5f992945cb0adabcb47fff94cdfe1c2d993b347270b03a1b7f35f4
```

On the fixed H29 `Q` truth table, the independent native evaluator reports:

```text
frozen fits                 1489 / 1489
residual exact-fit options    12
residual targets with fit     12
distinct residual fit cells    6
```

This is exactly the six-cell / twelve-edge residual kernel from the degree-
one peeling audit.  Consequently the combined fixed-H29 instance is UNSAT,
and Kissat returns exit code 20.

The emitted fixed-H29 formula has:

```text
104675 variables
350198 clauses
805948 literals
```

including 96,570 unit clauses that freeze the regression `Q` table.  The
owner layer itself has 253,628 clauses and 709,378 literals.

## 4. Files and hashes

```text
d909b392c4ba29cb4b447a6dac967c1e6449a87ae920a077487a987cd94a3698  scratch/k15_compact_owner_cnf.cpp
d11acb25cc9794ea0440cebdf29055ab935843455aa476ff49547a97c228ffb9  scratch/k15_compact_owner_cnf
a326aab8149c6d521704ca152a616785d809d55bc80170b385b585763dc3dbc5  scratch/export_k15_compact_owner_flat.py
407e5d13e4dbf806c6bff9696fc40214ecb83d11ea338c4e50e22508fbf2d4f9  scratch/export_fixed_word_q_fixture.py
7d83d0a259aff7e011d6731beadfa61b8053a7ae2491f977810a66ffa541d569  scratch/export_raw_fixedpoint_owner_fixture.py
9a9edd9c8d55b9a551b03cc1437476cc29dd4fb6cff8bbc8fee52e7a5f6d2dc6  scratch/k15_h29_one_owner.flat
41b46bed20af45fd2a4ee24cfe8434a5d022ae9d1b5c635c2deb0654f4bb920e  scratch/k15_h29_fixed_owner.emit.json
83faed7a3c3fdfa0e2d7963689293b3747f7cb71f53727a2f61ecd15c919d82b  scratch/k15_h29_fixed_owner.cnf
4b44945b8f2cd19b0f5a94dec406e79d4b3dad6cd3b59127ecfbc9414927eb12  scratch/k11_raw_owner_regression.emit.json
7e13ec4058c0b873454b36b1b0ad13d4cb3a33084017f25ccd24b428a0d6ea82  scratch/k13_raw_owner_regression.emit.json
```

## 5. Remaining performance gate

The Python CP-SAT bottleneck has been removed from the owner predicate.  The
remaining native task is the chronology/radius base CNF: choose one Hamilton
path in the five-parent successor union, expose its ordered middle masks, and
emit the 96,570 dynamic `Q[p,x]` literals consumed here.  Once that interface
exists, the complete peeled search can run under Kissat with Python used only
for launch and certificate audit.
