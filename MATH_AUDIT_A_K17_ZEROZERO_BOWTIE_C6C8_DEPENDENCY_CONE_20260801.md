# Audit A: the `k=17` zero/zero bow-tie core and targeted C6/C8 census

Date: 2026-08-01  
Status: exact bow-tie theorem verified; geometric dependency cone verified;
the audited executable still has one false-negative pruning line and is not a
complete census until that line is repaired

This note independently audits

```text
scratch/census_k17_zerozero_bowtie_c6c8_20260801.cpp
```

and the four-seam core stated in

```text
MATH_THEOREM_K17_DENSE_ZERO265_Q1_BOWTIE_UNSAT_CORE_20260801.md.
```

It does not edit or strengthen that theorem note, and it does not report a new
heavy census.  All claims below are source-level or are replayed directly from
the frozen 228,730-seam atlas.

Audited snapshot hashes are

```text
census source  5de11829ee69b567e159e92679795c5961f696405fe1621c22955247804f4bc5
q1 seam atlas  78a8b64767e9d2f2ceec3e6e58d529eafed70e8a47da64239f267e2b07321cdd
core rows      0ba57f56f524c1e9cda3494c4367488ef70e1dacca5b072feb8f0a32f0c9a552
```

A later source with a different hash must be re-audited at least against the
two explicit fixes in Sections 2 and 5.2.

## 1. Exact four-seam replay

In the exported q1 numbering put

\[
 A=1330,\qquad B=7017,\qquad C=2538,
\]

and let `c=984`, `d=999`.  Direct filtering of

```text
scratch/threadD_k17_zerozero_bowtie_q4_20260801/q1.seams.tsv
```

gives exactly the following four rows and no others of colours `c,d`:

\[
\begin{array}{c|c|c|c|c}
 &\text{tail}&\text{head}&\text{colour}&\text{upper}\\ \hline
x&A^+&B^+&c&19326\\
y&C^-&B^+&d&19326\\
z&B^-&A^-&c&19326\\
w&B^-&C^+&d&19326.
\end{array}
\]

Thus each of `c,d` has literal occurrence degree two.

### Theorem 1.1 (minimal bow-tie obstruction)

There is no choice of exactly one `c`-seam and exactly one `d`-seam that
uses one incoming socket, one outgoing socket, and one orientation of the
physical piece `B`.

#### Proof

The exact-colour equations are

\[
 x+z=1,\qquad y+w=1.                                      \tag{1.1}
\]

The `B+` incoming socket and `B-` outgoing socket give

\[
 x+y\leq1,\qquad z+w\leq1.                                \tag{1.2}
\]

Equations (1.1) select two seams in total.  Since the two left sides in
(1.2) partition those four seam variables, both inequalities are equalities.
Consequently one selected seam uses `B+` and one uses `B-`, contrary to
the one-orientation constraint on the same physical piece.  \(\square\)

This proof uses neither an LP nor a SAT solver.  It is also minimal in the
natural sense: deleting a colour equation, a socket-capacity row, or the
orientation-identification row makes the remaining system satisfiable.
All four seams have upper mask 19326, explaining why rank-ten zero-provider
counting does not see this obstruction.

There are two piece-numbering systems in the artifacts.  The exported q1
formula calls the central piece 7017.  The independent dense replay orders
the same physical path as piece 7018, with endpoint-owner anchors 19294 and
19262.  Numeric piece IDs therefore must not be transported between the two
builders.  The current census source correctly resolves the dense central
piece from those two owner masks and verifies that both belong to piece 7018.

## 2. Exact dependency cone

Fix the 7,612 cut lower masks.  For a selected lower colour `R`, every
residual q1 seam of colour `R` has both rank-nine endpoint owners containing
`R`.  A factor incidence switch changes a residual state only in a cut-path
component containing an endpoint of a changed **uncut** incidence.

