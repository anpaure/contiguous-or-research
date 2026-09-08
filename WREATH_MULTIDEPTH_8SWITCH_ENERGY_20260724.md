# Multidepth balanced-eight-switch energy and the capacity-packing gate

## 1. Result and limitation

Let

\[
 n=2m+1,\qquad W=\binom{n}{m},\qquad
 N_q=\binom{n}{m-q}.
\]

This note gives an exact all-depth update formula for a balanced two-wreath
eight-switch.  If the switch cuts the two old wreaths into four paths of
vertex lengths \(\ell_1,\ldots,\ell_4\), then at depth \(q\) exactly

\[
 r_q=\sum_{i=1}^4\min(\ell_i,2q)\le 8q                 \tag{1.1}
\]

old colour slots and the same number of new colour slots can differ.  All
other depth-\(q\) colours cancel literally.  This yields an exact sparse
update of the whole capacity ledger, not just of the first shadow.

There is a canonical nonnegative quadratic capacity energy \(Q_q\).  It
vanishes exactly when every depth-\(q\) load is in its prescribed
floor/ceiling range.  A factor with

\[
 \sum_{q=1}^h Q_q=o\!\left(\frac{W}{nh}\right)         \tag{1.2}
\]

can be pruned to the capacity-respecting packing required by the CRP
reduction, losing only \(o(W/h)\) middle vertices.

The exact finite audit also gives a rigorous obstruction.  Neither the
depth-one energy nor the unweighted sum of the energies has strict descent
under balanced eight-switches: positive local minima occur already for
\(m=4\), and an all-depth positive local minimum occurs for both \(m=4\) and
\(m=5\).  Thus a successful proof must bound all local minima, use neutral
plateau/absorber moves, change the weights dynamically, or enlarge the move
class.  The assertion that every nonbalanced factor has a strictly
energy-decreasing balanced eight-switch is false.

No asymptotic CRP theorem, and hence no constant-one theorem, is claimed.

## 2. A radius-\(q\) colour attached to each middle vertex

Let \(F\) be an exact wreath factor in \(KG(n,m)\).  Orient every wreath and
write \(\sigma_F\) for its successor permutation.  For a middle vertex
\(X\) and \(1\le q<m\), define

\[
 c_{F,q}(X)=
 \bigcap_{j=0}^{q}\sigma_F^{-q+2j}(X).              \tag{2.1}
\]

The definition is independent of the choice of orientation, because
reversing an oriented wreath merely reverses the list of sets in the
intersection.

### Lemma 2.1 -- radius-colour identity

For every wreath \(C\) of \(F\), the multiset

\[
 \{c_{F,q}(X):X\in V(C)\}                           \tag{2.2}
\]

is precisely the cyclic interval family \(\mathcal C_q(C)\) of its
\((m-q)\)-intervals.  In particular, every colour in (2.2) has size
\(m-q\), and the \(n\) colours on one wreath are pairwise distinct.

#### Proof

Let \(z_i\) be the coordinate omitted by the edge from the \(i\)-th to the
\((i+1)\)-st middle vertex.  With cyclic subscripts, the middle vertices are

\[
 A_i=\{z_{i+1},z_{i+3},\ldots,z_{i+2m-1}\}.          \tag{2.3}
\]

Intersecting \(A_{i-q},A_{i-q+2},\ldots,A_{i+q}\)
leaves exactly

\[
 \{z_{i+q+1},z_{i+q+3},\ldots,z_{i-q+2m-1}\},       \tag{2.4}
\]

which has \(m-q\) elements.  Multiplication of subscripts by \(2\) is a
permutation of \(\mathbb Z_n\), so the sets (2.4), as \(i\) varies, are the
ordinary cyclic intervals of length \(m-q\) in the associated coordinate
order.  A nonempty proper cyclic interval has a unique start, proving
distinctness.  \(\square\)

Write

\[
 \mu_{F,q}(S)=|\{X:c_{F,q}(X)=S\}|,
 \qquad S\in\binom{[n]}{m-q}.                       \tag{2.5}
\]

Since every middle vertex is a centre, one has

\[
 \sum_S\mu_{F,q}(S)=W.                              \tag{2.6}
\]

## 3. Exact seam cancellation under a balanced eight-switch

Consider a balanced two-wreath eight-switch as characterized in
`WREATH_SHADOW_SWITCH_AUDIT.md`.  It cuts two old \(n\)-cycles twice each,
leaving four untouched paths \(P_1,\ldots,P_4\) of positive vertex lengths
\(\ell_1,\ldots,\ell_4\), where

\[
 \ell_1+\ell_2+\ell_3+\ell_4=2n.                   \tag{3.1}
\]

