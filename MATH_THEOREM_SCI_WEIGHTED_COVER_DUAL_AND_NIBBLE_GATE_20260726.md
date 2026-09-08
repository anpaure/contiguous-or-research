# SCI as weighted covering rank: exact dual and the correlated-nibble gate

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or
independent depthwise rounding is used.

## 0. Verdict

The owner-recycling strip-cover problem is a set-cover problem, not a
matching problem. Its weighted-rank analogue is therefore a
column-density inequality.

For a nonnegative target weight \(w\), define

\[
 \rho(w)=
 \max\left\{
 \max_S w_S,\
 \max_{C\in\mathscr C_{m,h}}
 {w(\mathcal T_H(C))\over2h+2H}
 \right\}.                                                \tag{0.1}
\]

Then the exact fractional identity

\[
 \tau^*_{m,H,h}=W+\frac HhN_1
\]

is equivalent to the sharp all-weight inequality

\[
 \boxed{
 \sum_{S\in\mathcal B_{m,H}}w_S
 \le
 \left(W+\frac HhN_1\right)\rho(w)
 \qquad(w\ge0).}                                          \tag{0.2}
\]

The best constant is attained by the dual weight

\[
 w_S=
 \begin{cases}
 1,&|S|=m,\\[2mm]
 H/(2h),&|S|=m-1\text{ or }m+1,\\[2mm]
 0,&\text{all other protected ranks}.
 \end{cases}                                               \tag{0.3}
\]

Thus edge transitivity completely removes arbitrary dual weights for the
initial fractional SCI instance. Every dual vector may be averaged over
coordinates without changing its objective or feasibility; the remaining
finite optimization is a one-dimensional layer knapsack.

This does not remove the integral gap. Inequality (0.2) is the dual
characterization of the fractional cover number itself. A transitive set
system may still have a constant integral covering gap; disjoint triangles
with their full wreath-product automorphism group give a transitive
example with fractional cover \(3t/2\) and integral cover \(2t\).

Independent orbit rounding also fails at the SCI scale. Selecting every
cycle independently with probability \(1/D_1\) gives every signed
depth-one target mean load one, but leaves

\[
                         (2e^{-1}+o(1))N_1=\Theta(W)
\]

first-layer targets uncovered. Any multiplier \(1+o(1)\), which is the
largest compatible with an \(o(W)\) cost increase, leaves the same positive
fraction. A covering nibble must therefore be strongly negatively
correlated and nearly resolve the two first-shadow layers.

There is an exact asymptotic integral target.  SCI holds if and only if
there is a family \(\mathcal F\) of cycles with

\[
 |\mathcal F|={N_1\over2h}+o(W/h),                         \tag{0.4}
\]

its middle union has size \(N_1+o(W)\), both signed first-shadow layers
have \(o(W)\) holes, and the aggregate number of holes at depths
\(2,\ldots,H\) is \(o(W)\). This gives

\[
 (2h+2H)|\mathcal F|
 +\left|\mathcal B_{m,H}\setminus
       \bigcup_{C\in\mathcal F}\mathcal T_H(C)\right|
 =\tau^*_{m,H,h}+o(W).                                    \tag{0.5}
\]

Equivalently, the first three resource layers require an approximate
quota-perfect hypergraph matching, while the same selected cycles must
cover all deeper layers.

Known exact fixed-frame strip factors meet the cycle-count and middle
requirements even more strongly: they use \(W/(2h)+o(W/h)\) cycles and
cover almost every middle owner. Their extra cycle cost above
\(\tau^*\) is only

\[
                         {H\over h}(W-N_1)=o(W).
\]

But they do not cover the physical shadow layers: the fixed-frame
Gaussian type deficit remains \(\Theta(W)\). Hence known strip factors do
not certify SCI.

The surviving theorem is a correlated covering-nibble statement for the
full mixed-frame orbit.  Symmetry computes the exact density constant for
the initial uniform instance, and (0.2) then applies to every weight.
However, edge transitivity does not symmetrize the objective of an adaptive
residual, does not keep that residual layer-uniform after integral choices,
and does not produce the required near-resolution of the first-shadow
layers.

## 1. The SCI primal and its exact dual

Put

\[
 W=\binom{2m}{m},
 \qquad
 N_q=\binom{2m}{m-q},
\]

and let

