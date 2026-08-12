# PBBS growing-depth chronology: an exact split-gap renewal, all-sheet Pascal pullback, and uniform packing lower bounds

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

The decisive split-gap formula, the \(1/(2d+1)\) normalization, the
ordinary-time/step-two conversion, and the \(K+1\) degree constant were
independently audited in Section 8 of
MATH_AUDIT_O_PBBS_GROWING_DEPTH_RENEWAL_KERNEL_20260726.md.

## 0. Outcome

Put

\[
 n=2m+1,\qquad B_m=\operatorname {Cat}_m,
 \qquad H=\lceil A\sqrt m\rceil,                 \tag{0.1}
\]

where \(A>0\) is fixed.  Let \(\overline\nu_H\) be the maximum number of
pairwise quotient-edge-disjoint positive PBBS residence intervals of
residence at most \(H\), after quotient cycles of length at most \(H+1\)
are removed.

This report proves a genuinely all-depth renewal recurrence.  It also
proves two uniform packing lower bounds, including an actual growing-depth
lower family.  It does **not** prove either

\[
 \overline\nu_H=o_A(B_m/H)                       \tag{0.2}
\]

or a matching \(\Omega_A(B_m/H)\) obstruction.

The exact new state is as follows.  On an augmented reduced PBBS orbit,
strict alternation of adjacent equality-particle labels splits every
predecessor gap into two positive pieces \(u,r\).  If the outer inverse
peak-deletion terminal occupancy is \(z\), its first parent return time is

\[
 \boxed{
 G^{(z)}_{b,i}
 =r_{b,i}+\sum_{j=0}^{2z}g_{b,i+j}
 =\sum_{j=0}^{2z+1}r_{b,i+j}
  +\sum_{j=1}^{2z+1}u_{b,i+j}.}                 \tag{0.3}
\]

It satisfies the exact renewal step

\[
 \boxed{
 G^{(z+1)}_{b,i}-G^{(z)}_{b,i}
 =g_{b,i+2z+1}+g_{b,i+2z+2}.}                  \tag{0.4}
\]

Every quantity in (0.3)--(0.4) is an actual PBBS chronological quantity;
there is no independence or fibre-envelope substitution.

Let \(M_{m,s}\) be the number of normalized rank-\(m\) roots whose first
omitted-label return has gap \(2s+1\).  For every \(1\le s<m\), hence
before the outer circumference, Theorem 3.1 gives the exact coefficient
recurrence

\[
 \boxed{
 \begin{aligned}
 M_{m,s}={}&
 \sum_{d=1}^{m-1}\ \sum_{\mathcal O\in\mathfrak O_d}
 {1\over 2d+1}
 \sum_{b\in\mathbb Z_{2d+1}}
 \sum_{i=1}^{|\mathcal O|/(2d+1)}
 \sum_{z\ge0}
 \mathbf1_{\{G^{(z)}_{b,i}=2s+1\}}\\
 &\hspace{36mm}\cdot
 \binom{m+d-k(\mathcal O)-z-1}{2d-1}.
 \end{aligned}}                                  \tag{0.5}
\]

The binomial-zero convention imposes all feasibility conditions.  The
completely pruned root has gap \(2m+1\), hence shell \(s=m\), and
contributes nothing in the stated range \(s<m\).  Consequently

\[
 R_{m,H}^{\rm all}=\sum_{s=1}^{H-1}M_{m,s},
 \qquad
 R_{m,H+1}^{\rm all}-R_{m,H}^{\rm all}=M_{m,H}. \tag{0.6}
\]

Thus the new short-return kernel really does iterate through every
Gaussian depth.  What it does not supply is a contraction: evaluating
(0.5) requires the joint cyclic law of consecutive \(u,r\) blocks, and
packing them requires their ordered placement on the parent cycles.

The fixed-depth audits give the exact initial conditions

\[
 M_{m,1}=0,\qquad M_{m,2}=m-1,                  \tag{0.7}
\]

and the independently audited gap-seven classification gives

\[
 M_{m,3}=2^{m-1}-m.                              \tag{0.8}
\]

The \(M_{m,2}\) starts are exactly the \(n(m-1)\) physical depth-three
wrong-rank windows.  Independently, every correct depth-three target is
present with load between \(1\) and \(35\).  Correct support and return
chronology are therefore already distinct at the first nontrivial depth.

For every shell \(s+1\le H\), the exact interval support has \(s+2\)
quotient edges.  If \(M_{m,s}^{(H)}\) denotes the starts retained on
cycles longer than \(H+1\), then

\[
 \boxed{
 \overline\nu_H\ge
 \max_{1\le s\le H-1}
 \left\lceil{M_{m,s}^{(H)}\over2s+3}\right\rceil}             \tag{0.9}
\]

