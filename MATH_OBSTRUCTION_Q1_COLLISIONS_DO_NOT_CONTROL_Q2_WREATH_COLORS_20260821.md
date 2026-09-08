# q=1 collisions do not control q=2 colours in an exact wreath factor

**Date:** 2026-08-21  
**Method:** exact Johnson-cycle reduction plus a literal b=9 factor  
**Status:** unconditional finite obstruction and exact physical gate; no
asymptotic nonexistence claim

## 0. Outcome

Put \(b=2r+1\), and let \(\mathscr F\) be an exact factor of the rank-r
layer into cyclic-interval wreaths.  The q=1 windows of its rows form a
physically FIFO-legal cycle system in \(J(b,r-1)\):

* each rank-r target occurs exactly once as the **union colour** of a
  consecutive q=1 pair;
* a q=1 target of multiplicity \(m\) has degree \(2m\) in the collapsed
  cycle system; and
* every depth-q target is the **intersection colour** of q consecutive q=1
  vertices on one of the same row cycles.

Thus q=1 collision data controls only vertex visit multiplicities.  Deeper
coverage is a path-colour condition on the same serialized cycles.

This distinction is already strict inside genuine exact \(C_9\) wreath
factors.  There are two exact fourteen-row factors with the same optimal
q=1 duplicate excess

\[
                         Q_1=A-A_1=42,                 \tag{0.1}
\]

such that one has

\[
                    (h_1,h_2,h_3)=(0,0,0),            \tag{0.2}
\]

while the other has

\[
                    (h_1,h_2,h_3)=(0,2,0).            \tag{0.3}
\]

The missing q=2 targets in the second factor are \(\{3,8\}\) and
\(\{7,9\}\).  Both factors also have minimum q=1 pair energy 42 and maximum
q=1 load two.  Therefore even complete and optimally balanced q=1 coverage
does not imply exact q=2 coverage: the scalar q=1 load data do not determine
the next layer.  An exact all-depth lift needs an additional path-colour,
recursive-design, or simultaneous-current hypothesis.  The finite example
does not rule out an asymptotic inequality which bounds deeper holes in
terms of \(Q_1\) and would still suffice for an o(A) theorem.

## 1. The exact cycle-colour identity

For a row \(C=(c_i)_{i\in\mathbb Z_b}\), write

\[
 S_i=I_C(i,r-1),\qquad M_i=I_C(i,r).                 \tag{1.1}
\]

### Proposition 1.1 (same-row Johnson serialization)

For every i,

\[
 S_i\cup S_{i+1}=M_i,\qquad
 S_i\cap S_{i+1}=I_C(i+1,r-2).                       \tag{1.2}
\]

More generally, for \(1\le q<r\),

\[
 \bigcap_{j=0}^{q-1}S_{i+j}=I_C(i+q-1,r-q).          \tag{1.3}
\]

Consequently the sequences \((S_i)_{i\in\mathbb Z_b}\) are simple
length-b cycles in \(J(b,r-1)\).  Their edge union-colours are the rank-r
windows of \(\mathscr F\), each exactly once, and their q-vertex path
intersection-colours are exactly the depth-q windows of \(\mathscr F\).

If \(\mu_1(S)\) is the q=1 multiplicity and the row cycles are collapsed
on equal target labels, then

\[
                            d(S)=2\mu_1(S).           \tag{1.4}
\]

#### Proof

Unwrap the cyclic word over the span from i to \(i+r+q-3\); this span has
length at most \(2r-2<b\).  Consecutive length-\((r-1)\) windows delete the
left endpoint and add the next right endpoint.  Their union and intersection
give (1.2), and intersecting q consecutive windows leaves exactly the block
from \(i+q-1\) through \(i+r-2\), proving (1.3).

The labels in one row are distinct, so its q=1 windows are distinct.  Exact
middle ownership says that the union colours (1.2) over all rows and starts
are precisely \(\binom{[b]}r\), once each.  Finally every occurrence of S
has one predecessor and one successor edge on its row cycle, proving
(1.4). \(\square\)

Proposition 1.1 keeps the physical constraint explicit: the cycles are not
arbitrary Johnson cycles.  They are sliding-window cycles of permutations,
so their dropped and inserted labels obey the FIFO queue law.

## 2. A literal q=1-complete, q=2-incomplete factor

For \(b=9,r=4\), take the following fourteen unoriented cyclic orders:

\[
\begin{array}{llll}
125784369,&125893674,&126537894,&132674958,\\
134629578,&143289657,&146593728,&148769235,\\
159347286,&159428637,&163547298,&172358649,\\
176258439,&187654239.
\end{array}                                                \tag{2.1}
\]

Their rank-four cyclic windows partition all \(\binom94=126\) middle
targets.  Their rank-three support is all 84 targets, while their rank-two
support has size 34 and misses exactly \(\{3,8\}\) and \(\{7,9\}\).  Their
rank-one support is complete.  The q=1 multiplicity statistics are

\[
 Q_1=42,\qquad
 \sum_S\binom{\mu_1(S)}2=42,\qquad
 \max_S\mu_1(S)=2.                                      \tag{2.2}
\]

For comparison, the audited balanced vertical factor
`m4_switch_balanced_vertical_wreath_factor.txt` has (0.2) and exactly the
same three q=1 scalar statistics in (2.2).  Thus even the optimally balanced
q=1 load histogram \(1^{42}2^{42}\) does not determine q=2 coverage.

The factor (2.1) was found by an H100 CP-SAT search minimizing q=2 support
subject to q=1 completeness.  Optimality for q=2 holes is not claimed, and
its validity no longer depends on the solver: the checker enumerates every
displayed cyclic window directly.

## 3. Exact sufficient condition exposed by the reduction

Proposition 1.1 reduces the all-depth construction to the following
physically scoped object.  One needs FIFO-legal length-b Johnson cycles
whose union-coloured edges partition \(\binom{[b]}r\), whose vertex
collision excess is \(O(A/b)\), and whose q-consecutive intersection-colour
supports have aggregate complement o(A) for \(1\le q\le H\).

This condition is both sufficient and, after reading the q=1 cycles from
an exact wreath factor, necessary.  It is stronger than a near-regular
q=1 degree condition: (2.1) satisfies the optimal q=1 support, collision
ledger, and pair energy but fails two q=2 colours.  At growing b the finite example does not
rule out a quantitative inequality using additional expansion or current
information; it isolates exactly what that information must control.

## 4. Scope

The proved claims are the exact same-row identities (1.2)--(1.4) and the
literal exact-factor separation (0.2)--(0.3).  The note does not prove a
linear or asymptotic q=2 deficit, does not rule out a recursive all-depth
factor, and does not claim that q=1 energy plus a specified stronger
path-expansion hypothesis is insufficient.

## 5. Checker

The H100 audit is

```text
scratch/audit_wreath_q1_cycle_q2_color_gate_20260821.py
```

It checks exact middle ownership, every union/intersection identity, the
degree formula, both all-depth profiles, the common optimal q=1 scalar
statistics, and the two missing pairs.