The four paths are reconnected, possibly with some path orientations
reversed, into two new \(n\)-cycles.

### Theorem 3.1 -- exact all-depth switch update

For \(1\le q<m\), put

\[
 r_q=2n-\sum_{i=1}^4\max(\ell_i-2q,0)
     =\sum_{i=1}^4\min(\ell_i,2q).                  \tag{3.2}
\]

There are removal and addition histograms \(\rho_q,\alpha_q\), supported
only on the seam-crossing radius-\(q\) centres, such that

\[
 \boxed{\mu_{F',q}=\mu_{F,q}-\rho_q+\alpha_q}       \tag{3.3}
\]

and

\[
 \|\rho_q\|_1=\|\alpha_q\|_1=r_q\le8q.            \tag{3.4}
\]

If \(\delta_q=\alpha_q-\rho_q\), then

\[
 \sum_S\delta_q(S)=0,\qquad
 \|\delta_q\|_1\le16q,\qquad
 \|\delta_q\|_2^2\le32q.                          \tag{3.5}
\]

These statements are exact even when a path has fewer than \(2q+1\)
vertices.

#### Proof

The colour at a centre depends only on the factor segment from distance
\(q\) before the centre to distance \(q\) after it; see (2.1).  A centre in
a path of length \(\ell\) has this entire segment inside the path in exactly

\[
 \max(\ell-2q,0)                                    \tag{3.6}
\]

positions.  At such a centre the same path segment occurs before and after
the switch.  A reversal of the path is harmless because (2.1) is
orientation-independent.  Its old and new colours therefore cancel
literally.

Among the \(2n\) centres on the two touched cycles, the number not covered
by (3.6) is the first expression in (3.2).  Using (3.1) gives the second
expression.  The new cycles contain the same four paths, so the number of
new seam-crossing centres is the same \(r_q\).  Recording their old and new
colours gives (3.3)--(3.4), and \(r_q\le4(2q)=8q\).

By Lemma 2.1 a colour occurs at most once on each touched old wreath and at
most once on each touched new wreath.  Hence
\(0\le\rho_q(S),\alpha_q(S)\le2\), and consequently
\(|\delta_q(S)|\le2\).  Now

\[
 \|\delta_q\|_1
 \le\|\rho_q\|_1+\|\alpha_q\|_1\le16q,
\]

and \(\delta_q(S)^2\le2|\delta_q(S)|\) gives the last
bound in (3.5).  Equality of the total removal and addition masses gives
\(\sum_S\delta_q(S)=0\).  \(\square\)

Thus the apparent \(\Theta(nh)\)-sized multiband object has an
\(O(q)\)-sparse change at depth \(q\) under the exact factor-preserving
move.

## 4. The exact quadratic capacity energy

Write

\[
 W=c_qN_q+r_q^{\rm cap},\qquad
 0\le r_q^{\rm cap}<N_q,                            \tag{4.1}
\]

and define

\[
 \boxed{
 Q_q(F)=\frac12\sum_{S\in\binom{[n]}{m-q}}
  (\mu_{F,q}(S)-c_q)(\mu_{F,q}(S)-c_q-1).}          \tag{4.2}
\]

For every integer \(d\), \(d(d-1)/2\ge0\), with equality exactly for
\(d\in\{0,1\}\).  Therefore

\[
 Q_q(F)\ge0,                                        \tag{4.3}
\]

and

\[
 Q_q(F)=0
 \iff
 \mu_{F,q}(S)\in\{c_q,c_q+1\}\quad\hbox{for every }S.
                                                               \tag{4.4}
\]

Because the loads sum to \(W\), (4.4) automatically puts load \(c_q+1\)
on exactly \(r_q^{\rm cap}\) targets.  Thus \(Q_q=0\) is exactly the
floor/ceiling capacity condition, without choosing the high-capacity targets
in advance.

There is also no hidden first-moment obstruction at a zero.  Put
\(r=m-q\).  Every wreath has exactly \(r\) length-\(r\) intervals through
each coordinate, so

\[
 \sum_{S\ni x}\mu_{F,q}(S)=rW/n.                   \tag{4.4a}
\]

If \(Q_q=0\) and \(\mathcal R_q=\{S:\mu_{F,q}(S)=c_q+1\}\), then

\[
 |\mathcal R_q|=r_q^{\rm cap},\qquad
 |\{S\in\mathcal R_q:x\in S\}|
 =\frac{r\,r_q^{\rm cap}}n                       \tag{4.4b}
\]

for every coordinate \(x\).  Thus the high-capacity family produced by an
energy zero is automatically one of the regular families constructed
abstractly in `CAPACITY_POINT_MARGIN_COMPATIBILITY_20260724.md`.  The
potential is therefore minimizing over the correct point-compatible
capacity fibre, rather than over spurious balanced vectors.

The same potential has an exact pair-collision interpretation.  Let

\[
 P_q(F)=\sum_S\binom{\mu_{F,q}(S)}2
\tag{4.4c}
\]

be the number of unordered pairs of depth-`q` occurrences with the same
target.  The information-theoretic minimum among integer load vectors of
total mass `W` is

\[
 P_q^{\min}=(N_q-r_q^{\rm cap})\binom{c_q}{2}
 +r_q^{\rm cap}\binom{c_q+1}{2}.
\tag{4.4d}
\]

Direct expansion of (4.2) gives the lossless identity

\[
\boxed{Q_q(F)=P_q(F)-P_q^{\min}.}
\tag{4.4e}
\]

Thus `Q_q` is exactly the pair-collision excess above the balanced capacity
floor.  In particular, a second-moment or switching argument must remove the
entire excess in (4.4e), not merely show that raw pair collisions are sparse.

There is an exact harmonic form as well.  Let `Omega` be the oriented cyclic
orders modulo rotation, let `A_r` be rank-`r` cyclic-interval incidence, and
orient the wreaths of `F` arbitrarily to obtain an indicator `x` on `Omega`.
With

\[
 x_0={1\over m!(m+1)!}{\bf1}_\Omega,
 \qquad y=x-x_0,
\tag{4.4f}
\]

one has `A_m y=0` and

\[
 \mu_{F,q}-{W\over N_q}{\bf1}=A_{m-q}y.
\tag{4.4g}
\]

Writing `W=c_qN_q+r_q^{cap}`, direct expansion gives

\[
\boxed{
 Q_q(F)={1\over2}\|A_{m-q}y\|_2^2
 -{r_q^{\rm cap}(N_q-r_q^{\rm cap})\over2N_q}.}
\tag{4.4h}
\]

The final term is the fixed integer quantization floor.  Thus the capacity
energy is exactly the squared middle-kernel shadow norm, up to a factor-
independent constant.  The cross-rank spectrum of this norm is computed in
`WREATH_CROSS_RANK_SPECTRAL_LEAKAGE_20260724.md`.

### Proposition 4.1 -- exact switch energy

Under the switch of Theorem 3.1,

\[
\begin{aligned}
 Q_q(F')-Q_q(F)
  &=\sum_S\delta_q(S)(\mu_{F,q}(S)-c_q)
    +\frac12\sum_S\delta_q(S)(\delta_q(S)-1)\\
  &=\sum_S\mu_{F,q}(S)\delta_q(S)
    +\frac12\|\delta_q\|_2^2.                      \tag{4.5}
\end{aligned}
\]

In particular, the nonnegative quadratic toll in (4.5) is at most

\[
 \frac12\|\delta_q\|_2^2\le16q.                   \tag{4.6}
\]

#### Proof

For

\[
 f_q(x)=\tfrac12(x-c_q)(x-c_q-1),
\]

direct expansion gives

\[
 f_q(x+d)-f_q(x)=d(x-c_q)+\tfrac12d(d-1).           \tag{4.7}
\]

Sum (4.7) with \(d=\delta_q(S)\).  The identities
\(\sum_S\delta_q(S)=0\) turn the first line of (4.5) into the second;
(4.6) follows from (3.5).  \(\square\)

For comparison, moving one occurrence from a target of load \(a\) to a
target of load \(b\) changes \(Q_q\) by exactly

\[
 b-a+1.                                             \tag{4.8}
\]

It is therefore strictly favourable precisely when the source is at least
two load units heavier than the target.

For weights \(w_q\ge0\), put

\[
 \Phi_w(F)=\sum_{q=1}^h w_qQ_q(F).                 \tag{4.9}
\]

Every balanced switch satisfies the exact formula obtained by summing
(4.5), with total quadratic toll at most

\[
 T_w=16\sum_{q=1}^h w_q q.                          \tag{4.10}
\]

## 5. From small energy to a capacity-respecting packing

The next statement connects the energy directly to the CRP theorem.

### Lemma 5.1 -- optimal balanced-capacity overflow

Fix a depth and abbreviate \(N=N_q,c=c_q,r=r_q^{\rm cap}\).  For a load
vector \(\mu\) of total mass \(W=cN+r\), put

\[
 D^- =\sum_S(c-\mu(S))_+,
 \qquad
 D^+ =\sum_S(\mu(S)-(c+1))_+.                      \tag{5.1}
\]

Among all capacity vectors \(b(S)\in\{c,c+1\}\) with
\(\sum_Sb(S)=W\), the minimum overflow is

\[
 \boxed{
 O_q^*(\mu)=\min_b\sum_S(\mu(S)-b(S))_+
            =\max(D^-,D^+)\le D^-+D^+\le Q_q.}     \tag{5.2}
\]

#### Proof

Let

\[
 A=\sum_S(\mu(S)-c)_+,
 \qquad k=|\{S:\mu(S)\ge c+1\}|.
\]

The total-sum identity gives \(A=r+D^-\), while separating the first unit
above \(c\) gives \(A=k+D^+\).  Assigning the \(r\) high capacities to
overloaded targets saves exactly \(\min(r,k)\) units, so

\[
 O_q^*=A-\min(r,k)
 =\begin{cases}D^-,&k\ge r,\\D^+,&k<r.
 \end{cases}                                        \tag{5.3}
\]

Moreover \(D^--D^+=k-r\), proving the maximum formula.  If
\(d=\mu(S)-c\le-1\), then \(d(d-1)/2\ge-d\); if \(d\ge2\), then
\(d(d-1)/2\ge d-1\).  Summing these pointwise inequalities proves
\(D^-+D^+\le Q_q\).  \(\square\)

### Theorem 5.2 -- energy-pruning bridge

For every exact wreath factor \(F\) and every \(h<m\), one can delete at
most

\[
 \sum_{q=1}^h Q_q(F)                                \tag{5.4}
\]

wreaths so that the remaining wreaths respect a balanced floor/ceiling
capacity vector at every depth \(q\le h\).  The number \(L\) of uncovered
middle vertices consequently satisfies

\[
 \boxed{L\le n\sum_{q=1}^h Q_q(F).}                \tag{5.5}
\]

In particular, (1.2) implies the CRP hypothesis \(L=o(W/h)\).

#### Proof

At each depth choose a capacity vector attaining (5.2), and let \(O\) be
the sum of all current overflows over all depths.  Initially,

\[
 O\le\sum_{q=1}^hQ_q(F).                            \tag{5.6}
\]

If an overflow remains, choose a depth-target pair \((q,S)\) with load
above capacity and delete a wreath containing that occurrence.  This lowers
that overflow by at least one.  Deletion only lowers other loads, so it
cannot increase any overflow.  After at most \(O\) deletions all capacities
are respected.  Exact middle ownership means each deleted wreath uncovers
exactly \(n\) middle vertices, giving (5.5).  \(\square\)

The bound is deliberately one-sided: a deleted wreath can remove many
overflow units, so (5.5) need not be sharp.

## 6. A precise conditional descent target

For a balanced switch \(C\), define its weighted linear score

\[
 \Lambda_C(F)=
 \sum_{q=1}^h w_q\sum_S
 (\mu_{F,q}(S)-c_q)\delta_{C,q}(S).                 \tag{6.1}
\]

Proposition 4.1 gives

\[
 \Delta_C\Phi_w\le \Lambda_C(F)+T_w.              \tag{6.2}
\]

Hence the following is immediate but useful.

### Proposition 6.1 -- drift implies a local-minimum bound

Suppose that at every factor in a switch-connected class there is a
probability distribution on its legal balanced eight-switches satisfying

\[
 \mathbb E_C\Lambda_C(F)\le-\kappa\Phi_w(F)         \tag{6.3}
\]

for some \(\kappa>0\).  Then every balanced-switch local minimum of
\(\Phi_w\) satisfies

\[
 \boxed{\Phi_w(F)\le\frac{16\sum_{q\le h}w_q q}{\kappa}.} \tag{6.4}
\]

Moreover, repeated strict descent reaches such a factor.

For uniform weights, (6.4) is \(O(h^2/\kappa)\).  To deduce the sufficient
energy scale (1.2) from this estimate alone, one needs

\[
 \kappa\gg \frac{nh^3}{W}.                         \tag{6.5}
\]

At the illustrative pair-exposure scale \(\kappa=\Theta(1/B)=
\Theta(n/W)\), the toll estimate yields only
\(O(Wh^2/n)\), larger than the pruning target by a factor of order \(h^3\).
Thus even a mean-drift theorem must exploit more than an unstructured
two-wreath exposure, or must amortize the quadratic toll through neutral
multi-switch routes.

## 7. Exact finite obstructions to naive strict descent

The checker

`scratch/audit_wreath_multidepth_energy.py`

uses the exhaustive exact-switch generator in
`scratch/check_wreath_shadow_switches.py`.  All quantities are recomputed
from the physical factor after every switch.

### 7.1 Depth-one obstruction

At the \(m=4\) raw-missing greedy trap,

\[
 (M_1;Q_1,Q_2,Q_3,Q_4)=(2;3,34,0,0).               \tag{7.1}
\]

There are fourteen legal balanced eight-switches, and their depth-one
energy changes have histogram

\[
 \{0:9,\ +1:2,\ +2:3\}.                            \tag{7.2}
\]

Thus \(Q_1>0\), but no legal balanced switch decreases \(Q_1\).  This is a
finite rigorous counterexample to strict single-depth convex descent.

For comparison, at the analogous \(m=5\) raw-missing trap,

\[
 (M_1;Q_1,Q_2,Q_3,Q_4,Q_5)=(25;32,206,524,0,0),    \tag{7.3}
\]

four legal switches lower \(Q_1\).  The quadratic potential can escape a
plateau of the raw missing-colour objective, but not every such plateau.

### 7.2 All-depth obstruction

Deterministic steepest descent for the unweighted energy
\(\Phi=\sum_qQ_q\) terminates at the following positive local minima:

| \(m\) | descent steps | missing tuple \((M_0,M_1,\ldots,M_m)\) | \((Q_1,\ldots,Q_m)\) | legal neighbours | best \(\Delta\Phi\) |
|---:|---:|:---|:---|---:|---:|
| 4 | 5 | \((0,3,0,0,0)\) | \((4,21,0,0)\) | 10 | 0 |
| 5 | 32 | \((0,29,2,0,0,0)\) | \((36,154,316,0,0)\) | 32 | 0 |

Therefore

\[
 \Phi(F)>0\quad\Longrightarrow\quad
 \exists C:\Delta_C\Phi(F)<0                       \tag{7.4}
\]

is false even in the first audited dimensions.

### 7.3 The successful \(m=4\) plateau route is not energy-monotone

Along the archived six-switch path to full support and the two subsequent
balancing switches, the exact pairs `(missing tuple, capacity energy)` are

| step | missing tuple | \((Q_1,Q_2,Q_3,Q_4)\) |
|---:|:---|:---|
| 0 | \((0,4,0,0,0)\) | \((5,36,0,0)\) |
| 1 | \((0,4,0,0,0)\) | \((5,31,0,0)\) |
| 2 | \((0,4,0,0,0)\) | \((4,32,0,0)\) |
| 3 | \((0,2,0,0,0)\) | \((2,29,0,0)\) |
| 4 | \((0,1,0,0,0)\) | \((1,36,0,0)\) |
| 5 | \((0,1,1,0,0)\) | \((2,36,0,0)\) |
| 6 | \((0,0,0,0,0)\) | \((1,28,0,0)\) |
| 7 | \((0,0,0,0,0)\) | \((1,25,0,0)\) |
| 8 | \((0,0,0,0,0)\) | \((0,21,0,0)\) |

Full support and balanced capacity are distinct targets: step 6 has no
missing colour at any depth but still has positive capacity energy.  The
successful route also makes several temporary energy increases.  This is
evidence for plateau routing or an absorber, not for scalar greedy descent.

## 8. Exact remaining switching statement

The balanced-eight-switch route to CRP is reduced to either of the following
theorem-level targets.

1. **Local-minimum theorem.**  Prove that every local minimum, under a
   suitable fixed or dynamically reweighted capacity potential, satisfies
   \(\sum_{q\le h}Q_q=o(W/(nh))\).
2. **Neutral-routing theorem.**  From every factor above that energy scale,
   use \(Q\)-neutral or bounded-uphill balanced switches to reach a factor
   admitting a strict net decrease, with the total excursion amortized.
3. **Larger-trade theorem.**  Compose balanced eight-switches into an
   endpoint-neutral trade whose linear load transport dominates its
   \(O(\sum q)\) quadratic toll.

Theorem 3.1 is the useful structural input for all three: a switch changes
only \(O(q)\) certified colours at depth \(q\), with an exact histogram and
an explicit quadratic toll.  The finite audit shows exactly what cannot be
used as the missing asymptotic argument.

## 9. Status

**Proved in this note**

* the radius-\(q\) middle-vertex colour formula;
* exact seam cancellation and the bound \(r_q\le8q\);
* the all-depth load and quadratic-energy update;
* the exact overflow formula and the energy-to-CRP pruning theorem;
* finite positive local minima for the natural strict-descent objectives.

**Still open**

No theorem bounds the energy of all balanced-switch local minima at the
scale (1.2), and no neutral-routing/absorber theorem is proved.  Consequently
CRP and \(\nu(k)\le(1+o(1))W(k)\) remain conditional.
