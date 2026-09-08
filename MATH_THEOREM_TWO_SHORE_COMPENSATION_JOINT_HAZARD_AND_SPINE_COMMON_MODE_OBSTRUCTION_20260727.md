# Two-shore compensation, exact joint hazards, and the surviving spine common mode

Date: 2026-07-27

Scope: the vertex-induced compensated repaired-ring process.  This note
tests whether retaining the lower/upper shore and gap state can cancel
the post-collar (+1) profile shift.

## 0. Verdict

Compensation cancels marginal degree disparity, but it does **not**
cancel the profile common-event (+1) term.  For a protected profile
(S) and the unprotected part (T) of one row, the exact nonterminal
hazard is

\[
 \boxed{
 \Lambda_S(T)={|T|\over r}
 -\nu\bigl(J(S\cup T)-J(S)\bigr).}
 \tag{0.1}
\]

The correction has the literal positive decomposition

\[
 \boxed{
 J(S\cup T)-J(S)
 =\sum_{e:e\cap S\ne\varnothing}|e\cap T|
 +\sum_{e:e\cap S=\varnothing}(|e\cap T|-1)_+.}
 \tag{0.2}
\]

The first sum is exactly a one-new-resource term.  After reversing the
row sum it is

\[
 \boxed{
 \mathcal B_1(S)=
 \sum_{y\notin S}a_S(y)d(S\cup\{y\}),
 \qquad
 a_S(y)=|\{e:y\in e, e\cap S\ne\varnothing\}|.}
 \tag{0.3}
\]

Thus the compensated stopped generator still raises profile order by
one.  The second sum in (0.2), but not the first, starts with two new
resources.

If (S=C\dot\cup P\dot\cup Q), where (P,Q) are its two shore
increments and (C) is the common core, then

\[
 a_{P,Q\mid C}(y):=
 |\mathcal E(y)\cap
   (\mathcal E(P)\setminus\mathcal E(C))\cap
   (\mathcal E(Q)\setminus\mathcal E(C))|,
 \tag{0.3a}
\]

\[
 a_{C\cup P\cup Q}(y)
 =a_{C\cup P}(y)+a_{C\cup Q}(y)-a_C(y)-a_{P,Q\mid C}(y),
 \tag{0.4}
\]

with a nonnegative shared-event term (a_{P,Q\mid C}).  Equivalently,
conditional on protecting (C),

\[
 \boxed{
 \Lambda_C(P\cup Q)
 =\Lambda_C(P)+\Lambda_C(Q)
 -\nu I_C(P,Q),\qquad I_C(P,Q)\ge0.}
 \tag{0.5}
\]

Hence the gap state controls the size of a **positive correlation**;
it never supplies a negative compensator.  On a one-sided state
(Q=\varnothing), the purported compensation term is identically zero.

For the exact post-collar consecutive spine, resolving every shore,
orientation, coordinate and gap label gives a nonnegative child matrix
(K_k) whose row sum is

\[
 \boxed{
 K_k\mathbf 1=c_k\mathbf1,qquad
 c_k={r-k-1\over r-k},qquad H\le k<m.}
 \tag{0.6}
\]

In particular (c_k\ge1/3) in the audited range.  The symmetric
two-shore common mode therefore contains the same order-one spine
eigenmode as the scalar hierarchy.  The antisymmetric mode can cancel
under reversal, but it does not dominate the nonnegative common mass
which must be controlled.

The exact carré-du-champ identity reaches the same conclusion.  If
(Z_+,Z_-) are the two shore observables and
(Z_c=Z_++Z_-), (Z_d=Z_+-Z_-), then

\[
 \boxed{
 \Gamma(Z_c)=\Gamma_{++}+\Gamma_{--}+2\Gamma_{+-},
 \qquad
 \Gamma(Z_d)=\Gamma_{++}+\Gamma_{--}-2\Gamma_{+-},}
 \tag{0.7}
\]

where (Gamma_{+-}\ge0), and hence

\[
 \Gamma(Z_c)+\Gamma(Z_d)
 =2(\Gamma_{++}+\Gamma_{--}).
 \tag{0.8}
\]

Correlation can reduce the difference mode only by increasing the
common mode.  Consequently no positive two-shore/gap energy which is
uniformly coercive on common mass removes the (+1) spine shift by
shore cancellation.  A successful
argument must instead exploit terminal-kill incidence globally, use a
trajectory-specific cutoff, or introduce a state variable beyond the
two shore/gap profile.

