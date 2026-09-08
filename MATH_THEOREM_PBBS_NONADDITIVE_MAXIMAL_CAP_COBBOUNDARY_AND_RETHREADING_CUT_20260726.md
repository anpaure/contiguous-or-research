# Nonadditive PBBS baseline replacement: maximal caps, exact coboundaries, and the rethreading cut

Date: 2026-07-26

Method: pure mathematics only.  No computation, search, solver, or
probabilistic surrogate is used.

This note continues
`MATH_THEOREM_PBBS_BASELINE_REPLACEMENT_CREDIT_NO_GO_20260726.md` and
`MATH_THEOREM_PBBS_PORTAL_LITERAL_DELAY_EQUIVALENCE_AND_TWO_POINT_NO_GO_20260726.md`.
It does not charge seams or portals.  It asks directly when the existing
word positions can be relabelled and rethreaded into a new literal word.

## 0. Outcome

Let \(\Omega\) be the coordinate set, let \(\mathcal T\) be the required
target catalogue, and prescribe one word interval \(I_T\) for every
\(T\in\mathcal T\).  At position \(j\), define the maximal permissible
letter

\[
 C_j=\bigcap_{T:\,j\in I_T}T,                     \tag{0.1}
\]

where an empty intersection is \(\Omega\).  There is a nonzero literal
word \(Y_1,\ldots,Y_L\) for which every \(I_T\) has OR exactly \(T\) if
and only if

\[
 \boxed{
 C_j\ne\varnothing\quad(1\le j\le L),
 \qquad
 T=\bigcup_{j\in I_T}C_j\quad(T\in\mathcal T).}   \tag{0.2}
\]

When (0.2) holds, the maximal-cap word \(Y_j=C_j\) is itself a solution.
Apart from the mandatory nonempty-slot condition \(C_j\ne\varnothing\),
the target-coverage part is equivalently expressed as follows.  Put

\[
F_x=\bigcup_{T:\,x\notin T}I_T,                  \tag{0.3}
\]

Then the exact statewise coverage condition is

\[
 \boxed{I_T\setminus F_x\ne\varnothing
        \quad(T\in\mathcal T,\ x\in T).}          \tag{0.4}
\]

Thus a coordinate belonging to a target needs one position of that
target's interval which is not simultaneously used by any target excluding
the coordinate.  Marginal balances and pairwise endpoint counts do not
imply (0.4).

For the canonical depth-\(H\) PBBS owner-endpoint schedule, (0.1) is
exactly the ordinary erosion baseline

\[
                         C_j=D_j:=\bigcap_{t=j}^{j+H}X_t.       \tag{0.5}
\]

Therefore every in-place word retaining just the canonical middle-owner
witness intervals already satisfies \(Y_j\subseteq D_j\) position by
position.  It succeeds if and only if every positive coordinate run in the
owner chronology has length at least \(H+1\).  In particular, one positive
residence of length at most \(H\) is already a statewise obstruction.  No
signed coboundary, Eulerian token braid, or aggregate circulation which
leaves those owner intervals unchanged can absorb even one such return,
let alone a positive-density family.

The obstruction does not rule out wholesale endpoint rethreading.  It
does quantify the necessary movement.  If a maximal positive run \(R\)
has length \(s\le H\), let \(\delta_H(R)\) be the minimum number of zero
owners in an \((H+1)\)-window meeting \(R\), as defined in (5.2).  Any
successful interval assignment must change at least

\[
                         \boxed{\min\{s,\delta_H(R)\}}           \tag{0.6}
\]

canonical middle-owner witness intervals in the local collar.  For an
\(H\)-isolated run, \(\delta_H(R)=H+1-s\); nearby positive runs can make
\(\delta_H(R)\) smaller, and this is an exact structured sharing
exception rather than a reason to multiply marginal estimates.  More
exactly, the changed-owner set must satisfy the disjunctive escape cut
(5.4) below.  These cuts add for runs with disjoint \(H\)-collars, but
ordinary edge-disjoint residence packing does not make the collars
disjoint.  The surviving Gaussian problem is therefore the integral
overlap problem for these rethreading cuts together with (0.4).

This is a sharp reduction, not a construction of the required PBBS braid.
It proves a genuine no-go for every fixed-endpoint in-place replacement
and gives a necessary-and-sufficient configuration criterion for the only
remaining moving-endpoint escape.

