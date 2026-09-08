# Entrance/exit capacity for exact dimension induction

Date: 2026-09-08. Author: Codex subagent `exact_b_induction`.

Status: new finite necessary condition, proved below. It does not prove or
disprove `nu(k)=B(k)`. In particular it is not an existence theorem for a
word attaining the lower bound. The arithmetic table was evaluated only on
`ssh h100`; no mathematical program ran locally.

## 1. Scope and what changed

The earlier finite-lift audit
`FINITE_LIFT_SLACK_THEOREMS_AUDIT_20260724.md`, Sections 8–10, groups a
tagged witness by its first and last tagged runs. Its valid bound has a
quadratic run allowance, `r*(binom(q,2)+3q)`.

A different charging argument gives a linear allowance. It counts every
witness that starts at a tagged position against that position, including
witnesses that leave its tagged run. Only witnesses starting at an untagged
position need a boundary charge, and each crosses an entrance cut.
Reversing the word gives a separate exit-cut condition.

For an exact word in dimension 17, this forces **each coordinate to have at
least 179 entrance cuts and 179 exit cuts**. Thus it has at least 358 tag
transitions for each coordinate. This replaces the earlier necessary
17-run lower bound by at least 179 tagged runs. A coordinate appearing in
either endpoint letter needs at least 180 tagged runs.

These are conditions on every possible word, not merely on a selected
carrier or fixed-window compiler. They rule out bounded-piece dimension
splices as an all-dimension exact construction, while allowing highly
distributed coordinate support.

## 2. Fixed-cut lemma

Let `A=(A_1,...,A_N)` be a word of nonempty subsets of `X union {z}`,
where `|X|=k`. Write `P_i=A_i minus {z}` for the old-coordinate projection.
Fix a cut between positions `c` and `c+1`, and put

\[
 C_c=P_c\cup P_{c+1}.
\]

For any rank `r>=1`, the number of distinct rank-r old projections of
intervals crossing this cut is at most

\[
 \boxed{[r-|C_c|+1]_+.}                                      \tag{2.1}
\]

Proof. Such an interval has old projection `L_i union R_j`, where

\[
 L_i=\bigcup_{p=i}^{c}P_p,
 \qquad R_j=\bigcup_{p=c+1}^{j}P_p.
\]

Replace `L_i` by `L_i union P_{c+1}`; this does not change its union with
`R_j`. The distinct modified left states form an inclusion chain starting
above `C_c`. States with cardinality greater than `r` cannot contribute.
There are at most `r-|C_c|+1` remaining distinct states. For each such
state, union with the right chain is again a chain and gives at most one
distinct set of rank `r`. If `|C_c|>r`, no output is possible. This proves
(2.1). No disjointness of the left and right projections is assumed.

At a tag-transition cut, the adjacent untagged letter is nonempty, so
`|C_c|>=1`. Consequently (2.1) is at most `r`.

## 3. Entrance and exit inequalities

Let `h_z` be the number of letters containing `z`. Define the entrance and
exit cut sets

\[
 E_z=\{c:z\notin A_c,\ z\in A_{c+1}\},\qquad
 F_z=\{c:z\in A_c,\ z\notin A_{c+1}\}.
\]

If the word covers all targets `T union {z}` with `T subseteq X` and
`|T|=r`, then

\[
 \boxed{\binom{k}{r}\le h_z+
   \sum_{c\in E_z}[r-|C_c|+1]_+,}                             \tag{3.1}
\]

and independently

\[
 \boxed{\binom{k}{r}\le h_z+
   \sum_{c\in F_z}[r-|C_c|+1]_+.}                             \tag{3.2}
\]

Proof of (3.1). Select one literal witness for each required tagged target.
All targets with a witness starting at a tagged position contribute at
most `h_z`: at a fixed start, successive interval unions form an inclusion
chain and have at most one distinct old projection of rank `r`.
Every remaining selected witness starts at an untagged position and meets a
tagged position, hence crosses at least one entrance cut. Assign it, for
example, to its first entrance cut. At each cut apply (2.1). The assignments
and the tagged-start charge exhaust every selected witness. The exit
inequality is (3.1) applied to the reversed word.

In particular,

\[
 |E_z|,|F_z|\ \ge\
 \left\lceil\frac{[\binom{k}{r}-h_z]_+}{r}\right\rceil.       \tag{3.3}
\]

The weighted inequalities can be much stronger than (3.3): the charge at
an entrance is `r-|C_c|+1`, not always `r`.

