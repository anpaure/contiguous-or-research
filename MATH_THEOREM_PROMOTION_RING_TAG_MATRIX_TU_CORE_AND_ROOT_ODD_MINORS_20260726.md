# Promotion-ring tags: the TU census core and root-density physical odd minors

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
external input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad W=\binom{2m}m,\qquad
 N_q=\binom{2m}{m-q},\qquad M=m+H,
 \tag{0.1}
\]

Assume \(4\le H=o(m)\), as in the calibrated promotion-ring regime,
and take one fixed promotion ring of length \(M\) over every rank-\(M\)
top.  There are \(N_H\) rings and

\[
 L:=MN_H
 \tag{0.2}
\]

phase slots.  Tags have the exact SCD census

\[
 \gamma_d=N_d-N_{d+1}\quad(0\le d<H),
 \qquad \gamma_H=N_H,
 \tag{0.3}
\]

with \(E=L-W\) blanks on the covering-side calibration.

This note settles the matrix-structure question as follows.

1. **The census/root subsystem is TU.**  Slot occupancy, the global tag
   counts, and exactly one tag \(H\) in every ring form a bipartite
   transportation matrix.  Thus the exact tag census has no integral
   rounding problem before target rows are imposed.

2. **Ring-local nesting is laminar but does not survive global target
   identification.**  In threshold variables, one slot is a chain
   \(1\ge y_{s,1}\ge\cdots\ge y_{s,H}\ge0\).  Splitting every target row
   into ring-labelled copies leaves only these chains and the
   transportation census.  The sole nonlocal operation is identifying
   copies of the same Boolean target belonging to different rings.

3. **The often-invoked uniform fractional point needs an additional
   hypothesis after frames are fixed.**  At depth \(q\), let \(D_q(T)\)
   be the number of raw ring slots displaying \(T\).  Uniform tag
   marginals give target load

   \[
   {N_q\over L}D_q(T).
   \tag{0.4}
   \]

   Hence the point is exact if and only if

   \[
   D_q(T)=L/N_q\quad\text{for every }T.
   \tag{0.5}
   \]

   This is not automatic for one fixed frame per top, and is impossible
   when \(N_q\nmid L\).  The exact uniform point in the full catalogue
   comes from averaging the frame as well as the tags.

4. **The coupled target matrix is not TU, even on actual promotion
   rings.**  For every \(H\ge4\) and \(m\) sufficiently large, one can
   fix frames on a constant fraction of all tops so that their tag-
   \(H\) root columns contain pairwise row- and column-disjoint copies of

   \[
   \begin{pmatrix}
   1&1&0\\
   1&0&1\\
   0&1&1
   \end{pmatrix}.
   \tag{0.6}
   \]

   More precisely, the number of disjoint triangles is

   \[
   \binom{2m-6}{M-4}
   =\left({1\over64}+o(1)\right)N_H,
   \tag{0.7}
   \]

   and they use

   \[
   \left({3\over64}+o(1)\right)N_H
   \tag{0.8}
   \]

   distinct top rings.  Thus odd minors occur at positive **root/ring
   density**.

5. This is not yet a coefficient-one obstruction.  The minors use only
   \(\Theta(N_H)=\Theta(W/m)\) phase columns, a \(\Theta(1/m)\) fraction
   of the \(L\asymp W\) slot columns.  Even deleting \(O(H)\) incidences
   per minor costs \(O(HN_H)=o(W)\).  A negative constant-one theorem
   would require phase-density amplification or an outside-isolation
   argument forcing \(\Omega(m)\) loss per affected ring.

The precise verdict is therefore: **TU is false, local laminarity is
real, and the currently proved odd obstruction has positive ring density
but sublinear coefficient-one cost.**

## 1. The fixed-frame tag matrix

Let \(\mathcal R\) be the \(N_H\)-element ring set and let

\[
 \mathcal S=\dot\bigcup_{R\in\mathcal R}S_R,
 \qquad |S_R|=M,
 \tag{1.1}
\]

be the phase slots.  The frame on every ring is fixed.  For a lower
depth \(q\), write

\[
 \phi_q(s)\in\binom{[n]}{m-q}
 \tag{1.2}
\]

for the forward-intersection target at slot \(s\).  Upper targets can be
included identically; the lower first three depths already contain the
obstruction below.

Use variables

\[
 x_{s,d}\quad(s\in\mathcal S, d\in\{0,\ldots,H,\bot\}),
 \tag{1.3}
\]

where \(\bot\) is a blank.  The census/root equations are

\[
 \sum_d x_{s,d}=1\quad(s\in\mathcal S),
 \tag{1.4}
\]

