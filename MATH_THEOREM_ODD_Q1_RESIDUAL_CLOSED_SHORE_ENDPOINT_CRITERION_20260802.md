# Odd q1 residual completion: closed shores and free endpoints

**Date:** 2026-08-02  
**Status:** unconditional max-flow duality theorem.  It sharpens the
capacitated residual-root criterion after a one-per-upper primary selector
has been fixed.  It does not construct the primary selector, impose the
final component rank, prove residence or deeper upper coverage, or solve
`nu(17)`.

## 0. Outcome

Put `k=2r-1`.  Let `A` be the roots of rank `r-1` left unused by a primary
Johnson-edge selector `Q_0`, and let `b_T` be the required final degree of
each rank-`r` owner `T`.  Write

\[
             c_T=b_T-\deg_{Q_0}(T)\ge0.
\]

Every residual root must choose two distinct containing owners.  The
usual max-flow criterion is

\[
 2|X|\le
 \sum_T\min\bigl(c_T,|\{L\in X:L\subset T\}|\bigr)
 \qquad(X\subseteq A).                              \tag{0.1}
\]

The theorem below eliminates the root-family variable `X`.  For an owner
set `Y`, put

\[
 \begin{aligned}
 I_A(Y)&=|\{L\in A:N(L)\subseteq Y\}|,\\
 J_A(Y)&=|\{L\in A:|N(L)\setminus Y|=1\}|,
 \end{aligned}                                      \tag{0.2}
\]

where

\[
                    N(L)=\{L+x:x\notin L\}
\]

is the set of the `r` middle owners containing `L`.

Then residual completion exists if and only if

\[
 \boxed{
       2I_A(Y)+J_A(Y)\le\sum_{T\in Y}c_T
       \quad\hbox{for every owner set }Y.}           \tag{0.3}
\]

Thus only lower faces whose complete extension star, or all but one point
of that star, is trapped in `Y` can obstruct completion.

If `b_T=2` and `Q_0` is a linear forest, (0.3) becomes

\[
 \boxed{
 2I_A(Y)+J_A(Y)+|\partial_{Q_0}Y|
       \le 2\kappa(Q_0[Y])                           \tag{0.4}
 }
\]

for every `Y`.  Here `partial_(Q_0)Y` is the selected-edge boundary and
`kappa(Q_0[Y])` counts all components of the induced forest, including
isolated vertices.  The right side minus the boundary is exactly the
number of unused degree slots at the induced path endpoints.  The
remaining q1 problem is therefore an endpoint-supply theorem for Boolean
stars, not an opaque family of arbitrary Hall shores.

## 1. Network formulation

Use the network

```text
source --(2)--> residual root L --(1)--> owner T --(c_T)--> sink,
```

with the middle arc present exactly when `L subset T`.  Integral flow of
value `2|A|` chooses two distinct owners for every residual root and uses
owner `T` at most `c_T` times.  Assume throughout the necessary total
capacity identity

\[
                         \sum_Tc_T=2|A|.             \tag{1.1}
\]

For a cut whose source side contains a root set `X subseteq A` and an
owner set `Y`, the capacity is

\[
 2(|A|-|X|)+e(X,V\setminus Y)+\sum_{T\in Y}c_T,     \tag{1.2}
\]

where `e` counts root-owner incidences.

Optimizing (1.2) over `Y` for fixed `X` gives (0.1), which is the prior
capacitated residual-root criterion.  Optimizing in the opposite order
gives the closed-shore form.

## 2. Closed-shore theorem

### Theorem 2.1

Under (1.1), the residual network has flow value `2|A|` if and only if
(0.3) holds for every owner set `Y`.

#### Proof

Fix `Y`.  The contribution of one residual root `L` to (1.2) is

\[
 \begin{cases}
 2,&L\notin X,\\
 |N(L)\setminus Y|,&L\in X.
 \end{cases}
\]

The optimal choice is independent for every root, so the minimum cut with
this fixed owner shore has capacity

\[
 \sum_{L\in A}\min\bigl(2,|N(L)\setminus Y|\bigr)
       +\sum_{T\in Y}c_T.                            \tag{2.1}
\]

Subtract (2.1) from the target value `2|A|`.  A root contributes two to
the difference when its whole extension star lies in `Y`, one when exactly
one extension lies outside, and zero otherwise.  Hence the difference is

\[
              2I_A(Y)+J_A(Y)-\sum_{T\in Y}c_T.      \tag{2.2}
\]

All cuts have capacity at least `2|A|` exactly when (2.2) is nonpositive
for every `Y`.  Max-flow/min-cut proves the claim, and integral capacities
give an integral residual completion.  \(\square\)

### Corollary 2.2 (canonical minimum-cut closure)

Every minimum cut has a representative in which

\[
 X=\{L\in A:|N(L)\setminus Y|\le1\},                \tag{2.3}
\]

with arbitrary choices only at roots having exactly two outside owners.
In particular, no family of roots with three or more available outside
owners is needed in a deficiency certificate.

This is immediate from the rootwise minimization in (2.1).

## 3. Linear-forest endpoint form

