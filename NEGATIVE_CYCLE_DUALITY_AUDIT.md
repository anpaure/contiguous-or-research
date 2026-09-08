# Negative-cycle duality for the diamond load problem

## Status and verdict

This note audits the negative-cycle route proposed in
`RECTANGLE_LOAD_AUGMENTATION.md`.

There is an exact and useful dual theorem: for every colour-perfect diamond
matching at `m>=2`, the matched-row exchange digraph contains a negative
directed simple cycle for the linearized convex-load objective.  More
generally, any nonnegative weight supported on middle vertices of current
load at least two has a negative exchange cycle.  In particular, every
overloaded middle vertex has an exchange cycle that lowers its own load.

This does **not** prove convex-potential descent.  For an exchange cycle `C`,
the exact identity is

\[
 \Delta\Phi(C)=w_d(C)+\frac12\|\delta_C\|_2^2.                 \tag{0.1}
\]

The second term is nonnegative, nonlocal, and not an arc-additive cycle
weight.  In the strict `m=3` rectangle trap, the shortest negative linear
cycle is already a rectangle, with terms `-1+2=+1`.  Shortening a negative
cycle therefore cannot repair the argument.

There is also a new finite obstruction to every constant-order **strict
one-move** replacement.
An explicit colour-perfect matching at `m=5` has maximum middle load three
and has no decreasing exchange cycle of order two, three, or four.  One
order-five cycle changes `Phi` by `-1` and lowers the maximum load to two.
Together with the existing `m=3` and `m=4` certificates, the first necessary
repair orders are respectively three, four, and five.

Thus the strongest credible strict-descent statement is now a
**diameter-order augmentation conjecture**: order at most `m`, not one of the
formerly proposed fixed lists of moves.  This note does not prove that
conjecture.  Neutral short moves can sometimes cross the same potential
plateau and are discussed in Section 4; they leave open a different
constant-order lexicographic theorem.  Acyclicity remains a separate problem.

## 1. Exchange vectors and exact curvature

Use

\[
 \mathcal L=\binom{[2m]}{m-1},\qquad
 \mathcal M=\binom{[2m]}m,\qquad
 \mathcal U=\binom{[2m]}{m+1}.
\]

Let `P` be a perfect matching in the lower--upper inclusion graph.  Index its
matched pairs as

\[
 e_i=(S_i,U_i),\qquad S_i\subset U_i.
\]

For every allowed pair `S_i subset U_j`, let

\[
 v_{ij}\in\{0,1\}^{\mathcal M}
\]

be the incidence vector of the two middle sets strictly between `S_i` and
`U_j`.  The current middle-load vector is

\[
 d=\sum_i v_{ii}.                                             \tag{1.1}
\]

Contract every current matching edge.  The matched-row exchange digraph has
an arc `i -> j` exactly when `S_i subset U_j`.  A directed simple cycle

\[
 C=(i_0,i_1,\ldots,i_{t-1})
\]

cyclically reassigns `U_(i_{s+1})` to `S_(i_s)`.  Its load change is

\[
 \delta_C=\sum_s(v_{i_s i_{s+1}}-v_{i_s i_s}),                \tag{1.2}
\]

where indices are cyclic.  Both the old and new selections have `2t`
middle incidences, so

\[
 \sum_X\delta_C(X)=0.                                         \tag{1.3}
\]

For any weight vector `lambda` on `mathcal M`, give an exchange arc the
reduced cost

\[
 w_\lambda(i,j)
 =\langle\lambda,v_{ij}-v_{ii}\rangle.                         \tag{1.4}
\]

Then its cycle sum is exactly

\[
 w_\lambda(C)=\langle\lambda,\delta_C\rangle.                 \tag{1.5}
\]

For the convex potential

\[
 \Phi(d)=\sum_X\binom{d(X)}2,
\]

direct expansion and (1.3) give the decisive identity

