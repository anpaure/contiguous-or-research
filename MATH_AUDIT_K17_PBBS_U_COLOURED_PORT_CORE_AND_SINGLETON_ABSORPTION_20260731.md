# K17 PBBS-U coloured-port cores and the singleton absorption

## Scope

This note audits the final stitching gate for two independently produced
two-dead-port PBBS-U factors.  It separates three logically different
conditions:

1. pairwise Johnson/residence-safe endpoint compatibility;
2. a colour-distinct perfect matching of all physical ports except the two
   intended path ends;
3. one globally residence-safe Hamilton path.

The two old factors fail already at (2).  The failure is not a subtle
multi-seam `010/0110` effect.  A lossless two-donor absorption removes the
smaller obstruction and produces a new factor which passes (2) and has SAT
models for the exact four-state DFA degree cover.

## 1. Independently checked common invariants

Both old inputs have 737 nonempty components partitioning all 5,005 rank-nine
subsets of `[15]`, complete internal coverage of every rank 10--15 target, no
internal `010` or `0110`, and 4,268 distinct internal rank-eight intersection
colours.

| factor | SHA-256 | compatible port edges | dead ports |
|---|---|---:|---|
| greedy absorption | `0bcd678828c8d258b6976aa2831a250dd3650c395bf9d3864df1415ee5961a6b` | 7,013 | `(599,1),(734,0)` |
| alternate absorption | `9d93b190bfd88bac5f6945ba281aaeace38fbe3f68bb1b24e6e2a6651e526e01` | 7,155 | `(195,0),(417,1)` |

The larger raw edge count of the second factor is misleading.

## 2. Exact coloured-port formulation

Make one Boolean variable for each compatible seam between two physical
ports.  Require exactly one chosen seam at every non-dead port and at most one
chosen seam of each rank-eight colour.  This is exactly the degree-cover gate:
it allows one forced-endpoint path and any number of cycles, so its
unsatisfiability is stronger than failure of Hamiltonicity.

The independently emitted pairwise CNFs are:

| factor | variables | clauses | CNF SHA-256 | DRAT core |
|---|---:|---:|---|---:|
| `0bcd...` | 7,013 | 108,065 | `e68c222b1991c1953a6a55296fe32ec936488562f6dd9033674a1f07a8860dab` | 11 clauses |
| `9d93...` | 7,155 | 112,462 | `927fc2ee5c2562037efefe25fa3c04795b4c3e5e4c0fe0ce7cf1cc5b8b39fea4` | 6 clauses |

Both proofs replay as `VERIFIED` under `drat-trim`.

## 3. Human core for `0bcd...`: two ports, one colour

Component 498 is the singleton word

```text
0x667a
```

Its two physical ports have the following six seam variables:

```text
port 996:  1959, 6011, 6200
port 997:  1960, 6012, 6201
```

Every one of the six seams has intersection colour `0x663a`:

```text
0x66ba -- 0x667a
0x663b -- 0x667a
0x667a -- 0x6e3a.
```

Each port requires a seam, hence at least two of the six variables must be
true.  Colour simplicity permits at most one.  This is the entire
contradiction.  The extracted 11-clause core is just the two three-variable
port clauses plus the required pairwise colour exclusions.

This gives a useful absorption invariant.  For every component which is not a
path endpoint, the union of the compatible-colour sets of its two ports must
have size at least two.  More robustly, run unit propagation on the coloured
port instance after every absorption and reject any move which empties a port.

## 4. Human core for `9d93...`: a forced-port cascade

Port 739 has the unique seam 5379, so it consumes port 965.  This deletes
seams 6232 and 6233.  The two ports 1454 and 1455 of singleton component 727
then force seams 132 and 133.  Both use physical port 17 (and also share colour
`0x5c66`), which is impossible.

Thus the 7,155-edge factor is worse conditioned than the 7,013-edge factor:
it fails even without colour-at-most-one clauses, whereas `0bcd...` has an
uncoloured degree cover and fails only at the one-colour singleton.

## 5. Full four-state DFA audit

The exact engine is

```text
scratch/solve_k17_pbbs_u_hamilton_cegar_20260731.py
SHA-256 ac56ec51c705a981738cc085ec60084d45a6576216eece06a08ec8625fd67e25
```

Its four states are the longest suffixes in `{epsilon,0,01,011}`.  Exhaustive
truth-table replay agrees with direct forbidden-subword evaluation; reversal
is handled by applying the same transition function to the explicitly
reversed component.  The selected-orientation equations give exactly one
incoming and outgoing arc, except for the unique start/end, colour AMOs are
global, and each subtour cut forbids one exact selected directed cycle.

