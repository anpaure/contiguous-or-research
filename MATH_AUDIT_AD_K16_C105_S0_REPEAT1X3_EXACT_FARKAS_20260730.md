# AD audit: an exact no-capacity Farkas certificate for the K16 C=105 `s0_repeat1x3` face

Date: 2026-07-30  
Status: **proved for the frozen source-relative seam catalogue**  
Canonical floor-105 theorem: **not edited by this note**

## 1. Result

Let `E_0` be the slack-zero part of the authenticated 211,604-seam K16
catalogue, with slack measured by the frozen scale-two direct dual.  Let the
93 deficient colours be partitioned as

\[
D=D_1\sqcup D_2\sqcup D_4,
\qquad (|D_1|,|D_2|,|D_4|)=(15,60,18),
\]

where the subscript is the target price in the direct dual.  For a seam
\(e\), let \(H(e)\subseteq D\) be its Boolean target-incidence set.

### Theorem 1 (exact branch obstruction)

There is no nonnegative real vector \(x=(x_e)_{e\in E_0}\) satisfying

\[
\begin{aligned}
&\sum_{e\in\delta^+(v)}x_e-\sum_{e\in\delta^-(v)}x_e=0
&&\text{for every port }v,\\
&\sum_{e\in E_0}x_e=105,\\
&\sum_{t\in D_w}\sum_{e:t\in H(e)}x_e=(18,60,18)_w
&&\text{for }w=1,2,4,\\
&\sum_{e:t\in H(e)}x_e\ge 1
&&\text{for every }t\in D.
\end{aligned}
\tag{1.1}
\]

This is exactly the continuous balanced-service relaxation of the
`s0_repeat1x3` ledger: total dual slack zero, three excess occurrences in the
price-one class, and no excess occurrence in the other two price classes.

The theorem remains true after deleting all port-capacity rows.  Therefore it
is strictly stronger than the earlier capacity-enforced LP-infeasibility
status.

It does **not** exclude any other C=105 ledger branch, and it asserts nothing
about a different seam catalogue.

## 2. Exact finite instance and SCC reduction

The inputs are

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
  SHA256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657

scratch/k16_direct_cycle_dual_exact_20260730.audit.json
  SHA256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d
```

Independent raw parsing gives 41,491 slack-zero seams.  Their directed graph
has six nontrivial strongly connected components, of sizes

\[
5,5,5,30,356,863.
\]

Exactly 1,930 slack-zero seams have both ends in the same nontrivial SCC (or
are self-loops).  Only these seams need a Farkas column.

Indeed, every nonnegative finite circulation decomposes into directed cycles.
Consequently every seam with positive circulation belongs to a directed
cycle and hence has both endpoints in one SCC.  All other slack-zero seams
carry zero flow in every feasible circulation.  This proves that the
SCC deletion is an equivalence for (1.1), not a heuristic support restriction.

## 3. The integer-scaled certificate

The certificate stores rational multipliers on a common denominator
\(10^6\).  Equivalently, multiply every multiplier by \(10^6\) and use the
following integer convention.

* \(A_v\) is the free multiplier of the balance equality at port \(v\).
* \(K=118200\) is the free multiplier of the count equality.
* The three free group multipliers are

  \[
  (G_1,G_2,G_4)=(-1980879,2162517,1398229).
  \]

* \(Z_t\ge0\) multiplies the row
  \(-\sum_{e:t\in H(e)}x_e\le-1\).

Only 644 of the \(A_v\) and 75 of the \(Z_t\) are nonzero.  All capacity
multipliers are zero.  The complete exact arrays are frozen in the 41,646-byte
certificate file cited in Section 6.

For every one of the 1,930 cycle-eligible seams \(e:u\to v\), raw replay
checks the integer column inequality

\[
C_e:=A_u-A_v+K+
  \sum_{t\in H(e)}(G_{b_t}-Z_t)\ge0.
\tag{3.1}
\]

The minimum is zero and exactly 522 columns are tight.  On the right-hand
side the same multipliers give

\[
\begin{aligned}
R={}&105K+18G_1+60G_2+18G_4-\sum_{t\in D}Z_t\\
 ={}&-999963<0,
\end{aligned}
\tag{3.2}
\]

with

\[
\sum_t Z_t=132674283.
\]

Thus the unscaled rational certificate has right-hand side
\(-999963/1000000\).

## 4. Sign audit and proof

Assume that \(x\) satisfies (1.1).  Since \(x_e\ge0\) and every column in
(3.1) is nonnegative,

\[
0\le \sum_e C_e x_e.
\tag{4.1}
\]

Expand the right side.  The \(A_v\) terms vanish by endpoint balance.  The
count and the three group equations have free multipliers and contribute
their exact right-hand sides.  Finally, \(Z_t\ge0\) and target service is at
least one, so

\[
\begin{aligned}
\sum_e C_e x_e
&=105K+18G_1+60G_2+18G_4
  -\sum_t Z_t\sum_{e:t\in H(e)}x_e\\
&\le105K+18G_1+60G_2+18G_4-\sum_tZ_t\\
&=R<0.
\end{aligned}
\tag{4.2}
\]

Equations (4.1) and (4.2) contradict each other.  This proves Theorem 1.

The sign convention is therefore fully audited:

* balance, count, and group rows are equalities, so their multipliers are
  free;
* service is written as \(-L_t(x)\le-1\), so its multiplier \(Z_t\) is
  nonnegative;
* no upper bound on \(x_e\), and no port-capacity row, enters the proof.

## 5. How the rational ray was frozen

GLOP was used only as a numerical locator.  Each located multiplier was
rounded to the common grid \(10^{-6}\).  The derivation program then computed
every column with Python `Fraction`; its general fail-closed rule is to add
the exact worst negative column deficit to the free count multiplier and to
reject the candidate if that correction destroys the strict negative
right-hand side.  For this candidate the required correction was exactly
zero.

Acceptance does not trust GLOP status or floating-point tolerances.  A second
program, which does not import either the catalogue parser or the derivation
program, streams the binary twice, recomputes the target sets and direct
slacks, reconstructs the SCCs, and checks (3.1)--(3.2) with exact rational
arithmetic.  It passed in 1.20 seconds using 30,136 KiB maximum RSS on one
H100 CPU under a 256 MiB address-space cap.

## 6. Frozen artifacts

```text
scratch/derive_ad_k16_c105_s0_repeat1x3_farkas_20260730.py
  SHA256 c4f98cef2d027a6f0fc78bc364696ace837f1c244f18ffee53aee71c6b32f14d

