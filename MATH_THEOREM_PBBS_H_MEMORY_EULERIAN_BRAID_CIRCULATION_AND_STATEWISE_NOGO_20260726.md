# PBBS nonadditive replacement as an exact H-memory Eulerian braid

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, random-marginal
surrogate, or additive seam charge is used.

This note continues
`MATH_THEOREM_PBBS_NONADDITIVE_MAXIMAL_CAP_COBBOUNDARY_AND_RETHREADING_CUT_20260726.md`
and
`MATH_ATTACK_PBBS_GAUSSIAN_ANNULUS_NONLINEAR_LOW_SWITCH_20260726.md`.

## 0. Outcome

Put

\[
 n=2m+1,
 \qquad W=\binom{2m+1}m,
 \qquad H=\lceil A\sqrt m\rceil,                  \tag{0.1}
\]

where \(A>0\) is fixed.  Let \(\mathcal O\) be the \(W\) labelled middle
owner occurrences of the PBBS factor.  The labels distinguish physical
occurrences; their underlying sets are the \(W\) members of the middle
antichain.

The full dense-switch problem has an exact integral circulation form.
Its states are admissible histories of \(H+1\) owners, and an arc shifts
the history by one owner.  Arc admissibility excludes precisely a proper
positive coordinate run of length at most \(H\).  Each arc is decorated by all
actual lower intersections and upper unions of its suffix windows through
depth \(H\).

For binary arc variables \(z_a\), the three systems

\[
 \begin{aligned}
 \text{history flow:}&\quad
       \sum_{a\in\delta^+(v)}z_a
       =\sum_{a\in\delta^-(v)}z_a,\\
 \text{owner transversal:}&\quad
       \sum_{a:\,\operatorname{term}(a)=X}z_a=1,\\
 \text{decorated coverage:}&\quad
       \sum_a c_{T,a}z_a\ge1
 \end{aligned}                                    \tag{0.2}
\]

are equivalent to an owner-exact, return-safe Johnson cycle factor covering
every requested target \(T\).  If its support has \(C(z)\) cycles, the
componentwise erosion word has exact length at most

\[
                         \boxed{W+2HC(z).}          \tag{0.3}
\]

If \(h(z)\) targets are left uncovered, appending them gives

\[
                         \boxed{W+2HC(z)+h(z).}     \tag{0.4}
\]

Thus

\[
                         HC(z)+h(z)=o(W)            \tag{0.5}
\]

is an exact nonadditive coefficient-one criterion.  Soft successor
switches are not charged: arbitrarily many may occur inside a selected
cycle.  Only hard output components and actual target holes occur in
(0.4).  Multi-seam windows are already encoded in the history state, so
no independence or one-seam approximation appears.

There is also an exact fractional dual.  A statewise obstruction consists
of target weights \(\beta_T\ge0\), owner prices \(\alpha_X\), and a history
potential \(\phi\) such that every admissible arc satisfies

\[
 \sum_T\beta_Tc_{T,a}
 \le \alpha_{\operatorname{term}(a)}
    +\phi_{\operatorname{tail}(a)}
    -\phi_{\operatorname{head}(a)},                \tag{0.6}
\]

while

\[
                         \sum_T\beta_T>
                         \sum_X\alpha_X.           \tag{0.7}
\]

Equations (0.6)--(0.7) rule out even a fractional braid, hence also every
integral in-place compiler.  Conversely, in the absence of such a dual
certificate the fractional system is feasible.  Integral rounding and the
cycle count remain additional requirements.

For the unrestricted two-rotor atlas, the fractional alternative is
settled positively.  Giving the two rotor arcs out of every permutation
state total weight \(1/[m!(m+1)!]\) gives owner mass exactly one, exact
state balance, and target mass

\[
                         {W\over\binom nr}\ge1                    \tag{0.7a}
\]

on every set of every paired annulus rank \(r\), simultaneously.  Hence
the unrestricted atlas has no fractional coboundary obstruction.  Its sole
remaining issue is correlated integral owner-transversal rounding with
\(o(W/m)\) support cycles.

Two statewise no-go theorems follow.

1. If the allowed successor relation is the unchanged PBBS successor,
   the first short positive residence deletes its unique history arc.
   The owner immediately after that arc has no admissible predecessor, so
   (0.2) is infeasible.  This is the circulation form of the maximal-cap
   obstruction: a letter-only or zero-winding recoding cannot work.