## 1. Exact compensated joint hazard

Let (mathcal H_t) be an active hypergraph.  Every active edge has
clock rate

\[
 \nu={1\over r\Delta},
 \tag{1.1}
\]

and an active resource (y) has compensation rate

\[
 \chi(y)={\Delta-d(y)\over r\Delta}
 ={1\over r}-\nu d(y).
 \tag{1.2}
\]

For a resource set (A), write

\[
 \mathcal E(A)=\{e:e\cap A\ne\varnothing\},
 \qquad
 J(A)=\sum_{y\in A}d(y)-|\mathcal E(A)|.
 \tag{1.3}
\]

The rate of an event deleting at least one member of (A) is exactly

\[
 \begin{aligned}
 \Lambda(A)
 &=\nu|\mathcal E(A)|+\sum_{y\in A}\chi(y)\\
 &={|A|\over r}-\nu J(A).
 \end{aligned}
 \tag{1.4}
\]

This is the marginal compensation identity.

Now fix a protected set (S), and let (T\cap S=\varnothing).  In the
stopped link, events meeting (S) are terminal and favorable.  The
nonterminal rate at which an event deletes at least one member of (T)
while avoiding (S) is

\[
 \Lambda_S(T)
 =\nu|\mathcal E(T)\setminus\mathcal E(S)|
 +\sum_{y\in T}\chi(y).
 \tag{1.5}
\]

Since

\[
 |\mathcal E(S\cup T)|-|\mathcal E(S)|
 =|\mathcal E(T)\setminus\mathcal E(S)|,
 \tag{1.6}
\]

substitution of (1.2) proves (0.1).

For completeness, the full generator, including death of (S), is
consistent with this identity.  The terminal hazard is

\[
 \Lambda(S)={|S|\over r}-\nu J(S),
 \tag{1.7}
\]

so for a row (f=S\dot\cup T),

\[
 \Lambda_S(T)+\Lambda(S)
 ={ |f|\over r}-\nu J(f)=\Lambda(f).
 \tag{1.8}
\]

Thus no term has been lost: the (+1) term below is precisely the
conditional-survival correction left after terminal events are treated
as favorable.

## 2. Literal signed decomposition and the (+1) child

The excess has the per-edge representation

\[
 J(A)=\sum_e(|e\cap A|-1)_+.
 \tag{2.1}
\]

For one edge (e), put (a=|e\cap S|) and (b=|e\cap T|).  If
(a\ge1), then

\[
 (a+b-1)_+-(a-1)_+=b;
 \tag{2.2}
\]

if (a=0), the difference is ((b-1)_+).  Summation proves (0.2).

Let

\[
 \mathcal F_S=\{f:S\subseteq f\},
 \qquad N_S=|\mathcal F_S|=d(S).
 \tag{2.3}
\]

All rows have the same size, say (K).  The nonterminal stopped
generator is therefore

\[
 \boxed{
 \mathcal L^{\rm nt}N_S
 =-{K-|S|\over r}N_S
 +\nu\sum_{f\in\mathcal F_S}
       \bigl(J(f)-J(S)\bigr).}
 \tag{2.4}
\]

The first sum in (0.2), reversed over the new resource (y), is

\[
 \begin{aligned}
 \sum_{f\in\mathcal F_S}
 \sum_{e:e\cap S\ne\varnothing}|e\cap(f\setminus S)|
 &=\sum_{y\notin S}
   |\{e:y\in e, e\cap S\ne\varnothing\}|
   |\{f:S\cup\{y\}\subseteq f\}|\\
 &=\sum_{y\notin S}a_S(y)d(S\cup\{y\}),
 \end{aligned}
 \tag{2.5}
\]

which is (0.3).  Every coefficient in (2.5) is nonnegative.  Moreover,

Here (a_S(y)) is an active-event count, while
(d(S\cup\{y\})) is an active-row count.  Their product counts ordered
triples ((e,f,y)), and (e=f) is allowed.  The multiplicity
(|e\cap T|) in (0.2) is intentional: for an edge already meeting
(S), each further resource (y\in e\cap T) contributes one to
(J(S\cup T)-J(S)).  Thus (2.5) is an equality, not a union bound.

