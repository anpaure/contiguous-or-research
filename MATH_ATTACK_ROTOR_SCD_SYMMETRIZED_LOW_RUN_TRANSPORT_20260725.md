# Symmetrized rotor--SCD recoloring as exact occurrence transport

Date: 2026-07-25

Pure mathematics only.

## 0. Outcome

Let

\[
 G=S_{2m},\qquad |G|=(2m)!,\qquad
 W=\binom{2m}{m},\qquad M=m+H,
\]

and let \(Q<H\) be the truncated rotor depth.  Fix one integral balanced
top-rooted full-flag resolution \(\mathcal B\), with exactly \(M\) columns
over every top and

\[
 T=M\binom{2m}{M}=W-o(W)
\tag{0.1}
\]

columns in total.  Color its full coordinate orbit by

\[
 \{g\mathcal B:g\in G\}.
\]

The symmetrized double-resolution theorem says that the resulting
occurrence multiset is uniform on exact quotient states and has an
integral legal rotor cycle resolution.  This note solves the associated
run optimization exactly after arbitrary equal-state occurrence
reassignment and re-resolution of the legal successor permutation are
allowed.  A recoloring of one frozen rotor cycle factor is a more
restrictive problem and can only have a larger optimum.

For the \(M\) resolved columns of \(\mathcal B\) at a top \(U\), let
\(p_U^*(\mathcal B)\) be the minimum number of components in a spanning
vertex-disjoint legal rotor path factor.  Then the minimum possible total
number of maximal constant-color runs in the whole symmetrized occurrence
multiset is

\[
 \boxed{
 R_{\rm orb}^*(\mathcal B)
 =|G|\sum_U p_U^*(\mathcal B).}
\tag{0.2}
\]

The upper bound is constructive.  Take optimal path factors in the base
resolution, conjugate them through every color, and use exact uniformity of
the start/end occurrence fibers to splice all open paths by one regular
rotor transport.  Every original path remains a monochromatic interval.
The lower bound holds for every chronology and every equal-state
reassignment, because the runs of one color at one top are themselves a
legal path factor of that color's prescribed state table.

This gives a genuine conditional low-run construction from the new
whole-transversal theorem.  If every top admits a law on legal successor
permutations satisfying the cycle-cylinder bound with parameter
\(\theta_U\), then

\[
 \boxed{
 R_{\rm orb}^*(\mathcal B)
 \le |G|H_M\sum_U\theta_U.}
\tag{0.3}
\]

In particular, uniformly bounded \(\theta_U\) gives

\[
 R_{\rm orb}^*(\mathcal B)
 =O\!\left(|G|{W\log M\over M}\right)
 =o\!\left({|G|W\over Q}\right).
\tag{0.4}
\]

All columns remain in their original color, so every color's exact SCD or
floor/ceiling rank quotas are preserved.  Thus (0.3) is a low-color-run
assignment theorem, not another marginal reduction.

What remains open is constructing \(\mathcal B\) with the required
whole-transversal law.  There is an exact universal obstruction.  If
\(\Delta_U\) is the legal-successor Hall deficiency and
\(\delta_U\) is the consecutive queue-cylinder discrepancy at top \(U\),
then every orbit coloring satisfies

\[
 \boxed{
 R\ge |G|\sum_U
 \max\left\{\Delta_U,{\delta_U\over2}\right\}.}
\tag{0.5}
\]

Hence the target run scale forces

\[
 \sum_U\max\{\Delta_U,\delta_U/2\}=o(W/Q).
\tag{0.6}
\]

The anticycle tables have \(\Delta_U=M\) and \(\delta_U=2M\), making
(0.5) sharp and giving \(R\ge |G|T=(1-o(1))|G|W\).  They therefore
cannot be repaired by symmetrization or block recoloring.  They are not,
however, ambient-balanced base colors, so they do not rule out a different
\(\mathcal B\).

For a prescribed full SCD orbit the same argument applies radius by
radius and recovers the exact one-SCD obstruction: low total run toll is
equivalent to one integral SCD with low rotor path-forest toll.  The new
double resolution removes denominators and occurrence-capacity issues, but
it cannot average away that atom.

## 1. Fixed-color state tables and path factors

Resolve every column of \(\mathcal B\) to a radius-\(Q\) quotient state.
At a fixed top \(U\), write

