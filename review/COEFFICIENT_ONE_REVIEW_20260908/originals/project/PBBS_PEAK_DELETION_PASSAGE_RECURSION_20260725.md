# Peak deletion reduces PBBS returns to decorated shorter returns

Date: 2026-07-25

No computation or external input is used.

## 0. Outcome

Let \(D\) be a Dyck root of semilength \(r\), and let
\(\partial D\) be the Dyck root obtained by simultaneous peak deletion.
The exact equality-particle theorem gives a useful recursion.  A physical
return prunes to a genuinely shorter physical return in the particle PBBS,
with an additional prescribed continuation:

\[
 \boxed{\text{physical short return}
        \longrightarrow
        \text{shorter particle return followed by its predecessor}.}
\]

For a fixed pruned core the inverse peak-deletion fibre is counted exactly
below.  The resulting formula shows:

1. the return counts satisfy a recursive upper bound through smaller PBBS
   systems;
2. the sharp recursion retains a continuation condition after the smaller
   return; discarding it recovers only the bounded-height estimate;
3. using no information about those returns gives exactly the Catalan
   count back, with no saving;
4. even imposing literal adjacency of the two relevant equality particles
   removes only a constant fraction of a typical inverse fibre, not an
   extra factor \(1/r\).

Thus repeated pruning does not by itself prove the fixed-window residence
gate.  The missing quantitative input is a genuine decorated-return or
phase-clustering estimate.

## 1. Return and passage classes

Let \(\mathcal R_g(r)\) be the set of semilength-\(r\) Dyck roots which,
in some (equivalently every) spatial lift, start a consecutive omitted-label
return of gap at most \(g<2r+1\).

For a semilength-\(d\) PBBS root \(E\), label its particle coordinates
persistently in cyclic order.  Let \(\mathcal A_g(d)\) be the set of roots
for which, during the first \(g\) PBBS updates, there are a coordinate
\(a\) and times

\[
 0<h<t\le g
\]

such that the selected particle identities are

\[
 \kappa_0=a,\qquad \kappa_h=a,qquad \kappa_t=a-1,
 \tag{1.1}
\]

where \(a-1\) is the immediate cyclic predecessor of \(a\), and \(h\) is
the first positive reoccurrence time of \(a\).  Thus

\[
 \mathcal A_g(d)\subseteq\mathcal R_{g-2}(d),       \tag{1.2a}
\]

and (1.1) records the extra continuation from that shorter return to the
predecessor coordinate.  Call this a decorated short return.  Refine by
the number of leaves (peaks):

\[
 A_g(d,k)=\#\{E\in\mathcal A_g(d):\operatorname{pk}(E)=k\}.
 \tag{1.2}
\]

### Lemma 1.1 (exact decorated return under pruning)

If \(D\in\mathcal R_g(r)\), then

\[
 \boxed{\partial D\in\mathcal A_g(d)
        \subseteq\mathcal R_{g-2}(d)},
 \qquad d=r-\operatorname{pk}(D).                  \tag{1.3}
\]

#### Proof

Use the equality-particle dynamics of Theorem 14.1 in
`PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`.  At the first occurrence
of the returned physical label, one equality particle \(a\) enters its
edge.  Before that same edge can be entered again, particle \(a\) must be
selected once more and vacate it.  Let \(h\) be its first subsequent
selection time.  In the recorded particle word, coordinate \(a\) is
therefore the omitted label at times zero and \(h\), with no intervening
occurrence: this is a genuine consecutive omitted-coordinate return in the
smaller PBBS system.  Same-label gaps are odd; gap one would repeat a
factor state, and the final predecessor entry needs at least two further
updates.  Hence \(h\le g-2\).  Equality particles never overtake, so the
particle making the final entry is the immediate predecessor \(a-1\).
The recorded equality-particle word evolves by the canonical PBBS map and
is precisely \(0\partial D\).  This proves (1.1)--(1.3). \(\square\)

The distinction between \(\mathcal R\) and \(\mathcal A\) is still
essential: \(\mathcal A_g\) remembers which coordinate is selected after
the shorter return.  Dropping that continuation gives a valid recursive
upper bound, but loses exactly the information absent from the height-only
argument.

## 2. Exact inverse peak-deletion fibres

Fix a plane tree \(E\) with \(d\ge1\) edges and \(k\) leaves.  A tree
\(D\) satisfies \(\partial D=E\) precisely when new leaf children are
inserted in the ordered child slots of the \(d+1\) vertices of \(E\), with
at least one new child at each old leaf.  The total number of slots is

\[
 \sum_{v\in E}(\deg^+(v)+1)=2d+1.                  \tag{2.1}
\]

