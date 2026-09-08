# K16 append-0200 basin: exact one-debt portal and return obstruction

**Date:** 2026-07-30  
**Lane:** D  
**Status:** exact scoped two-substitution obstruction; no length-12,874 word is claimed

## 1. Frozen basin

Let `A` be the authenticated length-12,873 partial word

```text
scratch/k16_12873_repaired_partial.word
SHA-256 0a70a67eced48a82883a698c6fd25688a27c52faf19e3fa11bbbd9a78581bea6
```

and put

\[
W=A\,\|\,\mathtt{0x0200}.
\]

The literal file is

```text
scratch/k16_append0200_12874_onehole.word
SHA-256 aa17f3ca70525115c941e906fecf1384bad8302cd95b236413c7f2f3f8777c18
```

and equality with `A` followed by the one displayed cell was checked byte for
byte.  Appending preserves every old interval.  The two high holes of `A`
receive the exact terminal witnesses

```text
0xce61 : [12871,12873]
0xce63 : [12870,12873]
```

whereas exact ending-OR replay gives

\[
H(W)=\{10365\}=\{\mathtt{0x287d}\}.
\tag{1.1}
\]

## 2. Exact substitution formula

For a position `p`, retain multiplicities in the left-suffix and right-prefix
OR banks

\[
\mathcal L_p=\{0\}\uplus
 \left\{\bigvee_{i=a}^{p-1}W_i:a<p\right\},
\qquad
\mathcal R_p=\{0\}\uplus
 \left\{\bigvee_{i=p+1}^{b}W_i:p<b\right\}.
\]

For the substitution \(W_p\mapsto r\), every changed interval contains `p`,
and its exact signed multiplicity column is

\[
\Delta_{p,r}(T)=
\sum_{L\in\mathcal L_p,\,R\in\mathcal R_p}
\left([L\vee r\vee R=T]-[L\vee W_p\vee R=T]\right).
\tag{2.1}
\]

Writing \(C=L\vee R\), a value `r` can install a target `T` exactly when

\[
C\subseteq T,
\qquad T\setminus C\subseteq r\subseteq T
\tag{2.2}
\]

for some context `C`.  Thus (2.2) enumerates every relevant arbitrary
nonzero replacement, and

\[
c_W(T)+\Delta_{p,r}(T)>0\quad(0<T<2^{16})
\tag{2.3}
\]

is the exact completion test.  No unique-provider or one-bit approximation
is used below.

## 3. The complete first-substitution census

There are exactly 26,701 substitutions satisfying (2.2) for the sole hole
`0x287d`.  None has zero collateral debt.  The sharp minimum is one, attained
by exactly the following 16 replacements, all at zero-based position 6440:

```text
old 0xa069

0x2005 0x2004 0x200d 0x200c
0x2025 0x2024 0x202d 0x202c
0x2045 0x2044 0x204d 0x204c
0x2065 0x2064 0x206d 0x206c
```

Every one of the 16 edited words has exactly the singleton debt

\[
\{43129\}=\{\mathtt{0xa879}\}.
\tag{3.1}
\]

This exchange is literal.  In `W`, `0xa879` has exactly one witness,
`[6439,6440]`, because

\[
\mathtt{0x2879}\vee\mathtt{0xa069}=\mathtt{0xa879}.
\]

Every listed low-phase replacement changes that same interval to
`0x287d`, installing the old hole and destroying only the unique `0xa879`
witness.

> **Theorem 3.1 (sharp one-debt portal).** No single arbitrary substitution
> completes `W`.  The minimum possible collateral debt of an installing
> substitution is exactly one, and the complete minimum family is the 16-row
> list above.

## 4. Complete return census from all 16 portals

For each of the 16 post-portal words, the same exact calculation was rerun
with target `0xa879`.

* Exactly 27,840 arbitrary substitutions can install the debt in each
  branch.
* No branch has a safe return substitution.
* In every branch the minimum return collateral is one.
* The 16 minimum returns all edit position 6440 again, to

```text
0xa001 0xa000 0xa009 0xa008
0xa021 0xa020 0xa029 0xa028
0xa041 0xa040 0xa049 0xa048
0xa061 0xa060 0xa069 0xa068
```

  and every one loses exactly `0x287d`.

Thus the minimum return is a phase toggle, not a balanced exchange: restoring
the top-containing label `0xa879` at the same two-cell interval removes the
low label `0x287d`.  Since the displayed list is the complete minimum-return
list, every off-position return creates at least two collateral holes.

In total, all \(16\cdot27840=445440\) sharp-portal/return rows were checked;
the universal list is empty.

> **Theorem 4.1 (no two-substitution closure through a sharp portal).** No
> length-preserving sequence consisting of one of the 16 minimum-debt
> installers followed by one arbitrary substitution completes `W`.

This theorem is deliberately scoped.  It does not exclude:

1. a first installer with two or more debts which a correlated second edit
   closes simultaneously; or
2. two edits whose common interval creates `0x287d` although neither edit
   installs it by itself.

Those are the exact remaining radius-two branches.  A proof-safe model must
include the mixed two-position interval term rather than add two static
columns.

## 5. Executable audit and resource record

The complete audit is

```text
scratch/audit_threadA_k16_append0200_one_debt_return_20260730.py
SHA-256 ca77a8ed469fa9e70311d6549f34ad31f15bc9ca13489906e4824474e6112e30
```

It independently checks both input hashes, reconstructs every service value
by (2.2), proves collateral exactness by global-versus-local multiplicities,
and would full-replay any safe return before reporting it.  Its frozen H100
outputs are

```text
scratch/threadD_append0200_return.stdout.txt
SHA-256 3139109752cde8ec41124607521506f0e7e65faca9e97d4140267c0286e9ce55

scratch/threadD_append0200_return.resource.txt
SHA-256 dbbc869505fadd86f73cfe02906c91bb39cefb7a9bf2b6eca489323a97fdfed6
```

The bounded run used one H100 CPU, 17.14 seconds wall time, 47,768 KiB peak
RSS, no swap, and exited zero with

```text
PASS_APPEND0200_ONE_DEBT_RETURN_CENSUS
universal_two_substitution_words []
```

No SAT/CP solver was used.  This obstruction does not change the verified
global bracket

\[
12873\le\nu(16)\le12875.
\]