\[
 A_U=\{\omega_1,\ldots,\omega_M\}.
\tag{1.1}
\]

The middle owners in the whole balanced resolution are distinct because
\(T\le W\).  Hence the resolved states in (1.1) are distinct.  The
argument below also works with labeled repeated occurrences.

Let \(D_U\) be the directed graph on \(A_U\) whose arcs are the legal
rotor successors.  A partial directed matching \(P\) has indegree and
outdegree at most one at every vertex.  If \(c(P)\) is the number of its
directed-cycle components, then deleting one edge from every cycle leaves
a spanning path factor with

\[
 M-|P|+c(P)
\tag{1.2}
\]

components.  Define

\[
 p_U^*(\mathcal B)
 =\min_P\bigl(M-|P|+c(P)\bigr).
\tag{1.3}
\]

This is the exact minimum number of legal rotor paths covering the table.
It depends on the ordered quotient states, not merely on the rank loads of
their flags.

Put

\[
 P(\mathcal B)=\sum_U p_U^*(\mathcal B).
\tag{1.4}
\]

A color \(g\mathcal B\) has at top \(gU\) the conjugate table \(gA_U\),
so its path-factor minimum is again \(p_U^*(\mathcal B)\).  Every color
therefore has total minimum \(P(\mathcal B)\).

## 2. Occurrence-transport formulation

Let \(\widehat{\mathcal B}=\bigsqcup_{g\in G}g\mathcal B\).  Repeated
columns are retained as indexed occurrences.  For an exact quotient state
\(s\), let \(O_s\) be its occurrence fiber.  The symmetrized
double-resolution theorem gives

\[
 |O_s|=h
\tag{2.1}
\]

independently of \(s\).

There are two equivalent ways to describe the recoloring problem.

1. Start with unlabeled dynamic rotor occurrences and biject each fiber
   \(O_s\) with the prescribed colored occurrences of state \(s\).
2. Keep the colors on the column occurrences fixed and choose a legal
   successor permutation of those occurrences, allowing arbitrary
   pairings between occurrence fibers of legal state types.

The second description is more transparent.  A same-color successor arc
at top \(U\) is an integral transportation unit in the bipartite legal
graph \(D_U\).  For a fixed color, the chosen same-color units form a
partial directed matching.  Their connected components are precisely the
monochromatic intervals, after one edge is cut in every monochromatic
cycle.

Thus the local integer variables may be written

\[
 f^g_{s,t}\in\{0,1\}\qquad(s\to t),
\tag{2.2}
\]

with

\[
 \sum_t f^g_{s,t}\le1,
 \qquad
 \sum_s f^g_{s,t}\le1.
\tag{2.3}
\]

The component objective is (1.2).  The variables for different colors
are coupled only when the unused path endpoints are spliced into a global
successor permutation.  Full coordinate symmetrization makes that endpoint
transport exactly feasible, as the next theorem shows.

This also explains why a transition-augmented Birkhoff relaxation is not
enough.  The statewise occurrence assignments are products of assignment
polytopes, but (2.2) couples two different state fibers and the cycle term
in (1.2) is not a row marginal.  The six-cycle two-color example from
`MATH_ATTACK_J_ROTOR_SCD_RESOLUTION_20260724.md` already has zero
fractional switch cost and positive integral switch cost.

## 3. Exact orbit run identity

### Theorem 3.1 (symmetrized path factors splice exactly)

Optimize simultaneously over

1. every legal successor permutation of the occurrence multiset
   \(\widehat{\mathcal B}\); and
2. every typewise alignment between its dynamic occurrences and the
   prescribed colors \(g\mathcal B\).

Count a maximal cyclic constant-color interval as one run.  Then

\[
 \boxed{R_{\rm orb}^*(\mathcal B)=|G|P(\mathcal B).}
\tag{3.1}
\]

#### Proof: lower bound

Fix any feasible successor permutation and alignment.  Rotor edges
preserve the top.  For one color \(g\) and one top \(gU\), cut its maximal
constant-color intervals out of the ambient rotor cycles.  The intervals
are vertex-disjoint legal paths through all states of \(gA_U\).  An
entirely monochromatic ambient cycle contributes one cyclic component and
is counted as one run, exactly as in (1.2).  Hence this color/top pair has
at least \(p_U^*(\mathcal B)\) runs.