If \(D\) has \(r\) edges, then \(r-d\) leaves were added.  After assigning
one compulsory new leaf to each of the \(k\) old leaves, the remaining
\(r-d-k\) leaves are distributed freely among the \(2d+1\) slots.

### Lemma 2.1 (exact fibre size)

For \(r\ge d+k\),

\[
 \boxed{
 \#\{D:|D|=2r,\ \partial D=E\}
 =\binom{r+d-k}{2d}.}                              \tag{2.2}
\]

If one specified noncompulsory slot is required to receive no new leaf,
then the number is

\[
 \boxed{\binom{r+d-k-1}{2d-1}.}                   \tag{2.3}
\]

The ratio of (2.3) to (2.2) is exactly

\[
 \boxed{\frac{2d}{r+d-k}.}                        \tag{2.4}
\]

#### Proof

After the compulsory assignments, stars and bars in \(2d+1\) boxes gives

\[
 \binom{(r-d-k)+(2d+1)-1}{(2d+1)-1}
 =\binom{r+d-k}{2d}.
\]

Forbidding one box leaves \(2d\) boxes and gives (2.3).  Dividing the two
binomial coefficients gives (2.4). \(\square\)

The terminal adjacency used in the exact gap-seven classification is one
instance of (2.3): it forbids new leaves in the final root slot.  Formula
(2.4) is the exact price of that constraint.

## 3. The rigorous return-to-passage recurrence

Lemma 1.1 and the fibre partition give immediately:

### Theorem 3.1 (peak-deletion passage bound)

For every \(g<2r+1\),

\[
 \boxed{
 |\mathcal R_g(r)|
 \le
 \sum_{d=1}^{r-1}\sum_{k=1}^{d}
 A_g(d,k)\binom{r+d-k}{2d}.}                       \tag{3.1}
\]

Writing

\[
 R_{g-2}(d,k)
 =\#\{E\in\mathcal R_{g-2}(d):\operatorname{pk}(E)=k\},
\]

the inclusion in Lemma 1.1 gives the closed coarse recursion

\[
 \boxed{
 |\mathcal R_g(r)|
 \le
 \sum_{d=1}^{r-1}\sum_{k=1}^{d}
 R_{g-2}(d,k)\binom{r+d-k}{2d}.}                   \tag{3.2}
\]

If a specified empty-slot condition is separately proved necessary for a
subclass of returns, its contribution is bounded instead by

\[
 \sum_{d,k}A_g(d,k)\binom{r+d-k-1}{2d-1}.          \tag{3.3}
\]

#### Proof

Partition \(\mathcal R_g(r)\) by the pruned root
\(E=\partial D\).  Lemma 1.1 restricts \(E\) to
\(\mathcal A_g(d)\), and Lemma 2.1 counts its complete inverse fibre.
Summing proves (3.1).  Lemma 1.1 and
\(A_g(d,k)\le R_{g-2}(d,k)\) give (3.2).  If one slot is forbidden, use
(2.3) instead. \(\square\)

## 4. Why pruning alone gives no asymptotic saving

If the return/continuation condition is discarded, replace \(A_g(d,k)\) by the
Narayana number counting all \(d\)-edge plane trees with \(k\) leaves.
Then the right side of (3.1) is exactly

\[
 \operatorname{Cat}_r-1,                           \tag{4.1}
\]

because every \(r\)-edge plane tree other than the root with \(r\) leaf
children has one unique nonempty pruned core.  Adding that single omitted
tree gives \(\operatorname{Cat}_r\).
Thus an unquantified pruning statement recovers the full
Catalan space and nothing less.

Nor does a single literal adjacency supply the desired \(1/r\).  On the
bulk regime \(d=\Theta(r)\) and \(k=\Theta(d)\), formula (2.4) is bounded
away from zero.  For example, at the central profile

\[
 d=\frac r2+O(1),\qquad k=\frac d2+O(1),
\]

the ratio tends to

\[
 \frac{2(r/2)}{r+r/2-r/4}=\frac45.                 \tag{4.2}
\]

So an empty terminal slot removes only one fifth of a typical inverse
fibre.  The hoped-for factor \(1/r\) must come from the *dynamics of the
decorated continuation* in (1.1), or from a sharp use of the smaller-return
distribution in (3.2), not from inverse peak deletion or terminal adjacency
by itself.

## 5. Exact quantitative target left by the recursion

For total-root counting to imply the fixed-window residence packing gate at

\[
 g\le2A\sqrt r+1,
\]

it is enough to prove

\[
 \boxed{
 \sum_{d,k}A_g(d,k)\binom{r+d-k}{2d}
 =o_A\!\left(\frac{\operatorname{Cat}_r}{2r+1}\right).}
                                                               \tag{5.1}
\]

