# Three-rank Hall cuts, a poisoned conflict-free core, and the depth-two bowtie

Date: 2026-07-26

Method: pure mathematics.

## 0. Outcome

Let

\[
 n=2m+1,\qquad
 \mathcal X=\binom{[n]}m,\qquad
 \mathcal L=\binom{[n]}{m-1},\qquad
 \mathcal U=\binom{[n]}{m+1},
\]

\[
 W=|\mathcal X|=|\mathcal U|,\qquad
 N_1=|\mathcal L|={m\over m+2}W,\qquad
 d=W-N_1={2W\over m+2}.
\tag{0.1}
\]

The exact capacitated-Hall completion theorem is correct, but it cannot
by itself turn the known conflict-free central-three-layer construction
into the required core.

There are two distinct stages.

1. A conflict-free linear forest `P` has distinct lower and upper colors
   and `W-o(W)` edges.  Before the Hall theorem applies, every missing
   lower color must be inserted while preserving upper injectivity and
   middle degree at most two.  This exactification is a four-resource
   matching problem.  Its matrix contains a determinant-two triangle.
2. Once an exact lower core `F` exists, its uncolored completion is the
   integral max-flow problem already characterized by capacitated Hall.

The first stage is not a cosmetic issue.  The known conflict-free theorem
can be run with a prescribed `O(m)`-edge gadget so that the resulting
`W-o(W)`-edge two-sided-rainbow linear forest has an isolated middle set
`A_*` but uses all `m+1` upper cofacets of `A_*`.  Its singleton residual
Hall cut is

\[
                         2\le0.                         \tag{0.2}
\]

Thus the asymptotic conflict-free conclusion does not imply even
uncolored extendibility, let alone the required exact core.

The cycle count itself is not the obstruction.  If a Hall-admissible exact
core differs from the conflict-free forest in `o(W)` edges, then it has
`o(W)` cycle components automatically.

At depth two, an occurrence of an `(m-2)`-target `S` gangs two depth-one
parents `S\cup\{a\}` and `S\cup\{b\}`.  The three possible pairs on
`a,b,c` have the local incidence matrix

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix},
 \qquad\det=2.                                         \tag{0.3}
\]

Hence the actual `q=2` completion is a colored graph-matching/bowtie
problem, not a directed network flow.  Ordinary max flow survives only
after one parent of every child has already been designated; that
single-parent routing relaxation forgets the required consecutive
two-parent occurrence.

The requested core therefore remains unproved.  The precise positive
theorem still needed is a Hall-aware absorption theorem for the
conflict-free matching, followed at `q=2` by a bowtie/blossom theorem.

---

## 1. All residual Hall cuts in waste-slack form

Let `F` be any graph on `\mathcal X` whose Johnson edges have pairwise
distinct upper colors and whose middle degree is at most two.  It need
not yet cover every lower color.  Put

\[
 \mathcal U_1=u(F),\qquad
 \mathcal U_0=\mathcal U\setminus\mathcal U_1,\qquad
 \delta_F(A)=2-d_F(A).
\tag{1.1}
\]

If `|F|=e`, then

\[
 |\mathcal U_0|=W-e,\qquad
 \sum_A\delta_F(A)=2(W-e).                           \tag{1.2}
\]

Thus the uncolored extension of `F` to a spanning two-factor is the same
capacitated incidence flow as in the exact-core theorem, and is feasible
if and only if

\[
 \sum_{A\in\mathcal A}\delta_F(A)
 \le
 \sum_{U\in\mathcal U_0}\min\{2,d_{\mathcal A}(U)\}
 \qquad(\mathcal A\subseteq\mathcal X),               \tag{1.3}
\]

where `d_{\mathcal A}(U)=|\{A\in\mathcal A:A\subset U\}|`.

There is an exact form which separates Boolean-lattice expansion from the
way the used upper colors are occupied.  For each used `U`, let
`E_U=\{A_U,B_U\}` be the endpoints of the selected Johnson edge.  Define

\[
 \sigma(\mathcal A)
 :=\sum_{U\in\mathcal U}\min\{2,d_{\mathcal A}(U)\}
   -2|\mathcal A|                                      \tag{1.4}
\]

and

\[
 \omega_F(\mathcal A)
 :=\sum_{U\in\mathcal U_1}
 \left(\min\{2,d_{\mathcal A}(U)\}
       -|E_U\cap\mathcal A|\right).                    \tag{1.5}
\]

### Theorem 1.1 (exact waste-slack criterion)

For every `\mathcal A\subseteq\mathcal X`, the Hall cut (1.3) is
equivalent to

\[
 \boxed{\omega_F(\mathcal A)\le\sigma(\mathcal A).}    \tag{1.6}
\]

Moreover `\sigma(\mathcal A)\ge0` for every `\mathcal A`.

