# Prescribed tasks in a sparse C6 reservoir: spread SDR and the central source-star obstruction

Date: 2026-07-31  
Lane: K, additive-constant sparse-reservoir compiler  
Status: exact positive transfer theorem, fractional-pressure rounding theorem,
and a literal Catalan-scale counterexample to degree-only assignment.  The
PBBS/Pascal eligibility and guarded-ticket hypotheses remain open.

## 0. Outcome

There are two logically different assignment problems.

1. **Assignment into an already authenticated row-sparse reservoir.**  Here
   spread is automatic.  Any SDR image is a subset of the reservoir, so its
   nonnegative conflict rows can only decrease.  The exact remaining gate is
   ordinary Hall.  A convenient local sufficient condition is

   \[
      \min_{\tau\in T}d_G(\tau)\ge r,
      \qquad
      \max_{e\in\mathcal R}d_G(e)\le r.                         \tag{0.1}
   \]

   For the proposed \(r=m\), this gives the desired SDR by one edge count.

2. **Simultaneous assignment and sparse-reservoir extraction from the full
   C6 atlas.**  Here \(m\) eligible incidences per task, ordinary Hall, and
   pairwise-distinct source endpoints are all insufficient.  A literal
   family of \(\Theta(W/m)\) tasks has pairwise-disjoint native eligibility
   stars of size \(m+1\), so Hall is trivial, but every SDR has
   \(\Omega(m^2)\) average raw conflict in every row.  This also defeats an
   \(O(dm)\) target whenever \(d=o(m)\).

The positive simultaneous theorem needs a **fractional pressure base**.
Let \(w(e,f)\) be normalized list-pair conflict.  If the task transversal
matroid has a fractional base \(y\) with

\[
             \sum_f w(e,f)y_f\le D\quad(e\in\mathcal E),          \tag{0.2}
\]

and every pair weight is at most \(B\), pipage rounding produces an SDR image
\(S\) with

\[
 \boxed{
   \max_e\sum_{f\in S\setminus\{e\}}w(e,f)
       \le (\mathrm e-1)D+B\log(2|\mathcal E|).}                  \tag{0.3}
\]

Thus \(D=O(m),B=O(1)\) gives \(O(m)\), and
\(D=O(dm),B=O(d)\) gives \(O(dm)\) because the middle-level anchor ground
has logarithmic size \(\log|\mathcal E|=O(m)\).

After this assignment, per-list Markov pruning and Haxell select one packet
from every assigned list whenever

\[
                           L_{\min}\ge8D_{\rm row}.                \tag{0.4}
\]

The remaining all-dimensional task is therefore exact: prove Hall inside
one pre-extracted guarded reservoir, or prove the fractional pressure rows
(0.2) and the pair-code bound \(B=O(d)\) for the actual occurrence-labelled
PBBS/Pascal tasks and their complete witness/topology/common-cap tickets.

## 1. Conflict kernel and row-sparse reservoirs

Let \(\mathcal E\) be a family of oriented middle-level incidence anchors.
For each anchor \(e\), let \(P_e\) be its packet list.  In the raw
incidence-C6 catalogue, \(|P_e|=L=m^2\).  Define

\[
 w(e,f)={1\over |P_e|}
   |\{(p,q)\in P_e\times P_f:p\sim q\}|,                         \tag{1.1}
\]

where \(p\sim q\) means that their declared resources conflict.  For unequal
guarded list sizes, (1.1) is oriented; all arguments below use only
nonnegativity and the stated row bound.  Set \(w(e,e)=0\), since within-list
conflicts are irrelevant to a transversal.

For \(R\subseteq\mathcal E\), put

\[
                         A_e(R)=\sum_{f\in R\setminus\{e\}}w(e,f). \tag{1.2}
\]

Call \(R\) **\(D\)-row-sparse** when \(A_e(R)\le D\) for every \(e\in R\).

The authenticated raw theorem supplies two relevant reservoirs:

\[
\begin{array}{c|c|c}
\text{reservoir}&\text{size lower bound}&D\\ \hline
R_1&3I/(4m^2)&72m+216\\
R_2&W/(32m)&16m\quad\text{(token-energy upper bound),}
\end{array}                                                       \tag{1.3}
\]

where

\[
                         W={2m+1\choose m},\qquad I=W(m+1).       \tag{1.4}
\]

The anchors of \(R_2\) also have pairwise-distinct lower and upper source
endpoints.

### Lemma 1.1 (monotonicity)

If \(R\) is \(D\)-row-sparse and \(S\subseteq R\), then

\[
                            A_e(S)\le D\qquad(e\in S).             \tag{1.5}
\]

#### Proof

Every summand in (1.2) is nonnegative, and the sum for \(S\) is a sub-sum of
the sum for \(R\).  
\(\square\)

This elementary observation is the key quantifier correction.  Once the
prescribed tasks really are eligible inside the same authenticated
reservoir, no additional probabilistic spread theorem is required after
the matching.

## 2. Exact SDR gate inside a fixed reservoir

Let `T` be the prescribed task bank and let

\[
                         G=(T,R;E_G)                              \tag{2.1}
\]

be the literal task--eligible-anchor graph after every physical, witness,
residence, boundary, and fixed-guard eligibility test which is intended to
precede packet selection.

### Theorem 2.1 (fixed-reservoir transfer)

There is an injective task assignment \(\phi:T\to R\) if and only if

\[
                         |N_G(X)|\ge|X|\qquad(X\subseteq T).      \tag{2.2}
\]

For every such assignment, its image \(S=\phi(T)\) obeys the same row bound
as \(R\):

\[
                         A_e(S)\le D\qquad(e\in S).               \tag{2.3}
\]

#### Proof

The equivalence is Hall's theorem.  Equation (2.3) is Lemma 1.1.  
\(\square\)

### Corollary 2.2 (candidate-pressure criterion)

Suppose for some integer \(r\ge1\) that

\[
 d_G(\tau)\ge r\quad(\tau\in T),
 \qquad
 d_G(e)\le r\quad(e\in R).                                      \tag{2.4}
\]

Then \(G\) has an SDR, and every SDR image is \(D\)-row-sparse.

#### Proof

For \(X\subseteq T\), double-count its incident eligibility edges:

\[
 r|X|\le |E_G(X,N_G(X))|\le r|N_G(X)|.
\]

Hence (2.2) holds.  Apply Theorem 2.1.  
\(\square\)

For the proposed degree \(r=m\), the extra hypothesis is exactly a maximum
task pressure of \(m\) per reservoir incidence.  If “private incidence” means
that an anchor is eligible for at most one task, the corollary is immediate
with room to spare.  Pairwise-distinct physical endpoint labels do not imply
this eligibility-pressure bound.

The exact weakest finite criterion remains (2.2).  Average right degree or
\(d_G(\tau)\ge m\) alone cannot replace it.

There is a second positive route when “private” has its strongest literal
meaning.  Call a raw anchor family `S` **strongly source-private** when, for
distinct anchors \(e=(C,U)\) and \(f=(D,V)\), neither source vertex \(C,U\)
occurs in any candidate of \(P_f\), and conversely.  The union of the lower
vertex roles in \(P_f\) is the closed Johnson neighbourhood of \(D\); the
upper roles give the closed Johnson neighbourhood of \(V\).  Hence strong privacy
is equivalent to the selected lower centres and upper centres both having
Johnson distance at least two.

### Theorem 2.3 (strong-private raw row bound)

Every strongly source-private raw anchor family `S` satisfies

\[
                          A_e(S)\le11m+2\qquad(e\in S).            \tag{2.5}
\]

Consequently, if the task eligibility graph has an SDR whose image is
strongly source-private, one can choose compatible raw C6s at all assigned
anchors for every \(m\ge89\).

