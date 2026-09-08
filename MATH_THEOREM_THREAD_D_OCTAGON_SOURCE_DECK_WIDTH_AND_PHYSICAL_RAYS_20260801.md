# The octagon source-deck difference has constant width and constant physical ray number

Date: 2026-08-01  
Lane: Thread D / H2, quaternary-octagon reset  
Status: exact all-`d` source-deck theorem for `d>=5`.  Ambient legality of
turning the internal ray anchors into split hosts remains open.

## 0. Result

Let `Q^0,Q^1` be the two sharp depth-`d` octagon sources, after the two
exterior binary hosts of the split-boundary theorem have been expanded, and
let

\[
             \mathcal D_\epsilon
        =\{\bigcup_{i=s}^t Q_i^\epsilon:0\le s\le t<|Q^\epsilon|\}.
\]

For every `d>=5`,

\[
 |\mathcal D_0\setminus\mathcal D_1|=4d+1,
 \qquad
 |\mathcal D_1\setminus\mathcal D_0|=6d-3.                 \tag{0.1}
\]

Their inclusion-poset widths are exactly

\[
       \operatorname{width}(\mathcal D_0\setminus\mathcal D_1)=6,
       \qquad
       \operatorname{width}(\mathcal D_1\setminus\mathcal D_0)=7. \tag{0.2}
\]

More importantly for physical repair, the two differences have disjoint
partitions into respectively eight and nine **native endpoint rays**: every
part is realized by intervals with one common literal left or right endpoint
in its native expanded source word.

Thus the phase switch does not expose `Theta(d)` unrelated source masks.  It
exposes a constant number of monotone physical rays.  The minimum abstract
chain covers (six and seven chains) are not themselves native ray covers;
the explicit physical refinements use eight and nine rays.

This is not yet a nine-host reset theorem.  Exactly seven anchors in each
phase are tensor-internal source positions.  Phase zero additionally uses the
left exterior near half `L(1)`; phase one uses both `L(1)` and the right
exterior near half `R(9d+25)`.  Splitting or transporting the seven internal
anchors must still preserve owner, deadline, residence, protected witnesses
and the common cap.  The theorem isolates that remaining legality issue; it
does not assume it away.

## 1. Notation

Write

\[
 F=\{f_0,\ldots,f_{d+1}\}
\]

for the filler bank.  If `X` is a set of active labels and `M` a set of
filler indices, abbreviate

\[
                   [X;M]=X\cup(F\setminus\{f_i:i\in M\}). \tag{1.1}
\]

Intervals such as `[i,j]` and `[j,d+1]` below denote sets of filler indices.

## 2. The six-chain decomposition of phase zero

The following six disjoint chains partition
`D_0\D_1`.  Within a displayed row, order the indexed family in the direction
that makes the missing set shrink.

\[
\begin{array}{c|l}
0&[a_3;[2,d+1]]\subset[a_3;[3,d+1]]
       \subset[a_0a_2a_3;\{d+1\}]\\
1&[a_1;\{0,1\}]\subset[a_1;\{0\}]
       \subset[a_1a_2a_3;\{0\}]\subset[a_1a_2a_3;\varnothing]\\
2&[za_1;\{0\}\cup[j,d+1]],\quad 2\le j\le d\\
3&[za_3;[1,j]],\quad 2\le j\le d-1\\
4&[za_3;[0,j]],\quad 2\le j\le d-1\\
5&[za_3;[0,j]\cup\{d+1\}],\quad1\le j\le d-1.
\end{array}                                                \tag{2.1}
\]

The chain lengths are

\[
                  3,4,d-1,d-2,d-2,d-1,                    \tag{2.2}
\]

whose sum is `4d+1`.

The following six members are pairwise incomparable:

\[
\begin{gathered}
[a_1a_2a_3;\varnothing],\quad
[a_0a_2a_3;\{d+1\}],\\
[za_3;\{0,1,2\}],\quad[za_3;\{0,1,d+1\}],\quad
[za_3;\{1,2,3\}],\quad[za_1;\{0,d,d+1\}].              \tag{2.3}
\end{gathered}
\]

Equations (2.1) and (2.3) prove the first equality in (0.2).

## 3. The seven-chain decomposition of phase one

The following seven disjoint chains partition `D_1\D_0`:

