# Lane L: exact private-stutter supply, adjacent collars, and bounded sidecars

Date: 2026-08-01  
Status: exact native collar theorem, exact pin-contracted compiler Hall
theorem, exact integral cut master, and conditional bounded-sidecar
corollary.  No all-dimensional private-site or coindependent-bank supply is
claimed.

## 0. Outcome

The capacity-one theorem of item2532L has an exact supply formulation.

1. Full age collars are much more local than their positional windows
   suggest.  Individually legal stutter retimings can interfere only when
   their chronology centers are adjacent.  For an adjacent pair, one
   labelled cross-rectangle inclusion is necessary and sufficient.  If it
   holds, all phase choices form a literal Boolean cube and every site's
   complete OR ray is invariant under every other toggle.
2. Consequently any set of nonadjacent centers is automatically
   full-collar compatible.  Site supply on a fixed independent chronology
   bank is exactly ordinary SDR Hall.  Ordered interval menus have an exact
   gap-two earliest-start criterion.
3. For a fixed cap/trace state and a fixed selected site tuple, the complete
   simultaneous compiler condition is one contracted Hall theorem.  Delete
   all selected ray cells, pin every intermediate target to its old long
   cell, and match the residual targets.  This is necessary and sufficient,
   not only a safe sufficient test.
4. With binary site choices, the compiler condition is the exact family of
   linear Hall cut-load rows.  Interval target neighborhoods reduce the
   family to cell intervals; laminar neighborhoods reduce it to the
   laminar members.
5. A bounded number of source sidecars follows if their site lists have an
   SDR in a collar-transparent bank and all candidate rays lie in one
   pre-certified coindependent compiler reserve.  The selected source cost is
   `H` sites and the compiler-state footprint is at most `Hd` ray cells.

Three shortcuts are false.  Raw site Hall does not see adjacent collar
failure.  Per-site compiler privacy does not imply joint Hall.  Feasible ray
packets do not form a matroid, so unrestricted packet selection is not an
ordinary Rado/matroid-intersection problem.

## 1. Occurrence-labelled data

Let

\[
                  \cdots\longrightarrow X^{t-1}
                  \longrightarrow X^t
                  \longrightarrow X^{t+1}
                  \longrightarrow\cdots                         \tag{1.1}
\]

be a literal depth-`d` age chronology, where

\[
                  X^t=(X^t_0,\ldots,X^t_d),
                  \qquad B_t=X^t_0.                             \tag{1.2}
\]

At a candidate center `t`, let `\widehat X^t` be an individually legal
same-neighbour, same-type stutter alternative:

\[
          X^{t-1}\longrightarrow\widehat X^t
          \longrightarrow X^{t+1}.                              \tag{1.3}
\]

Put

\[
          \Delta_{t,i}=X^t_i\triangle\widehat X^t_i,
          \qquad D_t=B_t\triangle\widehat B_t.                   \tag{1.4}
\]

When the terminal cell is a singleton, this site carries a directed coatom
transfer `Q^-(t)\to Q^+(t)`.  Its occurrence-labelled ray `R_t` is the set
of its `d` changed intervals, and `\lambda_t` is its longest, coatom-valued
cell.

Fix throughout Sections 4--6 one complete cap/trace state `\theta` and its
target--cell incidence graph

\[
                       G_\theta=({\cal T},{\cal C};E_\theta).
                                                                    \tag{1.5}
\]

Changing `\theta` changes the graph.  Hall in a union of cap-state graphs is
not a substitute for one common state.

## 2. Exact native full-collar compatibility

### Theorem 2.1 (nearest-neighbour cross criterion)

A set `S` of distinct candidate centers is simultaneously literal, and
every partial toggle of `S` is literal, if and only if every adjacent
selected pair `t,t+1` satisfies

\[
 \boxed{\quad
       \Delta_{t,i}\subseteq
       B_{t+1}\cap\widehat B_{t+1}
       \qquad(0\le i<d).
       \quad}                                                   \tag{2.1}
\]

Nonadjacent selected centers impose no native compatibility row.

#### Proof

Every transition incident to only one changed state is already certified by
(1.3).  For adjacent selected centers the sole missing transition is

