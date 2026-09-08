# Independent raw replay of the K16 scale-two balanced-cycle dual

Date: 2026-07-30  
Lane: AD  
Status: **PASS for the frozen binary catalogue; exact floor 104**

## 1. Audited statement

Let \(D=D_L\sqcup D_U\) be the target bank encoded in the frozen seam
catalogue

```text
scratch/k16_len8_source_seam_ledger_20260730.bin
SHA-256 832ddd883452e73c0f2462f8550e900d8ffcf01f7397f17b980dd552853b6657.
```

Thus \(D_L\) consists of the 45 rank-six lower-q2 zero-load masks and
\(D_U\) consists of the 48 rank-eleven upper-q3 zero-load masks.  The binary
contains 12,870 ports and 211,604 directed seams.  For a seam
\(e=(u,v)\), let \(H(e)\subseteq D\) be the **set**, rather than the
multiset, of target masks in its active lower-q2 and upper-q3 slots.

The independently replayed certificate supplies positive integral target
weights \(b_t\) and integral port potentials \(\phi_v\) such that

\[
 b_t\in\{1,2,4\},\qquad \sum_{t\in D}b_t=207,
 \qquad -4\leq\phi_v\leq2,                         \tag{1.1}
\]

and, for every one of the 211,604 seams,

\[
 b(H(e)):=\sum_{t\in H(e)}b_t
 \leq 2+\phi_v-\phi_u.                             \tag{1.2}
\]

The exact replay found no negative slack.

### Theorem 1.1 (direct balanced-service floor 104)

For every nonnegative integral seam vector
\(x\in\mathbb Z_{\geq0}^{211604}\) satisfying

\[
 \sum_{e\in\delta^+(v)}x_e=\sum_{e\in\delta^-(v)}x_e
 \quad\text{for every port }v,                     \tag{1.3}
\]

and

\[
 m_t:=\sum_{e:t\in H(e)}x_e\geq1
 \quad\text{for every }t\in D,                    \tag{1.4}
\]

the total seam count \(C:=\sum_e x_e\) obeys

\[
                         C\geq104.                  \tag{1.5}
\]

In particular, (1.5) holds for every selected balanced port permutation in
this catalogue.

### Proof

Define the integral seam slack

\[
 s_e:=2+\phi_v-\phi_u-b(H(e))\geq0.                 \tag{1.6}
\]

Multiply (1.6) by \(x_e\), sum over seams, and use (1.3).  Every coefficient
\(\phi_v\) cancels exactly, including when the balanced circulation has
several components or has multiplicity greater than one.  Therefore

\[
 2C
 =\sum_{t\in D}b_t m_t+\sum_e s_ex_e
 \geq\sum_{t\in D}b_t
 =207.                                               \tag{1.7}
\]

Since \(C\) is integral, \(C\geq\lceil207/2\rceil=104\).  \(\square\)

This proof uses neither a numerical LP assertion nor a cycle-decomposition
algorithm.  Endpoint balance alone is the exact hypothesis needed to cancel
the potential.

## 2. Exact target prices

The 93 prices have histogram

```text
price 1: 15 targets
price 2: 60 targets
price 4: 18 targets
```

Equivalently, on the seven frozen phase blocks they are

| block representative | block size | price |
|---:|---:|---:|
| 33337 | 15 | 1 |
| 33609 | 15 | 2 |
| 34069 | 15 | 4 |
| 36343 | 15 | 2 |
| 36599 | 15 | 2 |
| 39791 | 15 | 2 |
| 46811 | 3 | 4 |

Consequently

\[
 15(1)+15(2)+15(4)+15(2)+15(2)+15(2)+3(4)=207.
\]

The complete mask-to-price map and the complete 12,870-entry potential are
frozen in

```text
scratch/k16_direct_cycle_dual_exact_20260730.audit.json
SHA-256 29b4aae4bc889e07261725b275455a58583d949932a0eeabf65eae33eb7c460d
payload SHA-256 8b934733599fa90f8512b4302b10013b1a711ca75651b9d67832e4f7196ed59c.
```

The replay independently recomputed and checked that payload hash before
reading the vector.  The potential histogram is

| \(\phi\) | -4 | -3 | -2 | -1 | 0 | 1 | 2 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| ports | 2 | 39 | 3970 | 2420 | 5971 | 426 | 42 |

These counts sum to 12,870.

## 3. Independent binary and incidence audit

The new checker

```text
scratch/audit_ad_k16_direct_scale2_floor104_rawstream_20260730.py
SHA-256 a6b434c787be1c0a842c95cc3dd8c2cff0918c910ba5719f7f3e36abe52c9830
```

imports no project parser, catalogue writer, optimizer, OR-Tools module, or
previous verifier.  It reads the binary record stream directly using only
the Python standard library.  Its checks are as follows.

1. It pins the binary SHA above and separately pins the source factor

   ```text
   scratch/k16_asymmetric_len8_orbit_repair_20260730.json
   SHA-256 6bea170e55a52a6f345382efac6bf898dcb11f18ce0f4c3dd392b9a59cd8d204.
   ```

   The same factor SHA is present in the binary header.

