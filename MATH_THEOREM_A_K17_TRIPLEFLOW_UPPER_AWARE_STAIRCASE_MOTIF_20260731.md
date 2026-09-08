# K17 tripleflow: upper-aware pair choices and exact short-run cuts

Date: 2026-07-31  
Status: exact reduction and necessary staircase inequalities; simultaneous
upper/residence selection remains open  
Scope: the frozen `0f6267...` tripleflow core catalogue and its residual
AA/XX/YY/AX/AY pair choices

## 0. Verdict

The present tripleflow factor is an exact lower-q1 2-factor, but it is not a
K17 carrier.  It has 989 cycles, 4,413 immediate-upper holes, and cyclic
short-run populations

\[
                  N_1=0,\qquad N_2=7887,\qquad N_3=7940.       \tag{0.1}
\]

The numbers in (0.1) count maximal cyclic positive runs; they are not
absolute staircase frontiers and therefore cannot themselves be compared
to \(\Delta_{17}=7401\).

The proposed dichotomy “the budget permits some length-three runs but
forbids every length-two run” is false.  For a final lower-rainbow path the
canonical tail-start schedule satisfies the sharp necessary inequality

\[
                         2n_2+n_3\le7401,                         \tag{0.2}
\]

where \(n_i\) counts its interior runs of length \(i\).  Thus early
length-two runs are allowed.  However, if \(r_i\) denotes the number of old
length-\(i\) motifs retained as interior runs, then among the 15,827 old
motifs the maximum-cardinality tail-start retention face is uniquely

\[
                     (r_2,r_3)=(0,7401).                          \tag{0.3}
\]

On that *optimization face*, but not for feasibility in general, all 7,887
old length-two motifs must be broken and 539 old length-three motifs must be
broken.  With arbitrary starts the exact count consequence is only

\[
                            n_2+n_3\le7401.                        \tag{0.4}
\]

The useful constructive reduction is therefore an upper-aware pair-choice
model with:

1. exact lower-colour and owner-degree equations;
2. one at-least-one row of arity at most 36 for every rank-ten upper target;
3. exact local `toggle--11--toggle` clauses for length-two runs; and
4. exact motif indicators feeding (0.2), (0.4), or the full positional
   staircase automaton.

This is materially stronger than the three independent incidence flows,
but no satisfying simultaneous upper/residence selection is presently
authenticated.

## 1. Frozen baseline and lineage

The attachment assignment is

```text
scratch/k17_pbbs_u_yaux_cap3_anneal_20260731.tsv
SHA-256 e7a566d8a9e846c406cd67b2a234acbabaecddeaa286f384e2c0355dd5406323
```

and the materialized core bank is

```text
scratch/k17_pbbs_u_yaux_tripleflow_bridge_20260731.fragments
SHA-256 0f6267a487916ff2ee2aa04b3656d4a2b24aa7a72a057e87c39b381cfddfa25d

scratch/k17_pbbs_u_yaux_tripleflow_bridge_20260731.tsv
SHA-256 065f03bd0896c7578a6b8a61c44a93d626294048457b7ba3475d945f18876a19

scratch/k17_pbbs_u_yaux_tripleflow_bridge_20260731.audit.json
SHA-256 d915ce52e543507674d2384b630d8eb0aa210cd0a3b905cd087d73c69291c8ad
payload f6558b94f1e377df6f82f75955de4d3a67fd640d583f94e5e1d0733dd1d92f7e
```

It consists of 1,430 disjoint Johnson paths, 9,295 owners, and 7,865
pairwise-distinct internal lower colours.  It has 715 left and 715 right A
attachments and no internal positive run of length one or two.

The arbitrary residual factor is

```text
scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.components
SHA-256 2a388a4585c953ab3e7b3f70b26a1ac8160cf414a66b99c9b72436bac3266b93

scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.tsv
SHA-256 39fe645656fe199600bd564bccc218d770752910cd1d6cb66aeebb8ad2bcaad8

scratch/k17_pbbs_u_tripleflow_residual_factor_20260731.audit.json
SHA-256 f9daf5e8ac7cb47d4b148789fcddcbd0d1a53030f6a9e0d173a892ed78063350
payload 520c709b458a772e9bb1e7727b558b72a3d1b1c8fafb0b95672dfc5d5dec9323
```