\[
 \sum_sx_{s,d}=\gamma_d\quad(d<H),
 \qquad
 \sum_sx_{s,\bot}=E,
 \tag{1.5}
\]

and

\[
 \sum_{s\in S_R}x_{s,H}=1\quad(R\in\mathcal R).
 \tag{1.6}
\]

The global equation \(\sum_sx_{s,H}=N_H\) is the sum of (1.6).  A tag
\(d\) activates its slot through depths \(q\le d\), so exact lower
target ownership adds

\[
 \sum_{s:\phi_q(s)=T}\sum_{d=q}^{H}x_{s,d}=1
 \quad(1\le q\le H, T\in\tbinom{[n]}{m-q}).
 \tag{1.7}
\]

For approximate coverage, the right side may be weakened and holes
charged literally.  The coefficient matrix is the same.

It is often useful to introduce thresholds

\[
 y_{s,q}:=\sum_{d=q}^{H}x_{s,d}.
 \tag{1.8}
\]

Integral tag assignments are exactly the zero-one vectors satisfying

\[
 1\ge y_{s,1}\ge y_{s,2}\ge\cdots\ge y_{s,H}\ge0,
 \tag{1.9}
\]

\[
 \sum_sy_{s,q}=N_q,
 \qquad
 \sum_{s\in S_R}y_{s,H}=1,
 \tag{1.10}
\]

and

\[
 \sum_{s:\phi_q(s)=T}y_{s,q}=1.
 \tag{1.11}
\]

The differences \(y_{s,d}-y_{s,d+1}\) recover the tag \(d\).

## 2. The TU census core

### Theorem 2.1 (rooted tag transportation is TU)

The coefficient matrix of (1.4)--(1.6), after deleting the redundant
global tag-\(H\) row, is totally unimodular.  Hence every feasible
fractional census/root assignment has an integral realization.

#### Proof

Make a bipartite graph with one vertex for every slot.  On the other
shore put one vertex for each tag \(d<H\), one blank vertex, and one
vertex \((R,H)\) for every ring.  The variable \(x_{s,d}\), for
\(d<H\) or \(d=\bot\), is the edge from slot \(s\) to the corresponding
global tag vertex.  The variable \(x_{s,H}\) is the edge from \(s\) to
\((R,H)\), where \(s\in S_R\).

After multiplying all slot rows by \(-1\), (1.4)--(1.6) is the
node--edge incidence matrix of this directed bipartite graph.  Such a
matrix is totally unimodular.  Integral right sides therefore have an
integral feasible point whenever the transportation system is feasible.
\(\square\)

The monotone ring-tag path theorem is consistent with this result.  One
may first choose the integral tag histogram of every ring and then order
its nonblank tags monotonically around the chosen cut.  This proves
census and path feasibility.  It does not preserve arbitrary target
rows (1.7), because sorting changes which phase receives each tag.

## 3. Local laminarity and the exact uniform-point audit

For a fixed ring and phase \(s\), the targets

\[
 \phi_0(s)\supset\phi_1(s)\supset\cdots\supset\phi_H(s)
 \tag{3.1}
\]

form one chain.  At any fixed proper depth, different phases of one
promotion ring give different cyclic intervals.  Thus if each global
target row is split into copies \((R,T)\), its restriction to a ring is
just a collection of phase chains.  In threshold variables, this is the
laminar order polytope (1.9), coupled only by the histogram equations
(1.10).  Every integral histogram can be realized by choosing a height
for every phase.

The nonlocal operation in (1.11) is the quotient

\[
 (R,T)\longmapsto T,
 \tag{3.2}
\]

which identifies target copies belonging to different rings.  Row
identification does not preserve total unimodularity, and Section 4
shows that it creates physical odd cycles.

There is also a necessary correction to the uniform fractional claim.
Define the raw fixed-frame degree

\[
 D_q(T):=|\{s\in\mathcal S:\phi_q(s)=T\}|.
 \tag{3.3}
\]

The uniform census point is

\[
 x_{s,d}={\gamma_d\over L}\quad(d<H),
 \qquad
 x_{s,H}={1\over M},
 \qquad
 x_{s,\bot}={E\over L}.
 \tag{3.4}
\]

It satisfies (1.4)--(1.6), since \(N_H/L=1/M\).  Its threshold is

\[
 y_{s,q}={N_q\over L}.
 \tag{3.5}
\]

Therefore its load on target \(T\) is exactly

\[
 \boxed{{N_q\over L}D_q(T).}
 \tag{3.6}
\]

### Proposition 3.1 (uniformity criterion)

After the ring frames are fixed, the uniform census point satisfies all
depth-\(q\) target equations if and only if

