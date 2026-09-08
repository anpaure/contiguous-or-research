# Lane N: cross-level PBBS trace budgets and the harmonic terminal-block escape

Date: 2026-07-25

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Audited correction and outcome

Put

\[
N=2r+1,
\qquad
B_r=\operatorname{Cat}_r.
\]

The proposed implication

\[
d(D)=1
\quad\Longrightarrow\quad
\text{next omitted-label gap }2\operatorname{ht}(D)+1
\]

is false, including on primitive roots. Consequently the claimed
Catalan-density disproof of \((\mathrm{RP}_A)\), and every conclusion that
global phase fusion is forced by that disproof, are retracted. None of the
results below uses that implication or the false static sector transport.

This report resumes from the audited peak-deletion chronology. It proves two
exact limitations of the currently available Pascal/trace method.

1. At every pruning level, transported descendant traces have total capacity
   at most \(B_r\). Therefore every nonnegative scalar combination of these
   levelwise trace-volume inequalities can yield at best the scale

   \[
   \boxed{B_r/H.}
   \]

   In the Gaussian window \(H=\Theta_A(\sqrt r)\), the current
   coefficient-one gate \((\mathrm{CP}_A)\) and the stronger
   \((\mathrm{RP}_A)\) share the quotient scale
   \(B_r/N=\Theta_A(B_r/H^2)\), with big-oh and little-oh respectively.
   Thus the whole additive level-volume cone misses one factor \(H\).

2. On an exact integral harmonic pruning profile, requiring a terminal block
   of uniformly bounded size to be identically zero at every level retains a
   positive fraction of the entire inverse fibre. If the block sizes are
   \(b_n\), obtaining even a factor \(1/R\) from zero-block constraints
   requires

   \[
   \boxed{
   \sum_n\frac{b_n}{(n+2)(n+4)}\ge\frac12\log R.
   }
   \]

   Current chronology proves only \(2\le b_n\le g_n+1\) and does not imply
   this growth. By contrast, a positive prescribed block mass \(s\ge1\) at
   depth \(n\) costs \(O_{b,s}(n^{-2s})\).

An explicit abstract capacitated trace system realizes the residual
\(\Theta(B/H)\) scale while satisfying the displayed scalar rank, slot,
zero-block, trace-capacity, and formal strict-gap-descent constraints. It
does not realize an actual PBBS fibre map or endpoint genealogy and is not
a counterexample to the theorem. Its role is to prove that an additional
PBBS-specific cross-level restriction is logically indispensable.

The exact surviving alternatives are:

* force the weighted terminal-block growth above;
* force positive terminal-block mass sufficiently deep or sufficiently
  often; or
* prove a genuinely cross-level non-reuse/decorrelation theorem for actual
  PBBS traces.

Global literal fusion remains a possible fallback, not a consequence of a
disproved residence lower bound.

## 1. Retraction certificate

A primitive counterexample is

\[
D_0=1110011000.
\]

It has semilength five, height three, and \(d(D_0)=1\). Under the exact
two-step map

\[
\tau(P1R0S)=S1P0R
\]

one obtains

\[
\begin{aligned}
D_0&=1110011000,\\
D_1&=1110001100,\\
D_2&=1100111000,\\
D_3&=D_0.
\end{aligned}
\]

Their canonical first-maximum data are

\[
\begin{array}{c|ccc}
 &D_0&D_1&D_2\\ \hline
d(D_j)&1&5&1\\
\delta(D_j)&3&3&7.
\end{array}
\]

At the claimed step-two time \(s=3=\operatorname{ht}(D_0)\), the return
equation would require

\[
d(D_0)+d(D_1)+d(D_2)=\delta(D_3).
\]

Instead

\[
1+5+1=7,\qquad \delta(D_3)=3,\qquad
7\not\equiv3\pmod {11}.
\]