\[
 \mathcal B_{m,H}
 =\bigcup_{q=-H}^{H}\binom{[2m]}{m+q}.
\]

For every physical cyclic \(h\)-strip \(C\), let
\(\mathcal T_H(C)\) be its \(2h\) middle targets and its \(2h\) lower and
\(2h\) upper targets at every depth \(1,\ldots,H\). Its exact literal
cost is

\[
                         c=2h+2H.                          \tag{1.1}
\]

The fractional SCI programme is

\[
 \boxed{
 \begin{aligned}
 {\rm(P)}\qquad
 \min\quad&c\sum_Cx_C+\sum_Sz_S,\\
 \text{subject to}\quad&
 z_S+\sum_{C:S\in\mathcal T_H(C)}x_C\ge1
                                      &&(S\in\mathcal B_{m,H}),\\
 &x_C,z_S\ge0.
 \end{aligned}}                                           \tag{1.2}
\]

Its integer version requires \(x_C,z_S\in\{0,1\}\).

### Proposition 1.1 (exact SCI dual)

The dual of (1.2) is

\[
 \boxed{
 \begin{aligned}
 {\rm(D)}\qquad
 \max\quad&\sum_{S\in\mathcal B_{m,H}}y_S,\\
 \text{subject to}\quad&
 0\le y_S\le1 &&(S\in\mathcal B_{m,H}),\\
 &\sum_{S\in\mathcal T_H(C)}y_S\le2h+2H
                                      &&(C\in\mathscr C_{m,h}).
 \end{aligned}}                                           \tag{1.3}
\]

#### Proof

Give the cover inequality for \(S\) the multiplier \(y_S\ge0\).
Minimization over the singleton variable \(z_S\ge0\) forces
\(y_S\le1\). Minimization over \(x_C\ge0\) gives the strip constraint.
The remaining constant term is \(\sum_Sy_S\). \(\square\)

## 2. Exact weighted covering rank

For \(w\ge0\), define \(\rho(w)\) by (0.1).

### Theorem 2.1 (covering-rank equivalence)

The least constant \(K\) such that

\[
                         \sum_Sw_S\le K\rho(w)
 \qquad\text{for every }w\ge0                              \tag{2.1}
\]

is exactly the fractional cover optimum \(\tau^*_{m,H,h}\). Consequently,

\[
                         K=W+\frac HhN_1.                  \tag{2.2}
\]

#### Proof

If \(w\ne0\), then

\[
                         y={w\over\rho(w)}
\]

satisfies \(0\le y_S\le1\) and every strip inequality in (1.3).
Duality therefore gives

\[
                         {\sum_Sw_S\over\rho(w)}
 \le\tau^*_{m,H,h}.
\]

This proves (2.1) with \(K=\tau^*\).

Conversely, take an optimal dual vector \(y^*\). It satisfies
\(\rho(y^*)\le1\) and
\(\sum_Sy^*_S=\tau^*\). Hence every valid \(K\) is at least \(\tau^*\).
\(\square\)

Equivalently, for every residual weight \(w\), either some singleton has
density at least \(\sum_Sw_S/\tau^*\), or some whole strip has that
density:

\[
 \boxed{
 \max\left\{
 \max_Sw_S,\
 \max_C{w(\mathcal T_H(C))\over2h+2H}
 \right\}
 \ge{\sum_Sw_S\over\tau^*}.}                              \tag{2.3}
\]

This is an exact fractional density theorem. Applying it greedily gives
the usual logarithmic set-cover bound, not an additive \(o(W)\)
integrality theorem.

## 3. Symmetrization and the exact extremal dual

The coordinate group acts transitively on cycles, on the middle layer, and
on each signed depth layer. If \(y\) is dual feasible, average all its
coordinate translates. The result is dual feasible, has the same total
objective, and is constant on each signed layer.

Write the averaged values as

\[
 a_0,\qquad a_q^-,a_q^+\quad(1\le q\le H).
\]

Every strip contains \(2h\) targets in each represented layer, so its
constraint becomes

\[
 a_0+\sum_{q=1}^H(a_q^-+a_q^+)
 \le1+\frac Hh,                                           \tag{3.1}
\]

with all variables in \([0,1]\). The objective is

\[
 Wa_0+\sum_{q=1}^HN_q(a_q^-+a_q^+).                       \tag{3.2}
\]

