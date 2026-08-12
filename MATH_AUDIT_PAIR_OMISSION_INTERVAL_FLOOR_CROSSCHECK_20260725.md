# Cross-audit of the adjacent pair-omission interval chart

Date: 2026-07-25

Method: pure mathematics only.  No computation or search is used.

## 1. Verdict and scope

The interval theorem in
`MATH_AUDIT_PAIR_OMISSION_INTERVAL_CORNERS_AND_FLOOR_DESCENT_20260725.md`
is correct, with the following hypotheses kept explicit:

* this is one adjacent chart, with (A=P_j,B=P_{j+1});
* the local factors are conjugate, (F_B=\theta F_A), where
  (\theta=(a_1\ b_1)(a_2\ b_2)) exchanges (A) and (B);
* upper depths obey (1\le q\le H\le m-2);
* the energy is the doubled integral factorial-floor excess, with finite
  nonnegative signed-depth weights.

Under these hypotheses every independent maximal-interval corner is a
genuine lower-saturating, middle-injective matching, including its common
background.  The two coherent endpoints are energy-equal at every signed
rank.  If (A_j,V_j) are the coherent square and independent-interval
variance, then

\[
 A_j-V_j=4\mathcal C_j,
\]

and fair interval rounding has the exact floor-corrected expectation

\[
 \mathbb E Q_w=Q_w(M^-)-\mathcal C_j.
\]

This remains valid at the first upper rank, where (c_1^+=0).  The only
notational amendment needed in the source proof is that the signs in its
display (6.3) are Rademacher signs (\eta_I\in\{-1,+1\}), not zero-one
bits.  No mathematical factor changes.

## 2. Legality of every independent choice

Let

\[
 \mathcal D_j=\left\{S\in{[n]\choose m-1}:S\cap(A\cup B)=\varnothing,
 \quad S\cap P_h\ne\varnothing\ (h<j)\right\}.
\]

For (S\in\mathcal D_j), write (e_A(S),e_B(S)) for its two tokens and
(Y_A(S),Y_B(S)) for their middle owners.  Since (S) is fixed pointwise
by (\theta) and (F_B=\theta F_A),

\[
 e_B(S)=\theta e_A(S),\qquad Y_B(S)=\theta Y_A(S).                 \tag{2.1}
\]

In fact an arbitrary tokenwise choice, not merely an interval-correlated
choice, is legal.  Lower saturation is immediate.  For middle injectivity,
same-side collisions are impossible because the rank-(m) windows of one
exact factor are all distinct.  For a mixed collision, suppose

\[
 Y_A(S)=Y_B(T)=\theta Y_A(T).                                    \tag{2.2}
\]

The common set avoids (A), because it is an (F_A)-owner, and avoids
(B), because it is an (F_B)-owner.  It is therefore fixed by (\theta).
Applying (\theta) in (2.2) gives (Y_A(S)=Y_A(T)), whence (S=T) by
injectivity in (F_A).  A corner chooses only one of the two tokens over
that lower vertex, so this is not a collision.

It remains to include the background, which cannot be omitted from this
argument.  All tokens outside (\mathcal D_j) are identical in (M^-)
and (M^+).  An (A)-choice and every background token coexist in the
matching (M^-), while a (B)-choice and every background token coexist
in (M^+).  Thus no changed token collides with the background; background
owners are mutually distinct in either endpoint.  This proves the full
matching assertion.

## 3. Coherent endpoint flatness, rank by rank

Every lower flag of a changed token is a subset of (S), hence is fixed
by (\theta).  Thus the two lower load vectors are identical.  All middle
loads are zero-one by Section 2, so their factorial excess is zero.

For an upper depth (q), a token assigned to a first-avoided pair (P)
has (S\subseteq U_q\subseteq[n]\setminus P).  Hence (U_q) meets all
earlier pairs and avoids (P): it has the same first-avoided category.
Consequently the (A/B) upper coordinates form the invariant stratum

\[
 \mathcal U_{j,q}=\{U:U\text{ meets every }P_h\ (h<j),
                    \ U\text{ avoids }A\text{ or }B\}.            \tag{3.1}
\]