\[
                     \widehat X^t\longrightarrow
                     \widehat X^{t+1}.                           \tag{2.2}
\]

The old-head transition gives

\[
                     \Delta_{t,i}\subseteq B_{t+1}.              \tag{2.3}
\]

The transition (2.2) is literal exactly when

\[
 \widehat X^t_i\setminus\widehat B_{t+1}
       =X^t_i\setminus\widehat B_{t+1}
       \qquad(0\le i<d),
\]

which is equivalent to
`\Delta_{t,i}\subseteq\widehat B_{t+1}`.  Combining with (2.3) proves
(2.1).  Since literal recurrence is checked on consecutive states, there
are no other rows.  The same argument applies to every subset of `S`.
\(\square\)

### Corollary 2.2 (Boolean cube and OR-ray orthogonality)

Under (2.1), the selected toggles commute and form a literal Boolean cube.
Moreover each selected site's complete ray `R_t` and every value on that
ray are independent of all other selected phases.  Rays at distinct centers
are occurrence-disjoint.

#### Proof

Theorem 2.1 proves the cube.  For every site,
`D_t\subseteq B_{t+1}` by its fixed-head condition.  If `t+1` is also
toggled, the `i=0` row of (2.1) also gives
`D_t\subseteq\widehat B_{t+1}`.  Thus in every phase the next newborn masks
the complete write at `t`.

Consider a ray interval ending at a different center `u`.  A prior changed
position `t<u` either lies outside that interval or occurs together with
`t+1`, which masks it.  Future writes lie outside the interval.  Hence only
the phase at `u` affects its ray.  Distinct right endpoints give distinct
occurrence-labelled interval cells.  \(\square\)

The apparent windows `[t-d,t+1]` may therefore overlap heavily.  Distance
at least two between centers is a simple sufficient condition, independent
of `d`.

### Minimal adjacent obstruction

At `d=1` on letters `a,b,c`, put

\[
 A=(ab\mid c),\qquad X=(ac\mid b),\qquad H=(bc\mid a).           \tag{2.4}
\]

In the chronology `A\to X\to A\to X`, both adjacent middle states can
individually be changed to `H`.  Changing both would require `H\to H`, but

\[
                       bc\setminus bc=\varnothing\ne\{a\}.       \tag{2.5}
\]

Equivalently,

\[
 X_0\triangle H_0=\{a,b\}
       \not\subseteq A_0\cap H_0=\{b\}.                          \tag{2.6}
\]

Thus two distinct ray cells and two individually legal sites need not give
a legal pair.

## 3. Site SDR, interval, and guard criteria

Fix a prescribed simple transfer chain

\[
                   Q_0\longrightarrow Q_1\longrightarrow
                   \cdots\longrightarrow Q_h,                   \tag{3.1}
\]

and let `L_i` be the occurrence-labelled candidate centers for
`Q_i\to Q_{i+1}`.

### Proposition 3.1 (Hall on an independent chronology bank)

Let `J` be any independent set of chronology centers, for example one
parity class after opening a cyclic chronology.  A distinct
full-collar-compatible representative `p_i\in L_i\cap J` exists for every
stage if and only if

\[
 \boxed{\quad
   \left|\bigcup_{i\in I}(L_i\cap J)\right|\ge |I|
   \qquad\text{for every }I\subseteq\{0,\ldots,h-1\}.
   \quad}                                                       \tag{3.2}
\]

#### Proof

The centers in `J` are nonadjacent, so Theorem 2.1 makes every distinct
choice compatible.  The remaining statement is exactly the ordinary
marriage theorem.  \(\square\)

In particular, if every `L_i\cap J` has at least `h` members, (3.2) is
automatic.  Without fixing `J`, `3h-2` distinct candidate centers per stage
suffice greedily: each previous choice forbids at most its center and its two
neighbours.

### Proposition 3.2 (exact ordered interval staircase)

Suppose stage `i` must use a center in the integer interval
`[a_i,b_i]`, and the chosen centers must increase in stage order with gap at
least two.  Define

\[
 \rho_0=a_0,\qquad
 \rho_i=\max\{a_i,\rho_{i-1}+2\}.                              \tag{3.3}
\]

Such a choice exists if and only if `\rho_i\le b_i` for every `i`.
Equivalently,

