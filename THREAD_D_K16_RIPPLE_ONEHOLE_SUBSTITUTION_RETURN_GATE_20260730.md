# K16 ripple one-hole basin: exact substitution portal and return gate

**Date:** 2026-07-30  
**Lane:** D  
**Status:** exact scoped obstruction; no length-12,874 universal word is claimed

## 1. Frozen one-hole word and literal provenance

Let

```text
R = scratch/k16_ripple_insert12874_onehole.word
SHA-256 5ac147eca512b7e398c7217f1796836f454a304274c6e54fda7050fc9b4f66db
```

The word has length 12,874.  Exact ending-OR replay gives

\[
H(R)=\{10365\}=\{\mathtt{0x287d}\}.
\tag{1.1}
\]

Its ancestry is literal and reproducible.  Start with

```text
scratch/k16_12873_ripple3_partial.word
SHA-256 87f19da2994c6052caa3f9a5d87936ee340588111b29466689c10a46b3fd8b31
```

which differs from the authenticated three-hole incumbent at exactly five
positions:

| position | old | new |
|---:|---:|---:|
| 6441 | `0x806d` | `0x006d` |
| 6497 | `0x886a` | `0x8862` |
| 12870 | `0x8c62` | `0x8c63` |
| 12871 | `0x8c61` | `0xcc61` |
| 12872 | `0xcc41` | `0xce41` |

That length-12,873 parent has precisely

\[
H=\{\mathtt{0x287d},\mathtt{0x8ce6},\mathtt{0x9ce6}\}.
\]

Insert `0x0864` at gap 12,870.  The two high holes acquire the literal
witnesses

\[
\begin{aligned}
\mathtt{0x8ce6}&=\bigvee R[12868,12870],\\
\mathtt{0x9ce6}&=\bigvee R[12867,12870].
\end{aligned}
\tag{1.2}
\]

No covered target becomes a hole.  The exact insertion generator
`scratch/search_k16_one_insertion_completion_20260730.cpp`, SHA-256
`c4e8f792264233be60ab87ea061c9ca0e95cd91be006634e25d9fc35aa686c62`,
was replayed on one H100 CPU under a 256 MiB virtual-memory cap.  It exhausted
all 12,874 gaps and all 15 necessary nonzero insertion masks, reported

```text
BEST holes=1 position=12870 value=2148
NO_PASS best_holes=1 best_position=12870 best_value=2148
source_holes=3 candidates=15
```

and reproduced the frozen SHA exactly.  Thus `R` is not merely a heuristic
file: it is the exact best one-insertion descendant of this particular
parent.  This says nothing about altered parents.

## 2. Exact one-substitution calculus

For a word \(W=(w_0,\ldots,w_{n-1})\), let \(c_W(T)\) be the number of
intervals with OR label \(T\).  At a position \(p\), form the left and right
context multisets

\[
\begin{aligned}
\mathcal L_p&=\{0\}\uplus
 \left\{\bigvee_{i=a}^{p-1}w_i:0\le a<p\right\},\\
\mathcal R_p&=\{0\}\uplus
 \left\{\bigvee_{i=p+1}^{b}w_i:p<b<n\right\}.
\end{aligned}
\]

Repeated OR values retain their start/end multiplicities.  If \(w_p\) is
replaced by a nonzero mask \(r\), every changed interval contains \(p\), and

\[
\Delta_{p,r}(T)=
 \sum_{L\in\mathcal L_p,\,Q\in\mathcal R_p}
 \left(
 [L\vee r\vee Q=T]-[L\vee w_p\vee Q=T]
 \right).
\tag{2.1}
\]

This is an exact integer identity, including diagonal multiplicities.  Put
\(C=L\vee Q\).  A replacement can create a target \(T\) exactly when some
context satisfies

\[
C\subseteq T,
\qquad T\setminus C\subseteq r\subseteq T.
\tag{2.2}
\]

Consequently (2.2) generates a finite, complete replacement catalogue; no
arbitrary 16-bit value outside it can install the target.  A candidate is
universal exactly when

\[
c_W(T)+\Delta_{p,r}(T)>0
\quad(0<T<2^{16}).
\tag{2.3}
\]

Equations (2.1)--(2.3), rather than a unique-provider approximation, were
used for every census below.

## 3. Complete installing-substitution census for `R`

There are exactly 26,889 position/replacement pairs satisfying (2.2) for
the missing target `0x287d`.  Exact full multiplicity deltas give the
following collateral-debt histogram:

| new holes | candidates | new holes | candidates |
|---:|---:|---:|---:|
| 2 | 169 | 11 | 3,120 |
| 4 | 201 | 12 | 4,493 |
| 5 | 257 | 13 | 4,454 |
| 6 | 35 | 14 | 3,813 |
| 7 | 208 | 15 | 2,446 |
| 8 | 690 | 16 | 1,263 |
| 9 | 1,175 | 17 | 1,297 |
| 10 | 2,560 | 18 | 305 |
| 19 | 403 |  |  |

The entries sum to 26,889.  In particular there is no debt-zero or debt-one
candidate.

> **Theorem 3.1 (one-substitution no-go and sharp portal debt).** No arbitrary
> one-cell substitution completes `R`.  Every substitution that installs
> `0x287d` creates at least two other holes, and the bound two is attained
> exactly 169 times.

The 169 minimizers form four position/debt families:

| position | old value | replacement count | exact debt pair |
|---:|---:|---:|---|
| 0 | `0x882c` | 128 | `{43117,44141}` = `{0xa86d,0xac6d}` |
| 5921 | `0x2921` | 8 | `{10553,10557}` = `{0x2939,0x293d}` |
| 6440 | `0xa069` | 32 | `{43129,43133}` = `{0xa879,0xa87d}` |
| 12873 | `0xce41` | 1 | `{52833,52835}` = `{0xce61,0xce63}` |

This catalogue is complete for arbitrary nonzero substitutions, not only
one-bit flips or replacements equal to the missing mask.

## 4. The terminal `1 -> 2` portal and its complete one-return census

The cleanest minimum portal is

\[
p=12873:\quad \mathtt{0xce41}\longmapsto\mathtt{0x287d}.
\tag{4.1}
\]

Before (4.1), the two displaced targets have exactly one witness each:

```text
0xce61 : [12872,12873]
0xce63 : [12871,12873]
```

The edit replaces those two witnesses by the singleton witness for
`0x287d`; there are no other holes.  Thus (4.1) is an exact directed exchange

\[
\{\mathtt{0xce61},\mathtt{0xce63}\}
 \longleftarrow
\mathtt{0x287d}.
\tag{4.2}
\]

Starting from the post-portal word, (2.2) gives exactly 2,285 substitutions
capable of installing both high debts.  Their exact final-debt histogram is

\[
1^{128},4^{65},6^{255},7^9,8^{143},9^{98},10^{226},11^{192},
12^{436},13^{350},14^{196},15^{102},16^{44},17^{30},18^8,19^3.
\tag{4.3}
\]

None is universal.  All 128 debt-one returns edit the terminal position
again and lose `0x287d`; they simply toggle the portal to a high-pair state.
Among the 2,157 off-terminal return candidates the minimum debt is four,
attained 65 times:

* 64 replacements at position 6435 lose exactly
  `{20065,20067,20081,20215}`;
* `p12872: 0xcc61 -> 0xce61` loses exactly
  `{52321,52323,52327,52455}`.

> **Theorem 4.1 (no balanced two-cycle through the terminal portal).** No
> second arbitrary substitution can close (4.1).  Any substitution return
> away from the portal position which restores both high targets creates at
> least four new holes.  Hence any closed substitution circuit retaining the
> terminal installation has at least three edit steps.

This is not a global radius-two no-go.  It leaves two exact escapes:

1. begin with one of the other 168 minimum-debt portals and close its debt;
2. use two edits whose joint interaction creates the first `0x287d` witness,
   even though neither edit installs it alone.

Those cases require a simultaneous two-position model using (2.1) on the
union of both supports; composing static signed columns without their mixed
term is unsound.

## 5. Exact next gate

For fixed distinct positions \(p,q\), let

\[
\Delta_{p,r;q,s}(T)
=c_{W^{p\mapsto r,q\mapsto s}}(T)-c_W(T).
\]

Only intervals meeting \(p\) or \(q\) contribute.  Splitting them into
`p-only`, `q-only`, and `both` context rectangles gives a finite exact
two-site evaluator.  The remaining length-12,874 gate is precisely whether
some pair satisfies

\[
c_R(T)+\Delta_{p,r;q,s}(T)>0
\quad(0<T<2^{16}).
\tag{5.1}
\]

A proof-producing implementation should first install the 169 sharp portal
branches, then add the joint-only witness branches separately.  An UNSAT or
exhaustion claim is valid only if both classes are covered.  The terminal
branch can already be removed by Theorem 4.1.

## 6. Scope and independent checks

The repository verifier rejects `R` because of the single hole, as it should.
Independent ending-OR replay, the parent-plus-insertion identity, and the
reproduced insertion generator agree on all claims in Section 1.  The
substitution tables use exact integer interval multiplicities and full
zero-crossing tests.  They do not certify a global two-edit obstruction and
do not change the verified bracket

\[
12873\le \nu(16)\le12875.
\]
