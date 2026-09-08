# Priority ladders: exact residual degrees and an owner-scale all-row bite

Date: 2026-07-25

Method: pure mathematics only.  No computation, solver, web input, or
fixed-uniformity matching theorem is used.

## 0. Outcome

Use the deterministic exactly-rainbow gap-permutation catalogue from
`MATH_ATTACK_H_DETERMINISTIC_CARRIER_ROTOR_TRAJECTORIES_20260725.md`.
Write

\[
 W=\binom{2m}{m},\qquad M=m+H,\qquad
 N=\binom{2m}{M},\qquad R_q=\binom{2m}{m-q},
\tag{0.1}
\]

and

\[
 \lambda_q={W\over R_q},\qquad
 c_q=\min\left\{M,\left\lfloor{R_q\over N}\right\rfloor\right\},
 \qquad d_q=M-c_q.
\tag{0.2}
\]

The first conclusion is an exact residual-degree theorem.  If some row
targets have already been used, then every phase of a fixed base trajectory
has a first blocked depth.  If

\[
 B_q=\#\{\hbox{phases first blocked at depth at most }q\},
\tag{0.3}
\]

then a common priority order exists if and only if

\[
 \boxed{B_q\le d_q\quad(1\le q\le Q).}
\tag{0.4}
\]

Moreover, the number of surviving priorities is exactly

\[
 \boxed{
 \Pi=(M-B_Q)!\prod_{q=1}^Q
 { (d_q-B_{q-1})!\over(d_q-B_q)!}.}
\tag{0.5}
\]

There is also an exact one-phase update law.  Put

\[
 n_q=B_q-B_{q-1},\qquad \sigma_q=d_q-B_q,
\tag{0.6}
\]

and regard an unblocked phase as having class (Q+1), with

\[
 n_{Q+1}=M-B_Q.
\]

If one phase's first-block class moves from (r) down to (s<r), then

