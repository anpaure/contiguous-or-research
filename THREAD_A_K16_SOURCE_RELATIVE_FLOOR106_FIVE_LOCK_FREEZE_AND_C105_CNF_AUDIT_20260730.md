# Thread A: source-relative floor 106 by the authenticated five-lock automaton

Date: 2026-07-30

## 1. Exact scope

Fix the 211,604 directed seams in
`scratch/k16_len8_source_seam_ledger_20260730.bin`, SHA-256

```text
832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657.
```

Let (x_e\in\mathbb Z_{\ge0}) be a balanced seam circulation:

\[
\sum_{e:\,\operatorname{tail}(e)=v}x_e
=
\sum_{e:\,\operatorname{head}(e)=v}x_e
\qquad(v\in V).
\]

Repeated seams are allowed.  Every one of the 93 source defects must be
served at least once.  Port capacity, edge binarity, cut separation, q1,
reverse-edge, residence, survivor, and deeper-shadow constraints are all
omitted.

This is an integral relaxation of every physical binary balanced selection
from the frozen catalogue.  It is **not** a fractional-circulation model and
it is not an unrestricted (K=16) theorem.

## 2. The floor-106 theorem

### Theorem 2.1 (authenticated source-relative floor 106)

Every nonnegative integral balanced/service circulation in the frozen seam
catalogue has

\[
C:=\sum_e x_e\ge106.
\]

### Proof

The exact scale-two certificate
`scratch/k16_direct_cycle_dual_exact_20260730.audit.json`, SHA-256

```text
29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d,
```

assigns target weights (b_t\in\{1,2,4\}), of total weight (207), and an
integer vertex potential (y).  Every seam has nonnegative integer slack

\[
s(e)=2+y(\operatorname{head}e)-y(\operatorname{tail}e)
      -\sum_{t\in H(e)}b_t.
\]

Write

\[
\mu_t=\sum_{e:\,t\in H(e)}x_e,
\qquad
Q=\sum_t b_t(\mu_t-1),
\qquad
R=\sum_e s(e)x_e.
\]

Balance cancels the potential, so

\[
2C=\sum_t b_t\mu_t+R=207+Q+R.                 \tag{2.1}
\]

The fifteen weight-one targets are partitioned into the five lock triples

\[
\begin{aligned}
L_1&=\{35044,36935,40066\},\\
L_2&=\{37320,41102,47364\},\\
L_3&=\{33906,36417,51235\},\\
L_4&=\{33337,50976,58385\},\\
L_5&=\{41872,49436,61960\}.
\end{aligned}
\]

Define the five-lock syndrome

\[
z_i\equiv\sum_{t\in L_i}\mu_t\pmod2.
\]

One mandatory copy of every target gives the baseline (z=11111).  Only an
extra weight-one service occurrence can toggle a lock bit, and the number of
such extra occurrences is at most (Q).  Therefore

\[
\operatorname{wt}(z)\ge5-Q.                  \tag{2.2}
\]

The authenticated closed-walk automaton proves the following exact finite
lemma for (0\le R\le3): every directed closed walk of slack (R), and every
XOR sum arising from an arbitrary integral cycle decomposition of total
slack (R), has

\[
\operatorname{wt}(z)\le R,
\qquad
\operatorname{wt}(z)\equiv R\pmod2.          \tag{2.3}
\]

Indeed, for both single closed walks and arbitrary split circulations, the
computed syndrome sets are exactly

\[
\{z\in\mathbb F_2^5:
  \operatorname{wt}(z)\le R,
  \operatorname{wt}(z)\equiv R\pmod2\}.
\]

If (C\le105), the direct dual first gives (C\ge104); hence by (2.1)
(Q+R\in\{1,3\}), and in particular (R\le3).  Combining (2.2) and (2.3)
gives

\[
5-Q\le R,
\quad\text{so}\quad
Q+R\ge5,
\]

a contradiction.  Thus (C\ge106).  ∎

This proof is stronger and cleaner than the explicit equality-face census.
The program nevertheless independently exhausts all 16 (C=104) vectors
and all 1,776 (C=105) vectors and records zero survivors.

## 3. Audit of the automaton lemma

The frozen C++ implementation performs the following exact steps.

1. It parses the raw ledger and the pinned dual, reconstructing all seam
   slacks and five-bit labels.
2. It contracts the slack-zero digraph into strongly connected components.
3. It verifies that every tight internal label is a coboundary and fixes a
   gauge on each tight component.
4. The remaining tight condensation is a DAG.  A batched dynamic program
   propagates all five-bit states through tight paths and through every
   positive-slack transition, for total slack at most three.
5. It records the exact closed-walk syndrome sets.  The XOR-product closure
   records arbitrary multisets of closed walks.  This is complete because
   every finite nonnegative integral balanced directed multigraph decomposes
   into directed closed walks.

Independent theorem audits checked the SCC contraction, gauge equations,
topological recurrence, cycle-splitting closure, all boundary cases in the
branch census, and the human inequality above.  No mathematical gap was
found.

## 4. Frozen lineage