Indeed every quotient return root has \(2r+1\) spatial lifts, so (5.1)
makes the *total* physical number of short returns \(o_A(\operatorname{Cat}_r)\),
and hence makes their maximum edge-disjoint packing little-oh Catalan.

Condition (5.1) is stronger than necessary because packing may exploit
clustering.  Its value is that it identifies the precise missing
probability scale: after averaging through the inverse-fibre kernel, a
Gaussian-window decorated return must occur with probability
\(o_A(1/r)\).  Peak deletion supplies the kernel exactly, but it supplies
no such passage probability bound.

The next genuinely new theorem in this lane must therefore control the
short selected-coordinate pattern

\[
 a,\ldots,a,\ldots,a-1
\]

inside the canonical PBBS quotient, or use phase clustering to prove the
weaker packing estimate directly.

## 6. Every return branches into two shorter returns after pruning

There is more structure in the continuation than was used in (3.2).
Assume throughout this section that the original gap (t) is less than the
physical circumference (2r+1), as it is in every fixed Gaussian window
for all sufficiently large (r).

Let (a=kappa_0) be the equality particle which enters the returned
physical edge at time zero, and let (b=a-1) be its immediate predecessor.
Choose integer lifts of the particle positions preserving cyclic order, as
in Theorem 14.1, and put

\[
 \Delta=x_a(0)-x_b(0)\ge1.                         \tag{6.1}
\]

### Lemma 6.1 (two-child return lemma)

If the original omitted label returns for the first time at time (t),
then in the pruned PBBS:

1. coordinate (a) has a consecutive return on an interval
   ([0,h]) with (0<h<t);
2. coordinate (b) is selected exactly (Delta+1) times in
   ([0,t]), including time (t), and therefore supplies (Delta)
   consecutive return intervals wholly contained in ([0,t]).

In particular the pruned root contains at least two distinct shorter
return occurrences, one labelled (a) and one labelled (b).

#### Proof

At time zero, (14.4) gives

\[
 \lambda_0=x_a(0)+1=:u,
\]

and the update moves particle (a) from (u-1) into (u).  Before (u)
can be entered again, (a) must be selected and move out.  Let (h>0) be
its first subsequent selection.  Then (kappa_0=kappa_h=a), with no
intermediate (a), so ([0,h]) is a consecutive omitted-coordinate
return in the particle PBBS.  Since the final entrant is a different
particle, (h<t).

At the final return, Corollary 14.2 gives (kappa_t=b), and

\[
 \lambda_t=x_b(t)+1=u.
\]

Thus, immediately before the time-(t) update,

\[
 x_b(t)=u-1=x_a(0).                                 \tag{6.2}
\]

Every selection of (b) increases its integer-lifted position by exactly
one, and no other update changes it.  Because (t<2r+1), no particle can
make a full physical circuit inside the interval, so (6.1)--(6.2) imply
that (b) was selected exactly (Delta) times before time (t), and once
more at time (t).  Consecutive selection times of the same coordinate are
consecutive omitted-coordinate returns in the particle PBBS.  Hence the
(Delta+1) selections yield (Delta) such return intervals.  Since
(a\ne b), at least one is distinct from the (a)-return. \(\square\)

### Lemma 6.2 (exact terminal inverse-slot spacing)

Normalize the state as \(0D\), and write the nonempty pruned core as
\(E=e_1\cdots e_{2d}\).  In the plane-tree inverse construction of
Section 2, let \(z\) be the number of free new leaf peaks placed in the
terminal root corner, after the last core letter \(e_{2d}\).  Then

\[
 \boxed{\Delta=2z+1.}                               \tag{6.3}
\]

In particular (z=0) is precisely the physically adjacent case, while
(z\ge1) forces at least four shorter return occurrences in the pruned
window: the (a)-return and at least three (b)-returns.

#### Proof

Every inverse expansion has the unique contour form

\[
 D=(10)^{z_0}e_1(10)^{z_1}\cdots
   e_{2d}(10)^{z_{2d}}.
\]

The relevant variable is \(z=z_{2d}\).  Since every nonempty Dyck word
ends in zero, the physical segment from the last core letter to the leading
unmatched zero is

\[
 0(10)^z0.
\]

The equality edge entering the first zero is particle \(b\); the equality
edge entering the final zero is the distinguished particle \(a\); and all
intermediate edges alternate.  Their lifted edge coordinates are therefore
separated by exactly \(2z+1\).  Lemma 6.1 then gives \(2z+1\)
predecessor-return intervals plus the leader return, hence at least
\(2z+2\) child occurrences. \(\square\)