2. If one tries to obtain the upper constraints from an anti-dihedral
   singleton symmetry, every output component has period exactly
   \(n=2m+1\).  Hence \(C=W/n\), and (0.3) has excess
   \[
                         2H{W\over n}=o(W)
   \]
   for the erosion compiler, but a singleton sliding-spine
   literalization needs a prefix of length \(m+H\) per component and costs
   \[
                         {W\over n}(m+H)
                         =\left({1\over2}+o(1)\right)W.          \tag{0.8}
   \]
   Thus symmetry cannot supply the required wholesale long-endpoint word.
   The distinction between (0.3) and (0.8) is essential: the
   anti-dihedral object is a singleton-spine proposal, not a return-safe
   PBBS erosion factor.

What remains is the unrestricted, nonsymmetric integral solution of
(0.2) with (0.5), or a dual certificate (0.6)--(0.7) for the actual PBBS
allowed-transition graph.  The note gives an exact Eulerian braid and
genuine statewise obstructions, but does not assert that this final
integral circulation exists.

## 1. The exact run-safe history graph

Let \(\mathcal E\subseteq\mathcal O\times\mathcal O\) be an allowed
successor relation.  At minimum, \((X,Y)\in\mathcal E\) requires the
underlying sets to be adjacent in the Johnson graph.  Three important
choices are:

1. the unchanged directed PBBS successor;
2. PBBS segment interiors together with a specified catalogue of legal
   tail--head joins; and
3. the unrestricted Johnson relation, representing wholesale chronology
   replacement.

A history state is a tuple

\[
                         v=(X_0,X_1,\ldots,X_H)     \tag{1.1}
\]

whose consecutive pairs lie in \(\mathcal E\).  Repeated occurrence labels
are allowed in a formal state; the owner-transversal equations below
prevent their repeated use in the selected chronology.

There is a directed arc

\[
 a:(X_0,\ldots,X_H)\longrightarrow(X_1,\ldots,X_H,Y)           \tag{1.2}
\]

when \((X_H,Y)\in\mathcal E\) and the following exact closing-run test
holds:

\[
 \boxed{
 x\in X_H\setminus Y
 \quad\Longrightarrow\quad
 x\in\bigcap_{i=0}^{H}X_i.}                       \tag{1.3}
\]

Call the resulting finite digraph \(\mathscr G_H(\mathcal E)\).

### Lemma 1.1 (local test equals global positive-run safety)

A cyclic owner chronology lifts to a closed walk in
\(\mathscr G_H(\mathcal E)\) if and only if every proper positive run of
every coordinate has length at least \(H+1\).

#### Proof

Every proper positive run ends at an edge \(X_H\to Y\) which removes its
coordinate.  If its length is at most \(H\), that coordinate is absent at
some one of the preceding \(H+1\) owners and (1.3) fails.  Conversely, if
(1.3) fails at a removal edge, the coordinate was absent among the
preceding \(H+1\) owners; its just-ended maximal positive run therefore
has at most \(H\) owner states.  A coordinate present on the entire cycle
has no removal edge and causes no exception. \(\square\)

The test is exact for literal erosion.  It is weaker than requiring all
nearby transition supports to be disjoint; the latter is a convenient
geodesic sufficient condition, not the factorization invariant.

## 2. Arc decorations contain the complete cylinder

For an arc (1.2), write its head history as

\[
                         (Z_0,Z_1,\ldots,Z_H),     \tag{2.1}
\]

where \(Z_H=Y\).  For every \(0\le q\le H\), define the actual suffix
labels

\[
 \lambda_{q}^-(a)=\bigcap_{i=H-q}^{H}Z_i,
 \qquad
 \lambda_{q}^+(a)=\bigcup_{i=H-q}^{H}Z_i.         \tag{2.2}
\]

These are sets, not merely ranks or normalized port types.  If the odd
PBBS two-shore convention shifts one signed depth by one, use the audited
shifted catalogue; none of the arguments changes.

Let \(\mathcal T\) be any required target catalogue through depth \(H\),
including both central antichains when desired.  Put

\[
 c_{T,a}=1
 \quad\Longleftrightarrow\quad
 T=\lambda_q^-(a)\text{ or }T=\lambda_q^+(a)
 \text{ at an allowed signed depth}.              \tag{2.3}
\]