## 1. Exact maximal-cap factorization

Positions are linearly ordered.  An interval is a nonempty set
\([a,b]=\{a,a+1,\ldots,b\}\).  The same theorem applies to cyclic
intervals after choosing their prescribed lifts to a linear double cover.

### Theorem 1.1 (maximal-cap criterion)

Fix nonempty targets \(\mathcal T\subseteq2^\Omega\setminus\{\varnothing\}\)
and a prescribed interval \(I_T\subseteq[L]\) for every target.  Define
\(C_j\) by (0.1).  The following are equivalent.

1. There are nonempty letters \(Y_j\subseteq\Omega\) such that
   \[
                              \bigcup_{j\in I_T}Y_j=T
                              \qquad(T\in\mathcal T).           \tag{1.1}
   \]
2. The maximal caps satisfy (0.2).
3. Every \(C_j\) is nonempty and (0.4) holds for every incidence
   \((T,x)\) with \(x\in T\).

Moreover every feasible word obeys

\[
                              Y_j\subseteq C_j,                 \tag{1.2}
\]

and \((C_1,\ldots,C_L)\) is the unique coordinatewise maximal feasible
word.

#### Proof

Suppose (1.1) holds.  If \(j\in I_T\), then every letter in that interval
is a subset of its OR \(T\).  Hence \(Y_j\subseteq T\) for every active
target and therefore \(Y_j\subseteq C_j\).  In particular \(C_j\ne
\varnothing\).  For a fixed target,

\[
 T=\bigcup_{j\in I_T}Y_j
   \subseteq\bigcup_{j\in I_T}C_j
   \subseteq T,                                    \tag{1.3}
\]

where the last inclusion follows because \(C_j\subseteq T\) whenever
\(j\in I_T\).  Thus (0.2) holds.

Conversely, if (0.2) holds, take \(Y_j=C_j\).  The letters are nonempty
and (1.1) is exactly the second part of (0.2).

Finally,

\[
 x\in C_j
 \quad\Longleftrightarrow\quad
 x\in T\text{ for every }T\text{ with }j\in I_T
 \quad\Longleftrightarrow\quad
 j\notin F_x.                                      \tag{1.4}
\]

Consequently \(x\in\bigcup_{j\in I_T}C_j\) is equivalent to
\(I_T\setminus F_x\ne\varnothing\).  This proves the equivalence with
(0.4), and (1.2) proves maximality. \(\square\)

The theorem is genuinely statewise.  It uses the complete set of targets
active at one position, rather than multiplying marginal probabilities or
checking pairwise intersections.

### Corollary 1.2 (endpoint injectivity on each rank)

In any feasible interval assignment, distinct equal-cardinality targets
have distinct left endpoints and distinct right endpoints.

#### Proof

Two intervals with the same left endpoint are nested, so their ORs are
comparable by inclusion.  Distinct sets of equal cardinality are
incomparable.  The right-endpoint assertion is identical after reversing
the word. \(\square\)

Thus an Eulerian endpoint schedule cannot average away the central
antichain constraints: its left- and right-endpoint projections are
injective before any circulation or cap condition is considered.

## 2. Exact signed-coboundary form

Fix the intervals \((I_T)\), and let \(D_1,\ldots,D_L\) be any baseline
word.  For a coordinate \(x\), write

\[
 d_j^x=\mathbf1_{\{x\in D_j\}},
 \qquad y_j^x=\mathbf1_{\{x\in Y_j\}},
 \qquad \eta_j^x=y_j^x-d_j^x.                     \tag{2.1}
\]

Define the integral prefix potential

\[
 p_0^x=0,
 \qquad p_k^x=\sum_{j=1}^k\eta_j^x.               \tag{2.2}
\]

Then \(\eta_j^x=p_j^x-p_{j-1}^x\), and for every interval \([a,b]\),

\[
 \sum_{j=a}^b y_j^x
 =\sum_{j=a}^b d_j^x+p_b^x-p_{a-1}^x.             \tag{2.3}
\]

### Theorem 2.1 (integral coboundary criterion)

For fixed witness intervals, an in-place replacement of \(D\) exists if
and only if there are integral potentials \(p^x\) such that

