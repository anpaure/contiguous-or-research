# Type-I suffix-core exact subcube encoding

## 1. Guard and theorem

The existing exact six-subcube module is strengthened when both

```text
K11_FOREST_SUBCUBE_DEFICIENCY=1
K11_FOREST_RANK_FILTRATION_TYPE1=1
```

are enabled.  Type I already requires `K11_FOREST_RANK6_BRANCH=1`, whose
audited canonical orientation fixes

```text
A[0]=63
```

as the unique literal six-set entry.  The rank-at-most-five core is the
suffix positions `1,...,464`.  If

\[
 p_U^C=\#\{i\in\{1,\ldots,464\}:A_i\subseteq U\},
 \qquad
 a_j^C=\#\{U:p_U^C=j\},
\]

the exact proper-target run-credit theorem gives

\[
 7a_{28}^C+5a_{29}^C+3a_{30}^C+a_{31}^C\le461. \tag{1.1}
\]

This is an unrestricted necessary condition inside the exact Type-I branch.

## 2. Why only one support count changes

The unrestricted module already defines, for every six-set `U`, all 465
support indicators and their exact population count

\[
 p_U=\#\{0\le i<465:A_i\subseteq U\}.
\]

Because `A[0]=63` and both `63` and `U` have rank six,

\[
 63\subseteq U\quad\Longleftrightarrow\quad U=63.
\]

Consequently

\[
 p_U^C=p_U\quad(U\ne63),\qquad p_{63}^C=p_{63}-1. \tag{2.1}
\]

No second bank of support indicators and no second 464-input population
counter is needed.

## 3. Exact charge correction

On the independently proved active range, the unrestricted charge is

```text
p:          28 29 30 31 >=32
gamma(p):    7  5  3  1   0
```

and the proper-target core charge `eta` has the same table.  Equation (2.1)
and `p_63^C>=28` imply `p_63>=29`.  Direct evaluation gives

\[
 \eta(p_{63}-1)-\gamma(p_{63})
   =2\mathbf1_{p_{63}\le31}+\mathbf1_{p_{63}=32}. \tag{3.1}
\]

The source retains the already exact flag

```text
endpoint_low31 <-> (p_63 <= 31)
```

and adds one exact conjunction flag

```text
eq32 <-> (p_63 == 32).
```

It then ripple-adds the two-bit correction

```text
eq32 + 2*endpoint_low31
```

to the existing exact global charge sum and compares the result to 461.
This is algebraically identical to (1.1).

## 4. Exact incremental inventory

The combined guard adds to `SubcubeRunCreditPlan`:

| component | variables | clauses |
|---|---:|---:|
| `p_63>=29` comparator | 0 | 4 |
| exact `p_63=32` flag | 1 | 10 |
| 12-bit ripple addition | 24 | 168 |
| corrected sum `<=461` | 0 | 7 |
| **total** | **25** | **189** |

Thus the unrestricted subcube module remains exactly

```text
646781 variables / 4309410 clauses
```

outside Type I, while the Type-I instance is

```text
646806 variables / 4309599 clauses.
```

The fully integrated production-style Type-I build changes from

```text
3633096 variables / 19448397 clauses
```

to

```text
3633121 variables / 19448586 clauses.
```

The Type-II subcube inventory is unchanged at `646781 / 4309410`.  The
current whole Type-II build, which also contains a separately guarded
component/pin circuit added concurrently, is

```text
3640328 variables / 19476694 clauses.
```

## 5. Verification

The independent finite checker is

```text
python3 scratch/verify_k11_type1_core_subcube_encoding.py
```

It exhausts the equality-32 gate, evaluates `gamma` and `eta` from the exact
run-capacity formula, checks (3.1) for every `29<=p<=465`, exhausts every
possible contribution from the other 461 subcubes, and independently derives
the `25 / 189` inventory.

An explicit-zero and absent subcube guard still have identical all-off clause
streams:

```text
CLAUSE_STREAM_FNV64=ad22e261832b9ae2 ADD_CALLS=55261249.
```

The fully enabled Type-I clause-stream fingerprint is

```text
CLAUSE_STREAM_FNV64=325b7d6a6eb412fe ADD_CALLS=85224013.
```

Frozen combined-source artifacts at the final rebuild are

```text
1c3ce629c74aeef7339e2d43bd2f922aaf5b98d24f6a993d2d4f01aea7c63d06
  k11_forest_sat.cpp
d06bcd3f740b0c1d5878a13391c29302d5007f4b1b181f039f5c96c945c49c6d
  scratch/verify_k11_type1_core_subcube_encoding.py
```

## 6. Scope

This cut is exact and cheap, but it is only a necessary condition.  A SAT
model still requires exhaustive interval-OR verification.  An UNSAT claim
still requires archived proof traces and independent proof checking for both
Type-I and Type-II branches.