Because the complete preceding \(H\)-owner cylinder is part of the state,
\(c_{T,a}\) remains exact even if the window crosses many old PBBS segment
boundaries.  This is the state expansion missing from an edge-local seam
matching.

## 3. Integral circulation equivalence

For every history arc \(a\), let \(z_a\in\{0,1\}\).  Its terminal owner is

\[
                         \operatorname{term}(a)=Z_H.            \tag{3.1}
\]

Consider the equations

\[
 \sum_{a\in\delta^+(v)}z_a
 =\sum_{a\in\delta^-(v)}z_a
 \qquad(v\in V(\mathscr G_H)),                    \tag{3.2}
\]

\[
 \sum_{a:\,\operatorname{term}(a)=X}z_a=1
 \qquad(X\in\mathcal O),                          \tag{3.3}
\]

and

\[
 \sum_a c_{T,a}z_a\ge1
 \qquad(T\in\mathcal T).                          \tag{3.4}
\]

### Theorem 3.1 (H-memory Eulerian braid equivalence)

Equations (3.2)--(3.4) are equivalent to a directed Johnson cycle factor
which

1. uses every labelled owner occurrence exactly once;
2. uses only transitions in \(\mathcal E\);
3. has no proper positive coordinate run of length at most \(H\); and
4. realizes every target in \(\mathcal T\) as an actual consecutive owner
   intersection or union through depth \(H\).

#### Proof

Suppose \(z\) is integral.  All arcs entering one history state have the
same terminal owner, namely the last owner of that state.  Equation (3.3)
therefore implies that every history state has selected indegree at most
one.  Flow conservation gives selected outdegree equal to selected
indegree.  Hence the selected history arcs are vertex-disjoint directed
cycles.

Reading terminal owners along those cycles gives compatible shifted
histories, hence directed owner cycles using only \(\mathcal E\).  Equation
(3.3) says every owner occurrence appears exactly once.  Lemma 1.1 gives
run safety.  Finally every selected arc supplies precisely the suffix
windows (2.2), so (3.4) is exactly target coverage.

Conversely, take the length-\((H+1)\) histories along any owner cycle factor
with properties 1--3 and select their shift arcs.  Every used history has
one incoming and one outgoing arc, giving (3.2); owner exactness gives
(3.3); and property 4 gives (3.4). \(\square\)

No target independence has been assumed.  All depths and both signs use
the same binary circulation.

## 4. Literalization and exact cost

For one selected output owner cycle \(C=(X_i)\), put

\[
                         D_i=\bigcap_{r=0}^{H}X_{i+r}.           \tag{4.1}
\]

Every \(D_i\) is nonempty when \(H<m\), because an \(H\)-edge Johnson
walk removes at most \(H\) coordinates from its first owner.  Lemma 1.1
and the exact erosion identities give, for \(0\le q\le H\),

\[
 \bigcap_{r=0}^{q}X_{t+r}
 =\bigcup_{i=t+q-H}^{t}D_i,                       \tag{4.2}
\]

\[
 \bigcup_{r=0}^{q}X_{t+r}
 =\bigcup_{i=t-H}^{t+q}D_i.                       \tag{4.3}
\]

Thus one erosion letter is paid per owner occurrence.  Repeating the first
\(2H\) letters of each cyclic component linearizes every witness in
(4.2)--(4.3).

### Theorem 4.1 (nonadditive in-place cost)

Let \(z\) satisfy (3.2)--(3.3), let \(C(z)\) be the number of selected
cycles, and let

\[
 h(z)=|\{T\in\mathcal T:\sum_a c_{T,a}z_a=0\}|.   \tag{4.4}
\]

Then there is a nonzero literal word of length

\[
                         \boxed{W+2HC(z)+h(z)}     \tag{4.5}
\]

covering every target in \(\mathcal T\).

#### Proof

Concatenate the componentwise linearized erosion words.  Their total
principal length is \(W\), and their total cyclic opening cost is
\(2HC(z)\).  Equations (4.2)--(4.3) cover every target emitted by a
selected history arc.  Append each of the \(h(z)\) remaining targets as
one literal letter. \(\square\)

This is not an additive portal or seam ledger.  Changing the successor at
\(s\) locations has no term \(Hs\).  A dense set of soft switches is free
once it lies inside the same selected Eulerian components.

