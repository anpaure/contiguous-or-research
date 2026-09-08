# Audit of the binary-toggle variable-weight queue and claimed monotone-rotor lift

**Date:** 2026-08-07  
**Audited source:**
`MATH_THEOREM_BINARY_TOGGLE_VARIABLE_WEIGHT_QUEUE_AND_ROTOR_LIFT_20260807.md`  
**Verdict:** **LOCAL QUEUE THEOREM PASS; FULL ROTOR-LIFT CLAIM FAILS.**
The owner, immediate-palette, suffix-target, residence, age-profile, and
regeneration statements in Theorem 2.1 are exact for arbitrary positive
phase weights.  The short-clock and ordinary long-rotor bullets of Theorem
3.1 are also correct, subject to the stated ambient-coordinate supply.
The mixed appended-rail bullet is false: a queue rotates the entire
\((d+1)\)-tuple of weights, whereas the mixed monotone rotor rotates only
its reduced mobile block and leaves the appended singleton ages terminal.
In fact a general top-rank rigidity theorem proves that no convex
combination of these queues can realize any mixed vertex.  Consequently
Corollary 3.2 and the advertised optimal-Ferrers upgrade do not follow.

## 1. Local queue setup

Put \(p=d+1\).  The source uses disjoint sets

\[
 K,\quad P_a,\quad\{x_a^0,x_a^1\}\quad(a\in\mathbb Z_p),
\]

with

\[
 |K|=R-H,\qquad |P_a|=h_a-1,\qquad
 H=\sum_a h_a,qquad h_a\ge1,
\]

and letters

\[
 A_{up+a}=K\cup P_a\cup\{x_a^u\},
 \qquad u\in\mathbb Z_2.
\tag{1.1}
\]

The literal support size is exactly

\[
 (R-H)+(H-p)+2p=R+p.
\tag{1.2}
\]

Thus every embedding into a global \(k\)-coordinate problem requires

\[
 \boxed{k\ge R+p=R+d+1.}
\tag{1.3}
\]

This condition appears in Section 1 of the source as an ambient-ground-set
assumption, but it must also be included explicitly in every global
corollary.  The old monotone rotor theorem assumes only \(k\ge R\), so the
new lift is not an all-range replacement under the old hypotheses.

## 2. Owner and immediate-palette audit

A \(p\)-window contains one letter of every phase.  Hence its rank is

\[
 (R-H)+\sum_a(h_a-1)+p=R.
\]

At endpoint \(up+a\), its phase-toggle vector is

\[
 \epsilon_b=
 \begin{cases}
 u,&b\le a,\\
 1-u,&b>a.
 \end{cases}
\tag{2.1}
\]

The \(2p\) vectors (2.1) are the two constants and the two orientations of
each nonconstant one-cut vector.  They are pairwise distinct.  Because all
phase supports are disjoint, the literal owner recovers (2.1); owner
simplicity is therefore exact for every positive weight vector, including
weights equal to one.

Moving one endpoint forward updates exactly one phase \(b\).  The lower
owner-edge colour contains neither \(x_b^0\) nor \(x_b^1\), while the upper
colour contains both.  Every other phase contributes exactly one toggle.
Thus either colour first recovers \(b\), then recovers the unchanged part
of (2.1).  The two cyclic updates of a fixed phase have complementary
unchanged toggle vectors.  Since \(p\ge2\), at least one unchanged phase
exists, so those two colours are different.  Hence both immediate palettes
are simple.  This proves Items 1--3 of Theorem 2.1.

## 3. Residence, suffix targets, and age profile

Each toggle choice is selected for exactly \(p\) consecutive owner states
and absent for the next \(p\).  Every core and \(P_a\)-coordinate belongs
to every owner.  Thus the claimed two-sided owner residence is exact.

A proper \(j\)-suffix contains precisely the nonempty proper cyclic phase
interval

\[
 a-j+1,a-j+2,\ldots,a,
\]

and has rank

\[
 R-H+\sum_{v=0}^{j-1}h_{a-v}.
\tag{3.1}
\]

Its literal set contains exactly one toggle from every included phase and
no toggle from an excluded phase.  It therefore recovers the phase
interval, hence \((a,j)\), and its toggle choices distinguish the two
binary half-periods.  This proves cross-endpoint and cross-depth target
simplicity even when two interval sums in (3.1) are numerically equal.

Finally, \(K\) occurs in the current source letter and has age zero.  The
current phase contributes its \(h_a\) phase coordinates at age zero, and
the preceding phases contribute \(h_{a-1},\ldots,h_{a-d}\) at successive
ages.  Thus

\[
 c(up+a)=(R-H+h_a,h_{a-1},\ldots,h_{a-d})
\tag{3.2}
\]

is correct, as is literal return after \(2p\) positions.  Items 4--8 of
Theorem 2.1 pass.

## 4. Which rotor lifts pass

### 4.1 Short clock

Taking \(h_0=\cdots=h_d=1\) and \(|K|=R-d-1\) makes every endpoint age
profile

\[
 (R-d,1,\ldots,1),
\]

exactly the short clock.  Marking its final \(a\) ranks realizes \(v_a\).
This bullet passes.

### 4.2 Ordinary long rotor