#### Proof

The left side of (1.3) is

\[
 2|\mathcal A|-
 \sum_{U\in\mathcal U_1}|E_U\cap\mathcal A|.
\]

Move the used-upper term to the right and add and subtract
`\sum_{U\in\mathcal U_1}\min\{2,d_{\mathcal A}(U)\}`.
The resulting inequality is exactly (1.6).

The bipartite inclusion graph between `\mathcal X` and `\mathcal U` is
`(m+1)`-regular on two shores of size `W`.  It decomposes into perfect
matchings, hence contains a spanning two-regular subgraph.  Sending the
two copies of every `A\in\mathcal A` through that subgraph proves

\[
 2|\mathcal A|
 \le\sum_U\min\{2,d_{\mathcal A}(U)\},
\]

which is `\sigma(\mathcal A)\ge0`. \(\square\)

The criterion shows exactly what a conflict-free matching theorem would
have to control.  It controls `|F|`, color collisions, degree and short
cycles.  It does not compare the used-upper waste `\omega_F` with the
often small universal slack `\sigma`.

For example, for a singleton `\mathcal A=\{A\}`,

\[
 \sigma(\{A\})=m-1,                                   \tag{1.7}
\]

and (1.6) reduces to

\[
 \boxed{
 \delta_F(A)
 \le|\{U\in\mathcal U_0:A\subset U\}|.}                \tag{1.8}
\]

For near-full cuts one also has a useful exact complement form.  If
`\mathcal B=\mathcal X\setminus\mathcal A` and

\[
 n_j(\mathcal B)
 =|\{U:d_{\mathcal B}(U)=j\}|,
\]

then

\[
 \boxed{
 \sigma(\mathcal A)
 =2|\mathcal B|-2n_{m+1}(\mathcal B)-n_m(\mathcal B).} \tag{1.9}
\]

Indeed an upper set contributes zero, one, or two to (1.4) according as
all, all but one, or at most `m-1` of its facets lie in `\mathcal B`.

---

## 2. A conflict-free near core whose singleton Hall cut fails

The cloned transition hypergraph used in the known central-three-layer
construction has vertex classes

\[
 \mathcal L,\qquad\mathcal U,\qquad
 \mathcal X^0,\qquad\mathcal X^1.
\tag{2.1}
\]

For every interval `R\subset U` with `|U\setminus R|=2`, let `A,B` be
the two intermediate middle sets and insert the four lifted edges

\[
                         \{R,U,A^\alpha,B^\beta\},
 \qquad\alpha,\beta\in\{0,1\}.                        \tag{2.2}
\]

The exact degrees in odd dimension are

\[
\begin{aligned}
 d_{\mathcal L}&=2(m+1)(m+2),\\
 d_{\mathcal U}&=2m(m+1),\\
 d_{\mathcal X^\alpha}&=2m(m+1).
\end{aligned}                                         \tag{2.3}
\]

The maximum pair codegree is `2(m+1)`, whereas the maximum degree is
`D=2(m+1)(m+2)`.  The fixed-cycle conflict estimates are unchanged from
the known construction because the Johnson degree is `m(m+1)=Theta(m^2)`.
Thus the fixed-girth conflict-free matching theorem applies and gives
`N_1-o(W)=W-o(W)` lifted edges.

We now prescribe a small legal matching before applying it.

Fix `A_*\in\mathcal X` and enumerate

\[
 A_*=\{a_0,\ldots,a_{m-1}\},\qquad
 [n]\setminus A_*=\{x_0,\ldots,x_m\}.
\]

For `0\le i\le m`, put, with indices on the `a`'s read modulo `m`,

\[
\begin{aligned}
 U_i&=A_*\cup\{x_i\},\\
 P_i&=U_i\setminus\{a_i\},\\
 Q_i&=U_i\setminus\{a_{i+1}\},\\
 R_i&=U_i\setminus\{a_i,a_{i+1}\}.
\end{aligned}                                         \tag{2.4}
\]

### Lemma 2.1 (the poisoned gadget)

The `m+1` lifted interval edges

\[
                         g_i=\{R_i,U_i,P_i^0,Q_i^1\}    \tag{2.5}
\]

form a matching.  Their projected graph is a matching disjoint from
`A_*`, and they use every upper cofacet of `A_*`.

#### Proof

The upper colors `U_i` are distinct.  The lower colors `R_i` are distinct
because `R_i` contains the unique outside point `x_i`.  Every `P_i` and
`Q_i` also contains `x_i`, so middle sets belonging to different indices
are distinct; for one index `P_i\ne Q_i`.  Thus (2.5) is a matching.
Neither endpoint equals `A_*`, while the family `\{U_i\}` is exactly the
set of all `m+1` upper cofacets of `A_*`. \(\square\)

