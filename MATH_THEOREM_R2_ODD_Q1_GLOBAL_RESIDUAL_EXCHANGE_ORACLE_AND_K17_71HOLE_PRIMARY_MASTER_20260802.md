# R2 theorem: global residual exchange oracle and the K17 71-hole primary master

**Date:** 2026-08-02  
**Status:** exact closed-shore exchange calculus, polynomial separation and
bounded-neighbourhood oracle, with independently replayed K7/K9 calibration.
The unrestricted integral selector remains a Benders master, not a proved
polynomial-time algorithm. Residence, source, compiler, opening and the final
component rank are outside scope.

## 1. Fixed-selector value

Put `k=2r-1`. Let `R0` be the allowed rank-`r-1` roots, let `T` be the
rank-`r` owners, and let `Q` be a root-injective primary selector. A selected
diamond `e=(L,R,T,H)` uses root `L`, upper colour `R`, and owner endpoints
`T,H`. Define

\[
 A(Q)=\mathcal R_0-U(Q),\qquad
 c_Q(T)=b_T-\deg_Q(T).
\]

Assume nonnegative residual capacities and the total ledger

\[
             D_Q:=2|A(Q)|=\sum_Tc_Q(T).             \tag{1.1}
\]

For an owner shore `Y`, put

\[
 w_Y(L)=\bigl(2-|N(L)\setminus Y|\bigr)_+          \tag{1.2}
\]

and

\[
 \Psi_Q(Y)=\sum_{L\in A(Q)}w_Y(L)-\sum_{T\in Y}c_Q(T). \tag{1.3}
\]

### Theorem 1 (exact value)

The maximum residual flow is

\[
 \boxed{
 F(Q)=D_Q-d(Q),\qquad d(Q)=\max_Y\Psi_Q(Y).}        \tag{1.4}
\]

In particular, `Q` has a full residual completion exactly when `d(Q)=0`.

#### Proof

For fixed `Y`, minimize the canonical cut independently at every residual
root. Its contribution is

\[
 \min\bigl(2,|N(L)\setminus Y|\bigr).
\]

The resulting cut capacity is

\[
 C_Q(Y)=\sum_{L\in A(Q)}
 \min\bigl(2,|N(L)\setminus Y|\bigr)+\sum_{T\in Y}c_Q(T).
\]

Since `2-min(2,s)=(2-s)_+`, one has
`D_Q-C_Q(Y)=Psi_Q(Y)`. Min-cut/max-flow gives (1.4). \(\square\)

Let

\[
 \alpha_Y(e)=
 \mathbf1_{T(e)\in Y}+\mathbf1_{H(e)\in Y}-w_Y(L(e)), \tag{1.5}
\]

\[
 \kappa_Y=\sum_{L\in\mathcal R_0}w_Y(L)-\sum_{T\in Y}b_T. \tag{1.6}
\]

Root injectivity gives the selector-linear form

\[
 \boxed{\Psi_Q(Y)=\kappa_Y+\sum_{e\in Q}\alpha_Y(e).} \tag{1.7}
\]

Thus `d(Q)` is the upper envelope of the exact primary Benders rows.

## 2. Signed exchange calculus

Let `z` be a legal signed diamond current, so the final selector is `Q+z`.
Define its root-support and owner-degree currents by

\[
 \rho_z(L)=\sum_{e:L(e)=L}z_e,\qquad
 \gamma_z(T)=\sum_ez_e
  \bigl(\mathbf1_{T(e)=T}+\mathbf1_{H(e)=T}\bigr). \tag{2.1}
\]

### Theorem 2 (exact shore and global changes)

For every shore,

\[
 \boxed{
 \delta_z(Y):=\Psi_{Q+z}(Y)-\Psi_Q(Y)
 =\sum_{T\in Y}\gamma_z(T)-\sum_L\rho_z(L)w_Y(L)
 =\sum_ez_e\alpha_Y(e).}                            \tag{2.2}
\]

If `z` preserves selector cardinality, then

