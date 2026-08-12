# PBBS fixed-Gaussian residence packing: exact pruning recurrence and a candidate obstruction

Date: 2026-07-25

Method: pure equality-particle and plane-tree analysis. No computation or
external search is used.

## 0. Outcome

Let

\[
 N=2r+1,\qquad B_r=\operatorname{Cat}_r,
\qquad H=\lceil A\sqrt r\rceil
\]

with \(A>0\) fixed. The constant-one gate is

\[
 \boxed{\nu_H(P_r)=o_A(B_r).}
\tag{0.1}
\]

This note does not prove or refute (0.1). It does provide two exact
advances and one sharply quantified obstruction candidate.

1. Every short outer PBBS return descends to a strictly shorter return
   in the peak-deleted PBBS. Grouping an edge-disjoint outer family by
   pruning rank gives an exact **capacitated packing recurrence**,
   equations (4.2)--(4.4).
2. For a complete pruning-rank profile, both the unrestricted inverse
   multiplicity and the multiplicity with every passage slot prescribed
   factor into explicit binomial kernels, equations (3.7)--(3.9).
3. Slot prescriptions alone cannot yield a little-oh theorem. The
   Catalan-positive unary-root family

   \[
   \mathcal U_r=\{\,1E0:E\in\mathcal D_{r-1}\,\}
   \]

   has size \(B_{r-1}\sim B_r/4\) and has final-root slot zero at every
   active pruning level. If only order \(B_r/\sqrt r\) members of this
   family start a fixed-Gaussian short return, the desired little-oh
   estimate already fails. This gives a concrete candidate obstruction,
   equation (6.7).

Thus the remaining theorem cannot follow from pruning ranks plus a
product of one-slot fibre losses. It must exploit the actual nested PBBS
passage itineraries, or else those itineraries may furnish a
counterexample through \(\mathcal U_r\).

## 1. Strict return descent under peak deletion

Normalize a quotient state as \(0D\), where \(D\in\mathcal D_r\).
Write

\[
 D^{(0)}=D,\qquad D^{(j+1)}=\partial D^{(j)},
\qquad r_j=|D^{(j)}|/2.
\tag{1.1}
\]

Suppose the original omitted physical label has a consecutive return of
odd gap \(g_0<N\). The equality-particle theorem says that the particle
selected at time zero must be selected again before its immediate
predecessor makes the final entry. Let \(g_1\) be the first positive time
at which that particle is selected again in the reduced PBBS on
\(0D^{(1)}\).

Then \(g_1\) is itself a consecutive same-label return and

\[
 \boxed{3\le g_1\le g_0-2.}
\tag{1.2}
\]

The lower bound is the no-gap-one fact and oddness; the upper bound follows
because \(g_1<g_0\) and both gaps are odd.

As long as

\[
 g_j<2r_j+1,
\tag{1.3}
\]

the same argument applies again and produces

\[
 g_{j+1}\le g_j-2.
\tag{1.4}
\]

Thus every gap \(g_0\le2H-1\) has a canonical descending return chain
until either rank zero is reached or the reduced circumference becomes at
most the current gap. In particular the number of nontrivial descent
levels is at most \(H-1\).

At one descent step, let the reduced omitted-particle itinerary be
\(\kappa_t\), rooted with \(\kappa_0=0\), and let

\[
 h_E=\min\{t>0:\kappa_t=0\}
\]

for \(E=D^{(1)}\). If the outer return occurs at \(g\), then

\[
 \kappa_g=-1,\qquad h_E<g,
\qquad n_{-1}(g)=2z+1,
\tag{1.5}
\]

where \(z\) is the final-root-slot occupancy in the inverse
leaf expansion \(E\mapsto D\). Hence

\[
 \boxed{z=z_E(g):=\frac{n_{-1}(g)-1}{2}.}
\tag{1.6}
\]

For fixed \(E\), different predecessor-passage times give different
values of \(z\), because successive eligible occurrences of particle
\(-1\) have strictly increasing odd occurrence counts.