Delete from the cloned hypergraph all color vertices used in (2.5), both
clones of every `P_i,Q_i`, and both clones of `A_*`.  The following
uniform estimate is the point that permits the known theorem to be
reapplied.

### Lemma 2.2 (the residual hypergraph remains regular)

Every undeleted vertex loses only `O(m)` incident lifted edges.  Hence all
remaining degrees are `(1-o(1))D` and the pair-codegree and conflict
bounds retain their required asymptotic form.

#### Proof

Every element `a\in A_*` occurs only `O(1)` times among the ordered pairs
`(a_i,a_{i+1})`.  Consequently a fixed lower set is contained in only
`O(1)` of the deleted middle sets `P_i,Q_i`, except that it may also be
contained in `A_*`.  Each such lower--middle pair has codegree at most
`2(m+1)`.  Its codegree with a deleted upper color is at most four, even
though it can lie in `O(m)` of the `U_i`.  Its total loss is therefore
`O(m)`.

The dual argument applies to a fixed upper set.  To contain some
`P_i=A_*-a_i+x_i`, an upper set must contain the corresponding `x_i` and
all but one point of `A_*`; an undeleted upper set does this for only
`O(1)` indices.  A fixed middle clone is similarly incident with only
`O(1)` deleted lower or upper colors.  Pair codegrees with deleted middle
clones are one in the middle--middle case.  Thus every vertex loses
`O(m)` edges.  Since `D=Theta(m^2)`, the claimed regularity follows.
Deleting vertices cannot increase any codegree or conflict degree.
\(\square\)

Apply the fixed-girth conflict-free matching theorem to the residual
hypergraph, unite its matching with the gadget, and delete one edge from
every remaining projected cycle.  Add every unused middle set as an
isolated vertex.

### Theorem 2.3 (poisoned conflict-free central construction)

There is a spanning two-sided-rainbow Johnson linear forest `P` with

\[
                         |E(P)|=W-o(W)                \tag{2.6}
\]

and `o(W)` path components, such that `A_*` is isolated and every upper
cofacet of `A_*` is used by `P`.  Consequently `P` has no spanning
two-factor extension.

#### Proof

The size, rainbow and component assertions follow from the standard
fixed-girth diagonal argument.  Both clones of `A_*` and of every gadget
endpoint were deleted, so no new projected edge meets the gadget or
`A_*`.  Lemma 2.1 therefore survives in the final linear forest.

For `\mathcal A=\{A_*\}`, the left side of (1.3) is
`\delta_P(A_*)=2`.  All `m+1` upper cofacets of `A_*` lie in
`u(P)`, so the right side is zero.  This is (0.2), and Theorem 1.1
proves nonextendibility.  Equivalently,

\[
 \omega_P(\{A_*\})=m+1>m-1=\sigma(\{A_*\}).
\]

\(\square\)

This theorem does not say that every conflict-free output is poisoned.
It proves that the quantitative conclusion of the known construction
does not imply any of the residual Hall cuts.  A Hall-aware choice or an
absorber is genuinely additional mathematics.

---

## 3. Exactifying the missing lower colors is not a flow

Let `P` be any two-sided-rainbow degree-two graph with `e` edges.  It
misses

\[
                         k=N_1-e                       \tag{3.1}
\]

lower colors.  It has `W-e=d+k` unused upper colors and total middle
deficit `2(d+k)`.

For a missing lower color `R` and unused upper color `U\supset R`, let
`A,B` be the two intermediate middle sets and introduce
`z_{R,U}\in\{0,1\}`.  Exactification of the lower core requires

\[
\begin{aligned}
 \sum_{\substack{U\in\mathcal U_0(P)\\U\supset R}}z_{R,U}&=1
       &&(R\text{ missing}),\\
 \sum_{\substack{R\text{ missing}\\R\subset U}}z_{R,U}&\le1
       &&(U\in\mathcal U_0(P)),\\
 \sum_{\substack{R\subset A\subset U}}z_{R,U}&\le\delta_P(A)
       &&(A\in\mathcal X).
\end{aligned}                                         \tag{3.2}
\]

An integral solution adds exactly the missing lower colors, retains upper
injectivity and preserves middle degree at most two.  But (3.2) is not a
bipartite flow system.

### Proposition 3.1 (determinant-two exactification minor)

Suppose an unused `U` has three facets `A_1,A_2,A_3` for which the three
pair colors `A_1\cap A_2,A_2\cap A_3,A_3\cap A_1` are all missing.  The
corresponding variables, restricted to the middle capacity rows, have
matrix

\[
 \begin{pmatrix}
  1&0&1\\
  1&1&0\\
  0&1&1
 \end{pmatrix}.
\tag{3.3}
\]