Let \({\cal P}_{c,d}\) be the old pieces containing at least one owner above
18782 or 19038.  If a switch affects no member of \({\cal P}_{c,d}\), the
union of the affected old pieces contains no owner above either target.  The
reconstructed paths use exactly that same owner union.  Hence no old or new
endpoint in the reconstructed region can support colour `c` or `d`, and
the complete `c,d` provider sets are unchanged.

It follows that a one-switch repair of Theorem 1.1 must do at least one of:

1. alter the physical central path and therefore its orientation/socket row;
2. alter the literal support set of colour (c); or
3. alter the literal support set of colour (d).

This proves the geometric prefilter in `geometric_target`.  The source also
computes the signed support delta on the exact triples

\[
  (\text{tail state},\text{head state},\text{colour})
\]

but the audited snapshot does **not** use that delta in its final filter.
The proof-safe second filter would retain every central-path move or nonzero
`c,d` support delta.  That rule is sound: if both the central orientation row
and the two provider-support sets are unchanged, the four clauses of
Theorem 1.1 remain an induced unsatisfiable subsystem.

This is a dependency-cone theorem only for one C6 or one standard C8, the
fixed cut set and fixed selected colours.  It says nothing about compound
switches, cut relocation, replacing (c) or (d), or a temporary topology
change followed by a second move.

### Executable false-negative

The audited source computes `provider_changed`, but `evaluate` still returns
on

```cpp
if (!central && !gain) return;
```

where `gain` means that the **sum** of the two provider counts strictly
increases.  This is not complete: a count-neutral replacement can change a
provider's socket/orientation and destroy the core.  The line must be

```cpp
if (!central && !changed) return;
```

and aggregate fields `providers18782`, `providers19038`, and `provider_gain`
must remain diagnostics only.  Until that repair is present in the compiled
source and the census is rerun, a zero-survivor conclusion is invalid.

## 3. C6 and C8 catalogue completeness

For standard rank-seven-core C8 switches the in-source enumeration is exact.
There are

\[
 \binom{17}{7}\binom{10}{4}\cdot3\cdot2=24,504,480       \tag{3.1}
\]

oriented keys: the core, four outside labels, one of the three Hamilton
4-cycles modulo dihedral symmetry, and one of the two incidence phases.
The rank-seven core and four-label set are recovered uniquely from a standard
C8; the three arrays in `q4_orders` are exactly the three undirected cycles.
`make_c8` then tests presence of every removed incidence, absence of the
opposite new incidence, and protection of every removed incidence.  Thus it
is complete for this standard C8 class.

The C6 side is not self-authenticating in this source.  `read_moves` verifies
32 columns, sequential IDs, current old incidences, protection, and exactly
46,818 rows, but it does not regenerate all rank-seven cores, label triples,
and phases.  Completeness therefore depends on the separately authenticated
protected-C6 catalogue and its hash.  A production manifest must pin that
input; row count alone is not a completeness certificate.

Neither catalogue covers arbitrary support-four circuits, topology-changing
multi-switches, or higher alternating circuits.

## 4. Fixed-cut path reconstruction

For every moved uncut lower incidence the scorer takes the union of all old
pieces containing `old_owner`, `other`, or `new_owner`; deletes the old edge;
adds the new edge; and rebuilds the resulting maximum-degree-two graph.
The following checks are exact:

* every rebuilt vertex is one of the same distinct middle owners;
* maximum degree is at most two;
* every vertex is reached from an endpoint, so no residual cycle is hidden;
* the number of new paths equals the number of affected old paths; and
* every positive coordinate run bounded internally by zeroes has length at
  least four.

The lexicographic reassignment of new paths to the affected old numeric IDs
is harmless for B, H10 and the three projection matching numbers: all those
objects are invariant under a common permutation of the affected physical
piece labels.  It must not, however, be used to transport a named physical
piece across builders; owner anchors are required for that purpose.

The residence verdict is deliberately **internal D3 only**.  Boundary runs
are exported.  Every regenerated seam is tested by
`relaxed_pair_resident`, which is the exact two-block necessary test but lets
an all-one block export a run through its other boundary.  Consequently the
census does not certify a globally resident cyclic completion.

## 5. Exact meanings of the reported gates

