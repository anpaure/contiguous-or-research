# Second independent audit of the K16 endpoint-transport upper pins

**Date:** 2026-07-31  
**Status:** exact, solver-free, fixed-order P/Q theorem

## 1. Authenticated input and conclusion

The input is

```text
scratch/k16_fourfilter_def4_endpoint_transport_fixed_5_targets_20260731.word
SHA-256 9142910f9009deb4a012d2ad3828ea39753c9f8438592f18cd036e65891f939b
```

It is a permutation of all \({16\choose8}=12870\) rank-eight masks.  A
fresh arbitrary-width interval-OR replay finds exactly two upper holes:

\[
U_{10}=\mathtt{0x3ceb},\qquad U_{11}=\mathtt{0xa9fe}.
\]

An independent event-DAG implementation, importing no project DP module,
proves that either required upper pin separately drives the optimistic lower
capacity below

\[
\sum_{r=1}^{7}{16\choose r}=26332.
\]

Thus this fixed middle order cannot support a waste-three monotone P/Q
compiler.  This is not a no-go for another order or a non-P/Q architecture.

## 2. The provider-length lemma

Let the middle owner intervals be \(I_i=[p_i,q_i]\), with
\(q_i-p_i\le d\), and suppose the P row omits at most \(h\) physical start
positions.  For an upper target \(U\), put

\[
\rho_U=\max\{s:T_a,T_{a+1},\ldots,T_{a+s-1}\subseteq U\}.
\]

### Lemma 2.1

If a contiguous physical interval \(J=[a,b]\) consists of nonempty cells
contained in \(U\) and has OR \(U\), then

\[
|J|\le d+h+\rho_U.                                      \tag{2.1}
\]

### Proof

Write \(\ell=|J|\).  Every retained start in the physical interval
\([a,b-d]\) starts a row no earlier than \(a\) and, because its lifetime is
at most \(d\), ends no later than \(b\).  Its whole owner interval is
therefore contained in \(J\).  All its cells are subsets of \(U\), so exact
middle replay forces its target \(T_i\) to be a subset of \(U\).

The interval \([a,b-d]\) has \(\ell-d\) physical positions and loses at
most \(h\) omitted starts.  Its retained starts index consecutive owner
rows.  Hence it supplies at least \(\ell-d-h\) consecutive targets contained
in \(U\), which is at most \(\rho_U\).  Rearranging gives (2.1).  (When the
lower bound is nonpositive, (2.1) is immediate.)  \(\square\)

Here \(d=h=3\).  The independently reconstructed compatible-owner runs are

| target | compatible owners | run histogram | \(\rho_U\) | exhaustive pin bound |
|---|---:|---|---:|---:|
| `0x3ceb` | 45 | \(25\cdot1+10\cdot2\) | 2 | 8 |
| `0xa9fe` | 165 | \(66\cdot1+31\cdot2+11\cdot3+1\cdot4\) | 4 | 10 |

The audit payload records every run and hashes the two run catalogues.

## 3. Independent exact event DAG

At each of the \(12873\) physical positions the independent implementation
chooses whether the next P start and next Q deadline occur.  Its state is

\[
(s,e,(R_e,\ldots,R_{s-1}),\phi,V,\lambda),              \tag{3.1}
\]

where \(s,e\) are the numbers of started and ended rows, the \(R_i\) are
their exact accumulated cell ORs, and \((\phi,V,\lambda)\) is the
before/active/finished upper-pin automaton.  The maximal uncapped cell is the
intersection of all active targets; inside the distinguished pin it is
intersected with \(U\).

This maximal-cell reduction is exact.  Any legal cell may be enlarged to
the active-target intersection (and, inside the pin, to its intersection
with \(U\)); this stays within every active target and can only help every
required OR.  Once the pin OR first reaches \(U\), ending the pin is also
without loss because uncapping a redundant suffix only enlarges cells.

Equal states in (3.1) have identical continuations.  Retaining only their
largest accumulated

\[
A=\sum_i(q_i-p_i)
\]

is therefore exact.  Lemma 2.1 makes the length-eight and length-ten pin
automata exhaustive over *all* pin locations and all monotone three-hole P/Q
schedules.

The exact results are:

| upper pin | max states/layer | \(A_{\max}\) | optimistic \(A+9\) | deficit | maximizing \(X\) | maximizing \(Y\) | pin |
|---|---:|---:|---:|---:|---|---|---|
| `0x3ceb` | 82 | 25740 | 25749 | 583 | `12870,12871,12872` | `0,1,12872` | `[12872,12872]` |
| `0xa9fe` | 128 | 25743 | 25752 | 580 | `6102,12871,12872` | `0,1,6101` | `[6096,6101]` |

Direct reconstruction of each maximizing capped word gives:

- every physical cell nonempty;
- zero failed middle rows;
- exact distinguished pin OR;
- selected area equal to the dynamic-programming objective.

The actual omitted-start credit of each displayed witness is only six.  The
conclusion deliberately grants the larger universal credit nine, so it does
not depend on boundary truncation.

## 4. Frozen independent artifacts

```text
scratch/audit_k16_endpoint_transport_upperpin_independent_20260731.py
SHA-256 4940f768ea95a86d8e7d071ad3dc7700c832c267f1cc97b4e861f7bcd1dff7d1

scratch/k16_endpoint_transport_upperpin_independent_20260731.audit.json
SHA-256 34cc7ed60b6aed00a68f0e91aee444f02bd527ad340f239cadfa99cfc091c613
payload SHA-256 074551e6243c55595362eb55c6d39ff2faad95e828563cf050fe9111b67bccb8
```

The implementation uses only the Python standard library, takes about four
seconds on the local audit machine, and peaks below 35 MB.  It performs no
SAT, stochastic search, or imported recurrence call.
