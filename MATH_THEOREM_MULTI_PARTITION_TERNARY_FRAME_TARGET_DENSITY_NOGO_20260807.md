# Subexponentially many fixed triple partitions cannot repair the canonical queue target obstruction

**Date:** 2026-08-07  
**Method:** sum the exact \(3p\)-target bound over the canonical
\(\mathbb F_3^p\)-frames induced by several global triple partitions  
**Status:** unconditional counting theorem, with an explicit scope boundary.
It rules out every canonical fibre construction based on
\(o(3^p/p)\) preselected global triple partitions. It does **not** rule
out a construction which chooses a new partition adaptively for each
ring, changes frames inside a component, or uses noncanonical source
letters.

## 1. Setup and scope

Use the rank-two queue parameters

\[
 n=2m+1,\qquad p=d+1,\qquad c=m-2p,\qquad
 W={n\choose m}.
\tag{1.1}
\]

Fix an ordered partition \(\mathcal T\) of all but at most two coordinates
of \([n]\) into triples. As in
MATH_THEOREM_TERNARY_FRAME_QUEUE_CYCLE_FACTOR_AND_TARGET_BOUNDARY_20260807.md,
the \(\mathcal T\)-good owners are partitioned into canonical frames

\[
 \mathcal F(J,K)\cong\mathbb F_3^p,
 \qquad |\mathcal F(J,K)|=3^p.
\tag{1.2}
\]

Inside such a frame, a **canonical queue source position** is a source
letter of the form

\[
 K\cup(T_i\setminus\{x\}),
 \qquad i\in[p],\quad x\in T_i.
\tag{1.3}
\]

It has rank \(c+2\). The complete inventory (1.3) has exactly \(3p\)
members, independently of the omission schedule.

Let

\[
 \boldsymbol{\mathcal T}
   =(\mathcal T^{(1)},\ldots,\mathcal T^{(t)})
\tag{1.4}
\]

be any preselected list of \(t\) ordered global triple partitions. A
**\(t\)-partition canonical fibre bank** means any collection of source
positions such that every position is assigned to a pair

\[
 (a,\mathcal F),
 \qquad a\in[t],
 \quad \mathcal F\text{ a canonical frame of }\mathcal T^{(a)},
\tag{1.5}
\]

and uses the canonical source rule (1.3) in that frame. No assumption is
made about how the omissions are scheduled inside a frame. The bank is
**target-clean** when all its rank-\((c+2)\) source letters are distinct.

This definition includes a union of canonical queue rings or paths, with
each component contained in a frame from one of the listed partitions.
It deliberately does not include components which change their literal
frame during the component.

## 2. Exact multi-partition counting bound

### Theorem 2.1 (multi-partition target-density no-go)

Every target-clean \(t\)-partition canonical fibre bank has at most

\[
 \boxed{
  t\,\frac{3p}{3^p}\,W
 }
\tag{2.1}
\]

source positions.

Consequently, if the positions are arranged in vertex-disjoint cyclic
queue rings, the rings cover at most the same number of middle owners.
If instead they form linear paths and \(C\) is the total number of path
components, they cover at most

\[
 \boxed{
  t\,\frac{3p}{3^p}\,W+C
 }
\tag{2.2}
\]

middle-owner vertices.

#### Proof

Fix \(a\in[t]\). The good owners for \(\mathcal T^{(a)}\) are partitioned
into full frames of size \(3^p\). Hence the number \(F_a\) of such frames
satisfies

\[
 F_a\le \frac{W}{3^p}.
\tag{2.3}
\]

In one fixed frame, every canonical source position belongs to the
\(3p\)-element inventory (1.3). Target-cleanliness therefore permits at
most \(3p\) selected positions assigned to that frame. This is true even
for an arbitrary nonstationary omission schedule. Summing first over the
frames of \(\mathcal T^{(a)}\), and then over \(a\in[t]\), gives

\[
 \#\{\text{selected source positions}\}
 \le \sum_{a=1}^t3pF_a
 \le t\frac{3p}{3^p}W,
\]

which is (2.1). Possible collisions of owners or targets between
different partitions can only lower the attainable count.

A cyclic word component has as many owner vertices as source
transitions. A linear path has one more owner vertex than transitions.
Summing this endpoint surplus over the \(C\) paths proves (2.2).
\(\square\)

### Corollary 2.2 (exponential partition requirement)

If a cyclic canonical fibre bank covers at least \(\alpha W\) distinct
owners while keeping the rank-\((c+2)\) source row target-clean, where
\(\alpha>0\), then necessarily

\[
 \boxed{
  t\ge \alpha\frac{3^p}{3p}.
 }
\tag{2.4}
\]

For linear paths with \(C=o(W)\), the same conclusion holds with
\(\alpha\) replaced by \(\alpha-o(1)\).

In particular,

\[
 t=o(3^p/p)
 \quad\Longrightarrow\quad
 \frac{\#\{\text{covered owners}\}}W=o(1)
\tag{2.5}
\]

for cyclic banks, and also for path banks with \(C=o(W)\). Thus any
bounded, polynomial, or more generally \(e^{o(p)}\)-sized preselected
family of global triple partitions has zero asymptotic owner density.

At the merged-PBBS reset density

\[
 \theta=4\sum_{j\ge1}e^{-4\pi j^2}>0,
\tag{2.6}
\]

one needs at least

\[
 \boxed{
  (\theta-o(1))\frac{3^p}{3p}
 }
\tag{2.7}
\]

preselected partitions before this framework can meet even the counting
requirement.

#### Proof

Rearrange (2.1), or (2.2) after subtracting \(C=o(W)\). Since
\(3^p/p=e^{(\log3+o(1))p}\), every \(e^{o(p)}\) value of \(t\) is
\(o(3^p/p)\). \(\square\)

## 3. Sharpness and exact proof boundary

The factor \(3p\) per frame is sharp at the single-frame level: the
ternary quotient construction contains canonical cycles of length \(3p\),
and one such cycle uses the entire inventory (1.3) once. The theorem does
not assert that these one-cycle choices can be made target-disjoint across
all frames or partitions. Therefore (2.1) is a sharp **counting ceiling**
for the fixed-frame mechanism, not a matching existence theorem attaining
that ceiling globally.

The no-go applies even before q1 palettes, fusion, and the upper compiler
are imposed. Those extra requirements can only make the selected bank
smaller.

The conclusion is consequently structural:

\[
 \boxed{
 \begin{minipage}{0.82\linewidth}
 The deterministic one-third owner packing cannot be upgraded to a
 target-clean positive-density packing by trying a bounded or
 subexponential list of fixed global triple partitions and thinning each
 canonical frame. A successful extension must use exponentially many
 partition types in a genuinely correlated outer design, change the
 literal frame within components, or introduce noncanonical source
 inventories.
 \end{minipage}}
\tag{3.1}
\]

This leaves open an orthogonal-array or resolvable-design construction
which correlates the exponentially many required frame systems. It also
leaves open the slack-core decoration route, where different cycles over
the same owner geometry may receive different literal source inventories.
