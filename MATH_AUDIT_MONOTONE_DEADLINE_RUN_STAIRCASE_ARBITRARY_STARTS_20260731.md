# Audit and arbitrary-start extension of the monotone-deadline run staircase

Date: 2026-07-31  
Root theorem: `MATH_THEOREM_MONOTONE_DEADLINE_RUN_STAIRCASE_20260731.md`  
Audited root SHA256:
`25362dab46213604949757748eece765e513caf37cf97657e72d826c809c4426`  
Verdict: the canonical-start theorem is correct in its stated row-exact and
scalar scope.  The exact extension below covers arbitrary omitted starts.

## 1. Canonical theorem audit

For starts \(s_i=i\), increasing deadlines \(e_i\), and an interior
coordinate run \([a,b]\), a physical position can carry that coordinate
only after the preceding absent row ends and before the following absent row
starts.  The safe integer corridor is

\[
 [e_{a-1}+1,b].
\]

It is nonempty exactly when \(b\ge e_{a-1}+1\), proving Theorem 2.1.  Runs
touching either carrier boundary are unconditional.  If
\(h_i=e_i-i\) and \(\tau_j=\min\{i:h_i\ge j\}\), a run of length \(j\)
starting at \(a\) is feasible exactly when \(a\le\tau_j\).  Taking cumulative
maxima over runs of length at most \(j\) gives precisely

\[
 \tau_j\ge\rho_j.
\]

The proper-prefix area is \(dW-\sum_j\tau_j\); the final \(d\) omitted
starts contribute \(\binom{d+1}{2}\).  Hence the scalar gate is exactly
\(\sum_j\tau_j\le\Delta\), and the minimum row-exact loss is
\(\sum_j\rho_j\).  Empty physical letters, positional pins, Hall, and the
common-cap equations remain separate gates.  The root theorem now states
those qualifications explicitly.

## 2. Arbitrary start and deadline thresholds

Let \(L=W+d\).  Encode arbitrary omitted starts and deadlines by two
nondecreasing vectors

\[
 0\le\alpha_1\le\cdots\le\alpha_d\le W,
 \qquad
 0\le\tau_1\le\cdots\le\tau_d\le W,
\]

with holes

\[
 x_j=\alpha_j+j-1,qquad y_j=\tau_j+j-1.
\tag{2.1}
\]

Put

\[
 g_i=|\{j:\alpha_j\le i\}|,qquad
 h_i=|\{j:\tau_j\le i\}|.
\]

The selected start and deadline of row \(i\) are

\[
 s_i=i+g_i,qquad q_i=i+h_i.
\tag{2.2}
\]

The row intervals are nonempty exactly when

\[
 \tau_j\le\alpha_j\qquad(1\le j\le d).
\tag{2.3}
\]

Indeed, (2.3) says that every deadline-height level activates no later than
the corresponding start-height level, equivalently \(h_i\ge g_i\) for every
row.  Chain alignment, when upper transfer is wanted, is the additional
literal condition

\[
 s_{i+1}\le q_i+1
 \quad\Longleftrightarrow\quad
 g_{i+1}\le h_i.
\tag{2.4}
\]

## 3. Exact arbitrary-start run theorem

### Theorem 3.1 (safe-corridor criterion)

For a legal schedule (2.2), an interior coordinate run \([a,b]\) is
recovered in every one of its rows if and only if

\[
 q_{a-1}+1<s_{b+1}.
\tag{3.1}
\]

Equivalently, with \(\ell=b-a+1\),

\[
 h_{a-1}<\ell+g_{b+1}.
\tag{3.2}
\]

#### Proof

A position carrying the coordinate must avoid the preceding absent row and
the following absent row, hence must lie in

\[
 J=[q_{a-1}+1,s_{b+1}-1].
\]

If \(J\ne\varnothing\), every owner interval \([s_i,q_i]\),
\(a\le i\le b\), meets \(J\): increasing deadlines give
\(q_i\ge q_{a-1}+1\), increasing starts give
\(s_i\le s_{b+1}-1\), and the row itself is legal.  A point of this
intersection witnesses the coordinate in row \(i\).  If \(J\) is empty, no
position can avoid both adjacent absent rows.  Substituting (2.2) gives
(3.2).  Boundary runs have only one adjacent absent row and remain
automatic.  \(\square\)

