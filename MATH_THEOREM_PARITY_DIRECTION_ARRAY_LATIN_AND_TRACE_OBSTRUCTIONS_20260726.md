# Parity direction arrays: exact Latin equations and trace-code obstructions

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input
is used.

## 0. Outcome

Let

\[
 E=Q_r^{\rm even},\qquad O=Q_r^{\rm odd}.
\]

The two-dimensional direction array

\[
                         d_p(x)\in[r],qquad (p,x)\in E\times Q_r,
                                                                  \tag{0.1}
\]

has an exact Latin/complete-mapping formulation.  With binary variables
\(z_{p,x,i}=\mathbf1_{\{d_p(x)=i\}}\), the three families

\[
\begin{aligned}
 \sum_i z_{p,x,i}&=1,\tag{L0}\\
 \sum_i z_{p,y\oplus e_i,i}&=1,\tag{L1}\\
 \sum_i z_{o\oplus e_i,x,i}&=1\tag{L2}
\end{aligned}
\]

say respectively that every array cell has one direction, every \(p\)-row
is a cube-neighbour permutation, and every \(x\)-column is a perfect
matching from \(E\) to \(O\).  Thus the parity complete-mapping equations
are a special three-partite assignment system, not a collection of
independent bipartite transportation problems.

The affine double-factor construction is an exact integral Latin solution.
For a coordinate permutation \(S\), an array of the form

\[
                         d_p(x)=\delta(Sp\oplus x)     \tag{0.2}
\]

satisfies (L0)--(L2) if and only if both

\[
 y\longmapsto y\oplus e_{\delta(y)},\qquad
 y\longmapsto y\oplus e_{S\delta(y)}                 \tag{0.3}
\]

are cube-neighbour permutations.  If the first is a \(C_{2r}\)-factor,
then every row is its affine translate.  This recovers the proved \(Q_4\)
double-factor seed.

There are, however, two exact trace obstructions.

1. **Universal half-depth cut.**  At aligned coarse depth \(d=r/2\), the
   trace code has at most

   \[
                  \binom r{r/2}2^r
   \]

   values for \(2^{2r-1}\) even-time starts.  Hence its collision excess is

   \[
   \boxed{
     2^{2r-1}-\binom r{r/2}2^r
     =\left(1-O(r^{-1/2})\right)2^{2r-1}.}            \tag{0.4}
   \]

   For the finite seed \(r=4,d=2\), at most \(96\) codes serve \(128\)
   aligned starts, so at least \(32\) collisions are forced.  No choice of
   direction array, including a nonaffine one, removes this cut.

2. **Affine symmetry orbit.**  For (0.2), a start with completed direction
   set \(J\) has trace multiplicity at least

   \[
   \boxed{
    2^{\max\{|J\cap S^{-1}J|-1,0\}}.}                \tag{0.5}
   \]

   Therefore suspending the \(Q_4\) seed while allowing \(S=(2\ 4)\) to
   fix almost every new direction retains exponential trace collisions.
   A successful growing affine construction must arrange
   \(|J\cap S^{-1}J|\le1\) for almost every protected window, in addition
   to constructing the same-vertex double factor (0.3).

The universal cut (0.4) closes any demand for trace near-injectivity all the
way to half depth.  It does not close the intended regime \(H=o(r)\).  In
that shallow regime the precise remaining finite theorem is a growing
double factor \((G_0,G_1,S)\) whose protected direction windows are nearly
disjoint from their \(S\)-images, followed by a proof that the remaining
nonsymmetry collisions are \(o(2^{2r})\).  A bounded seed plus ordinary
fixed-direction suspension cannot satisfy this condition.

## 1. Exact local Latin equations

For every \((p,x,i)\in E\times Q_r\times[r]\), introduce

\[
                         z_{p,x,i}\in\{0,1\}.          \tag{1.1}
\]

Define

\[
 F_p(x)=x\oplus e_{d_p(x)},\qquad
 T_x(p)=p\oplus e_{d_p(x)}.                           \tag{1.2}
\]

### Theorem 1.1 (three-index complete-mapping equations)