Since

\[
                         W>N_1>N_2>\cdots>N_H,
\]

the layer knapsack first takes

\[
                         a_0=1
\]

and puts its remaining mass \(H/h\) in the two signed depth-one
variables. For example,

\[
                         a_1^-=a_1^+={H\over2h},
\]

with all deeper values zero. This is exactly (0.3), and its objective is

\[
                         W+\frac HhN_1.                    \tag{3.3}
\]

Thus arbitrary nonuniform dual weights cannot improve the initial
fractional optimum. This use of symmetry is valid because both the
right-hand side of every cover constraint and the dual objective are
coordinate-invariant.

## 4. Why symmetry does not settle integral SCI

Let \(\tau\) be the integral cover optimum. Any integral cover of cost
\(\tau\) also proves

\[
                         \sum_Sw_S\le\tau\rho(w)
\]

by charging every target to a covering column. But Theorem 2.1 already
proves the stronger constant \(\tau^*\), whether or not an integral cover
of comparable cost exists.

Therefore the all-weight density inequality detects the fractional cover,
not the integral cover. This is the covering/packing distinction:

* for a transitive packing orbit, translating one large integral matching
  controls all route weights and proves proximity to the stable-set
  polytope;
* for set cover, the all-weight inequality is already LP duality and can
  coexist with a large integral gap.

### Proposition 4.1 (transitivity alone does not close covering gaps)

For every \(t\ge1\), there is a target- and column-transitive set system
which is a disjoint union of \(t\) triangles, with columns the two-point
edges inside each triangle. Its fractional cover number is \(3t/2\), while
its integral cover number is \(2t\).

#### Proof

One triangle has fractional solution \(1/2\) on each of its three edges,
of value \(3/2\). Summing its three point constraints proves the matching
dual lower bound \(3/2\). Integrally, two edges are necessary and
sufficient.

For \(t\) triangles the programme is a direct sum, giving the displayed
values. The wreath product

\[
                         S_t\wr S_3
\]

permutes triangles and acts transitively on all points and on all edge
columns. \(\square\)

Thus even simultaneous row and column transitivity permits a linear
integrality gap.

## 5. Residual weights after partial covering

For a residual demand vector \(b\in[0,1]^{\mathcal B_{m,H}}\), the
fractional residual cover value is

\[
 \tau^*(b)
 =\max\left\{
 \sum_Sb_Sy_S:
 0\le y_S\le1,\
 \sum_{S\in\mathcal T_H(C)}y_S\le c
 \right\}.                                                \tag{5.1}
\]

If \(b\) is not constant on coordinate orbits, averaging \(y\) changes
the objective \(\sum b_Sy_S\). Hence the symmetrization of Section 3 is
not valid for an arbitrary residual produced by earlier integral choices.

The density inequality (2.3) still supplies one efficient next column, but
iterating it gives only the harmonic greedy bound. Edge transitivity does
not assert that the residual remains pseudorandom or layer-uniform.

This is the exact answer to the residual-weight question:

* initial arbitrary dual weights are removed by averaging because the SCI
  demand is uniform;
* arbitrary adaptive residual weights are not removed by edge
  transitivity.

There is also an exact complementary-slackness ledger.  Put

\[
                         a={H\over2h}.
\]

For a feasible fractional solution let

\[
 \ell_S=z_S+\sum_{C:S\in\mathcal T_H(C)}x_C.
\]

Because the dual vector (0.3) saturates every strip column, subtraction of
its value from the primal objective gives the identity

\[
\begin{aligned}
 {\rm cost}(x,z)-\tau^*
 ={}&\sum_{|S|=m}(\ell_S-1)\\
 &+a\sum_{|S|=m-1,m+1}(\ell_S-1)\\
 &+(1-a)\sum_{|S|=m-1,m+1}z_S\\
 &+\sum_{2\le \lvert |S|-m\rvert\le H}z_S .         \tag{5.2}
\end{aligned}
\]

All four terms are nonnegative.  For an integral cycle family
\(\mathcal F\), repair every uncovered target by its singleton, write
\(\mu_0,\mu_1^\pm\) for the three relevant multiplicities, and write
\(M_q^\pm\) for the numbers of holes.  Then (5.2) becomes