\[
 p_j^x-p_{j-1}^x\in\{-d_j^x,1-d_j^x\},            \tag{2.4}
\]

\[
 \sum_{j=a}^b d_j^x+p_b^x-p_{a-1}^x
 \begin{cases}
   =0,&x\notin T,\\
   \ge1,&x\in T,
 \end{cases}
 \quad\text{when }I_T=[a,b],                       \tag{2.5}
\]

and

\[
                         \sum_{x\in\Omega}
                         (d_j^x+p_j^x-p_{j-1}^x)\ge1
                         \qquad(1\le j\le L).     \tag{2.6}
\]

#### Proof

Equations (2.4) say exactly that every new coordinate indicator is zero or
one.  Equation (2.5) says that the interval contains no copy of an excluded
coordinate and at least one copy of every included coordinate.  This is
equivalent to its OR being \(T\).  Equation (2.6) is nonemptiness of the
new letter.  The converse reconstructs \(y_j^x=d_j^x+p_j^x-p_{j-1}^x\).
\(\square\)

On a cyclic slot set an edit decomposes as a periodic coboundary plus one
winding term.  A multiplicity-preserving braid has zero winding and is a
pure coboundary.  The OR problem does not require multiplicity
preservation, so forbidding the winding term would be an unjustified extra
hypothesis.  The maximal-cap criterion already includes both cases.

## 3. The canonical PBBS endpoint schedule

Let

\[
                         \ldots,X_{i-1},X_i,X_{i+1},\ldots      \tag{3.1}
\]

be a Johnson owner path, away from its linearization collars.  For
\(0\le q\le H\), put

\[
 L_{i,q}=\bigcap_{t=i}^{i+q}X_t,
 \qquad
 U_{i,q}=\bigcup_{t=i}^{i+q}X_t.                  \tag{3.2}
\]

The canonical erosion schedule prescribes

\[
 \begin{aligned}
 I_{X_i}&=[i-H,i],\\
 I_{L_{i,q}}&=[i+q-H,i],\\
 I_{U_{i,q}}&=[i-H,i+q].
 \end{aligned}                                    \tag{3.3}
\]

Repeated occurrences of an equal lower or upper target may either be
treated as labelled copies or discarded.  This does not change the cap:
the owner intervals alone have intersection \(D_j\), and every retained
canonical lower or upper target active at \(j\) contains \(D_j\).

Define

\[
                         D_j=\bigcap_{t=j}^{j+H}X_t.             \tag{3.4}
\]

### Theorem 3.1 (erosion is the maximal fixed-schedule word)

For the full target schedule (3.3), the maximal cap at every position is

\[
                              \boxed{C_j=D_j.}                  \tag{3.5}
\]

Consequently every literal word retaining the owner intervals in (3.3)
obeys \(Y_j\subseteq D_j\), regardless of which lower or upper occurrences
are retained.  In particular, neither signed transfers between positions
nor a circulation of existing coordinate tokens can repair a failed
erosion identity without changing some owner witness interval.

#### Proof

The owner intervals active at position \(j\) are exactly those with

\[
                              j\le i\le j+H.                    \tag{3.6}
\]

Their intersection is \(D_j\), so the full cap satisfies \(C_j\subseteq
D_j\).

If \(j\in I_{L_{i,q}}\), then

\[
                              j\le i\le i+q\le j+H,             \tag{3.7}
\]

and hence \(D_j\subseteq L_{i,q}\).  If \(j\in I_{U_{i,q}}\), the
intervals \([j,j+H]\) and \([i,i+q]\) meet: the two required inequalities
are \(j\le i+q\) and \(i\le j+H\).  Choose a common index \(t\).  Then

\[
                              D_j\subseteq X_t\subseteq U_{i,q}.           \tag{3.8}
\]

Thus \(D_j\) is contained in every target active at \(j\), giving
\(D_j\subseteq C_j\).  Combine the two inclusions. \(\square\)

This theorem is stronger than an additive seam lower bound: it is a
pointwise maximality statement for all possible replacement letters.

## 4. Exact short-residence obstruction

Fix a coordinate \(x\), and write

\[
                              b_i=\mathbf1_{\{x\in X_i\}}.      \tag{4.1}
\]

