# Thread D: sound binary c-space to exact compiler Benders

Date: 2026-07-29

> **Run-transversal update.**  The authoritative eager model, erosion proof,
> k=9 boundary, and compiler-ready predicate are now in
> `THREAD_D_RUN_TRANSVERSAL_CSPACE_BENDERS_20260729.md`.  In particular the
> old aggregate run-count/seam description is strengthened to one start and
> one end per residue; deeper upper separation uses the exact
> next-occurrence/maximal-good-run blocker interface.  This note remains the
> baseline adapter/compiler audit, but the newer note governs those rows.

Status: exact reduction and executable implementation.  The `k=11` positive
and negative regressions are audited.  A deterministic `k=15` eager-only
complement seed is replayed as a hint, not as a carrier.  No new `k=15` job
was launched because the H100 CPU was saturated; the pre-existing `k=15` run
is not a certificate for the new complement-coherent option.

Implementation:

```text
scratch/threadD_cspace_compiler_benders.py
scratch/test_threadD_cspace_compiler_benders.py
```

The implementation is deliberately fail-closed.  A positive result requires
the retained literal word to have the compiler's exact SHA-256 and to pass the
independent word verifier.  An `UNKNOWN`, timeout, exhausted round limit, or
sampled/incomplete subproblem emits no negative cut.

## 1. Exact binary c-space map

Let `k=2m+1`, `r=m+1`,

\[
 W=\binom{k}{r},\qquad N=W/k,
\]

and let `c` be a cyclic binary word of length `W`.  In the normalized
voltage-one gauge define

\[
 T_i(x)=c_{i-xN},\qquad i\in\mathbb Z_W, x\in\mathbb Z_k.       \tag{1.1}
\]

All indices in this note are cyclic.  Then

\[
 T_{i+N}=\rho T_i.                                                \tag{1.2}
\]

The `N` class-sum equations

\[
 \sum_{a=0}^{k-1}c_{j+aN}=r\quad(0\le j<N)                       \tag{1.3}
\]

are equivalent to `|T_i|=r` for every `i`.  Requiring Hamming distance two
between `T_j,T_{j+1}` for `0<=j<N` gives every one of the `W` Johnson edges
by (1.2).  The forbidden cyclic words `0 1^ell 0`, `1<=ell<=d`, are exactly
the residence constraints because every coordinate trace in (1.1) is a
translate of `c`.

For odd `k`, rotation is free on both central layers: if a nonidentity
rotation with odd orbit length `a>1` fixed an `r`-set, then `a` would divide
both `k` and `r`, hence would divide `2r-k=1`.  Consequently `N`
rotation-distinct quotient columns give the complete middle deck, and `N`
rotation-distinct adjacent intersections give the complete lower first
shadow deck.

An imported unit-voltage-`v` cycle is harmless: its coordinate-zero trace,
reconstructed by (1.1), is the coordinate-multiplier relabeling
`x -> v^(-1)x` in voltage-one gauge.  Choice and arc IDs are not assumed to
survive this relabeling; the adapter regenerates and validates them from the
literal reconstructed cycle.

### Lemma 1.1 (redundant cyclic run equality)

Every rank-correct equivariant Johnson chronology satisfies

\[
 \#\{p:c_p=0,c_{p+1}=1\}=N.                                    \tag{1.4}
\]

#### Proof

Each of the `W` physical Johnson edges adds exactly one coordinate.  The `k`
coordinate traces are translates of `c`, so they have a common number `R` of
cyclic `01` transitions.  Counting added-coordinate incidences gives
`kR=W`, hence `R=N`.  This does not require a probabilistic or marginal
argument.  The model includes (1.4) as a redundant propagation equality,
with every `01` indicator reified in both directions.  \(\square\)

At `k=15`, (1.3) gives `|c|=8*429=3432`, while (1.4) gives 429 chronological
one-runs, of average length eight.  Residence still forbids chronological
lengths one, two, and three.

## 2. Sound relational and shadow rows

### Joint collisions

Suppose quotient positions `a,b` currently obey

\[
 T_b=\rho^sT_a.
\]