\[
\begin{aligned}
 \mathfrak L(\mathcal F)={}&
 \sum_{|S|=m}(\mu_0(S)-1)_+\\
 &+a\!\sum_{|S|=m-1}(\mu_1^-(S)-1)_+
   +a\!\sum_{|S|=m+1}(\mu_1^+(S)-1)_+\\
 &+(1-a)(M_1^-+M_1^+)
   +\sum_{q=2}^H(M_q^-+M_q^+).                       \tag{5.3}
\end{aligned}
\]

Consequently the exact integral gap is

\[
 \boxed{\tau-\tau^*=\min_{\mathcal F\subseteq\mathscr C_{m,h}}
                         \mathfrak L(\mathcal F).}    \tag{5.4}
\]

This is the genuinely weaker owner-recycling criterion.  Middle collisions
have unit price, first-shadow collisions have only the collar price
\(a=H/(2h)=o(1)\), and collisions at depths at least two are free.  On the
other hand, every nonmiddle hole has asymptotically unit price.  The ledger
alone would allow first-shadow overmultiplicity \(o(W/a)\); nevertheless,
the common \(2h\)-incidence count and the middle constraint force it down to
\(o(W)\) in every genuinely near-optimal family.  This counting consequence
is proved in Theorem 7.1.

To verify (5.2), insert the dual vector (0.3) into

\[
 c^Tx+\mathbf1^Tz-\mathbf1^Ty
 =\sum_Cx_C(c-A_C^Ty)
  +\sum_Sz_S(1-y_S)+\sum_Sy_S(\ell_S-1).
\]

The first sum vanishes, because every strip contains \(2h\) middle targets
and \(4h\) signed depth-one targets.  Formula (5.3) follows from the
cost-minimizing integral repair
\(z_S=\mathbf1_{\{\mu(S)=0\}}\), and minimizing over \(\mathcal F\) proves
(5.4).

## 6. Independent orbit rounding has a Poisson hole barrier

Let \(D_q\) be the number of catalogue cycles containing a fixed signed
depth-\(q\) target, and let \(D_0\) be the middle degree. The exact orbit
ratios are

\[
 {D_0\over D_1}={N_1\over W},
 \qquad
 {D_q\over D_1}={N_1\over N_q}.                           \tag{6.1}
\]

Select every cycle independently with probability

\[
                         p={t\over D_1},
\]

and repair every uncovered target by its singleton. The expected objective
is exactly

\[
 \begin{aligned}
 \mathbb E\,{\rm cost}(t)
 ={}&(2h+2H){tN_1\over2h}\\
 &+W(1-p)^{D_0}
 +2\sum_{q=1}^HN_q(1-p)^{D_q}.                            \tag{6.2}
 \end{aligned}
\]

### Proposition 6.1 (independent rounding cannot prove SCI)

At the fractional intensity \(t=1+o(1)\), the expected number of uncovered
signed depth-one targets is

\[
 \boxed{
 2N_1(1-t/D_1)^{D_1}
 =(2e^{-1}+o(1))N_1=\Theta(W).}                            \tag{6.3}
\]

In fact, uniformly over every intensity \(0\le t\le D_1\),

\[
 \mathbb E\,{\rm cost}(t)
 \ge (1+\log2-o(1))N_1
 =\tau^*+(\log2-o(1))W.                               \tag{6.4}
\]

Thus no independent orbit sampling, at any intensity, has expected cost
\(\tau^*+o(W)\).

#### Proof

Equation (6.3) follows from \(D_1\to\infty\).  Keeping only the cycle cost
and the two signed depth-one repair terms in (6.2) gives

\[
 {\mathbb E\,{\rm cost}(t)\over N_1}
 \ge t+2(1-t/D_1)^{D_1}.                              \tag{6.5}
\]

The right side has its unique minimum at

\[
 t_{D_1}=D_1\left(1-2^{-1/(D_1-1)}\right)=\log2+o(1),
\]

where its value is

\[
 D_1\left(1-2^{-1/(D_1-1)}\right)
 +2^{-1/(D_1-1)}
 =1+\log2+o(1).
\]

Finally \(N_1/W=m/(m+1)=1-o(1)\) and
\(\tau^*=W+(H/h)N_1=W+o(W)\), proving (6.4). \(\square\)

