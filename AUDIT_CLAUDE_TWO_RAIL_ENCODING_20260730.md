# Audit of Claude's two-rail reduction and encodings

Date: 2026-07-30

Audited source directory:

`/Users/amir.nuriyev/Downloads/opusproblem/work`

The inspected source hashes are:

| file | SHA-256 |
|---|---|
| `railanat.py` | `40a47606b290e7d63faf27d7a9b0d69b9febd2f5d1f597e0bd4bac10998ecfdc` |
| `rbexact.py` | `75e2e7c14a43bc5302b7c0a59557b31cb23d3d032069d77b143bb51e8c43db3c` |
| `rbcover.py` | `67a6c15fd5ecd88c0cb8914dad2afdae35bb2169c60c985e14818b6e9d161460` |
| `gauges.py` | `55d1583bc3301be70b68b8d07d1c5662178c4b4bfe75c008ff8077759e312301` |
| `cnf16.py` | `4064361aa70568db9721be867b171d18761075dd3baa61d99ff7ec883887d7a4` |

## Verdict

The two-rail **structural decomposition is correct**, but the exploratory
`rbcover.py` coverage model is not exact.  It proves only a loose union-of-
possible-labels condition.  The same defect occurs in `railpair.py`.

This bug does not destroy the separate A-rail existence claim at
(n=15): an independent corrected model chooses one label and one phase
increment per selected arc and has produced a physically replayed covering
A-path.  It does mean that no result from `rbcover.py` or `railpair.py`
alone should be cited as a certificate.

The two independently valid rails found so far do **not** combine into the
desired K16 carrier: the exact gauge/seam/residence solve for that fixed pair
is `INFEASIBLE`.

## 1. The mathematical two-rail normal form

Let $K=2R$, $n=K-1=2R-1$, and suppose an equivariant bilayer carrier
has one cyclic block of top-bit states.  Its quotient revolution splits into

* an A-rail of rank $R-1$ subsets of $[n]$, carrying the top bit; and
* a B-rail of rank $R$ subsets of $[n]$, without the top bit.

The rotation action is free on both ranks because

\[
  \gcd(2R-1,R)=\gcd(2R-1,R-1)=1.
\]

Thus middle-layer bijectivity is equivalent to each rail visiting every
necklace orbit of its rank exactly once.  Generalized transversality makes
the interior steps Johnson.  At the two rail boundaries, c-part symmetric
difference one and the rank difference force containment.  Unit wrap
voltage rotates the first A-column once after the B-to-A seam.

The q1 accounting in `railanat.py` is correct:

* no-top q1 labels arise from B-B intersections and the two containment
  seams;
* top q1 labels arise only from A-A intersections.

For K16 the B rail has 428 interior edges plus two seams for 429 no-top q1
orbits, hence one unit of excess.  The A rail has 428 interior edges for 335
top-q1 orbits, hence substantial repetition is allowed.

This equivalence concerns the middle ownership/Johnson/q1 anatomy.  A pair
of such quotient paths is not by itself a carrier certificate: phases,
both containment seams, unit voltage, residence, q2, and all upper palettes
must still hold simultaneously.

`railanat.py` reconstructs the physical wrap frame correctly, but it only
prints its measurements.  Apart from the single-top-run assertion it does
not assert the advertised palette conclusions.  It is an analyzer of a
previously audited artifact, not a proof-producing verifier.

## 2. `rbcover.py` is a relaxation, not an exact covering model

For a quotient arc $i\to j$, `adj[i][j]` stores every label realizable by
some relative rotation.  In `rbcover.py` lines 61--65, the one arc literal
`al` is appended directly to the coverage list of **every** such label.
Lines 66--70 then require

\[
  \bigvee_{e:\lambda\in L(e)} a_e
\]

for each label $\lambda$.  If one selected arc has
$L(e)=\{\lambda_1,\lambda_2\}$, the same Boolean literal satisfies both
label clauses although one physical alignment of that edge can realize only
one label.

The postsolve code at lines 88--97 does not repair this.  It loops over all
relative rotations of each path edge and again credits every possible
label.  Its own output calls this a `loose count`.

The exact condition is an SDR/flow condition.  Introduce
$x_{e,\lambda,\delta}$ for one label and one phase increment and impose

\[
  \sum_{\lambda,\delta}x_{e,\lambda,\delta}=a_e,
  \qquad
  \sum_{e,\delta}x_{e,\lambda,\delta}\ge1.
\]

