# MMM parallel switches as exact `c`-space shears

Date: 2026-07-29

Status: exact translation theorem, exact fixed-depth support ledger, and one
reproducible `k=15` finite improvement.  The finite result is **not** a
decorated carrier: it leaves 47 lower-`q2` holes and changes the terminal
lower-`q3` positive-degree count from 11 to 12.

Primary source: Merino--Mička--Mütze, *On a combinatorial generation problem
of Knuth*, especially equations (25a)--(25d).  Their switch replaces one
physical label of a parallel quotient edge, preserves the necklace order,
adds its shift to the voltage, and rotates the suffix of the periodic path.

## 1. Exact shear formula

Put

\[
 k=2m+1,\qquad W=kN,
\]

and let a strict spiral have quotient upper necklaces `U_0,...,U_(N-1)`,
chosen representatives, phase prefix `s_j`, and unit-or-not voltage `v`:

\[
 T_{j+tN}=\rho^{s_j+tv}U_j,
 \qquad j\in\mathbb Z_N,\ t\in\mathbb Z_k.             \tag{1.1}
\]

Assume `v` is a unit.  Its coordinate-zero trace, written by quotient
columns, is

\[
 h_j(t):={\bf1}_{\{0\in T_{j+tN}\}}=c_{j+tN}.          \tag{1.2}
\]

Apply an MMM switch of signed shift `delta` at one quotient edge.  Choose
the quotient origin so that the switched edge is the only boundary between
the prefix and suffix.  Equations (25a)--(25d) give

\[
 s'_j=s_j+\delta\eta_j,
 \qquad v'=v+\delta,                                   \tag{1.3}
\]

where `eta_j` is zero before the switch and one after it.  Define

\[
 q=\delta v^{-1}\pmod k,
 \qquad a=v'v^{-1}=1+q\pmod k,
 \qquad b_j=q\eta_j.                                  \tag{1.4}
\]

### Theorem 1.1 (parallel-switch shear)

If `c'` is the coordinate-zero trace after the switch, then exactly