The failure mechanism is exact: a transported off-spine forest can enter a
positive-depth pre-spine sector and become first deepest. Relative height
below the old maximum at the root seam does not prevent this later
overtaking. Thus neither the sector recursion nor the proposed
Catalan-positive return family is available.

## 2. Exact transported trace capacities at every pruning level

Let

\[
\Omega_r=\mathcal D_r
\]

be the directed step-two quotient-edge set. Thus \(|\Omega_r|=B_r\).
Let \(\mathcal P\) be any pairwise quotient-edge-disjoint family of
nonwrapping PBBS residence intervals of residence at most \(H\).

For \(I\in\mathcal P\), repeatedly peak-delete its canonical first-repeat
trace. Let \(J_j(I)\) be the resulting \(j\)-times-pruned trace for as long
as its return gap is below the current circumference; after that point put

\[
J_j(I)=\varnothing.
\]

The reduced trace is allowed to traverse one reduced edge more than once.
All multiplicities below are occurrence multiplicities.

For a reduced quotient edge \(e\), define the exact \(j\)-fold fibre
capacity

\[
F_j(e)=\#\{D\in\mathcal D_r:\partial^jD=e\}.
\]

The ranks of the possible \(e\)'s vary, so the range is the disjoint union
of all lower Dyck quotient-edge sets, together with a cemetery state after
the pruning has exhausted a root.  Thus every top edge has exactly one
\(j\)-fold image, and fibre partition gives

\[
\boxed{
\sum_eF_j(e)=B_r.
}
\tag{2.1}
\]

For a trace \(J\), write \(m_e(J)\) for the number of traversals of \(e\).

### Theorem 2.1 (levelwise transported-fibre capacity)

For every pruning level \(j\ge0\) and every reduced edge \(e\),

\[
\boxed{
L_{j,e}:=
\sum_{I\in\mathcal P}m_e(J_j(I))
\le F_j(e).
}
\tag{2.2}
\]

Consequently

\[
\boxed{
\sum_{I\in\mathcal P}|J_j(I)|
=\sum_eL_{j,e}
\le B_r.
}
\tag{2.3}
\]

#### Proof

Peak deletion semiconjugates the step-two PBBS quotient. Every occurrence
of \(e\) in \(J_j(I)\) is therefore the image of a specified top-level
edge occurrence in the original trace \(I\). Even if the reduced trace
wraps a short reduced cycle and revisits \(e\), distinct occurrences come
from distinct top-level trace positions.

The original intervals are pairwise top-edge-disjoint. Hence all top edges
which project to the displayed occurrences of \(e\), over the whole family,
are distinct members of the fibre \((\partial^j)^{-1}(e)\). There are
exactly \(F_j(e)\) such edges, proving (2.2). Summing first over \(e\), and
then using (2.1), proves (2.3). \(\square\)

No independence between different levels is asserted. The same top edge
may support one descendant occurrence at many successive pruning levels.
That reuse is precisely the obstruction below.

## 3. The additive trace-volume ceiling

Let \((w_j)_{j\ge0}\) be arbitrary nonnegative real weights with finite
support, and define the weighted descendant trace volume of \(I\) by

\[
Q_w(I)=\sum_jw_j|J_j(I)|.
\tag{3.1}
\]

### Theorem 3.1 (all nonnegative level-volume combinations stop at \(B_r/H\))

For every such weight sequence,

\[
\boxed{
\sum_{I\in\mathcal P}Q_w(I)
\le B_r\sum_jw_j.
}
\tag{3.2}
\]

Every descendant residence remains at most \(H\), and hence

\[
\boxed{
Q_w(I)\le(H+1)\sum_jw_j
\qquad(I\in\mathcal P).
}
\tag{3.3}
\]

It follows that a cardinality proof which uses only a common lower bound on
\(Q_w(I)\) and the levelwise budgets (2.3) cannot have a universal scale
better than

\[
\boxed{B_r/(H+1).}
\tag{3.4}
\]

#### Proof

Multiply (2.3) by \(w_j\), sum over \(j\), and interchange the two finite
nonnegative sums. This gives (3.2).