The correct lazy row is

\[
 \bigvee_{x\in\mathbb Z_k}
 \left(c_{b-xN}\mathbin{\mathsf{xor}}c_{a-(x-s)N}\right).        \tag{2.1}
\]

It forbids only their joint rotated equality.  It does not ban either
column pattern separately.  The lower-first-shadow collision row is the
same relation after replacing each column bit by the exact conjunction of
its two endpoint bits.  Both XOR and conjunction variables are reified in
both directions.

### Lower rows and the terminal compiler presolve

For a rank-`r-q` target `S`, the lower row is the exact disjunction over all
`W` starts of

\[
 \bigcap_{a=0}^{q}T_{i+a}=S.                                    \tag{2.2}
\]

The carrier gate needs `2<=q<d`.  This implementation also separates
`q=d`, but labels it a compiler presolve, not a carrier axiom.  Indeed the
maximal erosion

\[
 P_i=\bigcap_{a=0}^{d}T_{i-a}
\]

has rank `h=r-d`.  In the zero-core envelope relaxation a rank-`h` target
`S` is adjacent at `i` only if `S subseteq P_i`; equal ranks force `S=P_i`.
Thus a missing terminal lower target has zero envelope degree and rejects
the exact one-core compiler before any core choice.  This is why the frozen
negative `k=11` fixture has envelope Hall `220/231`: one missing orbit gives
eleven zero-degree physical targets.

### Complete upper separation

For a proper upper target `S`, set

\[
 b_i=[T_i\subseteq S]
\]

and, for `x in S`, let `q_(i,x)` mean that `x` is still missing from the
maximal `S`-contained suffix ending at `i`.  The exact cyclic recurrence is

\[
 q_{i,x}=\neg b_i\ \vee\ (q_{i-1,x}\wedge[x\notin T_i]).         \tag{2.3}
\]

A Hamilton middle deck contains a state outside every proper `S`, so (2.3)
has a reset and a unique cyclic solution.  The target is covered exactly
when some `i` has `b_i=1` and `q_(i,x)=0` for every `x in S`.  Hence (2.3)
detects unions of arbitrary-width cyclic intervals; no fixed witness width
is assumed.

There is one exact specialization.

### Lemma 2.1 (upper first-shadow edge reduction)

For a cyclic Johnson chronology and `|S|=r+1`, `S` is the union of a
nontrivial consecutive block if and only if

\[
 S=T_i\cup T_{i+1}                                               \tag{2.4}
\]

for some cyclic edge, including the wrap edge.

#### Proof

Take the first adjacent pair in a witnessing block.  It is a distinct
rank-`r` Johnson pair, so its union has rank `r+1`; it is contained in the
block union `S` of the same rank, hence equals `S`.  The converse is
immediate.  \(\square\)

The master therefore uses an exact two-column union selector for upper
`q=1`, but retains (2.3) at every deeper rank.

## 3. Optional complement-coherent subclass

This is an optional exact restriction, never an unconditional row.  It is
available only when `W` is odd, equivalently for the present family at
`k=3,7,15,31,...`.  It is rejected at `k=11`.

Put `W=2s+1`.  Middle-level complement coherence is

\[
 \overline{T_i}=X_{i+s},\qquad X_j=T_j\cap T_{j+1}.                \tag{3.1}
\]

Substituting (1.1), with `p=i-xN`, gives the scalar identity

\[
 \boxed{1-c_p=c_{p+s}c_{p+s+1}}                                  \tag{3.2}
\]

for every `p`.  Conversely every `p` occurs as `i-xN`, so (3.2) implies the
literal set identities (3.1).  The model encodes each row by the three
clauses

```text
c[p] OR c[p+s]
c[p] OR c[p+s+1]
not c[p] OR not c[p+s] OR not c[p+s+1].
```

Let `t=(W+1)/2`, so `2t=1 mod W`, and define `d_i=c_(ti)`.  Since
`s=t-1=-t mod W`, (3.2) is equivalent to

\[
 d_{i+1}=\operatorname{NAND}(d_i,d_{i+2}).                        \tag{3.3}
\]