There is no contribution to this stratum from any other phase.  On
(\mathcal U_{j,q}), conjugacy of the factors gives

\[
 \mu_q^+(M^+;U)=\mu_q^+(M^-;\theta^{-1}U).                         \tag{3.2}
\]

Outside this stratum the endpoint loads are identical.  Hence the upper
load vectors have equal collision sums, and, since their total masses and
target-rank sizes agree, equal integral floor excess.  This proves exact
endpoint equality separately at every signed rank.  It is precisely the
global pair-symmetric flatness identity; a mixed interval corner is not a
single (\theta)-image of (M^-), so (3.2) does not assert flatness for
mixed corners.

## 4. The joined Gram and its factor (4)

For a changed (S), let (U_q(S)) be its phase-(A) upper flag and set

\[
 d_S=\phi(e_B(S))-\phi(e_A(S)).
\]

All lower coordinates of (d_S) vanish, and its upper depth-(q) part is

\[
 (d_S)_q^+=\delta_{\theta U_q(S)}-\delta_{U_q(S)}.                 \tag{4.1}
\]

If (U,V\subseteq[n]\setminus A), then

\[
 \begin{aligned}
 \langle\delta_{\theta U}-\delta_U,
          \delta_{\theta V}-\delta_V\rangle
 &=2\mathbf1_{\{U=V\}}-2\mathbf1_{\{\theta U=V\}}\\
 &=2\mathbf1_{\{U=V,\ U\cap B\ne\varnothing\}}.               \tag{4.2}
 \end{aligned}
\]

Indeed, (\theta U=V), with both (U,V) avoiding (A), forces the
common set to avoid (A\cup B), hence to be fixed by (\theta); this is
exactly the cancelling case (U=V) avoiding (B).  Therefore

\[
 \langle d_S,d_T\rangle_w
 =2\sum_{q=1}^H w_q^+
   \mathbf1_{\{U_q(S)=U_q(T),\ U_q(S)\cap B\ne\varnothing\}}.     \tag{4.3}
\]

For (q\le m-2), the flag length (m+q) is strictly smaller than the
row length (2m-1).  Distinct starts in one row give distinct proper
cyclic windows.  Thus innovations in one maximal carrier interval are
orthogonal.  If (z_I=\sum_{S\in I}d_S), and

\[
 \mu_{q,U}=|\{S\in\mathcal D_j:U_q(S)=U\}|,
\]

then

\[
 \begin{aligned}
 A_j:=\left\|\sum_Iz_I\right\|_w^2
   &=2\sum_{q,U:\,U\cap B\ne\varnothing}w_q^+\mu_{q,U}^2,\\
 V_j:=\sum_I\|z_I\|_w^2
   &=2\sum_{q,U:\,U\cap B\ne\varnothing}w_q^+\mu_{q,U}.
                                                                    \tag{4.4}
 \end{aligned}
\]

It follows, with no asymptotic loss, that

\[
 A_j-V_j
 =2\sum_{q,U}w_q^+\mu_{q,U}(\mu_{q,U}-1)
 =4\sum_{q,U}w_q^+{\mu_{q,U}\choose2}
 =4\mathcal C_j.                                                    \tag{4.5}
\]

The restriction (q\le m-2) is used exactly once: it rules out a repeated
full cyclic window inside one physical interval.

## 5. Exact floor descent, including (c_1^+=0)

At one rank let (K) be the number of targets and (T=cK+\delta),
(0\le\delta<K), the common mass of every corner.  Put

\[
 \lambda=T/K,\qquad B=\delta(K-\delta)/K,
\]

and for an integral load vector (x) define the doubled floor excess

\[
 Q(x)=\|x-\lambda\mathbf1\|_2^2-B
     =\sum_Z(x_Z-c)(x_Z-c-1).                                     \tag{5.1}
\]

Let (x^-,x^+) be the coherent endpoint vectors, let
(\bar x=(x^-+x^+)/2), and use independent Rademacher signs
(\eta_I\in\{-1,+1\}):

\[
 x_\eta=\bar x+\frac12\sum_I\eta_Iz_I.                            \tag{5.2}
\]

Then