Assume now that the desired final owner degree is two everywhere and that
`Q_0` is a linear forest.  Then

\[
                         c_T=2-\deg_{Q_0}(T).        \tag{3.1}
\]

For any owner set `Y`, the selected-degree sum is

\[
 \sum_{T\in Y}\deg_{Q_0}(T)
       =2|E(Q_0[Y])|+|\partial_{Q_0}Y|.              \tag{3.2}
\]

Since `Q_0[Y]` is a forest,

\[
 |E(Q_0[Y])|=|Y|-\kappa(Q_0[Y]).                    \tag{3.3}
\]

Equations (3.1)--(3.3) give

\[
 \sum_{T\in Y}c_T
   =2\kappa(Q_0[Y])-|\partial_{Q_0}Y|.               \tag{3.4}
\]

Substitution into (0.3) proves (0.4).

For a linear forest, each induced component is a path or an isolated
vertex.  The quantity on the right of (3.4) is literally its number of
free degree slots: two per induced component, minus one for every selected
edge leaving `Y`.  Therefore (0.4) says:

> roots whose extension stars are trapped in `Y` consume two free path
> endpoints, roots with one external escape consume one endpoint, and the
> induced primary paths must supply all of them.

This also explains the authenticated K7 fixed-primary failure: the three
stranded residual slots are an endpoint shortage on a closed owner shore,
not a scalar shortage in the complete instance.

### Corollary 3.1 (literal endpoint Hall)

If `Q_0` is spanning, has no isolated owner, and every residual capacity
is zero or one, then its positive-capacity owners are exactly its path
endpoints.  The root-side form (0.1) reduces to

\[
 2|X|\le
 |\{T:\ T\hbox{ is an available endpoint of }Q_0,
                 \ L\subset T\hbox{ for some }L\in X\}|.     \tag{3.5}
\]

Thus in this common normal form the residual degree gate is literally a
two-endpoints-per-root Hall theorem, rather than a general capacitated
matching problem.

## 4. Fixed-boundary version

Nothing in Theorem 2.1 requires the uniform target degree two.  For the
ordinary `h=1` projection, use

\[
 b_T=2-\mathbf1_{\{T=B\}}
      -\#\{\hbox{selected `D`-neighbour deficit occurrences at }T\}.
                                                               \tag{4.1}
\]

Then (0.3), with `c_T=b_T-deg_(Q_0)(T)`, is still necessary and
sufficient.  Formula (0.4) acquires only the explicit boundary correction

\[
 \sum_{T\in Y}c_T
 =2\kappa(Q_0[Y])-|\partial_{Q_0}Y|
   -\sum_{T\in Y}(2-b_T).                            \tag{4.2}
\]

Thus the lollipop boundary does not restore arbitrary Hall shores; it
subtracts four named endpoint units from the same closed-shore ledger.

## 5. Linear primary-selector cuts

The owner-shore theorem can be moved entirely to the primary side.  This
is useful because the residual-root set is the complement of the roots
used by `Q_0`.

Let

\[
                  \mathcal R_0=\mathcal Q\setminus O
\]

be the roots not prescribed for omission.  For an owner shore `Y`, define

\[
 w_Y(L)=\bigl(2-|N(L)\setminus Y|\bigr)_+,
 \qquad L\in\mathcal R_0.                            \tag{5.1}
\]

Thus `w_Y(L)` is two on a fully trapped star, one on an almost-trapped
star, and zero otherwise.  A primary diamond `e` has a root `L(e)` and two
owner endpoints `T(e),H(e)`.  Put

\[
 \alpha_Y(e)=\mathbf1_{T(e)\in Y}+\mathbf1_{H(e)\in Y}
                         -w_Y(L(e)).                 \tag{5.2}
\]

The coefficient is always nonnegative.  If all of `N(L)` lies in `Y`,
both diamond endpoints lie in `Y` and `alpha=0`.  If exactly one extension
lies outside, every diamond has at least one endpoint in `Y`, so `alpha`
is zero or one.  Otherwise `w=0`.

### Theorem 5.1 (exact primary Benders rows)

A primary selector `Q_0`, using distinct roots in `mathcal R_0`, admits a
residual completion to owner degrees `b_T` if and only if, for every owner
shore `Y`,

\[
 \boxed{
  \sum_{e\in Q_0}\alpha_Y(e)
       \le
  \sum_{T\in Y}b_T-\sum_{L\in\mathcal R_0}w_Y(L).}  \tag{5.3}
\]

#### Proof

The unused roots are

\[
 A=\mathcal R_0\setminus\{L(e):e\in Q_0\}.
\]

Therefore the left side of (0.3) is

\[
 \sum_{L\in A}w_Y(L)
 =\sum_{L\in\mathcal R_0}w_Y(L)
   -\sum_{e\in Q_0}w_Y(L(e)).                       \tag{5.4}
\]

The residual capacity inside `Y` is

\[
 \sum_{T\in Y}c_T
 =\sum_{T\in Y}b_T
  -\sum_{e\in Q_0}
      (\mathbf1_{T(e)\in Y}+\mathbf1_{H(e)\in Y}). \tag{5.5}
\]

