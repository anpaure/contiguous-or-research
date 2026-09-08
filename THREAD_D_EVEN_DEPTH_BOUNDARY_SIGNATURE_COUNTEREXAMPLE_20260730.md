# Even-depth boundary events: exact K16 census and finite counterexamples

**Date:** 2026-07-30  
**Lane:** D, exact finite contiguous-OR audit  
**Status:** proved counterexample to the proposed event lower bound; exact
solver-free census

## 1. Verdict

There are two different statistics which must not be conflated.

1. The project's established **compiler short-cell waste** is the number of
   cells in rows `0,...,d-1` which are not first witnesses for lower masks.
   For an optimal length `W+d` compiler it is exactly the arithmetic slack

   \[
      \sigma=dW+\binom{d+1}{2}-\Lambda.
   \]

2. The proposed four K16 objects are **elementary middle-boundary events**:
   immediate deletion of the left or right endpoint of an interval leaves
   its middle-rank OR unchanged.  This is a useful new statistic, but it is
   not called waste anywhere in the existing compiler theorems.

For the verified length-12,874 K16 word, compiler waste is `12,287`, not
four.  The new elementary-event count is exactly four.  However:

* neither of the two natural `(d-1)`-bit signatures defined below takes the
  values `00,01,10,11` exactly; and
* the retained flat optimal K14 word has `d=2` and only one elementary
  boundary event, disproving

  \[
     \#\{\text{elementary boundary events}\}\ge 2^{d-1}.
  \]

Thus K16 equality `4=2^(3-1)` is a certificate-specific observation, not an
even-dimension law.

## 2. The two exact definitions

Let `A=(A_0,...,A_(n-1))`, let

\[
   U[a,b]=\bigvee_{i=a}^b A_i,
   \qquad r=\lceil k/2\rceil,
\]

and let `d` be the monotone-deadline depth.

### 2.1 Established compiler waste

The short-cell grid consists of all intervals of lengths `1,...,d`, hence
has

\[
   M_d(n)=\sum_{j=0}^{d-1}(n-j)=dn-\binom d2
\]

cells.  If every one of the `Lambda` lower masks has a short first witness,
the exact cell waste is

\[
   \mathsf W_{\rm comp}(A)=M_d(n)-\Lambda.              \tag{2.1}
\]

This is the definition in
`MATH_CAPACITY_ORDERED_OR_PASCAL_QUANTILES_20260727.md`, Section 3.  In a
flat compiler having no short upper cell, it is equivalently the
duplicate-lower plus early-middle ledger of
`MATH_THEOREM_R_ALLK_NEGATIVE_WINDOW_CONFLICT_MASS_COMPILER_20260730.md`,
Section 2.  The general depth/repeat decomposition is in
`MONOTONE_DEADLINE_LOWER_BOUND_AND_EQUALITY_AUDIT_20260727.md`, Section 3.

### 2.2 New elementary boundary event

An elementary middle-boundary event is a tuple `(T,[a,b],side)` with
`|T|=r`, `a<b`, and either

\[
  T=U[a,b]=U[a+1,b] \quad(\text{side L}),               \tag{2.2}
\]

or

\[
  T=U[a,b]=U[a,b-1] \quad(\text{side R}).               \tag{2.3}
\]

The deleted endpoint is the *redundant cell*.  This definition counts
oriented cover relations in the interval-containment poset.  It does not
count two equal-OR intervals at unrelated positions.

The census is complete: while extending a fixed interval to the right, OR
rank is nondecreasing, so scanning may stop after it exceeds `r`.  Store all
rank-`r` intervals and test their two immediate subintervals.  Conversely,
every event (2.2) or (2.3) appears in exactly that test.

For a redundant endpoint `x`, order the cells of the shorter interval
inward from that endpoint as `y_1,y_2,...`.  Two natural signatures are:

\[
 c_h=1\!\left[x\subseteq y_1\vee\cdots\vee y_h\right],
 \qquad 1\le h<d,                                      \tag{2.4}
\]

and

\[
 g_h=1\!\left[(x\setminus(y_1\vee\cdots\vee y_{h-1}))
                    \cap y_h\ne\varnothing\right].    \tag{2.5}
\]

Absent inward cells are read as zero.  Formula (2.4) records cumulative
coverage of the redundant endpoint; (2.5) records whether the next inward
cell contributes a previously uncovered endpoint bit.  Both are literal,
coordinate-relabeling invariant, and have exactly `d-1` bits.

## 3. Exact K16 audit

The word is

```text
answers/k16_upper12874.word
SHA-256 631e78e5e466423a6c53dbdd31c2157c006bb286f8c8534e2cddf50e751df75e
```

It has `r=8`, `W=12870`, `d=3`, `Lambda=26332`, and length `n=12874`.
All `Lambda` lower masks occur in the first three rows.  The exact ledger is

```text
short cells                              38,619
distinct lower masks                     26,332
lower occurrences                        32,176
duplicate-lower excess                    5,844
nonlower short cells                      6,443
  rank 8                                  6,442
  rank 9                                      1
compiler cell waste                      12,287
```

Thus `5844+6443=12287`, exactly as (2.1) requires.  The optimal-length
arithmetic slack would be `sigma=12284`; the one extra physical letter adds
three short cells.