The round-zero CNFs also have independently verified DRAT proofs:

| factor | variables | clauses | CNF SHA-256 | proof SHA-256 |
|---|---:|---:|---|---|
| `0bcd...` | 118,453 | 795,444 | `0dfed3dd69b4727a2ba2a5038e9cfbac88eadeb737fdf008f6e1a1ce0f00d914` | `679dae6901fd28dc9ac55d8f1131a3e8d680cd59de85cfe899db64d529a84c0c` |
| `9d93...` | 118,166 | 790,843 | `88998459ff2000beeda1fec9685a870140d702365b6659aac28782e756c85602` | `dd95b5255c8d927f8ffa855575625a8554dea85cfbfa5e5f12e123dff99556b3` |

Since the tiny port cores already imply UNSAT, the DFA clauses are not the
cause in either case.

## 6. Lossless repair of the better factor

Absorb singleton `0x667a` between two internal neighbours:

```text
0x6772 -> 0x667a -> 0x663b.
```

The new colours are `0x6672` and `0x663a`; the donor cut frees `0x6672`.
The exact census finds 243 structurally valid two-donor absorptions, of which
166 are lossless for the complete upper palette.  The deterministic first
choice above reduces the component count from 737 to 736 and produces

```text
scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments
SHA-256 3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465
```

The new coloured-port CNF is SAT.  The exact four-state DFA CEGAR also returns
SAT degree covers; its first five decoded rounds have respectively

```text
path 551 + 7 cycles
path 474 + 6 cycles
path 240 + 8 cycles
path  75 + 6 cycles
path  40 + 6 cycles.
```

Those are not yet a Hamilton certificate, but they prove that the former
degree-cover obstruction has been removed.  The remaining operation is sound
subtour elimination on this repaired factor.

## 7. Recommended absorption score

Raw endpoint-edge count should not be optimized.  Use the lexicographic gate

1. exactly two dead physical ports;
2. no component whose required ports see fewer than two colours;
3. coloured-port unit propagation reaches a fixpoint without an empty port;
4. the coloured degree-cover CNF is SAT;
5. maximize path size / minimize subtours under the exact DFA.

The two failed factors distinguish steps 2 and 3 sharply, while the repaired
factor reaches step 5.

## 8. Coloured-Hall cut theorem

Let (G=(P,E)) be any physical port graph, let (R\subseteq P) be the ports
which must be saturated, and give each seam (e) a colour \(\chi(e)\).  A
*rainbow degree cover* is a set (M\subseteq E) with

\[
 \deg_M(p)=1\quad(p\in R),\qquad
 |M\cap\chi^{-1}(c)|\leq 1\quad(c\in\chi(E)).
\]

**Theorem 8.1 (seam-independent coloured Hall).**  If (X\subseteq R) is
independent in (G), then every rainbow degree cover satisfies

\[
 |X|\leq |\chi(\delta(X))|.                 \tag{8.1}
\]

Indeed, the selected edge incident with each (p\in X) is distinct because
no edge has two ends in (X).  Rainbowness then injects these (|X|) edges
into their colours in \(\chi(\delta(X))\).

For the two ports of a nonendpoint component, write (C_0,C_1) for their
available-colour sets.  Since the port graph has no self-component seams,
(8.1), together with the singleton port cuts, gives the necessary score

\[
 h=\min\{|C_0|-1, |C_1|-1, |C_0\cup C_1|-2\}\geq0.       \tag{8.2}
\]

This is a necessary preprocessing cut, not a sufficient degree-cover
criterion.

For component 498 of `0bcd...`, (C_0=C_1=\{\mathtt{663a}\}), so (8.1)
reads (2\leq1).  More precisely, if (A=\{a_1,a_2,a_3\}) and
(B=\{b_1,b_2,b_3\}) are its two port banks, the complete core is

\[
 (a_1\vee a_2\vee a_3),\quad(b_1\vee b_2\vee b_3),\quad
 (\neg a_i\vee\neg b_j)\ (1\leq i,j\leq3).                \tag{8.3}
\]

These eleven clauses are deletion-minimal: deleting a port clause permits a
single edge from the other bank, while deleting the (ij)-th cross clause
permits (a_i=b_j=1).  Thus the obstruction is a coloured-Hall/partition-
matroid cut, not an uncoloured Tutte obstruction.

## 9. Exact two-donor absorption theorem for this atlas

In the `0bcd...` atlas take component 31 at zero-based position 6,
component 498, and component 463 at position 0.  Their marked cells are

