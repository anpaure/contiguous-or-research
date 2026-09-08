# Adjacent priority swaps form an exact low-run flag-balancing cube

Date: 2026-07-25

The first-avoided-pair construction is not a single clustered matching.  A
whole hypercube of clustered matchings is obtained by independently swapping
disjoint adjacent pairs in the priority order.  The affected lower-target
families are disjoint, so the complete multidepth load vector is affine in
the swap bits.  This gives a genuine vector-balancing object in which *every*
vertex is already an exact integral matching with the required run bound.

The remaining unproved estimate is now a concrete covariance bound for the
outer flags contributed by the swap families.

## 1. First-avoided matchings for arbitrary priorities

Fix disjoint coordinate pairs

\[
 P_1,P_2,\ldots,P_m
\]

and local exact row factors \(F_{P_j}\).  Given any priority permutation
\(\rho\) of these pairs, assign a lower target \(S\) to the first pair in
the \(\rho\)-order which it avoids, and take the corresponding token in that
local factor.

Exactly as in Theorem 5.1 of
`PAIR_OMISSION_TIGHT_ROW_MULTICOVER_20260725.md`, the resulting token set
\(M_\rho\)

1. saturates every rank-\((m-1)\) target exactly once;
2. has distinct rank-\(m\) owners, because the owner inherits the same first
   avoided pair;
3. is a union of physical tight-row runs; and
4. satisfies, uniformly in \(\rho\),

\[
 \boxed{
 J(M_\rho)=O\left(\frac{W\log^2m}{m}\right).}
\tag{1.1}
\]

The proof of the component bound depends only on the position of a pair in
the priority list, not its name.

## 2. One adjacent swap

Start with the identity priority.  Let

\[
 A=P_j,qquad B=P_{j+1}.
\]

Define

\[
 \mathcal D_j=left\{
 S\in\binom{[n]}{m-1}:
 S\cap P_h\ne\varnothing\ (h<j),\quad
 S\cap A=S\cap B=\varnothing
 \right\}.
\tag{2.1}
\]

### Lemma 2.1

Interchanging \(A,B\) changes the selected token exactly for the lower
targets in \(\mathcal D_j\).  Such a target moves from its token in \(F_A\)
to its token in \(F_B\).

### Proof

If a target has an avoided pair before position \(j\), its first avoided
pair is unchanged.  If it meets one of \(A,B\), their relative order is
irrelevant.  If it meets all earlier pairs and avoids both, the first avoided
pair changes from \(A\) to \(B\).  \(\square\)

Inside one row of \(F_A\), the affected starts are those meeting all earlier
pairs and also avoiding \(B\).  Each coordinate-membership indicator changes
twice around a cyclic interval row, so these starts have \(O(j)\) cyclic
components.  The same holds in \(F_B\).  Thus the swap is physically a
union of long row intervals whenever its affected mass is not concentrated
in short exceptional components.

## 3. Disjointness of all affected families

### Lemma 3.1

For \(j<k\),

\[
 \boxed{\mathcal D_j\cap\mathcal D_k=\varnothing.}
\tag{3.1}
\]

### Proof

Every member of \(\mathcal D_j\) avoids \(P_j\).  Since \(j<k\), every
member of \(\mathcal D_k\) is required to meet \(P_j\).  \(\square\)

Now take the disjoint adjacent transpositions

\[
 (P_1,P_2),(P_3,P_4),\ldots.
\tag{3.2}
\]

For \(j\in\{1,3,5,\ldots\}\), let a bit \(\epsilon_j\in\{0,1\}\)
decide whether that adjacent pair is swapped.  Because the transpositions
have disjoint positions, and because their affected target families are
disjoint, all choices commute.

Let \(M_\epsilon\) be the first-avoided matching for the resulting priority.
For each \(j\), let

\[
 \Delta_j=\mu(M_{\{j\}})-\mu(M_0)
\tag{3.3}
\]

be the complete weighted flag-load increment of the single swap.

### Theorem 3.2 (exact priority-swap cube)

For every bit vector \(\epsilon\),

\[
 \boxed{
 \mu(M_\epsilon)=\mu(M_0)+\sum_{j\text{ odd}}\epsilon_j\Delta_j.}
\tag{3.4}
\]

Every \(M_\epsilon\) is an exact lower-saturating, middle-simple token
matching, and every one satisfies the uniform run bound (1.1).

### Proof