## 5. Exact fractional dual and statewise cuts

Relax \(z_a\in\{0,1\}\) to \(z_a\ge0\), retaining (3.2)--(3.4).  Let
\(\beta_T\ge0\), let \(\alpha_X\in\mathbb R\), and let
\(\phi_v\in\mathbb R\).  Call \((\beta,\alpha,\phi)\) a statewise cut if

\[
 \sum_T\beta_Tc_{T,a}
 \le \alpha_{\operatorname{term}(a)}
    +\phi_{\operatorname{tail}(a)}
    -\phi_{\operatorname{head}(a)}
 \qquad(a\in E(\mathscr G_H)).                    \tag{5.1}
\]

### Theorem 5.1 (decorated-circulation Farkas dual)

The fractional system (3.2)--(3.4) is feasible if and only if every
statewise cut satisfies

\[
                         \boxed{
                         \sum_T\beta_T\le\sum_X\alpha_X.}       \tag{5.2}
\]

#### Proof

If \(z\) is feasible, multiply (3.4) by \(\beta_T\), sum, and use (5.1):

\[
 \begin{aligned}
 \sum_T\beta_T
 &\le\sum_a z_a\sum_T\beta_Tc_{T,a}\\
 &\le\sum_a z_a\alpha_{\operatorname{term}(a)}
   +\sum_a z_a(\phi_{\operatorname{tail}(a)}
                     -\phi_{\operatorname{head}(a)})\\
 &=\sum_X\alpha_X.
 \end{aligned}                                    \tag{5.3}
\]

The last equality uses (3.2)--(3.3).  Conversely, the standard finite
Farkas alternative for the nonnegative variables \(z_a\), equality rows
(3.2)--(3.3), and covering rows (3.4) says that infeasibility is certified
by free equality multipliers and nonnegative covering multipliers.  With
the owner multiplier negated, its arc inequalities and strict objective
are exactly (5.1) and the strict reverse of (5.2). \(\square\)

Examples of genuine statewise cuts are immediate.

* If a required target is emitted by no admissible arc, take its
  \(\beta\)-weight to be one and all other variables zero.
* A history potential can charge a target family which is available only
  after entering a closed set of memory states.  This detects frozen
  projections and successor traps which have zero signature in owner
  marginals.
* Point, pair, and fixed-depth weights are only special cases.  The dual
  permits one common weight on the full all-depth target catalogue.

Passing every statewise cut proves only fractional feasibility.  An
integral theorem additionally needs owner-transversal rounding and control
of \(C(z)\).

## 6. The unchanged-PBBS statewise no-go

Let \(\mathcal E\) contain only the original directed successor of each
PBBS owner occurrence.

### Theorem 6.1 (one short run kills the fixed-successor circulation)

If the PBBS chronology contains a positive coordinate run of length at
most \(H\), then (3.2)--(3.3) has no solution, even fractionally.

#### Proof

Let \(X\to Y\) be the original PBBS edge which closes that short run.
The unique history arc projecting to this edge fails (1.3), so it is absent
from \(\mathscr G_H(\mathcal E)\).  Because the successor relation is
fixed, \(Y\) has no other allowed predecessor occurrence.  Hence no
history arc has terminal owner \(Y\), while (3.3) demands terminal mass
one at \(Y\).  This is already a one-owner Farkas cut. \(\square\)

The theorem rules out every letter circulation which retains the PBBS
successor.  A viable braid must change physical successors, not merely
move coordinate tokens among the old erosion positions.

## 7. Anti-dihedral singleton closure is also obstructed

There is a tempting wholesale alternative: replace erosion letters by one
cyclic singleton spine

\[
 X_i=\{s_i,s_{i+1},\ldots,s_{i+m-1}\},             \tag{7.1}
\]

and use a rank-reversing coordinate anti-automorphism
\(\theta(A)=[n]\setminus R(A)\) to turn all lower prefix coverage into
upper coverage.  Suppose on a component

\[
                         \theta(X_i)=X_{\epsilon i+c}
                                      \cup X_{\epsilon i+c+1},
                         \qquad\epsilon\in\{1,-1\}.             \tag{7.2}
\]

### Theorem 7.1 (anti-dihedral statewise rigidity)

Every component satisfying (7.1)--(7.2) has period exactly
\(n=2m+1\) and is one ordinary wreath.  Hence a factor enumerating all
\(W\) middle owners has \(W/n\) components and singleton-spine
linearization excess