Let \(x=(x_0,\ldots,x_d)\) be a positive composition of \(b+1\).  Taking
\(h_i=x_i\) and \(|K|=R-b-1\) gives, over one binary half-period, the
cyclic rotations of

\[
 (R-b-1+x_0,x_1,\ldots,x_d).
\]

Averaging uniformly over all positive compositions and all phases is the
same stationary rank distribution as the long rotor.  Marking every
proper suffix realizes \((d/b)v_b\).  This bullet passes.

## 5. The mixed appended rail does not lift

Fix

\[
 1\le a<d<b\le R-1,
 \qquad D=d-a,quad L=b-a.
\]

The genuine mixed rotor uses a positive reduced composition
\((x_0,\ldots,x_D)\) of \(L+1\) and age profile

\[
 (R-b-1+x_0,x_1,\ldots,x_D,
   \underbrace{1,\ldots,1}_{a}).
\tag{5.1}
\]

Its transition rotates only the reduced block:

\[
 (x_0,x_1,\ldots,x_D,1^a)
 \longmapsto
 (x_D,x_0,\ldots,x_{D-1},1^a).
\tag{5.2}
\]

The appended singleton ages remain terminal.  In contrast, the proposed
queue sets

\[
 \mathbf h=(x_0,x_1,\ldots,x_D,1^a)
\]

and rotates the **entire** \(p\)-tuple as the endpoint phase advances.
The singleton rail consequently passes through current and intermediate
ages.  Equations (5.1)--(5.2) are not its endpoint orbit.

### Explicit smallest counterexample

Take

\[
 d=3,qquad a=1,qquad b=4,qquad R\ge5.
\]

The reduced positive compositions are the rotations of \((2,1,1)\), so
the proposed queue has full weights \((2,1,1,1)\), up to rotation, and
core rank \(R-5\).  Among its twelve nonempty proper cyclic intervals,
the sums \(1,2,3,4\) each occur exactly three times:

\[
\begin{array}{c|c}
\text{interval length}&\text{cyclic sums}\\ \hline
1&2,1,1,1\\
2&3,2,2,3\\
3&3,4,4,4.
\end{array}
\]

After normalization per endpoint, its fully marked rank vector is

\[
 \frac34v_4.
\tag{5.3}
\]

The required mixed vertex is instead

\[
 \frac{b-d}{b-a}v_a+
 \frac{d-a}{b-a}v_b
 =\frac13v_1+\frac23v_4,
\tag{5.4}
\]

whose three lower ranks have mass \(2/3\) and whose top rank has mass one.
Thus (5.3) and (5.4) differ.

## 6. General top-rank rigidity obstruction

The preceding failure is not repaired by a different convex combination
of positive-weight queues.

### Theorem 6.1

In a queue with weights \(\mathbf h=(h_0,\ldots,h_d)\), a proper suffix of
rank \(R-1\) is offered at endpoint phase \(a\) if and only if

\[
 h_{a+1}=1.
\tag{6.1}
\]

Consequently, if a convex combination of marked binary-toggle queues has
\(q_{R-1}=1\), then every queue of positive weight has

\[
 h_0=h_1=\cdots=h_d=1,
\tag{6.2}
\]

and the combination has no marked mass below rank \(R-d\).

#### Proof

An endpoint suffix has rank \(R-1\) precisely when its complementary
nonempty cyclic phase interval has total weight one.  All weights are
positive integers.  The complement must therefore be the single next
phase, and its weight must be one, proving (6.1).

At a fixed endpoint, positive weights make the proper suffix ranks strictly
increasing, so rank \(R-1\) can be marked at most once.  An averaged marked
mass equal to one forces it to be offered and marked at every endpoint of
every queue having positive mixture weight.  Equation (6.1) at all phases
then gives (6.2).  The all-unit queue offers exactly
\(R-d,R-d+1,\ldots,R-1\), proving the last statement. \(\square\)

Every mixed vertex has top coordinate one and has positive mass beginning
at rank \(R-b<R-d\).  Theorem 6.1 therefore excludes **every** mixed
vertex, not only the example in Section 5.

It also excludes the principal odd-dimensional Ferrers residual from the
queue hull.  For odd global dimension, the two central binomial
coefficients agree and the Ferrers correction is supported only in ranks
at most \(d\), so

\[
 q_{R-1}=1.
\]

For the nontrivial asymptotic range \(R-d>1\), one also has \(q_1>0\).
Theorem 6.1 makes these two conditions incompatible with a convex
combination of binary-toggle queues.

## 7. Capacity and occurrence scope

After adding (1.3), the valid short and ordinary-long queue components can
be averaged over all coordinate embeddings.  This gives uniform owner and
rank-target **fractional marginals**.  It does not give owner-disjoint or
named-target-disjoint components, and it does not provide a common
occurrence matching.  The source explicitly disclaims those integral
conclusions, so there is no further hidden one-copy claim in the local
parts that pass.

The correct strengthened statement is only:

> Subject to \(k\ge R+d+1\), the zero, short-clock, and ordinary-long
> rotor families have owner-simple binary-toggle queue lifts with simple
> local immediate palettes and exact local residence.

It is not true for the mixed vertices, hence not for all of
\(\mathcal M_{R,d}\), and not for the optimal triangular residual vector
in general.  The binary-toggle construction is a genuine partial
owner-changing lift, but it does not close the fractional trace
circulation gate claimed in Corollary 3.2.