## 2. Pruning profiles

Put

\[
 \ell_j=r_j-r_{j+1}.
\tag{2.1}
\]

This is the number of leaves removed from the \(j\)-th pruned tree.
Every leaf of \(D^{(j+1)}\) must have at least one leaf child in
\(D^{(j)}\), so

\[
 \ell_j\ge\ell_{j+1}.
\tag{2.2}
\]

Equivalently, the pruning ranks are discretely convex:

\[
 \boxed{s_j:=r_j-2r_{j+1}+r_{j+2}\ge0.}
\tag{2.3}
\]

A complete pruning profile is therefore the same numerical data as a
partition

\[
 r=\ell_0+\ell_1+\cdots,
\qquad
 \ell_0\ge\ell_1\ge\cdots\ge1.
\tag{2.4}
\]

The slack \(s_j=\ell_j-\ell_{j+1}\) is exactly the number of free new
leaves at inverse step \(j\), after putting one mandatory new leaf on
each leaf of the core.

## 3. Exact one-level and multilevel inverse multiplicities

Fix three consecutive pruning ranks

\[
 r_0,\quad r_1,\quad r_2.
\]

The core \(E=D^{(1)}\) has \(r_1\) edges and

\[
 k(E)=r_1-r_2
\]

leaves. To lift it to rank \(r_0\), one attaches
\(r_0-r_1\) new leaves in its \(2r_1+1\) ordered child slots, with one
mandatory leaf at each of the \(k(E)\) core leaves. The number of free
leaves is

\[
 s=r_0-r_1-k(E)=r_0-2r_1+r_2.
\tag{3.1}
\]

### Proposition 3.1 (rank-profile kernel)

For every fixed core \(E\) with these ranks, the unrestricted inverse
fibre has size

\[
 \boxed{
 P(r_0,r_1,r_2)
 =\binom{s+2r_1}{2r_1}
 =\binom{r_0+r_2}{2r_1}.}
\tag{3.2}
\]

If the final root slot is prescribed to contain exactly \(z\) leaves,
then the fibre has size

\[
 \boxed{
 K(r_0,r_1,r_2;z)
 =
 \begin{cases}
 \displaystyle
 \binom{r_0+r_2-z-1}{2r_1-1},&0\le z\le s,\\[5pt]
 0,&\text{otherwise.}
 \end{cases}}
\tag{3.3}
\]

Moreover

\[
 \boxed{\sum_{z=0}^{s}K(r_0,r_1,r_2;z)
 =P(r_0,r_1,r_2).}
\tag{3.4}
\]

The exact one-slot fraction is

\[
 \boxed{
 \frac{K(r_0,r_1,r_2;z)}{P(r_0,r_1,r_2)}
 =
 \frac{2r_1}{r_0+r_2}
 \frac{(s)_{\underline z}}
      {(r_0+r_2-1)_{\underline z}}.}
\tag{3.5}
\]

For \(z=0\), the second factor is one. Notice that

\[
 \frac{2r_1}{r_0+r_2}\le1
\]

is exactly the profile convexity (2.3).

#### Proof

After the mandatory children are installed, distribute \(s\) identical
leaves among \(2r_1+1\) ordered slots. This gives (3.2). Prescribing the
last slot to contain \(z\) leaves leaves \(s-z\) objects for \(2r_1\)
slots, giving (3.3). The hockey-stick identity gives (3.4), and direct
division of the two binomial coefficients gives (3.5). \(\square\)

Now fix a complete rank profile

\[
 r_0>r_1>\cdots>r_L>0,\qquad r_{L+1}=0,
\tag{3.6}
\]

and fix the bottom word \(D^{(L)}\). For every \(0\le j<L\), prescribe a
final-root-slot value \(z_j\). Since both kernels depend only on three
successive ranks, not on the detailed core shape, inverse choices at
successive levels multiply.

### Corollary 3.2 (exact tower multiplicity)