Sum over every \(U\) and all \(|G|\) colors:

\[
 R\ge |G|\sum_U p_U^*(\mathcal B)=|G|P(\mathcal B).
\tag{3.2}
\]

#### Proof: upper bound

For every base top \(U\), choose an optimal legal path factor
\(F_U\) with \(p_U^*(\mathcal B)\) components.  In color \(g\), at top
\(gU\), use the conjugate factor \(gF_U\).  Across all colors this gives

\[
 |G|P(\mathcal B)
\tag{3.3}
\]

open monochromatic paths which partition all occurrences.

It remains to splice their endpoints by legal rotor edges.  Consider one
indexed path start \(a\) in the base resolution.  For a fixed exact state
\(s\), the permutations \(g\) which send the state of \(a\) to \(s\)
form a coset of \(\operatorname {Stab}_G(s)\).  Summing over all
\(P(\mathcal B)\) base starts shows that every exact state is the type of
exactly

\[
 k=P(\mathcal B)|\operatorname {Stab}_G(s)|
\tag{3.4}
\]

path starts in the full orbit.  The same count holds for path ends,
because their base total is also \(P(\mathcal B)\).  The stabilizer size is
state-independent.

At every top the full quotient-state rotor graph is regular.  Its
source--target bipartite graph therefore has a perfect matching
\(\phi_U\).  Take \(k\) labeled copies of \(\phi_U\).  For each exact
state \(s\), biject the \(k\) path ends of type \(s\) to the \(k\) path
starts of type \(\phi_U(s)\).  The added edge is legal.  Every start gets
one predecessor and every end gets one successor, so the resulting
directed graph is a successor permutation of all occurrences.

Every path in (3.3) remains monochromatic.  Hence the resulting cyclic
coloring has at most \(|G|P(\mathcal B)\) runs.  Combine this with (3.2).
\(\square\)

The theorem is a complete occurrence-transport result.  It does not
merely show that the start and end marginals agree: it uses their exact
integer orbit multiplicities and a perfect matching of the legal rotor
graph to splice every occurrence.

The optimization of the successor permutation is essential.  Theorem 3.1
constructs a rotor cycle resolution adapted to the target colors; it does
not claim that an arbitrarily frozen cycle factor admits the same run
count by recoloring alone.

### Corollary 3.2 (exact reset ledger)

The radius-\(Q\) columns of the whole orbit compile with total length

\[
 |G|T+(2Q+1)|G|P(\mathcal B).
\tag{3.5}
\]

Thus the symmetrized low-run route succeeds exactly when

\[
 \boxed{P(\mathcal B)=o(W/Q).}
\tag{3.6}
\]

In particular, changing the equal-state occurrence bijections or the
ambient Euler chronology cannot compensate for a base resolution with
\(P(\mathcal B)=\Omega(W/Q)\).

## 4. Whole-transversal randomized construction

Assume the legal adjacency matrix \(A_U\) of every base top has at least
one perfect matching.  Let \(\mathbb P_U\) be a probability law on its
legal successor permutations.  For a directed simple cycle \(C\) of
length \(j\), suppose

\[
 \mathbb P_U(C\subset\sigma)
 \le {\theta_U\over(M)_j}.
\tag{4.1}
\]

### Theorem 4.1 (whole-transversal orbit coloring)

Under (4.1), there is a deterministic equal-state occurrence alignment
and legal rotor successor permutation of \(\widehat{\mathcal B}\) with

\[
 \boxed{
 R\le |G|H_M\sum_U\theta_U.}
\tag{4.2}
\]

Every color remains exactly \(g\mathcal B\).

#### Proof

The cycle-cylinder theorem gives

\[
 \mathbb E_U c(\sigma)\le\theta_UH_M.
\]

Choose one successor permutation at every base top so that their total
cycle count is at most \(H_M\sum_U\theta_U\).  Regard every cycle as one
path factor component after a marked cut.  Hence

\[
 P(\mathcal B)\le H_M\sum_U\theta_U.
\]

Apply Theorem 3.1.  Its construction conjugates the chosen base factors
through every color and performs only legal endpoint transport, so no
column changes color and all exact quotas remain untouched. \(\square\)

If \(\theta_U\le\theta=O(1)\), then

\[
 \sum_U\theta_U\le\theta N_H\le\theta W/M.
\]