By Lemma 2.1, swap \(j\) changes only tokens whose lower endpoint belongs
to \(\mathcal D_j\).  Lemma 3.1 makes these supports disjoint, so the token
changes and their flag-load increments add exactly.  Legality and the run
bound hold because the resulting state is itself a first-avoided matching
for a priority permutation.  \(\square\)

This is stronger than componentwise switching two fixed matchings: no
interface estimate is needed.  Low physical complexity is built into every
corner of the cube.

## 4. Exact random-sign identity

Put \(\sigma_j=2\epsilon_j-1\), and define the cube midpoint

\[
 \mu_c=\mu(M_0)+\frac12\sum_{j\text{ odd}}\Delta_j.
\tag{4.1}
\]

For independent uniform signs,

\[
 \mu(M_\epsilon)-\lambda
 =\mu_c-\lambda+\frac12\sum_j\sigma_j\Delta_j.
\]

Hence in the weighted flag Hilbert space,

\[
 \boxed{
 \mathbb E_\epsilon
 \|\mu(M_\epsilon)-\lambda\|_w^2
 =\|\mu_c-\lambda\|_w^2
 +\frac14\sum_{j\text{ odd}}\|\Delta_j\|_w^2.}
\tag{4.2}
\]

### Corollary 4.1

If

\[
 \|\mu_c-\lambda\|_w^2
 +\frac14\sum_j\|\Delta_j\|_w^2
 \le B+o(W),
\tag{4.3}
\]

where \(B\) is the exact integer-floor baseline, then some priority-swap
state has floor-corrected energy \(o(W)\) and run count \(o(W/H)\).  It
therefore gives the constant-one word through the clustered-token transfer.

This is a literal conditional-expectation theorem: expose the swap bits one
at a time, always choosing the value which does not increase the conditional
expected energy in (4.2).

## 5. What can be bounded unconditionally

The families \(\mathcal D_j\) are disjoint, so

\[
 \sum_{j\text{ odd}}|\mathcal D_j|\le |V_-|=O(W).
\tag{5.1}
\]

At the lower rank, a swap does not change the load at all.  At the middle
rank, the old and new token maps are each injective on \(\mathcal D_j\), so

\[
 \|\Delta_{j,0}\|_2^2\le2|\mathcal D_j|.
\tag{5.2}
\]

More generally, suppose that at signed depth \(q\), both the old and new
flag maps restricted to \(\mathcal D_j\) have maximum multiplicity
\(R_{j,q}\).  Then

\[
 \boxed{
 \|\Delta_{j,q}\|_2^2
 \le2R_{j,q}|\mathcal D_j|.}
\tag{5.3}
\]

Indeed, for a nonnegative integer load vector of mass \(D\) and maximum
entry \(R\), its squared norm is at most \(RD\); apply this to both sides.

For the first upper flag in one local factor, every occurrence of a fixed
rank-\((m+1)\) target uses two of its rank-\(m\) facets.  Distinct
occurrences use disjoint facets because the local factor partitions the
rank-\(m\) windows.  Therefore

\[
 R_{j,1}^+\le\left\lfloor\frac{m+1}{2}\right\rfloor.
\tag{5.4}
\]

This worst-case estimate is far too weak for (4.3); it permits a variance of
order \(mW\) already at the first upper flag.  The same-rank orbit codegree
estimate \(O(m^{-2})\) is an average statement over the symmetric row
multicover and does not imply a small \(R_{j,q}\) for the fixed factors used
by one priority cube.

## 6. Exact remaining covariance statement

The priority cube removes the run/interface obstruction completely.  The
remaining positive estimate is now:

\[
 \boxed{
 \|\mu_c-\lambda\|_w^2-B
 +\frac14\sum_{j\text{ odd}}\|\Delta_j\|_w^2
 =o(W).}
\tag{6.1}
\]

It may be attacked by choosing the local factors \(F_{P_j}\) jointly before
forming the cube.  Sufficient concrete conditions are:

1. the half-swapped midpoint is floor-balanced up to \(o(W)\); and
2. the affected-family flag maps have total weighted collision norm

\[
 \sum_{j,q}w_qR_{j,q}|\mathcal D_j|=o(W).
\tag{6.2}
\]

Neither condition follows from arbitrary exact local factors.  In
particular the first adjacent swap has \(\mathcal D_1\) of macroscopic size,
so a linear first-upper collision excess in either \(F_{P_1}\) or
\(F_{P_2}\) survives in (6.1).

Thus adjacent priority swaps do produce the requested long-block
interpolation exactly, but verifying their flag covariance still requires a
jointly near-rainbow choice of the local row factors.  No such all-depth
factor selection is proved here.

