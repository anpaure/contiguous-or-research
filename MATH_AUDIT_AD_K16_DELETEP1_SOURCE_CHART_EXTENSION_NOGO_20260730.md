# K16 gap one: exact delete-p1 source-chart extension no-go

Date: 2026-07-30  
Lane: AD  
Status: proved exact no-go for one frozen source-chart catalogue; this is not
an infeasibility theorem for the full `(4,9,4)` profile

## 1. Frozen scope

The root word is

```text
scratch/k16_upper12874_best_delete.word
SHA-256 a72cc9e0ba87dabf1005ce750ffd738e7eeef92599a0d8f9dfe80b26f458a649
length 12873
sole hole 0x2c6d
```

Its seventeen editable cells have profile `(4,9,4)` and absolute positions

\[
0,1,2,3;quad 6435,\ldots,6443;quad 12869,\ldots,12872.
\tag{1.1}
\]

The maximal-context chart ledger is read from

```text
scratch/occupancy_blocker_v3_4_9_4_anchorany.map.json
SHA-256 546d200ddbbc3fb85725d9b8e4e561aaf0cf80e285f5f59b4fea781103ba602d
```

Let \(R\) be its 57-target repair family and put

\[
                         H=\mathtt{2c6d}.
\tag{1.2}
\]

For \(T\in R\setminus\{H\}\), let \(\mathscr C_T\) be the set of
maximal-context charts \((J,b_T(J))\) which are literally realized by the
root:

\[
             b_T(J)\vee\bigvee_{p\in J}W_p=T.
\tag{1.3}
\]

There are 62 such charts.  Their per-target multiplicities are

\[
 51\text{ targets with one chart},\quad
 4\text{ with two},\quad 1\text{ with three},
\tag{1.4}
\]

while \(H\) has none.  Consequently there are exactly

\[
                        3\cdot2^4=48
\tag{1.5}
\]

ways to choose one root chart for every old repair target.  Target \(H\)
has the usual 65 local charts in this profile.

## 2. Exact source-chart criterion

Fix one chart \((I,b_H(I))\) for \(H\), and choose one
\(J_T\in\mathscr C_T\) for every \(T\ne H\).  For each of the seventeen
positions define

\[
 K_p=\bigcap_{\substack{T\in R\\p\in J_T}}T,
\tag{2.1}
\]

where \(J_H=I\), and use `0xffff` for the intersection of an empty family.

### Theorem 2.1 (exact restricted-catalogue criterion)

The selected 57 charts are simultaneously realizable by nonzero collar
values if and only if

\[
 K_p\ne0\quad\text{at every used position},
\tag{2.2}
\]

and

\[
 b_T(J_T)\vee\bigvee_{p\in J_T}K_p=T
                         \qquad(T\in R).
\tag{2.3}
\]

When these conditions hold, assigning \(K_p\) at used cells realizes every
selected chart literally.

#### Proof

This is Theorem 3.1 of the chart-intersection reduction with the chart
supports fixed.  Necessity follows because any realizing value at \(p\) is
a nonzero submask of every target whose chart contains \(p\), hence a
submask of \(K_p\), and every required target bit must occur in some such
intersection.  Conversely (2.2) makes the canonical values nonzero, while
(2.3) says precisely that the maximal fixed context and their variable OR
equal the target.  Maximal-context equivalence turns each equality into a
literal interval.  Targets outside \(R\) retain fixed-gap witnesses.
\(\square\)

This criterion allows all seventeen reconstructed values to differ from the
root.  Only the **supports** of the 56 old charts are restricted to charts
already witnessed by the root.

## 3. Exact finite no-go

### Theorem 3.1 (no source-chart extension)

No choice of one of the 65 charts for \(H\), together with one root chart
from each \(\mathscr C_T\), satisfies Theorem 2.1.

#### Audit

The complete product contains

\[
                            65\cdot48=3120
\tag{3.1}
\]

selections.  Exact intersection replay gives

\[
\begin{array}{c|r}
\text{first failed condition}&\text{selections}\\ \hline
K_p=0\text{ at a used cell}&768\\
\text{some durable equality (2.3) fails}&2352\\
\text{pass}&0.
\end{array}
\tag{3.2}
\]

At the chart level, 16 of the 65 choices for \(H\) give a zero intersection
for all 48 old-chart selections.  The other 49 avoid zero intersections for
all 48 selections but fail at least one durable equality.

The replay is solver-free and enumerates only the 3,120 explicitly defined
chart selections.  Its source is