A positive run is a maximal consecutive interval on which \(b_i=1\).

### Theorem 4.1 (fixed-schedule delay criterion)

Assume all \(D_j\) are nonempty.  The canonical schedule (3.3) is
factorable if and only if every positive run of every coordinate has
length at least \(H+1\).

In particular, a positive run of length \(s\le H\) makes the fixed
schedule infeasible.

#### Proof

Suppose \(R\) is a positive run of length \(s\le H\), and take
\(i\in R\).  For every \(j\in[i-H,i]\), the \((H+1)\)-interval
\([j,j+H]\) cannot lie inside \(R\).  Since \(R\) is maximal, it contains
all consecutive occurrences of \(x\) meeting \(i\), and hence

\[
                              x\notin D_j.                         \tag{4.2}
\]

Theorem 3.1 gives \(x\notin Y_j\) throughout the prescribed owner witness
\([i-H,i]\), although \(x\in X_i\).  Factorization is impossible.

Conversely, suppose every positive run has length at least \(H+1\).  If
\(x\in X_i\), the run containing \(i\) contains an \((H+1)\)-subinterval
which contains \(i\).  Thus

\[
                              X_i=\bigcup_{j=i-H}^{i}D_j.          \tag{4.3}
\]

More generally, if \(x\in L_{i,q}\), the one-run containing
\([i,i+q]\) has length at least \(H+1\), so it contains an
\((H+1)\)-subinterval \([j,j+H]\) with
\(i+q-H\le j\le i\).  Therefore

\[
                              L_{i,q}=
                              \bigcup_{j=i+q-H}^{i}D_j.           \tag{4.4}
\]

If \(x\in U_{i,q}\), choose \(t\in[i,i+q]\) with \(x\in X_t\).  The
positive run containing \(t\) contains an \((H+1)\)-subinterval
\([j,j+H]\) containing \(t\), where necessarily
\(i-H\le j\le i+q\).  Hence

\[
                              U_{i,q}=
                              \bigcup_{j=i-H}^{i+q}D_j.           \tag{4.5}
\]

The reverse inclusions in (4.3)--(4.5) follow from the proof of Theorem
3.1.  The nonempty word \((D_j)\) therefore factors the schedule. \(\square\)

For the PBBS step-two factor, an eligible short positive residence is
exactly such a short positive run, up to the fixed endpoint convention of
the residence interval.  Thus the fixed-endpoint in-place route is not
merely expensive at critical packing: it is statewise impossible at the
first genuine return.

## 5. How many owner endpoints must move?

The remaining escape changes witness intervals.  The owner targets alone
already force a quantitative local movement.

Let \(R=[a,a+s-1]\) be a maximal positive run of a coordinate \(x\), with
\(1\le s\le H\), on a retained owner cycle longer than \(H+1\).  Its
canonical owner intervals are

\[
                              I_i^0=[i-H,i].                    \tag{5.1}
\]

For an \((H+1)\)-window meeting \(R\), put

\[
 Z_x(j)=\{k\in[j,j+H]:x\notin X_k\},
 \qquad
 \delta_H(R)=
 \min_{[j,j+H]\cap R\ne\varnothing}|Z_x(j)|.       \tag{5.2}
\]

Maximality of \(R\) and \(|R|\le H\) imply \(\delta_H(R)\ge1\).  If the
whole \(H\)-collar outside \(R\) consists of zero owners for \(x\), then
\(\delta_H(R)=H+1-s\).

For an arbitrary successful interval assignment, call an owner index
changed if its chosen witness interval is not \(I_i^0\), and let \(M\) be
the changed set.

### Theorem 5.1 (statewise owner-rethreading cut)

For every short positive run \(R\), either

\[
                              R\subseteq M,                     \tag{5.3}
\]

or there are \(i\in R\setminus M\) and \(j\in[i-H,i]\) such that

\[
 \boxed{
                              Z_x(j)\subseteq M.}   \tag{5.4}
\]

Consequently

\[
 \boxed{|M\cap(R+[-H,H])|
        \ge\min\{s,\delta_H(R)\}.}                \tag{5.5}
\]

Here the collar notation in (5.5) may be replaced by the precise union of
the owner indices occurring in (5.3)--(5.4).

#### Proof