## 4. Exact-budget corollary

If the word is universal, deleting all tagged letters leaves a universal
word on `X`: every witness for an old target was entirely untagged, so it
remains an interval after deletion. Therefore

\[
 N-h_z\ge\nu(k)\ge B(k).
\]

Set

\[
 G(k,r,N)=[\binom{k}{r}+B(k)-N]_+.
\]

Every coordinate in a universal `(k+1)`-dimensional word satisfies

\[
 \boxed{|E_z|,|F_z|\ge\left\lceil G(k,r,N)/r\right\rceil.}   \tag{4.1}
\]

When `k=2r`, `N=B(2r+1)`, and `d_j=B(j)-W(j)`, the exact numerator is

\[
 G=\operatorname{Cat}_r+d_{2r}-d_{2r+1}.                     \tag{4.2}
\]

Thus an exact odd-dimensional word requires

\[
 |E_z|,|F_z|\ge
 \left\lceil\frac{\operatorname{Cat}_r+d_{2r}-d_{2r+1}}r
 \right\rceil,                                               \tag{4.3}
\]

whenever the numerator is positive. This is
`Theta(4^r/r^(5/2))` entrance cuts and independently that many exit cuts,
using `d_j=O(sqrt(j))` and the elementary Catalan asymptotics already proved
in the handoff. In particular, an exact recurrence whose new bit occupies
only a fixed number or polynomial number of intervals cannot work in every
dimension, regardless of the internal words used in those intervals.

For a word whose `z`-tagged positions form `q_z` maximal intervals,

\[
 |E_z|=q_z-\mathbf1_{z\in A_1},\qquad
 |F_z|=q_z-\mathbf1_{z\in A_N}.
\]

Hence if (4.1) requires `Q` entrances and exits, then

\[
 q_z\ge Q+\max(\mathbf1_{z\in A_1},\mathbf1_{z\in A_N}).       \tag{4.4}
\]

## 5. Exact finite arithmetic

The following numbers use the definition of `B` in the handoff. They do not
assume equality with `nu` in the child dimension.

| old k | child | B(k) | B(k+1) | G | minimum entrances | minimum exits |
|---:|---:|---:|---:|---:|---:|---:|
| 6 | 7 | 21 | 37 | 4 | 2 | 2 |
| 8 | 9 | 72 | 128 | 14 | 4 | 4 |
| 10 | 11 | 254 | 465 | 41 | 9 | 9 |
| 12 | 13 | 926 | 1719 | 131 | 22 | 22 |
| 14 | 15 | 3434 | 6438 | 428 | 62 | 62 |
| 16 | 17 | 12873 | 24313 | 1430 | 179 | 179 |
| 18 | 19 | 48623 | 92381 | 4862 | 541 | 541 |

For example, at dimension 17 the untagged word has at least 12,873
positions, so `h_z<=24313-12873=11440`. There are 12,870 tagged targets
whose old projection has rank 8. Entrances must therefore supply at least
1,430 targets beyond the tagged-start capacity. Every entrance contributes
at most eight, giving at least 179 entrances. The exit proof is separate.

Arithmetic reproduction (run only on `ssh h100`):

```python
from math import comb

def B(k):
    s = (k + 1) // 2
    w = comb(k, s)
    low = sum(comb(k, j) for j in range(1, s))
    d = 0
    while d*w + d*(d+1)//2 < low:
        d += 1
    return w + d

for k in (6, 8, 10, 12, 14, 16, 18):
    r = k // 2
    gap = comb(k, r) + B(k) - B(k+1)
    print(k, B(k), B(k+1), gap, (gap+r-1)//r)
```

## 6. Consequence for the induction investigation

The old exact shared-tail/dual-erosion proposal was already ruled out by
the nonzero-source theorem in
`MATH_ODD_EVEN_SHARED_TAIL_LIFT_20260727.md`, Section 7: a source with
consecutive distinct equal-rank fixed-window unions cannot have a zero
projection, so its tagged sector misses the new singleton.

The new entrance/exit inequalities show that merely replacing that proposal
by a bounded number of sectors does not fix the exact even-to-odd step.
The new coordinate must be distributed across exponentially many sectors
in an exact odd-dimensional construction. This supports pursuing an
unrestricted state/owner construction or a recurrence that simultaneously
interleaves many short pieces. It supplies no theorem that such a
construction exists, and it does not invalidate any previously certified
exact word.