\[
       \max_{0\le j\le i}\{a_j+2(i-j)\}\le b_i
       \qquad(0\le i<h).                                       \tag{3.4}
\]

#### Proof

The recurrence is the earliest possible choice at each stage.  Inductively
it is no later than the corresponding point of any feasible choice, so its
failure is decisive.  Expanding the recurrence gives (3.4).  \(\square\)

Raw Hall on all centers is insufficient.  The lists

\[
                         L_0=\{0,2\},\qquad L_1=\{1\}            \tag{3.5}
\]

satisfy ordinary Hall, but have no nonadjacent representatives.  If both
adjacent cross rows fail, they have no compatible representatives at all.
Stable sets of a path do not form a matroid.

### Proposition 3.3 (factorized external guards)

Suppose every additional pin/envelope guard is a conjunction of literal
one-resource reads, every guarded resource has at most one selected writer,
and each read asks for its old phase, its new phase, or is indifferent.  A
guard required initially or finally is represented by an initial or terminal
sentinel read.  On a selected site set, direct `p\to q` when `q` must be
toggled after `p` to preserve one of `p`'s reads.  Add the prescribed
relocation-chain precedence arcs.  A legal serialization exists if and only
if this dependency digraph is acyclic.

#### Proof

Every edge is a necessary precedence constraint.  If the graph is acyclic,
any topological order respects every factorized read, while Theorem 2.1
handles the native recurrence rows.  \(\square\)

Laminar guard supports alone do not imply acyclicity: two nested guards can
read one another's writes and form a two-cycle.  Laminar guards are safe when
all comparable dependencies consistently follow containment depth.
With multiple writers per guarded resource, pairwise precedence need not be
complete; the exact object is the full finite guard-order CSP, not this DAG.

## 4. Pin-contracted Hall is exactly compiler serialization

For a selected tuple

\[
                         P=(p_0,\ldots,p_{h-1}),                 \tag{4.1}
\]

assume:

* `p_i` realizes `Q_i\to Q_{i+1}`;
* its port `\lambda_i:=\lambda_{p_i}` has old/new values
  `Q_i,Q_{i+1}` and both incidences
  `Q_i\lambda_i,Q_{i+1}\lambda_i\in E_\theta`;
* the rays are occurrence-disjoint; and
* the tuple satisfies Theorem 2.1 and every external guard.

Put

\[
 D(P)=\bigcup_{i=0}^{h-1}R_{p_i},\qquad
 {\cal T}_0={\cal T}\setminus\{Q_1,\ldots,Q_h\}.                \tag{4.2}
\]

### Theorem 4.1 (pin-contracted Hall iff private serialization)

There is an initial compiler matching which saturates
`{\cal T}\setminus\{Q_h\}`, uses the forced pins

\[
                         Q_i\longleftrightarrow\lambda_i
                         \qquad(1\le i<h),                       \tag{4.3}
\]

leaves `\lambda_0` free, and uses no other cell of `D(P)`, if and only if

\[
 \boxed{\quad
        |N_\theta(A)\setminus D(P)|\ge |A|
        \qquad\text{for every }A\subseteq{\cal T}_0.
        \quad}                                                  \tag{4.4}
\]

Under these equivalent conditions, toggling `p_0,\ldots,p_{h-1}` in chain
order and relocating the intermediate matching edges produces a matching
which saturates all of `{\cal T}`.  Every background edge remains fixed,
and no upper or compiler debt remains.

#### Proof

If (4.4) holds, Hall gives a matching of `{\cal T}_0` into
`{\cal C}\setminus D(P)`.  Add the forced pins (4.3).  The result saturates
every target except `Q_h`, while `\lambda_0` is free.

Toggle `p_0`.  Its new longest value is `Q_1`.  Move `Q_1` from
`\lambda_1` to `\lambda_0`, freeing `\lambda_1`.  Continue in the same way.
At the last site, assign `\lambda_{h-1}` to `Q_h`.  Section 2 returns every
native collar and upper occurrence; the declared guards return by
hypothesis.