If (5.3) fails, choose an unchanged \(i\in R\).  Since its owner interval
is \([i-H,i]\) and \(x\in X_i\), the escape criterion (0.4), applied only
to the owner targets, supplies a position \(j\in[i-H,i]\) which belongs to
no chosen witness interval of an owner excluding \(x\).

Every owner index \(k\in[j,j+H]\) has \(j\in I_k^0\).  If
\(x\notin X_k\), that owner would forbid \(x\) at \(j\) unless its interval
were changed.  Hence \(Z_x(j)\subseteq M\), proving (5.4).  This set has
size at least \(\delta_H(R)\).  Alternative (5.3) contains \(s\) changed
owners.  Taking the smaller lower bound proves (5.5). \(\square\)

For a family \(\mathcal R\) of short runs define the exact relaxed
rethreading number

\[
 \kappa_H(\mathcal R)=\min\left\{|M|:
 \begin{array}{l}
 \text{for every }R\in\mathcal R,\text{ either (5.3) holds, or}\\
 \text{there are }i,j\text{ for which (5.4) holds}
 \end{array}\right\}.                              \tag{5.6}
\]

Every full literal factorization changes at least
\(\kappa_H(\mathcal R)\) canonical owner witnesses.  If the relevant
\(H\)-collars are disjoint, then

\[
 \kappa_H(\mathcal R)
 \ge\sum_{R\in\mathcal R}
       \min\{|R|,\delta_H(R)\}.                   \tag{5.7}
\]

For overlapping collars, (5.6), not the sum of marginal demands, is the
correct quantity.  This is precisely where an Eulerian moving-frame braid
could share rethreading work.  Edge-disjoint residence traces alone do not
prove a lower bound on \(\kappa_H\), because their \(H\)-collars may
overlap.

## 6. Exact moving-endpoint configuration criterion

The only escape left by Theorems 3.1 and 4.1 is to choose new witness
intervals.  This choice has an exact finite integral formulation.

For every target \(T\), every interval \([a,b]\subseteq[L]\), and every
coordinate-position pair, introduce binary variables

\[
 z_{T,a,b}\in\{0,1\},
 \qquad y_{x,j}\in\{0,1\}.                         \tag{6.1}
\]

### Theorem 6.1 (exact cap-braid integer system)

A nonzero word of length \(L\) representing every target in
\(\mathcal T\) exists if and only if the following system is feasible:

\[
 \sum_{1\le a\le b\le L}z_{T,a,b}=1
                         \qquad(T\in\mathcal T),   \tag{6.2}
\]

\[
 y_{x,j}+z_{T,a,b}\le1
 \quad(x\notin T,\ j\in[a,b]),                    \tag{6.3}
\]

\[
 \sum_{j=a}^b y_{x,j}\ge z_{T,a,b}
 \quad(x\in T),                                   \tag{6.4}
\]

and

\[
                         \sum_{x\in\Omega}y_{x,j}\ge1
                         \qquad(1\le j\le L).     \tag{6.5}
\]

#### Proof

Given a word and chosen witnesses, set the corresponding \(z\)'s and
coordinate incidences to one.  An excluded coordinate cannot occur in a
witness interval, giving (6.3), while every included coordinate occurs at
least once, giving (6.4).  Conversely, (6.2) chooses an interval for every
target, and (6.3)--(6.4) say exactly that its OR is the target.  Equation
(6.5) makes every letter nonzero. \(\square\)

Eliminating \(y\) for a fixed integral choice of \(z\) gives Theorem 1.1.
Thus (6.2)--(6.5) is not a marginal relaxation: it is the literal problem
itself in moving-endpoint normal form.

There is an equivalent active-state description.  Put

\[
                         \mathcal A_j=\{T:j\in I_T\}.            \tag{6.6}
\]

Each target indicator \(\mathbf1_{\{T\in\mathcal A_j\}}\) has the
consecutive-ones property, and

\[
                         C(\mathcal A_j)=\bigcap_{T\in\mathcal A_j}T.
                                                               \tag{6.7}
\]

A sequence of active states is a valid cap braid if and only if

\[
 C(\mathcal A_j)\ne\varnothing,
 \qquad
 T=\bigcup_{j:\,T\in\mathcal A_j}C(\mathcal A_j).  \tag{6.8}
\]