#### Proof

Fix one selected list.  Consider a rank-`m` vertex token `R` occurring in a
nonfixed role.  Every other selected lower source centre whose list contains
`R` is a Johnson neighbour of `R`.  Those neighbours form a rook graph,
and a Johnson-distance-two code has at most `m` vertices in it.  At most one
of these anchors can realize `R` in its multiplicity-`m` one-free role: if
two use the same inserted coordinate their lower sources are adjacent, and
if they use different inserted coordinates their upper sources are
adjacent.  All remaining occurrences have multiplicity one.  Therefore the
external multiplicity of `R` is at most

\[
                              m+(m-1)=2m-1.                       \tag{2.6}
\]

The fixed list has `m` one-free lower tokens of multiplicity `m` and
`m^2` zero-free lower tokens of multiplicity one.  After division by
\(L=m^2\), their total token-energy contribution is at most

\[
             {m\cdot m(2m-1)+m^2(2m-1)\over m^2}=4m-2.           \tag{2.7}
\]

The upper shore contributes the same amount.

The fixed source incidence and the two one-free incidence roles contain a
source endpoint, so strong privacy gives them zero external load.  Fix a
zero-free incidence `(R,R+s)`.  An external occurrence in the first or
third zero-free incidence role fixes source upper `R+b` or source lower
`R-c+s`; the corresponding source-code condition allows at most one of
each.  Occurrences in the middle zero-free role have source lowers in one
rook neighbourhood of `R`, so there are at most `m`.  Thus one zero-free
incidence has external multiplicity at most `m+2`.  There are `3m^2`
zero-free incidence-role occurrences in the fixed list, contributing at
most

\[
                              3m+6.                              \tag{2.8}
\]

Equations (2.7)--(2.8) sum to `11m+2`.  Token energy upper-bounds actual
pair conflict, proving (2.5).  The packet conclusion follows from Theorem
3.1 below because

\[
                         m^2\ge8(11m+2)                           \tag{2.9}
\]

for \(m\ge89\).  
\(\square\)

This theorem is stronger than mere injectivity or distinct source
endpoints.  A source endpoint may be different from every other source
endpoint and still occur as a nonfixed token in another full list.

## 3. From row-sparse anchors to compatible packets

After fixing an SDR, attach one actual packet part \(\mathcal P_\tau\) to each
assigned anchor.  Assume

\[
                  |\mathcal P_\tau|\ge L_{\min}                    \tag{3.1}
\]

and that the average external degree of each part in the complete selected
conflict graph is at most \(D_{\rm row}\).

### Theorem 3.1 (Markov--Haxell completion)

If

\[
                              L_{\min}\ge8D_{\rm row},             \tag{3.2}
\]

then one can select one mutually compatible packet from every assigned
part.

#### Proof

In each part delete packets of external degree greater than `2D_row`.
Markov retains at least half of every part.  The induced graph has maximum
degree at most `2D_row`, and each part has size at least `L_min/2`.
Haxell's independent-transversal theorem applies because

\[
                   L_{\min}/2\ge4D_{\rm row}
                     =2(2D_{\rm row}).
\]

\(\square\)

For \(R_1\), take \(L_{\min}=m^2\) and \(D_{\rm row}=72m+216\); the displayed
inequality holds at \(m\ge579\).  For \(R_2\), token energy upper-bounds
actual conflict, so \(D_{\rm row}=16m\) and \(m\ge128\) suffices.

If a task guard merely restricts a raw list to at least \(\alpha m^2\)
candidates and adds no new conflict resource, its raw average row grows by
at most the factor \(1/\alpha\).  Thus the exact deletion-only condition over
a reservoir of original row bound \(D_0\) is

\[
                         \alpha^2m^2\ge8D_0.                       \tag{3.3}
\]

Complete protected packets generally add new witness, topology, and cap
tokens.  For them one must prove directly

\[
                         D_{\rm row}\le Cdm.                        \tag{3.4}
\]