Since \(H_M=O(\log M)\) and \(Q\log M/M=o(1)\), (4.2) gives (0.4).

There is an exact permanent form.  Under the uniform law on the legal
successor permutations of \(A_U\), put

\[
 \Xi_U=
 \sum_{j=1}^M
 \sum_{\substack{C\text{ directed simple cycle}\\|C|=j}}
 {\operatorname {per}A_U[V_U\setminus V(C),
                         V_U\setminus V(C)]
  \over \operatorname {per}A_U}.
\tag{4.3}
\]

Then \(\Xi_U\) is exactly the expected cycle count, so the same proof
gives

\[
 \boxed{R\le |G|\sum_U\Xi_U.}
\tag{4.4}
\]

Consequently

\[
 \sum_U\Xi_U=o(W/Q)
\tag{4.5}
\]

is a randomized whole-interval theorem sufficient for the desired orbit
run scale.  Unlike rank marginals, (4.3) controls cylinders of every order
up to \(M\).

## 5. Block recoloring: exact meaning and limitation

Suppose one begins from any rotor cycle resolution of the uniform
occurrence multiset and partitions its cycles into directed intervals.
Giving one interval a constant color \(g\) is legal only if every state in
the interval is one of the prescribed states of \(g\mathcal B\), with no
state used twice by that color.  Across all intervals, every prescribed
color--state slot must be used exactly once.

Thus a block recoloring is an integral exact-cover problem with constraints

\[
 \sum_{\substack{I:\ I\text{ contains an occurrence of type }s}}
 x_{I,g}=1
 \quad\text{for every prescribed color--state slot }(g,s),
\tag{5.1}
\]

where \(x_{I,g}=1\) only when color \(g\) is admissible on the whole
interval \(I\).  Coordinate symmetrization gives the uniform fractional
point of (5.1), but does not make this interval incidence matrix totally
unimodular.

Theorem 3.1 identifies the exact integral content of (5.1): after arbitrary
equal-state re-splicing, its optimum number of blocks is
\(|G|P(\mathcal B)\).  Hence a block-recoloring theorem with
\(o(|G|W/Q)\) intervals is equivalent to (3.6).  It is not a weaker
consequence of the double-resolution marginals.

This explains both sides of the result.

* If (4.1) holds, Theorem 4.1 explicitly supplies the blocks as conjugate
  whole-transversal cycles.
* If the base state tables have large path-cover number, no choice of
  interval endpoints, palette permutations, or equal-state occurrence
  bijections can cross the lower bound (3.2).

## 6. Quantitative Hall and cylinder lower bounds

Let \(\nu_U\) be the maximum matching size in the legal successor graph on
\(A_U\), and put

\[
 \Delta_U=M-\nu_U.
\tag{6.1}
\]

For an injective queue word \(w\) of length \(2Q-1\), let

\[
 P_U(w)=\#\{\omega\in A_U:(z_1,\ldots,z_{2Q-1})=w\},
\]

\[
 S_U(w)=\#\{\omega\in A_U:(z_2,\ldots,z_{2Q})=w\},
\]

and define

\[
 \delta_U=\|P_U-S_U\|_1.
\tag{6.2}
\]

### Proposition 6.1 (universal orbit run lower bound)

Every exact coloring of every legal rotor chronology of
\(\widehat{\mathcal B}\) into the prescribed orbit colors satisfies

\[
 \boxed{
 R\ge |G|\sum_U
 \max\left\{\Delta_U,{\delta_U\over2}\right\}.}
\tag{6.3}
\]

#### Proof

For a partial matching \(P\), (1.2) gives

\[
 M-|P|+c(P)\ge M-\nu_U=\Delta_U.
\]

For any factorization of \(A_U\) into \(p\) legal paths, cancellation of
the queue shifts on internal edges gives

\[
 \delta_U\le2p.
\]

Therefore

\[
 p_U^*(\mathcal B)
 \ge\max\{\Delta_U,\delta_U/2\}.
\]

Insert this inequality in the chronology-independent lower bound (3.2).
\(\square\)

In particular, if a family \(\mathcal U_{\rm bad}\) of tops satisfies

\[
 \max\{\Delta_U,\delta_U/2\}\ge\kappa M
 \qquad(U\in\mathcal U_{\rm bad}),
\tag{6.4}
\]