On a cyclic word the active-state sequence is a closed walk and its state
transitions have an integral Eulerian circulation.  However, an ordinary
circulation recording only transition multiplicities omits both the
one-cyclic-run condition for each target and the incidence coverage in
(6.8).  Those decorated constraints are exactly the information lost by a
first-moment Eulerian-braid argument.

### Corollary 6.2 (return-free full-fan cycle criterion)

Let a Johnson cycle factor partition all \(W\) middle owners into \(c\)
directed cycles, each of length greater than \(2H\).  On each component
write its owners cyclically as \(X_i\), and set

\[
                         D_j=\bigcap_{t=0}^{H}X_{j+t}.           \tag{6.9}
\]

Suppose:

1. every positive coordinate run on every component has length at least
   \(H+1\); and
2. for every required lower or upper target through depth \(H\), some
   consecutive owner window has that intersection or union.

Then the componentwise cyclic erosion words \((D_j)\), each linearized by
duplicating at most \(2H\) boundary letters, concatenate to a nonzero
literal word of length

\[
                              W+2Hc                              \tag{6.10}
\]

covering every required target through depth \(H\).

#### Proof

A Johnson path of \(H\) steps loses at most \(H\) coordinates, so
\(|D_j|\ge m-H>0\).  Theorem 4.1 gives all canonical erosion identities
for every consecutive owner window.  Hypothesis 2 assigns one such window
to every target.  Its erosion witness has at most \(2H+1\) positions, so
duplicating a cyclic prefix of length \(2H\) captures every witness which
crosses the drawing seam.  Sum over the \(c\) components. \(\square\)

This is an exact positive criterion which reuses the \(W\) baseline
positions.  If \(c\le B=W/(2m+1)\), its boundary cost is
\(O(HB)=o(W)\) at Gaussian \(H\).  PBBS supplies the full-fan support and
component bound but fails hypothesis 1 at its short returns.  Theorems 3.1
and 4.1 show that a letter-only PBBS modification cannot repair that
failure; a successful PBBS construction must realize the more general
moving-endpoint system of Theorem 6.1.

## 7. Gaussian PBBS implication

Take \(H=\lceil A\sqrt m\rceil\).  The preceding results give the following
complete architecture boundary.

1. **Fixed PBBS endpoints are closed.**  At the first genuine
   residence of length at most \(H\), the maximal cap is the deficient
   erosion letter.  Relabelling the existing \(W\) slots, adding a
   zero-winding coboundary, or circulating their coordinate multiplicities
   cannot help.

2. **Sparse endpoint surgery is quantitatively constrained.**  Every
   short run obeys (5.3)--(5.5).  A run with
   \(\min\{|R|,\delta_H(R)\}\ge\varepsilon H\) requires at least
   \(\varepsilon H\) changed owner witnesses.  For an \(H\)-isolated run
   this holds whenever
   \(|R|\in[\varepsilon H,(1-\varepsilon)H]\).  Nearby positive runs may
   lower \(\delta_H(R)\) and thereby expose the exact sharing pattern a
   successful braid would need.  The aggregate obstruction is
   \(\kappa_H\), not a product of marginal return counts.

3. **A full-density moving braid remains possible in principle.**  The
   previously proved annular endpoint census already forces
   \(\Omega_A(W)\) owner witnesses to acquire Gaussian span.  Theorem 6.1
   explains what those long intervals must additionally satisfy: every
   target-coordinate incidence needs a private escape position (0.4), and
   every simultaneous active-target cap must remain nonempty.

4. **The exact next theorem is now explicit.**  For one PBBS-selected
   occurrence of every required lower and upper target through depth \(H\),
   construct intervals on \(W+o_A(W)\) positions satisfying (0.2), with
   both central antichains included; or exhibit a family of coordinates
   and targets for which every consecutive-ones interval assignment has
   an empty active cap or violates (0.4).  The first alternative
   immediately yields the literal word by taking maximal caps.  The second
   is a statewise no-go for all nonadditive in-place replacements, not
   merely for additive seams.

No such unrestricted PBBS interval assignment or universal violating
family is proved here.  What is proved is that the apparent
signed-coboundary freedom vanishes completely at fixed endpoints and that
the sole surviving escape is the exact decorated cap-braid system
(6.2)--(6.8).