and, with \(J_H=1+\lfloor\log_2(H+1)\rfloor\),

\[
 \boxed{
 \overline\nu_H\ge {1\over4J_H}
 \sum_{s=1}^{H-1}{M_{m,s}^{(H)}\over s+2}.}      \tag{0.10}
\]

These are actual chronology bounds, not marginal counts.  In particular,
for every fixed \(A>0\), eventually

\[
 \boxed{
 \overline\nu_{\lceil A\sqrt m\rceil}
 \ge \left({1\over18}+o_A(1)\right)2^m.}         \tag{0.11}
\]

More importantly, an independently audited spectator-conveyor family
gives a lower bound at a genuinely growing shell.  For fixed

\[
 0<\alpha<A,\qquad \eta>0,
 \qquad s=\lfloor\alpha\sqrt m\rfloor,
\]

one has

\[
 \boxed{
 \overline\nu_H\ge
 {B_m\over2s+3}
 \exp\!\left[-\bigl(\log(3+\eta)+o(1)\bigr)s\right].}         \tag{0.12}
\]

This is exponentially larger than every fixed-depth polynomial family,
but it is still stretched-exponentially below \(B_m/H\).

Finally, a two-tail completion lemma proves a sharp no-go for deductions
from the listed scalar recurrences.  Any prescribed subcritical early
shell histogram can be
completed at two later shells so as to satisfy exactly

\[
 \sum_sM_{m,s}=B_m,\qquad \sum_ssM_{m,s}=mB_m.   \tag{0.13}
\]

In particular, (0.7)--(0.8), the convex rank-excess recurrence, and the
Kac first moment cannot force any further Gaussian returns.  The new
Pascal kernel does not alter this conclusion: it gives exact conditional
fibre weights once the literal events \(G^{(z)}_{b,i}\le2H-1\) are known,
but it does not create those events.

The exact remaining gate is therefore the Pascal-weighted joint law of
the low values in (0.3), their transported slot addresses, and their
ordered interval conflicts.  Section 9 states a precise bounded-degree
criterion which would refute (0.2).

## 1. The exact depth dictionary

Let two consecutive occurrences of an omitted PBBS coordinate have odd
gap

\[
                         2s+1.                  \tag{1.1}
\]

On the complemented centered step-two chronology, that coordinate has
positive residence

\[
                         q=s+1                  \tag{1.2}
\]

and the complete insertion-through-deletion support contains exactly

\[
                         q+1=s+2                \tag{1.3}
\]

quotient transition edges.  It enters horizon \(H\) exactly when

\[
                         s+1\le H,              \tag{1.4}
\]

equivalently when its physical gap is at most \(2H-1\).

This convention reconciles the two shallow audits.

* Gap three would have \(s=1\) and residence two.  It never occurs, so
  the complemented centered rows satisfy \(G_2+P_2\).  The audited
  correct depth-two lower loads lie in \([1,10]\), and the upper loads
  lie in \([1,3]\).
* Gap five has \(s=2\), residence three, and four-edge support.  Its
  normalized start count is \(m-1\), hence its physical start count is
  \(n(m-1)\).
* At those starts one coordinate has state pattern \(0,1,1,0\) on one
  centered parity.  It contributes exactly one unit of depth-three rank
  excess.
* The independent global-maximum corridor still supplies every correct
  depth-three target, with correct load in \([1,35]\).  That theorem does
  not count the wrong-rank windows above.
* Gap seven has \(s=3\), residence four, five-edge support, and normalized
  start count \(2^{m-1}-m\).

Thus neither the \(q=2\) load caps nor the \(q=3\) correct-support cap can
be extrapolated to growing chronology.  The relevant variable is the
first-return shell \(M_{m,s}\).

## 2. Adjacent-label split gaps

Fix an augmented rank-\(d\) reduced PBBS orbit \(\mathcal O\).  Put

\[
 p=2d+1,\qquad L=|\mathcal O|.                  \tag{2.1}
\]

The persistent equality-particle labels are the cyclic group
\(\mathbb Z_p\).  Write \(\kappa_t\) for the selected label at event time
\(t\).  Coordinate homomesy says that every label occurs exactly

\[
                         L/p                    \tag{2.2}
\]

times.

For a label \(b\), list its cyclic visit times as \(t_{b,i}\), and put

\[
 g_{b,i}=t_{b,i+1}-t_{b,i}.                     \tag{2.3}
\]

Indices are cyclic, with a lifted integer representative used when time
differences are taken.