The array \(d_p(x)\) makes every \(F_p\) a cube-neighbour permutation and
every \(T_x:E\to O\) a bijection if and only if its indicator variables
satisfy (L0)--(L2), namely

\[
\begin{aligned}
 \sum_{i=1}^r z_{p,x,i}&=1
                              &&(p\in E,\ x\in Q_r),\tag{1.3}\\
 \sum_{i=1}^r z_{p,y\oplus e_i,i}&=1
                              &&(p\in E,\ y\in Q_r),\tag{1.4}\\
 \sum_{i=1}^r z_{o\oplus e_i,x,i}&=1
                              &&(o\in O,\ x\in Q_r).\tag{1.5}
\end{aligned}
\]

#### Proof

Equation (1.3) selects one outgoing cube edge at every array cell.  The
possible predecessors of \(y\) under \(F_p\) are \(y\oplus e_i\), and the
edge from that predecessor reaches \(y\) precisely when its selected label
is \(i\).  Thus (1.4) is exactly the unique-predecessor equation for the
row permutation.

Similarly, the possible even predecessors of \(o\in O\) under \(T_x\) are
\(o\oplus e_i\).  Equation (1.5) says that exactly one of them selects its
edge toward \(o\).  Since \(|E|=|O|\), this is exactly column bijectivity.
\(\square\)

Each variable in (1.3)--(1.5) belongs to one constraint of each family.
Thus the matrix is a special three-uniform, three-partite incidence matrix.
The separate row equations (1.3)--(1.4) are bipartite matching matrices,
and so are the separate column equations (1.3)--(1.5), but their common
refinement is not obtained by a two-dimensional transportation argument.
No total-unimodularity conclusion follows from the two separate projections.

There is always the context-independent integral solution
\(d_p(x)=d(x)\) whenever \(x\mapsto x\oplus e_{d(x)}\) is a neighbour
permutation.  It proves that (1.3)--(1.5) themselves are not the difficult
existence gate.  Its traces have the exponential erased-parity collisions
already proved in the paired-order lift theorem.

## 2. Adding the \(C_{2r}\)-row condition

Equations (1.3)--(1.5) impose permutation rows, but not the required cycle
length and isometry.  Let \(\mathscr C_r\) be the set of oriented physical
isometric \(C_{2r}\)'s in \(Q_r\).  A literal component formulation uses
variables \(u_{p,C}\in\{0,1\}\) and equations

\[
                         \sum_{C\ni x}u_{p,C}=1
                         \qquad(p\in E,\ x\in Q_r).   \tag{2.1}
\]

If \(d_C(x)\) is the outgoing direction of \(C\) at \(x\), the column
complete-mapping equations become

\[
 \sum_{\substack{p,C:\ x\in C,\\
                  p\oplus e_{d_C(x)}=o}}
       u_{p,C}=1
                     \qquad(o\in O,\ x\in Q_r).      \tag{2.2}
\]

Equations (2.1)--(2.2) are the exact whole-component set-partitioning model.
They prevent a fractional solution from choosing directions ownerwise and
then silently assembling incompatible row cycles.

Every row factor contains \(2^r/(2r)\) cycles.  Each cycle uses every
direction twice, so every direction occurs exactly \(2^r/r\) times in one
row.  In particular,

\[
                              r\mid2^r,                \tag{2.3}

\]

and hence a necessary arithmetic condition is that \(r\) be a power of
two.  This is satisfied in the recursive application.

The component columns in (2.1)--(2.2) carry an entire cyclic direction
word and all of its trace codes.  They are not network arcs.  Thus even a
future proof that the local degree matrix (1.3)--(1.5) is integral would
not round the required whole-cycle problem.

## 3. Exact affine Latin construction

Let \(S\in S_r\) permute the coordinate directions, and let
\(\delta:Q_r\to[r]\).  Put

\[
 G_0(y)=y\oplus e_{\delta(y)},\qquad
 G_1(y)=y\oplus e_{S\delta(y)}.                       \tag{3.1}
\]

For \(p\in E\), define