\[
 \begin{aligned}
 \Phi(d+\delta_C)-\Phi(d)
 &=\sum_X\left(d(X)\delta_C(X)
       +\frac{\delta_C(X)^2-\delta_C(X)}2\right)\\
 &=w_d(C)+\frac12\|\delta_C\|_2^2.                            \tag{1.6}
 \end{aligned}
\]

Consequently `w_d(C)<0` is necessary, but not sufficient, for an improving
cycle.  The correct margin is

\[
 w_d(C)<-\frac12\|\delta_C\|_2^2.                             \tag{1.7}
\]

The curvature contains cross terms between different arcs of `C` and is not
representable by fixed arc weights.  Ordinary negative-cycle algorithms see
only (1.5), not (1.7).

## 2. The exact linear negative-cycle theorem

The lower--upper inclusion graph is regular of degree

\[
 D=\binom{m+1}{2}.
\]

A fixed middle set `X` lies in exactly `m^2` diamonds: choose the element of
`X` deleted at the lower endpoint and the element outside `X` inserted at the
upper endpoint.  Therefore the uniform fractional perfect matching

\[
 x_{S,U}=1/D
\]

has the constant middle load

\[
 \mu=\frac{m^2}{D}=\frac{2m}{m+1}<2.                          \tag{2.1}
\]

### Theorem 2.1 (weighted negative-cycle duality)

Let `lambda(X)>=0`.  If

\[
 \sum_X\lambda(X)(d(X)-\mu)>0,                               \tag{2.2}
\]

then the matched-row exchange digraph contains a directed simple cycle `C`
of order at most

\[
 N=|\mathcal L|=\binom{2m}{m-1}
\]

such that

\[
 w_\lambda(C)<0.                                              \tag{2.3}
\]

#### Proof

Give a diamond `(S,U)` the linear cost

\[
 c_\lambda(S,U)=\sum_{S\subset X\subset U}\lambda(X).
\]

The current matching has total cost

\[
 \sum_X\lambda(X)d(X).
\]

The uniform fractional perfect matching has total cost

\[
 \mu\sum_X\lambda(X).
\]

Under (2.2), the latter is strictly smaller.  The bipartite perfect-matching
polytope is integral, so some perfect matching `Q` has smaller linear cost
than `P`.  The symmetric difference of `P` and `Q` is a disjoint union of
alternating even cycles.  After the edges of `P` are contracted, these are
directed simple cycles in the matched-row exchange graph, and their reduced
costs sum to `cost(Q)-cost(P)<0`.  At least one is negative.  A simple cycle
uses at most all `N` matched rows.  QED.

### Corollary 2.2 (variance certificate)

Take `lambda=d`.  Since

\[
 \sum_Xd(X)=\mu|\mathcal M|,
\]

the dual gap is exactly

\[
 \sum_Xd(X)^2-\mu\sum_Xd(X)
 =\sum_X(d(X)-\mu)^2>0                                       \tag{2.4}
\]

for every `m>=2`.  Thus every colour-perfect matching has a negative
linearized-load cycle.

### Corollary 2.3 (single-vertex escape)

If `d(X)>=2`, take `lambda=1_X`.  Because `d(X)>mu`, Theorem 2.1 gives a
directed simple cycle with

\[
 \delta_C(X)<0.                                               \tag{2.5}
\]

In particular, every overloaded vertex can be relieved by some exchange
cycle of order at most `N`.

This is a genuine augmentation statement, but it is only coordinatewise.
The cycle may overload another vertex, increase the current maximum, or have
positive exact `Delta Phi` because of (1.6).

The same proof applies to every nonnegative weight supported on vertices of
load at least two.  Hence no nonnegative linear price on the overloaded
region can certify a local obstruction.  The remaining obstruction is
integral simultaneous protection plus curvature.

### Corollary 2.4 (fractional protected packet)

Let

\[
 H=\{X:d(X)\ge2\},\qquad h=|H|.
\]

There are directed simple exchange cycles `C_1,...,C_s`, with `s<=h`, and
positive real coefficients `alpha_1,...,alpha_s` such that