These are ordinary augmented PBBS selection times.  A displacement of
\(t\) on the normalized step-two quotient chronology \(\tau\) is an
ordinary-time displacement \(2t\); it is not an increment of the visit
index \(i\).  Formula (0.3) is used only for return epochs.  Quotient
conflict degrees below are defined directly with \(\tau^{\pm t}\).

### Lemma 2.1 (strict adjacent-label alternation)

For \(a=b+1\), every open interval

\[
 (t_{b,i-1},t_{b,i})
\]

contains exactly one \(a\)-visit.  Denote it by \(s_{b,i}\).

#### Proof

The audited no-overtaking theorem says that an open interval between two
consecutive \(a\)-visits contains at most one \(b\)-visit.  There are
exactly \(L/p\) such intervals and exactly \(L/p\) \(b\)-visits, so every
one contains exactly one.  Reversing the roles of the complementary
interval partitions gives exactly one \(a\)-visit between consecutive
\(b\)-visits.  \(\square\)

Define the two positive split gaps

\[
 u_{b,i}=s_{b,i}-t_{b,i-1},\qquad
 r_{b,i}=t_{b,i}-s_{b,i}.                       \tag{2.4}
\]

Then

\[
 \boxed{g_{b,i-1}=u_{b,i}+r_{b,i}.}             \tag{2.5}
\]

The first two future \(b\)-visits after the event \(s_{b,i}\) are
\(t_{b,i}\) and \(t_{b,i+1}\).  Hence the second predecessor-selection
time is

\[
 t_{b,i+1}-s_{b,i}
 =r_{b,i}+g_{b,i}
 =r_{b,i}+u_{b,i+1}+r_{b,i+1}.                 \tag{2.6}
\]

This is the terminal-zero case of (0.3).

Let

\[
 h_{b,i}=s_{b,i+1}-s_{b,i}
 =g_{b,i}+r_{b,i}-r_{b,i+1}.                   \tag{2.6a}
\]

### Theorem 2.2 (all-occupancy predecessor renewal)

For every feasible terminal occupancy \(z\ge0\), before the outer
circumference, the first parent return time at phase \(s_{b,i}\) is the
quantity \(G^{(z)}_{b,i}\) in (0.3).  Moreover, (0.4) holds.

#### Proof

The exact predecessor-passage theorem identifies the parent return with
the \((2z+2)\)-nd future selection of the immediate predecessor \(b\).
Starting from \(s_{b,i}\), that event occurs at \(t_{b,i+2z+1}\).  Thus

\[
 \begin{aligned}
 t_{b,i+2z+1}-s_{b,i}
 &=t_{b,i}-s_{b,i}
   +\sum_{j=0}^{2z}(t_{b,i+j+1}-t_{b,i+j})\\
 &=r_{b,i}+\sum_{j=0}^{2z}g_{b,i+j}.
\end{aligned}
\]

Strict alternation places the next \(a\)-selection before
\(t_{b,i+1}\), hence before this endpoint even when \(z=0\).  The
leader-return clause in the predecessor-passage theorem is therefore
automatic; the displayed predecessor event is the first physical return.

Substituting \(g_{b,j}=u_{b,j+1}+r_{b,j+1}\) gives the second expression
in (0.3).  Replacing \(z\) by \(z+1\) adds exactly the two final gaps in
(0.4).  Subtracting (0.3) at consecutive split indices and using (2.6a)
also gives the exact phase recurrence

\[
 \boxed{
 G^{(z)}_{b,i+1}-G^{(z)}_{b,i}
 =g_{b,i+2z+1}-h_{b,i}.}                        \tag{2.6b}
\]

\(\square\)

Every feasible \(G^{(z)}_{b,i}<n\) is a consecutive omitted-label gap;
the odd-gap theorem therefore makes it odd.  Equation (0.4) also shows
that it is strictly increasing in \(z\), by an even increment at least
two.

It is useful to record the complete orbitwise first moment.  Direct every
event selecting \(b+1\) to the next event selecting \(b\).  Strict
alternation makes this a permutation of the \(L\) event points.  The sum
of the forward lengths around every cycle of that permutation is an
integer multiple of \(L\).  Therefore there is an integer
\(\omega(\mathcal O)\) such that

\[
 \sum_{b,i}r_{b,i}=\omega(\mathcal O)L.         \tag{2.7}
\]

Since every \(b\)-gap family sums to \(L\),

\[
 \sum_{b,i}(u_{b,i}+r_{b,i})=pL.                \tag{2.8}
\]

All \(u,r\) are positive, so

\[
 \boxed{
 \sum_{b,i}u_{b,i}=(p-\omega(\mathcal O))L,
 \qquad1\le\omega(\mathcal O)\le p-1.}         \tag{2.9}
\]