Literal replay gives 24,310 owners and edges, degree two at every owner,
all 24,310 lower colours exactly once, and 989 cycles.  Its residual graph
edges have types

\[
 AA=5005,\quad XX=5005,\quad YY=5005,\quad AX=715,\quad AY=715. \tag{1.1}
\]

The audit field `AA_incidence_edges=10010` counts the two A incidences of
the 5,005 AA graph edges; it is not an edge count.

Immediate-upper coverage is 15,035 of 19,448.  The exact missing split by
new-coordinate signature is

\[
\begin{array}{c|rrrr}
\text{signature}&00&x&y&xy\\ \hline
\text{missing}&0&1465&1457&1491.
\end{array}                                                       \tag{1.2}
\]

Thus the pure-old upper-q1 shore is complete and every one of the 4,413
debts is tagged.  Deeper upper holes are 3,486 at rank 11, 1,104 at rank 12,
and 100 at rank 13.

There are two lineage cautions.  The generator that produced the attachment
assignment is not frozen locally, and the current residual-flow source file
points to an older balanced-flow bank rather than byte-identically producing
the tripleflow residual filenames.  The materialized files and their audit
are explicit, but producer lineage is incomplete.

## 2. Exact residual pair-choice model

Let \(E=[15]\) and let \(x,y\) be the new coordinates.  Owners are

\[
 U_V=V,\quad X_T=T+x,\quad Y_T=T+y,\quad A_C=C+x+y,
\]

where \(|V|=9,|T|=8,|C|=7\).  Let \(F\) be the fixed core-edge set.  Every
residual choice \(q\) selects one literal Johnson edge \(e(q)\), with lower
colour \(\lambda(q)=\bigcap e(q)\) and upper colour
\(\mu(q)=\bigcup e(q)\).  The five choice types are

\[
\begin{array}{c|c|c}
q&\lambda(q)&\mu(q)\\ \hline
AA(D;C_1,C_2)&D+xy&(C_1\cup C_2)+xy\\
XX(C;T_1,T_2)&C+x&(T_1\cup T_2)+x\\
YY(C;T_1,T_2)&C+y&(T_1\cup T_2)+y\\
AX(C;T)&C+x&T+xy\\
AY(C;T)&C+y&T+xy.
\end{array}                                                       \tag{2.1}
\]

Here \(|D|=6\), \(D\subset C_i\), and \(C\subset T_i,T\).  The attachment
side and residual owner capacities determine which displayed choices are
available.  Write \(z_q\in\{0,1\}\), let \(d_F(v)\) be the fixed degree of
owner \(v\), and let \(b_Z=1\) iff a fixed edge has upper colour \(Z\).

### Theorem 2.1 (exact upper-aware factor equivalence)

A choice vector \(z\) gives a spanning degree-two factor retaining \(F\),
using every lower colour exactly once and covering every rank-ten upper
target, if and only if

\[
 \sum_{q:\lambda(q)=R}z_q=1                                      \tag{2.2}
\]

for every residual lower-colour row \(R\),

\[
 \sum_{q:v\in e(q)}z_q=2-d_F(v)                                  \tag{2.3}
\]

for every owner \(v\), and

\[
 b_Z+\sum_{q:\mu(q)=Z}z_q\ge1                                   \tag{2.4}
\]

for every rank-ten target \(Z\).

#### Proof

Equation (2.3) gives degree two after adding the fixed edges.  Equation
(2.2), together with the pairwise-distinct fixed lower colours, gives one
edge of every rank-eight colour and no repetition.  Equation (2.4) is
literally the assertion that \(Z\) is the union of the endpoints of at least
one selected or fixed edge.  These prove sufficiency.  Reading the lower
colour, endpoint incidences, and upper union of any factor in this fixed
catalogue gives (2.2)--(2.4), proving necessity. \(\square\)

### Proposition 2.2 (small upper rows)

Every nontrivial row (2.4) has at most 36 residual choice literals.

#### Proof

For \(Z=V+x\), \(|V|=9\), an XX provider is determined by its rank-seven
core \(C=V\setminus\{a,b\}\), of which there are \(\binom92=36\); the y case
is identical.  For \(Z=S+x+y\), \(|S|=8\), there are at most
\(\binom82=28\) AA providers.  Each of the eight rank-seven facets
\(C\subset S\) supplies at most one residual cross provider: AX if its
attachment is left, AY if it is right, and neither if it is free.  Thus the
total is at most \(28+8=36\).  A 00 target has no residual provider and is
already fixed-covered. \(\square\)

