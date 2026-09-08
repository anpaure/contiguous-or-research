# Pull-clock audit: corrected fractional proof and the unchanged one-copy gate

Date: 2026-08-01  
Status: proof-safe repair of the pull-clock fractional construction.  The
submitted proof has reversed inequalities in both its nonnegativity and slot
cost arguments, but the intended conclusions follow from the reverse chain.
The construction gives a single periodic multicover inside each fixed owner;
it does not improve the one-owner/one-target integral rounding gate.

## 1. Setup

Put

```text
r=ceil(k/2),  W=C(k,r),
d=min{t:tW+C(t+1,2)>=sum_(1<=s<r)C(k,s)},
c=r-d-1.
```

Let `b_1>=...>=b_d>=0`, extended by zero above `d`, be the left-filled
Ferrers column counts, and put

```text
q_s=[C(k,s)-b_s]/W.
```

The already-proved Ferrers identities give

```text
0<=q_1<=...<=q_(r-1)<=1,       sum_s q_s<=d.
```

For `1<=t<=c` and `1<=j<=d`, define

```text
A_t=q_(c-t+1),                  P=sum_t A_t,
G_j=1-q_(c+j),                 H=sum_j G_j.
```

Then `H-P=d-sum_s q_s>=0`.  When `H=0`, also `P=0`, and the all-high clock
already dominates `q`; below assume `H>0`.  Put

```text
w_j=G_j/H,   w_(d+1)=w_(d+2)=0,
Delta_j=w_j-w_(j+1),
x_(delta,j)=A_delta Delta_j-A_(delta+1)Delta_(j+1),
A_(c+1)=0.
```

The staircase tile is

```text
S_(delta,j)={(t,q):1<=t<=delta, 1<=q<=j-delta+t}.
```

## 2. Correct ratio lemma

Assume first that `c>=d`.  Set

```text
rho=(k-c+1)/c=C(k,c)/C(k,c-1)>1.
```

### Lemma 2.1

For every defined index,

```text
A_delta/A_(delta+1)>=rho             when A_(delta+1)>0,  (2.1)
Delta_(j+1)/Delta_j<=rho             when Delta_j>0.      (2.2)
```

The cross-multiplied weak forms are used when a denominator vanishes.

### Proof

For `2<=s<=c`, binomial ratios decrease with `s`, so

```text
C(k,s)>=rho C(k,s-1).
```

Since `b_s<=b_(s-1)` and `rho>=1`,

```text
C(k,s)-b_s
 >=rho C(k,s-1)-rho b_(s-1).
```

Thus `q_s>=rho q_(s-1)`, which is (2.1) after reversing the low ranks.

The high band begins above the Ferrers correction because `c+j>d`.  Write

```text
p_s=C(k,s)/W,       D_s=p_(s+1)-p_s.
```

Then `Delta_j=D_(c+j)/H`, including the endpoint convention `p_r=1`.
For `s<=r-2`, whenever the ratio is nonzero,

```text
D_(s+1)/D_s
 =[(k-s)(k-2s-3)]/[(s+2)(k-2s-1)]
 <(k-s)/(s+1)
 <=(k-c-1)/(c+2)
 <rho.
```

At the odd-middle endpoint the numerator is zero, so the same weak bound
holds.  This proves (2.2).  QED.

The submitted proof stated both comparisons in the opposite direction.  In
particular `D_(s+1)/D_s` is smaller, not larger, than the adjacent binomial
ratio.

### Corollary 2.2 (nonnegative tile densities)

```text
x_(delta,j)>=0.
```

Indeed, (2.1)--(2.2) give

```text
A_(delta+1)Delta_(j+1)
 <=(A_delta/rho)(rho Delta_j)=A_delta Delta_j.
```

## 3. Exact staircase decomposition

A cell `(t,q)` belongs to `S_(delta,j)` exactly when

```text
delta>=t,        j>=q+delta-t.
```

Therefore two telescoping sums give

```text
sum_(delta>=t) sum_(j>=q+delta-t) x_(delta,j)=A_t w_q. (3.1)
```

Thus the product coupling `M_(tq)=A_t w_q` is a nonnegative combination of
the physical pull staircases.  Its low row sums are `A_t`; its high-column
usage is `Pw_q=(P/H)G_q<=G_q`.

## 4. Correct slot-cost proof

Let

```text
C=sum_(delta,j)(j+1)x_(delta,j).
```

Direct telescoping gives

```text
C=A_1+Pw_1+(P-A_1)(w_1-w_2).                         (4.1)
```

Put