Thus the universal exactification matrix is not totally unimodular.  A
particular leave can delete this minor, but the ordinary bipartite
capacitated-Hall theorem does not apply to (3.2) in general.

The proposition identifies why Theorem 1.1 cannot prove existence of the
core: its max-flow theorem starts only after (3.2) has been solved.

The cycle requirement would then be automatic.  If `P` is a linear
forest and an exact core `F` satisfies

\[
                         |E(F)\triangle E(P)|=o(W),     \tag{3.4}
\]

then every cycle component of `F` contains an added edge, and hence

\[
                         c(F)\le|E(F)\setminus E(P)|=o(W).             \tag{3.5}
\]

Accordingly, a Hall-aware `o(W)`-edit absorber for (3.2), not a new
cycle theorem, is the precise missing depth-one result.

---

## 4. The exact higher-depth analogue

Put

\[
 N_2=\binom{n}{m-2}
 ={m(m-1)\over(m+2)(m+3)}W,\qquad
 W-N_2={6(m+1)\over(m+2)(m+3)}W.                     \tag{4.0}
\]

Fix `S\in\binom{[n]}{m-2}`.  Its rank-`m-1` parents are

\[
                         R_a=S\cup\{a\},
 \qquad a\in[n]\setminus S.                           \tag{4.1}
\]

A genuine depth-two occurrence with target `S` has two consecutive
depth-one parents

\[
                         R_a,\ R_b,\qquad a\ne b,       \tag{4.2}
\]

and middle owner

\[
                         X_{ab}=S\cup\{a,b\}.           \tag{4.3}
\]

Thus the target-local occurrence catalogue is an ordinary graph on the
parent vertices `R_a`.  It is exactly the mixed fan graph `B_S`: an edge
`R_aR_b` records a length-two owner window whose intersection is `S`.

Suppose residual parent copies have capacities `c(R)` and owner copies
have capacities `h(X)`.  Even the relaxation which asks for one
occurrence of each depth-two target has variables `w_{S,ab}` with

\[
\begin{aligned}
 \sum_{a<b}w_{S,ab}&\ge1 &&(S),\\
 \sum_{S,b:R_a=S\cup\{a\}}w_{S,ab}&\le c(R_a) &&(R_a),\\
 \sum_{S:S\cup\{a,b\}=X}w_{S,ab}&\le h(X) &&(X).
\end{aligned}                                         \tag{4.4}
\]

Actual factor compatibility adds the requirement that the two parent
occurrences be consecutive in one common path or cycle.

### Theorem 4.1 (the max-flow structure breaks at depth two)

The matrix of (4.4) contains the determinant-two minor (0.3).  Hence the
depth-two occurrence problem is a colored graph `b`-matching with blossom
constraints, augmented by owner and chronology constraints.  It is not a
directed network matrix.

#### Proof

Fix `S` and three outside points `a,b,c`.  Restrict to the parent-capacity
rows `R_a,R_b,R_c` and the occurrence columns `ab,bc,ca`.  Their
incidence matrix is (0.3).  The determinant is two.  Deleting owner or
chronology rows cannot remove this displayed minor from the remaining
system. \(\square\)

There is a conditional max-flow statement, but it is strictly weaker.
If every child demand has already been assigned one designated parent,
then routing child copies through parent copies uses the containment
network

\[
 \binom{[n]}{m-1}\longrightarrow\binom{[n]}{m-2}
\]

and is feasible exactly when

\[
 \sum_{S\in\mathcal B}b(S)
 \le
 \sum_{R\in N(\mathcal B)}c(R)
 \qquad
 \left(\mathcal B\subseteq\binom{[n]}{m-2}\right).      \tag{4.5}
\]

This is ordinary capacitated Hall and has an integral max flow.  But
(4.5) selects only one parent of each child.  It neither constructs the
second parent in (4.2) nor proves that the two are consecutive.  Therefore
it is a nested-flag routing lemma, not the depth-two factor theorem.

---

## 5. Precise surviving theorem

The central-three-layer route would be completed by the following
two-stage statement.

1. Starting from a fixed-girth conflict-free matching, solve the
   determinant-two exactification system (3.2) by `o(W)` edits and choose
   the solution so that every waste-slack inequality (1.6) holds.
2. Use Theorem 1.1 to complete the exact core.  Equation (3.5) then gives
   `c(F)=o(W)` without further work.

For depth two, the analogue must additionally solve the bowtie system
(4.4), including its blossom inequalities and common-path chronology.
The single-parent Hall system (4.5) remains available as a subroutine but
does not replace that theorem.

This is stronger than the previously stated scalar gate and weaker than a
generic colored-factor conjecture: it identifies the exact local
determinant-two obstruction, proves that the existing conflict-free
construction can violate Hall, and isolates the first place where genuine
`q=2` pair coupling destroys max-flow integrality.