2. It parses the six signed-load tables.  It verifies that the lower-hole
   bitmap is exactly

   \[
   \{S\subseteq[16]: |S|=6,\ L_{q2}(S)=0\}
   \]

   and has size 45, and that the upper-hole bitmap is exactly

   \[
   \{S\subseteq[16]: |S|=11,\ U_{q3}(S)=0\}
   \]

   and has size 48.  Both bitmaps are Boolean.

3. It parses every 39-byte seam record independently.  All 211,604 endpoint
   pairs are distinct and lie in the port bank; all seams carry the
   positive-residence-safe flag; every q1/q2/q3 active mask has the declared
   Hamming grade; every inactive mask slot is zero; and the source-distance
   flag agrees with the sentinel convention.

4. It reconstructs \(H(e)\) from the lower-q2 and upper-q3 active slots and
   checks that the binary provider flag is set if and only if \(H(e)\neq
   \varnothing\).  The resulting exact census is

   ```text
   no target hit:       206179 seams
   one target hit:        5232 seams
   two target hits:        193 seams
   all providers:         5425 seams.
   ```

5. It checks (1.2) with exact Python integers on every seam.

### Boolean-incidence correction made explicit

Repeated active shadow masks are legal in this binary: 51,722 seams have at
least one repeated mask within a local shadow family, accounting for 56,776
repeated active slots.  Two local windows can expose the same colour.  The
service row is nevertheless Boolean per seam, so \(H(e)\) is a set and that
colour contributes once to \(b(H(e))\).  The candidate checker and this
independent replay both use this correct set semantics.  Counting repeated
slots with multiplicity would describe a different, invalid dual row.

## 4. Exact slack replay

The complete exact slack histogram is

| slack \(s_e\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| seams | 41491 | 33388 | 74860 | 29927 | 30191 | 1568 | 178 | 1 |

Thus the minimum is zero, the maximum is seven, and 41,491 seam inequalities
are tight.  The hit-weight histogram is

```text
b(H)=0: 206179
b(H)=1:    902
b(H)=2:   3825
b(H)=3:     30
b(H)=4:    668.
```

This independently reproduces the claimed scale-two dual and its floor
\(207/2=103.5\), hence the integral floor 104.

## 5. Exact equality face at count 104

The certificate gives a complete algebraic classification of any possible
count-104 integral solution, before imposing port capacity or any physical
side rows.  Put

\[
 R:=\sum_{t\in D}b_t(m_t-1),\qquad
 S:=\sum_e s_ex_e.                                   \tag{5.1}
\]

At \(C=104\), identity (1.7) becomes

\[
                    R+S=208-207=1.                   \tag{5.2}
\]

Both \(R\) and \(S\) are nonnegative integers.  There are therefore exactly
two cases.

* **No-repeat / one-slack case:** \(R=0,S=1\).  Every one of the 93 targets
  is serviced exactly once.  All selected seam copies are tight except for
  exactly one selected copy of a slack-one seam.

* **One price-one repeat / tight case:** \(R=1,S=0\).  Exactly one of the 15
  price-one targets is serviced twice, every other target exactly once, and
  every selected seam is tight.

This is an exhaustive equality classification, not a feasibility result.
Ruling out both cases would prove floor 105; finding either case would prove
that 104 is tight in the corresponding reduced service-plus-balance
relaxation.  Port capacity, separation and the other physical rows must be
stated explicitly in any subsequent case test.

## 6. Scope and claims deliberately not made

The proved scope is the frozen, source-relative, direction-coherent
q\(\leq3\)/upper-width-four seam binary above.  The word “unrestricted” in
“unrestricted direct dual” means that all 211,604 seams of this frozen
catalogue participate; it does **not** mean all possible K16 rethreads.

The proof uses only:

* nonnegative integral seam variables;
* endpoint balance at each of the 12,870 ports; and
* service of the 45 lower-q2 and 48 upper-q3 targets.

It does not use port capacity, cut separation, reverse-edge exclusion, q1
palette preservation, survivor rows, additional residence rows, or deeper
shadow rows.  Hence those rows can only strengthen the lower bound.

Conversely, this audit does not regenerate the seam catalogue from the
factor and does not prove that the catalogue contains every conceivable K16
operation.  It also does not certify the floating solver's assertion that
103.5 is the optimum of its LP.  It certifies the displayed exact dual
feasibility, which alone is sufficient for Theorem 1.1.

## 7. Frozen independent replay artifacts

```text
independent audit artifact
  scratch/ad_k16_direct_scale2_floor104_rawstream_v3_20260730.audit.json
  SHA-256 1f5a78e4e6a97e3f2a52fb81d60962cdc0ee4effd5e92e7db3e2d37c81a37313
  payload SHA-256 0125bc3f637a27177ed3438bc7113e7476b5778b194b4a11ffa44b2aabdc682b

H100 resource record
  scratch/ad_k16_direct_scale2_floor104_rawstream_v3_20260730.resource.txt
  SHA-256 23b6172c223868cdedf53b6c3126901d10a334c4644534f34b7737a3a089df56

captured stdout
  scratch/ad_k16_direct_scale2_floor104_rawstream_v3_20260730.stdout.txt
  SHA-256 e4cecd52b7e256b11824b5fdae5516e7aa6257457a61e82df6b895f863c339e3
```

The replay used one H100 CPU, 36,692 KiB maximum RSS, 1.67 seconds elapsed
time, and exited with status zero.  The process was capped below 256 MiB.