```text
alpha=p_c,   beta=p_(c+1),   gamma=p_(c+2),
theta=1/rho=c/(k-c+1).
```

Since `A_1<=alpha` and `0<=w_1-w_2<=1`, (4.1) gives the sharper convenient
form

```text
C<=alpha+Pw_1+(P-alpha)(w_1-w_2).                    (4.2)
```

Indeed, the difference between the right side and (4.1) is
`(alpha-A_1)[1-(w_1-w_2)]>=0`.

From (2.1),

```text
P-A_1=sum_(t>=2)A_t
 <=theta sum_(t=1)^(c-1)A_t
 <=theta P.
```

As `H>=P`,

```text
(P-alpha)/H<=(P-A_1)/H<=theta.                       (4.3)
```

We also have

```text
Pw_1<=G_1=1-beta,
w_1-w_2=(gamma-beta)/H.
```

One more adjacent-difference comparison, now at `s=c` (one step before the
displayed `Delta` sequence), says

```text
(gamma-beta)/(beta-alpha)<=rho.                     (4.4)
```

This is proved by the same exact formula for `D_(s+1)/D_s`; it is not
literally an instance of (2.2), whose first ratio starts at `s=c+1`.

Substitution in (4.2), using (4.3)--(4.4), yields

```text
C<=alpha+(1-beta)+theta rho(beta-alpha)=1.           (4.5)
```

This repairs the submitted argument.  Its displayed bounds
`(P-alpha)/H<=rho` and `(gamma-beta)/(beta-alpha)>=rho` have the wrong
strength and direction and do not imply `C<=1`.

## 5. Finite range outside `c>=d`

The standard estimate `d<=ceil(sqrt(r))` implies `c>=d` for `r>=8`.
Evaluating the defining inequality for the finite range `r<8` leaves only

```text
k=3,4,5: c=0;
k=7:     (r,d,c)=(4,2,1);
k=8:     (r,d,c)=(4,2,1);
k=11:    (r,d,c)=(6,3,2).
```

For `c=0`, the all-high clock offers every strict-lower rank and dominates
the demand.  In the remaining cases the exact pull costs are

```text
k=7:   C=2/5;
k=8:   C=1/5;
k=11:  C=62/273,
```

and every `x_(delta,j)` is nonnegative by direct rational evaluation.

The original long-double range scan

```text
scratch/audit_pull_clock_ratio_and_cost_20260801.cpp
```

reports `PASS_RANGE` through `k=2000`, but that output is evidence only:
at large `k`, floating subtraction cannot resolve the `O(d^2)` Ferrers
boundary correction against exponential binomial coefficients.

The replacement verifier

```text
scratch/audit_pull_clock_exact_cppint_20260801.cpp
SHA256 1359a3a12edae4d8886b0abf2af2e205ed0432d8804071b3a86b446546f178dc
```

uses a standalone exact bigint, reconstructs the Ferrers correction without
rounding, checks every cross-multiplied ratio and the cost identity, and
directly checks the three exceptional positive-`c` cases.  Its H100 O3 run
reports

```text
FINITE k=7  r=4 d=2 c=1 h=0 PASS=1
FINITE k=8  r=4 d=2 c=1 h=0 PASS=1
FINITE k=11 r=6 d=3 c=2 h=0 PASS=1
PASS_EXACT_PULL_CLOCK_RANGE 2..2000 failures=0 main=1992 finite=3
```

The exact output SHA is
`732b0fb6e1a5d43d8f00f43888984a8051425a0b2d5ce086e5ba750750f5f4c5`.
The all-`k` conclusion rests on the analytic ratio proof plus the finite
exact calculation, not on extrapolating the range scan.  Hence the repaired
pull-clock construction is valid for every relevant `k`.

## 6. Literal stationary realization

After clearing denominators, concatenate `Nx_(delta,j)` low runs of length
`j`, each followed by a high separator, and fill unused positions with high
letters.  Choose `N` divisible by `d+1`.  At time `t`, use private label
`f_(t mod d+1)`; a high letter is `C union {f_t}`, and a low letter of type
`(delta,j)` is `(C-D) union {f_t}` for a fixed `delta`-subset `D` during
that run.

Every `(d+1)`-window contains all private labels and a high separator, so
its owner is the same fixed set `T=C union F`.

Here is the literal staircase replay.  In the all-high word, a proper suffix
of length `ell` has rank `c+ell`.  Inside a low run of length `j`, each
suffix wholly contained in that run loses the same `delta`-set `D`.  For
fixed `ell<=j` there are `j-ell+1` such occurrences and their rank becomes
`c-delta+ell`.  Thus the number of new occurrences of low rank
`c-t+1` is