Thus in the permuted **d-order** zeros are isolated and every maximal
one-run has length one or two.  This is not the chronological `c`-residence
order.  If `a,b` are the numbers of length-one and length-two `d`-runs, then

\[
 2a+3b=W=(2m+1)N,\qquad a+2b=|c|=(m+1)N,
\]

so

\[
 b=N,\qquad a=(m-1)N.                                             \tag{3.4}
\]

At `k=15`, `s=3217,t=3218`: the `d`-word has 3003 isolated zeros,
2574 singleton one-runs, and 429 length-two one-runs.  Separately, the
chronological `c`-word has the 429 runs from Lemma 1.1.

Complement coherence gives the all-depth occurrence identity

\[
 \overline{\bigcup_{j=0}^{q}T_{i+j}}
 =\bigcap_{j=0}^{q+1}T_{i+s+j}.                                  \tag{3.5}
\]

In particular completed lower-`q2` rows imply upper-`q1`, so that staged
family is halved.  For deeper ranks, arbitrary-width upper blocks correspond
to arbitrary-width lower intersections; (3.5) does **not** justify a fixed
`q+1`-window shortcut.  The implementation therefore retains the complete
upper recurrence (2.3), audits (3.1) independently of (3.2), and still
requires final literal-word verification.

The solver-free regression exhausts every odd toy word through `W=11` and
checks equivalence of (3.2), (3.3), and the run form.  A recurrence-pruned
complete census gives:

```text
k=3:  3 NAND words, 3 rank-correct, 3 owner-perfect;
k=7:  18,807 NAND words, 217 rank-correct, 0 owner-perfect.
```

The `k=7` statement is a finite obstruction inside this complement-coherent
binary c-space subclass, not a general Middle Levels obstruction.

## 4. Exact Benders contract

One round has the following order.

1. Solve the exact c-space master: class sums, residence, Johnson seams,
   the redundant `#01=N` equality, a fixed Hamming radius if requested, and
   optional complement coherence.
2. Separate middle and lower-q1 orbit collisions using the joint rows (2.1).
3. Separate exact lower rows through `q=d`.
4. Separate all upper targets, using (2.4) only at `q=1` and (2.3) deeper.
5. Reconstruct the literal physical cycle, regenerate repository choice and
   directed-arc IDs, and run the exact compiler subproblem.
6. The compiler ranges over every equivariant cyclic one-core for this
   carrier, checks the core-free and selected-core weighted quotient Hall
   flows, constructs the physical target matching, tests every upper-safe
   cut, writes the physical word, and invokes the independent exhaustive
   literal verifier.

Inside the Benders loop, only these exact fixed-carrier failures may generate
a full-c assignment no-good:

```text
CARRIER_GATE_REJECTED
ENVELOPE_HALL_INFEASIBLE
EXACT_CORE_HALL_INFEASIBLE
NO_UPPER_SAFE_OPENING
```

The standalone compile command may also reject
`CSPACE_FIXED_FACTOR_REJECTED` by a full-c no-good when the literal trace
itself fails rank, Johnson, or owner-orbit reconstruction; the Benders eager
and collision stages prevent such a trace from reaching its compiler call.

The no-good is false at exactly that complete c assignment.  The cut ledger
retains both a semantic digest and a provenance-augmented digest.  It never
uses the old unsafe single-column no-good.

A master `INFEASIBLE` status is therefore logically scoped to the printed
voltage-one c-space, radius, optional complement restriction, and declared
equivariant-one-core/upper-safe-opening compiler architecture.  It is not a
lower bound for unrestricted `nu(k)` and not a general coefficient-one
no-go.  OR-Tools supplies a replayable solver audit here, not an independently
checked DRAT proof.

Positive status is stricter: both compile entry points assert that the word
exists and its bytes have the compiler's stated SHA-256.  A stale output path
cannot be reported as the current word.  The independently hashed verifier
must then cover every nonempty mask and confirm the exact middle row.

## 5. Input and provenance boundary