\[
 P=\mathtt{6772},\qquad S=\mathtt{667a},\qquad Q=\mathtt{663b}.
\]

Replace the three source components by the nonempty old left suffix and the
merged component

\[
 F_{31}[0..6]\;S\;F_{463}[0..].                           \tag{9.1}
\]

**Proposition 9.1.**  Construction (9.1) is an exact lossless absorption:

* it partitions the same 5,005 rank-nine states;
* it has 736 components rather than 737;
* every internal edge is Johnson and there is no internal `010` or `0110`;
* its 4,269 internal rank-eight colours are distinct; and
* all 4,944 old-coordinate masks of ranks 10 through 15 remain covered by
  internal intervals.

The only replaced old internal colour is
(P\cap F_{31}[7]=\mathtt{6672}).  The two inserted edges have colours

\[
 P\cap S=\mathtt{6672},\qquad S\cap Q=\mathtt{663a},       \tag{9.2}
\]

so colour simplicity gains exactly one edge.  The remaining assertions,
including losslessness of arbitrary-width upper coverage, follow by literal
replay of every component and every interval; they are not inferred from a
local collar approximation.  The resulting byte-exact atlas is
`scratch/k17_pbbs_u_singleton_absorbed_20260731.fragments`, SHA-256
`3b1a277fa10d2152a9f0d217fa9ff47c0a1ce3ca648321f9ac65af289d87e465`.

## 10. Independent semantic replay of the first DFA degree cover

The retained round-zero producer instance has 118,282 variables and 794,240
clauses, CNF SHA-256 `b1e2079d...`.  Its saved model has SHA-256
`c1c2ab6f...`; after solver commentary is removed, the canonical sorted
positive-assignment digest is
`150f2bebb0d5a2540643e62922170ae72e340fcbef31f65bec1f34968a305208`.

An independent verifier imports neither the producer nor a SAT solver.  It
reconstructs (9.1), rebuilds all 1,288 oriented states and 9,188 directed
candidate seams in the producer's deterministic order, decodes the retained
assignment, and directly checks its physical semantics.  The result is:

* 485 forward and 251 reversed component orientations;
* 7,011 physical pair-safe seams, with forced dead ports `(596,1)` and
  `(731,0)`;
* 735 Johnson seams whose colours are distinct and disjoint from all 4,269
  internal colours, hence 5,004 distinct path/factor edge colours;
* one path from component 731, direction 0, cell `09fe`, to component 596,
  direction 0, cell `69ae`, using 551 components and 3,694 cells;
* seven directed cycles with `(components,cells)` equal to
  `(91,504),(43,432),(22,155),(9,130),(8,50),(8,25),(4,15)`; and
* all 11,040 four-state DFA labels replay correctly, the path contains no
  `010/0110`, and every cycle is safe under cyclic replay.

Thus the repaired atlas has a full fresh-colour, four-state-DFA degree cover.
This theorem does **not** claim a 5,005-cell U path: the seven cycles are real.
Nor does it impose the two exterior four-sector collars or the absolute K17
rho-three budget; an open path may end with an unfinished length-one or
length-two run.  Exact subtour elimination followed by literal merged-word
and exterior-collar replay is the remaining gate.

Pairwise seam safety cannot replace that replay.  When a component has fewer
than three cells, `010` or `0110` can span three successive components even
though both adjacent component pairs pass their local collar tests.  Hence
`scratch/k17_pbbs_u_0bcd_pairsafe_degree_sat_20260731.audit.json` is retained
only as evidence about the pairwise degree layer; it is not a residence
certificate.  Every future integrated braid must propagate the four-state
DFA and then scan the materialized word.

The fail-closed independent verifier and payload are

```text
scratch/threadD_verify_k17_pbbs_u_singleton_absorption_degree_cover_20260731.py
  SHA-256 67106066fffaed473252f18274cd699668f73b817e35242ebaa0e0d32fe6cc69
scratch/threadD_k17_pbbs_u_singleton_degree_replay_20260731/independent.audit.json
  SHA-256 2c5c5727386fa3b0044bc6085648922dfa0321544cf3cdad12850991dd6a73fb
  payload af44ee5d8d3d9d508039d9886e9040b4f2592b571210e8cd51e61537adeeb95f
```

It reruns in 1.05 seconds with about 57 MB maximum resident memory on the
local audit host.  This is a semantic certificate of the saved degree-cover
assignment, independent of the CNF builder; the ongoing subtour CEGAR is
deliberately not duplicated here.