```text
L_(delta,j)(t)=(j-delta+t)_+.
```

At high rank `c+q`, the net loss is

```text
R_(delta,j)(q)
 =(j-q+1)_+-(j-q-delta+1)_+
 =min(delta,(j-q+1)_+).
```

This is exactly the number of `t` for which `(t,q)` lies in
`S_(delta,j)`.  Hence the tile records the literal low additions and the
literal *net* high deficits; it is not merely a rank-count analogy.

Uniform averaging over shifts, labels, omitted sets and owners makes every
target at a fixed rank uniform.  Thinning the available marks from `v_s` to
`q_s` completes the fractional theorem.  The periodic word proves literal
stationarity because it is itself a closed de Bruijn walk.

The independent literal verifier

```text
scratch/audit_pull_clock_literal_tiles_20260801.cpp
SHA256 76792100bce69bc44dca56a3ee201ac6331dd4233fb0e3ffa2a5b8ef4fee7e36
```

constructs the cyclic private-phase word, enumerates every proper suffix,
and compares its complete signed rank histogram with `L_(delta,j)` and
`R_(delta,j)`.  Its H100 O3 replay reports

```text
PASS_PULL_CLOCK_LITERAL_TILES cases=9360 maxd=12 maxc=15
```

with output SHA
`a19a2bb95cc7e81f4f6f69e3308bc97e45cefa7013ce5365c950a6330d17a8b3`.
This finite replay supports the literal identities; the displayed counting
argument proves them for all parameters.

This gives one periodic occurrence-cycle in each fixed-owner fibre, which
is a modest support improvement over an arbitrary convex mixture of rotor
cycles.  It still repeats that owner `N` times.

## 7. Exact one-copy integer problem

Even before names are restored, multiplying the block densities by the
desired horizon gives the necessary rank-only integer packing system

```text
sum_(delta,j)L_(delta,j)(t) z_(delta,j)=C(k,c-t+1)-b_(c-t+1),
sum_(delta,j)R_(delta,j)(q) z_(delta,j)<=W-C(k,c+q)+b_(c+q),
sum_(delta,j)(j+1)z_(delta,j)<=W,
z_(delta,j) in Z_>=0.                               (7.1)
```

For a cyclic private clock one must additionally close its phase (the
displayed periodic construction arranged this by taking the horizon
divisible by `d+1`).  The rational pull proof supplies even (7.1) only over the
reals, not over the
integers: generally `Wx_(delta,j)` need not be integral.  Its displayed
matrix is not TU (already `L_(1,2)(1)=2`).  An extended integral automaton
can serialize any *given* integer block multiset, but the exact rank rows in
(7.1) are extra Parikh constraints and do not inherit network
integrality.  The existing aggregate monotone-rotor semigroup theorem
sidesteps this particular package restriction and already gives exact
integer rank/type decomposition for the canonical demand for `k>=31`.
Thus (7.1), even if separately rounded, would not close the stronger named
problem below.

There is a literal integer-RHS hole already at `(c,d)=(2,2)`.  Set the
horizon, low demands and high capacities to

```text
W=3,       (N_1,N_2)=(1,1),       (G_1,G_2)=(2,1).
```

For example, the fractional choice

```text
z_(1,1)=1/2,        z_(2,2)=1/2
```

has low output `(1,1)`, high use `(3/2,1/2)`, and slot cost `5/2`.
The submitted product formula itself also gives a feasible point: with
`A=(1/3,1/3)` and `w=(2/3,1/3)`, multiplying by `W=3` yields

```text
z_(1,2)=z_(2,1)=z_(2,2)=1/3,
```

of cost `8/3`.
However, the second low equation

```text
z_(2,1)+2z_(2,2)=1
```

forces `z_(2,1)=1,z_(2,2)=0` integrally.  The first then forces
`z_(1,1)=1,z_(1,2)=0`, whose slot cost is four, exceeding the horizon.
Thus even the rank-only pull-block polytope is not integral.  This is an
abstract package obstruction, not a counterexample to the canonical
binomial demand.

Let `D` be the literal order-`d` trace digraph.  An arc `e=u->v` has owner
`T(e)`, and occurrence `(e,j)` offers the fixed target `U_j(e)`.  After the
Ferrers boundary targets are fixed, a one-copy circuit asks for binary
variables `x_e,z_(e,j)` satisfying

```text
sum_(e:T(e)=T)x_e=1                           (every owner T),
sum_(e in delta+(v))x_e=sum_(e in delta-(v))x_e (every state v),
sum_((e,j):U_j(e)=S) z_(e,j)=1                (every residual target S),
z_(e,j)<=x_e,
```