Version-one c-space payloads must contain an exact schema, encoding, dense
binary `c`, and `c_sha256`; duplicate keys and unknown fields are rejected.
The retained frozen theory source is

```text
scratch/threadD_claude_cword_e9a01efc.py
```

and is byte-identical to the audited live `work/cword.py` at SHA-256
`e9a01efc1edf5df791b1238854c66a678f7228b2b8fdf7ee19540bddbebf6abd`.
Its legacy `{k,c}` / `{k,c,cycle}` output lacks provenance fields.  The
`wrap-legacy-cword` command accepts only those exact shapes, independently
replays `c` and any claimed cycle, and emits a strict v1 payload plus an audit
which explicitly says that the historical raw-file generator is not
authenticated.

Audit, compile, and search records hash the input, adapter, compiler bridge,
graded quotient catalogue, literal verifier, frozen cword source, choice
table, arc table, model proto, and retained outputs.  No `ready15` forced
ports are used.

## 6. Exact k=11 regression and k=15 boundary

The current solver-free suite replays three independent `k=11` ledgers.

1. The positive geometry fixture has `c` SHA-256
   `963c1f4be3a5d4103fdab2aa2e45f40ae2f8910e96cf22bf65747c40a4d6dab7`,
   exact middle/lower-q1 ownership, no residence or shadow holes, and
   core-free envelope Hall `231/231`.
2. The negative fixture has `c` SHA-256
   `a885520acf412e620d962139558fe28759d6e6778d725dcde8a09e562a962421`.
   It passes the carrier gate but misses terminal lower target orbit 25;
   its eleven physical rotations have zero envelope degree and Hall is
   exactly `220/231`.
3. The retained exact positive carrier has `c` SHA-256
   `c93dbcb246aa07bc374e6a179f6512d86b77658774c600a78377b2de75dfc177`.
   The exact common core/Hall model used 3,696 variables and 5,355
   constraints, both weighted and physical Hall were `231/231`, and 242
   cuts were upper-safe.  It emitted the optimal length-465 word

```text
scratch/sound_cword_cegar_k11_radius0.word
```

with SHA-256
`0f80c3295248a862b0fd5ad6a594a4162c346e0d9e404d351e9a28dbdcba38a0`.
The independent verifier recomputes all 2,047 nonempty masks and the exact
middle row.  The retained run reports 0.0204 seconds in the compiler and
0.1607 seconds end-to-end with one worker.  This exact run predates the new
optional complement flag, but the current adapter independently replays its
c trace and physical chronology.

At `k=15`, the H100 remained oversubscribed.  The already-running baseline
`sound_cword_cegar.py` process was left untouched and had not emitted a
result at the last audit.  The frozen eager hint

```text
scratch/k15_complement_nand_eager_seed.cw
```

has file SHA-256
`9164047a2b7c8a17e626c1589c58965738472bfd2c6c5d220a121bd959eaa71b`.
Its canonical dense-vector SHA-256 is
`ea4f7c806db0527745f8a97ac31a312f350826d86c5113c8da802548ba4da54f`;
the frozen generator audit's historical `c_sha256` field denotes the raw
`.cw` bytes, not this stable-vector encoding.  The generator advances the
long-gap residues by `7j mod 429` and uses four lifted intervals with an
extra `2C`.
Independent current-source replay verifies 3,432 ones, 429 chronological
runs with histogram `4^425 433^4`, no class/Johnson/residence/complement
defect, and the forced `d`-run counts from (3.4).  It has only 26 of 429
middle orbits and 26 of 429 lower-q1 orbits, misses 312 lower-q2 orbits, 178
terminal lower-q3 orbits, and 608 upper orbits.  Its frozen audit deliberately
reports `EAGER_PASS_ONLY` and `carrier_gate_pass=false`.  The `--seed-cw`
interface accepts it only together with `--complement-coherent`, replays every
eager row and set identity, and records these deficits before treating it as
a hint or fixed radius center.  Runtime provenance pins and replays the seed
bytes but makes no generator-process claim; the separate regression pins the
generator and frozen audit artifacts.  The solver-free current-source replay
is retained as
`scratch/threadD_k15_complement_nand_eager_seed.audit.json`; its status is
literally `EAGER_HINT_ONLY_NOT_A_CARRIER_CERTIFICATE`.