Peak deletion strictly shortens every surviving same-label return by at
least two ordinary PBBS steps, so in particular it never increases its
residence. A residence-\(H\) return has a step-two trace of at most \(H+1\)
edges. Therefore \(|J_j(I)|\le H+1\) for every \(j\), proving (3.3).

Suppose this proof template establishes \(Q_w(I)\ge q_w\) for every
selected interval. Then (3.2) gives

\[
|\mathcal P|\le\frac{B_r\sum_jw_j}{q_w}.
\]

But the quantity being lower-bounded itself obeys (3.3), so necessarily

\[
q_w\le(H+1)\sum_jw_j.
\]

The smallest possible right side obtainable from this template is
therefore no smaller than \(B_r/(H+1)\), proving (3.4). \(\square\)

The theorem concerns scalar nonnegative combinations of the levelwise
total-volume inequalities. It does not rule out edge-dependent dual
weights which exploit actual PBBS passage locations, signed or nonlinear
cross-level energies, or an injective non-reuse theorem.

### Corollary 3.2 (Gaussian factor loss for the CP and RP targets)

For fixed \(A>0\) and

\[
H=\lceil A\sqrt r\rceil,
\]

one has

\[
N=\Theta_A(H^2).
\]

The audited dominance-staircase seam reduces coefficient one to the
Catalan-order packing gate

\[
(\mathrm{CP}_A):
\qquad
\overline\nu_H=O_A(B_r/N)
=O_A(B_r/H^2).
\]

The stronger exact quotient formulation of \((\mathrm{RP}_A)\) asks for

\[
\overline\nu_H=o_A(B_r/N)
=o_A(B_r/H^2).
\]

The ceiling (3.4) is larger than the common \(B_r/N\) scale of both gates
by a factor \(\Theta_A(H)\).  Thus nonnegative scalar level-volume
combinations alone cannot establish the current coefficient-one input
\((\mathrm{CP}_A)\), still less \((\mathrm{RP}_A)\).

### Corollary 3.3 (the formal trace-area envelope has the same ceiling)

In the formal slowest allowed strict gap descent through positive return
gaps, put

\[
g_j=2H-1-2j,
\qquad 0\le j\le H-2.
\]

The descendant step-two trace lengths are

\[
\ell_j=\frac{g_j+3}{2}=H+1-j.
\]

Thus one parent interval has total descendant trace area

\[
\boxed{
\sum_{j=0}^{H-2}\ell_j
=\frac{(H-1)(H+4)}2
=\Theta(H^2).
}
\tag{3.5}
\]

However, summing (2.3) over these \(H-1\) levels gives total capacity

\[
(H-1)B_r=\Theta(HB_r).
\]

Dividing by (3.5) again gives only \(\Theta(B_r/H)\).  The endpoint
\(g_{H-2}=3\) is used here only as the rank-one envelope; no claim is made
that every actual PBBS genealogy realizes the entire displayed sequence.
The apparent quadratic area is paid from \(H\) separate copies of the same
top capacity,
not from one cross-level disjoint budget.

## 4. Exact harmonic terminal-block probabilities

The next theorem isolates the independent Pascal obstruction. Fix an
integer \(L\ge1\). Choose \(R\) to be a sufficiently large multiple of
\((L+4)!\), and put, for \(0\le j\le L+2\),

\[
r_j=\frac{R}{j+1}.
\tag{4.1}
\]

These ranks, and all free masses below, are integral through the required
levels.  They occur in nonempty actual plane-tree inverse fibres.  Indeed,
choose a bottom Dyck root of rank \(r_{L+1}\) having exactly
\[
r_{L+1}-r_{L+2}
=\frac{R}{(L+2)(L+3)}
\]
peaks; a Dyck root of rank \(u\) exists with every prescribed peak count
between \(1\) and \(u\).  Each successive inverse fibre is nonempty because
its free mass is the positive integer displayed in (4.3).  Thus the
profile is not merely a real-variable saddle calculation.

