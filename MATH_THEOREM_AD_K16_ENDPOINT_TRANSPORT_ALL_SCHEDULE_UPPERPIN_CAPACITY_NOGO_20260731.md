# The K16 endpoint-transport carrier: two independent all-P/Q upper-pin no-gos

**Date:** 2026-07-31  
**Status:** exact solver-free-compatible event-DAG theorem; independently reproduced headline optima

## 1. Authenticated carrier

This note concerns only

```text
scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word
SHA-256 9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b.
```

The file contains each of the \({16\choose8}=12870\) rank-eight masks once.
Its adjacent-union rank-nine palette is complete.  Its unrestricted
target-order upper audit has exactly two holes:

\[
U_1=\mathtt{3ceb},\qquad U_2=\mathtt{a9fe}.              \tag{1.1}
\]

The displayed maximum-area P/Q schedule is

\[
X=\{12870,12871,12872\},\qquad Y=\{0,1,8589\},          \tag{1.2}
\]

with selected area \(30023\) and \(30029\) physical lower cells.  Its exact
lower matching is \(26327/26332\), deficiency five, with four zero-host
targets

```text
29cc, 38c6, 8000, 898d.
```

The fixed-schedule Hall result is not decisive below: the whole monotone
depth-three P/Q architecture is impossible for this target order.

## 2. Recalled exact pin and length criteria

For scheduled middle intervals \(I_i=[p_i,q_i]\), define

\[
E_j=\bigcap_{i:j\in I_i}T_i,
\qquad
H_{i,x}=\{j\in I_i:x\in E_j\}.                          \tag{2.1}
\]

A physical interval \(J\) can be capped to a target \(U\), while keeping
every cell nonempty and preserving every middle row, if and only if

\[
E_j\cap U\ne\varnothing\quad(j\in J),                  \tag{2.2}
\]

\[
U\subseteq\bigcup_{j\in J}E_j,                          \tag{2.3}
\]

and

\[
H_{i,x}\not\subseteq J
\quad\text{for every }x\in T_i\setminus U.              \tag{2.4}
\]

Sufficiency uses \(E_j\cap U\) on \(J\) and \(E_j\) elsewhere.  Necessity
is immediate from any physical realization.  This is the exact individual
pin criterion, including all middle-bit losses.

If there are \(h\) omitted starts, all row spans are at most \(d\), and

\[
\rho_T(U)=\max\{s:T_a,\ldots,T_{a+s-1}\subseteq U\},     \tag{2.5}
\]

then every legal \(U\)-pin obeys

\[
|J|\le d+h+\rho_T(U).                                   \tag{2.6}
\]

Indeed, among the first \(|J|-d\) possible starts of \(J\), at most \(h\)
are omitted.  Every remaining row interval lies wholly in \(J\), so its
target must be a subset of \(U\).  Those rows are consecutive, giving
(2.6).

Here \(d=h=3\).  The exact compatible-owner censuses are

\[
\rho_T(\mathtt{3ceb})=2,qquad
\rho_T(\mathtt{a9fe})=4.                                \tag{2.7}
\]

There are respectively \(45\) and \(165\) compatible rank-eight owners.
Thus every possible pin has length at most

\[
8\quad\text{or}\quad10.                                 \tag{2.8}
\]

These are proved global bounds for this target order, not arbitrary search
windows.

## 3. Exact all-schedule event DAG

The event DAG scans the \(12873\) physical positions.  A state stores

\[
(x,y,Q,\phi,R,\ell),                                    \tag{3.1}
\]

where \(x,y\) count used start/deadline holes, \(Q\) is the ordered queue of
actual capped row accumulators, \(\phi\) is the before/inside/after pin
phase, \(R\) is the current pin OR, and \(\ell\) is its length.  Each
transition tries both start-hole and both deadline-hole choices.  The cell
is the active-target intersection outside the pin and its intersection with
\(U\) inside.  Empty cells and incorrect ending rows are rejected.

Once \(R=U\), the pin is ended immediately without loss: restoring later
cells to their uncapped envelopes can only help middle rows.  Histories at
the same state are therefore merged by retaining the largest selected area

\[
A=\sum_i(q_i-p_i).                                      \tag{3.2}
\]

The future depends only on (3.1), so this dominance is exact.  Bounds (2.8)
make the two finite DAGs exhaustive for arbitrary physical pins.

### Theorem 3.1 (exact optima)

The complete results are