\[
 \mathbb E Q(x_\eta)=\|\bar x-\lambda\mathbf1\|_2^2-B+\frac14V_j,
                                                                    \tag{5.3}
\]

whereas the average of the endpoint energies is

\[
 \frac{Q(x^-)+Q(x^+)}2
 =\|\bar x-\lambda\mathbf1\|_2^2-B+\frac14A_j.                   \tag{5.4}
\]

Endpoint equality from Section 3 and (4.5) therefore give

\[
 \mathbb E Q_w(M_\eta)
 =Q_w(M^-)-\frac{A_j-V_j}{4}
 =Q_w(M^-)-\mathcal C_j.                                          \tag{5.5}
\]

This calculation never divides by (c).  At the first upper rank,

\[
 K=W,\qquad T={m\over m+2}W,
 \qquad c_1^+=0,
 \qquad B_1={2m\over(m+2)^2}W,                                   \tag{5.6}
\]

and hence (Q_1^+(x)=\sum_Ux_U(x_U-1)).  Formula (5.5) is unchanged.
Thus the guaranteed descent in doubled energy is exactly
(\mathcal C_j), not (2\mathcal C_j); in the undoubled factorial
excess it is (\mathcal C_j/2).

## 6. Interval and run accounting

In an (F_A)-row, membership in (\mathcal D_j) is the intersection of
(j) predicates: avoidance of (B), and meeting each (P_h), (h<j).
For either membership predicate associated with one coordinate pair, the
set of cyclic starts has at most two components and at most four boundary
edges.  Boundaries of an intersection lie in the union of the individual
boundaries.  Thus one row has at most (2j) maximal carrier intervals.

The exact number of rows in one local factor is

\[
 R_m={1\over2m-1}{2m-1\choose m-1}=\operatorname {Cat}_{m-1},
\]

so, if (r_j) is the total number of interval bits,

\[
 r_j\le\min\{2jR_m,|\mathcal D_j|\}.                               \tag{6.1}
\]

Changing one interval removes one contiguous selected interval from its
(F_A)-row and inserts its conjugate interval into an (F_B)-row.  Each
operation changes the cyclic run count upward by at most one.  Summing over
bits gives the deterministic bound

\[
 J(M_\eta)-J(M^-)\le2r_j.                                         \tag{6.2}
\]

With (W={2m+1\choose m}), the exact ratio is

\[
 {R_m\over W}={m(m+1)\over(2m-1)(2m)(2m+1)}.                      \tag{6.3}
\]

For uniformity in (j), let (N_j) be the number of category-(j)
lower sets.  Independent Bernoulli sampling on the (2m-1) coordinates
of (Q_j), with (p=(m-1)/(2m-1)), followed by conditioning on size
(m-1), gives

\[
 N_j\le C\sqrt m{2m-1\choose m-1}(3/4)^{j-1}.                     \tag{6.4}
\]

Indeed the earlier-pair events are independent before conditioning, each
has probability (1-(1-p)^2<3/4), and the conditioning event has
probability at least (c/\sqrt m).  Since
(\mathcal D_j\subseteq\{\kappa=j\}), (6.1) and (6.4), split at
(j=\lceil20\log m\rceil), imply

\[
 r_j=O(W\log m/m)                                                   \tag{6.5}
\]

uniformly in (j).  Therefore the added run count is
(O(W\log m/m)).  Combining this with
(J(M^-)=O(W\log^2m/m)) gives

\[
 J(M_\eta)=o(W/H)\qquad\text{whenever}\qquad
 H=o(m/\log^2m).                                                    \tag{6.6}
\]

Finally, the number of selected tokens is
(T={2m+1\choose m-1}=mW/(m+2)), and at most one selected token per run
has an absent physical predecessor.  Hence

\[
 \Pr(\text{predecessor selected}\mid\text{token selected})
 \ge1-{J(M_\eta)\over T}=1-o(1/H).                                \tag{6.7}
\]

All constants in (6.4)--(6.7) are absolute.  No constant-one theorem is
deduced: the chart has zero lower innovation and no upper innovation on
targets avoiding (B), so charged all-sector coverage and compatibility
of several adjacent charts remain separate open statements.