There are `12,875` middle-rank interval occurrences covering all `12,870`
middle masks.  Exactly five masks occur twice, and none occurs more often.
Four duplicated pairs are nested and give the following complete elementary
event list.  Indices are zero based and inclusive.

| target | longer = shorter | redundant cell | side | `c` | `g` | endpoint-touch | `(side R, bit15(T))` | `(bit15(T), short-length parity)` |
|---|---|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `0x6879` | `[0,2]=[0,1]` | `p2=0x2069` | R | `01` | `11` | `10` | `10` | `00` |
| `0x4e71` | `[6433,6436]=[6434,6436]` | `p6433=0x0c61` | L | `00` | `10` | `00` | `00` | `01` |
| `0xcc63` | `[12870,12872]=[12871,12872]` | `p12870=0x8c62` | L | `01` | `11` | `00` | `01` | `10` |
| `0xce61` | `[12872,12873]=[12873,12873]` | `p12872=0xcc61` | L | `11` | `10` | `01` | `01` | `11` |

For example,

```text
0x4879 OR 0x2800                     = 0x6879,
0x4879 OR 0x2800 OR 0x2069           = 0x6879,
```

and the other three displayed equalities are checked literally in the same
way.

The fifth repeated middle mask is

```text
0xc279: [11727,11729] and [12827,12829].
```

These intervals are disjoint, so this duplicate is not an elementary
boundary event.  This is also why middle duplicate excess is five while the
new event count is four.

## 4. No canonical saturated signature follows

The most direct signature (2.4) yields

```text
01, 00, 01, 11,
```

which repeats `01` and misses `10`.  The incremental signature (2.5) yields

```text
11, 10, 11, 10.
```

Other immediate invariant choices also fail:

* global left/right endpoint contact gives `10,00,00,01`;
* redundant-side together with membership of coordinate 15 in the target
  gives `10,00,01,01`.

The last table column happens to give `00,01,10,11`.  It is not canonical:
it singles out coordinate 15 from this particular odd-to-even construction,
uses parity of physical interval length, changes under coordinate relabeling,
and has no specified `(d-1)`-bit extension for general `d`.  Sorting the four
events and assigning binary names would be equally vacuous.  A genuine
signature theorem therefore needs extra recursive/flag structure not present
in the literal event definition.

The smaller words make the failure sharper.  At `d=2`, cumulative
containment signatures are `1,1` for K10, `0,0` for K12, and only `0` for
K14.  Orientation gives both bits for K10 and K12 but only one for K14.

## 5. All retained even optima through K14

The following table is recomputed directly from the canonical answer files.
K16 is appended for comparison but is an upper certificate, not a proved
optimum.

| `k` | `d` | length | established compiler waste | middle duplicate excess | elementary events | `2^(d-1)` |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 2 | 0 | 0 | 0 | n/a |
| 4 | 1 | 7 | 3 | 1 | 1 | 1 |
| 6 | 1 | 21 | 0 | 0 | 0 | 1 |
| 8 | 2 | 72 | 51 | 0 | 0 | 2 |
| 10 | 2 | 254 | 122 | 2 | 2 | 2 |
| 12 | 2 | 926 | 266 | 2 | 2 | 2 |
| 14 | 2 | 3434 | 392 | 1 | 1 | 2 |
| 16 | 3 | 12874 | 12287 | 5 | 4 | 4 |

The K14 counterexample is especially clean.  Its exact raw audit records:

```text
length = B(14) = 3434,
exact middle layer = true,
flat interior = true,
exact boundary ramp = true.
```

Its sole event is

```text
0x351a: [3431,3433] = [3432,3433],
redundant p3431 = 0x3410.
```

Hence excluding small nonflat words does not rescue the proposed bound.

## 6. Frozen audit and provenance

The solver-free checker is

```text
scratch/audit_threadD_even_depth_boundary_signature_counterexample_20260730.py
SHA-256 4781e20378a84a52de9bb4956989a366a60fdb92726b2517a1350e70ea4e75ae
```

and emits

```text
scratch/threadD_even_depth_boundary_signature_counterexample_20260730.audit.json
SHA-256 85a34db167bf4945f335c7d267321d281e5c75b28722fd740530976d1f4f9b1d
payload 606d6d1610960b32cefcdb3e7f7fe46ecedcbf0db86ffc756c31dff4e3b2f32e
```

It authenticates every input word, enumerates every middle-rank interval,
checks every immediate containment edge, and independently reconstructs the
short-cell waste ledger.  The retained optimum baseline is

```text
scratch/raw_optimal_k01_k14_compiler_normal_form_audit.json
SHA-256 33457ecdd9c96bc78eac7f2e2f35dc408315d986ea90ed3bd94d3d8b7527c913
```

produced by

```text
scratch/analyze_raw_optimal_compiler_normal_form.py
SHA-256 34736cf1521935c40508b2a0dc5aec1bf9d4ed2dfde8ee6fba1c5448e69eff8b
```

The canonical K2--K14 word hashes are frozen in `answers/README.md`.  The
K16 length-12,874 hash is not yet listed there, so the checker pins that
certificate independently.  It also hard-pins the baseline audit and
analyzer hashes and asserts the K14 optimal-length, exact-middle, flat-
interior, and exact-boundary-ramp fields.  No SAT solver, remote compute,
or web access was used.
