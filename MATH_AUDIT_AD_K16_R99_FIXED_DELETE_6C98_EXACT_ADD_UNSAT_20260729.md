# AD independent audit: the fixed-delete `6c98` exact-add UNSAT

Date: 2026-07-29  
Scope: solver-free audit of one fixed radius-99 delete-branch cut.  This note
does **not** prove that the delete branch, or radius 99, is infeasible.

## 1. Frozen objects and verdict

The audited cut is the 99-edge subset with value digest

```text
6c98aa96b824b580be70fb9bab617e80fef233b4bf11b33a7a83adce5d9c39b4.
```

The fixed-add DIMACS file has SHA-256

```text
fbcbace828f3aad11e61291e4244a51a23adedee384182a8ec5ea26eefc67dfc
```

and header `p cnf 9938 19816`.  The independent verifier

```text
scratch/audit_ad_k16_r99_fixed_delete_6c98_unsat_core_20260729.py
```

reconstructs all 19,816 clauses, in order, from the frozen source factor,
cut, and quotient catalogue.  Its output is

```text
scratch/ad_k16_r99_fixed_delete_6c98_unsat_core_20260729.audit.json
```

with file SHA-256

```text
e964098bf5ffb69843b9cbd7f4da1f24ebd5718bbd721dd5244d11a9f7ae20f5
```

and embedded payload digest

```text
fec33ab4f3cf6d60b037c57bbb49199d02707e8d888efd6b56231c25f058c438.
```

**Verdict.**  The fixed `6c98` cut admits no loopless off-source addition set
that restores quotient degree exactly and covers both quotient q1 palettes.
This conclusion has a direct three-portal proof and therefore does not depend
on trusting the unproved `cadical195` summary.

## 2. Exact reconstructed model

The source has 858 loopless quotient edge orbits.  The cut consists of 99
pairwise endpoint-disjoint source edges.  Consequently:

* precisely 198 quotient nodes lose one unit of degree;
* the permitted add domain is every loopless off-source seam whose two
  endpoints are among these 198 nodes, exactly 1,448 seams;
* every active node has an exact-one add constraint;
* summing those 198 constraints forces exactly 99 additions;
* 68 lower-q1 and 70 upper-q1 rotation-colour rows lose every retained source
  provider and receive a positive provider clause.

The remaining 8,490 variables are the sequential-counter auxiliaries.  The
counter clauses encode exact-one correctly: the at-most-one counter records
whether a prefix contains at least one or at least two selected seams and
forbids the final `at least two` state; the second counter is the exact prefix
OR and forces its final state true.

The 35-edge joint matching in
`scratch/k16_r99_joint_matching_delete_20260729.audit.json` is only a hint and
metadata.  No clause forces any of those edges.  Thus the UNSAT is not an
artifact of freezing the preliminary double-repair matching.

If SAT, the model would give an equivariant spanning physical 2-factor with
both q1 palettes.  It does not impose quotient or physical connectedness,
unit voltage, residence, or any q>=2 shadow condition.  UNSAT of this weaker
model is therefore sufficient to reject the fixed cut.

## 3. The four-row core

The reported deletion-shrunk q1 core has indices

```text
112, 113, 121, 136
```

among the 138 lost q1 rows.  All four are upper rows.  Independent catalogue
and DIMACS reconstruction gives the following exact provider graph.

| upper colour | usable off-source provider seams (endpoint nodes) |
|---|---|
| `(1,1883)` | `4737:92-576`, `4740:92-617`, `18552:499-576`, `18555:499-617`, `21385:576-617` |
| `(1,1907)` | `18171:490-611`, `18172:490-617` |
| `(1,3255)` | `21408:576-638`, `21411:576-754` |
| `(1,5939)` | `22529:611-663`, `22530:611-739` |

Their unique source providers are, respectively,

```text
4742, 22511, 23229, 24034,
```

and all four source providers belong to the cut.

### Theorem 3.1 (literal three-portal obstruction)

Let an add set obey the exact degree-restoration rows for the fixed `6c98`
cut.  It cannot cover all four upper colours listed above.

#### Proof

Every provider in every one of the four rows is incident with at least one
node in

```text
P={576,611,617}.
```

Each node of `P` lost exactly one source edge, so exact restoration permits
altogether only

```text
d(P)=1+1+1=3
```

selected seam incidences at `P`.  A selected seam has exactly one upper
colour, so it can cover at most one of the four distinct required rows.  Four
selected providers would therefore require at least four incidences at `P`,
contradicting `d(P)=3`.  ∎

Equivalently, the forcing chain is transparent: the third colour consumes
node 576; the fourth consumes node 611; the second must then use its
`490-617` provider; every provider of the first colour meets 576 or 617.

The local four-row conflict is deletion-minimal by literal endpoint-disjoint
choices.  On omitting the four colours in table order, choose respectively

```text
{18172,21408,22529}, {4740,21408,22529},
{4737,18172,22529}, {4740,18171,21408}.
```

Each triple covers the other three colours and has six distinct endpoints.
This proves deletion-minimality only of the displayed local portal conflict;
it does not prove that each triple extends through the rest of the 99-edge
perfect matching.

This also explains why the preceding same-palette **union-of-endpoints**
closure can miss the conflict: the decisive set is a vertex cover of every
provider edge, not the union of all provider endpoints.

## 4. A globally valid cut-only Benders row

The local proof can be projected back to source-cut bits without retaining the
entire `6c98` assignment.

### Theorem 4.1 (provider-cover Benders inequality)

