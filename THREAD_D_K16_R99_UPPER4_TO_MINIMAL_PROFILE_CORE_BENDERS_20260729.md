# Thread D: r99 upper4-to-profile-core Benders update

Date: 2026-07-29  
Status: one new exact Hall row and one subset-minimal exact recourse-profile
row proved for the retain branch; neither radius-99 branch is closed.

## 1. Provenance-safe resumes

The authenticated retain history

```text
scratch/k16_r99_joint_guarded_upper4_retain_r103_native_20260729.json
SHA-256 b005a07ce33382e0d15e5fd86394164460338c9fa2d8839fd2bc699d739d6982
```

contains 103 rounds, 142 historical same-palette Hall rows and 103
historical joint rows.  Its producer predates the authoritative upper4
metadata, so it is cut history, not a current-model certificate.  The
fail-closed adapter

```text
scratch/threadD_prepare_k16_r99_retain_r103_hall_bootstrap_20260729.py
SHA-256 850930214a6ca3c43dd53ef9a3e2287d623ff55d2aa6fa8fb4f7688248015a2c
```

semantically replayed all 142 Hall rows, removed the two rows already in the
current eager portal-Hall set, imported 140 rows, ignored all 103 historical
joint rows, and reconstructed upper4 from the current theorem audit.  The
materialized v4 checkpoint is

```text
scratch/threadD_k16_r99_retain_r103_hall_bootstrap_20260729.json
SHA-256 3fc624326ef53ebf42da67c410c8bed18a38465b79d02e1c03df3873e9404089
payload 53d7c180430579340a4657d39bbb7cdb0aa74ffabbf05389e3119b9edb854f27
```

and was generated on H100 without a solver in 1.98 seconds at 87,692 KiB
peak RSS.

The current delete history reached round 83:

```text
scratch/k16_r99_joint_guarded_upper4_delete_r83_native_20260729.json
SHA-256 80199acbfcb100da780e86cb982f996e439a5d3bc0de688900aaeb803c4218a5
payload 34cf25077d19db4f13ac84e6f294643b264d4ae893824455f401bdae94c8a2c3
```

It has 116 Hall and 85 joint rows.  Its last cut is Hall-clean but violates a
joint-cover row by six.  Its upper4 dependency is an older byte version, so
this file also remains authenticated history pending the same current-row
normalization; no delete-branch conclusion is drawn here.

## 2. First current exact master attempt

The current lifted master with the 140 imported retain rows has 21,645
Boolean variables.  Its branch-free exact recourse has 27,428 variables and
2,387 constraints.  A one-worker 180-second master call returned `UNKNOWN`:

```text
scratch/threadD_k16_r99_exact_retain_r103_round1_20260729.json
SHA-256 81b5284d264a413a6cc1dec1d70b409ca1a06dbf1eacc2c2b7ae0ef0e0d88c7e
```

Peak RSS was 301,392 KiB.  No cut, infeasibility, or feasibility statement
follows from this result.

## 3. New exact same-palette Hall row

The guarded master was reordered fail-closed: exact Hall separation now
precedes the expensive joint threshold oracle, a found Hall row is persisted
immediately, and a joint timeout is recorded as inconclusive.  The current
source is

```text
scratch/search_k16_r99_joint_cover_cegar_20260729.py
SHA-256 9638b42730461eea9cb3b441796ad80ff367aadfc2c4927b7d0fe7ca0de6913b
```

It also runs each helper in a fresh process group and kills that group on
timeout.  Two orphaned solver children left by the pre-hardening source were
explicitly terminated; no r99 worker was left running.

From r103 the current upper4-aware round found cut

```text
667fe1f795699d0f543b3429e170ef12b0dbf4d7b97f12c680b43c9720424641
```

and the new lower Hall row

\[
 \sum_{h\in F}|\operatorname{ends}(h)\cap P|x_h
 \;\ge\;x_{2169}+x_{2898},                                      \tag{H104}
\]

where

\[
P=\{38,39,55,75,76,132,133,211,328,351,352,524,525\}.
\]

The two colours are `(0,1231)` and `(0,1239)`.  Every loopless off-source
provider of either colour meets `P`; exact degree restitution and distinct
colour use therefore prove (H104).  At the discovery cut its two sides are
`1<2`.  The current-schema row SHA is
`fc9556e0623af0a9b9fe3c07515cf00b50eb69d205a1895788617186556f34bf`.
The full checkpoint is

```text
scratch/threadD_k16_r99_guarded_upper4_retain_r104_failclosed_20260729.json
SHA-256 d1c620835aa1ab6eb8d1bd6e8071978e0da5b1eac08b6e32ee7730c058e70e98
payload 9bdac72cd1d187177c500cc25a64bc760bbf556757b62271f224190165c25554
```

## 4. Hall-clean r105 and exact recourse failure

After adding (H104), the next master cut was

```text
40339f5f3096867b019c2ce24b752cdae7c03e002e6d32ba4dcf4501f747c087.
```

Both same-palette Hall deficits are zero.  The exact integral joint-cover
threshold query timed out after 315 seconds; the patched runner preserved the
candidate and asserted no joint conclusion:

```text
scratch/threadD_k16_r99_guarded_upper4_retain_r105_jointunknown_20260729.json
SHA-256 665b60f3eafabb8948293c8b00cd75b3ba7ee5a44d5081b9b5af3051b5ca98bf
payload d7267773edfc043c23a8c1fee73bb5deeb24f951754596b2d1a8aa10071fafa3
```

