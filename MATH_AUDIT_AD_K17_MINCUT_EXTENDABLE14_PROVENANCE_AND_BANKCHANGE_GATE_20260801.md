# AD audit: the `k=17` all-minimum-cut extendable-14 gate

Date: 2026-08-01  
Status: independently replayed exact finite theorem for the frozen SCD owner
forest.  This note audits only the minimum-residence-cut / existing-piece
rank-ten support relaxation.  It is not a path, compiler, or `nu(17)` theorem.

## 1. Frozen objects and provenance

The canonical owner-component input is

* `scratch/threadA_k17_m9_scd_lower_compiler_20260801/components.tsv`,
  SHA-256
  `dc4557fb557dccb87bec15476e11b81655d17c6c6c5295b020fec95adbcb47ef`.

The audited atlas source and frozen stdout are

* `scratch/audit_k17_min_cut_alternative_provider_atlas_20260801.cpp`,
  SHA-256
  `07fd078c2a127cc66bf6331ef72aa936f4141e0c6dbe12ab267d771135c19d7b`;
* `scratch/k17_min_cut_alternative_provider_atlas_20260801.stdout.txt`,
  SHA-256
  `270005e6ac00d93d1cbe37857f2e96b102cf4ec8e9dcdfc4afc88f7fac82fce6`.

I compiled that current source and ran it on the canonical owner input.  The
recomputed stdout was byte-for-byte equal to the frozen stdout.  In
particular, this authenticates the numerical theorem below even though the
historical run log is incomplete.

The surviving tables used downstream have hashes

| table | SHA-256 |
|---|---|
| `patterns.tsv` | `790a3e4292eae6fdb68c1618c05c09c444c82f706bda3bb4bef785763feb143e` |
| `segments.tsv` | `e4ceaa36f504086f1ecdadba4b2d3feebabda34865d3fe611272e2201fab8678` |
| `states.tsv` | `fe7f8390aad61357ebd7313d250f404fa1c50470a67963f483cc7626560fe7c0` |
| `extendable_arcs.tsv` | `9ef66394ffc8c40a04292e836c02fa4838c395c3b338b41908ae994e3555f2c2` |
| `robust_arcs.tsv` | `1e34eaf63f12de7b42d2e6f723333757763717ea3c554250e31ada9fe482d9e1` |

The resource log
`scratch/k17_min_cut_alternative_provider_atlas_20260801.resource.txt`
(SHA-256
`2af267e02844edae154c53fb6dd2b90271f58cba1c7552c69e9eca0b90afa9a9`)
records only

```text
/dev/shm/k17_alt_atlas scratch/components.tsv
```

The named input is not present, and a two-argument invocation cannot have
emitted the TSV tables, because table emission is guarded by `argc==3`.
Moreover, the directory contains duplicated prefixed/unprefixed tables but
no `k17_alt.extendable_arcs.tsv`.  Thus the table directory is not supported
by one atomic historical command manifest.  The byte-identical replay above
rescues the stdout theorem; the displayed table hashes freeze the actual
surviving downstream inputs.

## 2. Exact relaxation

For each original owner component `c`, let `H_c` be its complete family of
minimum interval-stabbing cut patterns.  A pattern `H` partitions `c` into
owner segments.  Each segment has two orientations.

The atlas contains every ordered pair of distinct oriented segments which

1. has Johnson-adjacent endpoint owners;
2. if both segments come from the same original component, occurs together
   in at least one minimum pattern of that component; and
3. passes the following necessary depth-three extendability test at the
   seam.

For every coordinate, an endpoint one-run of total length below four is
allowed only if at least one incident segment is all-one in that coordinate,
so that a later seam may extend the run.  If neither incident segment is
all-one, the short run is already bounded by zeros inside those segments and
can never be repaired by exterior chronology.  This is exactly the source
predicate `extendable_positive_seam`.

Let `U(c,p)` be the rank-ten colour of the old edge destroyed by a selected
cut `p`.  For `H in H_c`, call `U(c,p)` *individually supported relative to
`(c,H)`* if the atlas contains an extendable seam of colour `U(c,p)` and every
incident segment from component `c` belongs to `H`.  Choices in all other
components remain unrestricted.  Define