The number of towers over the fixed bottom word, with rank profile
(3.6) and all displayed slot values prescribed, is

\[
 \boxed{
 \mathcal K(\mathbf r,\mathbf z)
 =
 \prod_{j=0}^{L-1}
 \binom{r_j+r_{j+2}-z_j-1}{2r_{j+1}-1}.}
\tag{3.7}
\]

Without slot prescriptions it is

\[
 \boxed{
 \mathcal P(\mathbf r)
 =
 \prod_{j=0}^{L-1}
 \binom{r_j+r_{j+2}}{2r_{j+1}}.}
\tag{3.8}
\]

Here an inadmissible binomial is zero. Their ratio is

\[
 \boxed{
 \frac{\mathcal K(\mathbf r,\mathbf z)}
      {\mathcal P(\mathbf r)}
 =
 \prod_{j=0}^{L-1}
 \left[
 \frac{2r_{j+1}}{r_j+r_{j+2}}
 \frac{(s_j)_{\underline{z_j}}}
      {(r_j+r_{j+2}-1)_{\underline{z_j}}}
 \right].}
\tag{3.9}
\]

If the profile is continued all the way to the empty tree, the final
nonempty core is the unique star of its rank, so no additional bottom
multiplicity is needed.

This is the exact multiplicative law requested by the peak-deletion
approach.

In particular, fix an actual descending passage tower

\[
 g_0>g_1>\cdots>g_{L-1}
\]

and its bottom core. At level \(j\), equation (1.6) prescribes

\[
 z_j=z_{D^{(j+1)}}(g_j).
\]

Conditional on the displayed pruning ranks and bottom core, the number of
outer roots realizing every one of these slot requirements is exactly
\(\mathcal K(\mathbf r,\mathbf z)\), before the additional reduced-itinerary
conditions are imposed. Hence (3.7) is an upper bound for every fixed
passage tower and becomes exact once those lower-core passages are fixed.

## 4. Exact capacitated packing descent

Work in the rotation quotient, whose directed transition-edge set is
\(\mathcal D_r\). Let

\[
 \overline\nu_H(r)
\]

be the maximum number of pairwise quotient-edge-disjoint nonwrapping
short-residence intervals on long quotient cycles.

For a nonnegative integral edge-capacity function \(c\) on
\(\mathcal D_d\), define

\[
 \mathfrak p_h(d;c)
\]

to be the maximum total multiplicity of reduced consecutive-return
walks of residence at most \(h\), where every directed quotient edge
\(E\) is used at most \(c(E)\) times, counting traversal multiplicity.
Reduced cycles are allowed to wrap here. This convention is needed because
a nonwrapping outer interval can project to a wrapping reduced walk.

Fix \(d\), and consider top roots \(D\in\mathcal D_r\) with
\(|\partial D|/2=d\). For a reduced edge \(E\in\mathcal D_d\), put

\[
 r_2(E)=|\partial E|/2
\]

and

\[
 c_{r,d}(E)
 =P(r,d,r_2(E))
 =\binom{r+r_2(E)}{2d}.
\tag{4.1}
\]

This is exactly the number of directed top quotient edges above \(E\).
It is constant along every reduced PBBS orbit, as also follows directly
from the semiconjugacy.

### Proposition 4.1 (capacitated descent)

Take an edge-disjoint outer family and replace every outer return interval
by its canonical first-repeat subinterval in the reduced PBBS. If the
outer residence is at most \(H\), the reduced residence is at most
\(H-1\), by (1.2). At any reduced edge \(E\), at most \(c_{r,d}(E)\)
projected subinterval traversals can pass through \(E\), because the outer
family uses each of its \(c_{r,d}(E)\) preimage edges at most once.
Therefore the exact capacitated descent inequality is

\[
 \boxed{
 \overline\nu_H(r)
 \le
 \sum_{d=1}^{r-1}
 \mathfrak p_{H-1}\bigl(d;c_{r,d}\bigr).}
\tag{4.2}
\]