The independent provider census is

```text
scratch/k17_pbbs_u_tripleflow_upper_provider_census_20260731.audit.json
SHA-256 ca03685a0faf8027ef58c4a30f03c292c69546a7bc88f42ae1d99a9164144df2
payload d12f16d77ca421ecb3aadb39f5b438297876c7d815e31eba396ed2859e4db57c
```

It finds provider arity 1 through 36 and 1,916 singleton-provider targets.
This is only rowwise nonemptiness.  The exact upper-aware model source

```text
scratch/solve_k17_pbbs_u_tripleflow_upper_q1_factor_20260731.py
SHA-256 4ce9b27bf43165e3f4216e29653a7946197bf76ae727b8d5f3fca335e50a6414
```

implements (2.2)--(2.4), but there is no frozen SAT witness or UNSAT
certificate.  Its docstring must not be read as a proved feasibility claim.

## 3. Edge states and exact local run clauses

For a coordinate \(t\), call an edge `11`, `00`, or a *toggle* according as
both, neither, or exactly one endpoint contains \(t\).  For an old
coordinate \(t\), the residual choices have states

\[
\begin{array}{c|c|c}
q&11&\text{toggle}\\ \hline
AA(D;a,b)&t\in D&t\in\{a,b\}\\
XX(C;a,b),YY(C;a,b)&t\in C&t\in\{a,b\}\\
AX(C;a),AY(C;a)&t\in C&t=a.
\end{array}                                                       \tag{3.1}
\]

All remaining cases are `00`.  For the new coordinate \(x\), AA, XX, and
AX are `11`, AY toggles, and YY is `00`; interchange \(x,y\) for the mirror
statement.  Fixed edges are classified directly from their endpoint bits.

Let \(a_e=1\) for a fixed edge and \(a_{e(q)}=z_q\) for a choice edge.

### Theorem 3.1 (short-run motif clauses)

In a selected degree-two graph, a finite maximal positive run of length two
is exactly a selected occurrence walk with edge states

\[
                    \text{toggle--11--toggle}.                    \tag{3.2}
\]

A finite maximal positive run of length three is exactly

\[
                 \text{toggle--11--11--toggle}.                  \tag{3.3}
\]

Consequently a particular run-two occurrence with edge set
\(e_1,e_2,e_3\) is forbidden by the exact local clause

\[
                       a_{e_1}+a_{e_2}+a_{e_3}\le2,               \tag{3.4}
\]

and a run-three occurrence is forbidden by

\[
                  a_{e_1}+a_{e_2}+a_{e_3}+a_{e_4}\le3.           \tag{3.5}
\]

For a disconnected factor the catalogue must also include a selected
triangle with bit word \(0,1,1\), a selected four-cycle with bit word
\(0,1,1,1\), and an all-positive selected triangle.  These are respectively
cyclic runs of lengths two, three, and three.  The physical graph is simple,
so there is no two-cycle case.

An interior run of length one would make its two incident lower colours
equal to the positive owner with that coordinate deleted.  Hence (2.2)
already excludes every run-one occurrence.

#### Proof

At the left boundary of a positive run the coordinate toggles from zero to
one; every internal edge is `11`; and at the right boundary it toggles back
to zero.  Conversely those edge states give exactly the displayed maximal
run.  Substituting fixed edges by one and choice edges by their Booleans
gives (3.4) and (3.5).  Closing the two exterior zeros to one vertex gives
the triangle/four-cycle cases, while a three-cycle wholly positive is a
cyclic run of length three.  The run-one assertion follows from lower-colour
simplicity as stated. \(\square\)

The clauses must mix families: a short run can pass from an AA edge through
an AX edge into an XX edge, or through fixed core edges.  Same-family-only
enumeration is unsound.  A proof-safe generator enumerates canonical
nonbacktracking walks of two, three, and four edges in the occurrence graph,
tests bit words `010`, `0110`, `01110`, substitutes fixed edges, rejects
conjunctions already impossible under (2.2)--(2.3), and canonicalizes
reversal.  Closed triangles and four-cycles are added separately and
canonicalized under rotation and reversal.