\[
 b_c(H)=\#\{p\in H:U(c,p)\text{ is not individually supported relative to }(c,H)\}.
\tag{2.1}
\]

This is a relaxation: it ignores simultaneous choices in other components,
a common orientation per segment, seam degree, colour capacity, connectivity,
and all other resource conflicts.

## 3. Exact extendable-14 theorem

### Theorem 3.1

For the frozen `k=17` owner forest,

\[
 \min_{H\in H_c} b_c(H)=
 \begin{cases}
 1,&c\in\{471,694,779,1000,1187,1209,1282,1574,1587,1630,2177,2276,3210,3293\},\\
 0,&\text{for the other 4,848 components}.
 \end{cases}
\tag{3.1}
\]

Consequently

\[
 \sum_c\min_{H\in H_c}b_c(H)=14.                 \tag{3.2}
\]

One minimizing representative `(component, option, unsupported colour)`
for each exceptional component is

```text
471:0:86735   694:0:31988   779:0:12250   1000:0:79722
1187:0:15070  1209:0:8165   1282:0:19709  1574:0:75693
1587:0:24371  1630:0:32286  2177:0:45903  2276:0:40870
3210:0:57583  3293:0:59815
```

The complete replay census is

| object | count |
|---|---:|
| original components | 4,862 |
| minimum patterns | 8,894 |
| distinct physical segments | 12,672 |
| oriented states | 25,344 |
| possible cut colours | 4,232 |
| raw candidate arcs | 2,005,920 |
| extendable arcs | 554,218 |
| robust arcs | 87,316 |
| extendable-zero possible colours | 243 |
| patterns whose cuts are all individually supported | 8,389 |

#### Proof

The source enumerates every minimum cut pattern and every induced segment,
then every compatible ordered orientation pair.  It computes (2.1) for every
pattern.  The byte-identical replay gives histogram

```text
best_bad_hist=0:4848,1:14
```

and prints precisely the fourteen rows above.  Since other components are
left unrestricted when a row is tested, the atlas is a superset of every
simultaneous global minimum-pattern selection.  Hence a zero here could be
spurious support, but a missing support cannot be created by coordinating
the same existing segments.  This proves (3.1)--(3.2).  `square`

### Lemma 3.2 (rank-ten interval witnesses force their seam colour)

Let `X_0,...,X_t` be a nonconstant owner-simple Johnson interval of rank-nine
sets and suppose

\[
                         \bigcup_{i=0}^tX_i=U,
 \qquad |U|=10.                                    \tag{3.3}
\]

Then every adjacent pair in the interval has union `U`.

#### Proof

Equation (3.3) implies `X_i subseteq U` for all `i`.  Two distinct rank-nine
subsets of one ten-set omit two distinct elements, so their union is the
whole ten-set.  Consecutive owners in an owner-simple Johnson interval are
distinct.  `square`

### Corollary 3.3 (existing-piece chronology no-go)

The 19,448 original edge-union colours are pairwise distinct.  Therefore a
selected cut colour has no surviving internal occurrence.  If a global
ordering of the selected existing pieces supplied that colour by a longer
interval, Lemma 3.2 would force an immediate seam of the same colour.  Any
globally depth-three-resident seam necessarily passes the extendability
predicate used by the atlas.  Theorem 3.1 therefore implies:

> Every choice of one minimum residence pattern per component leaves at
> least fourteen distinct selected rank-ten targets which no ordering and
> orientation of those existing pieces can realize.

In particular, at least one *bank-changing* operation is necessary: an
extra cut/resegmentation, an inserted owner macro, a changed owner bank, or
another mechanism that creates new endpoint states.

This strengthens a mere one-seam statement: for rank ten, a longer interval
cannot evade the missing immediate seam colour.

## 4. What lower bound follows, and what does not

The unconditional conclusion is only

\[
   \boxed{\text{minimum-cut existing-piece chronology is impossible; at
   least one bank change is required.}}                \tag{4.1}
\]

There is no audited implication `at least fourteen extra cuts`.  One extra
cut can change more than one endpoint state, while a compound macro can
create several providers at once.  The atlas does not price such operations.

For the restricted repair family consisting solely of target-specific
compact L3 facet sockets

\[
          U-v_0,\ U-v_1,\ U-v_2,\ U-v_3,             \tag{4.2}
\]