The full fixed-cut model then used all 26,570 loopless off-source seams,
exact endpoint degrees, and every lost lower/upper q1 row.  It has 27,764
variables and 1,195 guarded constraints for this cut (69 lost lower and 69
lost upper rows).  CP-SAT proved it infeasible in 1.13 seconds.  The final
21-feature core replayed infeasible in 1.11 seconds.  Deleting each one of
the 21 features produced an independently replayed feasible 99-seam witness,
so the core is subset-minimal in this feature system.

The exact artifact is

```text
scratch/threadD_k16_r99_retain_r105_fixed_recourse_minimal_core_20260729.json
SHA-256 ba56f188ec49c8a30c867623470aad6c1b3f8541c311a9cd4715fc1ef7d8c2bf
payload c8d65e5c8a8e3766a87a5b8cbbcd238d36d8a4c8d48346d5f2849437b804ceb4
```

## 5. Minimal profile-core Benders theorem

For a source cut `x`, let

\[
b_v(x)=\sum_{e\in F:\,v\in e}x_e\in\{0,1,2\}.
\]

Put

```text
Z = {397,399,465,476,501,544,590,592,
     661,713,728,772,777,821,843,851}.
```

Let `z_v=[b_v=0]`, let `u_v=[b_v<=1]`, and use the three source-unique lost
colour indicators

```text
x_17223  for lower (1,693),
x_20660  for upper (1,5805),
x_20691  for upper (1,5813).
```

Then every exact degree-plus-both-q1 completion satisfies

\[
 \boxed{
   \sum_{v\in Z}z_v+u_{823}+u_{845}
   +x_{17223}+x_{20660}+x_{20691}\le20.}                  \tag{PC105}
\]

**Proof.**  If all 21 indicators equal one, the cut satisfies every guarded
feature in the replayed core.  Any exact seam completion would then satisfy
the corresponding guarded recourse model, contradicting its independently
replayed `INFEASIBLE` status.  Thus at least one indicator is zero, which is
exactly (PC105).  The recourse model contains no branch lock, so (PC105) is
valid in both retain and delete masters.  \(\square\)

The indicators have exact linear channels.  For `b_v in {0,1,2}`,

\[
 b_v\le2(1-z_v),\quad b_v\ge1-z_v
\]

is equivalent to `z_v=[b_v=0]`, while

\[
 b_v\le2-u_v,\quad b_v\ge2(1-u_v)
\]

is equivalent to `u_v=[b_v<=1]`.  For a general source-provider set `S_c`,
the lost-colour bit has the exact AND channel

\[
 \ell_c\le x_e\ (e\in S_c),\qquad
 \ell_c\ge\sum_{e\in S_c}x_e-|S_c|+1.
\]

Hence (PC105) is directly CP-SAT/0-1-linear encodable, not a candidate-only
no-good.  The full 99-edge incumbent no-good is also valid but weaker.

The independent solver-free profile replay is

```text
scratch/threadD_k16_r99_retain_r105_state_core_and_hall_20260729.audit.json
SHA-256 0ff37f35db85155f97f064c189bb86e25876f4224f52cfd78bc40510041df4e4
payload 7914307310d4fb022ddf11e62118b276bea688e7281652b5564e2225ba5cf820
```

Its solver-free source is
`scratch/audit_threadD_k16_r99_retain_r105_state_core_20260729.py`, SHA-256
`2daebcf6b06cfffe3f1dfa9c3168ec3f0963fcaef649a5c009618cc2753fe429`.

It evaluates (PC105) as follows:

| cut | true core features | excluded by (PC105) |
|---|---:|---:|
| retain r103 | 20 | no |
| retain r104 | 21 | yes |
| retain r105 | 21 | yes |
| delete r83 | 18 | no |

Subset-minimality means every one-feature deletion admits a seam witness for
the remaining 20 features.  It does not assert facetness or minimum support
over all possible feature languages.

## 6. Exact surviving gate

No radius-99 branch is closed, and no exact repair was found.  The precise
next operation is to install profile rows of the form (PC105) in the cut
master using the exact channels above, then repeat:

1. current upper4 plus canonical Hall separation;
2. exact fixed-cut degree/both-q1 recourse;
3. add a replayed profile core or accept an explicit 99-seam repair.

The cut space is finite, so full incumbent no-goods alone give finite
termination whenever all subproblem calls are conclusive.  Profile cores are
the stronger reusable family exposed by this iteration.  Connectivity,
voltage, fresh residence and deeper shadows remain downstream of a positive
q1 repair.

## 7. Resource and execution audit

All solving ran on H100 CPU with one worker, BLAS/OpenMP thread caps, and
`ulimit -v 2097152` (2 GiB).  No heavy local process was run.

| operation | wall time | peak RSS |
|---|---:|---:|
| r103 semantic bootstrap | 1.98 s | 87,692 KiB |
| current lifted master, `UNKNOWN` | 3:02.60 | 301,392 KiB |
| r104 exact Hall extraction | 25.23 s | 1,978,416 KiB |
| r105 persisted joint timeout | 5:40.77 | 1,978,916 KiB |
| subset-minimal exact profile core | 1:00.24 | 405,688 KiB |

Reusable launchers are

```text
scratch/threadD_k16_r99_guarded_current_round1_h100_20260729.sh
SHA-256 78727947d30e8cd72e7c406d9475cf013392b6ec1f50c34927c0868409d85143

scratch/threadD_k16_r99_fixed_recourse_r105_h100_20260729.sh
SHA-256 89f6b93b7d46dfb85c192ff068fecc3d037fb1fbe64f71e91b278f21121952e9
```

Both refuse nonfresh output roots, overlapping r99 jobs, hash drift, and a
busy exact-lane lock.
