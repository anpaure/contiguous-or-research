# Triangular marked-trace circulation: the new fractional gate

Date: 2026-08-01  
Status: exact all-`k` LP reduction, exact boundary-root criterion, and an
explicit connected rational solution in the first sharp case `k=6`.  The
existing canonical consecutive clock is proved not to be a circulation.
No all-`k` nonemptiness or integral rounding theorem is claimed.

## 0. Outcome

Put

\[
 r=\lceil k/2\rceil,\qquad W=\binom kr,\qquad
 \Lambda=\sum_{s=1}^{r-1}\binom ks,
\]

and

\[
 d=\min\{q:qW+\binom{q+1}{2}\geq\Lambda\},\qquad
 h=(\Lambda-dW)_+.
\]

The optimal triangular fractional chain theorem supplies:

* `d` boundary chains generated jointly by one uniform singleton prefix;
* boundary rank multiplicities `b_s` with `sum_s b_s=h`; and
* residual owner-chain marginals

  \[
                 q_s=\frac{\binom ks-b_s}{W}.          \tag{0.1}
  \]

This note identifies the additional fractional theorem needed to serialize
those chains.  It is an exact **marked trace circulation** problem.  The
rank vector (0.1) is not by itself enough: the tails and heads of the trace
edges must balance as literal order-`d` de Bruijn states.

The canonical consecutive clock from the bounded-chain trace theorem fails
this condition already at `k=6`.  A different balanced clock exists there,
and is given explicitly below.

The corrected implication chain is

\[
 \boxed{
 \begin{array}{c}
 \text{optimal triangular fractional chain factor}\quad\text{(proved)}\\
 \Downarrow\\
 \text{connected marked trace circulation with histogram }q
       \quad\text{(new fractional gate)}\\
 \Downarrow\\
 \text{one-edge-per-owner coloured Euler rounding and root absorber}
       \quad\text{(integral gate).}
 \end{array}}
\]

## 1. The exact marked-trace LP

Let

\[
                     \mathcal A=2^{[k]}\setminus\{\varnothing\}.
\]

An order-`d` trace edge is a word

\[
                         e=(B_0,B_1,\ldots,B_d),       \tag{1.1}
\]

with tail and head

\[
 \partial^-e=(B_0,\ldots,B_{d-1}),\qquad
 \partial^+e=(B_1,\ldots,B_d).                        \tag{1.2}
\]

Its owner and proper suffix cells are

\[
 T(e)=\bigcup_{i=0}^d B_i,\qquad
 S_j(e)=\bigcup_{i=d-j+1}^d B_i\quad(1\leq j\leq d). \tag{1.3}
\]

A marked trace atom is a pair `(e,J)`, where

* `|T(e)|=r`;
* `J subseteq {1,...,d}`; and
* the sets `S_j(e)`, `j in J`, are distinct and have rank below `r`.

The marked cells are nested automatically.  Let `x_(e,J)>=0` be the atom
weight.  The **triangular marked-trace system** consists of

\[
 \sum_{(e,J):T(e)=T}x_{e,J}=1
 \qquad\left(T\in\binom{[k]}r\right),                 \tag{1.4}
\]

\[
 \sum_{(e,J):S\in\{S_j(e):j\in J\}}x_{e,J}
       =1-\frac{b_{|S|}}{\binom{k}{|S|}}
 \qquad(\varnothing\neq S,\ |S|<r),                  \tag{1.5}
\]

and the literal de Bruijn balance equations

\[
 \sum_{(e,J):\partial^-e=v}x_{e,J}
   =\sum_{(e,J):\partial^+e=v}x_{e,J}
 \qquad(v\in\mathcal A^d).                            \tag{1.6}
\]

Equation (1.4) is owner-perfectness, (1.5) is the residual lower palette,
and (1.6) is zero expected boundary imbalance.

### Theorem 1.1 (exact joint fractional reduction)