More generally, summing (0.3) over all event points gives

\[
 \boxed{
 {1\over L}\sum_{b,i}G^{(z)}_{b,i}
 =(2z+1)p+\omega(\mathcal O).}                  \tag{2.10}
\]

No stronger identity such as \(\omega=d+1\) is asserted or used.  The
mean (2.10) does not determine the lower tail
\(G^{(z)}\le2H-1\).

## 3. Exact all-shell census

Let \(F\in\mathcal D_d\) be a nonexceptional first-pruned root with

\[
 k=\operatorname {pk}(F),\qquad
 y=m-d-k,\qquad p=2d+1.                         \tag{3.1}
\]

Its inverse fibre is the weak-composition simplex

\[
 \mathcal W_{p,y}
 =\{(x_0,\ldots,x_{p-1})\in\mathbb Z_{\ge0}^p:
                   \sum_jx_j=y\}.              \tag{3.2}
\]

If the terminal coordinate has exact value \(z\), the other \(p-1=2d\)
coordinates contain mass \(y-z\).  The exact sheet size is therefore

\[
 \boxed{
 K_{m;d,k}(z)
 =\binom{y-z+p-2}{p-2}
 =\binom{m+d-k-z-1}{2d-1}.}                    \tag{3.3}
\]

It is zero unless \(0\le z\le y\).

Let \(\mathfrak O_d\) be the augmented rank-\(d\) orbit set.  The
augmentation is a \(p\)-fold labelled cover of the normalized reduced
roots.  On an orbit, the events \(s_{b,i}\) enumerate every augmented
phase exactly once.  Peak count is orbit-invariant.

### Theorem 3.1 (coefficient-exact all-\(s\) renewal)

For every \(1\le s<m\), formula (0.5) holds.

#### Proof

Fix an augmented event \(s_{b,i}\) and an occupancy \(z\).  Theorem 2.2
says that its first parent return has gap \(G^{(z)}_{b,i}\).  Equation
(3.3) counts all parents on that exact terminal sheet.  Summing over
events and augmented orbits counts every labelled reduced root once;
division by \(p=2d+1\) removes the augmentation.  Inverse fibres partition
the nonexceptional rank-\(m\) roots.  The completely pruned root belongs
to shell \(s=m\), outside the theorem's range.  This proves (0.5).
\(\square\)

The threshold at one reduced phase is now

\[
 Z_H(b,i)=\max\{z:G^{(z)}_{b,i}\le2H-1\},       \tag{3.4}
\]

with value \(-1\) if the set is empty.  Because the \(G^{(z)}\)'s are
strictly increasing odd integers,

\[
 \boxed{Z_{H+1}(b,i)-Z_H(b,i)\in\{0,1\}.}       \tag{3.5}
\]

The increment is one exactly when the next occupancy sheet has return
gap (2H+1).  Summing (3.3) over the phases where this happens gives
(0.6).

This is an exact recurrence, but it is not scalar: (0.4) requires the
next two ordered predecessor gaps.  Equations (2.9)--(2.10) supply their
first moments and do not supply their lower-tail placement.

## 4. Rank excess is the shell integral, not the chronology

Let

\[
 e_q=\sum_{s\ge1}(q-s)_+M_{m,s}                 \tag{4.1}
\]

be normalized PBBS rank excess.  Discrete differentiation gives

\[
 \boxed{
 e_q-e_{q-1}=\sum_{s\le q-1}M_{m,s}=R_{m,q}^{\rm all},}
                                                               \tag{4.2}
\]

and

\[
 \boxed{
 M_{m,q-1}=e_q-2e_{q-1}+e_{q-2}.}               \tag{4.3}
\]

The shallow seeds are

\[
 e_1=e_2=0,\qquad e_3=m-1.                      \tag{4.4}
\]

Summing (4.1) over all \(q\le H\) gives the exact all-depth footprint

\[
 \boxed{
 \sum_{q=1}^{H}e_q
 =\sum_{s=1}^{H-1}\binom{H-s+1}{2}M_{m,s}.}     \tag{4.5}
\]

Using (0.7)--(0.8), for \(H\ge4\),

\[
 \begin{aligned}
 \sum_{q=1}^{H}e_q
 ={}&\binom{H-1}{2}(m-1)
 +\binom{H-2}{2}(2^{m-1}-m)\\
 &+\sum_{s=4}^{H-1}\binom{H-s+1}{2}M_{m,s}.    \tag{4.6}
 \end{aligned}
\]

In particular, at \(H=\lceil A\sqrt m\rceil\),

\[
 \boxed{
 \sum_{q=1}^{H}e_q
 \ge\left({A^2\over4}+o_A(1)\right)m2^m.}       \tag{4.7}
\]

