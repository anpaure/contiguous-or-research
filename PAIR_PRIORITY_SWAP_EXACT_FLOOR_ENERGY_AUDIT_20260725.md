# Exact floor energy of the adjacent-priority swap cube

Date: 2026-07-25

This note audits the unresolved covariance term in
`PAIR_PRIORITY_ADJACENT_SWAP_CUBE_20260725.md`.  There are two distinct
facts.

1.  For arbitrary local factors, the upper-flag collision energy of the
    cube is a sum of independent **one-bit orientation energies**.  There
    are no cross-bit quadratic terms to exploit.
2.  For the natural pair-symmetric choice of local factors, every corner of
    the cube has exactly the same floor-corrected energy, separately at
    every rank.  The sign variance is cancelled exactly by the fractional
    midpoint's deficit below the integer floor.  It neither creates a new
    obstruction nor produces any descent.

Thus the (O(W)) upper-flag increment bound is not by itself an
Ω\((W)\) energy defect.  A genuine defect is exactly the collision excess
of the integral corners.  The cube can orient pre-existing local factors,
but cannot average a bad pair-symmetric factor into a good one.

## 1. The exact integer floor

Fix one target rank \(\mathcal T\), of size \(K\), and let every cube
corner have total flag mass \(T\).  Write

\[
 T=cK+\delta,\qquad 0\leq\delta<K.
\tag{1.1}
\]

For a load vector \(x\in\mathbb Z_{\geq0}^{\mathcal T}\) of mass \(T\),
put

\[
 P(x)=\sum_{Z\in\mathcal T}\binom{x_Z}{2}
\tag{1.2}
\]

and

\[
 P^{\min}=(K-\delta)\binom c2+
                 \delta\binom{c+1}{2}.
\tag{1.3}
\]

The factorial floor excess is

\[
 \Phi(x)=P(x)-P^{\min}\geq0.
\tag{1.4}
\]

Equivalently, if \(\lambda=T/K\) and

\[
 B=\frac{\delta(K-\delta)}K,
\tag{1.5}
\]

then the doubled floor excess is

\[
 \boxed{
  2\Phi(x)
  =\sum_Z(x_Z-c)(x_Z-c-1)
  =\lVert x-\lambda\mathbf1\rVert_2^2-B.}
\tag{1.6}
\]

Now let

\[
 x_\epsilon=x_0+\sum_{j=1}^s\epsilon_j\Delta_j,
 \qquad \epsilon_j\in\{0,1\},
\tag{1.7}
\]

and write

\[
 \bar x=x_0+\frac12\sum_j\Delta_j.
\tag{1.8}
\]

Independent fair bits give the exact identities

\[
 \boxed{
 \mathbb E P(x_\epsilon)
 =P(\bar x)+\frac18\sum_j\lVert\Delta_j\rVert_2^2,}
\tag{1.9}
\]

and

\[
 \boxed{
 \mathbb E[2\Phi(x_\epsilon)]
 =\lVert\bar x-\lambda\mathbf1\rVert_2^2-B
   +\frac14\sum_j\lVert\Delta_j\rVert_2^2.}
\tag{1.10}
\]

The first term on the right of (1.10) need not be nonnegative: \(\bar x\)
is generally half-integral, whereas \(B\) is the minimum only over integer
load vectors.  This is the exact place where a large sign variance may be
cancelled.

## 2. First-avoided strata make the upper energy block diagonal

Fix a priority order of the disjoint coordinate pairs.  If a token with
lower endpoint \(S\) is assigned to the first pair \(P\) avoided by \(S\),
then every upper flag \(U_q\) of this token satisfies

\[
 S\subseteq U_q\subseteq[n]\setminus P.
\tag{2.1}
\]

It therefore avoids \(P\), while it meets every earlier pair because \(S\)
does.  Consequently

\[
 \boxed{P\text{ is also the first priority pair avoided by }U_q.}
\tag{2.2}
\]

Consider one swappable adjacent block \((A,B)\) at positions \(j,j+1\).
For the rank of \(U_q\), define

\[
 \mathcal U_{j,q}=\left\{U:
 \begin{array}{l}
 U\text{ meets every pair before position }j,\\
 U\text{ avoids at least one of }A,B
 \end{array}\right\}.
\tag{2.3}
\]