When this row is normalized using the already restricted guarded list,
(3.2) asks \(\alpha m^2\ge8Cdm\), which holds eventually when \(d=o(m)\).

## 4. Simultaneous extraction: a fractional pressure theorem

Suppose the eligible anchors are not already contained in one row-sparse
reservoir.  Let \(M_G\) be the transversal matroid on \(\mathcal E\): a set of
anchors is independent when it can be matched to distinct tasks.  Its
bases have size \(|T|\) and are exactly the images of task-covering SDRs.

A fractional task matching consists of numbers \(x_{\tau e}\ge0\) with

\[
 \sum_{e\in N_G(\tau)}x_{\tau e}=1\quad(\tau\in T),
 \qquad
 y_e:=\sum_\tau x_{\tau e}\le1\quad(e\in\mathcal E).              \tag{4.1}
\]

Then \(y\) lies in the base polytope of \(M_G\).

### Theorem 4.1 (fractional-pressure spread SDR)

Assume (4.1) and constants \(D,B\) with \(B>0\) such that

\[
 \sum_f w(e,f)y_f\le D\quad(e\in\mathcal E),
 \qquad
 0\le w(e,f)\le B\quad(e,f\in\mathcal E).                       \tag{4.2}
\]

Then there is a task-covering SDR with image \(S\) satisfying

\[
 \max_{e\in\mathcal E}
   \sum_{f\in S\setminus\{e\}}w(e,f)
 \le(\mathrm e-1)D+B\log(2|\mathcal E|).                         \tag{4.3}
\]

If \(B=0\), then all pair weights vanish and any task-covering SDR base
satisfies the same conclusion with zero row load.

#### Proof

For any anchor set \(B\), the restriction of \(x\) to task--\(B\) edges is a
fractional bipartite matching of value \(y(B)\).  Bipartite matching
integrality gives \(y(B)\le r_{M_G}(B)\), while
\(y(\mathcal E)=|T|\).  These are
exactly the base-polytope inequalities for \(M_G\).

Apply randomized pipage rounding to \(y\) in the base polytope of \(M_G\).
The base-polytope exchange lemma writes every nonintegral rounding step as
a mean-preserving random choice between the two endpoints of a segment

\[
                         y+t(\mathbf1_i-\mathbf1_j).               \tag{4.4}
\]

Both endpoints remain in the same base polytope, and iteration ends at the
indicator of a base \(S\).

Fix one row anchor \(e\) and put

\[
 q_f=\exp(w(e,f)/B)-1\ge0,
 \qquad
 F_e(y)=\prod_f(1+q_fy_f).                                       \tag{4.5}
\]

Along (4.4), all factors except \(i,j\) are fixed and the product of the two
moving factors has second derivative \(-2q_iq_j\le0\).  Hence \(F_e\) is
concave along every pipage segment.  The mean-preserving endpoint choice
therefore does not increase its expectation.  At the final base,

\[
 F_e(\mathbf1_S)
   =\exp\!\left({1\over B}\sum_{f\in S}w(e,f)\right).             \tag{4.6}
\]

Since \(0\le w/B\le1\), convexity of the exponential on \([0,1]\) gives

\[
 e^{w/B}-1\le(\mathrm e-1){w\over B}.
\]

Using \(1+u\le e^u\) and (4.2),

\[
 \mathbb E\exp\!\left({1\over B}\sum_{f\in S}w(e,f)\right)
 \le F_e(y)
 \le\exp\!\left({(\mathrm e-1)D\over B}\right).                 \tag{4.7}
\]

Markov's inequality makes the probability that row \(e\) exceeds the right
side of (4.3) at most \(1/(2|\mathcal E|)\).  A union bound over the anchor
ground leaves positive probability that no row exceeds it.  The resulting
base is matchable to all tasks by the definition of `M_G`.  
\(\square\)

For the middle-level incidence ground,