\[
 \boxed{
 F(Q+z)-F(Q)=d(Q)-\max_Y\bigl(\Psi_Q(Y)+\delta_z(Y)\bigr).} \tag{2.3}
\]

Consequently, an integral gain of at least `g` is equivalent to

\[
 \Psi_Q(Y)+\delta_z(Y)\le d(Q)-g\qquad\text{for every }Y. \tag{2.4}
\]

#### Proof

Writing `a_Q(L)=1-1[L in U(Q)]`, the move changes this residual-root
coefficient to `a_Q(L)-rho_z(L)` and changes residual owner capacity by
`-gamma_z(T)`. Substitution in (1.3) gives the first equality in (2.2);
(1.5) gives the second. Equation
(2.3) follows from Theorem 1 because the total demand is unchanged. \(\square\)

The deltas of a jointly legal packet add exactly:

\[
                  \delta_{z_1+\cdots+z_t}(Y)
                  =\sum_i\delta_{z_i}(Y).           \tag{2.5}
\]

No halo or locality hypothesis is needed. This is stronger than short-run
blocker additivity. Only the final selector's root collisions, degrees,
protection and topology can interact. The maximum-flow gains themselves do
not add, because the maximizing shore may change.

### 2.1 Same-upper single diamond

For `z=e'-e` with `R(e')=R(e)`,

