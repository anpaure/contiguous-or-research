# Root-lattice banks: closed-price opportunity cost and the exact robust-kernel gate

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional finite reduction.  For a physically admissible
two-state root-lattice bank, its exact dual opportunity cost is a weighted
sum of the one-step subadditivity defects of the closed configuration
price.  After subtracting the workload-linear part, those defects are the
increments of a nonnegative nondecreasing superadditive function.  Thus
the bank inequality is exactly the original all-price inequality with a
small positive perturbation of the signed-tail kernel.  This theorem does
not prove that perturbed inequality.

## 1. Finite exact-work configuration instance

Fix a maximum part size `D>=2`.  Let `s_j` be the number of physical
sockets of exact capacity `j`, `1<=j<=D`, and let `n_L` be the number of
jobs of work `L`.  Assume exact work balance

\[
 \sum_{j=1}^D j s_j=\sum_{L\ge1}L n_L.             \tag{1.1}
\]

For a nonnegative tail price
`theta=(theta_1,...,theta_D)`, the price of one part of length `j` is

\[
 c_\theta(j)=\sum_{q=1}^j\theta_q.                 \tag{1.2}
\]

Let `f_theta(L)` be the minimum total part price over all exact
fragmentations of a length-`L` job into parts of lengths at most `D`.
Allowing an overcover instead gives the same minimum: trim the last part,
which cannot increase (1.2).

The complete dual slack is

\[
 S(\theta)=\sum_{j=1}^D s_jc_\theta(j)
             -\sum_{L\ge1}n_Lf_\theta(L).          \tag{1.3}
\]

For `2<=j<=D`, put

\[
 u^{(j)}=(1^j,0^{D-j}),\qquad
 v^{(j)}=u^{(j-1)}+u^{(1)}.                       \tag{1.4}
\]

The root-lattice bank contains `R_j` labelled length-`j` jobs designated
in state `u^(j)` and `R_j` labelled length-`j` jobs designated in state
`v^(j)`.

We call the bank **socket-admissible** if its exact part multiplicities can
be removed from `(s_j)`: equivalently, if the complete tail minus the bank
tail is itself the conjugate tail of a nonnegative exact-capacity
histogram.  This is stronger than mere coordinatewise nonnegativity of the
tail difference, and it is the precise condition needed for the
closed-price reduction below.

## 2. Closed prices are the exact worst case

### Lemma 2.1 (configuration closure)

Put

\[
 f(L)=f_\theta(L),\qquad
 \widehat\theta_j=f(j)-f(j-1)\quad(1\le j\le D),  \tag{2.1}
\]

with `f(0)=0`.  Then:

1. `f` is nonnegative, nondecreasing and subadditive;
2. `widehat theta_j>=0`;
3. the job minimum induced by the part costs `f(1),...,f(D)` is again
   exactly `f(L)` for every `L`; and
4. `f(j)<=c_theta(j)` for every physical capacity `j`.

Consequently, for a socket-admissible bank, replacing `theta` by
`widehat theta` leaves every residual-job minimum unchanged and can only
decrease the price of the residual physical sockets.  Hence it is enough
to test the bank inequality on closed prices.

#### Proof

Concatenating fragmentations proves subadditivity.  Trimming one unit from
a nonempty part in an optimal fragmentation of `L+1` proves
`f(L)<=f(L+1)`, and nonnegativity is immediate.  Thus (2.1) is
nonnegative.

For any fragmentation `L=lambda_1+...+lambda_t`, substitute into each
part an original `theta`-optimal fragmentation.  This gives

\[
 f(L)\le\sum_i f(\lambda_i).
\]

Conversely an original optimal fragmentation of `L`, evaluated with the
new part prices, costs at most its old cost `f(L)`.  Therefore the new
minimum is exactly `f(L)`.  The one-part fragmentation proves
`f(j)<=c_theta(j)` for `j<=D`.

If the residual sockets have exact counts `s'_j>=0`, their old and new
prices are respectively `sum_j s'_j c_theta(j)` and `sum_j s'_j f(j)`.
The latter is no larger, while all residual-job minima agree.  Thus a
closed price is at least as strong a residual separator. `square`

The socket-admissibility qualification is essential.  A coordinatewise
nonnegative tail vector need not be the conjugate of a physical capacity
histogram, and closure need not decrease its dot product coordinatewise.

## 3. Exact opportunity cost of the two-state bank

Assume from now on that the price is closed, so a part of length `j` costs
`f(j)` and a length-`j` job has minimum `f(j)`.

### Theorem 3.1 (bank cost is local subadditivity defect)

Define

\[
 \delta_j=f(j-1)+f(1)-f(j)\ge0\qquad(2\le j\le D). \tag{3.1}
\]

Then a bank job designated in `u^(j)` has opportunity cost zero, while a
bank job designated in `v^(j)` has opportunity cost exactly `delta_j`.
Therefore

