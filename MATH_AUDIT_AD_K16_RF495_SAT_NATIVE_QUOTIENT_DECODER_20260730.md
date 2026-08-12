# AD audit: SAT-native RF495 shared-OR quotient and acceptance path

Date: 2026-07-30  
Scope: the frozen seed-5/self, length-12,873, 4/9/5 RF495 fibre only.  This note neither runs a solver nor makes a global claim about \(\nu(16)\).

## 1. Frozen data and notation

There are eighteen mutable nonzero cells, indexed by free ordinals
\(i=0,\ldots,17\), split into three chains of lengths \(4,9,5\).  Write
\(x_{i,b}\) for bit \(b\in\{0,\ldots,15\}\) of cell \(i\).  The authenticated
maximal-provider table contains exactly one row
\[
 (T,Q,F)
\]
for each of seventy residual targets \(T\) and each of seventy nonempty chain
intervals \(Q\).  Thus it has 4,900 rows.  Every row satisfies \(F\subseteq T\),
and it comes with an authenticated physical representative interval whose
fixed-body OR is \(F\) and whose mutable positions are exactly \(Q\).

For each nonsingleton chain interval \(Q=[a,b]\) and coordinate \(j\), introduce
\(z_{Q,j}\).  There are
\[
 \left(\binom{5}{2}+\binom{10}{2}+\binom{6}{2}-(4+9+5)\right)16
 =52\cdot16=832
\]
such variables.  For singleton \(Q=\{i\}\), define \(z_{Q,j}:=x_{i,j}\)
without introducing a variable.

Finally introduce one provider variable \(p_{T,Q}\) for every authenticated
row.  Importantly, these variables are indexed by the explicit pair
`(target_dec, free_qmask18)`, not by an old witness ID or an accidental TSV
row number.

## 2. Exact DIMACS formula

Use one-based DIMACS variables in three disjoint ranges:

1. 288 cell bits;
2. 832 nonsingleton interval-OR bits;
3. 4,900 provider bits.

The formula has four clause families.

### 2.1 Nonzero cells

For each mutable cell \(i\), add
\[
 \bigvee_{j=0}^{15}x_{i,j}.
\]
This gives 18 clauses.

### 2.2 Exact shared interval ORs

For every nonsingleton \(Q=[a,b]\), coordinate \(j\), let \(u\) denote the
already defined bit for \([a,b-1]\) and let \(v=x_{b,j}\).  Encode
\(z_{Q,j}\leftrightarrow(u\vee v)\) by
\[
 (\neg u\vee z_{Q,j}),\qquad
 (\neg v\vee z_{Q,j}),\qquad
 (u\vee v\vee\neg z_{Q,j}).
\]
There are exactly \(3\cdot832=2,496\) clauses.  Induction on interval length
proves
\[
 z_{Q,j}=\bigvee_{i\in Q}x_{i,j}
\]
in every satisfying assignment.  All three clauses are necessary for the
claimed exact equivalence; one-way OR definitions would invalidate an UNSAT
conclusion.

### 2.3 Provider implications

For an authenticated row \((T,Q,F)\), add
\[
 \neg p_{T,Q}\vee\neg z_{Q,j}\quad(j\notin T)
\]
and
\[
 \neg p_{T,Q}\vee z_{Q,j}\quad(j\in T\setminus F).
\]
Here `z` means the corresponding cell bit for singleton \(Q\).  No clause is
needed for \(j\in F\), because the fixed part already supplies that bit.
Consequently the row contributes exactly \(16-|F|\) binary clauses.  Direct
recount from the frozen 4,900-row table gives
\[
 \sum_{(T,Q,F)}(16-|F|)=76,054.
\]
If \(p_{T,Q}=1\), these clauses and the exact OR recurrence give
\[
 F\mathbin\vert\bigvee_{i\in Q}x_i=T.
\]

### 2.4 Target coverage, without at-most-one