Let `F` be a loopless source factor.  Fix one palette and a set `T` of palette
colours having unique source providers `f_c in F`.  Let `S` be a quotient-node
set meeting every loopless off-source provider seam of every `c in T`.  If a
source cut `x` admits loopless off-source exact degree restoration and restores
all colours in `T`, then

```text
sum_{f in F} |ends(f) intersect S| x_f
    >= sum_{c in T} x_{f_c}.                         (4.1)
```

#### Proof

The right side counts exactly those colours in `T` whose unique retained
source provider was cut.  Each such colour needs a selected off-source
provider seam.  Distinct colours require distinct seams within one palette.
Every such seam meets `S`, so charge it to one selected incidence at `S`.
Exact degree restoration supplies precisely the left-side number of available
incidences at `S`.  No incidence can receive two charges because a selected
edge consumes its endpoint capacity.  This proves (4.1).  ∎

For the four core colours, an exact 26-node provider cover is

```text
S={97,208,403,485,502,521,541,546,576,581,600,606,611,
   615,617,619,620,623,667,751,757,758,759,761,832,852}.
```

Its value digest is

```text
6ea4d37d689dba187904f8f7a6b0653f092ff3c809cc8bb307f153a005977b37.
```

For each colour, the 36 providers form the complete graph on its nine facet
nodes.  Deleting the unique source provider leaves `K_9` minus that edge.  The
four chosen vertex covers omit, respectively,

```text
{92,499}, {490}, {638,754}, {663,739}.
```

The audit checks every one of the 140 off-source provider edges literally.
On the `6c98` cut, `S` meets the active endpoint set only in
`{576,611,617}`.  Thus the two sides of (4.1) are 3 and 4, and the row rejects
the candidate by one.

The candidate-weight cover cost 3 is exact.  For colour `(1,1883)`, provider
edges `92-576` and `499-617` are disjoint, so any cover costs at least two
active nodes.  For colour `(1,5939)`, edge `611-663` is endpoint-disjoint from
both and forces a third.  The displayed `S` attains that lower bound.

After moving the right side to the left, the row has 52 nonzero coefficients
on the 858 source-cut bits: 3 coefficients `-1`, 47 coefficients `+1`, and 2
coefficients `+2`.  Its signed support digest is

```text
35770364d98f106d480240f5e49f55f52d668264793fbfea3e7d5e26fbbf973e.
```

This row is strictly more reusable than a 99-bit assignment no-good.  It is a
single-palette, full-provider, exact degree-capacity cut; it is not another
copy of the joint-double-cover layer.

## 5. Exact separator normal form

The reusable row family has a compact exact separation ILP.  At a candidate
cut, give node `v` cost equal to its lost degree `d_x(v)`.  For every lost
source-unique palette colour `c`, introduce `t_c`, and for every quotient node
introduce `p_v`.  Solve

```text
maximize  sum_c t_c - sum_v d_x(v) p_v

subject to p_u + p_v >= t_c
           for every loopless off-source provider seam uv of c,
           p_v,t_c in {0,1}.
```

A positive objective supplies `T={c:t_c=1}` and
`S={v:p_v=1}`, hence a violated inequality (4.1).  The `6c98` witness has
objective at least `4-3=1`.  This is the correct strengthening exposed by the
fixed-add conflict: arbitrary provider vertex covers, rather than static
all-endpoint unions.  No claim of total unimodularity or polynomial-time
separation is made.

## 6. Provenance and certificate hygiene

The tiny solve summary

```json
{"solver":"cadical195","sat":false,"seconds":0.011141300201416016,
 "vars":9938,"clauses":19816,"maxrss_kb":26112,"model":null}
```

does not embed the CNF digest, command line, solver-binary digest, raw solver
transcript, or DRAT/LRAT/FRAT proof.  Standing alone it is not a checkable
UNSAT certificate.

The four-row artifact pins the CNF digest and records 209 external Kissat
calls, but it used no guarded assumptions and retained all degree clauses.
Consequently:

* it is a deletion-shrunk q1-row core, not a cut-assignment assumption core;
* its claim that deleting any one of the four rows makes the entire degree
  base SAT is an unproved external-solver transcript (no four witnesses are
  saved);
* it is explicitly not a proof of minimum core cardinality;
* none of those gaps affects Theorem 3.1, which proves the four-row UNSAT
  directly.

The earlier build auditor pins the generator but not the imported catalogue
library, and its catalogue digest omits explicit lower/upper labels (although
those labels are deterministically derived from the stored edge masks).  The
new verifier additionally pins the current library SHA-256

```text
4e86c8621f682a2df2a3721008e6a4b95c8623a9f3e69a8f32b930241938e2c6
```

and reconstructs every q1 row from the physical edge masks.

## 7. Exact boundary

Proved:

1. the frozen DIMACS is exactly the stated fixed-cut degree-plus-both-q1
   model;
2. the preliminary 35-seam matching is not forced;
3. the four listed upper rows plus the three portal capacities are already
   inconsistent;
4. inequality (4.1), instantiated by the 26-node cover, is a globally valid
   cut-only Benders row and rejects `6c98` by one.

Not proved:

1. infeasibility of any other radius-99 cut or of the delete branch;
2. deletion-minimality of the four-row core relative to the entire saved
   degree CNF (the saved transcript reports it, but no SAT witnesses exist);
3. completeness or tractability of the provider-cover separator family;
4. connectivity, voltage, residence, or deeper-shadow feasibility for any
   cut that passes this row.
