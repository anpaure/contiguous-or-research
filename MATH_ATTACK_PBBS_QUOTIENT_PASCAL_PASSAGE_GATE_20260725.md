# The exact Pascal-passage gate for PBBS quotient residence

Date: 2026-07-25

No computation or web search is used in this note.

## 0. Outcome

Put

\[
 N=2r+1,
 \qquad B=\operatorname{Cat}_r,
\]

and normalize a PBBS state as \(0D\), where \(D\) is a Dyck word of
semilength \(r\).  Let \(\partial D\) be simultaneous peak deletion, as
in Theorem 14.1 of `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.

This note gives an exact one-level recursive classification of every
consecutive omitted-label return of gap \(g<N\).  If

\[
 E=\partial D\in\mathcal D_d,
\]

then the reduced PBBS omitted-particle itinerary determines one nonnegative
integer \(z\).  The original return occurs exactly when the final root slot
in the inverse leaf expansion \(E\mapsto D\) contains \(z\) new leaf
children.  If \(k=\operatorname{pk}(E)\), the exact number of rank-\(r\)
inverse trees with this prescribed slot is

\[
 \boxed{
 K_r(E,z)=
 \binom{r+d-k-z-1}{2d-1}.}
 \tag{0.1}
\]

Consequently the number of quotient roots starting a specified gap \(g<N\)
has the exact Pascal sum (4.1) below.

The recursion does **not** by itself prove

\[
 \overline\nu_H=O\!\left(\frac{\operatorname{Cat}_r}{2r+1}\right).
 \tag{0.2}
\]

There is an exact obstruction to an unweighted induction.  For

\[
 E_d=(10)^{d-2}1100
\]

and \(d\) near \(r/4\), all

\[
 \binom r{2d-1}=\exp((\log2+o(1))r)
\]

rank-\(r\) inverse roots having empty final root slot start a gap-seven
return.  After short quotient cycles are discarded, at least one ninth of
these quotient intervals can be packed, while **every one of them projects
under \(\partial\) to the same ordered reduced passage trace**.  (That
reduced walk can wrap its short reduced cycle.)  Thus recursive
peak deletion has exponential, not bounded or polynomial, packing
congestion.

This does not contradict (0.2): \(2^r\) is exponentially smaller than
\(\operatorname{Cat}_r/(2r+1)\).  It identifies the first unresolved gate
precisely.  A proof of (0.2) must be a Pascal-**weighted aggregate passage
packing theorem** over all reduced cores.  It cannot be an unweighted charge
of each outer interval to its nested reduced interval, nor can it obtain a
uniform entropy loss from fixing the root slot.

Throughout the quotient application we assume

\[
 4\le H,\qquad 2H-1<N,\qquad H\log N=o(r),
 \tag{0.3}
\]

which contains the intended range
\(H=\sqrt r\,\omega(r)\) under the upper restriction used in the PBBS
reduction.

## 1. Equality particles and the reduced itinerary

Let the unmatched physical zero of the rooted cyclic word \(0D\) have
coordinate \(u\).  The equality particles are the cyclic edges whose two
endpoint bits agree.  Label them persistently in cyclic order.  Label by
\(0\) the equality particle immediately before \(u\), and label its cyclic
predecessor by \(-1\).  If

\[
 E=\partial D\in\mathcal D_d,
 \qquad p=2d+1,
\]

then Theorem 14.1 says that the recorded particle word is the normalized
PBBS word \(0E\) on \(p\) sites.

Let

\[
 \kappa_t\in\mathbb Z_p
\]

be the omitted particle label at time \(t\) in this reduced PBBS.  Thus
\(\kappa_0=0\).  Let \(x_j(t)\in\mathbb Z_N\) be the physical edge occupied
by particle \(j\) immediately before the update at time \(t\).  With
consistent integer lifts over any interval of length less than \(N\), the
exact skew system is

\[
 \begin{aligned}
 x_j(t+1)&=x_j(t)+\mathbf1_{\{\kappa_t=j\}},\\
 \lambda_t&=x_{\kappa_t}(t)+1,
 \end{aligned}
 \tag{1.1}
\]

where \(\lambda_t\) is the original PBBS omitted physical label.

For \(j\in\mathbb Z_p\), put

\[
 n_j(t)=\#\{0\le s<t:\kappa_s=j\}.
 \tag{1.2}
\]

Then

\[
 x_j(t)=x_j(0)+n_j(t)
 \tag{1.3}
\]

on such an integer lift.

## 2. The final root slot is the physical predecessor gap

Use the plane-tree contour bijection.  The core tree encoded by \(E\) has
\(d\) edges and

\[
 k=\operatorname{pk}(E)
\]

leaves.  Every tree with one-step pruning equal to this core is obtained by
attaching new leaf children in the ordered child slots of the core:

* a vertex with \(c\) existing children has \(c+1\) slots;
* every core leaf must receive at least one new leaf child; and
* all other slot occupancies are arbitrary nonnegative integers.

The total number of slots is

\[
 \sum_v(\deg^+(v)+1)=d+(d+1)=2d+1.
 \tag{2.1}
\]

Let \(z=z_*(D)\) be the number of new leaf children put in the **final root
slot**, after the last existing child of the root.  Since \(d\ge1\), the
root is not a core leaf and this slot has no mandatory child.

### Lemma 2.1 (root-slot spacing)

With compatible integer lifts in cyclic particle order,

\[
 \boxed{x_0(0)-x_{-1}(0)=2z+1.}
 \tag{2.2}
\]

#### Proof

For \(z=0\), no deleted peak lies between the predecessor equality edge and
the distinguished equality edge, so those two particle positions are one
physical edge apart.  Adding one leaf in the final root slot appends one
terminal peak \(10\) before the final root zero.  The two new adjacencies
through this peak are unequal, so the same two consecutive equality
particles become two physical edges farther apart.  Repeating this for the
\(z\) terminal leaves gives \(1+2z\).  \(\square\)

Equivalently, the terminal condition used in the gap-seven classification,
that the last two bits of \(D\) are \(00\), is exactly \(z=0\).

## 3. Exact predecessor-passage criterion

For a reduced root \(E\), define

\[
 h_E=\min\{t>0:\kappa_t=0\}.
 \tag{3.1}
\]

For \(1\le g<N\), call \(g\) a **predecessor-passage time** of \(E\) when

\[
 \boxed{
 \kappa_g=-1,\qquad h_E<g,
 \qquad n_{-1}(g)\text{ is odd}.}
 \tag{3.2}
\]

For such a passage put

\[
 z_E(g)=\frac{n_{-1}(g)-1}{2}.
 \tag{3.3}
\]

### Theorem 3.1 (one-level PBBS return classification)

Let \(D\in\mathcal D_r\), let \(E=\partial D\in\mathcal D_d\) with
\(d\ge1\), and let \(1\le g<N\).  The physical omitted label at time zero
has its next occurrence exactly at time \(g\) if and only if

1. \(g\) is a predecessor-passage time of \(E\); and
2. the final root-slot occupancy of \(D\) is

   \[
   z_*(D)=z_E(g).
   \tag{3.4}
   \]

#### Proof

Put

\[
 a=x_0(0)-x_{-1}(0)=2z_*(D)+1.
\]

At time zero, particle \(0\) is selected and

\[
 \lambda_0=x_0(0)+1.
 \tag{3.5}
\]

Particle order is preserved.  Before \(N\) total particle moves have
occurred, particle \(0\) cannot travel once around the physical coordinate
circle, and no particle can overtake another.  Therefore the next particle
which can enter the physical edge just vacated behind particle \(0\) is its
cyclic predecessor \(-1\).  Consequently, for \(0<t<N\),

\[
 \lambda_t=\lambda_0
 \quad\Longleftrightarrow\quad
 \kappa_t=-1
 \ \text{ and }\ x_{-1}(t)=x_0(0).
 \tag{3.6}
\]

By (1.3), the second condition is

\[
 n_{-1}(t)=x_0(0)-x_{-1}(0)=a.
 \tag{3.7}
\]

The predecessor's move at time \(t\) enters the physical edge occupied by
particle \(0\) immediately after time zero.  Hence particle \(0\) must have
been selected again strictly before \(t\), which is \(h_E<t\).  Conversely,
when (3.6)--(3.7) and \(h_E<t\) hold, (1.1) gives
\(\lambda_t=\lambda_0\).

There is no earlier return: among occurrences of particle \(-1\), exactly
one has \(n_{-1}(t)=a\), namely its \((a+1)\)-st selection, and no other
particle can enter that physical edge first by cyclic order.  Thus the
return is consecutive.  Finally, (2.2) turns (3.7) into

\[
 n_{-1}(g)=2z_*(D)+1,
\]

which is exactly (3.2)--(3.4).  \(\square\)

The passage itinerary is a property only of the reduced quotient root
\(E\).  All other inverse-tree slot occupancies are irrelevant to this
particular return.

## 4. Exact Pascal enumeration

Fix a nonempty core \(E\in\mathcal D_d\) with \(k=\operatorname{pk}(E)\).
To obtain semilength \(r\), attach \(r-d\) new leaves.  One leaf is mandatory
at each of the \(k\) core leaves, leaving

\[
 y=r-d-k
 \tag{4.1a}
\]

free leaves to distribute among the \(2d+1\) slots.  Thus the total
one-step inverse fibre has size

\[
 \boxed{
 P_r(E)=\binom{y+2d}{2d}
       =\binom{r+d-k}{2d}.}
 \tag{4.1b}
\]

If the final root slot is prescribed to contain \(z\) leaves, the remaining
\(y-z\) free leaves are distributed among \(2d\) slots.  Hence

\[
 \boxed{
 K_r(E,z)=
 \begin{cases}
 \displaystyle\binom{y-z+2d-1}{2d-1}
 =\binom{r+d-k-z-1}{2d-1},&0\le z\le y,\\[6pt]
 0,&\text{otherwise.}
 \end{cases}}
 \tag{4.2}
\]

Let \(R_g(r)\) be the number of normalized Dyck quotient roots of
semilength \(r\) which start a consecutive omitted-label return of gap
\(g<N\).  Theorem 3.1 and (4.2) give the exact identity

\[
 \boxed{
 R_g(r)=
 \sum_{d=1}^{r-1}
 \ \sum_{\substack{E\in\mathcal D_d\\
                    g\text{ is a passage time of }E}}
 \binom{r+d-\operatorname{pk}(E)-z_E(g)-1}{2d-1},}
 \tag{4.3}
\]

where an inadmissible binomial coefficient is zero.

The omitted boundary \(d=0\) is harmless here.  Its inverse trees are the
height-one stars \((10)^r\), there is only one equality particle, and their
first physical return has full circumference rather than gap \(g<N\).

### Check 1: gap five

At rank one, \(E=10\), the reduced quotient is fixed and its omitted labels
advance by one on \(\mathbb Z_3\).  At time five,

\[
 \kappa_5=-1,qquad h_E=3,qquad n_{-1}(5)=1,
\]

so \(z_E(5)=0\).  Here \(d=k=1\), and (4.2) gives

\[
 K_r(10,0)=\binom{r-1}{1}=r-1,
\]

recovering the exact gap-five count.

### Check 2: gap seven

For

\[
 E_d=(10)^{d-2}1100,
 \qquad d\ge2,
\]

the first eight reduced omitted labels are

\[
 0,\ p-3,\ p-1,\ 1,\ p-2,\ 0,\ 2,\ p-1,
 \qquad p=2d+1.
 \tag{4.4}
\]

Thus time seven is a passage, \(h_{E_d}=5\),
\(n_{-1}(7)=1\), and \(z_{E_d}(7)=0\).  Since
\(\operatorname{pk}(E_d)=d-1\), formula (4.2) gives

\[
 K_r(E_d,0)=\binom r{2d-1}.
 \tag{4.5}
\]

Summing (4.5) over \(d\ge2\) recovers

\[
 R_7(r)=\sum_{d\ge2}\binom r{2d-1}=2^{r-1}-r.
\]

## 5. The exact obstruction to unweighted recursive packing

Let \(\tau=\phi^2\) be the step-two quotient permutation.  Peak deletion is
a semiconjugacy:

\[
 \partial(\tau D)=\tau(\partial D).
 \tag{5.1}
\]

Thus an outer quotient interval starting at \(D\) projects edge by edge to
the reduced interval starting at \(E=\partial D\).  More precisely, the
return root is based at the odd-step occurrence \(D\), whereas its projected
residence interval begins at the preceding insertion edge.  Passing from
\(D\) to that insertion edge is one fixed shift by the PBBS permutation.
It is a bijection on quotient roots and commutes with peak deletion.  We
therefore identify a return root with its insertion-edge start below; this
changes neither distinctness, interval length, nor the projected trace.

### Theorem 5.1 (one reduced passage has exponential outer packing load)

Choose \(d=d(r)\) so that the odd integer \(2d-1\) differs from \(r/2\)
by at most two.  Put

\[
 \mathcal F_{r,d}
 =\{D\in\mathcal D_r:\partial D=E_d, z_*(D)=0\}.
\]

Then

\[
 |\mathcal F_{r,d}|=\binom r{2d-1}
 =\exp((\log2+o(1))r).
 \tag{5.2}
\]

Every member starts a gap-seven return.  If (0.3) holds, then on the long
quotient cycles these starts contain a pairwise edge-disjoint family of
residence intervals of size at least

\[
 \boxed{
 \frac19\left(\binom r{2d-1}-Z_H\right)
 =(1-o(1))\frac19\binom r{2d-1}.}
 \tag{5.3}
\]

Every interval in this family projects under \(\partial\) to the same
ordered reduced passage trace starting at \(E_d\); the reduced walk itself
wraps a short reduced cycle and is not being called a nonwrapping quotient
interval.  Moreover

\[
 \partial E_d=10,
 \tag{5.3a}
\]

so all members have the same complete two-level pruned return skeleton.

#### Proof

Equation (5.2) and the gap-seven assertion are (4.5) and Theorem 3.1.
There are at most \(Z_H\) quotient starts on short quotient cycles.  By
(17.2),

\[
 Z_H\le(2H+2)N^{2H+2}=\exp(o(r))
 \tag{5.4}
\]

under (0.3), whereas the binomial coefficient in (5.2) has exponential
rate \(\log2\).  Thus deleting all short-cycle starts removes \(o(|\mathcal
F_{r,d}|)\) members.

A gap-seven residence interval uses five consecutive step-two quotient
edges.  On one directed cycle, a fixed such interval can meet only intervals
whose start edges lie at one of the four preceding, its own, or the four
following positions.  Hence its closed conflict neighbourhood contains at
most nine starts.  Greedily select one interval and delete its closed
conflict neighbourhood.  This selects at least one ninth of all remaining
starts.  Intervals on different quotient cycles are automatically disjoint,
proving (5.3).

Finally, all selected roots have \(\partial D=E_d\), and (5.1) makes their
entire ordered projected walks identical.  Deleting the \(d-1\) peaks of
\(E_d\) leaves \(10\), proving (5.3a).  \(\square\)

In particular, charging each outer interval to any bounded menu of edges or
states in its nested reduced passage has exponential congestion.

There is a second, pointwise obstruction.  From (4.1b)--(4.2), fixing an
empty final root slot retains the exact fraction

\[
 \boxed{
 \frac{K_r(E,0)}{P_r(E)}
 =\frac{2d}{r+d-\operatorname{pk}(E)}.}
 \tag{5.5}
\]

This ratio can equal one.  For example, for \(E_d\) at its minimum possible
outer rank \(r=2d-1\), the free-leaf number is zero, so every inverse tree
has empty final root slot.  Therefore there is no uniform constant entropy
loss at one pruning level.

## 6. The remaining weighted aggregate gate

Let

\[
 R_{\le H}^{\rm long}(r)
 =\sum_{\substack{g\le2H-1\\g\text{ odd}}}
   R_g^{\rm long}(r)
\]

be the number of short-return starts on long quotient cycles.  Since there
is at most one start interval at each quotient edge and every such interval
has at most \(H+1\) edges, the elementary conflict-graph bound gives

\[
 \boxed{
 \frac{R_{\le H}^{\rm long}(r)}{2H+1}
 \le \overline\nu_H
 \le R_{\le H}^{\rm long}(r).}
 \tag{6.1}
\]

Indeed, an interval of length at most \(H+1\) can meet only intervals whose
start lies among at most \(H\) preceding, its own, or at most \(H\)
following quotient edges.  Greedy packing proves the lower bound; the upper
bound is tautological.

Combining (4.3) with the removal of short-cycle roots gives an exact
Pascal-weighted formula for the start count in (6.1).  Therefore the clean
stronger sufficient estimate for (0.2) is

\[
 \sum_{\substack{g\le2H-1\\g\text{ odd}}}
 \sum_{d=1}^{r-1}
 \sum_{\substack{E\in\mathcal D_d\\g\text{ passage for }E}}
 \binom{r+d-\operatorname{pk}(E)-z_E(g)-1}{2d-1}
 =O\!\left(\frac{\operatorname{Cat}_r}{2r+1}\right),
 \tag{6.2}
\]

apart from the negligible short-cycle term.  Estimate (6.2) controls all
starts and is stronger than necessary; the exact residence theorem only
asks for the packing bound (0.2).

Theorem 5.1 shows why an induction on \(d\) cannot discard the binomial
weight in (6.2).  A successful proof must exploit jointly

1. the reduced PBBS predecessor-passage condition (3.2);
2. the core leaf statistic \(\operatorname{pk}(E)\), which controls the
   Pascal fibre weight;
3. the prescribed slot \(z_E(g)\); and
4. overlap competition between interval lifts over different reduced
   cores and quotient cycles.

The pruning-rank profile, Dyck height, one-step marginal enumeration, and
unweighted reduced packing number do not supply this joint control.

## 7. Precise verdict

The bound (0.2) is neither proved nor disproved here.

What is proved is:

* the exact current invariant (3.6)--(3.7);
* the exact predecessor-passage classification, Theorem 3.1;
* the exact Pascal kernel (4.2) and return-start identity (4.3);
* the exact long-cycle quotient greedy factor \(1/9\) for the fixed-core
  gap-seven family; and
* exponential congestion of the natural recursive charge
  \(D\mapsto\partial D\).

The fixed-core obstruction has size only \(\exp((\log2+o(1))r)\), while

\[
 \frac{\operatorname{Cat}_r}{2r+1}
 =\exp((\log4+o(1))r).
\]

It is therefore rigorously harmless for the desired numerical bound.  The
first unresolved step is exactly the Pascal-weighted aggregate
passage-packing estimate described in Section 6.