For each residual target \(T\), add the single clause
\[
 \bigvee_Q p_{T,Q}.
\]
There are seventy clauses of length seventy.  There is deliberately no
at-most-one condition and no reverse implication from a realized output to a
provider bit.  Different targets may use the same \(Q\), and several provider
bits for one target may be true.

The exact dimensions are therefore
\[
 \begin{aligned}
 V&=288+832+4,900=6,020,\\
 C&=18+2,496+76,054+70=78,638.
 \end{aligned}
\]
The exact number of literal occurrences is
\[
 18\cdot16+832\cdot7+2\cdot76,054+70\cdot70=163,120.
\]

**Solver-free incumbent regression.**  Evaluating the frozen `lead_score3.cells`
directly realizes 71 maximal rows belonging to 67 targets, and misses exactly
\(\{0x18e7,0x3de7,0x9e20\}\).  The multiply realized targets are `0x18e6`
(two rows), `0x9c67` (three), and `0xbde7` (two).  Thus, after setting precisely
the 71 realized provider bits true, every structural and provider clause holds
and only those three target-ALO clauses fail.  This is a useful regression for
both signs of every implication and confirms that ALO, not exact-one, is the
intended new block semantics.

## 3. Projection-equivalence theorem

**Theorem 3.1 (exact canonicalization).**  Let \(N\) be the SAT-native formula
above and let \(E\) be the frozen 4,900-provider exact-one formula.  Their sets
of satisfying assignments have exactly the same projection onto the 288 cell
bits.

**Proof.**  Given a model of \(E\), set every interval bit to the literal OR
of its cells and retain the selected provider for each target.  The OR-gate
clauses hold.  The direct forbidden-bit clauses of \(E\) imply the negative
provider-to-OR clauses, and its needed-bit clause implies the positive
provider-to-OR clause.  Hence this extends to a model of \(N\).

Conversely, take a model of \(N\).  In each target block choose one true
provider and set every other exact-one selector false.  Exact OR equivalence
turns a negative provider implication into zero for every cell bit in \(Q\),
and turns a positive provider implication into the direct disjunction of the
cell bits in \(Q\).  Thus every direct semantic clause of \(E\) holds for the
chosen provider.  Complete the standard sequential at-most-one auxiliaries by
the prefix assignment associated with the chosen position.  This yields a
model of \(E\) with the same 288 cell bits. \(\square\)

Combined with the already audited maximal-provider theorem, this proves exact
equisatisfiability with literal residual-target coverage inside the frozen
fibre.  It does not assert that each true provider is the only provider of its
target.

## 4. Required independent map and DIMACS audit

Before a run, an auditor independent of the builder should fail closed unless
all of the following hold.

1. The source maximal-provider TSV, frozen parent word, source layout map, and
   1,120-variable chain catalogue match their frozen SHA-256 values.
2. DIMACS has exactly 6,020 variables, 78,638 clauses, no zero literal inside a
   clause, and no literal outside `1..6020`.
3. The map is a bijection onto the three advertised variable ranges.  Every
   `(cell ordinal, bit)`, `(interval endpoints, bit)`, and `(target,Q)` occurs
   exactly once.
4. Every mapped \(Q\) is a nonempty contiguous interval within exactly one of
   the 4/9/5 chains.  The seventy-Q universe is complete.
5. Every provider row agrees field-by-field with the authenticated maximal
   table, including target, `free_qmask18`, fixed OR, physical representative
   endpoints, and original witness ID; \(F\subseteq T\).
6. Reconstructing the clauses independently gives the exact DIMACS clause
   multiset (preferably the exact ordered clause list), including all three
   clauses for every recurrence gate and one ALO clause for every target.
7. Recomputed clause-family counts and literal counts equal the values in
   Section 2.  No at-most-one, provider reverse implication, middle-row, or
   \(D^3\) clause is present.

## 5. Fail-closed SAT decoding and two literal replays

A SAT output is not an accepted word until all of the following pass.

1. Parse a unique `SATISFIABLE` status and reject contradictory assignments.
   Require a value for every variable used by the formula; independently
   evaluate every DIMACS clause under the parsed assignment.