Moreover,

\[
 a_S(y)\ge d(S\cup\{y\}),
 \tag{2.6}
\]

because every edge containing (S\cup\{y\}) is counted by (a_S(y)).
Thus even the diagonal (e=f) is a genuine positive one-child source.

The second term in (0.2) is

\[
 \mathcal B_{\ge2}(S)=
 \sum_{f\in\mathcal F_S}
 \sum_{e:e\cap S=\varnothing}
 (|e\cap(f\setminus S)|-1)_+.
 \tag{2.7}
\]

Every nonzero summand in (2.7) displays at least two resources of
(f\setminus S).  Hence the exact compensated generator splits into a
(+1) protected-common-event branch (2.5) and a (+2)-or-higher
external branch (2.7).  Marginal compensation removes neither (2.5)
nor its diagonal.

## 3. Two shores and the gap-dependent correlation

Let a common protected core (C) be fixed, and let (P,Q) be disjoint
shore increments, also disjoint from (C).  Define the conditional
edge families

\[
 \mathcal E_C(P)=\mathcal E(P)\setminus\mathcal E(C),
 \qquad
 \mathcal E_C(Q)=\mathcal E(Q)\setminus\mathcal E(C),
 \tag{3.1}
\]

and

\[
 I_C(P,Q)=|\mathcal E_C(P)\cap\mathcal E_C(Q)|.
 \tag{3.2}
\]

For (A=P,Q,P\cup Q), write

\[
 \Lambda_C(A)=\nu|\mathcal E(A)\setminus\mathcal E(C)|
 +\sum_{y\in A}\chi(y).
 \tag{3.2a}
\]

Coin hazards are additive on the disjoint sets (P,Q), while selected
edge hazards obey inclusion--exclusion.  Therefore

\[
 \begin{aligned}
 \Lambda_C(P\cup Q)
 &=\nu|\mathcal E_C(P)\cup\mathcal E_C(Q)|
   +\sum_{y\in P\cup Q}\chi(y)\\
 &=\Lambda_C(P)+\Lambda_C(Q)-\nu I_C(P,Q),
 \end{aligned}
 \tag{3.3}
\]

which proves (0.5).  The only gap-dependent term has the sign
(-I_C(P,Q)) in the deletion hazard, hence the sign (+I_C(P,Q)) in
the normalized survival drift.  When the two shores are far enough
that they have no common event, it is zero.  When they share events, it
makes their survival more positively correlated.

The same conclusion is visible directly in the (+1) coefficient.
Put

\[
 a_A(y)=|\mathcal E(y)\cap\mathcal E(A)|.
 \tag{3.4}
\]

For (S=S_+\cup S_-), inclusion--exclusion gives

\[
 a_S(y)=a_{S_+}(y)+a_{S_-}(y)
 -|\mathcal E(y)\cap\mathcal E(S_+)\cap\mathcal E(S_-)|.
 \tag{3.5}
\]

In particular,

\[
 \boxed{a_S(y)\ge\max\{a_{S_+}(y),a_{S_-}(y)\}.}
 \tag{3.6}
\]

The negative sign in (3.5) removes only double counting.  It cannot
cancel either one-shore branch.  On the legitimate boundary state
(S_-=\varnothing), it vanishes identically and (2.5) is unchanged.

## 4. Exact post-collar gap kernel

In this section we use the same repaired-spine regime as the audited
scalar no-go, namely (r=m+H+O(1)), and only
(H\le k<\min\{m,r-1\}).

There are two scalar gap coordinates along the physical spine:

\[
 g=m-k
 \quad\hbox{(remaining coordinate gap)},
 \qquad
 h=(H-k)_+
 \quad\hbox{(remaining unsaturated collar gap)}.
 \tag{4.0}
\]

Before collar saturation, a prescribed next coordinate must be placed
in both independent boundary orders.  After saturation, the complete
collar order has already been fixed and only the coordinate-gap order
continues.  Thus the exact aggregate kernels are

\[
 c_k=
 \begin{cases}
 \displaystyle {r-k-1\over r-k}{1\over m-k},&k<H,\\[2mm]
 \displaystyle {r-k-1\over r-k},&H\le k<m.
 \end{cases}
 \tag{4.0a}
\]

Resolving which shore owns the two gap endpoints partitions each row
of this kernel; it does not change its row sum.