\[
                         {W\over n}(m+H)
                         =\left({1\over2}+o(1)\right)W.          \tag{7.3}
\]

#### Proof

The transition \(X_i\to X_{i+1}\) deletes \(s_i\) and inserts
\(s_{i+m}\).  The anti-automorphism reverses these roles.  In the
rotational case \(\epsilon=1\), comparison with the transition between
the two upper owners in (7.2) gives

\[
 R(s_{i+m})=s_{i+c},
 \qquad
 R(s_i)=s_{i+c+m+1}.                               \tag{7.4}
\]

Apply the second equality at \(i+m\) and compare with the first.  Since
\(2m+1=n\),

\[
                         s_{i+c+n}=s_{i+c}.         \tag{7.5}
\]

In the reflection case \(\epsilon=-1\), the same comparison reverses the
indices but again gives \(s_{j+n}=s_j\).  Thus \(X_{i+n}=X_i\).

If the component has \(L\) distinct middle windows, then \(L\mid n\).
A proper divisor of the odd number \(n\) is at most \(n/3<m\), and a
period-\(L\) symbol word cannot have an injective \(m\)-window.  Hence
\(L=n\).

It remains to exclude a repeated symbol in this period.  Every
\((m+1)\)-window is injective: otherwise two adjacent middle windows would
fail to be distinct \(m\)-sets.  Hence the intersection of \(q+1\)
successive middle windows is their positional overlap of size \(m-q\), for
every \(0\le q\le m-1\).  Applying \(\theta\) and (7.2), the corresponding
union of \(q+2\) middle windows has size \(m+1+q\).  It is the symbol
window of that length, so it is injective.  At \(q=m-1\), every
\((n-1)\)-window is injective.  On a period of length \(n\ge5\), any two
repeated positions lie together in some \((n-1)\)-window, a contradiction.
Thus the \(n\) symbols are distinct and the component is a wreath.

There are therefore \(W/n\) components.  A singleton spine must repeat a
prefix of length \(m+H\) when each component is linearized, giving (7.3).
\(\square\)

Thus symmetry can remove the upper coverage equations only by forcing a
linear component toll.  A viable Eulerian braid must be nonsymmetric and
satisfy both signed coverage systems directly.

## 8. An explicit all-depth fractional Eulerian braid

The unrestricted statewise dual has no fractional obstruction.  This is
proved by one common two-rotor circulation, not by choosing independent
distributions at different depths.

Write a permutation state as

\[
                         \pi=(x_1,x_2,\ldots,x_n)\in S_n.       \tag{8.1}
\]

Let \(A\) left-rotate the first \(n-1\) positions and fix the last, and
let \(B\) left-rotate all \(n\) positions.  Both moves project the middle
prefix owner

\[
                         X(\pi)=\{x_1,\ldots,x_m\}               \tag{8.2}
\]

to

\[
                         X(g\pi)=X(\pi)-\{x_1\}+\{x_{m+1}\},
                         \qquad g\in\{A,B\}.                    \tag{8.3}
\]

For an owner \(X\), let

\[
 \mathcal F_X=\{\pi:X(\pi)=X\},
 \qquad
 D=|\mathcal F_X|=m!(m+1)!.                       \tag{8.4}
\]

### Theorem 8.1 (uniform two-rotor fractional braid)

Fix \(t\in[0,1]\) and assign

\[
 z_{\pi,A}={t\over D},
 \qquad
 z_{\pi,B}={1-t\over D}.                          \tag{8.5}
\]

Then:

1. every owner fibre has total selected mass one;
2. inflow equals outflow at every permutation state;
3. the circulation is positive-run-safe for every \(H<m\); and
4. for every \(1\le r\le n-1\) and every \(r\)-set \(S\), the total
   selected mass of states whose first \(r\) entries have underlying set
   \(S\) is
   \[
                         \boxed{{W\over\binom nr}.}              \tag{8.6}
   \]

Consequently all lower ranks \(r=m-q\) and upper ranks
\(r=m+1+q\), \(0\le q\le H\), satisfy their covering inequalities
simultaneously, since

\[
                         {W\over\binom n{m-q}}ge1,
 \qquad
                         {W\over\binom n{m+1+q}}\ge1.           \tag{8.7}
\]