\[
 \sum_{j=1}^s\alpha_j\delta_{C_j}(X)=\mu-d(X)<0
 \qquad(X\in H).                                               \tag{2.6}
\]

#### Proof

The uniform fractional matching minus `P` has projected load change
`mu*1-d`.  Decompose the uniform fractional matching into a convex
combination of integral perfect matchings.  Decompose the symmetric
difference of each such matching with `P` into directed simple exchange
cycles.  After projection onto the coordinates in `H`, this expresses the
strictly negative vector `(mu-d)|_H` as a nonnegative combination of cycle
change vectors.  Conic Caratheodory in `R^h` reduces the representation to
at most `h` cycles.  QED.

Thus simultaneous protection of every currently heavy vertex is already
possible *fractionally*.  What is missing is an integral packet whose cycles
can be executed compatibly and whose cross-curvature is controlled.  This
connects the exchange-dual calculation directly to the packet-absorber route
in the general construction programme.

## 3. Boolean geometry does not give a short chord theorem

The inclusion graph itself contains induced alternating cycles whose order
grows with `m`.

### Proposition 3.1 (induced cycles through order `m+1`)

For every `3<=t<=m+1`, the rank-`m-1`/rank-`m+1` inclusion graph contains an
induced alternating cycle of order `t`.

#### Proof

Choose disjoint objects

\[
 |C|=m-2,\qquad z,\qquad a_0,\ldots,a_{t-1}.
\]

They fit in `[2m]` because `(m-2)+1+t<=2m`.  Put

\[
 S_i=C\cup\{a_i\},\qquad
 U_i=C\cup\{z,a_i,a_{i+1}\},                                 \tag{3.1}
\]

with cyclic indices.  Then `S_j subset U_i` exactly when `j=i` or
`j=i+1`.  Hence the subgraph induced by these `2t` vertices is precisely

\[
 S_0-U_0-S_1-U_1-\cdots-S_{t-1}-U_{t-1}-S_0.
\]

There are no inclusion chords.  QED.

This proposition does not prove that a load-derived *minimal negative*
cycle must be long.  It proves the narrower, important point: no shortening
argument based only on Boolean inclusion chords can force order two or
three, or even any bound below `m+1`.

## 4. Exact finite hierarchy: orders three, four, five are necessary

The checker `scratch/check_negative_cycle_duality.py` independently rebuilds
the Boolean layers and diamond endpoints, validates each perfect matching,
enumerates every directed simple cycle through the stated cutoff, and
recomputes both terms in (1.6).

Its exact output is:

| `m` | load profile | minimum exact change by cycle order | first repair |
|---:|---|---|---:|
| 3 | `1^11 2^8 3^1` | order 2: `+1`; order 3: `-1` | 3 |
| 4 | `1^29 2^40 3^1` | orders 2,3: `0`; order 4: `-1` | 4 |
| 5 | `1^85 2^166 3^1` | orders 2,3,4: `0`; order 5: `-1` | 5 |

For `m=5`, the exhaustive cycle counts are

\[
 169,\quad1203,\quad10148,\quad103282
\]

at orders two through five.  The repairing row cycle is

\[
 (4,44,154,33,24)                                             \tag{4.1}
\]

in the zero-based canonical ordering of the rank-four lower sets.  It has

\[
 w_d=-4,\qquad \frac12\|\delta\|_2^2=3,
 \qquad\Delta\Phi=-1,                                        \tag{4.2}
\]

and changes the maximum load from three to two.

The shorter cycles already include many negative *linear* cycles.  In the
same `m=5` matching, the minimum linear terms by order are

\[
 -2,-4,-6,-7,
\]

but their curvature cancels every exact gain through order four.  This is a
direct finite demonstration that negative-cycle duality and exact convex
descent are different problems.

There is an important qualification.  The order-`m` repair need not be
primitive if neutral moves are allowed.  The same checker verifies

