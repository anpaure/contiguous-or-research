# Protected reset packets leave the minimal determinant obstruction

Date: 2026-08-01

Status: unconditional residual-matrix obstruction.  Deleting the identical
root/lower/upper footprint of a complete-reversal packet or q-port macro
does not make the remaining common host system laminar, totally unimodular,
or even bimodular.  This does not prove that a common integral extension
fails; it rules out obtaining it by simply intersecting the two exact Hall
projections through a TU/laminar argument.

## 0. Setup and outcome

Let the ground set have size \(2m\), and put

\[
 {\cal L}={\Omega\choose m-1},\qquad
 {\cal X}={\Omega\choose m},\qquad
 {\cal U}={\Omega\choose m+1}.                             \tag{0.1}
\]

An unoriented diamond column is

\[
             e=(C,D;\,C+a,C+b),\qquad
             D=C+a+b.                                      \tag{0.2}
\]

An oriented column additionally orders the two middle roots as tail and
head.

Let a protected packet consume at most \(M\) distinct resources on each
of the three ranks.  Delete all those resource rows and every diamond
column incident with one of them.

Two residual obstructions survive under explicit inequalities.

1. If

   \[
                    {2m\choose m-1}>7M,                    \tag{0.3}
   \]

   the residual lower/owner/root-cap matrix contains the smallest possible
   non-TU zero-one minor, a \(3\times3\) determinant-two Johnson triangle.
2. If

   \[
                    {2m\choose m-1}>11M,                   \tag{0.4}
   \]

   the full ordered four-resource matrix contains the known \(5\times5\)
   determinant-three minor.

For the q-port resident role converter at
\(q=2(d+1)\),

\[
                              M=q(2d+2)=4(d+1)^2.           \tag{0.5}
\]

Thus the sufficient bounds become

\[
 {2m\choose m-1}>28(d+1)^2
 \quad\hbox{and}\quad
 {2m\choose m-1}>44(d+1)^2.                               \tag{0.6}
\]

Both hold overwhelmingly in the asymptotic regime.  For one
\((4d+2)\)-root complete-reversal packet, substitute \(M=4d+2\).

## 1. A residual star triangle

For \(C\in{\cal L}\) and distinct
\(a,b,c\notin C\), put

\[
 Q_a=C+a,\qquad Q_b=C+b,\qquad Q_c=C+c.                   \tag{1.1}
\]

The three diamond columns are

\[
 e_{ab}=(C,C+a+b;Q_a,Q_b),\quad
 e_{bc}=(C,C+b+c;Q_b,Q_c),\quad
 e_{ca}=(C,C+c+a;Q_c,Q_a).                               \tag{1.2}
\]

On the three combined root-capacity rows
\(Q_a,Q_b,Q_c\), these columns give

\[
 \begin{pmatrix}
 1&0&1\\
 1&1&0\\
 0&1&1
 \end{pmatrix},
 \qquad \det=2.                                           \tag{1.3}
\]

The three row supports are pairwise crossing two-sets.  In particular they
are not laminar.

### Theorem 1.1 (a protected packet cannot delete every star triangle)

Condition (0.3) guarantees a star triangle (1.2) all of whose lower,
middle-root, and owner resources avoid the protected packet.

#### Proof

The total number of star triangles is

\[
                    T={2m\choose m-1}{m+1\choose3}.        \tag{1.4}
\]

A fixed forbidden lower resource is the common \(C\) in exactly

\[
                              {m+1\choose3}                 \tag{1.5}
\]

triangles.

A fixed forbidden middle root \(Q\) occurs in

\[
                              m{m\choose2}                  \tag{1.6}
\]

star triangles: choose its common facet in \(m\) ways and the two other
extensions outside \(Q\).

A fixed forbidden owner \(U\) occurs in

\[
                          (m-1){m+1\choose2}                \tag{1.7}
\]