Substitute (5.4)--(5.5) into (0.3) and rearrange.  The result is exactly
(5.3).  \(\square\)

Equation (5.3) is a genuine selector inequality: every coefficient is
known before the residual flow is chosen.  A failed max-flow returns its
owner shore `Y`, and (5.3) may be added directly to a one-per-upper
primary master.  The remaining nonlinearity is no longer hidden in the
residual matching; it is the task of finding a primary forest satisfying
this explicit cut family together with the upper, root and graphic rows.

### Theorem 5.2 (fixed-margin circuit invariance)

Let `Q_0` and `Q_0'` be primary incidence selectors with the same owner
degree vector and the same used-root support.  Then, for every owner shore
`Y`,

\[
             \sum_{e\in Q_0}\alpha_Y(e)
             =\sum_{e\in Q_0'}\alpha_Y(e).           \tag{5.6}
\]

In particular, no sequence of alternating incidence-circuit toggles which
preserves those margins can improve a violated primary Benders row.

#### Proof

By (5.2),

\[
 \sum_{e\in Q_0}\alpha_Y(e)
 =\sum_{T\in Y}\deg_{Q_0}(T)
   -\sum_{L\in U(Q_0)}w_Y(L),                       \tag{5.7}
\]

where `U(Q_0)` is the used-root support.  Both terms are fixed by the two
declared margins, proving (5.6).  Every alternating incidence circuit
preserves all root and owner degrees, so the final assertion follows.
\(\square\)

This sharply limits the density reservoir.  A deficient shore may expose
many unused Johnson chords, but a repair must change the primary root
support, change the **primary** owner-degree vector/endpoint placement, or
reselect which occurrences are designated primary inside a larger full
factor.  The prescribed final target degrees `b_T` remain fixed.  Merely
rethreading one frozen primary incidence fibre cannot repair its residual
Hall defect.  A fixed-margin move on the full factor is itself still
margin-invariant; full-factor q1 annealing can escape only because its
changed upper multiplicities permit a different one-per-upper primary
marking afterward, with different primary root support and primary owner
degrees.

### Proposition 5.3 (minimal same-upper support exchange)

Let `e=(L,R,T,H)` be one primary diamond.  Choose an unused root
`L' subset R` and let `e'=(L',R,T',H')` be its unique same-upper diamond.
Suppose that after deleting `TH`, the new endpoints have available primary
degree, and `T',H'` lie in distinct components of the remaining primary
forest.  Then

\[
                         Q_0'=Q_0-e+e'              \tag{5.8}
\]

is still root-injective, one-per-upper, degree at most two, and a linear
forest.  Its exact shore-row change is

\[
 \sum_{f\in Q_0'}\alpha_Y(f)-
 \sum_{f\in Q_0}\alpha_Y(f)
                         =\alpha_Y(e')-\alpha_Y(e). \tag{5.9}
\]

Hence any strict decrease in `alpha_Y` is a certified repair of that
primary Benders row.  Support one is minimal: Theorem 5.2 shows that a move
which changes neither used-root support nor primary owner degrees changes
no row.

The authenticated K7 deficient selector contains such moves.  Among 73
root-injective same-upper replacements retaining the degree cap and a
linear forest, 49 improve its minimum row and the best row gain is two.  A
literal example uses upper mask `93`: replace root `84` and owner edge
`85--92` by unused root `76` and edge `77--92`.  On the minimum shore the
old coefficient is two and the new coefficient zero.  The row defect falls
from three to one, and the exact global residual flow rises from `25/28`
to `26/28`.

This proves that the invariant is an actuator specification rather than a
dead end: the weakest legal escape is a same-upper primary replacement
which transports one root and one primary endpoint.  It does not prove
that repeated improving replacements always reach zero defect or preserve
the protected K17 boundary.

## 6. Exact remaining theorem

The q1 selector can now be organized in three exact stages:

1. choose one distinct-root diamond for every immediate-upper colour;
2. make its owner graph a protected linear forest satisfying (0.3), or
   equivalently (0.4) in the uniform case;
3. use the integral residual flow and require its component-link graph to
   have the final graphic rank.

The robust two-copy transversal theorem closes the root/upper marginal of
stage 1.  The present theorem makes the complete stage-2 extension test an
endpoint inequality over closed Boolean stars.  It does not prove that a
primary forest satisfying all those inequalities exists.  That protected
forest-plus-endpoint statement is the remaining integral q1 theorem.

There is also an exact topological normalization.  A spanning primary
forest with `W-Cat_r` edges has `Cat_r` components.  If `t` roots are
omitted and the final owner-degree ledger has total deficit `2t`, every
saturating residual flow has `Cat_r-t` edges on the contracted primary
components.  Requiring graphic rank `Cat_r-t` is therefore equivalent to
requiring the contracted completion to be a forest with exactly `t`
components.  The degree cap then makes it a `t`-path cover: one rooted path
when `t=1`, and the two ordinary paths before the exceptional `D` join when
`t=2`.  For `t=0`, the corresponding connected degree-two completion is
one cycle and has `Cat_r` residual edges rather than a forest.
