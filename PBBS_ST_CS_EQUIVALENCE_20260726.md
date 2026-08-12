# Gaussian PBBS residence packing and clustered-span cost are equivalent

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, or probabilistic
experiment is used.

## 0. Outcome

Put

\[
 H=\lceil A\sqrt r\rceil,
 \qquad B=\operatorname {Cat}_r,
\]

with fixed \(A>0\).  Let \(\mathcal I_H\) be the family of eligible
nonwrapping quotient residence intervals on the long PBBS quotient cycles,
and let

\[
 \overline\nu_H=\nu(\mathcal I_H)
\]

be its maximum quotient-edge-disjoint packing number.  Let
\(\mathfrak S_H\) be the minimum clustered seam cost

\[
 \sum_J(7H+3S_J-3),
\tag{0.1}
\]

where the selected cuts hit every interval in \(\mathcal I_H\), cuts are
partitioned into clusters on their quotient cycles, and \(S_J\) is the
span of cluster \(J\).  Singleton clusters are always admissible in the
Gaussian window.

Then, modulo the already proved sub-Gaussian-height packing tail,

\[
 \boxed{
 \mathfrak S_H=o_A(B)
 \quad\Longleftrightarrow\quad
 H\overline\nu_H=o_A(B).}
\tag{0.2}
\]

Thus the clustered-span gate \((CS_A)\) and the short packing gate
\((ST_A)\) are equivalent at the coefficient-one scale.  In particular,
if actual Gaussian PBBS returns have

\[
 \overline\nu_H=\Theta_A(B/H),
\]

then no choice of cut transversal and no clustering of the established
form can have \(o(B)\) auxiliary cost.

## 1. Upper comparison: packing gives a cheap transversal

### Lemma 1.1 (circular interval piercing)

For a finite family \(\mathcal I\) of proper intervals on a disjoint union
of cycles, there is a set of at most \(2\nu(\mathcal I)\) cycle edges
meeting every member of \(\mathcal I\).

#### Proof

Work on one cycle.  If the intervals have a common edge, one edge pierces
the family.  Otherwise choose an edge \(e\) which is an endpoint of one
interval and cut the cycle at \(e\).  Intervals not containing \(e\) become
ordinary intervals on a line.  The classical greedy algorithm, choosing
the right endpoint of the leftmost-ending unhit interval, gives a piercing
set whose size equals the line packing number.  Add \(e\) to hit the
discarded intervals.  The line packing number is at most the circular
packing number, so the piercing number is at most \(\nu+1\le2\nu\) when
\(\nu\ge1\).  Sum over the cycles.  \(\square\)

Make every piercing edge a singleton cluster.  Its span is zero and its
cost is \(7H-3\).  Therefore

\[
 \boxed{
 \mathfrak S_H\le2(7H-3)\overline\nu_H.}
\tag{1.1}
\]

Consequently \((ST_A)\) implies \((CS_A)\).

## 2. Lower comparison on the Gaussian-height sector

Fix \(a\in(0,A)\).  Write \(\mathcal I_H^{\ge a}\) for intervals whose
starting Dyck root has height at least \(a\sqrt r\), and put

\[
 \overline\nu_H^{\ge a}=\nu(\mathcal I_H^{\ge a}).
\]

The height-gap theorem says that such an interval has quotient trace length
at least

\[
 a\sqrt r+2\ge {a\over2A}H
\tag{2.1}
\]

for all sufficiently large \(r\).  Set \(\gamma=a/(2A)\).

### Lemma 2.1 (one cluster can serve only span-many disjoint intervals)

Let \(I_1,\ldots,I_t\) be pairwise edge-disjoint cycle intervals, each of
length at least \(\gamma H\).  Suppose a cluster of cuts of span \(S\)
contains one cut belonging to each \(I_i\).  Then

\[
 S\ge\gamma H(t-2).
\tag{2.2}
\]

#### Proof

Lift the cycle immediately before the first cluster cut and order the
intervals met by the cluster from left to right.  Apart from the first and
last intervals, every assigned interval lies wholly between the extreme
cluster cuts.  The middle \(t-2\) intervals are edge-disjoint and each has
length at least \(\gamma H\).  Their lengths therefore sum to at most the
cluster span \(S\).  \(\square\)

### Theorem 2.2 (cluster-cost lower bound)

For every fixed \(a\in(0,A)\), there is \(c_{a,A}>0\) such that

\[
 \boxed{
 \mathfrak S_H\ge c_{a,A}H\overline\nu_H^{\ge a}.}
\tag{2.3}
\]

#### Proof

Choose a maximum edge-disjoint family
\(\mathcal P\subseteq\mathcal I_H^{\ge a}\).  Any cut transversal of
\(\mathcal I_H\) contains a cut in each \(I\in\mathcal P\).  Assign one
such cut to its cluster.  A cut cannot be assigned to two members of
\(\mathcal P\), because the intervals are edge-disjoint.

If cluster \(J\) receives \(t_J\) assigned intervals, Lemma 2.1 gives

\[
 7H+3S_J-3
 \ge 7H-3+3\gamma H(t_J-2)_+.
\tag{2.4}
\]

For \(H\ge2\), the right side is at least

\[
 c_{a,A}Ht_J,
 \qquad
 c_{a,A}:=\min\{1,3\gamma/2\}>0.
\tag{2.5}
\]

(For \(t_J\le3\), use \(7H-3\ge Ht_J\); for \(t_J\ge4\), use
\(t_J-2\ge t_J/2\).)  Summing over clusters and using
\(\sum_Jt_J=|\mathcal P|\) proves (2.3).  \(\square\)

## 3. Restoring the low-height sector

The proved sub-Gaussian height-packing theorem gives a function
\(\varepsilon_A(a)\downarrow0\) as \(a\downarrow0\) such that

\[
 \overline\nu_H^{<a}
 \le \varepsilon_A(a){B\over H}+o_A(B/H).
\tag{3.1}
\]

Assume \(\mathfrak S_H=o_A(B)\).  Theorem 2.2 gives, for every fixed
\(a>0\),

\[
 \overline\nu_H^{\ge a}=o_A(B/H).
\tag{3.2}
\]

Together with (3.1),

\[
 \limsup_{r\to\infty}{H\overline\nu_H\over B}
 \le\varepsilon_A(a).
\]

Letting \(a\downarrow0\) proves \((ST_A)\).  Equation (1.1) proves the
reverse implication, establishing (0.2).

## 4. Exact implication boundary

This comparison uses only:

1. the established residence intervals and their quotient-edge supports;
2. the height-gap theorem;
3. the already proved sub-Gaussian-height packing tail; and
4. the established cluster cost \(7H+3S-3\).

It uses no PBBS return enumeration and no probabilistic assumption.
Therefore cross-cut dominance sharing can improve constants and can merge
dense local requests, but it cannot turn a critical Gaussian packing
\(\Theta(B/H)\) into an \(o(B)\) seam cost.  A proof through the present
PBBS literal compiler still requires the same vanishing chronology theorem
as \((ST_A)\), or a genuinely in-place baseline replacement outside the
additive clustered-cost model.