\[
 d_p(x)=\delta(Sp\oplus x),\qquad
 F_p(x)=x\oplus e_{d_p(x)}.                           \tag{3.2}
\]

### Theorem 3.1 (affine complete-mapping equivalence)

The array (3.2) satisfies (1.3)--(1.5) if and only if \(G_0\) and \(G_1\)
are both neighbour permutations of \(Q_r\).  If \(G_0\) is a physical
\(C_{2r}\)-factor, every row \(F_p\) is an affine conjugate of it and is
the same kind of factor.

#### Proof

For fixed \(p\), the change of variables \(y=Sp\oplus x\) gives

\[
                         Sp\oplus F_p(x)=G_0(y).       \tag{3.3}
\]

Thus every row is a permutation exactly when \(G_0\) is.

For fixed \(x\), the same change of variables gives

\[
                         ST_x(p)\oplus x=G_1(y).       \tag{3.4}
\]

The affine map \(p\mapsto Sp\oplus x\) sends the even shore bijectively to
one parity shore, while a neighbour permutation sends that shore to the
other.  Hence \(T_x\) is bijective exactly when \(G_1\) is.  Equation
(3.3) also preserves the complete row-cycle structure. \(\square\)

This is a literal complete-mapping construction, not a fractional
rounding.  The common-phase \(Q_4\) pair has \(S=(2\ 4)\) and supplies the
first nonconstant instance.

## 4. Affine trace-orbit obstruction

For an aligned coarse window of length \(d\) starting at \((p,x)\), put

\[
 J=J_{p,d}(x)
 =\{d_p(x),d_p(F_px),\ldots,d_p(F_p^{d-1}x)\}.         \tag{4.1}
\]

The physical trace code is

\[
                         \mathcal C_d(p,x)
  =\bigl(J,x|_{J^c},p|_{J^c}\bigr).                  \tag{4.2}
\]

### Theorem 4.1 (affine symmetry orbit)

For the affine array (3.2), every code fibre containing \((p,x)\) has size
at least

\[
                  2^{\max\{|J\cap S^{-1}J|-1,0\}}.   \tag{4.3}
\]

#### Proof

Put

\[
                         K=J\cap S^{-1}J.             \tag{4.4}
\]

Let \(a\) be any even vector supported on \(K\), and define

\[
                         p'=p\oplus a,\qquad
                         x'=x\oplus Sa.               \tag{4.5}
\]