\[
 \boxed{\Pi_G(f)=\sum_{j=2}^D R_j\delta_j.}        \tag{3.2}
\]

#### Proof

The state `u^(j)` is the one-part fragmentation and costs `f(j)`, the job
minimum.  The state `v^(j)` is the two-part fragmentation `(j-1,1)` and
costs `f(j-1)+f(1)`.  Subtracting the same job minimum gives (3.1)--(3.2).
`square`

This improves the generic estimate
`Pi_G<=2 sum_j jR_j`: only one of the two base states pays, and its price is
the actual subadditivity defect rather than the full work.

## 4. Workload-defect transform

Put

\[
 g(q)=qf(1)-f(q)\qquad(q\ge0).                    \tag{4.1}
\]

### Lemma 4.1

The function `g` is nonnegative, nondecreasing and superadditive, with
`g(0)=g(1)=0`, and

\[
 \boxed{g(q)-g(q-1)=\delta_q\qquad(q\ge2).}       \tag{4.2}
\]

#### Proof

Repeated subadditivity gives `f(q)<=qf(1)`, so `g>=0`.  The one-step
subadditivity inequality `f(q)<=f(q-1)+f(1)` gives (4.2) and monotonicity.
Finally,

\[
 g(i+j)=(i+j)f(1)-f(i+j)
       \ge g(i)+g(j)
\]

by subadditivity of `f`. `square`

Equivalently, the increment measure `a_q=Delta g(q)` satisfies the reverse
anchored-window inequalities

\[
 \sum_{q=x+1}^{x+t}a_q\ge\sum_{q=1}^t a_q,       \tag{4.3}
\]

whenever the displayed indices exist.  Thus the workload defect is not an
arbitrary nonnegative vector; its prefix is the least massive window of
each length.

Let

\[
 M_q=\sum_{j\ge q}s_j,\qquad
 N_q=\sum_{L\ge q}n_L,\qquad
 Q_q=M_q-N_q.                                     \tag{4.4}
\]

Summation by parts and (1.1) give

\[
 S(f)=\sum_{q\ge1}Q_q\Delta f(q)
     =-\sum_{q\ge1}Q_q\Delta g(q),               \tag{4.5}
\]

because `Delta f(q)=f(1)-Delta g(q)` and

\[
 \sum_qQ_q=\sum_jjs_j-\sum_LL n_L=0.             \tag{4.6}
\]

Combining (3.2) and (4.5) yields the exact bridge.

### Theorem 4.2 (robust-kernel equivalence)

For every closed price,

\[
 \boxed{
 S(f)-\Pi_G(f)
 =-\sum_{q\ge1}\bigl(Q_q+R_q^*\bigr)\Delta g(q),
 }                                                  \tag{4.7}
\]

where `R_1^*=0`, `R_q^*=R_q` for `2<=q<=D`, and `R_q^*=0` for `q>D`.
Consequently the socket-admissible root bank is fractionally reservable if
and only if

\[
 \boxed{
 -\sum_{q\ge1}Q_q a_q\ge\sum_{q=2}^D R_q a_q
 }                                                  \tag{4.8}
\]

for every increment sequence `a=Delta g` whose cumulative function is
nonnegative, nondecreasing and superadditive.

Thus same-depth bank reservation is not a consequence of bare all-price
nonnegativity.  It is the **perturbed** all-price theorem obtained by
replacing the signed tail `Q` by `Q+R^*` on the first `D` coordinates.

## 5. Exact zero-cost face and size control

### Corollary 5.1 (zero bank cost)

If `R_j>0` for every `2<=j<=D`, then

\[
 \Pi_G(f)=0
 \quad\Longleftrightarrow\quad
 f(j)=jf(1)\quad(0\le j\le D).                   \tag{5.1}
\]

#### Proof

Every summand in (3.2) is nonnegative.  Hence zero cost is equivalent to
`delta_j=0` for every `j`.  Equation (4.2), together with `g(1)=0`, is
equivalent to `g(j)=0` throughout the physical range. `square`

For the minimal root bank

\[
 R_j=\left\lceil{D L_{\max}\over j}\right\rceil,
\]

one has

\[
 L_{\max}g(D)
 \le \Pi_G(f)
 \le \left(\left\lceil{D L_{\max}\over2}\right\rceil\right)g(D).
                                                               \tag{5.2}
\]

Indeed `sum_(j=2)^D delta_j=g(D)` and the displayed minimum and maximum
bound every `R_j`.  Thus prices close to the workload-linear face make the
bank automatically cheap; away from that face, the exact missing theorem
is a quantitative lower bound for the complete slack in terms of the same
defect increments.

### Proposition 5.2 (no universally free nontrivial bank)

No fixed nontrivial same-work exchange bank can have zero opportunity cost
for every closed nondecreasing subadditive price.