This growing aggregate is still exponentially below Catalan scale.  More
importantly, neither (4.2) nor (4.5) records where the intervals lie on
their quotient cycles.  They cannot determine packing.

## 5. The all-time Pascal kernel

The outer fibre algebra can be iterated exactly.  Fix one reduced orbit
and identify every parent fibre with a reference copy of
\(\mathcal W_{p,y}\).  Persistent equality-particle gaps show that PBBS
transport permutes the free coordinates.  Explicitly, if an output
coordinate is initially written as

\[
 x'_j=x_{\rho(j)}+\beta_j,
\]

then nonnegativity on every weak composition gives \(\beta_j\ge0\), and
preservation of total free mass for every weak composition forces
\(\sum_j\beta_j=0\) and makes \(\rho\) a permutation.  Hence every pulled
back phase test has the form

\[
                         x_{a_i}\le Z_i.         \tag{5.1}
\]

For a finite phase set \(I\), put

\[
 c_a(I)=\min\{Z_i:i\in I,\ a_i=a\},             \tag{5.2}
\]

with \(c_a=\infty\) if address \(a\) is not tested.  If one \(Z_i=-1\),
the intersection is empty.

### Theorem 5.1 (arbitrary-time threshold-cylinder kernel)

If all selected phases are reduced-active, then

\[
 \boxed{
 \left|\bigcap_{i\in I}\{x:x_{a_i}\le Z_i\}\right|
 =[X^y]\prod_{a:c_a<\infty}(1+X+\cdots+X^{c_a})
             \prod_{a:c_a=\infty}{1\over1-X}.}  \tag{5.3}
\]

Equivalently,

\[
 \boxed{
 \sum_{J\subseteq C(I)}(-1)^{|J|}
 \binom{y-\sum_{a\in J}(c_a+1)+p-1}{p-1},}     \tag{5.4}
\]

where \(C(I)=\{a:c_a<\infty\}\).

#### Proof

Repeated tests of one address reduce to the smallest cap.  A constrained
coordinate contributes (1+X+\cdots+X^{c_a}), and an unconstrained one
contributes \((1-X)^{-1}\).  Coefficient extraction proves (5.3).
Inclusion--exclusion on violations \(x_a\ge c_a+1\) proves (5.4).
\(\square\)

The exact-shell version replaces a bounded-coordinate factor by \(X^z\).
Thus every mixed old/new term in the horizon increment has an exact
coefficient formula.  The state needed by that formula is the complete
address-collision partition and the coordinatewise minimum caps; it is
not determined by one- and two-time marginals.

At the Pascal saddle

\[
 d={m\over2}+O(\sqrt{m\log m}),\qquad
 k={m\over6}+O(\sqrt{m\log m}),                 \tag{5.5}
\]

one terminal-zero condition retains

\[
 {K_{m;d,k}(0)\over|\mathcal W_{p,y}|}
 ={2d\over m+d-k}={3\over4}+o(1).              \tag{5.6}
\]

For caps at most \(3\log m\), two distinct transported addresses retain
the product density up to \(o(1)\), while a repeated address changes it
by at most the sharp factor (4/3+o(1)).  In particular, two active
phases retain at least \(9/16-o(1)\) of their complete fibre.

These constants show that one pruning level has no vanishing one- or
two-point factor.  They do **not** show that an \(O(\sqrt m)\)-phase
intersection retains constant density: even independent terminal-zero
tests contribute \((3/4)^{\Theta(\sqrt m)}\).  Nor do pair correlations
upper-bound an interval independence number.

## 6. Exact interval scheduling and uniform lower bounds

On a retained parent quotient cycle, attach to every eligible start its
literal interval of \(s+2\le H+1\) consecutive edges.  After a cycle is
cut at an edge not used by the intervals under consideration, order the
line intervals by increasing right endpoint.  If \(p(j)\) is the last
interval ending strictly before interval \(j\) begins, then the exact
weighted-interval scheduling recurrence is

\[
 F(0)=0,\qquad
 F(j)=\max\{F(j-1),1+F(p(j))\}.                 \tag{6.1}
\]

For a circular family and an arbitrary reference edge \(e\), every
independent family either contains no interval through \(e\), or contains
exactly one such interval \(I\).  In the second case delete the closed
conflict neighborhood of \(I\) and apply (6.1) on the complementary line.
Taking the maximum over these alternatives is an exact circular
recurrence.  Summing over quotient cycles is exactly
\(\overline\nu_H\).

This recurrence is uniform in all shell lengths.  It also exposes why the
shell census (0.5) does not close the problem: (6.1) needs the ordered
right endpoints, not only their number.