scratch/ad_k16_c105_s0_repeat1x3_farkas_20260730.certificate.json
  SHA256 3a8f9d1fa506b56ff2ae5d3a4463a647bfbdf4773ea5df961a3483299da2d582
  payload 34ee9a957ca908a82ea21d1de02cad07cfbb5240181412a32f9edc9cc1a1ec20

scratch/ad_k16_c105_s0_repeat1x3_farkas_derive_replay_20260730.audit.json
  SHA256 f66aae4d9f8144828d0ac95f95028f87a0eb6a47c92615703d430392f53f27b4

scratch/ad_k16_c105_s0_repeat1x3_farkas_derive_20260730.resource.txt
  SHA256 a733879f2da6bb3601846cf36b82c4f6b716cf95a0f1ea5ca0094c67d32b6bbd

scratch/ad_k16_c105_s0_repeat1x3_farkas_derive_20260730.stdout.txt
  SHA256 e7859e1b009fbb3b7cf1f05b3962687a76b47cc7e6e5e5320727a418c42560

scratch/audit_ad_k16_c105_s0_repeat1x3_farkas_rawstream_20260730.py
  SHA256 c92686c142003b86316b72ff930f073f2d74ae74fb3295929615c75cefc87444

scratch/ad_k16_c105_s0_repeat1x3_farkas_rawstream_20260730.audit.json
  SHA256 3117bd8d0084337a1e854edd2f1536bea0a81991c5ebc6d1c0df116a012ab1b3
  payload 596119173ee74b8721a8a9a2a4d4f47e3fa00973b60b035c9b68831281ecbb60

scratch/ad_k16_c105_s0_repeat1x3_farkas_rawstream_20260730.resource.txt
  SHA256 f907311a505f2bdddb07fef265247358cb57f707641af9cb75cf84fde7f1cd48

scratch/ad_k16_c105_s0_repeat1x3_farkas_rawstream_20260730.stdout.txt
  SHA256 8c413f7e36fb0e59425893a3a0e3d4977159f60e9701c38bb9c19e6cca710588
```

The independent audit status is

```text
PASS_EXACT_RAWSTREAM_FARKAS_NO_CAPACITY
```

## 7. Exact boundary

What is proved:

1. the continuous `s0_repeat1x3` face is empty;
2. the obstruction uses balance, count, class-occurrence totals, and target
   service only;
3. it remains valid without port capacity and hence excludes every integer or
   physical specialization of this branch inside the frozen catalogue.

What is not proved:

1. no other C=105 ledger branch is excluded here;
2. no C=106 lower bound follows;
3. the certificate does not apply to seams outside the authenticated
   direction-coherent q<=3/upper-width-four catalogue;
4. this note makes no claim about literal carrier construction or compiler
   feasibility.