\[
 \boxed{h'_j(t)=h_j(at+b_j).}                          \tag{1.5}
\]

In particular this is generally not a local bit flip and not a two-run
endpoint swap.

#### Proof

By (1.1)--(1.3),

\[
 h'_j(t)={\bf1}_{\{0\in\rho^{s'_j+tv'}U_j\}}.
\]

The right side of (1.5) is

\[
 h_j(at+b_j)
 ={\bf1}_{\{0\in\rho^{s_j+(at+b_j)v}U_j\}}.
\]

Equations (1.4) make the two exponents equal.  This proves (1.5).  Notice
also that the coordinate multiplier used to normalize the new voltage to
one fixes coordinate zero, so it does not alter this trace identity.  \(\square\)

There is a useful geometric form.  Cut the physical cycle at the `k` lifts
of the switched quotient edge.  The retained pieces are `k` paths of one
quotient lap each.  Before the switch, the path ending on sheet `t` is
joined to the next path on sheet `t+v`; after the switch it is joined to the
path on sheet

\[
                         t+v+\delta.                   \tag{1.6}
\]

Thus the switch is a global permutation of `k` long retained blocks.  Both
orders are one physical cycle exactly when `v` and `v+delta` are units.

## 2. Starts, ends, residence, and shadows

At every quotient seam other than the switched one, (1.5) merely reindexes
the `k` sheet pairs.  At the switched seam it replaces the old pairing
`t -> t` by `t -> t+q` (after dividing phases by `v`).  At the cyclic wrap,
the multiplier `a=1+q` cancels the suffix jump `q`, so the old wrap pairing
is again merely reindexed.

Consequently:

1. all class sums are unchanged;
2. every unaffected quotient seam still has one insertion and one deletion;
3. the alternate physical incidence also has one insertion and one deletion;
4. hence the start and end residues remain transversals and the new trace is
   again run-transversal; and
5. middle Hamiltonicity and the perfect lower-`q1` rainbow are preserved
   whenever the new voltage is a unit.

Run *locations* need not be close.  Formula (1.6) can reconnect all `k`
long blocks differently.  Internally each retained block is unchanged, so
the exact residence test is the seam-collar criterion: every old short run
must have its closed span hit by a deleted seam, and every possible new
short run lies in a collar of an inserted seam.  For a residence-clean input
only the latter test remains.

For fixed-depth shadows the change is nevertheless local in quotient
support.  A `q`-edge window is changed only if it meets the switched edge.
Therefore one parallel switch changes at most `q` quotient-window
occurrences at depth `q`.  In particular:

* upper `q1` changes exactly one quotient edge-union occurrence;
* lower `q2` changes only the two triple-intersection occurrences that meet
  the switched edge; and
* fixed-width upper windows have the analogous collar bound.

There is no such bound for unrestricted upper intervals: the new long-block
order combines new suffixes and prefixes.

## 3. Correct run-transversal parameterization

The phrase “start and end are permutations `Z_N -> Z_k`” is false when
`N != k` (at `k=15`, `N=429`).  The exact data are as follows.  List the
`N` cyclic one-runs in cyclic order.  For run `a`, let

\[
 \sigma_a\in\mathbb Z_W,
 \quad \ell_a\ge d+1,
 \quad \epsilon_a=\sigma_a+\ell_a-1,
 \quad g_a=\sigma_{a+1}-\epsilon_a-1\ge1.             \tag{3.1}
\]

Then

\[
 \sum_a\ell_a=rN,
 \qquad \sum_a(\ell_a+g_a)=W,                         \tag{3.2}
\]

and run transversality is exactly the assertion that both residue lists

\[
 (\sigma_a\bmod N)_a,
 \qquad(\epsilon_a\bmod N)_a                           \tag{3.3}
\]

are permutations of `Z_N`.  The inserted- and deleted-coordinate functions
on quotient seams are maps `Z_N -> Z_k`; they are not permutations and may
repeat.  An arbitrary pair of permutations plus a composition is not enough:
the positive gaps, lifted cyclic order, and recurrence (3.1) are essential.

With `alpha_j` the coordinate deleted on seam `j` and `beta_j` the coordinate
inserted there, the correctly indexed gap identities are

\[
\begin{aligned}
 T_j\cap T_{j+1}
   &=T_j\setminus\{\alpha_j\},\\
 T_j\cap T_{j+1}\cap T_{j+2}
   &=T_j\setminus\{\alpha_j,\alpha_{j+1}\},\\
 T_j\cup\cdots\cup T_{j+w-1}
   &=T_j\cup\{\beta_j,\ldots,\beta_{j+w-2}\}.
                                                               \tag{3.4}
\end{aligned}
\]

Repeated entries on the right are harmless because these are set unions.

## 4. A literal `k=15` escape from the two-run neighborhood

The exact fixture

```text
scratch/fixtures/k15_residence_hint_explicit_v1.json
SHA-256 4482c3d448b3e314f89cc0c6e3f04a950e12a9e97ceb680da0478a00f2f4ee10
```

selects five quotient incidences lying in nontrivial parallel-edge groups.
Enumerating all 32 label assignments gives 15 unit-voltage physical cycles.
One switch is

\[
 (1807,7,12)\longrightarrow(1807,11,12).              \tag{4.1}
\]

The changed inclusion edge has voltage `0 -> 7`; thus (4.1) is an MMM
shift-seven switch (up to the paper's rotation/reversal convention), and
the total spiral voltage changes `1 -> 8`.

The repository-owned exact physical audit gives:

| quantity | before | after |
|---|---:|---:|
| physical middle vertices | 6435 distinct | 6435 distinct |
| lower `q1` colours | 6435 distinct | 6435 distinct |
| residence defects | 0 | 0 |
| lower `q2` holes | 47 | 47 |
| terminal lower `q3` positive-degree holes | 11 | 12 |
| exact all-width upper holes | 95 | **94** |

The exact upper delta is one gained rank-nine orbit representative `1951`
and no lost upper orbit.  The lower-`q2` missing family is identical.  The
new lower-`q3` hole is representative `1159`.

This one switch changes 3,092 of the 6,435 bits of the coordinate-zero trace,
removes and adds 406 run starts, and removes and adds 406 run ends.  It is
therefore a genuine multi-run move, while preserving the two eager run
transversals, residence, middle Hamiltonicity, and the exact lower first
shadow.  In the current width-eight annealer's exact objective it changes

```text
(middle,q1,q2,upper,E)=(0,0,47,95,661)
                       ->(0,0,47,94,658).
```

Thus it strictly improves the score by three.  The short-window upper
support is globally rearranged (81 orbit representatives enter and 80
leave), even though exact all-width support gains representative `1951` and
loses none.  It is an exact escape from the reported two-run local minimum,
but not a solution of the carrier problem.

The shear formula itself is also checked literally on this pair: every one
of the 429 columns has a unique affine offset in (1.5), and the offset word is

```text
0^381 7^48
```

with multiplier `a=8`.  Thus the finite switch is exactly the two-piece
affine shear predicted by Theorem 1.1, not merely an endpoint-orbit match.
The nonzero run-histogram delta is

```text
4:-2, 5:+2, 8:+2, 9:-1, 11:+1, 12:-1, 14:-1, 19:-1, 25:+1.
```

In particular the minimum remains four and the total remains 429 runs.

Reproduction:

```sh
python3 scratch/audit_k15_mmm_parallel_switch_cspace_escape_20260729.py
```

Frozen summary:

```text
scratch/k15_mmm_parallel_switch_cspace_escape.audit.json
```

The audit script has SHA-256

```text
323601c0edbcd5a209b9ba99432fd63347dd3d708b8ad03515f4b6a083427289
```

## 5. Gluing-label moves give a second multi-run graph

The potential-decreasing MMM arborescence family is a Cartesian product of
one gluing-label menu for every non-star plane tree.  Changing one menu
choice keeps the potential-decreasing arborescence, hence both endpoints are
quotient Hamilton cycles with the exact lower first shadow.  The product
graph is connected.  Applying the paper's usable voltage repair at an
endpoint whose raw voltage is not a unit restores a strict physical spiral.

For `k=15`, the independent extractor finds 33 variables with menu histogram

\[
                         1^7,\ 2^{19},\ 3^7.           \tag{5.1}
\]

Against the all-first-choice endpoint, every one of the 33 nontrivial
single-variable changes toggles exactly 12 inclusion-edge orbits, changes
five or six contracted lower choices, and remains one 858-vertex quotient
Hamilton cycle.  Among the raw endpoints, 18 of 33 already have unit
voltage.  These are mathematically valid multi-run neighbors far outside an
endpoint-swap annealer.

This proves that the MMM state space contains a connected central/`q1`-safe
large-neighborhood graph.  It does **not** prove monotone descent for
residence, `q2`, upper shadows, or compiler Hall.  Exact `k=11` enumeration
already shows that the full published gluing-tree family contains no member
passing all three carrier gates simultaneously.  The positive theorem is
the existence of safe large moves, not the existence of a decorated endpoint.