| required pin | maximum states/layer | max selected area | optimistic capacity \(A+9\) | gap to 26332 |
|---|---:|---:|---:|---:|
| `3ceb` | 82 | 25740 | 25749 | 583 |
| `a9fe` | 128 | 25743 | 25752 | 580 |

A maximizing `3ceb` history has

\[
X=\{12870,12871,12872\},\quad
Y=\{0,1,12872\},\quad J=[12872,12872].                 \tag{3.3}
\]

A maximizing `a9fe` history has

\[
X=\{6102,12871,12872\},\quad
Y=\{0,1,6101\},\quad J=[6096,6101].                    \tag{3.4}
\]

Direct maximal-cap reconstruction gives zero middle failures and the exact
pin OR in each case.  Their actual omitted-start credits are six, so their
actual candidate lower-cell counts are \(25746\) and \(25749\); the theorem
uses the more generous uniform credit nine.

### Corollary 3.2 (endpoint carrier is P/Q-dead)

No monotone depth-three P/Q schedule for SHA `9142910f...` can realize all
middle targets, either one of the required upper targets in (1.1), and all
\(26332\) lower targets.  In particular, the two upper pins cannot coexist
with a lower perfect matching or a common capped word.

#### Proof

Every upper-complete realization needs each target in (1.1).  By (2.8), its
pin is represented in the corresponding complete event DAG.  At a selected
start, at most \(q_i-p_i\) proper prefixes can be lower; the three omitted
starts add at most nine further lower cells.  The two upper bounds in the
table are both below \(26332\).  \(\square\)

## 4. Fixed maximum-schedule audit

For the schedule (1.2), neither target has a legal capped pin or a literal
maximal-envelope pin.  Exact first-reach statistics are

| target | capped intervals first reaching target | minimum length | legal after middle-host test | literal maximal-envelope pins |
|---|---:|---:|---:|---:|
| `3ceb` | 12799 | 6 | 0 | 0 |
| `a9fe` | 8596 | 6 | 0 | 0 |

Thus the displayed Hall-five schedule fails before any joint upper/lower
cap.  The all-schedule theorem shows that changing only \(X,Y\) cannot fix
this.

## 5. Independent lower target cross-check

There is a second, upper-independent obstruction.  In an equality-length
P/Q compiler, a lower occurrence has length at most three.  Augmenting the
same exact event DAG by a required `8000` pin of length at most three gives

\[
A_{\max}(\mathtt{8000})=25776,qquad A_{\max}+9=25785.   \tag{5.1}
\]

The DAG has at most \(47\) states per layer.  One maximizing history is

\[
X=\{6175,12871,12872\},\quad
Y=\{0,1,6141\},\quad J=[6142,6142].                     \tag{5.2}
\]

The optimistic capacity in (5.1) is still \(547\) below \(26332\).  Hence
the endpoint carrier is independently P/Q-dead even if both upper holes are
ignored.  This cross-check was also reproduced by a separate lane.

## 6. Comparison with the original def4 carrier

The scopes must not be merged:

| carrier | SHA prefix | q1 status | upper holes | decisive compatible run | all-schedule optimistic capacity |
|---|---|---|---|---:|---:|
| original def4 | `0a3a34c4` | missing `b8ce` | `a9fe,b8ce,b8cf` | \(\rho(b8ce)=1\) | 25754 |
| endpoint transport | `9142910f` | complete | `3ceb,a9fe` | \(\rho(3ceb)=2\), \(\rho(a9fe)=4\) | 25749, 25752 |

Endpoint transport succeeds at the rank-nine palette but moves the exact
obstruction to two higher targets.  Both chronologies are dead under all
monotone depth-three P/Q schedules, for separately authenticated reasons.
Neither result excludes a new target order or a non-P/Q equality
architecture.

## 7. Frozen artifacts

```text
scratch/audit_ad_k16_endpoint_transport_all_schedule_upperpin_capacity_20260731.py
scratch/ad_k16_endpoint_transport_all_schedule_upperpin_capacity_20260731.audit.json
```

The JSON payload SHA-256 is

```text
1df1d218ab2cd2d5236c044e727d5e0921f716912ffa2af769e1457007d52d24.
```

The imported generic recurrence and its original-carrier audit are frozen
separately in

```text
scratch/audit_ad_k16_def4_b8ce_shortpin_capacity_20260731.py
scratch/ad_k16_def4_b8ce_all_schedule_shortpin_capacity_20260731.audit.json.
```