Conversely, before the first toggle any serialization of the stipulated
pinned form has
the intermediate pins (4.3), a free `\lambda_0`, and no other matching edge
on a selected ray.  Delete the pins and their target rows.  What remains is
a matching of `{\cal T}_0` into `{\cal C}\setminus D(P)`, so (4.4) is
necessary.  \(\square\)

If a previously chosen matching with the same hole differs from the
conditioned matching above, their symmetric difference is a disjoint union
of alternating cycles and cell-ended alternating paths.  Flipping whole
components relocates the matching without exposing a target.

Define the raw Hall slack

\[
                    s_\theta(A)=|N_\theta(A)|-|A|.              \tag{4.5}
\]

Then (4.4) is equivalently

\[
                  |D(P)\cap N_\theta(A)|\le s_\theta(A)
                  \qquad(A\subseteq{\cal T}_0).                 \tag{4.6}
\]

This is the exact common-cap load row.

## 5. Exact integral site-choice master

For an oriented candidate `p\in L_i` let `\kappa(p)` be its physical
chronology center and let `y_{ip}\in\{0,1\}` select it at stage `i`.  Assume
candidate pins are valid in the fixed state `\theta`.  The exact
selected-tuple system consists of

\[
 \sum_{p\in L_i}y_{ip}=1,\qquad
 \sum_{i,p:\,\kappa(p)=t}y_{ip}\le1
       \quad\text{for every center }t,                         \tag{5.1}
\]

the adjacent failed-cross rows

\[
                         y_{ip}+y_{jq}\le1,                     \tag{5.2}
\]

every required external-guard precedence row, and the Hall cut-load rows

\[
 \boxed{\quad
 \sum_{i,p}y_{ip}\,
       |R_p\cap N_\theta(A)|
       \le s_\theta(A)
 \qquad(A\subseteq{\cal T}_0).
 \quad}                                                        \tag{5.3}
\]

Here (5.2) is imposed for each pair of oriented candidate choices
`p\in L_i,q\in L_j` at adjacent centers for which the cross condition (2.1)
fails.
For an integral selection satisfying the collar rows, Corollary 2.2 makes
the selected rays disjoint, so the left side of (5.3) is exactly
`|D(P)\cap N_\theta(A)|`.  Theorems 2.1 and 4.1 therefore prove:

### Theorem 5.1 (exact Hall/Benders supply criterion)

Under the one-writer guard hypothesis of Proposition 3.3, the integral
system (5.1)--(5.3), together with its guard-order condition, is feasible if
and only if the prescribed chain has a system of
distinct occurrence-labelled sites, a literal serialization order, and one
simultaneous alternating relocation matching in the fixed cap state
`\theta`.

A maximum-flow/min-cut oracle on
`G_\theta[{\cal T}_0,{\cal C}\setminus D(P)]` separates a violated row
(5.3) for any integral candidate.  No claim about the fractional convex
hull is made.

If the cap state is variable, the exact quantifier is

\[
        \exists P\ \exists\theta\in\Theta(P)
        \quad\text{such that (4.4) holds}.                       \tag{5.4}
\]

Replacing (5.4) by Hall in `\bigcup_\theta G_\theta` is unsound.

## 6. Interval and laminar compiler cuts

### Theorem 6.1 (convex-neighbourhood reduction)

Suppose the cells are linearly ordered and every residual target
`q\in{\cal T}_0` has an interval neighborhood `I_q`.  Then (4.4) is
equivalent to

\[
 \boxed{\quad
   |\{q\in{\cal T}_0:I_q\subseteq J\}|
       \le |J\setminus D(P)|
   \qquad\text{for every cell interval }J.
   \quad}                                                       \tag{6.1}
\]

#### Proof

Necessity is Hall applied to every target family whose complete
neighborhood lies in `J`.  Conversely, if `A` violates Hall, decompose the
union of its target intervals into interval components.  Every `I_q` lies
in one component, and some component contains more rows of `A` than
available cells.  That component violates (6.1).  \(\square\)

### Corollary 6.2 (laminar-neighborhood reduction)

If the residual neighborhoods themselves form a laminar family
`{\cal L}`, it is necessary and sufficient to check

\[
 |\{q\in{\cal T}_0:N_\theta(q)\subseteq J\}|
       \le |J\setminus D(P)|
       \qquad(J\in{\cal L}).                                    \tag{6.2}
\]