the three internal seams all have colour `U`.  Under the additional rule
that one selected socket is charged to and repairs only its displayed target
`U`, the fourteen targets in Corollary 3.3 require at least fourteen such
sockets.  This is a conditional target-specific socket count, not an extra-cut
bound and not a claim against a multi-target macro.

The preliminary representative-socket census which totals 28 extraction
cuts is likewise only about one fixed representative choice for the fourteen
rows; it is not a WLOG optimum over all patterns or all macro families.

## 5. Stronger existing exact-19 support closure, with provenance caveat

A stronger, already existing support-only master couples all component
patterns and support arcs.  It proves optimum nineteen omitted cut colours
inside the `(pattern, existing extendable arc, optional shared orientation)`
relaxation:

* budget 18, mode 0: CNF SHA
  `86c2cf2dea93049e10fd08f25ce90033526af3535a7f4bd8523e9111b1369202`,
  DRAT SHA
  `0227734d919488dadc54e3d013b4d6f92052d33bb00894355bb0c757c1409ce5`,
  checker transcript SHA
  `5883c92f00e2a32dac8a1d355421cfefd0d755852a6a223f75ef52b066cf68fc`;
  the transcript reports `s VERIFIED` for 265,918 variables and 521,959
  clauses;
* budget 19, mode 1: CNF SHA
  `44e6cf9a9b8d92b4825cffb5bd8f45a9737c87bb06ebdf1705c4f7fd486a0edb`,
  map SHA
  `9a7ca77adbb71bcfe2caed5f8c2d0d812a1d7e5da637eed833a5b668f56a845e`,
  SAT output SHA
  `dbf4371446bb11c4df7d13a85ef47932de391fecb18082c4d1dd7045eda60125`,
  literal-CNF/pattern replay SHA
  `7ad1690488a04edc51fe26ce657ca173a58bfc1c96238bb8f2ffbafc52fe984b`.

Thus the frozen formulas have a valid DRAT refutation at 18 and a literal
SAT model at 19.  The SAT replay selects 4,862 patterns, 1,419 cut colours,
4,773 positive arc variables, and nineteen residual masks; mode 1 also has
a common orientation bit assignment.

The proof/model bundle does **not** contain an atomic source/input/command
manifest.  The current builder
`scratch/build_k17_allmin_support_closure_cnf_20260801.cpp` (SHA
`9d1fbffb4d9235214fc5cf901629570ce053517151cbce1bd154f6407dce0fa0`)
and verifier
`scratch/verify_k17_allmin_support_closure_model_20260801.cpp` (SHA
`a8aef70e06d777615ed55b40b0be56312f40796191948da87a28616d33767654`)
postdate the frozen formulas, and an independent audit explicitly declines
to claim them as the formulas' source lineage.  Accordingly:

* the CNF/DRAT and CNF/SAT statements are cryptographically frozen and
  internally replayed;
* identifying those variables with the authenticated geometric atlas still
  relies on the documented but not hash-manifested generation lineage.

The exact-19 result is therefore the authoritative stronger existing
support-closure result, but it should be cited with that provenance caveat
until a fresh hash-bound regeneration reproduces the formulas or their
semantic optimum.

Even with perfect provenance, exact 19 remains a support-relaxation theorem.
Mode 1 imposes no endpoint degree, colour capacity, connectivity, common
run-age chronology, ranks 11+, or lower compiler.

## 6. Scope boundary

Proved here:

1. the current atlas source exactly reproduces the frozen numerical stdout;
2. the all-minimum existing-piece rank-ten support relaxation has the exact
   componentwise lower bound 14;
3. the rank-ten interval lemma upgrades atlas absence to absence of every
   longer existing-piece interval witness;
4. some bank-changing operation is mandatory;
5. fourteen target-specific L3 sockets are conditionally necessary if that
   is the only repair mechanism.

Not proved here:

* fourteen extra cuts, seven extra cuts, or any other cut-count lower bound;
* joint attainability of the componentwise fourteen;
* a physical path or cycle, ranks 11+, lower compilation, or a universal
  literal OR word;
* semantic rederivation of the exact-19 CNFs from one frozen generation
  manifest.

No handoff or research-index file was edited by this audit.