\[
 D_q(T)=L/N_q\quad\text{for every }T.
 \tag{3.7}
\]

The same condition is necessary even if target equality is weakened to
load at least one.

#### Proof

Equation (3.6) proves the equality statement.  For the covering
statement, the average of (3.6) over the \(N_q\) targets is one because
\(\sum_TD_q(T)=L\).  If every load is at least one, every load must
therefore equal one.  \(\square\)

In particular, \(N_q\mid L\) is necessary for exact uniformity at depth
\(q\).  The uniform fractional design obtained by averaging all cyclic
frames on every top does not imply (3.7) for an arbitrary integral
one-frame-per-top atlas.

## 4. One physical promotion-ring triangle

The following construction uses only lower depths \(1,2,3\).  Let
\(C\) be an \((m-3)\)-set, let \(c\in C\), and choose distinct
coordinates

\[
 u,v,w,a_1,a_2,a_3\notin C.
 \tag{4.1}
\]

Choose three distinct tops \(U_i\) which contain the respective middle
owners

\[
 \begin{aligned}
 X_1&=C\cup\{u,v,a_1\},\\
 X_2&=C\cup\{u,v,a_2\},\\
 X_3&=C\cup\{u,w,a_3\}.
 \end{aligned}
 \tag{4.2}
\]

Fix a cyclic frame on \(U_i\) in which \(X_i\) is one consecutive
\(m\)-window and the first three outgoing coordinates at that phase are

\[
 \begin{array}{c|ccc}
 X_1&a_1&v&c\\
 X_2&a_2&u&v\\
 X_3&a_3&w&u.
 \end{array}
 \tag{4.3}
\]

Such a frame exists: list the elements of \(X_i\) beginning with the
displayed three coordinates, then list the \(H\) elements of
\(U_i\setminus X_i\).

Let \(s_i\) be the displayed root phase.  Its first three lower erosion
targets are

\[
 \begin{array}{c|ccc}
 &\phi_1&\phi_2&\phi_3\\ \hline
 s_1&C+u+v&C+u&(C-c)+u\\
 s_2&C+u+v&C+v&C\\
 s_3&C+u+w&C+u&C.
 \end{array}
 \tag{4.4}
\]

### Theorem 4.1 (physical root-column odd minor)

In the coupled matrix (1.4)--(1.7), take the three columns

\[
 x_{s_1,H},\quad x_{s_2,H},\quad x_{s_3,H}
 \tag{4.5}
\]

and the target rows \(C+u+v\) at depth 1, \(C+u\) at depth 2, and
\(C\) at depth 3.  Their submatrix is

\[
 \boxed{
 \begin{pmatrix}
 1&1&0\\
 1&0&1\\
 0&1&1
 \end{pmatrix},}
 \tag{4.6}
\]

with determinant \(-2\).  Hence the fixed-frame coupled tag matrix is
not totally unimodular.

#### Proof

A tag \(H\) activates all three displayed depths.  Table (4.4) gives
the three incidences in (4.6).  Every column is an actual tag choice at
one phase of an actual promotion ring.  \(\square\)

Assigning weight \(1/2\) to the three displayed columns solves the three
displayed unit target equations; no zero-one assignment on those three
columns does.  Other phases may supply the same targets, so this is a
non-TU certificate, not by itself an integrality gap for the complete
system.

## 5. A positive-density family among the top rings

The preceding triangle can be realized on a constant fraction of the
top rings with mutually disjoint rows and columns.

Fix six distinct ground coordinates

\[
 a_1,a_2,a_3,u,v,w.
 \tag{5.1}
\]

Let \(\mathcal B\) be the family of all \((M-1)\)-sets \(B\) which
contain \(u,v,w\) and avoid \(a_1,a_2,a_3\).  Equivalently,

\[
 |\mathcal B|=\binom{2m-6}{M-4}.
 \tag{5.2}
\]

For \(B\in\mathcal B\), define three tops

\[
 U_i(B):=B\cup\{a_i\}\quad(i=1,2,3).
 \tag{5.3}
\]

All these tops are distinct as \((B,i)\) varies.

We next choose distinct \((m-3)\)-sets \(C_B\subseteq
B\setminus\{u,v,w\}\).  This is always possible.

### Lemma 5.1 (distinct target cores)

There is an injection

\[
 B\longmapsto C_B,
 \qquad |C_B|=m-3,
 \qquad C_B\subseteq B\setminus\{u,v,w\}.
 \tag{5.4}
\]

#### Proof

On the residual ground set of size \(2m-6\), form the inclusion graph
between the \((M-4)\)-sets and the \((m-3)\)-sets.  It is biregular.
The right shore is the central layer and has at least as many vertices as
the left shore.  If the two degrees are \(d_L,d_R\), edge counting gives

