# Punctured weighted bites: the exact LP dual and a two-edge induced obstruction

**Date:** 2026-08-22  
**Status:** unconditional reduction and punctured-geometry counterexample;
no claim that the actual nibble reaches the counterexample

This note specializes edge-dependent isolated marking to the directed
punctured-configuration hypergraph.  It gives:

1. the exact linear program for simultaneously balancing target deletion
   loads and first-order rooted degree erosion;
2. its Farkas dual;
3. an exact expansion of the duplicate part in the boundary-codegree basis;
4. for every `r>=3`, an induced punctured residual on two overlapping edges
   in which no nonzero balanced-load rate exists.

The last item rules out a theorem asserting that every induced punctured
residual admits a self-regularizing weighted bite.  It does not rule out a
history theorem saying that the actual matching process avoids these
residuals, nor a priority algorithm which deliberately removes such a gadget.

## 1. The primal system

Put `b=2r+1`.  A directed punctured configuration has `k=2r` middle
targets and `k=2r` lower targets.  Let `H` be any nonempty induced residual,
with target shores `V_M,V_L`, edge set `E(H)`, and positive target degrees
`d(v)`.  Targets of degree zero may be removed before forming the system.
Write

\[
             n_\sigma=|V_\sigma|,
 \qquad      Z=|E(H)|,
 \qquad      \sigma\in\{M,L\}.                     \tag{1.1}
\]

Give every surviving configuration `G` a nonnegative rate `lambda_G` and
normalize

\[
                              \sum_G\lambda_G=1.     \tag{1.2}
\]

The target load is

\[
                              q_v=\sum_{G\ni v}\lambda_G.       \tag{1.3}
\]

If it is constant on each shore, double-counting incidences forces

\[
                  q_v=q_\sigma:={k\over n_\sigma}
                  \qquad(v\in V_\sigma).             \tag{1.4}
\]

For two surviving configurations put

\[
             D(F,G)=\bigl(|F\cap G|-1\bigr)_+,       \tag{1.5}
\]

and define the rooted duplicate-exposure matrix

\[
 P_{vG}={1\over d(v)}\sum_{F\ni v}D(F,G).            \tag{1.6}
\]

The arbitrary-rate drift identity gives, under (1.4),

\[
 e_v=kq_M+kq_L-q_\sigma-\sum_G P_{vG}\lambda_G,
                   \qquad v\in V_\sigma.             \tag{1.7}
\]

Thus balanced target hazards and shorewise balanced rooted erosion are
equivalent to the following finite linear feasibility problem:

\[
 \boxed{
 \begin{aligned}
  &\lambda_G\ge0,\\
  &\sum_{G\ni v}\lambda_G=q_\sigma
                       &&(v\in V_\sigma),\\
  &\sum_G P_{vG}\lambda_G=\rho_\sigma
                       &&(v\in V_\sigma),
 \end{aligned}}                                      \tag{1.8}
\]

where `rho_M,rho_L` are free real variables.  The load equations already
imply (1.2), because summing them on either shore gives
`k sum_G lambda_G=n_sigma q_sigma=k`.

Solving only the first two lines of (1.8) is a balanced fractional target
load.  The third line is an independent duplicate-exposure constraint; it
is not implied by fractional matching feasibility.

## 2. Exact Farkas dual

For a target `v`, let `y_v` be dual to the load equation and `z_v` dual to
the duplicate-exposure equation.  The free variables `rho_sigma` force

\[
                         \sum_{v\in V_\sigma}z_v=0
                         \qquad(\sigma=M,L).          \tag{2.1}
\]

### Theorem 2.1 (dual criterion)

System (1.8) is feasible if and only if the following implication holds for
every pair of real target weightings `(y,z)` satisfying (2.1):

\[
 \left.
 \begin{array}{ll}
 \displaystyle
 \sum_{v\in G}y_v+\sum_vz_vP_{vG}\ge0
                  &\text{for every }G\in E(H)
 \end{array}
 \right\}
 \Longrightarrow
 \boxed{
 \sum_{\sigma\in\{M,L\}}{k\over n_\sigma}
                   \sum_{v\in V_\sigma}y_v\ge0.}    \tag{2.2}