Because the quotient object is a path, chosen phase increments can then be
accumulated from its start without an additional cycle-consistency
constraint.

`railpair.py` repeats the same bug.  Its per-arc option literals imply the
arc and a selected arc requires `BoolOr(opts)`, but it never imposes
`sum(opts)==arc`.  One quotient arc may therefore simultaneously claim
several incompatible intersection/union pairs.  Any `railpair.py` output
requires an independent physical replay before use.

## 3. The corrected exact rail artifacts

The independent replacement

`/dev/shm/k16_shortcycles/audit_claude_exact_covering_rail_path_20260729.py`

(SHA-256
`e3cbaea786cb8f171e0c7711aa0e98db87107458514cf60278a4aeff06ebc7ca`)
uses `sum(choices)==arc`, stores a phase increment for the chosen label,
materializes the physical path, and checks every physical Johnson edge and
label.

It produced:

* exact A rail, (n=15,r=7): 429 vertices, 428 physical edges, all 335
  labels covered; artifact SHA-256
  `09734f1ee91af8f1e6d9569cb05010dbd5edc30e0aa74d79762e9591abc8ae91`;
* exact B rail, (n=15,r=8): 429 vertices and 428 pairwise-distinct labels;
  artifact SHA-256
  `8a03664ea922357f069b002a9fa69adc447719b09e00a5b792c522e29b26654f`.

Therefore separate exact rail abundance is real; it is no longer dependent
on `rbcover.py`.

The fixed-pair call to `gauges.py` reports `INFEASIBLE` in 0.9 seconds.  The
gauge model's core encoding is sound for its assumptions:

* exactly one absolute rotation is chosen for each column;
* the presence equivalence is encoded in both directions;
* B-B and A-A steps have c-part symmetric difference two;
* the two rank-different seams have c-part symmetric difference one, hence
  containment;
* the wrap column is the unit rotation of the first column;
* every positive c-run ending at a deletion is forced to have length at
  least (D+1).

Its subsequent `biword2` audit is required for q1/q2/upper completeness.
The `INFEASIBLE` verdict concerns only this ordered A/B pair; it is not a
no-go for all rail pairs.

Operational warning: `gauges.py`, `rbcover.py`, and `rbexact.py` ignore the
Boolean returned by `main` in their `__main__` blocks.  Consequently an
`INFEASIBLE` solve still exits with shell status zero.  Monitors must parse
the printed solver status or a validated artifact rather than the process
exit code.

## 4. `rbexact.py`

At `--slack 0`, the existence encoding is sound.  Every selected internal
path arc must choose at least one possible label, and each label has a global
at-most-one constraint.  From any satisfying assignment, extra true label
literals on an arc may be deleted until one remains; the selected labels are
then distinct.  Along a path, their witnessing relative phases can be
chosen sequentially.

Two qualifications are necessary:

1. `--slack` is ineffective.  Even for positive slack, every one of the
   (NV-1) internal arcs still needs a label and the global per-label
   at-most-one constraints still force all of them distinct.  The model is
   stronger than its documented slack version.
2. `/dev/shm/rb15.log` stores only the quotient vertex path, not the chosen
   labels or phase increments.  It is solver evidence, not a replayable
   certificate.  The corrected exact B-rail artifact above supersedes it.

## 5. `cnf16.py --rails` is sound as a slice, but not a size reduction

The prescribed-rail constraints at lines 149--165 fix the top pattern and
require every quotient class to equal some rotation of its prescribed
necklace.  They use only `BoolOr(opts)`, not explicit exactly-one.  This is
nevertheless exact here: ranks $R$ and $R-1$ have free $\mathbb Z_n$
action, so
two distinct rotation selectors cannot both imply the same class bits.

The generic middle, q1, q2, and upper selector rows are then emitted
unchanged.  Thus `--rails` adds constraints but removes no generic palette
selectors.  The actual K10 files demonstrate this exactly:

| model | variables | clauses | gzip size |
|---|---:|---:|---:|
| two-rail `--tfix` | 78,792 | 1,869,193 | 6.6 MB |
| prescribed `--rails` | 79,044 | 1,871,489 | 6.7 MB |

The difference is precisely 252 rotation selectors and 2,296 rail clauses;
the full generic model remains.

At K16 the source loops emit approximately:

| selector family | selectors retained |
|---|---:|
| middle | 11,042,460 |
| q1 | 9,815,520 |
| q2 | 6,870,864 |
| upper | 122,731,752 |
| **total** | **150,460,596** |