## 4. Staircase population inequalities

Let \(P=(v_0,\ldots,v_{W-1})\), \(W=24310\), be a final lower-rainbow
Johnson path.  Let \(n_2,n_3\) be the numbers, over all 17 coordinates, of
its interior positive runs of lengths two and three.

Every oriented Johnson edge deletes exactly one coordinate and inserts
exactly one coordinate.  Therefore distinct finite positive runs have
distinct start edges and distinct end edges.

### Theorem 4.1 (tail-start count cut)

For the canonical tail-start schedule,

\[
             n_2\le\rho_2,\qquad n_2+n_3\le\rho_3.                \tag{4.1}
\]

In particular, staircase feasibility implies (0.2).

#### Proof

Interior run starts are positive indices.  The starts of all length-two
runs are distinct and at most \(\rho_2\), proving the first inequality.  The
starts of all length-two or length-three runs are distinct and at most
\(\rho_3\), proving the second.  The canonical scalar cost is
\(\rho_2+\rho_3\le7401\). \(\square\)

For the old motif bank (0.1), its tail weight is

\[
                   2(7887)+7940=23714.                             \tag{4.2}
\]

Thus a path retaining old motif occurrences must remove, lengthen, or make
boundary-exempt at least 16,313 units of this weight.  Maximizing the number
of retained old motifs subject to (0.2) gives (0.3), so at least 8,426 old
motif occurrences must fail to survive as interior short runs.  This is a
motif-occurrence bound, not a lower bound of 8,426 edge edits: one changed
edge can hit several motifs.

### Theorem 4.2 (arbitrary-start count cut)

Write \(\alpha_i=W-\delta_i\), with
\(W\ge\delta_1\ge\delta_2\ge\delta_3\ge0\), and let
\(g(t)=|\{i:\alpha_i\le t\}|\).  When run one is absent,
\(\delta_3=0\) is without loss.  Define

\[
\begin{aligned}
R_2&=\max\bigl(\{s:\text{a run two starts at }s, g(s+2)=0\}\cup\{0\}\bigr),\\
R_3&=\max\bigl(\{s:\text{a run two starts at }s, g(s+2)\le1\}\\
   &\hspace{45mm}\cup\{s:\text{a run three starts at }s, g(s+3)=0\}
     \cup\{0\}\bigr).
\end{aligned}                                                   \tag{4.2a}
\]

These are the adjusted frontiers \(\rho_2^\delta,\rho_3^\delta\).  The exact
candidate schedule has \(\tau=(0,R_2,R_3)\), must satisfy
\(0\le R_2\le R_3\le W\) and \(R_2\le\alpha_2\), and has full loss

\[
 \begin{split}
 L={}&\delta_1+\delta_2+R_2+R_3\\
    &+\mathbf1[\alpha_1<R_2]+\mathbf1[\alpha_1<R_3]
      +\mathbf1[\alpha_2<R_3].
 \end{split}                                                       \tag{4.3a}
\]

At the K17 threshold, the exact scalar test simplifies to

\[
 \min_{W\ge\delta_1\ge\delta_2\ge0}
     \bigl(\delta_1+\delta_2+R_2+R_3\bigr)\le7401.                \tag{4.3}
\]

Every feasible path satisfies (0.4).

#### Proof

A length-two run ending immediately before position \(t\) contributes to
both \(R_2,R_3\) when \(g(t)=0\), to \(R_3\) only when \(g(t)=1\), and is
shielded when \(g(t)\ge2\).  A length-three run contributes to \(R_3\) when
\(g(t)=0\) and is shielded when \(g(t)\ge1\).  A third start threshold can
therefore improve neither frontier, so setting \(\delta_3=0\) only decreases
cost.

If the four-term base in (4.3) is at most 7,401, then

\[
 \alpha_1=W-\delta_1
    \ge W-(7401-R_3)=16909+R_3>R_3\ge R_2.
\]

Since \(\alpha_2\ge\alpha_1\), legality holds and every indicator in
(4.3a) vanishes.  Conversely, if the full legal loss (4.3a) is at most
7,401, its nonnegative four-term base is at most 7,401 and the same argument
again forces all three indicators to vanish.  Thus (4.3) is genuinely exact,
not a relaxation.