### 5.1 Provider counts

`target_provider_counts` counts distinct directed atlas triples of the two
selected colours.  It does not count selected seams of a cycle cover, and it
does not quotient opposite orientations to physical undirected edges.  The
same physical seam can therefore contribute different directed state
occurrences.  The support-delta field, not aggregate count gain, is the
proof-relevant bow-tie statistic.

### 5.2 `factor_q1_holes`

This is the upper-q1 hole count of the underlying degree-two factor after the
incidence switch, including switched incidences whose lower masks are cut.
The delta formula is exact provided the baseline factor covers every
rank-ten mask.  The imported single-C6 source explicitly asserts this
baseline property; the targeted bow-tie `main` currently does not.  A
proof-safe build must add

```cpp
for (Mask u=0; u<(Mask(1)<<K); ++u)
  if (pc(u)==10) demand(baseq[u]>0,"base factor q1");
```

or else initialize and update the full baseline hole count.  Without that
hypothesis the routine only notices holes on masks with nonzero move delta.
Also, `factor_q1_holes==0` is printed but is not part of
`all_pre_q1_gates`; that is consistent only if q1 is intentionally left to
the next stage.

### 5.3 B and H10

`B=0` means that every physical piece has at least one orientation with at
least one relaxed outgoing and at least one relaxed incoming candidate.
It is a local support row, not common-orientation or coloured-cycle-cover
feasibility.

`H10=0` means that every rank-ten mask has an internal-factor provider or a
relaxed seam candidate after the move.  It does not require the eventual
selected q1 seams to use those providers.  `H10` is also distinct from
`factor_q1_holes`, which concerns the uncut degree-two factor itself.

### 5.4 TH, TC and CH

The three numbers are exact maximum matching sizes in the support
projections tail-piece--head-piece, tail-piece--colour and colour--head-piece.
The multiplicity-aware delta update and augmenting-path recomputation are
sound.  Three perfect projections are necessary but not sufficient for one
common three-resource matching; Theorem 1.1 is precisely such a failure.
Exact q1 SAT (or an equivalent integral three-resource theorem) remains a
separate gate.

## 6. Proof-safe independent replay specification

An independent verifier for a frozen census should:

1. pin hashes of the factor, cut bank, C6 catalogue and produced rows;
2. rebuild all 7,612 paths and the complete relaxed atlas from the raw factor;
3. derive the central path from owner masks 19294 and 19262;
4. assert full baseline factor-q1 coverage and replay the four exact core
   provider triples;
5. regenerate the standard C8 key set and independently regenerate or
   canonical-compare the C6 catalogue;
6. evaluate every move affecting the central path or any old piece containing
   an owner above 18782 or 19038, retaining every nonzero exact provider
   support delta and using no aggregate-count pruning;
7. rebuild the entire switched factor, cut graph and atlas from scratch for
   every reported survivor, and compare the full (c,d) provider sets;
8. recompute factor-q1 holes, path count, internal D3, B, H10 and TH/TC/CH;
   and
9. send every pre-q1 survivor to the exact orientation/colour formula.

Steps 2, 6 and 7 are the expensive part and belong on the H100 CPU.  The
result of a resource exit is `UNKNOWN`, never a negative certificate.

## 7. Audited boundary

Unconditional:

* the frozen q1 atlas contains exactly the four stated core seams;
* the bow-tie is an exact minimal local obstruction;
* the geometric dependency cone and the support-delta replacement rule are
  logically complete for one move on the fixed-cut C6/standard-C8 face;
* the local path, internal-D3, B/H10 and projection computations have the
  scoped meanings proved above.

Conditional or still requiring certificate lineage:

* C6 enumeration completeness requires the authenticated 46,818-row input;
* `factor_q1_holes` requires an explicit baseline factor-q1 assertion; and
* the executable census requires the one-line `gain` to `changed` repair and
  a fresh authenticated rerun;
* a zero count of targeted pre-q1 survivors would exclude only this one-move,
  fixed-cut catalogue, not compound switches or the global `k=17` problem.