Fix the triangular boundary board and its multiplicities `b_s`.  A
fractional selection of its boundary chains and owner traces covers every
strict-lower target exactly once and has zero expected trace-boundary
imbalance if and only if (1.4)--(1.6) is feasible.

#### Proof

Choose a uniform permutation `pi` of `[k]` and put

\[
                         A_i=\{\pi_i\}\quad(1\leq i\leq d).
\]

The selected boundary cell `(i,s)` is the literal suffix

\[
                       \{\pi_{i-s+1},\ldots,\pi_i\}.
\]

It is a uniform rank-`s` target, so all boundary addresses together give a
fixed rank-`s` target weight `b_s/binom(k,s)`.

Equation (1.5) supplies exactly the complementary weight.  Equation (1.4)
uses one unit of trace mass at every middle owner.  Finally, the coefficient
of a state `v` in the de Bruijn boundary of the selected trace measure is
the left side minus the right side of (1.6).  Hence (1.6) is precisely zero
expected imbalance.  These observations prove both directions. \(\square\)

Summing (1.5) over targets of rank `s`, then using (1.4), gives the rank
histogram

\[
 \sum_{e,J}x_{e,J}\,
       |\{j\in J:|S_j(e)|=s\}|=\binom ks-b_s=Wq_s.     \tag{1.7}
\]

After averaging any solution under `Sym(k)`, every owner remains of mass
one and every target of a fixed rank has equal load.  Thus the all-`k`
fractional question may be stated as membership of `q` in the projection of
the `Sym(k)`-invariant circulation polytope.  It is important that this is a
projection of the **literal-state** circulation polytope.  The elementary
conditions

\[
                   0\leq q_s\leq1,\qquad \sum_s q_s\leq d
\]

prove the chain factor, but do not imply (1.6).

Formally, let `ST_(k,r,d)` be the set of vectors `h=(h_s)` obtained from a
`Sym(k)`-invariant nonnegative solution of (1.4) and (1.6), with `h_s`
defined by dividing the left side of (1.7) by `W`.  Then the exact all-`k`
criterion is

\[
 \boxed{\text{triangular fractional chains have a balanced trace lift}
                  \iff q\in\mathsf{ST}_{k,r,d}.}       \tag{1.8}
\]

This is not a renaming of the uniform-matroid chain polytope: Proposition
2.1 gives an explicit point of the latter whose natural canonical lift has
nonzero literal divergence.  Determining whether the particular vector
(0.1) always lies in `ST_(k,r,d)` is the new fractional existence problem.

## 2. The old canonical clock is not balanced

The failure occurs in the first zero-slack triangular case.

### Proposition 2.1 (the `k=6` canonical divergence)

For `k=6`, one has

\[
 r=3,\quad W=20,\quad d=1,\quad h=1.
\]

The boundary board has its unique cell at rank one, so

\[
                       b_1=1,\qquad
                       q_1=\frac14,\quad q_2=\frac34. \tag{2.1}
\]

Apply the canonical consecutive clock of the bounded-chain trace theorem:
for a selected lower set `S subsetneq T`, choose `x in S` and put

\[
                       B_1=S,\qquad
                       B_0=(T\setminus S)\cup\{x\}.    \tag{2.2}
\]

Its head-rank distribution is

\[
                         \tfrac14[1]+\tfrac34[2],      \tag{2.3}
\]

whereas its tail-rank distribution is

\[
                         \tfrac14[3]+\tfrac34[2].      \tag{2.4}
\]

Therefore its rank projection already violates (1.6).  In particular,
uniform owner orderings, uniform choices of `x`, and coordinate
symmetrization cannot turn this canonical distribution into a circulation.

#### Proof

If `|S|=1`, then (2.2) gives `B_0=T`, of rank three.  If `|S|=2`, it gives
`|B_0|=2`.  The head is `S` itself.  Insert the probabilities in (2.1).
Because statewise balance implies balance after projecting a state to the
rank of its sole letter, (2.3)--(2.4) contradict (1.6). \(\square\)