\[
 \begin{array}{c|c|c}
 m&\text{short exchange sequence}&\text{successive Phi values}\\ \hline
 4&(2,2,2)&43,43,43,42,\\
 5&(2,2)&169,169,168.
 \end{array}                                                   \tag{4.3}
\]

All intermediate maximum loads remain three and the final maximum is two.
At `m=5`, the first neutral rectangle moves the unique overload to another
middle vertex and the next rectangle removes it.  At `m=4`, two neutral
rectangles rearrange the degree-one/two neighbourhood before a third
rectangle descends.  Therefore the certificates refute a bounded list of
**strictly decreasing single moves**, but they do not refute a theorem using
neutral rectangles plus a secondary well-founded potential.  The `m=3`
strict trap still requires at least one directed triangle, because it has no
neutral rectangle at all.

The `m=4` certificate refutes the one-step four-or-six augmentation
conjecture in the previous note.  The `m=5` certificate further refutes a
one-step theorem using only alternating cycles of total lengths `4,6,8`.
The pattern `3,4,5` supports, but does not prove, an order-`m` strict-descent
theorem.  Equation (4.3) simultaneously identifies a second viable route:
rectangles and triangles with nonincreasing `Phi` and a new plateau
potential.

## 5. The corrected all-dimensional target

The strongest target still consistent with every exact certificate is:

### Diameter-order augmentation conjecture

If a colour-perfect diamond matching on `[2m]` has maximum middle load at
least three, then there is a directed simple exchange cycle `C` of order at
most `m` such that

\[
 w_d(C)+\frac12\|\delta_C\|_2^2<0                             \tag{5.1}
\]

and

\[
 \max_X(d(X)+\delta_C(X))\le\max_Xd(X).                       \tag{5.2}
\]

Repeated application would terminate and yield maximum middle load at most
two.  That would prove the non-acyclic orthogonal two-SDR lemma.

The order `m` is sharp for the certified examples `m=3,4,5`.  It also agrees
with the diameter of the Johnson graph on the middle layer, suggesting that
a successful proof should route one unit of overload to a deficient middle
vertex along a shortest Johnson path.  This geometric routing statement is
not yet proved: an arbitrary Johnson path need not lift to a single
lower/upper colour-preserving exchange cycle.

The negative-cycle theorem supplies only the much larger unconditional
linear bound `N=C(2m,m-1)` and no curvature margin.  The next proof must add
one of the following genuinely nonlinear ingredients:

1. a lift of a shortest overload-to-deficit Johnson path to one exchange
   cycle while controlling all intermediate middle loads;
2. a packet of interacting exchange cycles whose cross-curvature cancels;
3. a state-expanded residual network that records middle-resource load, not
   merely matched-row arc cost.

Alternatively, one can seek a secondary potential on each constant-`Phi`
plateau such that every overloaded state has a nonincreasing rectangle or
triangle move decreasing the lexicographic pair `(Phi,secondary)`.  The
finite paths in (4.3) show why this possibility must not be discarded.

Acyclicity of the resulting maximum-degree-two projected graph remains
separate.  No assertion in this note uses or proves it.

## 6. Audited ledger

**Proved here**

* the exact exchange-cycle identity (1.6);
* weighted negative-cycle duality, with simple-cycle order at most `N`;
* a load-reducing exchange cycle for every individual middle vertex of load
  at least two;
* a fractional packet of at most `|{X:d(X)>=2}|` cycles decreasing every
  currently heavy coordinate simultaneously;
* induced Boolean alternating cycles of every order `3,...,m+1`, ruling out
  a pure chord-shortening proof.

**Proved by exhaustive finite verification**

* the existing `m=3` hierarchy: rectangles fail, order three repairs;
* the existing `m=4` hierarchy: orders two and three fail, order four
  repairs;
* the new `m=5` hierarchy: every cycle of order at most four fails, while an
  explicit order-five cycle repairs.

**Open**

* the diameter-order augmentation conjecture;
* whether some dimension requires an exchange cycle longer than `m`, or a
  simultaneous packet rather than a single cycle;
* preservation or subsequent elimination of projected cycles.