triangles: choose the common rank-\((m-1)\) facet of \(U\), then the third
extension outside \(U\).

Therefore at most

\[
 M\left[
 {m+1\choose3}
 +m{m\choose2}
 +(m-1){m+1\choose2}
 \right]                                                   \tag{1.8}
\]

triangles meet the protected footprint.  Dividing the bracket by
\({m+1\choose3}\) gives

\[
                1+{3(2m+1)\over m+1}<7.                   \tag{1.9}
\]

Condition (0.3) makes (1.8) strictly smaller than (1.4), so one residual
triangle survives. \(\square\)

### Corollary 1.2 (minimality)

The residual common-projection matrix is not totally unimodular.  The
obstruction is support-minimal: every one-by-one or two-by-two zero-one
matrix has determinant in \(\{-1,0,1\}\), while (1.3) has determinant two.

Thus the protected packet's highly structured deletions do not turn the
two exact marginal Hall systems into one network or laminar matrix.

## 2. The ordered determinant-three minor also survives

The ordered four-transversal matrix already has the following base gadget
on four active coordinates:

\[
\begin{array}{c|cccc}
 &L&U&T&H\\ \hline
e_1&1&134&14&13\\
e_2&3&234&34&23\\
e_3&4&234&24&34\\
e_4&4&124&14&24\\
e_5&4&134&34&14.
\end{array}                                                \tag{2.1}
\]

On rows

\[
             T_{34},\ U_{234},\ U_{134},\ L_4,\ T_{14},    \tag{2.2}
\]

its matrix is

\[
 \begin{pmatrix}
 0&1&0&0&1\\
 0&1&1&0&0\\
 1&0&0&0&1\\
 0&0&1&1&1\\
 1&0&0&1&0
 \end{pmatrix},
 \qquad \det=-3.                                           \tag{2.3}
\]

For general \(m\), adjoin one fixed \((m-2)\)-set to every resource in
(2.1).  This gives legal ranks \(m-1,m,m+1\) on \(2m\) coordinates.

The gadget uses three distinct lower resources, five distinct middle
resources, and three distinct owner resources.

### Theorem 2.1 (residual ordered torsion)

Condition (0.4) guarantees a coordinate image of (2.1) avoiding the entire
protected footprint.  Hence the residual ordered four-resource matrix is
not bimodular.

#### Proof

Choose a uniformly random coordinate permutation of one fixed lifted
copy of (2.1).  By transitivity, each one of its rank-\(s\) resources is
uniform on \({\Omega\choose s}\).  A union bound gives collision
probability at most

\[
 {3M\over {2m\choose m-1}}
 +{5M\over {2m\choose m}}
 +{3M\over {2m\choose m+1}}
 \le {11M\over {2m\choose m-1}}.                           \tag{2.4}
\]

Under (0.4), this is less than one.  Some coordinate image is therefore
completely residual, and its minor is exactly (2.3). \(\square\)

## 3. Exact implication and non-implication

The protected square theorem proves both marginal extensions for one
support-four square:

* exact lower colours with root capacity two; and
* separately, exact lower colours with injective owners.

For the full resident reversal packet, the phase-common q1-host theorem
proves the first kind of protected completion under its stated threshold;
it does not prove the second.

Theorems 1.1 and 2.1 show why these proofs still cannot simply be
intersected.  The residual correlation matrix retains its smallest odd
root circuit and a determinant-three ordered circuit even after the whole
resident packet footprint is removed.

This is not an infeasibility theorem.  The minors may be escaped by using
other residual columns, just as the finite determinant-three face can have
an integral slack-releasing escape.  The exact surviving positive target
is therefore:

\[
\boxed{
\text{a protected common ordered-diamond extension theorem
using Boolean exchanges beyond TU/laminar rounding}.
}
\]

What is closed is the proposed shortcut:

\[
\boxed{
\text{structured packet deletion does not make the common host
laminar, TU, or bimodular}.
}
\]