\[
 |\mathcal E|\le I=W(m+1),
 \qquad
 \log(2I)\le3m\quad(m\ge2).                                    \tag{4.8}
\]

Consequently:

* \(D\le Cm\) and \(B\le B_0\) imply row bound
  \(((\mathrm e-1)C+3B_0)m\);
* \(D\le Cdm\) and \(B\le B_0d\) imply row bound
  \(((\mathrm e-1)C+3B_0)dm\).

The finite system (4.1)--(4.2) is the promised pressure formulation.  It is
strictly stronger than Hall but weaker than first exhibiting an integral
row-sparse SDR.

For task-dependent guarded menus, use every eligible pair \(q=(\tau,e)\) as
a probe.  Define \(w_q(f)\) to be the maximum normalized conflict from the
guarded list at \((\tau,e)\) to the guarded list of any task eligible at \(f\).
Impose (4.2) for every probe.  The same proof unions over the number \(Q\) of
eligible pairs and replaces \(\log(2|\mathcal E|)\) by \(\log(2Q)\).  Since
\(Q\) is at most the product of two middle-level-scale grounds,
\(\log Q=O(m)\).  After the base is matched to tasks, the row for every actual
assigned list is bounded by its corresponding probe.  Every all-width
witness, topology, and common-cap conflict must be included in \(w_q\); the
raw local kernel cannot stand in for it.

The fractional-pressure premise has an exact finite dual.  Fix a pressure
cap \(P\).  The system (4.1) together with

\[
                         \sum_a w_q(a)y_a\le P\qquad(q\in Q)       \tag{4.9}
\]

is infeasible if and only if there are unrestricted task potentials \(u_t\)
and nonnegative numbers \(\beta_a,\lambda_q\) such that

\[
 u_t\le\beta_a+\sum_q\lambda_qw_q(a)
 \quad\text{for every eligible }(t,a),                            \tag{4.10}
\]

but

\[
                    \sum_tu_t>
                    \sum_a\beta_a+P\sum_q\lambda_q.              \tag{4.11}
\]

Indeed, multiplying (4.10) by a feasible \(x_{ta}\) and summing contradicts
(4.11); the converse is ordinary LP separation/Farkas duality.  Setting all
\(\lambda_q=0\) recovers the fractional Hall obstruction.  Thus the missing
PBBS/Pascal input can be stated as exclusion of literal weighted
Hall--pressure certificates, rather than an unspecified discrepancy
assumption.

## 5. Degree `m` alone: two exact counterexamples

### Proposition 5.1 (Hall can fail inside a perfect reservoir)

Take any \(m\) mutually private reservoir anchors and \(m+1\) tasks, each
eligible at exactly those \(m\) anchors.  Every task has \(m\) eligible private
incidences, but the task set itself violates Hall by one.

The example can be embedded into a task bank of \(\Theta(W/m)\) by adjoining a
disjoint balanced eligibility component.  Therefore the asserted task
scale does not repair the local cut.

### Proposition 5.2 (literal Catalan-scale source-star obstruction)

Let \(\Omega\) have size \(2m+1\).  Fix a coordinate \(z\), put

\[
                         t=\lceil\log_2m\rceil,                    \tag{5.1}
\]

and fix a \(t\)-set \(R\subseteq\Omega\setminus\{z\}\).  Define

\[
 \mathcal F=\{C\in{\Omega\choose m}:R\subseteq C, z\notin C\}.  \tag{5.2}
\]

For every \(C\in\mathcal F\), create one prescribed task \(\tau_C\) whose
eligible anchors are its complete native outgoing star

\[
                 E_C=\{(C,C+a):a\in\Omega\setminus C\}.           \tag{5.3}
\]

Then:

1. \(|\mathcal F|=\Theta(W/m)\);
2. every task has \(m+1\) eligible literal C6 incidences;
3. the stars `E_C` are pairwise disjoint, so Hall is automatic; and
4. **every** representative assignment has average raw conflict
   \(\Omega(m^2)\) in every selected list.