\]

Consequently, a pair `(y,z)` for which every edge expression on the left is
nonnegative but the boxed quantity is negative is an exact infeasibility
certificate.

#### Proof

Write (1.8) as

\[
 A\lambda=q,\qquad P\lambda-S\rho=0,qquad\lambda\ge0,          \tag{2.3}
\]

where `S` is the two-column shore-indicator matrix.  The vector `(y,z)`
annihilates the free `rho` columns exactly when `S^Tz=0`, which is (2.1).
Its value on the column of `lambda_G` is the edge expression in (2.2), and
its value on the right-hand side is the boxed expression.  The conic form of
Farkas's lemma now gives (2.2), with both necessity and sufficiency.
The sign can also be checked directly from a feasible point:

\[
 \sum_G\lambda_G\left(\sum_{v\in G}y_v+
                         \sum_vz_vP_{vG}\right)
 ={k\over n_M}\sum_{v\in V_M}y_v
  +{k\over n_L}\sum_{v\in V_L}y_v
  +\sum_{\sigma\in\{M,L\}}\rho_\sigma
                         \sum_{v\in V_\sigma}z_v.   \tag{2.4}
\]

The last sum vanishes by (2.1), leaving exactly the boxed right side of
(2.2), so nonnegative edge expressions force its nonnegativity.
\(\square\)

The dual separates two possible failures.  Taking `z=0` tests whether a
balanced fractional target load exists at all.  Nonzero zero-shore-sum `z`
tests the additional rooted duplicate balance after target loads have been
made exact.

## 3. Boundary-codegree representation of the dual matrix

For every integer `t>=0`,

\[
               (t-1)_+=\sum_{j=2}^t(-1)^j{t\choose j}.          \tag{3.1}
\]

Apply (3.1) to `t=|F cap G|` and interchange the target-subset and
configuration sums in (1.6).  This gives the exact identity

\[
 \boxed{
 P_{vG}={1\over d(v)}
   \sum_{\substack{T\subseteq G\\|T|\ge2}}
       (-1)^{|T|}\,d_H(T\cup\{v\}).}                \tag{3.2}
\]

Here `d_H(S)` is the number of residual punctured configurations containing
all targets in `S`; if `v in T`, the union in (3.2) is just `T`.

For a full punctured configuration `G`, its targets are the edges of the
punctured boundary graph `B_r`, so every `T` in (3.2) is a boundary
subgraph of `G`.  If a summand `d_H(T union {v})` is nonzero, choose any
residual configuration `F` containing `T union {v}` and represent that
whole family in the boundary graph of `F`.  The proved full-hypergraph
estimate then supplies

\[
       d_H(T\cup\{v\})\le d_{\mathcal C_r}(T\cup\{v\})
       \le C^{|T\cup\{v\}|}D_M r^{2-q_F(T\cup\{v\})}.       \tag{3.3}
\]

Here `q_F(S)` is the number of boundary cuts used by the target family `S`
in the containing configuration `F`.

Equation (3.2) is the requested boundary specialization of the weighted
Gate-A LP.  It also exposes the exact limitation of using (3.3) alone: the
denominator in (3.2) is the *current* degree `d_H(v)`, which may be much
smaller than `D_M`.  Absolute full-hypergraph codegrees do not establish
dual feasibility for an arbitrary induced residual.

## 4. A two-edge induced punctured residual

We now construct an exact obstruction inside the punctured geometry.  Work
on `Omega={0,1,...,2r}`.  For a permutation
`u=(u_0,...,u_(2r))`, read indices modulo `b=2r+1` and put

\[
 I_h^u(s)=\{u_s,u_{s+1},\ldots,u_{s+h-1}\},
\]

\[
 E(u)=\{(M,I_r^u(s)):1\le s\le2r\}
       \mathbin{\dot\cup}
       \{(L,I_{r-1}^u(s)):1\le s\le2r\}.           \tag{4.0}
\]