Every unshielded short run has a distinct positive start at most \(R_3\),
so there are at most \(R_3\) of them.  Every shielded run has its distinct
ending edge in \([\alpha_1,W-1]\), a set of \(\delta_1\) edges.  Hence

\[
              n_2+n_3\le R_3+\delta_1
                 \le \delta_1+\delta_2+R_2+R_3\le7401.
\]

This proves (0.4). \(\square\)

The exact position implications for a surviving run with zero-based start
\(s\) are useful in a positional model.  For a run two put \(t=s+2\):

\[
 t<\alpha_1\Longrightarrow s\le R_2,\qquad
 t<\alpha_2\Longrightarrow s\le R_3.                              \tag{4.4}
\]

For a run three put \(t=s+3\):

\[
 t<\alpha_1\Longrightarrow s\le R_3.                              \tag{4.5}
\]

The sharp one-run loss formula gives the threshold-free necessary bands

\[
\begin{array}{ll}
\text{run two:}&s\le3700\quad\hbox{or}\quad s\ge20608,\\
\text{run three:}&s\le7401\quad\hbox{or}\quad s\ge16906.
\end{array}                                                       \tag{4.6}
\]

Tail starts remove the late alternatives.

## 5. Exact PB interface and present boundary

For every coordinate-occurrence-labelled potential motif \((t,M)\),
introduce \(u_{t,M}\) as the exact conjunction of its edge literals:

\[
 u_{t,M}\le a_e\quad(e\in E(M)),\qquad
 u_{t,M}\ge\sum_{e\in E(M)}a_e-|E(M)|+1.                        \tag{5.1}
\]

The coordinate label is essential: one selected edge tuple may support
short runs in several coordinates, and each is a separate contribution.
After a concrete final opening/rethread identifies which motifs remain
interior, and after the motif catalogue has been rebuilt to include every
replacement seam, (4.1) gives the cheap necessary cut

\[
           2\sum_{(t,M)\in\mathcal M_2}u_{t,M}+
             \sum_{(t,M)\in\mathcal M_3}u_{t,M}\le7401          \tag{5.2}
\]

for tail starts, while Theorem 4.2 gives

\[
 \sum_{(t,M)\in\mathcal M_2\cup\mathcal M_3}u_{t,M}\le7401    \tag{5.3}
\]

for arbitrary starts.  These are necessary count projections, not
sufficient positional schedules.  On a disconnected preliminary 2-factor
they are safe only after either fixing the eventual switches/opening or
interpreting \(u_{t,M}\) as *retained* motif variables.  Rethreading may destroy
old motifs and create new seam motifs.

The cleanest cheap selection-side precondition is the following, conditional
on a motif-preserving final fusion/opening and the front-loading order below:

* on the rebuilt final seam catalogue, impose every exact run-two no-good
  (3.4), including mixed-family and closed-triangle cases;
* retain the authenticated core's finite run-three bank for later
  front-loading; and
* either forbid every newly created run-three motif or carry its indicator
  into the exact run-summary/order model.

The frozen tripleflow core itself has no run one or two; a literal replay
finds 182 internal run-three occurrences in 157 components, all on old
coordinates.  Their total current span is 2,210.  Thus, conditionally on
placing these 157 components in one initial dangerous segment, inserting
only \(g\) other connector owners before its end, and creating no other run
of length at most three, the exact tail bound is

\[
                         \rho_3\le2206+g.                           \tag{5.4}
\]

Consequently \(g\le5195\) fits the 7,401 budget.  Under the stronger
component-contiguous balanced-packet hypothesis in which each dangerous
component lies in its own initial packet and contributes at most eleven
additional non-U owners before the packet end, \(g\le11(157)=1727\) and
\(\rho_3\le3933\).  These are conditional ordering certificates, not
properties of the present 989-cycle factor.

None of this proves that the upper rows (2.4), owner degrees, and the
no-run-two clauses have a common solution.

The exact next theorem is therefore: solve (2.2)--(2.4) jointly with the
mixed-family run-two clauses, then connect/open the selected factor while
preserving upper-q1 and placing every retained run-three/seam motif inside a
legal (4.3) chronology.  Deeper upper shadows and the common-Q compiler
remain subsequent gates.  The current 989-cycle factor and the inequalities
above prove neither feasibility nor impossibility of that system.