then

\[
 R\ge\kappa|G|M|\mathcal U_{\rm bad}|.
\tag{6.5}
\]

A positive-density bad family therefore gives \(R=\Omega(|G|W)\), which
misses the target by a factor of order \(Q\).

For the explicit anticycle table, every top has

\[
 \Delta_U=M,qquad\delta_U=2M.
\]

Thus (6.3) gives

\[
 R\ge |G|MN_H=|G|T=(1-o(1))|G|W.
\tag{6.6}
\]

This is sharp because the table has no legal internal edge, so every
column is a separate run.  Full symmetrization supplies a legal uncolored
rotor circulation, but cannot reduce a color-preserving run count by even
one.

## 7. Full-SCD orbit specialization

Now let \(\mathcal D\) be one full Boolean SCD, clipped to radii
\(0\le d\le H\).  Write \(\mathcal D_d\) for its radius-\(d\) state set
and \(p_d^*(\mathcal D)\) for its minimum spanning rotor path-forest
component count.

At radius \(d\), define \(\Delta_d(\mathcal D)\) as the maximum-matching
deficiency of the induced legal rotor graph on \(\mathcal D_d\), and let
\(\delta_d(\mathcal D)\) be its consecutive \((2d-1)\)-queue cylinder
discrepancy.  Then

\[
 p_d^*(\mathcal D)
 \ge
 \max\left\{\Delta_d(\mathcal D),
             {\delta_d(\mathcal D)\over2}\right\}.
\tag{7.1}
\]

For any complete coordinate-orbit coloring by indexed copies of
\(\mathcal D\), every chronology has weighted run toll at least

\[
 \boxed{
 \mathsf T
 \ge N_{\rm col}
 \sum_{d=0}^H(2d+1)
 \max\left\{\Delta_d(\mathcal D),
             {\delta_d(\mathcal D)\over2}\right\},}
\tag{7.2}
\]

where \(N_{\rm col}\) is the number of indexed SCD colors.  If arbitrary
equal-state re-splicing is allowed in the full rotor master, the exact
optimum is

\[
 \boxed{
 \mathsf T_{\min}
 =N_{\rm col}
  \sum_{d=0}^H(2d+1)p_d^*(\mathcal D).}
\tag{7.3}
\]

For the recursive-necklace/SCD double resolution,
\(N_{\rm col}=R_0|G|\), where \(R_0\) is the necklace length.  Keeping the
necklaces frozen can only increase the optimum in (7.3).  Therefore the
double resolution has a low-switch coloring only if

\[
 \sum_{d=0}^H(2d+1)p_d^*(\mathcal D)=o(W).
\tag{7.4}
\]

Conversely, the full-master orbit/Euler construction realizes (7.3) from
any \(\mathcal D\) satisfying (7.4).  This converse may re-splice the
recursive necklaces; it is not an upper bound for a frozen necklace
factor.  Thus the new integral double resolution does not evade the
one-SCD rotor path-forest gate.

## 8. Exact surviving construction gate

The low-color-run problem now has a complete positive/negative sandwich.

1. **Positive theorem.**  Construct one exact balanced base resolution
   whose fixed-top legal successor graphs admit whole-transversal laws with
   \[
    H_M\sum_U\theta_U=o(W/Q).
   \]
   Then Theorem 4.1 gives an explicit orbit coloring with
   \(o(|G|W/Q)\) runs and preserves every color quota exactly.
2. **Exact optimum.**  Without a whole-transversal law, the best possible
   run count is still exactly \(|G|P(\mathcal B)\).
3. **Negative certificate.**  Hall deficiency and consecutive queue
   cylinders give the universal lower bound (6.3).  A positive-density
   family of linearly defective tops rules out the target scale.
4. **SCD specialization.**  For genuine full-SCD orbit colors, the exact
   optimum is the one-SCD path-forest functional (7.3).  No mixture or
   equal-state occurrence transport lowers its normalized value.

The remaining object is therefore not an uncolored stationary circulation
and not an SCD/rank marginal.  It is one integral base resolution whose
fixed-top state tables have \(o(W/Q)\) total path-cover number, preferably
certified by the permanent cylinder estimate (4.3).  Proving that object
would complete the requested low-color-run assignment; violating (6.3) on
a positive-density set of tops would quantitatively close this route.