\[
 \boxed{
 {\Pi'\over\Pi}
 ={\sigma_s\over \sigma_r+n_r}
  \prod_{q=s+1}^{r-1}{\sigma_q\over\sigma_q+n_q},}
\tag{0.7}
\]

where for (r=Q+1) the denominator in front is (n_{Q+1}).  Formula
(0.7) is the exact priority-aware residual recurrence which was absent from
the previous nibble audits.

The second conclusion is positive.  Sacrifice only (o(W)) additional
scalar claims and replace (d_q) by

\[
 \bar d_q=\min\{M,\max(d_q,\lceil C_m\Lambda_q\rceil)\},
 \qquad
 \Lambda_q=\sum_{r=1}^q\lambda_r,
 \qquad C_m=(\log m)^2.
\tag{0.8}
\]

Then one can select, in a single semi-random round,

\[
 \boxed{(\theta-\theta^2-o(1)){N\over M}}
\tag{0.9}
\]

carrier trajectories whose owners and every claimed signed flag through
depth (Q) are mutually disjoint.  Here (0<\theta<1) is arbitrary and
fixed.  This is an **owner-scale** bite.  The ordinary decorated-edge bite
has only order

\[
 {N\over K_Q}=\Theta\!\left({N\over M\sqrt m}\right),
\]

so the priority ladder gives the full factor-(\Theta(\sqrt m)) gain in a
rigorous first round.

There is a stronger grid-rescaled form.  Split banded trajectories into
return-free geodesic chunks of length $g\sim H$, at reset cost $o(W)$.
With another $o(W)$-cost deadline enlargement, one all-row bite covers

\[
 \boxed{{1-o(1)\over m^{2/3}\omega_m\log^2m}\,W}
\tag{0.10a}
\]

middle owners, for an arbitrarily slow suitable $\omega_m\to\infty$.
Thus a regenerating grid residual would need only

\[
 m^{2/3}\omega_m\log^2m=o(m)
\]

rounds, rather than $m$ rounds.  The exact grid invariant is clearance
majorization; its sharp higher-overlap enemy is a shared product rectangle.

These results do not yet iterate to a near-perfect common matching.  After
earlier rounds have used targets, (0.5)--(0.7) show that the next round is
controlled by the **pathwise deadline slack profile**

\[
 \sigma_q(P)=\bar d_q-B_q(P),
\tag{0.10}
\]

not by the row densities alone.  In particular (d_1\le2) before the
harmless slack enlargement.  A row-quasirandom residual consumes shallow
deadline slack after only a vanishing selected fraction.  Thus common
priority symmetry really does improve the one-bite scale, but it does not
by itself prove residual closure.  The remaining theorem is an aligned
deadline-slack regeneration statement for the deterministic base-path
catalogue.

## 1. Column heights and first-block deadlines

Fix one unprioritized exactly-rainbow base trajectory

\[
 P=(\omega_t:t\in\mathbb Z_M).
\]

At phase (t), write its signed flags as

\[
 F^-_q(t),\quad F^+_q(t)\qquad(1\le q\le Q).
\]

Let (Z_q^\pm) be the targets already forbidden in the corresponding
signed row.  Owners are always claimed, so a base trajectory having a
forbidden owner is discarded before priorities are considered.

For a phase whose owner is available, define its first blocked depth

\[
 r(t)=\min\{q:F^-_q(t)\in Z_q^-\text{ or }
                    F^+_q(t)\in Z_q^+\},
\tag{1.1}
\]

with (r(t)=Q+1) if the set is empty.

Let (j(t)\in[M]) be the ordinary priority rank of phase (t), and put

\[
 s(t)=M-j(t)+1.
\tag{1.2}
\]

Thus small (s) means low priority.  A phase is claimed at signed depth
(q) precisely when (j(t)\le c_q), equivalently

\[
 s(t)>d_q.
\tag{1.3}
\]

Consequently a phase first blocked at depth (r\le Q) is legal precisely
when

\[
 s(t)\le d_r.
\tag{1.4}
\]

For an unblocked phase put (d_{Q+1}=M), so (1.4) remains valid.  The
priority problem is therefore the elementary problem of bijectively
assigning the slots (1,\ldots,M) to unit jobs with nested deadlines
(d_{r(t)}).

The multiset of physical column heights is worth recording.  Exactly

\[
 d_1
\]

columns have height zero, exactly

\[
 d_{q+1}-d_q=c_q-c_{q+1}
\]

columns have height (q), and (c_Q) columns have height (Q).  This is
the precise sense in which the (2Q) rows form one ladder rather than
independent target slots.

## 2. Exact priority enumeration

Put

\[
 n_q=\#\{t:r(t)=q\},\qquad
 B_q=\sum_{a=1}^q n_a,
\tag{2.1}
\]

and (n_{Q+1}=M-B_Q).

### Theorem 2.1 (deadline Hall criterion and exact degree)

There is a legal common priority order if and only if

\[
 B_q\le d_q\qquad(1\le q\le Q).
\tag{2.2}
\]

When (2.2) holds, its exact number is (0.5).

#### Proof

The phases with first-block depth at most (q) must all be assigned one of
the first (d_q) reverse-priority slots.  This proves necessity.

For sufficiency, sort the phases in nondecreasing order of their deadline.
The (n_q) phases of class (q) are assigned after exactly (B_{q-1})
earlier phases.  Their number of injective choices is

\[
 (d_q-B_{q-1})_{n_q}
 ={(d_q-B_{q-1})!\over(d_q-B_q)!}.
\tag{2.3}
\]

The (M-B_Q) unblocked phases may then be assigned the remaining slots in
((M-B_Q)!) ways.  Multiplication gives (0.5).  Every factor is positive
exactly under (2.2).  \(\square\)

This theorem gives the exact residual tag degree.  If
\({\cal B}(U)) is the unprioritized base-path catalogue above carrier
(U), then

\[
 \boxed{
 D_U(Z)=\sum_{P\in{\cal B}(U):\,P\text{ owner-available}}\Pi_Z(P).}
\tag{2.4}
\]

No product-independence approximation occurs in (2.4).

### Theorem 2.2 (one-phase hazard multiplier)

Suppose one new forbidden target changes one phase's first-block class from
(r) to (s<r).  If both the old and new deadline systems are feasible,
then (0.7) holds.

#### Proof

Use the factorial formula (0.5).  At (q=s), only (B_s) increases, and
the resulting ratio is

\[
 d_s-B_s=\sigma_s.
\]

For (s<q<r), both (B_{q-1}) and (B_q) increase.  The ratio of the
new (q)-factor to the old one is

\[
 {d_q-B_q\over d_q-B_{q-1}}
 ={\sigma_q\over\sigma_q+n_q}.
\]

At (q=r\le Q), only (B_{r-1}) increases, giving

\[
 {1\over d_r-B_{r-1}}={1\over\sigma_r+n_r}.
\]

If (r=Q+1), the last factorial changes from
((M-B_Q)!) to ((M-B_Q-1)!), giving (1/n_{Q+1}) instead.  Multiplying
the factors proves (0.7).  \(\square\)

For several new blockers one applies Theorem 2.2 successively.  Equivalently,

\[
 {\Pi_{Z\cup E}(P)\over\Pi_Z(P)}
 =\Pr_{\pi\text{ uniform among old legal priorities}}
   (\pi\text{ avoids every new target of }E).
\tag{2.5}
\]

Thus the exact residual recurrence after adjoining a decorated trajectory
(E) is

\[
 \boxed{
 D_U(Z\cup E)
 =\sum_{P\in{\cal B}(U):\,P\text{ owner-available after }E}
   \Pi_Z(P)\,H_Z(P,E),}
\tag{2.6}
\]

where (H_Z(P,E)) is the multiplier in (2.5), computable by (0.7).
Equations (2.4) and (2.6) are the desired ladder-aware residual-degree
recurrences.

### 2.3 Geodesic-grid form and the exact defect

On a return-free geodesic segment write

\[
 G_{i,j}=C\cup\{A_{i+1},\ldots,A_g\}
             \cup\{B_1,\ldots,B_j\},
 \qquad X_t=G_{t,t}.
\tag{2.7}
\]

With the physical phase convention of the rotor identities,

\[
 L_q(t)=G_{t+q,t},\qquad U_q(t)=G_{t-q,t}.
\tag{2.8}
\]

(The equivalent cell $G_{t,t+q}$ is $U_q(t+q)$, not $U_q(t)$.)  Thus all
signed flags belonging to phase $t$ lie in one vertical grid column
$j=t$.  A priority of height $h(t)$ claims the centered vertical segment

\[
 \{G_{t-q,t}:0\le q\le h(t)\}
 \cup
 \{G_{t+q,t}:0\le q\le h(t)\}.
\tag{2.9}
\]

For a residual grid, let $a_t$ be the largest radius for which every cell
of (2.9) through radius $a_t$ is unused.  Then Theorem 2.1 has the
equivalent two-dimensional boundary form

\[
 \boxed{\#\{t:a_t\ge q\}\ge c_q\quad(1\le q\le Q).}
\tag{2.10}
\]

In other words, after sorting, the available-clearance profile must
majorize the prescribed height profile.  The optimal priority is simply
the monotone pairing of largest demanded heights with largest available
clearances.  This is the exact product-grid invariant suggested by the
geodesic representation.

There is also an exact deficiency formula.  Put

\[
 \delta(P)=\max_{q\le Q}(B_q(P)-d_q)_+.
\tag{2.11}
\]

Then $\delta(P)$ is the minimum number of whole phase columns which must be
removed to make the remaining deadline system feasible.  The lower bound
is immediate.  For the upper bound, remove the $\delta(P)$ phases with
smallest first-block depths.  Every prefix count becomes

\[
 \max\{B_q(P)-\delta(P),0\}\le d_q.
\]

The signed flags of one phase concatenate through its owner into one chain,

\[
 L_Q\subset\cdots\subset L_1\subset X
 \subset U_1\subset\cdots\subset U_Q.
\]

Hence each removed phase contributes at most one nested flag-chain string.
Therefore the **withheld duplicate-occurrence strings** of a
family of paths have a chain cover of size at most

\[
 \boxed{\sum_P\delta(P),}
\tag{2.12}
\]

and hence antichain width at most the same number.  This is a structured
donor certificate, not yet a chain cover of the actual physical holes.
The targets in these withheld strings may already be covered by another
occurrence, while losing their distinct-claim slots can leave unrelated
targets elsewhere in the row uncovered.  Passing from (2.12) to a repair
requires an integral donor-to-hole braid or an additional alignment
theorem.

Formula (2.10) identifies what a successful product-grid ordering would
have to preserve.  It is not automatic: two different geodesic grids can
meet in crossing rectangles, so removing a centered strip in one grid need
not leave a monotone clearance boundary in another.  The boundary
majorization, rather than mere cell density, is the residual invariant.

There is, however, a useful exact pruning lemma for these rectangles.

### Lemma 2.3 (large grid overlap contains a product rectangle)

Let ${\cal G}$ and ${\cal G}'$ be two full length-$g$ geodesic grids of
the form (2.7), and let ${\cal L}={\cal G}\cap{\cal G}'$ as a family of
physical Boolean sets.  Then ${\cal L}$ is a sublattice of each product of
two chains.  If ${\cal L}$ has width $w$, it contains a compressed
$w\times w$ product subgrid.  Consequently, if the two grids share no
compressed $s\times s$ subgrid, then

\[
 \boxed{|{\cal G}\cap{\cal G}'|\le(s-1)(2g+1).}
\tag{2.13}
\]

#### Proof

Each full grid is closed under physical intersection and union:

\[
 G_{i,j}\cap G_{k,l}=G_{\max(i,k),\min(j,l)},\qquad
 G_{i,j}\cup G_{k,l}=G_{\min(i,k),\max(j,l)}.
\]

Therefore their intersection is a sublattice.

Take an antichain of size $w$ in one grid-coordinate system and write its
points as

\[
 (x_1,y_1),\ldots,(x_w,y_w),
 \qquad x_1<\cdots<x_w,\quad y_1<\cdots<y_w.
\]

For $a<b$, the meet of points $a,b$ is $(x_b,y_a)$ and their join is
$(x_a,y_b)$.  Hence closure under meet and join supplies every point
$(x_a,y_b)$, $1\le a,b\le w$, which is a compressed $w\times w$ subgrid.

If no $s\times s$ subgrid is shared, the width is at most $s-1$.  The
height of a $(g+1)\times(g+1)$ product grid is $2g+1$.  Dilworth's theorem
then gives (2.13).  \(\square\)

More relevantly for deadlines, restrict the common claimed cells to the
ranks $m-q,\ldots,m+q$.  Each Boolean chain contains at most one set of
each cardinality.  Hence a nonconflicting grid pair can block at most

\[
 \boxed{(s-1)(2q+1)}
\tag{2.14}
\]

phase columns through depth $q$ (and possibly fewer, because several
common cells can lie in one phase column).  Thus large *chain-like*
overlaps are compatible with the deadline budget; the dangerous objects
are the wide product rectangles.

Thus one possible route to PDRC is to declare every shared polylogarithmic
product rectangle an additional conflict.  Nonconflicting grid pairs would
then have only $O(gs)$ common physical cells and only $O(sq)$ blockers
through depth $q$.  What is still needed is a
degree estimate showing that these extra rectangle conflicts are sparse
enough in the symmetric catalogue, together with control of scattered
intersections under repeated bites.

## 3. The first-shadow bottleneck

The exact first-row slack is uniformly bounded.

### Lemma 3.1

For all sufficiently large (m),

\[
 \boxed{d_1\le2.}
\tag{3.1}
\]

#### Proof

At even dimension (2m),

\[
 \lambda_1={W\over R_1}={m+1\over m}.
\]

The crossing definition gives \(\lambda_H\ge M\), and therefore

\[
 {R_1\over N}={\lambda_H\over\lambda_1}
 \ge {M m\over m+1}>M-2.
\]

Taking the floor and then the cap at (M) gives (c_1\ge M-2).  Hence
(d_1=M-c_1\le2).  \(\square\)

Thus one pre-existing depth-one collision multiplies the initial priority
degree by at most

\[
 {d_1\over M}=O(M^{-1}),
\tag{3.2}
\]

and three distinct blocked phase columns kill it completely.  More
generally (0.7) shows that priority symmetry is controlled by the entire
slack vector \((\sigma_q)\), not by the total number of unused targets in
each row.

This already rules out a scalar row-density closure argument.  Two
residuals can have the same row cardinalities while one places its used
targets in at most (d_q) phase columns of a base path and the other
places them in more than (d_q) columns.  The first residual contributes
positively to (2.4); the second contributes zero.  Any iterative theorem
must preserve aligned deadline slack, not merely rowwise quasirandomness.

There is a sharper first-band interpretation.  If a base path contributes
positively to the original residual degree, then at least (M-2) of its
phase columns have both their lower and upper depth-one targets unused.
After the slack enlargement in the next section, the corresponding number
is still

\[
 M-O(\log^2m).
\tag{3.3}
\]

Thus an iteration down to (o(N)) active carrier tags necessarily
contains, already in its first row, a residual two-sided-rainbow path
packing: almost every surviving path must lie almost wholly in the unused
lower and upper first shadows.  Priority orders cannot manufacture that
packing; they can discard only (o(M)) bad first-row phases.  Their real
gain is that, once this shallow avoidance is supplied, the higher rows can
share the same discarded phase budget through the deadline inequalities.

## 4. An (o(W))-cost slack enlargement

The bounded first-row capacity obstructs even one owner-scale random bite.
It can be enlarged at negligible total cost.

Put

\[
 C_m=(\log m)^2,
 \qquad \Lambda_q=\sum_{r=1}^q\lambda_r,
\tag{4.1}
\]

and define \(\bar d_q\) and \(\bar c_q=M-\bar d_q\) by (0.8).  Both
\(d_q\) and \(\Lambda_q\) are nondecreasing, so the new claims remain
nested.

### Lemma 4.1 (the enlargement is scalar-negligible)

\[
 \boxed{
 \sum_{q=1}^Q(\bar d_q-d_q)=o(M).}
\tag{4.2}
\]

Consequently replacing (c_q) by \(\bar c_q\) on both signed sides adds
only (o(W)) to the scalar leave.

#### Proof

The crossing estimate gives

\[
 {\lambda_H\over M}=1+O(H/m).
\tag{4.3}
\]

For (q\le\sqrt m), the central-binomial expansion gives

\[
 \lambda_q=\exp(q^2/m+O(q/m+q^3/m^2)),
 \qquad \Lambda_q=O(q).
\tag{4.4}
\]

Since (c_q\le\lambda_H/\lambda_q), (4.3)--(4.4) imply

\[
 d_q\ge c q^2-C H
\tag{4.5}
\]

for absolute positive constants (c,C).  Hence
(d_q<C_m\Lambda_q) in this range only when

\[
 q=O(\sqrt H+C_m).
\]

The contribution of those depths is at most

\[
 O\!\left(C_m\sum_{q\le C(\sqrt H+C_m)}q\right)
 =O(C_mH+C_m^3)=o(m).
\tag{4.6}
\]

For \(\sqrt m\le q\le Q\), one has (d_q=\Omega(m)).  Also

\[
 \Lambda_q\le q\lambda_q\le Q\lambda_Q,
\]

while

\[
 Q=\sqrt{m(\log\log m+\gamma)},\qquad
 \lambda_Q=\log m\,e^{\gamma+o(1)}=\log^{1+o(1)}m.
\]

Therefore

\[
 C_m\Lambda_q\le C_mQ\lambda_Q=o(m),
\]

so no enlargement occurs in this range.  This proves (4.2).

There are (N) carriers and two signed rows per depth.  The extra scalar
leave is

\[
 2N\sum_q(\bar d_q-d_q)=o(NM)=o(W).
\]

\(\square\)

## 5. A rigorous owner-scale all-row bite

Discard priorities temporarily.  Above every carrier choose uniformly one
base trajectory from the symmetric deterministic catalogue, independently
between carriers.  Activate each carrier independently with probability

\[
 \alpha={\theta\over M},\qquad 0<\theta<1.
\tag{5.1}
\]

Every base trajectory is internally injective at every signed row through
depth (Q).

The raw global load of a fixed target in either signed depth-(q) row is

\[
 \mu_q={MN\over R_q}=\rho\lambda_q,
 \qquad \rho={MN\over W}=1-o(1).
\tag{5.2}
\]

The owner load is \(\rho\le1\).

For an active trajectory (P), let (B_q(P)) be the number of its phase
columns which, in at least one signed row of depth at most (q), use a
target also used by another active trajectory.

### Lemma 5.1 (aggregate collision prefixes)

\[
 \boxed{
 \mathbb E\sum_{P\ {\mathrm{active}}}B_q(P)
 \le 2\theta\rho\,\alpha N\Lambda_q.}
\tag{5.3}
\]

#### Proof

Fix one signed depth-(r) row.  For a target (S), let (L_S) be its
active load.  If (p_{U,S}) is the probability that the random base path
above (U) contains (S), then

\[
 \sum_U p_{U,S}=\mu_r.
\]

Independence between carrier choices gives

\[
 \mathbb E\binom{L_S}{2}
 \le {\alpha^2\mu_r^2\over2}.
\]

Because internal row injectivity makes all occurrences belong to distinct
paths,

\[
 L_S\mathbf1_{\{L_S\ge2\}}\le2\binom{L_S}{2}.
\]

Summing over the (R_r) targets gives expected involved occurrences at
most

\[
 \alpha^2R_r\mu_r^2
 =\alpha^2NM\mu_r.
\tag{5.4}
\]

Sum (5.4) over both signs and (r\le q), use
\(\mu_r=\rho\lambda_r\) and \(\alpha M=\theta\), and note that counting
involved occurrences only overcounts the distinct phase columns in
(B_q(P)).  This gives (5.3).  \(\square\)

### Lemma 5.2 (few deadline-bad active paths)

The expected number of active paths for which

\[
 B_q(P)>\bar d_q
\tag{5.5}
\]

at some depth (q\le Q) is (o(\alpha N)).

#### Proof

Since \(\bar d_q\ge C_m\Lambda_q\), it is enough to control
(B_q(P)>C_m\Lambda_q).  Partition the increasing sequence
\((\Lambda_q)\) into dyadic blocks.  There are

\[
 O(\log\Lambda_Q)=O(\log m)
\]

blocks.  If a path violates the inequality at a depth in one block, then
at the last depth (q_j) of that block it satisfies

\[
 B_{q_j}(P)>{C_m\over2}\Lambda_{q_j}
\]

after an immaterial adjustment of the first block.  Markov's inequality
and (5.3) show that the expected number caught by one block is at most

\[
 O(\theta/C_m)\,\alpha N.
\]

Summing over the blocks gives

\[
 O\!\left({\theta\log m\over C_m}\right)\alpha N
 =o(\alpha N).
\]

\(\square\)

### Theorem 5.3 (owner-scale all-row bite)

For every fixed \(0<\theta<1\), there is a family of at least

\[
 \boxed{(\theta-\theta^2-o(1)){N\over M}}
\tag{5.6}
\]

base trajectories and one priority order on every chosen trajectory such
that

1. all middle owners are mutually distinct;
2. all claimed lower targets are mutually distinct in every depth
   (q\le Q);
3. all claimed upper targets are mutually distinct in every depth
   (q\le Q);
4. the claim counts are the nested counts \(\bar c_q\).

#### Proof

Let (A) be the number of active paths.  The expected value is

\[
 \mathbb EA=\alpha N={\theta N\over M}.
\]

Let (C_0) be the number of pairs of active paths sharing a middle owner.
The owner version of the calculation in Lemma 5.1 gives

\[
 \mathbb EC_0\le{W\alpha^2\rho^2\over2}
 \le(1+o(1)){\theta^2N\over2M}.
\tag{5.7}
\]

Delete both endpoints of every such pair.  This deletes at most (2C_0)
paths and makes all owners distinct.

Before that deletion, also mark every path which violates (5.5).  By
Lemma 5.2 there are (o(\alpha N)) such paths in expectation.  Therefore
some outcome leaves at least

\[
 A-2C_0-\#\{\hbox{deadline-bad paths}\}
 \ge(\theta-\theta^2-o(1)){N\over M}
\tag{5.8}
\]

paths.

Deleting paths can only remove flag collisions.  For each surviving path,
declare a phase blocked at its first signed depth at which any of its raw
targets is duplicated among the survivors.  Its prefix counts satisfy

\[
 B_q(P)\le\bar d_q.
\]

Theorem 2.1 supplies a priority order in which that phase has column height
strictly below its first duplicated depth.  Choose such an order separately
on every surviving path.

If a target is duplicated at depth (q), every one of its occurrences is
in a phase whose first duplicated depth is at most (q).  Hence every one
of those phases has height below (q), and none of the duplicate
occurrences is claimed.  All claimed targets are therefore mutually
distinct, simultaneously in every signed row.  Owners were already made
distinct.  This proves the theorem.  \(\square\)

The leading constant in (5.6) is not optimized.  The important point is
the scale (N/M), rather than (N/(M\sqrt m)).

The deadline-bad paths may alternatively be retained as structured reserve
donors.  By (2.11), their minimum total deleted-column defect is

\[
 D=\sum_{P\ {\mathrm{active}}}\delta(P)
 \le\sum_{P\ {\mathrm{active}}}B_Q(P).
\tag{5.9}
\]

Lemma 5.1 and the endpoint estimate

\[
 \Lambda_Q=\Theta\!\left({m\over Q}\lambda_Q\right)
\]

give

\[
 \boxed{
 \mathbb ED
 =O\!\left({N\Lambda_Q\over M}\right)
 =O\!\left({N\lambda_Q\over Q}\right)
 =o(W/Q).}
\tag{5.10}
\]

Hence some owner-scale bite has a collision-induced **donor** width
$o(W/Q)$ by (2.12).  It does not by itself bound the width of the actual
new physical holes.  This is a one-bite assertion.  Summing it naively over
$O(M)$ bites gives only $O(W\lambda_Q/Q)$, so a full proof still needs
deadline regeneration, cancellation, or a joint flagged reserve rather
than independent per-bite repair.

## 6. Exact residual recurrence and the iteration gate

Theorem 5.3 starts from an empty forbidden family.  In a later round, a
base path (P) already has first-block counts (B_q(P)) and slacks

\[
 \sigma_q(P)=\bar d_q-B_q(P).
\tag{6.1}
\]

A new collision moving one phase from class (r) to (s) consumes one
unit of every prefix slack from (s) through (r-1), and its exact degree
cost is (0.7).  This gives a natural residual closure property.

### Definition 6.1 (priority-deadline residual closure, PDRC)

A residual catalogue has PDRC if, for every active carrier tag:

1. the weighted degree (2.4) is within (1+o(1)) of one common value;
2. all but an (o(1)) fraction of that weight lies on base paths satisfying
   \[
    \sigma_q(P)\ge C_m\Lambda_q\qquad(q\le Q);
   \tag{6.2}
   \]
3. under the corresponding weighted base-path laws, every owner has
   normalized load at most (1+o(1)), and every raw signed depth-(q)
   target has normalized load at most ((1+o(1))\rho\lambda_q).

The proof of Theorem 5.3, with (0.7) used to update the old deadlines,
gives the following conditional statement.

### Corollary 6.2 (conditional iteration)

If PDRC is restored after every bite while at least (uN) carrier tags
remain, then one owner-scale bite matches

\[
 (\theta-\theta^2-o(1)){uN\over M}
\]

additional tags.  If PDRC persists down to (u=\eta_m=o(1)) for

\[
 O(M\log(1/\eta_m))
\]

bites, the resulting common matching leaves (o(N)) carrier tags.

The hypothesis is deliberately explicit.  It is not implied by initial
catalogue symmetry or by the separate-row Hall inequalities.

Indeed, before the slack enlargement the first row has (d_1\le2).  In a
row-quasirandom residual using a fraction (f) of the first-row targets,
a typical raw path has order (fM) blocked first-row phase columns, while
feasibility permits only (O(1)).  Even after the (o(W))-cost
enlargement, the permitted number is only (C_m\lambda_1=\log^2m(1+o(1))).
Thus a row-quasirandom iteration loses (6.2) after a selected fraction

\[
 f\gg {\log^2m\over m}.
\tag{6.3}
\]

Reaching (1-o(1)) requires the unused targets and the surviving base
paths to become highly aligned.  Formula (0.7) identifies exactly what
must be regenerated: positive pathwise deadline slack at every prefix.

## 7. Verdict

The common priority order does materially improve the mathematics:

* it is exactly a laminar deadline system, with the closed degree formulas
  (0.5) and (0.7);
* after an (o(W))-cost redistribution of claims, it absorbs all flag
  collisions in an owner-scale sparse round;
* this gives a rigorous factor-(\Theta(\sqrt m)) improvement over the
  ordinary augmented-edge bite.

But priority symmetry does not automatically control all depths through
(Q).  The exact obstruction is no longer an unspecified high codegree.
It is loss of the prefix slack profile

\[
 \boxed{\sigma_q(P)=\bar d_q-B_q(P).}
\]

The remaining common-matching theorem can now be stated sharply:

> prove that the deterministic gap-permutation base catalogue regenerates
> PDRC under the owner-scale bite, or construct an equivalent global
> selection in which all but (o(N)) carrier tags retain enough aligned
> deadline slack.

That regeneration statement is not proved here, so coefficient one is not
claimed.

## 8. Geodesic-chunk rescaling

The product-grid form suggests splitting a banded gap trajectory into
return-free chunks.  Take

\[
 g=(1-o(1))H,
\tag{8.1}
\]

shorter than every residence and nonresidence run; for the adjacent-switch
catalogue one may take (g=H-Q-O(1)).  Every such chunk is a Johnson
geodesic and has the full grid representation (2.7).  Splitting all
carriers creates

\[
 T=(1+o(1)){W\over g}
\tag{8.2}
\]

labelled chunk tags.  The reset cost is

\[
 O(QT)=O(QW/g)=o(W),
\]

and the discarded carrier remainders cost (O(gW/m)=o(W)).

The calibrated claims per chunk are now

\[
 c_q^{(g)}=\min\left\{g,\left\lfloor{R_q\over T}\right\rfloor\right\},
 \qquad d_q^{(g)}=g-c_q^{(g)}.
\tag{8.3}
\]

Choose any sufficiently slow \(\omega_m\to\infty\), and put

\[
 \varepsilon_m={g\over m^{2/3}\omega_m},
 \qquad L_m=(\log m)^2,
\tag{8.4}
\]

\[
 \bar d_q^{(g)}=\min\left\{g,
  \max\left(d_q^{(g)},
   \left\lceil\varepsilon_m\Lambda_q\right\rceil\right)
 \right\},
 \qquad \bar c_q^{(g)}=g-\bar d_q^{(g)}.
\tag{8.5}
\]

### Lemma 8.1 (chunk slack is negligible)

\[
 \boxed{
 \sum_{q=1}^Q(\bar d_q^{(g)}-d_q^{(g)})=o(g).}
\tag{8.6}
\]

#### Proof

Write \(\rho_g=gT/W=1-O(H/m+g/m)=1-o(1)\).  Then

\[
 {R_q\over T}={g\over\rho_g\lambda_q}.
\tag{8.7}
\]

For (q\le\sqrt m), the same expansion as in (4.4) gives

\[
 d_q^{(g)}
 \ge {g\over m}(c q^2-C H)-1,
 \qquad \Lambda_q=O(q).
\tag{8.8}
\]

Consequently (8.5) can enlarge the integer deadline only for

\[
 q=O\!\left(\sqrt H+{\varepsilon_m m\over g}\right),
\]

apart from harmless rounding.  The total rounding contribution is

\[
 O\!\left(\sqrt H+{\varepsilon_m m\over g}\right)=o(g).
\]

The remaining continuous contribution is bounded by

\[
 O\!\left(\varepsilon_m H
       +{\varepsilon_m^3m^2\over g^2}\right)
 =O\!\left({gH\over m^{2/3}\omega_m}
       +{g\over\omega_m^3}\right)=o(g).
\]

For \(\sqrt m\le q\le Q\), one has (d_q^{(g)}=\Omega(g)), whereas

\[
 \varepsilon_m\Lambda_q
 \le {g\over m^{2/3}\omega_m}Q\lambda_Q=o(g).
\]

This proves (8.6).  Multiplication by (2T) shows that the two signed
scalar claim loss is (o(Tg)=o(W)).  \(\square\)

### Theorem 8.2 (geodesic-grid all-row bite)

Activate every chunk tag with probability

\[
 \alpha={\varepsilon_m\over L_mg}
 ={1\over m^{2/3}\omega_mL_m}.
\tag{8.9}
\]

and choose a uniform symmetric exact-rainbow geodesic chunk above every
activated tag.  There is an outcome containing

\[
 \boxed{(1-o(1))\alpha T}
\tag{8.10}
\]

chunks, together with one priority on every chosen chunk, such that all
owners and all modified claimed signed targets through depth (Q) are
mutually distinct.  The selected chunks cover

\[
 (1-o(1)){W\over m^{2/3}\omega_mL_m}
\tag{8.11}
\]

middle owners.

#### Proof

The raw global target load of a signed depth-(q) set is

\[
 \mu_q^{(g)}={gT\over R_q}=\rho_g\lambda_q.
\tag{8.12}
\]

Repeating Lemma 5.1 with (N,M) replaced by (T,g) gives

\[
 \mathbb E\sum_{P\ {\rm active}}B_q(P)
 \le2\alpha g\rho_g\,\alpha T\Lambda_q
 ={2\varepsilon_m\rho_g\over L_m}\,\alpha T\Lambda_q.
\tag{8.13}
\]

Compare this with the deadline floor
(\varepsilon_m\Lambda_q) in (8.5).  The same dyadic argument as Lemma 5.2
shows that only

\[
 O\!\left({\log m\over L_m}\right)\alpha T=o(\alpha T)
\]

active paths are deadline-bad.

The expected number of active owner-collision pairs is at most

\[
 {W\alpha^2\over2}.
\]

Deleting both endpoints costs, relative to \(\alpha T\), at most

\[
 O\!\left({W\alpha^2\over\alpha T}\right)
 =O(\alpha g)=O(\varepsilon_m/L_m)=o(1).
\]

Thus $(1-o(1))\alpha T$ paths remain owner-disjoint
and deadline-good.  Assign priorities exactly as in Theorem 5.3, hiding
every duplicated raw target.  The claims are then mutually distinct in all
signed rows.  Finally $gT=(1-o(1))W$, which gives (8.11).  \(\square\)

This grid bite has the mesoscopic dynamic scale: if its residual invariant
regenerated, then

\[
 O(m^{2/3}\omega_m\log^2m)=o(m)
\]

successful rounds would cover the middle layer.  Its iteration requires a chunk version of
PDRC.  Lemma 2.3 shows why product-grid rectangles are the relevant
higher-overlap obstruction and suggests declaring shared polylogarithmic
rectangles as extra conflicts.  The missing proof is that this pruning is
degree-negligible and that the clearance-majorization profile (2.10)
regenerates for
$O(m^{2/3}\omega_m\log^2m)$ rounds.

### Proposition 8.3 (the (m^{-2/3}) density ceiling)

The exponent in Theorem 8.2 is the sharp scale for a row-exchangeable
priority-slack bite.  More precisely, suppose a bite of density (\alpha)
is to be absorbed only by lowering the nested claim counts, and suppose
that on a positive proportion of its chunks the collision prefixes obey

\[
 B_q(P)\ge c\alpha gq
\tag{8.14}
\]

for all (q) in a fixed positive subinterval below (\alpha m).  If the
additional scalar claim loss is (o(W)), then

\[
 \boxed{\alpha=o(m^{-2/3}).}
\tag{8.15}
\]

#### Proof

Uniformly for (q=o(\sqrt m)), (8.7) and the central-binomial expansion
give the upper bound

\[
 d_q^{(g)}\le C{g\over m}(q^2+H)+1.
\tag{8.16}
\]

Assume first that (\alpha m/\sqrt H\to\infty), as at the putative
critical scale.  On an interval

\[
 C_1\sqrt H\le q\le c_1\alpha m
\]

with suitable absolute constants, (8.14)--(8.16) force an additional
deadline of at least

\[
 c_2\alpha gq-C_2{gq^2\over m}.
\]

Summing over this interval gives

\[
 \sum_q(\bar d_q^{(g)}-d_q^{(g)})
 \ge c_3g\alpha^3m^2-o(g\alpha^3m^2).
\tag{8.17}
\]

There are (T=(1+o(1))W/g) chunk tags.  Hence the global extra scalar
leave is at least

\[
 (c_3-o(1))W\alpha^3m^2.
\]

For this to be (o(W)), one must have (\alpha^3m^2=o(1)), which is
(8.15).  If (\alpha m=O(\sqrt H)), then

\[
 \alpha=O(\sqrt H/m)=o(m^{-2/3})
\]

at the calibrated (H\sim\sqrt{m\log m}), so the conclusion again holds.
\(\square\)

Thus the (m^{-2/3}) scale is not an arbitrary parameter choice.  It is
the cubic area between the linear collision boundary
(q\mapsto\alpha gq) and the quadratic natural deadline boundary
(q\mapsto gq^2/m).  Passing this scale requires genuine residual
avoidance/alignment, not a larger scalar sacrifice of priority columns.
