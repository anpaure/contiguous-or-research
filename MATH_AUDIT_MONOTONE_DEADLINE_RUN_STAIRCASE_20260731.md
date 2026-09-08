# Independent audit of the monotone-deadline run staircase

## Verdict

The run--deadline equivalence, threshold/deadline bijection, and scalar
capacity identity in
MATH_THEOREM_MONOTONE_DEADLINE_RUN_STAIRCASE_20260731.md are correct for
the stated canonical schedule

\[
s_i=i,\qquad
\{e_0<\cdots<e_{W-1}\}=[0,W+d-1]\setminus Y.
\]

The theorem gives an exact carrier-row realization criterion and an exact
count of physical lower cells.  It is not by itself a valid-word or
lower-compiler theorem.

## 1. Independent derivation

For a coordinate run \([a,b]\), a physical position can contain the
coordinate precisely after the preceding absent row has expired and before
the following absent row begins.  For an interior run this safe interval is

\[
[e_{a-1}+1,b].
\]

Every carrier row \(i\in[a,b]\) intersects that safe interval if and only if
it is nonempty, because \(e_i>e_{a-1}\).  Hence the exact condition is

\[
b\ge e_{a-1}+1
\quad\Longleftrightarrow\quad
b-a+1\ge h_{a-1}+1.
\]

For a run of length \(\ell\), this says \(h_{a-1}<\ell\), equivalently
\(a\le\tau_\ell\).  Taking the last start over runs of length at most \(j\)
gives exactly \(\tau_j\ge\rho_j\).  Since \(\rho_j\) is nondecreasing, the
coordinatewise minimum feasible threshold vector is \(\tau=\rho\).

If \(y_j\) is the \(j\)-th omitted deadline, exactly \(j-1\) earlier
positions are omitted, so its retained-row cut is

\[
\tau_j=y_j-j+1.
\]

Thus \(y_j=\tau_j+j-1\), proving the claimed bijection.  Finally,

\[
\sum_i(d-h_i)=\sum_{j=1}^d\tau_j
\]

by counting pairs \((i,j)\) with \(h_i<j\).  Adding the
\(\binom{d+1}{2}\) cells beginning at the final \(d\) physical positions
gives exactly the displayed capacity criterion.

## 2. Exhaustive finite audit

An independent brute-force program checked every:

- binary carrier of length \(1\le W\le8\);
- depth \(0\le d\le4\); and
- \(d\)-subset of omitted deadlines in \([0,W+d-1]\).

For each case it compared:

1. literal maximal-envelope row recovery;
2. the interior-run inequality; and
3. the threshold/frontier inequalities.

All three predicates agreed in every case:

    PASS exhaustive W<=8,d<=4

This includes all left-boundary, right-boundary, all-one, all-zero, and
multiple-run configurations at those sizes.

## 3. Necessary scope corrections

Three qualifications were added to the theorem.

1. The left boundary is free because there is no preceding absent row; it
   is not supplied by a literal left physical tail.  The right boundary can
   use the final physical tail.
2. Scalar compatibility does not force a legal nonempty word.  Nonemptiness
   is the separate intersection condition in Lemma 2.2.  Nor does scalar
   capacity imply the Hall/common-cap lower assignment.
3. The \(k=17\) rejection applies to the canonical class with all omitted
   starts at the end.  It does not exclude schedules with internal omitted
   starts.

The audit script was extended with the omitted-deadlines option, so a
retained nonminimal schedule can now be replayed directly instead of
silently replacing it by \(\tau=\rho\).  It separately reports minimal
scalar feasibility, selected-schedule feasibility, row compatibility, and
maximal-envelope nonemptiness.

## 4. Numerical reproduction

### Authenticated \(k=16\) carrier

Carrier SHA-256:

    c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906

For the retained holes \(Y=\{0,1,6388\}\), an independent replay gives

| quantity | value |
|---|---:|
| \(W\) | 12870 |
| \(\rho\) | \((0,0,6384)\) |
| retained \(\tau\) | \((0,0,6386)\) |
| \(\Lambda\) | 26332 |
| \(\Delta\) | 12284 |
| proper-prefix area | 32224 |
| all physical lower cells | 32230 |
| empty maximal-envelope letters | 0 |

The retained schedule therefore spends exactly two more units than the
minimum staircase.

### Raw \(k=16\to17\) two-shore carrier

Carrier SHA-256:

    ea10337264c7998d227cf4c8ef5d5df463d5fb4efd9c29c7a1e0171d7b4897a4

Independent run enumeration gives

\[
\rho=(11440,11440,17824),\qquad
\mathsf R_3=40704,\qquad
\Delta_{17}=7401.
\]

The exact-length run census is:

| length | interior runs | last start |
|---:|---:|---:|
| 1 | 17 | 11440 |
| 2 | 139 | 11438 |
| 3 | 1821 | 17824 |

Thus the raw carrier is impossible in the canonical final-start-hole
schedule class by scalar capacity alone.  This is a sound negative for that
class, not a global \(k=17\) obstruction.

## 5. Audited artifacts

The theorem and script were independently read in full, the script
byte-compiled, and both numerical examples replayed.  Their final hashes
should be recorded only after concurrent documentation edits settle.