The terminal root corner is always noncompulsory for a nonempty core.
For a fixed core \(E\), the \(z=0\) part of its inverse fibre is exactly
(2.3), while the \(z\ge1\) part is the difference between (2.2) and (2.3).
Thus every parent return obeys the exact dichotomy

\[
\begin{array}{c|c|c}
\text{inverse slot}&\text{fibre fraction}&
   \text{short returns forced in the core window}\\ \hline
z=0&\displaystyle {2d\over r+d-k}&\ge2\\[2mm]
z\ge1&\displaystyle 1-{2d\over r+d-k}&\ge4.
\end{array}                                         \tag{6.4}
\]

More precisely, fixing the terminal occupancy to equal \(z\) leaves

\[
 \binom{r+d-k-z-1}{2d-1}
\]

inverse expansions.  Thus the dynamics prescribes an exact Pascal slot,
not merely the alternatives \(z=0\) and \(z\ge1\).

This is a genuine branching constraint, not merely the height bound.
However, it is not yet a Catalan estimate.  Distinct parent preimages of one
core can induce the same child return occurrences, and descendant branches
from the same time window can merge after further pruning.  A proof of
\((\mathrm{RP}_A)\) must quantify that merging, or show that repeated
selection of the (z=0) branch has sufficiently small inverse-fibre mass.

## 7. Two endpoint chains survive repeated pruning

Although the full binary descendant family can merge, two canonical
lineages cannot: always take the leader child at the left endpoint and the
predecessor child at the right endpoint.

Let an original return occupy the PBBS time interval $[0,t]$.  Define the
pruning tower

\[
 D^{(0)}=D,\qquad D^{(j+1)}=\partial D^{(j)},
 \qquad r_j=\tfrac12|D^{(j)}|.                     \tag{7.1}
\]

Peak defect, and hence $r_{j+1}$, is constant along the whole PBBS orbit
of $D^{(j)}$, because the equality particles persist.  Thus pruning
commutes with following the time interval $[0,t]$ in the sense supplied by
Theorem 14.1.

### Theorem 7.1 (two-sided endpoint return chains)

For every $j\ge1$ for which

\[
 2r_{j-1}+1>t,                                      \tag{7.2}
\]

the level-$j$ PBBS contains two distinct consecutive omitted-coordinate
returns

\[
 I_j^L=[0,h_j],\qquad I_j^R=[s_j,t],               \tag{7.3}
\]

with

\[
 0<h_j<t,\qquad0<s_j<t.                            \tag{7.4}
\]

Moreover the left gaps and right gaps each drop by at least two at every
further pruning step on which (7.2) remains valid.

#### Proof

At level zero use the given parent return.  Apply Lemma 6.1.  Its leader
child is a consecutive return beginning at time zero; call it $I_1^L$.
Its predecessor child has a last consecutive return ending at time $t$;
call it $I_1^R$.  They have different coordinate labels, so they are
distinct.

Now apply the same construction to $I_j^L$, always retaining its leader
child.  Because the child return is strictly shorter and has the same left
endpoint, this gives $I_{j+1}^L=[0,h_{j+1}]$ with
$h_{j+1}\le h_j-2$.  Apply the construction to $I_j^R$ and retain its
last predecessor child.  It has the same right endpoint and strictly
shorter odd gap, so $I_{j+1}^R=[s_{j+1},t]$ with
$t-s_{j+1}\le t-s_j-2$.

Condition (7.2) is exactly what permits the order-preserving integer lift
used in Lemma 6.1 at level $j-1$.  The equality-particle renormalization
identifies the level-$(j+1)$ time evolution with the PBBS evolution of
$D^{(j+1)}$, completing the induction. \(\square\)

The two lineages in (7.3) are endpoint-anchored, so no child-merging
argument can identify them with one another.  Full binary growth is not
claimed: interior descendants from different branches may coincide.

This gives a sharper necessary class than bounded height.  Define
$\mathcal B_g(r)$ to consist of roots whose entire pruning tower, through
the first level reached from a core of circumference greater than $g$,
carries the two endpoint chains (7.3).
Then

\[
 \boxed{\mathcal R_g(r)\subseteq\mathcal B_g(r).}  \tag{7.5}
\]

A Catalan estimate

\[
 |\mathcal B_{2A\sqrt r+1}(r)|
 =o_A\!\left(\frac{\operatorname{Cat}_r}{r}\right) \tag{7.6}
\]

would prove the total-root form of $\mathrm{RP}_A$.  Unlike the one-sided
height constraint, (7.5) simultaneously constrains both temporal endpoints
at every surviving pruning level.  Establishing (7.6), or finding a
Catalan-scale counterfamily inside $\mathcal B_g(r)$, is now the precise
iterated-core problem.