Then \(p'\) is even and

\[
 Sp'\oplus x'=Sp\oplus Sa\oplus x\oplus Sa
              =Sp\oplus x.                           \tag{4.6}
\]

Hence the entire row trajectory in the \(y\)-coordinate, and in particular
its direction set \(J\), is unchanged.  Since \(a\) is supported on \(J\),
we have \(p'|_{J^c}=p|_{J^c}\).  Since \(a\) is supported on
\(S^{-1}J\), the vector \(Sa\) is supported on \(J\), so also
\(x'|_{J^c}=x|_{J^c}\).  Thus all pairs in (4.5) have the same code.

There are \(2^{|K|-1}\) even vectors supported on \(K\) when \(|K|\ge1\),
and one when \(K=0\).  This proves (4.3). \(\square\)

### Corollary 4.2 (bounded-seed suspension fails)

If \(S\) moves at most \(s\) coordinates, then every \(d\)-window has

\[
                         |J\cap S^{-1}J|\ge d-s.      \tag{4.7}
\]

Hence its affine trace multiplicity is at least

\[
                         2^{\max\{d-s-1,0\}}.         \tag{4.8}
\]

In particular, extending the \(Q_4\) solution while keeping
\(S=(2\ 4)\) on the seed and fixing all fresh directions has exponential
collision multiplicity as soon as \(d\to\infty\).

#### Proof

Every fixed point of \(S\) which belongs to \(J\) also belongs to
\(S^{-1}J\).  At most \(s\) members of \(J\) are moved.  Apply Theorem
4.1. \(\square\)

Thus the affine construction can work only with a genuinely growing
coordinate permutation.  A necessary symmetry condition for near
injectivity is

\[
 \bigl|\{(p,x):|J_{p,d}(x)\cap S^{-1}J_{p,d}(x)|\ge2\}\bigr|
                              =o(2^{2r})              \tag{4.9}
\]

at every protected depth.  A half-rotation of a cyclic direction order
would make every interval \(J\) of length \(d<r/2\) disjoint from its
image, showing that (4.9) is combinatorially possible.  What is not known
is a same-vertex double factor (3.1) realizing that permutation.

## 5. Universal trace-code capacity cut

The affine symmetry is not the only obstruction.  Independently of how the
array is constructed, an aligned depth-\(d\) code has the form (4.2), with
\(|J|=d\).  This code is an exact representation of either signed physical
trace: completed pairs in \(J\) are respectively empty or full, while on
\(J^c\) the two physical bits are recovered from \((x_i,p_i)\).  Therefore
the complete trace-code universe has size at most

\[
                         M_{r,d}=\binom rd2^{2(r-d)}.  \tag{5.1}

\]

There are

\[
                         A_r=|E|\,|Q_r|=2^{2r-1}      \tag{5.2}

\]

aligned even-time starts.

### Theorem 5.1 (trace-code Hall cut)

For every direction array satisfying the complete-mapping and row-cycle
conditions, the total aligned trace collision excess at coarse depth \(d\)
is at least

\[
 \boxed{
                         (A_r-M_{r,d})_+.}             \tag{5.3}

\]

The same bound holds separately for lower and upper physical traces.

#### Proof

For a code value \(c\), let \(n_c\) be the number of aligned starts which
produce it.  Then

\[
 \sum_c(n_c-1)_+=A_r-|\{c:n_c>0\}|.                 \tag{5.4}
\]

The number of used codes is at most the size (5.1) of the complete code
universe.  This gives (5.3).  The lower and upper traces determine the same
data (4.2) on completed pairs, so the count applies to both signs.
\(\square\)

This is a genuine Hall cut because trace injectivity asks for a matching of
aligned starts to distinct code slots.  It is not the retracted inference
from unequal lower and upper target shores in an edge-cover problem.

At \(d=r/2\), Stirling's formula gives

\[
 {M_{r,r/2}\over A_r}
 ={2\binom r{r/2}\over2^r}
 =2\sqrt{\frac{2}{\pi r}}\,(1+o(1)),                 \tag{5.5}

\]

which proves (0.4).  At \(r=4,d=2\),

\[
                         A_4=128,\qquad M_{4,2}=6\cdot16=96, \tag{5.6}

\]

so the finite Hall lower bound is \(32\).

For \(d=o(r)\), the ratio

\[
                         {M_{r,d}\over A_r}
 ={2\binom rd\over4^d}                               \tag{5.7}

\]

is generally much larger than one, and (5.3) is silent.  Hence the
universal counting cut does not rule out the protected shallow-depth
regime.

## 6. Exact surviving construction gate

The ownership part now has two exact formulations:

* the general Latin equations (1.3)--(1.5), with whole cycles enforced by
  (2.1)--(2.2); and
* the affine complete-mapping construction (3.1)--(3.2).

The \(Q_4\) seed proves that nonconstant integral solutions exist, but
Theorem 5.1 proves that this finite seed is not a trace-near-injective cell
at its half depth.  Theorem 4.1 proves that a bounded-support suspension of
its permutation \(S\) is exponentially worse at growing depths.

For \(H=o(r)\), the sharpest surviving positive theorem is therefore:

> Construct a growing same-vertex double factor \((G_0,G_1,S_r)\) such
> that both factors are physical \(C_{2r}\)-factors and, for every
> \(d\le H/2\), all but \(o(2^{2r})\) starts have
> \(J\cap S_r^{-1}J\) of size at most one; then prove that collisions not
> generated by the symmetry orbit are also \(o(2^{2r})\).

A cyclic half-rotation has the desired window geometry, but no compatible
double factor is known.  Conversely, the current \(Q_4\) transposition has
the compatible double factor but not the growing window geometry.  This is
the precise finite construction gap; ownerwise or ordinary TU rounding of
the direction entries does not address it.