No run of the new source, and in particular no run with
`--complement-coherent`, is claimed.  The next legitimate execution step is
a bounded H100 CPU smoke only after the existing batches release cores.

## 7. Reproduction and frozen hashes

The full local regression is solver-free and lightweight:

```bash
PYTHONPATH=scratch python3 \
  scratch/test_threadD_cspace_compiler_benders.py

PYTHONPATH=scratch python3 \
  scratch/threadD_cspace_compiler_benders.py audit \
  scratch/threadD_cspace_k11_positive.json \
  --output scratch/threadD_cspace_k11_positive.audit.json
```

Legacy Claude output is converted without trusting its history by

```bash
PYTHONPATH=scratch python3 \
  scratch/threadD_cspace_compiler_benders.py wrap-legacy-cword RAW.json \
  --output STRICT_V1.json --audit WRAP.audit.json
```

The frozen complement hint is replayed without a solver by

```bash
PYTHONPATH=scratch python3 \
  scratch/threadD_cspace_compiler_benders.py audit-cw-hint \
  scratch/k15_complement_nand_eager_seed.cw --k 15 \
  --output scratch/threadD_k15_complement_nand_eager_seed.audit.json \
  --generator scratch/generate_k15_complement_nand_seed.py \
  --seed-audit scratch/k15_complement_nand_eager_seed.audit.json
```

After H100 capacity becomes available, the optional symmetric smoke is the
`benders-search` command with `--k 15 --complement-coherent` and
`--seed-cw scratch/k15_complement_nand_eager_seed.cw`; it must use the H100
CPU OR-Tools environment and bounded workers/time.  It was not executed in
this iteration.

Frozen SHA-256 values at this note's audit point are:

```text
c32d0fead1b862d124ac367de350e89a01de58503ad1e8b9eb9ea981204de710  threadD_cspace_compiler_benders.py
9f16bfbd950dda1751e897685534ab0272ae505d9b85e99f0b9d4ee4e6ce2100  test_threadD_cspace_compiler_benders.py
5eaf8f2412fd5054d66382e6c16dd6de0bb35087c101f89522ea2ee8a2034e23  threadD_claude_exact_benders_adapter.py
a364a0e48e1f35dc9610436adf3e841f16290b883f12308de04dfce728fa8fda  graded_quotient_pipeline.py
ef7fe81cb6591d27c60143d055aa4b253219fa45573512ab2866c623c33c2799  verify_exact_or_word.py
e9a01efc1edf5df791b1238854c66a678f7228b2b8fdf7ee19540bddbebf6abd  threadD_claude_cword_e9a01efc.py
770684d9ae7bafd51a22502328e81769a6896aad4e3a55a31d9c25dccd020217  threadD_cspace_k11_positive.audit.json
440c89ed1f10f961c7d457722a04ebabfb46a16759f21b7d59e2384ef7773f0b  threadD_cspace_k11_corefail.audit.json
e2038cfba2a5881da0b5cc0b912985f32d48bd70b943e5d37def95718facc9ba  sound_cword_cegar_k11_radius0.result.json
0f80c3295248a862b0fd5ad6a594a4162c346e0d9e404d351e9a28dbdcba38a0  sound_cword_cegar_k11_radius0.word
9164047a2b7c8a17e626c1589c58965738472bfd2c6c5d220a121bd959eaa71b  k15_complement_nand_eager_seed.cw
3556ea4b1eb329776343d7fdc06cd3d7cb19a4ea34d9e3313a689ccab4da47c3  generate_k15_complement_nand_seed.py
970ff44cc60e7a03d479e823b1ed4ae7e7d5a51028c669e88d1fd6a440568f94  k15_complement_nand_eager_seed.audit.json
a48153a0e56f4f3585beeab1f901ac00bf6950a6857ba00d8883235dbc2c35cd  threadD_k15_complement_nand_eager_seed.audit.json
```