Rail prescription adds only 12,870 phase-selector variables and 193,908
clauses on top.  Unit propagation may make the solve easier, but construction
time, compressed CNF size, and selector memory remain those of the huge flat
model.  A genuine rail reduction should use one phase variable per class and
direct phase-conditioned palette witnesses, eliminating the generic middle
selectors completely.

The generic selector implications in `cnf16.py` are sufficient, so a SAT
assignment that passes `cnfdecode.py`'s independent `biword2` replay is a
valid carrier.  The restricted upper-width catalogue makes an UNSAT verdict
scoped to that sufficient width family, not necessarily to every possible
arbitrary-width carrier.

The K10 artifact `/dev/shm/ck10rw_PASS.json` (SHA-256
`9d4630d0a8f6fd4ea790dda4013b46e994daada533b864d31bc41f931ec3f114`)
passes a fresh full `biword2` replay with zero Hamilton, Johnson, residence,
q1, q2, middle, or upper defects.  Its mathematical validity therefore does
not depend on trusting the CNF encoding or `railanat.py`.

## Bottom line

The useful theorem is the structural two-rail decomposition plus the exact
one-label-per-edge rail formulation.  The current evidence establishes:

1. valid complete two-rail carriers exist at K8 and K10;
2. exact A and B quotient paths of the required individual types exist at
   K16;
3. the particular exact A/B pair tested cannot be gauged into a resident
   unit-voltage K16 carrier;
4. neither `rbcover.py` nor `railpair.py` proves a coupled K16 construction;
5. `cnf16.py --rails` is a sound restrictive slice but retains essentially
   the entire flat K16 selector burden.

The remaining problem is genuinely the coupled choice of both paths,
phase increments, seams, residence, and deeper palettes—not separate rail
existence.

## Addendum: the two exact chronologies are intrinsically nonresident

The follow-up checker

`scratch/audit_k16_rail_path_phase_residence_20260730.py`

(SHA-256
`a73ef80179b88aea4463b533168b56ffc7058d1492fad1ad465a8e7404fba54f`)
tests each fixed quotient chronology in isolation.  It removes the other
rail, both A/B seams, the unit-voltage closure, all q1/q2/upper palette
requirements, and every right-end run condition.  At the left end it imposes
no residence check on a deletion in the first three transitions.  Thus it is
strictly weaker than the residence condition needed by a K16 carrier.

The remaining model chooses an arbitrary physical rotation independently at
each of the 429 quotient vertices and asks only that:

1. every one of the 428 interior transitions is Johnson; and
2. whenever a coordinate is deleted at transition index at least three, it
   was present in the preceding three columns.

Fixing the first phase to zero is without loss by global coordinate rotation.
The test was run in both path orientations.  All four exact audits are
`INFEASIBLE`:

| chronology | orientation | audit SHA-256 |
|---|---|---|
| exact A rail (`22d4df5e...`) | forward | `d45bc70282392a8c97905a2966f01ec75c071aff500fd16bc9102ce1feb0d487` |
| exact A rail (`22d4df5e...`) | reverse | `6c9318a2360d2a5989fcef2e264e29a76d782c44b8202e53aa39d0d188c5b469` |
| exact B rail (`8a03664e...`) | forward | `158934fa0ffe870adf05a03ea59d40142787acc407282718ab3e323e6c8c35ab` |
| exact B rail (`8a03664e...`) | reverse | `3cd90e790b55f25350de3efd700c0006681b7f588a06b4ebd57ed44ae453858b` |

The JSON scope sentence says endpoint runs are omitted.  More precisely, the
encoding exempts every deletion among the first three transitions, including
some short runs that need not literally touch the first vertex.  This only
makes the model weaker, so it cannot invalidate the infeasibility conclusion.
Likewise, the model does not require the phase choices to preserve the exact
label assignment that originally certified each rail.

Therefore the earlier fixed-pair gauge failure is not caused by a bad seam,
endpoint alignment, final voltage, or interaction between the two rails.
Each quotient chronology is already incompatible with even this relaxed
open-rail phase/residence problem.  Reversing either path does not help.

This remains a chronology-specific no-go, not a theorem against all A or B
rails.  Its algorithmic consequence is nevertheless sharp: future quotient
path generation must hard-constrain physical phase and residence while the
path is chosen.  Generating label-perfect quotient paths first and attempting
to gauge residence afterward can return intrinsically unusable chronologies,
as happened for both rails here.