For fixed \(\alpha\), define the adjusted frontier

\[
 \rho_j^{\alpha}=
 \max\Bigl(
  \{a:\ [a,b]\text{ is an interior coordinate run and }
       (b-a+1)+g_{b+1}\le j\}\cup\{0\}
 \Bigr).
\tag{3.3}
\]

It is nondecreasing in \(j\).

### Corollary 3.2 (adjusted staircase criterion)

All middle rows are recovered coordinatewise if and only if

\[
 \tau_j\ge\rho_j^{\alpha}qquad(1\le j\le d).
\tag{3.4}
\]

This is row-OR exactness.  A legal nonempty physical word still requires the
maximal envelope to be nonempty at every position.  As in the root theorem,
each active row block has size at most \(d+1\), so the \(d\)-local
intersection condition is sufficient and a rank-\(r\) Johnson path with
\(r>d\) satisfies it.

## 4. Exact arbitrary-start capacity loss

For an omitted start \(x_j=\alpha_j+j-1\), the first owner starting after
it has row index \(\alpha_j\).  Its deadline is \(q_{\alpha_j}\); if
\(\alpha_j=W\), use \(q_W=L\).  The general P/Q cell identity therefore
specializes to

\[
 \boxed{
\operatorname{Loss}(\alpha,\tau)
 =\sum_{j=1}^{d}\tau_j
  +\sum_{j:\alpha_j<W}(L-q_{\alpha_j}(\tau))
 }.
\tag{4.1}
\]

Equivalently, with all \(j,t\in\{1,\ldots,d\}\),

\[
 \operatorname{Loss}(\alpha,\tau)
 =\sum_j\tau_j+sum_j(W-\alpha_j)
  +|\{(j,t):\alpha_j<\tau_t\}|.
\tag{4.1a}
\]

The first term is deadline-hole loss.  The second is the exact loss of
boundary cells at internal omitted starts.  Consequently

\[
 |{\cal C}_{\rm full}|
 =dW+{d+1\choose2}-\operatorname{Loss}(\alpha,\tau),
\tag{4.2}
\]

and scalar capacity is equivalent to

\[
 \operatorname{Loss}(\alpha,\tau)\le\Delta.
\tag{4.3}
\]

For fixed \(\alpha\), moving any deadline threshold right weakly decreases
every selected deadline and strictly increases \(\sum_j\tau_j\).  Thus the
unique minimum among legal row-exact schedules is attained at

\[
 \tau=\rho^{\alpha},
\]

provided \(\rho_j^{\alpha}\le\alpha_j\) for every \(j\).  Define

\[
 {\mathsf R}_d^{\alpha}(T)=
 \begin{cases}
 \operatorname{Loss}(\alpha,\rho^{\alpha}),
   &\rho^{\alpha}\le\alpha,\\
 +\infty,&\text{otherwise}.
 \end{cases}
\tag{4.4}
\]

Then the exact arbitrary-start row-exact/scalar criterion is

\[
 \boxed{
 \min_{0\le\alpha_1\le\cdots\le\alpha_d\le W}
 {\mathsf R}_d^{\alpha}(T)\le\Delta.
 }
\tag{4.5}
\]

If chain alignment is imposed, it is enough to test (2.4) at the canonical
choice \(\tau=\rho^{\alpha}\): increasing \(\tau\) only moves deadlines
left and cannot repair a failed chain inequality.  Nonempty-envelope, pin,
Hall, and common-cap requirements can force a nonminimal retained schedule
and must be audited separately.

The root theorem is the tail-start specialization
\(\alpha=(W,\ldots,W)\).  Its second sum in (4.1) vanishes,
\(g_i=0\), and \(\rho^{\alpha}=\rho\), recovering
\({\mathsf R}_d(T)=\sum_j\rho_j\).

## 5. K16 replay

The authenticated carrier is

    scratch/k16_trueff_commoncap_direct_cnf_20260731/
      k16_true_fourfilter_endpoint_reroot_targets_20260731.word

with SHA256

    c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906.

It has \(W=12870\), consists of all rank-eight masks exactly once, and has

\[
 \rho=(0,0,6384).
\]

The retained compiler schedule has

\[
 \alpha=(12870,12870,12870),\qquad
 \tau=(0,0,6386).
\]

