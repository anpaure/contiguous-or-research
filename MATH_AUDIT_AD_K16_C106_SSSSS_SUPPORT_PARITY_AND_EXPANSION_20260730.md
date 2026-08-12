# K16 C=106 `SSSSS`: exact 662-column parity obstruction and expansion bank

Date: 2026-07-30  
Lane: AD  
Status: proved, source-relative, support-local no-go with a global parity escape cut

## 1. Frozen inputs and scope

The inputs are the frozen seam ledger

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657
```

the exact scale-two direct certificate

```text
scratch/k16_direct_cycle_dual_exact_20260730.audit.json
SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d
```

the 662-column PDLP support

```text
scratch/k16_floor106_s5_pdlp_20260730.tsv
SHA-256 e8cfd1c9f5ac8c68e49c8efeed9beae76334128b39a282a3cac126757deee494
```

and its exact rational reconstruction

```text
scratch/k16_floor106_s5_capacity_exact_20260730.audit.json
SHA-256 7f9780503ca106052044dc0b13604666509602e80f9bf7df6b091bbaa62c806e
```

The branch is `SSSSS`: selected mass 106, every one of the 93 targets is
serviced exactly once, and total direct-dual slack is five.  Endpoint balance
and port capacity one are retained.  Separation, q1, reverse-edge,
residence, survivor, and deeper rows are outside this note.

The no-go below concerns the frozen 662 columns only.  It does **not** prove
that the global `SSSSS` branch is infeasible.

## 2. Restitution and redundant equations

For a seam (e:u\to v), let (H(e)) be its serviced-target set, let
(b_t\in\{1,2,4\}) be the direct target price, let (y_v) be the frozen
port potential, and define

\[
 s_e=2+y_v-y_u-\sum_{t\in H(e)}b_t\ge0.
\]

For every nonnegative endpoint-balanced vector (x), telescoping gives

\[
 \sum_e s_ex_e+\sum_t b_tm_t=2\sum_e x_e,
 \qquad
 m_t:=\sum_{e:t\in H(e)}x_e.                       \tag{2.1}
\]

Since \(\sum_tb_t=207\), exact-once service reduces (2.1) to

\[
 \sum_e s_ex_e=2\sum_e x_e-207.                    \tag{2.2}
\]

Consequently, under balance and exact service, the count-106 row and the
slack-five row are equivalent; one should not include both as independent
rows.  Equivalently, if service is imposed only as (m_t\ge1), then balance,
count 106, and slack five force

\[
 \sum_tb_t(m_t-1)=0,
\]

and positivity of every (b_t) forces all 93 service equalities.  Thus the
service upper bounds are also redundant in that formulation.

Under endpoint balance, outgoing capacity at most one implies incoming
capacity at most one.  Individual bounds (x_e\le1) follow from outgoing
capacity and nonnegativity.  These are exact equivalences, not heuristic
presolve suggestions.

For the concrete 662-column Boolean model, there are 571 balance rows but
only

\[
571-3=568
\]

independent balance rows, one dependency for each support component.  The
outdegree histogram is

\[
1^{493},\quad2^{68},\quad3^8,\quad4^1,\quad5^1.
\]

Thus only 78 outgoing-capacity rows are nontrivial for Boolean variables;
the other 493 are variable upper bounds.  All incoming-capacity rows may be
deleted once balance and outgoing capacity are present.

## 3. Exact support geometry

Let (S) be the 662-column support.  Its directed graph has 571 active
vertices and three weak components with vertex/edge pairs

\[
 (2,2),\qquad(4,4),\qquad(565,656).
\]

The exact reconstructed circulation is strictly positive on every support
edge.  Hence every support edge belongs to a directed cycle, and every weak
component is strongly connected.  The circulation-space dimension is

\[
 |S|-|V|+c=662-571+3=94.                            \tag{3.1}
\]

The frozen reconstruction supplies 94 independent directed cycles.  The 93
service rows plus the slack row give a square (94\times94) integer matrix
of full rational rank.  Therefore the exact rational point is the **unique**
balanced real point on (S) satisfying the `SSSSS` rows.  Its common edge
denominator is

\[
 93159758129346024801758,
\]

and all 662 edge coordinates lie strictly between zero and one.  This already
proves that (S) contains no binary `SSSSS` point.  Section 4 gives a much
smaller parity certificate.

Equivalently, choose 568 independent balance rows and append the 93 service
rows and either the slack-five row or the count-106 row.  The resulting

\[
(568+93+1)\times662=662\times662
\]

system has full rational rank.  Hence the support-restricted CP-SAT search
has no genuine degrees of freedom: its equalities uniquely prescribe the
fractional point before capacity is considered.  The exact point has maximum
outgoing mass

\[
\frac{37778099230409452138842}{46579879064673012400879}<1,
\]

so no capacity row is active.  A timed Boolean solve on this fixed support is
therefore unnecessary.

There is also an immediate local simplification.  The isolated four-cycle

\[
 \{115844,138783,144563,173099\}
\]

services target 51252 twice and target 43540 once.  Binary balance selects
the entire simple cycle or none.  Exact-once service therefore forces all
four variables to zero.

## 4. A 33-target parity certificate

Define

\[
\begin{split}
T=\{&33337,36132,36343,37320,39791,40066,41170,41285,\
&42010,46224,46811,47003,47068,49436,49572,50939,\
&50976,51235,51252,54312,56173,56439,56941,57059,\
&58301,58385,59099,60983,61238,61297,61368,61918,63926\}.
                                                               \tag{4.1}
\end{split}
\]

There is a frozen bit (p_v\in\mathbb F_2) on each of the 571 support
vertices, with 283 ones, such that every (e:u\to v\) in (S) obeys

\[
 |H(e)\cap T|\equiv p_u+p_v\pmod2.                 \tag{4.2}
\]

The audit constructs (p) by propagation in each support component and
checks (4.2) on all 662 edges.  Hence every integral balanced circulation
supported on (S) has

\[
\begin{split}
 \sum_{t\in T}m_t
 &\equiv\sum_{e\in S}|H(e)\cap T|x_e\\
 &\equiv\sum_v p_v(\operatorname{out}_x(v)+
                         \operatorname{in}_x(v))\\
 &\equiv0\pmod2.                                      \tag{4.3}
\end{split}
\]

But `SSSSS` has (m_t=1) for every target and (|T|=33), so its left side
is one.  This contradiction proves:

> **Theorem 4.1 (support-local integral no-go).**  No integral endpoint-
> balanced `SSSSS` solution is supported on the frozen 662 columns.  The
> conclusion already holds without port capacity or any later physical row.

As a matrix cross-check, the (94\times94) service/slack cycle matrix has
rank 89 over \(\mathbb F_2\), while its right-hand-side augmentation has
rank 90.  The set (4.1), with zero slack coefficient, is an explicit
inconsistent left-null row.

## 5. Global parity escape bank

Extend (p_v) by zero on the other frozen-ledger vertices, and for every
catalogue seam define

\[
 \rho_e:=|H(e)\cap T|+p_{\operatorname{tail}(e)}+
                 p_{\operatorname{head}(e)}\pmod2.    \tag{5.1}
\]

For any global integral balanced `SSSSS` solution, the same cancellation as
in (4.3) gives

\[
 \sum_e\rho_ex_e\equiv1\pmod2.                       \tag{5.2}
\]

All 662 support seams have \(\rho_e=0\).  Across the full catalogue, 9,366
seams have \(\rho_e=1\), with slack histogram

\[
\begin{array}{c|rrrrrrrr}
s_e&0&1&2&3&4&5&6&7\\ \hline
\#&2382&1815&2743&1327&918&126&54&1.
\end{array}
\]

Since `SSSSS` has total nonnegative slack five, no selected seam may have
slack greater than five.  Thus the exact global cut is

\[
 \boxed{\sum_{e:\rho_e=1,\ s_e\le5}x_e\equiv1\pmod2},\qquad
 \sum_{e:\rho_e=1,\ s_e\le5}x_e\ge1,                \tag{5.3}
\]

on a bank of 9,311 seams.  This is stronger than the generic support-escape
cut because it specifies the admissible parity class.

If exactly one outside-support seam is used, contracting the three support
components shows that its endpoints must lie in the same support component;
one directed crossing edge cannot balance a component cut.  Exactly 298 of
the 9,311 seams pass this necessary one-column return test.  Their slack
histogram is

\[
\begin{array}{c|rrrrrr}
s_e&0&1&2&3&4&5\\ \hline
\#&49&60&115&42&29&3.
\end{array}                                           \tag{5.4}
\]

Therefore a complete exact support-expansion strategy is:

1. test the 298 one-column candidates first;
2. if all fail, every solution uses at least two outside columns;
3. in every case enforce the odd parity row (5.3).

No claim is made here that one of the 298 candidates succeeds.

## 6. Reproducible artifacts

The raw-binary checker is

```text
scratch/audit_ad_k16_c106_sssss_support_parity_escape_20260730.py
SHA-256 728b3dc859b7f1174dccad099bc621a729198bf78bd4b573d581fdb2a2628abf
```

Its audit output is

```text
scratch/ad_k16_c106_sssss_support_parity_escape_20260730.audit.json
SHA-256 d44c78780df5be82808d42f61ce1337f0f3cb18cde307f0222cf30a52c8705f5
payload 55eac841209a59fac4354eb8b19f8cd30e8c75c683792aeefc5fa0581a820a40
```

The annealer-facing parity bank is

```text
scratch/ad_k16_c106_sssss_parity_escape_bank_20260730.tsv
SHA-256 cb021f38ab5e423804bcb8bb885aa20026f34ef59eb93b0500dd716cfc573600
```

Each TSV row records the seam ID, exact direct slack, and whether it is one-
column return-capable relative to the three support components.