For \(0\le n<L\), consider the inverse step which reconstructs the
rank-\(r_{n+1}\) tree from its rank-\(r_{n+2}\) core. The number of ordered
child slots and the free leaf mass are

\[
\boxed{
p_n=2r_{n+2}+1=\frac{2R}{n+3}+1,
}
\tag{4.2}
\]

and

\[
\boxed{
y_n=r_{n+1}-2r_{n+2}+r_{n+3}
=\frac{2R}{(n+2)(n+3)(n+4)}.
}
\tag{4.3}
\]

Write

\[
a_n=p_n-1=\frac{2R}{n+3},
\qquad
\alpha_n=\frac{y_n}{a_n}
=\frac1{(n+2)(n+4)}.
\tag{4.4}
\]

The unrestricted inverse fibre is the weak-composition simplex of \(y_n\)
objects in \(p_n\) slots, of size

\[
F_n=\binom{y_n+p_n-1}{p_n-1}.
\tag{4.5}
\]

### Theorem 4.1 (zero terminal-block retention)

Suppose a specified terminal block of \(b_n\) slots is required to have
total zero. Its exact retained fraction is

\[
\boxed{
\rho_n(b_n)
=\frac{\binom{y_n+p_n-b_n-1}{p_n-b_n-1}}
       {\binom{y_n+p_n-1}{p_n-1}}
=\prod_{i=0}^{b_n-1}
  \frac{a_n-i}{a_n+y_n-i}.
}
\tag{4.6}
\]

If

\[
1\le b_n\le a_n/2,
\]

then

\[
\boxed{
\exp(-2b_n\alpha_n)
\le\rho_n(b_n)
\le
\exp\!\left(-\frac{b_n\alpha_n}{1+\alpha_n}\right).
}
\tag{4.7}
\]

#### Proof

For total zero, every slot in the specified block is zero. The remaining
\(y_n\) objects are distributed among \(p_n-b_n\) slots, giving the first
ratio in (4.6). Direct cancellation of factorials gives the product.

Put

\[
x_i=\frac{y_n}{a_n-i}.
\]

Then

\[
-\log\rho_n(b_n)=\sum_{i=0}^{b_n-1}\log(1+x_i).
\]

Since \(b_n\le a_n/2\), one has \(x_i\le2\alpha_n\). The inequality
\(\log(1+x)\le x\) gives

\[
-\log\rho_n(b_n)\le2b_n\alpha_n,
\]

which is the lower bound in (4.7).

For the other direction,

\[
\log(1+x_i)
\ge\frac{x_i}{1+x_i}
=\frac{y_n}{a_n+y_n-i}
\ge\frac{\alpha_n}{1+\alpha_n}.
\]

Sum over \(i\) and exponentiate. \(\square\)

### Corollary 4.2 (bounded blocks retain positive mass)

For any sequence \((b_n)_{0\le n<L}\) in the range of Theorem 4.1,

\[
\boxed{
\prod_{n=0}^{L-1}\rho_n(b_n)
\ge
\exp\!\left[
-2\sum_{n=0}^{L-1}
\frac{b_n}{(n+2)(n+4)}
\right].
}
\tag{4.8}
\]

Conditional on the rank string, successive inverse choices form Cartesian
fibres and their level factors depend only on the displayed ranks.
Therefore the product in (4.8) is the retained fraction of the full
finite tower fibre, not an independence heuristic.

Since

\[
\sum_{n=0}^{\infty}\frac1{(n+2)(n+4)}
=\frac12\sum_{n=0}^{\infty}
 \left(\frac1{n+2}-\frac1{n+4}\right)
=\frac5{12},
\tag{4.9}
\]

the uniform bound \(b_n\le b_*\) gives

\[
\boxed{
\prod_{n=0}^{L-1}\rho_n(b_n)
\ge e^{-5b_*/6}>0.
}
\tag{4.10}
\]