Its loss is \(6386\), so (4.2) gives

\[
 3(12870)+6-6386=32230
\]

physical lower cells.  The retained schedule spends exactly two cells beyond
the minimal row-exact frontier.  Its scalar surplus is
\(32230-26332=5898\).  The authenticated singleton cap and common-cap
certificate, not Theorem 3.1, justify that deliberate retiming.

The value \(6384\) is also the global arbitrary-start minimum for this fixed
carrier.  Bit 11 has the final interior length-three run
\([6384,6386]\).  If some start threshold satisfies
\(\alpha_j\le6387\), then its start-loss term is at least

\[
 12873-(6387+3)=6483.
\]

If no start threshold does, then \(g_{6387}=0\), so the run has adjusted
length three and forces \(\tau_3\ge6384\).  Hence every arbitrary-start
schedule has loss at least \(6384\), attained by tail starts with
\(\tau=(0,0,6384)\).

## 6. K17 fixed sector chronologies: arbitrary-start no-go

Two authenticated fixed chronologies share the relevant profile.  The
first-occurrence raw chronology is

    scratch/k17_c7be_evenodd_firstoccurrence_sector_targets_20260731.word
    SHA 1f320529b533d8ec744ac6c2845c60f4507ed69e23d0fdeda46319ba8be94776.

The optimized upper-73 sector chronology named in the root theorem is

    scratch/k17_c7be_pascal_shadow_upper73_sector_targets_20260731.word
    SHA ea10337264c7998d227cf4c8ef5d5df463d5fb4efd9c29c7a1e0171d7b4897a4.

The root note currently calls the latter the “first raw concatenation”; the
hashes above remove that naming ambiguity.  Each file has \(W=24310\),
consists of all rank-nine masks exactly once, and has tail-start frontier

\[
 \rho=(11440,11440,17824),\qquad \sum_j\rho_j=40704>7401=\Delta_{17}.
\]

This canonical failure extends to every arbitrary start-hole vector for
either fixed chronology.  Bit 7 has the interior singleton run
\([11440,11440]\).  Suppose a schedule had loss at most \(7401\).

- If some \(\alpha_j\le11441\), then
  \(q_{\alpha_j}\le\alpha_j+3\), so the corresponding start-loss term in
  (4.1) is at least

  \[
   24313-(11441+3)=12869>7401,
  \]

  a contradiction.
- Otherwise \(g_{11441}=0\).  The singleton run has adjusted length one, so
  (3.4) forces \(\tau_1\ge11440\).  Monotonicity then gives
  \(\tau_1+\tau_2+\tau_3\ge34320>7401\), again a contradiction.

Therefore each fixed carrier is

\[
 \boxed{\text{UNSAT for middle row exactness plus scalar capacity over all
 arbitrary start/deadline holes}.}
\]

This conclusion precedes chain alignment, envelope nonemptiness, pins, Hall,
common cap, and upper transfer.  It does not rule out a rethreaded K17
carrier.

## 7. Independent finite audit

The deterministic audit exhausts every binary coordinate trace for every
legal threshold schedule with \(1\le W\le6\) and \(0\le d\le3\).  It checks
the literal maximal envelope, safe-corridor criterion, adjusted frontier,
legality, exact catalogue loss, and fixed-\(\alpha\) minimization.  It then
replays both finite carriers above.  The run reports:

- 5,223 legal arbitrary schedules;
- 241,260 schedule/coordinate-trace comparisons;
- 11,644 fixed-start minimizations;
- exact K16 frontier \((0,0,6384)\); and
- exact K17 frontier plus the bit-7 singleton obstruction.

Artifacts:

    scratch/audit_monotone_deadline_run_staircase_arbitrary_starts_20260731.py
      SHA 45be54382df8f1b788f877d603d1fdb9ceebb933e9a462119f479a01db9ccbbe
    scratch/monotone_deadline_run_staircase_arbitrary_starts_20260731.audit.json
      SHA 2962af618842e751c8ed0c20f3d9d102090acbf09a1f7bbcb82e7e4173309f4a
      payload 12aaa0a0436ae9248f7031b6eeced84d3ef1801c9e03b0f769929418b877d0bc

The JSON records the script, root theorem, and carrier hashes and contains a
stable payload hash.  This audit is mathematical/light verification only.
