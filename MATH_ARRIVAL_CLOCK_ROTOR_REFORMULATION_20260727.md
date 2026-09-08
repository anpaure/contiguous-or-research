# Arrival clocks: an exact form of the multirow rotor gate

Date: 2026-07-27

## 1. Setup

Let `T=(T_i)_{i in Z_W}` be a `d`-resident cyclic chronology of the middle
layer, and let `P` be its maximal depth-`d` erosion.  A word `A subseteq P`
satisfies

\[
D^dA=T
\tag{1.1}
\]

exactly when, for every coordinate `x` and every `i` with `x in T_i`, the
support of `x` in `A` meets `[i,i+d]`.

Thus each coordinate support is a renewal/hitting set inside the allowed
support supplied by `P`.

## 2. Arrival-time theorem

For `x in T_i`, define its next-arrival clock

\[
a_i(x)=\min\{t\in\{0,\ldots,d\}:x\in A_{i+t}\}.
\tag{2.1}
\]

### Theorem 2.1

If `D^dA=T`, then for every `0<=t<=d`,

\[
(D^tA)_i
=\{x\in T_i:a_i(x)\le t\}.
\tag{2.2}
\]

For every coordinate common to consecutive middle states,

\[
x\in T_i\cap T_{i+1},\quad a_i(x)>0
\quad\Longrightarrow\quad
a_{i+1}(x)=a_i(x)-1.
\tag{2.3}

When `a_i(x)=0`, the clock resets to the distance to the next occurrence of
`x` in `A`.

#### Proof

Membership in `D^tA_i` means precisely that `x` occurs in one of
`A_i,...,A_{i+t}`, which is (2.2).  If the first occurrence after `i` is at
`i+a_i(x)` with positive distance, shifting the starting point to `i+1`
reduces that distance by one; no earlier occurrence can appear, by
minimality.  This proves (2.3).  □

### Converse

Conversely, choose for every coordinate a support `H_x subseteq P_x` which
hits every required length-`d+1` central window, and set

\[
A_i=\{x:i\in H_x\}.
\]

Then (1.1) holds and (2.1)--(2.3) follow.  Hence the support sets and the
countdown clocks are equivalent descriptions.

## 3. Exact lower-coverage reformulation

The depth-`d` sandwich compiler closes the lower ideal if and only if the
renewal supports can be chosen so that

\[
\boxed{
\left\{
\{x\in T_i:a_i(x)\le t\}:
i\in\mathbb Z_W,\ 0\le t<d
\right\}
\supseteq
\{S:1\le |S|<r\}.}
\tag{3.1}
\]

This is the multirow gate with no auxiliary pins or presentation choices.
Each middle state carries a deadline-labelled chain, and the countdown
recurrence couples adjacent chains.  Unbundled symmetric chains correspond
to choosing these deadline orders independently; the entire difficulty is
the renewal consistency (2.3).

The formulation explains why a local abundance theorem is insufficient:
one choice of a coordinate occurrence controls `d+1` consecutive columns
and all their threshold sets simultaneously.  It also gives a constructive
target for recursion: build the central rotor together with its coordinate
renewal clocks, rather than build a rotor and repair its lower tableau later.

## 4. `k=11` audit

For `scratch/sigma_multirow_k11_465.word`, the cyclic base has width 462 and
the depth is three.  The exact arrival counts are

\[
0^{1309},\qquad1^{531},\qquad2^{470},\qquad3^{462}.
\]

Every middle six-set has exactly one coordinate with deadline three.  The
profile distribution is

| multiplicities at deadlines `0,1,2,3` | columns |
|---|---:|
| `(3,1,1,1)` | 396 |
| `(2,2,1,1)` | 48 |
| `(1,3,1,1)` | 10 |
| `(2,1,2,1)` | 7 |
| `(1,2,2,1)` | 1 |

Consequently the cyclic row two is exactly all 462 five-sets, cyclic row one
contains 454 four-sets and eight three-sets, and row zero supplies the
remaining lower quantiles.  After the safe cut and three appended entries,
the corresponding linear counts are 456 and eight.  The countdown
recurrence has zero violations.

Reproduce the audit with

```sh
python3 scratch/sigma_arrival_clock_audit.py \
  --k 11 --depth 3 scratch/sigma_multirow_k11_465.word
```

## 5. Remaining theorem

The exact-formula conjecture would follow from a uniform construction of a
middle rotor and coordinate renewal supports satisfying (3.1), together
with one upper-safe cut.  This is sharper than “universal shadows plus a
compiler”: the same clocks generate the lower shadows and enforce their
cross-depth correlation.