### Theorem 6.1 (one-shell packing)

For every \(1\le s\le H-1\),

\[
 \overline\nu_H\ge
 \left\lceil{M_{m,s}^{(H)}\over2s+3}\right\rceil.             \tag{6.2}
\]

#### Proof

Every interval in shell \(s\) has \(s+2\) edges.  Two such circular
intervals can intersect only if their start positions differ by one of
the \(2(s+1)\) nonzero offsets from \(-(s+1)\) through \(s+1\).  There is
at most one start at a quotient position.  Hence the shell conflict graph
has maximum degree at most \(2s+2\), and greedy selection gives (6.2).
Different quotient cycles are disjoint.  \(\square\)

### Theorem 6.2 (dyadic harmonic-shell packing)

Formula (0.10) holds.

#### Proof

Put every support length \(\ell=s+2\) into its bin

\[
                         2^j\le\ell<2^{j+1}.
\]

If \(N_j\) starts lie in the bin, its conflict graph has maximum degree
less than \(2^{j+2}-1\), so it contains an independent set of size at
least \(N_j/2^{j+2}\).  Its harmonic mass is at most \(N_j/2^j\).  Thus
the best bin retains at least one fourth of that bin's harmonic mass.
There are at most \(J_H\) nonempty bins, proving (0.10).  \(\square\)

The logarithm cannot be removed from shell sizes alone: intervals of
many lengths can all contain one common edge while their reciprocal-length
sum is harmonic.  A PBBS improvement must use the ordered split-gap
process in (0.3).

Two exact necessary consequences of \((ST_A)\) are therefore

\[
 M_{m,s}^{(H)}
 =o_A\!\left((2s+3){B_m\over H}\right)
 \qquad(1\le s\le H-1),                         \tag{6.3}
\]

and

\[
 \sum_{s=1}^{H-1}{M_{m,s}^{(H)}\over s+2}
 =o_A\!\left({B_m\log H\over H}\right).         \tag{6.4}
\]

They are necessary only.  Shell intervals of different lengths can
cluster on the same quotient edges.

## 7. Unconditional growing-window lower bounds

Let \(Z_H^{\rm cyc}\) be the number of quotient roots on cycles of length
at most \(H+1\).  The voltage-itinerary bound gives

\[
 Z_H^{\rm cyc}\le(2H+2)n^{2H+2}
 =\exp(O_A(\sqrt m\log m))=2^{o(m)}.             \tag{7.1}
\]

Apply Theorem 6.1 to the exact gap-seven shell \(s=3\).  Its supports have
five edges, so

\[
 \overline\nu_H
 \ge {\bigl(2^{m-1}-m-Z_H^{\rm cyc}\bigr)_+\over9}
 =\left({1\over18}+o_A(1)\right)2^m             \tag{7.2}
\]

for every fixed \(A>0\) and all sufficiently large \(m\).  This proves
(0.11).  It persists uniformly throughout the Gaussian window, but

\[
 {2^m\over B_m/H}=\Theta_A\!\left({m^2\over2^m}\right)\to0. \tag{7.3}
\]

The stronger growing-shell calibration uses the audited
spectator-conveyor theorem from
`MATH_THEOREM_N_ST_LONG_PERIOD_FIBRE_AMPLIFICATION_OBSTRUCTION_20260726.md`
and its independent audit
`MATH_AUDIT_N_ST_LONG_PERIOD_FIBRE_AMPLIFICATION_20260726.md`.
For \(s=\lfloor\alpha\sqrt m\rfloor\), it supplies actual simple
long-cycle return passages whose exact terminal-zero inverse-fibre mass is

\[
 B_m\exp\!\left[-\bigl(\log(3+\eta)+o(1)\bigr)s\right].       \tag{7.4}
\]

Distinct lifts of one simple reduced passage cannot share a parent edge:
a collision projects to the same reduced edge at the same offset, then
bijectivity forces the parent roots to agree.  Different selected reduced
passages have disjoint projected supports.  Finally, every shell-\(s\)
support has \(s+2\) edges, so Theorem 6.1 contributes the exact greedy
denominator (2s+3).  This proves (0.12).

Since \(s\sim\alpha\sqrt m\),

\[
 {H\over2s+3}
 \exp[-(\log(3+\eta)+o(1))s]\longrightarrow0.   \tag{7.5}
\]

Thus (0.12) is a genuine growing-\(q\) theorem but not a counterexample to
\((ST_A)\).