2. Decode the first 288 variables into eighteen nonzero 16-bit cells.
3. Recompute all 832 interval OR bits from those cells and compare them with
   the assigned OR variables.
4. For every target, require at least one true provider.  For every true
   provider, verify both the symbolic equality
   \(F\vert\operatorname{OR}(Q)=T\) and the mapped physical representative
   interval equality in the materialized word.  Do not require exactly one.
5. Hash-check the frozen parent and fixed layout.  Fill exactly 12,873 cells;
   reject zero/unset cells or any fixed-body mismatch.
6. Replay all literal contiguous ORs twice by independent algorithms:
   an ending-frontier recurrence and a start-by-start monotone scan.  Each must
   report all 65,535 nonempty masks and the same word SHA-256.  Reaching
   `0xffff` permits a start scan to stop because every longer interval has the
   same OR.  Middle-row histograms are diagnostics only.

Only then may the status be `SAT_PASS_LITERAL_65535_OF_65535_TWICE`, and the
materialized word may be promoted.

## 6. UNSAT and resource-limit scope

Kissat should receive the frozen CNF as the exact input and a distinct proof
path.  A solver line saying UNSAT is insufficient.  Promotion requires a
nonempty DRAT trace and an independent checker success against the exact CNF
hash; the solver binary, checker binary, command, exit codes, stdout/stderr,
proof hash, and resource log should be retained.  A timeout, signal, missing
proof, failed checker, ENOSPC, or memory termination is `UNKNOWN`.

A verified UNSAT result proves only that this frozen seed-5/self RF495
18-cell fibre has no length-12,873 completion.  It is not a global lower bound
for \(\nu(16)\).

## 7. Frozen concrete artifacts and independent audit outcome

The concrete package is
`scratch/k16_rf495_chain_provider_alo_cnf_20260730/`.  The full model is
exactly the formula of Section 2.  A second sufficient face pins the middle-9
chain to `lead_score3` and leaves the left-4 and right-5 chains active.  The
latter has 1,225 variables, 13,505 clauses, and 28,151 literal occurrences;
the pinned middle chain delivers exactly 37 residual targets, leaving exactly
33 target blocks with 25 providers each.

The independent auditor reconstructs every map row, every physical
representative interval, and the complete ordered clause stream, rather than
trusting the builder's counts.  It reports PASS for both variants.  A separate
decoder/wrapper auditor reports `PASS_PRELAUNCH_NOT_RUN`: no solver or remote
command was invoked by either audit.

**Theorem 7.1 (exact middle-pinned face).**  After the nine middle-chain cells
are fixed to `lead_score3`, the `left4_right5` CNF has exactly the same
projection onto the remaining nine cell values as the full literal completion
condition under that pin.

**Proof.**  Every authenticated mutable set (Q) is wholly contained in one
of the three chains.  Direct replay of the pinned middle chain supplies the 37
listed targets independently of both active chains, so deleting their target
clauses loses no condition.  None of the remaining 33 targets is supplied by
any pinned middle-chain interval.  Hence such a target is covered under the
pin if and only if one of its 25 left- or right-chain rows satisfies
(F\mathbin\vert\operatorname{OR}(Q)=T).  The exact recurrence and provider
implications encode precisely that disjunction, by Theorem 3.1.  Applying this
independently to all 33 targets proves both directions. \(\square\)

Frozen SHA-256 values:

| artifact | SHA-256 |
|---|---|
| `full.cnf` | `68f67f5d86134ff1dff1d26d3748ba4430169c72ec35561d0ec3c78293b37eb6` |
| `full.map.json` | `edb29d1859d93e2d24f5fcb666799232cf46b7ef343af2dd4c50e2b6bf6962b4` |
| `full.build.audit.json` | `a8c0bc8d8b7888e5461126d83c540404a632a455ab8c4731041f10d5fca7f2ac` |
| `left4_right5.cnf` | `7c4e281e58beae9b57fcbb4b6dfc6d1f4d604ecb9cabfb034bfe21cfbf130848` |
| `left4_right5.map.json` | `dc01f727c00c666542163a54190eb591894228ef53e7bafa46f8356846adb38c` |
| `left4_right5.build.audit.json` | `5bca957d3109d52e4b49268509392fb4c4e2fdb488e4314c69672a4e09a3c865` |
| independent semantic/clause audit | `4723a844871b2d147ef437e7bd5ccc618e1862dbd292c6cf1993ca913f84371b` |
| independent decoder/wrapper audit | `77b83092349176cc57cad8d42df12138ceea384dbbe321b26a4f2d258d2b8e78` |
| decoder | `efa046932616bf946c9f89459746fc332207c77ef2d8f20026a915444d6abce1` |
| final prelaunch wrapper | `e62b503600f3773109115d2ab7c748f8d936375bf56cfeff7b105ad6df7810a0` |

The wrapper uses a unique `/home/amodo/or15/work/` directory, requires an
externally audited `AUTHORIZED_CPU`, refuses a duplicate same-CNF process or
existing run artifacts, and caps Kissat at one CPU, nice 15, 590 solver seconds
inside 600 wall seconds, and 2 GiB address space.  SAT promotion requires the
two literal replays.  Kissat's real-file proof is binary, so the patched
wrapper invokes `drat-trim` with `-i` and accepts UNSAT only on checker exit
zero plus an anchored `s VERIFIED` line.  The prelaunch ledger includes hashes
of the CNF, map, parent, two verifiers, wrapper, Kissat, and drat-trim, and also
captures the Kissat version.  CPU availability remains an external prelaunch
fact; this note does not authorize or record a launch.

## 8. Execution boundary at freeze

The earlier unrestricted 10,018-variable exact-one core-47 run and the
1,120-variable CP-SAT run both ended `UNKNOWN` by timeout; neither is an
infeasibility result.  The full 6,020-variable relaxed CNF was deliberately
kept at build/audit stage and was not launched.

At `2026-07-30T14:44:28Z`, a read-only H100 audit reported 235,896 MiB
available RAM but only 29 MiB free swap.  More decisively, a two-sample
per-core utilization check reported 0.06% aggregate idle time and no logical
CPU with more than 3% idle time; coordinated jobs already owned cores 46 and
47.  Thus no core met the requested "clearly free" gate.  Launching another
solver would have violated the execution policy.

The coupled-face package was initially staged, without a solver invocation,
at `/home/amodo/or15/work/ad_rf495_chain_alo_lr_7c4e281e_20260730`.  Before a
free CPU appeared, the independently replayed oriented-anchor Hall theorem
closed the entire same fixed fibre.  In the `left4_right5` face its ten
mandatory rank-eight targets must inject into only nine typed anchors: four
physical left starts for the left chain and five physical right ends for the
right chain.  In the full fibre the corresponding count is (21>20).  Since
Theorems 3.1 and 7.1 prove that the CNFs have exactly these literal-completion
projections, the Hall theorem proves both frozen CNFs unsatisfiable without a
SAT run.  This implication is independent of maximal-row dominance because
the Hall audit works on all 6,089 raw literal intervals.

The decisive theorem is
`MATH_THEOREM_K_K16_RF495_ORIENTED_ANCHOR_HALL_FIBRE_NOGO_20260730.md`
(SHA-256
`d1b23b644e484829af12b1e3fcb4b22503f33e9796978e8083f15c2cda460a77`).
Its two independent literal replays have SHA-256 values
`b1c1698fa5909babfadec63f4c031fca8b139ba100d3a3fd92c843f70c825b58`
and
`e75c06d1e912a7d85184006bfba19bbecc296fbab68a63ea6c306c690104fb42`.
The remote `OWNER.txt` is therefore
`CANCELLED_BEFORE_LAUNCH_THEOREM_REDUNDANT`; there is no started marker,
solver output, or proof.  This is a mathematical UNSAT corollary for the
fixed fibre, not a solver/DRAT verdict and not a global lower bound for
\(\nu(16)\).