This family is independent of the orientation of \((A,B)\).  Moreover,
for distinct disjoint adjacent blocks,

\[
 \boxed{\mathcal U_{j,q}\cap\mathcal U_{k,q}=\varnothing.}
\tag{2.4}
\]

Indeed, a member of the earlier family avoids one pair in that block,
whereas membership in a later family requires meeting every earlier pair.

By (2.2), flipping bit \(j\) changes the upper load only on
\(\mathcal U_{j,q}\).  Hence the upper increments \(\Delta_{j,q}^+\) have
pairwise disjoint coordinate supports.  More strongly, if
\(P_{j,q}^{0}\) and \(P_{j,q}^{1}\) denote the collision sums contributed
on \(\mathcal U_{j,q}\) by the two orientations, then

\[
 \boxed{
 P_q^+(\epsilon)
 =P_{q,\mathrm{fixed}}^+
  +\sum_j P_{j,q}^{\epsilon_j}.}
\tag{2.5}
\]

For arbitrary nonnegative rank weights \(w_q\), put

\[
 E_j^b=\sum_qw_qP_{j,q}^b.
\tag{2.6}
\]

The best corner of the cube is therefore known exactly:

\[
 \boxed{
 \min_\epsilon\sum_qw_qP_q^+(\epsilon)
 =\sum_qw_qP_{q,\mathrm{fixed}}^+
  +\sum_j\min(E_j^0,E_j^1).}
\tag{2.7}
\]

Equivalently, its improvement below the fair average is only

\[
 \frac12\sum_j|E_j^0-E_j^1|.
\tag{2.8}
\]

There is no high-dimensional vector-balancing cancellation left in the
upper flags: each bit merely chooses the cheaper of two local orientations.

## 3. Pair-symmetric factors make the cube exactly energy-flat

Let \(\tau_j\) exchange the two coordinate pairs \(A,B\) and fix every
other coordinate.  Choose

\[
 F_B=\tau_jF_A
\tag{3.1}
\]

for every disjoint adjacent block.  The choices can be made independently
because the blocks use disjoint pair names.

### Theorem 3.1 (rankwise energy-flatness)

For the pair-symmetric choice (3.1), every corner of the priority-swap cube
has exactly the same factorial floor excess at every upper rank.  The lower
flag load vectors are identical at every corner.  The middle-owner load is
injective at every corner and hence also has identical zero factorial
excess.

#### Proof

Fix all bits except bit \(j\).  Coordinate exchange \(\tau_j\) maps the
family of lower targets whose first avoided pair is \(A\) or \(B\) in the
first orientation bijectively onto the corresponding family in the second
orientation.  It also maps the selected token in \(F_A\) or \(F_B\), and
all of its flags, onto the selected token and flags in the other
orientation.  Therefore, on the invariant target family
\(\mathcal U_{j,q}\),

\[
 \mu_{q,j}^{+,1}(U)=
 \mu_{q,j}^{+,0}(\tau_j^{-1}U).
\tag{3.2}
\]

The collision sum is invariant under a permutation of target coordinates,
so

\[
 P_{j,q}^1=P_{j,q}^0.
\tag{3.3}
\]

Equation (2.5) proves upper-rank energy invariance under this bit, hence
under every bit.

Only targets \(S\) avoiding both \(A,B\) actually change their selected
token.  Such an \(S\) lies in the pointwise fixed complement of
\(A\cup B\).  Its new lower flag is the \(\tau_j\)-image of its old lower
flag, but that flag is a subset of \(S\), and is therefore fixed pointwise.
Thus every lower load vector is unchanged.  Middle owners remain distinct
by the token-matching theorem, so their collision sum is zero throughout.
\(\square\)

Let \(Q_q=2\Phi_q\) be the doubled floor energy at one upper rank.  Theorem
3.1 and (1.10) give the exact cancellation identity

\[
 \boxed{
 \lVert\bar\mu_q-\lambda_q\mathbf1\rVert_2^2-B_q
 =Q_q(M_0)-\frac14\sum_j
             \lVert\Delta_{j,q}^+\rVert_2^2.}
\tag{3.4}
\]

Thus the entire sign variance is offset **at the same rank** by the
half-integral midpoint lying below the integer floor.  There is no
cancellation between lower and upper ranks, or between different depths.

This also yields the sharp dichotomy