In particular, choosing the representative `(C,C+z)` for every task gives
separately distinct lower and upper source endpoints, yet does not reduce
the conflict.

#### Proof

After fixing `R` and excluding `z`, choose the remaining `m-t` elements of
`C` from `2m-t` coordinates.  Thus

\[
 |\mathcal F|={2m-t\choose m-t},
 \qquad
 {\binom{2m-t}{m-t}\over\binom{2m+1}{m}}
 =\prod_{j=0}^{t}{m-t+1+j\over2m-t+1+j}
 =2^{-(t+1)}\exp(O(t^2/m))=\Theta(1/m).                           \tag{5.4}
\]

The lower endpoint of an anchor in `E_C` determines `C`, so the eligibility
stars are disjoint and every choice of one representative per task is
injective.

Fix an arbitrary representative

\[
                         e_C=(C,C+a_C)                             \tag{5.5}
\]

for every task.  For each

\[
 x\in C\setminus R,
 \qquad
 c\in\Omega\setminus(C\cup\{z\}),                               \tag{5.6}
\]

put

\[
                         C'=C-x+c\in\mathcal F.                    \tag{5.7}
\]

The `m(m-t)` choices give distinct `C'`.  Set

\[
                              V=C+c=C'+x.                          \tag{5.8}
\]