No small-circumference error is hidden in (4.2): such a reduced return is
one of the allowed wrapping walks in \(\mathfrak p\). The only short-cycle
term enters later, when quotient packing is compared with physical packing
through the deck inequality.

#### Proof

Peak deletion commutes with the step-two quotient permutation. Therefore
the trace of the canonical reduced first-repeat interval is a subtrace of
the projection of its outer interval. Fix a reduced directed edge \(E\).
Every traversal of \(E\) by one of the selected subtraces comes from a
top directed edge in \(\partial^{-1}(E)\). Distinct traversals in the
outer family come from distinct top edges, because the outer intervals are
edge-disjoint. The fibre has exactly \(c_{r,d}(E)\) edges by (3.2).
Thus the projected walks obey the displayed edge capacities. Different
values of \(d\) partition the outer roots, so summing their capacitated
optima proves (4.2). \(\square\)

There is a sharper start cap. For \(E\in\mathcal D_d\), let
\(\mathcal Z_H(E)\) be the set of slot values \(z_E(g)\) arising from
predecessor-passage times which produce outer residence at most \(H\).
Define

\[
 L_{r,H}(E)
 =
 \sum_{z\in\mathcal Z_H(E)}
 K(r,d,r_2(E);z).
\tag{4.3}
\]

The sets in this sum are disjoint inverse fibres, by uniqueness of the
root-slot occupancy. Let \(J_E\) be the canonical first-repeat interval
starting at \(E\). Every outer short return above \(E\) projects to
\(J_E\). Hence the number of outer intervals is bounded by the optimum of
the integral capacitated system

\[
\boxed{
\begin{aligned}
\max\quad&\sum_{E\in\mathcal D_d}a_E\\
\text{subject to}\quad&
0\le a_E\le L_{r,H}(E),\qquad a_E\in\mathbb Z,\\
&
\sum_{E\in\mathcal D_d}m_F(J_E)a_E
\le c_{r,d}(F)
\qquad(F\in\mathcal D_d).
\end{aligned}}
\tag{4.4}
\]

Here \(m_F(J_E)\) is the number of traversals of \(F\) by \(J_E\).
Summing (4.4) over \(d\) is a refinement of (4.2). Conversely, every
prospective violation of (0.1) yields a large feasible solution of one
of these systems.

Iterating (4.4) down a fixed pruning profile gives edge capacities
\(\mathcal P(\mathbf r)\) and start caps
\(\mathcal K(\mathbf r,\mathbf z)\). In particular, if
\(\mathscr T\) is any collection of admissible passage towers, its outer
packing number is bounded by

\[
 \boxed{
 \sum_{\mathbf r}
 \operatorname{Pack}_{\mathbf r}
 \left(
 \text{nested passage intervals};
 \ \mathcal P(\mathbf r),\mathcal K(\mathbf r,\mathbf z)
 \right),}
\tag{4.5}
\]

where the two capacity systems are the explicit products (3.7)--(3.8).
Equation (4.5) is schematic notation for the iterated integer system
(4.4), not an appeal to an unproved probabilistic independence.

For the physical factor, the exact deck inequality gives

\[
 N\overline\nu_H(r)
\le\nu_H(P_r)
\le2N\overline\nu_H(r)+N Z_H.
\tag{4.6}
\]

Thus the fixed-window gate is equivalent, up to the negligible
short-cycle term, to

\[
 \boxed{\overline\nu_H(r)=o_A(B_r/N).}
\tag{4.7}
\]

Equations (3.7)--(4.4) are the exact recursive form of this gate.

## 5. Why a product of slot losses cannot close the recurrence

It is tempting to use only the first factor in (3.5),

\[
 \frac{2r_{j+1}}{r_j+r_{j+2}},
\]

and hope that multiplying it over \(\Theta(\sqrt r)\) pruning levels
forces an exponential loss. This is false even as an aggregate counting
principle.