#### Proof

Every state has total outgoing mass \(1/D\).  A fibre has \(D\) states,
which proves the owner equation.  The two incoming arcs are the unique
\(A^{-1}\)- and \(B^{-1}\)-preimages and have total mass
\(t/D+(1-t)/D=1/D\), proving circulation.

Along either rotor move the first \(n-2\) symbols shift left, and the next
symbol is one of the two coordinates not in those positions.  Thus every
\((n-1)\)-symbol frame is injective.  In the induced sliding
\(m\)-owner chronology every proper positive coordinate run has \(m\)
owner states.  Since \(H<m\), the history is run-safe.

For a fixed \(r\)-set \(S\), exactly

\[
                         r!(n-r)!                              \tag{8.8}
\]

permutations have prefix set \(S\).  Multiply by outgoing mass \(1/D\):

\[
 {r!(n-r)!\over m!(m+1)!}
 ={\binom nm\over\binom nr}
 ={W\over\binom nr},                              \tag{8.9}
\]

proving (8.6).  The central binomial coefficients are maximal at ranks
\(m,m+1\), so (8.7) follows. \(\square\)

At Gaussian depth \(q=x\sqrt m+O(1)\), the exact slack is

\[
 {W\over\binom n{m-q}}
 =\exp(x^2+o(1)).                                  \tag{8.10}
\]

Thus no marginal, coboundary, or fractional decorated-circulation cut can
obstruct the unrestricted rotor atlas.  Any negative theorem must be an
integral owner-fibre obstruction, a component obstruction, or a physical
restriction on which rotor states may replace the PBBS baseline.

### Theorem 8.2 (integral rotor criterion and literal cost)

Let \(y_{\pi,g}\in\{0,1\}\) satisfy

\[
 \sum_{\pi\in\mathcal F_X}\sum_g y_{\pi,g}=1
 \qquad\text{for every middle owner }X,            \tag{8.11}
\]

\[
 \sum_g y_{\pi,g}=\sum_g y_{g^{-1}\pi,g}
 \qquad(\pi\in S_n),                              \tag{8.12}
\]

and the prefix-cover inequalities corresponding to (8.7).  If the support
has \(C(y)\) directed cycles, then there is a literal singleton word of
length

\[
                         \boxed{W+C(y)(m+H)}        \tag{8.13}
\]

covering the complete paired band through depth \(H\).

#### Proof

Equations (8.11)--(8.12) select disjoint rotor cycles with exactly one
state over every middle owner.  Reading the first emitted symbol along a
cycle gives a cyclic singleton word; its consecutive \(m\)-windows are
the middle owners, while its shorter and longer prefix windows are exactly
the target sets in the prefix-cover constraints.  Write one period of each
cycle and repeat its first \(m+H\) symbols.  This linearizes every required
window.  Summing over components gives (8.13). \(\square\)

Therefore an integral rounding with

\[
                         C(y)=o(W/m)                              \tag{8.14}
\]

is an explicit nonadditive \(W+o(W)\) Gaussian-annulus braid.  Theorem
8.1 proves its exact common fractional precursor.  It does not prove the
correlated integral owner-transversal rounding in (8.11)--(8.14).

## 9. Exact remaining theorem

The additive seam question has disappeared.  The remaining PBBS theorem
is exactly one of the following alternatives.

> **Positive H-memory braid.**  Enlarge the successor relation beyond the
> fixed PBBS edges by an owner-valid catalogue of moving-frame joins and
> find an integral solution of (3.2)--(3.3) for which
> \[
>                         HC(z)+h(z)=o(W).
> \]
> All lower and upper Gaussian targets must be evaluated by the actual
> history labels (2.2), not by one-seam marginals.

or

> **Negative statewise cut.**  Produce weights satisfying
> (5.1) with \(\sum_T\beta_T>\sum_X\alpha_X\) for every physically
> authorized moving-frame successor catalogue, or prove an integral
> owner-fibre/odd-cycle obstruction after the fractional cuts pass.

The fixed-successor and anti-dihedral subfamilies are closed by Theorems
6.1 and 7.1.  No unrestricted physically authorized PBBS moving-frame
catalogue is presently known to satisfy the positive alternative, and no
dual cut is presently known for the full unrestricted Johnson relation.
This is the exact current boundary; chronology length is nowhere counted
as literal word length.