plus connected support.  For an open trail or bounded sidecar, the balance
row is changed by the two endpoints and the added route arcs.

The pull blocks do not remove any of these rows.  A literal pull block is a
run of several occurrences of one fixed owner, so no nontrivial block is a
legal one-copy atom.  Recolouring its positions by distinct owners changes
the actual `(d+1)`-window unions and is exactly the unresolved owner/flag
lifting problem.

## 8. No generic TU or bounded-defect consequence

The state-incidence matrix alone is TU, but appending the owner-partition
rows is not.  One rank-two owner with its two opposite depth-one traces has
the minor

```text
[ 1  1 ]
[-1  1 ]
```

of determinant two.  This is already the pure-private (`c=0`) pull clock.

The obstruction occurs in the actual triangular instance `k=4`: the six
owners are the edges of `K_4`, and a one-copy choice orients every edge.
Every vertex has odd selected degree, so no balanced circuit or open trail
exists without added route edges.  More generally, for the same
`(r,d)=(2,1)` pull-clock family on even `k`, an open trail needs exactly
`k/2-1` added route edges and a circuit exactly `k/2`; a matching gives the
upper bound and parity gives the lower bound.

The infinite family is not on the central-rank optimal-depth slice except
at `k=4`.  It therefore does not refute `B(k)+O(1)` for the Boolean problem.
It does prove that no bounded-defect rounding theorem follows from the
pull-clock stationary/block axioms alone.

There is one TU island: if every owner tail state is fixed integrally, then
choosing heads to meet the prescribed state indegrees is a bipartite
`b`-matching.  This does not include simultaneous tail choice, named-target
colouring, or connectivity.

## 9. Exact coupling to an SCD flag selector

The fractional clock cannot simply be intersected with an arbitrary exact
protected SCD selector.  For a fixed integral flag table, write `w` for an
ordered rail state and form the literal successor bipartite graph `G_w` as
in
`MATH_THEOREM_SCD_FLAG_RAIL_BALANCE_STATEWISE_HALL_AND_OWNER_GATE_20260801.md`.
The exact coupling criterion is:

1. the prefix and suffix flag counts agree at every `w`;
2. every `G_w` has a perfect matching; and
3. those statewise matchings have one common choice using every owner colour
   exactly once.

The pull clock supplies a rational stationary measure, hence fractional rail
balance after full symmetrization.  The protected SCD theorem supplies an
integral exact named-target marginal.  Neither theorem makes the same flag
table satisfy the three rows above.

This failure is literal, not hypothetical.  The standard recursive SCD at
`(k,m,d)=(7,3,3)` is an exact target selector but has rail-divergence
`L1=24`, fifteen zero-out roots, and the explicit dead flag

```text
p={0,1,6},   z=(1,0),   B(p)={6}.
```

All possible successor roots have flag `(0,beta)` with
`beta in {2,3,4,5}`, whereas the last rail entry must lie in `{6}`.  Its
statewise Hall graph therefore has an isolated left vertex.  So that exact
SCD selector cannot be coupled to the clock at all.

The independent H100 O3 replay uses

```text
scratch/audit_scd_flag_turn_balance_20260801.cpp
SHA256 6aa038097f5904c04dd3244c12e81755faffedc267fec4a92048f06fd03a17de
```

and reproduces

```text
n=7 m=3 d=3 chains=35 flags=35 build=OK
div_nz=6 div_l1=24 div_max=5 turn_edges=36 zero_out=15
```

with full output SHA
`5dfdf9a156cb07c3d35bc1a68dd8eacd6ac6e30db0ac1f11344a66df27d6213b`.

This does not prove that every co-designed protected selector fails.  It
proves the sharp quantifier boundary: coupling is a new integral
statewise-Hall plus owner-rainbow theorem.  The `k=4` parity example in
Section 8 separately shows that even connected literal fractional
stationarity does not imply a bounded-defect one-copy rounding in the
general pull-clock class.

## 10. Verdict

The repaired pull-clock proof gives a valid and explicit fractional
stationary clock for every `k`.  At the integer quotient, the existing
aggregate monotone-rotor theorem is already stronger: it gives an exact
age-signature decomposition for the canonical demand for every `k>=31`.
The pull blocks add connectedness only inside a repeated fixed-owner
multicover.  They do not supply a one-copy owner/target rounding, a TU
formulation, or a dimension-independent route sidecar.

The surviving gate is unchanged: one occurrence-labelled owner-rainbow
circulation, with exact named lower colours and connected support, followed
by the independent upper/residence/compiler guards.