The deck normalization is exact in the lower direction: every selected
quotient interval has \(n\) pairwise edge-disjoint spatial lifts, and
distinct selected quotient supports lift disjointly.  Hence both (7.2)
and (0.12) may be multiplied by \(n\) to obtain physical residence-packing
lower bounds.  The critical physical scale \(B_m\sqrt m\) corresponds to
the quotient scale \(B_m/H\) up to the fixed factor determined by \(A\).

## 8. A no-go for the listed scalar recurrences

The gap process has the exact Kac identities

\[
 \sum_sM_{m,s}=B_m,\qquad
 \sum_ssM_{m,s}=mB_m.                            \tag{8.1}
\]

They follow by summing the cyclic gaps of every omitted label: every
label's gaps sum to its cycle length, and the mean odd gap is
(2m+1).

### Theorem 8.1 (two-tail completion)

Let \(a_s\ge0\) be any finite integer histogram supported on \(s<m\), and
put

\[
 A_0=\sum_sa_s<B_m,\qquad D_0=\sum_ssa_s,
 \qquad A_0=0\ \hbox{or}\ D_0<mA_0.             \tag{8.2}
\]

Then \(a\) can be completed by nonnegative integer masses at two adjacent
indices, both at least \(m\), so that (8.1) holds exactly.

#### Proof

The empty histogram is completed trivially by mass \(B_m\) at \(s=m\).
Assume \(A_0>0\).

Put

\[
 T=B_m-A_0,\qquad M=mB_m-D_0,
 \qquad \mu={M\over T}.                         \tag{8.3}
\]

Because \(D_0<mA_0\), one has \(\mu>m\).  Let \(r=\lfloor\mu\rfloor\)
and define

\[
 x=(r+1)T-M,\qquad y=M-rT.                      \tag{8.4}
\]

The integers \(x,y\) are nonnegative, \(x+y=T\), and
\(rx+(r+1)y=M\).  Put mass \(x\) at shell \(r\), mass \(y\) at shell
\(r+1\), and zero at every other unprescribed shell.  Then both equations
in (8.1) hold.  Since \(\mu>m\), \(r\ge m\).  \(\square\)

For the audited shallow seeds, an explicit completion is

\[
 \widehat M_2=m-1,\qquad
 \widehat M_3=2^{m-1}-m,                        \tag{8.5}
\]

\[
 \widehat M_m=B_m-(m-2)2^{m-1}-1,\qquad
 \widehat M_{m+1}=(m-3)2^{m-1}+2,              \tag{8.6}
\]

with all other terms zero.  For all sufficiently large \(m\), these are
nonnegative, and direct substitution gives

\[
 \sum_s\widehat M_s=B_m,
 \qquad\sum_ss\widehat M_s=mB_m.                \tag{8.7}
\]

Its rank-excess sequence

\[
 \widehat e_q=\sum_s(q-s)_+\widehat M_s
\]

has nonnegative discrete curvature and agrees with every seed in
(0.7)--(0.8).  Nevertheless, for every (4\le H<m),

\[
 \sum_{s\le H-1}\widehat M_s=2^{m-1}-1.        \tag{8.8}
\]

This is an abstract histogram obstruction, not a claim that
\(\widehat M\) is realized by PBBS.  It proves exactly that the shallow
audits, nonnegative curvature, total gap mass, and Kac first moment cannot
force Catalan-critical Gaussian starts.

The completion deliberately places its compensating mass at \(s\ge m\),
where positive winding and more than one outer circumference are possible.
No zero-winding passage theorem is asserted there.  This is why the result
is a no-go only for the listed scalar identities, not a realizability
counterexample.

The conclusion survives the known growing-shell calibration.  Any finite
collection of prescribed early masses with total \(o(B_m/m)\), including
the stretched-exponential mass in (7.4), can be added to \(a_s\) in
Theorem 8.1; its two tail masses remain nonnegative and all unprescribed
Gaussian shells remain zero.  Thus the presently proved subcritical
growing families do not repair the scalar recurrence.

## 9. A rigorous critical lower-bound criterion

The exact kernel does give a clean route to a counterexample if bounded
local degree occurs on critical Pascal mass.

For a reduced root \(F\in\mathcal D_d\), put

\[
 \mathscr A_H=\{F:B_2(F)\le2H-1\},              \tag{9.1}
\]

and define its two-sided reduced active degree

\[
 \Delta_H(F)=\sum_{t=1}^{H+1}
 \left(\mathbf1_{\mathscr A_H}(\tau^tF)
      +\mathbf1_{\mathscr A_H}(\tau^{-t}F)\right).           \tag{9.2}
\]

The exact terminal-zero sheet above a rank/peak cell has size

\[
 K_0(d,k)=\binom{m+d-k-1}{2d-1}.                \tag{9.3}
\]

Let