#### Proof

Take the closed price `f(0)=0` and `f(j)=1` for every `j>=1`.  It is
nondecreasing and subadditive.  A positive-work job has minimum one,
attained by a one-part fragmentation.  Every fragmentation with two or
more parts costs at least two.  Hence the only universally optimal
configuration of a length-`j<=D` job is its one-part state.  Two distinct
states cannot both be universally free, so their difference cannot
generate a nonzero root-lattice direction at zero opportunity cost.
`square`

Accordingly, avoiding the perturbation in (4.8) requires extra physical
capacity (as in the adjacent-depth absorber), a price-adaptive bank built
inside the exposed optimal face, or a new robust all-price theorem.  A
fixed same-depth two-state bank cannot remove it formally.

## 6. Relation to the Apéry stability dichotomy

The arithmetic-stability theorem gives, for a formal Apéry clock `U`,

\[
 \Phi(U)\ge C(\lambda)
 -{\Delta\over\lambda}
   \bigl(\lVert K'\rVert_1+\lambda\operatorname{Var}(K')\bigr). \tag{6.1}
\]

If `Delta<=epsilon_0 lambda`, then `Phi(U)>=3K(0)/16`.  Restoring the
finite Bellman shoulder gives only

\[
 \Phi(V)\ge\Phi(U)-\mathscr S^-.                 \tag{6.2}
\]

Hence the near-arithmetic, small-shoulder branch does fund the root bank
whenever the clocks are normalized so that the finite
Boolean-to-Rayleigh transfer has the explicit form

\[
 S(f)/W=\Phi(V)+o(1).                              \tag{6.3}
\]

Namely, if

\[
 \Delta\le\epsilon_0\lambda,\qquad
 \mathscr S^-\le {3K(0)\over32},                 \tag{6.4}
\]

then `Phi(V)>=3K(0)/32`, so the Boolean slack is `Omega(W)` and dominates
`Pi_G=O(D^2L_max)`.

This is the proof-safe direction.  The two alternatives in the existing
counterclock dichotomy do **not** themselves provide reserve:

* a large relative Apéry displacement merely makes (6.1) inconclusive;
  it is not a lower bound for (4.8);
* adverse shoulder debt enters (6.2) with a minus sign and decreases the
  available dual slack one-for-one.

Therefore a theorem claiming that either defect automatically pays the
bank would simultaneously prove the unresolved robust all-price
inequality.  It cannot be obtained by reinterpreting the existing
dichotomy.  The exact analytic target is now (4.8), or equivalently a
quantitative stability theorem of the form

\[
 -\sum_qQ_q\Delta g(q)
 \ge \sum_{q=2}^D R_q\Delta g(q)                 \tag{6.5}
\]

on the reverse-window cone.

The distinction between the two construction levels is exact:

* unperturbed all-price feasibility is sufficient for the existing
  adjacent-depth `B+1` residual absorber;
* the perturbed inequality (6.5) is needed only by the fixed same-depth
  root-lattice route toward coefficient zero.

## 7. A finite counterexample to bare all-price implying a bank

Take `D=2`, two length-two jobs and two length-one jobs.  Let the physical
sockets consist of two capacity-two sockets and two capacity-one sockets.
The complete instance is integrally feasible: put the two long jobs in
the two capacity-two sockets and the two singleton jobs in the two
singleton sockets.  It therefore satisfies every all-price inequality.

Use the two length-two jobs as one root-bank pair: designate one in the
state `u^(2)=(2)` and the other in the state `v^(2)=(1,1)`.  Their total
bank tail is `(3,1)`.  Removing it from the complete socket tail `(4,2)`
leaves `(1,1)`, the physical tail of one capacity-two socket.  Thus the
bank is socket-admissible.  But the two residual singleton jobs cannot
both use the one residual socket, so the residual instance is infeasible.

The closed price

\[
 f(0)=0,\qquad f(1)=f(2)=1                       \tag{7.1}
\]

certifies the failure exactly: the complete slack is zero, while the
forced two-part state has opportunity cost

\[
 f(1)+f(1)-f(2)=1.                               \tag{7.2}

\]

Thus even exact primal feasibility and universal unperturbed all-price
nonnegativity do not imply fractional interior for a prescribed
root-lattice bank.  Boolean asymptotics may have enough additional
structure to prove (6.5), but that is a substantive robust theorem.

## 8. Scope

This note proves the closed-price reduction under physical
socket-admissibility, the exact opportunity formula, the
workload-defect/reverse-window transform, and the perturbed-kernel
equivalence.  It does not prove the unperturbed all-price theorem, the
robust inequality (6.5), physical occurrence naming, zero-slack
containment Hall, boundary realization, protected serialization,
`B(k)+O(1)`, or `nu(k)=B(k)`.