Indeed, the maximal neighborhoods in any target family are pairwise
disjoint, so a deficient union contains a deficient maximal laminar member.

These are compiler-neighborhood statements.  Laminar positional guard
supports still need Proposition 3.3.

## 7. Bounded-sidecar corollaries

### Corollary 7.1 (common coindependent reserve)

Fix a chain of `h` transfers.  Suppose:

1. a collar-transparent bank `J` has site lists satisfying (3.2);
2. all rays of the candidate sites under consideration lie in a declared
   cell bank `{\cal B}`;
3. `G_\theta[{\cal T}_0,{\cal C}\setminus{\cal B}]` has a matching
   saturating `{\cal T}_0`; and
4. every candidate has its valid forced port and all external guards return.

Then a distinct representative system from `J` and the one residual
matching in row 3 give a complete private-ray serialization.

For fixed `h=H` this uses exactly `H` stutter source occurrences.  The
selected ray footprint has at most `Hd` occurrence cells.  If every list in
one parity bank has at least `H` sites, the site Hall row is automatic; the
`3H-2` greedy bound and the interval staircase (3.3) are alternative
supply certificates.

This is a concrete bounded-sidecar theorem, but the coindependent bank in
row 3 is a real hypothesis, not a scalar unused-cell count.

### Corollary 7.2 (precompiled laminar macro selector)

Suppose each bounded path macro has already been checked against the same
residual matching and cap state.  Regard the macros as ground elements and
suppose the compatible macro sets are exactly the independent sets of a
certified laminar matroid `M_{\cal L}`.  If demand `j` has macro menu `E_j`,
distinct compatible macros exist exactly when

\[
       r_{M_{\cal L}}\!\left(\bigcup_{j\in J}E_j\right)
       \ge |J|
       \qquad\text{for every demand family }J.                  \tag{7.1}
\]

This is Rado's theorem.  It applies only after each macro's compiler and
native collar state has been contracted.  Arbitrary raw ray packets do not
form this matroid.

In particular, merely having laminar physical collar intervals does not
create the required matroid.  A parent interval and its two disjoint child
intervals give feasible sets of sizes one and two, but the parent cannot be
augmented by either child.  The laminar matroid in Corollary 7.2 is a
separately certified capacity system, not interval-disjointness itself.

### Theorem 7.3 (fixed-matching relocation flow)

Fix a compiler matching `M` and a globally collar-compatible catalogue of
oriented stutter sites.  Assume every shorter ray cell is `M`-free and every
other `M`-edge avoids the catalogue rays used by a flow.  A site `p` is:

* root-eligible when `\lambda_p` is `M`-free and `Q^-(p)` has a retained
  `M`-provider outside that port;
* continuation-eligible at `q` when `Q^-(p)=q` and
  `M(q)=\lambda_p`.

Build the occurrence-state network `\Gamma_M` as follows.

1. Give every physical site center and every target node capacity one.
2. Add `\sigma\to p` for every root-eligible site.
3. Add `p\to Q^+(p)` for every oriented fibre choice.
4. Add `q\to p` for every continuation-eligible site at `q`.
5. Add `q\to\tau` for every designated unmatched hole `q`.

Then `H` simultaneous private-ray augmentations with one common alternating
relocation matching exist if and only if

\[
                         \operatorname{maxflow}(\Gamma_M)=H.    \tag{7.2}
\]

Equivalently every node-capacitated `\sigma`--`\tau` cut has capacity at
least `H`.

This is an iff on the declared background-fixed, longest-port handoff face.
It does not cover a global rematching which changes background `M`-edges or
uses changed shorter-ray cells.

#### Proof

An integral path begins at a free port whose tail remains matched.  On
reaching an intermediate target `q`, move its `M`-edge to the newly changed
port; this frees the unique continuation port `M(q)`.  At a terminal target,
use the final port to match the hole.  Thus every path is exactly one
alternating relocation chain.

Capacity one makes the paths occurrence- and target-disjoint.  Global collar
compatibility lets their toggles commute, so an `H`-flow raises the matching
rank by `H` without upper or compiler debt.  Conversely every simultaneous
handoff records one such path; disjoint handoffs give an integral flow.
\(\square\)