```text
scratch/audit_ad_k16_deletep1_source_chart_extension_20260730.py
SHA-256 3503175e66d38815130d41cf036520b8787586bdc1b308bfd91dcb4d3c3bea4a
```

It independently pins both input hashes, reconstructs (1.3)--(1.5), forms
all intersections (2.1), and checks (2.2)--(2.3) directly.

## 4. Narrow root-frozen splice and the eleven residual charts

There is a useful smaller sufficient construction, but its scope needs to be
stated explicitly.  Fix an \(H\)-chart \(I\), leave every cell outside
\(I\) equal to the root value \(W_p\), and on \(I\) use the greatest values
compatible with \(H\) and the selected old charts.  For an old root chart
\(J_T\), every required bit omitted by \(H\) must then retain an original
root supplier outside \(I\):

\[
 (T\setminus b_T(J_T))\setminus H
 \subseteq \bigvee_{p\in J_T\setminus I}W_p.
\tag{4.1}
\]

For choices obeying (4.1), the greatest legal value on \(p\in I\) is

\[
 C_p=H\cap\bigcap_{\substack{T\ne H\\p\in J_T}}T.
\tag{4.2}
\]

### Lemma 4.1 (exactness of the root-frozen splice test)

Within the operation just defined, the old charts and the proposed
\(H\)-chart are simultaneously realized if and only if (4.1) holds for
every old chart, every \(C_p\) is nonzero, and

\[
                 b_H(I)\vee\bigvee_{p\in I}C_p=H.
\tag{4.3}
\]

#### Proof

Outside \(I\), the root values are unchanged.  Inside \(I\), every bit not
in \(H\) is absent.  Thus (4.1) is exactly the condition that each such old
required bit keeps a supplier.  A required old bit lying in \(H\) keeps any
original supplier outside \(I\), and an original supplier inside \(I\) is
contained in every selected old target active there, hence in \(C_p\).
Therefore all old charts survive.  Nonzeroness and (4.3) are exactly the
remaining conditions for the new chart.  Conversely failure of any one of
these conditions makes the stated root-frozen operation impossible.
\(\square\)

Condition (4.1) is not asserted to be necessary when cells outside \(I\)
are also free: an intersection of target masks can in principle add a bit
which the root did not carry there.  The unrestricted-value statement is
instead Theorem 3.1, proved by the full exact replay.

The root-frozen filter rejects 54 of the 65 \(H\)-charts because at least one
old target has no chart satisfying (4.1).  The number of individually
impossible old targets ranges from 1 through 32.  The eleven surviving
charts admit 492 old-chart selections in total, but every selection for a
fixed \(H\)-chart gives the same vector (4.2).  The exact vectors and the
bits missing from (4.3) are shown below; all eleven surviving
\(H\)-charts have zero fixed context.

\[
\begin{array}{c|c|c}
(\text{block},a,b)&(C_a,\ldots,C_b)&H\setminus\bigvee C_p\\ \hline
(0,1,1)&(2069)&0c04\\
(0,1,2)&(2069,046d)&0800\\
(0,1,3)&(2069,046d,042d)&0800\\
(0,2,2)&(046d)&2800\\
(0,2,3)&(046d,042d)&2800\\
(0,3,3)&(042d)&2840\\
(1,3,3)&(2869)&0404\\
(1,3,4)&(2869,206d)&0400\\
(1,4,4)&(206d)&0c00\\
(1,6,6)&(042d)&2840\\
(2,1,1)&(0c61)&200c.
\end{array}
\tag{4.4}
\]

All masks in (4.4) are hexadecimal.  Every missing mask is nonzero, so the
narrow splice has no completion.

## 5. Exact boundary

Theorem 3.1 closes the following class:

* choose an arbitrary local chart for the sole hole `0x2c6d`;
* for every other repair target, retain the support of one maximal-context
  chart already witnessed by the delete-p1 root; and
* assign arbitrary nonzero values to the seventeen cells, tested through
  their exact canonical intersections.

It does **not** close the full `(4,9,4)` profile.  A completion may move one
or more old repair targets to a chart support not witnessed by the root.
It also says nothing about the sibling profiles, a changed fixed gap, or an
unrelated length-12,873 word.  Thus the sharp remaining obstruction inside
the fixed-gap profile is precisely simultaneous migration of at least one
old target together with the missing target; mere addition of one new chart
to the complete root chart catalogue is impossible.