For the smallest block size currently forced by the two-child chronology,
\(b_n=2\), the lower bound is \(e^{-5/3}\), uniformly in \(L\) and \(R\).

Conversely, if zero-block constraints alone produce a retained fraction at
most \(R^{-1}\), then (4.8) necessarily gives

\[
\boxed{
\sum_{n=0}^{L-1}
\frac{b_n}{(n+2)(n+4)}
\ge\frac12\log R.
}
\tag{4.11}
\]

The exact terminal-block chronology currently supplies only

\[
2\le b_n\le g_n+1.
\]

It supplies no lower bound of the form (4.11).

## 5. Positive terminal-block mass

At the same inverse step, suppose a terminal block has
\(2\le b\le p_n-1\) slots,
total prescribed free mass \(s\), and its distinguished seam slot is fixed
to \(z\), where

\[
0\le z\le s\le y_n.
\]

The first condition distributes \(s-z\) objects among the other \(b-1\)
block slots. The remaining \(y_n-s\) objects lie outside the block.

### Theorem 5.1 (exact terminal-block slot-vector count)

The exact number of compatible inverse slot vectors is

\[
\boxed{
K_n^{(2)}(b,s,z)
=
\binom{s-z+b-2}{b-2}
\binom{y_n-s+p_n-b-1}{p_n-b-1}.
}
\tag{5.1}
\]

If \(b+s\le p_n/2\), then

\[
\boxed{
\frac{K_n^{(2)}(b,s,z)}{F_n}
\le
\binom{s+b-1}{s}
\left(2\alpha_n\right)^s
=
\binom{s+b-1}{s}
\left(\frac{2}{(n+2)(n+4)}\right)^s.
}
\tag{5.2}
\]

#### Proof

The two independent stars-and-bars choices give (5.1).

Forget the seam coordinate; this only enlarges the admissible block family.
The probability that an unrestricted weak composition gives total block
mass \(s\), divided by the probability of total block mass zero, is

\[
\binom{s+b-1}{s}
\frac{(y_n)_{\underline{s}}}
     {(y_n+p_n-b-1)_{\underline{s}}}.
\tag{5.3}
\]

Under \(b+s\le p_n/2\), every denominator factor is at least \(p_n/2\),
whereas every numerator factor is at most \(y_n\). Hence (5.3) is at most

\[
\binom{s+b-1}{s}
\left(\frac{2y_n}{p_n}\right)^s
\le
\binom{s+b-1}{s}(2\alpha_n)^s.
\]

Finally the zero-block probability is at most one. This proves (5.2).
\(\square\)

For fixed \(b\) and \(s\ge1\), (5.2) is

\[
O_{b,s}(n^{-2s}).
\]

This statement is in the range \(b+s\le p_n/2\) and \(s\le y_n\), which
holds at any fixed displayed depth after choosing the integral scale \(R\)
sufficiently large.  The theorem is an exact count of slot vectors
satisfying the displayed block equations.  It is necessary algebra for a
two-child PBBS passage, not a sufficiency theorem for dynamic passage
compatibility.

Thus positive block mass at a sufficiently deep valid level is genuinely
contractive. The algebraic escape is specifically

\[
b_n=O(1),
\qquad s_n=z_n=0
\]

through many levels.

## 6. A sharp abstract countermodel for the recorded scalar axioms

This section is a logical scope certificate, not a PBBS construction.

Fix \(H\ge2\) and a finite integral harmonic tower with at least \(H-1\)
displayed inverse levels. Let \(F\) be its unrestricted tower-fibre size
and let \(K\) be the exact number of tower slot vectors for which one
designated two-slot terminal block is zero at every displayed level.
Corollary 4.2 gives

\[
K/F\ge e^{-5/3}.
\tag{6.1}
\]

Choose a directed cycle \(C_Q\), with \(Q>H+1\) divisible by \(H+1\)
(for example \(Q=2(H+1)\)), and take \(F\) disjoint lane lifts of it as an
abstract top edge system. Project every lane identically to \(C_Q\) at
every pruning level while transporting its slot vector bijectively. Retain
the \(K\) admissible lanes.