\[
 \mathscr L^{(0)}_{H,K}
 =\sum_{d=1}^{m-1}\sum_{\substack{F\in\mathcal D_d:\\
                   d+\operatorname {pk}(F)\le m,\\
                   F\in\mathscr A_H,\ \Delta_H(F)\le K}}
 K_0(d,\operatorname {pk}(F)).                  \tag{9.4}
\]

### Theorem 9.1 (bounded-degree pullback)

For every fixed \(K\ge0\),

\[
 \boxed{
 \overline\nu_H\ge
 \left\lceil{[\mathscr L^{(0)}_{H,K}-Z_H^{\rm cyc}]_+
                  \over K+1}\right\rceil.}      \tag{9.5}
\]

#### Proof

Every terminal-zero parent over a root in (9.4) is active by the exact
predecessor threshold.  If two such parent intervals overlap, their
starts differ by at most \(H+1\) in one of the two cyclic directions.
Peak deletion sends the second start to a reduced active phase at that
same displacement.  Thus its parent conflict degree is at most
\(\Delta_H(F)\le K\).  Deleting all roots on short quotient cycles loses
at most \(Z_H^{\rm cyc}\) vertices.  Greedy selection in the remaining
maximum-degree-\(K\) conflict graph proves (9.5).  \(\square\)

In the saddle tube (5.5), let

\[
 P_m(d,k)=\binom{m+d-k}{2d}.                    \tag{9.6}
\]

Equation (5.6) gives

\[
 K_0(d,k)=\left({3\over4}+o(1)\right)P_m(d,k)   \tag{9.7}
\]

uniformly.  Hence, if for fixed \(K,\kappa>0\) the complete-fibre-weighted
saddle mass of the roots in (9.4) is at least

\[
                         \kappa B_m/H,           \tag{9.8}
\]

then

\[
 \boxed{
 \overline\nu_H\ge
 \left({3\kappa\over4(K+1)}-o(1)\right){B_m\over H}.}        \tag{9.9}
\]

This would refute \((ST_A)\).  Conversely, \((ST_A)\) forces the
\(K_0\)-weighted parent mass of every fixed-\(K\) stratum in (9.4) to be
\(o_A(B_m/H)\).  This says nothing by itself about the unweighted number
of reduced cores, or about complete \(P_m\)-weighted mass outside the
stated saddle tube.

The one- and two-point Pascal constants do not prove (9.8).  They are
conditional on the literal reduced indicators in (9.1).  A divergent
mean pair correlation would also be insufficient for a positive proof,
because an interval graph can have rare dense clusters and a large
independent remainder.  A positive proof needs a degree-profile or
ordered-Hall theorem for the actual process (0.3).

## 10. Precise proved and unproved boundary

The following are proved here, using the cited audited PBBS inputs.

1. Strict adjacent-label alternation yields the split-gap coordinates
   \(u,r\).
2. Every terminal occupancy \(z\) has the exact return epoch (0.3), with
   the two-gap renewal step (0.4).
3. The coefficient-exact shell formula (0.5) and horizon recurrence
   (0.6) hold at every \(s<m\).
4. The winding conservation (2.9) and all-\(z\) first moment (2.10) are
   exact.
5. The arbitrary-time Pascal pullback is the coefficient formula
   (5.3)--(5.4).
6. The literal variable-length chronology has the exact scheduling
   recurrence (6.1), the shell bound (0.9), and the dyadic bound (0.10).
7. The unconditional fixed-shell lower bound (0.11) and the actual
   growing-shell lower bound (0.12) hold.
8. The two-tail completion theorem proves that the shallow shell values,
   curvature, total mass, and Kac first moment listed in Section 8 are
   insufficient.
9. The bounded-degree criterion (9.5)--(9.9) is an exact route to a
   critical lower obstruction.

The following are not proved.

* No \(o_A(B_m/H)\) upper bound for \(\overline\nu_H\) is obtained.
* No fixed \(K,\kappa>0\) satisfying (9.8) is obtained.
* No claimed identity \(\omega(\mathcal O)=d+1\) is used.
* Correct-target loads, even though complete at every fixed depth, do not
  determine the return shells or their order.
* The all-time Pascal formula solves the outer fibre intersection algebra,
  but not the reduced renewal epochs or the circular scheduling maximum.

Thus the PBBS growing-depth lane has an exact all-sheet recurrence and a
rigorous growing-\(q\) lower boundary.  Its unresolved theorem is now
sharply localized: prove either that every critical Pascal-weighted active
sector has diverging ordered local clusters strong enough to force the
interval scheduling value to be \(o(B_m/H)\), or exhibit critical mass in
one bounded-degree stratum of (9.4).