Define

\[
 \mathcal U_r
 =\{D=1E0:E\in\mathcal D_{r-1}\}.
\tag{5.1}
\]

These are the plane trees whose root has exactly one child. Therefore

\[
 \boxed{|\mathcal U_r|=B_{r-1}
 \sim\frac14B_r.}
\tag{5.2}
\]

If \(E\ne\varnothing\), simultaneous peak deletion satisfies

\[
 \boxed{\partial(1E0)=1(\partial E)0.}
\tag{5.3}
\]

Indeed, the outer root edge is not a leaf edge during that pruning round;
all deleted peaks lie inside \(E\). Consequently every nonempty pruned
tree in the tower of \(D\in\mathcal U_r\) again has unary root.

In each inverse step, no new leaf lies after the root's sole surviving
child. Hence

\[
 \boxed{z_j(D)=0
\quad\text{at every active pruning level}.}
\tag{5.4}
\]

Thus the intersection of all the zero-final-slot events over the entire
pruning tower has Catalan-positive density, at least \(1/4+o(1)\). The
individual factors in (3.9) can be close to one on the profiles carrying
this mass, and no argument which forgets the PBBS passage condition can
deduce \(o(B_r)\).

This is stronger than the previously observed fixed-core exponential
congestion: the family (5.1) itself has the full Catalan exponential base
four.

It does **not** refute (0.1), because (5.4) records only the inverse-slot
side of the return criterion. The reduced PBBS predecessor-passage
conditions may still select a vanishing fraction of \(\mathcal U_r\).

The unary family is also stable under the exact pruning kernel. If
\(F\ne\varnothing\), the unary preimages of \(1F0\) are precisely

\[
 1E0\qquad(\partial E=F).
\tag{5.5}
\]

Thus their multiplicity is the ordinary inverse-fibre multiplicity of
\(F\), one rank lower. Consequently the candidate obstruction is not a
single exceptional profile: it is a Catalan branching subtree of the full
Pascal kernel, closed under descent until the final star.

## 6. A sharp candidate positive-density obstruction

Let

\[
 \mathcal U_r^{\mathrm{short}}(A)
\]

be the members of \(\mathcal U_r\) which start a quotient short-return
interval of residence at most \(H=\lceil A\sqrt r\rceil\) on a quotient
cycle longer than \(H+1\). Put

\[
 S_r(A)=|\mathcal U_r^{\mathrm{short}}(A)|.
\tag{6.1}
\]

There is an exact Pascal formula for this candidate family before the
long-cycle deletion. For \(F\in\mathcal D_{d-1}\), put

\[
 C(F)=1F0\in\mathcal D_d
\]

and let \(\mathcal P_H^0(F)\) mean that the reduced PBBS rooted at
\(C(F)\) has a predecessor-passage time \(g\le2H-1\) with

\[
 n_{-1}(g)=1.
\]

Equivalently, its required outer slot is \(z=0\). If
\(e(F)=|\partial F|/2\), then

\[
 \boxed{
 S_r^{\rm all}(A)
 =
 \sum_{d=1}^{r-1}
 \ \sum_{\substack{F\in\mathcal D_{d-1}\\
                    \mathcal P_H^0(F)}}
 \binom{r-1+e(F)}{2d-2}.}
\tag{6.2}
\]

Here \(S_r^{\rm all}\) includes short quotient cycles. To prove (6.2),
write an outer unary tree as \(D=1E0\). Its pruned core is \(1F0\)
exactly when \(\partial E=F\). The number of rank-\((r-1)\) inverse
subtrees \(E\) above \(F\) is

\[
 P(r-1,d-1,e(F))
 =\binom{r-1+e(F)}{2d-2}.
\]

Every such unary lift has outer final-root slot zero, so the exact
predecessor-passage classification gives precisely the condition
\(\mathcal P_H^0(F)\). This proves (6.2). The short-cycle contribution is
\(\exp(o(r))\), so it is negligible at the threshold below.