## 7. The natural pair-symmetric factor choice

There is one canonical way to make the two sides of a swap agree as much as
possible.  Let

\[
 R=[n]\setminus(A\cup B),
\]

let \(\tau\) interchange the two coordinate pairs \(A,B\) while fixing
\(R\), choose a factor \(F_A\) on \(R\cup B\), and put

\[
 F_B=\tau F_A.
\tag{7.1}
\]

Every affected lower target \(S\in\mathcal D_j\) lies in \(R\).  If its
old token and flags are denoted by

\[
 (S,Y,L_q,U_q),
\]

then its new data are exactly

\[
 (S,\tau Y,L_q,\tau U_q).
\tag{7.2}
\]

Here every lower flag is fixed because \(L_q\subseteq S\subseteq R\).
Only the upper flags can change, and an upper flag changes only if it uses a
coordinate of \(B\).

After averaging \(F_A\) over coordinate permutations of \(R\cup B\) which
preserve \(B\) setwise, the \(q+1\) coordinates in \(U_q\setminus S\) are
uniform among the \(m\) coordinates of \((R\cup B)\setminus S\).  Hence

\[
 \Pr(U_q\cap B\ne\varnothing)
 \le\frac{2(q+1)}m.
\tag{7.3}
\]

For the Gaussian overload weights \(w_q\ll e^{-q^2/m}\),

\[
 \sum_{q\le H}w_q\Pr(U_q\cap B\ne\varnothing)
 \le\frac{C}{m}\sum_{q\ge1}q e^{-q^2/m}
 =O(1).
\tag{7.4}
\]

Thus some pair-symmetric choice has only \(O(|\mathcal D_j|)\) total
*weighted changed occurrences*.  This is a genuine all-depth collar bound,
but it is not yet (6.1): aggregation of equal upper targets can enlarge the
squared norm, and even the unaggregated bound is only \(O(W)\), not
\(o(W)\), after summing the disjoint affected families.

The test therefore gives a sharp placement of the remaining saving.  Pair
symmetry removes every lower-flag increment and confines upper increments to
the two swapped coordinate pairs.  To finish, one still needs either

1. an extra little-oh cancellation among those coordinate-pair increments;
   or
2. an exact use of the integer-floor reservoir showing that the
   \(O(W)\) collar variance is already absorbed by the midpoint's deficit
   below the raw discrete baseline.

Neither assertion is established by the orbit average alone.

## 8. Exact floor-energy audit of the pair-symmetric cube

The floor-accounting question left at the end of Section 7 is resolved in
`PAIR_PRIORITY_SWAP_EXACT_FLOOR_ENERGY_AUDIT_20260725.md`.

For every upper depth, first-avoided targets split into disjoint families
belonging to the disjoint adjacent blocks.  Hence the upper collision
energy is a sum of one-bit orientation energies, with no cross-bit terms.
For the pair-symmetric choice (7.1), flipping a bit merely permutes the
affected upper load vector by the corresponding pair exchange.  Thus every
corner has exactly the same floor-corrected energy, separately at every
rank; all lower loads are unchanged.

Writing \(Q_q\) for doubled integer-floor excess and \(B_q\) for the raw
integer squared-distance floor, the exact identity is

\[
 \left\lVert\mu_{c,q}-\lambda_q\mathbf1\right\rVert_2^2-B_q
 =Q_q(M_0)-\frac14\sum_j\lVert\Delta_{j,q}\rVert_2^2.
\tag{8.1}
\]

So the sign variance is offset rank by rank by the half-integral midpoint
lying below the integer floor.  This is not a descent: the integral energy
is flat on the cube.  At the first upper rank,

\[
 B_1=\frac{2m}{(m+2)^2}W=O(W/m),
\tag{8.2}
\]

and therefore a genuine \(\Theta(W)\) aggregated increment variance would
force \(Q_1=\Theta(W)\).  The changed-occurrence bound (7.4) alone does not
imply such a load-vector variance, because occurrence changes may cancel
after aggregation.

Finally, the first adjacent block gives the sharp local limitation

\[
 \min_{\epsilon_1}\Phi_1^+(M_\epsilon)
 \ge \min\{C_1(F_A),C_1(F_B)\},
\tag{8.3}
\]

where \(C_1(F_P)\) is the complete length-\((m+1)\) collision count of the
local factor.  Thus the cube still requires a locally near-rainbow exact
factor; it cannot create one by choosing swap signs.