\[
 \boxed{
 \frac14\sum_j\lVert\Delta_{j,q}^+\rVert_2^2
 \le Q_q(M_0)+B_q.}
\tag{3.5}
\]

If \(B_q=o(W)\) and the aggregated sign variance is \(\Omega(W)\), then
the integral corners really do have \(Q_q=\Omega(W)\).  If the corners are
floor-balanced, the variance is automatically at most the integer-floor
reservoir \(B_q\).  Merely counting changed token occurrences cannot decide
which case holds, because many changed occurrences may cancel in the
aggregated load vector.

At the first upper rank, the target count is \(K=W\), the mass is
\(T=N_1=mW/(m+2)\), and

\[
 B_1=T\left(1-\frac TK\right)
    =\frac{2m}{(m+2)^2}W=O(W/m).
\tag{3.6}
\]

Therefore a genuine \(\Theta(W)\) first-upper load-increment variance
cannot be hidden by the floor: (3.5) would force \(\Theta(W)\) collision
excess.  On the other hand, the orbit collar estimate in the source note
bounds changed *occurrences*, not the squared norm of the aggregated load
increment, so it does not establish such a lower bound.

## 4. Sharp limitation at the first adjacent block

For a local factor \(F_P\), let

\[
 C_1(F_P)=\sum_U\binom{\nu_{F_P}(U)}2
\tag{4.1}
\]

be the collision count of all its length-\((m+1)\) flags.  In a priority
whose first pair is \(A\), every lower target in the local universe
\([n]\setminus A\) is assigned to \(A\).  By (2.2), all of their upper
flags lie in the first-avoided-\(A\) stratum, disjoint from every later
phase.  Hence

\[
 \boxed{
 \Phi_1^+(A,B,\ldots)\ge C_1(F_A),\qquad
 \Phi_1^+(B,A,\ldots)\ge C_1(F_B).}
\tag{4.2}
\]

It follows that even after the optimal first swap,

\[
 \boxed{
 \min_{\epsilon_1}\Phi_1^+(M_\epsilon)
 \ge\min\{C_1(F_A),C_1(F_B)\}.}
\tag{4.3}
\]

For the symmetric pairing, the two local collision counts are equal, and
the cube cannot decrease them at all.  Thus an \(o(W)\) first-upper result
from this architecture already requires a local exact factor on
\(2m-1\) coordinates with

\[
 C_1(F_P)=o(W).
\tag{4.4}
\]

The arithmetic minimum of \(C_1(F_P)\) is only \(O(W/m)\), so (4.4) is not
numerically impossible.  It is, however, precisely a local near-rainbow
shadow theorem; the priority cube does not prove it.

## 5. Verdict

The exact answer to the covariance question is:

* the apparent sign variance is **not automatically a genuine excess**;
* under pair-symmetric factor pairing it is cancelled exactly, rank by
  rank, by the fractional midpoint's deficit below the integer floor;
* it does **not** cancel across signed ranks;
* this cancellation gives no improvement, because the integral energy is
  constant on the entire cube;
* for arbitrary factor pairing the cube has the exact separable optimum
  (2.7), so it performs only independent orientation choices;
* if the aggregated first-upper variance is genuinely \(\Omega(W)\), the
  small first-upper floor (3.6) forces a genuine \(\Omega(W)\) collision
  excess;
* obtaining \(o(W)\) therefore still requires a locally near-rainbow factor
  (and its multidepth analogue), not a better choice of swap signs.

This closes the floor-accounting ambiguity in (6.1) of the source note,
but does not prove the missing local near-rainbow factor theorem.

### Scope clarification: global bits versus interval bits

The flatness theorem above concerns one coherent bit for the whole
adjacent-pair stratum.  It does not apply after that bit is refined into
independent maximal physical-interval bits.  In the conjugate-factor atlas
of
`MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`,
every refined corner is still a genuine matching, but a mixed corner is no
longer the image of an endpoint under one global coordinate permutation.
If the interval innovations are (z_I), the global bit has variance

\[
 \left\|\sum_Iz_I\right\|^2,
\]

so its Haar gap is zero, whereas independent interval bits have variance
\(\sum_I\|z_I\|^2\).  Their difference is the explicit nonnegative
cross-interval duplicate census.  Thus global rankwise flatness and refined
interval descent are compatible statements.