The live working C++ and verifier filenames temporarily drifted after the
authenticated run, but have now been restored to the exact hashes below.
The immutable authority for this theorem is the separately preserved bundle
in
`scratch/k16_floor106_authenticated_frozen_20260730/` and also under the
explicit `*_r03_*_frozen_*` filenames in `scratch/`.

The authoritative hashes are:

| artifact | SHA-256 |
|---|---|
| frozen ledger | `832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657` |
| exact scale-two dual | `29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d` |
| frozen C++ automaton | `ed27cc92e6662754016e0e872b3a741c0f801261e5cc2e43c81419444fd49455` |
| frozen authenticated verifier | `59991d8befd070a4d6c38054e2a7a5220709650a1a944053ef5f290909bf12fe` |
| raw automaton audit | `ce4dcfeb9db976b0cfbac6a1ab3bf4d579ccae749785947b5ed4e5932ffc3373` |
| original authenticated wrapper | `e9db884cd069ebbf3218848832aecc469939836ba42cb134d64392ed866d0feb` |
| root replay wrapper | `93ae9e2e3a39b8a0530ff9c876eb033dcd4174123c50d0919c681a6eb107ea99` |
| Thread-A frozen replay wrapper | `eba07f402110510bcc2162d925530e24ae1595cf4ccacf832fe4c0236a920a65` |

The authenticated verifier recompiles the frozen C++ source and reproduces
the raw automaton JSON byte-for-byte.  The root and Thread-A replays are
fresh executions of the same implementation, not implementation-independent
automata.  Their wrapper JSON differs through elapsed time and therefore has
a different valid payload hash.  The compiler version string is recorded;
the compiler executable itself is not hash-pinned.

The raw C++ audit leaves nonnegativity and integrality implicit in its
closed-walk decomposition.  The authenticated wrapper explicitly says
“nonnegative” but does not say “integral.”  The proved and audited scope is
**nonnegative integral**.  No claim is made for fractional circulations.

## 5. Thread-A C=105 CNF cross-check

Before the five-lock theorem arrived, Thread A emitted deterministic compact
CNFs for all six aggregate (Q+R=3) faces, plus the same-target/distinct-target
split of the weight-one (Q=2,R=1) face.  The emitter is
`scratch/threadA_emit_k16_c105_capacity_face_cnf_20260730.py`, SHA-256

```text
0c81ac5ef352901416b8b019e6d6858538042e4cd13479c1d775eff7087ec255.
```

It enforces endpoint balance and port capacity one, all target lower bounds,
exact weight-group service totals, and exact total slack.  It omits the
redundant count row because the same telescoping identity forces (C=105).
Independent read-only semantic reviews passed; one review also checked 941
small truth-table instances of the truncated unary counter.  No standalone
truth-table artifact was retained, so the proof-producing CNFs and their
checked DRAT/LRAT bundles remain the durable finite certificates.

The primary CNFs are:

| face | variables | clauses | SHA-256 |
|---|---:|---:|---|
| (R=3,Q=0) | 1,891,866 | 6,002,817 | `140e69e9ea0626686a723581cc0eb9726e4d0cccdbf3841b049e44ad235f2d96` |
| (R=2,Q=1) | 1,170,300 | 3,520,678 | `9b66cc50224b053b55fb846b590c37b56a52f8d4df64b106ae6301fba4af6958` |
| (R=1,Q=2), two weight-one units | 81,178 | 225,000 | `6d97d552d9dea52fb5d61a2fdd5771cdfaf42ea83bc58d7466953cb6170ff8cc` |
| (R=1,Q=2), one weight-two unit | 232,599 | 826,402 | `c0d02cbb7b49a7f8bc2de65ce42fbeeb1b57c0fd4b83cc18accdf668931895f6` |
| (R=0,Q=3), weight-one only | 6,005 | 14,431 | `d9c06bd5c8fb3e36e2db6c4f60ff77ea3ad00c4586a452b385067b92bf58d1ce` |
| (R=0,Q=3), weight one plus weight two | 56,663 | 215,311 | `e622d0bffb5184844eeac092930636aecbfe1eb86d84d5f1c698e2aeeabb19b4` |

Kissat and CaDiCaL both returned UNSAT on the two (R=0) and two (R=1)
aggregate faces; their DRAT/LRAT proofs were checked.  The same-target and
distinct-target (R=1) subfaces were also separately proved UNSAT.  Both
solvers returned UNSAT on the (R=2) face, but its proof check was stopped
when the stronger automaton arrived.  Both (R=3) runs were terminated and
remain UNKNOWN as solver runs.  No solver status is used in Theorem 2.1.

The emitted formulas, completed proofs, logs, and interrupted-job ledgers are
preserved under
`scratch/threadA_k16_c105_capacity_proof_bundle_20260730/`.

## 6. Final boundary

The proved conclusion is exactly

\[
\boxed{C\ge106}
\]

for the frozen source-relative nonnegative-integral balanced/service seam
relaxation.  Because that model already relaxes binary port-capacitated seam
selection, all six (C=105) capacity faces are impossible.  Nothing here
proves unrestricted (K=16) nonexistence or rules out a construction using
seams outside the frozen catalogue.