This is a defect of the clock, not a no-go for the triangular profile.

## 3. A connected rational balanced clock at `k=6`

Fix one owner `T in binom([6],3)`.  For `x in T`, write

\[
                             P_x=T\setminus\{x\}.
\]

Use the following twelve directed order-one trace edges, each with weight
`1/12`:

\[
 \{x\}\longrightarrow P_x,qquad
 P_x\longrightarrow\{x\}qquad(x\in T),              \tag{3.1}
\]

and

\[
                         P_x\longrightarrow P_y
                         \qquad(x,y\in T,\ x\neq y).  \tag{3.2}
\]

The owner of every edge is `T`, because the union of its two endpoint
letters is `T`.  Mark the head letter, which is the unique proper suffix
cell when `d=1`.

### Theorem 3.1 (exact `k=6` joint fractional solution)

Taking (3.1)--(3.2) independently in every owner gives a rational solution
of (1.4)--(1.6).  Its positive support is weakly connected and contains
every singleton boundary state.

#### Proof

There are six edges in (3.1) and six in (3.2), so their total weight in one
owner is one, proving (1.4).

At singleton vertex `{x}`, the only displayed incident edges are

\[
                         \{x\}\to P_x,qquad P_x\to\{x\},
\]

with equal weight `1/12`.  At `P_x`, (3.1) contributes one incoming and one
outgoing edge, and (3.2) contributes two incoming and two outgoing edges.
Thus every literal vertex is balanced.

The marked head mass at rank one is the mass of the three reverse edges in
(3.1), namely `3/12=1/4`.  The marked head mass at rank two is the other
three edges in (3.1) plus all six edges in (3.2), namely
`3/12+6/12=3/4`.  More precisely, in one owner each singleton `{x}` receives
weight `1/12`, while each pair `P_x` receives

\[
                  \frac1{12}+2\frac1{12}=\frac14.     \tag{3.3}
\]

A fixed global singleton lies in `binom(5,2)=10` owners, so its owner load
is `10/12=5/6`; the unique boundary cell contributes `1/6`.  A fixed global
pair lies in four owners, so (3.3) gives owner load one and there is no
boundary rank-two contribution.  This proves (1.5).

Finally, every singleton is joined to every disjoint pair, and the pair
vertices are joined whenever their union has rank three.  These incidences
connect all singleton and pair vertices on `[6]`.  Hence the positive
support is weakly connected and contains all six singleton states. \(\square\)

Thus `k=6` separates three statements cleanly:

1. the triangular fractional chain factor is feasible;
2. its previously chosen canonical clock is not balanced;
3. a different connected balanced clock is feasible.

## 4. Boundary rooting, including all `d` boundary chains

Let

\[
 \mathcal V_\partial=
 \{(\{x_1\},\ldots,\{x_d\}):x_1,\ldots,x_d
                                      \text{ are distinct}\}. \tag{4.1}
\]

The uniform singleton prefix in the triangular theorem induces the uniform
root distribution on `V_partial`.  It also realizes all `d` boundary chains
simultaneously; there are not `d` independent boundary states.

### Proposition 4.1 (rational connected boundary-root criterion)

Suppose (1.4)--(1.6) has a rational `Sym(k)`-invariant solution `x` whose
positive de Bruijn support is weakly connected and meets
`V_partial`.  Then:

1. its support contains every state in `V_partial`;
2. after multiplying by a common denominator `N`, the trace multigraph has
   an Euler circuit rooted at any prescribed state of `V_partial`; and
3. averaging the choice of root uniformly over `V_partial` couples that
   Euler circuit to the common singleton boundary prefix, with identical
   initial and terminal root distributions.

Consequently the full triangular fractional system, including boundary
chains of capacities `1,2,...,d`, has zero expected boundary imbalance.

#### Proof