The passage condition in (6.2) has a particularly concrete initial
form. Every \(C(F)=1F0\) is primitive. In the exact two-step PBBS formula,
the terminal primitive-component suffix is empty, so its two-step deficit
is one. If the initial omitted particle is labelled zero, then

\[
 \boxed{\kappa_2=-1.}
\tag{6.3}
\]

Thus \(\mathcal P_H^0(F)\) asks whether, after this forced first selection
of the predecessor at time two, particle zero is selected again and the
predecessor receives its next selection at some odd time
\(g\le2H-1\). No inverse-tree statistic remains in this question; it is
a return-spacing question internal to the PBBS orbit of the primitive
core \(1F0\).

On each long directed quotient cycle, two intervals of length at most
\(H+1\) can conflict only if their starts lie within \(H\) edges in
either direction. Greedy interval packing therefore gives

\[
 \boxed{
 \overline\nu_H(r)
 \ge \frac{S_r(A)}{2H+1}.}
\tag{6.4}
\]

Lifting all \(N\) spatial phases of a quotient-edge-disjoint family gives

\[
 \boxed{
 \nu_H(P_r)
 \ge \frac{N\,S_r(A)}{2H+1}.}
\tag{6.5}
\]

Since \(N\sim2r\) and \(H\sim A\sqrt r\),

\[
 \frac{\nu_H(P_r)}{B_r}
 \ge
 \left(\frac1A+o_A(1)\right)
 \frac{\sqrt r\,S_r(A)}{B_r}.
\tag{6.6}
\]

Therefore:

\[
 \boxed{
 \limsup_{r\to\infty}
 \frac{\sqrt r\,S_r(A)}{B_r}>0
 \quad\Longrightarrow\quad
 \nu_H(P_r)\ne o_A(B_r).}
\tag{6.7}
\]

The whole unary family has asymptotic size \(B_r/4\). Thus it is enough
for only an order-\(r^{-1/2}\) fraction of unary-root trees to have a
fixed-Gaussian short return in order to disprove the constant-one
residence gate.

This threshold is natural: a heuristic uniform first-return hazard over
\(N\asymp r\) physical labels in a window of length
\(H\asymp\sqrt r\) is precisely of order \(H/N\asymp r^{-1/2}\).
The heuristic is not a proof, but it identifies \(\mathcal U_r\) as a
genuine positive-density obstruction candidate rather than an
exponentially negligible fixed-core family.

Equally, a proof of (0.1) via the present recursion must establish the
opposite quantitative statement

\[
 \boxed{S_r(A)=o_A(B_r/\sqrt r)}
\tag{6.8}
\]

and its analogues for all other Catalan-mass pruning towers.

## 7. Exact remaining alternatives

The equality-particle recursion now leaves two concrete routes.

### Route I: prove a weighted recursive contraction

Use the integer system (4.4), with the exact kernels

\[
 P(r_0,r_1,r_2)
 =\binom{r_0+r_2}{2r_1},
\]

\[
 K(r_0,r_1,r_2;z)
 =\binom{r_0+r_2-z-1}{2r_1-1},
\]

and prove that its iterated optimum is

\[
 o_A(B_r/N).
\]

Any such proof must use the location and overlap of the nested passage
intervals \(J_E\). The scalar inequalities \(K\le P\) and the pruning
profile alone cannot work because of \(\mathcal U_r\).

### Route II: refute by a Catalan-mass passage family

Prove (6.7), preferably inside the stable unary-root class. A still
stronger counterexample would give

\[
 S_r(A)\gg B_r/\sqrt r,
\]

which by (6.5) forces a macroscopic or divergent normalized packing.

At present neither route is complete. The substantive new reduction is
that the recursive problem is not an unspecified peak-deletion induction:
it is the explicit capacitated passage system (4.4), and the first
Catalan-scale obstruction candidate is the unary-root tower (5.1), not
the exponentially smaller gap-seven fixed-core family.