If an `H`-flow has a decomposition using at most `L` sites per path, it uses
at most `HL` stutter occurrences.  Hence fixed `H,L` gives an honest bounded
source sidecar.  The min-cut row alone does not imply bounded `L`.

On the direct one-site face, `\Gamma_M` is just the bipartite graph between
holes and root-eligible private bays, so (7.2) reduces to ordinary Hall.  In
particular, with `H` holes, `H` pairwise separated eligible bays per hole
already force a direct bounded sidecar.

## 8. Sharp obstructions outside the prepared face

### 8.1 Individual privacy is not joint privacy

Let two residual targets `x,y` both have neighborhood `\{1,2,3\}`.  Two
collar-disjoint rays delete cells `1` and `2`.  Deleting either ray alone
leaves a matching of `x,y`; deleting both leaves only cell `3`.  The joint
cut `A=\{x,y\}` has slack one and ray load two, violating (4.6).

Thus site SDR Hall plus per-site privacy is insufficient.

### 8.2 Coindependent ray packets are not a matroid

Let residual target neighborhoods be `\{a,b\}` and `\{c,d\}`, and let
`e,f` be harmless cells.  Consider two-cell packets

\[
          P=\{a,c\},\qquad Q=\{b,e\},\qquad R=\{d,f\}.            \tag{8.1}
\]

Deleting `P` is feasible, and deleting `Q\cup R` is feasible.  But neither
`P\cup Q` nor `P\cup R` is feasible.  Hence the feasible packet sets violate
matroid augmentation.  There is no unrestricted ordinary Rado or
two-matroid shortcut for (5.3).

### 8.3 Laminar guards alone do not order the moves

Two nested factorized guards can each read the resource written by the
other.  Their dependency graph is a directed two-cycle, so no serialization
exists even though the positional supports are laminar.

### 8.4 Reachability and min-cut do not bound sidecar length

For arbitrary `N`, take letters `c,0,\ldots,N` and targets

\[
                              q_i=\{c,i\}.
\]

For `0\le i<N` define depth-one rank-three states

\[
\begin{aligned}
 Z_i&=(\{i,i+1\}\mid\{c\}),\\
 X_i&=(\{c,i\}\mid\{i+1\}),\\
 X_i^+&=(\{c,i+1\}\mid\{i\}),\\
 A_i&=(\{c\}\mid\{i,i+1\}).
\end{aligned}                                                   \tag{8.2}
\]

Both

\[
                  Z_i\to X_i\to Z_i,\qquad
                  Z_i\to X_i^+\to Z_i                            \tag{8.3}
\]

are literal, so site `i` carries `q_i\to q_{i+1}`.  Also

\[
                         Z_i\to A_i\to Z_{i+1}                   \tag{8.4}
\]

is literal.  Concatenate two occurrences of `X_0` separated by `Z_0`,
followed by the connectors and the single occurrences `X_1,\ldots,X_{N-1}`.
This gives one open literal chronology with separated site centers.

Match `q_0` at the first `X_0` occurrence, leave the port of the second
`X_0` occurrence free, match `q_i` at `X_i` for `1\le i<N`, and leave
`q_N` unmatched.  From the free root port, the reachable relocation network
is the unique path of `N` site nodes.  Its min-cut is one and the hole is
reachable, but its only augmentation consumes all `N` stutters.
Thus even `H=1` has no bounded-sidecar consequence without a bounded-depth
or short-route hypothesis.  The case `N=2` is the smallest nondirect
instance.

## 9. Exact remaining all-dimensional gate

The local transition, collar, ray, and compiler quantifiers are now
separated without loss:

\[
\begin{array}{c}
\text{site SDR / interval supply}\\
+\ \text{adjacent labelled cross rows}\\
+\ \text{one fixed-cap Hall cut system}\\
\end{array}
\quad\Longleftrightarrow\quad
\text{one private alternating serialization}.                  \tag{9.1}
\]

For a bounded terminal defect, Corollary 7.1 reduces the all-dimensional
problem to planting a positive menu of stutter sites whose rays lie in one
coindependent compiler reserve.  Neither fractional occurrence supply nor
strong connectivity of the target projection proves this row.  No
`B(k)+O(1)` conclusion is claimed.