\[
\begin{array}{c|l}
0&[a_1;[2,d+1]]\subset[a_1;[3,d+1]]
 \subset[a_0a_1a_3;\{d+1\}]\subset[a_0a_1a_3;\varnothing]\\
1&[a_3;\{0\}\cup[j,d+1]],\ 4\le j\le d+2,
 \quad\text{then }[a_0a_2a_3;\{0\}]\\
2&[a_3;\{0,1\}\cup[j,d+1]],\quad4\le j\le d+2\\
3&[za_1;[1,j]],\quad2\le j\le d-1\\
4&[za_1;[0,j]],\quad2\le j\le d-1\\
5&[za_1;[0,j]\cup\{d+1\}],\quad1\le j\le d-1\\
6&[za_3;\{0\}\cup[j,d+1]],\quad2\le j\le d.
\end{array}                                                \tag{3.1}
\]

Here `j=d+2` means that the tail `[j,d+1]` is empty.  The lengths are

\[
                     4,d,d-1,d-2,d-2,d-1,d-1,             \tag{3.2}
\]

and sum to `6d-3`.

An explicit seven-element antichain is

\[
\begin{gathered}
[a_3;\{0,1\}],\quad[a_3;\{0,d+1\}],
\quad[za_3;\{0,d,d+1\}],\\
[za_1;\{0,1,2\}],\quad[za_1;\{0,1,d+1\}],\quad
[za_1;\{1,2,3\}],\quad[a_1;[3,d+1]].                    \tag{3.3}
\end{gathered}
\]

This proves the second equality in (0.2).

All assertions in Sections 2 and 3 are direct membership checks against the
eight-address sharp inverse.  Active-label signatures first separate most
families; within a fixed signature, containment is reverse containment of
the missing filler intervals.

## 4. Exact native endpoint-ray partitions

Index the expanded source words from zero, including both halves of each
exterior host.  Write `L(s)` for all relevant deck values with a witness
interval starting at `s`, and `R(t)` for those with a witness ending at `t`.

For phase zero, the following eight rays are nonempty, pairwise disjoint,
and partition `D_0\D_1`:

\[
\begin{aligned}
&L(1),\ L(6d+19),\ L(7d+22),\ L(8d+24),\\
&R(6d+16),\ R(7d+19),\ R(7d+20),\ R(7d+21).             \tag{4.1}
\end{aligned}
\]

Their respective lengths are

\[
                         2,d-1,2,1,2,d-1,d-2,d-2.         \tag{4.2}
\]

For phase one, the nine rays are

\[
\begin{aligned}
&L(1),\ L(d+5),\ L(d+6),\ L(2d+7),\ L(3d+10),\\
&R(3d+7),\ R(3d+8),\ R(3d+9),\ R(9d+25),               \tag{4.3}
\end{aligned}
\]

with lengths

\[
                         1,d-1,d-1,d-1,2,d-1,d-2,d-2,2. \tag{4.4}
\]

The sums in (4.2) and (4.4) are exactly (0.1).  Since enlarging an interval
with one endpoint fixed can only enlarge its union, every part is a genuine
inclusion chain.  Direct evaluation of the eight-address source shows that
the values listed in (2.1) and (3.1) occur at exactly the ray partition
claimed in (4.1) and (4.3).

The exterior left-near half is the anchor `L(1)` in both phases.  In phase
one, `R(9d+25)` is also exterior: it is the packet-near half of the right
host.  All remaining anchors in (4.1) and (4.3) are literal tensor-internal
positions, seven in each phase.  Consequently:

* the abstract phase discrepancy has constant physical complexity;
* one cannot identify the Dilworth widths `6,7` with a host count;
* an `8/9`-socket reset is arithmetically possible;
* proving those internal sockets owner/deadline/common-cap legal is the exact
  remaining step before this becomes a whole repair packet.

## 5. Replay

The dependency-free exact replay is

`scratch/audit_threadD_octagon_source_deck_chain_rays_20260801.py`.

It verifies the formulas, partitions, chains, antichains and native endpoint
rays for every `5<=d<=64`.  The formulas themselves are symbolic in `d`; the
finite range is a regression audit, not the logical source of the theorem.

Script SHA-256:

`d077fadb652280b6abea7a2aa1032a92cec294f8872b60e5a51459b395745399`

Audit JSON SHA-256:

`797e767f8594ec2fc830a723d8837602f768655d5ec7d71d86b835f52e5c869c`

Canonical payload SHA-256:

`057efcd6a2551d541c729425cef14c7c365fa10e7dd8056ac7be04cab1cd8183`
