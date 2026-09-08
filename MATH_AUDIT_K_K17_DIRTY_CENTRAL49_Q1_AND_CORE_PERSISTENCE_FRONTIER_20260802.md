# `k=17`: dirty-central 49-bank q1 closure and the exact retained-core frontier

Date: 2026-08-02  
Lane: K, proof-scope audit  
Face: two distinct-base, one-for-one recuts of the frozen round02 bank.

## 1. Result

The seven locally dirty central anchors are

\[
  1834:9924\longmapsto 9925,\ldots,9931.
\]

Each has exactly the same seven locally compensating partner recuts.  The
resulting (7\cdot7=49) final banks are distinct.  Every one passes the
literal zero-265 local ledger, but every one is q1-infeasible.

More precisely, the canonical proof replay reports

\[
\begin{array}{c|c}
\text{check}&\text{count}\\ \hline
\text{byte-identical final bank/CNF/maps rebuild}&49\\
\text{Kissat UNSAT (exit 20)}&49\\
\text{independent `drat-trim` VERIFIED}&49\\
\text{SAT}&0.
\end{array}
\]

Therefore dirty-single compensation is closed on this fixed Hamming-two
face.  This does not make either dirty singleton legal and says nothing
about an unlisted pair or another move class.

## 2. Independent replay and arithmetic

The adopted generator has 169,426 distinct joint-local-clean banks.  The
49 banks above are exactly the rows supported by the seven dirty central
anchors; the role-changing anchor `1835:9933->9932` has no jointly clean
partner.  Hence deletion of the proved-negative dirty slice leaves

\[
                 169426-49=169377                         \tag{2.1}
\]

banks, each containing at least one of the thirteen individually clean
anchors: the twelve visible socket escapes or the clean central state change
`1834:9924->9923`.

The imported proof manifest has 49 rows, 49 distinct bank hashes, 49
distinct CNF hashes and 49 distinct proof hashes.  A separate lightweight
replay checks the (7\times7) anchor/partner incidence and the arithmetic in
(2.1).

## 3. Retained-core persistence reduction

For a clean anchor (a), let ({\cal L}_a) be its authenticated library of
occurrence-labelled q1 contradictions.  A retained certificate records the
physical occurrence roles, complementation, complete effective provider
sets of its positive rows, resource clauses and named blockers.  The
literal-core, closed-fan, implication-bicycle and guarded-core-minor
criteria prove:

> If one such certificate embeds in the final two-recut formula, the final
> formula is UNSAT.  A bank is promoted to a fresh exact build whenever the
> selected filter cannot certify such an embedding.

This filter is one-sided: it has no false rejection, whereas promotion does
not mean SAT.

The frozen 13-profile semantic filter partitions the original clean census
as

\[
 169426
   =164323\ \text{persistence-certified UNSAT}
    +5103\ \text{fresh-build rows}.                      \tag{3.1}
\]

All 49 dirty-central banks lie in the second summand.  Combining (3.1) with
the exact 49-bank proof gives the sharper current frontier

\[
 \boxed{
 169426
   =164323\ \text{persistence-UNSAT}
    +49\ \text{dirty-central DRAT-UNSAT}
    +5054\ \text{unresolved}.}                           \tag{3.2}
\]

Thus 164,372 banks are now proved q1-negative and 5,054 banks, or about
2.983% of the joint-local-clean census, require a fresh q1 build under this
chosen core library.  The 5,054 are an upper bound on fresh builds: adding
authenticated cores can decrease it.  They are not feasible witnesses.

The first promotion reason of these 5,054 rows is distributed as

\[
3387\ \text{reference-endpoint touches},\quad
1100\ \text{new-out atoms},\quad
471\ \text{palette toggles},\quad
70\ \text{new-in atoms},\quad
26\ \text{new core-colour tail providers}.
\]

These are conservative disturbance labels, not certificates that the old
core is actually repairable.

The twelve visible source profiles have local checked proof manifests.  The
clean-central profile contributes 12,504 of the 164,323 semantic verdicts;
its q1 obstruction is also certified directly by the occurrence-labelled
final-atlas dual-fan criterion.  Its separate remote profile manifest is not
needed for that mathematical implication, but should be synced before a
claim that every source-profile proof artifact is locally self-contained.

## 4. Exact termination scope

The present result proves no monotonically decreasing recut potential.  It
gives a finite, proof-producing decision reduction:

1. the complete final-net anchor theorem generates every breaker on this
   fixed face;
2. the 49 dirty-central rows are closed by checked refutations;
3. retained semantic cores reject 164,323 clean-anchor rows; and
4. only the residual 5,054 need fresh exact q1 formulas.

Only if all 5,054 are rejected may one conclude that the fixed one-for-one
face has no Hamming-two q1 completion.  Even then the conclusion is only
that the next radius *inside this face* is at least three.  Added cuts,
alternative base cuts, split/merge moves, C6/C8/q4 rethreads and every
downstream rank-ten/deep-shadow, residence, topology and compiler condition
remain outside the theorem.

## 5. Frozen artifacts

The complete checked 49-bank bundle is represented locally by its compact
proof manifest and audit:

| artifact | SHA-256 |
|---|---|
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/proof_manifest.tsv` | `7959c9ce00d855cd187fe24e770e785f908dee5106cef8daf75480a75d55c0b6` |
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/theorem.audit.json` | `bf468abc0fd076613c81b21468f23e8e947e153eeff3d85e4bb52b15705e32f9` |
| `scratch/threadD_k17_round02_dirtycentral49_q1_20260802/THEOREM_SCOPE.txt` | `bcda315af6bff664e7cb4a29df52479af4218e0008423a2a537bfa12316ca81d` |
| remote full `artifacts.sha256` | `52eba4e2c2869b5b04324062f3959f733e464338d6ce8de577aaaf5b25d89ca9` |
| local `final.sha256` | `4601e6efa6282ebbc8a6b23f395a218bb24cb9a5bfdeab671acc4887411e64ad` |

The semantic persistence census is frozen at

| artifact | SHA-256 |
|---|---|
| `scratch/threadD_k17_round02_semantic_filter_20260802/audit.json` | `d90115ba056c0ca9b0e98d17db652abfe0cec3883f3d49c08cac19b323a3d77a` |
| `scratch/threadD_k17_round02_semantic_filter_20260802/counts.tsv` | `8097bec379e2fee7e550190a65f9ff51d085eb79cd13e9773bfaece7f24d7f40` |
| `scratch/threadD_k17_round02_semantic_filter_20260802/filter.tsv` | `3e46a46861006379406d4cbdf4c142491b338f3f5f1e8873a080d6c83b9f1238` |

The full DRAT files remain in the bound H100 bundle; the local manifest
records their individual hashes.  No solver output outside that manifest is
used here.