Let (Gamma_k) be the normalized mass of an oriented consecutive
spine profile of order (k).  The audited physical formula is

\[
 \Gamma_k=
 {2(r-k)(m-k)!(m-H)!\over r(m!)^2},
 \qquad H\le k\le m.
 \tag{4.1}
\]

For one prescribed continuation,

\[
 {\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}{1\over m-k}.
 \tag{4.2}
\]

Write (g=m-k) for the remaining coordinate gap.  There are exactly
(g) admissible next coordinate continuations.  Resolve the catalogue
by

* orientation (+/-);
* the two-shore balance;
* the complete ordered gap state; and
* the next coordinate label.

This only partitions those (g) continuations.  If (K_k) is the
resulting nonnegative child matrix, every row therefore has sum

\[
 \sum_{\omega'}K_k(\omega,\omega')
 =g{\Gamma_{k+1}\over\Gamma_k}
 ={r-k-1\over r-k}=c_k.
 \tag{4.3}
\]

Consequently (K_k\mathbf1=c_k\mathbf1).  Reversal commutes with
(K_k), so its symmetric shore sector contains this common positive
eigenvector.  The antisymmetric sector may have cancellations, but a
nonnegative profile energy controlling both orientations must control
the symmetric vector.  Since (c_k\ge1/3) throughout the audited
post-collar range, resolving the gap and shore state does not restore a
contracting (O(1/m)) kernel.

The one-sided consecutive state is an exact counterstate to universal
shore compensation: choose the physical (+) spine and leave the
opposite shore increment empty.  Equations (3.5) and (4.3) show that its
entire (+1) transfer survives.  Adding its reversed copy changes this
to the symmetric vector ((1,1)), not to zero.

## 5. Carré-du-champ audit

Let (Z_+,Z_-) be any two stopped shore observables.  For an edge event
(e), let its two nonnegative decrements be denoted
Δ±ᴱ(e), and for a coin event (y), denote them by Δ±ᶜ(y).
The predictable covariance matrix is exactly

\[
 \Gamma_{\sigma\tau}
 =\nu\sum_e\Delta_\sigma^E(e)\Delta_\tau^E(e)
 +\sum_y\chi(y)
       \Delta_\sigma^\circ(y)\Delta_\tau^\circ(y),
 \qquad\sigma,\tau\in\{+,-\}.
 \tag{5.1}
\]

In particular Γ₊₋≥0.  For (Z_c=Z_++Z_-) and
(Z_d=Z_+-Z_-), bilinearity gives (0.7)--(0.8).

Thus a reversal-symmetric common event may disappear completely from
the difference mode, but then it contributes four times one-shore
variance to the common mode.  Conversely an event affecting only one
shore gives the same square in the common and difference modes.  If a
quadratic energy has positive-definite coefficient matrix (A), then

\[
 (\Delta_+,\Delta_-)A(\Delta_+,\Delta_-)^{\mathsf T}
 \ge\lambda_{\min}(A)(\Delta_+^2+\Delta_-^2),
 \tag{5.2}
\]

so it cannot erase the one-sided counterstate.  An indefinite signed
form can erase the common vector only by ceasing to dominate the
nonnegative shore mass and therefore cannot charge profile stops.

## 6. Exact boundary

Proved:

1. marginal compensation identity (1.4);
2. exact protected nonterminal hazard (0.1);
3. the literal (+1) and (+2)-or-higher split (0.2)--(0.3);
4. gap-dependent positive-correlation identity (0.5);
5. persistence of the order-one post-collar common mode (0.6); and
6. the common/difference carré-du-champ identities (0.7)--(0.8).

Therefore the proposed two-shore/gap compensation does not remove the
consecutive-spine obstruction.  This does not prove that the actual
trajectory has nonnegligible stopped profile incidence.  It rules out
only a universal shore cancellation based on marginal compensation and
the two-shore common/difference modes.  It also does not rule out a
highly anisotropic gap Lyapunov function which pays the common mode by a
separate terminal or trajectory drift.  The smallest remaining escapes
are:

* retain terminal-kill credits in an incidence-weighted global
  telescoping argument;
* prove a trajectory-specific finite cutoff before the collar; or
* add a richer state which records the selected-edge/common-event
  column responsible for (2.5), rather than only its two shores and
  gap.