Invariance sends any one state of `V_partial` to every other one, and leaves
positive support invariant.  This proves 1.  Multiply all weights by a
common denominator.  Equations (1.6) give equal integral indegree and
outdegree at every positive-degree state.  A weakly connected balanced
directed multigraph has an Euler circuit, and the circuit may be cut at any
vertex on it.  This proves 2.  Cutting the same circuit at a uniformly
chosen ordered-singleton state gives the boundary distribution generated by
a uniform permutation.  Every cut is closed, so its start and end states
are equal; averaging preserves equality. \(\square\)

Equivalently, for an invariant rational circulation put

\[
 \rho_\partial=
 \sum_{v\in\mathcal V_\partial}
       \sum_{(e,J):\partial^-e=v}x_{e,J}.               \tag{4.2}
\]

Under connected positive support, the exact fractional boundary-cut
throughput condition is simply `rho_partial>0`: invariance then supplies
positive throughput at every ordered-singleton state, and multiplication by
a common denominator supplies an integral visit at every such state.  This
criterion concerns the ability to **root** a repeated fractional Euler
circuit.  It must not be confused with one-copy coloured integrality.

The denominator `N` is load-bearing.  The Euler circuit in Proposition 4.1
uses `N` copies of every owner colour.  Dividing by `N` gives a rooted
fractional object, not one physical word.  The proposition therefore proves
boundary compatibility at the fractional level and no more.

There are three distinct gates:

* **flow balance:** equations (1.6);
* **coloured integrality:** one actual trace edge for each owner and one
  actual occurrence of every residual lower target; and
* **topology/rooting:** connected positive support containing an ordered
  singleton state.

Neither of the last two follows from the first.

## 5. A stationary cyclic-word sufficient model

There is a useful owner-local way to search for solutions of the LP.  Fix a
rank-`r` set `T` and a finite cyclic word of nonempty subsets of `T`.  Assume
that every cyclic window of length `d+1` has union `T`.  At every phase mark
some of its proper suffix unions, always using distinct strict-lower sets.

Choose a phase uniformly.  The resulting trace law is a circulation because
the distribution of the first `d` letters is the shift of the distribution
of the last `d` letters.  Average further over all bijections of `T` and all
rank-`r` owners.  If the expected marked rank histogram is exactly `q`, then
(1.4)--(1.6) and (1.5) hold.

This converts all-`k` fractional existence into a concrete stationary
window question:

> construct rotation-invariant marked cyclic trace laws whose histogram is
> `q`, whose symmetrized support is connected, and whose support reaches an
> ordered singleton state.

The elementary uniform-matroid inequalities on `q` do not prove this.  A
cyclic word imposes simultaneous overlap constraints on all `d` suffix
unions.  The `k=6` construction is the first nontrivial balanced example.

## 6. The exact integral theorem still needed

Even an all-`k` solution of the marked-trace LP would leave the following
rounding statement.

### Triangular coloured Euler absorber

Starting from a rational connected solution of (1.4)--(1.6), choose:

1. one literal singleton prefix, hence one integral realization of all
   boundary chains;
2. one trace edge for every rank-`r` owner;
3. exactly one residual witness for every strict-lower target; and
4. those edges so that they form one Euler trail rooted at the terminal
   singleton-prefix state.

A plausible proof must combine two exchanges:

* a coloured discrepancy/matching absorber preserving owner and target
  equations while reducing the denominator from `N` to one; and
* a de Bruijn cycle absorber merging support components and planting the
  boundary root without changing those colours.

The boundary bank cannot be rounded independently after the owner traces:
its one permutation simultaneously determines all `d` initial chains and
the first de Bruijn state.  Conversely, connected support alone does not
round owner colours: Proposition 4.1 explicitly repeats every owner `N`
times.

Upper OR witnesses and residence constraints beyond the lower trace are not
included here.  They must eventually be carried as protected colours by the
same absorber.  The present conclusion is narrower but exact: the optimal
triangular fractional chain theorem and de Bruijn serialization meet at a
new, genuine marked-circulation gate, and the previously chosen canonical
clock does not pass it.