\[
 \boxed{\delta_z(Y)=\alpha_Y(e')-\alpha_Y(e).}       \tag{2.6}
\]

The new root must be unused; after deleting the old owner edge, the new
endpoints must respect degree two and join distinct primary-forest
components. Since `alpha` lies in `{0,1,2}`, a single replacement changes
global residual flow by at most two.

### 2.2 Dual owner--upper circuits

At a touched upper `R_i`, let `P_i` be the unchanged selected owner facet,
`T_i^-` the removed facet and `T_i^+` the inserted facet. The primary root
changes from

\[
 L_i^-=P_i\cap T_i^-\quad\text{to}\quad L_i^+=P_i\cap T_i^+.
\]

A dual alternating circuit preserves every upper and owner degree, hence
`gamma_z=0`, and

\[
 \boxed{
 \delta_{C_{2\ell}}(Y)=
   \sum_{i=1}^{\ell}\bigl(w_Y(L_i^-)-w_Y(L_i^+)\bigr).} \tag{2.7}
\]

A dual C6 transports three roots and can change flow by at most six; a dual
C8 transports four and can change flow by at most eight. Root collision,
omitted-root, protected and forest guards are still literal. By contrast,
every root--owner fixed-margin circuit has `rho=gamma=0`, so it changes no
closed-shore row and no residual-flow value.

## 3. Exact globally scored neighbourhood oracle

For a current selector, enumerate the legal family `M(Q)` consisting of the
no-op, all same-upper replacements and all alternating dual C6/C8 circuits.
For every candidate `m`, run one fresh residual max-flow and return

\[
                 \arg\max_{m\in\mathcal M(Q)}F(Q+m). \tag{3.1}
\]

This is polynomial in the explicit instance size: C6 and C8 have fixed
length and each candidate evaluation is a max-flow. A nonpositive result is
complete for this bounded neighbourhood only. Completeness in the primary
dual owner--upper fibre requires every legal alternating circuit, not only
C6/C8. Independently, the root--owner Markov theorem proves that higher
chordless circuits can be indispensable in that incidence graph; a matching
indispensability statement for the dual graph needs its own embedding proof.

The equivalent lazy formulation uses one-hot move variables `lambda_m` and
minimizes `theta` subject to

\[
 \theta\ge\Psi_Q(Y)+\sum_m\lambda_m\delta_m(Y)
       \quad(Y\subseteq\mathcal T),\qquad
 \sum_m\lambda_m=1.                                 \tag{3.2}
\]

Separate a tentative move by rebuilding its residual network. At integrality
and after minimizing `theta`, its optimum is exactly the post-move
deficiency. This Benders form can avoid one max-flow per raw candidate while
retaining the exact global score.

A decrease on one returned shore is only a pricing signal. It is necessary
to decrease every currently maximum shore, but even that is not sufficient:
an initially slack shore may become maximum. Equation (2.3), or one fresh
min-cut, is the acceptance rule.

## 4. Unrestricted primary selector master

Let `x_e` range over all allowed diamond columns. The exact structural rows
are

\[
 \sum_{e:R(e)=R}x_e=1,                              \tag{4.1}
\]

\[
 \sum_{e:L(e)=L}x_e\le1,                            \tag{4.2}
\]

\[
 \sum_{e:T\in\{T(e),H(e)\}}x_e\le b_T,             \tag{4.3}
\]

together with protected/boundary rows and the graphic inequalities

\[
 \sum_{e:\{T(e),H(e)\}\subseteq S}x_e\le |S|-1
        \qquad(\emptyset\ne S\subseteq\mathcal T). \tag{4.4}
\]

Introduce `theta>=0` and minimize it subject to

\[
 \boxed{
 \theta\ge\kappa_Y+\sum_e\alpha_Y(e)x_e
             \qquad(Y\subseteq\mathcal T).}         \tag{4.5}
\]

For integral `x`, the optimum `theta` is exactly the residual deficiency.
Adding `theta<=d(Q_inc)-1` asks for a genuinely improving selector.

### Theorem 3 (polynomial separation, including fractional selectors)

Put

\[
 a_L=1-\sum_{e:L(e)=L}x_e,qquad
 c_T=b_T-\sum_{e:T\in\{T(e),H(e)\}}x_e.             \tag{4.6}
\]

For a fractional master point satisfying `a_L,c_T>=0`, use the network

```text
source --(2 a_L)--> root L --(a_L)--> owner T --(c_T)--> sink.
```

One minimum cut returns the maximally violated row (4.5).

#### Proof

For fixed owner shore `Y`, the optimized root contribution is
`a_L min(2,|N(L)-Y|)`. Subtracting the resulting cut from
`2 sum_L a_L` gives exactly the right side of (4.5). \(\square\)

If selector cardinality is fixed, maximizing residual flow and minimizing
`theta` are equivalent. Selectors of different cardinalities must not be
compared by raw flow: their target demands differ by two per primary root.
Use a fixed upper palette, or lexicographically minimize uncovered uppers
before comparing deficiency.

## 5. Which polynomial tool is exact?

### Shore-side submodularity

For fixed `Q`, `w_Y(L)` is supermodular in `Y`; its nonzero marginals occur
only when all but one or all of `N(L)` is already in the shore. Hence
`-Psi_Q(Y)` is submodular. Fixed-selector evaluation is therefore a
submodular minimization, but the explicit residual network gives the
stronger ordinary min-cut implementation.

### Selector-side non-submodularity

The selector objective is a maximum of affine modular rows. This does not
make it submodular. The coefficient-class example

\[
 h(S)=\max\bigl(0,\mathbf1_{a\in S}+\mathbf1_{b\in S}-1\bigr)
\]

violates submodularity on `{a}` and `{b}`. It uses only coefficient values
allowed by the Benders representation. This is a formal obstruction to
deducing selector submodularity from (4.5), not a claimed literal Boolean
K17 counterexample. Selector-side submodular minimization is therefore not
authorized without a new Boolean-specific theorem. Nor does supermodularity
follow: the same max-affine class contains

\[
 g(S)=\max(\mathbf1_{a\in S},\mathbf1_{b\in S}),
\]

which violates supermodularity on `{a}` and `{b}`. Thus the generic selector
objective is neither submodular nor supermodular.

### Min-cost flow

For one fixed shore, the unguarded dual-circuit pricing relaxation assigns
the transition through `R` from `T^-` to `T^+` the cost

\[
 w_Y(P_R\cap T^-)-w_Y(P_R\cap T^+).                 \tag{5.1}
\]

Literal fixed-length C6/C8 enumeration is polynomial and exact after every
guard is replayed. Ordinary negative-cycle search is exact only if its state
space enforces a simple circuit using every upper at most once; otherwise a
walk can use two transitions at one upper, delete both selected facets, and
invalidate (5.1). Root injectivity, omitted/protected roots and forest
legality are further structural guards, so an unguarded negative cycle is
only a pricing relaxation until it is rejected or repriced fail closed.
There is also no single fixed cost vector for the maximum over all shores:
the limiting shore can switch after the move.

The unrestricted selector simultaneously consumes an upper, a root and two
owner slots, and must satisfy a graphic forest. The upper/root marginal alone
is bipartite matching, but the owner and graphic correlation is not supplied
by a min-cost-flow or two-matroid theorem.

### Benders

Benders separation is exact and polynomial, both for bounded moves and for
the fractional unrestricted master. The integral master need not be integral;
branch-and-cut is exact but has no polynomial-time guarantee from the current
theorems. No Boolean-specific NP-hardness claim is made.

## 6. Exact K7 and K9 calibration

At K7 the authenticated selector has flow `25/28`, deficiency three, and a
maximum shore `I=4,J=10,c(Y)=15`. Of 73 legal same-upper replacements, 49
improve that one row. Their global flows split as

```text
24: 6 moves, 25: 23 moves, 26: 20 moves.
```

The upper-93 move `root 84, edge 85--92 -> root 76, edge 77--92` gains two
on the old shore but only one globally. Four legal dual C6 circuits include
two old-shore improvers and zero global improvers.

The independently replayed K9 calibration starts from an 84-edge primary
subforest with 42 components and flow `84/84`. Its 297 legal single-diamond
neighbours have flows

```text
82: 10, 83: 96, 84: 191.
```

The deterministic worst neighbour changes upper 175 from
`root 135, edge 143--167` to `root 139, edge 143--171`. It has flow `82/84`
and maximum shore `I=22,J=12,c(Y)=54`. From this seed:

| move | legal | old-shore improving | global-flow improving | old-row improvers: down/flat/up |
|---|---:|---:|---:|---:|
| same-upper | 296 | 184 | 14 | 23 / 147 / 14 |
| dual C6 | 5 | 3 | 0 | 1 / 2 / 0 |
| dual C8 | 14 | 4 | 0 | 4 / 0 / 0 |

These are literal countercalibrations to incumbent-row descent, not merely
examples where the predicted gain has the wrong magnitude.

## 7. K17 frozen 71-hole extraction and master

The historical 50M snapshot explicitly used for this calibration is rooted
at

```text
/home/amodo/or15/work/root_k17_h1_global_outer_20260802/
  exact_q1_anneal71_stage_20260802
```

The connected factor model, extended model, pair map and exact missing rows
have hashes

```text
24296cdf3b600c4018c109d8de9d352b05913e2cd08b5c7074675fdfc9c63df4
0debc7f6aabfb30b9f69e13da39e3ca355f29206d7dec3e5592cc5544f7c4f63
d90eda6666629aad49a52247b07068d24d3e8da265f587dae55e864dca223d63
5c4b9a9a3cb6fe2a0d4a17b02475a6aa092456dc356db8ab1edab085a1825b0f
```

The map contains 218,790 root--owner incidence variables and 875,088
ordinary pair variables. Decode every selected ordinary pair row as

\[
 e_q=(q,T_q\cup H_q,T_q,H_q).                       \tag{7.1}
\]

This yields 24,308 literal ordinary factor edges. Bucket them by upper
union, retaining every provider occurrence rather than choosing lexicographically.

The necessary non-D palette has 19,412 targets; this snapshot covers 19,341
and has 71 empty buckets. The frozen missing bank has 71 rows of 45 pair
columns, hence 3,195 literals. Passive physical replay has 93 rank-ten holes;
71 and 93 have different scopes and must not be conflated.

This is a historical calibration, not a claim about the live q1 Pareto
endpoint. The shared h1 aggregate continued to acquire later descendants
while this theorem was reviewed. They are intentionally outside this frozen
scope; the 71-hole object is retained because it is the user-designated
exchange snapshot and its literal artifacts are hashed above.

### Two exact modes

1. **Global existence mode.** Use every allowed diamond as an `x` column and
   let the residual flow construct the complementary ordinary factor. The
   incumbent providers are only a warm start/change cost. For the full
   all-upper ordinary selector, make all 875,088 pair columns available and
   select 19,448 primary edges, leaving 4,860 residual roots and target flow
   9,720. A primary forest then has 4,862 components; the later two-path
   contracted rank is 4,860.

2. **Live-factor co-design mode.** Retain the exact h1 factor variables `p_e`
   and channel `x_e<=p_e`. The frozen 71-hole factor is infeasible because its
   71 necessary buckets are empty. Factor-changing root--owner circuits or
   the original exact master must first realize missing providers. Once the
   upper palette is complete, same-upper and dual owner--upper circuits
   optimize primary root support while preserving that palette only when
   every inserted diamond is already a selected factor provider
   (`x_e<=p_e`), or the move is coupled to and replayed with a physical
   factor rethread.

An intermediate necessary-non-D selector may instead fix 19,412 primaries,
leaving 4,896 residual roots and target flow 9,792. This attacks the exact 71
rows but deliberately defers the 36 D-containing targets. Its primary forest
has 4,898 components and residual graphic rank 4,896, again leaving two
paths. Raw flow values from the 19,341-edge partial marking are not comparable
to either fixed-size master.

### Fail-closed optimization transaction

1. Authenticate the four hashes above and replay the incidence/pair channel.
2. Export the 24,308 factor diamonds and all provider buckets.
3. Choose the fixed palette: 19,412 necessary non-D targets or the stronger
   19,448 all-upper target. Do not mix their residual demands.
4. Add (4.1)--(4.5). These rows require a fixed boundary ledger. Either
   branch/fix every selected `D`-neighbour incidence and set
   `b_T=2-1[T=B]-d_T^D`, or keep `d_T^D` as master variables, use
   `c_T=2-1[T=B]-d_T^D-deg_x(T)`, and include
   `+sum_(T in Y) d_T^D` in every deficiency row. Mixing a variable `D` bank
   with a fixed `kappa_Y` is invalid.
5. Seed actual covered colours from the incumbent, but retain every repeat
   provider and all potential columns for empty buckets.
6. Solve/decode/separate by one exact residual min-cut. Add its normalized
   owner-shore row; a repeated violated row is a decoder error.
7. Price same-upper and dual C6/C8 moves on the accumulated shore bank, but
   accept a move only after a fresh global min-cut. For completeness inside a
   dual primary fibre, admit every legal dual alternating circuit; C6/C8
   alone are a restricted neighbourhood.
8. At `theta=0`, export the integral residual flow and separately enforce the
   contracted graphic rank/two-path topology.

Neither same-upper nor dual owner--upper moves can create one of the 71 empty
upper buckets: both preserve the primary upper palette. Root--owner factor
circuits can change upper multiplicities, after which the primary marking
must be extracted again.

## 8. Frozen inputs and scope

The theorem rebases on

```text
closed-shore theorem  efbc4bc95e03794e1a2eb2bf07b1caeb9ee4a368677ab3a6dd1f74abaccdb3ad
Markov theorem        76ac68ed45f0449a8537dc2d76f133638fbf41e622e3e6a80f3bcfa3fe8ee759
K17 h1 aggregate      living file; not a byte-frozen input
K17 71-hole snapshot  four literal hashes in Section 7
```

The K9 finite package is

```text
scratch/r2_k9_primary_residual_exchange_oracle_20260802
manifest SHA-256 8adc0013993a7e3cc7f86275a73634aee5013789b81f0a8f0defcaed1fce1fec
audit SHA-256    25f683c45bc4f738d2771a15d804ea18a2af28ea7956085324d3e53d883dffaa
```

This theorem supplies an exact residual-flow objective and separator. It
does not assert existence of a zero-deficiency K17 selector, integral
polynomial-time optimization, final topology, residence, source, compiler,
opening, exterior windows, regeneration or a universal word.