In each retained lane, select the

\[
Q/(H+1)
\]

disjoint intervals of length \(H+1\) beginning at multiples of \(H+1\).
For \(0\le j\le H-2\), declare the nested descendant trace to be the
initial length-\((H+1-j)\) subinterval, and declare it empty thereafter.

Then:

* the top intervals are edge-disjoint;
* every level-edge load is at most \(K\le F\);
* all levelwise transported-fibre capacities hold;
* the positive trace lengths decrease strictly by one, formally
  corresponding to ordinary gap decrease by two through the gap-three
  envelope;
* the exact harmonic rank and zero-block Pascal counts hold in the
  independent tower coordinate; and
* the family size is

  \[
  \boxed{
  \frac{KQ}{H+1}
  \ge e^{-5/3}\frac{FQ}{H+1}
  =\Theta(B_{\rm abs}/H),
  }
  \tag{6.2}
  \]

  where \(B_{\rm abs}=FQ\) is the abstract top edge mass.

Thus the displayed scalar capacity, rank, slot, and formal descent axioms
used in Sections 2--5 admit the \(B/H\) extremal scale. They cannot
logically imply \(O(B/H^2)\).

No claim is made that the declared traces form a PBBS orbit, an actual
inverse-fibre map, or a full two-child endpoint genealogy. Excluding this
countermodel therefore requires an additional PBBS-specific dynamical
restriction; the model is not a counterexample to any PBBS packing
statement.

## 7. Precise proved and conditional boundary

### Proved for actual PBBS packings

1. The levelwise capacities (2.2)--(2.3), including reduced traces with
   repeated edge occurrences.
2. The weighted total inequality (3.2).
3. The \(B_r/H\) ceiling for every proof using only nonnegative scalar
   combinations of levelwise trace volumes.
4. The formal slow-descent trace-area arithmetic (3.5), with no assertion
   that an actual PBBS genealogy realizes the full envelope.

### Proved for exact integral Pascal fibres

1. The harmonic slot/free-mass formulas (4.2)--(4.4).
2. The exact zero-block fraction (4.6) and both constants in (4.7).
3. Positive limiting retention for bounded block sizes, including the
   explicit \(e^{-5/3}\) lower bound for two-slot blocks.
4. The necessary weighted-growth condition (4.11).
5. The exact positive-mass count (5.1) and decay estimate (5.2).

### Not proved

1. That an actual PBBS passage genealogy realizes the persistent escape
   \(b_n=2,s_n=z_n=0\).
2. That actual PBBS chronology forces (4.11).
3. Any cross-level non-reuse or decorrelation theorem.
4. The quotient bound \(O_A(B_r/N)\), namely \((\mathrm{CP}_A)\);
   the stronger \((\mathrm{RP}_A)\); or the coefficient-one theorem
   through this lane.

The exact next PBBS-specific target is therefore:

\[
\boxed{
\text{force weighted terminal-block growth, positive deep block mass,
or cross-level trace decorrelation on every critical passage tower.}
}
\]

Ranks, seam slots, bounded terminal-block sizes, strict gap descent, and
all additive transported trace volumes are now rigorously known to be
insufficient by themselves.

## 8. Independent audit record

Two independent audits checked the occurrence injection in (2.2), the
\(B_r/H\) scalar ceiling, the CP/RP normalization, every binomial
cancellation in (4.6) and (5.1), both exponential constants in (4.7), the
harmonic sum \(5/12\), the threshold \(\frac12\log R\), and the abstract
lane loads.  The final statement incorporates their domain and scope
corrections: a cemetery state is included in (2.1),
\(0\le n<L\), \(2\le b\le p_n-1\), \(Q>H+1\), and the trace-area sequence
is explicitly only a formal envelope.  No remaining mathematical error
was found.