The same obstruction holds for a uniform sample of nearly the same fixed
size.  Indeed, if \(M=|\mathscr C_{m,h}|\) and \(n\) cycles are sampled
without replacement, then a fixed depth-one target is missed with exact
probability

\[
 {\binom{M-D_1}{n}\over\binom Mn}
 =\prod_{j=0}^{n-1}\left(1-{D_1\over M-j}\right).
\]

When \(nD_1/M=t=O(1)\), this is \(e^{-t+o(1)}\), since
\(D_1/M=2h/N_1=o(1)\) and \(n/M=t/D_1=o(1)\).  For unbounded \(t\), the
cycle cost alone is \(\omega(W)\).  Thus fixing the sample size does not
remove the barrier: it is the Poisson probability of missing a target whose
fractional load is one.

## 7. A precise correlated covering-nibble target

For a cycle family \(\mathcal F\), let

\[
 U_0(\mathcal F)
 =\left|\bigcup_{C\in\mathcal F}
       \left(\mathcal T_H(C)\cap\binom{[2m]}m\right)\right|,
\]

and let \(M_q^\pm(\mathcal F)\) be its numbers of missing signed
depth-\(q\) targets.

### Theorem 7.1 (exact asymptotic SCI nibble output)

Assume \(H/h=o(1)\).  Then \(\tau-\tau^*=o(W)\) if and only if there are
cycle families \(\mathcal F=\mathcal F_m\) satisfying

\[
 |\mathcal F|={N_1\over2h}+o(W/h),                         \tag{7.1}
\]

\[
                         U_0(\mathcal F)=N_1+o(W),          \tag{7.2}
\]

\[
                         M_1^-(\mathcal F)+M_1^+(\mathcal F)=o(W), \tag{7.3}
\]

and

\[
 \sum_{q=2}^H
 \bigl(M_q^-(\mathcal F)+M_q^+(\mathcal F)\bigr)=o(W).     \tag{7.4}
\]

Equivalently, these conditions are a necessary and sufficient correlated
covering-nibble output for SCI.

#### Proof

First suppose (7.1)--(7.4).  Use every cycle in \(\mathcal F\), and repair
every uncovered protected target by its singleton. By (7.1), the cycle cost
is

\[
 \begin{aligned}
 (2h+2H)|\mathcal F|
 &=(2h+2H){N_1\over2h}+o(W)\\
 &=N_1+\frac HhN_1+o(W).
 \end{aligned}
\]

The number of missing middle targets is, by (7.2),

\[
                         W-N_1+o(W).
\]

Equations (7.3)--(7.4) make all other singleton repairs \(o(W)\).
The total is

\[
 W+\frac HhN_1+o(W)=\tau^*+o(W).
\]

Conversely, suppose \(\tau-\tau^*=o(W)\), and choose an integral family
\(\mathcal F\) attaining the minimum in (5.4).  Thus
\(\mathfrak L(\mathcal F)=o(W)\).  Put

\[
                         R=2h|\mathcal F|.
\]

The first-shadow hole terms in (5.3) give
\(M_1^-+M_1^+=o(W)\), because \(1-a=1-o(1)\).  Hence either signed
first-shadow union has size \(N_1-o(W)\), and therefore

\[
                         R\ge N_1-o(W).                    \tag{7.5}
\]

The middle collision term is

\[
 \sum_{|S|=m}(\mu_0(S)-1)_+=R-U_0(\mathcal F)=o(W).
                                                                    \tag{7.6}
\]

Since \(U_0(\mathcal F)\le W\), this gives

\[
                         R\le W+o(W)=N_1+o(W),             \tag{7.7}
\]

where \(W-N_1=W/(m+1)=o(W)\).  Equations (7.5)--(7.7) yield
\(R=N_1+o(W)\), which is (7.1), and (7.6) then yields (7.2).
Finally, the last line of (5.3) gives (7.4).  This proves necessity.

For completeness, the same counting now forces the apparently weakly
priced first-shadow collisions to be small.  For either sign,

\[
 \sum_S(\mu_1^\pm(S)-1)_+
 =R-(N_1-M_1^\pm)=o(W).                                \tag{7.8}
\]

Thus the selected columns act as an approximate matching on all three
critical resource layers, even though this was not imposed separately.
\(\square\)

The first three conditions say that, on the resource system consisting of
middle targets and the two signed depth-one layers, the chosen cycles are
an approximate quota-perfect matching:

* they have \(N_1+o(W)\) middle occurrences and cover
  \(N_1+o(W)\) distinct middle targets;
* they have \(N_1+o(W)\) occurrences in each signed first layer and cover
  all but \(o(W)\) targets there.

Condition (7.4) is genuinely additional. Distinct first-shadow claims do
not force distinct or covering depth-two claims; the local bowtie minor
already shows why depth two is not a network projection of depth one.

## 8. What the known exact strip factors certify

For dyadic \(h=o(m)\), the fixed-frame Stage-A construction partitions all
but \(e^{-\Omega(m)}W\) middle owners into cyclic \(h\)-strips. Let
\(\mathcal F_{\rm A}\) be that family. Then

\[
 |\mathcal F_{\rm A}|={W\over2h}+o(W/h),\qquad
 U_0(\mathcal F_{\rm A})=W-o(W).                         \tag{8.1}
\]

Its cycle cost is

\[
 (2h+2H)|\mathcal F_{\rm A}|
 =W+\frac HhW+o(W).                                       \tag{8.2}
\]

Compared with the exact fractional value, the excess due solely to its
larger cycle count and lack of middle singleton repair is

\[
 \left(W+\frac HhW\right)
 -\left(W+\frac HhN_1\right)
 ={H\over h}(W-N_1)=o(W).                                 \tag{8.3}
\]

Thus cycle count and middle coverage are already coefficient-safe.

However, one fixed pair frame has a positive Gaussian physical-target
deficit. For some \(q=\Theta(\sqrt m)\),

\[
                         M_q^-(\mathcal F_{\rm A})
                         +M_q^+(\mathcal F_{\rm A})
                         =\Theta(W).                       \tag{8.4}
\]

Therefore (7.3)--(7.4) are not certified. Exact strip factors solve the
owner/middle part of SCI, not the labelled shadow cover.

## 9. Orbit mixtures and the precise open theorem

A convex mixture of coordinate translates of Stage-A factors produces a
uniform fractional cycle vector of total mass
\(W/(2h)+o(W/h)\), asymptotically the optimal mass
\(N_1/(2h)\), but it is not an integral cover. An integral choice of one
translated factor retains a fixed-frame target deficit; choosing independent
cycles from different translates encounters the Poisson barrier of Section
6.

The missing object is a dependent mixed-frame selection which:

1. selects only \(N_1/(2h)+o(W/h)\) cycles, or the slightly larger
   \(W/(2h)+o(W/h)\) Stage-A count;
2. keeps their middle and first-shadow collision excess \(o(W)\);
3. covers all deeper signed layers with aggregate \(o(W)\) holes;
4. may recycle middle owners, but pays exactly for every selected strip.

Generic covering-nibble theorems do not presently give this conclusion in
the growing edge-size regime. A strip column has

\[
                         2h(2H+1)
\]

physical target claims, while the first-shadow fractional load is exactly
one. Standard independent or weakly dependent covering leaves a positive
fraction at such a critical load. A successful nibble must behave like a
near-perfect matching on the middle and first-shadow resources and like a
cover on every deeper resource layer, all with the same cycle choices.

## 10. Exact implication boundary

The following statements are proved.

1. The SCI dual is (1.3).
2. The exact weighted covering-rank inequality is (0.2), with best constant
   \(\tau^*=W+(H/h)N_1\).
3. Coordinate symmetrization reduces the initial dual to the layer
   knapsack (3.1)--(3.2), whose optimizer is (0.3).
4. The exact integral defect is the weighted collision/hole ledger
   (5.3)--(5.4).
5. Edge transitivity does not imply integral set-cover proximity.
6. Independent orbit rounding has a uniform linear gap, (6.4).
7. The correlated-nibble output (7.1)--(7.4) is equivalent to SCI.
8. Known exact strip factors satisfy the cycle-count and middle conditions
   but fail the physical shadow-cover condition.

The following statements are not proved.

1. A correlated mixed-frame nibble satisfying (7.1)--(7.4).
2. The additive \(o(W)\) SCI integrality gap.
3. Coefficient one.

Thus arbitrary dual weights are fully controlled at the fractional level,
but adaptive residual weights and integral coverage remain. Owner recycling
removes the packing obstruction; it does not remove the critical-load
covering problem at the two first-shadow layers.