The shore tags in (4.0) are part of each target.  Take

\[
 w=(0,1,\ldots,2r-2,2r-1,2r),
 \qquad
 w'=(0,1,\ldots,2r-2,2r,2r-1).                     \tag{4.1}
\]

Thus `w'` swaps the final two entries of `w`.  Put

\[
                         E=E(w),\qquad E'=E(w'),
 \qquad                    U=E\cup E'.              \tag{4.2}
\]

Retain exactly the targets in `U`, on both shores, and let `H_U` be the
induced punctured-configuration residual.

### Lemma 4.1 (the union induces exactly two configurations)

For every `r>=3`,

\[
                       E(H_U)=\{E,E'\}.              \tag{4.3}
\]

Moreover, in each shore `E` and `E'` have `2r-2` common targets and two
private targets.  Thus

\[
 |E\cap E'|=4r-4,qquad |U|=4r+4,qquad
 |U\cap V_M|=|U\cap V_L|=2r+2.                     \tag{4.4}
\]

#### Proof

For the base word write

\[
 M_s=I_r^w(s),\qquad L_s=I_{r-1}^w(s),qquad1\le s\le2r,
                                                                    \tag{4.5}
\]

and use primes for `w'`.  Swapping the adjacent entries
`a=2r-1,b=2r` changes a cyclic interval exactly when the interval contains
one of `a,b` but not the other.  Directly from its two boundary cuts, the
only changed targets are

\[
 M_r,M_{2r},L_{r+1},L_{2r},                         \tag{4.6}
\]

and their four primed replacements.  This proves the counts in (4.4).

The containment graph of any punctured configuration is the alternating
path

\[
 L_1-M_1-L_2-M_2-\cdots-L_{2r}-M_{2r}.             \tag{4.7}
\]

The containment graph induced by `U` can be read completely from the sets
in (4.5)--(4.6).  It has the common initial path ending at `L_r`, followed
by the two internally disjoint branches

\[
 \begin{array}{ccccc}
 &M_r&-&L_{r+1}&\\[-1mm]
 L_r&&&&M_{r+1},\\[-1mm]
 &M'_r&-&L'_{r+1}&
 \end{array}                                        \tag{4.8}
\]

where both displayed branches join `L_r` to `M_(r+1)`.  It then has the
common path from `M_(r+1)` through `M_(2r-1)`, followed by the two tails

\[
 \begin{array}{ccccc}
 &&L_{2r}&-&M_{2r}\\[-1mm]
 M_{2r-1}&&&&\\[-1mm]
 &&L'_{2r}&-&M'_{2r},
 \end{array}                                        \tag{4.9}
\]

with the two middle targets at the right as alternative endpoints.  The
unchanged initial and middle portions are exactly their corresponding
subpaths in (4.7).  These are all containment edges: for each lower target,
delete one point from each listed middle `r`-set and compare with the four
exceptional `(r-1)`-sets in (4.6).  Every unlisted comparison differs in at
least two points.

Any configuration contained in `U` has `2r` targets on each shore and its
full containment graph is a path of the form (4.7).  Inspection of
(4.8)--(4.9) gives the following exact four-candidate classification: it
uses every common path vertex, one whole two-vertex branch in (4.8), and
one whole two-vertex tail in (4.9).  For completeness, this is also a short
graph deletion check.  The union graph has `4r+4` vertices and `4r+4`
edges; its leaves are `L_1,M_(2r),M'_(2r)`, its degree-three vertices are
`L_r,M_(r+1),M_(2r-1)`, and every other vertex has degree two.  If `R` is
the four-vertex complement of an induced path candidate, then `R` has two
vertices in each shore and

\[
 \sum_{x\in R}\deg_U(x)-e_U(R)=5.                 \tag{4.9a}
\]

Here `deg_U` and `e_U(R)` are respectively degree and induced-edge count in
this union containment graph.

Propagating connectivity from the three degree-one vertices through the
degree-two common portions in (4.8)--(4.9), while resolving the three
degree-three junctions, forces `R` to be one complete branch and one
complete tail; explicitly,

\[
 R=R_1\cup R_2,\quad
 R_1\in\bigl\{\{M_r,L_{r+1}\},\{M'_r,L'_{r+1}\}\bigr\},\quad
 R_2\in\bigl\{\{L_{2r},M_{2r}\},\{L'_{2r},M'_{2r}\}\bigr\}. \tag{4.9b}
\]

Conversely, each of those four choices leaves an induced alternating path.
This proves the classification without assuming that an arbitrary
alternating path is a cyclic-window path.

It remains to exclude the two mixed choices.  For a genuine punctured path
indexed by a word `u`, its canonically oriented same-start pairs satisfy

\[
 M_s\setminus L_s=\{u_{s+r-1}\},\qquad1\le s\le2r. \tag{4.9c}
\]

The common pairs, the chosen branch in (4.8), and the chosen terminal
same-start pair therefore reconstruct all word positions except `r-1`; the
unique unused symbol reconstructs that last position.  The two terminal
choices have the same singleton difference `{r-2}`.  Hence the unprimed
first branch reconstructs `u=w`, whereas the primed first branch
reconstructs `u=w'`.  Once `u` is fixed, its terminal two targets are
respectively the unprimed or primed tail in (4.9).  Thus a mixed
branch--tail choice disagrees with the unique word it reconstructs.  The
all-unprimed choice is `E`, and the all-primed choice is `E'`.  This proves
(4.3).  \(\square\)

### Theorem 4.2 (exact punctured balanced-load obstruction)

The induced residual `H_U` admits no nonzero edge-rate vector whose target
loads are constant on each shore.  Consequently the full simultaneous
system (1.8) is infeasible.

#### Proof

Let the rates of `E,E'` be `lambda,mu`.  In either shore there are
`2r-2` common targets, two targets private to `E`, and two private to `E'`.
Their respective loads are

\[
                         \lambda+\mu,\qquad\lambda,\qquad\mu.  \tag{4.10}
\]

If all are equal, (4.10) forces `lambda=mu=0`.

Equivalently, here is a literal Farkas certificate.  Set `z=0`, give every
common target weight `y_v=1`, and give every private target weight

\[
                              y_v=-(r-1).             \tag{4.11}
\]

Each of `E,E'` contains `4r-4` common and four private targets, so its dual
edge expression is zero.  But

\[
 \sum_{v\in U}y_v=(4r-4)-8(r-1)=-4(r-1)<0.          \tag{4.12}
\]

Both shores have size `2r+2`, so the right side of (2.2) is
`(2r/(2r+2)) sum_v y_v<0`.  Theorem 2.1 certifies infeasibility.  \(\square\)

There is also no nonzero rate vector making the rooted erosions `e_v`
constant on all targets, even without load balance.  A common target lies
in both residual edges and has no external conflict row, hence `e_v=0`.
An `E`-private target has `e_v=mu`, while an `E'`-private target has
`e_v=lambda`.  Equality again forces `lambda=mu=0`.

## 5. Scope of the obstruction

Selecting either residual edge covers `4r` of the `4r+4` targets and leaves
only four isolated targets, a fraction `1/(r+1)=o(1)`.  Thus this gadget is
not an obstruction to an algorithm which recognizes it and gives one edge
absolute priority.  It proves the more precise negative statement:

\[
 \boxed{\text{There is no hereditary feasible-rate theorem for all induced
 punctured residuals.}}                              \tag{5.1}
\]

Accordingly, a positive adaptive-weighting proof of Gate A must contain a
history or priority assertion.  The exact remaining alternatives are:

1. prove that before the stopping density the actual process avoids every
   dual certificate of the form (2.2);
2. when such a certificate develops, use it to identify a priority family
   which can be covered with `o(A)` collateral holes; or
3. replace independent rates by a dependent matching-valued bite whose
   finite external rows are controlled directly.

The full boundary-codegree theorem enters the weighted route through
(3.2)--(3.3), but cannot by itself exclude the explicit residual in
Section 4.
