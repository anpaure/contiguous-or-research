# Thread D: exact mixed-palette endpoint-capacity Farkas separator

Date: 2026-07-29  
Status: source-complete and syntax-checked; **not executed**.  Candidate
separation/replay is H100-CPU-only and remains unlaunched pending an assigned
memory slot.

## 1. The row family

Let `x_h` denote deletion of source seam `h`, let

\[
 b_v(x)=\sum_{h\ni v}x_h,
 \qquad
 r_c(x)=\sum_{h\in S_c}x_h-|S_c|+1,
\]

and let `B` be add-seam endpoint incidence and `Q` lower/upper q1-colour
incidence.  Every nonnegative pair `(lambda,w)` satisfying

\[
                 Q^T\lambda\le B^Tw
\]

gives the globally valid, branch-independent Benders row

\[
                 \lambda^Tr(x)\le w^Tb(x).                 \tag{1}
\]

The separator optimizes

\[
\max\{\lambda^Tr(x)-w^Tb(x):
 Q^T\lambda\le B^Tw,\ 0\le\lambda\le1,\ 0\le w\le2\}.    \tag{2}
\]

The box in (2) is without loss.  A violating homogeneous Farkas ray has
`max_c lambda_c>0` (otherwise its objective is nonpositive), so scale it to
`max_c lambda_c=1`.  Every add seam carries at most two protected labels,
and hence `Q_a^T lambda<=2`.  If some `w_v>2`, replace it by two.  Every seam
incident with `v` still has endpoint price at least two, every other column is
unchanged, and `w^T b(x)` can only decrease because `b(x)>=0`.  Repeating
this truncation gives `0<=w<=2` while preserving the violation.

This is the exact Farkas separator for fractional mixed lower/upper
endpoint-capacity recourse.  It contains the certified upper-four endpoint
row, every same-palette endpoint-cover row, and every normalized joint-cover
row.  It is not an integral exact-degree theorem.

The joint-cover embedding uses the endpoint baseline explicitly.  If
`a_c,b_c,gamma_v` are lower-colour, upper-colour, and endpoint cover weights
with

\[
 a_{\ell(s)}+b_{u(s)}+\gamma_i+\gamma_j\ge1
 \quad(s=ij),
\]

then set

\[
 \lambda_c=1-a_c\ (c\text{ lower}),\qquad
 \lambda_c=1-b_c\ (c\text{ upper}),\qquad
 w_v=\tfrac12+\gamma_v.                                    \tag{2a}
\]

For a seam carrying both protected labels, its cover row is exactly
`Q^T lambda <= B^T w`; with only one protected label the two endpoint halves
already pay one unit.  The loopless identity
`(1/2) sum_v b_v(x)=sum_h x_h=99` then rearranges (1) into the stored joint
cover inequality.  Thus every recorded joint-cover deficit is automatically
a violation of the mixed Farkas family; this containment does not require
source uniqueness for the definition of `r_c(x)`.

For a returned numerical solution, the implementation chooses a decimal
denominator `D`, replaces every `lambda_c` by `floor(D lambda_c)` and every
`w_v` by `ceil(D w_v)`, and checks all 26,570 add-seam inequalities with
Python integers.  It reports a row only when the exact integer margin is
positive.  Failure to recover such weights is `INCONCLUSIVE`; it never
certifies feasibility or absence of a violated row.

Expanding (1) in source-cut variables gives the integer row

\[
 \sum_c\Lambda_c(|S_c|-1)
 +\sum_{h\in F_0}
 \left(\sum_{v\in h}W_v-\sum_{c:h\in S_c}\Lambda_c\right)x_h
 \ge0,                                                       \tag{3}
\]

which the certificate stores after gcd normalization.  Replay regenerates
both (1) and (3), their exact margin, and the complete column census.

## 2. Frozen source and exact size

The source is

```text
scratch/k16_dynamic_cross_r147_round0_seed16822_20260729.json
SHA-256 d1662b09981bbfe3fbd25e46bad045c628407eda9d1c52936ca39c721151a7c8
```

and the catalogue digest is

```text
e5ffa02199834c476f45b314b2eacfbaa1866a74895cc0aa4e12744c8d157ff3.
```

The LP has exactly:

| item | count |
|---|---:|
| lower prize variables | 764 |
| upper prize variables | 764 |
| endpoint-price variables | 858 |
| total variables | 2,386 |
| loopless off-source column inequalities | 26,570 |
| nonzeros | 106,280 |

Every matrix row has two `+1` prize entries and two `-1` endpoint entries.
With float64 data and int32 CSR indices, the exact CSR payload is 1,381,644
bytes.  CSR, objective, right side, bound array, and returned solution occupy
1,670,556 declared numeric-array bytes.  These figures do not estimate
Python, catalogue, SciPy, or HiGHS overhead; the enforced `RLIMIT_AS` is the
actual process bound.

The frozen static audit is

```text
scratch/threadD_k16_r99_mixed_endpoint_farkas_static_size_20260729.audit.json
```

## 3. H100-only launch contract

The source is

```text
scratch/threadD_k16_r99_mixed_endpoint_farkas_separator_20260729.py
SHA-256 fe9511c467425f15a015ea063a36085318531d7eeb435654b07c67e794fd093a
```

It refuses candidate work unless the short hostname is `arboghast`, workers
equal one, and the requested address-space cap is at most 2,048 MiB.  It sets
the common BLAS/OpenMP thread variables to one, applies `RLIMIT_AS`, and takes
a nonblocking host-wide lock so duplicate separator/replay jobs fail closed.
It also refuses to overwrite an existing result.

After explicit server-headroom authorization, a first retained-branch test
should use the best Hall-clean historical candidate, round 39:

```bash
python3 scratch/threadD_k16_r99_mixed_endpoint_farkas_separator_20260729.py \
  --separate \
  --candidate scratch/k16_r99_joint_guarded_upper4_retain_r43_20260729.json \
  --round 39 \
  --output scratch/threadD_k16_r99_mixed_farkas_retain_r39_20260729.json \
  --seconds 300 --workers 1 --memory-mib 2048
```

Only after that process ends should delete round 9 be tested analogously.
Replay uses `--replay --certificate FILE --workers 1 --memory-mib 2048` and
is subject to the same H100 lock and cap.

No command in this section was run while preparing this note.

## 4. Exact scope boundary

A positive certificate rules out its candidate and any other cut violating
the emitted affine row.  A nonpositive numerical optimum, timeout, import
failure, or unsuccessful integer reconstruction proves nothing.

Passing the complete family (1) proves fractional feasibility only for
`By<=b(x), Qy>=r(x)`.  The next stronger fractional tier uses exact degree,
unit bounds, a free endpoint potential `pi`, and nonnegative upper-bound
slacks `s`:

\[
 Q^T\lambda\le B^T\pi+s,
 \qquad
 \lambda^Tr(x)\le\pi^Tb(x)+\sum_as_a.
\]

Even that does not remove the integral alternating-rectangle obstruction.
An exact branch closure still requires branch-free integral recourse
assumption cores, or an explicit integral repair.  Connectivity, voltage,
residence, and deeper shadows follow only after q1 recourse succeeds.

## 5. Physical-overlay specialization: do not feed it to the r99 driver

The detector-zero artifact

```text
scratch/k16_q1_endpoint_resume1_failedlit0_20260729.json
```

is a literal 12,870-edge physical factor, not a 99-edge quotient cut.  The
driver documented above must reject it.  Its correct mixed-Hall instance uses
the 12,479 physical red seams `R\Q`, the 12,479 physical blue seams `Q\R`,
and 22,880 physical lower/upper q1 resources.

That instance now has a solver-free sparse certificate.  Twenty-one colour
prices in `{1,2}` and nine endpoint prices in `{1,2}` satisfy every one of
the 12,479 red-column inequalities and expand to

```text
b11795+b11796+b11821 <= 0.
```

Motif 390 requires the same sum at least one.  The physical fixed overlay is
therefore LP-infeasible with integer margin one.  Its separate proof-safe
implementation is

```text
MATH_THEOREM_L_K16_FAILEDLIT0_MIXED_HALL_CORE_AND_ESCAPE_20260729.md
scratch/audit_k16_failedlit0_mixed_hall_farkas_20260729.py
scratch/k16_failedlit0_mixed_hall_farkas_20260729.audit.json.
```

This is the integration boundary: reuse the dual mathematics and certificate
schema, but not the r99 source/candidate parser or quotient coordinate map.