\[
 d_L|\mathcal X|\le d_R|N(\mathcal X)|
 \tag{5.5}
\]

for every left family \(\mathcal X\).  Since
\(d_L/d_R=|\mathcal C|/|\mathcal B|\ge1\), where \(\mathcal C\) is the
central right shore, Hall's condition holds.  A matching saturating
the left shore gives (5.4).  \(\square\)

Choose any \(c_B\in C_B\).  On the three tops \(U_i(B)\), use the
frames from Section 4 with \(C=C_B\).  Different \(B\)'s use distinct
top rings.  Their three selected target rows are

\[
 C_B+u+v,qquad C_B+u,qquad C_B,
 \tag{5.6}
\]

and are distinct across \(B\) because the cores \(C_B\) are distinct
and avoid \(u,v\).

### Theorem 5.2 (root-density block diagonal odd minor)

The complete fixed-frame promotion-ring matrix can contain a block
diagonal submatrix consisting of \(|\mathcal B|\) copies of (4.6).
Moreover

\[
 {3|\mathcal B|\over N_H}
 =3{(M)_4(2m-M)_2\over(2m)_6}
 ={3\over64}+o(1),
 \tag{5.7}
\]

where \((z)_j=z(z-1)\cdots(z-j+1)\).  Thus the odd minors use a positive
fraction of all top rings.

#### Proof

The tops and columns are distinct by (5.3), and the selected target rows
are distinct by (5.6).  There are also no off-block incidences.  At depth
1 the exceptional third-column target is \(C_{B'}+u+w\), which cannot
equal \(C_B+u+v\) because every core avoids \(v,w\).  At depth 2 the
exceptional second-column target \(C_{B'}+v\) cannot equal \(C_B+u\).
At depth 3 the exceptional first-column target
\((C_{B'}-c_{B'})+u\) contains \(u\), whereas every selected core
\(C_B\) avoids it.  All remaining cross incidences would force
\(C_{B'}=C_B\).  Hence the selected submatrix is genuinely block
diagonal.  The exact ratio follows from

\[
 {\binom{2m-6}{M-4}\over\binom{2m}{M}}
 ={(M)_4(2m-M)_2\over(2m)_6}.
 \tag{5.8}
\]

Since \(M/m\to1\), the last ratio tends to \(1/64\).  \(\square\)

The determinant of this block diagonal submatrix has magnitude
\(2^{|\mathcal B|}\).  Thus the failure of TU is not confined to one
exceptional top or one accidental target coincidence.

## 6. Why this is not yet a constant-one obstruction

Although Theorem 5.2 has positive ring density, it uses only three phase
columns per three rings.  Relative to all \(L=MN_H\) phase slots,

\[
 {3|\mathcal B|\over L}
 =\left({3\over64}+o(1)\right){1\over M}
 =O(1/m).
 \tag{6.1}
\]

At the calibrated promotion height,

\[
 HN_H=O(WH/m)=o(W).
 \tag{6.2}
\]

Therefore even an adversarial rule charging \(O(H)\) target incidences
for every displayed triangle would charge only \(o(W)\).  The physical
odd minors refute a TU proof, but they do not refute coefficient one.

There are now two precise possible continuations.

1. **Positive route.**  Prove that deleting or absorbing \(O(H)\) phase
   columns per ring makes the global target-identification quotient
   balanced, ideal, or otherwise integrally roundable.  The deletion
   ledger is \(O(HN_H)=o(W)\).
2. **Negative route.**  Construct \(\Omega(M)\) outside-isolated odd
   residuals per positive-density family of rings, or prove that each
   root-level triangle forces \(\Omega(M)\) unavoidable target loss.

No such amplification or near-TU theorem is proved here.

## 7. Exact verdict

Proved:

1. the root/tag census matrix is a transportation matrix and is TU;
2. all within-ring threshold structure is laminar;
3. the uniform slotwise fractional point is exact after frames are fixed
   if and only if the raw target degrees are constant;
4. the globally coupled target matrix contains an actual determinant-two
   promotion-ring minor; and
5. a constant fraction of all top rings can support mutually disjoint
   copies of that odd minor.

Not proved:

1. a phase-density \(\Omega(W)\) family of forced odd residuals;
2. an integral gap of order \(\Omega(W)\); or
3. an \(o(W)\)-loss balanced/TU core after removing the root-density
   triangles.

Thus the exact constant-one gate is no longer “is the tag matrix TU?”--it
is not.  The live question is whether its non-TU target identifications
are confined to an \(o(W)\)-repairable portion of the phase atlas.