In the raw C6 list at \(e_C\), the upper owner \(V\) occurs in at least \(m\)
candidates.  If \(a_C=c\), then \(V\) is the fixed upper source and occurs in
all \(m^2\); otherwise it is the one-free owner \(C+c\), obtained by fixing \(c\)
and varying the \(m\) removed coordinates.  The same argument at \(e_{C'}\)
uses \(x\) in place of \(c\).  Hence the two lists contain at least \(m^2\)
actual conflicting candidate pairs sharing \(V\), and

\[
                              w(e_C,e_{C'})\ge1.                   \tag{5.9}
\]

Summing over the distinct neighbours gives, for every selected list,

\[
                    A_{e_C}(S)\ge m(m-t)=\Omega(m^2).             \tag{5.10}
\]

This holds for every representative assignment \(S\).  
\(\square\)

The obstruction also survives the usual \(O(md)\) unary guard loss on
deletion-only sublists of the raw one-to-one C6 catalogue, provided the
surviving packets retain their raw six-owner support.  Suppose at most
\(gmd\) raw candidates are deleted from each selected list.  For a fixed
outside parameter, call its \(m\)-candidate fibre good when at least \(m/2\)
candidates remain; at most \(2gd\) actual parameter fibres per list are bad.

When a graph label equals the chosen source addition \(a_C\), it is not an
actual parameter fibre: the shared owner \(C+a_C\) is fixed in every retained
candidate.  If \(4gd<m\), then the fixed owner retains at least
\(m^2-gmd>m/2\) candidates and this graph label is automatically good.  If
\(a_C\ne z\), the unused actual \(z\)-fibre has no neighbour in
\(\mathcal F\), so the \(m\) relevant graph labels are the fixed label and the
remaining actual fibres.  If \(4gd\ge m\), the right side of (5.11) below is
nonpositive and the bound is trivial.

The Johnson graph in (5.6)--(5.7) is \(m(m-t)\)-regular.  Deleting edges whose
graph label is bad at either endpoint leaves average degree at least

\[
                          (m-t)(m-4gd).                            \tag{5.11}
\]

Every surviving good edge contributes at least \(1/4\) normalized actual
conflict.  Hence some guarded list has row at least

\[
                         {(m-t)(m-4gd)\over4}=\Omega(m^2)          \tag{5.12}
\]

when \(g\) is fixed and \(d=o(m)\).  Arbitrary guarded lifts which identify
candidates or replace the raw support require an additional support and
multiplicity hypothesis; (5.11)--(5.12) do not apply to them automatically.

This is a literal Boolean middle-level incidence/native-C6 counterexample
at the required \(\Theta(W/m)\) scale; no artificial token is introduced.  It
does not satisfy strong source privacy: nearby source centres occur as
zero-free vertices in one another's full lists.  Nor is it proved that a
canonical PBBS child exposes precisely the task bank (5.2)--(5.3).  It
refutes the stated marginal implication, not PBBS reachability under
additional hidden structure.

## 6. Consequences for the additive-constant route

The sparse C6 theorem already supplies the correct physical density and raw
row energy.  The new task assignment has only two proof-safe routes.

### Fixed-reservoir route

Construct the actual guarded task graph inside one authenticated reservoir
\(R_1\) or \(R_2\) and prove Hall.  The local pressure row

\[
                 d_G(\tau)\ge m,qquad d_G(e)\le m                 \tag{6.1}
\]

is sufficient.  Monotonicity then supplies the raw `O(m)` row for free.
For complete packets one must additionally prove that guard/ticket resources
raise it by at most \(O(dm)\).

### Correlated-extraction route

Construct the fractional matching (4.1) with pressure \(D=O(dm)\) and pair
code \(B=O(d)\).  Theorem 4.1 then produces a spread SDR, and Theorem 3.1
selects compatible packets when the guarded lists remain quadratic and
\(d=o(m)\).

An independently extracted density-\(m^{-2}\) reservoir does not
automatically meet prescribed task menus: one task with only \(m\) eligible
full-atlas incidences retains only \(1/m\) eligible anchors in expectation.
Thus extraction and assignment must be correlated, unless task eligibility
inside the frozen reservoir is proved directly.

Finally, local raw spread is not a common-cap theorem.  The complete ticket
rows must use one literal guard and satisfy either explicit disjoint paths
or the all-set Rado/gammoid cuts.  A single cap-one cut vertex shared by two
task menus defeats every local anchor assignment regardless of (2.2) or
(4.2).

## 7. Exact remaining lemma

The all-dimensional bridge may now be stated without an entropy heuristic:

> On one bounded regenerative PBBS/Pascal state, expose the
> \(\Theta(W/m)\) prescribed compound tasks and either:
>
> * map them into one authenticated sparse C6 reservoir with Hall (for
>   example by (6.1)); or
> * give the task transversal matroid a fractional base satisfying
>   \(D=O(dm), B=O(d)\) in (4.2).
>
> Every eligible task--anchor pair must retain \(\Omega(m^2)\) whole guarded
> packets, and the row kernel must include all physical, protected-witness,
> topology, and complete common-cap ticket conflicts under one guard.

This lemma plus Theorems 3.1 and 4.1 gives the required compatible sparse
packet bank.  Neither \(m\) eligible incidences per task nor endpoint privacy
proves it; Proposition 5.2 is the exact obstruction.

## 8. Independent replay and audit scope

The symbolic source-star construction was replayed independently for
\(2\le m\le8\).  The replay enumerates the family \(\mathcal F\), checks that its
native stars are disjoint, and counts actual shared-upper-owner candidate
pairs rather than token-energy surrogates.  In every case the minimum
normalized row is at least \(m(m-t)\).

Artifacts:

* `scratch/audit_k_sparse_c6_prescribed_task_source_star_20260731.py`;
* `scratch/k_sparse_c6_prescribed_task_source_star_20260731.audit.json`;
* canonical replay payload SHA-256
  `86754cfd0c32f81d2dc1c9a7ae2eb2e09f527299e523b82d9aafeae465946f2d`.

Two independent proof audits checked the strong-private \(11m+2\) row count,
the matroid pipage argument, the Farkas signs, and the literal/guarded
counterexample normalization.  The conclusion is deliberately split:
assignment inside a fixed row-sparse reservoir is closed by Hall, while
simultaneous extraction from the full atlas is false under the marginal
degree premise alone.  No PBBS reachability or additive-constant upper bound
is claimed.
